# Longer proxy-merge retry

Seven previously completed searches reached the initial 60-second limit after
proxy-merge permissions expanded their search space. With a 300-second limit
and two workers, all seven completed with all high-prior mappings accepted and
confidence 0.9. They took approximately 35–39 seconds each at this concurrency.

The exact source cohort is `../../proxy-merges/retry.tsv`. This directory keeps
its own manifest and attempt ledger; the initial batch is preserved separately.
See the [combined comparison](../curated-proxy-merges/comparison.tsv) and
[migration report](../../proxy-merges/README.md).
