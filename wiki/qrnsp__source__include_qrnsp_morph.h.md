---
title: "include/qrnsp_morph.h"
nav_title: "qrnsp_morph.h"
---

# `include/qrnsp_morph.h`

```c
/*
 * QR-NSP Volcanic Edition — Traffic Morphing
 * Module 7: Statistical fingerprint matching
 *
 * Deep Packet Inspection (DPI) increasingly uses statistical
 * analysis beyond simple protocol signatures. They profile:
 *   - Packet size distributions
 *   - Inter-arrival time distributions
 *   - Burst patterns
 *   - Flow duration / volume ratios
 *   - TLS fingerprints (JA3/JA4)
 *
 * Traffic morphing transforms QR-NSP's traffic to statistically
 * match a target cover protocol (Netflix streaming, Zoom calls,
 * WhatsApp video, YouTube). The adversary's DPI classifier sees
 * traffic that matches the expected statistical profile.
 *
 * Approach: Learn statistical profiles of real services offline,
 * then pad/delay/batch outgoing packets to match the target
 * distribution at runtime.
 *
 * SPDX-License-Identifier: AGPL-3.0-or-later
 */

#ifndef QRNSP_MORPH_H
#define QRNSP_MORPH_H

#include <stdint.h>
#include <stddef.h>

/* ─────────────────────────────────────────────
 * Cover protocol profiles
 * ───────────────────────────────────────────── */

typedef enum {
    MORPH_COVER_NETFLIX_4K,     /* Netflix 4K streaming (~25 Mbps)     */
    MORPH_COVER_YOUTUBE_1080,   /* YouTube 1080p (~8 Mbps)             */
    MORPH_COVER_ZOOM_VIDEO,     /* Zoom video call (~3.5 Mbps)         */
    MORPH_COVER_WHATSAPP_CALL,  /* WhatsApp voice call (~64 kbps)      */
    MORPH_COVER_WEB_BROWSE,     /* General HTTPS browsing              */
    MORPH_COVER_CUSTOM,         /* User-provided profile               */
    MORPH_COVER_COUNT
} morph_cover_t;

/* ─────────────────────────────────────────────
 * Statistical profile: describes a traffic pattern
 *
 * Each profile contains histogram bins for packet sizes
 * and inter-arrival times. The morpher samples from these
 * distributions when shaping outgoing traffic.
 * ───────────────────────────────────────────── */

#define MORPH_SIZE_BINS     32    /* Packet size histogram bins         */
#define MORPH_IPAT_BINS     32    /* Inter-arrival time histogram bins  */
#define MORPH_BURST_BINS    16    /* Burst length histogram bins        */

typedef struct {
    morph_cover_t type;

    /* Packet size distribution */
    uint16_t size_bin_edge[MORPH_SIZE_BINS];  /* Bin upper edges (bytes) */
    double   size_bin_prob[MORPH_SIZE_BINS];  /* Probability per bin     */

    /* Inter-arrival time distribution */
    uint32_t ipat_bin_edge[MORPH_IPAT_BINS];  /* Bin upper edges (μs)   */
    double   ipat_bin_prob[MORPH_IPAT_BINS];  /* Probability per bin    */

    /* Burst profile */
    uint16_t burst_bin_edge[MORPH_BURST_BINS]; /* Packets per burst     */
    double   burst_bin_prob[MORPH_BURST_BINS];

    /* Aggregate stats */
    double   avg_bitrate_kbps;    /* Target average bitrate             */
    double   peak_bitrate_kbps;   /* Peak bitrate                       */
    double   avg_packet_size;     /* Mean packet size                   */
    double   avg_ipat_us;         /* Mean inter-arrival time            */

    /* TLS/QUIC fingerprint mimicry */
    uint16_t initial_pkt_sizes[8]; /* First 8 packet sizes to mimic     */
    int      initial_pkt_count;
} morph_profile_t;

/* ─────────────────────────────────────────────
 * Morpher session
 * ───────────────────────────────────────────── */

typedef struct {
    morph_profile_t profile;      /* Active cover profile               */
    int             active;       /* Morphing enabled                   */

    /* Shaping state */
    uint64_t last_tx_ns;          /* Last packet sent timestamp         */
    uint64_t session_start_ns;    /* Session start                      */
    uint64_t bytes_sent;          /* Total bytes sent this session      */
    uint64_t pkts_sent;           /* Total packets sent                 */

    /* Current burst tracking */
    uint32_t burst_remaining;     /* Packets left in current burst      */
    uint64_t burst_gap_ns;        /* Inter-burst gap                    */

    /* Padding buffer */
    uint8_t  pad_buf[2048];       /* For packet size padding            */

    /* PRNG for sampling from distributions */
    uint64_t rng_state[2];

    /* KS statistic monitoring (detect when we're drifting) */
    double   ks_size;             /* Running KS stat for size dist      */
    double   ks_ipat;             /* Running KS stat for IPAT dist      */
    uint64_t sample_count;
} morph_session_t;

/* ─────────────────────────────────────────────
 * API
 * ───────────────────────────────────────────── */

/* Initialize with a built-in cover profile */
int morph_init(morph_session_t *sess, morph_cover_t cover,
               const uint8_t seed[32]);

/* Initialize with a custom profile (e.g., captured from real traffic) */
int morph_init_custom(morph_session_t *sess,
                      const morph_profile_t *profile,
                      const uint8_t seed[32]);

void morph_destroy(morph_session_t *sess);

/*
 * Shape outgoing packet: given a payload, determine:
 *   - How much padding to add (target size from profile)
 *   - How long to delay before sending (target IPAT from profile)
 *   - Whether to split into multiple packets or batch
 *
 * out_size:  recommended padded packet size
 * out_delay: recommended delay in nanoseconds before sending
 *
 * Returns 0 on success.
 */
int morph_shape(morph_session_t *sess,
                size_t payload_size,
                size_t *out_size,
                uint64_t *out_delay_ns);

/*
 * Pad a packet buffer to the target size.
 * Fills extra space with random-looking padding.
 *
 * buf:      packet buffer (must have capacity >= target_size)
 * data_len: actual data in buffer
 * target:   target padded size (from morph_shape)
 */
int morph_pad(morph_session_t *sess,
              uint8_t *buf, size_t data_len, size_t target);

/*
 * Record that a packet was sent (updates internal statistics).
 */
void morph_record_tx(morph_session_t *sess,
                     size_t pkt_size, uint64_t timestamp_ns);

/*
 * Get current quality of morphing (KS distance to target profile).
 * Lower is better. < 0.1 is good. > 0.3 means DPI might detect.
 */
double morph_quality(const morph_session_t *sess);

/*
 * Generate cover (chaff) traffic when no real data to send.
 * Returns recommended dummy packet size and delay.
 * Essential: real traffic is bursty, but cover profiles may
 * require continuous flow (e.g., video streaming).
 */
int morph_generate_cover(morph_session_t *sess,
                         size_t *out_size, uint64_t *out_delay_ns);

/* Get a read-only pointer to built-in profiles */
const morph_profile_t *morph_get_builtin_profile(morph_cover_t cover);

#endif /* QRNSP_MORPH_H */

```
