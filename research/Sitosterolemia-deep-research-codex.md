---
provider: codex-local-synthesis
model: gpt-5
cached: true
start_time: '2026-05-11T00:00:00Z'
end_time: '2026-05-11T00:00:00Z'
duration_seconds: 0.0
template_file: codex_sitosterolemia_manual_curation
template_variables:
  disease_name: Sitosterolemia
  category: Mendelian
citation_count: 3
source_providers:
- pubmed
- mondo-cache
- clingen-cache
---

## Question

Curated deep-research synthesis for a disease-level sitosterolemia dismech entry
focused on FDA surrogate endpoint integration.

## Output

# Sitosterolemia Curation Synthesis

## Disease Identity

- MONDO cache check: `MONDO:0008863` has exact label `sitosterolemia`.
- Local ClinGen cache check: `cache/clingen/gene_validity.csv` records both
  `ABCG5 -> sitosterolemia (MONDO:0008863)` and
  `ABCG8 -> sitosterolemia (MONDO:0008863)` as definitive autosomal recessive
  gene-disease relationships.
- Curation implication: a standalone `Sitosterolemia.yaml` entry is more
  appropriate than mapping the FDA row to a generic hyperlipidemia disorder.

## Exact PMID-backed Quote Inventory

### Core Disease Framing and Gene Mechanism

- PMID:33807969
  - `Sitosterolemia is a lipid disorder characterized by the accumulation of dietary xenosterols in plasma and tissues caused by mutations in either ABCG5 or ABCG8.`
  - `ABCG5 ABCG8 encodes a pair of ABC half transporters that form a heterodimer (G5G8), which then traffics to the surface of hepatocytes and enterocytes and promotes the secretion of cholesterol and xenosterols into the bile and the intestinal lumen.`
  - `promotes the secretion of cholesterol and xenosterols into the bile and the intestinal lumen.`

- PMID:14769702
  - `Sitosterolemia is a recessively inherited disorder that results from mutations in either ABCG5 or G8 proteins, with hyperabsorption of dietary sterols and decreased hepatic excretion of plant sterols and cholesterol.`
  - `hyperabsorption of dietary sterols and decreased hepatic excretion of plant sterols and cholesterol`

### Plant Sterol Accumulation and FDA Readout

- PMID:14769702
  - `markedly elevated plasma and tissue sitosterol and campesterol levels`
  - `Sitosterol concentrations decreased by 21% (P<0.001) in patients treated with ezetimibe compared with a nonsignificant 4% rise in those on placebo (between-group P<0.001).`
  - `Campesterol also progressively declined`
  - `Ezetimibe produced significant and progressive reductions in plasma plant sterol concentrations in patients with sitosterolemia, consistent with the hypothesis that ezetimibe inhibits the intestinal absorption of plant sterols as well as cholesterol, leading to reductions in plasma concentrations.`

### Clinical Features and Hematology

- PMID:29984642
  - `The main clinical features are tendinous and cutaneous xanthomas, arthritis or arthralgia, premature cardiovascular disease and atherosclerosis.`
  - `Hematological abnormalities (hemolytic anemia and macrothrombocytopenia) may be present in 25-35% of patients, in whom it is usually associated with the main clinical features, as occurs in the 70% of the cases.`
  - `the peripheral blood smear is essential and reveals giant platelets and stomatocytes`

## Pathograph Decisions

- Proximal mechanism: `ABCG5/ABCG8 sterol efflux deficiency`.
- Central biochemical event: `Plant sterol accumulation`, with sitosterol and
  campesterol as the measured sterols.
- Clinical consequence links:
  - `Plant sterol accumulation` -> `Premature atherosclerosis`
  - `Plant sterol accumulation` -> `Xanthomas`
- Hematologic manifestations are modeled as phenotypes, not downstream
  pathophysiology nodes, because the endpoint integration here is the plasma
  sterol pharmacodynamic readout.

## FDA Endpoint Mapping

- `FDA-SE-adult-noncancer-037` and `FDA-SE-pediatric-noncancer-026` both use
  `Plasma sitosterol and campesterol` in homozygous sitosterolemia.
- Disease YAML mapping:
  - `biochemical.name`: `Plasma sitosterol and campesterol`
  - readout target: `Plant sterol accumulation`
  - relationship: `PHARMACODYNAMIC_MARKER_OF`
  - direction: `POSITIVE`
  - endpoint context: `PHARMACODYNAMIC`

## Completeness Notes

- Covered: ABCG5/ABCG8 genetics, sterol transporter mechanism, sitosterol and
  campesterol accumulation, xanthomas, premature atherosclerosis,
  thrombocytopenia, hemolytic anemia, giant platelets, stomatocytic
  poikilocytosis, and ezetimibe pharmacodynamic response.
- Not split: ABCG5- versus ABCG8-related disease; current evidence and FDA rows
  support a unified sitosterolemia disease entry.
