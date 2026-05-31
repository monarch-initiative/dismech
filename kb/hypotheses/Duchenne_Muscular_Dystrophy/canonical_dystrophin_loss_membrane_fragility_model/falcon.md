---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-23T18:53:05.132820'
end_time: '2026-05-23T19:03:11.288051'
duration_seconds: 606.16
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: Duchenne Muscular Dystrophy
  category: Genetic
  hypothesis_group_id: canonical_dystrophin_loss_membrane_fragility_model
  hypothesis_label: Canonical Dystrophin Loss and Membrane Fragility Model
  hypothesis_status: CANONICAL
  hypothesis_yaml: "hypothesis_group_id: canonical_dystrophin_loss_membrane_fragility_model\n\
    hypothesis_label: Canonical Dystrophin Loss and Membrane Fragility Model\nstatus:\
    \ CANONICAL\ndescription: Out-of-frame DMD variants abolish functional dystrophin,\
    \ the cytoskeletal link between cytoplasmic\n  F-actin and the sarcolemmal dystrophin-glycoprotein\
    \ complex (DGC). Without dystrophin the DGC is destabilized\n  at the sarcolemma,\
    \ leaving muscle fibers vulnerable to contraction-induced mechanical injury, calcium\n\
    \  influx through stretched/damaged membrane, and activation of calcium-dependent\
    \ proteases. Repeated cycles\n  of fiber necrosis, satellite-cell-driven regeneration,\
    \ chronic inflammation, and progressive fibro-fatty\n  replacement of muscle ultimately\
    \ exhaust regenerative capacity, producing the characteristic progressive\n  proximal\
    \ weakness, cardiomyopathy, respiratory failure, and short life expectancy of\
    \ Duchenne muscular\n  dystrophy. Exon-skipping and gene-replacement therapies\
    \ that restore even partial dystrophin expression\n  provide interventional validation\
    \ of this canonical chain.\nevidence:\n- reference: PMID:16770791\n  supports:\
    \ SUPPORT\n  evidence_source: HUMAN_CLINICAL\n  snippet: severe Duchenne and milder\
    \ Becker muscular dystrophy are both caused by mutations\n  explanation: |\n \
    \   Canonical mechanism review used as the seed reference for the hypothesis-search\
    \ deep-research run."
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 40
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
- **Disease Name:** Duchenne Muscular Dystrophy
- **Category:** Genetic

## Target Hypothesis
- **Hypothesis ID:** canonical_dystrophin_loss_membrane_fragility_model
- **Hypothesis Label:** Canonical Dystrophin Loss and Membrane Fragility Model
- **Status in KB:** CANONICAL

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: canonical_dystrophin_loss_membrane_fragility_model
hypothesis_label: Canonical Dystrophin Loss and Membrane Fragility Model
status: CANONICAL
description: Out-of-frame DMD variants abolish functional dystrophin, the cytoskeletal link between cytoplasmic
  F-actin and the sarcolemmal dystrophin-glycoprotein complex (DGC). Without dystrophin the DGC is destabilized
  at the sarcolemma, leaving muscle fibers vulnerable to contraction-induced mechanical injury, calcium
  influx through stretched/damaged membrane, and activation of calcium-dependent proteases. Repeated cycles
  of fiber necrosis, satellite-cell-driven regeneration, chronic inflammation, and progressive fibro-fatty
  replacement of muscle ultimately exhaust regenerative capacity, producing the characteristic progressive
  proximal weakness, cardiomyopathy, respiratory failure, and short life expectancy of Duchenne muscular
  dystrophy. Exon-skipping and gene-replacement therapies that restore even partial dystrophin expression
  provide interventional validation of this canonical chain.
evidence:
- reference: PMID:16770791
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: severe Duchenne and milder Becker muscular dystrophy are both caused by mutations
  explanation: |
    Canonical mechanism review used as the seed reference for the hypothesis-search deep-research run.
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
- **Disease Name:** Duchenne Muscular Dystrophy
- **Category:** Genetic

## Target Hypothesis
- **Hypothesis ID:** canonical_dystrophin_loss_membrane_fragility_model
- **Hypothesis Label:** Canonical Dystrophin Loss and Membrane Fragility Model
- **Status in KB:** CANONICAL

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: canonical_dystrophin_loss_membrane_fragility_model
hypothesis_label: Canonical Dystrophin Loss and Membrane Fragility Model
status: CANONICAL
description: Out-of-frame DMD variants abolish functional dystrophin, the cytoskeletal link between cytoplasmic
  F-actin and the sarcolemmal dystrophin-glycoprotein complex (DGC). Without dystrophin the DGC is destabilized
  at the sarcolemma, leaving muscle fibers vulnerable to contraction-induced mechanical injury, calcium
  influx through stretched/damaged membrane, and activation of calcium-dependent proteases. Repeated cycles
  of fiber necrosis, satellite-cell-driven regeneration, chronic inflammation, and progressive fibro-fatty
  replacement of muscle ultimately exhaust regenerative capacity, producing the characteristic progressive
  proximal weakness, cardiomyopathy, respiratory failure, and short life expectancy of Duchenne muscular
  dystrophy. Exon-skipping and gene-replacement therapies that restore even partial dystrophin expression
  provide interventional validation of this canonical chain.
evidence:
- reference: PMID:16770791
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: severe Duchenne and milder Becker muscular dystrophy are both caused by mutations
  explanation: |
    Canonical mechanism review used as the seed reference for the hypothesis-search deep-research run.
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


# Hypothesis-Search Research Report (Duchenne Muscular Dystrophy)

**Hypothesis ID:** canonical_dystrophin_loss_membrane_fragility_model  
**Hypothesis label:** Canonical Dystrophin Loss and Membrane Fragility Model  
**Search date:** 2026-05-24  

## Executive Judgment

**Verdict: Supported, with important scope-qualifiers.** Multiple lines of interventional evidence strongly support the core causal idea that dystrophin loss renders muscle (and heart) vulnerable to contraction-induced injury and that restoring membrane-associated dystrophin function (or reducing mechanical load / stabilizing membrane) can mitigate injury and downstream pathology (russell2023modulatingfastskeletal pages 1-2, hahn2023rapidrestitutionof pages 1-2, zhou2024systemicdeliveryof pages 1-2, dambrosio2023evolvingtherapeuticoptions pages 8-9, mendell2023long‐termsafetyand pages 1-2). However, the literature also qualifies a strict “membrane tear → Ca2+ influx” sequence: Ca2+ entry through mechanosensitive and store-operated pathways (TRPC/SOCE/TRPV2) can be sufficient to drive dystrophy-like pathology even without overt membrane permeability in some models, and sarcoplasmic-reticulum (SR) Ca2+ leak / handling defects can be a parallel (or amplifying) upstream source of Ca2+ dyshomeostasis (millay2009calciuminfluxis pages 1-2, burr2015geneticevidencein pages 5-6, head2010branchedfibresin pages 1-2, lorin2015dystrophiccardiomyopathyrole pages 11-13). In addition, emerging therapy data show that micro-dystrophin can restore many structural outcomes but may not fully restore all dystrophin-dependent signaling/scaffolding functions in heart (e.g., cavin 4 localization) compared with full-length dystrophin (zhou2024systemicdeliveryof pages 1-2).

## Key Concepts and Definitions (current understanding)

1. **Dystrophin and the dystrophin-glycoprotein complex (DGC/DAPC):** Dystrophin provides a mechanical and signaling scaffold linking intracellular F-actin to transmembrane and extracellular matrix elements; dystrophin loss destabilizes this interface, increasing vulnerability to mechanical stress and altering membrane-associated signaling/ion-channel organization (zhou2024systemicdeliveryof pages 1-2, russell2023modulatingfastskeletal pages 1-2).

2. **Sarcolemmal fragility and contraction-induced injury:** In dystrophin deficiency, mechanical stress during contraction—especially eccentric (lengthening) contraction—drives membrane injury/rupture and functional force loss, supporting a mechanical-injury trigger (russell2023modulatingfastskeletal pages 1-2).

3. **Ca2+ dyshomeostasis as a proximate effector:** Elevated cytosolic Ca2+ is widely supported as a key downstream effector that can activate proteases and mitochondrial injury pathways leading to necrosis; importantly, Ca2+ dysregulation can be caused by (i) membrane disruption, (ii) mechanosensitive channel opening (TRPC/TRPV), (iii) store-operated Ca2+ entry (STIM1–ORAI1), and (iv) SR Ca2+ leak/handling defects (burr2015geneticevidencein pages 5-6, head2010branchedfibresin pages 1-2, millay2009calciuminfluxis pages 1-2, matsumura2011stretchactivatedcalciumchannel pages 1-2).

4. **Interventional validation:** Therapies that (a) partially restore dystrophin function (micro-/full-length dystrophin), (b) stabilize membranes (synthetic amphiphilic copolymers/poloxamers), or (c) reduce mechanical load (fast skeletal myosin inhibition) provide mechanistic tests of the chain (hahn2023rapidrestitutionof pages 1-2, zhou2024systemicdeliveryof pages 1-2, russell2023modulatingfastskeletal pages 1-2, dambrosio2023evolvingtherapeuticoptions pages 8-9, mendell2023long‐termsafetyand pages 1-2).

## Mechanistic Causal Chain (strength of links)

Below is the seed hypothesis chain, annotated with where evidence is strongest vs. inferential.

### 1) Out-of-frame DMD variants → loss of functional dystrophin
**Status:** Established background premise; not re-litigated in this run.

### 2) Dystrophin loss → DGC destabilization / impaired sarcolemmal support
**Strong evidence:** Full-length dystrophin gene therapy in mdx4cv restores DGC components at the sarcolemma, consistent with dystrophin being required for DGC restoration (Nature Communications, **2024-07**; https://doi.org/10.1038/s41467-024-50569-6) (zhou2024systemicdeliveryof pages 1-2).

### 3) DGC/dystrophin loss → contraction-induced sarcolemmal injury (tears/permeability)
**Strong evidence (interventional physiology):** In mdx muscle, contraction of intact muscle drives sarcolemmal rupture and force loss, particularly under eccentric conditions; removal of contraction prevents injury, supporting contraction dependence rather than passive stretch alone (JCI, **2023-05**; https://doi.org/10.1172/jci153837) (russell2023modulatingfastskeletal pages 1-2).

### 4) Membrane injury and/or mechanosensitive channels → Ca2+ influx / Ca2+ dyshomeostasis
**Strong but not exclusive:** Evidence supports mechanosensitive-channel contributions and pharmacologic reduction of damage. For example, TRPC1-related stretch-activated channel activity correlates with dystrophic severity, and streptomycin (a SAC blocker) reduced CK and prevented exercise-induced rises in muscle Ca2+ and Evans blue dye uptake in mdx mice (AJP Cell Physiol, **2011-12**; https://doi.org/10.1152/ajpcell.00056.2011) (matsumura2011stretchactivatedcalciumchannel pages 1-2).

**Competing/qualifying evidence:** TRPC3 overexpression (∼6× protein at sarcolemma) caused dramatically enhanced SOCE and dystrophy-like disease, supporting that Ca2+ influx can be *sufficient* to induce dystrophy-like pathology “independent of membrane fragility” (PNAS, **2009-11**; https://doi.org/10.1073/pnas.0906591106) (millay2009calciuminfluxis pages 1-2). A genetics-focused synthesis further emphasizes that dystrophy-like histopathology can occur **without membrane permeability** in some Ca2+ entry models (burr2015geneticevidencein pages 5-6).

### 5) Ca2+ dyshomeostasis → protease activation / mitochondrial injury → necrosis
**Moderate-to-strong evidence, but partially inferred in the newest primary therapy papers:** The Ca2+ hypothesis is supported by mouse genetic evidence summarized in Burr & Molkentin (Cell Death & Differentiation, **2015-06**; https://doi.org/10.1038/cdd.2015.65): calpastatin overexpression decreased histopathology and Evans blue dye uptake, and Ppif deletion decreased histopathology/EBD uptake and reduced mitochondrial swelling, consistent with Ca2+-activated protease and mitochondrial permeability transition involvement (burr2015geneticevidencein pages 5-6).

**Qualifier:** Some late-stage phenotypes may be amplified by SR Ca2+ handling defects (RyR/SERCA dysfunction) and regenerated/branched fiber architecture; in older mdx muscles with >90% branched fibers, a moderate eccentric protocol caused **40 ± 8%** maximal force loss, whereas controls or mdx with <10% branched fibers had no force loss (Experimental Physiology, **2010-05**; https://doi.org/10.1113/expphysiol.2009.052019) (head2010branchedfibresin pages 1-2).

### 6) Necrosis → inflammation/regeneration cycles → fibrosis/fatty replacement → clinical progression
**Strong at phenomenological level; mechanistic edges partially inferred in the most recent interventional studies:** EDG-5506 reduced fibrosis in key tissues with longer-term treatment while protecting from stress injury, consistent with injury→fibrosis coupling (JCI, **2023-05**) (russell2023modulatingfastskeletal pages 1-2). Micro-dystrophin gene therapy studies report sustained functional benefits and molecular evidence consistent with membrane stabilization (sarcolemmal localization and DAPC restoration), but the causal step-by-step linkage to inflammation/fibrosis is often inferred rather than directly mapped longitudinally in humans (mendell2023long‐termsafetyand pages 1-2, dambrosio2023evolvingtherapeuticoptions pages 8-9, roberts2023therapeuticapproachesfor pages 12-15).

## Strongest Direct Evidence for the Hypothesis

### A. Contraction is a causal trigger of injury in dystrophin-deficient muscle
Russell et al. directly link dystrophin absence to **contraction-driven** sarcolemmal rupture/force loss, and show that removing contraction prevents injury; this is among the most direct tests of the mechanical-injury segment of the canonical chain (JCI, 2023-05; https://doi.org/10.1172/jci153837) (russell2023modulatingfastskeletal pages 1-2).

### B. Membrane stabilization can rapidly rescue dystrophin-deficient fiber function and Ca2+ transients
Hahn et al. show that synthetic amphiphilic copolymers (including P188) rapidly restore twitch function in single live mdx fibers, with large quantitative effects (e.g., P188 150 μM: **+220%** twitch SL shortening vs vehicle in mdx fibers) and improved Ca2+ transients (Skeletal Muscle, 2023-05; https://doi.org/10.1186/s13395-023-00318-y) (hahn2023rapidrestitutionof pages 1-2). This supports membrane dysfunction as proximate to functional impairment.

### C. Dystrophin restoration restores DGC localization and improves pathology
Zhou et al. show triple-AAV full-length dystrophin delivery restores DGC components at the sarcolemma and improves histopathology/contractility/strength in mdx4cv mice (Nature Communications, 2024-07; https://doi.org/10.1038/s41467-024-50569-6) (zhou2024systemicdeliveryof pages 1-2). This is direct evidence for dystrophin→DGC→functional benefit.

### D. Human interventional validation: micro-dystrophin gene therapy signals
Two complementary sources provide quantitative human evidence:

* D’Ambrosio & Mendell summarize SRP-9001 molecular and functional readouts including **>80% micro-dystrophin-positive fibers** (mean intensity **96%**) and western blot micro-dystrophin **74% of normal**, with NSAA signals and notable immune-mediated safety events in some deletion subtypes (Neurotherapeutics, 2023-10; https://doi.org/10.1007/s13311-023-01423-y) (dambrosio2023evolvingtherapeuticoptions pages 8-9).
* Mendell et al. report long-term follow-up (Study 101; NCT03375164) with mean NSAA rising from **20.5 to 27.5** at year 4 (mean change **+7.0**, SD 2.9), and a propensity-score weighted comparison showing a **9.4** (SE 3.4) least-squares mean difference vs external control (P=0.0125) (Muscle & Nerve, 2024-08; https://doi.org/10.1002/mus.27955) (mendell2023long‐termsafetyand pages 1-2).

These clinical data are consistent with the hypothesis’ claim that even partial dystrophin restoration can modify downstream functional trajectory.

## Evidence Against / Limits / Failure Modes

1. **Ca2+ entry can be sufficient without primary membrane permeability:** TRPC3 transgenic models show that elevating Ca2+ entry/SOCE alone can produce a dystrophy-like phenotype and that the phenotype can occur “independent of membrane fragility” (Millay et al., PNAS, 2009-11; https://doi.org/10.1073/pnas.0906591106) (millay2009calciuminfluxis pages 1-2). Burr & Molkentin further synthesize evidence that dystrophy-like histopathology can occur **without membrane permeability** in some Ca2+ entry models (burr2015geneticevidencein pages 5-6). This *competes* with a strict “membrane tear first” ordering.

2. **SR Ca2+ leak/handling and late-stage architecture (branched fibers) may dominate some phases:** In older mdx muscle, the strong association between branched fibers and eccentric-contraction force loss (40±8%) suggests a stage-dependent mechanism where regeneration-induced architecture and SR Ca2+ handling defects become major amplifiers (head2010branchedfibresin pages 1-2).

3. **Membrane sealing is not uniformly beneficial across tissues/outcomes:** Cardiac-focused reviews cite benefit of poloxamer 188 in some dystrophin-deficient models but also note deleterious effects in dystrophic skeletal muscle in other studies, limiting a universal membrane-sealant strategy (gandhi2024cardiomyopathyinduchenne pages 2-4).

4. **Micro-dystrophin may not fully restore all dystrophin-dependent signaling:** Full-length dystrophin (but not micro-dystrophin) restored cavin 4 localization/signaling in mdx4cv heart in Zhou et al., suggesting a scope limit of the “partial restoration is sufficient for all endpoints” claim (zhou2024systemicdeliveryof pages 1-2).

## Recent Developments (prioritizing 2023–2024)

### 1) Mechanical-load reduction as a mechanistic therapy
EDG-5506 (fast skeletal myosin inhibitor) provides a mechanistically targeted strategy that directly tests the “contraction-induced injury” edge: **<15%** contraction reduction protected mdx muscle from stress injury and reduced fibrosis over time (JCI, 2023-05; https://doi.org/10.1172/jci153837) (russell2023modulatingfastskeletal pages 1-2).

### 2) Membrane-stabilizing polymers with rapid functional rescue in dystrophin-deficient fibers
Synthetic copolymers (including P188) can rapidly normalize twitch performance and Ca2+ transients in isolated mdx fibers with large effect sizes (Skeletal Muscle, 2023-05; https://doi.org/10.1186/s13395-023-00318-y) (hahn2023rapidrestitutionof pages 1-2). This supports real-time membrane biophysics as a druggable mechanism.

### 3) Full-length dystrophin delivery beyond micro-dystrophin
Triple-vector full-length dystrophin assembly in vivo is a major 2024 development; beyond DGC restoration and functional improvement, it highlights signaling limitations of micro-dystrophin in heart (Nature Communications, 2024-07; https://doi.org/10.1038/s41467-024-50569-6) (zhou2024systemicdeliveryof pages 1-2).

### 4) Clinical micro-dystrophin gene therapy: durability signals and safety caveats
Long-term follow-up of delandistrogene moxeparvovec suggests durable functional benefit (NSAA +7 over 4 years in n=4) and manageable short-term TRAEs in that small cohort (Muscle & Nerve, 2024-08; https://doi.org/10.1002/mus.27955) (mendell2023long‐termsafetyand pages 1-2). Contemporary syntheses emphasize both molecular expression measures and immune-mediated safety signals in certain deletion subtypes (Neurotherapeutics, 2023-10) (dambrosio2023evolvingtherapeuticoptions pages 8-9).

### 5) Objective pharmacodynamic biomarkers tied to micro-dystrophin expression
Boehler et al. propose the **N-terminal titin fragment** as a non-invasive PD biomarker correlated with micro-dystrophin expression across mice, dogs, and humans and more sensitive than CK at low expression levels (Skeletal Muscle, 2024-01; https://doi.org/10.1186/s13395-023-00334-y) (boehler2024nterminaltitinfragment pages 1-2).

## Current Applications and Real-World Implementations

1. **Clinical gene therapy implementation and monitoring:** ClinicalTrials.gov entries specify micro-dystrophin quantification endpoints (Western blot, immunofluorescence, percent dystrophin-positive fibers at Week 12) and functional endpoints (NSAA at Week 48) for SRP-9001 (trial record first posted 2018; NCT03769116; https://clinicaltrials.gov/study/NCT03769116) (NCT03769116 chunk 1). These endpoints operationalize the “dystrophin restoration → sarcolemmal stabilization → function” logic.

2. **Use of functional outcomes plus emerging biomarkers:** NSAA is used as the core functional outcome in multiple SRP-9001 studies (NCT03769116 chunk 1, mendell2023long‐termsafetyand pages 1-2). Biomarker development (titin fragment) is positioned to reduce reliance on variable CK and strengthen mechanistic attribution in trials (boehler2024nterminaltitinfragment pages 1-2).

3. **Mechanism-guided therapeutics beyond gene replacement:** EDG-5506 represents a direct translation of the contraction-injury mechanism into a pharmacologic strategy potentially complementary to dystrophin restoration (russell2023modulatingfastskeletal pages 1-2).

## Expert Opinions / Authoritative Analyses (clearly labeled)

* **Nature Reviews Drug Discovery (review-level):** Roberts et al. summarize early SRP-9001 signals (NSAA improvements, CK reductions, MRI fat fraction/qT2 improvements) while emphasizing field-wide safety concerns at high vector doses (Nature Reviews Drug Discovery, 2023-08; https://doi.org/10.1038/s41573-023-00775-6) (roberts2023therapeuticapproachesfor pages 12-15). This frames the mechanistic validation as plausible but complicated by dose/immunity/transgene design.

* **Cell Death & Differentiation (review-level genetics synthesis):** Burr & Molkentin argue that mouse genetics largely “solidify” Ca2+ as a proximate effector of myofiber death, motivating therapeutic targeting of Ca2+ entry/handling pathways in addition to membrane mechanics (Cell Death & Differentiation, 2015-06; https://doi.org/10.1038/cdd.2015.65) (burr2015geneticevidencein pages 5-6).

## Relevant Statistics and Data (selected)

* **Membrane stabilization in isolated fibers:** mdx twitch shortening reduced to **30%** of control; P188 restored twitch shortening by **+110%** (15 μM) and **+220%** (150 μM) vs vehicle; inverted triblock **+180%** (15 μM) (hahn2023rapidrestitutionof pages 1-2).

* **Branched fiber stage effect:** old mdx (>90% branched fibers) eccentric protocol caused **40 ± 8%** maximal force loss; none in controls or mdx with <10% branched fibers (head2010branchedfibresin pages 1-2).

* **SAC blockade regimen:** streptomycin **182 mg/kg i.p. daily**, starting at age 18 days for 18 days (treated n=16; control n=37), reduced CK and prevented exercise-induced increases in muscle Ca2+ and Evans blue dye uptake (matsumura2011stretchactivatedcalciumchannel pages 1-2).

* **Micro-dystrophin expression and function (reviewed clinical summary):** mean **>80%** micro-dystrophin-positive fibers (intensity **96%**) and western blot **74% of normal**; NSAA signals reported (+5.5 in one analysis; +3.9 at week 52; +3.2 vs external control) (dambrosio2023evolvingtherapeuticoptions pages 8-9).

* **Long-term NSAA (primary clinical trial follow-up):** baseline 20.5 to 27.5 at year 4 (mean +7.0); external-control comparison LS mean difference 9.4 (SE 3.4), P=0.0125; 18 treatment-related adverse events, all within 70 days and resolved (mendell2023long‐termsafetyand pages 1-2).

## Evidence Matrix (required)

The evidence matrix below is designed for curator verification and includes supports/refutes/qualifies/competes tags, mechanistic claim tested, quantitative findings, context, and limitations.

| Citation | Evidence type | Supports / refutes / qualifies / competing | Mechanistic claim tested | Key findings (include quantitative stats) | Context (tissue/model, stage) | Confidence & limitations |
|---|---|---|---|---|---|---|
| Russell et al., 2023, *J Clin Invest*, doi:10.1172/JCI153837, https://doi.org/10.1172/jci153837 | Model organism | Supports | Dystrophin loss causes contraction-driven sarcolemmal rupture/injury; reducing contraction should interrupt downstream damage/fibrosis | Mechanical stress in mdx muscle causes sarcolemmal rupture and force loss, especially during eccentric contractions; denervation or BTS prevents injury. EDG-5506 reduced fast myosin activity with IC50 ~0.2–0.4 μM for fast myofibrils and >100 μM for slow/cardiac myofibrils; modest contraction reduction (<15%) protected mdx muscle from stress injury, reduced fibrosis with longer treatment, and in dystrophic dogs lowered circulating injury biomarkers and increased activity (russell2023modulatingfastskeletal pages 1-2) | mdx mouse skeletal muscle; dystrophic dog; acute injury and longer-term treatment | High for contraction-dependence and interventional rescue; limited direct quantitation in the excerpt for fibrosis magnitude and no human efficacy data |
| Hahn et al., 2023, *Skeletal Muscle*, doi:10.1186/s13395-023-00318-y, https://doi.org/10.1186/s13395-023-00318-y | In vitro / ex vivo fiber physiology | Supports | Membrane instability contributes to defective Ca2+ handling and contractility; membrane sealants can rapidly rescue function | mdx FDB fibers had twitch sarcomere shortening reduced to 30% of control (P<0.001). Copolymers restored shortening: P188 +110% at 15 μM and +220% at 150 μM; diblock +50% at both doses; inverted triblock +180% at 15 μM and +90% at 150 μM (all P<0.05). Depressed twitch Ca2+ transients in mdx fibers improved with P188 and inverted triblock (P<0.001) (hahn2023rapidrestitutionof pages 1-2) | Isolated live flexor digitorum brevis fibers from adult mdx mice | High for rapid functional rescue in isolated fibers; limited for chronic pathology, inflammation, fibrosis, and human translation |
| Zhou et al., 2024, *Nat Commun*, doi:10.1038/s41467-024-50569-6, https://doi.org/10.1038/s41467-024-50569-6 | Model organism / gene therapy | Supports and qualifies | Restoring full-length dystrophin should reassemble DGC and improve pathology; micro-dystrophin may be incomplete for some signaling functions | Triple-AAV full-length dystrophin restored dystrophin expression in skeletal and cardiac muscle of mdx4cv mice, restored DGC components at the sarcolemma, and improved histopathology, contractility, and overall strength. Full-length dystrophin, unlike micro-dystrophin, also restored defective cavin 4 localization/associated signaling in heart, suggesting membrane stabilization alone is not the whole story (zhou2024systemicdeliveryof pages 1-2) | mdx4cv mouse skeletal and cardiac muscle | High for proof-of-concept gene restoration; excerpt lacks detailed quantitative effect sizes and does not directly measure membrane tears/Ca2+ influx |
| Millay et al., 2009, *PNAS*, doi:10.1073/pnas.0906591106, https://doi.org/10.1073/pnas.0906591106 | Model organism / genetic perturbation | Competing and qualifies | Increased Ca2+ influx through TRPC channels can itself be sufficient to cause dystrophy-like disease, potentially independent of membrane fragility | Skeletal muscle TRPC3 transgenic mice showed ~6-fold TRPC3 overexpression, markedly enhanced SOCE in FDB fibers, and severe dystrophy-like pathology with central nucleation, fibrosis, inflammation, and wasting. Transgene-mediated inhibition of TRPC channels reduced calcium influx and ameliorated disease in mdx and Sgcd-deficient mice (millay2009calciuminfluxis pages 1-2) | TRPC3 transgenic mice; mdx and δ-sarcoglycan-deficient models | High for Ca2+-centric sufficiency; qualifies the canonical model by showing dystrophy-like pathology can arise without primary membrane fragility as the sole driver |
| Burr & Molkentin, 2015, *Cell Death Differ*, doi:10.1038/cdd.2015.65, https://doi.org/10.1038/cdd.2015.65 | Review-level synthesis of genetic perturbation studies | Qualifies and supports | Ca2+ dysregulation is the key proximate effector downstream of dystrophin loss; membrane permeability is not always required | Summarizes mouse genetics showing: TRPC3 overexpression causes dystrophy-like histopathology without membrane permeability; dominant-negative TRPC/dnTRPC6, dnTRPV2, Orai1 knockdown, and dnOrai reduce pathology/CK; calpastatin overexpression lowers histopathology and Evans blue dye uptake; Ppif deletion reduces histopathology/EBD uptake and mitochondrial swelling; SERCA1 overexpression decreases histopathology and serum CK, and rescues TRPC3-driven pathology (burr2015geneticevidencein pages 5-6) | Multiple mouse muscular dystrophy models | Moderate-high because mechanistic breadth is strong, but this is review-level synthesis rather than a single primary experiment |
| Matsumura et al., 2011, *Am J Physiol Cell Physiol*, doi:10.1152/ajpcell.00056.2011, https://doi.org/10.1152/ajpcell.00056.2011 | Model organism / pharmacologic intervention | Supports | Stretch-activated/TRPC-linked channels contribute to abnormal Ca2+ entry, membrane permeability, and muscle injury in dystrophin deficiency | TRPC1 correlated with dystrophic severity. Streptomycin SAC blockade (182 mg/kg i.p. daily), given to mdx mice from age 18 days for 18 days (treated n=16; saline controls n=37), reduced circulating CK and prevented exercise-induced increases in total muscle Ca2+ and Evans blue dye uptake in diaphragm and sternomastoid; also attenuated limb muscle damage/permeability changes (matsumura2011stretchactivatedcalciumchannel pages 1-2) | mdx mice, early disease; diaphragm, sternomastoid, limb muscle | Moderate-high; supports SAC involvement but streptomycin is not fully specific and human relevance remains uncertain |
| Head, 2010, *Exp Physiol*, doi:10.1113/expphysiol.2009.052019, https://doi.org/10.1113/expphysiol.2009.052019 | Ex vivo / model organism physiology | Qualifies | Later-stage weakness/damage may depend on branched regenerated fibers and SR Ca2+ handling abnormalities, not just acute membrane rupture | In old mdx muscles with >90% branched fibers, a moderate eccentric protocol caused 40 ± 8% loss of maximal force; the same protocol caused no force loss in controls or mdx muscles with <10% branched fibers. The paper emphasizes abnormal Ca2+ transients and contributions from RyR/SERCA dysfunction and mechanosensitive channels (head2010branchedfibresin pages 1-2) | Aged mdx skeletal muscle; regenerated/branched fibers | Moderate-high for stage-specific qualification; less direct for DGC destabilization and no therapeutic intervention in this excerpt |
| Gandhi et al., 2024, *Cells*, doi:10.3390/cells13141168, https://doi.org/10.3390/cells13141168 | Review with cited experimental cardiac data | Supports and qualifies | Dystrophin loss in heart causes membrane leak/permeability and can be transiently improved by membrane sealants, but membrane sealing may not fully solve multisystem pathology | Review cites significantly increased Evans blue dye leakage in mdx left ventricular cardiomyocytes and elevated serum cTnI as evidence of cardiac membrane permeability. Poloxamer 188 improved acute cardiac function in murine/canine models, but other skeletal muscle studies reported deleterious or mixed effects, limiting generalization (gandhi2024mitochondriainduchenne pages 3-5, gandhi2024cardiomyopathyinduchenne pages 2-4) | Cardiac muscle emphasis; murine and canine dystrophin-deficient models | Moderate; helpful for cardiac scope but largely synthesized/review-level and not definitive on long-term disease modification |
| D’Ambrosio & Mendell, 2023, *Neurotherapeutics*, doi:10.1007/s13311-023-01423-y, https://doi.org/10.1007/s13311-023-01423-y | Review-level synthesis of clinical trial data | Supports | Clinical micro-dystrophin restoration provides interventional validation of the canonical chain via sarcolemmal localization and functional benefit | For SRP-9001/delandistrogene moxeparvovec: ~3.3 vector genomes per nucleus; >80% micro-dystrophin-positive fibers in gastrocnemius with mean intensity 96.0% at sarcolemma; western blot mean micro-dystrophin 74% of normal. Functional signals included mean NSAA improvement 5.5 points in one analysis, >2-point improvement at 1 year vs placebo in younger cohort, and +3.9 from baseline at week 52 with +3.2 vs external control in another study. Safety signals included immune-mediated myositis/myocarditis with elevated troponin I in some large-deletion patients, plus transaminase/GGT elevation, vomiting, transient thrombocytopenia (dambrosio2023evolvingtherapeuticoptions pages 8-9) | Ambulatory boys with DMD treated with SRP-9001/ELEVIDYS | Moderate-high for clinical relevance, but review-level and cross-trial synthesis; causal link from expression to long-term membrane stabilization is inferred |
| Mendell et al., 2024, *Muscle & Nerve*, doi:10.1002/mus.27955, https://doi.org/10.1002/mus.27955 | Human clinical trial | Supports | Sustained micro-dystrophin expression/localization may alter disease progression in DMD | Phase 1/2a Study 101 (NCT03375164), 4 ambulatory boys, mean age 5.1 years: 18 treatment-related adverse events, all within 70 days and resolved. Mean NSAA rose from 20.5 at baseline to 27.5 at year 4; mean change +7.0 (SD 2.9). Propensity-score–weighted comparison versus external control showed LS mean difference 9.4 (SE 3.4), P=0.0125. Prior study reports described robust sarcolemmal micro-dystrophin localization and DAPC restoration (mendell2023long‐termsafetyand pages 1-2, mendell2023long‐termsafetyand pages 2-3) | Ambulatory pediatric DMD, long-term follow-up after single IV gene transfer | High for long-term functional signal in a small cohort; major limitations are n=4, external controls, and incomplete mechanistic readout at late follow-up |
| Roberts et al., 2023, *Nat Rev Drug Discov*, doi:10.1038/s41573-023-00775-6, https://doi.org/10.1038/s41573-023-00775-6 | Review-level synthesis | Supports and qualifies | Micro-dystrophin trials provide pharmacodynamic/clinical support, but safety and trial heterogeneity limit strong mechanistic inference | Summarizes phase I/2a SRP-9001 at 2×10^14 vg/kg (n=4): detectable dystrophin by 12 weeks, improved NSAA scores, reduced serum CK up to 1 year, and improved MRI fat fraction/qT2 in 3 patients vs natural history cohort. Also notes serious safety concerns seen in the broader high-dose micro-dystrophin field, including myocarditis and death with another construct (PF-06939926), raising caution about vector dose/transgene-specific effects (roberts2023therapeuticapproachesfor pages 12-15) | Human DMD gene therapy trials and comparative field context | Moderate-high; excellent overview but review-level and partly extrapolates across different micro-dystrophin constructs |
| Boehler et al., 2024, *Skeletal Muscle*, doi:10.1186/s13395-023-00334-y, https://doi.org/10.1186/s13395-023-00334-y | Biomarker study (animal + human translational) | Supports | If micro-dystrophin stabilizes muscle, noninvasive damage biomarkers should track expression and outperform noisy CK | N-terminal titin fragment levels correlated with micro-dystrophin expression across mdx mice, GRMD dogs, and human DMD participants, and were more sensitive than CK to lower levels of expressed micro-dystrophin. Authors propose titin as a pharmacodynamic biomarker to support mechanism-of-action/effect assessment in gene therapy trials (boehler2024nterminaltitinfragment pages 1-2) | Cross-species translational biomarker study linked to micro-dystrophin trials | Moderate-high; strong translational utility, but biomarker correlation does not by itself prove the exact causal edge between membrane repair and clinical benefit |


*Table: This table summarizes key supportive, qualifying, and competing evidence for the canonical dystrophin-loss/membrane-fragility model in Duchenne muscular dystrophy. It emphasizes direct mechanistic tests, interventional validation, recent 2023–2024 advances, and major limitations relevant for knowledge-base curation.*

## Alternative / Competing Mechanistic Models

1. **“Calcium-first” / channelopathy model (competing ordering):** Dystrophy can be initiated or driven primarily by abnormal Ca2+ entry through TRPC/SOCE/TRPV channels, with membrane tears not strictly required for onset in some models (millay2009calciuminfluxis pages 1-2, burr2015geneticevidencein pages 5-6). Relationship to seed hypothesis: **parallel/competing upstream driver** of Ca2+ overload.

2. **SR Ca2+ leak / excitation–contraction coupling defect model (complementary):** SR RyR leak, impaired SERCA function, and abnormal Ca2+ transients may precede or amplify injury, especially in later-stage regenerated muscle (head2010branchedfibresin pages 1-2, lorin2015dystrophiccardiomyopathyrole pages 11-13). Relationship: **parallel source** of Ca2+ dyshomeostasis; may be downstream of dystrophin loss but not necessarily downstream of membrane rupture.

3. **Redox/ROS–mechanotransduction amplification model (complementary):** ROS and redox signaling can potentiate mechanosensitive channel activity (e.g., ROS–Src–TRPC1/caveolin-3 axis described in mechanistic summaries), amplifying Ca2+ entry and damage (burr2015geneticevidencein pages 5-6). Relationship: **amplifier** of the Ca2+ influx node.

4. **Signaling scaffold / domain-specific dystrophin function model (qualifying):** Some clinical features (especially cardiac signaling phenotypes) may require dystrophin domains absent from micro-dystrophin; full-length dystrophin restored cavin 4 localization/signaling in heart where micro-dystrophin did not (zhou2024systemicdeliveryof pages 1-2). Relationship: **qualifies** “partial dystrophin is sufficient” for all tissues/endpoints.

## Knowledge Gaps (explicit, curation-relevant)

1. **Relative causal contribution of membrane microtears vs mechanosensitive/SOCE Ca2+ entry vs SR leak in *human* DMD progression.**
   *Why it matters:* Determines whether best proximal targets are (a) membrane stabilization, (b) channel/SOCE inhibition, or (c) SR Ca2+ handling restoration.
   *What was checked:* Evidence supports contraction-driven rupture (russell2023modulatingfastskeletal pages 1-2), mechanosensitive channel blockade benefit (matsumura2011stretchactivatedcalciumchannel pages 1-2), Ca2+-entry sufficiency without permeability (millay2009calciuminfluxis pages 1-2), and SR/branched-fiber stage effects (head2010branchedfibresin pages 1-2).
   *What would resolve it:* Longitudinal human muscle imaging + Ca2+-handling biomarkers + membrane-permeability readouts pre/post targeted perturbations (see Discriminating Tests).

2. **Protease identity and necessity in vivo in modern (2023–2024) interventional paradigms.**
   *Why it matters:* The seed chain includes calcium-dependent proteases (e.g., calpains) as a key edge, but newer therapy studies often infer this step.
   *What was checked:* Genetic synthesis implicates calpastatin protection (burr2015geneticevidencein pages 5-6); recent mechanical-load and membrane-stabilizer studies demonstrate upstream rescue but do not quantify calpain activity in the excerpts (russell2023modulatingfastskeletal pages 1-2, hahn2023rapidrestitutionof pages 1-2).
   *What would resolve it:* Direct calpain activity reporters (in vivo biosensors) combined with EDG-5506 / copolymer treatment and Ca2+ entry modulation.

3. **Tissue specificity: diaphragm vs limb vs heart mechanistic dominance.**
   *Why it matters:* DMD mortality is strongly cardiopulmonary; mechanisms and treatment responses may diverge.
   *What was checked:* Streptomycin prevented diaphragm EBD/Ca2+ rises (matsumura2011stretchactivatedcalciumchannel pages 1-2); full-length dystrophin restored a heart-specific signaling phenotype (cavin 4) (zhou2024systemicdeliveryof pages 1-2); cardiac permeability evidence cited (EBD leakage, cTnI) (gandhi2024cardiomyopathyinduchenne pages 2-4).
   *What would resolve it:* Parallel endpoint panels in each tissue, including DGC restoration, mechanosensitive channel expression/activity, SR Ca2+ leak, and fibrosis metrics.

4. **Clinical mechanistic surrogacy: how well do titin fragment and CK reflect membrane stabilization vs other injury mechanisms?**
   *Why it matters:* Biomarkers will be used to validate mechanistic edges and guide trials.
   *What was checked:* Titin fragment correlates with micro-dystrophin and is more sensitive than CK (boehler2024nterminaltitinfragment pages 1-2); CK variability complicates PD inference (boehler2024nterminaltitinfragment pages 1-2).
   *What would resolve it:* Biomarker-to-biopsy-to-imaging triangulation in treated cohorts, including mechanosensitive channel activity and SR Ca2+ biomarkers.

## Discriminating Tests (efficient studies to distinguish models)

1. **Human, longitudinal “mechanism panel” cohort nested within micro-dystrophin therapy**
   *Stratification:* DMD genotype (large deletions overlapping transgene vs not), age/stage, ambulatory vs non-ambulatory.
   *Assays:* Serial plasma/urine titin fragment + CK; cardiac troponin I; qMRI (fat fraction, qT2); optional muscle biopsy at baseline and Week 12 (as in NCT03769116 endpoints) for DGC localization, TRPC/TRPV2/SOCE markers, and SR Ca2+ leak markers.
   *Perturbation:* Compare responders vs non-responders by micro-dystrophin localization and biomarker dynamics.
   *Expected outcome:* If membrane fragility is primary, early normalization of permeability injury markers should precede functional stabilization; if channelopathy dominates, Ca2+-entry signatures should predict outcomes even when membrane permeability markers are modest.

2. **Epistasis in mouse: full-length dystrophin restoration × TRPC/SOCE inhibition**
   *Model:* mdx4cv with full-length dystrophin triple-AAV (zhou2024systemicdeliveryof pages 1-2) crossed or combined with TRPC/SOCE genetic reductions (burr2015geneticevidencein pages 5-6).
   *Endpoints:* Ca2+ influx imaging during eccentric contractions, membrane permeability assays, calpain activity reporters, fibrosis.
   *Expected outcome:* If dystrophin restoration fully normalizes Ca2+ entry, TRPC/SOCE inhibition adds little; if Ca2+ channel mechanisms are partially independent, combined perturbation yields additive benefit.

3. **Stage-specific test of “branched fiber” mechanism vs acute membrane fragility**
   *Model:* Young vs old mdx with quantified branching burden (head2010branchedfibresin pages 1-2).
   *Perturbations:* EDG-5506 (reduces contraction injury) vs membrane sealant vs SR Ca2+ handling enhancer (burr2015geneticevidencein pages 5-6).
   *Expected outcome:* Greater benefit of SR-targeting in old branched muscles would support a stage shift from membrane fragility dominance to SR/architecture dominance.

## Curation Leads (candidate KB updates; curator verification required)

### Candidate evidence references (with snippets to verify)

1. **Contraction as causal trigger / mechanical injury:** Russell et al. report that contraction of intact mdx muscle causes sarcolemmal rupture and force loss, especially in eccentric contractions, and that modest (<15%) fast-myosin inhibition protects and reduces fibrosis (https://doi.org/10.1172/jci153837, published **2023-05**) (russell2023modulatingfastskeletal pages 1-2).

2. **Membrane stabilization → rapid functional rescue:** Hahn et al. show copolymer/P188 treatment restores twitch sarcomere shortening (+110% to +220%) and improves Ca2+ transients in mdx fibers (https://doi.org/10.1186/s13395-023-00318-y, published **2023-05**) (hahn2023rapidrestitutionof pages 1-2).

3. **Channelopathy/Ca2+ sufficiency:** Millay et al. report ∼6× TRPC3 overexpression, enhanced SOCE, and dystrophy-like phenotype; TRPC inhibition reduces disease manifestations in mdx and Sgcd deficiency (https://doi.org/10.1073/pnas.0906591106, published **2009-11**) (millay2009calciuminfluxis pages 1-2).

4. **Human interventional validation:** Mendell et al. report NSAA +7 over 4 years, LS mean difference 9.4 vs external control (P=0.0125) after delandistrogene moxeparvovec (https://doi.org/10.1002/mus.27955, published **2024-08**) (mendell2023long‐termsafetyand pages 1-2).

5. **PD biomarker lead:** Boehler et al. propose N-terminal titin fragment as PD biomarker correlated with micro-dystrophin and more sensitive than CK at low expression (https://doi.org/10.1186/s13395-023-00334-y, published **2024-01**) (boehler2024nterminaltitinfragment pages 1-2).

### Candidate KB nodes/edges

* Add/strengthen **mechanosensitive cation channel-mediated Ca2+ entry** (TRPC/TRPV2; SOCE STIM1–ORAI1) as a **parallel edge** from dystrophin/DGC disruption to Ca2+ dyshomeostasis (millay2009calciuminfluxis pages 1-2, matsumura2011stretchactivatedcalciumchannel pages 1-2, burr2015geneticevidencein pages 5-6).
* Add a **stage modifier** node: “regeneration-associated branched fibers” increasing mechanical vulnerability and Ca2+ dysregulation in later disease (head2010branchedfibresin pages 1-2).
* Add **SR Ca2+ leak/handling dysfunction** as a parallel upstream contributor to Ca2+ overload that can be dominant in specific contexts (head2010branchedfibresin pages 1-2, lorin2015dystrophiccardiomyopathyrole pages 11-13).
* Add **micro-dystrophin domain limitation** edge for heart signaling (cavin 4 localization/signaling) (zhou2024systemicdeliveryof pages 1-2).
* Add **titin fragment (N-terminal)** as a pharmacodynamic biomarker node linked to micro-dystrophin expression and muscle injury, with stronger sensitivity than CK at low expression (boehler2024nterminaltitinfragment pages 1-2).

### Candidate ontology terms (suggestions)

* Cell types: skeletal muscle fiber (myofiber), cardiomyocyte, satellite cell.
* Processes: sarcolemma organization/stability, mechanosensitive ion channel activity, calcium ion transmembrane transport, store-operated calcium entry, calpain-mediated proteolysis, necrotic cell death, fibrosis, muscle regeneration.
* Biomarkers: creatine kinase, cardiac troponin I, titin fragment.

---

## Notes on Coverage

This report prioritized 2023–2024 sources where available for interventional validation (EDG-5506, membrane polymers, full-length dystrophin delivery, human gene therapy follow-up, titin biomarker), and used seminal mechanistic papers for channelopathy/Ca2+ sufficiency and stage-dependent Ca2+ handling as needed to test causal edges. Some mechanistic steps (e.g., precise calpain substrates in vivo in humans; quantitative membrane tear frequency in treated vs untreated human muscle) remain under-characterized in the retrieved excerpts and are listed as knowledge gaps.

References

1. (russell2023modulatingfastskeletal pages 1-2): Alan J. Russell, Mike DuVall, Ben Barthel, Ying Qian, Angela K. Peter, Breanne L. Newell-Stamper, Kevin Hunt, Sarah Lehman, Molly Madden, Stephen Schlachter, Ben Robertson, Ashleigh Van Deusen, Hector M. Rodriguez, Carlos Vera, Yu Su, Dennis R. Claflin, Susan V. Brooks, Peter Nghiem, Alexis Rutledge, Twlya I. Juehne, Jinsheng Yu, Elisabeth R. Barton, Yangyi E. Luo, Andreas Patsalos, Laszlo Nagy, H. Lee Sweeney, Leslie A. Leinwand, and Kevin Koch. Modulating fast skeletal muscle contraction protects skeletal muscle in animal models of duchenne muscular dystrophy. Journal of Clinical Investigation, May 2023. URL: https://doi.org/10.1172/jci153837, doi:10.1172/jci153837. This article has 39 citations and is from a highest quality peer-reviewed journal.

2. (hahn2023rapidrestitutionof pages 1-2): Dongwoo Hahn, Joseph D. Quick, Brian R. Thompson, Adelyn Crabtree, Benjamin J. Hackel, Frank S. Bates, and Joseph M. Metzger. Rapid restitution of contractile dysfunction by synthetic copolymers in dystrophin-deficient single live skeletal muscle fibers. Skeletal Muscle, May 2023. URL: https://doi.org/10.1186/s13395-023-00318-y, doi:10.1186/s13395-023-00318-y. This article has 3 citations and is from a peer-reviewed journal.

3. (zhou2024systemicdeliveryof pages 1-2): Yuan Zhou, Chen Zhang, Weidong Xiao, Roland W. Herzog, and Renzhi Han. Systemic delivery of full-length dystrophin in duchenne muscular dystrophy mice. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-50569-6, doi:10.1038/s41467-024-50569-6. This article has 42 citations and is from a highest quality peer-reviewed journal.

4. (dambrosio2023evolvingtherapeuticoptions pages 8-9): Eleonora S. D'Ambrosio and Jerry R. Mendell. Evolving therapeutic options for the treatment of duchenne muscular dystrophy. Neurotherapeutics, 20:1669-1681, Oct 2023. URL: https://doi.org/10.1007/s13311-023-01423-y, doi:10.1007/s13311-023-01423-y. This article has 44 citations and is from a peer-reviewed journal.

5. (mendell2023long‐termsafetyand pages 1-2): Jerry R. Mendell, Zarife Sahenk, Kelly J. Lehman, Linda P. Lowes, Natalie F. Reash, Megan A. Iammarino, Lindsay N. Alfano, Sarah Lewis, Kathleen Church, Richard Shell, Rachael A. Potter, Danielle A. Griffin, Mark Hogan, Shufang Wang, Stefanie Mason, Eddie Darton, and Louise R. Rodino‐Klapac. Long‐term safety and functional outcomes of delandistrogene moxeparvovec gene therapy in patients with duchenne muscular dystrophy: a phase 1/2a nonrandomized trial. Muscle & Nerve, 69:93-98, Aug 2024. URL: https://doi.org/10.1002/mus.27955, doi:10.1002/mus.27955. This article has 84 citations and is from a peer-reviewed journal.

6. (millay2009calciuminfluxis pages 1-2): Douglas P. Millay, Sanjeewa A. Goonasekera, Michelle A. Sargent, Marjorie Maillet, Bruce J. Aronow, and Jeffery D. Molkentin. Calcium influx is sufficient to induce muscular dystrophy through a trpc-dependent mechanism. Proceedings of the National Academy of Sciences, 106:19023-19028, Nov 2009. URL: https://doi.org/10.1073/pnas.0906591106, doi:10.1073/pnas.0906591106. This article has 273 citations and is from a highest quality peer-reviewed journal.

7. (burr2015geneticevidencein pages 5-6): Adam R. Burr and Jeffery D. Molkentin. Genetic evidence in the mouse solidifies the calcium hypothesis of myofiber death in muscular dystrophy. Cell Death and Differentiation, 22:1402-1412, Jun 2015. URL: https://doi.org/10.1038/cdd.2015.65, doi:10.1038/cdd.2015.65. This article has 135 citations and is from a domain leading peer-reviewed journal.

8. (head2010branchedfibresin pages 1-2): Stewart I. Head. Branched fibres in old dystrophic mdx muscle are associated with mechanical weakening of the sarcolemma, abnormal ca2+ transients and a breakdown of ca2+ homeostasis during fatigue. Experimental Physiology, 95:641-656, May 2010. URL: https://doi.org/10.1113/expphysiol.2009.052019, doi:10.1113/expphysiol.2009.052019. This article has 114 citations and is from a peer-reviewed journal.

9. (lorin2015dystrophiccardiomyopathyrole pages 11-13): Charlotte Lorin, Isabelle Vögeli, and Ernst Niggli. Dystrophic cardiomyopathy: role of trpv2 channels in stretch-induced cell damage. Cardiovascular research, 106 1:153-62, Apr 2015. URL: https://doi.org/10.1093/cvr/cvv021, doi:10.1093/cvr/cvv021. This article has 73 citations and is from a domain leading peer-reviewed journal.

10. (matsumura2011stretchactivatedcalciumchannel pages 1-2): Cíntia Yuri Matsumura, Ana Paula Tiemi Taniguti, Adriana Pertille, Humberto Santo Neto, and Maria Julia Marques. Stretch-activated calcium channel protein trpc1 is correlated with the different degrees of the dystrophic phenotype in mdx mice. American journal of physiology. Cell physiology, 301 6:C1344-50, Dec 2011. URL: https://doi.org/10.1152/ajpcell.00056.2011, doi:10.1152/ajpcell.00056.2011. This article has 62 citations.

11. (roberts2023therapeuticapproachesfor pages 12-15): Thomas C. Roberts, Matthew J. A. Wood, and Kay E. Davies. Therapeutic approaches for duchenne muscular dystrophy. Nature Reviews Drug Discovery, 22:917-934, Aug 2023. URL: https://doi.org/10.1038/s41573-023-00775-6, doi:10.1038/s41573-023-00775-6. This article has 135 citations and is from a highest quality peer-reviewed journal.

12. (gandhi2024cardiomyopathyinduchenne pages 2-4): Shivam Gandhi, H. Lee Sweeney, Cora C. Hart, Renzhi Han, and Christopher G. R. Perry. Cardiomyopathy in duchenne muscular dystrophy and the potential for mitochondrial therapeutics to improve treatment response. Cells, 13:1168, Jul 2024. URL: https://doi.org/10.3390/cells13141168, doi:10.3390/cells13141168. This article has 24 citations.

13. (boehler2024nterminaltitinfragment pages 1-2): Jessica F. Boehler, Kristy J. Brown, Valeria Ricotti, and Carl A. Morris. N-terminal titin fragment: a non-invasive, pharmacodynamic biomarker for microdystrophin efficacy. Skeletal Muscle, Jan 2024. URL: https://doi.org/10.1186/s13395-023-00334-y, doi:10.1186/s13395-023-00334-y. This article has 10 citations and is from a peer-reviewed journal.

14. (NCT03769116 chunk 1):  A Randomized, Double-blind, Placebo-controlled Study of Delandistrogene Moxeparvovec (SRP-9001) for Duchenne Muscular Dystrophy (DMD). Sarepta Therapeutics, Inc.. 2018. ClinicalTrials.gov Identifier: NCT03769116

15. (gandhi2024mitochondriainduchenne pages 3-5): Shivam Gandhi, H. Lee Sweeney, Cora Coker Hart, Renzhi Han, and Christopher G.R Perry. Mitochondria in duchenne muscular dystrophy-induced cardiomyopathy: a prospective therapeutic target to improve treatment response. Unknown journal, Jan 2024. URL: https://doi.org/10.20944/preprints202401.2158.v1, doi:10.20944/preprints202401.2158.v1.

16. (mendell2023long‐termsafetyand pages 2-3): Jerry R. Mendell, Zarife Sahenk, Kelly J. Lehman, Linda P. Lowes, Natalie F. Reash, Megan A. Iammarino, Lindsay N. Alfano, Sarah Lewis, Kathleen Church, Richard Shell, Rachael A. Potter, Danielle A. Griffin, Mark Hogan, Shufang Wang, Stefanie Mason, Eddie Darton, and Louise R. Rodino‐Klapac. Long‐term safety and functional outcomes of delandistrogene moxeparvovec gene therapy in patients with duchenne muscular dystrophy: a phase 1/2a nonrandomized trial. Muscle & Nerve, 69:93-98, Aug 2024. URL: https://doi.org/10.1002/mus.27955, doi:10.1002/mus.27955. This article has 84 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](falcon_artifacts/artifact-00.md)
