---
name: github-communication
description: >
  Write the prose of a GitHub PR body, issue comment, review body, or review
  reply in this repo. Use before posting anything to GitHub — opening a PR,
  summarizing or triaging an issue, replying to a reviewer, reporting what a
  scan found, or explaining why you did not make a change. Covers audience
  calibration, leading with the finding, and the abstraction and hedging
  patterns this repo has accumulated. Not for YAML `description` /
  `explanation` / `notes` prose, which is held to a different standard.
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
summaries scheduled workflows post. **Not** in scope for this skill's
plainness-and-jargon rules: prose inside KB YAML (`description`, `explanation`,
`notes`) or in `docs/`. Those are written for a curator who wants the
mechanism, and their denser register is correct — do not apply this skill's
plainness rules to them.

**The exemption is about density, not about audience.** Every one of those
targets — `docs/`, and KB `notes:` — is still written for a human reader: a
curator, a maintainer, someone reading the rendered page. None of it is
license to write for a future AI session, or to narrate your own process as a
note to yourself. A `docs/` PR titled "Custody of a Claim" whose content is
mostly about the author's own push count and review rounds is not a denser
register, it's a diary entry that happens to sit under `docs/`, and it fails
this rule exactly as a bad PR body would — see #12535. The same drift shows up
in `notes:`: a sentence like "Review round 1. The screening-yield rate is
deleted, as above" presumes a reader who already has the review thread open,
and describes the curation session rather than the disease. That content has a
home — the `details` field of a `history/` record (see *History Records* in
`CLAUDE.md`) — which already says review/audit provenance goes there, "not
inside the KB YAML." If you are writing about your own review cycle, what you
will remember for next time, or what a prior round of you did, that is a
`history/` entry or a PR/issue comment (governed by the rules above), never a
`docs/` page or a `notes:` field. See #8908 for the wider pattern this is one
instance of.

**That exemption is about vocabulary, not about audience.** Denser register is
fine; a document that only the agent that wrote it would find useful is not.
`docs/` (outside `docs/superpowers/`, which is explicitly an agent-facing
investigation/plan/spec log) and `notes:` are for a human curator who wants
domain content — a mechanism, a decision, a dataset, a finding. They are not
the place for an agent to narrate its own compliance with its own process
rules. If a passage is a first-person reflection on the writing agent's own
workflow ("I pushed twice, which cost a review round, so next time I will...")
rather than a fact about the disease, the schema, or the corpus, it belongs in
the PR/issue thread that already carries that conversation — under this
skill's plain-language rules — not in a `docs/` file or a `notes:` field.
PR #12535 is the worked example: a "curation retrospective" whose real content
was process narration addressed to no reader in particular, closed for
exactly this reason. Related: #8908.

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

