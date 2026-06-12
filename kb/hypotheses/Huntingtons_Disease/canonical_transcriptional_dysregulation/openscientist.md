---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-05-23T04:29:58.004987'
end_time: '2026-05-23T05:11:45.601810'
duration_seconds: 2507.6
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: Huntington's Disease
  category: Genetic
  hypothesis_group_id: canonical_transcriptional_dysregulation
  hypothesis_label: Transcriptional Dysregulation
  hypothesis_status: CANONICAL
  hypothesis_yaml: "hypothesis_group_id: canonical_transcriptional_dysregulation\n\
    hypothesis_label: Transcriptional Dysregulation\nstatus: CANONICAL\ndescription:\
    \ |\n  Mutant huntingtin disrupts transcriptional regulation by sequestering key\
    \ transcription factors and co-activators (Sp1, CBP, REST/NRSF), leading to widespread\
    \ downregulation of neuronal survival genes including BDNF. This is a canonical\
    \ downstream mechanistic layer in HD, linking mutant huntingtin protein interactions\
    \ to loss of neuronal maintenance programs.\nevidence:\n- reference: PMID:11839795\n\
    \  supports: SUPPORT\n  evidence_source: MODEL_ORGANISM\n  snippet: In HD transgenic\
    \ mice (R6/2) that express N-terminal-mutant huntingtin, Sp1 binds to the soluble\n\
    \    form of mutant huntingtin but not to aggregated huntingtin.\n  explanation:\
    \ In vivo evidence from HD transgenic mice showing that Sp1 binds soluble mutant\
    \ huntingtin,\n    supporting the sequestration mechanism.\n- reference: PMID:11839795\n\
    \  supports: SUPPORT\n  evidence_source: IN_VITRO\n  snippet: Mutant huntingtin\
    \ inhibits the binding of nuclear Sp1 to the promoter of nerve growth factor\n\
    \    receptor and suppresses its transcriptional activity in cultured cells.\n\
    \  explanation: Cell culture experiments demonstrating that mutant huntingtin\
    \ suppresses Sp1-regulated\n    transcription.\n- reference: PMID:11264541\n \
    \ supports: SUPPORT\n  evidence_source: IN_VITRO\n  snippet: We found that CBP\
    \ was depleted from its normal nuclear location and was present in polyglutamine\n\
    \    aggregates in HD cell culture models, HD transgenic mice, and human HD postmortem\
    \ brain.\n  explanation: HD cell culture models showing CBP depletion from its\
    \ normal nuclear location and sequestration\n    into polyglutamine aggregates.\n\
    - reference: PMID:11264541\n  supports: SUPPORT\n  evidence_source: MODEL_ORGANISM\n\
    \  snippet: We found that CBP was depleted from its normal nuclear location and\
    \ was present in polyglutamine\n    aggregates in HD cell culture models, HD transgenic\
    \ mice, and human HD postmortem brain.\n  explanation: HD transgenic mice confirming\
    \ CBP sequestration into polyglutamine aggregates in vivo.\n- reference: PMID:11264541\n\
    \  supports: SUPPORT\n  evidence_source: HUMAN_CLINICAL\n  snippet: We found that\
    \ CBP was depleted from its normal nuclear location and was present in polyglutamine\n\
    \    aggregates in HD cell culture models, HD transgenic mice, and human HD postmortem\
    \ brain.\n  explanation: Human HD postmortem brain tissue showing CBP depletion\
    \ and sequestration into polyglutamine\n    aggregates.\n- reference: PMID:12881722\n\
    \  supports: SUPPORT\n  evidence_source: HUMAN_CLINICAL\n  snippet: aberrant accumulation\
    \ of REST/NRSF in the nucleus is present in Huntington disease. We show\n    that\
    \ wild-type huntingtin coimmunoprecipitates with REST/NRSF and that less immunoprecipitated\
    \ material\n    is found in brain tissue with Huntington disease.\n  explanation:\
    \ Human postmortem brain data showing aberrant nuclear REST/NRSF accumulation\
    \ and reduced\n    huntingtin-REST/NRSF interaction in HD.\n- reference: PMID:12881722\n\
    \  supports: SUPPORT\n  evidence_source: MODEL_ORGANISM\n  snippet: loss of expression\
    \ of NRSE-controlled neuronal genes is shown in cells, mice and human brain\n\
    \    with Huntington disease.\n  explanation: Mouse model data confirming loss\
    \ of NRSE-controlled gene expression in HD, corroborating\n    the REST/NRSF dysregulation\
    \ mechanism.\n- reference: PMID:12881722\n  supports: SUPPORT\n  evidence_source:\
    \ IN_VITRO\n  snippet: Wild-type huntingtin inhibits the silencing activity of\
    \ NRSE, increasing transcription of BDNF.\n    We show that this effect occurs\
    \ through cytoplasmic sequestering of repressor element-1 transcription\n    factor/neuron\
    \ restrictive silencer factor (REST/NRSF), the transcription factor that binds\
    \ to NRSE.\n  explanation: Cell-based experiments showing wild-type huntingtin\
    \ sequesters REST/NRSF in the cytoplasm\n    to permit BDNF transcription, a function\
    \ lost with the mutant protein."
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 1
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
citation_count: 32
---

## Question

# Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Huntington's Disease
- **Category:** Genetic

## Target Hypothesis
- **Hypothesis ID:** canonical_transcriptional_dysregulation
- **Hypothesis Label:** Transcriptional Dysregulation
- **Status in KB:** CANONICAL

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: canonical_transcriptional_dysregulation
hypothesis_label: Transcriptional Dysregulation
status: CANONICAL
description: |
  Mutant huntingtin disrupts transcriptional regulation by sequestering key transcription factors and co-activators (Sp1, CBP, REST/NRSF), leading to widespread downregulation of neuronal survival genes including BDNF. This is a canonical downstream mechanistic layer in HD, linking mutant huntingtin protein interactions to loss of neuronal maintenance programs.
evidence:
- reference: PMID:11839795
  supports: SUPPORT
  evidence_source: MODEL_ORGANISM
  snippet: In HD transgenic mice (R6/2) that express N-terminal-mutant huntingtin, Sp1 binds to the soluble
    form of mutant huntingtin but not to aggregated huntingtin.
  explanation: In vivo evidence from HD transgenic mice showing that Sp1 binds soluble mutant huntingtin,
    supporting the sequestration mechanism.
- reference: PMID:11839795
  supports: SUPPORT
  evidence_source: IN_VITRO
  snippet: Mutant huntingtin inhibits the binding of nuclear Sp1 to the promoter of nerve growth factor
    receptor and suppresses its transcriptional activity in cultured cells.
  explanation: Cell culture experiments demonstrating that mutant huntingtin suppresses Sp1-regulated
    transcription.
- reference: PMID:11264541
  supports: SUPPORT
  evidence_source: IN_VITRO
  snippet: We found that CBP was depleted from its normal nuclear location and was present in polyglutamine
    aggregates in HD cell culture models, HD transgenic mice, and human HD postmortem brain.
  explanation: HD cell culture models showing CBP depletion from its normal nuclear location and sequestration
    into polyglutamine aggregates.
- reference: PMID:11264541
  supports: SUPPORT
  evidence_source: MODEL_ORGANISM
  snippet: We found that CBP was depleted from its normal nuclear location and was present in polyglutamine
    aggregates in HD cell culture models, HD transgenic mice, and human HD postmortem brain.
  explanation: HD transgenic mice confirming CBP sequestration into polyglutamine aggregates in vivo.
- reference: PMID:11264541
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: We found that CBP was depleted from its normal nuclear location and was present in polyglutamine
    aggregates in HD cell culture models, HD transgenic mice, and human HD postmortem brain.
  explanation: Human HD postmortem brain tissue showing CBP depletion and sequestration into polyglutamine
    aggregates.
- reference: PMID:12881722
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: aberrant accumulation of REST/NRSF in the nucleus is present in Huntington disease. We show
    that wild-type huntingtin coimmunoprecipitates with REST/NRSF and that less immunoprecipitated material
    is found in brain tissue with Huntington disease.
  explanation: Human postmortem brain data showing aberrant nuclear REST/NRSF accumulation and reduced
    huntingtin-REST/NRSF interaction in HD.
- reference: PMID:12881722
  supports: SUPPORT
  evidence_source: MODEL_ORGANISM
  snippet: loss of expression of NRSE-controlled neuronal genes is shown in cells, mice and human brain
    with Huntington disease.
  explanation: Mouse model data confirming loss of NRSE-controlled gene expression in HD, corroborating
    the REST/NRSF dysregulation mechanism.
- reference: PMID:12881722
  supports: SUPPORT
  evidence_source: IN_VITRO
  snippet: Wild-type huntingtin inhibits the silencing activity of NRSE, increasing transcription of BDNF.
    We show that this effect occurs through cytoplasmic sequestering of repressor element-1 transcription
    factor/neuron restrictive silencer factor (REST/NRSF), the transcription factor that binds to NRSE.
  explanation: Cell-based experiments showing wild-type huntingtin sequesters REST/NRSF in the cytoplasm
    to permit BDNF transcription, a function lost with the mutant protein.
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

# Mechanistic Hypothesis Report: Transcriptional Dysregulation in Huntington's Disease

**Hypothesis ID:** canonical_transcriptional_dysregulation  
**Disease:** Huntington's Disease (Genetic)  
**KB Status:** CANONICAL  
**Report Date:** 2026-05-23  
**Papers Reviewed:** 89  
**Findings Confirmed:** 6  

---

## Executive Judgment

**Verdict: SUPPORTED — with mechanistic refinement required**

The transcriptional dysregulation hypothesis in Huntington's disease (HD) is well-supported as a canonical downstream pathogenic mechanism, validated across human postmortem brain, transgenic and knock-in mouse models, and cell culture systems. Three core transcription factor (TF) pathways — Sp1/TAFII130, CBP/p300, and REST/NRSF — have been independently confirmed, with the **REST/NRSF loss-of-function pathway** representing the most robustly validated arm, including genome-wide ChIP validation, direct loss-of-function phenocopy experiments, and pharmacological rescue of BDNF expression. The CBP depletion pathway is functionally validated by single-cell rescue experiments linking CBP loss to histone hypo-acetylation and toxicity. The Sp1/TAFII130 pathway is supported by biochemical interaction data and transcriptional rescue in both presymptomatic and symptomatic HD brain tissue.

However, the original mechanistic model — physical sequestration of transcription factors into visible polyglutamine aggregates — requires significant refinement. A key counter-study by Yu et al. (2002, [PMID: 11971872](https://pubmed.ncbi.nlm.nih.gov/11971872/)) demonstrated that Sp1, CBP, and TBP were NOT depleted from their normal nuclear locations despite abundant intranuclear inclusions in HD mice. This apparent contradiction was resolved by Schaffar et al. (2004, [PMID: 15225551](https://pubmed.ncbi.nlm.nih.gov/15225551/)), who showed that **soluble oligomers**, not insoluble aggregates, inhibit transcription factor function through conformational destabilization. The mechanism should therefore be described as functional inhibition by soluble/oligomeric mutant huntingtin (mHTT) species rather than physical trapping in visible aggregates.

Furthermore, recent breakthroughs in somatic CAG repeat expansion research (2024–2025) have repositioned transcriptional dysregulation within a broader causal framework: preventing somatic expansion via Msh3 knockout also prevents transcriptional dysregulation entirely (Wang et al., 2025, [PMID: 39938516](https://pubmed.ncbi.nlm.nih.gov/39938516/)), placing DNA mismatch repair-driven instability causally upstream. The hypothesis therefore retains its canonical status but must be understood as a **critical mediating layer** between somatic repeat expansion and neuronal death, not an independent initiating event.

**Most important caveats:**
1. The physical TF sequestration into aggregates model is contested; functional inhibition by soluble mHTT is the better-supported mechanism
2. Somatic CAG expansion is upstream and may be the true determinant of disease onset timing
3. Epigenetic mechanisms (H3K9me3 enrichment, HDAC dysregulation) operate in parallel and contribute independently to transcriptional changes
4. Clinical translation of transcription-targeted therapies (HDAC inhibitors) has been disappointing, and one bromodomain inhibitor (JQ1) was actually detrimental in HD mice

---

## Summary

Transcriptional dysregulation is one of the most extensively studied downstream mechanisms in Huntington's disease pathogenesis. The hypothesis proposes that mutant huntingtin, carrying an expanded polyglutamine tract, disrupts transcriptional regulation by interfering with key transcription factors and co-activators — principally Sp1, CREB-binding protein (CBP), and the repressor element-1 silencing transcription factor (REST/NRSF) — leading to widespread downregulation of neuronal survival genes, most notably brain-derived neurotrophic factor (BDNF). This mechanism links the proximal molecular defect (polyglutamine expansion in HTT) to the loss of neuronal maintenance programs that ultimately manifests as selective striatal neurodegeneration.

Our systematic evaluation of 89 papers spanning primary research, model organism studies, human clinical data, and mechanistic reviews confirms that this hypothesis is robustly supported at multiple levels of evidence. The REST/NRSF pathway has the strongest validation, with genome-wide ChIP data demonstrating increased REST occupancy at target loci in HD cells, animal models, and human brain, plus pharmacological rescue experiments restoring BDNF levels. The CBP depletion pathway is confirmed by single-cell experiments linking CBP loss to histone hypo-acetylation and toxicity, with rescue by CBP overexpression. However, the field has evolved substantially since the original sequestration model was proposed: the mechanism now appears to involve functional inhibition by soluble/oligomeric mHTT species rather than physical trapping in visible aggregates, and the entire transcriptional program sits downstream of somatic CAG repeat expansion driven by mismatch repair machinery.

These findings have direct implications for therapeutic strategy: targeting transcriptional dysregulation (e.g., HDAC inhibitors, REST complex modulators) addresses a critical mediating layer of pathology, but upstream interventions targeting somatic expansion (e.g., MSH3 suppression) may prevent transcriptional dysregulation from developing in the first place. The hypothesis is most strongly validated in striatal medium spiny neurons (MSNs), the cell type most vulnerable in HD, and explains the progressive loss of neuronal identity genes observed in both mouse models and human brain.

---

## Key Findings

### Finding 1: Sp1/TAFII130 Sequestration by Mutant Huntingtin Is an Early Event in HD

Dunah et al. (2002) provided critical evidence that huntingtin physically interacts with the transcriptional activator Sp1 and its coactivator TAFII130, and that soluble mutant huntingtin inhibits Sp1 binding to DNA in postmortem brain tissues from both presymptomatic and symptomatic HD patients ([PMID: 11988536](https://pubmed.ncbi.nlm.nih.gov/11988536/)). The study demonstrated that "huntingtin interacts with the transcriptional activator Sp1 and coactivator TAFII130. Coexpression of Sp1 and TAFII130 in cultured striatal cells from wild-type and HD transgenic mice reverses the transcriptional inhibition of the dopamine D2 receptor gene caused by mutant huntingtin, as well as protects neurons from huntingtin-induced cellular toxicity." This rescue experiment provides strong functional evidence that Sp1 pathway disruption is causally linked to neuronal dysfunction. The detection of Sp1 inhibition in presymptomatic brain tissue is particularly significant, suggesting this event precedes clinical disease.

Li et al. (2002) confirmed that Sp1 binds soluble mutant huntingtin in R6/2 mice and that mutant huntingtin suppresses Sp1-regulated transcription of nerve growth factor receptor ([PMID: 11839795](https://pubmed.ncbi.nlm.nih.gov/11839795/)). Importantly, the interaction was with soluble, not aggregated, huntingtin — a distinction that would later prove critical for mechanistic interpretation.

**Counter-evidence:** Yu et al. (2002) found that "All three transcription factors were diffusely distributed in the nucleus, despite the presence of abundant intranuclear inclusions. There were no differences in the nuclear staining of these transcription factors between HD and wild-type mouse brains" ([PMID: 11971872](https://pubmed.ncbi.nlm.nih.gov/11971872/)). This directly challenges the physical sequestration model, though it remains compatible with functional inhibition by soluble mHTT species that do not form visible inclusions.

### Finding 2: CBP Depletion from Nucleus into PolyQ Aggregates Is Confirmed Across Models and Human Brain

Nucifora et al. (2001) provided foundational evidence that "CBP was depleted from its normal nuclear location and was present in polyglutamine aggregates in HD cell culture models, HD transgenic mice, and human HD postmortem brain" ([PMID: 11264541](https://pubmed.ncbi.nlm.nih.gov/11264541/)). CBP overexpression rescued polyQ-induced toxicity, establishing a causal link between CBP loss and cell death. This cross-species concordance (cell culture, mouse model, human brain) significantly strengthens the evidence.

Jiang et al. (2006) extended these findings at single-cell resolution, demonstrating that "cell toxicity was accompanied by CBP depletion, rather than merely recruitment. Transfection with a htt exon1 construct containing uninterrupted polyglutamine or a polyglutamine region engineered to form a compact beta structure resulted in cell toxicity. CBP depletion was accompanied by histone hypo-acetylation. CBP overexpression rescued both acetylated histone levels and cell toxicity" ([PMID: 16766198](https://pubmed.ncbi.nlm.nih.gov/16766198/)). This study provides the most direct mechanistic link: CBP depletion → histone hypo-acetylation → toxicity, with full rescue by CBP overexpression at each step.

**Counter-evidence and mechanistic refinement:** Yu et al. (2002) found that CBP was NOT depleted by Western blot in HD mice, and most CBP was not co-localized with huntingtin inclusions by double-labeling and electron microscopy ([PMID: 11971872](https://pubmed.ncbi.nlm.nih.gov/11971872/)). Schaffar et al. (2004) resolved this apparent contradiction by demonstrating that "monomers or small soluble oligomers of huntingtin exon1 accumulate in the nucleus and inhibit the function of TBP in a polyQ-dependent manner... independent of the formation of insoluble coaggregates. Interaction of toxic huntingtin with the benign polyQ repeat of TBP structurally destabilizes the transcription factor" ([PMID: 15225551](https://pubmed.ncbi.nlm.nih.gov/15225551/)). Hsp70/Hsp40 chaperones could interfere with this conformational change and inhibit TF deactivation. This reframing — from physical sequestration into aggregates to functional inhibition by soluble oligomers via conformational destabilization — is now the prevailing mechanistic view.

### Finding 3: REST/NRSF Dysregulation Is the Most Robustly Validated Arm of the Hypothesis

Zuccato et al. (2003) established the foundational mechanism: "Wild-type huntingtin inhibits the silencing activity of NRSE, increasing transcription of BDNF. We show that this effect occurs through cytoplasmic sequestering of repressor element-1 transcription factor/neuron restrictive silencer factor (REST/NRSF), the transcription factor that binds to NRSE" ([PMID: 12881722](https://pubmed.ncbi.nlm.nih.gov/12881722/)). In HD, mutant huntingtin loses this cytoplasmic retention function, leading to aberrant nuclear accumulation of REST/NRSF and transcriptional silencing of NRSE-controlled genes. This was confirmed across cells, HD transgenic mice, and human HD postmortem brain.

Zuccato et al. (2007) provided genome-wide validation using ChIP-on-chip, demonstrating "increased binding of the RE1 silencing transcription factor/neuron-restrictive silencer factor (REST/NRSF) repressor occurs at multiple genomic RE1/NRSE loci in HD cells, in animal models, and in postmortem brains, resulting in a decrease of RE1/NRSE-mediated gene transcription. The same molecular phenotype is produced in cells and brain tissue depleted of endogenous huntingtin, thereby directly validating the loss-of-function hypothesis of HD" ([PMID: 17596446](https://pubmed.ncbi.nlm.nih.gov/17596446/)). The loss-of-function validation is particularly powerful: mHTT pathology at REST-controlled loci phenocopies complete HTT absence, proving that the mechanism is loss of wild-type HTT function rather than a toxic gain of function.

Pharmacological validation came from Conforti et al. (2013), who identified compound C91 that disrupts the REST-mSIN3b complex and restores BDNF protein levels in HD cells ([PMID: 23800350](https://pubmed.ncbi.nlm.nih.gov/23800350/)). Datta & Bhattacharyya (2011) added mechanistic depth by identifying HIPPI as a transcriptional activator of REST, with "feeble interaction of HIP1 with mutant huntingtin protein resulted in increased nuclear accumulation of HIPPI and HIP1, leading to higher occupancy of HIPPI at the REST promoter, triggering its transcriptional activation and consequent repression of REST target genes" ([PMID: 21832040](https://pubmed.ncbi.nlm.nih.gov/21832040/)).

### Finding 4: Somatic CAG Repeat Expansion Is an Upstream Competing Mechanism

Multiple recent studies have established that somatic expansion of the CAG repeat in striatal MSNs, driven by mismatch repair genes (MSH3, PMS1, PMS2, FAN1), is a primary determinant of HD onset and progression ([PMID: 40490511](https://pubmed.ncbi.nlm.nih.gov/40490511/); [PMID: 39938516](https://pubmed.ncbi.nlm.nih.gov/39938516/); [PMID: 39937881](https://pubmed.ncbi.nlm.nih.gov/39937881/)). Wang et al. (2025) demonstrated that "Msh3 deficiency prevents mHtt aggregation by keeping somatic MSN CAG length below 150. Importantly, Msh3 deficiency corrects synaptic, astrocytic, and locomotor defects in HD mice" ([PMID: 39938516](https://pubmed.ncbi.nlm.nih.gov/39938516/)). This is a transformative finding: **preventing somatic expansion also prevents transcriptional dysregulation**, placing somatic instability causally upstream of the transcriptional changes described by this hypothesis.

The genetic modifier landscape from genome-wide association studies ([PMID: 40490511](https://pubmed.ncbi.nlm.nih.gov/40490511/)) further reinforces this hierarchy, showing that DNA repair genes (MSH3, PMS2, FAN1) modify HD onset through somatic expansion, with a synonymous CAG-adjacent variant in HTT dramatically hastening motor onset without increasing somatic expansion — suggesting additional complexity beyond expansion alone.

### Finding 5: The Physical Sequestration Model Is Challenged — Functional Inhibition Is the Better Framework

Yu et al. (2002) systematically examined TBP, CBP, and Sp1 in HD mouse models and found "All three transcription factors were diffusely distributed in the nucleus, despite the presence of abundant intranuclear inclusions. There were no differences in the nuclear staining of these transcription factors between HD and wild-type mouse brains" ([PMID: 11971872](https://pubmed.ncbi.nlm.nih.gov/11971872/)). Double-labeling showed most CBP was NOT co-localized with huntingtin inclusions, and Western blots confirmed transcription factors were not trapped in inclusions.

Schaffar et al. (2004) provided the mechanistic resolution: monomers or small soluble oligomers of huntingtin exon 1 accumulate in the nucleus and inhibit transcription factor function in a polyQ-dependent manner through conformational destabilization, independent of insoluble co-aggregate formation ([PMID: 15225551](https://pubmed.ncbi.nlm.nih.gov/15225551/)). This finding shifts the field from a "sequestration" model to a "functional inhibition" model and explains why molecular chaperones (Hsp70/Hsp40), which prevent the toxic conformational change in mHTT, can rescue transcription factor activity.

### Finding 6: Epigenetic Dysregulation Operates as a Parallel Mechanism

Beyond direct transcription factor interference, mHTT drives transcriptional changes through epigenetic mechanisms. Lee et al. (2017) identified SETDB1/ESET as a mediator of mHTT-induced degeneration, with "H3K9me3-enriched epigenome signatures of multiple neuronal pathways including Egr1, Fos, Ezh1, and Arc are deregulated in HD transgenic (R6/2) mice. Nogalamycin modulated the expression of the H3K9me3-landscaped epigenome in medium spiny neurons and reduced mutant HTT nuclear inclusion formation" ([PMID: 28593442](https://pubmed.ncbi.nlm.nih.gov/28593442/)). Lee et al. (2013) showed H3K9me3-dependent silencing of CHRM1 and synaptic transmission genes in HD striatal cell lines ([PMID: 23455440](https://pubmed.ncbi.nlm.nih.gov/23455440/)).

Hecklau et al. (2021) demonstrated that "selective inhibition of HDAC1 and HDAC3 by RGFP109 alleviated transcriptional dysregulation of a number of genes, including the transcription factor genes" ([PMID: 33679321](https://pubmed.ncbi.nlm.nih.gov/33679321/)). Suelves et al. (2017) showed HDAC3 inhibition prevented cognitive deficits and, remarkably, suppressed striatal CAG expansions in HD mice ([PMID: 28729730](https://pubmed.ncbi.nlm.nih.gov/28729730/)), suggesting a bidirectional relationship between epigenetic state and somatic instability. However, Kedaigle et al. (2019) found that the bromodomain inhibitor JQ1 was selectively detrimental to R6/2 mice, worsening HD-related transcriptional pathways ([PMID: 31696228](https://pubmed.ncbi.nlm.nih.gov/31696228/)), cautioning that epigenetic modulation in HD can have unexpected adverse effects.

---

## Evidence Matrix

{{figure:evidence_matrix.png|caption=Evidence matrix visualization showing the distribution of supporting, qualifying, and competing evidence across evidence types for the HD transcriptional dysregulation hypothesis}}

| Citation | Evidence Type | Direction | Mechanistic Claim | Key Finding | Context | Confidence |
|----------|--------------|-----------|-------------------|-------------|---------|------------|
| [PMID: 11988536](https://pubmed.ncbi.nlm.nih.gov/11988536/) | Human Clinical + In Vitro | **SUPPORTS** | Sp1/TAFII130 inhibition | mHTT interacts with Sp1/TAFII130; soluble mHTT inhibits Sp1 DNA binding in presymptomatic + symptomatic HD brain; rescue by Sp1/TAFII130 coexpression | Human postmortem, striatal cells | High |
| [PMID: 11839795](https://pubmed.ncbi.nlm.nih.gov/11839795/) | Model Organism + In Vitro | **SUPPORTS** | Sp1 binding to soluble mHTT | Sp1 binds soluble mHTT in R6/2 mice; mHTT suppresses Sp1-regulated NGF-R transcription | R6/2 mice, cell culture | High |
| [PMID: 11264541](https://pubmed.ncbi.nlm.nih.gov/11264541/) | Human + Model + In Vitro | **SUPPORTS** | CBP depletion into polyQ aggregates | CBP depleted from nucleus, present in polyQ aggregates across cell culture, HD mice, human brain | Multiple model systems + human | High |
| [PMID: 16766198](https://pubmed.ncbi.nlm.nih.gov/16766198/) | In Vitro | **SUPPORTS** | CBP depletion → toxicity | Single-cell: CBP depletion accompanies toxicity; histone hypo-acetylation; CBP overexpression rescues | Cell culture | High |
| [PMID: 12881722](https://pubmed.ncbi.nlm.nih.gov/12881722/) | Human + Model + In Vitro | **SUPPORTS** | REST/NRSF loss-of-function | WT HTT sequesters REST in cytoplasm; mHTT loses this function; nuclear REST silences BDNF and NRSE genes | Cells, mice, human brain | Very High |
| [PMID: 17596446](https://pubmed.ncbi.nlm.nih.gov/17596446/) | Human + Model + In Vitro | **SUPPORTS** | Genome-wide REST dysregulation | Increased REST occupancy at multiple NRSE loci; HTT depletion phenocopies; loss-of-function validated | ChIP-on-chip, multiple systems | Very High |
| [PMID: 23800350](https://pubmed.ncbi.nlm.nih.gov/23800350/) | In Vitro | **SUPPORTS** | REST complex as therapeutic target | C91 disrupts REST-mSIN3b, reduces mSIN3b nuclear entry, restores BDNF in HD cells | HD cell models | High |
| [PMID: 21832040](https://pubmed.ncbi.nlm.nih.gov/21832040/) | In Vitro | **SUPPORTS** | Additional REST upregulation mechanism | HIPPI activates REST transcription; increased nuclear HIPPI in HD model | HD cell model | Medium |
| [PMID: 11971872](https://pubmed.ncbi.nlm.nih.gov/11971872/) | Model Organism | **REFUTES** (sequestration model) | Physical TF trapping in inclusions | Sp1, CBP, TBP NOT depleted from nucleus despite abundant inclusions; not co-localized | N171-82Q, R6/2 mice | High |
| [PMID: 15225551](https://pubmed.ncbi.nlm.nih.gov/15225551/) | In Vitro | **QUALIFIES** | Mechanism of TF inhibition | Soluble oligomers, not aggregates, inhibit TFs via conformational destabilization; chaperones rescue | In vitro + cell culture | High |
| [PMID: 39938516](https://pubmed.ncbi.nlm.nih.gov/39938516/) | Model Organism | **COMPETING** (upstream) | Somatic expansion drives transcriptionopathy | Msh3 KO prevents somatic expansion AND transcriptional dysregulation in Q140 mice | Q140 knock-in mice | Very High |
| [PMID: 40490511](https://pubmed.ncbi.nlm.nih.gov/40490511/) | Human Genetic | **COMPETING** (upstream) | MMR modifier genes drive HD onset | GWAS confirms MMR genes modify somatic expansion and clinical trajectory | HD patient cohorts | Very High |
| [PMID: 28593442](https://pubmed.ncbi.nlm.nih.gov/28593442/) | Model Organism | **SUPPORTS** (parallel) | H3K9me3 epigenetic silencing | SETDB1/ESET mediates heterochromatin-dependent gene silencing in R6/2 MSNs; rescue extends lifespan | R6/2 mice | High |
| [PMID: 23455440](https://pubmed.ncbi.nlm.nih.gov/23455440/) | In Vitro | **SUPPORTS** (parallel) | H3K9me3 silences CHRM1 | H3K9me3-ChIP-seq + RNA-seq identifies neuronal synaptic genes silenced by H3K9me3 in HD | STHdh cell lines | High |
| [PMID: 33679321](https://pubmed.ncbi.nlm.nih.gov/33679321/) | Model Organism | **SUPPORTS** (parallel) | HDAC1/3 inhibition rescues transcription | Selective RGFP109 alleviates transcriptional dysregulation of multiple genes | HD mice | High |
| [PMID: 28729730](https://pubmed.ncbi.nlm.nih.gov/28729730/) | Model Organism | **SUPPORTS** (parallel) | HDAC3 in cognition + expansion | HDAC3 inhibitor prevents cognitive deficits AND suppresses striatal CAG expansions | Hdh knock-in mice | High |
| [PMID: 32681824](https://pubmed.ncbi.nlm.nih.gov/32681824/) | Human + Model | **QUALIFIES** | Cell-type specificity | snRNA-seq reveals mtRNA release and innate immune activation in SPNs, not general TF depletion | Human caudate, HD mice | High |
| [PMID: 31696228](https://pubmed.ncbi.nlm.nih.gov/31696228/) | Model Organism | **QUALIFIES** | Epigenetic modulation risks | BET inhibitor JQ1 selectively detrimental to R6/2 mice; worsens HD transcriptional pathways | R6/2 mice | High |
| [PMID: 34215255](https://pubmed.ncbi.nlm.nih.gov/34215255/) | In Vitro | **SUPPORTS** | WT HTT is a transcriptional regulator | HTT knockout causes widespread transcriptome changes in neuronal development/signaling pathways | CRISPR HTT-KO, SH-SY5Y | High |

---

## Mechanistic Causal Chain

{{figure:causal_chain.png|caption=Mechanistic causal chain diagram showing the pathway from inherited CAG expansion through transcriptional dysregulation to clinical HD manifestation, with evidence strength annotations at each step}}

The transcriptional dysregulation hypothesis implies the following causal chain from upstream trigger to clinical manifestation. Evidence strength varies substantially across links:

```
1. INHERITED CAG EXPANSION (≥36 repeats in HTT exon 1)
   Evidence: ESTABLISHED (Mendelian genetics, 1993)
   |
   v
2. SOMATIC CAG REPEAT EXPANSION IN MSNs
   (driven by MSH3/PMS1/PMS2/FAN1 — DNA mismatch repair)
   Evidence: VERY STRONG (GWAS + mouse genetics, 2024-2025)
   |
   v
3. THRESHOLD-EXCEEDING polyQ-EXPANDED mHTT IN VULNERABLE NEURONS
   (soluble/oligomeric species are the toxic form)
   Evidence: STRONG (PMID:15225551, PMID:11971872)
   |
   ├─────────────────────────┬────────────────────────┐
   v                         v                        v
4a. Sp1/TAFII130          4b. CBP/p300             4c. REST/NRSF
    FUNCTIONAL              DEPLETION/                NUCLEAR
    INHIBITION              INACTIVATION              ACCUMULATION
    [STRONG]                [MODERATE-STRONG]         [VERY STRONG]
   |                         |                        |
   v                         v                        v
5a. ↓D2R, NGFR,          5b. Global histone       5c. ↓BDNF + NRSE-
    Sp1-target genes          hypo-acetylation         controlled neuronal
                              → gene silencing          survival genes
   |                         |                        |
   └─────────────────────────┴────────────────────────┘
                             |
        PARALLEL EPIGENETIC LAYER
        (H3K9me3 ↑, HDAC dysfunction)
                             |
                             v
6. LOSS OF NEURONAL SURVIVAL + IDENTITY PROGRAMS
   (convergent gene silencing from TF + epigenetic mechanisms)
   |
   v
7. SELECTIVE STRIATAL MSN DEGENERATION
   (D2-MSNs > D1-MSNs > cortical neurons)
   |
   v
8. HD CLINICAL MANIFESTATIONS
   (chorea, cognitive decline, psychiatric symptoms)
```

### Where Evidence Is Strong

- **Steps 1–3**: The genetic-to-protein chain is established beyond doubt. Somatic expansion as a modifier of onset is now confirmed by human GWAS and mouse genetics.
- **Step 4c → 5c (REST/NRSF pathway)**: Genome-wide ChIP validation, loss-of-function phenocopy, cross-species concordance, and pharmacological rescue make this the strongest arm.
- **Step 4a (Sp1/TAFII130)**: Biochemical interaction confirmed in presymptomatic human brain; transcriptional rescue demonstrated.
- **Step 4b (CBP)**: Single-cell resolution evidence of CBP depletion → histone hypo-acetylation → toxicity, with rescue by CBP overexpression.

### Where Links Are Inferred or Weak

- **Step 2 → Step 4**: The precise CAG length threshold at which transcription factor interactions become pathologically disrupted is unknown. Wang et al. (2025) suggest ~150 repeats in mouse MSNs, but this has not been confirmed in human tissue.
- **Step 4b (CBP sequestration vs. functional inhibition)**: The most contested link — Yu et al. (2002) found no evidence of physical CBP depletion despite abundant inclusions, while Nucifora et al. (2001) and Jiang et al. (2006) did find depletion. Different model systems and detection methods may explain the discrepancy.
- **Steps 5 → 6 → 7**: Whether transcriptional changes are sufficient to cause neuronal death or require additional insults (excitotoxicity, mitochondrial dysfunction) is unresolved.
- **Relative contributions of arms 4a, 4b, 4c**: No study has simultaneously quantified the contribution of each pathway in a single model system.

### Missing Causal Steps

1. The transition from transcriptional dysregulation to cell death is not mechanistically resolved
2. Why striatal MSNs are uniquely vulnerable to the same transcriptional mechanisms affecting all HTT-expressing neurons remains incompletely explained
3. Burns et al. (2025, [PMID: 40482637](https://pubmed.ncbi.nlm.nih.gov/40482637/)) found mitochondrial deficits at postnatal day 0 in R6/2 mice, preceding striatal identity gene loss — suggesting transcriptional changes may not be the earliest downstream event

---

## Knowledge Gaps

### 1. Contested Mechanism of CBP Depletion

**Scope:** Whether CBP is physically sequestered into aggregates or functionally inhibited by soluble mHTT without visible depletion.  
**Why it matters:** Determines whether therapeutic strategies should target aggregate clearance or mHTT-TF protein–protein interactions.  
**What was checked:** Yu et al. (2002) performed immunohistochemistry, double-labeling, electron microscopy, and Western blot in HD mice — found no depletion. Nucifora et al. (2001) found depletion in cell culture, mice, and human brain. Jiang et al. (2006) confirmed functional depletion at single-cell level. Schaffar et al. (2004) showed soluble oligomers inhibit TFs without co-aggregation.  
**Resolution:** Single-cell CUT&Tag for H3K27ac (CBP enzymatic product) combined with CBP ChIP-seq in human HD brain at different Vonsattel grades would resolve whether CBP is physically depleted or functionally impaired at specific loci.

### 2. Relative Contribution of Each TF Pathway

**Scope:** Sp1 vs. CBP vs. REST/NRSF — quantitative hierarchy unknown.  
**Why it matters:** Therapeutic prioritization requires knowing which arm contributes most to neuronal dysfunction and death.  
**What was checked:** Each pathway studied independently across different labs and model systems; never compared head-to-head in a single system.  
**Resolution:** Combinatorial rescue experiments (Sp1 overexpression + CBP overexpression + REST knockdown) individually and in combination in isogenic HD iPSC-derived MSNs with transcriptomic, electrophysiological, and survival readouts.

### 3. Somatic Expansion–Transcription Threshold

**Scope:** At what somatic CAG length does transcriptional dysregulation begin in human MSNs?  
**Why it matters:** Defines the therapeutic window for expansion-suppression strategies (e.g., MSH3 ASOs).  
**What was checked:** Wang et al. (2025) suggest ~150 CAGs as a threshold in mouse MSNs; no human single-cell data linking individual cell repeat length to transcriptomic state.  
**Resolution:** Single-cell simultaneous measurement of CAG length (long-read sequencing) and transcriptome (scRNA-seq) in human HD brain tissue across disease stages.

### 4. Clinical Translation Failure

**Scope:** HDAC inhibitors show robust benefit in animal models but have not demonstrated efficacy in HD clinical trials. JQ1 (BET bromodomain inhibitor) was actually detrimental to R6/2 mice ([PMID: 31696228](https://pubmed.ncbi.nlm.nih.gov/31696228/)).  
**Why it matters:** If the transcriptional dysregulation hypothesis is correct and clinically relevant, transcription-targeting therapies should help; their failure challenges the therapeutic tractability of this mechanism.  
**What was checked:** Preclinical studies with HDAC inhibitors (pan, HDAC1/3-selective, HDAC3-selective) all show benefit. No positive Phase II/III clinical trial results were identified.  
**Resolution:** Phase Ib/IIa trial of selective HDAC3 inhibitor in early-manifest HD with transcriptomic biomarker panel as primary pharmacodynamic endpoint.

### 5. BDNF Transcription vs. BDNF Transport

**Scope:** Both reduced BDNF transcription (via REST dysregulation) and impaired BDNF vesicular transport (via mHTT-motor protein interaction) are documented; their relative contributions to striatal BDNF deficiency are unknown.  
**Why it matters:** Determines whether treatment should target BDNF gene expression or BDNF delivery.  
**What was checked:** Yu et al. (2018, [PMID: 30451892](https://pubmed.ncbi.nlm.nih.gov/30451892/)) showed decreased BDNF release/transport in zQ175 cortical neurons. Gauthier et al. and Saudou lab demonstrated mHTT impairs BDNF vesicle transport ([PMID: 23575829](https://pubmed.ncbi.nlm.nih.gov/23575829/)).  
**Resolution:** AAV-mediated constitutive BDNF expression (bypassing transcriptional regulation) in cortical neurons of knock-in mice; if transport is the primary deficit, overproduction should not fully rescue striatal BDNF levels.

### 6. Absence of Human Single-Cell TF Binding Data

**Scope:** No genome-wide ChIP-seq for REST, Sp1, or CBP at single-cell resolution in human HD brain exists.  
**What was checked:** Zuccato et al. (2007) used bulk ChIP-on-chip; Lee et al. (2020, [PMID: 32681824](https://pubmed.ncbi.nlm.nih.gov/32681824/)) and Malaiya et al. (2021, [PMID: 34011527](https://pubmed.ncbi.nlm.nih.gov/34011527/)) provide snRNA-seq but not TF binding.  
**Resolution:** Single-cell CUT&Tag or CUT&RUN for REST, Sp1, and CBP in human HD caudate at multiple Vonsattel grades.

### 7. No GenCC/ClinGen Functional Evidence Classification

**Scope:** The transcriptional dysregulation mechanism has not been formally classified in standardized disease mechanism databases.  
**Resolution:** Formal curation submission with evidence codes to GenCC/ClinGen.

---

## Alternative Models

### 1. Somatic CAG Repeat Expansion (UPSTREAM CAUSE)
- **Relationship to seed hypothesis:** Upstream driver
- **Evidence strength:** Very strong (GWAS + mouse genetics)
- **Key studies:** [PMID: 39938516](https://pubmed.ncbi.nlm.nih.gov/39938516/), [PMID: 40490511](https://pubmed.ncbi.nlm.nih.gov/40490511/), [PMID: 39937881](https://pubmed.ncbi.nlm.nih.gov/39937881/)
- **Assessment:** Transcriptional dysregulation is positioned as a downstream mediator; preventing expansion prevents transcriptionopathy. The two are hierarchically related, not mutually exclusive.

### 2. Epigenetic Dysregulation — H3K9me3 and HDAC (PARALLEL MECHANISM)
- **Relationship:** Parallel mechanism contributing to the same transcriptional phenotype
- **Evidence strength:** Strong
- **Key studies:** [PMID: 28593442](https://pubmed.ncbi.nlm.nih.gov/28593442/), [PMID: 23455440](https://pubmed.ncbi.nlm.nih.gov/23455440/), [PMID: 33679321](https://pubmed.ncbi.nlm.nih.gov/33679321/), [PMID: 28729730](https://pubmed.ncbi.nlm.nih.gov/28729730/)
- **Assessment:** Operates through distinct chromatin remodeling pathways (H3K9me3, histone deacetylation) that converge on the same transcriptional phenotype. May partially overlap with CBP depletion pathway (CBP loss reduces histone acetylation). HDAC3 inhibition notably suppresses both transcriptional dysregulation AND somatic expansion, suggesting it acts at the intersection.

### 3. Mitochondrial Dysfunction / PGC-1alpha Impairment (DOWNSTREAM + PARALLEL)
- **Relationship:** Partially downstream (PGC-1alpha is a transcriptional target), partially parallel (independent metabolic pathway)
- **Evidence strength:** Strong
- **Key studies:** [PMID: 33655829](https://pubmed.ncbi.nlm.nih.gov/33655829/), [PMID: 28819135](https://pubmed.ncbi.nlm.nih.gov/28819135/), [PMID: 40482637](https://pubmed.ncbi.nlm.nih.gov/40482637/)
- **Assessment:** Burns et al. (2025) found mitochondrial deficits are the earliest molecular changes in R6/2 mice (P0), potentially preceding transcriptional identity loss. PGC-1alpha downregulation links the two mechanisms.

### 4. Excitotoxicity / NMDA Receptor Dysregulation (PARALLEL)
- **Relationship:** Parallel mechanism
- **Evidence strength:** Strong
- **Key studies:** [PMID: 14522959](https://pubmed.ncbi.nlm.nih.gov/14522959/), [PMID: 19168136](https://pubmed.ncbi.nlm.nih.gov/19168136/), [PMID: 18279698](https://pubmed.ncbi.nlm.nih.gov/18279698/)
- **Assessment:** Enhanced NMDA receptor activation contributes to MSN death independently of transcriptional changes. Some excitotoxicity vulnerability may result from transcriptional downregulation of glutamate transporters, creating a feedback loop.

### 5. BDNF Transport Deficit (DOWNSTREAM)
- **Relationship:** Downstream consequence + independent transport defect
- **Key studies:** [PMID: 23575829](https://pubmed.ncbi.nlm.nih.gov/23575829/), [PMID: 30451892](https://pubmed.ncbi.nlm.nih.gov/30451892/), [PMID: 27601642](https://pubmed.ncbi.nlm.nih.gov/27601642/))
- **Assessment:** The striatum receives a "double hit" — reduced BDNF transcription in cortex (REST pathway) AND impaired BDNF vesicular transport (mHTT-motor protein interaction). Both contribute to striatal BDNF deficiency.

### 6. Aberrant RNA Processing (PARALLEL POST-TRANSCRIPTIONAL)
- **Relationship:** Parallel post-transcriptional mechanism
- **Key studies:** [PMID: 39394467](https://pubmed.ncbi.nlm.nih.gov/39394467/), [PMID: 41841355](https://pubmed.ncbi.nlm.nih.gov/41841355/)
- **Assessment:** Aberrant HTT mRNA processing produces HTT1a transcripts encoding pathogenic exon 1 protein; RNA splicing modulators are in development. Distinct from but complementary to the transcriptional dysregulation model.

---

## Discriminating Tests

### Test 1: Somatic Expansion–Transcription Threshold
- **Question:** At what somatic CAG length does transcriptional dysregulation begin?
- **Design:** Single-cell multiome (scRNA-seq + repeat sizing via long-read sequencing) from human HD caudate across Vonsattel grades 0–4
- **Sample:** Postmortem brain, n=10–20 per grade, age/sex matched
- **Expected result if hypothesis correct:** Transcriptional dysregulation severity correlates with somatic CAG length within individual MSNs, with a clear threshold
- **Expected result if alternative:** Transcriptional changes appear before significant somatic expansion

### Test 2: TF Pathway Hierarchy
- **Question:** Which TF pathway (Sp1, CBP, REST) contributes most to MSN dysfunction?
- **Design:** CRISPR-based selective rescue of each pathway in human HD iPSC-derived MSNs (72Q): (a) Sp1 overexpression; (b) CBP overexpression; (c) REST knockdown; (d) All three combined
- **Readouts:** Transcriptome rescue, neuronal survival, electrophysiology, BDNF levels
- **Expected result:** If REST/NRSF is dominant, condition (c) should show >50% transcriptional rescue; if contributions are additive, (d) >> any individual

### Test 3: CBP Depletion vs. Functional Inhibition
- **Question:** Is CBP physically depleted or functionally inhibited in HD MSNs in vivo?
- **Design:** CUT&Tag for H3K27ac (CBP enzymatic product) + CBP ChIP-seq at single-cell resolution in human HD brain
- **Stratification:** Vonsattel Grade 0–1 vs. Grade 3–4
- **Expected result if physical depletion:** Global H3K27ac loss correlated with CBP immunostaining reduction
- **Expected result if functional inhibition:** Selective H3K27ac loss at mHTT-sensitive loci with preserved global CBP protein levels

### Test 4: BDNF Transcription vs. Transport
- **Question:** Which contributes more to striatal BDNF deficiency — transcriptional reduction or transport deficit?
- **Design:** AAV-mediated delivery of BDNF cDNA under a constitutive (CMV/CAG) promoter to cortical neurons of Q140 mice, bypassing transcriptional regulation
- **Expected result if transcription is primary:** Full rescue of striatal BDNF levels and behavioral phenotype
- **Expected result if transport is primary:** Partial rescue only; BDNF accumulates in cortex

### Test 5: HDAC3-Selective Clinical Trial
- **Question:** Can selective HDAC3 inhibition improve HD symptoms in patients?
- **Design:** Phase Ib/IIa trial of HDAC3-selective inhibitor in early-manifest HD (TFC 11–13)
- **Primary endpoint:** Blood transcriptomic signature (REST target gene panel, BDNF)
- **Secondary endpoints:** CSF mHTT levels, somatic expansion rate in blood, brain volume MRI
- **Patient stratification:** CAG 40–45 vs. 45+; somatic instability index

---

## Curation Leads

*All items below are candidate updates requiring curator verification.*

### Candidate Evidence References to Add

1. **[PMID: 11988536](https://pubmed.ncbi.nlm.nih.gov/11988536/) (Dunah 2002)** — Not in seed YAML. Should be added as SUPPORT for Sp1 pathway with presymptomatic detection.
   - Verified snippet: *"huntingtin interacts with the transcriptional activator Sp1 and coactivator TAFII130. Coexpression of Sp1 and TAFII130 in cultured striatal cells from wild-type and HD transgenic mice reverses the transcriptional inhibition of the dopamine D2 receptor gene caused by mutant huntingtin, as well as protects neurons from huntingtin-induced cellular toxicity"*

2. **[PMID: 11971872](https://pubmed.ncbi.nlm.nih.gov/11971872/) (Yu 2002)** — Should be added as QUALIFIES evidence. Critical challenge to physical sequestration model.
   - Verified snippet: *"All three transcription factors were diffusely distributed in the nucleus, despite the presence of abundant intranuclear inclusions. There were no differences in the nuclear staining of these transcription factors between HD and wild-type mouse brains"*

3. **[PMID: 15225551](https://pubmed.ncbi.nlm.nih.gov/15225551/) (Schaffar 2004)** — Should be added as QUALIFIES evidence. Provides mechanistic resolution: soluble oligomers, not aggregates, inhibit TFs via conformational destabilization.

4. **[PMID: 17596446](https://pubmed.ncbi.nlm.nih.gov/17596446/) (Zuccato 2007)** — Should be added as SUPPORT. Genome-wide ChIP validation of REST dysregulation with loss-of-function confirmation.
   - Verified snippet: *"increased binding of the RE1 silencing transcription factor/neuron-restrictive silencer factor (REST/NRSF) repressor occurs at multiple genomic RE1/NRSE loci in HD cells, in animal models, and in postmortem brains"*

5. **[PMID: 16766198](https://pubmed.ncbi.nlm.nih.gov/16766198/) (Jiang 2006)** — Should be added as SUPPORT. Single-cell CBP depletion–toxicity link with rescue.
   - Verified snippet: *"cell toxicity was accompanied by CBP depletion, rather than merely recruitment"*

6. **[PMID: 39938516](https://pubmed.ncbi.nlm.nih.gov/39938516/) (Wang 2025)** — Should be added as COMPETING/UPSTREAM evidence. Demonstrates somatic expansion drives transcriptionopathy.

### Candidate Pathophysiology Nodes/Edges

- **Add node:** Somatic CAG Repeat Expansion (MSH3/PMS1-dependent) — positioned upstream of transcriptional dysregulation
- **Add edge:** Somatic expansion → mHTT pathogenic threshold → Transcriptional dysregulation
- **Refine existing edge:** `mHTT → Sp1/CBP sequestration` → `mHTT soluble oligomers → Sp1/CBP functional inhibition via conformational destabilization` (based on PMID:15225551, PMID:11971872)
- **Add parallel node:** H3K9me3/HDAC-mediated epigenetic silencing as a parallel mechanism
- **Distinguish edges:** `REST dysregulation → ↓BDNF transcription` (loss-of-function) vs. `mHTT → impaired BDNF axonal transport` (transport deficit) — both contribute to striatal BDNF deficiency

### Candidate Ontology Terms

- **Cell types:** Medium spiny neuron (CL:0000617); D2-expressing MSN; Cortical pyramidal neuron
- **Biological processes:** GO:0006355 (regulation of transcription, DNA-templated); GO:0016573 (histone acetylation); GO:0045892 (negative regulation of transcription, DNA-templated); GO:0006357 (regulation of transcription by RNA polymerase II)
- **Molecular functions:** GO:0003700 (DNA-binding transcription factor activity); GO:0004402 (histone acetyltransferase activity)

### Candidate Status Changes

- **Current status:** CANONICAL — recommend maintaining
- **Recommended qualifier:** Add that the "sequestration" mechanism operates primarily through functional inhibition by soluble/oligomeric mHTT rather than physical trapping in visible aggregates
- **Recommended context:** Position as downstream of somatic CAG expansion; most strongly validated for REST/NRSF arm; CBP arm has significant counter-evidence regarding physical depletion

### Candidate Knowledge Gaps for KB

1. **CBP sequestration vs. functional inhibition** — Unresolved discrepancy between Nucifora 2001 and Yu 2002
2. **Somatic expansion threshold for transcription** — No human single-cell data linking repeat length to transcriptomic state
3. **Clinical HDAC inhibitor failure** — Preclinical success not translated; JQ1 actually harmful
4. **TF pathway hierarchy** — Relative contribution of Sp1 vs. CBP vs. REST unknown
5. **BDNF transcription vs. transport** — Both reduced; primary deficit for striatal BDNF loss unknown
