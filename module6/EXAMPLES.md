# Module 6 — Hands-on labs

Generated from `docs/MODULE6.md` for slides, PDF, and video.
Run commands from the **course repository root** unless noted.

**Course topic:** SPI — UVM+SV Verification

## 1. SPI UVM agent (`spi_uvm/`)

**Source:** `module6/examples/spi_uvm/`

**What you'll learn:**
- SPI DUT from Module 5 with UVM driver, monitor, and scoreboard
- Monitor samples MOSI on rising SCLK (Mode 0, MSB first)
- Bus-centric checking vs relying only on the DUT `done` flag

**Run:**

```bash
cd module6/examples/spi_uvm && make SIM=verilator TEST=test_spi_uvm
```

**You should see:** SCOREBOARD

**Go deeper:** Read the full walkthrough in `docs/MODULE6.md` and explore `module6/examples/spi_uvm/`.
