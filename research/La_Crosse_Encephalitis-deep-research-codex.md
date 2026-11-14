# La Crosse encephalitis: cached-source completeness pass

This is a local literature sweep produced from the PubMed references already cached for the pull request. No external deep-research provider was used.

## Source set

| Reference | Role in this pass |
| --- | --- |
| PMID:35755222 | Open full-text overview of La Crosse virus disease. Used for the LACV infectious agent, Aedes vector and small-mammal amplifying hosts, usually asymptomatic infection, neuroinvasive presentations, acute fever/headache/vomiting/seizure/CSF/imaging findings, possible hyponatremia, long-term epilepsy/hemiparesis/neurobehavioral sequelae, serologic diagnosis with neutralization confirmation, supportive care, seizure treatment, and absence of recommended antiviral therapy. |
| PMID:34280142 | U.S. ArboNET surveillance analysis of human LACV disease during 2003-2019. Used for Peribunyaviridae/California-serogroup background, enzootic mosquito and mammal ecology, incidental dead-end human infection, the incubation-period and clinical-spectrum background, national reported-case counts, the neuroinvasive/non-neuroinvasive case mix, and nationwide annual incidence. Its introductory statements are treated as background rather than review synthesis. |
| PMID:35607778 | Contemporary pediatric LACV neuroinvasive disease cohort. Used for pediatric transmission framing, acute seizure and status-epilepticus burden, altered mental status as a severe-disease predictor, EEG abnormality, abnormal MRI, SIADH, post-encephalitic epilepsy at follow-up, epileptiform EEG discharges as a long-term epilepsy predictor, long-term neurobehavioral abnormalities, and EEG/MRI diagnostic rows. |
| PMID:25956408 | Mouse olfactory-bulb capillary neuroinvasion study. Used as indirect model support for hematogenous LACV CNS entry through virus-induced olfactory-bulb capillary permeability rather than axonal transport from olfactory sensory neurons. |
| PMID:35891445 | Open full-text LACV Gc fusion-peptide study. Used as indirect animal-model support that LACV infects neurons in the brain and induces neuronal apoptosis after CNS entry. Its viral fusion-peptide mutant results were left out because this entry does not model vaccine attenuation determinants. |
| PMID:39079177 | 2024 review of pediatric La Crosse virus encephalitis. Used for age-dependent symptomatic susceptibility in children, and as a recency check for disease-severity predictors, EEG as an epilepsy-risk marker, and underrecognized long-term neurobehavioral sequelae. |

## Completeness cross-check

- The `epidemiology:` block now records the pediatric predisposition to symptomatic LACV disease described by the 2024 review.
- The ArboNET introductory snippets now use `quote_role: BACKGROUND`, while the 2003-2019 case counts and incidence values remain `PRIMARY_RESULT` evidence from the surveillance analysis.
- The pathophysiology graph now separates hematogenous olfactory-bulb neuroinvasion, LACV neuronal infection and apoptosis, viral meningoencephalitis, and SIADH-mediated hyponatremia.
- Post-encephalitic epilepsy, impaired executive functioning, and hemiparesis are wired downstream of neuronal infection and cell death to make the acute-to-chronic progression explicit.
- Altered mental status, EEG abnormality, and abnormal diffusion-weighted cerebral MRI morphology have phenotype rows from the 152-child LACV neuroinvasive disease cohort.
- The hyponatremia row now uses a cohort observation of SIADH rather than a three-word review sentence, fixing the snippet-length failure on the original PR.
- Diagnosis now includes electroencephalography and brain MRI rows in addition to serologic testing with neutralization confirmation.

## Deferred or bounded items

- Eastern chipmunk and eastern gray squirrel remain described as amplifying hosts in prose rather than species-bound host rows because the cached sources name them with common names only and the entry already binds the vector and the incidental human host.
- Asian invasive Aedes vectors remain out of the pathograph because the conserved human disease mechanism is mosquito-bite inoculation followed by CNS invasion; species-specific vector competence is an enzootic ecology detail.
- LACV Gc fusion-peptide mutants remain out of the structured mechanism because they inform viral neuroinvasiveness and live-attenuated vaccine design rather than a recurrent host pathophysiology step.

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 6 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.
