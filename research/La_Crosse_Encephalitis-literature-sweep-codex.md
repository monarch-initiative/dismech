# La Crosse encephalitis literature sweep

This curation sweep checked recent La Crosse virus reviews, the 2003-2019 U.S.
ArboNET surveillance analysis, a contemporary pediatric neuroinvasive cohort,
and experimental neuroinvasion work before creating
`kb/disorders/La_Crosse_Encephalitis.yaml`.

## Sources used

- **PMID:35755222** — open full-text overview of La Crosse virus disease. Used
  for the virus identity, endemic U.S. distribution, the clinical spectrum of
  febrile illness, meningitis, and encephalitis, the frequent acute symptoms,
  lymphocytic CSF pleocytosis, possible hyponatremia and cerebral edema,
  serologic diagnosis with plaque-reduction neutralization confirmation, absence
  of recommended antivirals, supportive care, and long-term neurologic sequelae.
- **PMID:34280142** — U.S. ArboNET surveillance analysis of human LACV disease
  from 2003-2019. Used for the Aedes/small-mammal enzootic cycle, humans as
  incidental dead-end hosts, the neuroinvasive/non-neuroinvasive case mix,
  encephalitis and meningitis counts, and the underreporting caveat for passive
  arboviral surveillance.
- **PMID:35607778** — 152-child single-center cohort and long-term
  neurobehavioral follow-up study. Used for pediatric transmission framing,
  acute seizure and status epilepticus frequencies, altered mental status as a
  severe-disease predictor, SIADH, EEG and MRI abnormalities, epilepsy at
  follow-up, EEG as a long-term epilepsy predictor, and long-term
  neurobehavioral sequelae.
- **PMID:25956408** — mouse olfactory-bulb capillary neuroinvasion study. Used
  as indirect model support for hematogenous LACV CNS entry through
  olfactory-bulb capillary leak.
- **PMID:39079177** — 2024 review of La Crosse virus encephalitis in children.
  Used for age-dependent symptomatic susceptibility in children, and as a
  recency check for severity predictors, EEG as an epilepsy-risk marker, and
  underrecognized neurobehavioral sequelae.
- **PMID:35891445** — open full-text study of LACV Gc fusion-peptide mutants.
  Used as indirect model support for LACV neuronal infection and apoptosis
  after CNS entry; the structured entry did not need a separate
  glycoprotein-fusion determinant node.

## Lump/split decision

`stubs/La_Crosse_Encephalitis.yaml` carries no MONDO descendants and lists
`Bunyaviridae infectious disease` and `mosquito-borne viral encephalitis` as
parents, so it was curated as a leaf mosquito-borne viral encephalitis.

The infectious agent is bound to `NCBITaxon:11577` La Crosse virus, and the
primary vector descriptor uses `NCBITaxon:7162` with the display term
*Aedes triseriatus*. NCBI Taxonomy labels this homotypic species
*Ochlerotatus triseriatus*, while the LACV clinical literature continues to use
*Aedes triseriatus*. Chipmunks and gray squirrels are carried in prose rather
than bound to a broad squirrel/chipmunk ancestor because the sources did not
require that extra host granularity for human disease.

## Exclusions

- **Asian tiger and Asian bush mosquitoes** were left out of `agent_life_cycle`.
  Experimental vector-competence and emergence claims exist, but the review and
  surveillance sources still identify *Aedes triseriatus* as the primary native
  vector for the core life cycle.
- **Gc fusion-peptide determinants** were not modeled as their own
  pathophysiology node. PMID:35891445 shows the fusion peptide modulates
  neuroinvasion after peripheral inoculation in mice, but the main conserved
  entry can explain human meningoencephalitis with the higher-level
  mosquito-bite and hematogenous-neuroinvasion nodes.
- **Acute flaccid paralysis** was excluded as a phenotype. The overview notes
  that one jurisdiction's apparent acute-flaccid-paralysis cases were later
  reinterpreted as upper motor neuron weakness from brain lesions.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 2 |
| Resolved | 2 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |

Every term resolved, and every label the report gave matched.

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
