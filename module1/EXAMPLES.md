# Module 1 — Hands-on labs

Generated from `docs/MODULE1.md` for slides, PDF, and video.
Run commands from the **course repository root** unless noted.

**Course topic:** Design & Verification Methodology (Part 1)

## 1. Spec to RTL counter (`spec_to_rtl/`)

**Source:** `module1/examples/spec_to_rtl/`

**What you'll learn:**
- Reading SPEC.md and mapping each requirement to RTL in `dut/counter.v`
- Building a minimal top and C++ harness (clock, reset, enable)
- Directed verification: enable for N cycles and check `count == N`

**Run:**

```bash
cd module1/examples/spec_to_rtl && make run
```

**You should see:** [PASS] spec_to_rtl

**Go deeper:** Read the full walkthrough in `docs/MODULE1.md` and explore `module1/examples/spec_to_rtl/`.
