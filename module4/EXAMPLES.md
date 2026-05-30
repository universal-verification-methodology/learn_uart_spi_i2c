# Module 4 — Hands-on labs

Generated from `docs/MODULE4.md` for slides, PDF, and video.
Run commands from the **course repository root** unless noted.

**Course topic:** UART — UVM+SV Verification

## 1. UART UVM agent (`uart_uvm/`)

**Source:** `module4/examples/uart_uvm/`

**What you'll learn:**
- Same UART DUT as Module 3 with a full UVM agent (sequence, driver, monitor, scoreboard)
- Monitor reconstructs bytes from the serial `tx` line
- Loopback RX checking via `check_rx_byte` in the scoreboard

**Run:**

```bash
cd module4/examples/uart_uvm && make SIM=verilator TEST=test_uart_uvm
```

**You should see:** SCOREBOARD

**Go deeper:** Read the full walkthrough in `docs/MODULE4.md` and explore `module4/examples/uart_uvm/`.
