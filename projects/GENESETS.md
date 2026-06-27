---
title: Gene Sets
status: ACTIVE
description: >-
  How dismech references external gene sets (MSigDB/KEGG/WikiPathways/Hallmark/
  cell-type signatures) and their curated GO interpretations, and aligns a gene
  set's curated biological processes against a disease pathograph.
tags: [INFRASTRUCTURE, GENE_SETS, GO, ALIGNMENT]
diseases:
  - Asthma
  - Colon_Adenocarcinoma
  - Sickle_Cell_Disease
  - IDH_Mutant_AML
  - Alzheimer_Disease
  - Amyotrophic_Lateral_Sclerosis
  - Arrhythmogenic_Right_Ventricular_Cardiomyopathy
  - Basal_Cell_Carcinoma
  - Chronic_Myeloid_Leukemia
  - Dilated_Cardiomyopathy
  - MSI_High_Endometrial_Cancer
  - Huntington_Disease
  - Hypertrophic_Cardiomyopathy
  - Parkinsons_Disease
  - Rheumatoid_Arthritis
  - Small_Cell_Lung_Cancer
  - Type_2_Diabetes_Mellitus
  - Type_I_Diabetes
  - Cholera
  - 22q11.2_Deletion_Syndrome
  - Duchenne_Muscular_Dystrophy
  - Ebola_Virus_Disease_EVD
  - Familial_Chylomicronemia_Syndrome
  - Familial_Hypercholesterolemia
  - Fragile_X_Syndrome
  - HPV_Negative_Head_and_Neck_Cancer
  - Idiopathic_Pulmonary_Fibrosis
  - Non-Small_Cell_Lung_Cancer
  - Renal_Cell_Carcinoma
  - Systemic_Lupus_Erythematosus
---

# Gene Sets

dismech consumes curated gene sets and their GO interpretations from
[`monarch-initiative/genesets`](https://github.com/monarch-initiative/genesets)
(MSigDB/KEGG/WikiPathways/Hallmark pathways and cell-type signatures). Two things
work with them:

1. **Cite a gene set as evidence** — each set is a structured reference source
   (`MYGENESET:<id>`) cached as line-oriented markdown.
2. **Align a gene set's curated biological processes to a disease pathograph** —
   `just genesets-align` scores how well a disorder's curated mechanism covers the
   gene set's GO terms.

## `just` targets

| Target | What it does |
|---|---|
| `just genesets-refresh` | Fetch interpretation YAMLs (pinned commit) + mygeneset.info membership into `data/genesets/`. |
| `just genesets-rebuild` | (Re)write `references_cache/MYGENESET_*.md` (`--id KEGG_ASTHMA` to limit). |
| `just genesets-list` | List ingestable gene-set ids. |
| `just genesets-align <disease> <set>` | Compare one gene set's curated GO terms to a disorder's pathograph BPs. |
| `just genesets-align-all` | Catalog-wide BP-alignment audit (every disease-context set ↔ its disorder). |

## Structured source: `MYGENESET:`

`src/dismech/structured_sources/mygeneset.py` ingests **100** gene sets into
`references_cache/MYGENESET_<id>.md`. Identity is keyed on
[mygeneset.info](https://mygeneset.info): the reference id is `MYGENESET:<_id>`
(the bare set name, e.g. `KEGG_ASTHMA`). The pin lives in
`data/genesets/MANIFEST.yaml` (genesets repo commit + mygeneset/mygene base URLs);
`data/genesets/interpretations/` and `membership/` are fetched, not committed.

Each cache file has these sections, with every row a quotable evidence `snippet:`:

- **Description**, **Context** (disease/tissue `MONDO`/`UBERON`),
- **Curated GO interpretation** — `GO id | label | aspect | role | confidence`,
- **Members** — `symbol | hgnc:id` (NCBIGene→HGNC resolved via mygene.info;
  NCBIGene fallback only for loci with no HGNC),
- **Source** — genesets commit + mygeneset + upstream `gene_set_id` xref.

Citing a row as evidence (a gene-set row is a *lead*, not mechanism — back disease
claims with a primary PMID too):

```yaml
evidence:
- reference: MYGENESET:KEGG_ASTHMA
  supports: SUPPORT
  snippet: "GO:0045064 | T-helper 2 cell differentiation | biological_process | core_process | high"
  explanation: The curated KEGG_ASTHMA interpretation lists Th2 differentiation as a core process.
```

## The `gene_sets` slot

A `Disease` declares its gene sets via the `gene_sets` slot
(`GeneSetAssociation`: `gene_set` + `relationship` + `note`). This is the precise,
curated disease↔set link — membership and the GO interpretation stay in the cache
file, so the slot never re-duplicates genes.

```yaml
gene_sets:
- gene_set: MYGENESET:KEGG_ASTHMA          # → references_cache/MYGENESET_KEGG_ASTHMA.md
  relationship: CANONICAL_PATHWAY
  note: KEGG legacy asthma pathway; overlaps the Th2 + inflammatory arms.
```

`GeneSetRelationshipEnum`: `CANONICAL_PATHWAY`, `CELL_TYPE_SIGNATURE`,
`PERTURBATION_SIGNATURE`, `DISEASE_SIGNATURE`, `OTHER`.

**30 disorders** declare `gene_sets` (see the disease list above). Each declared
link is a precise, per-entry mapping — e.g. `KEGG_COLORECTAL_CANCER` is on
`Colon_Adenocarcinoma`, while metastasis/EMT-specific sets belong on the
metastatic entries.

## BP alignment

`src/dismech/genesets_align.py` compares a gene set's curated GO terms to a
disorder's `biological_processes` + `cellular_components` + `protein_complexes`,
matched over GO via OAK:

- **Match status**: `EXACT` and `DESCENDANT` (pathograph term is *more specific*)
  count as represented; `ANCESTOR` (pathograph has only a *more general* term)
  is shown but does **not** count.
- **Role-weighted**: corroboration is scored over the set's `core_process`/
  `core_component` BPs; `nonspecific`/`false_association` BPs are expected absent
  and only lint if they appear in the pathograph.
- **Output**: per-BP status, a corroboration fraction (core BPs represented), and
  the core-BP gap list.

`genesets-align-all` runs this across the catalog, preferring the explicit
`gene_sets` links (marked `declared`) and falling back to a one-disorder-per-MONDO
guess (marked `mondo?`) for sets no disorder declares. Recurring gaps it surfaces:
`MHC class II protein complex` (a GO cellular-component, modeled via CL in dismech)
across Asthma/RA/T1D; `mitochondrion` + `neuron apoptotic process` across
neurodegeneration; `regulation of cell population proliferation` across the cancer
pathways.

## Coverage

100 ingested sets; 56 are disease-context. 30 are wired to a disorder via
`gene_sets`. The rest either have no dismech disorder yet, or are cell-type /
process / signature sets that attach to phenotypes or modules rather than a single
disease. The IL6→JAK/STAT MEDICUS set is a signaling pathway, not a disease — it
belongs on a mechanism module.
