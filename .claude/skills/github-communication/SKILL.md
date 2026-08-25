---
name: github-communication
description: >
  Write the prose of a GitHub PR body, issue comment, review body, or review
  reply in this repo. Use before posting anything to GitHub — opening a PR,
  summarizing or triaging an issue, replying to a reviewer, reporting what a
  scan found, or explaining why you did not make a change. Covers audience,
  length budget, the default of silence, and the specific abstraction and
  hedging patterns this repo has accumulated. Not for YAML `description` /
  `explanation` / `notes` prose, which is held to a different standard.
---

# Writing GitHub Comments

Most people here do not read every agent comment, and nobody is expected to
edit them before they post. So the comment you write is the final artifact.
Write it for the person who opens the thread cold.

**Scope.** PR bodies, issue comments, review bodies and replies, and the
summaries scheduled workflows post. **Not** in scope: prose inside KB YAML
(`description`, `explanation`, `notes`) or in `docs/`. Those are written for a
curator who wants the mechanism, and their denser register is correct — do not
apply this skill's plainness rules to them.

## The rules

**Lead with the finding, in one sentence, under 30 words.** A reader who stops
after that sentence should have the answer. Not what you set out to do, not
what the thread is about — what you found or what you changed.

**Budget the opening.** Everything before the first heading: 60 words. If it
does not fit, the extra was context the reader already had.

**Default to silence.** Posting nothing is a valid outcome and usually the
right one when you have no specific finding, when someone else already said
it, or when your comment would restate the thread. A scan that found nothing
says so in one line, or says nothing at all. Do not manufacture a
contribution to justify a run.

**Match length to the question.** A yes/no question gets a yes or a no and a
reason. Headings on a three-sentence answer are noise. Reserve structure —
headings, tables, checklists — for content that has genuine sections.

**Name things concretely.** `src/dismech/entity_refs.py:SECTION_KEYS`, not
"the resolution layer". "Three of the twelve snippets are not exact
substrings", not "there are some evidence integrity concerns". If you cannot
name the file, the function, or the number, you probably have not checked.

**Say the plain thing when something is wrong.** If a decision looks like a
mistake, write "I think this is wrong, because X". Do not build an elaborate
frame around it. Elliptical prose most often appears where an agent has found
a contradiction and is hedging instead of reporting it — the hedge is the
defect, not the style.

**Quantify or drop it.** "Comprehensive", "robust", "significant", "extensive"
carry no information. Either give the count, or cut the word.

**No meta-commentary.** Do not narrate your process, list what you could not
check unless it changes the conclusion, apologize for length, or tell the
reader you tried to write plainly. Saying you were brief is not being brief.

**Never write bare `#1`, `#2` for your own list items** — GitHub expands them
into unrelated issue titles. Write "item 1", "finding 2". Reserve `#N` for real
issue and PR references. (Also in `CLAUDE.md`.)

## PR bodies

A curation PR has a real deliverable, so describe it and stop. Four sections is
usually the whole document:

- **Summary** — what entry, what MONDO ID, what the mechanism is, in a few lines.
- **What I intentionally did NOT do** — judgment calls and the reason for each.
  This is the highest-value section in a curation PR and the most often
  omitted. `PR #8442` (LCA5) is the model: it records a phenotype it declined
  to assert and quotes the source sentence that made it decline.
- **Evidence scope** — what the evidence establishes and, where it matters,
  what it does not. See `PR #9149`, which states that Phase 1 initiation
  establishes clinical-stage status but not disease-specific efficacy.
- **Validation** — the commands you ran and their results. Never claim a check
  that did not finish.

Do not add an "Implementation Details" section that restates the summary in
longer words.

## Reviews and replies

State the defect, the file and line, and what would fix it. If you are not
making a change a reviewer asked for, say which ask and why in two sentences —
that is a complete reply, and a longer one reads as evasion.

Do not thank, do not praise, do not preface. Disagreeing is fine and useful;
do it once, with the argument stated plainly, then follow `CLAUDE.md`'s
escalation rule rather than going back and forth.

## Before you post

Read the first sentence alone. Does it carry the finding? Then read the last
paragraph — if it is about you rather than the work, delete it.

Two failures are worth catching by name, because both have shipped here:

- A long comment on a question the author has not finished asking. If the
  thread is deciding *which* approach, do not deliver all of them.
- A comment whose length is set by how much you investigated rather than by
  how much the reader needs. Investigation is not the deliverable.
