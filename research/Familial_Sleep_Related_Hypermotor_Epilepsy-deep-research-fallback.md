# Familial Sleep-Related Hypermotor Epilepsy Deep Research Fallback

## Provider Attempts

- `falcon`: `timeout --foreground 120s just research-disorder falcon Familial_Sleep_Related_Hypermotor_Epilepsy` produced no usable content and was terminated with signal 15.
- `openai`: `timeout --foreground 120s just research-disorder openai Familial_Sleep_Related_Hypermotor_Epilepsy` produced no usable content and was terminated with signal 15.

Because the preferred deep-research providers did not return usable content in
bounded attempts, this fallback records the literature scope used for curation.
All YAML evidence was taken from generated Orphanet and PubMed reference
caches, not from hand-created reference text.

## Literature Scope

Familial sleep-related hypermotor epilepsy corresponds to MONDO:0000030 and
Orphanet ORPHA:98784. The Orphanet record provides the structured definition,
autosomal dominant inheritance, gene rows for CABP4, CHRNA2, CHRNA4, CHRNB2,
CRH, DEPDC5, and KCNT1, and the HPO phenotype-frequency table used for
frequency-backed phenotype entries.

The clinical scope was anchored with the GeneReviews ADSHE chapter and the
Neurology consensus definition paper. Those sources support the modern
sleep-related hypermotor epilepsy terminology, diagnostic certainty levels
based on witnessed, video-documented, and video-EEG-documented events, genetic
testing across the heterogeneous ADSHE gene set, non-progressive but lifelong
course, carbamazepine-centered therapy, genotype-informed alternatives, VNS,
and genetic counseling.

Mechanistic curation focused on three evidence-backed branches. CHRNA4,
CHRNB2, and CHRNA2 studies support nicotinic acetylcholine receptor dysfunction
with altered receptor efficacy or loss of function. DEPDC5 evidence supports
loss-of-function variants in ADNFLE families and GATOR1/mTORC1 dysregulation in
model systems. KCNT1 evidence supports altered Slack-channel effects on
cortical neuronal excitability. These branches converge on cortical
excitation-inhibition imbalance and sleep-related hypermotor seizure
expression.

## Curation Decisions

- Used MONDO:0000030 as the disease term because the ORPHA record title is
  broader and its MONDO cross-reference points to an obsolete identifier.
- Included all ORPHA very frequent and frequent HPO phenotypes: nocturnal
  seizures, paroxysmal dystonia, involuntary movements, and motor stereotypy.
- Retained additional occasional ORPHA phenotypes when clinically coherent for
  SHE semiology or diagnosis: focal hyperkinetic seizure, interictal
  epileptiform activity, and urinary incontinence.
- Modeled the five MONDO/OMIM ENFL subtypes as root subtypes, and added a
  DEPDC5-related SHE subtype because Orphanet and human family sequencing both
  support DEPDC5 loss-of-function in SHE/ADNFLE presentations.
- Did not force individual mechanistic branches for CABP4 or CRH because the
  available curated evidence was sufficient to record them as genetic
  heterogeneity but not enough for a distinct mechanism node.
