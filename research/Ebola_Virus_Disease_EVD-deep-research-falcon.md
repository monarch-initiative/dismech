---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-15T09:13:04.463833'
end_time: '2025-12-15T09:20:22.100697'
duration_seconds: 437.64
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Ebola Virus Disease (EVD)
  mondo_id: ''
  category: ''
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 15
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Ebola Virus Disease (EVD)
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Ebola Virus Disease (EVD)**.
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
- **Disease Name:** Ebola Virus Disease (EVD)
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Ebola Virus Disease (EVD)**.
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


Plan
- Compile 2023–2025 primary literature and high-quality reviews on EVD mechanisms, entry factors, immune evasion, vascular injury, coagulopathy, tissue tropism, vaccines/therapeutics, and epidemiology. (Completed)
- Synthesize core pathophysiology with mechanistic attributions to specific viral proteins and host pathways. (Completed)
- Map key genes/proteins, processes (GO), cellular components, cell types (CL), anatomical sites (UBERON), and chemicals (ChEBI). (Completed)
- Integrate recent developments (2023–2024) in vaccines/therapeutics and outbreak statistics with URLs and dates. (Completed)
- Provide evidence items with direct citations and quotes where available. (Completed)

Disease Pathophysiology Research Report

Target Disease
- Disease Name: Ebola Virus Disease (EVD)
- MONDO ID: MONDO:0005737
- Category: Viral hemorrhagic fever (Filoviridae)

1. Core Pathophysiology
- Primary mechanisms: Ebola virus (EBOV) initiates infection by attachment and macropinocytic uptake into endosomes, proteolytic priming of GP by cathepsins, and obligatory engagement of the late endosomal/lysosomal cholesterol transporter Niemann–Pick C1 (NPC1) to trigger membrane fusion and cytosolic entry. Genetic screens newly identified SLC39A9 and PIK3C3 as host factors facilitating entry/internalization, complementing established roles for TIM‑1/HAVCR1 and C‑type lectins as attachment factors and macropinocytosis as the uptake route (PLOS Pathogens, Aug 22, 2024; https://doi.org/10.1371/journal.ppat.1012444). “Genetic depletion of SLC39A9 and PIK3C3 lead to reduction of EBOV entry… PIK3C3 kinase activity is indispensable for the internalization of EBOV virions” (excerpt) (gong2024genomewidecrisprcas9screen pages 25-26, gong2024genomewidecrisprcas9screen pages 29-30).
- Immune evasion and replication: VP35 binds dsRNA and functions as polymerase cofactor, antagonizing RIG‑I signaling; VP24 antagonizes IFN signaling via karyopherin‑α/STAT1 nuclear import and contributes to nucleocapsid assembly; GP mediates entry and its secreted isoform (sGP) modulates immunity and can act as an antibody decoy; VP40 and NP structure the virion and nucleocapsid (Egyptian Journal of Medical Human Genetics, Nov 2024; https://doi.org/10.1186/s43042-024-00600-8) (ndayambaje2024molecularcharacterizationof pages 1-2).
- Endothelial dysfunction/vascular leak: EBOV GP and shed/sG P are implicated in endothelial activation, barrier disruption, and vascular leak; reviews highlight GP-driven endothelial perturbations and sGP-mediated immune modulation; endothelial barrier failure integrates with inflammatory signaling to drive shock in VHFs (Signal Transduct Target Ther, Sep 2024; https://doi.org/10.1038/s41392-024-01917-x) (wang2024emergingandreemerging pages 53-53).
- Coagulopathy/DIC: Ebola belongs to VHFs characterized by thromboinflammation—cytokine-driven endothelial activation, tissue factor pathway triggering, platelet activation—culminating in consumptive coagulopathy and bleeding (overview) (Signal Transduct Target Ther, Sep 2024; https://doi.org/10.1038/s41392-024-01917-x) (wang2024emergingandreemerging pages 53-53).
- Disease course/epidemiology: Meta-analysis of EVD parameters (publications up to July 7, 2023) estimated pooled incubation period 8.5 days (95% CI 7.7–9.2), serial interval 15.4 days (95% CI 13.2–17.5), symptom onset-to-death 9.3 days (95% CI 8.5–10.1), onset-to-recovery 13.0 days (95% CI 10.4–15.7); CFR is high and heterogeneous across species and contexts (MedRxiv, Mar 21, 2024; https://doi.org/10.1101/2024.03.20.24304571) (nash2024ebolavirusdisease pages 25-27).

2. Key Molecular Players
- Genes/Proteins (HGNC):
  - NPC1 (HGNC:14930): endo/lysosomal receptor essential for EBOV fusion/entry (PLOS Pathogens, Mar 15, 2024; https://doi.org/10.1371/journal.ppat.1012038) (ayoubi2024recentadvancesin pages 6-8).
  - HAVCR1/TIM‑1 (HGNC:16064): phosphatidylserine receptor serving as EBOV attachment/cofactor (PLOS Pathogens, Aug 22, 2024; https://doi.org/10.1371/journal.ppat.1012444) (gong2024genomewidecrisprcas9screen pages 25-26).
  - SLC39A9 (HGNC:18018): zinc transporter impacting glycosylation; CRISPR hit promoting EBOV entry (PLOS Pathogens, Aug 22, 2024; https://doi.org/10.1371/journal.ppat.1012444) (gong2024genomewidecrisprcas9screen pages 25-26, gong2024genomewidecrisprcas9screen pages 29-30).
  - PIK3C3/VPS34 (HGNC:8975): class III PI3K; CRISPR hit; kinase activity required for virion internalization (PLOS Pathogens, Aug 22, 2024) (gong2024genomewidecrisprcas9screen pages 25-26, gong2024genomewidecrisprcas9screen pages 29-30).
  - Cathepsins (e.g., CTSB/CTSL): endosomal proteases priming GP (PLOS Pathogens, Aug 22, 2024) (gong2024genomewidecrisprcas9screen pages 25-26).
  - EBOV GP (glycoprotein; gene GP): mediates receptor binding/fusion; sGP immune decoy (Egyptian J Med Hum Genet, Nov 2024; PLOS Pathogens, Mar 15, 2024) (ndayambaje2024molecularcharacterizationof pages 1-2, ayoubi2024recentadvancesin pages 6-8).
  - VP35 (gene VP35): dsRNA-binding; polymerase cofactor; IFN antagonist (Egyptian J Med Hum Genet, Nov 2024) (ndayambaje2024molecularcharacterizationof pages 1-2).
  - VP24 (gene VP24): interferon antagonism via karyopherin‑α/STAT1 blockade; nucleocapsid assembly (Egyptian J Med Hum Genet, Nov 2024) (ndayambaje2024molecularcharacterizationof pages 1-2).
  - NP (nucleoprotein), L (RNA-dependent RNA polymerase), VP30, VP40: nucleocapsid and assembly (Egyptian J Med Hum Genet, Nov 2024) (ndayambaje2024molecularcharacterizationof pages 1-2).
- Chemical entities (ChEBI):
  - Small-molecule NPC1 inhibitors (e.g., MBX2254/MBX2270; diaryl sulfides SC198/SC073/SC816) targeting NPC1-GP interaction; clomiphene and other GP-directed entry inhibitors discussed (PLOS Pathogens, Mar 15, 2024) (ayoubi2024recentadvancesin pages 6-8).
- Cell Types (CL):
  - Monocytes/macrophages (CL:0000576/CL:0000235), dendritic cells (CL:0000451): early targets/immune dysregulation (Egyptian J Med Hum Genet, Nov 2024) (ndayambaje2024molecularcharacterizationof pages 1-2).
  - Endothelial cells (CL:0000115): barrier dysfunction/vascular leak (Signal Transduct Target Ther, Sep 2024) (wang2024emergingandreemerging pages 53-53).
- Anatomical Locations (UBERON):
  - Liver (UBERON:0002107), spleen (UBERON:0002106), vasculature/endothelium (UBERON:0001981): organ injury and vascular pathology in VHFs (Signal Transduct Target Ther, Sep 2024; Egyptian J Med Hum Genet, Nov 2024) (wang2024emergingandreemerging pages 53-53, ndayambaje2024molecularcharacterizationof pages 1-2).

3. Biological Processes (GO) disrupted
- Viral entry via endocytosis/macropinocytosis; endosomal proteolysis; membrane fusion (GO:0046718, GO:0006907, GO:0007010 proxy for macropinocytosis). Supported by CRISPR/host factor data (gong2024genomewidecrisprcas9screen pages 25-26, gong2024genomewidecrisprcas9screen pages 29-30).
- Negative regulation of type I interferon signaling (GO:0060338) by VP24/VP35 (ndayambaje2024molecularcharacterizationof pages 1-2).
- Innate immune response to dsRNA (GO:0039529) antagonized by VP35 (ndayambaje2024molecularcharacterizationof pages 1-2).
- Endothelial cell activation and increased permeability (GO:0001936, GO:0043114) in VHFs; sGP/GP-linked effects (wang2024emergingandreemerging pages 53-53).
- Blood coagulation and extrinsic pathway (GO:0007596; GO: extrinsic pathway of coagulation) leading to DIC in VHFs (wang2024emergingandreemerging pages 53-53).

4. Cellular Components
- Late endosome/lysosome membrane (GO:0031902/GO:0005765) where NPC1 mediates GP-dependent fusion (ayoubi2024recentadvancesin pages 6-8).
- Viral inclusion bodies and nucleocapsid (GO:0019013; viral nucleocapsid) for replication and immune evasion (ndayambaje2024molecularcharacterizationof pages 1-2).
- Endothelial adherens junctions/glycocalyx (GO:0005912; extracellular region) implicated in vascular permeability (wang2024emergingandreemerging pages 53-53).

5. Disease Progression (sequence of events)
- Exposure and incubation (median ~8–9 days) followed by abrupt febrile illness; early infection of monocytes/macrophages/DCs promotes high viremia and IFN antagonism (nash2024ebolavirusdisease pages 25-27, ndayambaje2024molecularcharacterizationof pages 1-2).
- Amplifying inflammation with endothelial activation, GP/sGP-mediated barrier dysfunction, and coagulopathy; clinical progression to hypovolemia, shock, and multiorgan failure (wang2024emergingandreemerging pages 53-53).
- Outcome trajectories: fatal cases with rapid onset-to-death (~9 days); survivors recover ~13 days from symptom onset (medians), reflecting heterogeneous host responses and care (nash2024ebolavirusdisease pages 25-27).

6. Phenotypic Manifestations (HP terms)
- Acute febrile illness (HP:0001945), hemorrhage/bleeding (HP:0001091), thrombocytopenia (HP:0001873), hypotension (HP:0002615), shock (HP:0001943), hepatic dysfunction (HP:0001410), diarrhea/vomiting (HP:0002014/HP:0002013), neurologic symptoms (HP:0001297), conjunctival injection/rash (HP:0000532/HP:0000988). Mechanistic linkage to vascular leak/coagulopathy and immune dysregulation (wang2024emergingandreemerging pages 53-53, ndayambaje2024molecularcharacterizationof pages 1-2, nash2024ebolavirusdisease pages 25-27).

7. Recent Developments and Implementations (2023–2024)
- Therapeutics: Two monoclonal antibody products—REGN‑EB3 (Inmazeb) and mAb114 (Ansuvimab/Ebanga)—are FDA‑approved and remain the only licensed EVD therapeutics; continued development targets broader neutralization across species and combination strategies; entry inhibitors (NPC1‑targeting small molecules) and host‑directed agents (AAK1 inhibitors) are under study; “Monoclonal antibodies remain the only FDA‑approved therapeutics…”; secreted GP can act as a decoy reducing mAb efficacy, motivating multi‑epitope cocktails (PLOS Pathogens, Mar 15, 2024; https://doi.org/10.1371/journal.ppat.1012038) (ayoubi2024recentadvancesin pages 6-8).
- Vaccines: rVSV‑ZEBOV (Ervebo) is FDA/WHO prequalified and used operationally (ring vaccination); heterologous Ad26.ZEBOV/MVA‑BN‑Filo regimen shows robust immunogenicity and age‑stratified responses; antibody kinetics differ by platform, with rVSV showing less‑rapid decline and children maintaining higher titers in modeling; “participants receiving a delayed dose 2 had a higher GMC… than standard 56‑day regimen” (example from implementation literature cited within) (PLOS Pathogens, Mar 15, 2024; MedRxiv meta‑analysis context) (ayoubi2024recentadvancesin pages 6-8, nash2024ebolavirusdisease pages 25-27).
- Occupational exposure guidance: Clinical guidance highlights availability of mAbs and ring vaccination approaches for post‑exposure risk contexts (summarized in 2024 overview) (PLOS Pathogens, Mar 15, 2024) (ayoubi2024recentadvancesin pages 6-8).

8. Epidemiology and Statistics (recent meta-analysis/outbreak reports)
- Incubation period: pooled 8.5 days (95% CI 7.7–9.2) (MedRxiv, Mar 21, 2024; https://doi.org/10.1101/2024.03.20.24304571) (nash2024ebolavirusdisease pages 25-27).
- Serial interval: pooled 15.4 days (95% CI 13.2–17.5) (nash2024ebolavirusdisease pages 25-27).
- Symptom onset-to-death: pooled 9.3 days (95% CI 8.5–10.1); onset-to-recovery 13.0 days (95% CI 10.4–15.7) (nash2024ebolavirusdisease pages 25-27).
- Case fatality ratio (CFR): ranges widely by species/outbreak (e.g., Zaire, Sudan, Bundibugyo), reflecting heterogeneity in strain, care, and demographics; meta‑analysis describes extensive variability (nash2024ebolavirusdisease pages 25-27). Example: Equateur Province 2020 outbreak CFR ~42% (The Lancet Microbe 2024, retrospective characterization; Feb 2024; https://doi.org/10.1016/S2666-5247(23)00259-8) (nash2024ebolavirusdisease pages 25-27).

Expert Commentary and Analysis
- Entry biology has matured from a single‑receptor (NPC1) paradigm to a multistep continuum: initial attachment via TIM‑1/lectins and PS‑mediated interactions, GP‑dependent macropinocytosis, cathepsin priming, and NPC1 engagement as the essential fusion checkpoint. The 2024 CRISPR study identifying SLC39A9 and PIK3C3 as crucial entry factors extends this model toward glycan regulation and PI3K‑dependent endocytic trafficking as druggable host nodes (gong2024genomewidecrisprcas9screen pages 25-26, gong2024genomewidecrisprcas9screen pages 29-30).
- Immune evasion hinges on multifunctional proteins: VP35 integrates polymerase cofactor function with dsRNA sequestration; VP24 concurrently shapes nucleocapsid assembly and disrupts STAT1 nuclear import, undermining IFN signaling; GP and sGP diversify immune modulation and may reduce therapeutic mAb effectiveness, supporting multi‑epitope antibody strategies and small‑molecule entry inhibitors (ndayambaje2024molecularcharacterizationof pages 1-2, ayoubi2024recentadvancesin pages 6-8).
- Vascular pathobiology remains central to fatal EVD. Cross‑VHF evidence supports a model of endothelial activation, glycocalyx disruption, and increased permeability, compounded by coagulopathy and hypovolemia; GP/sGP likely contribute to endothelial dysfunction, while thromboinflammation and tissue factor drive DIC phenotypes in severe disease (wang2024emergingandreemerging pages 53-53).
- Implementation: mAb therapeutics have improved survival yet leave residual mortality; ensuring timely access and integrating supportive care remain critical. Vaccine platforms provide complementary options: rVSV for rapid ring vaccination and Ad26/MVA for durable heterologous immunity; durability modeling and age‑dependent immunogenicity inform booster and deployment strategies (ayoubi2024recentadvancesin pages 6-8, nash2024ebolavirusdisease pages 25-27).

Direct evidence quotes
- “Genetic depletion of SLC39A9 and PIK3C3 lead to reduction of EBOV entry… PIK3C3 kinase activity is indispensable for the internalization of EBOV virions” (PLOS Pathogens, Aug 22, 2024; https://doi.org/10.1371/journal.ppat.1012444) (gong2024genomewidecrisprcas9screen pages 25-26, gong2024genomewidecrisprcas9screen pages 29-30).
- “Monoclonal antibodies remain the only FDA‑approved therapeutics… secreted GP may act as a decoy reducing mAb efficacy; escape variants motivate multi‑epitope antibody cocktails” (PLOS Pathogens, Mar 15, 2024; https://doi.org/10.1371/journal.ppat.1012038) (ayoubi2024recentadvancesin pages 6-8).

Ontology Annotations (selected; with supporting citations for mechanistic linkage)
- Genes/Proteins (HGNC): NPC1; HAVCR1; SLC39A9; PIK3C3; CTSB/CTSL; GP; VP24; VP35; NP; L; VP30; VP40 (gong2024genomewidecrisprcas9screen pages 25-26, ndayambaje2024molecularcharacterizationof pages 1-2, gong2024genomewidecrisprcas9screen pages 29-30, ayoubi2024recentadvancesin pages 6-8).
- Biological Process (GO): viral entry via endocytosis/macropinocytosis; endosomal proteolysis; membrane fusion; negative regulation of type I IFN signaling; endothelial cell permeability; blood coagulation (gong2024genomewidecrisprcas9screen pages 25-26, ndayambaje2024molecularcharacterizationof pages 1-2, wang2024emergingandreemerging pages 53-53, gong2024genomewidecrisprcas9screen pages 29-30).
- Cellular Component (GO): late endosome/lysosome membrane; viral nucleocapsid; endothelial cell-cell junction; endothelial glycocalyx/extracellular region (ayoubi2024recentadvancesin pages 6-8, ndayambaje2024molecularcharacterizationof pages 1-2, wang2024emergingandreemerging pages 53-53).
- Cell Types (CL): monocytes/macrophages; dendritic cells; endothelial cells (ndayambaje2024molecularcharacterizationof pages 1-2, wang2024emergingandreemerging pages 53-53).
- Anatomical Sites (UBERON): liver; spleen; vasculature/endothelium (wang2024emergingandreemerging pages 53-53, ndayambaje2024molecularcharacterizationof pages 1-2).
- Chemical Entities (ChEBI): NPC1-targeting small molecules; GP entry inhibitors (ayoubi2024recentadvancesin pages 6-8).
- Phenotypes (HP): hemorrhage, thrombocytopenia, shock, hepatic dysfunction, gastrointestinal symptoms (wang2024emergingandreemerging pages 53-53, nash2024ebolavirusdisease pages 25-27).

Current Applications and Real‑World Implementations (with URLs/dates)
- Therapeutic mAbs: Inmazeb (REGN‑EB3) and Ebanga (Ansuvimab/mAb114) in clinical use; continued work on pan‑ebolavirus mAbs and combinations (PLOS Pathogens, Mar 15, 2024; https://doi.org/10.1371/journal.ppat.1012038) (ayoubi2024recentadvancesin pages 6-8).
- Vaccination: rVSV‑ZEBOV ring vaccination in outbreak control; Ad26.ZEBOV/MVA‑BN‑Filo immunogenicity and durability modeling to inform booster policies (PLOS Pathogens, Mar 15, 2024; MedRxiv Mar 21, 2024) (ayoubi2024recentadvancesin pages 6-8, nash2024ebolavirusdisease pages 25-27).
- Host‑targeted entry inhibitors (NPC1, AAK1) and AI‑driven repurposing pipelines are under investigation to complement antibody therapy (PLOS Pathogens, Mar 15, 2024) (ayoubi2024recentadvancesin pages 6-8).

Evidence items (with PMIDs/DOIs/URLs)
- Ayoubi et al., Recent advances in the treatment of Ebola disease: A brief overview. PLOS Pathogens. Mar 15, 2024. DOI: 10.1371/journal.ppat.1012038. URL: https://doi.org/10.1371/journal.ppat.1012038 (mechanisms, therapeutics, vaccines, NPC1 targeting) (ayoubi2024recentadvancesin pages 6-8).
- Gong et al., Genome-wide CRISPR/Cas9 screen identifies SLC39A9 and PIK3C3 as crucial entry factors for Ebola virus infection. PLOS Pathogens. Aug 22, 2024. DOI: 10.1371/journal.ppat.1012444. URL: https://doi.org/10.1371/journal.ppat.1012444 (entry host factors, macropinocytosis/cathepsins/NPC1 pathway context) (gong2024genomewidecrisprcas9screen pages 25-26, gong2024genomewidecrisprcas9screen pages 29-30).
- Ndayambaje et al., Molecular characterization of Ebola virus, immune response, and therapeutic challenges. Egyptian Journal of Medical Human Genetics. Nov 2024. DOI: 10.1186/s43042-024-00600-8. URL: https://doi.org/10.1186/s43042-024-00600-8 (viral proteins and immune evasion overview; sGP) (ndayambaje2024molecularcharacterizationof pages 1-2).
- Wang et al., Emerging and reemerging infectious diseases: global trends and new strategies for their prevention and control. Signal Transduct Target Ther. Sep 2024. DOI: 10.1038/s41392-024-01917-x. URL: https://doi.org/10.1038/s41392-024-01917-x (vascular dysfunction/endothelial injury in VHFs; sGP and GP endothelial effects referenced) (wang2024emergingandreemerging pages 53-53).
- Nash et al., Ebola Virus Disease mathematical models and epidemiological parameters: a systematic review and meta-analysis. MedRxiv. Mar 21, 2024. DOI: 10.1101/2024.03.20.24304571. URL: https://doi.org/10.1101/2024.03.20.24304571 (incubation, serial interval, onset-to-death/recovery, CFR ranges; example DRC Equateur 2020 CFR) (nash2024ebolavirusdisease pages 25-27).

Limitations and open questions
- Direct, human in vivo mechanistic evidence for endothelial glycocalyx injury markers (e.g., syndecan‑1) specific to Ebola in 2023–2024 sources is less abundant in the retrieved set; however, cross‑VHF vascular leak paradigms and EBOV GP/sGP endothelial effects are supported in recent reviews (wang2024emergingandreemerging pages 53-53). Further targeted clinical studies in EVD cohorts would refine causal pathways.

Conclusion
EVD pathophysiology reflects a convergence of: (i) multistep entry culminating in NPC1‑dependent fusion and newly defined host entry nodes (SLC39A9, PIK3C3); (ii) potent viral antagonism of type I IFN and immune sensing by VP24/VP35; (iii) endothelial dysfunction with vascular leak and thromboinflammation leading to DIC; and (iv) rapid clinical trajectories with high CFR variability. Recent advances in therapeutics (licensed mAbs) and vaccines (rVSV‑ZEBOV; Ad26.ZEBOV/MVA‑BN‑Filo) have improved outcomes and outbreak control, while host‑directed entry inhibitors and broader mAb strategies aim to further reduce mortality and expand cross‑species protection (gong2024genomewidecrisprcas9screen pages 25-26, ndayambaje2024molecularcharacterizationof pages 1-2, wang2024emergingandreemerging pages 53-53, ayoubi2024recentadvancesin pages 6-8, nash2024ebolavirusdisease pages 25-27).

References

1. (gong2024genomewidecrisprcas9screen pages 25-26): Mingli Gong, Cheng Peng, Chen Yang, Zhenhua Wang, Hongwu Qian, Xue Hu, Peng Zhou, Chao Shan, and Qiang Ding. Genome-wide crispr/cas9 screen identifies slc39a9 and pik3c3 as crucial entry factors for ebola virus infection. PLOS Pathogens, 20:e1012444, Aug 2024. URL: https://doi.org/10.1371/journal.ppat.1012444, doi:10.1371/journal.ppat.1012444. This article has 7 citations and is from a highest quality peer-reviewed journal.

2. (gong2024genomewidecrisprcas9screen pages 29-30): Mingli Gong, Cheng Peng, Chen Yang, Zhenhua Wang, Hongwu Qian, Xue Hu, Peng Zhou, Chao Shan, and Qiang Ding. Genome-wide crispr/cas9 screen identifies slc39a9 and pik3c3 as crucial entry factors for ebola virus infection. PLOS Pathogens, 20:e1012444, Aug 2024. URL: https://doi.org/10.1371/journal.ppat.1012444, doi:10.1371/journal.ppat.1012444. This article has 7 citations and is from a highest quality peer-reviewed journal.

3. (ndayambaje2024molecularcharacterizationof pages 1-2): Martin Ndayambaje, Callixte Yadufashije, Thierry Habyarimana, Theogene Niyonsaba, Hicham Wahnou, Patrick Gad Iradukunda, Cedrick Izere, Olivier Uwishema, Pacifique Ndishimye, and Mounia Oudghiri. Molecular characterization of ebola virus, immune response, and therapeutic challenges: a narrative review. Egyptian Journal of Medical Human Genetics, Nov 2024. URL: https://doi.org/10.1186/s43042-024-00600-8, doi:10.1186/s43042-024-00600-8. This article has 4 citations and is from a peer-reviewed journal.

4. (wang2024emergingandreemerging pages 53-53): Shen Wang, Wujian Li, Zhenshan Wang, Wanying Yang, Entao Li, Xianzhu Xia, Feihu Yan, and Sandra Chiu. Emerging and reemerging infectious diseases: global trends and new strategies for their prevention and control. Signal Transduction and Targeted Therapy, Sep 2024. URL: https://doi.org/10.1038/s41392-024-01917-x, doi:10.1038/s41392-024-01917-x. This article has 62 citations and is from a peer-reviewed journal.

5. (nash2024ebolavirusdisease pages 25-27): Rebecca K. Nash, Sangeeta Bhatia, Christian Morgenstern, Patrick Doohan, David Jorgensen, Kelly McCain, Ruth McCabe, Dariya Nikitin, Alpha Forna, Gina Cuomo-Dannenburg, Joseph T. Hicks, Richard J. Sheppard, Tristan Naidoo, Sabine van Elsland, Cyril Geismar, Thomas Rawson, Sequoia Iris Leuba, Jack Wardle, Isobel Routledge, Keith Fraser, Natsuko Imai-Eaton, Anne Cori, and H. Juliette T. Unwin. Ebola virus disease mathematical models and epidemiological parameters: a systematic review and meta-analysis. MedRxiv, Mar 2024. URL: https://doi.org/10.1101/2024.03.20.24304571, doi:10.1101/2024.03.20.24304571. This article has 1 citations.

6. (ayoubi2024recentadvancesin pages 6-8): L’Emir Wassim El Ayoubi, Omar Mahmoud, Johnny Zakhour, and Souha S. Kanj. Recent advances in the treatment of ebola disease: a brief overview. PLOS Pathogens, 20:e1012038, Mar 2024. URL: https://doi.org/10.1371/journal.ppat.1012038, doi:10.1371/journal.ppat.1012038. This article has 30 citations and is from a highest quality peer-reviewed journal.