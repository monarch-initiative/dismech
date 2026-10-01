# Traumatic brain injury pilot: scoping

**Status:** scoping only. No KB content has been written. This tests the proposed
injury granularity rule in design decisions §3f
([`design-decisions.md`](../../explanation/design-decisions.md#3f-injury-and-trauma-granularity-2026-10-01))
on one case before the rule is adopted.

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

If a traumatic brain injury entry and a shared secondary-injury module are added, both
existing entries should be able to conform to the module at their injury-cascade nodes.
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
- `has_subtypes:` by severity (mild, moderate, severe) only if the literature shows the
  strata differ in mechanism, not just in degree. Focal contusion and diffuse axonal
  injury are a stronger candidate split, since their tissue mechanisms differ.
- Root pathophysiology node: the mechanical event at `TISSUE` scale with UBERON
  `locations`, matching the shape `Post-Traumatic_Epilepsy` already uses.
- `computational_models:` one finite-element head-impact model, if a published one can
  be cited, linked to the axonal-injury node with `model_scale` and a `PROXY_QUANTITY`
  divergence (tissue strain standing in for axonal damage). This is the only part of the
  pilot that tests the biomechanics half of §3f.

### Module: secondary injury after neurotrauma

Working name `neurotrauma_secondary_injury`. Candidate node chain, to be checked against
the literature before any node is written:

1. Primary mechanical tissue disruption (shear and stretch of axons, vessels, cell
   membranes)
2. Blood-brain barrier breakdown
3. Ionic flux and glutamate release
4. Calcium overload and mitochondrial failure
5. Diffuse axonal injury
6. Neuroinflammation
7. Neuronal death and tissue loss

Steps 3–4 and 6 overlap existing modules. The module should point at
`glutamate_excitotoxicity` and `neuroinflammation_glial_activation` for those steps
rather than repeat them, and the `create-module` skill's guidance on complementarity
applies. If after that the new module holds only steps 1, 2 and 5, it may be better
split into a blood-brain barrier module and an axonal injury module that are each
reusable outside trauma (stroke, sepsis-associated encephalopathy).

### Conformance changes to existing entries

- `Post-Traumatic_Epilepsy`: its blood-brain barrier and neuroinflammation nodes conform
  to the new module; its epileptogenesis nodes keep their existing conformance.
- `Chronic_Traumatic_Encephalopathy`: its root trauma node conforms to the module's
  primary-injury node. Its tau node stays unconformed until a tau module exists.

## Decisions needed before curating

1. Is the §3f rule acceptable as a working hypothesis for this pilot?
2. Split by severity, by lesion type (focal vs diffuse), or neither?
3. One secondary-injury module, or smaller reusable modules (barrier, axonal injury)?
4. Should an ECTO term request for mechanical injury exposure be filed now, or after the
   pilot shows how the exposure is used?
