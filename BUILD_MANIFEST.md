# Prompt Mogging v0.2.3 — Build Manifest

**Build timestamp (UTC):** 2026-06-11T03:00:51Z
**Release:** v0.2.3 — Dispatcher / Semantic Rule Runtime

## Files

- `README.md` — 4827 chars — v0.2.3 stamp: YES — SHA-256: `1c7d1ccf986ca3c1cb2238ec72ffc548cb6e31af6358770a6b1a23061fd345a9`
- `DISPATCHER_STUB.md` — 786 chars — v0.2.3 stamp: YES — SHA-256: `956be21b1a22a10359a0ba1cc1677e5af3e7ebbbfce8b5e22006c85aa48d3618`
- `SKILL.md` — 53032 chars — v0.2.3 stamp: YES — SHA-256: `a458df74cec4e58842a327c276291e95d76e8247b6cb0e94ab56263b237720a1`
- `NATIVE_CORE.md` — 832 chars — v0.2.3 stamp: YES — SHA-256: `e3b7ba28ea44a5e82df840f461a7574cd9c2a7b8b7fb421ce150c2acee067d5a`
- `ACCEPTANCE_TESTS.md` — 8336 chars — v0.2.3 stamp: YES — SHA-256: `3807c33aa386e691e9d573efda5e66b2f459c3e85dd3bd9daf88b231bea22895`
- `TUTORIAL.md` — 3882 chars — v0.2.3 stamp: YES — SHA-256: `99c9fc97654476e08c5e84bac025a1af303c18c3bd75daaeb55d61ff5a253f07`
- `CHANGELOG.md` — 2466 chars — v0.2.3 stamp: YES — SHA-256: `eb0fd04299918cfb3453f65bfdf8eaefb6fc9bff6e12de8714bdeb517eac0acc`
- `PATCH_NOTES.md` — 2496 chars — v0.2.3 stamp: YES — SHA-256: `e7a5fb499fad733f152452143e0e1d2d043d5426de9edf6a1874364c2e677774`
- `CLAUDE_REVIEW_PROMPT_v0_2_3.md` — 2000 chars — v0.2.3 stamp: YES — SHA-256: `a7d5d02425f71c31aa358beaa9be5d55ca222c4de4aa55c97d1f7f03f68a5887`
- `dist/agent-skill/prompt-mogging/SKILL.md` — 1233 chars — v0.2.3 stamp: YES — SHA-256: `5054f591efcc68c8b99f7a7f476ef536383f45d6ddb6b2806e21090dfdc37e66`
- `dist/agent-skill/prompt-mogging/references/FULL_SPEC.md` — 53032 chars — v0.2.3 stamp: YES — SHA-256: `a458df74cec4e58842a327c276291e95d76e8247b6cb0e94ab56263b237720a1`
- `dist/agent-skill/prompt-mogging/references/DISPATCHER_STUB.md` — 786 chars — v0.2.3 stamp: YES — SHA-256: `956be21b1a22a10359a0ba1cc1677e5af3e7ebbbfce8b5e22006c85aa48d3618`
- `dist/agent-skill/prompt-mogging/references/ACCEPTANCE_TESTS.md` — 8336 chars — v0.2.3 stamp: YES — SHA-256: `3807c33aa386e691e9d573efda5e66b2f459c3e85dd3bd9daf88b231bea22895`
- `dist/agent-skill/prompt-mogging/references/CHANGELOG.md` — 2466 chars — v0.2.3 stamp: YES — SHA-256: `eb0fd04299918cfb3453f65bfdf8eaefb6fc9bff6e12de8714bdeb517eac0acc`
- `dist/agent-skill/prompt-mogging/references/NATIVE_CORE.md` — 832 chars — v0.2.3 stamp: YES — SHA-256: `e3b7ba28ea44a5e82df840f461a7574cd9c2a7b8b7fb421ce150c2acee067d5a`

## Authority and sync checks

- `DISPATCHER_STUB.md` is the platform/custom-instructions consult stub.
- `SKILL.md` is the canonical full runtime specification and contains floor semantics.
- `NATIVE_CORE.md` is retired/tombstoned and must not be used as active runtime instructions.
- Stub-only state is inert and reports `not loaded` for `mog status` / `mog help`.
- Fragments, quotes, diffs, review pastes, and discussion are not loading unless explicitly run.
- `TUTORIAL.md` illustrates behavior; `ACCEPTANCE_TESTS.md` adjudicates behavior.
- Dist package is regenerated from root source files.

## Candidate review gates

- Dispatcher stub remains under 600 characters under the stated convention.
- Loaded definition includes intent-to-govern.
- Play ordinary-conversation guard is present.
- Play commitment split is present.
- Tag epistemics are present.
- Debug/diagnostic distinction is present.
- Compact PM_PREF / PM_REC memory discipline is present.
- No active `NATIVE_CORE` runtime instructions remain.
