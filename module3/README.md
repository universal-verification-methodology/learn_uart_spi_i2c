# Module 3: UART — Protocol + RTL + Basic Testbench

**Goal**: Understand the UART protocol (8N1, baud), translate it to RTL (TX, RX, baud gen), and verify with a **basic** (non-UVM) directed testbench.

## Overview

This module is the first **protocol** module:

- **UART protocol**: 8N1 framing, start/stop bits, baud rate.
- **RTL**: `uart_tx`, `uart_rx`, `baud_gen` (from spec → RTL methodology).
- **Basic testbench**: Directed test (e.g. loopback TX→RX, send bytes, check received bytes). No UVM yet—UVM for UART is Module 4.

## How to learn this module

1. Read [docs/MODULE3.md](../docs/MODULE3.md) — **Before You Start**, **Design Architecture**, **Verification & Testing Methods**, then **Topics Covered**.
2. Read [docs/UART_LEARNING_GUIDE.md](../docs/UART_LEARNING_GUIDE.md) for protocol depth.
3. Follow hands-on labs in [EXAMPLES.md](EXAMPLES.md), then watch [media/module3/slides.pptx](../media/module3/slides.pptx) or `video.mp4` if available.

## Links

- **Full module doc**: [docs/MODULE3.md](../docs/MODULE3.md)
- **Hands-on labs**: [EXAMPLES.md](EXAMPLES.md)
- **Checklist**: [CHECKLIST.md](CHECKLIST.md)
- **Example: UART baseline**: [examples/uart_baseline/](examples/uart_baseline/)

## Quick Start

1. **Environment**: Verilator, Make, C++ compiler (no UVM required for this example).

2. **Run the UART baseline example** (loopback, directed test):

```bash
cd module3/examples/uart_baseline
make run
```

Or from repo root: `./scripts/module3.sh --run`

See [examples/uart_baseline/README.md](examples/uart_baseline/README.md) for details.

## Next Steps

After completing this module, proceed to **Module 4: UART UVM+SV** — full UART verification with UVM (agent, sequences, driver, monitor, scoreboard).
