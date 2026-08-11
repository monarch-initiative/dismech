# IEMbase 0129: AR-related Androgen receptor deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 129 |
| Nosology | 24.2.23.01 |
| Gene | AR |
| External IDs | OMIM:300068; ORPHA:754 |
| Generated mapping | MAPPED, high confidence |
| Candidate DisMech targets | `Complete_Androgen_Insensitivity_Syndrome.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as AR-related androgen receptor deficiency, with
alternate labels testicular feminization, androgen insensitivity syndrome, and
AIS. Treatability is marked unknown.

The characteristic biochemical row is normal DHT. Clinical rows include absent
axillary hair, absent pubic hair, and absent uterus. No treatment rows are
listed.

## DisMech phenotype coverage

`Complete_Androgen_Insensitivity_Syndrome.yaml` is the generated local target.
It describes X-linked AR variants in 46,XY individuals with age-appropriate
androgen production but target-tissue androgen resistance, leading to female
external genitalia, absent or sparse pubic/axillary hair, primary amenorrhea,
absent Mullerian structures, and undescended testes.

The local phenotype coverage includes absent uterus, sparse or absent
axillary/pubic hair, primary amenorrhea, blind vagina, cryptorchidism, female
external genitalia in 46,XY individuals, elevated LH, increased testosterone,
increased estradiol, increased AMH, and germ-cell tumor risk. Treatments
include individualized gonadectomy, estrogen replacement, and vaginal dilation.

## Concordance and completeness

Judgement: correct current mapping, with a label-scope caveat.

The DisMech CAIS entry covers the specific IEMbase clinical signals of absent
uterus and absent terminal sexual hair well. It is also much richer for AR
mechanism, 46,XY phenotype, hormone profile, and management. IEMbase's normal
DHT row is a useful reminder that AIS is androgen-resistance physiology rather
than impaired DHT synthesis.

The IEMbase label "androgen receptor deficiency" and alternate "AIS" are broad;
if separate partial or mild AIS records are curated later, they should not be
forced into the complete AIS target without subtype review.

## Curation actions

- Keep `Complete_Androgen_Insensitivity_Syndrome.yaml` as the current target
  for this IEMbase record.
- Consider adding normal DHT as a differentiating biochemical row, especially
  relative to SRD5A2 deficiency.
- Preserve the broader AIS label-scope caveat for future subtype handling.
