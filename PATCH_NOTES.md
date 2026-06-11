# Prompt Mogging v0.2.3 — Patch Notes

## Release name

v0.2.3 — Dispatcher / Semantic Rule Runtime

## Baseline

v0.1.5 — Factuality Hygiene + Controls.

## Patch purpose

Move Prompt Mogging from a `NATIVE_CORE` + reference-spec architecture to a dispatcher + full semantic ruleset architecture.

The field problem was under-firing from recognition failure and salience decay. The fix is a high-salience dispatcher stub plus a machine-scannable full skill with Trigger Index, `WHEN:` lines, tags, debug, and compact preference memory.

---

## Patch 1 — Dispatcher split

Add `DISPATCHER_STUB.md` for platform/custom instructions.

The stub:

- silently consults the full skill each turn,
- activates only when full skill is loaded and intended to govern,
- treats fragments/review pastes/discussion as not loaded,
- is inert without full skill,
- contains no floor content,
- outranks tone/personality settings.

---

## Patch 2 — NATIVE_CORE retirement

`NATIVE_CORE.md` is retired as active runtime artifact.

Floor semantics are merged into `SKILL.md`.

Root `NATIVE_CORE.md` becomes a tombstone to prevent accidental use of old v0.1.x instructions.

---

## Patch 3 — Semantic rule runtime

`SKILL.md` now contains:

- activation contract,
- Trigger Index,
- per-technique `WHEN:` lines,
- floor rules,
- optional moves,
- runtime algorithm,
- priority order,
- visible tags,
- debug/status diagnostics,
- compact memory preferences,
- lessons-learnt promotion pipeline.

---

## Patch 4 — Play boundary hardening

Play mode now:

- enters only on explicit command directed at skill/mode,
- does not activate on ordinary “what if” questions,
- tags entry/exit only,
- cannot suppress no-pill/reframe on decision/commitment/launch/spend questions,
- forces rigor split or exit offer for commitment questions.

---

## Patch 5 — Observability

Added:

- `[pm-*]` activation tags,
- `[pm-debug]` compact debug footers,
- `[pm-diagnostic]` explicit why-silent diagnostics,
- tag epistemics rule: tags are best-effort attribution, not causal proof.

---

## Patch 6 — Memory discipline

Added:

- `PM_PREF` compact preference records,
- `PM_REC` compact recurrence records,
- rule against storing raw traces, debug logs, hidden reasoning, did-it-help signals, or temporary task state.

---

## Patch 7 — Test and tutorial rewrite

Rewrote:

- `ACCEPTANCE_TESTS.md`,
- `TUTORIAL.md`,
- README usage instructions,
- dist package and manifest.

`ACCEPTANCE_TESTS.md` remains behavioral authority.
