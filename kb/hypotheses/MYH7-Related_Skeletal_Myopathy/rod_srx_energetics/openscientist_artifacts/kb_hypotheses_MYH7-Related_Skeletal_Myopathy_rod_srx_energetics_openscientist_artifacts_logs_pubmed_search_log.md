# PubMed Search Log — rod_srx_energetics hypothesis

Agent: OpenScientist | Iteration 1 | Search date: 2026-10-16
Database: PubMed (NCBI E-utilities via search_pubmed MCP tool)

| # | Query | max_results | Hits returned | Key PMIDs | Outcome |
|---|-------|-------------|---------------|-----------|---------|
| 1 | MYH7 Laing distal myopathy super-relaxed state myosin | 8 | 0 | — | No results (query too specific) |
| 2 | R1500P myosin mouse model skeletal myopathy hypercontractile | 8 | 1 | 38690726 | Retrieved seed mouse paper |
| 3 | human skeletal myopathy myosin mutations disrupt head sequestration super-relaxed ATP | 8 | 1 | 37788100 | Retrieved seed patient paper |
| 4 | MYH7 rod light meromyosin mutation thick filament assembly myopathy mechanism | 8 | 0 | — | No results |
| 5 | MYH7 myosin storage myopathy Laing distal myopathy pathogenesis | 8 | ERROR | — | 429 Too Many Requests (rate limited) |
| 6 | MYH7 Laing distal myopathy pathogenesis thick filament assembly protein aggregation | 8 | 1 | 22918376 | Competing-mechanism review |
| 7 | myosin super-relaxed state mavacamten hypertrophic cardiomyopathy energetics | 6 | 1 | 40391807 | Variant-specific SRX in HCM |
| 8 | myosin interacting heads motif super-relaxed state thick filament structure regulation | 6 | 2 | 38103642, 28871556 | SRX/IHM structural background; SRX-assay caveats |
| 9 | Laing distal myopathy MYH7 proline mutation coiled coil destabilization biophysical | 6 | 0 | — | No results |

## Iteration 2 additional searches
| # | Query | max_results | Hits | Key PMIDs | Outcome |
|---|-------|-------------|------|-----------|---------|
| 10 | MYH7 Laing distal myopathy clinical phenotype weakness foot drop natural history | 6 | 0 | — | No results (unverified absence) |
| 11 | myosin storage myopathy MYH7 light meromyosin aggregate hyaline body | 6 | ERROR | — | 429 rate limited |
| 12 | myosin storage myopathy MYH7 Laing distal myopathy hyaline body subsarcolemmal | 6 | 0 | — | No results (unverified absence) |
| 13 | myosin super relaxed state skeletal muscle energy metabolism resting ATP | 6 | 4 | 40295335, 36696446, 36528760, 19966283 | Convergent SRX mechanism + methodological caveats |

## Iteration 2 database access (preflight + queries)
Network preflight via `requests` (execute_code sandbox), 2026-10-16:
- mygene.info — HTTP 200 (OK)
- GenCC search.thegencc.org home — HTTP 200 (HTML)
- ClinGen search.clinicalgenome.org/kb/genes/HGNC:7577 — **ReadTimeout** (not accessed)
- gnomAD GraphQL https://gnomad.broadinstitute.org/api — HTTP 200 (OK)
- NCBI eutils einfo — HTTP 200 (OK)

Executed queries:
- **gnomAD constraint (MYH7, GRCh38)** — SUCCEEDED. Query: `gene(gene_symbol:"MYH7"){gnomad_constraint{pLI oe_lof oe_lof_upper lof_z mis_z syn_z obs_lof exp_lof}}`. Result saved to `data/gnomad_MYH7_constraint.json`. Key: pLI=6.6e-21, LOEUF=0.66, mis_z=7.38, obs/exp LoF=129/225.
- **GenCC per-gene JSON** — FAILED/unavailable. `POST https://search.thegencc.org/api/submissions` -> HTTP 404 (json, 21 bytes); `/submissions` -> HTTP 200 but text/html (not parseable here). GenCC gene-disease validity classification NOT retrieved programmatically (knowledge gap, labeled unverified).
- **ClinGen** — not accessed (ReadTimeout on preflight).

## Iteration 3 searches
| # | Query | max_results | Hits | Key PMIDs | Outcome |
|---|-------|-------------|------|-----------|---------|
| 14 | MYH7 distal myopathy reduced myosin force generation thick filament instability weakness mechanism | 6 | 0 | — | No results (unverified absence) |
| 15 | Laing distal myopathy MYH7 muscle weakness mechanism myosin | 8 | 3 | 24664454, 22918376, 22155079 | Clinical spectrum + dominant-negative aggregation mechanism |
| 16 | myosin activator inhibitor mavacamten aficamten skeletal muscle therapy distal myopathy super-relaxed | 6 | 0 | — | No results (unverified absence; skeletal myosin-modulator trial evidence not retrieved) |

## Iteration 3 database queries (ClinVar via NCBI E-utilities, 2026-10-16)
Endpoint: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi (db=clinvar). SUCCEEDED. Saved to `data/clinvar_MYH7_counts.json`.
- MYH7[gene] = 6011; P/LP = 1479
- cardiomyopathy[dis] = 5070; "myosin storage myopathy"[dis] = 397
- Free-text: Laing = 396, distal myopathy = 414, myopathy = 499, myosin storage = 691
- NOTE: "Laing distal myopathy"[dis] and "distal myopathy"[dis] -> 0 (ClinVar disease-vocabulary mapping artifact; free-text counts are the interpretable values).

## Iteration 4 searches
| # | Query | max_results | Hits | Key PMIDs | Outcome |
|---|-------|-------------|------|-----------|---------|
| 17 | skeletal muscle phosphocreatine 31P MRS myopathy energy metabolism fatigue | 5 | 5 | 21719720, 17275621, 12914557, 10545311, 8606701 | 31P-MRS is an established in-vivo energetics tool, but NONE are MYH7/Laing-specific -> documents gap: the raised-basal-ATP prediction has not been tested in vivo in MYH7 patients |

## Notes / limitations
- search_pubmed returns a small number of top hits per query; it is not an exhaustive systematic search. Several specific queries returned 0 hits, which reflects the ranking/matching behavior of the tool, NOT confirmed absence of literature. These are labeled "unverified absence", not "no literature exists".
- One query (#5) failed on NCBI rate-limiting (HTTP 429); not retried this iteration.
- No ClinGen / GenCC / ClinVar / omics dataset was queried this iteration — gene-disease validity and variant curation remain unchecked (knowledge gap).
