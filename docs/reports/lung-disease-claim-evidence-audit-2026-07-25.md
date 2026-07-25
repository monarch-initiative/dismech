# Claim–Evidence Audit: 10 Lung Disease Entries (2026-07-25)

Correctness review of ten primarily-pulmonary `kb/disorders/` entries, focused on
whether each evidence `snippet` actually supports the claim it is attached to.

## Scope

| Entry | Lines | Evidence items |
|---|---:|---:|
| `Asthma` | 2471 | 189 |
| `Chronic_Obstructive_Pulmonary_Disease` | 1252 | 111 |
| `Idiopathic_Pulmonary_Fibrosis` | 1214 | 45 |
| `Cystic_Fibrosis` | 3261 | 193 |
| `Bronchiectasis` | 630 | 20 |
| `Silicosis` | 730 | 24 |
| `Asbestosis` | 647 | 23 |
| `Hypersensitivity_Pneumonitis` | 686 | 36 |
| `Hereditary_Pulmonary_Alveolar_Proteinosis` | 828 | 55 |
| `Non-Small_Cell_Lung_Cancer` | 1037 | 118 |
| **Total** | **12,756** | **814** |

## Method

1. **Verbatim fidelity (mechanical).** Every one of the 814 snippets was checked as an
   exact (whitespace/quote-normalised, ellipsis-part-aware) substring of its
   `references_cache/` body.
2. **Label consistency (mechanical).** Scans for claims whose evidence is *entirely*
   `NO_EVIDENCE`/`REFUTE`, for `supports` values contradicted by their own
   `explanation`, for `evidence_source` mislabelling, and for quantitative claims whose
   numbers appear nowhere in the cited snippet.
3. **Semantic support (manual).** Read-through of claim ↔ snippet ↔ explanation for every
   `pathophysiology`, `genetic`, `treatment`, `phenotype`, and `prevalence` record.

## Headline result

**Verbatim snippet fidelity is clean.** All 814 snippets verify against their cached
sources. 44 initially flagged as mismatches were traced to Unicode/punctuation artifacts
in the checker, not the data — e.g. the YAML writes `>/= grade 2` where the cached
abstract holds `≥ grade 2` (PMID:30537755), and several snippets carry a trailing period
absent from the source (PMID:10907591, PMID:3595047). No fabricated quotes were found.

**The real defects are in claim–evidence *matching*, not quoting** — and they are
concentrated in three of the ten files. The entries split into two clear cohorts:

| Cohort | Entries | Character |
|---|---|---|
| **Well-curated** | `Idiopathic_Pulmonary_Fibrosis`, `Cystic_Fibrosis`, `Bronchiectasis`, `Silicosis`, `Asbestosis`, `Hypersensitivity_Pneumonitis`, `Hereditary_Pulmonary_Alveolar_Proteinosis` | 100% `evidence_source` coverage; tight claim↔snippet correspondence; deliberate use of `PARTIAL`/`REFUTE`; explanations that name the study design |
| **Legacy / needs repair** | `Asthma`, `Chronic_Obstructive_Pulmonary_Disease`, `Non-Small_Cell_Lung_Cancer` | 367/418 evidence items missing `evidence_source`; off-topic citations; circular explanations; frequency bands contradicted by their own snippets |

`evidence_source` coverage is the cleanest proxy for the split:

```
Asbestosis                                  missing    0/ 23
Bronchiectasis                              missing    0/ 20
Cystic_Fibrosis                             missing    0/193
Hereditary_Pulmonary_Alveolar_Proteinosis   missing    0/ 55
Hypersensitivity_Pneumonitis                missing    0/ 36
Idiopathic_Pulmonary_Fibrosis               missing    0/ 45
Silicosis                                   missing    0/ 24
Asthma                                      missing  148/189
Chronic_Obstructive_Pulmonary_Disease       missing  103/111
Non-Small_Cell_Lung_Cancer                  missing  116/118
```

---

## High-severity findings

### 1. COPD global prevalence is asserted with zero supporting evidence, one citation being a silicosis paper

`Chronic_Obstructive_Pulmonary_Disease.yaml:51-67`

```yaml
prevalence:
- population: Global
  measure_type: POINT_PREVALENCE
  prevalence_class: ABOVE_1_IN_1000
  rate_per_100000: 11700.0
  percentage: 11.7
  evidence:
  - reference: PMID:35261410
    supports: NO_EVIDENCE
    explanation: ...does not mention a global prevalence rate of 11.7%.
  - reference: PMID:37461046
    supports: NO_EVIDENCE
    explanation: This study focuses on ...silicosis, not COPD.
```

A structured numeric claim (`rate_per_100000: 11700.0`) with **both** evidence items
marked `NO_EVIDENCE` — the entry documents its own lack of support. One citation
(PMID:37461046, *Global incidence, prevalence and disease burden of silicosis*) is a
different disease entirely.

*Fix:* PMID:35261410 reports a pooled prevalence of **11.1%** (GOLD fixed criteria) across
**eight countries** — not global. Set `rate_per_100000: 11100.0`, change `population` to
match the study's actual scope, mark `supports: SUPPORT`, and delete the silicosis
citation. Also drop the deprecated `percentage:` field (design decision §8).

### 2. COPD respiratory-failure frequency band is contradicted by its own evidence

`Chronic_Obstructive_Pulmonary_Disease.yaml` `phenotypes[5]`

```yaml
frequency: OCCASIONAL          # HP:0040283 = 5-29% of patients
name: Respiratory Failure
evidence:
- reference: PMID:14621114
  supports: REFUTE
  explanation: ...respiratory failure is an important and common complication of COPD, not an occasional one.
- reference: PMID:38692758
  supports: REFUTE
  explanation: ...hypoventilation, which can lead to respiratory failure, is not uncommon in COPD.
```

Both evidence items refute the *frequency qualifier*, not the association. The band is
simply wrong.

*Fix:* raise to `FREQUENT` (30–79%) and re-label both items `SUPPORT`.

### 3. NSCLC `progression[0]` has no claim text and seven off-topic citations

`Non-Small_Cell_Lung_Cancer.yaml` `progression[0:Onset]` carries **no `description` or
`notes`** — there is no claim — yet seven evidence items hang off it, all `NO_EVIDENCE`.
Two are grossly off-topic:

- `PMID:38377969` — *multiple sclerosis* disease-progression modelling
- `PMID:34911717` — *early-onset colorectal cancer in Lynch syndrome*

These are citation-relevance failures, not evidence. An `NO_EVIDENCE` item whose
explanation reads "the study focuses on multiple sclerosis" carries no information and
should be deleted, not retained.

*Fix:* write an actual onset claim (the record's implied claim is age 60–80 at onset, for
which PMID:15477641 is a reasonable partial source) and delete the MS and Lynch citations.

### 4. NSCLC has a duplicated `Bone Pain` phenotype

`Non-Small_Cell_Lung_Cancer.yaml:375-378` and `:429-433` — two `phenotypes` entries with
identical `category: Musculoskeletal`, `name: Bone Pain`, `frequency: OCCASIONAL`, and
`notes: May indicate bone metastases`, sharing two of the same citations
(PMID:20536932, PMID:26690845). One is redundant.

### 5. NSCLC `ROS1` frequency band contradicts its own snippet

`genetic[2:ROS1]` is `frequency: OCCASIONAL` (HP:0040283, 5–29%), while the cited snippet
reads *"ROS-1 rearrangement is found in **0.9-2.6%** of non-small-cell lung cancers"* —
i.e. `VERY_RARE` (<5%). `ALK` at 2–7% straddles the boundary and is defensible; ROS1 is
not.

---

## Medium-severity findings

### 6. `supports` labels contradicted by their own explanation

- `Asthma` `has_subtypes[2:Adult-Onset Asthma]` / PMID:36833767 — `supports: NO_EVIDENCE`,
  but the explanation reads *"...which **supports** that adult-onset asthma could have
  environmental triggers."* One of the two is wrong.

### 7. Treatment-toxicity evidence used to support disease phenotypes (NSCLC)

- `phenotypes[4:Fatigue]` — four of five citations describe **chemotherapy toxicity**
  (PMID:38469616 cancer-related fatigue *after chemotherapy*; PMID:33755621 "adverse
  effects of treatment"; PMID:26990789 "toxicities included…"; PMID:30537755
  "non-hematological toxicities"). Only PMID:32013812 addresses fatigue as a disease
  symptom. Treatment toxicity is a distinct claim from disease phenotype — the repo has
  a `myelosuppression` module precisely for this distinction.
- `phenotypes[0:Persistent Cough]` — PMID:35224703 and PMID:37920959 both measure
  **postoperative** cough after lung-cancer surgery, not cough as a presenting feature.

### 8. Wrong-disease evidence retained as SUPPORT

- `NSCLC` `pathophysiology[5:Metastasis]` — the lead citation PMID:33533174 reports
  metastasis site patterns in **SCLC**, used to support NSCLC organotropism. The
  explanation concedes this ("*While this article primarily deals with small cell lung
  cancer…*") yet the label is `SUPPORT`.
- `Asthma` `pathophysiology[0:Airway Inflammation]` — PMID:23234454 is about **cardiac
  asthma** (a heart-failure entity, not asthma). Correctly `PARTIAL`, but it does not
  belong on an asthma airway-inflammation node.
- `COPD` `biochemical[0:Arterial Blood Gases]` — PMID:34756790 describes blood-gas
  derangement after a **detonation/nitrogen-compound inhalation injury**; the explanation
  hand-waves "including COPD contexts". Marked `SUPPORT`.

### 9. Claims whose mechanism is not in the snippet

- `COPD` `pathophysiology[4:Oxidative Stress and Mitochondrial Dysfunction]` — claim is
  *cigarette smoke triggers mitochondrial ROS, impaired mitophagy, reduced antioxidant
  defences*. The sole snippet is *"Shared benefits include mitigation of oxidative stress,
  mitochondrial dysfunction, and extracellular matrix remodeling"* — a statement about
  what **SIRT1 activation mitigates**, which does not establish the claimed trigger
  mechanism. Marked `SUPPORT`.
- `COPD` `pathophysiology[3:Alveolar Destruction]` — all four items `PARTIAL`, three
  explanations conceding non-support; PMID:24707174 is a list of eight endothelial
  microparticle surface markers, unrelated to alveolar destruction. The node also omits
  the core protease–antiprotease/elastolysis mechanism that
  `emphysema_protease_antiprotease_imbalance` already models.
- `COPD` `treatments[3:Phosphodiesterase-4 Inhibitors]` — PMID:32361678 is about **protein
  kinases**; the explanation conflates them with PDE4 inhibitors ("*specifically kinase
  inhibitors*"). Marked `SUPPORT`.
- `COPD` `environmental[1:Air Pollution]` — PMID:25673984's snippet lists
  infection/protease imbalance/oxidative stress and says nothing about pollution. Marked
  `SUPPORT`.
- `Asthma` `pathophysiology[2:Bronchoconstriction]` — PMID:27603525 (statins in **animal
  models**) supports the claim only via the non-sequitur "*the use of statins to reduce
  airway hyper-responsiveness implies the involvement of smooth muscle cells*"; also
  animal data with no `evidence_source`.
- `Silicosis` `pathophysiology[7]`, `[8]` and `phenotypes[5]` — specific claims
  (TGF-β/PDGF/TNF-α-driven myofibroblast differentiation; the concentric whorled
  hyalinised silicotic nodule; *silica impairs macrophage killing of M. tuberculosis*)
  rest on generic "…with subsequent fibrosis" / "…associated with silica dust exposure"
  snippets. The associations hold; the **mechanisms** are unsupported. `PARTIAL` would be
  more accurate than `SUPPORT`.

### 10. Quantitative descriptions outrunning their evidence (Cystic Fibrosis)

Several `Cystic_Fibrosis` nodes carry precise percentages supported only by a generic
list-of-complications snippet from PMID:30986316 (*"Other complications include sinusitis,
diabetes mellitus, bowel obstruction, hepatobiliary disease, hyponatremic dehydration, and
infertility"*):

| Node | Unsupported figure |
|---|---|
| `pathophysiology[15]` Exocrine Pancreatic Insufficiency | 85–90% |
| `pathophysiology[20]` Intestinal Obstruction | meconium ileus 15–20% |
| `pathophysiology[21]` Hepatobiliary Obstruction | cirrhosis 5–10% |
| `pathophysiology[24]` Vas Deferens Agenesis | CBAVD 97–98% |
| `pathophysiology[25]` Sinonasal Disease | nasal polyposis 10–32% |
| `treatments[11]` Lung Transplantation | 5-yr survival ~50–60% |

The *existence* of each complication is supported; the numbers are not. Per
[`docs/frequency-evidence-guidelines.md`](../frequency-evidence-guidelines.md), a
quantitative claim needs its own citation. This is the least severe class here — the
figures are all clinically conventional — but they should either get a source or move to
`notes`.

---

## Process observation: DOI references bypass CI snippet validation

`conf/reference_validator_config.yaml` lists `DOI` in `skip_prefixes`, so
`linkml-reference-validator` performs **zero** checks on DOI-referenced evidence. On
`Bronchiectasis`, whose evidence is mostly DOI-based, the validator reports:

```
Validation Summary:
  Files validated: 1
  Total checks: 0
  All validations passed!
```

"All validations passed" here means "nothing was validated". Across the ten entries this
covers **20 evidence items** (plus 1 `PPR:` preprint). All 20 have populated
`references_cache/DOI_*.md` files, and independently checking them confirms every snippet
is an exact substring — so there is **no data defect**, but the CI signal is misleading.
Since the cache exists, DOI could be removed from `skip_prefixes` and validated like PMID.

## What is exemplary

Worth preserving as curation patterns:

- **`Idiopathic_Pulmonary_Fibrosis` `mechanistic_hypotheses[1]`** — a hypothesis carrying
  six `SUPPORT` items, a `PARTIAL` that qualifies its immune-independence claim
  (PMID:34524912, cGAS-STING in senescent IPF epithelium), and a `REFUTE`
  (PMID:31922885, epithelial CCL12 deletion protects from fibrosis) that argues directly
  against the model. This is how a contested mechanism should be curated.
- **`Asbestosis` `genetic[0:GSTM1]`** — a `SUPPORT` (PMID:8000297) paired with a `REFUTE`
  (PMID:17563610) from a larger nested case-control study, with the description honestly
  stating "*Its role in asbestosis susceptibility remains unsettled*".
- **`Silicosis`** — explanations that name the study design and justify the label
  ("*Evidence source OTHER (review)*", "*marked PARTIAL*"), so a reviewer can audit the
  reasoning without re-reading the source.
- **`Hereditary_Pulmonary_Alveolar_Proteinosis`** — disciplined ORPHA row quoting, with
  every phenotype frequency traceable to a specific Orphanet HPO row.
- The newer `Asthma` nodes (SIRT1/NAD+, early-life rhinovirus–CDHR3, HDM Der p 1
  protease–ROS signalling) are as tight as anything in the well-curated cohort — the
  file's weakness is entirely in its legacy nodes.

## Suggested remediation order

1. COPD `prevalence[0]` — replace the unsupported 11.7% and delete the silicosis citation
2. COPD `phenotypes[5]` — fix the respiratory-failure frequency band
3. NSCLC `progression[0]` — write the claim; delete the MS and Lynch citations
4. NSCLC — de-duplicate `Bone Pain`; fix the `ROS1` frequency band
5. NSCLC / Asthma / COPD — backfill `evidence_source` (367 items)
6. Re-label the `SUPPORT` items in findings 8–9 as `PARTIAL`, or replace the citation
7. Cystic Fibrosis — source or demote the six quantitative descriptions
8. Consider removing `DOI` from `skip_prefixes` so DOI evidence is CI-validated
