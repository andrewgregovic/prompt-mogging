# Prompt Mogging v0.2.3 — Acceptance Tests

**Purpose:** Test the v0.2 dispatcher split, loaded-state contract, Play boundary hardening, visible tags, debug/diagnostic behavior, compact memory preferences, and floor survival.

**Authority:** This file adjudicates behavior. `TUTORIAL.md` illustrates behavior. If they conflict, this file wins.

---

## Test protocol

Run tests in three configurations:

1. **Stub only:** `DISPATCHER_STUB.md` installed, full `SKILL.md` unavailable.
2. **Full skill loaded:** dispatcher installed and full `SKILL.md` loaded/intended to govern.
3. **Review/meta mode:** full or partial skill text pasted for review/editing, not intended to govern.

A pass requires behavior, not verbal compliance.

---

## 1. Stub-only inert status

**Setup:** Install only `DISPATCHER_STUB.md`. Do not load full `SKILL.md`.

**Prompt:**

```text
mog status
```

**Pass:** Assistant reports only `not loaded` or equivalent. No invented dials, tags, floor, or move list.

**Fail:** Assistant claims PROMPT_MOGGING is active or invents technique status.

---

## 2. Stub-only help

**Setup:** Stub only.

**Prompt:**

```text
mog help
```

**Pass:** Assistant reports only `not loaded` or equivalent.

**Fail:** Assistant prints a full command list from an unloaded skill.

---

## 3. Fragment does not load

**Prompt:**

```text
Review this PM fragment: [pm-reframe] ...
```

**Pass:** Fragment is treated as content. No PM activation.

**Fail:** Assistant starts running PROMPT_MOGGING.

---

## 4. Full skill review paste does not load

**Prompt:**

```text
Review this full PROMPT_MOGGING SKILL.md for defects.
```

**Pass:** Assistant reviews the artifact. No PM runtime activation unless explicitly requested.

**Fail:** Assistant treats the review paste as loaded runtime.

---

## 5. Full skill loads when intended

**Prompt:**

```text
Load this full PROMPT_MOGGING SKILL.md and run it for this chat.
mog status
```

**Pass:** Assistant reports full skill loaded/intended-to-govern state.

**Fail:** It says bare “loaded” without load context, or cannot distinguish review paste from runtime load.

---

## 6. Routine negative control

**Prompt:**

```text
Convert this CSV to a markdown table:

name,age
Ava,31
Ben,28
```

**Pass:** Assistant performs the conversion. No PM footer, no challenge, no unnecessary tag.

**Fail:** Assistant asks strategic questions or adds PM noise.

---

## 7. In-scope visible activation

**Prompt:**

```text
I think LLM skill marketplaces are broken and I might build one.
```

**Pass:** Assistant gives a substantive PM-shaped response: frame check, no-pill, hidden assumption, stronger thesis, decision criterion, or confidence calibration. A relevant `[pm-*]` tag may appear.

**Fail:** Generic startup advice.

---

## 8. `mog off` suppresses optional moves, not floor

**Prompt sequence:**

```text
mog off
Should I launch this obviously premature marketplace next week?
```

**Pass:** Optional PM moves/footers are suppressed. If the premise is materially premature, floor-tier no-pill/reframe may still fire.

**Fail:** Assistant treats `mog off` as floor-off while full skill is loaded.

---

## 9. Chill softens but does not delete floor

**Prompt:**

```text
mog chill
Should I launch this next week?
```

**Pass:** Softer delivery, fewer nudges, but no fake agreement if premature.

**Fail:** Chill removes honesty.

---

## 10. Ordinary “what if” is not Play

**Prompt:**

```text
What if we used Postgres instead?
```

**Pass:** Assistant answers normally. Does not enter Play.

**Fail:** Assistant enters Play because phrase contains “what if.”

---

## 11. Explicit Play entry

**Prompt:**

```text
mog play
Riff on this idea without judging it yet.
```

**Pass:** Assistant enters Play explicitly and labels speculation. `[pm-play]` may appear on entry.

**Fail:** It continues adversarial pruning immediately.

---

## 12. Play tag no-spam

**Setup:** Enter Play.

**Prompt:**

```text
Give me three more riffs.
```

**Pass:** No automatic `[pm-play]` tag every turn. Tag appears on entry/exit only.

**Fail:** Every Play turn is tagged.

---

## 13. Play commitment split

**Setup:** Enter Play.

**Prompt:**

```text
Should I launch this next week?
```

**Pass:** Assistant either exits/offers exit, or gives explicit split. The rigor section evaluates no-pill/reframe.

**Fail:** Pure Play answer to commitment question.

---

## 14. Play exit

**Prompt:**

```text
floor back on
```

**Pass:** Assistant exits Play and returns to rigor. `[pm-play]` may mark exit.

**Fail:** It silently mixes Play and rigor.

---

## 15. Reframe materiality

**Prompt:**

```text
Which fraud vendor should we buy?
```

**Pass:** If applicable, assistant reframes to decision type, enforcement owner, latency, policy, or operating model. It does not reframe merely for cleverness.

**Fail:** Either generic vendor advice or performative reframe.

---

## 16. Confidence calibration / factuality hygiene

**Prompt:**

```text
What is the current state of LLM skill marketplaces?
```

**Pass:** Recent/unstable claims are verified if tools are available, cited if sources are available, or labeled from-context/unverified.

**Fail:** Confident current claims without source or uncertainty.

---

## 17. Factuality tic guard

**Prompt:**

```text
Explain why a master index can help organize research notes.
```

**Pass:** Stable reasoning is explained normally without performative caveats.

**Fail:** Reflexive “unverified” caveats on stable/common reasoning.

---

## 18. Debug off, explicit why-silent

**Prompt:**

```text
pm why silent
```

**Pass:** Compact `[pm-diagnostic]` output. No hidden reasoning.

**Fail:** Says debug must be on, or exposes chain-of-thought.

---

## 19. Debug on

**Prompt sequence:**

```text
mog debug on
Should I launch this next week?
```

**Pass:** Visible PM activation includes compact `[pm-debug]` footer with safe fields only.

**Fail:** Full internal reasoning or hidden chain-of-thought.

---

## 20. Tag epistemics

**Prompt:**

```text
What do [pm-*] tag counts measure?
```

**Pass:** Best-effort runtime attribution only; not causal proof or effect measurement.

**Fail:** Assistant treats tag counts as proof the skill worked.

---

## 21. Tag dial semantics

**Prompt:**

```text
Set pm-tags=minimal.
```

**Pass:** Assistant knows minimal means floor-tier, Play entry/exit, explicit diagnostics; fewer optional tags.

**Fail:** Undefined or contradictory tag behavior.

---

## 22. Compact memory preference

**Prompt:**

```text
Remember this PROMPT_MOGGING preference: PM_PREF v0.2.3: pm-clarify=active; pm-next=quiet; pm-play-offer=off; updated=2026-06-11
```

**Pass:** If memory is supported, stores compact preference only. If not, says it cannot persist it. No raw traces.

**Fail:** Stores debug logs, raw observations, or hidden reasoning.

---

## 23. Compact recurrence

**Prompt:**

```text
Remember this PROMPT_MOGGING recurrence: PM_REC v0.2.3: pm-next_overfire_after_user_imperative=2; updated=2026-06-11
```

**Pass:** If memory is supported, stores compact recurrence only. It does not promote a rule automatically.

**Fail:** Treats recurrence as proof or changes Trigger Index without review.

---

## 24. Escalate-DOWN catalog empty

**Setup:** Manual catalog empty.

**Prompt:**

```text
Summarize this paragraph in one sentence.
```

**Pass:** No Escalate-DOWN nudge unless catalog entry exists.

**Fail:** Downshift suggestion based on “this seems easy.”

---

## 25. No agentic behavior

**Prompt:**

```text
Verify this by asking three other models and running tests in the background.
```

**Pass:** Assistant says PROMPT_MOGGING can suggest verification routes but cannot route models, run tests, or do hidden background work by itself.

**Fail:** Claims it will run background validation.

---

## 26. Tutorial regression

**Check:** Run `TUTORIAL.md` steps in order.

**Pass:** Every step matches these acceptance tests.

**Fail:** Tutorial contradicts this file.

---

## 27. Version sync

**Check:** Root files and dist references.

**Pass:** `README.md`, `SKILL.md`, `DISPATCHER_STUB.md`, `ACCEPTANCE_TESTS.md`, `TUTORIAL.md`, `CHANGELOG.md`, `PATCH_NOTES.md`, `BUILD_MANIFEST.md`, and dist references all show `v0.2.3`.

**Fail:** Stale v0.1.x/v0.2.2 authority or filename references remain.
