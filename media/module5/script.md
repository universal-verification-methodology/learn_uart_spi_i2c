        # Narration script — Module 5: SPI — Protocol + RTL + Basic Testbench

        **Target length:** ~17 minutes (45 slides; auto-generated — edit per slide as needed)

        ## Timing table

        | Slide | Section | Duration | Narration |
|-------|---------|----------|-----------|
| 1 | Module 5 | 0:25 | Welcome to module 5, SPI — Protocol + RTL + Basic Testbench. In this module you will understand the spi protocol (mode 0, signals), translate it to rtl (spi master, clk_div), and verify with a basic (non-uvm) directed testbench.. |
| 2 | Learning objectives | 0:28 | Here is what you will learn in this module. SPI mode 0: SCLK idle low; capture on rising edge; change on falling edge; CS_N active low for frame. RTL block architecture: clk_div + spi_master hierarchy, FSM, and Mode 0 timing on the wire. Baseline verification: Directed stimulus, done-based checks, and optional waveform review (8 SCLK edges, MSB first). Path to Module 6: Same DUT, UVM agent... |
| 3 | Prerequisites | 0:20 | Before you start, make sure you have these prerequisites. Modules 1–4 (spec→RTL, UVM, UART baseline, UART UVM). Verilator, Make, C++ compiler. No UVM required for spi_baseline. |
| 4 | Learning path | 0:22 | Learning path. Understand the SPI protocol (mode 0, signals), translate it to RTL (SPI master, clk_div), and verify with a basic (non-UVM) directed testbench. |
| 5 | Overview | 0:16 | Overview. Module 5 is the second protocol module (after UART): |
| 6 | How to learn this module | 0:08 | Next section: How to learn this module. |
| 7 | Suggested learning path | 0:20 | Follow this learning path. Read the guides before running the labs. Read the detailed SPI learning guide: SPI_LEARNING_GUIDE.md — what SPI is, what kind of protocol (serial, synchronous, master–slave)... Read the protocols + UVM overview: LEARNING_GUIDE_PROTOCOLS_AND_UVM.md — Part B § 4. When to Use Baseline vs UVM (why we start with a... From docs/MODULE5.md — read guides before running demos. |
| 8 | Design architecture | 0:08 | Next section: Design architecture. |
| 9 | 1. Block hierarchy | 0:26 | 1. Block hierarchy. top_spi_baseline → clk_div + spi_master; C++ supplies clk/rst_n. Refer to the diagram on the right. |
| 10 | 2. SPI master RTL | 0:34 | 2. SPI master RTL. clk_div: clk_div_tick every DIVIDER clocks. spi_master: Mode 0; cs_n frames; MSB-first on mosi; done when complete. Outputs: sclk (idle low), mosi, cs_n — no miso in baseline. Refer to the diagram on the right. |
| 11 | 3. Mode 0 timing on the wire | 0:26 | 3. Mode 0 timing on the wire. Capture on rising SCLK; change MOSI on falling SCLK; 8 edges per byte. Refer to the diagram on the right. |
| 12 | RTL block diagram (reference) | 0:22 | RTL block diagram (reference). Module 5: DUT hierarchy and signal flow. |
| 13 | Verification / testbench diagram (reference) | 0:22 | Verification / testbench diagram (reference). Module 5: stimulus, observation, and checking. |
| 14 | spi_master — Mode 0 shift | 0:28 | spi_master — Mode 0 shift. Review the code on screen and match it to files in the repository. |
| 15 | clk_div — SPI clock | 0:28 | clk_div — SPI clock. Review the code on screen and match it to files in the repository. |
| 16 | Execution & simulation flow | 0:08 | Next section: Execution & simulation flow. |
| 17 | How the example runs (toolchain) | 0:32 | How the example runs (toolchain). Match each bullet to files in the repository. Makefile: Verilator compiles RTL + SystemVerilog testbench into a C++ model sim_main.cpp: generates clk/rst_n, calls eval() until $finish Directed test (initial block or C++): drive stimulus, wait for DUT flags Self-check: compare outputs; print PASS/FAIL (see terminal demo slide) Repo path... |
| 18 | Example directory layout | 0:24 | Example directory layout. Match each bullet to files in the repository. dut/: spi_master.v, clk_div.v top_spi_baseline.sv: clk_div, spi_master; directed test in initial block sim_main.cpp: Clock, reset; run until $finish Match each path to files under module/examples/. |
| 19 | Makefile — spi_baseline run | 0:28 | Makefile — spi_baseline run. Review the code on screen and match it to files in the repository. |
| 20 | Key files to study | 0:08 | Next section: Key files to study. |
| 21 | Open these in the repo | 0:28 | Open these in the repo. module5/examples/spi_baseline/dut/spi_master.v — Mode 0 master module5/examples/spi_baseline/dut/clk_div.v — clk_div_tick module5/examples/spi_baseline/top_spi_baseline.sv — directed test docs/SPI_LEARNING_GUIDE.md — protocol reference Trace while running module5/EXAMPLES.md labs. |
| 22 | Verification & testing methods | 0:08 | Next section: Verification & testing methods. |
| 23 | 1. Baseline goals | 0:26 | 1. Baseline goals. Confirm Mode 0 serialization before SPI UVM (Module 6). Refer to the diagram on the right. |
| 24 | 2. Directed test flow | 0:26 | 2. Directed test flow. Pulse start + data_in (0x55, 0xAA); wait(done); read [PASS] messages. Refer to the diagram on the right. |
| 25 | 3. Waveform learning (optional) | 0:30 | 3. Waveform learning (optional). Count 8 SCLK cycles per frame; verify MSB-first bit order on MOSI. Defer MISO, multi-slave CS, and random data to Module 6. Refer to the diagram on the right. |
| 26 | Directed SPI test | 0:28 | Directed SPI test. Review the code on screen and match it to files in the repository. |
| 27 | Syllabus topics | 0:08 | Next section: Syllabus topics. |
| 28 | 1. SPI Protocol (Mode 0) | 0:24 | 1. SPI Protocol (Mode 0). Signals: sclk (serial clock), mosi (master out, slave in), cs_n (active-low chip select). Optional: miso (not used in this baseline). Mode 0 (CPOL=0, CPHA=0): SCLK idles low; data captured on rising edge; data changed on falling edge. Timing: One bit per clk_div_tick; clk_div_tick derived from system clock via divider (e.g. DIVIDER=8). |
| 29 | 2. Hands-on testbench (spi_baseline) | 0:20 | 2. Hands-on testbench (spi_baseline). Directed test in top_spi_baseline.sv: start, data_in, wait(done). Pass: [PASS] lines and SPI baseline test PASS. |
| 30 | Hands-on examples | 0:08 | Next section: Hands-on examples. |
| 31 | Module 5 self-check | 0:45 | Module 5 self-check. Watch the terminal output and confirm you see the expected pass message. |
| 32 | Exercise scaffold | 0:28 | Exercise scaffold. Review the code on screen and match it to files in the repository. |
| 33 | Example 1: SPI baseline master | 0:24 | Example 1: SPI baseline master. SPI Mode 0 master RTL (spi_master + clk_div) Directed writes 0x55 and 0xAA with start / wait(done) Observing SCLK, MOSI, and CS_N timing in simulation (optional VCD) module5/examples/spi_baseline/README.md |
| 34 | Demo: SPI baseline master | 0:45 | Demo: SPI baseline master. Watch the terminal output and confirm you see the expected pass message. |
| 35 | Key concepts | 0:08 | Next section: Key concepts. |
| 36 | 1. Synchronous serial (SPI) | 0:20 | 1. Synchronous serial (SPI). sclk defines bit times; unlike UART there is an explicit clock line. Mode 0: idle low, sample MOSI on rising edge, change on falling edge. |
| 37 | 2. Chip select frames | 0:16 | 2. Chip select frames. cs_n low defines one transfer; typically 8 SCLK cycles per byte. |
| 38 | Common pitfalls | 0:08 | Next section: Common pitfalls. |
| 39 | Wrong SPI mode in head | 0:24 | Wrong SPI mode in head. Mistake: Sampling on falling edge when using Mode 0. Correct: Rising edge capture, falling edge change for CPOL=0, CPHA=0. Why: Bits will be shifted and MSB/LSB order will look wrong. |
| 40 | Trusting done only | 0:24 | Trusting done only. Mistake: No waveform or bus check on MOSI/SCLK. Correct: Optional VCD review or Module 6 monitor-based check. Why: done only means the FSM finished, not that bits were correct. |
| 41 | Practice & assessment | 0:08 | Next section: Practice & assessment. |
| 42 | What you should know | 0:28 | By now you should be able to explain the following. Describe SPI mode 0 and the role of sclk, mosi, cs_n, clk_div_tick. Explain the role of spi_master and clk_div. Run the spi_baseline example and interpret the directed test. Ready for Module 6: SPI UVM+SV verification. From MODULE5 Learning Outcomes. |
| 43 | Exercises | 0:28 | Exercises. Run spi_baseline Trace one transfer Mode 0 timing Optional: Waveforms |
| 44 | Assessment checklist | 0:28 | Assessment checklist. Can describe SPI mode 0 (idle low, capture on rising, change on falling) and signals sclk, mosi, cs_n. Can explain the role of spi_master and clk_div in the RTL. Can run spi_baseline and interpret the directed test result. Ready for Module 6: SPI UVM+SV verification. |
| 45 | Summary & next steps | 0:28 | In summary: Understand the SPI protocol (mode 0, signals), translate it to RTL (SPI master, clk_div), and verify with a basic (non-UVM) directed testbench. Next up: SPI UVM+SV. Understand the SPI protocol (mode 0, signals), translate it to RTL (SPI master, clk_div), and verify with a basic (non-UVM) directed... Complete module5/CHECKLIST.md Review module5/EXAMPLES.md and run each lab Next: SPI... |

        ## Section narration (edit for TTS)

        - **How to learn:** Read the detailed SPI learning guide: SPI_LEARNING_GUIDE.md — what SPI is, what kind of protocol (serial, synchronous, master–slave), how it works (signals, modes CPOL/CPHA, Mode 0, timing), and where it’s used. Then Read the protocols + UVM overview: LEARNING_GUIDE_PROTOCOLS_AND_UVM.md — Part B § 4. When to Use Baseline vs UVM (why we start with a baseline test before SPI UVM in Module 6)..
- **Design architecture (Block hierarchy, SPI master RTL, Mode 0 timing on the wire):** Walk through the block diagram, then relate each block to files under module5/examples/.
- **Execution:** Explain make run / UVM make steps, then walk the artifact table and directed-test sequence slide by slide.
- **Verification (Baseline goals, Directed test flow, Waveform learning (optional)):** Explain what stimulus is applied, what is checked, and what is intentionally out of scope.
- **Syllabus:** Cover 2 topic section(s) — pause on protocol timing and signals.
- **Before exercises:** Ask learners to recall the learning outcomes slide; they should explain each bullet in their own words.
- **Hands-on:** Run module5/EXAMPLES.md labs; narrate expected PASS lines.

        ## Notes

        - Slides from **Before You Start**, **Design Architecture**, **Verification & Testing Methods**, **Topics Covered**, **EXAMPLES.md**, and **Learning Outcomes**.
        - Full detail: `docs/MODULE5.md` and `module5/EXAMPLES.md`.
        - Regenerate: `regenerate_course_outlines.sh <course_root> --module 5`
