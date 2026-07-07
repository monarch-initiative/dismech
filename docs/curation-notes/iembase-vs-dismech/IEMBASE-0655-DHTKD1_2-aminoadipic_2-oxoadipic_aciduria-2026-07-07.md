# IEMbase 0655: DHTKD1-related 2-aminoadipic 2-oxoadipic aciduria

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 655 |
| Nosology | 1.8.03.02 |
| Nosology code | IEM0132 |
| Gene | DHTKD1 |
| External IDs | OMIM:204750; ORPHA:79154 |
| Generated mapping | UNMAPPED; weak candidate `D-2-Hydroxyglutaric_Aciduria.yaml` |
| Candidate DisMech targets | No exact local target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive DHTKD1-related 2-aminoadipic
2-oxoadipic aciduria, abbreviated AMOXAD.

Clinical rows include developmental delay, metabolic acidosis, and optional
seizures. Biochemical rows include increased urinary 2-aminoadipic acid,
2-hydroxyadipic acid, 2-ketoadipic acid, 3-hydroxyglutaric acid,
3-hydroxyisovaleric acid, 3-methylglutaconic acid, and C6-C10 dicarboxylic
acids; ketones during hypoglycemia; and normal-to-increased urinary ethylmalonic
acid.

## DisMech phenotype coverage

`D-2-Hydroxyglutaric_Aciduria.yaml` is a nearby organic-aciduria context but not
an exact target. It models D2HGDH/IDH2-related D-2-hydroxyglutarate accumulation,
not DHTKD1-related lysine/tryptophan degradation. Its core metabolite,
2-hydroxyglutarate, is different from the IEMbase adipic/ketoadipic and
dicarboxylic-acid pattern.

Targeted search did not find a local DHTKD1, 2-aminoadipic 2-oxoadipic
aciduria, or AMOXAD entry.

## Concordance and completeness

Judgement: true local DHTKD1 / AMOXAD gap; reject D-2-hydroxyglutaric aciduria
as exact.

The generated candidate is useful only as a broad organic-acidemia neighbor. It
would misrepresent the causal gene and diagnostic metabolite panel if used as
coverage.

## Curation actions

- Keep this row unmapped until a DHTKD1 / AMOXAD target exists.
- Do not map to `D-2-Hydroxyglutaric_Aciduria.yaml`.
- Preserve 2-aminoadipic, 2-ketoadipic, 2-hydroxyadipic, 3-hydroxyglutaric,
  3-hydroxyisovaleric, 3-methylglutaconic, dicarboxylic-acid, ketone,
  ethylmalonic-acid, acidosis, developmental-delay, and seizure prompts.
