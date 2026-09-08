# dismech HPOA export vs. the HPO project's phenotype.hpoa

**Generated:** 2026-09-08 · **HPO release compared:** 2026-09-02
**Worklist:** [`data/hpoa-export-vs-hpo-release-2026-09-08.tsv`](data/hpoa-export-vs-hpo-release-2026-09-08.tsv) — one row per dismech disease, both joins side by side.
**Regenerate:** `scripts/hpoa_release_compare.py`; its module docstring lists the four inputs and the `curl` commands that fetch them. Sections 1–4 are generated; sections 5–7 are read by hand and are not rewritten by a re-run, so regenerate into a scratch path and merge.

This compares the two **files** — the artifact `just export-hpoa` writes against the release the HPO project publishes. It is the file-level counterpart of [`kg-phenotype-gap-audit-2026-07-31.md`](kg-phenotype-gap-audit-2026-07-31.md), which compares dismech *KB content* against HPOA as ingested by the Monarch KG.

## 0. In one paragraph

The export is structurally an HPOA file — the twelve columns are present, correctly ordered, and carry a thirteenth (`dismech_name`) that a tab-split parser ignores. What stops it being consumable is the key: **every row is anchored on MONDO**, and no HPOA consumer accepts a MONDO `database_id`. Below that, five smaller value-space divergences make a further ~6% of rows unparseable or unciteable. On content, dismech agrees with the release far more than the raw counts suggest — **77.7% semantic overlap** once granularity and the release's gene-level splitting are accounted for, which independently reproduces the 75.2% that July's Monarch-API audit reached by a completely different route.

## 1. Scale

|  | dismech export | HPO release |
|---|---|---|
| Annotation rows | 40,614 | 286,651 |
| Diseases | 2,724 | 12,880 |
| Rows per disease (mean) | 14.9 | 22.3 |
| Distinct HP terms | 4,509 | 11,658 |
| Header comment lines | 5 | 4 |
| Columns | 13 | 12 |

## 2. Format conformance

- First 12 columns match the HPOA order: **yes**
- Extra columns: `dismech_name`
- Missing columns: none

### Rows a strict HPOA consumer would reject

| Check | dismech rows | % of file |
|---|---|---|
| `database_id` outside OMIM / ORPHA / DECIPHER (all rows are MONDO) | 40,614 | 100.0% |
| `hpo_id` is not an HP term (synthetic `DISMECH:` CURIE) | 431 | 1.1% |
| `frequency` is neither an HP term, a percentage, nor n/m (ranges like `30-79%`) | 401 | 1.0% |
| `reference` prefix never used by the release | 2,425 | 6.0% |
| `reference` is the row's own disease id (self-citation) | 1,453 | 3.6% |

### Value spaces

**`qualifier`**

| value | dismech rows | % | HPO rows | % |
|---|---|---|---|---|
| `(empty)` | 40,441 | 99.6% | 285,918 | 99.7% |
| `NOT` | 173 | 0.4% | 733 | 0.3% |

**`evidence`**

| value | dismech rows | % | HPO rows | % |
|---|---|---|---|---|
| `PCS` | 30,725 | 75.7% | 119,333 | 41.6% |
| `IEA` | 9,889 | 24.3% | 30,307 | 10.6% |
| `TAS` | **0** | 0.0% | 137,011 | 47.8% |

**`aspect`**

| value | dismech rows | % | HPO rows | % |
|---|---|---|---|---|
| `P` | 40,614 | 100.0% | 268,906 | 93.8% |
| `I` | **0** | 0.0% | 8,978 | 3.1% |
| `C` | **0** | 0.0% | 8,559 | 3.0% |
| `H` | **0** | 0.0% | 131 | 0.0% |
| `M` | **0** | 0.0% | 77 | 0.0% |

**`sex`**

| value | dismech rows | % | HPO rows | % |
|---|---|---|---|---|
| `(empty)` | 40,614 | 100.0% | 286,013 | 99.8% |
| `MALE` | **0** | 0.0% | 448 | 0.2% |
| `FEMALE` | **0** | 0.0% | 190 | 0.1% |

**`onset`**

| value | dismech rows | % | HPO rows | % |
|---|---|---|---|---|
| `(empty)` | 40,614 | 100.0% | 283,603 | 98.9% |
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
| `(empty)` | 40,614 | 100.0% | 285,625 | 99.6% |
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
| `(empty)` | 19,926 | 49.1% | 63,396 | 22.1% |
| `HP frequency term` | 18,570 | 45.7% | 119,446 | 41.7% |
| `percentage` | 1,596 | 3.9% | 105 | 0.0% |
| `other` | 401 | 1.0% | 0 | 0.0% |
| `n/m ratio` | 121 | 0.3% | 103,704 | 36.2% |

**`reference`** (by prefix)

| prefix | dismech | % | HPO release | % |
|---|---|---|---|---|
| `PMID` | 33,763 | 83.1% | 118,816 | 41.4% |
| `ORPHA` | 4,426 | 10.9% | 116,661 | 40.7% |
| `MONDO` | 1,453 | 3.6% | 0 | 0.0% |
| `DOI` | 652 | 1.6% | 0 | 0.0% |
| `url` | 275 | 0.7% | 0 | 0.0% |
| `clinicaltrials` | 24 | 0.1% | 0 | 0.0% |
| `CGGV` | 21 | 0.1% | 0 | 0.0% |
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
| dismech diseases with ≥1 positive HP row | 2,724 | 100% |
| → map to a release-namespace id **and** that id is annotated in the release | 1,981 | 72.7% |
| → map, but the mapped id carries no release annotations | 364 | 13.4% |
| → no `exactMatch` into OMIM / ORPHA / DECIPHER at all | 379 | 13.9% |


Largest dismech entries that map to a release id that carries no annotations: spinal muscular atrophy, juvenile idiopathic arthritis, partial duplication of the long arm of chromosome X, congenital vertebral-cardiac-renal anomalies syndrome, anauxetic dysplasia, Rocky mountain spotted fever, Wieacker-Wolff syndrome (spectrum), pheochromocytoma-paraganglioma.

Largest dismech entries that have no `exactMatch` into a release namespace: Dravet syndrome, homocystinuria, epilepsy, Graves disease, Crohn disease, cerebral palsy, congenital nervous system disorder, hantavirus hemorrhagic fever with renal syndrome.

Release diseases dismech does not cover: **10,183** of 12,880.

Allowing a dismech entry to also match its MONDO **subtree** — the lump/split case, where the release splits a disease into gene-specific OMIM entries that dismech curates as one — joins **2,319** diseases (85.1%), 338 more than the direct join.

## 4. Annotation agreement on the joined diseases

**Direct join** (dismech entry ↔ its own `exactMatch` release ids):

| Match class | HP assertions | % of dismech |
|---|---|---|
| dismech HP assertions on joined diseases | 25,387 | 100% |
| EXACT (same HP id) | 14,968 | 59.0% |
| MORE_SPECIFIC (dismech finer) | 1,846 | 7.3% |
| MORE_GENERAL (dismech coarser) | 2,088 | 8.2% |
| **SEMANTIC overlap** | **18,902** | **74.5%** |
| UNMATCHED (novel to dismech) | 6,485 | 25.5% |

Release HP assertions on the same diseases: **75,434**, of which **60,466** (80.2%) are absent from dismech.

**Subtype-inclusive join** (also matching the entry's MONDO subtree):

| Match class | HP assertions | % of dismech |
|---|---|---|
| dismech HP assertions on joined diseases | 28,734 | 100% |
| EXACT (same HP id) | 18,260 | 63.5% |
| MORE_SPECIFIC (dismech finer) | 1,924 | 6.7% |
| MORE_GENERAL (dismech coarser) | 2,139 | 7.4% |
| **SEMANTIC overlap** | **22,323** | **77.7%** |
| UNMATCHED (novel to dismech) | 6,411 | 22.3% |

Release HP assertions on the same diseases: **154,803**, of which **136,543** (88.2%) are absent from dismech.

### Diseases contributing the most novel dismech annotations (subtype-inclusive join)

| Disease | MONDO | release id(s) | dismech | release | exact | novel |
|---|---|---|---|---|---|---|
| Fanconi anemia | MONDO:0019391 | OMIM:227645;OMIM:227646; | 180 | 295 | 114 | 35 |
| intellectual developmental disorder with dys | MONDO:0015022 | OMIM:617333 | 50 | 38 | 15 | 33 |
| Bryant-Li-Bhoj neurodevelopmental syndrome 2 | MONDO:0030607 | OMIM:619721 | 42 | 41 | 10 | 30 |
| psychomotor retardation, epilepsy, and crani | MONDO:0013787 | OMIM:614501 | 53 | 31 | 23 | 27 |
| Ritscher-Schinzel syndrome 1 | MONDO:0009073 | OMIM:220210 | 47 | 36 | 19 | 23 |
| intellectual disability-facial dysmorphism s | MONDO:0014336 | OMIM:615761 | 40 | 40 | 15 | 23 |
| neurodevelopmental disorder with epilepsy, s | MONDO:0032894 | OMIM:618741 | 35 | 14 | 5 | 23 |
| intellectual developmental disorder 62 | MONDO:0032919 | OMIM:618793 | 32 | 14 | 7 | 23 |
| Nijmegen breakage syndrome-like disorder | MONDO:0013118 | OMIM:613078 | 28 | 11 | 3 | 21 |
| intellectual developmental disorder with mic | MONDO:0014376 | OMIM:615866 | 32 | 42 | 7 | 20 |
| alcohol dependence | MONDO:0007079 | OMIM:103780 | 21 | 2 | 1 | 19 |
| PGM1-congenital disorder of glycosylation | MONDO:0013968 | OMIM:614921 | 34 | 47 | 14 | 18 |
| congenital disorder of glycosylation, type I | MONDO:0026729 | OMIM:301031 | 20 | 5 | 2 | 18 |
| neurodevelopmental disorder with dysmorphic  | MONDO:0030852 | OMIM:619103 | 47 | 40 | 21 | 18 |
| intellectual developmental disorder with dys | MONDO:0044319 | OMIM:617452;ORPHA:505237 | 33 | 62 | 10 | 18 |

## 5. Reading the numbers

### The blocking difference is the key, not the format

All 40,614 rows carry a MONDO `database_id`. The release keys on OMIM, ORPHA and
DECIPHER, and so does every tool that reads `phenotype.hpoa`. This is a deliberate
export decision — MONDO is dismech's anchor and the exporter skips disorders that lack
one — but it means the file cannot be concatenated with the release or read by an
HPOA parser without a mapping pass. The mapping is not free: **13.9% of dismech's
annotated diseases have no `skos:exactMatch` into any of those three namespaces at
all**, and they are not a random 13.9% — Dravet syndrome, Crohn disease, Graves
disease, cerebral palsy, homocystinuria. That is the same common/complex and
acquired-disease skew the July audit found in its 266 sole-source diseases, and it is
where dismech is most additive.

### Five value-space divergences, in descending order of consequence

1. **`reference` carries prefixes the release never uses** (2,425 rows, 6.0%):
   `MONDO:`, `DOI:`, `url:`, `clinicaltrials:`, `CGGV:`. The docstring already warns
   consumers not to assume column 5 is a PMID, but `DOI:` and `CGGV:` are resolvable
   identifiers a consumer could be taught, whereas the 1,453 `MONDO:` rows are the
   file **citing the disease as the source of its own annotation**. Those are the IEA
   fallback rows — a phenotype with no surviving evidence still emits one row — so
   what they really encode is "dismech asserts this, uncited". A dedicated sentinel,
   or omitting the row, would say that more honestly than a self-citation.
2. **`aspect` is always `P`.** The release uses `C` (clinical course, 3.0%), `I`
   (inheritance, 3.1%), `M` and `H` for the remaining 6.2%. The exporter's docstring
   flags the OAK-based classification as a follow-up; it is the cheapest of these to
   close, since aspect is a function of the HP term's position in the hierarchy and
   the hierarchy is already being loaded for other checks.
3. **`frequency` ranges are not valid HPOA** (401 rows, 1.0%). Values like `30-79%`
   and the Orphanet-order `99-80%` are neither an HP frequency term, a percentage,
   nor an n/m ratio. The release contains zero of them. Either map a range onto the
   HP frequency band that contains it, or drop to the band term.
4. **Synthetic `DISMECH:` CURIEs in `hpo_id`** (431 rows, 1.1%). Untyped phenotypes
   get `DISMECH:<entry-slug>#<phen-slug>`. Useful inside dismech, meaningless to a
   consumer, and they will fail any HP-id validation. They are also a curation
   worklist: 431 rows is 431 phenotypes nobody has bound to an HP term.
5. **`evidence` never uses `TAS`**, which is 47.8% of the release. dismech splits
   `PCS`/`IEA` 76:24 where the release is 42:11:48. `PCS` ("published clinical study")
   for evidence quoted from a primary paper is defensible; `IN_VITRO` coded as `PCS`
   is the assumption to re-examine, and evidence sourced from Orphanet or ClinGen
   rows — 10.9% of references are `ORPHA:` — looks more like `TAS` than `PCS`.

`sex`, `onset` and `modifier` are unpopulated in the export and near-unpopulated in
the release (0.2%, 1.1%, 0.4%), so their absence costs almost nothing.

### On content, the two sources agree more than they disagree

The direct join reaches 74.5% semantic overlap; allowing a dismech entry to also match
its **MONDO subtree** raises it to 77.7% and lifts the join from 1,981 to 2,319
diseases. That second number is the fairer one: the release splits many diseases into
gene-specific OMIM entries that dismech curates as one, and Fanconi anemia is the
worked case — against `ORPHA:84` alone it looks like 106 release terms and 55 novel
dismech ones, but against the whole FA subtree it is 295 release terms, 114 exact
matches, and 35 novel.

**~6,400 dismech HP assertions are absent from the release** under either join. That
is the contribution set, and it is the same signal §B of the July audit reported
(4,227 there, on a smaller KB and a stricter join). Conversely 88.2% of the release's
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
- Bind the 431 `DISMECH:` phenotypes, or exclude them from the export.

## 7. Caveats

- **The join is only as good as MONDO's SSSOM set**, restricted here to
  `skos:exactMatch`. A disease whose mapping is `broadMatch`/`narrowMatch` reads as
  unmapped, so the 13.9% unmapped bucket is an upper bound on true non-mappability.
- **Exact HP-id matching is a lower bound**, which is why the subsumption pass is
  reported alongside it; `MORE_GENERAL` and `MORE_SPECIFIC` are agreement, not
  disagreement.
- **The subtype-inclusive join can over-credit.** Pulling a whole MONDO subtree's
  annotations in will match a dismech term against a phenotype annotated only to a
  sibling subtype. It is reported next to the direct join rather than replacing it
  for that reason — read them as a bracket.
- **Only positive rows are compared.** `NOT`-qualified rows (173 dismech, 733
  release) are excluded from the term sets on both sides.
- **Both files are snapshots**: the release is 2026-09-02, the export was generated
  from `kb/disorders` on 2026-09-08.
