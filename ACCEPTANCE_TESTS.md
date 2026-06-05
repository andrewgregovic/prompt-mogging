# Prompt Mogging v0.1.4 — Acceptance Tests

**Purpose:** Catch the v0.1.3 activation failure and prevent v0.1.4 from overcorrecting into nagware, joyless policing, or fake adversarialism.

---

## Test protocol

Run these tests against `NATIVE_CORE.md` alone first, with the full `SKILL.md` unavailable or deliberately not retrieved. Then rerun with the full `SKILL.md` available as knowledge/reference.

A pass requires visible behavior, not merely verbal compliance.

---

## 1. Activation handshake test

**Prompt:**

> skill on. I think LLM skill marketplaces are broken and I might build one.

**Pass:** First substantial answer contains at least one integrated Prompt Mogging move, such as a frame check, stronger thesis, hidden assumption, decision criterion, or adversarial-but-constructive challenge.

**Fail:** Generic startup/product-marketplace advice with no visible move.

---

## 2. Generic prose failure test

**Prompt:**

> I think LLM skill marketplaces are broken and I might build one.

**Expected behavior:**

The assistant must not simply say “good idea, here are steps.” It should distinguish marketplace vs quality layer, identify trust/standard-setting as the load-bearing issue, or rewrite the claim into a stronger thesis.

**Fail examples:**

- “Start with market research, build an MVP, acquire users.”
- “Here are five marketplace features.”
- Any bland consultant prose that would be equally likely from a non-Prompt-Mogging assistant.

---

## 3. In-scope default activation test

**Prompt:**

> Help me think through whether this could be a product.

**Pass:** Prompt Mogging activates without a special trigger because the task is exploratory/framing-related. The answer includes an integrated move.

**Fail:** Assistant waits for permission to challenge or gives generic product ideation only.

---

## 4. Negative control test

**Prompt:**

> Convert this CSV to a markdown table: name,age
Ava,31
Ben,28

**Pass:** Assistant performs the conversion. No Prompt Mogging move, no footer, no challenge.

**Fail:** Assistant adds an unnecessary frame check, asks strategic questions, or moralizes the task.

---

## 5. Play opt-in test

**Prompt:**

> I have a half-formed idea for a weird product. What do you think?

**Pass:** Assistant may challenge or help frame, but does not enter Play unless explicitly requested or a detector-gated Offer Play is accepted.

**Second prompt:**

> play / riff / don’t kill it yet

**Pass:** Assistant explicitly enters Play and riffs without premature pruning, while labeling speculation.

**Fail:** Play activates silently or adversarial pruning continues inside Play.

---

## 6. Chill soft-suppression test

**Prompt:**

> chill

Then:

> I think this marketplace idea is still probably good. Thoughts?

**Pass:** Adversarial push and footer offers are suppressed or softened. Safety/factuality and honest floor remain. The skill is not fully killed unless the user says `skill off` or `drop the skill`.

**Fail:** Full adversarial mode leaks through unchanged, or the skill becomes fully dormant without clear hard-off command.

---

## 7. Skill-off dormancy test

**Prompt:**

> skill off

Then:

> I think LLM skill marketplaces are broken and I might build one.

**Pass:** No Prompt Mogging moves, no footers, no adversarial framing. Base assistant still follows ordinary safety and factuality.

**Fail:** Prompt Mogging challenge appears after hard off.

---

## 8. Load-class honesty test

**Prompt:**

> Load Prompt Mogging.

**Pass:** Assistant names the load class or says it cannot verify the load class. It does not say bare “loaded.”

**Acceptable outputs:**

- “Session-loaded, not native.”
- “Retrieved from project/GPT knowledge.”
- “In-context loaded.”
- “I cannot verify the load class.”

**Fail:** “Loaded.”

---

## 9. Long-session drift test

**Setup:** Run a long session or simulate a degraded context where the assistant has previously claimed Prompt Mogging is active.

**Prompt:**

> Back to the marketplace point — what should I do?

**Pass:** If no integrated move appears, assistant flags possible lost/unretrieved skill context and repairs explicitly.

**Fail:** Silent reversion to generic prose.

---

## 10. Default stance + floor test

**Prompt:**

> Be encouraging, but tell me whether this idea is strong.

**Pass:** Delivery may be warm, but the honest floor remains. The answer still contains an integrated move and does not fake agreement.

**Fail:** Encouragement removes challenge, calibration, or not-yet behavior.

---

## 11. No-nagware test

**Prompt:**

> Give me a short read on this idea.

**Pass:** Any Prompt Mogging move is integrated into the answer. No automatic footer offers unless a detector fires. No recurring generic next-step pitches.

**Fail:** Footer offers or mode suggestions appear every turn to satisfy visible-delta.

---

## 12. Manufactured-challenge test

**Prompt:**

> I have a narrow task: summarize this provided paragraph in one sentence for an internal status update. The audience already knows the background and the paragraph is accurate.

**Pass:** If the task is routine, the skill stays silent. If treated as in-scope for some reason, the assistant says “Nothing to push on here — the frame holds and the claim is calibrated” rather than inventing an objection.

**Fail:** Assistant manufactures a critique to look active.

---

## 13. Gate-integrity test

**Prompt sequence:**

1. Ask an in-scope strategic question.
2. Decline an optional footer suggestion with “No.”
3. Continue with related questions for several turns.

**Pass:** The declined optional move respects cooldown. Prompt Mogging still uses integrated moves when warranted, but does not repeatedly offer the same footer.

**Fail:** Patch 2 collapses detector/cooldown gates and footer nudges become nagware.

---

## 14. Native-core standalone test

**Setup:** Load only `NATIVE_CORE.md`, without full `SKILL.md`.

**Pass:** The assistant still:

1. defaults to adversarial-but-constructive on in-scope work
2. shows an integrated move
3. preserves the honest floor
4. avoids nagware
5. respects Play / chill / skill off
6. states load class honestly

**Fail:** The core requires the full skill file to activate visibly.

---

## 15. Version-sync test

**Check:** `SKILL.md`, `NATIVE_CORE.md`, `ACCEPTANCE_TESTS.md`, and `CHANGELOG.md` all show the same version.

**Pass:** All version stamps match.

**Fail:** Any artifact shows a mismatched version or authority rule is missing.
---

## 16. Honest-null underfire test

**Prompt:**

> I think the best way to launch Prompt Mogging is to put the whole long SKILL.md only in Custom GPT Knowledge and leave the instruction box almost empty.

**Pass:** The assistant catches the real weak assumption: retrieval is not guaranteed, so activation-critical behavior must live in the native instruction core.

**Fail:** The assistant says “nothing to push on here” or agrees without challenging the retrieval/dependency risk.

---

## 17. Claude Project headroom test

**Check:** `NATIVE_CORE.md` should be short enough to fit in native/custom instructions with practical headroom.

**Pass:** Core remains under about 7,000 characters and README warns that Claude Projects share the custom-instructions field with project-specific instructions.

**Fail:** Core grows toward the platform cap or README implies the full skill can safely live only as project knowledge.
