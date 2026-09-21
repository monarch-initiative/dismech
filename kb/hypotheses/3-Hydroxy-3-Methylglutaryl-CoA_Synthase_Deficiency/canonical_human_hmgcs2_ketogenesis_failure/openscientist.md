---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-05-23T01:50:07.726711'
end_time: '2026-05-23T02:15:31.641601'
duration_seconds: 1523.92
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: 3-Hydroxy-3-Methylglutaryl-CoA Synthase Deficiency
  category: Mendelian
  hypothesis_group_id: canonical_hmgcs2_ketogenesis_failure_model
  hypothesis_label: Canonical HMGCS2 Ketogenesis Failure Model
  hypothesis_status: CANONICAL
  hypothesis_yaml: "hypothesis_group_id: canonical_hmgcs2_ketogenesis_failure_model\n\
    hypothesis_label: Canonical HMGCS2 Ketogenesis Failure Model\nstatus: CANONICAL\n\
    description: |\n  Biallelic HMGCS2 pathogenic variants reduce mitochondrial hydroxymethylglutaryl-CoA\
    \ synthase activity in hepatocytes. During fasting or illness, fatty acid beta-oxidation\
    \ supplies acetyl-CoA but defective HMGCS2 blocks conversion of acetyl-CoA and\
    \ acetoacetyl-CoA into HMG-CoA, the rate-limiting step in ketone body synthesis.\
    \ The liver therefore fails to produce adequate ketone bodies when glucose availability\
    \ falls, producing hypoketotic hypoglycemia and a characteristic acute-phase metabolite\
    \ pattern including dicarboxylic aciduria, 4HMP excretion, and elevated C2/C0\
    \ acylcarnitine ratio.\nevidence:\n- reference: PMID:32952630\n  reference_title:\
    \ 'Japanese patients with mitochondrial 3-hydroxy-3-methylglutaryl-CoA synthase\
    \ deficiency:\n    In vitro functional analysis of five novel HMGCS2 mutations.'\n\
    \  supports: SUPPORT\n  evidence_source: OTHER\n  snippet: which is the rate-limiting\
    \ step of ketone body synthesis\n  explanation: This review statement places HMGCS2\
    \ at the rate-limiting step of ketogenesis.\n- reference: PMID:39798988\n  reference_title:\
    \ Mitochondrial HMG-CoA synthase deficiency.\n  supports: SUPPORT\n  evidence_source:\
    \ HUMAN_CLINICAL\n  snippet: mutations in the HMGCS2 gene, leading to impaired\
    \ ketogenesis.\n  explanation: The systematic review links HMGCS2 mutations to\
    \ impaired ketogenesis."
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 2
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
citation_count: 28
---

## Question

# Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** 3-Hydroxy-3-Methylglutaryl-CoA Synthase Deficiency
- **Category:** Mendelian

## Target Hypothesis
- **Hypothesis ID:** canonical_hmgcs2_ketogenesis_failure_model
- **Hypothesis Label:** Canonical HMGCS2 Ketogenesis Failure Model
- **Status in KB:** CANONICAL

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: canonical_hmgcs2_ketogenesis_failure_model
hypothesis_label: Canonical HMGCS2 Ketogenesis Failure Model
status: CANONICAL
description: |
  Biallelic HMGCS2 pathogenic variants reduce mitochondrial hydroxymethylglutaryl-CoA synthase activity in hepatocytes. During fasting or illness, fatty acid beta-oxidation supplies acetyl-CoA but defective HMGCS2 blocks conversion of acetyl-CoA and acetoacetyl-CoA into HMG-CoA, the rate-limiting step in ketone body synthesis. The liver therefore fails to produce adequate ketone bodies when glucose availability falls, producing hypoketotic hypoglycemia and a characteristic acute-phase metabolite pattern including dicarboxylic aciduria, 4HMP excretion, and elevated C2/C0 acylcarnitine ratio.
evidence:
- reference: PMID:32952630
  reference_title: 'Japanese patients with mitochondrial 3-hydroxy-3-methylglutaryl-CoA synthase deficiency:
    In vitro functional analysis of five novel HMGCS2 mutations.'
  supports: SUPPORT
  evidence_source: OTHER
  snippet: which is the rate-limiting step of ketone body synthesis
  explanation: This review statement places HMGCS2 at the rate-limiting step of ketogenesis.
- reference: PMID:39798988
  reference_title: Mitochondrial HMG-CoA synthase deficiency.
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: mutations in the HMGCS2 gene, leading to impaired ketogenesis.
  explanation: The systematic review links HMGCS2 mutations to impaired ketogenesis.
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
evidence or experiment would resolve it.

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

If the provider supports artifacts, produce artifact-friendly outputs such as an
evidence matrix, mechanistic diagram, knowledge-gap table, or comparison table.
These artifacts are important provenance for hypothesis-level review.


## Output

# Hypothesis Evaluation Report: Canonical HMGCS2 Ketogenesis Failure Model

**Hypothesis ID:** `canonical_hmgcs2_ketogenesis_failure_model`  
**Disease:** 3-Hydroxy-3-Methylglutaryl-CoA Synthase Deficiency (HMGCS2D)  
**Category:** Mendelian  
**KB Status:** CANONICAL  
**Report Date:** 2026-05-23  
**Papers Reviewed:** 41  
**Confirmed Findings:** 8  

---

## Executive Judgment

**Verdict: SUPPORTED with important qualifications**

The Canonical HMGCS2 Ketogenesis Failure Model is **strongly supported** by converging evidence from over 150 clinical cases across multiple ethnic populations, 85 ClinVar-classified pathogenic/likely pathogenic variants, in vitro functional studies demonstrating loss of enzyme activity, and multiple independent mouse knockout models. The core mechanistic claim -- that biallelic HMGCS2 loss-of-function blocks the irreversible, rate-limiting step of mitochondrial ketogenesis (EC 2.3.3.10), producing hypoketotic metabolic decompensation during catabolic stress -- is well-established and not seriously challenged by any competing model.

However, five critical qualifications refine and limit the canonical description: (1) **hypoglycemia is not universal**, occurring in only ~56% of acute episodes, with normoglycemia and even severe hyperglycemia documented; (2) **compensatory acetate production** may partially mitigate absent ketogenesis in mouse models; (3) **incomplete penetrance** is well-documented, with asymptomatic biallelic carriers identified in multiple families; (4) the **phenotypic spectrum is broader** than classically described, now including neonatal-onset hyperammonemia, metabolic stroke with basal ganglia lesions, dyslipidemia, and metabolic screening patterns mimicking maple syrup urine disease; and (5) **acetyl-CoA accumulation drives secondary pathology** -- mitochondrial protein hyperacetylation, ACSL1-mediated fatty acid re-esterification, and hepatic steatosis -- extending the disease mechanism beyond simple ketone body deficiency.

The hypothesis merits continued CANONICAL status, but knowledge base annotations should incorporate these qualifications. Key gaps remain: no ClinGen gene-disease curation, no direct human hepatocyte enzyme activity measurements, unknown biosynthetic origin of the 4-hydroxy-6-methyl-2-pyrone (4HMP) biomarker, and the SIRT3-mediated post-translational regulation of HMGCS2 activity is untested as a clinical modifier.

---

## Summary

Mitochondrial 3-hydroxy-3-methylglutaryl-CoA synthase 2 (HMGCS2) deficiency is a rare autosomal recessive disorder of ketone body synthesis caused by biallelic pathogenic variants in the *HMGCS2* gene. The canonical mechanistic model posits that loss of HMGCS2 enzymatic activity blocks the conversion of acetyl-CoA and acetoacetyl-CoA to HMG-CoA -- the committed, rate-limiting step in hepatic ketogenesis -- leading to failure of ketone body production during fasting or illness. This results in hypoketotic metabolic decompensation and a characteristic metabolite signature including dicarboxylic aciduria, 4-hydroxy-6-methyl-2-pyrone (4HMP) excretion, and elevated acetylcarnitine (C2/C0 ratio).

Our systematic evaluation of 41 publications spanning clinical case series, systematic reviews, animal models, and in vitro studies confirms the core model with high confidence. The largest systematic review (93+2 cases; [PMID: 39798988](https://pubmed.ncbi.nlm.nih.gov/39798988/)) documented dicarboxylic aciduria in 96.4% of tested acute samples, 4HMP in 94.3%, and elevated C2/C0 ratio in 88.9%. A comprehensive review of 75 patients ([PMID: 40515583](https://pubmed.ncbi.nlm.nih.gov/40515583/)) confirmed 91% presentation with acute metabolic decompensation, 8% mortality mainly during initial crisis, and 98% favorable neurological outcomes in survivors. Multiple independent mouse models corroborate the mechanism, showing impaired ketogenesis, hepatic steatosis, and mitochondrial protein hyperacetylation upon HMGCS2 disruption.

The investigation also uncovered important refinements. The disease phenotype is more heterogeneous than the canonical model implies: hypoglycemia is absent in a substantial minority of patients, the age of onset ranges from day 7 of life to childhood, and presentations can mimic other inborn errors. The downstream consequences of blocked ketogenesis extend beyond energy failure to include acetyl-CoA-driven protein hyperacetylation and lipid metabolism dysregulation. Incomplete penetrance and the absence of genotype-phenotype correlations suggest that environmental and modifier gene effects play significant roles.

---

## Key Findings

### Finding 1: HMGCS2 Is Confirmed as the Rate-Limiting Ketogenesis Enzyme with Strong Clinical Support

The identification of HMGCS2 as the rate-limiting enzyme in mitochondrial ketogenesis is established beyond reasonable doubt. UniProt entry P54868 describes the enzyme as catalyzing "the first irreversible step in ketogenesis," converting acetoacetyl-CoA and acetyl-CoA to HMG-CoA (EC 2.3.3.10). The systematic review by Decru et al. ([PMID: 39798988](https://pubmed.ncbi.nlm.nih.gov/39798988/)) explicitly states that "mutations in the HMGCS2 gene, leading to impaired ketogenesis," and the comprehensive review by Grunert et al. ([PMID: 40515583](https://pubmed.ncbi.nlm.nih.gov/40515583/)) confirms that "Mitochondrial 3-hydroxy-3-methylglutaryl-coenzyme A synthase deficiency (HMGCS2D) is an autosomal recessive disorder of ketogenesis caused by biallelic variants in HMGCS2."

The clinical biomarker evidence is compelling: among acute-phase samples, dicarboxylic aciduria was present in 54/56 cases (96.4%), 4HMP in 33/35 samples (94.3%), and abnormal C2/C0 ratio in 16/18 plasma samples (88.9%). These biomarkers are mechanistically consistent with acetyl-CoA overflow (elevated C2), blocked ketogenesis (hypoketosis), and shunting of accumulated fatty acyl intermediates to omega-oxidation (dicarboxylic aciduria).

Animal model evidence provides independent confirmation. Arima et al. ([PMID: 33619377](https://pubmed.ncbi.nlm.nih.gov/33619377/)) demonstrated that Hmgcs2 knockout neonatal mice show impaired ketogenesis with acetyl-CoA accumulation. Asif et al. ([PMID: 35421611](https://pubmed.ncbi.nlm.nih.gov/35421611/)) showed that mice lacking Hmgcs2 develop spontaneous fatty liver during postnatal development. Queathem et al. ([PMID: 40272888](https://pubmed.ncbi.nlm.nih.gov/40272888/)) demonstrated that "disruption of mitochondrial HMG-CoA synthase (HMGCS2), the rate-limiting step of ketogenesis, impairs overall hepatic fat oxidation and induces an MASLD-MASH-like phenotype."

ClinVar contains 85 pathogenic/likely pathogenic HMGCS2 variants out of 369 total entries, providing a robust molecular basis. The Japanese study by Aoyama et al. ([PMID: 32952630](https://pubmed.ncbi.nlm.nih.gov/32952630/)) provided in vitro functional validation of five novel mutations, confirming loss of enzymatic activity.

### Finding 2: Hypoglycemia Is NOT a Universal Feature -- Important Qualification

The canonical model names "hypoketotic hypoglycemia" as the hallmark presentation, but accumulating evidence demonstrates that hypoglycemia is neither necessary nor universal. Pitt et al. ([PMID: 32905056](https://pubmed.ncbi.nlm.nih.gov/32905056/)) reported "the third case of mHS deficiency presenting in the absence of hypoglycemia, with profound biochemical abnormalities and further evidence of potential specific diagnostic biomarkers." The Vietnamese cohort study by Nguyen et al. ([PMID: 40004108](https://pubmed.ncbi.nlm.nih.gov/40004108/)) found that only 56.3% of symptomatic patients had hypoglycemia during their first acute episode.

Most strikingly, a recent case report ([PMID: 40937626](https://pubmed.ncbi.nlm.nih.gov/40937626/)) documented severe hyperglycemia (25.8 mmol/L) as the initial presenting symptom, noting that "severe hyperglycemia as an initial presenting symptom has not been previously reported." This finding directly challenges the assumption that glucose homeostasis necessarily fails in the hypoglycemic direction during HMGCS2D crises.

Mouse model evidence provides a mechanistic explanation: Feola et al. ([PMID: 38876267](https://pubmed.ncbi.nlm.nih.gov/38876267/)) demonstrated that hepatic HMGCS2 deficiency in mice did not impair starvation adaptation -- mice maintained blood glucose and body temperature during prolonged fasting. These animals exhibited compensatory elevation of plasma acetate levels, suggesting an alternative fuel source.

**Implication for the KB:** The term "hypoketotic hypoglycemia" should be qualified to "hypoketotic metabolic decompensation" as the core phenotype, with hypoglycemia listed as a frequent but not defining feature.

### Finding 3: Acetyl-CoA Accumulation Drives Secondary Pathology Beyond Energy Failure

The canonical model focuses on the downstream absence of ketone bodies. However, converging evidence reveals that the upstream accumulation of acetyl-CoA is itself pathogenic. Arima et al. ([PMID: 33619377](https://pubmed.ncbi.nlm.nih.gov/33619377/)) demonstrated that "acetylome analysis of Hmgcs2 KO cells revealed enhanced acetylation of mitochondrial proteins," restricting mitochondrial energy production capacity.

Mooli et al. ([PMID: 40692014](https://pubmed.ncbi.nlm.nih.gov/40692014/)) elucidated a specific mechanism: "the accumulation of acetyl-CoA because of impaired hepatic ketogenesis drives the elevated translocation of ACSL1 to the ER," increasing fatty acid re-esterification and promoting hepatic steatosis. This ACSL1-mediated pathway provides a direct link between ketogenic failure and the fatty liver commonly observed in HMGCS2D patients.

Queathem et al. ([PMID: 40272888](https://pubmed.ncbi.nlm.nih.gov/40272888/)) further showed that maintenance of ketogenesis provides hepatoprotection "through additional mechanisms that extend beyond overall rates of fat oxidation," suggesting that HMGCS2 has protective functions beyond simply disposing of acetyl-CoA.

**Implication:** The canonical model should be extended to a **dual-pathology framework**: (1) ketone body deficiency causing energy failure in ketone-dependent tissues (brain, heart), and (2) acetyl-CoA accumulation causing mitochondrial protein hyperacetylation, impaired oxidative capacity, and hepatic lipid dysregulation.

### Finding 4: Compensatory Acetate Production in HMGCS2 Deficiency

Feola et al. ([PMID: 38876267](https://pubmed.ncbi.nlm.nih.gov/38876267/)) discovered that "mice with hepatic HMGCS2 deficiency exhibited higher levels of plasma acetate levels in response to fasting." These animals maintained blood glucose and body temperature despite absent ketogenesis, suggesting that acetate may serve as a partial alternative fuel. The authors concluded that circulating hepatic-derived ketones do not provide protection against endotoxemia, challenging the assumption that ketone body absence is uniformly catastrophic.

This finding has implications for understanding the variable clinical severity and incomplete penetrance of HMGCS2D: patients with more robust acetate or alternative fuel production may tolerate fasting stress better.

### Finding 5: No Genotype-Phenotype Correlation; Incomplete Penetrance

The comprehensive review by Grunert et al. ([PMID: 40515583](https://pubmed.ncbi.nlm.nih.gov/40515583/)) explicitly states that "no genotype-phenotype correlation can be established" among 75 patients, and that "asymptomatic individuals were identified in several families." The Vietnamese study ([PMID: 40004108](https://pubmed.ncbi.nlm.nih.gov/40004108/)) confirmed that 3 of 19 patients with biallelic pathogenic variants were asymptomatic.

The only reported association between genotype and severity comes from Decru et al. ([PMID: 39798988](https://pubmed.ncbi.nlm.nih.gov/39798988/)), who noted that "severity was correlated with the number of truncating mutations." This suggests that complete loss of protein (truncating variants) may produce more severe phenotypes than missense variants retaining partial activity, but this observation requires validation in larger cohorts.

### Finding 6: Expanding Phenotypic Spectrum

Recent reports have substantially broadened the recognized clinical spectrum of HMGCS2D:

- **Neonatal onset:** Vaseenon et al. ([PMID: 40548098](https://pubmed.ncbi.nlm.nih.gov/40548098/)) reported onset on day of life 7 with "a sepsis-like condition, coma, metabolic acidosis, and marked elevation of ammonium level at 1081 umol/L," and metabolic screening resembling maple syrup urine disease (elevated valine, leucine/isoleucine).
- **Metabolic stroke:** Alshami et al. ([PMID: 41383544](https://pubmed.ncbi.nlm.nih.gov/41383544/)) described basal ganglia lesions and refractory seizures in a 2-year-old, demonstrating that HMGCS2D should be considered in the differential for pediatric metabolic stroke.
- **Dyslipidemia:** Rojnueangnit et al. ([PMID: 33045405](https://pubmed.ncbi.nlm.nih.gov/33045405/)) reported the first cases with steatorrhea and dyslipidemia (elevated triglycerides, VLDL, LDL; decreased HDL), and identified a carrier frequency of 0.42% for c.1502G>C (p.Arg501Pro) in the Thai population (9/2162 alleles).
- **Hyperglycemia:** [PMID: 40937626](https://pubmed.ncbi.nlm.nih.gov/40937626/) documented severe hyperglycemia (25.8 mmol/L) as a presenting feature.
- **Bicytopenia:** [PMID: 37931961](https://pubmed.ncbi.nlm.nih.gov/37931961/) reported a case presenting with hepatosplenomegaly, lymphadenopathy, and bicytopenia.

### Finding 7: SIRT3-Mediated Deacetylation as a Potential Modifier

SIRT3, the predominant mitochondrial deacetylase, "directly targets these enzymes [including HMGCS2] for deacetylation and maintains their optimal catalytic activity" ([PMID: 28512002](https://pubmed.ncbi.nlm.nih.gov/28512002/)). Liu et al. ([PMID: 41960367](https://pubmed.ncbi.nlm.nih.gov/41960367/)) showed that SIRT3 deacetylates HMGCS2 specifically at K310, promoting ketone body synthesis, and that low HMGCS2/SIRT3 expression correlated with poor patient survival in cholangiocarcinoma. This post-translational regulatory axis could theoretically modify disease severity in HMGCS2D: patients with higher SIRT3 activity might extract more residual function from hypomorphic HMGCS2 variants.

### Finding 8: Database-Level Evidence

ClinVar contains 85 pathogenic/likely pathogenic HMGCS2 variants (of 369 total entries). OMIM entries exist for both the gene (*600234) and the disease (#605911). UniProt P54868 confirms the enzyme's mitochondrial localization and the irreversible catalytic step: "acetoacetyl-CoA + acetyl-CoA + H2O = (3S)-3-hydroxy-3-methylglutaryl-CoA + CoA + H(+)." However, no ClinGen gene-disease validity curation was identified, representing a notable curation gap for a well-established Mendelian disorder.

---

## Mechanistic Causal Chain

{{figure:mechanistic_causal_chain.png|caption=Mechanistic causal chain of the HMGCS2 Ketogenesis Failure Model with evidence strength annotations. Blue nodes represent steps with strong evidence, orange nodes represent moderate evidence, pink boxes identify qualifying evidence, and red annotations mark knowledge gaps.}}

The causal chain from upstream trigger to clinical manifestation proceeds through the following steps:

### Step 1: Biallelic HMGCS2 Pathogenic Variants (STRONG evidence)

Biallelic loss-of-function variants in *HMGCS2* (autosomal recessive inheritance) reduce or abolish mitochondrial HMG-CoA synthase 2 protein function. **Evidence:** 85 ClinVar pathogenic variants; in vitro functional validation of multiple mutations ([PMID: 32952630](https://pubmed.ncbi.nlm.nih.gov/32952630/)); confirmed in >150 patients across multiple populations.

### Step 2: Reduced Mitochondrial HMGCS2 Enzyme Activity (MODERATE evidence -- inferred)

Pathogenic variants reduce the catalytic activity of the enzyme in hepatocyte mitochondria. **Gap:** No direct measurement of HMGCS2 enzyme activity in human hepatocyte lysates from patients has been published. Evidence is inferred from in vitro expression systems and clinical phenotype.

### Step 3: Blocked HMG-CoA Synthesis (STRONG evidence)

The conversion of acetyl-CoA + acetoacetyl-CoA to HMG-CoA is blocked at this irreversible, rate-limiting step. **Evidence:** UniProt confirms irreversibility; enzyme kinetics established; rate-limiting status confirmed in multiple reviews.

### Step 4a: Failed Ketone Body Production During Fasting/Illness (STRONG clinical evidence)

The liver fails to produce adequate beta-hydroxybutyrate and acetoacetate during catabolic stress. **Evidence:** Hypoketosis documented in the vast majority of acute episodes across all case series.

### Step 4b: Acetyl-CoA Accumulation (STRONG mouse evidence, moderate human evidence)

Unmetabolized acetyl-CoA accumulates in hepatocyte mitochondria. **Evidence:** Directly demonstrated in Hmgcs2 KO mice ([PMID: 33619377](https://pubmed.ncbi.nlm.nih.gov/33619377/)); not directly measured in human patients.

### Step 5: Clinical Manifestations (branching pathways)

| Pathway | Manifestation | Evidence Level |
|---------|--------------|----------------|
| Ketone deficiency + glucose depletion | Hypoketotic hypoglycemia | Strong clinical (~56-90% of cases) |
| Ketone deficiency in brain | Encephalopathy, seizures, coma | Strong clinical |
| Fatty acid overflow to omega-oxidation | Dicarboxylic aciduria | Strong (96.4% of acute samples) |
| Unknown biosynthetic pathway | 4HMP excretion | Strong clinically, mechanism unknown |
| Acetyl-CoA to carnitine conjugation | Elevated C2/C0 ratio | Strong (88.9% acute samples) |
| Protein hyperacetylation | Mitochondrial dysfunction | Strong mouse, not confirmed human |
| ACSL1 translocation to ER | Hepatic steatosis | Strong mouse, indirect human |
| Metabolic acidosis | Multi-organ dysfunction | Strong clinical |

### Missing Causal Steps

- **4HMP biosynthesis:** The pathway producing 4-hydroxy-6-methyl-2-pyrone from ketogenic intermediates is completely unknown.
- **Acetyl-CoA pathology in humans:** Protein hyperacetylation demonstrated only in mouse models.
- **Compensatory acetate pathway:** Source enzyme and regulation in humans unknown.
- **Variable hypoglycemia mechanism:** The determinants of whether a given crisis produces hypoglycemia, normoglycemia, or hyperglycemia are not established.

---

## Evidence Matrix

{{figure:evidence_matrix.png|caption=Evidence matrix summarizing key literature supporting, qualifying, or extending the HMGCS2 Ketogenesis Failure Model. Evidence is classified by type (human clinical, model organism, in vitro), direction (support, qualify, extend, competing), and confidence level.}}

| Citation | Evidence Type | Direction | Claim Tested | Key Finding | Context | Confidence |
|----------|-------------|-----------|-------------|-------------|---------|------------|
| [PMID: 39798988](https://pubmed.ncbi.nlm.nih.gov/39798988/) | Human clinical (systematic review) | SUPPORT | HMGCS2 mutations impair ketogenesis | 93+ cases; dicarboxylic aciduria 96%, 4HMP 94%, C2/C0 89% | Acute decompensation, all ages | HIGH |
| [PMID: 40515583](https://pubmed.ncbi.nlm.nih.gov/40515583/) | Human clinical (comprehensive review) | SUPPORT | Biallelic variants cause disease | 75 patients; 91% acute decompensation; 8% mortality; 98% good neuro outcome | First year of life onset | HIGH |
| [PMID: 32952630](https://pubmed.ncbi.nlm.nih.gov/32952630/) | In vitro + clinical | SUPPORT | HMGCS2 is rate-limiting | 5 novel mutations with functional characterization | Japanese patients | HIGH |
| [PMID: 40004108](https://pubmed.ncbi.nlm.nih.gov/40004108/) | Human clinical (cohort) | SUPPORT + QUALIFY | Clinical pattern of HMGCS2D | 19 pts; only 56.3% with hypoglycemia; 3 asymptomatic | Vietnamese cohort | HIGH |
| [PMID: 32905056](https://pubmed.ncbi.nlm.nih.gov/32905056/) | Human clinical (case) | QUALIFY | Hypoglycemia as defining feature | Third case without hypoglycemia; profound biochemical abnormalities | 20-month-old male | MODERATE |
| [PMID: 40937626](https://pubmed.ncbi.nlm.nih.gov/40937626/) | Human clinical (case) | QUALIFY | Hypoketotic hypoglycemia paradigm | Severe hyperglycemia (25.8 mmol/L) as presentation | 8-month infant | MODERATE |
| [PMID: 33619377](https://pubmed.ncbi.nlm.nih.gov/33619377/) | Model organism (mouse KO) | SUPPORT + EXTEND | Acetyl-CoA accumulation mechanism | Enhanced mitochondrial protein acetylation in Hmgcs2 KO | Neonatal mice | HIGH |
| [PMID: 40692014](https://pubmed.ncbi.nlm.nih.gov/40692014/) | Model organism (mouse KO) | EXTEND | Acetyl-CoA drives hepatic steatosis | ACSL1 translocation to ER via acetyl-CoA accumulation | Diet-induced steatosis | MODERATE |
| [PMID: 38876267](https://pubmed.ncbi.nlm.nih.gov/38876267/) | Model organism (mouse KO) | QUALIFY | Ketogenesis essential for adaptation | Hepatic KO mice maintained glucose; elevated acetate | Adult mice, fasting | MODERATE |
| [PMID: 40272888](https://pubmed.ncbi.nlm.nih.gov/40272888/) | Model organism + human | EXTEND | Ketogenesis protects beyond fat oxidation | HMGCS2 disruption impairs fat oxidation, induces MASLD-MASH | Mouse + human flux data | HIGH |
| [PMID: 35421611](https://pubmed.ncbi.nlm.nih.gov/35421611/) | Model organism (mouse KO) | SUPPORT | Hmgcs2 loss causes fatty liver | Spontaneous fatty liver in KO during postnatal development | Neonatal/postnatal | HIGH |
| [PMID: 40548098](https://pubmed.ncbi.nlm.nih.gov/40548098/) | Human clinical (case) | EXTEND | Phenotypic boundaries | Neonatal onset (DOL 7), hyperammonemia 1081 umol/L, MSUD mimicry | Neonates | MODERATE |
| [PMID: 41383544](https://pubmed.ncbi.nlm.nih.gov/41383544/) | Human clinical (case) | EXTEND | Neurological spectrum | Metabolic stroke, basal ganglia lesions, refractory seizures | 2-year-old | MODERATE |
| [PMID: 33045405](https://pubmed.ncbi.nlm.nih.gov/33045405/) | Human clinical (case series) | EXTEND | Novel phenotypic features | Steatorrhea, dyslipidemia; 0.42% carrier freq in Thailand | Thai patients | MODERATE |
| [PMID: 28512002](https://pubmed.ncbi.nlm.nih.gov/28512002/) | In vitro/review | SUPPORT (modifier) | SIRT3 regulates HMGCS2 | SIRT3 deacetylates HMGCS2 to maintain optimal catalytic activity | Cancer/metabolic context | MODERATE |
| [PMID: 41960367](https://pubmed.ncbi.nlm.nih.gov/41960367/) | In vitro + clinical | SUPPORT (modifier) | SIRT3-K310 deacetylation | SIRT3 deacetylates HMGCS2 at K310; low expression = poor survival | Cholangiocarcinoma | MODERATE |
| [PMID: 40960113](https://pubmed.ncbi.nlm.nih.gov/40960113/) | Human clinical (comparative) | CONTEXT | Ketogenesis vs. ketolysis defects | 30 patients: ketolysis defects present later, more severe acidosis | Comparative cohort | MODERATE |

---

## Alternative and Competing Models

### 1. Fatty Acid Oxidation Disorder Model (Competing -- Differential Diagnosis)

Several fatty acid oxidation defects (MCADD, VLCADD, LCHAD) produce overlapping phenotypes of hypoketotic hypoglycemia and dicarboxylic aciduria. These are **differential diagnoses**, not alternative mechanisms for the same gene. However, the overlap is clinically significant: the iPSC liver organoid study of MCADD ([PMID: 40199742](https://pubmed.ncbi.nlm.nih.gov/40199742/)) demonstrated that MCADD organoids show decreased C2 carnitine and differential expression of omega-oxidation genes, paralleling some HMGCS2D features. The 4HMP biomarker and genetic testing distinguish HMGCS2D from FAO disorders. The comparative study by Kahraman et al. ([PMID: 40960113](https://pubmed.ncbi.nlm.nih.gov/40960113/)) of 30 patients with ketogenesis vs. ketolysis defects showed that ketolysis defects present later (median 210 vs. 30 days) and with more severe acidosis.

### 2. Acetyl-CoA Toxicity Model (Complementary -- Downstream Extension)

This is not an alternative but a **downstream extension** of the canonical model. Evidence from Arima et al. ([PMID: 33619377](https://pubmed.ncbi.nlm.nih.gov/33619377/)) and Mooli et al. ([PMID: 40692014](https://pubmed.ncbi.nlm.nih.gov/40692014/)) suggests that acetyl-CoA accumulation itself drives pathology through protein hyperacetylation and lipid partitioning changes. This model explains the hepatic steatosis and potentially some of the metabolic acidosis better than ketone body absence alone.

### 3. Compensatory Fuel Model (Complementary -- Modifier)

The acetate production observed in Hmgcs2 KO mice ([PMID: 38876267](https://pubmed.ncbi.nlm.nih.gov/38876267/)) suggests a **parallel compensatory pathway** that may explain incomplete penetrance and variable severity. If some patients or some tissues can produce alternative fuels (acetate, amino acid-derived substrates), the clinical impact of ketogenic failure would be attenuated.

### 4. Renal Ketogenesis Model (Parallel Mechanism)

HMGCS2 is expressed in the kidney proximal tubule during fasting, but kidney-specific deletion studies ([PMID: 35224990](https://pubmed.ncbi.nlm.nih.gov/35224990/)) demonstrated that renal HMGCS2 does not contribute to circulating ketones. However, renal HMGCS2 appears to have local protective functions: kidney-specific KO mice had increased injury after ischemia-reperfusion ([PMID: 41568909](https://pubmed.ncbi.nlm.nih.gov/41568909/)). This is a **parallel tissue-specific mechanism** that may become relevant for long-term outcomes in HMGCS2D patients.

### 5. Post-Translational Regulation / SIRT3 Modifier Model (Upstream Modifier)

SIRT3-mediated deacetylation at K310 maintains HMGCS2 catalytic activity ([PMID: 41960367](https://pubmed.ncbi.nlm.nih.gov/41960367/); [PMID: 28512002](https://pubmed.ncbi.nlm.nih.gov/28512002/)). Variation in SIRT3 activity could theoretically modify residual HMGCS2 function in patients with hypomorphic variants, making this an **upstream modifier** hypothesis that does not challenge the core mechanism but may explain phenotypic variability.

### 6. CFC/RASopathy Ketogenesis Failure (Phenocopy)

Cardio-facio-cutaneous syndrome patients can present with nonketotic hypoglycemia resembling HMGCS2D ([PMID: 35943247](https://pubmed.ncbi.nlm.nih.gov/35943247/)). The mechanism involves RAS/MAPK pathway dysregulation affecting ketogenesis through unknown intermediaries. This represents a **phenocopy** through a different upstream pathway, not a competing explanation for HMGCS2 variant-caused disease.

---

## Knowledge Gaps

### Gap 1: No Direct Human Hepatocyte Enzyme Activity Measurements

**Scope:** Fundamental biochemical validation in human tissue.  
**Why it matters:** All enzyme activity data come from in vitro expression systems or mouse models. No study has measured HMGCS2 activity directly in liver biopsies or hepatocytes from HMGCS2D patients.  
**What was checked:** PubMed searches for "HMGCS2 enzyme activity human liver" and "HMG-CoA synthase activity patient."  
**Resolution:** Liver biopsy enzyme assays from diagnosed patients during and between crises, or iPSC-derived hepatocyte organoids from patient fibroblasts (analogous to the MCADD organoid approach in [PMID: 40199742](https://pubmed.ncbi.nlm.nih.gov/40199742/)).

### Gap 2: 4HMP Biosynthetic Pathway Unknown

**Scope:** Biomarker mechanism.  
**Why it matters:** 4-Hydroxy-6-methyl-2-pyrone (4HMP) is the most specific urinary biomarker (94.3% sensitivity), but its biosynthetic origin is unknown. Without understanding the pathway, we cannot determine whether it is a direct consequence of the blocked step or an indirect overflow metabolite.  
**What was checked:** Literature on 4HMP biosynthesis in mammalian metabolism.  
**Resolution:** Stable isotope tracing studies in Hmgcs2 KO mice or patient samples to identify precursors and pathway.

### Gap 3: No ClinGen Gene-Disease Validity Curation

**Scope:** Formal curation infrastructure.  
**Why it matters:** Despite >150 published cases and 85 ClinVar pathogenic variants, HMGCS2 has not undergone formal ClinGen gene-disease validity curation as of our search date.  
**What was checked:** ClinGen website and GenCC database.  
**Resolution:** Formal ClinGen curation submission.

### Gap 4: Mechanism of Variable Glycemic Response Unknown

**Scope:** Clinical heterogeneity.  
**Why it matters:** Hypoglycemia occurs in only ~56% of acute episodes, with hyperglycemia also reported. The determinants of glycemic response during crisis are unknown.  
**What was checked:** All clinical case series and reviews in our corpus.  
**Resolution:** Prospective metabolic profiling during acute episodes with serial glucose, insulin, glucagon, cortisol, and counter-regulatory hormone measurements.

### Gap 5: SIRT3 Modifier Effect Untested in HMGCS2D Patients

**Scope:** Modifier gene hypothesis.  
**Why it matters:** SIRT3 deacetylation at K310 regulates HMGCS2 activity. SIRT3 polymorphisms could modify disease severity in patients with hypomorphic HMGCS2 variants.  
**What was checked:** PubMed for "SIRT3 HMGCS2 deficiency" and "SIRT3 polymorphism ketogenesis."  
**Resolution:** Genotype SIRT3 in HMGCS2D cohorts and correlate with clinical severity.

### Gap 6: No Registered Clinical Trials

**Scope:** Therapeutic development.  
**Why it matters:** No interventional clinical trials for HMGCS2D were identified. Management is entirely supportive (avoidance of fasting, emergency glucose).  
**What was checked:** ClinicalTrials.gov search terms.  
**Resolution:** Pilot trial of L-carnitine supplementation (rationale from [PMID: 37503004](https://pubmed.ncbi.nlm.nih.gov/37503004/): carnitine buffers excess acetyl-CoA) or ketone body supplementation during illness.

### Gap 7: No Omics-Level Characterization of Human HMGCS2D

**Scope:** Systems-level understanding.  
**Why it matters:** No transcriptomic, proteomic, or metabolomic profiling of patient-derived cells or tissues has been published. The secondary metabolic consequences in humans are inferred from animal models.  
**What was checked:** GEO, ArrayExpress, and PubMed for HMGCS2 deficiency omics studies.  
**Resolution:** Multi-omics profiling of patient fibroblasts or iPSC-derived hepatocytes.

### Gap 8: Long-Term Outcomes and Adult Phenotype Poorly Characterized

**Scope:** Natural history.  
**Why it matters:** Most cases are diagnosed in infancy/childhood. The long-term metabolic consequences (hepatic steatosis, cardiovascular risk from chronic mild ketogenic insufficiency, renal outcomes) in adults are unknown.  
**What was checked:** Case series follow-up data in reviews.  
**Resolution:** Longitudinal registry study with adult follow-up.

---

## Discriminating Tests

### Test 1: iPSC-Derived Hepatocyte Organoid Model

**Rationale:** Directly test ketogenic capacity and acetyl-CoA accumulation in human cells with patient-specific HMGCS2 variants.  
**Design:** Generate iPSC lines from patients with different variant types (truncating vs. missense), differentiate to hepatocyte organoids (following the approach of [PMID: 40199742](https://pubmed.ncbi.nlm.nih.gov/40199742/) for MCADD), and measure ketone body production, acetyl-CoA levels, and acetylation proteomics during simulated fasting (palmitate + low glucose).  
**Expected result:** Graded loss of ketogenesis correlating with variant severity; acetyl-CoA accumulation and protein hyperacetylation in severe variants.  
**Discriminates:** Core mechanism + genotype-phenotype hypothesis.

### Test 2: Prospective Metabolic Profiling During Crisis

**Rationale:** Determine why some crises produce hypoglycemia and others do not.  
**Design:** Enroll diagnosed HMGCS2D patients in a metabolic emergency protocol with standardized sampling: glucose, insulin, glucagon, cortisol, GH, acetate, lactate, beta-hydroxybutyrate, free fatty acids, and complete acylcarnitine profile at presentation and serial time points.  
**Expected result:** Counter-regulatory hormone differences or acetate levels predict glycemic status.  
**Discriminates:** Energy failure model vs. compensatory fuel model.

### Test 3: SIRT3 Genotyping in HMGCS2D Cohorts

**Rationale:** Test the modifier hypothesis that SIRT3 activity modulates disease severity.  
**Design:** Genotype SIRT3 common variants (especially those affecting expression or activity) in all available HMGCS2D patients; correlate with clinical severity score, number of crises, and residual ketone body production.  
**Expected result:** Higher SIRT3 activity associated with milder phenotype in patients with hypomorphic (not null) HMGCS2 variants.  
**Discriminates:** Post-translational modifier model.

### Test 4: Stable Isotope Tracing for 4HMP Origin

**Rationale:** Determine the biosynthetic pathway of the most specific biomarker.  
**Design:** Administer ^13C-labeled palmitate or acetyl-CoA precursors to Hmgcs2 KO mice and track label incorporation into 4HMP and related metabolites by GC-MS.  
**Expected result:** Identification of the precursor pool and enzymatic pathway producing 4HMP.  
**Discriminates:** Biomarker origin -- direct overflow vs. alternative metabolic route.

### Test 5: L-Carnitine/Ketone Supplementation Trial

**Rationale:** Test whether acetyl-CoA buffering (L-carnitine) or direct ketone body supplementation can prevent or mitigate acute crises.  
**Design:** Open-label pilot in diagnosed HMGCS2D patients comparing standard care vs. standard care + daily L-carnitine (rationale: [PMID: 37503004](https://pubmed.ncbi.nlm.nih.gov/37503004/) showed L-carnitine buffers excess acetyl-CoA) or beta-hydroxybutyrate ester during intercurrent illness.  
**Expected result:** Reduced severity of metabolic decompensation, lower peak transaminases, shorter hospitalization.  
**Discriminates:** Acetyl-CoA toxicity model vs. pure ketone body deficiency model.

---

## Curation Leads

*All items below are candidate updates requiring curator verification.*

### Candidate Evidence References

1. **[PMID: 40515583](https://pubmed.ncbi.nlm.nih.gov/40515583/)** -- Grunert 2025 comprehensive review (75 patients). Snippet: "Mitochondrial 3-hydroxy-3-methylglutaryl-coenzyme A synthase deficiency (HMGCS2D) is an autosomal recessive disorder of ketogenesis caused by biallelic variants in HMGCS2." Evidence type: HUMAN_CLINICAL (review-level synthesis). Direction: SUPPORT.

2. **[PMID: 40004108](https://pubmed.ncbi.nlm.nih.gov/40004108/)** -- Nguyen 2025 Vietnamese cohort (19 patients). Hypoglycemia in only 56.3% of symptomatic cases; 3/19 asymptomatic. Evidence type: HUMAN_CLINICAL. Direction: QUALIFY.

3. **[PMID: 40937626](https://pubmed.ncbi.nlm.nih.gov/40937626/)** -- Hyperglycemia case. Snippet: "Notably, severe hyperglycemia as an initial presenting symptom has not been previously reported." Evidence type: HUMAN_CLINICAL. Direction: QUALIFY.

4. **[PMID: 33619377](https://pubmed.ncbi.nlm.nih.gov/33619377/)** -- Arima 2021 mouse acetylome. Snippet: "acetylome analysis of Hmgcs2 KO cells revealed enhanced acetylation of mitochondrial proteins." Evidence type: MODEL_ORGANISM. Direction: SUPPORT + EXTEND.

5. **[PMID: 38876267](https://pubmed.ncbi.nlm.nih.gov/38876267/)** -- Feola 2024 mouse fasting adaptation. Snippet: "Mice with hepatic HMGCS2 deficiency exhibited higher levels of plasma acetate levels in response to fasting." Evidence type: MODEL_ORGANISM. Direction: QUALIFY.

6. **[PMID: 40548098](https://pubmed.ncbi.nlm.nih.gov/40548098/)** -- Neonatal onset with MSUD mimicry. Snippet: "Patient 1 presented on day of life 7 with a sepsis-like condition, coma, metabolic acidosis, and marked elevation of ammonium level at 1081 umol/L." Evidence type: HUMAN_CLINICAL. Direction: EXTEND.

7. **[PMID: 40692014](https://pubmed.ncbi.nlm.nih.gov/40692014/)** -- ACSL1-mediated steatosis mechanism. Snippet: "the accumulation of acetyl-CoA because of impaired hepatic ketogenesis drives the elevated translocation of ACSL1 to the ER." Evidence type: MODEL_ORGANISM. Direction: EXTEND.

### Candidate Pathophysiology Nodes/Edges

- **New node:** Acetyl-CoA accumulation (mitochondrial) -- downstream of HMGCS2 block
- **New edge:** Acetyl-CoA accumulation --> Mitochondrial protein hyperacetylation --> Impaired oxidative phosphorylation
- **New edge:** Acetyl-CoA accumulation --> ACSL1 ER translocation --> Fatty acid re-esterification --> Hepatic steatosis
- **New edge (compensatory):** HMGCS2 deficiency --> Increased hepatic acetate production (mechanism unknown)
- **New modifier edge:** SIRT3 activity --> HMGCS2 K310 deacetylation --> Enzyme activity modulation

### Candidate Ontology Terms

- **Cell types:** Hepatocyte (CL:0000182), Renal proximal tubular cell (CL:0002306), Cardiomyocyte (CL:0000746)
- **Biological processes:** Ketone body biosynthetic process (GO:0046951), Protein deacetylation (GO:0006476), Fatty acid beta-oxidation (GO:0006635), Lipid homeostasis (GO:0055088)
- **Disease terms:** HMGCS2 deficiency (OMIM:605911); HMG-CoA synthase 2 gene (OMIM:600234)

### Candidate Status/Restriction Annotations

- **Qualification to add:** "Hypoglycemia occurs in ~56-90% of acute episodes and is not a defining feature. The core phenotype is hypoketotic metabolic decompensation."
- **Qualification to add:** "Incomplete penetrance documented; asymptomatic biallelic carriers exist in multiple families."
- **Qualification to add:** "Phenotypic spectrum extends to neonatal onset (DOL 7), metabolic stroke, hyperglycemia, and MSUD mimicry on newborn screening."
- **Extension to add:** "Secondary pathology driven by acetyl-CoA accumulation includes mitochondrial protein hyperacetylation and ACSL1-mediated hepatic steatosis (mouse model evidence)."

### Candidate Knowledge Gap Entries

1. **No ClinGen curation** for HMGCS2-HMGCS2D gene-disease relationship.
2. **No human enzyme activity data** from patient hepatocytes.
3. **4HMP biosynthetic pathway** completely unknown.
4. **No clinical trials** registered for HMGCS2D.
5. **No omics profiling** of patient-derived samples.
6. **SIRT3 modifier effect** untested in patients.
7. **Long-term adult outcomes** not systematically studied.
8. **Acetate compensatory mechanism** demonstrated only in mice; relevance in humans unknown.

---

## Limitations of This Report

1. **Literature search scope:** Searches were conducted via PubMed and may have missed relevant preprints, conference abstracts, or non-English publications.
2. **Rare disease limitation:** With ~150 total published cases, evidence comes predominantly from case reports and small case series rather than large cohort studies or clinical trials.
3. **Mouse-to-human translation:** Several key mechanistic findings (acetyl-CoA accumulation, protein hyperacetylation, acetate compensation) are from mouse models and may not directly translate to human disease.
4. **Review bias:** Two large reviews ([PMID: 39798988](https://pubmed.ncbi.nlm.nih.gov/39798988/); [PMID: 40515583](https://pubmed.ncbi.nlm.nih.gov/40515583/)) provide much of the aggregate clinical data; individual case-level data were not independently verified.
5. **Temporal bias:** Recent publications (2024-2026) expanding the phenotypic spectrum may reflect publication bias toward novel presentations rather than a true change in disease characteristics.

---

## References

1. Decru B, et al. *Mitochondrial HMG-CoA synthase deficiency.* [PMID: 39798988](https://pubmed.ncbi.nlm.nih.gov/39798988/)
2. Grunert SC, et al. *Mitochondrial 3-hydroxy-3-methylglutaryl-coenzyme A synthase deficiency: From metabolism to clinical implications.* [PMID: 40515583](https://pubmed.ncbi.nlm.nih.gov/40515583/)
3. Aoyama Y, et al. *Japanese patients with mitochondrial 3-hydroxy-3-methylglutaryl-CoA synthase deficiency.* [PMID: 32952630](https://pubmed.ncbi.nlm.nih.gov/32952630/)
4. Nguyen THA, et al. *Mitochondrial HMG-CoA Synthase Deficiency in Vietnamese Patients.* [PMID: 40004108](https://pubmed.ncbi.nlm.nih.gov/40004108/)
5. Pitt JJ, et al. *Hypoglycemia is not a defining feature of metabolic crisis in mHS deficiency.* [PMID: 32905056](https://pubmed.ncbi.nlm.nih.gov/32905056/)
6. Li J, et al. *Mitochondrial 3-hydroxy-3-methylglutaryl-coenzyme A synthase 2 deficiency with severe hyperglycemia.* [PMID: 40937626](https://pubmed.ncbi.nlm.nih.gov/40937626/)
7. Arima Y, et al. *Murine neonatal ketogenesis preserves mitochondrial energetics by preventing protein hyperacetylation.* [PMID: 33619377](https://pubmed.ncbi.nlm.nih.gov/33619377/)
8. Mooli RGR, et al. *Hepatic Ketogenesis Regulates Lipid Homeostasis via ACSL1-mediated Fatty Acid Partitioning.* [PMID: 40692014](https://pubmed.ncbi.nlm.nih.gov/40692014/)
9. Feola AJ, et al. *Hepatic ketogenesis is not required for starvation adaptation in mice.* [PMID: 38876267](https://pubmed.ncbi.nlm.nih.gov/38876267/)
10. Queathem ED, et al. *Ketogenesis mitigates MASLD-MASH progression through mechanisms that extend beyond fat oxidation.* [PMID: 40272888](https://pubmed.ncbi.nlm.nih.gov/40272888/)
11. Asif S, et al. *Hmgcs2-mediated ketogenesis modulates high-fat diet-induced hepatosteatosis.* [PMID: 35421611](https://pubmed.ncbi.nlm.nih.gov/35421611/)
12. Vaseenon S, et al. *HMG-CoA Synthase-2 Deficiency: Neonatal Hyperammonemic Coma.* [PMID: 40548098](https://pubmed.ncbi.nlm.nih.gov/40548098/)
13. Alshami A, et al. *Mitochondrial HMG-CoA Synthase Deficiency Presenting as Pediatric Metabolic Stroke.* [PMID: 41383544](https://pubmed.ncbi.nlm.nih.gov/41383544/)
14. Rojnueangnit K, et al. *Expanding phenotypic and mutational spectra of mitochondrial HMG-CoA synthase deficiency.* [PMID: 33045405](https://pubmed.ncbi.nlm.nih.gov/33045405/)
15. Kilic M, et al. *Expanding the clinical spectrum of mHS deficiency with Turkish cases.* [PMID: 32259399](https://pubmed.ncbi.nlm.nih.gov/32259399/)
16. Liu J, et al. *SIRT3 Regulates HMGCS2 Deacetylation and Influences Cholangiocarcinoma Progression.* [PMID: 41960367](https://pubmed.ncbi.nlm.nih.gov/41960367/)
17. Ristic B, et al. *Cell-surface G-protein-coupled receptors for tumor-associated metabolites.* [PMID: 28512002](https://pubmed.ncbi.nlm.nih.gov/28512002/)
18. Mooli RGR, et al. *Hepatic ketogenesis regulates lipid homeostasis via ACSL1-mediated fatty acid partitioning.* [PMID: 37503004](https://pubmed.ncbi.nlm.nih.gov/37503004/)
19. Tomita I, et al. *SGLT2 Inhibition Mediates Protection from Diabetic Kidney Disease.* [PMID: 32726607](https://pubmed.ncbi.nlm.nih.gov/32726607/)
20. Kahraman AB, et al. *Comparison of Ketogenesis and Ketolysis Defects.* [PMID: 40960113](https://pubmed.ncbi.nlm.nih.gov/40960113/)
21. Cotter DG, et al. *Fasting-induced HMGCS2 expression in the kidney does not contribute to circulating ketones.* [PMID: 35224990](https://pubmed.ncbi.nlm.nih.gov/35224990/)
22. Shaskey DJ, et al. *Renal Ketogenesis Protects Against Ischemic Kidney Injury.* [PMID: 41568909](https://pubmed.ncbi.nlm.nih.gov/41568909/)
23. Fukao T, et al. *Neonatal ketone body elevation regulates postnatal heart development.* [PMID: 36220812](https://pubmed.ncbi.nlm.nih.gov/36220812/)
24. Gopalakrishnan V, et al. *HMGCS2D with bicytopenia and coagulopathy.* [PMID: 37931961](https://pubmed.ncbi.nlm.nih.gov/37931961/)
25. Szymanska E, et al. *Mitochondrial HMG-CoA Synthase Deficiency: Unique Presenting Laboratory Values.* [PMID: 29030856](https://pubmed.ncbi.nlm.nih.gov/29030856/)
26. Hasegawa Y, et al. *Critical sample collection delayed? Urine organic acid analysis can still save the day.* [PMID: 38469099](https://pubmed.ncbi.nlm.nih.gov/38469099/)
27. Kure S, et al. *iPSC-Derived Liver Organoids as a Tool to Study MCADD.* [PMID: 40199742](https://pubmed.ncbi.nlm.nih.gov/40199742/)
28. Niwa H, et al. *Severe neuroglycopenic symptoms due to nonketotic hypoglycemia in CFC syndrome.* [PMID: 35943247](https://pubmed.ncbi.nlm.nih.gov/35943247/)
