---
title: "src/deniable/deniable.c"
nav_title: "deniable.c"
---

# `src/deniable/deniable.c`

```c
/*
 * QR-NSP Volcanic Edition — Deniable Encryption Engine
 * Module 5: Multi-password hidden volumes + honey-encryption
 *
 * Key insight: the entire container is random bytes. Without the
 * correct password, an adversary cannot prove ANY volume exists.
 * Honey-encryption ensures that wrong passwords still yield output
 * that looks like real data, defeating brute-force triage.
 *
 * SPDX-License-Identifier: AGPL-3.0-or-later
 */

#include "qrnsp_deniable.h"
#include "qrnsp_aead.h"
#include "mlkem_params.h"  /* SHA3 wrappers */
#include <string.h>
#include <stdlib.h>
#include <stdio.h>

#if defined(__linux__)
#include <sys/random.h>
#endif

/* ─────────────────────────────────────────────
 * Entropy
 * ───────────────────────────────────────────── */

static int
secure_random(uint8_t *out, size_t len)
{
#if defined(__linux__)
    return (getrandom(out, len, 0) == (ssize_t)len) ? 0 : -1;
#else
    FILE *f = fopen("/dev/urandom", "rb");
    if (!f) return -1;
    size_t n = fread(out, 1, len, f);
    fclose(f);
    return (n == len) ? 0 : -1;
#endif
}

/* ─────────────────────────────────────────────
 * PBKDF2-SHA3-256
 *
 * HMAC-SHA3-256 based key derivation.
 * Deliberately slow to resist brute-force.
 *
 * For production: replace with Argon2id (memory-hard).
 * PBKDF2 is used here for zero-dependency compilation.
 * ───────────────────────────────────────────── */

/* HMAC-SHA3-256: H(K ⊕ opad || H(K ⊕ ipad || message)) */
static void
hmac_sha3_256(uint8_t out[32],
              const uint8_t *key, size_t key_len,
              const uint8_t *msg, size_t msg_len)
{
    uint8_t k_pad[136]; /* SHA3-256 block size = rate = 136 bytes */
    uint8_t ipad[136], opad[136];
    uint8_t inner_hash[32];

    /* If key > block size, hash it first */
    uint8_t k_derived[32];
    if (key_len > 136) {
        mlkem_hash_h(k_derived, key, key_len);
        key = k_derived;
        key_len = 32;
    }

    /* Pad key to block size */
    memset(k_pad, 0, 136);
    memcpy(k_pad, key, key_len);

    /* ipad = k_pad ⊕ 0x36, opad = k_pad ⊕ 0x5C */
    for (int i = 0; i < 136; i++) {
        ipad[i] = k_pad[i] ^ 0x36;
        opad[i] = k_pad[i] ^ 0x5C;
    }

    /* Inner hash: H(ipad || msg) */
    uint8_t *inner_buf = malloc(136 + msg_len);
    if (!inner_buf) { memset(out, 0, 32); return; }
    memcpy(inner_buf, ipad, 136);
    memcpy(inner_buf + 136, msg, msg_len);
    mlkem_hash_h(inner_hash, inner_buf, 136 + msg_len);
    free(inner_buf);

    /* Outer hash: H(opad || inner_hash) */
    uint8_t outer_buf[136 + 32];
    memcpy(outer_buf, opad, 136);
    memcpy(outer_buf + 136, inner_hash, 32);
    mlkem_hash_h(out, outer_buf, 136 + 32);

    memset(k_pad, 0, sizeof(k_pad));
    memset(ipad, 0, sizeof(ipad));
    memset(opad, 0, sizeof(opad));
    memset(inner_hash, 0, sizeof(inner_hash));
    memset(k_derived, 0, sizeof(k_derived));
}

/*
 * PBKDF2-HMAC-SHA3-256
 *
 * dk = T1 || T2 || ...
 * Ti = U1 ⊕ U2 ⊕ ... ⊕ Uc
 * U1 = HMAC(password, salt || INT(i))
 * Uj = HMAC(password, U_{j-1})
 */
static void
pbkdf2_sha3(uint8_t *dk, size_t dk_len,
             const uint8_t *password, size_t pass_len,
             const uint8_t *salt, size_t salt_len,
             uint32_t iterations)
{
    uint32_t block_count = (uint32_t)((dk_len + 31) / 32);
    uint8_t *salt_block = malloc(salt_len + 4);
    if (!salt_block) return;
    memcpy(salt_block, salt, salt_len);

    for (uint32_t i = 1; i <= block_count; i++) {
        /* salt || INT_32_BE(i) */
        salt_block[salt_len]     = (uint8_t)(i >> 24);
        salt_block[salt_len + 1] = (uint8_t)(i >> 16);
        salt_block[salt_len + 2] = (uint8_t)(i >> 8);
        salt_block[salt_len + 3] = (uint8_t)(i);

        uint8_t U[32], T[32];
        hmac_sha3_256(U, password, pass_len, salt_block, salt_len + 4);
        memcpy(T, U, 32);

        for (uint32_t j = 1; j < iterations; j++) {
            hmac_sha3_256(U, password, pass_len, U, 32);
            for (int k = 0; k < 32; k++) T[k] ^= U[k];
        }

        /* Copy block to output */
        size_t offset = (i - 1) * 32;
        size_t copy = (dk_len - offset < 32) ? dk_len - offset : 32;
        memcpy(dk + offset, T, copy);

        memset(U, 0, sizeof(U));
        memset(T, 0, sizeof(T));
    }

    memset(salt_block, 0, salt_len + 4);
    free(salt_block);
}

/* ─────────────────────────────────────────────
 * Key Derivation: password + salt → (key, nonce, volume_offset)
 *
 * We derive 76 bytes:
 *   key[32] || nonce[12] || volume_locator[32]
 *
 * volume_locator determines WHERE in the container this volume
 * lives. This is the key deniability property: without the password,
 * you don't know where to look, and every position looks random.
 * ───────────────────────────────────────────── */

#define KDF_OUTPUT_LEN  76

static void
derive_volume_params(uint8_t out[KDF_OUTPUT_LEN],
                     const char *password, size_t pass_len,
                     const uint8_t salt[DENY_SALT_BYTES],
                     uint32_t iterations)
{
    pbkdf2_sha3(out, KDF_OUTPUT_LEN,
                (const uint8_t *)password, pass_len,
                salt, DENY_SALT_BYTES,
                iterations);
}

/*
 * Compute volume offset within container from the locator.
 * Maps 32-byte locator to an offset in [header_end, container_end - volume_size]
 */
static size_t
compute_volume_offset(const uint8_t locator[32],
                      size_t container_size,
                      size_t header_size,
                      size_t volume_size)
{
    /* Use first 8 bytes of locator as uint64, modulo available space */
    uint64_t loc = 0;
    for (int i = 0; i < 8; i++)
        loc |= ((uint64_t)locator[i]) << (i * 8);

    size_t available = container_size - header_size - volume_size;
    if (available == 0) return header_size;

    /* Align to 16-byte boundary for cache friendliness */
    size_t offset = header_size + (size_t)(loc % available);
    offset &= ~(size_t)0xF;
    if (offset < header_size) offset = header_size;
    if (offset + volume_size > container_size)
        offset = container_size - volume_size;

    return offset;
}

/* ─────────────────────────────────────────────
 * Honey-Encryption: Distribution-Transforming Encoder
 *
 * Maps any AES-GCM "decryption" (which produces random-looking
 * bytes for wrong keys) through a DTE that outputs text matching
 * a target distribution.
 *
 * Approach: use the "decrypted" bytes as a seed for a Markov chain
 * generator. The output looks like English/JSON/code regardless of
 * whether the key was correct.
 * ───────────────────────────────────────────── */

/* Simple order-1 character-level English Markov chain.
 * Transition table: given prev char class, emit next char.
 * 5 classes: vowel(0), consonant(1), space(2), punctuation(3), digit(4) */

static const char vowels[]     = "aeiouy";
static const char consonants[] = "bcdfghjklmnpqrstvwxz";
static const char spaces[]     = " ";
static const char punct[]      = ".,;:!?'-";
static const char digits[]     = "0123456789";

/* Transition probabilities (simplified, 5×5 matrix as cumulative %) */
/* Rows: current class, Cols: next class threshold */
static const uint8_t english_transitions[5][5] = {
    /* From vowel:     vowel  cons  space  punct  digit */
    {   15,   80,   95,   100,  100 },  /* Mostly consonants after vowels */
    /* From consonant: */
    {   55,   75,   93,    99,  100 },  /* Mostly vowels after consonants */
    /* From space:     */
    {   20,   78,   80,    82,  100 },  /* Start of word: cons > vowel */
    /* From punct:     */
    {   10,   20,   90,    92,  100 },  /* Space after punctuation */
    /* From digit:     */
    {    5,   10,   40,    45,  100 },  /* More digits after digits */
};

static int
char_class(char c)
{
    if (c >= 'a' && c <= 'z') {
        if (c=='a'||c=='e'||c=='i'||c=='o'||c=='u'||c=='y') return 0;
        return 1;
    }
    if (c == ' ' || c == '\n') return 2;
    if (c >= '0' && c <= '9') return 4;
    return 3;
}

static char
pick_char(int class_id, uint8_t random_byte)
{
    /* Map random byte to character within the class */
    switch (class_id) {
    case 0: return vowels[random_byte % 6];
    case 1: return consonants[random_byte % 20];
    case 2: return ' ';
    case 3: return punct[random_byte % 8];
    case 4: return digits[random_byte % 10];
    default: return ' ';
    }
}

static void
honey_generate_english(uint8_t *out, size_t len, const uint8_t *seed, size_t seed_len)
{
    int prev_class = 2; /* Start as if after space */
    size_t si = 0;
    uint8_t word_len = 0;

    for (size_t i = 0; i < len; i++) {
        /* Use seed bytes as entropy source */
        uint8_t r = seed[si % seed_len];
        si++;
        uint8_t r2 = seed[si % seed_len];
        si++;

        /* Pick next class based on transition table */
        uint8_t pct = r % 100;
        int next_class = 4;
        for (int c = 0; c < 5; c++) {
            if (pct < english_transitions[prev_class][c]) {
                next_class = c;
                break;
            }
        }

        /* Force word boundaries (no words > 12 chars) */
        if (next_class <= 1) {
            word_len++;
            if (word_len > 3 + (r2 % 10)) {
                next_class = 2;
                word_len = 0;
            }
        } else {
            word_len = 0;
        }

        /* Capitalize after period+space */
        char c = pick_char(next_class, r2);
        if (i > 1 && out[i-1] == ' ' && i > 2 &&
            (out[i-2] == '.' || out[i-2] == '!' || out[i-2] == '?')) {
            if (c >= 'a' && c <= 'z') c -= 32;
        }
        /* Capitalize first character */
        if (i == 0 && c >= 'a' && c <= 'z') c -= 32;

        out[i] = (uint8_t)c;
        prev_class = char_class(c);
    }
}

static void
honey_generate_json(uint8_t *out, size_t len, const uint8_t *seed, size_t seed_len)
{
    /* Generate valid-looking JSON */
    const char *keys[] = {"id","name","email","status","count","active","type","value"};
    const char *vals[] = {"null","true","false","42","\"pending\"","\"ok\"","0.5","[]"};
    int nkeys = 8;

    size_t pos = 0;
    size_t si = 0;

    if (pos < len) out[pos++] = '{';

    int first = 1;
    while (pos + 30 < len) {
        if (!first && pos < len) out[pos++] = ',';
        first = 0;

        uint8_t r = seed[si++ % seed_len];
        const char *k = keys[r % nkeys];
        const char *v = vals[seed[si++ % seed_len] % nkeys];

        if (pos < len) out[pos++] = '"';
        for (const char *p = k; *p && pos < len; p++) out[pos++] = (uint8_t)*p;
        if (pos < len) out[pos++] = '"';
        if (pos < len) out[pos++] = ':';
        for (const char *p = v; *p && pos < len; p++) out[pos++] = (uint8_t)*p;
    }

    if (pos < len) out[pos++] = '}';
    while (pos < len) out[pos++] = ' '; /* Pad with spaces */
}

static void
honey_generate(uint8_t *out, size_t len,
               const uint8_t *seed, size_t seed_len,
               honey_dist_t dist)
{
    switch (dist) {
    case HONEY_DIST_ENGLISH_TEXT:
        honey_generate_english(out, len, seed, seed_len);
        break;
    case HONEY_DIST_JSON:
        honey_generate_json(out, len, seed, seed_len);
        break;
    case HONEY_DIST_CODE:
        /* Use English generator with different character distribution */
        honey_generate_english(out, len, seed, seed_len);
        /* Sprinkle code-like characters */
        for (size_t i = 0; i < len; i++) {
            if (seed[i % seed_len] < 10) out[i] = '{';
            else if (seed[i % seed_len] < 20) out[i] = '}';
            else if (seed[i % seed_len] < 25) out[i] = '(';
            else if (seed[i % seed_len] < 30) out[i] = ')';
            else if (seed[i % seed_len] < 33) out[i] = ';';
            else if (seed[i % seed_len] < 36) out[i] = '=';
        }
        break;
    case HONEY_DIST_CSV:
        /* Generate CSV-like rows */
        {
            size_t pos = 0;
            size_t si = 0;
            while (pos < len) {
                /* 3-6 fields per row */
                int fields = 3 + (seed[si++ % seed_len] % 4);
                for (int f = 0; f < fields && pos < len; f++) {
                    if (f > 0 && pos < len) out[pos++] = ',';
                    int flen = 2 + (seed[si++ % seed_len] % 8);
                    for (int c = 0; c < flen && pos < len; c++) {
                        uint8_t r = seed[si++ % seed_len];
                        if (r < 100) out[pos++] = '0' + (r % 10);
                        else out[pos++] = 'a' + (r % 26);
                    }
                }
                if (pos < len) out[pos++] = '\n';
            }
        }
        break;
    case HONEY_DIST_BINARY:
    default:
        /* Just use raw seed bytes — looks like encrypted/compressed data */
        for (size_t i = 0; i < len; i++)
            out[i] = seed[i % seed_len];
        break;
    }
}

/* ═════════════════════════════════════════════
 * Seal: create multi-volume deniable container
 * ═════════════════════════════════════════════ */

size_t
deny_required_size(const deny_volume_t *volumes, int n_volumes)
{
    size_t total = DENY_SALT_BYTES; /* Salt at start */

    for (int i = 0; i < n_volumes; i++) {
        total += DENY_VOLUME_OVERHEAD + volumes[i].plaintext_len;
    }

    /* Add 50% padding for deniability (volumes shouldn't fill container) */
    total = total * 3 / 2;

    /* Round up to 4K boundary */
    total = (total + 4095) & ~(size_t)4095;
    if (total < DENY_CONTAINER_4K) total = DENY_CONTAINER_4K;

    return total;
}

deny_result_t
deny_seal(const deny_volume_t *volumes, int n_volumes,
          deny_container_t *container)
{
    if (n_volumes < 1 || n_volumes > DENY_MAX_PASSWORDS)
        return DENY_ERR_TOO_MANY_VOLUMES;

    size_t cap = container->capacity;

    /* Check capacity */
    size_t needed = DENY_SALT_BYTES;
    for (int i = 0; i < n_volumes; i++)
        needed += DENY_VOLUME_OVERHEAD + volumes[i].plaintext_len;
    if (needed > cap)
        return DENY_ERR_CAPACITY;

    uint8_t *buf = container->data;

    /* ── Step 1: Fill entire container with random bytes ── */
    /* This is critical: every byte must be random BEFORE writing volumes.
     * After seal, the container is random + encrypted volumes (also random).
     * An adversary cannot distinguish volume regions from padding. */
    if (secure_random(buf, cap) != 0)
        return DENY_ERR_KDF;

    /* ── Step 2: Write salt (first 32 bytes) ── */
    /* Salt is already random from step 1 — this is the public part */
    uint8_t *salt = buf;
    /* (salt stays as-is from the random fill) */

    /* ── Step 3: For each volume, derive key and write encrypted data ── */
    for (int v = 0; v < n_volumes; v++) {
        /* Derive key + nonce + locator from password */
        uint8_t kdf_out[KDF_OUTPUT_LEN];
        derive_volume_params(kdf_out,
                             volumes[v].password, volumes[v].password_len,
                             salt, DENY_KDF_ITERATIONS);

        uint8_t *vol_key   = kdf_out;       /* 32 bytes */
        uint8_t *vol_nonce = kdf_out + 32;   /* 12 bytes */
        uint8_t *locator   = kdf_out + 44;   /* 32 bytes */

        /* Compute volume size and offset */
        size_t vol_size = DENY_VOLUME_OVERHEAD + volumes[v].plaintext_len;
        size_t vol_offset = compute_volume_offset(locator, cap,
                                                  DENY_SALT_BYTES, vol_size);

        /* ── Write volume: [nonce:12][length:4][ciphertext:N][tag:16] ── */
        uint8_t *dst = buf + vol_offset;

        /* Nonce (from KDF, not random — deterministic for reproducibility) */
        memcpy(dst, vol_nonce, DENY_NONCE_BYTES);
        dst += DENY_NONCE_BYTES;

        /* Plaintext length (big-endian, 4 bytes) */
        uint32_t pt_len = (uint32_t)volumes[v].plaintext_len;
        uint8_t len_bytes[4] = {
            (uint8_t)(pt_len >> 24), (uint8_t)(pt_len >> 16),
            (uint8_t)(pt_len >> 8),  (uint8_t)(pt_len)
        };

        /* Encrypt: plaintext = length_prefix || actual_plaintext */
        uint8_t *pt_buf = malloc(4 + pt_len);
        if (!pt_buf) { memset(kdf_out, 0, sizeof(kdf_out)); return DENY_ERR_ENCRYPT; }
        memcpy(pt_buf, len_bytes, 4);
        memcpy(pt_buf + 4, volumes[v].plaintext, pt_len);

        uint8_t tag[DENY_TAG_BYTES];

        /* AAD = salt (binds volume to this container) */
        if (aead_encrypt(dst, tag, pt_buf, 4 + pt_len,
                         salt, DENY_SALT_BYTES,
                         vol_nonce, vol_key) != 0) {
            free(pt_buf);
            memset(kdf_out, 0, sizeof(kdf_out));
            return DENY_ERR_ENCRYPT;
        }

        dst += 4 + pt_len;
        memcpy(dst, tag, DENY_TAG_BYTES);

        free(pt_buf);
        memset(kdf_out, 0, sizeof(kdf_out));
    }

    container->used = cap;
    return DENY_OK;
}

/* ═════════════════════════════════════════════
 * Open: attempt to decrypt a volume
 * ═════════════════════════════════════════════ */

deny_result_t
deny_open(const deny_container_t *container,
          const char *password, size_t pass_len,
          uint8_t *out, size_t out_cap,
          size_t *out_len)
{
    *out_len = 0;
    const uint8_t *buf = container->data;
    size_t cap = container->capacity;
    const uint8_t *salt = buf;

    /* Derive key + nonce + locator */
    uint8_t kdf_out[KDF_OUTPUT_LEN];
    derive_volume_params(kdf_out, password, pass_len,
                         salt, DENY_KDF_ITERATIONS);

    uint8_t *vol_key   = kdf_out;
    uint8_t *vol_nonce = kdf_out + 32;
    uint8_t *locator   = kdf_out + 44;

    /*
     * Try multiple possible volume sizes. Since we don't store the
     * volume size anywhere (that would leak metadata), we try
     * plausible sizes from the computed offset.
     *
     * Strategy: read nonce from the computed offset, then try
     * decrypting increasing payload sizes until auth succeeds or
     * we exceed the container.
     */

    /* Maximum possible volume from this offset */
    size_t max_vol = cap - DENY_SALT_BYTES;

    /* Try the most likely location first */
    for (size_t try_pt_len = 4; try_pt_len <= max_vol && try_pt_len <= out_cap + 64; try_pt_len++) {
        size_t vol_size = DENY_NONCE_BYTES + try_pt_len + DENY_TAG_BYTES;
        size_t vol_offset = compute_volume_offset(locator, cap,
                                                  DENY_SALT_BYTES, vol_size);

        if (vol_offset + vol_size > cap) continue;

        const uint8_t *src = buf + vol_offset;
        const uint8_t *ct_nonce = src;
        const uint8_t *ct = src + DENY_NONCE_BYTES;
        const uint8_t *tag = src + DENY_NONCE_BYTES + try_pt_len;

        /* Verify nonce matches our derived nonce (quick reject) */
        if (memcmp(ct_nonce, vol_nonce, DENY_NONCE_BYTES) != 0)
            continue;

        /* Attempt decryption */
        uint8_t *pt_buf = malloc(try_pt_len);
        if (!pt_buf) continue;

        int ret = aead_decrypt(pt_buf, ct, try_pt_len, tag,
                               salt, DENY_SALT_BYTES,
                               vol_nonce, vol_key);

        if (ret == 0) {
            /* Authentication succeeded! Parse length prefix. */
            uint32_t real_len = ((uint32_t)pt_buf[0] << 24) |
                                ((uint32_t)pt_buf[1] << 16) |
                                ((uint32_t)pt_buf[2] << 8)  |
                                ((uint32_t)pt_buf[3]);

            if (real_len <= try_pt_len - 4 && real_len <= out_cap) {
                memcpy(out, pt_buf + 4, real_len);
                *out_len = real_len;
                free(pt_buf);
                memset(kdf_out, 0, sizeof(kdf_out));
                return DENY_OK;
            }
        }

        free(pt_buf);
    }

    /* ── No volume found — generate honey-encrypted plausible output ── */
    /*
     * This is the deniability guarantee: wrong passwords don't return
     * "error", they return convincing fake data.
     *
     * We use the derived key as a seed for the honey generator.
     * Different wrong passwords → different plausible outputs.
     */
    size_t honey_len = 64 + (kdf_out[0] % 192); /* Variable plausible length */
    if (honey_len > out_cap) honey_len = out_cap;

    honey_generate(out, honey_len, kdf_out, KDF_OUTPUT_LEN, HONEY_DIST_ENGLISH_TEXT);
    *out_len = honey_len;

    memset(kdf_out, 0, sizeof(kdf_out));
    return DENY_ERR_HONEY;
}

/* ═════════════════════════════════════════════
 * Probe (timing-sensitive — use carefully)
 * ═════════════════════════════════════════════ */

int
deny_probe(const deny_container_t *container,
           const char *password, size_t pass_len)
{
    uint8_t tmp[1024];
    size_t tmp_len;
    deny_result_t r = deny_open(container, password, pass_len,
                                tmp, sizeof(tmp), &tmp_len);
    memset(tmp, 0, sizeof(tmp));
    return (r == DENY_OK) ? 1 : 0;
}

```
