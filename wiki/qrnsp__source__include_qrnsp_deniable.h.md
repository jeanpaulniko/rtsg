---
title: "include/qrnsp_deniable.h"
nav_title: "qrnsp_deniable.h"
---

# `include/qrnsp_deniable.h`

```c
/*
 * QR-NSP Volcanic Edition — Deniable Encryption
 * Module 5: Multi-password KDF + Honey-Encryption
 *
 * Threat model:
 *   An adversary captures the device AND coerces the user to reveal
 *   the password ("rubber-hose cryptanalysis"). The user surrenders
 *   the DECOY password. The adversary decrypts and finds plausible
 *   but harmless data. The TRUE payload remains hidden.
 *
 * Architecture:
 *
 *   ┌─────────────────────────────────────────────────────────┐
 *   │                    Sealed Container                      │
 *   ├──────────┬──────────┬────────────┬──────────────────────┤
 *   │ SALT:32  │ DECOY_CT │  REAL_CT   │  HONEY_PAD           │
 *   │          │ (N bytes)│  (M bytes) │  (fills to capacity)  │
 *   ├──────────┴──────────┴────────────┴──────────────────────┤
 *   │            Entire container looks like random bytes       │
 *   └─────────────────────────────────────────────────────────┘
 *
 *   Password A (decoy)  → derives key_A → decrypts DECOY_CT → plausible data
 *   Password B (real)   → derives key_B → decrypts REAL_CT  → secret payload
 *   Any other password  → derives key_X → honey-decrypt → valid-looking garbage
 *
 * Properties:
 *   1. Without the correct password, you can't prove REAL_CT even EXISTS
 *      (it's indistinguishable from HONEY_PAD random bytes)
 *   2. Decoy data is user-chosen (e.g., innocent photos, diary entries)
 *   3. Honey-encryption ensures brute-force yields plausible plaintexts
 *   4. Container size is fixed — no metadata leaks payload sizes
 *
 * SPDX-License-Identifier: AGPL-3.0-or-later
 */

#ifndef QRNSP_DENIABLE_H
#define QRNSP_DENIABLE_H

#include <stdint.h>
#include <stddef.h>

/* ─────────────────────────────────────────────
 * Container parameters
 * ───────────────────────────────────────────── */

#define DENY_SALT_BYTES       32
#define DENY_KEY_BYTES        32      /* AES-256 key                     */
#define DENY_NONCE_BYTES      12      /* AES-GCM nonce                   */
#define DENY_TAG_BYTES        16      /* AES-GCM auth tag                */
#define DENY_KDF_ITERATIONS   100000  /* PBKDF2 iterations (tune for HW) */

/* Per-volume overhead: nonce(12) + length(4) + tag(16) = 32 bytes */
#define DENY_VOLUME_OVERHEAD  (DENY_NONCE_BYTES + 4 + DENY_TAG_BYTES)

/* Container header: salt(32) + decoy_offset(4) + real_offset(4) = 40 bytes
 * NOTE: offsets are encrypted under a header key derived from a third
 * "structure password" to prevent offset metadata from revealing volume layout.
 * Without the structure key, offsets are indistinguishable from random. */
#define DENY_HEADER_BYTES     (DENY_SALT_BYTES + 8 + DENY_TAG_BYTES) /* 56 */

/* Default container sizes */
#define DENY_CONTAINER_4K     4096
#define DENY_CONTAINER_64K    65536
#define DENY_CONTAINER_1M     1048576

/* Maximum passwords supported */
#define DENY_MAX_PASSWORDS    4

/* ─────────────────────────────────────────────
 * Honey-Encryption: Distribution-Transforming Encoder (DTE)
 *
 * Maps any 256-bit key to a plausible plaintext from a target
 * distribution. When an adversary brute-forces the container,
 * EVERY attempted key yields something that looks like real data.
 *
 * Supported honey distributions:
 * ───────────────────────────────────────────── */

typedef enum {
    HONEY_DIST_ENGLISH_TEXT,    /* Markov-chain English prose           */
    HONEY_DIST_JSON,            /* Valid JSON objects                   */
    HONEY_DIST_BINARY,          /* Random-looking binary (uniform)      */
    HONEY_DIST_CODE,            /* Source code snippets                 */
    HONEY_DIST_CSV,             /* CSV data rows                       */
} honey_dist_t;

/* ─────────────────────────────────────────────
 * Volume descriptor
 * ───────────────────────────────────────────── */

typedef struct {
    const char  *password;       /* Null-terminated password            */
    size_t       password_len;

    const uint8_t *plaintext;    /* Data for this volume                */
    size_t         plaintext_len;

    honey_dist_t   honey_type;   /* Distribution for honey-encryption   */
} deny_volume_t;

/* ─────────────────────────────────────────────
 * Sealed container (opaque output)
 * ───────────────────────────────────────────── */

typedef struct {
    uint8_t *data;               /* Container bytes (caller allocates)  */
    size_t   capacity;           /* Total container size                */
    size_t   used;               /* Bytes written so far                */
} deny_container_t;

/* ─────────────────────────────────────────────
 * Seal result
 * ───────────────────────────────────────────── */

typedef enum {
    DENY_OK = 0,
    DENY_ERR_CAPACITY,           /* Container too small for payloads    */
    DENY_ERR_TOO_MANY_VOLUMES,   /* Exceeded MAX_PASSWORDS              */
    DENY_ERR_KDF,                /* Key derivation failed               */
    DENY_ERR_ENCRYPT,            /* AEAD encryption failed              */
    DENY_ERR_DECRYPT,            /* AEAD decryption failed              */
    DENY_ERR_NO_VOLUME,          /* Password doesn't match any volume   */
    DENY_ERR_HONEY,              /* Honey decryption (still returns data)*/
} deny_result_t;

/* ─────────────────────────────────────────────
 * API
 * ───────────────────────────────────────────── */

/*
 * Seal: create a deniable container with multiple volumes.
 *
 * volumes:    array of volume descriptors (1 to MAX_PASSWORDS)
 * n_volumes:  number of volumes
 * container:  output container (caller must set .data and .capacity)
 *
 * The container is filled entirely — unused space is honey-encrypted
 * random data, indistinguishable from real volumes.
 *
 * Returns DENY_OK on success.
 */
deny_result_t deny_seal(const deny_volume_t *volumes, int n_volumes,
                        deny_container_t *container);

/*
 * Open: attempt to decrypt a volume from a container.
 *
 * container:  sealed container
 * password:   password to try
 * pass_len:   password length
 * out:        output buffer for decrypted plaintext
 * out_cap:    output buffer capacity
 * out_len:    actual plaintext length (set on success)
 *
 * Returns:
 *   DENY_OK       — valid volume decrypted
 *   DENY_ERR_HONEY — no matching volume; honey-decryption returned
 *                     plausible-looking data in out[] (this is BY DESIGN)
 *
 * CRITICAL: The caller CANNOT distinguish DENY_OK from DENY_ERR_HONEY
 * without knowing the true password. This is the deniability property.
 * We return different codes only for the API user who knows the truth.
 */
deny_result_t deny_open(const deny_container_t *container,
                        const char *password, size_t pass_len,
                        uint8_t *out, size_t out_cap,
                        size_t *out_len);

/*
 * Probe: check if a password matches any volume (without full decrypt).
 * Returns 1 if a volume's authentication tag validates, 0 otherwise.
 *
 * WARNING: timing side-channel — use only when the adversary is not
 * watching. For coercion scenarios, always use deny_open() which
 * always returns data regardless of password validity.
 */
int deny_probe(const deny_container_t *container,
               const char *password, size_t pass_len);

/*
 * Compute required container size for given volumes.
 */
size_t deny_required_size(const deny_volume_t *volumes, int n_volumes);

#endif /* QRNSP_DENIABLE_H */

```
