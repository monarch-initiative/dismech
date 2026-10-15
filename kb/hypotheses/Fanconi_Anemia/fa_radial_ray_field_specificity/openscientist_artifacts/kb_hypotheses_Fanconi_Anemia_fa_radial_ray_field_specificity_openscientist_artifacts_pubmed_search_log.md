# PubMed Search Log — fa_radial_ray_field_specificity

- Provider: OpenScientist `search_pubmed` MCP tool (NCBI E-utilities esearch/efetch backend)
- Endpoint: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/
- Retrieval date: 2026-09-13
- Analyst run: Iteration 1
- Note: `search_pubmed` returned nothing for many highly-specific multi-term queries (apparent AND-of-all-terms behavior); simpler queries were used as fallback. Rate-limit (HTTP 429) hit once and the query was retried.

| # | Query | Result outcome |
|---|-------|----------------|
| 1 | Fanconi anemia radial ray thumb hand anomalies spectrum | 1 hit — PMID 35360980 (seed reference; accessed) |
| 2 | Fanconi anemia p53 p21 apoptosis progenitor hematopoietic stem cell | 2 hits — PMID 23538752, 15753076 |
| 3 | Fancd2 Aldh2 aldehyde developmental defects mouse limb malformation | HTTP 429 rate limit (retried as #5) |
| 4 | preaxial limb bud progenitor proliferation radius thumb specification apoptosis | 0 hits |
| 5 | Fancd2 Aldh2 double knockout mice developmental abnormalities aldehyde | 0 hits |
| 6 | Aldh2 Fancd2 aldehyde DNA damage stem cells | 3 hits — PMID 37348497, 33512438, 22922648 |
| 7 | Fanconi anemia p53 hyperactivation hematopoietic attrition developmental Ceccaldi | 0 hits |
| 8 | Fanconi anemia p53 p21 axis bone marrow failure progenitor attrition | 0 hits |
| 9 | Fanconi anemia p53 axis bone marrow failure | 5 hits — incl. PMID 33723374, 30977208, 37355617 |
| 10 | bone marrow failure Fanconi anemia exacerbated p53 p21 DNA damage response | 1 hit — PMID 22683204 (Ceccaldi 2012, key paper) |
| 11 | radial ray deficiency Holt-Oram TBX5 TAR RBM8A thrombocytopenia absent radius shared developmental | 0 hits |
| 12 | radial ray malformation TBX5 SALL4 Fanconi differential diagnosis | 0 hits |
| 13 | radial ray deficiency genetic syndromes thumb hypoplasia differential diagnosis | 0 hits |
| 14 | radial longitudinal deficiency thumb hypoplasia syndromes | 6 hits — incl. PMID 41984002, 33086350, 33191038, 40520541 |
| 15 | sonic hedgehog anterior limb bud radial ray formation apoptosis patterning | 0 hits |
| 16 | Fancd2 Fanconi anemia limb development sonic hedgehog VACTERL mouse | 0 hits |
| 17 | Fanconi anemia VACTERL sonic hedgehog developmental | 0 hits |
| 18 | Fanconi anemia mouse model congenital malformation apoptosis embryo | 0 hits |
| 19 | Fanconi anemia formaldehyde developmental malformations mice | 0 hits |
| 20 | formaldehyde Adh5 Aldh2 craniofacial skeletal malformation development | 0 hits |
| 21 | acetaldehyde Fancd2 embryonic development craniofacial | 0 hits |
| 22 | aldehyde dehydrogenase alcohol congenital malformation FANCD2 mice | 0 hits |
| 23 | Fancd2 counteracts toxic effects naturally produced aldehydes mice | 1 hit — PMID 21734703 (Langevin 2011) |
| 24 | p53 hyperactivation developmental defects limb craniofacial Mdm2 apoptosis | 0 hits |
| 25 | p53 activation ribosomopathy developmental malformation apoptosis progenitor | 0 hits |
| 26 | Fanconi anemia congenital abnormalities VACTERL phenotype cohort registry | 0 hits |
| 27 | Fanconi anemia phenotype congenital anomalies IFAR classification | 0 hits |
| 28 | Fanconi anemia congenital anomalies genotype phenotype | 6 hits — incl. PMID 35417938 context, 41733882, 41017074 |
| 29 | Fanconi anemia FANCB FANCD1 BRCA2 severe VACTERL limb anomalies | 1 hit — PMID 35417938 (NCI genotype-phenotype cohort) |
| 30 | zone of polarizing activity sonic hedgehog radius ulna anterior posterior patterning limb | 1 hit — PMID 8922533 |

## Iteration 2 additional queries (2026-09-13)

| # | Query | Result outcome |
|---|-------|----------------|
| 31 | Holt-Oram syndrome TBX5 limb development radial ray | 4 hits — PMID 15096952, 16917909, 24664963, 12210327 |
| 32 | TBX5 SALL4 upper limb anterior posterior patterning | 0 hits |
| 33 | thrombocytopenia absent radius TAR syndrome RBM8A | 5 hits — PMID 42147171, 42079218, 40907933, 41925074, 42420238 |
| 34 | SALL4 Okihiro Duane radial ray syndrome mutation | 4 hits — PMID 36829172, 35179219, 37438083, 36635047 |
| 35 | limb bud anterior mesenchyme proliferation apoptosis radius digit formation | 1 hit — PMID 25280231 (radius-selective FGFR effect) |
| 36 | thalidomide preaxial limb defect oxidative stress cereblon SALL4 | 0 hits |
| 37 | Fanconi anemia mouse knockout phenotype absence congenital malformations | 0 hits |
| 38 | Fancd2 Fancg mouse limb skeletal abnormalities developmental | 0 hits |
| 39 | Fanconi anemia mouse models review phenotype limitations | 2 hits — PMID 39491640, 9565158 |

## Negative-search caveat
Direct searches for FA / aldehyde mouse-model studies demonstrating **anterior limb-bud-specific** progenitor apoptosis (queries #4, #15, #16, #18) returned no results. This is an unverified absence limited by the tool's strict AND matching, NOT a curated database negative. A systematic MeSH-indexed search (PubMed advanced, Embase) is required before asserting true absence.

## Iteration 4 — structured-database query (NOT PubMed)

A live, verified computational query was executed against the **Monarch Initiative v3 API** (`https://api.monarchinitiative.org/v3/api`, `biolink:DiseaseToPhenotypicFeatureAssociation`) to test the radial-ray field annotation for FA vs. the two principal competing radial-ray syndromes. This is a structured knowledge-graph query, not a literature search; full results and interpretation are in `monarch_hpo_query.json`.

| Disease (MONDO) | Total D→P assoc. | Radial-ray field annotations retrieved |
|---|---|---|
| Fanconi anemia (MONDO:0019391) | 668 | radius (Radial ray deficiency, Absent/Hypoplastic radius), 1st metacarpal (Aplasia/Short 1st metacarpal), thumb (Absent/Short/Triphalangeal + duplication + preaxial polydactyly) |
| TAR syndrome (MONDO:0010121) | 115 | radius (Absent/Hypoplastic, bilateral radial aplasia) **and** thumb (Absent/Adducted/Broad/Short) |
| Holt-Oram (MONDO:0007732) | 132 | extensive radius + thumb/1st-metacarpal set |

- **Preflight:** endpoint reachability confirmed via `requests` before the query (sandbox blocks `socket`/`glob`; allowed `requests` used instead).
- **ID correction:** first attempt used wrong MONDO ids (TAR MONDO:0008113, Holt-Oram MONDO:0007750) returning sparse nodes (20 / 5 assoc.); correct ids resolved via `/search` → TAR MONDO:0010121, Holt-Oram MONDO:0007732.
- **Sandbox limitation:** execute_code cwd=/app has no write access to the job filesystem (`os.path.isdir` on the /agent/jobs path = False); printed results were transcribed into `monarch_hpo_query.json` via the Write tool. No silent fallback — the query genuinely succeeded; only the file write was relocated.
- **Self-correction:** the query REFUTED the earlier Iteration-2 framing of "TAR spares the thumb" as an annotation-level discriminator — TAR carries thumb annotations. The clinical thumb-preservation teaching concerns penetrance/obligate presence, not absence of any thumb annotation.
- **Limitation:** counts (668 vs 115 vs 132) reflect curation depth, not phenotype frequency; this is an ontology-annotation check, not mechanistic evidence.
