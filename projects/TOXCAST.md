---
title: ToxCast Assay Coverage of the Pathograph
status: IN_PROGRESS
description: >-
  How far EPA's ToxCast and Tox21 assay annotations reach into the dismech
  pathograph. About a third of the assay endpoints declare a gene target that
  some pathophysiology node names, and those nodes sit in about a tenth of the
  disease entries. A shared gene is a candidate for a mapping, not a mapping.
tags: [NAM, ENVIRONMENTAL_EXPOSURE, PATHOPHYSIOLOGY, FEASIBILITY_ANALYSIS]
diseases:
- Generalized_Resistance_to_Thyroid_Hormone
- Resistance_to_Thyroid_Hormone_Alpha
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

The third row is empty in this snapshot, not broken: every panel target that
any entry binds sits either on a node or in a `genetic:` record. The row
exists because a gene can be bound in other places, such as a treatment's
`target_gene` or a subtype's gene list, and a target found only there would
land in it.

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

## Worked example: one THRB endpoint against the thyroid-hormone-resistance entries

The counts above say how many candidates exist. This says what writing one down
costs, using the endpoint #12858 names for the purpose.

**The endpoint.** `TOX21_TRB_COA_Antagonist_Followup_ratio`, EPA assay endpoint
2247. A GST-tagged TR-beta ligand-binding domain, a terbium-labelled anti-GST
antibody and a fluorescein-labelled SRC-2 coactivator peptide report coactivator
recruitment by resonance energy transfer, normalized against DMSO-only and T3
control wells. EPA annotates the target as human THRB, the direction as loss,
and the format as **cell-free**; a hit is a chemical that reduces recruitment.
Its method paper is PMID:31566444, which describes the reaction as 5.0 nM of
GST-tagged TR-beta ligand-binding domain with a 200 nM coactivator peptide — no
cell of any kind.

**The node the gene join offers.** THRB is named by exactly one pathophysiology
node in the corpus: `THRB Dominant-Negative Receptor Formation`, the trigger
node of Generalized_Resistance_to_Thyroid_Hormone. It is `MOLECULAR`, and its
`genetic_context` records `functional_impact_category: DOMINANT_NEGATIVE` with a
missense allele.

**The node the join cannot offer, and which the assay actually matches.** The
next node down that chain is `Impaired Corepressor Release at Thyroid Hormone
Response Elements`. Its molecular function is `GO:0001222` transcription
corepressor binding and its description says the mutant receptor "fails to
release the nuclear receptor corepressor complex (NCoR/SMRT) ... and
correspondingly fails to recruit coactivators". Failure to recruit coactivators
is precisely what endpoint 2247 measures. That node names no gene, so the gene
join is blind to it.

This is a limit on candidate *discovery*, not on the mapping vocabulary. This
entry names THRB once, on the trigger node, and describes the consequences
downstream without repeating it, so the join reaches the lesion and not the
state. How general that is has not been measured, and it is not universal —
only 64 of the 452 candidate nodes carry a `genetic_context` at all. But where
it holds, the count on this page and the mapping a curator would actually want
point at different nodes.

### The record the schema requires

Written out in full, against the trigger node the join proposes. This block
validates: schema, ontology terms, and the quoted snippet against the cached
method paper.

```yaml
experimental_models:
- name: TOX21_TRB_COA_Antagonist_Followup_ratio
  experimental_model_type: OTHER
  description: >-
    EPA ToxCast/Tox21 assay endpoint 2247. A cell-free TR-FRET assay in which a
    GST-tagged TR-beta ligand-binding domain, a terbium-labelled anti-GST
    antibody and a fluorescein-labelled SRC-2 coactivator peptide together
    report coactivator recruitment by the receptor, with the signal normalized
    to DMSO-only wells for 0% and T3 wells for 100% activity. EPA annotates the
    intended target as human THRB, the format as cell-free, the function type
    as a ratio and the signal direction as loss, so a hit is a chemical that
    reduces recruitment.
  organism:
    preferred_term: human
    term:
      id: NCBITaxon:9606
      label: Homo sapiens
  culture_system: Cell-free TR-FRET reaction; no cultured cells
  publication: PMID:31566444
  modeled_mechanisms:
  - target: THRB Dominant-Negative Receptor Formation
    relationship: MEASURES
    fidelity: LOW
    model_scale: MOLECULAR
    description: >-
      The endpoint reads transcriptional output of TR-beta in the same
      direction the node's mechanism produces, so a hit is informative about
      the receptor's coactivator-recruitment capacity.
    limitations: >-
      The assay reads a wild-type receptor ligand-binding domain whose
      coactivator recruitment has been reduced by a chemical. The node names a
      heterozygous missense allele whose product keeps DNA binding and RXR
      heterodimerization while failing to release corepressor. Target gene and
      signal direction agree; the mechanism does not.
    readouts:
    - name: TR-FRET 520:495 coactivator-recruitment emission ratio
      target: THRB Dominant-Negative Receptor Formation
      direction: DECREASED
      interpretation: >-
        Less coactivator peptide recruited to the receptor gives less resonance
        energy transfer and so a lower emission ratio. This is the quantity the
        endpoint reports, and the direction EPA annotates as a loss signal.
      evidence:
      - reference: PMID:31566444
        reference_title: "Limited Chemical Structural Diversity Found to Modulate Thyroid Hormone Receptor in the Tox21 Chemical Library."
        supports: SUPPORT
        evidence_source: IN_VITRO
        snippet: "A time-resolved fluorescence resonance energy transfer (TR-FRET) signal was indicative of coactivator recruitment"
        explanation: >-
          States that the measured TR-FRET signal is the coactivator-recruitment
          readout this entry records.
    divergences:
    - divergence_type: CAUSE_UNREPRESENTED
      materiality: INVALIDATING
      description: >-
        The node's lesion is a heterozygous missense THRB allele. There is no
        allele in this assay: the reduction in coactivator recruitment is
        imposed pharmacologically on a recombinant wild-type ligand-binding
        domain.
    - divergence_type: BOUNDARY_OMISSION
      materiality: INVALIDATING
      description: >-
        The node's mechanism requires a co-expressed wild-type receptor to
        compete with, thyroid hormone response elements to occupy and an
        NCoR/SMRT corepressor complex to retain. The assay contains one
        receptor ligand-binding domain, a coactivator peptide and an antibody:
        no second allele, no DNA and no corepressor.
    evidence:
    - reference: PMID:31566444
      reference_title: "Limited Chemical Structural Diversity Found to Modulate Thyroid Hormone Receptor in the Tox21 Chemical Library."
      supports: SUPPORT
      evidence_source: IN_VITRO
      snippet: "were used to determine TR activity in a cell-free functional assay"
      explanation: >-
        Establishes that the endpoint is a cell-free biochemical measurement of
        receptor activity rather than a cellular or organismal model.
```

Four things about that block are worth reading closely.

**The vocabulary does fit, and it fits well.** `MEASURES` says the assay reads
the node without modelling the disease. `CAUSE_UNREPRESENTED` is defined as the
lesion not being encoded, with "the mechanism is imposed phenomenologically
instead of arising from the allele" — a taxonomy derived from the
computational-model caveats already in the corpus, extending here unchanged.
`BOUNDARY_OMISSION` carries the rest, and `ExperimentalReadout` takes the
measured quantity — the 520:495 emission ratio — with its direction, exactly as
it would for a readout of an organoid or an animal. #12858's claim that dismech
already has the words for this holds up.

**Both divergences come out `INVALIDATING`.** Neither is a caveat on an
otherwise usable link; each says on its own that the claim should not transfer.
The dominant-negative mechanism is a claim about two alleles competing in one
nucleus. No endpoint in the panel expresses a disease allele — ToxCast screens
chemicals against wild-type receptors — so the third node in the chain,
`Dominant-Negative Inhibition of Wild-Type Receptor Transcription`, is
unreachable from any of THRB's 13 endpoints, cell-based or not.

**The scale audit reports no gap, and that is not reassurance.** The link's
`model_scale` is `MOLECULAR` and the node's `biological_scale` is `MOLECULAR`,
so `just model-scale-audit` sees nothing to flag. CLAUDE.md's instruction to
read an aligned result as "no *scale* gap" and never as "good model" has a live
instance here.

**`ExperimentalModel` has little to say about this assay.** The class describes
a cultured system. #12858 proposes four correspondences onto it — `organism`,
`tissue`, `cellShortName` and the citation PMID — and for this endpoint two of
them carry nothing, because `tissue` and `cellShortName` are both `NA`.
`experimental_model_type` is not among those four and has no value that fits
either: a cell-free reaction falls to `OTHER`, which records nothing, and
#12858 already flags that 481 of the panel's endpoints are biochemical or
cell-free — a different 481 from the candidate count in the report's own
summary table, which happens to take the same value. Its sibling endpoint 2240,
`TOX21_TRB_BLA_Antagonist_Followup_ratio`, is the same receptor in the same
direction from the same paper, and is cell-based in HEK293T cells, so it fills
all four and types as `CELL_LINE`. Two endpoints a curator would reach for
together need different treatment — and the tissue the cell-based one records
is kidney, which appears nowhere in this disease.

### What it costs to say it twice

`ModelMechanismLink.target` resolves only within one disease file, and an
`ExperimentalModel` is nested inside one `Disease`. So the record above lives in
Generalized_Resistance_to_Thyroid_Hormone and nothing else in the repository
knows the endpoint exists.

The paralogs make the cost concrete. THRB has 13 endpoints and THRA has 13, and
**four are the same four**: `TOX21_TR_LUC_GH3_Agonist`,
`TOX21_TR_LUC_GH3_Antagonist` and their two followups each name THRA and THRB
together in rat GH3 pituitary cells, so a hit there does not say which paralog
it acted through. Those two dismech entries exist to separate the paralogs —
Generalized_Resistance_to_Thyroid_Hormone for THRB, and
Resistance_to_Thyroid_Hormone_Alpha, whose own trigger node is `THRA
Dominant-Negative Receptor Variant`. Writing a paralog-blind endpoint into both
means two records that each look paralog-specific, with no shared identity, and
nothing that could later correct them together.

Species compounds it. Of THRB's 13 endpoints, 11 name the human gene; two
(`ATG_zfTRb_XSP1` and `ATG_zfTRb_XSP2`) name zebrafish `thrb` while running in
human cells, so they join to this node only because the upper-cased symbol
collides.

Resistance_to_Thyroid_Hormone_Alpha already carries a real `ExperimentalModel`:
primary erythroid progenitors from 11 genotyped RTH-alpha patients, linked
`PARTIALLY_RECAPITULATES` at `HIGH` fidelity to the erythroid node. Put the
ToxCast record beside it and the class is being asked to hold two different
kinds of thing — a patient-derived culture carrying the patients' own variants,
and a purified receptor domain with a chemical on it.

**Nothing from this example is committed to `kb/`.** The block above validates
but every divergence on it is `INVALIDATING`, and whether a link like it belongs
in dismech at all is the next deliverable's question, not this one's.

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

Issue #12858 asks for more than the measurement and the example above. Each of
these is its own piece of work and none is started here:

- an evaluation of whether assay-to-node mappings should be added to dismech
  at all;
- an evaluation of the AOP-Wiki Key Event links the API itself publishes for
  some endpoints;
- the open questions the issue raises about endpoints without a gene target,
  non-cell-based assay formats, and the biological-process field.
