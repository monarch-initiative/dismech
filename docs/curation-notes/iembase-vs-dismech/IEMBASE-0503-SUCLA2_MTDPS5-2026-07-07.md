# IEMbase 0503: SUCLA2-related mitochondrial DNA depletion syndrome type 5

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 503 |
| Nosology | 5.2.04.01 |
| Gene | SUCLA2 |
| External IDs | OMIM:612073; ORPHA:1933 |
| Generated mapping | CANDIDATE; MEDIUM; `Mitochondrial_DNA_Depletion_Syndrome_7.yaml` |
| Candidate DisMech targets | `Mitochondrial_DNA_Depletion_Syndrome_7.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive SUCLA2-related ATP-specific
succinyl-CoA synthetase beta-subunit deficiency as mitochondrial DNA depletion
syndrome type 5, encephalomyopathic with or without methylmalonic aciduria. No
treatments are listed. Biochemical rows include increased urinary
C4-DC methylmalonylcarnitine and succinylcarnitine, normal-to-increased
transaminases, increased urinary methylmalonic acid, increased plasma lactate,
and increased lactate/pyruvate ratio. Clinical rows include neurological
symptoms, axial hypotonia, psychomotor retardation, sensorineural deafness,
dystonia, choreoathetosis, failure to thrive, feeding difficulties, lactic
acidosis, Leigh syndrome, peripheral neuropathy, and pyramidal signs.

## DisMech phenotype coverage

`Mitochondrial_DNA_Depletion_Syndrome_7.yaml` is not the correct target. The
local entry is MTDPS7 / infantile-onset spinocerebellar ataxia caused by TWNK
variants, with impaired Twinkle helicase function, tissue-specific mtDNA
depletion, respiratory-chain deficiency, ataxia, hypotonia, athetosis,
ophthalmoplegia, sensorineural hearing loss, neuropathy, optic atrophy,
autonomic dysfunction, hypogonadism, epilepsy, and a hepatocerebral subtype.

The local MTDPS7 phenotype overlaps IEMbase in mtDNA depletion, neurologic
involvement, deafness, hypotonia, dystonia/athetosis-adjacent movement
features, neuropathy, and transaminase context. It does not model SUCLA2,
succinyl-CoA synthetase deficiency, MTDPS5, methylmalonic aciduria,
succinylcarnitine/methylmalonylcarnitine elevations, or the SUCLA2-specific
encephalomyopathic disease identity.

## Concordance and completeness

Judgement: false-positive candidate; true SUCLA2/MTDPS5 local gap.

The candidate was probably selected through shared "mitochondrial DNA depletion
syndrome" vocabulary. IEMbase's record and DisMech's candidate are adjacent
within the mtDNA-depletion syndrome family, but the gene, primary molecular
defect, biochemical signature, and numbered subtype differ.

## Curation actions

- Do not map this record to `Mitochondrial_DNA_Depletion_Syndrome_7.yaml`.
- Track SUCLA2-related MTDPS5 / succinyl-CoA synthetase beta-subunit deficiency
  as a local curation gap.
- Preserve IEMbase prompts for methylmalonic aciduria, C4-DC
  methylmalonylcarnitine/succinylcarnitine, lactate/pyruvate ratio, Leigh
  syndrome, deafness, dystonia, hypotonia, and failure to thrive for a future
  exact entry.
