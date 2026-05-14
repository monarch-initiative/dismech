# Inclusion Body Myopathy with Paget Disease of Bone and Frontotemporal Dementia Deep Research Fallback

## Provider Attempts

- `falcon`: `just research-disorder falcon Inclusion_Body_Myopathy_with_Paget_Disease_of_Bone_and_Frontotemporal_Dementia` produced no content after approximately 20 minutes and was terminated with signal 15.
- `openai`: `just research-disorder openai Inclusion_Body_Myopathy_with_Paget_Disease_of_Bone_and_Frontotemporal_Dementia` produced no content in the bounded follow-up window and was terminated with signal 15.

Because the preferred deep-research providers did not return usable content in
bounded attempts, this fallback records the literature scope used for curation.
All YAML evidence was taken from generated Orphanet, PubMed, and
ClinicalTrials.gov reference caches, not from hand-created reference text.

## Literature Scope

Inclusion body myopathy with Paget disease of bone and frontotemporal dementia
corresponds to Orphanet ORPHA:52430 and MONDO:0000507. Orphanet defines the
condition as an autosomal dominant adult-onset multisystem degenerative genetic
disorder characterized by proximal and distal muscle weakness, early-onset
Paget disease of bone, and premature frontotemporal dementia. The Orphanet
record provides the exact MONDO and OMIM mappings, the worldwide
<1/1,000,000 point-prevalence band, adult onset, disease-gene assertions for
VCP, HNRNPA2B1, and HNRNPA1, and the HPO phenotype-frequency table used for
phenotype coverage.

The key human clinical review for classic VCP-associated IBMPFD describes a
progressive autosomal dominant disorder due to VCP variants, with approximately
90% myopathy, about half Paget disease of bone, one-third premature
frontotemporal dementia, and ubiquitin / beta amyloid / TDP-43 inclusions in
affected muscle, brain, and heart. This review anchors the disease triad and
supports the proximal VCP proteostasis node.

The principal mechanistic paper shows that VCP is essential for maturation of
ubiquitin-containing autophagosomes. RNAi-mediated VCP deficiency,
dominant-negative VCP, and disease-associated VCP mutants caused immature
autophagic vesicle accumulation; patient-derived IBMPFD myoblasts accumulated
large LAMP-positive vacuoles and LC3-II. These findings support the causal
chain from VCP proteostasis failure to defective autophagosome maturation,
ubiquitin-positive aggregate accumulation, and rimmed-vacuole myopathy.

A focused autophagy review independently frames IBMPFD as a disorder of
autophagy and links p97/VCP mutations to accumulation of autophagic structures
through defective p97/VCP-mediated autophagosome maturation. This was used as
secondary support for the autophagy node rather than as sole evidence for a
human phenotype.

The VCP-associated myopathy practice recommendation supports the diagnostic and
management sections: VCP myopathy should be considered in limb-girdle myopathy
or autosomal dominant myopathy, genetic testing is definitive, muscle biopsy is
important when genetic results are unavailable or uncertain, rimmed vacuoles are
a hallmark, electrodiagnostic studies and MRI help rule out mimics, and
standardized management optimizes patient care.

ClinicalTrials.gov records NCT04823143 and NCT01353430 were used only as
observational natural-history and phenotyping studies for VCP disease. No
interventional disease-modifying treatment was asserted from these trials.

## Curation Decisions

- Used MONDO:0000507 as the disease term because ORPHA:52430 maps it exactly.
- Included all ORPHA very frequent and frequent HPO phenotypes, plus selected
  occasional respiratory muscle weakness and ALS entries that are important to
  the disease spectrum and progression.
- Used VCP as the mechanistically modeled gene, while retaining HNRNPA2B1 and
  HNRNPA1 in the genetic section because Orphanet lists them as disease-causing
  genes for this structured disorder grouping.
- Kept the pathophysiology graph atomic: VCP-dependent proteostasis failure,
  defective ubiquitin-containing autophagosome maturation, ubiquitin-positive
  aggregate accumulation, rimmed-vacuole skeletal myopathy, pagetic bone
  remodeling, and frontotemporal neurodegeneration.
- Represented care conservatively as supportive multidisciplinary management
  and genetic counseling; no curative or established disease-modifying therapy
  was asserted.
