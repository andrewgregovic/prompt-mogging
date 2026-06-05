# Prompt Mogging — CHANGELOG v0.1.4

## v0.1.4 — Activation Reliability Patch

**Status:** Built release pack — full `SKILL.md` v0.1.4 included and version-synced with `NATIVE_CORE.md`.  
**Baseline:** v0.1.3 draft.  
**Release type:** Narrow reliability patch.

### Why this release exists

v0.1.3 could be loaded or turned on without producing visible Prompt Mogging behavior. The runtime could fall through to ordinary “answer the request” behavior when no detector fired. This made the skill indistinguishable from generic assistant prose on clean in-scope questions.

Core lesson:

> A skill is not loaded unless its behavioral delta is visible.

### Changed

- Active default stance changed from Balanced candor/collaboration to **Adversarial-but-constructive** for in-scope work.
- Core integrated posture/floor behaviors are ON by default for in-scope work.
- Added visible-delta rule for substantial in-scope answers.
- Added explicit honest-null option: “Nothing to push on here — the frame holds and the claim is calibrated.”
- Added manufactured-challenge guard: fake-adversarial is as dishonest as fake-agreeable.
- Reconciled `chill`: now soft suppression, while `skill off` / `drop the skill` remain hard dormant.
- Added load-state honesty taxonomy: in-context, retrieved, session-paste, claimed-load failure.
- Added native packaging rule: activation-critical rules must live in always-in-context native instructions.
- Added `NATIVE_CORE.md` as the runtime-critical compressed activation core.
- Added v0.1.4 acceptance tests.

### Preserved

- Play mode remains explicit opt-in only.
- Footer offers remain detector-gated and cooldown-tuned.
- Optional moves remain optional.
- Chat-only/no-agent boundary remains intact.
- No new agentic routing, validation, execution, or backend state.
- STOPmaxxing remains excluded.

### Release blockers

- None known after build. Run acceptance tests before publishing.

### Previous candidate blockers now closed

Before shipping v0.1.4:

1. Run `NATIVE_CORE.md` standalone against the acceptance tests.
2. Confirm the no-nagware, manufactured-challenge, and gate-integrity tests pass.
3. Verify all artifact version stamps match.
4. If `SKILL.md` and `NATIVE_CORE.md` conflict on activation behavior, resync before release.
