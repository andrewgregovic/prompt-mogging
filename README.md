# Prompt Mogging

A portable chat skill that puts the model into an **adversarial-but-constructive** stance for exploratory, strategic, and framing work — so "skill on" actually changes how the model answers, instead of silently falling back to generic assistant prose.

Works with Custom GPTs, Claude Projects/Skills, and any chat context that supports custom instructions plus reference knowledge.

## The problem this solves

You load a "thinking partner" skill or system prompt. The model says it's loaded. Then you ask a real question and get the same hedged, agreeable, frame-preserving answer it would have given without the skill. There is no visible behavioral delta — the skill is loaded in name only.

Prompt Mogging fixes this by:

- Defaulting in-scope answers to **adversarial-but-constructive** (challenge weak frames, hidden assumptions, premature conclusions — while strengthening the user's best version).
- Requiring a **visible delta** on substantial in-scope answers: at least one integrated move (frame check, hidden-assumption surfacing, stronger-claim rewrite, calibrated uncertainty, no-pill / not-yet).
- Putting activation-critical rules in an always-in-context **NATIVE_CORE** rather than relying on retrieval, which can silently fail.
- Forbidding **manufactured challenge** — fake-adversarial is as dishonest as fake-agreeable. If nothing's wrong, the skill says so explicitly.

## Quick start

Two artifacts, two places:

1. **`NATIVE_CORE.md`** → paste into your platform's custom/native instructions field (Custom GPT instructions, Claude Project instructions, etc.). This is the always-in-context activation core.
2. **`SKILL.md`** → attach as knowledge / reference (Custom GPT knowledge files, Claude Project knowledge). This is the full canonical spec the model consults for detail.

Do not rely on `SKILL.md` retrieval alone for activation. If the activation rules are only in retrievable knowledge, the skill can be "loaded" without ever firing.

## Manual controls

- `skill off` / `drop the skill` — hard dormant for the session.
- `skill on` — resume.
- `chill` / `ease up` / `simple mode` — soft suppression: keeps the honest floor and safety, drops adversarial push and footer offers.
- `play` / `riff` / `what-if` — opt-in Play mode: divergence and speculation, honest spine still on.

Full control surface and detector behavior in [SKILL.md](SKILL.md).

## What's in this repo

- [`SKILL.md`](SKILL.md) — canonical full specification (v0.1.4).
- [`NATIVE_CORE.md`](NATIVE_CORE.md) — always-in-context activation core. Paste target for native instructions.
- [`ACCEPTANCE_TESTS.md`](ACCEPTANCE_TESTS.md) — runnable checklist for activation reliability, no-nagware behavior, manufactured-challenge risk, and drift.
- [`CHANGELOG.md`](CHANGELOG.md) — release notes.
- [`PATCH_NOTES.md`](PATCH_NOTES.md) — patch rationale and insertion map (audit trail).
- [`BUILD_MANIFEST.md`](BUILD_MANIFEST.md) — build contents and version sync status.

## Authority rule

If `SKILL.md` and `NATIVE_CORE.md` conflict on activation behavior, `NATIVE_CORE.md` wins at runtime and the version must be resynced before release.

## Build and validation

`NATIVE_CORE.md` goes into Custom GPT Instructions, native Skill instructions, Project instructions, or the equivalent always-in-context instruction field. `SKILL.md` goes into Knowledge/reference as the full canonical specification.

Do not rely on Knowledge/RAG alone for activation-critical behavior. Retrieved knowledge can be missed or decay across a long session, so the native core carries the behavior that must fire every turn.

Run validation before tagging a release:

```bash
python scripts/validate_release.py
python scripts/build_release.py
python scripts/build_agent_skill.py
```

`build_release.py` regenerates `BUILD_MANIFEST.md` and creates `Prompt_Mogging_<version>_Release_Pack.zip`. `build_agent_skill.py` creates `dist/agent-skill/prompt-mogging/` for Agent Skills / Codex Skills discovery.

Updating the Custom GPT UI remains manual unless/until OpenAI exposes an official GPT configuration API, or the user is using a supported Skills upload flow.

## Status

**v0.1.4 — Activation Reliability Patch.** Built, version-synced, acceptance tests included. See [CHANGELOG.md](CHANGELOG.md) for the v0.1.3 → v0.1.4 delta.

## License

See [LICENSE](LICENSE).
