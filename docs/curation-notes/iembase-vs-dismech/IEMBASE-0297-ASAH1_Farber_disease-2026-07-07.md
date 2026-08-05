# IEMbase 0297: ASAH1-related Acid ceramidase deficiency, inflammatory phenotype

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 297 |
| Nosology | 20.1.14.01 |
| Gene | ASAH1 |
| External IDs | OMIM:228000; ORPHA:333 |
| Generated mapping | MAPPED; `Farber_Disease.yaml` |
| Candidate DisMech targets | `Farber_Disease.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents Farber disease / acid ceramidase deficiency with an
inflammatory phenotype. Inheritance is autosomal recessive and treatability is
marked yes, although no treatment rows are present in the cached record.

Clinical rows include arthritis, hepatosplenomegaly, hoarseness, limited deep
tendon reflexes, subcutaneous nodules, cherry red spot, developmental delay,
failure to thrive, foam cells, hypotonia, intellectual disability, lung
infiltrates, lymphadenopathy, and seizures. Biochemical rows show markedly
decreased leukocyte acid ceramidase activity, normal-to-increased CSF protein,
and increased C26-ceramide.

## DisMech phenotype coverage

`Farber_Disease.yaml` is the correct local target. The local entry models
biallelic ASAH1 variants, acid ceramidase loss of function, ceramide catabolism
blockade, lysosomal ceramide storage, lipid-laden macrophage granulomas,
cytokine and ceramide plasma signatures, CNS storage injury, and retinal
storage/macrophage activation.

Local phenotype coverage includes the core clinical triad and related features:
periarticular subcutaneous nodules, arthritis, arthralgia, flexion contracture,
joint swelling, hoarse voice, respiratory involvement, failure to thrive,
floppy infant, global developmental delay, intellectual disability, CNS foam
cells, cherry red spot, abnormal acid ceramidase activity, and granulomas with
lipid-laden macrophages. Local biochemical coverage includes reduced acid
ceramidase activity and increased ceramide species. Local treatment coverage is
richer than IEMbase and includes supportive management, hematopoietic stem cell
transplantation, recombinant acid ceramidase enzyme replacement, and
AAV-mediated ASAH1 gene therapy for retinopathy.

## Concordance and completeness

Judgement: correct high-concordance mapping to `Farber_Disease.yaml`.

IEMbase and DisMech agree on ASAH1 disease identity, recessive inheritance,
acid ceramidase deficiency, ceramide accumulation, nodules, arthritis,
hoarseness, CNS/developmental involvement, cherry red spot, foam cells, and
respiratory involvement. DisMech is stronger for mechanism, granuloma biology,
biochemical framing, treatment landscape, and retinal/CNS mechanistic detail.

IEMbase adds useful prompts for hepatosplenomegaly, limited deep tendon reflexes,
lung infiltrates, lymphadenopathy, seizures, CSF protein, and C26-ceramide.
The absence of cached IEMbase treatment rows should not be interpreted as lack
of local treatment relevance.

## Curation actions

- Keep this record mapped to `Farber_Disease.yaml`.
- Review IEMbase-only hepatosplenic, reflex, lung-infiltrate, lymphadenopathy,
  seizure, CSF-protein, and C26-ceramide prompts against the Farber evidence
  base before import.
- Do not downgrade local treatment coverage based on the sparse IEMbase treatment
  section.
