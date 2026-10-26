# PubMed / E-utilities search log (OpenScientist)
Search date: 2026-10-25. Tool: mcp search_pubmed + NCBI efetch (requests).

| Query | Results | Usable hits (PMID) |
|---|---|---|
| ATP5F1B hypermetabolism uncoupled oxidative phosphorylation | 1 | 36239646 |
| ATP5F1B dystonia variants ATP synthase | 2 | 40276935, 36860166 |
| congenital hypermetabolism uncoupled oxidative phosphorylation Leu335Pro | ERROR 429 (rate-limited) | — |
| Ganetzky Mootha congenital hypermetabolism ... fibroblasts | 1 | 36239646 (abstract truncated in index; full via efetch) |
| Luft disease mitochondrial hypermetabolism loose coupling | 2 | 14556468 (review), 1249587 |
| ATP synthase F1 beta subunit catalytic mechanism rotary conformational coupling | 6 | 37429854, 24798048, 18579516, 18216260, 18003896, 29360236 (orientation) |
| yeast ATP synthase beta subunit mutation uncoupling proton motive force respiration | 1 | 36239646 (no yeast-specific primary hit returned) |
| ATP5F1A dominant dystonia complex V deficiency movement disorder | 2 | 40672495, 36860166 |
| mitochondrial ATP synthase deficiency basal ganglia dystonia selective neuronal vulnerability energy | 0 | — (negative) |
| ATP5F1B hypermetabolism twins neurological phenotype follow-up | 0 | — (negative) |
| ATP5MC3 dominant dystonia mitochondrial ATP synthase subunit c | 2 | 34636445, 36860166 |
| mitochondrial uncoupling thermogenesis proton leak hypermetabolism weight loss | 0 | — (negative) |

## Full-abstract retrievals (NCBI efetch, retmode=text)
- PMID 36239646 (NEJM 2022;387:1395-1403; doi 10.1056/NEJMoa2202949): retrieved full abstract.
  KEY: "elevated oxygen consumption and decreased mitochondrial membrane potential";
  "In yeast, mutations affecting the same region loosen coupling between the proton motive force
  and ATP synthesis, resulting in high rates of mitochondrial respiration. Expression of the mutant
  allele in human cell lines recapitulates this phenotype."
  CURATION FLAG: the seed-YAML snippet ("these results suggest the increased oxygen consumption rate
  is caused by dissipation of the proton motive force, without a corresponding increase in ATP synthesis")
  is NOT present in the NEJM abstract (likely from full text / figure legend). Verify against full text.
- PMID 36860166 (Brain 2023;146:2730-2738; doi 10.1093/brain/awad068): retrieved full abstract.
- PMID 40672495 (medRxiv 2025.07.08.25330848; doi 10.1101/2025.07.08.25330848): PREPRINT; efetch returned
  metadata/authors; abstract body not available via index. Treat as preprint-level, not peer-reviewed.

## Negative searches (absence checked, date 2026-10-25)
- No primary paper found reporting side-by-side respiration + complex V activity across both-arm variants.
- No paper found reporting a patient with BOTH hypermetabolism and dystonia from an ATP5F1B variant.
- No dedicated yeast primary paper surfaced via the queries used (mechanism cited within PMID 36239646).

## Snippet verification (Iteration 5, 2026-10-25) — programmatic exact-substring checks vs live efetch abstracts
- PMID 36239646: seed-YAML snippet "...increased oxygen consumption rate is caused by dissipation of the proton motive force..." => ABSENT from NEJM abstract (False). CONFIRMS curation lead CL-1.
- PMID 36239646: replacement snippet "elevated oxygen consumption and decreased mitochondrial membrane potential" => PRESENT (True).
- PMID 36239646: "loosen coupling between the proton motive force [and ATP synthesis]" => present in abstract but exact-substring test returned False due to a line-wrap/newline artifact in efetch text; present after whitespace normalization. Use normalized whitespace when curating.
- PMID 34636445: "impaired complex V activity, ATP generation, and oxygen consumption" => PRESENT (True). CONFIRMS CL-2.
- PMID 36860166: "no decrease of ATP5F1B protein amount but severe reduction of complex V activity..." => PRESENT (True).
