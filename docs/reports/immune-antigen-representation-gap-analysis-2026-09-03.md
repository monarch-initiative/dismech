# How dismech Represents Antigens on B and T Cells: Gap Analysis (2026-09-03)

A census of how the knowledge base records **antigen identity** in immune and
autoimmune entries, and whether the recorded antigen can be attributed to the
lymphocyte lineage that recognises it.

Scope, **as of 2026-09-03**: all 2,535 files in `kb/disorders/` plus all 167 in
`kb/modules/` (2,702 entries), narrowed to a 573-entry immune cohort. Every
number below is regenerable with `scripts/immune_antigen_audit.py`, but this is a
dated snapshot and the KB grows daily — a run today scans more entries and will
not reproduce these totals verbatim. The conclusions are robust to that drift:
re-run on 2026-09-07 against 2,881 entries, the headline 64.0% / 36.0% split and
the zero-bindable-HLA-rows result of §5 were unchanged. Nothing here is gated,
and no KB or schema file was changed.

```bash
just immune-antigen-audit                                # the run behind this report
just immune-antigen-audit --format tsv --out /tmp/antigen.tsv
just immune-antigen-audit --entry Celiac_Disease
```

---

## The finding in one line

**The schema has no antigen concept.** The string `antigen` does not appear once
in any of the 21 files under `src/dismech/schema/` (7 top-level YAML, 13 more
under `classifications/`, and a README) — not as a class, not as a slot, not
as an enum value. Every antigen in the knowledge base is free text.

The measurable consequence, stated over the denominator that can actually carry
the answer: **only three classes own a cell-type slot** — `Pathophysiology`,
`Biochemical` and `ExperimentalModel` (plus `FunctionalEffect.affected_cell_types`).
Of the 3,122 objects that name an antigen, **428 are instances of one of those
classes, and 274 of them (64.0%) name no B, T or antigen-presenting lineage.**
So for roughly two thirds of the antigen mentions that *could* say which
lymphocyte sees the antigen, the answer is not recorded and can only be had by
reading the sentence.

| Antigen-naming objects in a class that can own a cell-type slot | Count | Share |
|---|---:|---:|
| naming a B, T or antigen-presenting lineage | 154 | 36.0% |
| **naming none** | **274** | **64.0%** |

The remaining **2,694 (86.3% of 3,122)** are evidence items, treatments,
phenotypes, references, `genetic` rows and descriptors — classes with no
cell-type slot at all. For those, an absent lineage is not a curation gap, it is
structurally impossible, so they are excluded from the rate above.

Counted across *all* 3,122 objects the figure is 2,967 (95.0%) with no lineage,
of which 2,892 have an empty or absent cell-type slot and 75 have one naming a
non-lymphoid cell. That number is real but inflated by its denominator; 64% is
the one a design decision should be taken on.

| Antigen-naming objects (all 3,122) | Count | Share |
|---|---:|---:|
| with a B-lineage cell type | 58 | 1.9% |
| with a T-lineage cell type | 87 | 2.8% |
| with an antigen-presenting cell | 49 | 1.6% |
| no B/T/APC lineage — cell-type slot empty or absent | 2,892 | 92.6% |
| no B/T/APC lineage — slot set, names a non-lymphoid cell | 75 | 2.4% |

Per entry: of the 323 immune-cohort entries that name an antigen anywhere,
**226 (70%) attribute none of them to a B or T lineage**.

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
| TNF (10), neutrophil cytoplasmic (10), NMDAR (9), CD20 (7), GBM (5), AChR (4), nuclear (4), **Mullerian (4)**, AQP4 (3), GM1 (3), Sm (3), Ro (3), La (3), Hu (3), TPO (3), **DNase (3)** | CD20 monoclonal (26), TNF (25), CD20 (20), PD-1 (7), IL-6 (6), IgE (4), C5 (4), VEGF (4), IL-5 (4) |

Reading down the left column: `neutrophil cytoplasmic`, `NMDAR`, `AChR`,
`AQP4`, `Sm`, `Ro`, `La`, `Hu` and `TPO` are genuine autoantigens; `TNF` and `CD20` are
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
the KB uses it — **33 HP terms with `antibody` in the label are already in
`cache/hp/terms.csv`** — 26 of them of the form `... antibody positivity`,
headed by `HP:0030057 Autoimmune antibody positivity` — covering ANA,
anti-dsDNA-adjacent, ANCA/MPO/PR3, anti-Ro/SS-A, anti-cardiolipin, anti-β2GPI,
anti-MuSK and more. Three entries use them.

But note what the HP binding says: it asserts *the patient is seropositive*. It
does not identify the antigen as a molecular entity, so it cannot be joined to
the gene that encodes it, to the tissue that expresses it, or to a T-cell
response against the same protein.

`biomarker_term` bindings across `kb/disorders/` and `kb/modules/` by prefix —
CHEBI 452, NCIT 269, HP 71, `hgnc` 4, GO 2, plus 22 blocks carrying no
`term.id` at all — show the slot is already used
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

**HLA, and why almost none of it is backfillable.** 1,289 prose mentions across
106 cohort entries; 48 entries bind an `HLA-*` gene via `gene_term`. At the row
level there are 100 `genetic` rows naming HLA, of which 59 are bound and 41 are
not.

The unbound 41 look like a backlog and are not one. **Not a single one names an
HGNC gene symbol:**

| Of the 41 unbound HLA rows, the name is | Rows |
|---|---:|
| an HGNC gene symbol (`HLA-DRB1`, `HLA-B`, …) — bindable | **0** |
| a serotype (`HLA-DQ2`, `HLA-B27`, `HLA-DR3`), an allele (`HLA-DRB1*03:01`, `HLA-DQB1*06:02`), a haplotype (`HLA-DR3-DQ2`) or a region | **41** |

A serotype is not a gene. `HLA-DQ2` is a serological specificity carried by an
HLA-DQA1/HLA-DQB1 haplotype, so there is no single HGNC identifier that means
it, and binding one would assert something false. Six of the 41 rows say exactly
this in their own `notes`, and the two entries where HLA restriction *is* the
mechanism are among them:

> `Celiac_Disease` — "No gene_term is bound because DQ2 is a serotype encoded by
> an HLA-DQA1/HLA-DQB1 haplotype rather than a single gene."

> `Type_I_Diabetes` — "HLA-DQ2 is a haplotype-level risk label, not a single
> HGNC-resolvable gene."

That is the [ontology term contract](../../CLAUDE.md) working as intended — no
term beats a bad one — and it is prior art, not a gap. The other 35 unbound rows
have no such note, but they are the same *kind* of name; what they are missing
is the written-down reasoning, not a binding.

The real gap here is a different one, and no amount of `gene_term` backfill
touches it: **the KB has nowhere to put a serotype, an allele or a haplotype.**
`HLA-DQ2`, `HLA-B27` and `DRB1*15:01` are typed into a free-text `name` because
`GeneDescriptor` binds HGNC genes and nothing binds an HLA allele. Even where a
gene does bind, it loses the allele — `hgnc:4948` is *HLA-DRB1*, which cannot
distinguish the DR15 haplotype of anti-GBM disease from the shared-epitope
DRB1\*04 of rheumatoid arthritis. **Nowhere in the KB is a peptide linked to the
allele that presents it.**

**Surface / lineage markers.** These divide sharply by whether a CL term happens
to encode them. Counted over the immune cohort, by whether the marker appears in
a curated identity field (`name` / `preferred_term` / `label`) or in prose:

| Marker | Mentions | In an identity field | In prose |
|---|---:|---:|---:|
| CD4 | 952 | 226 (23.7%) | 726 |
| CD8 | 737 | 183 (24.8%) | 554 |
| CD27 † | 245 | 12 (4.9%) | 233 |
| CD3 | 141 | 3 (2.1%) | 138 |
| CD20 | 140 | 4 (2.9%) | 136 |
| CD19 | 104 | 4 (3.8%) | 100 |

The table stops at 100 mentions; below it the script also reports CD21 (25),
CD38 (10), CD79a (3), CD138 (1) and CD22 (1).

CD4 and CD8 are the best-represented, but only as a side effect: they ride along
inside CL labels such as `CD8-positive, alpha-beta T cell`. CD19, CD20 and CD3 —
the B-lineage and pan-T markers, and the ones that matter for therapy — have no
CL term to ride on and are therefore almost entirely prose. **79 entries mention
rituximab**; the CD20 it depletes is a sentence in a `description`, not a target.

† **CD27 is in the table because it outranks the three rows below it, but it is
not the same signal, and it should not be read as one.** 217 of its 245 mentions
(89%) come from a single entry, `CD27-related_lymphoproliferative_and_immune_disorder`,
which is named after the gene; the other 28 are scattered across 12 entries. And
none of its 12 identity-field hits is a CL label — they are the disease `name`,
its MONDO `disease_term`, a pathophysiology node name, two `diagnosis` names,
and HGNC **gene** descriptors under `pathophysiology`, `genetic` and `diagnosis`.

That makes CD27 a *different* failure mode from CD4/CD8, and a sharper one for
this report's argument. Where CD27 is bound at all, it is bound as a gene. The
KB can say "the CD27 gene" and it can say "a memory B cell" — it has no way to
say that the cell displays the molecule. A lineage marker is exactly a molecule
displayed by a cell, so the one relation that would make it queryable is the one
missing, and binding the gene does not supply it.

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
  Antibodies` — three unbound strings, with no `biomarker_term` key on any of them. Note
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

Most of this requires no new ontology, but two things do, and they are not the
same size. HLA is cheap: MRO exists and is one `ols:` configuration line (§7a).
Naming an antigen by protein accession is not — dismech has no UniProt binding
at all, and OLS/OAK do not serve UniProt, so that one needs a real decision
rather than a config change (§7a).

| Need | Existing resource |
|---|---|
| Antigen as a protein | `GeneProductDescriptor` (NCIT gene-product hierarchy), `ProteinComplexDescriptor` |
| Antigen as a gene | `GeneDescriptor` (HGNC), already used for COL4A3, HARS1, PLA2R1 |
| Antigen as a small molecule / hapten | `ChemicalEntityDescriptor` (CHEBI) |
| Dietary or environmental antigen | `ExposureDescriptor` (ECTO), `FoodDescriptor` (FOODON) |
| Seropositivity | 26 of those 33 cached HP terms are `... antibody positivity` terms |
| Recognising lineage | B/T-lineage CL bindings already on 531 cohort pathophysiology nodes (2,158 carry some `cell_types`) |
| Attaching an antigen to a node | the `<kind>#<name>` entity-reference grammar |
| Recording *how* an antigen acts | the `ModelMechanismLink` / `influences_mechanisms` link-object pattern |
| HLA serotype, allele, haplotype, presenting complex | **MRO** (IEDB's MHC Restriction Ontology) — not yet in `conf/oak_config.yaml`; see §7a |
| Antigen as a protein, by accession | **UniProt** is the form IEDB publishes antigens in, and dismech has *no* slot that accepts it — see §7a |

The pattern the KB already uses for exactly this shape of problem is the
**link object**: `treatments.target_mechanisms`, `environmental.influences_mechanisms`,
and `animal_models.modeled_mechanisms` all attach a typed, evidence-bearing edge
from an entity to a pathograph node. An antigen link would be the same shape —
antigen descriptor, target node, a recognising-lineage value (B / T / both), and
its own evidence — and would inherit the pathograph rendering and export for
free.

## 7a. Alignment with IEDB

*Added 2026-09-07. All IEDB figures in this section were queried on that date
against `https://query-api.iedb.org`; they are a snapshot, like the rest of this
document.*

The four senses this report separates are not novel distinctions. The Immune
Epitope Database has modelled them for twenty years, its data is public domain,
and its identifiers are already in the CURIE form dismech uses. Two things follow
that change the recommendations above.

### The HLA gap has an ontology, and §5 stops one step short of it

§5 concludes that "the KB has nowhere to put a serotype, an allele or a
haplotype." That is true of dismech's descriptors and remains the finding. But
the resource that fills it exists, is maintained by IEDB, and reaches dismech
through the adapter pattern `conf/oak_config.yaml` already uses:

| §5 calls this unbindable | MRO term |
|---|---|
| `HLA-DQ2` (serotype) | `MRO:0000283` HLA-DQ2 serotype |
| `HLA-B27` (serotype) | `MRO:0000217` HLA-B27 serotype |
| `HLA-DRB1*03:01` (allele) | `MRO:0000703` HLA-DRB1\*03:01 chain |
| the presenting molecule | `MRO:0001284` HLA-DRB1\*03:01 protein complex |
| `HLA-DR3-DQ2` (haplotype) | `MRO:0000005` MHC haplotype, with the `MRO:0000000` *haplotype member of* relation † |

MRO (the MHC Restriction Ontology, PMID:26759709) is an IEDB product. It carries
51,436 terms at version 2026-08-26, is loaded in OLS, and resolves today through
the same `ols:` adapter as HP, GO and CL:

```bash
uv run runoak -i ols:mro info MRO:0000283 MRO:0001620 MRO:0000217
# MRO:0000283 ! HLA-DQ2 serotype
# MRO:0001620 ! HLA protein complex with DQ2 serotype
# MRO:0000217 ! HLA-B27 serotype
```

† `MRO:0000000` is an **object property**, not a class. Its label is as given,
but `runoak -i ols:mro info MRO:0000000` returns 404 — that route serves classes
— and a property cannot be bound through a `reachable_from` dynamic enum the way
the five class terms above can. The config change below covers the classes;
expressing "this allele is a member of that haplotype" needs its own answer.

So adding `MRO: ols:mro` to `conf/oak_config.yaml` is a one-line change, after
which HLA serotypes and alleles — the classes, at least — validate and cache
exactly like every other bound term. This does **not** reopen the backfill §5 closed: the 41 unbound rows still
name no HGNC gene, and binding them to `gene_term` would still be wrong. It
changes which slot they are waiting for, not whether they are waiting.

MRO also separates the **chain** from the **protein complex** — the distinction
§5 needs when it observes that `hgnc:4948` (*HLA-DRB1*) cannot tell the DR15
haplotype of anti-GBM disease from the DRB1\*04 shared epitope of rheumatoid
arthritis. The complex term is what a peptide is presented *by*, so it is the
natural target of the peptide-to-allele link §5 says is missing everywhere.

### IEDB's schema answers the report's central question, and answers it asymmetrically

`bcell_search` and `tcell_search` are parallel tables over the same assay corpus.
Both carry `parent_source_antigen_iri` (a UniProt accession), `disease_iris`,
`assay_iris` (OBI), `host_organism_iri` (NCBITaxon), `qualitative_measure` and
`pubmed_id`. They differ in one place, and the difference is not incidental:

| Human-host records, queried 2026-09-07 | B cell | T cell |
|---|---:|---:|
| with a disease assigned | 1,352,189 | 268,067 |
| with an MHC allele (`mhc_allele_iri`, an MRO term) | **0** | **297,935** |

MHC restriction is a field only the T-cell table ever populates. That is the
strongest available argument against modelling this in dismech as one generic
"antigen" slot shared by both lineages: the recognising lineage determines which
fields are even meaningful. A B-cell antigen link needs an antigen and an
isotype; a T-cell antigen link needs an antigen, an MRO restriction and a
presentation relation. A single slot would leave one of those two permanently
half-empty, which is the failure mode §3a already documents in the `genetic`
block.

### The Celiac exemplar, tested

§6 asserts that in celiac disease B cells target tissue transglutaminase while T
cells target deamidated gliadin peptides on HLA-DQ2/DQ8, and notes that the entry
names the antigen on neither node. IEDB bears out the half of that claim which
is a clean separation, and qualifies the other half:

| Celiac disease, IEDB, queried 2026-09-07 | B cell | T cell |
|---|---:|---:|
| assay records | 824 | 2,748 |
| against TGM2 (`UNIPROT:P21980`) | **256–472** (see §9) | **0** |
| carrying an MRO restriction | 0 | 1,876 |

Zero of 2,748 celiac T-cell records are against TGM2 — a result two independent
counting methods agree on exactly, and the sharpest single finding here. The
B-side claim needs more care than §6 gives it: TGM2 is heavily represented (256
of 824 by server-side filter, 472 by counting the returned column — §9 explains
the spread), but it is **not** the top B-cell antigen. Gliadin `UNIPROT:D2T2K3`
is, at 318.

So the textbook framing holds asymmetrically rather than as a clean swap:
gliadin is seen by both lineages, and TG2 is the antigen seen by only one. The
T-cell antigens are the gliadins (`UNIPROT:D2T2K3`, `UNIPROT:A0A060N479`,
`UNIPROT:Q402I5`), restricted dominantly by `MRO:0001229`
(HLA-DQA1\*05:01/DQB1\*02:01) and `MRO:0001620` (HLA protein complex with DQ2
serotype). The lineage-specific part of the divergence is not a curatorial
hypothesis — it is a zero in a public dataset, addressable by identifier.

### Divergence is disease-specific, which is itself the argument for a slot

Celiac is not the general case, and a recommendation built only on it would be
wrong:

| Disease (IEDB, 2026-09-07) | B-cell records | T-cell records | Dominant antigen |
|---|---:|---:|---|
| celiac disease | 824 | 2,748 | **partly divergent** — TGM2 is B-only (256 vs 0); gliadin leads both |
| type 1 diabetes mellitus | 550 | 4,407 | **overlapping, different leaders** — GAD65 (`UNIPROT:Q05329`) leads the B side, insulin (`UNIPROT:P01308`) the T side |
| myasthenia gravis | 77 | 726 | convergent — AChR α (`UNIPROT:P02708`) leads both |
| pemphigus | 251 | 64 | convergent — DSG3 (`UNIPROT:P32926`) on both, 81 B / 60 T |

There are at least three patterns here, not two. Celiac is a clean split. In
myasthenia gravis both lineages lead on the same protein. Type 1 diabetes is
neither: the repertoires overlap heavily, but the *leading* antigen differs by
lineage — GAD65 on the B side, insulin on the T side, with GAD65 second there.
A curator cannot infer which pattern holds from the disease, and dismech
currently has no field in which to record the answer either way, so the
information is lost precisely where it is most informative. That is a stronger
case for the link object in §7 than a uniform-divergence story would have been.

### What IEDB does not solve

- **Diseases are DOID, not MONDO.** Any join runs through a DOID→MONDO mapping
  and inherits its gaps. Matching on disease *name* is worse: `pemphigus vulgaris`
  returns nothing because IEDB files those records under `pemphigus`, which
  returns 251 B-cell and 64 T-cell records — so a naive name join silently
  under-reports rather than failing.
- **Antigens are UniProt, and nothing in dismech accepts a UniProt accession.**
  `GeneDescriptor` binds `hgnc:`, and `GeneProductDescriptor` — the obvious
  candidate — cannot take one either: its required `GeneProductTerm` is
  `reachable_from: NCIT:C26548`, and the string `UNIPROT` appears nowhere in
  `src/dismech/schema/dismech.yaml` or `conf/oak_config.yaml`, so
  `UNIPROT:P21980` fails term validation today. A protein-level antigen is also
  a different entity from the gene that encodes it, which is the distinction §3a
  shows the `genetic` block collapsing. Unlike the HLA gap this is **not** a
  configuration line: OLS and OAK do not serve UniProt, so the options are a new
  prefix plus fetcher, mapping antigens onto NCIT gene-product terms, or a
  UniProt-typed slot. That decision is out of scope here and is flagged, not
  taken.
- **An assay count is not a mechanism.** These are counts of published
  experiments, weighted by what was studied and fundable. They say what has been
  measured, never what matters — and `qualitative_measure` includes `Negative`
  records, which a naive count silently treats as support.
- **Coverage is uneven and cannot be assumed.** Prevalent, heavily-studied
  autoimmune diseases are deep; rarer entries in this cohort may have nothing.

IEDB data is public domain and its 2024 update is PMID:39558162.

## 8. What this audit deliberately does not decide

- **Whether to change the schema.** The numbers say the information is absent
  from structure; they do not say the cost of adding a slot is worth paying.
  That is a design-decision call (`docs/explanation/design-decisions.md`), and
  the 105 unbound autoantibody strings could equally be addressed by binding
  them to existing HP terms with no schema change at all.
- **Which sense of "different antigens" matters most.** All four are gaps, but
  they are not equally expensive. Note that the one that *looked* mechanical is
  not: §5 shows all 41 unbound HLA rows name a serotype, allele or haplotype
  rather than a gene, so there is no `gene_term` backfill to do. What the HLA
  work needs is somewhere to put an allele and a peptide-to-allele link — and
  §7a finds that MRO already supplies both, reachable through the `ols:` adapter
  dismech already uses. That makes it a smaller job than this report first
  judged, but still a slot decision rather than a sweep.
- **Whether an unbound antigen is a defect.** Many are correctly unbound —
  `Anti-Endomysial Antibodies` names a *tissue staining pattern*, not a molecule,
  and forcing a CURIE onto it would be worse than leaving it. The
  `dismech-terms` rule stands: no term beats a bad one.

## 9. Method and caveats

`scripts/immune_antigen_audit.py` (`just immune-antigen-audit`), offline, over
`kb/disorders/` and `kb/modules/`. Runtime is hardware-bound: ~70 s on a CI
runner, ~3 min 40 s on a throttled container.

The IEDB figures in §7a come from a different method and carry different
caveats. They were obtained by ad-hoc HTTP queries against
`https://query-api.iedb.org` on 2026-09-07, not by the committed script, so
**they do not regenerate with `just immune-antigen-audit`** and are reproducible
only by re-issuing the queries. Counts are exact (`Prefer: count=exact`) rather
than sampled, but they are counts of assay records, so a protein studied often
outranks a protein that matters; `qualitative_measure` includes `Negative`
records, which these totals do not exclude.

**Per-antigen counts are method-dependent, and the tables above disclose the
spread rather than picking a number.** Filtering server-side on
`parent_source_antigen_iri=eq.UNIPROT:P21980` returns 256 celiac B-cell records;
paginating the whole 824-row result and counting that same column in the returned
rows gives 472. The rows involved carry several curated accessions for one
protein — `SRC454731`, `P21980.2` and `NP_004604.2` all appear — so the
server-side equality filter and the projected column do not agree on what counts
as that antigen, and this report does not claim to know which is canonical.
Presence and absence are unaffected: the zero on the celiac T-cell side and the
`0` versus `297,935` MHC split reproduce identically under both methods, and the
whole-table totals (824, 2,748, 550, 4,407, 77, 726) are single-method counts
with no such ambiguity. Ranking within a lineage is also unaffected, since one
method is used throughout a given comparison — which is how the type 1 diabetes
row was corrected: a 500-row sample had suggested GAD65 led the T-cell side, and
full enumeration of all 4,407 rows shows insulin leads it, 1,057 to 692.

**Every count must carry its disease filter, and one in an earlier draft did
not.** The pemphigus row originally reported DSG3 as 145 B / 134 T, which are
corpus-wide counts with no `disease_names` filter; scoped to `pemphigus` the
figures are 81 B / 60 T. The unfiltered number was larger than the whole
denominator it sat next to — pemphigus has 64 T-cell records in total — which is
the tell for this class of mistake, and the reason the query shapes are written
out below rather than left implicit.

Disease selection is by IEDB's own disease *name*, which is DOID-derived and does
not match dismech's MONDO labels: `pemphigus vulgaris` matches nothing while
`pemphigus` matches 251 B-cell and 64 T-cell records, so a name join
under-reports silently.

The queries behind §7a take these shapes:

```bash
BASE=https://query-api.iedb.org
# whole-table count (the Range/Prefer pair returns an exact total, not rows)
curl -s -o /dev/null -D - -H 'Prefer: count=exact' -H 'Range: 0-0' \
  "$BASE/tcell_search?disease_names=cs.%7Bceliac%20disease%7D"
# a disease-scoped, antigen-scoped count — BOTH filters, always
curl -s ... "$BASE/bcell_search?disease_names=cs.%7Bceliac%20disease%7D\
&parent_source_antigen_iri=eq.UNIPROT:P21980"
# the B/T asymmetry
curl -s ... "$BASE/tcell_search?host_organism_iri=eq.NCBITaxon:9606\
&mhc_allele_iri=not.is.null"
```

- **Only three classes can answer the lineage question, and the headline is
  reported over those.** `cell_types` is a slot on `Pathophysiology`,
  `Biochemical` and `ExperimentalModel` only (`FunctionalEffect` has
  `affected_cell_types`). An evidence item or a treatment cannot record a
  lineage, so counting its silence as a gap inflates the rate: 2,694 of the
  3,122 antigen-naming objects (86.3%) are of such classes. The 64% figure is
  taken over the 428 that could carry the slot; the 95% figure over all 3,122 is
  reported alongside it and is a denominator artifact. Eligibility is decided by
  path, because the walker sees raw mappings with no class information: the
  path's last segment must be a member of a `pathophysiology` / `biochemical` /
  `experimental_models` list. That excludes objects nested *inside* an eligible
  one — `pathophysiology[0].evidence[2]` is an EvidenceItem — and treating the
  subtree as eligible would add 907 such objects (495 evidence items, 255
  `downstream` links, 105 `biological_processes` descriptors) and report 88%
  instead of 64%. The test does follow nesting in the other direction, so
  `stages[0].pathophysiology[1]` counts; no antigen-naming object currently sits
  there, so it does not move the 428.
- **"No lineage" is not the same as "no cell types".** Of the 2,967 objects with
  no B/T/APC lineage, 2,892 have an empty or absent cell-type slot and 75 have
  one that names a non-lymphoid cell. The script reports these separately.
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
  counted as unattributed. This biases both unattributed figures *upward*
  slightly; the correction is bounded by the 20 uses of the ambiguous
  `CL:0000542 lymphocyte`.
- **The HLA row classification is a name test, not a curator's judgement.** A
  row counts as bindable only when its `name` is exactly an HGNC HLA gene symbol;
  serotypes, alleles, haplotypes and region descriptions are counted as not
  bindable. "Explained" means the row's `notes` say why it is unbound, matched on
  wording — a row could be deliberate without using those words. One row
  (`Juvenile_Idiopathic_Arthritis` — "Non-HLA immune-susceptibility genes…")
  matches the HLA substring while being about the opposite, and is counted.
- **Attribution is scored on the antigen-naming object itself**, not on its
  parent or siblings. A node whose `description` names an antigen while a sibling
  node carries the B cell counts as unattributed — correctly, since no relation
  between them is recorded, but a human reader would often infer one.
