---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-09T22:17:02.898813'
end_time: '2026-06-09T22:27:42.895992'
duration_seconds: 640.0
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: Microtubule-Dependent Neuronal Migration Failure Module
  category: Module
  hypothesis_group_id: microtubule_migration_model
  hypothesis_label: Microtubule-Dependent Neuronal Migration Model
  hypothesis_status: CANONICAL
  hypothesis_yaml: "hypothesis_group_id: microtubule_migration_model\nhypothesis_label:\
    \ Microtubule-Dependent Neuronal Migration Model\nstatus: CANONICAL\ndescription:\
    \ Microtubule-associated proteins, tubulin subunits, dynein, and kinesin motors\
    \ form a coupled\n  apparatus for neuronal polarization, nucleokinesis, migration,\
    \ and projection outgrowth. Pathogenic\n  variants disrupt this apparatus through\
    \ altered microtubule polymerization, heterodimer formation, MAP\n  binding, motor\
    \ ATPase activity, microtubule binding, or cargo/centrosome-nucleus coupling.\
    \ Developing\n  neurons then fail to migrate to appropriate cortical positions,\
    \ producing dyslamination, lissencephaly/subcortical-band-heterotopia\n  patterns,\
    \ and selected polymicrogyria-like cortical malformations.\nevidence:\n- reference:\
    \ PMID:23603762\n  supports: SUPPORT\n  evidence_source: OTHER\n  snippet: Our\
    \ data reinforce the importance of centrosomal and microtubule-related proteins\
    \ in cortical\n    development and strongly suggest that microtubule-dependent\
    \ mitotic and postmitotic processes are\n    major contributors to the pathogenesis\
    \ of MCD.\n  explanation: Broad synthesis from human genetics, biochemical assays,\
    \ yeast assays, and mouse in utero\n    experiments supporting the module-level\
    \ mechanism."
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 38
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Microtubule-Dependent Neuronal Migration Failure Module
- **Category:** Module

## Target Hypothesis
- **Hypothesis ID:** microtubule_migration_model
- **Hypothesis Label:** Microtubule-Dependent Neuronal Migration Model
- **Status in KB:** CANONICAL

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: microtubule_migration_model
hypothesis_label: Microtubule-Dependent Neuronal Migration Model
status: CANONICAL
description: Microtubule-associated proteins, tubulin subunits, dynein, and kinesin motors form a coupled
  apparatus for neuronal polarization, nucleokinesis, migration, and projection outgrowth. Pathogenic
  variants disrupt this apparatus through altered microtubule polymerization, heterodimer formation, MAP
  binding, motor ATPase activity, microtubule binding, or cargo/centrosome-nucleus coupling. Developing
  neurons then fail to migrate to appropriate cortical positions, producing dyslamination, lissencephaly/subcortical-band-heterotopia
  patterns, and selected polymicrogyria-like cortical malformations.
evidence:
- reference: PMID:23603762
  supports: SUPPORT
  evidence_source: OTHER
  snippet: Our data reinforce the importance of centrosomal and microtubule-related proteins in cortical
    development and strongly suggest that microtubule-dependent mitotic and postmitotic processes are
    major contributors to the pathogenesis of MCD.
  explanation: Broad synthesis from human genetics, biochemical assays, yeast assays, and mouse in utero
    experiments supporting the module-level mechanism.
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

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Microtubule-Dependent Neuronal Migration Failure Module
- **Category:** Module

## Target Hypothesis
- **Hypothesis ID:** microtubule_migration_model
- **Hypothesis Label:** Microtubule-Dependent Neuronal Migration Model
- **Status in KB:** CANONICAL

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: microtubule_migration_model
hypothesis_label: Microtubule-Dependent Neuronal Migration Model
status: CANONICAL
description: Microtubule-associated proteins, tubulin subunits, dynein, and kinesin motors form a coupled
  apparatus for neuronal polarization, nucleokinesis, migration, and projection outgrowth. Pathogenic
  variants disrupt this apparatus through altered microtubule polymerization, heterodimer formation, MAP
  binding, motor ATPase activity, microtubule binding, or cargo/centrosome-nucleus coupling. Developing
  neurons then fail to migrate to appropriate cortical positions, producing dyslamination, lissencephaly/subcortical-band-heterotopia
  patterns, and selected polymicrogyria-like cortical malformations.
evidence:
- reference: PMID:23603762
  supports: SUPPORT
  evidence_source: OTHER
  snippet: Our data reinforce the importance of centrosomal and microtubule-related proteins in cortical
    development and strongly suggest that microtubule-dependent mitotic and postmitotic processes are
    major contributors to the pathogenesis of MCD.
  explanation: Broad synthesis from human genetics, biochemical assays, yeast assays, and mouse in utero
    experiments supporting the module-level mechanism.
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


## Microtubule-Dependent Neuronal Migration Failure Module — Hypothesis Search Report (as of 2026-06-10)

### Executive judgment
**Verdict: Supported (with important scope qualifiers).** Recent human-genetic discoveries with direct functional validation strengthen the module-level claim that microtubule-associated proteins (MAPs), tubulin subunits, and microtubule motors/regulators form an integrated apparatus required for nucleokinesis, radial migration, and cortical lamination, and that disruption produces lissencephaly/pachygyria, subcortical band heterotopia (SBH), and heterotopia patterns. The strongest direct 2023–2024 support comes from (i) a newly identified lissencephaly-associated *NDEL1* mosaic variant that disrupts LIS1 binding and nucleus–centrosome coupling (nucleokinesis) with in vivo migration assays, and (ii) *Eml1* forebrain conditional knockout with early centrosome/cilia/microtubule defects and partial pharmacologic rescue by microtubule stabilization that reduces heterotopia metrics. Key caveats are that (a) some “microtubule genes” act primarily through progenitor/centrosome/cilia and cell-cycle pathways rather than purely post-mitotic neuronal migration, and (b) competing mechanisms (actin/membrane dynamics; Golgi/vesicle trafficking/adhesion) can generate convergent migration/lamination phenotypes and may be more parsimonious for subsets of patients. (tsai2024novellissencephalyassociatedndel1 pages 1-2, tsai2024novellissencephalyassociatedndel1 pages 4-5, zaidi2024forebraineml1depletion pages 6-8, zaidi2024forebraineml1depletion pages 8-11, zaidi2024forebraineml1depletion pages 1-2, goo2023schizophreniaassociatedmitoticarrest pages 1-2)

---

### Key concepts and definitions (current understanding)
**Neuronal radial migration** can be decomposed into (at least) leading process extension and **cell-body translocation**; the latter is driven by **nucleokinesis**, i.e., forward movement of the nucleus into the leading process. Microtubules (MTs) and MT motors generate forces for nucleokinesis, while MTs also organize trafficking and guidance-cue responses during leading process behavior. (sebastien2023doublecortinrestrictsneuronal pages 1-3)

**Centrosome–nucleus coupling** refers to coordinated movements and physical linkage between the centrosome (MT organizing center) and the nucleus during migration; failure of this coupling is a proximate cellular signature of migration breakdown and is explicitly implicated for *NDEL1* variant-associated pachygyria/SBH. (tsai2024novellissencephalyassociatedndel1 pages 1-2)

**“Two-stroke” migration cycle**: leading process extension and centrosome advance are followed by nuclear translocation (nucleokinesis), implying a coupled centrosome/MT/motor apparatus. (tsai2024novellissencephalyassociatedndel1 pages 1-2)

**Interkinetic nuclear migration (INM/IKNM)** describes cell-cycle–linked apical–basal oscillation of progenitor nuclei in radial glia; dynein- and kinesin-dependent MT-based transport contributes directionality (dynein supporting apicalward; kinesin supporting basalward movement as described in recent synthesis). (viola2024radialgliaprogenitor pages 2-5)

**Tubulin code / post-translational modification (PTM) subpopulations**: MT behavior is not only polymerization dynamics but also lattice state and PTMs (e.g., polyglutamylation) that tune MAP and motor interactions; this provides a mechanistic “qualifier” for classic tubulinopathy models. (sebastien2023doublecortinrestrictsneuronal pages 1-3)

---

### Evidence matrix (support/refute/qualify/competing)
| Citation (year) | URL/DOI | Evidence type | Supports / refutes / qualifies / competing | Mechanistic claim tested | Key finding (include quantitative stats when available) | Disease subtype/context | Confidence & limitations |
|---|---|---|---|---|---|---|---|
| Tsai et al. (2024) | https://doi.org/10.1007/s00401-023-02665-y | Human clinical genetics + in utero electroporation + molecular assays | Supports | NDEL1-LIS1-dynein coupling is required for nucleus-centrosome coupling and nucleokinesis during neuronal migration | De novo somatic mosaic NDEL1 p.Arg105Pro identified in 2 patients with pachygyria ± SBH; mosaicism ~25-30% in case 1 and ~15-20% in case 2; variant disrupted LIS1 binding, impaired neuronal migration, increased leading-process length, and impaired nucleus-centrosome coupling; could not rescue Ndel1 knockdown (tsai2024novellissencephalyassociatedndel1 pages 1-2, tsai2024novellissencephalyassociatedndel1 pages 4-5) | Pachygyria with/without subcortical band heterotopia | High: direct human genotype-to-function link in a top-tier journal; limited by only 2 mosaic cases and unresolved broader prevalence/penetrance |
| Zaidi et al. (2024) | https://doi.org/10.1083/jcb.202310157 | Mouse conditional knockout + patient cells + rescue pharmacology | Supports | EML1-dependent microtubule/centrosome/cilium integrity in radial glia is causally upstream of heterotopia formation | Forebrain Eml1 cKO caused SH with 100% penetrance; patient cells showed MT aggregates in 83.33%; EpoD restored centrosomal structure in 86% of patient cells, reduced MT aggregates to 37.93%, and reduced ectopic Pax6+ cells outside VZ from 60% to 32% in cKO embryos; heterotopia volume partially reduced (zaidi2024forebraineml1depletion pages 6-8, zaidi2024forebraineml1depletion pages 8-11, zaidi2024forebraineml1depletion pages 1-2, zaidi2024forebraineml1depletion pages 11-13) | Subcortical heterotopia; early radial glia delamination | High: strong causal rescue data; qualifies seed model because defect prominently involves progenitors/radial glia, centrosome and cilia biology, not only postmitotic neuronal migration |
| Sébastien et al. (2023) | https://doi.org/10.1101/2023.06.02.543327 | Human iPSC-derived cortical neurons + CRISPR KO | Qualifies | DCX-dependent migration defects may arise through tubulin post-translational modification and organelle transport, not necessarily altered bulk MT polymerization dynamics | DCX-KO neurons had reduced nuclear movement velocities and increased early neurite branching, but EB-comet MT growth dynamics were unchanged; instead, tubulin polyglutamylation and lysosome processivity were reduced, and branching was rescued by DCX or TTLL11 (sebastien2023doublecortinrestrictsneuronal pages 1-3) | Lissencephaly / SBH-relevant DCX biology in cortical neurons | Moderate: mechanistically rich human-cell model; preprint status and no direct in vivo cortical lamination endpoint in excerpt |
| Goo et al. (2023) | https://doi.org/10.1038/s41380-022-01856-5 | Primary mechanistic study in mouse/human systems | Competing | Golgi-centered vesicle trafficking and polarity control can drive migration defects independently of classic MT polymerization failure | MAD1 localized to Golgi, interacted with KIFC3, impaired Golgi morphology/positioning and VSVG trafficking when deficient, and caused migration plus multipolar-to-bipolar transition defects; supports Golgi/adhesion/polarity as an alternative mechanistic route (goo2023schizophreniaassociatedmitoticarrest pages 1-2, goo2023schizophreniaassociatedmitoticarrest pages 4-5) | Developing neocortical neuronal migration | High for alternative mechanism; not an MCD patient genetics paper, so disease-module relevance is indirect |
| Tsai et al. (2024) | https://doi.org/10.1242/dev.201912 | Human case genetics + in utero electroporation | Competing | Actin/membrane-dynamics defects can produce lissencephaly-like migration failure independently of the seed microtubule module | De novo BAIAP2 p.Arg29Trp in lissencephaly; Baiap2 knockdown caused fewer neurons reaching CP, more delayed in IZ, increased multipolar cells, and ~30% neurons arrested in white matter by P7, without major progenitor effects (tsai2024lissencephalyassociatedbaiap2variant pages 1-2, tsai2024lissencephalyassociatedbaiap2variant pages 2-5) | Posterior-predominant lissencephaly | Moderate-high: direct migration phenotype and human variant; mechanism points to actin/membrane remodeling rather than canonical tubulin/motor dysfunction |
| Leca et al. (2023) | https://doi.org/10.1038/s41598-023-27782-2 | Mouse genetic model | Qualifies | TUBA1A-related cortical malformations can result from dosage/transcript instability and progenitor depletion, not only altered tubulin protein function in migrating neurons | Codon-modified Tuba1a reduced mRNA levels (qPCR, P<0.0001), increased apoptosis, reduced VZ thickness, and decreased CTIP2+ neurons and PAX6+ progenitors; homozygotes were perinatal lethal (leca2023codonmodificationof pages 5-6) | Tubulinopathy / severe neurodevelopmental phenotype | Moderate-high: strong in vivo data; tests dosage effect rather than patient missense mechanism, so it broadens rather than directly proves the seed hypothesis |
| Ruiz-Reig et al. (2024) summarizing primary KIF2A data | https://doi.org/10.4103/1673-5374.375298 | Review-level synthesis of human genetics + model data | Supports | KIF2A-dependent MT depolymerization is required for radial migration and cortical lamination | Summarizes human KIF2A variants causing lissencephaly/MCD; functional data include ~90% monopolar spindles in U2OS after KIF2A loss, altered progenitor-neuron balance, increased multipolar cells in upper IZ, delayed radial migration, and reduced interneuron migration velocity in mouse models (ruizreig2024connectingneurodevelopmentto pages 1-2, ruizreig2024connectingneurodevelopmentto pages 4-5) | Lissencephaly, pachygyria, heterotopia, microcephaly | Moderate: strong orientation and quantitative details, but largely review-level rather than newly generated 2024 primary evidence |
| Ren et al. (2024) | https://doi.org/10.3389/fped.2024.1367305 | Human case report + literature synthesis | Supports | TUBA1A variants affecting motor/MAP interaction surfaces are strongly associated with migration-related cortical malformations | Reports ~70% of TUBA1A cases have lissencephaly; 77 missense variants known; R402 substitutions account for ~30% of identified TUBA1A mutations; epilepsy in ~28% (44/155), seizures controlled in ~33%; R402 mutants support kinesin but impair dynein, consistent with dominant-negative disruption of migration (ren2024lissencephalycausedby pages 2-4, ren2024lissencephalycausedby pages 4-6, ren2024lissencephalycausedby pages 1-2) | TUBA1A-related lissencephaly spectrum | Moderate: useful clinical statistics and mechanistic framing, but much evidence is literature review rather than new functional testing |
| Procopio et al. (2024) | https://doi.org/10.3390/ijms25105505 | Human clinical genetics case series | Supports / qualifies | DCX-related microtubule dysfunction explains SBH, but severity is modified by mutation class, X-inactivation, and mosaicism | Three female SBH cases with DCX variants; missense variant segregated over 4 generations with mild/variable epilepsy, whereas nonsense variants caused severe drug-resistant epilepsy and ID; age at seizure onset ranged 3-10 years; IQs reported 55-64; MRI showed SBH with pachygyria; skewed X-inactivation and low-level mosaicism proposed as modifiers (procopio2024phenotypicvariabilityin pages 2-4, procopio2024phenotypicvariabilityin pages 1-2) | Subcortical band heterotopia / DCX spectrum | Moderate: strong human phenotypic nuance; limited functional validation in this paper |
| Poirier et al. (2013), cited in recent sources | PMID:23603762 | Human clinical genetics + functional follow-up (legacy anchor) | Supports | Tubulin, dynein, and kinesin gene mutations define a coherent MCD module centered on MT-dependent mitotic/postmitotic processes | Landmark study linked TUBG1, DYNC1H1, KIF5C, and KIF2A to malformations of cortical development and microcephaly; repeatedly cited by 2024 papers as foundational evidence that MT motors/tubulin defects converge on cortical malformation pathogenesis (sakamoto2024lossofdnah5 pages 18-20, tsai2024novellissencephalyassociatedndel1 pages 16-17, ruizreig2024connectingneurodevelopmentto pages 4-5) | Broad MCD module: lissencephaly/pachygyria/microcephaly | High as canonical foundation; older than requested priority window and details in current evidence are second-hand through recent citations |


*Table: This table summarizes the strongest currently available evidence for and against the Microtubule-Dependent Neuronal Migration Model, prioritizing 2023-2024 primary studies while retaining one landmark legacy anchor. It highlights where the model is directly supported, where it is broadened by qualifying mechanisms, and which competing pathways may explain overlapping cortical malformation phenotypes.*

---

### 1) Strongest direct evidence for the hypothesis
#### A. Human mosaic *NDEL1* variant + functional validation of nucleokinesis failure (2024)
A 2024 *Acta Neuropathologica* study identified the first lissencephaly-spectrum association for *NDEL1* (de novo **somatic mosaic** p.Arg105Pro) in **two unrelated patients with pachygyria ± SBH**, with mosaicism fractions reported at **~25–30%** (case 1) and **~15–20%** (case 2). (Publication date: 2024-01; URL: https://doi.org/10.1007/s00401-023-02665-y) (tsai2024novellissencephalyassociatedndel1 pages 4-5)

Mechanistically, the variant is located in a domain needed for self-association and **LIS1 binding**, and is reported to **disrupt NDEL1–LIS1 interaction**, producing **impaired nucleus–centrosome coupling** and neuronal migration defects in functional assays, consistent with a dynein-regulatory nucleokinesis failure mechanism. (tsai2024novellissencephalyassociatedndel1 pages 1-2)

Why this is “direct” support: it links a patient variant → a defined microtubule-motor regulatory interaction (NDEL1–LIS1–dynein axis) → a specific migration sub-step (nucleokinesis/coupling) → a canonical imaging phenotype (pachygyria/SBH). (tsai2024novellissencephalyassociatedndel1 pages 1-2, tsai2024novellissencephalyassociatedndel1 pages 4-5)

#### B. Microtubule/centrosome defects causally upstream of heterotopia, with partial rescue by MT stabilization (2024)
A 2024 *Journal of Cell Biology* study used a **forebrain-specific *Eml1* conditional knockout** and **human patient cells** to connect early centrosome/primary cilium and microtubule defects to **subcortical heterotopia (SH)**, reporting **100% penetrance** of SH in the mouse model. (Publication date: 2024-09; URL: https://doi.org/10.1083/jcb.202310157) (zaidi2024forebraineml1depletion pages 1-2)

The study reports pronounced centrosome/MT ultrastructural abnormalities in patient cells (e.g., MT aggregates in **83.33%** of cells). Critically, pharmacologic MT stabilization/polymerization support using **Epothilone D (EpoD)** restored centrosomal structure in **86%** of patient cells and reduced MT aggregates to **37.93%**, and in vivo reduced ectopic Pax6+ progenitors outside the VZ from **60% (saline) to 32% (EpoD)**; heterotopia volume metrics were partially reduced. (zaidi2024forebraineml1depletion pages 6-8, zaidi2024forebraineml1depletion pages 8-11, zaidi2024forebraineml1depletion pages 11-13)

Why this is “direct” support: it provides an **interventional rescue** at the MT level (a causal test) that partially rescues cell-positioning defects and heterotopia burden, consistent with MT dysfunction being a driver rather than a bystander. (zaidi2024forebraineml1depletion pages 8-11, zaidi2024forebraineml1depletion pages 11-13)

---

### 2) Evidence that argues against the hypothesis or limits its scope
**Not all migration defects are best explained by bulk MT polymerization dynamics.** In a 2023 human iPSC-derived cortical neuron model, **DCX knockout reduced nuclear movement velocities** (consistent with impaired nucleokinesis/migration), but **EB comet dynamics were unchanged**, shifting attention to MT lattice/PTM states rather than classic polymerization rate changes. The study reports reduced **α-tubulin polyglutamylation** and reduced lysosome processivity, proposing a “tubulin code”/transport-centered proximate mechanism. (Publication date: 2023-06-02 preprint; URL: https://doi.org/10.1101/2023.06.02.543327) (sebastien2023doublecortinrestrictsneuronal pages 1-3)

**Some ‘microtubule module’ genes may act upstream in progenitors/radial glia via centrosome/cilia/cell-cycle, not only post-mitotic neuronal migration.** *Eml1* loss shows primary cilia and centrosome defects plus altered cell-cycle kinetics in radial glia, implying that heterotopia can emerge through progenitor delamination/ectopic progenitor distribution as a primary driver, with migration failure as downstream or parallel. (zaidi2024forebraineml1depletion pages 1-2, zaidi2024forebraineml1depletion pages 21-26)

**Genotype-to-phenotype heterogeneity implies strong modifiers and partial penetrance of specific mechanistic sub-edges.** In DCX-related SBH, mutation class (missense vs nonsense), skewed X-inactivation, and mosaicism are highlighted as major sources of intrafamilial heterogeneity (e.g., seizure-free relatives vs drug-resistant epilepsy). This qualifies any one-to-one mapping from “microtubule binding defect” to clinical severity. (Publication date: 2024-05; URL: https://doi.org/10.3390/ijms25105505) (procopio2024phenotypicvariabilityin pages 2-4, procopio2024phenotypicvariabilityin pages 1-2)

---

### 3) Claim status: established vs emerging vs speculative vs contradicted
**Established (high confidence at module level):**
- Disruption of the MT/motor/centrosome apparatus is repeatedly associated with malformations of cortical development (MCD), including lissencephaly/pachygyria and heterotopia patterns; this remains the canonical framing in the module and is reinforced by 2024 patient+functional data (notably *NDEL1*, *EML1*). (tsai2024novellissencephalyassociatedndel1 pages 1-2, zaidi2024forebraineml1depletion pages 8-11)

**Emerging (supported but still limited in cohort size/generalization):**
- *NDEL1* as a human lissencephaly-spectrum gene with a defined dynein-regulator interaction defect (LIS1 binding disruption) and nucleokinesis/coupling phenotype (currently only two mosaic cases in the extracted evidence). (tsai2024novellissencephalyassociatedndel1 pages 4-5, tsai2024novellissencephalyassociatedndel1 pages 1-2)
- MT-stabilizer pharmacologic rescue as a proof-of-mechanism for at least a subset of MT/centrosome/cilia-driven heterotopia mechanisms (*Eml1*). (zaidi2024forebraineml1depletion pages 8-11, zaidi2024forebraineml1depletion pages 11-13)

**Speculative / model-dependent (requires broader confirmation):**
- That specific MT PTM changes (e.g., polyglutamylation) are the dominant causal bridge from DCX loss to human SBH, versus being one of several downstream changes; current support is strong mechanistically but is preprint-level and mostly in vitro. (sebastien2023doublecortinrestrictsneuronal pages 1-3)

**Contradicted / not supported in current extracted set:**
- No strong “refutation” items were found that disprove MT/motor coupling as a causal route to these malformations; rather, the main counterweight is **etiologic heterogeneity** with competing mechanisms producing similar phenotypes. (tsai2024lissencephalyassociatedbaiap2variant pages 1-2, goo2023schizophreniaassociatedmitoticarrest pages 1-2)

---

### 4) Subtypes, stages, tissues, cell types, and pathways best explained by the hypothesis
**Phenotypes best explained:**
- **Pachygyria / lissencephaly ± SBH** via nucleokinesis failure in post-mitotic migrating neurons (e.g., *NDEL1* mosaic variant disrupting LIS1 binding and nucleus–centrosome coupling). (tsai2024novellissencephalyassociatedndel1 pages 1-2, tsai2024novellissencephalyassociatedndel1 pages 4-5)
- **Subcortical heterotopia** via early centrosomal/MT/ciliary defects causing radial glia detachment and ectopic progenitor/neuron positioning (*Eml1*). (zaidi2024forebraineml1depletion pages 1-2, zaidi2024forebraineml1depletion pages 8-11)

**Cell types / developmental windows:**
- Post-mitotic migrating cortical neurons (nucleokinesis, leading process regulation): highlighted by *NDEL1* and DCX iPSC neuron work. (tsai2024novellissencephalyassociatedndel1 pages 1-2, sebastien2023doublecortinrestrictsneuronal pages 1-3)
- Radial glia progenitors (INM, apical attachment, centrosome/primary cilium signaling): highlighted by *Eml1* conditional KO and radial glia polarity synthesis. (viola2024radialgliaprogenitor pages 2-5, zaidi2024forebraineml1depletion pages 1-2)

**Pathway modules (microtubule-centered):**
- Dynein regulation via LIS1 and adaptors (NDE1/NDEL1) controlling nucleus–centrosome coupling. (tsai2024novellissencephalyassociatedndel1 pages 1-2)
- Microtubule structural/biochemical regulation including MT stability and PTMs (polyglutamylation). (sebastien2023doublecortinrestrictsneuronal pages 1-3, zaidi2024forebraineml1depletion pages 6-8)

**Clinical statistics consistent with the hypothesis (2024 syntheses):**
- In TUBA1A tubulinopathies, ~**70%** of reported cases exhibit lissencephaly; substitutions at **R402** account for ~**30%** of identified TUBA1A mutations; epilepsy occurs in ~**28% (44/155)** with seizures reportedly controlled in ~**33%** of affected patients. (Publication date: 2024-05; URL: https://doi.org/10.3389/fped.2024.1367305) (ren2024lissencephalycausedby pages 2-4, ren2024lissencephalycausedby pages 4-6)

---

### 5) Alternative / competing mechanistic hypotheses
These are not necessarily “refutations”; they often represent parallel or upstream mechanisms that converge on the same migration/lamination endpoints.

1) **Actin/membrane-dynamics migration failure model (competing/parallel)**
A 2024 *Development* paper reports a de novo **BAIAP2** variant (p.Arg29Trp) in lissencephaly and shows that Baiap2 knockdown in vivo disrupts neuronal migration, including increased multipolar morphology and ~**30%** of neurons arrested in white matter by P7, without major progenitor proportion changes, implicating actin-linked membrane dynamics and morphogenesis rather than primary MT polymerization defects. (Publication date: 2024-12; URL: https://doi.org/10.1242/dev.201912) (tsai2024lissencephalyassociatedbaiap2variant pages 2-5, tsai2024lissencephalyassociatedbaiap2variant pages 1-2)

2) **Golgi/vesicle trafficking + adhesion/polarity model (competing/upstream)**
A 2023 *Molecular Psychiatry* study implicates MAD1 (MAD1L1 locus) in neuronal migration and polarity via **Golgi localization and vesicular trafficking** from Golgi to plasma membrane, including effects on VSVG transport and secretion/trafficking relevant to adhesion (e.g., integrin), providing a route to migration failure independent of a primary MT polymerization lesion. (Publication date: 2023-11; URL: https://doi.org/10.1038/s41380-022-01856-5) (goo2023schizophreniaassociatedmitoticarrest pages 1-2, goo2023schizophreniaassociatedmitoticarrest pages 4-5)

3) **Centrosome/cilia signaling and progenitor delamination model (complementary/upstream)**
In *Eml1* deficiency, primary cilia and centrosomes are altered and MT dynamics/cell-cycle kinetics are abnormal in radial glia, supporting a model where progenitor positioning defects are primary drivers of heterotopia and secondary migration errors follow. (zaidi2024forebraineml1depletion pages 1-2, zaidi2024forebraineml1depletion pages 21-26)

---

### 6) Explicit knowledge gaps (curation-relevant)
1) **Edge uncertainty: “microtubule defect → migration failure” vs “microtubule defect → progenitor delamination/cell-cycle changes → malformation.”**
- Why it matters: KB modules may need subtype-specific causal chains (post-mitotic migration vs progenitor anchoring/INM).
- What was checked: *Eml1* evidence shows early centrosome/cilia and cell-cycle changes with heterotopia rescue by MT stabilization. (zaidi2024forebraineml1depletion pages 1-2, zaidi2024forebraineml1depletion pages 8-11)
- What would resolve: lineage-restricted rescues/perturbations (radial glia–specific vs post-mitotic neuron–specific) with matched quantitative readouts (heterotopia volume, lamination indices, live nucleokinesis metrics). (zaidi2024forebraineml1depletion pages 8-11)

2) **Generalizability and prevalence for newly implicated genes/edges (e.g., *NDEL1*).**
- Why it matters: Two mosaic cases support causality but do not define prevalence, penetrance, or allelic series.
- What was checked: mosaic levels, predicted deleteriousness, LIS1 binding disruption and migration/coupling phenotypes. (tsai2024novellissencephalyassociatedndel1 pages 4-5, tsai2024novellissencephalyassociatedndel1 pages 1-2)
- What would resolve: larger sequencing cohorts with deep-coverage mosaic detection in blood/saliva/brain (where available), plus standardized phenotyping and functional validation of additional alleles.

3) **Quantitative mapping from molecular lesion to nucleokinesis/migration parameters across models.**
- Why it matters: the hypothesis specifies multiple mechanistic lesion types (polymerization, binding, ATPase, coupling), but cross-study comparability is limited.
- What was checked: DCX KO shows reduced nuclear movement velocities without changes in EB comet dynamics; *Eml1* provides quantitative rescue fractions and ectopic progenitor proportions. (sebastien2023doublecortinrestrictsneuronal pages 1-3, zaidi2024forebraineml1depletion pages 8-11)
- What would resolve: standardized live imaging pipelines (nuclear translocation velocity, centrosome–nucleus distance distributions, pause frequency, leading process length) applied across isogenic iPSC neurons/organoids and in utero electroporation models.

4) **Modifier mechanisms (X-inactivation/mosaicism) that shift severity independent of the MT lesion magnitude.**
- Why it matters: phenotype severity in DCX SBH is strongly modified and may confound simple mechanism-to-severity inferences.
- What was checked: DCX SBH case series highlighting skewed X-inactivation and low-level mosaicism as modifiers. (procopio2024phenotypicvariabilityin pages 2-4, procopio2024phenotypicvariabilityin pages 1-2)
- What would resolve: paired genetic + epigenetic profiling (X-inactivation assays) and single-cell genotyping in patient-derived lines to connect cellular genotype fractions to migration phenotypes.

5) **Source/data absences (in the current tool-derived corpus):**
- No clinical trials are present that directly target MT dynamics in these malformations (as expected for developmental structural disorders); evidence for MT-stabilizer rescue is preclinical. (zaidi2024forebraineml1depletion pages 8-11)
- Many key statements for older foundational genetics (e.g., Poirier 2013) are cited second-hand in recent texts here; primary-text extraction from those legacy papers was not retrieved in this run. (sakamoto2024lossofdnah5 pages 18-20)

---

### 7) Discriminating tests (to separate this hypothesis from alternatives)
1) **Head-to-head pharmacologic rescue triage in isogenic systems (MT vs actin vs trafficking):**
- System: isogenic iPSC-derived cortical neurons and/or forebrain organoids carrying patient variants (*NDEL1* p.R105P mosaic modeling; DCX loss; TUBA1A R402). (sebastien2023doublecortinrestrictsneuronal pages 1-3, tsai2024novellissencephalyassociatedndel1 pages 4-5)
- Perturbations: MT stabilization (e.g., EpoD-class), actin modulators (Rho/Arp2/3 axis), Golgi/secretory trafficking perturbation/rescue.
- Readouts: live nucleokinesis metrics, centrosome–nucleus coupling distance, lamination in organoids.
- Expected discriminator: MT-focused lesions should preferentially rescue with MT-targeted interventions; actin/BAIAP2-like lesions should rescue with actin/membrane-pathway correction.

2) **Cell-type-resolved causal tests in vivo:**
- Approach: conditional alleles or CRISPR perturbations restricted to radial glia vs post-mitotic neurons (Cre drivers), to deconvolve progenitor delamination/INM from neuronal migration contributions.
- Expected discriminator: if heterotopia is driven primarily by progenitor defects, radial glia-specific rescue should normalize ectopic Pax6+ distributions and heterotopia burden (as MT stabilization partially does in *Eml1*). (zaidi2024forebraineml1depletion pages 8-11, zaidi2024forebraineml1depletion pages 1-2)

3) **Quantitative “coupling failure” biomarker development:**
- Candidate cellular biomarkers: centrosome–nucleus coupling distance distributions; nuclear translocation velocity; MT PTM levels (polyglutamylation) in relevant neuronal stages.
- Rationale: DCX KO suggests PTM-level biomarkers may better reflect mechanism than EB comet MT dynamics. (sebastien2023doublecortinrestrictsneuronal pages 1-3)

4) **Mosaicism-aware patient stratification:**
- In sequencing cohorts, add deep coverage and multiple tissues to detect somatic mosaicism (motivated by *NDEL1* mosaic cases and mosaic/chimeric inheritance in TUBA1A literature synthesis). (tsai2024novellissencephalyassociatedndel1 pages 4-5, ren2024lissencephalycausedby pages 4-6)

---

### Current applications and real-world implementations
1) **Clinical genetic testing and stratification**
- Targeted or panel-based NGS is used in practice for cortical malformations; a DCX SBH case series used a targeted NGS panel (39 genes), illustrating real-world implementation of gene-first diagnosis. (procopio2024phenotypicvariabilityin pages 2-4)
- Clinical interpretation increasingly requires mosaicism-aware analyses (as in *NDEL1* mosaic cases and reported mosaic/chimeric inheritance in TUBA1A syntheses). (tsai2024novellissencephalyassociatedndel1 pages 4-5, ren2024lissencephalycausedby pages 4-6)

2) **Mechanism-driven preclinical “rescue” as translational proof-of-mechanism**
- The *Eml1* study’s partial rescue of centrosome/MT defects and reduction of ectopic progenitor fractions and heterotopia burden with MT stabilization provides a concrete example of mechanism-driven intervention testing, even if not directly clinically deployable in pregnancy. (zaidi2024forebraineml1depletion pages 8-11, zaidi2024forebraineml1depletion pages 11-13)

3) **Patient-derived cellular models for variant interpretation**
- DCX CRISPR KO in iPSC-derived cortical neurons demonstrates an implementable workflow for connecting variants/genes to nucleokinesis metrics and MT PTM changes. (sebastien2023doublecortinrestrictsneuronal pages 1-3)

---

### Expert synthesis and analysis (authoritative sources)
A 2024 radial glia polarity synthesis emphasizes that MT motors and centrosomal/ciliary architecture are central to progenitor nuclear dynamics (INM) and that radial glial polarity provides the scaffold for neuronal migration, supporting a systems view where centrosome/MT/motor defects can affect both progenitor organization and neuronal migration. (Publication date: 2024-10; URL: https://doi.org/10.3389/fcell.2024.1478283) (viola2024radialgliaprogenitor pages 2-5)

---

### Curation leads (candidate KB updates; curator verification required)
**Lead 1 — Add *NDEL1* as a high-priority evidence node for dynein-regulated nucleokinesis in lissencephaly spectrum.**
- Candidate evidence reference: Tsai et al., *Acta Neuropathologica* (2024-01), https://doi.org/10.1007/s00401-023-02665-y. (tsai2024novellissencephalyassociatedndel1 pages 1-2)
- Snippet to verify in primary text: de novo somatic mosaic p.R105P with impaired neuronal migration and impaired nucleus–centrosome coupling; disrupted binding to LIS1. (tsai2024novellissencephalyassociatedndel1 pages 1-2, tsai2024novellissencephalyassociatedndel1 pages 4-5)
- Candidate edges: *NDEL1* —(binds/regulates)→ LIS1/PAFAH1B1 —(activates/regulates)→ cytoplasmic dynein —(drives)→ centrosome–nucleus coupling/nucleokinesis —(enables)→ radial neuronal migration —(prevents)→ pachygyria/SBH.
- Candidate ontology terms: nucleokinesis; centrosome–nucleus coupling; dynein complex; cortical neuron radial migration.

**Lead 2 — Add an explicit “radial glia/progenitor delamination and cilia/centrosome” qualifier branch within the module.**
- Candidate evidence: Zaidi et al., *J Cell Biol* (2024-09), https://doi.org/10.1083/jcb.202310157. (zaidi2024forebraineml1depletion pages 1-2)
- Snippet to verify: “microtubule dynamics and cell cycle kinetics are abnormal in mouse mutant radial glia” and EpoD reduces ectopic Pax6+ outside VZ from 60% to 32%. (zaidi2024forebraineml1depletion pages 1-2, zaidi2024forebraineml1depletion pages 8-11)
- Candidate edges: EML1 → centrosome/primary cilium integrity → MT nucleation/dynamics → radial glia apical attachment / progenitor positioning → subcortical heterotopia.

**Lead 3 — Add a “tubulin PTM / tubulin code” mechanistic qualifier for DCX-related migration phenotypes.**
- Candidate evidence: Sébastien et al., bioRxiv (2023-06-02), https://doi.org/10.1101/2023.06.02.543327. (sebastien2023doublecortinrestrictsneuronal pages 1-3)
- Snippet to verify: DCX-KO reduces nuclear movement velocities without EB comet dynamics changes; reduced α-tubulin polyglutamylation; rescue with DCX or TTLL11.

**Lead 4 — Add competing-mechanism flags for convergent phenotypes.**
- Actin/membrane dynamics competing evidence: Tsai et al., *Development* (2024-12), https://doi.org/10.1242/dev.201912. (tsai2024lissencephalyassociatedbaiap2variant pages 1-2)
- Golgi/vesicle trafficking competing evidence: Goo et al., *Molecular Psychiatry* (2023-11), https://doi.org/10.1038/s41380-022-01856-5. (goo2023schizophreniaassociatedmitoticarrest pages 1-2)

---

### Conclusion
Across 2023–2024 evidence, the seed hypothesis remains well supported at the **module** level, but curation should explicitly represent **multiple proximal mechanistic routes** within “microtubule-dependent migration failure,” including (i) dynein-regulated nucleus–centrosome coupling/nucleokinesis (strengthened by *NDEL1* mosaic variant data), (ii) centrosome/cilia/MT nucleation defects in radial glia causing delamination and heterotopia (with MT-stabilizer partial rescue), and (iii) tubulin-code/PTM-mediated modulation of motors/transport that can impair nucleokinesis without changing simple MT growth dynamics. Competing actin/membrane and Golgi/trafficking mechanisms should be captured as alternatives that produce overlapping cortical malformation phenotypes and may define distinct patient subsets. (tsai2024novellissencephalyassociatedndel1 pages 1-2, zaidi2024forebraineml1depletion pages 8-11, sebastien2023doublecortinrestrictsneuronal pages 1-3, tsai2024lissencephalyassociatedbaiap2variant pages 1-2, goo2023schizophreniaassociatedmitoticarrest pages 1-2)

References

1. (tsai2024novellissencephalyassociatedndel1 pages 1-2): Meng-Han Tsai, Hao-Chen Ke, Wan-Cian Lin, Fang-Shin Nian, Chia-Wei Huang, Haw-Yuan Cheng, Chi-Sin Hsu, Tiziana Granata, Chien-Hui Chang, Barbara Castellotti, Shin-Yi Lin, Fabio M. Doniselli, Cheng-Ju Lu, Silvana Franceschetti, Francesca Ragona, Pei-Shan Hou, Laura Canafoglia, Chien-Yi Tung, Mei-Hsuan Lee, Won-Jing Wang, and Jin-Wu Tsai. Novel lissencephaly-associated ndel1 variant reveals distinct roles of nde1 and ndel1 in nucleokinesis and human cortical malformations. Acta Neuropathologica, Jan 2024. URL: https://doi.org/10.1007/s00401-023-02665-y, doi:10.1007/s00401-023-02665-y. This article has 11 citations and is from a highest quality peer-reviewed journal.

2. (tsai2024novellissencephalyassociatedndel1 pages 4-5): Meng-Han Tsai, Hao-Chen Ke, Wan-Cian Lin, Fang-Shin Nian, Chia-Wei Huang, Haw-Yuan Cheng, Chi-Sin Hsu, Tiziana Granata, Chien-Hui Chang, Barbara Castellotti, Shin-Yi Lin, Fabio M. Doniselli, Cheng-Ju Lu, Silvana Franceschetti, Francesca Ragona, Pei-Shan Hou, Laura Canafoglia, Chien-Yi Tung, Mei-Hsuan Lee, Won-Jing Wang, and Jin-Wu Tsai. Novel lissencephaly-associated ndel1 variant reveals distinct roles of nde1 and ndel1 in nucleokinesis and human cortical malformations. Acta Neuropathologica, Jan 2024. URL: https://doi.org/10.1007/s00401-023-02665-y, doi:10.1007/s00401-023-02665-y. This article has 11 citations and is from a highest quality peer-reviewed journal.

3. (zaidi2024forebraineml1depletion pages 6-8): Donia Zaidi, Kaviya Chinnappa, Berfu Nur Yigit, Valeria Viola, Carmen Cifuentes-Diaz, Ammar Jabali, Ana Uzquiano, Emilie Lemesre, Franck Perez, Julia Ladewig, Julien Ferent, Nurhan Ozlu, and Fiona Francis. Forebrain eml1 depletion reveals early centrosomal dysfunction causing subcortical heterotopia. The Journal of Cell Biology, Sep 2024. URL: https://doi.org/10.1083/jcb.202310157, doi:10.1083/jcb.202310157. This article has 6 citations.

4. (zaidi2024forebraineml1depletion pages 8-11): Donia Zaidi, Kaviya Chinnappa, Berfu Nur Yigit, Valeria Viola, Carmen Cifuentes-Diaz, Ammar Jabali, Ana Uzquiano, Emilie Lemesre, Franck Perez, Julia Ladewig, Julien Ferent, Nurhan Ozlu, and Fiona Francis. Forebrain eml1 depletion reveals early centrosomal dysfunction causing subcortical heterotopia. The Journal of Cell Biology, Sep 2024. URL: https://doi.org/10.1083/jcb.202310157, doi:10.1083/jcb.202310157. This article has 6 citations.

5. (zaidi2024forebraineml1depletion pages 1-2): Donia Zaidi, Kaviya Chinnappa, Berfu Nur Yigit, Valeria Viola, Carmen Cifuentes-Diaz, Ammar Jabali, Ana Uzquiano, Emilie Lemesre, Franck Perez, Julia Ladewig, Julien Ferent, Nurhan Ozlu, and Fiona Francis. Forebrain eml1 depletion reveals early centrosomal dysfunction causing subcortical heterotopia. The Journal of Cell Biology, Sep 2024. URL: https://doi.org/10.1083/jcb.202310157, doi:10.1083/jcb.202310157. This article has 6 citations.

6. (goo2023schizophreniaassociatedmitoticarrest pages 1-2): Bon Seong Goo, Dong Jin Mun, Seunghyun Kim, Truong Thi My Nhung, Su Been Lee, Youngsik Woo, Soo Jeong Kim, Bo Kyoung Suh, Sung Jin Park, Hee-Eun Lee, Kunyou Park, Hyunsoo Jang, Jong-Cheol Rah, Ki-Jun Yoon, Seung Tae Baek, Seung-Yeol Park, and Sang Ki Park. Schizophrenia-associated mitotic arrest deficient-1 (mad1) regulates the polarity of migrating neurons in the developing neocortex. Molecular Psychiatry, 28:856-870, Nov 2023. URL: https://doi.org/10.1038/s41380-022-01856-5, doi:10.1038/s41380-022-01856-5. This article has 23 citations and is from a highest quality peer-reviewed journal.

7. (sebastien2023doublecortinrestrictsneuronal pages 1-3): Muriel Sébastien, Alexandra L. Paquette, Emily N. P. Prowse, Adam G. Hendricks, and Gary J. Brouhard. Doublecortin restricts neuronal branching by regulating tubulin polyglutamylation. BioRxiv, Jun 2023. URL: https://doi.org/10.1101/2023.06.02.543327, doi:10.1101/2023.06.02.543327. This article has 3 citations.

8. (viola2024radialgliaprogenitor pages 2-5): Valeria Viola, Kaviya Chinnappa, and Fiona Francis. Radial glia progenitor polarity in health and disease. Frontiers in Cell and Developmental Biology, Oct 2024. URL: https://doi.org/10.3389/fcell.2024.1478283, doi:10.3389/fcell.2024.1478283. This article has 8 citations.

9. (zaidi2024forebraineml1depletion pages 11-13): Donia Zaidi, Kaviya Chinnappa, Berfu Nur Yigit, Valeria Viola, Carmen Cifuentes-Diaz, Ammar Jabali, Ana Uzquiano, Emilie Lemesre, Franck Perez, Julia Ladewig, Julien Ferent, Nurhan Ozlu, and Fiona Francis. Forebrain eml1 depletion reveals early centrosomal dysfunction causing subcortical heterotopia. The Journal of Cell Biology, Sep 2024. URL: https://doi.org/10.1083/jcb.202310157, doi:10.1083/jcb.202310157. This article has 6 citations.

10. (goo2023schizophreniaassociatedmitoticarrest pages 4-5): Bon Seong Goo, Dong Jin Mun, Seunghyun Kim, Truong Thi My Nhung, Su Been Lee, Youngsik Woo, Soo Jeong Kim, Bo Kyoung Suh, Sung Jin Park, Hee-Eun Lee, Kunyou Park, Hyunsoo Jang, Jong-Cheol Rah, Ki-Jun Yoon, Seung Tae Baek, Seung-Yeol Park, and Sang Ki Park. Schizophrenia-associated mitotic arrest deficient-1 (mad1) regulates the polarity of migrating neurons in the developing neocortex. Molecular Psychiatry, 28:856-870, Nov 2023. URL: https://doi.org/10.1038/s41380-022-01856-5, doi:10.1038/s41380-022-01856-5. This article has 23 citations and is from a highest quality peer-reviewed journal.

11. (tsai2024lissencephalyassociatedbaiap2variant pages 1-2): Meng-Han Tsai, Wan-Cian Lin, Shih-Ying Chen, M. Hsieh, F. Nian, Haw-Yuan Cheng, Hong-Jun Zhao, Shih-Shun Hung, Chi-Hsin Hsu, Pei-Shan Hou, Chien-Yi Tung, Mei-Hsuan Lee, and Jin-Wu Tsai. Lissencephaly-associated baiap2 variant causes defects in neuronal migration during brain development. Development, Dec 2024. URL: https://doi.org/10.1242/dev.201912, doi:10.1242/dev.201912. This article has 11 citations and is from a domain leading peer-reviewed journal.

12. (tsai2024lissencephalyassociatedbaiap2variant pages 2-5): Meng-Han Tsai, Wan-Cian Lin, Shih-Ying Chen, M. Hsieh, F. Nian, Haw-Yuan Cheng, Hong-Jun Zhao, Shih-Shun Hung, Chi-Hsin Hsu, Pei-Shan Hou, Chien-Yi Tung, Mei-Hsuan Lee, and Jin-Wu Tsai. Lissencephaly-associated baiap2 variant causes defects in neuronal migration during brain development. Development, Dec 2024. URL: https://doi.org/10.1242/dev.201912, doi:10.1242/dev.201912. This article has 11 citations and is from a domain leading peer-reviewed journal.

13. (leca2023codonmodificationof pages 5-6): Ines Leca, Alexander William Phillips, Lyubov Ushakova, Thomas David Cushion, and David Anthony Keays. Codon modification of tuba1a alters mrna levels and causes a severe neurodevelopmental phenotype in mice. Scientific Reports, Jan 2023. URL: https://doi.org/10.1038/s41598-023-27782-2, doi:10.1038/s41598-023-27782-2. This article has 9 citations and is from a peer-reviewed journal.

14. (ruizreig2024connectingneurodevelopmentto pages 1-2): Nuria Ruiz-Reig, Janne Hakanen, and Fadel Tissir. Connecting neurodevelopment to neurodegeneration: a spotlight on the role of kinesin superfamily protein 2a (kif2a). Neural Regeneration Research, 19:375-379, May 2024. URL: https://doi.org/10.4103/1673-5374.375298, doi:10.4103/1673-5374.375298. This article has 14 citations and is from a peer-reviewed journal.

15. (ruizreig2024connectingneurodevelopmentto pages 4-5): Nuria Ruiz-Reig, Janne Hakanen, and Fadel Tissir. Connecting neurodevelopment to neurodegeneration: a spotlight on the role of kinesin superfamily protein 2a (kif2a). Neural Regeneration Research, 19:375-379, May 2024. URL: https://doi.org/10.4103/1673-5374.375298, doi:10.4103/1673-5374.375298. This article has 14 citations and is from a peer-reviewed journal.

16. (ren2024lissencephalycausedby pages 2-4): Sijing Ren, Yu Kong, Ruihan Liu, Qiu-bo Li, Xuehua Shen, and Qing-xia Kong. Lissencephaly caused by a de novo mutation in tubulin tuba1a: a case report and literature review. Frontiers in Pediatrics, May 2024. URL: https://doi.org/10.3389/fped.2024.1367305, doi:10.3389/fped.2024.1367305. This article has 5 citations.

17. (ren2024lissencephalycausedby pages 4-6): Sijing Ren, Yu Kong, Ruihan Liu, Qiu-bo Li, Xuehua Shen, and Qing-xia Kong. Lissencephaly caused by a de novo mutation in tubulin tuba1a: a case report and literature review. Frontiers in Pediatrics, May 2024. URL: https://doi.org/10.3389/fped.2024.1367305, doi:10.3389/fped.2024.1367305. This article has 5 citations.

18. (ren2024lissencephalycausedby pages 1-2): Sijing Ren, Yu Kong, Ruihan Liu, Qiu-bo Li, Xuehua Shen, and Qing-xia Kong. Lissencephaly caused by a de novo mutation in tubulin tuba1a: a case report and literature review. Frontiers in Pediatrics, May 2024. URL: https://doi.org/10.3389/fped.2024.1367305, doi:10.3389/fped.2024.1367305. This article has 5 citations.

19. (procopio2024phenotypicvariabilityin pages 2-4): Radha Procopio, Francesco Fortunato, Monica Gagliardi, Mariagrazia Talarico, Ilaria Sammarra, Maria Chiara Sarubbi, Donatella Malanga, Grazia Annesi, and Antonio Gambardella. Phenotypic variability in novel doublecortin gene variants associated with subcortical band heterotopia. International Journal of Molecular Sciences, 25:5505, May 2024. URL: https://doi.org/10.3390/ijms25105505, doi:10.3390/ijms25105505. This article has 8 citations.

20. (procopio2024phenotypicvariabilityin pages 1-2): Radha Procopio, Francesco Fortunato, Monica Gagliardi, Mariagrazia Talarico, Ilaria Sammarra, Maria Chiara Sarubbi, Donatella Malanga, Grazia Annesi, and Antonio Gambardella. Phenotypic variability in novel doublecortin gene variants associated with subcortical band heterotopia. International Journal of Molecular Sciences, 25:5505, May 2024. URL: https://doi.org/10.3390/ijms25105505, doi:10.3390/ijms25105505. This article has 8 citations.

21. (sakamoto2024lossofdnah5 pages 18-20): Koichiro Sakamoto, Masakazu Miyajima, Madoka Nakajima, Ikuko Ogino, Kou Horikoshi, Ryo Miyahara, Kaito Kawamura, Kostadin Karagiozov, Chihiro Kamohara, Eri Nakamura, Nobuhiro Tada, and Akihide Kondo. Loss of dnah5 downregulates dync1h1 expression, causing cortical development disorders and congenital hydrocephalus. Cells, 13:1882, Nov 2024. URL: https://doi.org/10.3390/cells13221882, doi:10.3390/cells13221882. This article has 2 citations.

22. (tsai2024novellissencephalyassociatedndel1 pages 16-17): Meng-Han Tsai, Hao-Chen Ke, Wan-Cian Lin, Fang-Shin Nian, Chia-Wei Huang, Haw-Yuan Cheng, Chi-Sin Hsu, Tiziana Granata, Chien-Hui Chang, Barbara Castellotti, Shin-Yi Lin, Fabio M. Doniselli, Cheng-Ju Lu, Silvana Franceschetti, Francesca Ragona, Pei-Shan Hou, Laura Canafoglia, Chien-Yi Tung, Mei-Hsuan Lee, Won-Jing Wang, and Jin-Wu Tsai. Novel lissencephaly-associated ndel1 variant reveals distinct roles of nde1 and ndel1 in nucleokinesis and human cortical malformations. Acta Neuropathologica, Jan 2024. URL: https://doi.org/10.1007/s00401-023-02665-y, doi:10.1007/s00401-023-02665-y. This article has 11 citations and is from a highest quality peer-reviewed journal.

23. (zaidi2024forebraineml1depletion pages 21-26): Donia Zaidi, Kaviya Chinnappa, Berfu Nur Yigit, Valeria Viola, Carmen Cifuentes-Diaz, Ammar Jabali, Ana Uzquiano, Emilie Lemesre, Franck Perez, Julia Ladewig, Julien Ferent, Nurhan Ozlu, and Fiona Francis. Forebrain eml1 depletion reveals early centrosomal dysfunction causing subcortical heterotopia. The Journal of Cell Biology, Sep 2024. URL: https://doi.org/10.1083/jcb.202310157, doi:10.1083/jcb.202310157. This article has 6 citations.

## Artifacts

- [Edison artifact artifact-00](falcon_artifacts/artifact-00.md)
