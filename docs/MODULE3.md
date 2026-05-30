# Module 3: UART — Protocol + RTL + Basic Testbench

**Goal**: Understand the UART protocol (8N1, baud), translate it to RTL (TX, RX, baud gen), and verify with a **basic** (non-UVM) directed testbench.

---

## Navigation

[← Previous: Module 2: Methodology (Part 2)](MODULE2.md) | [Next: Module 4: UART UVM+SV →](MODULE4.md)

[↑ Back to README](../README.md)

---

## Before You Start (Learning Path)

Modules 3–8 are **learning modules**, not just exercises. Before running commands:

1. **Read the detailed UART learning guide**: [UART_LEARNING_GUIDE.md](UART_LEARNING_GUIDE.md) — what UART is, what kind of protocol (serial, asynchronous, point-to-point), how it works (frame format, baud rate, TX/RX), timing, and where it’s used.
2. **Read the protocols + UVM overview**: [LEARNING_GUIDE_PROTOCOLS_AND_UVM.md](LEARNING_GUIDE_PROTOCOLS_AND_UVM.md) — **Part B § 4. When to Use Baseline vs UVM** (why we start with a baseline testbench before UVM).

Then return here and follow **Overview** → **Topics Covered** → **Example** → **Exercises**.

---

## Running Module 3

- **Module doc**: [module3/README.md](../module3/README.md)
- **Example**: [module3/examples/uart_baseline/](../module3/examples/uart_baseline/) — UART TX/RX RTL + basic loopback test (no UVM)

**Quick run** (from repo root):

```bash
cd module3/examples/uart_baseline
make run
```

Or: `./scripts/module3.sh --run`

- **Slides & video**: [slides.pptx](../media/module3/slides.pptx) · [slides.pdf](../media/module3/slides.pdf) · [video.mp4](../media/module3/video.mp4) — regenerate: `./scripts/build_all_media.sh --module 3`

---

## Overview

Module 3 is the first **protocol** module:

- **UART protocol**: 8N1 framing, start/stop bits, baud rate.
- **RTL**: `uart_tx`, `uart_rx`, `baud_gen` — translating protocol to RTL (same methodology as Module 1).
- **Basic testbench**: Directed test (loopback TX→RX, send bytes, check received bytes). **No UVM** — UVM for UART is Module 4.

### What You'll Learn

- **UART 8N1**: Start bit (0), 8 data bits (LSB first), stop bit (1); idle high.
- **Baud rate**: Role of a baud generator (clock divider → baud_tick).
- **RTL architecture**: TX (parallel→serial, shift per baud_tick), RX (start detect, sample, data_valid), baud_gen (divider).
- **Basic TB**: Loopback, directed stimulus, and checking without UVM.

### Prerequisites

- Module 1 (spec → RTL) and Module 2 (basic TB → UVM, toolchain).
- Verilator, Make, C++ compiler. **No UVM required** for the uart_baseline example.

---

## Design Architecture

### 1. Block hierarchy

- **top_uart_baseline** → `baud_gen`, `uart_tx`, `uart_rx`; **sim_main.cpp** drives `clk`/`rst_n` only.
- **Loopback**: `assign rx = tx` — one wire connects transmitter to receiver.

### 2. RTL blocks

- **baud_gen**: `DIVIDER` → `baud_tick` every N clocks; shared by TX and RX.
- **uart_tx**: parallel-in / serial-out; start + 8 data (LSB first) + stop; `busy` during frame.
- **uart_rx**: start detect, sample per `baud_tick`, `data_valid` + optional `framing_error`.

### 3. Timing and clocking

- Single `clk` domain; async `rst_n`; all bit times referenced to `baud_tick`.

---

## Verification & Testing Methods

### 1. Verification goals

- Prove RTL implements **UART 8N1** before UVM (Module 4).
- Happy-path loopback: bytes sent on TX appear correctly on RX.

### 2. Baseline directed test

- **Stimulus**: `initial` block — `start`, `data_in` (0x55, 0xAA).
- **Check**: `wait(data_valid)`; compare `data_out`; `$error` / `$display`.
- **No UVM**: pin wiggling only — fastest way to learn the protocol on real RTL.

### 3. Coverage gaps (defer to Module 4)

- Random baud, framing errors, `busy` back-to-back, functional coverage.
- Map checks to [UART_LEARNING_GUIDE.md](UART_LEARNING_GUIDE.md) spec bullets.

---

## Key files to study

- `module3/examples/uart_baseline/dut/baud_gen.v` — divider → `baud_tick`
- `module3/examples/uart_baseline/dut/uart_tx.v` — 8N1 transmit
- `module3/examples/uart_baseline/dut/uart_rx.v` — receive and `data_valid`
- `module3/examples/uart_baseline/top_uart_baseline.sv` — loopback + directed test
- `docs/UART_LEARNING_GUIDE.md` — protocol reference

## Key Concepts

### 1. Asynchronous serial

- No dedicated clock wire; TX and RX must share the same bit time (`baud_tick`).
- Loopback (`rx = tx`) proves TX serialization and RX deserialization together.

### 2. 8N1 frame

- Idle high → start (0) → 8 data bits LSB first → stop (1).
- `busy` on TX; `data_valid` pulse on RX when a byte is ready.

## Common Pitfalls

1. **Mismatched baud timing**
   - **Mistake**: Different dividers on TX and RX in a loopback test.
   - **Correct**: One `baud_gen` drives both (as in uart_baseline).
   - **Why**: RX samples at the wrong bit times.

2. **Only checking `busy`**
   - **Mistake**: Assuming success when TX finishes.
   - **Correct**: Wait for `data_valid` and compare `data_out` to the sent byte.
   - **Why**: `busy` does not prove the loopback byte is correct.

---

## Topics Covered

### 1. UART Protocol (8N1)

- **Signals**: Serial line (tx/rx), idle high; system clock; baud_tick (one pulse per bit time).
- **Frame**: 1 start bit (0), 8 data bits (LSB first), 1 stop bit (1).
- **Timing**: One bit per baud_tick; baud_tick derived from system clock via a divider (e.g. DIVIDER = clk_freq / baud_rate).

#### UART quick reference (8N1)

- **Framing**: `idle=1` → `start=0` → 8 data bits (LSB first) → `stop=1`.
- **Baud math**: `DIVIDER = round(clk_hz / baud)`. Example: 50 MHz clock, 115200 baud → divider ≈ 434.
- **Sampling**: Basic design samples once per bit at the `baud_tick`. Production UARTs often oversample (e.g., 8x or 16x) to tolerate clock drift; you can add this later by replacing `baud_tick` with an oversample tick and using a mid-bit sample.
- **Reset state**: Line idles high, TX not busy, RX clears internal shift register, `data_valid` low.
- **Errors**: `framing_error` when stop bit is not high at expected sample; optional `parity_error` if parity enabled (not used in 8N1 baseline).

#### TX design checklist

- Inputs: `clk`, `rst_n`, `baud_tick`, `start`, `data_in[7:0]`.
- Outputs: `tx`, `busy`.
- Behavior: On `start`, latch `data_in`, drive start bit low, then shift out bits [0:7] each `baud_tick`, then drive stop bit high for one `baud_tick`. Deassert `busy` after stop bit.
- Edge cases: Ignore `start` while `busy` (or queue it in a FIFO if you extend the design).

#### RX design checklist

- Inputs: `clk`, `rst_n`, `baud_tick`, `rx`.
- Outputs: `data_out[7:0]`, `data_valid` (pulse), `framing_error`.
- Behavior: Detect falling edge for start; wait one `baud_tick` to sample mid-start; sample 8 bits on successive `baud_tick`s; sample stop bit last. If stop is not high, raise `framing_error`. Pulse `data_valid` for one cycle when byte is ready.
- Robustness options: Add metastability sync on `rx`; add oversampling + majority vote; add `rx_ready`/`rx_valid` handshake if you later connect to a FIFO.

#### Baud generator notes

- Inputs: `clk`, `rst_n`, `divisor` (constant parameter in the baseline).
- Output: `baud_tick` high for one cycle every `divisor` clocks.
- For synthesis, keep the counter simple (`divisor-1` down-counter or up-counter compare). For sim, you can parametrize `divisor` to speed up runs.

#### Protocol extensions (not in baseline example)

- **Data bits**: 5–9 data bits are common.
- **Parity**: Even/odd/mark/space; adds a parity bit before stop.
- **Stop bits**: 1 or 2 stop bits.
- **Flow control**: RTS/CTS hardware pins (outside the serial line) to throttle traffic.
- The baseline RTL assumes 8N1 with no parity and no flow control.

### 2. Hands-on testbench (uart_baseline)

- **Loopback**: Connect TX output to RX input; send bytes from TX, check they appear on RX.
- **Directed test**: Reset release, send 0x55 and 0xAA, wait for `data_valid`, check `data_out`. Implemented in `top_uart_baseline.sv` (initial block) and C++ (clk, rst_n); no UVM.
- **Self-check flow**: `wait(rst_n)` → pulse `start`/`data_in` → `wait(!busy)` → `wait(data_valid)` → compare `data_out` → repeat → `$finish`.

---

## Example: uart_baseline

#### Example 3.1: UART baseline loopback (`module3/examples/uart_baseline/`)

**What it demonstrates:**

- UART 8N1 TX/RX RTL with shared `baud_gen`
- Loopback wiring (`rx = tx`) and directed bytes 0x55 / 0xAA
- Baseline self-check without UVM (wait for `data_valid`, compare `data_out`)

```bash
cd module3/examples/uart_baseline
make run
```

| Component | Role |
|-----------|------|
| **dut/** | uart_tx.v, uart_rx.v, baud_gen.v |
| **top_uart_baseline.sv** | Loopback (rx=tx), baud_gen, uart_tx, uart_rx; directed test in initial block |
| **sim_main.cpp** | Clock, reset; run until `$finish` |

Run: `cd module3/examples/uart_baseline && make run`

---

## Command Reference

```bash
cd module3/examples/uart_baseline
make run
```

```bash
./scripts/module3.sh --check   # Environment + example dirs
./scripts/module3.sh --run     # Run uart_baseline
```

---

## Learning Outcomes

- Describe UART 8N1 frame and baud timing.
- Explain the role of uart_tx, uart_rx, and baud_gen.
- Run the uart_baseline example and interpret the loopback test.
- Ready for Module 4: UART UVM+SV verification.

---

## Exercises

1. **Run uart_baseline**
   - Run `make run` in `module3/examples/uart_baseline`. Confirm you see loopback success (e.g. bytes sent and received match).

2. **Trace one byte**
   - Open `top_uart_baseline.sv` and the DUT sources. For one byte (e.g. 0x55), trace: testbench drives `start` and `data_in` → uart_tx sends start bit, 8 data bits (LSB first), stop bit → uart_rx detects start, samples 8 bits, pulses `data_valid` with `data_out`. Map each step to the corresponding RTL (baud_tick, busy, etc.).

3. **Baud and divider**
   - In the example, find the baud divisor (or clock/baud relationship). Change the baud rate (or divisor) in simulation only and re-run; confirm the test still passes if TX and RX use the same timing.

4. **Optional: Waveforms**
   - If the Makefile generates a VCD, open it and identify: baud_tick, tx, rx, start, data_valid, data_out. Confirm one UART frame (start + 8 data + stop) per byte.

---

## Assessment

- [ ] Can describe UART 8N1 (start bit, 8 data LSB first, stop bit) and the role of baud_tick.
- [ ] Can explain the role of uart_tx, uart_rx, and baud_gen in the RTL.
- [ ] Can run uart_baseline and interpret the loopback test result.
- [ ] Ready for Module 4: UART UVM+SV verification.

---

## Next Steps

After completing this module, proceed to **Module 4: UART UVM+SV** — full UART verification with UVM (agent, sequences, driver, monitor, scoreboard).
