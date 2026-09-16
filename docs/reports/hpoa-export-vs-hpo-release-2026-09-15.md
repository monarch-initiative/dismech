# dismech HPOA export vs. the HPO project's phenotype.hpoa

**Generated:** 2026-09-15 · **HPO release compared:** 2026-09-02
**Worklist:** [`data/hpoa-export-vs-hpo-release-2026-09-15.tsv`](data/hpoa-export-vs-hpo-release-2026-09-15.tsv) — one row per dismech disease, both joins side by side.
**Regenerate:** `just compare-hpoa-release` (fetches the four inputs, caches them under `output/hpoa-compare/`, writes the generated sections to stdout). Sections 1–4 are generated; sections 5–7 are read by hand and are not rewritten by a re-run, so regenerate into a scratch path and merge.

This compares the two **files** — the artifact `just export-hpoa` writes against the release the HPO project publishes. It is the file-level counterpart of [`kg-phenotype-gap-audit-2026-07-31.md`](kg-phenotype-gap-audit-2026-07-31.md), which compares dismech *KB content* against HPOA as ingested by the Monarch KG.

## 0. In one paragraph

The export is structurally an HPOA file — the twelve columns are present, correctly ordered, and carry a thirteenth (`dismech_name`) that a tab-split parser ignores. What stops it being consumable is the key: **every row is anchored on MONDO**, and no HPOA consumer accepts a MONDO `database_id`. Below that, five smaller value-space divergences make a further ~6% of rows unparseable or unciteable. On content, dismech agrees with the release far more than the raw counts suggest — **76.5% semantic overlap** once granularity and the release's gene-level splitting are accounted for, which independently reproduces the 75.2% that July's Monarch-API audit reached by a completely different route.

## 1. Scale

|  | dismech export | HPO release |
|---|---|---|
| Annotation rows | 43,754 | 286,651 |
| Diseases | 2,879 | 12,880 |
| Rows per disease (mean) | 15.2 | 22.3 |
| Distinct HP terms | 4,664 | 11,658 |
| Header comment lines | 5 | 4 |
| Columns | 13 | 12 |

## 2. Format conformance

- First 12 columns match the HPOA order: **yes**
- Extra columns: `dismech_name`
- Missing columns: none

### Rows a strict HPOA consumer would reject

| Check | dismech rows | % of file |
|---|---|---|
| `database_id` outside OMIM / ORPHA / DECIPHER (all rows are MONDO) | 43,754 | 100.0% |
| `hpo_id` is not an HP term (synthetic `DISMECH:` CURIE) | 460 | 1.1% |
| `frequency` is neither an HP term, a percentage, nor n/m (ranges like `30-79%`) | 422 | 1.0% |
| `reference` prefix never used by the release | 2,571 | 5.9% |
| `reference` is the row's own disease id (self-citation) | 1,445 | 3.3% |

### Value spaces

**`qualifier`**

| value | dismech rows | % | HPO rows | % |
|---|---|---|---|---|
| `(empty)` | 43,550 | 99.5% | 285,918 | 99.7% |
| `NOT` | 204 | 0.5% | 733 | 0.3% |

**`evidence`**

| value | dismech rows | % | HPO rows | % |
|---|---|---|---|---|
| `PCS` | 33,710 | 77.0% | 119,333 | 41.6% |
| `IEA` | 10,044 | 23.0% | 30,307 | 10.6% |
| `TAS` | **0** | 0.0% | 137,011 | 47.8% |

**`aspect`**

| value | dismech rows | % | HPO rows | % |
|---|---|---|---|---|
| `P` | 43,754 | 100.0% | 268,906 | 93.8% |
| `I` | **0** | 0.0% | 8,978 | 3.1% |
| `C` | **0** | 0.0% | 8,559 | 3.0% |
| `H` | **0** | 0.0% | 131 | 0.0% |
| `M` | **0** | 0.0% | 77 | 0.0% |

**`sex`**

| value | dismech rows | % | HPO rows | % |
|---|---|---|---|---|
| `(empty)` | 43,754 | 100.0% | 286,013 | 99.8% |
| `MALE` | **0** | 0.0% | 448 | 0.2% |
| `FEMALE` | **0** | 0.0% | 190 | 0.1% |

**`onset`**

| value | dismech rows | % | HPO rows | % |
|---|---|---|---|---|
| `(empty)` | 43,754 | 100.0% | 283,603 | 98.9% |
| `HP:0003577` | **0** | 0.0% | 891 | 0.3% |
| `HP:0003593` | **0** | 0.0% | 542 | 0.2% |
| `HP:0011463` | **0** | 0.0% | 365 | 0.1% |
| `HP:0003623` | **0** | 0.0% | 341 | 0.1% |
| `HP:0011461` | **0** | 0.0% | 224 | 0.1% |
| `HP:0003621` | **0** | 0.0% | 217 | 0.1% |
| `HP:0003581` | **0** | 0.0% | 150 | 0.1% |
| `HP:0011462` | **0** | 0.0% | 107 | 0.0% |
| `HP:0030674` | **0** | 0.0% | 88 | 0.0% |
| `HP:0003584` | **0** | 0.0% | 54 | 0.0% |
| `HP:0003596` | **0** | 0.0% | 42 | 0.0% |

…and 6 further values used only by the release.

**`modifier`**

| value | dismech rows | % | HPO rows | % |
|---|---|---|---|---|
| `(empty)` | 43,754 | 100.0% | 285,625 | 99.6% |
| `HP:0012825` | **0** | 0.0% | 359 | 0.1% |
| `HP:0012828` | **0** | 0.0% | 180 | 0.1% |
| `HP:0003676` | **0** | 0.0% | 58 | 0.0% |
| `HP:0031796` | **0** | 0.0% | 54 | 0.0% |
| `HP:0025303` | **0** | 0.0% | 47 | 0.0% |
| `HP:0012833` | **0** | 0.0% | 41 | 0.0% |
| `HP:0012832` | **0** | 0.0% | 32 | 0.0% |
| `HP:0025206` | **0** | 0.0% | 31 | 0.0% |
| `HP:0012829` | **0** | 0.0% | 30 | 0.0% |
| `HP:0025215` | **0** | 0.0% | 18 | 0.0% |
| `HP:0011010` | **0** | 0.0% | 17 | 0.0% |

…and 43 further values used only by the release.

**`frequency`** (by form)

| form | dismech | % | HPO release | % |
|---|---|---|---|---|
| `(empty)` | 21,620 | 49.4% | 63,396 | 22.1% |
| `HP frequency term` | 19,694 | 45.0% | 119,446 | 41.7% |
| `percentage` | 1,849 | 4.2% | 105 | 0.0% |
| `other` | 422 | 1.0% | 0 | 0.0% |
| `n/m ratio` | 169 | 0.4% | 103,704 | 36.2% |

**`reference`** (by prefix)

| prefix | dismech | % | HPO release | % |
|---|---|---|---|---|
| `PMID` | 36,759 | 84.0% | 118,816 | 41.4% |
| `ORPHA` | 4,424 | 10.1% | 116,661 | 40.7% |
| `MONDO` | 1,445 | 3.3% | 0 | 0.0% |
| `DOI` | 690 | 1.6% | 0 | 0.0% |
| `url` | 379 | 0.9% | 0 | 0.0% |
| `CGGV` | 30 | 0.1% | 0 | 0.0% |
| `clinicaltrials` | 24 | 0.1% | 0 | 0.0% |
| `PPR` | 3 | 0.0% | 0 | 0.0% |
| `OMIM` | 0 | 0.0% | 50,479 | 17.6% |
| `ISBN-13` | 0 | 0.0% | 280 | 0.1% |
| `DECIPHER` | 0 | 0.0% | 223 | 0.1% |
| `http` | 0 | 0.0% | 182 | 0.1% |
| `ISBN-10` | 0 | 0.0% | 8 | 0.0% |
| `ISBN` | 0 | 0.0% | 1 | 0.0% |
| `https` | 0 | 0.0% | 1 | 0.0% |

## 3. Disease-level join

The two files share no key: the release is anchored on OMIM / ORPHA / DECIPHER, dismech on MONDO. The join goes through MONDO's own SSSOM `skos:exactMatch` set.

| Bucket | Diseases | % |
|---|---|---|
| dismech diseases with ≥1 positive HP row | 2,879 | 100% |
| → map to a release-namespace id **and** that id is annotated in the release | 2,119 | 73.6% |
| → map, but the mapped id carries no release annotations | 373 | 13.0% |
| → no `exactMatch` into OMIM / ORPHA / DECIPHER at all | 387 | 13.4% |


Largest dismech entries that map to a release id that carries no annotations: familial hemiplegic migraine, spinal muscular atrophy, juvenile idiopathic arthritis, partial duplication of the long arm of chromosome X, congenital vertebral-cardiac-renal anomalies syndrome, anauxetic dysplasia, Rocky mountain spotted fever, Wieacker-Wolff syndrome (spectrum).

Largest dismech entries that have no `exactMatch` into a release namespace: Dravet syndrome, homocystinuria, epilepsy, Graves disease, Crohn disease, cerebral palsy, congenital nervous system disorder, hantavirus hemorrhagic fever with renal syndrome.

Release diseases dismech does not cover: **9,995** of 12,880.

Allowing a dismech entry to also match its MONDO **subtree** — the lump/split case, where the release splits a disease into gene-specific OMIM entries that dismech curates as one — joins **2,463** diseases (85.6%), 344 more than the direct join.

## 4. Annotation agreement on the joined diseases

**Direct join** (dismech entry ↔ its own `exactMatch` release ids):

| Match class | HP assertions | % of dismech |
|---|---|---|
| dismech HP assertions on joined diseases | 27,514 | 100% |
| EXACT (same HP id) | 15,917 | 57.9% |
| MORE_SPECIFIC (dismech finer) | 2,018 | 7.3% |
| MORE_GENERAL (dismech coarser) | 2,230 | 8.1% |
| **SEMANTIC overlap** | **20,165** | **73.3%** |
| UNMATCHED (novel to dismech) | 7,349 | 26.7% |

Release HP assertions on the same diseases: **79,614**, of which **63,697** (80.0%) are absent from dismech.

**Subtype-inclusive join** (also matching the entry's MONDO subtree):

| Match class | HP assertions | % of dismech |
|---|---|---|
| dismech HP assertions on joined diseases | 30,954 | 100% |
| EXACT (same HP id) | 19,273 | 62.3% |
| MORE_SPECIFIC (dismech finer) | 2,106 | 6.8% |
| MORE_GENERAL (dismech coarser) | 2,287 | 7.4% |
| **SEMANTIC overlap** | **23,666** | **76.5%** |
| UNMATCHED (novel to dismech) | 7,288 | 23.5% |

Release HP assertions on the same diseases: **159,207**, of which **139,934** (87.9%) are absent from dismech.

### Diseases contributing the most novel dismech annotations (subtype-inclusive join)

| Disease | MONDO | release id(s) | dismech | release | exact | novel |
|---|---|---|---|---|---|---|
| combined immunodeficiency due to CD3gamma de | MONDO:0014276 | OMIM:615607 | 48 | 19 | 5 | 38 |
| Fanconi anemia | MONDO:0019391 | OMIM:227645;OMIM:227646; | 182 | 295 | 114 | 36 |
| developmental and epileptic encephalopathy 8 | MONDO:0030856 | OMIM:619124 | 60 | 48 | 18 | 36 |
| intellectual developmental disorder with dys | MONDO:0015022 | OMIM:617333 | 50 | 38 | 15 | 33 |
| Bryant-Li-Bhoj neurodevelopmental syndrome 2 | MONDO:0030607 | OMIM:619721 | 44 | 41 | 8 | 32 |
| infantile hypertrophic cardiomyopathy due to | MONDO:0014162 | OMIM:615395 | 32 | 9 | 1 | 29 |
| spinocerebellar ataxia, autosomal recessive  | MONDO:0859245 | OMIM:619862 | 42 | 20 | 9 | 28 |
| psychomotor retardation, epilepsy, and crani | MONDO:0013787 | OMIM:614501 | 53 | 31 | 23 | 27 |
| Charcot-Marie-Tooth disease type 2T | MONDO:0044640 | OMIM:617017 | 33 | 14 | 4 | 26 |
| methylmalonic aciduria, cblA type | MONDO:0009613 | OMIM:251100 | 40 | 33 | 12 | 24 |
| short-rib thoracic dysplasia 21 without poly | MONDO:0030356 | OMIM:619479 | 51 | 37 | 24 | 24 |
| Ritscher-Schinzel syndrome 1 | MONDO:0009073 | OMIM:220210 | 47 | 36 | 19 | 23 |
| intellectual disability-facial dysmorphism s | MONDO:0014336 | OMIM:615761 | 40 | 40 | 15 | 23 |
| neurodevelopmental disorder with epilepsy, s | MONDO:0032894 | OMIM:618741 | 35 | 14 | 5 | 23 |
| intellectual developmental disorder 62 | MONDO:0032919 | OMIM:618793 | 32 | 14 | 7 | 23 |

## 5. Reading the numbers

### The blocking difference is the key, not the format

All 43,754 rows carry a MONDO `database_id`. The release keys on OMIM, ORPHA and
DECIPHER, and so does every tool that reads `phenotype.hpoa`. This is a deliberate
export decision — MONDO is dismech's anchor and the exporter skips disorders that lack
one — but it means the file cannot be concatenated with the release or read by an
HPOA parser without a mapping pass. The mapping is not free: **13.4% of dismech's
annotated diseases have no `skos:exactMatch` into any of those three namespaces at
all**, and they are not a random 13.4% — Dravet syndrome, Crohn disease, Graves
disease, cerebral palsy, homocystinuria. That is the same common/complex and
acquired-disease skew the July audit found in its 266 sole-source diseases, and it is
where dismech is most additive.

### Five value-space divergences, in descending order of consequence

1. **`reference` carries prefixes the release never uses** (2,571 rows, 5.9%):
   `MONDO:`, `DOI:`, `url:`, `CGGV:`, `clinicaltrials:`, `PPR:`. The exporter's docstring
   already warns consumers not to assume column 5 is a PMID, but `DOI:` and `CGGV:`
   are resolvable identifiers a consumer could be taught, whereas the 1,445 `MONDO:`
   rows are the file **citing the disease as the source of its own annotation**. Those
   are the IEA fallback rows — a phenotype with no surviving evidence still emits one
   row — so what they really encode is "dismech asserts this, uncited". A dedicated
   sentinel, or omitting the row, would say that more honestly than a self-citation.
2. **`aspect` is always `P`.** The release uses `C` (clinical course, 3.0%), `I`
   (inheritance, 3.1%), `M` and `H` for the remaining 6.2%. The exporter's docstring
   flags the OAK-based classification as a follow-up; it is the cheapest of these to
   close, since aspect is a function of the HP term's position in the hierarchy and
   the hierarchy is already being loaded for other checks.
3. **`frequency` ranges are not valid HPOA** (422 rows, 1.0%). Values like `30-79%`
   and the Orphanet-order `99-80%` are neither an HP frequency term, a percentage,
   nor an n/m ratio. The release contains zero of them. Either map a range onto the
   HP frequency band that contains it, or drop to the band term.
4. **Synthetic `DISMECH:` CURIEs in `hpo_id`** (460 rows, 1.1%). Untyped phenotypes
   get `DISMECH:<entry-slug>#<phen-slug>`. Useful inside dismech, meaningless to a
   consumer, and they will fail any HP-id validation. They are also a curation
   worklist: 460 rows is 460 phenotypes nobody has bound to an HP term.
5. **`evidence` never uses `TAS`**, which is 47.8% of the release. dismech splits
   `PCS`/`IEA` 77:23 where the release is 42:11:48. `PCS` ("published clinical study")
   for evidence quoted from a primary paper is defensible; `IN_VITRO` coded as `PCS`
   is the assumption to re-examine, and evidence sourced from Orphanet or ClinGen
   rows — 10.1% of references are `ORPHA:` — looks more like `TAS` than `PCS`.

`sex`, `onset` and `modifier` are unpopulated in the export and near-unpopulated in
the release (0.2%, 1.1%, 0.4%), so their absence costs almost nothing.

### On content, the two sources agree more than they disagree

The direct join reaches 73.3% semantic overlap; allowing a dismech entry to also match
its **MONDO subtree** raises it to 76.5% and lifts the join from 2,119 to 2,463
diseases. That second number is the fairer one: the release splits many diseases into
gene-specific OMIM entries that dismech curates as one, and Fanconi anemia is the
worked case — against `ORPHA:84` alone it looks like 106 release terms and 56 novel
dismech ones, but against the whole FA subtree (22 OMIM entries plus the ORPHA one) it
is 295 release terms, 114 exact matches, and 36 novel.

**~7,300 dismech HP assertions are absent from the release** under either join. That
is the contribution set, and it is the same signal §B of the July audit reported
(4,227 there, on a smaller KB and a stricter join). Conversely 87.9% of the release's
assertions on the same diseases are absent from dismech — breadth by design, not a
gap, and the caveat the earlier report insists on applies here unchanged.

## 6. Follow-ups

Roughly in order of value per unit of work:

- Emit a mapped `database_id` (OMIM / ORPHA / DECIPHER, from MONDO's own SSSOM set)
  alongside or instead of the MONDO id, and report the diseases that cannot be mapped
  rather than emitting an unusable row. This is what makes the file consumable at all.
- Replace the `MONDO:` self-citation on IEA fallback rows.
- Derive `aspect` from the HP hierarchy (the exporter's own recorded follow-up).
- Normalize frequency ranges to HP frequency bands.
- Decide whether `IN_VITRO` → `PCS` and structured-source rows → `PCS` are the right
  codings, or whether `TAS` is the honest code for the latter.
- Bind the 460 `DISMECH:` phenotypes, or exclude them from the export.

## 7. Caveats

- **The join is only as good as MONDO's SSSOM set**, restricted here to
  `skos:exactMatch`. A disease whose mapping is `broadMatch`/`narrowMatch` reads as
  unmapped, so the 13.4% unmapped bucket is an upper bound on true non-mappability.
- **Exact HP-id matching is a lower bound**, which is why the subsumption pass is
  reported alongside it; `MORE_GENERAL` and `MORE_SPECIFIC` are agreement, not
  disagreement.
- **The subtype-inclusive join can over-credit.** Pulling a whole MONDO subtree's
  annotations in will match a dismech term against a phenotype annotated only to a
  sibling subtype. It is reported next to the direct join rather than replacing it
  for that reason — read them as a bracket.
- **Only positive rows are compared.** `NOT`-qualified rows (204 dismech, 733
  release) are excluded from the term sets on both sides.
- **Both files are snapshots**: the release is 2026-09-02, the export was generated
  from `kb/disorders` on 2026-09-15. The KB moves fast — one week and ~380 commits
  separate this run from the first, which shifted every count here by a few percent
  without changing any of the findings.
