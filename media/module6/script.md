        # Narration script — Module 6: SPI — UVM+SV Verification

        **Target length:** ~15 minutes (43 slides; auto-generated — edit per slide as needed)

        ## Timing table

        | Slide | Section | Duration | Narration |
|-------|---------|----------|-----------|
| 1 | Module 6 | 0:25 | Welcome to module 6, SPI — UVM+SV Verification. In this module you will extend spi verification to uvm+sv — spi agent (transaction, sequence, driver, monitor, scoreboard); run on verilator.. |
| 2 | Learning objectives | 0:24 | Here is what you will learn in this module. SPI UVM agent: Transaction (SpiTransaction), sequence (SpiSequence), driver (SpiDriver), monitor (SpiMonitor), scoreboard (SpiScoreboard). Interface: spi_master_if (clk, rst_n, clk_div_tick, start, data_in, sclk, mosi, cs_n, busy, done) connects UVM to DUT. Mode 0 monitoring: SCLK idle low; capture on rising edge; monitor samples MOSI on each rising... |
| 3 | Prerequisites | 0:20 | Before you start, make sure you have these prerequisites. Module 1 (spec → RTL), Module 2 (UVM+SV, uvm_smoke), Module 5 (SPI protocol + RTL + basic TB). Verilator, Make, C++ compiler, UVM (UVM_HOME or vendored UVM). |
| 4 | Learning path | 0:22 | Learning path. Extend SPI verification to UVM+SV — SPI agent (transaction, sequence, driver, monitor, scoreboard); run on Verilator. |
| 5 | Overview | 0:16 | Overview. Module 6 builds on Module 5 (SPI protocol + RTL + basic testbench): |
| 6 | How to learn this module | 0:08 | Next section: How to learn this module. |
| 7 | Suggested learning path | 0:20 | Follow this learning path. Read the guides before running the labs. Read the detailed SPI learning guide: SPI_LEARNING_GUIDE.md — what SPI is, how it works (signals, Mode 0, timing), and how it maps to... Read the protocols + UVM overview: LEARNING_GUIDE_PROTOCOLS_AND_UVM.md — Part B § 5. How UVM Maps to a Protocol and § 7. SPI UVM Mapping... From docs/MODULE6.md — read guides before running... |
| 8 | Design architecture | 0:08 | Next section: Design architecture. |
| 9 | 1. SPI DUT (reused from Module 5) | 0:30 | 1. SPI DUT (reused from Module 5). spi_master + clk_div in module6/examples/spi_uvm/dut/. spi_master_if connects UVM to DUT pins. Refer to the diagram on the right. |
| 10 | 2. UVM agent structure | 0:34 | 2. UVM agent structure. SpiTransaction = one byte; SpiSequence = directed list; SpiDriver waits on done. SpiMonitor samples MOSI on rising SCLK while cs_n is low (Mode 0, MSB first). SpiScoreboard compares expected vs observed_mosi. Refer to the diagram on the right. |
| 11 | 3. Bus vs DUT checking | 0:26 | 3. Bus vs DUT checking. Monitor validates wire behavior; done alone is not sufficient for sign-off. Refer to the diagram on the right. |
| 12 | RTL block diagram (reference) | 0:22 | RTL block diagram (reference). Module 6: DUT hierarchy and signal flow. |
| 13 | Verification / testbench diagram (reference) | 0:22 | Verification / testbench diagram (reference). Module 6: stimulus, observation, and checking. |
| 14 | SpiTransaction & agent | 0:28 | SpiTransaction & agent. Review the code on screen and match it to files in the repository. |
| 15 | Execution & simulation flow | 0:08 | Next section: Execution & simulation flow. |
| 16 | How the example runs (toolchain) | 0:32 | How the example runs (toolchain). Match each bullet to files in the repository. Makefile: Verilator + UVM_HOME compile RTL, interface, and test_*.sv UVM phases: build → connect → run_test → report (same pattern as Module 2) Sequence → driver → DUT → monitor → scoreboard (read SCOREBOARD at end) Typical command: make SIM=verilator TEST=test_* (see module6 demo slide) Loopback / hooks connect... |
| 17 | Example directory layout | 0:20 | Example directory layout. Match each bullet to files in the repository. dut/: spi_master.v, clk_div.v (same as Module 5) test_spi_uvm.sv: Interface, SpiTransaction, SpiSequence, SpiDriver, SpiMonitor, SpiScoreboard, SpiAgent, SpiEnv, SpiTest; top... Match each path to files under module/examples/. |
| 18 | Makefile — UVM SPI sim | 0:28 | Makefile — UVM SPI sim. Review the code on screen and match it to files in the repository. |
| 19 | Key files to study | 0:08 | Next section: Key files to study. |
| 20 | Open these in the repo | 0:24 | Open these in the repo. module6/examples/spi_uvm/dut/spi_master.v — reused from Module 5 module6/examples/spi_uvm/test_spi_uvm.sv — SpiMonitor samples MOSI on SCLK docs/LEARNING_GUIDE_PROTOCOLS_AND_UVM.md — § 7 SPI UVM mapping Trace while running module6/EXAMPLES.md labs. |
| 21 | Verification & testing methods | 0:08 | Next section: Verification & testing methods. |
| 22 | 1. Mode 0 in the testbench | 0:26 | 1. Mode 0 in the testbench. Monitor must use rising-edge capture and falling-edge change — matches CPOL/CPHA=0. Refer to the diagram on the right. |
| 23 | 2. Directed regression | 0:26 | 2. Directed regression. Same byte pattern as UART UVM (0x00 … 0xFF) for apples-to-apples learning. Refer to the diagram on the right. |
| 24 | 3. Extensions | 0:26 | 3. Extensions. MISO reads, random data, mode parameters — see LEARNING_GUIDE § 7. Refer to the diagram on the right. |
| 25 | Syllabus topics | 0:08 | Next section: Syllabus topics. |
| 26 | 1. SPI protocol recap (Mode 0) | 0:16 | 1. SPI protocol recap (Mode 0). cs_n frames; 8 SCLK cycles per byte; MSB first on MOSI. |
| 27 | 2. Toolchain | 0:16 | 2. Toolchain. Match each bullet to files in the repository. make SIM=verilator TEST=test_spi_uvm; +UVM_TESTNAME=SpiTest. |
| 28 | Hands-on examples | 0:08 | Next section: Hands-on examples. |
| 29 | Module 6 self-check | 0:45 | Module 6 self-check. Watch the terminal output and confirm you see the expected pass message. |
| 30 | Exercise scaffold | 0:28 | Exercise scaffold. Review the code on screen and match it to files in the repository. |
| 31 | Example 1: SPI UVM agent | 0:24 | Example 1: SPI UVM agent. SPI DUT from Module 5 with UVM driver, monitor, and scoreboard Monitor samples MOSI on rising SCLK (Mode 0, MSB first) Bus-centric checking vs relying only on the DUT done flag module6/examples/spi_uvm/README.md |
| 32 | Demo: SPI UVM agent | 0:45 | Demo: SPI UVM agent. Watch the terminal output and confirm you see the expected pass message. |
| 33 | Key concepts | 0:08 | Next section: Key concepts. |
| 34 | 1. Bus-centric verification | 0:16 | 1. Bus-centric verification. Monitor rebuilds the byte from SCLK/MOSI/CS_N, not only the DUT status flag. |
| 35 | 2. Mode 0 in the monitor | 0:16 | 2. Mode 0 in the monitor. Wait for cs_n low, then 8 rising edges, MSB first into observed_mosi. |
| 36 | Common pitfalls | 0:08 | Next section: Common pitfalls. |
| 37 | Sampling MOSI on wrong edge | 0:24 | Sampling MOSI on wrong edge. Mistake: Using falling SCLK for Mode 0 capture. Correct: Rising-edge samples in SpiMonitor. Why: Scoreboard mismatches even when done pulses. |
| 38 | Ignoring CS framing | 0:24 | Ignoring CS framing. Mistake: Counting SCLK edges across multiple frames. Correct: Reset bit index when cs_n deasserts and a new frame starts. Why: Bytes merge or split incorrectly. |
| 39 | Practice & assessment | 0:08 | Next section: Practice & assessment. |
| 40 | What you should know | 0:24 | By now you should be able to explain the following. Describe the SPI UVM agent (transaction, sequence, driver, monitor, scoreboard) and mode 0 monitoring. Run spi_uvm and interpret UVM output. Ready for Module 7: I²C protocol + RTL + basic testbench. From MODULE6 Learning Outcomes. |
| 41 | Exercises | 0:28 | Exercises. Run spi_uvm Trace one transaction Change the sequence Optional: Compare to UART UVM |
| 42 | Assessment checklist | 0:24 | Assessment checklist. Can describe the SPI UVM agent and how it maps to SPI (one byte, mode 0 monitoring). Can run spi_uvm and interpret UVM output. Ready for Module 7: I²C protocol + RTL + basic testbench. |
| 43 | Summary & next steps | 0:28 | In summary: Extend SPI verification to UVM+SV — SPI agent (transaction, sequence, driver, monitor, scoreboard); run on Verilator. Next up: I²C. Extend SPI verification to UVM+SV — SPI agent (transaction, sequence, driver, monitor, scoreboard); run on Verilator. Complete module6/CHECKLIST.md Review module6/EXAMPLES.md and run each lab Next: I²C |

        ## Section narration (edit for TTS)

        - **How to learn:** Read the detailed SPI learning guide: SPI_LEARNING_GUIDE.md — what SPI is, how it works (signals, Mode 0, timing), and how it maps to our RTL. Then Read the protocols + UVM overview: LEARNING_GUIDE_PROTOCOLS_AND_UVM.md — Part B § 5. How UVM Maps to a Protocol and § 7. SPI UVM Mapping (where UVM sits, how transaction/driver/monitor/scoreboard map to SPI)..
- **Design architecture (SPI DUT (reused from Module 5), UVM agent structure, Bus vs DUT checking):** Walk through the block diagram, then relate each block to files under module6/examples/.
- **Execution:** Explain make run / UVM make steps, then walk the artifact table and directed-test sequence slide by slide.
- **Verification (Mode 0 in the testbench, Directed regression, Extensions):** Explain what stimulus is applied, what is checked, and what is intentionally out of scope.
- **Syllabus:** Cover 2 topic section(s) — pause on protocol timing and signals.
- **Before exercises:** Ask learners to recall the learning outcomes slide; they should explain each bullet in their own words.
- **Hands-on:** Run module6/EXAMPLES.md labs; narrate expected PASS lines.

        ## Notes

        - Slides from **Before You Start**, **Design Architecture**, **Verification & Testing Methods**, **Topics Covered**, **EXAMPLES.md**, and **Learning Outcomes**.
        - Full detail: `docs/MODULE6.md` and `module6/EXAMPLES.md`.
        - Regenerate: `regenerate_course_outlines.sh <course_root> --module 6`
