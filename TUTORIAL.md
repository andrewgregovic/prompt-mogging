# Prompt Mogging Tutorial v0.2.3

Try these prompts in order.

This is a user-facing tutorial and light smoke test. It illustrates behavior; `ACCEPTANCE_TESTS.md` adjudicates behavior. If they conflict, `ACCEPTANCE_TESTS.md` wins.

---

## 1. Stub-only is inert

Use a host where only `DISPATCHER_STUB.md` is installed and the full `SKILL.md` is not loaded.

```text
mog status
```

Expected:

```text
not loaded
```

No technique list, no invented status, no floor claim.

---

## 2. Full skill review paste is not loading

```text
Review this full PROMPT_MOGGING SKILL.md for defects.
```

Expected: the assistant treats the skill as an artifact under review. It does not start emitting `[pm-*]` tags or running PM unless explicitly told to run it.

---

## 3. Load the full skill intentionally

```text
Load this full PROMPT_MOGGING SKILL.md and run it for this chat.
mog status
```

Expected: the assistant reports loaded state, mode, tags/debug settings, and any known dials. It should not reveal hidden reasoning.

---

## 4. Routine task stays quiet

```text
Convert this CSV to a markdown table:

name,age
Ava,31
Ben,28
```

Expected: normal table conversion. No PM footer. No unnecessary challenge. No `[pm-*]` tag unless a floor-tier issue is materially triggered.

---

## 5. In-scope prompt activates visibly

```text
I think LLM skill marketplaces are broken and I might build one.
```

Expected: at least one integrated PM move, likely a frame check or no-pill. It may tag the visible move, for example `[pm-reframe]` or `[pm-nopill]`.

---

## 6. `mog off` suppresses optional moves, not the floor

```text
mog off

Should I launch this marketplace next week?
```

Expected: optional PM moves and footer nudges are suppressed. But if the premise is premature, a floor-tier rule may still fire, for example `[pm-nopill] Not yet...`

---

## 7. Ordinary “what if” is not Play

```text
What if we used Postgres instead?
```

Expected: normal answer. It should not enter Play merely because the phrase contains “what if.”

---

## 8. Enter Play explicitly

```text
mog play

Riff on what Prompt Mogging could become. Yes-and it. Don’t prune yet.
```

Expected: `[pm-play]` appears on entry. The assistant explores and labels speculation. It does not score or prune until you exit Play.

---

## 9. Commitment question inside Play forces rigor split

While still in Play:

```text
Should I launch this next week?
```

Expected: the assistant either splits the answer or offers to exit Play. Default is split:

```text
[pm-play] Play answer: ...

[pm-nopill] Rigor split: I would not launch next week because...
```

Play does not suppress no-pill/reframe for commitment questions.

---

## 10. Exit Play

```text
floor back on

Now evaluate the strongest three options.
```

Expected: `[pm-play]` marks exit, then rigor resumes.

---

## 11. Debug and why-silent

```text
pm why silent
```

Expected: compact `[pm-diagnostic]` output, not hidden reasoning.

Then:

```text
mog debug on
```

Expected: future visible PM activations include compact `[pm-debug]` footers.

---

## 12. Memory preferences

```text
Remember this PROMPT_MOGGING preference: PM_PREF v0.2.3: pm-clarify=active; pm-next=quiet; pm-play-offer=off; updated=2026-06-11
```

Expected: if host memory supports it, the assistant stores a compact preference. It must not store raw traces, debug logs, hidden reasoning, or temporary task state.

---

## What this tutorial proves

- Stub-only is inert.
- Full skill must be loaded and intended to govern.
- Review pastes do not activate PM.
- Routine tasks stay quiet.
- In-scope work gets visible behavioral delta.
- `mog off` does not suppress floor-tier rules.
- Play is explicit only.
- Play cannot bypass no-pill/reframe for commitment questions.
- Debug/status are compact and do not reveal hidden reasoning.
- Memory stores compact preferences only.
