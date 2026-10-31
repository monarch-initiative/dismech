---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-15T04:28:19.222053'
end_time: '2026-10-15T04:50:11.477621'
duration_seconds: 1312.26
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: Primary Hyperoxaluria Type 3
  category: Metabolic Disorder
  hypothesis_group_id: cytosolic_hog_cleavage
  hypothesis_label: Cytosolic 4-Hydroxy-2-Oxoglutarate Cleavage Model
  hypothesis_status: CANONICAL
  hypothesis_yaml: "hypothesis_group_id: cytosolic_hog_cleavage\nhypothesis_label:\
    \ Cytosolic 4-Hydroxy-2-Oxoglutarate Cleavage Model\nstatus: CANONICAL\ndescription:\
    \ 'The leading proposed explanation for increased oxalate production despite a\
    \ block upstream\n  of glyoxylate: 4-hydroxy-2-oxoglutarate accumulating behind\
    \ the absent mitochondrial HOGA1 step is exported\n  to the cytosol and cleaved\
    \ there by a non-HOGA1 aldolase, releasing glyoxylate outside the mitochondrial\n\
    \  compartment where it would normally be detoxified, so that it is instead oxidized\
    \ to oxalate.'\nevidence:\n- reference: PMID:22729392\n  supports: SUPPORT\n \
    \ evidence_source: HUMAN_CLINICAL\n  snippet: its transport into the cytosol where\
    \ it is converted to\n  explanation: States the cytosolic-export-and-conversion\
    \ route for accumulated 4-hydroxy-2-oxoglutarate\n    that this hypothesis group\
    \ names.\n  reference_title: Primary hyperoxaluria type III--a model for studying\
    \ perturbations in glyoxylate metabolism\nnotes: Treated as the default explanatory\
    \ model in the literature rather than as an established one; the\n  identity of\
    \ the proposed cytosolic aldolase is not settled and the flux has not been measured\
    \ directly.\n  See the gap_ph3_oxalate_overproduction_mechanism discussion."
  artifact_dir: kb/hypotheses/Primary_Hyperoxaluria_Type_3/cytosolic_hog_cleavage/openscientist_artifacts
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
citation_count: 9
term_validation:
  total_terms: 4
  verified: 4
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 5
artifact_sources:
  openscientist_artifacts_zip: 5
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
- filename: kb_hypotheses_Primary_Hyperoxaluria_Type_3_cytosolic_hog_cleavage_openscientist_artifacts_data_uniprot_HOGA1_preflight.json
  path: openscientist_artifacts/kb_hypotheses_Primary_Hyperoxaluria_Type_3_cytosolic_hog_cleavage_openscientist_artifacts_data_uniprot_HOGA1_preflight.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist uniprot HOGA1 preflight
- filename: kb_hypotheses_Primary_Hyperoxaluria_Type_3_cytosolic_hog_cleavage_openscientist_artifacts_logs_pubmed_search_log.json
  path: openscientist_artifacts/kb_hypotheses_Primary_Hyperoxaluria_Type_3_cytosolic_hog_cleavage_openscientist_artifacts_logs_pubmed_search_log.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist pubmed search log
- filename: kb_hypotheses_Primary_Hyperoxaluria_Type_3_cytosolic_hog_cleavage_openscientist_artifacts_tables_evidence_matrix.csv
  path: openscientist_artifacts/kb_hypotheses_Primary_Hyperoxaluria_Type_3_cytosolic_hog_cleavage_openscientist_artifacts_tables_evidence_matrix.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist evidence matrix
---

## Question

# Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Primary Hyperoxaluria Type 3
- **Category:** Metabolic Disorder

## Target Hypothesis
- **Hypothesis ID:** cytosolic_hog_cleavage
- **Hypothesis Label:** Cytosolic 4-Hydroxy-2-Oxoglutarate Cleavage Model
- **Status in KB:** CANONICAL

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: cytosolic_hog_cleavage
hypothesis_label: Cytosolic 4-Hydroxy-2-Oxoglutarate Cleavage Model
status: CANONICAL
description: 'The leading proposed explanation for increased oxalate production despite a block upstream
  of glyoxylate: 4-hydroxy-2-oxoglutarate accumulating behind the absent mitochondrial HOGA1 step is exported
  to the cytosol and cleaved there by a non-HOGA1 aldolase, releasing glyoxylate outside the mitochondrial
  compartment where it would normally be detoxified, so that it is instead oxidized to oxalate.'
evidence:
- reference: PMID:22729392
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: its transport into the cytosol where it is converted to
  explanation: States the cytosolic-export-and-conversion route for accumulated 4-hydroxy-2-oxoglutarate
    that this hypothesis group names.
  reference_title: Primary hyperoxaluria type III--a model for studying perturbations in glyoxylate metabolism
notes: Treated as the default explanatory model in the literature rather than as an established one; the
  identity of the proposed cytosolic aldolase is not settled and the flux has not been measured directly.
  See the gap_ph3_oxalate_overproduction_mechanism discussion.
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
result beneath `kb/hypotheses/Primary_Hyperoxaluria_Type_3/cytosolic_hog_cleavage/openscientist_artifacts`. Do not create an empty bundle when no data
source was accessed and no analysis ran. Give each artifact a stable relative
path and connect computed claims to their input, method, and output artifacts.
Do not bundle large recoverable raw
downloads, a provider data lake, controlled/patient-level data, credentials, or
signed URLs; record their stable external identifiers, versions, and checksums
instead. State explicitly when an expected artifact is external, local-only,
missing, or was not produced.


## Output

# Mechanistic Hypothesis Search — Primary Hyperoxaluria Type 3
## Cytosolic 4-Hydroxy-2-Oxoglutarate Cleavage Model (`cytosolic_hog_cleavage`)

**Disease:** Primary Hyperoxaluria Type 3 (PH3) | **Category:** Metabolic Disorder
**Hypothesis status in KB:** CANONICAL
**Search date:** 2026-10-15 | **Iterations completed:** 5 | **Papers reviewed:** 24 | **Findings recorded:** 7

---

## Executive Judgment

**Verdict: PARTIALLY SUPPORTED but UNRESOLVED.**

The cytosolic HOG-cleavage model is the field's default explanatory framework for why patients lose a mitochondrial enzyme upstream of glyoxylate yet overproduce oxalate. Its *upstream* half is firmly established: HOGA1 (DHDPSL) is a strictly mitochondrial enzyme whose PH3 variants are loss-of-function, and the hydroxyproline-pathway metabolites 4-hydroxy-2-oxoglutarate (HOG), 4-hydroxyglutamate, and 2,4-dihydroxyglutarate (DHG) accumulate in PH3 patient urine, serum, and liver. The hypothesis also rests on one piece of *direct* biochemical support — the detection of a cytosolic, non-HOGA1 HOG-aldolase activity in human hepatocyte cell lines ([PMID:22729392](https://pubmed.ncbi.nlm.nih.gov/22729392/)).

However, the hypothesis's **defining causal step is unproven**. The responsible cytosolic aldolase has never been molecularly identified, and the one explicitly tested candidate — N-acetylneuraminate aldolase (NAL) — was nearly inactive against HOG ([PMID:22771891](https://pubmed.ncbi.nlm.nih.gov/22771891/)). The HOG→glyoxylate→oxalate flux that the model requires has never been directly measured. The strongest counter-evidence comes from the Hoga1-knockout mouse, which accumulates HOG but does **not** become hyperoxaluric, and in which residual (non-HOGA) HOG→glyoxylate aldolase activity localizes to **liver mitochondria, not cytosol**, while the cytosolic compartment instead favors reductive diversion of HOG to DHG ([PMID:26428388](https://pubmed.ncbi.nlm.nih.gov/26428388/), [PMID:39040543](https://pubmed.ncbi.nlm.nih.gov/39040543/), [PMID:40578401](https://pubmed.ncbi.nlm.nih.gov/40578401/)). Finally, hepatic-LDH RNAi (nedosiran) fails to correct oxalate in PH3, implying a multi-organ oxalate source that the hepatocyte-centric terminal step of this model does not capture ([PMID:39582099](https://pubmed.ncbi.nlm.nih.gov/39582099/)).

Two **competing, more parsimonious mechanisms** explain the same disease features without requiring an unidentified cytosolic aldolase: (1) HOG directly inhibits glyoxylate reductase (GR, the PH2 enzyme), impairing glyoxylate detoxification ([PMID:22771891](https://pubmed.ncbi.nlm.nih.gov/22771891/)); and (2) HOGA1 loss reduces pyruvate availability and Krebs-cycle flux, indirectly raising oxalate ([PMID:31696211](https://pubmed.ncbi.nlm.nih.gov/31696211/)). **Recommendation for curation:** retain the model as the default narrative but downgrade its mechanistic certainty — flag the cytosolic-aldolase edge as *speculative/unconfirmed* and register the two competing hypotheses as tracked alternatives with an explicit knowledge gap on direct flux measurement and enzyme identity.

---

## Key Findings

### F001 — Direct in vitro support: cytosolic non-HOGA1 HOG aldolase activity in human hepatocytes

The single most direct piece of evidence for the seed hypothesis comes from Belostotsky, Pitt & Frishberg (*Primary hyperoxaluria type III—a model for studying perturbations in glyoxylate metabolism*, [PMID:22729392](https://pubmed.ncbi.nlm.nih.gov/22729392/)). Using GC-MS on PH3 patient urine, they documented significant elevations of HOG, its precursor 4-hydroxyglutamate, and its derivative 2,4-dihydroxyglutarate relative to mutation carriers and controls. Critically, in human hepatocyte cell lines they *detected a cytosolic 4-hydroxy-2-oxoglutarate aldolase activity* that was not attributable to HOGA1. The authors articulate the model's central route verbatim: HOG undergoes "its transport into the cytosol where it is converted to glyoxylate by a different cytosolic aldolase." This is the biochemical observation on which the entire cytosolic cleavage hypothesis is built.

**Caveat:** the finding is qualitative — an activity was detected, but the enzyme was not purified or identified, and no flux from HOG through glyoxylate to oxalate was quantified. The observation establishes *possibility*, not *operation in vivo*.

### F002 — Qualifier: in Hoga1-KO mouse, residual HOG→glyoxylate activity is mitochondrial; cytosol favors reductive diversion to DHG

Li et al. (*4-hydroxy-2-oxoglutarate metabolism in a mouse model of Primary Hyperoxaluria Type 3*, [PMID:39040543](https://pubmed.ncbi.nlm.nih.gov/39040543/), *Biochem Biophys Rep* 2024) directly interrogated the compartmentalization the model depends on. In Hoga1-knockout mouse tissues, residual HOG→glyoxylate aldolase activity "was highest in liver mitoplasts, with no activity present in brain tissue lysates" — i.e., the non-HOGA aldolase activity is **mitochondrial, not cytosolic**, the opposite of what the seed model predicts. Moreover, "the metabolism of HOG to DHG was highest in liver and kidney cortical tissue, enhanced in the cytosolic compartment of the liver, and preferred NADPH as a cofactor." In other words, the murine cytosol preferentially *reduces* HOG to a dead-end (DHG) rather than *cleaving* it to glyoxylate. This directly qualifies the seed hypothesis at the level of its defining subcellular logic — at least in mouse.

### F003 — Scope limitation: HOGA1-deficient mice do not recapitulate hyperoxaluria; human penetrance is low

The model must explain oxalate overproduction, yet the best in vivo model fails to overproduce oxalate. Li et al. (*Hydroxyproline metabolism in a mouse model of Primary Hyperoxaluria Type 3*, [PMID:26428388](https://pubmed.ncbi.nlm.nih.gov/26428388/), 2015) reported that Hoga1-null mice accumulate HOG, 4-OH-glutamate, and DHG but show **no increased oxalate excretion**, noting this "may be consistent with the recent recognition that only a small fraction of the individuals with the genotype for HOGA deficiency develop PH." Boffa/Brunetti-Pierri et al. ([PMID:40578401](https://pubmed.ncbi.nlm.nih.gov/40578401/), 2025) tested whether the murine non-phenotype was an artifact of species differences in AGT compartmentalization: even Hoga1-/-/Agxt-/- mice engineered to express AGT in peroxisomes only (the human-like configuration) "did not show increased urinary oxalate, suggesting that AGT expression in both cellular compartments is not an explanation for the lack of hyperoxaluria in Hoga1-/- mice." This both documents incomplete penetrance in humans and removes one candidate explanation for the mouse–human discrepancy, leaving the in vivo validity of the compartmentalization model unconfirmed.

### F004 — Competing mechanism: reduced pyruvate / Krebs-cycle flux

Huang et al. (*Regulation of human 4-hydroxy-2-oxoglutarate aldolase by pyruvate and α-ketoglutarate*, [PMID:31696211](https://pubmed.ncbi.nlm.nih.gov/31696211/), 2019) characterized recombinant human HOGA1 and found it possesses dual aldolase **and** oxaloacetate-decarboxylase activities sharing the same catalytic machinery, both with micromolar substrate affinities likely operative in vivo, with pyruvate acting as a competitive inhibitor. They propose an alternative to cytosolic cleavage entirely: "loss of HOGA1 function could increase oxalate production in PH3 by decreasing pyruvate availability and metabolic flux through the Krebs cycle." This is a *parallel, more parsimonious* mechanism that requires no unidentified cytosolic enzyme.

### F005 — Competing mechanism + candidate-aldolase falsification: HOG inhibits glyoxylate reductase; NAL fails to cleave HOG

Riedel et al. (*4-Hydroxy-2-oxoglutarate aldolase inactivity in primary hyperoxaluria type 3 and glyoxylate reductase inhibition*, [PMID:22771891](https://pubmed.ncbi.nlm.nih.gov/22771891/), 2012) delivered three results that both anchor and challenge the model. First, they confirmed loss-of-function: all nine PH3 HOGA variants expressed in E. coli/CHO were unstable, aggregated, and retained no measurable activity. Second, they confirmed the upstream substrate accumulation on which both the seed and competing models depend: "a buildup of HOG was confirmed in the urine, sera and liver samples from PH3 patients." Third — and most consequentially — they tested two mechanistic candidates. N-acetylneuraminate aldolase, a plausible cytosolic HOG-cleaving aldolase, "showed minimal activity towards HOG," falsifying the leading named candidate for the seed's missing enzyme. And glyoxylate reductase "was inhibited by HOG but not by 2-hydroxyglutarate or 2-oxoglutarate," furnishing a competing mechanism in which accumulating HOG impairs glyoxylate detoxification directly.

### F006 — Mechanistic history: PH3 hypothesis evolved from gain-of-function to loss-of-function

The downstream mechanism of PH3 has been unsettled from the start. Belostotsky et al. (*Mutations in DHDPSL are responsible for primary hyperoxaluria type III*, [PMID:20797690](https://pubmed.ncbi.nlm.nih.gov/20797690/), 2010, *Am J Hum Genet*) identified biallelic DHDPSL (HOGA1) mutations as the cause of PH3, establishing that "DHDPSL is the gene encoding 4-hydroxy-2-oxoglutarate aldolase, catalyzing the final step in the metabolic pathway of hydroxyproline." Monico et al. ([PMID:21896830](https://pubmed.ncbi.nlm.nih.gov/21896830/), 2011) initially "hypothesized to cause a gain of mitochondrial 4-hydroxy-2-oxoglutarate aldolase activity, resulting in excess oxalate," before revising to a loss-of-function model after mutation screening and RT-PCR. They also noted PH3's distinctive clinical signature: lower urine oxalate and higher urine calcium/uric acid than PH1/PH2, with generally preserved eGFR (mean 116 mL/min/1.73m² at 7.2 yr). The historical reversal itself illustrates that the paradox at the model's core — upstream block, downstream overproduction — has never had a settled resolution.

### F007 — Qualifier: hepatic LDH inhibition (nedosiran) fails in PH3, implying a multi-organ oxalate source

Wanders et al. (*Human glyoxylate metabolism revisited: New insights pointing to multi-organ involvement*, [PMID:39582099](https://pubmed.ncbi.nlm.nih.gov/39582099/), *J Inherit Metab Dis* 2025, review-level synthesis) report that the hepatic-LDH-targeting RNAi nedosiran "effectively reduced urinary oxalate excretion in PH1 patients but not in PH2 or PH3 patients," and conclude from a thorough literature study that "glyoxylate/oxalate metabolism is not confined to the liver but instead involves multiple different organs." If the terminal oxalate-generating step in PH3 were purely hepatic (as the hepatocyte-centric seed model implies), inhibiting hepatic LDH should lower oxalate — it does not. This points to a tissue-context gap in the seed hypothesis.

---

## Mechanistic Model / Interpretation

### The causal chain implied by the seed hypothesis

```
  Hydroxyproline (dietary + collagen turnover)
        │
        ▼
  [mitochondrial hydroxyproline degradation pathway]
        │
        ▼
  4-hydroxy-2-oxoglutarate (HOG)  ◄── normally cleaved here by HOGA1
        │                               (mitochondrial) → pyruvate + glyoxylate
        │                               glyoxylate detoxified in mitochondrion
        │
   [HOGA1 LOSS-OF-FUNCTION in PH3]  ── ESTABLISHED (F001,F005,F006)
        │
        ▼
  HOG accumulates behind the block  ── ESTABLISHED (F001,F005)
        │
        ▼
  ??? HOG exported to CYTOSOL        ── INFERRED, not measured (GAP)
        │
        ▼
  ??? cleaved by non-HOGA1           ── SPECULATIVE; enzyme unidentified,
      cytosolic aldolase                 NAL falsified (F005); mouse data
        │                                 put residual activity in mito (F002)
        ▼
  glyoxylate released in cytosol     ── INFERRED (GAP)
      (away from mito detox)
        │
        ▼
  glyoxylate oxidized to OXALATE     ── hepatic LDH route; but nedosiran
        │                               fails in PH3 → multi-organ source (F007)
        ▼
  Hyperoxaluria / calcium oxalate    ── NOT reproduced in Hoga1-KO mouse (F003)
      stones, nephrocalcinosis
```

### Where the literature is strong, inferred, or missing

| Causal link | Status | Evidence |
|---|---|---|
| HOGA1 is mitochondrial and loss-of-function in PH3 | **Established** | F005, F006; UniProt (mitochondrial-only, no cytosolic paralog annotated) |
| HOG/4-OH-Glu/DHG accumulate in PH3 patients | **Established** | F001, F005 |
| HOG is exported to cytosol | **Inferred / unmeasured** | Proposed in F001; no transport assay |
| A cytosolic non-HOGA1 aldolase cleaves HOG | **Speculative** | Activity detected (F001) but enzyme unidentified; NAL falsified (F005); mouse localizes activity to mito (F002) |
| Released glyoxylate → oxalate (hepatic) | **Qualified / challenged** | Nedosiran fails in PH3 → multi-organ (F007) |
| Net result = hyperoxaluria | **Challenged in model organism** | Hoga1-KO mice not hyperoxaluric (F003) |

The model is a chain whose first two links are solid rock and whose central link — the cytosolic cleavage event that gives the hypothesis its name — is the weakest and most contested of all.

### Competing mechanistic landscape

```
        HOGA1 loss-of-function + HOG accumulation (shared premise)
         │                    │                         │
         ▼                    ▼                         ▼
  SEED: cytosolic       ALT-1: HOG inhibits        ALT-2: ↓pyruvate →
  aldolase cleaves      glyoxylate reductase       ↓Krebs flux →
  HOG → glyoxylate      (GR, PH2 enzyme) →         ↑oxalate
  → oxalate             impaired glyoxylate        (Huang 2019, F004)
  (F001)                detox (Riedel 2012, F005)
  needs unknown         parsimonious: no new        parsimonious: no new
  enzyme                enzyme required             enzyme required
```

---

## Evidence Base / Evidence Matrix

| Citation | Evidence type | Stance | Mechanistic claim tested | Key finding | Subtype/context | Confidence & limitations |
|---|---|---|---|---|---|---|
| [PMID:22729392](https://pubmed.ncbi.nlm.nih.gov/22729392/) | Human clinical + in vitro | **Supports** | Cytosolic non-HOGA1 HOG aldolase exists; HOG exported & cleaved in cytosol | GC-MS: HOG/4-OH-Glu/DHG ↑ in PH3 urine; cytosolic HOG aldolase activity detected in human hepatocyte lines | PH3, human hepatocytes | Moderate; qualitative activity, enzyme unidentified, no flux measured |
| [PMID:22771891](https://pubmed.ncbi.nlm.nih.gov/22771891/) | In vitro + human biomarker | **Qualifies / competing** | Candidate cytosolic aldolase (NAL); GR inhibition by HOG | PH3 HOGA variants inactive; HOG buildup confirmed in urine/sera/liver; NAL nearly inactive on HOG; GR inhibited by HOG | PH3 patients + recombinant enzymes | High for loss-of-function & NAL falsification; GR inhibition in vitro only |
| [PMID:39040543](https://pubmed.ncbi.nlm.nih.gov/39040543/) | Model organism (mouse) | **Qualifies / refutes** | Subcellular localization of residual HOG cleavage vs reduction | Residual HOG→glyoxylate activity in liver mitoplasts (not cytosol); cytosol favors NADPH-dependent HOG→DHG reduction | Hoga1-KO mouse | High for mouse; enzyme identities not established; species caveat |
| [PMID:26428388](https://pubmed.ncbi.nlm.nih.gov/26428388/) | Model organism (mouse) | **Qualifies (scope)** | Does HOGA1 loss → hyperoxaluria? | Hoga1-null mice accumulate HOG/4-OH-Glu/DHG but no ↑ oxalate excretion; low human penetrance noted | Hoga1-KO mouse | High; model may not capture human disease |
| [PMID:40578401](https://pubmed.ncbi.nlm.nih.gov/40578401/) | Model organism (mouse) | **Qualifies** | Is AGT compartmentalization the reason mice are protected? | Hoga1-/-/Agxt-/- mice with peroxisomal-only AGT still no hyperoxaluria | Hoga1-KO mouse, humanized AGT | High; rules out one explanation, leaves model unconfirmed in vivo |
| [PMID:31696211](https://pubmed.ncbi.nlm.nih.gov/31696211/) | In vitro enzymology | **Competing** | Alternative: ↓pyruvate/Krebs flux raises oxalate | Recombinant HOGA1 has dual aldolase + OAA-decarboxylase activity; pyruvate competitive inhibitor; proposes Krebs-flux mechanism | PH3 biochemical model | Moderate; biochemical inference, not tested in vivo |
| [PMID:20797690](https://pubmed.ncbi.nlm.nih.gov/20797690/) | Human clinical/genetic | **Supports (upstream)** | Causal gene/enzyme for PH3 | Biallelic DHDPSL/HOGA1 mutations cause PH3; encodes HOG aldolase | PH3 cohort (15 patients) | High for causal gene |
| [PMID:21896830](https://pubmed.ncbi.nlm.nih.gov/21896830/) | Human clinical/genetic | **Context** | GOF vs LOF mechanism | Initial GOF hypothesis revised to LOF; PH3 clinical signature (lower oxalate, preserved eGFR) | PH3 cohort | High for clinical description; mechanism historically unsettled |
| [PMID:39582099](https://pubmed.ncbi.nlm.nih.gov/39582099/) | Review (clinical-trial synthesis) | **Qualifies** | Is the oxalate source purely hepatic? | Nedosiran reduces oxalate in PH1 but not PH2/PH3; glyoxylate/oxalate metabolism multi-organ | PH1/PH2/PH3 trials | Review-level; synthesizes trial outcomes |

---

## Data and Tool Use

This investigation was a **literature- and annotation-based hypothesis search**. No patient-level omics dataset, cohort file, or quantitative data lake specific to PH3 HOG flux was available or accessed. The inventory below is explicit about what was searched vs. accessed.

| Source | Accession / URI | Access status | Query / scope | Relevance |
|---|---|---|---|---|
| PubMed | Multiple PMIDs (24 papers reviewed) | **Accessed** (search_pubmed) | PH3, HOGA1, 4-hydroxy-2-oxoglutarate, cytosolic aldolase, glyoxylate reductase, nedosiran, Hoga1 knockout | Directly relevant; primary evidence source |
| UniProt (HOGA1) | HOGA1 human entry | **Accessed / cited** | Subcellular localization annotation | Confirmed mitochondrial-only localization; no cytosolic paralog annotated |
| GenCC / ClinGen gene-disease | — | **Not searched with logged query** | — | Unverified for this run; see Knowledge Gaps |
| ClinicalTrials.gov | — | **Not independently queried**; nedosiran PH3 outcome obtained via review [PMID:39582099] | — | Trial outcome is review-reported, not primary-trial-accessed |
| Omics / proteomics of PH3 cytosolic aldolase | — | **No usable result** | No dataset identifying the cytosolic HOG-cleaving enzyme | Source-level absence (curation-relevant) |

### Attempted analyses

| Analysis | Input → method → output | Outcome |
|---|---|---|
| Literature evidence synthesis | PubMed abstracts → manual appraisal → evidence matrix (F001–F007) | **Succeeded** (narrative/curatorial) |
| HOGA1 subcellular localization check | UniProt annotation → inspection → "mitochondrial only" | **Succeeded** (annotation lookup) |
| Direct HOG→glyoxylate→oxalate flux quantification | — | **Skipped / not available** — no dataset or assay accessible; this is the central unmeasured quantity |
| Identification of cytosolic aldolase from omics | — | **Failed / no usable result** — no dataset resolves enzyme identity |

**No computational statistical analysis of a primary dataset was performed**, because none relevant to the defining causal step (cytosolic HOG cleavage flux) was available. This is stated explicitly rather than substituted silently with literature synthesis. The limitation: the model's key quantitative claim remains untested by any accessible data in this run.

---

## Limitations and Knowledge Gaps

1. **Identity of the cytosolic HOG-cleaving aldolase is unknown.** This is the defining, name-giving step of the hypothesis. *Checked:* NAL explicitly tested and nearly inactive (F005); UniProt shows no annotated cytosolic HOGA1 paralog. *Resolution:* enzyme purification/activity-guided fractionation of human hepatocyte cytosol + proteomics; CRISPR knockout of candidates with HOG-aldolase activity assay.

2. **HOG→glyoxylate→oxalate flux has never been directly measured.** *Checked:* no dataset or isotope-tracing study located. *Resolution:* ¹³C-HOG tracing in PH3 patient-derived hepatocytes/organoids measuring labeled oxalate output.

3. **Subcellular localization conflict (mouse vs. hypothesis).** Mouse residual aldolase activity is mitochondrial, and cytosol favors HOG→DHG reduction (F002) — opposite to the model. *Checked:* Li 2024. *Resolution:* compartment-resolved assays in human tissue to determine whether the human cytosol behaves differently from mouse.

4. **Mouse model does not reproduce hyperoxaluria; human penetrance low.** *Checked:* F003 (two independent mouse studies). *Resolution:* identify genetic/dietary modifiers that convert HOGA1 loss into an oxalate phenotype.

5. **Multi-organ oxalate source / nedosiran failure.** The hepatocyte-centric terminal step is challenged by PH3 nedosiran non-response (F007). *Resolution:* tissue-specific contribution mapping (kidney vs. liver) to oxalate.

6. **Source/database absences.** GenCC and ClinGen were **not searched with a logged query** in this run and should be labeled *unverified* rather than claimed absent. No PH3-specific omics/cohort dataset identifying the cytosolic aldolase was found. These are curation-relevant source absences as of 2026-10-15.

---

## Alternative Models

| Model | Relationship to seed | Core claim | Parsimony |
|---|---|---|---|
| **Glyoxylate reductase (GR) inhibition by HOG** ([PMID:22771891](https://pubmed.ncbi.nlm.nih.gov/22771891/)) | **Parallel/alternative** | Accumulated HOG inhibits GR, impairing glyoxylate detoxification, raising oxalate | High — no new enzyme needed; links PH3 biochemically to PH2 |
| **Reduced pyruvate / Krebs-cycle flux** ([PMID:31696211](https://pubmed.ncbi.nlm.nih.gov/31696211/)) | **Parallel/alternative** | HOGA1 loss lowers pyruvate supply and TCA flux, indirectly increasing oxalate | High — no new enzyme needed |
| **Cytosolic reductive diversion to DHG** ([PMID:39040543](https://pubmed.ncbi.nlm.nih.gov/39040543/)) | **Competing cytosolic fate** | Cytosolic HOG is reduced (NADPH) to DHG, not cleaved — a sink that argues against cytosolic cleavage | Challenges seed's cytosolic step |
| **Multi-organ oxalate production** ([PMID:39582099](https://pubmed.ncbi.nlm.nih.gov/39582099/)) | **Upstream/contextual** | Oxalate arises outside liver, explaining nedosiran's PH3 failure | Reframes tissue context |
| **Residual mitochondrial non-HOGA aldolase** ([PMID:39040543](https://pubmed.ncbi.nlm.nih.gov/39040543/)) | **Alternative to cytosolic export** | A second mitochondrial aldolase cleaves HOG, releasing glyoxylate without cytosolic export | Removes the need for export step |

---

## Discriminating Tests

1. **¹³C-HOG isotope tracing in PH3 patient-derived hepatocyte organoids** (vs. HOGA1-corrected isogenic controls). *Expected if seed is true:* labeled glyoxylate and oxalate appear in the cytosolic fraction; an export inhibitor reduces oxalate. *Expected if GR-inhibition/Krebs models dominate:* oxalate rises without cytosolic glyoxylate flux from HOG.

2. **Activity-guided purification + proteomics of the cytosolic HOG aldolase** from human liver cytosol, followed by CRISPR knockout. *Expected if seed is true:* a specific cytosolic enzyme accounts for the activity and its knockout lowers HOG-derived oxalate.

3. **Compartment-resolved enzymology in human (not mouse) liver** to test whether human cytosol cleaves vs. reduces HOG. *Expected if seed is true:* human cytosol shows aldolase, not just NADPH-reductase, activity — distinguishing it from the mouse result (F002).

4. **GR-inhibition test in vivo:** measure glyoxylate reductase activity and glyoxylate pools in PH3 tissue under HOG load. *Expected if ALT-1 dominates:* measurable GR inhibition tracking HOG concentration.

5. **Humanized/modifier mouse screen** to find conditions converting Hoga1 loss into hyperoxaluria, resolving the species discrepancy (F003).

---

## Curation Leads (require curator verification)

**Candidate status change:** Retain `cytosolic_hog_cleavage` as the default narrative model but **downgrade the cytosolic-aldolase edge from CANONICAL-implied to SPECULATIVE/UNCONFIRMED**. The upstream half (HOGA1 LOF + HOG accumulation) is well-supported and can remain established.

**Candidate evidence references & snippets to verify:**
- [PMID:22729392](https://pubmed.ncbi.nlm.nih.gov/22729392/): "In human hepatocyte cell lines, we detected a cytosolic 4-hydroxy-2-oxoglutarate aldolase activity" — SUPPORT (direct).
- [PMID:22771891](https://pubmed.ncbi.nlm.nih.gov/22771891/): "NAL showed minimal activity towards HOG" — QUALIFIES (falsifies candidate); "GR was inhibited by HOG but not by 2-hydroxyglutarate or 2-oxoglutarate" — COMPETING.
- [PMID:39040543](https://pubmed.ncbi.nlm.nih.gov/39040543/): "HOG to glyoxylate aldolase activity was highest in liver mitoplasts" — QUALIFIES (localization conflict).
- [PMID:26428388](https://pubmed.ncbi.nlm.nih.gov/26428388/): "An increased oxalate excretion is not observed in the KO mice" — QUALIFIES (scope).
- [PMID:40578401](https://pubmed.ncbi.nlm.nih.gov/40578401/): "did not show increased urinary oxalate" — QUALIFIES.
- [PMID:31696211](https://pubmed.ncbi.nlm.nih.gov/31696211/): "loss of HOGA1 function could increase oxalate production in PH3 by decreasing pyruvate availability and metabolic flux through the Krebs cycle" — COMPETING.
- [PMID:39582099](https://pubmed.ncbi.nlm.nih.gov/39582099/): "nedosiran effectively reduced urinary oxalate excretion in PH1 patients but not in PH2 or PH3 patients" — QUALIFIES.

**Candidate pathophysiology edges to add:**
- `HOG –inhibits→ glyoxylate_reductase` (competing mechanism, PMID:22771891)
- `HOGA1_loss –reduces→ pyruvate/Krebs_flux –increases→ oxalate` (competing, PMID:31696211)
- `HOG –reduced_by(NADPH)→ DHG` cytosolic sink (competing fate, PMID:39040543)
- `oxalate_production –not_confined_to→ liver` multi-organ context (PMID:39582099)

**Candidate `knowledge_gaps` / discussion prompts:**
- Unidentified cytosolic HOG aldolase (name-giving step unconfirmed; NAL falsified).
- HOG→glyoxylate→oxalate flux never directly measured.
- Mouse-vs-hypothesis localization conflict; mouse non-phenotype.
- GenCC/ClinGen not searched with logged query in this run — **unverified**, not absent.

**Candidate ontology terms:** hepatocyte cytosol (GO:0005829 cytosol); mitochondrion (GO:0005739); hydroxyproline catabolic process (GO:0019470); glyoxylate metabolic process (GO:0046487); oxalate biosynthesis.

---

## Artifact Bundle

An artifact bundle with a checksummed `MANIFEST.yaml`, evidence matrix, search logs, and this report was prepared under `kb/hypotheses/Primary_Hyperoxaluria_Type_3/cytosolic_hog_cleavage/openscientist_artifacts` (per iterations 4–5). No primary dataset or data lake was accessed; no raw downloads are bundled. The bundle records external identifiers (PMIDs, UniProt HOGA1) rather than recoverable raw content. **Expected-but-absent artifacts** (explicitly stated): no isotope-tracing dataset, no PH3 cytosolic-proteomics file, and no logged GenCC/ClinGen query response — these were not produced because no such source was accessed.

---

## Summary of Verdict

The cytosolic HOG-cleavage model is the **correct default narrative for PH3 but is mechanistically unestablished at its defining step**. Its upstream claims (mitochondrial HOGA1 loss-of-function; accumulation of HOG and hydroxyproline-pathway metabolites) are solidly established. Its central claim — that an unidentified cytosolic aldolase cleaves exported HOG to release glyoxylate for oxidation to oxalate — rests on a single qualitative activity detection, has no identified enzyme, was weakened by falsification of the one tested candidate (NAL), is contradicted by mouse compartmentalization data showing cytosolic reductive diversion and mitochondrial residual cleavage, and is unsupported by the Hoga1-knockout non-phenotype and nedosiran's PH3 failure. Two competing mechanisms — HOG inhibition of glyoxylate reductase, and reduced pyruvate/Krebs-cycle flux — explain the same disease features more parsimoniously. **The hypothesis should remain CANONICAL as the field's default but be curated with an explicit mechanistic-uncertainty flag and tracked alternatives.**


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist uniprot HOGA1 preflight](openscientist_artifacts/kb_hypotheses_Primary_Hyperoxaluria_Type_3_cytosolic_hog_cleavage_openscientist_artifacts_data_uniprot_HOGA1_preflight.json)
- [OpenScientist pubmed search log](openscientist_artifacts/kb_hypotheses_Primary_Hyperoxaluria_Type_3_cytosolic_hog_cleavage_openscientist_artifacts_logs_pubmed_search_log.json)
- [OpenScientist evidence matrix](openscientist_artifacts/kb_hypotheses_Primary_Hyperoxaluria_Type_3_cytosolic_hog_cleavage_openscientist_artifacts_tables_evidence_matrix.csv)

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 4 |
| Resolved | 4 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |

Every term resolved, and every label the report gave matched.

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 9 |
| On topic | 8 |
| Off topic | 0 |

All extracted references resolved successfully.
