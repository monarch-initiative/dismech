# Hypothesis-Based Phenotype Algorithms

**Status:** **Enacted** — the schema slots are live and Timothy syndrome is the
worked example. Maintainer-approved (`@cmungall`, 2026-07-12).
**Tracking:** [#6245](https://github.com/monarch-initiative/dismech/issues/6245)
**Registered in:** [Design Decisions §11](explanation/design-decisions.md)

**What was enacted (vs. the original proposal below):** `Definition` gained
`derivation_basis` (`DefinitionDerivationBasisEnum`), `validation_status` (the
`AlgorithmValidationStatus` object: `status` + `rationale` + optional
`evidence`), and reuses `attaches_to` to link the pathograph node(s) it is
predicated on. A gating test
(`test_hypothesis_based_definition_attaches_to_foreign_keys`) enforces that a
`MECHANISTIC_HYPOTHESIS` definition has resolving `attaches_to` refs. The
declared-vs-inferred consistency lint and the KGX-export treatment remain
follow-ups. The rest of this document is the original design write-up, retained
as the rationale of record.

## Summary

DisMech `definitions` blocks can already carry a
`definition_type: PHENOTYPE_ALGORITHM` (a PheKB-/OHDSI-style computable phenotype).
Today those algorithms are implicitly assumed to be grounded in **established,
consensus phenotype criteria**. This proposal adds a way to mark a phenotype
algorithm as **derived from — and predicated on — an unproven mechanistic
hypothesis**, by linking it (via the existing `attaches_to` slot) to the
pathograph node(s) it operationalizes and inferring the hypothesis basis from
them.

The goal is to let DisMech carry a *mechanism hypothesis, its model-system
evidence, and a computable EHR case-finding query* as one linked, epistemically
honest object — something a raw phenotype-algorithm library cannot express.

This is not a one-off: Timothy is one instance of a recurring **trigger-provoked
latent disease** archetype (Brugada/fever, malignant hyperthermia/anesthesia,
G6PD/oxidants, drug-induced long-QT, CPVT/exercise, …), most of whose disorders
already exist in the KB. See the companion survey
[Mechanism-hypothesis-driven EHR case-finding](reports/hypothesis-driven-ehr-case-finding-2026-07-12.md)
for the candidate register — it also shows why `derivation_basis` must span an
*established ↔ emerging* spectrum rather than being a single flag.

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

Two new slots on `Definition` plus a reuse of the existing `attaches_to` slot; one
new enum and one small object class. All are optional; existing entries are
unaffected (their absence reads as the established-criteria default).

### 1. `derivation_basis` — new enum `DefinitionDerivationBasisEnum`

Records the epistemic grounding, orthogonal to `definition_type`:

| Value | Meaning |
|---|---|
| `ESTABLISHED_CRITERIA` | Published consensus criteria or a validated computable phenotype (e.g. OHDSI Phenotype Library). The implicit default for existing entries. |
| `MECHANISTIC_HYPOTHESIS` | Predicated on a specific, not-yet-proven disease mechanism hypothesis. Membership is contingent on the hypothesis holding. |
| `MODEL_SYSTEM_EXTRAPOLATION` | Extrapolated from an animal/in-vitro model result not yet demonstrated in humans. |

### 2. Link to the pathograph — **reuse the existing `attaches_to` slot** (not a new hypothesis ID)

Rather than storing a separate `hypothesis_group_id` string on the definition and
keeping it in sync, point the algorithm **directly at the pathophysiology
node(s)/edge(s) it is predicated on**, reusing the existing `attaches_to` slot and
its `[<file>:]<kind>#<name>` hash-anchor grammar (already used by `discussions`,
e.g. `pathophysiology#Amyloid Plaque Formation`). For the motivating case the
definition would attach to the fever-exacerbation node/edge, e.g.
`attaches_to: [pathophysiology#Fever-triggered CaV1.2 activation]`.

The hypothesis basis is then **inferred from the pathograph**, not re-declared:
those nodes'/edges' `downstream[].hypothesis_groups` resolve to the disease-level
`mechanistic_hypotheses[]` entries, which carry the `status`
(`CANONICAL` / `ALTERNATIVE` / `EMERGING` / `DEPRECATED`). So tooling can traverse
*algorithm → attached node/edge → hypothesis group → status* with no redundant
key. This makes `derivation_basis` (below) a **declared-and-cross-checkable**
value rather than a free-floating assertion: an algorithm attached only to
`CANONICAL` nodes that declares `MECHANISTIC_HYPOTHESIS` (or vice versa) is a
lintable inconsistency.

### 3. `validation_status` — a structured object, not a bare enum

Validation maturity lives on the `Definition` (not `CriteriaSet`), and is an
**object** so it can carry a free-text rationale (and, later, evidence) alongside
the graded status — mirroring how `MechanisticHypothesis` pairs a `status` enum
with a `description`. Proposed `AlgorithmValidationStatus` class:

| Slot | Range | Meaning |
|---|---|---|
| `status` | `AlgorithmValidationStatusEnum` | `PROPOSED` (drafted, never run) / `UNVALIDATED` (executable, not yet evaluated against a gold standard) / `VALIDATED_AGAINST_GOLD_STANDARD` (PPV/sensitivity characterized). |
| `rationale` | `string` | Why this status — what was (or was not) run, against which cohort, with what result. |
| `evidence` | `EvidenceItem` (multivalued, optional) | Citation(s) backing the status. This is the **same `EvidenceItem` model used everywhere else** — a `reference` (PMID / DOI / NCT / structured-source CURIE) plus a verbatim `snippet` (the excerpt) and an `explanation`, with the snippet snippet-validated against the cached source. So a validation study, or a paper reporting the algorithm's yield, is captured as PMID + excerpt rather than only prose. |

`rationale` (free text) and `evidence` (PMID/DOI + excerpt) are complementary: the
rationale narrates *why* the status is what it is; each `evidence` item pins a
specific verifiable claim to a citable source and quote. A `PROPOSED` algorithm may
have rationale but no evidence yet; a `VALIDATED_AGAINST_GOLD_STANDARD` one should
carry at least one `evidence` item pointing at the validation study.

`definition_type` stays `PHENOTYPE_ALGORITHM`; the new axes layer on top. A new
`definition_type` value was considered and rejected (see Alternatives).

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

pathophysiology:
# ... the fever-exacerbation node/edge added per #6245, whose downstream edges
# opt into the hypothesis group:
- name: Fever-triggered CaV1.2 activation
  # downstream:
  # - target: Ventricular tachyarrhythmia (torsade de pointes)
  #   hypothesis_groups: [fever_exacerbated_cav1.2]
  # - target: Seizures
  #   hypothesis_groups: [fever_exacerbated_cav1.2]

definitions:
- name: Fever-associated arrhythmia case-finding query for latent CACNA1C carriers
  definition_type: PHENOTYPE_ALGORITHM
  derivation_basis: MECHANISTIC_HYPOTHESIS       # NEW (declared; cross-checked vs. attached nodes)
  attaches_to:                                    # reused slot; grounds the algorithm in the pathograph
  - pathophysiology#Fever-triggered CaV1.2 activation
  validation_status:                              # NEW (object, not bare enum)
    status: PROPOSED
    rationale: >-
      Drafted from the zebrafish result; never executed against a human EHR/OMOP
      dataset. No PPV/sensitivity yet.
    # Once a validation study exists, its status flips and cites the study as
    # a standard EvidenceItem (PMID + excerpt), e.g.:
    #   status: VALIDATED_AGAINST_GOLD_STANDARD
    #   rationale: >-
    #     Executed against the CACNA1C-genotyped arm of an EHR biobank; the
    #     febrile-onset arrhythmia query reached PPV 0.42 for a rare/likely-
    #     pathogenic CACNA1C variant vs. chart-reviewed controls.
    #   evidence:
    #   - reference: PMID:XXXXXXXX
    #     supports: SUPPORT
    #     evidence_source: HUMAN_CLINICAL
    #     snippet: "<verbatim excerpt reporting the PPV / validation result>"
    #     explanation: Gold-standard validation of the febrile-arrhythmia query.
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

- **Foreign-key test** (`tests/test_data.py`): a definition's `attaches_to`
  references must resolve to real nodes/objects in the same entry (the same
  `[<file>:]<kind>#<name>` resolution `discussions.attaches_to` already needs) —
  and if `derivation_basis: MECHANISTIC_HYPOTHESIS`, at least one attached
  node/edge should sit in a non-`CANONICAL` hypothesis group.
- **Consistency lint** (advisory): warn when the declared `derivation_basis`
  disagrees with the basis *inferred* from the attached nodes' hypothesis-group
  status (e.g. declared `ESTABLISHED_CRITERIA` but attached to an `EMERGING`-group
  node). Advisory, not gating — the pathograph annotations may lag the algorithm.
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
4. **A bare `hypothesis_group_id` string on the definition.** Rejected in favor of
   reusing `attaches_to` to link the pathograph nodes/edges directly (see §2): a
   free-floating ID duplicates a key that already lives on the causal edges and
   can drift out of sync, whereas node links let the hypothesis basis be
   *inferred* and cross-checked.
5. **A bare `validation_status` enum.** Rejected in favor of an object carrying a
   `rationale` (and optional `evidence`), so the maturity claim is auditable
   rather than a bare token.

## Open questions for review

- **Resolved by review:** `validation_status` lives on `Definition` (not
  `CriteriaSet`) and is an **object** with a free-text `rationale`; the
  hypothesis link is `attaches_to` node references with the basis inferred, not a
  standalone `hypothesis_group_id`.
- Should a `CriteriaSet`-level status override still be allowed for the case where
  a definition bundles a screening set and a confirmatory set at different
  maturities, or is a definition-level status sufficient?
- If the pathograph node an algorithm should attach to does not exist yet, is a
  transient `preferred_term`-style reference acceptable, or must the node be added
  first (so `attaches_to` always resolves)?
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
