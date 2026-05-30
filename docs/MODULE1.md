# Module 1: Design & Verification Methodology (Part 1)

**Goal**: Understand the specification → RTL design flow, design methodology, and why we verify.

---

## Navigation

[← Previous: N/A (First Module)] | [Next: Module 2: Methodology (Part 2) →](MODULE2.md)

[↑ Back to README](../README.md)

---

## Before You Start (Learning Path)

1. **Read** [UNDERSTANDING_THE_SPEC.md](../module1/UNDERSTANDING_THE_SPEC.md) — how to read interface, behavior, and timing in a spec.
2. **Read** [SPEC_TO_RTL_GUIDE.md](../module1/SPEC_TO_RTL_GUIDE.md) — mapping spec sections to RTL structure.
3. **Skim** Design Architecture and Verification sections below, then run the **spec_to_rtl** example.
4. **Trace** one requirement in SPEC.md to a line in `dut/counter.v` and to a check in `sim_main.cpp`.

---

## Running Module 1

This module focuses on **methodology** only (no UVM, no protocol-specific content).

- **Module doc**: [module1/README.md](../module1/README.md)
- **Example**: [module1/examples/spec_to_rtl/](../module1/examples/spec_to_rtl/) — tiny spec → RTL → simulation

**For beginners**: To learn how to **understand a specification** and **translate it into RTL**, read in order: [UNDERSTANDING_THE_SPEC.md](../module1/UNDERSTANDING_THE_SPEC.md) → [SPEC_TO_RTL_GUIDE.md](../module1/SPEC_TO_RTL_GUIDE.md) → [spec_to_rtl WALKTHROUGH.md](../module1/examples/spec_to_rtl/WALKTHROUGH.md).

**Quick run** (from repo root):

```bash
cd module1/examples/spec_to_rtl
make run
```

Or use the module script:

```bash
./scripts/module1.sh --run
```

- **Slides & video**: [slides.pptx](../media/module1/slides.pptx) · [slides.pdf](../media/module1/slides.pdf) · [video.mp4](../media/module1/video.mp4) — regenerate: `./scripts/build_all_media.sh --module 1`

---

## Overview

Module 1 establishes the **design and verification mindset** you will use for UART, SPI, and I²C in later modules:

1. **Specification → RTL**: Start from a written spec (interface, behavior, timing) and implement it in RTL.
2. **Design methodology**: How to structure a small block (spec document, RTL, testbench).
3. **Intro to verification**: What we verify (correctness vs spec, corner cases) and why (bugs are cheaper to fix before tape-out).

### What You'll Learn

- **Spec-to-RTL flow**: From SPEC.md (or equivalent) to synthesizable Verilog/SystemVerilog.
- **Why verify**: The cost of bugs, and how directed tests (and later UVM) reduce risk.
- **Minimal toolchain**: Verilator + Make + C++ harness for RTL simulation (no UVM in this module).

### Prerequisites

- Linux/macOS/WSL2 with a terminal
- **Verilator** (5.x recommended)
- **GNU Make**
- **C++ compiler** (GCC or Clang)

UVM is **not** required for Module 1.

---

## Design Architecture

### 1. Artifact flow (spec_to_rtl)

- **SPEC.md** → requirements in plain language (interface, behavior, timing).
- **dut/counter.v** → synthesizable RTL implementing the spec.
- **top.v** → wrapper connecting DUT pins to the simulation harness.
- **sim_main.cpp** → clock, reset, stimulus, and result checking outside RTL.

### 2. Counter DUT structure

- **8-bit up-counter**: increments when `enable` is high; holds when disabled.
- **Reset**: synchronous active-low `rst_n` clears `count` to zero.
- **Ports**: `clk`, `rst_n`, `enable`, `count[7:0]` — map directly from the spec interface table.

### 3. Simulation harness attachment

- C++ generates `clk` and drives `rst_n` / `enable`; reads `count` each cycle.
- No SystemVerilog testbench yet — you will add structured TB/UVM in Module 2.

---

## Verification & Testing Methods

### 1. What we verify in Module 1

- RTL behavior matches **SPEC.md** (reset, enable gating, count progression).
- Directed scenario: release reset, enable for N cycles, expect `count == N`.

### 2. Stimulus and checking

- **Stimulus**: C++ toggles `enable` for a known number of clock cycles.
- **Check**: compare `count` to expected value; print PASS/FAIL.
- **Traceability**: each check should cite the spec sentence it proves.

### 3. What is not covered yet

- Random stimulus, functional coverage, scoreboards — Module 2 (UVM) and protocol modules.
- Use [UNDERSTANDING_THE_SPEC.md](../module1/UNDERSTANDING_THE_SPEC.md) and [SPEC_TO_RTL_GUIDE.md](../module1/SPEC_TO_RTL_GUIDE.md) while tracing the example.

---

## Key files to study

- `module1/examples/spec_to_rtl/SPEC.md` — requirements document
- `module1/examples/spec_to_rtl/dut/counter.v` — RTL implementation
- `module1/examples/spec_to_rtl/top.v` — DUT wrapper
- `module1/examples/spec_to_rtl/sim_main.cpp` — stimulus and checking

## Key Concepts

### 1. Specification first

- Interface, behavior, and timing live in SPEC.md before RTL.
- Every check in the testbench should trace to a spec sentence.

### 2. Traceability

- Spec line ↔ RTL line ↔ test expectation — practice for UART/SPI/I²C later.

## Common Pitfalls

1. **RTL before spec**
   - **Mistake**: Coding counters or FSMs without a written spec.
   - **Correct**: Complete SPEC.md (or equivalent) first.
   - **Why**: Reviewers and tests have no golden reference.

2. **Weak checks**
   - **Mistake**: Only printing values without comparing to expected results.
   - **Correct**: Explicit PASS/FAIL when `count != expected`.
   - **Why**: Simulation can run without verifying correctness.

---

## Topics Covered

### 1. Specification → RTL Design Flow

- **Specification**: Document interface (ports, widths, direction), behavior (reset, enable, state transitions), and timing (sync/async).
- **RTL**: Implement the spec in Verilog/SystemVerilog; each requirement in the spec should map to clear RTL (e.g., reset logic, enable gating, counter width).
- **Traceability**: Being able to point from a line in the spec to the RTL that implements it (and vice versa).

### 2. Design Methodology

- **Single block**: One spec, one (or a few) RTL files, one testbench.
- **Reuse**: The same flow (spec → RTL → testbench) scales to protocol blocks (UART, SPI, I²C) in Modules 3–8.
- **Documentation**: Keep SPEC.md (or similar) next to the RTL so that reviewers and verification can check against it.

### 3. Intro to Verification: What We Verify, and Why

- **What we verify**: That the RTL matches the specification (correct function, reset, enable, boundaries like count wrap).
- **Why we verify**: Finding bugs in RTL is far cheaper than finding them in silicon or in system integration; directed tests (and later UVM) give repeatable, automated checks.
- **Directed test**: A simple test that drives specific inputs (e.g., reset, then 10 enabled cycles) and checks expected outputs (e.g., count == 10). The spec_to_rtl example is a minimal directed test.

---

## Understanding the Spec and Translating to Design

Beginners can use these guides in order:

1. **[module1/UNDERSTANDING_THE_SPEC.md](../module1/UNDERSTANDING_THE_SPEC.md)** — How to read a specification: what to look for (interface, behavior, timing, edge cases), questions to answer, and a simple checklist before writing RTL.
2. **[module1/SPEC_TO_RTL_GUIDE.md](../module1/SPEC_TO_RTL_GUIDE.md)** — How to translate a spec into RTL: interface → ports, timing → always block, reset → first branch, normal behavior → remaining branches, edge cases, and traceability (spec ↔ RTL).
3. **[module1/examples/spec_to_rtl/WALKTHROUGH.md](../module1/examples/spec_to_rtl/WALKTHROUGH.md)** — Concrete walkthrough: the counter spec read section-by-section and each requirement mapped to the exact line in dut/counter.v.

---

## Example: spec_to_rtl

#### Example 1.1: Spec to RTL counter (`module1/examples/spec_to_rtl/`)

**What it demonstrates:**

- Reading SPEC.md and mapping each requirement to RTL in `dut/counter.v`
- Building a minimal top and C++ harness (clock, reset, enable)
- Directed verification: enable for N cycles and check `count == N`

```bash
cd module1/examples/spec_to_rtl
make run
```

The example in [module1/examples/spec_to_rtl/](../module1/examples/spec_to_rtl/) also documents:

| Step        | Artifact        | Description |
|------------|-----------------|-------------|
| **Spec**   | SPEC.md         | 8-bit up-counter: clk, rst_n, enable, count; behavior and timing. |
| **RTL**    | dut/counter.v   | Verilog implementation of that spec. |
| **Top**    | top.v           | Wrapper that instantiates the counter; C++ drives pins. |
| **Test**   | sim_main.cpp    | C++ harness: clock, reset, enable for 10 cycles; check count == 10. |

Run it:

```bash
cd module1/examples/spec_to_rtl
make run
```

Optional: `make run TRACE=1` to generate a VCD for waveform viewing.

---

## Command Reference

### Environment checks

```bash
verilator --version
make --version
```

### Build and run spec_to_rtl

```bash
cd module1/examples/spec_to_rtl
make run
```

### Module script (from repo root)

```bash
./scripts/module1.sh --check   # Environment only
./scripts/module1.sh --run     # Run spec_to_rtl
./scripts/module1.sh --help    # Options
```

---

## Learning Outcomes

By the end of Module 1, you should be able to:

- Describe the **specification → RTL** flow and why a written spec matters.
- Explain **what we verify** (RTL vs spec) and **why** (cost of bugs, repeatability).
- Run the **spec_to_rtl** example (make run) and relate SPEC.md, counter.v, and sim_main.cpp.
- Be ready for **Module 2**: basic testbench patterns and UVM+SV (agents, sequences, drivers, monitors, scoreboards) and toolchain (Verilator, UVM_HOME, Make).

---

## Exercises

1. **Read the spec and RTL**
   - Open [module1/examples/spec_to_rtl/SPEC.md](../module1/examples/spec_to_rtl/SPEC.md) and [dut/counter.v](../module1/examples/spec_to_rtl/dut/counter.v). Map each requirement in the spec to the corresponding RTL.

2. **Run and extend the test**
   - Run `make run` and confirm PASS. Change the test in sim_main.cpp (e.g., enable for 20 cycles and check count == 20, or test wrap from 255 to 0) and re-run.

3. **Optional: Trace**
   - Run `make run TRACE=1` and open the generated VCD in a waveform viewer. Identify clk, rst_n, enable, and count and confirm they match the spec.

---

## Assessment

- [ ] Can explain the spec → RTL flow and the role of a written specification.
- [ ] Can explain what we verify (RTL vs spec) and why verification is done.
- [ ] Can run the spec_to_rtl example and describe what SPEC.md, counter.v, and sim_main.cpp do.
- [ ] Ready to move to Module 2 (basic TB, UVM+SV, toolchain).

---

## Next Steps

After completing this module, proceed to **Module 2: Design & Verification Methodology (Part 2)** — basic testbench (directed tests, pin wiggling), evolution to UVM+SV (agents, sequences, drivers, monitors, scoreboards), and toolchain (Verilator, UVM_HOME, Make).
