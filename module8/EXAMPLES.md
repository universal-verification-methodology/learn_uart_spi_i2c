# Module 8 — Hands-on labs

Generated from `docs/MODULE8.md` for slides, PDF, and video.
Run commands from the **course repository root** unless noted.

**Course topic:** I²C — UVM+SV Verification

## 1. I²C UVM agent (`i2c_uvm/`)

**Source:** `module8/examples/i2c_uvm/`

**What you'll learn:**
- I²C DUT from Module 7 with UVM agent and two-phase scoreboard (addr + data)
- `I2cMonitor` reuses baseline bus-sampling ideas in reusable form
- Course capstone: compare UART, SPI, and I²C verification patterns

**Run:**

```bash
cd module8/examples/i2c_uvm && make SIM=verilator TEST=test_i2c_uvm
```

**You should see:** SCOREBOARD

**Go deeper:** Read the full walkthrough in `docs/MODULE8.md` and explore `module8/examples/i2c_uvm/`.
