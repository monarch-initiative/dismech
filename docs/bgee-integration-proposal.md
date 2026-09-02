# Proposal: how Bgee and ASAP data should be integrated into dismech

*Draft for review by the Bgee and ASAP/scFAIR teams and @cmungall. Prepared 2026-09-01, ASAP/scFAIR section added 2026-09-02. AI-assisted
(Claude Code), with all API behaviour and KB statistics measured rather than
estimated.*

## Summary

dismech would like to use Bgee, but **not** in the way an expression atlas is
usually consumed. We are **not** proposing to import expression calls as evidence
for disease mechanisms, and we think doing so would actively damage both
resources' claims. We are proposing three narrower integrations where Bgee is
uniquely able to answer a question dismech currently cannot:

| | Integration | Status | Depends on Bgee for |
|---|---|---|---|
| **A** | **Cross-species model fidelity** — is the model species' ortholog expressed where the human mechanism operates? | **prototype built and run** | homologous-anatomy expression comparison |
| **B** | **Absent calls as negative evidence** — refuting a mechanism claim, or substantiating a curated model failure | design sketch | conservative propagated absent calls |
| **C** | **Curation-time QC** of cell-type / tissue bindings | design sketch | present calls, as a flag only |

**A is the headline.** It addresses a gap dismech has today — 773 entries record a
`HUMAN_MODEL_MISMATCH` and 138 mechanism links are graded
`FAILS_TO_RECAPITULATE`, all justified in free-text prose with no structured data
behind them — and Bgee is, as far as we can tell, the only resource that can
supply that data, because it already computes cross-species anatomical homology.

The main thing we need from the Bgee team is a read on **cell-type resolution**
and on the **stability of the expression-comparison endpoint**. Details in
[Questions for the Bgee team](#questions-for-the-bgee-team).

We also looked at [ASAP](https://asap.epfl.ch/) and
[scFAIR](https://sc-fair.org/) in the same pass, since they sit in the same
Lausanne/SIB orbit and ASAP is cell-type-native. The short version: ASAP's
**public** catalogue cannot help us today (120 projects, 3 carrying a disease
term, 21 distinct CL terms), but **scFAIR's schema overlaps dismech's
analysis-provenance model closely enough to be worth a conversation**. See
[ASAP and scFAIR](#asap-and-scfair).

## What dismech is, briefly

The [Disorder Mechanisms Knowledge Base](https://github.com/monarch-initiative/dismech)
is a curated, evidence-grounded *mechanism* graph: 2,502 disease entries and 167
reusable mechanism modules, each a causal chain from etiology through molecular
and cellular dysfunction to phenotype. It is deliberately **not** an association
graph — Monarch KG already is one, and dismech's design decisions explicitly
forbid re-implementing it.

Two properties matter for this proposal:

- **Every claim carries a citation with an exact-substring-validated quote.** An
  `EvidenceItem` names a reference, a `supports` polarity, and a `snippet` that a
  validator checks is a verbatim substring of the cached source. Fabricated or
  paraphrased snippets fail CI.
- **Mechanism nodes are bound to ontology terms** — 10,904 CL cell-type bindings
  (521 distinct), 4,750 UBERON bindings (615 distinct), 12,043 HGNC gene bindings
  (3,189 distinct). These are the same ontologies Bgee annotates to, so the join
  is free.

## Why we are not importing expression calls as evidence

We want to state this plainly up front, because it is the *reason* the three
proposals below are shaped the way they are — not a dismissal of Bgee.

**1. Bgee is healthy wild-type by construction.** Bgee rejects samples from
diseased subjects, abnormal genetic backgrounds, knockouts, and treatments not
expected in the wild. That curation policy is a strength, and it is exactly why a
Bgee call cannot support a disease-mechanism claim: it describes the normal
baseline the mechanism *departs from*. "CPS1 is expressed in liver in healthy
people" is a precondition for a hepatocyte urea-cycle claim being coherent, not
support for it.

**2. The propagation direction runs opposite to dismech's granularity.** Bgee
propagates *present* calls to ancestor structures and *absent* calls to direct
descendants. So a present call is safe to generalize and unsafe to specialize —
"expressed in liver" may have propagated up from one sub-region, and reading it
down onto "hepatocyte" inverts Bgee's own semantics. dismech's mechanism nodes sit
almost entirely at the specific end. We measured the consequence: **0 of 20** real
KB cell-type bindings had a direct Bgee call for the corresponding gene, while
every gene returned 74–218 conditions overall. The join only "works" if you walk
part-of closure downward, which is precisely the inference Bgee declines to make —
and would manufacture a false citation.

**3. Present calls are near-vacuous as support.** Every gene we sampled was
`expressed` in 74–218 conditions. Admitting those as evidence would let almost any
tissue claim be "supported" for almost any gene — evidence inflation that
manufactures the appearance of grounding. dismech already carries this caveat for
a comparable resource in `structured_sources/mygeneset.py`: *"gene-set membership
is not mechanism... a lead that should still be backed by a primary citation."*

Note this is **not** an objection to structured-source rows as quotable evidence
in general. dismech happily cites Orphanet, ClinGen, CIViC, and ICEES rows that
way. The difference is that those rows assert something about a *disease*; a Bgee
present-call row asserts nothing about any disease.

This position updates, and sharpens the reasoning of,
[`docs/reports/monarch-kg-dismech-gap-analysis-2026-07-30.md`](reports/monarch-kg-dismech-gap-analysis-2026-07-30.md)
§7, which recommended against importing Bgee on scope-duplication grounds. We
think the conclusion was right but the reason was the weakest available: the
load-bearing reasons are the healthy-only policy and the propagation asymmetry,
both of which are about evidence validity rather than scope.

**The corollary is the interesting part.** The same asymmetry that rules out
present calls makes **absent calls** the one Bgee product that is both
propositional and safe to narrow. That is proposal B.

## A. Cross-species model fidelity

### The gap

A dismech `animal_models[].modeled_mechanisms[]` link asserts that a model in some
species is informative for a named mechanism node, with a `fidelity` grade
(`HIGH`/`MODERATE`/`LOW`/`UNKNOWN`) and free-text `limitations`. Current usage:

| Signal | Count in `kb/` |
|---|---|
| `HUMAN_MODEL_MISMATCH` discussions | 773 |
| `PARTIALLY_RECAPITULATES` links | 335 |
| `FAILS_TO_RECAPITULATE` links | 138 |
| `fidelity` grades recorded | 1,309 |

Every one of these is a curator's prose judgement. None has structured data behind
it. The schema comment for `limitations` literally lists "species divergence,
supraphysiological expression, absent cell types" as the things curators should be
recording — and there is currently no way to check any of them.

### What Bgee can answer

One necessary (never sufficient) condition is checkable:

> Is the model species' ortholog of the disease gene actually expressed in the
> anatomy where the human mechanism operates?

If the ortholog is absent there — or there is no ortholog at all — the model cannot
recapitulate that node *by that gene's action*, whatever grade the curator
assigned.

This needs cross-species anatomical homology, which is the thing Bgee has and
generic atlases do not. The `expression_comparison` endpoint returns, per
homologous multi-species condition, a conservation score plus
`genesExpressionPresent` / `genesExpressionAbsent` / `genesNoData`. That is
almost exactly the required shape.

**Bgee's species coverage is not the constraint — the orthology step is.** Bgee's
52 species include every animal-model species used in `kb/` today: mouse (391
links), zebrafish (39), rat (17), dog (14), and the long tail down to
*Nothobranchius furzeri* and naked mole rat.

The mismatch is upstream of Bgee. *Xenopus laevis* is in Bgee (taxon 8355) but is
**not** in the Ensembl vertebrates division — only *X. tropicalis* is — so Compara
cannot supply an ortholog and those links are skipped rather than silently
mis-mapped onto the sibling species. This is another argument for asking whether
Bgee can resolve orthology internally (question 3): Bgee's own species set is
wider than the one we can currently pre-map against.

### The prototype

`scripts/bgee_model_fidelity.py` (in this PR) implements the check:

```
hgnc:NNNN  --HGNC REST-->  ENSG  --Ensembl Compara-->  model-species ortholog
                                          |
                         Bgee expression_comparison (homologous anatomy)
                                          |
              intersect with the target node's own UBERON/CL bindings
```

Verdicts, of which only the first two are findings:

| Verdict | Meaning |
|---|---|
| `ORTHOLOG_NOT_1TO1` | paralog expansion/loss; the model gene is not a clean substitute |
| `DIVERGENT_ABSENT` | human present, ortholog **absent** in the homologous anatomy |
| `ORTHOLOG_LOOKUP_EMPTY` | Ensembl returned no ortholog — **not** a finding, see below |
| `CONSERVED` | both expressed — the necessary condition holds |
| `MODEL_NO_DATA` / `HUMAN_NO_DATA` | Bgee has no call there |
| `ANATOMY_UNMATCHED` | the node's anatomy has no multi-species condition |

`CONSERVED` is deliberately **not** treated as validating a fidelity grade. Shared
expression is a precondition, not evidence that the model reproduces the mechanism.

#### An empty ortholog list is not evidence of absence

Our first full run treated "Ensembl returned no ortholog" as the strongest
fidelity caveat. That was wrong, and the run's own output is what showed it:
it reported no mouse ortholog for **PTEN** and **VHL**, which is plainly false.

`homology/id/human/ENSG00000171862` (PTEN) returns `homologies: []` against mouse
at HTTP 200, and so does the reverse lookup from mouse `ENSMUSG00000013663` —
yet mouse *Pten* plainly exists (MGI:109583). VHL behaves identically. Whatever
the cause, the endpoint's silence is not evidence of absence, so this verdict is
now a prompt to verify by hand rather than a caveat to act on.

A separate bug in the same area is worth recording because it is the classic one:
the prototype initially cached a failed fetch as "no ortholog", making a transient
rate-limit indistinguishable from a real absence and poisoning the cache so
re-runs reproduced it offline. `GLUL` was reported as having no mouse ortholog for
exactly that reason and resolves cleanly on retry. Fixed — a failed fetch now
raises rather than being cached, matching the convention
`scripts/kg_gene_gap_audit.py` already documents.

**This is the concrete case for question 3 below.** We would rather use one
authoritative orthology source inside Bgee than reconcile this one.

The KB yields **548** model-mechanism links where the target node carries UBERON/CL
anatomy and the disease carries HGNC genes — i.e. the full addressable set for this
check.

### Worked example

`AHCY_Deficiency` curates two models against its hepatocyte node. The check
independently reproduces the curator's distinction:

```
** ORTHOLOG_NOT_1TO1  AHCY_Deficiency  AHCY  Mouse      FAILS_TO_RECAPITULATE   orthology type ortholog_one2many
   CONSERVED          AHCY_Deficiency  AHCY  Zebrafish  PARTIALLY_RECAPITULATES liver: both expressed
```

The mouse model is graded `FAILS_TO_RECAPITULATE` in prose; Compara independently
reports the mouse ortholog is `one2many`, which is a concrete, citable reason a
single-gene mouse knockout may not phenocopy. The zebrafish liver comparison is
concordant with its `PARTIALLY_RECAPITULATES` grade.

### What a full run looks like

A complete sweep over 260 of the 548 addressable links (capped for runtime; the
run is cached and resumable):

| Verdict | Count | |
|---|---|---|
| `ANATOMY_UNMATCHED_CL` | 158 | not evaluable |
| `CONSERVED` | 31 | necessary condition holds |
| `HUMAN_NO_DATA` | 23 | not evaluable |
| `ORTHOLOG_NOT_1TO1` | 17 | **finding** |
| `ANATOMY_UNMATCHED_TISSUE` | 15 | not evaluable |
| `ORTHOLOG_LOOKUP_EMPTY` | 10 | verify by hand |
| `MODEL_NO_DATA` | 6 | not evaluable |
| `SPECIES_UNMAPPED` | 3 | not evaluable |
| `DIVERGENT_ABSENT` | **0** | — |

**Two things in this table are the honest headline, and neither is comfortable.**

First, **79% of links are not evaluable at all** (205 of 260), overwhelmingly
because the node's cell type has no Bgee multi-species condition. The check works;
its yield is bounded by cell-type coverage rather than by anything in dismech.
That is question 1 below, quantified.

Second, **`DIVERGENT_ABSENT` never fired.** That verdict — human present, model
ortholog absent in the homologous anatomy — is the one that would be strongest
evidence for a curated model failure, and across 260 links there was not a single
instance. This is consistent with absent calls being rare in what the comparison
endpoint returns, and it means proposal B currently rests on a datum we have not
yet seen the API produce at scale. We would rather say that plainly than present a
verdict class that has never triggered as though it were working.

The `--tissue-fallback` option recovers some unmatched links by re-trying against
the node's own UBERON locations at explicitly-labelled coarser granularity, but
only for nodes that carry one.

### The findings that survive look right

Spot-checking the `ORTHOLOG_NOT_1TO1` hits against known biology, they are sound
and mechanistically meaningful rather than artefacts:

- **AHCY** → mouse *Ahcy* / *Ahcyl1* / *Ahcyl2*
- **OPN1LW** → mouse, where the human LW/MW tandem duplication has no 1:1 counterpart
- **CSF1R, HARS1, GPC1, SGMS2, VEZF1** → zebrafish, largely the **teleost
  whole-genome duplication**

That last group is the pattern worth naming. A zebrafish paralog pair is a
classic fidelity caveat — knock out one copy and the other may compensate, so a
negative result in the model says less than it appears to. It is exactly the kind
of thing `limitations` is supposed to record, and exactly the kind of thing a
curator working from the literature alone will often miss.

Note this signal comes from Ensembl Compara, not Bgee. Bgee's contribution is the
homologous-anatomy expression comparison downstream of it — which is why question
3 (whose orthology should we be using?) matters for the design.

### How output would be used

**As a curation aid that produces a worklist, never as an auto-written evidence
item.** A `DIVERGENT_ABSENT` or `ORTHOLOG_NOT_1TO1` verdict would prompt a curator to
review the `limitations` text and, where warranted, add a `HUMAN_MODEL_MISMATCH`
discussion — with a primary-literature citation, per the normal evidence SOP. The
Bgee result is the *lead*; the PMID is the evidence. This is the same discipline
dismech applies to deep-research provider output.

## B. Absent calls as negative evidence

Bgee's conservative absent calls — global absence reported only when all
experiments agree, with presence always superseding absence — are the one Bgee
product that is propositional *and* safely narrowable to sub-structures.

Two uses, both of which are genuine evidence rather than leads:

- **Refuting a mechanism claim.** "Gene X is not expressed in tissue Y in healthy
  animals" bears directly on a claim that X acts in Y. This would be an
  `EvidenceItem` with `supports: REFUTE`.
- **Substantiating a curated model failure.** `FAILS_TO_RECAPITULATE` links
  *require* both `limitations` and `evidence` in dismech's schema. An absent call
  for the ortholog in the relevant anatomy is exactly the missing datum.

**Open design question.** This would need a structured-source cache
(`references_cache/BGEE_*.md`) so absent-call rows are quotable and
substring-validated, following the existing Orphanet/ClinGen/ICEES pattern.
Whether that is worth building depends on how many absent calls are actually
retrievable at useful granularity — see the questions below. In our sampling,
absent calls were rare (6 of 200 conditions for one gene) and surfaced through the
`expr_calls` action but not the per-gene page.

## C. Curation-time QC of cell-type and tissue bindings

The KB has **863** ontology-bound pathophysiology nodes that co-assert a gene and
a cell type (1,855 distinct gene/cell-type pairs), plus 340 asserting a gene and a
UBERON location. A Bgee-backed check could flag implausible bindings for curator
review.

We rank this **lowest**, for a reason worth being explicit about: given the
propagation asymmetry, a naive present-call check produces false alarms at exactly
the granularity dismech curates at. It becomes worthwhile mainly if cell-type
resolution improves (question 1 below). It would flag, never auto-correct, and
never emit evidence.

## What we measured

All figures from live API calls and the current `main`, 2026-09-01.

| Measurement | Value |
|---|---|
| KB cell-type bindings with a direct Bgee call for the paired gene | **0 of 20** sampled |
| Multi-species comparison conditions carrying a CL term | **47 of 1,192 (4%)** |
| Model-mechanism links not evaluable (full run, n=260) | **205 (79%)** |
| `DIVERGENT_ABSENT` verdicts across 260 links | **0** |
| TP53 human conditions: UBERON vs CL | 139 vs 6 |
| Typical gene: total conditions / CL-typed | 74–218 / 2–14 |
| HGNC → Ensembl resolution success | 12 of 12 |
| Bgee species covering dismech's animal models | all |
| Addressable model-fidelity links in `kb/` | 548 |

**Operational notes** (all worked around in the prototype, none blocking):

- The JSON API requires **Ensembl gene IDs**; HGNC IDs and symbols return
  "Page not found". We map via `rest.genenames.org`.
- The API returns **403 to default Python `urllib`** user agents; setting an
  explicit `User-Agent` fixes it. `curl` is unaffected.
- **The SPARQL endpoint at `https://www.bgee.org/sparql/` is behind a Cloudflare
  challenge** and returns an interstitial page rather than results to
  programmatic clients. This is the one thing we could not work around.
- The human bulk TSV is 174 MB, `last-modified` 2024-05-17.

## Questions for the Bgee team

Ordered by how much they affect the design. We would rather hear "that's not
what Bgee is for" early than build against a wrong assumption.

1. **Cell-type resolution.** This is the big one. The 2024 NAR paper describes
   Bgee providing "one definitive answer all the way to the cell resolution", but
   what we observe through the API is still overwhelmingly UBERON tissue
   conditions (139 vs 6 for TP53), and none of the 20 KB cell types we sampled had
   a direct call. Are we querying it wrong — is there a parameter or endpoint that
   surfaces the scRNA-seq-derived CL-resolved calls specifically? If not, what is
   the roadmap, and is there a list of cell types with good human coverage today?
   Proposal C, and much of A, scale directly with this.

2. **Is `expression_comparison` a supported public API?** Proposal A depends on
   it. We found it by inspection of the web UI's calls rather than in the
   documentation. Is it intended for programmatic use, does it have stability
   guarantees, and are there rate limits or a preferred access pattern we should
   respect? If it is UI-internal, is there a supported equivalent — or would the
   RDF dump / SPARQL be the intended route?

3. **Orthology handling in `expression_comparison`.** We currently pre-map
   orthologs with Ensembl Compara REST and pass a gene pair. Does the endpoint do
   its own orthology grouping if given a bare multi-species gene list, and if so
   whose orthology calls does it use? We would rather use yours than introduce a
   second, possibly inconsistent, source — particularly since the Ensembl REST
   homology endpoint returned empty ortholog lists for PTEN and VHL against mouse
   (in both directions, HTTP 200), which cost us a round of false findings. If
   Bgee already resolves orthology internally for the comparison, that is
   strictly better for us than what we are doing.

4. **Retrieving absent calls.** Proposal B hinges on these, and our full run
   makes the question sharper: across 260 model-mechanism links the
   `DIVERGENT_ABSENT` verdict never once fired, and `genesExpressionAbsent` came
   back empty in every comparison we inspected. Either absent calls are genuinely
   this sparse at the conditions we hit, or the comparison endpoint does not
   surface them the way we assume.

   Is there a recommended way to retrieve high-confidence absent calls for a gene
   across conditions — ideally with the supporting experiment count — via API
   rather than the bulk TSV? Is `call_type=absent` on the `expr_calls` action the
   intended route? And does `expression_comparison` populate
   `genesExpressionAbsent` under conditions we might simply not have reached?

5. **SPARQL endpoint accessibility.** The Cloudflare challenge blocks
   programmatic access from our environment. Is there an allowlist process, an
   alternate host, or a documented client pattern that gets through?

6. **Stable citable records.** If we build the structured-source cache in
   proposal B, we need a stable identifier and a pinned release. Is there a
   citable identifier scheme for a gene/condition call, and is
   `archives.bgee.org` the right thing to pin a release against? dismech pins
   upstream bulk files by sha256 in a committed manifest, so a versioned URL is
   much better for us than a "current release" one.

7. **Is any of this better done upstream?** If expression-conservation-derived
   model-fidelity signal is something Bgee would rather compute and publish
   itself, we would rather consume that than maintain a derived pipeline. We are
   proposing to build only because we could not find it.

## ASAP and scFAIR

The same Lausanne/SIB orbit hosts [ASAP](https://asap.epfl.ch/) (Automated
Single-cell Analysis Portal, EPFL Deplancke lab + SIB) and the
[scFAIR](https://sc-fair.org/) metadata-standardization consortium. We looked at
both, because ASAP is cell-type-native and cell-type resolution is exactly where
the Bgee check above hits its ceiling.

### ASAP's public catalogue does not close that gap

We pulled the full public catalogue (`GET https://asap.epfl.ch/api/projects`,
11 MB) and measured it:

| | |
|---|---|
| Public projects | **120** |
| Organisms | *Drosophila* 55, human 32, mouse lemur 27, mouse 6 |
| Projects with a disease term other than `PATO:0000461` "normal" | **3** (2 age-related macular degeneration, 1 cataract) |
| Distinct **CL** terms across the whole catalogue | **21** |
| Human projects carrying no cell-type annotation | 18 of 32 |
| Experiment accessions | GEO Series 29, ArrayExpress 46 |

Three consequences, all negative, and we would rather record them than
manufacture a use case:

- **Not a disease-dataset source for dismech.** Our `datasets:` records need
  disease-relevant accessions; three disease projects does not move that.
- **Does not fix the cell-type gap.** 21 distinct CL terms against dismech's 521.
  Cell-type annotation in the catalogue is overwhelmingly FBbt (Fly Cell Atlas)
  and Tabula Microcebus.
- **The interesting surface is not exposed.** ASAP advertises ~14,000 bulk and
  single-cell datasets importable from CELLxGENE, Bgee, EBI SC Atlas, HCA and
  GEO. That federated index is the thing that *would* be useful for dataset
  discovery, and `/external_catalog_candidates` returns HTTP 406 to JSON clients
  with no API route.

Note this is a statement about the **public API catalogue**, not about ASAP as a
platform. We may simply be looking at the wrong surface.

### What ASAP does expose that is interesting

Each project carries a reproducibility triple — `reproducibility_script_url`,
`reproducibility_instructions_url`, and a versioned `asap_data_db` dump — plus a
`project_cell_set_key` content hash. That is a working implementation of what
dismech's hypothesis-analysis `MANIFEST.yaml` regime is reaching for, and worth
comparing notes on regardless of whether any data flows between us.

There is also `GET /api/compliance/checks`, which looks up a previously-run
**scFAIR** compliance check by file URL. It does not run one — that needs a
`.h5ad` / `.loom` upload through the web UI.

### scFAIR is the part with real overlap

scFAIR's schema 7.1.0 includes a structured description of **computational
analysis workflows**, which maps closely onto dismech's own analysis-provenance
model. The two are complementary rather than redundant: scFAIR captures the
happy path in more mechanical detail (container digests, conda environments,
random seeds, resource usage), while dismech captures failure and
unverifiability (execution status, auditability, whether a data source was
actually accessed).

We have written that comparison up separately, including what LinkML modeling
would give each side, in
[`docs/reports/scfair-dismech-schema-comparison-2026-09-02.md`](reports/scfair-dismech-schema-comparison-2026-09-02.md).
It is a schema discussion rather than a data-integration one, so it is kept out
of this proposal.

### Questions for the ASAP / scFAIR team

8. **Is the external catalogue queryable?** The ~14,000-dataset federated index
   over CELLxGENE / Bgee / EBI SC Atlas / HCA / GEO is the surface we would
   actually want for dataset discovery, and we could not reach it
   programmatically. Is there an API, a dump, or a documented route?

9. **Is there a disease-annotated subset we are missing?** The public catalogue
   has three non-normal disease terms. If disease-annotated projects exist behind
   authentication, or if disease annotation is expected to grow, that changes our
   read considerably.

10. **Can scFAIR compliance be checked programmatically?** `/api/compliance/checks`
    looks up existing checks; is there a route to submit a file, or to run the
    validator locally against `rules.yaml`? dismech has no validator for dataset
    quality at all, and this is the one identifier class in our stack with no
    resolution check.

11. **Would a LinkML rendering of the scFAIR schema be welcome?** The analysis
    JSON schema currently has no machine-readable form, so nothing validates it.
    See the companion report for what this would involve and why we think it is
    an offer rather than an imposition — but the prior question is whether
    scFAIR wants a formal schema language at all, given that forking CELLxGENE
    means inheriting its Markdown-spec convention.

## Questions for @cmungall / Monarch

- **Route: direct or via Monarch KG?** Monarch KG already ingests Bgee. Should
  dismech consume this signal through the KG rather than calling Bgee directly?
  Our instinct is direct for proposal A, because the KG's gene→anatomy edges do
  not carry the cross-species homology comparison or the present/absent/no-data
  breakdown that the check turns on — but this is exactly the "don't reimplement
  Monarch" boundary the design decisions care about, so it should be an explicit
  call rather than a default.
- **Does expression conservation belong in the KGX export?** If dismech records a
  structured model-fidelity caveat, that is arguably content Monarch would want
  back.
- **Does this change design decision §6** (evidence & provenance policy)? Our
  reading is that proposal B introduces a genuinely new *kind* of evidence —
  atlas-derived negative evidence about healthy baseline — which the current
  policy does not contemplate either way. If it proceeds it should get a decision-
  register entry rather than arriving as a fait accompli.

## What we are asking for

Not a commitment — a read on whether proposal A is built on a supported
foundation (questions 2 and 3), and whether proposals B and C are worth
building given where cell-type coverage and absent-call access actually stand
(questions 1 and 4). The prototype exists and runs; we would rather adjust it now
than after it has produced a worklist curators have started acting on.

From the ASAP / scFAIR side we are mainly asking whether we are looking at the
right surface (questions 8-10), and whether a schema conversation is wanted at
all (question 11). Nothing there is blocked on an answer — it just determines
whether we build anything.

## Appendix: reproducing the measurements

```bash
# Per-gene expression calls (Ensembl IDs only; needs an explicit User-Agent)
curl -H 'User-Agent: dismech/0.1' \
  'https://www.bgee.org/api/?page=gene&action=expression&gene_id=ENSG00000141510&species_id=9606&display_type=json'

# Present + absent calls
curl 'https://www.bgee.org/api/?page=data&action=expr_calls&display_type=json&gene_id=ENSG00000198947&species_id=9606&get_results=1&limit=200&call_type=absent'

# Cross-species comparison over homologous anatomy (the endpoint proposal A uses)
curl 'https://www.bgee.org/api/?page=expression_comparison&action=submit_expression_comparison&display_type=json&gene_list=ENSG00000198947%0AENSMUSG00000045103'

# Species list
curl 'https://www.bgee.org/api/?page=species&action=species_list&display_type=json'

# The prototype
uv run python scripts/bgee_model_fidelity.py --file kb/disorders/AHCY_Deficiency.yaml
uv run python scripts/bgee_model_fidelity.py --all --findings-only --tsv /tmp/bgee_fidelity.tsv
```

ASAP:

```bash
# Full public project catalogue (~11 MB, 120 projects)
curl -H 'Accept: application/json' 'https://asap.epfl.ch/api/projects'

# One project
curl -H 'Accept: application/json' 'https://asap.epfl.ch/api/projects/ASAP48'

# OpenAPI spec (Swagger UI lives at /api-doc)
curl 'https://asap.epfl.ch/api/openapi.yaml'

# scFAIR validator rule config (the machine-readable form of schema 7.1.0)
curl 'https://raw.githubusercontent.com/DeplanckeLab/asap_web/main/src/config/scfair/7.1.0/rules.yaml'
```

## References

- Bastian et al., *The Bgee suite: integrated curated expression atlas and
  comparative transcriptomics in animals*, NAR 49:D831 (2021).
  [doi:10.1093/nar/gkaa793](https://doi.org/10.1093/nar/gkaa793)
- *Bgee in 2024: focus on curated single-cell RNA-seq datasets, and query tools*,
  NAR 53:D878 (2025). [doi:10.1093/nar/gkae1118](https://doi.org/10.1093/nar/gkae1118)
- Bgee expression-call documentation:
  <https://www.bgee.org/support/tutorial-expression-calls>
- dismech design decisions:
  [`docs/explanation/design-decisions.md`](explanation/design-decisions.md)
- Prior Monarch KG gap analysis:
  [`docs/reports/monarch-kg-dismech-gap-analysis-2026-07-30.md`](reports/monarch-kg-dismech-gap-analysis-2026-07-30.md)
