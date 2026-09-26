---
name: epa-ctx-api
description: >
  Query EPA's CompTox Chemicals Dashboard APIs (CTX) for ToxCast and Tox21 assay
  metadata — what each assay endpoint measures. Use when looking up an assay
  endpoint's intended gene target, target family or biological process; when
  checking which assays exist for a gene; when deciding whether an assay endpoint
  could correspond to a mechanism; or when refreshing the cached annotations.
  Covers the live API host, the key, the endpoints that serve assay descriptions,
  and the ways the gene-target field misleads.
---

# EPA CTX APIs: ToxCast assay metadata

An **assay endpoint** is one measurement ToxCast makes: a named readout, in a
named system, aimed at a named molecular target. This skill covers how to read
EPA's descriptions of those endpoints.

**Scope: assay metadata only.** Chemical results — which chemicals were active in
which assay, at what potency — are deliberately not covered here, and dismech has
made no decision about whether they belong in the knowledge base. That question
is issue #12682. Do not fetch, cache or cite a hit-call on the strength of this
skill, and do not treat ToxCast as a citable reference source: there is no
`TOXCAST:` reference prefix and nothing under `references_cache/`.

## EPA CTX API URL

The live base URL, taken from EPA's own client
([USEPA/ctx-python](https://github.com/USEPA/ctx-python), `src/ctxpy/base.py`):

```
https://comptox.epa.gov/ctx-api/
```

That host answers. Every data path returns `401` without a key and `200` with
one.

EPA's own CTX API landing page, and dismech issue #12682, both still link
`api-ccte.epa.gov`, which no longer resolves. Use the base URL above.

## The key

A free individual key is requested by emailing `ccte_api@epa.gov` with your
name, email and organization. It is sent by hand, so allow a day or two.

Pass it as a header on every request. There is no query-parameter form.

```bash
curl -s -H "accept: application/json" -H "x-api-key: $CTX_API_KEY" \
  "https://comptox.epa.gov/ctx-api/bioactivity/assay/search/by-aeid/1816"
```

In this repository the key lives in `CTX_API_KEY`, exported from `~/.zshenv`
so every shell and every `just` recipe inherits it. Never write the key into a
file under the repository.

## In this repository

```bash
just toxcast-refresh            # cache all endpoint annotations under data/toxcast/
just toxcast-refresh --summary  # describe what is already cached
just toxcast-refresh --force    # refetch
```

The cache is gitignored; `data/toxcast/MANIFEST.yaml` is committed and records
the retrieval date. Read it in code through
`dismech.toxcast_assays.default_annotations()`, which returns parsed
`AssayEndpoint` objects. That module is deliberately **not** a
`StructuredSource`: it emits no `references_cache/` files because nothing it
caches is citable evidence.

## Endpoint map

**The authoritative list is EPA's own OpenAPI spec**, not this table:

```
https://comptox.epa.gov/ctx-api/docs/bioactivity.json     # 30 bioactivity paths
https://comptox.epa.gov/ctx-api/docs/bioactivity.html     # the same, rendered
```

The narrative companion is EPA's
[*CTX APIs User Guide*](https://epa.figshare.com/articles/online_resource/CTX_APIs_v1_0_0_User_Guide/28892738)
on figshare, CC0. Read the spec before assuming a lookup is unavailable.

Below are the paths that serve assay metadata. The spec's other paths return
chemical results and are out of scope here.

| Path | Returns |
|---|---|
| `bioactivity/assay/` | **All ~1,570 endpoint annotations**, one object each with roughly 52 fields. Several megabytes; fetch once and cache. |
| `bioactivity/assay/search/by-aeid/{aeid}` | One endpoint's annotation. The per-claim lookup. |
| `bioactivity/assay/count` | The endpoint total, as a bare number. |
| `bioactivity/assay/search/by-gene/{geneSymbol}` | Every endpoint for a gene. `ESR1` returns 36. |
| `bioactivity/assay/search/by-endpoint/?endpoint=<name>` | An `aeid` from an endpoint name. The query parameter is `endpoint`; omitting it, or calling it `name`, returns `400`. |
| `bioactivity/aop/search/by-toxcast-aeid/{aeid}` | AOP-Wiki Key Event and AOP numbers, with live `aopwiki.org` links. Endpoint 2 maps to Key Event 1394 and AOP 220. Roughly one endpoint in seven has a record, so expect an empty list. |
| `bioactivity/aop/search/by-event-number/{n}` | The same, keyed on a Key Event. |
| `bioactivity/aop/search/by-entrez-gene-id/{id}` | The same, keyed on an Entrez gene. |

There is **no version endpoint**: the spec has no such path, and
`bioactivity/version` returns `404`. So the invitroDB release cannot be read from
any of the paths above, which is why the manifest records a retrieval date.

## Reading an annotation

Seven field groups define an endpoint's biological attributes, and each
constrains something different:

| Field | Example | What it constrains |
|---|---|---|
| `gene[]` | `ESR1`, estrogen receptor 1, Entrez 2099, UniProt P03372 | the molecular target |
| `intendedTargetType` / `Sub` | protein / receptor | what kind of thing the target is |
| `intendedTargetFamily` / `Sub` | nuclear receptor / steroidal | the target's class |
| `biologicalProcessTarget` | regulation of transcription factor activity | the process being read |
| `organism`, `tissue`, `cellShortName` | human, breast, MDA-kb2 | the system it was measured in |
| `assayFunctionType` | antagonist, binding, reporter gene | the method, and so the limitation |
| `signalDirection` | gain, loss, bidirectional | which way a hit reads |

Four more are worth carrying:

| Field | Why |
|---|---|
| `assayComponentEndpointName` | The name anyone will cite, e.g. `TOX21_ERa_LUC_VM7_Agonist`. |
| `assayFormatType` | `cell-based`, `biochemical`, `cell-free` or `organism`. A large minority are not cell-based. |
| `cellViabilityAssay` | True for a counter-screen, where a hit is cytotoxicity rather than target activity. |
| `citations[]` | Real `pmid`, `title`, `author` for the assay's own publication. Cite this for the method. |

Two prose fields sit alongside them: `assayComponentTargetDesc` describes the
target, and `assayComponentEndpointDesc` how the endpoint was fitted. The target
description usually restates the gene inline, so the target is stated twice and
can be checked against itself:

> ...antagonist activity regulated by the human androgen receptor
> [GeneSymbol:AR | GeneID:367 | Uniprot_SwissProt_Accession:P10275].

## The gene target is often absent, and cannot be read off the name

This is the field most likely to mislead, and the reason a gene-symbol match is
not a mapping.

`gene` is populated on 1,109 of the ~1,570 endpoints and `null` on the rest. Of
those 1,109, one yields no usable symbol: endpoint 1848 names
`luciferase [Cloning vector pGL3-Basic, complete sequence]` with a null symbol
and null Entrez id, which is the assay's reporter enzyme rather than a
biological target. So 1,108 endpoints name a target you can work with.

**One laboratory assay often yields several endpoints, and only the one carrying
the biological readout is annotated with a gene.** A beta-lactamase reporter
produces three: `_ch1` is the uncleaved substrate signal, `_ch2` the cleaved
product signal, and `_ratio` their quotient, which is the measure of receptor
activity. EPA labels them `substrate`, `product` and `ratio` in
`assayFunctionType` accordingly. So `TOX21_ERa_BLA_Agonist_ratio` carries `ESR1`
while `TOX21_ERa_BLA_Agonist_ch1` and `_ch2` carry no gene at all, even though
all three come from the same experiment on the same receptor. Viability
counter-screens likewise carry none.

**Where a gene is present, it is a list.** Forty-one endpoints name more than
one, and `OT_ER_ERaERb_0480` names both `ESR1` and `ESR2`, so a hit there does
not isolate one receptor.

**The symbol is species-specific.** Endpoint 725 is `NVS_NR_mERa` and its gene is
mouse `Esr1`, Entrez 13982, not human `ESR1`. The `organism` field says which:
1,324 endpoints are human, 135 rat, 46 zebrafish. Matching on an upper-cased
symbol merges orthologs, which is what a coverage count wants and not what a
species-specific claim wants.

Each gene object carries `geneSymbol`, `officialSymbol`, `officialFullName`,
`entrezGeneId` and `uniprotAccessionNumber`. Prefer an identifier over the
symbol. Note dismech binds genes to HGNC, which neither identifier is, so a
mapping step is needed rather than a copy.

## Licence

EPA states the CompTox data are "free of all copyright restrictions, and are
fully and freely available for both non-commercial and commercial use", which is
what makes caching derived data in this repository acceptable. The cached
annotations are gitignored because they are large and regenerable, not because of
any licence restriction; `data/toxcast/MANIFEST.yaml` records the retrieval date.
