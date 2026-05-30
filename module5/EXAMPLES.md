# Module 5 — Hands-on labs

Generated from `docs/MODULE5.md` for slides, PDF, and video.
Run commands from the **course repository root** unless noted.

**Course topic:** SPI — Protocol + RTL + Basic Testbench

## 1. SPI baseline master (`spi_baseline/`)

**Source:** `module5/examples/spi_baseline/`

**What you'll learn:**
- SPI Mode 0 master RTL (`spi_master` + `clk_div`)
- Directed writes 0x55 and 0xAA with `start` / `wait(done)`
- Observing SCLK, MOSI, and CS_N timing in simulation (optional VCD)

**Run:**

```bash
cd module5/examples/spi_baseline && make run
```

**You should see:** SPI baseline test PASS

**Go deeper:** Read the full walkthrough in `docs/MODULE5.md` and explore `module5/examples/spi_baseline/`.
