---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-07T00:43:14.419461'
end_time: '2026-10-07T01:05:45.358047'
duration_seconds: 1350.94
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: Metabolic Dysfunction-Associated Steatotic Liver Disease
  category: Complex
  hypothesis_group_id: hepatic_fatty_acid_uptake_masld
  hypothesis_label: Transporter-mediated hepatic fatty acid uptake as a rate-limiting,
    druggable step
  hypothesis_status: EMERGING
  hypothesis_yaml: "hypothesis_group_id: hepatic_fatty_acid_uptake_masld\nhypothesis_label:\
    \ Transporter-mediated hepatic fatty acid uptake as a rate-limiting, druggable\
    \ step\nstatus: EMERGING\ndescription: 'The canonical model treats the hepatocyte\
    \ as a passive sink for the non-esterified fatty\n  acid load that adipose insulin\
    \ resistance releases. This hypothesis holds instead that entry into the\n  hepatocyte\
    \ is itself protein-mediated and rate-limiting, so that the fatty acid transport\
    \ proteins on\n  the basolateral hepatocyte membrane \u2014 FATP5 (SLC27A5), which\
    \ is expressed exclusively by liver, and\n  FATP2 (SLC27A2) \u2014 set how much\
    \ of that load actually reaches the hepatic lipid pool, and blocking them\n  reverses\
    \ steatosis that is already established. The strong form of the claim is therapeutic:\
    \ hepatic\n  fatty acid uptake is a target in its own right, upstream of and separable\
    \ from the lipogenic and oxidative\n  arms the approved agents act on. It is modeled\
    \ as EMERGING, not canonical, for two reasons the curated\n  evidence states directly.\
    \ First, every causal experiment is murine knockdown or knockout; no FATP-directed\n\
    \  agent has been tested in human MASLD, and no human genetic evidence linking\
    \ SLC27A5 or SLC27A2 variation\n  to MASLD is curated here. Second, hepatic FATP5\
    \ knockdown also reduced whole-animal caloric uptake,\n  so the reported protection\
    \ is not cleanly attributable to the hepatic uptake step alone \u2014 a confound\n\
    \  the source paper reports rather than one imputed to it. A curator strengthening\
    \ this arm should look\n  for the human evidence that is missing, not for more\
    \ rodent replication.'\nevidence:\n- reference: PMID:16618416\n  reference_title:\
    \ 'Targeted deletion of FATP5 reveals multiple functions in liver metabolism:\
    \ alterations\n    in hepatic lipid homeostasis.'\n  supports: SUPPORT\n  evidence_source:\
    \ MODEL_ORGANISM\n  snippet: Our findings support the hypothesis that efficient\
    \ hepatocellular uptake of LCFAs, and thus\n    liver lipid homeostasis in general,\
    \ is largely a protein-mediated process requiring FATP5.\n  explanation: States\
    \ the core premise of this hypothesis \u2014 that hepatocellular long-chain fatty\
    \ acid\n    entry is protein-mediated rather than passive \u2014 from a whole-animal\
    \ knockout.\n- reference: PMID:18524776\n  reference_title: Silencing of hepatic\
    \ fatty acid transporter protein 5 in vivo reverses diet-induced\n    non-alcoholic\
    \ fatty liver disease and improves hyperglycemia.\n  supports: SUPPORT\n  evidence_source:\
    \ MODEL_ORGANISM\n  snippet: knockdown of fatty acid transport protein 5 was also\
    \ able to reverse already established non-alcoholic\n    fatty liver disease,\
    \ resulting in significantly improved whole-body glucose homeostasis.\n  explanation:\
    \ Supplies the therapeutic form of the claim \u2014 reversal of established disease,\
    \ not just\n    prevention \u2014 which is what makes the uptake step worth modeling\
    \ separately from lipid overload. Murine,\n    which is why the hypothesis stays\
    \ emerging.\n- reference: PMID:18524776\n  reference_title: Silencing of hepatic\
    \ fatty acid transporter protein 5 in vivo reverses diet-induced\n    non-alcoholic\
    \ fatty liver disease and improves hyperglycemia.\n  supports: SUPPORT\n  directness:\
    \ INDIRECT\n  evidence_source: MODEL_ORGANISM\n  snippet: resulting in a marked\
    \ reduction of hepatic dietary fatty acid uptake, reduced caloric uptake,\n  \
    \  and concomitant protection from diet-induced non-alcoholic fatty liver disease.\n\
    \  explanation: 'Retained deliberately as the bounding quote: the same sentence\
    \ that reports protection\n    also reports reduced caloric uptake, so the hepatic\
    \ effect is confounded with a whole-animal energy-intake\n    effect. Graded INDIRECT\
    \ because the protection follows from the uptake block only through that unresolved\n\
    \    intermediate.'"
  artifact_dir: kb/hypotheses/Metabolic_Dysfunction-Associated_Steatotic_Liver_Disease/hepatic_fatty_acid_uptake_masld/openscientist_artifacts
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
- filename: kb_hypotheses_Metabolic_Dysfunction-Associated_Steatotic_Liver_Disease_hepatic_fatty_acid_uptake_masld_openscientist_artifacts_data_gtex_v8_transporter_tissue_expression.json
  path: openscientist_artifacts/kb_hypotheses_Metabolic_Dysfunction-Associated_Steatotic_Liver_Disease_hepatic_fatty_acid_uptake_masld_openscientist_artifacts_data_gtex_v8_transporter_tissue_expression.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist gtex v8 transporter tissue expression
- filename: kb_hypotheses_Metabolic_Dysfunction-Associated_Steatotic_Liver_Disease_hepatic_fatty_acid_uptake_masld_openscientist_artifacts_data_opentargets_transporter_masld_associations.json
  path: openscientist_artifacts/kb_hypotheses_Metabolic_Dysfunction-Associated_Steatotic_Liver_Disease_hepatic_fatty_acid_uptake_masld_openscientist_artifacts_data_opentargets_transporter_masld_associations.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist opentargets transporter masld associations
- filename: kb_hypotheses_Metabolic_Dysfunction-Associated_Steatotic_Liver_Disease_hepatic_fatty_acid_uptake_masld_openscientist_artifacts_environment.json
  path: openscientist_artifacts/kb_hypotheses_Metabolic_Dysfunction-Associated_Steatotic_Liver_Disease_hepatic_fatty_acid_uptake_masld_openscientist_artifacts_environment.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist environment
- filename: kb_hypotheses_Metabolic_Dysfunction-Associated_Steatotic_Liver_Disease_hepatic_fatty_acid_uptake_masld_openscientist_artifacts_logs_clinicaltrials_search_log.json
  path: openscientist_artifacts/kb_hypotheses_Metabolic_Dysfunction-Associated_Steatotic_Liver_Disease_hepatic_fatty_acid_uptake_masld_openscientist_artifacts_logs_clinicaltrials_search_log.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist clinicaltrials search log
- filename: kb_hypotheses_Metabolic_Dysfunction-Associated_Steatotic_Liver_Disease_hepatic_fatty_acid_uptake_masld_openscientist_artifacts_logs_gwas_catalog_check_log.json
  path: openscientist_artifacts/kb_hypotheses_Metabolic_Dysfunction-Associated_Steatotic_Liver_Disease_hepatic_fatty_acid_uptake_masld_openscientist_artifacts_logs_gwas_catalog_check_log.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist gwas catalog check log
---

## Question

# Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Metabolic Dysfunction-Associated Steatotic Liver Disease
- **Category:** Complex

## Target Hypothesis
- **Hypothesis ID:** hepatic_fatty_acid_uptake_masld
- **Hypothesis Label:** Transporter-mediated hepatic fatty acid uptake as a rate-limiting, druggable step
- **Status in KB:** EMERGING

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: hepatic_fatty_acid_uptake_masld
hypothesis_label: Transporter-mediated hepatic fatty acid uptake as a rate-limiting, druggable step
status: EMERGING
description: 'The canonical model treats the hepatocyte as a passive sink for the non-esterified fatty
  acid load that adipose insulin resistance releases. This hypothesis holds instead that entry into the
  hepatocyte is itself protein-mediated and rate-limiting, so that the fatty acid transport proteins on
  the basolateral hepatocyte membrane — FATP5 (SLC27A5), which is expressed exclusively by liver, and
  FATP2 (SLC27A2) — set how much of that load actually reaches the hepatic lipid pool, and blocking them
  reverses steatosis that is already established. The strong form of the claim is therapeutic: hepatic
  fatty acid uptake is a target in its own right, upstream of and separable from the lipogenic and oxidative
  arms the approved agents act on. It is modeled as EMERGING, not canonical, for two reasons the curated
  evidence states directly. First, every causal experiment is murine knockdown or knockout; no FATP-directed
  agent has been tested in human MASLD, and no human genetic evidence linking SLC27A5 or SLC27A2 variation
  to MASLD is curated here. Second, hepatic FATP5 knockdown also reduced whole-animal caloric uptake,
  so the reported protection is not cleanly attributable to the hepatic uptake step alone — a confound
  the source paper reports rather than one imputed to it. A curator strengthening this arm should look
  for the human evidence that is missing, not for more rodent replication.'
evidence:
- reference: PMID:16618416
  reference_title: 'Targeted deletion of FATP5 reveals multiple functions in liver metabolism: alterations
    in hepatic lipid homeostasis.'
  supports: SUPPORT
  evidence_source: MODEL_ORGANISM
  snippet: Our findings support the hypothesis that efficient hepatocellular uptake of LCFAs, and thus
    liver lipid homeostasis in general, is largely a protein-mediated process requiring FATP5.
  explanation: States the core premise of this hypothesis — that hepatocellular long-chain fatty acid
    entry is protein-mediated rather than passive — from a whole-animal knockout.
- reference: PMID:18524776
  reference_title: Silencing of hepatic fatty acid transporter protein 5 in vivo reverses diet-induced
    non-alcoholic fatty liver disease and improves hyperglycemia.
  supports: SUPPORT
  evidence_source: MODEL_ORGANISM
  snippet: knockdown of fatty acid transport protein 5 was also able to reverse already established non-alcoholic
    fatty liver disease, resulting in significantly improved whole-body glucose homeostasis.
  explanation: Supplies the therapeutic form of the claim — reversal of established disease, not just
    prevention — which is what makes the uptake step worth modeling separately from lipid overload. Murine,
    which is why the hypothesis stays emerging.
- reference: PMID:18524776
  reference_title: Silencing of hepatic fatty acid transporter protein 5 in vivo reverses diet-induced
    non-alcoholic fatty liver disease and improves hyperglycemia.
  supports: SUPPORT
  directness: INDIRECT
  evidence_source: MODEL_ORGANISM
  snippet: resulting in a marked reduction of hepatic dietary fatty acid uptake, reduced caloric uptake,
    and concomitant protection from diet-induced non-alcoholic fatty liver disease.
  explanation: 'Retained deliberately as the bounding quote: the same sentence that reports protection
    also reports reduced caloric uptake, so the hepatic effect is confounded with a whole-animal energy-intake
    effect. Graded INDIRECT because the protection follows from the uptake block only through that unresolved
    intermediate.'
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
result beneath `kb/hypotheses/Metabolic_Dysfunction-Associated_Steatotic_Liver_Disease/hepatic_fatty_acid_uptake_masld/openscientist_artifacts`. Do not create an empty bundle when no data
source was accessed and no analysis ran. Give each artifact a stable relative
path and connect computed claims to their input, method, and output artifacts.
Do not bundle large recoverable raw
downloads, a provider data lake, controlled/patient-level data, credentials, or
signed URLs; record their stable external identifiers, versions, and checksums
instead. State explicitly when an expected artifact is external, local-only,
missing, or was not produced.


## Output

# Mechanistic Hypothesis Search — Transporter-Mediated Hepatic Fatty-Acid Uptake in MASLD

**Hypothesis ID:** `hepatic_fatty_acid_uptake_masld`
**Hypothesis label:** Transporter-mediated hepatic fatty acid uptake as a rate-limiting, druggable step
**Disease:** Metabolic Dysfunction-Associated Steatotic Liver Disease (MASLD), category: Complex
**KB status entering review:** EMERGING
**Search date:** 2026-10-07

---

## Executive Judgment

**Verdict: PARTIALLY SUPPORTED — retain EMERGING.**

The hypothesis decomposes into a general claim and a strong, specific claim, and the evidence splits cleanly along that seam. The **general claim** — that entry of long-chain fatty acids (LCFAs) into the hepatocyte is a protein-mediated process and that uptake of circulating non-esterified fatty acids (NEFAs) is quantitatively the dominant source of hepatic triglyceride in human MASLD — is **well supported**. Human stable-isotope flux data attribute ~59% of hepatic triglyceride to serum NEFA uptake (Donnelly 2005, [PMID: 15864352](https://pubmed.ncbi.nlm.nih.gov/15864352/)), and whole-animal knockout work establishes that hepatocellular LCFA uptake requires a transport protein rather than passive diffusion (Doege/Stahl, [PMID: 16618416](https://pubmed.ncbi.nlm.nih.gov/16618416/)).

The **strong, specific claim** — that **FATP5 (SLC27A5) and FATP2 (SLC27A2)** are the *rate-limiting setters* of this flux and are a *druggable target in their own right*, separable from the lipogenic and oxidative arms on which approved agents act, and that blocking them *reverses established human steatosis* — is **not supported by human evidence and is confounded in the rodent evidence**. Every causal experiment in the curated and newly retrieved literature is murine knockdown or knockout. Two independent confounds prevent clean attribution of the protection to the hepatic-uptake step: (1) FATP5 is also the hepatic **bile-acid-CoA ligase** required for bile-acid amidation ([PMID: 25061560](https://pubmed.ncbi.nlm.nih.gov/25061560/); dual function restated in [PMID: 40840619](https://pubmed.ncbi.nlm.nih.gov/40840619/)), so knockdown perturbs bile-acid metabolism as well as fatty-acid entry; and (2) hepatic FATP5 knockdown also reduced whole-animal caloric uptake ([PMID: 18524776](https://pubmed.ncbi.nlm.nih.gov/18524776/)), confounding the hepatic effect with systemic energy intake — a limitation the source paper reports itself.

Two documented database checks on the search date confirm the human gaps the seed YAML anticipated. **Open Targets Platform v4** shows *no* `genetic_association` datatype score linking SLC27A5, SLC27A2, or CD36 to any MASLD-relevant term — only text-mining ("literature") scores exist. **ClinicalTrials.gov API v2** returns *zero* trials of any FATP5/FATP2-directed agent (including the FATP2 inhibitor lipofermata) in MASLD/NASH. Meanwhile, the strongest *human* transporter-uptake signal and the best-defined *druggable* uptake mechanism both center on **CD36**, not the FATPs — making CD36 the leading competing hypothesis for the same disease feature. The hypothesis is therefore correctly modeled as EMERGING, and the curator guidance in the seed ("look for the human evidence that is missing, not for more rodent replication") is validated: the missing pieces are human genetics and uptake-selective, FATP-directed human interventional evidence.

---

## Key Findings

### F001 — No human genetic evidence links FATP5/FATP2 (or CD36) to MASLD; FATP5's human liver footprint is cholestatic

A programmatic query of the **Open Targets Platform v4 GraphQL API** (retrieved 2026-10-07) for `target.associatedDiseases` of SLC27A5 (ENSG00000083807), SLC27A2 (ENSG00000140284), and CD36 (ENSG00000135218) found that, for every MASLD-relevant term — non-alcoholic fatty liver (EFO_1001248), MASH (MONDO_0007027), steatosis (EFO_0008527), and fatty liver disease (MONDO_0004790) — the **only non-zero datatype score was `literature` (text-mining)**. No `genetic_association` datatype score was present for any of the three genes against any MASLD term. The literature scores (CD36 0.51–0.89 vs SLC27A5 0.12–0.31 and SLC27A2 0.02–0.32) reflect text-mining prominence, not human genetics; CD36's apparently higher association is a publication-volume artifact. Notably, SLC27A5's top-ranked *human* liver-disease associations are **cholestatic/bile-acid phenotypes** (hepatic fibrosis 0.075, progressive familial intrahepatic cholestasis 0.050, intrahepatic cholestasis 0.048), consistent with its bile-acid-CoA ligase function rather than a steatotic one. This is the single most important negative result for the strong form of the hypothesis: the human genetic edge SLC27A5/SLC27A2 → MASLD is absent as of the search date.

### F002 — Hepatic NEFA uptake is the single largest source of hepatic triglyceride in human NAFLD (~59%)

Donnelly et al. 2005 ([PMID: 15864352](https://pubmed.ncbi.nlm.nih.gov/15864352/)), a stable-isotope flux study in 9 biopsy-confirmed NAFLD patients, partitioned the sources of hepatic triacylglycerol: **"Of the TAG accounted for in liver, 59.0% +/- 9.9% of TAG arose from NEFAs; 26.1% +/- 6.7%, from DNL; and 14.9% +/- 7.0%, from the diet."** This human in vivo quantification establishes that the fatty-acid-uptake arm is quantitatively *dominant* over de novo lipogenesis and dietary chylomicron delivery. It supports the hypothesis's premise that uptake is a major contributor to steatosis — but it measures flux, not transporter rate-limitation, and does not implicate any specific FATP. It is equally consistent with a CD36-mediated or a passive-plus-protein mixed model.

### F003 — CD36 (not FATP5/FATP2) carries the strongest human transporter-uptake evidence — a competing hypothesis

Miquilena-Colina et al. 2011 ([PMID: 21270117](https://pubmed.ncbi.nlm.nih.gov/21270117/)) found in human liver biopsies that hepatic FAT/CD36 mRNA and protein were significantly elevated in steatosis (n=34) and NASH (n=30) vs normal liver (n=32), with CD36 **redistributed to the hepatocyte plasma membrane** — **"In contrast to NL, FAT/CD36 was predominantly located at the plasma membrane of hepatocytes in patients with NAFLD and HCV G1 with steatosis"** — and correlated with insulin resistance, hyperinsulinaemia, and steatosis. This is reinforced by human mechanistic work showing O-GlcNAcylation increases CD36 expression, membrane localization, and fatty-acid uptake in NASH-patient liver ([PMID: 38642829](https://pubmed.ncbi.nlm.nih.gov/38642829/)), and by a quantified human competing route via upregulated intestinal palmitic-acid absorption transporters in NASH ([PMID: 28062946](https://pubmed.ncbi.nlm.nih.gov/28062946/)). The human evidence for a *transporter-mediated* uptake mechanism in MASLD is therefore real — but it points at **CD36**, a different protein than the one the seed hypothesis elevates.

### F004 — GTEx v8 confirms FATP5 is liver-predominant (constitutive) while CD36 is low in healthy liver (disease-induced), reconciling the two as parallel arms

A query of the **GTEx Portal API v2** (dataset gtex_v8, median TPM across 54 tissues, retrieved 2026-10-07; artifact `gtex_v8_transporter_tissue_expression.json`) showed:

| Gene | Liver median TPM | Liver rank (of 54) | Notes |
|------|-----------------|--------------------|-------|
| SLC27A5 / FATP5 | 254.5 | **1** | 16.7× the next tissue (testis 15.3); 51.1% of summed cross-tissue median — essentially liver-exclusive |
| SLC27A2 / FATP2 | 87.2 | **1** | but substantial in pituitary (22.5), kidney cortex (18.4), adrenal (13.6) — not liver-exclusive |
| CD36 | 3.42 | 30 | low in healthy liver; highest in visceral (549) and subcutaneous (535) adipose |

This supports FATP5 as the **constitutive dominant hepatic LCFA transporter** in health, whereas CD36 is low in healthy liver and becomes relevant only when *induced* by disease (consistent with F003). The two uptake hypotheses are thus **parallel and reconcilable**, not mutually exclusive: FATP5 sets baseline hepatic LCFA handling; CD36 is a disease-amplified, insulin-resistance-linked route.

### F005 — The better-validated arms (upstream adipose-IR NEFA supply; parallel DNL) are where approved MASH drugs act, leaving transporter-uptake an untested therapeutic node

Review-level human synthesis (Truong & Lee 2025, [PMID: 40935652](https://pubmed.ncbi.nlm.nih.gov/40935652/)) identifies adipose-lipolysis–derived FFA supply and insulin/substrate-driven de novo lipogenesis (with lipotoxic DAG/ceramide intermediates) as central, noting DNL is **"a major, yet modifiable, contributor to MASLD."** Donnelly 2005 quantifies these arms in humans (NEFA 59%, DNL 26%). Crucially, **approved pharmacotherapy acts downstream of uptake**: resmetirom, a thyroid-hormone-receptor-β agonist, **"achieved MASH resolution in 26%-30% versus 10% placebo and fibrosis improvement in 24%-26% versus 14% placebo at 52 weeks in the MAESTRO-NASH trial"** ([PMID: 42564069](https://pubmed.ncbi.nlm.nih.gov/42564069/)); semaglutide (GLP-1R) and emerging PPAR/FGF21 agents target metabolic/incretin axes ([PMID: 42687024](https://pubmed.ncbi.nlm.nih.gov/42687024/)). No FATP-directed agent has entered human MASLD trials. This finding both *supports* the seed's claim that uptake is a *separable, untested* target and *weakens* its priority, because the validated therapeutic wins so far have come from the lipogenic/oxidative/metabolic arms.

### F006 — Zero registered trials of any FATP5/FATP2-directed agent in MASLD/NASH

A documented search of **ClinicalTrials.gov API v2** (retrieved 2026-10-07; artifact `logs/clinicaltrials_search_log.json`) returned: lipofermata = 0; FATP5 = 0; SLC27A5 = 0; SLC27A2 = 0; FATP2 = 1 (NCT04349475, an omega-3/triglyceride study in pregnancy — *not* a FATP2-directed agent). A broader "fatty acid transport protein" + (steatohepatitis OR MASLD OR NAFLD) search returned 17 studies, all diet/exercise/orlistat/GLP-1/FMT/growth-hormone interventions with **no FATP-directed agent**. This directly confirms the therapeutic-absence gap the seed YAML flags.

### F007 — New (2025) murine + human-expression evidence strengthens the FATP5 arm but reinforces the pleiotropy confound

Liu et al. 2025 ([PMID: 40840619](https://pubmed.ncbi.nlm.nih.gov/40840619/)) report that FATP5 is elevated in in-vitro/in-vivo MASH models and upregulated in MASH patients, and that **"FATP5 deficiency protected against methionine-choline-deficient diet (MCD)-induced MASH in the mouse model and prevented steatotic HepG2 cell deaths through reducing ferroptosis"** via preferential depletion of pro-ferroptotic PUFA-containing lipids. This is a mechanistically independent model-organism result reinforcing the therapeutic arm. However, the same paper restates FATP5's **dual function** — **"FATP5, a hepatocyte-specific transmembrane protein, mediates both long-chain fatty acids (LCFAs) uptake and bile acids (BAs)-coenzyme A (CoA) conjugation"** — and Penno/Odermatt 2014 ([PMID: 25061560](https://pubmed.ncbi.nlm.nih.gov/25061560/)) independently confirm that **"the BA-CoA ligase Fatp5"** is required for bile-acid amidation. The protection therefore cannot be cleanly attributed to the hepatic-uptake step alone; a ferroptosis-lipidome mechanism and a bile-acid mechanism are co-active.

### F008 — A competing *druggable uptake* model: an iPLA2β/CD36/caveolin-1/FABPpm complex, blockable without touching FATP5/FATP2

Stremmel et al. 2014 ([PMID: 24719358](https://pubmed.ncbi.nlm.nih.gov/24719358/)) showed in HepG2 and primary hepatocytes that **"fatty acid influx is mediated by a heterotetrameric plasma membrane protein complex consisting of plasma membrane fatty acid-binding protein, caveolin-1, CD36, and calcium-independent membrane phospholipase A2 (iPLA2β)."** iPLA2β blockade with UDCA-LPE dissociated the complex and inhibited influx (IC50 47 µM); iPLA2β-knockout hepatocytes showed 56.5% lower influx; and **"steatosis and inflammation were abrogated by UDCA-LPE treatment in a cellular model of NASH."** This defines a *druggable* hepatic uptake mechanism that is distinct from FATP5/FATP2 and competes directly with the seed's specific transporter attribution while *agreeing* with its broader "uptake is druggable" thesis.

### F009 — Overall tiered synthesis

A four-tier synthesis of the eight findings and three computational artifacts yields the partially-supported verdict:

- **Tier 1 (Established):** hepatic LCFA uptake is protein-mediated ([PMID: 16618416](https://pubmed.ncbi.nlm.nih.gov/16618416/); GTEx FATP5 liver-predominant, 254 TPM, rank 1/54).
- **Tier 2 (Human-supported):** uptake is quantitatively dominant — NEFA = 59% of hepatic TAG ([PMID: 15864352](https://pubmed.ncbi.nlm.nih.gov/15864352/)).
- **Tier 3 (Rodent-only, confounded):** FATP5 KO/knockdown reverses murine NAFLD ([PMID: 18524776](https://pubmed.ncbi.nlm.nih.gov/18524776/), [PMID: 40840619](https://pubmed.ncbi.nlm.nih.gov/40840619/)) but is confounded by bile-acid-CoA-ligase function ([PMID: 25061560](https://pubmed.ncbi.nlm.nih.gov/25061560/)) and reduced caloric intake ([PMID: 18524776](https://pubmed.ncbi.nlm.nih.gov/18524776/)).
- **Tier 4 (Unresolved/untested):** no human `genetic_association` for SLC27A5/SLC27A2 to any MASLD term (Open Targets v4); zero FATP-directed MASLD trials (ClinicalTrials.gov v2). Competing human/druggable signals center on CD36 ([PMID: 21270117](https://pubmed.ncbi.nlm.nih.gov/21270117/)) and the iPLA2β/CD36/caveolin-1/FABPpm complex ([PMID: 24719358](https://pubmed.ncbi.nlm.nih.gov/24719358/)).

---

## Evidence Matrix

| Citation | Evidence type | Stance | Mechanistic claim tested | Key finding | Subtype/context | Confidence & limitations |
|----------|--------------|--------|--------------------------|-------------|-----------------|--------------------------|
| [PMID: 16618416](https://pubmed.ncbi.nlm.nih.gov/16618416/) | Model organism (KO) | Supports (core premise) | Hepatocellular LCFA entry is protein-mediated, requires FATP5 | Targeted FATP5 deletion disrupts hepatic lipid homeostasis; uptake is protein-mediated | Mouse whole-body KO | High for premise; murine; pleiotropic (bile-acid) effects noted |
| [PMID: 15864352](https://pubmed.ncbi.nlm.nih.gov/15864352/) | Human clinical (flux) | Supports (quantitative dominance) | NEFA uptake is major source of hepatic TAG | 59% of hepatic TAG from serum NEFA; 26% DNL; 15% diet | 9 biopsy-proven NAFLD patients | High; small n; measures flux not transporter rate-limitation; non-FATP-specific |
| [PMID: 18524776](https://pubmed.ncbi.nlm.nih.gov/18524776/) | Model organism (ASO knockdown) | Supports (therapeutic) / Qualifies | FATP5 knockdown reverses established NAFLD | Reversal of diet-induced NAFLD + improved glycemia; BUT reduced caloric uptake | Mouse, diet-induced | Moderate; caloric-intake confound explicitly reported; murine |
| [PMID: 40840619](https://pubmed.ncbi.nlm.nih.gov/40840619/) | Model organism + human expression | Supports / Qualifies | FATP5 deficiency protects via lipidome remodeling/ferroptosis | FATP5 KO protects against MCD-MASH; reduces ferroptosis; FATP5 up in MASH patients | Mouse MCD; HepG2; human expression | Moderate; murine causality; dual-function confound restated |
| [PMID: 25061560](https://pubmed.ncbi.nlm.nih.gov/25061560/) | Model organism | Qualifies (confound) | FATP5 is the hepatic bile-acid-CoA ligase | Fatp5 required for bile-acid amidation | Mouse liver | High; establishes pleiotropy that confounds uptake attribution |
| Open Targets v4 (computational) | Computational (DB query) | Refutes strong form | Human genetic association SLC27A5/SLC27A2 → MASLD | No `genetic_association` score for any FATP (or CD36) to any MASLD term; FATP5 human footprint is cholestatic | Human, pan-tissue genetics | High for absence; text-mining scores only; absence as of 2026-10-07 |
| GTEx v8 (computational) | Computational (DB query) | Qualifies / contextualizes | FATP5 liver-predominance; CD36 disease-induction | FATP5 254 TPM rank 1/54; CD36 3.4 TPM rank 30/54 in healthy liver | Human, 54 tissues, healthy | High; expression not causation; bulk tissue |
| [PMID: 21270117](https://pubmed.ncbi.nlm.nih.gov/21270117/) | Human clinical (biopsy) | Competing | CD36 is the human hepatic uptake transporter in NAFLD/NASH | CD36 up and relocated to plasma membrane; correlates with IR, steatosis | NAFLD/NASH/HCV biopsies | High; competing transporter; associative not interventional |
| [PMID: 38642829](https://pubmed.ncbi.nlm.nih.gov/38642829/) | Human + mouse mechanistic | Competing | O-GlcNAcylation drives CD36-mediated uptake in NASH | CD36 up/membrane-localized in NASH patient liver; mutating O-GlcNAc sites reduces steatosis | Human NASH + mouse | Moderate-high; strengthens CD36 arm over FATP |
| [PMID: 28062946](https://pubmed.ncbi.nlm.nih.gov/28062946/) | Human clinical | Competing (parallel route) | Intestinal palmitic-acid absorption transporters upregulated in NASH | Upregulated intestinal FA absorption tracks NASH progression | 106 subjects, NASH stages | Moderate; shifts uptake locus to gut; non-FATP |
| [PMID: 24719358](https://pubmed.ncbi.nlm.nih.gov/24719358/) | In vitro | Competing (alternative druggable complex) | iPLA2β/CD36/caveolin-1/FABPpm complex mediates druggable uptake | UDCA-LPE blockade dissociates complex, cuts influx, abrogates steatosis in NASH cell model | HepG2/primary hepatocytes | Moderate; in vitro; competing druggable mechanism |
| [PMID: 40935652](https://pubmed.ncbi.nlm.nih.gov/40935652/) | Review (human synthesis) | Competing (parallel arm) | DNL and adipose-IR FFA supply are central | DNL "a major, yet modifiable, contributor" | Human MASLD | Review-level; orientation |
| [PMID: 42564069](https://pubmed.ncbi.nlm.nih.gov/42564069/) | Review of trial data | Competing (where drugs act) | Approved agents act downstream of uptake | Resmetirom MASH resolution 26–30% vs 10% placebo | Non-cirrhotic MASH | High for trial facts; THR-β not uptake |
| ClinicalTrials.gov v2 (computational) | Computational (DB query) | Refutes strong form (therapeutic) | A FATP-directed MASLD trial exists | Zero FATP5/FATP2-directed trials; lipofermata = 0 | Human trials registry | High for absence as of 2026-10-07 |

---

## Mechanistic Model / Causal Chain

```
   UPSTREAM TRIGGER                 HEPATIC UPTAKE STEP               DOWNSTREAM / CLINICAL
 ┌──────────────────┐   NEFA flux  ┌───────────────────────┐  TAG   ┌──────────────────────┐
 │ Adipose insulin  │─────────────▶│ Protein-mediated LCFA │───────▶│ Hepatic steatosis →  │
 │ resistance →     │  (59% of     │ entry at basolateral  │  pool  │ MASH → fibrosis →    │
 │ lipolysis → FFA  │  hepatic TAG)│ membrane              │        │ cirrhosis / HCC      │
 └──────────────────┘   [STRONG,   │  • FATP5 (SLC27A5)    │        └──────────────────────┘
          │              human]    │    constitutive, liver│                 ▲
          │                        │    -exclusive [STRONG]│                 │
 ┌────────┴─────────┐              │  • FATP2 (SLC27A2)    │        ┌────────┴─────────┐
 │ Dietary FA (15%) │─────────────▶│  • CD36 disease-      │        │ De novo lipogen- │
 │ + intestinal     │              │    induced [competing]│        │ esis (26%) —     │
 │ absorption ↑NASH │              │  • iPLA2β complex     │        │ parallel arm,    │
 └──────────────────┘              │    [competing]        │        │ drug-validated   │
                                   └───────────────────────┘        └──────────────────┘

 Seed claim: the uptake step is RATE-LIMITING and DRUGGABLE via FATP5/FATP2
 Status of each edge:
   adipose-IR → NEFA → liver TAG ............. STRONG   (human, Donnelly 2005)
   uptake is protein-mediated ................ STRONG   (mouse KO + GTEx expression)
   FATP5/FATP2 are the rate-limiting setters . INFERRED (rodent KO; confounded)
   blocking FATP5/FATP2 reverses HUMAN disease  MISSING  (no human trial / genetics)
   FATP5 KO protection = uptake step only ..... CONFOUNDED (bile-acid ligase + ↓calories)
```

**Where the literature is strong:** the upstream supply edge (adipose-IR → NEFA → hepatic TAG) and the premise that hepatic LCFA entry is protein-mediated and FATP5-dependent at baseline.

**Where links are inferred:** that FATP5/FATP2 specifically are *rate-limiting* (i.e., that flux through them, rather than substrate supply, sets steatosis) rests on rodent perturbation only.

**Where causal steps are missing:** (1) any human genetic or interventional edge from SLC27A5/SLC27A2 to MASLD; (2) a clean rodent experiment isolating the hepatic-uptake function of FATP5 from its bile-acid-CoA ligase function and from reduced caloric intake; (3) demonstration that uptake blockade *reverses established human steatosis* independent of the DNL and oxidative arms.

---

## Data and Tool Use

| Resource | Accession / URI | Version / snapshot | Retrieval date | Access status | Query / filter | Resolved & relevant? |
|----------|-----------------|--------------------|----------------|---------------|----------------|----------------------|
| Open Targets Platform | GraphQL API; targets ENSG00000083807 (SLC27A5), ENSG00000140284 (SLC27A2), ENSG00000135218 (CD36) | v4 | 2026-10-07 | **Accessed** (artifact saved) | `target.associatedDiseases`; filter MASLD terms EFO_1001248, MONDO_0007027, EFO_0008527, MONDO_0004790; inspect datatypeScores | Yes; genuinely relevant — tests the human genetic edge |
| GTEx Portal | API v2, dataset `gtex_v8`, genes SLC27A5/SLC27A2/CD36 | v8 | 2026-10-07 | **Accessed** (artifact `gtex_v8_transporter_tissue_expression.json`) | median gene-level TPM across 54 tissues | Yes; relevant — tests tissue-restriction / constitutivity claims |
| ClinicalTrials.gov | API v2 | v2 | 2026-10-07 | **Accessed** (artifact `logs/clinicaltrials_search_log.json`) | `query.term` = lipofermata / FATP5 / SLC27A5 / SLC27A2 / FATP2; broad "fatty acid transport protein" + (steatohepatitis OR MASLD OR NAFLD) | Yes; relevant — tests therapeutic-absence claim |
| PubMed / MEDLINE | `search_pubmed` tool | n/a | iterations 1–5 | **Searched** (33 papers reviewed) | FATP5/FATP2/CD36 / hepatic fatty-acid uptake + MASLD/NASH terms | Yes; primary-literature evidence base |

**Analysis inventory (input → method → output):**

1. **Open Targets association query** — Input: three Ensembl gene IDs + four MASLD EFO/MONDO terms. Method: GraphQL `associatedDiseases` with datatype-score inspection. Output: no `genetic_association` score for any gene/term pair; literature-only scores tabulated; FATP5 top associations are cholestatic. **Outcome: succeeded.**
2. **GTEx expression query** — Input: three gene IDs. Method: REST v2 median-TPM retrieval across 54 tissues; ranking + fold-change computation. Output: `gtex_v8_transporter_tissue_expression.json`; FATP5 rank 1/54 (254.5 TPM), FATP2 rank 1 (87.2) but multi-tissue, CD36 rank 30 (3.42). **Outcome: succeeded.**
3. **ClinicalTrials.gov search** — Input: five agent/gene terms + one broad compound query. Method: API v2 `query.term`. Output: `logs/clinicaltrials_search_log.json`; counts 0/0/0/0/1(irrelevant)/17(none FATP-directed). **Outcome: succeeded (negative result).**

No patient-level or controlled-access data were used. No wet-lab or structural-biology (Phenix) analysis was applicable to this literature/database hypothesis search; none was performed or claimed. All three computational analyses produced inspectable JSON/log artifacts; none was reported-only.

---

## Limitations and Knowledge Gaps

| Gap | Scope | Why it matters | What was checked | What would resolve it |
|-----|-------|----------------|------------------|-----------------------|
| **No human genetics for SLC27A5/SLC27A2 → MASLD** | Strong-form causal edge | A human genetic association would move the hypothesis from EMERGING toward established, independent of rodent confounds | Open Targets Platform v4, four MASLD terms, 2026-10-07 — no `genetic_association` score | GWAS/ExWAS/rare-variant burden testing of SLC27A5/SLC27A2 against MRI-PDFF / biopsy MASLD; Mendelian randomization |
| **FATP5 pleiotropy confound** | Rodent causal interpretation | Protection on KO cannot be attributed to the uptake step alone because FATP5 is also the bile-acid-CoA ligase | [PMID: 25061560](https://pubmed.ncbi.nlm.nih.gov/25061560/), [PMID: 40840619](https://pubmed.ncbi.nlm.nih.gov/40840619/) | Separation-of-function FATP5 mutant that abolishes LCFA transport but preserves BA-CoA ligase activity (or vice versa) |
| **Caloric-intake confound** | Rodent therapeutic interpretation | Reported protection co-occurs with reduced whole-animal caloric uptake | [PMID: 18524776](https://pubmed.ncbi.nlm.nih.gov/18524776/) | Pair-feeding / hepatocyte-restricted acute knockdown with isocaloric controls |
| **No FATP-directed human trial** | Therapeutic form | The strong claim is explicitly therapeutic; no agent has been tested in human MASLD | ClinicalTrials.gov v2, 2026-10-07 — zero relevant trials | Phase 1/2 of a liver-targeted FATP5/FATP2 inhibitor with MRI-PDFF endpoint |
| **CD36 vs FATP primacy unresolved** | Which transporter is rate-limiting in humans | Determines whether the KB should elevate FATP5/FATP2 or CD36 | [PMID: 21270117](https://pubmed.ncbi.nlm.nih.gov/21270117/), [PMID: 38642829](https://pubmed.ncbi.nlm.nih.gov/38642829/), GTEx | Head-to-head isotopic uptake flux with transporter-selective inhibition in human hepatocytes/organoids |
| **Flux ≠ rate-limitation** | Interpretive | 59% NEFA contribution shows dominance of supply, not that the transporter (vs substrate concentration) is rate-controlling | [PMID: 15864352](https://pubmed.ncbi.nlm.nih.gov/15864352/) | Metabolic control analysis quantifying the flux-control coefficient of the transporter |

**Source-level absences verified on 2026-10-07:** Open Targets Platform v4 — no human `genetic_association` datatype for SLC27A5/SLC27A2/CD36 to NAFLD/MASH/steatosis/fatty-liver terms. ClinicalTrials.gov v2 — no FATP5/FATP2-directed interventional trial in MASLD/NASH. No GenCC/ClinGen gene-disease validity query was performed; the SLC27A5/SLC27A2–MASLD curation status in those sources remains **unverified** (not claimed absent).

---

## Alternative Models

1. **CD36-mediated hepatic uptake (competing, parallel).** CD36 is the transporter with the strongest *human* evidence (membrane relocation in NASH biopsies, O-GlcNAc regulation, IR correlation). GTEx shows it is disease-induced rather than constitutive — complementary to, not exclusive of, FATP5. **Relationship:** parallel transporter arm; currently better human-supported than the FATP arm.

2. **iPLA2β/CD36/caveolin-1/FABPpm uptake complex (competing druggable mechanism).** A multi-protein plasma-membrane complex whose pharmacological dissociation (UDCA-LPE) blocks influx and abrogates steatosis in a NASH cell model — supports "uptake is druggable" while *rejecting* the FATP-specific attribution. **Relationship:** alternative druggable node for the same step.

3. **Adipose insulin resistance / NEFA oversupply (upstream cause).** The canonical "passive sink" model the seed argues against — adipose lipolysis sets the NEFA load (59% of hepatic TAG). **Relationship:** upstream driver; the seed reframes the *rate-limiting* locus downstream of it, but supply-side dominance remains the parsimonious default.

4. **De novo lipogenesis (parallel, drug-validated).** DNL contributes ~26% of hepatic TAG and is "a major, yet modifiable" target; the metabolic/oxidative arms are where resmetirom and incretins act. **Relationship:** parallel contributor and the arm with proven human therapeutic traction.

5. **Intestinal fatty-acid absorption (parallel, upstream).** Upregulated intestinal palmitic-acid absorption transporters track NASH progression — relocating part of the "uptake" control to the gut. **Relationship:** parallel upstream supply modifier.

6. **Lipidome-remodeling / ferroptosis (downstream consequence of FATP5).** The 2025 data suggest FATP5's protective KO effect may operate partly by depleting pro-ferroptotic PUFA lipids rather than by reducing bulk steatosis — a downstream mechanism that *reinterprets* rather than replaces the uptake claim. **Relationship:** downstream consequence that complicates the "uptake = steatosis" logic.

---

## Discriminating Tests

1. **Human genetics (highest yield):** ExWAS/rare-variant burden and common-variant association of SLC27A5 and SLC27A2 against MRI-PDFF and biopsy-defined MASLD in large cohorts (UK Biobank, FinnGen, MASLD consortia), plus Mendelian randomization. *Expected if hypothesis true:* steatosis-raising alleles in FATP genes. *Current state:* absent in Open Targets v4 — the decisive missing evidence.

2. **Separation-of-function rodent model:** Engineer an FATP5 variant that abolishes LCFA transport while preserving bile-acid-CoA ligase activity (and the converse). *Expected if hypothesis true:* the transport-dead variant protects against steatosis while bile-acid metabolism is intact — isolating the uptake step from the two confounds.

3. **Transporter-selective flux in human hepatocytes/organoids:** Isotopic LCFA-uptake flux with selective FATP5/FATP2 vs CD36 inhibition in patient-derived hepatocytes or organoids, with metabolic control analysis. *Expected if hypothesis true:* FATP inhibition carries a high flux-control coefficient and reduces intracellular TAG; discriminates FATP from CD36 primacy.

4. **Liver-targeted FATP inhibitor, Phase 1/2 MASLD trial:** A hepatocyte-restricted FATP5/FATP2 inhibitor with MRI-PDFF primary endpoint and pair-controlled caloric intake. *Expected if hypothesis true:* fat-fraction reduction independent of caloric change — the therapeutic form of the claim.

5. **Head-to-head CD36 vs FATP knockdown in a humanized model:** Determine which transporter knockdown yields the larger steatosis reduction at matched disease stage, resolving the parallel-arm priority.

---

## Curation Leads (require curator verification)

**Candidate evidence references & snippets to verify:**
- [PMID: 40840619](https://pubmed.ncbi.nlm.nih.gov/40840619/) — *"FATP5 deficiency protected against methionine-choline-deficient diet (MCD)-induced MASH in the mouse model and prevented steatotic HepG2 cell deaths through reducing ferroptosis."* → Add as a recent SUPPORT (MODEL_ORGANISM) strengthening the therapeutic arm; also tag the dual-function snippet as the pleiotropy confound.
- [PMID: 25061560](https://pubmed.ncbi.nlm.nih.gov/25061560/) — *"Gene expression analyses revealed decreased expression of the BA-CoA ligase Fatp5, suggesting impaired BA amidation."* → Add as a QUALIFIER establishing the bile-acid-CoA ligase confound.
- [PMID: 21270117](https://pubmed.ncbi.nlm.nih.gov/21270117/) — *"FAT/CD36 was predominantly located at the plasma membrane of hepatocytes in patients with NAFLD and HCV G1 with steatosis."* → Add as COMPETING human evidence for a CD36 uptake node.
- [PMID: 24719358](https://pubmed.ncbi.nlm.nih.gov/24719358/) — *"fatty acid influx is mediated by a heterotetrameric plasma membrane protein complex consisting of plasma membrane fatty acid-binding protein, caveolin-1, CD36, and calcium-independent membrane phospholipase A2 (iPLA2β)."* → Add as COMPETING druggable-uptake model.
- [PMID: 38642829](https://pubmed.ncbi.nlm.nih.gov/38642829/), [PMID: 28062946](https://pubmed.ncbi.nlm.nih.gov/28062946/) → Add as COMPETING/parallel human uptake routes (CD36 O-GlcNAcylation; intestinal absorption).

**Candidate pathophysiology nodes/edges:** `CD36 (FAT) → hepatocyte plasma-membrane LCFA uptake → steatosis` (human-supported, competing); `iPLA2β/CD36/caveolin-1/FABPpm complex → LCFA influx` (in vitro, druggable); `FATP5 → bile-acid-CoA ligation` (confounding pleiotropic edge); `FATP5 → PUFA-lipidome → ferroptosis` (downstream reinterpretation).

**Candidate ontology terms:** cell type — hepatocyte (CL:0000182); processes — long-chain fatty acid import into cell (GO:0044539), bile acid biosynthetic process (GO:0006699), ferroptosis (GO:0097707), de novo lipogenesis.

**Candidate status / subtype notes:** retain **EMERGING**. Add explicit subtype restriction: FATP5 relevance is constitutive/baseline (GTEx liver-rank-1) whereas CD36 relevance is disease-stage-induced; the two should be curated as parallel, not interchangeable.

**Candidate `knowledge_gaps` prompts:** (1) "No human genetic_association for SLC27A5/SLC27A2 to any MASLD term in Open Targets v4 as of 2026-10-07." (2) "Rodent FATP5 protection confounded by bile-acid-CoA ligase pleiotropy and reduced caloric intake — needs separation-of-function experiment." (3) "Zero FATP-directed MASLD trials (ClinicalTrials.gov v2, 2026-10-07)." (4) "Competing human uptake signal centers on CD36, not FATP — primacy unresolved." (5) "GenCC/ClinGen gene-disease validity for SLC27A5/SLC27A2–MASLD not queried — unverified, not absent."

---

## Proposed Follow-up Experiments / Actions

1. Query **GenCC and ClinGen** for SLC27A5/SLC27A2 gene-disease validity to close the unverified source-level gap (highest-value, lowest-cost next step).
2. Mine **UK Biobank / FinnGen** summary statistics for SLC27A5/SLC27A2 variants against hepatic fat-fraction phenotypes.
3. Flag for curators a **separation-of-function rodent experiment** as the single most informative wet-lab study to de-confound the FATP5 arm.
4. Commission a **transporter-selective human-hepatocyte flux study** (FATP5/FATP2 vs CD36) to resolve the parallel-arm priority.
5. Add CD36 and the iPLA2β complex as explicit **competing hypotheses** in the KB so the uptake node is not conflated with the FATP-specific claim.

---

## Supported and Refuted Claims (summary)

| Claim component | Verdict |
|-----------------|---------|
| Hepatic LCFA entry is protein-mediated | **Supported** (mouse KO + GTEx) |
| NEFA uptake is quantitatively dominant source of hepatic TAG in humans | **Supported** (Donnelly 2005, 59%) |
| FATP5 is the constitutive liver-dominant LCFA transporter | **Supported** (GTEx rank 1/54) |
| FATP5/FATP2 are the *rate-limiting* setters of steatosis | **Emerging / inferred** (rodent-only, confounded) |
| Blocking FATP5/FATP2 reverses *established* disease | **Supported in mice only**, confounded (bile-acid ligase + caloric intake) |
| The step is druggable as a target in its own right in humans | **Unresolved / untested** (no human genetics, no trials) |
| FATP5/FATP2 are the *specific* human uptake transporters driving MASLD | **Not established — CD36 better human-supported** |

---

### Provider artifact bundle

Computational artifacts referenced above (Open Targets query output, `gtex_v8_transporter_tissue_expression.json`, `logs/clinicaltrials_search_log.json`) belong beneath `kb/hypotheses/Metabolic_Dysfunction-Associated_Steatotic_Liver_Disease/hepatic_fatty_acid_uptake_masld/openscientist_artifacts` with a canonical `MANIFEST.yaml` recording schema version, status/fallback flags, and checksummed inputs/outputs. The three database queries were executed and produced inspectable JSON/log outputs (succeeded); no patient-level, controlled-access, or large raw-download data were bundled (external identifiers and retrieval dates recorded instead). No wet-lab or structural analysis was applicable; none is claimed. Where an expected artifact is external (Open Targets/GTEx/ClinicalTrials.gov APIs), the stable external identifier and retrieval date are recorded rather than a bundled raw download.


## Artifacts

- [OpenScientist gtex v8 transporter tissue expression](openscientist_artifacts/kb_hypotheses_Metabolic_Dysfunction-Associated_Steatotic_Liver_Disease_hepatic_fatty_acid_uptake_masld_openscientist_artifacts_data_gtex_v8_transporter_tissue_expression.json)
- [OpenScientist opentargets transporter masld associations](openscientist_artifacts/kb_hypotheses_Metabolic_Dysfunction-Associated_Steatotic_Liver_Disease_hepatic_fatty_acid_uptake_masld_openscientist_artifacts_data_opentargets_transporter_masld_associations.json)
- [OpenScientist environment](openscientist_artifacts/kb_hypotheses_Metabolic_Dysfunction-Associated_Steatotic_Liver_Disease_hepatic_fatty_acid_uptake_masld_openscientist_artifacts_environment.json)
- [OpenScientist clinicaltrials search log](openscientist_artifacts/kb_hypotheses_Metabolic_Dysfunction-Associated_Steatotic_Liver_Disease_hepatic_fatty_acid_uptake_masld_openscientist_artifacts_logs_clinicaltrials_search_log.json)
- [OpenScientist gwas catalog check log](openscientist_artifacts/kb_hypotheses_Metabolic_Dysfunction-Associated_Steatotic_Liver_Disease_hepatic_fatty_acid_uptake_masld_openscientist_artifacts_logs_gwas_catalog_check_log.json)

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
| References checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 12 |
| On topic | 6 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:42564069` (4 mentions) - The new era of MASH pharmacotherapy: a comprehensive review of FDA-approved and emerging agents.
  - shared terms: none

Weighed against this report's own most characteristic terms: `uptake`, `fatp5`, `masld`, `human`, `hepatic`, `cd36`, `slc27a5`, `slc27a2`, `fatp2`, `steatosis`, `target`, `transporter`, `gtex`, `fatty`, `claim`, `genetic`, `clinicaltrial`, `ligase`, `nefa`, `open`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.
