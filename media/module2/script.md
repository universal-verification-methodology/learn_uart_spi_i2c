        # Narration script — Module 2: Design & Verification Methodology (Part 2)

        **Target length:** ~19 minutes (50 slides; auto-generated — edit per slide as needed)

        ## Timing table

        | Slide | Section | Duration | Narration |
|-------|---------|----------|-----------|
| 1 | Module 2 | 0:25 | Welcome to module 2, Design & Verification Methodology (Part 2). In this module you will understand basic testbench patterns (directed tests, pin wiggling), the evolution to a uvm+sv testbench (agents, sequences, drivers, monitors, scoreboards), and the toolchain (verilator, uvm_home, make).. |
| 2 | Learning objectives | 0:24 | Here is what you will learn in this module. Basic TB vs UVM: From “wiggle pins and check” to “transaction → sequence → driver/monitor → scoreboard.” UVM building blocks: Transaction (sequence item), sequence, driver, monitor, scoreboard, agent, env, test. Toolchain: UVM_HOME, include paths, Verilator flags (-sv, --timing, --trace), and make SIM=verilator TEST=.... |
| 3 | Prerequisites | 0:28 | Before you start, make sure you have these prerequisites. Module 1 completed (spec → RTL flow, spec_to_rtl example run). Verilator (5.036+) GNU Make and C++ compiler UVM: UVM_HOME set (must contain src/uvm_pkg.sv) or vendored UVM in the repo (see uvm_smoke Makefile) |
| 4 | Learning path | 0:22 | Learning path. Understand basic testbench patterns (directed tests, pin wiggling), the evolution to a UVM+SV testbench (agents, sequences, drivers, monitors, scoreboards), and the toolchain (Verilator, UVM_HOME... |
| 5 | Overview | 0:16 | Overview. Module 2 builds on Module 1 (spec → RTL) by focusing on how we verify: |
| 6 | How to learn this module | 0:08 | Next section: How to learn this module. |
| 7 | Suggested learning path | 0:28 | Follow this learning path. Read the guides before running the labs. Complete Module 1 — run spec_to_rtl and understand spec → RTL → directed check. Read this module’s Design Architecture and Verification sections before uvm_smoke. Set UVM_HOME (or use vendored UVM under tools/) — see Command Reference. Run uvm_smoke and trace one transaction from sequence → driver → DUT → monitor → scoreboard... |
| 8 | Design architecture | 0:08 | Next section: Design architecture. |
| 9 | 1. DUT and interface | 0:30 | 1. DUT and interface. simple_register.v: enable, d, q — minimal storage for learning UVM data flow. reg_if: virtual interface bundling clk, rst_n, enable, d, q for the agent. Refer to the diagram on the right. |
| 10 | 2. UVM component hierarchy (1/2) | 0:38 | 2. UVM component hierarchy (1/2). RegTransaction → one write operation (data + enable + observed q). RegSequence → stream of directed transactions. RegDriver / RegMonitor → drive pins / sample pins each cycle. RegScoreboard → expected queue vs observed. Refer to the diagram on the right. |
| 11 | 2. UVM component hierarchy (2/2) | 0:16 | 2. UVM component hierarchy (2/2). RegAgent, RegEnv, RegTest — standard UVM layering used again in Modules 4, 6, 8. |
| 12 | 3. Build and simulation flow | 0:30 | 3. Build and simulation flow. Verilator compiles SV + UVM + C++; +UVM_TESTNAME selects the test. Phases: build → connect → run (objections hold simulation until sequence completes). Refer to the diagram on the right. |
| 13 | RTL block diagram (reference) | 0:22 | RTL block diagram (reference). Module 2: DUT hierarchy and signal flow. |
| 14 | Verification / testbench diagram (reference) | 0:22 | Verification / testbench diagram (reference). Module 2: stimulus, observation, and checking. |
| 15 | RegTransaction — UVM item | 0:28 | RegTransaction — UVM item. Review the code on screen and match it to files in the repository. |
| 16 | Execution & simulation flow | 0:08 | Next section: Execution & simulation flow. |
| 17 | How the example runs (toolchain) | 0:32 | How the example runs (toolchain). Match each bullet to files in the repository. Makefile: Verilator + UVM_HOME compile RTL, interface, and test_*.sv UVM phases: build → connect → run_test → report (same pattern as Module 2) Sequence → driver → DUT → monitor → scoreboard (read SCOREBOARD at end) Typical command: make SIM=verilator TEST=test_* (see module2 demo slide) Loopback / hooks connect... |
| 18 | Example directory layout (1) | 0:32 | Example directory layout (1). Match each bullet to files in the repository. DUT: dut/simple_register.v — tiny register (clk, rst_n, enable, d, q). Interface: reg_if — connects testbench to DUT. Transaction: RegTransaction — data + enable + observed_q. Sequence: RegSequence — produces 5 directed transactions (0x00, 0x01, 0x55, 0xAA, 0xFF). Driver: RegDriver — drives enable and d from... |
| 19 | Example directory layout (2) | 0:24 | Example directory layout (2). Match each bullet to files in the repository. Monitor: RegMonitor — samples enable, d, q each cycle; writes transaction to scoreboard. Scoreboard: RegScoreboard — compares expected vs observed; reports matches/mismatches. Test: RegTest — builds env, queues expected values, starts sequence, objections. Match each path to files under module/examples/. |
| 20 | Makefile — UVM + Verilator | 0:28 | Makefile — UVM + Verilator. Review the code on screen and match it to files in the repository. |
| 21 | Key files to study | 0:08 | Next section: Key files to study. |
| 22 | Open these in the repo | 0:24 | Open these in the repo. module2/examples/uvm_smoke/dut/simple_register.v — tiny DUT module2/examples/uvm_smoke/test_uvm_smoke.sv — transaction, agent, scoreboard module2/examples/uvm_smoke/Makefile — Verilator + UVM build Trace while running module2/EXAMPLES.md labs. |
| 23 | Verification & testing methods | 0:08 | Next section: Verification & testing methods. |
| 24 | 1. Transaction-level verification | 0:30 | 1. Transaction-level verification. Stimulus is a transaction (what to write), not raw pin wiggles in initial blocks. The monitor reconstructs what happened on the bus; the scoreboard compares to expected. Refer to the diagram on the right. |
| 25 | 2. Directed regression in uvm_smoke | 0:30 | 2. Directed regression in uvm_smoke. Fixed sequence: 0x00, 0x01, 0x55, 0xAA, 0xFF — repeatable, easy to debug. Pass criteria: scoreboard reports matches, zero mismatches. Refer to the diagram on the right. |
| 26 | 3. Skills you reuse on UART/SPI/I²C | 0:30 | 3. Skills you reuse on UART/SPI/I²C. Same agent pattern; only the transaction and protocol timing in driver/monitor change. Read UVM log lines: DRIVER, MONITOR, SCOREBOARD, final summary. Refer to the diagram on the right. |
| 27 | Syllabus topics | 0:08 | Next section: Syllabus topics. |
| 28 | 1. Basic Testbench (Directed Tests, Pin Wiggling) | 0:24 | 1. Basic Testbench (Directed Tests, Pin Wiggling). Directed test: Drive specific inputs (e.g., reset, then a fixed sequence of data) and check expected outputs (e.g., register value, count). Pin wiggling: The testbench directly drives and samples DUT pins (clock, reset, data, enable) — no transaction layer yet. Relation to Module 1: The spec_to_rtl example used a C++ harness to drive... |
| 29 | 2. Evolution to UVM+SV Testbench | 0:36 | 2. Evolution to UVM+SV Testbench. Transaction (uvm_sequence_item): Represents “one operation” (e.g., one write to a register: data + enable). The sequence produces... Sequence: Produces a stream of transactions (e.g., a few directed values: 0x00, 0x01, 0x55, 0xAA, 0xFF). Can be deterministic (directed)... Driver: Gets transactions from the sequencer and drives the DUT interface (e.g., set... |
| 30 | 3. Toolchain (Verilator, UVM_HOME, Make) | 0:24 | 3. Toolchain (Verilator, UVM_HOME, Make). Match each bullet to files in the repository. Verilator: Compiles SystemVerilog (including UVM) + C++ into an executable. Key flags: -sv, --timing, --trace, --binary, include... UVM_HOME: Points to the UVM library root; the build uses $(UVM_HOME)/src/uvm_pkg.sv and +incdir+$(UVM_HOME)/src. If not set, the... Make: One target to compile (Verilator +... |
| 31 | Command reference highlights | 0:08 | Next section: Command reference highlights. |
| 32 | Environment checks | 0:16 | Environment checks. verilator --version Full detail in docs/MODULE2.md command reference. |
| 33 | Build and run uvm_smoke | 0:16 | Build and run uvm_smoke. cd module2/examples/uvm_smoke Full detail in docs/MODULE2.md command reference. |
| 34 | Module script (from repo root) | 0:16 | Module script (from repo root). ./scripts/module2.sh --check # Environment + UVM + example dirs Full detail in docs/MODULE2.md command reference. |
| 35 | Hands-on examples | 0:08 | Next section: Hands-on examples. |
| 36 | Module 2 self-check | 0:45 | Module 2 self-check. Watch the terminal output and confirm you see the expected pass message. |
| 37 | Exercise scaffold | 0:28 | Exercise scaffold. Review the code on screen and match it to files in the repository. |
| 38 | Example 1: UVM smoke test | 0:24 | Example 1: UVM smoke test. UVM transaction, sequence, driver, monitor, and scoreboard on a tiny register DUT How objections start and end the test in run_phase Interpreting DRIVER / MONITOR / SCOREBOARD messages and match counts module2/examples/uvm_smoke/README.md |
| 39 | Demo: UVM smoke test | 0:45 | Demo: UVM smoke test. Watch the terminal output and confirm you see the expected pass message. |
| 40 | Key concepts | 0:08 | Next section: Key concepts. |
| 41 | 1. Transaction-level TB | 0:20 | 1. Transaction-level TB. Stimulus is a transaction (what to do), not raw pin toggles in one big initial block. Driver converts transactions to pin activity; monitor converts pins back to transactions. |
| 42 | 2. Scoreboard closure | 0:16 | 2. Scoreboard closure. Expected queue vs observed values — same pattern for UART/SPI/I²C UVM modules. |
| 43 | Common pitfalls | 0:08 | Next section: Common pitfalls. |
| 44 | Skipping monitor or scoreboard | 0:24 | Skipping monitor or scoreboard. Mistake: Only driving the DUT and eyeballing waves. Correct: Monitor + scoreboard automate expected vs observed. Why: Scales when you add dozens of tests. |
| 45 | UVM_HOME not set | 0:24 | UVM_HOME not set. Mistake: Build fails with missing uvm_pkg.sv. Correct: Export UVM_HOME or use vendored UVM under tools/. Why: Compiler cannot find UVM includes. |
| 46 | Practice & assessment | 0:08 | Next section: Practice & assessment. |
| 47 | What you should know | 0:32 | By now you should be able to explain the following. Explain basic testbench (directed tests, pin wiggling) and how it evolves into UVM (transaction, sequence, driver, monitor, scoreboard). Describe the role of transaction, sequence, driver, monitor, scoreboard, agent, env, and test in a UVM testbench. Run the uvm_smoke example (make SIM=verilator TEST=test_uvm_smoke) and interpret UVM output... |
| 48 | Exercises | 0:28 | Exercises. Run uvm_smoke Traceability Change the sequence Optional: Waveforms |
| 49 | Assessment checklist | 0:28 | Assessment checklist. Can explain basic TB vs UVM (transaction, sequence, driver, monitor, scoreboard). Can describe the role of UVM_HOME, Verilator flags, and Make in building/running a UVM test. Can run uvm_smoke and interpret the output. Ready to move to Module 3 (UART protocol + RTL + basic testbench). |
| 50 | Summary & next steps | 0:28 | In summary: Understand basic testbench patterns (directed tests, pin wiggling), the evolution to a UVM+SV testbench (agents, sequences, drivers, monitors, scoreboards), and the toolchain (Verilator, UVM_HOME, Make). Next up: UART. Understand basic testbench patterns (directed tests, pin wiggling), the evolution to a UVM+SV testbench (agents, sequences, drivers... Complete module2/CHECKLIST.md... |

        ## Section narration (edit for TTS)

        - **How to learn:** Complete Module 1 — run `spec_to_rtl` and understand spec → RTL → directed check. Then Read this module’s Design Architecture and Verification sections before `uvm_smoke`. Then Set UVM_HOME (or use vendored UVM under `tools/`) — see Command Reference. Then Run `uvm_smoke` and trace one transaction from sequence → driver → DUT → monitor → scoreboard..
- **Design architecture (DUT and interface, UVM component hierarchy, Build and simulation flow):** Walk through the block diagram, then relate each block to files under module2/examples/.
- **Execution:** Explain make run / UVM make steps, then walk the artifact table and directed-test sequence slide by slide.
- **Verification (Transaction-level verification, Directed regression in uvm_smoke, Skills you reuse on UART/SPI/I²C):** Explain what stimulus is applied, what is checked, and what is intentionally out of scope.
- **Syllabus:** Cover 3 topic section(s) — pause on protocol timing and signals.
- **Before exercises:** Ask learners to recall the learning outcomes slide; they should explain each bullet in their own words.
- **Hands-on:** Run module2/EXAMPLES.md labs; narrate expected PASS lines.

        ## Notes

        - Slides from **Before You Start**, **Design Architecture**, **Verification & Testing Methods**, **Topics Covered**, **EXAMPLES.md**, and **Learning Outcomes**.
        - Full detail: `docs/MODULE2.md` and `module2/EXAMPLES.md`.
        - Regenerate: `regenerate_course_outlines.sh <course_root> --module 2`
