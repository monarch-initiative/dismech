# IEMbase 0024: MAT1A-related methionine adenosyltransferase I-III deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 24 |
| Nosology | 1.5.01.01 |
| Gene | MAT1A |
| External IDs | OMIM:250850 |
| Generated mapping | MAPPED by `alias_exact:methionine adenosyltransferase i iii deficiency` |
| Candidate DisMech targets | `Inborn_Disorder_of_Methionine_Cycle_and_Sulfur_Amino_Acid_Metabolism.yaml#MAT I/III deficiency` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase presents MAT I/III deficiency as a hypermethioninemia/SAM-synthesis
disorder. Characteristic clinical signals are cabbage-like breath odor from
dimethylsulfide and vacuolating myelopathy. Additional neurologic findings
include cognitive dysfunction, developmental delay, language difficulties,
demyelination, dystonia, tremor, dysdiadochokinesis, dysmetria, headache,
nystagmus, and increased tendon reflexes.

The biochemical signature is high plasma methionine, high
methionine-to-cystathionine and methionine-to-total-homocysteine ratios, elevated
urinary methionine sulfoxide, normal S-adenosylhomocysteine, and low-to-normal
S-adenosylmethionine. IEMbase lists no treatment rows for this record.

## DisMech phenotype coverage

The generated subtype mapping is correct. DisMech models MAT I/III deficiency
under the methionine-cycle and sulfur amino-acid metabolism umbrella, with a
MAT1A subtype, persistent isolated hypermethioninemia, impaired
S-adenosylmethionine synthesis, risk of cerebral white-matter injury, delayed
language development, and therapies including low-methionine diet,
S-adenosylmethionine/ademetionine supplementation, and liver transplantation for
severe refractory disease.

## Concordance and completeness

Judgement: correct mapping with good biochemical concordance, but IEMbase has
more granular neurologic phenotype detail.

DisMech captures the central mechanism and the core severe phenotype of
hypermethioninemia-associated white-matter injury. IEMbase adds the
cabbage-like odor, vacuolating myelopathy, cerebellar/extrapyramidal signs,
nystagmus, hyperreflexia, and several useful ratio markers. Conversely, DisMech
is more complete for therapy and mechanism.

## Curation actions

- Keep the generated subtype mapping.
- Consider adding the odor, myelopathy, and movement/cerebellar signs to the
  MAT I/III subtype if supported by evidence.
- Consider whether IEMbase ratio markers and urinary methionine sulfoxide should
  be added as subtype-specific biochemical markers.
