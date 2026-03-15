---
title: "src/orchestrator/orchestrator.c"
nav_title: "orchestrator.c"
---

# `src/orchestrator/orchestrator.c`

```c
/*
 * QR-NSP Volcanic Edition — Unified Orchestrator
 * Module 8: Pipeline controller
 *
 * SPDX-License-Identifier: AGPL-3.0-or-later
 */

#include "qrnsp_orchestrator.h"
#include "qrnsp_aead.h"
#include "mlkem_params.h"
#include <string.h>
#include <stdlib.h>

/* ═════════════════════════════════════════════
 * Init
 * ═════════════════════════════════════════════ */

int
orch_init(orch_session_t *sess, int role, morph_cover_t cover)
{
    memset(sess, 0, sizeof(*sess));
    sess->role = role;
    sess->state = ORCH_STATE_INIT;

    /* Generate our keypair */
    if (hybrid_keypair_generate(sess->pk, sess->sk) != 0)
        return -1;

    /* Pre-init morph with a temp seed (re-seeded after KEM) */
    uint8_t temp_seed[32] = {0};
    morph_init(&sess->morph, cover, temp_seed);
    sess->morph.active = 0; /* Inactive until handshake completes */

    sess->cover_interval_ns = 100000000ULL; /* 100ms default */
    sess->next_msg_id = 1;

    return 0;
}

int
orch_get_pubkey(const orch_session_t *sess,
                uint8_t pk[QRNSP_CRYPTO_PUBLICKEYBYTES])
{
    memcpy(pk, sess->pk, QRNSP_CRYPTO_PUBLICKEYBYTES);
    return 0;
}

/* ═════════════════════════════════════════════
 * Handshake: KEM exchange → derive all session keys
 * ═════════════════════════════════════════════ */

int
orch_handshake(orch_session_t *sess,
               const uint8_t peer_pk[QRNSP_CRYPTO_PUBLICKEYBYTES],
               uint8_t ct[QRNSP_CRYPTO_CIPHERTEXTBYTES],
               int is_ciphertext)
{
    memcpy(sess->peer_pk, peer_pk, QRNSP_CRYPTO_PUBLICKEYBYTES);
    sess->state = ORCH_STATE_HANDSHAKE;

    if (!is_ciphertext) {
        /* We are initiator: encapsulate to peer's pk */
        if (hybrid_encapsulate(ct, sess->shared_secret, peer_pk) != 0)
            return -1;
    } else {
        /* We are responder: decapsulate from received ct */
        if (hybrid_decapsulate(sess->shared_secret, ct, sess->sk, sess->pk) != 0)
            return -1;
    }

    sess->kem_complete = 1;

    /* ── Initialize all sub-modules with the shared secret ── */

    /* Module 3: QUIC steganography */
    stego_session_init(&sess->stego, sess->shared_secret, sess->role);

    /* Module 4: Jitter channel */
    jitter_tx_init(&sess->jitter_tx, sess->shared_secret);
    jitter_rx_init(&sess->jitter_rx, sess->shared_secret);

    /* Module 6: TCP fallback */
    fallback_init(&sess->fallback, sess->shared_secret);

    /* Module 7: Re-seed morph with real shared secret */
    morph_init(&sess->morph, sess->morph.profile.type, sess->shared_secret);
    sess->morph.active = 1;

    /* Set initial capabilities */
    sess->capabilities = ORCH_CAP_QUIC_PADDING | ORCH_CAP_JITTER;
    sess->state = ORCH_STATE_ACTIVE;

    return 0;
}

/* ═════════════════════════════════════════════
 * Chunking: split messages into packet-sized pieces
 * ═════════════════════════════════════════════ */

static int
chunk_message(const uint8_t *msg, size_t msg_len,
              uint32_t msg_id, size_t max_chunk_data,
              orch_chunk_t *chunks, int max_chunks)
{
    if (max_chunk_data > 1400) max_chunk_data = 1400;
    if (msg_len == 0) return 0;

    uint16_t total = (uint16_t)((msg_len + max_chunk_data - 1) / max_chunk_data);
    if (total > max_chunks) return -1;

    for (uint16_t i = 0; i < total; i++) {
        chunks[i].msg_id = msg_id;
        chunks[i].chunk_index = i;
        chunks[i].total_chunks = total;

        size_t offset = (size_t)i * max_chunk_data;
        size_t remaining = msg_len - offset;
        chunks[i].data_len = (uint16_t)(remaining < max_chunk_data ?
                                         remaining : max_chunk_data);
        memcpy(chunks[i].data, msg + offset, chunks[i].data_len);
    }

    return (int)total;
}

/* Serialize chunk header + data into a buffer */
static size_t
serialize_chunk(const orch_chunk_t *c, uint8_t *buf)
{
    /* [MSG_ID:4][CHUNK:2][TOTAL:2][DATA:N] */
    buf[0] = (uint8_t)(c->msg_id >> 24);
    buf[1] = (uint8_t)(c->msg_id >> 16);
    buf[2] = (uint8_t)(c->msg_id >> 8);
    buf[3] = (uint8_t)(c->msg_id);
    buf[4] = (uint8_t)(c->chunk_index >> 8);
    buf[5] = (uint8_t)(c->chunk_index);
    buf[6] = (uint8_t)(c->total_chunks >> 8);
    buf[7] = (uint8_t)(c->total_chunks);
    memcpy(buf + ORCH_CHUNK_HEADER, c->data, c->data_len);
    return ORCH_CHUNK_HEADER + c->data_len;
}

static int
deserialize_chunk(const uint8_t *buf, size_t len, orch_chunk_t *c)
{
    if (len < ORCH_CHUNK_HEADER) return -1;

    c->msg_id      = ((uint32_t)buf[0] << 24) | ((uint32_t)buf[1] << 16) |
                     ((uint32_t)buf[2] << 8) | buf[3];
    c->chunk_index = ((uint16_t)buf[4] << 8) | buf[5];
    c->total_chunks= ((uint16_t)buf[6] << 8) | buf[7];
    c->data_len    = (uint16_t)(len - ORCH_CHUNK_HEADER);
    if (c->data_len > sizeof(c->data)) return -1;
    memcpy(c->data, buf + ORCH_CHUNK_HEADER, c->data_len);
    return 0;
}

/* ═════════════════════════════════════════════
 * Send: message → chunk → encrypt → inject → morph → packets
 * ═════════════════════════════════════════════ */

int
orch_send(orch_session_t *sess,
          const uint8_t *msg, size_t msg_len,
          uint8_t packets[][2048], size_t *pkt_sizes,
          uint64_t *pkt_delays, int max_pkts, int *n_pkts)
{
    if (sess->state != ORCH_STATE_ACTIVE &&
        sess->state != ORCH_STATE_FALLBACK)
        return -1;

    *n_pkts = 0;

    /* Determine max chunk payload based on available stego capacity */
    size_t max_chunk_data = 1024; /* Conservative default */

    /* Chunk the message */
    orch_chunk_t chunks[256];
    int nchunks = chunk_message(msg, msg_len, sess->next_msg_id++,
                                max_chunk_data, chunks, 256);
    if (nchunks < 0) return -1;
    if (nchunks > max_pkts) return -1;

    /* Process each chunk */
    for (int i = 0; i < nchunks && *n_pkts < max_pkts; i++) {
        /* Serialize chunk */
        uint8_t chunk_buf[1500];
        size_t chunk_len = serialize_chunk(&chunks[i], chunk_buf);

        /* Determine morphed packet size and delay */
        size_t target_size;
        uint64_t delay_ns;
        morph_shape(&sess->morph, chunk_len + 64, &target_size, &delay_ns);

        /* Build output packet: for now, chunk_buf IS the payload.
         * In production, this would be injected into a QUIC PADDING
         * region of a real cover traffic packet. */
        if (target_size > 2048) target_size = 2048;
        memset(packets[*n_pkts], 0, target_size);
        memcpy(packets[*n_pkts], chunk_buf, chunk_len);

        /* Pad to target size */
        morph_pad(&sess->morph, packets[*n_pkts], chunk_len, target_size);

        pkt_sizes[*n_pkts] = target_size;
        pkt_delays[*n_pkts] = delay_ns;

        morph_record_tx(&sess->morph, target_size, 0 /* timestamp filled by caller */);

        sess->chunks_sent++;
        (*n_pkts)++;
    }

    sess->msgs_sent++;
    sess->bytes_sent += msg_len;

    return 0;
}

/* ═════════════════════════════════════════════
 * Receive: packet → extract → dechunk → reassemble
 * ═════════════════════════════════════════════ */

static orch_reassembly_t *
find_or_create_reassembly(orch_session_t *sess, uint32_t msg_id, uint16_t total)
{
    /* Find existing */
    for (int i = 0; i < sess->reassembly_count; i++) {
        if (sess->reassembly[i].msg_id == msg_id)
            return &sess->reassembly[i];
    }

    /* Create new */
    if (sess->reassembly_count >= 4) {
        /* Evict oldest */
        if (sess->reassembly[0].buffer)
            free(sess->reassembly[0].buffer);
        memmove(&sess->reassembly[0], &sess->reassembly[1],
                3 * sizeof(orch_reassembly_t));
        sess->reassembly_count = 3;
    }

    orch_reassembly_t *r = &sess->reassembly[sess->reassembly_count++];
    memset(r, 0, sizeof(*r));
    r->msg_id = msg_id;
    r->total_chunks = total;
    r->buffer_size = (size_t)total * 1400;
    r->buffer = calloc(1, r->buffer_size);

    return r;
}

int
orch_receive(orch_session_t *sess,
             const uint8_t *pkt, size_t pkt_len,
             uint64_t timestamp_ns)
{
    if (!sess->kem_complete) return -1;

    /* Try QUIC PADDING extraction first */
    uint8_t extracted[2048];
    size_t extracted_len = 0;
    int found = 0;

    if (sess->capabilities & ORCH_CAP_QUIC_PADDING) {
        stego_result_t sr = stego_extract(&sess->stego, pkt, pkt_len,
                                          extracted, sizeof(extracted),
                                          &extracted_len);
        if (sr == STEGO_OK) found = 1;
    }

    /* Feed to jitter receiver regardless */
    if (sess->capabilities & ORCH_CAP_JITTER) {
        jitter_rx_feed(&sess->jitter_rx, timestamp_ns);
    }

    /* Update fallback metrics */
    fallback_quic_rx(&sess->fallback, timestamp_ns);

    if (!found) return -1; /* Not a QR-NSP packet */

    /* Deserialize chunk */
    orch_chunk_t chunk;
    if (deserialize_chunk(extracted, extracted_len, &chunk) != 0)
        return -1;

    sess->chunks_received++;

    /* Reassemble */
    orch_reassembly_t *r = find_or_create_reassembly(
        sess, chunk.msg_id, chunk.total_chunks);
    if (!r || !r->buffer) return -1;

    /* Store chunk */
    size_t offset = (size_t)chunk.chunk_index * 1400;
    if (offset + chunk.data_len <= r->buffer_size) {
        memcpy(r->buffer + offset, chunk.data, chunk.data_len);

        /* Mark received */
        int word = chunk.chunk_index / 16;
        int bit  = chunk.chunk_index % 16;
        if (word < 64) {
            if (!(r->received_mask[word] & (1 << bit))) {
                r->received_mask[word] |= (1 << bit);
                r->chunks_received++;
            }
        }

        if (r->first_chunk_ns == 0)
            r->first_chunk_ns = timestamp_ns;
    }

    /* Check if message is complete */
    if (r->chunks_received >= r->total_chunks) {
        sess->msgs_received++;
        return 1; /* Message complete */
    }

    return 0; /* Still assembling */
}

int
orch_recv_msg(orch_session_t *sess,
              uint8_t *out, size_t out_cap, size_t *out_len)
{
    /* Find a completed message */
    for (int i = 0; i < sess->reassembly_count; i++) {
        orch_reassembly_t *r = &sess->reassembly[i];
        if (r->chunks_received >= r->total_chunks && r->buffer) {
            size_t total_len = (size_t)r->total_chunks * 1400;
            /* Actual length may be less (last chunk smaller) */
            if (total_len > out_cap) total_len = out_cap;
            memcpy(out, r->buffer, total_len);
            *out_len = total_len;

            sess->bytes_received += total_len;

            /* Free reassembly slot */
            free(r->buffer);
            r->buffer = NULL;
            memmove(&sess->reassembly[i], &sess->reassembly[i+1],
                    (sess->reassembly_count - i - 1) * sizeof(orch_reassembly_t));
            sess->reassembly_count--;

            return 0;
        }
    }
    return -1;
}

/* ═════════════════════════════════════════════
 * Tick: periodic maintenance
 * ═════════════════════════════════════════════ */

int
orch_tick(orch_session_t *sess, uint64_t now_ns)
{
    if (sess->state < ORCH_STATE_ACTIVE) return 0;

    /* Update transport state machine */
    transport_state_t ts = fallback_tick(&sess->fallback, now_ns);
    switch (ts) {
    case TRANSPORT_QUIC_OK:
        if (sess->state == ORCH_STATE_FALLBACK) {
            sess->state = ORCH_STATE_ACTIVE;
            sess->capabilities |= ORCH_CAP_QUIC_PADDING;
        }
        break;
    case TRANSPORT_HTTP2_ACTIVE:
    case TRANSPORT_HTTP2_DEGRADED:
        sess->state = ORCH_STATE_FALLBACK;
        sess->capabilities &= ~ORCH_CAP_QUIC_PADDING;
        sess->capabilities |= ORCH_CAP_TCP_CHAFF | ORCH_CAP_H2_PADDING;
        break;
    case TRANSPORT_BLOCKED:
        sess->state = ORCH_STATE_JITTER_ONLY;
        sess->capabilities = ORCH_CAP_JITTER; /* Only timing channel */
        break;
    default:
        break;
    }

    return 0;
}

/* ═════════════════════════════════════════════
 * Destroy
 * ═════════════════════════════════════════════ */

void
orch_destroy(orch_session_t *sess)
{
    /* Free reassembly buffers */
    for (int i = 0; i < sess->reassembly_count; i++) {
        if (sess->reassembly[i].buffer)
            free(sess->reassembly[i].buffer);
    }

    stego_session_destroy(&sess->stego);
    jitter_tx_destroy(&sess->jitter_tx);
    jitter_rx_destroy(&sess->jitter_rx);
    fallback_destroy(&sess->fallback);
    morph_destroy(&sess->morph);

    memset(sess, 0, sizeof(*sess));
    sess->state = ORCH_STATE_CLOSED;
}

/* ═════════════════════════════════════════════
 * Stats
 * ═════════════════════════════════════════════ */

void
orch_get_stats(const orch_session_t *sess, orch_stats_t *stats)
{
    stats->state = sess->state;
    stats->capabilities = sess->capabilities;
    stats->msgs_sent = sess->msgs_sent;
    stats->msgs_received = sess->msgs_received;
    stats->bytes_sent = sess->bytes_sent;
    stats->bytes_received = sess->bytes_received;
    stats->cover_packets = sess->cover_packets_sent;
    stats->morph_quality = morph_quality(&sess->morph);
    stats->fallback_count = sess->fallback.fallback_count;
    stats->recovery_count = sess->fallback.recovery_count;
}

```
