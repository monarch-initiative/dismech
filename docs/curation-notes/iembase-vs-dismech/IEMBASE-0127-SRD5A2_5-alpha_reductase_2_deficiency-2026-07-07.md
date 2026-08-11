# IEMbase 0127: SRD5A2-related Steroid 5-alpha-reductase type 2 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 127 |
| Nosology | 24.2.22.01 |
| Gene | SRD5A2 |
| External IDs | OMIM:264600; ORPHA:1331 |
| Generated mapping | CANDIDATE, medium confidence |
| Candidate DisMech targets | `46_XY_DSD_Due_to_5_Alpha_Reductase_2_Deficiency.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as SRD5A2-related steroid 5-alpha-reductase type 2
deficiency, with alternate labels pseudovaginal perineoscrotal hypospadias and
5alpha reductase deficiency. Treatability is marked unknown.

The characteristic biochemical rows are decreased DHT and increased
testosterone/dihydrotestosterone ratio. Clinical rows include a reduced
5-alpha/5-beta urinary metabolite ratio and virilization at puberty. No
treatment rows are listed.

## DisMech phenotype coverage

`46_XY_DSD_Due_to_5_Alpha_Reductase_2_Deficiency.yaml` is the correct local
target. It describes biallelic SRD5A2 loss of function, impaired
testosterone-to-DHT conversion, incomplete intrauterine masculinization in
46,XY individuals, and possible pubertal virilization.

The local phenotype coverage includes cryptorchidism, ambiguous male
genitalia, small or bifid scrotum, perineal hypospadias, micropenis, decreased
fertility, urogenital sinus anomaly, pubertal virilization, and voice change.
Biochemical coverage includes DHT and testosterone-to-DHT ratio. Treatments
include gonadectomy and orchiopexy/testis descent.

## Concordance and completeness

Judgement: accept the generated candidate as the correct mapping.

The candidate status appears to reflect lexical uncertainty rather than a real
scope mismatch. IEMbase and DisMech agree on SRD5A2, DHT deficiency, elevated
testosterone-to-DHT ratio, 46,XY undervirilization context, and pubertal
virilization. IEMbase adds the urinary 5-alpha/5-beta metabolite ratio, which
is useful diagnostic granularity not yet obvious in the local file.

## Curation actions

- Promote the generated candidate to a correct mapping to
  `46_XY_DSD_Due_to_5_Alpha_Reductase_2_Deficiency.yaml`.
- Consider adding the urinary 5-alpha/5-beta metabolite ratio as a
  subtype-specific diagnostic biochemical row.
- No new standalone disease target is needed.
