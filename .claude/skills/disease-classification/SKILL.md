---
name: disease-classification
description: >
  Skill for populating the `classifications` top-level block of a dismech
  Disease entry. Covers Harrison's Part assignment, mechanistic nosology,
  lysosomal storage, IUIS immunodeficiency, channelopathy, and ICD-O
  morphology fields, with a lookup table from common clinical phrasing
  to controlled-vocabulary keys.
---

# Adding classifications

The `classifications` block carries multiple disease-taxonomy assignments,
each ranged by its own enum. Curators populate the slot(s) most relevant
to the disease — most entries will set `harrisons_chapter` plus zero or
more of the more specific category slots (`mechanistic_category`,
`lysosomal_storage_category`, etc.).

```yaml
classifications:
  harrisons_chapter:
  - classification_value: ENDOCRINOLOGY_METABOLISM
  - classification_value: GENETICS_ENVIRONMENT_DISEASE
  mechanistic_category:
  - classification_value: tauopathy
```

All `classification_value` slots are enum-typed: free-text values will
fail schema validation. Use the controlled keys below.

## Harrison's Part (`harrisons_chapter`)

Despite the slot name, the controlled vocabulary lives at the **Part**
level of Harrison's Principles of Internal Medicine (21st edition), not
at individual chapter granularity. The full enum is defined in
`src/dismech/schema/dismech.yaml` as `HarrisonsChapterEnum`. The slot is
multivalued — assign every Part that contains a relevant chapter.

### Lookup table (common phrasings → enum key)

Use this table to translate the natural-language category you want to
express into the right enum key.

| You want to say…                                            | Use this key                    |
|-------------------------------------------------------------|---------------------------------|
| cancer / solid tumor / leukemia / lymphoma / sarcoma        | `ONCOLOGY_HEMATOLOGY`           |
| hematologic malignancy / anemia / coagulation disorder      | `ONCOLOGY_HEMATOLOGY`           |
| bacterial / viral / fungal / parasitic / infectious disease | `INFECTIOUS_DISEASES`           |
| cardiomyopathy / coronary / vascular / cardiac channelopathy| `CARDIOVASCULAR`                |
| asthma / COPD / lung / allergic respiratory disease         | `RESPIRATORY`                   |
| sepsis / ARDS / critical illness                            | `CRITICAL_CARE`                 |
| kidney / glomerular / electrolyte / urinary tract           | `KIDNEY_URINARY_TRACT`          |
| GI / hepatic / pancreatic / IBD / peptic                    | `GASTROINTESTINAL`              |
| autoimmune / connective tissue / rheumatology / arthritis   | `IMMUNE_RHEUMATOLOGIC`          |
| musculoskeletal                                             | `IMMUNE_RHEUMATOLOGIC`          |
| diabetes / thyroid / adrenal / pituitary / metabolic        | `ENDOCRINOLOGY_METABOLISM`      |
| inborn error of metabolism (general)                        | `ENDOCRINOLOGY_METABOLISM`      |
| neurodegenerative / movement disorder / epilepsy / stroke   | `NEUROLOGIC`                    |
| psychiatric / demyelinating / neuromuscular                 | `NEUROLOGIC`                    |
| skin disorder                                               | `DERMATOLOGY`                   |
| poisoning / overdose / envenomation                         | `POISONING_ENVENOMATION`        |
| environmental exposure (altitude, radiation, hypothermia)   | `ENVIRONMENTAL_EXPOSURES`       |
| hereditary / RASopathy / ciliopathy / mitochondrial disease | `GENETICS_ENVIRONMENT_DISEASE`  |
| hearing loss / vestibular disorder                          | `DISORDER_OF_EAR`               |
| symptom-defined entry (e.g., chronic pain, fatigue)         | `CARDINAL_MANIFESTATIONS`       |
| does not fit any Part                                       | `OTHER`                         |

### How to pick Parts

- Prefer the **organ-system Part** where Harrison's would publish the
  primary chapter on the disease (e.g., asthma → `RESPIRATORY`, not
  `IMMUNE_RHEUMATOLOGIC`).
- Add a **second Part** when the disease has a major mechanistic axis
  that Harrison's covers separately. Example: Familial Mediterranean
  Fever → `IMMUNE_RHEUMATOLOGIC` (primary clinical home) plus
  `GENETICS_ENVIRONMENT_DISEASE` (Mendelian inheritance is a recurring
  theme).
- Skeletal dysplasias and other hereditary musculoskeletal conditions
  generally go to `GENETICS_ENVIRONMENT_DISEASE`. Reserve
  `IMMUNE_RHEUMATOLOGIC` for inflammatory / immune-mediated entities.
- Cancers always go to `ONCOLOGY_HEMATOLOGY`; an organ-system Part is
  optional and usually unnecessary unless the entry is about an
  organ-specific paraneoplastic syndrome.

### Verifying the enum

```bash
uv run python -c "
import yaml
with open('src/dismech/schema/dismech.yaml') as f:
    data = yaml.safe_load(f)
for k in data['enums']['HarrisonsChapterEnum']['permissible_values']:
    print(k)
"
```

## Other classification slots

The same `classifications` block accepts several more specific taxonomies
when they apply. All use `classification_value:` ranged by their own
enum.

- **`mechanistic_category`** — pathway / mechanism-based nosology
  (`tauopathy`, `synucleinopathy`, `proteotoxic disease`, `RASopathy`,
  `ciliopathy`, `mitochondrial disease`, `intermediate filament
  disease`, etc.). Multivalued.
- **`lysosomal_storage_category`** — biochemical classification of
  lysosomal storage disorders (`glycoproteinosis`, `disorder of
  glycogen metabolism`, etc.). Single-valued.
- **`iuis_category`** — IUIS primary-immunodeficiency classification.
  Single-valued.
- **`channelopathy_category`** — organ-system grouping for
  channelopathies (`cardiac channelopathy`, `neurological
  channelopathy`, etc.). Single-valued.
- **`icdo_morphology`** — ICD-O cancer-morphology category
  (`Carcinoma`, `Adenocarcinoma`, `Sarcoma`, `Leukemia`, `Lymphoma`,
  `Melanoma`, `Glioma`, `Embryonal Neoplasm`, `Squamous Cell
  Carcinoma`). Apply to neoplastic entries.

When the same concept fits both Harrison's and a more specific slot,
**set both**. Example: a tauopathy gets `harrisons_chapter:
NEUROLOGIC` and `mechanistic_category: tauopathy`.

## Validation

```bash
uv run linkml-validate -s src/dismech/schema/dismech.yaml \
  -C Disease kb/disorders/<File>.yaml
```

Schema validation will reject free-text Harrison's values; if you see
``'<value>' is not one of [...]`` for `harrisons_chapter`, look the
phrasing up in the table above and switch to the enum key.
