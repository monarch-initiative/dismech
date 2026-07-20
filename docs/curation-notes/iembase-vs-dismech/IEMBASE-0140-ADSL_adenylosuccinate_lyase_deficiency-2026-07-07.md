# IEMbase 0140: ADSL-related Adenylosuccinate lyase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 140 |
| Nosology | 16.2.03.01 |
| Gene | ADSL |
| External IDs | OMIM:103050; OMIM:608222; ORPHA:46 |
| Generated mapping | MAPPED, high confidence |
| Candidate DisMech targets | `Adenylosuccinate_Lyase_Deficiency.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as ADSL-related adenylosuccinate lyase deficiency, with
alternate label adenylosuccinase deficiency and abbreviation ADSLD. Treatability
is marked unknown.

Characteristic biochemical rows include increased SAICA riboside in CSF,
plasma, and urine, and increased succinyladenosine in CSF, plasma, and urine.
The enzyme-testing row records markedly decreased RBC adenylosuccinate lyase
activity. Clinical rows include autism, cerebellar hypoplasia, cerebral
hypomyelination, epilepsy, hypotonia, and psychomotor delay. No treatment rows
are listed.

## DisMech phenotype coverage

`Adenylosuccinate_Lyase_Deficiency.yaml` is the correct local target. It models
ADSL deficiency as an ultra-rare autosomal recessive purine-metabolism disorder
with reduced adenylosuccinate lyase activity, impaired de novo purine synthesis
and purine nucleotide-cycle flux, and accumulation of the dephosphorylated ADSL
substrates SAICAr and S-Ado.

The local entry includes severe and mild subtypes plus a fatal neonatal form.
Phenotype coverage includes severe global developmental delay, intellectual
disability, seizures, generalized hypotonia, absent speech, autistic behavior,
microcephaly, craniofacial dysmorphism, cerebral white-matter MRI
abnormalities, cerebral atrophy, and cerebellar atrophy. Biochemical coverage
includes reduced ADSL activity, increased succinylpurines, and
succinyladenosine. Treatments include seizure-directed supportive care and
investigational allopurinol therapy.

## Concordance and completeness

Judgement: correct mapping with strong local coverage.

IEMbase and DisMech agree on ADSL deficiency, succinylpurine accumulation,
reduced enzyme activity, epilepsy, hypotonia, autism/autistic behavior, white
matter involvement, and psychomotor/developmental delay. DisMech is richer for
subtypes, mechanism, dysmorphism, broader neurologic outcomes, and treatment
context. IEMbase adds compartment-specific SAICA riboside and succinyladenosine
rows across CSF, plasma, and urine, plus cerebellar hypoplasia wording that
should be reviewed against the local cerebellar atrophy representation.

## Curation actions

- Keep `Adenylosuccinate_Lyase_Deficiency.yaml` as the canonical target.
- Consider adding explicit SAICA riboside rows by specimen if the biochemical
  panel is expanded.
- Review cerebellar hypoplasia versus cerebellar atrophy wording before adding
  a new structural brain phenotype.
