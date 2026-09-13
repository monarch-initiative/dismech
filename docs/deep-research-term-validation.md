# Deep-Research Term Validation

Deep-research (DR) reports suggest ontology terms because our templates ask them
to — "Suggest HPO terms for each phenotype", "Suggest GO terms for biological
processes and CL terms for cell types", "suggest NCIT clinical-intervention
terms", and a closing summary line of term suggestions across HPO, GO, CL,
UBERON, CHEBI, NCIT and MONDO. Until `deep-research-client` 0.2.11 nothing
checked any of them.

Citation validation does not reach them. The OpenScientist report on
Charcot-Marie-Tooth X-linked had 26 of 26 citations verified and a 0%
confabulation rate, and offered `MONDO:0010674` — mucopolysaccharidosis type 2,
Hunter syndrome — as the MONDO term for the disease
([#9729](https://github.com/monarch-initiative/dismech/issues/9729)). A report
can be citation-clean and still carry a wrong CURIE in a summary table.

Since 0.2.11 every research recipe in `project.justfile` resolves the report's
ontology terms as part of generating it, and writes the answer into the report.

## What gets checked

`deep-research-client[terms]` delegates to `linkml-term-validator` — the same
library behind `just validate-terms` — so the rules are the ones dismech already
uses on `kb/`.

Every CURIE in the report body is resolved through OAK, and three things are
reported:

- **Existence.** An identifier no ontology contains is reported as unresolved —
  a likely confabulation. `HP:0106487`, offered by the CMTX report as "impaired
  distal sensation", is one: HPO has no such term.
- **The name the report gave it.** The label written beside a CURIE is compared
  with the term's own label and its synonyms. This is the check that catches a
  real identifier used for the wrong thing, which existence checking cannot see.
- **Obsolescence.** A real term the ontology has since retired.

Label matching is strict about *where* it looks and lenient about *what* it
accepts: only labels in table cells, emphasized text, or immediately beside the
identifier are compared, and every synonym counts as a match. It undercounts
rather than inventing errors.

The results are graded, and the grades matter when you read them:

| Section | What it means |
|---|---|
| Unresolved terms | The identifier does not exist. Do not use it. |
| Terms the report names something else | The identifier resolves to a term the report calls something else — a different disease, or a different term in the same ontology. Usually the wrong identifier. |
| Terms whose name is worth a second look | The report's name is recognisably related without being the term's own name — a paraphrase, or a *related* synonym. Listed, not judged. |
| Terms named inconsistently | The report gives one identifier more than one name of its own. |
| Prefixes with no resolver | Not checked either way. Not evidence of anything. |

Some of the middle two categories are noise on a well-behaved report — a report
writing "distal weakness" next to `HP:0002460` (*Distal muscle weakness*) is
right, and gets flagged. Read the unresolved list first, then work the "names
something else" list for entries where the ontology label names **a different
disease, or a different term in the same ontology** — a sibling, a parent, a
near-miss.

The second kind is easy to skim past and is the more common wrong-term failure.
The CMTX report has one: it writes "areflexia" beside `HP:0001265`, which HPO
calls *Hyporeflexia* — *Areflexia* is `HP:0001284`. Reduced reflexes and absent
reflexes are distinct HPO terms with a real clinical distinction, so a curator
who reads that line as paraphrase binds the wrong CURIE while writing the right
`preferred_term`. This is the granularity problem `dismech-terms` exists to
catch, arriving through a report rather than through a search.

## Where the results go

Two places, the same as reference validation:

- a `## Term Validation` section appended to the report body, and
- a `term_validation:` block in the report's YAML frontmatter:

```yaml
# the real summary for research/Charcot-Marie-Tooth_Disease_Type_X-deep-research-openscientist.md,
# with the mislabelled list trimmed to its first entry
term_validation:
  total_terms: 24
  verified: 21
  not_found: 1
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.045
  labels_checked: 20
  labels_matching: 5
  labels_mismatched: 8
  mislabelled_terms:
  - term_id: MONDO:0010674
    reported_labels:
    - MONDO
    ontology_label: mucopolysaccharidosis type 2
  labels_variant: 7
  unresolved_terms:
  - HP:0106487
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
```

`confabulation_rate` measures identifier resolution and **nothing else** — a
report whose every CURIE resolves but whose labels name different terms still
shows `0.0`. That is why `labels_mismatched` and `needs_review` are stated
outright. Do not read the rate alone as an all-clear.

## Two configuration choices, and why

Both were settled by running the validator, not by preference.

**No `--term-oak-config conf/oak_config.yaml`.** Our config routes the prefixes
reports actually cite — MONDO, HP, GO, CL, UBERON, CHEBI, NCIT — to OLS, which
is exactly what the upstream default `ols:` adapter already does. But it also
maps HGNC, GENO, ECTO, XCO, OPL and the ICD prefixes to `sqlite:obo:`, and
passing it made a validation run download a 380 MB `hgnc.db` mid-report. Pass it
yourself for a run where ECTO or GENO terms matter and you will take the local
builds:

```bash
just dr_term_validation='--validate-terms --term-cache-dir terms_cache --term-oak-config conf/oak_config.yaml' \
    research-disorder falcon Silicosis
```

**`--term-skip-prefix HGNC`**, because gene CURIEs cannot be checked reliably
either way, and both failure modes are false alarms on a real gene:

| Adapter | `HGNC:4283` (which is GJB1) |
|---|---|
| `sqlite:obo:hgnc` | does not resolve — the build holds genes under the lowercase `hgnc:` this repo uses, so an uppercase CURIE is reported as invented |
| `ols:` | resolves to **"mitochondrial chromosome"** |

Skipping reports the prefix as unverifiable instead, which is honest. Matching
is case-insensitive, so it covers `hgnc:` too. Gene identifiers in a report
still need checking — do it the way you already do, against HGNC itself, when
you bind one into a `kb/` entry.

## What it does not do

- **It does not validate the knowledge base.** `just validate-terms` on
  `kb/**.yaml` is unchanged and is still the gate. This checks a provider
  artifact.
- **It does not check dynamic-enum membership.** dismech bindings must be
  reachable from an enum root — `regimen_term` from `NCIT:C15697`, and so on. A
  report suggesting `NCIT:C66930` for a regimen passes the existence check here
  and still fails `just validate`.
- **It does not know what the report is about.** A term that exists, is current,
  and is named correctly can still be the wrong term for this disease. That is
  Named Entity Confusion, and `just preflight-dr` is the check for it. The CMTX
  case was caught here only because the report wrote `| MONDO | MONDO:0010674 |`
  and "MONDO" is not what the ontology calls Hunter syndrome — a label mismatch,
  not a topic judgement.

## Turning it off, and the flags

The flags live in one place, the `dr_term_validation` variable in
`project.justfile`:

```
dr_term_validation := "--validate-terms --term-cache-dir terms_cache --term-skip-prefix HGNC"
```

To skip it — quick iteration, or no network:

```bash
just dr_term_validation='' research-disorder falcon Marfan_Syndrome
```

Validation runs **after** the report is written to disk, so a network failure
during it costs you the validation section, never the report. Recover with
`just validate-research-terms <the report that was written>`.

Other options `deep-research-client` accepts (pass them through the recipe's
trailing `*args`, or override `dr_term_validation`):

| Flag | Effect |
|---|---|
| `--term-adapter TEXT` | OAK adapter to resolve through. Default `ols:`; `sqlite:obo:` downloads each ontology once and answers locally. |
| `--term-oak-config PATH` | Per-prefix adapter map, for ontologies the default adapter does not serve. |
| `--term-offline` | Resolve only from the label cache; uncached terms are reported as unverifiable. |
| `--term-max-terms N` | Stop after N terms. The report records `truncated: true`. |
| `--term-skip-prefix PREFIX` | Report a prefix as unverifiable instead of resolving it. Repeatable. |
| `--no-term-labels` | Existence checking only. Turns off the check that catches most real errors, so rarely worth it. |
| `--fail-on-unresolved` | Exit non-zero on an unresolved or mislabelled term. For pipelines, not interactive runs. |

The check is deliberately **not** gated by default. A bad CURIE in a provider
artifact is information, not a reason to discard a 20-minute run.

## Checking a report that already exists

Every report generated before 0.2.11 — effectively all of `research/` — can be
checked after the fact:

```bash
just validate-research-terms research/Marfan_Syndrome-deep-research-falcon.md
```

This rewrites the report in place, replacing any previous `## Term Validation`
section, so it is safe to re-run. Resolved labels are cached in `terms_cache/`,
so a second pass over the same report is offline and instant
(`just validate-research-terms <report> --offline` never touches the network).

**One report at a time, as you come to curate it.** The recipe accepts a glob,
but pointing it at the whole tree rewrites ~1400 committed files and re-resolves
tens of thousands of terms for reports nobody is reading today.

**The same asymmetry `validate-research-reference` has:** on a report that
predates term validation, the retro-fit path adds the markdown section but
**not** a `term_validation:` frontmatter block. Upstream only *refreshes* a
frontmatter summary that is already there, so that a tool asked to check terms
never reformats a file's frontmatter. On a legacy report, read the section at
the bottom.

For a non-destructive look, or JSON for tooling:

```bash
scripts/run_deep_research_client.sh validate-terms research/Foo-deep-research-falcon.md
scripts/run_deep_research_client.sh validate-terms research/Foo.md --json /tmp/terms.json
```

## The label cache

Resolved labels land in `terms_cache/`, which is **gitignored** and in the same
per-prefix `curie,label,retrieved_at` format as the committed `cache/` CSVs.

They are kept apart on purpose. `cache/<prefix>/terms.csv` is committed so that
KB term validation is deterministic offline, and its rows correspond to terms
actually bound in `kb/`. A provider's suggestion list is a different thing:
pointing research runs at `cache/` would add committed-cache churn for terms
nobody curated, arriving through a path no reviewer is looking at.

Because the format is identical, a curator who wants the pre-warm can opt in for
a run:

```bash
just dr_term_validation='--validate-terms --term-cache-dir cache --term-skip-prefix HGNC' \
    research-disorder falcon Marfan_Syndrome
```

Review the resulting `cache/` diff before committing it, and run
`just normalize-cache` and `just check-term-cache-integrity` as you would for any
other cache change.

## Also in 0.2.11

Two other changes arrived in the same release.

**Provider fallback** (`--fallback`) lets a run hand off to another provider when
the chosen one has no credentials or credit, and records which provider actually
produced the report. It is wired in as an opt-in, with an alignment step that
renames a report that fell back to the provider named in its own frontmatter —
otherwise a `claude_code` report would keep the `-falcon.md` name that
`scripts/deep_research_coverage.py` reads coverage out of. See
[`docs/deep-research-provider-fallback.md`](deep-research-provider-fallback.md).

**Auth and billing failures are now non-retryable, and "available" means
reachable.** Nothing in this repo reads provider availability programmatically —
no workflow shells out to `research-providers` — so this changes what you see
when you run it by hand and how quickly a run with a missing key gives up,
and needs no change here.

## Related

- [`docs/deep-research-reference-validation.md`](deep-research-reference-validation.md)
  — the citation-side counterpart, wired the same way.
- `just preflight-dr` — the Named Entity Confusion check, which asks a question
  this one cannot.
- `.claude/skills/dismech-terms` — how to choose and validate a binding once you
  are putting it in a `kb/` entry.
