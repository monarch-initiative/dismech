# IEMbase 0041: GLUL-related glutamine synthetase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 41 |
| Nosology | 1.9.01.01 |
| Gene | GLUL |
| External IDs | OMIM:610015; ORPHA:71278 |
| Generated mapping | UNMAPPED; best fuzzy candidate `Lipoic_Acid_Synthetase_Deficiency.yaml` |
| Candidate DisMech targets | none currently valid |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents GLUL deficiency as glutamine synthetase deficiency. The
biochemical signature is markedly low plasma glutamine, low CSF glutamine, low
urinary glutamine, normal CSF and plasma glutamic acid, and normal-to-high blood
ammonia.

The phenotype is severe and early: absent head control, developmental delay,
epileptic encephalopathy, intractable epilepsy, neonatal seizures, abnormal EEG,
possible cerebellar hypoplasia, and possible necrotising erythema. IEMbase lists
glutamine as a nutritional treatment. Prevalence is listed as 1:2,000,000.

## DisMech phenotype coverage

There is no current DisMech entry or subtype for GLUL-related glutamine
synthetase deficiency. The generated fuzzy candidate,
`Lipoic_Acid_Synthetase_Deficiency.yaml`, should be rejected. LIAS deficiency is
a mitochondrial lipoylation disorder with lipoate-dependent enzyme defects,
lactic acidosis, hyperglycinemia, neonatal epilepsy, and combined dehydrogenase
impairment. GLUL deficiency is a glutamine synthesis disorder with systemic and
CSF glutamine depletion.

Several local urea-cycle entries mention astrocytic glutamine synthetase as part
of ammonia detoxification, and citrin deficiency discusses impaired glutamine
synthetase function as a downstream state, but none of those entries represent
primary GLUL deficiency.

## Concordance and completeness

Judgement: generated unmapped status is correct, and the LIAS candidate is a
false positive.

IEMbase provides a strong future curation target. The most important phenotype
contrast is low glutamine with epileptic encephalopathy, not the high glycine and
lactic-acidosis profile of mitochondrial lipoylation defects.

## Curation actions

- Do not map this record to `Lipoic_Acid_Synthetase_Deficiency.yaml`.
- Consider GLUL deficiency as a future high-value metabolic encephalopathy
  target because it has severe clinical expression and a clear biochemical
  signature.
- If curated, capture glutamine supplementation separately from generic
  supportive epilepsy management.
