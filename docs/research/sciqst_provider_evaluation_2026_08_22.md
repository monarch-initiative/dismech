# Sciqst as a deep-research provider — evaluation (2026-08-22)

**Verdict: do not adopt as a primary deep-research provider — but there is a free
corpus of 2,078 public reviews, 338 of which name a dismech disease, and those
are worth a look as leads.**

Sciqst reviews are short by construction (corpus median 7 references, hard
maximum 23 across all 2,078), and there is no API. That rules it out as a
substitute for Falcon/Edison, Asta or OpenScientist. It does not rule out mining
the existing free corpus, which costs nothing and is the subject of the second
half of this page.

## What it is

[Sciqst](https://www.sciqst.com/) (ByronInsight AG, Switzerland) generates
literature reviews from PubMed on a posed question. Freemium: 6 free credits,
then one-time credit packs from $5. Reviews can be public or private; public ones
are server-rendered at `https://www.sciqst.com/reviews/<id>` with title, abstract
and inline PMIDs all present in the HTML, and are listed in
[`sitemap.xml`](https://www.sciqst.com/sitemap.xml). The landing page cites MIT,
Charité, Novartis, Roche, AstraZeneca and USZ as institutional users (the ToS
notes these free institutional credits "[do] not signify a formal contractual
relationship with the aforementioned institutions").

`robots.txt` opts model-training crawlers out (`GPTBot`, `ClaudeBot`,
`Google-Extended`, `CCBot`) while explicitly allowing search and user-requested
retrieval, with `Allow: /` for everything except a handful of app endpoints. The
survey below is user-requested retrieval of sitemap-listed public pages.

## Corpus survey (n = 2,078 public reviews)

Method: `sitemap.xml` → 2,078 `/reviews/<id>` URLs (plus 1,895 public mindmaps,
not examined) → fetch each → extract `og:title`, meta description, and all
inline PMIDs. Matching against dismech used the 2,128 `kb/disorders/` names and
1,831 `stubs/` labels, restricted to names ≥10 characters to suppress junk hits.
Results are in
[`sciqst_dismech_review_matches_2026_08_22.tsv`](sciqst_dismech_review_matches_2026_08_22.tsv).

### Reference count is the real, durable limitation

| References | Reviews |
|---|---|
| 0 | 2 |
| 1–5 | 451 |
| 6–10 | 1,361 |
| 11–15 | 234 |
| 16–25 | 30 |
| 26+ | **0** |

Median 7, mean 7.4, maximum 23. **No review in the entire public corpus cites
more than 23 papers.** Against the providers dismech already uses (median
`citation_count`): openai 98, perplexity 51, openscientist 34, falcon/edison 31,
claude_code 23, asta 20. Sciqst's *maximum* is the median of our weakest
mainstream provider. A dismech disease entry routinely needs 30–60 distinct
citations across pathophysiology, phenotypes, genetics and treatment; a
7-reference review cannot carry one.

### Correction: the recency restriction is NOT general

An earlier draft of this evaluation claimed Sciqst "structurally cannot reach"
pre-2022 literature, generalizing from three reviews found via web search whose
PMIDs were all ≥38.8M. **That generalization was wrong.** Across the full corpus,
by the oldest paper each review cites:

| Oldest cited paper | Reviews | Share |
|---|---|---|
| pre-2000 (<11M) | 51 | 2.5% |
| 2000–2008 (11–20M) | 215 | 10.4% |
| 2008–2022 (20–35M) | 494 | 23.8% |
| 2022–2024 (35–38M) | 252 | 12.1% |
| 2024+ (≥38M) | 1,064 | 51.3% |

So about half the corpus is recency-only, and the other half reaches back —
36.7% cite something pre-2022, 12.9% something pre-2008. Individual reviews cite
papers from 1997–2004 freely. The three search-surfaced samples happened to fall
in the recency-only half. Reference *count*, not literature age, is the binding
constraint.

## The free corpus: what actually overlaps with dismech

**338 of the 2,078 reviews name a dismech disease** — 329 matching a curated
`kb/disorders/` entry, 9 matching an uncurated `stubs/` disease.

The catch is topical. Classifying the 338 by title:

| Orientation | Count | Share |
|---|---|---|
| clinical / therapeutic (management, efficacy, dosing, X vs Y, guidelines) | 145 | 43% |
| other / descriptive | 116 | 34% |
| mixed mechanism + clinical | 46 | 14% |
| **mechanism-leaning** | **31** | **9%** |

Sciqst's user base is evidently writing *clinical practice* questions — "Optimal
NOAC Selection for Elderly Frail Patients with Atrial Fibrillation", "Comparative
Efficacy and Safety of Apixaban Versus Rivaroxaban", "Permissive Hypercapnia".
dismech is a pathophysiology knowledge base. So the effective yield is not 338
but roughly the 31 mechanism-leaning reviews plus the better half of the 46
mixed — call it 40–50 reviews of plausible interest, each carrying ≤13
references.

Best of the mechanism-leaning set:

| Refs | dismech entry | Review |
|---|---|---|
| 13 | Glomerulonephritis | Mechanisms of Albuminuria in Diabetic Nephropathy |
| 12 | Metabolic Dysfunction-Associated… | Incretin-Based Therapies for MASLD |
| 11 | Non-Small Cell Lung Cancer | Mechanisms of Osimertinib Resistance in NSCLC |
| 10 | Optic Neuritis | Mechanistic Insights and Clinical Implications of Ethambutol… |
| 10 | Brucellosis | Brucellosis: Epidemiology, Pathogenesis, and Prevention |
| 9 | IgA Nephropathy | Advances in Understanding and Managing IgA Nephropathy |
| 8 | Polycystic Ovary Syndrome | Complex Pathophysiology of PCOS |
| 8 | Hemochromatosis | Genetic and Clinical Insights into Hereditary Hemochromatosis |
| 8 | ADPKD | Advances in Understanding ADPKD |
| 7 | Keratoconus | Advances in Understanding the Pathophysiology of Keratoconus |

### The 9 that hit the uncurated stub queue

These are the most interesting, because they cover diseases dismech has *not*
curated — a free head start rather than a duplicate:

| Refs | Stub disease | Review |
|---|---|---|
| 17 | interstitial cystitis | [Advances in Understanding and Treating Interstitial Cystitis/BPS](https://www.sciqst.com/reviews/blD2jv15tSEk) |
| 12 | myelofibrosis | [Advancements in the Management of Myelofibrosis: From JAK Inhibitors…](https://www.sciqst.com/reviews/NNnZoytcsArD) |
| 10 | trigeminal neuralgia | [Advances in Balloon Compression Techniques…](https://www.sciqst.com/reviews/eSexu_aPYZdX) |
| 9 | Muckle-Wells syndrome | [Muckle-Wells Syndrome: Current Insights and Future Directions](https://www.sciqst.com/reviews/UR7W72h-38nY) |
| 8 | X-linked hypophosphatemic rickets | [Comprehensive Insights into X-linked Hypophosphatemic Rickets](https://www.sciqst.com/reviews/PTAd9ybXlLzV) |
| 7 | pheochromocytoma | [Metastatic Pheochromocytoma: Advancements and Challenges](https://www.sciqst.com/reviews/MBFqX6jSLv7K) |
| 7 | pheochromocytoma | [Biochemical Screening for Pheochromocytoma](https://www.sciqst.com/reviews/W7iakmRKF6IB) |
| 3 | pancreatitis | [The Role of Antibiotics in the Management of Pancreatitis](https://www.sciqst.com/reviews/WfYrk1_UhsSJ) |
| 1 | trigeminal neuralgia | [The A931T Variant in the TRPM7 Channel](https://www.sciqst.com/reviews/q89f9xkknzZm) |

The interstitial cystitis review (17 references) is the single largest
dismech-relevant item in the corpus and the obvious one to try first. Note
`X-linked hypophosphatemic rickets` is a live conformer target for the
`defective_skeletal_mineralization` module, so that one has a concrete home.

## Integration blockers (unchanged)

- **No API, no docs, no export.** dismech generates reports through
  `deep-research-client` (pinned `>=0.2.10`); a `just research-disorder sciqst
  <Disease>` recipe needs a provider adapter *upstream*, and there is no
  documented interface to write one against. Capture must be manual, in the shape
  of the existing `manual` provider slug.
- **The search is not disclosed.** No PubMed query, keyword set, or date range
  appears on a review page; the only metadata is a timestamp and "A generated
  literature review based on recent scholarly papers". No model is named.
- **Provenance is third-party.** A public review was generated by some other
  user, for their question, with settings we cannot see. That is weaker
  provenance than any report in `research/` today, all of which we ran ourselves.
- **ToS.** Silent on automated access and on accuracy. It permits claiming
  authorship of a generated review "permitted that it does not violate any
  existing copyrights", forbids implying anyone other than the member created or
  endorsed it, and grants ByronInsight a "limited, non-exclusive, worldwide,
  fully paid, perpetual, irrevocable, transferable right and license to use…Your
  Content". Nothing blocks *reading* a public review and following its PMIDs;
  re-publishing someone else's generated review into `research/` is a different
  act and is not clearly licensed.

## Recommendation

1. **Do not register `sciqst` in `DEEP_RESEARCH_PROVIDERS`** and do not commit
   third-party reviews into `research/`. The provenance and licensing are wrong
   for that, and a registry entry drives a legend and filter chip on the public
   research index.
2. **Treat the 338 matched reviews as a PMID lead list, nothing more.** The
   useful content of a Sciqst review, for us, is its reference list — its own
   entries are PMID + title with no abstract text, so a curator must fetch the
   real abstract anyway. Following a lead costs one `just fetch-reference` call
   and carries no provenance debt.
3. **Start with the interstitial cystitis and Muckle-Wells reviews** if anyone
   wants to test the value of the lead-list idea on an uncurated disease.
4. Standard discipline applies unchanged and non-negotiably: every PMID
   re-fetched with `just fetch-reference`, every snippet verified with
   `just count-verified-snippets`, every ontology term through
   `just validate-terms`.

## What would change the verdict

1. A documented API or bulk export.
2. Reference counts in the 25+ range — currently impossible; 23 is the observed
   corpus ceiling.
3. A disclosed, controllable PubMed query. The site advertises "customizable
   PubMed search keywords" behind login; if that also lifts the result-count cap,
   the central objection here weakens. Testing it needs an account with credits,
   which this evaluation did not have.

Item 2 is the blocker. Items 1 and 3 would not matter if reviews stay at 7
references.
