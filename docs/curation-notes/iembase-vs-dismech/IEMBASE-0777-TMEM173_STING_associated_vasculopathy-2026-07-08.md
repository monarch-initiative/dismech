# IEMbase 0777: TMEM173-related STING superactivity

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 777 |
| Nosology | 16.3.09.01 |
| Nosology code | IEM0034 |
| Gene | TMEM173 |
| External IDs | OMIM:615934; ORPHA:481662 |
| Generated mapping | MAPPED; `STING_Associated_Vasculopathy_with_Onset_in_Infancy.yaml` |
| Candidate DisMech targets | `STING_Associated_Vasculopathy_with_Onset_in_Infancy.yaml` |
| Review date | 2026-07-08 |

## IEMbase phenotype signal

IEMbase labels this autosomal dominant record as TMEM173-related STING
superactivity, with alternate names SAVI and dominant familial chilblain lupus
type. The source signal includes recurrent infections, fever, interstitial lung
disease, acral violaceous plaques and nodules, chilblain lesions, ulcerative
lesions with infarcts and gangrene, nail dystrophy or loss, lymphadenopathy,
arthralgia, nasal septum perforation, malar flush, arterial and pulmonary
hypertension, B lymphopenia, elevated CRP/ESR, elevated IgG, autoantibodies,
and a strong interferon-stimulated gene signature.

## DisMech phenotype coverage

`STING_Associated_Vasculopathy_with_Onset_in_Infancy.yaml` is the correct local
target. It models activating STING1/TMEM173 variants, constitutive cGAS/STING
and type I interferon signaling, endothelial activation and small-vessel
vasculopathy, progressive interstitial lung disease/fibrosis, and JAK inhibitor
therapy. Local phenotypes include interstitial lung disease, skin vasculopathy,
failure to thrive, polyarticular arthritis, livedo reticularis, and nasal
septum perforation.

## Concordance and completeness

Judgement: exact disease-level coverage; generated mapping should be accepted.

The disease identity, gene, inheritance, interferonopathy mechanism, ILD, skin
vasculopathy, arthritis/arthralgia, and nasal involvement are concordant.
DisMech is strong for the central STING mechanism and therapeutic context.
IEMbase is more granular for inflammatory and immune-laboratory features and
for cutaneous complications: CRP/ESR, IgG, autoantibodies, B lymphopenia,
recurrent infections, lymphadenopathy, nail dystrophy/loss, acral plaques, and
ulceration/gangrene are not all separately represented in the local phenotype
set.

## Curation actions

- Keep `STING_Associated_Vasculopathy_with_Onset_in_Infancy.yaml` as exact
  coverage for IEMbase 0777.
- Consider adding explicit recurrent infections, B lymphopenia, inflammatory
  marker elevation, lymphadenopathy, nail dystrophy/loss, and ulcerative
  gangrenous vasculopathy if supported by existing evidence.
- Preserve TMEM173/STING1 naming equivalence: IEMbase uses TMEM173, while the
  local HGNC label is STING1.
