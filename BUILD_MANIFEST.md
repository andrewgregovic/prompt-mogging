# Prompt Mogging v0.1.5 Build Manifest

**Build timestamp (UTC):** 2026-06-05T06:19:33Z

**Release:** v0.1.5 — Factuality Hygiene + Controls

## Files

- `SKILL.md` — 52712 chars — v0.1.5 stamp: YES — SHA-256: `dd332682fbe37c58460227fb5dc1316a406585f19368e5ec0d781a505956fdcc`
- `NATIVE_CORE.md` — 6631 chars — v0.1.5 stamp: YES — SHA-256: `02f526814d9f6a00759fbdf7a7954ec4075c6f895f1a09ccaf36423d820380ce`
- `ACCEPTANCE_TESTS.md` — 10648 chars — v0.1.5 stamp: YES — SHA-256: `47f2c9b68fd166565914dd58ad3db338cfc61af83a3630404d7c39960417ce98`
- `TUTORIAL.md` — 3448 chars — v0.1.5 stamp: YES — SHA-256: `193791225c0df892e03768a4959611090bead584322eeb73a55b76760d061e3a`
- `CHANGELOG.md` — 2245 chars — v0.1.5 stamp: YES — SHA-256: `307da4e424dd858665543098f3fa779983b45a3758a441384a82b46305e45889`
- `PATCH_NOTES.md` — 2327 chars — v0.1.5 stamp: YES — SHA-256: `4f3750ca8e8b5a13d38c62b2f838a6d8a9a1d175f29e8a9c4c52980b57d6c4a3`
- `README.md` — 2384 chars — v0.1.5 stamp: YES — SHA-256: `f8caa36bdf4c76b5283bd15eeb21b49f0a62a2c0987b68dd8a29cde41b2a3933`

## Authority and sync checks

- `NATIVE_CORE.md` is the always-in-context activation core.
- `SKILL.md` is the full canonical reference.
- If they conflict on activation behavior, `NATIVE_CORE.md` wins at runtime and the version must be resynced before release.
- `TUTORIAL.md` illustrates behavior; `ACCEPTANCE_TESTS.md` adjudicates behavior.

## Candidate review gates

- Factuality floor present in both native core and full skill.
- Namespaced controls present in native core and full skill.
- `mog off` / legacy `skill off` never disable base-model safety/factuality.
- Tutorial linked and authority rule present.
- Acceptance tests include factuality hygiene, factuality tic, and control namespace tests.
- Native core stays under 7,000 chars.
