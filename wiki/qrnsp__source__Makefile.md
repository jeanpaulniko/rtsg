---
title: "Makefile"
nav_title: "Makefile"
---

# `Makefile`

```makefile
# QR-NSP Volcanic Edition — Build System
# Module 1: XDP QUIC Interceptor
# Module 2: ML-KEM-1024 + X25519 Hybrid KEM
#
# Prerequisites:
#   apt install clang llvm libbpf-dev linux-headers-$(uname -r) libelf-dev zlib1g-dev
#   (Kernel 5.8+ for BPF_MAP_TYPE_RINGBUF)

CC       = gcc
CLANG    = clang
LLC      = llc

# Flags
CFLAGS   = -O2 -Wall -Wextra -march=native -I include
LDFLAGS_DAEMON = -lbpf -lelf -lz

# BPF compilation flags
BPF_CFLAGS = -O2 -target bpf -D__TARGET_ARCH_x86 \
             -I include \
             -I /usr/include/$(shell uname -m)-linux-gnu \
             -Wno-compare-distinct-pointer-types

# Output
BUILD_DIR = build
XDP_OBJ   = $(BUILD_DIR)/qrnsp_xdp.o
DAEMON    = $(BUILD_DIR)/qrnsp-daemon
TEST_CRYPTO = $(BUILD_DIR)/test_crypto

# ── Crypto sources ──
CRYPTO_SRCS = src/crypto/ntt.c src/crypto/poly.c src/crypto/symmetric.c \
              src/crypto/kem.c src/crypto/hybrid_kem.c
AEAD_SRCS   = src/aead/aes256gcm.c
STEGO_SRCS  = src/stego/inject.c
JITTER_SRCS = src/jitter/jitter.c
DENIABLE_SRCS = src/deniable/deniable.c
FALLBACK_SRCS = src/fallback/fallback.c
MORPH_SRCS    = src/morph/morph.c
ORCH_SRCS     = src/orchestrator/orchestrator.c

ALL_SRCS = $(CRYPTO_SRCS) $(AEAD_SRCS) $(STEGO_SRCS) $(JITTER_SRCS) \
           $(DENIABLE_SRCS) $(FALLBACK_SRCS) $(MORPH_SRCS) $(ORCH_SRCS)

.PHONY: all clean xdp daemon crypto stego jitter deniable pipeline test help

all: $(BUILD_DIR) xdp daemon crypto stego jitter deniable pipeline

$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)

# ── XDP BPF object ──
xdp: $(BUILD_DIR) $(XDP_OBJ)

$(XDP_OBJ): src/xdp/qrnsp_xdp.c include/qrnsp.h
	$(CLANG) $(BPF_CFLAGS) -c $< -o $@
	@echo "  [BPF] $@"

# ── Userspace daemon ──
daemon: $(BUILD_DIR) $(DAEMON)

$(DAEMON): src/daemon/daemon.c include/qrnsp.h
	$(CC) $(CFLAGS) $< -o $@ $(LDFLAGS_DAEMON)
	@echo "  [CC]  $@"

# ── Crypto test ──
crypto: $(BUILD_DIR) $(TEST_CRYPTO)

$(TEST_CRYPTO): tests/test_crypto.c $(CRYPTO_SRCS) include/mlkem_params.h include/qrnsp_crypto.h
	$(CC) $(CFLAGS) tests/test_crypto.c $(CRYPTO_SRCS) -o $@
	@echo "  [CC]  $@"

# ── Stego pipeline test ──
stego: $(BUILD_DIR) $(BUILD_DIR)/test_stego

$(BUILD_DIR)/test_stego: tests/test_stego.c $(CRYPTO_SRCS) $(AEAD_SRCS) $(STEGO_SRCS) \
                         include/qrnsp_stego.h include/qrnsp_aead.h
	$(CC) $(CFLAGS) tests/test_stego.c $(CRYPTO_SRCS) $(AEAD_SRCS) $(STEGO_SRCS) -o $@
	@echo "  [CC]  $@"

# ── Run tests ──
test: crypto stego jitter deniable pipeline
	./$(TEST_CRYPTO)
	./$(BUILD_DIR)/test_stego
	./$(BUILD_DIR)/test_jitter
	./$(BUILD_DIR)/test_deniable
	./$(BUILD_DIR)/test_pipeline

test-stego: stego
	./$(BUILD_DIR)/test_stego

test-jitter: jitter
	./$(BUILD_DIR)/test_jitter

test-deniable: deniable
	./$(BUILD_DIR)/test_deniable

test-pipeline: pipeline
	./$(BUILD_DIR)/test_pipeline

# ── Jitter channel test ──
jitter: $(BUILD_DIR) $(BUILD_DIR)/test_jitter

$(BUILD_DIR)/test_jitter: tests/test_jitter.c $(JITTER_SRCS) src/crypto/symmetric.c \
                          include/qrnsp_jitter.h
	$(CC) $(CFLAGS) tests/test_jitter.c $(JITTER_SRCS) src/crypto/symmetric.c -o $@ -lm
	@echo "  [CC]  $@"

# ── Deniable encryption test ──
deniable: $(BUILD_DIR) $(BUILD_DIR)/test_deniable

$(BUILD_DIR)/test_deniable: tests/test_deniable.c $(DENIABLE_SRCS) $(AEAD_SRCS) \
                            src/crypto/symmetric.c include/qrnsp_deniable.h
	$(CC) $(CFLAGS) tests/test_deniable.c $(DENIABLE_SRCS) $(AEAD_SRCS) src/crypto/symmetric.c -o $@
	@echo "  [CC]  $@"

# ── Full pipeline test (Modules 6-8) ──
pipeline: $(BUILD_DIR) $(BUILD_DIR)/test_pipeline

$(BUILD_DIR)/test_pipeline: tests/test_pipeline.c $(ALL_SRCS)
	$(CC) $(CFLAGS) tests/test_pipeline.c $(ALL_SRCS) -o $@ -lm
	@echo "  [CC]  $@"

# ── Clean ──
clean:
	rm -rf $(BUILD_DIR)

# ── Help ──
help:
	@echo "QR-NSP Build Targets:"
	@echo "  make all            Build everything"
	@echo "  make xdp            Build XDP BPF object"
	@echo "  make daemon         Build userspace daemon"
	@echo "  make crypto         Build ML-KEM + X25519 test"
	@echo "  make stego          Build PADDING injection test"
	@echo "  make jitter         Build timing channel test"
	@echo "  make deniable       Build deniable encryption test"
	@echo "  make pipeline       Build full pipeline test (M6-8)"
	@echo "  make test           Run ALL tests"
	@echo "  make clean          Remove build artifacts"

```
