---
disorder: Myoclonus_Dystonia_Syndrome
research_status: fallback_after_provider_timeouts
last_updated: "2026-05-07T21:58:00Z"
provider_attempts:
  - provider: falcon
    command: "timeout 180s just research-disorder falcon Myoclonus_Dystonia_Syndrome"
    result: "timeout_exit_124"
  - provider: openai
    command: "timeout 180s just research-disorder openai Myoclonus_Dystonia_Syndrome"
    result: "timeout_exit_124"
manual_evidence_scope:
  - ORPHA:36899
  - PMID:20301587
  - PMID:11528394
  - PMID:17200151
  - PMID:25209853
  - PMID:23365103
  - PMID:27053715
  - PMID:33452690
  - PMID:29952836
  - PMID:31449710
---

# Myoclonus-Dystonia Syndrome Evidence-Backed Research Fallback

## Provider Attempts

Both bounded deep-research providers failed to return usable artifacts. Falcon
timed out after 180 seconds, and the secondary OpenAI run also timed out after
180 seconds. No partial provider research file was left on disk, so the curation
uses fetched Orphanet and PubMed cache evidence.

## Evidence Synthesis

ORPHA:36899 defines myoclonus-dystonia syndrome as a rare movement disorder with
mild-to-moderate dystonia and lightning-like myoclonic jerks. The structured
record supplies the European point-prevalence band, autosomal dominant
inheritance, disease-causing SGCE and KCTD17 gene rows, MONDO:0000903 exact
mapping, and HPO phenotype frequencies for myoclonus, limb myoclonus, dystonia,
torticollis, writer's cramp, compulsive behaviors, anxiety, depression, and
panic attack.

PMID:20301587 provides the clinical GeneReviews frame for SGCE
myoclonus-dystonia: rapid myoclonus and dystonia, typical neck/trunk/upper-limb
distribution, additional focal dystonia including cervical dystonia and writer's
cramp, alcohol responsiveness, diagnosis by heterozygous SGCE pathogenic
variant, treatment options, and autosomal dominant inheritance with
parental-origin-dependent penetrance.

PMID:11528394 is the key SGCE discovery paper. It describes autosomal dominant,
alcohol-sensitive myoclonic jerks with dystonia and psychiatric abnormalities,
then reports heterozygous SGCE loss-of-function variants mapped by positional
cloning. It also supports SGCE brain expression and maternal-imprinting
penetrance differences.

PMID:17200151 supports the protein-processing mechanism. Disease-associated
epsilon-sarcoglycan missense variants fail to reach the cell surface, are
retained intracellularly, become polyubiquitinated, and are rapidly degraded by
the proteasome. The YAML therefore models impaired plasma-membrane localization
and increased ubiquitination as an upstream mechanism.

PMID:29952836 and PMID:31449710 provide review-level mechanistic synthesis for
the downstream motor network. They implicate altered cerebello-thalamic pathway
function, possible GABAergic/Purkinje-cell dysfunction, striatal plasticity,
serotonin homeostasis, calcium homeostasis, dopaminergic-membrane stabilization,
and the cerebello-thalamo-pallido-cortical network.

PMID:25209853 supports diagnostic phenotype predictors for SGCE-positive cases:
age at onset no later than 10 years and predominant upper-body involvement of
pure myoclonus-dystonia. PMID:23365103 supports the psychiatric component in
SGCE mutation-positive individuals, especially compulsivity, anxiety, and
alcoholism.

PMID:27053715 provides class I randomized crossover trial evidence that
zonisamide improves myoclonus and related disability. PMID:33452690 supports
deep brain stimulation, especially GPi stimulation, as a long-term treatment
option for medically refractory myoclonus-dystonia.

## Scope Confirmation

The YAML emphasizes the SGCE-related form because it is the best-evidenced and
major genetically defined subtype, but it retains KCTD17 as an Orphanet-listed
disease-causing gene. Evidence blocks avoid the title-only KCTD17 DOI cache and
use only exact snippets from cache-backed Orphanet and PubMed references.
