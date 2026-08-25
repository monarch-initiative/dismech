---
name: github-communication
description: >
  Write the prose of a GitHub PR body, issue comment, review body, or review
  reply in this repo. Use before posting anything to GitHub — opening a PR,
  summarizing or triaging an issue, replying to a reviewer, reporting what a
  scan found, or explaining why you did not make a change. Covers audience,
  length budget, and the specific abstraction and
  hedging patterns this repo has accumulated. Not for YAML `description` /
  `explanation` / `notes` prose, which is held to a different standard.
---

# Writing GitHub Comments

The overall goal here is to make GitHub comments is issues and PRs (particularly
the first/leading comment) more readable to broader audiences. Avoid too much internal
jargon, particularly up-front. Especially avoid elliptical language, use plain terms where possible.

What follows are guidelines, the important thing is the principle. If the issue or PR pertains
to a complex technical validation issue, then assume a technical audience, and it will be necessary to use technical language around
the schema, LinkML etc. If the issue/PR involves nuanced interpretation of cellular data, then assume a cell/molbio audience. And
so on.



**Scope.** PR bodies, issue comments, review bodies and replies, and the
summaries scheduled workflows post. **Not** in scope: prose inside KB YAML
(`description`, `explanation`, `notes`) or in `docs/`. Those are written for a
curator who wants the mechanism, and their denser register is correct — do not
apply this skill's plainness rules to them.

## The rules

**BLUF: Lead with the finding, ideally around 3 sentences.** Use plain language,
ideally with minimal technical jargon (technical details specific to the intended audience can come later).

**Avoid abstract and elliptical language, Avoid metaphors. Be concrete.** If it
is necessary to use abstractions, ground these with concrete examples

**Say the plain thing when something is wrong.** If a decision looks like a
mistake, write "I think this is wrong, because X". Do not build an elaborate
frame around it. Elliptical prose most often appears where an agent has found
a contradiction and is hedging instead of reporting it — the hedge is the
defect, not the style.

**Use diagrams where appropriate**. GitHub will render both mermaid and simple
ascii diagrams. Use judgment. With mermaid you have less control of layout, and
it will be less compact, but it can be easier to grasp on a first pass.

**No meta-commentary.** Do not narrate your process, list what you could not
check unless it changes the conclusion, apologize for length, or tell the
reader you tried to write plainly. Saying you were brief is not being brief.

**Never write bare `#1`, `#2` for your own list items** — GitHub expands them
into unrelated issue titles. Write "item 1", "finding 2". Reserve `#N` for real
issue and PR references. (Also in `CLAUDE.md`.)

