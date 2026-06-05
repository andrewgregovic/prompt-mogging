# Prompt Mogging v0.1.4 Built Release Pack

This pack contains a built, version-synced v0.1.4 release of Prompt Mogging.

## Files

- `SKILL.md` — full canonical v0.1.4 specification, patched from v0.1.3.
- `NATIVE_CORE.md` — paste this into native GPT / Skill / Project instructions. This is the always-in-context activation core.
- `ACCEPTANCE_TESTS.md` — runnable checklist for activation reliability, no-nagware behavior, manufactured-challenge risk, and drift.
- `CHANGELOG.md` — release notes.
- `PATCH_NOTES.md` — patch rationale and insertion map retained for audit/traceability.

## Packaging model

Use two artifacts:

1. `NATIVE_CORE.md` in primary/native instructions.
2. Full `SKILL.md` as knowledge/reference.

Do not rely on full `SKILL.md` retrieval for activation-critical behavior. Retrieval can fail or be skipped on a given turn.

## Platform sizing note

`NATIVE_CORE.md` is the paste target for native/custom instructions. It is intentionally much smaller than the full skill. Custom GPT instructions are the cleaner native home because the field is dedicated. Claude Project custom instructions share space with project-specific instructions; if a project is already near the cap, trim project-specific prose rather than moving activation rules into retrieval-only knowledge.

## Authority rule

`SKILL.md` is the canonical full specification. `NATIVE_CORE.md` is the canonical always-in-context activation core for native GPT / Skill / Project instructions. If they conflict on activation behavior, `NATIVE_CORE.md` wins at runtime and the version must be resynced before release.

## Build status

This pack closes the candidate-pack blocker: the full `SKILL.md` is now v0.1.4 and no longer contradicts the native core on Balanced default, visible-delta, or `chill` semantics.

Run `ACCEPTANCE_TESTS.md` before publishing.
