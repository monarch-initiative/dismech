# Concept Explorer and embeddings

The disease and mechanism embedding browsers now live in the
[DisMech Concept Explorer](https://monarch-initiative.github.io/dismech-ont-scores/),
alongside ontology associations. Their old URLs redirect there and preserve
`?focus=<disease name>&space=<representation>` selections.

Choose an ontology term, inspect its associated diseases, and follow **Explore
similarities and mechanisms** into the map. Disease details link to individual
mechanisms; mechanism details link to curated annotations, downstream nodes,
module conformance, and the original DisMech entry. **Clear term selection**
returns to the whole similarity space.

## Freshness and methods

The downstream repository builds daily from a fresh DisMech main checkout and
publishes a validated Pages artifact. Its source SHA, data-build timestamp,
coverage, model, and build-status link are visible. A release manifest records
input hashes, ontology versions and output checksums. Generation failures retain
the last successful snapshot rather than publishing incomplete data.

The new local model2vec representations replace the old OpenAI ada snapshots;
cosine values and plot positions are not numerically comparable across those
models. Neighbors use full-vector cosine similarity; the map uses a separate PCA
projection. Similarity is a curation lead, not evidence of shared causation.

The ontology score implementation is also explicitly versioned as
`context-v2-max-product`: the original exporter was not recoverable. Read the
[method contract](https://github.com/monarch-initiative/dismech-ont-scores/blob/main/METHODS.md)
for the formula, propagation predicates, exclusions and limitations. The
[original audit and architecture](explanation/concept-space-browser.md) records
why the browsers were combined.

## Development

The UI, source extraction, score export and publication pipeline are maintained in
[dismech-ont-scores](https://github.com/monarch-initiative/dismech-ont-scores).
Curated assertions remain here in `kb/`. To rebuild the browser, run in its repo:

```bash
uv sync --locked
uv run python scripts/build_site.py --source /path/to/dismech
uv run python scripts/build_site.py --validate
uv run python -m http.server 8000 --directory dist
```

No paid API key is needed. The first run downloads the pinned local model and
ontology snapshots. Vectors are reused by model/revision/text hash, while the
current entity inventory is rebuilt independently, so edits, renames, and
removals cannot leave stale entities in the published map.

`src/dismech/embed.py`, the `just embed-*` recipes, and committed embedding JS
remain available as legacy research tools/artifacts; they no longer supply the
public browser. In particular, legacy ordinary indexing does not refresh an
existing nonempty collection, and its export enumerates the vector cache; do not
use it as a fresh current-KB export. The independent `dismech.node_embeddings`
evaluation/suggestion CLI remains available for research.
