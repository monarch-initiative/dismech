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

- **Every PMID and DOI in the report body and citation list** is resolved
  against PubMed, Crossref and DataCite. An identifier that returns nothing is
  reported as unresolved (a possible confabulation).
- **Quotes attributed to a reference** are checked against the text of that
  reference.

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
  unresolved_references:
  - PMID:99999999
  - PMID:31234567
---
```

`confabulation_rate` is computed over the references a lookup actually answered
about (`verified + not_found`); `unverifiable` ones — skipped prefixes, or
identifier types with no resolver — are excluded, because nothing was learned
about them. **Read `unresolved_references` before anything else**: those are the
identifiers not to build on.

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

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup
that failed for transport reasons is indistinguishable from one that failed
because the record does not exist, so spot-check before acting on them:

- `PMID:99999999` (1 mention) - Could not fetch reference
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
| `--fail-on-unresolved` | Exit non-zero when anything failed to resolve. For pipelines, not interactive runs. |

## Checking a report that already exists

Reports generated before 0.2.9 — the bulk of `research/` — can be checked after
the fact:

```bash
just validate-research-reference research/Marfan_Syndrome-deep-research-falcon.md
just validate-research-reference research/*-deep-research-openscientist.md
```

This rewrites each report in place, replacing any previous
`## Reference Validation` section, so it is safe to re-run.

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
papers and quotes them correctly, so every counter here comes back green. The
MONDO gene/OMIM/synonym preflight is unchanged and still mandatory:

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
- Issue #8432 (this integration), #4525 (recording hallucinated DR citation IDs),
  #7791 (misattribution the snippet layer cannot catch)
