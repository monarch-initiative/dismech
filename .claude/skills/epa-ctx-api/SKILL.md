---
name: epa-ctx-api
description: >
  Query EPA's CompTox Chemicals Dashboard APIs (CTX) for chemical identity and
  ToxCast/Tox21 bioactivity. Use when resolving a chemical name or CAS number to
  a DTXSID, looking up an assay endpoint's intended gene target, checking whether
  a chemical is active in a named ToxCast assay, verifying a hit-call or AC50
  before citing it, or deciding whether a chemical-to-gene claim is backed by a
  real measurement. Covers the live API host, the key, the endpoint map, and the
  response quirks that make a naive read of the data wrong.
---

# EPA CTX APIs: chemical identity and ToxCast bioactivity

A chemical-to-gene statement is an assertion. *"This chemical is active in this
named reporter assay, whose intended target is that gene"* is a measurement with
a method attached. These APIs are where the second kind comes from, and the
method is also what carries the limitation: a reporter assay reads an isolated
acute molecular event in one well, not an organism-level outcome.

**This skill documents the API response, not what dismech keeps.** The cache
files written under `references_cache/` carry a deliberately reduced subset of
the fields described below, so a field named here may not appear there.

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
  "https://comptox.epa.gov/ctx-api/chemical/search/equal/bisphenol%20a"
```

In this repository the key lives in `CTX_API_KEY`, exported from `~/.zshenv`
so every shell and every `just` recipe inherits it. Never write the key into a
file under the repository, a cache file, or a commit message.

## Endpoint map

**The authoritative list is EPA's own OpenAPI spec**, not this table:

```
https://comptox.epa.gov/ctx-api/docs/bioactivity.json     # 30 bioactivity paths
https://comptox.epa.gov/ctx-api/docs/bioactivity.html     # the same, rendered
```

Equivalent specs exist per domain at `docs/chemical.json`, `docs/exposure.json`
and `docs/hazard.json`. The narrative companion is EPA's
[*CTX APIs User Guide*](https://epa.figshare.com/articles/online_resource/CTX_APIs_v1_0_0_User_Guide/28892738)
on figshare, CC0.

Read the spec before assuming a lookup is unavailable. The table below is the
subset this repository uses, **not** the full 30. `Size` is the measured response
body, `by-dtxsid` rows on bisphenol A and `by-aeid` rows on endpoint 2.

| Path | Returns | Size |
|---|---|---|
| `chemical/search/equal/{name}` | Matches carrying `dtxsid`, `dtxcid`, `casrn`, `preferredName`. The name-to-DTXSID entry point. | 305 B |
| `chemical/search/{by}/{query}` | `by` is `equal`, `starts-with` or `contains`. Prefer `equal`, and read the `rank` field before trusting a hit. | varies |
| `chemical/detail/search/by-dtxsid/{dtxsid}` | One record: formula, mass, plus `totalAssays`, `activeAssays`, `percentAssays`, `toxcastSelect`. | 2.4 KB |
| `bioactivity/assay/` | **All 1,570 assay-endpoint annotations.** Fetch once and cache it; never per query. | 8.2 MB |
| `bioactivity/assay/search/by-aeid/{aeid}` | One endpoint's annotation. This is the per-claim lookup. | 5.2 KB |
| `bioactivity/data/search/by-dtxsid/{dtxsid}` | **Every measurement for one chemical**, 2,798 rows for bisphenol A. | 19.7 MB |
| `bioactivity/data/search/by-aeid/{aeid}` | Every measurement for one endpoint, across all chemicals. | 20.9 MB |
| `bioactivity/data/summary/search/by-dtxsid/{dtxsid}` | One row: `activeMc`, `totalMc`, `activeSc`, `totalSc`, and the cytotoxicity burst columns. | 371 B |
| `bioactivity/data/summary/search/by-aeid/{aeid}` | One row of active counts for that endpoint. | 101 B |

### Four resources beyond the table, worth knowing exist

**Batch POST variants.** `by-dtxsid`, `by-aeid`, `by-spid` and `by-m4id` each have
a `POST` form taking a list. Fetching fifty chemicals is one request, not fifty.

**AOP links.** `bioactivity/aop/search/by-toxcast-aeid/{aeid}`, and the same by
`by-event-number` and `by-entrez-gene-id`, return AOP-Wiki Key Event and AOP
numbers with live `aopwiki.org` links. Endpoint 2 maps to Key Event 1394 and AOP
220. Roughly one endpoint in seven has a record, so expect an empty list.

**Administered equivalent dose.** `bioactivity/data/aed/search/by-dtxsid/{dtxsid}`
converts in-vitro potency to an administered dose in mg/kg/day through `httk`
PBTK and three-compartment models, at 50th and 95th percentiles. This is the route
from a micromolar assay concentration to something comparable with human exposure;
bisphenol A returns 662 records.

**Assay lookup by gene symbol.** `bioactivity/assay/search/by-gene/{geneSymbol}`
returns each endpoint for a gene with its active counts. `ESR1` returns 36.

### Version provenance

There is **no version endpoint** — the spec has no such path, and
`bioactivity/version` and `chemical/version` both return `404`. But the release is
not unrecoverable: the AED payload carries `invitrodbVersion` and `httkVersion` on
every record, currently `invitrodb_v_4_2` and `httk_v_2_3_1`. Prefer those to a
bare retrieval date when pinning a manifest.

## How "active" is decided

The property is `hitc`, the **continuous hit call** on each concentration-response
series, and the cutoff is **0.90**.

Everything in this section is quoted from the `tcpl` package's *Introduction and
Appendices*
[vignette](https://cran.r-project.org/web/packages/tcpl/vignettes/Introduction_Appendices.html),
sections *Hit Calls* and *Data Interpretation*. `tcpl` is the pipeline that
computes these values and is described in
[PMID:27797781](https://pubmed.ncbi.nlm.nih.gov/27797781/) (Filer et al.,
Bioinformatics 2017). The threshold's own source is Nyffeler et al. 2023, cited by
that vignette.

`hitc` is not a measurement. It is the product of three proportional weights, each
the probability that one condition holds, so it lands between 0 and 1. In tcpl's
own wording the three are:

1. *"The winning AIC value is less than that of the constant model"* — the fitted
   curve beats a flat line.
2. *"At least one median response is outside the cutoff band"* — some dose group's
   median response actually cleared the cutoff.
3. *"The top of the fitted curve is outside the cutoff band"* — the curve's
   predicted maximum clears it too.

So a series scores high only when the response is real, observed, and predicted to
exceed a threshold. The threshold itself is `coff`, reported per row, and is *"the
maximum of all values given by the methods assigned at level 5"* — where several
cutoff methods apply to an endpoint, the largest wins.

**The 0.90 cutoff is EPA's convention, not a property of the data.** tcpl states
that *"for current ToxCast work, a hitc greater than or equal to 0.90 is labeled
active, whereas anything less was considered inactive"*, and gives the reason: the
threshold follows other tcplfit2 implementations (Nyffeler et al., 2023) and
*"reflects the apparent bimodal nature of the hitc distribution, where a
preponderance of the hitc fall between 0 and 0.1 and 0.9 and 1.0"*. The same
passage says users may binarize at a different threshold. A chemical is therefore
"active" at a stated stringency, and the number is what to quote.

**`hitc` of -1 means the series could not be fitted.** It is a tcpl v2 code for a
concentration-response series tcpl was *"unable to fit"*, for instance fewer than
four concentrations. It is neither active nor inactive and must not be read as a
low score.

## Four things that make a naive read wrong

A naive read is one that takes the response's shape to match the question being
asked of it, and so assumes three things: that there is one record per assay
endpoint, that activity is a yes-or-no answer, and that an intended gene target
is present and means what the endpoint's name suggests. None of the three holds.

Each fails silently: the response is well-formed, the code does not error, and
the result is a false statement about a measurement.

**1. One endpoint usually has several rows.**
`bioactivity/data/search/by-dtxsid` returns one row per *sample per fitted
model*, not one per assay endpoint. Bisphenol A comes back as 2,798 rows over 981
endpoints and 107 sample ids. Two thirds of those endpoints, 657 of 981, carry
more than one row; the median is 2 and the maximum is 13.

**2. Rows within one endpoint disagree.** Endpoint 742, `OT_ER_ERaERa_0480`, is
an Odyssey Thera protein-fragment complementation assay in HEK293T cells that
reads estrogen receptor alpha homodimerization as a fluorescence gain, at the
8-hour timepoint the name's `0480` denotes in minutes. For bisphenol A it carries
three rows at `hitc` 1.000 and three at 0.000.
Quoting one row as *the* result for that endpoint is cherry-picking whichever row
the code happened to reach first. Either report the spread and the sample count,
or key the citation on the sample.

**3. The hit-call is a probability, not a boolean.** For bisphenol A: about 1,780
rows at 0.0 and 658 at 1.0, but roughly 340 strung between them, and 27 rows at
`-1`, which means unfittable. Write the number, not the word. See
**How "active" is decided** above.

**4. The intended gene target is often absent, and cannot be read off the name.**
`gene` is populated on 1,109 of the 1,570 endpoints and `null` on 461, and the
gaps are not where you would guess.

One laboratory assay often yields several endpoints, and only the one carrying the
biological readout is annotated with a gene. A beta-lactamase reporter produces
three: `_ch1` is the uncleaved substrate signal, `_ch2` the cleaved product
signal, and `_ratio` their quotient, which is the measure of receptor activity.
EPA labels them `substrate`, `product` and `ratio` in `assayFunctionType`
accordingly. So `TOX21_ERa_BLA_Agonist_ratio` carries `ESR1` while
`TOX21_ERa_BLA_Agonist_ch1` and `_ch2` carry no gene at all, even though all three
come from the same experiment on the same receptor. Viability counter-screens
likewise carry none.

Where a gene is present, it is a **list**. Forty-one endpoints name more than one,
and `OT_ER_ERaERb_0480` names both `ESR1` and `ESR2`, so a hit there does not
isolate one receptor.

Each gene object carries `geneSymbol`, `officialSymbol`, `entrezGeneId` and
`uniprotAccessionNumber`. Note the symbol is species-specific: endpoint 725 is
`NVS_NR_mERa` and its gene is mouse `Esr1`, Entrez 13982, not human `ESR1`. An
`organism` field on the annotation says which — 1,324 of the endpoints are human,
135 rat, 46 zebrafish.

## Reading an annotation

The fields worth carrying into a citation, from `bioactivity/assay/search/by-aeid/`:

| Field | Why it matters |
|---|---|
| `assayComponentEndpointName` | The name a curator will cite, e.g. `TOX21_ERa_LUC_VM7_Agonist`. |
| `gene[]` | Intended target. See quirk 4. |
| `assayFunctionType` | `reporter gene`, `binding`, `signaling`, and so on. This is the method, and so the limitation. |
| `signalDirection` | `gain`, `loss`, `bidirectional`. A `loss` assay reading down is not inhibition of the disease process. |
| `intendedTargetFamily` | `nuclear receptor`, `kinase`, `cyp`, … |
| `organism`, `tissue`, `cellShortName` | Species and system. |
| `assaySourceName` | `TOX21`, `NVS`, `ATG`, `ERF`, … |
| `cellViabilityAssay` | True for a counter-screen. A hit here is cytotoxicity, not target activity. |
| `citations[]` | Real `pmid`, `title`, `author` for the assay's own publication. Cite this for the method. |
| `normalizedDataType` | The scale `top` is expressed on: `percent_activity`, `log2_fold_induction`, `log10_fold_induction`, `fold_induction`. A `top` cannot be read without it. |

`cellViabilityAssay` and the burst columns in the chemical summary
(`cytotoxMedianUm`, `cytotoxLowerUm`) are how you tell a specific target effect
from a chemical that is simply killing the cells at that concentration. A hit
whose AC50 sits above the cytotoxicity threshold is suspect.

## Potency and efficacy: `ac50` and `top`

These are two different things, and a row needs both to be read.

- **`ac50` is potency**: the concentration at which the response reaches half its
  maximum. A low `ac50` means the chemical acts at a low concentration. `tcpl`
  defines it as *"the active concentration at 50% maximal response (AC50) for the
  winning model"*, and elsewhere as *"50% activity concentration"*.
- **`top` is efficacy**: the fitted maximum response itself, as a change from
  baseline. A small `top` means the response was slight however low the `ac50`.
  `tcpl` gives `|top|` as *"absolute value of the maximal predicted change in
  response from baseline (i.e. y=0)"*, and calls it *"top modeled efficacy"* where
  it is compared against the cutoff.

A hit can be potent and feeble at once, so neither number alone characterises it.
Both sit inside `mc5Param`, which also carries `ac5`, `ac10`, `ac20`, `acc`,
`bmd`, `bmdl`, `bmdu`, `coff` and `hitcall`. There is no top-level potency field.

**These field names are the API's, and the definitions are upstream.** The CTX
response is the ToxCast pipeline's level-5 output, so the authority for what each
field means is the `tcpl` package that produces it, not this skill and not the API
docs. Check a field against its *Introduction and Appendices*
[vignette](https://cran.r-project.org/web/packages/tcpl/vignettes/Introduction_Appendices.html),
which carries a field dictionary, before relying on it; the package is described
in [PMID:27797781](https://pubmed.ncbi.nlm.nih.gov/27797781/) (Filer et al.,
Bioinformatics 2017).

Both definitions say "for the winning model", which is why one endpoint yields
several different AC50s: the model selected differs per row.

**On units, the upstream dictionary and the API disagree in emphasis.** tcpl's
dictionary states flatly that the `conc` column of its data tables "is
micromolar", while also defining `tested_conc_unit` as "the concentration unit for
the concentration values in the data-containing tables". The API surfaces the
latter as `testedConcUnit` per row, and for bisphenol A it reads `uM` on 2,775
rows and is **`null` on 23**. Those 23 still carry `concMin` and `concMax`, so a
concentration is reported with no unit stated on the row; 18 of them are also
active and carry an `ac50`. Micromolar is the overwhelming convention and is
documented as such, but where the row declines to say so, do not supply the unit
on its behalf.

Because the winning model differs per row, **AC50 varies within one endpoint**:
bisphenol A on endpoint 117 spans 0.089 to 35.5 µM across nine rows. Report a
range, not a point.

`mc3Param` and `mc4Param` carry the full concentration-response series and every
candidate model's parameters. They are the bulk of the 19.7 MB and belong in
no cache file.

## Scope: do not mirror ToxCast

Fetch narrowly, for the claim in front of you. One chemical's full bioactivity
response is 19.7 MB of which a citation needs a few lines, and the dose-response
series inside it is not evidence a curator can quote.

The repository route, which writes a quotable cache file, is the dismech
structured source rather than raw `curl`:

```bash
just toxcast-fetch DTXSID7020182       # cache the record for one chemical
just toxcast-list                      # what is already cached
```

Raw `curl` is for reconnaissance: confirming an endpoint exists, reading a field
you have not seen before, checking an annotation. **A hit-call, an AC50 or an
intended gene target is only citable from a `references_cache/TOXCAST_*.md` row,
never from a raw response you read once and never from memory.** That is the same
rule CLAUDE.md applies to ontology CURIEs, and for the same reason: a
well-formed, plausible, entirely fictional `aeid`/gene pair is easy to produce
and gives no internal signal that it was invented.

## Bulk route, if per-chemical fetching is too slow

invitroDB is published whole, and is the right route for a corpus-wide analysis
rather than a per-claim lookup:

- [invitroDB on EPA figshare](https://epa.figshare.com/articles/dataset/ToxCast_Database_invitroDB_/6062623)
- assay description documentation, also on figshare
- the summary files linked from EPA's *Exploring ToxCast data* page, hosted on
  `clowder.edap-cluster.com`

All are far larger than anything that should enter this repository. Use them
outside it and cache only the rows a curated claim cites.

## Licence

EPA states the CompTox data are "free of all copyright restrictions, and are
fully and freely available for both non-commercial and commercial use", which is
what makes committing derived cache files into this repository acceptable. Record
the retrieval date and the invitroDB release in the manifest; the release is
available from the AED payload, as **Version provenance** above describes.
