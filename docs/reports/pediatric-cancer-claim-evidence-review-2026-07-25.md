# Pediatric Cancer Entries: Claim–Evidence Correctness Review (2026-07-25)

Review of ten pediatric cancer entries in `kb/disorders/`, focused on whether each
evidence item's `snippet` actually supports the claim it is attached to. The
automated stack (`linkml-validate`, `linkml-term-validator`,
`linkml-reference-validator`) verifies that snippets are *substrings of the cited
abstract* and that ontology terms resolve — it cannot verify that a real quote
*supports the specific assertion* it is attached to. That semantic gap is what
this review covers.

## Entries reviewed

| Entry | Evidence items | Verdict |
|---|---|---|
| `Acute_Lymphoblastic_Leukemia` | 88 | Exemplary |
| `Hepatoblastoma` | 55 | Exemplary |
| `Atypical_Teratoid_Rhabdoid_Tumor` | 38 | Strong (low-value DR stubs) |
| `Alveolar_Rhabdomyosarcoma` | 79 | Strong (1 frequency error) |
| `Medulloblastoma` | 6 | Sound but thin |
| `Osteosarcoma` | 31 | Sound; metadata gaps |
| `Ewing_Sarcoma` | 130 | Deep content, systematic snippet defect |
| `Wilms_Tumor` | 65 | Several claim–evidence mismatches |
| `Neuroblastoma` | 10 | Model-system evidence carrying human claims |
| `Retinoblastoma` | 5 | Thin; unevidenced frequencies |

## Automated validation baseline

All ten pass all three validators:

- `linkml-term-validator`: `✅ All 10 files passed validation`
- `linkml-reference-validator`: 0 issues per file (every snippet is a genuine
  substring of its cached reference)
- MONDO `disease_term` bindings all correct; every `conforms_to` module-node
  reference resolves

No fabricated PMIDs, no misquoted snippets, and no hallucinated ontology terms
were found. Every issue below is a *semantic* claim–evidence problem that the
validators are structurally unable to catch.

---

## A. Internal contradiction

### A1. `Wilms_Tumor` — TP53 frequency contradicts itself and its own evidence

`genetic[6].notes` (line ~1241) states:

> TP53 mutations are found in approximately 50-60% of diffuse anaplastic Wilms tumors.

`histopathology[4].description` (line ~1050) states the opposite:

> Nearly all anaplastic Wilms tumors harbor TP53 mutations.

Both cite **the same** PMID:33394739 snippet:

> "...indicated that nearly all anaplastic WT have TP53 mutations if one looks hard enough"

and both explanations read "Confirms near-universal TP53 mutation". The 50-60%
figure is contradicted by the evidence attached to it and by the sibling section.
Recommend dropping the 50-60% and aligning `genetic[6]` with the cited "nearly
all" wording.

---

## B. Frequency bands unsupported or contradicted by the cited evidence

Per [`docs/frequency-evidence-guidelines.md`](../frequency-evidence-guidelines.md),
a `frequency:` band is a separate quantitative claim needing its own support.

### B1. `Wilms_Tumor` — same snippet read two different ways

Four phenotypes cite one snippet:

> "However, up to 35% of patients can present with either hematuria, hypertension, fever, or flank pain"

| Phenotype | Assigned band |
|---|---|
| Hematuria | `FREQUENT` (30–79%) |
| Hypertension | `FREQUENT` (30–79%) |
| Fever | `OCCASIONAL` (5–29%) |
| Abdominal Pain | `OCCASIONAL` (5–29%) |

≤35% is the ceiling for the *union* of all four symptoms, so no individual
symptom can reach 30–79% unless it accounts for nearly the entire 35%. Hematuria
and Hypertension should be `OCCASIONAL`, matching how the same sentence was read
for the other two.

### B2. `Alveolar_Rhabdomyosarcoma` — band contradicts its own number

`phenotypes[3]` Metastatic Disease is `FREQUENT` (30–79%); its sole evidence
(PMID:40790568) reads:

> "Seventeen (13.3%) patients had metastatic disease at diagnosis, primarily to the lungs"

13.3% is the `OCCASIONAL` band.

### B3. `Ewing_Sarcoma` — survival statistics cited to support a frequency

`phenotypes[4]` Metastatic Disease is `FREQUENT`, supported by three snippets
that all report **survival in** metastatic disease, never its frequency:

- "lowers the five-year survival rate to 20% to 30%" (PMID:30215968)
- "an approximately 10-30% 5-year event-free survival rate" (PMID:17301523)
- "The 3-year EFS estimates were 37.4%" (PMID:36669140)

None of these is a frequency of metastatic presentation.

### B4. Unevidenced frequency bands

| Entry | Phenotypes with `frequency:` | …of which carry no evidence at all |
|---|---|---|
| `Retinoblastoma` | 5/5 | **5** |
| `Neuroblastoma` | 7/7 | **6** |
| `Ewing_Sarcoma` | 7/7 | **5** |
| `Alveolar_Rhabdomyosarcoma` | 4/4 | 1 |

`Medulloblastoma` and `Atypical_Teratoid_Rhabdoid_Tumor` assign **no** frequency
bands at all and evidence every phenotype — the safer pattern when a
quantitative source is not at hand.

---

## C. Numbers asserted in prose that the attached evidence does not carry

### C1. `Wilms_Tumor` — one aggregate statistic split into three per-gene figures

`pathophysiology[1]` (WTX/AMER1 "approximately 15-20%"), `pathophysiology[2]`
(CTNNB1 "approximately 15%"), `genetic[1]` and `genetic[2]` all cite the same
PMID:25018051 snippet:

> "mutations of Wnt/β-catenin pathway-related WT1, β-catenin, and WTX together account for about one-third of Wilms tumor cases"

An aggregate for three genes cannot support the individual per-gene percentages.

### C2. `Wilms_Tumor` — other unsupported specifics

- IGF2 loss of imprinting "approximately 70% of Wilms tumors" (`pathophysiology[5]`,
  `genetic[3]`) cited to "closely associated with the development of **many** Wilms tumors".
- `genetic[7]` asserts "Wilms tumor cells lacking microRNAs are sensitized to
  ferroptotic cell death through inhibition of GPX4" — the cited snippet mentions
  neither ferroptosis nor GPX4.
- `phenotypes[4]` Aniridia attributes the phenotype to "contiguous deletion of WT1
  and PAX6 on chromosome 11p13"; the snippet only lists WAGR component features.

### C3. `Wilms_Tumor` — explanation asserts the opposite of its snippet

`genetic[5]` (Combined LOH 1p/16q) explanation: *"Confirms frequency and
prognostic relevance"*. The snippet says:

> "Combined LOH 1p and 16q has **limited impact as a prognostic marker** because only 5% of favorable histology WT carry this molecular change."

The snippet supports the 5% frequency; it argues *against* the prognostic-relevance
framing.

### C4. `Neuroblastoma` — percentages with no numeric source

MYCN "approximately 20% of cases" (`has_subtypes[0]`, `genetic[0]`,
`pathophysiology[1]`) and ALK "8-10% of sporadic and ~50% of familial"
(`pathophysiology[2]`, `genetic[1]`) are each supported only by snippets that
contain no percentage:

> "MYCN amplification is a key factor contributing to the poor prognosis of NB."
> "The primary predisposition genes in familial neuroblastoma are ALK and PHOX2B."

---

## D. Evidence-source classification

### D1. `Neuroblastoma` — an in-vitro/xenograft model carrying human clinical claims

PMID:41560679 is the sole support for **5 of 10** evidence items in the entry.
Its own abstract describes iPSC-derived cranial neural crest cells transplanted
into immunodeficient mice, explicitly calling the system "an **in vitro** model".
It is cited to support human epidemiologic and prognostic assertions:

- MYCN amplification in ~20% of cases, "the most powerful adverse prognostic marker"
- ALK activation frequencies
- `genetic[2]`: "1p deletion, 11q deletion, and 17q gain are associated with worse
  prognosis and help define risk stratification" — the snippet reports **NF1 loss
  and 17q gain acquired in the cell model**, and says nothing about 1p, 11q, or
  prognosis.

This conflicts with the CLAUDE.md rule that model-organism evidence should not be
the only support for human phenotypes. Two of the five items
(`pathophysiology[0].evidence[0]`, `[1]`) carry **no** `evidence_source`, so they
silently default to `HUMAN_CLINICAL` for a cell/xenograft paper.

### D2. Missing `evidence_source` generally

| Entry | Evidence items missing `evidence_source` |
|---|---|
| `Osteosarcoma` | 24 / 31 |
| `Retinoblastoma` | 4 / 5 |
| `Neuroblastoma` | 3 / 10 |
| `Ewing_Sarcoma` | 2 / 130 |
| `Alveolar_Rhabdomyosarcoma` | 1 / 79 |

Absent values default to `HUMAN_CLINICAL`, which is wrong for several of the
Osteosarcoma citations (e.g. PMID:25704303, a PI3K/Akt review of largely in-vitro
work).

---

## E. Snippet integrity — a systematic extraction artifact in `Ewing_Sarcoma`

`Ewing_Sarcoma` snippets were harvested **line-by-line from the line-wrapped
cache file** rather than as whole sentences. Measured directly:

| Entry | PMID snippets that are *exactly one wrapped line* of the cached abstract |
|---|---|
| `Ewing_Sarcoma` | **37 / 130** |
| `Acute_Lymphoblastic_Leukemia` | 0 / 88 |
| `Hepatoblastoma` | 0 / 55 |
| `Atypical_Teratoid_Rhabdoid_Tumor` | 0 / 28 |

22 snippets end on a dangling function word. Examples:

- `pathophysiology[0].evidence[1]`: `"It is associated in 85% of cases with the"` — the
  explanation claims this "directly supports the 85% frequency of EWS-FLI1
  translocation", but the fragment never says what "it" is or what the 85% refers to.
- `pathophysiology[1].evidence[0]`: `"recruited by the EWS-FLI1 fusion protein to tumor-specific enhancers and"`
- `pathophysiology[2].evidence[0]`: `"forms dynamic, sub-diffraction-limit hubs with mechanisms of dissolution that"`
- `pathophysiology[5].evidence[2]`: `"had longer alleles (>135"` — clipped mid-number
- `pathophysiology[12].evidence[0]`: `"contacts. Moreover, loss of STAG2 also disrupted PRC2-mediated regulation of"` — begins mid-sentence
- `pathophysiology[2].evidence[3]`: `"depletion promoted a pro-metastatic phenotype"` — no subject; the claim concerns
  EWS-FLI1 depletion but the fragment does not name it

**Important:** I checked the source abstracts for several of these and the
underlying sentences *do* support the claims. This is not fabrication — the
science is right. But the snippets defeat the purpose of snippet verification: a
human or agent reviewer cannot confirm support without re-fetching the paper,
while `linkml-reference-validator` passes them because they are technically
substrings. Re-extracting these 37 snippets at sentence boundaries would restore
auditability without changing a single claim.

---

## F. Weak or tangential evidence attachments

- **`Osteosarcoma` `treatments[1]`** — claim specifies the MAP regimen
  (methotrexate, doxorubicin, cisplatin); both snippets say only "multi-agent
  chemotherapy". The named agents are unevidenced.
- **`Osteosarcoma` `phenotypes[2]`** — claim is that lung is the most common
  metastatic site and the primary cause of mortality; `evidence[1]` is "CT imaging
  of the chest should be performed to identify lung nodules" (staging workup,
  not the claim). `evidence[0]` does support it.
- **`Hepatoblastoma` `pathophysiology[5].evidence[1]`** — claim is that
  β-catenin/YAP1-driven growth "can be attenuated experimentally by pathway
  inhibition"; the cited result is **rapamycin** (mTOR inhibition), a different
  pathway. The explanation hedges appropriately but the support is indirect.
- **`Alveolar_Rhabdomyosarcoma`** — `treatments[0]` names the VAC regimen but is
  supported only by "Despite intensive multimodal therapy, outcomes remain poor";
  PMID:41038289 *elsewhere in the same file* explicitly names VAC and could be
  attached here. `biochemical[1]` claims desmin and a "diffuse strong nuclear
  positivity" discriminator not present in the snippet. `biochemical[0]` claims
  "fusion status is more predictive of outcome than histologic classification" —
  unevidenced.
- **`Acute_Lymphoblastic_Leukemia`** — the ELN boilerplate "The current
  recommendation summarizes clinical management. It covers treatment approaches…"
  is attached to three separate treatment claims. It is a table-of-contents
  sentence that supports nothing specific.
- **`Atypical_Teratoid_Rhabdoid_Tumor`** — 10 `references[].findings[].evidence[]`
  stubs whose explanation is verbatim "Deep research cited this publication as
  relevant literature for Atypical Teratoid Rhabdoid Tumor" and whose snippet is
  the paper's opening sentence. No claim is asserted; these inflate the evidence
  count without adding auditable support.
- **`Retinoblastoma`** — five phenotypes, no evidence on any of them; `biochemical[0]`
  ("RB1 Genetic Testing") is notes-only. The entry's factual content is correct
  but almost entirely unevidenced.
- **`Medulloblastoma`** — `phenotypes[3]` (Macrocephaly) and `[4]` (Papilledema) are
  supported by mixed-histology pediatric brain-tumor series rather than
  medulloblastoma-specific data. The explanations disclose this, which is the
  right handling, but the support is indirect.

---

## What is working well

Three entries are models for the rest of the KB:

- **`Acute_Lymphoblastic_Leukemia`** — node descriptions explicitly scope their own
  claims ("This node is limited to those two kinase-defined contexts and does not
  generalize kinase dependence to every B-ALL subtype"), causal edges that traverse
  unstated intermediates are marked `PARTIAL`, and percentages are deliberately
  left inside the quotation rather than promoted to structured fields ("the
  percentage is retained only inside the exact cohort-review quotation and is not
  encoded as a universal frequency field"). This is exactly the discipline missing
  in §C.
- **`Hepatoblastoma`** — splits a single PMID's evidence into `HUMAN_CLINICAL`,
  `MODEL_ORGANISM`, and `IN_VITRO` items according to *which experiment in the paper*
  supports each claim (PMID:24837480 used three ways). This is the correct
  interpretation of `evidence_source` and the direct fix pattern for §D.
- **`Alveolar_Rhabdomyosarcoma`** — mechanistic hypotheses, `discussions` with
  `proposed_experiments`, and edge descriptions that state what the evidence does
  *not* establish ("This does not by itself prove that FGFR signaling maintains
  the upstream chromatin state").

## Suggested priority

1. `Wilms_Tumor` A1 (self-contradiction) and C3 (explanation inverts its snippet)
2. Frequency bands B1–B3 (three bands contradicted by their own cited numbers)
3. `Neuroblastoma` D1 — re-source the human prognostic claims; set
   `evidence_source` on the iPSC/xenograft items
4. `Ewing_Sarcoma` E — re-extract the 37 line-clipped snippets at sentence boundaries
5. Backfill `evidence_source` in `Osteosarcoma` (24 items) and `Retinoblastoma` (4)
6. Drop or evidence the unevidenced frequency bands (B4)

## Method

```bash
scripts/run_reference_validator.sh validate data kb/disorders/<F>.yaml \
  --schema src/dismech/schema/dismech.yaml --target-class Disease \
  --config conf/reference_validator_config.yaml
scripts/run_term_validator.sh validate-data kb/disorders/*.yaml \
  -s src/dismech/schema/dismech.yaml -t Disease --labels -c conf/oak_config.yaml
```

Every evidence item was then extracted with its enclosing claim (node/phenotype/
gene/treatment name plus description) and read against its snippet and
explanation. Cached abstracts in `references_cache/` were consulted directly for
the truncated-snippet and evidence-source findings. No KB files were modified by
this review.
