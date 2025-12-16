---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-15T09:13:12.517600'
end_time: '2025-12-15T09:20:40.346160'
duration_seconds: 447.83
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Familial Mediterranean Fever
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 26
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Familial Mediterranean Fever
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Familial Mediterranean Fever**.
Focus on the molecular and cellular mechanisms underlying disease progression.

### Required Information

#### 1. Core Pathophysiology
- What are the primary pathophysiological mechanisms?
- What molecular pathways are dysregulated?
- What cellular processes are affected?

#### 2. Key Molecular Players
- **Genes/Proteins**: Which genes are causally involved or implicated?
- **Chemical Entities**: What metabolites, drugs, or small molecules are relevant?
- **Cell Types**: Which cell types are primarily affected?
- **Anatomical Locations**: Which tissues/organs are involved?

#### 3. Biological Processes (for GO annotation)
- What biological processes (GO terms) are disrupted?
- Consider: signaling pathways, metabolic processes, cellular responses, transport, etc.

#### 4. Cellular Components
- Where in the cell do key processes occur?
- Consider: organelles, membrane compartments, extracellular space, etc.

#### 5. Disease Progression
- What is the sequence of events from initial trigger to clinical manifestation?
- Are there distinct stages or phases?

#### 6. Phenotypic Manifestations
- What are the key clinical phenotypes?
- How do they relate to the underlying mechanisms?

### Citation Requirements

- Cite primary literature (PMID preferred) for all mechanistic claims
- Prioritize recent reviews and landmark papers
- Include direct quotes where possible to support key statements

### Output Format

Structure your response as a narrative that could be used to populate a disease knowledge base entry with:
- Pathophysiology description
- Gene/protein annotations with ontology terms (HGNC, GO)
- Phenotype associations (HP terms)
- Cell type involvement (CL terms)
- Anatomical locations (UBERON terms)
- Chemical entities (CHEBI terms)
- Evidence items with PMIDs


## Output

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Familial Mediterranean Fever
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Familial Mediterranean Fever**.
Focus on the molecular and cellular mechanisms underlying disease progression.

### Required Information

#### 1. Core Pathophysiology
- What are the primary pathophysiological mechanisms?
- What molecular pathways are dysregulated?
- What cellular processes are affected?

#### 2. Key Molecular Players
- **Genes/Proteins**: Which genes are causally involved or implicated?
- **Chemical Entities**: What metabolites, drugs, or small molecules are relevant?
- **Cell Types**: Which cell types are primarily affected?
- **Anatomical Locations**: Which tissues/organs are involved?

#### 3. Biological Processes (for GO annotation)
- What biological processes (GO terms) are disrupted?
- Consider: signaling pathways, metabolic processes, cellular responses, transport, etc.

#### 4. Cellular Components
- Where in the cell do key processes occur?
- Consider: organelles, membrane compartments, extracellular space, etc.

#### 5. Disease Progression
- What is the sequence of events from initial trigger to clinical manifestation?
- Are there distinct stages or phases?

#### 6. Phenotypic Manifestations
- What are the key clinical phenotypes?
- How do they relate to the underlying mechanisms?

### Citation Requirements

- Cite primary literature (PMID preferred) for all mechanistic claims
- Prioritize recent reviews and landmark papers
- Include direct quotes where possible to support key statements

### Output Format

Structure your response as a narrative that could be used to populate a disease knowledge base entry with:
- Pathophysiology description
- Gene/protein annotations with ontology terms (HGNC, GO)
- Phenotype associations (HP terms)
- Cell type involvement (CL terms)
- Anatomical locations (UBERON terms)
- Chemical entities (CHEBI terms)
- Evidence items with PMIDs


# Disease Pathophysiology Research Report

## Target Disease
- Disease Name: Familial Mediterranean Fever (FMF)
- MONDO ID: [not specified]
- Category: Genetic (monogenic autoinflammatory disease)

## Pathophysiology overview
Familial Mediterranean fever is a prototypic inflammasomopathy caused by gain‑of‑function variants in MEFV encoding pyrin, a cytosolic inflammasome sensor in monocytes and neutrophils. Pathogenesis centers on dysregulated pyrin inflammasome assembly with downstream caspase‑1 activation, maturation and release of IL‑1β and IL‑18, gasdermin D–mediated pore formation and pyroptosis, and amplification by neutrophil/monocyte alarmins (S100 proteins). At baseline, pyrin is restrained by RhoA–PKN1/2–14‑3‑3 phosphorylation‑dependent autoinhibition; genetic variants and specific triggers lower the activation threshold and favor spontaneous or easily triggered inflammasome assembly (park2016pyrininflammasomeactivation pages 1-10, bella2024thepyrininflammasome pages 8-10, bella2024thepyrininflammasome pages 6-7, bella2024thepyrininflammasome pages 1-2).

Direct quote supporting the core mechanism: “RhoA activated the serine-threonine kinases PKN1 and PKN2 that bind and phosphorylate pyrin. Phosphorylated pyrin bound to 14-3-3 proteins… [and] blocked the pyrin inflammasome.” (Nature Immunology, 2016; URL: https://doi.org/10.1038/ni.3457; published Jun 2016) (park2016pyrininflammasomeactivation pages 1-10).

Recent reviews and experimental work in 2023–2024 refine these mechanisms by implicating PP2A activity in positively regulating pyrin via dephosphorylation, highlighting cytoskeletal control and gasdermin D as essential executioners, and identifying endogenous steroid catabolites and alarmins (S100A8/A9/A12) as important amplifiers and biomarkers in pyrin‑mediated inflammation (Frontiers in Immunology 2024, https://doi.org/10.3389/fimmu.2023.1341680; mBio 2023, https://doi.org/10.1128/mbio.02066-23; Frontiers in Pediatrics 2024, https://doi.org/10.3389/fped.2024.1421353) (bella2024thepyrininflammasome pages 8-10, bella2024thepyrininflammasome pages 6-7, bella2024thepyrininflammasome pages 5-6, chaaban2024anarrativereview pages 19-20, bella2024thepyrininflammasome pages 1-2).

| Entity | Type / Ontology | Identifier | Role in FMF pathophysiology (one sentence) | Evidence (year & DOI URL) (context ID) | Notes |
|---|---|---|---|---|---|
| MEFV / pyrin | Gene / inflammasome sensor (HGNC:MEFV) | HGNC:MEFV | Cytosolic inflammasome sensor whose gain-of-function variants lower activation threshold and drive caspase-1–dependent IL-1β/IL-18 release. | 2016 10.1038/ni.3457; 2024 10.3389/fimmu.2023.1341680 (park2016pyrininflammasomeactivation pages 1-10, bella2024thepyrininflammasome pages 5-6) | Central causal gene in FMF; exon 10 (B30.2) variants frequent. |
| PKN1 | Ser/Thr kinase (GO:protein kinase activity) | PKN1 | Phosphorylates pyrin (S208/S242) downstream of RhoA to enforce pyrin autoinhibition. | 2016 10.1038/ni.3457 (park2016pyrininflammasomeactivation pages 1-10) | Works with PKN2 to enable 14-3-3 binding. |
| PKN2 | Ser/Thr kinase (GO:protein kinase activity) | PKN2 | Partner kinase to PKN1 that phosphorylates pyrin and maintains 14-3-3–mediated inhibition. | 2016 10.1038/ni.3457 (park2016pyrininflammasomeactivation pages 1-10) | Reductions in PKN2 binding seen with pathogenic MEFV variants. |
| 14-3-3 (YWHA family) | Chaperone family (YWHA genes) | YWHA* | Binds phosphorylated pyrin to prevent inflammasome assembly. | 2016 10.1038/ni.3457 (park2016pyrininflammasomeactivation pages 1-10) | Loss of 14-3-3 binding occurs with reduced pyrin phosphorylation. |
| PP2A (PPP2CA/PPP2CB) | Ser/Thr phosphatase (PPP family) | PPP2CA / PPP2CB | Phosphatase activity implicated in dephosphorylating pyrin to permit inflammasome activation. | 2023 10.1128/mbio.02066-23; 2024 10.3389/fimmu.2023.1341680 (bella2024thepyrininflammasome pages 8-10, bella2024thepyrininflammasome pages 5-6) | PP2A involvement described as counterbalancing PKN-mediated phosphorylation. |
| RhoA | Small GTPase (HGNC:RHOA) | RHOA | Upstream GTPase whose inactivation (by toxins or prenylation defects) reduces PKN activity and relieves pyrin inhibition. | 2016 10.1038/ni.3457; 2024 10.3389/fimmu.2023.1341680 (park2016pyrininflammasomeactivation pages 1-10, bella2024thepyrininflammasome pages 5-6) | Targets of bacterial effectors converge here. |
| ASC (PYCARD) | Inflammasome adaptor (HGNC:PYCARD) | PYCARD | Adaptor recruited by pyrin PYD to assemble ASC specks and recruit pro–caspase-1. | 2024 10.3389/fimmu.2023.1341680 (bella2024thepyrininflammasome pages 5-6) | Required for caspase-1 activation and downstream signaling. |
| CASP1 (caspase-1) | Effector protease (CASP family) | CASP1 | Cleaves pro–IL-1β and pro–IL-18 to active forms and cleaves GSDMD to trigger pyroptosis. | 2016 10.1038/ni.3457; 2024 10.3389/fimmu.2023.1341680 (park2016pyrininflammasomeactivation pages 1-10, bella2024thepyrininflammasome pages 5-6) | Central executor of canonical inflammasome responses. |
| GSDMD (gasdermin D) | Pore-forming effector (GSDM family) | GSDMD | N-terminal fragment forms membrane pores enabling cytokine release and pyroptotic cell death. | 2024 10.3389/fimmu.2023.1341680; 2024 10.3389/fped.2024.1421353 (bella2024thepyrininflammasome pages 8-10, chaaban2024anarrativereview pages 19-20) | GSDMD pores also permit release of alarmins (S100 proteins). |
| IL1B (IL‑1β) | Proinflammatory cytokine (HGNC:IL1B) | IL1B | Principal downstream cytokine driving fever, serositis and systemic inflammation in FMF. | 2016 10.1038/ni.3457; 2024 10.3389/fped.2024.1421353 (park2016pyrininflammasomeactivation pages 1-10, chaaban2024anarrativereview pages 19-20) | Target of effective biologic therapies in colchicine-resistant disease. |
| IL18 | Proinflammatory cytokine (HGNC:IL18) | IL18 | Co-released with IL-1β from pyrin inflammasome activation and contributes to inflammation. | 2016 10.1038/ni.3457; 2024 10.3389/fped.2024.1421353 (park2016pyrininflammasomeactivation pages 1-10, chaaban2024anarrativereview pages 19-20) | Elevated in FMF flares and some steady‑state measurements. |
| S100A8/A9/A12 (alarmins) | Damage-associated proteins (CHEBI/S100 family) | S100A8 / S100A9 / S100A12 | Neutrophil/monocyte alarmins released during pyroptosis that amplify inflammation and serve as biomarkers. | 2024 10.3389/fimmu.2023.1341680; 2024 10.3389/fped.2024.1421353 (bella2024thepyrininflammasome pages 8-10, chaaban2024anarrativereview pages 19-20) | S100A levels correlate with disease activity and may be GSDMD-dependent. |
| PSTPIP1 (CD2BP1) | Cytoskeletal adaptor (HGNC:PSTPIP1) | PSTPIP1 | Interacts with pyrin to modulate oligomerization and inflammasome assembly; variants linked to hyperinflammation. | 2024 10.3389/fimmu.2023.1341680 (bella2024thepyrininflammasome pages 5-6) | Mutations can produce overlapping autoinflammatory phenotypes. |
| Colchicine | Drug / microtubule inhibitor (CHEBI) | CHEBI:Colchicine | First‑line therapy that disrupts microtubules and reduces pyrin inflammasome activation and attacks. | 2024 10.15167/bustaffa-marta_phd2024-05-28; 2024 10.3389/fimmu.2023.1341680 (bustaffa2024theeurofeverfmf pages 76-79, bella2024thepyrininflammasome pages 5-6) | Effective for attack prevention and amyloidosis prophylaxis; some genotypes show reduced response. |
| Anakinra | IL‑1 receptor antagonist (drug) | ANAKINRA | Blocks IL‑1 signaling to rapidly control pyrin-mediated systemic inflammation in colchicine‑resistant cases. | 2024 10.3389/fped.2024.1421353; 2024 10.15167/bustaffa-marta_phd2024-05-28 (chaaban2024anarrativereview pages 19-20, bustaffa2024theeurofeverfmf pages 76-79) | Used off‑label/approved in refractory FMF; rapid onset. |
| Canakinumab | Anti–IL‑1β monoclonal antibody (drug) | CANAKINUMAB | Neutralizes IL‑1β to reduce flares in patients unresponsive or intolerant to colchicine. | 2024 10.3389/fped.2024.1421353; 2024 10.15167/bustaffa-marta_phd2024-05-28 (chaaban2024anarrativereview pages 19-20, bustaffa2024theeurofeverfmf pages 76-79) | Long‑acting IL‑1β blockade option. |
| Rilonacept | IL‑1 trap (biologic) | RILONACEPT | Binds IL‑1α/β preventing receptor engagement and decreasing FMF inflammation in resistant cases. | 2024 10.3389/fped.2024.1421353 (chaaban2024anarrativereview pages 19-20) | Alternative IL‑1–directed therapy. |
| GGPP (geranylgeranyl pyrophosphate) | Metabolite (CHEBI) | GGPP | Prenylation substrate whose deficiency (e.g., in HIDS) leads to RhoA inactivation and pyrin activation; exogenous GGPP can suppress response. | 2016 10.1038/ni.3457 (park2016pyrininflammasomeactivation pages 1-10) | Links metabolic/prenylation defects to pyrin activation. |
| Pregnanolone & etiocholanolone | Steroid catabolites (CHEBI) | Pregnanolone / Etiocholanolone | Endogenous catabolites that can directly activate pyrin (B30.2-dependent) independent of RhoA. | 2024 10.3389/fimmu.2023.1341680 (bella2024thepyrininflammasome pages 6-7) | May explain non‑infectious triggers of flares. |
| Yersinia effectors (YopE/YopT/YopM) | Bacterial virulence proteins | YopE / YopT / YopM | Pathogen effectors that inactivate RhoA (YopE/T) or modulate PKN/14‑3‑3 (YopM) to trigger or evade pyrin responses. | 2016 10.1038/ni.3457; 2020 10.1038/s41590-020-0705-6 (park2016pyrininflammasomeactivation pages 1-10) | Historical selection of MEFV variants linked to resistance to Y. pestis (see Park et al.). |
| C. difficile TcdB | Bacterial toxin | TcdB | Toxin that inactivates Rho GTPases and can trigger pyrin inflammasome activation. | 2024 10.3389/fimmu.2023.1341680 (bella2024thepyrininflammasome pages 6-7) | Example of non‑Yersinia effector causing RhoA perturbation. |
| Neutrophils | Immune cell (CL:0000775) | CL:0000775 | Major effector cells in FMF attacks that release IL‑1, S100 alarmins, form NETs and undergo pyroptosis contributing to tissue inflammation. | 2024 10.3389/fimmu.2023.1341680; 2024 10.3389/fped.2024.1421353 (bella2024thepyrininflammasome pages 8-10, chaaban2024anarrativereview pages 19-20) | Abundant in serosal and synovial inflammatory infiltrates during attacks. |
| Monocytes / macrophages | Immune cell (CL:0000235) | CL:0000235 | Primary cells where pyrin inflammasome assembles, producing IL‑1β/IL‑18 and driving systemic symptoms. | 2016 10.1038/ni.3457; 2024 10.3389/fimmu.2023.1341680 (park2016pyrininflammasomeactivation pages 1-10, bella2024thepyrininflammasome pages 5-6) | Source of circulating IL‑1 and priming signals. |
| Peritoneum | Tissue (UBERON) | UBERON:0002106 | Frequent anatomical site of FMF serositis causing abdominal pain during attacks. | 2024 10.15167/bustaffa-marta_phd2024-05-28 (bustaffa2024theeurofeverfmf pages 76-79) | Clinically implicated in peritonitis episodes. |
| Pleura | Tissue (UBERON) | UBERON:0001004 | Site of pleuritic pain/serositis in FMF attacks. | 2024 10.15167/bustaffa-marta_phd2024-05-28 (bustaffa2024theeurofeverfmf pages 76-79) | Pleuritis is a common attack manifestation. |
| Synovium | Tissue (UBERON) | UBERON:0002381 | Joint tissue involved in FMF arthritis during inflammatory episodes. | 2024 10.15167/bustaffa-marta_phd2024-05-28 (bustaffa2024theeurofeverfmf pages 76-79) | Acute mono/oligoarthritis is typical. |
| Kidney (AA amyloidosis) | Organ / pathology (UBERON / HP) | UBERON:0002113 / HP:0001973 | Major long-term complication from chronic IL‑1–driven inflammation leading to AA amyloid deposition and renal impairment. | 2024 10.15167/bustaffa-marta_phd2024-05-28; 2024 10.3389/fimmu.2023.1341680 (bustaffa2024theeurofeverfmf pages 76-79, bella2024thepyrininflammasome pages 5-6) | Risk reduced by effective colchicine and IL‑1 suppression. |


*Table: Compact ontology‑grounded table summarizing key genes, proteins, cells, tissues, triggers and therapies in FMF with evidence links to the gathered literature (pqac context IDs and DOIs).*

## 1. Core pathophysiology
- Primary mechanisms:
  - Pyrin inflammasome hyperactivation due to MEFV gain‑of‑function variants, especially in the B30.2/SPRY domain (exon 10), reduces dependence on cytoskeletal cues and lowers the threshold for assembly with ASC and pro‑caspase‑1 (Frontiers in Immunology 2024, https://doi.org/10.3389/fimmu.2023.1341680) (bella2024thepyrininflammasome pages 8-10, bella2024thepyrininflammasome pages 6-7, bella2024thepyrininflammasome pages 5-6).
  - RhoA–PKN1/2–14‑3‑3 axis: In healthy cells, active RhoA stimulates PKN1/2 to phosphorylate pyrin at Ser208/Ser242, enabling 14‑3‑3 binding and autoinhibition. Inactivation of RhoA (by bacterial toxins or prenylation defects) or MEFV variants diminishes phosphorylation and 14‑3‑3 binding, permitting inflammasome assembly (Nature Immunology 2016, https://doi.org/10.1038/ni.3457) (park2016pyrininflammasomeactivation pages 1-10).
  - Positive regulation by phosphatase: PP2A catalytic subunits (PPP2CA/PPP2CB) are implicated in dephosphorylating pyrin and promoting inflammasome assembly when the RhoA–PKN brake is released (mBio 2023, https://doi.org/10.1128/mbio.02066-23) (bella2024thepyrininflammasome pages 8-10).
  - Triggers: RhoA‑inactivating bacterial effectors (Yersinia YopE/YopT; C. difficile TcdB) trigger pyrin; YopM can recruit PKN1/2 to oppose pyrin, but disease‑associated pyrin may resist this inhibition. Endogenous steroid catabolites (pregnanolone, etiocholanolone) can directly engage B30.2 and activate pyrin independent of RhoA (Frontiers in Immunology 2024, https://doi.org/10.3389/fimmu.2023.1341680; Nature Immunology 2016, https://doi.org/10.1038/ni.3457) (park2016pyrininflammasomeactivation pages 1-10, bella2024thepyrininflammasome pages 6-7).
  - Downstream execution: Caspase‑1 cleaves pro‑IL‑1β and pro‑IL‑18, and gasdermin D (GSDMD) to form pores causing cytokine release and pyroptosis; GSDMD pores facilitate release of S100A8/A9 alarmins that amplify inflammation (Frontiers in Immunology 2024, https://doi.org/10.3389/fimmu.2023.1341680; Frontiers in Pediatrics 2024, https://doi.org/10.3389/fped.2024.1421353) (bella2024thepyrininflammasome pages 8-10, chaaban2024anarrativereview pages 19-20, bella2024thepyrininflammasome pages 1-2).

- Dysregulated molecular pathways:
  - Inflammasome signaling (pyrin–ASC–caspase‑1) with heightened IL‑1/IL‑18 axis activity (park2016pyrininflammasomeactivation pages 1-10, chaaban2024anarrativereview pages 3-4).
  - Rho GTPase signaling and cytoskeletal regulation (actin/microtubules) governing pyrin activation (park2016pyrininflammasomeactivation pages 1-10, bella2024thepyrininflammasome pages 6-7, bella2024thepyrininflammasome pages 5-6).
  - Phosphorylation/dephosphorylation balance (PKN1/2 vs. PP2A) as a rheostat of pyrin activity (park2016pyrininflammasomeactivation pages 1-10, bella2024thepyrininflammasome pages 8-10).

- Affected cellular processes:
  - Priming (NF‑κB–dependent) and activation steps for inflammasome assembly; caspase‑1 activation; pyroptotic cell death; alarmin release; and neutrophil‑driven serosal inflammation (bella2024thepyrininflammasome pages 8-10, chaaban2024anarrativereview pages 19-20, bella2024thepyrininflammasome pages 1-2).

## 2. Key molecular players
- Genes/Proteins (HGNC): MEFV/pyrin; RHOA; PKN1, PKN2; 14‑3‑3 (YWHA family); PYCARD (ASC); CASP1; GSDMD; IL1B; IL18; S100A8/S100A9/S100A12; PSTPIP1 (park2016pyrininflammasomeactivation pages 1-10, bella2024thepyrininflammasome pages 8-10, bella2024thepyrininflammasome pages 6-7, bella2024thepyrininflammasome pages 5-6, chaaban2024anarrativereview pages 19-20).
- Chemical entities (CHEBI): colchicine; geranylgeranyl pyrophosphate (GGPP); pregnanolone; etiocholanolone (park2016pyrininflammasomeactivation pages 1-10, bella2024thepyrininflammasome pages 6-7, bustaffa2024theeurofeverfmf pages 76-79).
- Cell types (CL): monocytes/macrophages (pyrin expression/assembly); neutrophils (effector cells, alarmin release, pyroptosis) (bella2024thepyrininflammasome pages 8-10, bella2024thepyrininflammasome pages 5-6, chaaban2024anarrativereview pages 19-20).
- Anatomical locations (UBERON): peritoneum; pleura; synovium; kidney (AA amyloidosis) (bustaffa2024theeurofeverfmf pages 76-79, bella2024thepyrininflammasome pages 8-10).

## 3. Biological processes (GO) disrupted
- Inflammasome complex assembly (GO:0140775) and ASC speck formation (GO:0140694) (bella2024thepyrininflammasome pages 5-6).
- Positive regulation of interleukin‑1 beta production (GO:0032731) and interleukin‑18 production (GO:0032655) (park2016pyrininflammasomeactivation pages 1-10, chaaban2024anarrativereview pages 3-4).
- Rho protein signal transduction (GO:0007266) and actin cytoskeleton organization (GO:0030036) (park2016pyrininflammasomeactivation pages 1-10, bella2024thepyrininflammasome pages 6-7).
- Protein phosphorylation (GO:0006468) by PKN1/2 and protein dephosphorylation (GO:0006470) by PP2A regulating pyrin (park2016pyrininflammasomeactivation pages 1-10, bella2024thepyrininflammasome pages 8-10).
- Pyroptosis (GO:0070269) and gasdermin‑mediated pore formation (GO:0140718) (bella2024thepyrininflammasome pages 8-10, chaaban2024anarrativereview pages 19-20).

## 4. Cellular components (GO)
- Cytosol (GO:0005829) and inflammasome complex (GO:0061702) where pyrin–ASC–caspase‑1 assemble (bella2024thepyrininflammasome pages 5-6).
- ASC speck (GO:0140694) as the oligomeric adaptor platform (bella2024thepyrininflammasome pages 5-6).
- Plasma membrane (GO:0005886) for GSDMD pore formation and cytokine/alarmin release (bella2024thepyrininflammasome pages 8-10, chaaban2024anarrativereview pages 19-20).

## 5. Disease progression: triggers to manifestations
- Initiation: Triggering insults lower RhoA activity (bacterial toxins/effectors such as YopE/YopT; metabolic deficits in prenylation; or endogenous steroid catabolites engaging B30.2) or MEFV variants intrinsically reduce the phosphorylation/14‑3‑3 brake (Nature Immunology 2016, https://doi.org/10.1038/ni.3457; Frontiers in Immunology 2024, https://doi.org/10.3389/fimmu.2023.1341680) (park2016pyrininflammasomeactivation pages 1-10, bella2024thepyrininflammasome pages 6-7).
- Activation: PP2A dephosphorylation and loss of 14‑3‑3 binding permit pyrin to recruit ASC and pro‑caspase‑1, forming the inflammasome (mBio 2023, https://doi.org/10.1128/mbio.02066-23) (bella2024thepyrininflammasome pages 8-10).
- Effector phase: Caspase‑1 cleaves IL‑1β/IL‑18 and GSDMD, inducing pyroptosis; S100A8/A9/A12 alarmins are released and amplify inflammation (Frontiers in Immunology 2024, https://doi.org/10.3389/fimmu.2023.1341680; Frontiers in Pediatrics 2024, https://doi.org/10.3389/fped.2024.1421353) (bella2024thepyrininflammasome pages 8-10, chaaban2024anarrativereview pages 19-20).
- Tissue response: Neutrophil‑predominant serosal and synovial inflammation yields fever, peritonitis, pleuritis, and arthritis; repeated IL‑1–driven inflammation predisposes to AA amyloidosis, especially in uncontrolled disease (Eurofever update 2024, https://doi.org/10.15167/bustaffa-marta_phd2024-05-28) (bustaffa2024theeurofeverfmf pages 76-79, bella2024thepyrininflammasome pages 8-10).

Evolutionary context: MEFV variants show signals of positive selection in Mediterranean populations, with functional data linking mutant pyrin to resistance against Yersinia pestis via preserved IL‑1β responses despite YopM-mediated suppression (Nature Immunology 2020, https://doi.org/10.1038/s41590-020-0705-6; published Jun 2020) (park2016pyrininflammasomeactivation pages 1-10).

## 6. Phenotypic manifestations and mechanisms (HP terms)
- Recurrent fever (HP:0001945) and serositis: peritonitis (HP:0002587), pleuritis (HP:0002106), pericarditis (HP:0001693); acute arthritis/arthralgia (HP:0002829) (bustaffa2024theeurofeverfmf pages 76-79).
- Elevated acute‑phase reactants (e.g., CRP, SAA) and risk for AA amyloidosis with renal involvement (HP:0001919; HP:0000093) in chronic or uncontrolled inflammation (bustaffa2024theeurofeverfmf pages 76-79, bella2024thepyrininflammasome pages 8-10).
- Cytokine signature: increased IL‑1β/IL‑18 with broader proinflammatory milieu (IL‑6, TNF‑α) during attacks and sometimes intercritically, aligning with pyrin‑caspase‑1 hyperactivity (Frontiers in Pediatrics 2024, https://doi.org/10.3389/fped.2024.1421353) (chaaban2024anarrativereview pages 3-4).

## 7. Recent developments (2023–2024), applications, expert opinions
- PP2A implication: 2023 mechanistic evidence shows PP2A catalytic subunits dephosphorylate pyrin to drive activation when the RhoA–PKN brake is removed, identifying a potential druggable node in pyrin regulation (mBio 2023, https://doi.org/10.1128/mbio.02066-23) (bella2024thepyrininflammasome pages 8-10).
- GSDMD and alarmin axis: 2024 reviews integrate data that GSDMD pores not only mediate pyroptosis but also facilitate S100A8/A9 release, linking inflammasome execution to biomarker/effector alarmins (Frontiers in Immunology 2024, https://doi.org/10.3389/fimmu.2023.1341680; Frontiers in Pediatrics 2024, https://doi.org/10.3389/fped.2024.1421353) (bella2024thepyrininflammasome pages 8-10, chaaban2024anarrativereview pages 19-20).
- Endogenous activators: Steroid catabolites (pregnanolone, etiocholanolone) can activate pyrin via B30.2 independent of RhoA, expanding noninfectious triggers of flares (Frontiers in Immunology 2024, https://doi.org/10.3389/fimmu.2023.1341680) (bella2024thepyrininflammasome pages 6-7).
- Clinical implementations: Colchicine remains first‑line; in colchicine‑resistant or ‑intolerant FMF, IL‑1–targeted biologics (anakinra, canakinumab, rilonacept) are widely used and recommended in practice; Eurofever longitudinal efforts in 2024 summarize real‑world treatment patterns and genotype–phenotype correlations (Eurofever update 2024, https://doi.org/10.15167/bustaffa-marta_phd2024-05-28; Frontiers in Pediatrics 2024, https://doi.org/10.3389/fped.2024.1421353) (bustaffa2024theeurofeverfmf pages 76-79, chaaban2024anarrativereview pages 19-20).

Expert synthesis from a 2024 pediatric rheumatology perspective: pyrin inflammasome activation is “strictly dependent on homeostasis‑altering molecular processes,” with RhoA–PKN–14‑3‑3 regulation, cytoskeletal cues, GSDMD pores, and S100 alarmins forming an integrated axis of dysregulated innate immunity in FMF (Frontiers in Immunology 2024, published Jan 2024; URL: https://doi.org/10.3389/fimmu.2023.1341680) (bella2024thepyrininflammasome pages 1-2).

## 8. Gene/protein annotations with ontology and processes
- MEFV (HGNC:MEFV): pyrin; processes: inflammasome assembly (GO:0140775), negative regulation by phosphorylation (PKN1/2) and 14‑3‑3 binding; cellular component: cytosol/inflammasome complex (park2016pyrininflammasomeactivation pages 1-10, bella2024thepyrininflammasome pages 5-6).
- RHOA (HGNC:RHOA): upstream small GTPase; process: Rho protein signal transduction (GO:0007266) regulating PKN1/2 and actin dynamics (park2016pyrininflammasomeactivation pages 1-10, bella2024thepyrininflammasome pages 6-7).
- PKN1/PKN2: kinases mediating pyrin Ser208/Ser242 phosphorylation; process: protein phosphorylation (GO:0006468) (park2016pyrininflammasomeactivation pages 1-10).
- PP2A (PPP2CA/PPP2CB): phosphatase dephosphorylating pyrin; process: protein dephosphorylation (GO:0006470) (bella2024thepyrininflammasome pages 8-10).
- PYCARD/ASC: adaptor for speck formation; cellular component: ASC speck (GO:0140694) (bella2024thepyrininflammasome pages 5-6).
- CASP1: executioner protease; processes: interleukin‑1 beta production (GO:0032611), pyroptosis (GO:0070269) (park2016pyrininflammasomeactivation pages 1-10, bella2024thepyrininflammasome pages 8-10).
- GSDMD: pore‑forming effector; process: gasdermin‑mediated pore formation (GO:0140718) (bella2024thepyrininflammasome pages 8-10, chaaban2024anarrativereview pages 19-20).
- S100A8/A9/A12: alarmins; processes: positive regulation of inflammatory response (GO:0050729) (bella2024thepyrininflammasome pages 8-10, chaaban2024anarrativereview pages 19-20).

## 9. Phenotype associations (HP), cells (CL), anatomy (UBERON), chemicals (CHEBI)
- HP: Recurrent fever (HP:0001945), peritonitis (HP:0002587), pleuritis (HP:0002106), arthritis (HP:0001369/HP:0002829), AA amyloidosis (HP:0001973), renal insufficiency (HP:0000083) (bustaffa2024theeurofeverfmf pages 76-79, bella2024thepyrininflammasome pages 8-10).
- CL: Monocytes/macrophages (CL:0000235), neutrophils (CL:0000775) (bella2024thepyrininflammasome pages 8-10, bella2024thepyrininflammasome pages 5-6, chaaban2024anarrativereview pages 19-20).
- UBERON: Peritoneum (UBERON:0002106), pleura (UBERON:0001004), synovium (UBERON:0002381), kidney (UBERON:0002113) (bustaffa2024theeurofeverfmf pages 76-79).
- CHEBI: Colchicine; geranylgeranyl pyrophosphate (GGPP); pregnanolone; etiocholanolone (park2016pyrininflammasomeactivation pages 1-10, bella2024thepyrininflammasome pages 6-7, bustaffa2024theeurofeverfmf pages 76-79).

## 10. Current applications and real-world implementations
- Colchicine: microtubule inhibitor that diminishes pyrin‑dependent activation and prevents amyloidosis; some genotypes (e.g., M694V homozygotes) may show reduced responsiveness, necessitating biologics (Eurofever 2024, https://doi.org/10.15167/bustaffa-marta_phd2024-05-28; Frontiers in Immunology 2024, https://doi.org/10.3389/fimmu.2023.1341680) (bustaffa2024theeurofeverfmf pages 76-79, bella2024thepyrininflammasome pages 5-6).
- IL‑1 blockade: anakinra (IL‑1 receptor antagonist), canakinumab (anti–IL‑1β), and rilonacept (IL‑1 trap) provide rapid control of attacks and are recommended in colchicine‑resistant or ‑intolerant FMF (Frontiers in Pediatrics 2024, https://doi.org/10.3389/fped.2024.1421353; Eurofever 2024, https://doi.org/10.15167/bustaffa-marta_phd2024-05-28) (chaaban2024anarrativereview pages 19-20, bustaffa2024theeurofeverfmf pages 76-79).

## 11. Relevant statistics and data
- Real‑world cohort synthesis (Eurofever FMF longitudinal update, 2024) underscores widespread colchicine use as first‑line with escalation to IL‑1 inhibitors in nonresponders and confirms serosal/arthritis predominance; genotype–phenotype observations include higher risk of severe disease (e.g., amyloidosis) in certain MEFV genotypes (URL: https://doi.org/10.15167/bustaffa-marta_phd2024-05-28; May 2024). Specific numerical rates were not extractable from the gathered excerpt, but the report documents these patterns across multinational centers (bustaffa2024theeurofeverfmf pages 76-79).
- Cytokine profiling in clinical and ex vivo studies demonstrates elevated IL‑1β and IL‑18 during flares with broader proinflammatory cytokines (IL‑6, TNF‑α), consistent with pyrin‑caspase‑1 activation (Frontiers in Pediatrics 2024, https://doi.org/10.3389/fped.2024.1421353; Jul 2024) (chaaban2024anarrativereview pages 3-4).

## 12. Evidence items (with URLs and dates)
- Park YH et al. Pyrin inflammasome activation and RhoA signaling in FMF and HIDS. Nature Immunology. Jun 2016. URL: https://doi.org/10.1038/ni.3457 (park2016pyrininflammasomeactivation pages 1-10).
- La Bella S et al. The pyrin inflammasome, a leading actor in pediatric autoinflammatory diseases. Frontiers in Immunology. Jan 2024. URL: https://doi.org/10.3389/fimmu.2023.1341680 (bella2024thepyrininflammasome pages 8-10, bella2024thepyrininflammasome pages 6-7, bella2024thepyrininflammasome pages 5-6, bella2024thepyrininflammasome pages 1-2).
- Malik HS et al. Phosphoprotein phosphatase activity positively regulates oligomeric pyrin to trigger inflammasome assembly. mBio. Oct 2023. URL: https://doi.org/10.1128/mbio.02066-23 (bella2024thepyrininflammasome pages 8-10).
- Chaaban A et al. Cytokines in the pathogenesis and treatment of FMF. Frontiers in Pediatrics. Jul 2024. URL: https://doi.org/10.3389/fped.2024.1421353 (chaaban2024anarrativereview pages 19-20, chaaban2024anarrativereview pages 3-4).
- Bustaffa M. The Eurofever FMF longitudinal cohort: first update. May 2024. URL: https://doi.org/10.15167/bustaffa-marta_phd2024-05-28 (bustaffa2024theeurofeverfmf pages 76-79).
- Park YH et al. Ancient FMF mutations in human pyrin and resistance to Yersinia pestis. Nature Immunology. Jun 2020. URL: https://doi.org/10.1038/s41590-020-0705-6 (park2016pyrininflammasomeactivation pages 1-10).

## Conclusion
FMF pathophysiology is driven by a failure of the RhoA–PKN1/2–14‑3‑3 checkpoint that restrains pyrin, with MEFV variants and specific triggers enabling PP2A‑assisted dephosphorylation and assembly of the pyrin inflammasome. Caspase‑1–dependent IL‑1β/IL‑18 release and GSDMD‑mediated pyroptosis, together with S100 alarmin amplification, explain the febrile serositis, arthritis, and risk of AA amyloidosis. 2023–2024 work highlights PP2A as a positive regulator and integrates cytoskeletal control, endogenous steroid catabolites, and alarmin biology into an updated model. Clinically, colchicine remains foundational, while IL‑1–targeted biologics are effective for colchicine‑resistant disease (park2016pyrininflammasomeactivation pages 1-10, bella2024thepyrininflammasome pages 8-10, bella2024thepyrininflammasome pages 6-7, bella2024thepyrininflammasome pages 5-6, chaaban2024anarrativereview pages 19-20, chaaban2024anarrativereview pages 3-4, bustaffa2024theeurofeverfmf pages 76-79, bella2024thepyrininflammasome pages 1-2).

References

1. (park2016pyrininflammasomeactivation pages 1-10): Yong Hwan Park, Geryl Wood, Daniel L Kastner, and Jae Jin Chae. Pyrin inflammasome activation and rhoa signaling in the autoinflammatory diseases fmf and hids. Nature Immunology, 17:914-921, Jun 2016. URL: https://doi.org/10.1038/ni.3457, doi:10.1038/ni.3457. This article has 646 citations and is from a highest quality peer-reviewed journal.

2. (bella2024thepyrininflammasome pages 8-10): Saverio La Bella, Armando Di Ludovico, Giulia Di Donato, Ozge Basaran, Seza Ozen, Marco Gattorno, Francesco Chiarelli, and Luciana Breda. The pyrin inflammasome, a leading actor in pediatric autoinflammatory diseases. Frontiers in Immunology, Jan 2024. URL: https://doi.org/10.3389/fimmu.2023.1341680, doi:10.3389/fimmu.2023.1341680. This article has 23 citations and is from a peer-reviewed journal.

3. (bella2024thepyrininflammasome pages 6-7): Saverio La Bella, Armando Di Ludovico, Giulia Di Donato, Ozge Basaran, Seza Ozen, Marco Gattorno, Francesco Chiarelli, and Luciana Breda. The pyrin inflammasome, a leading actor in pediatric autoinflammatory diseases. Frontiers in Immunology, Jan 2024. URL: https://doi.org/10.3389/fimmu.2023.1341680, doi:10.3389/fimmu.2023.1341680. This article has 23 citations and is from a peer-reviewed journal.

4. (bella2024thepyrininflammasome pages 1-2): Saverio La Bella, Armando Di Ludovico, Giulia Di Donato, Ozge Basaran, Seza Ozen, Marco Gattorno, Francesco Chiarelli, and Luciana Breda. The pyrin inflammasome, a leading actor in pediatric autoinflammatory diseases. Frontiers in Immunology, Jan 2024. URL: https://doi.org/10.3389/fimmu.2023.1341680, doi:10.3389/fimmu.2023.1341680. This article has 23 citations and is from a peer-reviewed journal.

5. (bella2024thepyrininflammasome pages 5-6): Saverio La Bella, Armando Di Ludovico, Giulia Di Donato, Ozge Basaran, Seza Ozen, Marco Gattorno, Francesco Chiarelli, and Luciana Breda. The pyrin inflammasome, a leading actor in pediatric autoinflammatory diseases. Frontiers in Immunology, Jan 2024. URL: https://doi.org/10.3389/fimmu.2023.1341680, doi:10.3389/fimmu.2023.1341680. This article has 23 citations and is from a peer-reviewed journal.

6. (chaaban2024anarrativereview pages 19-20): Ahlam Chaaban, Hasan Yassine, Razane Hammoud, Ruba Kanaan, Louna Karam, and José-Noel Ibrahim. A narrative review on the role of cytokines in the pathogenesis and treatment of familial mediterranean fever: an emphasis on pediatric cases. Frontiers in Pediatrics, Jul 2024. URL: https://doi.org/10.3389/fped.2024.1421353, doi:10.3389/fped.2024.1421353. This article has 10 citations and is from a poor quality or predatory journal.

7. (bustaffa2024theeurofeverfmf pages 76-79): MARTA BUSTAFFA. The eurofever fmf longitudinal cohort: first update on the longitudinal data. Other, May 2024. URL: https://doi.org/10.15167/bustaffa-marta\_phd2024-05-28, doi:10.15167/bustaffa-marta\_phd2024-05-28. This article has 0 citations.

8. (chaaban2024anarrativereview pages 3-4): Ahlam Chaaban, Hasan Yassine, Razane Hammoud, Ruba Kanaan, Louna Karam, and José-Noel Ibrahim. A narrative review on the role of cytokines in the pathogenesis and treatment of familial mediterranean fever: an emphasis on pediatric cases. Frontiers in Pediatrics, Jul 2024. URL: https://doi.org/10.3389/fped.2024.1421353, doi:10.3389/fped.2024.1421353. This article has 10 citations and is from a poor quality or predatory journal.