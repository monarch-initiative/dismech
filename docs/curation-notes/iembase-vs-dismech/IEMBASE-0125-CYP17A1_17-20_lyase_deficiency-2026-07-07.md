# IEMbase 0125: CYP17A1-related 17,20-Lyase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 125 |
| Nosology | 24.2.05.02 |
| Gene | CYP17A1 |
| External IDs | OMIM:202110; ORPHA:90796 |
| Generated mapping | UNMAPPED |
| Candidate DisMech targets | Partial mechanistic neighbor `Congenital_Adrenal_Hyperplasia.yaml#17A-OHD`; no standalone isolated 17,20-lyase deficiency target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as CYP17A1-related 17,20-lyase deficiency, with
alternate label P450c17 deficiency. Treatability is marked unknown.

The IEMbase signal is sparse. Characteristic biochemical rows include mildly
increased or normal-to-high 17-OH-progesterone. The only extracted clinical row
is cryptorchidism. No treatment rows are listed.

## DisMech phenotype coverage

`Congenital_Adrenal_Hyperplasia.yaml` includes a `17A-OHD` subtype and a
CYP17A1 17-hydroxylase/17,20-lyase deficiency mechanism. That local subtype is
appropriate for combined CYP17A1 deficiency with cortisol and sex-steroid
deficiency plus relative mineralocorticoid precursor excess.

The local CAH entry does not currently separate isolated 17,20-lyase deficiency
from 17-alpha-hydroxylase deficiency. Its CYP17A1 coverage is broader and more
mineralocorticoid/cortisol oriented than this IEMbase record.

## Concordance and completeness

Judgement: generated unmapped result is a partial false negative, but the local
target is only an umbrella/neighbor.

The best available local context is the CAH `17A-OHD` subtype, because it is
the only local CYP17A1 disease branch. However, IEMbase 0125 appears to be the
isolated 17,20-lyase branch rather than the full 17-alpha-hydroxylase/17,20-lyase
deficiency profile. The IEMbase signal of cryptorchidism and mild
17-OH-progesterone elevation does not match the fuller local CAH
mineralocorticoid-excess profile closely enough to call it complete coverage.

## Curation actions

- Do not create a hard standalone mapping to CAH without preserving the
  isolated 17,20-lyase nuance.
- Record `Congenital_Adrenal_Hyperplasia.yaml#17A-OHD` as partial local
  context until a CYP17A1 isolated 17,20-lyase subtype or entry exists.
- Consider future subtype splitting if DisMech needs to distinguish isolated
  17,20-lyase deficiency from combined CYP17A1 CAH.
