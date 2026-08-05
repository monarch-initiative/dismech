# IEMbase 0167: IDH2-related D-2-hydroxyglutaric aciduria type II

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 167 |
| Nosology | 5.2.02.01 |
| Gene | IDH2 |
| External IDs | OMIM:613657; ORPHA:79315 |
| Generated mapping | MAPPED to `D-2-Hydroxyglutaric_Aciduria.yaml` |
| Candidate DisMech targets | `D-2-Hydroxyglutaric_Aciduria.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as IDH2-related mitochondrial NADP+-dependent
isocitrate dehydrogenase 2 superactivity, with alternate labels
D-2-hydroxyglutaric aciduria type 2, D2HGA type II, and somatic Ollier disease
and Maffuci syndrome context. Treatability is marked unknown, and the local
IEMbase JSON does not list treatment rows.

The biochemical rows show increased D-2-hydroxyglutaric acid in CSF, plasma,
and urine across age bands. Clinical rows include developmental delay,
hypotonia, variable epilepsy, and cardiomyopathy as a variable to
characteristic feature.

## DisMech phenotype coverage

`D-2-Hydroxyglutaric_Aciduria.yaml` is the correct target. The local entry
explicitly models the IDH2 type II branch as heterozygous, usually de novo,
IDH2 gain of neomorphic D-2-HG-producing activity. It covers D-2-HG
overproduction from alpha-ketoglutarate, D-2-HG accumulation in urine, plasma,
and CSF, developmental delay, hypotonia, seizures, cardiomyopathy, white
matter changes, psychomotor impairment, mutant IDH2 inhibitor rationale,
supportive cardiac care, and D-2-HG monitoring.

## Concordance and completeness

Judgement: correct mapping with high concordance.

The profiles agree on IDH2-related type II disease, D-2-HG accumulation across
body fluids, neurodevelopmental impairment, hypotonia, epilepsy, and the
prominent cardiomyopathy signal that differentiates type II from type I.
DisMech is stronger for mechanism and treatment-development context, including
IDH2 inhibition. IEMbase adds the nosology placement under Krebs-cycle
disorders and records the somatic Ollier/Maffucci context as an alternate
label, which should remain context rather than a separate disease mapping for
this germline metabolic comparison.

## Curation actions

- Keep the mapping to `D-2-Hydroxyglutaric_Aciduria.yaml`.
- If subtype anchors are later exposed, map this record to the IDH2/type II
  branch.
- Retain Ollier/Maffucci somatic IDH2 context as scope context, not as the
  canonical germline D2HGA type II target.
