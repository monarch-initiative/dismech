# Adult-Onset Dystonia-Parkinsonism Deep Research Fallback

## Provider Attempts

- `falcon`: `timeout 75s just research-disorder falcon Adult_Onset_Dystonia_Parkinsonism` was terminated by timeout with signal 15 before returning content.
- `openai`: `timeout 75s just research-disorder openai Adult_Onset_Dystonia_Parkinsonism` was terminated by timeout with signal 15 before returning content.
- `perplexity`: `timeout 75s just research-disorder perplexity Adult_Onset_Dystonia_Parkinsonism` failed immediately with an API quota/401 error.

Because the preferred deep-research providers did not return usable content in
bounded attempts, this fallback records the literature scope used for curation.
All YAML evidence was taken from generated Orphanet and PubMed reference caches,
not from hand-created reference text.

## Literature Scope

Adult-onset dystonia-parkinsonism corresponds to Orphanet ORPHA:199351 and
MONDO:0013060. Orphanet defines it as a rare neurodegenerative disease usually
presenting before age 30 with dystonia, L-dopa-responsive parkinsonism,
pyramidal signs, and rapid cognitive decline. Orphanet also provides the
autosomal recessive inheritance, PLA2G6 gene association, point prevalence, and
HPO phenotype frequency table used for the phenotype section.

The original locus paper used homozygosity mapping and mutational analysis in
families with adult-onset levodopa-responsive dystonia-parkinsonism, pyramidal
signs, cognitive/psychiatric features, and cerebral/cerebellar atrophy to
identify PLA2G6 mutations. A subsequent PARK14 phenotype-spectrum study found
compound heterozygous PLA2G6 mutations in early-onset L-dopa-responsive
parkinsonism with dementia and frontotemporal lobar atrophy, with variable iron
accumulation.

GeneReviews frames PLA2G6-associated neurodegeneration as an age-related
continuum and describes adult PLAN as gait disturbance or neuropsychiatric
onset followed by dystonia and parkinsonism in the late teens to early
twenties. It supports diagnosis by biallelic pathogenic PLA2G6 variants,
autosomal recessive inheritance, consideration of dopaminergic agents for adult
PLAN, and multidisciplinary supportive management.

The largest PLA2G6-related parkinsonism systematic review describes young onset
with parkinsonism/dystonia, gait/balance, psychiatric/cognitive symptoms,
frequent pyramidal signs, myoclonus, cognitive impairment, levodopa
responsiveness complicated by dyskinesias, DBS benefit in some patients,
cerebral/cerebellar atrophy, variable mineralization, abnormal presynaptic
dopaminergic terminal imaging, and mixed Lewy/tau pathology in autopsied cases.

Mechanistically, PLA2G6 encodes calcium-independent group VI phospholipase A2.
Experimental evidence supports membrane lipid and retromer disruption,
ceramide elevation, mitochondrial respiratory-chain dysfunction, reduced ATP
synthesis, abnormal mitochondrial morphology, lipid peroxidation, elevated ROS,
patient-fibroblast mitochondrial membrane defects, and dopaminergic neuron
degeneration in a PARK14 knockin mouse model. Human neuropathology supports
widespread alpha-synuclein-positive Lewy pathology and hyperphosphorylated tau
with neurofibrillary tangles.

## Curation Decisions

- Used ORPHA:199351 for disease scope, inheritance, prevalence, gene mapping,
  and HPO phenotype frequencies.
- Used MONDO:0013060 as the disease term, preserving its canonical label
  "autosomal recessive Parkinson disease 14" while using the Orphanet name as
  the display/preferred term.
- Represented brain iron accumulation as occasional and variable, not required,
  because adult-onset series report absent iron in some cases and systematic
  review data indicate mineralization in a minority.
- Added levodopa/dopaminergic therapy, DBS, and multidisciplinary supportive
  care only where cached evidence directly supported those interventions.
- Avoided unsupported disease-modifying therapy claims; experimental
  deuterated polyunsaturated fatty acid rescue in models was kept out of the
  treatment section because it is not established clinical care for this
  disorder.
