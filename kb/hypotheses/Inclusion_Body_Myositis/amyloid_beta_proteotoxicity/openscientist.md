---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-02T19:33:24.555390'
end_time: '2026-08-02T19:47:47.016429'
duration_seconds: 862.46
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: Inclusion Body Myositis
  category: Autoimmune
  hypothesis_group_id: amyloid_beta_proteotoxicity
  hypothesis_label: Amyloid-beta and its precursor APP are abnormally and specifically
    over-produced in IBM myofibres and are the upstream proteotoxic driver of the
    disease
  hypothesis_status: DEPRECATED
  hypothesis_yaml: "hypothesis_group_id: amyloid_beta_proteotoxicity\nhypothesis_label:\
    \ Amyloid-beta and its precursor APP are abnormally and specifically over-produced\
    \ in\n  IBM myofibres and are the upstream proteotoxic driver of the disease\n\
    status: DEPRECATED\ndescription: |-\n  Proposed by Askanas and Engel from the\
    \ early 1990s, this model cast sporadic IBM as a muscle analogue of Alzheimer\
    \ disease: increased APP transcription in vacuolated fibres leads to intracellular\
    \ accumulation of APP and its proteolytic fragment amyloid-beta, preferentially\
    \ the more aggregation-prone Abeta42, whose soluble oligomers are cytotoxic and\
    \ sit upstream of tau phosphorylation, oxidative stress, proteasome inhibition,\
    \ ER stress and vacuolar degeneration. It was the dominant degenerative account\
    \ of IBM for roughly two decades and supplied the rationale for the Congo red\
    \ / amyloid criterion in older diagnostic schemes.\n  It is recorded here as DEPRECATED,\
    \ and the two claims embedded in the label fail for different reasons.\n  The\
    \ claim of SPECIFICITY fails outright: beta-amyloid-immunoreactive, Congo-red-positive\
    \ rimmed vacuoles with tubulofilaments occur in long-standing denervation (postpoliomyelitis\
    \ muscular atrophy), in oculopharyngeal muscular dystrophy, and in congenital\
    \ myopathies of childhood, so the finding tracks chronicity of fibre injury rather\
    \ than IBM itself. Comparative quantification puts the point sharply: in the same\
    \ biopsies in which sarcoplasmic TDP-43 marked 23% of myofibres, focal beta-amyloid\
    \ immunoreactivity (R1282) was found in 0.00% and fluorescent Congo red material\
    \ in 0.57%. TDP-43 mislocalization, not amyloid, is now the sensitive and specific\
    \ molecular marker of IBM.\n  The claim of ABNORMAL PRESENCE is weaker than the\
    \ literature suggests rather than plainly false. Positive immunoblot and ADDL\
    \ data exist, but almost entirely from the originating laboratory; unbiased laser-capture\
    \ mass spectrometry of rimmed vacuoles recovered 213 enriched proteins dominated\
    \ by protein-folding and autophagy machinery without reporting amyloid-beta or\
    \ APP enrichment; cultured IBM myotubes from the same laboratory do not accumulate\
    \ betaAPP, so any accumulation is not cell-autonomous; the companion phospho-tau\
    \ claim was shown to rest on antibodies that stain normal myonuclei and recognize\
    \ proteins other than tau, which impugns the reagent class the histological arm\
    \ depended on; and a formal citation-network analysis of the entire literature\
    \ on this belief found its authority inflated by citation bias, amplification\
    \ and invention rather than by accumulated data.\n  What survives is modest and\
    \ is retained in the entry: protein aggregates of several kinds, amyloid-beta\
    \ among them, are demonstrable in a small minority of IBM myofibres and are best\
    \ read as a marker of overwhelmed proteostasis (see the `Autophagy-Lysosome Failure\
    \ and Rimmed Vacuole Formation` node) rather than as a specific or upstream cause.\
    \ Neither of the two live models for IBM requires amyloid-beta, and no anti-amyloid\
    \ therapeutic strategy has been taken into IBM trials.\nevidence:\n- reference:\
    \ PMID:8394158\n  reference_title: beta-Amyloid precursor protein mRNA is increased\
    \ in inclusion-body myositis muscle.\n  supports: SUPPORT\n  evidence_source:\
    \ HUMAN_CLINICAL\n  snippet: Vacuolated muscle fibers in muscle biopsies of 8\
    \ out of 8 inclusion body myositis (IBM) patients,\n    including 2 hereditary\
    \ patients, manifested increased mRNA for the beta-amyloid precursor protein\n\
    \    (beta APP) that contains Kunitz-type protease inhibitor motif.\n  explanation:\
    \ 'The founding observation of the hypothesis: increased APP transcript in vacuolated\
    \ IBM\n    fibres, offered as evidence that APP accumulation is generated locally\
    \ rather than deposited.'\n- reference: PMID:16432144\n  reference_title: 'Inclusion-body\
    \ myositis: a myodegenerative conformational disorder associated with\n    Abeta,\
    \ protein misfolding, and proteasome inhibition.'\n  supports: SUPPORT\n  evidence_source:\
    \ HUMAN_CLINICAL\n  snippet: In s-IBM, abnormal accumulation of the amyloid-beta\
    \ (Abeta) precursor protein and its proteolytic\n    fragment, Abeta, associated\
    \ with the aging intracellular milieu of the muscle fiber, appear to be\n    key\
    \ upstream pathogenic events.\n  explanation: The canonical statement of the hypothesis\
    \ by its originators, asserting APP/Abeta accumulation\n    as the key upstream\
    \ pathogenic event.\n- reference: PMID:20711838\n  reference_title: Novel demonstration\
    \ of amyloid-\u03B2 oligomers in sporadic inclusion-body myositis muscle\n   \
    \ fibers.\n  supports: SUPPORT\n  evidence_source: HUMAN_CLINICAL\n  snippet:\
    \ We now report for the first time that in s-IBM muscle biopsies A\u03B2-dimer,\
    \ -trimer, and -tetramer\n    are identifiable by immunoblots. While all the s-IBM\
    \ samples we studied had A\u03B2-oligomers, their molecular\n    weights and intensity\
    \ varied between the patient samples. None of the control muscle biopsies had\n\
    \    A\u03B2 oligomers.\n  explanation: The strongest biochemical evidence offered\
    \ for the hypothesis, and the closest thing to\n    a direct test of abnormal\
    \ presence; it reports oligomers in every IBM sample and none in controls,\n \
    \   but comes from the originating laboratory and has not been widely replicated\
    \ independently.\n- reference: PMID:19533646\n  reference_title: Sarcoplasmic\
    \ redistribution of nuclear TDP-43 in inclusion body myositis.\n  supports: REFUTE\n\
    \  evidence_source: HUMAN_CLINICAL\n  snippet: we found TDP-43 sarcoplasmic immunoreactivity\
    \ in 23% of IBM myofibers, while other reported\n    IBM biomarkers were less\
    \ frequent, with rimmed vacuoles in 2.8%, fluorescent Congo red material in\n\
    \    0.57%, SMI-31 immunoreactivity in 0.83%, and focal R1282 beta-amyloid immunoreactivity\
    \ in 0.00% of\n    myofibers.\n  explanation: 'Head-to-head quantification in\
    \ the same biopsies: beta-amyloid immunoreactivity was detected\n    in no myofibres\
    \ at all, while TDP-43 mislocalization marked 23%. Directly refutes amyloid-beta\
    \ as\n    the characteristic or specific molecular lesion of IBM.'\n- reference:\
    \ PMID:9781653\n  reference_title: 'Rimmed vacuoles with beta-amyloid and ubiquitinated\
    \ filamentous deposits in the muscles\n    of patients with long-standing denervation\
    \ (postpoliomyelitis muscular atrophy): similarities with\n    inclusion body\
    \ myositis.'\n  supports: REFUTE\n  evidence_source: HUMAN_CLINICAL\n  snippet:\
    \ We conclude that vacuolated muscle fibers containing filamentous inclusions\
    \ positive for amyloid\n    and ubiquitin are not unique to IBM and the other\
    \ vacuolar myopathies but can also occur in a chronic\n    neurogenic condition,\
    \ such as postpoliomyelitis.\n  explanation: 'Refutes the specificity claim directly:\
    \ identical amyloid-positive ubiquitinated filamentous\n    vacuoles arise in\
    \ chronic denervation, so the finding tracks chronicity of fibre injury rather\
    \ than\n    IBM.'\n- reference: PMID:16788822\n  reference_title: Rimmed vacuoles\
    \ with beta-amyloid and tau protein deposits in the muscle of children\n    with\
    \ hereditary myopathy.\n  supports: REFUTE\n  evidence_source: HUMAN_CLINICAL\n\
    \  snippet: Our studies demonstrate for the first time that the full morphological\
    \ phenotype of IBM including\n    beta-amyloid and tau protein deposits may also\
    \ develop in children, and that congenital, probably\n    genetic, muscle defects\
    \ may lead to abnormal protein aggregation in IBM-like inclusions.\n  explanation:\
    \ 'Further refutes specificity, and removes ageing as a necessary condition: the\
    \ complete\n    beta-amyloid-plus-tau morphology occurs in congenital myopathy\
    \ in children.'\n- reference: PMID:8268725\n  reference_title: 'Ubiquitin and\
    \ beta-amyloid-protein in inclusion body myositis (IBM), familial IBM-like\n \
    \   disorder and oculopharyngeal muscular dystrophy: an immunocytochemical study.'\n\
    \  supports: PARTIAL\n  evidence_source: HUMAN_CLINICAL\n  snippet: Labelling\
    \ with anti-beta-amyloid-protein antibody was seen in a few fibres in IBM but\
    \ not in\n    the other two conditions. The structures labelled with this antibody\
    \ have yet to be determined.\n  explanation: 'Mixed: beta-amyloid labelling did\
    \ discriminate IBM from OPMD and familial IBM-like disorder\n    in this series,\
    \ but only in a few fibres, and the authors explicitly decline to say what structure\n\
    \    the antibody bound.'\n- reference: PMID:10599804\n  reference_title: Cultured\
    \ inclusion-body myositis muscle fibers do not accumulate beta-amyloid precursor\n\
    \    protein and can be innervated.\n  supports: REFUTE\n  evidence_source: IN_VITRO\n\
    \  snippet: Cultured muscle fibers from patients with sporadic inclusion-body\
    \ myositis (s-IBM), similar\n    to normal control muscle fibers, 1) did not have\
    \ beta-amyloid precursor protein (betaAPP) immunoreactivity\n  explanation: 'From\
    \ the originating laboratory: IBM myotubes in culture do not accumulate betaAPP,\
    \ so\n    the accumulation is not a cell-autonomous property of the IBM myofibre\
    \ and cannot be a primary intrinsic\n    lesion.'\n- reference: PMID:19626672\n\
    \  reference_title: Nature of \"Tau\" immunoreactivity in normal myonuclei and\
    \ inclusion body myositis.\n  supports: REFUTE\n  evidence_source: HUMAN_CLINICAL\n\
    \  snippet: Antibodies previously reported to indicate abnormal accumulation of\
    \ phosphorylated-tau in IBM\n    myofibers react to normal myonuclei and recognize\
    \ proteins other than tau.\n  explanation: Refutes the companion phospho-tau limb\
    \ of the Alzheimer-analogy model and demonstrates\n    that the immunohistochemical\
    \ reagent class on which the histological arm of the hypothesis rested\n    can\
    \ report protein accumulation that is not there.\n- reference: PMID:28009083\n\
    \  reference_title: Proteomics of rimmed vacuoles define new risk allele in inclusion\
    \ body myositis.\n  supports: PARTIAL\n  evidence_source: HUMAN_CLINICAL\n  snippet:\
    \ Proteins associated with protein folding and autophagy were the largest group\
    \ represented.\n  explanation: Unbiased laser-capture mass spectrometry of the\
    \ rimmed vacuole itself returns a proteostasis-machinery\n    signature; the paper\
    \ reports 213 enriched proteins and does not report amyloid-beta or APP among\
    \ them,\n    which is what the hypothesis would predict to dominate.\n- reference:\
    \ PMID:19622839\n  reference_title: 'How citation distortions create unfounded\
    \ authority: analysis of a citation network.'\n  supports: REFUTE\n  evidence_source:\
    \ OTHER\n  snippet: Unfounded authority was established by citation bias against\
    \ papers that refuted or weakened\n    the belief; amplification, the marked expansion\
    \ of the belief system by papers presenting no data\n    addressing it; and forms\
    \ of invention such as the conversion of hypothesis into fact through citation\n\
    \    alone.\n  explanation: A formal citation-network analysis whose subject was\
    \ precisely this belief about beta-amyloid\n    in IBM. It does not measure muscle,\
    \ but it explains why the apparent weight of literature behind the\n    hypothesis\
    \ overstates the underlying data, and is the reason this hypothesis is curated\
    \ as DEPRECATED\n    rather than merely ALTERNATIVE.\nnotes: Retained rather than\
    \ deleted because the hypothesis remains widely cited in reviews, textbooks\n\
    \  and older diagnostic criteria, and curators encountering amyloid claims in\
    \ the IBM literature need the\n  assessment recorded rather than silently absent."
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
citation_count: 27
artifact_count: 4
artifact_sources:
  openscientist_artifacts_zip: 4
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
- filename: provenance_ibm_amyloid_mechanistic_diagram.json
  path: openscientist_artifacts/provenance_ibm_amyloid_mechanistic_diagram.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist ibm amyloid mechanistic diagram
- filename: provenance_ibm_amyloid_mechanistic_diagram.png
  path: openscientist_artifacts/provenance_ibm_amyloid_mechanistic_diagram.png
  media_type: image/png
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist ibm amyloid mechanistic diagram
---

## Question

# Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Inclusion Body Myositis
- **Category:** Autoimmune

## Target Hypothesis
- **Hypothesis ID:** amyloid_beta_proteotoxicity
- **Hypothesis Label:** Amyloid-beta and its precursor APP are abnormally and specifically over-produced in IBM myofibres and are the upstream proteotoxic driver of the disease
- **Status in KB:** DEPRECATED

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: amyloid_beta_proteotoxicity
hypothesis_label: Amyloid-beta and its precursor APP are abnormally and specifically over-produced in
  IBM myofibres and are the upstream proteotoxic driver of the disease
status: DEPRECATED
description: |-
  Proposed by Askanas and Engel from the early 1990s, this model cast sporadic IBM as a muscle analogue of Alzheimer disease: increased APP transcription in vacuolated fibres leads to intracellular accumulation of APP and its proteolytic fragment amyloid-beta, preferentially the more aggregation-prone Abeta42, whose soluble oligomers are cytotoxic and sit upstream of tau phosphorylation, oxidative stress, proteasome inhibition, ER stress and vacuolar degeneration. It was the dominant degenerative account of IBM for roughly two decades and supplied the rationale for the Congo red / amyloid criterion in older diagnostic schemes.
  It is recorded here as DEPRECATED, and the two claims embedded in the label fail for different reasons.
  The claim of SPECIFICITY fails outright: beta-amyloid-immunoreactive, Congo-red-positive rimmed vacuoles with tubulofilaments occur in long-standing denervation (postpoliomyelitis muscular atrophy), in oculopharyngeal muscular dystrophy, and in congenital myopathies of childhood, so the finding tracks chronicity of fibre injury rather than IBM itself. Comparative quantification puts the point sharply: in the same biopsies in which sarcoplasmic TDP-43 marked 23% of myofibres, focal beta-amyloid immunoreactivity (R1282) was found in 0.00% and fluorescent Congo red material in 0.57%. TDP-43 mislocalization, not amyloid, is now the sensitive and specific molecular marker of IBM.
  The claim of ABNORMAL PRESENCE is weaker than the literature suggests rather than plainly false. Positive immunoblot and ADDL data exist, but almost entirely from the originating laboratory; unbiased laser-capture mass spectrometry of rimmed vacuoles recovered 213 enriched proteins dominated by protein-folding and autophagy machinery without reporting amyloid-beta or APP enrichment; cultured IBM myotubes from the same laboratory do not accumulate betaAPP, so any accumulation is not cell-autonomous; the companion phospho-tau claim was shown to rest on antibodies that stain normal myonuclei and recognize proteins other than tau, which impugns the reagent class the histological arm depended on; and a formal citation-network analysis of the entire literature on this belief found its authority inflated by citation bias, amplification and invention rather than by accumulated data.
  What survives is modest and is retained in the entry: protein aggregates of several kinds, amyloid-beta among them, are demonstrable in a small minority of IBM myofibres and are best read as a marker of overwhelmed proteostasis (see the `Autophagy-Lysosome Failure and Rimmed Vacuole Formation` node) rather than as a specific or upstream cause. Neither of the two live models for IBM requires amyloid-beta, and no anti-amyloid therapeutic strategy has been taken into IBM trials.
evidence:
- reference: PMID:8394158
  reference_title: beta-Amyloid precursor protein mRNA is increased in inclusion-body myositis muscle.
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: Vacuolated muscle fibers in muscle biopsies of 8 out of 8 inclusion body myositis (IBM) patients,
    including 2 hereditary patients, manifested increased mRNA for the beta-amyloid precursor protein
    (beta APP) that contains Kunitz-type protease inhibitor motif.
  explanation: 'The founding observation of the hypothesis: increased APP transcript in vacuolated IBM
    fibres, offered as evidence that APP accumulation is generated locally rather than deposited.'
- reference: PMID:16432144
  reference_title: 'Inclusion-body myositis: a myodegenerative conformational disorder associated with
    Abeta, protein misfolding, and proteasome inhibition.'
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: In s-IBM, abnormal accumulation of the amyloid-beta (Abeta) precursor protein and its proteolytic
    fragment, Abeta, associated with the aging intracellular milieu of the muscle fiber, appear to be
    key upstream pathogenic events.
  explanation: The canonical statement of the hypothesis by its originators, asserting APP/Abeta accumulation
    as the key upstream pathogenic event.
- reference: PMID:20711838
  reference_title: Novel demonstration of amyloid-β oligomers in sporadic inclusion-body myositis muscle
    fibers.
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: We now report for the first time that in s-IBM muscle biopsies Aβ-dimer, -trimer, and -tetramer
    are identifiable by immunoblots. While all the s-IBM samples we studied had Aβ-oligomers, their molecular
    weights and intensity varied between the patient samples. None of the control muscle biopsies had
    Aβ oligomers.
  explanation: The strongest biochemical evidence offered for the hypothesis, and the closest thing to
    a direct test of abnormal presence; it reports oligomers in every IBM sample and none in controls,
    but comes from the originating laboratory and has not been widely replicated independently.
- reference: PMID:19533646
  reference_title: Sarcoplasmic redistribution of nuclear TDP-43 in inclusion body myositis.
  supports: REFUTE
  evidence_source: HUMAN_CLINICAL
  snippet: we found TDP-43 sarcoplasmic immunoreactivity in 23% of IBM myofibers, while other reported
    IBM biomarkers were less frequent, with rimmed vacuoles in 2.8%, fluorescent Congo red material in
    0.57%, SMI-31 immunoreactivity in 0.83%, and focal R1282 beta-amyloid immunoreactivity in 0.00% of
    myofibers.
  explanation: 'Head-to-head quantification in the same biopsies: beta-amyloid immunoreactivity was detected
    in no myofibres at all, while TDP-43 mislocalization marked 23%. Directly refutes amyloid-beta as
    the characteristic or specific molecular lesion of IBM.'
- reference: PMID:9781653
  reference_title: 'Rimmed vacuoles with beta-amyloid and ubiquitinated filamentous deposits in the muscles
    of patients with long-standing denervation (postpoliomyelitis muscular atrophy): similarities with
    inclusion body myositis.'
  supports: REFUTE
  evidence_source: HUMAN_CLINICAL
  snippet: We conclude that vacuolated muscle fibers containing filamentous inclusions positive for amyloid
    and ubiquitin are not unique to IBM and the other vacuolar myopathies but can also occur in a chronic
    neurogenic condition, such as postpoliomyelitis.
  explanation: 'Refutes the specificity claim directly: identical amyloid-positive ubiquitinated filamentous
    vacuoles arise in chronic denervation, so the finding tracks chronicity of fibre injury rather than
    IBM.'
- reference: PMID:16788822
  reference_title: Rimmed vacuoles with beta-amyloid and tau protein deposits in the muscle of children
    with hereditary myopathy.
  supports: REFUTE
  evidence_source: HUMAN_CLINICAL
  snippet: Our studies demonstrate for the first time that the full morphological phenotype of IBM including
    beta-amyloid and tau protein deposits may also develop in children, and that congenital, probably
    genetic, muscle defects may lead to abnormal protein aggregation in IBM-like inclusions.
  explanation: 'Further refutes specificity, and removes ageing as a necessary condition: the complete
    beta-amyloid-plus-tau morphology occurs in congenital myopathy in children.'
- reference: PMID:8268725
  reference_title: 'Ubiquitin and beta-amyloid-protein in inclusion body myositis (IBM), familial IBM-like
    disorder and oculopharyngeal muscular dystrophy: an immunocytochemical study.'
  supports: PARTIAL
  evidence_source: HUMAN_CLINICAL
  snippet: Labelling with anti-beta-amyloid-protein antibody was seen in a few fibres in IBM but not in
    the other two conditions. The structures labelled with this antibody have yet to be determined.
  explanation: 'Mixed: beta-amyloid labelling did discriminate IBM from OPMD and familial IBM-like disorder
    in this series, but only in a few fibres, and the authors explicitly decline to say what structure
    the antibody bound.'
- reference: PMID:10599804
  reference_title: Cultured inclusion-body myositis muscle fibers do not accumulate beta-amyloid precursor
    protein and can be innervated.
  supports: REFUTE
  evidence_source: IN_VITRO
  snippet: Cultured muscle fibers from patients with sporadic inclusion-body myositis (s-IBM), similar
    to normal control muscle fibers, 1) did not have beta-amyloid precursor protein (betaAPP) immunoreactivity
  explanation: 'From the originating laboratory: IBM myotubes in culture do not accumulate betaAPP, so
    the accumulation is not a cell-autonomous property of the IBM myofibre and cannot be a primary intrinsic
    lesion.'
- reference: PMID:19626672
  reference_title: Nature of "Tau" immunoreactivity in normal myonuclei and inclusion body myositis.
  supports: REFUTE
  evidence_source: HUMAN_CLINICAL
  snippet: Antibodies previously reported to indicate abnormal accumulation of phosphorylated-tau in IBM
    myofibers react to normal myonuclei and recognize proteins other than tau.
  explanation: Refutes the companion phospho-tau limb of the Alzheimer-analogy model and demonstrates
    that the immunohistochemical reagent class on which the histological arm of the hypothesis rested
    can report protein accumulation that is not there.
- reference: PMID:28009083
  reference_title: Proteomics of rimmed vacuoles define new risk allele in inclusion body myositis.
  supports: PARTIAL
  evidence_source: HUMAN_CLINICAL
  snippet: Proteins associated with protein folding and autophagy were the largest group represented.
  explanation: Unbiased laser-capture mass spectrometry of the rimmed vacuole itself returns a proteostasis-machinery
    signature; the paper reports 213 enriched proteins and does not report amyloid-beta or APP among them,
    which is what the hypothesis would predict to dominate.
- reference: PMID:19622839
  reference_title: 'How citation distortions create unfounded authority: analysis of a citation network.'
  supports: REFUTE
  evidence_source: OTHER
  snippet: Unfounded authority was established by citation bias against papers that refuted or weakened
    the belief; amplification, the marked expansion of the belief system by papers presenting no data
    addressing it; and forms of invention such as the conversion of hypothesis into fact through citation
    alone.
  explanation: A formal citation-network analysis whose subject was precisely this belief about beta-amyloid
    in IBM. It does not measure muscle, but it explains why the apparent weight of literature behind the
    hypothesis overstates the underlying data, and is the reason this hypothesis is curated as DEPRECATED
    rather than merely ALTERNATIVE.
notes: Retained rather than deleted because the hypothesis remains widely cited in reviews, textbooks
  and older diagnostic criteria, and curators encountering amyloid claims in the IBM literature need the
  assessment recorded rather than silently absent.
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

# Amyloid-beta Proteotoxicity in Inclusion Body Myositis: A Focused Hypothesis-Search Report

**Disease:** Inclusion Body Myositis (IBM) — Category: Autoimmune
**Hypothesis ID:** `amyloid_beta_proteotoxicity`
**Hypothesis Label:** Amyloid-beta and its precursor APP are abnormally and specifically over-produced in IBM myofibres and are the upstream proteotoxic driver of the disease
**Status in KB:** DEPRECATED

---

## Executive Judgment

**Verdict: REFUTED as stated; correctly curated as DEPRECATED.**

The amyloid-beta proteotoxicity model — Askanas and Engel's proposal that sporadic IBM is a "muscle Alzheimer disease" in which locally over-produced APP and its Aβ fragment drive an intracellular proteotoxic cascade upstream of tau phosphorylation, oxidative stress, proteasome inhibition and vacuolar degeneration — does not survive contact with the current literature. The hypothesis embeds two separable claims, and the search confirms that both fail, for different reasons.

The **specificity claim** fails outright. Head-to-head quantification in the same IBM biopsies detected focal β-amyloid immunoreactivity in **0.00%** of myofibres and Congo-red material in **0.57%**, versus TDP-43 sarcoplasmic mislocalization in **23%** ([PMID: 19533646](https://pubmed.ncbi.nlm.nih.gov/19533646/)). The identical amyloid-positive, ubiquitinated, tubulofilamentous rimmed-vacuole morphology occurs in chronic denervation (postpoliomyelitis muscular atrophy; [PMID: 9781653](https://pubmed.ncbi.nlm.nih.gov/9781653/)), in congenital childhood myopathy — complete with β-amyloid **and** tau ([PMID: 16788822](https://pubmed.ncbi.nlm.nih.gov/16788822/)) — and APP is upregulated in GNE myopathy ([PMID: 23496965](https://pubmed.ncbi.nlm.nih.gov/23496965/)). The finding tracks chronicity of fibre injury, not IBM. A TDP-43-driven cryptic HDGFL2 peptide, by contrast, is present in the great majority of IBM biopsies and essentially absent across 197 disease controls ([PMID: 39757935](https://pubmed.ncbi.nlm.nih.gov/39757935/)), giving IBM a genuinely specific molecular marker that is not amyloid.

The **abnormal-presence / upstream-driver claim** is weakly rather than plainly supported. The strongest biochemical evidence — Aβ oligomers present in every IBM sample and no control ([PMID: 20711838](https://pubmed.ncbi.nlm.nih.gov/20711838/)) — comes almost entirely from the originating laboratory and was not independently replicated in our targeted search. Cultured IBM myotubes do not accumulate βAPP, so any accumulation is not cell-autonomous ([PMID: 10599804](https://pubmed.ncbi.nlm.nih.gov/10599804/)). Unbiased laser-capture proteomics of the rimmed vacuole recovered 213 proteins dominated by protein-folding and autophagy machinery, without reporting amyloid-beta or APP enrichment ([PMID: 28009083](https://pubmed.ncbi.nlm.nih.gov/28009083/)). Inflammatory cytokines (TNF-α, IL-1β) sit **upstream** of amyloid handling, inverting the hypothesis's causal order ([PMID: 23294492](https://pubmed.ncbi.nlm.nih.gov/23294492/), [PMID: 23998706](https://pubmed.ncbi.nlm.nih.gov/23998706/)). The genetic architecture of IBM contains no amyloid-pathway risk gene, and the proteostasis-targeting drug arimoclomol — the therapy nearest to this mechanism — failed a 150-patient RCT ([PMID: 37739573](https://pubmed.ncbi.nlm.nih.gov/37739573/)). No anti-amyloid agent has ever been trialed in IBM.

**Most important caveat:** What survives, and is retained in the KB entry, is modest and true — protein aggregates of several kinds, amyloid-beta among them, are demonstrable in a small minority of IBM myofibres. These are best read as a **marker of overwhelmed proteostasis**, downstream, not as a specific or upstream cause. Model-organism data show that forced Aβ/APP overexpression *can* cause muscle pathology in principle, which is why the hypothesis is "deprecated" rather than "nonsense": the mechanism is biologically possible but is not what drives human IBM.

---

## Key Findings

### Finding 1 — Amyloid-beta/APP accumulation is not specific to IBM

Convergent human-tissue evidence refutes the specificity claim across four independent lines. First, direct comparative quantification: in the same IBM biopsies, focal R1282 β-amyloid immunoreactivity was seen in **0.00%** of myofibres and fluorescent Congo-red material in **0.57%**, against TDP-43 sarcoplasmic mislocalization in **23%**, rimmed vacuoles in 2.8%, and SMI-31 in 0.83% ([PMID: 19533646](https://pubmed.ncbi.nlm.nih.gov/19533646/)). If amyloid were the characteristic molecular lesion of IBM, it should not be undetectable in fibres where a competing marker labels nearly a quarter of the tissue.

Second, the amyloid-positive rimmed-vacuole morphology is not unique to IBM. Vacuolated fibres with filamentous inclusions positive for amyloid and ubiquitin occur in **postpoliomyelitis muscular atrophy**, a chronic *neurogenic* condition ([PMID: 9781653](https://pubmed.ncbi.nlm.nih.gov/9781653/)). Third, the *complete* IBM morphological phenotype — β-amyloid **and** tau deposits — develops in **children** with congenital hereditary myopathy ([PMID: 16788822](https://pubmed.ncbi.nlm.nih.gov/16788822/)), which simultaneously refutes specificity and removes ageing as a necessary condition. Fourth, in GNE myopathy, APP mRNA is elevated (non-significantly) and APP co-localizes with cell-stress markers (αB-crystallin, iNOS, NCAM, IL-1β), pointing to a generic stress response rather than an IBM-specific lesion ([PMID: 23496965](https://pubmed.ncbi.nlm.nih.gov/23496965/)).

Finally, the positive counter-example: a TDP-43-dependent cryptic **HDGFL2** peptide arising from loss of TDP-43 splicing repression was positive in roughly two-thirds of IBM biopsies and **absent in 197/197 disease controls** except 2 vacuolar myopathies ([PMID: 39757935](https://pubmed.ncbi.nlm.nih.gov/39757935/)). This demonstrates that a genuinely IBM-specific molecular marker exists — and it is not amyloid.

### Finding 2 — Forced APP/Aβ overexpression causes muscle pathology in models, but does not prove APP drives human IBM

Model-organism evidence provides *qualified, non-clinical* support for the general principle of Aβ proteotoxicity, while also undercutting the specific causal ordering of the seed hypothesis. MCK-βAPP transgenic mice, engineered to accumulate intramyofibre β-amyloid, develop mitochondrial structural and functional damage, reduced TCA-cycle activity, a switch to anaerobic metabolism, increased ROS and plasmalemmal depolarization as early as 2–3 months — *before* overt histopathology ([PMID: 22518836](https://pubmed.ncbi.nlm.nih.gov/22518836/)). This shows Aβ accumulation *can* be upstream of mitochondrial injury in a controlled system.

However, two observations dissociate the model from the human disease. In Drosophila expressing wild-type human APP in muscle, age- and activity-dependent weakness developed (rescued by Parkin) **without any protein aggregates or structural abnormalities** ([PMID: 21518451](https://pubmed.ncbi.nlm.nih.gov/21518451/)) — decoupling toxicity from deposition, and implying that amyloid *deposits* (the histological criterion) are not the toxic species even where APP is pathogenic. More decisively for causal ordering, inflammatory cytokines drive amyloid handling rather than the reverse: **TNF-α** upregulates macroautophagic processing of APP/β-amyloid in human muscle cells ([PMID: 23294492](https://pubmed.ncbi.nlm.nih.gov/23294492/)), and **IL-1β**, which is upregulated in sIBM myofibres, co-localizes with APP and *promotes* APP/amyloid production ([PMID: 23998706](https://pubmed.ncbi.nlm.nih.gov/23998706/)). This places inflammation upstream of APP/amyloid, inverting the seed hypothesis.

### Finding 3 — A cytotoxic-autoimmune model is the leading competing mechanism and is better supported clinically

The dominant competing hypothesis frames IBM as a late-onset, treatment-refractory **autoimmune** disease. Microarray analysis of 411 muscle samples (40 IBM) identified a T-cell cytotoxicity signature featuring highly differentiated/terminally differentiated **KLRG1+ CD8 effector T cells** invading myofibres; these cells are non-proliferative (Ki67-low) and enriched in IBM blood ([PMID: 31326977](https://pubmed.ncbi.nlm.nih.gov/31326977/)). IBM is associated with a blood autoantibody, **anti-cN1A/NT5C1A** (combined IgG/IgM/IgA sensitivity ~76%, specificity ~94–96%; [PMID: 24752512](https://pubmed.ncbi.nlm.nih.gov/24752512/)) and an HLA autoimmune haplotype. Functionally, anti-cN1A-positive IBM serum applied to human myotubes upregulated adaptive immune-response genes (1126 DEGs; [PMID: 41283441](https://pubmed.ncbi.nlm.nih.gov/41283441/)).

A parallel intrinsic-degeneration axis — independent of amyloid — involves clonally expanded **mtDNA deletions** and COX-deficient fibres exceeding age-matched controls ([PMID: 7602331](https://pubmed.ncbi.nlm.nih.gov/7602331/)); deep sequencing found a mean heteroplasmy of 10% (range 1–35%) in IBM versus 1% in controls ([PMID: 33354847](https://pubmed.ncbi.nlm.nih.gov/33354847/)). These two axes (cytotoxic autoimmunity + mitochondrial degeneration) explain IBM's clinical and pathological features more parsimoniously than amyloid, and neither requires Aβ.

### Finding 4 — No proteostasis- or amyloid-directed therapy has shown efficacy; no anti-amyloid agent has been trialed

Therapeutic evidence supplies an indirect but decisive test. **Arimoclomol**, an oral heat-shock-response co-inducer that reduced sIBM pathological markers in vitro and improved mutant-VCP inclusion-body myopathy mice ([PMID: 27009270](https://pubmed.ncbi.nlm.nih.gov/27009270/)), was taken into a multicentre randomised double-blind placebo-controlled trial (n=150, 20 months; NCT02753530) and did **not** show statistically significant efficacy on the IBMFRS or qMRI thigh measures ([PMID: 37739573](https://pubmed.ncbi.nlm.nih.gov/37739573/), [PMID: 40018748](https://pubmed.ncbi.nlm.nih.gov/40018748/)). A 2025 systematic review of 14 IBM RCTs concluded that **all** interventions — immunosuppressive, immunomodulatory, muscle-growth (bimagrumab), and protein-homeostasis (arimoclomol, sirolimus) — provide low-to-high-quality evidence of **no effect** on disease progression ([PMID: 39843353](https://pubmed.ncbi.nlm.nih.gov/39843353/)). Critically, **no anti-amyloid strategy** (BACE/γ-secretase inhibitor, anti-Aβ antibody) appears among trialed agents — the amyloid model has never been tested therapeutically in IBM despite three decades of prominence.

### Finding 5 — IBM genetic architecture supports autoimmunity and proteostasis/autophagy, not amyloid processing

Genetic and GWAS evidence provides an orthogonal test. The only genome-wide-significant IBM association is the **HLA class II region**, with **HLA-DRB1\*03:01** the top allele and risk attributable to amino acids in the peptide-binding pocket ([PMID: 29611059](https://pubmed.ncbi.nlm.nih.gov/29611059/)); an Immunochip study (252 IBM within 2566 IIM) found HLA and **PTPN22** reaching p<5×10⁻⁸ ([PMID: 26362759](https://pubmed.ncbi.nlm.nih.gov/26362759/)). Candidate/exome sequencing implicates protein-homeostasis and rimmed-vacuole genes — **VCP, SQSTM1, FYCO1** — i.e. autophagy/proteostasis machinery ([PMID: 29611059](https://pubmed.ncbi.nlm.nih.gov/29611059/)). **No amyloid-processing gene (APP, PSEN1/2, BACE1, APOE) is reported as an IBM susceptibility locus.** A separate targeted search for independent (non-originating-lab) replication of the Aβ-oligomer/Aβ42 immunohistochemistry returned no papers, confirming the abnormal-presence data remain single-lab.

---

## Mechanistic Model / Interpretation

### Causal chain implied by the seed hypothesis

```
[Ageing myofibre milieu]
        │
        ▼
[↑ APP transcription in vacuolated fibres]         ← PMID:8394158 (support, single observation)
        │
        ▼
[Intracellular APP + Aβ accumulation, esp. Aβ42]   ← PMID:16432144, 20711838 (single-lab)
        │
        ▼
[Cytotoxic soluble Aβ oligomers]
        │
        ▼
[Tau phosphorylation → oxidative stress → proteasome inhibition → ER stress]
        │
        ▼
[Vacuolar degeneration → muscle weakness / IBM]
```

### Where the literature is strong, inferred, or broken

| Causal link | Status | Evidence |
|---|---|---|
| ↑ APP mRNA in vacuolated fibres | **Weak / single observation** | PMID:8394158 (support); non-specific — also GNE myopathy (PMID:23496965) |
| Aβ accumulation specific to IBM | **BROKEN (refuted)** | 0.00% β-amyloid vs 23% TDP-43 (PMID:19533646); also denervation & congenital myopathy (PMID:9781653, 16788822) |
| Aβ accumulation is cell-autonomous | **BROKEN (refuted)** | Cultured IBM myotubes do not accumulate βAPP (PMID:10599804) |
| Aβ oligomers present & IBM-restricted | **Unreplicated (single-lab)** | PMID:20711838; no independent replication found |
| Aβ upstream of tau pathology | **BROKEN** | "p-tau" antibodies stain normal myonuclei / non-tau proteins (PMID:19626672, from seed) |
| Aβ is the *upstream* driver | **INVERTED** | Inflammation (TNF-α, IL-1β) drives APP/amyloid handling (PMID:23294492, 23998706) |
| Aβ dominates vacuole content | **Not supported** | Vacuole proteome dominated by folding/autophagy proteins (PMID:28009083) |

The upstream trigger (ageing) and the terminal phenotype (vacuolar degeneration, weakness) are real, but the *specific* and *causal* role of Aβ between them is not supported. The most defensible reading reverses the arrow: **chronic autoimmune/inflammatory injury and mitochondrial degeneration overwhelm proteostasis, producing mixed protein aggregates (Aβ among them) as a downstream by-product.**

{{figure:ibm_amyloid_mechanistic_diagram.png|caption=Mechanistic comparison: the seed amyloid-beta proteotoxicity hypothesis versus the two better-supported competing IBM models — cytotoxic CD8 autoimmunity with anti-cN1A/HLA, and parallel mitochondrial mtDNA-deletion degeneration. Amyloid aggregates are positioned as a downstream marker of overwhelmed proteostasis rather than an upstream driver.}}

---

## Evidence Base

| Citation (PMID) | Type | Stance | Mechanistic claim tested | Key finding | Subtype/context | Confidence & limitations |
|---|---|---|---|---|---|---|
| [8394158](https://pubmed.ncbi.nlm.nih.gov/8394158/) | Human clinical | Supports | Local ↑ APP transcription | ↑ βAPP mRNA in vacuolated fibres of 8/8 IBM | sIBM + hereditary | Founding observation; non-specific |
| [16432144](https://pubmed.ncbi.nlm.nih.gov/16432144/) | Review/human | Supports | APP/Aβ as key upstream event | Canonical statement by originators | sIBM | Originating lab; assertion-level |
| [20711838](https://pubmed.ncbi.nlm.nih.gov/20711838/) | Human clinical | Supports | Aβ oligomers present, IBM-restricted | Aβ dimer/trimer/tetramer in all IBM, no controls | sIBM | Strongest biochemistry; single-lab; **no replication found** |
| [19533646](https://pubmed.ncbi.nlm.nih.gov/19533646/) | Human clinical | **Refutes** | Aβ is characteristic lesion | β-amyloid 0.00% vs TDP-43 23% of fibres | sIBM | Direct head-to-head; high confidence |
| [9781653](https://pubmed.ncbi.nlm.nih.gov/9781653/) | Human clinical | **Refutes** | Specificity | Amyloid+ubiquitin vacuoles in postpolio denervation | Chronic denervation | High confidence |
| [16788822](https://pubmed.ncbi.nlm.nih.gov/16788822/) | Human clinical | **Refutes** | Specificity + ageing necessity | Full Aβ+tau morphology in children | Congenital myopathy | High confidence |
| [8268725](https://pubmed.ncbi.nlm.nih.gov/8268725/) | Human clinical | Qualifies | Discriminates IBM from OPMD | Aβ label in a few IBM fibres only; structure unknown | IBM vs OPMD/fIBM | Weak; target undefined |
| [23496965](https://pubmed.ncbi.nlm.nih.gov/23496965/) | Human clinical | Refutes/qualifies | Specificity | APP ↑ & co-localizes with stress markers | GNE myopathy | APP tracks cell stress, not IBM |
| [39757935](https://pubmed.ncbi.nlm.nih.gov/39757935/) | Human clinical | Competing | Specific molecular marker | Cryptic HDGFL2 absent in 197 controls | sIBM | Strong specificity for TDP-43 axis |
| [10599804](https://pubmed.ncbi.nlm.nih.gov/10599804/) | In vitro | **Refutes** | Cell-autonomous accumulation | Cultured IBM myotubes lack βAPP | sIBM | From originating lab; decisive |
| [19626672](https://pubmed.ncbi.nlm.nih.gov/19626672/) | Human clinical | **Refutes** | Aβ→tau limb | "p-tau" antibodies stain normal myonuclei/non-tau | sIBM | Impugns reagent class |
| [28009083](https://pubmed.ncbi.nlm.nih.gov/28009083/) | Human clinical | Qualifies | Aβ dominates vacuole | 213 proteins, folding/autophagy dominate | sIBM rimmed vacuoles | No reported Aβ/APP enrichment |
| [22518836](https://pubmed.ncbi.nlm.nih.gov/22518836/) | Model organism | Qualified support | Aβ→mitochondrial injury | MCK-βAPP mice: early mito dysfunction | Transgenic mouse | Forced overexpression; not human IBM |
| [21518451](https://pubmed.ncbi.nlm.nih.gov/21518451/) | Model organism | Qualifies | Toxicity requires aggregates | APP weakness **without** aggregates | Drosophila | Dissociates toxicity from deposition |
| [23294492](https://pubmed.ncbi.nlm.nih.gov/23294492/) | In vitro | Competing/inverts | Causal order | TNF-α ↑ macroautophagy of APP/Aβ | Human muscle cells | Inflammation upstream of amyloid |
| [23998706](https://pubmed.ncbi.nlm.nih.gov/23998706/) | Human/in vitro | Competing/inverts | Causal order | IL-1β co-localizes w/ APP, promotes amyloid | sIBM | Inflammation upstream of amyloid |
| [31326977](https://pubmed.ncbi.nlm.nih.gov/31326977/) | Human clinical | Competing | Autoimmune-cytotoxic model | KLRG1+ CD8 T cells invade myofibres | sIBM (411 samples) | Leading alternative |
| [24752512](https://pubmed.ncbi.nlm.nih.gov/24752512/) | Human clinical | Competing | Autoantibody biomarker | Anti-cN1A combined sensitivity 76% | sIBM | Supports autoimmune model |
| [41283441](https://pubmed.ncbi.nlm.nih.gov/41283441/) | In vitro | Competing | Autoantibody functional effect | Anti-cN1A+ serum → 1126 DEGs (immune) | sIBM myotubes | Pilot; small n |
| [33354847](https://pubmed.ncbi.nlm.nih.gov/33354847/) | Human clinical | Competing | Mitochondrial degeneration | mtDNA deletions, 10% vs 1% heteroplasmy | sIBM | Parallel amyloid-independent axis |
| [7602331](https://pubmed.ncbi.nlm.nih.gov/7602331/) | Human clinical | Competing | Mitochondrial degeneration | COX-deficient fibres w/ clonal mtDNA deletions | sIBM | Parallel axis |
| [37739573](https://pubmed.ncbi.nlm.nih.gov/37739573/) | Human clinical (RCT) | Refutes (indirect) | Proteostasis therapy efficacy | Arimoclomol negative, n=150 | sIBM | Closest test of proteotoxicity model |
| [39843353](https://pubmed.ncbi.nlm.nih.gov/39843353/) | Systematic review | Refutes (indirect) | Any therapy efficacy | 14 RCTs, no effect; no anti-amyloid agent | sIBM | High-quality synthesis |
| [27009270](https://pubmed.ncbi.nlm.nih.gov/27009270/) | Human/in vitro | Refutes (indirect) | Proteostasis therapy | Earlier arimoclomol proof-of-concept negative | sIBM | Reinforces failure |
| [29611059](https://pubmed.ncbi.nlm.nih.gov/29611059/) | Human genetic | Competing | Genetic architecture | HLA-DRB1\*03:01 top; VCP/SQSTM1/FYCO1 | sIBM | No amyloid-pathway gene |
| [26362759](https://pubmed.ncbi.nlm.nih.gov/26362759/) | Human genetic | Competing | Genetic architecture | HLA + PTPN22 genome-wide significant | IIM incl. IBM | Immune, not amyloid |
| [19622839](https://pubmed.ncbi.nlm.nih.gov/19622839/) | Meta/other | Refutes (meta) | Authority of the belief | Citation bias, amplification, invention | IBM amyloid literature | Explains inflated apparent support |

---

## Limitations and Knowledge Gaps

For each gap: **scope · why it matters · what was checked · what would resolve it.**

1. **No independent replication of the Aβ-oligomer / Aβ42 immunoblot data.**
   *Scope:* the single strongest biochemical support (PMID:20711838) and the ADDL/immunoblot arm generally. *Why it matters:* the abnormal-presence claim rests almost entirely on the originating laboratory; a formal citation-network analysis found the belief's authority inflated by citation bias, amplification and invention rather than accumulated data ([PMID: 19622839](https://pubmed.ncbi.nlm.nih.gov/19622839/)). *What was checked:* a targeted PubMed search for independent (non-originating-lab) replication of Aβ-oligomer/Aβ42 IHC in IBM returned no papers. *Resolution:* blinded, multi-centre quantitative Aβ42/oligomer assays (MSD/ELISA + mass spectrometry) on IBM vs disease-control muscle from independent labs.

2. **The Aβ → tau causal link is compromised at the reagent level.**
   *Scope:* the phospho-tau limb of the Alzheimer analogy. *Why it matters:* antibodies reported to show abnormal p-tau in IBM react to normal myonuclei and recognize non-tau proteins ([PMID: 19626672](https://pubmed.ncbi.nlm.nih.gov/19626672/)), so the histological arm may report protein that is not there. *Resolution:* mass-spectrometry-validated, epitope-defined tau detection with genetic-knockdown controls.

3. **Directionality of the inflammation ↔ amyloid edge is inferred, not perturbed longitudinally in patients.**
   *Scope:* whether cytokines (TNF-α, IL-1β) are upstream of APP/amyloid in vivo. *Why it matters:* in-vitro data (PMID:23294492, 23998706) invert the seed hypothesis, but human temporal ordering is unproven. *Resolution:* longitudinal biopsies / spatial-omics timecourse, or an anti-cytokine perturbation measuring downstream APP/amyloid.

4. **No amyloid-directed clinical trial exists.**
   *Scope:* therapeutic test of the mechanism. *Why it matters:* the hypothesis has never been falsified or confirmed by targeted therapy; the nearest proxy (arimoclomol, proteostasis) failed (PMID:37739573, 39843353). *Resolution:* this is a *source/data absence* — no BACE/γ-secretase inhibitor or anti-Aβ antibody has been trialed in IBM. A small biomarker-driven trial would resolve it but is low priority given refutation on other axes.

5. **Genetic source absence for the amyloid pathway.**
   *Scope:* GWAS/exome susceptibility. *Why it matters:* no APP, PSEN1/2, BACE1, or APOE association is reported (PMID:29611059, 26362759), whereas HLA/PTPN22 (immune) and VCP/SQSTM1/FYCO1 (autophagy) are. *What was checked:* published IBM GWAS/Immunochip and candidate-gene studies. *Resolution:* larger IBM-specific GWAS/whole-genome sequencing explicitly interrogating amyloid-pathway loci (confirmatory).

6. **Vacuole proteomics did not explicitly report Aβ/APP absence.**
   *Scope:* PMID:28009083 reports 213 enriched proteins dominated by folding/autophagy but does not state whether Aβ/APP were sought and not found. *Why it matters:* "not reported" is weaker than "absent." *Resolution:* targeted re-interrogation of the LCM-MS peptide libraries for APP/Aβ peptides.

---

## Alternative Models

| Model | Relationship to seed | Core evidence | Assessment |
|---|---|---|---|
| **Cytotoxic CD8 T-cell autoimmunity (anti-cN1A / HLA)** | **Alternative / upstream** | KLRG1+ CD8 invasion (PMID:31326977); anti-cN1A biomarker (PMID:24752512); HLA-DRB1\*03:01, PTPN22 (PMID:29611059, 26362759); serum functional DEGs (PMID:41283441) | Best-supported; drives inflammation *upstream* of amyloid handling |
| **TDP-43 proteinopathy / cryptic-exon dysregulation** | **Alternative (specific marker)** | TDP-43 in 23% fibres (PMID:19533646); cryptic HDGFL2 absent in 197 controls (PMID:39757935) | Sensitive & specific molecular lesion; supplants amyloid as IBM's signature |
| **Autophagy-lysosome failure / proteostasis collapse** | **Parallel / downstream container** | Vacuole proteome folding+autophagy dominant (PMID:28009083); VCP/SQSTM1/FYCO1 risk genes (PMID:29611059) | Frames amyloid as one of several downstream aggregates |
| **Mitochondrial degeneration (mtDNA deletions, COX-deficiency)** | **Parallel / amyloid-independent** | Clonal mtDNA deletions, COX-deficient fibres (PMID:7602331); 10% vs 1% heteroplasmy (PMID:33354847) | Independent intrinsic-degeneration axis; arises without amyloid in patients |
| **Inflammation-driven amyloid handling** | **Inverts seed causal order** | TNF-α ↑ APP autophagy (PMID:23294492); IL-1β promotes APP/amyloid (PMID:23998706) | Places amyloid downstream of the immune process |

The seed hypothesis is thus best understood as a **downstream consequence** node feeding off the proteostasis-failure container, while the *upstream drivers* are the autoimmune-cytotoxic and TDP-43 axes.

---

## Discriminating Tests

1. **Blinded multi-lab quantitative amyloid assay across myopathies.** Sample: IBM vs postpolio/GNE/OPMD/congenital-myopathy vs age-matched controls. Assay: quantitative Aβ40/Aβ42/oligomer (MSD + MS) plus TDP-43/cryptic-HDGFL2 IHC on serial sections. *Expected under seed:* Aβ specifically elevated in IBM. *Expected under refutation:* Aβ tracks chronicity across all vacuolar myopathies; HDGFL2/TDP-43 uniquely marks IBM.

2. **Temporal-ordering perturbation.** Anti-cytokine (IL-1β/TNF-α) intervention or ex-vivo cytokine challenge of human myotubes, reading APP/Aβ as the *downstream* variable. *Expected:* cytokine modulation changes amyloid load (amyloid downstream), not vice versa.

3. **Patient stratification by anti-cN1A status × amyloid burden.** Test whether amyloid deposition correlates with immune markers (CD8 invasion, MHC-I, HLA-DRB1\*03:01) rather than with an independent amyloid axis. *Expected:* amyloid co-varies with proteostatic/inflammatory load, not as an independent driver.

4. **Amyloid-lowering proof-of-concept (falsification test).** A short biomarker trial of a BACE/γ-secretase inhibitor or anti-Aβ antibody in early IBM, primary endpoint = muscle Aβ reduction, secondary = IBMFRS/qMRI. *Expected under seed:* clinical benefit tracks Aβ reduction. *Expected under refutation:* Aβ falls, disease progresses (mirroring arimoclomol). This is the only direct clinical test never performed.

5. **Cell-autonomy re-test with genetic tools.** iPSC-derived IBM myotubes ± inflammatory milieu ± TDP-43 knockdown, assaying spontaneous βAPP accumulation. *Expected:* accumulation requires the inflammatory/TDP-43 context (consistent with PMID:10599804), not the IBM genotype alone.

---

## Curation Leads (require curator verification)

**Status recommendation:** Retain **DEPRECATED**. The search reinforces the existing curation across five independent axes (specificity, cell-autonomy, unbiased proteomics, therapeutics, genetics). No change to status warranted.

**Candidate evidence references to add / verify (snippets to confirm against abstracts):**

- **PMID:39757935** — *Loss of TDP-43 Splicing Repression Occurs in Myonuclei of Inclusion Body Myositis Patients.* Verify: "cryptic HDGFL2 immunoreactivity was absent in 197 muscle biopsies from a variety of disease controls, except for 2 patients with vacuolar myopathies." Role: COMPETING — IBM-specific molecular marker distinct from amyloid.
- **PMID:23496965** — *Cell stress molecules in the skeletal muscle of GNE myopathy.* Verify: mRNA of APP higher in GNE myopathy (not statistically significant); APP correlates with pro-inflammatory/cell-stress markers. Role: REFUTE (specificity).
- **PMID:22518836** — *Mitochondrial dysfunction in skeletal muscle of APP-overexpressing mice.* Role: QUALIFIED SUPPORT (model organism).
- **PMID:21518451** — *Expression of human APP in Drosophila skeletal muscle.* Verify: "Muscles from transgenic animals did not display protein aggregates or structural abnormalities." Role: QUALIFIES.
- **PMID:23294492 / PMID:23998706** — TNF-α / IL-1β drive APP/amyloid handling. Role: COMPETING/INVERTS causal order.
- **PMID:31326977, 24752512, 41283441, 33354847, 7602331** — autoimmune-cytotoxic and mitochondrial competing models.
- **PMID:37739573, 39843353, 27009270** — negative therapeutic evidence.
- **PMID:29611059, 26362759** — genetic architecture (HLA/PTPN22 + VCP/SQSTM1/FYCO1; no amyloid gene).

**Candidate pathophysiology nodes / edges:**
- Add edge: `Inflammation (TNF-α, IL-1β) → APP/amyloid processing` (inflammation upstream) — PMID:23294492, 23998706.
- Reposition `amyloid-beta aggregates` as a **downstream child** of `Autophagy-Lysosome Failure and Rimmed Vacuole Formation`; mark edge `amyloid-beta → tau phosphorylation` as **contradicted/reagent-compromised** (PMID:19626672).
- Add competing node: `TDP-43 mislocalization / cryptic-exon (HDGFL2)` as the specific molecular lesion.

**Candidate ontology terms:**
- Cell types: skeletal muscle fibre (CL:0000188); CD8-positive, alpha-beta cytotoxic T cell (CL:0000794); KLRG1+ terminally differentiated effector T cell.
- Processes: GO:0006914 (autophagy); GO:0043161 (proteasome-mediated protein catabolism); GO:0002250 (adaptive immune response); GO:0034205 (amyloid-beta formation); mtDNA maintenance.

**Candidate `knowledge_gaps` / discussion prompts:**
- "Independent replication of muscle Aβ-oligomer/Aβ42 immunoblot data is absent as of the search date (single-lab)."
- "No amyloid-directed therapeutic has been trialed in IBM; the mechanism has never been clinically falsified directly."
- "No amyloid-pathway susceptibility locus (APP/PSEN/BACE1/APOE) reported in IBM genetics."
- "Vacuole proteomics (PMID:28009083) does not explicitly state whether Aβ/APP peptides were sought — 'not reported' vs 'absent' should be distinguished."

---

## Conclusion

Across specificity (0.00% vs 23% for TDP-43; non-specificity across denervation, GNE, congenital myopathy), cell-autonomy (cultured IBM myotubes lack βAPP), unbiased vacuole proteomics (folding/autophagy, not amyloid), therapeutics (arimoclomol failed; no anti-amyloid trial), and genetics (HLA/PTPN22 + VCP/SQSTM1/FYCO1, no amyloid gene), the amyloid-beta proteotoxicity hypothesis is **refuted as a specific, upstream driver of IBM** and is correctly curated as **DEPRECATED**. Model-organism data show Aβ *can* be proteotoxic in principle, so amyloid is retained as a real but **downstream marker of overwhelmed proteostasis**, subordinate to the better-supported autoimmune-cytotoxic and TDP-43 mechanisms.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist ibm amyloid mechanistic diagram](openscientist_artifacts/provenance_ibm_amyloid_mechanistic_diagram.json)
![OpenScientist ibm amyloid mechanistic diagram](openscientist_artifacts/provenance_ibm_amyloid_mechanistic_diagram.png)