# Module 1: Design & Verification Methodology (Part 1)

**Goal**: Understand the specification → RTL design flow, design methodology, and why we verify.

## Overview

This module establishes the **methodology** you will use for the rest of the course:

- **Specification → RTL**: From a written spec to synthesizable RTL
- **Design methodology**: How to structure and document a small block
- **Intro to verification**: What we verify, and why (before diving into UVM in Module 2)

No protocol-specific content (UART/SPI/I²C) or UVM yet—those come in later modules.

## How to learn this module

1. Read [docs/MODULE1.md](../docs/MODULE1.md) — **Before You Start**, **Design Architecture**, **Verification & Testing Methods**, then **Topics Covered**.
2. Use [UNDERSTANDING_THE_SPEC.md](UNDERSTANDING_THE_SPEC.md) and [SPEC_TO_RTL_GUIDE.md](SPEC_TO_RTL_GUIDE.md) while studying the counter example.
3. Run [EXAMPLES.md](EXAMPLES.md), then review [media/module1/slides.pptx](../media/module1/slides.pptx) (or `video.mp4`).

## Links

- **Full module doc**: [docs/MODULE1.md](../docs/MODULE1.md)
- **Hands-on example**: [EXAMPLES.md](EXAMPLES.md)
- **Example: spec → RTL**: [examples/spec_to_rtl/](examples/spec_to_rtl/)

### For beginners: understanding the spec and translating to design

- **[UNDERSTANDING_THE_SPEC.md](UNDERSTANDING_THE_SPEC.md)** — How to read a specification: what to look for (interface, behavior, timing, edge cases) and a simple checklist.
- **[SPEC_TO_RTL_GUIDE.md](SPEC_TO_RTL_GUIDE.md)** — How to translate a spec into RTL step by step: ports, clock/reset, reset branch, normal behavior, edge cases, and traceability.
- **[examples/spec_to_rtl/WALKTHROUGH.md](examples/spec_to_rtl/WALKTHROUGH.md)** — Concrete walkthrough: our counter spec read section-by-section and each requirement mapped to the exact RTL in `dut/counter.v`.

## Quick Start

1. **Environment** (Verilator + Make + C++ compiler):

```bash
verilator --version
make --version
```

2. **Run the spec-to-RTL example** (tiny counter: spec → RTL → simulation):

```bash
cd module1/examples/spec_to_rtl
make run
```

See [examples/spec_to_rtl/README.md](examples/spec_to_rtl/README.md) for details.

## Next Steps

After completing this module, proceed to **Module 2: Design & Verification Methodology (Part 2)** — basic testbench, UVM+SV, and toolchain.
