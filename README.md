# PROMPT_MOGGING

*A loadable chat skill that turns an AI assistant into a sharper thinking partner for open-ended work — and is honest enough to tell you when not to use it.*

**Prompt Mogging is not a tone preset. It's a controllable interaction mode — a behavioral QA layer you switch on for thinking-shaped work and off for everything else.**

> **Status:** v0.1.5 — early pilot. Works today; expect rough edges. Feedback wanted — see [Issues](../../issues).
>
> New in v0.1.5: a factuality floor for recent/unstable claims, namespaced controls, and a [`TUTORIAL.md`](./TUTORIAL.md) that doubles as a smoke test.

---

## What this is

PROMPT_MOGGING is a set of instructions you load into an AI chat assistant (Claude, a custom GPT, or any equivalent). It doesn't bolt features onto the model — it changes how the assistant *behaves* in exploratory conversations. It asks the questions a good collaborator would ask, pushes back when your question is aimed at the wrong target, tells you when it's uncertain instead of bluffing, and points at where to go next.

It exists because experienced users already do these things by hand — they interrogate their own prompts, ask for a second opinion, reframe the problem before answering it. Most people don't, and don't know they're allowed to. This skill runs those moves for you, so you get power-user-grade conversation without learning the tricks.

It is a **chat skill, not an agent.** It talks. It does not run code, browse, switch models, or do anything behind your back. Everything it does happens in the reply you can read.

## What it's for — and what it isn't

**Use it for** thinking-shaped work: exploring a problem, framing a decision, learning something new, diagnosing what's wrong, working out what you don't yet know.

**Skip it for** routine execution: reformatting, extraction, lookups, mechanical edits. On those it's built to stay out of the way and let the assistant just do the task. Load it for that kind of work and it'll say so and stand down rather than clutter the answer.

## It's opinionated on purpose

Read this part before you decide whether you'll like it.

PROMPT_MOGGING will sometimes **not** just do what you asked. It may say "not yet," or "that's the wrong question," or reframe your request, or tell you the honest answer is "it depends, and here's why." That isn't a malfunction — it's the point. An assistant that only ever agrees with you is the exact failure this is built to avoid.

If you don't want that for a given session — if you want straight compliance — turn it off:

```
mog off            # stand down for the session (alias: skill off, in PM context)
mog chill          # soften: stop pushing, keep the honesty floor
mog on             # bring it back
```

The off switch is real and immediate. You are never trapped in it.

## What it actually does

These appear only when they're relevant — usually as a one-line, ignorable footer with a quick **Yes / No / Love it / Loathe it** so it learns your taste for the session. They don't fire every turn, and declining one quiets it.

| Move | What it does |
|---|---|
| **Clarify first** | When your request is vague, offers the 2–5 questions worth answering before it guesses. |
| **Frame check** | When answering as asked would send you down the wrong path, names the better question. Challenges once — if you keep your framing, it drops it. |
| **Uncertainty, stated** | Flags what it doesn't know instead of sounding confident anyway. |
| **Next steps, scored** | After a chunk of thinking, offers a few ranked ways forward. |
| **Stronger review** | For high-stakes or checkable claims, suggests a second opinion, a stronger model, or how to verify — and if two sources disagree, treats the disagreement as the signal. |
| **Simpler route** | If a task is the kind a cheaper or simpler tool handles fine, says so. |
| **Play mode** | An explicit "let's just riff" gear where it stops judging and helps you generate. Enter with `play` or `riff`; leave when you want it critical again. |
| **Challenge level / role** | Set how hard it pushes (gentle coach → blunt reviewer), or have it take a specific lens (skeptical CFO, confused newcomer, and so on). |

## How to use it

The skill ships as **two files** for a reason:

- [`NATIVE_CORE.md`](./NATIVE_CORE.md) (~7,000 characters) — the activation core. This must sit in the assistant's **instructions** so it's reliably present every turn.
- [`SKILL.md`](./SKILL.md) (~53,000 characters) — the full specification. This goes in **knowledge/reference**, consulted as needed.

The split exists because activation rules can't depend on retrieval: if the whole skill lives only in a knowledge file, the assistant may not pull it into a given turn and silently reverts to generic mode. The core in the instructions box prevents that; the full file supplies the detail.

**Claude — recommended, persists across chats**

1. Create a Project (Claude Pro or Team).
2. Paste the contents of `NATIVE_CORE.md` into the project's **Custom instructions** box.
3. Upload `SKILL.md` to the project's **Knowledge**.
4. Every chat in the project now runs the skill. (The core is ~7k and the instructions box caps near 8k, so it fits — but the box is shared with any instructions of your own, so you'll have little spare room.)

**Custom GPT**

1. In the GPT editor, open the **Configure** tab.
2. Paste the contents of `NATIVE_CORE.md` into the **Instructions** field.
3. Upload `SKILL.md` under **Knowledge**.
4. Save. (The Instructions field is dedicated here, so the core fits comfortably — Custom GPT is the cleaner native home.)

**Any chat, zero setup — Claude, ChatGPT, or other**

Paste `NATIVE_CORE.md` at the top of a new conversation (add `SKILL.md` after it if you want the full detail). Works immediately but doesn't carry over — re-paste for each new chat. Best for trying the skill before committing to a Project or GPT.

**Loading the skill (paste method specifics)**

When you paste `SKILL.md` into a fresh chat with nothing else, the assistant will guess at intent — usually by producing an unsolicited review or analysis of the file. That isn't the skill misbehaving; it's the model trying to be helpful with the only signal it has. Two reliable patterns avoid it:

- **Paste, then task on the next line.** Drop in `SKILL.md`, hit return, and write your actual task underneath. The task is the signal that the file is context, not the request.
- **Paste, then explicit hold.** If you want to load now and ask later, end the paste with this line on its own:

  ```
  Loaded — acknowledge briefly and wait for my task.
  ```

  The assistant will confirm the load class and stop, instead of inventing work to do.

Paste-load is **per-session and decays.** In long threads earlier context falls out of the window and the skill goes quiet without warning. If the behavioral delta disappears, start a fresh chat and re-paste. (Projects and Custom GPTs don't have this problem — that's why they're the recommended hosts.)

**Controls you can type anytime**

```
mog on · mog off · mog chill · mog play · floor back on
```

- **Canonical:** the `mog *` controls above. `floor back on` exits Play / loose ideation back to rigor.
- **Aliases:** bare `play`, `riff`, `what-if`, `chill`, `ease up`, `simple mode`, and legacy `skill on` / `skill off` all still work when the context clearly means Prompt Mogging. In a multi-skill setup, generic `skill off` will ask which skill you mean.
- `mog off` disables Prompt Mogging's behavior only. It never disables the base model's own safety or factuality behavior — that isn't part of this skill and can't be switched off by it.

**New here? Run [`TUTORIAL.md`](./TUTORIAL.md)** — seven prompts, about five minutes, walks you through off → on → Play → floor → chill so you can see each mode switch. (It mirrors the test suite; [`ACCEPTANCE_TESTS.md`](./ACCEPTANCE_TESTS.md) is the authority if the two ever disagree.)

## A quick taste


> **You:** Help me pick a database for my app.
>
> **Assistant — frame check:** Before I answer that: "which database" is usually the wrong first question. The load-bearing one is your access pattern and scale — a choice that's right for 10k rows and read-heavy is wrong for 10M and write-heavy. Tell me roughly which world you're in and the database answer mostly falls out. Want the 3 questions that pin it down?

That's the skill working: not the answer you asked for — the answer you needed.

## What it can't do (on purpose)

Being honest about limits is part of the design:

- **It can't act.** No running code, no browsing, no calling other models, no automation. It suggests; you do.
- **It can't remember** across sessions unless the host you run it in provides memory. By default, each chat starts fresh.
- **It can't validate** anything for you. When it says "verify this," that's a prompt for *you* to check — not a claim that it did.
- **It's only as good as the model underneath it.** It shapes behavior; it doesn't add intelligence.

## Status & roadmap

v0.1.5, early pilot. The move set is deliberately small — a handful that earn their place — rather than everything that was possible. Things parked for later (preferences that persist across sessions, a built-in "you're overdoing it" governor, voice-matching for drafts you'll publish, and more) are tracked in [Issues](../../issues).

If something grates, misfires, or nags, that's the most useful feedback there is. Open an issue. The internal change history lives in [`CHANGELOG.md`](./CHANGELOG.md).

## Where the name comes from

The internal version of this skill uses deliberately ridiculous slang — "mogging," "no-pilling," "botmaxx" and friends — borrowed from the two essays it's based on. It's a joke that turned out to be load-bearing: the silly names made the techniques easy to reason about while building it. This user-facing version uses plain labels instead. If you enjoy internet-brainrot taxonomy, the originals are a fun read; if not, you lose nothing by ignoring them.

- [40 Techniques for Mogging LLMs Without Getting Cooked](https://medium.com/@andrew.gregovic/40-techniques-for-mogging-llms-without-getting-cooked-feac634cd684)
- [Prompt Engineering Considered Harmful, Lmao](https://medium.com/@andrew.gregovic/prompt-engineering-considered-harmful-lmao-f3325bed0ccf)

## License & contributing

> Apache-2.0; no bots contributing without manual review

Contributions welcome. One part of the skill is explicitly built to grow by contribution: the **Simpler route** catalog (which task-shapes warrant a cheaper tool) is meant to be extended via PR as people hit real cases.
