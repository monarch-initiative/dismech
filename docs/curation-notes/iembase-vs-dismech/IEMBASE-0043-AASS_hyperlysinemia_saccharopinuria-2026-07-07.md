# IEMbase 0043: AASS-related alpha-aminoadipic semialdehyde synthase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 43 |
| Nosology | 1.8.01.01 |
| Gene | AASS |
| External IDs | OMIM:268700 |
| Generated mapping | UNMAPPED |
| Candidate DisMech targets | None; fuzzy neighbor `Succinic_Semialdehyde_Dehydrogenase_Deficiency.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as autosomal recessive AASS-related
alpha-aminoadipic semialdehyde synthase deficiency, also named familial
hyperlysinemia or saccharopinuria. The cached subtype label is benign form.

The characteristic biochemical pattern is increased lysine in CSF, plasma, and
urine, with increased saccharopine in CSF, plasma, and urine. Homocitrulline and
N-acetyl-lysine are normal-to-increased in urine. The only clinical statement is
no clinical significance in childhood, and IEMbase lists no treatments.

## DisMech phenotype coverage

There is no local DisMech entry for primary AASS deficiency, familial
hyperlysinemia, or saccharopinuria.

The fuzzy neighbor `Succinic_Semialdehyde_Dehydrogenase_Deficiency.yaml` is a
false-positive lexical and metabolite-neighbor candidate. It is an ALDH5A1 GABA
catabolism disorder with succinic semialdehyde/GHB accumulation and a
neurologic phenotype, not an AASS lysine degradation disorder.

`DECR_Deficiency.yaml` also mentions impaired lysine degradation and
hyperlysinemia, but that entry is NADK2-related mitochondrial NADP(H)
deficiency with secondary DECR and lysine-pathway impairment, C10:2
acylcarnitine, and progressive encephalopathy. It is not a disease-level match
for primary AASS deficiency.

## Concordance and completeness

Judgement: true unmapped record. No current DisMech disorder captures the
primary AASS biochemical disorder.

The most important distinction is primary versus secondary hyperlysinemia.
IEMbase ID 43 is a largely benign AASS/saccharopine pathway record. The local
DECR entry uses hyperlysinemia as one component of a broader NADK2 mitochondrial
disorder, and the SSADH entry is a different aldehyde dehydrogenase/GABA
disorder.

## Curation actions

- Keep the record unmapped.
- Do not map to SSADH deficiency or DECR deficiency on the basis of
  semialdehyde or hyperlysinemia wording.
- If curated later, create a standalone AASS/familial hyperlysinemia entry with
  restrained clinical scope and the lysine/saccharopine biochemical signature.
