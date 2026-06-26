---
title: Gene Sets ↔ dismech Integration
status: IN_PROGRESS
description: >-
  Plan for sourcing named gene-set curation (MSigDB/KEGG/Hallmark/cell-type
  signatures) and their curated GO interpretations from the monarch-initiative/genesets
  repo, and wiring two-way feedback with dismech disease pathographs.
tags: [INFRASTRUCTURE, CROSS_REPO, GENE_SETS, GO, ENRICHMENT]
diseases:
  - Asthma
  - Parkinsons_Disease
  - Systemic_Lupus_Erythematosus
  - Colon_Adenocarcinoma
  - Huntington_Disease
  - Amyotrophic_Lateral_Sclerosis
  - Graves_Disease
  - Hashimotos_Thyroiditis
  - Type_I_Diabetes
  - Dravet_syndrome
---

# Gene Sets ↔ dismech Integration

> **Status:** import **+ both-way tooling built**. The gene-set GO-interpretation
> curation lives in **[`monarch-initiative/genesets`](https://github.com/monarch-initiative/genesets)**
> (formerly `cmungall/genesets-rs`; merged to `main`, now **100** curated sets).
> dismech's duplicated `genesets/` dir was **retired**; gene sets are ingested as a
> structured reference source (`MYGENESET:`, evidence-validated — see
> [Implemented](#implemented-the-mygeneset-structured-source)), and the
> [BP aligner](#built-just-genesets-align-disease-set) scores each disease's
> pathograph against its set's curated BPs (per-disease + `genesets-align-all`).
> Remaining: the optional `gene_sets` schema element + confidence weighting.

## TL;DR

We used to keep a small pile of raw gene sets **inside** dismech (`genesets/`),
while the richer **GO-interpretation** layer lives **in
`monarch-initiative/genesets`**. These are the same underlying objects viewed
from two angles. Decisions taken:

1. **`monarch-initiative/genesets` is the single source of truth** for named,
   reusable gene sets and their curated GO interpretations. dismech's duplicated
   `genesets/` membership dir is **retired** (done, this branch).
2. **dismech consumes gene-set interpretations as a structured reference source**
   (a new `MYGENESET:` cache prefix, exactly like `ORPHA:`, `CGGV:`, `CGDS:`), so
   a disease curator can cite a gene set and quote its curated GO interpretation
   as a *lead*. Identifier scheme keyed on **mygeneset.info** — see
   [Identifier / prefix decision](#identifier--prefix-decision).
3. **Close the loop both directions:** dismech disease pathographs are a
   hand-curated gold standard of "which GO processes matter for disease X";
   gene-set GO interpretations are a hand-curated gold standard of "which GO
   processes a gene set means." Where a disease has a matching pathway gene set
   (e.g. Asthma ↔ `KEGG_ASTHMA`), each can audit and enrich the other.

## What exists today

### A. dismech `genesets/` — raw membership (RETIRED)

dismech *used to* hold one directory per MSigDB set under `genesets/<NAME>/`
(`DESCRIPTION.md` + `genes.csv` + `PAPER.md`), membership-only and never wired
into `src/`/`scripts/`/`justfile`. **These 13 dirs are now deleted** —
membership is owned by `monarch-initiative/genesets`. The 13 sets were:
Alzheimer's, Asthma, Autoimmune Thyroid, Colorectal Cancer, Graft-vs-Host,
Huntington's, IL6→JAK/STAT (MEDICUS), Parkinson's, Prion, SLE, Type I Diabetes,
ALS (WP), Dravet (WP). See [Coverage backlog](#coverage-backlog) for which of
these still need a GO interpretation upstream.

### B. `monarch-initiative/genesets` — curated GO interpretation layer

A LinkML curation system (mirroring dismech's own validation stack) that records
the "correct/reasonable" GO interpretation of a gene set:

- `curation/schema/genesets_interpretation.yaml` — `GeneSetInterpretation` with
  an ontology-agnostic biological context (`cell_type`, `tissue`, `disease`,
  `chemical`, `phenotype`) plus a list of `TermAssociation`.
- `curation/genesets/<SOURCE>_<CONTEXT>.yaml` — e.g. `KEGG_ASTHMA.yaml`.
- Each `TermAssociation` carries a GO term + **role** drawn from a 6-value
  vocabulary, plus `confidence`, `specificity`, optional enrichment stats, and
  reference-validated literature evidence.
- Three-stage validation identical in spirit to dismech: `linkml-validate`,
  `linkml-term-validator` (GO/CL/UBERON/MONDO/PR vs OAK), `linkml-reference-validator`
  (snippets must be verbatim substrings).
- A `genesets-workflows curate` CLI (`draft` → `validate` → `report` with
  precision/recall/F1) — i.e. it's explicitly **evaluation-first**.

### C. dismech disease pathographs — the mechanism graph

`kb/disorders/*.yaml` (rendered to `pathographs/MONDO_*.json`) already encode,
per disease, a curated causal graph of `pathophysiology` nodes, each carrying:

- `biological_processes` → GO terms (Asthma has GO:0042092 type 2 immune
  response, GO:0045064 Th2 differentiation, GO:0006939 smooth-muscle
  contraction, GO:0070254 mucus secretion, …),
- `cell_types` → CL terms,
- gene terms → HGNC (the Th2 node: IL4, IL13, IL4R, STAT6, IL5, GATA3),
- evidence → reference-validated PMIDs.

So dismech *already curates, per disease, the GO processes that matter* — just
not as a "gene set" object and not benchmarked against MSigDB pathways.

## The core insight (why this is two-way)

A gene set like `KEGG_ASTHMA` is just a bag of genes. `genesets-rs` answers
*"what does this bag mean in GO terms?"*. dismech's Asthma pathograph answers
*"what GO processes drive this disease, with evidence and causal structure?"*.
**For any disease that has a matching pathway gene set, these two answers should
substantially agree** — and the disagreements are the valuable part:

- **GO terms in the gene-set interpretation but missing from the pathograph**
  → candidate `biological_processes` (or whole pathophysiology nodes) dismech
  should add.
- **GO terms central in the pathograph but absent from the gene-set
  interpretation** → either the gene set is incomplete, or the process is
  disease-specific context the generic pathway omits (still useful signal).
- **`false_association` terms in the interpretation** → an explicit denylist
  dismech can use to avoid over-claiming.

## Proposed architecture

```
                 genesets-rs (source of truth)
   ┌───────────────────────────────────────────────────────┐
   │  membership:   curation/genesets/<SET>/genes.csv        │
   │  interpretation: curation/genesets/<SET>.yaml           │
   │     GeneSetInterpretation                               │
   │       context: {disease, tissue, cell_type, ...}        │
   │       term_associations:                                │
   │         - GO:xxxx  role=core_process  conf=high  PMID   │
   │  tooling:  draft / validate / report (P/R/F1)           │
   └───────────────┬───────────────────────────────────────┘
                   │  (1) export deterministic cache files
                   ▼
   references_cache/MSIGDB_KEGG_ASTHMA.md   ← dismech structured source
                   │  (2) curator cites GENESET / MSIGDB ref as a *lead*
                   ▼
   kb/disorders/Asthma.yaml  →  pathographs/MONDO_0004979.json
                   │  (3) export disease GO/gene set back out
                   ▼
   dismech "disease gene set" + curated GO list
                   │  (4) feeds genesets-rs eval benchmark & enrichment
                   └──────────────► back to genesets-rs
```

### Layer 1 — membership (retire the dismech copy)

Move/keep raw gene-set membership only in `genesets-rs`. dismech's `genesets/`
directory becomes redundant; either delete it or replace it with a pinned
pointer (a manifest of `reference_id` + source URL + sha) so we don't maintain
two diverging copies of the same MSigDB lists. *(This is a structural decision —
see Open Decisions.)*

### Layer 2 — GO interpretation (owned by genesets-rs)

The `GeneSetInterpretation` files (PR #3) are authored and validated in
`genesets-rs`. dismech never edits them; it only reads them.

### Layer 3 — dismech consumption (new structured source)

Add a `MSigDB`/`GeneSet` structured source under
`src/dismech/structured_sources/` (subclass `StructuredSource`, same pattern as
`OrphanetSource`/`ClinGenSource`). It ingests the genesets-rs interpretation
files and emits deterministic line-oriented `references_cache/MSIGDB_*.md` files
with quotable rows, e.g.:

```
## Gene set
| KEGG_ASTHMA | C2:CP:KEGG_LEGACY | hsa05310 | 30 genes |

## Curated GO interpretation
| GO:0042092 | type 2 immune response | core_process | high |
| GO:0019886 | antigen processing and presentation of exogenous peptide antigen via MHC class II | core_process | high |
| GO:0006939 | smooth muscle contraction | nonspecific | low |

## Members
| FCER1A | MS4A2 | IL4 | IL5 | IL13 | CCL11 | TNF | CD40 | ... |
```

A disease curator can then cite the gene set as a normal evidence reference and
quote a row, *as a lead that still needs primary-literature backing* (gene-set
membership is not, by itself, mechanistic evidence for a disease claim — treat
it like a Deep-Research lead under the existing anti-hallucination SOP).

## Two-way feedback flows

| # | Direction | Input | Output | Mechanism |
|---|-----------|-------|--------|-----------|
| 1 | genesets → dismech | `KEGG_ASTHMA` GO interpretation | candidate `biological_processes` / missing pathophysiology nodes for `Asthma` | diff curated GO list vs pathograph GO terms |
| 2 | genesets → dismech | `false_association` terms | denylist to avoid over-claiming | filter at curation/review time |
| 3 | dismech → genesets | per-disease curated GO list + evidence | gold-standard eval set for `genesets-rs report` (P/R/F1) | export disease "GO truth" |
| 4 | dismech → genesets | genes attached to pathophysiology nodes | a *disease-mechanism gene set* (alternative to KEGG) | export union of node gene_terms |
| 5 | genesets → dismech | enrichment of a dismech disease gene set | suggested GO terms ranked by role/confidence | run `genesets-rs` enrichment on flow-4 output |
| 6 | dismech → genesets | causal edges between pathophysiology nodes | which GO processes are *upstream/downstream* | richer than flat gene-set → GO mapping |

Flows 3–4 are the payoff the genesets-rs PR is explicitly asking for: it wants an
"evaluation-first benchmark," and dismech's hand-curated, evidence-backed,
causally-structured disease pathographs are a *better* gold standard than a flat
gene list.

## Data-model crosswalk

| genesets-rs `TermAssociation.role` | dismech analogue | Notes |
|---|---|---|
| `core_process` | a `biological_processes` GO term on a central pathophysiology node | the heart of the pathograph |
| `core_component` | (no direct slot) cell-type / cellular-component context | dismech uses CL `cell_types`; GO CC is rarely modeled |
| `supporting_process` | GO term on a peripheral / modifier node | e.g. the protective SIRT1 node |
| `marker_driven_plausible` | gene present but mechanism unproven | candidate, needs evidence before promotion |
| `nonspecific` | omit from pathograph | housekeeping / generic |
| `false_association` | denylist; never add | actively useful negative signal |

Note the **axes differ**: the genesets `role` is a *relevance/centrality* axis;
dismech's `modifier` (INCREASED/DECREASED) is a *direction* axis, and dismech
encodes relevance *structurally* (a GO term is in the graph iff a curator judged
it relevant, with evidence). A clean mapping would let `role` seed whether a GO
term even enters the pathograph, while dismech adds direction + evidence +
causal position on top.

## Worked example: `KEGG_ASTHMA` vs the Asthma pathograph

**`KEGG_ASTHMA` members (30):** FCER1A, MS4A2, FCER1G, HLA-DMA/DMB/DOA/DOB/
DPA1/DPB1/DQA1/DQA2/DQB1/DRA/DRB1/DRB3/DRB4/DRB5, IL3, IL4, IL5, IL9, IL10,
IL13, PRG2, RNASE3, CCL11, TNF, EPX, CD40, CD40LG.

**Asthma pathograph nodes (`pathographs/MONDO_0004979.json`):** Airway
Inflammation, Type 2 Immune Response/Th2 Signaling (IL4, IL13, IL4R, STAT6, IL5,
GATA3), Bronchoconstriction, Mucus Overproduction, Airway Remodeling,
SIRT1-mediated protective deacetylation, rhinovirus-inception node.

**Gap analysis (flow 1) — what the gene set has that the pathograph lacks:**

- **Antigen presentation (MHC class II):** the entire `HLA-D*` block →
  GO:0019886 "antigen processing and presentation … via MHC class II". dismech's
  Asthma graph has no antigen-presentation / dendritic-cell-priming node. **Add
  one.**
- **FcεRI / mast-cell & basophil degranulation:** FCER1A, MS4A2 (FcεRIβ),
  FCER1G → IgE high-affinity receptor signaling and degranulation. dismech notes
  IgE and mast cells but has no explicit FcεRI signaling/degranulation node.
- **Eosinophil effector granule proteins:** PRG2 (MBP), EPX, RNASE3 (ECP),
  CCL11 (eotaxin) → eosinophil recruitment + degranulation as a distinct
  effector node, currently implicit.
- **CD40/CD40LG costimulation** and **IL-10** (regulatory) — not modeled.

**Reverse gap (flow 3) — what the pathograph has that the gene set lacks:**
airway remodeling (GO:0048771), mucus/goblet metaplasia (GO:0070254),
bronchoconstriction (GO:0006939), the SIRT1 protective arm, rhinovirus inception.
These are disease-context processes the generic KEGG pathway omits → dismech is
*richer* here, and these become "expected-miss" cases when scoring enrichment.

This single example shows the value in both directions: KEGG_ASTHMA would prompt
3–4 concrete new pathophysiology nodes in dismech, while the Asthma pathograph
would tell genesets-rs which asthma-relevant processes *no flat gene set can be
expected to recover*.

## Worked examples: the other four disease sets

I pulled the four remaining disease interpretations from PR #3
(`feat/curate-genesets`) and diffed each against the matching dismech entry.
Legend: **✓** dismech has the same/child GO term; **~** dismech has a related
sibling term; **✗** genuine gap (add to dismech); **omit-OK** = genesets tagged
it `nonspecific`/marker and dismech correctly does *not* model it.

### Cross-cutting findings (more useful than any single disease)

1. **The `nonspecific` role is a validated denylist.** `GO:0006412 translation`
   is tagged `nonspecific` in **all five** interpretations, and dismech's five
   matching entries **never** include it. This is direct evidence for feedback
   flow #2: genesets-rs's `nonspecific`/`false_association` roles line up with
   exactly what dismech curators already omit by hand. A `nonspecific`/`false_*`
   term appearing in a dismech pathograph would be a useful lint signal.
2. **`Colon_Adenocarcinoma` is the highest-value target.** The dismech CRC entry
   is a 6-node stub with **zero** `biological_processes` GO terms (it names Wnt/
   APC only in prose). `KEGG_COLORECTAL_CANCER`'s interpretation (Wnt, regulation
   of proliferation, MAPK, cell migration) is a ready-made scaffold — flow 1 pays
   off most where dismech is thinnest.
3. **Curation divergence worth a decision: neuron death.** genesets models
   neurodegenerative neuron loss as `GO:0051402 neuron apoptotic process`
   (AD + PD, `core`), whereas dismech PD models it as `GO:0097707 ferroptosis`
   and avoids generic apoptosis. Not obviously a "gap" — possibly dismech being
   more specific/current. The diff tool must treat parent/child and
   mechanism-substitution as *reconcile*, not *missing*.

### KEGG_PARKINSONS_DISEASE → `Parkinsons_Disease` (MONDO:0005180)

| genesets term | role | dismech |
|---|---|---|
| GO:0042416 dopamine biosynthetic process | core | ✓ present |
| GO:0006119 oxidative phosphorylation | core | ✗ **gap** (dismech has GO:0007005 mitochondrion organization, not OXPHOS) |
| GO:0006511 ubiquitin-dependent protein catabolic process | core | ✗ **gap** (PARK2/PINK1/PRKN are curated as *genes*, but no proteasome/mitophagy GO process) |
| GO:0005739 mitochondrion (CC) | core_component | ~ BP analogue only |
| GO:0051402 neuron apoptotic process | core | ~ dismech uses GO:0097707 ferroptosis |
| GO:0006915 apoptotic process | supporting | ~ ferroptosis |
| GO:0006412 translation | nonspecific | omit-OK |

**Actionable:** add OXPHOS (`GO:0006119`) and ubiquitin-proteasome/mitophagy
(`GO:0006511`/`GO:0000422`) to the *Mitochondrial Dysfunction* /
*Autophagy-Lysosome* nodes — strongly justified since PINK1/PRKN are already
genes there. dismech is otherwise far richer (α-synuclein inclusion bodies,
gut-brain seeding, complement, iron/ferroptosis, BBB).

### KEGG_TYPE_I_DIABETES_MELLITUS → `Type_I_Diabetes` (MONDO:0005147)

| genesets term | role | dismech |
|---|---|---|
| GO:0001913 T cell mediated cytotoxicity | core | ✓ present |
| GO:0006915 apoptotic process | supporting | ✓ present |
| GO:0019882 antigen processing and presentation | core | ~ dismech has **MHC class I** child GO:0002474 only |
| GO:0042613 MHC class II protein complex (CC) | core_component | ✗ **gap** (HLA-DQ2/DQ8 are curated genes, but no MHC-II GO term) |
| GO:0006955 immune response | supporting | ~ GO:0002250 adaptive immune response |
| GO:0030073 insulin secretion | marker_driven_plausible | ✗ minor (descriptive *Insulin Deficiency* node, no GO term) |
| GO:0006412 translation | nonspecific | omit-OK |

**Actionable:** add **MHC class II** antigen presentation (`GO:0019886`) — dismech
annotates only MHC-I despite HLA-DQ (class II) being its lead susceptibility
genes. Otherwise strong agreement; dismech adds type-I-IFN, dendritic-cell
migration, ER stress, viral defense.

### KEGG_ALZHEIMERS_DISEASE → `Alzheimer_Disease` (MONDO:0004975)

| genesets term | role | dismech |
|---|---|---|
| GO:0042987 amyloid precursor protein catabolic process | core | ✓ GO:0042982 APP metabolic + GO:0034205 amyloid-β formation |
| GO:0005739 mitochondrion | core_component | ✓ present |
| GO:0006119 oxidative phosphorylation | core | ~ GO:0022904 respiratory electron transport chain |
| GO:0051402 neuron apoptotic process | core | ✗ gap (but see divergence note) |
| GO:0006816 calcium ion transport | supporting | ✗ minor gap |
| GO:0006915 apoptotic process | supporting | ✗ |
| GO:0006412 translation | nonspecific | omit-OK |

**Actionable:** little — dismech AD is already richer (NLRP3 inflammasome, tau/
microtubule depolymerization, HSV-1 reactivation, neuroinflammation, BBB,
synaptic). Only modest adds (explicit neuronal Ca²⁺ transport).

### KEGG_COLORECTAL_CANCER → `Colon_Adenocarcinoma` (MONDO:0005575)

| genesets term | role | dismech |
|---|---|---|
| GO:0016055 Wnt signaling pathway | core | ✗ **gap** (Wnt/APC in prose only, no GO term) |
| GO:0042127 regulation of cell population proliferation | core | ✗ **gap** |
| GO:0000165 MAPK cascade | supporting | ✗ gap |
| GO:0016477 cell migration | supporting | ✗ gap |
| GO:0006915 apoptotic process | supporting | ✗ gap |
| GO:0006412 translation | nonspecific | omit-OK |

**Actionable:** the whole interpretation is a scaffold for the missing
`biological_processes` of a stub entry. (Subtype entries
`BRAF_V600E_Mutant_Colorectal_Cancer` (7 GO), `MSI_High_Colorectal_Cancer` (4),
`Metastatic_Colorectal_Cancer` (7) are better annotated — the generic base entry
is the one to enrich.)

## Identifier / prefix decision

**Source of identity = [mygeneset.info](https://mygeneset.info)** (the upstream
aggregator: MSigDB, GO, KEGG, Reactome, WikiPathways, DO, CTD, user sets …).
mygeneset's `_id` is the bare set name with a separate `source` field — e.g.
`{_id: KEGG_ASTHMA, source: msigdb}`, or the pathological
`{_id: TSANG_PBMC_FLUVIRIN_..._POSITIVE, source: msigdb}`.

**Decision:** adopt a single generic structured-source prefix **`MYGENESET:`**,
local-id = the mygeneset `_id` **verbatim** (`MYGENESET:KEGG_ASTHMA`,
`MYGENESET:TSANG_PBMC_..._POSITIVE`). One prefix then covers *anything* in
mygeneset.info, not just MSigDB. Rationale + handling of the "crazy IDs":

- **Long / unusual ids are fine in the CURIE.** dismech already cites long
  structured ids (`CGGV:assertion_<uuid>-<timestamp>`). The reference_id stays
  the exact `MYGENESET:<_id>`.
- **Cache filename uses a safe encoding.** `references_cache/MYGENESET_<id>.md`
  where `<id>` is the `_id` with non-`[A-Za-z0-9_]` chars replaced. For ids that
  are too long (> ~180 chars) or collide after sanitizing, fall back to a
  content-addressed name `MYGENESET_<sha1(_id)[:16]>.md`. The exact CURIE always
  lives in the cache **frontmatter** (`reference_id:`), so the filename never
  needs to be human-perfect — the dismech cache contract maps filename↔id via
  frontmatter, exactly as for `CGGV_*`.
- **Version lives in metadata, not the id.** mygeneset `_id` is version-less; pin
  `source` + `msigdb_release` (`v2025.1.Hs`) in the cache body for deterministic
  CI, not in the CURIE.
- **Carry `source` to disambiguate.** mygeneset treats `_id` as a primary key, but
  cross-source name collisions are theoretically possible; store `source`
  alongside and flag any collision at build time.

> **Upstream alignment to confirm with @cmungall:** the `monarch-initiative/genesets`
> interpretation files currently set `gene_set_id: MSIGDB:KEGG_ASTHMA`. For a 1:1
> import join, either (a) switch upstream `gene_set_id` to `MYGENESET:<_id>` (keep
> `MSIGDB:` as an xref), or (b) have the dismech importer remap `MSIGDB:` → `MYGENESET:`.
> Option (a) is cleaner and future-proofs non-MSigDB sources.

## Implemented: the `MyGeneset` structured source

`src/dismech/structured_sources/mygeneset.py` (`MyGenesetSource`, registered in
the CLI as `mygeneset`) ingests gene sets exactly like `OrphanetSource`/`ClinGenSource`:

- **Inputs (pinned, not committed — `data/genesets/MANIFEST.yaml` is the pin):**
  the curated `GeneSetInterpretation` YAMLs from `monarch-initiative/genesets`
  at a pinned commit, joined with gene membership from **mygeneset.info**.
- **Output (committed):** one `references_cache/MYGENESET_<id>.md` per set, in the
  same line-oriented markdown-table format as the other structured sources, so
  individual rows are quotable evidence `snippet:` values.
- **Commands:**
  ```bash
  just genesets-refresh                 # fetch interpretations (pinned commit) + mygeneset membership
  just genesets-rebuild                 # (re)write references_cache/MYGENESET_*.md   (--id KEGG_ASTHMA to limit)
  just genesets-list                    # list ingestable ids
  just genesets-align Asthma KEGG_ASTHMA  # BP alignment for one disease ↔ set
  just genesets-align-all               # catalog-wide BP-alignment audit (by MONDO)
  ```
- **Cache body sections:** Description · Context (disease/tissue MONDO/UBERON) ·
  Curated GO interpretation (`GO id | label | aspect | role | confidence`) ·
  Members (`symbol | hgnc:id`, dismech's canonical gene namespace) · Source
  (genesets commit + mygeneset + upstream `gene_set_id` xref).

**It acts as evidence today.** A disorder can cite e.g.:

```yaml
evidence:
- reference: MYGENESET:KEGG_ASTHMA
  supports: SUPPORT
  snippet: "GO:0045064 | T-helper 2 cell differentiation | biological_process | core_process | high"
  explanation: The curated KEGG_ASTHMA interpretation lists Th2 differentiation as a core process.
```

This validates through the real `linkml-reference-validator` (verified), and all
emitted files pass the `check-reference-cache-frontmatter` contract. Caveat
(unchanged): a gene-set row is a *lead*, not mechanism — back disease claims with
a primary PMID too. **100 sets ingested** (pin `08115aa0`, 2026-06-26 — upstream
grew from 23 → 100); a few cell-type sets have no mygeneset membership and
serialize without a Members block.

## Proposed (not built): a `gene_sets` schema element + BP alignment

The structured-source path above makes gene sets *citable*. A complementary idea
is a first-class **`gene_sets`** slot on `Disease` (sibling of `pathophysiology`,
**not** under computational models — it's a reference object, not a model) that
points at an external gene set and optionally carries a short interpretation:

```yaml
gene_sets:
- reference: MYGENESET:KEGG_ASTHMA          # resolves to the cache file above
  relationship: CANONICAL_PATHWAY           # or CELL_TYPE_SIGNATURE, PERTURBATION, ...
  note: KEGG legacy asthma pathway; overlaps the Th2 + antigen-presentation arms.
```

Kept deliberately thin — membership and the GO interpretation already live
upstream and in the cache file, so the slot just records the disease↔set link and
its semantics (avoids re-duplicating genes in the KB).

### Scoring: align the curated *BPs*, not the genes

The primary alignment unit is the **biological process**, not the gene. Each
interpretation already curates a small, role-tagged list of GO BPs (the
`TermAssociation`s); the pathograph independently curates GO BPs on its
`pathophysiology[].biological_processes`. The audit is **set BPs ↔ pathograph
BPs**, and the interpretation's role tags do the noise-filtering that gene-level
overlap can't:

- **`core_process` / `core_component`** set BPs → *should* be represented in the
  pathograph. A core BP with no pathograph match is the actionable gap.
- **`supporting_process`** → nice-to-have; informational.
- **`nonspecific` / `false_association`** → *expected absent*; if one shows up in
  the pathograph that's a lint warning, not a gap. (Validated: `GO:0006412
  translation` is `nonspecific` in all 5 disease sets and absent from all 5
  pathographs.)

This is why **gene-level Jaccard is the wrong tool** — it's symmetric and swamped
by the large tail of downstream set genes we never intend to node out. At the BP
level the curated list is already the signal, and scoring is **asymmetric +
role-weighted**:

- *Corroboration* = fraction of the set's **core** BPs represented in the
  pathograph (want high; low = review).
- *Gap list* = the set's core BPs with **no** pathograph match — the concrete
  curation to-do (e.g. asthma's antigen-presentation / FcεRI arms).
- The reverse direction (pathograph BPs absent from the set) is descriptive, not
  a penalty — disease-specific biology the generic pathway omits.

Matching must be **hierarchy-aware**, not exact-id equality: a set BP counts as
represented if a pathograph BP is the same term, an **ancestor**, or a
**descendant** (via OAK over GO — already configured in `conf/oak_config.yaml`).
This handles the divergences flagged in the worked examples: T1D's generic
`antigen processing and presentation` (set) vs the MHC-class-I **child** in the
pathograph; PD's `neuron apoptotic process` (set) vs the pathograph's
**mechanism substitution** to ferroptosis (which hierarchy alone won't bridge —
surface it for human reconcile rather than scoring it as missing).

A gene-level signal, if wanted at all, should be **asymmetric containment**
(`|P∩G|/|P|`), never symmetric Jaccard.

### Built: `just genesets-align <disease> <set>`

`src/dismech/genesets_align.py` (+ the `align` CLI command) implements exactly the
above. It reads the set BPs from the committed `references_cache/MYGENESET_*.md`
file (no refresh needed) and the pathograph BPs from the disorder YAML, matches
them over GO via OAK, and prints per-BP status + corroboration + the core-BP gap
list. **Matching counts EXACT and DESCENDANT** (pathograph term more specific) as
represented; an **ANCESTOR** match (pathograph has only a *more general* term —
e.g. `metabolic process`) is shown but **does not count**, which avoids the
over-general false positive. It **does not need the schema element**; the
`gene_sets` slot would just give the link a durable home + an audit badge.

It reproduces the manual gap analysis:

| Disease ↔ set | Corroboration | Core-BP gaps surfaced |
|---|---|---|
| Asthma ↔ KEGG_ASTHMA | 2/3 | `MHC class II protein complex` (the antigen-presentation arm) |
| Type I Diabetes ↔ KEGG_T1D | 2/3 | `MHC class II protein complex` (vs the pathograph's MHC-class-I child, matched as DESCENDANT) |
| Parkinson's ↔ KEGG_PD | 2/6 | OXPHOS + ubiquitin-catabolism (broader-only), `mitochondrion` (CC), `neuron apoptotic process` |

(The PD apoptosis-vs-ferroptosis divergence I flagged earlier got reconciled
*upstream* — `ferroptosis` is now a curated set BP and matches EXACT.)

The aligner reads **only the disorder's own `biological_processes`**, and that is
correct: `conforms_to` is a consistency-check pointer, **not** an import. A
conforming disorder node fully duplicates the module's content locally (with
organ-specific substitution) by design, so its own BPs are already authoritative.
Pulling module BPs in via `conforms_to` would double-count and would *mask*
under-curation — a disorder that declares `conforms_to` but omits the module's
expected BPs is a **conformance** gap for the existing module-checking to catch,
not something the aligner should paper over. Remaining open knob: whether to
additionally weight corroboration by the set's `confidence`.

### Catalog-wide audit: `just genesets-align-all`

`align-all` (also `ga.sweep`) maps every disease-context set to its dismech
disorder by the set's disease-context **MONDO** (via `build_mondo_index`) and runs
the aligner across the whole catalog. On the 100-set pin: **56 disease-context
sets, 37 mapped to a dismech disorder.** The table is reproducible (`just
genesets-align-all`), so it's not pasted in full — recurring patterns:

- **`MHC class II protein complex` (CC)** is the gap for Asthma, Rheumatoid
  Arthritis, and Type I Diabetes (all 2/3). It's a *cellular_component* — dismech
  models cells via CL, not GO CC, so this class of gap is partly structural, not a
  curation miss. (Worth deciding whether CC-aspect set BPs should be scored at all.)
- **`mitochondrion` (CC) + `neuron apoptotic process`** recur across the
  neurodegeneration sets (Alzheimer's 1/4, Parkinson's 2/6, Huntington's 3/5, ALS
  0/4) — genuine, actionable mechanistic gaps.
- **`regulation of cell population proliferation`** is the common gap across the
  KEGG cancer sets (CML, CRC, prostate, NSCLC, basal cell …) — a generic
  proliferation BP most cancer pathographs don't carry as an explicit node.
- Best-aligned: `WP_22Q11.2_CNV` ↔ 22q11.2 Deletion Syndrome **2/2**; worst flag
  sparse pathographs (HCM 0/4, gastric-cancer nets 0/2) as enrichment targets —
  the same signal as the `Colon_Adenocarcinoma` stub.

Caveat: the MONDO→disorder map keeps one disorder per MONDO (advisory), so a set
may align against a sibling subtype (e.g. KEGG_COLORECTAL_CANCER → the
`Metastatic_Colorectal_Cancer` entry rather than `Colon_Adenocarcinoma`).

## Coverage backlog

**Largely closed by the 23 → 100 upstream expansion.** Of the original 8
not-yet-interpreted staged sets, **6 now have an interpretation** (Huntington's,
SLE, ALS, Autoimmune Thyroid, Graft-vs-Host, Prion). Still missing upstream:
`WP_DRAVET_SYNDROME` (never had one) and `KEGG_MEDICUS_…_IL6_…JAK_STAT` (a
signaling pathway, not a disease → wants a *module* mapping, not a disorder). The
original pre-expansion backlog table is kept below for history.

Of the 13 sets dismech had staged, **5 had an upstream GO interpretation** at the
first pin (Alzheimer's, Asthma, Colorectal Cancer, Parkinson's, Type I Diabetes).
The **8 then-not-yet-interpreted** — ranked by dismech two-way value (does a rich
dismech pathograph exist to cross-check against?):

| MSigDB set (`_id`) | dismech entry to cross-check | Value |
|---|---|---|
| `KEGG_HUNTINGTONS_DISEASE` | `Huntington_Disease` | high — rich pathograph |
| `KEGG_SYSTEMIC_LUPUS_ERYTHEMATOSUS` | `Systemic_Lupus_Erythematosus` | high — rich pathograph |
| `WP_AMYOTROPHIC_LATERAL_SCLEROSIS_ALS` | `Amyotrophic_Lateral_Sclerosis` | high — rich pathograph |
| `KEGG_AUTOIMMUNE_THYROID_DISEASE` | `Graves_Disease` + `Hashimotos_Thyroiditis` | high — two conformers |
| `WP_DRAVET_SYNDROME` | `Dravet_syndrome` | medium — entry exists |
| `KEGG_GRAFT_VERSUS_HOST_DISEASE` | *(no dismech entry)* | low now — would seed a new entry |
| `KEGG_PRION_DISEASES` | *(no dismech prion entry)* | low now — would seed a new entry |
| `KEGG_MEDICUS_REFERENCE_IL6_FAMILY_TO_JAK_STAT_SIGNALING_PATHWAY` | *(not a disease — a signaling pathway)* | special — maps to a *module*, not a disorder |

The MEDICUS IL6→JAK/STAT set is a **signaling pathway, not a disease**; its
natural dismech counterpart is a mechanism *module* (cf. the JAK/STAT arms of RA,
Castleman, etc.), not a single disorder — worth a distinct interpretation
`context_type` discussion upstream.

The merged repo also carries 15 non-disease interpretations (cell-type C8
signatures, Hallmark, Reactome, TCA) that were never staged in dismech — those
feed the cell-type / process side of the import, not this disease backlog.

## Open decisions

Record the chosen answers in
[`docs/explanation/design-decisions.md`](../docs/explanation/design-decisions.md);
these touch scope, structured-source policy, and cross-repo governance.

1. ~~**Source of truth for membership**~~ — **RESOLVED:** `monarch-initiative/genesets`
   owns membership + interpretation; dismech `genesets/` retired.
2. ~~**Cache prefix**~~ — **RESOLVED:** `MYGENESET:<_id>` (see above). Still open:
   exact quotable-row shape, and confirming the upstream `gene_set_id` alignment.
3. **Are gene-set GO interpretations admissible as dismech evidence?** Likely
   **no** as standalone support (membership ≠ mechanism) — only as a *lead* that
   must be backed by a primary PMID, consistent with the DR/NEC anti-hallucination
   SOP. Confirm and document.
4. **Disease ↔ gene-set mapping table** — which dismech diseases have a canonical
   pathway gene set, and the MONDO/DOID ↔ mygeneset crosswalk (the interpretation
   files already carry the disease `context` MONDO, so the join is mostly free).
5. **Where does the diff/enrichment tooling run** — a `just` recipe in dismech
   that calls genesets-rs, or a genesets-rs command that reads dismech exports?
6. **Round-trip cadence** — manual, or a CI job that re-scores the benchmark when
   either repo changes.

## Next steps

- [x] Pull all 5 disease interpretations from PR #3 and diff term-by-term against
      dismech (Asthma, Parkinson's, Type I Diabetes, Alzheimer's, Colorectal) —
      done; see worked-examples section.
- [ ] File the concrete gaps as curation issues: PD OXPHOS + ubiquitin/mitophagy;
      T1D MHC-class-II presentation; CRC `Colon_Adenocarcinoma` GO scaffold.
- [x] Retire dismech's `genesets/` dir (membership owned upstream) — done.
- [x] Build the `MyGeneset` structured source + `references_cache/MYGENESET_*.md`
      generator (following `OrphanetSource`); 23 sets ingested, evidence-validated.
- [ ] Confirm upstream `gene_set_id` alignment with @cmungall (`MYGENESET:` vs
      `MSIGDB:`); curate the 8 backlog interpretations upstream (value-ranked above).
- [ ] Decide on the `gene_sets` schema element (scope) and wire the first disease
      to cite its canonical set (Asthma ↔ `MYGENESET:KEGG_ASTHMA`).
- [x] Build the BP aligner (`just genesets-align <disease> <set>`): hierarchy-aware,
      role-weighted match of a set's curated BPs vs the pathograph's
      `biological_processes` (OAK over GO) → corroboration score + core-BP gap list.
      Reproduces the manual gap analysis (see below).
- [ ] Record decisions 1–6 in the design-decisions register.

## Notes / log

### 2026-06-25
- Initial brainstorm. Inventoried both sides: dismech `genesets/` (13 MSigDB
  membership-only sets, `MSIGDB:` reference_ids, unwired) and genesets-rs PR #3
  (GeneSetInterpretation schema + GO `role` taxonomy + eval-first CLI).
- Identified the Asthma ↔ KEGG_ASTHMA pilot and a concrete gap list (antigen
  presentation, FcεRI degranulation, eosinophil effectors, CD40 costimulation).
- Extended the diff to all 5 disease interpretations in the PR. Key results:
  `GO:0006412 translation` is `nonspecific` in all five and absent from all five
  dismech entries (denylist validated); `Colon_Adenocarcinoma` is a GO-free stub
  (highest-value enrichment target); concrete adds for PD (OXPHOS, ubiquitin/
  mitophagy) and T1D (MHC class II). Noted the neuron-death modeling divergence
  (genesets apoptosis vs dismech ferroptosis) — the diff tool must reconcile
  parent/child + mechanism substitution, not flag them as missing.

### 2026-06-26
- genesets repo renamed `cmungall/genesets-rs` → `monarch-initiative/genesets`;
  interpretation PR **merged** to `main` (23 interpretation files). Confirmed the
  merge picked up `evidence_source` with dismech's exact enum; `supports` stayed
  3-valued (`SUPPORT`/`REFUTE`/`NEUTRAL`) — lossless for the import direction.
- **Retired** dismech's `genesets/` dir (13 membership-only sets deleted); nothing
  in `src/`/`tests/`/`conf/` referenced it.
- Computed the [coverage backlog](#coverage-backlog): 5 of the 13 staged sets now
  have upstream interpretations; 8 do not.
- Settled the identifier scheme on **mygeneset.info** (`MYGENESET:<_id>`) after
  confirming mygeneset's `_id` is the bare set name + a `source` field.
- Built the `MyGeneset` structured source (`src/dismech/structured_sources/mygeneset.py`)
  + `data/genesets/MANIFEST.yaml` (pins genesets commit `c9af95e9`), CLI/justfile
  recipes (`genesets-refresh|rebuild|list`), and tests. Ran refresh+rebuild → 23
  `references_cache/MYGENESET_*.md`. Confirmed a `MYGENESET:` citation validates
  through the real `linkml-reference-validator` and the whole cache passes the
  frontmatter contract. Membership comes from mygeneset (symbol + NCBIGene,
  resolved to `hgnc:` via mygene.info — mygeneset has no HGNC field); the
  curated GO interpretation + evidence come from the genesets repo.
- Wrote up the `gene_sets` schema-element + disease-vs-set scoring idea as a
  documented proposal (not built) — see the "Proposed" section.

### 2026-06-26 (cont.)
- Decision: HGNC resolution lives in dismech's ingest (not upstream — mygeneset
  has no HGNC field, and `monarch-initiative/genesets` is out of push scope).
  `MyGenesetSource` now resolves NCBIGene→HGNC via mygene.info (batched) during
  refresh; Members render as `hgnc:` (e.g. IL4 → `hgnc:6014`, matching the dismech
  Asthma entry), with NCBIGene fallback only for genes lacking an HGNC (LOC*
  loci, withdrawn symbols). Re-refreshed + rebuilt all 23 cache files.
- Reframed scoring: the goal is **BP↔BP alignment** (the set's curated GO
  `TermAssociation`s vs the pathograph's `biological_processes`), not gene
  overlap. Gene-level Jaccard is symmetric and swamped by downstream set genes;
  at the BP level the role tags filter noise, so the metric is asymmetric +
  role-weighted (core BPs should be covered; nonspecific/false expected absent)
  and hierarchy-aware (OAK over GO, to bridge parent/child + surface mechanism
  substitutions). Updated the proposal accordingly.
- Built the aligner (`src/dismech/genesets_align.py` + `just genesets-align`,
  tests). Counts EXACT/DESCENDANT as represented; ANCESTOR is "broader-only" and
  not counted (kills the `metabolic process` false positive seen in PD).
  Reproduces the manual gaps: Asthma 2/3 (MHC-II), T1D 2/3 (MHC-II; antigen
  presentation matched DESCENDANT to the MHC-I child), PD 2/6 (OXPHOS + ubiquitin
  broader-only, mitochondrion CC, neuron apoptosis).
- Correction (per @cmungall): `conforms_to` is **not** an import — conformance
  duplicates module content into the disorder node, so the aligner correctly uses
  only the disorder's own BPs; importing module BPs would mask conformance gaps.
  Dropped that as a proposed knob.
- Bumped the genesets pin to `08115aa0`: upstream grew **23 → 100** curated sets,
  closing most of the coverage backlog. Re-ingested all 100. Added
  `just genesets-align-all` (`ga.sweep`) — maps each disease-context set to its
  dismech disorder by MONDO and aligns catalog-wide: 56 disease sets, 37 mapped.
  Recurring gaps: MHC-class-II (CC) in Asthma/RA/T1D, mitochondrion + neuron
  apoptosis across neurodegeneration, generic proliferation across cancers.
