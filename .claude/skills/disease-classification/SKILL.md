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

## Backing classifications with evidence

Every `classification_value` entry is a `ClassificationAssignment` and
carries optional `evidence:` and `notes:` slots inherited from the base
class. Cite an authoritative source whenever you can — this turns the
classification from "curator opinion" into a checkable annotation and
prevents AI-fabricated taxonomy drift over time.

**Do not** quote Harrison's Principles of Internal Medicine directly:
the textbook is copyrighted and snippets are not redistributable. Cite
the open-access peer-reviewed alternatives below instead. The pattern
is the same as any other dismech evidence block — exact-quote snippet
from the cited reference's abstract or text.

```yaml
harrisons_chapter:
- classification_value: GASTROINTESTINAL
  evidence:
  - reference: PMID:39101000
    supports: SUPPORT
    evidence_source: HUMAN_CLINICAL
    snippet: "Inflammatory bowel disease (IBD), comprising Crohn's disease and ulcerative colitis, is a chronic relapsing inflammatory disorder of the gastrointestinal tract."
    explanation: Recent review characterises IBD as a gastrointestinal-tract inflammatory disorder, supporting placement in Harrison's GI Part.
```

### Authoritative classification sources per Part

For each Part, the table below names a reusable family of citable
sources. Prefer the most disease-specific source available, but these
are good fallbacks when a disorder-specific recent review isn't at
hand.

| Part                              | Authoritative sources to cite (open or freely accessible)                                                                                |
|-----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| `ONCOLOGY_HEMATOLOGY`             | WHO Classification of Tumours (5th edition, IARC "blue books"); WHO Classification of Hematolymphoid Tumours; NCI PDQ; recent NEJM / *Blood* / *JCO* / *Lancet Oncol* / *Nat Rev Cancer* reviews. |
| `INFECTIOUS_DISEASES`             | CDC Yellow Book / NIOSH bulletins; WHO disease fact sheets; recent *Clin Infect Dis* / *Lancet Infect Dis* reviews.                       |
| `CARDIOVASCULAR`                  | ESC / ACC-AHA guideline papers (PMID-citable); *Eur Heart J* / *Circulation* / *JACC* state-of-the-art reviews.                          |
| `RESPIRATORY`                     | GOLD report (COPD); GINA report (asthma); ERS / ATS task-force statements; *Lancet Respir Med* reviews.                                  |
| `CRITICAL_CARE`                   | Surviving Sepsis Campaign guidelines; SCCM / ESICM consensus papers; *Intensive Care Med* / *Crit Care Med* reviews.                     |
| `KIDNEY_URINARY_TRACT`            | KDIGO clinical practice guideline papers; *Kidney Int* / *JASN* reviews.                                                                  |
| `GASTROINTESTINAL`                | ACG / AGA / ESGE practice guidelines; *Lancet Gastroenterol Hepatol* / *Gastroenterology* / *Hepatology* reviews.                        |
| `IMMUNE_RHEUMATOLOGIC`            | ACR / EULAR classification-criteria papers (these are *literally* classification papers); *Lancet* / *NEJM* / *Nat Rev Rheumatol* reviews. |
| `ENDOCRINOLOGY_METABOLISM`        | ADA *Standards of Care*; Endocrine Society clinical practice guidelines; ESPE consensus statements; *J Clin Endocrinol Metab* reviews.    |
| `NEUROLOGIC`                      | AAN practice guidelines; Movement Disorder Society criteria; International League Against Epilepsy (ILAE) classification papers; *Lancet Neurol* reviews. |
| `DERMATOLOGY`                     | AAD / EADV consensus papers; *J Am Acad Dermatol* / *Br J Dermatol* reviews.                                                              |
| `POISONING_ENVENOMATION`          | AACT / ACMT / EAPCCT position statements; *Clin Toxicol* reviews; WHO/IPCS environmental health criteria.                                 |
| `ENVIRONMENTAL_EXPOSURES`         | IARC Monographs on carcinogenic risk; NIEHS / EPA assessments; *Environ Health Perspect* reviews.                                         |
| `GENETICS_ENVIRONMENT_DISEASE`    | OMIM phenotype entries (cite via PMID of the OMIM-summary paper); MONDO/Orphanet (use the structured `ORPHA:` prefix for Orphadata entries — see `CLAUDE.md`); GeneReviews (cite via PMID). |
| `DISORDER_OF_EAR`                 | AAO-HNSF clinical practice guidelines; *Otolaryngol Clin North Am* reviews.                                                               |
| `AGING`                           | American Geriatrics Society (AGS) consensus statements; *J Am Geriatr Soc* reviews.                                                       |
| `CARDINAL_MANIFESTATIONS`         | Symptom-focused systematic reviews in general internal-medicine journals (*Ann Intern Med*, *JAMA*, *BMJ*).                              |
| `GLOBAL_MEDICINE`                 | WHO position papers; *Lancet Global Health* / *Lancet* commission reports.                                                                |
| `CONSULTATIVE_MEDICINE`           | Hospital-medicine / perioperative-medicine society consensus papers; *J Hosp Med* reviews.                                                |

### Structured sources are first-class evidence

When the cited source is already in dismech's structured cache
(currently Orphanet and ClinGen — see `CLAUDE.md`), prefer the
structured prefix over a free-text PMID for classification evidence:

```yaml
harrisons_chapter:
- classification_value: GENETICS_ENVIRONMENT_DISEASE
  evidence:
  - reference: ORPHA:558
    supports: SUPPORT
    snippet: "Marfan syndrome is a systemic disease of connective tissue"
    explanation: Orphanet classifies Marfan as a systemic connective-tissue disorder of Mendelian inheritance.
```

These structured snippets are deterministic (Orphadata is refreshed
from a pinned XML manifest) and never drift in wording.

### Workflow for adding classification evidence

1. **Pick the cited source.** Prefer (a) an existing reference already
   on the disease entry that characterises the disease's category,
   (b) a structured prefix (`ORPHA:`, `CGGV:`, `CGDS:`) if applicable,
   or (c) a fresh authoritative paper from the table above.
2. **Cache it** if it's a literature reference and not yet present:
   ```bash
   just fetch-reference PMID:XXXX
   ```
3. **Write the evidence block** with an *exact-quote* snippet from the
   cached abstract that itself frames the disease in the classification's
   terms (e.g., "is a chronic kidney disease characterised by…").
4. **Validate**:
   ```bash
   just validate kb/disorders/<File>.yaml
   just validate-references kb/disorders/<File>.yaml
   ```

### Auditing missing classification evidence

```bash
uv run python - <<'PY'
from pathlib import Path
from ruamel.yaml import YAML
y = YAML(typ='safe')
for p in sorted(Path("kb/disorders").glob("*.yaml")):
    data = y.load(p.read_text()) or {}
    items = ((data.get("classifications") or {}).get("harrisons_chapter") or [])
    for it in items:
        if isinstance(it, dict) and not it.get("evidence"):
            print(f"{p.name}\t{it.get('classification_value')}")
PY
```

## Validation

```bash
uv run linkml-validate -s src/dismech/schema/dismech.yaml \
  -C Disease kb/disorders/<File>.yaml
```

Schema validation will reject free-text Harrison's values; if you see
``'<value>' is not one of [...]`` for `harrisons_chapter`, look the
phrasing up in the table above and switch to the enum key.
