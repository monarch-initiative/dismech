---
name: dismech-references
description: >
  Add, validate, repair, or review evidence references and exact-quote snippets
  in dismech KB YAML and deep-research reports. Use for PMID, DOI, NCT, ICTRP,
  or structured-source evidence; reference-cache generation; snippet failures;
  title snippets; bracket normalization; deep-research citation validation;
  Named Entity Confusion preflight; evidence_source classification; and final
  evidence checks before a PR.
---

# Curate Evidence and References

Use this workflow whenever evidence or its cited source changes.

## Non-negotiable rules

- Quote an exact substring of the cited source. Do not paraphrase or fabricate a
  `snippet`.
- Confirm that the quote substantively supports the precise claim. A matching
  string from the wrong paper, or an unrelated sentence from the right paper,
  is not evidence.
- Prefer a result sentence from the abstract or authoritative source record.
  A paper title usually establishes only that a topic was studied.
- Never create or hand-edit `references_cache/*.md`. Generate or regenerate a
  cache entry with `just fetch-reference <ID>`.
- Never use fuzzy auto-repair to rewrite snippets. Read the source and copy the
  exact passage, choose another source, or remove the evidence.
- Treat deep-research output as leads, not ground truth.

## Evidence shape

```yaml
evidence:
  - reference: PMID:12345678
    supports: SUPPORT
    evidence_source: HUMAN_CLINICAL
    snippet: "Exact text copied from the cited source."
    explanation: "How this passage supports the specific KB claim."
```

Use `supports: SUPPORT`, `REFUTE`, or the value allowed by the schema. Make the
`explanation` connect the quote to the claim without adding conclusions the
quote does not establish.

Classify `evidence_source` by the cited study, not by the curator or the claim:

- `HUMAN_CLINICAL`: patients, cohorts, clinical observations, or trials
- `MODEL_ORGANISM`: in vivo non-human animal or organism work
- `IN_VITRO`: cells, organoids, explants, or biochemical assays
- `COMPUTATIONAL`: modeling, simulation, or in-silico analysis
- `OTHER`: evidence that does not fit the categories above

Inspect the schema and nearby current entries if a field or enum is uncertain.

## Workflow

### 1. Screen deep-research sources

If evidence came from `research/`, first read the report's
`reference_validation`, `unresolved_references`, `needs_review`, and
`off_topic_references` results. Do not curate an unresolved identifier. An
off-topic flag is a reason to inspect the paper, not an automatic rejection.

For an older report without validation output, run:

```bash
just validate-research-reference research/My_Disease-deep-research-falcon.md
```

The same recipes also check the report's **ontology terms** (`term_validation`
in the frontmatter, `## Term Validation` at the end of the body). That is a
different check from the citations one and catches a different error: a report
can have every citation verified and still name the wrong MONDO term for the
disease. Never bind a CURIE listed under `unresolved_terms`. For an older report,
`just validate-research-terms <report>` adds the section; see
[`docs/deep-research-term-validation.md`](../../../docs/deep-research-term-validation.md).

Before using any report content, check that the report describes the intended
disease:

```bash
just preflight-dr research/My_Disease-deep-research-falcon.md MONDO:XXXXXXX
```

It reads the local MONDO build when it is on disk and the same term from OLS
otherwise, and says which in its `MONDO source` line; it never downloads the
build (about 1.3 GB on disk). It exits 2 only when OLS is unreachable too, and
that is not a verdict: retry, or run `just fetch-ontology-dbs mondo` once. Over
OLS the rival-gene disease lookup cannot run, so a report that never names the
canonical gene but cites the right OMIM number comes back `WARN`, not `FAIL`.
Without the local HGNC build it skips the HGNC lexicon and alias lookups, as
`--no-hgnc` does, rather than downloading it; `just fetch-ontology-dbs hgnc`
gives the sharper gene lexicon.

Interpret the result as follows:

- `PASS`: proceed to normal source, snippet, and term verification.
- `WARN`: resolve the reported conflict or degraded lookup, then manually check
  the causal gene, OMIM xref, and synonyms.
- `FAIL`: discard the report. Do not cherry-pick from it.
- `SKIP`: the automated check cannot discriminate; manually check disease
  identity before proceeding.

For a `WARN` or `SKIP`, inspect the intended MONDO record directly. This reads
it from OLS and downloads nothing:

```bash
uv run python -c "from dismech.mondo_ols import fetch_mondo_term; print(fetch_mondo_term('MONDO:XXXXXXX'))"
```

It prints the label, the `RO:0004003` gene(s) with their symbols, every xref
(OMIM among them), exact synonyms, and obsolescence. For related and broad
synonyms, open the term in the OLS browser
(`https://www.ebi.ac.uk/ols4/ontologies/mondo`, search the MONDO ID). Only if
you already have the local build, `uv run runoak -i sqlite:obo:mondo info
MONDO:XXXXXXX -O obo` shows the same record; without the build that command
downloads about 1.3 GB.

Compare its causal-gene relationship (`RO:0004003`), OMIM xref, and synonyms
with the report. Look specifically for synonym aliasing, eponymic collision,
abbreviation ambiguity, or conflation with a closely related disease. On any
identity mismatch, discard the report rather than cherry-picking from it.

A report that cites the right OMIM number can still be about the wrong gene
(#12166: an immunodeficiency 97 report cited OMIM 619802 and discussed TBK1,
never PIK3CG). When the canonical gene is never named, `preflight-dr` looks up
whether the genes the report does discuss cause another MONDO disease and, if
one does, returns `FAIL` whatever the OMIM citation says. A `WARN` that reports
a matching OMIM number and zero canonical-gene mentions means no rival gene
resolved to another disease: search the report for the gene under any name,
and discard it if the gene is not there.

See `docs/deep-research-reference-validation.md` and
`research/nec_risk_disease_classes.md` for uncommon cases.

### 2. Fetch each new reference

```bash
just fetch-reference PMID:12345678
```

Use the actual identifier for other supported reference types. Read the fetched
record and confirm its identity, topic, and quoted passage. A successful fetch
does not prove that the source supports the claim.

"Successfully cached" also does not mean the record has text to quote. If the
fetch printed a `WARNING: ... cached with no quotable text`, read
[Empty caches](#empty-caches-content_type-unavailable) before going further.

### 3. Run the fast edit loop

After each disorder-file edit, run:

```bash
just validate kb/disorders/MyDisease.yaml
just count-verified-snippets kb/disorders/MyDisease.yaml
just validate-terms kb/disorders/MyDisease.yaml
```

All three commands accept the files supported by their recipes; batch files
where practical. `count-verified-snippets` is fast and offline, but advisory.
It reports missing cache entries and skipped prefixes rather than resolving
them.

### 4. Run the authoritative pre-PR sweep

Once, after the tranche is complete, name every changed disorder file:

```bash
just validate-disorders \
  kb/disorders/FirstDisease.yaml \
  kb/disorders/SecondDisease.yaml
```

This batched command mirrors CI's schema, term, and reference checks and uses
`--no-full-text`. It is the authoritative evidence gate for disorder files.
Use `just validate-kb-references <file>` only when a non-disorder target or a
full-text-permitting diagnostic requires it.

Never report a validation command as passing unless it finished and you read
its output.

## Resolve failures

When a snippet is not found:

1. Read the fetched source record.
2. Confirm the identifier belongs to the intended paper or record.
3. Copy an exact, substantively relevant passage.
4. If no such passage exists, cite a better source or remove the evidence.

If the claim is useful but no quotable evidence is available, move it to a
`notes` field where appropriate, keep an unevidenced description only where the
schema and curation policy permit it, or remove the claim. Never manufacture a
quote to preserve an evidence block.

**Moving a claim to `notes` applies to your own well-established knowledge, and
to nothing else.** It is the exact wrong move for a claim you took from a
deep-research report and could not verify: moving that into `notes` does not
soften it, it launders it, because `notes` is the one place no check will ever
look. The two cases read identically in the diff and are opposite in kind.

| You cannot quote it because… | Do |
|---|---|
| the fact is textbook and no abstract states it crisply | move it to `notes`, no evidence |
| a DR report asserted it and the cited abstract does not contain it | **drop the claim** — it is unverified, not merely unquotable |

`Total checks: 0` in reference-validator output means zero issues were counted;
it does not mean no evidence was examined. Use the wrapper's affirmative
`Snippets checked: N/N verified` summary to describe cache-backed coverage.

`DOI:` and `PMID:` snippets are checked by the same authoritative validator.
A missing source, missing body, or mismatched quote fails validation; a failed
fetch is not evidence that the quote is valid. A cache containing only an
abstract cannot verify text quoted from elsewhere in the paper.

Some dataset-accession prefixes remain in `skip_prefixes` within
`conf/reference_validator_config.yaml`. The `(N skipped by prefix)` summary
reports those omissions; skipped never means verified. `--unskip-prefix` is a
diagnostic for auditing an exempt prefix and is not required for DOI evidence.

Never add literature prefixes to `skip_prefixes`, downgrade an unverified
reference to a warning, or relax quote matching to make CI pass. Changes that
weaken an evidence constraint require explicit approval from `cmungall`
(issue #11921).

## Typography: a snippet need not be byte-identical

"Exact substring" means exact **after normalization, on both sides**.
`SupportingTextValidator.normalize_text` (in `linkml-reference-validator`, and
reused by `just count-verified-snippets`) spells out Greek letters, lowercases,
replaces every non-word non-space character with a space, then collapses runs of
whitespace with `re.sub(r"\s+", " ", ...)`. Python's `\s` on `str` patterns
matches Unicode whitespace, so most publisher typography folds away on both
sides:

| In the source | Write in the snippet |
|---|---|
| U+2009 thin space (common around `=` in Nature journals) | an ordinary space |
| U+00A0 no-break space | an ordinary space |
| U+2013 en dash, U+2212 minus (ranges, negative exponents) | an ordinary hyphen |
| U+00D7 multiplication sign | see the traps below |

So `"AUC = 0.933"` typed with ordinary spaces matches source text reading
`AUC<U+2009>=<U+2009>0.933`, and `"(3.97-6.38)"` matches `(3.97–6.38)`. In the
#9308 tranche, **8 of 15 snippets were not byte-exact and all 15 verified**.

This is worth knowing because the alternative is silently worse curation. During
#9308 both the curator and the reviewer independently concluded that a figure in
a Nature paper could not be quoted, because the source puts thin spaces around
every `=`. Neither checked, and it cost a curated entry — recovered only
mid-review. A curator who believes a figure "cannot be quoted" paraphrases it
into `explanation` prose or drops the claim, and nothing goes red.

**Greek letters verify in either spelling.** `greek_map` runs on both sides, so
`α3β3` and `alpha3beta3` both normalize to `alpha3beta3`, `γ` to `gamma`, and
`NF-κB` to `nf kappab`. Prefer copying the source's visible letter, so the quote
reads as the source does (#9433). The ASCII spelling is an acceptable fallback,
provided it keeps the source's spacing: `NF-kappa B` normalizes to
`nf kappa b` and does not match.

**Never truncate a quote to avoid a character.** A snippet that stops just
before a Greek letter, `×`, or any other character it was cited for still
verifies, and clears `check-snippet-length` once it has `MIN_SNIPPET_WORDS = 5`
words, so the length gate is not a backstop. On #15493 two such fragments
(`Leu335 lies close to the hydrophobic sleeve in the`, `Mutations in this region
in the`) passed every gate and supported nothing (#15607). Quote through the
character, or choose a different sentence.

To test a candidate, call the real normalizer, not a re-implementation of it:

```bash
uv run python -c "from linkml_reference_validator.validation.supporting_text_validator import SupportingTextValidator as V; print(V.normalize_text('the α3β3 assembly'))"
```

**Prefer ASCII for invisible and lookalike characters** — an invisible character
in a quote is a trap for the next curator, and it buys nothing, since the
source's typography folds anyway. A visible Greek letter that is part of the
nomenclature is not that case. Existing snippets that copied the source's thin spaces and en dashes
verbatim are equally valid and need no repair; several hundred `kb/disorders`
snippets do exactly that.

**The traps — characters that do *not* vanish.** Each of these survives
normalization on one side only, so the comparison fails:

- **`x` for `×`.** `x` is a word character and survives, while U+00D7 becomes a
  space, so `"7.03 x 10-48"` does *not* match `7.03 × 10−48`. Include the
  literal `×`, or end the quote before the scientific-notation clause.
- **Mid-word invisibles.** U+00AD soft hyphen and U+200B zero-width space
  normalize to a *space*, splitting the word: cached `diffi<U+00AD>culties`
  becomes `diffi culties` and never matches `difficulties`.
- **Ligatures.** U+FB01 `ﬁ` is a word character and survives unchanged, so
  cached `speciﬁc` does not match `specific`. Note the asymmetry: `just
  count-verified-snippets` folds ligatures in its relaxed cache-defect pass
  (#8048, `normalize_relaxed` in `src/dismech/reference_snippet_audit.py`) but
  the gating `linkml-reference-validator` does not — so such a snippet can pass
  the fast check and fail the pre-PR sweep.
- **Micro sign.** U+00B5 `µ` survives, since only U+03BC `μ` is in `greek_map`.

If a quote you copied verbatim still fails, run `just count-verified-snippets` —
it names the span it could not find rather than leaving you guessing.

## Titles and brackets

Run `just check-title-snippets` when adding or repairing evidence. Quote a title
only in the rare case that the title itself states a result; explain why it is
probative. If the cached record has no abstract, cite the underlying study or a
different source instead of treating a topic-shaped title as a finding. Do not
manually regenerate `tests/title_snippet_baseline.txt` when fixing an existing
title snippet.

Snippet matching applies `literal_bracket_patterns` from
`conf/reference_validator_config.yaml`:

- all-caps abbreviations and spans containing a percent sign remain literal and
  must be quoted exactly;
- numeric citation markers and curator glosses are stripped before matching.

If a verbatim quote fails near brackets, read the reason printed by
`count-verified-snippets`. Do not change the global patterns to accommodate one
snippet without replaying validation across the KB.

### Bridging a stripped bracket with an ellipsis

Any other bracketed span is stripped too, including source text such as a bare
confidence interval (`[0.31-0.83]`), a cohort size (`[n = 30]`), or a citation
marker (`[9]`). Stripping applies to the snippet only, not the cached text, so a
stripped span at the end of a quote is harmless but one in the middle leaves a
hole and the quote fails. That does **not** mean the sentence cannot be quoted.

Both `count-verified-snippets` and the `validate-disorders` gate split a snippet
on every run of two or more ASCII dots (`..` or more; the single `…` character
does not count) and require each part to appear somewhere in the cached text.
So replace the stripped span with ` ... `. From PMID:10023895 (#9848):

```yaml
# Source: "... urinary-tract infection (0.50 [0.31-0.83]), or haematuria (0.59 [0.35-0.98])."
# Fails: [0.31-0.83] is stripped mid-quote
snippet: "a history of urinary-tract infection (0.50 [0.31-0.83]), or haematuria (0.59"
# Verifies: the ellipsis bridges the stripped span
snippet: "a history of urinary-tract infection (0.50 ... or haematuria (0.59"
```

Do not truncate the quote before the stripped span instead. That is how a
haematuria claim ended up citing a quote that stopped one clause short of the
word "haematuria": it verified and supported nothing.

**An ellipsis may bridge text you are omitting, never text the claim relies
on.** The parts are matched independently, in any order, so nothing checks what
the ellipsis skipped. Bridging intervening prose to join the subject to the
finding is the practice #3757 established, with worked examples. Skipping over
the clause that carries the finding, or a negation or qualifier, produces a quote
that verifies and misstates the source, which is worse than a failing one; #441
records that caution. When in doubt, quote a shorter contiguous span that
supports the claim on its own.

### Read the title off the cache, never from memory

`reference_title` (on an `EvidenceItem`) and `title` (on a top-level
`references:` entry) name the paper you cited, and until #9138 nothing checked
them. The failure mode that exposed is specific: **correct PMID, verified
snippet, invented title.** Each gate reads a different field — `linkml-validate`
confirms the slot is a string, `count-verified-snippets` and
`validate-kb-references` check the *snippet*, `validate-terms` checks ontology
terms, and `check_title_snippets` (despite the name) asks whether a snippet
quotes a title. None of them reads the title.

On PR #9111 three of twenty `(reference, reference_title)` pairs named papers
that do not exist. Two were written by an agent that had just verified the
adjacent snippets as exact substrings of the cached text, then wrote the titles
beside them from memory. Being rigorous about the quote and careless about the
citation attached to it is a distinct failure mode, and these values are not
inert — they render on the disorder page and flow into the cx2 and SEPIO
exports.

The correct title is already on disk, in the reference's cache frontmatter:

```bash
head -5 references_cache/PMID_34081534.md
# ---
# reference_id: PMID:34081534
# title: Axonal Growth Abnormalities Underlying Ocular Cranial Nerve Disorders.
```

Copy it from there. `just check-reference-titles` gates new mismatches (offline,
similarity-based, so punctuation, dashes, diacritics and source-XML markup do
not trip it) and prints the cached title in the failure message, so the fix is a
copy-paste. `just list-reference-title-mismatches` is the triage view;
`just check-reference-titles-present` is the complementary gate for *absent*
titles: every evidence item must carry one. Fill a gap with
`uv run python scripts/backfill_reference_titles.py <file>`, which copies the
cached title, rather than typing it.

## Frequency claims

A phenotype `frequency:` value is a separate quantitative claim from the
disease-phenotype association. Give it evidence that supports the frequency
band or omit it. Follow `docs/frequency-evidence-guidelines.md` for acceptable
quantitative, derived, qualitative, and clinical-estimate evidence.

## The prose layer is unchecked — figures in `description` and `notes`

Every anti-hallucination check dismech runs reads `evidence[].snippet`.
`validate-references`, `count-verified-snippets`, `check_snippets_verbatim.py`,
`check-title-snippets`, `check-snippet-length` — all of them. **A claim that
never becomes a snippet is checked by nothing.**

So this passes the entire suite:

```yaml
# Wrong: a real, topical PMID attached to a figure it does not contain
- name: Autism Spectrum Disorder
  description: >-
    ...TAND collectively affects ~90% of TSC patients across the lifespan.
  evidence:
  - reference: PMID:27226234        # real paper, correct topic, zero percentages
    snippet: "TSC-associated neuropsychiatric disorders, which can include..."
```

The snippet verifies. The PMID resolves. The paper is genuinely about TSC. The
`~90%` appears nowhere in it. This is a distinct failure mode from an unresolved
identifier or a named-entity confusion: the citation is right and the *number* is
imported from somewhere else. It is also, empirically, the one that gets through
— @jmcmurry ran 10 new entries whose curating agents were each explicitly warned
about this exact risk and each adversarially reviewed for it: snippets came back
**992/992 clean**, and unverified or source-contradicted prose claims turned up
in **10 of 10 entries** (#7791). Two recurring generators worth naming: an author
affiliation read as patient ancestry ("a Sydney affiliation" → "Australian
families"), and a process claim stated as a world fact.

**The rule:** a figure you cannot attach to a verbatim snippet does not belong in
prose either. Prose is not the safe place to put a claim you could not verify —
it is the *unprotected* place. So when screening a deep-research report, verify
every quantitative claim you write into `description` or `notes` against the
cached text of the reference you attribute it to, alongside the snippet and term
checks in the workflow above.

```bash
just prose-figure-audit                        # whole KB census (~2 min, offline)
just prose-figure-audit --dr-only --format list
just prose-figure-audit kb/disorders/Asthma.yaml --format list
```

The audit reports percentages, `1 in N`, per-100,000 rates and `N-fold` figures
that do not appear in the references cited *beside* them. Two things it is not:

- **It is advisory, not a gate.** It is heuristic, is not in `just qc`, and is
  not wired into CI. Derived figures are legitimate (a curator may convert
  1-in-25,000 to 4 per 100,000; the common conversions are handled, arithmetic in
  general is not), and not every real source is cached prose.
- **`OK` is not verification.** Finding the number in an adjacent abstract says
  nothing about whether it was that percentage *of that thing*. Only reading the
  source settles it — which is exactly the point of the failure mode.

## Finding a cache file

A cache filename is the reference id with `:`, `/`, `?` and `=` replaced by `_`,
plus `.md`. **The prefix keeps the identifier's own casing — it is not
uppercased.** `PMID:29167994` caches as `PMID_29167994.md`, but
`clinicaltrials:NCT05813288` caches as `clinicaltrials_NCT05813288.md`, so a
glob for `CLINICALTRIALS_*` finds nothing. Searching `pmid_*` on a
case-sensitive filesystem is the mirror of the same mistake.

Do not hand-derive the path when a tool will do it. `resolve_cache_path` in
`src/dismech/reference_snippet_audit.py` is the authority, and it also resolves
a bare identifier (`NCT06087757`) back to its prefixed file. Prefer the recipes
that take a reference id or a KB file:

```bash
just fetch-reference PMID:29167994     # fetch or regenerate the cache entry
just count-verified-snippets kb/disorders/Asthma.yaml
```

When you do need to glob, match case-insensitively and on the tail rather than
guessing a prefix:

```bash
ls references_cache/ | grep -i "_29167994"
```

The prefixes in use, with the count of cached records at the time of writing —
mixed case is normal and none of it is a typo:

| Prefix | Cached | What it is |
|---|---:|---|
| `PMID` | 35586 | PubMed |
| `DOI` | 6056 | DOI-only literature |
| `clinicaltrials` | 1082 | ClinicalTrials.gov (NCT) |
| `NCIT` | 796 | NCI Thesaurus predicate edges |
| `ICEES` | 505 | ICEES KG comorbidity pairs |
| `CGGV` | 502 | ClinGen gene-disease validity |
| `ORPHA` | 347 | Orphanet |
| `GEO` | 176 | Gene Expression Omnibus |
| `url` | 116 | Web page |
| `MYGENESET` | 100 | MyGeneset |
| `STRCHIVE` | 73 | STRchive |
| `PPR` | 25 | Europe PMC preprint |
| `CIVIC` | 15 | CIViC assertions and evidence |
| `ICTRP` | 7 | WHO ICTRP (non-NCT trial registries) |
| `file` | 5 | Local document |
| `CGDS` | 3 | ClinGen dosage sensitivity |
| `METABOLIGHTS` | 2 | MetaboLights |
| `MGNIFY` | 1 | MGnify |

The list is a snapshot for orientation, not a closed set — a new structured
source adds a prefix. Regenerate it with
`ls references_cache/ | sed 's/_.*//' | sort | uniq -c | sort -rn` rather than
trusting these counts.

## Empty caches (`content_type: unavailable`)

The fetcher writes `content_type: unavailable` into a cache file's frontmatter
when it found the record but retrieved no text a snippet could quote: no
abstract and no full text. The file still has a title, authors and journal, and
the fetch still reports "Successfully cached". A real abstract is
`abstract_only`; full texts are `full_text_xml`, `full_text_pdf` and similar.
Go by that field, not by how short the body looks: structured caches (ORPHA,
ClinGen) and records with no `## Content` heading, such as `PMID:31909928`, are
short and fully quotable.

**An empty cache describes one fetch, not the paper.** `PMID:33054089` came back
`unavailable` and was refetched an hour later as `full_text_xml` from PMC. So
the first step is a retry, especially for an open-access paper:

```bash
scripts/run_reference_validator.sh cache reference PMID:12345678 --force
```

`just fetch-reference` prints a warning to stderr when the file it leaves behind
is `unavailable`. The warning is advisory: the file is kept and the exit code is
unchanged. When you write a note about such a paper, say that no quotable text
was retrieved on the fetches you made, not that the record cannot be quoted; the
next curator's fetch may succeed.

**If it stays empty, nothing in it can be a snippet.** A title is not a finding,
and a sentence recalled from the paper is not a quote from the cache. Say in
`notes` why it is not cited as evidence, and optionally also list it as a
top-level `references:` entry with no snippet. The worked
example is the "Not cited, and why." paragraph in the `notes` of
`kb/disorders/Distal_Hereditary_Motor_Neuronopathy_Type_9.yaml`: two papers on a
further WARS1 family that cache with no abstract text are named there as leads
for a curator with full-text access, and no evidence item cites them.

To see the whole backlog:

```bash
just list-empty-reference-caches                # summary by identifier prefix
just list-empty-reference-caches --format tsv   # one row per record
just list-empty-reference-caches --no-kb        # skip the kb/ citation lookup
```

It splits records by `full_text_attempted: true` (the full-text route was tried
and found nothing) versus no such marker (never retried under that route, so a
`--force` refetch is the obvious first move), counts how many are cited anywhere
in `kb/`, and names any that an evidence item with a `snippet:` cites. That last
count should be zero. The recipe is a read-only triage view and always exits 0.

## `abstract_only` is also one fetch, not the paper

The rule above generalizes one tier up, and this is the tier that catches
people, because nothing looks wrong. An `abstract_only` cache has a title,
authors, journal and a real abstract, and snippets quoting it verify. It is
still only a record of what one fetch retrieved, and a re-fetch can upgrade it.

**Which command you need depends on one frontmatter field.** Read
`full_text_attempted` before re-fetching, because the two cases take different
commands and the plain one silently does nothing in the second:

| Frontmatter | What a plain `just fetch-reference` does |
|---|---|
| no `full_text_attempted` | re-runs the full-text chain, and can upgrade the cache |
| `full_text_attempted: true` | **nothing** — the retry is skipped; you need `--force` |

```bash
grep -E '^(content_type|full_text_attempted):' references_cache/PMID_22771891.md

# never attempted: the plain fetch is enough
just fetch-reference PMID:22771891
#   Content type: full_text_xml
#   Content length: 42746 characters

# already attempted: force a real refresh
scripts/run_reference_validator.sh cache reference PMID:12345678 --force
```

The skip is deliberate, not a bug: `_maybe_retry_full_text` in the validator's
fetcher returns the record untouched when `full_text_attempted` is set, so a
clean negative result is not re-queried on every later run. The census's own
split matters here — of its 8,482 recoverable files, **2,610 carry
`full_text_attempted: true`** and will not budge for a plain re-fetch, which is
also why that subset is the closest thing to a list of papers stranded by the
#10876 extractor bug.

`--force` is not simply the stronger option. It replaces cached text with
whatever the refresh returns, so on a source that now serves less than it did,
it loses text rather than gaining it. Prefer the plain fetch where the
frontmatter says it will work.

**After a `--force`, read the diff before committing.** A shortened body is the
documented failure mode, not a hypothetical: in #12879 a re-fetch returned 64
caches **5,360 lines shorter** than the committed ones and broke snippets that
had verified moments earlier, in a PR whose subject was something else
entirely. That issue is also where a fetch came back as an anti-bot page and
was cached and compared as though it were the article — the same "HTTP 200 is
not retrieval" trap, from inside this repository.

```bash
git diff --stat references_cache/        # insertions should not be mostly deletions
```

A re-fetch that *shrinks* a file can still be legitimate: the current extractor
writes a cleaner body than older ones did, so a file can lose a duplicated
abstract and keep every quotable sentence. The test is whether the snippets
still verify, not whether the file got smaller:

```bash
just count-verified-snippets kb/disorders/<Entry>.yaml
```

**This is measured, not anecdotal.** The census in
[`docs/reports/abstract-only-recovery-census-2026-09-16.md`](../../../docs/reports/abstract-only-recovery-census-2026-09-16.md)
(issue #10878) found 8,482 `abstract_only` caches — 26.7% of them — with a real
body recoverable through the production extractor, and 5,809 that would gain at
least one table. So the odds that a given `abstract_only` cache is hiding full
text are roughly one in four.

```bash
just abstract-only-recovery-census                  # offline table census (seconds)
just abstract-only-recovery-census --phase all      # network phases, resumable, hours
```

**Refetch the paper you need; never bulk-refetch the backlog.** #10878 declined
a blanket refetch on purpose: rewriting thousands of `references_cache/` files
in one PR is the merge-invisible failure shape that #8623 and #10061 document,
and every open curation PR touching one of those files would go quietly wrong on
merge. A single-file refetch because you need a number is the sanctioned move;
batching the rest is a maintainer call, and the report names the two batching
axes.

**Re-fetch whenever the fact you need lives in a table or a figure.** An
abstract can never carry a table row, so a number sourced to "Table 2" is not
checkable against an `abstract_only` cache no matter how carefully you read it.
`PMID:22771891` is the worked case: the cache was `abstract_only`, the abstract
says only that HOG "was confirmed in the urine, sera and liver samples from PH3
patients", and the concentrations a reviewer needed were in Table 2. One
`fetch-reference` brought back `full_text_xml` carrying Table 2 verbatim as a
markdown table, so those values became quotable snippets and the check went
offline for everyone.

**Reach for the repository's fetcher before any external full-text route.** On
that paper, four outside routes were tried first — the NCBI BioC endpoint,
Europe PMC `fullTextXML`, a PubMed MCP full-text call, and the PMC PDF URL —
and a review note was written saying the values "could not be verified" while
`just fetch-reference` returned them first time. The fetcher is
not only the sanctioned way to *write* a cache file; it is usually the best way
to *read* a paper.

**An HTTP 200 does not establish retrieval.** `pmc.ncbi.nlm.nih.gov/articles/<PMCID>/pdf/<file>.pdf`
answers 200 with a 21 KB reCAPTCHA challenge page whose title is "Checking your
browser", and the article page does the same. Check the body, not the status
code — the same trap CLAUDE.md records for the ICTRP portal's "not found" page.

**Figure captions do not come through the XML route.** The same refreshed cache
carries every table and no caption, so a kinetic constant printed in a figure
legend stays uncheckable from the cache even at `full_text_xml`. When a number
you need is in a caption, say in `notes` where it lives rather than implying the
cache supports it.

### Do not commit a publisher PDF

Reading a paper on PMC is not permission to redistribute it. An NIH Public
Access author manuscript carries the publisher's copyright — `nihms-393374.pdf`
for `PMID:22771891` is stamped "© 2012 Elsevier B.V. All rights reserved" — and
sits outside the PMC open-access subset, which is the redistributable tier.
`references_cache/files/` is gitignored for exactly this class of file, so
placing a PDF anywhere else in the tree routes around an existing decision.

What the repository does deposit is fetcher-generated extracted text: tens of
thousands of `references_cache/*.md` files, thousands of them `full_text_xml`,
`full_text_pdf` or `full_text_html`. That is the deposit route. A PDF a user
hands you is fine to read and quote in the session; the way to make its content
durable is `just fetch-reference`, never a commit of the file or a hand-written
cache entry.

## Reference-cache integrity

Check the derived cache structure with:

```bash
just check-reference-cache-frontmatter
just check-reference-cache-nul-bytes
```

If an entry is malformed or incorrect, regenerate it with
`just fetch-reference <ID>`; never patch its filename, frontmatter, or content.

The one exception is a NUL byte. If `just check-reference-cache-nul-bytes` fails,
run `uv run python scripts/repair_reference_cache_nuls.py --apply` and commit the
result. Do not re-fetch: the PDF extractor writes an unmapped glyph (usually an
`fi`/`fl` ligature) as `\x00`, so a re-fetch writes the same NULs back
(#12543, linkml/linkml-reference-validator#100).

## Never patch the validator from inside dismech

`linkml-reference-validator` (LRV) is used as a library, as-is. dismech does not
patch it, wrap it, or reimplement any part of it, and
`tests/test_upstream_validator_behaviours.py` fails if a patch module reappears
or if anything imports one.

This is worth stating because the repository spent months doing the opposite.
`src/dismech/patch_reference_validator.py` grew to 650 lines that replaced nine
private LRV methods at import time — how the fetcher named cache files, parsed
JATS tables, quoted YAML, coerced authors. Every one of those was a real bug with
a correct fix, and the patch made each of them invisible to the only project that
could fix it properly. The costs compounded:

- **The fix never reached anyone else.** Nine defects were fixed for dismech and
  for nobody else using LRV.
- **It broke on contact with an upgrade.** Patching a private method means
  depending on its signature. When LRV changed one, `just validate-kb-references`
  died at import with `AttributeError: 'function' object has no attribute
  '__func__'` — the gate, not a test.
- **It hid the upstream problem from tests.** dismech's suite tested the patch,
  so it stayed green while the thing it was patching was still broken.

All twelve are now fixed in LRV -- #66-74, #85, #87, #88, and finally #92 and
#93, which closed the two that were real upstream gaps rather than workarounds
(the URLSource HTML sanitization and the PDF-URL title). Both were filed rather
than quietly kept, and both are gone from here now that 0.3.0 carries the fixes.

Two of the twelve arrived the same way the others did -- a curation PR adding a
patch as a side effect of curating a disease, noticed only during an unrelated
rebase. That is what the guard in
`tests/test_upstream_validator_behaviours.py` exists to catch.

**If you genuinely must patch, the patch is temporary and the issue is filed
first.** Open the upstream issue before writing the patch, name that issue in a
comment at the patch site, and test the *behaviour* you need rather than the
patch itself — a behaviour test keeps passing when the fix lands upstream and the
patch comes out, which is exactly when you want to find out it is redundant.
`tests/test_upstream_validator_behaviours.py` is the worked example: each test
names the upstream issue it pins, and none of them reference a patch.

A bug worth working around is a bug worth reporting.
