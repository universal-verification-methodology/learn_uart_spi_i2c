        # Narration script — Module 3: UART — Protocol + RTL + Basic Testbench

        **Target length:** ~24 minutes (60 slides; auto-generated — edit per slide as needed)

        ## Timing table

        | Slide | Section | Duration | Narration |
|-------|---------|----------|-----------|
| 1 | Module 3 | 0:25 | Welcome to module 3, UART — Protocol + RTL + Basic Testbench. In this module you will understand the uart protocol (8n1, baud), translate it to rtl (tx, rx, baud gen), and verify with a basic (non-uvm) directed testbench.. |
| 2 | Learning objectives | 0:28 | Here is what you will learn in this module. UART 8N1: Start bit (0), 8 data bits (LSB first), stop bit (1); idle high. Baud rate: Role of a baud generator (clock divider → baud_tick). RTL architecture: TX (parallel→serial, shift per baud_tick), RX (start detect, sample, data_valid), baud_gen (divider). Basic TB: Loopback, directed stimulus, and checking without UVM. |
| 3 | Prerequisites | 0:20 | Before you start, make sure you have these prerequisites. Module 1 (spec → RTL) and Module 2 (basic TB → UVM, toolchain). Verilator, Make, C++ compiler. No UVM required for the uart_baseline example. |
| 4 | Learning path | 0:22 | Learning path. Understand the UART protocol (8N1, baud), translate it to RTL (TX, RX, baud gen), and verify with a basic (non-UVM) directed testbench. |
| 5 | Overview | 0:16 | Overview. Module 3 is the first protocol module: |
| 6 | How to learn this module | 0:08 | Next section: How to learn this module. |
| 7 | Suggested learning path | 0:20 | Follow this learning path. Read the guides before running the labs. Read the detailed UART learning guide: UART_LEARNING_GUIDE.md — what UART is, what kind of protocol (serial, asynchronous... Read the protocols + UVM overview: LEARNING_GUIDE_PROTOCOLS_AND_UVM.md — Part B § 4. When to Use Baseline vs UVM (why we start with a... From docs/MODULE3.md — read guides before running demos. |
| 8 | Design architecture | 0:08 | Next section: Design architecture. |
| 9 | 1. Block hierarchy | 0:30 | 1. Block hierarchy. top_uart_baseline → baud_gen, uart_tx, uart_rx; sim_main.cpp drives clk/rst_n only. Loopback: assign rx = tx — one wire connects transmitter to receiver. Refer to the diagram on the right. |
| 10 | 2. RTL blocks | 0:34 | 2. RTL blocks. baud_gen: DIVIDER → baud_tick every N clocks; shared by TX and RX. uart_tx: parallel-in / serial-out; start + 8 data (LSB first) + stop; busy during frame. uart_rx: start detect, sample per baud_tick, data_valid + optional framing_error. Refer to the diagram on the right. |
| 11 | 3. Timing and clocking | 0:26 | 3. Timing and clocking. Single clk domain; async rst_n; all bit times referenced to baud_tick. Refer to the diagram on the right. |
| 12 | RTL block diagram (reference) | 0:22 | RTL block diagram (reference). Module 3: DUT hierarchy and signal flow. |
| 13 | Verification / testbench diagram (reference) | 0:22 | Verification / testbench diagram (reference). Module 3: stimulus, observation, and checking. |
| 14 | uart_tx — 8N1 frame FSM | 0:28 | uart_tx — 8N1 frame FSM. Review the code on screen and match it to files in the repository. |
| 15 | uart_rx — start detect & sample | 0:28 | uart_rx — start detect & sample. Review the code on screen and match it to files in the repository. |
| 16 | baud_gen — divider → baud_tick | 0:28 | baud_gen — divider → baud_tick. Review the code on screen and match it to files in the repository. |
| 17 | Execution & simulation flow | 0:08 | Next section: Execution & simulation flow. |
| 18 | How the example runs (toolchain) | 0:32 | How the example runs (toolchain). Match each bullet to files in the repository. Makefile: Verilator compiles RTL + SystemVerilog testbench into a C++ model sim_main.cpp: generates clk/rst_n, calls eval() until $finish Directed test (initial block or C++): drive stimulus, wait for DUT flags Self-check: compare outputs; print PASS/FAIL (see terminal demo slide) Repo path... |
| 19 | Example directory layout | 0:24 | Example directory layout. Match each bullet to files in the repository. dut/: uart_tx.v, uart_rx.v, baud_gen.v top_uart_baseline.sv: Loopback (rx=tx), baud_gen, uart_tx, uart_rx; directed test in initial block sim_main.cpp: Clock, reset; run until $finish Match each path to files under module/examples/. |
| 20 | Directed test execution sequence (1) | 0:32 | This section explains how the example is built and executed in simulation. wait(rst_n) pulse start/data_in wait(!busy) wait(data_valid) compare data_out Follow this order when tracing waveforms or debugging. |
| 21 | Directed test execution sequence (2) | 0:20 | This section explains how the example is built and executed in simulation. repeat $finish. Follow this order when tracing waveforms or debugging. |
| 22 | Makefile — uart_baseline run | 0:28 | Makefile — uart_baseline run. Review the code on screen and match it to files in the repository. |
| 23 | Key files to study | 0:08 | Next section: Key files to study. |
| 24 | Open these in the repo | 0:32 | Open these in the repo. module3/examples/uart_baseline/dut/baud_gen.v — divider → baud_tick module3/examples/uart_baseline/dut/uart_tx.v — 8N1 transmit module3/examples/uart_baseline/dut/uart_rx.v — receive and data_valid module3/examples/uart_baseline/top_uart_baseline.sv — loopback + directed test docs/UART_LEARNING_GUIDE.md — protocol reference Trace while running module3/EXAMPLES.md labs. |
| 25 | Verification & testing methods | 0:08 | Next section: Verification & testing methods. |
| 26 | 1. Verification goals | 0:30 | 1. Verification goals. Prove RTL implements UART 8N1 before UVM (Module 4). Happy-path loopback: bytes sent on TX appear correctly on RX. Refer to the diagram on the right. |
| 27 | 2. Baseline directed test | 0:34 | 2. Baseline directed test. Stimulus: initial block — start, data_in (0x55, 0xAA). Check: wait(data_valid); compare data_out; $error / $display. No UVM: pin wiggling only — fastest way to learn the protocol on real RTL. Refer to the diagram on the right. |
| 28 | 3. Coverage gaps (defer to Module 4) | 0:30 | 3. Coverage gaps (defer to Module 4). Random baud, framing errors, busy back-to-back, functional coverage. Map checks to UART_LEARNING_GUIDE.md spec bullets. Refer to the diagram on the right. |
| 29 | Loopback directed test | 0:28 | Loopback directed test. Review the code on screen and match it to files in the repository. |
| 30 | Syllabus topics | 0:08 | Next section: Syllabus topics. |
| 31 | Protocol & design details | 0:08 | Next section: Protocol & design details. |
| 32 | Detail: UART quick reference (8N1) (1) | 0:28 | Protocol and design detail: UART quick reference (8N1) (1). Framing: idle=1 → start=0 → 8 data bits (LSB first) → stop=1. Baud math: DIVIDER = round(clk_hz / baud). Example: 50 MHz clock, 115200 baud → divider ≈ 434. Sampling: Basic design samples once per bit at the baud_tick. Production UARTs often oversample (e.g., 8x or 16x) to tolerate clock... Reset state: Line idles high, TX not busy... |
| 33 | Detail: UART quick reference (8N1) (2) | 0:16 | Protocol and design detail: UART quick reference (8N1) (2). Errors: framing_error when stop bit is not high at expected sample; optional parity_error if parity enabled (not used in 8N1 baseline). From MODULE3 Topics Covered — protocol/design depth. |
| 34 | Detail: TX design checklist | 0:28 | Protocol and design detail: TX design checklist. Inputs: clk, rst_n, baud_tick, start, data_in[7:0]. Outputs: tx, busy. Behavior: On start, latch data_in, drive start bit low, then shift out bits [0:7] each baud_tick, then drive stop bit high for one... Edge cases: Ignore start while busy (or queue it in a FIFO if you extend the design). From MODULE3 Topics Covered — protocol/design depth. |
| 35 | Detail: RX design checklist | 0:28 | Protocol and design detail: RX design checklist. Inputs: clk, rst_n, baud_tick, rx. Outputs: data_out[7:0], data_valid (pulse), framing_error. Behavior: Detect falling edge for start; wait one baud_tick to sample mid-start; sample 8 bits on successive baud_ticks; sample stop... Robustness options: Add metastability sync on rx; add oversampling + majority vote; add rx_ready/rx_valid handshake... |
| 36 | Detail: Baud generator notes | 0:24 | Protocol and design detail: Baud generator notes. Inputs: clk, rst_n, divisor (constant parameter in the baseline). Output: baud_tick high for one cycle every divisor clocks. For synthesis, keep the counter simple (divisor-1 down-counter or up-counter compare). For sim, you can parametrize divisor to speed... From MODULE3 Topics Covered — protocol/design depth. |
| 37 | Detail: Protocol extensions (not in baseline example) (1) | 0:28 | Protocol and design detail: Protocol extensions (not in baseline example) (1). Data bits: 5–9 data bits are common. Parity: Even/odd/mark/space; adds a parity bit before stop. Stop bits: 1 or 2 stop bits. Flow control: RTS/CTS hardware pins (outside the serial line) to throttle traffic. From MODULE3 Topics Covered — protocol/design depth. |
| 38 | Detail: Protocol extensions (not in baseline example) (2) | 0:16 | Protocol and design detail: Protocol extensions (not in baseline example) (2). The baseline RTL assumes 8N1 with no parity and no flow control. From MODULE3 Topics Covered — protocol/design depth. |
| 39 | Verification flow (reference) | 0:22 | Verification flow (reference). Stimulus, DUT response, and check points for this module. |
| 40 | 1. UART Protocol (8N1) (1/4) | 0:36 | 1. UART Protocol (8N1) (1/4). Signals: Serial line (tx/rx), idle high; system clock; baud_tick (one pulse per bit time). Frame: 1 start bit (0), 8 data bits (LSB first), 1 stop bit (1). Timing: One bit per baud_tick; baud_tick derived from system clock via a divider (e.g. DIVIDER = clk_freq / baud_rate). Framing: idle=1 → start=0 → 8 data bits (LSB first) → stop=1. Baud math: DIVIDER =... |
| 41 | 1. UART Protocol (8N1) (2/4) | 0:36 | 1. UART Protocol (8N1) (2/4). Reset state: Line idles high, TX not busy, RX clears internal shift register, data_valid low. Errors: framing_error when stop bit is not high at expected sample; optional parity_error if parity enabled (not used in 8N1 baseline). Inputs: clk, rst_n, baud_tick, start, data_in[7:0]. Outputs: tx, busy. Behavior: On start, latch data_in, drive start bit low, then... |
| 42 | 1. UART Protocol (8N1) (3/4) | 0:36 | 1. UART Protocol (8N1) (3/4). Inputs: clk, rst_n, baud_tick, rx. Outputs: data_out[7:0], data_valid (pulse), framing_error. Behavior: Detect falling edge for start; wait one baud_tick to sample mid-start; sample 8 bits on successive baud_ticks; sample stop... Robustness options: Add metastability sync on rx; add oversampling + majority vote; add rx_ready/rx_valid handshake if you later... |
| 43 | 1. UART Protocol (8N1) (4/4) | 0:36 | 1. UART Protocol (8N1) (4/4). For synthesis, keep the counter simple (divisor-1 down-counter or up-counter compare). For sim, you can parametrize divisor to speed... Data bits: 5–9 data bits are common. Parity: Even/odd/mark/space; adds a parity bit before stop. Stop bits: 1 or 2 stop bits. Flow control: RTS/CTS hardware pins (outside the serial line) to throttle traffic. |
| 44 | 2. Hands-on testbench (uart_baseline) | 0:24 | 2. Hands-on testbench (uart_baseline). Loopback: Connect TX output to RX input; send bytes from TX, check they appear on RX. Directed test: Reset release, send 0x55 and 0xAA, wait for data_valid, check data_out. Implemented in top_uart_baseline.sv... Self-check flow: wait(rst_n) → pulse start/data_in → wait(!busy) → wait(data_valid) → compare data_out → repeat → $finish. |
| 45 | Hands-on examples | 0:08 | Next section: Hands-on examples. |
| 46 | Module 3 self-check | 0:45 | Module 3 self-check. Watch the terminal output and confirm you see the expected pass message. |
| 47 | Exercise scaffold | 0:28 | Exercise scaffold. Review the code on screen and match it to files in the repository. |
| 48 | Example 1: UART baseline loopback | 0:24 | Example 1: UART baseline loopback. UART 8N1 TX/RX RTL with shared baud_gen Loopback wiring (rx = tx) and directed bytes 0x55 / 0xAA Baseline self-check without UVM (wait for data_valid, compare data_out) module3/examples/uart_baseline/README.md |
| 49 | Demo: UART baseline loopback | 0:45 | Demo: UART baseline loopback. Watch the terminal output and confirm you see the expected pass message. |
| 50 | Key concepts | 0:08 | Next section: Key concepts. |
| 51 | 1. Asynchronous serial | 0:20 | 1. Asynchronous serial. No dedicated clock wire; TX and RX must share the same bit time (baud_tick). Loopback (rx = tx) proves TX serialization and RX deserialization together. |
| 52 | 2. 8N1 frame | 0:20 | 2. 8N1 frame. Idle high → start (0) → 8 data bits LSB first → stop (1). busy on TX; data_valid pulse on RX when a byte is ready. |
| 53 | Common pitfalls | 0:08 | Next section: Common pitfalls. |
| 54 | Mismatched baud timing | 0:24 | Mismatched baud timing. Mistake: Different dividers on TX and RX in a loopback test. Correct: One baud_gen drives both (as in uart_baseline). Why: RX samples at the wrong bit times. |
| 55 | Only checking busy | 0:24 | Only checking busy. Mistake: Assuming success when TX finishes. Correct: Wait for data_valid and compare data_out to the sent byte. Why: busy does not prove the loopback byte is correct. |
| 56 | Practice & assessment | 0:08 | Next section: Practice & assessment. |
| 57 | What you should know | 0:28 | By now you should be able to explain the following. Describe UART 8N1 frame and baud timing. Explain the role of uart_tx, uart_rx, and baud_gen. Run the uart_baseline example and interpret the loopback test. Ready for Module 4: UART UVM+SV verification. From MODULE3 Learning Outcomes. |
| 58 | Exercises | 0:28 | Exercises. Run uart_baseline Trace one byte Baud and divider Optional: Waveforms |
| 59 | Assessment checklist | 0:28 | Assessment checklist. Can describe UART 8N1 (start bit, 8 data LSB first, stop bit) and the role of baud_tick. Can explain the role of uart_tx, uart_rx, and baud_gen in the RTL. Can run uart_baseline and interpret the loopback test result. Ready for Module 4: UART UVM+SV verification. |
| 60 | Summary & next steps | 0:28 | In summary: Understand the UART protocol (8N1, baud), translate it to RTL (TX, RX, baud gen), and verify with a basic (non-UVM) directed testbench. Next up: UART UVM+SV. Understand the UART protocol (8N1, baud), translate it to RTL (TX, RX, baud gen), and verify with a basic (non-UVM) directed testbench. Complete module3/CHECKLIST.md Review module3/EXAMPLES.md and run each lab Next: UART UVM+SV |

        ## Section narration (edit for TTS)

        - **How to learn:** Read the detailed UART learning guide: UART_LEARNING_GUIDE.md — what UART is, what kind of protocol (serial, asynchronous, point-to-point), how it works (frame format, baud rate, TX/RX), timing, and where it’s used. Then Read the protocols + UVM overview: LEARNING_GUIDE_PROTOCOLS_AND_UVM.md — Part B § 4. When to Use Baseline vs UVM (why we start with a baseline testbench before UVM)..
- **Design architecture (Block hierarchy, RTL blocks, Timing and clocking):** Walk through the block diagram, then relate each block to files under module3/examples/.
- **Execution:** Explain make run / UVM make steps, then walk the artifact table and directed-test sequence slide by slide.
- **Verification (Verification goals, Baseline directed test, Coverage gaps (defer to Module 4)):** Explain what stimulus is applied, what is checked, and what is intentionally out of scope.
- **Syllabus:** Cover 2 topic section(s) — pause on protocol timing and signals.
- **Before exercises:** Ask learners to recall the learning outcomes slide; they should explain each bullet in their own words.
- **Hands-on:** Run module3/EXAMPLES.md labs; narrate expected PASS lines.

        ## Notes

        - Slides from **Before You Start**, **Design Architecture**, **Verification & Testing Methods**, **Topics Covered**, **EXAMPLES.md**, and **Learning Outcomes**.
        - Full detail: `docs/MODULE3.md` and `module3/EXAMPLES.md`.
        - Regenerate: `regenerate_course_outlines.sh <course_root> --module 3`
