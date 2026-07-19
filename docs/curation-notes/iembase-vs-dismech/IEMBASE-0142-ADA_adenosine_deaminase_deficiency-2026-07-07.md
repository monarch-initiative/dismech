# IEMbase 0142: ADA-related adenosine deaminase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 142 |
| Nosology | 16.2.07.01 |
| Gene | ADA |
| External IDs | OMIM:102700; ORPHA:39041 |
| Generated mapping | MAPPED to `Severe_Combined_Immunodeficiency.yaml#ADA deficiency` |
| Candidate DisMech targets | `Severe_Combined_Immunodeficiency.yaml#ADA deficiency` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as ADA-related adenosine deaminase deficiency, with
alternate label severe combined immunodeficiency and abbreviation ADA.
Treatability is marked yes.

The biochemical signal is markedly decreased red-cell adenosine deaminase
activity, increased urinary deoxyadenosine, increased red-cell dATP, and
decreased immunoglobulins. Clinical rows include severe combined
immunodeficiency, B-cell lymphopenia, recurrent infections, failure to thrive,
splenomegaly, skeletal abnormalities, anterior rib cupping, and scapular
spurring.

## DisMech phenotype coverage

`Severe_Combined_Immunodeficiency.yaml` has an ADA deficiency subtype with ADA
as the causal gene. It models ADA-SCID as a systemic purine metabolic disorder
in which toxic deoxyadenosine and dATP accumulation impairs lymphocyte
development and viability.

Local coverage is strong for the core immune phenotype: recurrent infections,
failure to thrive, T/B/NK-cell immunophenotype, immune reconstitution by
hematopoietic stem cell transplantation or gene therapy, and PEG-ADA enzyme
replacement. The entry also captures deoxyadenosine/dATP-mediated
pathophysiology rather than treating ADA-SCID as only a generic SCID label.

## Concordance and completeness

Judgement: correct subtype mapping with good mechanism-level concordance.

The generated mapping is appropriate. IEMbase's ADA, deoxyadenosine, dATP,
immunoglobulin, recurrent-infection, and failure-to-thrive signals all align
with the local ADA-SCID subtype. IEMbase is more granular for rib and scapular
skeletal rows and for B-cell lymphopenia wording. DisMech is richer for the
causal chain and treatment rationale.

## Curation actions

- Keep the mapping to `Severe_Combined_Immunodeficiency.yaml#ADA deficiency`.
- Do not confuse this with `Deficiency_of_Adenosine_Deaminase_2.yaml`, which is
  ADA2/CECR1 vasculopathy, not ADA-SCID.
- Consider future ADA-SCID refinement for the IEMbase-only skeletal rows and
  explicit red-cell ADA/dATP diagnostic marker wording.
