# Prompt Mogging — NATIVE_CORE.md retired as of v0.2.3

`NATIVE_CORE.md` is no longer the activation core.

As of v0.2.3, the v0.1.x `NATIVE_CORE` semantics are merged into `SKILL.md`. The platform/custom-instructions layer should contain only `DISPATCHER_STUB.md`.

## Current artifact graph

- `DISPATCHER_STUB.md` — high-salience consult stub for platform/custom instructions.
- `SKILL.md` — full PROMPT_MOGGING semantic rule runtime, including floor semantics.
- `NATIVE_CORE.md` — tombstone only; do not paste as runtime instructions.

## Important behavior

Stub-only state is inert. If `DISPATCHER_STUB.md` is installed but the full `SKILL.md` is not loaded and intended to govern, PROMPT_MOGGING has no floor and no techniques.

Base assistant safety and factuality behavior still continue, but they are not PROMPT_MOGGING.
