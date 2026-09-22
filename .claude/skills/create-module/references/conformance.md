# Module conformance and categories

### Mechanism Modules

Mechanism modules (`kb/modules/`) define conserved pathological processes that recur across
multiple disorders (e.g., the fibrotic response). A module uses the **same schema** as a
regular dismech Disease entry — it has `pathophysiology` nodes with cell types, biological
processes, evidence, and causal edges (`downstream`).

**How conformance works:**

Individual disorder entries declare that a pathophysiology node conforms to a module node
using the `conforms_to` slot:

```yaml
# In kb/disorders/Liver_Cirrhosis.yaml
pathophysiology:
- name: Hepatic Stellate Cell Activation
  conforms_to: "fibrotic_response#Mesenchymal Cell Activation"
  cell_types:
  - preferred_term: Hepatic Stellate Cell
    term:
      id: CL:0000632
      label: hepatic stellate cell
  biological_processes:
  - preferred_term: TGF-beta Receptor Signaling
    term:
      id: GO:0007179
      label: transforming growth factor beta receptor signaling pathway
    modifier: INCREASED
```

**Key principles:**
- **Same schema**: Modules validate against the `Disease` class, just like disorder files
- **Not DRY**: Disorder entries fully duplicate content; conformance is for consistency checking, not inheritance
- **Organ-specific substitution**: Module nodes define generic cell types (e.g., `fibroblast`); conforming disorder nodes substitute organ-specific types (e.g., `hepatic stellate cell`)
- **Consistency checking**: If a node declares `conforms_to`, it should include the expected biological processes and causal edges from the module
- **Reference format**: `"module_name#Node Name"` — module name matches the filename in `kb/modules/` (without `.yaml`), node name matches a pathophysiology `name` in that module

**Creating a module?** Use the `create-module` skill — it covers the module
schema shape, the trigger→consequence node chain, the treatment
`target_mechanisms` drug pattern, evidence discipline, and the **Xogenesis**
(pathological-structure-formation) open-ontology anchor convention (OGMS process
+ MPATH entity + UBERON site; SNOMED as guide-only). See also the primer
`docs/primers/modules-and-conformance.md`.

**Discovering modules:** the set of modules changes constantly, so this file
deliberately does **not** carry a hand-maintained list — it drifted behind
`kb/modules/` and is not scalable. List the directory, or use the recipe that
prints each module's description plus its node chain (the `module#Node Name`
strings you need for `conforms_to`):

```bash
just list-modules            # all modules, clipped, with conformance targets
just list-modules inflamm    # filter: prints description AND notes in full
ls kb/modules/               # bare names only

# Probing module contents directly (complements the recipe above)
rg -il "<mechanism term>" kb/modules          # which module already covers this?
rg -n "conforms_to:.*fibrotic_response#" kb/disorders kb/comorbidities kb/modules
```

Inspect likely matches before creating a new module — a mechanism is often
already covered by a module under a name you did not guess.

A module's own `description` is the authoritative statement of its scope,
complementarity with sibling modules, worked conformers, and key conformance
target. Read it before conforming to it, and keep it current when you change the
module — that description is now the *only* place that information lives.

**Module collections:** records in `kb/module_collections/` organize modules
into a published framework or another explicit navigational family. They
validate against `ModuleCollection`, not `Disease`, and use module filename
stems (without node anchors) as members. A collection is not a mechanism,
does not replace the module directory as the complete registry, and does not
assert disease membership. One module may belong to several collections.

Thematic families to be aware of when picking a conformance target (find their
members with `just list-modules`, do not assume this list is exhaustive):

- **Hallmarks of cancer** (Hanahan & Weinberg, PMID:21376230) — a coherent set
  covering the hallmark capabilities and enabling characteristics. A neoplastic
  entry may declare `conforms_to` against several in parallel, one per capability
  it manifests, substituting tumor-type-specific drivers. Flagship multi-hallmark
  conformers: Hepatocellular_Carcinoma, Non-Small_Cell_Lung_Cancer,
  Glioblastoma_IDH_Wildtype, Pancreatic_Ductal_Adenocarcinoma.
- **Hallmarks of aging** (Lopez-Otin et al.) — the senescence, telomere,
  proteostasis, autophagy, nutrient-sensing, epigenetic, mitochondrial,
  stem-cell, dysbiosis, and inflammaging modules. Most carry a `biochemical:`
  biomarker block with `BiomarkerReadout` links (`grep -l '^biochemical:'
  kb/modules/*.yaml` for the current set); `cellular_senescence` and `inflammaging`
  are the pattern to copy. **Before adding a composite marker
  here** — an epigenetic clock, a multi-analyte panel, a frailty index — read the
  decision register entry *Computed indices and composite endpoints in aging biology*
  (`docs/explanation/design-decisions.md` §12). dismech has no class for a value
  computed over other measurements, the question is undecided, and the interim
  conventions (bind the assay, carry the index identity in `preferred_term`) are
  recorded there rather than being rederived per module. NCIT has no term for an
  epigenetic clock or biological age; do not bind one to `NCIT:C17961` or
  `NCIT:C16269`. Background: [biomarkers-of-aging gap analysis](../../../../docs/reports/biomarkers-of-aging-gap-analysis-2026-08-31.md).
- **Treatment toxicity / "side effect as mechanism"** — adverse-drug-reaction
  pathophysiology recurring across culprit drugs, so a drug-toxicity entry can
  conform rather than re-derive the chain. Note that several general mechanism
  modules already double as toxicity targets without a separate "side effect"
  class (`peripheral_axonal_degeneration` for chemotherapy-induced peripheral
  neuropathy, `cardiomyopathy_maladaptive_remodeling` for anthracycline
  cardiotoxicity). `cardiac_ion_channel_repolarization` is **not** one of them,
  despite drug-induced long QT being a real entity: that module scopes itself to
  inherited arrhythmia syndromes *in structurally normal hearts*, its notes list
  only heritable syndromes, and its sole mention of acquired repolarization
  change sits inside a quoted snippet. An acquired drug-induced long-QT module
  would be a new module, not a second use of that one.
- **Antimicrobial drug mechanisms** — antibacterial target modules (cell wall,
  ribosome, topoisomerase, RNA polymerase, folate), antifungal and antiviral
  counterparts, plus pharmacokinetic *gating* modules such as
  `intracellular_pathogen_persistence`. A disease usually conforms to a gating
  module **and** a target module. See `projects/ANTIMICROBIAL.md`.
- **"Disease-like phenotypes"** — final-common-pathway modules for phenotypes
  that are themselves diseases, carrying both an HP and a MONDO identifier
  (osteoporosis, glaucoma, cataract, epilepsy, nephrotic syndrome, …). Each is a
  recurrent downstream convergence point across many disorders.
- **Serial homology** — bundled multi-element malformations from one lesion in a
  serially reused developmental program (limb/digit, pharyngeal arch, axial
  segmentation).
- **Xogenesis** — pathological-structure formation (granuloma, thrombus,
  atheroma, amyloid deposit), using the OGMS + MPATH + UBERON anchor convention
  described in the `create-module` skill.

**Module categories (`module_categories`):**

A module may be tagged with the areas of study it is relevant to, using the
enum-backed `module_categories` slot (`ModuleCategoryEnum`: `TOXICOLOGY`,
`PHARMACOLOGY`, `ONCOLOGY`, `INFECTIOUS_DISEASE`, `IMMUNOLOGY`, `NEUROSCIENCE`,
`DEVELOPMENTAL_BIOLOGY`, `METABOLISM`, `AGING`). Each value asserts *"this
module is relevant to this area of study"* and renders as a coloured pill on the
module index card and at the top of the module page, with the enum's own
`description` as the hover text.

```yaml
name: Parkinsonism Dopaminergic Degeneration Module
category: Module
module_categories:
- TOXICOLOGY
- NEUROSCIENCE
```

- **It is a browsing aid, not a mechanistic claim.** The pill says a toxicologist
  would find this module relevant; it does not assert that the module's diseases
  are toxic in origin, and it is not a classification of conforming disorders
  (those use `classifications`).
- **Multivalued and non-exclusive.** A drug-toxicity module is both `TOXICOLOGY`
  and `PHARMACOLOGY`; an antiviral drug-target module is both `PHARMACOLOGY` and
  `INFECTIOUS_DISEASE`. Tag every area that genuinely applies.
- **Leaving a module untagged is a legitimate outcome.** The starter vocabulary
  is a set of disciplines, not a partition of the corpus — the cardiovascular,
  dermatology, renal, GI and ophthalmology modules currently carry no category
  because no value fits, and a wrong pill is worse than no pill. Add a value to
  the enum rather than stretching an existing one.
- **The vocabulary and its prose live only in the schema.** Labels come from each
  permissible value's `title`, hover text from its `description`; pill colours are
  generated from the value's position in the enum (golden-angle hues at fixed
  saturation/lightness), so adding a category is a schema edit alone — no colour
  to choose and no renderer change. Appending a value leaves existing hues
  untouched; reordering or removing one reshuffles them.
- **That holds up to 13 categories.** The golden-angle walk keeps a minimum
  separation of ~20° through the 13th value and drops to ~12° at the 14th, where
  `test_every_category_gets_a_visually_distinct_hue` goes red. That test is the
  tripwire, not a nuisance: at 14 the palette needs a real decision (a second
  visual dimension, or grouping categories into families), and the enum has
  outgrown "just append a value".
- The slot lives on the `Disease` class because modules validate against it. It is
  intended for `kb/modules/` entries; disorder entries use the separate free-text
  `categories` slot for nosological grouping, which is unrelated.

**Module-level hypotheses and gaps:**
- Modules may define `mechanistic_hypotheses` just like disease entries. Use stable `hypothesis_group_id` values for canonical, alternative, or emerging mechanism groupings.
- Causal edges opt into those groups with `downstream[].hypothesis_groups`. In conforming disorder entries, copy and specialize the same grouping only when the disease-specific causal edge belongs to that model.
- An `Experiment` records references and observed outcomes in different slots.
  `would_support` / `would_refute` take entity references such as
  `pathophysiology#Motor Neuron Degeneration`; `supporting_outcome` /
  `refuting_outcome` take prose describing what would be observed. Do not put
  prose in the reference slots.
- Knowledge gaps should currently use `discussions` with `kind: KNOWLEDGE_GAP`, `attaches_to`, and optional `proposed_experiments`. A separate structural `knowledge_gaps:` slot is still a schema follow-up; do not invent it in YAML entries yet.
- For the specific case where model-system evidence exists but its fidelity to human biology is uncertain (e.g., mouse knockout does not reproduce the human phenotype, lissencephalic models lack human-specific outer radial glia/OSVZ biology, organoid data are not confirmed in human tissue), use `kind: HUMAN_MODEL_MISMATCH` instead of the generic `KNOWLEDGE_GAP`. Key distinction: `KNOWLEDGE_GAP` means evidence is absent; `HUMAN_MODEL_MISMATCH` means evidence exists in a model but translational validity to human disease is the open question. Include a `prompt` that states the mismatch explicitly as a question, a `rationale` explaining why the mismatch is mechanistically meaningful, and `proposed_experiments` mapping to the experiments needed to resolve it. See the Autosomal_Recessive_Primary_Microcephaly entry for a worked example.
