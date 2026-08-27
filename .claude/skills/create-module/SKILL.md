---
name: create-module
description: >
  Skill for creating a new mechanism module in kb/modules/ (a conserved
  pathological process that recurs across disorders). Use when the user asks to
  create/curate a module, add an Xogenesis (pathological-structure-formation)
  module, or factor a recurrent mechanism out of several disorders. Covers the
  module schema shape, the trigger→consequence node chain, the treatment
  target_mechanisms drug pattern, the Xogenesis open-ontology anchor convention,
  evidence discipline, validation, and registration.
---

# Create a Mechanism Module

## When to use

- The user asks to create a new `kb/modules/*.yaml` module.
- A conserved mechanism (a final-common pathway, a recurrent downstream
  convergence point, a shared drug-target pattern) recurs across ≥2 disorders and
  is worth checking for consistency via `conforms_to`.
- The user asks for an **Xogenesis** module — the formation of a pathological
  material anatomical entity (cyst, calculus, granuloma, thrombus, amyloid
  deposit, atheroma, neoplasm, fibrous scar).

Read `docs/primers/modules-and-conformance.md` first for the conformance mental
model (conformance is a **consistency check, not DRY inheritance**).

## Does it clear the module bar?

Only create a module when there is **one conserved mechanism** reducible to a
short linear causal chain with **one rate-limiting "key conformance target"
node** that every conformer funnels through. If the candidate is mechanistically
heterogeneous (many unrelated pathways to the same label), it is **not** a
module — consider a `Grouping` (`SHARED_PHENOTYPE`) instead.

## Module shape

- Validates against the **`Disease`** class with `category: Module`.
- Top-level: `name`, `description`, `category: Module`, `creation_date`,
  `notes`, `pathophysiology`. Optional: `treatments`, `mechanistic_hypotheses`,
  `discussions`.
- Nodes bind **GO and CL terms only** (plus UBERON `locations`, GO
  `cellular_components`). **No** CHEBI/MONDO term bindings in nodes — describe
  chemistry/disease in prose. (Exception: a `treatments` block's
  `therapeutic_agent` carries a CHEBI/NCIT id per the treatment schema.)
- Chain of ~5 nodes, each with a `role`:
  `trigger → amplifier → central_effector → effector → consequence`.
  The **`central_effector`** is normally the key conformance target — the
  disorder-agnostic, rate-limiting step. Every node carries `evidence` and
  `downstream` edges; the `notes` spell out the disorder-specific substitutions
  conforming entries make.
- **Treatment drug-target pattern** (optional but preferred when a drug acts on
  a specific node): a `treatments[]` entry uses `target_mechanisms` with a
  `treatment_effect` (`INHIBITS`/`ACTIVATES`) pointing at the node name it acts
  on. Model after `cellular_senescence` (senolytic) or `renal_cystogenesis`
  (tolvaptan).

## Evidence discipline (non-negotiable)

Every `snippet` must be an **exact substring** of the cited paper's cached
abstract. Never fabricate. For each PMID:

```bash
uv run linkml-reference-validator cache reference PMID:XXXXXXXX   # (or: just fetch-reference)
```

Do not hand-write `references_cache/*.md`. Discard any PMID whose real abstract
does not contain your snippet (DR/LLM-suggested citations are frequently wrong —
verify each one).

## Xogenesis anchor convention (pathological structure formation)

A module whose terminal output is the **formation of a pathological material
anatomical entity** X carries a lightweight, consistent **anchor stanza in
`notes`** linking to open ontologies (prose CURIEs — no schema slot). Keep it
uniform and greppable:

- **process genus** `OGMS:0000061` pathological bodily process — deliberately
  **not** GO's `anatomical structure formation` (that genus presupposes normal
  *programmed* development). Sub-type it:
  - `OGMS:0000080` **pathological transformation** — a canonical structure
    *becomes* pathological (cyst from a tubule, aneurysm from a vessel wall).
  - `OGMS:0000081` **pathological derivation** — a *new* formation replaces/adds
    to prior tissue (granuloma, thrombus, stone, neoplasm).
- **output continuant** `OGMS:0000078` pathological anatomical structure
  (discrete) or `OGMS:0000079` portion of pathological body substance
  (deposit/stone/fluid).
- **species** an `MPATH:603` (pathological anatomical entity) subtree term for
  the specific X (cyst `MPATH:62`, concretion `MPATH:614`, granuloma `MPATH:847`,
  thrombosis `MPATH:125`, abscess `MPATH:608`, aneurysm `MPATH:90`, fibrosis
  `MPATH:181`, neoplasm `MPATH:218`); **site** a `UBERON` term.
- **SNOMED CT** "Morphologically abnormal structure" (49755003) is an external
  census / gap-detection guide only — **never bound** in dismech data. If the
  target X has no MPATH class (e.g. thrombus continuant, amyloid deposit,
  atheroma), note the OBO gap in the module `notes`.

Example stanza (in `notes`):

> Xogenesis anchor: the terminal output is a granuloma (MPATH:847), an
> `OGMS:0000078` pathological anatomical structure produced by an `OGMS:0000081`
> pathological derivation; process genus `OGMS:0000061`.

Verify each anchor CURIE resolves:

```bash
uv run runoak -i sqlite:obo:mpath info MPATH:847 -O obo
uv run runoak -i sqlite:obo:ogms info OGMS:0000078 -O obo
```

Worked Xogenesis modules to copy: `renal_cystogenesis`, `granuloma_formation`,
`thrombogenesis`, `atherogenesis`, `amyloidogenesis`,
`nephrolithiasis_crystal_nucleation`, `cholelithiasis_biliary_supersaturation`,
`fibrotic_response`.

## Validation

```bash
uv run linkml-validate --schema src/dismech/schema/dismech.yaml \
  --target-class Disease kb/modules/<name>.yaml
uv run linkml-term-validator validate-data kb/modules/<name>.yaml \
  -s src/dismech/schema/dismech.yaml -t Disease --labels -c conf/oak_config.yaml
bash scripts/run_reference_validator.sh validate data kb/modules/<name>.yaml \
  --schema src/dismech/schema/dismech.yaml --target-class Disease \
  --config conf/reference_validator_config.yaml
```

Confirm every snippet is an exact substring of its cached abstract before
committing.

## Record and connect

1. **Do not add the module to a static catalog, and in particular not to a list
   in `CLAUDE.md`.** There is no module registry there any more — it did not
   scale and drifted behind `kb/modules/`, which is the source of truth.
   Discovery is `just list-modules` (or `ls kb/modules/`), which reads the module
   YAML directly, so choose a descriptive filename and keep the top-level `name`
   and `description` useful for repository search. What that makes load-bearing
   is the module's own `description:` slot: write it so it states the causal
   chain in one sentence, the drug-target pattern if there is one, the key
   conformance target, how the module is complementary to (not overlapping with)
   its sibling modules, and — for an Xogenesis module — the OGMS/MPATH/UBERON
   anchor. That description is the only place a curator will find this, so it
   must stand alone. Put curation guardrails ("do NOT create a `Foo` Disease
   entry", species caveats) in `notes:`; `just list-modules <filter>` prints both
   fields in full and matches on both.
2. Scaffold a history record:
   `just new-history --kind module --slug <name> --event CREATE --outcome changed …`
3. Wire real conformers: add `conforms_to: "<name>#<Node>"` to the matching
   pathophysiology nodes of the relevant disorder entries, then re-validate.
