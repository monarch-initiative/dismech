# ECM Disorder Claim–Evidence Review (2026-07-25)

Correctness review of ten extracellular-matrix (ECM) disorder entries, with the
emphasis on **claim–evidence match**: does each cited snippet actually support the
claim it is attached to, at the strength and scope the entry asserts?

## Scope and method

Ten ECM disorders spanning the major matrix compartments were reviewed:

| Entry | ECM compartment / protein | Evidence items |
|---|---|---|
| `Marfan_Syndrome` | fibrillin-1 microfibril | 118 |
| `Vascular_Ehlers-Danlos_Syndrome` | collagen III | 36 |
| `Ehlers-Danlos_Syndrome_COL5A1-related` | collagen V | 60 |
| `Osteogenesis_Imperfecta_Type_I` | collagen I | 33 |
| `Pseudoxanthoma_Elasticum` | elastic fibre mineralisation (ABCC6/PPi) | 44 |
| `Alport_Syndrome` | collagen IV basement membrane | 60 |
| `Kniest_Dysplasia` | collagen II | 55 |
| `Stickler_Syndrome_Type_1` | collagen II | 58 |
| `Arterial_Tortuosity_Syndrome` | GLUT10 arterial wall matrix | 49 |
| `Dystrophic_Epidermolysis_Bullosa` | collagen VII anchoring fibril | 87 |

**~620 evidence items** were checked in two passes:

1. **Mechanical** — every `snippet` was re-verified as a substring of its
   `references_cache/` file (ellipsis-split, whitespace-normalised).
2. **Semantic** — each snippet was read against the claim's own `description` /
   `frequency` / `supports` / `presence` values, which is the layer no validator
   covers.

The mechanical pass was effectively clean. Six snippets differ from cache only by
Greek-letter transliteration or quote style (β→beta, α→alpha, ⩽→≤, `"`→`'`) — all
faithful quotes that the fuzzy reference validator accepts. **No fabricated
snippets, no wrong-paper PMIDs, and no Named Entity Confusion were found.** Every
finding below comes from the semantic pass.

## Verdict

Three entries — **`Vascular_Ehlers-Danlos_Syndrome`, `Pseudoxanthoma_Elasticum`,
`Arterial_Tortuosity_Syndrome`** — are clean and should be treated as the
reference standard. ATS is the best of the set: it retains a *contradicting*
`PARTIAL` item (TGF-β is not elevated in skin or end-stage vascular tissue) with
the note "included to represent the mechanism faithfully", and it states the
limits of single-case treatment evidence rather than overselling it.

Twenty-six findings in the other seven entries follow, ordered by severity.

---

## High severity

### M1 — `Marfan_Syndrome`: four `REFUTE` items whose explanations all affirm support

`biochemical > Fibrillin-1 Protein` (lines 1048–1075) carries `presence: Abnormal`
and four evidence items, **all** marked `supports: REFUTE`. Every one of the four
explanations states the opposite:

> "The literature indicates that fibrillin-1 protein abnormalities are directly
> linked to Marfan syndrome…" (PMID:8180508, `REFUTE`)

> "The literature highlights the role of fibrillin-1 in the pathogenesis of Marfan
> syndrome…" (PMID:22705998, `REFUTE`)

All four papers support `presence: Abnormal`. If the intent was to refute the
secondary `context:` claim ("not routine diagnostics"), that is nowhere stated,
and PMID:22705998 / PMID:37688493 do not address diagnostics at all. As it stands
the `supports` field is inverted relative to its own explanations.

### M2 — `Marfan_Syndrome`: `prevalence_class` contradicts the record's own rate

Prevalence record 1 (lines 106–111):

```yaml
prevalence_class: BAND_1_5_PER_10000   # = 10–50 per 100,000
rate_low: 5.0
rate_high: 10.0                        # = 0.5–1 per 10,000
```

`BAND_1_9_PER_100000` is the band consistent with the recorded rate. The cited
source (PMID:21308160, "one in 10,000 to 20,000") matches the rate, not the class.

### M3 — `Marfan_Syndrome`: a `REFUTE` that the record actually supports

In the same record, PMID:26631233 (max prevalence **6.5/100,000**) is marked
`REFUTE`. 6.5 lies **inside** the recorded `rate_low: 5.0` – `rate_high: 10.0`
interval, so it supports the record. The explanation compares against
"the 0.01-0.02 percentage range stated in the question" — a value that appears
nowhere in the record (`percentage: 0.005-0.01`). Both explanations in this block
are stale against a superseded earlier version of the claim.

### C1 — `Ehlers-Danlos_Syndrome_COL5A1-related`: `Myopia` has no supporting evidence

The `Myopia` phenotype asserts `frequency: OCCASIONAL` on two evidence items,
neither of which supports it:

- PMID:36237549 (`PARTIAL`) — explanation: "does not specifically mention myopia"
- PMID:30246406 (`NO_EVIDENCE`) — a **feline** case report; explanation: "does not
  mention myopia"

A phenotype with a frequency band and zero supporting evidence should either gain
a real citation or be removed (CLAUDE.md §4, Option C).

### C2 — `Ehlers-Danlos_Syndrome_COL5A1-related`: `Frameshift Mutations` refuted by its own citation

`genetic > COL5A1` lists `Frameshift Mutations` as a variant class (line 479). The
only evidence bearing on it is PMID:2683783 (`NO_EVIDENCE`, a 1989 paper), whose
explanation reads:

> "This reference doesn't support the existence of frameshift mutations in COL5A1,
> making the specific part of the statement regarding frameshift mutations
> unsubstantiated."

The entry states a claim its own evidence explicitly marks unsubstantiated.

### C3 — `Ehlers-Danlos_Syndrome_COL5A1-related`: other-subtype evidence marked `SUPPORT`

`treatments > Supportive Care` cites **PMID:33741806** as `SUPPORT`. That paper is
*"Practical management strategies for benign hypermobility syndromes"* — hEDS/HSD,
a different subtype from COL5A1 classic EDS. The same block cites **PMID:32941194**
(*"Current management of the vascular subtype of Ehlers-Danlos syndrome"*), whose
own explanation concedes it "is different from COL5A1-related EDS". Three of the
five items in this block are `NO_EVIDENCE`. Separately,
`treatments > Gastrointestinal Management` rests on a single `NO_EVIDENCE` item.

### A1 — `Alport_Syndrome`: two human phenotypes supported only by mouse data

`GBM Lamellation` and `Focal Segmental Glomerulosclerosis` are human phenotype
claims whose sole evidence is PMID:34029143, a `Col4a5` mouse study
(`evidence_source: MODEL_ORGANISM`). This contradicts the standing rule that
"model organism evidence should not be the only support for human phenotypes."
GBM basket-weave lamellation is abundantly documented in human biopsy series, so
this is a citation gap rather than a factual error.

### A2 — `Alport_Syndrome`: digenic claim quotes the hypothesis, not the result

The `Digenic inheritance` block quotes PMID:25575550's **BACKGROUND** section:

> "Therefore, we explored the possibility that Alport syndrome is under digenic
> control."

The explanation says this "explicitly establishes digenic inheritance". Exploring a
possibility does not establish it. The same abstract's CONCLUSIONS contain a
directly supporting sentence:

> "This pedigree analysis provides evidence for digenic inheritance of Alport
> syndrome."

as does METHODS ("we identified 11 patients who had pathogenic mutations in two
collagen IV genes"). This matters because CLAUDE.md names Alport as a worked
digenic exemplar. Straightforward snippet swap.

---

## Medium severity

### M4 — `Marfan_Syndrome`: `Aortic Aneurysm` cites a paper about a different disease

PMID:7911041 is a 1994 review, *"Cardiovascular molecular genetics"*. The quoted
sentence concerns **supravalvular aortic stenosis, Williams syndrome and elastin**;
it never mentions aortic aneurysm. It is marked `SUPPORT` with the explanation
"supporting the frequent occurrence of aortic aneurysm and dissection." The claim is
well supported by the other five items in the block, so this one can simply be
dropped. (PMID:36058493 and PMID:32290873 in the same block are also generic
disease-definition sentences that do not speak to aneurysm frequency.)

### M5 — `Marfan_Syndrome`: exercise-benefit trials cited to support activity *restriction*

`environmental > Physical Activity Restrictions` claims "Avoidance of strenuous
isometric exercise and contact sports". Two of its three `SUPPORT` items show the
opposite direction of effect:

- PMID:36453629 — a 10,000-steps/day intervention **slowed** aortic root Z-score
  growth (−0.24 vs +0.008/yr, P=0.01)
- PMID:28947563 — exercise **blunted** aortic root dilation in Marfan mice

The explanations strain to reconcile this ("indirectly supporting the idea that
physical activity restrictions can help"). The nuance is real — moderate dynamic
exercise is beneficial while isometric/contact activity is restricted — but the
claim text does not carry it, and these items should not be `SUPPORT` as written.

### C4 — `Ehlers-Danlos_Syndrome_COL5A1-related`: evidence points away from the claim

`Chronic Joint Pain` (`frequency: FREQUENT`) cites PMID:10906878:

> "Thirty patients with Type III Ehlers-Danlos syndrome reported joint pain more
> frequently than did patients with Types I, II, or IV."

Types I and II *are* classic EDS — the subtype this entry curates. The quote
therefore reports that classic EDS patients had **less** joint pain than
hypermobile-type patients, which does not support a FREQUENT band here.

### C5 — `Ehlers-Danlos_Syndrome_COL5A1-related`: frequency contradicts its own Orphanet row

`Delayed Wound Healing` asserts `frequency: VERY_FREQUENT` (99–80%) while its
ORPHA:287 evidence item — marked `SUPPORT` — reads
`HP:0001058 | Poor wound healing | Frequent (79-30%)`. Either the band should be
FREQUENT, or the conflict should be handled the way `Marfan_Syndrome` handles
spontaneous pneumothorax: keep the curated band, mark the Orphanet item `PARTIAL`,
and record the disagreement in `notes:`.

### C6 — `Ehlers-Danlos_Syndrome_COL5A1-related`: `evidence_source` absent throughout

All 56 literature items in this file omit `evidence_source`. Three are
misclassifiable by default:

- PMID:30246406 — feline COL5A1 EDS case → `MODEL_ORGANISM`
- PMID:2728341 — wound healing in dogs and cats → `MODEL_ORGANISM`
- PMID:15095409 — cultured patient fibroblasts → `IN_VITRO`

Per CLAUDE.md, veterinary observations are `MODEL_ORGANISM`. This is the only file
of the ten with the field systematically unset.

### O1 — `Osteogenesis_Imperfecta_Type_I`: `evidence_source` inconsistent with the rest of the KB

All six ORPHA:666 items use `evidence_source: HUMAN_CLINICAL`. Every other file in
the sample tags Orphanet structured-database rows `OTHER` (Marfan 32/32, Stickler
38/38, vEDS 2/2, cEDS 4/4). Orphanet rows are curated database records, not primary
clinical observations.

### O2 — `Osteogenesis_Imperfecta_Type_I`: spectrum-level bands applied to a subtype entry

ORPHA:666 is **"Osteogenesis imperfecta"** — the whole spectrum, not type I. Five
phenotypes (`Osteoporosis`, `Bone Pain`, `Progressive Hearing Impairment`,
`Wormian Bones`, `Bruising Susceptibility`) adopt the spectrum band as the type I
`frequency:` and mark it `SUPPORT`. `Hyperhidrosis`, in the same file, explicitly
declines to do so:

> "No type I-specific frequency is asserted here because the Orphanet band reflects
> the whole OI spectrum rather than type I alone."

The reasoning is right; it should be applied consistently. Since type I is the
mildest OI form, importing spectrum bands is likely to overstate severity-linked
phenotypes.

### K1 — `Kniest_Dysplasia`: quantitative treatment claim with no evidence

`treatments > Cleft Palate Repair` asserts "Clefting abnormalities are present in
approximately 70% of Kniest dysplasia cases" and carries **no evidence block**. The
supporting datum exists in the file — PMID:25592122's "five of the seven patients
exhibited clefting abnormalities" (71%), cited under the `Cleft Palate` phenotype —
and just needs to be attached here. Otherwise Kniest is one of the strongest entries
reviewed, with quantified, disease-specific evidence on nearly every phenotype.

### S1 — `Stickler_Syndrome_Type_1`: three unreconciled prevalence figures

Three prevalence records disagree by up to an order of magnitude, with no note
reconciling them:

- PMID:40146061 — 1 in 21,844 live births ≈ **4.6/100,000**
- ORPHA:828 — `1-9 / 100 000 | Europe | Point prevalence`
- ORPHA:828 — `1-5 / 10 000 | Worldwide | Prevalence at birth` ≈ **10–50/100,000**

Records 1 and 3 are both birth-referenced and differ ~2–10×. Contrast the same
file's careful handling of the type-1-vs-grouping issue elsewhere. (Incidentally,
the second Orphanet row quotes `PMID:2012` — a year captured as a PMID in the
upstream Orphanet data. The snippet is a faithful quote; the artifact is upstream.)

### S2 — `Stickler_Syndrome_Type_1`: grouping-level frequencies on a subtype entry

Roughly 18 phenotypes (`Arachnodactyly`, `Kyphosis`, `Pectus Carinatum`,
`Spondylolisthesis`, `Hypotonia`, `Chronic Otitis Media`, …) take ORPHA:828 —
the **Stickler syndrome grouping**, all types — verbatim as the STL1 frequency.
The entry does this well twice: `Cataract` is downgraded to FREQUENT with stated
reasoning, and `Membranous Vitreous` is upgraded with stated reasoning. Given the
entry's own statement that STL1 skeletal features are milder than STL2/STL3, the
remaining ~18 deserve the same treatment. Same root cause as **O2**.

### A3 — `Alport_Syndrome`: progression explanation describes content not in its snippet

`progression` record 1 claims "Microscopic hematuria is typically the first clinical
manifestation, present from early childhood in X-linked males." Its evidence
(PMID:32712016) is a generic disease-definition sentence about collagen IV genes and
basement membranes; the explanation reads "Emphasizes the importance of early
diagnosis, supporting childhood onset" — describing the paper's title rather than
the quoted text.

### A4 — `Alport_Syndrome`: over-read screening recommendation

`Microscopic Hematuria` is described as "the earliest and most consistent finding",
supported only by "screening programs for glomerular hematuria in children and young
adults could benefit from inclusion of genetic testing" — a recommendation about
screening programme design, not a statement about earliness or consistency.

### D1 — `Dystrophic_Epidermolysis_Bullosa`: severe-RDEB frequencies asserted at disease level

Seven phenotypes carry a disease-level `frequency:` (mostly `VERY_FREQUENT`, i.e.
80–99% of patients) restricted only by a free-text note:

| Phenotype | frequency | note |
|---|---|---|
| Pseudosyndactyly | VERY_FREQUENT | "Characteristic of severe RDEB" |
| Esophageal Stricture | VERY_FREQUENT | "Primarily in RDEB" |
| Dysphagia | VERY_FREQUENT | "Secondary to esophageal strictures in RDEB" |
| Growth Retardation | VERY_FREQUENT | "Primarily in severe RDEB" |
| Cutaneous SCC | VERY_FREQUENT | "Leading cause of death in severe RDEB" |
| Microstomia | FREQUENT | "Primarily in severe RDEB" |
| Osteoporosis | FREQUENT | "Primarily in severe RDEB" |

The entry's scope includes DDEB, where — by its own subtype description — "nail
dystrophy may be the only manifestation." None of these occur in 80–99% of *all*
DEB patients. The entry defines four subtypes (`DDEB`, `RDEB-sev gen`,
`RDEB-intermediate`, `RDEB-Inversa`) but uses the `subtype:` foreign key **zero
times**, though the schema supports it and `tests/test_data.py` enforces it. Moving
these to `subtype: RDEB-sev gen` would make the scoping machine-readable instead of
prose-only.

---

## Low severity

- **M6 — `Marfan_Syndrome` progression**: two explanations argue a source "does not
  confirm that the onset of Marfan syndrome itself is restricted to
  childhood-adolescence", but the record now reads `age_range: All ages`. Stale text
  from a superseded claim.
- **O3 — `Osteogenesis_Imperfecta_Type_I`**: three snippets are mid-sentence
  line-wrap fragments rather than clean quotes — `"year, one-half of which affected
  the tibia/fibula. Long-bone fracture rate was"` (Osteoporosis),
  `"findings (presence of Wormian bones, platybasia, basilar impression (McGregor's"`
  (Wormian Bones, unbalanced parentheses), `"Other areas included pain,
  gastrointestinal problems,"` (Bone Pain). Each validates as a substring but cuts
  off before the clause the explanation relies on.
- **S3 — `Stickler_Syndrome_Type_1`**: Orphanet rows that *conflict* with the curated
  band are marked `SUPPORT` (Cataract, Membranous Vitreous). `Marfan_Syndrome` marks
  the analogous conflicting pneumothorax row `PARTIAL` — the better pattern.
- **D2 — `Dystrophic_Epidermolysis_Bullosa`**: PMID:19700011 on
  `Esophageal and Mucosal Blistering` quotes "…bone marrow, musculoskeletal system,
  heart, kidney, and teeth" — no esophageal or mucosal content. (Its second use, on
  `Dental Caries`, is apt.)
- **D3 — `Dystrophic_Epidermolysis_Bullosa`**: `Anemia` (VERY_FREQUENT),
  `Osteoporosis` and `Constipation` (FREQUENT) rest on management-list fragments —
  e.g. `"management of constipation"` — that establish the complication is managed,
  not how often it occurs.

---

## Cross-cutting patterns

1. **Grouping/spectrum frequency leakage (O2, S2, D1).** The most common systematic
   problem. A subtype entry inherits `frequency:` from a parent-level source —
   ORPHA:666 (all OI), ORPHA:828 (all Stickler) — or asserts a severe-subtype rate at
   disease level. Three files already contain the correct pattern in miniature
   (OI's Hyperhidrosis note, Stickler's Cataract downgrade, Marfan's pneumothorax
   `PARTIAL` + `notes:`); it is applied inconsistently within the same files.

2. **`supports` drifting from `explanation` (M1, M3, M4, C3, C4, M5).** Where an
   entry is wrong, it is usually the enum and the prose disagreeing rather than a
   bad quote. `REFUTE` items whose explanations affirm support, and `SUPPORT` items
   whose explanations concede non-support, are both present. Worth a lint: flag any
   `REFUTE`/`NO_EVIDENCE` whose explanation lacks negation, and any `SUPPORT` whose
   explanation contains "does not", "but only", or "different from".

3. **`NO_EVIDENCE` items retained as if they were support (C1, C2, C3).** Concentrated
   almost entirely in `Ehlers-Danlos_Syndrome_COL5A1-related`. In two cases a claim's
   *only* evidence is `NO_EVIDENCE`, leaving a frequency-banded phenotype and a
   variant class standing on nothing.

4. **Stale explanations surviving claim edits (M3, M6).** Explanations referencing
   values ("0.01-0.02", "childhood-adolescence") no longer present in the record.
   Because explanations are free text, no validator catches this.

5. **What is working.** No fabrication was found anywhere in ~620 items. The three
   clean entries plus Kniest show the target standard: disease-specific quantified
   quotes, honest `PARTIAL` grading, contradicting evidence preserved rather than
   dropped, and limits of single-case data stated explicitly.

## Disposition

Fourteen findings were fixed in place on `claude/ecm-disorders-review-ky690u`; the
remainder are tracked as issues because they need new literature, clinical input, or
a curation-policy decision.

### Fixed

| Finding | Entry | Fix |
|---|---|---|
| M1 | Marfan | 4 `REFUTE` → `SUPPORT`/`PARTIAL`; dropped one non-bearing item |
| M2 | Marfan | `prevalence_class` → `BAND_1_9_PER_100000`, matching the recorded rate |
| M3 | Marfan | `REFUTE` → `SUPPORT` (6.5/100,000 is inside the interval); stale explanations rewritten |
| M4 | Marfan | Removed PMID:7911041 from `Aortic Aneurysm` |
| M6 | Marfan | Rewrote two stale `progression` explanations |
| C1 | cEDS | Removed unsupported `Myopia` phenotype + its causal edge |
| C2 | cEDS | Removed the `NO_EVIDENCE` item contradicting its own claim |
| C3 | cEDS | Dropped 4 `NO_EVIDENCE` items; hEDS-cohort item `SUPPORT` → `PARTIAL` |
| C5 | cEDS | `Delayed Wound Healing` `VERY_FREQUENT` → `FREQUENT` |
| C6 | cEDS | `evidence_source` added where unambiguous (5 items) |
| O1 | OI type I | 6 ORPHA rows `HUMAN_CLINICAL` → `OTHER` |
| O3 | OI type I | 3 truncated snippets replaced with clean sentences |
| A2 | Alport | Digenic snippet swapped for the paper's METHODS + CONCLUSIONS |
| K1 | Kniest | Attached the 5/7 clefting evidence to `Cleft Palate Repair` |
| S3 | Stickler | 2 conflicting Orphanet rows `SUPPORT` → `PARTIAL` |
| D2 | DEB | Removed the mismatched citation from the mucosal-blistering node |

All seven edited files pass `linkml-validate`; the full `tests/test_data.py` suite
passes (1648 tests); and every snippet still substring-matches its cache file.

### Tracked as issues

| Issue | Findings | Why deferred |
|---|---|---|
| [#6951](https://github.com/monarch-initiative/dismech/issues/6951) | O2, S2, D1 | Grouping/spectrum `frequency:` leakage — needs a curation policy plus a DEB `subtype:` migration |
| [#6952](https://github.com/monarch-initiative/dismech/issues/6952) | A1, A3, A4 | Alport phenotypes needing human citations |
| [#6953](https://github.com/monarch-initiative/dismech/issues/6953) | M5 | Exercise direction-of-effect — needs clinical input on dynamic vs isometric framing |
| [#6954](https://github.com/monarch-initiative/dismech/issues/6954) | C4, C6 (bulk) | ~45 remaining `evidence_source` tags; uncited frameshift variant class; cross-subtype pain evidence |
| [#6955](https://github.com/monarch-initiative/dismech/issues/6955) | cross-cutting | QC proposal: lint `supports` enums against their own `explanation` |
| [#6956](https://github.com/monarch-initiative/dismech/issues/6956) | S1 | Stickler prevalence reconciliation — needs epidemiology judgment |

### Note on tooling

`linkml-reference-validator` reports `Total checks: 0` in this environment, including
on files untouched by these edits — an environmental issue, not a content one.
Snippet verification here was done with an offline substring checker against
`references_cache/` implementing the same contract (ellipsis-split, whitespace- and
Unicode-normalised).
