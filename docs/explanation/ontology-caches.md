# Ontology Term Caches

## Why we commit cache files

The `cache/` directory contains CSV snapshots of ontology term labels (HP, MONDO, GO, CL, CHEBI, MAXO, etc.) used by the term validator. These are **intentionally committed to the repository**, not generated on the fly.

### The problem with live lookups

Ontology labels change over time. If validation fetched labels directly from ontology sources on every run:

- A term label change upstream (e.g., HP renames a phenotype) would cause existing disorder YAML files to fail validation unexpectedly
- Different developers would get different validation results depending on when they last fetched
- CI would be non-deterministic — a passing build today could fail tomorrow with no code changes
- Bulk label updates across dozens of ontologies would create cascading validation failures

### How caches solve this

Committed caches act as a **pinned snapshot** of the ontology labels we validate against:

- **Deterministic validation**: Everyone gets the same results, every time
- **Controlled migrations**: When ontology labels change, we update caches intentionally via `linkml-term-validator migrate-cache --refresh-labels`, review the diffs, and merge as a deliberate PR
- **Minimal churn**: Cache files use deterministic ordering (sorted by CURIE) and preserve timestamps for unchanged entries, so re-running the validator doesn't produce spurious diffs
- **Reproducible CI**: Builds are hermetic — no network dependencies for validation

### Cache structure

```
cache/
├── chebi/terms.csv      # Chemical entities
├── cl/terms.csv         # Cell types
├── enums/               # Dynamic enum membership caches
│   ├── anatomicalentityterm_*.csv
│   ├── biologicalprocessterm_*.csv
│   └── ...
├── go/terms.csv         # Gene Ontology (processes, components)
├── hp/terms.csv         # Human Phenotype Ontology
├── maxo/terms.csv       # Medical Action Ontology
├── mondo/terms.csv      # Mondo Disease Ontology
├── ncit/terms.csv       # NCI Thesaurus
├── uberon/terms.csv     # Anatomy
└── ...
```

Each `terms.csv` contains three columns:

| Column | Description |
|--------|-------------|
| `curie` | The ontology term ID (e.g., `HP:0001250`) |
| `label` | The canonical label at time of caching (e.g., `Seizure`) |
| `retrieved_at` | ISO timestamp of when this entry was last fetched/updated |

### Maintaining caches

**Adding new terms**: When a disorder YAML references a term not yet in the cache, running `just validate-terms-file <file>` will automatically fetch and cache it.

**Refreshing labels**: To update cached labels to match current ontology versions:

```bash
# Preview changes (dry run)
uv run linkml-term-validator migrate-cache --refresh-labels --dry-run

# Apply updates
uv run linkml-term-validator migrate-cache --refresh-labels

# Sort and deduplicate only (no network)
uv run linkml-term-validator migrate-cache --sort-only
```

**Important**: After refreshing labels, check if any disorder YAML files need updating to match the new labels. A label change in the cache means existing `label:` fields in YAML files may no longer match.

### Cache stability (linkml-term-validator ≥0.3.0rc2)

As of v0.3.0rc2, the term validator ensures cache stability:

- **Deterministic ordering**: Entries are sorted by CURIE on every write
- **Timestamp preservation**: Only new or relabeled entries get updated timestamps
- **Idempotent writes**: Re-validating identical data produces identical cache files

This eliminates the spurious diffs that previously occurred when multiple agents or developers ran validation concurrently.

### Anti-patterns

- **Don't use `git add -A` in worktrees** — cache files from other worktrees or validation runs can leak into your commit. Always use `git add kb/ references_cache/ research/` for disorder PRs.
- **Don't delete cache files** to "fix" validation — the cache is the source of truth for what labels we accept. If a label is wrong, update it via `migrate-cache`.
- **Don't manually edit cache CSVs** — use the migration CLI to ensure consistent formatting.
