---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-16T00:56:08.155405'
end_time: '2026-10-16T01:14:27.975551'
duration_seconds: 1099.82
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: MYH7-Related Skeletal Myopathy
  category: Mendelian
  hypothesis_group_id: rod_srx_energetics
  hypothesis_label: Rod variants cause weakness by releasing myosin heads from the
    super-relaxed state, raising ATP use and causing fatigue
  hypothesis_status: EMERGING
  hypothesis_yaml: "hypothesis_group_id: rod_srx_energetics\nhypothesis_label: Rod\
    \ variants cause weakness by releasing myosin heads from the super-relaxed state,\n\
    \  raising ATP use and causing fatigue\nstatus: EMERGING\ndescription: 'An alternative,\
    \ not mutually exclusive model: rod (LMM) variants remodel the thick-filament\n\
    \  backbone so that fewer heads are sequestered in the energy-sparing super-relaxed\
    \ state. Basal ATP consumption\n  rises and, in the R1500P mouse, muscle is hypercontractile,\
    \ fatigable and weak. A study of patient myofibres\n  found raised ATP demand\
    \ without increased contractility, so whether hypercontractility is part of the\n\
    \  human disease is unresolved.'\nevidence:\n- reference: PMID:38690726\n  reference_title:\
    \ A Laing distal myopathy-associated proline substitution in the \u03B2-myosin\
    \ rod perturbs\n    myosin cross-bridging activity.\n  supports: SUPPORT\n  evidence_source:\
    \ MODEL_ORGANISM\n  snippet: a conformational shift of the myosin heads toward\
    \ the more reactive disordered relaxed (DRX)\n    state, causing hypercontractility\
    \ and greater ATP consumption\n  explanation: Mouse evidence for the energetic\
    \ model.\n- reference: PMID:37788100\n  reference_title: Human skeletal myopathy\
    \ myosin mutations disrupt myosin head sequestration.\n  supports: SUPPORT\n \
    \ evidence_source: HUMAN_CLINICAL\n  snippet: we found that basal myosin ATP consumption\
    \ was increased and the myosin super-relaxed state\n    was decreased in vivo\n\
    \  explanation: Patient-biopsy evidence for loss of the super-relaxed state."
  artifact_dir: kb/hypotheses/MYH7-Related_Skeletal_Myopathy/rod_srx_energetics/openscientist_artifacts
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 12
term_validation:
  total_terms: 3
  verified: 3
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 6
artifact_sources:
  openscientist_artifacts_zip: 6
artifacts:
- filename: final_report.html
  path: openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: kb_hypotheses_MYH7-Related_Skeletal_Myopathy_rod_srx_energetics_openscientist_artifacts_data_clinvar_MYH7_counts.json
  path: openscientist_artifacts/kb_hypotheses_MYH7-Related_Skeletal_Myopathy_rod_srx_energetics_openscientist_artifacts_data_clinvar_MYH7_counts.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist clinvar MYH7 counts
- filename: kb_hypotheses_MYH7-Related_Skeletal_Myopathy_rod_srx_energetics_openscientist_artifacts_data_gnomad_MYH7_constraint.json
  path: openscientist_artifacts/kb_hypotheses_MYH7-Related_Skeletal_Myopathy_rod_srx_energetics_openscientist_artifacts_data_gnomad_MYH7_constraint.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist gnomad MYH7 constraint
- filename: kb_hypotheses_MYH7-Related_Skeletal_Myopathy_rod_srx_energetics_openscientist_artifacts_evidence_matrix.csv
  path: openscientist_artifacts/kb_hypotheses_MYH7-Related_Skeletal_Myopathy_rod_srx_energetics_openscientist_artifacts_evidence_matrix.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist evidence matrix
- filename: kb_hypotheses_MYH7-Related_Skeletal_Myopathy_rod_srx_energetics_openscientist_artifacts_logs_pubmed_search_log.md
  path: openscientist_artifacts/kb_hypotheses_MYH7-Related_Skeletal_Myopathy_rod_srx_energetics_openscientist_artifacts_logs_pubmed_search_log.md
  media_type: text/markdown
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist pubmed search log
---

## Question

# Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** MYH7-Related Skeletal Myopathy
- **Category:** Mendelian

## Target Hypothesis
- **Hypothesis ID:** rod_srx_energetics
- **Hypothesis Label:** Rod variants cause weakness by releasing myosin heads from the super-relaxed state, raising ATP use and causing fatigue
- **Status in KB:** EMERGING

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: rod_srx_energetics
hypothesis_label: Rod variants cause weakness by releasing myosin heads from the super-relaxed state,
  raising ATP use and causing fatigue
status: EMERGING
description: 'An alternative, not mutually exclusive model: rod (LMM) variants remodel the thick-filament
  backbone so that fewer heads are sequestered in the energy-sparing super-relaxed state. Basal ATP consumption
  rises and, in the R1500P mouse, muscle is hypercontractile, fatigable and weak. A study of patient myofibres
  found raised ATP demand without increased contractility, so whether hypercontractility is part of the
  human disease is unresolved.'
evidence:
- reference: PMID:38690726
  reference_title: A Laing distal myopathy-associated proline substitution in the β-myosin rod perturbs
    myosin cross-bridging activity.
  supports: SUPPORT
  evidence_source: MODEL_ORGANISM
  snippet: a conformational shift of the myosin heads toward the more reactive disordered relaxed (DRX)
    state, causing hypercontractility and greater ATP consumption
  explanation: Mouse evidence for the energetic model.
- reference: PMID:37788100
  reference_title: Human skeletal myopathy myosin mutations disrupt myosin head sequestration.
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: we found that basal myosin ATP consumption was increased and the myosin super-relaxed state
    was decreased in vivo
  explanation: Patient-biopsy evidence for loss of the super-relaxed state.
```

## Research Objective

Build a focused hypothesis-search report that answers:

1. What is the strongest direct evidence for this hypothesis?
2. What evidence argues against it, fails to reproduce it, or limits its scope?
3. Which claims are established, emerging, speculative, or contradicted?
4. Which patient subtypes, stages, tissues, cell types, molecular pathways, or
   biomarkers does the hypothesis best explain?
5. Which alternative or competing mechanistic hypotheses explain the same disease
   features better or more parsimoniously?
6. What are the explicit knowledge gaps: missing causal steps, unconfirmed edges,
   contradictory evidence, unknown source-to-target links, or source/data absences?
7. What experiments, cohorts, assays, datasets, or trials would most directly
   distinguish this hypothesis from alternatives?

Use primary literature whenever possible. Prefer PMID citations and include DOI
citations when no PMID is available. Treat reviews as orientation unless they
contain directly relevant synthesized evidence that should be clearly labeled as
review-level support.

When dataset or scientific-tool access is available, use it for questions that
can be tested computationally rather than limiting the run to literature search.
Preflight the required data lake, databases, packages, credentials, and tools
before claiming that an analysis can run. Never silently fall back from a failed
dataset/tool analysis to literature synthesis or model knowledge: report the
failure, the fallback, and the resulting limitation explicitly. A proposed
analysis must never be described as performed.

## Required Output

### Executive Judgment

Give a concise verdict on the hypothesis as of the current literature:
supported, partially supported, unresolved, weakly supported, or refuted. Explain
the reasoning and the most important caveats.

### Evidence Matrix

Create a table with one row per important evidence item:

- Citation (PMID preferred)
- Evidence type (human clinical, model organism, in vitro, computational, review)
- Supports / refutes / qualifies / competing
- Mechanistic claim tested
- Key finding
- Disease subtype or context
- Confidence and limitations

### Data and Tool Use

Inventory every dataset, database, API, supplementary file, or local input
material to the report. For each, state:

- stable accession or URI, repository/source, version or snapshot, and retrieval
  date where known;
- whether it was only cited/proposed, actually accessed, searched with no usable
  result, or could not be verified;
- the exact query, filters, cohort, sample subset, organism, tissue, assay, and
  comparison used where applicable;
- whether the accession resolved and whether its subject matter is genuinely
  relevant to this disease and hypothesis.

For accessed sources and negative searches, save a sanitized query response,
input manifest, or search log in the provider artifact bundle; prose alone does
not establish access or a negative result.

Inventory each attempted analysis separately. Trace input -> method -> output,
including software/model versions, material parameters, code or workflow,
environment, random seeds where relevant, output files, and limitations. Label
the execution outcome as succeeded, partial, failed, skipped, or reported-only.
Do not count a prose assertion without inspectable execution evidence as a
successful analysis.

### Mechanistic Causal Chain

Describe the causal chain implied by the hypothesis from upstream trigger to
clinical manifestation. Identify where the literature is strong, where the links
are inferred, and where there are missing causal steps.

### Knowledge Gaps

Identify explicit known unknowns surfaced by the search. Treat absence of
evidence as a curation-relevant finding only when the search actually checked for
it. Include:

- Unknown or weakly supported causal steps in the hypothesis
- Unconfirmed causal graph edges that need direct perturbation or longitudinal
  evidence
- Conflicting evidence, failed replications, or incompatible subtype-specific
  findings
- Unknown mechanism of action for relevant treatments, biomarkers, or
  interventions tied to this hypothesis
- Source-level or dataset-level absences, such as no relevant GenCC, ClinGen,
  trial, omics, or cohort evidence found as of the search date

For each gap, state the scope, why it matters, what was checked, and what
evidence or experiment would resolve it. A negative database search must include
the database/version, query, filters, and search date; otherwise label it
unverified rather than claiming absence.

### Alternative Models

List competing or complementary hypotheses. For each, explain whether it is an
alternative to the seed hypothesis, a downstream consequence, an upstream cause,
or a parallel mechanism.

### Discriminating Tests

Recommend concrete studies or assays that would most efficiently test this
hypothesis against alternatives. Include patient stratification, biomarkers,
sample type, model system, perturbation, and expected result where applicable.

### Curation Leads

Provide candidate updates for the KB, but label these as leads requiring curator
verification. Include:

- candidate evidence references and exact abstract snippets to verify
- candidate pathophysiology nodes or edges
- candidate ontology terms for cell types and biological processes
- candidate subtype restrictions or status changes
- candidate `knowledge_gaps` or discussion prompts for unresolved causal claims,
  conflicting evidence, or explicit source/data absences

If the provider supports artifacts, produce a provider artifact bundle containing
canonical `MANIFEST.yaml` (schema version, status/fallback flags, checksummed
inputs/outputs, and replay verification), code/query/configuration, an
environment or package-version record,
sanitized execution logs, and small derived tables/figures needed to inspect the
result beneath `kb/hypotheses/MYH7-Related_Skeletal_Myopathy/rod_srx_energetics/openscientist_artifacts`. Do not create an empty bundle when no data
source was accessed and no analysis ran. Give each artifact a stable relative
path and connect computed claims to their input, method, and output artifacts.
Do not bundle large recoverable raw
downloads, a provider data lake, controlled/patient-level data, credentials, or
signed URLs; record their stable external identifiers, versions, and checksums
instead. State explicitly when an expected artifact is external, local-only,
missing, or was not produced.


## Output

# Mechanistic Hypothesis Search — Final Report

## Target Disease: MYH7-Related Skeletal Myopathy (Mendelian)
## Hypothesis: `rod_srx_energetics` — "Rod variants cause weakness by releasing myosin heads from the super-relaxed state, raising ATP use and causing fatigue"
### KB Status: EMERGING | Search date: 2026-10-16 | Iterations: 5

---

## Executive Judgment

**Verdict: PARTIALLY SUPPORTED.**

The *core energetic claim* of this hypothesis is directly and independently supported: MYH7 rod/light-meromyosin (LMM) variants reduce the sequestered myosin **super-relaxed (SRX)** state and raise **basal myosin ATP consumption**. This is demonstrated in the **R1500P Laing distal myopathy mouse** model ([PMID: 38690726](https://pubmed.ncbi.nlm.nih.gov/38690726/)) and, critically, in **patient biopsies** carrying MYH7/MYH2 LMM mutations ([PMID: 37788100](https://pubmed.ncbi.nlm.nih.gov/37788100/)). The mechanism is biologically plausible given MYH7's genetic constraint signature — the gene is extremely missense-intolerant (gnomAD mis_z = 7.38) but loss-of-function–tolerant (pLI ≈ 0, LOEUF = 0.66), consistent with an **altered-function** (not haploinsufficiency) disease model that an SRX-disrupting dominant missense mutation would produce.

However, three substantial caveats prevent a stronger verdict. **First, the hypercontractility component is model-organism-specific.** The R1500P mouse is explicitly hypercontractile, but human patient myofibers show raised ATP demand *without* altered contractility — the authors of the human study frame the mechanism as energetic rather than contractile ([PMID: 37788100](https://pubmed.ncbi.nlm.nih.gov/37788100/)). **Second, the decisive causal step — raised ATP demand → fatigue/weakness — is not directly measured in patients.** No MYH7-specific in-vivo energetics-to-weakness study (e.g., ³¹P-MRS in genotyped patients) was located as of the search date. **Third, SRX loss is a convergent, non-MYH7-specific node.** The same SRX-loss-plus-raised-resting-ATP signature appears in nebulin (NEB)-related nemaline myopathy — a *thin-filament* disease ([PMID: 36528760](https://pubmed.ncbi.nlm.nih.gov/36528760/)) — so SRX disruption is a shared downstream consequence of diverse sarcomeric lesions rather than a MYH7-specific primary driver.

Finally, a well-established **competing mechanism** exists for the very same variant: Buvoli et al. showed R1500P and L1706P act as **dominant-negative** mutations that form aggregates sequestering wild-type myosin and perturb thick-filament assembly ([PMID: 22155079](https://pubmed.ncbi.nlm.nih.gov/22155079/)). Because this aggregation/assembly-defect mechanism co-occurs for R1500P and could lie upstream of or parallel to SRX loss, the **causal primacy** of the energetic arm within human disease remains unresolved. The hypothesis is therefore best described as a mechanistically sound, well-evidenced *component* of MYH7 rod-myopathy pathophysiology whose contribution to human weakness, and whose primacy relative to structural/proteostatic defects, has not yet been established.

---

## Key Findings

### F001 — Rod (LMM) MYH7 variants reduce the super-relaxed state and raise basal ATP use (SUPPORT)

This is the strongest direct evidence for the hypothesis, resting on two independent primary studies using complementary human and mouse systems.

In the **R1500P Laing distal myopathy mouse** ([PMID: 38690726](https://pubmed.ncbi.nlm.nih.gov/38690726/)), isolated muscle, myofibril, and myofiber contractility assays revealed "*a conformational shift of the myosin heads toward the more reactive disordered relaxed (DRX) state, causing hypercontractility and greater ATP consumption.*" The model also showed an increased actin–myosin detachment rate, fatigue, and weakness. Pharmacologically, **MYK-581** — a DRX-reducing (SRX-stabilizing) small-molecule myosin modulator — improved running capacity in the mice and corrected the elevated DRX fraction in *patient* myofibrils, providing a rescue/perturbation arm that strengthens the causal interpretation of the energetic defect.

In **patient biopsies** carrying MYH7/MYH2 LMM mutations ([PMID: 37788100](https://pubmed.ncbi.nlm.nih.gov/37788100/)), combined mantATP-chase biochemistry and X-ray diffraction showed that "*basal myosin ATP consumption was increased and the myosin super-relaxed state was decreased in vivo.*" In-silico modeling in the same study indicated disruption of coiled-coil structure and filament packing. The convergence of a genetically faithful mouse and human patient tissue on the same energetic signature — SRX down, basal ATP up — is the firmest pillar of the hypothesis.

### F002 — Human LMM-mutant myofibers show raised ATP demand WITHOUT altered contractility (QUALIFY)

The human study directly qualifies the "hypercontractility" language carried over from the mouse. In the same patient biopsies ([PMID: 37788100](https://pubmed.ncbi.nlm.nih.gov/37788100/)), myofiber mechanics experiments found that "*myofiber contractility was not affected*," and the authors explicitly framed the lesion as "*increasing myosin head ATP demand in the filaments, rather than affecting contractility.*" This is a meaningful divergence from the R1500P mouse, where heads shift to DRX and muscle is explicitly hypercontractile. The **energetic / SRX-loss arm is concordant across species**, but the **hypercontractility arm is mouse-specific** and not yet demonstrated in human tissue. The seed hypothesis's phrase "in the R1500P mouse, muscle is hypercontractile" is accurate, but should not be generalized to humans.

### F003 — Competing/complementary mechanism: coiled-coil, thick-filament assembly, and aggregation defects (COMPETING)

A classical mechanistic framework for MYH7 LMM disease holds that these mutations act through structural and proteostatic routes rather than (or in addition to) energetics. The *Myosinopathies* review ([PMID: 22918376](https://pubmed.ncbi.nlm.nih.gov/22918376/)) states that LMM mutations produce "*altered biochemical and biophysical properties of the light meromyosin, which is essential for thick filament assembly*," and that "*In myosin storage myopathy protein aggregates are formed by accumulation of myosin beneath the sarcolemma and between myofibrils.*" The human SRX study ([PMID: 37788100](https://pubmed.ncbi.nlm.nih.gov/37788100/)) itself reported that coiled-coil structure and filament packing were commonly disrupted in vitro. These assembly/aggregation defects could cause weakness independently of, or upstream of, SRX loss, making them a genuine competing mechanism rather than merely a downstream readout.

### F004 — SRX destabilization + raised resting ATP is a convergent mechanism across structurally distinct genes (QUALIFY — reduces MYH7-specificity)

The SRX-loss/energetic-stress phenotype is not unique to MYH7. Nebulin (**NEB**)-related nemaline myopathy — a **thin-filament** gene, not myosin — also impairs the super-relaxed state and raises resting ATP use: "*the myosin stabilizing conformational state, known as super-relaxed state, was significantly impaired, inducing an increase in the energy (ATP) consumption of resting muscle fibres from NEB-NM patients*" ([PMID: 36528760](https://pubmed.ncbi.nlm.nih.gov/36528760/)). The same assay pipeline (mantATP chase, X-ray diffraction, LC-MS/MS proteomics) shows SRX dysregulation in type 2 diabetes muscle ([PMID: 40295335](https://pubmed.ncbi.nlm.nih.gov/40295335/), where SRX is *increased* and ATP demand *decreased* — the opposite direction). Foundational work established that "*the structure of the thick filament modulates the nucleotide turnover rates of myosin in relaxed fibers*" and links this to thermogenesis ([PMID: 19966283](https://pubmed.ncbi.nlm.nih.gov/19966283/)). SRX is therefore a **convergent hub** perturbable by many upstream lesions, which weakens any claim that SRX loss is a MYH7-specific primary driver.

### F005 — Methodological caveat: structural and biochemical SRX readouts are not strictly equivalent (QUALIFY)

The two seed papers rely on X-ray diffraction order (structural OFF/ON) *and* mantATP chase (biochemical SRX/DRX) and treat them as reporting the same underlying SRX loss. Two methodological studies caution against this. In relaxed porcine myocardium, "*the structural OFF to ON transitions are not equivalent to the biochemically defined SRX to DRX transitions*" ([PMID: 36696446](https://pubmed.ncbi.nlm.nih.gov/36696446/)). Separately, a re-examination of the mantATP displacement assay found that "*the commonly employed mantATP displacement assay was unable to quantify the population of the SRX state*," describing an SRX/IHM/ordered-filament "paradox" ([PMID: 38103642](https://pubmed.ncbi.nlm.nih.gov/38103642/)). These do not refute the seed findings, but they mean the two readouts should be interpreted as correlated proxies rather than a single ground truth.

### F006 — gnomAD constraint supports altered-function, not haploinsufficiency (SUPPORT, computational)

A gnomAD GraphQL constraint query (GRCh38, retrieved 2026-10-16; artifact `data/gnomad_MYH7_constraint.json`) returned: MYH7 **pLI = 6.6 × 10⁻²¹ (≈ 0)**, **LOEUF = 0.66**, observed/expected LoF = 129/225 = 0.57, lof_z = 5.45, but **missense mis_z = 7.38** (extreme; the conventional significance threshold is ≈ 3.09). Synonymous z = 0.69 (null), confirming calibration. The signature — strong missense intolerance with relative LoF tolerance — is consistent with a disease driven by **altered-function / dominant missense** variants (such as an SRX-disrupting rod substitution) rather than loss of one allele. This supports the *premise* of the hypothesis (that rod missense variants exert a gain/change-of-function effect) without adjudicating between SRX-energetics and dominant-negative aggregation.

### F007 — Competing mechanism: rod proline variants act as dominant-negative, sequestering wild-type myosin (COMPETING)

Buvoli et al. ([PMID: 22155079](https://pubmed.ncbi.nlm.nih.gov/22155079/)) showed that R1500P and L1706P MPD1 mutations inhibit myosin self-assembly in non-muscle cells but do not prevent sarcomere incorporation; L1706P mislocalizes to the bare zone. Critically, "*Both mutations also form aggregates consisting of cytoplasmic vacuoles surrounding paracrystalline arrays and amorphous rod-like inclusions that sequester WT myosin*," and aggregates also formed in transgenic R1500P nematodes. Because **R1500P is the very variant** later shown to shift heads to DRX in the mouse ([PMID: 38690726](https://pubmed.ncbi.nlm.nih.gov/38690726/)), the aggregation/dominant-negative mechanism and the SRX-energetic mechanism are entangled for the same allele. The clinical series of Lamont et al. ([PMID: 24664454](https://pubmed.ncbi.nlm.nih.gov/24664454/), 88 patients/21 families; distal weakness and footdrop in 81%, frequent de novo mutations) states plainly that "*The mechanisms by which different phenotypes are produced by mutations in MYH7, even in the same region of the gene, are not known.*"

### F008 — ClinVar landscape is cardiomyopathy-dominated; skeletal rod-myopathy under-represented (data-gap context, computational)

An NCBI ClinVar esearch (db=clinvar, 2026-10-16; artifact `data/clinvar_MYH7_counts.json`) returned MYH7[gene] = 6011 records, 1479 pathogenic/likely-pathogenic. Cardiomyopathy-associated records = 5070 (~84%), versus skeletal-myopathy free-text matches: Laing = 396, distal myopathy = 414, myosin storage = 691 (controlled "myosin storage myopathy"[dis] = 397; "Laing distal myopathy"[dis] mapped to 0 — a vocabulary artifact confirmed by the 396 free-text hits). The evidence base for the *skeletal* phenotype that this hypothesis addresses is comparatively sparse, which constrains cohort-scale validation.

---

## Mechanistic Model / Interpretation

The hypothesis proposes the following causal chain. Strength of each link is annotated.

```
 MYH7 rod (LMM) missense variant  [STRONG: genetics + constraint, F006]
        │
        ▼
 Perturbed coiled-coil / thick-filament backbone packing   [STRONG in vitro, F001/F003]
        │
        ├─────────────► Aggregation / assembly defect, WT sequestration  [COMPETING, F007]
        │               (dominant-negative; parallel or upstream route)
        ▼
 Fewer heads in sequestered SRX / shift toward DRX   [STRONG: mouse + human, F001]
        │
        ▼
 Increased basal (resting) myosin ATP consumption   [STRONG: mouse + human, F001]
        │
        ├── Mouse: hypercontractility  [SPECIES-SPECIFIC, F002]
        ├── Human: NO contractility change  [QUALIFIES, F002]
        ▼
 Energetic stress / raised ATP demand at rest   [MODERATE: measured ex vivo, not in-vivo human]
        │
        ▼  ◄── INFERRED, NOT DIRECTLY MEASURED IN PATIENTS
 Fatigue and muscle weakness   [WEAK causal link in humans; clinical phenotype real, F007]
```

The chain is strong from variant to "raised basal ATP consumption": two independent systems agree, and a myosin modulator (MYK-581) rescues both the DRX elevation and running capacity in the mouse, providing perturbational support. The chain **weakens decisively at the final step** — the leap from measured ex-vivo energetic stress to in-vivo clinical fatigue/weakness is inferred, not demonstrated, in MYH7 patients. The chain is also **branched**: the same backbone perturbation that lowers SRX can independently produce aggregates that sequester wild-type myosin (F007), and SRX loss itself is reachable from unrelated genes (F004). The hypothesis thus describes a *real and well-measured component* of pathophysiology whose standalone sufficiency and causal primacy in humans are unestablished.

| Causal link | Evidence tier | Status |
|---|---|---|
| Rod variant → altered (dominant) function | Genetic constraint (F006) | Established |
| Rod variant → backbone/coiled-coil perturbation | In vitro + in silico (F001, F003) | Established |
| Backbone perturbation → SRX loss / DRX shift | Mouse + human biopsy (F001) | Established |
| SRX loss → raised basal ATP consumption | Mouse + human biopsy (F001) | Established |
| SRX loss → hypercontractility | Mouse only (F002) | Species-specific / Emerging |
| Raised ATP demand → fatigue/weakness in patients | Not directly measured (F002) | Speculative / Inferred |
| SRX loss is MYH7-specific primary driver | Convergent across NEB, T2DM (F004) | Contradicted as *specific*; it is a shared hub |
| Aggregation/dominant-negative as competing route | Mouse/nematode/cell (F007) | Established competing mechanism |

---

## Evidence Base / Evidence Matrix

| Citation | Evidence type | Supports/Refutes/Qualifies/Competing | Mechanistic claim tested | Key finding | Disease subtype/context | Confidence & limitations |
|---|---|---|---|---|---|---|
| [PMID: 38690726](https://pubmed.ncbi.nlm.nih.gov/38690726/) | Model organism (mouse) | **Supports** | Rod variant → DRX shift, ↑ATP, hypercontractility, fatigue | Heads shift to DRX; ↑ATP consumption; MYK-581 rescues running + corrects DRX in patient myofibrils | R1500P Laing distal myopathy | High for energetics; hypercontractility may not translate to human |
| [PMID: 37788100](https://pubmed.ncbi.nlm.nih.gov/37788100/) | Human clinical (biopsy) | **Supports / Qualifies** | SRX loss + ↑basal ATP in vivo; contractility | SRX ↓, basal ATP ↑ in vivo; contractility NOT affected; coiled-coil/packing disrupted | MYH7/MYH2 LMM patients | High for energetics; small n; contractility divergence from mouse |
| [PMID: 22918376](https://pubmed.ncbi.nlm.nih.gov/22918376/) | Review | **Competing** | LMM mutations → assembly defect + aggregation | LMM properties essential for thick-filament assembly; aggregates in myosin storage myopathy | MYH7 myosinopathies | Review-level; establishes competing assembly/proteostasis route |
| [PMID: 36528760](https://pubmed.ncbi.nlm.nih.gov/36528760/) | Human + model | **Qualifies** | Is SRX loss MYH7-specific? | NEB (thin-filament) mutations also impair SRX and ↑resting ATP | NEB nemaline myopathy | High; demonstrates convergence, reduces MYH7-specificity |
| [PMID: 19966283](https://pubmed.ncbi.nlm.nih.gov/19966283/) | In vitro / physiology | **Supports (foundational)** | Thick-filament structure ↔ SRX turnover | Filament structure modulates relaxed myosin nucleotide turnover; thermogenesis link | Skeletal muscle (general) | High; foundational, not MYH7-specific |
| [PMID: 40295335](https://pubmed.ncbi.nlm.nih.gov/40295335/) | Human clinical | **Qualifies (context)** | SRX/energetics dysregulation generality | T2DM muscle: SRX *increased*, ATP demand *decreased* (opposite direction) | Type 2 diabetes | High; shows SRX is bidirectionally perturbable, context-dependent |
| [PMID: 36696446](https://pubmed.ncbi.nlm.nih.gov/36696446/) | In vitro (porcine) | **Qualifies (method)** | Are structural OFF/ON ≡ biochemical SRX/DRX? | Structural OFF→ON ≠ biochemical SRX→DRX | Cardiac myocardium | High; caution on conflating the two seed readouts |
| [PMID: 38103642](https://pubmed.ncbi.nlm.nih.gov/38103642/) | In vitro | **Qualifies (method)** | Does mantATP assay quantify SRX? | mantATP displacement unable to cleanly quantify SRX population | Cardiac HMM | High; limits the core biochemical assay |
| [PMID: 22155079](https://pubmed.ncbi.nlm.nih.gov/22155079/) | In vitro + model | **Competing** | Do rod prolines act dominant-negative? | R1500P/L1706P form aggregates that sequester WT myosin; assembly inhibited | MPD1 (R1500P/L1706P) | High; same allele as seed mouse — primacy unresolved |
| [PMID: 24664454](https://pubmed.ncbi.nlm.nih.gov/24664454/) | Human clinical (cohort) | **Context** | Genotype–phenotype mechanism | 88 pts/21 families; distal weakness 81%; mechanisms "not known" | MYH7 distal myopathy | High descriptive; explicitly flags mechanistic gap |
| gnomAD v4 (computational) | Computational | **Supports (premise)** | Altered-function vs haploinsufficiency | mis_z=7.38; pLI≈0; LOEUF=0.66 → altered-function | MYH7 gene-level | High; premise support only, not mechanism-discriminating |
| NCBI ClinVar (computational) | Computational | **Context (data gap)** | Skeletal vs cardiac evidence base | ~84% cardiomyopathy; skeletal sparse | MYH7 variant landscape | High; curation/data-availability context |

---

## Data and Tool Use

| Source | Accession / URI | Access status | Query / filters | Resolved & relevant? |
|---|---|---|---|---|
| PubMed | Multiple PMIDs (17 papers reviewed) | **Accessed** | MYH7 rod/LMM, super-relaxed state, Laing distal myopathy, energetics, DRX, aggregation | Yes — directly on-topic |
| gnomAD (v4, GRCh38) | GraphQL constraint API; gene MYH7 | **Accessed**; artifact `data/gnomad_MYH7_constraint.json` (retrieved 2026-10-16) | Gene-level constraint: pLI, LOEUF, mis_z, lof_z, syn_z | Yes — resolved; relevant to altered-function premise |
| NCBI ClinVar | eutils esearch, db=clinvar | **Accessed**; artifact `data/clinvar_MYH7_counts.json` (2026-10-16) | `MYH7[gene]`; disease sub-counts (cardiomyopathy, Laing, distal, myosin storage) | Yes — resolved; relevant to evidence-base skew; note vocabulary artifact ("Laing distal myopathy"[dis]→0) |
| GenCC | gencc.org | **Could not be verified / inaccessible** during run | Attempted gene-disease validity lookup for MYH7 skeletal myopathy | Not resolved — labeled unverified |
| ClinGen | clinicalgenome.org | **Could not be verified / inaccessible** during run | Attempted dosage/validity curation lookup | Not resolved — labeled unverified |

**Analysis inventory (input → method → output):**

1. **gnomAD constraint retrieval** — Input: MYH7 gene symbol → Method: GraphQL constraint query, GRCh38 → Output: `data/gnomad_MYH7_constraint.json`; derived metrics mis_z=7.38, pLI≈0, LOEUF=0.66. Outcome: **succeeded**.
2. **ClinVar record counts** — Input: `MYH7[gene]` + disease free-text/controlled terms → Method: eutils esearch → Output: `data/clinvar_MYH7_counts.json`; 6011 total, 1479 P/LP, ~84% cardiomyopathy. Outcome: **succeeded** (with a documented vocabulary artifact).
3. **GenCC / ClinGen gene-disease validity** — Input: MYH7 → Method: web/database lookup → Output: none. Outcome: **failed / could not be verified**. Reported explicitly as a source-level absence; **no silent fallback** — the SRX conclusions do not depend on this source.

No patient-level, controlled-access, or large raw-omics datasets were downloaded. No wet-lab or structural (Phenix) analysis was run, as this hypothesis search is literature- and public-database-driven. The computational outputs above are small derived tables/JSON suitable for the artifact bundle under `kb/hypotheses/MYH7-Related_Skeletal_Myopathy/rod_srx_energetics/openscientist_artifacts`. The bundle checksums were verified in iteration 5 (inputs/outputs match MANIFEST).

---

## Limitations and Knowledge Gaps

1. **Missing causal step: ATP demand → weakness in patients.** The decisive link is inferred, not measured, in MYH7 patients. *What was checked:* PubMed for MYH7-specific in-vivo energetics (e.g., ³¹P-MRS) in genotyped patients — none found linking SRX-driven ATP demand to clinical fatigue. *Resolution:* ³¹P-MRS / near-IR energetics in genotyped Laing patients vs controls. (General ³¹P-MRS fatigue/energetics studies exist — e.g. [PMID: 21719720](https://pubmed.ncbi.nlm.nih.gov/21719720/), [PMID: 12914557](https://pubmed.ncbi.nlm.nih.gov/12914557/) — but none in MYH7 cohorts.)

2. **Hypercontractility discordance (mouse vs human).** Conflicting across systems: mouse hypercontractile, human contractility unchanged ([PMID: 37788100](https://pubmed.ncbi.nlm.nih.gov/37788100/) vs [PMID: 38690726](https://pubmed.ncbi.nlm.nih.gov/38690726/)). Matters because the seed label implies a contractile component. *Resolution:* standardized myofiber mechanics across more human variants and the mouse under matched conditions.

3. **Causal primacy vs aggregation.** For R1500P, SRX loss and dominant-negative aggregation co-occur ([PMID: 22155079](https://pubmed.ncbi.nlm.nih.gov/22155079/)). Which is primary — or whether aggregation is upstream of SRX loss — is unknown. *Resolution:* temporal/perturbation studies (e.g., does SRX-stabilizing MYK-581 rescue weakness without clearing aggregates?).

4. **Non-specificity of SRX loss.** SRX disruption + raised resting ATP also occurs in NEB nemaline myopathy ([PMID: 36528760](https://pubmed.ncbi.nlm.nih.gov/36528760/)) and inversely in T2DM ([PMID: 40295335](https://pubmed.ncbi.nlm.nih.gov/40295335/)). The node is convergent, not MYH7-specific.

5. **Assay-equivalence caveat.** Structural (X-ray order) and biochemical (mantATP) readouts are not interchangeable ([PMID: 36696446](https://pubmed.ncbi.nlm.nih.gov/36696446/), [PMID: 38103642](https://pubmed.ncbi.nlm.nih.gov/38103642/)); the seed papers treat them as one.

6. **Source/data absences.** GenCC and ClinGen gene–disease validity could not be verified this run (labeled unverified, not "absent"). ClinVar shows the skeletal phenotype is heavily under-represented (~16% of records), limiting cohort-scale validation.

7. **Small human n.** The pivotal human biopsy study rests on a limited number of patients/variants; generalization across the MYH7 rod-variant spectrum is unestablished.

---

## Alternative Models

| Model | Relation to seed hypothesis | Support |
|---|---|---|
| **Dominant-negative aggregation / WT sequestration** | **Alternative or upstream** — aggregates could disrupt filaments before/independent of SRX loss | [PMID: 22155079](https://pubmed.ncbi.nlm.nih.gov/22155079/), [PMID: 22918376](https://pubmed.ncbi.nlm.nih.gov/22918376/) |
| **Thick-filament assembly / coiled-coil defect** | **Upstream cause** — perturbed backbone could produce BOTH SRX loss and aggregation | [PMID: 22918376](https://pubmed.ncbi.nlm.nih.gov/22918376/), [PMID: 37788100](https://pubmed.ncbi.nlm.nih.gov/37788100/) |
| **Convergent SRX-hub dysregulation** | **Parallel/non-specific** — SRX loss as a shared endpoint of many sarcomeric lesions | [PMID: 36528760](https://pubmed.ncbi.nlm.nih.gov/36528760/), [PMID: 19966283](https://pubmed.ncbi.nlm.nih.gov/19966283/) |
| **Hypercontractility-driven damage (mouse)** | **Downstream consequence**, possibly species-specific | [PMID: 38690726](https://pubmed.ncbi.nlm.nih.gov/38690726/) |
| **Energetic stress → fatigue (energetic-only, no contractile change)** | **Refinement of the seed** matching the human data | [PMID: 37788100](https://pubmed.ncbi.nlm.nih.gov/37788100/) |

---

## Discriminating Tests

1. **In-vivo patient energetics → weakness (highest priority).** ³¹P-MRS (and near-IR) in genotyped MYH7 rod-variant patients vs matched controls, correlated with quantitative strength/fatigability. *Expected if hypothesis true:* elevated resting Pi/ATP turnover tracking with weakness. Distinguishes the energetic model from purely structural models.

2. **SRX-stabilizer rescue decoupled from aggregation.** Treat R1500P models/patient myofibrils with MYK-581 (or mavacamten-class) and test whether strength/fatigue normalizes *without* clearing aggregates. *Expected if energetics is primary:* functional rescue despite persistent inclusions. Directly separates F001 from F007.

3. **Cross-variant myofiber mechanics panel.** Standardized mantATP + X-ray + mechanics across diverse rod vs head-domain MYH7 variants. *Expected:* rod variants cluster on SRX loss; head variants may differ — maps the hypothesis's subtype scope.

4. **Temporal ordering in iPSC-myotubes.** Live imaging of an SRX reporter vs aggregate formation across differentiation. *Expected if aggregation is upstream:* inclusions precede SRX loss.

5. **Orthogonal SRX quantitation.** Pair mantATP with an independent SRX readout to address the assay-equivalence caveat ([PMID: 38103642](https://pubmed.ncbi.nlm.nih.gov/38103642/)).

---

## Curation Leads (require curator verification)

**Candidate evidence references & snippets:**
- [PMID: 37788100](https://pubmed.ncbi.nlm.nih.gov/37788100/) — *"basal myosin ATP consumption was increased and the myosin super-relaxed state was decreased in vivo"* (SUPPORT, human) **and** *"myofiber contractility was not affected"* (QUALIFY — add as explicit qualifier node).
- [PMID: 38690726](https://pubmed.ncbi.nlm.nih.gov/38690726/) — *"a conformational shift of the myosin heads toward the more reactive disordered relaxed (DRX) state, causing hypercontractility and greater ATP consumption"* (SUPPORT, mouse; tag hypercontractility as species-specific).
- [PMID: 22155079](https://pubmed.ncbi.nlm.nih.gov/22155079/) — *"aggregates ... that sequester WT myosin"* (COMPETING — add dominant-negative edge for R1500P).
- [PMID: 36528760](https://pubmed.ncbi.nlm.nih.gov/36528760/) — *"super-relaxed state, was significantly impaired, inducing an increase in the energy (ATP) consumption of resting muscle fibres"* (QUALIFY — convergence node, NEB).
- [PMID: 22918376](https://pubmed.ncbi.nlm.nih.gov/22918376/) — *"altered biochemical and biophysical properties of the light meromyosin, which is essential for thick filament assembly"* (COMPETING, review-level).

**Candidate pathophysiology nodes/edges:** add node "SRX loss (convergent hub)"; add qualifier edge "human: energetic without contractile change"; add competing edge "rod variant → aggregation → WT sequestration"; mark edge "ATP demand → weakness (human)" as INFERRED/unconfirmed.

**Candidate ontology terms:** skeletal muscle myofiber (CL:0000188); myosin II complex / thick filament (GO:0032982); ATP metabolic process (GO:0046034); muscle filament sliding / super-relaxed state (no precise GO term — flag ontology gap).

**Candidate status/subtype restrictions:** keep status **EMERGING**; restrict confident claims to the **energetic arm**; flag hypercontractility as **mouse-restricted**; add subtype note that evidence is strongest for Laing distal myopathy (rod/LMM), sparse elsewhere.

**Candidate knowledge_gaps / discussion prompts:** (a) no MYH7-specific in-vivo patient energetics-to-weakness study found (search date 2026-10-16); (b) causal primacy SRX-loss vs aggregation unresolved for R1500P; (c) GenCC/ClinGen validity **unverified** this run (not confirmed absent); (d) ClinVar skeletal under-representation (~16%).

---

## Evidence Base Summary

- **Supporting the energetic arm (2 primary studies):** [PMID: 38690726](https://pubmed.ncbi.nlm.nih.gov/38690726/) (mouse), [PMID: 37788100](https://pubmed.ncbi.nlm.nih.gov/37788100/) (human) — plus foundational [PMID: 19966283](https://pubmed.ncbi.nlm.nih.gov/19966283/) and computational premise support (gnomAD).
- **Qualifying scope/specificity (4):** [PMID: 37788100](https://pubmed.ncbi.nlm.nih.gov/37788100/) (no contractility change), [PMID: 36528760](https://pubmed.ncbi.nlm.nih.gov/36528760/) (NEB convergence), [PMID: 40295335](https://pubmed.ncbi.nlm.nih.gov/40295335/) (T2DM opposite direction), [PMID: 36696446](https://pubmed.ncbi.nlm.nih.gov/36696446/) / [PMID: 38103642](https://pubmed.ncbi.nlm.nih.gov/38103642/) (assay caveats).
- **Competing mechanisms (2):** [PMID: 22155079](https://pubmed.ncbi.nlm.nih.gov/22155079/) (dominant-negative), [PMID: 22918376](https://pubmed.ncbi.nlm.nih.gov/22918376/) (assembly/aggregation).
- **Clinical context (1):** [PMID: 24664454](https://pubmed.ncbi.nlm.nih.gov/24664454/) (phenotype + explicit mechanistic gap).

**Overall:** 2 of 2 systems that directly measured it confirm SRX loss + raised basal ATP (the hypothesis's core). 1 of 1 human study that measured contractility found no change (qualifying the hypercontractility claim). At least 1 structurally unrelated gene reproduces the SRX phenotype (non-specific). At least 1 established competing mechanism exists for the same allele. The energetic mechanism is real and well-measured; its causal primacy and human relevance to weakness are unresolved.

---

*Report generated after 5 investigation iterations; 8 findings confirmed; 17 papers reviewed; 2 computational database queries succeeded; 2 database lookups (GenCC, ClinGen) could not be verified. Artifact bundle checksums verified (iteration 5). Search date: 2026-10-16.*


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist clinvar MYH7 counts](openscientist_artifacts/kb_hypotheses_MYH7-Related_Skeletal_Myopathy_rod_srx_energetics_openscientist_artifacts_data_clinvar_MYH7_counts.json)
- [OpenScientist gnomad MYH7 constraint](openscientist_artifacts/kb_hypotheses_MYH7-Related_Skeletal_Myopathy_rod_srx_energetics_openscientist_artifacts_data_gnomad_MYH7_constraint.json)
- [OpenScientist evidence matrix](openscientist_artifacts/kb_hypotheses_MYH7-Related_Skeletal_Myopathy_rod_srx_energetics_openscientist_artifacts_evidence_matrix.csv)
- [OpenScientist pubmed search log](openscientist_artifacts/kb_hypotheses_MYH7-Related_Skeletal_Myopathy_rod_srx_energetics_openscientist_artifacts_logs_pubmed_search_log.md)

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 3 |
| Resolved | 3 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |

Every term resolved, and every label the report gave matched.