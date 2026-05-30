        # Narration script — Module 1: Design & Verification Methodology (Part 1)

        **Target length:** ~17 minutes (47 slides; auto-generated — edit per slide as needed)

        ## Timing table

        | Slide | Section | Duration | Narration |
|-------|---------|----------|-----------|
| 1 | Module 1 | 0:25 | Welcome to module 1, Design & Verification Methodology (Part 1). In this module you will understand the specification → rtl design flow, design methodology, and why we verify.. |
| 2 | Learning objectives | 0:24 | Here is what you will learn in this module. Spec-to-RTL flow: From SPEC.md (or equivalent) to synthesizable Verilog/SystemVerilog. Why verify: The cost of bugs, and how directed tests (and later UVM) reduce risk. Minimal toolchain: Verilator + Make + C++ harness for RTL simulation (no UVM in this module). |
| 3 | Prerequisites | 0:28 | Before you start, make sure you have these prerequisites. Linux/macOS/WSL2 with a terminal Verilator (5.x recommended) GNU Make C++ compiler (GCC or Clang) |
| 4 | Learning path | 0:22 | Learning path. Understand the specification → RTL design flow, design methodology, and why we verify. |
| 5 | Overview | 0:16 | Overview. Module 1 establishes the design and verification mindset you will use for UART, SPI, and I²C in later modules: |
| 6 | How to learn this module | 0:08 | Next section: How to learn this module. |
| 7 | Suggested learning path | 0:28 | Follow this learning path. Read the guides before running the labs. Read UNDERSTANDING_THE_SPEC.md — how to read interface, behavior, and timing in a spec. Read SPEC_TO_RTL_GUIDE.md — mapping spec sections to RTL structure. Skim Design Architecture and Verification sections below, then run the spec_to_rtl example. Trace one requirement in SPEC.md to a line in dut/counter.v and to a check in... |
| 8 | Design architecture | 0:08 | Next section: Design architecture. |
| 9 | 1. Artifact flow (spec_to_rtl) | 0:38 | 1. Artifact flow (spec_to_rtl). SPEC.md → requirements in plain language (interface, behavior, timing). dut/counter.v → synthesizable RTL implementing the spec. top.v → wrapper connecting DUT pins to the simulation harness. sim_main.cpp → clock, reset, stimulus, and result checking outside RTL. Refer to the diagram on the right. |
| 10 | 2. Counter DUT structure | 0:34 | 2. Counter DUT structure. 8-bit up-counter: increments when enable is high; holds when disabled. Reset: synchronous active-low rst_n clears count to zero. Ports: clk, rst_n, enable, count[7:0] — map directly from the spec interface table. Refer to the diagram on the right. |
| 11 | 3. Simulation harness attachment | 0:30 | 3. Simulation harness attachment. C++ generates clk and drives rst_n / enable; reads count each cycle. No SystemVerilog testbench yet — you will add structured TB/UVM in Module 2. Refer to the diagram on the right. |
| 12 | RTL block diagram (reference) | 0:22 | RTL block diagram (reference). Module 1: DUT hierarchy and signal flow. |
| 13 | counter.v — spec in RTL | 0:28 | counter.v — spec in RTL. Review the code on screen and match it to files in the repository. |
| 14 | Execution & simulation flow | 0:08 | Next section: Execution & simulation flow. |
| 15 | How the example runs (toolchain) | 0:32 | How the example runs (toolchain). Match each bullet to files in the repository. Makefile: Verilator compiles RTL + SystemVerilog testbench into a C++ model sim_main.cpp: generates clk/rst_n, calls eval() until $finish Directed test (initial block or C++): drive stimulus, wait for DUT flags Self-check: compare outputs; print PASS/FAIL (see terminal demo slide) Repo path... |
| 16 | Makefile — Verilator build & run | 0:28 | Makefile — Verilator build & run. Review the code on screen and match it to files in the repository. |
| 17 | Key files to study | 0:08 | Next section: Key files to study. |
| 18 | Open these in the repo | 0:28 | Open these in the repo. module1/examples/spec_to_rtl/SPEC.md — requirements document module1/examples/spec_to_rtl/dut/counter.v — RTL implementation module1/examples/spec_to_rtl/top.v — DUT wrapper module1/examples/spec_to_rtl/sim_main.cpp — stimulus and checking Trace while running module1/EXAMPLES.md labs. |
| 19 | Verification & testing methods | 0:08 | Next section: Verification & testing methods. |
| 20 | 1. What we verify in Module 1 | 0:30 | 1. What we verify in Module 1. RTL behavior matches SPEC.md (reset, enable gating, count progression). Directed scenario: release reset, enable for N cycles, expect count == N. Refer to the diagram on the right. |
| 21 | 2. Stimulus and checking | 0:34 | 2. Stimulus and checking. Stimulus: C++ toggles enable for a known number of clock cycles. Check: compare count to expected value; print PASS/FAIL. Traceability: each check should cite the spec sentence it proves. Refer to the diagram on the right. |
| 22 | 3. What is not covered yet | 0:30 | 3. What is not covered yet. Random stimulus, functional coverage, scoreboards — Module 2 (UVM) and protocol modules. Use UNDERSTANDING_THE_SPEC.md and SPEC_TO_RTL_GUIDE.md while... Refer to the diagram on the right. |
| 23 | sim_main.cpp — directed check | 0:28 | sim_main.cpp — directed check. Review the code on screen and match it to files in the repository. |
| 24 | Syllabus topics | 0:08 | Next section: Syllabus topics. |
| 25 | 1. Specification → RTL Design Flow | 0:24 | 1. Specification → RTL Design Flow. Specification: Document interface (ports, widths, direction), behavior (reset, enable, state transitions), and timing (sync/async). RTL: Implement the spec in Verilog/SystemVerilog; each requirement in the spec should map to clear RTL (e.g., reset logic, enable... Traceability: Being able to point from a line in the spec to the RTL that implements it (and... |
| 26 | 2. Design Methodology | 0:24 | 2. Design Methodology. Single block: One spec, one (or a few) RTL files, one testbench. Reuse: The same flow (spec → RTL → testbench) scales to protocol blocks (UART, SPI, I²C) in Modules 3–8. Documentation: Keep SPEC.md (or similar) next to the RTL so that reviewers and verification can check against it. |
| 27 | 3. Intro to Verification: What We Verify, and Why | 0:24 | 3. Intro to Verification: What We Verify, and Why. What we verify: That the RTL matches the specification (correct function, reset, enable, boundaries like count wrap). Why we verify: Finding bugs in RTL is far cheaper than finding them in silicon or in system integration; directed tests (and later UVM)... Directed test: A simple test that drives specific inputs (e.g., reset, then 10 enabled... |
| 28 | Command reference highlights | 0:08 | Next section: Command reference highlights. |
| 29 | Environment checks | 0:16 | Environment checks. verilator --version Full detail in docs/MODULE1.md command reference. |
| 30 | Build and run spec_to_rtl | 0:16 | Build and run spec_to_rtl. cd module1/examples/spec_to_rtl Full detail in docs/MODULE1.md command reference. |
| 31 | Module script (from repo root) | 0:16 | Module script (from repo root). ./scripts/module1.sh --check # Environment only Full detail in docs/MODULE1.md command reference. |
| 32 | Hands-on examples | 0:08 | Next section: Hands-on examples. |
| 33 | Module 1 self-check | 0:45 | Module 1 self-check. Watch the terminal output and confirm you see the expected pass message. |
| 34 | Exercise scaffold | 0:28 | Exercise scaffold. Review the code on screen and match it to files in the repository. |
| 35 | Example 1: Spec to RTL counter | 0:24 | Example 1: Spec to RTL counter. Reading SPEC.md and mapping each requirement to RTL in dut/counter.v Building a minimal top and C++ harness (clock, reset, enable) Directed verification: enable for N cycles and check count == N module1/examples/spec_to_rtl/README.md |
| 36 | Demo: Spec to RTL counter | 0:45 | Demo: Spec to RTL counter. Watch the terminal output and confirm you see the expected pass message. |
| 37 | Key concepts | 0:08 | Next section: Key concepts. |
| 38 | 1. Specification first | 0:20 | 1. Specification first. Interface, behavior, and timing live in SPEC.md before RTL. Every check in the testbench should trace to a spec sentence. |
| 39 | 2. Traceability | 0:16 | 2. Traceability. Spec line ↔ RTL line ↔ test expectation — practice for UART/SPI/I²C later. |
| 40 | Common pitfalls | 0:08 | Next section: Common pitfalls. |
| 41 | RTL before spec | 0:24 | RTL before spec. Mistake: Coding counters or FSMs without a written spec. Correct: Complete SPEC.md (or equivalent) first. Why: Reviewers and tests have no golden reference. |
| 42 | Weak checks | 0:24 | Weak checks. Mistake: Only printing values without comparing to expected results. Correct: Explicit PASS/FAIL when count != expected. Why: Simulation can run without verifying correctness. |
| 43 | Practice & assessment | 0:08 | Next section: Practice & assessment. |
| 44 | What you should know | 0:28 | By now you should be able to explain the following. Describe the specification → RTL flow and why a written spec matters. Explain what we verify (RTL vs spec) and why (cost of bugs, repeatability). Run the spec_to_rtl example (make run) and relate SPEC.md, counter.v, and sim_main.cpp. Be ready for Module 2: basic testbench patterns and UVM+SV (agents, sequences, drivers, monitors, scoreboards)... |
| 45 | Exercises | 0:24 | Exercises. Read the spec and RTL Run and extend the test Optional: Trace |
| 46 | Assessment checklist | 0:28 | Assessment checklist. Can explain the spec → RTL flow and the role of a written specification. Can explain what we verify (RTL vs spec) and why verification is done. Can run the spec_to_rtl example and describe what SPEC.md, counter.v, and sim_main.cpp do. Ready to move to Module 2 (basic TB, UVM+SV, toolchain). |
| 47 | Summary & next steps | 0:28 | In summary: Understand the specification → RTL design flow, design methodology, and why we verify. Next up: Design & Verification Methodology (Part 2). Understand the specification → RTL design flow, design methodology, and why we verify. Complete module1/CHECKLIST.md Review module1/EXAMPLES.md and run each lab Next: Design & Verification Methodology (Part 2) |

        ## Section narration (edit for TTS)

        - **How to learn:** Read UNDERSTANDING_THE_SPEC.md — how to read interface, behavior, and timing in a spec. Then Read SPEC_TO_RTL_GUIDE.md — mapping spec sections to RTL structure. Then Skim Design Architecture and Verification sections below, then run the spec_to_rtl example. Then Trace one requirement in SPEC.md to a line in `dut/counter.v` and to a check in `sim_main.cpp`..
- **Design architecture (Artifact flow (spec_to_rtl), Counter DUT structure, Simulation harness attachment):** Walk through the block diagram, then relate each block to files under module1/examples/.
- **Verification (What we verify in Module 1, Stimulus and checking, What is not covered yet):** Explain what stimulus is applied, what is checked, and what is intentionally out of scope.
- **Syllabus:** Cover 3 topic section(s) — pause on protocol timing and signals.
- **Before exercises:** Ask learners to recall the learning outcomes slide; they should explain each bullet in their own words.
- **Hands-on:** Run module1/EXAMPLES.md labs; narrate expected PASS lines.

        ## Notes

        - Slides from **Before You Start**, **Design Architecture**, **Verification & Testing Methods**, **Topics Covered**, **EXAMPLES.md**, and **Learning Outcomes**.
        - Full detail: `docs/MODULE1.md` and `module1/EXAMPLES.md`.
        - Regenerate: `regenerate_course_outlines.sh <course_root> --module 1`
