# How dismech Represents Antigens on B and T Cells: Gap Analysis (2026-09-03)

A census of how the knowledge base records **antigen identity** in immune and
autoimmune entries, and whether the recorded antigen can be attributed to the
lymphocyte lineage that recognises it.

Scope: all 2,535 files in `kb/disorders/` plus all 167 in `kb/modules/`
(2,702 entries), narrowed to a 573-entry immune cohort. Numbers are regenerable
with `scripts/immune_antigen_audit.py`; nothing here is gated, and no KB or
schema file was changed.

```bash
uv run python scripts/immune_antigen_audit.py                        # the summary below
uv run python scripts/immune_antigen_audit.py --format tsv --out /tmp/antigen.tsv
uv run python scripts/immune_antigen_audit.py --entry Celiac_Disease
```

---

## The finding in one line

**The schema has no antigen concept.** The string `antigen` does not appear once
in any of the seven files under `src/dismech/schema/` — not as a class, not as a
slot, not as an enum value. Every antigen in the knowledge base is free text.

The measurable consequence: of the **3,122 objects** across the immune cohort
that name an antigen in prose, **2,967 (95.0%)** carry no `cell_types` at all.
For the overwhelming majority of antigen mentions, *which lymphocyte sees this
antigen* is not recoverable from structure — only by reading the sentence.

| Antigen-naming objects | Count | Share |
|---|---:|---:|
| with a B-lineage cell type | 58 | 1.9% |
| with a T-lineage cell type | 87 | 2.8% |
| with an antigen-presenting cell | 49 | 1.6% |
| **with no `cell_types` whatsoever** | **2,967** | **95.0%** |

Per entry, the picture is the same: of the 323 immune-cohort entries that name
an antigen anywhere, **226 (70%) attribute none of them to a B or T lineage**.

---

## 1. The cohort, and how little of it is structurally identifiable

| Cohort membership established by | Entries |
|---|---:|
| `classifications.harrisons_chapter: IMMUNE_RHEUMATOLOGIC` | 104 |
| prose only — matches `autoimmun` / `autoantibod` / `autoantigen` | 263 |
| prose only — matches `immunodeficien` / `immune-mediated` / `hypersensitiv` / `vasculit` | 206 |
| **total** | **573** |

Only 18% of the immune cohort is identifiable from a curated classification.
The rest had to be found by grep. That is a prior gap, not the subject of this
report, but it bounds what any antigen-focused query could return today: a
consumer asking "show me the autoimmune diseases" gets 104 of 573.

Within the cohort, 323 entries name an antigen and **250 name none** — including
entries where an antigen is the defining fact of the disease (see §6).

## 2. Where antigen text actually lives

Objects in the immune cohort whose own scalar fields name an antigen:

| Top-level slot | Objects |
|---|---:|
| `pathophysiology` | 1,083 |
| `treatments` | 412 |
| `biochemical` | 239 |
| `phenotypes` | 208 |
| `discussions` | 195 |
| `references` | 146 |
| `genetic` | 138 |
| `diagnosis` | 112 |
| `mechanistic_hypotheses` | 98 |
| `has_subtypes` | 92 |
| `environmental` | 87 |

Raw pattern frequency across the cohort: `antigen` (generic) 2,005;
bare `anti-X` 1,480; `anti-X antibody` 1,331; `autoantigen` 213; `epitope` 200;
`antigen present*` 191; `molecular mimicry` 122; `neoantigen` 43;
`citrullinat*` 33; `superantigen` 30; `deamidat*` 20; `epitope spreading` 11.

### 2a. The free-text form cannot distinguish an autoantigen from a drug target

The same `anti-X` string carries four different kinds of fact, and nothing in
the YAML separates them. Ranking the captured `X` by how many entries use it:

| Outside `treatments` (candidate autoantigens) | Inside `treatments` / `clinical_trials` (drug targets) |
|---|---|
| TNF (10), neutrophil cytoplasmic (10), NMDAR (9), CD20 (7), GBM (5), AChR (4), nuclear (4), **Mullerian (4)**, GM1 (3), titin (3), Sm (3), Hu (3), TPO (3), **DNase (3)** | CD20 monoclonal (26), TNF (25), CD20 (20), PD-1 (7), IL-6 (6), IgE (4), C5 (4), VEGF (4), IL-5 (4) |

Reading down the left column: `neutrophil cytoplasmic`, `NMDAR`, `AChR`,
`titin`, `Sm`, `Hu` and `TPO` are genuine autoantigens; `TNF` and `CD20` are
therapeutic targets that leaked out of `treatments` via evidence prose;
`DNase` is `anti-DNase B titre`, an *anti-streptococcal* serology and not a
self-antigen at all; and `Mullerian` is anti-Müllerian hormone, which is not an
antibody target in any sense — the pattern matched `anti-Müllerian`.

An autoantigen, a pathogen antigen, a hormone name and a monoclonal-antibody
target are indistinguishable to any consumer of this data. That is the cost of
having no slot: the distinction exists only in a curator's head.

## 3. Sense 1 — autoantigen identity

**116 autoantibody rows** in `biochemical` across **66 entries**. Of those,
**11 carry a `biomarker_term`**; the other 105 are name strings.

Where a binding does exist it is almost always to a *phenotype*, not to the
antigen. `Adult-Onset_Myasthenia_Gravis` is the best-curated case in the KB:

```yaml
biochemical:
- name: Anti-Acetylcholine Receptor Antibody
  biomarker_term:
    preferred_term: Anti-acetylcholine receptor antibody positivity
    term: {id: HP:6001064, label: Anti-acetylcholine receptor antibody positivity}
```

This is a real improvement over a bare string, and HPO supports it further than
the KB uses it — **32 HP terms with `antibody` in the label are already in
`cache/hp/terms.csv`** (`HP:0030057 Autoimmune antibody positivity` is the
parent), covering ANA, anti-dsDNA-adjacent, ANCA/MPO/PR3, anti-Ro/SS-A,
anti-cardiolipin, anti-β2GPI, anti-MuSK and more. Three entries use them.

But note what the HP binding says: it asserts *the patient is seropositive*. It
does not identify the antigen as a molecular entity, so it cannot be joined to
the gene that encodes it, to the tissue that expresses it, or to a T-cell
response against the same protein.

`biomarker_term` bindings across `kb/disorders/` by prefix — CHEBI 451,
NCIT 248, HP 71, `hgnc` 4, GO 2 — show the slot is already used
heterogeneously, so an antigen-as-gene-product binding would not be
unprecedented. It would just be undeclared.

### 3a. The `genetic` block is being used as an antigen slot, with a disclaimer

`GeneDiseaseRelationshipEnum` has ten values — `CAUSATIVE`, `RISK_FACTOR`,
`PROTECTIVE`, `MODIFIER`, `SUSCEPTIBILITY`, `SOMATIC_DRIVER`, `COOPERATING`,
`BIOMARKER`, `DISPUTED`, `UNKNOWN`. **None of them means "the protein this gene
encodes is the target of the autoimmune response."**

Two entries record the autoantigen gene anyway and work around the missing
value in free text:

- `Anti-GBM_Disease` — `COL4A3 (alpha-3 type IV collagen) autoantigen target gene`,
  with `association: Autoantigen target (not a causal germline mutation)` and
  `relationship_type` left empty. The curator wrote the disclaimer into the data
  because the enum could not carry it.
- `Antisynthetase_Syndrome` — `HARS1 (autoantigen; anti-Jo-1 target)`,
  `association: Autoantigen`, with a note that "HARS1 is the autoantigen, not a
  mutated disease gene."

A third case shows the failure mode this invites. `Membranous_Nephropathy`
records `PLA2R1 susceptibility locus` with `association: GWAS`. PLA2R1 is both
a GWAS hit *and* the defining autoantigen; the entry captures the first fact and
silently drops the second, because `genetic` has a value for one and not the
other. Its own `biochemical` block, meanwhile, carries `Anti-PLA2R
autoantibodies` as an unbound string. The same protein appears twice in one
file, in two vocabularies, with no link between them.

`Pemphigus_Vulgaris` shows the opposite failure: DSG1 and DSG3 — arguably the
most precisely characterised autoantigen pair in medicine — appear **nowhere**
in its `genetic` block, which holds only three HLA rows. They exist solely
inside strings like `Anti-Desmoglein 3 Antibodies`.

## 4. Sense 2 — B versus T attribution in the pathograph

Across the immune cohort's pathophysiology nodes:

| | Nodes |
|---|---:|
| carrying a B-lineage cell type | 203 |
| carrying a T-lineage cell type | 384 |
| carrying **both** | 56 |

Per entry: 87 have both B and T nodes, 132 have T only, 45 have B only, and
**309 of 573 have neither**.

The cell-type layer itself is in good shape — `CL:0000236 B cell` (163 uses),
`CL:0000084 T cell` (150), `CL:0000625 CD8-positive, alpha-beta T cell` (82),
`CL:0000624 CD4-positive, alpha-beta T cell` (72), `CL:0000786 plasma cell` (58),
`CL:0000844 germinal center B cell` (11), `CL:0000980 plasmablast` (9). The gap
is not the vocabulary. It is that **a node says which cell is present and,
separately, prose says which antigen is involved, with no edge between them.**

The 56 both-lineage nodes are where this bites hardest: a node carrying `T cell`
and `B cell` together is exactly the node where the two lineages might be seeing
*different* antigens, and it is structurally incapable of saying so.

The KB's only antigen-centric module makes the point. `molecular_mimicry_autoimmunity`
collapses the entire lymphocyte response into one node:

```yaml
- name: Cross-Reactive Autoreactive Lymphocyte Activation
  cell_types: [T cell, B cell]
```

Its own `description` says the cross-reactive antigen "activates autoreactive T
and/or B cells" — the *and/or* is doing load-bearing work that the data model
cannot express. The module names no antigen structurally, and its downstream
node `Epitope Spreading and Autoimmune Amplification` — the mechanism by which
the antigen set *changes over time* — has no antigens to spread between.

## 5. Senses 3 and 4 — HLA restriction and surface markers

**HLA.** 1,289 prose mentions. 106 cohort entries mention HLA; **48 bind an
`HLA-*` gene via `gene_term`**, so 58 do not. The split is not random — it
correlates with nothing, and the entries missing the binding include the two
diseases where HLA restriction *is* the mechanism:

| Entry | HLA rows | `gene_term` bound? |
|---|---|---|
| `Celiac_Disease` | HLA-DQ2, HLA-DQ8 | **no** |
| `Type_I_Diabetes` | HLA-DQ2, HLA-DQ8 | **no** |
| `Pemphigus_Vulgaris` | HLA-DRB1\*04, HLA-DRB1\*14, HLA-DQB1\*0503 | **no** |
| `Systemic_Lupus_Erythematosus` | HLA-DR2, HLA-DR3 | **no** |
| `Multiple_Sclerosis`, `Rheumatoid_Arthritis`, `Graves_Disease` | HLA-DRB1 | yes (`hgnc:4948`) |
| `Anti-GBM_Disease` | HLA-DRB1 (DR15 / DRB1\*15:01) | yes |

Two further problems are visible in that table. Serological and allele-level
designations (`HLA-DQ2`, `HLA-DR3`, `DRB1*15:01`) have no home: they are not
HGNC genes, so they get typed into `name` as free text. And even where the gene
binds, the binding loses the allele — `hgnc:4948` is *HLA-DRB1*, which cannot
distinguish the DR15 haplotype of anti-GBM disease from the shared-epitope
DRB1\*04 of RA. **Nowhere in the KB is a peptide linked to the allele that
presents it.**

**Surface / lineage markers.** These divide sharply by whether a CL term
happens to encode them:

| Marker | Total mentions | In `name` / `preferred_term` / `label` | In prose (`description`/`snippet`/`explanation`/…) |
|---|---:|---:|---:|
| CD4 | 1,080 | 257 (24%) | 823 |
| CD8 | 988 | 243 (25%) | 745 |
| CD3 | 198 | 4 (2%) | 194 |
| CD19 | 172 | 11 (6%) | 161 |
| CD20 | 167 | 4 (2%) | 163 |

CD4 and CD8 are well represented, but only as a side effect: they ride along
inside CL labels such as `CD8-positive, alpha-beta T cell`. CD19, CD20 and CD3 —
the B-lineage and pan-T markers, and the ones that matter for therapy — have no
CL term to ride on and are therefore almost entirely prose. **79 entries mention
rituximab**; the CD20 it depletes is a sentence in a `description`, not a
target.

## 6. Worked exemplars

### `Celiac_Disease` — the textbook B/T divergence, entirely unstructured

Coeliac disease is the canonical case: the T-cell antigen is a **deamidated
gliadin peptide presented on HLA-DQ2/DQ8**, while the dominant B-cell antigen is
**tissue transglutaminase (TG2)**, the very enzyme that performs the
deamidation. Two different molecules, two different lineages, one disease. What
the entry actually holds:

- `pathophysiology`: `Gluten-Triggered Immune Response` (cell type: `T Helper Cell`)
  and `Autoantibody Production` (cell type: `Plasma Cell`) — the two lineages are
  correctly separated into distinct nodes, and **neither node names its antigen**.
- `biochemical`: `Anti-tTG IgA`, `Anti-Endomysial Antibodies`, `Anti-DGP
  Antibodies` — three unbound strings, `biomarker_term: null` on all three. Note
  `Anti-DGP` is a *B-cell* readout of the *T-cell* antigen; nothing records that.
- `genetic`: TGM2, the B-cell autoantigen, is **absent**. The block holds
  HLA-DQ2 and HLA-DQ8 with `gene_term: null`, plus ten bound susceptibility
  genes (IL2, IL21, BACH2, PTPN22 …).
- `environmental`: `Gluten Exposure` has **no `exposure_term`** and **no
  `influences_mechanisms`**, so the T-cell antigen is not in the pathograph at
  all. Only `Gastrointestinal Infections` and `Gut Microbiome` are linked.

The entry is not badly curated — the node split is right and the genetics are
bound. It is that the one fact this report is about has nowhere to go.

### `Type_I_Diabetes` — the autoantibody panel is simply missing

T1D is clinically *defined* by islet autoantibody status, and the antigens are
named in every guideline. In the entry:

- `GAD65`, `IA-2`, `ZnT8` — **zero occurrences each**.
- `biochemical` holds `Blood Glucose`, `Hemoglobin A1c (HbA1c)` and an NMR
  metabolomic risk score. **No autoantibody rows at all.**
- `autoantibody` appears 16 times, all in prose, and eight of those are evidence
  `explanation` fields *apologising for the gap* — "Supports T-cell mediated
  cytotoxicity but does not discuss autoantibody production", and seven near-
  identical siblings.

The node `Autoimmune Destruction of Beta Cells` lists seven cell types
(CD8+ cytotoxic T, CD4+ T, Treg, B cell, DC, macrophage) on a single node — a
rich cellular picture with no antigen attached to any of it.

### `Pemphigus_Vulgaris` — a compartmentalised antigen story held in prose

The entry curates the desmoglein compensation theory well, including a
dedicated node `Desmoglein Compensation and Lesion Distribution` whose
description states that mucosal-dominant PV has anti-Dsg3 only while
mucocutaneous PV has anti-Dsg3 plus anti-Dsg1. This is precisely an
antigen-stratified subtype claim — and it is a paragraph. `has_subtypes` is
absent, DSG1/DSG3 are not in `genetic`, and the two `biochemical` antibody rows
are unbound.

### `Adult-Onset_Myasthenia_Gravis` — the current ceiling

Three autoantibody rows bound to HP autoantibody-positivity terms; three HLA
genes bound to HGNC; a node correctly separating germinal-centre B cells and T
follicular helper cells in the hyperplastic thymus, whose description explains
that thymic myoid cells express the autoantigen *in situ*. This is as far as the
present schema goes, and it still cannot state that the AChR seen by the B cell
and the AChR peptide seen by the T cell are the same protein.

---

## 7. What already exists to build on

Nothing here requires a new ontology.

| Need | Existing resource |
|---|---|
| Antigen as a protein | `GeneProductDescriptor` (NCIT gene-product hierarchy), `ProteinComplexDescriptor` |
| Antigen as a gene | `GeneDescriptor` (HGNC), already used for COL4A3, HARS1, PLA2R1 |
| Antigen as a small molecule / hapten | `ChemicalEntityDescriptor` (CHEBI) |
| Dietary or environmental antigen | `ExposureDescriptor` (ECTO), `FoodDescriptor` (FOODON) |
| Seropositivity | 32 cached HP autoantibody-positivity terms under `HP:0030057` |
| Recognising lineage | CL bindings already on 531 pathophysiology nodes in the cohort |
| Attaching an antigen to a node | the `<kind>#<name>` entity-reference grammar |
| Recording *how* an antigen acts | the `ModelMechanismLink` / `influences_mechanisms` link-object pattern |

The pattern the KB already uses for exactly this shape of problem is the
**link object**: `treatments.target_mechanisms`, `environmental.influences_mechanisms`,
and `animal_models.modeled_mechanisms` all attach a typed, evidence-bearing edge
from an entity to a pathograph node. An antigen link would be the same shape —
antigen descriptor, target node, a recognising-lineage value (B / T / both), and
its own evidence — and would inherit the pathograph rendering and export for
free.

## 8. What this audit deliberately does not decide

- **Whether to change the schema.** The numbers say the information is absent
  from structure; they do not say the cost of adding a slot is worth paying.
  That is a design-decision call (`docs/explanation/design-decisions.md`), and
  the 105 unbound autoantibody strings could equally be addressed by binding
  them to existing HP terms with no schema change at all.
- **Which sense of "different antigens" matters most.** All four are gaps, but
  they are not equally expensive: HLA `gene_term` backfill for 57 entries is
  mechanical; peptide-to-allele restriction is a genuinely new modelling problem.
- **Whether an unbound antigen is a defect.** Many are correctly unbound —
  `Anti-Endomysial Antibodies` names a *tissue staining pattern*, not a molecule,
  and forcing a CURIE onto it would be worse than leaving it. The
  `dismech-terms` rule stands: no term beats a bad one.

## 9. Method and caveats

`scripts/immune_antigen_audit.py`, offline, ~4 min over `kb/disorders/` and
`kb/modules/`.

- **The cohort is a keyword union, not an ontology closure.** No MONDO descendant
  query was run (that needs the MONDO build). 263 of 573 entries are in the cohort
  because their prose says "autoimmune". False positives are certain — an entry
  mentioning autoimmunity in a differential diagnosis is counted.
- **The antigen patterns are deliberately generous**, because the point is to
  find every place an antigen is named, and none of those places is a slot.
  §2a shows the noise this admits (anti-Müllerian hormone, anti-DNase B). Raw
  pattern counts are upper bounds; the structural counts (`cell_types` present or
  absent, `biomarker_term` bound or not) are exact.
- **Lineage is matched on curated CL labels by substring**, not by CL closure, so
  a node bound to an unusual CL term whose label omits "B cell" / "T cell" is
  counted as unattributed. This biases the 95% figure *upward* slightly; the
  correction is bounded by the 20 uses of the ambiguous `CL:0000542 lymphocyte`.
- **Attribution is scored on the antigen-naming object itself**, not on its
  parent or siblings. A node whose `description` names an antigen while a sibling
  node carries the B cell counts as unattributed — correctly, since no relation
  between them is recorded, but a human reader would often infer one.
