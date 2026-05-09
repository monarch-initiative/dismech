# Pyruvate Dehydrogenase Deficiency Deep Research Fallback

## Provider Attempts

- 2026-05-05T19:39Z: `just research-disorder falcon "Pyruvate dehydrogenase deficiency"`
  failed before provider execution because the disorder YAML file had not yet
  been created.
- 2026-05-05T19:42Z: direct `deep-research-client research` with provider
  `falcon` produced no output during the bounded 240 second wait and was
  terminated by `timeout`.
- 2026-05-05T19:47Z: direct `deep-research-client research` with provider
  `openai` produced no output during the bounded 180 second wait and was
  terminated by `timeout`.
- 2026-05-05T19:52Z: direct `deep-research-client research` with provider
  `openscientist` produced no output during the bounded 180 second wait and was
  terminated by `timeout`.
- 2026-05-05T20:07Z: direct `deep-research-client research` with provider
  `perplexity` failed immediately with a 401 quota error.

No provider-generated deep-research narrative was available within the bounded
runtime. Curation therefore proceeded from regenerated structured Orphanet
records, fetched PubMed caches, fetched ClinicalTrials.gov caches, and direct
NCBI/ClinicalTrials.gov metadata checks. No `references_cache/*.md` file was
created or edited by hand.

## Evidence Scope Used For Curation

- ORPHA:765 for the disease definition, inheritance, age of onset, prevalence,
  exact MONDO mapping, broad OMIM subtype mappings, and structured root HPO
  phenotype rows.
- ORPHA:79243, ORPHA:255138, ORPHA:79244, ORPHA:2394, ORPHA:255182, and
  ORPHA:79246 for the six recognized PDH complex subunit/regulatory subtypes,
  exact subtype MONDO/OMIM cross-references, and disease-causing gene rows.
- PMID:22896851 for the 371-patient clinical, biochemical, neuroimaging, and
  natural-history spectrum.
- PMID:23622387 for diagnostic approach, PDH complex architecture, major
  subtypes, and sex-linked PDHA1 presentation patterns.
- PMID:21908116 for the PDH complex glycolysis-to-TCA role, epilepsy mechanism,
  structural brain-anomaly mechanism, and ketogenic-diet bypass rationale.
- PMID:28101805 for human clinical ketogenic-diet outcomes in 19 Swedish
  pediatric patients.
- PMID:26008863 for thiamine-responsive PDHA1-associated paroxysmal
  exercise-induced dystonia.
- PMID:29445841 for E1-alpha folding/assembly defects and impaired PDC activity.
- PMID:16651305 and PMID:18411236 for dichloroacetate clinical-trial evidence,
  lactate reduction, lack of broad clinical-outcome improvement, and neuropathy
  safety signal.
- PMID:23467562 and PMID:35996497 for phenylbutyrate mechanism, in vitro/model
  evidence, variant-specific potential responsiveness, and the comparative
  DCA/phenylbutyrate treatment landscape.
- clinicaltrials:NCT02616484 for the active-not-recruiting Phase 3
  dichloroacetate trial, clinicaltrials:NCT03734263 for the completed Phase 2
  phenylbutyrate trial, and clinicaltrials:NCT03056794 for the recruiting
  natural-history/genetic study.

## Curation Conclusions

Pyruvate dehydrogenase deficiency is best represented as a genetically
heterogeneous neurometabolic mitochondrial disorder in which defects in PDH
complex structural subunits or regulatory phosphatase reduce conversion of
pyruvate to acetyl-CoA. The metabolic block links glycolysis to inadequate TCA
cycle substrate supply, pyruvate/lactate accumulation, lactic acidosis, and
energy failure in the developing brain. Human cohort and review evidence
supports neurodevelopmental delay, hypotonia, seizures, corpus-callosum and
ventricular abnormalities, Leigh-like neuroimaging, and early mortality in the
severe neonatal end of the spectrum. Treatment evidence is strongest for
ketogenic diet as a bypass strategy providing acetyl-CoA through fatty-acid
oxidation/ketosis; thiamine responsiveness exists in selected PDHA1 variants;
dichloroacetate and sodium phenylbutyrate remain targeted pharmacologic or
investigational approaches with biochemical rationale and limited or mixed
clinical evidence.
