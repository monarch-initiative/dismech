---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-02-19T22:13:52.131352'
end_time: '2026-02-19T22:25:10.749297'
duration_seconds: 678.62
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Malaria
  mondo_id: ''
  category: Infectious
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 31
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Malaria
- **MONDO ID:**  (if available)
- **Category:** Infectious

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Malaria**.
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
- **Disease Name:** Malaria
- **MONDO ID:**  (if available)
- **Category:** Infectious

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Malaria**.
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


Title: Molecular and Cellular Pathophysiology of Malaria (Plasmodium falciparum and Plasmodium vivax) — 2024 Update

Disease: Malaria (infectious disease; apicomplexan protozoa of genus Plasmodium).
MONDO ID: Not established from the retrieved sources in this run.

1. Key concepts and definitions (current understanding)

1.1 Core life-cycle stages relevant to pathophysiology
Malaria pathophysiology is stage-specific: (i) liver-stage infection establishes infection after sporozoite inoculation, with clinically silent development in hepatocytes; (ii) blood-stage asexual replication drives nearly all acute clinical disease; and (iii) in P. vivax (and P. ovale) a dormant liver-stage “hypnozoite” reservoir can reactivate and drive relapses, shaping chronic/recurrent disease and transmission dynamics. The importance of hypnozoite-driven relapse is quantified in recent clinical synthesis: an estimated 66–95% of P. vivax cases are relapses originating from liver hypnozoites. (commons2024effectofprimaquine pages 1-2)

1.2 Sequestration/cytoadherence and microvascular dysfunction (hallmark of severe P. falciparum)
A defining mechanistic concept in severe falciparum malaria is cytoadherence and sequestration of Plasmodium falciparum-infected erythrocytes (iRBCs) in post-capillary venules and microvessels. This process (a) allows iRBCs to evade splenic clearance and (b) produces tissue hypoperfusion, endothelial activation, barrier dysfunction (e.g., blood–brain barrier disruption), and inflammatory/coagulopathic cascades. PfEMP1 (Plasmodium falciparum erythrocyte membrane protein 1) is a major parasite adhesin mediating this binding to host endothelial receptors including ICAM1 and EPCR. (blankson2024understandingthepathogenesis pages 80-83, blankson2024understandingthepathogenesisa pages 80-83, gopinadhan2024ahumanpluripotent pages 8-10)

1.3 Antigenic variation
PfEMP1 is encoded by a ~60-member var gene family, enabling antigenic variation and receptor-binding diversity, which contributes to immune evasion and tissue-specific sequestration phenotypes. (blankson2024understandingthepathogenesis pages 80-83, blankson2024understandingthepathogenesisa pages 80-83)

1.4 Hemolysis, anemia, and malaria toxins
Blood-stage infection causes destruction of parasitized and non-parasitized erythrocytes, impaired erythropoiesis (“dyserythropoiesis”), hypersplenism, and inflammatory iron restriction, driving malarial anemia. A key parasite-derived bioactive “toxin-like” product is hemozoin (Hz; malaria pigment), formed during hemoglobin digestion, which accumulates in organs and modulates innate immune signaling and oxidative pathways. (blankson2024understandingthepathogenesisa pages 80-83, blankson2024understandingthepathogenesis pages 78-80)

2. Core pathophysiology (molecular/cellular mechanisms)

2.1 Sequestration/cytoadherence → endothelial activation → barrier failure

Parasite and host ligands/receptors
• Parasite: PfEMP1/var gene products displayed on iRBC surfaces mediate adhesion to endothelial receptors including ICAM1 and EPCR. (blankson2024understandingthepathogenesis pages 80-83, blankson2024understandingthepathogenesisa pages 80-83)
• Host endothelium: ICAM-1 (HGNC:5344; gene ICAM1) and VCAM-1 (HGNC:12663; gene VCAM1) are endothelial adhesion molecules upregulated during inflammatory activation and are measurably increased in in vitro BBB models after exposure to Pf-iRBCs. (gopinadhan2024ahumanpluripotent pages 8-10)

EPCR pathway perturbation
EPCR (endothelial protein C receptor; gene PROCR) is implicated in severe malaria; PfEMP1 binding to EPCR is described as disrupting EPCR’s anti-inflammatory/cytoprotective functions, providing a mechanistic link to endothelial injury in cerebral malaria. (blankson2024understandingthepathogenesis pages 80-83, blankson2024understandingthepathogenesisa pages 80-83, wassmer2024unravellingmysteriesat pages 12-14)

BBB disruption (cellular process and quantitative evidence)
A 2024 in vitro BBB model using hiPSC-derived brain microvascular endothelial cells demonstrated functional barrier breakdown after co-culture with Pf-iRBCs (HB3var03 strain). Key quantitative findings included: baseline barrier tightness (TEER ~1200 Ω·cm2 in hiPSC-BMECs vs ~100 Ω·cm2 in immortalized cells), and after 6 hours of Pf-iRBC exposure, reduced TEER and increased sodium fluorescein permeability (paracellular leak), accompanied by increased ICAM-1 and VCAM-1 expression. (gopinadhan2024ahumanpluripotent pages 8-10, gopinadhan2024ahumanpluripotent media b2e9c3aa)

2.2 Inflammation, cytokines, innate sensing, and immunopathology

Cytokine dysregulation
Severe malaria is associated with dysregulated pro-inflammatory cytokines and stress pathways including TNF-α, IFNγ, IL-1, IL-6, MIF, and HIF-1; imbalance of regulatory cytokines (e.g., low IL-10/IL-12 in severe malarial anemia) is also described. (blankson2024understandingthepathogenesis pages 80-83, blankson2024understandingthepathogenesisa pages 80-83)

Hemozoin-triggered innate activation and metalloprotease involvement
Hemozoin accumulates in organs (liver, spleen, lungs, brain) and, when phagocytosed by monocytes, can induce TNFα and IL-1β and increase MMP-9 activity; MMP-9 is described as capable of degrading basement membranes and disrupting endothelial tight junctions, consistent with a BBB injury mechanism. (blankson2024understandingthepathogenesis pages 78-80)

DNA/Hz sensing and inflammasome activation
In a placental malaria model summary, hemozoin complexed with DNA is described as activating NLRP3 and TLR9, inducing IL-1β and type I interferon signaling, linking parasite products to innate inflammatory programs and (context-dependent) immune suppression with chronic elevation. (ekregbesi2024developingaphysiologic pages 13-16)

Neutrophils and NETs
Neutrophil extracellular trap (NET) formation in response to infected erythrocytes is described as requiring CXCR4 and MIF, linking chemokine receptor signaling and inflammatory mediators to microvascular immunopathology. (blankson2024understandingthepathogenesis pages 220-224, blankson2024understandingthepathogenesisa pages 220-224)

2.3 Hemolysis, oxidative stress, and anemia mechanisms

Erythropoiesis inhibition by circulating hemozoin
A 2024 severe malaria review summarizes that circulating hemozoin at ~1–10 µg/mL can directly inhibit erythropoiesis, and can induce lipid oxidation products (15-HETE, 4HNE) that stiffen RBCs and shorten RBC lifespan, consistent with combined production-loss anemia. (blankson2024understandingthepathogenesis pages 80-83, blankson2024understandingthepathogenesisa pages 80-83)

Splenic clearance/hypersplenism
Hypersplenism and enhanced splenic clearance/removal of RBCs is described as contributing to anemia and can persist for weeks. (blankson2024understandingthepathogenesisa pages 80-83)

Metabolic derangements (hypoglycemia/lactate)
A placental malaria model summary links ROS-driven mitochondrial dysfunction and increased glycolysis to hyperlactatemia, hypoglycemia, and tissue hypoxia/necrosis, providing a mechanistic bridge between inflammatory/oxidative programs and systemic metabolic complications. (ekregbesi2024developingaphysiologic pages 13-16)

3. Key molecular players and entities (knowledge-base oriented)

3.1 Parasite genes/proteins (Plasmodium)
• PfEMP1 (variant surface antigen family): mediates cytoadherence to ICAM1/EPCR; encoded by ~60 var genes; antigenic variation and receptor-binding diversity. (blankson2024understandingthepathogenesis pages 80-83, blankson2024understandingthepathogenesisa pages 80-83)
• var gene family: encodes PfEMP1; central to immune evasion and tissue-specific pathology via differential receptor binding. (blankson2024understandingthepathogenesis pages 80-83, blankson2024understandingthepathogenesisa pages 80-83)

3.2 Host genes/proteins (HGNC) implicated in mechanisms
• ICAM1 (HGNC:5344): endothelial receptor and marker of endothelial activation; upregulated in BBB model after Pf-iRBC exposure. (gopinadhan2024ahumanpluripotent pages 8-10)
• VCAM1 (HGNC:12663): endothelial activation marker; increased in BBB model after Pf-iRBC exposure. (gopinadhan2024ahumanpluripotent pages 8-10)
• PROCR / EPCR: receptor for protein C with cytoprotective roles; implicated in severity and PfEMP1 binding-mediated dysfunction. (blankson2024understandingthepathogenesis pages 80-83, blankson2024understandingthepathogenesisa pages 80-83, wassmer2024unravellingmysteriesat pages 12-14)
• CXCR4 (HGNC:2561): required for NET formation in response to infected erythrocytes (mechanistic role in inflammatory pathology). (blankson2024understandingthepathogenesis pages 220-224)
• MIF (HGNC:7097): elevated inflammatory mediator linked to NET formation and severe malaria immunopathology. (blankson2024understandingthepathogenesis pages 220-224, blankson2024understandingthepathogenesisa pages 220-224)
• MMP9 (HGNC:7176): induced/activated in hemozoin-exposed monocytes; mechanistically linked to basement membrane/tight junction disruption. (blankson2024understandingthepathogenesis pages 78-80)
• TLR9 (HGNC:15633) and NLRP3 (HGNC:16400): described as sensing pathways engaged by hemozoin+DNA, driving IL-1β/type I IFN programs. (ekregbesi2024developingaphysiologic pages 13-16)
• TNF (HGNC:11892), IFNG (HGNC:5438), IL1B (HGNC:5992), IL6 (HGNC:6018): cytokines highlighted in severe malaria inflammatory dysregulation. (blankson2024understandingthepathogenesis pages 80-83, blankson2024understandingthepathogenesisa pages 80-83, blankson2024understandingthepathogenesis pages 78-80)

Disease–target associations (Open Targets, supportive/triage evidence)
Open Targets lists malaria associations for TLR9, TLR7, ABO, and several MMPs (e.g., MMP8), with example literature PMIDs for ABO-malaria associations including 37708213 (PMC10522014) among others. (gopinadhan2024ahumanpluripotent media b2e9c3aa)

3.3 Cell types (CL) primarily involved (mechanistically)
• Brain microvascular endothelial cell (BBB endothelium): barrier integrity loss and adhesion molecule upregulation in response to Pf-iRBC exposure. (gopinadhan2024ahumanpluripotent pages 8-10)
• Monocyte/macrophage (phagocytes): hemozoin uptake drives cytokine release and MMP activity. (blankson2024understandingthepathogenesis pages 78-80)
• Neutrophil: NET formation implicated in severe malaria inflammation. (blankson2024understandingthepathogenesis pages 220-224)
• Erythrocyte: infected and uninfected RBC destruction, altered deformability (oxidative lipid products), and sequestration. (blankson2024understandingthepathogenesisa pages 80-83)

3.4 Anatomical locations (UBERON) involved
• Liver: hypnozoite reservoir (vivax/ovale) and hemozoin accumulation. (commons2024effectofprimaquine pages 1-2, blankson2024understandingthepathogenesis pages 78-80)
• Spleen: clearance/hypersplenism and hemozoin accumulation. (blankson2024understandingthepathogenesisa pages 80-83, blankson2024understandingthepathogenesis pages 78-80)
• Brain microvasculature/BBB: cerebral malaria sequestration and barrier dysfunction. (wassmer2024unravellingmysteriesat pages 12-14, gopinadhan2024ahumanpluripotent pages 8-10)
• Placenta: sequestration-driven pathology in pregnancy-associated malaria models. (ekregbesi2024developingaphysiologic pages 13-16)

3.5 Chemical entities (CHEBI-relevant)
• Hemozoin (malaria pigment): inhibits erythropoiesis; immunomodulatory; organ deposition. (blankson2024understandingthepathogenesis pages 80-83, blankson2024understandingthepathogenesis pages 78-80)
• Sodium fluorescein: permeability tracer used to quantify BBB leak in vitro. (gopinadhan2024ahumanpluripotent pages 8-10, gopinadhan2024ahumanpluripotent media b2e9c3aa)
• 15-HETE and 4HNE (lipid oxidation products): associated with RBC stiffening/shortened RBC lifespan in severe malarial anemia context. (blankson2024understandingthepathogenesis pages 80-83, blankson2024understandingthepathogenesisa pages 80-83)

4. Biological processes disrupted (GO-oriented)
Representative disrupted biological processes supported by the retrieved evidence include:
• Cell adhesion / cytoadherence (iRBC–endothelium binding): PfEMP1–ICAM1/EPCR mediated adhesion and sequestration. (blankson2024understandingthepathogenesis pages 80-83, gopinadhan2024ahumanpluripotent pages 8-10)
• Endothelial cell activation and inflammatory signaling (e.g., TNF/IFNγ-driven programs; adhesion molecule upregulation): increased ICAM1/VCAM1, cytokine dysregulation. (blankson2024understandingthepathogenesis pages 80-83, gopinadhan2024ahumanpluripotent pages 8-10)
• Regulation of vascular permeability / barrier function: reduced TEER and increased paracellular permeability in BBB model. (gopinadhan2024ahumanpluripotent pages 8-10, gopinadhan2024ahumanpluripotent media b2e9c3aa)
• Innate immune response and inflammasome activation (TLR9/NLRP3; IL-1β; type I IFN): hemozoin+DNA sensing. (ekregbesi2024developingaphysiologic pages 13-16)
• Matrix remodeling / basement membrane organization (MMP-9 activity): hemozoin-associated MMP-9 induction and barrier disruption mechanism. (blankson2024understandingthepathogenesis pages 78-80)
• Erythrocyte homeostasis / erythropoiesis: hemozoin inhibition of erythropoiesis and anemia pathogenesis. (blankson2024understandingthepathogenesis pages 80-83)
• Neutrophil extracellular trap formation: CXCR4/MIF-dependent NET release to infected erythrocytes. (blankson2024understandingthepathogenesis pages 220-224)

5. Cellular components (where processes occur; GO-CC oriented)
• Plasma membrane / cell surface (iRBC surface PfEMP1; endothelial ICAM1/EPCR/VCAM1). (blankson2024understandingthepathogenesis pages 80-83, gopinadhan2024ahumanpluripotent pages 8-10)
• Microvascular lumen and endothelium interface (sequestration site). (wassmer2024unravellingmysteriesat pages 12-14, gopinadhan2024ahumanpluripotent pages 8-10)
• Tight junction-associated structures of endothelial cells (occludin/ZO-1/claudin-5 localization disruption reported in BBB model). (gopinadhan2024ahumanpluripotent pages 8-10)
• Extracellular space / circulating plasma (soluble receptor forms; extracellular vesicles; microparticles; cytokines). (blankson2024understandingthepathogenesis pages 80-83, blankson2024understandingthepathogenesis pages 220-224)
• Phagolysosomal compartments (hemozoin phagocytosis by monocytes/macrophages). (blankson2024understandingthepathogenesis pages 78-80)

6. Disease progression (sequence of events)

6.1 P. falciparum (typical progression to severe disease)
1) Blood-stage infection expands; iRBCs display variant surface antigens (PfEMP1). (blankson2024understandingthepathogenesis pages 80-83)
2) iRBC cytoadherence to endothelial receptors (ICAM1/EPCR) → sequestration → reduced microvascular flow and hypoperfusion. (blankson2024understandingthepathogenesis pages 80-83, gopinadhan2024ahumanpluripotent pages 8-10)
3) Endothelial activation and barrier dysfunction: adhesion molecules upregulated; BBB tight junction localization disrupted; permeability increases. (gopinadhan2024ahumanpluripotent pages 8-10, gopinadhan2024ahumanpluripotent media b2e9c3aa)
4) Hemolysis and hemozoin release/uptake → cytokine amplification (TNFα/IL-1β), MMP activity (MMP-9), and oxidative injury pathways. (blankson2024understandingthepathogenesis pages 78-80, blankson2024understandingthepathogenesis pages 80-83)
5) Organ-specific syndromes emerge (e.g., cerebral malaria with BBB breakdown and neurologic manifestations; placental malaria). (wassmer2024unravellingmysteriesat pages 12-14, ekregbesi2024developingaphysiologic pages 13-16)

6.2 P. vivax (relapsing biology)
1) Acute blood-stage infection causes febrile illness and hematologic effects.
2) Dormant hypnozoites persist in liver and can reactivate, producing relapses that cumulatively erode health and sustain transmission; relapse dominates recurrence burden. (commons2024effectofprimaquine pages 1-2)
3) Radical cure requires 8-aminoquinolines (primaquine/tafenoquine) that target hypnozoites but carry hemolysis risk in G6PD deficiency. (brito2024operationaleffectivenessof pages 1-3, commons2024effectofprimaquine pages 1-2)

7. Phenotypic manifestations (HP-oriented; mechanistic links)
• Fever (systemic inflammatory response; cytokines). (blankson2024understandingthepathogenesis pages 78-80)
• Anemia / severe malarial anemia (hemolysis + impaired erythropoiesis + hypersplenism; hemozoin inhibition of erythropoiesis; oxidative lipid products). (blankson2024understandingthepathogenesis pages 80-83, blankson2024understandingthepathogenesisa pages 80-83)
• Cerebral malaria phenotypes: coma, seizures, neurologic sequelae (linked to sequestration, BBB disruption, endothelial activation, inflammation/coagulation). (wassmer2024unravellingmysteriesat pages 12-14, gopinadhan2024ahumanpluripotent pages 8-10)
• Hypoglycemia / hyperlactatemia (linked to oxidative stress/mitochondrial dysfunction and metabolic shifts). (ekregbesi2024developingaphysiologic pages 13-16)

8. Recent developments and latest research (prioritizing 2023–2024)

8.1 High-fidelity in vitro BBB models for mechanistic and therapeutic discovery (2024)
The 2024 hiPSC-derived BBB model improves physiologic relevance by achieving high baseline TEER and demonstrating rapid Pf-iRBC-induced barrier leak with concurrent adhesion molecule induction, providing a platform for dissecting endothelial injury mechanisms and screening interventions. Figure 1 (schematic + TEER + permeability data) consolidates these endpoints. Publication: May 2024; URL/DOI: https://doi.org/10.1186/s12987-024-00541-9. (gopinadhan2024ahumanpluripotent pages 8-10, gopinadhan2024ahumanpluripotent media b2e9c3aa)

8.2 Systems-level reframing of cerebral malaria pathology (2024 review)
A 2024 Trends in Parasitology review highlights multi-compartment and perivascular-space concepts in cerebral malaria, emphasizing that neuropathology arises from host and parasite factors including endothelial dysfunction and dysregulated immune responses. It cites multiple mechanistic studies with PubMed IDs, including EPCR association with severity (Bernabeu & Smith; PMID 27939609), and CD8+ T cell involvement (Riggle et al.; PMID 31821175). Publication: Jan 2024; URL/DOI: https://doi.org/10.1016/j.pt.2023.11.005. (wassmer2024unravellingmysteriesat pages 12-14)

8.3 Quantitative modern synthesis of vivax relapse biology and primaquine dose–response (2023 online / 2024 print)
A 2024 Lancet Infectious Diseases individual-patient-data meta-analysis (published online Sept 22, 2023; Feb 2024 issue) provides dose–response evidence that higher total primaquine dosing substantially reduces recurrence risk at day 180 (51.0% without primaquine; 19.3% low total dose; 8.1% high total dose), with adjusted hazard ratios vs no primaquine of 0.21 (low-dose) and 0.10 (high-dose). URL/DOI: https://doi.org/10.1016/S1473-3099(23)00430-9. (commons2024effectofprimaquine pages 1-2)

8.4 Real-world radical cure implementation for vivax: tafenoquine/primaquine rollout (2024)
A 2024 Lancet Infectious Diseases operational study in Brazil describes real-world deployment of tafenoquine alongside quantitative G6PD screening (TRuST rollout), with follow-up for recurrences up to day 180 using linked surveillance records, across 43 health-care centres (Sept 2021–Aug 2022). It contextualizes prior trial evidence including ~70% reduction in recurrence vs placebo, and emphasizes hemolysis risk management via G6PD testing. Publication: Jun 2024; URL/DOI: https://doi.org/10.1016/S1473-3099(24)00074-4. (brito2024operationaleffectivenessof pages 1-3)

8.5 Prevention innovations: monoclonal antibody prophylaxis in endemic settings (2024)
A phase 2 NEJM trial in Mali evaluated subcutaneous L9LS in children (6–10 years) during a 6-month malaria season. Quantitative efficacy results: P. falciparum infection occurred in 81% of placebo vs 48% (150 mg) and 40% (300 mg), yielding efficacy of 66% and 70% against infection, and 67% and 77% against clinical malaria, respectively. Publication: May 2024; URL/DOI: https://doi.org/10.1056/NEJMoa2312775. (brito2024operationaleffectivenessof pages 1-3)

9. Current applications and real-world implementations

9.1 Global burden context (WHO 2023 data summarized in 2024 sources)
Multiple 2024 sources summarizing the WHO World Malaria Report 2023 converge on: 249 million malaria cases and 608,000 deaths in 2022, with strong concentration in Africa and in young children. A directly quotable sentence from a 2024 SMC implementation paper states: “Globally, an estimated 249 million malaria cases occurred in 2022, leading to 608,000 malaria deaths in a single year.” (Jan 2024; DOI: https://doi.org/10.58614/jahsm481). (musa2024impactandacceptability pages 1-2)
A 2024 World Malaria Report summary article with DOI provides additional distributional details: children under 5 years accounted for 76% of malaria deaths in 2022, and Africa contributed ~233 million cases (93.6% of global cases). Publication: Jun 2024; URL/DOI: https://doi.org/10.56786/phwr.2024.17.32.1. (shin20242023worldmalaria pages 1-4)

9.2 Radical cure programs (P. vivax)
Implementation of tafenoquine in Brazil is an example of health-system translation of pathophysiology (hypnozoite eradication) into practice, integrating point-of-care quantitative G6PD testing to mitigate hemolysis risk and using surveillance databases to assess recurrence through day 180. (brito2024operationaleffectivenessof pages 1-3)

9.3 Endothelial/BBB platforms for therapeutic testing
The hiPSC-BBB cerebral malaria model provides a practical experimental system that can be used to test interventions aimed at preventing iRBC-induced barrier breakdown (e.g., anti-adhesion therapies, anti-inflammatory strategies, barrier stabilizers), using TEER and fluorescein permeability as quantitative endpoints. (gopinadhan2024ahumanpluripotent pages 8-10, gopinadhan2024ahumanpluripotent media b2e9c3aa)

10. Expert opinion and authoritative analysis (from 2024 sources)

10.1 Mechanistic consensus on cerebral malaria drivers
The Trends in Parasitology review frames cerebral malaria as a multi-factorial syndrome involving “host and parasite factors, with endothelial dysfunction” and highlights EPCR-related severity, immune cell contributions (including CD8+ T cells), and extracellular vesicle-mediated vascular effects, emphasizing that neuropathology cannot be reduced to a single adhesion interaction. (wassmer2024unravellingmysteriesat pages 12-14)

10.2 Radical cure as a hypnozoite-targeting imperative
The 2024 Lancet Infectious Diseases IPD meta-analysis and the Brazil operational study both reinforce that eliminating hypnozoites is central for preventing recurrence/relapse, but that implementation must address hemolysis risks (G6PD deficiency) and adherence feasibility. (brito2024operationaleffectivenessof pages 1-3, commons2024effectofprimaquine pages 1-2)

11. Key statistics and data (recent)

Global epidemiology (WHO 2023 WMR, as summarized in 2024 publications)
• 2022 global malaria burden: ~249 million cases; ~608,000 deaths. (shin20242023worldmalaria pages 1-4, musa2024impactandacceptability pages 1-2)
• Under-5 mortality share: 76% of malaria deaths in 2022 were in children under 5 years. (shin20242023worldmalaria pages 1-4)

Vivax relapse biology and primaquine effect sizes
• Estimated 66–95% of vivax cases are relapses from hypnozoites. (commons2024effectofprimaquine pages 1-2)
• Recurrence risk at day 180: 51.0% without primaquine vs 19.3% (low total dose) vs 8.1% (high total dose). (commons2024effectofprimaquine pages 1-2)
• Adjusted hazard ratio vs no primaquine: 0.21 (low dose) and 0.10 (high dose). (commons2024effectofprimaquine pages 1-2)

BBB disruption model (P. falciparum)
• Baseline TEER: hiPSC-BMECs ~1200 Ω·cm2 vs immortalized cells ~100 Ω·cm2; Pf-iRBC exposure causes TEER drop and fluorescein permeability increase at ~6 h. (gopinadhan2024ahumanpluripotent pages 8-10, gopinadhan2024ahumanpluripotent media b2e9c3aa)

Severe malarial anemia and hemozoin
• Circulating hemozoin: ~1–10 µg/mL reported, with direct erythropoiesis inhibition and oxidative lipid product induction (15-HETE, 4HNE) linked to RBC stiffening and shortened lifespan. (blankson2024understandingthepathogenesis pages 80-83)

12. Evidence items with PMIDs (when available from retrieved sources)

• EPCR association with severe malaria (cited in Wassmer et al. 2024 review): Bernabeu & Smith; PMID 27939609. (wassmer2024unravellingmysteriesat pages 12-14)
• CD8+ T cell targeting of cerebrovasculature in cerebral malaria (cited in Wassmer et al. 2024 review): Riggle et al.; PMID 31821175. (wassmer2024unravellingmysteriesat pages 12-14)
• ABO association evidence is listed in Open Targets with example PMIDs including 37708213 (PMC10522014). (gopinadhan2024ahumanpluripotent media b2e9c3aa)

Note: Several key mechanistic claims in this report come from 2024 reviews that cite primary literature (PMIDs), but the full primary articles themselves were not directly retrieved in this run; therefore, additional PMIDs for each mechanistic sub-claim (e.g., specific PfEMP1 domain interactions, coagulation pathway components) should be curated from the reference lists of these reviews during knowledge-base ingestion. (wassmer2024unravellingmysteriesat pages 12-14, blankson2024understandingthepathogenesis pages 80-83)

Appendix A. Ontology-ready annotation suggestions (seed set)

A1. Genes/proteins (HGNC)
• ICAM1; VCAM1; PROCR (EPCR); TNF; IFNG; IL1B; IL6; CXCR4; MIF; MMP9; TLR9; NLRP3. (blankson2024understandingthepathogenesis pages 80-83, blankson2024understandingthepathogenesis pages 78-80, ekregbesi2024developingaphysiologic pages 13-16, gopinadhan2024ahumanpluripotent pages 8-10)

A2. Biological processes (GO)
• iRBC cytoadherence / cell adhesion; endothelial activation; regulation of vascular permeability; inflammatory response; cytokine-mediated signaling pathway; inflammasome complex activation; neutrophil extracellular trap formation; erythrocyte homeostasis; regulation of erythrocyte differentiation/erythropoiesis. (blankson2024understandingthepathogenesis pages 78-80, ekregbesi2024developingaphysiologic pages 13-16, gopinadhan2024ahumanpluripotent pages 8-10)

A3. Cellular components (GO-CC)
• Endothelial tight junction; plasma membrane; extracellular vesicle/microparticle; extracellular space; basement membrane. (blankson2024understandingthepathogenesis pages 78-80, gopinadhan2024ahumanpluripotent pages 8-10)

A4. Cell types (CL)
• Brain microvascular endothelial cell; monocyte; macrophage; neutrophil; erythrocyte. (blankson2024understandingthepathogenesis pages 78-80, gopinadhan2024ahumanpluripotent pages 8-10)

A5. Anatomical entities (UBERON)
• Liver; spleen; brain microvasculature/blood–brain barrier; placenta. (blankson2024understandingthepathogenesis pages 78-80, ekregbesi2024developingaphysiologic pages 13-16, gopinadhan2024ahumanpluripotent pages 8-10)

A6. Chemicals (CHEBI)
• Hemozoin; sodium fluorescein; 15-HETE; 4HNE; primaquine; tafenoquine; chloroquine. (blankson2024understandingthepathogenesis pages 80-83, brito2024operationaleffectivenessof pages 1-3, gopinadhan2024ahumanpluripotent pages 8-10)

Key cited 2023–2024 sources (URLs, publication dates)
• Shin et al. 2024 (Jun 2024). 2023 World Malaria Report summary. Public Health Weekly Report. https://doi.org/10.56786/phwr.2024.17.32.1 (shin20242023worldmalaria pages 1-4)
• Dev & Wangdi 2024 (Jun 2024). World Malaria Day editorial. Frontiers in Public Health. https://doi.org/10.3389/fpubh.2024.1433213 (dev2024editorialworldmalaria pages 1-2)
• Gopinadhan et al. 2024 (May 2024). BBB model in cerebral malaria. Fluids and Barriers of the CNS. https://doi.org/10.1186/s12987-024-00541-9 (gopinadhan2024ahumanpluripotent pages 8-10)
• Wassmer et al. 2024 (Jan 2024). Cerebral malaria perivascular space review. Trends in Parasitology. https://doi.org/10.1016/j.pt.2023.11.005 (wassmer2024unravellingmysteriesat pages 12-14)
• Commons et al. 2024 (Feb 2024 issue; online Sept 2023). Primaquine dose IPD meta-analysis. Lancet Infectious Diseases. https://doi.org/10.1016/S1473-3099(23)00430-9 (commons2024effectofprimaquine pages 1-2)
• Brito et al. 2024 (Jun 2024). Tafenoquine/primaquine operational effectiveness in Brazil. Lancet Infectious Diseases. https://doi.org/10.1016/S1473-3099(24)00074-4 (brito2024operationaleffectivenessof pages 1-3)
• Kayentao et al. 2024 (May 2024). L9LS monoclonal antibody prophylaxis. NEJM. https://doi.org/10.1056/NEJMoa2312775 (brito2024operationaleffectivenessof pages 1-3)

Figure citation
• Figure: BBB model schematic + TEER reduction + fluorescein permeability increase after Pf-iRBC co-culture (Gopinadhan et al. 2024, Figure 1). (gopinadhan2024ahumanpluripotent media b2e9c3aa)

References

1. (commons2024effectofprimaquine pages 1-2): Robert J Commons, Megha Rajasekhar, Peta Edler, Tesfay Abreha, Ghulam R Awab, J Kevin Baird, Bridget E Barber, Cindy S Chu, Liwang Cui, André Daher, Lilia Gonzalez-Ceron, Matthew J Grigg, Jimee Hwang, Harin Karunajeewa, Marcus V G Lacerda, Simone Ladeia-Andrade, Kartini Lidia, Alejandro Llanos-Cuentas, Rhea J Longley, Dhelio B Pereira, Ayodhia P Pasaribu, Sasithon Pukrittayakamee, Komal R Rijal, Inge Sutanto, Walter R J Taylor, Pham V Thanh, Kamala Thriemer, José Luiz F Vieira, James A Watson, Lina M Zuluaga-Idarraga, Nicholas J White, Philippe J Guerin, Julie A Simpson, Ric N Price, Bipin Adhikari, Nicholas M Anstey, Ashenafi Assefa, Sarah C Boyd, Nguyen Hoang Chau, Nicholas PJ Day, Tamiru Shibiru Degaga, Arjen M Dondorp, Annette Erhart, Marcelo Urbano Ferreira, Prakash Ghimire, Justin A Green, Gavin CKW Koh, Asrat Hailu Mekuria, Ivo Mueller, Mohammad Nader Naadim, Erni J Nelwan, Francois Nosten, David J Price, Jetsumon Sattabongkot, Kasia Stepniewska, Lorenz von Seidlein, Timothy William, Charles J Woodrow, and Adugna Woyessa. Effect of primaquine dose on the risk of recurrence in patients with uncomplicated plasmodium vivax: a systematic review and individual patient data meta-analysis. The Lancet Infectious Diseases, 24:172-183, Feb 2024. URL: https://doi.org/10.1016/s1473-3099(23)00430-9, doi:10.1016/s1473-3099(23)00430-9. This article has 56 citations and is from a highest quality peer-reviewed journal.

2. (blankson2024understandingthepathogenesis pages 80-83): SO Blankson. Understanding the pathogenesis of severe malaria: the role of serological markers and plasma-derived extracellular vesicles. Unknown journal, 2024.

3. (blankson2024understandingthepathogenesisa pages 80-83): SO Blankson. Understanding the pathogenesis of severe malaria: the role of serological markers and plasma-derived extracellular vesicles. Unknown journal, 2024.

4. (gopinadhan2024ahumanpluripotent pages 8-10): Adnan Gopinadhan, Jason M. Hughes, Andrea L. Conroy, Chandy C. John, Scott G. Canfield, and Dibyadyuti Datta. A human pluripotent stem cell-derived in vitro model of the blood–brain barrier in cerebral malaria. Fluids and Barriers of the CNS, May 2024. URL: https://doi.org/10.1186/s12987-024-00541-9, doi:10.1186/s12987-024-00541-9. This article has 12 citations and is from a peer-reviewed journal.

5. (blankson2024understandingthepathogenesis pages 78-80): SO Blankson. Understanding the pathogenesis of severe malaria: the role of serological markers and plasma-derived extracellular vesicles. Unknown journal, 2024.

6. (wassmer2024unravellingmysteriesat pages 12-14): Samuel C. Wassmer, Tania F. de Koning-Ward, Georges E.R. Grau, and Saparna Pai. Unravelling mysteries at the perivascular space: a new rationale for cerebral malaria pathogenesis. Trends in Parasitology, 40:28-44, Jan 2024. URL: https://doi.org/10.1016/j.pt.2023.11.005, doi:10.1016/j.pt.2023.11.005. This article has 22 citations and is from a domain leading peer-reviewed journal.

7. (gopinadhan2024ahumanpluripotent media b2e9c3aa): Adnan Gopinadhan, Jason M. Hughes, Andrea L. Conroy, Chandy C. John, Scott G. Canfield, and Dibyadyuti Datta. A human pluripotent stem cell-derived in vitro model of the blood–brain barrier in cerebral malaria. Fluids and Barriers of the CNS, May 2024. URL: https://doi.org/10.1186/s12987-024-00541-9, doi:10.1186/s12987-024-00541-9. This article has 12 citations and is from a peer-reviewed journal.

8. (ekregbesi2024developingaphysiologic pages 13-16): POA Ekregbesi. Developing a physiologic model of placental malaria in mice. Unknown journal, 2024.

9. (blankson2024understandingthepathogenesis pages 220-224): SO Blankson. Understanding the pathogenesis of severe malaria: the role of serological markers and plasma-derived extracellular vesicles. Unknown journal, 2024.

10. (blankson2024understandingthepathogenesisa pages 220-224): SO Blankson. Understanding the pathogenesis of severe malaria: the role of serological markers and plasma-derived extracellular vesicles. Unknown journal, 2024.

11. (brito2024operationaleffectivenessof pages 1-3): Marcelo Brito, Rosilene Rufatto, José Diego Brito-Sousa, Felipe Murta, Vanderson Sampaio, Patrícia Balieiro, Djane Baía-Silva, Vanessa Castro, Brenda Alves, Aline Alencar, Stephan Duparc, Penny Grewal Daumerie, Isabelle Borghini-Fuhrer, Elodie Jambert, Cássio Peterka, Francisco Edilson Lima, Leonardo Carvalho Maia, Catherine Lucena Cruz, Bruna Maciele, Mariana Vasconcelos, Myrna Machado, Elder Augusto Figueira, Antônio Alcirley Balieiro, Dhelio Batista Pereira, and Marcus Lacerda. Operational effectiveness of tafenoquine and primaquine for the prevention of plasmodium vivax recurrence in brazil: a retrospective observational study. The Lancet Infectious Diseases, 24:629-638, Jun 2024. URL: https://doi.org/10.1016/s1473-3099(24)00074-4, doi:10.1016/s1473-3099(24)00074-4. This article has 28 citations and is from a highest quality peer-reviewed journal.

12. (musa2024impactandacceptability pages 1-2): Abuhuraira Ado Musa, Shuaibu Sulieman, Abdulbaqi Alhaji Magaji, Rashidat Oluwabukola Owolabi, and Maryam Dahiru Umar. Impact and acceptability of seasonal malaria chemoprevention (smc) and pharmacovigilance campaign among under-five children in nigeria: an explanatory study. Journal of Applied Health Sciences and Medicine, Jan 2024. URL: https://doi.org/10.58614/jahsm481, doi:10.58614/jahsm481. This article has 1 citations.

13. (shin20242023worldmalaria pages 1-4): Hyun-Il Shin, Bor-Ming Ku, Haneul Jung, So-dam Lee, Seon-Young Lee, Jung-Won Ju, Jonghee Kim, and Hee-Il Lee. 2023 world malaria report (status of world malaria in 2022). Public Health Weekly Report, 17:1351-1377, Jun 2024. URL: https://doi.org/10.56786/phwr.2024.17.32.1, doi:10.56786/phwr.2024.17.32.1. This article has 19 citations.

14. (dev2024editorialworldmalaria pages 1-2): Vas Dev and Kinley Wangdi. Editorial: world malaria day 2023 - ending malaria transmission: reaching the last mile to zero malaria. Frontiers in Public Health, Jun 2024. URL: https://doi.org/10.3389/fpubh.2024.1433213, doi:10.3389/fpubh.2024.1433213. This article has 2 citations.