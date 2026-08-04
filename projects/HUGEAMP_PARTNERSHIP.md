---
title: HuGeAMP / Knowledge Portal Network Partnership
status: PROPOSED
description: Assess and pursue integration with the Human Genetics Amplifier (HuGeAMP) platform and the Knowledge Portal Network (Broad Institute / Flannick lab), an open, API-accessible aggregation of human genetic association results across 26 disease portals and ~1,700 phenotypes. HuGeAMP supplies statistical gene-trait genetic evidence at scale; dismech supplies ontology-grounded causal mechanism. The two are complementary and neither currently has what the other has.
tags:
- collaboration
- genetics
- gwas
- integration
---

# HuGeAMP / Knowledge Portal Network Partnership

## Overview

**HuGeAMP** (Human Genetics Amplifier) is the software platform behind the
**Knowledge Portal Network (KPN)** — an ecosystem of disease-specific genetics
portals developed at the Broad Institute (Jason Flannick lab), originally funded
through the Accelerating Medicines Partnership in Type 2 Diabetes (AMP-T2D).

- Portal network entry point: <https://hugeamp.org/> and <https://kp4cd.org/>
- **Open REST API**: <https://bioindex.hugeamp.org/> — no key, no auth
- Bulk data: `arn:aws:s3:::dig-open-bottom-line-analysis` (AWS Open Data registry;
  terms at <https://a2f.hugeamp.org/policies.html>)

The strategic fit is clean and non-overlapping:

| | HuGeAMP / KPN | dismech |
|---|---|---|
| Core claim | *Which* genes/variants **associate** with a trait | *How* a lesion **causes** the disease |
| Evidence type | Statistical (GWAS, burden, fine-mapping, LDSC) | Curated, snippet-verified literature |
| Granularity | Variant → gene → trait | Gene → pathophysiology chain → phenotype |
| Semantics | Internal phenotype codes, free-text descriptions | MONDO / HP / GO / CL / CHEBI / NCIT |
| Scale | ~1,700 phenotypes, hundreds of datasets | 1,829 disorders, 120 modules, 56 groupings |
| Weakness | No mechanism, no ontology grounding | Thin common-variant / polygenic evidence |

HuGeAMP answers "what associates"; dismech answers "why it matters and through
what mechanism." Each is the other's stated weakness.

## Verified platform survey (2026-08-04)

All figures below were confirmed by direct API probe, not from documentation.

### API is fully open and current

```bash
curl https://bioindex.hugeamp.org/api/bio/indexes          # 122 indexes
curl https://bioindex.hugeamp.org/api/portal/groups        # 26 portals
curl https://bioindex.hugeamp.org/api/portal/phenotypes    # 1,700 phenotypes
curl https://bioindex.hugeamp.org/api/portal/datasets      # dataset metadata + PMIDs
curl "https://bioindex.hugeamp.org/api/bio/query/<index>?q=<key>&limit=N"
```

Most indexes carry 2026-05 build timestamps — the resource is actively maintained.

### 26 portals

`md` (Common Metabolic Diseases, the umbrella), `t2d`, `t1d`, `cvd`, `cd`
(cerebrovascular), `sleep`, `lung`, `msk` (musculoskeletal), `kidney`, `neph`
(nephrotic syndrome), `ndkp` (neurodegenerative), `als`, `ocular`,
`vision_genomics`, `autoimmune`, `skin`, `cancer`, `reproductive`, `aging`,
`v2f` (variant-to-function), `a2f` (association-to-function), `nage`
(non-additive genetic effects), `aggregator` (BCH CRDC), `radiant`, `sysbio_kp`,
`private_sleep`.

### Indexes most relevant to dismech

| Index | Key | Payload | dismech use |
|---|---|---|---|
| `huge` | gene | HuGE score, `bf_common`, `bf_rare` per gene-phenotype | Gene-level genetic-evidence strength, ClinGen-validity-adjacent |
| `huge-phenotype` | phenotype | same, phenotype-first | Rank candidate genes for a disorder entry |
| `gene-finder` | phenotype | gene, pValue, zStat, subjects, ancestry | Populate `genetic:` with `SUSCEPTIBILITY` loci |
| `genetic-correlation` | phenotype | `rg`, `stdErr`, `pValue` vs other phenotypes | **Comorbidity shared-etiology signal** (see below) |
| `pigean-*` | phenotype/gene | Gene-set and latent-factor enrichment | Cross-check pathophysiology node gene sets |
| `gene-program-*` | tissue/cell_type | Gene programs per cell state | Bridge to `GWAS_MECHANISMS` (Ota et al.) work |
| `credible-sets`, `credible-variants` | phenotype | Fine-mapped credible sets | Variant-level provenance for a curated risk gene |
| `partitioned-heritability-tissue` | phenotype | Tissue/annotation heritability enrichment | Corroborate the cell types on a pathophysiology node |
| `global-enrichment` | phenotype | Epigenomic annotation enrichment | Same |
| `phewas-associations` | variant | Cross-trait associations for one variant | Pleiotropy → comorbidity leads |

Worked probes:

```
huge?q=PCSK9      → PCSK9/ApoB huge=121800 (bf_common 350, bf_rare 348)
                     PCSK9/MI   huge=1669.4
gene-finder?q=T2D → TCF7L2 p=5e-324 (n=1,927,558); KCNQ1 p=3.98e-267
genetic-correlation?q=T2D
                  → DiabeticRetino rg=0.936±0.018; HBA1C rg=0.936±0.015;
                    PolyneuropathyDM rg=0.884±0.023
```

## The gaps each side fills

### What HuGeAMP fills for dismech

dismech's common-variant/polygenic evidence is thin relative to its Mendelian coverage:

- **90 of 1,829** disorder files use `RISK_FACTOR` or `SUSCEPTIBILITY` gene typing
- **3 of 1,829** carry a `data_type: GWAS` dataset

The `Genetic.relationship_type` enum already has `SUSCEPTIBILITY` defined as
"polygenic susceptibility loci such as GWAS hits" — the slot exists and is
almost unused. HuGeAMP is the obvious systematic filler, and it is already
meta-analyzed and effect-sized, so it beats citing individual GWAS papers.

### What dismech fills for HuGeAMP

**HuGeAMP phenotypes carry no ontology identifiers.** Every one of the 1,700
phenotype records has exactly four fields: `name`, `description`, `group`,
`dichotomous`. The only exception is the `NEPHBCH` group (Boston Children's
aggregation), where **73** phenotypes are already keyed by HPO ID
(`HP-0007018`, `HP-0002110`, …) — proving the platform accepts HPO-shaped
identifiers, just not systematically.

853 of the 1,700 phenotypes are dichotomous (disease-like) and are the natural
MONDO-mapping targets; the other 847 are continuous traits (HP / measurement
terms, or out of scope).

A naive exact-string match of dismech disorder names against phenotype
descriptions already yields **51** hits (`Asthma`↔`Asthma`, `Gout`↔`Gout`,
`Myocardial_Infarction`↔`MI`, `Idiopathic_Pulmonary_Fibrosis`↔`IPF`,
`Membranous_Nephropathy`↔`MN`, …). Synonym-aware matching over MONDO labels and
exact synonyms would plausibly reach several hundred. **A curated
HuGeAMP-phenotype → MONDO/HP mapping table is the single highest-value thing
dismech can hand them**, and it is a byproduct of work dismech wants anyway.

The mechanism layer is the second thing: HuGeAMP portals render gene-trait
association tables with no mechanistic annotation. dismech pathographs are
exactly the "so what does this gene *do* in this disease" layer their gene pages
lack.

## Integration options

### Tier 1 — Unilateral, no partnership needed (open API, do it now)

1. **`HugeAmpSource` structured reference source.** Follows the existing
   `src/dismech/structured_sources/` framework (`icees.py` is the closest
   template — same "pinned bulk/API pull → deterministic line-oriented markdown
   in `references_cache/` → curator quotes a table row as an evidence snippet"
   shape). Proposed prefix `HUGEAMP:<index>_<key>`, e.g.
   `HUGEAMP:huge_PCSK9`. Cache body carries a `## Gene-trait genetic evidence`
   markdown table whose rows are stable quotable substrings.
2. **Genetic-correlation signals on comorbidity entries.** `kb/comorbidities/`
   currently sources EHR co-occurrence only (COHD, ICEES, Disease Trajectories) —
   all of which measure *observed* co-occurrence and cannot separate shared
   genetic etiology from causal sequence or ascertainment bias. HuGeAMP `rg`
   values are a mechanistically **different and complementary** line of evidence
   for the same disease pairs. Requires two small enum additions:
   - `AssociationSignalSourceEnum`: `+ HUGEAMP`
   - `AssociationSignalMethodEnum`: `+ GENETIC_CORRELATION`
   - `AssociationMetricTypeEnum`: `+ RG` (genetic correlation coefficient)

   The `AssociationSignal` class otherwise already fits: `metric_value` = rg,
   `p_value`, and `population` = ancestry + project.
3. **Susceptibility-gene backfill.** For each dismech disorder mappable to a
   HuGeAMP phenotype, pull top `gene-finder` / `huge-phenotype` hits and propose
   `genetic:` entries with `relationship_type: SUSCEPTIBILITY`. Must be
   curator-reviewed, not bulk-committed (see Caveats).
4. **Dataset provenance.** `/api/portal/datasets` returns PMIDs per dataset —
   directly usable to populate dismech `datasets:` blocks with
   `data_type: GWAS` and a real `publication:`.

### Tier 2 — Requires contact, low commitment

5. **Ship them the phenotype→MONDO/HP mapping table** as an open TSV. Concrete,
   immediately useful to them, cheap for dismech, and establishes the
   relationship without either side taking on a dependency.
6. **Reciprocal deep links.** dismech disorder pages link out to the matching
   KP phenotype page; KP gene/phenotype pages link to the dismech pathograph.
   The `src/dismech/render.py` external-browser link machinery already does this
   pattern for HPO JAX / Monarch / OLS.

### Tier 3 — Genuine collaboration

7. **Mechanism annotation layer for KP gene pages.** Serve dismech pathophysiology
   nodes as the "what does this gene do here" panel on KP gene-phenotype pages.
8. **Genetics-informed pathograph validation.** Use `partitioned-heritability-tissue`
   and `global-enrichment` to test whether the cell types curated on a
   pathophysiology node are the tissues where that trait's heritability is
   actually enriched — a falsifiable, automatable QC signal on curated mechanism.
   This is the most scientifically interesting item on the list.
9. **PIGEAN / gene-program bridge.** Their `pigean-*` and `gene-program-*`
   indexes are latent-factor gene-set decompositions of trait genetics — the same
   gene→program→trait abstraction as
   [`projects/GWAS_MECHANISMS.md`](GWAS_MECHANISMS.md) (Ota et al., Nature 2025).
   That project already needs a program-to-mechanism mapping layer; HuGeAMP is a
   second, independently derived source of programs to validate against.

## Caveats and risks

- **Association is not mechanism.** A HuGE score or a GWAS p-value supports a
  `SUSCEPTIBILITY` gene-disease relationship; it does **not** support any
  pathophysiology causal edge. Nothing from HuGeAMP may be curated as a
  `downstream:` edge without independent mechanistic literature. This is the
  main way a bulk import could damage the KB.
- **Statistical results are not snippet-verifiable in the usual way.** The
  dismech evidence contract (exact quote from an abstract) does not apply to a
  computed table row. The structured-source pattern (ORPHA/ICEES/CGGV) already
  solves this — the quotable unit is a deterministic cache-file table row — so
  `HugeAmpSource` must follow it rather than inventing a new evidence shape.
- **Phenotype namespace is unstable and undocumented.** Names like `BS`,
  `HP-0007018`, `SKIN_Eczema`, `T2D` follow no single convention and are
  portal-local. Any mapping table needs a version pin and a refresh check
  (`data/hugeamp/MANIFEST.yaml`, matching the Orphadata pattern).
- **`rg` between a disease and its own complication is near-tautological.**
  T2D↔DiabeticRetino rg=0.936 reflects that one causes the other, not shared
  upstream etiology. Curators must not read every high `rg` as evidence of a
  shared mechanism.
- **Licensing needs confirmation before any redistribution.** The AWS bucket is
  Open Data but terms live at <https://a2f.hugeamp.org/policies.html>; per-dataset
  `access` fields exist in the dataset metadata (some are not "Open access").
  Confirm before committing cache files.
- **Ancestry.** Most bottom-line results are `Mixed` or European-dominant.
  Curated `population:` fields must say so rather than implying generality.

## Cross-project synergies

- [`GWAS_MECHANISMS.md`](GWAS_MECHANISMS.md) — direct overlap; HuGeAMP is a
  second program-level source alongside the Ota/Pritchard framework, and its
  hematological phenotype coverage matches that project's disease list.
- [`MONDO_EHR_MAPPINGS.md`](MONDO_EHR_MAPPINGS.md) — same mapping discipline,
  different target vocabulary; tooling should be shared.
- [`COMORBIDITIES.md`](COMORBIDITIES.md) — genetic correlation as a third
  evidence stream beside COHD/ICEES/Disease Trajectories.
- [`ORGAN_FIBROSIS_COLLABORATION.md`](ORGAN_FIBROSIS_COLLABORATION.md) —
  precedent for the external-resource collaboration shape.

## Recommended first move

Tier 1 items 1–2 are the right pilot: they are unilateral, use only the open
API, exercise an existing framework, and produce the phenotype mapping table as
a byproduct — which is the artifact worth opening a conversation with. Approach
the Flannick lab with the mapping in hand rather than with a proposal.

## Contact / Collaboration

- Knowledge Portal Network: <https://kp4cd.org/>
- Programmatic access docs: <https://www.kp4cd.org/node/642>
- Maintainer: Jason Flannick lab, Broad Institute of MIT and Harvard
- AMP-T2D / AMP CMD consortium governance applies to some datasets

## Notes

### 2026-08-04 (Project creation)

Created from a platform survey. All API figures (122 indexes, 26 portals, 1,700
phenotypes, 73 HP-coded, 51 exact name matches, 90/1,829 susceptibility files,
3/1,829 GWAS datasets) were verified by direct probe against
`bioindex.hugeamp.org` and the local KB on this date. No contact with the
Flannick lab has been made; the partnership framing here is an internal
assessment, not an agreed plan.
