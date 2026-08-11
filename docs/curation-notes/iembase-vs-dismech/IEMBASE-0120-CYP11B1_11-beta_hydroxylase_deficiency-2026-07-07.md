# IEMbase 0120: CYP11B1-related 11-beta-Hydroxylase type 1 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 120 |
| Nosology | 24.2.02.01 |
| Gene | CYP11B1 |
| External IDs | OMIM:202010; ORPHA:418 |
| Generated mapping | MAPPED, high confidence |
| Candidate DisMech targets | `Congenital_Adrenal_Hyperplasia.yaml#11B-OHD` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as CYP11B1-related 11-beta-hydroxylase type 1
deficiency, with alternate labels congenital adrenal hyperplasia and CAH.
Treatability is marked unknown.

The characteristic biochemical rows include increased ACTH, low potassium, high
sodium, increased 11-deoxycortisol, mildly increased 17-OH-progesterone,
increased androgens, and increased deoxycorticosterone. Clinical rows include
accelerated growth, testicular adrenal rest tumors, and varying degrees of
genital ambiguity in 46,XX individuals. No treatment rows are listed.

## DisMech phenotype coverage

`Congenital_Adrenal_Hyperplasia.yaml` includes an `11B-OHD` subtype for
CYP11B1-related congenital adrenal hyperplasia. The subtype description covers
cortisol deficiency, adrenal androgen excess, and accumulation of
mineralocorticoid precursors. The broader CAH entry also captures ACTH-driven
adrenal hyperplasia and androgen excess, ambiguous genitalia/46,XX
virilization, hypertension, infertility, and testicular adrenal rest tumors.

The local entry is still mostly optimized around 21-hydroxylase deficiency, so
its biochemical section is less granular for CYP11B1-specific steroid
precursors than the IEMbase record.

## Concordance and completeness

Judgement: correct mapping, with subtype resolution needed.

The generated file-level CAH mapping is correct, but the manual target should
resolve to the `11B-OHD` subtype rather than to undifferentiated CAH. DisMech
captures the central CYP11B1 mechanism and the major androgen/mineralocorticoid
precursor phenotype. IEMbase adds useful diagnostic resolution for
11-deoxycortisol, deoxycorticosterone, potassium, sodium, ACTH, and mild
17-OH-progesterone elevation.

## Curation actions

- Keep `Congenital_Adrenal_Hyperplasia.yaml#11B-OHD` as the target.
- Consider adding subtype-specific biochemical rows for 11-deoxycortisol,
  deoxycorticosterone, ACTH, sodium, potassium, and mild
  17-OH-progesterone elevation.
- Preserve testicular adrenal rest tumors and 46,XX genital ambiguity as shared
  CAH phenotypes, but make their 11B-OHD relevance clear where possible.
