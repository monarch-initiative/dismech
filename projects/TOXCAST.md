---
title: ToxCast Assay Coverage of the Pathograph
status: IN_PROGRESS
description: >-
  How far EPA's ToxCast and Tox21 assay annotations reach into the dismech
  pathograph. About a third of the assay endpoints declare a gene target that
  some pathophysiology node names, and those nodes sit in about a tenth of the
  disease entries. A shared gene is a candidate for a mapping, not a mapping.
tags: [NAM, ENVIRONMENTAL_EXPOSURE, PATHOPHYSIOLOGY, FEASIBILITY_ANALYSIS]
---

# ToxCast Assay Coverage of the Pathograph

ToxCast and Tox21 are the US EPA's high-throughput screening programs. Each
**assay endpoint** in them is one measurement: a named readout, in a named
system, aimed at a named molecular target. EPA publishes a structured
description of every endpoint, saying which gene it targets, what kind of
target that is, which process it reads, which species and tissue it ran in,
what method it used, and which way a hit reads.

That description is what could let an assay be tied to a dismech
pathophysiology node without reference to any chemical. This project measures
how far it reaches into the pathograph as it stands, and tests whether dismech
can represent such a tie at all, before any is committed.

It is tracked in issue #12858. The parent is #12682, which owns everything
about chemical results: which chemicals were active in which assay, at what
potency. None of that is in scope here, and nothing on this page depends on a
chemical having been tested.

## What "coverage" means on this page

An endpoint is a **candidate** for a node when both name the same gene. The
counts below are counts of candidates.

They are not counts of mappings, and the difference is the reason for the
word. Issue #12858 sets out three ways an endpoint and a node can share a gene
and still not correspond: the node names a lesion where the assay reads a
state, the two run in opposite directions, or they measure different
quantities of the same gene product. None of those is visible to a join on
gene. So every figure here is an upper bound on what could be mapped, and the
share of candidates that survive a closer reading is not yet known.

The join itself:

- On the dismech side, a node names a gene through `genes[]`, the singular
  `gene`, or the gene of its `genetic_context`. Those are the slots the
  pathograph builder links a gene to a mechanism on. Only HGNC-bound
  descriptors count; a gene written as free text is not a binding.
- On the ToxCast side, the key is the gene symbol the endpoint declares,
  upper-cased. An endpoint can declare several genes and is a candidate if any
  of them is on a node.
- A gene in ToxCast has its own species, separate from the system the assay
  ran in. A receptor from zebrafish expressed in a human cell line is a
  zebrafish gene in a human assay. A target counts as **human** when at least
  one endpoint names the human gene, and as **ortholog-only** when the panel
  names it solely through another species. An ortholog joins to dismech only
  where its upper-cased symbol is also a human gene's symbol, and is reported
  apart wherever it matters.

## The snapshot

Assay annotations retrieved from the EPA CTX API on 2026-09-30; `kb/disorders/`
as of commit `0aedd3ce8e`. Both move: the panel with each EPA release, the
pathograph with every curation pull request. The complete tables are in
[the coverage report](../docs/reports/toxcast-pathograph-coverage-2026-09-30.md),
and `just toxcast-coverage` regenerates them, so treat the numbers below as
dated and the recipe as current.

### a) Pathograph node coverage

| | Count | Share |
| --- | ---: | ---: |
| Assay endpoints in the panel | 1,570 | |
| Endpoints declaring a gene target | 1,108 | 70.6% of the panel |
| **Candidate endpoints** | **552** | **35.2% of the panel** |
| Pathophysiology nodes in `kb/disorders/` | 22,403 | |
| Nodes naming an HGNC-bound gene | 4,021 | 17.9% of nodes |
| **Candidate nodes** | **452** | **2.0% of nodes** |
| Candidate endpoint-node pairs | 2,080 | |

Half of the endpoints that declare a gene are candidates, and they converge on
a small part of the pathograph: 452 nodes, or 11.2% of the nodes that name any
gene. The 2,080 pairs are the size of the job if every candidate were read.

Three things about where the candidates fall:

- **They are overwhelmingly molecular.** Of the candidate nodes that carry a
  `biological_scale`, 186 are `MOLECULAR`, 37 `CELLULAR`, 5 `TISSUE` and 2
  `ORGANISM`. Another 222 carry no scale tag. That is the expected shape: a
  node names a gene mostly where its claim is about that gene's product.
- **The assay-heavy families are not the node-heavy ones.** Nuclear receptors
  are the largest family in the panel, at 255 endpoints, and 164 of those are
  candidates, yet between them they reach 56 nodes in 45 entries. The 42
  candidate endpoints in the DNA-binding family reach 104 nodes in 84 entries,
  and the 55 kinase candidates reach 92 nodes in 79 entries.
- **64 candidate nodes record a variant**, in the sense of carrying a
  `genetic_context`. Those are the nodes most likely to name a lesion where an
  assay reads a state. The other 388 are not cleared by that: a node can name
  a lesion in its prose without using the slot.

### b) Gene coverage

The panel names 496 distinct gene targets: 433 human and 63 ortholog-only.

| Where the target sits in `kb/disorders/` | Human | Ortholog-only | All |
| --- | ---: | ---: | ---: |
| On a pathophysiology node | 180 | 14 | 194 |
| Bound in a `genetic:` record, on no node | 31 | 4 | 35 |
| Bound elsewhere in an entry only | 0 | 0 | 0 |
| Bound nowhere | 222 | 45 | 267 |

So 39% of the panel's targets are on the pathograph, 7% are known to dismech
without being on it, and 54% are not bound in any disease entry.

The panel is very uneven, and so is the pathograph, in different places. 247
targets appear in exactly one endpoint and twelve appear in ten or more. Of
those twelve, nine are on a node: ESR1, AR, PPARG, NR3C1, ESR2, THRA, THRB,
NR1H4 and TP53. PGR (14 endpoints) and NR3C2 (10) are bound nowhere, and CXCL8
(10) only in `genetic:` records. Going the other way, the targets that reach
the most entries are cancer drivers with few assays behind them: TP53 is on 38
nodes in 36 entries from 10 endpoints, STAT3 on 21 nodes from 2, and PIK3CA on
18 nodes from a single endpoint. ESR1 has 40 endpoints and 8 nodes.

ESR1 is worth a note of its own. When #12858 was written it was the most
heavily assayed target in the panel and no node named it. The 8 nodes in 7
entries it has now are the work of the estrogen signalling project
(`projects/ESTROGEN_SIGNALLING.md`), which was opened to close that gap.

### c) Disease coverage

| Entries in `kb/disorders/` | Count | Share |
| --- | ---: | ---: |
| All entries | 3,256 | |
| **Carry at least one candidate node** | **317** | **9.7%** |
| Bind a target somewhere, on no node | 189 | 5.8% |
| Bind no target | 2,750 | 84.5% |

317 entries carry a node a ToxCast endpoint could be considered for. In 230 of
them it is a single node; 77 have two or three, and 10 have four or more.

The 189 entries in the middle row already bind a panel target, typically in
`genetic:`, without any node naming it. Whether the gene belongs on a node is
a curation question for each entry and not a backfill, because a gene on a
node asserts that it drives that mechanism in that disease.

## What the counts leave out

- **Endpoints with no gene target.** 462 endpoints, 29.4% of the panel, cannot
  be found by a gene join at all. 110 are flagged as cell-viability
  counter-screens. The rest include the raw channels of reporter assays, where
  only the ratio endpoint carries the gene, background controls, and
  whole-system readouts such as the neurodevelopment and zebrafish development
  assays. Having no gene is not the
  same as having no node to speak to: a viability endpoint may bear on a
  cell-death node. Reaching those needs a different key, and #12858 asks
  whether the annotation's biological-process field could be one.
- **Nodes with no gene.** 82.1% of pathophysiology nodes name no HGNC-bound
  gene, and are invisible to this join for the same reason.
- **Orthologs.** 71 of the 552 candidate endpoints reach a node only through
  another species' gene, such as a rat receptor matched to a node that names
  the human one. They are candidates for the gene, and an extra step removed
  from a claim about the human protein.
- **Symbol drift.** The join rewrites three symbols ToxCast still carries that
  HGNC has replaced (`H2AFX`, `H3F3A`, `PPP2R4`) and splits one composite gene
  object (`FOS|JUN`). `just toxcast-coverage --check-symbols` lists any human
  target symbol that is no longer an HGNC approved symbol.
- **Modules.** Mechanism modules are counted apart from diseases: 12 of the
  898 module nodes name a panel target, across 9 modules.

## How this compares with the figures in #12858

The issue reported 170 targets on 368 nodes at commit `fc510ecca0`. This page
reports 194 on 452. The two are not comparable figure for figure: the issue
read `genes[]` alone, this count also reads `gene` and `genetic_context`, and
the pathograph has been curated in between. The endpoint totals agree, at
1,570 endpoints and 1,108 with a usable gene target. The issue's 497 distinct
targets are 496 here because `FOS|JUN` is split into two genes that the panel
already names separately.

## Regenerating

```bash
just toxcast-refresh                                 # cache the annotations; needs CTX_API_KEY
just toxcast-coverage                                # the full report, to stdout
just toxcast-coverage --json                         # the headline figures
just toxcast-coverage --format tsv --table targets   # one row per gene target
just toxcast-coverage --format tsv --table nodes     # one row per candidate node
just toxcast-coverage --format tsv --table endpoints # one row per assay endpoint
just toxcast-coverage --format tsv --table diseases  # one row per entry with a candidate node
just toxcast-coverage --out docs/reports/toxcast-pathograph-coverage-<date>.md
```

The annotations are cached under `data/toxcast/` and gitignored;
`data/toxcast/MANIFEST.yaml` records when they were retrieved. The coverage
recipe is offline once they are cached, reports only, and exits 0. The
`epa-ctx-api` skill covers the API itself and the ways the gene field
misleads.

## Still to come on this page

Issue #12858 asks for more than the measurement above. Each of these is its
own piece of work and none is started here:

- one worked example of fitting an assay into the schema's existing
  model-to-mechanism vocabulary;
- an evaluation of whether assay-to-node mappings should be added to dismech
  at all;
- an evaluation of the AOP-Wiki Key Event links the API itself publishes for
  some endpoints;
- the open questions the issue raises about endpoints without a gene target,
  non-cell-based assay formats, and the biological-process field.
