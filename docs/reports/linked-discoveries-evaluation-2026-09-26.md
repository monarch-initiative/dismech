# NLM Linked Discoveries as a literature source for dismech

**Date:** 2026-09-26
**Source evaluated:** <https://linkeddiscoveries.ncbi.nlm.nih.gov/> (user guide v1.0, last
updated 2026-09-24)
**Question:** what, if anything, should dismech build on NLM's Linked Discoveries pilot —
as a source of new evidence, as a check on evidence already cited, or as a source of the
retraction and expression-of-concern signal the knowledge base currently has no gate for?

## Verdict

**Use it interactively, not programmatically. The one signal in it that dismech should
adopt now — retraction and expression-of-concern status of cited PMIDs — is available
first-hand from PubMed E-utilities, and that is the route to build on.**

Linked Discoveries builds a *neighborhood* of up to 200 PubMed records around a seed
PMID using BiomedBERT embeddings, and annotates every record with MedGen condition,
NCBI Gene and PubChem tags, review status, NIH funding, publication updates
(retraction, expression of concern, erratum) and the citation edges among the
neighbors. Three findings drive the verdict:

1. **There is no documented API.** The page's JavaScript calls an internal
   CSRF-protected `POST /<pmid>/links/` endpoint. It works from a script (the
   measurements below used it, roughly 400 calls, no errors, no rate-limit headers), but the
   site describes itself as an early-stage pilot "for exploratory and evaluation
   purposes only" and publishes no terms for programmatic access. That rules it out as
   a CI dependency or a scheduled feed until NLM says otherwise.
2. **Its retraction signal is PubMed's retraction signal.** On every one of the 18
   retracted or expression-of-concern papers found under `kb/`, Linked Discoveries and
   E-utilities `esummary` agree exactly. `esummary` is documented, batchable (200 PMIDs
   per call) and needs no session cookie, so a whole-KB census takes about three
   minutes there. **That census found 15 retracted and 6 expression-of-concern
   papers among the 41,234 PMIDs cited under `kb/`; 11 of them are cited as live
   evidence in 13 KB files (26 evidence items).** See
   [Retractions in the cited corpus](#retractions-in-the-cited-corpus). This is the
   actionable outcome of the evaluation, and it does not need Linked Discoveries.
3. **The semantic neighborhood is genuinely different from PubMed Similar Articles**
   (median 20 % overlap between a 200-record neighborhood and the top 100 Similar
   Articles for the same seed) and the per-record condition tags make it filterable
   to one disease, which Similar Articles is not. For a rare disease with its own
   literature that yields 140–190 condition-matched papers new to the KB from one
   seed. That is a good curation-time lead source — reached through the "Linked
   Discoveries" button on a PubMed abstract page, or the evaluation probe below — not
   a replacement for the weekly Europe PMC literature scan.

A fourth capability was tested and is **not worth building now**: using the per-record
MedGen condition tags as a computable Named Entity Confusion check on evidence ("is
the paper cited under disease X actually about disease X?"). Exact-CUI concordance on
a random sample of cited papers was 63 %, and every one of the 40 discordant pairs was
a granularity, phenotype-tag or synonym mismatch rather than a wrong disease.

## What it is

From the user guide and the endpoint's own responses:

- **Eligibility.** Seeds and neighbors are PubMed records with an abstract that
  represent original research, reviews or related evidence. Errata, comments,
  retraction notices, biographies and preprints cannot be seeds. New records are
  added daily; MedGen/Gene/PubChem tags lag by up to a month.
- **Neighborhood.** BiomedBERT embeddings of title + abstract + keywords; the 49
  (default) to 200 (maximum) nearest records, ordered by similarity. The guide is
  explicit that scores within a neighborhood are close together and the order should
  not be read as a ranking. Full text is not used.
- **Annotation, applied after the neighborhood is built:** MedGen condition CUIs,
  NCBI Gene IDs (any organism — the Tay-Sachs seed's neighborhood carries mouse
  *Hexa* and human *HEXA* as separate tags), PubChem CIDs, `isReview` (MeSH
  publication types including systematic reviews, meta-analyses, guidelines and
  consensus statements — broader than the bare `Review` type), NIH funding, a
  `publicationUpdates` block (`retraction`, `retractedRepublished`,
  `expressionOfConcern`, `erratum`, `update`, `comment` counts), `isRetracted`, and
  a `citationEdges` list of cites/cited-by pairs within the neighborhood.
- **Export.** The page offers a CSV download and "View all in PubMed"; the JSON the
  page consumes carries everything above plus each record's abstract.

### Access

The endpoint is `POST https://linkeddiscoveries.ncbi.nlm.nih.gov/<pmid>/links/` with
form field `neighbors` (1–200; 0 and 201 return 400), the `linked-discoveries-csrftoken`
cookie echoed in an `X-CSRFToken` header, and a `Referer` on the site. The cookie is
set by a seed page (`/<pmid>/`), not by the landing page. A GET returns 405. An
unknown PMID returns 200 with an empty `articles` list; an ineligible seed (a letter
without an abstract) returns the seed with `realCount: 0`. Response time was 0.3 s for
one neighbor and 2.1 s (675 KB, 686 citation edges) for 200. There is no
`/api/`, no OpenAPI document, and no rate-limit header; the probe paced itself at
0.4–0.5 s between calls.

`scripts/linked_discoveries_probe.py` wraps this for reproducing the numbers below. It
is deliberately not in the justfile.

## Coverage of the KB's cited literature

A random sample of 150 PMIDs (seed 0) from the 38,424 unique PMIDs cited as
`reference:` under `kb/disorders/`, each queried with `neighbors=1`:

| Measure | Count |
|---|---:|
| Seed record found | 150 / 150 |
| Seed has a neighborhood | 149 / 150 |
| Seed flagged retracted or expression of concern | 0 |
| Seed carries an erratum | 3 (E-utilities agrees: 3) |
| Seed is a review by Linked Discoveries' definition | 41 (E-utilities `Review` type: 31) |
| Seed carries ≥ 1 MedGen condition tag | 113 |
| Seed carries ≥ 1 Gene tag | 58 |
| Seed carries ≥ 1 PubChem tag | 36 |

The one seed with no neighborhood (`PMID:20466094`) is a 2010 comment/letter without
an abstract, which is what the eligibility rule predicts. Across the whole cited
corpus, `esummary` reports `Has Abstract` for 40,666 of 41,225 resolvable PMIDs
(98.6 %), so near-total coverage is expected, not a sample artefact.

## Retractions in the cited corpus

Because Linked Discoveries surfaces retraction and expression-of-concern status per
record, the question of whether dismech cites any retracted paper was cheap to answer
— and the cheap route turned out to be E-utilities, which the pilot re-serves rather
than improves on.

**Method.** Every `PMID:` under `kb/` (disorders, modules, comorbidities, groupings,
hypotheses; 41,234 unique) was sent to `esummary` in batches of 200; 41,225 resolved
(the 9 failures are malformed identifiers such as `870684507`). A record is
*retracted* when its `pubtype` includes `Retracted Publication` and *under expression
of concern* when its `references` block carries `Expression of concern in`. All 18
flagged records were then queried on Linked Discoveries: 18 / 18 agree on both flags.

**Result.** 15 retracted, 6 under expression of concern (3 are both), 1,226 with an
erratum. The 18 flagged records fall into two groups.

Cited as live evidence — `reference: PMID:…` on an evidence item — in 13 files, 26
evidence items:

| PMID | Status | Cited in | Items |
|---|---|---|---:|
| 33596356 | Retracted | `Glomerulonephritis`, `Microscopic_Polyangiitis`, module `necrotizing_vasculitis` | 6 |
| 21610853 | Expression of concern | `Scrub_Typhus` | 5 |
| 42051968 | Retracted | `Congenital_Epulis` | 4 |
| 9774102 | Expression of concern | `X-linked_Lymphoproliferative_Disease_Due_To_SH2D1A_Deficiency` | 3 |
| 23926107 | Retracted | `Idiopathic_Pulmonary_Fibrosis` | 2 |
| 12612585 | Retracted | `CLCN2-Related_Leukoencephalopathy` | 1 |
| 19377461 | Retracted | `ODonnell-Luria-Rodan_Syndrome` | 1 |
| 29958291 | Retracted | `Melanoma_in_Congenital_Melanocytic_Nevus` | 1 |
| 35865667 | Retracted | `X-Linked_Nephrogenic_Diabetes_Insipidus` | 1 |
| 39777366 | Expression of concern | `Basal_Cell_Carcinoma` | 1 |
| 41110921 | Retracted | `Heart_Failure` | 1 |

Not cited as evidence — the other seven appear in prose or in non-evidence slots.
Four are already recorded as retracted where they are mentioned (`PRKN-Related_Juvenile_Parkinson_Disease`
carries a "Retracted-literature note" for 30135585; the `Vitamin_D-Dependent_Rickets`
and `Rachitic_and_Osteomalacic_Disorders` groupings record 38847469 and 39569444 as
retracted; a hypothesis assessment records 41329731 as retracted;
`Adult-Type_Hypolactasia` says of 28690131 that "the retracted global meta-analysis …
is not used"). Two are not flagged where they appear: 31181104 is the `publication:`
of a GEO dataset record in `Q_Fever`, and 29649003 sits in a hypothesis report's
citation list. So curators already handle retraction by hand when they notice it; the
11 live citations are the ones nobody noticed.

**The reference cache cannot be the check.** `references_cache/PMID_*.md` is a
snapshot at fetch time. Five of the 11 cached files above carry PubMed's
`RETRACTED ARTICLE` line in the fetched abstract because they were fetched after the
retraction; the other six (fetched earlier, or as full text) say nothing. Retraction
is a post-publication event, so the check has to ask PubMed at check time, not read
the cache.

**Recommendation.** A `check-retracted-references` script over `esummary`: report-only
first (the 11 above need a curator's decision each — a retracted paper cited as
`REFUTE`, or as the historical origin of a claim, is not automatically wrong), then a
gate with a shrink-only baseline once triaged. It belongs next to
`check-source-defect-claims`, which already knows the vocabulary. Cost is one
`esummary` call per 200 PMIDs, 3 requests/s without an API key, so a nightly whole-KB
sweep is a few minutes; a per-PR check over changed files is seconds.

## Neighborhood as a lead source

For 15 entries — the 5 with the most cited PMIDs, and 10 drawn at random from entries
with ≥ 10 PMIDs and a MONDO→UMLS exact match — the entry's most-cited PMID was used as
seed, a 200-record neighborhood fetched, and neighbors kept only if tagged with the
entry's own MedGen CUI. Each kept record was classed as already cited in that entry,
cited elsewhere in the KB, or new to the KB. For the same seeds, PubMed Similar
Articles (`elink cmd=neighbor_score`, 100 records) was fetched for comparison.

| Entry | Seed | Seed is | Condition-matched of 200 | In entry | Elsewhere in KB | New to KB | Similar-Articles top-100 also in neighborhood |
|---|---|---|---:|---:|---:|---:|---:|
| Peutz_Jeghers_Syndrome | 20301443 | GeneReviews chapter | 197 | 4 | 3 | 190 | 8 |
| Melorheostosis | 31485554 | natural-history study | 156 | 10 | 3 | 143 | 75 |
| Cholera | 23201968 | systematic review | 46 | 5 | 0 | 41 | 2 |
| Beare-Stevenson_Cutis_Gyrata_Syndrome | 25706251 | case report | 28 | 9 | 0 | 19 | 49 |
| Snijders_Blok-Campeau_Syndrome | 32483341 | cohort | 17 | 5 | 0 | 12 | 20 |
| Multiple_Sclerosis | 37266405 | in-silico modelling | 15 | 0 | 0 | 15 | 6 |
| Schizophrenia | 41422157 | SETD1A mechanism | 10 | 0 | 0 | 10 | 26 |
| Asthma | 42181267 | SIRT1 review | 4 | 0 | 0 | 4 | 17 |
| Amyotrophic_Lateral_Sclerosis | 33085325 | EMG guidance (archived) | 4 | 0 | 1 | 3 | 32 |
| Autosomal_Recessive_Nonsyndromic_Hearing_Loss_35 | 39261511 | ESRRB variant study | 4 | 3 | 0 | 1 | 22 |
| MEPAN_Syndrome | 31070877 | GeneReviews chapter | 2 | 1 | 0 | 1 | 13 |
| Multiple_Myeloma | 34201396 | bone-disease review | 2 | 0 | 0 | 2 | 61 |
| Alzheimer_Disease | 42297981 | plasma proteomics of aging | 1 | 0 | 0 | 1 | 12 |
| IREB2-Related_Neurodegeneration | 39587636 | variant report | 1 | 1 | 0 | 0 | 15 |
| Dilated_Cardiomyopathy_1P | 34113975 | PLN arrhythmia prediction | 0 | 0 | 0 | 0 | 21 |

Three things to read off this.

**Yield is bimodal, and the axis is whether the disease has a literature of its own.**
Peutz-Jeghers and melorheostosis are diseases with a dedicated corpus; the
neighborhood of a good seed *is* that corpus, and almost all of it is new to the KB
(the KB cites 4 and 10 of those papers respectively). The common diseases return
single digits not because the neighborhood is poor but because it is *specific to the
seed*: the neighbors of a SIRT1 review are SIRT1 papers, most tagged with COPD or
"inflammation" rather than the Asthma CUI, and an exact-CUI filter drops them. This
is the filter being strict, and it is the right default — loosening it to the MedGen
hierarchy is possible (the response carries a partial `diseaseHierarchy`) but turns
"about asthma" into "about airways".

**The seed decides everything, and the most-cited PMID is not always a good one.**
Where the seed is a GeneReviews chapter or a natural-history study, the neighborhood
is the disease. Where it is the entry's most-cited *mechanism* paper (SETD1A, PLN,
plasma proteomics) the neighborhood is that mechanism across diseases. A curator
choosing the seed by hand — the entry's GeneReviews chapter where one exists, else
its defining clinical series — will do better than any rule.

**It is not Similar Articles.** Overlap between the 200-record neighborhood and the
top 100 Similar Articles ranged from 2 to 75 (median 20). The two rankings are built
differently (BiomedBERT embeddings vs PubMed's word-weighted algorithm) and disagree
substantially; neither is a subset of the other, so a curator who has already read the
Similar Articles list has not seen most of the neighborhood.

Two of the fifteen neighborhoods contained a retracted paper (a KCNQ1 variant
evaluation next to the DCM1P seed, a PPP2R5D variant report next to the IREB2 seed;
neither is cited in the KB). That is the pilot's stated purpose — surfacing
contradictory, retracted or otherwise less prominent work around a finding — working
as designed, and it is the reason to open the neighborhood *before* citing a seed's
claim rather than after.

### Where it would fit

Not in `literature-scan`, which is a dated feed over all diseases at once; a
neighborhood has no date filter and is one disease at a time. It fits the `curate`
skill's research step, as an optional per-entry pull: seed on the GeneReviews chapter
or the entry's defining series, filter to the entry's CUI, drop what the KB already
cites, and hand the remainder to the same reference workflow as any other lead (a
neighborhood record is a *lead*; its abstract still has to be fetched with
`just fetch-reference` and quoted exactly). `scripts/linked_discoveries_probe.py
neighborhood <pmid> --neighbors 200 --cui <CUI> --mark-kb` does exactly that today.
Whether that step should exist at all is the question to put to NLM first — see
[Recommended use](#recommended-use).

## Condition tags as a Named Entity Confusion check

Named Entity Confusion — evidence cited under the wrong disease because a name
resolved to a sibling — is the failure the `preflight-dr` check exists for on
deep-research reports. Linked Discoveries tags each record with MedGen CUIs, and
2,951 of dismech's 3,133 disorder entries have a MONDO term with a UMLS exact match
(from `mondo_exactmatch_umls.sssom.tsv`), so "does this cited paper carry the citing
entry's CUI?" is computable for most of the KB. It was computed for the 150-PMID
sample:

| | Count |
|---|---:|
| (PMID, citing entry) pairs where the entry's MONDO has a UMLS match | 147 |
| … where the paper carries ≥ 1 condition tag | 109 |
| … where one of those tags is the entry's CUI | 69 (63 %) |
| … discordant | 40 |

All 40 discordant pairs were read. Every one is a granularity or tagging effect, not
a wrong disease: the paper is tagged with a subtype (severe pre-eclampsia under
`Preeclampsia`; hypertrophic cardiomyopathy 17 under `Hypertrophic_Cardiomyopathy_7`),
a parent (`Congenital disorder of glycosylation` under `CCDC115-CDG`; `Motor neuron
disease` under `Progressive_Muscular_Atrophy`), a synonym MedGen keeps as a separate
concept (Lamb-Shaffer syndrome under `12p12.1_Microdeletion_Syndrome`; urothelial
carcinoma under `Transitional_Cell_Carcinoma`), or only with phenotypes (the Cornelia
de Lange GeneReviews chapter is tagged with cryptorchidism, myopia and reflux but not
with the syndrome). A few tags are simply noise (a COPD update tagged `Streptococcal
pneumonia`). Zero of 150 sampled citations point at a different disease.

So the check would need MONDO-descendant or MedGen-hierarchy expansion before it
could tell "tangential" from "wrong", and even then its true-positive rate on the
present KB looks very low. It is not worth building now. The user guide's own caveat
applies: absence of a tag does not mean the paper is not about the disease.

One incidental finding from the same pass: `Arsenic_Related_Cancers` is anchored to
`MONDO:0005096` *squamous cell carcinoma*, which is why a chronic-inflammation review
matched it. That anchor looks over-broad for an entry about arsenic-related cancers
and is worth a look on its own; it is not changed here.

## Compared with E-utilities

Everything the endpoint returns is also obtainable from documented NCBI services,
but not in one call:

| Signal | Linked Discoveries | E-utilities |
|---|---|---|
| Retracted / expression of concern / erratum | `isRetracted`, `publicationUpdates` | `esummary` `pubtype` + `references`; batch of 200 per call; 18 / 18 agreement |
| Related records | 200 BiomedBERT neighbors, similarity score | `elink cmd=neighbor_score` (100, different algorithm, median 20 % overlap) |
| Condition / gene / chemical tags | per record, in the same response | `elink` to `medgen`, `gene`, `pccompound`, one call per PMID per database |
| Citation edges among the set | `citationEdges`, in the same response | `elink pubmed_pubmed_citedin` / `pubmed_pubmed_refs` per PMID |
| Review / NIH funding | booleans per record | `pubtype` and grant fields per record |
| Abstract | included | `efetch` |

For the retraction census the native route wins outright: it is documented, needs
no cookie, batches 200 PMIDs, and gives the same answer. For neighborhoods the pilot
offers something E-utilities does not — a different similarity model plus
per-disease filtering — which is the reason to keep using it interactively.

## Recommended use

1. **Build the retraction check on `esummary`, not on Linked Discoveries.** Report-only
   first, listing the 11 live citations above for triage; then gate with a shrink-only
   baseline. Cite the retraction notice in the entry rather than deleting silently —
   `PRKN-Related_Juvenile_Parkinson_Disease` and the two rickets groupings show the
   pattern already in use.
2. **Use the pilot interactively during curation and review.** The "Linked
   Discoveries" button on a PubMed abstract page opens the neighborhood; look at it
   for retracted, contradicting or more recent work before citing a seed's claim.
   For a rare disease with its own literature, a neighborhood seeded on the
   GeneReviews chapter is a fast census of what the KB does not yet cite.
3. **Ask NLM before scripting it into a workflow.** The endpoint is undocumented and
   the pilot's terms are "evaluation only". The NLM Help Desk is the contact the
   site names; the question is whether programmatic neighborhood queries at
   curation volume (thousands per week) are welcome, and whether an API is planned.
   Until then `scripts/linked_discoveries_probe.py` stays an evaluation tool: not in
   the justfile, not in CI, paced.
4. **Do not build the MedGen-tag NEC check.** The plumbing exists but the signal is
   granularity, not confusion.
5. **Follow up the incidental `Arsenic_Related_Cancers` anchor** separately.

## Reproducing the measurements

```bash
# a seed's own status (retraction / EoC / erratum / review / tag counts)
uv run python scripts/linked_discoveries_probe.py seed-status 9500320 40526437

# a neighborhood, filtered to one MedGen CUI, marked against kb/ citations
uv run python scripts/linked_discoveries_probe.py neighborhood 20301443 \
    --neighbors 200 --cui C0031269 --mark-kb --format tsv

# PubMed Similar Articles for the same seed
curl -s 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/elink.fcgi?dbfrom=pubmed&db=pubmed&id=20301443&cmd=neighbor_score&retmode=json'

# retraction status for a batch of cited PMIDs (up to 200 per call, POST)
curl -s -X POST https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi \
    -d db=pubmed -d retmode=json -d id=33596356,21610853,42051968 \
  | python3 -c 'import json,sys; r=json.load(sys.stdin)["result"]
for k in r["uids"]: print(k, r[k]["pubtype"], [x["reftype"] for x in r[k].get("references",[])])'

# MONDO -> UMLS exact matches used for the CUI filter
curl -sL https://raw.githubusercontent.com/monarch-initiative/mondo/master/src/ontology/mappings/mondo_exactmatch_umls.sssom.tsv
```

The 150-PMID sample is `random.seed(0); random.sample(sorted(pmids), 150)` over the
unique `reference: PMID:` values under `kb/disorders/`; the 15 neighborhood entries
are the 5 with the most cited PMIDs plus `random.seed(1); random.sample(rest, 10)`
over entries with ≥ 10 PMIDs and a UMLS exact match. Counts are as of the `main`
head on 2026-09-26 and move with every curation PR.
