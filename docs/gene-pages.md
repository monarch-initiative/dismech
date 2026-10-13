# Gene pages

dismech is organised by disease, but most of what it records about a gene is
spread across many disease entries: TP53 is named by about a hundred of them,
PTEN by about twenty. A gene page puts those mentions side by side, next to
what outside sources say the gene normally does, and (for some genes) a short
curated summary of how the gene relates to its diseases.

Pages are published under `pages/genes/`: one per gene named by at least two
disorders, plus any gene with a curated summary, and an index of every gene the
KB names. A gene named by a single disorder gets an index row that links
straight to that disorder.

## Three layers

Each page is assembled from three sources with different rules.

| Layer | Where | Written by | Rule |
|---|---|---|---|
| Ingest | `kb/genes/ingest/*.tsv` | `just genes-ingest-build` | Dropped and reloaded from pinned upstream snapshots. Never edited by hand. |
| KB slice | computed, not stored | `dismech.genes.slice` | Whatever the disease, module and comorbidity entries say right now. |
| Curated summary | `kb/genes/curated/hgnc_<n>.md` | an agent, optionally reviewed | Every checkable statement is a provedown claim recomputed from the other two layers. |

### Ingest: identity and normal function

Three sources, each pinned in `data/<source>/MANIFEST.yaml`:

- **HGNC complete set**, pinned by sha256: symbol, name, locus type, location,
  previous symbols and cross-references.
- **[ai-gene-review](https://github.com/ai4curation/ai-gene-review)**, pinned by
  commit: an AI-assisted review of the gene's GO annotations. Only the
  function layer is ingested (the gene description and its `core_functions`,
  each a molecular function with the processes it drives and where it acts);
  the per-annotation reviews and deep-research files stay upstream and are
  linked.

- **ClinGen gene–disease validity**, pinned by sha256 in `data/clingen-genes/`:
  one row per assertion (gene, MONDO disease, mode of inheritance, tier). This
  is the same CSV `data/clingen/` pins for the quotable `CGGV:` citation cache,
  pinned separately so that moving the gene-page snapshot does not rewrite
  hundreds of cached citation files. A gene page shows the tier and links to
  ClinGen; it is not a citation, and a KB entry still records a tier by copying
  it into `gene_disease_validity` with `CGGV:` evidence.

ai-gene-review is keyed on the UniProt accession, so it is joined to HGNC on
UniProt, never on the folder's gene symbol: symbols are renamed (GBA became
GBA1), and a symbol join silently pairs the wrong records. A review whose
symbol matches an HGNC gene but whose UniProt does not is reported by the build
and left out.

Its content is AI-generated. Gene pages show it as a labelled outside source,
and only for reviews whose upstream `status` is `COMPLETE`. It is never cited
as evidence in a KB entry.

The build refuses an input that does not match its pin: a downloaded file
whose checksum differs, or an ai-gene-review checkout at another commit. A
refresh that fails its checksum leaves the previous pinned file in place.

Only genes some KB entry names, plus any gene carrying a curated summary, are
written — so the tables follow the KB rather than all 45,000 HGNC genes. That
is the same rule the renderer publishes pages under, and the two read it
through one function (`dismech.genes.curated.curated_ids`) so they cannot
drift apart. The summary clause is what makes a gene page possible for a gene
no entry names, which is the normal state of a gene curated *because* it causes
no disease: without its HGNC row the page would be titled with the bare CURIE
and the claims API would report the gene as having no name. The build reports
such genes on their own line (`curated-only genes (no KB entry)`).

To pick up a new upstream release:

```bash
just genes-ingest-refresh --repin   # rewrites the manifests' pins
just genes-ingest-build             # rewrites kb/genes/ingest/
git diff data/hgnc data/ai-gene-review data/clingen-genes kb/genes/ingest
```

Commit the manifest change and the table diff together, as with the Orphanet
and ClinGen snapshots.

### KB slice: what the entries say

A gene is "named" by an entry when a descriptor's `term.id` is an HGNC CURIE
anywhere inside one of the entry's sections: a `genetic[]` record, a
pathophysiology node's `genes`, a subtype's `genes`, an animal model, a
variant, an oligonucleotide's `target_gene`, a carrier's `targeting_receptor`,
and so on. A symbol in prose, or a CURIE inside an evidence snippet, does not
count. The walk is generic rather than a list of slots, so a gene-valued slot
added to the schema later is picked up without a code change.

```bash
just gene-slice hgnc:9588                  # one line per gene
just gene-slice hgnc:9588 --format tsv     # one row per occurrence
just gene-slice --min-disorders 10         # genes named by 10+ disorders
```

The page's disorder table shows each disorder's `genetic[].relationship_type`.
A disorder that has a `genetic[]` record for the gene but no type is shown as
**untyped**, with its free-text `association` beside it. Untyped records are
common, including in the entries most closely identified with a gene (Cowden
Syndrome and PTEN Hamartoma Tumor Syndrome both record PTEN only as
`association: Causative`), so the gene page doubles as a worklist for typing
them.

### ClinGen against the KB

Each ClinGen assertion is matched to the dismech entries whose own disease it
is: the entry's `disease_term`, a `has_subtypes[].subtype_term`, or a
`mondo_mappings` term with `skos:exactMatch`. That is the same rule
`just check-gene-validity` uses. The page then says how each matched entry
records the gene: its relationship type, **untyped**, **no genetic record**,
or **not named**. A ClinGen disease no entry curates is listed as such.

The mismatches are a worklist across the whole KB:

```bash
just genes-clingen-gaps                                  # counts by status and tier
just genes-clingen-gaps --format tsv --classification Definitive
```

On the page, and in the claims API's `clingen_but_untyped()`, only the tiers
that support a relationship (Definitive, Strong, Moderate) mark a gap; the
recipe lists every tier with its classification so the rest can be read too.

Each row is a lead, not a defect. A Definitive tier on an untyped record
usually means the record can be typed `CAUSATIVE` from evidence ClinGen has
already assessed, but a Disputed or Refuted tier on a gene an entry does not
name is a reason *not* to add one. The scope is whatever the ingest tables
cover: genes some KB entry already names, plus any gene with a curated summary.

### Curated summary: prose that is checked

A summary is Markdown with YAML frontmatter. Statements a reader could check
against the KB are written as [provedown](https://github.com/ai4curation/provedown)
result spans: the visible text is the claim, and `data-code` is an expression
that must reproduce it.

```markdown
---
hgnc_id: hgnc:9588
symbol: PTEN
status: DRAFT
---

<details>
<summary>Claim setup</summary>

<pre><code>
from dismech.genes.claims import gene
g = gene("hgnc:9588")
</code></pre>

</details>

PTEN is named by <span class="result" data-code="g.disorder_count()">21<span class="method"></span></span>
disorder entries. Cowden Syndrome's genetic record is
<span class="result" data-code="g.relationship('Cowden Syndrome')">untyped<span class="method"></span></span>.
```

`just genes-verify` and every page build re-run each claim. When the KB changes
so that a claim is no longer true, the summary is marked **stale** on its page,
with the failing claim highlighted and the new value shown; it is not hidden
and the build does not fail. A stale summary needs its prose updated to match
the KB, not the other way round.

The claim methods are in `src/dismech/genes/claims.py`. They return values
shaped for prose: entry names as written in each entry's `name`, and enum
values lower-cased with spaces ("somatic driver"). Methods that check a
specific statement (`node`, `in_module`, `includes`) return what they were given
when it holds and raise an error when it does not. Lists use
`data-compare="names"` with items separated by semicolons, because disease
names and GO labels contain commas ("Glioblastoma, IDH-Wildtype").

Rules for writing a summary:

- **Say only what the KB or the ingest layer says.** A summary is a reading of
  dismech, not a new source. If the summary needs a fact the KB lacks, the fix
  belongs in the disease entry, with its evidence, not on the gene page.
- **Write claims that survive growth.** "Includes X and Y" (`g.includes(...)`)
  stays true when a third disease is curated; an exact list of every disorder
  goes stale on the next curation PR that mentions the gene. Leave complete
  lists to the page's tables.
- **Name mechanism nodes through `g.node(entry, name)`**, which fails if the
  node is renamed or no longer carries the gene.
- **Headings and connecting prose make claims too.** A heading "Germline
  disease" over a checked list of causative entries asserts something no span
  checks. KRAS's causative records include Evans syndrome and melorheostosis,
  both recorded `SOMATIC`, so that heading over them would be false while every
  span passed. Name sections after what
  the KB records ("Causative records"), and state an origin only through
  `g.variant_origin(entry)` or `g.disorders('causative', 'germline')`. Where
  an entry records no origin, the claim reads "unrecorded" and so should the
  summary. Likewise `g.includes(..., relationship='somatic driver')` checks the
  relationship a sentence attributes, where a bare `g.includes(...)` only
  checks that the entry names the gene.
- `status: DRAFT` for agent-written text, `REVIEWED` once a person has read it.
  Verification is computed and is not recorded in the file.

**The verifier only runs code that calls this API.** Summaries are written by
agents and can merge through the automated approve-and-merge path, and
provedown executes the Python a document contains. Before anything runs,
`dismech.genes.curated` checks that the code cells only import `gene` from
`dismech.genes.claims` and bind its result to a name, and that each claim has
exactly the shape `g.<GeneClaims method>(literals)`, optionally inside
`len(...)`. The shape is checked rather than a list of allowed syntax, because
a permissive check admits `g.slice.occurrences.clear()`: no file or process
access, but a call that empties the cached KB index every later summary and
page in the same build reads from. Anything else (another import, an attribute
chain, a non-literal argument, SQL) is refused and the summary is reported as
not verified, with nothing executed.

The same applies to the HTML a summary contains. Raw HTML is limited to
provedown's markup (`<span class="result">`, `<span class="method">`,
`<code>`, `<pre>`) and `<details>`/`<summary>`; everything else is written as
Markdown, and link targets must be http(s) or relative. A summary outside that
allowlist is reported as not verified and its page shows the source escaped.

## Building

```bash
just gen-gene-pages                          # pages/genes/, re-verifying summaries
just gen-gene-pages --gene hgnc:9588         # one page plus the index
just genes-verify                            # summaries only (report-only)
just genes-verify --strict                   # exit 1 on a stale or refused summary
```

The nightly KB sweep runs `just genes-verify --strict` as a non-blocking step,
so a summary made stale by a curation PR shows up as a failed step the next
morning without that PR ever having been held up by it.

`pages/genes/` is derived, like `pages/disorders/`, and is written by the page
build workflow rather than committed by hand. The page build rebuilds every
gene page on each run, because a change to any disorder can change any gene's
page.

## Known limits

- The ai-gene-review comparison is by exact GO identifier. PTEN's KB nodes are
  annotated with PI3K/AKT signalling, and its ai-gene-review core function with
  the negative regulation of that process, so the two share no identifier even
  though they agree. A closure-aware comparison needs the GO hierarchy.
- GenCC, which aggregates ClinGen with other submitters (Orphanet, PanelApp,
  Genomics England), is not ingested yet.
- Comorbidity entries are walked but currently name no genes.
