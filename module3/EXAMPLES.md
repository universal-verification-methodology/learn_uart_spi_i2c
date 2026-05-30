# Module 3 — Hands-on labs

Generated from `docs/MODULE3.md` for slides, PDF, and video.
Run commands from the **course repository root** unless noted.

**Course topic:** UART — Protocol + RTL + Basic Testbench

## 1. UART baseline loopback (`uart_baseline/`)

**Source:** `module3/examples/uart_baseline/`

**What you'll learn:**
- UART 8N1 TX/RX RTL with shared `baud_gen`
- Loopback wiring (`rx = tx`) and directed bytes 0x55 / 0xAA
- Baseline self-check without UVM (wait for `data_valid`, compare `data_out`)

**Run:**

```bash
cd module3/examples/uart_baseline && make run
```

**You should see:** UART baseline test PASS

**Go deeper:** Read the full walkthrough in `docs/MODULE3.md` and explore `module3/examples/uart_baseline/`.
