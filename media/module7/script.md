        # Narration script — Module 7: I²C — Protocol + RTL + Basic Testbench

        **Target length:** ~16 minutes (43 slides; auto-generated — edit per slide as needed)

        ## Timing table

        | Slide | Section | Duration | Narration |
|-------|---------|----------|-----------|
| 1 | Module 7 | 0:25 | Welcome to module 7, I²C — Protocol + RTL + Basic Testbench. In this module you will understand the i²c protocol (start/stop, addressing, ack/nack), translate it to rtl (simple master + timing), and verify with a basic (non-uvm) directed testbench.. |
| 2 | Learning objectives | 0:28 | Here is what you will learn in this module. RTL block architecture: clk_div + i2c_master FSM (START → addr → data → STOP). Baseline verification: Directed writes plus inline bus monitor (sample SDA on rising SCL). Protocol vs simplification: Real open-drain/ACK vs this repo’s push-pull teaching model. Path to Module 8: Same DUT with UVM monitor/scoreboard on address and data phases. |
| 3 | Prerequisites | 0:20 | Before you start, make sure you have these prerequisites. Modules 1–6. Verilator, Make, C++ compiler. No UVM required for this baseline. |
| 4 | Learning path | 0:22 | Learning path. Understand the I²C protocol (start/stop, addressing, ACK/NACK), translate it to RTL (simple master + timing), and verify with a basic (non-UVM) directed testbench. |
| 5 | Overview | 0:16 | Overview. Module 7 is the I²C protocol + RTL + basic testbench module (UVM comes in Module 8). |
| 6 | How to learn this module | 0:08 | Next section: How to learn this module. |
| 7 | Suggested learning path | 0:20 | Follow this learning path. Read the guides before running the labs. Read the detailed I²C learning guide: I2C_LEARNING_GUIDE.md — what I²C is, what kind of protocol (serial, synchronous, two-wire bus)... Read the protocols + UVM overview: LEARNING_GUIDE_PROTOCOLS_AND_UVM.md — Part B § 4. When to Use Baseline vs UVM (why we start with a... From docs/MODULE7.md — read guides before running demos. |
| 8 | Design architecture | 0:08 | Next section: Design architecture. |
| 9 | 1. Block hierarchy | 0:26 | 1. Block hierarchy. top_i2c_baseline → clk_div + i2c_master; C++ drives clk/rst_n. Refer to the diagram on the right. |
| 10 | 2. I²C master FSM | 0:30 | 2. I²C master FSM. States: IDLE → START → ADDR_BITS → DATA_BITS → STOP. One teaching write: 7-bit addr + data byte on scl/sda (push-pull model). Refer to the diagram on the right. |
| 11 | 3. Teaching vs real I²C | 0:26 | 3. Teaching vs real I²C. No open-drain, ACK/NACK, or arbitration in baseline — learn sequencing first. Refer to the diagram on the right. |
| 12 | RTL block diagram (reference) | 0:22 | RTL block diagram (reference). Module 7: DUT hierarchy and signal flow. |
| 13 | Verification / testbench diagram (reference) | 0:22 | Verification / testbench diagram (reference). Module 7: stimulus, observation, and checking. |
| 14 | i2c_master FSM | 0:28 | i2c_master FSM. Review the code on screen and match it to files in the repository. |
| 15 | clk_div — SCL timing | 0:28 | clk_div — SCL timing. Review the code on screen and match it to files in the repository. |
| 16 | Execution & simulation flow | 0:08 | Next section: Execution & simulation flow. |
| 17 | How the example runs (toolchain) | 0:32 | How the example runs (toolchain). Match each bullet to files in the repository. Makefile: Verilator compiles RTL + SystemVerilog testbench into a C++ model sim_main.cpp: generates clk/rst_n, calls eval() until $finish Directed test (initial block or C++): drive stimulus, wait for DUT flags Self-check: compare outputs; print PASS/FAIL (see terminal demo slide) Repo path... |
| 18 | Example directory layout | 0:24 | Example directory layout. Match each bullet to files in the repository. dut/: i2c_master.v, clk_div.v top_i2c_baseline.sv: Instantiates DUT + directed test + monitor/self-check sim_main.cpp: Clock/reset harness; simulation runs until $finish Match each path to files under module/examples/. |
| 19 | Makefile — i2c_baseline run | 0:28 | Makefile — i2c_baseline run. Review the code on screen and match it to files in the repository. |
| 20 | Key files to study | 0:08 | Next section: Key files to study. |
| 21 | Open these in the repo | 0:24 | Open these in the repo. module7/examples/i2c_baseline/dut/i2c_master.v — START/addr/data/STOP FSM module7/examples/i2c_baseline/top_i2c_baseline.sv — stimulus + inline bus monitor docs/I2C_LEARNING_GUIDE.md — protocol reference Trace while running module7/EXAMPLES.md labs. |
| 22 | Verification & testing methods | 0:08 | Next section: Verification & testing methods. |
| 23 | 1. Inline bus monitor | 0:26 | 1. Inline bus monitor. Top module detects START; samples SDA on rising SCL; rebuilds addr+W and data. Refer to the diagram on the right. |
| 24 | 2. Self-check flow | 0:26 | 2. Self-check flow. Compare captured bytes to driven addr/data_in; print I2C baseline test PASS. Refer to the diagram on the right. |
| 25 | 3. Path to Module 8 | 0:26 | 3. Path to Module 8. Move monitor into I2cMonitor; scoreboard splits address and data phases. Refer to the diagram on the right. |
| 26 | Directed I2C test | 0:28 | Directed I2C test. Review the code on screen and match it to files in the repository. |
| 27 | Syllabus topics | 0:08 | Next section: Syllabus topics. |
| 28 | 1. I²C Protocol Essentials | 0:36 | 1. I²C Protocol Essentials. Bus idle: SCL=1, SDA=1. START: SDA goes 1→0 while SCL is 1. STOP: SDA goes 0→1 while SCL is 1. Address phase: 7-bit address + R/W bit (0=write, 1=read) sent MSB first. Data phase: 8-bit data bytes sent MSB first. |
| 29 | 2. Hands-on testbench (i2c_baseline) | 0:20 | 2. Hands-on testbench (i2c_baseline). Stimulus: start, addr, data_in, wait(done). Monitor/self-check: reconstruct address+W and data from SCL/SDA; compare to expected. |
| 30 | Hands-on examples | 0:08 | Next section: Hands-on examples. |
| 31 | Module 7 self-check | 0:45 | Module 7 self-check. Watch the terminal output and confirm you see the expected pass message. |
| 32 | Example 1: I²C baseline master | 0:24 | Example 1: I²C baseline master. I²C master FSM: START → address+W → data → STOP Inline bus monitor sampling SDA on rising SCL Comparing reconstructed address and data bytes to stimulus module7/examples/i2c_baseline/README.md |
| 33 | Demo: I²C baseline master | 0:45 | Demo: I²C baseline master. Watch the terminal output and confirm you see the expected pass message. |
| 34 | Key concepts | 0:08 | Next section: Key concepts. |
| 35 | 1. Two-wire bus | 0:16 | 1. Two-wire bus. SCL + SDA; START/STOP when SCL is high; data changed when SCL is low (simplified model). |
| 36 | 2. Address + data phases | 0:16 | 2. Address + data phases. 8 bits address+R/W (MSB first), then 8 bits data — monitor both separately. |
| 37 | Common pitfalls | 0:08 | Next section: Common pitfalls. |
| 38 | Ignoring START detection | 0:24 | Ignoring START detection. Mistake: Sampling bits before a valid START condition. Correct: Detect SDA 1→0 while SCL high, then sample on rising SCL. Why: Reconstructed bytes align to wrong frame boundary. |
| 39 | Expecting full-spec ACK | 0:24 | Expecting full-spec ACK. Mistake: Assuming teaching RTL models open-drain ACK/NACK. Correct: Treat baseline as sequencing practice; ACK comes in extensions. Why: Our push-pull teaching DUT simplifies the bus. |
| 40 | Practice & assessment | 0:08 | Next section: Practice & assessment. |
| 41 | Exercises | 0:28 | Exercises. Run i2c_baseline Trace one transfer Bus monitor Optional: Waveforms |
| 42 | Assessment checklist | 0:28 | Assessment checklist. Can describe I²C START, STOP, address+R/W, and data phase (and ACK/NACK concept). Can explain the role of i2c_master and clk_div; know the baseline uses push-pull (simplified). Can run i2c_baseline and interpret the test result. Ready for Module 8: I²C UVM+SV verification. |
| 43 | Summary & next steps | 0:28 | In summary: Understand the I²C protocol (start/stop, addressing, ACK/NACK), translate it to RTL (simple master + timing), and verify with a basic (non-UVM) directed testbench. Next up: I²C UVM+SV. Understand the I²C protocol (start/stop, addressing, ACK/NACK), translate it to RTL (simple master + timing), and verify with a basic... Complete module7/CHECKLIST.md Review module7/EXAMPLES.md and... |

        ## Section narration (edit for TTS)

        - **How to learn:** Read the detailed I²C learning guide: I2C_LEARNING_GUIDE.md — what I²C is, what kind of protocol (serial, synchronous, two-wire bus), how it works (START/STOP, address+R/W, data, ACK/NACK concept), and where it’s used. Then Read the protocols + UVM overview: LEARNING_GUIDE_PROTOCOLS_AND_UVM.md — Part B § 4. When to Use Baseline vs UVM (why we start with a baseline test before I²C UVM in Module 8)..
- **Design architecture (Block hierarchy, I²C master FSM, Teaching vs real I²C):** Walk through the block diagram, then relate each block to files under module7/examples/.
- **Execution:** Explain make run / UVM make steps, then walk the artifact table and directed-test sequence slide by slide.
- **Verification (Inline bus monitor, Self-check flow, Path to Module 8):** Explain what stimulus is applied, what is checked, and what is intentionally out of scope.
- **Syllabus:** Cover 2 topic section(s) — pause on protocol timing and signals.
- **Hands-on:** Run module7/EXAMPLES.md labs; narrate expected PASS lines.

        ## Notes

        - Slides from **Before You Start**, **Design Architecture**, **Verification & Testing Methods**, **Topics Covered**, **EXAMPLES.md**, and **Learning Outcomes**.
        - Full detail: `docs/MODULE7.md` and `module7/EXAMPLES.md`.
        - Regenerate: `regenerate_course_outlines.sh <course_root> --module 7`
