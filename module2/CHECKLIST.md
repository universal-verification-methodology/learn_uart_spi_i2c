# Module 2 Checklist: Design & Verification Methodology (Part 2)

## Prerequisites

- [ ] Module 1 completed (spec_to_rtl run and traceability exercise).

## Read and understand

- [ ] Read [docs/MODULE2.md](../docs/MODULE2.md) — Design Architecture and Verification sections.
- [ ] UVM_HOME set (or vendored UVM under `tools/`).

## Hands-on

- [ ] Run [EXAMPLES.md](EXAMPLES.md) (`uvm_smoke` → scoreboard matches, no mismatches).
- [ ] Trace one transaction: sequence → driver → DUT → monitor → scoreboard.

## You should be able to

- [ ] Name the role of transaction, sequence, driver, monitor, scoreboard, agent, env, test.
- [ ] Explain how UVM replaces ad-hoc `initial` pin wiggling from Module 1.
- [ ] Run Verilator + UVM build (`make SIM=verilator TEST=test_uvm_smoke`).

## Next

- [ ] Ready for Module 3: UART protocol + RTL + basic testbench.
