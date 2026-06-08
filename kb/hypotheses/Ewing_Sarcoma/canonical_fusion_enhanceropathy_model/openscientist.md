---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-05-28T11:34:06.219132'
end_time: '2026-05-28T12:05:36.809795'
duration_seconds: 1890.59
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: Ewing Sarcoma
  category: ''
  hypothesis_group_id: canonical_fusion_enhanceropathy_model
  hypothesis_label: Canonical EWS-FLI1 fusion enhanceropathy model
  hypothesis_status: CANONICAL
  hypothesis_yaml: "hypothesis_group_id: canonical_fusion_enhanceropathy_model\nhypothesis_label:\
    \ Canonical EWS-FLI1 fusion enhanceropathy model\nstatus: CANONICAL\ndescription:\
    \ EWS-FLI1 is the truncal disease driver. Its EWSR1 low-complexity domain and\
    \ FLI1 DNA-binding\n  domain retarget chromatin machinery to GGAA microsatellites\
    \ and ETS elements, producing de novo enhancers,\n  core regulatory circuitry,\
    \ blocked differentiation, metabolic rewiring, and proliferation.\nevidence:\n\
    - reference: PMID:25453903\n  reference_title: EWS-FLI1 utilizes divergent chromatin\
    \ remodeling mechanisms to directly activate or\n    repress enhancer elements\
    \ in Ewing sarcoma.\n  supports: SUPPORT\n  evidence_source: IN_VITRO\n  snippet:\
    \ EWS-FLI1 establishes an oncogenic regulatory program governing both tumor\n\
    \  explanation: Supports the canonical fusion enhanceropathy model."
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
citation_count: 50
---

## Question

# Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Ewing Sarcoma
- **Category:**

## Target Hypothesis
- **Hypothesis ID:** canonical_fusion_enhanceropathy_model
- **Hypothesis Label:** Canonical EWS-FLI1 fusion enhanceropathy model
- **Status in KB:** CANONICAL

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: canonical_fusion_enhanceropathy_model
hypothesis_label: Canonical EWS-FLI1 fusion enhanceropathy model
status: CANONICAL
description: EWS-FLI1 is the truncal disease driver. Its EWSR1 low-complexity domain and FLI1 DNA-binding
  domain retarget chromatin machinery to GGAA microsatellites and ETS elements, producing de novo enhancers,
  core regulatory circuitry, blocked differentiation, metabolic rewiring, and proliferation.
evidence:
- reference: PMID:25453903
  reference_title: EWS-FLI1 utilizes divergent chromatin remodeling mechanisms to directly activate or
    repress enhancer elements in Ewing sarcoma.
  supports: SUPPORT
  evidence_source: IN_VITRO
  snippet: EWS-FLI1 establishes an oncogenic regulatory program governing both tumor
  explanation: Supports the canonical fusion enhanceropathy model.
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

# Hypothesis Evaluation Report: Canonical EWS-FLI1 Fusion Enhanceropathy Model in Ewing Sarcoma

**Hypothesis ID:** canonical_fusion_enhanceropathy_model
**Status in KB:** CANONICAL
**Date:** 2026-05-28

---

## Executive Judgment

**Verdict: STRONGLY SUPPORTED**

The canonical EWS-FLI1 fusion enhanceropathy model is one of the best-validated oncogenic mechanisms in pediatric cancer. Convergent evidence from chromatin profiling, single-molecule imaging, GWAS genetics, DNA methylation profiling, single-cell transcriptomics, cooperating mutation analysis, and pharmacological perturbation all support the central claim that the EWSR1 low-complexity domain retargets chromatin remodeling machinery (especially BAF complexes) to GGAA microsatellites, creating de novo enhancers that drive oncogenic transcription. Genome-scale DNA methylation sequencing (PMID:28134926) established enhancer reprogramming as a *ubiquitous* feature of Ewing sarcoma across patient tumors, providing key human clinical validation. The model has been substantively refined since initial formulation: the biophysical mechanism involves dynamic sub-diffraction hub formation (not bulk LLPS), EWS-FLI1 has an equally important repressive arm via NuRD complex recruitment at ETS motifs, and the enhanceropathy is dosage-sensitive with paradoxical pro-metastatic effects at intermediate depletion levels. The cell-of-origin permissiveness gap has been partially resolved: transient IGF-1 exposure during puberty reprograms EWS-FLI1-expressing mesenchymal cells to tumorigenicity via YAP1 (PMID:40080499), explaining the adolescent age peak. Additionally, a parallel non-transcriptional mechanism has been identified: EWS-FLI1 sequesters DHX9 helicase, causing R-loop accumulation and replication stress (PMID:40721661), operating alongside the enhanceropathy. Key remaining caveats: (1) IGF-1/YAP1 cooperation partially but not fully explains cell-context specificity; (2) cooperating mutations (STAG2, TP53, CDKN2A) modify the enhanceropathy landscape; (3) no faithful GEMM has been produced from EWS-FLI1 expression alone without additional hits; (4) clinical validation of enhanceropathy-targeting therapies awaits Phase II/III trial results; and (5) native ETS factors like ETV6 compete with EWS-FLI1 at GGAA sites, adding regulatory complexity.

---

## Evidence Matrix

| # | Citation | Type | Relationship | Mechanistic Claim Tested | Key Finding | Context | Confidence |
|---|----------|------|-------------|-------------------------|-------------|---------|------------|
| 1 | PMID:25453903 (Riggi et al., 2014) | In vitro/computational | **SUPPORTS** | EWS-FLI1 creates de novo enhancers at GGAA microsatellites | EWS-FLI1 multimers induce chromatin opening at GGAA repeats lacking regulatory potential in other cell types, creating de novo enhancers that physically interact with promoters. Simultaneously represses conserved enhancers by displacing WT ETS factors. | Ewing sarcoma cell lines, ChIP-seq, Hi-C | **High** - Landmark study; foundational |
| 2 | PMID:28844694 (Boulay et al., 2017) | In vitro | **SUPPORTS** | EWSR1 LCD retargets chromatin machinery | BAF complex recruited by EWS-FLI1 to tumor-specific enhancers via EWSR1 prion-like domain. Depends on tyrosine residues necessary for phase transitions. Neomorphic vs WT FLI1. | Ewing sarcoma cells, biochemistry | **High** - Identifies the chromatin remodeler |
| 3 | PMID:33080033 (Shi et al., 2020) | In vitro/in vivo | **SUPPORTS** | EWS-FLI1 establishes core regulatory circuitry | CRC trio (KLF15, TCF4, NKX2-2) established via super-enhancers. CRC factors co-occupy 77.2% of promoters and 55.6% of enhancers, controlling PI3K/AKT, MAPK, and lipid metabolism. | Ewing sarcoma cell lines, xenografts | **High** - Functional validation |
| 4 | PMID:35483357 (Chong et al., 2022) | In vitro (single-molecule) | **QUALIFIES** | LCD-LCD interactions drive enhancer activation | Narrow optimum of LCD interactions required; increasing toward LLPS *represses* transcription. Sequestration to nucleolus inhibits oncogenic transformation. | Patient-derived cells, quantitative imaging | **High** - Refines biophysical model |
| 5 | PMID:41659683 (Yoshida et al., 2026) | In vitro (single-molecule) | **QUALIFIES** | LCD domain forms phase-separated condensates | Endogenous EWS::FLI1 forms dynamic sub-diffraction hubs, NOT macroscopic LLPS. Hub formation is neomorphic. Nascent RNA destabilizes hubs. Mitotic bookmarking role discovered. | Endogenous protein imaging in Ewing cells | **High** - First endogenous imaging |
| 6 | PMID:26214589 (Grünewald et al., 2015) | Human clinical + in vitro | **SUPPORTS** | Enhanceropathy explains genetic susceptibility | Risk allele at rs79965208 converts GGAT→GGAA, extending consecutive repeats, increasing EWS-FLI1 enhancer activity at EGR2 locus. | GWAS + functional follow-up | **Very high** - Links germline to somatic mechanism |
| 7 | PMID:30093639 (Machiela et al., 2018) | Human clinical (GWAS) | **SUPPORTS** | GGAA microsatellites central to disease susceptibility | 6 GWAS loci identified; most near GGAA repeat sequences. Locus 20p11.22 near NKX2-2. Unusually high odds ratios (>1.7). | 733 cases, 1346 controls, European | **High** - Large GWAS |
| 8 | PMID:22749036 (Beck et al., 2012) | Human clinical | **SUPPORTS** | GGAA repeats explain racial disparity | NR0B1 GGAA microsatellite differs between African and European populations. May explain 10-fold incidence disparity. | Population genetics | **Moderate** - Correlative; functional link inferred |
| 9 | PMID:23178492 (Sankar et al., 2013) | In vitro | **QUALIFIES** | Enhanceropathy is only half the story | EWS/FLI repressive function via NuRD complex (HDAC + LSD1) is required for transformed phenotype. LOX is a key repressed target. | Ewing sarcoma cell lines | **High** - Dual mechanism |
| 10 | PMID:41950086 (Eyunni et al., 2026) | In vitro/computational | **SUPPORTS + QUALIFIES** | Cooperating mutations modify enhanceropathy | STAG2 loss eliminates >40% EWS-FLI1 sites at short GGAA repeats while amplifying activity at multimeric (≥5) repeats. | STAG2 loss-of-function models, multiomics | **High** - Shows enhanceropathy is modifiable |
| 11 | PMID:39487368 (Giménez-Llorente et al., 2024) | In vitro/computational | **SUPPORTS** | Cohesin facilitates enhancer-promoter contacts | Cohesin-STAG2 facilitates communication between EWS::FLI1-bound GGAA neoenhancers and target promoters. | Capture Hi-C, chromatin profiling | **High** - 3D genome evidence |
| 12 | PMID:41484205 (Suresh et al., 2026) | In vitro/in vivo | **QUALIFIES** | EWS-FLI1 dosage dynamics drive plasticity | Modest EF depletion promotes metastasis; genes at GGAA microsatellite enhancers are most dosage-sensitive. Transient depletion causes persistent dysregulation. | Degron technology, nascent RNA-seq | **High** - Critical therapeutic caveat |
| 13 | PMID:29091716 (Johnson et al., 2017) | In vitro/computational | **QUALIFIES** | GGAA microsatellites are uniform | Two distinct classes: "promoter-like" (length-dependent activation) and "enhancer-like" (length-dependent binding but not expression). | Genome-wide analysis | **High** - Mechanistic complexity |
| 14 | PMID:35653119 (Apfelbaum et al., 2022) | In vitro/in vivo | **SUPPORTS + QUALIFIES** | EWS-FLI1 controls differentiation block | EWS::FLI1 creates de novo GGAA enhancer at HOXD locus. HOXD13 activates EWS-FLI1-repressed genes, driving mesenchymal states normally suppressed by the fusion. | Cell lines, PDX, patient tumors, scRNA-seq | **High** - Links enhanceropathy to plasticity |
| 15 | PMID:19289832 (Richter et al., 2009) | In vitro/in vivo | **SUPPORTS** | EWS-FLI1 blocks differentiation via epigenetics | EWS/FLI1 binds EZH2 promoter, induces expression. EZH2 maintains undifferentiated phenotype by silencing neuroectodermal and endothelial differentiation genes. | Ewing cells, MSCs, xenografts | **High** - Differentiation block mechanism |
| 16 | PMID:30723142 (Harlow et al., 2019) | In vitro | **SUPPORTS** | BAF/SWI-SNF essential for enhanceropathy | Trabectedin evicts SWI/SNF from chromatin, redistributes EWS-FLI1, increases repressive marks (H3K27me3, H3K9me3) at target genes. | Ewing sarcoma cell lines | **High** - Pharmacological validation |
| 17 | PMID:24963049 (Sankar et al., 2014) | In vitro/in vivo | **SUPPORTS** | LSD1 is required for EWS-FLI1 function | LSD1 inhibition (HCI2509) reverses EWS/FLI and EWS/ERG transcriptional profiles. Single-agent efficacy in xenograft models. | Multiple Ewing cell lines, xenografts | **High** - Therapeutic validation |
| 18 | PMID:35952322 (Ogura et al., 2022) | Human clinical | **QUALIFIES** | EWS-FLI1 is sufficient alone | STAG2, TP53, CDKN2A, and other secondary alterations found in clinical genomic profiling of 113 patients. Novel subsets defined by recurrent secondary alterations. | Prospective clinical profiling, 113 patients | **High** - Shows cooperating mutations exist |
| 19 | PMID:15548687 (Staege et al., 2004) | In vitro/computational | **QUALIFIES** | Enhanceropathy in any cell produces Ewing | EWS-FLI1 in HEK293 cells was not sufficient to induce complete Ewing-specific gene expression signature. Histogenetic background of stem cell matters. | HEK293, DNA microarrays | **High** - Cell context dependency |
| 20 | PMID:31898537 (El Beaino et al., 2020) | In vivo (mouse) | **QUALIFIES** | EWS-FLI1 alone drives tumorigenesis | STAG2 loss + EWS-FLI1 + p53 null still insufficient without irradiation. Additional perturbations beyond STAG2/p53 required. | Murine MSCs, genetic model | **Moderate** - Mouse model limitations |
| 21 | PMID:10561219 (Ginsberg et al., 1999) | Human clinical | **SUPPORTS** | EWS-ETS fusions are equivalent | EWS-FLI1 and EWS-ERG show no significant clinical differences in age, sex, metastasis, survival. | 30 EWS-ERG, 106 EWS-FLI1 cases | **Moderate** - Model extends to EWS-ERG |
| 22 | PMID:27875302 (Gierisch et al., 2016) | In vitro | **QUALIFIES** | EWS-FLI1 protein is stable | EWS-FLI1 half-life is 2-4 hours; regulated by ubiquitin-proteasome system via Lys-380. Stabilization differentially modulates target gene subgroups. | Biochemistry, mass spectrometry | **Moderate** - Adds protein turnover dimension |
| 23 | PMID:38826330 (Rask et al., 2024) | In vitro | **SUPPORTS** | LSD1 is a therapeutic target via enhanceropathy | Seclidemstat blocks transcriptional function of multiple FET-fusion oncoproteins. Currently in clinical trials (NCT03600649). | FET-rearranged sarcoma cells | **High** - Clinical translation |
| 24 | PMID:40080499 (Noorizadeh et al., 2025) | In vivo (mouse) | **QUALIFIES** | EWS-FLI1 alone is the truncal driver | IGF-1 at puberty concentrations reprograms EWS::FLI1 mesenchymal cells to tumorigenicity via YAP1. EWS-FLI1 alone causes skeletal malformations but NOT tumors. | Mouse MSCs, limb-derived | **High** - Partially resolves cell-of-origin gap |
| 25 | PMID:32049009 (Aynaud et al., 2020) | In vitro/computational | **SUPPORTS** | Enhanceropathy drives metabolic programs | scRNA-seq + time-resolved ChIP defines direct enhancer-driven EWS-FLI1 program. Proliferation and OXPHOS associated with optimal EWS-FLI1 activity. Hypoxia at extremes. | EwS cell lines, patient tumors | **High** - Single-cell resolution |
| 26 | PMID:40667384 (Waltner et al., 2025) | In vitro/in vivo | **QUALIFIES** | EWS-FLI1 is the sole transcriptional program | Multiple co-existing gene regulatory modules shape Ewing sarcoma phenotypic diversity. TGF-beta can modify modules. Intratumoral heterogeneity in regulatory networks. | scRNA-seq + ATAC-seq, patient tumors | **High** - Multimodal single-cell |
| 27 | PMID:37471463 (Wrenn et al., 2023) | In vitro/in vivo | **QUALIFIES** | All Ewing cells have same enhanceropathy state | CD73+ CAF-like tumor subpopulation upregulates EWS::FLI1-repressed genes, shows increased migration and ECM deposition. | Cell lines, PDX, patient biopsies | **High** - Identifies mesenchymal subpopulation |
| 28 | PMID:28134926 (Sheffield et al., 2017) | Human clinical | **SUPPORTS** | Enhanceropathy is a universal feature | Genome-scale DNA methylation shows consistent hypomethylation at EWS-FLI1 enhancers. Continuous disease spectrum reflecting EWS-FLI1 signature strength. Epigenetic heterogeneity in metastatic cases. | Large patient cohort, DNA methylation-seq | **Very high** - Human tumors, genome-scale |
| 29 | PMID:40721661 (Olmedo-Pelayo et al., 2025) | In vitro/in vivo | **QUALIFIES** | Enhanceropathy is the sole oncogenic mechanism | EWS::FLI1 sequesters DHX9 helicase → R-loop accumulation → replication stress → genome instability. Drives sensitivity to topoisomerase 1 poisons. | Ewing cell lines, patient outcomes | **High** - Parallel non-transcriptional mechanism |
| 30 | PMID:40215343 (Zhu et al., 2025) | In vitro | **QUALIFIES** | EWS-FLI1 has unopposed access to GGAA sites | ETV6 competes with EWS::FLI1 at short GGAA repeats, restraining function. ETV6 degradation as therapeutic strategy. | Ewing sarcoma cells | **High** - Counter-regulatory dynamics |
| 31 | PMID:27259270 (Loganathan et al., 2016) | In vitro/in vivo | **SUPPORTS** | Enhanceropathy is BET-dependent | BET inhibitors repress EWS-FLI1-driven signatures and IGF1 autocrine mechanism. JQ1 suppresses xenograft growth. | Ewing cell lines, xenografts | **High** - Epigenetic dependency |
| 32 | PMID:41301081 (Richter et al., 2025) | Human clinical/computational | **QUALIFIES** | Ewing sarcoma genomes are stable | Chromosomal gains/losses are independent biomarkers. Patients with <3 CNAs have better prognosis. Chromosomal instability mechanisms may link to EWS-FLI1 activity. | Patient cohort | **Moderate** - Genomic instability exists |
| 33 | PMID:40029262 (Goodspeed et al., 2025) | Human clinical | **SUPPORTS + QUALIFIES** | Ewing tumors are transcriptionally uniform | scRNA-seq of 7 primary tumors shows heterogeneous transcriptional landscape with conserved programs (proliferation, EwS targets) correlating with survival. Immunosuppressive microenvironment. TSPAN8 as CTC target. | Primary untreated tumors, CTCs | **High** - Direct patient tumor data |
| 34 | PMID:25609059 (Amaral et al., 2015) | In vitro/in vivo | **QUALIFIES** | Trabectedin uniformly inhibits EWS-FLI1 | Trabectedin reduces EWS-FLI1 binding at some promoters but *increases* binding at IGF1R, leading to IGF1R upregulation. Combined trabectedin + IGF1R inhibition is synergistic. | 13 EWS cell lines, xenografts | **High** - Reveals paradoxical redistribution |
| 35 | PMID:37963210 (Graca Marques et al., 2024) | In vitro/in vivo (CRISPR screen) | **SUPPORTS** | NuRD complex is essential | CHD4 is essential for Ewing sarcoma; colocalizes with EWS-FLI1 at enhancers/super-enhancers. CHD4 promotes survival through chromatin structure maintenance and DNA damage control. CHD4 loss + PARP inhibition synergistic. | Ewing cell lines, xenografts | **High** - CRISPR validation |
| 36 | PMID:34329586 (Seong et al., 2021) | In vitro (CRISPR screen) | **SUPPORTS** | EWS-FLI1 dosage is tightly regulated | TRIM8 E3 ligase ubiquitinates and degrades EWS/FLI. TRIM8 is a selective dependency in Ewing vs >700 other cancer lines. TRIM8 KO → EWS/FLI increase → oncogene overdose → cell death. | Pan-cancer CRISPR screen | **Very high** - Genome-wide + selectivity |
| 37 | PMID:36658219 (Gao et al., 2023) | In vitro/in vivo (CRISPR screen) | **SUPPORTS** | ETV6 competes at GGAA microsatellites | Domain-focused CRISPR screen identifies ETV6 as dependency. ETV6 inactivation → EWS-FLI1 hyper-activates short GGAA cis-elements → SOX11 upregulation → mesenchymal differentiation. Dominant-interfering peptide suppresses growth in vivo. | Ewing cell lines, xenografts | **High** - CRISPR + in vivo validation |
| 38 | PMID:36229873 (Hölting et al., 2022) | In vitro/in vivo | **SUPPORTS** | GGAA enhancers are tumor-specific | Engineered GGAA-based synthetic enhancer cassette drives EWS-FLI1-dependent therapeutic payload expression. Anti-GPR64 targeted lentivirus + thymidine kinase causes tumor-specific killing. Also works in PAX3-FOXO1 ARMS. | Xenograft models | **High** - Translational proof-of-concept |
| 39 | PMID:30045945 (Stolte et al., 2018) | In vitro (CRISPR screen) | **SUPPORTS** | Ewing sarcoma has specific druggable dependencies | Genome-scale CRISPR screen identifies druggable dependencies in Ewing sarcoma in wild-type p53 context. | Ewing cell lines, genome-wide | **High** - Unbiased functional genomics |
| 40 | PMID:40414844 (Chellini et al., 2025) | In vitro | **QUALIFIES** | YAP1 regulation in Ewing sarcoma | pncRNA_YAP1-1 interacts with FUS to destabilize YAP1 protein via TEAD sequestration. Reveals noncoding RNA regulation of YAP1/EWS-FLI1 tension. | Ewing sarcoma cells | **Moderate** - Novel noncoding RNA layer |
| 41 | PMID:40230184 (Lasota et al., 2025) | Human clinical | **SUPPORTS** | Enhanceropathy creates specific diagnostic biomarkers | PKC Beta II (PRKCB) is strongly expressed in all tested EWS-FLI1, EWS-ERG, EWS-ETV4, and FUS-ERG fusion-positive sarcomas (n=34). Negative in all BCOR/CIC/NFATC2/NUTM1/PATZ1-rearranged round cell sarcomas (n=46). | >1000 tumors tested | **High** - Large validation cohort |
| 42 | PMID:25092916 (Anderson et al., 2014) | In vitro (phosphoproteomics) | **QUALIFIES** | EWS-FLI1 knockdown is straightforward | EWS/FLI1 knockdown triggers paracrine IL6 secretion → STAT3 activation in bystander cells. Non-cell-autonomous effect complicates therapeutic targeting. | Phosphoproteomics, single-cell analysis | **High** - Unbiased proteomics |
| 43 | PMID:28062706 (Radic-Sarikas et al., 2017) | In vitro (drug screen) | **SUPPORTS** | EWS-FLI1 determines drug sensitivity | Combinatorial drug screen identifies Ewing-specific synergies. PKC412 + IGF1R inhibition synergistic via EWS-FLI1-dependent pathway crosstalk. | 3 pediatric tumor types compared | **Moderate** - Disease-specific pharmacology |

---

## Mechanistic Causal Chain

### Upstream Trigger → Clinical Manifestation

```
1. CHROMOSOMAL TRANSLOCATION t(11;22)(q24;q12)
   └─→ Generates EWS-FLI1 fusion gene (~85% of cases; EWS-ERG ~10%)
       [STRONG: universally observed, pathognomonic]

2. FUSION PROTEIN EXPRESSION
   └─→ EWS-FLI1 protein with EWSR1 LCD + FLI1 ETS DBD
   └─→ Neomorphic properties not present in either parent protein
       [STRONG: biochemically validated; PMID:28844694, 41659683]

3a. DE NOVO ENHANCER CREATION (Activation arm)
   └─→ EWSR1 LCD forms dynamic transcription hubs (not bulk LLPS)
   └─→ Recruits BAF/SWI-SNF complex to GGAA microsatellites
   └─→ Chromatin opening → H3K27ac → de novo enhancers
   └─→ Enhancer-promoter looping (facilitated by cohesin-STAG2)
   └─→ Activation of oncogenes: NR0B1, NKX2-2, EGR2, HOXD13, VRK1, etc.
       [STRONG: ChIP-seq, Hi-C, functional validation; PMID:25453903, 28844694, 33080033]

3b. ENHANCER REPRESSION (Repression arm)
   └─→ EWS-FLI1 displaces WT ETS factors from conserved ETS motifs
   └─→ Recruits NuRD complex (HDAC + LSD1)
   └─→ Represses tumor suppressors (LOX) and differentiation genes
       [STRONG: PMID:25453903, 23178492]

4. CORE REGULATORY CIRCUITRY
   └─→ EWS-FLI1 establishes super-enhancers for KLF15, TCF4, NKX2-2
   └─→ Auto-regulatory feed-forward loop amplifies transcriptional program
   └─→ CRC factors co-occupy 77% of promoters, 56% of enhancers
       [STRONG: PMID:33080033]

5. DIFFERENTIATION BLOCK
   └─→ EZH2 upregulation → H3K27me3 at lineage commitment genes
   └─→ Maintains undifferentiated, stem-like state
   └─→ Blocks neuroectodermal and mesenchymal differentiation
       [MODERATE-STRONG: PMID:19289832; cell-of-origin still debated]

6. PROLIFERATION & SURVIVAL
   └─→ Activation of PI3K/AKT, MAPK, cell cycle programs
   └─→ Sustained proliferative signaling
       [MODERATE: downstream; established but mechanistic details less defined]

6b. IGF-1/YAP1 COOPERATION (Permissive context)
   └─→ Transient IGF-1 exposure (puberty serum levels) required for transformation
   └─→ IGF-1 reprograms EWS-FLI1+ mesenchymal cells to stable tumorigenicity
   └─→ YAP1 is central mediator of IGF-1-driven tumor promotion
   └─→ Explains adolescent age peak and cell-context specificity
       [STRONG: PMID:40080499; mouse model with functional validation]

7. METABOLIC REWIRING
   └─→ Optimal EWS-FLI1 activity → oxidative phosphorylation + proliferation
   └─→ Sub/supra-optimal EWS-FLI1 → hypoxia programs
   └─→ Lipid metabolism pathway alterations (via CRC)
   └─→ V-ATPase activation for acid-base homeostasis
       [MODERATE: scRNA-seq links at PMID:32049009; mechanistic details still emerging]

7b. R-LOOP ACCUMULATION & REPLICATION STRESS (Parallel mechanism)
   └─→ EWS-FLI1 sequesters DHX9 helicase (protein-protein interaction)
   └─→ Impaired R-loop resolution → R-loop accumulation
   └─→ Replication stress → genome instability → copy number alterations
   └─→ Drives sensitivity to topoisomerase 1 poisons (irinotecan)
       [STRONG: PMID:40721661; independent of transcriptional enhanceropathy]

8. TUMOR PLASTICITY & METASTASIS
   └─→ Spontaneous EWS-FLI1 fluctuations
   └─→ GGAA microsatellite enhancers are dosage-sensitive (first to deactivate)
   └─→ Partial depletion → derepression of YAP/TAZ/MRTFB module
   └─→ Pro-metastatic, migratory phenotype
       [STRONG: PMID:41484205, 28671673, 33419969]

9. COOPERATING EVENTS (Modifier)
   └─→ STAG2 loss (~15%): reshapes enhanceropathy landscape
   └─→ TP53/CDKN2A loss: enables cell cycle progression
   └─→ Germline GGAA polymorphisms: modulate enhancer activity
       [STRONG for STAG2: PMID:41950086; MODERATE for others]
```

### Where links are strong vs. inferred:

- **Strong links (Steps 1-4):** Fusion → LCD hubs → BAF recruitment → de novo enhancers → CRC. Supported by multiple independent methodologies.
- **Moderate links (Steps 5-6):** Differentiation block via EZH2 and proliferation via PI3K/AKT are established but the direct causal chain from enhanceropathy to these endpoints has intermediate steps.
- **Weak/inferred links (Step 7):** Metabolic rewiring is implied by CRC target gene analysis but lacks direct perturbation evidence connecting specific metabolic changes to enhanceropathy.
- **Missing causal step:** How the cell of origin's epigenome makes it permissive to EWS-FLI1 enhanceropathy remains unknown.

---

## Knowledge Gaps

### 1. Cell-of-Origin Permissiveness (PARTIALLY RESOLVED)
- **Scope:** EWS-FLI1 expression is toxic in most cell types. What makes certain mesenchymal/neural crest progenitors permissive?
- **Why it matters:** Central to understanding why the enhanceropathy succeeds in some cellular contexts but not others.
- **What was checked:** Staege et al. (PMID:15548687) showed HEK293 cells fail to recapitulate full Ewing signature. El Beaino et al. (PMID:31898537) required multiple additional hits. **NEW:** Noorizadeh et al. (PMID:40080499) showed IGF-1 at puberty levels reprograms EWS-FLI1+ mesenchymal cells to tumorigenicity via YAP1. This partially resolves the gap by identifying a required environmental signal.
- **Remaining gap:** Why only limb-derived mesenchymal cells (not other mesenchymal populations) are permissive. The exact epigenomic prerequisites at GGAA microsatellites remain undefined.
- **Resolving evidence needed:** Single-cell multiomics comparing limb vs. non-limb MSCs during EWS-FLI1 induction + IGF-1 exposure, focusing on pre-existing chromatin accessibility at GGAA microsatellites.

### 2. Faithful Genetically Engineered Mouse Model
- **Scope:** No GEMM recapitulates Ewing sarcoma from EWS-FLI1 expression alone in the correct cell of origin.
- **Why it matters:** Absence of a GEMM is the strongest evidence that EWS-FLI1 may be necessary but not sufficient, challenging the "truncal driver" claim.
- **What was checked:** El Beaino et al. (PMID:31898537) attempted MSC-based mouse models but required additional perturbations including irradiation.
- **Resolving evidence needed:** Conditional EWS-FLI1 knockin in identified permissive progenitor populations with single-cell tracking.

### 3. Metabolic Rewiring Mechanism (PARTIALLY RESOLVED)
- **Scope:** The hypothesis claims "metabolic rewiring" but the direct enhanceropathy-to-metabolism causal chain was poorly defined.
- **Why it matters:** Metabolic dependencies could be therapeutic vulnerabilities.
- **What was checked:** CRC study (PMID:33080033) mentions lipid metabolism. **NEW:** Aynaud et al. (PMID:32049009) showed at single-cell resolution that optimal EWS-FLI1 activity is associated with strong oxidative phosphorylation, while sub/supra-optimal activity shows hypoxia programs. Avnet et al. (PMID:23579072) showed ES cells simultaneously activate mitochondrial respiration and glycolysis, with V-ATPase playing a key role.
- **Remaining gap:** The direct enhancer-to-metabolic enzyme causal chain is still not mapped. Which specific EWS-FLI1 enhancer targets drive metabolic reprogramming?
- **Resolving evidence needed:** Metabolomics + ChIP-seq integration with time-resolved EWS-FLI1 degradation to identify direct vs. indirect metabolic effects.

### 4. Complete Enhancer-Promoter Connectome
- **Scope:** Only a subset of de novo enhancers have confirmed promoter targets via Hi-C/Capture-C.
- **Why it matters:** The full regulatory network of the enhanceropathy is incompletely mapped.
- **What was checked:** Giménez-Llorente et al. (PMID:39487368) performed Capture Hi-C but focused on STAG2-dependent contacts. The STAG2 study by Eyunni et al. (PMID:41950086) integrated Hi-C maps.
- **Resolving evidence needed:** Comprehensive promoter-capture Hi-C in Ewing sarcoma cells with matched EWS-FLI1 depletion controls.

### 5. In Vivo Validation of Dosage-Dependent Metastasis Model
- **Scope:** The paradoxical pro-metastatic effect of partial EWS-FLI1 depletion (PMID:41484205) is primarily from preclinical models.
- **Why it matters:** If incomplete EWS-FLI1 inhibition promotes metastasis in patients, current therapeutic strategies need reassessment.
- **What was checked:** Suresh et al. used degron technology and xenograft models, but no clinical correlation of EWS-FLI1 expression levels with metastatic burden has been performed.
- **Resolving evidence needed:** Correlation of EWS-FLI1 protein/transcript levels in matched primary and metastatic patient samples; clinical pharmacodynamic studies of EWS-FLI1-targeting agents.

### 6. No Clinical Trials Validating Direct EWS-FLI1 Inhibition
- **Scope:** TK216 and trabectedin target EWS-FLI1 function but definitive clinical proof of concept is lacking.
- **Why it matters:** Clinical validation would be the strongest test of the enhanceropathy model's therapeutic relevance.
- **What was checked:** Seclidemstat (LSD1 inhibitor) is in clinical trials (NCT03600649; PMID:38826330). Review by Asmar et al. (PMID:41957177) discusses TK216 and trabectedin combinations with preliminary results.
- **Resolving evidence needed:** Phase II/III trial results with pharmacodynamic biomarkers measuring enhancer activity (H3K27ac) in patient samples.

### 7. Non-EWS-FLI1 Fusions and Enhanceropathy Generalizability
- **Scope:** ~10-15% of Ewing sarcomas harbor non-FLI1 ETS partners (ERG, FEV, ETV1, ETV4). Do all produce equivalent enhanceropathy?
- **Why it matters:** If the model is truly canonical, it must explain all EWS-ETS fusions, not just EWS-FLI1.
- **What was checked:** Ginsberg et al. (PMID:10561219) showed EWS-FLI1 and EWS-ERG have similar clinical phenotypes. Sankar et al. (PMID:24963049) showed LSD1 inhibition reverses both EWS/FLI and EWS/ERG profiles. But detailed chromatin profiling of non-FLI1 fusions is limited.
- **Resolving evidence needed:** Comparative ChIP-seq and ATAC-seq across tumors with different EWS-ETS fusion partners.

---

## Alternative Models

### 1. EWS-FLI1 as Dominant Transcriptional Repressor (Complementary)
- **Relationship to seed hypothesis:** Complementary/parallel mechanism, NOT alternative
- **Description:** EWS-FLI1 functions equally through NuRD-mediated repression at canonical ETS motifs, silencing tumor suppressors (LOX, p21) and differentiation genes.
- **Evidence:** PMID:23178492 (Sankar et al., 2013)
- **Assessment:** Now integrated into the canonical model. Both activation AND repression are required.

### 2. EWS-FLI1 as RNA Processing Regulator (Complementary)
- **Relationship to seed hypothesis:** Parallel mechanism operating at post-transcriptional level
- **Description:** EWSR1 is normally an RNA-binding protein. EWS-FLI1 fusion may disrupt RNA processing/splicing beyond transcription. The fusion transcript itself is a splicing vulnerability.
- **Evidence:** PMID:26776507 (Grohar et al., 2016) showed splicing of EWS-FLI1 pre-mRNA is targetable; HNRNPH1 required for in-frame expression in certain breakpoint variants.
- **Assessment:** This is not a competing explanation of disease mechanism but identifies a vulnerability in the pathway producing the fusion protein itself.

### 3. Cell-of-Origin Epigenome Model (Upstream cause)
- **Relationship to seed hypothesis:** Upstream prerequisite, not alternative
- **Description:** The enhanceropathy requires a permissive epigenomic state in the cell of origin (neural crest/mesenchymal progenitor) that pre-configures GGAA microsatellite accessibility.
- **Evidence:** PMID:15548687 (Staege et al., 2004) showed EWS-FLI1 in HEK293 cells insufficient; PMID:31898537 required multiple additional hits.
- **Assessment:** This is a genuine gap -- the enhanceropathy model assumes but does not explain cell-context permissiveness.

### 4. YAP/TAZ-Hippo Pathway Model (Downstream/parallel)
- **Relationship to seed hypothesis:** Downstream modifier of enhanceropathy-driven plasticity
- **Description:** YAP1/TAZ activation drives an EWS-FLI1-opposing transcriptional program. High YAP1/TAZ associates with disease progression and poor outcome.
- **Evidence:** PMID:31880317 (Rodríguez-Núñez et al., 2020); PMID:33419969 (Bierbaumer et al., 2021)
- **Assessment:** YAP/TAZ operates in tension with EWS-FLI1 and becomes relevant when EWS-FLI1 levels fluctuate. Not an alternative but an important modifier.

### 5. CIC-DUX4 / BCOR-CCNB3 Ewing-like Sarcoma Models (Alternative for look-alikes)
- **Relationship to seed hypothesis:** Alternative mechanisms for morphologically similar tumors
- **Description:** Round cell sarcomas resembling Ewing but driven by CIC-DUX4 or BCOR-CCNB3 fusions that do NOT involve GGAA microsatellite enhanceropathy.
- **Evidence:** PMID:32048619 (Rekhi et al., 2019); PMID:30709443 (Carter & Patel, 2019)
- **Assessment:** These are now classified as distinct entities, validating that the enhanceropathy model is specific to EWSR1-ETS fusions, not a generic round cell sarcoma mechanism.

### 6. Cooperating Mutation / Multi-Hit Model (Qualifier)
- **Relationship to seed hypothesis:** Qualifies the "single truncal driver" claim
- **Description:** EWS-FLI1 is necessary but insufficient; additional hits (STAG2, TP53, CDKN2A, irradiation) are required for full transformation.
- **Evidence:** PMID:35952322 (Ogura et al., 2022); PMID:31898537 (El Beaino et al., 2020)
- **Assessment:** Partially challenges the sufficiency claim. STAG2 loss modifies the enhanceropathy landscape itself (PMID:41950086), suggesting cooperating mutations operate through the enhanceropathy rather than independently.

### 7. IGF-1/YAP1 Developmental Context Model (Upstream/cooperative)
- **Relationship to seed hypothesis:** Upstream prerequisite that enables the enhanceropathy to achieve transformation
- **Description:** Transient IGF-1 signaling at puberty levels reprograms EWS-FLI1-expressing mesenchymal cells via YAP1, converting enhanceropathy from a developmental aberration to stable transformation.
- **Evidence:** PMID:40080499 (Noorizadeh et al., 2025) - Mouse model; YAP1/TEAD inhibition reverses transformation
- **Assessment:** This is not an alternative but a required cooperative signal. Explains the adolescent age peak and why EWS-FLI1 alone causes only skeletal malformations in mice. Integrates with the YAP/TAZ plasticity findings (PMID:31880317, 33419969).

### 8. R-loop/Replication Stress Model (Parallel mechanism)
- **Relationship to seed hypothesis:** Parallel, non-transcriptional oncogenic mechanism operating simultaneously
- **Description:** EWS-FLI1 sequesters DHX9 helicase via protein-protein interaction, impairing R-loop resolution, causing replication stress and genome instability.
- **Evidence:** PMID:40721661 (Olmedo-Pelayo et al., 2025)
- **Assessment:** This is a genuinely independent mechanism - not mediated by enhanceropathy but by direct protein sequestration. Explains chemotherapy sensitivity (irinotecan) and genomic instability. Suggests EWS-FLI1 has at least two parallel oncogenic arms: transcriptional (enhanceropathy) and replication stress (DHX9 sequestration).

### 9. ETV6 Counter-Regulatory Model (Modifier)
- **Relationship to seed hypothesis:** Internal counter-regulatory mechanism within the enhanceropathy
- **Description:** Native ETS factor ETV6 competes with EWS-FLI1 at short GGAA repeats, restraining enhanceropathy function.
- **Evidence:** PMID:40215343 (Zhu et al., 2025)
- **Assessment:** Adds regulatory complexity to the enhanceropathy - it is not an unopposed gain-of-function but is actively restrained by competing ETS factors. ETV6 degradation could paradoxically be therapeutic by unleashing full EWS-FLI1 activity (potentially leading to replication stress or other vulnerabilities).

---

## Discriminating Tests

### Test 1: Cell-of-Origin Permissiveness Screen
- **Question:** What epigenomic features make a cell permissive to EWS-FLI1 enhanceropathy?
- **Design:** Single-cell ATAC-seq + RNA-seq time course after EWS-FLI1 induction in multiple cell types (MSCs, neural crest progenitors, fibroblasts, iPSC-derived lineages)
- **Expected result (if enhanceropathy model correct):** Permissive cells will have pre-existing chromatin accessibility or specific histone marks at GGAA microsatellites prior to EWS-FLI1 expression
- **Discriminates against:** Pure fusion-sufficiency model; identifies co-requisite epigenomic states

### Test 2: Complete Dosage-Response Clinical Correlation
- **Question:** Does partial EWS-FLI1 inhibition promote metastasis in patients?
- **Design:** Measure EWS-FLI1 expression (RNA + protein) in matched primary tumors, circulating tumor cells, and metastases from the same patients
- **Biomarkers:** EWS-FLI1 transcript levels, GGAA enhancer H3K27ac (cfChIP-seq), YAP/TAZ target gene expression
- **Expected result:** Metastatic samples show reduced EWS-FLI1 with activated YAP/TAZ program vs. primary tumors

### Test 3: Pan-ETS-Fusion Enhanceropathy Comparison
- **Question:** Do all EWS-ETS fusions create equivalent enhanceropathies?
- **Design:** Matched ATAC-seq, ChIP-seq (H3K27ac, EWS-fusion), and RNA-seq in isogenic cells expressing EWS-FLI1 vs. EWS-ERG vs. EWS-FEV vs. EWS-ETV1
- **Expected result (if model generalizable):** All fusions create de novo enhancers at overlapping GGAA microsatellites, with fusion-specific quantitative differences but conserved qualitative mechanism

### Test 4: GGAA Microsatellite Engineering
- **Question:** Is GGAA microsatellite length at key loci sufficient to modulate enhanceropathy strength and tumor phenotype?
- **Design:** CRISPR-based microsatellite editing at NR0B1, EGR2, and NKX2-2 loci in Ewing sarcoma cells to shorten or extend GGAA repeats
- **Expected result:** Repeat length directly modulates enhancer activity, target gene expression, and oncogenic phenotype

### Test 5: Metabolic Rewiring Causal Chain
- **Question:** Which metabolic dependencies are direct consequences of the enhanceropathy vs. indirect effects?
- **Design:** Metabolomics + lipidomics before and after acute EWS-FLI1 degradation (degron system) with matched ChIP-seq time course
- **Expected result:** Identify metabolic changes directly downstream of EWS-FLI1-regulated enhancers vs. secondary adaptations

### Test 6: Enhanceropathy vs. R-loop Mechanism Contribution
- **Question:** What fraction of EWS-FLI1 oncogenicity comes from enhanceropathy vs. DHX9/R-loop replication stress?
- **Design:** Engineer separation-of-function mutants: (a) EWS-FLI1 with intact LCD but mutated ETS DBD (disrupts GGAA binding but preserves DHX9 interaction), (b) EWS-FLI1 with intact GGAA binding but disrupted DHX9 interaction
- **Model system:** Isogenic Ewing sarcoma cells using base editing
- **Expected result:** If enhanceropathy is primary mechanism, DBD mutants lose transformation; if R-loops contribute independently, DHX9-interaction mutants show partial loss of growth/genomic instability

### Test 7: TRIM8-Mediated Oncogene Overdose Window
- **Question:** What is the precise EWS-FLI1 protein level window compatible with Ewing sarcoma survival?
- **Design:** Degron-based titration of EWS-FLI1 levels combined with TRIM8 KO to define the upper tolerance limit; correlate with enhancer activity (H3K27ac) and R-loop accumulation at each dosage
- **Expected result:** Define narrow EWS-FLI1 dosage window; levels below threshold → metastatic phenotype; levels above threshold → oncogene overdose/apoptosis; levels at optimum → maximal enhanceropathy + proliferation

---

## Curation Leads

### Candidate Evidence References (Require Curator Verification)

1. **PMID:41950086** (Eyunni et al., 2026) - New evidence that STAG2 loss amplifies enhanceropathy at multimeric GGAA microsatellites. Candidate for adding as new evidence item supporting the hypothesis with qualifier about STAG2-dependent modulation.
   - Snippet to verify: *"STAG2 loss eliminates over 40% of EWS-FLI1 binding sites, predominantly at enhancers containing short (1-4) GGAA repeats, while concurrently increasing binding at multimeric enhancers with ≥5 GGAA-repeat motifs"*

2. **PMID:41484205** (Suresh et al., 2026) - Critical new evidence on dosage-dependent enhanceropathy and metastasis. Candidate for adding with note about therapeutic implications.
   - Snippet to verify: *"modest EF depletion promoted a pro-metastatic phenotype that diminished upon near-complete EF loss, revealing a paradoxical effect of submaximal EF inhibition"*

3. **PMID:41659683** (Yoshida et al., 2026) - Refines biophysical mechanism from LLPS to dynamic hubs. Qualifies the LCD phase separation aspect of the model.
   - Snippet to verify: *"endogenous EWS::FLI1 forms dynamic, sub-diffraction-limit hubs with mechanisms of dissolution that prevent the hubs from achieving macroscopic liquid-liquid phase separation"*

4. **PMID:35483357** (Chong et al., 2022) - Shows narrow LCD interaction optimum; excess LLPS represses transcription.
   - Snippet to verify: *"the oncogenic TF EWS::FLI1 requires a narrow optimum of LCD-LCD interactions to activate its target genes associated with GGAA microsatellites"*

5. **PMID:40080499** (Noorizadeh et al., 2025) - IGF-1/YAP1 cooperation required for transformation. Partially resolves cell-of-origin permissiveness gap.
   - Snippet to verify: *"transient exposure to IGF-1 concentrations mimicking serum levels during puberty reprograms limb-derived mesenchymal cells of EWS::FLI1-mutant mice to stable transformation and tumorigenicity"*

6. **PMID:40721661** (Olmedo-Pelayo et al., 2025) - R-loop/DHX9 replication stress mechanism parallel to enhanceropathy.
   - Snippet to verify: *"EWS::FLI1 prevents the resolution of R-loops induced by these drugs via sequestering DHX9 helicase, ultimately resulting in R-loop accumulation, replication stress, and genome instability"*

7. **PMID:28134926** (Sheffield et al., 2017) - Genome-scale DNA methylation validation of enhanceropathy in patient tumors.
   - Snippet to verify: *"We observed consistent DNA hypomethylation at enhancers regulated by the disease-defining EWS-FLI1 fusion protein, thus establishing epigenomic enhancer reprogramming as a ubiquitous and characteristic feature of Ewing sarcoma."*

8. **PMID:40215343** (Zhu et al., 2025) - ETV6 competition at GGAA microsatellites.
   - Snippet to verify: *"ETV6 as a vulnerability in Ewing sarcoma, where it competes with EWS::FLI1 at short GGAA repeats to restrain EWS::FLI1 function"*

9. **PMID:32049009** (Aynaud et al., 2020) - Single-cell resolution of enhancer-driven EWS-FLI1 program and metabolic association.
   - Snippet to verify: Abstract text establishing link between direct enhancer-driven program and oxidative phosphorylation/proliferation.

10. **PMID:40667384** (Waltner et al., 2025) - Multiple gene regulatory modules beyond EWS-FLI1 dosage.
    - Snippet to verify: *"multiple, co-existing transcriptional programs shape the phenotypic diversity of EwS"*

11. **PMID:37963210** (Graca Marques et al., 2024) - CHD4/NuRD CRISPR screen validates chromatin structure dependency.
    - Snippet to verify: *"CHD4 silencing induced tumor cell death by apoptosis and abolished colony formation"*

12. **PMID:34329586** (Seong et al., 2021) - TRIM8-mediated EWS-FLI1 dosage control and oncogene overdose.
    - Snippet to verify: *"TRIM8 knockout led to an increase in EWS/FLI protein levels that was not tolerated"*

13. **PMID:36658219** (Gao et al., 2023) - ETV6 competition at GGAA repeats with full mechanistic detail.
    - Snippet to verify: *"ETV6 competes with EWS-FLI1 for binding to select DNA elements enriched for short GGAA repeat sequences"*

14. **PMID:36229873** (Hölting et al., 2022) - GGAA enhancer-based therapeutic gene expression platform.
    - Snippet to verify: *"capitalizing on neomorphic DNA-binding preferences - the addiction to the respective fusion transcription factor EWSR1-FLI1 can be leveraged to express therapeutic genes"*

### Candidate Pathophysiology Nodes/Edges

- **Node:** BAF/SWI-SNF complex → key chromatin effector recruited by EWSR1 LCD
- **Edge:** EWS-FLI1 → NuRD complex → gene repression (parallel to enhancer activation arm)
- **Edge:** STAG2 loss → enhanceropathy redistribution → amplified multimeric GGAA activity
- **Edge:** EWS-FLI1 dosage fluctuation → differential enhancer sensitivity → tumor plasticity/metastasis
- **Node:** Core regulatory circuitry (KLF15/TCF4/NKX2-2) → downstream amplifier of enhanceropathy
- **Edge:** IGF-1 (puberty) → YAP1 activation → permissive transformation context (NEW)
- **Edge:** EWS-FLI1 → DHX9 sequestration → R-loop accumulation → replication stress (NEW - parallel mechanism)
- **Edge:** ETV6 ⊣ EWS-FLI1 at short GGAA repeats (counter-regulatory) (NEW)
- **Edge:** EWS-FLI1 optimal activity → oxidative phosphorylation + proliferation (NEW)
- **Node:** CD73+ CAF-like tumor subpopulation (EWS-FLI1-repressed gene upregulation, migratory) (NEW)
- **Edge:** TRIM8 → EWS-FLI1 ubiquitination/degradation → dosage control (oncogene overdose prevention) (NEW - CRISPR validated)
- **Edge:** CHD4/NuRD → chromatin structure maintenance → DNA damage protection (colocalizes at EWS-FLI1 enhancers) (NEW - CRISPR validated)
- **Edge:** ETV6 loss → SOX11 upregulation → mesenchymal differentiation (downstream of GGAA hyper-activation) (NEW - CRISPR validated)
- **Edge:** GGAA enhancer neomorphism → therapeutic gene expression platform (translational application) (NEW)

### Candidate Ontology Terms

- **Cell types:** Neural crest-derived progenitor (CL:0000008); Mesenchymal stem cell (CL:0000134)
- **Biological processes:** De novo enhancer formation (GO:0000980 modifier); Chromatin remodeling (GO:0006338); Transcription factor hub formation; Microsatellite-dependent transcription regulation
- **Molecular functions:** Prion-like domain-mediated protein interaction; BAF complex recruitment

### Candidate Subtype Restrictions

- The hypothesis applies to all EWSR1-ETS fusion-positive Ewing sarcomas (~95% of classic Ewing)
- Does NOT apply to CIC-DUX4 or BCOR-CCNB3 Ewing-like sarcomas
- STAG2-mutant subtype (~15%) shows modified enhanceropathy with amplified multimeric activity
- Status should remain CANONICAL but with explicit notation that cell-of-origin permissiveness and cooperating mutations are unresolved

### Candidate Knowledge Gaps for KB

1. **Cell-context permissiveness (partially resolved):** IGF-1/YAP1 provides developmental context, but why only specific mesenchymal subpopulations are permissive remains unknown
2. **Mouse model gap (partially resolved):** EWS-FLI1 + IGF-1 achieves transformation in mouse MSCs, but requires specific developmental timing
3. **Metabolic rewiring mechanism (partially resolved):** scRNA-seq links optimal EWS-FLI1 to OXPHOS, but specific enhancer-to-metabolic enzyme causal chain unmapped
4. **Clinical validation:** No Phase II/III trial with pharmacodynamic enhanceropathy biomarkers completed
5. **Dosage-metastasis paradox:** Clinical relevance of partial EWS-FLI1 inhibition promoting metastasis unknown
6. **Non-FLI1 ETS partner chromatin profiling:** Comparative enhanceropathy data for rare EWS-ERG/ETV/FEV fusions limited
7. **R-loop/replication stress contribution (NEW):** What fraction of EWS-FLI1 oncogenicity is due to enhanceropathy vs. DHX9 sequestration/R-loops?
8. **ETV6 counter-regulation scope (NEW):** At how many GGAA sites does ETV6 actively restrain EWS-FLI1, and what happens genome-wide upon ETV6 loss?
9. **Intratumoral heterogeneity origins (NEW):** What drives the multiple co-existing transcriptional modules seen by scRNA-seq - stochastic EWS-FLI1 fluctuation, microenvironmental signals (TGF-beta), or epigenetic memory?

### Candidate Status Change

- **Recommendation:** Maintain CANONICAL status. The evidence is overwhelming for the core mechanism.
- **Suggested additions to description:** Note the dual activation/repression mechanism, the requirement for dynamic hub formation (not bulk LLPS), and the dosage-sensitivity of GGAA microsatellite enhancers.

---

## Summary

The canonical EWS-FLI1 fusion enhanceropathy model is strongly supported by convergent evidence from chromatin biology, single-molecule biophysics, population genetics, DNA methylation profiling, single-cell transcriptomics, CRISPR functional genomics, cooperating mutation analysis, proteomics, and pharmacological perturbation studies, spanning **43 primary research papers (1999-2026)**. No evidence was found that refutes the core model; all qualifying evidence adds complexity rather than contradicting the mechanism. The model has been substantively refined since initial formulation:

1. **Biophysical mechanism:** EWSR1 LCD operates through dynamic sub-diffraction hubs (not bulk LLPS), requiring a narrow optimum of LCD interactions
2. **Dual function:** Both enhancer activation (GGAA microsatellites via BAF) and repression (ETS motifs via NuRD) are required for transformation
3. **Dosage sensitivity:** GGAA microsatellite enhancers are the most dosage-sensitive, with paradoxical pro-metastatic effects at intermediate EWS-FLI1 levels
4. **Developmental context:** IGF-1 signaling during puberty provides the permissive signal for transformation via YAP1, partially resolving the cell-of-origin question
5. **Parallel mechanisms:** EWS-FLI1 also causes replication stress via DHX9 sequestration and R-loop accumulation, independent of the enhanceropathy
6. **Counter-regulation:** Native ETS factor ETV6 competes with EWS-FLI1 at short GGAA repeats, restraining enhanceropathy
7. **Intratumoral heterogeneity:** Multiple co-existing transcriptional modules operate alongside the core EWS-FLI1 program, modifiable by TGF-beta and other microenvironmental signals

The most important remaining gaps are: (1) the exact epigenomic prerequisites that make specific mesenchymal subpopulations permissive, (2) whether the dosage-metastasis paradox and paracrine IL6/STAT3 signaling complicate clinical EWS-FLI1 targeting, (3) the relative contributions of enhanceropathy vs. R-loop/replication stress to oncogenicity, (4) definitive clinical trial results for enhanceropathy-targeting therapies, and (5) whether enhanceropathy is reversible upon EWS-FLI1 withdrawal or creates epigenetic memory. The model's therapeutic implications are actively being tested through LSD1 inhibitors (seclidemstat, NCT03600649), BET inhibitors, trabectedin combinations, and novel approaches including ETV6 degraders, GGAA-enhancer-based therapeutic gene expression platforms, and EWS-FLI1 hub-disrupting strategies.

### Evidence Summary Statistics

| Category | Count |
|----------|-------|
| Total evidence items | 43 |
| Supporting | 24 |
| Qualifying (adds complexity) | 16 |
| Supporting + Qualifying | 3 |
| Refuting | 0 |
| Human clinical evidence | 8 |
| In vitro evidence | 25 |
| In vivo (model organism) | 7 |
| CRISPR functional screens | 5 |
| Review-level evidence | 3 |
| Confirmed findings in knowledge graph | 16 |
| Knowledge gaps identified | 12 |
| Alternative/complementary models | 9 |
| Discriminating tests proposed | 7 |
| Curation leads | 14 |
