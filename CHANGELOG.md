# Prompt Mogging — CHANGELOG v0.1.5

## v0.1.5 — Factuality Hygiene + Controls

**Status:** Candidate release pack for review.  
**Baseline:** v0.1.4 Activation Reliability Patch.  
**Release type:** Narrow floor/control/tutorial patch.

### Why this release exists

v0.1.4 fixed activation reliability. Testing then surfaced two product-level improvements and one floor issue:

1. The skill could make current market/platform/study claims without citations or uncertainty labels.
2. `skill on/off` is too generic for a multi-skill environment.
3. The smoke-test sequence is useful as a user-facing tutorial.

### Changed

- Added factuality / citation hygiene for recent or temporally unstable load-bearing claims.
- Put factuality hygiene in both `NATIVE_CORE.md` and full `SKILL.md`; it is a floor rule, not optional reference material.
- Added a no-tic guard: do not reflexively caveat stable or non-load-bearing facts.
- Namespaced public controls: `prompt mogging on/off`, `mog on/off`, `mog chill`, `mog play`, `floor back on`.
- Kept `skill on/off` as legacy/contextual aliases only.
- Clarified that hard-off disables Prompt Mogging behavior only and never disables base-model safety/factuality.
- Added `TUTORIAL.md` as a user-facing game tutorial and smoke-test walkthrough.
- Added tutorial/test authority rule: tutorial illustrates; acceptance tests adjudicate.
- Added v0.1.5 acceptance tests.

### Preserved

- v0.1.4 activation reliability.
- Adversarial-but-constructive default for in-scope work.
- Visible-delta rule.
- No manufactured challenge.
- No-nagware / detector-gated footer model.
- Play remains opt-in.
- Chill remains soft suppression.
- Chat-only/no-agent boundary.

### Review gates before publishing

- Factuality hygiene appears in `NATIVE_CORE.md` and `SKILL.md`.
- Native core remains within practical instruction-size limits.
- `mog off` floor-survival test passes.
- Factuality hygiene and factuality-tic tests both pass.
- Tutorial matches acceptance tests and defers to them.
- All version stamps match v0.1.5.

---

## v0.1.4 — Activation Reliability Patch

See prior release for full notes. v0.1.4 fixed the failure where Prompt Mogging could be “loaded” or turned on without visible behavioral delta.
