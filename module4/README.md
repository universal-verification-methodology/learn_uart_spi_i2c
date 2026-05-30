# Module 4: UART — UVM+SV Verification

**Goal**: Extend UART verification to **UVM+SV** — UART agent (transaction, sequence, driver, monitor, scoreboard); run on Verilator.

## Overview

This module builds on Module 3 (UART protocol + RTL + basic testbench):

- **Same DUT**: UART TX, RX, baud_gen (reused from module3/examples/uart_baseline).
- **UVM testbench**: UART agent — transaction, sequence, driver, monitor, scoreboard; loopback TX→RX; directed sequence (e.g. 0x00, 0x01, 0x55, 0xAA, 0xFF).
- **Toolchain**: Verilator + UVM_HOME + Make (same as Module 2).

## How to learn this module

1. Read [docs/MODULE4.md](../docs/MODULE4.md) and [docs/UART_LEARNING_GUIDE.md](../docs/UART_LEARNING_GUIDE.md).
2. Complete Module 3 `uart_baseline` first.
3. Run [EXAMPLES.md](EXAMPLES.md), then review [media/module4/slides.pptx](../media/module4/slides.pptx).

## Links

- **Full module doc**: [docs/MODULE4.md](../docs/MODULE4.md)
- **Examples**: [EXAMPLES.md](EXAMPLES.md)
- **Checklist**: [CHECKLIST.md](CHECKLIST.md)
- **Example: UART UVM**: [examples/uart_uvm/](examples/uart_uvm/)

## Quick Start

1. **Environment**: Verilator, Make, C++ compiler, **UVM** (UVM_HOME or vendored UVM).

2. **Run the UART UVM example**:

```bash
cd module4/examples/uart_uvm
make SIM=verilator TEST=test_uart_uvm
```

Or from repo root: `./scripts/module4.sh --run`

See [examples/uart_uvm/README.md](examples/uart_uvm/README.md) for details.

## Next Steps

After completing this module, proceed to **Module 5: SPI** — protocol + RTL + basic testbench.
