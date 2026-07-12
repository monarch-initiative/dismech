# Hypothesis-Based Phenotype Algorithms (Proposal)

**Status:** Proposal / open decision — *not yet enacted in the schema.*
**Tracking:** [#6245](https://github.com/monarch-initiative/dismech/issues/6245)
**Registered in:** [Design Decisions §11 (Gaps)](explanation/design-decisions.md)
**Maintainer sign-off requested:** `@cmungall`

## Summary

DisMech `definitions` blocks can already carry a
`definition_type: PHENOTYPE_ALGORITHM` (a PheKB-/OHDSI-style computable phenotype).
Today those algorithms are implicitly assumed to be grounded in **established,
consensus phenotype criteria**. This proposal adds a way to mark a phenotype
algorithm as **derived from — and predicated on — an unproven mechanistic
hypothesis**, and to link it to the disease-level `mechanistic_hypotheses` entry
it operationalizes.

The goal is to let DisMech carry a *mechanism hypothesis, its model-system
evidence, and a computable EHR case-finding query* as one linked, epistemically
honest object — something a raw phenotype-algorithm library cannot express.

## Motivating example (why now)

Issue [#6245](https://github.com/monarch-initiative/dismech/issues/6245) reports a
zebrafish study of Timothy syndrome
([PMID:42426269](https://europepmc.org/article/MED/42426269)): *"elevated water
temperature elicited arrhythmia and seizure-like behavior even in overtly normal
heterozygotes, implicating fever as a modifiable risk."* Fever is known to
activate CaV1.2, the channel mutated in Timothy syndrome.

This suggests a computable phenotype: **query an EHR/OMOP dataset for a new
ventricular arrhythmia or QT-prolongation event temporally following a documented
febrile episode**, to surface candidate *latent / mild* CACNA1C-spectrum cases —
carriers who never meet the classical syndromic case definition (prolonged QT +
syndactyly + neurodevelopmental features) because they are asymptomatic at
baseline.

The epistemic catch: **that query is only valid if the CaV1.2-thermal-activation
mechanism actually operates in humans.** Running it is simultaneously

1. a case-finding tool, and
2. a *test* of the mechanistic hypothesis — a positive yield is itself partial
   evidence for the mechanism.

If we drop this query into `definitions` with the same `definition_type:
PHENOTYPE_ALGORITHM` we use for the OHDSI-validated Rheumatoid Arthritis and
Diabetes Mellitus algorithms, a downstream consumer will mistake a speculative,
hypothesis-generating query for a consensus-grounded, validated one. Preventing
that conflation is the core motivation.

## The problem stated precisely

A phenotype algorithm has (at least) two independent epistemic axes that the
current schema collapses into one:

- **What kind of definition is it?** — captured today by `definition_type`
  (`DIAGNOSTIC_CRITERIA`, `PHENOTYPE_ALGORITHM`, `CASE_DEFINITION`, `OTHER`).
- **How well-grounded is it, and where does it come from?** — *not captured at
  all.* An OHDSI-validated RA cohort and a mechanism-predicated fever-arrhythmia
  query are both `PHENOTYPE_ALGORITHM`, yet they sit at opposite ends of an
  evidentiary spectrum.

## What already exists (and is reused)

DisMech already has most of the machinery; it is simply not wired to
`Definition`:

- **`mechanistic_hypotheses`** — a disease-level (and module-level) list of
  `MechanisticHypothesis` objects, each with a stable `hypothesis_group_id`, a
  human-readable `hypothesis_label`, a `status`
  (`CANONICAL` / `ALTERNATIVE` / `EMERGING` / `DEPRECATED`), its own `evidence`,
  and `applies_to_subtypes`. A fever-exacerbation hypothesis is a textbook
  `EMERGING` entry.
- **`downstream[].hypothesis_groups`** — causal edges opt into a hypothesis group
  by ID, so fever→arrhythmia and fever→seizure edges can be attributed to the
  same group as the algorithm.
- **`evidence_source: MODEL_ORGANISM`** — lets the zebrafish result be cited as
  first-class evidence, kept explicitly distinct from human evidence (per the
  [evidence policy](explanation/design-decisions.md), model-organism evidence
  must not be the sole support for a human phenotype claim). The "tie to a model
  system" is therefore already representable.
- **`discussions` with `kind: HUMAN_MODEL_MISMATCH`** — the right home for the
  plain knowledge-gap capture the issue also requests: evidence *exists* in
  zebrafish; human translational validity is the open question.

What is missing is (a) a link from a `Definition` to the hypothesis it tests, and
(b) a marker of the algorithm's epistemic grounding and validation state.

## Proposed schema extension

Add three slots to the `Definition` class. All are optional; existing entries are
unaffected (their absence reads as the established-criteria default).

### 1. `derivation_basis` — new enum `DefinitionDerivationBasisEnum`

Records the epistemic grounding, orthogonal to `definition_type`:

| Value | Meaning |
|---|---|
| `ESTABLISHED_CRITERIA` | Published consensus criteria or a validated computable phenotype (e.g. OHDSI Phenotype Library). The implicit default for existing entries. |
| `MECHANISTIC_HYPOTHESIS` | Predicated on a specific, not-yet-proven disease mechanism hypothesis. Membership is contingent on the hypothesis holding. |
| `MODEL_SYSTEM_EXTRAPOLATION` | Extrapolated from an animal/in-vitro model result not yet demonstrated in humans. |

### 2. `hypothesis_group_id` — **reuse the existing slot** (range `string`)

Points the algorithm at the disease-level `mechanistic_hypotheses[]` entry it
operationalizes. This is the key wire: it lets tooling traverse
*hypothesis → causal edges (via `downstream[].hypothesis_groups`) → algorithm*
as one connected sub-model.

### 3. `validation_status` — new enum `AlgorithmValidationStatusEnum`

Makes the case-finding maturity explicit:

| Value | Meaning |
|---|---|
| `PROPOSED` | Drafted; never executed against data. |
| `UNVALIDATED` | Executable but not yet evaluated against a gold-standard/labeled cohort. |
| `VALIDATED_AGAINST_GOLD_STANDARD` | PPV/sensitivity characterized against a reference standard. |

`definition_type` stays `PHENOTYPE_ALGORITHM`; the two new axes layer on top. A
new `definition_type` value was considered and rejected (see Alternatives).

## Worked example (Timothy syndrome)

```yaml
mechanistic_hypotheses:
- hypothesis_group_id: fever_exacerbated_cav1.2
  hypothesis_label: >-
    Fever/hyperthermia lowers the threshold for CaV1.2-driven arrhythmia and
    seizures
  status: EMERGING
  description: >-
    Elevated body temperature activates CaV1.2, augmenting the mutant persistent
    inward calcium current, so febrile episodes may unmask arrhythmia and seizure
    susceptibility even in CACNA1C carriers who are asymptomatic at baseline.
  evidence:
  - reference: PMID:42426269
    evidence_source: MODEL_ORGANISM
    supports: SUPPORT
    snippet: >-
      elevated water temperature elicited arrhythmia and seizure-like behavior
      even in overtly normal heterozygotes, implicating fever as a modifiable
      risk
    explanation: >-
      Zebrafish cacna1c model demonstrates temperature-triggered decompensation
      in phenotypically normal heterozygotes.

definitions:
- name: Fever-associated arrhythmia case-finding query for latent CACNA1C carriers
  definition_type: PHENOTYPE_ALGORITHM
  derivation_basis: MECHANISTIC_HYPOTHESIS       # NEW
  validation_status: PROPOSED                     # NEW
  hypothesis_group_id: fever_exacerbated_cav1.2   # reused slot; ties to the hypothesis
  scope: >-
    EHR/OMOP case-finding; hypothesis-generating, NOT a validated diagnostic
    algorithm.
  description: >-
    Identify individuals with a new ventricular arrhythmia / QT-prolongation
    event within a short window after a documented febrile episode, as candidate
    latent CACNA1C-spectrum cases. Predicated on the fever_exacerbated_cav1.2
    hypothesis; a positive yield is itself partial evidence for that hypothesis.
  criteria_sets:
  - name: Febrile-onset rhythm disturbance
    description: >-
      Fever episode (temperature or diagnosis code) followed within N days by a
      new ventricular arrhythmia / long-QT event, absent a prior arrhythmia
      history.
    # inclusion_criteria / exclusion_criteria ...
  notes: >-
    Hypothesis-based case-finding query, not a consensus phenotype definition.
    Yield must be interpreted as evidence bearing on fever_exacerbated_cav1.2,
    not as confirmed Timothy-spectrum diagnoses.
```

## Guardrails to bake in

- **Foreign-key test** (`tests/test_data.py`): if
  `derivation_basis: MECHANISTIC_HYPOTHESIS`, then `hypothesis_group_id` **must**
  resolve to a declared `mechanistic_hypotheses[].hypothesis_group_id` on the
  same entry — the same referential discipline `conforms_to` and the grouping
  foreign keys already enforce.
- **Renderer badge**: hypothesis-based / unvalidated definitions must be visibly
  flagged (e.g. "⚗ hypothesis-based — not a validated phenotype") so they never
  render as clinical criteria.
- **Evidence discipline unchanged**: a model-system-only hypothesis still may not
  be the sole support for a *human* phenotype claim; the human CaV1.2-fever
  activation literature must accompany the zebrafish citation before any human
  phenotype edge is asserted.

## Alternatives considered

1. **New `definition_type` value** (e.g. `HYPOTHESIS_BASED_CASE_FINDING`).
   Rejected: "what kind of definition" and "how well-grounded" are independent
   axes; folding them into one enum makes `PHENOTYPE_ALGORITHM` +
   `derivation_basis` unrepresentable and forces a combinatorial enum.
2. **Free-text only in `notes`/`scope`.** Rejected: not machine-queryable, and
   the whole point is to let tooling (and export layers) distinguish validated
   from speculative algorithms and traverse to the underlying hypothesis.
3. **A separate top-level `hypothesis_based_algorithms` slot.** Rejected: it
   would duplicate the `Definition`/`CriteriaSet` structure and split phenotype
   algorithms across two homes.

## Open questions for review

- Should `validation_status` live on `Definition` or on `CriteriaSet` (a
  definition may bundle a screening set and a confirmatory set at different
  maturities)?
- Do we want an explicit `predicts_population` marker distinguishing
  *"finds known cases of disease X"* from *"predicts an as-yet-unvalidated latent
  subpopulation"*? For now the `MECHANISTIC_HYPOTHESIS` basis plus `scope` prose
  carries this.
- Should the KGX/BioLink export surface hypothesis-based algorithms differently
  (or suppress them) so they are never consumed as validated phenotypes
  downstream?
- Is `MODEL_SYSTEM_EXTRAPOLATION` distinct enough from `MECHANISTIC_HYPOTHESIS`
  to warrant its own value, or should model-system provenance ride entirely on
  the linked hypothesis's `evidence`?

## Relationship to existing decisions

- Extends, does not contradict, the **evidence & provenance policy** (§6) — the
  model-organism-not-sole-support rule applies unchanged.
- Complements the deferred **structural `knowledge_gaps:` slot** (§11): a
  hypothesis-based algorithm is the *actionable* counterpart to a knowledge gap —
  a proposed way to gather the missing human evidence.
- The **`discussions` / `HUMAN_MODEL_MISMATCH`** kind remains the home for the
  narrative gap; this proposal adds the *computable* artifact that a curator
  might run to resolve it.
