# Phenotype Profiles

A **phenotype profile** is what co-occurs in a disease cohort, exported from a
model fitted to structured EHR records: a label, and one weighted list of
clinical codes per domain. Profiles are curated as a separate artifact and cited
from a disease entry as evidence, the same way Orphanet or ClinGen records are.

Schema: [`src/dismech/schema/phenotype_distribution.yaml`](https://github.com/monarch-initiative/dismech/blob/main/src/dismech/schema/phenotype_distribution.yaml)
Tooling: `src/dismech/phenotype_distribution.py`
Worked example: `examples/phenotype_distributions/`
Curated sets: `kb/phenotype_distributions/` (created by the first curated set;
this directory does not exist yet)

## The shape

```
ProfileSet ──has──> Profile ──has──> CodeDistribution ──has──> WeightedCode
     │                                  (per domain,            (code + label
  disease                                with its                + weight
  (MONDO)                                vocabulary)             + qualifier?)
profile_source
 (provenance)
```

One set is about one disease, declared once at the top. Each profile under it is
one pattern.

The whole shape, at its smallest — this is
`examples/phenotype_distributions/minimal_asthma_illustrative.yaml`, with
invented weights:

```yaml
collection_id: EXAMPLE-MINIMAL-ASTHMA-001
provenance_tier: ILLUSTRATIVE
disease:
  disease_name: Asthma
  disease_term: {term_id: MONDO:0004979, term_label: asthma}
profile_source:
  resource: Illustrative example — not a real model run
  method: COMPUTATIONAL_INFERENCE
  weight_basis: Fraction of the whole fitted corpus.
profiles:
- profile_id: EXAMPLE-ASTHMA-EXACERBATION-001
  profile_label: Frequent exacerbation with oral corticosteroid use
  profile_weight: 0.02
  code_distributions:
  - clinical_domain: CONDITION
    code_vocabulary: OMOP_CONCEPT_ID
    truncated: true
    weighted_codes:
    - {code: '317009', code_label: Asthma, code_weight: 0.31}
    - {code: '255573', code_label: Chronic obstructive lung disease, code_weight: 0.14}
    - {code: '4145356', code_label: Wheezing, code_weight: 0.10}
```

Everything below is why each of those fields is shaped the way it is. The same
shape filled in from a real model export — with the seventeen-digit weights,
pinned provenance and caveats that real numbers bring — is
`charmpheno_population_eds.yaml`, discussed under
[the worked examples](#the-worked-examples).

## Design decisions

The shape follows the proposal from the author of the models that produce this
data ([CHARMPheno](https://github.com/oneilsh/CHARMPheno)). Several of the
decisions below are recorded because a larger alternative was tried first and
did not survive review.

### A disease page, not a model report

An earlier draft grew a full model layer — component counts, inference methods,
hyperparameters, per-domain reliability, cohort arms and their denominators.
That was the wrong altitude twice over. Per-domain weights, reliability and
precision/recall are **model evaluation**, not disease-page content; and they
are the fastest-moving part of the pipeline, so a curation schema encoding them
would need revising every time the models moved.

What a page needs is a label and weighted codes. Everything else lives in
`profile_source`, including an open `profile_metadata` key/value map, so the
model layer can be reshaped freely without touching the profile contract.

### One set, one MONDO term

`disease` sits on the set, not on each profile: every profile in a fit is about
the same cohort, so repeating the term per profile only creates a way for them
to disagree. Nesting and overlap between cohorts is expressed by MONDO's own
subclass tree, which dismech already renders, so this schema ships **no** cohort,
arm, or grouping vocabulary of its own.

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
"prevalence". This schema never does. In a disease knowledge base `prevalence`
means a count of patients carrying a label over a stated denominator of patients
at risk, and dismech has a `prevalence[]` block that means exactly that. A
profile's share is a fraction of fitted mass; the two are not convertible, and
rendering one beside the other under the same word invites a comparison that does
not hold. The slots are `profile_weight` and `code_weight`.

Because denominator hygiene is the whole reason for the different name,
`profile_source.weight_basis` states what the weights are a fraction of — the
whole analysed corpus, one disease arm, one cohort — and the lint requires it
wherever any `profile_weight` appears. Two weights are comparable only when their
sets declare the same denominator; without it, a corpus-wide weight and an
arm-wide weight differ by orders of magnitude and look identical.

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
different force.

## Citing a profile from a dismech entry

A profile set names no dismech entry. Nothing else in this repo points that way
— ORPHA, ClinGen, ICEES and NCIT records are cited *by* an entry and know nothing
about it — and a source-side pointer would be a second place for the same fact
to be wrong. The association a set does need is the MONDO term it already carries.

`just phenodist-rebuild` renders each curated profile to
`references_cache/PHENODIST_<profile_id>.md`, a deterministic line-oriented file
in the same format as the Orphanet, ClinGen, and ICEES structured sources. The
disease entry cites it like any other structured source, quoting a row:

```yaml
evidence:
- reference: PHENODIST:CHARMPHENO-EDS-DYSAUTONOMIA-001
  supports: SUPPORT
  evidence_source: OTHER
  snippet: "| 4159659 | Postural orthostatic tachycardia syndrome | 0.11381 |"
  explanation: POTS is among the highest-weighted codes in the profile.
```

The column order of those rows is part of the cache contract and is pinned by a
test: reordering it would silently invalidate every snippet already quoted from
it. As with every other file in `references_cache/`, these are generated —
**never hand-write or hand-edit one**.

## Provenance tier

Every set must declare `provenance_tier`, so "these numbers are illustrative" is
a machine-readable fact rather than a sentence in a description that tooling
cannot read:

| Tier | Meaning |
|---|---|
| `CURATED` | Human-curated from literature or a named source; citable from a kb entry |
| `TOOL_EXPORTED` | Transcribed from a model or pipeline export; the numbers are real, the mapping to disease concepts is curator judgement |
| `ILLUSTRATIVE` | Synthetic or placeholder; must never be cited or rendered into the cache |

The renderer *raises* on an `ILLUSTRATIVE` set rather than writing it to
`references_cache/`, so synthetic numbers cannot become citable even by mistake.

Note the exact scope of that guard: it is a hard error for `ILLUSTRATIVE` only.
A `TOOL_EXPORTED` set under `examples/` — like the CHARMPheno one — stays
uncitable because `just phenodist-rebuild` only globs `kb/phenotype_distributions/`,
which is a directory convention rather than an enforced invariant, backed by a
test asserting no kb entry cites an example profile. The tier is the hard guard
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
    `--check-terms` run does not mean every term was checked. Verify LOINC by
    hand. A network-backed adapter that fails to respond yields a warning, not an
    error — an unperformed lookup is not evidence of a bad term.
- **Quoted evidence.** A `DataItem` citing a fetchable document — `PMID:`,
  `DOI:`, `clinicaltrials:`, `ORPHA:`, `CGGV:`, `CGDS:`, `ICEES:`, `NCIT:`,
  `PHENODIST:` — must be a verbatim substring of that document's
  `references_cache/` file, and the cache file must exist. Without this, an
  unverified quote could be rendered into a generated `PHENODIST_*.md` and then
  cited from a kb entry, where `validate-references` would verify it against the
  cache dismech itself produced — laundering an unverified quote into a
  validated-looking one.
- **Stale cache.** `write_cache_files` prunes orphaned `PHENODIST_*.md`, so a
  renamed or deleted `profile_id` cannot leave a citable file behind. Pruning
  runs only for a *full* rebuild — no paths, or directory paths — so naming an
  individual file never deletes another set's cache; `--no-prune` disables it
  entirely.

## Commands

```bash
# Validate one profile set (schema + lint)
just validate-phenotype-distribution kb/phenotype_distributions/my_set.yaml

# Validate all sets, including the worked example (part of `just qc`)
just validate-phenotype-distributions

# Regenerate references_cache/PHENODIST_*.md for curated sets
just phenodist-rebuild
```

`phenodist-rebuild` is a **no-op today** and prints "No phenotype profile sets
found": it globs `kb/phenotype_distributions/` only, and that directory does not
exist until the first curated set lands. The empty output is the correct result,
not a failure — the worked example is deliberately out of scope for it. It still
prunes, so a full rebuild after every curated set is deleted clears their cache
files rather than leaving them citable.

`validate-phenotype-distributions` runs schema validation, the lint, and the OAK
term check.

The lint catches what LinkML cannot express: duplicate profile ids, code weights
summing above 1, profile weights summing above 1, a short distribution that does
not declare itself `truncated`, a description misstating its own sum, a code
listed twice under the same qualifier, a `profile_weight` whose source declares
no `weight_basis`, and a quoted evidence item that is not a verbatim substring of
its cited reference.

## The worked examples

**Start with `examples/phenotype_distributions/minimal_asthma_illustrative.yaml`** —
one disease, one profile, three codes, and a comment on each decision the shape
makes. Its numbers are invented, which is what its `ILLUSTRATIVE` tier says, so
the renderer refuses to make it citable.

`examples/phenotype_distributions/charmpheno_population_eds.yaml` is populated
from a **real exported model** in the CHARMPheno dashboard's `population_eds`
bundle. Every number — the code probabilities and the profile weights — is
transcribed from that bundle's exported JSON. What is curator judgement, and
marked as such, is the reading of an unsupervised component as a named clinical
pattern. It is excluded from `just phenodist-rebuild` so it cannot become
citable, and a test asserts that no kb entry cites it and no cache file for it is
committed.

Its two profiles are each chosen to show something:

| Profile | Shows |
|---|---|
| `CHARMPHENO-EDS-HYPERMOBILE-001` | An `anchor`-quality profile with half its mass on its own diagnosis code — real, precise, and a tautology. Not worth citing. |
| `CHARMPHENO-EDS-DYSAUTONOMIA-001` | A profile recovering the EDS-dysautonomia association from coding alone, with the autonomic codes outweighing the anchor. |

That the first is unusable is the point: a profile can be real, precise,
well-provenanced, and still say nothing an entry does not already state.

## Relationship to existing dismech blocks

| Block | Relationship |
|---|---|
| `phenotypes[].frequency` | A band over patients. A `code_weight` is mass within a fitted distribution, not a frequency; they are not convertible. |
| `prevalence[]` | Disease *occurrence* in a population, over a denominator of patients. A profile weight has a corpus denominator, not a patient one. |
| `association_signals` | Disease-disease co-occurrence on comorbidity entries, also EHR-derived; a profile is code co-occurrence within one disease. |
| `genetic[].case_fractions` | Per-gene share of cases; the same "structured estimate with its own population and evidence" pattern, restricted to genetic heterogeneity. |

## Not in this iteration

An earlier version of this schema also carried a `PhenotypeDistributionCollection`
— the full statistical object behind a literature-derived `frequency:` band, with
distribution families, cohort identification chains, intervals and implied HPO
bands. It was cut as out of scope for this pass. Nothing here depends on it, and
it can return as its own schema if the use case is taken up.
