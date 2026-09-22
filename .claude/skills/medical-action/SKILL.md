---
name: medical-action
description: >-
  Curate or review treatments and other medical actions in dismech, including
  diagnostic testing, screening, surveillance, monitoring, counseling,
  prevention, and proposed interventions. Use for action_category, NCIT action
  terms, therapeutic agents, regimens, devices, modality, oligonucleotides,
  delivery systems, dosing intervals, and clinical-trial records. Not for
  patient-specific medical advice or changing the schema.
---

# Curate Medical Actions

Dismech records medical actions more broadly than treatment, including approved,
investigational, and proposed interventions. Curate what the source establishes
about the action, its purpose, and its status. A trial registration, mechanistic
rationale, or model-system rescue does not establish clinical efficacy or approval.

## Choose the record and purpose

Read the current `Treatment`, `Diagnosis`, `ClinicalTrial`, and
`MedicalActionCategoryEnum` definitions in `src/dismech/schema/dismech.yaml`.
These remain distinct records; there is no new `medical_actions:` section to invent.

| Record | Use |
|---|---|
| `treatments[]` (`Treatment`) | Treatment or another clinical action, with `action_category` distinguishing its purpose |
| `diagnosis[]` (`Diagnosis`) | Diagnostic entries using `diagnosis_term`, results, markers, presence, and evidence |
| `clinical_trials[]` (`ClinicalTrial`) | A registered trial and its registry phase/status, not a substitute for an action's evidence |

Preserve an existing well-placed diagnostic record; do not migrate it merely
because `Treatment` also accommodates diagnostic actions. Choose the section
whose fields fit the claim. The schema does not give `Diagnosis` an
`action_category` or treatment-target slots.

For `treatments[]`, use the broad functional `action_category`:

| Category | Purpose | Treatment-target links? |
|---|---|---|
| `THERAPEUTIC` | Treat, prevent, mitigate, or manage disease or symptoms | When supported |
| `DIAGNOSTIC` | Establish or refine diagnosis | No |
| `SCREENING` | Screening or surveillance for disease, risk, or early manifestations | No |
| `MONITORING` | Observe disease status or complications over time | No |
| `COUNSELING_INFORMATIONAL` | Education, risk communication, genetic counseling, reproductive planning | No |

**Nontherapeutic actions must not use `target_mechanisms` or
`target_phenotypes`.** Detecting, measuring, or explaining a mechanism does not
treat it. A genetic counseling action is not a mechanism-modifying intervention.
If a record bundles diagnosis and therapy, separate their claims and evidence.

## Ground the action and its components

Use `dismech-terms` for actual lookups and dynamic-enum validation. Read
[action bindings](references/action-bindings.md) when choosing an action term,
device qualifier, agent, or regimen. Keep these dimensions separate:

- `treatment_term` (or `diagnosis_term`) names the clinical action. NCIT action
  bindings must fall under the schema's clinical-intervention root; an equipment
  or substance term cannot replace an action.
- `treatment_term.therapeutic_agent` names the drug or drug class. Prefer CHEBI
  for specific small molecules and NCIT where appropriate for classes/biologics.
- `regimen_term` names an established combination protocol, not any combination
  of drugs and not a generic pharmacologic class.
- `therapeutic_modality` describes the therapeutic platform; it is not a
  substitute for `action_category` or a reason to classify counseling as therapy.

When no valid action term captures the full specificity, retain the accurate
action in `preferred_term`; omit a binding that cannot be sourced. Keep a device
identity in the supported qualifier pattern rather than binding equipment as an
action. Qualifier terms need their own online validation.

Read [modalities and oligonucleotides](references/modalities-and-oligonucleotides.md)
for ASO/siRNA mechanism, target, chemistry, and dosing. New carrier descriptions
belong in Treatment-level `delivery_system`, for any modality; see
[delivery systems](../../../docs/delivery-systems.md). The nested carrier fields
remain valid for legacy records, not the pattern to copy into new ones.

## State evidence and status precisely

Use `dismech-references` for source identity, exact quotes, and evidence grading.
Keep approved use, off-label use, trial investigation, and a proposed mechanism
distinct in the description/context and evidence. `Treatment` has no dedicated
approval-status slot: do not invent one or reuse a trial's recruitment status.
Record the relevant disease, population, jurisdiction, and date when the source
makes them material to an approval or recommendation claim.

Evidence for a therapeutic action and evidence that it acts on a particular
mechanism are separate claims. Use `pathograph` when adding `target_mechanisms`:
targets are bare names, and the edge must describe the sourced effect. Keep
model evidence and inferred human benefit distinguishable. A proposed action can
be recorded with its limitations; do not promote a hypothesis into established care.

Read [clinical trials](references/clinical-trials.md) for NCT and ICTRP fetching,
registry evidence, and phase/status enums. Registration establishes what was
registered; publications are needed for reported outcomes.

## Validate

Run the normal schema, term, snippet, and final batched validation in CLAUDE.md.
For changed treatment-target edges, also run `just check-causal-targets <file>`.
For new qualifier bindings run `just check-qualifier-terms-online`; for a delivery
block run `just check-delivery-system`. Inspect nontherapeutic actions for target
links even when the pathograph targets themselves resolve correctly.
