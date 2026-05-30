# Module 5: SPI — Protocol + RTL + Basic Testbench

**Goal**: Understand the SPI protocol (mode 0, signals), translate it to RTL (SPI master, clk_div), and verify with a **basic** (non-UVM) directed testbench.

## Overview

This module is the second **protocol** module (after UART):

- **SPI protocol**: Mode 0 (CPOL=0, CPHA=0), SCLK, MOSI, CS_N; 8-bit transfers MSB first.
- **RTL**: `spi_master`, `clk_div` — master drives SCLK/MOSI/CS_N; divider produces clk_div_tick.
- **Basic testbench**: Directed test (start, data_in; wait for done). **No UVM** — UVM for SPI is Module 6.

## How to learn this module

1. Read [docs/MODULE5.md](../docs/MODULE5.md) and [docs/SPI_LEARNING_GUIDE.md](../docs/SPI_LEARNING_GUIDE.md).
2. Complete Modules 1–4 (methodology + UART) for context.
3. Run [EXAMPLES.md](EXAMPLES.md), then review [media/module5/slides.pptx](../media/module5/slides.pptx).

## Links

- **Full module doc**: [docs/MODULE5.md](../docs/MODULE5.md)
- **Examples**: [EXAMPLES.md](EXAMPLES.md)
- **Checklist**: [CHECKLIST.md](CHECKLIST.md)
- **Example: SPI baseline**: [examples/spi_baseline/](examples/spi_baseline/)

## Quick Start

1. **Environment**: Verilator, Make, C++ compiler (no UVM required for this example).

2. **Run the SPI baseline example**:

```bash
cd module5/examples/spi_baseline
make run
```

Or from repo root: `./scripts/module5.sh --run`

See [examples/spi_baseline/README.md](examples/spi_baseline/README.md) for details.

## Next Steps

After completing this module, proceed to **Module 6: SPI UVM+SV** — full SPI verification with UVM (agent, sequences, driver, monitor, scoreboard).
