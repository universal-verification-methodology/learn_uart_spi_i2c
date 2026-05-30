        # Narration script — Module 8: I²C — UVM+SV Verification

        **Target length:** ~15 minutes (42 slides; auto-generated — edit per slide as needed)

        ## Timing table

        | Slide | Section | Duration | Narration |
|-------|---------|----------|-----------|
| 1 | Module 8 | 0:25 | Welcome to module 8, I²C — UVM+SV Verification. In this module you will extend i²c verification to uvm+sv — i²c agent (transaction, sequence, driver, monitor, scoreboard); run on verilator.. |
| 2 | Learning objectives | 0:24 | Here is what you will learn in this module. I²C UVM agent: I2cTransaction, I2cSequence, I2cDriver, I2cMonitor, I2cScoreboard. Interface: i2c_if (clk, rst_n, start, addr, data_in, scl, sda, clk_div_tick, busy, done) connects UVM to DUT. How to hook up a UVM monitor and scoreboard to a bus-oriented DUT. |
| 3 | Prerequisites | 0:20 | Before you start, make sure you have these prerequisites. Module 7 (I²C protocol + RTL + basic TB). Verilator, Make, C++ compiler, UVM (UVM_HOME or vendored UVM). |
| 4 | Learning path | 0:22 | Learning path. Extend I²C verification to UVM+SV — I²C agent (transaction, sequence, driver, monitor, scoreboard); run on Verilator. |
| 5 | Overview | 0:16 | Overview. Module 8 builds on Module 7 (I²C protocol + RTL + basic testbench): |
| 6 | How to learn this module | 0:08 | Next section: How to learn this module. |
| 7 | Suggested learning path | 0:20 | Follow this learning path. Read the guides before running the labs. Read the detailed I²C learning guide: I2C_LEARNING_GUIDE.md — what I²C is, how it works (START/STOP, address+R/W, data, timing), and how... Read the protocols + UVM overview: LEARNING_GUIDE_PROTOCOLS_AND_UVM.md — Part B § 5. How UVM Maps to a Protocol and § 8. I²C UVM Mapping... From docs/MODULE8.md — read guides before... |
| 8 | Design architecture | 0:08 | Next section: Design architecture. |
| 9 | 1. I²C DUT (reused from Module 7) | 0:30 | 1. I²C DUT (reused from Module 7). i2c_master + clk_div; i2c_if for UVM connection. Wire sequence: START → address+W → data → STOP. Refer to the diagram on the right. |
| 10 | 2. UVM agent | 0:34 | 2. UVM agent. I2cTransaction holds addr + data; monitor fills observed_*. I2cMonitor reimplements baseline bus sampling inside UVM. I2cScoreboard checks address and data phases independently. Refer to the diagram on the right. |
| 11 | 3. Course capstone | 0:26 | 3. Course capstone. Compare UART (async), SPI (SCLK+CS), I²C (shared bus) — same UVM skeleton, different monitors. Refer to the diagram on the right. |
| 12 | RTL block diagram (reference) | 0:22 | RTL block diagram (reference). Module 8: DUT hierarchy and signal flow. |
| 13 | Verification / testbench diagram (reference) | 0:22 | Verification / testbench diagram (reference). Module 8: stimulus, observation, and checking. |
| 14 | I2cTransaction & agent | 0:28 | I2cTransaction & agent. Review the code on screen and match it to files in the repository. |
| 15 | Execution & simulation flow | 0:08 | Next section: Execution & simulation flow. |
| 16 | How the example runs (toolchain) | 0:32 | How the example runs (toolchain). Match each bullet to files in the repository. Makefile: Verilator + UVM_HOME compile RTL, interface, and test_*.sv UVM phases: build → connect → run_test → report (same pattern as Module 2) Sequence → driver → DUT → monitor → scoreboard (read SCOREBOARD at end) Typical command: make SIM=verilator TEST=test_* (see module8 demo slide) Loopback / hooks connect... |
| 17 | Example directory layout | 0:20 | Example directory layout. Match each bullet to files in the repository. dut/: i2c_master.v, clk_div.v (same as Module 7) test_i2c_uvm.sv: Interface, I2cTransaction, I2cSequence, I2cDriver, I2cMonitor, I2cScoreboard, I2cAgent, I2cEnv, test_i2c_uvm... Match each path to files under module/examples/. |
| 18 | Makefile — UVM I2C sim | 0:28 | Makefile — UVM I2C sim. Review the code on screen and match it to files in the repository. |
| 19 | Key files to study | 0:08 | Next section: Key files to study. |
| 20 | Open these in the repo | 0:24 | Open these in the repo. module8/examples/i2c_uvm/dut/i2c_master.v — reused from Module 7 module8/examples/i2c_uvm/test_i2c_uvm.sv — I2cMonitor + two-field scoreboard docs/LEARNING_GUIDE_PROTOCOLS_AND_UVM.md — § 8 I²C UVM mapping Trace while running module8/EXAMPLES.md labs. |
| 21 | Verification & testing methods | 0:08 | Next section: Verification & testing methods. |
| 22 | 1. Two-phase scoreboard | 0:26 | 1. Two-phase scoreboard. Separate checks for address+W byte and data byte — catches shifted or merged fields. Refer to the diagram on the right. |
| 23 | 2. Reuse baseline monitor logic | 0:26 | 2. Reuse baseline monitor logic. Module 7 inline monitor → Module 8 I2cMonitor for scalable tests. Refer to the diagram on the right. |
| 24 | 3. Extensions | 0:26 | 3. Extensions. ACK/NACK, reads, multi-master — LEARNING_GUIDE § 8. Refer to the diagram on the right. |
| 25 | Syllabus topics | 0:08 | Next section: Syllabus topics. |
| 26 | 1. I²C protocol recap | 0:16 | 1. I²C protocol recap. START/STOP on SCL high; MSB-first address and data on SDA. |
| 27 | 2. Toolchain | 0:16 | 2. Toolchain. Match each bullet to files in the repository. make SIM=verilator TEST=test_i2c_uvm; +UVM_TESTNAME=test_i2c_uvm. |
| 28 | Hands-on examples | 0:08 | Next section: Hands-on examples. |
| 29 | Module 8 self-check | 0:45 | Module 8 self-check. Watch the terminal output and confirm you see the expected pass message. |
| 30 | Example 1: I²C UVM agent | 0:24 | Example 1: I²C UVM agent. I²C DUT from Module 7 with UVM agent and two-phase scoreboard (addr + data) I2cMonitor reuses baseline bus-sampling ideas in reusable form Course capstone: compare UART, SPI, and I²C verification patterns module8/examples/i2c_uvm/README.md |
| 31 | Demo: I²C UVM agent | 0:45 | Demo: I²C UVM agent. Watch the terminal output and confirm you see the expected pass message. |
| 32 | Key concepts | 0:08 | Next section: Key concepts. |
| 33 | 1. Two-phase scoreboard | 0:16 | 1. Two-phase scoreboard. Compare observed_addr and observed_data separately from one transaction. |
| 34 | 2. Course capstone | 0:16 | 2. Course capstone. Same UVM skeleton as UART/SPI; only monitor protocol rules differ. |
| 35 | Common pitfalls | 0:08 | Next section: Common pitfalls. |
| 36 | Merging address and data checks | 0:24 | Merging address and data checks. Mistake: One expected byte for the whole transaction. Correct: Separate expected/observed for address+W and data phases. Why: Off-by-one bit in address can hide behind a correct data byte. |
| 37 | Skipping baseline Module 7 | 0:24 | Skipping baseline Module 7. Mistake: Jumping to UVM without understanding inline bus monitor logic. Correct: Run i2c_baseline first; then map monitor to I2cMonitor. Why: UVM monitor is the same idea in a reusable component. |
| 38 | Practice & assessment | 0:08 | Next section: Practice & assessment. |
| 39 | What you should know | 0:28 | By now you should be able to explain the following. Describe the I²C UVM agent and how I2cMonitor maps to SCL/SDA behavior. Explain two-phase scoreboard checking (address vs data). Run i2c_uvm and interpret UVM / scoreboard output. Compare verification architecture across UART, SPI, and I²C modules in this course. From MODULE8 Learning Outcomes. |
| 40 | Exercises | 0:28 | Exercises. Run i2c_uvm Trace one transaction Change the sequence Compare across protocols |
| 41 | Assessment checklist | 0:24 | Assessment checklist. Can describe the I²C UVM agent and how it maps to I²C (addr+data, monitor on SCL/SDA). Can run i2c_uvm and interpret UVM output. Can compare UVM structure across UART, SPI, and I²C. |
| 42 | Summary & next steps | 0:28 | In summary: Extend I²C verification to UVM+SV — I²C agent (transaction, sequence, driver, monitor, scoreboard); run on Verilator. Next up: Next module in course. Extend I²C verification to UVM+SV — I²C agent (transaction, sequence, driver, monitor, scoreboard); run on Verilator. Complete module8/CHECKLIST.md Review module8/EXAMPLES.md and run each lab Next: Next module in course |

        ## Section narration (edit for TTS)

        - **How to learn:** Read the detailed I²C learning guide: I2C_LEARNING_GUIDE.md — what I²C is, how it works (START/STOP, address+R/W, data, timing), and how it maps to our RTL. Then Read the protocols + UVM overview: LEARNING_GUIDE_PROTOCOLS_AND_UVM.md — Part B § 5. How UVM Maps to a Protocol and § 8. I²C UVM Mapping (where UVM sits, how transaction/driver/monitor/scoreboard map to I²C)..
- **Design architecture (I²C DUT (reused from Module 7), UVM agent, Course capstone):** Walk through the block diagram, then relate each block to files under module8/examples/.
- **Execution:** Explain make run / UVM make steps, then walk the artifact table and directed-test sequence slide by slide.
- **Verification (Two-phase scoreboard, Reuse baseline monitor logic, Extensions):** Explain what stimulus is applied, what is checked, and what is intentionally out of scope.
- **Syllabus:** Cover 2 topic section(s) — pause on protocol timing and signals.
- **Before exercises:** Ask learners to recall the learning outcomes slide; they should explain each bullet in their own words.
- **Hands-on:** Run module8/EXAMPLES.md labs; narrate expected PASS lines.

        ## Notes

        - Slides from **Before You Start**, **Design Architecture**, **Verification & Testing Methods**, **Topics Covered**, **EXAMPLES.md**, and **Learning Outcomes**.
        - Full detail: `docs/MODULE8.md` and `module8/EXAMPLES.md`.
        - Regenerate: `regenerate_course_outlines.sh <course_root> --module 8`
