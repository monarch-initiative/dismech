# Benign Familial Infantile Epilepsy Deep Research Fallback

## Provider Attempts

- `timeout 75s just research-disorder falcon Benign_Familial_Infantile_Epilepsy`
  - Result: timed out with `Recipe research-disorder was terminated by signal 15`.
- `timeout 75s just research-disorder openai Benign_Familial_Infantile_Epilepsy`
  - Result: timed out with `Recipe research-disorder was terminated by signal 15`.

No provider-generated research artifact was available within the bounded
window. The YAML therefore was curated directly from MONDO/ORPHA structured
records and PubMed abstracts cached via `just fetch-reference`.

## Evidence-backed curation scope

The entry integrates the following deterministic sources:

- MONDO terms for the disease and its molecular subtypes:
  - `MONDO:0017615` benign familial infantile epilepsy (root).
  - `MONDO:0011593` seizures, benign familial infantile, 2 (PRRT2-related).
  - `MONDO:0011178` infantile convulsions and choreoathetosis (ICCA).
  - `MONDO:0011904` seizures, benign familial infantile, 3 (SCN2A-related BFNIS).
  - `MONDO:0014903` seizures, benign familial infantile, 5 (SCN8A-related).
- HGNC gene identifiers: `hgnc:30500` PRRT2, `hgnc:10588` SCN2A,
  `hgnc:10596` SCN8A.
- PubMed caches (six PMIDs):
  - `PMID:22243967` PRRT2 discovery paper establishing PRRT2 as the major
    BFIE gene and the shared molecular cause of BFIE and ICCA.
  - `PMID:23077018` PRRT2 phenotypic-spectrum cohort confirming
    PRRT2 mutation frequencies (>80% BFIE, >90% ICCA) and the afebrile,
    autosomal-dominant infantile-seizure clinical definition.
  - `PMID:23343561` review of PRRT2 across paroxysmal neurological
    disorders, summarising the truncating/haploinsufficiency mutation
    mechanism and SNAP-25 interaction.
  - `PMID:27052163` mechanistic cellular study showing PRRT2 loss
    impairs Ca2+-dependent synchronous synaptic vesicle release and
    SNAP-25/synaptotagmin 1/2 interactions.
  - `PMID:12243921` original identification of SCN2A as the gene
    underlying benign familial neonatal-infantile seizures (BFNIS).
  - `PMID:38160512` Australian long-term cohort of self-limited
    familial neonatal/infantile epilepsy reporting genetic yields
    (PRRT2, KCNQ2, SCN2A, SCN8A), seizure-recurrence rates, late-onset
    PKD and hemiplegic migraine, antiseizure-medication burden, and
    Vineland-3 adaptive function outcomes.

## Integrated Literature Synthesis

BFIE is an autosomal-dominant, self-limited focal epilepsy of infancy.
PMID:22243967 (Heron et al., 2012) established PRRT2 as the dominant
gene, identifying heterozygous truncating mutations in 14/17 BFIE
families (82%) and in 5/6 ICCA families (83%) and noting the
pleiotropy of PRRT2 across age (infancy vs. later childhood) and
anatomical substrate (cortex vs. basal ganglia). PMID:23077018
(Ono et al., 2012) independently replicated PRRT2 mutation
frequencies (>80% BFIE, >90% ICCA), provided the canonical clinical
definition (afebrile autosomal-dominant infantile seizures with
onset around 6 months of age), and showed PRRT2 mutations do not
extend to other infantile epilepsy syndromes. PMID:23343561
(Ebrahimi-Fakhari et al., 2015) reviews the unifying molecular
mechanism: the vast majority of PRRT2 variants are truncating and
predicted to cause haploinsufficiency at the presynaptic
SNAP-25/SNARE machinery, explaining the shared pathogenesis of BFIE,
ICCA, and paroxysmal kinesigenic dyskinesia (PKD). PMID:27052163
(Valente et al., 2016) provides the direct cellular evidence:
PRRT2 is enriched at presynaptic terminals, interacts with SNAP-25
and synaptotagmin 1/2, and its loss decreases synapse number,
increases docked synaptic vesicles at rest, and severely impairs
synchronous Ca2+-dependent neurotransmitter release.

Beyond PRRT2, PMID:12243921 (Heron et al., 2002) identified SCN2A
missense variants as the cause of benign familial neonatal-infantile
seizures (BFNIS), a clinically intermediate syndrome bridging the
neonatal and infantile onset windows. PMID:38160512 (Howell et al.,
2024) provides the most comprehensive long-term cohort: 14/15 of
their Australian self-limited familial epilepsy families had a
genetic diagnosis, with the gene mix PRRT2 (n=4), KCNQ2 (n=3),
SCN2A (n=4), and SCN8A (n=2). The same cohort reports that 10/50
individuals had later seizure recurrence (median 11.8-12.8 years
after the last infantile seizure), that paroxysmal kinesigenic
dyskinesia (5 individuals, 4 families) and hemiplegic migraine
(8 individuals, 3 families) emerged later in life, that the
majority (82%) of carriers had average Vineland-3 adaptive
functioning, and that global developmental delay was associated
with older age at last seizure, longer epilepsy duration, and a
higher number of antiseizure medications.

## Curation Notes

- The "Seizure Clusters" phenotype uses the generic HP:0001250 (Seizure)
  with `temporality: RECURRENT`. The more specific HP:0033349
  (Seizure cluster) was considered but is classified under HP:0012823
  (Clinical modifier) rather than HP:0000118 (Phenotypic abnormality),
  so it is not reachable from the `PhenotypeTerm` enum source nodes.
  HP:0031796 (Recurrent), the direct parent of HP:0033349, is the
  meaning of the `RECURRENT` temporality enum value, so this
  composition preserves the clinical semantics within the schema.
- Treatment evidence is intentionally `PARTIAL`: PMID:38160512 reports
  ASM burden in this cohort but does not establish first-line agent
  efficacy. Carbamazepine and oxcarbazepine are captured as
  `therapeutic_agent` CHEBI entries based on standard pediatric
  epilepsy clinical practice for BFIE, while the formal evidence link
  is anchored to PMID:38160512's documentation of ASM use.
- KCNQ2-related BFNS was intentionally excluded from `has_subtypes`
  because KCNQ2-associated benign familial neonatal seizures are a
  distinct nosological entity from BFIE proper; PMID:38160512 includes
  KCNQ2 carriers in its self-limited familial epilepsy cohort but
  they are not BFIE.
