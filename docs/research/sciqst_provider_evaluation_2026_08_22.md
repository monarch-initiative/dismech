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

Method: `sitemap.xml` → 2,078 `/reviews/<id>` URLs (plus 1,894 public mindmaps,
surveyed separately below) → fetch each → extract `og:title`, meta description,
and all inline PMIDs. Matching against dismech used the 2,128 `kb/disorders/`
names and 1,831 `stubs/` labels, restricted to names ≥10 characters to suppress
junk hits. Results are in
[`sciqst_dismech_review_matches_2026_08_22.tsv`](sciqst_dismech_review_matches_2026_08_22.tsv)
(one row per matched review, with the topical `orientation` label used below).

**The ≥10-character filter makes 338 a lower bound.** It excludes 62 curated
entries — counted by filename stem, which is the key the matcher used; the same
cut over the entries' top-level `name:` field gives 60 — among them `Asthma`, `COVID-19`, `Epilepsy`, `Glaucoma`,
`Cholera`, `Dengue`, `Botulism`, `Chordoma`, `Glioma` — i.e. exactly the common
short names a clinical-question corpus is full of. The true overlap is larger
than 338, which shifts the yield arithmetic below but not the verdict: the
23-reference ceiling is the binding constraint and is independent of matching.

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
**36.6%** cite something pre-2022 and **12.8%** something pre-2008. (Denominator
2,076, not 2,078: two reviews cite nothing and so have no oldest paper. Both
figures are recomputed from the counts rather than summed from the rounded
shares above, which is where an earlier 36.7% / 12.9% came from.) Note the
PMID→year boundaries are approximate and the two lower ones run 1–2 years late:
20M is nearer early 2010 than 2008, and 11M nearer 2001 than 2000; the 35M/2022
and 38M/2024 boundaries are good. Individual reviews cite papers from 1997–2004
freely. The three search-surfaced samples happened to fall in the recency-only
half. Reference *count*, not literature age, is the binding constraint.

## The free corpus: what actually overlaps with dismech

**338 of the 2,078 reviews name a dismech disease** — 329 matching a curated
`kb/disorders/` entry, 9 matching an open `stubs/` entry (though most of those
stubs turn out to be stale; see below).

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

Best of the mechanism-leaning set. This is an **editorial pick, not a strict
top-10 by reference count** — it skips a 12-reference Cystic Fibrosis row and an
11-reference Hepatocellular Carcinoma row whose subjects (cystic lung disease
imaging, radiotherapy) are not mechanism content despite the classifier's label.
Re-cut it yourself from the `orientation` column:

| Refs | dismech entry | Review |
|---|---|---|
| 13 | Glomerulonephritis | Mechanisms of Albuminuria in Diabetic Nephropathy |
| 12 | Metabolic Dysfunction-Associated… | Incretin-Based Therapies for MASLD |
| 11 | Non-Small Cell Lung Cancer | Mechanisms of Osimertinib Resistance in NSCLC |
| 10 | Optic Neuritis | Mechanistic Insights and Clinical Implications of Ethambutol… |
| 10 | Brucellosis | Brucellosis: Insights into Epidemiology, Pathogenesis, and Public Health Implications |
| 9 | IgA Nephropathy | Advances in Understanding and Managing IgA Nephropathy |
| 8 | Polycystic Ovary Syndrome | Complex Pathophysiology of PCOS |
| 8 | Hemochromatosis | Genetic and Clinical Insights into Hereditary Hemochromatosis |
| 8 | ADPKD | Advances in Understanding ADPKD |
| 7 | Keratoconus | Advances in Understanding the Pathophysiology of Keratoconus |

### The 9 that hit the stub queue

These are the 9 rows that matched an open `stubs/` entry, covering 7 distinct
diseases. **Read the table with a caveat: only 3 of those 7 are genuinely
uncurated** — interstitial cystitis, trigeminal neuralgia and Muckle-Wells. The
other 4 diseases (5 of the 9 rows) are *stale stubs* whose disease has since been curated under a different name —
`pheochromocytoma` → `Pheochromocytoma_Paraganglioma.yaml`, `myelofibrosis` →
`Primary_Myelofibrosis.yaml`, `X-linked hypophosphatemic rickets` →
`X-Linked_Hypophosphatemia.yaml`, `pancreatitis` → `Chronic_Pancreatitis.yaml`
plus `kb/modules/pancreatitis_acinar_autodigestion.yaml`. That is the expected
drift CLAUDE.md describes, cleared by `just tidy-stubs --apply`; it is a
side-finding of this survey, not a problem with the corpus.

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

Interstitial cystitis, trigeminal neuralgia and Muckle-Wells are the genuinely
uncurated ones. The interstitial cystitis review (17 references) is the largest
item **in this stub subset** — corpus-wide the largest dismech-relevant match is
a 22-reference review, *The Impact of the COVID-19 Pandemic on Clostridioides
difficile Infection (CDI) Acquisition and Outcomes*, against the already-curated
`Clostridioides difficile Infection`. Note that `X-Linked_Hypophosphatemia` is
**already a worked conformer** of `defective_skeletal_mineralization` (it
declares both the phosphopenic-arm and mineralization-front nodes), not a
conformer target — another instance of the stale-stub drift above.

## The mindmap corpus (n = 1,865)

Sciqst also publishes 1,894 free "interactive AI mind maps" at
`/mindmaps/<id>` (the sitemap lists 1,895 entries, one of which is the index page). These are **not** a second form of literature review. Surveyed
the same way (1,865 parsed successfully; 29 fetch errors):

- **90,426 total nodes**, median 47 per map, range 9–182.
- **Zero citations. Corpus-wide, not a single mindmap cites a single PMID or
  DOI.** Reviews at least give you a reference list; mindmaps give you nothing to
  verify against.
- 71% are pure trees (`edges = nodes − 1`); the mean map has 1.01 edges beyond a
  spanning tree, i.e. occasional cross-links, no real graph structure.
- The graph is embedded in the page as a `var mindmapNodes` JSON array and
  rendered client-side with vis-network, so it is trivially extractable — each
  node carries `name`, `category`, `connections`, and fixed x/y coordinates.
- Only **73 maps** name a dismech disease (72 curated, 1 stub), and those are
  heavily duplicated — Heart Failure ×9, Atrial Fibrillation ×8, Long COVID ×4,
  Ischemic Stroke ×4. Versus 338 matching reviews, the mindmaps are a much
  thinner overlap. Rows are in
  [`sciqst_dismech_mindmap_matches_2026_08_22.tsv`](sciqst_dismech_mindmap_matches_2026_08_22.tsv).

### The disqualifying property: edges are untyped

A node's `category` records only its depth tier (`Main Topic`, `Subtopic`,
`Detail`, `Sub_Detail`, `Default`). Edges carry **no predicate at all**. The full
Osteoporosis map ([`IflXOSqUjp10`](https://www.sciqst.com/mindmaps/IflXOSqUjp10),
75 nodes) is a textbook chapter outline:

```
Osteoporosis
├── Definition
├── Causes ── Genetic Factors / Lifestyle Factors / Medical Conditions
│             └── Medications ── Bisphosphonates, Hormone Therapy
├── Symptoms ── Bone Pain / Fractures / Height Loss
├── Diagnosis ── Bone Density Test / X-rays / Blood Tests
├── Treatment ── Lifestyle Changes / Surgical Options
└── Prevention ── Calcium and Vitamin D / Exercise / Healthy Lifestyle
```

No RANKL, no osteoclast, no bone remodeling — nothing of what
`kb/modules/osteoporosis_bone_resorption.yaml` models (remodeling imbalance →
RANKL-driven osteoclastogenesis → increased resorption → impaired formation → net
bone loss). It also lists **bisphosphonates under "Causes"**, which is
backwards — they are the treatment. Uncited, so nothing catches it.

The best case is a map whose prompt explicitly asked for mechanism —
[*"What is the pathophysiology of left bundle branch block"*](https://www.sciqst.com/mindmaps/WwCi9y5pokG3).
It does contain a latent causal chain (`Delayed Ventricular Activation →
Asynchronous Contraction → Reduced Cardiac Output`). But the *same untyped edge*
also expresses `Left Bundle Branch Block → Symptoms → Fatigue` (manifestation)
and `→ Treatment → Medications → Beta Blockers` (treated-by). Causal,
manifestation and therapeutic relations are indistinguishable, and the deepest
tier is padding (`Beta Blockers → Reduce Heart Rate`, `Low Salt Diet`).

Only 13 of the 1,865 parsed maps have a mechanism word in the title at all.

Content is not as boilerplate as the Osteoporosis example suggests — 77.4% of the
49,351 distinct node labels appear in exactly one map, and only 10.6% of maps
carry four or more of `Definition/Causes/Symptoms/Diagnosis/Treatment/Prevention`.
The problem is not that maps are identical; it is that the relations are
unlabelled and the claims are unsourced.

### Contrast with a dismech pathograph

`pathographs/*.json` edges carry `predicate`, `causal_link_type`, and a
`description`, and nodes carry `meta.evidence` with resolvable references:

```json
{"causal_link_type": "DIRECT", "predicate": "causes",
 "source": "Inherited ADSHE gene architecture",
 "target": "Nicotinic acetylcholine receptor dysfunction",
 "description": "CHRNA4, CHRNA2, and CHRNB2 variants alter receptor function."}
```

A Sciqst mindmap edge is `"connections": ["Asynchronous Contraction"]`. There is
no lossless mapping from the second into the first: the predicate and the
evidence are not missing fields to be filled in, they are the entire content of a
dismech edge.

### Verdict on mindmaps

**No usable content.** Do not ingest them. An uncited, untyped concept tree is
the one artifact type dismech is specifically built to be the opposite of, and
converting one would mean inventing both the predicate and the evidence — which
is the fabrication mode the evidence SOP exists to prevent.

Two secondary observations, neither a reason to ingest:

- **As a demand signal, resist the temptation.** The 1,865 map titles are real
  user queries and show what clinicians actually ask about. But weighting the
  stub queue by that is the same mistake as the retired ranked dashboard
  (issue #8969) — a cheap popularity-correlated feature that tracks how common a
  topic is rather than whether it is worth curating.
- **The interaction model is worth stealing, though.** vis-network with a 2D/3D
  orbit toggle, node size scaled by depth tier (30px at level 1 down to 10px at
  level 10), hold-1s-to-expand progressive disclosure, click-to-focus and
  double-click-to-search. dismech pathographs render via dagre/mermaid and get
  hard to read at high node counts; progressive expansion by depth is a real
  answer to that. That is a UI idea to file, not data to import.

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
   research index. **Do not ingest mindmaps in any form** — see above.
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
