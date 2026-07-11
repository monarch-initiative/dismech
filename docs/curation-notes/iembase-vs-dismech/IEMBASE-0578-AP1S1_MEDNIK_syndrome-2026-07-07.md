# IEMbase 0578: AP1S1-related MEDNIK syndrome

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 578 |
| Nosology | 22.1.04.01 |
| Gene | AP1S1 |
| External IDs | OMIM:609313; ORPHA:171851 |
| Generated mapping | MAPPED; `MEDNIK_syndrome.yaml` |
| Candidate DisMech targets | `MEDNIK_syndrome.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents AP1S1-related MEDNIK syndrome, with alternate label mental
retardation, enteropathy, deafness, peripheral neuropathy, ichthyosis, and
keratoderma. The record is autosomal recessive, classified under disorders of
copper metabolism, flagged as treatable, and lists zinc acetate.

Biochemical rows include increased plasma ASAT/ALAT, increased plasma bile
acids by enzyme assay, decreased serum ceruloplasmin, decreased serum copper,
and increased plasma very-long-chain fatty acids. Clinical rows add cerebral
atrophy on MRI, hyperkeratosis, and intestinal pseudo-obstruction.

## DisMech phenotype coverage

`MEDNIK_syndrome.yaml` is the correct local target. It models autosomal
recessive AP1S1 disease with adaptor-protein trafficking dysfunction,
mislocalization of copper pumps, copper-handling defects, intestinal barrier
dysfunction, and the core MEDNIK phenotype of enteropathy, deafness, peripheral
neuropathy, ichthyosis, keratoderma, neurodevelopmental involvement, and liver
copper overload. Zinc acetate therapy is also represented.

## Concordance and completeness

Judgement: correct exact mapping.

IEMbase and DisMech agree on the AP1S1 identity, recessive inheritance, MEDNIK
syndrome label, copper-metabolism framing, enteropathy, deafness, peripheral
neuropathy, ichthyosis/keratoderma, and zinc treatment signal. DisMech is
stronger for the trafficking and copper-pump mechanism.

IEMbase adds useful import prompts for low serum copper and ceruloplasmin,
ASAT/ALAT and bile-acid abnormalities, very-long-chain fatty acids, cerebral
atrophy, hyperkeratosis wording, and intestinal pseudo-obstruction.

## Curation actions

- Keep `MEDNIK_syndrome.yaml` as the exact DisMech target.
- Review the IEMbase serum copper/ceruloplasmin, ASAT/ALAT, bile-acid, and
  very-long-chain fatty-acid rows against the local hepatic/copper mechanism.
- Consider adding cerebral atrophy, hyperkeratosis, and intestinal
  pseudo-obstruction only after source-level confirmation.
