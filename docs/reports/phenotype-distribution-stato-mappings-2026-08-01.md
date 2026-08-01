# STATO mappings and LinkML idiom review for the phenotype-distribution schema

**Target:** `src/dismech/schema/phenotype_distribution.yaml` as proposed in
[#7612](https://github.com/monarch-initiative/dismech/pull/7612).
**Date:** 2026-08-01.
**Scope:** two independent questions — (1) which of the schema's statistical
constructs should be bound to [STATO](https://obofoundry.org/ontology/stato.html)
terms, and (2) whether other LinkML machinery would express these data more
idiomatically.

Every STATO/OBI/IAO identifier below was resolved and label-checked against the
authoritative ontology before being written down:

```bash
uv run runoak -i sqlite:obo:stato info STATO:0000227 -O obo
```

STATO release used: the `sqlite:obo:stato` build current on 2026-08-01 (735
`STATO:` terms plus imported OBI/IAO/BFO terms). Nothing here is quoted from
memory; terms reported as **gaps** were confirmed absent by exhaustive search of
the term list, not by failing to find them in one query.

---

## Part 1 — Suggested STATO mappings

### 1.0 Mechanics first: `meaning` vs `*_mappings`

LinkML gives four distinct places to attach an ontology term, and they are not
interchangeable:

| Construct | Meaning | Validated in dismech? |
|---|---|---|
| `permissible_values.<PV>.meaning` | This PV **is** that class | Yes — `just validate-terms-schema` resolves the CURIE and compares the ontology's canonical label against the PV's `title`/`description`/aliases/name |
| `permissible_values.<PV>.broad_mappings` / `close_mappings` / `narrow_mappings` / `related_mappings` | Weaker SKOS-style relation | No — not currently checked by `linkml-term-validator` |
| `enums.<E>.enum_uri` | The enum as a whole corresponds to an ontology class/value set | No |
| `classes.<C>.class_uri` | Instances of this class are instances of that ontology class | No |

All four round-trip correctly through the installed `linkml-runtime` (verified
with `SchemaView`), so nothing below requires a LinkML upgrade.

Two practical consequences:

1. **Use `meaning:` only for genuine equivalence.** Roughly half of the
   distribution families have no STATO term at all. Asserting `meaning:` on a
   near-miss would be exactly the kind of "fabricated identity" the dismech
   term-validation stack exists to prevent. Near-misses go in
   `broad_mappings` / `close_mappings`, which record the relationship honestly
   and can still be consumed by an alignment tool.
2. **Adding `meaning:` obliges a `title:`.** The validator builds the accepted
   alias set from the PV name, `title`, `description`, `aliases`, and label-ish
   annotations, normalizes (lowercase, punctuation stripped), and requires the
   ontology label to be in that set. `NEGATIVE_BINOMIAL` normalizes to
   `negative binomial`, but the STATO label is `negative binomial distribution`
   — so each mapped PV needs `title: negative binomial distribution` (or an
   equivalent alias) or the check fails. This is a feature: it forces the
   curator to look at the label they are claiming to match.

**Prerequisite (one line):** STATO is not currently a configured prefix, so any
`meaning:` added today would be skipped with an `Unconfigured prefix` INFO
rather than checked. Add to `conf/oak_config.yaml`:

```yaml
  # Statistics ontology (distribution families, estimators, intervals)
  STATO: sqlite:obo:stato
```

and to the schema's `prefixes:` block:

```yaml
  STATO: http://purl.obolibrary.org/obo/STATO_
  IAO: http://purl.obolibrary.org/obo/IAO_
  OBI: http://purl.obolibrary.org/obo/OBI_
```

The `sqlite:obo:stato` adapter downloads a ~1.8 MB database and resolves
offline thereafter, so this adds no meaningful CI cost. `OBI` is already
declared in `dismech.yaml`.

---

### 1.1 `DistributionFamilyEnum` — the headline case

This is where STATO pays off most: 14 of 27 values map exactly.

| PV | Predicate | Term | Label |
|---|---|---|---|
| `BERNOULLI` | `meaning` | STATO:0000262 | Bernoulli distribution |
| `BINOMIAL` | `meaning` | STATO:0000276 | binomial distribution |
| `BETA` | `meaning` | STATO:0000177 | beta distribution |
| `MULTINOMIAL` | `meaning` | STATO:0000103 | multinomial distribution |
| `NORMAL` | `meaning` | STATO:0000227 | normal distribution |
| `LOGNORMAL` | `meaning` | STATO:0000438 | log normal distribution |
| `GAMMA` | `meaning` | STATO:0000268 | Gamma distribution |
| `EXPONENTIAL` | `meaning` | STATO:0000160 | exponential distribution |
| `WEIBULL` | `meaning` | STATO:0000501 | Weibull probability distribution |
| `POISSON` | `meaning` | STATO:0000051 | Poisson distribution |
| `NEGATIVE_BINOMIAL` | `meaning` | STATO:0000283 | negative binomial distribution |
| `STUDENT_T` | `meaning` | STATO:0000059 | Student's t distribution |
| `MIXTURE` | `meaning` | STATO:0000334 | mixture distribution |
| `EMPIRICAL` | `meaning` | STATO:0000330 | empirical distribution |
| `KERNEL_DENSITY` | `meaning` | STATO:0000332 | smooth kernel distribution |

STATO's definition of `smooth kernel distribution` ("estimated using a smooth
kernel function… the kernel density estimator is the estimated probability
density function") is exactly `KERNEL_DENSITY`, so this one is a true `meaning`
despite the label divergence — give it `title: smooth kernel distribution` and
keep `KERNEL_DENSITY` as the PV name.

Non-exact but usefully anchored:

| PV | Predicate | Term | Rationale |
|---|---|---|---|
| `CATEGORICAL` | `broad_mappings` | STATO:0000103 multinomial distribution | Categorical is multinomial at n=1; STATO has no separate class |
| `KAPLAN_MEIER` | `close_mappings` | STATO:0000335 survival distribution | STATO defines it as "estimated empirically from a censored lifetime data", i.e. the KM object; `related_mappings: OBI:0000889` (survival curve) for the curve itself |
| `NONPARAMETRIC_QUANTILE` | `broad_mappings` | STATO:0000321 non-parametric distribution | |
| `ZERO_INFLATED_POISSON`, `ZERO_INFLATED_NEGATIVE_BINOMIAL` | `broad_mappings` | STATO:0000334 mixture distribution | Both are literally two-component mixtures — a defensible parent, not a fudge |
| `UNIFORM` | `broad_mappings` | STATO:0000067 continuous probability distribution | |
| `MULTIVARIATE_NORMAL`, `LOGISTIC_NORMAL`, `DIRICHLET` | `broad_mappings` | STATO:0000538 continuous multivariate probability distribution | |
| `DIRICHLET_MULTINOMIAL`, `BETA_BINOMIAL` | `broad_mappings` | STATO:0000539 discrete multivariate probability distribution / STATO:0000117 discrete probability distribution | |
| `OTHER` | `broad_mappings` | STATO:0000225 probability distribution | |

Enum-level: `enum_uri: STATO:0000225` (probability distribution).

**Genuine STATO gaps worth reporting upstream** (these are mainstream families,
not exotica — the compositional ones are precisely what the CHARMPheno layer
needs): Dirichlet, logistic-normal, multivariate normal, uniform, categorical
(as distinct from multinomial), beta-binomial, Dirichlet-multinomial,
zero-inflated Poisson / negative binomial. STATO already carries the shape /
scale / location parameter classes (STATO:0000436 / STATO:0000435 /
STATO:0000500), so new families would slot in cleanly. This is a small, tractable
PR to [ISA-tools/stato](https://github.com/ISA-tools/stato), and dismech is a
credible requester.

---

### 1.2 `DistributionEstimate` / `DistributionParameter` — class and slot bindings

| Element | Predicate | Term | Label |
|---|---|---|---|
| class `DistributionEstimate` | `class_uri` | STATO:0000225 | probability distribution |
| class `DistributionParameter` | `class_uri` | STATO:0000742 | probability distribution parameter |
| slot `parameter_name` where the parameter is a shape/scale/location | `related_mappings` | STATO:0000436 / STATO:0000435 / STATO:0000500 | probability distribution shape / scale / location parameter |
| class `Quantile` | `class_uri` | STATO:0000291 | quantile |
| class `TimeToEventEstimate` | `class_uri` | STATO:0000335 | survival distribution |
| class `SurvivalPoint` | `related_mappings` | OBI:0000889 | survival curve |
| class `MixtureComponent` | `related_mappings` | STATO:0000334 | mixture distribution |
| class `LatentPhenotype` | `class_uri` | STATO:0000741 | statistical model component |
| class `LatentPhenotypeModel` | `class_uri` | STATO:0000107 | statistical model (STATO:0000530 `Bayesian model` for the Bayesian fits) |
| class `CohortDescriptor` | `class_uri` | STATO:0000193 | study group population |
| class `Stratum` | `class_uri` | STATO:0000265 | factor level |
| class `ComparisonEstimate` | `class_uri` | STATO:0000085 | effect size estimate |
| class `CovariateEffect` | `class_uri` | STATO:0000144 | model parameter estimate |
| class `DataItem` | `class_uri` | IAO:0000027 | data item |
| class `Document` | `class_uri` | IAO:0000310 | document |

`CohortDescriptor` deserves a note: STATO:0000203 `cohort` is defined as a study
group population *with a longitudinal design*, which is not true of every record
this class will carry (case series, cross-sectional EHR pulls). Bind the class to
the parent STATO:0000193 `study group population` and add STATO:0000203 as a
`close_mappings`; or, better, let `data_source_type` carry the design distinction
(see §2.9).

`Stratum` → STATO:0000265 `factor level` is a better fit than anything in the
sampling branch, and it comes with STATO:0000258 `variable` for the `variable`
slot — the pair is exactly the schema's `variable` / `stratum_value` structure.

---

### 1.3 `EstimationFrameworkEnum`

| PV | Predicate | Term | Label |
|---|---|---|---|
| `MAXIMUM_LIKELIHOOD` | `meaning` | STATO:0000428 | maximum likelihood estimation |
| `BAYESIAN_POSTERIOR` | `meaning` | STATO:0000706 | Bayesian inference (`related_mappings: STATO:0000532` posterior probability distribution) |
| `BOOTSTRAP` | `close_mappings` | STATO:0000548 | sampling distribution estimation by bootstrapping |
| `META_ANALYTIC_POOLING` | `close_mappings` | STATO:0000155 | meta analysis |
| `MCMC_POSTERIOR` | `narrow_mappings` | STATO:0000536 | Gibbs sampling (STATO has no MCMC parent) |
| `EMPIRICAL_TABULATION` | `related_mappings` | STATO:0000330 | empirical distribution |
| `FREQUENTIST_POINT` | `related_mappings` | STATO:0000599 | point estimate |
| `OTHER` | `broad_mappings` | STATO:0000119 | model parameter estimation |

Enum-level: `enum_uri: STATO:0000119` (model parameter estimation).

**Gaps:** MCMC (as a parent of Gibbs), variational inference, Laplace
approximation, expectation-maximization, expert elicitation. The first three
matter here because the schema's own documentation turns on them — the whole
point of `VARIATIONAL_POSTERIOR` and `LAPLACE_APPROXIMATION` is that their
intervals are too narrow, and there is no term to hang that on. STATO does carry
STATO:0000427 `restricted maximum likelihood estimation`, worth adding as a PV
if REML fits ever appear.

---

### 1.4 `PointEstimateTypeEnum` and `DistributionSummary`

| Element | Predicate | Term | Label |
|---|---|---|---|
| slot `point_estimate` | `related_mappings` | STATO:0000599 | point estimate |
| PV `MODE` | `meaning` | STATO:0000033 | mode |
| PV `PROPORTION` | `meaning` | STATO:0000607 | proportion |
| PV `MEAN` | `close_mappings` | STATO:0000401 / STATO:0000402 / STATO:0000692 | sample mean / population mean / probability distribution mean |
| PV `RATE` | `close_mappings` | STATO:0000673 | event frequency rate (`narrow_mappings: STATO:0000670` incidence rate) |
| slot `standard_deviation` | `related_mappings` | STATO:0000237 | standard deviation |
| slot `variance` | `related_mappings` | STATO:0000113 | variance |
| slot `skewness` | `related_mappings` | STATO:0000068 | skewness |
| slot `iqr_lower` / `iqr_upper` | `related_mappings` | STATO:0000167 / STATO:0000170 | first quartile / third quartile |
| slot `standard_error` | `related_mappings` | STATO:0000562 | standard error of estimate |
| slot `p_value` | `related_mappings` | STATO:0000700 | p-value |
| slot `count` | `related_mappings` | STATO:0000047 | count |
| slot `n_individuals` | `related_mappings` | STATO:0000088 | study group population size |
| slot `quantile` | `related_mappings` | STATO:0000291 | quantile |

Three findings here are worth surfacing rather than burying in a table:

1. **STATO has no `median` class.** It has `mode`, `sample mean`, `population
   mean`, `geometric mean`, `harmonic mean`, `trimmed mean`, `quadratic mean`,
   `median difference`, `median time-to-event`, and OBI:0200119 `median
   calculation` (a process) — but no plain median datum. `MEDIAN` and the
   `median` slot are therefore unmappable today. That is a surprising hole and
   the single most valuable thing to report upstream.
2. **`MEAN` is three different things** depending on whether the record is an
   empirical summary (STATO:0000401), a population parameter (STATO:0000402), or
   a fitted distribution's mean (STATO:0000692). The enum currently cannot say
   which. `POSTERIOR_MEAN` and `MAP` make the same conflation visible from the
   other direction. This is an argument for splitting "which functional" from
   "of what object" — see §2.6.
3. **`fdr` has no term.** OBI has OBI:0001265 `FWER adjusted p-value` and
   OBI:0200163 `false discovery rate correction method` (a method, not a value),
   but no "FDR-adjusted p-value" datum. Model it as a `related_mappings` to
   OBI:0200163 and note the gap.

Also unmapped and probably worth adding as PVs, since STATO already covers them:
`kurtosis` (STATO:0000178), and for `ReliabilityReadout`, sensitivity/specificity
(STATO:0000233 `true positive rate`, STATO:0000134 `true negative rate`),
`precision` (STATO:0000416), and Matthews correlation (STATO:0000524).

---

### 1.5 `IntervalTypeEnum`

| PV | Predicate | Term | Label |
|---|---|---|---|
| `CONFIDENCE` | `meaning` | STATO:0000196 | confidence interval |
| `RANGE` | `meaning` | STATO:0000035 | range |
| `IQR` | `meaning` | STATO:0000164 | inter quartile range |
| `CREDIBLE_HPD` | `close_mappings` | STATO:0000455 | credible interval |
| `CREDIBLE_EQUAL_TAILED` | `related_mappings` | STATO:0000455 | credible interval |
| — | enum-level `enum_uri` | STATO:0000600 | interval estimate |
| slot `interval_level` | `close_mappings` | STATO:0000561 | confidence level |

**A real ontology defect to report:** STATO:0000455 `credible interval` is
*defined* as the highest-posterior-density region ("such that the density at any
point inside the interval is greater than the density at any point outside…
which is also often known as the highest posterior density region"). That
definition excludes equal-tailed credible intervals, which are the more common
reporting convention. So STATO's single term is really `CREDIBLE_HPD`, and
`CREDIBLE_EQUAL_TAILED` has nowhere to go. The schema's own rationale — "a
confidence interval and a credible interval are not interchangeable and must not
be silently relabelled on import" — applies one level down, and the PR is right
to keep the two PVs distinct. Worth an upstream issue asking STATO to loosen the
`credible interval` definition and add equal-tailed / HPD children.

**Gaps:** prediction interval, tolerance interval. Both are standard; neither
exists in STATO.

**A modelling note the mappings expose:** the generic bound slots
`interval_lower` / `interval_upper` have no STATO term, because STATO's
STATO:0000315 / STATO:0000314 are `lower/upper confidence limit` — frequentist-
specific. That is a hint that the bound pair is only interpretable together with
`interval_type`, which the schema knows (it says so in the `DistributionSummary`
docstring) but does not enforce. See §2.4 and §2.7.

---

### 1.6 `ReadoutMetricEnum` and `FitStatistic`

| PV | Predicate | Term | Label |
|---|---|---|---|
| `AUROC` | `meaning` | STATO:0000608 | area under the receiver operator characteristic curve |
| `AUPRC` | `meaning` | STATO:0000691 | area under the precision-recall curve |
| `F1` | `meaning` | STATO:0000628 | F1 score |
| `ACCURACY` | `meaning` | STATO:0000415 | accuracy |
| `R2` | `meaning` | STATO:0000564 | coefficient of determination |
| `CALIBRATION_SLOPE` | `meaning` | STATO:0000687 | calibration slope |
| `AVERAGE_PRECISION` | `related_mappings` | STATO:0000691 | (AP is the estimator of AUPRC) |
| `CONCORDANCE_INDEX` | `related_mappings` | STATO:0000608 | (the c-index generalizes AUROC to censored data) |
| `PREDICTIVE_GAIN` | `related_mappings` | STATO:0000550 | log likelihood |

**Gaps:** balanced accuracy, Brier score, concordance index, perplexity, NPMI
topic coherence, and the two CHARMPheno-specific readouts (`PAIR_COVERAGE`,
`PREDICTIVE_GAIN`). The last two are legitimately project-specific and belong in
`model_properties`-land conceptually — but the first four are general and worth
requesting.

`FitStatistic.statistic_name` is currently free text, and its own docstring
lists "AIC, WAIC, KS D, chi-square" — every one of which except WAIC has a STATO
term. **Recommendation: promote it to an enum** with `meaning`s:

| PV | Term | Label |
|---|---|---|
| `AIC` | STATO:0000325 | Akaike information criterion |
| `AICC` | STATO:0000326 | corrected Akaike information criterion |
| `BIC` | STATO:0000327 | Bayesian information criterion |
| `DIC` | STATO:0000378 | deviance information criterion |
| `DEVIANCE` | STATO:0000377 | deviance |
| `LOG_LIKELIHOOD` | STATO:0000550 | log likelihood |
| `LIKELIHOOD_RATIO` | STATO:0000409 | likelihood ratio |
| `KOLMOGOROV_SMIRNOV` | STATO:0000083 | Kolmogorov-Smirnov test |
| `CHI_SQUARE_GOODNESS_OF_FIT` | STATO:0000309 | Pearson's Chi square test of goodness of fit |
| `HOSMER_LEMESHOW` | STATO:0000653 | Hosmer-Lemeshow goodness-of-fit test |

with `OTHER` + the existing free text for WAIC/LOO. This turns an unqueryable
string into a filterable, ontology-anchored field for ~20 lines of schema.

The same argument applies with even more force to
**`ComparisonEstimate.effect_measure`**, whose docstring names "risk ratio, mean
difference, standardized mean difference" — all present in STATO:

| PV | Term | Label |
|---|---|---|
| `RELATIVE_RISK` | STATO:0000245 | relative risk |
| `ODDS_RATIO` | STATO:0000182 | odds ratio |
| `HAZARD_RATIO` | STATO:0000677 | hazard ratio |
| `MEAN_DIFFERENCE` | STATO:0000457 | mean difference |
| `MEDIAN_DIFFERENCE` | STATO:0000617 | median difference |
| `STANDARDIZED_MEAN_DIFFERENCE` | STATO:0000100 | standardized mean difference |
| `INCIDENCE_RATE_RATIO` | STATO:0000680 | incidence rate ratio |
| `PREVALENCE_RATIO` | STATO:0000678 | prevalence ratio |

A free-text `effect_measure` is the field most likely to accumulate "RR", "rr",
"risk ratio", "relative risk" as four spellings of one thing — and the
comparison is the number a curator is most likely to import.

---

### 1.7 `DistributionMeasureEnum` and `MatrixKindEnum` — where STATO does *not* help

`DistributionMeasureEnum` is mostly clinical-epidemiological rather than
statistical, and only partially anchored:

| PV | Predicate | Term |
|---|---|---|
| `PHENOTYPE_PROPORTION` | `close_mappings` | STATO:0000412 prevalence (`broad_mappings: STATO:0000607` proportion) |
| `EVENT_RATE` | `close_mappings` | STATO:0000673 event frequency rate |
| `EVENT_COUNT` | `broad_mappings` | STATO:0000047 count |
| `TIME_TO_EVENT` | `related_mappings` | STATO:0000659 median time-to-event, OBI:0200083 survival analysis objective |
| `LABORATORY_VALUE` | `broad_mappings` | IAO:0000109 measurement datum |

`PENETRANCE`, `AGE_AT_ONSET`, `AGE_AT_DIAGNOSIS`, `AGE_AT_DEATH`, `DURATION`,
`SEVERITY_GRADE`, `TREATMENT_RESPONSE`, `COMORBIDITY_CO_OCCURRENCE`,
`LATENT_PHENOTYPE_WEIGHT`, and `CODE_PROBABILITY` have no STATO analogue and
should not be forced into one — they are disease-domain concepts, and the right
homes are HPO onset terms, GENO, or nothing. Leave them unmapped; an unmapped PV
with a good description is better than a wrong `meaning`.

`MatrixKindEnum` is similar: only `COVARIANCE` maps (STATO:0000525 `covariance
matrix`). STATO has `correlation coefficient` (STATO:0000142) but no correlation
*matrix*; nothing for precision, loading, transition, or concentration matrices.

One unexploited resource is worth flagging for later: STATO carries a whole
`covariance structure` branch (STATO:0000346) with ~25 children — unstructured
(STATO:0000405), compound symmetry, first-order autoregressive, Toeplitz,
factor-analytic, and so on. If the logistic-normal Σ ever needs its *structure*
described rather than just its entries, that vocabulary already exists and is
exactly the right granularity.

---

### 1.8 Summary of upstream STATO requests

Worth one issue on `ISA-tools/stato`, listed by how load-bearing they are here:

1. `median` (a datum, not `median calculation`) — the most surprising gap.
2. Loosen `credible interval` (STATO:0000455), which is currently defined as
   HPD only; add equal-tailed and HPD children.
3. Compositional / multivariate families: Dirichlet, logistic-normal,
   multivariate normal, categorical, Dirichlet-multinomial, beta-binomial.
4. Zero-inflated Poisson / negative binomial; uniform.
5. Inference frameworks: MCMC (as a parent for Gibbs), variational inference,
   Laplace approximation, expectation-maximization.
6. Prediction interval; tolerance interval.
7. Metrics: balanced accuracy, Brier score, concordance index, FDR-adjusted
   p-value (the OBI:0001265 sibling).

---

## Part 2 — More idiomatic LinkML

The schema is competently written — flat global `slots:`, explicit ranges,
`inlined_as_list`, `tree_root`, enum-backed everything, long rationale prose in
`description`. What it does *not* yet use is most of the LinkML machinery that
would let the schema state its own invariants instead of delegating them to
`src/dismech/phenotype_distribution.py`. Ten suggestions, roughly in order of
value-to-effort.

### 2.1 Bind terms with `bindings` / `binds_value_of`, as the main schema already does

This is the biggest divergence from house style. `dismech.yaml` binds every
descriptor's term through a dynamic enum plus a binding:

```yaml
  PhenotypeDescriptor:
    slot_usage:
      term:
        bindings:
          - binds_value_of: id
            range: PhenotypeTerm       # reachable_from HP:0000118 / MONDO:0000001
            obligation_level: REQUIRED
```

`phenotype_distribution.yaml` instead defines its own `Term` class with two
plain strings:

```yaml
  Term:
    slots: [term_id, term_label]
```

Nothing constrains `term_id` to HPO for `phenotype_term`, to MONDO for
`disease_term`, or to LOINC for `loinc_term`, and `just validate-terms` has no
hook. Three consequences:

- The `term_id`/`term_label` naming diverges from the main schema's `id`/`label`,
  so a record's phenotype term is not shaped like a dismech phenotype term —
  which undercuts the stated convergence goal.
- The anti-hallucination guarantee that the rest of dismech relies on does not
  extend to this schema.
- Reviewers reading a `PhenotypeContext` cannot tell that `phenotype_term` must
  be HPO except from prose.

**Recommendation:** reuse the main schema's `Term`/descriptor shape and its
`*Term` dynamic enums via `imports:` (see §2.10); failing that, at minimum add
`bindings` with `reachable_from` enums local to this schema.

### 2.2 Collapse the repeated interval quartet into a mixin

`interval_lower`, `interval_upper`, `interval_type`, `interval_level` appear
verbatim in **seven** classes (`DistributionSummary`, `DistributionParameter`,
`TimeToEventEstimate`, `ComparisonEstimate`, `CovariateEffect`,
`ReliabilityReadout`, and partially in `Quantile`, `DistributionBin`,
`SurvivalPoint`). LinkML mixins exist for exactly this:

```yaml
classes:
  IntervalEstimate:
    mixin: true
    class_uri: STATO:0000600      # interval estimate
    description: >-
      An interval around an estimate. `interval_type` and `interval_level` are
      not optional in practice: an interval whose kind and coverage are unstated
      cannot be compared with another one.
    slots: [interval_lower, interval_upper, interval_type, interval_level]

  DistributionSummary:
    mixins: [IntervalEstimate]
    slots: [point_estimate, point_estimate_type, ...]
```

Benefits beyond brevity: the STATO binding lives in one place; a rule about
type/level co-occurrence (§2.7) is written once; and a consumer can ask
"everything that carries an interval" via `SchemaView`. The same treatment suits
an `Annotatable`-style mixin for the `notes` / `description` pair that appears
on ~20 classes, and an `Attested` mixin for `identity_attestation`.

### 2.3 Define `types:`, not repeated min/max constraints

`minimum_value: 0.0` + `maximum_value: 1.0` is repeated on `proportion`,
`interval_level`, `probability`, `weight`, `corpus_prevalence`,
`reliability_score`, `p_value`, `fdr`, `quantile`. That is nine chances to
forget one:

```yaml
types:
  Probability:
    typeof: float
    minimum_value: 0.0
    maximum_value: 1.0
    description: A probability or proportion on the unit interval.
  NonNegativeCount:
    typeof: integer
    minimum_value: 0
```

then `range: Probability` / `range: NonNegativeCount` throughout. This also gives
one place to attach `STATO:0000607` for the proportion-typed values.

### 2.4 Use LinkML's array model for `MatrixParameter`

`MatrixParameter` hand-rolls `n_rows` / `n_columns` / row-major `values` /
`row_labels` / `column_labels`, and the Python lint then checks that
`len(values) == n_rows * n_columns`. LinkML has a native N-dimensional array
model (`linkml:elements`, `array`, `dimensions`, `array_linearization_order`,
with `RowOrderedArray` / `ColumnOrderedArray` for exactly the row-major
convention). Roughly:

```yaml
  MatrixParameter:
    implements: [linkml:RowOrderedArray]
    attributes:
      values:
        implements: [linkml:elements]
        array:
          exact_number_dimensions: 2
          dimensions:
            - alias: row
            - alias: column
```

This makes the linearization order a machine-readable declaration rather than a
sentence in `values`'s description ("in row-major order"), gets the cardinality
check for free in array-aware tooling, and generalizes if a 3-D object ever
appears. **Caveat:** the array model is newer and less uniformly supported by
generators than the rest of the metamodel, and the current shape is perfectly
readable YAML. If it is adopted, keep the Python cardinality check as a belt-and-
braces measure rather than deleting it.

### 2.5 `attributes:` for class-local slots; reserve global `slots:` for shared ones

Every slot is currently global, which forces genuinely different concepts to
share a name. `value` means "scalar parameter value" in `DistributionParameter`,
"the quantile's value" in `Quantile`, and "the fit statistic's value" in
`FitStatistic`. Likewise `name`, `count`, `weight`, `component`, `metric`,
`description`, `id`, `unit`.

This is not merely stylistic — it is what makes §1.4's slot-level mappings
impossible to state cleanly. `value` cannot carry a STATO mapping because it has
three meanings. Move single-use slots into `attributes:` on their owning class,
and keep the global `slots:` block for the genuinely reusable, semantically
stable ones (`interval_*`, `p_value`, `n_observations`, `notes`, `description`).
The main dismech schema mixes both idioms already, so this is not a new
convention.

### 2.6 Consider `designates_type` polymorphism for distribution families

The schema says "Determines which `parameters` are expected" about `family`, and
then cannot check it — a `BETA` record with a `lambda` parameter validates fine.
LinkML's answer is a type designator:

```yaml
  DistributionEstimate:
    abstract: true
    slots: [family, estimation_framework, summary, ...]
    slot_usage:
      family:
        designates_type: true

  BetaEstimate:
    is_a: DistributionEstimate
    class_uri: STATO:0000177
    attributes:
      alpha: {range: float, required: true, minimum_value: 0}
      beta:  {range: float, required: true, minimum_value: 0}
```

This gives per-family required parameters, per-family `class_uri` (so §1.1's
mappings land on classes rather than PVs), and makes `parameterization_note`
unnecessary for the families that get subclasses.

**But it runs directly against the PR's stated design principle** — "the common
denominator, not one model's output" — and a 27-class hierarchy is a large
maintenance surface for a schema whose whole argument is that model shapes churn.
My recommendation is the middle path: **keep the enum + generic
`DistributionParameter`, and add `rules:` (§2.7) for the six families that
actually appear in curation** (Beta, lognormal, negative binomial, normal,
Dirichlet, logistic-normal). That buys most of the validation with none of the
hierarchy. Mention `designates_type` in the schema's design notes so the option
is on the record rather than rediscovered later.

### 2.7 Move part of the Python lint into `rules:` / `any_of` / `value_presence`

`src/dismech/phenotype_distribution.py` lints seven invariants. Three are
natively expressible:

**"Every record needs either a `phenotype` or a `latent_phenotype`"** — currently
prose in a docstring:

```yaml
  PhenotypeDistributionRecord:
    any_of:
      - slot_conditions:
          phenotype: {value_presence: PRESENT}
      - slot_conditions:
          latent_phenotype: {value_presence: PRESENT}
```

**"A Bayesian framework should not report a confidence interval"**:

```yaml
    rules:
      - preconditions:
          slot_conditions:
            estimation_framework:
              any_of:
                - equals_string: BAYESIAN_POSTERIOR
                - equals_string: MCMC_POSTERIOR
                - equals_string: VARIATIONAL_POSTERIOR
        postconditions:
          slot_conditions:
            interval_type:
              any_of:
                - equals_string: CREDIBLE_EQUAL_TAILED
                - equals_string: CREDIBLE_HPD
        description: >-
          A Bayesian fit reports a credible interval, not a confidence interval.
```

**"A Beta estimate carries alpha and beta"** — the §2.6 middle path, as a rule
over `parameters[*].parameter_name`.

Also worth adding: `APPROXIMATE_POSTERIOR` in `bias_risks` should arguably be
*required* when `estimation_framework` is `VARIATIONAL_POSTERIOR` or
`LAPLACE_APPROXIMATION` — the schema already says so in prose ("Uncertainty is
usually understated"), and a rule would make it true by construction rather than
by curator diligence.

**What must stay in Python** — worth stating explicitly so nobody tries: the
matrix cardinality check, "the interval brackets the point estimate", "the
implied frequency band is consistent with the point estimate", the
`target_entry` filesystem existence check, and the identity-attestation
arithmetic (`unique_person_count == row_count` iff `one_row_per_person`). LinkML
rules compare slots to *constants*, not to other slots, so cross-field numeric
comparison is out of scope. Roughly half the lint moves; the half that stays is
the half that most needs a test.

### 2.8 Make `record_id` a key, and derive `evidence_reference`

Two lint checks vanish with two metaslots:

```yaml
  record_id:
    key: true            # uniqueness within the collection, enforced by LinkML
```

and

```yaml
  evidence_reference:
    equals_expression: "'PHENODIST:' + {record_id}"
    pattern: "^PHENODIST:[A-Za-z0-9][A-Za-z0-9._-]*$"
```

`equals_expression` states the derivation the lint currently checks by hand ("an
`evidence_reference` disagreeing with its record"). Support for evaluating it is
not universal across generators, so keep the lint — but the schema then *says*
what the rule is instead of only the Python knowing.

While there: the two CURIE patterns (`record_id`, `evidence_reference`) share
structure and would be better as a `structured_pattern` with `settings:`, which
is how the pattern gets reused if a second bridge prefix is ever added.

### 2.9 Reuse existing vocabularies for the cohort/design axis

`DataSourceTypeEnum` and `AscertainmentEnum` are re-derivations of study-design
vocabulary that OBI and STATO already carry in part: OBI:0500000 `study design`,
STATO:0000089 `case-control study design`, STATO:0000203 `cohort`,
STATO:0000508 `stratified sampling`, STATO:0000503 `simple random sampling`,
STATO:0000096 `population stratification prior to sampling`. Coverage is
incomplete (nothing for EHR, claims, biobank, or newborn screening), so this is
not a replacement — but `CASE_SERIES`, `CLINICAL_TRIAL`, and
`SYSTEMATIC_REVIEW_META_ANALYSIS` should carry `meaning`s (STATO:0000155 for
the last), and `PROBAND_ASCERTAINED` / `POPULATION_BASED` deserve at least
`related_mappings`. This is the same "don't re-implement the ontology, point at
it" discipline the grouping design already applies to MONDO.

### 2.10 `imports:` rather than copy-plus-drift-test

The PR duplicates `Term`, `TermDescriptor`, `FrequencyClassEnum`,
`EvidenceDirectionEnum`, `Agent`, `Activity`, and `Document` from (or alongside)
`dismech.yaml`, and adds a test asserting `EvidenceDirectionEnum` has not
drifted from `EvidenceItemSupportEnum`. A test that enforces non-drift is a
workaround for the absence of an import.

The idiomatic fix is a shared module — `src/dismech/schema/dismech_common.yaml`
holding `Term`, the `*Term` dynamic enums, `FrequencyEnum`,
`EvidenceItemSupportEnum`, `Agent`, `Activity`, `Document` — imported by both
`dismech.yaml` and `phenotype_distribution.yaml`:

```yaml
imports:
  - linkml:types
  - dismech_common
```

Then drift is impossible by construction and the test can be deleted. This
directly answers the PR's review question 2 ("if #7439 lands in `dismech.yaml`
these should converge"): the convergence mechanism is an import, and doing it now
is cheaper than doing it after #7439 lands, because right now there is one copy
to reconcile rather than two.

The cost is real — extracting a common module touches `dismech.yaml`, which
everything depends on. If that is too much for this PR, the fallback is to
*generate* the duplicated fragment from `dismech.yaml` in a `just` target so the
copy is derived rather than maintained. But the import is the right end state,
and worth an issue if not this PR.

### 2.11 Smaller things

- **`subsets:`** — the schema has three fairly separable layers (distribution,
  model, SEPIO evidence). Declaring `subsets: {distribution_layer:, model_layer:,
  evidence_layer:}` and tagging elements with `in_subset:` makes the generated
  documentation navigable and gives the PR's review question 1 ("is the
  common-denominator cut in the right place?") a machine-readable answer: you can
  count what is in the model layer and watch whether it grows.
- **`unit`** — `unit` is a free-text string on six classes ("years, mg/dL,
  events/year"). LinkML has a `UnitOfMeasure` construct (`ucum_code`, `symbol`,
  `has_quantity_kind`); binding to UCUM would make `mg/dL` comparable across
  records, which matters for the `LABORATORY_VALUE` estimand specifically since
  those records are the ones most likely to be pooled.
- **`ModelProperty`** — the name/value escape hatch stringifies numbers
  ("Numbers are written out"). `dismech.yaml` already uses `class_uri:
  linkml:Any` for a typed-any slot; `property_value` could take that range and
  keep numbers numeric without giving up the escape hatch.
- **`title:` on permissible values** is applied inconsistently (present on
  `FrequencyClassEnum` and `EvidenceDirectionEnum`, absent almost everywhere
  else). Adding `meaning:` forces the issue for mapped PVs (§1.0), and doing it
  uniformly is worth the churn.

---

## Recommended sequencing

Nothing here needs to block #7612. Suggested split:

**In this PR (cheap, self-contained):**
- Add the `STATO`/`IAO` prefixes and the `conf/oak_config.yaml` adapter line.
- Add `meaning:` + `title:` for the 14 exact distribution families, the 6 exact
  metrics, the 3 exact interval types, and the 4 exact estimation frameworks
  (§1.1, §1.3, §1.5, §1.6) — this is the mapping payload, ~40 PVs, all verified.
- Add `class_uri` for the ~15 classes in §1.2.
- Promote `statistic_name` and `effect_measure` to STATO-mapped enums (§1.6) —
  the highest-value structural change and a small diff.

**Follow-up issues:**
- The `IntervalEstimate` mixin and custom `types:` (§2.2, §2.3) — mechanical.
- `bindings` for ontology terms (§2.1) and the shared-module import (§2.10) —
  these two are really one piece of work and the most important for convergence
  with `dismech.yaml` / #7439.
- The `rules:`/`any_of` subset of the lint (§2.7).
- One upstream STATO issue with the seven requests in §1.8.
