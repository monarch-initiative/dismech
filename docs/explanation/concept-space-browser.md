# A shared concept-space browser

Status: proposal, with a freshness audit on 2026-09-20. No repository migration,
scoring change, or deployment has been enacted.

## Recommendation

Evolve `monarch-initiative/dismech-ont-scores` into the downstream home for both
ontology navigation and embedding exploration. Keep its repository name and URLs
initially; use **DisMech Concept Explorer** as the eventual product name. Creating
a separate embeddings repository would duplicate entity indexes, source snapshots,
release machinery, and freshness problems without improving the user's journey.

The shared unit is a selected concept and its neighborhood. Ontology association,
text similarity, and curated causal edges are different ways to explore that
neighborhood, with different evidential meanings. Combine navigation and identity;
keep the methods and scores explicit.

This follows the [design decisions](design-decisions.md): DisMech remains the
mechanism-first source of curated assertions (§1), its causal graph keeps its
meaning (§3), and the browser does not mint a new ontology. Similarity results
are derived exploration aids, never new curated causal or equivalence assertions.

## What is stale, and why

The audit used DisMech revision
`ee19405a11cbea07871522b3f33c8c868764cf80` and ont-scores revision
`567c7b957ed44fd4803aa89f87e21c403cfdf67e`, plus the live published payloads.

| Surface | Observed snapshot | Refresh problem |
|---|---|---|
| [Ontology scores](https://monarch-initiative.github.io/dismech-ont-scores/) | Live manifest generated March 29, 2026; 59,720 rows and 5,548 terms | No repository-authored Actions workflows. Pages serves committed output from `main` using the legacy branch build. Last Pages run was March 29. |
| [Disease embeddings](https://dismech.monarchinitiative.org/app/embeddings/) | 720 records in each of four spaces; live payload is byte-identical to the committed file last changed April 16 | No embedding generation step in the DisMech workflows. Publishing existing JS does not refresh vectors. |
| Mechanism embeddings (`app/embeddings/mechanisms_data.js`) | Committed payload last changed February 4; 1,235 points across 304 diseases | Same absent regeneration path; this is a separate payload from disease embeddings. |

The current checkout has 3,052 `kb/disorders/*.yaml` files. That comparison
demonstrates drift; it is not a requirement that every disease have a nonempty
representation in every space. Future builds must report intentional exclusions.

### Ontology-score generation has a missing prerequisite

The downstream [justfile](https://github.com/monarch-initiative/dismech-ont-scores/blob/567c7b957ed44fd4803aa89f87e21c403cfdf67e/justfile)
invokes `python -m dismech.export.context_score`. That module is absent from
current DisMech main. It is also absent from the source revision recorded in the
[published manifest](https://monarch-initiative.github.io/dismech-ont-scores/build/site-data/indexes/manifest.js),
`c7158080b76a8791f3083c8adc0c410c1385065c`. GitHub's path-specific commit API
returns no commits for that path on the default branch. A filename search in the
available local DisMech workspaces did not recover it either.

This does not prove that the exporter never existed on another branch or as
uncommitted code. It does mean a clean checkout cannot reproduce the published
scores. Recover and version that implementation before enabling a daily build.
Do not approximate its scoring formula from the README and silently publish the
result as the same method. If recovery fails, a replacement needs a named method
version, reviewed semantics, and an explicit comparison with the old output.

The existing browser shard builder is present downstream. Its `dismech_sha`
currently describes the checkout supplied when packaging TSVs, not necessarily
the checkout that produced those TSVs. The exporter must produce an input
manifest, and the packager must preserve and validate it rather than restamping
old scores with a fresh checkout SHA.

### Scheduling the legacy embedder is insufficient

In `src/dismech/embed.py`, each `index_*` method inserts the supplied records only
when its collection is empty or `recreate=True`. Re-running ordinary indexing
against a populated collection therefore keeps old content and misses additions
and removals. The grouped rebuild recipes use `--recreate`, but also delete the
vector caches, forfeiting reuse and making a daily API build unnecessarily costly.

`get_embeddings()` and the mechanism exporter read every row in
`all_embeddings`. A reusable text cache can contain earlier versions and deleted
entities; it must not define the published entity set. Display names parsed back
out of embedding text are also unsuitable as join keys.

Separate the current entity inventory from the vector cache. Rebuild the inventory
from each source snapshot; resolve only its current rendered-text hashes against
the cache; publish exactly that set. Cache keys must include model/revision,
template hash, preprocessing version, and rendered text. Changed metadata alone
can reuse a vector, while changed text, a renamed node, and a deleted disease
must produce the correct current inventory.

## Follow the NAMs/history deployment pattern

Both [monarch-nams](https://github.com/monarch-initiative/monarch-nams/blob/main/.github/workflows/pages.yml)
and [dismech-history](https://github.com/monarch-initiative/dismech-history/blob/main/.github/workflows/pages.yml)
have repository-owned workflows with `push`, `pull_request`, `workflow_dispatch`,
and daily `schedule` triggers. Each checks out fresh upstream DisMech inputs,
builds and validates a disposable site, and deploys a Pages artifact outside PRs.
This is the appropriate pattern; sharing a reusable workflow can wait until the
actual build contracts converge.

Implement `.github/workflows/pages.yml` **in ont-scores**, after exporter recovery:

1. Check out the browser and a separate DisMech source tree, with
   `persist-credentials: false`; capture both exact SHAs once. Use a sparse source
   checkout containing the KB, exporter, templates, configuration, and dependency
   lockfile actually needed by the build. Every view uses this same snapshot.
2. Install the locked generator environment. Fetch required ontology releases
   explicitly, recording versions and checksums. Ontology caches accelerate
   downloads; they must not hide which release supplied a closure.
3. Export scores and build the active embedding inventory. Reuse vectors by
   content/model key; missing cache entries must remain rebuildable. Build all
   indexes, neighbors, projections, and TSVs into a clean `dist/` directory.
4. Run contract tests and validate the complete artifact before upload. PR builds
   use small fixtures and no API credentials; a local embedding backend permits
   integration tests without a paid provider. Never publish PR output.
5. Use `actions/configure-pages@v5`, `actions/upload-pages-artifact@v4`, and a
   separate `actions/deploy-pages@v4` job. Give the build `contents: read`; give
   only deployment `pages: write` and `id-token: write`, with the `github-pages`
   environment. Separate PR concurrency groups from the publishing group.
6. Change the repository's Pages source from branch publishing to Actions when
   the first validated artifact is ready. Preserve the existing download paths
   and `#term/<ontology>/<id>` routes. Do not commit regenerated site data.

Use a daily cron offset from the existing NAMs/history jobs plus manual dispatch.
Upstream dispatch is optional latency reduction; the schedule should work without
a cross-repository write token. Set timeouts after measuring a full fresh build,
since ontology closure and embedding generation are heavier than history
extraction. Keep the last successful site on a failed build, expose its actual
source date, and link to workflow failures. A deployment timestamp must never
masquerade as a data-generation timestamp.

## One browser, several views

Start with a shared search box, selection state, and detail panel, retaining the
existing specialized views behind tabs. A term selection lists associated
diseases and highlights those same diseases in the embedding map. A disease
selection exposes its annotated terms, text neighbors, and mechanism nodes. A
mechanism selection shows its source pathograph, annotations, and similar nodes
across diseases and modules.

For example: select a cell type, inspect the disease ranking and its supporting
nodes, open those diseases in the mechanism map, then inspect a neighboring node
that lacks that cell annotation. That last step is a curation lead, not an inferred
annotation. The interface should make it easy to see whether a neighborhood is
explained by shared curated terms or only by similar wording.

| View | Relationship presented | Explanation shown |
|---|---|---|
| Ontology | Disease–term association and ontology propagation | Direct support, supporting nodes, traversed predicates, specificity and score components |
| Embeddings | Similarity within one declared representation/model | Rendered source text, full-vector cosine neighbors, model and template provenance |
| Pathograph | Curated causal edges and explicit module conformance | Source node, predicate, evidence and the original entry |

Do not average ontology scores and cosine similarity into a default universal
score. Their scales and interpretations differ. Do not rank neighbors using 2D
UMAP/t-SNE distances; use the original vector space. A projection is a visual
layout and may move when the corpus changes. Distinguish disease-level and
mechanism-level representations rather than putting their independently fitted
coordinates on a common map.

### Identity and artifact contract

Use typed keys: ontology CURIE; disease source path/slug; module source path/slug;
and mechanism `(source path, node name)`. MONDO IDs are mappings, not unique
disease-record keys: entries can lack a mapping or use scoped mappings to the
same term. Node names are stable within a snapshot, not immutable across renames;
persist source revision with bookmarked node references and report unresolved
old names rather than matching approximately.

One release manifest should carry:

- Source and browser SHAs, source snapshot time, build time, artifact format and
  scoring-method versions, and checksums for all published payloads.
- Ontology release identifiers/checksums and closure predicates.
- Per-space model identifier/revision, template/preprocessing hashes, vector
  dimension, projection method/parameters/seed, and neighbor metric.
- Current eligible IDs, represented IDs, and excluded IDs with reasons; failures
  are not silent exclusions. Different representation coverage is visible.

All views in a release must agree on the source inventory. If an expensive
embedding build runs less often, expose it as a separately dated snapshot and
disable cross-view joins for missing/changed entities; do not stamp it current.
The simpler first implementation is an atomic daily release of both views.

## Migration sequence and acceptance criteria

1. Recover the score generator and demonstrate a clean-checkout rebuild. Capture
   its algorithm contract and provenance before changing the UI. This is the
   current blocker for automatic ontology-score refresh.
2. Repair the embedding inventory/cache boundary and test add, edit, rename,
   deletion, unchanged-text reuse, and model/template invalidation. The existing
   `dismech.node_embeddings` backend abstraction is a candidate for reuse; its
   current model2vec path is CPU-based and has no API-key requirement. Pin the
   model revision and evaluate retrieval quality before replacing legacy vectors.
   Its current CLI supports evaluation/suggestions, not a ready-made site export.
3. Add the downstream build and publish the two existing views with shared source
   provenance. Retain legacy URLs until verified redirects preserve useful
   selection state. Keep extraction/scientific methods in DisMech initially;
   downstream owns packaging, UI, and deployment.
4. Add shared identity/search/selection and the cross-view journey above. Only
   then consider a repository rename; it is unnecessary to deliver the feature.

The first release must pass a clean build without developer-local files, verify
every shard/download and internal entity reference, and account for every eligible
input. Tests must show that removed records disappear even with a warm vector
cache, identical inputs reuse vectors, and source changes invalidate the right
artifacts. Browser smoke tests should follow a term to a disease to a mechanism
and back, including old deep links and an entity without embeddings. Simulate a
failed generation step and verify that it cannot deploy a partial/current-looking
site. No new schedule or redirect is activated by this proposal.
