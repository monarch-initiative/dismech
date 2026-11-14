# CCDI Pediatric Oncology Diagnosis Groups

The NCI Childhood Cancer Data Initiative (CCDI) files every pediatric cancer
diagnosis under one of 31 disease groups. The list is a caDSR common data
element, **16607972 "Diagnosis Pediatric Oncology Grouping Category"**, and
dismech carries it as a classification axis on neoplasm entries.

| Artifact | Path |
|----------|------|
| LinkML enum (31 values) | `src/dismech/schema/classifications/ccdi_pediatric_oncology.yaml` |
| Assignment class | `CCDIPediatricOncologyAssignment` in `src/dismech/schema/dismech.yaml` |
| Slot | `classifications.ccdi_pediatric_oncology_category` |
| Audit | `just ccdi-pediatric-oncology-audit` (`scripts/ccdi_pediatric_oncology_audit.py`) |
| Groupings | `kb/groupings/CCDI_Pediatric_Oncology_Diagnosis_Groups.yaml` and the groupings it nests |
| Curator guidance | `.claude/skills/disease-classification/SKILL.md` |

## What the CDE is

| Field | Value |
|---|---|
| caDSR public ID, version | 16607972, v1 |
| Value domain | 16607971 "Pediatric Oncology Category", enumerated |
| Context | Pediatric Cancer |
| Origin | CCDI: Childhood Cancer Data Initiative |
| Status | Released 2025-10-22 |
| Values last revised | 2026-01-26, to harmonize with CC4K |
| Retrieved | 2026-11-14, from the caDSR API |

The CDE classifies a **diagnosis record**. A value on a dismech entry says
which group a case of that disease is filed under. It is not a claim that the
disease is a childhood disease: osteosarcoma and Hodgkin lymphoma both have a
value.

It is a flat list. It mixes histology (medulloblastoma, ependymoma), site
(renal tumors, liver tumors) and lineage (myeloid leukemia), and it has four
residual "Other ..." values. It is a filing system for a data commons, not a
nosology, and dismech treats it as one.

## How a value is assigned

caDSR binds each permissible value to NCI Thesaurus concepts, which makes the
assignment computable. For each neoplasm entry the audit:

1. reads the entry's `disease_term` (MONDO);
2. reads that MONDO term's `NCIT:` cross-references;
3. walks each NCIt concept's `is_a` ancestors;
4. keeps every value whose bound concept is the entry's concept or an ancestor
   of it;
5. drops a value that is broader than another kept value, so alveolar
   rhabdomyosarcoma is `Rhabdomyosarcoma` and not also a broader sarcoma value;
6. considers the residual values only when no specific value was kept.

```bash
just ccdi-pediatric-oncology-audit                    # summary + worklist
just ccdi-pediatric-oncology-audit --format tsv       # one row per entry
just ccdi-pediatric-oncology-audit --status MISSING --format list
just ccdi-pediatric-oncology-audit kb/disorders/Wilms_Tumor.yaml --format list
just ccdi-pediatric-oncology-audit --offline          # cached lookups only
```

The audit needs OLS, so it is report-only and is not in `just qc`. Lookups are
cached in the gitignored `tmp/ccdi_pediatric_oncology_ols.json`.

### What the audit does not decide

- **A tie.** Where two values apply and neither is narrower than the other,
  the entry is reported `AMBIGUOUS` and the slot stays absent.
- **A missing cross-reference.** An entry whose MONDO term has no NCIT
  cross-reference is `NO_NCIT`. Nothing is inferred from its name.
- **A value assigned by hand.** A recorded value the hierarchy cannot derive
  is reported `CURATED`, not as an error. Such an assignment has to say in its
  `notes` that it was assigned by hand and why the hierarchy does not give it.
- **Anything, unless asked.** `--apply` writes `MISSING` proposals only into
  the files named on the command line. It never sweeps the knowledge base.
- **Whether NCIt is right.** The result is only as good as NCIt's hierarchy
  and MONDO's cross-reference. Two bindings are worth knowing about:
  `High-Grade Glioma` is bound to *Malignant Glioma* (`NCIT:C4822`), which in
  NCIt is a broad class, and `Other Solid Tumors` is bound to *Childhood Solid
  Neoplasm* (`NCIT:C9107`), which has few descendants, so the audit rarely
  proposes it.

## The two concept bindings that are not one-to-one

| Value | caDSR concepts | How dismech records it |
|---|---|---|
| `Other Gliomas`, `Other Brain Tumors`, `Other Solid Tumors`, `Other Hematopoietic Tumors` | parent concept + `NCIT:C17649` (Other) | `annotations.residual_of`, no `meaning` |
| `Endocrine and Neuroendocrine Tumors` | `NCIT:C3809` and `NCIT:C3010` | `annotations.ncit_scope`, no `meaning` |

`Other CNS Embryonal Tumors` is a different case: caDSR binds it to the single
concept *Central Nervous System Embryonal Tumor, Not Otherwise Specified*
(`NCIT:C5398`), so it has an ordinary `meaning` and is not treated as a
residual.

## The groupings

`kb/groupings/CCDI_Pediatric_Oncology_Diagnosis_Groups.yaml` is the parent. It
nests three groupings, `CCDI Medulloblastoma`, `CCDI CNS Germ Cell Tumors` and
the older `Rhabdomyosarcoma`, and lists the entries of every other value as
direct members with the value named on the row. The CDE has no hierarchy, so
the parent adds none. The membership criterion of a CCDI grouping is the
classification itself, stated as `NECESSARY_AND_SUFFICIENT`:

```yaml
membership_criteria:
- criteria_semantics: NECESSARY_AND_SUFFICIENT
  logic:
    criterion_predicate: HAS_CLASSIFICATION
    classification: "ccdi_pediatric_oncology_category:Medulloblastoma"
```

So the slot and the groupings check each other: `just check-groupings --strict`
fails a listed member that lacks the value. `Rhabdomyosarcoma` was grouped by
myogenic histogenesis, a criterion written as prose that the evaluator could
only report as `UNKNOWN`; it now carries the CCDI value as a second criterion,
which is verified per member.

## What is tagged so far

108 entries carry a value: 107 derived by the audit and one, `Wilms_Tumor`,
assigned by hand. Run over the whole knowledge base on 2026-11-14 the audit
assessed 329 neoplasm entries and proposed a value for 125.

Many of the tagged entries are adult-predominant: hepatocellular carcinoma is
under `Liver Tumors`, small cell lung cancer under `Endocrine and
Neuroendocrine Tumors`, clear cell renal cell carcinoma under `Renal Tumors`.
That is what the rule gives, and it is consistent with what the value claims,
which is where a case would be filed and not who gets the disease.

18 proposals are left untagged, because for them NCIt's hierarchy and the
intent of the CDE part ways: the 12 entries proposed as `Lymphoproliferative
Diseases`, the two neuroblastomas that are not peripheral neuroblastic tumors,
and four predisposition syndromes. The audit reports them `MISSING`. The table
gives the reasons, with the two entries that get no proposal at all.

Read these proposals before accepting them, because NCIt's hierarchy and the
intent of the CDE part ways:

| Entry | Audit result | Why it needs a person |
|---|---|---|
| `Wilms_Tumor` | no value | NCIt's *Wilms Tumor* (`NCIT:C3267`) is independent of site, so it is not a *Kidney Neoplasm*. Assigned `Renal Tumors` by hand; the audit reports it `CURATED`. |
| `Ganglioneuroblastoma` | no value | A sibling of *Neuroblastoma* in NCIt, not a descendant. |
| `CNS_Neuroblastoma_FOXR2-Activated`, `Olfactory_Neuroblastoma` | `Neuroblastoma` | A CNS embryonal tumor and a nasal cavity tumor, which NCIt files under *Neuroblastoma*; the CDE value most likely means the peripheral tumor. |
| `B-Lymphoblastic_Leukemia_Lymphoma_With_Recurrent_Genetic_Abnormality` | `Lymphoproliferative Diseases` | NCIt's B lymphoblastic leukemia/lymphoma is not under *Acute Lymphoblastic Leukemia*. |
| `Chronic_Lymphocytic_Leukemia`, `Multiple_Myeloma`, `Lymphoma` and eight more | `Lymphoproliferative Diseases` | The concept is broad in NCIt; the CDE value probably means something narrower. |
| `Clear_Cell_Sarcoma_of_Kidney`, `Kidney_Sarcoma` | `AMBIGUOUS` | Under both a sarcoma value and `Renal Tumors`. |
| `RUNX1_Familial_Platelet_Disorder`, `Multiple_Endocrine_Neoplasia_Type_1`, `Multiple_Endocrine_Neoplasia_Type_2`, `Hereditary_Leiomyomatosis_and_Renal_Cell_Cancer` | a value | Predisposition syndromes whose MONDO term cross-references a neoplasm concept. |

## Updating when caDSR revises the value domain

The permissible values were renamed once already (2026-01-26). To refresh:

```bash
curl -sS https://cadsrapi.cancer.gov/rad/NCIAPI/1.0/api/DataElement/16607972
```

Compare its permissible values and their concept codes with the enum. Keys are
the CDE's values verbatim, so a rename upstream is a rename here, and it has to
follow the two-stage migration in the `extend-schema` skill: add the new key,
migrate entries and groupings, then retire the old one.
