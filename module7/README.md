# Module 7: I²C — Protocol + RTL + Basic Testbench

**Goal**: Understand the I²C protocol (start/stop, addressing, ACK/NACK), translate it to RTL (simple master + timing), and verify with a **basic** (non-UVM) directed testbench.

## Overview

This module is the third **protocol** module (after UART and SPI):

- **I²C protocol**: Two-wire bus (SCL, SDA), START/STOP conditions, 7-bit address + R/W bit, byte transfer (MSB first), ACK/NACK concept.
- **RTL**: `i2c_master`, `clk_div` — master generates SCL/SDA sequencing; divider produces `clk_div_tick` for timing.
- **Basic testbench**: Directed test (start, addr, data_in; wait for done) + simple bus monitor to reconstruct address and data from SDA/SCL. **No UVM** — UVM for I²C is Module 8.

> Note: The baseline RTL here is a **teaching simplification**: it treats SCL/SDA as push-pull outputs and does **not** model open-drain behavior, ACK/NACK, or multi-master arbitration.

## How to learn this module

1. Read [docs/MODULE7.md](../docs/MODULE7.md) and [docs/I2C_LEARNING_GUIDE.md](../docs/I2C_LEARNING_GUIDE.md).
2. Complete Modules 1–6 for methodology and UART/SPI context.
3. Run [EXAMPLES.md](EXAMPLES.md), then review [media/module7/slides.pptx](../media/module7/slides.pptx).

## Links

- **Full module doc**: [docs/MODULE7.md](../docs/MODULE7.md)
- **Examples**: [EXAMPLES.md](EXAMPLES.md)
- **Checklist**: [CHECKLIST.md](CHECKLIST.md)
- **Example: I²C baseline**: [examples/i2c_baseline/](examples/i2c_baseline/)

## Quick Start

1. **Environment**: Verilator, Make, C++ compiler (no UVM required for this example).

2. **Run the I²C baseline example**:

```bash
cd module7/examples/i2c_baseline
make run
```

Or from repo root: `./scripts/module7.sh --run`

See [examples/i2c_baseline/README.md](examples/i2c_baseline/README.md) for details.

## Next Steps

After completing this module, proceed to **Module 8: I²C UVM+SV** — full I²C verification with UVM (agent, sequences, driver, monitor, scoreboard).

