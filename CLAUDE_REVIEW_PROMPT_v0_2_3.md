# Claude Review Prompt — PROMPT_MOGGING v0.2.3

Review the attached repo patch as a floor-finder, not a taste reviewer.

Primary files:

1. `DISPATCHER_STUB.md`
2. `SKILL.md`
3. `NATIVE_CORE.md`
4. `README.md`
5. `ACCEPTANCE_TESTS.md`
6. `TUTORIAL.md`
7. `BUILD_MANIFEST.md`
8. `CHANGELOG.md`
9. `PATCH_NOTES.md`
10. `dist/agent-skill/prompt-mogging/SKILL.md`
11. `dist/agent-skill/prompt-mogging/references/*`

## Review for blockers

Find any issue where:

1. A fragment, quote, diff, example, full-file review paste, or meta-discussion accidentally loads the skill.
2. Stub-only state produces PROMPT_MOGGING behavior instead of `not loaded`.
3. `mog off`, `skill off`, chill, dials, cooldowns, or suppressions can suppress floor-tier rules while full skill is loaded.
4. Play mode can enter from ordinary conversational “what if/play/riff.”
5. Play mode can answer a decision/commitment/launch/spend question without rigor split or exit offer.
6. `[pm-play]` can tag every Play-mode turn.
7. `NATIVE_CORE.md` still contains active runtime instructions.
8. Dispatcher contains floor content or technique-selection logic.
9. Tags overclaim causal effect.
10. Tag dial semantics are undefined.
11. Debug/status leaks hidden chain-of-thought or private reasoning.
12. Memory stores raw traces, debug logs, private reasoning, did-it-help signals, or temporary task state.
13. Optional moves lack detector/silence/cooldown/Love/Loathe/did-it-help.
14. Escalate-DOWN can fire from confidence rather than manual catalog.
15. Agentic behavior creeps in: routing, execution, validation, backend state, hidden work.
16. README/TUTORIAL/ACCEPTANCE_TESTS/dist still reference the old active `NATIVE_CORE` architecture.
17. Version stamps or manifest hashes are stale.
18. Change log claims edits not present in draft.

## Expected output

Return:

- Verdict: PASS / PASS WITH FIXES / FAIL
- Blockers
- Defects
- Non-blocking improvements
- Specific section-level fixes
- Any change-log or manifest overclaims
