# IEMbase 0036: ABAT-related GABA transaminase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 36 |
| Nosology | 23.2.05.01 |
| Gene | ABAT |
| External IDs | OMIM:137150; OMIM:613163 |
| Generated mapping | UNMAPPED; best fuzzy candidate `Generalized_Epilepsy_with_Febrile_Seizures_Plus.yaml` |
| Candidate DisMech targets | none currently valid |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents ABAT deficiency as a GABA-catabolism disorder upstream of
succinic semialdehyde dehydrogenase. Biochemical markers include increased GABA
by MRS, increased free CSF GABA, increased CSF beta-alanine, increased CSF
homocarnosine, and increased growth hormone.

The clinical signal is a severe developmental and epileptic encephalopathy:
psychomotor delay, seizures, feeding difficulties, hypotonia, lethargy,
high-pitched cry, spasticity, increased tendon reflexes, accelerated growth, and
diffusion restriction in the internal capsule, external capsule, and
subcortical white matter on MRI. IEMbase lists flumazenil as a pharmacologic
intervention.

## DisMech phenotype coverage

There is no current DisMech entry or subtype for ABAT-related GABA transaminase
deficiency. The generated fuzzy candidate,
`Generalized_Epilepsy_with_Febrile_Seizures_Plus.yaml`, should be rejected.
GEFS+ is a familial epilepsy/channelopathy spectrum involving sodium-channel,
GABA-A receptor subunit, and synaptic genes such as GABRD; it is not an ABAT
enzyme defect.

`Succinic_Semialdehyde_Dehydrogenase_Deficiency.yaml` is a pathway neighbor in
GABA catabolism, but it is not the same disease. SSADH deficiency is caused by
ALDH5A1 and has GHB/4-hydroxybutyrate accumulation as a core diagnostic signal,
whereas ABAT deficiency is anchored by GABA transaminase loss and elevated GABA,
homocarnosine, beta-alanine, and growth hormone.

## Concordance and completeness

Judgement: generated unmapped status is correct. The GEFS+ candidate is a
misleading GABA-related lexical/pathway match, not a disease-entity match.

IEMbase provides a strong future curation outline for ABAT deficiency, including
the distinctive biochemical panel, growth phenotype, and early MRI diffusion
restriction pattern. DisMech currently lacks valid local phenotype coverage for
this disease.

## Curation actions

- Do not map this record to GEFS+ or to SSADH deficiency.
- Consider ABAT deficiency as a future GABA-catabolism curation target adjacent
  to, but separate from, SSADH deficiency.
- If curated, preserve the flumazenil treatment note and the growth hormone /
  accelerated-growth signal because these help distinguish ABAT deficiency from
  other epilepsy-metabolism disorders.
