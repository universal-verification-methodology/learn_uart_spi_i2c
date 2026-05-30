# Module 6: SPI — UVM+SV Verification

**Goal**: Extend SPI verification to **UVM+SV** — SPI agent (transaction, sequence, driver, monitor, scoreboard); run on Verilator.

## Overview

This module builds on Module 5 (SPI protocol + RTL + basic testbench):

- **Same DUT**: SPI master and clk_div (reused from module5/examples/spi_baseline).
- **UVM testbench**: SPI agent — transaction, sequence, driver, monitor, scoreboard; directed sequence (e.g. 0x00, 0x01, 0x55, 0xAA, 0xFF); monitor observes MOSI and scoreboard checks expected vs observed.
- **Toolchain**: Verilator + UVM_HOME + Make (same as Module 2).

## How to learn this module

1. Read [docs/MODULE6.md](../docs/MODULE6.md) and [docs/SPI_LEARNING_GUIDE.md](../docs/SPI_LEARNING_GUIDE.md) (UVM mapping § 7).
2. Complete Module 5 `spi_baseline` first.
3. Run [EXAMPLES.md](EXAMPLES.md), then review [media/module6/slides.pptx](../media/module6/slides.pptx).

## Links

- **Full module doc**: [docs/MODULE6.md](../docs/MODULE6.md)
- **Examples**: [EXAMPLES.md](EXAMPLES.md)
- **Checklist**: [CHECKLIST.md](CHECKLIST.md)
- **Example: SPI UVM**: [examples/spi_uvm/](examples/spi_uvm/)

## Quick Start

1. **Environment**: Verilator, Make, C++ compiler, **UVM** (UVM_HOME or vendored UVM).

2. **Run the SPI UVM example**:

```bash
cd module6/examples/spi_uvm
make SIM=verilator TEST=test_spi_uvm
```

Or from repo root: `./scripts/module6.sh --run`

See [examples/spi_uvm/README.md](examples/spi_uvm/README.md) for details.

## Next Steps

After completing this module, proceed to **Module 7: I²C** — protocol + RTL + basic testbench.
