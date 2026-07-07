# IEMbase 0284: GLB1-related Beta-galactosidase-1 deficiency, GM1 gangliosidosis

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 284 |
| Nosology | 20.1.14.01 |
| Gene | GLB1 |
| External IDs | OMIM:253010; ORPHA:79255 |
| Generated mapping | UNMAPPED; weak candidate `GM1_Gangliosidosis_Type_1.yaml` |
| Candidate DisMech targets | `GM1_Gangliosidosis_Type_1.yaml`; `GM1_Gangliosidosis_Type_2.yaml`; `GM1_Gangliosidosis_Type_3.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents GLB1-related beta-galactosidase-1 deficiency as a broad GM1
gangliosidosis record rather than a single age-defined type. Inheritance is
autosomal recessive, treatability is unknown, and prevalence is listed as
1:100,000 to 1:200,000.

The clinical rows span infantile through adult disease: Alder-Reilly anomaly,
ascites, brain atrophy, cardiomyopathy, corneal clouding, dystonia, edema, foam
cells, gait disturbance, gingival hypertrophy, intellectual disability,
macroglossia, seizures, and speech disturbance. The biochemical rows list
increased urinary oligosaccharides, increased mucopolysaccharide/unsaturated
keratan sulfate ratio, and increased serum LysoGM1.

## DisMech phenotype coverage

DisMech has separate local entries for `GM1_Gangliosidosis_Type_1.yaml`,
`GM1_Gangliosidosis_Type_2.yaml`, and `GM1_Gangliosidosis_Type_3.yaml`.
Together they cover the GLB1 beta-galactosidase deficiency spectrum better than
any single file.

Type 1 captures infantile GLB1 disease with neurodegeneration, developmental
regression, hepatosplenomegaly, dysostosis multiplex, coarse facial features,
and cherry-red macula. Type 2 captures intermediate disease with decreased
beta-galactosidase activity, developmental regression, seizures, ataxia,
feeding difficulty/dysphagia, speech decline/dysarthria, kyphosis, corneal
clouding, cardiomyopathy, cerebral atrophy, muscle weakness, and strabismus.
Type 3 captures adult/chronic basal-ganglia-predominant disease with dystonia,
parkinsonism, dysarthria, and gait disturbance. The local entries also include
gene therapy and supportive-care framing, but do not appear to model the
IEMbase LysoGM1 row or the urinary oligosaccharide row as biochemical entries.

## Concordance and completeness

Judgement: generated UNMAPPED is a false negative, but the best local target is
the GLB1 GM1 gangliosidosis spectrum, not only `GM1_Gangliosidosis_Type_1.yaml`.

IEMbase and DisMech agree on GLB1 identity, autosomal recessive inheritance,
beta-galactosidase deficiency, neurologic regression/intellectual disability,
seizures, brain atrophy, corneal clouding, cardiomyopathy, dystonia, gait
disturbance, and speech disturbance. DisMech is more nuanced for age-defined
subtypes and mechanistic interpretation. IEMbase is broader in one record and
adds laboratory prompts: urinary oligosaccharides, LysoGM1, and
mucopolysaccharide/keratan-sulfate ratio.

IEMbase also adds Alder-Reilly anomaly, foam cells, gingival hypertrophy,
macroglossia, edema, and ascites as review prompts. Some of these may be
type-specific or nonspecific lysosomal-storage features, so they should be
imported only with disease- and type-specific support.

## Curation actions

- Resolve this record to the local GM1 gangliosidosis spectrum:
  `GM1_Gangliosidosis_Type_1.yaml`, `GM1_Gangliosidosis_Type_2.yaml`, and
  `GM1_Gangliosidosis_Type_3.yaml`.
- Treat `GM1_Gangliosidosis_Type_1.yaml` alone as too narrow for this IEMbase
  record.
- Review LysoGM1, urinary oligosaccharides, Alder-Reilly anomaly, foam cells,
  gingival hypertrophy, macroglossia, edema, and ascites for possible subtype
  enrichment.
