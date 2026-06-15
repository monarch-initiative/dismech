# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the **Disorder Mechanisms Knowledge Base (dismech)** - a LinkML-based knowledge base storing disease pathophysiology information. It combines:
1. A LinkML schema defining the data model (`src/dismech/schema/dismech.yaml`)
2. A knowledge base of disorder YAML files (`kb/disorders/*.yaml`)
3. HTML rendering for browsable disorder pages (`pages/disorders/*.html`)

## Design Decisions

Before making structural, scope, ontology, BioLink/KGX, or evidence-policy choices,
consult the decision register at
[`docs/explanation/design-decisions.md`](docs/explanation/design-decisions.md). It records
*why* the project is built the way it is — project scope (what is/isn't a dismech entry),
the LinkML schema choice, the constrained ontology set, export-layer-only BioLink reuse,
the evidence/provenance policy, curation governance, and a tracked list of open/deferred
decisions. Cite it when a recorded decision is relevant; if a decision looks wrong or
stale, surface it rather than silently contradicting it. The specifics below in this file
remain authoritative for day-to-day curation mechanics.

## Skills

Claude Code skills are available in `.claude/skills/`:

- **dismech-terms**: Use when adding ontology term annotations (HPO phenotypes, CL cell types, GO processes, MAXO treatments). Covers term lookup with OAK, specificity guidelines, and validation.
- **dismech-references**: Use when validating/repairing evidence references. Ensures snippets match PubMed abstracts and catches AI hallucinations.

## Key Commands

```bash
# Install dependencies
just install

# Run all QC checks (validation + term validation)
just qc

# Validate all disorder YAML files against schema
just validate-all

# Validate a single disorder file
just validate kb/disorders/Asthma.yaml

# Validate ontology term references in schema (anti-hallucination check)
just validate-terms

# Run pytest tests
just pytest-all

# Run a single test
uv run pytest tests/test_data.py -k "test_name" -v

# Generate HTML pages for all disorders
uv run python -m dismech.render --all

# Generate HTML for a single disorder
uv run python -m dismech.render kb/disorders/Asthma.yaml

# Fetch and cache a reference (PMID, DOI, NCT) — NEVER create cache files manually
just fetch-reference PMID:12345678

# Validate references for a single file
just validate-references kb/disorders/Asthma.yaml

# List all available commands
just --list
```

## Architecture

### Schema (`src/dismech/schema/dismech.yaml`)
- LinkML schema defining Disease, Pathophysiology, Phenotype, EvidenceItem, etc.
- Uses ontology term bindings (HP, GO, GENO, MONDO, MAXO, etc.) with `meaning` fields
- Dynamic enums with `reachable_from` constraints for ontology validation
- Descriptor classes (PhenotypeDescriptor, CellTypeDescriptor, TreatmentDescriptor) bind entities to ontology terms

### Knowledge Base (`kb/disorders/`)
- One YAML file per disorder (55 total)
- Each file validates against the `Disease` class in the schema
- Evidence items require PMID references
- Ontology term bindings for phenotypes, cell types, biological processes, and treatments

### Ontology Configuration (`conf/oak_config.yaml`)
Maps ontology prefixes to OAK adapters for term validation:
- HP, CL, GO, MONDO, UBERON, CHEBI, GENO, HGNC → `sqlite:obo:<name>`
- MAXO (Medical Action Ontology) for treatment terms
- NCIT (NCI Thesaurus) for cancer/treatment concepts

### CURIE Prefix Casing

HGNC gene CURIEs use **lowercase** `hgnc:` prefix in this repo (e.g., `hgnc:746`, not `HGNC:746`). This is the canonical form that passes term validation. Do not flag lowercase `hgnc:` as an error in reviews.

### HTML Rendering (`src/dismech/render.py`)
- Jinja2 templates in `src/dismech/templates/`
- Generates browsable HTML pages in `pages/disorders/`
- Links ontology terms to external browsers (HPO JAX, MONDO Monarch, OLS, etc.)

### Scripts (`scripts/`)
- `add_maxo_terms.py`: Batch-add MAXO treatment terms to disorder files

### Structured-Database Sources (`src/dismech/structured_sources/`)
- Framework for ingesting structured knowledge bases (Orphanet, ClinGen; OMIM /
  MONDO / HGNC pluggable) into `references_cache/` as line-oriented markdown
- Flagship: `OrphanetSource` — pre-caches all 8,823 leaf disorders from
  Orphadata XML so curators can cite `ORPHA:<code>` and quote individual rows
  (definition, prevalence, HPO phenotypes, gene-disease, xrefs)
- `ClinGenSource` — pre-caches ClinGen Gene-Disease Validity assertions from
  the public CSV so curators can cite `CGGV:<assertion_id>` and quote the
  gene-disease validity row
- See "Structured-Database Reference Sources" below

### Validation Stack
- **linkml-validate**: Schema conformance checking
- **linkml-term-validator**: Validates ontology term references against authoritative sources (critical for catching AI hallucinations)
- **linkml-reference-validator**: Validates that quoted text appears in cited references

## Important Patterns

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

**Available modules:**
- `fibrotic_response` — Conserved fibrotic response: tissue injury → inflammation → mesenchymal cell activation → myofibroblast → excessive ECM → organ dysfunction
- `immune_checkpoint_blockade` — Conserved tumor-immune evasion pattern: neoantigen generation → anti-tumor T cell response → adaptive immune resistance (PD-L1 upregulation) → T cell exhaustion and immune escape. Drug mechanism design pattern: checkpoint inhibitor treatments use `target_mechanisms` to link back to the "Adaptive Immune Resistance" node they inhibit. Key conformance target: `immune_checkpoint_blockade#Adaptive Immune Resistance`
- `dna_repair_synthetic_lethality` — Conserved HRR/FA-BRCA deficiency pattern: HRR or FA/BRCA repair deficiency → replication-associated DNA damage accumulation → PARP/platinum synthetic lethality → POLQ/error-prone repair escape → restored HRR and acquired resistance. Key conformance target: `dna_repair_synthetic_lethality#PARP and Platinum Synthetic Lethality`
- `rtk_grb2_signaling_adaptation` — Conserved RTK/GRB2 adaptor pattern: activated RTK phosphotyrosine docking → GRB2 adaptor hub → RAS-MAPK/PI3K-AKT proliferation output, with an emerging GRB2-RAD51 replication-fork protection branch. Key conformance target: `rtk_grb2_signaling_adaptation#GRB2 Adaptor Hub`
- `parp_parg_macrodomain_viral_evasion` — Conserved antiviral ADP-ribosylation pattern: viral/interferon PARP induction → NAD-dependent antiviral ADP-ribosylation → PARG/host reset → viral macrodomain de-ADP-ribosylation countermeasure → enhanced viral replication/pathogenesis. Key conformance target: `parp_parg_macrodomain_viral_evasion#Viral Macrodomain De-ADP-Ribosylation Countermeasure`
- `lysosomal_substrate_accumulation` — Conserved lysosomal storage disease pattern: lysosomal hydrolase/cofactor deficiency → undegraded substrate accumulation in the lysosome → autophagic-lysosomal dysfunction and secondary cascade → storage-cell cytotoxicity and neuroinflammation → progressive multisystem/neurodegenerative disease. Conforming disorder nodes substitute the disorder-specific deficient enzyme, stored substrate, and storage cell type (e.g., glucocerebrosidase/glucocerebroside/Gaucher cell; hexosaminidase/GM2 ganglioside/neuron; alpha-galactosidase A/Gb3/endothelium). Key conformance target: `lysosomal_substrate_accumulation#Lysosomal Substrate Accumulation`
- `aortopathy_tgfbeta_dysregulation` — Conserved heritable thoracic aortic aneurysm/dissection (TAAD) pattern: aortic-wall ECM or smooth-muscle contractile-apparatus defect → paradoxically increased TGF-beta signaling dysregulation → medial degeneration (smooth muscle cell depletion + elastic fiber fragmentation) and wall weakening → progressive aortic dilation/aneurysm → aortic dissection and rupture. Conforming disorder nodes substitute the disorder-specific primary lesion (FBN1 microfibril deficiency in Marfan/Shprintzen-Goldberg; TGFBR1/2, SMAD3, TGFB2/3 in Loeys-Dietz; COL3A1 in vascular Ehlers-Danlos; SLC2A10 in arterial tortuosity; ACTA2/MYH11/MYLK/PRKG1 in nonsyndromic familial TAAD). Key conformance target: `aortopathy_tgfbeta_dysregulation#TGF-beta Signaling Dysregulation`
- `ciliopathy_dysfunction` — Conserved ciliopathy module: basal body/transition zone/IFT defect → impaired Hedgehog and Wnt/PCP signaling → retinal, renal, skeletal, CNS, and metabolic pleiotropy; parallel motile-cilia arm (axonemal dynein defect → mucociliary clearance deficit and laterality defects) for primary ciliary dyskinesia. Key conformance targets: `ciliopathy_dysfunction#Basal Body and Transition Zone Dysfunction`, `ciliopathy_dysfunction#Impaired Hedgehog Signal Transduction`, `ciliopathy_dysfunction#Motile Cilia Beat Dysfunction`
- `cardiac_ion_channel_repolarization` — Conserved cardiac channelopathy pattern: cardiac ion-channel or calcium-handling variant → altered action-potential duration / Ca²⁺ handling → arrhythmogenic substrate and triggered activity (EADs/DADs, dispersion of repolarization, reentry) → ventricular tachyarrhythmia → syncope and sudden cardiac death, with a parallel sinoatrial-node automaticity-failure branch producing bradyarrhythmia. For inherited arrhythmia syndromes in structurally normal hearts (Long QT, Short QT, Brugada, RYR2-CPVT, Timothy, torsade/short-coupled VF, familial sick sinus). Key conformance target: `cardiac_ion_channel_repolarization#Arrhythmogenic Substrate and Triggered Activity`

The following modules capture conserved final-common-pathway mechanisms of **"disease-like phenotypes"** — phenotypes that are themselves diseases, carrying both an HP and a MONDO identifier (e.g. osteoporosis, glaucoma). Each is a recurrent downstream convergence point across many disorders:
- `osteoporosis_bone_resorption` — Conserved low-bone-mass pattern (HP:0000939): bone remodeling imbalance → RANKL-driven osteoclastogenesis → increased osteoclastic bone resorption → impaired osteoblastic formation → net bone loss and skeletal fragility. Key conformance target: `osteoporosis_bone_resorption#Increased Osteoclastic Bone Resorption`
- `glaucoma_optic_neuropathy` — Conserved glaucomatous optic neuropathy (HP:0000501): trabecular meshwork outflow dysfunction → elevated intraocular pressure → retinal ganglion cell apoptosis → optic nerve degeneration/neuroinflammation → progressive optic neuropathy. Key conformance target: `glaucoma_optic_neuropathy#Retinal Ganglion Cell Apoptosis`
- `cataract_lens_opacification` — Conserved lens opacification (HP:0000518): lens homeostasis insult → loss of crystallin solubility/chaperone capacity → crystallin aggregation → loss of refractive transparency → cataract. Key conformance target: `cataract_lens_opacification#Crystallin Aggregation and High-Molecular-Weight Complex Deposition`
- `pulmonary_vascular_remodeling` — Conserved pulmonary arterial hypertension (HP:0002092): endothelial/BMPR2 dysfunction → PASMC proliferation/vasoconstriction → obstructive vascular remodeling → increased pulmonary vascular resistance → PAH with RV overload. Key conformance target: `pulmonary_vascular_remodeling#Obstructive Pulmonary Vascular Remodeling`
- `cardiomyopathy_maladaptive_remodeling` — Conserved structural/contractile cardiomyopathy (HP:0001638; distinct from the electrical `cardiac_ion_channel_repolarization` module): cardiomyocyte insult → neurohormonal activation → ventricular remodeling → contractile dysfunction → heart failure. Key conformance target: `cardiomyopathy_maladaptive_remodeling#Ventricular Remodeling`
- `gout_urate_crystal_inflammation` — Conserved gouty arthropathy (HP:0001997): hyperuricemia → monosodium urate crystal deposition → NLRP3 inflammasome activation → IL-1-driven neutrophilic inflammation → recurrent/chronic tophaceous gout. Key conformance target: `gout_urate_crystal_inflammation#NLRP3 Inflammasome Activation`
- `pancreatitis_acinar_autodigestion` — Conserved pancreatitis (HP:0001733): premature intra-acinar trypsinogen activation → calcium overload/impaired autophagy → acinar autodigestion and necrosis → local/systemic inflammation → pancreatitis. Key conformance target: `pancreatitis_acinar_autodigestion#Acinar Cell Autodigestion and Necrosis`
- `epilepsy_excitation_inhibition_imbalance` — Conserved epilepsy (HP:0001250): ion-channel/synaptic dysfunction → excitation/inhibition imbalance → neuronal hyperexcitability and hypersynchrony → seizure generation/epileptogenesis → recurrent unprovoked seizures. Key conformance target: `epilepsy_excitation_inhibition_imbalance#Excitation-Inhibition Imbalance`
- `hypothyroidism_thyroid_hormone_deficiency` — Conserved hypothyroidism (HP:0000821): impaired thyroid hormone synthesis → hormone insufficiency with TSH feedback → reduced peripheral hormone action → decreased metabolic rate → systemic hypometabolic state. Key conformance target: `hypothyroidism_thyroid_hormone_deficiency#Thyroid Hormone Insufficiency`
- `nephrotic_podocyte_injury` — Conserved nephrotic syndrome (HP:0000100): podocyte injury → foot process effacement/slit diaphragm disruption → glomerular filtration barrier breakdown → massive proteinuria with podocyte loss → nephrotic syndrome. Key conformance target: `nephrotic_podocyte_injury#Glomerular Filtration Barrier Breakdown`
- `photoreceptor_degeneration` — Conserved inherited retinal degeneration / retinitis pigmentosa (HP:0000510): photoreceptor gene defect → metabolic/oxidative stress → rod photoreceptor apoptosis → secondary cone degeneration → progressive visual field loss. Key conformance target: `photoreceptor_degeneration#Rod Photoreceptor Apoptosis`
- `nephrolithiasis_crystal_nucleation` — Conserved kidney-stone formation (HP:0000787): urinary supersaturation → crystal nucleation/growth → crystal retention and epithelial adhesion → tubular injury/inflammation → symptomatic kidney stones. Key conformance target: `nephrolithiasis_crystal_nucleation#Crystal Retention and Epithelial Adhesion`
- `cholelithiasis_biliary_supersaturation` — Conserved cholesterol gallstone formation (HP:0001081): biliary cholesterol supersaturation → cholesterol crystal nucleation → gallbladder hypomotility/bile stasis → gallstone aggregation → cholelithiasis. Key conformance target: `cholelithiasis_biliary_supersaturation#Biliary Cholesterol Supersaturation`
- `osteoarthritis_cartilage_degradation` — Conserved osteoarthritis (HP:0002758): mechanical overload/chondrocyte stress → catabolic chondrocyte phenotype with cytokine signaling → matrix-degrading enzyme upregulation (MMP-13/ADAMTS) → cartilage matrix loss and subchondral bone remodeling → joint degradation. Key conformance target: `osteoarthritis_cartilage_degradation#Matrix-Degrading Enzyme Upregulation`
- `sensorineural_hair_cell_loss` — Conserved sensorineural hearing loss (HP:0000407): cochlear sensory epithelium insult → ionic homeostasis disruption/oxidative stress → hair cell mechanotransduction failure and death → spiral ganglion degeneration → progressive sensorineural hearing loss. Key conformance target: `sensorineural_hair_cell_loss#Hair Cell Mechanotransduction Failure and Death`
- `hemolytic_anemia_erythrocyte_destruction` — Conserved hemolytic anemia (HP:0001878): reduced erythrocyte integrity → oxidative/membrane injury → premature erythrocyte destruction (erythrophagocytosis/intravascular hemolysis) → shortened RBC lifespan with erythropoietic strain → hemolytic anemia. Key conformance target: `hemolytic_anemia_erythrocyte_destruction#Premature Erythrocyte Destruction`
- `hepatic_steatosis_lipotoxicity` — Conserved fatty liver disease (HP:0001397): hepatocyte lipid overload → lipotoxic stress and organelle dysfunction → hepatocyte injury and inflammation (steatohepatitis) → stellate cell activation/fibrosis (feeds `fibrotic_response`) → steatosis progressing to fibrosis. Key conformance target: `hepatic_steatosis_lipotoxicity#Lipotoxic Stress and Organelle Dysfunction`
- `peripheral_axonal_degeneration` — Conserved peripheral neuropathy (HP:0009830): insult to peripheral neurons/Schwann cells → axonal transport/mitochondrial dysfunction → distal axonal degeneration/demyelination → length-dependent fiber dysfunction → peripheral neuropathy. Key conformance target: `peripheral_axonal_degeneration#Distal Axonal Degeneration and Demyelination`
- `cerebellar_purkinje_degeneration` — Conserved cerebellar ataxia (HP:0001251): cerebellar neuron insult → Purkinje cell calcium/proteostasis dysregulation → Purkinje neuron degeneration → loss of cerebellar cortical output → cerebellar ataxia. Key conformance target: `cerebellar_purkinje_degeneration#Purkinje Neuron Degeneration`
- `emphysema_protease_antiprotease_imbalance` — Conserved emphysema (HP:0002097): oxidant/inflammatory trigger → protease-antiprotease imbalance → alveolar ECM/elastin destruction → alveolar wall destruction and airspace enlargement → emphysema. Key conformance target: `emphysema_protease_antiprotease_imbalance#Protease-Antiprotease Imbalance`

**Module-level hypotheses and gaps:**
- Modules may define `mechanistic_hypotheses` just like disease entries. Use stable `hypothesis_group_id` values for canonical, alternative, or emerging mechanism groupings.
- Causal edges opt into those groups with `downstream[].hypothesis_groups`. In conforming disorder entries, copy and specialize the same grouping only when the disease-specific causal edge belongs to that model.
- Knowledge gaps should currently use `discussions` with `kind: KNOWLEDGE_GAP`, `attaches_to`, and optional `proposed_experiments`. A separate structural `knowledge_gaps:` slot is still a schema follow-up; do not invent it in YAML entries yet.
- For the specific case where model-system evidence exists but its fidelity to human biology is uncertain (e.g., mouse knockout does not reproduce the human phenotype, lissencephalic models lack human-specific outer radial glia/OSVZ biology, organoid data are not confirmed in human tissue), use `kind: HUMAN_MODEL_MISMATCH` instead of the generic `KNOWLEDGE_GAP`. Key distinction: `KNOWLEDGE_GAP` means evidence is absent; `HUMAN_MODEL_MISMATCH` means evidence exists in a model but translational validity to human disease is the open question. Include a `prompt` that states the mismatch explicitly as a question, a `rationale` explaining why the mismatch is mechanistically meaningful, and `proposed_experiments` mapping to the experiments needed to resolve it. See the Autosomal_Recessive_Primary_Microcephaly entry for a worked example.

### Disease Groupings

Disease groupings (`kb/groupings/`) are explicit, curated **unions** of distinct
`Disease` entries, assembled *below* the level of the `classifications` taxonomies.
The canonical example is the mucopolysaccharidoses (MPS), which group the separate
Hurler / Hunter / Sanfilippo / Morquio entries. Groupings validate against the
**`Grouping`** class (not `Disease`).

**Design principles:**
- **Point down, not up.** A grouping explicitly *lists its members* (`members:`)
  rather than being inferred from them. It is a union model.
- **Not a re-implementation of MONDO.** An optional `mappings:` block may
  cross-reference a MONDO grouping term, but the grouping stands on its own curated
  rationale — do not try to recapitulate the ontology hierarchy.
- **The boundary is auditable.** `grouping_basis` (multivalued enum: `SHARED_MECHANISM`,
  `SHARED_GENE_FAMILY`, `SHARED_PATHWAY`, `SHARED_PHENOTYPE`, `SHARED_TREATMENT_RESPONSE`,
  `CLINICAL_CONVENTION`, `OTHER`) records *why* the members belong together, and
  `grouping_rationale` (free text) explains the lump/keep-split decision. Note: "lump
  vs split" is a statement about the *entities* and lives in the individual `Disease`
  entries; a grouping sits *over* already-distinct entries, so it carries a
  `grouping_rationale`, not a `LUMP` flag.

**Membership criteria — text plus structured boolean (OWL-lite):**

`membership_criteria` is a multivalued list; each block pairs a required
human-readable `description` with an optional nested boolean `logic` expression
(`LogicalCriterion`) and a `criteria_semantics` marker. Branch nodes set `operator`
(`AND`/`OR`/`NOT`) and combine child `operands`; leaf nodes set `criterion_predicate`
and the payload for that predicate:
- `HAS_PHENOTYPE` → `phenotype_term` + optional `min_frequency` (FrequencyEnum, "≥")
- `HAS_GENE` → `gene`
- `CONFORMS_TO_MODULE` → `module` (a `kb/modules/` stem, optionally with `#Node Name`)
- `HAS_BIOLOGICAL_PROCESS` → `biological_processes`
- `HAS_CLASSIFICATION` → `classification`; `HAS_INHERITANCE` / `HAS_MAPPING` / `OTHER`
  carry the value in `description`
- `negated: true` negates a leaf (alternative to a `NOT` operator)

**Criteria semantics (`=>` / `<=` / `<=>`):** `criteria_semantics` records the OWL-style
direction relating a criteria block to membership, which determines what tooling may infer:
- `NECESSARY` (member ⇒ criteria): every member satisfies the criteria; used to **audit**
  listed members for violations. (MPS uses this — being an MPS entails GAG storage, but
  GAG storage alone does not make a disease an MPS.)
- `SUFFICIENT` (criteria ⇒ member): any disorder satisfying the criteria is a member; used
  to **classify** non-members as candidate additions.
- `NECESSARY_AND_SUFFICIENT` (member ⇔ criteria): the criteria *define* the grouping; both.

Multiple blocks are allowed (several `NECESSARY` blocks plus an optional defining block),
mirroring OWL subclass/equivalence axioms.

**Checking/classifying (`src/dismech/groupings.py`):**
```bash
just check-groupings                                 # lint + audit all groupings
just check-groupings kb/groupings/Mucopolysaccharidoses.yaml
just check-groupings --strict                        # gate on errors/violations
```
Two tiers: a **structural linter** (`lint_criterion`) classifies every node BRANCH vs LEAF
and enforces well-formedness (gating, enforced in `tests/test_data.py`); and an **advisory
membership evaluator** (`evaluate_grouping`) that three-valuedly checks each member's disease
entry against `NECESSARY`/`N&S` criteria (`SATISFIED`/`NOT_SATISFIED`/`UNKNOWN`) and, for
`SUFFICIENT`/`N&S` criteria, flags candidate non-members. The evaluator is advisory because
criteria are often aspirational (a member may not yet declare a required `conforms_to` edge).

**Per-member differentiating mechanisms:**

Each `members[]` entry references a `Disease` by name (`member`, with `member_type`
defaulting conceptually to `DISEASE`; `MODULE` and `GROUPING` members are also allowed)
and carries `differentiating_mechanisms` — prose plus optional structured descriptors
(`gene`, `phenotype_term`, `biological_processes`, `module`, `modifier`) capturing what
distinguishes that member from its siblings.

**Foreign keys (enforced by `tests/test_data.py`):**
- `members[].member` must resolve to a real `Disease.name` (DISEASE/SUBTYPE), module
  stem (MODULE), or grouping name (GROUPING).
- Every `module` reference (in criteria leaves and differentiating mechanisms) must
  resolve to a file in `kb/modules/`.
- Grouping `name` values must be unique.

**Validation:**
```bash
just validate-grouping kb/groupings/Mucopolysaccharidoses.yaml  # single file
just validate-groupings                                         # all (also part of `just qc`)
```

**Rendering (HTML):**
```bash
just gen-grouping-pages                                  # all groupings + index
just gen-grouping-page kb/groupings/Mucopolysaccharidoses.yaml
```
Renders `pages/groupings/*.html` (derived — not committed). The detail page shows
the `grouping_basis`/MONDO mapping, the rationale, the membership-criteria boolean
tree, and per-member differentiating mechanisms with an advisory audit badge
(SATISFIED/NOT_SATISFIED/UNKNOWN from `evaluate_grouping`) plus any candidate
members from SUFFICIENT/N&S criteria.

**Worked examples:** `Mucopolysaccharidoses` (NECESSARY, aspirational members),
`Inherited_Arrhythmia_Syndromes` (NECESSARY_AND_SUFFICIENT with a NOT leaf +
candidate discovery), `Heritable_Thoracic_Aortic_Disease` (NECESSARY with a
nested AND/OR phenotype branch), and `Lysosomal_Storage_Disorders` (defining
module criterion + a nested GROUPING member).

### Evidence Items
All evidence must have PMID references and support classification:
```yaml
evidence:
  - reference: PMID:12345678
    supports: SUPPORT  # or REFUTE, PARTIAL, NO_EVIDENCE, WRONG_STATEMENT
    evidence_source: HUMAN_CLINICAL  # or MODEL_ORGANISM, IN_VITRO, COMPUTATIONAL
    snippet: "Quoted text from the paper"
    explanation: "Why this evidence supports/refutes the claim"
```

**IMPORTANT**: The `evidence_source` field classifies **the type of evidence presented in the cited publication**, NOT how the curation was performed. Even if an AI agent is curating the entry, `evidence_source` describes what kind of study the paper reports (human clinical trial, animal model, cell culture, computational simulation, etc.).

Set `evidence_source` to clarify the publication's evidence type:
- HUMAN_CLINICAL for direct human observations (default when not specified)
- MODEL_ORGANISM when citing animal model recapitulation
- IN_VITRO for cell-based experiments
- COMPUTATIONAL for in silico predictions/simulations reported in the paper
- OTHER for evidence types that do not fit the above categories
Model organism evidence should not be the only support for human phenotypes; keep it distinct via `evidence_source`.

### Entry Metadata Dates

Each `Disease` entry should include a creation timestamp:

```yaml
creation_date: "2025-06-12T20:16:27Z"
```

Rules:
- Use ISO 8601 / RFC 3339 datetime strings.
- Keep `creation_date` stable after first creation.
- Prefer UTC (`Z` suffix) for consistency.
- **Do not add `updated_date` to new entries.** The field is deprecated — git history is the authoritative change log. Existing entries that still carry `updated_date` may retain it until a future bulk cleanup.

Quick classification rules (use these before tagging):
- HUMAN_CLINICAL: human patients, cohorts, case reports, clinical trials (NCT), epidemiology.
- MODEL_ORGANISM: any in vivo animal data (mouse, zebrafish, dog/cat/horse veterinary case series, primate, or other non-human animals), even if observational and not interventional.
- IN_VITRO: cultured cells or tissue explants (human or animal), organoids, ex vivo slices, biochemical assays outside an organism.
- COMPUTATIONAL: in silico modeling, docking, simulations, ML predictions, network/pathway inference without wet-lab confirmation.
- OTHER: anything that does not cleanly fit above (e.g., expert consensus without data, pathology image atlases without linked cohort context).

Edge cases:
- Veterinary observations are MODEL_ORGANISM (non-human mammals are still animal models for this purpose).
- In silico “modeling studies” belong to COMPUTATIONAL, even if they use clinical datasets as input.
- If a paper mixes sources, split evidence items so each item gets a single `evidence_source`.

### Ontology Term Mappings
When adding enum values with `meaning` fields, the description MUST exactly match the ontology term's canonical label. Use OAK to verify:
```bash
uv run runoak -i sqlite:obo:hp info HP:0040282 -O obo
```

This prevents AI hallucination of fake or mismatched ontology terms.

### Descriptor Qualifier Slots

Common clinical qualifiers on ontology-bound descriptors should use explicit slots on
the descriptor object rather than the deprecated generic `qualifiers` list:

- `temporality`: `ACUTE`, `TRANSIENT`, `SUBACUTE`, `CHRONIC`, `RECURRENT`,
  `DIURNAL`, `NOCTURNAL`, `PROLONGED`
- `clinical_course`: `PROGRESSIVE`, `STABLE`
- `severity`: prefer enum-backed values (`MILD`, `MODERATE`, `SEVERE`) when the qualifier
  is part of the ontology post-composition; free text is still tolerated for legacy
  phenotype/context summaries
- `onset`: structured `OnsetDescriptor` with `onset_category` and optional age fields

Pattern:
```yaml
phenotype_term:
  preferred_term: Diarrhea
  term:
    id: HP:0002014
    label: Diarrhea
  temporality: CHRONIC

phenotype_term:
  preferred_term: Muscle weakness
  term:
    id: HP:0001324
    label: Muscle weakness
  clinical_course: PROGRESSIVE
```

Use these first-class slots for common post-composition. Reserve `qualifiers` for
more complex predicate-value patterns that are not covered by dedicated slots.

### `preferred_term` vs Ontology Term Labels

Each descriptor (phenotype, cell type, treatment, etc.) has two distinct label fields with different rules:

- **`term.label`**: MUST exactly match the canonical ontology term label. Verified with OAK. Never deviate from the official label.
- **`preferred_term`**: The human-readable name used in display. **This CAN be more specific or nuanced than the ontology term** when the ontology does not fully capture the desired clinical or biological granularity.

When the ontology provides only a broad parent term but you want to convey greater specificity, use a more descriptive `preferred_term` while still linking to the best-fit ontology term:

```yaml
# Example: cell type with preferred clinical name
cell_types:
- preferred_term: CD4+ regulatory T cell
  term:
    id: CL:0000815
    label: regulatory T cell

# Example: treatment more specific than generic pharmacotherapy term
treatments:
- name: Anti-TNF Biologic Therapy
  description: Treatment with TNF inhibitors such as adalimumab or infliximab.
  treatment_term:
    preferred_term: anti-TNF biologic therapy
    term:
      id: NCIT:C15986
      label: Pharmacotherapy
```

**Guidelines:**
- Always link to the most specific available ontology term, even if `preferred_term` is more granular.
- If the ontology has a term that closely matches, prefer using its label as `preferred_term` for clarity.
- Use a more nuanced `preferred_term` only when the ontology term is genuinely too broad to convey the intended meaning.
- A `modifier` may be used to capture the semantics of some preferred terms.

### Treatment Terms (MAXO or NCIT)
Treatments can be annotated with Medical Action Ontology (MAXO) terms or NCI Thesaurus (NCIT)
clinical intervention terms. NCIT often provides more specific procedure and therapy terms
than MAXO. Use whichever ontology has the most specific and accurate term for the treatment.

```yaml
# MAXO example
treatments:
- name: Physical Therapy
  description: Rehabilitation exercises to improve mobility.
  treatment_term:
    preferred_term: physical therapy
    term:
      id: MAXO:0000011
      label: physical therapy

# NCIT example
treatments:
- name: Orthopedic Surgery
  description: Corrective surgery for skeletal deformities.
  treatment_term:
    preferred_term: orthopedic surgical procedure
    term:
      id: NCIT:C16186
      label: Orthopedic Surgical Procedure
```

Common MAXO terms:
- `MAXO:0000004` - surgical procedure
- `MAXO:0000011` - physical therapy
- `MAXO:0000079` - genetic counseling
- `MAXO:0000088` - dietary intervention
- `MAXO:0000647` - chemotherapy
- `MAXO:0000014` - radiation therapy
- `MAXO:0001017` - vaccination
- `MAXO:0010039` - organ transplantation
- `MAXO:0000950` - supportive care

Common NCIT clinical intervention terms:
- `NCIT:C15986` - Pharmacotherapy (drug treatments)
- `NCIT:C49236` - Therapeutic Procedure
- `NCIT:C15329` - Surgical Procedure
- `NCIT:C16186` - Orthopedic Surgical Procedure
- `NCIT:C15302` - Physical Therapy
- `NCIT:C15315` - Rehabilitation
- `NCIT:C15747` - Supportive Care

Use OAK to search for terms:
```bash
uv run runoak -i sqlite:obo:maxo search "physical therapy"
uv run runoak -i sqlite:obo:ncit info "l^Physical Therap"
```

#### Therapeutic Agent Pattern (drug + drug class on pharmacotherapy)

Treatment terms describe the **medical action** (e.g., Pharmacotherapy, chemotherapy,
vaccination) but not the specific agent involved. When the action is generic but a
specific drug or drug class is involved, combine the generic treatment term with the
`therapeutic_agent` slot, which is multivalued and bindable to CHEBI (for specific drugs)
or NCIT (for drug classes).

**When to use `therapeutic_agent`:**
- `treatment_term` is a generic action like `NCIT:C15986` (Pharmacotherapy),
  `MAXO:0000647` (chemotherapy), `MAXO:0001017` (vaccination), or `MAXO:0000014` (radiation therapy)
- A specific drug, chemical, or drug class is referenced in the `name` / `description`
- You want the treatment to be machine-queryable by drug identity

**Ontology selection:**
- **CHEBI**: preferred for specific small-molecule drugs (`CHEBI:36796` duloxetine, `CHEBI:46345` 5-fluorouracil)
- **NCIT**: use for drug classes, or for biologics/newer drugs that lack a CHEBI term
  (`NCIT:C20401` Monoclonal Antibody, `NCIT:C2322` Corticosteroid, `NCIT:C65216` Adalimumab)
- Leave `therapeutic_agent` absent when the treatment is non-pharmacological
  (surgery, physical therapy, counseling, dietary intervention — use `dietary_modifications` for the latter)

**Example — single specific drug (CHEBI):**
```yaml
treatments:
- name: Duloxetine
  description: SNRI, FDA-approved for fibromyalgia chronic pain management.
  treatment_term:
    preferred_term: Pharmacotherapy
    term:
      id: NCIT:C15986
      label: Pharmacotherapy
    therapeutic_agent:
    - preferred_term: duloxetine
      term:
        id: CHEBI:36796
        label: duloxetine
```

**Example — drug class (NCIT) when CHEBI is too specific:**
```yaml
treatments:
- name: Anti-TNF Biologic Therapy
  description: TNF inhibitors such as adalimumab or infliximab.
  treatment_term:
    preferred_term: anti-TNF biologic therapy
    term:
      id: NCIT:C15986
      label: Pharmacotherapy
    therapeutic_agent:
    - preferred_term: monoclonal antibody
      term:
        id: NCIT:C20401
        label: Monoclonal Antibody
```

**Example — combination therapy (multivalued):**
```yaml
treatments:
- name: FOLFIRINOX
  description: Combination chemotherapy regimen for pancreatic adenocarcinoma.
  treatment_term:
    preferred_term: chemotherapy
    term:
      id: MAXO:0000647
      label: chemotherapy
    therapeutic_agent:
    - preferred_term: fluorouracil
      term:
        id: CHEBI:46345
        label: 5-fluorouracil
    - preferred_term: irinotecan
      term:
        id: CHEBI:80630
        label: irinotecan
    - preferred_term: oxaliplatin
      term:
        id: CHEBI:31941
        label: oxaliplatin
```

**Guidelines:**
- `therapeutic_agent` is optional at the schema level but **recommended whenever `treatment_term` is NCIT:C15986** or another generic action term where a specific drug is involved.
- Use OAK to verify CHEBI terms: `uv run runoak -i sqlite:obo:chebi search "duloxetine"`
- For NCIT drug-class terms, the local `ncit` adapter is configured in `conf/oak_config.yaml`.
- A dedicated `treatment.name` (e.g., "Duloxetine") should still match common clinical usage; `therapeutic_agent` carries the machine-readable identifier.
- Do NOT put the drug name in `preferred_term` on `treatment_term` — `preferred_term` describes the action (Pharmacotherapy), `therapeutic_agent.preferred_term` describes the agent.

### Therapeutic Modality and Antisense Oligonucleotide (ASO) Detail

A treatment's **modality** (the kind of therapeutic platform) is captured by the
enum-backed `therapeutic_modality` slot — **not** the free-text `role` slot, which
is overloaded across host roles, pathophysiology-node roles, and treatment roles.
Prefer `therapeutic_modality` for platform classification so treatments are
queryable by modality across diseases.

`therapeutic_modality` values: `SMALL_MOLECULE`, `MONOCLONAL_ANTIBODY`,
`ANTISENSE_OLIGONUCLEOTIDE`, `SIRNA`, `MRNA_THERAPY`, `GENE_THERAPY`,
`GENE_EDITING`, `CELL_THERAPY`, `PROTEIN_REPLACEMENT`, `PEPTIDE`, `VACCINE`,
`RADIOTHERAPY`, `SURGERY`, `DEVICE`, `BEHAVIORAL`, `OTHER`.

`therapeutic_modality` complements (does not replace) `treatment_term` (the treatment
action) and `therapeutic_agent` (the specific drug). A pharmacotherapy ASO still
uses `NCIT:C15986` for `treatment_term` and an NCIT/CHEBI `therapeutic_agent`.

When `therapeutic_modality: ANTISENSE_OLIGONUCLEOTIDE`, add a structured
`aso_details` block (`AntisenseOligonucleotideDetail`) capturing the molecular
mechanism, RNA target, splice exon, chemistry, and conjugation:

- `aso_mechanism`: `RNASE_H_KNOCKDOWN`, `SPLICE_MODULATION_EXON_SKIPPING`,
  `SPLICE_MODULATION_EXON_INCLUSION`, `STERIC_BLOCKADE`, `MIRNA_MODULATION`
- `target_gene`: `GeneDescriptor` bound to HGNC (lowercase `hgnc:` prefix)
- `target_transcript`: free text for the RNA target / element (e.g., `APOB mRNA`,
  `SMN2 ISS-N1`)
- `target_exon`: free text for splice-switching ASOs (e.g., `exon 51`)
- `aso_chemistry`: `PHOSPHOROTHIOATE`, `PHOSPHORODIAMIDATE_MORPHOLINO`,
  `TWO_PRIME_O_METHYL`, `TWO_PRIME_O_METHOXYETHYL`, `LOCKED_NUCLEIC_ACID`,
  `CONSTRAINED_ETHYL`, `OTHER`
- `conjugation`: `UNCONJUGATED`, `GALNAC`, `LIPID`, `PEPTIDE`, `ANTIBODY`, `OTHER`

**Example — RNase H knockdown ASO (mipomersen, APOB):**
```yaml
treatments:
- name: Mipomersen
  therapeutic_modality: ANTISENSE_OLIGONUCLEOTIDE
  aso_details:
    aso_mechanism: RNASE_H_KNOCKDOWN
    target_gene:
      preferred_term: APOB
      term:
        id: hgnc:603
        label: APOB
    target_transcript: APOB mRNA
    aso_chemistry: TWO_PRIME_O_METHOXYETHYL
    conjugation: UNCONJUGATED
  treatment_term:
    preferred_term: Pharmacotherapy
    term:
      id: NCIT:C15986
      label: Pharmacotherapy
    therapeutic_agent:
    - preferred_term: mipomersen
      term:
        id: NCIT:C174575
        label: Mipomersen
```

**Example — splice-switching exon-skipping ASO (eteplirsen, DMD exon 51):**
```yaml
  therapeutic_modality: ANTISENSE_OLIGONUCLEOTIDE
  aso_details:
    aso_mechanism: SPLICE_MODULATION_EXON_SKIPPING
    target_gene:
      preferred_term: DMD
      term:
        id: hgnc:2928
        label: DMD
    target_exon: exon 51
    aso_chemistry: PHOSPHORODIAMIDATE_MORPHOLINO
    conjugation: UNCONJUGATED
```

**Example — GalNAc-conjugated ASO (eplontersen, TTR):** same as the RNase H
example but with `conjugation: GALNAC` and the TTR `target_gene`.

Leave `aso_details` absent for non-ASO treatments. The structured fields are
optional — populate what is documented and omit fields you cannot source.

### Subtype Naming Conventions

The `name` field on `Subtype` (in `has_subtypes`) serves as the **foreign key target** — other sections
(phenotypes, biochemical, genetic, prevalence, progression, histopathology) reference it via their
`subtype` field. A validation test (`test_subtype_foreign_keys`) enforces that all `subtype` values
match a defined `has_subtypes[].name`.

**Naming rules for `name`:**
- Keep names short and slug-friendly: `Type 1`, `MEN2A`, `Vascular EDS`, `FA-A`
- Avoid parenthetical qualifiers, long descriptions, or special characters
- Use `display_name` (optional) for verbose/human-readable labels when the `name` is too terse

**Example:**
```yaml
has_subtypes:
- name: Type 1
  display_name: Type 1 (Non-neuronopathic)
  description: Most common form, no CNS involvement...

phenotypes:
- name: Seizures
  subtype: Type 1    # references the short name
```

**When `display_name` is set**, renderers show it instead of `name`. When absent, `name` is displayed directly.

### Reference Ranges and Interpretation Bands

A `Biochemical` marker can carry clinical laboratory `reference_ranges`
(`ReferenceRange` class): a LOINC-coded normal interval (`lower_bound` /
`upper_bound` / `unit`) and a `population` stratifier. Omit a bound for
one-sided intervals. Attribute the interval with structured `evidence`
(the same `EvidenceItem` model used everywhere else — a citable PMID/DOI
with a verified snippet), **not** a free-text source string. When the
provenance is a lab manual that has no citable article (e.g., the Tietz
guide), put that attribution in `notes` rather than inventing a citation.

When a result is interpreted in graded categories rather than a single
normal interval (e.g., above one value is mild, above a higher value is
moderate, then severe), add `interpretation_bands` (`ReferenceRangeBand`).
Each band maps a value interval to a category and is rendered as a colored
pill on the disorder page:

- `name` (required): category label (e.g., "Normal", "Mild hypercalcemia").
- `lower_bound` / `upper_bound`: the band's half-open interval
  `[lower_bound, upper_bound)` — `lower_bound` inclusive, `upper_bound`
  exclusive — so adjacent bands sharing a boundary value partition cleanly
  (a result at the boundary falls in the upper band). Omit `lower_bound` for
  the open-below tier and `upper_bound` for the open-above tier.
- `abnormal_flag`: `NORMAL`, `LOW`, `HIGH`, `CRITICAL_LOW`, `CRITICAL_HIGH`
  (HL7 v2 / LOINC convention).
- `severity`: ordinal `MILD` / `MODERATE` / `SEVERE` when the category aligns
  with severity grading. Renderer colors bands by `severity` first, then
  `abnormal_flag`.
- `phenotype_term`: optional HP term an abnormal band maps to (LOINC2HPO style).
- `interpretation`: free-text clinical interpretation of results in the band.

```yaml
reference_ranges:
- loinc_term:
    id: LOINC:17861-6
    label: Calcium [Mass/volume] in Serum or Plasma
  lower_bound: 8.5
  upper_bound: 10.5
  unit: mg/dL
  population: adults
  evidence:
  - reference: PMID:26303319
    supports: SUPPORT
    snippet: "exact quote stating the interval"
    explanation: Source for the calcium reference interval.
  notes: "Or, for a non-citable lab-manual interval, record provenance here."
  interpretation_bands:
  - name: Normal
    lower_bound: 8.5
    upper_bound: 10.5
    unit: mg/dL
    abnormal_flag: NORMAL
  - name: Mild hypercalcemia
    lower_bound: 10.5
    upper_bound: 12.0
    unit: mg/dL
    abnormal_flag: HIGH
    severity: MILD
  - name: Severe hypercalcemia
    lower_bound: 14.0
    unit: mg/dL
    abnormal_flag: CRITICAL_HIGH
    severity: SEVERE
```

`reference_ranges` (empirical clinical intervals) are distinct from
`ModelVariableDescriptor` thresholds / `severity_scale` (computational-model
phenotype-activation points); use reference ranges for measured lab analytes.

The CKD-Mineral Bone Disorder entry is the worked example.

### Clinical Trials

Clinical trials can be added to disease entries with evidence validated against ClinicalTrials.gov:

```yaml
clinical_trials:
- name: NCT05813288
  phase: Phase III
  status: Completed
  description: Brief description of the trial's objective and approach
  target_phenotypes:
    - preferred_term: Wheezing
      term:
        id: HP:0030828
        label: Wheezing
    - preferred_term: Breathlessness
      term:
        id: HP:0002094
        label: Dyspnea
  evidence:
    - reference: clinicaltrials:NCT05813288
      supports: SUPPORT
      snippet: "Exact quote from the trial summary"
      explanation: "Why this trial is relevant to the disease"
```

**Fetching trial data:**
```bash
just fetch-reference NCT05813288  # Caches trial data from ClinicalTrials.gov API
```

**Key fields:**
- `name`: NCT identifier (e.g., NCT05813288)
- `phase`: Trial phase (Phase I, II, III, IV)
- `status`: Recruitment status (Recruiting, Completed, Terminated, Active not recruiting)
- `target_phenotypes`: Phenotypes addressed by the trial (with HP ontology terms)
- `evidence`: Evidence items validated against ClinicalTrials.gov

### MorPhiC Cellular Phenotypes

The MorPhiC Consortium (Molecular Phenotypes of Null Alleles in Cells) creates null alleles of human genes in iPSC-derived multicellular systems and measures their molecular and cellular phenotypes. MorPhiC data can enrich dismech entries with `category: Cellular` phenotypes.

**When to add MorPhiC-derived phenotypes:**
- The disorder involves a gene targeted by MorPhiC (check morphic.bio for gene lists)
- iPSC-derived cellular models recapitulate disease-relevant phenotypes
- Evidence source should be `IN_VITRO` for all MorPhiC-derived evidence

**Pattern for cellular phenotypes:**
```yaml
phenotypes:
- category: Cellular
  name: Impaired Cardiomyocyte Differentiation
  description: >
    Gene-null iPSC-derived cardiomyocytes show impaired differentiation...
  phenotype_term:
    preferred_term: Impaired cardiomyocyte differentiation
    term:
      id: HP:0001637
      label: Abnormal myocardium morphology
  evidence:
  - reference: PMID:39939790
    supports: SUPPORT
    evidence_source: IN_VITRO
    snippet: "exact quote from paper"
    explanation: "How MorPhiC data supports this phenotype"
```

**MorPhiC dataset references:**
```yaml
datasets:
- accession: morphic:GENE_SYMBOL
  title: MorPhiC null allele phenotyping of GENE in iPSC-derived cells
  data_type: MULTI_OMICS_PERTURBATION
  organism:
    preferred_term: human
    term:
      id: NCBITaxon:9606
      label: Homo sapiens
  publication: PMID:39939790
```

Key MorPhiC anchor genes: ISL1, EOMES, GCM1, NKX2-1. Data available under CC BY 4.0.

## Testing

Tests are in `tests/test_data.py`:
- Schema validation for all 56 disorder files
- Required field checks
- Evidence reference validation
- Unique name verification

## Standard Operating Procedure: Adding/Editing Evidence

When adding or editing evidence items in disorder files, follow this SOP to prevent hallucinations:

### 1. Never Fabricate Snippets

Evidence snippets MUST be exact quotes from the cited paper's abstract. Do not paraphrase.

**Wrong:**
```yaml
evidence:
  - reference: PMID:12345678
    snippet: The study showed that X causes Y through Z mechanism.  # Paraphrase - will fail validation
```

**Correct:**
```yaml
evidence:
  - reference: PMID:12345678
    snippet: "X causes Y through the Z mechanism, as demonstrated by..."  # Exact quote from abstract
```

### 2. Verify PMIDs Before Use

Always check that a PMID actually corresponds to the paper you think it does:

```bash
# Check cached abstract (if previously fetched)
cat references_cache/pmid_12345678.md

# Or fetch fresh and validate
just validate-references kb/disorders/MyDisease.yaml
```

### 2a. Deep-Research (Falcon/DR) Tool Outputs — Extra Verification Needed

Deep-research tools (Falcon, DGO, etc.) synthesize information across many sources but are **known to fabricate or misattribute citations, misquote snippets, and invent ontology identifiers**. When using DR outputs for curation:

**Treat DR outputs as *leads*, not ground truth.** Every PMID, snippet, and ontology term from a DR summary must be independently verified before committing.

**Three categories of hallucination risk:**
1. **Fabricated PMIDs** — The cited paper does not exist, or the PMID belongs to an unrelated paper
2. **Misquoted snippets** — The snippet is paraphrased or invented rather than an exact quote from the real abstract
3. **Invented ontology terms** — HP, GO, CL, MAXO, CHEBI, or NCIT identifiers that don't exist or whose canonical label doesn't match `term.label`

**Mandatory verification workflow for any curation step sourced from DR:**
1. For **each new PMID** cited: run `just fetch-reference PMID:XXXX` to fetch the real abstract
2. For **each snippet**: manually verify it is an exact substring of the abstract by comparing against the cached file in `references_cache/PMID_XXXX.md`
3. For **each ontology term** (HP, GO, CL, MAXO, CHEBI, NCIT): verify the term exists and its canonical label matches `term.label` by running `just validate-terms-file kb/disorders/YourDisease.yaml`
4. Run the full validation suite before committing (see Validation Workflow below)

If a DR-suggested citation cannot be verified against the real abstract, do not use it. Find an alternative source or remove the claim entirely.

**Historical note:** Issue #1737 audited DR-sourced entries and found ~1% hallucination rate in the cache layer — the dismech validation stack catches these errors, but only *after* the curator runs the checks. Treating DR outputs as leads rather than ground truth is the most reliable protection.

### 3. Validation Workflow

Before committing changes to any disorder file:

```bash
# 1. Schema validation (structure correct)
just validate kb/disorders/MyDisease.yaml

# 2. Reference validation (snippets match abstracts)
just validate-references kb/disorders/MyDisease.yaml

# 3. Term validation (ontology IDs/labels correct)
just validate-terms-file kb/disorders/MyDisease.yaml
```

### 4. When Evidence Cannot Be Verified

If a claim is well-established but you cannot find a quotable snippet:

- **Option A**: Move the claim to the `notes` field (no evidence required)
- **Option B**: Find a different paper with a quotable abstract
- **Option C**: Remove the evidence block entirely, keep the description

**Do NOT** fabricate quotes or use incorrect PMIDs.

### 5. Common Validation Errors

| Error | Cause | Fix |
|-------|-------|-----|
| "Text part not found as substring" | Snippet is paraphrased | Use exact quote from abstract |
| "Reference not found" | PMID doesn't exist | Verify PMID on PubMed |
| Low similarity score | Wrong PMID for the paper | Check abstract matches topic |

### 6. Frequency Qualifiers Need Their Own Evidence

Phenotype `frequency:` values (FREQUENT, OCCASIONAL, etc.) make a *separate*
quantitative claim from the disease–phenotype association itself. Most snippets
support only the association, not the band. See
[`docs/frequency-evidence-guidelines.md`](docs/frequency-evidence-guidelines.md)
for the curator SOP: acceptable evidence patterns (direct quantitative,
derived counts, qualitative-term mapping, clinical estimate), the literature-term
→ enum mapping table, and worked examples. **When in doubt, omit `frequency:`
rather than fabricate justification.**

### 7. Running Full QC

```bash
# All validation checks
just qc

# Compliance analysis (recommended field coverage)
just compliance-all

# With weighted scoring and threshold checks
just compliance-weighted

# Generate visual dashboard (dashboard/index.html)
just gen-dashboard
```

The dashboard shows priority curation targets - the 10 files with lowest compliance scores.



## CRITICAL: Reference Cache Files — NEVER Create Manually

Reference cache files in `references_cache/` are created EXCLUSIVELY by `linkml-reference-validator`.
**NEVER write these files by hand.** This is the #1 source of agent errors in dismech.

**Correct workflow:**
```bash
# 1. Fetch and cache the reference (creates references_cache/PMID_12345678.md)
just fetch-reference PMID:12345678

# 2. Validate that your snippet matches the cached abstract
just validate-references kb/disorders/MyDisease.yaml

# 3. If validation fails, fix the snippet or find a different PMID
just validate kb/disorders/MyDisease.yaml
```

**Why this matters:**
- `just fetch-reference` fetches the REAL abstract from PubMed and creates the cache file with the correct filename format (`PMID_` uppercase prefix), correct YAML frontmatter, and correct content
- Hand-created cache files have wrong filenames (lowercase `pmid_`), fabricated content, and wrong format
- CI validates snippets against these cached files — if the cache is fabricated, validation is meaningless

**What agents MUST do:**
1. Add YAML with `reference: PMID:XXXX` and a snippet
2. Run `just fetch-reference PMID:XXXX` for each new PMID cited
3. Run `just validate-references kb/disorders/YourFile.yaml`
4. If snippet doesn't match, fix it to be an exact quote or find a different PMID

**Deterministic cache contract check (dismech#871):**
`just check-reference-cache-frontmatter` validates that every
`references_cache/*.md` file has parseable YAML frontmatter matching the local
`linkml-reference-validator` cache contract and filename/reference_id mapping.
It runs as part of `just qc` before the heavier validators. This is still only
a structural check — `validate-references` remains the last defence against a
snippet matching the wrong cached paper.

**Agent guardrail:** Claude Code and Codex must never create or hand-edit
`references_cache/*.md`. If a cache file is wrong or malformed, regenerate it
with `just fetch-reference <ID>` instead of patching the frontmatter manually.

## Structured-Database Reference Sources

In addition to fetched literature references (PMID, DOI, NCT), dismech ingests
structured knowledge bases — currently **Orphanet** and **ClinGen** — into
`references_cache/` as deterministic line-oriented markdown files. Each file
holds one entity (one ORPHA disorder) and curators can quote individual rows
as evidence `snippet:` values.

**Available structured prefixes:**

| Prefix | Source | Coverage | License |
|--------|--------|----------|---------|
| `ORPHA:` | Orphadata bulk XML | 8,823 leaf disorders + subtypes | CC-BY 4.0 |
| `CGGV:` | ClinGen Gene-Disease Validity CSV | One record per gene-disease validity assertion | ClinGen terms |
| `CGDS:` | ClinGen Dosage Sensitivity downloads | One record per dosage-sensitive gene | ClinGen terms |
| `CIVIC_ASSERTION:`, `CIVIC_EID:` | CIViC accepted assertion and clinical evidence TSVs | One record per accepted CIViC assertion or evidence item | CIViC |

**Citing an Orphanet entry:**

```yaml
evidence:
  - reference: ORPHA:558
    supports: SUPPORT
    snippet: "Marfan syndrome is a systemic disease of connective tissue"
    explanation: Orphadata definition supports this characterization.
```

Snippets must be exact substrings of the cache file's body. The body uses
markdown section headings (`## Definition`, `## Inheritance`, `## Phenotypes`,
`## Genes`, `## Epidemiology`, `## Cross-references`, `## Source`) with
markdown tables for tabular data. Each table row is a stable quotable
substring across refreshes:

```
| HP:0002616 | Aortic root aneurysm | Very frequent (99-80%) |
| FBN1 | fibrillin-1 | hgnc:3603 | Disease-causing germline mutation(s) in |
| MONDO:0007947 | Exact |
```

A curator-quoted snippet may include or omit the leading and trailing
pipes — both substring-match against the cached body. Prefer the
unbracketed form for cleaner YAML:

```yaml
snippet: "HP:0002616 | Aortic root aneurysm | Very frequent (99-80%)"
```

**Citing a ClinGen gene-disease validity assertion:**

```yaml
evidence:
  - reference: CGGV:assertion_7f53d03d-f936-4628-ab75-351ae4da012a-2022-09-15T160000.000Z
    supports: SUPPORT
    snippet: "HEXB | HGNC:4879 | Sandhoff disease | MONDO:0010006 | AR | Definitive"
    explanation: ClinGen classifies the HEXB-Sandhoff disease relationship as definitive.
```

ClinGen cache bodies contain a `## Evidence summary` section when the
assertion report page has ClinGen narrative text, plus a `## Gene-disease
validity` markdown table:

```
## Evidence summary

In summary, HEXB is definitively associated with Sandhoff disease.

## Gene-disease validity

| Gene | HGNC | Disease | MONDO | MOI | Classification | SOP | GCEP | Classification date |
| HEXB | HGNC:4879 | Sandhoff disease | MONDO:0010006 | AR | Definitive | SOP9 | Lysosomal Diseases Gene Curation Expert Panel | 2022-09-15T16:00:00.000Z |
```

**Citing a ClinGen dosage sensitivity assertion:**

```yaml
evidence:
  - reference: CGDS:HGNC_9585
    supports: SUPPORT
    snippet: "PTCH1 | HGNC:9585 | 5727 | 9q22.32 | chr9:95442980-95516971 | 3 - Sufficient Evidence for Haploinsufficiency | 0 - No Evidence for Triplosensitivity | 2020-07-01"
    explanation: ClinGen dosage sensitivity supports PTCH1 haploinsufficiency as a disease mechanism.
```

ClinGen dosage cache bodies contain a `## Gene dosage sensitivity` table and,
when available, report-page narrative for haploinsufficiency and
triplosensitivity evidence.

**How the cache is built:**

```bash
# 1. Refresh the bulk XML pinned in data/orphadata/MANIFEST.yaml
just refresh-orphadata

# 2. Rebuild every references_cache/ORPHA_*.md
just structured-rebuild-orphanet

# Or rebuild a single ID
just structured-rebuild-orphanet --id 558

# ClinGen Gene-Disease Validity CSV
just clingen-refresh
just clingen-list
just clingen-rebuild
just clingen-rebuild --id CGGV:assertion_7f53d03d-f936-4628-ab75-351ae4da012a-2022-09-15T160000.000Z

# Use --csv-only to skip fetching report-page narrative during a fast rebuild
just clingen-rebuild --csv-only --id CGGV:assertion_7f53d03d-f936-4628-ab75-351ae4da012a-2022-09-15T160000.000Z

# ClinGen Dosage Sensitivity CSV/TSV
just clingen-dosage-refresh
just clingen-dosage-list
just clingen-dosage-rebuild
just clingen-dosage-rebuild --id CGDS:HGNC_9585
```

`data/orphadata/*.xml` is gitignored; `data/orphadata/MANIFEST.yaml` is
committed and pins the snapshot date + sha256 of each bulk file. To verify
no drift has occurred, run `just structured-rebuild-orphanet` locally and
check `git diff references_cache/ORPHA_*.md`. (A CI workflow that does this
automatically is a worthwhile follow-up but does not yet exist.)

**Adding a new structured source:**

The framework is in `src/dismech/structured_sources/`. To add a new source
(OMIM, MONDO, HGNC, …):

1. Subclass `StructuredSource` (`base.py`) and implement `build_index`,
   `identifiers`, `serialize`.
2. Pin bulk-data files in `data/<source>/MANIFEST.yaml`.
3. Register a CLI entry in `src/dismech/structured_sources/cli.py`.
4. Use the same UniProt-flat-file-style line layout — fixed column widths,
   sorted within each tag block — so curator-quoted snippets remain valid
   across refreshes.

**Agent guardrail:** Like literature cache files, `references_cache/ORPHA_*.md`
must NEVER be hand-edited. Regenerate via `just structured-rebuild-orphanet`.

## Git/GitHub Best Practices

### Open PRs from origin, not forks

Do not open PRs from forks. GitHub does not expose repository secrets to
fork-triggered workflows, so fork PRs will not receive automated AI review. Push
branches directly to `origin`; new contributors should first open an issue
requesting repository access.

### Use worktrees

Use worktrees for parallel feature work. The **primary checkout** (wherever you cloned the repo) must always stay on `main`. Feature branches go in worktrees only.

- Never check out `main` in a worktree — `main` belongs to the primary checkout.
- Never leave the primary checkout on a feature branch.
- If `git checkout main` fails with "already checked out at …", find which worktree holds `main` (`git worktree list | grep '\[main\]'`), switch that worktree to a feature branch, then retry.

### What to commit

| Path | Commit? | Reason |
|------|---------|--------|
| `kb/disorders/*.yaml`, `kb/modules/*.yaml` | YES | Core content |
| `references_cache/*.md` | YES | Required for deterministic `validate-references` CI |
| `cache/**/*.csv` | YES | Required for deterministic term validation CI |
| `research/*.md` | YES | Useful provenance |
| `src/`, `scripts/`, `tests/`, `conf/` | YES | Source code |

### What NOT to commit

| Path | Commit? | Reason |
|------|---------|--------|
| `pages/disorders/*.html` | NO | Derived — regenerated by downstream CI after merge |
| `dashboard/*.html` | NO | Derived — generated by `just gen-dashboard` |
| `docs/` HTML output | NO | Derived — regenerated by CI |

### Never force-push someone else's branch
If a PR was authored by another contributor, **do not** force-push, rebase, or reset their branch. Instead:
1. Ask the original author to rebase/fix conflicts themselves
2. Or create a separate fix commit on top of their work (no force-push)
3. Only force-push branches that you (or your orchestrator) created

### Refresh your own branch safely
Refreshing a PR branch with `main` is a content-changing operation, not bookkeeping.
For branches you own:
1. Prefer `git fetch origin && git rebase origin/main`
2. If the branch is stale or conflict-heavy, create a fresh branch from `origin/main` and cherry-pick only the intended commits
3. Avoid routine `git merge origin/main` into PR branches
4. After any refresh, review:
```bash
git diff --name-status origin/main...HEAD
git diff --stat origin/main...HEAD
```
5. If you see unrelated deletions, stale reversions, or protected-path churn, stop and fix that before commit/push
6. If merge/rebase/cherry-pick reports conflicts or index errors, do not commit or push until the operation is clean and the post-refresh diff has been reviewed

### Always use targeted git add
Never use `git add -A` or `git add .` in worktrees. Only stage files relevant to the task:
```bash
git add kb/disorders/ references_cache/ research/
```
This prevents committing generated files (HTML, schema docs, cache CSVs) that cause merge conflicts.

### Commit and push as final step
Every task should end with: validate → targeted git add → commit → push. Don't leave uncommitted work for someone else to discover.

### Post PR comments explaining your changes
After pushing fixes, comment on the PR summarizing:
- What you changed and why
- What you intentionally did NOT change, with reasoning
- Validation results

### Reviews

Your PR will always be removed by an automated Claude reviewer. This usually happens within a few minutes.
The reviewer will mark your PR as being ready to merge or requiring changes. Be sure to address all changes.
Try and address even "optional" changes if they improve overall quality and completion.

If you disagree you can say so, but provide clearly articulated arguments in the PR comments. Never get
into back and forth. If something cannot be resolved, stop, and assign a human like @cmungall to the PR, and ask
them to facilitate.

Note that sometimes it will appear that a review has stalled, but in fact this is usually because
the PR is in conflict. Actively try and manage this, resolve conflicts carefully.
