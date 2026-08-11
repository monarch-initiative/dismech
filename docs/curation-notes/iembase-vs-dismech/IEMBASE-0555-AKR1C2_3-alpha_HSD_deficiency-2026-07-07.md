# IEMbase 0555: AKR1C2-related 3-alpha-hydroxysteroid dehydrogenase type 3 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 555 |
| Nosology | 24.2.2.01 |
| Gene | AKR1C2 |
| External IDs | OMIM:600450; ORPHA:443087 |
| Generated mapping | UNMAPPED; best candidate `Congenital_Adrenal_Hyperplasia.yaml#3B-HSD` |
| Candidate DisMech targets | No exact local target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents AKR1C2-related 3-alpha-hydroxysteroid dehydrogenase type 3
deficiency, with alternate labels aldoketoreductase 2 deficiency, backdoor
pathway defect, and AKR1C. The record is autosomal recessive, and treatability
is unknown. No treatment rows are listed.

The biochemical rows show markedly decreased urinary
androsterone/etiocholanolone ratio and normal plasma testosterone. Clinical
rows include ambiguous genitalia in 46,XY individuals, cryptorchidism, and
adolescent/adult virilization.

## DisMech phenotype coverage

No exact local AKR1C2 or backdoor androgen pathway target was found. The
generated `Congenital_Adrenal_Hyperplasia.yaml#3B-HSD` candidate is not a valid
match. That local subtype is HSD3B2-related adrenal steroidogenesis disease,
whereas IEMbase describes AKR1C2-related 3-alpha-hydroxysteroid dehydrogenase
type 3 deficiency with a diagnostic androsterone/etiocholanolone ratio.

Other local 46,XY DSD entries overlap at the phenotype level for ambiguous
genitalia, but they do not provide AKR1C2 gene or backdoor pathway coverage.

## Concordance and completeness

Judgement: true local disease gap; reject the CAH 3B-HSD candidate.

The IEMbase record is a gene-specific steroid backdoor pathway disorder with
AKR1C2 identity, urinary steroid-ratio directionality, 46,XY undervirilization,
cryptorchidism, and later virilization. It should not be treated as HSD3B2
congenital adrenal hyperplasia.

## Curation actions

- Keep this record unmapped until an AKR1C2 / 3-alpha-HSD type 3 deficiency
  target exists.
- Do not map to `Congenital_Adrenal_Hyperplasia.yaml#3B-HSD`.
- Preserve the androsterone/etiocholanolone ratio, normal testosterone,
  ambiguous genitalia in 46,XY, cryptorchidism, virilization, and backdoor
  pathway labels.
