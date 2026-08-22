# Sciqst as a deep-research provider — evaluation (2026-08-22)

**Verdict: do not adopt as a primary deep-research provider.** Sciqst produces
short, recency-restricted reviews (6–11 references, essentially all from the
preceding 6–12 months) and exposes no API. It does not do the job Falcon/Edison,
Asta, OpenScientist and the other registered providers do for dismech curation.
There is a narrow niche where it could still earn a place — a *recent-literature
top-up* pass — described at the end.

## What it is

[Sciqst](https://www.sciqst.com/) (ByronInsight AG, Switzerland) generates
literature reviews from PubMed on a posed question. Freemium: 6 free credits,
then one-time credit packs from $5. Side feature: "medical mind maps". Reviews
can be public or private, and public ones are served at
`https://www.sciqst.com/<review title>` and are search-indexed. The landing page
cites MIT, Charité, Novartis, Roche, AstraZeneca and USZ as institutional users
(the ToS notes these free institutional credits "[do] not signify a formal
contractual relationship with the aforementioned institutions").

## Evidence: three public reviews sampled

| Review | Refs | PMID range | Body length |
|---|---|---|---|
| [Muckle-Wells Syndrome: Current Insights and Future Directions](https://www.sciqst.com/Muckle-Wells%20Syndrome:%20Current%20Insights%20and%20Future%20Directions%20in%20Research) | ~8 | 38808101–39334417 | — |
| [Uremic Syndrome: Pathophysiology, Clinical Manifestations…](https://www.sciqst.com/Uremic%20Syndrome:%20Pathophysiology,%20Clinical%20Manifestations,%20and%20Innovative%20Management%20Strategies) | 6 | 40951196–41148448 | — |
| [Mechanisms and Interventional Strategies in Renal Fibrosis: A Comprehensive Review](https://www.sciqst.com/%20Mechanisms%20and%20Interventional%20Strategies%20in%20Renal%20Fibrosis:%20A%20Comprehensive%20Review) | 11 | 38929126–39159720 | ~1,200–1,400 words |

Format positives, on dismech's terms:

- **Citations are inline PMIDs**, e.g. *"…have been associated with clinical
  manifestations in MWS, providing a genetic basis for disease presentation and
  progression (PMID 39201704; PMID: 39195255)."* That is directly compatible
  with our `reference: PMID:…` evidence model and with `just fetch-reference`.
- Claims carry per-sentence or per-clause citations rather than a bibliography
  dumped at the end.
- Section structure is mechanistic (the renal fibrosis review runs 20 headings,
  including pathway-level ones such as *Role of ISG15 and TGFβR1*, *m6A
  modification*, *lncRNAs and MicroRNAs*).

## The disqualifying finding: the literature window is wrong

Each sampled review's PMIDs span a window of only a few months, and every PMID
in all three is ≥ 38.8M — i.e. published in roughly the last 18 months.

Measured against what dismech's own DR corpus actually cites (33,048 `PMID:`
mentions across every report in `research/`):

| Publication era (PMID band) | dismech DR corpus | Sciqst sample |
|---|---|---|
| pre-2008 (<20M) | 13.8% | 0% |
| 2008–2022 (20–35M) | 46.7% | 0% |
| 2022–2024 (35–38M) | 12.1% | 0% |
| 2024+ (≥38M) | 27.5% | 100% |

**60.5% of the literature dismech curates from predates 2022. Sciqst cited none
of it.** The renal fibrosis review devotes a section to *Targeting TGF-β and
Related Pathways* while citing no foundational TGF-β fibrosis literature; the
Muckle-Wells review builds on NLRP3 without the 2001 CIAS1/NLRP3 discovery
papers. Disease *mechanism* — dismech's actual subject — is mostly established in
older literature, and a tool that structurally cannot reach it cannot anchor a
pathophysiology entry.

Reference count alone also places it at the bottom of the field. Median
`citation_count` for existing providers:

| Provider | n reports | median | min–max |
|---|---|---|---|
| openai | 36 | 98 | 8–165 |
| perplexity | 46 | 51 | 1–63 |
| openscientist | 107 | 34 | 1–85 |
| falcon/edison | 1262 | 31 | 3–90 |
| claude_code | 286 | 23 | 1–126 |
| asta | 186 | 20 | 5–65 |
| manual | 17 | 9 | 2–25 |
| cyberian-codex | 260 | 7 | 0–57 |
| **sciqst (sampled)** | 3 | **8** | 6–11 |

## Provenance and integration blockers

- **No API, no developer docs, no export.** Nothing on the site, in search, or in
  the ToS mentions programmatic access. dismech generates reports through
  `deep-research-client` (pinned `>=0.2.10`, an external PyPI package from
  monarch-initiative), so a `just research-disorder sciqst <Disease>` recipe would
  need a provider adapter *upstream* — and there is currently no documented
  interface to write one against. Capture would have to be manual, in the shape
  of the existing `manual` provider slug.
- **The search is not disclosed.** No PubMed query, keyword set, or date range
  appears on a review page; the only metadata is a timestamp
  (`Date 2025-11-06 01:41:18`) and the line "A generated literature review based
  on recent scholarly papers". No model is named. A report we cannot reconstruct
  the query for is weak provenance for `research/`.
- **ToS.** Silent on automated access and scraping; silent on accuracy
  disclaimers. It permits claiming authorship of a generated review "permitted
  that it does not violate any existing copyrights", forbids implying anyone
  other than the member created or endorsed it, and grants ByronInsight a
  "limited, non-exclusive, worldwide, fully paid, perpetual, irrevocable,
  transferable right and license to use…Your Content". Nothing there blocks
  committing a generated review into `research/`, but nothing affirmatively
  licenses it either.
- **NEC exposure is untested.** With no API there is no way to run a batch
  through `just preflight-dr`, and a 6-reference review gives that check very
  little gene-mention signal to work with — a `WARN` (below `--min-signal`)
  would be the likely verdict on most reports regardless of correctness.

## Where it could still earn a place

The recency bias that disqualifies it as a primary provider is exactly what the
`literature-scan` and `preprint-scan` workflows want: *what has appeared on this
disease since we curated it*. Sciqst is a competent, cheap, PMID-citing summary
of the last ~12 months.

If we want that, the low-cost path is **manual capture under a `sciqst` provider
slug**, mirroring the existing `manual` reports — save as
`research/<Disease>-deep-research-sciqst.md` with frontmatter of the form:

```yaml
---
provider: sciqst
model: n/a
cached: false
start_time: '...'
end_time: '...'
citation_count: 8
notes: >
  Recent-literature top-up generated via the Sciqst web UI (no API). Covers only
  the trailing ~12 months; NOT a substitute for a primary DR pass.
---
```

Registering `sciqst` in `DEEP_RESEARCH_PROVIDERS`
(`src/dismech/render.py`) plus `just gen-provider-docs` is a one-commit change,
but it is **deliberately not done here** — the registry drives a legend entry and
filter chip on the public research index, and adding one for a category with zero
reports is dead UI. Do it in the same PR as the first captured report.

Standard discipline is unchanged and non-negotiable for anything sourced this
way: every PMID re-fetched with `just fetch-reference`, every snippet verified
with `just count-verified-snippets`, every ontology term through
`just validate-terms`. Sciqst gives leads — its reference entries are PMID +
title only, with no abstract text — so snippets must be lifted from the real
abstract regardless.

## What would change the verdict

1. A documented API or bulk export.
2. A disclosed, controllable PubMed query — especially a settable date range that
   lifts the recency restriction. The site advertises "customizable PubMed search
   keywords" behind login; if that includes date bounds, the central objection
   here may be an artifact of the default settings on public reviews rather than
   a hard limit, and this evaluation should be re-run against a logged-in,
   date-unbounded query.
3. Reference counts in the 25+ range on a rare-disease prompt.

Item 2 is the cheapest to test and the most likely to move the answer. It needs
an account with credits, which this evaluation did not have.
