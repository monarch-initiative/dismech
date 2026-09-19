# Claim–Evidence Review: 10 Lung Disease Entries (2026-07-25)

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
4. **Full-text re-adjudication.** Every flagged item whose reference has (or could be
   fetched to have) a full-text cache was re-checked against the *whole paper*, not just
   the abstract — because a claim unsupported by the quoted sentence may still be
   supported elsewhere in the source. That distinction separates a **bad citation** from
   an **under-selected snippet**, which need opposite fixes. Searches de-hyphenate
   OCR line-breaks (`paren-\nchyma` → `parenchyma`) before matching.

## Headline result

**Verbatim snippet fidelity is clean.** All 814 snippets verify against their cached
sources. 44 initially flagged as mismatches were traced to Unicode/punctuation artifacts
in the checker, not the data — e.g. the YAML writes `>/= grade 2` where the cached
abstract holds `≥ grade 2` (PMID:30537755), and several snippets carry a trailing period
absent from the source (PMID:10907591, PMID:3595047). No fabricated quotes were found.

**The real defects are in claim–evidence *matching*, not quoting** — and they are
concentrated in three of the ten files. A full-text pass (see below) then split those
matching defects in two: some citations are genuinely wrong, while others are correct
citations with a badly chosen quote. One further defect sits below the entries entirely —
a cache file holding the wrong paper's full text (Finding 4b).

The entries split into two clear cohorts:

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

**Full-text coverage.** 46 of the 456 unique references cited by these entries have
full-text caches (40 already committed; 6 more fetched during this audit). Those back
**97 of the 814 evidence items**. Re-fetching every abstract-only reference relevant to a
finding yielded full text for 6 — the rest are genuinely abstract-only, so those findings
could not be re-adjudicated and stand as written.

---

## Meta-finding: abstract-only quoting systematically understates support

Twelve weak-labelled (`PARTIAL`/`NO_EVIDENCE`/`REFUTE`) items are backed by full text.
Checking them against the whole paper **rescues four outright** — the citation is correct
and the paper does support the claim; the curator simply quoted a weak sentence from the
abstract when an on-point sentence exists in the body.

This reframes part of the audit. Several `PARTIAL` labels in the legacy cohort are not
evidence weaknesses at all — they are artifacts of abstract-only curation, and the fix is
to **re-quote**, not to weaken the label or drop the citation.

| Item | Quoted (abstract) | Available in full text |
|---|---|---|
| COPD `pathophysiology[3]` Alveolar Destruction / PMID:11993785 | "*In the lung parenchyma, emphysema defined as alveolar destruction and airspace enlargement is present*" (`PARTIAL`) | "*The mechanism responsible for the development of emphysematous lesions is thought to be an imbalance in **protease and antiprotease** enzymes in the lung*" and "*the **loss of elastic recoil** induced by the emphysematous lungs…*" |
| COPD `pathophysiology[1]` Chronic Inflammation / PMID:11993785 | `PARTIAL`, explanation: "*…not specifically detailing the involvement of neutrophils, macrophages and…*" | "*predominant inflammatory cellular infiltrations … identified as activated **CD8+ T-lymphocytes and macrophages** … A number of **neutrophils** have been found in the bronchial lumen*" |
| COPD `environmental[1]` Air Pollution / PMID:25673984 | "*The major pathogenic factors … infection and inflammation, protease and antiprotease imbalance, and oxidative stress*" — says nothing about pollution | "*Such exposures can include environmental tobacco smoke, burning of biomass, and **air pollution particles**. All these particle exposures … can result in oxidative stress*" |
| COPD `pathophysiology[3]` Alveolar Destruction / PMID:32493486 | a surfactant-homeostasis sentence (`PARTIAL`) | "*The pathophysiology of chronic obstructive pulmonary disease (COPD), which involves **emphysematous destruction of alveolar sacs** and airway remodeling…*" |

Notably, the protease–antiprotease mechanism I first recorded as *missing* from the COPD
Alveolar Destruction node is present in a paper the node **already cites** — and it is the
mechanism modelled by `emphysema_protease_antiprotease_imbalance`, so re-quoting also
opens a natural `conforms_to` edge.

---

## Full text confirms (and strengthens) the bad-citation findings

Where full text was available for a citation I judged off-topic, it removed all doubt:

| Citation | Full-text verdict |
|---|---|
| PMID:37461046 in COPD `prevalence[0]` (Finding 1) | The **only** occurrence of "COPD" in the entire paper is inside a *bibliography entry title* in the reference list. Zero COPD content in the body. |
| PMID:33533174 in NSCLC `pathophysiology[5]` Metastasis (Finding 8) | Exclusively SCLC. Its three NSCLC mentions are explicitly **contrastive** — "*Unlike non-SCLC (NSCLC), which has an intrinsic tendency for CHT resistance, SCLC is tantalizingly chemosensitive*". The paper draws the very distinction the citation elides. |
| PMID:32361678 in COPD `treatments[3]` PDE4 Inhibitors (Finding 9) | **Zero** occurrences of "PDE4" or "phosphodiesterase" anywhere in the full text. The explanation's conflation of PDE4 inhibitors with kinase inhibitors is a genuine error. |
| PMID:22550239 in NSCLC `pathophysiology[2]` Angiogenesis | **Zero** occurrences of angiogenesis / angiogenic / VEGF / neovascular. Confirms the existing `NO_EVIDENCE`; the citation should be deleted, not retained. |
| PMID:20536932 in NSCLC `phenotypes[6]` Chest Pain | **Zero** occurrences of "chest pain". Confirms `NO_EVIDENCE`; delete. |
| PMID:29433833 in COPD `pathophysiology[3]` Alveolar Destruction | About macrophage phagocytosis/efferocytosis; no emphysema or alveolar-destruction content. The existing `PARTIAL` and its candid explanation are **correct as written**. |

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

### 3. NSCLC `progression[0]` has a structured-only claim and seven off-topic citations

`Non-Small_Cell_Lung_Cancer.yaml` `progression[0:Onset]` states its claim only as
structured fields — `phase: Onset` with `age_range: 60-80` — with **no prose
`description` or `notes`** to say what the evidence is meant to support. Seven evidence
items hang off it, all `NO_EVIDENCE`. Two are grossly off-topic:

- `PMID:38377969` — *multiple sclerosis* disease-progression modelling
- `PMID:34911717` — *early-onset colorectal cancer in Lynch syndrome*

These are citation-relevance failures, not evidence. An `NO_EVIDENCE` item whose
explanation reads "the study focuses on multiple sclerosis" carries no information and
should be deleted, not retained.

*Fix:* add a prose claim matching the structured `age_range` (PMID:15477641 — "*over 50%
of all patients with non-small cell lung cancer (NSCLC) are 65 years of age or older*" —
is a reasonable partial source, and would be `PARTIAL` rather than `NO_EVIDENCE` against a
stated claim), and delete the MS and Lynch citations.

### 4. NSCLC has a duplicated `Bone Pain` phenotype

`Non-Small_Cell_Lung_Cancer.yaml:375-378` and `:429-433` — two `phenotypes` entries with
identical `category: Musculoskeletal`, `name: Bone Pain`, `frequency: OCCASIONAL`, and
`notes: May indicate bone metastases`, sharing two of the same citations
(PMID:20536932, PMID:26690845). One is redundant.

### 4b. Full-text cache contamination: PMID:31922885 holds a *different paper entirely*

`references_cache/PMID_31922885.md` — cited by `Idiopathic_Pulmonary_Fibrosis`
`mechanistic_hypotheses[1]` as the `REFUTE` evidence — has a body containing
**French-language human–computer-interaction ergonomics text**:

```
full_text_provider: openalex
full_text_url: "https://inria.hal.science/inria-00075378"
```

```
Les ergonomes réalisent en général des évaluations d'interfaces homme-machine (IHM)
dans 4 contextes principaux… Ce texte propose une revue critique des pratiques
actuelles de l'évaluation d'interface.
```

The real paper is *"Diverse Injury Pathways Induce Alveolar Epithelial Cell CCL2/12,
Which Promotes Lung Fibrosis"* (Am J Respir Cell Mol Biol, 2020). OpenAlex resolved its
full text to an unrelated INRIA HAL technical report and the fetcher ingested it, while
`content_type` still advertises full text.

**This is pre-existing in the committed cache** (introduced by commit `94e6b830`), not by
this audit. Severity:

- The currently quoted snippet is drawn from the *PubMed abstract* portion of the file,
  which is intact — so **the IPF evidence item itself is presently valid**, and the
  `REFUTE` judgement is correct.
- But anything quoted from that body would be from an unrelated document **and would still
  pass `validate-references`**, because the validator only checks substring membership in
  the cache. The anti-hallucination guarantee silently does not hold for this file.

Scope: 1 of the 46 full-text caches used by these ten entries (~2%). The other three
institutional-repository resolutions (`inserm.hal.science` → PMID:38847551,
`research.rug.nl` → PMID:34524912, `researchportal.bath.ac.uk` → PMID:33197388) were
spot-checked and are correct, so this is not a blanket problem with the OpenAlex path —
but it is undetectable by current QC.

**It is not an isolated file.** A corpus-wide sweep (title-word overlap: what fraction of
a record's own `title:` words appear anywhere in its fetched body) surfaces four more
caches at 0% overlap, of which a spot-check confirms at least one is the identical failure
mode:

```
DOI_10.1186_s12890-024-03371-5.md
  title:         Evolution of treatment strategies for solid tumors with RET
                 rearrangement … Non-small Cell Lung Cancer (NSCLC)
  full_text_url: https://purehost.bath.ac.uk/…/2014_02_07_Apereo_Europe_2014.pdf
  body:          "Cope, J 2014, 'Training researchers with Sakai',
                  Esup Day 17 & Apereo Europe 2014, Paris…"
```

Also flagged at 0%: `DOI_10.1038_ejhg.2014.61.md`, `DOI_10.1055_s-0045-1806986.md`,
`DOI_10.11588_heidok.00035789.md`. (Four `url_…accessdata.fda.gov…` hits are false
positives — their `title` *is* a URL, so title-overlap is meaningless for them.)

*Suggested fix:* re-fetch the affected files, and add a cheap cross-check to
`check-reference-cache-frontmatter`. **Caveat on the detector:** title-word overlap did
*not* catch PMID:31922885, because these caches concatenate a correct PubMed abstract with
the wrong full-text body — the title words are present in the abstract half. A robust check
needs to score the *fetched body* separately from the abstract, or add a language-ID
signal. Both the finding and this blind spot are worth their own issue.

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
  cancer…*") yet the label is `SUPPORT`. **Full text confirms** the paper is entirely
  SCLC and mentions NSCLC only to contrast the two — see the full-text table above.
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
- `COPD` `pathophysiology[3:Alveolar Destruction]` — all four items `PARTIAL`.
  **Partly resolved by full text:** PMID:11993785 and PMID:32493486 both support the claim
  in their bodies (see the rescue table), and PMID:11993785 supplies the
  protease–antiprotease/elastic-recoil mechanism I first recorded as missing. What
  *remains* a defect: PMID:24707174 (a list of eight endothelial microparticle surface
  markers, abstract-only, unrelated to alveolar destruction) and PMID:29433833
  (efferocytosis, full text confirms no alveolar-destruction content).
- `COPD` `treatments[3:Phosphodiesterase-4 Inhibitors]` — PMID:32361678 is about **protein
  kinases**; the explanation conflates them with PDE4 inhibitors ("*specifically kinase
  inhibitors*"). Marked `SUPPORT`. **Full text confirms zero mentions of PDE4 or
  phosphodiesterase** — the citation is simply wrong for this node.
- ~~`COPD` `environmental[1:Air Pollution]` — PMID:25673984~~ — **withdrawn on full-text
  review.** The paper does support the claim ("*…burning of biomass, and air pollution
  particles. All these particle exposures … can result in oxidative stress*"); only the
  quoted sentence was wrong. Re-quote rather than re-label.
- `Asthma` `pathophysiology[2:Bronchoconstriction]` — PMID:27603525 (statins in **animal
  models**) supports the claim only via the non-sequitur "*the use of statins to reduce
  airway hyper-responsiveness implies the involvement of smooth muscle cells*"; also
  animal data with no `evidence_source`.
- `Silicosis` `pathophysiology[7]`, `[8]` and `phenotypes[5]` *(abstract-only sources; not
  re-adjudicable — refetch yielded no full text)* — specific claims
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

## Process observation: DOI references are skipped by the reference validator

`conf/reference_validator_config.yaml:33` lists `DOI` in `skip_prefixes`, so
`linkml-reference-validator` does not snippet-check DOI-referenced evidence. On
`Bronchiectasis`, whose evidence is mostly DOI-based, the wrapper reports:

```
Validation Summary:
  Files validated: 1
  Total checks: 0
  All validations passed!
  Snippets checked: 5/20 verified against cached references (15 skipped by prefix)
```

Read the **last** line, not the `Total checks: 0`. Per CLAUDE.md and issue #7252,
`Total checks` counts *issues found*, so it is 0 on any clean run; the affirmative signal
is the `Snippets checked: N/N` line that `scripts/run_reference_validator.sh` appends.
Here it says plainly what happened: **5 of 20 items were verified and 15 were skipped by
prefix.**

So the gap is real but narrower than "nothing was validated": across the ten entries,
**20 DOI-referenced items** (plus 1 `PPR:` preprint) are exempt from snippet checking.
All 20 have populated `references_cache/DOI_*.md` files, and independently checking them
confirms every snippet is an exact substring — so there is **no data defect**. Since the
caches exist, `DOI` could be removed from `skip_prefixes` and validated like `PMID`.

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

1. Re-fetch `references_cache/PMID_31922885.md` (contaminated body) and sweep the corpus
   for the same OpenAlex mis-resolution — this is the only finding that breaks a
   *guarantee* rather than a single entry
2. COPD `prevalence[0]` — replace the unsupported 11.7% and delete the silicosis citation
3. COPD `phenotypes[5]` — fix the respiratory-failure frequency band
4. NSCLC `progression[0]` — write the claim; delete the MS and Lynch citations
5. NSCLC — de-duplicate `Bone Pain`; fix the `ROS1` frequency band; delete the
   full-text-refuted PMID:22550239 (angiogenesis) and PMID:20536932 (chest pain) citations
6. **Re-quote, don't re-label** — the four rescued items above (COPD alveolar destruction
   ×2, chronic inflammation, air pollution): swap the abstract sentence for the on-point
   full-text sentence and raise `PARTIAL` → `SUPPORT`. While re-quoting alveolar
   destruction, consider a `conforms_to: emphysema_protease_antiprotease_imbalance#…` edge.

   > ⚠️ **Hyphen-wrap hazard when quoting PDF-derived caches.** The validator normalises
   > runs of whitespace, so an ordinary line wrap inside a snippet is safe — but
   > PDF-extracted bodies are *hyphen-split* at line ends (`paren-\nchyma`,
   > `air-\nways`), and those hyphens are real characters in the cache. A snippet
   > spanning one **will fail** `validate-references`. `PMID_32493486.md` has ~280 such
   > lines, `PMID_11993785.md` ~77, `PMID_37461046.md` ~10. Either choose a quote that
   > sits within one line, or verify with `just validate-references <file>` before
   > committing. (This report's own Method §4 de-hyphenates before matching, which is why
   > it could find these sentences in the first place — curators quoting them do not get
   > that for free.)

   > ⚠️ **`validate-references` rewrites the whole cache as a side effect — stage only
   > your YAML.** `just validate-references <file>` runs `just fix-references-cache`
   > first (`project.justfile:734`), and that recipe globs the *entire*
   > `references_cache/` directory (`project.justfile:815`), re-quoting frontmatter
   > wherever it is unquoted:
   >
   > ```diff
   > -reference_id: DOI:10.1001/jama.2008.598
   > +reference_id: "DOI:10.1001/jama.2008.598"
   > ```
   >
   > Validating a single file can therefore leave *thousands* of unrelated cache files
   > modified — observed runs during this review and its code review ranged from ~3,000 to
   > ~7,800, the count depending on how much of the cache was already quoted when the
   > recipe ran. Pairing that with `git add -A` would commit all of them, which is exactly
   > what CLAUDE.md's targeted-`git add` rule exists to prevent.
   >
   > Recovery, **in this order**: stage your edited YAML (and only the caches you
   > deliberately re-fetched) *first*, then `git checkout -- references_cache/` to discard
   > the rest. The order is load-bearing — `git checkout -- <path>` restores from the
   > index, not `HEAD`, so staging first is what protects your deliberate re-fetches.
7. Replace the genuinely wrong citations in findings 8–9 (PMID:33533174, PMID:32361678,
   PMID:24707174)
8. NSCLC / Asthma / COPD — backfill `evidence_source` (367 items)
9. Cystic Fibrosis — source or demote the six quantitative descriptions
10. Consider removing `DOI` from `skip_prefixes` so DOI evidence is CI-validated

**Process implication.** Four of twelve full-text-backed weak labels were curation
artifacts rather than evidence problems. Where a full-text cache exists, curators should
quote from the body, not the abstract — and a `PARTIAL` whose explanation reads "*the
abstract does not mention X*" is a prompt to check the full text before accepting the
label.
