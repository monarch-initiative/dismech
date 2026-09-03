---
name: ker-evidence-triage
description: >
  Assess how much evidence AOP-Wiki actually carries for a Key Event
  Relationship before curating from it. Use when judging whether a KER, or a set
  of them, is backed by literature; when reading `completion_score`,
  `weight_of_evidence`, `empirical_support`, or `oecd_status` off a KER or its
  parent AOP; when deciding how much deep-research effort an AOP-derived causal
  edge will cost; or when auditing an existing dismech edge whose provenance
  traces to AOP-Wiki.
---

# KER evidence triage

**A KER can be completely uncited.** At the time this skill was written
(09-03-2026), the AOP-Wiki XML export — the 08-06-2026 snapshot — held 2,369
KERs, of which 738 (31%) carry references and the other 1,631 (69%) carry none.
A KER with an empty evidence block still renders as a clean arrow between two
named events, and nothing in the console output distinguishes it from a
well-supported one.

This is the procedure for finding out which you have. It changes what the rest
of the work costs, so run it **before** committing deep-research effort, not
after — it is a prioritization gate, not a post-hoc note.

Reaching the records is the `aop-wiki` skill's job — read it for the CLI, the
date footgun, and the entity shapes. This skill is what you do with a KER once
you have one.

## The 29.41% rule

`completion_score.percent == 29.41` on a KER means the record is an empty stub:
endpoints and identifiers, nothing else. This is exact, not a heuristic. In the
08-06-2026 snapshot 1,536 of 2,369 KERs (65%) sit at that value and **zero of
them carry a single reference**. It is also the corpus median, so most of
AOP-Wiki's causal edges are assertions with nothing behind them.

One number, read before anything else, tells you whether the KER has content.
A stub KER is not disqualified — but it means AOP-Wiki is contributing a
hypothesis and no evidence, and every citation will have to be found from
scratch. Rank the work accordingly, and say so when you report the plan.

## The evidence fields

For each KER you are assessing, read three fields on `ker_info` and one on its
parent AOP:

| Field | On | What it tells you |
|---|---|---|
| `references` | KER | whether any literature is attached to *this edge* |
| `weight_of_evidence.free_text` | KER | whether anyone assessed the edge |
| `empirical_support.free_text` | KER | whether experimental support is described |
| `oecd_status` | AOP | whether the pathway was ever externally reviewed |

Three traps live here.

**`completion_score` is not a quality score.** It counts populated fields on the
wiki record. AOPs 552, 555, 556, 558 and 560 score 94–100% complete, have never
been OECD reviewed (`oecd_status: ""`), and every one of their KERs examined in
the cardiac sweep worked through in `mie-ker-capture` carries zero references.
High completeness on an unreviewed pathway is the most misleading state in the
data.

**An empty `oecd_status` is not a rejection.** 450 of 596 AOPs are empty. It means
no review has happened. Endorsement raises confidence in a pathway; its absence
is not evidence against one, and neither state substitutes for literature.

**AOP-level references do not discharge a KER.** The AOP record carries a
`references` HTML blob — real citations, often substantial. They attest to the
pathway as a whole and cannot be attributed to any specific causal step. Treat
them as a starting bibliography for primary-literature verification, never as
the citation for an edge.

## Map the AOP's citations onto its own steps

An AOP carries a `references` blob even when its KERs carry nothing. Do not stop
at counting it. Split it into individual citations and assign each one to the step
it actually serves — upstream, this edge, downstream, or none.

Two things fall out that a count cannot show.

**Whether the author evidenced this step at all.** AOP 558 carries ten citations
and not one measures cAMP after PDE inhibition — the edge the AOP is named for.
Four are enzyme-background or therapy reviews, four belong to the downstream
RyR2/calcium half, one is tangential, one has no evident connection to the
pathway. The bibliography is real and the step is still unevidenced.

**Whether the bibliography contradicts the pathway.** In the same list, Zhou 2017
attributes RyR2 hyperphosphorylation to oxidative-stress-driven calpain
activation — a competing mechanism to the cAMP/PKA route asserted by the very
next KER. An AOP citing evidence against its own edge is a strong signal to
verify that edge before curating it, and you only see it by reading the
citations rather than counting them.

## Recording the result

Record the triage result per edge. An uncited KER is not disqualified — it is a
claim you will have to source entirely yourself, and knowing that up front is the
point.

Whatever the triage says, the edge still needs its own primary literature before
it can be curated. **AOP-Wiki is never a dismech reference**: there is no `AOP:`
prefix in `references_cache/`, no fetcher, and no cacheable body for a snippet to
match. See `dismech-references`.
