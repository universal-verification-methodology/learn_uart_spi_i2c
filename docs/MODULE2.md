# Module 2: Design & Verification Methodology (Part 2)

**Goal**: Understand basic testbench patterns (directed tests, pin wiggling), the evolution to a UVM+SV testbench (agents, sequences, drivers, monitors, scoreboards), and the toolchain (Verilator, UVM_HOME, Make).

---

## Navigation

[← Previous: Module 1: Methodology (Part 1)](MODULE1.md) | [Next: Module 3: UART →](MODULE3.md)

[↑ Back to README](../README.md)

---

## Before You Start (Learning Path)

1. **Complete Module 1** — run `spec_to_rtl` and understand spec → RTL → directed check.
2. **Read** this module’s Design Architecture and Verification sections before `uvm_smoke`.
3. **Set UVM_HOME** (or use vendored UVM under `tools/`) — see Command Reference.
4. **Run** `uvm_smoke` and trace one transaction from sequence → driver → DUT → monitor → scoreboard.

---

## Running Module 2

This module focuses on **verification methodology** and **toolchain** (no UART/SPI/I²C yet—those start in Module 3).

- **Module doc**: [module2/README.md](../module2/README.md)
- **Example**: [module2/examples/uvm_smoke/](../module2/examples/uvm_smoke/) — tiny DUT + full UVM test (transaction, sequence, driver, monitor, scoreboard)

**Quick run** (from repo root):

```bash
cd module2/examples/uvm_smoke
make SIM=verilator TEST=test_uvm_smoke
```

Or use the module script:

```bash
./scripts/module2.sh --run
```

- **Slides & video**: [slides.pptx](../media/module2/slides.pptx) · [slides.pdf](../media/module2/slides.pdf) · [video.mp4](../media/module2/video.mp4) — regenerate: `./scripts/build_all_media.sh --module 2`

---

## Overview

Module 2 builds on Module 1 (spec → RTL) by focusing on **how we verify**:

1. **Basic testbench**: Directed tests, pin wiggling — drive inputs, check outputs. (You saw a minimal version in Module 1’s spec_to_rtl C++ harness.)
2. **UVM+SV**: A structured testbench with **transactions**, **sequences**, **drivers**, **monitors**, and **scoreboards** — the same pattern used for UART/SPI/I²C in later modules.
3. **Toolchain**: Verilator + UVM_HOME + Make — build and run a UVM test on RTL.

### What You'll Learn

- **Basic TB vs UVM**: From “wiggle pins and check” to “transaction → sequence → driver/monitor → scoreboard.”
- **UVM building blocks**: Transaction (sequence item), sequence, driver, monitor, scoreboard, agent, env, test.
- **Toolchain**: UVM_HOME, include paths, Verilator flags (`-sv`, `--timing`, `--trace`), and `make SIM=verilator TEST=...`.

### Prerequisites

- **Module 1** completed (spec → RTL flow, spec_to_rtl example run).
- **Verilator** (5.036+)
- **GNU Make** and **C++ compiler**
- **UVM**: UVM_HOME set (must contain `src/uvm_pkg.sv`) or vendored UVM in the repo (see uvm_smoke Makefile)

---

## Design Architecture

### 1. DUT and interface

- **simple_register.v**: `enable`, `d`, `q` — minimal storage for learning UVM data flow.
- **reg_if**: virtual interface bundling `clk`, `rst_n`, `enable`, `d`, `q` for the agent.

### 2. UVM component hierarchy

- **RegTransaction** → one write operation (data + enable + observed q).
- **RegSequence** → stream of directed transactions.
- **RegDriver** / **RegMonitor** → drive pins / sample pins each cycle.
- **RegScoreboard** → expected queue vs observed.
- **RegAgent**, **RegEnv**, **RegTest** — standard UVM layering used again in Modules 4, 6, 8.

### 3. Build and simulation flow

- Verilator compiles SV + UVM + C++; `+UVM_TESTNAME` selects the test.
- Phases: build → connect → run (objections hold simulation until sequence completes).

---

## Verification & Testing Methods

### 1. Transaction-level verification

- Stimulus is a **transaction** (what to write), not raw pin wiggles in `initial` blocks.
- The **monitor** reconstructs what happened on the bus; the **scoreboard** compares to expected.

### 2. Directed regression in uvm_smoke

- Fixed sequence: 0x00, 0x01, 0x55, 0xAA, 0xFF — repeatable, easy to debug.
- Pass criteria: scoreboard reports matches, zero mismatches.

### 3. Skills you reuse on UART/SPI/I²C

- Same agent pattern; only the **transaction** and **protocol timing** in driver/monitor change.
- Read UVM log lines: DRIVER, MONITOR, SCOREBOARD, final summary.

---

## Key files to study

- `module2/examples/uvm_smoke/dut/simple_register.v` — tiny DUT
- `module2/examples/uvm_smoke/test_uvm_smoke.sv` — transaction, agent, scoreboard
- `module2/examples/uvm_smoke/Makefile` — Verilator + UVM build

## Key Concepts

### 1. Transaction-level TB

- Stimulus is a **transaction** (what to do), not raw pin toggles in one big `initial` block.
- Driver converts transactions to pin activity; monitor converts pins back to transactions.

### 2. Scoreboard closure

- Expected queue vs observed values — same pattern for UART/SPI/I²C UVM modules.

## Common Pitfalls

1. **Skipping monitor or scoreboard**
   - **Mistake**: Only driving the DUT and eyeballing waves.
   - **Correct**: Monitor + scoreboard automate expected vs observed.
   - **Why**: Scales when you add dozens of tests.

2. **UVM_HOME not set**
   - **Mistake**: Build fails with missing `uvm_pkg.sv`.
   - **Correct**: Export UVM_HOME or use vendored UVM under `tools/`.
   - **Why**: Compiler cannot find UVM includes.

---

## Topics Covered

### 1. Basic Testbench (Directed Tests, Pin Wiggling)

- **Directed test**: Drive specific inputs (e.g., reset, then a fixed sequence of data) and check expected outputs (e.g., register value, count).
- **Pin wiggling**: The testbench directly drives and samples DUT pins (clock, reset, data, enable) — no transaction layer yet.
- **Relation to Module 1**: The spec_to_rtl example used a C++ harness to drive clk/rst_n/enable and check count; that’s a minimal directed test. Here we keep the same idea but structure it with UVM (transactions, driver, monitor, scoreboard).

### 2. Evolution to UVM+SV Testbench

- **Transaction** (`uvm_sequence_item`): Represents “one operation” (e.g., one write to a register: data + enable). The sequence produces transactions; the driver turns them into pin activity; the monitor turns pin activity back into transactions.
- **Sequence**: Produces a stream of transactions (e.g., a few directed values: 0x00, 0x01, 0x55, 0xAA, 0xFF). Can be deterministic (directed) or random (later).
- **Driver**: Gets transactions from the sequencer and drives the DUT interface (e.g., set enable and d on the bus, wait for clock).
- **Monitor**: Observes the DUT interface and turns pin activity into transactions, then sends them to the scoreboard via an analysis port.
- **Scoreboard**: Compares “expected” (what we sent) vs “observed” (what the monitor saw). Reports matches/mismatches.
- **Agent**: Groups driver, monitor, and sequencer for one interface. **Env**: Contains agent(s) and scoreboard. **Test**: Builds the env, starts the sequence, raises/drops objections.

This structure scales: for UART (Module 4), SPI (Module 6), and I²C (Module 8) you will have a protocol-specific transaction, sequence, driver, monitor, and scoreboard, but the same UVM pattern.

### 3. Toolchain (Verilator, UVM_HOME, Make)

- **Verilator**: Compiles SystemVerilog (including UVM) + C++ into an executable. Key flags: `-sv`, `--timing`, `--trace`, `--binary`, include paths for UVM.
- **UVM_HOME**: Points to the UVM library root; the build uses `$(UVM_HOME)/src/uvm_pkg.sv` and `+incdir+$(UVM_HOME)/src`. If not set, the uvm_smoke Makefile can fall back to a vendored UVM under `tools/`.
- **Make**: One target to compile (Verilator + make in obj_dir), one to run (`./obj_dir/Vtest_uvm_smoke +UVM_TESTNAME=...`). Same pattern for UART/SPI/I²C UVM tests later.

---

## Example: uvm_smoke

#### Example 2.1: UVM smoke test (`module2/examples/uvm_smoke/`)

**What it demonstrates:**

- UVM transaction, sequence, driver, monitor, and scoreboard on a tiny register DUT
- How objections start and end the test in `run_phase`
- Interpreting DRIVER / MONITOR / SCOREBOARD messages and match counts

```bash
cd module2/examples/uvm_smoke
make SIM=verilator TEST=test_uvm_smoke
```

The example in [module2/examples/uvm_smoke/](../module2/examples/uvm_smoke/) also documents:

| Component   | Role |
|------------|------|
| **DUT**    | `dut/simple_register.v` — tiny register (clk, rst_n, enable, d, q). |
| **Interface** | `reg_if` — connects testbench to DUT. |
| **Transaction** | `RegTransaction` — data + enable + observed_q. |
| **Sequence** | `RegSequence` — produces 5 directed transactions (0x00, 0x01, 0x55, 0xAA, 0xFF). |
| **Driver** | `RegDriver` — drives enable and d from transaction; waits for clock. |
| **Monitor** | `RegMonitor` — samples enable, d, q each cycle; writes transaction to scoreboard. |
| **Scoreboard** | `RegScoreboard` — compares expected vs observed; reports matches/mismatches. |
| **Test**     | `RegTest` — builds env, queues expected values, starts sequence, objections. |

Run it:

```bash
cd module2/examples/uvm_smoke
make SIM=verilator TEST=test_uvm_smoke
```

You should see UVM phases, DRIVER/MONITOR/SCOREBOARD messages, and a final scoreboard summary.

---

## Command Reference

### Environment checks

```bash
verilator --version
make --version
echo "$UVM_HOME"
ls "$UVM_HOME/src/uvm_pkg.sv"
```

### Build and run uvm_smoke

```bash
cd module2/examples/uvm_smoke
make SIM=verilator TEST=test_uvm_smoke
```

### Module script (from repo root)

```bash
./scripts/module2.sh --check   # Environment + UVM + example dirs
./scripts/module2.sh --run     # Run uvm_smoke
./scripts/module2.sh --help    # Options
```

---

## Learning Outcomes

By the end of Module 2, you should be able to:

- Explain **basic testbench** (directed tests, pin wiggling) and how it evolves into **UVM** (transaction, sequence, driver, monitor, scoreboard).
- Describe the role of **transaction**, **sequence**, **driver**, **monitor**, **scoreboard**, **agent**, **env**, and **test** in a UVM testbench.
- Run the **uvm_smoke** example (make SIM=verilator TEST=test_uvm_smoke) and interpret UVM output.
- Use the **toolchain**: Verilator, UVM_HOME, Make; know why `-sv`, `--timing`, and include paths are needed.
- Be ready for **Module 3**: UART protocol + RTL + basic (non-UVM) testbench.

---

## Exercises

1. **Run uvm_smoke**
   - Run `make SIM=verilator TEST=test_uvm_smoke` in module2/examples/uvm_smoke. Confirm you see DRIVER, MONITOR, SCOREBOARD messages and a final “Matches: 5, Mismatches: 0” (or similar).

2. **Traceability**
   - Open test_uvm_smoke.sv. For one transaction (e.g., 0x55), trace: sequence creates it → driver drives enable/d → DUT updates q → monitor samples q → scoreboard compares. Map each step to the corresponding class and method.

3. **Change the sequence**
   - Add or change one value in RegSequence (e.g., add 0x11). Update the expected queue in RegTest’s run_phase to match. Re-run and confirm the scoreboard still passes.

4. **Optional: Waveforms**
   - If the Makefile enables `--trace`, inspect the generated VCD. Identify clk, rst_n, enable, d, q and confirm they match the sequence.

---

## Assessment

- [ ] Can explain basic TB vs UVM (transaction, sequence, driver, monitor, scoreboard).
- [ ] Can describe the role of UVM_HOME, Verilator flags, and Make in building/running a UVM test.
- [ ] Can run uvm_smoke and interpret the output.
- [ ] Ready to move to Module 3 (UART protocol + RTL + basic testbench).

---

## Next Steps

After completing this module, proceed to **Module 3: UART** — UART protocol details, translating protocol to RTL (TX/RX, baud gen), RTL implementation, and **basic** (non-UVM or minimal SV) testbench. UVM verification for UART follows in Module 4.
