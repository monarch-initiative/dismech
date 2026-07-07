# IEMbase 0058: AUH-related 3-methylglutaconic aciduria type I

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 58 |
| Nosology | 1.2.12.01 |
| Gene | AUH |
| External IDs | OMIM:250950 |
| Generated mapping | UNMAPPED; best fuzzy candidate `Glutaryl-CoA_Dehydrogenase_Deficiency.yaml` |
| Candidate DisMech targets | No valid local target found |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as autosomal recessive AUH-related
3-methylglutaconyl-CoA hydratase deficiency, also called
3-methylglutaconic aciduria type I or MGA1. Treatability is marked yes, but no
specific treatment rows are present in the cached record.

The biochemical signal includes high C5-OH acylcarnitine, high C6-unsaturated
acylcarnitine, normal-high esterified carnitine, low-normal free carnitine,
low fibroblast 3-methylglutaconyl-CoA hydratase activity, increased urinary
3-hydroxyisovaleric acid, increased urinary 3-methylglutaconic acid, increased
urinary 3-methylglutaric acid, and possible transaminase, creatine kinase,
ammonia, glucose, and MRS N-acetylaspartate abnormalities.

The characteristic clinical signal includes ataxia, intellectual disability,
leukoencephalopathy, neurological regression, and psychomotor delay. Additional
features include athetosis, basal ganglia lesions, cerebellar abnormalities,
cerebral atrophy, dementia, fits, hepatomegaly, hypoglycemia, liver dysfunction,
metabolic acidosis, neonatal seizures, nystagmus, optic atrophy, febrile
seizures, limb spasticity, thrombocytopenia, and white-matter MRI changes.

## DisMech phenotype coverage

No valid local DisMech target was found. The fuzzy candidate
`Glutaryl-CoA_Dehydrogenase_Deficiency.yaml` is a false neighbor: it models
GCDH-related glutaric aciduria type I, a lysine/hydroxylysine/tryptophan
catabolic disorder with glutaric acid, 3-hydroxyglutaric acid, C5DC, and
striatal injury risk. That mechanism is distinct from AUH-related
3-methylglutaconyl-CoA hydratase deficiency in leucine metabolism.

The local HMGCLD, Barth syndrome, and HSD10 files contain related
3-methylglutaconic aciduria patterns, but none is an AUH/MGA1 entry and none
should absorb this record.

## Concordance and completeness

Judgement: true local gap; do not map to GA1/GCDH.

IEMbase provides a reasonably rich seed profile for future AUH curation:
AUH gene identity, hydratase enzyme assay, urinary 3-methylglutaconic and
3-methylglutaric acids, C5-OH/C6-unsaturated acylcarnitine markers, and a
neurologic phenotype centered on ataxia, regression, leukoencephalopathy, and
optic/basal-ganglia involvement.

## Curation actions

- Keep this record unmapped until a standalone AUH-related
  3-methylglutaconic aciduria type I entry exists.
- Mark `Glutaryl-CoA_Dehydrogenase_Deficiency.yaml` as a false-positive fuzzy
  candidate for this IEMbase record.
- Consider AUH/MGA1 as a future curation candidate in the leucine degradation
  or 3-methylglutaconic aciduria workstream.
