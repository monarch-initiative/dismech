# Baylisascariasis: cached-source completeness pass

This is a local literature sweep produced from the PubMed references already cached for the pull request. No external deep-research provider was used.

## Source set

| Reference | Role in this pass |
| --- | --- |
| PMID:16223954 | Full-text 2005 *Clinical Microbiology Reviews* review. Used for the organism identity, accidental ingestion of infective eggs from raccoon latrines or fecally contaminated articles, pica/geophagia risk, CNS larval invasion, diagnostic limitations, poor post-CNS-invasion treatment outcomes, and prevention framing. |
| PMID:26960940 | Full-text 2016 update review. Used for the Ascarididae placement of *Baylisascaris procyonis*, the raccoon-only direct life cycle, raccoons as high-shedding definitive hosts, humans as paratenic hosts, environmental embryonated eggs as the infective stage, L3 larval intestinal penetration and bloodstream migration, accidental CNS and eye migration, and early albendazole plus corticosteroid treatment. |
| PMID:40671903 | Full-text 2025 scoping review of 60 published human infections. Used for the neural versus ocular case counts, fatal and residual neurologic outcomes, ocular vision-loss outcomes, pica/geophagia and raccoon-latrine exposures, the 36-case Table 3 initial-sign frequencies, peripheral-blood and CSF eosinophilia frequencies, MRI white-matter abnormality frequency, serologic-test use, and ocular photocoagulation experience. |
| PMID:40742893 | Full-text 2025 MMWR report. Used for two recent Los Angeles County pediatric cases, raccoon-feces exposure investigation, eosinophilic meningitis with peripheral and CSF eosinophilia, diffuse white-matter MRI abnormalities, rBpRAG1 immunoblot testing at CDC, and the albendazole post-exposure window after high-suspicion oral exposure. |
| PMID:23829916 | Neurology-focused review abstract. Used for neural larva migrans with CSF and peripheral eosinophilia, diagnosis by larvae, epidemiologic history, serology, and CNS imaging, ocular larva migrans presenting as diffuse unilateral subacute neuroretinitis, and photocoagulation of visible intraocular larvae. |
| PMID:15715975 | CNS severe/fatal disease review abstract. Used for the diagnostic challenge of CNS Baylisascariasis and the need for brain-biopsy larvae or exclusion of competing eosinophilic meningoencephalitis causes for definitive diagnosis. |

## Completeness cross-check

- The pathophysiology graph now separates CNS larval invasion from eosinophilic meningoencephalitis, and retinal larval localization from diffuse unilateral subacute neuroretinitis.
- The eosinophilic meningoencephalitis node now carries the eosinophil cell type and eosinophil migration process, and it points to peripheral eosinophilia and CSF eosinophilia as separate phenotypes.
- The seven Table 3 presenting signs above 10% in neural larva migrans now have phenotype rows: fever, irritability, ataxia, gaze or eye-tracking abnormalities, headache, seizures, and motor impairment.
- Peripheral eosinophilia, CSF eosinophilia, lethargy, and diffuse white-matter MRI abnormalities now carry the frequencies reported in the 2025 scoping review.
- The MRI diagnosis row now uses the 24/24 detailed-report white-matter finding from PMID:40671903 in addition to the neurology review's diagnostic-method summary.
- Laser photocoagulation now records a `SURGERY` therapeutic modality and targets the retinal-larva node directly.
- The `progression:` block now records the fatal and residual-deficit outcome phase described by the 2025 scoping review.
- The reference note for PMID:15715975 now says the abstract supports brain-biopsy larval isolation or exclusion of other eosinophilic meningoencephalitis causes, rather than a noninvasive clinical diagnosis claim.

## Deferred or bounded items

- Visceral larva migrans remains prose-level context because the conserved, literature-rich branches in the cached sources are neural and ocular larva migrans; the sole non-neural/non-ocular case in the 2025 scoping review was an eosinophilic cardiac pseudotumor.
- Environmental raccoon-latrine removal remains in the literature sweep rather than a treatment row because it prevents exposure to eggs rather than treating an established disease mechanism.
- Post-exposure albendazole after known oral exposure remains captured on the early albendazole/corticosteroid row; the cached MMWR describes it as appropriate after high-suspicion exposure, not as a trial-tested treatment for established neural disease.

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 6 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.
