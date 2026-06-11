---
name: prompt-mogging
description: Chat-native semantic rule runtime for exploratory, strategic, diagnostic, ideation, learning, research, model-building, and framing conversations where the user benefits from constructive challenge, confidence calibration, or sharper decision framing.
---

# Prompt Mogging agent-skill wrapper v0.2.3

Use this skill when the user is doing exploratory, strategic, diagnostic, ideation, learning, research, model-building, or framing work.

Do not use it for routine execution, extraction, formatting, simple rewriting under clear constraints, mechanical conversion, or closed-form lookup.

This dist package mirrors the repository release:

- Full canonical spec: `references/FULL_SPEC.md`
- Dispatcher stub for platform/custom instructions: `references/DISPATCHER_STUB.md`
- Acceptance tests: `references/ACCEPTANCE_TESTS.md`
- Changelog: `references/CHANGELOG.md`

## Runtime note

`NATIVE_CORE.md` is retired as of v0.2.3. The full skill spec contains the floor semantics. The dispatcher stub is consult-only and contains no floor.

If this agent-skill package is loaded as a full skill by a host that reads this `SKILL.md`, apply the full runtime specification in `references/FULL_SPEC.md`.
