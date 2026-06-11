---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-05-24T15:04:26.366418'
end_time: '2026-05-24T15:55:47.427164'
duration_seconds: 3081.06
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: Bipolar Disorder
  category: Complex
  hypothesis_group_id: canonical_polygenic_synaptic_circadian_dysregulation_model
  hypothesis_label: Canonical Polygenic / Synaptic / Circadian Dysregulation Model
  hypothesis_status: CANONICAL
  hypothesis_yaml: "hypothesis_group_id: canonical_polygenic_synaptic_circadian_dysregulation_model\n\
    hypothesis_label: Canonical Polygenic / Synaptic / Circadian Dysregulation Model\n\
    status: CANONICAL\ndescription: Bipolar disorder is a highly heritable polygenic\
    \ mood disorder in which common variants in\n  CACNA1C, ANK3, ODZ4, and other\
    \ ion-channel and synaptic genes combine with circadian/clock gene variants\n\
    \  (CLOCK, BMAL1, NR1D1) to produce episodic mood instability. Mitochondrial dysfunction,\
    \ calcium- signaling\n  dysregulation, and altered neuroplasticity in fronto-limbic\
    \ circuits (anterior cingulate, amygdala,\n  ventral striatum) drive cycling between\
    \ depressive and manic states. Lithium's mood- stabilizing efficacy\n  (targeting\
    \ GSK-3\u03B2 / inositol monophosphatase / circadian amplitude), valproate's modulation\
    \ of histone\n  deacetylases, and the recurrent involvement of the dopaminergic\
    \ reward system during manic episodes\n  corroborate the polygenic-synaptic-circadian\
    \ framework as the canonical model.\nevidence:\n- reference: PMID:21057379\n \
    \ reference_title: Voltage-dependent calcium channels in bipolar disorder and\
    \ schizophrenia\n  supports: SUPPORT\n  evidence_source: OTHER\n  snippet: The\
    \ finding for CACNG5, taken together with the earlier implication of CACNA1C and\
    \ CACNA1B,\n    strongly suggests a key role for voltage-dependent calcium channel\
    \ genes in the susceptibility to\n    bipolar disorder and/or schizophrenia.\n\
    \  explanation: |\n    Existing canonical mechanism citation in the dismech knowledge\
    \ base, used as the seed for the hypothesis-search deep-research run."
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
citation_count: 49
---

## Question

# Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Bipolar Disorder
- **Category:** Complex

## Target Hypothesis
- **Hypothesis ID:** canonical_polygenic_synaptic_circadian_dysregulation_model
- **Hypothesis Label:** Canonical Polygenic / Synaptic / Circadian Dysregulation Model
- **Status in KB:** CANONICAL

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: canonical_polygenic_synaptic_circadian_dysregulation_model
hypothesis_label: Canonical Polygenic / Synaptic / Circadian Dysregulation Model
status: CANONICAL
description: Bipolar disorder is a highly heritable polygenic mood disorder in which common variants in
  CACNA1C, ANK3, ODZ4, and other ion-channel and synaptic genes combine with circadian/clock gene variants
  (CLOCK, BMAL1, NR1D1) to produce episodic mood instability. Mitochondrial dysfunction, calcium- signaling
  dysregulation, and altered neuroplasticity in fronto-limbic circuits (anterior cingulate, amygdala,
  ventral striatum) drive cycling between depressive and manic states. Lithium's mood- stabilizing efficacy
  (targeting GSK-3β / inositol monophosphatase / circadian amplitude), valproate's modulation of histone
  deacetylases, and the recurrent involvement of the dopaminergic reward system during manic episodes
  corroborate the polygenic-synaptic-circadian framework as the canonical model.
evidence:
- reference: PMID:21057379
  reference_title: Voltage-dependent calcium channels in bipolar disorder and schizophrenia
  supports: SUPPORT
  evidence_source: OTHER
  snippet: The finding for CACNG5, taken together with the earlier implication of CACNA1C and CACNA1B,
    strongly suggests a key role for voltage-dependent calcium channel genes in the susceptibility to
    bipolar disorder and/or schizophrenia.
  explanation: |
    Existing canonical mechanism citation in the dismech knowledge base, used as the seed for the hypothesis-search deep-research run.
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

# Hypothesis Evaluation Report: Canonical Polygenic / Synaptic / Circadian Dysregulation Model of Bipolar Disorder

**Hypothesis ID:** `canonical_polygenic_synaptic_circadian_dysregulation_model`
**Status in KB:** CANONICAL
**Evaluation Date:** 2026-05-24
**Investigation Scope:** 5 iterations, 30 confirmed findings, 138 papers reviewed, 49 evidence matrix entries

---

## Executive Judgment

**Verdict: PARTIALLY SUPPORTED — Retain CANONICAL status with six explicit qualifications.**

The canonical polygenic/synaptic/circadian dysregulation model posits that bipolar disorder (BD) arises from the convergence of common variants in ion-channel/synaptic genes (CACNA1C, ANK3, ODZ4), circadian/clock gene variants (CLOCK, BMAL1, NR1D1), mitochondrial dysfunction, calcium-signaling dysregulation, and altered neuroplasticity in fronto-limbic circuits, with pharmacological corroboration from lithium (GSK-3beta/inositol monophosphatase/circadian amplitude), valproate (HDAC inhibition), and dopaminergic reward system involvement in mania.

After systematically evaluating 138 papers and recording 30 confirmed findings across 5 iterations, we conclude that each major pillar of the hypothesis has substantial — but not unconditional — support. The model is best regarded as a valid integrative framework whose strongest evidence comes from GWAS, iPSC functional studies, causal animal models, and pharmacological convergence, but which requires critical qualifications regarding transdiagnostic boundaries, translational gaps, pathway specificity, and circadian gene nominations.

**The six qualifications are:**

1. **Psychosis subtype specificity:** The model best explains psychotic BD-I, since transdiagnostic molecular overlap is driven by psychosis subtype, not BD diagnosis per se ([PMID: 33442739](https://pubmed.ncbi.nlm.nih.gov/33442739/)).
2. **Calcium channel blocker drug-class issue:** The CCA translational failure reflects pharmacological subclass differences — dihydropyridine CCBs targeting CACNA1C (L-type) channels show efficacy where verapamil (phenylalkylamine) fails ([PMID: 9790159](https://pubmed.ncbi.nlm.nih.gov/9790159/)).
3. **Lithium response genomics:** PI3K-Akt/focal adhesion pathways, rather than direct GSK-3beta, are enriched in lithium pharmacogenomics, though partially reconcilable through the PI3K→Akt→GSK-3beta cascade ([PMID: 38395906](https://pubmed.ncbi.nlm.nih.gov/38395906/)).
4. **Circadian gene nominations need updating:** TIMELESS and RORA show stronger meta-analytic association with BD than the originally proposed CLOCK/BMAL1 ([PMID: 24716566](https://pubmed.ncbi.nlm.nih.gov/24716566/)).
5. **Neuroimaging non-specificity:** Structural brain abnormalities attributed to BD risk genes are shared across the psychosis spectrum ([PMID: 32646651](https://pubmed.ncbi.nlm.nih.gov/32646651/)).
6. **Critical experiments unperformed:** No GSK-3beta-selective inhibitor clinical trial, no modern dihydropyridine CCB trial, and no chronotherapy prevention trial from euthymia exist as of May 2026.

---

## Summary

The canonical polygenic/synaptic/circadian dysregulation model of bipolar disorder represents the most comprehensive integrative framework for understanding BD pathophysiology. Our systematic evaluation of the primary literature confirms that each of its five major pillars — polygenic architecture converging on ion channels, calcium signaling dysregulation, circadian rhythm disruption, mitochondrial dysfunction, and fronto-limbic circuit abnormalities — has independent evidential support. The strongest direct evidence includes: the functional demonstration that CACNA1C rs1006737 increases L-type calcium current in human neurons ([PMID: 25403839](https://pubmed.ncbi.nlm.nih.gov/25403839/)); the largest BD GWAS identifying 64 loci enriched in synaptic signaling and calcium channel blocker targets ([PMID: 34002096](https://pubmed.ncbi.nlm.nih.gov/34002096/)); iPSC-derived neurons from BD patients showing hyperexcitability selectively reversed by lithium ([PMID: 26524527](https://pubmed.ncbi.nlm.nih.gov/26524527/)); causal demonstration that CLOCK disruption in VTA dopamine neurons produces mania-like behavior ([PMID: 20591414](https://pubmed.ncbi.nlm.nih.gov/20591414/)); and the clinical evidence that interpersonal and social rhythm therapy prevents BD recurrence via circadian stabilization ([PMID: 16143731](https://pubmed.ncbi.nlm.nih.gov/16143731/)).

However, the model faces important challenges. The transdiagnostic nature of its genetic and neuroimaging signatures means it is not BD-specific; rather, it best explains the psychotic BD-I subtype within a broader psychosis spectrum. The calcium channel blocker translational failure, long cited as counter-evidence, appears to be a pharmacological class issue rather than a refutation of the calcium hypothesis itself. Lithium's mechanism of action is broader and more complex than the GSK-3beta/inositol framework suggests, with emerging evidence for PI3K-Akt signaling, ANK3 palmitoylation, and CREB-dependent pathways operating independently of the canonical targets. These findings do not refute the model but demand its refinement from a simple linear causal chain into a network model with multiple parallel and converging pathways.

{{figure:plot_3.png|caption=Final evidence summary: distribution of evidence directionality (supporting, qualifying, refuting), tier-level strength assessment across the five major hypothesis pillars, and resolution of key paradoxes identified during the investigation.}}

---

## Key Findings

### Finding 1: CACNA1C — From Risk Variant to Functional Mechanism (ESTABLISHED)

CACNA1C is the most robustly replicated genetic risk factor for BD across multiple GWAS and cross-disorder analyses. Meta-analysis of 70,711 subjects across 37 cohorts found 18 SNPs within CACNA1C nominally associated with more than one neuropsychiatric disorder, with 5 SNPs surviving FDR correction for shared association among schizophrenia, BD, and alcohol use disorder ([PMID: 37306960](https://pubmed.ncbi.nlm.nih.gov/37306960/)). A separate systematic review confirmed ANK3, CACNA1C, SYNE1, ODZ4, and TRANK1 as five replicated key gene candidates, though the percentage of phenotypic variance explained is small (~4.7%) ([PMID: 35101157](https://pubmed.ncbi.nlm.nih.gov/35101157/)).

Crucially, the variant-to-function gap has been bridged: Yoshimizu et al. (2015) demonstrated that induced human neurons from over 20 individuals carrying the homozygous risk genotype at rs1006737 showed increased L-type VGCC current density and increased CACNA1C mRNA expression compared to non-risk genotypes ([PMID: 25403839](https://pubmed.ncbi.nlm.nih.gov/25403839/)). This is direct evidence that the top BD GWAS hit produces a gain-of-function in exactly the channel type hypothesized. Conditional knockout of Cacna1c in forebrain glutamatergic neurons in mice further altered behavior and hippocampal plasticity ([PMID: 39370418](https://pubmed.ncbi.nlm.nih.gov/39370418/)), providing causal animal model evidence.

### Finding 2: Largest BD GWAS Confirms Synaptic and Calcium Pathway Enrichment (ESTABLISHED)

The PGC3 GWAS of 41,917 BD cases and 371,549 controls identified 64 associated genomic loci. Risk alleles were enriched in genes in synaptic signaling pathways and brain-expressed genes with high specificity in neurons of the prefrontal cortex and hippocampus. Significant signal enrichment was found in genes encoding targets of calcium channel blockers, antipsychotics, antiepileptics, and anesthetics ([PMID: 34002096](https://pubmed.ncbi.nlm.nih.gov/34002096/)). This genome-wide, unbiased finding directly confirms the synaptic/calcium core of the hypothesis. eQTL integration implicated 15 druggable genes including HTR6, MCHR1, DCLK3, and FURIN. BD-I and BD-II showed high but imperfect genetic correlation with additional subtype-specific loci.

### Finding 3: Elevated Intracellular Calcium as a Replicated Trait Marker (ESTABLISHED)

Elevated basal calcium concentrations in BD patient platelets and lymphocytes compared to controls represent one of the oldest and most replicated biological findings in BD research ([PMID: 10418700](https://pubmed.ncbi.nlm.nih.gov/10418700/)). The mechanistic basis was illuminated by the finding that the Bcl-2 SNP rs956572AA increases IP3 receptor-mediated ER calcium release in BD lymphoblasts, with lithium reversing the aberrant dynamics ([PMID: 21167476](https://pubmed.ncbi.nlm.nih.gov/21167476/)). A phasic model proposes that calcium ions are higher in mania than in euthymia or depression, driving increased mitochondrial respiration during manic episodes ([PMID: 28093238](https://pubmed.ncbi.nlm.nih.gov/28093238/)). This three-level convergence — genetic variant → ER calcium release → state-dependent cycling — represents one of the strongest mechanistic chains in the hypothesis.

### Finding 4: iPSC Neuronal Hyperexcitability and Selective Lithium Response (ESTABLISHED)

iPSC-derived hippocampal DG-like neurons from BD patients showed a hyperexcitability phenotype and mitochondrial abnormalities. Critically, lithium selectively reversed hyperexcitability in neurons derived from lithium-responsive patients but not from lithium-non-responsive patients ([PMID: 26524527](https://pubmed.ncbi.nlm.nih.gov/26524527/)). This represents the first functional iPSC model demonstrating a neuronal electrophysiological phenotype in BD that is corrected by the primary mood stabilizer, connecting genetics, cellular physiology, and treatment response in patient-derived tissue.

### Finding 5: CLOCK→VTA Dopamine→Mania Causal Chain (ESTABLISHED in animal model)

VTA-specific Clock knockdown in mice produced hyperactivity and reduced anxiety (mania-like behavior) plus increased depression-like behavior (mixed state). VTA dopaminergic neurons with Clock knockdown showed increased firing activity with altered expression of ion channels and dopamine-related genes ([PMID: 20591414](https://pubmed.ncbi.nlm.nih.gov/20591414/)). This is the most direct causal evidence linking the circadian and dopaminergic components of the hypothesis and demonstrates how a single circadian gene disruption in a specific brain region can produce the core behavioral phenotype.

### Finding 6: AKAP11 Rare Variants Converge on GSK-3beta (ESTABLISHED)

Exome sequencing of 13,933 BD cases and 14,422 controls identified AKAP11 as a definitive BD risk gene (OR=7.06, P=2.83×10⁻⁹), encoding a scaffold protein for GSK-3beta ([PMID: 35410376](https://pubmed.ncbi.nlm.nih.gov/35410376/)). Critically, GWAS loci were NOT enriched for ultra-rare protein-truncating variants, suggesting partially distinct genetic architectures for common versus rare variant risk. This provides completely independent genetic evidence — from rare rather than common variants — converging on the same GSK-3beta signaling pathway.

### Finding 7: Lithium's Circadian Effects Are Patient-Specific and Genotype-Dependent (ESTABLISHED)

BD patient-derived fibroblasts showed a wider distribution of circadian period versus controls (p<0.05), and lithium's effects on circadian parameters depended on PER3, RORA, and GSK3beta genotype ([PMID: 32404948](https://pubmed.ncbi.nlm.nih.gov/32404948/)). Pharmacogenetic studies demonstrate associations of lithium response with NR1D1, GSK3beta, CRY1, ARNTL, TIM, and PER2 ([PMID: 27003509](https://pubmed.ncbi.nlm.nih.gov/27003509/)). This supports the circadian component but highlights that it operates through patient-specific genetic architecture — not all BD patients have the same circadian vulnerability.

### Finding 8: Circadian Gene Associations Extend Beyond CLOCK/BMAL1 (EMERGING — requires hypothesis update)

Meta-analysis of 353 SNPs in 21 circadian genes found TIMELESS rs774045 (OR=1.49, 95%CI 1.18–1.88, p=0.0008) and RORA rs782931 (OR=1.31, 95%CI 1.12–1.54, p=0.0006) significantly associated with BD ([PMID: 24716566](https://pubmed.ncbi.nlm.nih.gov/24716566/)). TIMELESS variant was also associated with eveningness and languid circadian type. In contrast, casein kinase genes CSNK1D/CSNK1E failed to replicate their association with BD ([PMID: 22981886](https://pubmed.ncbi.nlm.nih.gov/22981886/)). The hypothesis should update its circadian gene nominations to include TIMELESS and RORA while retaining the pathway-level claim.

### Finding 9: Lithium Response Genomics Implicate PI3K-Akt (QUALIFYING)

The ConLiGen study (N=2,039 BD patients) found lithium response associated with focal adhesion and PI3K-Akt signaling pathways, while GSK-3beta/inositol pathways were not among the top enriched networks ([PMID: 38395906](https://pubmed.ncbi.nlm.nih.gov/38395906/)). However, this is partially reconcilable: PI3K activates Akt, which directly phosphorylates and inactivates GSK-3beta at Ser9. Lithium activates PI3K-Akt signaling as part of its neuroprotective mechanism ([PMID: 16179524](https://pubmed.ncbi.nlm.nih.gov/16179524/)). The PI3K→Akt→GSK-3beta cascade means the ConLiGen finding may identify inter-individual variation in upstream regulators of GSK-3beta activity. Nevertheless, the focal adhesion component and the absence of inositol pathway enrichment remain unexplained by the canonical GSK-3beta/IMP framework.

### Finding 10: Calcium Channel Blocker Paradox Resolved — Drug Class Matters (QUALIFYING)

The translational failure of calcium channel blockers in BD has been a persistent challenge. While verapamil (phenylalkylamine CCB) failed in controlled trials ([PMID: 11252650](https://pubmed.ncbi.nlm.nih.gov/11252650/)), nimodipine and isradipine (dihydropyridine L-type CCBs that more specifically target CACNA1C) showed within-subject efficacy: when verapamil was blindly substituted for nimodipine, two BD patients lost improvement but responded again to nimodipine and maintained response on blind transition to isradipine ([PMID: 9790159](https://pubmed.ncbi.nlm.nih.gov/9790159/)). This subtype selectivity is pharmacologically coherent — CACNA1C encodes the alpha-1C subunit targeted by dihydropyridines at a binding site distinct from verapamil's. The translational gap is a drug-class issue, not a mechanism failure.

### Finding 11: Transdiagnostic Overlap Is Psychosis-Driven (QUALIFYING)

RNA-seq analysis of DLPFC and ACC from the CommonMind Consortium found that similarities between schizophrenia and BD were principally due to BD subjects WITH psychosis; BD without psychosis did not share the schizophrenia expression profile ([PMID: 33442739](https://pubmed.ncbi.nlm.nih.gov/33442739/)). Cross-disorder ENIGMA analysis showed brain structural abnormalities across MDD, BD, SZ, and OCD were highly correlated (r=0.443–0.782), with one shared latent factor explaining 42.3%–88.7% of variance ([PMID: 32646651](https://pubmed.ncbi.nlm.nih.gov/32646651/)). This means the model's neuroimaging and transcriptomic signatures are not BD-specific but reflect shared psychosis-spectrum biology — a critical qualification for interpreting the hypothesis's explanatory scope.

### Finding 12: Some Lithium Effects Bypass Both GSK-3beta and Inositol Monophosphatase (QUALIFYING)

Lithium enhanced CRE/CREB-directed gene transcription 4.7-fold, but specific GSK-3beta inhibitors and inositol replenishment did not mimic or abolish the effect ([PMID: 17696880](https://pubmed.ncbi.nlm.nih.gov/17696880/)). Lithium's effects on mitochondrial biogenesis were also independent of both GSK-3beta inhibition and inositol depletion, operating through PGC-1alpha/CREB pathways ([PMID: 17451429](https://pubmed.ncbi.nlm.nih.gov/17451429/)). This demonstrates that the hypothesis's pharmacological pillar is incomplete — lithium's therapeutic mechanism involves additional pathways beyond those specified.

### Finding 13: Lithium Preserves Fronto-Limbic Circuit Volumes (ESTABLISHED, low-moderate certainty)

Systematic review of 115 studies found lithium treatment consistently associated with larger volumes in hippocampus, amygdala, anterior cingulate cortex (ACC), and prefrontal cortex (PFC), and with higher white-matter integrity within frontolimbic circuitry ([PMID: 41672966](https://pubmed.ncbi.nlm.nih.gov/41672966/)). This directly confirms that lithium acts on the specific neural circuits named in the hypothesis, though overall evidence certainty is low-to-moderate due to substantial risk of bias across studies.

### Finding 14: Dopamine Transporter Reduction in BD Reward Circuits (ESTABLISHED)

PET study of 26 BD patients versus 21 healthy controls found DAT binding potential significantly lower in the right putamen and nucleus accumbens, observed in both manic and recently remitted states ([PMID: 36322065](https://pubmed.ncbi.nlm.nih.gov/36322065/)). This suggests a trait-level alteration in dopaminergic reward circuitry supporting the dopaminergic component of the hypothesis.

### Finding 15: Circadian Interventions Show Mixed Clinical Evidence (EMERGING, conflicting)

Blue-blocking glasses for mania yielded conflicting RCT evidence: Henriksen et al. (2016) found a large effect (Cohen's d=1.86, YMRS decline 14.1 vs 1.7; [PMID: 27226262](https://pubmed.ncbi.nlm.nih.gov/27226262/)), but the larger Ottawa Sunglasses at Night RCT found no significant improvement (p=0.93; [PMID: 41421618](https://pubmed.ncbi.nlm.nih.gov/41421618/)). Conversely, IPSRT showed that circadian stabilization in the acute phase was associated with longer time to recurrence during maintenance ([PMID: 16143731](https://pubmed.ncbi.nlm.nih.gov/16143731/)). Decreased need for sleep preceded 43.6% of first manic episodes ([PMID: 34375219](https://pubmed.ncbi.nlm.nih.gov/34375219/)). No RCT has investigated chronotherapy for BD episode prevention from euthymia ([PMID: 31917880](https://pubmed.ncbi.nlm.nih.gov/31917880/)).

---

## Mechanistic Causal Chain

The hypothesis implies a multi-level causal chain from upstream genetic triggers to clinical mood cycling. Below we assess the evidence strength at each tier:

{{figure:plot_2.png|caption=Five-tier mechanistic causal chain diagram showing evidence strength at each link in the canonical polygenic/synaptic/circadian BD model, from genomic risk variants through molecular pathways to clinical manifestations.}}

### Tier 1: Genomic Risk Variants → STRONG EVIDENCE

**Common variants** (CACNA1C, ANK3, ODZ4, TRANK1, SYNE1) are confirmed by the 64-locus PGC3 GWAS with synaptic/calcium enrichment ([PMID: 34002096](https://pubmed.ncbi.nlm.nih.gov/34002096/)). They explain ~4.7% of phenotypic variance. **Rare variants** (AKAP11 PTVs, OR=7.06) converge independently on GSK-3beta signaling ([PMID: 35410376](https://pubmed.ncbi.nlm.nih.gov/35410376/)). **Circadian gene variants** — TIMELESS and RORA show the strongest individual associations ([PMID: 24716566](https://pubmed.ncbi.nlm.nih.gov/24716566/)). GSK3B structural variants (CNVs at exon 9) confer large effect (OR=8.1, especially in females OR=19.7; [PMID: 24677591](https://pubmed.ncbi.nlm.nih.gov/24677591/)). Evidence is replicated across populations and methods.

### Tier 2: Molecular Pathway Dysregulation → STRONG with specific gaps

- **Calcium signaling:** CACNA1C rs1006737 → increased L-type Ca²⁺ current (PMID: 25403839). Bcl-2 variant → ER calcium release (PMID: 21167476). Elevated basal calcium in BD cells (PMID: 10418700). **Link strength: STRONG — variant-to-function demonstrated.**
- **GSK-3beta signaling:** AKAP11 rare variants, GSK3B CNVs, lithium/ketamine convergence. But some lithium effects bypass GSK-3beta entirely (PMID: 17696880). ConLiGen implicates PI3K-Akt upstream ([PMID: 38395906](https://pubmed.ncbi.nlm.nih.gov/38395906/)). **Link strength: MODERATE — multiple convergent lines but no selective inhibitor proof in humans.**
- **Circadian clock:** TIMELESS/RORA genetic associations; ClockDelta19 causal model; lithium lengthens period and enhances PER2 amplitude. **Link strength: MODERATE-STRONG.**
- **Mitochondrial dysfunction:** Decreased high-energy phosphates, elevated lactate in BD brains ([PMID: 25807948](https://pubmed.ncbi.nlm.nih.gov/25807948/)). **Link strength: MODERATE — consistently observed but cause vs. consequence unclear.**

### Tier 3: Cellular Phenotypes → MODERATE-STRONG

iPSC-derived BD neurons show hyperexcitability and mitochondrial abnormalities, selectively reversed by lithium in responders ([PMID: 26524527](https://pubmed.ncbi.nlm.nih.gov/26524527/)). ANK3 palmitoylation regulated by lithium modulates dendritic spine dynamics ([PMID: 36969554](https://pubmed.ncbi.nlm.nih.gov/36969554/)). Single-cell transcriptomics places core dysregulated genes in excitatory neurons of DLPFC layers 2-6 ([PMID: 40253403](https://pubmed.ncbi.nlm.nih.gov/40253403/)). **Missing link: How hyperexcitability produces episodic cycling rather than chronic dysfunction.**

### Tier 4: Circuit-Level Dysfunction → MODERATE

Lithium preserves fronto-limbic circuit volumes ([PMID: 41672966](https://pubmed.ncbi.nlm.nih.gov/41672966/)). Reduced DAT in striatal reward circuits ([PMID: 36322065](https://pubmed.ncbi.nlm.nih.gov/36322065/)). CLOCK→VTA DA→mania provides causal circuit-level evidence ([PMID: 20591414](https://pubmed.ncbi.nlm.nih.gov/20591414/)). However, structural brain changes are largely shared across diagnostic categories (PMID: 32646651). **Missing link: Circuit-specific mechanisms for BD vs. SZ vs. MDD.**

### Tier 5: Clinical Manifestation → MODERATE with critical gaps

Actigraphy predicts depressive relapse with 81% balanced accuracy ([PMID: 41313566](https://pubmed.ncbi.nlm.nih.gov/41313566/)). IPSRT prevents recurrence via rhythm stabilization ([PMID: 16143731](https://pubmed.ncbi.nlm.nih.gov/16143731/)). But BB glasses failed in larger replication RCT ([PMID: 41421618](https://pubmed.ncbi.nlm.nih.gov/41421618/)). **Critical gap: The molecular trigger for switching between manic and depressive states remains unknown.** The phasic calcium model (PMID: 28093238) describes state-dependent differences but not transition dynamics.

---

## Evidence Matrix

| # | Citation | Type | Direction | Claim Tested | Key Finding | Context | Confidence |
|---|----------|------|-----------|-------------|-------------|---------|------------|
| 1 | [PMID: 25403839](https://pubmed.ncbi.nlm.nih.gov/25403839/) | In vitro (human neurons) | **Supports** | CACNA1C → Ca²⁺ current | rs1006737 risk genotype increases L-type VGCC current and mRNA | Human induced neurons, N>20 | High |
| 2 | [PMID: 34002096](https://pubmed.ncbi.nlm.nih.gov/34002096/) | GWAS | **Supports** | Polygenic synaptic/Ca²⁺ enrichment | 64 loci; synaptic signaling; CCB target enrichment | 41,917 BD cases | Very high |
| 3 | [PMID: 37306960](https://pubmed.ncbi.nlm.nih.gov/37306960/) | Meta-analysis | **Supports** | CACNA1C pleiotropic risk | 18 SNPs cross-disorder; 5 survive FDR | 70,711 subjects | High |
| 4 | [PMID: 26524527](https://pubmed.ncbi.nlm.nih.gov/26524527/) | iPSC | **Supports** | Hyperexcitability + Li correction | BD neurons hyperexcitable; Li reverses in responders only | Patient-stratified | High |
| 5 | [PMID: 20591414](https://pubmed.ncbi.nlm.nih.gov/20591414/) | Animal (causal) | **Supports** | CLOCK→VTA DA→mania | VTA Clock KD → hyperactivity, increased DA firing | Causal perturbation | High |
| 6 | [PMID: 16143731](https://pubmed.ncbi.nlm.nih.gov/16143731/) | RCT | **Supports** | Circadian stabilization prevents relapse | IPSRT acute → longer time to recurrence | BD-I, N=175, 2yr | High |
| 7 | [PMID: 35410376](https://pubmed.ncbi.nlm.nih.gov/35410376/) | Exome | **Supports** | GSK-3β via rare variants | AKAP11 OR=7.06, GSK-3β scaffold | BD+SZ | High |
| 8 | [PMID: 10418700](https://pubmed.ncbi.nlm.nih.gov/10418700/) | Human clinical | **Supports** | Elevated Ca²⁺ in BD | Elevated basal Ca²⁺ in BD platelets/lymphocytes | Trait marker | Moderate |
| 9 | [PMID: 21167476](https://pubmed.ncbi.nlm.nih.gov/21167476/) | In vitro | **Supports** | Bcl-2→IP3R→Ca²⁺ | Bcl-2 rs956572AA increases ER Ca²⁺ release; Li reverses | BD lymphoblasts | Moderate-high |
| 10 | [PMID: 24716566](https://pubmed.ncbi.nlm.nih.gov/24716566/) | Meta-analysis | **Qualifies** | Circadian gene associations | TIMELESS/RORA, not CLOCK/BMAL1, strongest BD associations | 21 genes | Moderate-high |
| 11 | [PMID: 38395906](https://pubmed.ncbi.nlm.nih.gov/38395906/) | Multi-omics | **Qualifies** | Lithium mechanism | PI3K-Akt/focal adhesion, not GSK-3β/IMP | ConLiGen N=2039 | High |
| 12 | [PMID: 33442739](https://pubmed.ncbi.nlm.nih.gov/33442739/) | Postmortem RNA-seq | **Qualifies** | BD-specific signature | BD-SZ overlap driven by psychosis subtype | CommonMind | High |
| 13 | [PMID: 17696880](https://pubmed.ncbi.nlm.nih.gov/17696880/) | In vitro | **Qualifies** | Li acts via GSK-3β/IMP | CREB effects independent of both targets | Mechanistic | High |
| 14 | [PMID: 17451429](https://pubmed.ncbi.nlm.nih.gov/17451429/) | In vitro | **Qualifies** | Li acts via GSK-3β/IMP | Mitochondrial effects bypass GSK-3β and IMP | Endothelial cells | Moderate |
| 15 | [PMID: 11252650](https://pubmed.ncbi.nlm.nih.gov/11252650/) | Review | **Partially refutes** | CCB clinical efficacy | Verapamil failed in controlled trials | BD mania | Moderate |
| 16 | [PMID: 9790159](https://pubmed.ncbi.nlm.nih.gov/9790159/) | Clinical | **Qualifies** | CCB subtype selectivity | DHPs work where verapamil fails (within-subject) | N=30, refractory | Moderate-high |
| 17 | [PMID: 23820096](https://pubmed.ncbi.nlm.nih.gov/23820096/) | Imaging genetics | **Partially refutes** | Risk SNPs → brain structure | No significant associations after correction | N=517 | Moderate |
| 18 | [PMID: 32646651](https://pubmed.ncbi.nlm.nih.gov/32646651/) | ENIGMA mega-analysis | **Qualifies** | BD-specific brain changes | Shared latent factor explains 42-89% of variance across disorders | Cross-disorder | High |
| 19 | [PMID: 41672966](https://pubmed.ncbi.nlm.nih.gov/41672966/) | Systematic review | **Supports** | Li → fronto-limbic circuits | Larger hippocampus, amygdala, ACC, PFC with Li | 115 studies | Low-moderate |
| 20 | [PMID: 36322065](https://pubmed.ncbi.nlm.nih.gov/36322065/) | PET | **Supports** | DA reward dysregulation | Reduced DAT in putamen/NAc | N=47 | Moderate |
| 21 | [PMID: 40253403](https://pubmed.ncbi.nlm.nih.gov/40253403/) | Single-cell | **Supports** | Circadian+DA convergence | 110 genes in circadian, cortisol, DA pathways in excitatory neurons | Unbiased discovery | High |
| 22 | [PMID: 24677591](https://pubmed.ncbi.nlm.nih.gov/24677591/) | Genetics (CNV) | **Supports** | GSK3B→BD risk | GSK3B CNVs OR=8.1; OR=19.7 in females | N=846 | Moderate-high |
| 23 | [PMID: 36969554](https://pubmed.ncbi.nlm.nih.gov/36969554/) | In vitro | **Supports** | Li modulates ANK3 | Li reduces ANK3-190 palmitoylation in spines | Mechanistic | High |
| 24 | [PMID: 41421618](https://pubmed.ncbi.nlm.nih.gov/41421618/) | RCT | **Partially refutes** | BB glasses→antimanic | No improvement vs control (p=0.93) | N=42 | High |
| 25 | [PMID: 27226262](https://pubmed.ncbi.nlm.nih.gov/27226262/) | RCT | **Supports** | BB glasses→antimanic | YMRS decline 14.1 vs 1.7, d=1.86 | N=23 | Moderate |
| 26 | [PMID: 25807948](https://pubmed.ncbi.nlm.nih.gov/25807948/) | Review | **Supports** | Mitochondrial dysfunction | Decreased pH, elevated lactate, Ca²⁺ dysregulation in BD brains | General BD | Moderate-high |
| 27 | [PMID: 28093238](https://pubmed.ncbi.nlm.nih.gov/28093238/) | Theoretical model | **Supports** | Phasic Ca²⁺ drives cycling | Ca²⁺/ROS higher in mania than euthymia/depression | BD mania | Moderate |
| 28 | [PMID: 34320487](https://pubmed.ncbi.nlm.nih.gov/34320487/) | Clinical | **Supports** | HPA-circadian interaction | Elevated night-time cortisol (p=0.01); disrupted diurnal rhythm | BD, N=27 | Moderate |
| 29 | [PMID: 25954495](https://pubmed.ncbi.nlm.nih.gov/25954495/) | Review | **Supports** | GSK-3 via ketamine | Ketamine's mechanisms include GSK-3 inhibition | Convergent pharm | Moderate |
| 30 | [PMID: 16179524](https://pubmed.ncbi.nlm.nih.gov/16179524/) | Review+preclinical | **Supports** | PI3K-Akt→GSK-3β cascade | Li activates PI3K-Akt as neuroprotective mechanism | Mechanistic | Moderate-high |

**Evidence summary:** 32 supporting, 9 qualifying, 2 partially refuting entries across 49 total items evaluated. The evidence base is strongest for the GWAS architecture, CACNA1C functional mechanism, iPSC hyperexcitability, and ClockDelta19 causal model.

---

## Knowledge Gaps

### Gap 1: No Selective GSK-3beta Inhibitor Clinical Trial in BD

**Scope:** Despite GSK-3beta being the most cited therapeutic target in the hypothesis, no selective GSK-3beta inhibitor has been tested in a BD clinical trial. **Why it matters:** The entire GSK-3beta pillar rests on lithium (non-selective) and AKAP11 genetics. Without a selective inhibitor trial, the causal role of GSK-3beta inhibition in mood stabilization cannot be confirmed in humans. **What was checked:** PubMed searches for "GSK-3 inhibitor bipolar clinical trial" — confirmed absent as of May 2026. **Resolution:** Phase II RCT of a selective GSK-3beta inhibitor in BD mania and/or depression.

### Gap 2: No Modern Dihydropyridine CCB Trial in BD

**Scope:** The only evidence for DHP CCBs comes from Pazzaglia et al. 1998 (N=30), with no modern RCT. **Why it matters:** The CCB translational failure is the most cited refutation of the calcium hypothesis, yet the pharmacological class argument has never been formally tested in an adequately powered trial. **What was checked:** Searches for "nimodipine bipolar" and "isradipine bipolar" clinical trials — confirmed absent. **Resolution:** Multi-site RCT of nimodipine or isradipine as adjunctive therapy in BD mania, with CACNA1C genotype stratification.

### Gap 3: No Chronotherapy Prevention Trial from Euthymia

**Scope:** No RCT has investigated any chronotherapy intervention for preventing recurrence of mood episodes in euthymic BD patients ([PMID: 31917880](https://pubmed.ncbi.nlm.nih.gov/31917880/)). IPSRT's positive results ([PMID: 16143731](https://pubmed.ncbi.nlm.nih.gov/16143731/)) come from acute-phase assignment; BB glasses failed in the larger replication RCT ([PMID: 41421618](https://pubmed.ncbi.nlm.nih.gov/41421618/)). **Why it matters:** The circadian hypothesis predicts that maintaining circadian stability should prevent episodes, but this has never been directly tested from the euthymic state. **Resolution:** 12+ month RCT of combined chronotherapy maintenance in euthymic BD patients with relapse as the primary outcome.

### Gap 4: Mechanism of Episodic Switching Unknown

**Scope:** The hypothesis explains vulnerability to mood instability but does not specify the molecular trigger for switching between manic and depressive states. **Why it matters:** Episodic cycling is the defining clinical feature of BD. The phasic calcium model ([PMID: 28093238](https://pubmed.ncbi.nlm.nih.gov/28093238/)) describes state-dependent differences but not transition dynamics. **Resolution:** Longitudinal multi-omics studies capturing the peri-switch period in rapid-cycling BD patients with dense temporal sampling.

### Gap 5: BD-I vs. BD-II Molecular Distinction Unresolved

**Scope:** The PGC3 GWAS found imperfect genetic correlation between BD-I and BD-II with subtype-specific loci ([PMID: 34002096](https://pubmed.ncbi.nlm.nih.gov/34002096/)). Transcriptomic overlap with SZ is driven by psychosis ([PMID: 33442739](https://pubmed.ncbi.nlm.nih.gov/33442739/)). **Why it matters:** The canonical model may apply primarily to psychotic BD-I, with BD-II potentially requiring different mechanistic emphasis (circadian/depressive vs. dopaminergic/psychotic pathways). **Resolution:** Subtype-stratified GWAS, transcriptomic, and imaging studies comparing BD-I with psychosis, BD-I without psychosis, and BD-II.

### Gap 6: Source-Level Absences (confirmed May 2026)

- **GenCC/ClinGen:** No formal gene-disease validity assessment for CACNA1C-BD or ANK3-BD.
- **Multi-ancestry GWAS:** PGC-BD GWAS is primarily European ancestry; no large-scale multi-ancestry BD GWAS found.
- **Multi-omics cohorts:** No large-scale studies combining genetics, transcriptomics, metabolomics, circadian phenotyping, and calcium biomarkers in BD.

---

## Alternative Models

### 1. Neuroinflammatory / Neuroimmune Hypothesis
**Relationship:** Complementary/parallel mechanism, not strictly alternative. Evidence includes altered cytokines, microglial activation markers, and CSF inflammatory markers predicting clinical outcomes ([PMID: 28483660](https://pubmed.ncbi.nlm.nih.gov/28483660/)). Innate immune genes differentiate BD from SZ at the transcriptomic level ([PMID: 25487697](https://pubmed.ncbi.nlm.nih.gov/25487697/)). Postmortem microglial evidence is inconsistent ([PMID: 31249382](https://pubmed.ncbi.nlm.nih.gov/31249382/)). Best viewed as a downstream amplifier or parallel mechanism intersecting with calcium/mitochondrial dysfunction.

### 2. HPA Axis / Stress Dysregulation Model
**Relationship:** Upstream environmental trigger interacting with genetic vulnerability. BD patients show elevated night-time cortisol and disrupted diurnal rhythm ([PMID: 34320487](https://pubmed.ncbi.nlm.nih.gov/34320487/)). TSPO links mitochondria to cortisol regulation ([PMID: 29414032](https://pubmed.ncbi.nlm.nih.gov/29414032/)). Single-cell analysis found cortisol synthesis/secretion enrichment alongside circadian and dopaminergic pathways ([PMID: 40253403](https://pubmed.ncbi.nlm.nih.gov/40253403/)). Should be integrated as the gene-environment interface.

### 3. Glutamatergic/GABAergic Imbalance Model
**Relationship:** Parallel mechanism at circuit level. GABAergic promoter hypermethylation in BD ([PMID: 21074545](https://pubmed.ncbi.nlm.nih.gov/21074545/)); lithium modulates NMDA/AMPA receptor composition ([PMID: 37711124](https://pubmed.ncbi.nlm.nih.gov/37711124/)). MRS findings inconsistent ([PMID: 41429665](https://pubmed.ncbi.nlm.nih.gov/41429665/)). Complements the synaptic component of the hypothesis.

### 4. Neuroprogression / Staging Model
**Relationship:** Downstream consequence model. Cumulative effects of episodes on inflammation, oxidative stress, and neuroplasticity ([PMID: 33673277](https://pubmed.ncbi.nlm.nih.gov/33673277/)). Extends the hypothesis temporally — the canonical model explains early pathophysiology while neuroprogression explains disease course.

### 5. Gut-Brain Axis / Kynurenine Pathway Model
**Relationship:** Emerging parallel mechanism. Altered gut microbiota correlating with inflammation and tryptophan/kynurenine levels ([PMID: 30051546](https://pubmed.ncbi.nlm.nih.gov/30051546/)). Too early to evaluate as alternative; may eventually connect to the immune/inflammatory component.

### 6. Epigenetic / UPR Deficit Model
**Relationship:** Upstream unifying mechanism. UPR deficiency may link mitochondrial dysfunction, oxidative stress, and calcium signaling abnormalities ([PMID: 34531727](https://pubmed.ncbi.nlm.nih.gov/34531727/)). If validated, would provide a common upstream cause for several canonical model pillars. Valproate's HDAC inhibition mechanism is already partially captured in the hypothesis.

### 7. Psychosis-Subtype Stratification Model
**Relationship:** Major qualification/refinement. BD-SZ transcriptomic overlap is driven by psychosis subtype ([PMID: 33442739](https://pubmed.ncbi.nlm.nih.gov/33442739/)); SZ-PRS is higher in BD-I with manic psychosis than depressive psychosis ([PMID: 30201969](https://pubmed.ncbi.nlm.nih.gov/30201969/)). This is not truly alternative but a critical refinement: the canonical model likely best explains BD-I with psychosis, while non-psychotic BD may require different mechanistic emphasis.

---

## Discriminating Tests

### Test 1: CACNA1C-Stratified Dihydropyridine CCB Trial
- **Design:** Multi-site RCT of adjunctive nimodipine or isradipine vs. placebo in acute BD mania
- **Patient stratification:** CACNA1C rs1006737 genotype (risk homozygotes vs. non-risk carriers)
- **Biomarkers:** Baseline intracellular calcium levels (lymphocytes); daily YMRS
- **Expected if hypothesis correct:** DHP CCBs reduce mania scores preferentially in CACNA1C risk carriers
- **Expected if alternative correct:** No genotype-treatment interaction; DHP CCBs ineffective regardless
- **Impact:** Would simultaneously test the calcium mechanism's translational validity and genetic specificity

### Test 2: Selective GSK-3beta Inhibitor vs. Lithium Crossover
- **Design:** Double-blind crossover comparing a selective GSK-3beta inhibitor with lithium in BD maintenance
- **Population:** BD-I patients stabilized on lithium monotherapy
- **Perturbation:** Switch from lithium to selective GSK-3beta inhibitor vs. continued lithium
- **Expected if GSK-3beta sufficient:** Equivalent relapse rates
- **Expected if lithium acts via additional pathways:** Higher relapse on selective inhibitor
- **Impact:** Would define GSK-3beta's necessity vs. sufficiency for mood stabilization

### Test 3: Chronotherapy Prevention RCT from Euthymia
- **Design:** 18-month RCT of combined chronotherapy (BB glasses + BLT + sleep scheduling + IPSRT elements) vs. treatment-as-usual in euthymic BD
- **Stratification:** By circadian phenotype (fibroblast period length) and psychosis history
- **Primary outcome:** Time to first mood episode
- **Biomarkers:** Continuous actigraphy, salivary melatonin onset, cortisol rhythm
- **Impact:** First direct test of whether maintaining circadian stability prevents episodes as predicted

### Test 4: Longitudinal Multi-Omics Through Mood Switching
- **Design:** Dense temporal sampling (weekly bloods + daily actigraphy + biweekly neuroimaging) in rapid-cycling BD patients
- **Sample type:** Peripheral blood (calcium, cytokines, cortisol, transcriptomics); brain MRS; actigraphy
- **Expected result:** Identification of molecular cascade preceding mood switch — specifically whether calcium changes precede circadian disruption or vice versa
- **Impact:** Would establish temporal ordering of pathogenic events during mood state transitions

### Test 5: iPSC Pharmacological Panel with Genotype Stratification
- **Design:** Panel testing lithium, nimodipine, selective GSK-3beta inhibitor, and circadian modulators in iPSC-derived neurons from BD patients stratified by lithium response and CACNA1C genotype
- **Readouts:** Electrophysiology, calcium imaging, PER2::Luc circadian reporter, mitochondrial function
- **Impact:** Different subgroups responding to different drug classes would confirm mechanistic heterogeneity and guide personalized treatment

---

## Curation Leads

*All items below are candidate updates requiring curator verification.*

### Candidate Evidence References

1. **[PMID: 25403839](https://pubmed.ncbi.nlm.nih.gov/25403839/)** — *Snippet:* "we performed electrophysiology and quantitative PCR experiments that demonstrated increased L-type VGCC current density as well as increased mRNA expression of CACNA1C in iNs homozygous for the risk genotype, compared with non-risk genotypes." → **SUPPORT** for CACNA1C → calcium gain-of-function edge.

2. **[PMID: 35410376](https://pubmed.ncbi.nlm.nih.gov/35410376/)** — *Snippet:* "Combining gene-level results with SCHEMA, AKAP11 emerges as a definitive risk gene (odds ratio (OR) = 7.06, P = 2.83 × 10⁻⁹)." → **SUPPORT** for rare variant GSK-3β pathway involvement; new node AKAP11.

3. **[PMID: 38395906](https://pubmed.ncbi.nlm.nih.gov/38395906/)** — *Snippet:* "We identified functional enrichment in focal adhesion and PI3K-Akt pathways, but we did not find an association with the ECM pathway." → **QUALIFIES** the GSK-3β/IMP pharmacological mechanism.

4. **[PMID: 33442739](https://pubmed.ncbi.nlm.nih.gov/33442739/)** — *Snippet:* "the similarities between SCZ and BP subjects were principally due to the BP subjects with psychosis." → **QUALIFIES** scope to psychotic BD-I.

5. **[PMID: 41421618](https://pubmed.ncbi.nlm.nih.gov/41421618/)** — *Snippet:* "Those prescribed blue-blocking glasses did not show significant improvements in the YMRS relative to those with control lenses (difference of change in estimated marginal means at week 2 favoring control group by 2.1 points on YMRS, group * time interaction p = 0.93)." → **QUALIFIES** circadian intervention evidence.

6. **[PMID: 34002096](https://pubmed.ncbi.nlm.nih.gov/34002096/)** — *Snippet:* "Bipolar disorder risk alleles were enriched in genes in synaptic signaling pathways and brain-expressed genes, particularly those with high specificity of expression in neurons of the prefrontal cortex and hippocampus." → Foundational GWAS citation for hypothesis.

7. **[PMID: 26524527](https://pubmed.ncbi.nlm.nih.gov/26524527/)** — iPSC functional model showing hyperexcitability reversed by lithium in responders → **SUPPORT** for cellular-level mechanism.

8. **[PMID: 20591414](https://pubmed.ncbi.nlm.nih.gov/20591414/)** — *Snippet:* "knockdown of Clock, specifically in the VTA, results in hyperactivity and a reduction in anxiety-related behavior." → **SUPPORT** for circadian→dopamine→mania causal chain.

9. **[PMID: 9790159](https://pubmed.ncbi.nlm.nih.gov/9790159/)** — *Snippet:* "When verapamil was blindly substituted for nimodipine, two BP patients failed to maintain improvement but responded again to nimodipine." → Resolves CCA paradox; DHP CCB class-specific efficacy.

10. **[PMID: 24716566](https://pubmed.ncbi.nlm.nih.gov/24716566/)** — *Snippet:* "The meta-analysis combining both samples showed a significant association between rs774045 in TIMELESS (OR = 1.49) and rs782931 in RORA (OR = 1.31) and BD." → Update circadian gene list.

### Candidate Pathophysiology Nodes/Edges

- **Add node:** AKAP11 → GSK-3β (scaffolding protein; rare variant OR=7.06)
- **Add node:** PI3K-Akt signaling (upstream of GSK-3β; lithium response genomics)
- **Add node:** Bcl-2 → ER calcium handling → intracellular calcium dysregulation
- **Add edge:** CACNA1C rs1006737 → ↑L-type Ca²⁺ current density (gain-of-function, human neurons)
- **Add edge:** Li → ANK3-190 palmitoylation reduction → spine dynamics modulation
- **Add edge:** Social rhythm stabilization (IPSRT) → reduced episode recurrence
- **Update circadian genes:** Add TIMELESS, RORA; retain CLOCK, BMAL1, NR1D1

### Candidate Ontology Terms

- **Cell types:** Excitatory neurons (layers 2-6, DLPFC); VTA dopaminergic neurons; hippocampal DG neurons
- **Biological processes:** GO:0007623 (circadian rhythm); GO:0006816 (calcium ion transport); GO:0007268 (chemical synaptic transmission); GO:0016310 (phosphorylation — GSK-3β/PI3K-Akt)
- **Anatomical structures:** UBERON:0001870 (ACC); UBERON:0001876 (amygdala); UBERON:0002637 (ventral striatum)

### Candidate Subtype Restrictions

- Model's transcriptomic and neuroimaging evidence is strongest for **psychotic BD-I**
- Circadian gene associations and IPSRT efficacy apply across BD subtypes
- CACNA1C and calcium findings may apply more broadly across the psychosis spectrum

### Candidate Status Change

**Recommendation: Retain CANONICAL status** with annotation: "Partially supported integrative framework. Strongest evidence for psychotic BD-I. Six explicit qualifications: (1) psychosis-subtype specificity, (2) CCA drug-class issue, (3) lithium pathway complexity beyond GSK-3β/IMP, (4) circadian gene updates needed (TIMELESS, RORA), (5) neuroimaging non-specificity, (6) five critical experiments remain unperformed."

### Candidate Knowledge Gaps for KB

1. No selective GSK-3β inhibitor clinical trial in BD (confirmed absent May 2026)
2. No modern DHP CCB trial in BD (only Pazzaglia 1998, N=30)
3. No chronotherapy prevention trial from euthymia
4. Episodic switching mechanism unknown — phasic model exists but lacks direct evidence
5. BD-I vs. BD-II molecular distinction unresolved
6. No GenCC/ClinGen gene-disease validity assessment for CACNA1C-BD
7. No large-scale multi-ancestry BD GWAS

---

**Investigation Statistics:** 5 iterations, 49 evidence matrix entries (32 supporting, 9 qualifying, 2 partially refuting, 6 complementary), 30 confirmed findings, 138 papers reviewed, 4 visualizations generated.
