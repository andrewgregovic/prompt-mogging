# PROMPT_MOGGING

*A loadable chat skill that turns an AI assistant into a sharper thinking partner for open-ended work — and is honest enough to tell you when not to use it.*

> **Status:** v0.1.3 — early pilot. Works today; expect rough edges. Feedback wanted — see [Issues](../../issues).

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
skill off          # stand down for the session
chill              # same, when you're telling the skill to back off
skill on           # bring it back
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

The skill is one file — [`SKILL.md`](./SKILL.md), about 56,000 characters. That's too big for the "instructions" box on most assistants (Claude Projects and Custom GPTs both cap it near 8,000 characters), so you load the skill as a **reference/knowledge file** and point the assistant at it. Pasting it into a single chat also works for a quick try.

**Claude — recommended, persists across chats**

1. Create a Project (Claude Pro or Team).
2. Upload `SKILL.md` to the project's **Knowledge**.
3. In the project's **Custom instructions** box, add one line:
   > *Follow the PROMPT_MOGGING skill in this project's knowledge. Apply its on-load contract (§0A) at the start of each chat.*
4. Every chat you start inside the project now runs the skill. (The instructions box is small — ~8k characters — which is exactly why the skill lives in Knowledge and the box just points to it.)

**Custom GPT**

1. In the GPT editor, open the **Configure** tab.
2. Upload `SKILL.md` under **Knowledge**. (The Instructions field caps at 8,000 characters — too small for the full skill.)
3. In **Instructions**, add:
   > *Follow the attached PROMPT_MOGGING SKILL.md, including its on-load contract. Use the neutral wrapper labels.*
4. Save. (If Code Interpreter is enabled, users can download the knowledge file — fine here, since the skill is open source anyway.)

**Any chat, zero setup — Claude, ChatGPT, or other**

Paste the contents of `SKILL.md` at the top of a new conversation. It works immediately but doesn't carry over — you re-paste for each new chat. Best for trying the skill before committing to a Project or GPT.

**Controls you can type anytime**

```
skill off · skill on · chill · play / riff · "be more blunt" · "ease up"
```

## A quick taste

> [ILLUSTRATIVE — swap in a real exchange if you have a better one]

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

v0.1.3, early pilot. The move set is deliberately small — a handful that earn their place — rather than everything that was possible. Things parked for later (preferences that persist across sessions, a built-in "you're overdoing it" governor, voice-matching for drafts you'll publish, and more) are tracked in [Issues](../../issues).

If something grates, misfires, or nags, that's the most useful feedback there is. Open an issue. The internal change history lives in [`/changelog`](./changelog).

## Where the name comes from

The internal version of this skill uses deliberately ridiculous slang — "mogging," "no-pilling," "botmaxx" and friends — borrowed from the two essays it's based on. It's a joke that turned out to be load-bearing: the silly names made the techniques easy to reason about while building it. This user-facing version uses plain labels instead. If you enjoy internet-brainrot taxonomy, the originals are a fun read; if not, you lose nothing by ignoring them.

- [40 Techniques for Mogging LLMs Without Getting Cooked](https://medium.com/@andrew.gregovic/40-techniques-for-mogging-llms-without-getting-cooked-feac634cd684)
- [Prompt Engineering Considered Harmful, Lmao](https://medium.com/@andrew.gregovic/prompt-engineering-considered-harmful-lmao-f3325bed0ccf) 

## License & contributing

> Apache 2.0; No bots contributing without manual review 

Contributions welcome. One part of the skill is explicitly built to grow by contribution: the **Simpler route** catalog (which task-shapes warrant a cheaper tool) is meant to be extended via PR as people hit real cases.
