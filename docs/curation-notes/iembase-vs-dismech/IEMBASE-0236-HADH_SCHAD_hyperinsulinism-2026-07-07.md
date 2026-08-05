# IEMbase 0236: HADH-related Short-chain 3-hydroxyacyl-CoA dehydrogenase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 236 |
| Nosology | 4.2.04.01 |
| Gene | HADH |
| External IDs | OMIM:231530; ORPHA:71212 |
| Generated mapping | UNMAPPED |
| Candidate DisMech targets | `Congenital_Isolated_Hyperinsulinism.yaml#SCHAD-HI` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as HADH-related short-chain 3-hydroxyacyl-CoA
dehydrogenase deficiency, with alternate labels familial hyperinsulinemic
hypoglycemia type 4, SCHAD, and HHF4. The record is autosomal recessive and
treatability is marked unknown.

The biochemical rows include C4-OH hydroxybutyrylcarnitine in dried blood spots
or plasma, low urinary ketones, 3-hydroxyglutaric acid, medium-chain
dicarboxylic acids, increased ammonia, decreased glucose, and elevated insulin
during hypoglycemia. Clinical rows include cardiomyopathy and protein
sensitivity. Characteristic rows include hyperinsulinism, hypoketotic
hypoglycemia, intellectual disability, Reye-like liver failure, and seizures.

## DisMech phenotype coverage

`Congenital_Isolated_Hyperinsulinism.yaml` has subtype coverage for
`SCHAD-HI`, displayed as HADH (SCHAD) hyperinsulinism (HHF4). The local subtype
describes recessive HADH/SCHAD deficiency causing protein/leucine-sensitive
hyperinsulinism through loss of the inhibitory SCHAD-glutamate dehydrogenase
interaction, with typical diazoxide responsiveness. The broader local CHI entry
covers inappropriate insulin secretion, hypoglycemia with suppressed ketones
and free fatty acids, seizures, and risk of permanent neurologic injury.

The local entry is stronger for pancreatic beta-cell mechanism and treatment
context. IEMbase is more granular for fatty-acid and organic-acid biomarkers,
including C4-OH hydroxybutyrylcarnitine and 3-hydroxyglutaric acid.

## Concordance and completeness

Judgement: false negative to existing subtype coverage.

If the IEMbase concept is intended as the clinically recognized HADH/SCHAD
hyperinsulinism entity, it should resolve to
`Congenital_Isolated_Hyperinsulinism.yaml#SCHAD-HI`. The mapping should preserve
that this is not a generic fatty-acid oxidation crisis entry: the core local
concordance is hyperinsulinemic, protein/leucine-sensitive, hypoketotic
hypoglycemia caused by HADH/SCHAD loss.

IEMbase's ammonia row should be treated cautiously in curation. The local CHI
record uses hyperammonemia primarily for the GLUD1 HI/HA subtype, while HADH
acts through a related glutamate-dehydrogenase regulatory axis.

## Curation actions

- Map this record to `Congenital_Isolated_Hyperinsulinism.yaml#SCHAD-HI`.
- Consider adding IEMbase's C4-OH and 3-hydroxyglutaric-acid biomarker prompts
  to the SCHAD-HI subtype if diagnostic-marker detail is refreshed.
- Do not create a separate standalone HADH fatty-acid oxidation entry unless
  future evidence requires scope beyond SCHAD-HI/HHF4.
