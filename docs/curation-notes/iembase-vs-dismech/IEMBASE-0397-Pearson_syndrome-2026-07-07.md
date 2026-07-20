# IEMbase 0397: NOGENE-related Pearson Syndrome

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 397 |
| Nosology | 6.3.01.01 |
| Gene | No single gene; single large-scale mtDNA deletion disorder |
| External IDs | OMIM:557000; ORPHA:699 |
| Generated mapping | UNMAPPED; low candidate `Pancreatic_Agenesis.yaml` |
| Candidate DisMech targets | `Pearson_Syndrome.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents Pearson syndrome, also listed as Pearson marrow-pancreas
syndrome and sideroblastic anemia with marrow cell vacuolization and exocrine
pancreatic dysfunction. The record has no nuclear gene, consistent with the
single large-scale mtDNA deletion disease class.

Characteristic rows include hypoplastic macrocytic anemia, sideroblastic
anemia, low weight, endocrine and exocrine pancreatic dysfunction, vacuolization
of hematopoietic precursors, increased plasma and urinary lactate, and increased
lactate/pyruvate ratio. Additional rows include failure to thrive, hypertonia,
hypotonia, leukocytosis, liver steatosis, proximal renal tubulopathy,
thrombocytopenia, perinatal death, and evolution to Kearns-Sayre syndrome.
There are no treatment rows.

## DisMech phenotype coverage

The generated unmapped status is a false negative. Local
`Pearson_Syndrome.yaml` is the correct target and models infantile single
large-scale mitochondrial DNA deletion disease with hematopoietic and
proliferative-tissue deleted-mtDNA burden, transfusion-dependent sideroblastic
anemia, pancytopenia with vacuolated marrow precursors, exocrine pancreatic
dysfunction, poor growth, renal tubular disease, lactic acidosis, and potential
later evolution toward a Kearns-Sayre-like phenotype.

The generated `Pancreatic_Agenesis.yaml` candidate is not appropriate:
pancreatic dysfunction in Pearson syndrome is secondary to mitochondrial DNA
deletion disease, not congenital pancreatic organ agenesis.

## Concordance and completeness

Judgement: false negative; resolve to `Pearson_Syndrome.yaml`.

The resources agree on Pearson marrow-pancreas identity, no single nuclear gene,
single large-scale mtDNA deletion disease class, sideroblastic anemia,
vacuolated marrow precursors, exocrine pancreatic dysfunction, poor growth,
renal tubulopathy, lactate elevation, and overlap/evolution toward KSS in
survivors.

## Curation actions

- Map this record to `Pearson_Syndrome.yaml`.
- Do not map to `Pancreatic_Agenesis.yaml`.
- Consider adding IEMbase's hypoplastic macrocytic anemia wording, lactate/
  pyruvate ratio, urinary lactate, liver steatosis, leukocytosis, endocrine
  pancreatic dysfunction, and proximal renal tubulopathy prompts after source
  verification.
