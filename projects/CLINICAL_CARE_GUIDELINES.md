---
title: Clinical Care Guideline Collection
status: IN_PROGRESS
description: >-
  Systematically collect recent clinical Practice Guideline citations from
  PubMed for dismech disorders, generalizing the Fanconi anemia care-guideline
  mining (issue #4878). Batch 1 captures the top 40 disorders by
  recent-guideline availability; batch 2 is a 10-disorder rare-disease slice
  that mirrors the Fanconi anemia case — together a snippet-verification and
  gap-assessment worklist.
tags: [CLINICAL_GUIDELINES, EVIDENCE, PUBMED, PHENOTYPE_COVERAGE, CURATION_WORKFLOW, RARE_DISEASE]
diseases:
  - COVID-19
  - Diabetes_Mellitus
  - Obesity
  - Heart_Failure
  - Chronic_Kidney_Disease
  - Lymphoma
  - Prostate_Adenocarcinoma
  - Coronary_Artery_Disease
  - Osteoporosis
  - Asthma
  - Atrial_Fibrillation
  - Liver_Cirrhosis
  - MSI_High_Colorectal_Cancer
  - Colon_Adenocarcinoma
  - Myocardial_Infarction
  - Tuberculosis
  - Hepatocellular_Carcinoma
  - Hepatitis_B
  - Cervical_Cancer
  - Small_Cell_Lung_Cancer
  - Psoriasis
  - Infectious_Disease
  - Ulcerative_Colitis
  - Non-Small_Cell_Lung_Cancer
  - Hepatitis_C
  - Influenza
  - Osteoarthritis
  - Crohn_Disease
  - Epilepsy
  - Rheumatoid_Arthritis
  - Endometriosis
  - Chronic_Obstructive_Pulmonary_Disease
  - Obstructive_Sleep_Apnea
  - Gastroesophageal_Reflux_Disease
  - Ischemic_Stroke
  - Multiple_Myeloma
  - Renal_Cell_Carcinoma
  - Multiple_Sclerosis
  - Epidermolysis_Bullosa
  - Kawasaki_Disease
  - Dermatomyositis
  - Takayasu_Arteritis
  - Peutz_Jeghers_Syndrome
  - Pompe_Disease
  - Gaucher_Disease
  - Hemophilia_B
  - Friedreich_Ataxia
  - Phenylketonuria
---

> **Note (2026-08-28):** the `Metastatic_*` entries named in this project were folded into their histologic parent entries per design decisions §3a (Metastatic_Prostate_Cancer → Prostate_Adenocarcinoma, Metastatic_Colorectal_Cancer → Colon_Adenocarcinoma, Metastatic_HCC → Hepatocellular_Carcinoma, Metastatic_Renal_Cell_Carcinoma → Renal_Cell_Carcinoma). Historical tables below retain the old names.

# Clinical Care Guideline Collection

## Task

Issue [#4878](https://github.com/monarch-initiative/dismech/issues/4878) —
"collect clinical care guidelines" (Melissa Haendel): *"we need to prioritize
other care guidelines like we did for fanconi anemia. Lets come up with a search
and prioritization strategy, as well as assessment against existing gaps in
HPOA file / dismech content."*

The Fanconi anemia work ([`FANCONI_ANEMIA_GAP_ANALYSIS.md`](FANCONI_ANEMIA_GAP_ANALYSIS.md))
mined a single disorder's care guideline into a custom HPO profile and diffed it
against the dismech entry. This project generalizes the **discovery and
prioritization** half of that work across the whole knowledge base: find, for
each dismech disorder, the recent clinical care descriptions that could be mined
for phenotype and treatment gaps.

## What counts as a "clinical care description"

A PubMed citation whose **Publication Type is `Practice Guideline`**, published
within the **last 10 years**. The `Practice Guideline` type is a curated NLM tag
applied to society/consensus management guidelines, so it is a high-precision
proxy for care descriptions — far better than free-text searching for the word
"guideline". `Practice Guideline` is narrower than the sibling `Guideline` type;
widening the net is a documented follow-on option (see the skill).

## Search and prioritization strategy

Fully reproducible via the **`collect-care-guidelines`** Agent Skill
(`.claude/skills/collect-care-guidelines/`). Two steps:

1. **Search** — for every `kb/disorders/*.yaml`, build a clean disease term
   (the top-level MONDO mapping label when present, else the `name` field) and
   run PubMed E-utilities `esearch`:

   ```
   ("<disease>"[MeSH Terms] OR "<disease>"[Title/Abstract])
     AND "Practice Guideline"[Publication Type]
   datetype=pdat  reldate=3650
   ```

   Ranking disorders by hit count *is* the prioritization: disorders with the
   most recent practice guidelines float to the top.

2. **Fetch** — pull citation metadata (`esummary`) for the ranked disorders into
   a tab-delimited citation table.

**Reliability note (why the disease phrase is field-tagged):** an unadorned
quoted term lets PubMed's Automatic Term Mapping shatter an unmatched name into
individual all-fields words. Early testing had "Alsahan-Harris syndrome" collapse
to `Harris` + `syndrome` and falsely return 30 unrelated guidelines (pelvic
floor, kidney cancer, …). Tagging the phrase with `[MeSH Terms]`/`[Title/Abstract]`
makes an unmatched disorder correctly return **zero**. This single fix is the
difference between a trustworthy worklist and noise.

## Results — Batch 1 (top 40 by guideline count)

Searched **1,564** disorder entries. **464** returned at least one recent
practice guideline; 340 returned ≥2, 280 returned ≥3.

The full ranking is preserved in
[`CLINICAL_CARE_GUIDELINES/guideline_search_all.jsonl`](CLINICAL_CARE_GUIDELINES/guideline_search_all.jsonl)
(one JSON record per disorder: `slug`, `search_name`, `count`, `pmids`).

This first batch takes the **top 40 disorders by recent-guideline count** and
exports their citation metadata to
[`CLINICAL_CARE_GUIDELINES/guideline_citations.tsv`](CLINICAL_CARE_GUIDELINES/guideline_citations.tsv)
— **1,200 citation rows** (up to 30 most-recent PMIDs per disorder; the
`guideline_count_for_disorder` column records the true total, which exceeds the
sampled rows for high-volume conditions).

| Rank | Disorder (dismech slug) | PubMed search term | Recent guidelines |
|-----:|-------------------------|--------------------|------------------:|
| 1 | COVID-19 | COVID-19 | 616 |
| 2 | Diabetes_Mellitus | Diabetes mellitus | 463 |
| 3 | Obesity | Obesity | 356 |
| 4 | Heart_Failure | Heart Failure | 265 |
| 5 | Chronic_Kidney_Disease | Chronic Kidney Disease | 196 |
| 6 | Lymphoma | Lymphoma | 182 |
| 7 | Metastatic_Prostate_Cancer | prostate cancer | 162 |
| 8 | Coronary_Artery_Disease | Coronary Artery Disease | 152 |
| 9 | Osteoporosis | Osteoporosis | 152 |
| 10 | Asthma | Asthma | 145 |
| 11 | Atrial_Fibrillation | Atrial Fibrillation | 142 |
| 12 | Liver_Cirrhosis | Liver Cirrhosis | 139 |
| 13 | MSI_High_Colorectal_Cancer | colorectal cancer | 129 |
| 14 | Metastatic_Colorectal_Cancer | colorectal cancer | 129 |
| 15 | Myocardial_Infarction | Myocardial Infarction | 126 |
| 16 | Tuberculosis | Tuberculosis | 120 |
| 17 | Hepatocellular_Carcinoma | hepatocellular carcinoma | 111 |
| 18 | Metastatic_HCC | hepatocellular carcinoma | 111 |
| 19 | Hepatitis_B | Hepatitis B | 109 |
| 20 | Cervical_Cancer | Cervical Cancer | 106 |
| 21 | Small_Cell_Lung_Cancer | Small Cell Lung Cancer | 103 |
| 22 | Psoriasis | Psoriasis | 101 |
| 23 | Infectious_Disease | Infectious Disease | 96 |
| 24 | Ulcerative_Colitis | Ulcerative Colitis | 96 |
| 25 | Non-Small_Cell_Lung_Cancer | Non-Small Cell Lung Cancer | 93 |
| 26 | Hepatitis_C | Hepatitis C | 86 |
| 27 | Influenza | Influenza | 82 |
| 28 | Osteoarthritis | Osteoarthritis | 74 |
| 29 | Crohn_Disease | Crohn Disease | 71 |
| 30 | Epilepsy | Epilepsy | 71 |
| 31 | Rheumatoid_Arthritis | Rheumatoid Arthritis | 71 |
| 32 | Endometriosis | Endometriosis | 67 |
| 33 | Chronic_Obstructive_Pulmonary_Disease | Chronic Obstructive Pulmonary Disease | 59 |
| 34 | Obstructive_Sleep_Apnea | Obstructive Sleep Apnea | 57 |
| 35 | Gastroesophageal_Reflux_Disease | Gastroesophageal Reflux Disease | 55 |
| 36 | Ischemic_Stroke | Ischemic Stroke | 55 |
| 37 | Metastatic_Renal_Cell_Carcinoma | renal cell carcinoma | 51 |
| 38 | Multiple_Myeloma | Multiple Myeloma | 51 |
| 39 | Renal_Cell_Carcinoma | Renal Cell Carcinoma | 51 |
| 40 | Multiple_Sclerosis | Multiple Sclerosis | 50 |

## Results — Batch 2 (rare diseases, Fanconi-anemia-style)

Batch 1's count-ranking surfaces common conditions. Batch 2 deliberately
re-slices the same 1,564-disorder search to **rare diseases** — the case the FA
work actually targeted, and the richest ground for phenotype-annotation gaps.

**Rare** is defined structurally from each entry's `prevalence.prevalence_class`:
any of `RARE`, `ULTRA_RARE`, `BAND_1_9_PER_100000`, `BAND_1_9_PER_1000000`, or
`BELOW_1_IN_1000000`, with no `COMMON` / `ABOVE_1_IN_1000` / `BAND_1_5_PER_10000`
record. Of **288** rare disorders, **48** have ≥1 recent practice guideline.

This batch picks **10** rare disorders spanning distinct disease families
(blistering skin disease, vasculitis, autoimmune myopathy, hereditary
cancer/polyposis, lysosomal storage, bleeding disorder, neurodegenerative
ataxia, inborn error of metabolism), each in the FA-comparable "mineable"
range of 3–11 guidelines. Citations →
[`CLINICAL_CARE_GUIDELINES/guideline_citations_rare_batch.tsv`](CLINICAL_CARE_GUIDELINES/guideline_citations_rare_batch.tsv)
(60 rows).

| Disorder (dismech slug) | PubMed search term | Prevalence tier | Recent guidelines |
|-------------------------|--------------------|-----------------|------------------:|
| Epidermolysis_Bullosa | epidermolysis bullosa | 1-9 / 1,000,000 | 11 |
| Kawasaki_Disease | Kawasaki Disease | rare | 11 |
| Dermatomyositis | Dermatomyositis | 1-9 / 100,000 | 8 |
| Takayasu_Arteritis | Takayasu Arteritis | 1-9 / 100,000 | 7 |
| Peutz_Jeghers_Syndrome | Peutz-Jeghers syndrome | 1-9 / 1,000,000 | 5 |
| Pompe_Disease | Pompe Disease | 1-9 / 100,000 | 4 |
| Gaucher_Disease | Gaucher Disease | 1-9 / 100,000 | 4 |
| Hemophilia_B | Hemophilia B | 1-9 / 100,000 | 4 |
| Friedreich_Ataxia | Friedreich ataxia | 1-9 / 100,000 | 3 |
| Phenylketonuria | phenylketonuria | 1-9 / 100,000 | 3 |

For continuity, `Fanconi_Anemia` itself (4 guidelines, same rare tier) is *not*
re-listed here — it already has its own [gap-analysis project](FANCONI_ANEMIA_GAP_ANALYSIS.md)
and serves as the benchmark this batch is modeled on.

## Worked example — Epidermolysis Bullosa (guidelines in practice)

`Epidermolysis_Bullosa` is the first entry curated *from* this citation set,
demonstrating the end-to-end flow. Its 11 guideline hits were filtered (2 were
excluded — see below), the relevant abstracts fetched with `just fetch-reference`,
and the multidisciplinary-care gap closed with snippet-verified evidence:

- **2 new phenotypes** — Esophageal Stricture (`HP:0002043`) and
  Pseudosyndactyly / mitten deformity (`HP:0010554`), previously only mentioned
  in prose.
- **6 new treatments** spanning the DEBRA International care guidelines —
  esophageal dilatation, hand surgery + therapy, palliative/end-of-life care,
  podiatric foot care, neonatal EB care, and orthodontic/dental care.

**NEC catch in practice:** two of EB's 11 hits — the pediatric autoimmune
blistering guideline (`PMID:41678328`) and the pemphigoid/EB-acquisita guideline
(`PMID:31646663`) — describe *autoimmune* EB acquisita, a distinct entity from
this Mendelian entry, and matched only on the "epidermolysis bullosa acquisita"
string. They were excluded. This is the same named-entity-confusion risk the
project's evidence policy warns about, caught by reading the titles.

**Thin-abstract reality:** the pregnancy/childbirth guideline (`PMID:34687549`)
and the physiotherapy appraisal (`PMID:35717492`) have no quotable abstract body,
so they could not supply snippet-verified evidence and were left for a curator
with full-text access — a reminder that a guideline *hit* is not automatically a
usable *citation*.

## Known limitations (for the curator)

- **Common-disease skew.** "Search-driven, keep hits" ranking by count surfaces
  high-prevalence conditions with rich society guidelines. This is the intended
  outcome for a first batch, but the highest-value *gap-mining* targets may be
  mid-tier disorders (a few good guidelines, likely under-annotated) — the FA
  case itself was a rare disease. The full 464-disorder ranking supports
  re-slicing on that basis.
- **Subtype collapse to a broad MONDO label.** Several dismech entries share one
  umbrella search term and therefore an identical guideline set:
  `MSI_High_Colorectal_Cancer` + `Metastatic_Colorectal_Cancer` (both
  "colorectal cancer"), `Hepatocellular_Carcinoma` + `Metastatic_HCC`,
  `Renal_Cell_Carcinoma` + `Metastatic_Renal_Cell_Carcinoma`. The guidelines are
  for the parent disease, not the specific subtype. Dedupe by `search_name`
  before mining.
- **Umbrella entries.** `Lymphoma` and `Infectious_Disease` match a very broad
  MeSH term; their counts overstate *specific* care relevance.
- **Candidate list, not evidence.** Automatic Term Mapping favors recall. Every
  citation is a *lead* — spot-check that the top hits are actually about the
  intended disease.

## Second-generation search — "does the abstract state a recommendation?"

The count-ranked search above is a good *prioritization* tool but a poor
*evidence-sourcing* tool, and the reason is worth recording: it ranks by how many
Practice Guidelines exist, which reliably surfaces the **flagship umbrella
guideline** for a disease — and those abstracts are frequently scope and process
metadata (`OBJECTIVE / TARGET POPULATION / EVIDENCE / METHODS`, panel
composition, or a chapter list) with no concrete recommendation in them. An
abstract that states no specific recommendation cannot yield a snippet-verified
evidence item, however authoritative the guideline is.

**Scope — this is not about drugs.** Care guidelines cover the whole of clinical
care: pharmacotherapy is only one branch. A usable abstract is one that states a
**specific, actionable recommendation** naming an intervention of *any* modality
— drug, surgical/interventional procedure, radiotherapy, device, diet,
rehabilitation, monitoring interval — or a **diagnostic action** (screening,
imaging, biopsy, staging, testing). Scoring only drug names encodes a
pharmacology bias and wrongly discards surgical, diagnostic and supportive-care
guidance. (Worked example: a cervical-cancer screening guideline whose abstract
says *"screening assays should differentiate between HPV genotypes 16 and 18"*
is perfectly good evidence for a diagnostic recommendation and names no drug at
all.)

```bash
uv run python .claude/skills/collect-care-guidelines/scripts/therapy_specific_search.py \
    spec.json out.json     # spec = [{slug, query, terms?[]}, ...]
```

It runs `esearch`, fetches each abstract, strips the citation/author/affiliation
front matter, and ranks hits by **`recommendation_sentences`** — sentences
carrying *both* an intervention/diagnostic term *and* a recommendation cue
(`we recommend`, `should be offered`, `first-line`, …). The looser
`intervention_sentences` count is reported alongside for triage. Optional
per-disease `terms` extend the default modality vocabulary with specific drug or
procedure names. Records land in
[`CLINICAL_CARE_GUIDELINES/therapy_specific_searches.jsonl`](CLINICAL_CARE_GUIDELINES/therapy_specific_searches.jsonl).

**Query- and scoring-design lessons (each cost a round to learn):**

1. **Don't OR `guideline*[Title]` with intervention terms.** It matches *studies
   about* guidelines — "Guideline adherence to aspirin prophylaxis…", "The
   Nationwide Impact of Guidelines for Prophylactic Aspirin…" — not guidelines
   themselves. Preeclampsia returned nothing but adherence/impact studies until
   the filter was tightened.
2. **Require `"Practice Guideline"[Publication Type]`**; put intervention terms
   in the *scoring*, not the query. Terms in `[tiab]` bias toward trials of that
   intervention over guidelines about it.
3. **Require a recommendation cue, and strip the front matter** — bare term
   matching produces two classic false positives: **author affiliations**
   ("Department of Surgery, …" — the ESMO metastatic-colorectal abstract scored
   6 bogus "intervention" hits this way) and **chapter/TOC listings**
   ("1) Definition; … 5) Surgical management"), neither of which recommends
   anything.

**Recommendation-free abstracts (negative results, recorded so they are not
re-litigated).** These disorders have many guidelines, but the abstracts state
no specific recommendation of *any* modality — not drug, not procedural, not
diagnostic. They need full-text access or a different source type, and should be
*skipped* by abstract-only snippet mining:

| Disorder | Why (re-checked with the modality-agnostic scorer) |
|---|---|
| `Non-Small_Cell_Lung_Cancer` | NCCN v4.2026 has **no text abstract**; ASCO Living Guidelines are ~1.9k-char scope-only. The NCCN abstract's single intervention hit is its own scope sentence ("provide recommendations … including diagnosis"). Tried twice. |
| `Metastatic_Colorectal_Cancer` | ESMO CPG abstract is ~12k chars of author affiliations/scope; `recommendation_sentences = 0` once affiliations are stripped. |
| `Myocardial_Infarction` | ACC/AHA-adjacent, AATS, SIPREC, Latin-American ACS documents state no specific recommendation in-abstract. |
| `Endometriosis` | SOGC No. 468 and Polish SGO abstracts are `OBJECTIVE/EVIDENCE` structure only; the French consensus lists chapter headings ("5) Surgical management") rather than recommending. |
| `Pulmonary_hypertension` | `recommendation_sentences = 0` across **12 candidates over two passes** (batch 15). Scored with the modality-agnostic vocabulary, so this is not a drug-lens artifact — the abstracts state no specific recommendation of any modality, including the diagnostic ones expected here (right heart catheterization, echocardiography). **NEC caution:** acute pulmonary embolism guidelines surface under PH queries and are a different entity. |
| `Amyloidosis` | Best hit (41277424) scores `rec=1`, but the sentence is *meta* — "Four conditional recommendations and 3 good practice statements were established to provide guidance for proper testing and workup" — a **count** of recommendations, not a recommendation. See the scorer limitation below. |
| `Sickle_Cell_Disease` | `rec=0` across 6 candidates despite `iv=12` on the best hit — intervention terms present, no recommendation cue. Verified **not** a cue-list gap: abstracts grepped directly for `shall`/`must`/`advise`/`indicated`/`offer`/`screen`; no directive language present. |
| `Lynch_Syndrome` | `rec=0` across 4 candidates. A surveillance-heavy disease where a diagnostic recommendation was expected; the abstracts state none. Same direct-grep verification. |
| `Polycystic_Ovary_Syndrome` | The 2023 international guideline (37589624) scores `rec=0` despite a 15k-char abstract. The only `rec>0` hit scores on **terminology**, not care ("The term *female pattern hair loss* should be used…"). |
| `Chronic_Pancreatitis` | **NEC risk.** Scored `rec=14` — highest in the batch-16 sweep — yet unusable: the top hit's leading sentence is meta, and the runner-up recommends Ringer's lactate for **acute** pancreatitis, a different entity. Acute-pancreatitis guidance surfaces under chronic-pancreatitis queries. |

**Known scorer limitation.** A recommendation cue also matches sentences that merely *describe recommendations existing* ("N recommendations were established…", "the guideline provides recommendations for…"). These inflate `recommendation_sentences` without offering anything quotable. The score is a triage signal, not a verdict — always read the sampled sentence before committing to a source.

**Corollary — don't let the meta heuristic push you onto a secondary source.** The limitation above has a mirror-image failure, and it bit on the very next batch after it was written down. The **primary** ERS bronchiectasis guideline states its own recommendation in reporting voice — "The Task Force recommendations include strong recommendations in favour of airway clearance techniques…" — which *reads* as meta. A Chinese-language **interpretation of that same guideline** phrased it more crisply ("The guideline strongly recommends airway clearance techniques…"). Scoring on phrasing alone therefore picked the commentary over the guideline itself; review caught it (#6601).

A guideline's own `RECOMMENDATIONS:` section frequently reports in the third person — that is the primary source speaking, not a description of someone else's work. **Check journal and title for primary-vs-commentary before preferring a cleaner sentence.** A bracketed, translated title (`[Highlights and interpretation of …]`) is a strong tell that you are reading commentary.

**`rec = 0` is a prompt to read, not a verdict — the scorer produces false negatives too.** The two failures above inflate the score; this one *suppresses* it. The scorer requires **both** an intervention/diagnostic term **and** a recommendation cue, so a missing noun silently kills a real hit. `Lyme_Disease` scored `rec=0` and was nearly recorded as a dead end, yet its guideline abstract is full of usable guidance:

> "Serology is recommended only in suspected disseminated LB…"

The cue (`is recommended`) matched; **"serology" simply wasn't in the intervention vocabulary**. One missing noun, one lost guideline. The vocabulary now covers laboratory/pathology diagnostics (serology, assay, antibody, antigen, culture, histology, cytology, genotyping, sequencing) — but the vocabulary will *always* be incomplete, so treat `rec=0` on a disease whose care you'd expect to be guideline-rich as a signal to open the abstract.

**How to tell a true negative from a vocabulary gap:** grep the abstract for *cue* language alone (`recommend`, `should`, `shall`, `must`, `advise`, `indicated`, `offer`, `first-line`). If there are **no cues at all**, no vocabulary could rescue it — a true negative. If cues are present but `rec=0`, you have a vocabulary gap. The batch-16 negatives (`Sickle_Cell_Disease`, `Lynch_Syndrome`) were verified this way and hold; they contain no directive language whatsoever.

**Corollary for source selection:** prefer the *therapy-specific* guideline over
the flagship (AGA's ascites update over a general cirrhosis guideline; an
appropriate-use recommendation over a disease overview). Regional and
specialty-society guidelines (SEOM-GEICO, SEOM-GOTEL, AFU, ALEH, Brazilian
Psychiatric Association) are frequently **more** snippet-usable than the big
international ones, because their abstracts summarize recommendations rather
than describe process.

## Evidence policy

This is a **discovery** artifact. Any citation ultimately used as dismech
evidence must still pass the standard snippet-verification workflow
(`just fetch-reference PMID:…`, then `just validate-references`). Guideline
provenance alone does **not** satisfy the dismech PMID + verified-snippet policy
— the same discipline applied when the FA `.hpoa` (evidence code `TAS`) terms
were each independently re-sourced.

## Files

- [`CLINICAL_CARE_GUIDELINES/guideline_citations.tsv`](CLINICAL_CARE_GUIDELINES/guideline_citations.tsv)
  — batch 1: the top-40 citation table (one row per disorder × guideline PMID).
- [`CLINICAL_CARE_GUIDELINES/guideline_citations_rare_batch.tsv`](CLINICAL_CARE_GUIDELINES/guideline_citations_rare_batch.tsv)
  — batch 2: the 10 rare-disease citation table (same columns).
- [`CLINICAL_CARE_GUIDELINES/guideline_search_all.jsonl`](CLINICAL_CARE_GUIDELINES/guideline_search_all.jsonl)
  — the full 1,564-disorder search result / prioritization ranking.
- [`CLINICAL_CARE_GUIDELINES/therapy_specific_searches.jsonl`](CLINICAL_CARE_GUIDELINES/therapy_specific_searches.jsonl)
  — second-generation recommendation-scored searches: one record per disorder
  with the query, the chosen PMID, its recommendation-sentence count, and the
  outcome (`USED` / `REJECTED_NO_RECOMMENDATION`). Covers enrichment batches
  10–14 and records the four recommendation-free disorders so they are not
  re-searched.
- `.claude/skills/collect-care-guidelines/` — the reusable Agent Skill
  (`SKILL.md` + `scripts/collect_guidelines.py` for the count-ranked search,
  `scripts/therapy_specific_search.py` for the recommendation-scoring variant).

## Next steps

1. **Gap assessment (the second half of #4878).** For a chosen disorder, diff
   its guideline-derived phenotype/treatment content against (a) the dismech
   entry and (b) the HPOA annotation file, FA-style.
2. **Mine the rest of batch 2.** Epidermolysis_Bullosa is done (worked example
   above); Kawasaki_Disease has the most remaining guideline material, then work
   down the batch-2 table.
3. **Widen the type filter** to `Guideline` where `Practice Guideline` is sparse.
4. **Extend the rare slice.** 48 rare disorders have guidelines; batch 2 covers
   10. The rest are queued in `guideline_search_all.jsonl`.
