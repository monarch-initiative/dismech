---
name: github-communication
description: >
  Write the prose of a GitHub PR body, issue comment, review body, or review
  reply in this repo, or a page under `docs/`. Use before posting anything to
  GitHub — opening a PR, summarizing or triaging an issue, replying to a
  reviewer, reporting what a scan found, or explaining why you did not make a
  change — and before adding or editing a `docs/` page or a KB `notes:` field.
  Covers audience calibration, leading with the finding, and the abstraction
  and hedging patterns this repo has accumulated. Its plainness rules do not
  apply to `docs/` or to YAML `description` / `explanation` / `notes`, but its
  audience rule does.
---

# Writing GitHub Comments

The overall goal here is to make GitHub comments in issues and PRs (particularly
the first/leading comment) more readable to broader audiences. Avoid too much internal
jargon, particularly up-front. Especially avoid elliptical language, use plain terms where possible.

What follows are guidelines, the important thing is the principle. If the issue or PR pertains
to a complex technical validation issue, then assume a technical audience, and it will be necessary to use technical language around
the schema, LinkML etc. If the issue/PR involves nuanced interpretation of cellular data, then assume a cell/molbio audience. And
so on.

**Scope.** PR bodies, issue comments, review bodies and replies, and the
summaries scheduled workflows post. Pages under `docs/` and prose inside KB
YAML (`description`, `explanation`, `notes`) are **exempt from the
plainness-and-jargon rules** below but **not** from the audience rule that
follows: those are written for a curator who wants the mechanism, so ontology
terms, gene symbols and pathway names belong there and this skill's plain
language would flatten them.

**The exemption is about vocabulary, not about audience.** A denser register is
fine; a document only the agent that wrote it would find useful is not. `docs/`
and `notes:` are still written for a human reader — a curator, a maintainer,
someone reading the rendered page. Neither is licence to write for a future AI
session or to narrate your own process as a note to yourself. If a passage is a
first-person reflection on the writing agent's own workflow ("I pushed twice,
which cost a review round, so next time I will…") rather than a fact about the
disease, the schema, or the corpus, it is in the wrong file. Where it belongs:

| What you are writing | Where it goes |
|---|---|
| A fact about a disease, the schema, or the corpus | `docs/`, or the entry's `notes:` |
| Review or audit provenance for an entry | the `details` field of a `history/` record |
| A reflection on your own review cycle | the PR or issue thread, under the rules below |
| A rule worth keeping | `CLAUDE.md`, or the skill it changes |

PR #12535 is the worked example: a curation retrospective titled *Custody of a
Claim* whose real content was the author's own push count and review rounds,
closed for exactly this reason. The same drift shows up in `notes:` — a
sentence like "Review round 1. The screening-yield rate is deleted, as above"
presumes a reader with the review thread already open, and describes the
curation session rather than the disease. *History Records* in `CLAUDE.md`
already says review and audit provenance goes in a `history/` record, "not
inside the KB YAML".

`docs/superpowers/` is the deliberate exception — it is an agent-facing
investigation, plan and spec log, and the audience rule does not apply there.

See #8908 for the wider pattern this is one instance of.

## Before you post

**Re-read the thread immediately before posting — not when you started the work
that produced the comment.** Threads move while a comment is being written, and
a reply that contradicts what somebody said an hour earlier is worse than no
reply at all.

The same goes for repository state you quote. Re-read the file at the commit you
are about to cite, rather than trusting a copy you read earlier in the session.

Worked example: a comment on #8512 reporting that a provider outage had cleared
said the issue had "been quiet since 14 August". A maintainer had commented ten
hours earlier, testing the very claim that comment went on to make and finding
it false — and the comment also quoted a `project.justfile` passage from a stale
`origin/main` ref, text that no longer existed and whose stated rationale had
since been replaced. Both checks had been run. They had been run eleven hours
too early, and retracting them took a second comment.

## The rules

**BLUF: Lead with the finding, ideally around 3 sentences.** Use plain language,
ideally with minimal technical jargon (technical details specific to the intended audience can come later).

**Avoid abstract and elliptical language. Avoid metaphors. Be concrete.** If it
is necessary to use abstractions, ground these with concrete examples.

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

