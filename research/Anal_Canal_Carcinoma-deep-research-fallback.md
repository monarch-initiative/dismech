# Anal Canal Carcinoma Deep Research Fallback

## Provider Attempts

- 2026-05-13T00:00Z: `just research-disorder asta Anal_Canal_Carcinoma`
  failed: `agentapi not found in PATH` and no provider API keys configured
  (OPENAI_API_KEY, EDISON_API_KEY, ASTA_API_KEY, PERPLEXITY_API_KEY all unset
  in this environment).
- 2026-05-13T00:00Z: `just research-disorder openai Anal_Canal_Carcinoma`
  failed for the same reason.
- 2026-05-13T00:00Z: `just research-disorder perplexity Anal_Canal_Carcinoma`
  failed for the same reason.
- 2026-05-13T00:00Z: `just research-disorder falcon Anal_Canal_Carcinoma`
  failed for the same reason.

No provider-generated research artifact was available to integrate. Curation
therefore proceeded from previously fetched PubMed abstracts in
`references_cache/`, without hand-editing any cache files.

## Literature Synthesis

The following PMIDs were used to anchor the curated `kb/disorders/Anal_Canal_Carcinoma.yaml`
entry. Each citation below corresponds to the cached abstract in
`references_cache/PMID_<id>.md` and is attributed to the role it plays in the
pathophysiology/clinical model.

### HPV etiology and viral mechanism

- **PMID:42101137** (J Med Virol 2026) — "Causative Human Papillomavirus (HPV)
  Genotypes of Anal Cancers in Australian Cisgender Women." Laser-capture
  microdissection of anal SCC lesions attributed HPV-16 as the causal genotype
  in the great majority of cases (93.3% HPV16). Anchors the HPV-16-dominant
  etiology, the `infectious_agent` and `environmental` entries for HPV, the
  HPV vaccination prevention rationale, and the higher risk of anal cancer in
  MSM living with HIV.
- **PMID:2175676** (Cell 1990) — "The E6 oncoprotein encoded by human
  papillomavirus types 16 and 18 promotes the degradation of p53." Classic
  biochemical study showing that the E6 proteins of oncogenic HPV types
  stimulate ATP- and ubiquitin-proteasome-dependent degradation of p53.
  Anchors the **E6 Oncoprotein-Mediated p53 Degradation** pathophysiology
  node and the upstream half of the HPV → p53 loss → genomic instability
  axis.
- **PMID:2537532** (Science 1989) — "The human papilloma virus-16 E7
  oncoprotein is able to bind to the retinoblastoma gene product." Founding
  biochemical evidence that HPV-16 E7 binds and inactivates pRB. Anchors the
  **E7 Oncoprotein-Mediated pRB Inactivation** pathophysiology node and the
  upstream half of the E7 → pRB inactivation → uncontrolled S-phase entry
  axis.

### Risk factors and natural history

- **PMID:15241823** (Cancer 2004) — "Human papillomavirus, smoking, and sexual
  practices in the etiology of anal cancer." Population-based case-control
  study identifying current cigarette smoking as an independent risk factor
  for anal cancer in both men and women, independent of HPV-related sexual
  exposures. Anchors the tobacco-smoking entry under `environmental`.
- **PMID:40019005** (J Low Genit Tract Dis 2025) — "Recent Guidelines on Anal
  Cancer Screening: A Systematic Review." Systematic review of society
  screening guidelines describing the AIN-to-invasive-SCC progression
  pathway, the role of high-resolution anoscopy in high-risk groups, and the
  benefit of treating precancerous anal lesions. Anchors the **Anal
  Intraepithelial Neoplasia Progression** pathophysiology node and the
  high-resolution anoscopy diagnostic entry.

### Molecular and immune profiling

- **PMID:34790403** (J Gastrointest Oncol 2021) — "Molecular characterization
  of squamous cell carcinoma of the anal canal." Multiplatform molecular
  profiling of 311 anal SCC specimens reporting recurrent somatic mutations
  in PIK3CA (28.1%), KMT2D (19.5%), FBXW7 (12%), TP53 (12%), and PTEN
  (10.8%), as well as PD-L1 expression in 40.5% of tumors and PD-1
  expression on infiltrating cells in 68.8%. Anchors the **Genomic
  Instability** and **Adaptive Immune Resistance** pathophysiology nodes,
  the TP53 and PIK3CA `genetic` entries, the histopathology entry for anal
  SCC, and the rationale for PD-1 checkpoint blockade.

### Clinical presentation and regional spread

- **PMID:33085290** ("Rectal Bleeding.") — Reference clinical definition of
  hematochezia as the passage of frank blood per rectum. Anchors the
  **Rectal Bleeding (Hematochezia)** phenotype entry as the most common
  presenting symptom of anal canal cancer.
- **PMID:37731305** (Ann Palliat Med 2023) — "Palliative care in colorectal
  and anal malignancies from diagnosis to death." Palliative care review of
  colorectal and anal malignancies documenting pain among the multiple
  symptoms commonly experienced by patients with these cancers. Anchors the
  **Anal Pain** phenotype entry; the description was deliberately scoped
  to the palliative-care evidence base (see Round-2 review fix).
- **PMID:39882228** (J Anus Rectum Colon 2025) — "Metastatic Status and
  Dissection Effect of Regional/Extraregional Lymph Nodes in Japanese
  Patients with Squamous Cell Carcinoma of the Anal Canal." Multicenter
  retrospective cohort of 435 anal canal SCC patients documenting that
  primary tumor progression is associated with inguinal lymph node
  metastasis and recurrence. Anchors the **Inguinal Lymphadenopathy**
  phenotype entry and the lymphatic drainage pattern of the anal canal
  below the dentate line.

### Epidemiology, histology, and treatment

- **PMID:41452529** (Int J Clin Oncol 2026) — "Cancer epidemiology in rare
  and hereditary colorectal diseases 2) anal canal cancer (cancer
  statistics)." Japanese and Western registry data documenting that anal
  canal cancer histology varies by population (Japan: 66.8–75.5%
  adenocarcinoma, 16.2–24.4% SCC; Western: 70–85% SCC), that HPV-16 is the
  most prevalent genotype in HPV-positive SCC (85% HPV-positive), and that
  adoption of chemoradiotherapy rose from 14% in the 1990s to >80% after
  2010. Anchors the SCC and adenocarcinoma subtype/histopathology entries,
  the HPV infection pathophysiology node, the histopathology diagnostic
  entry, and the Nigro-regimen chemoradiation treatment entry.
- **PMID:15571466** (Expert Opin Pharmacother 2004) — "Chemotherapeutic
  options in the management of anal cancer." Review establishing that, since
  Nigro's original 1974 contribution, the chemotherapy backbone for anal
  cancer has remained 5-fluorouracil plus mitomycin C, given concurrently
  with radiation. Anchors the **Chemoradiation (Nigro regimen)** treatment
  entry and the use of 5-FU and mitomycin C as `therapeutic_agent` values.
- **PMID:37210274** (Eur J Surg Oncol 2023) — "Survival outcomes following
  salvage abdominoperineal resection for recurrent and persistent anal
  squamous cell carcinoma." Multicenter retrospective cohort establishing
  salvage abdominoperineal resection as the primary treatment for
  locoregional failure after chemoradiation for anal SCC. Anchors the
  **Salvage Abdominoperineal Resection** treatment entry.
- **PMID:35114169** (Lancet Gastroenterol Hepatol 2022) — "Pembrolizumab for
  previously treated advanced anal squamous cell carcinoma: results from the
  non-randomised, multicohort, multicentre, phase 2 KEYNOTE-158 study."
  Phase 2 KEYNOTE-158 anal SCC cohort supporting pembrolizumab as an active
  second-line treatment for advanced anal SCC. Anchors the **Immune
  Checkpoint Inhibitor Therapy** treatment entry and the `target_mechanisms`
  link from PD-1 blockade to the **Adaptive Immune Resistance**
  pathophysiology node (immune_checkpoint_blockade module conformance).

## Curation Conclusions

The accepted disease model for HPV-associated anal canal carcinoma is a
multi-step transformation in which:

1. Persistent infection of basal stratified squamous epithelial cells of the
   anal canal (predominantly at the transformation zone) with high-risk HPV
   (most commonly HPV-16) establishes sustained expression of the viral
   oncoproteins E6 and E7.
2. E6 targets p53 for ubiquitin-proteasome-dependent degradation (PMID:2175676),
   abolishing DNA damage checkpoints and apoptotic responses.
3. E7 binds and inactivates pRB (PMID:2537532), releasing E2F transcription
   factors and driving uncontrolled G1/S transition and proliferation.
4. Combined p53 and pRB inactivation, together with HPV-associated chromosomal
   aberrations, produces genomic instability and accumulation of driver
   mutations (PIK3CA, KMT2D, FBXW7, TP53, PTEN; PMID:34790403).
5. HPV-driven dysplasia of the anal squamous epithelium progresses through
   AIN1 → AIN2 → AIN3/HSIL → invasive squamous cell carcinoma (PMID:40019005).
6. Invasive anal SCC frequently upregulates PD-L1 and engages adaptive immune
   resistance (PMID:34790403), providing the therapeutic rationale for PD-1
   blockade (PMID:35114169).

Clinically, anal canal carcinoma presents most commonly with hematochezia
(PMID:33085290), anal pain (PMID:37731305), and inguinal lymphadenopathy in
regional spread (PMID:39882228). HIV infection (especially in MSM) and
tobacco smoking are major risk modifiers (PMID:42101137, PMID:15241823).
Standard curative treatment for localized disease is the Nigro regimen of
concurrent 5-FU/mitomycin-C chemoradiation (PMID:15571466, PMID:41452529),
with salvage abdominoperineal resection reserved for locoregional failure
(PMID:37210274), and PD-1 inhibitors (pembrolizumab, nivolumab) for
recurrent or metastatic disease (PMID:35114169).

## Subtypes

Curated subtypes in the YAML:

- Anal Canal Squamous Cell Carcinoma (NCIT:C7469) — dominant histology in
  Western series, strongly HPV-16-driven (PMID:42101137).
- Anal Canal Adenocarcinoma (NCIT:C7471) — rare in Western series, but more
  common than SCC in Japanese registries (PMID:41452529); not HPV-associated;
  treated more like rectal adenocarcinoma.

## Items Intentionally Skipped

- KMT2D, FBXW7, and PTEN are cited in the **Genomic Instability**
  pathophysiology node via PMID:34790403 but are not yet broken out as
  individual `genetic` entries. A follow-up curation pass can split these
  into per-gene entries (with the same snippet as the parent entry) if
  schema-level gene-level granularity is desired.
- The Nigro regimen `treatment_term` currently uses `MAXO:0000014`
  (radiation therapy) with 5-FU and mitomycin C as `therapeutic_agent`
  values. `NCIT:C94626` (Chemoradiotherapy) would better represent the
  combined-modality nature of the regimen; this is a follow-up refinement
  flagged in Round-3 review.
