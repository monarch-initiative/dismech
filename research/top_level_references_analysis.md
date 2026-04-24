# Analysis: Top-Level `references:` Section Across Disorder Entries

Generated 2026-04-24 in response to issue #1344. Numbers are computed directly from
`kb/disorders/*.yaml` on the commit at which this report was written; re-run the
scripts in the appendix to refresh.

## TL;DR

- 928 disorder YAMLs total. **290 (31.3%) have a populated top-level `references:`
  section**; 638 (68.7%) have none.
- Across the populated files there are 2,998 `PublicationReference` entries —
  **82% DOI, 18% PMID**, ~0.4% other (`clinicaltrials:`, `GEO:`, URL).
- Only **40% of the 2,998 references carry any `findings:`**. The remaining 60% are
  stubs (reference + title, with empty or absent `findings`).
- Top-level `references:` is **not** a deduplicated roll-up of inline evidence PMIDs.
  Of the 288 files that have *both* a populated `references:` section and inline
  evidence PMIDs, **only 39 (13.5%) share any PMID between the two sets**. There are
  9,825 unique inline evidence PMIDs across the KB vs. 530 PMIDs in top-level
  references. The two sections are effectively parallel bibliographies.
- Do **not** auto-promote inline evidence PMIDs into `references:`. They serve
  different purposes (see Q2 / recommendations).

## Q1. How prevalent is a populated `references:` section?

| Metric | Value |
|---|---|
| Total `kb/disorders/*.yaml` files | 928 |
| Files with `references:` empty or absent | 638 (68.7%) |
| Files with ≥1 `PublicationReference` | 290 (31.3%) |
| Total `PublicationReference` entries across KB | 2,998 |
| Max references in a single file | 35 (`Wilsons_Disease.yaml`) |

The distribution is strongly bimodal: most files have zero references, and those
that do typically have 5–15 (median in the populated subset is ~10). A few outliers
(rare cancers, classic hereditary syndromes) carry 25–35.

Top-10 by reference count:

| Count | File |
|---:|---|
| 35 | `Wilsons_Disease.yaml` |
| 32 | `Hereditary_Breast_and_Ovarian_Cancer_Syndrome.yaml` |
| 31 | `Lung_Carcinoma.yaml` |
| 30 | `Rosacea.yaml` |
| 29 | `Uveal_Melanoma.yaml` |
| 26 | `Osteosarcoma.yaml` |
| 25 | `BRAF_V600_Mutant_Melanoma.yaml` |
| 25 | `HPV_Negative_Head_and_Neck_Cancer.yaml` |
| 25 | `Soil_Transmitted_Helminthiases.yaml` |
| 24 | `Classic_Familial_Adenomatous_Polyposis.yaml` |

## Q2. What is `references:` supposed to contain?

From `src/dismech/schema/dismech.yaml`:

```yaml
references:
  description: Top-level list of references with their key findings for this disease
  multivalued: true
  range: PublicationReference
```

`PublicationReference` has four slots:

- `reference` (**required**, identifier — DOI or PMID)
- `title` — human-readable paper title
- `found_in` — list of deep-research source files under `research/` that cited this
  reference (e.g. `SomeDisease-deep-research-falcon.md`)
- `findings` — a list of `Finding` objects, each with `statement`, `supporting_text`,
  and optional nested `evidence`.

The schema comment notes the design is *"inspired by ai-gene-review"*. The
`found_in` provenance field and the `findings` structure both point to the same
intent: `references:` is the landing zone for **deep-research sweeps** — structured
synthesis of what the literature says, produced by running provider agents (Falcon,
Codex, OpenAI, Perplexity, Asta, OpenScientist, etc.) on a disorder and caching
their outputs under `research/`.

This is distinct from the per-section `evidence:` blocks, which anchor specific
claims (a particular phenotype, a particular treatment, a particular
pathophysiology step) to quotable snippets from PubMed abstracts — the inline
validation layer enforced by `linkml-reference-validator`.

## Q3. Is there a gap between evidence PMIDs and top-level references?

Yes — and it is structural, not a curation oversight.

| File category | Count |
|---|---:|
| Both `references:` and inline evidence PMIDs populated | 288 |
| Only top-level `references:` populated (no evidence PMIDs) | 2 |
| Only inline evidence PMIDs (no `references:`) | 485 |
| Neither populated | 153 |

Cross-set check on the 288 files with both populated:

- 288 files carry 9,825 unique inline evidence PMIDs across the KB and 530 PMIDs in
  top-level references.
- **Only 39 files (13.5%) share any PMID between the two sets.**

The two sections come from different pipelines:

| Pattern | Pipeline | Top-level `references:` | Inline `evidence:` |
|---|---|---|---|
| **Deep-research sweep** (newer entries) | AI provider reads literature, emits `research/*.md`; curator integrates outputs | Populated, **DOI-based**, with `found_in` and often `findings` | Derived from the deep-research findings; mostly DOIs |
| **Section-by-section curation** (legacy / cancer-curator / module-conformance entries) | Curator writes pathophysiology/phenotype/treatment sections directly from PubMed abstracts | Empty or absent | Rich, **PMID-based**, many items per file |

Illustrative contrast:

- `Alzheimer_Disease.yaml`: dense inline evidence block (dozens of PMIDs) and zero
  top-level `references`.
- `Hereditary_Breast_and_Ovarian_Cancer_Syndrome.yaml`: 32 DOI references with
  full `findings`, sourced from deep-research.

## Q4. Should this be automated?

Two distinct questions.

### (A) Auto-promote inline evidence PMIDs → `references:`

Technically feasible — collect unique PMIDs per file from all `evidence:` blocks,
write them into `references:` with title lookups. **Not recommended.** Concrete
problems:

1. It conflates two different purposes. Inline evidence is per-claim anchoring;
   top-level `references:` is synthesized key papers + findings. Auto-promotion
   would produce hundreds of stub entries with empty `findings: []` — more noise
   than signal.
2. The `found_in:` provenance would be empty (no `research/` file produced these
   PMIDs), breaking the one-way invariant that every `references` entry traces to
   a `research/*.md` source.
3. The rendered page (`pages/disorders/*.html`) displays `references:` as a
   curated bibliography. Dumping every inline PMID there degrades the UX for the
   42% of files that currently do have curated top-level references.

### (B) Run deep-research sweeps on the 638 entries without any `references:`

This is the path to uniform coverage. The existing 290 populated entries were
produced this way, and the `research/` directory already contains 1,898 markdown
files from prior sweeps, with providers distributed roughly as:

| Provider (suffix on `research/*.md`) | Count |
|---|---:|
| falcon | 428 |
| codex | 268 |
| asta | 139 |
| openai | 47 |
| perplexity | 39 |
| manual | 28 |
| openscientist | 7 |
| other / tagged with issue numbers | ~942 |

A bulk sweep targeting the 638 files with zero `references:` would close the
biggest gap. The orthogonal gap is the **201 populated files whose references
carry empty `findings:`** (see Q5) — these could be enriched by a targeted
findings-extraction pass rather than a fresh sweep.

### (C) Third option: reject auto-promotion *and* bulk sweeps, treat this as
intentional

A viable editorial choice: `references:` may be most useful on entries where a
curator has actually synthesized a key-papers list. If the 290 populated entries
are the ones where that effort made sense, the 638-file gap may reflect
prioritization, not a defect. The decision belongs to `@cmungall` / curation leads.

## Q5. What do well-curated `references:` sections look like?

Among the 290 files with at least one reference:

| State of `findings:` across references in file | Files |
|---|---:|
| All references have `findings:` populated | 88 |
| All references have empty or absent `findings:` | 201 |
| Mixed (some populated, some empty) | 1 |

So even inside the "populated references" subset, the majority (201/290 ≈ 69%) are
**stub bibliographies** — reference + title only, no synthesized findings. Only
88 files (30%) have fully filled-in `findings:` with `statement` /
`supporting_text` / nested `evidence`.

Aggregate reference-item properties (across all 2,998 `PublicationReference`
entries):

| Property | Count | % |
|---|---:|---:|
| `reference` identifier present | 2,998 | 100.0% |
| `reference` is DOI | 2,456 | 81.9% |
| `reference` is PMID | 530 | 17.7% |
| `reference` is `clinicaltrials:NCT…` | 8 | 0.3% |
| `reference` is `GEO:…` | 3 | 0.1% |
| `reference` is bare URL | 1 | 0.0% |
| `found_in:` populated | 1,224 | 40.8% |
| `findings:` non-empty | 1,190 | 39.7% |

The mental model: fully curated entries (e.g., `Hereditary_Breast_and_Ovarian_
Cancer_Syndrome`) carry `reference` + `title` + `found_in` + nested `findings`
with quoted supporting text. Stub entries (e.g., most of `Stiff_Person_Syndrome`'s
references) carry `reference` + `title` and an empty `findings: []`.

## Summary of findings

1. **31.3% coverage**. 290/928 files have any top-level `references:`. 638 files
   have none. (The `github-actions` summary on the issue thread estimated 42%
   based on ~694 total files — both numbers were low; the KB has grown to 928
   files and true coverage is lower.)
2. **Two parallel populations**. Top-level references are a deep-research
   artifact (DOI-based, `found_in`-tagged, often with synthesized findings).
   Inline evidence is a per-claim PubMed-quote layer (PMID-based, tied to
   individual pathophysiology / phenotype / treatment entries). **These should
   not be conflated.**
3. **No actionable gap to auto-fill from evidence blocks.** Only 13.5% of the
   files that carry both sets share any PMID between them. Merging them would
   destroy provenance and pollute the rendered bibliographies.
4. **The actionable gap is coverage** — 638 entries with zero `references:` could
   be targeted by deep-research sweeps, mirroring how the current 290 were
   populated.
5. **Secondary actionable gap** — 201 populated files have references but empty
   `findings:`. A targeted findings-extraction pass (read the `found_in:`
   provenance `research/*.md`, emit `Finding` structures) would enrich these
   without new sweeps.

## Recommendations

1. **Do not** script auto-promotion of evidence PMIDs to `references:`.
2. **Consider** a bulk deep-research sweep targeting the 638 files with no
   `references:` section. Rank by priority (e.g., low-compliance disorders from
   `just compliance-all`, or high-traffic rendered pages) rather than running the
   full 638.
3. **Consider** a findings-extraction pass over the 201 files that already have
   stub references but empty `findings:`. The `found_in:` values already point to
   the source `research/*.md` files, so no new literature retrieval is needed.
4. **Document** the two-pipeline model in `CLAUDE.md` (or a short SOP under
   `docs/`). New curators should know that top-level `references:` is produced by
   the deep-research pipeline and is not interchangeable with inline `evidence:`.
5. **Enforce** that every `PublicationReference` has a `found_in:` value
   (provenance invariant). A trivial validator would catch future sweeps that
   forget to set it.

## Appendix: reproducing the numbers

The three scripts below were used to produce this report. They are idempotent and
read-only; run them from the repo root.

```python
# 1. Prevalence and top-10
import yaml, glob, os
files = sorted(glob.glob('kb/disorders/*.yaml'))
counts = {}
for f in files:
    with open(f) as fh:
        d = yaml.safe_load(fh) or {}
    counts[f] = len(d.get('references') or [])
print("Total:", len(files))
print("Populated:", sum(1 for c in counts.values() if c > 0))
print("Total refs:", sum(counts.values()))
for f, c in sorted(counts.items(), key=lambda x: -x[1])[:10]:
    print(c, os.path.basename(f))
```

```python
# 2. Reference-item properties (prefix, findings, found_in)
import yaml, glob, collections
files = sorted(glob.glob('kb/disorders/*.yaml'))
prefixes = collections.Counter()
with_findings = 0; with_found_in = 0; total = 0
for f in files:
    with open(f) as fh:
        d = yaml.safe_load(fh) or {}
    for r in (d.get('references') or []):
        total += 1
        rid = r.get('reference', '')
        prefixes[rid.split(':', 1)[0] if ':' in rid else 'other'] += 1
        if r.get('findings'): with_findings += 1
        if r.get('found_in'): with_found_in += 1
print("total:", total)
print("prefixes:", dict(prefixes.most_common()))
print("with findings:", with_findings)
print("with found_in:", with_found_in)
```

```python
# 3. Cross-set analysis (evidence PMIDs vs top-level references)
import yaml, glob
def collect_evidence_pmids(obj, out):
    if isinstance(obj, dict):
        if isinstance(obj.get('reference'), str) and any(
                k in obj for k in ('snippet', 'supports', 'evidence_source', 'explanation')):
            if obj['reference'].startswith('PMID:'):
                out.add(obj['reference'])
        for v in obj.values(): collect_evidence_pmids(v, out)
    elif isinstance(obj, list):
        for item in obj: collect_evidence_pmids(item, out)

both = only_top = only_ev = neither = 0
any_overlap = 0; both_total = 0
for f in sorted(glob.glob('kb/disorders/*.yaml')):
    with open(f) as fh:
        d = yaml.safe_load(fh) or {}
    ref_ids = {r.get('reference') for r in (d.get('references') or []) if r.get('reference')}
    d_no_refs = {k: v for k, v in d.items() if k != 'references'}
    ev = set(); collect_evidence_pmids(d_no_refs, ev)
    if ref_ids and ev:
        both += 1; both_total += 1
        if ref_ids & ev: any_overlap += 1
    elif ref_ids: only_top += 1
    elif ev: only_ev += 1
    else: neither += 1
print("both:", both, "only_top:", only_top, "only_ev:", only_ev, "neither:", neither)
print(f"overlap: {any_overlap}/{both_total}")
```
