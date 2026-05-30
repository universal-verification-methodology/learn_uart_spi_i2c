# Module 8: I²C — UVM+SV Verification

**Goal**: Extend I²C verification to **UVM+SV** — I²C agent (transaction, sequence, driver, monitor, scoreboard); run on Verilator.

## Overview

This module builds on Module 7 (I²C protocol + RTL + basic testbench):

- **Same DUT**: I²C master and clk_div (reused from module7/examples/i2c_baseline).
- **UVM testbench**: I²C agent — transaction, sequence, driver, monitor, scoreboard; directed sequence of address+data writes; monitor observes SDA/SCL and scoreboard checks expected vs observed.
- **Toolchain**: Verilator + UVM_HOME + Make (same as Module 2 and Module 6).

## How to learn this module

1. Read [docs/MODULE8.md](../docs/MODULE8.md) and [docs/I2C_LEARNING_GUIDE.md](../docs/I2C_LEARNING_GUIDE.md) (UVM mapping § 8).
2. Complete Module 7 `i2c_baseline` first.
3. Run [EXAMPLES.md](EXAMPLES.md), then compare with UART/SPI UVM modules; review [media/module8/slides.pptx](../media/module8/slides.pptx).

## Links

- **Full module doc**: [docs/MODULE8.md](../docs/MODULE8.md)
- **Examples**: [EXAMPLES.md](EXAMPLES.md)
- **Checklist**: [CHECKLIST.md](CHECKLIST.md)
- **Example: I²C UVM**: [examples/i2c_uvm/](examples/i2c_uvm/)

## Quick Start

1. **Environment**: Verilator, Make, C++ compiler, **UVM** (UVM_HOME or vendored UVM).

2. **Run the I²C UVM example**:

```bash
cd module8/examples/i2c_uvm
make SIM=verilator TEST=test_i2c_uvm
```

Or from repo root: `./scripts/module8.sh --run`

See [examples/i2c_uvm/README.md](examples/i2c_uvm/README.md) for details.

## Next Steps

This is the last module in the 8-module series; you can now compare methodology and UVM structure across UART, SPI, and I²C.
