---
title: "src/daemon/daemon.c"
nav_title: "daemon.c"
---

# `src/daemon/daemon.c`

```c
/*
 * QR-NSP Volcanic Edition — Userspace Daemon
 * SPDX-License-Identifier: AGPL-3.0-or-later
 * Consumes QUIC packets from the XDP ring buffer.
 * This is the Module 1 skeleton — packet inspection and logging.
 * Module 3 (PADDING injection) hooks into the process_event() path.
 *
 * Build: gcc -O2 -march=native -o qrnsp-daemon daemon.c -lbpf -lelf -lz
 * Run:   sudo ./qrnsp-daemon -i <interface> [-p <port>] [-t <target_ip>]
 */

#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <signal.h>
#include <errno.h>
#include <time.h>
#include <getopt.h>
#include <arpa/inet.h>
#include <sys/resource.h>
#include <net/if.h>

#include <bpf/libbpf.h>
#include <bpf/bpf.h>

/* ─────────────────────────────────────────────
 * Mirror XDP structures (keep in sync with qrnsp_xdp.c)
 * ───────────────────────────────────────────── */

#define SLOT_PAYLOAD_MAX  2048

#define SLOT_F_VALID      0x01
#define SLOT_F_LONG_HDR   0x02
#define SLOT_F_PADDING    0x04

#define CFG_ENABLED       0
#define CFG_TARGET_IP     1
#define CFG_TARGET_PORT   2
#define CFG_MODE          3

#define STAT_TOTAL_PKT    0
#define STAT_QUIC_PKT     1
#define STAT_QUEUED       2
#define STAT_DROPPED      3

struct qrnsp_event {
    uint64_t  timestamp_ns;
    uint32_t  pkt_len;
    uint32_t  payload_len;
    uint32_t  src_ip;
    uint32_t  dst_ip;
    uint16_t  src_port;
    uint16_t  dst_port;
    uint8_t   quic_flags;
    uint8_t   direction;
    uint8_t   flags;
    uint8_t   _pad0;
    uint32_t  quic_version;
    uint32_t  ifindex;
    uint8_t   payload[SLOT_PAYLOAD_MAX];
};

/* ─────────────────────────────────────────────
 * Globals
 * ───────────────────────────────────────────── */

static volatile sig_atomic_t g_running = 1;
static uint64_t g_events_processed = 0;
static uint64_t g_quic_long_headers = 0;
static uint64_t g_quic_short_headers = 0;

/* ─────────────────────────────────────────────
 * Signal handler
 * ───────────────────────────────────────────── */

static void
sig_handler(int sig)
{
    (void)sig;
    g_running = 0;
}

/* ─────────────────────────────────────────────
 * QUIC frame type decoder (RFC 9000 §19)
 * Used to identify PADDING frames for Module 3
 * ───────────────────────────────────────────── */

static const char *
quic_frame_type_str(uint8_t ftype)
{
    switch (ftype) {
    case 0x00: return "PADDING";
    case 0x01: return "PING";
    case 0x02: return "ACK";
    case 0x03: return "ACK+ECN";
    case 0x04: return "RESET_STREAM";
    case 0x05: return "STOP_SENDING";
    case 0x06: return "CRYPTO";
    case 0x07: return "NEW_TOKEN";
    case 0x08: case 0x09: case 0x0a: case 0x0b:
    case 0x0c: case 0x0d: case 0x0e: case 0x0f:
        return "STREAM";
    case 0x10: return "MAX_DATA";
    case 0x11: return "MAX_STREAM_DATA";
    case 0x12: case 0x13: return "MAX_STREAMS";
    case 0x1c: return "CONNECTION_CLOSE";
    case 0x1d: return "CONNECTION_CLOSE_APP";
    default:   return "UNKNOWN";
    }
}

/* ─────────────────────────────────────────────
 * Scan QUIC payload for PADDING frame regions
 *
 * In a 1-RTT (short header) packet after decryption,
 * PADDING frames are sequences of 0x00 bytes.
 * Pre-decryption, we can only estimate based on entropy.
 *
 * Returns: offset of first padding region, or -1 if none found.
 *          Sets *pad_len to length of the padding region.
 *
 * NOTE: This is a heuristic for unencrypted/initial packets.
 * For encrypted short-header packets, Module 2 (crypto) must
 * decrypt first, then this scanner runs on plaintext.
 * ───────────────────────────────────────────── */

static int
scan_padding_region(const uint8_t *payload, uint32_t len, uint32_t *pad_len)
{
    /* Skip QUIC header (variable length — use minimum for initial scan) */
    uint32_t hdr_min = (payload[0] & 0x80) ? 7 : 1;  /* long vs short */
    if (len <= hdr_min + 4)  /* Need at least header + some frames */
        return -1;

    /*
     * Walk frame types looking for PADDING (0x00) sequences.
     * In Initial packets, after the CRYPTO frame, remaining space
     * is typically padded to >= 1200 bytes (RFC 9000 §14.1).
     */
    uint32_t zero_start = 0;
    uint32_t zero_run   = 0;
    int found = 0;

    for (uint32_t i = hdr_min; i < len; i++) {
        if (payload[i] == 0x00) {
            if (!found) {
                zero_start = i;
                found = 1;
            }
            zero_run++;
        } else if (found) {
            /* End of zero run — PADDING frames are contiguous 0x00 */
            if (zero_run >= 32) {  /* Minimum useful padding region */
                *pad_len = zero_run;
                return (int)zero_start;
            }
            found = 0;
            zero_run = 0;
        }
    }

    /* Check trailing zeros */
    if (found && zero_run >= 32) {
        *pad_len = zero_run;
        return (int)zero_start;
    }

    return -1;
}

/* ─────────────────────────────────────────────
 * Process a single QUIC event from the ring buffer
 *
 * Module 1: Log + classify + scan for PADDING
 * Module 3 will add: inject payload into PADDING region
 * ───────────────────────────────────────────── */

static void
process_event(const struct qrnsp_event *evt)
{
    g_events_processed++;

    char src_str[INET_ADDRSTRLEN], dst_str[INET_ADDRSTRLEN];
    inet_ntop(AF_INET, &evt->src_ip, src_str, sizeof(src_str));
    inet_ntop(AF_INET, &evt->dst_ip, dst_str, sizeof(dst_str));

    int is_long = (evt->flags & SLOT_F_LONG_HDR);
    if (is_long) g_quic_long_headers++;
    else          g_quic_short_headers++;

    /* Terse output — one line per packet */
    printf("[%lu.%06lu] QUIC %s %s:%u → %s:%u  len=%u  hdr=%s",
           evt->timestamp_ns / 1000000000ULL,
           (evt->timestamp_ns / 1000ULL) % 1000000ULL,
           is_long ? "L" : "S",
           src_str, evt->src_port,
           dst_str, evt->dst_port,
           evt->payload_len,
           is_long ? "long" : "short");

    if (is_long && evt->quic_version != 0) {
        printf("  ver=0x%08X", evt->quic_version);
    }

    /* Scan for injectable PADDING regions */
    uint32_t pad_len = 0;
    int pad_off = scan_padding_region(evt->payload, evt->payload_len, &pad_len);
    if (pad_off >= 0) {
        printf("  PADDING@%d+%u", pad_off, pad_len);
    }

    printf("\n");
}

/* ─────────────────────────────────────────────
 * Ring buffer callback (libbpf)
 * ───────────────────────────────────────────── */

static int
ringbuf_event_handler(void *ctx, void *data, size_t data_sz)
{
    (void)ctx;
    if (data_sz < sizeof(struct qrnsp_event))
        return 0;

    const struct qrnsp_event *evt = data;
    if (!(evt->flags & SLOT_F_VALID))
        return 0;

    process_event(evt);
    return 0;
}

/* ─────────────────────────────────────────────
 * Print periodic stats
 * ───────────────────────────────────────────── */

static void
print_stats(int config_fd)
{
    /* Read per-CPU stats and sum */
    int ncpus = libbpf_num_possible_cpus();
    if (ncpus <= 0) ncpus = 1;

    uint64_t *values = calloc(ncpus, sizeof(uint64_t));
    if (!values) return;

    const char *names[] = {"total_pkt", "quic_pkt", "queued", "dropped"};
    uint64_t sums[4] = {0};

    /* Note: reading PERCPU_ARRAY requires ncpus-sized buffer */
    /* Simplified: just print daemon-side counters */
    free(values);

    fprintf(stderr, "\r[qrnsp] processed=%lu  long=%lu  short=%lu",
            g_events_processed, g_quic_long_headers, g_quic_short_headers);
    fflush(stderr);
}

/* ─────────────────────────────────────────────
 * Bump RLIMIT_MEMLOCK for BPF maps
 * ───────────────────────────────────────────── */

static int
bump_memlock(void)
{
    struct rlimit rl = { RLIM_INFINITY, RLIM_INFINITY };
    if (setrlimit(RLIMIT_MEMLOCK, &rl)) {
        fprintf(stderr, "setrlimit(MEMLOCK): %s\n", strerror(errno));
        return -1;
    }
    return 0;
}

/* ─────────────────────────────────────────────
 * Usage
 * ───────────────────────────────────────────── */

static void
usage(const char *prog)
{
    fprintf(stderr,
        "QR-NSP Daemon v0.1.0 — Censorship-Resistant QUIC Interceptor\n"
        "\n"
        "Usage: %s [options]\n"
        "  -i <iface>    Network interface (required)\n"
        "  -o <bpf.o>    Path to compiled XDP object (default: qrnsp_xdp.o)\n"
        "  -p <port>     Target port filter (default: 443)\n"
        "  -t <ip>       Target IP filter (optional)\n"
        "  -m <mode>     0=monitor, 1=intercept (default: 0)\n"
        "  -s <seconds>  Stats interval (default: 5)\n"
        "  -v            Verbose output\n"
        "  -h            This help\n",
        prog);
}

/* ─────────────────────────────────────────────
 * Main
 * ───────────────────────────────────────────── */

int
main(int argc, char **argv)
{
    const char *iface    = NULL;
    const char *obj_path = "qrnsp_xdp.o";
    uint32_t target_port = 443;
    uint32_t target_ip   = 0;
    uint32_t mode        = 0;   /* monitor */
    int stats_interval   = 5;
    int verbose          = 0;

    int opt;
    while ((opt = getopt(argc, argv, "i:o:p:t:m:s:vh")) != -1) {
        switch (opt) {
        case 'i': iface = optarg; break;
        case 'o': obj_path = optarg; break;
        case 'p': target_port = atoi(optarg); break;
        case 't': {
            struct in_addr addr;
            if (inet_pton(AF_INET, optarg, &addr) == 1)
                target_ip = addr.s_addr;
            else {
                fprintf(stderr, "Invalid IP: %s\n", optarg);
                return 1;
            }
            break;
        }
        case 'm': mode = atoi(optarg); break;
        case 's': stats_interval = atoi(optarg); break;
        case 'v': verbose = 1; break;
        case 'h': usage(argv[0]); return 0;
        default:  usage(argv[0]); return 1;
        }
    }

    if (!iface) {
        fprintf(stderr, "Error: interface (-i) required\n");
        usage(argv[0]);
        return 1;
    }

    int ifindex = if_nametoindex(iface);
    if (!ifindex) {
        fprintf(stderr, "Interface '%s' not found\n", iface);
        return 1;
    }

    /* Signals */
    signal(SIGINT,  sig_handler);
    signal(SIGTERM, sig_handler);

    /* Bump memlock for BPF */
    if (bump_memlock())
        return 1;

    fprintf(stderr, "[qrnsp] Loading XDP object: %s\n", obj_path);

    /* ── Open BPF object ── */
    struct bpf_object *obj = bpf_object__open_file(obj_path, NULL);
    if (!obj) {
        fprintf(stderr, "Failed to open BPF object: %s\n", strerror(errno));
        return 1;
    }

    /* ── Load BPF programs and maps ── */
    if (bpf_object__load(obj)) {
        fprintf(stderr, "Failed to load BPF object: %s\n", strerror(errno));
        bpf_object__close(obj);
        return 1;
    }

    /* ── Find XDP program ── */
    struct bpf_program *prog = bpf_object__find_program_by_name(obj, "qrnsp_xdp_intercept");
    if (!prog) {
        fprintf(stderr, "XDP program 'qrnsp_xdp_intercept' not found\n");
        bpf_object__close(obj);
        return 1;
    }

    int prog_fd = bpf_program__fd(prog);

    /* ── Attach XDP to interface ── */
    fprintf(stderr, "[qrnsp] Attaching XDP to %s (ifindex=%d)\n", iface, ifindex);

    /* Use SKB mode for broad compatibility; switch to DRV/HW for performance */
    LIBBPF_OPTS(bpf_xdp_attach_opts, attach_opts);
    if (bpf_xdp_attach(ifindex, prog_fd, XDP_FLAGS_SKB_MODE, &attach_opts)) {
        fprintf(stderr, "XDP attach failed: %s\n", strerror(errno));
        bpf_object__close(obj);
        return 1;
    }

    fprintf(stderr, "[qrnsp] XDP attached (SKB mode). Interface: %s\n", iface);

    /* ── Configure via BPF map ── */
    int config_fd = bpf_object__find_map_fd_by_name(obj, "qrnsp_config");
    if (config_fd >= 0) {
        uint32_t key, val;

        key = CFG_ENABLED;     val = 1;            bpf_map_update_elem(config_fd, &key, &val, BPF_ANY);
        key = CFG_TARGET_PORT; val = target_port;   bpf_map_update_elem(config_fd, &key, &val, BPF_ANY);
        key = CFG_TARGET_IP;   val = target_ip;     bpf_map_update_elem(config_fd, &key, &val, BPF_ANY);
        key = CFG_MODE;        val = mode;           bpf_map_update_elem(config_fd, &key, &val, BPF_ANY);

        fprintf(stderr, "[qrnsp] Config: port=%u ip=%s mode=%s\n",
                target_port,
                target_ip ? inet_ntoa((struct in_addr){.s_addr = target_ip}) : "any",
                mode ? "intercept" : "monitor");
    }

    /* ── Open ring buffer ── */
    struct ring_buffer *rb = ring_buffer__new(
        bpf_object__find_map_fd_by_name(obj, "qrnsp_ringbuf"),
        ringbuf_event_handler, NULL, NULL);

    if (!rb) {
        fprintf(stderr, "Failed to create ring buffer: %s\n", strerror(errno));
        goto cleanup;
    }

    fprintf(stderr, "[qrnsp] Ring buffer attached. Monitoring QUIC traffic...\n");

    /* ── Main loop ── */
    time_t last_stats = time(NULL);

    while (g_running) {
        int err = ring_buffer__poll(rb, 100 /* ms timeout */);
        if (err < 0 && err != -EINTR) {
            fprintf(stderr, "\nring_buffer__poll error: %d\n", err);
            break;
        }

        time_t now = time(NULL);
        if (now - last_stats >= stats_interval) {
            print_stats(config_fd);
            last_stats = now;
        }
    }

    fprintf(stderr, "\n[qrnsp] Shutting down...\n");

cleanup:
    /* Detach XDP */
    bpf_xdp_detach(ifindex, XDP_FLAGS_SKB_MODE, NULL);
    fprintf(stderr, "[qrnsp] XDP detached from %s\n", iface);

    if (rb)
        ring_buffer__free(rb);
    bpf_object__close(obj);

    fprintf(stderr, "[qrnsp] Total events processed: %lu\n", g_events_processed);
    return 0;
}

```
