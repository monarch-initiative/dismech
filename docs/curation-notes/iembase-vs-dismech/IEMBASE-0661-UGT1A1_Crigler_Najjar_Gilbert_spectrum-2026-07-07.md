# IEMbase 0661: UGT1A1-related UDP-glucuronosyltransferase A1 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 661 |
| Nosology | 17.2.01.01 |
| Nosology code | IEM0802 |
| Gene | UGT1A1 |
| External IDs | OMIM:218800; OMIM:606785; ORPHA:205 |
| Generated mapping | MAPPED to `Gilberts_Syndrome.yaml` |
| Candidate DisMech targets | `Gilberts_Syndrome.yaml` covers mild Gilbert physiology only |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive UGT1A1-related
UDP-glucuronosyltransferase A1 deficiency with both severe Crigler-Najjar
syndrome and milder Gilbert syndrome named as alternate labels.

Clinical rows include persistent jaundice across all ages, neonatal temperature
instability, abnormal eye movements, convulsions, and hearing loss. The
convulsion row increases from optional neonatal involvement to strong
childhood/adolescent involvement, consistent with bilirubin neurotoxicity scope.
The biochemical row includes increased plasma bilirubin.

## DisMech phenotype coverage

`Gilberts_Syndrome.yaml` is a correct target for the mild Gilbert end of the
UGT1A1 spectrum. It models reduced UGT1A1 activity, impaired bilirubin
glucuronidation, mild unconjugated hyperbilirubinemia, intermittent jaundice,
UGT1A1*28 and UGT1A1*6 genetics, and pharmacogenomic irinotecan relevance. It
also references Crigler-Najjar type II versus Gilbert bilirubin concentrations
in supporting evidence.

However, the local entry is explicitly a benign Gilbert syndrome entry. It does
not model Crigler-Najjar syndrome as a disease entity, profound neonatal
unconjugated hyperbilirubinemia, bilirubin encephalopathy/kernicterus, abnormal
eye movements, seizures/convulsions, hearing loss, temperature instability, or
Crigler-Najjar-specific treatment intensity such as phototherapy or liver
transplantation.

## Concordance and completeness

Judgement: partial mapping only. Accept `Gilberts_Syndrome.yaml` for the mild
Gilbert component, but do not treat it as complete coverage for the IEMbase
UGT1A1 deficiency spectrum.

The generated high-confidence alias match is understandable because IEMbase
lists Gilbert syndrome, but the same row also names severe Crigler-Najjar
syndrome. A single Gilbert entry under-covers the severe bilirubin-neurotoxicity
phenotype package.

## Curation actions

- Keep `Gilberts_Syndrome.yaml` as the mild-spectrum target.
- Add or map a separate Crigler-Najjar syndrome target if DisMech wants full
  UGT1A1 deficiency spectrum coverage.
- Preserve bilirubin, neonatal temperature instability, abnormal eye movements,
  convulsions/seizures, hearing loss, and persistent jaundice prompts.
- Avoid claiming full row-level completeness from the Gilbert mapping alone.
