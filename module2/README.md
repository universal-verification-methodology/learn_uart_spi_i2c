# Module 2: Design & Verification Methodology (Part 2)

**Goal**: Understand basic testbench patterns (directed tests, pin wiggling), the evolution to a UVM+SV testbench (agents, sequences, drivers, monitors, scoreboards), and the toolchain (Verilator, UVM_HOME, Make).

## Overview

This module builds on Module 1 (spec → RTL) by focusing on **verification**:

- **Basic testbench**: Directed tests, pin wiggling — driving inputs and checking outputs.
- **UVM+SV**: How a full testbench is structured (transaction, sequence, driver, monitor, scoreboard) and how that scales to protocol verification in later modules.
- **Toolchain**: Verilator + UVM_HOME + Make — build and run a UVM test on RTL.

No protocol-specific content (UART/SPI/I²C) yet; those start in Module 3.

## How to learn this module

1. Read [docs/MODULE2.md](../docs/MODULE2.md) — architecture and verification sections before running UVM.
2. Complete Module 1 `spec_to_rtl` if you have not already.
3. Run [EXAMPLES.md](EXAMPLES.md) (`uvm_smoke`), then review [media/module2/slides.pptx](../media/module2/slides.pptx).

## Links

- **Full module doc**: [docs/MODULE2.md](../docs/MODULE2.md)
- **Hands-on example**: [EXAMPLES.md](EXAMPLES.md)
- **Example: UVM smoke**: [examples/uvm_smoke/](examples/uvm_smoke/)

## Quick Start

1. **Environment** (Verilator, Make, C++ compiler, UVM):

```bash
verilator --version
make --version
echo "$UVM_HOME"
ls "$UVM_HOME/src/uvm_pkg.sv"
```

2. **Run the UVM smoke example** (tiny DUT + full UVM agent):

```bash
cd module2/examples/uvm_smoke
make SIM=verilator TEST=test_uvm_smoke
```

Or from repo root:

```bash
./scripts/module2.sh --run
```

See [examples/uvm_smoke/README.md](examples/uvm_smoke/README.md) for details.

## Next Steps

After completing this module, proceed to **Module 3: UART** — protocol details, RTL (TX/RX, baud gen), and basic (non-UVM) testbench.
