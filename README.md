# PROMPT_MOGGING

A loadable chat skill that turns an AI assistant into a sharper thinking partner for open-ended work — and is honest enough to tell you when not to use it.

> Status: **v0.2.3 — dispatcher / semantic-rule-runtime release.**
>
> New in v0.2.3: `NATIVE_CORE.md` is retired. Use `DISPATCHER_STUB.md` in platform instructions and load the full `SKILL.md` as the governing skill file.

PROMPT_MOGGING is not a tone preset. It is a chat-native semantic rule runtime: a thin dispatcher silently consults the full skill, and the skill decides whether to stay dormant, fire a floor rule, offer a move, enter Play, tag a visible activation, or show a compact diagnostic.

---

## What this is

PROMPT_MOGGING is a set of instructions you load into an AI chat assistant such as Claude, a Custom GPT, or an equivalent host.

It does not add tools. It changes conversational behavior for thinking-shaped work:

- frame checks,
- no-pill / not-yet calls,
- confidence calibration,
- stronger review suggestions,
- clarifying questions,
- handoffs and lessons,
- Play mode for exploratory riffing,
- compact debug / status diagnostics.

It remains a chat skill, not an agent. It does not run code, browse, switch models, validate claims, or do background work by itself.

---

## What changed from v0.1.x

v0.1.x used:

```text
NATIVE_CORE.md in platform instructions + SKILL.md as knowledge/reference
```

v0.2.3 uses:

```text
DISPATCHER_STUB.md in platform instructions + full SKILL.md loaded and intended to govern
```

`NATIVE_CORE.md` is now a tombstone. Its floor semantics are merged into `SKILL.md`.

This is a deliberate trade-off:

- stub + full `SKILL.md` loaded = full PROMPT_MOGGING behavior,
- stub only = inert, no PROMPT_MOGGING floor or techniques,
- fragments / quotes / review pastes = not loaded.

---

## What it is for

Use PROMPT_MOGGING for:

- product / strategy thinking,
- research framing,
- ambiguous decisions,
- architecture / design review,
- learning and model-building,
- diagnosis,
- long-context handoffs,
- high-stakes claims that need calibration.

Skip it for:

- formatting,
- extraction,
- simple rewriting,
- closed-form lookup,
- mechanical conversion,
- routine execution.

On routine tasks, optional PM moves should stay silent. Floor-tier rules still evaluate if materially triggered while the full skill is loaded.

---

## Install / load

### ChatGPT Custom GPT

1. Paste `DISPATCHER_STUB.md` into the GPT Instructions field.
2. Upload the full `SKILL.md` as Knowledge.
3. In usage, ensure the full skill is intended to govern the conversation.
4. Run `mog status` or `mog help`.

### Claude Project

1. Paste `DISPATCHER_STUB.md` into Project custom instructions.
2. Add the full `SKILL.md` to Project knowledge.
3. Use the project for thinking-shaped work.
4. Run `mog status` or `mog help`.

### Paste-load for testing

Paste the full `SKILL.md` and explicitly say it should govern the conversation, for example:

```text
Load this full PROMPT_MOGGING SKILL.md and run it for this chat.
```

A fragment, quotation, diff, or full-file review paste does **not** load the skill. If you are asking a model to edit/review `SKILL.md`, it should treat the skill as the object under review unless you explicitly say to run it.

---

## Controls

```text
mog help          # compact command list
mog status        # load/mode/dial/debug/tag status
mog on            # resume PM runtime if full skill is loaded
mog off           # suppress optional/non-floor PM behavior
mog chill         # softer mode; fewer nudges, less adversarial push
mog play          # enter Play mode explicitly
floor back on     # exit Play and return to rigor
mog debug on/off  # show/hide compact [pm-debug] traces
pm why silent     # explain why no PM move fired
```

Important: `mog off` suppresses optional/non-floor PM behavior. It does **not** suppress floor-tier rules while the full skill remains loaded.

---

## Visible tags

When PROMPT_MOGGING materially shapes the visible response, it may prefix the relevant section with a tag such as:

```text
[pm-nopill]
[pm-reframe]
[pm-confidence]
[pm-clarify]
[pm-up-verify]
[pm-play]
```

Tags are best-effort runtime attribution, not causal proof. Tag counts are not effect measurements.

---

## Authority

- `SKILL.md` is the canonical runtime spec.
- `DISPATCHER_STUB.md` is the platform-layer wake/consult stub.
- `ACCEPTANCE_TESTS.md` adjudicates behavior.
- `TUTORIAL.md` illustrates behavior and must defer to `ACCEPTANCE_TESTS.md`.
- `NATIVE_CORE.md` is retired/tombstoned.

---

## Dist package

The agent-skill distribution lives at:

```text
dist/agent-skill/prompt-mogging/
```

It contains a skill-wrapper `SKILL.md` and reference copies of the full spec, acceptance tests, changelog, and dispatcher stub.

---

## License

Apache-2.0.
