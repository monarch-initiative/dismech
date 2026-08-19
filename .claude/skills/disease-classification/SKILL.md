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

Every slot in `DiseaseClassifications` renders on the disorder page
automatically — the Classifications card is generated from the schema,
labelled by each slot's LinkML `title`, and grouped by `slot_group`. You
do not need to touch the template when curating, and a slot you populate
will never silently fail to appear.

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
- **`icimd_category`** — International Classification of Inherited
  Metabolic Disorders (ICIMD) category/group. Apply to inherited
  metabolic disorders (inborn errors of metabolism). Multivalued. See
  the dedicated section below.
- **`isds_skeletal_category`** — ISDS Nosology group (2023 revision) for
  genetic skeletal disorders (skeletal dysplasias, dysostoses, metabolic bone
  disorders, skeletal malformation/reduction syndromes). Multivalued in
  the schema, but a single ISDS-listed disorder takes exactly one group.
  See the dedicated section below.
- **`ilo_agent_category`** / **`ilo_disease_category`** — the two orthogonal
  axes of the ILO List of Occupational Diseases (revised 2010). Apply to any
  disease with a recognised occupational form. Both multivalued.
- **`eu_occupational_category`** — item(s) of the European schedule of
  occupational diseases (Rec. 2003/670/EC as amended). Multivalued.
  See the dedicated section below.

## Occupational disease (`ilo_agent_category`, `ilo_disease_category`, `eu_occupational_category`)

Two sanctioned occupational nosologies, plus six **agent-level** exposure axes
that do NOT go in this block. Full guidance:
[`docs/occupational-environmental-classifications.md`](../../../docs/occupational-environmental-classifications.md).

**First, the split that matters.** `classifications:` classifies the *disease*.
Facts about the *agent* — IARC carcinogen group, GHS hazard class, route,
duration, hazard type, exposome domain — belong on the `environmental:` entry
under `exposure_classifications:`, never here. "Benzene is IARC Group 1" is a
statement about benzene, not about any disease it causes.

```yaml
classifications:
  harrisons_chapter:
  - classification_value: RESPIRATORY
  ilo_disease_category:              # sections 2 and 4 -> disease-category axis
  - classification_value: pneumoconiosis_from_fibrogenic_mineral_dust
    notes: 'ILO List of Occupational Diseases (revised 2010), item 2.1.1.'
  eu_occupational_category:
  - classification_value: silicosis
    notes: 'European schedule Annex I item 301.11 "Silicosis".'

environmental:
- name: Occupational Respirable Crystalline Silica Exposure
  exposure_classifications:          # <- agent-level, NOT in classifications:
    hazard_agent_type:
    - classification_value: CHEMICAL
    exposure_route:
    - classification_value: INHALATION
    iarc_carcinogen_group:
      classification_value: GROUP_1
```

**Assign both nosologies when both apply** — they are separate instruments, not
substitutes, and neither implies the other. The EU schedule is finer-grained
(separate items for silicosis 301.11 / asbestosis 301.21 / mesothelioma 301.22
where ILO has one item 2.1.1 plus a cancer item 3.1.1) and uniquely carries
COVID-19 (408) and the 2025 asbestos additions (311–314).

**The ILO list is biaxial — pick the slot by section.** The two axes are
separate slots over separate enums, so a value from one axis will not validate
in the other's slot:

| ILO sections | Slot | Enum | Items name |
|---|---|---|---|
| 1 (chemical/physical/biological agents), 3 (cancer) | `ilo_agent_category` | `ILOCausativeAgentEnum` | the agent |
| 2 (by target organ system), 4 (other diseases) | `ilo_disease_category` | `ILODiseaseCategoryEnum` | the disease |

A disease commonly takes one from each — occupational asthma from isocyanates is
both `isocyanates` (1.1.35, agent slot) and `occupational_asthma` (2.1.7,
disease slot). Both slots stay multivalued because more than one item from a
single axis is normal (silicosis takes 2.1.1 and 2.1.2). Do NOT carry the ISDS
"exactly one group" rule over to this instrument.

The three occupational slots share a LinkML `slot_group`
(`occupational_classification`), but that is display grouping only and enforces
nothing — the separate enum ranges are what bind each axis.

**Assign only when an occupational form is recognised.** An exposure existing is
not enough — lead poisoning from contaminated water is not ILO 1.1.8; lead
poisoning in a smelter worker is. A disease with both occupational and
non-occupational forms (asthma, COPD, mesothelioma, hearing loss) still takes the
item; the assignment records that an occupational form is recognised, not that
every case is occupational. Say which in `notes`.

**Annex II is "suspected", not recognised.** EU keys prefixed `suspected_` come
from Annex II — the additional list of diseases *suspected* of being
occupational. Never report one as a recognised occupational disease; say so in
`notes`.

Record provenance in `notes` (revision, item number, annex). As with ICIMD and
ISDS this is a definitional taxonomy mapping, not an empirical disease claim, so
prefer `notes` over a manufactured evidence `snippet`.

Do NOT put the citing identifier for the *instrument* in `notes` prose — that
lives in the schema, on the enum's `source:` metaslot. The eight European items
added by the 2022 and 2025 amendments additionally carry a per-value `source:`,
so if a value has its own `source` it is a recent addition.

Worked examples: `Silicosis`, `Asbestosis`, `Malignant_Mesothelioma`,
`Noise_Induced_Hearing_Loss`.

## ICIMD (`icimd_category`) — inherited metabolic disorders

For inherited metabolic disorders, assign the ICIMD category/group from
`ICIMDEnum` (defined in `src/dismech/schema/classifications/icimd.yaml`,
transcribed from Ferreira et al. 2021, **PMID:33340416**). ICIMD is a
consensus, mechanism-first nosology of inborn errors of metabolism.

The enum is **hierarchical**: it encodes the 24 ICIMD **categories**
(layer 1) as top-level values and the ~113 disease **groups** (layer 2)
as children that declare their parent category via `is_a`. Both levels
are valid assignments.

**Assign the most specific applicable node** — usually a group. The
parent category is derivable through `is_a`, so you do not also need to
list the category. Assign at category level only when the specific group
is unknown. The slot is multivalued: add more than one node when a
disorder genuinely spans groups.

```yaml
classifications:
  harrisons_chapter:
  - classification_value: ENDOCRINOLOGY_METABOLISM
  icimd_category:
  - classification_value: organic_acidurias        # group; rolls up to amino_acid_metabolism
    notes: >-
      ICIMD (Ferreira et al. 2021, PMID:33340416): group "Organic acidurias"
      under category "Disorders of amino acid metabolism".
```

Record provenance in `notes:` (as above) for the ICIMD assignment. An
ICIMD placement is a *definitional taxonomy* mapping, not an empirical
disease claim, and the ICIMD paper's abstract carries no per-disease
sentence that would serve as an exact-quote `snippet:` supporting a
specific group. A formal `evidence:` block (identical shape to any other
dismech evidence — cached PMID + exact-quote snippet) is still valid and
welcome when a source genuinely states the placement (e.g. the iembase
entry text or a disease-specific review); prefer `notes:` over a generic
snippet that only supports the framework rather than the assignment.

Pair `icimd_category` with `harrisons_chapter` (usually
`ENDOCRINOLOGY_METABOLISM` and/or `GENETICS_ENVIRONMENT_DISEASE`) the
same way other specific taxonomies are set alongside Harrison's. ICIMD
is finer-grained and metabolism-specific; the lysosomal storage diseases
in particular can carry both `lysosomal_storage_category` and an ICIMD
group under `complex_molecule_degradation`.

To list the available categories/groups:

```bash
uv run python -c "
from linkml_runtime.utils.schemaview import SchemaView
sv = SchemaView('src/dismech/schema/dismech.yaml')
for k, pv in sv.get_enum('ICIMDEnum').permissible_values.items():
    print(('  ' if pv.is_a else '') + k + (f'  (is_a {pv.is_a})' if pv.is_a else '  [CATEGORY]'))
"
```

## ISDS Nosology (`isds_skeletal_category`) — genetic skeletal disorders

For genetic skeletal disorders, assign the group from
`ISDSNosologyGroupEnum` (defined in
`src/dismech/schema/classifications/isds_skeletal_nosology.yaml`,
transcribed from the ISDS Nosology of Genetic Skeletal Disorders, 2023
revision — Unger et al., **PMID:36779427**). That revision lists 771
entries across 552 genes in 41 groups, mixing molecular, radiographic,
and anatomical/pathogenetic organizing principles. It supersedes the
2019 revision (Mortier et al., PMID:31633310), whose group names are
retained as `structured_aliases` and whose four dissolved groups are
retained as `deprecated` values — **never assign a deprecated value**.

The enum is **flat**, not hierarchical, and the nosology deliberately
lists each disorder **exactly once**. So:

- **Assign one group.** The slot is multivalued only for an entry that
  lumps several distinct nosology disorders. Do not add a second group
  because the biology overlaps — Table 1 handles overlap with "see
  also" cross-references, not dual membership.
- **Only assign to listed disorders.** This is a transcription of an
  expert nosology, not an inference engine. If the entry is not in
  Table 1 (and is not an unambiguous subtype or synonym of a Table 1
  disorder), leave the slot empty — plenty of disorders with skeletal
  phenotypes were deliberately not included.
- Watch for cross-group traps: FGFR3 craniosynostosis belongs to the
  craniosynostosis group, not the FGFR3 group; Hajdu-Cheney is
  osteolysis, not OI/bone fragility; brachydactyly-hypertension is a
  syndromic brachydactyly, not acromelic.
- **Group numbers are not stable across revisions** — the brachydactyly
  groups moved from 37/38 to 18/19 between 2019 and 2023. Cite the
  group by name and revision in `notes:`, never by bare number.
- **Entities the nosology flags but declines to decompose** get the group on
  the entity only. Fanconi anemia is the worked case: it sits in group 38
  "Limb hypoplasia – reduction defects" in the 2023 revision (group 39 in
  2019 — note the shift, and that 2023 group 39 is a different group,
  "Split hand/foot"). Its gene column reads "(several)" and the group
  footnote says the complementation groups are "acknowledged but not further
  listed". That is a caveat about genetic decomposition, not about membership
  — so assign `limb_hypoplasia_reduction_defects` to Fanconi anemia, note the
  caveat, and do not invent per-complementation-group placements. Assign the
  enum key, not a number: the key is revision-stable, the number is not.

```yaml
classifications:
  harrisons_chapter:
  - classification_value: GENETICS_ENVIRONMENT_DISEASE
  isds_skeletal_category:
  - classification_value: fgfr3_chondrodysplasia
    notes: >-
      ISDS Nosology of Genetic Skeletal Disorders, 2023 revision
      (Unger et al., PMID:36779427), group 1 "FGFR3 chondrodysplasias";
      listed as "Achondroplasia, FGFR3-related".
```

Groups carry no `meaning:`; three carry a `close_mappings:` to a MONDO
class (FGFR3 chondrodysplasias, TRPV4 disorders, and acromesomelic
dysplasias — the gene-defined series). A candidate MONDO
class is rejected whenever it contains an entity ISDS lists in a
*different* group, so do not add mappings without running that check.
See `docs/isds-skeletal-nosology.md` for the accepted and rejected sets.

As with ICIMD, record provenance in `notes:` and prefer it over
`evidence:`. The paper's PubMed record is **abstract-only**, so no
exact-quote snippet from it can support a specific group placement —
the abstract states only that the nosology exists and has 771 entries
across 552 genes in 41 groups. Quote it only if you are supporting *that* framework
claim, never a per-disorder assignment.

To list the groups:

```bash
uv run python -c "
from linkml_runtime.utils.schemaview import SchemaView
sv = SchemaView('src/dismech/schema/dismech.yaml')
for k, pv in sv.get_enum('ISDSNosologyGroupEnum').permissible_values.items():
    print(k, '-', (pv.description or '').split('.')[0])
"
```

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
   just count-verified-snippets kb/disorders/<File>.yaml
   # then, once before the PR: just validate-disorders kb/disorders/<File>.yaml
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
