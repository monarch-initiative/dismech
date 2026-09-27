---
name: extend-schema
description: >
  Use when changing the data model / schema in src/dismech/schema/*.yaml; when
  considering a schema change, including deciding whether a curation need
  warrants one at all; or when migrating KB content after a schema change. Not
  for filling in an existing slot (see the curation skills) or for ontology
  bindings inside the schema's dynamic enums (see dismech-terms).
---

# Extend the dismech LinkML Schema

## When to use

- Adding a class, slot, or enum to `src/dismech/schema/dismech.yaml`.
- Narrowing, deprecating, or removing an existing one.
- Deciding whether a curation need warrants a schema change at all.
- Migrating `kb/` content after a schema change lands.

Do **not** use for: filling an existing slot (use the curation skills),
ontology `meaning` / `reachable_from` bindings inside dynamic enums (use
`dismech-terms`), or `kb/groupings/` membership logic (use `curate-grouping`).

## The schema files

| File | Class it governs |
|---|---|
| `src/dismech/schema/dismech.yaml` | `Disease` (disorders, modules), `Grouping`, `ModuleCollection` — 322 KB, the main one |
| `src/dismech/schema/curation_stub.yaml` | `CurationStub` (`stubs/`) |
| `src/dismech/schema/history.yaml` | `history/` records |
| `src/dismech/schema/hypothesis_assessment.yaml`, `hypothesis_reconciliation.yaml` | `kb/hypotheses/` |
| `src/dismech/schema/research_synthesis.yaml` | deep-research synthesis |
| `src/dismech/schema/classifications/` | the `classifications` block |
| `src/dismech/schema/dismech.history.yaml` | not a schema — an auto-appended edit log beside `dismech.yaml`. Never hand-edit it; `validate-all` skips `*.history.yaml` |

This guide mostly pertains to the *core schema* ie dismech.yaml

## Do Background Research

It is likely your proposal has been discussed before. Be sure to check issues.

## Major Schema Changes should be approved

If you are reviewing a schema change and it is not trivial, block merging until
approved by @cmungall or @mellybelly.

## Have a data population strategy

It is easy to have "nice to have" new slots. But think hard about the population strategy.

Will this be deterministically populated? If so, include code.

If non-deterministic, you MUST include string guidelines on how to populate. Especially
if subjective in nature. We want to avoid situations where agent and reviewer go back and forth
arguing on populating the slot because we underspecified how it was to be populated.

In general, things that involve new ontology terms should be fine because we have good practice
and deterministic search tools and checker tools.

## A note on extensions to the evidence model

It is easy to come up with proposed extensions to the evidence model but implementing them can be harder.
Adding some way of being able to determine good evidence from bad evidence is laudable, but there must be
good guidelines on populating this.

Don't try and over generalize - a strategy for evidence for cellular assays may be different for one for clinical approval.

Remember the core of dismech is the biological mechanism, this requires a lot of careful coordinated thought about how to
represent assays, readouts, interpretations etc. Be sure to read the docs and evidence slides.

## Does this need a schema change?

1. Does a slot already express this? #972 proposed treatment_category; the
answer was that therapeutic_modality already was that discriminator. Do not add a second, redundant slot.
2. Can it be derived instead of stored? Cancer cell of origin is derived from the pathograph (genetic_context.variant_origin on a node) and design decisions says no cell_of_origin: slot should be added.
3. Is qualifiers the right home? Usually not — prefer a dedicated slot
4. Is this a decision the register already made? Read `docs/explanation/design-decisions.md` before proposing, and cite it.

## The migration hazard (read before narrowing anything)

Additive changes are easier if they are optional or recommended slots. However, anything
that narrows or invalidates will be hard and needs a proper schema migration path.

Otherwise the schema change will need to be also bundle a giant set of changes on multiple yamls,
and the 100s of open PRs will become invalid!

In future we may properly implement schema migrations. For now you should do these kinds of changes
in two stages - a superposition stage where the narrower form can co-exist, weakly deprecating the old form;
then once migration is done (including open PRs) narrow the schema.

## Mechanics — what to regenerate

```bash
just lint-schema                              # linkml-lint -- dismech.yaml ONLY, not the other five
just validate-all                             # every *disorder* file; modules/groupings have their own recipes
just check-enum-values                        # whole-KB, offline
just validate-terms-schema                    # the schema's own dynamic enums
just gen-jsonschema                           # -> project/jsonschema/ (gitignored)
just gen-schema-docs                          # -> elements/ (derived; CI commits it, you don't)
```

**Committed generated artifacts:** `src/dismech/datamodel/dismech.py` and
`dismech_pydantic.py` are in git and are what `gen-python` writes.
**TODO — resolve:** history is inconsistent about whether a schema change must
regenerate them (#10758 did; #9806 and #10629 did not). Decide the rule and
state it here.

**Do not hand-commit** `elements/`, `docs/` HTML, or anything else the
generate-pages workflow owns. See CLAUDE.md "What NOT to commit".

## Downstream — what a new slot must be wired into

TODO. Checklist to confirm and expand:

- [ ] `src/dismech/entity_refs.py` — `SECTION_KEYS` if the new section can be
      the target of an `<kind>#<name>` reference. It is the source of truth
      shared by validation and rendering.
- [ ] `src/dismech/graph.py` — if the slot carries a `target` that should draw
      an edge. Note bare-name targets vs entity-reference grammar; mixing them
      up is silent (#10112).
- [ ] `src/dismech/render.py` + `src/dismech/templates/` — page rendering.
- [ ] `src/dismech/export/` — `kgx_export.py`, `cx2_export.py`,
      `browser_export.py`, `tabular_export.py` as applicable.
- [ ] `src/dismech/qc_plugins.py` — compliance scoring.
- [ ] A test in `tests/` (`test_clinical_burden_schema.py`,
      `test_genetic_schema.py`, `test_medical_action_schema.py` are the
      existing per-area schema tests).
- [ ] `CLAUDE.md` — curator-facing semantics, if a curator will fill the slot.
- [ ] `docs/explanation/design-decisions.md` — if this settles or reopens a
      recorded decision.
- [ ] **A `history/schema/` record.** The convention is live — `history/schema/`
      already holds records for `ModuleCategoryEnum`, `TherapeuticModalityEnum`,
      `maxo-removal`, `entity-ref-prefix-normalisation` and others, i.e. exactly
      the enum-narrowing and slot-addition changes this skill is for. Unlike the
      KB kinds, `schema` records need an explicit `--path`:

      ```bash
      just new-history --kind schema --slug <EnumOrSlotName> \
        --path src/dismech/schema/dismech.yaml \
        --event EDIT --outcome changed \
        --summary "Add <slot>" --agent-tool claude-code --model <model-id> \
        --pr <PR_NUMBER> --details "What changed and why."
      just validate-history <path-printed-by-new-history>
      ```

## Common mistakes

TODO. Seeds:

- Adding a slot that duplicates one that exists under a name you did not guess.
- Narrowing an enum without a plan for in-flight PRs.
- Leaving prose that argues for a value the schema no longer has.
- Renaming instead of deprecating, breaking entries mid-review.
- Committing `elements/` or `project/` output alongside the schema change.

## Validation before the PR

```bash
just lint-schema
just validate-terms-schema
just qc
```

`just qc` already chains `check-duplicate-keys`, `check-enum-values`,
`validate-all`, `validate-modules`, `validate-groupings` and
`validate-module-collections` (`project.justfile:879`), so do not run those
separately — `validate-all` is the slow one and you would pay for it twice.
`validate-terms-schema` is not in the chain and is the one that checks the
dynamic enums you just edited.
