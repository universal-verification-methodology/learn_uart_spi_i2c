        # Narration script — Module 4: UART — UVM+SV Verification

        **Target length:** ~17 minutes (45 slides; auto-generated — edit per slide as needed)

        ## Timing table

        | Slide | Section | Duration | Narration |
|-------|---------|----------|-----------|
| 1 | Module 4 | 0:25 | Welcome to module 4, UART — UVM+SV Verification. In this module you will extend uart verification to uvm+sv — uart agent (transaction, sequence, driver, monitor, scoreboard); run on verilator.. |
| 2 | Learning objectives | 0:24 | Here is what you will learn in this module. UART UVM agent: Transaction (UartTxTransaction), sequence (UartTxSequence), driver (UartTxDriver), monitor (UartTxMonitor), scoreboard... Interface: uart_tx_if (clk, rst_n, start, data, tx, baud_tick) connects UVM to DUT. Loopback check: TX path (driver → DUT → monitor → scoreboard) and RX path (DUT rx_valid/rx_data → scoreboard.check_rx_byte). |
| 3 | Prerequisites | 0:20 | Before you start, make sure you have these prerequisites. Module 1 (spec → RTL), Module 2 (UVM+SV, uvm_smoke), Module 3 (UART protocol + RTL + basic TB). Verilator, Make, C++ compiler, UVM (UVM_HOME or vendored UVM). |
| 4 | Learning path | 0:22 | Learning path. Extend UART verification to UVM+SV — UART agent (transaction, sequence, driver, monitor, scoreboard); run on Verilator. |
| 5 | Overview | 0:16 | Overview. Module 4 builds on Module 3 (UART protocol + RTL + basic testbench): |
| 6 | How to learn this module | 0:08 | Next section: How to learn this module. |
| 7 | Suggested learning path | 0:20 | Follow this learning path. Read the guides before running the labs. Read the detailed UART learning guide: UART_LEARNING_GUIDE.md — what UART is, how it works (frame, baud, TX/RX), and how it maps to our RTL. Read the protocols + UVM overview: LEARNING_GUIDE_PROTOCOLS_AND_UVM.md — Part B § 5. How UVM Maps to a Protocol and § 6. UART UVM... From docs/MODULE4.md — read guides before running demos. |
| 8 | Design architecture | 0:08 | Next section: Design architecture. |
| 9 | 1. UART DUT (reused from Module 3) | 0:34 | 1. UART DUT (reused from Module 3). dut/: uart_tx, uart_rx, baud_gen — identical RTL to uart_baseline. Loopback in top: rx = tx for closed-loop checking. Why reuse: Upgrade verification (UVM) without touching proven RTL. Refer to the diagram on the right. |
| 10 | 2. UVM testbench hierarchy | 0:34 | 2. UVM testbench hierarchy. uart_tx_if: virtual interface for driver/monitor. UartTxTransaction / Sequence / Driver / Monitor / Scoreboard / Agent / Env / Test — same pattern as uvm_smoke. Monitor reconstructs bytes from the serial tx line using UART 8N1 rules. Refer to the diagram on the right. |
| 11 | 3. Dual check paths | 0:30 | 3. Dual check paths. TX path: sequence → driver → DUT → monitor → scoreboard (observed_tx). RX path: loopback into uart_rx; check_rx_byte() when data_valid asserts. Refer to the diagram on the right. |
| 12 | RTL block diagram (reference) | 0:22 | RTL block diagram (reference). Module 4: DUT hierarchy and signal flow. |
| 13 | Verification / testbench diagram (reference) | 0:22 | Verification / testbench diagram (reference). Module 4: stimulus, observation, and checking. |
| 14 | UartTxDriver — bit timing | 0:28 | UartTxDriver — bit timing. Review the code on screen and match it to files in the repository. |
| 15 | UartTxTransaction & agent | 0:28 | UartTxTransaction & agent. Review the code on screen and match it to files in the repository. |
| 16 | Execution & simulation flow | 0:08 | Next section: Execution & simulation flow. |
| 17 | How the example runs (toolchain) | 0:32 | How the example runs (toolchain). Match each bullet to files in the repository. Makefile: Verilator + UVM_HOME compile RTL, interface, and test_*.sv UVM phases: build → connect → run_test → report (same pattern as Module 2) Sequence → driver → DUT → monitor → scoreboard (read SCOREBOARD at end) Typical command: make SIM=verilator TEST=test_* (see module4 demo slide) Loopback / hooks connect... |
| 18 | Example directory layout | 0:20 | Example directory layout. Match each bullet to files in the repository. dut/: uart_tx.v, uart_rx.v, baud_gen.v (same as Module 3) test_uart_uvm.sv: Interface, UartTxTransaction, UartTxSequence, UartTxDriver, UartTxMonitor, UartTxScoreboard, UartTxAgent... Match each path to files under module/examples/. |
| 19 | Makefile — UVM UART sim | 0:28 | Makefile — UVM UART sim. Review the code on screen and match it to files in the repository. |
| 20 | Key files to study | 0:08 | Next section: Key files to study. |
| 21 | Open these in the repo | 0:24 | Open these in the repo. module4/examples/uart_uvm/dut/ — same UART RTL as Module 3 module4/examples/uart_uvm/test_uart_uvm.sv — agent, env, loopback hooks docs/LEARNING_GUIDE_PROTOCOLS_AND_UVM.md — § 6 UART UVM mapping Trace while running module4/EXAMPLES.md labs. |
| 22 | Verification & testing methods | 0:08 | Next section: Verification & testing methods. |
| 23 | 1. Directed UART regression | 0:26 | 1. Directed UART regression. Sequence sends 0x00, 0x01, 0x55, 0xAA, 0xFF — repeatable regression before randomization. Refer to the diagram on the right. |
| 24 | 2. Scoreboard strategy | 0:30 | 2. Scoreboard strategy. Expected queue loaded in test; compare to monitor-reconstructed TX and to RX hook data. Fail fast on mismatch; read UVM SCOREBOARD summary at end of run. Refer to the diagram on the right. |
| 25 | 3. What to add next | 0:30 | 3. What to add next. Random baud, framing-error injection, coverage on busy / data_valid. See LEARNING_GUIDE_PROTOCOLS_AND_UVM.md § 6. Refer to the diagram on the right. |
| 26 | Scoreboard — TX/RX check | 0:28 | Scoreboard — TX/RX check. Review the code on screen and match it to files in the repository. |
| 27 | Syllabus topics | 0:08 | Next section: Syllabus topics. |
| 28 | 1. UART protocol recap (8N1) | 0:20 | 1. UART protocol recap (8N1). One byte = start (0) + 8 data (LSB first) + stop (1); baud_tick times each bit. Driver/monitor must follow the same rules as the RTL. |
| 29 | 2. Toolchain | 0:16 | 2. Toolchain. Match each bullet to files in the repository. Verilator -sv, --timing, UVM includes; make SIM=verilator TEST=test_uart_uvm; +UVM_TESTNAME=UartTxTest. |
| 30 | Hands-on examples | 0:08 | Next section: Hands-on examples. |
| 31 | Module 4 self-check | 0:45 | Module 4 self-check. Watch the terminal output and confirm you see the expected pass message. |
| 32 | Exercise scaffold | 0:28 | Exercise scaffold. Review the code on screen and match it to files in the repository. |
| 33 | Example 1: UART UVM agent | 0:24 | Example 1: UART UVM agent. Same UART DUT as Module 3 with a full UVM agent (sequence, driver, monitor, scoreboard) Monitor reconstructs bytes from the serial tx line Loopback RX checking via check_rx_byte in the scoreboard module4/examples/uart_uvm/README.md |
| 34 | Demo: UART UVM agent | 0:45 | Demo: UART UVM agent. Watch the terminal output and confirm you see the expected pass message. |
| 35 | Key concepts | 0:08 | Next section: Key concepts. |
| 36 | 1. Reuse DUT, upgrade TB | 0:16 | 1. Reuse DUT, upgrade TB. RTL unchanged from baseline; UVM replaces directed initial stimulus. |
| 37 | 2. Dual path checking | 0:16 | 2. Dual path checking. TX monitor reconstructs serial bytes; RX hook checks loopback data_valid. |
| 38 | Common pitfalls | 0:08 | Next section: Common pitfalls. |
| 39 | Monitor baud mismatch | 0:24 | Monitor baud mismatch. Mistake: Sampling tx at system clock instead of baud_tick times. Correct: One sample per baud_tick per UART rules (as in UartTxMonitor). Why: Reconstructed byte will not match driven data. |
| 40 | Forgetting loopback RX check | 0:24 | Forgetting loopback RX check. Mistake: Scoreboard only compares TX monitor output. Correct: Also call check_rx_byte when data_valid asserts. Why: TX path can pass while RX is broken. |
| 41 | Practice & assessment | 0:08 | Next section: Practice & assessment. |
| 42 | What you should know | 0:28 | By now you should be able to explain the following. Describe the UART UVM agent (transaction, sequence, driver, monitor, scoreboard). Explain loopback (TX→RX) and how TX and RX are both checked in the scoreboard. Run the uart_uvm example and interpret UVM output. Ready for Module 5: SPI protocol + RTL + basic testbench. From MODULE4 Learning Outcomes. |
| 43 | Exercises | 0:28 | Exercises. Run uart_uvm Trace one transaction Change the sequence Optional: Loopback path |
| 44 | Assessment checklist | 0:28 | Assessment checklist. Can describe the UART UVM agent: transaction (one byte), sequence, driver, monitor, scoreboard. Can explain loopback and how TX and RX are both checked. Can run uart_uvm and interpret UVM output (phases, scoreboard summary). Ready for Module 5: SPI protocol + RTL + basic testbench. |
| 45 | Summary & next steps | 0:28 | In summary: Extend UART verification to UVM+SV — UART agent (transaction, sequence, driver, monitor, scoreboard); run on Verilator. Next up: SPI. Extend UART verification to UVM+SV — UART agent (transaction, sequence, driver, monitor, scoreboard); run on Verilator. Complete module4/CHECKLIST.md Review module4/EXAMPLES.md and run each lab Next: SPI |

        ## Section narration (edit for TTS)

        - **How to learn:** Read the detailed UART learning guide: UART_LEARNING_GUIDE.md — what UART is, how it works (frame, baud, TX/RX), and how it maps to our RTL. Then Read the protocols + UVM overview: LEARNING_GUIDE_PROTOCOLS_AND_UVM.md — Part B § 5. How UVM Maps to a Protocol and § 6. UART UVM Mapping (where UVM sits, how transaction/driver/monitor/scoreboard map to UART)..
- **Design architecture (UART DUT (reused from Module 3), UVM testbench hierarchy, Dual check paths):** Walk through the block diagram, then relate each block to files under module4/examples/.
- **Execution:** Explain make run / UVM make steps, then walk the artifact table and directed-test sequence slide by slide.
- **Verification (Directed UART regression, Scoreboard strategy, What to add next):** Explain what stimulus is applied, what is checked, and what is intentionally out of scope.
- **Syllabus:** Cover 2 topic section(s) — pause on protocol timing and signals.
- **Before exercises:** Ask learners to recall the learning outcomes slide; they should explain each bullet in their own words.
- **Hands-on:** Run module4/EXAMPLES.md labs; narrate expected PASS lines.

        ## Notes

        - Slides from **Before You Start**, **Design Architecture**, **Verification & Testing Methods**, **Topics Covered**, **EXAMPLES.md**, and **Learning Outcomes**.
        - Full detail: `docs/MODULE4.md` and `module4/EXAMPLES.md`.
        - Regenerate: `regenerate_course_outlines.sh <course_root> --module 4`
