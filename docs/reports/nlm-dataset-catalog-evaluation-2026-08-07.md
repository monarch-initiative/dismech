# NLM Dataset Catalog as a dataset-discovery source

**Date:** 2026-08-07
**Source evaluated:** <https://datasetcatalog.nlm.nih.gov/>
**Question:** can the NLM Dataset Catalog be used to find `datasets:` records for dismech
disease entries?

## Verdict

**Do not adopt the catalog. Go directly to the dbGaP FHIR API and the ImmPort search
API instead — they are the only two repositories in the catalog that matter to
dismech, and both native APIs are strictly better than querying them through it.**

The catalog holds ~3.02 M datasets, but 99.8 % of them are generalist-repository
records (figshare, Zenodo, Mendeley, Dataverse) that are overwhelmingly journal
supplementary files — "MOESM2 of …", "Table1_…" — not datasets in dismech's sense.
The part that matters is small but genuinely new to dismech: **3,604 dbGaP studies
and 1,500 ImmPort studies**, both of which dismech currently has almost no coverage
of.

The catalog's apparent selling point is **coded disease indexing** — every dataset
carries `dcterms:subject` links to SKOS concepts bound to MeSH descriptor URIs, which
is exactly what GEO lacks. But that coding turns out to be *derived from dbGaP's own
metadata*: dbGaP publishes the same MeSH codes itself, in a `condition` field that is
directly searchable, and ImmPort publishes a richer disease field of its own. See
[Compared with the native APIs](#compared-with-the-native-dbgap-and-immport-apis) —
that comparison is what drives the verdict, and it reverses the recommendation this
report originally reached.

So the finding that the coded path works is real and reusable; it is the *route* to
it that should be the native APIs rather than this catalog.

One limit belongs to the underlying data rather than to any interface: MeSH indexing
here is **descriptor-only**, and most rare diseases have only a Supplementary Concept
Record (`C######`). Spot-checking eight SCR-only diseases against dbGaP's own text
search (`condition:text=Timothy syndrome`, `…=Wolman`, `…=Bethlem`, `…=Aicardi`, …)
returns zero for all of them, which confirms dbGaP simply holds no studies for them.
The 0 % rare-disease yield below is a data-availability fact, not a search artifact.

## What it indexes

Thirteen repositories (from the endpoint's own `repository_list` query), with counts
measured on 2026-08-07:

| Repository | Datasets | Useful to dismech? |
|---|---:|---|
| Figshare | 2,300,399 | No — journal supplementary files |
| Zenodo | 423,181 | Rarely |
| Mendeley Data | 147,358 | Rarely |
| Harvard Dataverse | 82,008 | Rarely |
| Dryad | 36,460 | Rarely |
| **dbGaP** | **3,604** | **Yes** |
| **ImmPort** | **1,500** | **Yes** |
| Borealis, Dartmouth / Texas / UCLA / UNC Dataverse, JHU RDR | remainder | No |

**Total: 3,024,275. dbGaP + ImmPort = 5,104 = 0.17 % of the catalog.**

Two consequences follow.

**There is no overlap with dismech's existing sources.** No GEO, SRA, EGA,
ArrayExpress, PRIDE, or MetaboLights. So this source does *not* have the
duplicate-record hazard that
[`docs/dataset-curation.md`](../dataset-curation.md) documents for ArrayExpress
(73.6 % GEO re-imports) and OmicsDI (89 % duplicates). Anything it returns is
additive.

**dismech is nearly empty on both new repositories.** The KB currently holds 3
`dbgap:` accessions and 0 ImmPort accessions across ~290 dataset records — against
project guidance that says to *prefer* dbGaP for rare disease.

## Access: use SPARQL, not the REST API

### REST API — too weak to use

`https://datasetcatalog.nlm.nih.gov/public/api/v1` accepts only `q`, `page`, `size`
(capped at 50), and `sort`. There is **no repository filter and no subject filter**,
and the free-text search appears to cover the title only. A query for `asthma`
returns 2,575 hits led entirely by figshare supplements; there is no way to ask it
for the 0.17 % slice that matters.

### SPARQL — the usable interface

The public UI drives a SPARQL endpoint that is reachable without authentication:

```bash
curl -sS -X POST \
  https://xvonuqz0ik.execute-api.us-east-1.amazonaws.com/prod/api/sparql \
  -H 'Content-Type: application/json' \
  -d '{"query_type":"raw_sparql","raw_sparql":"SELECT ?s WHERE { ?s ?p ?o } LIMIT 5"}'
```

Other `query_type` values the UI uses: `repository_list`, `by_dataset` (add
`"value": "<dataset id>"`, `"jsonld": true`).

The endpoint is behind a query guard that rejects anything it does not like with
`{"error": "PROTECTION ENGAGED: ..."}`. Measured constraints:

| Construct | Status |
|---|---|
| `SELECT` | allowed — the only query form (`DESCRIBE`/`CONSTRUCT` rejected) |
| `LIMIT` | **required** on every query |
| `OFFSET` | allowed up to 50,000 |
| `COUNT` | allowed, provided a `LIMIT` is present |
| `FILTER`, `UNION`, `VALUES`, `OPTIONAL` | allowed |
| `GROUP BY` | blocked |
| `REGEX`, `CONTAINS` | blocked |
| `ORDER BY`, `STRSTARTS` on an unbounded pattern | 504 (API Gateway ~30 s timeout) |

The blocked string functions matter: **there is no substring search over titles**, so
the label-based fallback that would rescue rare disease is not available server-side.
Exact-string label matching works but is brittle (`"Timothy Syndrome"` returns
nothing).

Because this is an undocumented endpoint backing a public UI, treat it as
best-effort: rate-limit politely, and expect the URL to change.

## Data model

Per-dataset fields (DATMM):

| Predicate | Content | Maps to dismech `Dataset` |
|---|---|---|
| `dcterms:identifier` | native accession — `phs001289.v1.p1`, `SDY1679` | `accession` |
| `dcterms:title` | verbatim | `title` |
| `dcterms:description` | verbatim | `description` |
| `foaf:homepage` | repository landing page | provenance `notes` |
| `dcterms:isPartOf` | repository URI | source selection |
| `dcterms:subject` | SKOS concepts (MeSH) | the discovery key |
| `dcterms:issued`, `dcterms:rights`, `bf:contribution`, `schema:funding` | — | not needed |

**Not available:** organism, sample count, data type, or a PubMed ID. dbGaP records'
`isReferencedBy` nodes are phenotype data dictionaries (`pht######`), not papers;
generalist-repository records link a DOI. So a record built from this source fills
`accession` / `title` / `description` / `notes` and leaves `organism`, `data_type`,
`sample_count`, and `publication` to a follow-up lookup — a thinner fill than the
GEO path in `scripts/build_dataset_records.py`, which gets all of them.

### The subject concepts

```
concept/0000000829
  rdf:type            skos:Concept
  dcterms:identifier  https://id.nlm.nih.gov/mesh/D016207
  rdfs:label          Cytokines
  skos:inScheme       MeSH RDF
  dcterms:source      repository_supplied
  dcterms:source      title/description_derived
  dcterms:source      PubMed_supplied
  dcterms:source      keyword_derived
```

`dcterms:source` records *how* each subject was assigned, which is a usable
confidence signal: `repository_supplied` and `PubMed_supplied` are far stronger than
`title/description_derived`. This is more provenance than GEO offers on anything.

### The descriptor-only limit

A query for any concept whose identifier starts with `https://id.nlm.nih.gov/mesh/C`
returns **zero rows** — no Supplementary Concept Records exist in the store.

Rare-disease names are still present, but only as *label-only* concepts with no
identifier and no scheme. The X-linked dystonia-parkinsonism study `phs001525.v2.p1`
carries 37 identified MeSH descriptors (`Dystonic Disorders`, `Genetic Diseases,
X-Linked`, …) plus three bare `repository_supplied` keyword concepts — `Lubag
Syndrome`, `Dystonia 3, Torsion, X-linked`, `Torsion Dystonia-Parkinsonism, Filipino
Type` — which are exactly the MeSH SCR synonyms, stripped of their IDs. The
information is there; it just isn't coded, and `CONTAINS`/`REGEX` are blocked, so it
cannot be searched.

## Measured yield against dismech

Mapping path: dismech entry → `disease_term` MONDO ID → MONDO `MESH:` dbxref →
catalog `dcterms:subject`.

**Mapping coverage.** Of 1,871 disorder files, 1,843 carry a MONDO `disease_term`,
and **1,061 (57.6 %) have a MONDO→MeSH cross-reference**. That is the hard ceiling
on the coded path. 1,196 entries currently lack a `datasets:` block; 641 of those
have a MeSH mapping.

**Yield.** Random sample of 60 of those 641 uncurated entries, querying dbGaP +
ImmPort:

| Stratum | n | ≥1 hit | Yield |
|---|---:|---:|---:|
| MeSH descriptor (`D######`) | 33 | 19 | **58 %** |
| MeSH SCR (`C######`) | 27 | 0 | **0 %** |
| Overall | 60 | 19 | 32 % |

The split is the whole story. Where a disease has a real MeSH descriptor the source
performs well — better than the 24 % GEO yield recorded for Mendelian entries in
`docs/dataset-curation.md`. Where it has only an SCR it returns nothing at all, and
that is 45 % of the sample.

**Precision.** On inspection of the hits, disease-named studies are near-perfect:

- *Sjögren's syndrome* (`MESH:D012859`) → `phs002446` "Single Cell Omics Resolves
  Transcriptional Alterations in Sjogren's Syndrome", `phs000672` NIDCR Sjögren's
  International Collaborative Alliance, `phs002723` genetic risk loci, `phs001842`
  salivary-gland RNAseq — 5/5 directly on target.
- *Andersen-Tawil syndrome* (`MESH:D050030`) → `phs001289` genotype-phenotype
  longitudinal study, `phs001316` potassium/acetazolamide trial — 2/2 on target, and
  a rare disease that happens to hold a descriptor.

The characteristic false positive is different from GEO's, and worth naming:
**incidental mega-cohort**. Broad studies are legitimately MeSH-indexed for every
condition they measure, so *Bronchiectasis* pulls in "Yale Center for Mendelian
Genomics" and *Asthma* pulls in eMERGE and the Bogalusa Heart Study. These resolve
perfectly and are about a real superset of the disease — they are simply not
disease-specific. This is a milder relative of the Named Entity Confusion problem
(§2b): the hit is not the *wrong* disease, it is a study in which the disease is one
variable among hundreds. **Relevance triage remains mandatory**, as it already is for
the GEO path.

## Compared with the native dbGaP and ImmPort APIs

Both repositories expose public, unauthenticated APIs that cover the same records.

### dbGaP FHIR — better than the catalog on every axis

`https://dbgap-api.ncbi.nlm.nih.gov/fhir/x1/ResearchStudy` needs no authentication and
publishes MeSH coding natively:

```json
"condition": [{
  "coding": [{
    "system": "urn:oid:2.16.840.1.113883.6.177",   // MeSH
    "code": "D002386",
    "display": "Cataract"
  }],
  "text": "Cataract"
}]
```

and it is **directly searchable** — `?condition=D012859` returns the Sjögren's
studies. `?condition:text=<string>` additionally searches the MeSH *entry terms*
carried alongside each code, which the catalog cannot offer at all because `REGEX`
and `CONTAINS` are blocked at its endpoint. (The `metadata` CapabilityStatement
advertises only `_has` and `batchId_internal`; `condition`, `focus`, and `keyword`
work regardless.)

**Coverage is the same:** 3,582 `ResearchStudy` resources vs the catalog's 3,604.

**Precision is better, and the difference is exactly the noise this report flagged.**
For bronchiectasis (`D001987`):

| Source | Returns |
|---|---|
| dbGaP FHIR `condition=D001987` | `phs000518` NHLBI GO-ESP Idiopathic Bronchiectasis · `phs001279` Cross-Sectional Characterization of Idiopathic Bronchiectasis |
| NLM catalog, same MeSH code | those two, **plus** `phs000744` Yale Center for Mendelian Genomics · `phs001899` NIAID Centralized Sequencing Program |

The catalog's extra recall *is* the incidental-mega-cohort false positive. dbGaP's
`condition` is the submitter-declared condition; the catalog adds subjects inferred
from title, description, keywords, and linked PubMed records, which is why it
consistently returns more (Cataract 11 vs 2, Myocardial infarction 102 vs 12,
Asthma 80 vs 45) and why more is worse here.

FHIR also carries fields the catalog drops entirely: study design (`category`),
sponsor, consent groups, release date, and a study-overview URL.

### ImmPort — far better than the catalog

`https://api.immport.org` requires a token, but the public search behind the ImmPort
data browser does not:

```
https://www.immport.org/shared/data/query/api/search/study?term=asthma
```

It returns 1,502 studies total (catalog: 1,500), supports field-targeted filters
(`&conditionOrDisease=asthma` narrows 56 hits to 29), and each record carries
`condition_or_disease`, `research_focus`, `study_accession`, **`pubmed_id`**,
`species`, `actual_enrollment` / `study_size`, `assay_method`, `biosample_type`,
`doi`, and `clinicaltrials_link`.

That is essentially every field a dismech `Dataset` record wants — including the
`publication:` PMID and the `organism` and `sample_count` values that **the catalog
cannot supply for any repository**. It restores full parity with the GEO path in
`scripts/build_dataset_records.py`, which the catalog route would not have.

### What the catalog still uniquely offers

Little that dismech needs. One endpoint spanning both repositories saves writing a
second client — marginal. It is a single aggregated index over five generalist
repositories that have no unified API, but those are the supplementary-file records
dismech should not be curating. And it can act as an independent existence check for
a dbGaP accession — which dbGaP's own FHIR API does better and first-hand.

## Recommended use

**Use the native APIs.** The MeSH-keyed discovery strategy below is worth building;
point it at `dbgap-api.ncbi.nlm.nih.gov/fhir/x1` and
`immport.org/shared/data/query/api` rather than at the catalog.

1. **Key on the MONDO→MeSH descriptor xref**, read from the local `mondo.db`
   `has_dbxref_statement` table, then query
   `ResearchStudy?condition=<code>` on dbGaP FHIR. Skip entries whose only mapping
   is a `MESH:C######` SCR — dbGaP holds nothing for them, so do not spend the query.
2. **Add `condition:text=<disease name>` as a second pass** for entries with no MeSH
   descriptor mapping. It searches MeSH entry terms and picks up studies the code
   query misses (`condition:text=bronchiectasis` → 3, vs 2 for `condition=D001987`).
   The catalog has no equivalent.
3. **For ImmPort, use `conditionOrDisease=` rather than the free `term=`** — it
   halved the asthma hit count (56 → 29) by restricting the match to the disease
   field instead of the whole record.
4. **Triage for the incidental-mega-cohort pattern** before writing anything. Going
   native reduces it but does not eliminate it — a useful heuristic remains: does the
   disease name (or an obvious synonym) appear in the study title? If not, it is
   probably a broad cohort.
5. **Follow the existing pipeline** — the proposal/triage/apply flow in
   `scripts/build_dataset_records.py` and `scripts/triage_dataset_proposals.py`
   already models exactly this, and dbGaP accessions arrive in precisely the
   `dbgap:phs######.v#.p#` shape `verify_dataset_accessions.py` expects.
6. **Bulk-generated records carry no `evidence:` block**, per the standing rule.
   Note that ImmPort's `pubmed_id` does let the `publication:` field be filled, as
   the GEO path already does — that is a linked identifier, not a quoted claim, so it
   does not reopen the fabrication risk the rule guards against.

A `scripts/discover_dbgap_immport.py` following the `discover_ega.py` /
`discover_arrayexpress.py` pattern is the natural implementation. Two pieces of work
would be needed alongside it:

- **an ImmPort resolver** in `scripts/verify_dataset_accessions.py` for `SDY####`
  (and an `immport:` prefix registration), since none exists;
- **a fix to the dbGaP resolver** — see below.

## Blocking bug found: the dbGaP verifier cannot succeed

`scripts/verify_dataset_accessions.py::resolve_dbgap` looks up
`{accession}[Study Accession]` against NCBI E-utilities `db=gap`. **NCBI no longer
exposes that database.** The API answers:

```
{"esearchresult":{"ERROR":"Invalid db name specified: gap"}}
```

and `einfo.fcgi` confirms `gap` is absent from the current `dblist`. The failure is
silent in the sense that it does not error out — it is reported as `NOT_FOUND`, which
`docs/dataset-curation.md` defines as *"treat as fabricated until shown otherwise"*.
Two real, catalog-sourced accessions demonstrate it:

```
$ uv run python scripts/verify_dataset_accessions.py \
    --accession dbgap:phs001289.v1.p1 --accession dbgap:phs002446.v1.p1
[1/2] NOT_FOUND  dbgap:phs001289.v1.p1  no gap record for phs001289
[2/2] NOT_FOUND  dbgap:phs002446.v1.p1  no gap record for phs002446
```

So **every dbGaP accession in the KB currently fails verification**, and any dbGaP
curation drive is blocked until it is fixed.

**The fix is the dbGaP FHIR API** — the same endpoint the discovery path should use:

```
GET https://dbgap-api.ncbi.nlm.nih.gov/fhir/x1/ResearchStudy?_id=<phs accession>
```

It is public, returns the canonical `phsNNNNNN.vN.pN` in
`identifier[0].value` alongside the title, and needs no key. A cheaper fallback if a
FHIR client is unwelcome: `https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id=<acc>`
returns HTTP 200 for a real study and 302 for a nonexistent one
(`phs009999.v1.p1` → 302).

This bug is independent of the catalog question and should be filed separately.

## Reproducing the measurements

### Native APIs (the recommended route)

```bash
# dbGaP: studies coded to a MeSH descriptor
curl -sS 'https://dbgap-api.ncbi.nlm.nih.gov/fhir/x1/ResearchStudy?condition=D012859&_format=json'

# dbGaP: entry-term text search (no catalog equivalent)
curl -sS 'https://dbgap-api.ncbi.nlm.nih.gov/fhir/x1/ResearchStudy?condition:text=bronchiectasis&_summary=count&_format=json'

# ImmPort: disease-field search
curl -sS 'https://www.immport.org/shared/data/query/api/search/study?term=asthma&conditionOrDisease=asthma'
```

### NLM catalog (for comparison / reproducing the numbers above)

Repository inventory:

```bash
curl -sS -X POST https://xvonuqz0ik.execute-api.us-east-1.amazonaws.com/prod/api/sparql \
  -H 'Content-Type: application/json' -d '{"query_type":"repository_list"}'
```

Datasets for one MeSH descriptor, restricted to dbGaP + ImmPort:

```sparql
SELECT ?title ?acc ?repo WHERE {
  ?c <http://purl.org/dc/terms/identifier> "https://id.nlm.nih.gov/mesh/D012859" .
  ?d <http://purl.org/dc/terms/subject> ?c .
  ?d <http://purl.org/dc/terms/isPartOf> ?repo .
  VALUES ?repo {
    <http://id.nlm.nih.gov/datmm/repository/0000000012>
    <http://id.nlm.nih.gov/datmm/repository/0000000010>
  }
  ?d <http://purl.org/dc/terms/title> ?title .
  OPTIONAL { ?d <http://purl.org/dc/terms/identifier> ?acc }
} LIMIT 25
```

Counting (note the mandatory `LIMIT`):

```sparql
SELECT (COUNT(?d) AS ?n) WHERE {
  ?d <http://purl.org/dc/terms/isPartOf> <http://id.nlm.nih.gov/datmm/repository/0000000012>
} LIMIT 1
```

dismech-side MeSH mapping coverage:

```python
import sqlite3, collections
db = sqlite3.connect("/root/.data/oaklib/mondo.db")
rows = db.execute(
    "SELECT subject, value FROM has_dbxref_statement WHERE value LIKE 'MESH:%'"
).fetchall()
mesh = collections.defaultdict(list)
for subject, value in rows:
    mesh[subject].append(value)
```
