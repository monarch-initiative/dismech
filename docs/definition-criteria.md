# Definition Criteria: Combining Sets and Linking Criteria to Phenotypes

A `definitions[]` entry can split published criteria into named
`criteria_sets`, each with its own `minimum_required` count. Two facts about
those criteria had no slot of their own:

- **How the sets combine.** A set's `minimum_required` says how many of *its*
  criteria are needed. Nothing said whether a case must meet every set, any
  one set, or is graded by which set it meets. That lived only in the
  definition's `description`.
- **Which phenotype a criterion is.** A criterion (`CriteriaItem`) could carry
  an HPO `term`, but its only link to the entry's phenotype of the same name
  was the shared CURIE. The criterion's term is not checked by
  `linkml-term-validator` either, because `CriteriaItem` has no ontology
  binding, the same gap `qualifiers` had (#10197).

Two optional slots close these gaps: `Definition.criteria_set_logic` and
`CriteriaItem.attaches_to`.

## `criteria_set_logic`: how the sets combine

| Value | Meaning | Worked example |
|---|---|---|
| `ALL_REQUIRED` | A case must satisfy every set. | `Antiphospholipid_Syndrome`, both the 2006 revised Sapporo and 2023 ACR/EULAR criteria |
| `ANY_SUFFICIENT` | Satisfying any one set is enough. The sets are alternative routes to one diagnosis. | `Neuromyelitis_Optica_Spectrum_Disorder`, the AQP4-IgG-positive and -negative pathways |
| `GRADED` | Each set defines its own grade, class or certainty level, and a case is classified by the set it meets. | `HELLP_Syndrome`, the Mississippi classes 1 to 3 |
| `WEIGHTED_SCORE` | Criteria carry points and a total across the sets decides. | `Pyoderma_Gangrenosum`, the PARACELSUS score |

Rules:

- **Copy it from the source.** Set the value only where a cited source states
  how the sets combine, and quote that statement in the definition's or a
  set's `evidence`. The Delphi pyoderma gangrenosum criteria are left unset
  because the cached abstract gives the major and minor criteria but not the
  rule joining them; the full paper does, and is not what the entry cites.
- **Absent means not recorded.** It does not default to `ALL_REQUIRED`.
- **Two or more sets only.** On a definition with one set the value says
  nothing, and `just check-entity-refs` reports it.
- **It does not change `minimum_required`**, which still counts criteria
  within one set.
- **Separate published systems are separate definitions**, not sets of one.
  The Tennessee and Mississippi HELLP systems answer different questions and
  are two `definitions[]` entries.
- **Points and thresholds have no slot yet.** For `WEIGHTED_SCORE`, state them
  in the definition's prose (its `description`, or the `validation_status`
  `rationale`, where PARACELSUS records its 10-point threshold).
- **A mixed rule takes the value of its top level.** The 2023 APS criteria
  require an entry criterion and then a points total within one set; the sets
  are combined `ALL_REQUIRED`, and the points belong to the second set.

## `attaches_to` on a criterion: which phenotype it tests for

```yaml
core_clinical_characteristics:
- preferred_term: Optic neuritis
  term:
    id: HP:0100653
    label: Optic neuritis
  attaches_to:
  - phenotypes#Optic Neuritis
```

The value uses the same `<kind>#<name>` grammar as `Discussion.attaches_to`,
and is resolved as a foreign key by the same sweep (`just check-entity-refs`).
It is usually a phenotype; a biochemical marker, histopathology finding or
genetic record is allowed where the criterion is one of those.

Rules:

- **Point at what the criterion tests for, not at whatever shares its CURIE.**
  NMOSD's "Acute myelitis" criterion and its "Longitudinally Extensive
  Transverse Myelitis" phenotype are both bound to `HP:0012486` *Myelitis*,
  and the phenotype is narrower than the criterion. The criterion is left
  unlinked.
- **A criterion that keeps its own `term` must carry the referenced
  phenotype's binding**, id and label alike. The phenotype's binding is the
  one checked against HPO, so this is what keeps the criterion's copy honest.
  `just check-entity-refs` fails otherwise. A criterion naming two phenotypes
  may carry either one's term.
- **Leave it absent when nothing in the entry corresponds.** A criterion such
  as "Social or occupational impairment" has no phenotype to point at.

### Finding and backfilling links

```bash
just list-criteria-item-refs                        # census, whole KB
just list-criteria-item-refs --format tsv           # one row per criterion
just list-criteria-item-refs kb/disorders/X.yaml --apply
```

Each criterion without `attaches_to` is classified:

| Status | Meaning | Written by `--apply` |
|---|---|---|
| `EXACT` | One phenotype carries the criterion's term, and the criterion's wording is that phenotype's `name` or `preferred_term` | yes |
| `TERM_ONLY` | One phenotype carries the term under different wording | no: read both |
| `AMBIGUOUS` | Several phenotypes carry the term, usually rows split by subtype | no |
| `NO_MATCH` | No phenotype carries the term | no: the entry may lack the phenotype, or one binding is wrong |
| `NO_TERM` | The criterion has no term | no |

`--apply` inserts two lines per criterion instead of round-tripping the file,
and skips any criterion it cannot locate unambiguously in the text. Run
`just validate` on each file it touches. The census moves with every curation
PR, so run the recipe rather than quoting a count.

## What these slots do not settle

- **Per-criterion points and a set-level threshold** for weighted scores.
- **What `minimum_required` counts** when a set has criteria in several
  slots. In practice it counts `core_clinical_characteristics` or
  `inclusion_criteria`, with `exclusion_criteria` all absent, but the schema
  does not say so.
- **Unlinked criterion terms are still unchecked** against the ontology. A
  linked criterion is covered through its phenotype; a `NO_MATCH` or
  `TERM_ONLY` criterion's term is not.
