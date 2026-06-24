# Research Provenance: HFM1-related gametogenic failure

**Date:** 2026-06-23
**Curator:** Dragon-AI Agent (claude-sonnet-4-6)
**Trigger:** Issue #3310 (Epic: Gene-axis gametogenic failure / meiotic disorder spectra)
**Branch:** fix/futurehouse-api-key-workflow-and-hfm1-curation

---

## NEC Preflight

MONDO:0014322 confirmed as the correct anchor for HFM1/POF9:
- OMIM: 615724 (premature ovarian failure 9)
- Causal gene in MONDO definition: **HFM1** (helicase for meiosis 1)
- HGNC: 20193
- No named-entity confusion risk — HFM1 has one OMIM disease entry

---

## Primary Literature

All PMIDs fetched via `just fetch-reference` and cached in `references_cache/`.

| PMID | Citation | Key finding |
|------|----------|-------------|
| PMID:35526155 | Xie et al. 2022, *Hum Reprod* | Biallelic HFM1 variants → NOA with metaphase-I arrest; mouse models recapitulate varying degrees of synapsis/crossover defects |
| PMID:34429122 | Tang et al. 2021, *Front Genet* | Homozygous HFM1 variants → NOA; microTESE unsuccessful; metaphase arrest on histology |
| PMID:37574498 | Yao et al. 2023, *Front Genet* | Novel splicing variant in HFM1 → NOA in two brothers |
| PMID:32962729 | Liu et al. 2020, *Fertil Steril* | WES in 24 POI patients; biallelic HFM1 identified as causative |
| PMID:36864181 | Tang et al. 2023, *Reprod Biol Endocrinol* | Homozygous splicing variant HFM1 → gametogenesis defect (NOA + POI) + recurrent implantation failure (RIF) |
| PMID:35486194 | Saebnia et al. 2022, *Hum Reprod* | Splice-acceptor mutation HFM1 → NOA (note: not used in entry — abstract validation needed) |

---

## Deep Research

Deep research was not run for this entry. The entry was curated directly from the primary literature listed above, which was sufficient to construct a well-evidenced four-node pathophysiology model conforming to the `meiotic_prophase_failure` module.

---

## Key Mechanistic Points

1. **HFM1 acts downstream of DSB resection** — unlike MCM8/MCM9 which act at the resection/loading step, HFM1 acts at crossover designation/Holliday junction resolution. No cancer predisposition reported.

2. **Bisexual germ-cell failure** — the same biallelic loss causes POI in 46,XX and NOA in 46,XY; the MONDO anchor MONDO:0014322 captures only the female presentation (POF9) because that was described first. The entry's preferred name broadens this appropriately.

3. **Hypomorphic genotype–phenotype gradient** — mouse knockins of patient hypomorphic variants show varying degrees of crossover reduction, suggesting that residual HFM1 activity modulates severity. This is the basis for the knowledge-gap discussion about RIF in females and microTESE retrievability in males.

4. **Module conformance** — all four pathophysiology nodes map to the `meiotic_prophase_failure` module via `conforms_to`, enabling consistency checking against the shared meiotic mechanism model.

---

## Schema Issues Encountered

The initial Write was blocked by the pre-hook validator with three issues:
1. `GO:0000711` label was "meiotic DNA double-strand break processing" (incorrect); canonical label is "meiotic DNA repair synthesis"
2. `HP:0011961` label was "Azoospermia" (incorrect); canonical label is "Non-obstructive azoospermia"
3. `HP:0200067` ("Recurrent spontaneous abortion") is not in the dynamic PhenotypeTerm enum; the RIF phenotype was removed from the structured phenotypes section and its description moved to the `notes` field and the POI node description.
