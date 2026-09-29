# Curated MONDO proxy-merge rerun

The [migration](../../proxy-merges/README.md) changed constraints in 43 Mendelian
inputs while preserving all hypotheses and priors. The original inputs and
baseline scores are retained in its manifest and baseline directory.

Current combined results, including the seven-case longer retry:

| Result | Before | After |
|---|---:|---:|
| All high-prior mappings consistent | 0 | 21 |
| Completed with retractions | 22 | 1 |
| Timed out | 21 | 21 |

All 21 consistent results have confidence 0.9. COL11A2 retains one DO retraction
at 0.5 after resolving its separate MeSH conflict. Timeout scores are excluded
from completed confidence statistics. CANVAS and cblE now accept both curated
external equivalents; each result matches exhaustive enumeration of 512 distinct
consistent assignments.

`attempts.tsv` records the initial 60-second, eight-worker run: 14 consistent,
one retracted, and 28 timed out. Seven formerly completed searches were retried
with a 300-second limit and two workers in
[the separate retry ledger](../curated-proxy-merges-retry/attempts.tsv); all
seven completed. `comparison.tsv` and `summary.json` combine the latest attempts.
`retractions.tsv` contains only completed retractions from the initial run;
the retry introduced none. Manifests retain exact input hashes, solver revision,
settings, and source-cohort hashes.

Reproduce from `analyses/` with a clean `BOOMER_SRC` checkout at
`744038e30741009930f57919ca2f03c6473ed198`:

```bash
just boomer-proxy-migrate
just boomer-proxy-solve
just boomer-proxy-retry
just boomer-proxy-summary
```

The old `pending` and `unique-solutions-completed` ledgers remain historical.
Their input hashes intentionally differ for the migrated entries; do not
rewrite those ledgers or treat them as scores for the current constraints.
