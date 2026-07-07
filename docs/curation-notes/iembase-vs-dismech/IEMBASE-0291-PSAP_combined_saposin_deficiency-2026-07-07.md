# IEMbase 0291: PSAP-related Combined saposin deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 291 |
| Nosology | 20.1.16.01 |
| Gene | PSAP |
| External IDs | OMIM:611721; ORPHA:309263 |
| Generated mapping | MAPPED; `Combined_Saposin_Deficiency.yaml` |
| Candidate DisMech targets | `Combined_Saposin_Deficiency.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents combined saposin deficiency / prosaposin deficiency due to
PSAP. The cached disease label contains a source spelling typo.
Inheritance is autosomal recessive and treatability is unknown.

The clinical rows are sparse: neonatal and infantile developmental delay,
hyperkinesia, and hypotonia. Biochemical rows are more specific and show the
multi-sphingolipid cofactor pattern: decreased fibroblast ceramidase activity,
increased plasma chitotriosidase, decreased fibroblast galactosylceramidase
activity, and decreased fibroblast glucosylceramidase activity.

## DisMech phenotype coverage

`Combined_Saposin_Deficiency.yaml` is the correct local target. The local entry
models biallelic PSAP loss, abolition of prosaposin and saposins A-D, combined
multi-sphingolipid lysosomal accumulation, severe neonatal neurodegeneration,
hepatosplenomegaly, thrombocytopenia, and cerebral demyelination. It also
distinguishes combined PSAP deficiency from isolated saposin C and saposin B
deficiencies.

Local biochemical coverage includes combined saposin A/B/C/D deficiency, but
does not enumerate the IEMbase secondary hydrolase assay pattern for ceramidase,
galactosylceramidase, and glucosylceramidase activities.

## Concordance and completeness

Judgement: correct mapping to `Combined_Saposin_Deficiency.yaml`.

IEMbase and DisMech agree on PSAP/prosaposin identity, recessive inheritance,
loss of multiple saposin-dependent sphingolipid degradation functions, early
neurodevelopmental disease, and hypotonia. DisMech is richer for the conceptual
boundary between combined prosaposin deficiency and isolated saposin
deficiencies, and for hepatosplenic, hematologic, demyelinating, and
neurodegenerative consequences.

IEMbase adds useful assay-level prompts: low ceramidase, galactosylceramidase,
and glucosylceramidase activities in fibroblasts, plus increased
chitotriosidase. These look like downstream functional readouts of saposin
cofactor loss rather than primary mutations in ASAH1, GALC, or GBA/GBA1, so
they should be framed carefully if imported.

## Curation actions

- Keep this record mapped to `Combined_Saposin_Deficiency.yaml`.
- Preserve the distinction between combined PSAP/prosaposin deficiency and
  isolated saposin A, B, C, or D disorders.
- Consider adding the IEMbase fibroblast hydrolase assays and chitotriosidase
  as downstream biochemical review prompts, not as separate causal-gene claims.
