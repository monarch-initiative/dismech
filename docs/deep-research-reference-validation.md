# Deep-Research Reference Validation

Deep-research (DR) providers routinely emit identifiers that look plausible and
do not resolve, and quotes attributed to papers that do not contain them. Until
`deep-research-client` 0.2.9 the only way to find out was to curate first and
check later: pull each PMID out of the report by hand, `just fetch-reference`
it, paste a snippet into a `kb/` entry, and discover the problem when
`just validate-disorders` finally ran — by which point the entry had been built
around a source that does not exist.

Since 0.2.9 the check happens where the report is made. Every research recipe in
`project.justfile` now resolves the report's citations as part of generating it,
and writes the answer into the report.

## What gets checked

`deep-research-client[validation]` delegates to `linkml-reference-validator` —
the same library behind `just fetch-reference` and `just validate-references` —
so the rules are the ones dismech already uses.

Because this path both reads and writes `references_cache/`, the recipes invoke
it through `scripts/run_deep_research_client.sh`, which applies dismech's
`patch_reference_validator` repairs first — exactly as
`scripts/run_reference_validator.sh` does for the validator CLI. That matters
most for the issue #7697 delimiter-aware frontmatter read: without it, a cached
record whose frontmatter contains a literal `---` is truncated on read and
reported as a **false unresolved reference**, and the guidance below tells you
not to cite unresolved references. Do not call `deep-research-client` directly
for anything that validates; go through the wrapper or the recipes.

- **Every PMID and DOI in the report body and citation list** is resolved
  against PubMed, Crossref and DataCite. An identifier that returns nothing is
  reported as unresolved (a possible confabulation).
- **Quotes attributed to a reference** are checked against the text of that
  reference.
- **Topical relevance of each resolved reference** (since 0.2.10). The report's
  own most characteristic vocabulary is extracted — term frequency weighted by
  how many sections a term appears across, with the echoed prompt and duplicate
  lines removed first — and each reference's already-fetched record (title,
  journal, MeSH terms, abstract) is scored against it. `>= 0.35` is `ON_TOPIC`,
  `<= 0.08` is `OFF_TOPIC`, and anything between, or a record with too little
  metadata to judge, is uncertain and reported as neither. The thresholds were
  fixed empirically upstream against real report/bibliography pairs.

The verdict is **asymmetric on purpose**, and it is worth knowing which way. A
high score is good evidence a reference belongs; a low score only counts as
evidence when there was an abstract it could have matched in. A record that
resolved to a title and a MeSH list and nothing else is never called off topic,
however little it shares — convicting on controlled vocabulary alone would flag
papers that are squarely on topic. So `off_topic: 0` does not mean "every
citation was weighed and cleared"; part of it is "some had nothing to convict
on." `relevance_assessed` minus `on_topic` minus `off_topic` is the size of that
undecided remainder.

The relevance check **costs nothing extra** — no additional lookups, since it
reads records the existence check already fetched. It is on by default; disable
it with `--validation-no-relevance` on a research run, or
`--no-check-relevance` on `validate-references`.

An off-topic flag is **a clue, not a verdict.** The reference resolved, so it is
not a fabrication; it simply shares almost none of the report's vocabulary. A
paper can be genuinely relevant in a way its title and abstract do not spell
out. Correspondingly, off-topic references do **not** count as confabulations
and do **not** trip `--fail-on-unresolved` — they set `needs_review` instead, so
they cannot fail a build but also cannot be missed by someone reading a
reassuring `confabulation_rate`.

Lookups are cached into `references_cache/`, the same directory the KB
validators read. A reference checked at report time does not need re-fetching
when it is later cited from a `kb/` entry.

## Where to read the results

### In the report's frontmatter

A report generated with validation carries a machine-readable summary at the
top:

```yaml
---
provider: claude_code
citation_count: 24
reference_validation:
  total_references: 24
  verified: 22
  not_found: 2
  unverifiable: 0
  confabulation_rate: 0.083
  quotes_checked: 9
  quotes_valid: 8
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:26543210
  quotes_not_checkable: 2
  relevance_assessed: 22
  on_topic: 19
  off_topic: 1
  off_topic_references:
  - PMID:28123456
  unresolved_references:
  - PMID:99999999
  - PMID:31234567
  needs_review: true
---
```

`confabulation_rate` is computed over the references a lookup actually answered
about (`verified + not_found`); `unverifiable` ones — skipped prefixes, or
identifier types with no resolver — are excluded, because nothing was learned
about them. **Read `unresolved_references` before anything else**: those are the
identifiers not to build on.

Several of these keys only appear when there is something to say. The
`quotes_*`/`unsupported_quote_references` keys need at least one quote to have
been checked; `off_topic`/`off_topic_references` appear only when something was
flagged, so a report with `relevance_assessed` and `on_topic` but no `off_topic`
is a clean relevance pass. `relevance_assessed` + `on_topic` are absent entirely
if relevance checking was disabled.

Note that the two failure lists never overlap: a quote attributed to a reference
that did not resolve is not *contradicted* by its source, it simply has no source
to check against, so it is counted under `quotes_not_checkable` rather than
`quotes_unsupported`. `unsupported_quote_references` therefore only ever names
references that *did* resolve. The example above shows both — one quote checked
against a real paper and not found in it, and two quotes stranded on the two
unresolved identifiers. `quotes_checked` counts only the ones there was something
to check against, so the example's eleven quoted claims appear as `9` plus a
separate `quotes_not_checkable: 2`, not as a total of eleven.

**`needs_review: true` is the one flag to grep for.** It is set whenever any
identifier failed to resolve, *or* any quote failed to match, *or* any reference
looks off topic — deliberately wider than `confabulation_rate`, which measures
identifier resolution and nothing else. A report whose every identifier resolved
but whose quotes did not match still reports `confabulation_rate: 0.0`; that is
how a CHILD-syndrome report with six mismatched quotes was once read as clean.
Treat `needs_review` as "go and look", not as a failure.

### In the report body

A `## Reference Validation` section is appended at the end:

```markdown
## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 24 |
| Resolved | 22 |
| Unresolved (possible confabulation) | 2 |
| Unverifiable | 0 |
| References weighed for topical relevance | 22 |
| On topic | 19 |
| Off topic | 1 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup
that failed for transport reasons is indistinguishable from one that failed
because the record does not exist, so spot-check before acting on them:

- `PMID:99999999` (1 mention) - Could not fetch reference

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they
resolve to share almost none of this report's vocabulary. That is a clue and not
a verdict - a paper can be relevant in ways its title and abstract do not spell
out - so read them before deciding:

- `PMID:28123456` (1 mention) - Some unrelated-looking paper title
  - shared terms: none

Weighed against this report's own most characteristic terms: `abcc9`, `sur2`, ...
```

That last caveat is the honest one and worth keeping in mind: a network failure
and a fabricated identifier look identical from here. Treat "unresolved" as
"check this by hand", not as proof of fabrication.

## Generating a validated report

Nothing to remember — it is on by default in every research recipe:

```bash
just research-disorder falcon Marfan_Syndrome
just research-module falcon fibrotic_response
just research-comorbidity openai com_Foo__Bar
```

The report is written to disk **before** validation runs, so a network failure
during validation costs you the validation section, never the report.

To skip it — quick iteration, or no network:

```bash
just dr_validation='' research-disorder falcon Marfan_Syndrome
```

The flags live in one place, the `dr_validation` variable in `project.justfile`:

```
dr_validation := "--validate-references --validation-cache-dir references_cache"
```

Other options `deep-research-client` accepts, if you need them for a one-off
(pass them through the recipe's trailing `*args`, or override `dr_validation`):

| Flag | Effect |
|---|---|
| `--validation-full-text` | Fetch full text as well as abstracts. ~23x slower; much better quote checking. |
| `--validation-max-references N` | Stop after N references. The report records `truncated: true`. |
| `--validation-skip-prefix DOI` | Report a prefix as unverifiable instead of resolving it. The largest saving after caching. |
| `--validation-rate-limit-delay S` | Seconds between lookups (default 0.5). Lowering it risks rate-limit errors being reported as unresolved references. |
| `--validation-no-relevance` | Turn off the topical-relevance check. It is free and on by default, so there is rarely a reason to. |
| `--fail-on-unresolved` | Exit non-zero when anything failed to resolve *or* any quote is unsupported. Off-topic references are excluded on purpose. For pipelines, not interactive runs. |

(On the standalone `validate-references` subcommand the relevance switch is
spelled `--no-check-relevance`.)

## Checking a report that already exists

Reports generated before 0.2.9 — the bulk of `research/` — can be checked after
the fact:

```bash
just validate-research-reference research/Marfan_Syndrome-deep-research-falcon.md
```

This rewrites each report in place, replacing any previous
`## Reference Validation` section, so it is safe to re-run.

**One report at a time, as you come to curate it** — that is the intended use.
The recipe accepts a glob, but pointing it at the whole tree rewrites ~1400
committed files and re-resolves tens of thousands of references against PubMed
for reports nobody is reading today. A report earns its validation section when
someone is about to build an entry on it.

**One asymmetry to know about:** the retro-fit path adds the markdown section
but **not** a `reference_validation:` frontmatter block. Upstream only *refreshes*
a frontmatter summary that is already there, deliberately — so that a tool asked
to check citations never reformats a file's frontmatter. On a legacy report,
read the section at the bottom; the frontmatter will not mention validation.

For a non-destructive look, or JSON for tooling, call the underlying command:

```bash
uv run deep-research-client validate-references research/Foo-deep-research-falcon.md
uv run deep-research-client validate-references research/Foo.md --json /tmp/report.json
```

## What this does **not** replace

A clean counts table is not permission to skip the evidence SOP. Three distinct
things stay exactly as they were:

**1. KB snippet validation.** This checks the *report's* citations. It says
nothing about the snippet you later paste into `kb/disorders/*.yaml` — that is a
different quote, in a different file, and it still needs
`just count-verified-snippets` in the curation loop and `just validate-disorders`
before the PR. A report can pass validation completely and still be the source of
a mis-transcribed snippet.

**2. Named Entity Confusion.** A report about the *wrong disease* cites real
papers and quotes them correctly, so every counter here comes back green. **The
0.2.10 relevance check does not help here either, and it is worth being precise
about why:** relevance is scored against *the report's own* characteristic
vocabulary. If the report is about the wrong disease, so is its vocabulary, and
its wrong-disease citations score as perfectly on topic. The two checks look for
different things — relevance catches one stray citation in an otherwise sound
report; `preflight-dr` catches a report that is internally consistent and about
the wrong entity. Passing one says nothing about the other. The MONDO
gene/OMIM/synonym preflight is unchanged and still mandatory:

```bash
just preflight-dr research/My_Disease-deep-research-falcon.md MONDO:XXXXXXX
```

See CLAUDE.md §2b.

**3. Misattribution.** A real, resolvable paper cited for a claim it does not
make survives an existence check untouched. Quote checking catches some of this
where the report actually quotes its source, but a report that *paraphrases* a
paper into a claim the paper never made is not detectable here (issue #7791).

The one-line version: this closes the "does the citation exist" gap and part of
the "does the quote appear in it" gap, at report time instead of hours later. It
does not close "is it about the right disease" or "does it say what the report
claims".

## Related

- CLAUDE.md §2a (DR outputs need extra verification) and §2b (Named Entity
  Confusion)
- [Quality Control & Compliance](quality-control.md)
- Issue #8432 (this integration), #8685 (the 0.2.10 relevance check),
  #4525 (recording hallucinated DR citation IDs), #7791 (misattribution the
  snippet layer cannot catch)
