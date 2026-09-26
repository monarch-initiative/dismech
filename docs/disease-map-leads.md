# Disease Map Leads (MINERVA)

`scripts/fetch_pdmap.py` pulls a MINERVA-hosted disease map's curated reactions
into `pathways/pdmap/` as **curation leads**. It defaults to the
[Parkinson's disease map](https://pdmap.pages.uni.lu/) (`pdmap.uni.lu/minerva`,
project `pd_map_spring_24`, version `Apr'24`, CC-BY 4.0), but nothing in it is
PD-specific: every MINERVA instance serves the same REST API, so
`--instance`/`--project` retargets it at another map.

```bash
just pdmap-list                 # submaps the project serves
just pdmap-fetch                # write pathways/pdmap/
just pdmap-fetch --submap "LRRK2 activity"
just pdmap-leads 40             # the worklist: cited PMIDs kb/ does not cite
```

## Why this exists

The PD map compiles over 1,500 papers into reaction-level diagrams, and each
reaction carries the PubMed IDs its curators read. That is the same shape as a
dismech causal edge plus its evidence — and the overlap with what dismech already
cites is almost nil. At the first run: **1,562 cited PubMed IDs across 23 submaps,
of which 14 appear anywhere in `kb/`**, and one in `Parkinsons_Disease.yaml` (which
cites 92 of its own). Run `just pdmap-fetch` for current figures; the totals move
with both the map and the KB.

The map was already known here as a *modelling* substrate — `Parkinsons_Disease`
carries the cohort-specific probabilistic Boolean models built from it
(PMID:39429779, `model_format: SBML-qual`), curated in stage 3 of
[`superpowers/plans/2026-08-28-boolean-modeling-and-pathographs.md`](superpowers/plans/2026-08-28-boolean-modeling-and-pathographs.md).
It was not used as a source of curation leads at all.

## A reaction is a lead, never evidence

A map reaction asserts that its cited paper supports that interaction. A dismech
evidence item asserts more: that a named sentence in a *cached* reference says so.
So an adopted lead still goes through `just fetch-reference PMID:NNNNNNN` and an
exact quote, exactly as if the map had never been consulted.

Two specific traps:

- **The article titles in these files come from MINERVA, not from
  `references_cache/`.** They are recorded so a curator can triage without a
  network call. Never copy one into a `reference_title:` slot — that slot is
  copied from the cache file's own `title:` frontmatter, and
  `just check-reference-titles` exists because composed-looking titles have
  reached commits before.
- **1,562 PMIDs is not 1,562 edges.** Most reactions sit *below* dismech's node
  granularity: the PD pathograph is ~29 multi-scale pathophysiology nodes, where
  the map is molecular species and reactions. Which reactions deserve a node is
  the curation judgement, and no export makes it.

## What the files contain

| Path | Contents |
|---|---|
| `pathways/pdmap/index.yaml` | source provenance (instance, project, version, licence, MeSH disease, retrieval date) and one row per submap |
| `pathways/pdmap/<submap>.yaml` | the submap's referenced reactions, plus the annotated elements they use |
| `pathways/pdmap/lead_pmids.tsv` | one row per cited PubMed ID: reaction count, submaps, whether `kb/` cites it, whether `references_cache/` holds it, and MINERVA's title/journal/year |
| `pathways/pdmap/.cache/` | raw API responses (gitignored; `--refresh` to bypass) |

By default only reactions carrying at least one PubMed reference are written —
an unreferenced reaction is structure, not a lead. `--all-reactions` includes
them, and `index.yaml` records which was used in `source.reaction_filter`, so the
omission is never silent.

Reaction and modifier types are the map's own (`State transition`,
`Positive influence`, `Catalysis`, `Inhibition`, …), recorded verbatim. They are
deliberately *not* translated into a dismech causal predicate: `downstream` edges
are unsigned (a signed `causal_effect` is a schema follow-up in the plan above),
and the translation is a judgement, not a lookup.

Element annotations become CURIEs, with `hgnc:` lowercased to match this
repository's convention. HGNC, UniProt, NCBI Gene, Ensembl, ChEBI, GO, Reactome,
MeSH, EC and PubChem are kept; InChI, InChIKey, STITCH, RefSeq and VMH are
dropped as bulk that helps no curator.

## The standard exports, if you need the map itself

There is no need to write a parser. `GET /minerva/api/convert/` lists four
interchange formats, in and out — CellDesigner SBML, SBML, SBGN-ML, GPML — and any
submap downloads in any of them:

```bash
curl -o m.zip "https://pdmap.uni.lu/minerva/api/projects/pd_map_spring_24/models/5151\
:downloadModel?handlerClass=lcsb.mapviewer.converter.model.sbml.SbmlParser"
unzip -p m.zip model.xml | head   # the response is a zip holding model.xml
```

Measured on submap 5151 (*Mitochondrial and ROS metabolism*), against the 184
reactions and 146 PubMed IDs the REST API reports for it:

| Format | Reactions | Distinct PubMed IDs |
|---|---:|---:|
| SBML L3V2 | 184 | 146 |
| CellDesigner SBML | 184 | 146 |
| SBGN-ML | — (1,002 glyphs) | 140 |

Prefer SBML: the annotations are plain MIRIAM RDF (`bqbiol:isDescribedBy` →
`identifiers.org/pubmed:…`), polarity is SBO-coded on reactions and modifiers
(`SBO:0000013` catalyst, `SBO:0000461` essential activator, `SBO:0000537` complete
inhibitor, `SBO:0000171` necessary stimulation, `SBO:0000407` absolute
inhibition), and SBGN-ML is layout-oriented and dropped 6 of the 146 PMIDs.

For the Boolean route, [CaSQ](https://pypi.org/project/casq/) consumes the
CellDesigner export and emits SBML-qual directly — that is the published pipeline
behind PMID:39429779 and needs no dismech code.

## Retargeting at another map

```bash
just pdmap-list --instance https://host/minerva --project some_project_id
just pdmap-fetch --instance https://host/minerva --project some_project_id \
    --out pathways/some-map
```

Check the project's licence in the `index.yaml` the run writes before committing
the output, and record the map as an `external_assertions` entry on any disease
entry curated from it.
