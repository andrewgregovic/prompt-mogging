# Prompt Mogging v0.1.5 — Patch Notes

## Release name

v0.1.5 — Factuality Hygiene + Controls

## Baseline

Built v0.1.4 release pack.

## Patch purpose

v0.1.4 made Prompt Mogging reliably active. v0.1.5 adds a factuality floor for recent/unstable load-bearing claims, namespaces controls for multi-skill environments, and turns the validation flow into a user-facing tutorial.

## Patch 1 — Factuality hygiene

Add to `NATIVE_CORE.md` honest/factuality floor and to `SKILL.md §5`:

```text
A recent or temporally unstable factual claim that is load-bearing for the answer — including claims about current markets, pricing, platform capabilities, policies, studies, availability, or ecosystem conditions — must be cited if a source is at hand, verified if the host can browse, or else labeled “unverified / from context.”

Adversarial-but-constructive confidence is not authority.

This skill cannot browse by itself. Where verification is not available in the host, the required behavior is the honest label, not a claim of having checked.

The caveat is warranted only when the claim is genuinely recent/unstable and material to the answer. Do not reflexively caveat stable or non-load-bearing facts.
```

## Patch 2 — Namespaced controls

Canonical:

```text
prompt mogging on
prompt mogging off
mog on
mog off
mog chill
mog play
floor back on
```

Legacy/contextual aliases:

```text
skill on / skill off
play / riff / what-if / chill / ease up / simple mode
```

Clarification:

```text
mog off and skill off disable Prompt Mogging's behavior only. The base model's own safety and factuality behavior is not part of this skill and is never suppressed by any control.
```

## Patch 3 — Tutorial

Add `TUTORIAL.md` and link it from README.

Tutorial authority rule:

```text
TUTORIAL.md illustrates behavior; ACCEPTANCE_TESTS.md adjudicates behavior. If they conflict, ACCEPTANCE_TESTS.md wins.
```

## Patch 4 — Acceptance tests

Add tests for:

- factuality hygiene
- factuality tic / over-caveating
- namespaced controls
- legacy alias behavior
- multi-skill ambiguity
- mog-off floor survival
- tutorial as regression
- tutorial/test authority

## Non-goals

- No new Prompt Mogging move.
- No agentic tooling.
- No browsing assumption.
- No removal of v0.1.4 activation reliability.
- No change to Play being opt-in.
