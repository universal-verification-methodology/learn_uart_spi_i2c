# Module 2 — Hands-on labs

Generated from `docs/MODULE2.md` for slides, PDF, and video.
Run commands from the **course repository root** unless noted.

**Course topic:** Design & Verification Methodology (Part 2)

## 1. UVM smoke test (`uvm_smoke/`)

**Source:** `module2/examples/uvm_smoke/`

**What you'll learn:**
- UVM transaction, sequence, driver, monitor, and scoreboard on a tiny register DUT
- How objections start and end the test in `run_phase`
- Interpreting DRIVER / MONITOR / SCOREBOARD messages and match counts

**Run:**

```bash
cd module2/examples/uvm_smoke && make SIM=verilator TEST=test_uvm_smoke
```

**You should see:** SCOREBOARD

**Go deeper:** Read the full walkthrough in `docs/MODULE2.md` and explore `module2/examples/uvm_smoke/`.
