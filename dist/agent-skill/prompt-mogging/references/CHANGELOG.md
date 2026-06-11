# Prompt Mogging — CHANGELOG v0.2.3

## v0.2.3 — Dispatcher / Semantic Rule Runtime

**Status:** repo-ready release candidate.  
**Release type:** structural architecture release.

### Why this release exists

v0.1.x improved activation reliability by putting `NATIVE_CORE.md` in primary instructions. Field testing then showed a different problem: technique behavior still under-fired because the long skill text lost salience and technique descriptions underspecified when to fire.

v0.2.3 moves to a dispatcher / semantic-ruleset architecture:

```text
DISPATCHER_STUB.md in platform instructions
+
full SKILL.md loaded and intended to govern
```

### Major changes

- Retired `NATIVE_CORE.md` as active artifact.
- Merged floor semantics into `SKILL.md`.
- Added `DISPATCHER_STUB.md`.
- Defined loaded state: full skill file + activation header/contract + intended to govern.
- Made fragments, quotes, diffs, review pastes, and discussion non-loading.
- Added Trigger Index and `WHEN:` lines.
- Added visible `[pm-*]` activation tags.
- Added tag epistemics: tags are best-effort attribution, not causal proof.
- Added `mog help`, `mog status`, `pm why silent`, and debug controls.
- Added `[pm-diagnostic]` for explicit why-silent diagnostics.
- Added compact memory preference format: `PM_PREF`.
- Added compact recurrence format: `PM_REC`.
- Added lessons-learnt promotion pipeline.
- Hardened Play mode:
  - ordinary “what if” does not enter Play,
  - Play enters only on explicit command directed at skill/mode,
  - `[pm-play]` tags entry/exit only,
  - decision/commitment/launch/spend questions inside Play force rigor split or exit offer.

### Preserved

- Chat-only/no-agent boundary.
- No automatic routing or model switching.
- No hidden background work.
- No executable validation.
- No chain-of-thought exposure.
- Detector-gated optional moves.
- Escalate-DOWN manual catalog only.
- Factuality hygiene + tic guard.

### Changed degradation model

v0.1.x degraded with some floor behavior still in `NATIVE_CORE.md`.

v0.2.3 degrades differently:

- stub + full `SKILL.md` loaded = full PM behavior,
- stub only = inert,
- review/meta paste = not loaded.

This is intentional and documented.

### Required migration

Replace root and dist artifacts:

- `README.md`
- `DISPATCHER_STUB.md`
- `SKILL.md`
- `NATIVE_CORE.md` tombstone
- `ACCEPTANCE_TESTS.md`
- `TUTORIAL.md`
- `PATCH_NOTES.md`
- `BUILD_MANIFEST.md`
- `dist/agent-skill/prompt-mogging/*`
