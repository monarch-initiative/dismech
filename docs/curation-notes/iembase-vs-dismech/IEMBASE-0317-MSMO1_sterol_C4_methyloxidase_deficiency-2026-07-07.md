# IEMbase 0317: MSMO1-related sterol C4-methyloxidase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 317 |
| Nosology | 14.7.07.01 |
| Gene | MSMO1 |
| External IDs | OMIM:607545; ORPHA:488168 |
| Generated mapping | UNMAPPED |
| Candidate DisMech targets | Fuzzy candidate `Cerebrotendinous_Xanthomatosis.yaml` rejected |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents MSMO1-related sterol C4-methyloxidase deficiency, also
labeled SC4MOL, as an autosomal recessive sterol-biosynthesis disorder.
Characteristic rows include developmental delay, hypotonia, microcephaly, and
short stature.

Additional clinical rows include high-arched palate, cataract, psoriasiform
dermatitis, failure to thrive, frontal bossing, and osteoporosis. The
biochemical signal is sterol-focused: increased 4,4-dimethyl sterols and
4-methyl sterols in fibroblasts, lymphoblasts, and plasma. No treatment rows
are present in the cached record.

## DisMech phenotype coverage

The generated fuzzy candidate is `Cerebrotendinous_Xanthomatosis.yaml`, but
that is a pathway-neighbor false positive. The local CTX entry is CYP27A1
disease with cholestanol and bile-acid abnormalities, tendon xanthomas,
neuro-ophthalmic features, and chenodeoxycholic acid treatment.

There is no valid local MSMO1/SC4MOL disease target. CTX overlaps only at a
very broad sterol-metabolism level and should not be used for this record.

## Concordance and completeness

Judgement: true local disease gap.

IEMbase provides a compact but distinctive clinical and biochemical profile for
future curation: developmental delay, hypotonia, microcephaly, short stature,
cataract, psoriasiform dermatitis, failure to thrive, frontal bossing,
osteoporosis, and elevated methylated sterol intermediates across multiple
sample types.

## Curation actions

- Do not map this record to cerebrotendinous xanthomatosis.
- Add a standalone MSMO1/SC4MOL sterol C4-methyloxidase deficiency target if
  this disease is prioritized.
- Preserve the 4,4-dimethyl sterol and 4-methyl sterol biochemical rows as key
  differentiators from CYP27A1/CTX.
