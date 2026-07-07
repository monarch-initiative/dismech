# IEMbase 0220: PDHA1-related Pyruvate dehydrogenase E1 alpha deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 220 |
| Nosology | 5.1.01.01 |
| Gene | PDHA1 |
| External IDs | OMIM:312170 |
| Generated mapping | MAPPED; `Pyruvate_Dehydrogenase_Deficiency.yaml` |
| Candidate DisMech targets | `Pyruvate_Dehydrogenase_Deficiency.yaml#E1-alpha deficiency` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as PDHA1-related pyruvate dehydrogenase E1 alpha
deficiency, with alternate label PDH. The record is X-linked and treatability is
marked yes.

The biochemical rows include increased alanine, lactate, lactate/pyruvate
ratio, pyruvate, and ketones, with normal glucose. Characteristic clinical rows
include corpus-callosum agenesis on MRI, dysmorphic features, failure to thrive,
lactic acidosis, and microcephaly. Additional rows include developmental delay,
drug-resistant epilepsy, hypotonia, Leigh syndrome, peripheral neuropathy,
pyramidal signs, seizures, and multiple craniofacial features. Treatments
listed by IEMbase are ketogenic diet and thiamine.

## DisMech phenotype coverage

`Pyruvate_Dehydrogenase_Deficiency.yaml` is the correct target, with subtype
resolution to `E1-alpha deficiency`. The local entry covers PDHA1 as the most
common PDH deficiency gene, X-linked inheritance, reduced PDH complex activity,
blocked pyruvate decarboxylation to acetyl-CoA, lactate and pyruvate
accumulation, lactic acidosis, neurodevelopmental injury, hypotonia, seizures,
movement disorders, corpus-callosum abnormalities, microcephaly, dysmorphic
features, ketogenic diet, thiamine-responsive PDHA1 residual activity,
dichloroacetate, phenylbutyrate, biochemical testing, enzyme assay, molecular
testing, and brain MRI.

## Concordance and completeness

Judgement: correct mapped target, with subtype resolution needed.

IEMbase and DisMech agree on PDHA1/E1-alpha identity, X-linked inheritance,
the PDH biochemical block, lactate/pyruvate abnormalities, lactic acidosis,
developmental delay, hypotonia, seizures/epilepsy, Leigh-spectrum CNS disease,
corpus-callosum involvement, microcephaly, dysmorphism, ketogenic diet, and
thiamine. IEMbase adds more granular craniofacial descriptors and flags
drug-resistant epilepsy; DisMech is richer for mechanism, therapy nuance, and
diagnostic workflow.

## Curation actions

- Keep the record mapped to `Pyruvate_Dehydrogenase_Deficiency.yaml`.
- Prefer subtype resolution to
  `Pyruvate_Dehydrogenase_Deficiency.yaml#E1-alpha deficiency`.
- Consider reviewing IEMbase's granular facial-feature and drug-resistant
  epilepsy rows if the PDHA1 subtype is later enriched.
