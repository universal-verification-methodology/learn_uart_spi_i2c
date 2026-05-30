# Module 4: UART — UVM+SV Verification

**Goal**: Extend UART verification to **UVM+SV** — UART agent (transaction, sequence, driver, monitor, scoreboard); run on Verilator.

---

## Navigation

[← Previous: Module 3: UART →](MODULE3.md) | [Next: Module 5: SPI →](MODULE5.md)

[↑ Back to README](../README.md)

---

## Before You Start (Learning Path)

This module applies **UVM** to the UART DUT. Before running commands:

1. **Read the detailed UART learning guide**: [UART_LEARNING_GUIDE.md](UART_LEARNING_GUIDE.md) — what UART is, how it works (frame, baud, TX/RX), and how it maps to our RTL.
2. **Read the protocols + UVM overview**: [LEARNING_GUIDE_PROTOCOLS_AND_UVM.md](LEARNING_GUIDE_PROTOCOLS_AND_UVM.md) — **Part B § 5. How UVM Maps to a Protocol** and **§ 6. UART UVM Mapping** (where UVM sits, how transaction/driver/monitor/scoreboard map to UART).

Then follow **Overview** → **Topics Covered** → **Example** → **Exercises**.

---

## Running Module 4

- **Module doc**: [module4/README.md](../module4/README.md)
- **Example**: [module4/examples/uart_uvm/](../module4/examples/uart_uvm/) — UART RTL + full UVM agent (same DUT as Module 3)

**Quick run** (from repo root):

```bash
cd module4/examples/uart_uvm
make SIM=verilator TEST=test_uart_uvm
```

Or: `./scripts/module4.sh --run`

- **Slides & video**: [slides.pptx](../media/module4/slides.pptx) · [slides.pdf](../media/module4/slides.pdf) · [video.mp4](../media/module4/video.mp4) — regenerate: `./scripts/build_all_media.sh --module 4`

---

## Overview

Module 4 builds on Module 3 (UART protocol + RTL + basic testbench):

- **Same DUT**: uart_tx, uart_rx, baud_gen (reused from module3/examples/uart_baseline).
- **UVM testbench**: UART agent — transaction (byte to send), sequence (directed bytes: 0x00, 0x01, 0x55, 0xAA, 0xFF), driver (start/data, wait for baud_tick), monitor (observe tx line, reconstruct byte), scoreboard (expected vs observed).
- **Loopback**: TX output → RX input; scoreboard checks both TX (monitor observes serial line) and RX (hook from DUT rx_valid/rx_data).
- **Toolchain**: Verilator + UVM_HOME + Make (same as Module 2).

### What You'll Learn

- **UART UVM agent**: Transaction (UartTxTransaction), sequence (UartTxSequence), driver (UartTxDriver), monitor (UartTxMonitor), scoreboard (UartTxScoreboard).
- **Interface**: uart_tx_if (clk, rst_n, start, data, tx, baud_tick) connects UVM to DUT.
- **Loopback check**: TX path (driver → DUT → monitor → scoreboard) and RX path (DUT rx_valid/rx_data → scoreboard.check_rx_byte).

### Prerequisites

- Module 1 (spec → RTL), Module 2 (UVM+SV, uvm_smoke), Module 3 (UART protocol + RTL + basic TB).
- Verilator, Make, C++ compiler, **UVM** (UVM_HOME or vendored UVM).

---

## Design Architecture

### 1. UART DUT (reused from Module 3)

- **dut/**: `uart_tx`, `uart_rx`, `baud_gen` — identical RTL to `uart_baseline`.
- **Loopback** in top: `rx = tx` for closed-loop checking.
- **Why reuse**: Upgrade verification (UVM) without touching proven RTL.

### 2. UVM testbench hierarchy

- **uart_tx_if**: virtual interface for driver/monitor.
- **UartTxTransaction / Sequence / Driver / Monitor / Scoreboard / Agent / Env / Test** — same pattern as `uvm_smoke`.
- **Monitor** reconstructs bytes from the serial `tx` line using UART 8N1 rules.

### 3. Dual check paths

- **TX path**: sequence → driver → DUT → monitor → scoreboard (`observed_tx`).
- **RX path**: loopback into `uart_rx`; `check_rx_byte()` when `data_valid` asserts.

---

## Verification & Testing Methods

### 1. Directed UART regression

- Sequence sends 0x00, 0x01, 0x55, 0xAA, 0xFF — repeatable regression before randomization.

### 2. Scoreboard strategy

- Expected queue loaded in test; compare to monitor-reconstructed TX and to RX hook data.
- Fail fast on mismatch; read UVM SCOREBOARD summary at end of run.

### 3. What to add next

- Random baud, framing-error injection, coverage on `busy` / `data_valid`.
- See [LEARNING_GUIDE_PROTOCOLS_AND_UVM.md § 6](LEARNING_GUIDE_PROTOCOLS_AND_UVM.md#6-uart-uvm-mapping-module-4).

---

## Key files to study

- `module4/examples/uart_uvm/dut/` — same UART RTL as Module 3
- `module4/examples/uart_uvm/test_uart_uvm.sv` — agent, env, loopback hooks
- `docs/LEARNING_GUIDE_PROTOCOLS_AND_UVM.md` — § 6 UART UVM mapping

## Key Concepts

### 1. Reuse DUT, upgrade TB

- RTL unchanged from baseline; UVM replaces directed `initial` stimulus.

### 2. Dual path checking

- TX monitor reconstructs serial bytes; RX hook checks loopback `data_valid`.

## Common Pitfalls

1. **Monitor baud mismatch**
   - **Mistake**: Sampling `tx` at system clock instead of `baud_tick` times.
   - **Correct**: One sample per `baud_tick` per UART rules (as in UartTxMonitor).
   - **Why**: Reconstructed byte will not match driven data.

2. **Forgetting loopback RX check**
   - **Mistake**: Scoreboard only compares TX monitor output.
   - **Correct**: Also call `check_rx_byte` when `data_valid` asserts.
   - **Why**: TX path can pass while RX is broken.

---

## Topics Covered

### 1. UART protocol recap (8N1)

- One byte = start (0) + 8 data (LSB first) + stop (1); `baud_tick` times each bit.
- Driver/monitor must follow the same rules as the RTL.

### 2. Toolchain

- Verilator `-sv`, `--timing`, UVM includes; `make SIM=verilator TEST=test_uart_uvm`; `+UVM_TESTNAME=UartTxTest`.

---

## Example: uart_uvm

#### Example 4.1: UART UVM agent (`module4/examples/uart_uvm/`)

**What it demonstrates:**

- Same UART DUT as Module 3 with a full UVM agent (sequence, driver, monitor, scoreboard)
- Monitor reconstructs bytes from the serial `tx` line
- Loopback RX checking via `check_rx_byte` in the scoreboard

```bash
cd module4/examples/uart_uvm
make SIM=verilator TEST=test_uart_uvm
```

| Component | Role |
|-----------|------|
| **dut/** | uart_tx.v, uart_rx.v, baud_gen.v (same as Module 3) |
| **test_uart_uvm.sv** | Interface, UartTxTransaction, UartTxSequence, UartTxDriver, UartTxMonitor, UartTxScoreboard, UartTxAgent, UartTxEnv, UartTxTest; top with DUT, loopback, baud_gen, clock/reset, RX scoreboard hook |

Run: `cd module4/examples/uart_uvm && make SIM=verilator TEST=test_uart_uvm`

---

## Command Reference

```bash
cd module4/examples/uart_uvm
make SIM=verilator TEST=test_uart_uvm
```

```bash
./scripts/module4.sh --check   # Environment + UVM + example dirs
./scripts/module4.sh --run     # Run uart_uvm
```

---

## Learning Outcomes

- Describe the UART UVM agent (transaction, sequence, driver, monitor, scoreboard).
- Explain loopback (TX→RX) and how TX and RX are both checked in the scoreboard.
- Run the uart_uvm example and interpret UVM output.
- Ready for Module 5: SPI protocol + RTL + basic testbench.

---

## Where UVM Applies (Recap)

UVM is used **only in the testbench**: it does not replace the UART RTL. The **transaction** represents one byte; the **driver** drives the DUT interface per UART timing (start, data, wait for frame); the **monitor** observes the serial line and reconstructs bytes; the **scoreboard** compares expected vs observed. See [LEARNING_GUIDE_PROTOCOLS_AND_UVM.md § 6](LEARNING_GUIDE_PROTOCOLS_AND_UVM.md#6-uart-uvm-mapping-module-4) for the full mapping.

---

## Exercises

1. **Run uart_uvm**
   - Run `make SIM=verilator TEST=test_uart_uvm` in `module4/examples/uart_uvm`. Confirm UVM phases, DRIVER/MONITOR/SCOREBOARD messages, and scoreboard pass (e.g. matches, no mismatches).

2. **Trace one transaction**
   - Open the test and agent sources. For one transaction (e.g. 0x55), trace: sequence creates transaction → driver drives start/data → DUT TX sends frame → monitor observes tx line and reconstructs byte → scoreboard compares expected vs observed. Map each step to the corresponding UVM class/method.

3. **Change the sequence**
   - Add or change one value in the UART sequence (e.g. add 0x11). Update the expected values in the test/scoreboard to match. Re-run and confirm the scoreboard still passes.

4. **Optional: Loopback path**
   - Identify where the RX path is checked (e.g. rx_valid/rx_data hook to scoreboard). Explain how both TX (monitor on serial line) and RX (loopback) are verified.

---

## Assessment

- [ ] Can describe the UART UVM agent: transaction (one byte), sequence, driver, monitor, scoreboard.
- [ ] Can explain loopback and how TX and RX are both checked.
- [ ] Can run uart_uvm and interpret UVM output (phases, scoreboard summary).
- [ ] Ready for Module 5: SPI protocol + RTL + basic testbench.

---

## Next Steps

After completing this module, proceed to **Module 5: SPI** — SPI protocol details, RTL (master, mode 0), and basic (non-UVM) testbench.
