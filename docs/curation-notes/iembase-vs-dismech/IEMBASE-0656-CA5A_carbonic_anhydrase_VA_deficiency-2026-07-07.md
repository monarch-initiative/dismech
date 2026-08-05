# IEMbase 0656: CA5A-related carbonic anhydrase VA deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 656 |
| Nosology | 1.1.09.01 |
| Nosology code | IEM0064 |
| Gene | CA5A |
| External IDs | OMIM:615751; ORPHA:401948 |
| Generated mapping | UNMAPPED; weak candidate `Carbamoyl_Phosphate_Synthetase_I_Deficiency.yaml` |
| Candidate DisMech targets | No exact local target; broad hyperammonemia/UCD context only |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive CA5A-related carbonic anhydrase VA
deficiency, also labeled hyperammonemia due to carbonic anhydrase VA deficiency.

Clinical rows emphasize neonatal/infantile metabolic decompensation: coma,
temperature instability, vomiting, encephalopathy, feeding difficulties, and
hypoglycemia. Biochemical rows include increased ammonia, low glucose,
normal-to-increased lactate, low-to-normal arginine and citrulline,
normal-to-high glutamine, normal urinary orotic acid, and multiple organic
acid/acylglycine abnormalities including 3-methylcrotonylglycine,
propionylglycine, ketones, 2-ketoglutaric acid, 3-hydroxybutyric acid,
3-hydroxyisovaleric acid, 3-hydroxypropionic acid, adipic acid, fumaric acid,
sebacic acid, and suberic acid.

## DisMech phenotype coverage

`Carbamoyl_Phosphate_Synthetase_I_Deficiency.yaml` is a mechanistically related
but gene-specific false exact candidate. It models CPS1 loss at the urea-cycle
entry step, with hyperammonemia, low citrulline, high glutamine, normal/low
orotic acid, encephalopathy, coma, and ammonia neurotoxicity. Those are useful
shared decompensation features, but the file does not model CA5A, mitochondrial
carbonic anhydrase VA, bicarbonate supply to multiple mitochondrial enzymes, or
the IEMbase organic-acid/acylglycine pattern.

No local CA5A or carbonic anhydrase VA deficiency disease entry was found.

## Concordance and completeness

Judgement: broad hyperammonemia context only; true CA5A disease-level gap.

The CPS1 entry should not be treated as exact coverage, but it is a useful
neighbor for shared acute hyperammonemic encephalopathy. The IEMbase row needs a
separate CA5A mechanism to preserve the combined urea-cycle, pyruvate
carboxylase, and organic-acid signature.

## Curation actions

- Keep this row unmapped until a CA5A target exists.
- Do not map to `Carbamoyl_Phosphate_Synthetase_I_Deficiency.yaml` as exact.
- Preserve ammonia, glucose, lactate, glutamine, arginine/citrulline, normal
  orotic acid, organic acids, acylglycines, hypoglycemia, vomiting,
  encephalopathy, coma, feeding, and temperature-instability prompts.
