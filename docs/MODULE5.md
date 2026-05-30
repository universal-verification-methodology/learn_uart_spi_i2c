# Module 5: SPI — Protocol + RTL + Basic Testbench

**Goal**: Understand the SPI protocol (mode 0, signals), translate it to RTL (SPI master, clk_div), and verify with a **basic** (non-UVM) directed testbench.

---

## Navigation

[← Previous: Module 4: UART UVM+SV](MODULE4.md) | [Next: Module 6: SPI UVM+SV →](MODULE6.md)

[↑ Back to README](../README.md)

---

## Before You Start (Learning Path)

Before running commands:

1. **Read the detailed SPI learning guide**: [SPI_LEARNING_GUIDE.md](SPI_LEARNING_GUIDE.md) — what SPI is, what kind of protocol (serial, synchronous, master–slave), how it works (signals, modes CPOL/CPHA, Mode 0, timing), and where it’s used.
2. **Read the protocols + UVM overview**: [LEARNING_GUIDE_PROTOCOLS_AND_UVM.md](LEARNING_GUIDE_PROTOCOLS_AND_UVM.md) — **Part B § 4. When to Use Baseline vs UVM** (why we start with a baseline test before SPI UVM in Module 6).

Then follow **Overview** → **Topics Covered** → **Example** → **Exercises**.

---

## Running Module 5

- **Module doc**: [module5/README.md](../module5/README.md)
- **Example**: [module5/examples/spi_baseline/](../module5/examples/spi_baseline/) — SPI master RTL + basic directed test (no UVM)

**Quick run** (from repo root):

```bash
cd module5/examples/spi_baseline
make run
```

Or: `./scripts/module5.sh --run`

- **Slides & video**: [slides.pptx](../media/module5/slides.pptx) · [slides.pdf](../media/module5/slides.pdf) · [video.mp4](../media/module5/video.mp4) — regenerate: `./scripts/build_all_media.sh --module 5`

---

## Overview

Module 5 is the second **protocol** module (after UART):

- **SPI protocol**: Mode 0 (CPOL=0, CPHA=0); SCLK, MOSI, CS_N; 8-bit transfers MSB first.
- **RTL**: `spi_master`, `clk_div` — master drives SCLK/MOSI/CS_N; divider produces clk_div_tick.
- **Basic testbench**: Directed test (start, data_in; wait for done). **No UVM** — UVM for SPI is Module 6.

### What You'll Learn

- **SPI mode 0**: SCLK idle low; capture on rising edge; change on falling edge; CS_N active low for frame.
- **RTL block architecture**: `clk_div` + `spi_master` hierarchy, FSM, and Mode 0 timing on the wire.
- **Baseline verification**: Directed stimulus, `done`-based checks, and optional waveform review (8 SCLK edges, MSB first).
- **Path to Module 6**: Same DUT, UVM agent with bus monitor on SCLK/MOSI/CS_N.

### Prerequisites

- Modules 1–4 (spec→RTL, UVM, UART baseline, UART UVM).
- Verilator, Make, C++ compiler. **No UVM required** for spi_baseline.

---

## Design Architecture

### 1. Block hierarchy

- **top_spi_baseline** → `clk_div` + `spi_master`; C++ supplies `clk`/`rst_n`.

### 2. SPI master RTL

- **clk_div**: `clk_div_tick` every `DIVIDER` clocks.
- **spi_master**: Mode 0; `cs_n` frames; MSB-first on `mosi`; `done` when complete.
- **Outputs**: `sclk` (idle low), `mosi`, `cs_n` — no `miso` in baseline.

### 3. Mode 0 timing on the wire

- Capture on rising SCLK; change MOSI on falling SCLK; 8 edges per byte.

---

## Verification & Testing Methods

### 1. Baseline goals

- Confirm Mode 0 serialization before SPI UVM (Module 6).

### 2. Directed test flow

- Pulse `start` + `data_in` (0x55, 0xAA); `wait(done)`; read `[PASS]` messages.

### 3. Waveform learning (optional)

- Count 8 SCLK cycles per frame; verify MSB-first bit order on MOSI.
- Defer MISO, multi-slave CS, and random data to Module 6.

---

## Key files to study

- `module5/examples/spi_baseline/dut/spi_master.v` — Mode 0 master
- `module5/examples/spi_baseline/dut/clk_div.v` — `clk_div_tick`
- `module5/examples/spi_baseline/top_spi_baseline.sv` — directed test
- `docs/SPI_LEARNING_GUIDE.md` — protocol reference

## Key Concepts

### 1. Synchronous serial (SPI)

- `sclk` defines bit times; unlike UART there is an explicit clock line.
- Mode 0: idle low, sample MOSI on rising edge, change on falling edge.

### 2. Chip select frames

- `cs_n` low defines one transfer; typically 8 SCLK cycles per byte.

## Common Pitfalls

1. **Wrong SPI mode in head**
   - **Mistake**: Sampling on falling edge when using Mode 0.
   - **Correct**: Rising edge capture, falling edge change for CPOL=0, CPHA=0.
   - **Why**: Bits will be shifted and MSB/LSB order will look wrong.

2. **Trusting `done` only**
   - **Mistake**: No waveform or bus check on MOSI/SCLK.
   - **Correct**: Optional VCD review or Module 6 monitor-based check.
   - **Why**: `done` only means the FSM finished, not that bits were correct.

---

## Topics Covered

### 1. SPI Protocol (Mode 0)

- **Signals**: sclk (serial clock), mosi (master out, slave in), cs_n (active-low chip select). Optional: miso (not used in this baseline).
- **Mode 0 (CPOL=0, CPHA=0)**: SCLK idles low; data captured on rising edge; data changed on falling edge.
- **Timing**: One bit per clk_div_tick; clk_div_tick derived from system clock via divider (e.g. DIVIDER=8).

### 2. Hands-on testbench (spi_baseline)

- **Directed test** in `top_spi_baseline.sv`: `start`, `data_in`, `wait(done)`.
- **Pass**: `[PASS]` lines and `SPI baseline test PASS`.

---

## Example: spi_baseline

#### Example 5.1: SPI baseline master (`module5/examples/spi_baseline/`)

**What it demonstrates:**

- SPI Mode 0 master RTL (`spi_master` + `clk_div`)
- Directed writes 0x55 and 0xAA with `start` / `wait(done)`
- Observing SCLK, MOSI, and CS_N timing in simulation (optional VCD)

```bash
cd module5/examples/spi_baseline
make run
```

| Component | Role |
|-----------|------|
| **dut/** | spi_master.v, clk_div.v |
| **top_spi_baseline.sv** | clk_div, spi_master; directed test in initial block |
| **sim_main.cpp** | Clock, reset; run until `$finish` |

Run: `cd module5/examples/spi_baseline && make run`

---

## Command Reference

```bash
cd module5/examples/spi_baseline
make run
```

```bash
./scripts/module5.sh --check   # Environment + example dirs
./scripts/module5.sh --run     # Run spi_baseline
```

---

## Learning Outcomes

- Describe SPI mode 0 and the role of sclk, mosi, cs_n, clk_div_tick.
- Explain the role of spi_master and clk_div.
- Run the spi_baseline example and interpret the directed test.
- Ready for Module 6: SPI UVM+SV verification.

---

## Exercises

1. **Run spi_baseline**
   - Run `make run` in `module5/examples/spi_baseline`. Confirm the directed test passes (e.g. expected bytes on MOSI).

2. **Trace one transfer**
   - Open `top_spi_baseline.sv` and DUT sources. For one byte (e.g. 0x55), trace: testbench asserts start and data_in → spi_master drives CS_N low, SCLK, and MOSI (MSB first, mode 0) → done pulses. Map SCLK edges (rising = capture, falling = change) to the RTL.

3. **Mode 0 timing**
   - In the monitor or RTL, identify where MOSI is sampled (rising SCLK) and where it changes (falling SCLK). Confirm this matches mode 0 (CPOL=0, CPHA=0).

4. **Optional: Waveforms**
   - If a VCD is generated, identify sclk, mosi, cs_n, start, done. Count 8 SCLK cycles per frame and verify MSB-first bit order.

---

## Assessment

- [ ] Can describe SPI mode 0 (idle low, capture on rising, change on falling) and signals sclk, mosi, cs_n.
- [ ] Can explain the role of spi_master and clk_div in the RTL.
- [ ] Can run spi_baseline and interpret the directed test result.
- [ ] Ready for Module 6: SPI UVM+SV verification.

---

## Next Steps

After completing this module, proceed to **Module 6: SPI UVM+SV** — full SPI verification with UVM (agent, sequences, driver, monitor, scoreboard).
