---
title: AOP / EMOD Framework Alignment
status: IN_PROGRESS
description: >-
  Assess to what extent dismech's environmental-exposure and evidence modeling
  aligns with the Adverse Outcome Pathway framework and its in-development
  Evidence Model (EMOD), and identify dismech patterns worth contributing back.
tags: [FRAMEWORK_ALIGNMENT, EVIDENCE, EXTERNAL_COLLABORATION, ENVIRONMENTAL_EXPOSURE, SCHEMA_EVOLUTION]
diseases:
  - Lead_Poisoning
---

# AOP / EMOD Framework Alignment

## Scope

Issue [#8309](https://github.com/monarch-initiative/dismech/issues/8309) asks **to
what extent** dismech's environmental-exposure modeling aligns with the Adverse
Outcome Pathway (AOP) framework. The question is a graded description, not an
adopt/reject decision, and the deliverable is a per-dimension assessment
("Comment B") on that issue.

There are **two AOP reference points**, and conflating them is the main way to get
this wrong:

| Reference point | Character | Stability |
|---|---|---|
| The published **handbook rubric** | Authored ordinal weight-of-evidence grades | Stable, citable |
| **EMOD** (Evidence Model) | Compositional — evidence derived from typed Observation records | In development; properties not finalized |

`Lead_Poisoning` is the pilot comparator entry used to ground the comparison
against a real dismech pathograph.

## Status

**Working notes complete; Comment B not yet drafted.** All six questions about the
AOP-Wiki evidence architecture were resolved from the official bulk XML export
(2026-08-06; 595 AOPs, 2361 KERs), so the handbook-rubric half is writable without
further research.

Kept on local branch `notes-8309-aop-emod`, unpushed.

## What is settled

- **The AOP evidence architecture is split across two levels.** KERs carry five
  free-text prose fields; the ordinal grade sits on the AOP's relationship
  listing. The issue's assumed three-dimension per-KER rubric is close but
  mis-levelled.
- **The value vocabulary is High / Moderate / Low / Not Specified** — an authored
  ordinal grade. `Not Specified` covers ~34% of weight-of-evidence grades and ~57%
  of quantitative-understanding grades, so a large share is simply ungraded.
- **Essentiality is assessed at AOP level**, not on the KER. It therefore does
  *not* map onto a dismech `CausalEdge`, which corrects the `inference.role`
  mapping the issue assumed.
- **dismech is substantially more structured on citations.** AOP KER evidence uses
  inline author-year references; dismech's `EvidenceItem` carries a resolvable ID
  plus an exact quote machine-validated against the fetched source. This is the
  sharpest divergence in dismech's favour, and it inverts the expectation the work
  started from.
- **Shared PATO grounding is the most defensible alignment claim.** AOP's Event
  Component `Action` and dismech's descriptor `modifier` bind to the same two PATO
  terms (`PATO:0002300` / `PATO:0002301`). Checkable rather than argued.
- **dismech has no population level.** `BiologicalScaleEnum` has four values
  against AOP's five-level ladder, exactly as the issue body predicted.
- **A terminal mechanism node is legal in dismech but not in an AOP**, where a Key
  Event needs KERs on both sides. A real structural divergence.

## What is open

1. Is AOP's `Causal Agent` Event Component genuinely dead, or dormant/revivable?
2. Does `Phenotype` remain a *proposed* EC entity, or has it since been adopted?
   Bears on the HP-binding comparison.
3. Should Comment B use the two-reference-point structure above, or address only
   the published rubric and leave EMOD out until its properties settle?

## Possible dismech → EMOD contribution

Per @gingin77 (an EMOD author) there is room for the AOP Evidence class to be
influenced by dismech schema patterns. Split by what dismech can stand behind:

**Proven in practice (~2000 entries):** exact-snippet validation; `supports`
polarity including `REFUTE`; the two evidence layers on a model link; the
`causal_link_type` directness distinction; `hypothesis_groups` for competing
mechanistic models on one graph.

**Not proven — must be offered as a proposal:** the `experiment.design` /
`inference.role` block and the derived-not-authored argument behind it. One worked
example, no schema change, no KB behind it.

This is outbound — a contribution to another project, not a dismech change — so it
is not a design-decision register entry.

## Next steps

- [ ] Draft Comment B on #8309: a graded, per-dimension assessment of how far
      dismech's evidence model covers what AOP's KER weight-of-evidence covers,
      with the EMOD half marked provisional and dated.
- [ ] Resolve open questions 1 and 2 with @gingin77 before the EC comparison is
      stated publicly.
- [ ] Decide whether this project should be published (it is currently local-only).

## Detail

Full working notes, including the provenance table for every source, the XML field
inventory and grade counts, the EMOD class inventory, the Observation-triple
mapping, and the pilot-comparator state:
[`AOP_EMOD_ALIGNMENT/working-notes-2026-08-12.md`](AOP_EMOD_ALIGNMENT/working-notes-2026-08-12.md).

Related: [#8390](https://github.com/monarch-initiative/dismech/issues/8390) /
[PR #8392](https://github.com/monarch-initiative/dismech/pull/8392) (the
`Lead_Poisoning` orphan-node defect found while grounding the pilot), and
[#7855](https://github.com/monarch-initiative/dismech/issues/7855) (KB-wide
causal-edge backlog).
