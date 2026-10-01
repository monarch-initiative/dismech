# Traumatic brain injury pilot: scoping

**Status:** scoped, decisions settled, no KB content written yet. This tests the
injury granularity rule in design decisions §3f
([`design-decisions.md`](../../explanation/design-decisions.md#3f-injury-and-trauma-granularity-2026-10-01))
on one case before it is applied more widely.

## Why traumatic brain injury

Two sequela entries already exist and already model parts of the acute injury cascade
inside themselves:

- `Post-Traumatic_Epilepsy` has a root `Traumatic Brain Injury` node (`TISSUE` scale) and
  downstream nodes for blood-brain barrier disruption with albumin extravasation,
  neuroinflammation and inflammasome activation, reactive astrogliosis with impaired
  glutamate homeostasis, and GABAergic interneuron loss. It conforms to
  `epilepsy_excitation_inhibition_imbalance` for the epileptogenic part only.
- `Chronic_Traumatic_Encephalopathy` has a root `Repetitive Head Trauma` node, then
  perivascular hyperphosphorylated tau and TDP-43 pathology, and conforms to
  `tdp43_proteinopathy`.

If a traumatic brain injury entry and the modules below are added, both existing entries
should be able to conform to those modules at their injury-cascade nodes.
Whether that works without distorting either entry is what the pilot tests.

## Ontology coverage (checked 2026-10-01)

| Need | Finding |
|---|---|
| `disease_term` | `MONDO:0858950` *traumatic brain injury*. It sits under `MONDO:0021178` *injury* and also under `MONDO:0005560` *brain disorder*, so it is reachable from `MONDO:0000001` *disease* and validates as a `DiseaseTerm` without a schema change. |
| Parent and sibling terms | `MONDO:0043510` *brain injury* (also under *disease*); `MONDO:0800482` *head injury* (under *injury* only, so not admissible as a `disease_term` today). No MONDO term for concussion or mild traumatic brain injury was found (`concussion` search returned only post-traumatic epilepsy). |
| Related entries already in the KB | `MONDO:0043264` post-traumatic epilepsy; `MONDO:0043512` traumatic encephalopathy (bound by the CTE entry). |
| Human exposure term (ECTO) | None. `l~injur`, `l~trauma`, `l~concuss`, `l~impact`, `l~crush`, `l~collision`, `l~acceleration`, `l~force` all returned nothing. `ECTO:9001937` *exposure to explosive* exists but is a chemical-exposure class, not blast overpressure. |
| Experimental condition (XCO) | `XCO:0000968` experimental traumatic brain injury, `XCO:0000969` lateral fluid percussion injury. Usable for animal-model context only. |
| Existing modules to reuse | `glutamate_excitotoxicity` (glutamatergic stimulation, calcium overload, mitochondrial dysfunction, excitotoxic neuronal death); `neuroinflammation_glial_activation` (danger signal release, glial activation, cytokine release, bystander injury); `mitochondrial_dysfunction`; `tdp43_proteinopathy`; `epilepsy_excitation_inhibition_imbalance`. No module covers blood-brain barrier breakdown in the CNS, diffuse axonal injury, or tau pathology. |

## Proposed shape

### Entry: `Traumatic_Brain_Injury`

- `disease_term`: `MONDO:0858950`.
- `environmental:` the mechanical injury, unbound, with the ECTO searches above recorded
  in `notes`.
- `progression:` primary injury (minutes), secondary injury (hours to weeks), chronic
  phase (months to years). These are phases, not subtypes.
- No `has_subtypes:` split. Severity is a gradient of one exposure and is recorded in
  the environmental record and in `progression:`. Focal contusion and diffuse axonal
  injury have different tissue mechanisms but usually co-occur in the same patient, so
  they are two branches of the pathograph, not two strata of patients.
- Root pathophysiology node: the mechanical event at `TISSUE` scale with UBERON
  `locations`, matching the shape `Post-Traumatic_Epilepsy` already uses. It has two
  downstream branches: focal contusion (vascular disruption, haemorrhage, local necrosis)
  and diffuse axonal injury.
- `computational_models:` one finite-element head-impact model, if a published one can
  be cited, linked to the axonal-injury node with `model_scale` and a `PROXY_QUANTITY`
  divergence (tissue strain standing in for axonal damage). This is the only part of the
  pilot that tests the biomechanics half of §3f.

### Modules: small and reusable

The cascade is split across several small modules rather than one trauma-specific
module, so each can be reused outside trauma. Candidate chain, each step to be checked
against the literature before a node is written:

| Step | Home |
|---|---|
| Primary mechanical tissue disruption | The entry's own root node (trauma-specific, not a module) |
| Blood-brain barrier breakdown | **New module**, working name `blood_brain_barrier_breakdown`. Reusable for ischaemic stroke, sepsis-associated encephalopathy, and the existing `Post-Traumatic_Epilepsy` barrier node |
| Diffuse axonal injury | **New module**, working name `traumatic_axonal_injury`. Check scope against `peripheral_axonal_degeneration` and `corticospinal_tract_axonopathy` first; if one of them can be widened instead, do that |
| Ionic flux, glutamate release, calcium overload, excitotoxic death | Existing `glutamate_excitotoxicity` |
| Mitochondrial failure | Existing `mitochondrial_dysfunction` |
| Neuroinflammation | Existing `neuroinflammation_glial_activation` |

The `create-module` skill applies to the two new modules, including its guidance on
stating complementarity with sibling modules in the module `description`.

### Conformance changes to existing entries

- `Post-Traumatic_Epilepsy`: its blood-brain barrier node conforms to
  `blood_brain_barrier_breakdown` and its neuroinflammation node to
  `neuroinflammation_glial_activation`; its epileptogenesis nodes keep their existing
  conformance.
- `Chronic_Traumatic_Encephalopathy`: repetitive mild injury is mostly axonal, so a link
  from its trauma node to `traumatic_axonal_injury` is the candidate. Its tau node stays
  unconformed until a tau module exists.

## Decisions (2026-10-01)

1. The §3f rule is accepted as the working rule.
2. `MONDO:0021178` *injury* is added to the `DiseaseTerm` and `DiseaseOrSubtypeTerm`
   roots. This does not affect the pilot, since `MONDO:0858950` was already admissible,
   but it makes burn, frostbite and fracture entries possible.
3. No subtype split, by severity or by lesion type (see above).
4. Small reusable modules, not one secondary-injury module.
5. No ECTO term request. The exposure stays unbound with the searches in `notes`.

## Build order

1. `blood_brain_barrier_breakdown` and `traumatic_axonal_injury` modules.
2. `Traumatic_Brain_Injury` entry conforming to them and to the existing modules.
3. Conformance edits to `Post-Traumatic_Epilepsy` and `Chronic_Traumatic_Encephalopathy`.
4. The finite-element model link, if a citable model is found.
