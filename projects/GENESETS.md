---
title: Gene Sets ↔ dismech Integration
status: IN_PROGRESS
description: >-
  Brainstorm for moving named gene-set curation (MSigDB/KEGG/Hallmark/cell-type
  signatures) and their curated GO interpretations into the genesets-rs repo,
  and wiring two-way feedback with dismech disease pathographs.
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

> **Status:** brainstorm / design proposal. Nothing here is built yet. The goal is
> to decide *where gene-set curation lives* and *how dismech and the
> [`genesets-rs`](https://github.com/cmungall/genesets-rs) repo feed each other*.
> Companion: [`genesets-rs` PR #3](https://github.com/cmungall/genesets-rs/pull/3)
> ("Curated GO Interpretations for Gene Sets").

## TL;DR

We currently keep a small pile of raw gene sets **inside** dismech
(`genesets/`), and a richer **GO-interpretation** layer is being built **in
`genesets-rs`** (PR #3). These are the same underlying objects viewed from two
angles. Proposal:

1. **Make `genesets-rs` the single source of truth** for named, reusable gene
   sets and their curated GO interpretations. Retire the duplicated raw
   membership lists in dismech's `genesets/`.
2. **Have dismech consume gene-set interpretations as a structured reference
   source** (a new `MSIGDB:` / `GENESET:` cache prefix, exactly like `ORPHA:`,
   `CGGV:`, `CGDS:`), so a disease curator can cite a gene set and quote its
   curated GO interpretation as a *lead*.
3. **Close the loop both directions:** dismech disease pathographs are a
   hand-curated gold standard of "which GO processes matter for disease X";
   gene-set GO interpretations are a hand-curated gold standard of "which GO
   processes a gene set means." Where a disease has a matching pathway gene set
   (e.g. Asthma ↔ `KEGG_ASTHMA`), each can audit and enrich the other.

## What exists today

### A. dismech `genesets/` — raw membership (13 sets)

`genesets/<NAME>/` holds one directory per MSigDB set, each with:

- `DESCRIPTION.md` — frontmatter with `reference_id: MSIGDB:KEGG_ASTHMA`,
  `msigdb_collection`, `source_pathway_id: hsa05310`, `n_genes`, keywords.
- `genes.csv` — `species/code,symbol` membership (KEGG_ASTHMA = 30 genes).
- `PAPER.md` — citation stub.

These are **membership only** — no GO interpretation, no link to a dismech
disease. They look like they were staged to become a structured source but were
never wired in (nothing in `src/`, `scripts/`, `justfile` references
`genesets/`). The 13 sets: Alzheimer's, Asthma, Autoimmune Thyroid, Colorectal
Cancer, Graft-vs-Host, Huntington's, IL6→JAK/STAT (MEDICUS), Parkinson's, Prion,
SLE, Type I Diabetes, ALS (WP), Dravet (WP).

### B. `genesets-rs` PR #3 — curated GO interpretation layer

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

## The duplication problem to resolve first

`genesets/` (dismech) and `curation/genesets/` (genesets-rs) both hold MSigDB
membership. Two diverging copies of the same upstream data is a maintenance
hazard and a provenance ambiguity. Decide single ownership (recommended:
genesets-rs) before building any tooling on top.

## Open decisions

Record the chosen answers in
[`docs/explanation/design-decisions.md`](../docs/explanation/design-decisions.md);
these touch scope, structured-source policy, and cross-repo governance.

1. **Source of truth for membership** — genesets-rs only, or mirrored? *(Recommend
   genesets-rs; dismech keeps a pinned manifest, not copies.)*
2. **Cache prefix & shape** — `MSIGDB:` vs a neutral `GENESET:`; what rows are
   quotable; how to pin a release (`v2025.1.Hs`) for deterministic CI.
3. **Are gene-set GO interpretations admissible as dismech evidence?** Likely
   **no** as standalone support (membership ≠ mechanism) — only as a *lead* that
   must be backed by a primary PMID, consistent with the DR/NEC anti-hallucination
   SOP. Confirm and document.
4. **Disease ↔ gene-set mapping table** — which dismech diseases have a canonical
   pathway gene set, and the MONDO/DOID ↔ MSigDB crosswalk (seed: the 13 sets in
   `genesets/`).
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
- [ ] Decide membership ownership; if genesets-rs wins, open a dismech issue to
      retire/repoint `genesets/`.
- [ ] Prototype the `MSigDB`/`GeneSet` structured source
      (`src/dismech/structured_sources/`) + `references_cache/MSIGDB_*.md`
      generator, following `OrphanetSource`.
- [ ] Add an exporter: dismech disease → (a) curated GO list, (b) union gene set,
      (c) causal-edge GO ordering — as a benchmark artifact for
      `genesets-rs report`.
- [ ] Write the disease ↔ gene-set crosswalk for the 13 existing sets.
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
</content>
</invoke>
