# IEMbase 0665: ECHS1-related mitochondrial short-chain enoyl-CoA hydratase 1 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 665 |
| Nosology | 1.3.01.01 |
| Nosology code | IEM0119 |
| Gene | ECHS1 |
| External IDs | OMIM:616277; ORPHA:255241 |
| Generated mapping | UNMAPPED; best candidate `Beta-Ketothiolase_Deficiency.yaml` |
| Candidate DisMech targets | `ECHS1_Deficiency.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive ECHS1-related mitochondrial short-chain
enoyl-CoA hydratase 1 deficiency, also labeled crotonase deficiency.

The biochemical signal includes increased plasma lactate and pyruvate, normal
lactate/pyruvate ratio, increased urinary
2,3-dihydroxy-2-methylbutyric acid, and increased urinary
S-(2-carboxypropyl)-cysteine. Clinical rows include neonatal hypotonia,
dystonia, seizures, apnea, brain MRI abnormalities, basal-ganglia lesions,
psychomotor regression, hypertrophic cardiomyopathy, possible hearing loss, and
possible optic atrophy.

## DisMech phenotype coverage

`ECHS1_Deficiency.yaml` is an exact local target. It models biallelic ECHS1
loss, mitochondrial short-chain enoyl-CoA hydratase/crotonase dysfunction,
Leigh or Leigh-like basal ganglia disease, developmental delay or regression,
dystonia, hypotonia, seizures, lactic acidosis, and toxic intermediates from
valine catabolism including methacrylyl-CoA and acryloyl-CoA.

The generated `Beta-Ketothiolase_Deficiency.yaml` candidate is a pathway-neighbor
false positive. It is adjacent in organic-acid and ketone/isoleucine metabolism,
but it is not the ECHS1 disease entity.

## Concordance and completeness

Judgement: false negative from stale generated mapping; current DisMech has an
exact high-concordance ECHS1 target.

IEMbase adds useful granularity for neonatal age-band timing, the normal
lactate/pyruvate-ratio row, cardiomyopathy, hearing loss, optic atrophy, apnea,
and specific urine metabolites. These should be reviewed as enrichment prompts
for `ECHS1_Deficiency.yaml`.

## Curation actions

- Resolve this IEMbase record to `ECHS1_Deficiency.yaml`.
- Do not use beta-ketothiolase deficiency as the target.
- Preserve the S-(2-carboxypropyl)-cysteine and
  2,3-dihydroxy-2-methylbutyric-acid biomarkers.
- Check whether cardiomyopathy, apnea, hearing loss, optic atrophy, and normal
  lactate/pyruvate ratio should be added or made more explicit locally.
