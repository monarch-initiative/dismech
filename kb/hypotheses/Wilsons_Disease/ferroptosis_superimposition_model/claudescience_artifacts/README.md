# ClaudeScience artefact bundle

Supporting materials for `../claudescience.md` — Iron-Related Ferroptosis Superimposition Model in Wilson Disease.

## Figures
- `fig1_evidence_chain.png` — literature support across the six-link causal chain (102 abstracts classified, 0 contradictions).
- `fig2_mechanism_bridge.png` — STRING v12 network: copper axis → ceruloplasmin bridge → iron export → ferroptosis effectors.
- `fig3_human_cohort.png` — human WD iron biomarkers, untreated vs treated vs controls (Gromadzka et al. 2021, PMID 33555495).
- `fig4_sex_subset.png` — sex-stratified iron burden (Gromadzka et al. 2020, PMID 32937238); men carry higher iron.
- `fig5_crosstalk_network.png` — extended 19-gene cuproptosis–ferroptosis crosstalk network; two molecular bridges.

## Data
- `evidence_table.csv` — top-ranked evidence rows per link (PMID, DOI, support grade, extracted finding).
- `data_evidence_matrix.csv` — full per-paper link classification (102 papers × 6 links, Strong/Partial/Mention/Contradicts).
- `data_string_network.json` — STRING v12 network for Fig 2 (10 genes).
- `data_crosstalk_string.json` — STRING v12 network for Fig 5 (19 genes, 23 edges).
- `data_bib.json` — bibliographic metadata for all cited PMIDs.
- `data_subset_abstracts.json` — full abstracts of the human subset papers.
- `data_fulltext_findings.json` — quantitative findings extracted from full texts.

## Code
- `make_figures.py` — regenerates all five figures from the `data_*.json` / `.csv` files in this folder. Run: `python make_figures.py`.

## Provenance
- Literature: PubMed / PubMed Central (NCBI) via the pubmed-mcp connector.
- Networks: STRING v12.0 (Homo sapiens, confidence ≥ 0.70).
- Gene annotations: NCBI Entrez / MyGene.info.
- Link classification and full-text extraction performed with an LLM extractor over abstracts and selected full texts. Grades reflect what abstracts report, not independent replication — verify via PMIDs/DOIs.
