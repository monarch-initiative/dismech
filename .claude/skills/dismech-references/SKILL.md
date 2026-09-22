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

Classify `evidence_source` by the evidence the quoted text describes, not by
the curator. When that evidence differs from the citing paper's own study,
record its provenance with `quote_role`:

- `HUMAN_CLINICAL`: patients, cohorts, clinical observations, or trials
- `MODEL_ORGANISM`: in vivo non-human animal or organism work
- `IN_VITRO`: cells, organoids, explants, or biochemical assays
- `COMPUTATIONAL`: modeling, simulation, or in-silico analysis
- `OTHER`: evidence that does not fit the categories above

Read [evidence semantics](references/evidence-semantics.md) when assigning or
reviewing `supports`, `directness`, `quote_role`, or `evidence_source`. These
axes describe different claims; optional assessments stay absent until assessed.

Read [structured sources](references/structured-sources.md) for ORPHA, ClinGen,
ICEES, NCIT, and other generated database records, including refresh/repin
procedures. For dataset accessions use [dataset curation](../../../docs/dataset-curation.md);
for trial registries use `medical-action`.

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

Interpret the result as follows:

- `PASS`: proceed to normal source, snippet, and term verification.
- `WARN`: resolve the reported conflict or degraded lookup, then manually check
  the causal gene, OMIM xref, and synonyms.
- `FAIL`: discard the report. Do not cherry-pick from it.
- `SKIP`: the automated check cannot discriminate; manually check disease
  identity before proceeding.

For a `WARN` or `SKIP`, inspect the intended MONDO record directly:

```bash
uv run runoak -i sqlite:obo:mondo info MONDO:XXXXXXX -O obo
```

Compare its causal-gene relationship (`RO:0004003`), OMIM xref, and synonyms
with the report. Look specifically for synonym aliasing, eponymic collision,
abbreviation ambiguity, or conflation with a closely related disease. On any
identity mismatch, discard the report rather than cherry-picking from it.

See `docs/deep-research-reference-validation.md` and
`research/nec_risk_disease_classes.md` for uncommon cases.

### 2. Fetch each new reference

```bash
just fetch-reference PMID:12345678
```

Use the actual identifier for other supported reference types. Read the fetched
record and confirm its identity, topic, and quoted passage. A successful fetch
does not prove that the source supports the claim.

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

After a tranche, run the applicable [offline gates](references/validation-gates.md).
That guide includes evidence waivers and gate-specific recovery.

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

**Prefer ASCII in new snippets** — an invisible character in a quote is a trap
for the next curator, and it buys nothing, since the source's typography folds
anyway. Existing snippets that copied the source's thin spaces and en dashes
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
`scripts/find_missing_reference_titles.py` is the complementary check for
*absent* titles.

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

## Reference-cache integrity

Check the derived cache structure with:

```bash
just check-reference-cache-frontmatter
```

If an entry is malformed or incorrect, regenerate it with
`just fetch-reference <ID>`; never patch its filename, frontmatter, or content.

Before pruning uncited reference caches, re-derive the cited identifiers from
the final entry; an earlier list becomes stale as soon as evidence changes.
Re-run `just count-verified-snippets` on the pushed tree and re-read any notes
calling a removed source cached. Full validation can silently fetch a missing
cache, so a passing network-enabled run does not prove the cache was committed.
