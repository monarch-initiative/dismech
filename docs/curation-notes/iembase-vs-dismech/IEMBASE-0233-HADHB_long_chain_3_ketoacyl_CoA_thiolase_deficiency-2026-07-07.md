# IEMbase 0233: HADHB-related Isolated deficiency of long-chain 3-ketoacyl-CoA thiolase

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 233 |
| Nosology | 4.2.06.02 |
| Gene | HADHB |
| External IDs | OMIM:143450 |
| Generated mapping | UNMAPPED; no candidate |
| Candidate DisMech targets | Partial umbrella coverage: `Mitochondrial_Trifunctional_Protein_Deficiency.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as HADHB-related isolated deficiency of long-chain
3-ketoacyl-CoA thiolase, with the alternate label LKAT. The record is autosomal
recessive and treatability is marked unknown.

The biochemical rows include long-chain hydroxyacylcarnitines, long-chain
ketoacylcarnitines, free carnitine, creatine kinase, transaminases,
hypoketotic hypoglycemia context, 3-hydroxy dicarboxylic organic acids,
glucose, and lactate. Characteristic rows include cardiac arrhythmia,
cardiomyopathy, muscular-axial hypotonia, high lethality, liver dysfunction,
pulmonary edema, and skeletal myopathy. Treatments listed by IEMbase are a
low-LCT diet, MCT formula, sodium-D-L-hydroxybutyrate, and triheptanoin.

## DisMech phenotype coverage

`Mitochondrial_Trifunctional_Protein_Deficiency.yaml` provides partial umbrella
coverage. It covers HADHB as a cause of mitochondrial trifunctional protein
deficiency, the beta subunit of the MTP complex, loss of long-chain
3-ketoacyl-CoA thiolase activity along with the other MTP activities, impaired
long-chain fatty-acid beta-oxidation, elevated long-chain
3-hydroxyacylcarnitines, cardiomyopathy, arrhythmia/cardiac disease context,
hypoglycemia, hepatic dysfunction, neuropathy, myopathy, rhabdomyolysis, MCT
diet, triheptanoin, fasting avoidance, acute glucose support, and genetic
counseling.

The local file does not appear to expose a dedicated isolated long-chain
3-ketoacyl-CoA thiolase/LKAT subtype. That distinction matters because IEMbase
frames the record as isolated HADHB thiolase deficiency rather than complete
MTP deficiency.

## Concordance and completeness

Judgement: partial false negative to local umbrella coverage, with an exact
isolated LKAT target missing.

The generated unmapped status misses substantial local HADHB/MTPD mechanism and
phenotype coverage. However, mapping this record directly to complete MTPD
without a caveat would blur IEMbase's isolated enzyme-defect scope. IEMbase also
adds ketoacylcarnitines, pulmonary edema, sodium-D-L-hydroxybutyrate, and
low-LCT/MCT formula wording as review prompts.

## Curation actions

- Use `Mitochondrial_Trifunctional_Protein_Deficiency.yaml` as partial umbrella
  coverage if a single current DisMech target is required.
- Record a gap for an exact isolated HADHB/LKAT subtype or standalone disease
  concept.
- Do not treat this as fully resolved by complete MTPD unless the crosswalk can
  preserve the isolated-thiolase scope caveat.
