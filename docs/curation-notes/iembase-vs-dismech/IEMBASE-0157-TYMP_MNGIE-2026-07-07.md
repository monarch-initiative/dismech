# IEMbase 0157: TYMP-related MNGIE

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 157 |
| Nosology | 9.1.08.01 |
| Gene | TYMP |
| External IDs | OMIM:131222; OMIM:603041; ORPHA:298 |
| Generated mapping | AMBIGUOUS: `Chronic_Intestinal_Pseudoobstruction.yaml#Mitochondrial`; `Mitochondrial_Neurogastrointestinal_Encephalomyopathy.yaml` |
| Candidate DisMech targets | `Mitochondrial_Neurogastrointestinal_Encephalomyopathy.yaml`; `Chronic_Intestinal_Pseudoobstruction.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as TYMP-related thymidine phosphorylase deficiency,
with alternate labels mitochondrial depletion syndrome 1, mitochondrial
neurogastrointestinal encephalomyopathy syndrome, and MNGIE. Treatability is
marked unknown.

The biochemical rows show markedly decreased WBC thymidine phosphorylase in
adolescence and adulthood, increased plasma and urinary thymidine and
2'-deoxyuridine, and increased plasma lactate. The clinical profile includes
abdominal pain, diarrhea, vomiting, gastrointestinal dysmotility,
gastroparesis, malabsorption, chronic malnutrition, intestinal
pseudo-obstruction, hypodense white matter/leukoencephalopathy, areflexia,
myelinating neuropathy, muscle weakness, myopathy, and ragged-red fibers.

## DisMech phenotype coverage

`Mitochondrial_Neurogastrointestinal_Encephalomyopathy.yaml` is the correct
canonical target. It explicitly models classic TYMP-related MNGIE, thymidine
phosphorylase deficiency, systemic thymidine and 2'-deoxyuridine accumulation,
mitochondrial DNA depletion/deletions, gastrointestinal dysmotility,
pseudo-obstruction, cachexia, ptosis/progressive external ophthalmoplegia,
demyelinating peripheral neuropathy, leukoencephalopathy, skeletal myopathy,
and disease-modifying approaches such as allogeneic hematopoietic stem cell
transplantation, liver transplantation, erythrocyte-encapsulated thymidine
phosphorylase, dialysis, and investigational gene therapy.

`Chronic_Intestinal_Pseudoobstruction.yaml` also has a mitochondrial subtype
displayed as MNGIE and anchored on TYMP, but that entry is an umbrella CIPO
entry. It is useful secondary context for the intestinal pseudo-obstruction
phenotype, not the primary disease target for TYMP-related MNGIE.

## Concordance and completeness

Judgement: generated ambiguity should resolve to the standalone MNGIE entry.

DisMech has strong concordance for gene, biochemical mechanism, nucleoside
accumulation, gastrointestinal dysmotility, pseudo-obstruction,
leukoencephalopathy, neuropathy, myopathy, and treatment mechanisms. IEMbase
adds WBC enzyme activity as an explicit row, urinary thymidine/deoxyuridine,
plasma lactate, areflexia, ragged-red fibers, and anorexia-nervosa wording as
possible review details.

## Curation actions

- Map IEMbase 157 to `Mitochondrial_Neurogastrointestinal_Encephalomyopathy.yaml`.
- Treat the CIPO mitochondrial subtype as secondary phenotype/subtype context,
  not as the canonical mapping.
- Consider future refinement for urinary thymidine/deoxyuridine, WBC thymidine
  phosphorylase, plasma lactate, and ragged-red fiber rows.
