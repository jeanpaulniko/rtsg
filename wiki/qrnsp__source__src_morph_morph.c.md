---
title: "src/morph/morph.c"
nav_title: "morph.c"
---

# `src/morph/morph.c`

```c
/*
 * QR-NSP Volcanic Edition — Traffic Morphing Engine
 * Module 7: Statistical fingerprint matching
 *
 * SPDX-License-Identifier: AGPL-3.0-or-later
 */

#include "qrnsp_morph.h"
#include "mlkem_params.h"
#include <string.h>
#include <math.h>

/* ═════════════════════════════════════════════
 * Built-in Cover Profiles
 *
 * Derived from published traffic analysis research:
 *   - Netflix: Reed & Slater 2019, packet captures from 4K streams
 *   - YouTube: Li et al. 2020, adaptive bitrate analysis
 *   - Zoom: Macmillan et al. 2021, video conferencing fingerprints
 *   - WhatsApp: Bahramali et al. 2020, voice call characterization
 * ═════════════════════════════════════════════ */

static const morph_profile_t builtin_profiles[] = {
    [MORPH_COVER_NETFLIX_4K] = {
        .type = MORPH_COVER_NETFLIX_4K,
        .size_bin_edge = {64,128,256,384,512,640,768,896,1024,1100,
                          1200,1280,1350,1400,1440,1460,1472,1480,1490,1500,
                          0,0,0,0,0,0,0,0,0,0,0,0},
        .size_bin_prob = {0.02,0.01,0.02,0.01,0.02,0.01,0.02,0.03,0.04,0.05,
                          0.08,0.10,0.10,0.12,0.10,0.08,0.06,0.05,0.04,0.04,
                          0,0,0,0,0,0,0,0,0,0,0,0},
        .ipat_bin_edge = {100,200,500,1000,2000,3000,4000,5000,6000,7000,
                          8000,10000,15000,20000,50000,100000,
                          0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        .ipat_bin_prob = {0.05,0.08,0.15,0.20,0.15,0.10,0.07,0.05,0.04,0.03,
                          0.02,0.02,0.01,0.01,0.01,0.01,
                          0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        .avg_bitrate_kbps = 25000.0,
        .peak_bitrate_kbps = 40000.0,
        .avg_packet_size = 1350.0,
        .avg_ipat_us = 2500.0,
        .initial_pkt_sizes = {583,1410,64,1460,1460,1460,1460,580},
        .initial_pkt_count = 8,
    },
    [MORPH_COVER_YOUTUBE_1080] = {
        .type = MORPH_COVER_YOUTUBE_1080,
        .size_bin_edge = {64,128,256,512,768,1024,1200,1350,1460,1500,
                          0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        .size_bin_prob = {0.08,0.03,0.04,0.05,0.05,0.10,0.15,0.20,0.20,0.10,
                          0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        .ipat_bin_edge = {200,500,1000,2000,5000,10000,20000,50000,100000,200000,
                          0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        .ipat_bin_prob = {0.03,0.10,0.25,0.25,0.15,0.10,0.05,0.04,0.02,0.01,
                          0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        .avg_bitrate_kbps = 8000.0,
        .peak_bitrate_kbps = 15000.0,
        .avg_packet_size = 1200.0,
        .avg_ipat_us = 4000.0,
        .initial_pkt_sizes = {517,1200,64,1350,1350,1350,1200,517},
        .initial_pkt_count = 8,
    },
    [MORPH_COVER_ZOOM_VIDEO] = {
        .type = MORPH_COVER_ZOOM_VIDEO,
        .size_bin_edge = {64,100,200,300,400,500,600,700,800,1000,
                          1100,1200,1300,1400,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        .size_bin_prob = {0.05,0.08,0.12,0.10,0.08,0.07,0.08,0.10,0.12,0.08,
                          0.05,0.04,0.02,0.01,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        .ipat_bin_edge = {500,1000,2000,5000,10000,20000,33000,50000,100000,200000,
                          0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        .ipat_bin_prob = {0.05,0.15,0.25,0.20,0.15,0.10,0.05,0.03,0.01,0.01,
                          0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        .avg_bitrate_kbps = 3500.0,
        .peak_bitrate_kbps = 5000.0,
        .avg_packet_size = 650.0,
        .avg_ipat_us = 8000.0,
        .initial_pkt_sizes = {300,64,800,1200,700,700,700,300},
        .initial_pkt_count = 8,
    },
    [MORPH_COVER_WHATSAPP_CALL] = {
        .type = MORPH_COVER_WHATSAPP_CALL,
        .size_bin_edge = {40,60,80,100,120,150,200,250,300,400,
                          0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        .size_bin_prob = {0.05,0.10,0.25,0.25,0.15,0.08,0.05,0.03,0.02,0.02,
                          0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        .ipat_bin_edge = {10000,15000,20000,25000,30000,40000,50000,60000,80000,100000,
                          0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        .ipat_bin_prob = {0.05,0.15,0.35,0.20,0.10,0.05,0.04,0.03,0.02,0.01,
                          0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        .avg_bitrate_kbps = 64.0,
        .peak_bitrate_kbps = 128.0,
        .avg_packet_size = 100.0,
        .avg_ipat_us = 20000.0,
        .initial_pkt_sizes = {120,60,100,100,100,100,100,60},
        .initial_pkt_count = 8,
    },
    [MORPH_COVER_WEB_BROWSE] = {
        .type = MORPH_COVER_WEB_BROWSE,
        .size_bin_edge = {64,128,256,512,768,1024,1280,1460,1500,0,
                          0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        .size_bin_prob = {0.25,0.10,0.10,0.10,0.08,0.12,0.10,0.10,0.05,0,
                          0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        .ipat_bin_edge = {100,500,1000,5000,10000,50000,100000,500000,1000000,5000000,
                          0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        .ipat_bin_prob = {0.10,0.15,0.15,0.15,0.10,0.10,0.10,0.08,0.05,0.02,
                          0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
        .avg_bitrate_kbps = 2000.0,
        .peak_bitrate_kbps = 10000.0,
        .avg_packet_size = 700.0,
        .avg_ipat_us = 50000.0,
        .initial_pkt_sizes = {517,64,1460,1460,1460,583,64,1460},
        .initial_pkt_count = 8,
    },
};

const morph_profile_t *
morph_get_builtin_profile(morph_cover_t cover)
{
    if (cover >= MORPH_COVER_COUNT || cover == MORPH_COVER_CUSTOM)
        return NULL;
    return &builtin_profiles[cover];
}

/* ═════════════════════════════════════════════
 * PRNG (xorshift128+)
 * ═════════════════════════════════════════════ */

static inline uint64_t
morph_rng(uint64_t s[2])
{
    uint64_t s1 = s[0], s0 = s[1];
    s[0] = s0;
    s1 ^= s1 << 23; s1 ^= s1 >> 17; s1 ^= s0 ^ (s0 >> 26);
    s[1] = s1;
    return s0 + s1;
}

static double
morph_uniform(uint64_t s[2])
{
    return (double)(morph_rng(s) >> 11) / (double)(1ULL << 53);
}

/* ═════════════════════════════════════════════
 * Sample from a discrete distribution (histogram)
 *
 * Given bin edges and probabilities, sample a value.
 * Returns a value uniformly within the selected bin.
 * ═════════════════════════════════════════════ */

static uint32_t
sample_histogram(uint64_t rng[2],
                 const uint16_t *edges, const double *probs,
                 int nbins, uint16_t prev_edge)
{
    double u = morph_uniform(rng);
    double cum = 0.0;
    uint16_t lo = prev_edge;

    for (int i = 0; i < nbins; i++) {
        if (edges[i] == 0 && i > 0) break; /* End of bins */
        cum += probs[i];
        if (u <= cum || i == nbins - 1) {
            uint16_t hi = edges[i];
            /* Uniform within bin */
            if (hi > lo) {
                return lo + (uint32_t)(morph_rng(rng) % (hi - lo));
            }
            return hi;
        }
        lo = edges[i];
    }
    return edges[0]; /* Fallback */
}

static uint32_t
sample_ipat_histogram(uint64_t rng[2],
                      const uint32_t *edges, const double *probs,
                      int nbins)
{
    double u = morph_uniform(rng);
    double cum = 0.0;
    uint32_t lo = 0;

    for (int i = 0; i < nbins; i++) {
        if (edges[i] == 0 && i > 0) break;
        cum += probs[i];
        if (u <= cum || i == nbins - 1) {
            uint32_t hi = edges[i];
            if (hi > lo)
                return lo + (uint32_t)(morph_rng(rng) % (hi - lo));
            return hi;
        }
        lo = edges[i];
    }
    return edges[0];
}

/* ═════════════════════════════════════════════
 * Init
 * ═════════════════════════════════════════════ */

int
morph_init(morph_session_t *sess, morph_cover_t cover,
           const uint8_t seed[32])
{
    memset(sess, 0, sizeof(*sess));

    if (cover >= MORPH_COVER_COUNT || cover == MORPH_COVER_CUSTOM)
        return -1;

    memcpy(&sess->profile, &builtin_profiles[cover], sizeof(morph_profile_t));
    sess->active = 1;

    /* Seed PRNG from shared secret */
    uint8_t h[32];
    uint8_t buf[64];
    memcpy(buf, seed, 32);
    memcpy(buf + 32, "morph_rng___________________", 32);
    mlkem_hash_h(h, buf, 64);
    memcpy(sess->rng_state, h, 16);
    if (sess->rng_state[0] == 0) sess->rng_state[0] = 1;
    if (sess->rng_state[1] == 0) sess->rng_state[1] = 1;

    return 0;
}

int
morph_init_custom(morph_session_t *sess,
                  const morph_profile_t *profile,
                  const uint8_t seed[32])
{
    int ret = morph_init(sess, MORPH_COVER_WEB_BROWSE, seed);
    if (ret == 0) {
        memcpy(&sess->profile, profile, sizeof(morph_profile_t));
    }
    return ret;
}

void
morph_destroy(morph_session_t *sess)
{
    memset(sess, 0, sizeof(*sess));
}

/* ═════════════════════════════════════════════
 * Shape: determine target size + delay for a packet
 * ═════════════════════════════════════════════ */

int
morph_shape(morph_session_t *sess,
            size_t payload_size,
            size_t *out_size,
            uint64_t *out_delay_ns)
{
    if (!sess->active) {
        *out_size = payload_size;
        *out_delay_ns = 0;
        return 0;
    }

    morph_profile_t *p = &sess->profile;

    /* Sample target packet size from profile distribution */
    uint32_t target = sample_histogram(sess->rng_state,
                                       p->size_bin_edge, p->size_bin_prob,
                                       MORPH_SIZE_BINS, 0);

    /* Ensure target >= payload (can't shrink, only pad) */
    if (target < (uint32_t)payload_size)
        target = (uint32_t)payload_size;

    /* Mimic initial packet sizes for new sessions */
    if (sess->pkts_sent < (uint64_t)p->initial_pkt_count) {
        uint16_t init_size = p->initial_pkt_sizes[sess->pkts_sent];
        if (init_size >= payload_size)
            target = init_size;
    }

    *out_size = target;

    /* Sample inter-arrival time from profile distribution */
    uint32_t ipat_us = sample_ipat_histogram(sess->rng_state,
                                             p->ipat_bin_edge, p->ipat_bin_prob,
                                             MORPH_IPAT_BINS);

    *out_delay_ns = (uint64_t)ipat_us * 1000ULL;

    return 0;
}

/* ═════════════════════════════════════════════
 * Pad: fill buffer to target size
 * ═════════════════════════════════════════════ */

int
morph_pad(morph_session_t *sess,
          uint8_t *buf, size_t data_len, size_t target)
{
    if (target <= data_len) return 0;

    /* Fill padding with PRNG bytes (looks random, not zeros) */
    size_t pad_len = target - data_len;
    for (size_t i = 0; i < pad_len; i++) {
        buf[data_len + i] = (uint8_t)(morph_rng(sess->rng_state) & 0xFF);
    }

    return 0;
}

/* ═════════════════════════════════════════════
 * Record TX + Quality Monitoring
 * ═════════════════════════════════════════════ */

void
morph_record_tx(morph_session_t *sess, size_t pkt_size, uint64_t timestamp_ns)
{
    if (sess->session_start_ns == 0)
        sess->session_start_ns = timestamp_ns;

    /* Update running KS statistic for packet sizes */
    /* Simplified: track empirical CDF deviation from profile */
    morph_profile_t *p = &sess->profile;
    double emp_cdf = 0.0, prof_cdf = 0.0;
    for (int i = 0; i < MORPH_SIZE_BINS && p->size_bin_edge[i] > 0; i++) {
        prof_cdf += p->size_bin_prob[i];
        if (pkt_size <= p->size_bin_edge[i]) {
            emp_cdf = (double)(sess->pkts_sent + 1) / (double)(sess->pkts_sent + 2);
            break;
        }
    }
    double ks = fabs(emp_cdf - prof_cdf);
    /* Exponential moving average */
    sess->ks_size = sess->ks_size * 0.99 + ks * 0.01;

    sess->last_tx_ns = timestamp_ns;
    sess->bytes_sent += pkt_size;
    sess->pkts_sent++;
    sess->sample_count++;
}

double
morph_quality(const morph_session_t *sess)
{
    /* Combined KS distance (lower = better morphing) */
    return (sess->ks_size + sess->ks_ipat) / 2.0;
}

/* ═════════════════════════════════════════════
 * Cover Traffic Generation
 *
 * When there's no real data to send, generate dummy
 * packets to maintain the cover profile's traffic pattern.
 * ═════════════════════════════════════════════ */

int
morph_generate_cover(morph_session_t *sess,
                     size_t *out_size, uint64_t *out_delay_ns)
{
    /* Same as shape, but with zero payload */
    return morph_shape(sess, 0, out_size, out_delay_ns);
}

```
