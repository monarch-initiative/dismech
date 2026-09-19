# Claim–Evidence Review: 10 Cardiac Disorder Entries (2026-07-25)

Correctness review of ten cardiac entries in `kb/disorders/`, focused on whether each
cited reference actually supports the claim it is attached to.

> **Status: remediation applied.** Findings 1–7 have been fixed in the KB; see
> [Remediation applied](#remediation-applied) at the end of this report for exactly what
> changed and what deliberately remains open.

## Scope and method

Entries reviewed:
`Brugada_Syndrome`, `Long_QT_Syndrome`, `Hypertrophic_Cardiomyopathy`,
`Dilated_Cardiomyopathy`, `Arrhythmogenic_Right_Ventricular_Cardiomyopathy`,
`Atrial_Fibrillation`, `Heart_Failure`, `Myocardial_Infarction`,
`Coronary_Artery_Disease`, `Peripartum_Cardiomyopathy`.

Three passes:

1. **Mechanical (snippet fidelity).** Every one of the **490 evidence items** was
   checked offline against its `references_cache/` file. Result: **no fabricated or
   misquoted snippets.** Twelve initial mismatches all resolved to transliteration or
   formatting artifacts, not curation errors — Greek letters written out (`β-blockers`
   → `beta-blockers`), `±` → `+/-`, smart-vs-straight quotes around `"strain"`, a
   trailing period on a truncated quote, and one line-wrap artifact in the cache
   (`definitive ( MYBPC3`). The anti-hallucination layer is doing its job.
2. **`evidence_source` audit.** Cross-checked each item tagged (or defaulting to)
   `HUMAN_CLINICAL` against what the cached paper actually reports.
3. **Semantic (claim ↔ evidence).** Read every claim with its snippets and
   explanations, asking whether the quote is *probative* for the specific assertion.

Pass 1 is clean. **All substantive findings come from passes 2 and 3.**

## Headline: the ten entries fall into two sharply different tiers

| Entry | Evidence items | `evidence_source` unset | `NO_EVIDENCE` | `PARTIAL` |
|---|---|---|---|---|
| Brugada_Syndrome | 30 | 0 | 0 | 0 |
| Long_QT_Syndrome | 79 | 0 | 0 | 0 |
| Myocardial_Infarction | 24 | 0 | 0 | 0 |
| ARVC | 79 | 0 | 0 | 3 |
| Peripartum_Cardiomyopathy | 24 | 1 | 0 | 0 |
| Dilated_Cardiomyopathy | 82 | 15 | 0 | 0 |
| Coronary_Artery_Disease | 16 | 13 | 2 | 8 |
| Atrial_Fibrillation | 23 | 14 | 1 | 3 |
| Heart_Failure | 18 | 15 | 2 | 7 |
| Hypertrophic_Cardiomyopathy | 115 | 82 | 0 | 9 |

**Tier A — Brugada, Long QT, MI, ARVC, Peripartum CM.** These are model entries. Tight
claim–evidence coupling, honest hedging, correct source typing. Highlights:

- **Peripartum_Cardiomyopathy** splits a single paper (PMID:17289576) into two evidence
  items — `MODEL_ORGANISM` for the STAT3-knockout mouse result and `HUMAN_CLINICAL` for
  the patient serum result — exactly the discipline `CLAUDE.md` prescribes for
  mixed-source papers.
- **ARVC** marks the Wnt/plakoglobin branch as provisional because its support is
  experimental, and flags the T-wave-inversion edge `PARTIAL` because the mechanistic
  bridge is genuinely unresolved.
- **Myocardial_Infarction** — every snippet is directly probative of its node. No filler.
- **Brugada** correctly types a bioinformatic hotspot study as `COMPUTATIONAL` and a
  patch-clamp study as `IN_VITRO`.

**Tier B — HCM, DCM, Atrial Fibrillation, Heart Failure, CAD.** These carry real
claim–evidence defects, described below. The pattern suggests an older, more automated
curation pass that was never revisited.

---

## Finding 1 — `NO_EVIDENCE` items whose `explanation` argues the opposite

The most serious recurring defect. An evidence item is flagged `supports: NO_EVIDENCE`
— correctly, because the snippet is non-probative — but the `explanation` then asserts
the claim as established fact. A reader (or downstream export) sees a confident
justification attached to a citation that does not support it.

| Location | Reference | Snippet is about… | Explanation asserts… |
|---|---|---|---|
| `Coronary_Artery_Disease.genetic[0]` (APOE) | PMID:40594772 | a *methods* sentence: "GWAS-significant CVD risk genes were used to calculate risk gene scores" | "GWAS studies have identified APOE as a significant cardiovascular disease risk gene" |
| `Coronary_Artery_Disease.genetic[1]` (LDLR) | PMID:40594772 | same methods sentence | "LDLR is a well-established cardiovascular disease risk gene identified through GWAS" |
| `Atrial_Fibrillation.pathophysiology[3]` (Atrial Thrombus Formation) | PMID:38255832 | "AF is an arrhythmia that affects the left atrium, cardiac function, and the patients' survival rate" | "AF affects cardiac function including atrial contraction, which contributes to thromboembolism risk" |
| `Heart_Failure.pathophysiology[1]` (Neurohormonal Activation) | PMID:33432192 | difficulty of *modelling HFpEF in animals* | "highlights the complexity of neurohormonal effects extending beyond the heart" |
| `Heart_Failure.pathophysiology[3]` (Fluid Retention) | PMID:36769308 | need for new treatments and biomarkers | "supporting the mechanism of fluid retention through impaired kidney function" |

Neither APOE nor LDLR is named anywhere in the quoted text. Both gene–disease
relationships are trivially citable; the same entry could use the ClinGen
(`CGGV:`) pattern already used successfully in HCM and DCM.

## Finding 2 — non-probative citations marked `SUPPORT`

Cases where the `explanation` itself concedes the quote does not establish the claim,
yet `supports: SUPPORT` is retained.

- **`Hypertrophic_Cardiomyopathy.treatments[1]` (Calcium Channel Blockers), PMID:3515244.**
  Snippet is about CCBs for **angina**. Explanation: *"Even though the focus is on
  angina, the acknowledged use of calcium channel blockers reinforces their role in
  cardiovascular conditions including HCM."* That is a non-sequitur. Note the adjacent
  item (PMID:36044874, hypertensive LVH) *was* correctly downgraded to `PARTIAL` with an
  honest rationale — so the curator knew the pattern and missed this one.
- **`Hypertrophic_Cardiomyopathy.treatments[2]` (Septal Myectomy), PMID:22687587.**
  Explanation: *"this reference does not directly state septal myectomy… Therefore, it
  indirectly supports the use."*
- **`Hypertrophic_Cardiomyopathy.phenotypes[3]` (Arrhythmias), PMID:34969871.** Snippet is
  a prevalence trend ("Between 2010 and 2018, prevalence increased for ARVC by 180% and
  HCM by 9%") used to support arrhythmia as an HCM phenotype. The same PMID is used
  appropriately in `prevalence[0]`.
- **`Hypertrophic_Cardiomyopathy.phenotypes[4]` (Arrhythmias), PMID:29203161.** A generic
  textbook definition of cardiac arrhythmia that never mentions HCM; the explanation
  supplies "including hypertrophic cardiomyopathy."
- **`Heart_Failure.treatments[3]` (SGLT2 Inhibitors), PMID:41110921.** Claim: *"Reduce
  hospitalizations and mortality across HF spectrum."* Snippet: *"Recommendations are
  complemented by practical tips to guide the initiation, titration, and maintenance of
  these foundational treatments."* The quote names neither SGLT2 inhibitors nor any
  outcome. One of the most citable results in cardiology (DAPA-HF, EMPEROR) is
  effectively uncited.
- **`Dilated_Cardiomyopathy.phenotypes[2]` (LV systolic dysfunction), PMID:39298146.**
  Snippet: *"Left ventricular ejection fraction (LVEF) (per 1%) was **not** associated
  with all-cause mortality."* This is a null prognostic finding cited to support a
  near-defining DCM phenotype; the explanation concedes it "shows it is less prognostic
  than fibrosis markers."
- **`Dilated_Cardiomyopathy.phenotypes[0]`** — phenotype named identically to the disease
  ("Dilated cardiomyopathy"), supported by *"Accurate risk stratification of NIDCM
  remains challenging."*

## Finding 3 — semantic conflation: same word, different claim

- **`Hypertrophic_Cardiomyopathy.biochemical[0]` (Troponin), PMID:15631686.** The claim is
  troponin as a **circulating biomarker of myocardial injury**. The snippet is about
  **mutations in troponin genes** causing cardiomyopathy. Two unrelated senses of
  "troponin"; the explanation bridges them by inference ("leading to myocardial damage
  where elevated troponin can be expected").
- **`Coronary_Artery_Disease.biochemical[0]` (LDL) and `[2]` (C-Reactive Protein).** Both
  cite the *same* snippet from PMID:39518492 — "inflammation, lipid accumulation, and
  smooth muscle cell proliferation" — which names neither LDL nor CRP.

## Finding 4 — mechanism inferred backwards from treatment response

`Dilated_Cardiomyopathy.pathophysiology[1]` (Neurohormonal Activation) is supported
entirely by two snippets about *therapy* (RAS inhibitors and beta-blockers improve
prognosis), with the explanation reasoning "…validating neurohormonal activation as a
key pathophysiological mechanism." Drug efficacy is weak evidence for mechanism, and
direct evidence for neurohormonal activation in HF/DCM is abundant. (By contrast,
`Heart_Failure.pathophysiology[1]` cites PMID:37895150 directly measuring SNS/RAAS/AVP
activation — the right pattern.)

## Finding 5 — `evidence_source` mis-typing (animal/in-vitro tagged as human)

Per `CLAUDE.md`, unset `evidence_source` defaults to `HUMAN_CLINICAL`. HCM has **82 of
115** items unset and DCM **15 of 82**, and several of those papers are explicitly not
human clinical:

| Location | Reference | What the paper actually is |
|---|---|---|
| `HCM.pathophysiology[2].evidence[0]` | PMID:1414892 | spontaneously hypertensive **rats**; also a hypertensive-LVH paper, not HCM |
| `HCM.pathophysiology[2].evidence[2]` | PMID:29522370 | **mouse** pressure-overload SPARC/macrophage study |
| `HCM.pathophysiology[0].evidence[1]`, `genetic[0].evidence[3]` | PMID:36797478 | base editing in **humanized mice** + iPSC-CMs |
| `HCM.treatments[0].evidence[2]` | PMID:37850394 | R-carvedilol in **Myh6R403Q mice** + iPSC-CMs |
| `Heart_Failure.pathophysiology[2]`, `phenotypes[5]` | PMID:38636927 | **isoproterenol-induced animal model** (Lilrb4a) |
| `Atrial_Fibrillation.pathophysiology[0]`, `environmental[1]` | PMID:39146015 | **DIO mice** + hiPSC-aCMs + human tissue (mixed — should be split) |
| `Coronary_Artery_Disease` (5 separate items) | PMID:40594772 | scRNA-seq of **mouse carotid** arteries + human carotid plaques (mixed) |

Two consequences worth calling out:

- `Heart_Failure.phenotypes[5]` (**Cardiomegaly**) is supported *solely* by the mouse
  isoproterenol snippet. `CLAUDE.md` states model-organism evidence should not be the
  only support for a human phenotype.
- `Dilated_Cardiomyopathy.pathophysiology[6]` (**Mitochondrial Dysfunction**) is
  supported solely by PMID:35418250, a **doxorubicin** cardiotoxicity mouse study — a
  distinct etiology — correctly tagged `MODEL_ORGANISM` but still the only support.

HCM demonstrates the inconsistency is local, not conceptual: PMID:25573453 (feline HCM)
*is* correctly tagged `MODEL_ORGANISM` while the neighbouring rodent papers are not.

## Finding 6 — claims that outrun their evidence

- **`Dilated_Cardiomyopathy.pathophysiology[4]` (Immune and Inflammatory Activation).**
  Claim asserts "viral myocarditis or autoimmune reactions can trigger or accelerate
  DCM"; the sole evidence is a `COMPUTATIONAL` immune-cell deconvolution study that
  addresses neither viral myocarditis nor autoimmunity.
- **`Dilated_Cardiomyopathy.pathophysiology[3]` (RNA Splicing Dysregulation).** Detailed
  claim about RBM20 splicing of TTN/CAMK2D/CACNA1C and toxic biomolecular condensates;
  the sole snippet only states RBM20 variants are linked to aggressive DCM. The entire
  mechanistic content is uncited.
- **`Atrial_Fibrillation.pathophysiology[0]` (Atrial Electrical Remodeling).** Description
  asserts the classic rate-dependent "AF begets AF" mechanism (shortened refractory
  period, loss of rate adaptation); the evidence is about *obesity/NOX2-mediated*
  remodeling. The canonical claim is uncited.
- **`Heart_Failure.pathophysiology[0]`** covers systolic *and* diastolic dysfunction, but
  both evidence items are HFpEF/diastolic — the systolic half is unsupported.
- **`Heart_Failure.phenotypes[0]` (Dyspnea)** gives a detailed mechanism (elevated left
  atrial and pulmonary venous pressure driving fluid into the interstitium) but cites an
  HFpEF fibrosis/exercise-tolerance snippet that never mentions dyspnea. Same shape for
  `phenotypes[1]` (Peripheral Edema), cited to a generic cardiorenal sentence.

## Finding 7 — structural and scope defects

- **Duplicate phenotype node.** `Hypertrophic_Cardiomyopathy.phenotypes[3]` and
  `phenotypes[4]` are both `Arrhythmias` / `Cardiovascular` / `HP:0011675` / `FREQUENT`.
  These should be merged.
- **`HCM.environmental[0]` is self-refuting.** The node is named `None Applicable` and
  carries a single `supports: REFUTE` item whose explanation states *"The statement that
  hypertrophic cardiomyopathy is not influenced by environmental factors is incorrect."*
  The KB is retaining a claim it knows to be false rather than curating the real
  environmental factors (strenuous exertion, heat) that the cited paper describes.
- **CAD MONDO mapping is too broad.** `Coronary_Artery_Disease.disease_term` is bound to
  `MONDO:1060134` *atherosclerotic cardiovascular disease* ("Any cardiovascular disease
  resulting from atherosclerosis" — includes stroke and PAD). The entry's own
  description defines CAD as coronary narrowing, so a coronary-specific class is needed.
  *(Resolved independently on `main` in #7187, which bound it to `MONDO:0021661`
  coronary atherosclerosis — a child of `MONDO:0005010` coronary artery disorder and a
  close match to this entry's atherosclerosis-centred description.)*
- **Carotid evidence used for coronary claims.** CAD's two main pathophysiology sources
  (PMID:38639096, PMID:40594772) are carotid-plaque studies applied to coronary disease
  without qualification. Defensible for general atherogenesis, but it should be stated.
- **Single-source overload.** PMID:40594772 carries 5 separate CAD claims; PMID:38255832
  carries 3 AF claims from near-identical generic sentences.
- **Curation process notes leaking into `explanation`.**
  `Dilated_Cardiomyopathy.pathophysiology[0].evidence[3]` ends with *"From the Stanford
  iPSC-cardiomyocyte 'clinical-trials-in-a-dish' program (Joseph Wu group) presented at
  the NAMeRS 2026 symposium (issue #4873)."* Provenance belongs in `notes` or a history
  record, not in a scientific justification field.
- **HCM `datasets` section is dominated by spaceflight data** — 7 NASA/GeneLab entries
  (ISS heart-on-a-chip, hiPSC-CMs in microgravity, mouse hearts on ISS, the NASA Twins
  Study). Relevance to HCM is *asserted* in the descriptions rather than demonstrated;
  the Twins Study item justifies itself via carotid intima-media thickness as "context
  for understanding how spaceflight stress may interact with HCM susceptibility." This
  reads as a bulk import into a disease entry where it does not belong.
- **Deprecated `percentage` field** still populated in `HCM.prevalence[0]`
  (`percentage: 0.2`) alongside the structured `rate_per_100000`.

## Finding 8 — large unevidenced sections in the four common-cardiology entries

Blocks carrying **zero** evidence items:

| Entry | Section | Unevidenced |
|---|---|---|
| Heart_Failure | treatments | 7/8 — ACE-I/ARB, beta blockers, ARNI, MRA, diuretics, CRT, ICD |
| Heart_Failure | genetic | 3/3 — TTN, MYH7, LMNA |
| Coronary_Artery_Disease | treatments | 5/6 — antiplatelets, ACE-I, beta blockers, PCI, CABG |
| Coronary_Artery_Disease | genetic | 2/4 — PCSK9, 9p21 |
| Atrial_Fibrillation | treatments | 5/7 — rate control, rhythm control, cardioversion, LAA closure, risk-factor modification |
| Atrial_Fibrillation | genetic | 4/5 — KCNQ1, KCNE2, KCNJ2, SCN5A |
| Dilated_Cardiomyopathy | treatments | 6/7 — ACE-I/ARB, beta blockers, SGLT2i, CRT, transplant, ICD |

This is the largest volume gap found. These are among the best-evidenced interventions
in medicine, and Heart_Failure's `genetic` section could be filled immediately from
ClinGen using the `CGGV:` pattern already working in HCM and DCM.

## Recommended remediation, in priority order

1. **Fix the contradictory `NO_EVIDENCE`/`SUPPORT` metadata** (Findings 1–2). Either
   replace the citation with a probative one or delete the evidence block and keep the
   claim in `notes`, per the `CLAUDE.md` SOP. Highest priority: CAD `APOE`/`LDLR`,
   Heart_Failure SGLT2 inhibitors, DCM LV systolic dysfunction.
2. **Backfill `evidence_source`** on the 139 unset items across HCM/DCM/AF/HF/CAD,
   splitting mixed-source papers (Finding 5). Remove or supplement the two phenotype
   nodes resting solely on model-organism evidence.
3. **Merge the duplicate HCM `Arrhythmias` phenotype** and replace
   `HCM.environmental[0] = "None Applicable"` with the real exertion/heat risk factors
   its own citation describes.
4. **Re-map CAD** to a coronary-specific MONDO class.
5. **Evidence the empty treatment and genetic sections** (Finding 8); ClinGen covers the
   genetic ones mechanically.
6. **Narrow the over-broad claims** in DCM `pathophysiology[3]`/`[4]` and AF
   `pathophysiology[0]` to what their citations actually support.
7. **Re-assess the HCM spaceflight `datasets` block** for scope.

Tier A entries (Brugada, Long QT, MI, ARVC, Peripartum CM) need no remediation and are
the right templates for the Tier B rewrites.

## Remediation applied

All five Tier-B entries were edited. Post-fix state:

| Entry | Evidence items | `evidence_source` unset | `NO_EVIDENCE` |
|---|---|---|---|
| Hypertrophic_Cardiomyopathy | 108 | 0 | 0 |
| Dilated_Cardiomyopathy | 83 | 0 | 0 |
| Atrial_Fibrillation | 26 | 0 | 0 |
| Heart_Failure | 23 | 0 | 0 |
| Coronary_Artery_Disease | 19 | 0 | 0 |

**Contradictory metadata removed (Findings 1–2).** The five `NO_EVIDENCE`-with-affirming-
explanation items and the non-probative `SUPPORT` items were replaced or deleted:

- CAD `APOE` → PMID:17878422 (apoE genotype–coronary risk meta-analysis, 121 studies).
- CAD `LDLR` → PMID:28444290 (EAS consensus: reduced LDL-receptor function raises ASCVD risk).
- CAD `PCSK9` (was unevidenced) → PMID:16554528 (ARIC: PCSK9 nonsense variants, −88% CHD).
- CAD `9p21` (was unevidenced) → PMID:17478681 (original 9p21 GWAS).
- CAD `LDL Cholesterol` → PMID:28444290; CAD `C-Reactive Protein` → PMID:20031199 (ERFC meta-analysis).
- CAD `Myocardial Infarction` phenotype → PMID:24902970 (plaque rupture → acute coronary syndrome).
- Heart_Failure SGLT2 inhibitors → PMID:31535829 (DAPA-HF outcome data added alongside the guideline).
- Atrial_Fibrillation thrombus node → PMID:8572814 (91% of nonrheumatic AF thrombi in the LAA).
- DCM `LV systolic dysfunction` and `Dilated cardiomyopathy` phenotypes → PMID:39519012; the
  null-LVEF result is retained but demoted to `PARTIAL` and reframed as a qualifier.
- HCM: six non-probative items deleted (the prevalence-trend and generic-arrhythmia
  citations, the troponin gene/biomarker conflation, the CCB-for-angina and
  indirect-myectomy citations, and the LVH-in-diverse-conditions subtype citation), plus
  one item whose "snippet" was just an article title.

**`evidence_source` backfilled (Finding 5).** 139 items across the five entries, classified
per reference: narrative reviews/guidelines/expert curation → `OTHER`; original human
studies → `HUMAN_CLINICAL`; in vivo animal work → `MODEL_ORGANISM`. Mixed-source papers
(PMID:39146015, PMID:40594772) were assigned per snippet.

**Structural fixes (Finding 7).** The duplicate HCM `Arrhythmias` phenotype was merged
(richer node kept, evidence folded in, 11 → 10 phenotypes); `HCM.environmental[0]` changed
from the self-refuting `None Applicable`/`REFUTE` to `Strenuous exertion and heat stress`
with `SUPPORT`; the deprecated `percentage: 0.2` was dropped; CAD re-mapped to
`MONDO:0021661` *coronary atherosclerosis*; the carotid-to-coronary extrapolation is now
stated explicitly in the two affected explanations; the NAMeRS/issue-number curation note
was removed from a DCM evidence explanation.

**Over-broad claims narrowed (Finding 6).** DCM `RNA Splicing Dysregulation` and `Immune
and Inflammatory Activation` descriptions now separate what the cited evidence shows from
what is proposed; the DCM neurohormonal explanation now states it is therapeutic rather
than direct mechanistic evidence; the "AF begets AF" claim gained its actual source
(PMID:7671380, Wijffels).

**Partial progress on Finding 8.** Heart_Failure `genetic` (TTN/MYH7/LMNA) now uses ClinGen
`CGGV:` assertions; HF ACE-I/ARB, beta blockers and MRA anchor on PMID:37254024 (GDMT); AF
rhythm control and risk-factor modification anchor on PMID:40526576; CAD antiplatelet
therapy on PMID:11786451.

### Still open

Treatment and phenotype blocks that remain unevidenced — a curation-volume task, not a
correctness defect: DCM treatments (6/7), CAD treatments (4/6: ACE-I, beta blockers, PCI,
CABG), HF treatments (4/8: ARNI, diuretics, CRT, ICD), AF treatments (3/7: rate control,
cardioversion, LAA closure), AF `genetic` (KCNQ1, KCNE2, KCNJ2, SCN5A), and assorted
phenotype/biochemical blocks. The HCM spaceflight `datasets` scope question (Finding 7) is
a curation-policy judgement and was left for maintainers.

### Verification

- All 495 evidence items across the ten entries re-checked offline against
  `references_cache`: 0 snippet mismatches. (The single flagged HCM item is the
  pre-existing `definitive ( MYBPC3` line-wrap artifact in the cache, not a curation error.)
- `linkml-validate` against the `Disease` class: no issues on all five edited entries.
- `linkml-term-validator` with `--labels`: passes on all five. Note that the configured
  `ols:mondo` adapter cannot perform ancestor traversal, so `cache/enums/diseaseterm_*.csv`
  is the effective membership source for MONDO terms; a new binding needs its CURIE there,
  verified against the local `sqlite:obo:mondo` adapter.
- `pytest tests/test_data.py`: 28 global structural tests and all 55 per-file tests for the
  edited entries pass. (Remaining warnings about missing `subtype_term` are pre-existing.)
- Eight new reference cache files were fetched with the validator, never hand-written.
  Three PMIDs initially recalled from memory turned out to be unrelated papers and were
  discarded — the correct sources were located via PubMed search and verified before use.
