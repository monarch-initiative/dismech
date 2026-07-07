# IEMbase 0521: SLC1A3-related glutamate aspartate transporter deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 521 |
| Nosology | 17.2.04.02 |
| Gene | SLC1A3 |
| External IDs | OMIM:612656; ORPHA:209967 |
| Generated mapping | CANDIDATE; `CACNA1A_Related_Disorder.yaml#Episodic Ataxia Type 2` |
| Candidate DisMech targets | No exact local target found |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as SLC1A3-related glutamate aspartate transporter
deficiency, with alternate labels EAAT1 glutamate transporter defect, episodic
ataxia type 6, and EA6. No biochemical or treatment rows are listed.

The clinical signal is neurologic and paroxysmal: ataxia, epilepsy, hemiplegic
migraine, interictal nystagmus, nausea, photophobia, and vomiting.

## DisMech phenotype coverage

No exact local SLC1A3/EAAT1/EA6 target was found. The generated candidate
`CACNA1A_Related_Disorder.yaml#Episodic Ataxia Type 2` is a plausible
phenotype-neighbor but not a valid disease target. The local CACNA1A entry
models P/Q-type calcium channel disease, with EA2, FHM1, SCA6, and DEE42
subtypes. It shares episodic ataxia, migraine, nystagmus, and epilepsy
vocabulary, but not the SLC1A3 glutamate/aspartate transporter gene or EAAT1
mechanism.

## Concordance and completeness

Judgement: generated candidate is a false positive; SLC1A3/EA6 is a true local
gap.

This IEMbase record should not be collapsed into CACNA1A episodic ataxia. The
shared symptoms are enough for differential context, but the gene and mechanism
are different.

## Curation actions

- Track SLC1A3-related EAAT1 deficiency / episodic ataxia type 6 as a local gap.
- Reject `CACNA1A_Related_Disorder.yaml#Episodic Ataxia Type 2` as an exact
  mapping while retaining it as episodic-ataxia differential context.
- Seed a future entry with SLC1A3/EAAT1 transporter dysfunction, ataxia,
  hemiplegic migraine, epilepsy, interictal nystagmus, nausea, photophobia, and
  vomiting.
