---
name: curate-grouping
description: >
  Create, edit, review, or audit dismech disease groupings in
  kb/groupings/*.yaml. Use for Grouping records, member unions, grouping_basis
  and grouping_rationale, membership_criteria boolean logic, criteria_semantics,
  differentiating_mechanisms, grouping foreign keys, ontology-closure audits,
  or grouping validation and rendering. Do not use for a Disease entry's
  classifications block; use disease-classification for that.
---

# Curate a Disease Grouping

Treat `kb/groupings/` as the source of truth. A grouping is an explicit curated
union of already-distinct diseases, modules, or other groupings. It validates
against `Grouping`, not `Disease`, and points down by listing `members`; it does
not recreate the MONDO hierarchy.

## Discover relevant examples

```bash
rg --files kb/groupings -g "*.yaml" | sort
rg -il "<disease family or mechanism>" kb/groupings
sed -n "1,160p" kb/groupings/Mucopolysaccharidoses.yaml
```

Use `Mucopolysaccharidoses` for a `NECESSARY` criteria example and
`Inherited_Arrhythmia_Syndromes` for nested boolean logic with
`NECESSARY_AND_SUFFICIENT` criteria. Inspect the current YAML rather than
copying a static catalog.

## Define the boundary

- Set `name`, optional `display_name`, `creation_date`, `description`,
  `grouping_basis`, `grouping_rationale`, `membership_criteria`, and `members`.
- Use `grouping_basis` to record why the members belong together; inspect the
  schema for current enum values rather than inventing one.
- Explain the lump/keep-split boundary in `grouping_rationale`. A grouping sits
  over distinct entities, so do not put a `LUMP` flag on it.
- An optional MONDO mapping is a cross-reference, not the source of membership.

## Model membership criteria

Each `membership_criteria` block needs a human-readable `description`. Its
optional `logic` is a `LogicalCriterion` tree:

- Branch nodes use `operator: AND`, `OR`, or `NOT` with `operands`.
- Leaf nodes use `criterion_predicate` and the matching payload:
  `HAS_PHENOTYPE`, `HAS_GENE`, `CONFORMS_TO_MODULE`,
  `HAS_BIOLOGICAL_PROCESS`, `HAS_CLASSIFICATION`, `HAS_INHERITANCE`,
  `HAS_MAPPING`, or `OTHER`.
- Use `negated: true` to negate a leaf when clearer than a `NOT` branch.

Choose `criteria_semantics` deliberately:

- `NECESSARY`: member => criteria. Audit listed members for contradictions.
- `SUFFICIENT`: criteria => member. Discover candidate additions.
- `NECESSARY_AND_SUFFICIENT`: both directions; the criteria define membership.

Do not encode an acknowledged exception to a necessary condition. A listed
member that fails a necessary criterion is a contradiction to resolve by
correcting the member annotation, criterion, or membership.

HP and GO leaves are evaluated over `is_a`/`part_of` ontology closure;
`HAS_GENE` remains exact. If ontology access fails, evaluation falls back to
exact matching and can under-report satisfaction. State the criterion at the
intended conceptual level rather than compensating for a missing annotation.

## Add members and differentiators

Grouping members are diseases, named disease subtypes, or nested disease
groupings. Do not add a mechanism module as a member. Use a `module` reference
inside membership criteria or a differentiating mechanism when the module helps
define or distinguish diseases; use a `ModuleCollection` in
`kb/module_collections/` when the task is to organize modules themselves.

- `members[].member` must resolve to a real `Disease.name` or grouping name
  according to `member_type`; `SUBTYPE` members name their parent disease.
- Every referenced module and optional `#Node Name` must exist.
- Use `differentiating_mechanisms` for what distinguishes a member from its
  siblings; bind genes, phenotypes, processes, or modules when appropriate.
- Keep grouping names unique.

## Nest a grouping inside another

A grouping can list another grouping as a member with `member_type: GROUPING`.
That declaration is the *only* source of hierarchy: the index page's tree, a
grouping page's "Where this grouping sits" strip, and the evaluator all read it
and nothing else (no MONDO inference).

- Nest only when every disease member of the child belongs to the parent under
  the parent's own criteria, and both rationales agree on the relation. Run
  `just grouping-nesting-audit` first: it prints the declared tree and the
  undeclared containments (child member set ⊆ parent member set). A
  containment is a lead, not a ruling — orthogonal cross-cuts such as
  `Centrosomopathies` vs `Primary_Microcephaly_Spectrum` contain each other's
  members by design and must stay separate.
- A nested grouping **replaces** the direct rows it covers; do not list a disease
  both directly and through a nested grouping. Keep the differentiating text by
  folding it into the GROUPING row's `differentiating_mechanisms` (one entry per
  covered disease, gene bindings included), as `Motor_Neuron_Disorders` does for
  `Bulbospinal_Muscular_Atrophies`.
- Diseases reached through a nested grouping are still members: `just
  check-groupings` evaluates them against the parent's criteria and prints them
  as `(via <child>)`, and the parent page shows them as `nested via` rows that
  count toward coverage.
- Record the change in the parent's `notes` and in a history record under
  `history/other/<Parent_slug>/`.

## Validate and inspect

```bash
just validate-grouping kb/groupings/<Grouping>.yaml
just check-groupings kb/groupings/<Grouping>.yaml
just check-groupings --strict kb/groupings/<Grouping>.yaml
just gen-grouping-page kb/groupings/<Grouping>.yaml
```

Use `just validate-groupings` for the full set. Treat the evaluator's
`UNKNOWN` as missing information, not failure; investigate every
`NOT_SATISFIED` listed member. Generated `pages/groupings/*.html` files are
derived and must not be committed with hand-authored changes.
