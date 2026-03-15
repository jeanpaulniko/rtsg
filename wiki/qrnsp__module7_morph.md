---
title: "Module 7: Traffic Morphing"
nav_title: "M7: Traffic Morph"
---

# Module 7: Statistical Traffic Morphing

**Files:** `src/morph/morph.c`  
**Header:** `include/qrnsp_morph.h`  

## Problem

DPI increasingly uses statistical analysis: packet size distributions, inter-arrival times, burst patterns, TLS fingerprints. Protocol signatures aren't enough for detection — they profile traffic *shape*.

## Solution

Learn statistical profiles of real services offline, then pad/delay/batch outgoing packets to match the target distribution at runtime.

## Built-in Profiles

| Profile | Avg Bitrate | Avg Pkt Size | Avg IPAT |
|---------|-------------|--------------|----------|
| Netflix 4K | 25 Mbps | 1350 bytes | 2.5ms |
| YouTube 1080p | 8 Mbps | 1200 bytes | 4ms |
| Zoom Video | 3.5 Mbps | 650 bytes | 8ms |
| WhatsApp Voice | 64 kbps | 100 bytes | 20ms |
| Web Browsing | 2 Mbps | 700 bytes | 50ms |

## Quality Monitoring

Running Kolmogorov-Smirnov statistic tracks drift from target profile. KS < 0.1 = good, KS > 0.3 = DPI risk.

## Cover Traffic

When no real data to send, generates dummy packets matching the profile to maintain continuous flow patterns.
