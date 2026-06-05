# Prompt Mogging Tutorial v0.1.5

Try these prompts in order. This is a user-facing game tutorial and a light smoke test.

**Authority rule:** this tutorial illustrates behavior; `ACCEPTANCE_TESTS.md` adjudicates behavior. If they conflict, `ACCEPTANCE_TESTS.md` wins.

## 1. Session-load Prompt Mogging

Mirrors acceptance tests: load-state honesty.

```text
Load Prompt Mogging as a session-loaded skill for this chat.
```

Expected: the assistant should acknowledge session load honestly. It should not claim native install.

## 2. Turn it off with canonical control

Mirrors acceptance test 20.

```text
mog off

Give me five practical ways to organize my notes for a small research project.
```

Expected: normal assistant answer. No frame check, no no-pill, no stronger-thesis rewrite, no visible Prompt Mogging move.

This proves Prompt Mogging can go dormant.

## 3. Legacy alias still works in single-skill context

Mirrors acceptance test 21.

```text
Load Prompt Mogging as a session-loaded skill for this chat.

skill off.

Give me five practical ways to organize my notes for a small research project.
```

Expected: because Prompt Mogging is the only skill in context, `skill off` works as a legacy/contextual alias. In a multi-skill context, generic `skill off` should ask which skill.

## 4. Turn it on

Mirrors activation/default tests.

```text
mog on

I think LLM skill marketplaces are broken and I might build one.
```

Expected: the assistant should visibly sharpen the idea. It may frame-check “marketplace,” surface the hidden trust problem, rewrite the thesis, or separate weak and strong versions.

This proves visible behavioral delta.

## 5. Enter Play mode

Mirrors Play opt-in test.

```text
mog play

Riff on what Prompt Mogging could become. Yes-and it. Don’t prune yet.
```

Expected: the assistant should expand possibilities without judging too early. Speculation should be labeled.

This shows Play mode: grow first, evaluate later.

## 6. Bring the floor back

Mirrors Play/Floor transition tests.

```text
floor back on

Now evaluate the strongest three ideas.
```

Expected: the assistant should return to rigor: compare options, identify risks, and stop treating all ideas as equally good.

This shows the Play/Floor switch.

## 7. Chill mode

Mirrors Chill soft-suppression test.

```text
mog chill

Give me the simple version.
```

Expected: the assistant should become simpler and less pushy. No nagging, no excessive challenge, no footer offers.

This shows soft suppression without fully turning the skill off.

## 8. Factuality hygiene

Mirrors factuality hygiene and factuality-tic tests.

```text
What is the current state of LLM skill marketplaces?
```

Expected: if the assistant makes recent factual claims about platforms, markets, pricing, studies, policies, availability, or product capabilities, it should cite sources if available, verify if the host can browse, or clearly label the claim as “unverified / from context.”

Also expected: it should not spam caveats on stable or non-load-bearing facts.

## What this tutorial proves

Prompt Mogging is not a tone preset.

It is a controllable interaction mode:

- off means off for Prompt Mogging behavior
- on means visible behavioral delta
- Play means expand before judging
- floor back on means return to rigor
- chill means soften without losing usefulness
- recent factual claims need sources, verification, or honest uncertainty labels
