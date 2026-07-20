# IEMbase 0064: HSD17B10-related HSD10 mitochondrial disease

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 64 |
| Nosology | 10.1.15.01 |
| Gene | HSD17B10 |
| External IDs | OMIM:300438 |
| Generated mapping | UNMAPPED; best fuzzy candidate `HSD10_Mitochondrial_Disease.yaml` |
| Candidate DisMech targets | `HSD10_Mitochondrial_Disease.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as X-linked HSD17B10-related
17-beta-hydroxysteroid dehydrogenase type 10 deficiency, also called
2-methyl-3-hydroxybutyryl-CoA dehydrogenase deficiency or HSD10. Treatability
is marked yes, but no specific treatment rows are present in the cached record.

The biochemical signal includes normal-high C5-OH
2-methyl-3-hydroxybutyrylcarnitine, normal-high C5:1 tiglylcarnitine, low
fibroblast 17-beta-HSD10 activity, high urinary
2-methyl-3-hydroxybutyric acid, high urinary tiglylglycine, low-normal glucose,
and normal-high CSF or plasma lactate.

The characteristic clinical signal includes cardiomyopathy, dystonia, lactic
acidosis, psychomotor delay, psychomotor regression, and seizures. Additional
features include basal ganglia lesions, white-matter brain atrophy,
choreoathetosis, dysarthria, frontotemporal atrophy, sensorineural hearing
loss, hypoglycemia, ketoacidosis, metabolic acidosis, male predominance,
movement disorder, periventricular white-matter changes, rigidity, spasticity,
and decreased vision.

## DisMech phenotype coverage

The generated `UNMAPPED` status is a false negative despite the low fuzzy score.
`HSD10_Mitochondrial_Disease.yaml` is the correct local target. DisMech models
HSD10 mitochondrial disease as an X-linked neurodegenerative disorder caused by
HSD17B10 variants affecting the multifunctional mitochondrial HSD10/MHBD protein.
It explicitly covers the dual role in isoleucine/neurosteroid metabolism and
mitochondrial RNase P/tRNA processing, with mitochondrial respiratory-chain
dysfunction and energy failure as the central disease mechanism.

DisMech covers infantile, neonatal, juvenile, and atypical/asymptomatic forms,
developmental regression, seizures, choreoathetosis, hypotonia, cardiomyopathy,
retinopathy, visual loss, 2-methyl-3-hydroxybutyric aciduria, lactic acidosis,
X-linked inheritance with variable female manifestations, supportive care, and
historical isoleucine-restricted diet as a non-curative approach.

## Concordance and completeness

Judgement: false-negative generated mapping; high manual concordance with
`HSD10_Mitochondrial_Disease.yaml`.

IEMbase adds granular lab and imaging features that are not all explicit in the
DisMech summary: C5-OH 2-methyl-3-hydroxybutyrylcarnitine, C5:1
tiglylcarnitine, fibroblast enzyme activity, urinary tiglylglycine, CSF lactate,
basal ganglia lesions, frontotemporal atrophy, sensorineural hearing loss,
ketoacidosis, periventricular white-matter changes, rigidity, spasticity, and
dysarthria. DisMech is stronger for current mechanism, especially mitochondrial
RNA processing rather than a purely isoleucine-metabolism framing.

## Curation actions

- Update mapping logic so HSD17B10/HSD10 resolves to
  `HSD10_Mitochondrial_Disease.yaml`.
- Treat IEMbase's "treatability yes" cautiously because no treatment rows are
  present and DisMech records no effective disease-modifying therapy.
- Consider IEMbase-specific acylcarnitine and neuroimaging details as future
  diagnostic/phenotype enrichments.
