# ICD-O morphology enum: completeness review against the knowledge base

**Date:** 2026-08-27
**Scope:** `ICDOMorphologyEnum` in
[`src/dismech/schema/classifications/icdo_morphology.yaml`](https://github.com/monarch-initiative/dismech/blob/main/src/dismech/schema/classifications/icdo_morphology.yaml),
bound to `classifications.icdo_morphology`.
**Related:** monarch-initiative/dismech#7548 (schema decision: four-digit ICD-O
codes and a behaviour slot — still open, and not addressed here).
**Companion:**
[`cancer-taxonomy-granularity-review-2026-08-28.md`](cancer-taxonomy-granularity-review-2026-08-28.md)
covers the adjacent question — which cancer concepts get a `Disease` entry at
all. It is about entry granularity; this report is about the morphology
*annotation* those entries carry. The two are independent: an entry at any of
its eight strata still needs a correct `icdo_morphology` value.

## The finding

The vocabulary was **not** complete. All ten of its original values carried an
ICD-O behaviour digit of `/3`, so it was a *malignant-only* histogenetic bucket
wearing the name of the full ICD-O morphology axis. That had two consequences in
the committed knowledge base:

1. **Neoplastic entries with no correct value simply went unclassified**, and
   four of them wrote the gap down in prose — Glomus Tumor (a `CURATION_TODO`
   discussion), Choriocarcinoma, Pheochromocytoma-Paraganglioma and
   GNAS-related pituitary adenoma 3. Those four notes are what this review acted
   on; they are the reason the omit-and-explain convention is worth keeping.
2. **Entries with no correct value took a wrong one.** Mesothelioma was tagged
   `Carcinoma`; polycythaemia vera, essential thrombocythaemia and primary
   myelofibrosis were tagged `Leukemia`; four germ cell entries were tagged
   `Embryonal Neoplasm`, an unrelated axis.

At review time 133 of ~280 neoplastic entries carried a value, and one value
(`Multiple Myeloma`) was used by nothing.

## The rule now written into the enum

A value names a morphology **family**, not an individual tumour entity. A family
earns a value when the knowledge base holds entries no existing value can hold
correctly *and* it is a top-level morphology group in ICD-O / the WHO
classification. A sub-family is split out of its parent only when it dominates
curation practice — which is why `Adenocarcinoma` and `Squamous Cell Carcinoma`
sit beside `Carcinoma`, and `Multiple Myeloma` beside `Plasma Cell Neoplasm`,
while single entities (glomus tumour, chordoma, GIST) are held by a family
rather than given a value of their own.

Most new values are **behaviour-neutral**: `Nerve Sheath Neoplasm` covers
schwannoma and MPNST alike. Where ICD-O itself splits a family on behaviour, the
values follow it (`Adenoma` vs `Adenocarcinoma`). This is what unblocked Glomus
Tumor: the objection to `Sarcoma` was never that the tumour is not mesenchymal,
it was that `Sarcoma` asserts malignancy for an entity that is usually benign. A
behaviour-neutral family value makes no such claim.

## Values added (13)

Every `meaning` was checked against the NCI EVS REST API on 2026-08-27 for
active status, preferred label and `ICD-O-3_Code`; every `exact_mappings` MONDO
term was checked against OLS4 for non-obsolescence. An `ICDO:` mapping is
recorded **only** where the bound NCIT concept itself carries an
`ICD-O-3_Code` annotation, rather than hand-typing a code.

| Value | NCIT | ICD-O-3 | KB entries it unblocks |
|---|---|---|---|
| `Adenoma` | C2855 | 8140/0 | adrenal cortical adenoma, the five pituitary adenoma entries, mucinous cystadenoma, the adenomatous polyposis entries |
| `Trophoblastic Tumor` | C3422 | — | choriocarcinoma, gestational trophoblastic neoplasm |
| `Mesothelial Neoplasm` | C3786 | — | pleural and peritoneal mesothelioma |
| `Pericytic Neoplasm` | C6528 | — | glomus tumour |
| `Nerve Sheath Neoplasm` | C4972 | — | schwannoma, neurofibroma, granular cell tumour, MPNST, the neurofibromatosis entries |
| `Meningioma` | C3230 | 9530/0 | meningioma |
| `Germ Cell Tumor` | C3708 | — | seminoma, embryonal carcinoma, yolk sac tumour, mixed and ovarian/testicular/CNS germ cell tumours |
| `Sex Cord-Stromal Tumor` | C3794 | 8590/1 | granulosa cell tumour, Sertoli-Leydig cell tumour, testicular sex cord-stromal neoplasm |
| `Neuroendocrine Neoplasm` | C3809 | — | phaeochromocytoma-paraganglioma, pancreatic and GEP NETs, large-cell and small-cell neuroendocrine carcinoma |
| `Plasma Cell Neoplasm` | C4665 | — | plasma cell neoplasm (family), AL amyloidosis, POEMS |
| `Myeloproliferative Neoplasm` | C4345 | 9960/3 | polycythaemia vera, essential thrombocythaemia, primary myelofibrosis, MPN-U |
| `Myelodysplastic Syndrome` | C3247 | 9989/3 | myelodysplastic syndrome |
| `Histiocytic and Dendritic Cell Neoplasm` | C9294 | — | Langerhans cell histiocytosis, Rosai-Dorfman disease |

One correction to the research recorded on #7548: **NCIT:C3234 (Mesothelioma) is
a retired concept** (`conceptStatus = Retired_Concept`, `active = false`,
parented under "Retired Concept 2023"). `Mesothelial Neoplasm` is bound to
**NCIT:C3786** instead, which is active and sits directly under NCIT's *Neoplasm
by Morphology* axis.

That retirement propagates into MONDO, and it is worth stating because it caught
this review out. `MONDO:0005065` "mesothelioma" is the obvious-looking mapping
and is the wrong one twice over: it still xrefs the retired `NCIT:C3234`, and
its definition — "a **usually malignant** and aggressive neoplasm of the
mesothelium" — is behaviour-leaning, which is precisely what a behaviour-neutral
family value must not assert. The correct term is **`MONDO:0006856`
"mesothelial neoplasm"**, which xrefs `NCIT:C3786` and is defined as "a benign
or malignant neoplasm arising from mesothelial cells".

The general check, which is cheap and worth running on any future addition:
**the MONDO term should carry a `database_cross_reference` to the same NCIT code
the value's `meaning` binds.** All thirteen values here satisfy it.

### No `Other` value

#7548 suggested adding one. This review deliberately did not. The four prose
notes that drove this expansion only exist because curators had nowhere to put a
value and wrote down why; an `Other` bucket would have absorbed exactly those
signals and left the vocabulary frozen. The convention is now stated in the enum
description and the `disease-classification` skill: **when no value fits, omit
the slot and record why** in `notes` or a `CURATION_TODO` discussion.

## Entries changed (31)

**Nine corrections** — values that asserted the wrong histogenesis:

| Entry | Was | Now |
|---|---|---|
| `Malignant_Mesothelioma` | Carcinoma | Mesothelial Neoplasm |
| `Choriocarcinoma` | Carcinoma | Trophoblastic Tumor |
| `Polycythemia_Vera` | Leukemia | Myeloproliferative Neoplasm |
| `Essential_Thrombocythemia` | Leukemia | Myeloproliferative Neoplasm |
| `Primary_Myelofibrosis` | Leukemia | Myeloproliferative Neoplasm |
| `Testicular_Seminoma` | Embryonal Neoplasm | Germ Cell Tumor |
| `Embryonal_Carcinoma` | Embryonal Neoplasm | Germ Cell Tumor |
| `Mixed_Germ_Cell_Tumor` | Embryonal Neoplasm | Germ Cell Tumor |
| `Malignant_Germ_Cell_Tumor_of_Ovary` | Embryonal Neoplasm | Germ Cell Tumor |

The germ cell group is the sharpest case. NCIT:C3752 (Embryonal Carcinoma) has
parents *Malignant Germ Cell Tumor* and *Nongerminomatous Germ Cell Tumor*,
both under NCIT:C3708; the children of NCIT:C3264 (Embryonal Neoplasm) are the
blastomas, the CNS embryonal tumours, Ewing sarcoma/pPNET, rhabdoid tumour and
Wilms tumour. The old value was a name collision, not a classification.

**Twenty-one exemplars** backfilled to exercise each new value, at least one per
value, each carrying a `notes` line recording the NCIT ancestry it rests on:
adrenal cortex adenoma, GNAS-related pituitary adenoma 3, gestational
trophoblastic neoplasm, malignant peritoneal mesothelioma,
glomus tumour, schwannoma, neurofibroma, granular cell tumour, meningioma,
yolk sac tumour, testicular germ cell tumour, adult granulosa cell tumour of
ovary, testicular sex cord-stromal neoplasm, pheochromocytoma-paraganglioma,
pancreatic neuroendocrine tumour, plasma cell neoplasm, multiple myeloma,
myeloproliferative neoplasm unclassifiable, myelodysplastic syndrome,
Langerhans cell histiocytosis, Rosai-Dorfman disease.

**And one exemplar withdrawn.** `Hydatidiform_Mole` was assigned
`Trophoblastic Tumor` in an earlier draft of this PR and the assignment has
been removed, because it failed the same rule every other value passes.
Hydatidiform mole does carry ICD-O morphology codes — 9100/0 for the mole NOS,
9103/0 for the partial mole — which is what made it look assignable. But
`NCIT:C3110` (Hydatidiform Mole) does not descend from `NCIT:C3422`
(Trophoblastic Tumor): its parents are *Gestational Trophoblastic Disorder* and
*Placenta Disorder*, NCIT asserts no `Neoplastic_Status` for it, and both
`NCIT:C4871` (Complete) and `NCIT:C4293` (Partial Hydatidiform Mole) sit under
*Placental Non-Neoplastic Disorder*. WHO agrees — gestational trophoblastic
*neoplasia* is invasive mole, choriocarcinoma, PSTT and ETT, and a non-invasive
mole is GTD but not GTN. This axis applies only to neoplastic diseases, so the
entry now omits the slot and records why, which is the convention this review
argues for. The molar pregnancies that do progress are covered by
`Gestational_Trophoblastic_Neoplasm`, which carries the value correctly.

Every one of the 23 values is now used by at least one entry — `Multiple
Myeloma`, unused since the enum was written, went to the `Multiple_Myeloma`
entry. The KB now carries 158 `icdo_morphology` assignments in total. (Note
that the raw before/after pair is not a clean measure of this PR: the branch
was rebased mid-review and picked up neoplastic entries added on `main` in the
meantime, so the denominator moved underneath it.)

The prose notes on Glomus Tumor, Choriocarcinoma,
Pheochromocytoma-Paraganglioma and GNAS-related pituitary adenoma 3 were
rewritten to say what is now assignable and what is still blocked. The Glomus
Tumor `CURATION_TODO` discussion **stays open**: the morphology half is solved,
the four-digit codes (8711/0 benign; 8710/3 and 8711/3 for glomangiosarcoma,
both on NCIT:C4221) and the behaviour digit are not.

## What is still not covered

These are families that remain without a home. None passed the ≥1-KB-entry *and*
top-level-ICD-O-group test cleanly enough to add in this pass, but they are the
next candidates if more entries accumulate:

| Family | KB entries | Note |
|---|---|---|
| Thymic epithelial neoplasms | `Thymoma`, `Thymus_Neoplasm` | NCIT:C3411 Thymoma is ICD-O 8580/**1**, under *Thymus Epithelial Neoplasm*; `Carcinoma` asserts both malignancy and the wrong histology |
| Gastrointestinal stromal tumour | `Gastrointestinal_Stromal_Tumor` | NCIT:C3868, ICD-O 8936/**1**, parent *Stromal Neoplasm*. Left at `Sarcoma`, which overstates behaviour. A single entity, not a family — the right fix is the behaviour slot from #7548, not a new value |
| Mast cell neoplasms | `Systemic_Mastocytosis`, `Maculopapular_Cutaneous_Mastocytosis` | NCIT parents *Mastocytosis* → *Mast Cell Neoplasm*; not histiocytic/dendritic, and WHO no longer files mastocytosis under MPN |
| Fibroblastic/myofibroblastic | `Solitary_Fibrous_Tumor`, `Inflammatory_Myofibroblastic_Tumor`, `Infantile_Myofibromatosis` | NCIT *Fibroblastic Neoplasm*; ICD-O 8815/0, 8815/1 and 9051/0 all on C7634 |
| Perivascular epithelioid cell (PEComa) | `Perivascular_Epithelioid_Cell_Neoplasm`, `Lymphangioleiomyomatosis` | NCIT files these under *Soft Tissue Neoplasm of Uncertain Differentiation*, **not** under *Pericytic Neoplasm* — do not reach for the new value here |
| Odontogenic | `Ameloblastoma` | |
| Craniopharyngioma | `Craniopharyngioma` | NCIT:C2964, ICD-O 9350/1, parents include *Benign Squamous Cell Neoplasm* — `Squamous Cell Carcinoma` would be wrong twice over |
| Benign melanocytic | `Nevus_of_Ota`, `Meningeal_Melanocytoma` | `Melanoma` is malignant-only |
| Neuronal and mixed neuronal-glial | `Dysembryoplastic_Neuroepithelial_Tumor`, `Mixed_Neuronal-Glial_Tumor` | not purely glial |
| Benign mesenchymal / fibroepithelial | `Uterine_Leiomyoma`, `Breast_Fibroadenoma`, `Bone_Giant_Cell_Tumor` | `Sarcoma` asserts malignancy |

One entry that *looks* uncovered is not: **`Chordoma`** is assignable as
`Embryonal Neoplasm` today, because NCIT:C2947 (Chordoma) sits under
*Notochordal Tumor*, a direct child of NCIT:C3264. It is left unassigned pending
a curator who is comfortable with that placement rather than assigned on the
strength of the ontology path alone.

Separately, roughly 120 neoplastic entries carry **no** `icdo_morphology`
despite an existing value fitting them (colon adenocarcinoma, Hodgkin lymphoma,
osteosarcoma, angiosarcoma, hairy cell leukaemia, MALT lymphoma, and so on).
That is a curation backlog, not a vocabulary gap, and is out of scope here.

## A note for the next enum extension

A change like this one needs the **`scope-override` label** on its PR. CI's
curation-scope guard fails any PR that touches `kb/` *and* anything outside
`kb/`, `stubs/`, `history/`, `cache/`, `references_cache/`, `research/`,
`pages/` or `dashboard/` — and an enum extension is inherently both halves at
once: the schema value and the entries that exercise it. Splitting them is
worse, not better, because the KB half cannot validate until the schema half
has merged. The guard exists to catch curation PRs that pick up infra changes
by accident; this is the intentional case it provides the label for.

## What this review did not do

Everything in #7548 that needs a schema decision rather than a vocabulary
extension is untouched and still assigned to @cmungall:

- `DiseaseMappings.icdo_mappings` for the four-digit `NNNN/N` code (multivalued
  — NCIT:C4221 carries two).
- A first-class `neoplastic_behavior` slot for the ICD-O `/0`–`/3` digit.
- Ingesting `NCIT:P334` (`ICD-O-3_Code`) and `NCIT:P363` (`Neoplastic_Status`)
  through `OntologyEdgeSource` so those assertions become snippet-validated
  evidence.

The generated `src/dismech/datamodel/dismech_pydantic.py` was **not**
regenerated: it is already ~12,500 diff lines stale against `main`'s schema, so
regenerating it here would bury this change. Nothing in the repository imports
it and no test checks it, but it is worth a dedicated refresh PR.
