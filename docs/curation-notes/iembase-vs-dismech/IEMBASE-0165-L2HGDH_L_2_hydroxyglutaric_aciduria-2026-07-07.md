# IEMbase 0165: L2HGDH-related L-2-hydroxyglutaric aciduria

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 165 |
| Nosology | 12.1.02.01 |
| Gene | L2HGDH |
| External IDs | OMIM:236792; ORPHA:79314 |
| Generated mapping | MAPPED to `L-2-Hydroxyglutaric_Aciduria.yaml` |
| Candidate DisMech targets | `L-2-Hydroxyglutaric_Aciduria.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as L2HGDH-related L-2-hydroxyglutarate dehydrogenase
deficiency, with alternate labels L-2-hydroxyglutaric aciduria and L2HGA.
Treatability is marked yes, but the local IEMbase JSON does not list treatment
rows for this disorder.

The biochemical rows show increased L-2-hydroxyglutaric acid in CSF, plasma,
and urine; CSF and plasma lysine reported as normal to normal-increased;
neonatal ammonia and lactate reported as normal to increased; and increased CSF
protein in infancy and childhood. Clinical rows include dentate nucleus lesions,
globus pallidus lesions, cerebellar white-matter MRI abnormalities,
intellectual disability, ataxia, dysarthria, tremor, dystonia,
choreoathetosis, seizures, hypotonia, spasticity, macrocephaly, and gliomas.

## DisMech phenotype coverage

`L-2-Hydroxyglutaric_Aciduria.yaml` is the correct target. It models biallelic
L2HGDH pathogenic variants, loss of mitochondrial L-2-hydroxyglutarate
dehydrogenase metabolite-repair activity, L-2-HG accumulation in urine, plasma,
CSF, and brain, selective white-matter vulnerability with basal ganglia and
dentate nucleus involvement, intellectual disability, psychomotor delay,
seizures/epilepsy, cerebellar ataxia, dystonia, dysarthria, tremor, chorea,
macrocephaly, spasticity, increased CNS neoplasm risk, riboflavin,
levocarnitine, supportive care, and movement-disorder interventions such as
deep brain stimulation.

## Concordance and completeness

Judgement: correct mapping with high concordance.

The IEMbase and DisMech profiles agree on L2HGDH, L-2-HG accumulation in urine,
plasma, and CSF, white-matter disease, dentate/basal ganglia involvement,
intellectual disability, seizures, ataxia, dystonia/movement disorder,
dysarthria, tremor, macrocephaly, spasticity, and glioma/CNS tumor risk.
DisMech is stronger for metabolite-repair mechanism, treatment rationale, and
neoplasm-risk discussion. IEMbase adds lysine, neonatal ammonia/lactate, CSF
protein, and choreoathetosis as potential review details.

## Curation actions

- Keep the mapping to `L-2-Hydroxyglutaric_Aciduria.yaml`.
- Consider future biomarker refinement for lysine, neonatal ammonia/lactate,
  and CSF protein if primary sources support them.
- Review whether IEMbase choreoathetosis should be represented as a distinct
  movement-disorder phenotype or covered by the existing chorea/dystonia rows.
