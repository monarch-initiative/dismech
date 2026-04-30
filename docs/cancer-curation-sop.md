# Cancer Curation SOP: MONDO/NCIT Usage and Subtype Axes

Curator-facing SOP for using MONDO and NCIT consistently across cancer entries
in dismech: disease anchors, mappings, histopathology, treatments, and subtype
schemes. Resolves [#1198](https://github.com/monarch-initiative/dismech/issues/1198)
as the cancer-specific extension of the broader MONDO-anchoring SOPs in
[#795](https://github.com/monarch-initiative/dismech/issues/795) and
[#1007](https://github.com/monarch-initiative/dismech/issues/1007).

The mechanics of cancer pathophysiology, histopathology, and biomarker curation
live in `.claude/skills/cancer-curator/SKILL.md`. **This document covers only
the modeling-decision questions that recur across oncology entries**: when to
split, when to anchor, when to ground subtypes in NCIT.

## Curation unit: one entry per mechanism graph

> A dismech entry is a curation unit centered on one coherent mechanism graph.
> Ontology classes are not themselves the unit of curation.

A cancer ontology subclass should become a separate dismech entry only when its
**causal program is genuinely distinct** — different cell of origin, different
primary driver, different signaling cascade.

**Split into separate entries** when:
- different driver class or cell of origin (`Alveolar_Rhabdomyosarcoma` PAX3/7-FOXO1 fusion vs. `Embryonal_Rhabdomyosarcoma`)
- distinct pathway-defined groups (`Medulloblastoma_SHH_Activated` vs. `Medulloblastoma_WNT_Activated`)
- distinct molecular contexts that drive different therapy programs (`IDH_Mutant_Astrocytoma` vs. `IDH_Mutant_Oligodendroglioma`)

**Do not split** — keep as a faceted subtype within one entry — when the
difference is:
- histologic grade or pattern within the same mechanism (Favorable Histology vs. Anaplastic Wilms — same nephroblastoma program; anaplasia adds TP53 loss as a modifier, not a new cell-of-origin program)
- anatomic facet of the same disease (Bilateral vs. Unilateral Wilms)
- stage, age qualifier, or laterality alone

If you are unsure: prefer one entry with multiple subtype axes over fragmenting
the mechanism graph across files.

## `disease_term`: MONDO-first

Always anchor `disease_term` to MONDO when a `MONDO:0000001` (disease) descendant exists:

```yaml
disease_term:
  preferred_term: Wilms tumor
  term:
    id: MONDO:0006058
    label: Wilms tumor
```

- When MONDO has only a broad parent and NCIT has the precise oncology concept:
  keep MONDO as `disease_term` and add NCIT to `mappings` (see next section).
- When no MONDO disease term exists at all: follow the
  [#795](https://github.com/monarch-initiative/dismech/issues/795) SOP
  (`skos:closeMatch` to the closest MONDO term + Mondo NTR).

The point is to keep one stable disease anchor type across the KB so that
downstream tools (G2P, MONDO comparators) do not have to special-case oncology.

## Disease-level `mappings`: routinely include NCIT

Cancer entries should populate **all four** mapping slots when the corresponding
ontology has a relevant term:

```yaml
mappings:
  mondo_mappings:
  - term: {id: MONDO:0006058, label: Wilms tumor}
    mapping_predicate: skos:exactMatch
    mapping_source: MONDO
  icd10cm_mappings:
  - term: {id: ICD10CM:C64.9, label: Malignant neoplasm of unspecified kidney, except renal pelvis}
    mapping_predicate: skos:closeMatch
    mapping_source: ICD-10-CM
  ncit_mappings:
  - term: {id: NCIT:C3267, label: Wilms Tumor}
    mapping_predicate: skos:exactMatch
    mapping_source: NCIT
```

NCIT mappings at the disease level are especially valuable for downstream CCDI
interoperability. Do not omit them just because MONDO is the primary anchor.

The schema slot `ncit_mappings` ranges over `NCITMapping` and accepts
disease, subtype, or disease/finding terms — use the most specific NCIT class
available.

## Subtypes: flat axes, not a lattice

Multi-dimensional cancer classification (histology × stage × laterality ×
predisposition × age) should be modeled as **flat `has_subtypes` entries with
explicit `classification` axes**, not as nested hierarchies and not as separate
disease files.

Use `classification` to label the axis that the subtype belongs to. The Wilms
tumor entry is the canonical worked example:

| `classification` axis      | Wilms subtypes                                                  |
|----------------------------|-----------------------------------------------------------------|
| `anaplasia_status`         | Favorable Histology, Anaplastic                                 |
| `histological_pattern`     | Blastemal Predominant, Epithelial Predominant, Stromal Predominant, Mixed Cell Type |
| `laterality`               | Bilateral, Unilateral                                           |
| `predisposition_context`   | Hereditary Predisposition-Associated, Sporadic                  |
| `age_group`                | Childhood, Adult                                                |

Other axes seen across cancer entries: `molecular_driver`, `stage`,
`anatomic_site`, `treatment_associated`, `mutation_class`.

When you introduce a new axis, prefer reusing an existing axis name. Axis
vocabulary is open but should converge over time. Keep axes **as close to
closed/explicit as practical** — for example, the complement of "hereditary /
predisposition-associated" is `Sporadic`, not "somatic", because hereditary
tumors still acquire somatic alterations.

## `subtype_term` and subtype `mappings`: ontology grounding only

A subtype with an NCIT or MONDO term is **ontology-grounded**, not a separate
curation target.

Use `subtype_term` when the subtype itself has a MONDO identifier (disease-level
grounding), and use `mappings.ncit_mappings` for NCIT clinical/oncology grounding.
The two slots are complementary and can both appear on the same subtype:

```yaml
# NCIT-grounded subtype (no MONDO term for this facet)
- name: Anaplastic
  classification: anaplasia_status
  mappings:
    ncit_mappings:
    - term: {id: NCIT:C6952, label: Anaplastic Kidney Wilms Tumor}
      mapping_predicate: skos:closeMatch
      mapping_source: NCIT

# MONDO-grounded subtype with an additional NCIT mapping
- name: Childhood
  classification: age_group
  subtype_term:
    preferred_term: childhood kidney Wilms tumor
    term: {id: MONDO:0024676, label: childhood kidney Wilms tumor}
  mappings:
    ncit_mappings:
    - term: {id: NCIT:C27730, label: Childhood Kidney Wilms Tumor}
      mapping_predicate: skos:closeMatch
      mapping_source: NCIT
```

- `subtype_term` and subtype-level `mappings` provide ontology grounding for
  the subtype facet within the parent disease entry.
- They do **not** imply that a separate dismech disease page exists or should
  exist for that subtype.
- Renderers should display these as outbound hyperlinks to the source ontology
  (NCIT, MONDO), not as cross-entry "Not Yet Curated" indicators.

If you find that downstream tooling treats a grounded subtype as a missing
disease entry, that is a tooling bug — fix the comparator, not the curation.

## NCIT vs. MAXO selection in cancer entries

NCIT often provides clinically more specific oncology terms than MAXO. Prefer
NCIT when it materially improves specificity; otherwise stay with the existing
MAXO conventions documented in `CLAUDE.md`.

| Use case                              | Preferred ontology                       | Notes |
|---------------------------------------|------------------------------------------|-------|
| `disease_term`                        | MONDO                                    | Always MONDO-first |
| Disease-level `mappings`              | MONDO + ICD-10-CM + NCIT                 | All available |
| `histopathology.finding_term`         | NCIT (or HP for canonical patterns)      | NCIT has tumor-specific morphology terms |
| Surgical procedures                   | NCIT or MAXO — whichever is more specific | NCIT often wins for oncologic procedures |
| Chemotherapy action                   | MAXO:0000647 (chemotherapy)              | Generic; pair with `therapeutic_agent` |
| Radiation therapy                     | MAXO:0000014                             | |
| Specific drug                         | CHEBI (small molecule) or NCIT (biologic / drug class) | Use `therapeutic_agent` slot |
| Biomarkers / gene products            | NCIT (clinical biomarker) + HGNC (gene)  | `biomarker_term` / `gene_products` |
| Staging system terms                  | NCIT                                     | NCIT carries COG, SIOP, AJCC codes |

## Worked example: Wilms tumor

`kb/disorders/Wilms_Tumor.yaml` is the reference implementation of this SOP:

- `disease_term`: `MONDO:0006058` Wilms tumor (MONDO-first)
- `mappings`: `MONDO:0006058` (exactMatch) + `ICD10CM:C64.9` (closeMatch) + `NCIT:C3267` (exactMatch)
- `has_subtypes`: 12 flat subtypes across 5 axes (`anaplasia_status`, `histological_pattern`, `laterality`, `predisposition_context`, `age_group`)
- Most subtypes carry `mappings.ncit_mappings` with `skos:closeMatch` to the corresponding NCIT class — ontology-grounded, no separate page implied
- Histopathology, treatments, and biomarkers follow the table above

When in doubt about a new cancer entry, mirror Wilms tumor's structure.

## Related documents

- `CLAUDE.md` — repo-wide curation conventions (treatment terms, MAXO/NCIT/CHEBI patterns)
- `.claude/skills/cancer-curator/SKILL.md` — mechanics of cancer pathophysiology, histopathology, and therapeutic agent curation
- `.claude/skills/disease-classification/SKILL.md` — deeper guidance on classification axes and the `classifications` block
- [#795](https://github.com/monarch-initiative/dismech/issues/795) — MONDO disposition/susceptibility anchors and `skos:closeMatch` fallback
- [#1007](https://github.com/monarch-initiative/dismech/issues/1007) — Subtype gaps between dismech and MONDO
- [#1198](https://github.com/monarch-initiative/dismech/issues/1198) — This document
