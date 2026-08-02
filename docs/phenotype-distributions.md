# Statistical Phenotype Distributions

A **phenotype distribution** is the full statistical object behind a number that
dismech currently records as a single coarse value: the distribution of a
phenotype, an onset age, a lab value, or an event count within a defined
disease cohort — curated as a separate artifact and cited from a disease entry
as evidence. The same file format also carries **EHR-derived phenotype
profiles**, a smaller and quite different object described below.

Schema: [`src/dismech/schema/phenotype_distribution.yaml`](https://github.com/monarch-initiative/dismech/blob/main/src/dismech/schema/phenotype_distribution.yaml)
Tooling: `src/dismech/phenotype_distribution.py`
Worked examples: `examples/phenotype_distributions/`
Curated collections: `kb/phenotype_distributions/` (created by the first curated
collection; this directory does not exist yet)

## Why a separate artifact

A dismech phenotype today carries a `frequency:` band and a snippet:

```yaml
phenotypes:
- name: Exocrine Pancreatic Insufficiency
  frequency: VERY_FREQUENT
  evidence:
  - reference: PMID:30986316
    snippet: "…characterized by pancreatic insufficiency…"
```

That is five HPO bands' worth of resolution over a claim that a real cohort
analysis answers with a denominator, an interval, an ascertainment context, and
a phenotype definition. The band is the right thing to *display* on a disease
page; it is the wrong thing to be the only record of what was measured. Two
studies reporting "the same" frequency at 45% and 88% are usually not in
conflict — they defined the phenotype differently or ascertained the cohort
differently — and the flat model has nowhere to put that.

Rather than growing the disease entry, distributions live in their own
collections and bridge back. This is the same division the FDA
surrogate-endpoint table already uses: source-level detail stays in the source
table, and the disease entry holds a reference.

## The shape of a record

One `PhenotypeDistributionRecord` is **one estimand, one phenotype, one disease,
one stratum, one analysis**. Strata are separate records rather than nested, so
each is independently citable.

```yaml
distributions:
- record_id: CF-PI-PROPORTION-001
  measure_type: PHENOTYPE_PROPORTION
  phenotype:
    preferred_term: Exocrine Pancreatic Insufficiency
    phenotype_term: {term_id: HP:0001738, term_label: Exocrine pancreatic insufficiency}
    phenotype_definition: >-
      At least one recorded diagnosis, or dispensed pancreatic enzyme
      replacement therapy on two or more dates at least 30 days apart.
  cohort:
    data_source_type: EHR
    ascertainment: CLINIC_BASED_REFERRAL
    n_individuals: 1240
  distribution:
    family: BETA
    estimation_framework: BAYESIAN_POSTERIOR
    parameters:
    - {parameter_name: alpha, value: 1070.0}
    - {parameter_name: beta, value: 172.0}
    summary:
      point_estimate: 0.862
      point_estimate_type: POSTERIOR_MEAN
      interval_lower: 0.842
      interval_upper: 0.881
      interval_type: CREDIBLE_EQUAL_TAILED
      interval_level: 0.95
  implied_frequency_class: VERY_FREQUENT
  bias_risks: [ASCERTAINMENT_BIAS, SINGLE_SITE]
```

`implied_frequency_class` is the bridge back to the coarse world: the HPO band
the distribution implies, so the two representations can be compared directly.
The lint rejects a band that the record's own point estimate contradicts.

### Which distribution family

`DistributionFamilyEnum` covers four shapes:

| Shape | Families | Typical estimand |
|---|---|---|
| Binary occurrence | `BERNOULLI`, `BINOMIAL`, `BETA`, `BETA_BINOMIAL` | phenotype proportion, penetrance |
| Continuous | `NORMAL`, `LOGNORMAL`, `GAMMA`, `WEIBULL`, `EMPIRICAL`, `NONPARAMETRIC_QUANTILE`, `KAPLAN_MEIER` | onset age, lab value, time to event |
| Counts and rates | `POISSON`, `NEGATIVE_BINOMIAL`, and zero-inflated forms | exacerbations per year |
| Compositional | `CATEGORICAL`, `DIRICHLET`, `LOGISTIC_NORMAL`, `MULTIVARIATE_NORMAL` | weights over a simplex |

Family alone does not fix the parameterization — gamma shape/rate and
shape/scale are different numbers — so `parameterization_note` records the
convention whenever the family admits more than one.

Use `EMPIRICAL` with `bins`/`quantiles` when a publication reports only a
histogram or percentiles. Do not fit a family the source did not fit.

The family also fixes support discreteness for all but six values, so leave
`discrete` unset unless the family is one of `EMPIRICAL`, `MIXTURE`,
`KAPLAN_MEIER`, `NONPARAMETRIC_QUANTILE`, `UNIFORM`, or `OTHER` — the cases
where a tabulation may be over counts or over bins of a continuous quantity and
a consumer genuinely cannot tell. Restating what `CATEGORICAL` or `GAMMA`
already settles just gives the two a chance to disagree; the lint errors on a
contradiction and warns on a repetition. A test pins this list against the enum,
because a family added to the enum but not to the lint's map would silently stop
being checked and would falsify every prose copy of the six.

### Time to event is not a proportion

Age-dependent penetrance reported as "60% by adulthood" throws away the age the
percentage applies to. Use `measure_type: TIME_TO_EVENT` with
`family: KAPLAN_MEIER` and populate `time_to_event.curve`, so the estimate stays
a curve.

## EHR-derived phenotype profiles

The second shape this schema carries, and a much smaller one. A
`PhenotypeDistributionCollection` records the full statistical object behind a
literature estimate. A **`ProfileSet`** records something different: what
co-occurs in a disease cohort, exported from a fitted model, reduced to what a
disease page can show.

```
ProfileSet ──has──> Profile ──has──> CodeDistribution ──has──> WeightedCode
     │                 │                (per domain,            (code + label
profile_source      disease              with its                + weight
(provenance)        (MONDO)              vocabulary)             + qualifier?)
```

```yaml
profiles:
- profile_id: CHARMPHENO-EDS-DYSAUTONOMIA-001
  profile_label: EDS dysautonomia — POTS, syncope, and GI dysmotility
  disease:
    disease_name: Ehlers-Danlos Syndrome
    disease_term: {term_id: MONDO:0020066, term_label: Ehlers-Danlos syndrome}
  profile_share: 0.00011972462747401996
  code_distributions:
  - clinical_domain: CONDITION
    code_vocabulary: OMOP_CONCEPT_ID
    truncated: true
    weighted_codes:
    - {code: '444070', code_label: Tachycardia, code_weight: 0.15634}
    - {code: '4159659', code_label: Postural orthostatic tachycardia syndrome, code_weight: 0.11381}
```

### Design principle: a disease page, not a model report

An earlier draft of this schema grew a full model layer — component counts,
inference methods, hyperparameters, per-domain reliability, cohort arms and the
denominators attached to them. That was the wrong altitude twice over. Per-domain
weights, reliability and precision/recall are **model evaluation**, not
disease-page content; and they are the fastest-moving part of the pipeline, so a
curation schema encoding them would need revising every time the models moved.

What a page needs is a label, a disease, and weighted codes. Everything else
lives in `profile_source`, including an open `profile_metadata` key/value map, so
the model layer can be reshaped freely without touching the profile contract.

The shape follows the proposal from the author of the models that produce this
data ([CHARMPheno](https://github.com/oneilsh/CHARMPheno)); the design decisions
below are theirs, and the reasoning is recorded because the alternative was tried
first and did not survive review.

### One profile, one MONDO term

A profile points at a single MONDO term. Nesting and overlap between cohorts is
expressed by MONDO's own subclass tree, which dismech already renders, so this
schema ships **no** cohort, arm, or grouping vocabulary of its own for profiles.

### Codes are opaque; the vocabulary is declared

`code` is a bare identifier — an OMOP concept id, an ICD-10-CM code, a LOINC
code — and `code_vocabulary` on the enclosing distribution says which system it
belongs to. Two things drove this:

* **Not a CURIE.** Exposing source-vocabulary CURIEs (SNOMED, RxNorm, LOINC)
  directly proved brittle in practice. A consumer resolves the code against the
  declared vocabulary and version, not against a prefix map.
* **Not OMOP-shaped either.** An earlier draft named the fields `concept_id` and
  `concept_name`, which quietly made OMOP the only representable case. Data may
  arrive already coded in something else, so the field names stay generic and the
  vocabulary is stated.

A profile's codes are **clinical codes, not ontology terms**. A consumer that
reads them as HPO terms because dismech is HPO-centric would be wrong today for
every existing profile.

### Multi-domain, kept factored

A profile holds one distribution *per domain* and encodes **no** cross-domain
combination — no weights, no merged vector. How a condition distribution and a
drug distribution should be weighed against each other is an open modelling
question and a rendering choice, and freezing an answer into the contract would
make the schema wrong as soon as the answer changed.

### Weights are not prevalences

The topic-model literature calls a component's share of corpus mass its
"prevalence". This schema never does, in either shape. In a disease knowledge
base `prevalence` means a count of patients carrying a label over a stated
denominator of patients at risk, and dismech has a `prevalence[]` block that
means exactly that. A profile's share is a fraction of fitted model mass; the two
are not convertible, and rendering one beside the other under the same word
invites a comparison that does not hold. The slots are `profile_share` and
`code_weight`.

`code_weight` is a code's mass *within its own distribution*, which is not the
frequency of that finding among patients — the confusion worth guarding hardest
against, because the numbers look like frequencies.

### Truncation is stated, not inferred

Almost every display export is a top-N subset, so its weights do not sum to 1.
`truncated: true` says so. Without it, a top-N export and a distribution that
lost mass are indistinguishable; the lint warns when weights fall short and the
flag is absent, and errors when they exceed 1.


## Evidence modelling: SEPIO

The evidence layer follows [SEPIO](https://sepio-framework.github.io/sepio-linkml/)
and deliberately uses the same vocabulary as the SEPIO pilot proposed for the
main dismech schema in
[#7439](https://github.com/monarch-initiative/dismech/issues/7439):

* an `EvidenceLine` is **one argument**, carrying a direction and a strength;
* it holds one or more `DataItem`s (the quoted text or the statistic);
* each item is `reported_in` a typed `Document`.

`EvidenceDirectionEnum` copies the permissible values of the native
`EvidenceItemSupportEnum` verbatim, so the two forms stay mechanically
inter-convertible; a test enforces that they do not drift apart.

Splitting direction from strength matters more for statistics than for prose. A
precisely estimated null and an underpowered null point the same way with very
different force. The example collection shows both on one proposition: a cohort
estimate that is `SUPPORT` / `MODERATE`, and a review sentence that is
`PARTIAL` / `WEAK` because it supports the qualitative claim while saying
nothing about the band.

## Importing into a dismech entry

Every record declares where it belongs:

```yaml
  dismech_bindings:
  - target_kind: DISEASE
    target_entry: Cystic_Fibrosis
    target_section: PHENOTYPE_FREQUENCY
    target_path: phenotypes#Exocrine Pancreatic Insufficiency
    evidence_reference: PHENODIST:CF-PI-PROPORTION-001
    proposed_value: VERY_FREQUENT
    import_status: PROPOSED
```

`just phenodist-rebuild` renders each curated record to
`references_cache/PHENODIST_<record_id>.md`, a deterministic line-oriented file
in the same format as the Orphanet, ClinGen, and ICEES structured sources. The
disease entry then cites it like any other structured source, quoting a row:

```yaml
phenotypes:
- name: Exocrine Pancreatic Insufficiency
  frequency: VERY_FREQUENT
  evidence:
  - reference: PHENODIST:CF-PI-PROPORTION-001
    supports: SUPPORT
    evidence_source: OTHER
    snippet: "CF-PI-PROPORTION-001 | PHENOTYPE_PROPORTION | BETA | 0.862 | 95% CREDIBLE_EQUAL_TAILED 0.842-0.881 | n=1240 | whole cohort"
    explanation: Cohort estimate places the proportion in the 80-99% band.
```

The column order of that summary row is part of the cache contract and is
pinned by a test: reordering it would silently invalidate every snippet already
quoted from it. As with every other file in `references_cache/`, these are
generated — **never hand-write or hand-edit one**.

`import_status` keeps the lifecycle visible: `PROPOSED` until a curator reviews
it, then `ACCEPTED`, `REJECTED`, `SUPERSEDED`, or `DEFERRED` with
`binding_notes` saying why.

## Provenance tier

Every collection must declare `provenance_tier`, so "these numbers are
illustrative" is a machine-readable fact rather than a sentence in a description
that tooling cannot read:

| Tier | Meaning |
|---|---|
| `CURATED` | Human-curated from literature or a named source; citable from a kb entry |
| `TOOL_EXPORTED` | Transcribed from a model or pipeline export; the numbers are real, the mapping to disease concepts is curator judgement |
| `ILLUSTRATIVE` | Synthetic or placeholder; must never be cited or rendered into the cache |

The renderer *raises* on an `ILLUSTRATIVE` collection rather than writing it to
`references_cache/`, so synthetic numbers cannot become citable even by mistake.

Note the exact scope of that guard: it is a hard error for `ILLUSTRATIVE` only.
A `TOOL_EXPORTED` collection under `examples/` — like the CHARMPheno one — stays
uncitable because `just phenodist-rebuild` only globs `kb/phenotype_distributions/`,
which is a directory convention rather than an enforced invariant, backed by a
test asserting no kb entry cites an example record. The tier is the hard guard
for synthetic numbers; the directory is the guard for real-but-unreviewed ones.

## What gets verified

Three checks exist because the schema's credibility rests on its terms and
quotes being checkable, not merely well-formed:

- **Ontology terms.** `--check-terms` (on in `just qc`) resolves every
  `term_id`/`term_label` pair against OAK using `conf/oak_config.yaml`, and
  errors when a CURIE does not exist or carries a label that is not its own.
  This is the check that catches the hallucinated-CURIE pattern: an identifier
  that exists but names something else.

    **Only prefixes present in `conf/oak_config.yaml` are checked** — currently
    HP, MONDO, CL, GO, UBERON, CHEBI, NCIT and the other configured ontologies.
    **LOINC is not configured, so LOINC terms are not verified**, and a clean
    `--check-terms` run does not mean every term was checked. That gap is real:
    the one term error found by hand while writing these examples
    (`LOINC:2075-0`, serum chloride, where sweat chloride `LOINC:2077-6` was
    meant) is in precisely the class the automated check cannot see. Verify
    LOINC by hand. A network-backed adapter that fails to respond yields a
    warning, not an error — an unperformed lookup is not evidence of a bad term.
- **Quoted evidence.** A `DataItem` citing a fetchable document — `PMID:`,
  `DOI:`, `clinicaltrials:`, `ORPHA:`, `CGGV:`, `CGDS:`, `ICEES:`, `NCIT:`,
  `PHENODIST:` — must be a verbatim substring of that document's
  `references_cache/` file, and the cache file must exist. Without this, an
  unverified quote could be rendered into a generated `PHENODIST_*.md` and then
  cited from a kb entry, where `validate-references` would verify it against the
  cache dismech itself produced — laundering an unverified quote into a
  validated-looking one.
- **Stale cache.** `write_cache_files` prunes orphaned `PHENODIST_*.md`, so a
  renamed or deleted `record_id` cannot leave a citable file behind. Pruning
  runs only for a *full* rebuild — no paths, or directory paths — so naming an
  individual collection file never deletes another collection's cache;
  `--no-prune` disables it entirely.

## Commands

```bash
# Validate one collection (schema + lint)
just validate-phenotype-distribution kb/phenotype_distributions/my_collection.yaml

# Validate all collections, including the worked examples (part of `just qc`)
just validate-phenotype-distributions

# Regenerate references_cache/PHENODIST_*.md for curated collections
just phenodist-rebuild
```

`validate-phenotype-distributions` runs schema validation, the lint, and the OAK
term check.

The lint catches what LinkML cannot express: duplicate record ids, an
`evidence_reference` disagreeing with its record, a `target_entry` that does not
resolve to a real kb file, a matrix whose value count contradicts its
dimensions, an interval that fails to bracket its point estimate, and a
frequency band the point estimate does not support. On the profile side it
catches code weights summing above 1, a short distribution that does not declare
itself `truncated`, and a code listed twice under the same qualifier.

## The worked examples

`examples/phenotype_distributions/` holds two collections. Both are excluded
from `just phenodist-rebuild` so neither can become citable, and a test asserts
that no kb entry cites one and no cache file for one is committed.

**`cystic_fibrosis_illustrative.yaml`** — the literature/cohort side, with
**illustrative placeholder numbers from a synthetic cohort**: Beta proportion,
lognormal onset, Kaplan-Meier time-to-event, negative-binomial counts with a sex
contrast, and a laboratory-value distribution with bins. Its one real citation
is the PMID:30986316 snippet on the pancreatic-insufficiency record, which is
already cached and verified in this repository and is scoped to the qualitative
claim it actually supports — deliberately paired with the quantitative cohort
line so the two evidence strengths sit side by side.

**`charmpheno_population_eds.yaml`** — the profile side, populated from a
**real exported model** in the CHARMPheno dashboard's `population_eds` bundle.
Every number — the code probabilities and the profile shares — is transcribed
from that bundle's exported JSON. What is curator judgement, and marked as such,
is the reading of an unsupervised component as a named clinical pattern.

Its two profiles are each chosen to show something:

| Profile | Shows |
|---|---|
| `CHARMPHENO-EDS-HYPERMOBILE-001` | An `anchor`-quality profile with half its mass on its own diagnosis code — real, precise, and a tautology. Binding `REJECTED`. |
| `CHARMPHENO-EDS-DYSAUTONOMIA-001` | A profile recovering the EDS-dysautonomia association from coding alone. Binding `PROPOSED`, because there is no denominator a frequency band could come from. |

That both bindings fall short of import is the point: a profile can be real,
precise, well-provenanced, and still be the wrong number for the slot.

## Relationship to existing dismech blocks

| Block | Relationship |
|---|---|
| `phenotypes[].frequency` | A distribution record with `measure_type: PHENOTYPE_PROPORTION` is the statistical form of this band; `implied_frequency_class` connects them. |
| `prevalence[]` | Disease *occurrence* in a population. A distribution describes a phenotype *within* the disease. Different denominators. |
| `biochemical[].reference_ranges` | Clinical decision intervals. A `LABORATORY_VALUE` distribution is the observed cohort distribution — related but not the same object. |
| `genetic[].case_fractions` | Per-gene share of cases; the same "structured estimate with its own population and evidence" pattern, restricted to genetic heterogeneity. |
| `association_signals` | Disease-disease co-occurrence on comorbidity entries; a `COMORBIDITY_CO_OCCURRENCE` record can feed one. |
| `definitions[]` | A record's `phenotype_definition` may point at a formal computable definition via `definition_ref`. |
