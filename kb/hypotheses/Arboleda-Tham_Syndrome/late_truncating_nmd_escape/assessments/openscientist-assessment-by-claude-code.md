# OpenScientist report on `late_truncating_nmd_escape` — assessment narrative

Companion to `openscientist-assessment-by-claude-code.yaml`, which is authoritative.

## What this run contributed

A distinction rather than a citation, and it is the right distinction. The hypothesis
bundles two claims that stand on completely different footing:

- **The clinical claim** — truncations in the last two *KAT6A* exons associate with a more
  severe phenotype — is robustly supported, with three independent cohorts converging on
  the same directional gradient.
- **The molecular claim** — those alleles produce a translated protein acting by gain of
  function or dominant interference — is structurally plausible and experimentally
  unproven.

Keeping them apart matters for curation, because a well-supported severity gradient is not
evidence about mechanism, and `functional_impact_category` records mechanism.

## The framing conclusion

*KAT6A* is among the most loss-of-function-intolerant genes in the genome (pLI 1.0, LOEUF
0.079), and early decay-competent truncations are unambiguously pathogenic. Haploinsufficiency
is therefore the baseline mechanism for this disease, and the late-truncating branch is
better read as a severity modifier layered on top of it than as a competing primary
mechanism that replaces it. The entry's hypothesis description was amended to say so; its
`ALTERNATIVE` status was kept, which the report explicitly endorses.

This is the same correction the Bainbridge-Ropers run produced for ASXL3 and the ADNP run
for ADNP — three of five screens, reached independently and by different routes. Here it
comes from population constraint; there it came from cohort severity and from a failed
protein hunt. Independent convergence on the same shape is worth more than any one of them.

## What was not promoted

Nothing. The three cohorts cited for the severity gradient were already the entry's own
evidence for this branch. That is not a failure of the run — an independent search
returning the same sources and reading them the same way is a check on existing curation —
but it means this screen's value was entirely in its framing.

## Bundle quality

The best-provisioned of the five bundles. It is the only one carrying an environment
record, naming the runtime, the package version, the fact that no random seeds were used,
and every external source by stable identifier and retrieval date. Its two PubMed search
logs record negative searches, including the truncated-protein query returning zero
papers, so the absence that keeps the molecular claim unproven is checkable against the
exact expression run rather than asserted.

It still omits the `MANIFEST.yaml` and analysis code, so both analyses are `PARTIAL` and
the analysis-run gate cannot be applied. The domain-retention analysis delivered no output
table at all; its result exists only as prose.

## Disposition

Category stays `UNKNOWN`. One hypothesis description amended. No new evidence promoted.
