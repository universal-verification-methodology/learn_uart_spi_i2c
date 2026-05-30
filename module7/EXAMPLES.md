# Module 7 — Hands-on labs

Generated from `docs/MODULE7.md` for slides, PDF, and video.
Run commands from the **course repository root** unless noted.

**Course topic:** I²C — Protocol + RTL + Basic Testbench

## 1. I²C baseline master (`i2c_baseline/`)

**Source:** `module7/examples/i2c_baseline/`

**What you'll learn:**
- I²C master FSM: START → address+W → data → STOP
- Inline bus monitor sampling SDA on rising SCL
- Comparing reconstructed address and data bytes to stimulus

**Run:**

```bash
cd module7/examples/i2c_baseline && make run
```

**You should see:** I2C baseline test PASS

**Go deeper:** Read the full walkthrough in `docs/MODULE7.md` and explore `module7/examples/i2c_baseline/`.
