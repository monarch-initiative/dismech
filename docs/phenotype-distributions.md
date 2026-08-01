# Statistical Phenotype Distributions

A **phenotype distribution** is the full statistical object behind a number that
dismech currently records as a single coarse value: the distribution of a
phenotype, an onset age, a lab value, an event count, or a latent phenotype
profile, within a defined disease cohort — curated as a separate artifact and
cited from a disease entry as evidence.

Schema: [`src/dismech/schema/phenotype_distribution.yaml`](https://github.com/monarch-initiative/dismech/blob/main/src/dismech/schema/phenotype_distribution.yaml)
Tooling: `src/dismech/phenotype_distribution.py`
Worked examples: `examples/phenotype_distributions/`
Curated collections: `kb/phenotype_distributions/`

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
| Compositional | `CATEGORICAL`, `DIRICHLET`, `LOGISTIC_NORMAL`, `MULTIVARIATE_NORMAL` | latent phenotype profile weights |

Family alone does not fix the parameterization — gamma shape/rate and
shape/scale are different numbers — so `parameterization_note` records the
convention whenever the family admits more than one.

Use `EMPIRICAL` with `bins`/`quantiles` when a publication reports only a
histogram or percentiles. Do not fit a family the source did not fit.

### Time to event is not a proportion

Age-dependent penetrance reported as "60% by adulthood" throws away the age the
percentage applies to. Use `measure_type: TIME_TO_EVENT` with
`family: KAPLAN_MEIER` and populate `time_to_event.curve`, so the estimate stays
a curve.

## Latent phenotypes

Model-derived records come from unsupervised phenotype models over structured
records — the reference implementation being
[CHARMPheno](https://github.com/oneilsh/CHARMPheno), which fits LDA / HDP /
structural topic models to OMOP data and exports probabilistic patient profiles.

### Design principle: the common denominator, not one model's output

This area iterates fast. Model classes, export shapes, and even which
diagnostics are trustworthy have all changed repeatedly, with decisions
explicitly reversed as evidence came in. A curation schema that encoded one
family's export would need revising every time that family moved, and would
quietly misrepresent the next one.

So the model layer holds only what LDA, HDP, structural topic models, matrix
factorizations, mixtures, and their successors all share:

| Common to all model classes | Where it goes |
|---|---|
| A component with an identity, label, and ranked weighted features | `LatentPhenotype` + `WeightedFeature` |
| A distribution of component weight over a population | `DistributionEstimate` (`EMPIRICAL`, `DIRICHLET`, `LOGISTIC_NORMAL`, …) |
| Optional covariate dependence of prevalence | `CovariateEffect` |
| Per-component quality metrics | `ReliabilityReadout` |
| How much data actually backed the component | `LatentPhenotype.estimation_scope` (+ `_size`) |
| Enough provenance to find the fit again | `LatentPhenotypeModel` |

Everything family-specific — block and arm layouts, masking rules, optimization
schedules, bespoke diagnostics — goes in `model_properties` as name/value pairs,
or in `notes`:

```yaml
model:
  model_properties:
  - name: gating_variable
    property_value: source_cohort
  - name: component_blocks
    property_value: components 0-79 shared background; components 80-99 EDS foreground
```

A new export shape should be recordable without a schema change. If it is not,
the missing thing is probably not a common denominator. A test asserts that
family-specific structure has not crept back into `LatentPhenotypeModel` as
first-class slots.

`estimation_scope` is the one place where a mechanism like gating does need to
leave a trace, because what a consumer needs downstream is not the mechanism but
its consequence: a component estimated from a 0.5%-prevalence arm is backed by
~959 documents, not by the 191,876-document corpus.

### Compositional distributions

Two families cover what these models emit, and both need vector or matrix
parameters:

* **Dirichlet / categorical** — a concentration or weight vector over
  components. Store it as a `DistributionParameter` with `vector_value` and
  `index_labels`.
* **Logistic-normal** — component prevalence conditioned on covariates and
  sampled as `eta ~ Normal(mu, Sigma); theta = softmax(eta)`. Store `mu` as a
  vector parameter and the correlation matrix as a `MatrixParameter`, naming the
  pinned `reference_component` and recording `identified` and `support_count`.
  Unlike a Dirichlet this represents components that co-vary, which is the
  reason such models exist.

Covariate coefficients go in `covariate_effects` with a mandatory
`coefficient_scale` — a coefficient on a latent logit scale is not a probability
difference and cannot be read as one.

### A component is not a disease concept

`LatentPhenotype` separates what the model produced (`top_features`,
`component_quality`, `corpus_prevalence`) from a curator's judgement about what
it means (`mapped_phenotype_terms` plus a stated `mapping_basis`). Never import
a component weight into a phenotype slot without that mapping — and note that
even with it, a component's code probability is conditional on the component, so
it still is not the phenotype's frequency in the cohort.

`component_quality` matters here. An `anchor`-quality component largely restates
the diagnosis code that defined its cohort — in the worked example, one such
component puts half its mass on the EDS type-3 code itself — so it is close to
circular as evidence. A `phenotype`-quality component whose top codes form a
coherent clinical pattern is a different proposition.

### Suppression is not zero

Exported histograms routinely withhold bins whose cell count falls below a
privacy threshold. `DistributionBin.suppressed` keeps that distinct from a
reported zero and from an unreported bin — the difference between "the tail is
small" and "the tail is unknown". In the worked example twelve of fifty bins are
suppressed, all in the upper tail.

## Reliability and bias

Two blocks exist because an EHR-derived number is only as good as the data
domain it came from.

`ModelDomain` / `DomainReliability` record, per source domain (conditions,
drugs, measurements, procedures), what the reliability assessment rests on and
what it measured. Domains are identified **by name, never by position**, so that
reordering them cannot silently reassign an assessment to the wrong data.

Read reliability as a caution flag, not a weight. Where domain weighting has
been tested directly the headroom was small and not recoverable from quantities
read off the fitted model — structural distinctiveness and token ownership
underperformed both a fixed baseline and directly learned weights — and no fixed
combination rule beat the primary domain alone in aggregate, while a secondary
domain still rescued the individual diseases whose evidence lives in it. That is
a routing conclusion, which is why `domain_role` (`PRIMARY` / `SPECIALIST` /
`SUPPORTING` / `EXCLUDED`) sits alongside `reliability_score` and is the field a
consumer should act on.

`IdentityAttestation` asserts `row_count`, `unique_person_count`, and
`one_row_per_person` without persisting identifiers. A held-out supervised
readout is honest only when each analysed row is a distinct person; an
attestation that is missing, false, or self-contradictory should have the
readout **rejected**, not discounted. The lint enforces internal consistency.

`bias_risks` is an enum rather than prose so records can be filtered before
import, and so "nobody checked" is visibly different from "checked and clean".
The lint warns when a record declares neither `bias_risks` nor `caveats`.

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

## Commands

```bash
# Validate one collection (schema + lint)
just validate-phenotype-distribution kb/phenotype_distributions/my_collection.yaml

# Validate all collections, including the worked examples (part of `just qc`)
just validate-phenotype-distributions

# Regenerate references_cache/PHENODIST_*.md for curated collections
just phenodist-rebuild
```

The lint catches what LinkML cannot express: duplicate record ids, an
`evidence_reference` disagreeing with its record, a `target_entry` that does not
resolve to a real kb file, a matrix whose value count contradicts its
dimensions, an interval that fails to bracket its point estimate, a
self-contradictory identity attestation, and a frequency band the point estimate
does not support.

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

**`charmpheno_population_eds.yaml`** — the model-derived side, populated from a
**real exported model** currently displayed in the CHARMPheno dashboard: the
`population_eds` bundle, a gated block-wise correlated STM over 191,876
one-document-per-person records with K=100 (80 shared background + 20
Ehlers-Danlos foreground components). Every number — theta histograms, NPMI,
pair coverage, corpus prevalence, code probabilities, covariate coefficients,
correlations, the eta scale and its standard error — is transcribed from the
bundle's exported JSON. What is curator judgement, and marked as such, is the
mapping from an unsupervised component to a dismech phenotype.

Its five records are each chosen to show a different failure mode:

| Record | Shows |
|---|---|
| `MIXTURE-001` | Vector-valued weights across all 20 foreground components; prior capacity is not patient proportion |
| `T96-THETA-001` | A whole-population theta distribution that is a spike at zero with 12/50 bins suppressed — correct and useless |
| `T96-CODEPROB-001` | An `anchor`-quality component with half its mass on its own diagnosis code |
| `T91-CODEPROB-001` | A `phenotype`-quality component recovering the EDS-dysautonomia association from coding alone |
| `T93-LOGISTICNORMAL-F63-001` | Covariate conditioning plus a correlation block supported by 1,124 observations, not 191,876 |

Three of the five bindings are `REJECTED` or `DEFERRED`. That is the point: a
record can be real, precise, well-provenanced, and still be the wrong number for
the slot.

## Relationship to existing dismech blocks

| Block | Relationship |
|---|---|
| `phenotypes[].frequency` | A distribution record with `measure_type: PHENOTYPE_PROPORTION` is the statistical form of this band; `implied_frequency_class` connects them. |
| `prevalence[]` | Disease *occurrence* in a population. A distribution describes a phenotype *within* the disease. Different denominators. |
| `biochemical[].reference_ranges` | Clinical decision intervals. A `LABORATORY_VALUE` distribution is the observed cohort distribution — related but not the same object. |
| `genetic[].case_fractions` | Per-gene share of cases; the same "structured estimate with its own population and evidence" pattern, restricted to genetic heterogeneity. |
| `association_signals` | Disease-disease co-occurrence on comorbidity entries; a `COMORBIDITY_CO_OCCURRENCE` record can feed one. |
| `definitions[]` | A record's `phenotype_definition` may point at a formal computable definition via `definition_ref`. |
