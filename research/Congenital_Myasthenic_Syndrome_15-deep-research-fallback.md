# Congenital Myasthenic Syndrome 15 Deep Research Fallback

## Provider Attempts

- `openscientist`: `just research-disorder openscientist Congenital_Myasthenic_Syndrome_15`
  completed successfully in 1287 s and returned an 832-line, 9-citation report.
  The report was **discarded without being curated from**, because it is about
  the wrong disease.

## Why the report was discarded

The report's central claim is:

> Finding 1 — CMS15 is a presynaptic CMS caused by biallelic *SLC18A3*/VAChT variants

CMS15 (MONDO:0014542) is the **ALG14** congenital myasthenic syndrome. MONDO
defines the term as "Any congenital myasthenic syndrome in which the cause of
the disease is a mutation in the ALG14 gene", with exact synonym `ALG14
congenital myasthenic syndrome` and cross-reference OMIM:616227. It was
described alongside CMS14 (ALG2, *with* tubular aggregates) in a single 2013
study, PMID:23404334, and the MONDO synonym "without tubular aggregates"
preserves that pairing. *SLC18A3*/VAChT congenital myasthenic syndrome is a
separate entity; the 2025 review of CMS genes (PMID:40533459) lists `ALG14` and
`SLC18A3` as distinct entries in the same gene list.

The report is internally coherent, well-cited science about a real disease. It
is simply not this one, which makes it more dangerous than an obviously broken
report — nothing in it looks wrong. It also asserts OMIM:616227, the *correct*
OMIM number for CMS15, next to the wrong gene, so a curator spot-checking the
identifier would find it matching.

`just preflight-dr <report> MONDO:0014542` scored the report's gene mentions as
`SLC18A3=35, CHAT=10, DAP=4, CHRNE=3, RAPSN=3`. ALG14 does not appear in the top
five. The preflight nonetheless resolved to `SKIP` rather than a failure,
because MONDO records no `RO:0004003` causal gene for this term.

The report itself is deliberately **not committed**. `research/` outputs are
consumed as first-class curation inputs and indexed by disease name, so a
wrong-disease report filed under the CMS15 name would mislead the next curator
and the artifact index. This fallback record replaces it.

Two tooling gaps were filed:

- dismech#9888 — `just research-disorder` passes a hardcoded empty `mondo_id`,
  so every deep-research run for every disease and provider is dispatched with
  no ontology grounding. That is the upstream cause of this misidentification.
- dismech#9889 — `preflight-dr` silently skips its gene-identity check when
  MONDO has no `RO:0004003` assertion, even where the MONDO definition and exact
  synonyms name the gene in plain text, as they do here.

## Literature Scope Used Instead

Curation was anchored on generated PubMed reference caches:

- PMID:23404334 — Cossins et al. 2013, *Brain*. The founding study identifying
  ALG14 and ALG2 as CMS genes; source for the limb-girdle phenotype, the
  ALG13/ALG14/DPAGT1 complex, endplate localisation of ALG14, and the siRNA
  experiment showing reduced surface acetylcholine receptor.
- PMID:28733338 — Schorling et al. 2017, *Neurology*. Five patients from three
  families with the severe infantile form; source for the neurodegenerative
  pole of the spectrum, the recurrent p.Asp74Asn allele, recessive segregation,
  and the temporary-only pyridostigmine response.
- PMID:34971077 — Long-surviving siblings with compound heterozygous ALG14
  variants; source for endplate acetylcholine receptor deficiency, the
  decremental response, imaging findings, and the pyridostigmine benefit.
- PMID:40533459 — 2025 review of the 40 genes causing CMS; used to confirm that
  ALG14 and SLC18A3 are separately recognised CMS genes.
