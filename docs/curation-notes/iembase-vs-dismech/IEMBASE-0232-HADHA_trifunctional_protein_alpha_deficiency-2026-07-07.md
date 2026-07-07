# IEMbase 0232: HADHA-related Trifunctional protein subunit alpha deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 232 |
| Nosology | 4.2.05.02 |
| Gene | HADHA |
| External IDs | OMIM:609015 |
| Generated mapping | UNMAPPED; best candidate `Mitochondrial_Trifunctional_Protein_Deficiency.yaml` |
| Candidate DisMech targets | `Mitochondrial_Trifunctional_Protein_Deficiency.yaml`; `Long-Chain_3-Hydroxyacyl-CoA_Dehydrogenase_Deficiency.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as HADHA-related trifunctional protein subunit alpha
deficiency. The source label contains an alpha-wording artifact, and the
alternate label explicitly spans long-chain hydroxyacyl-CoA dehydrogenase
deficiency or complete mitochondrial trifunctional protein deficiency. The
record is autosomal recessive and treatability is marked yes, but no treatment
rows are attached in the cached JSON.

The biochemical rows include multiple long-chain hydroxyacylcarnitines,
palmitoylcarnitine, C14:1, free carnitine, creatine kinase, transaminases,
hypoketotic hypoglycemia context, 3-hydroxy dicarboxylic organic acids,
ammonia, glucose, and lactate. Clinical rows include intrauterine
cardiomyopathy, intrauterine growth restriction, lactic acidosis, and maternal
HELLP syndrome. Characteristic rows include cardiac arrhythmia, cardiomyopathy,
coma, lethargy, liver dysfunction, peripheral neuropathy, pigmentary
retinopathy, and skeletal myopathy.

## DisMech phenotype coverage

Local coverage is split across two relevant entries.
`Mitochondrial_Trifunctional_Protein_Deficiency.yaml` covers complete MTP/TFP
deficiency caused by HADHA or HADHB variants, loss of the long-chain enoyl-CoA
hydratase, LCHAD, and long-chain 3-ketoacyl-CoA thiolase activities, elevated
long-chain 3-hydroxyacylcarnitines, cardiomyopathy, hypoglycemia, hepatic
dysfunction, neuropathy, rhabdomyolysis, retinopathy, maternal HELLP/acute
fatty liver of pregnancy context, MCT-based diet, triheptanoin, fasting
avoidance, glucose support, and genetic counseling.

`Long-Chain_3-Hydroxyacyl-CoA_Dehydrogenase_Deficiency.yaml` covers isolated
HADHA/LCHAD deficiency, especially the common c.1528G>C variant, with
long-chain 3-hydroxyacylcarnitines, hypoketotic hypoglycemia, cardiomyopathy,
hepatopathy, rhabdomyolysis, peripheral neuropathy, progressive
chorioretinopathy, dietary fat restriction with MCT supplementation,
triheptanoin, fasting avoidance, and pregnancy-related maternal complications.

## Concordance and completeness

Judgement: generated unmapped status is a false negative, but the IEMbase label
scope is broader than a single clean local target.

If the intended IEMbase concept is complete HADHA-related MTP deficiency,
`Mitochondrial_Trifunctional_Protein_Deficiency.yaml` is the best mapping. If
the intended concept is isolated HADHA/LCHAD deficiency, the better mapping is
`Long-Chain_3-Hydroxyacyl-CoA_Dehydrogenase_Deficiency.yaml`. The IEMbase
alternate label explicitly combines both, so a single mapping should carry a
scope caveat or a secondary target.

## Curation actions

- Treat this as a false negative to existing local fatty-acid-oxidation
  coverage, not a true disease gap.
- Prefer `Mitochondrial_Trifunctional_Protein_Deficiency.yaml` for the complete
  MTP wording, with `Long-Chain_3-Hydroxyacyl-CoA_Dehydrogenase_Deficiency.yaml`
  as secondary context for isolated HADHA/LCHAD disease.
- Consider splitting or annotating the IEMbase crosswalk if the curation model
  needs distinct isolated LCHAD versus complete MTP targets.
