# Histopathology `finding_term` NCIT triage

Provenance note for the `HistopathologyFindingTerm` branch expansion and the
subsequent backfill of `histopathology[].finding_term` bindings.

## Background

`HistopathologyFindingTerm` was widened from Morphologic Finding (`NCIT:C35867`)
+ Histologic Grade (`NCIT:C18000`) to cover the whole NCIT **Histopathology
Result** branch (`NCIT:C83490`), adding Immunophenotypic Finding
(`NCIT:C40998`), Ultrastructural Finding (`NCIT:C43265`), and Staining
Intensity (`NCIT:C127762`). See CLAUDE.md and the schema
(`src/dismech/schema/dismech.yaml`).

## Coverage at time of triage

At the start there were **436 histopathology findings**, of which **282**
carried a `finding_term`. This triage bound **31 more** across three batches:

- Neoplastic/heme batch (11): Carney-Stratakis (SDHB-loss IHC, epithelioid
  component, lymphatic invasion), Anal_Canal_Adenocarcinoma (mucinous
  adenocarcinoma, cytokeratin-positive immunophenotype), Penile_Cancer &
  Squamous_Cell_Carcinoma_of_Penis (squamous cell carcinoma),
  Myeloproliferative_Neoplasm_Unclassifiable (megakaryocyte proliferation),
  Aggressive_NK-cell_Leukemia (bone marrow involvement), Meningeal_Melanocytoma
  (meningeal melanocytoma, HMB45-positive marker panel).
- Non-neoplastic generic-pathology batch (20): inflammatory/lymphoplasmacytic/
  eosinophilic infiltrate, fibrosis, necrosis, acantholysis, hyperkeratosis,
  spongiosis, hypercellularity, nuclear inclusion, amyloid/hemosiderin
  deposition, villous atrophy, metaplasia, onion-skinning — see the per-file
  `finding_term` blocks.

## Key finding: where NCIT does and does not reach

The NCIT Morphologic Finding branch has **good coverage for generic pathology
patterns** (fibrosis, necrosis, granulomatosis, metaplasia, hyperplasia,
inflammatory/eosinophilic/lymphoplasmacytic infiltrate, amyloid/hemosiderin
deposition, acantholysis, spongiosis, hyperkeratosis, villous atrophy, nuclear
inclusion) and, via the newly added Immunophenotypic branch, for IHC markers
(SDHB loss, cytokeratin, HMB45, ER/PR/HER2, Ki-67 percentage bins).

It is **sparse or absent** for:

1. **Organ-specific microscopic findings**, especially renal
   (foot-process effacement, mesangial hypercellularity as a named term,
   glomerular crescents, segmental glomerulosclerosis, tip lesion) — not in the
   branch.
2. **A plain "Granuloma" / "granulomatous inflammation" morphologic finding.**
   `NCIT:C3064` (Granuloma) is a *Disorder* node, not reachable from the
   Histopathology Result branch; the in-branch granuloma terms are all
   tumor/entity-specific (Lymphomatoid Granulomatosis, Xanthogranuloma, etc.).
   Neurosarcoidosis and Farber disease granuloma findings were therefore left
   unbound rather than mis-bound.
3. **Disease/eponym-level "findings"** that are really entities, not morphology
   (Barrett esophagus, Castleman hyaline-vascular/plasma-cell variants, DNET
   "specific glioneuronal element", Touton giant cells, juvenile polyp).
4. **HP is not a substitute here.** `finding_term` currently allows only
   `HP:0025461` (Abnormal cell morphology) descendants — 60 terms, almost all
   cell-level (rosettes, inclusion bodies, Gaucher cells). It does **not** cover
   tissue/architectural findings, so the ~123 remaining unbound findings (mostly
   non-neoplastic renal/derm/neuro/muscle/metabolic) cannot be rescued by the
   current HP root.

## Remaining unbound: 123 findings across 76 files

These fall into three buckets:

- **No faithful morphologic-finding term in NCIT** and outside the current HP
  root (renal glomerular findings, demyelination patterns, muscle-biopsy
  findings such as ragged-red fibers / nemaline rods, corneal deposits,
  disease-specific patterns). Best left as prose unless the schema HP root is
  broadened.
- **Bindable only to an over-generic NCIT term** (e.g. everything → "Deposit")
  where the generic term adds little machine-queryable value; deferred.
- **Genuinely entity-level** ("findings" that are diagnoses); these arguably
  belong in `disease_term`/subtype rather than `histopathology`.

## Recommendations (open)

1. **Consider broadening the HP root** for `HistopathologyFindingTerm` beyond
   `HP:0025461` to a histology-relevant set (e.g. specific organ-histology HP
   branches) so non-neoplastic tissue findings become bindable — this is the
   single biggest lever for the remaining 123. Needs a design-decision entry
   because it risks blurring the histopathology/phenotype boundary.
2. For the renal findings specifically, evaluate whether an additional
   ontology (e.g. a renal-pathology vocabulary) is warranted, or accept prose.
3. Leave entity-level "findings" as prose or migrate them to `disease_term`.
