# Inheritance, subtypes, laboratory intervals, and occurrence

### Digenic / Oligogenic Inheritance (Multi-Locus)

Some disorders require variants at **two loci (digenic)** or a **few loci
(oligogenic/triallelic)** rather than a single Mendelian locus. Curate the
multi-locus mode of inheritance explicitly so it is machine-queryable — do not
leave it as free text.

**Where it goes:** add an `Inheritance` block (in the disease-level
`inheritance:` list, and/or on a `has_subtypes[]` entry when only one subtype is
multi-locus) with `inheritance_term` bound to the HPO mode-of-inheritance
subtree:

- `HP:0010984` **Digenic inheritance** (two loci both required)
- `HP:0010983` **Oligogenic inheritance** (triallelic / a few loci)
- `HP:0010982` **Polygenic inheritance** (many small-effect loci; use with
  `relationship_type: SUSCEPTIBILITY` gene typing)

Always **bind the `term:`** — an `inheritance_term` with only a `preferred_term`
and no `term:` is the common gap. The `Inheritance` class has no `genes` slot, so
name the contributing genes in the block `description`; put per-gene detail in
the `genetic:` section (use `relationship_type: MODIFIER` / `SUSCEPTIBILITY` /
`COOPERATING` for a contributing second locus) or, for a digenic subtype, in the
`has_subtypes[].genes` list.

**Evidence discipline:** the digenic/oligogenic claim gets its own PMID with an
exact-quote snippet (typically the double-heterozygote / joint-transmission /
epistasis sentence), separate from the general disease evidence.

**Exemplar:** `PRPH2-Related_Retinopathy` is the reference implementation — it
models digenicity both as an RP7-digenic subtype (listing PRPH2 + ROM1) and as a
top-level `Digenic inheritance` block bound to `HP:0010984`, citing the classic
double-heterozygote study (`PMID:8202715`). Other worked digenic/oligogenic
entries: `Alport_Syndrome`, `Usher_Syndrome`,
`Facioscapulohumeral_Muscular_Dystrophy` (FSHD2),
`MITF_Waardenburg_Tietz_Spectrum`, `Meckel_Syndrome`, `Hirschsprung_Disease`
(oligogenic RET-EDNRB), `GJB2-GJB6_Digenic_Nonsyndromic_Hearing_Loss`,
`Bardet-Biedl_Syndrome`, `Kallmann_Syndrome`. The
`Digenic_and_Oligogenic_Disorders` grouping collects them as an auditable union
(`grouping_basis: OTHER`, a `NECESSARY` `HAS_INHERITANCE` criterion).

### Subtype Naming Conventions

The `name` field on `Subtype` (in `has_subtypes`) serves as the **foreign key target** — other sections
(phenotypes, biochemical, genetic, prevalence, progression, histopathology) reference it via their
`subtype` field. A validation test (`check_subtype_foreign_keys`) enforces that all `subtype` values
match a defined `has_subtypes[].name`.

**Naming rules for `name`:**
- Keep names short and slug-friendly: `Type 1`, `MEN2A`, `Vascular EDS`, `FA-A`
- Avoid parenthetical qualifiers, long descriptions, or special characters
- Use `display_name` (optional) for verbose/human-readable labels when the `name` is too terse

**Example:**
```yaml
has_subtypes:
- name: Type 1
  display_name: Type 1 (Non-neuronopathic)
  description: Most common form, no CNS involvement...

phenotypes:
- name: Seizures
  subtype: Type 1    # references the short name
```

**When `display_name` is set**, renderers show it instead of `name`. When absent, `name` is displayed directly.

**A subtype list is a start, not an end state.** Only ~36% of declared
subtypes are ever referenced by a `subtype:` foreign key, and about a third
of the genes named in `has_subtypes[].genes` are not wired into the
pathograph at all (no pathophysiology node carries the gene, and no causal
`genetic:` entry links to one). When you declare a gene-specific subtype,
also (a) stratify at least the subtype-divergent phenotypes/genetic rows via
`subtype:`, and (b) make sure the gene reaches the pathograph — a `genes:`
descriptor on the relevant pathophysiology node is enough for
`dismech.graph` to auto-link it. Audit with:

```bash
just subtype-usage-audit                          # census + wiring summary
just subtype-usage-audit --format list --status ABSENT
just subtype-usage-audit kb/disorders/MyDisease.yaml --format list
```

See `docs/reports/subtype-field-usage-audit-2026-09-04.md` for the baseline
census and the two recurring failure shapes.

### Reference Ranges and Interpretation Bands

A `Biochemical` marker can carry clinical laboratory `reference_ranges`
(`ReferenceRange` class): a LOINC-coded normal interval (`lower_bound` /
`upper_bound` / `unit`) and a `population` stratifier. Omit a bound for
one-sided intervals. Attribute the interval with structured `evidence`
(the same `EvidenceItem` model used everywhere else — a citable PMID/DOI
with a verified snippet), **not** a free-text source string. When the
provenance is a lab manual that has no citable article (e.g., the Tietz
guide), put that attribution in `notes` rather than inventing a citation.

When a result is interpreted in graded categories rather than a single
normal interval (e.g., above one value is mild, above a higher value is
moderate, then severe), add `interpretation_bands` (`ReferenceRangeBand`).
Each band maps a value interval to a category and is rendered as a colored
pill on the disorder page:

- `name` (required): category label (e.g., "Normal", "Mild hypercalcemia").
- `lower_bound` / `upper_bound`: the band's half-open interval
  `[lower_bound, upper_bound)` — `lower_bound` inclusive, `upper_bound`
  exclusive — so adjacent bands sharing a boundary value partition cleanly
  (a result at the boundary falls in the upper band). Omit `lower_bound` for
  the open-below tier and `upper_bound` for the open-above tier.
- `abnormal_flag`: `NORMAL`, `LOW`, `HIGH`, `CRITICAL_LOW`, `CRITICAL_HIGH`
  (HL7 v2 / LOINC convention).
- `severity`: ordinal `MILD` / `MODERATE` / `SEVERE` when the category aligns
  with severity grading. Renderer colors bands by `severity` first, then
  `abnormal_flag`.
- `phenotype_term`: optional HP term an abnormal band maps to (LOINC2HPO style).
- `interpretation`: free-text clinical interpretation of results in the band.

```yaml
reference_ranges:
- loinc_term:
    id: LOINC:17861-6
    label: Calcium [Mass/volume] in Serum or Plasma
  lower_bound: 8.5
  upper_bound: 10.5
  unit: mg/dL
  population: adults
  evidence:
  - reference: PMID:26303319
    supports: SUPPORT
    snippet: "exact quote stating the interval"
    explanation: Source for the calcium reference interval.
  notes: "Or, for a non-citable lab-manual interval, record provenance here."
  interpretation_bands:
  - name: Normal
    lower_bound: 8.5
    upper_bound: 10.5
    unit: mg/dL
    abnormal_flag: NORMAL
  - name: Mild hypercalcemia
    lower_bound: 10.5
    upper_bound: 12.0
    unit: mg/dL
    abnormal_flag: HIGH
    severity: MILD
  - name: Severe hypercalcemia
    lower_bound: 14.0
    unit: mg/dL
    abnormal_flag: CRITICAL_HIGH
    severity: SEVERE
```

`reference_ranges` (empirical clinical intervals) are distinct from
`ModelVariableDescriptor` thresholds / `severity_scale` (computational-model
phenotype-activation points); use reference ranges for measured lab analytes.

The CKD-Mineral Bone Disorder entry is the worked example.

### Prevalence (disease occurrence)

Model disease occurrence with the **structured** `Prevalence` slots, not the
deprecated free-text `percentage` field (see design decision §8). Each prevalence
record should separate the four dimensions the old field conflated:

- `population` — cohort / geography only (e.g. `Worldwide`, `Ashkenazi Jewish
  population`). Do **not** put the measure type here.
- `measure_type` (`PrevalenceMeasureEnum`) — `POINT_PREVALENCE`, `BIRTH_PREVALENCE`,
  `LIFETIME_PREVALENCE`, `PERIOD_PREVALENCE`, `ANNUAL_INCIDENCE`, `CARRIER_FREQUENCY`,
  `CASES_IN_LITERATURE`, or `UNKNOWN`. Never compare a prevalence with an incidence.
- `prevalence_class` (`PrevalenceClassEnum`) — the coarse, always-fillable band.
  Numeric tiers are the Orphanet-aligned bands (`ABOVE_1_IN_1000`,
  `BAND_1_5_PER_10000`, `BAND_1_9_PER_100000`, `BAND_1_9_PER_1000000`,
  `BELOW_1_IN_1000000`, `NOT_YET_DOCUMENTED`). **A band reports magnitude only** —
  `measure_type` says what is being measured, and the band is meaningless without
  it. The qualitative tiers (`COMMON`, `RARE`, `ULTRA_RARE`) are the exception:
  they are defined by prevalence thresholds and presuppose no numeric estimate, so
  **never** use them with `measure_type: ANNUAL_INCIDENCE` or `CARRIER_FREQUENCY`,
  and not alongside a populated `rate_per_100000`. They are fine on the prevalence
  measures, on `CASES_IN_LITERATURE`, and on `UNKNOWN` (a source that says only
  "rare" without naming its measure). See design decision §8.
- `rate_per_100000` (+ `rate_low` / `rate_high` for ranges) — one normalized number
  in cases per 100,000 (`% × 1000`; `per million ÷ 10`; `1 in N → 100000/N`).
- `rate_denominator` (`RateDenominatorEnum`) — what the rate is a rate *of*:
  `POPULATION`, `LIVE_BIRTHS`, `PERSON_YEARS`, or `POPULATION_PER_YEAR`. Optional
  for the prevalence measures, which fall back to `POPULATION` (`LIVE_BIRTHS` for
  `BIRTH_PREVALENCE`). **Always set it on an `ANNUAL_INCIDENCE` record** — that
  measure has no fallback on purpose, because per-population-per-year and
  per-person-year are both common and not interchangeable.
- `notes` keeps the verbatim source phrasing; `evidence` is unchanged.

```yaml
prevalence:
- population: Worldwide
  measure_type: POINT_PREVALENCE
  prevalence_class: BAND_1_5_PER_10000
  rate_per_100000: 20.0
  notes: Orphanet worldwide point-prevalence class 1-5 / 10,000.
  evidence:
  - reference: ORPHA:558
    supports: SUPPORT
    snippet: "1-5 / 10 000 | Worldwide | Point prevalence | PMID:20301510"
    explanation: Orphanet epidemiology table.
```

**Incidence example** — note the explicit denominator, and that no qualitative
tier is used:

```yaml
prevalence:
- population: Olmsted County, Minnesota, 1990-2015
  measure_type: ANNUAL_INCIDENCE
  prevalence_class: BAND_1_9_PER_100000
  rate_per_100000: 1.2
  rate_denominator: PERSON_YEARS
  notes: 1.2 new cases per 100,000 person-years.
```

`scripts/migrate_prevalence.py` backfilled existing entries; do not populate
`percentage` on new records.

#### Per-gene case fractions (genetically heterogeneous diseases)

For a disease where multiple genes each explain some share of cases, record that
share with structured `Genetic.case_fractions` (multivalued `GeneCaseFraction`),
**not** the free-text `Genetic.frequency` field. This is the genetic-spectrum
analog of a `Prevalence` record and is distinct from population occurrence and
from allele frequency — the share is cohort/ancestry-dependent, so each estimate
carries its own `population` and `evidence`:

```yaml
genetic:
- name: BBS1
  gene_term:
    preferred_term: BBS1
    term:
      id: hgnc:966
      label: BBS1
  frequency: one of the most prevalent BBS genes   # coarse qualitative band (kept)
  case_fractions:
  - population: German BBS cohort
    case_fraction_percent: 24.6
    notes: Second most common gene in a contemporary German clinical series.
    evidence:
    - reference: PMID:35886001
      supports: SUPPORT
      evidence_source: HUMAN_CLINICAL
      snippet: "The most common associated genes were BBS10 (32.8%) and BBS1 (24.6%)"
      explanation: Quantifies the BBS1 share of cases in the German cohort.
```

Use `case_fraction_low`/`case_fraction_high` for ranges and `cohort_size` when the
proband count is reported. `Bardet-Biedl_Syndrome` (BBS1/BBS10) is the worked example.
