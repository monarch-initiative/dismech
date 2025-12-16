---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-15T10:02:05.172384'
end_time: '2025-12-15T10:10:08.032076'
duration_seconds: 482.86
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Tuberculosis
  mondo_id: ''
  category: Infectious Disease
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 19
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Tuberculosis
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Tuberculosis**.
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
- **Disease Name:** Tuberculosis
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Tuberculosis**.
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


Disease Pathophysiology Research Report: Tuberculosis

Target Disease
- Disease Name: Tuberculosis
- MONDO ID: not specified
- Category: Infectious Disease

Pathophysiology Description
Mycobacterium tuberculosis (Mtb) subverts innate immune defenses through specialized secretion systems, metabolic reprogramming of host phagocytes, and induction of maladaptive inflammatory programs. Type VII secretion, especially ESX-1, promotes phagosomal membrane damage and cytosolic access, which triggers cytosolic DNA sensing through cGAS–STING–TBK1 and induction of type I interferon (IFN) programs; ESX effectors can concomitantly inhibit autophagy and impair phagosome maturation, facilitating intracellular survival (jiang2024mycobacteriumtuberculosisvii pages 1-2). Metabolic rewiring of macrophage cholesterol handling fuels foamy macrophage formation and creates nutrient-rich, permissive niches (chen2024theimpactof pages 1-2). In the lung, spatial single-cell and spatial-transcriptomic profiling indicates distinct microenvironments: alveolar regions harbor TREM2+ foamy macrophages enriched for lipid handling genes and Mtb antigens, whereas granuloma cores exhibit interferon-driven antimicrobial signatures (teles2025spatialprofilingreveals pages 5-8, teles2025spatialprofilingreveals pages 8-11). Neutrophils contribute importantly to immunopathology; type I IFN–linked neutrophil programs and neutrophil extracellular traps (NETs) correlate with tissue damage and relapse risk, positioning NET-associated pathways as potential host-directed therapy (HDT) targets (saqib2025pathogenicrolefor pages 26-27). Inflammasome pathways (e.g., NLRP3/AIM2→caspase-1→IL‑1β) have context-dependent roles in early control versus pathology and are actionable in HDT concepts (cebani2024canweexploit pages 1-2).

Key Concepts and Definitions with Current Understanding
- Type VII secretion (ESX-1): A specialized secretion system that exports virulence substrates (e.g., EsxA/ESAT‑6 and EsxB/CFP‑10) to permeabilize the phagosomal membrane, enabling cytosolic access and engagement of host DNA sensors (jiang2024mycobacteriumtuberculosisvii pages 1-2).
- Cytosolic DNA sensing (cGAS–STING–TBK1): Host pathway that detects bacterial DNA in the cytosol and induces type I IFN responses; in TB, activation can both promote antimicrobial programs and drive detrimental inflammation depending on timing and magnitude (jiang2024mycobacteriumtuberculosisvii pages 1-2).
- Foamy macrophages: Lipid droplet–rich macrophages formed through increased cholesterol uptake/synthesis and impaired efflux, supporting Mtb persistence and TB progression (chen2024theimpactof pages 1-2). In human TB lungs, a TREM2+ foamy macrophage program is spatially concentrated in alveoli (teles2025spatialprofilingreveals pages 5-8, teles2025spatialprofilingreveals pages 8-11).
- NETosis/NETs: Neutrophil extracellular traps contribute to TB tissue pathology (caseating granulomas, vascular occlusion) and may be driven by IFN-linked programs; restraining NET formation can improve outcomes in relevant models (saqib2025pathogenicrolefor pages 26-27).
- Inflammasomes: Canonical (e.g., NLRP3, AIM2) and non-canonical (caspase‑4/5/11) complexes mature IL‑1β/IL‑18 and drive pyroptosis; balanced modulation is a candidate HDT strategy in TB (cebani2024canweexploit pages 1-2).

Recent Developments and Latest Research (2023–2024 priority)
- ESX effector Rv2347c/EsxP: “Rv2347c … inhibits the expression of the early marker RAB5 of phagosomes … triggers the host’s cytoplasmic sensing pathway STING/TBK1, inhibiting autophagy and upregulating IFNβ transcription” (Microbiology Spectrum, Nov 2024; DOI: 10.1128/spectrum.01188-24) (jiang2024mycobacteriumtuberculosisvii pages 1-2).
- Macrophage cholesterol metabolism: Mtb increases LDL uptake and de novo cholesterol synthesis, suppresses cholesterol ester hydrolysis and ABC-transporter–mediated efflux, driving lipid droplet accumulation and foam cell formation that facilitates persistence and granuloma/cavitation (Frontiers in Immunology, May 2024; DOI: 10.3389/fimmu.2024.1402024) (chen2024theimpactof pages 1-2).
- Spatial single-cell mapping in human TB: Alveoli/pneumonia regions contain TREM2+ foamy macrophages enriched for lipid metabolism (APOE, LIPA, NPC2, PLIN2), while granuloma cores show IFN-activated macrophages and higher expression of antimicrobial genes; TREM2 colocalizes with lipid droplets and Mtb antigens (bioRxiv, Aug 2025; DOI: 10.1101/2025.07.15.664002) (teles2025spatialprofilingreveals pages 5-8, teles2025spatialprofilingreveals pages 8-11).
- Neutrophil pathogenic programs: Type I IFN–linked neutrophil responses drive lung inflammation, NETosis, and pathology; specific neutrophil subsets (e.g., CD101‑negative) and NET-associated mechanisms are implicated as targets (Cell Reports, Jan 2025; DOI: 10.1016/j.celrep.2024.115072) (saqib2025pathogenicrolefor pages 26-27).
- Inflammasome HDT concepts: Reviews detail priming (TLRs→NF‑κB), activation (NLRP3/AIM2), caspase‑1/11/4/5, gasdermin D, and IL‑1 family maturation as targets for precision modulation in TB (IJMS, Jul 2024; DOI: 10.3390/ijms25158196) (cebani2024canweexploit pages 1-2).

Current Applications and Real‑World Implementations
- Pathway-informed HDTs: Reviews emphasize adjunctive HDTs to enhance autophagy, temper excessive inflammasome activity, or reprogram macrophage lipid metabolism alongside antibiotics, including repurposed drugs and small molecules (Frontiers in Immunology, Jan 2024; DOI: 10.3389/fimmu.2023.1305325) (zhao2024hostdirectedtherapyagainst pages 14-14). Translational implications also extend to NET inhibition strategies where excessive NETosis drives tissue injury (saqib2025pathogenicrolefor pages 26-27).
- Spatially guided targets: Spatial profiling highlights distinct compartments (alveoli versus granuloma core) and cell states (TREM2+ foamy versus IFN-activated macrophages), guiding localized or state-specific interventions (teles2025spatialprofilingreveals pages 5-8, teles2025spatialprofilingreveals pages 8-11).

Expert Opinions and Analysis from Authoritative Sources
- ESX-1 as central virulence hub: The 2024 Microbiology Spectrum study and related literature converge on ESX-1 as a driver of phagosomal rupture and downstream type I IFN induction, with specific effectors (e.g., EsxP) also inhibiting autophagy—an actionable axis for antivirulence or HDT strategies (jiang2024mycobacteriumtuberculosisvii pages 1-2).
- Lipid metabolism as a therapeutic node: The 2024 Frontiers in Immunology review argues that reducing host cholesterol availability or restoring efflux can limit Mtb invasion and enhance antibiotic efficacy—offering a rational HDT direction (chen2024theimpactof pages 1-2).
- Compartmentalized pathophysiology: Spatial single-cell work reveals alveoli enriched in lipid‑handling macrophages harboring Mtb antigens, versus granuloma cores with IFN‑driven antimicrobial programs—supporting tailored interventions by lesion context (teles2025spatialprofilingreveals pages 5-8, teles2025spatialprofilingreveals pages 8-11).
- NETs as double-edged swords: Neutrophil/NET programs are repeatedly implicated in advanced disease; strategies that limit NETosis (e.g., PAD4 inhibition) without broadly suppressing host defense merit investigation (saqib2025pathogenicrolefor pages 26-27).
- Inflammasome balance: Reviews stress that both insufficient and excessive inflammasome activity are harmful, advocating precision modulation rather than wholesale suppression (cebani2024canweexploit pages 1-2).

Relevant Statistics and Data from Recent Studies
- Spatial single-cell atlas (human pulmonary TB): 45,023 single cells profiled (avg. ~1,017 genes/cell), 27 cell types (10 myeloid, 7 lymphocyte); TREM2+ foamy macrophages localized to alveoli; granuloma cores with higher antimicrobial gene expression (e.g., 15 genes significantly higher vs alveoli, adjusted p = 3.72×10⁻⁷) (bioRxiv, Aug 2025; DOI: 10.1101/2025.07.15.664002) (teles2025spatialprofilingreveals pages 5-8).
- TREM2 induction by mycobacterial lipids: Mycolic acids and PDIM induced ~50–55% TREM2+ macrophages in vitro; live Mtb induced ~30% TREM2+ cells; TREM2–DAP12 reporter correlated with activation (r=0.93, p=0.007) (bioRxiv, Aug 2025; DOI: 10.1101/2025.07.15.664002) (teles2025spatialprofilingreveals pages 8-11).

Core Pathophysiology
- Primary mechanisms: ESX-1–mediated phagosome damage and cytosolic translocation; cGAS–STING–TBK1–IRF3 activation and type I IFN responses; autophagy inhibition by ESX effectors; host lipid metabolic reprogramming→foamy macrophages; neutrophil activation and NETosis; compartmentalized lesion biology (jiang2024mycobacteriumtuberculosisvii pages 1-2, chen2024theimpactof pages 1-2, teles2025spatialprofilingreveals pages 5-8, saqib2025pathogenicrolefor pages 26-27).
- Dysregulated pathways: Type I IFN signaling, autophagy, cholesterol uptake/efflux and ester metabolism, inflammasome activation (jiang2024mycobacteriumtuberculosisvii pages 1-2, chen2024theimpactof pages 1-2, cebani2024canweexploit pages 1-2).
- Affected cellular processes: Phagosome maturation/lysosome fusion, xenophagy/autophagy flux, lipid droplet biogenesis, NET formation, IFN-stimulated gene programs (jiang2024mycobacteriumtuberculosisvii pages 1-2, chen2024theimpactof pages 1-2, saqib2025pathogenicrolefor pages 26-27).

Key Molecular Players
- Genes/Proteins: EsxA/EsxB (ESX-1), Rv2347c/EsxP, cGAS, STING, TBK1, IRF3, IFN‑β, TREM2, APOE, NPC2, PLIN2, LIPA, ABC transporters (ABCA1/ABCG1 class), IL‑1β (jiang2024mycobacteriumtuberculosisvii pages 1-2, chen2024theimpactof pages 1-2, teles2025spatialprofilingreveals pages 5-8, cebani2024canweexploit pages 1-2).
- Chemical entities: Cholesterol (ChEBI:28694); interferon‑β; NET-modulatory agents (e.g., PAD4 inhibitors) as conceptual HDTs (chen2024theimpactof pages 1-2, saqib2025pathogenicrolefor pages 26-27).
- Cell types: Macrophages (alveolar, TREM2+ foamy, IFN-activated), neutrophils, Th17 cells, dendritic cells (teles2025spatialprofilingreveals pages 5-8, saqib2025pathogenicrolefor pages 26-27).
- Anatomical locations: Alveoli/pneumonia regions versus granuloma cores/mantles (teles2025spatialprofilingreveals pages 5-8).

Biological Processes (GO) for Annotation
- Type I interferon signaling (GO:0034138): cGAS–STING–TBK1–IRF3–IFNβ axis following ESX-1–mediated cytosolic access (jiang2024mycobacteriumtuberculosisvii pages 1-2).
- Autophagy/xenophagy (GO:0006914): Targeted and inhibited by ESX effectors; HDT target (jiang2024mycobacteriumtuberculosisvii pages 1-2).
- Lipid metabolic process (GO:0006629): Cholesterol uptake/synthesis, esterification and impaired efflux leading to foamy macrophages (chen2024theimpactof pages 1-2).
- Cholesterol transport (GO:0030301): ABC transporter–mediated efflux is suppressed during infection (chen2024theimpactof pages 1-2).
- Neutrophil degranulation/NET formation (GO:0043312): Contributes to tissue injury and relapse risk (saqib2025pathogenicrolefor pages 26-27).
- Inflammasome complex assembly and IL‑1β maturation: Context-dependent protective/pathologic roles; HDT node (cebani2024canweexploit pages 1-2).

Cellular Components
- Phagosome and phagolysosome membranes; cytosol (site of cGAS–STING sensing after ESX-mediated rupture) (jiang2024mycobacteriumtuberculosisvii pages 1-2).
- Lipid droplets (PLIN2+) and lysosomes (NPC2/LIPA) in foamy macrophages (teles2025spatialprofilingreveals pages 5-8, chen2024theimpactof pages 1-2).
- Extracellular region (NETs); inflammasome complexes (cytosolic) (saqib2025pathogenicrolefor pages 26-27, cebani2024canweexploit pages 1-2).

Disease Progression (sequence of events)
- Inhalation and alveolar deposition → uptake by alveolar macrophages → ESX-1–mediated phagosome damage and cytosolic access → cGAS–STING–TBK1–IRF3 activation and type I IFN programs; autophagy inhibition by ESX effectors (e.g., EsxP) → metabolic rewiring of macrophages to lipid-laden, TREM2+ foamy states in alveoli → lesion heterogeneity with granuloma cores enriched for IFN‑activated antimicrobial signatures and neutrophil influx/NETs in progressive disease → cavitation and dissemination in advanced disease (jiang2024mycobacteriumtuberculosisvii pages 1-2, chen2024theimpactof pages 1-2, teles2025spatialprofilingreveals pages 5-8, saqib2025pathogenicrolefor pages 26-27).

Phenotypic Manifestations (mechanism–phenotype links)
- Caseating necrosis and tissue destruction: Associated with neutrophil-driven inflammation and NETosis; vascular occlusions with neutrophil aggregates reported in TB (mechanistic framework; NETs) (saqib2025pathogenicrolefor pages 26-27).
- Alveolar pneumonia with macrophage lipid accumulation: TREM2+ foamy macrophages colocalize with Mtb antigens and lipid droplets in alveoli (teles2025spatialprofilingreveals pages 5-8, teles2025spatialprofilingreveals pages 8-11).
- Granuloma core IFN bias: IFN-driven antimicrobial gene expression and IFN-activated macrophage states correspond to granuloma cores (teles2025spatialprofilingreveals pages 5-8).

Evidence Items with URLs and Publication Dates
- Jiang et al., 2024 (Microbiology Spectrum, Nov 2024): “Rv2347c … blocks the maturation of phagosomes … activates the STING/TBK1 signaling pathway to inhibit cell autophagy” (DOI: 10.1128/spectrum.01188-24; https://doi.org/10.1128/spectrum.01188-24) (jiang2024mycobacteriumtuberculosisvii pages 1-2).
- Chen et al., 2024 (Frontiers in Immunology, May 30, 2024): “Mtb infection increases the uptake of LDL and cholesterol … suppresses ABC transporters … promoting the formation of lipid droplets and foam cells” (DOI: 10.3389/fimmu.2024.1402024; https://doi.org/10.3389/fimmu.2024.1402024) (chen2024theimpactof pages 1-2).
- Teles et al., 2025 preprint (bioRxiv, Aug 2025): Spatial profiling of human TB lungs identifies TREM2+ foamy macrophages in alveoli and IFN-activated programs in granuloma cores; TREM2 colocalizes with PLIN2 and Mtb antigens; mycolic acids/PDIM induce ~50–55% TREM2+ macrophages (DOI: 10.1101/2025.07.15.664002; https://doi.org/10.1101/2025.07.15.664002) (teles2025spatialprofilingreveals pages 5-8, teles2025spatialprofilingreveals pages 8-11).
- Saqib et al., 2025 (Cell Reports, Jan 2025): Type I IFN–mediated neutrophil programs drive immunopathology and NETosis; NETs implicated in TB tissue damage and as therapeutic targets (DOI: 10.1016/j.celrep.2024.115072; https://doi.org/10.1016/j.celrep.2024.115072) (saqib2025pathogenicrolefor pages 26-27).
- Cebani & Mvubu, 2024 (International Journal of Molecular Sciences, Jul 2024): Inflammasome pathways (NLRP3/AIM2→caspase‑1→IL‑1β; non‑canonical caspase‑4/5/11) as HDT targets in TB (DOI: 10.3390/ijms25158196; https://doi.org/10.3390/ijms25158196) (cebani2024canweexploit pages 1-2).
- Zhao et al., 2024 (Frontiers in Immunology, Jan 2024): Review of HDT strategies for TB and TB–diabetes comorbidity, including autophagy promotion and immunomodulation (DOI: 10.3389/fimmu.2023.1305325; https://doi.org/10.3389/fimmu.2023.1305325) (zhao2024hostdirectedtherapyagainst pages 14-14).

Structured, Ontology-Linked Annotations
| Category | Entity (identifier) | Role in TB | Key Process/Pathway (GO) | Cellular Component (GO/CC) | Cell Type (CL) | Anatomical Site (UBERON) | Chemical/Drug (ChEBI) | Evidence |
|---|---|---|---|---|---|---|---|---|
| Secretion system | ESX-1 (Type VII secretion system) | Mediates phagosomal membrane permeabilization and secretion of ESX substrates that enable cytosolic access and immune modulation | secretion / phagosomal membrane permeabilization (ESX-1 function) | bacterial secretion apparatus / phagosome membrane | infected macrophage (CL:0000235) | alveolus of lung (UBERON:0008952) | — | Microbiology Spectrum doi:10.1128/spectrum.01188-24; Nov 2024 (jiang2024mycobacteriumtuberculosisvii pages 1-2) |
| Effector proteins | EsxA / EsxB (ESAT-6 / CFP-10) | Pore-forming effectors that contribute to phagosomal rupture and downstream host sensing | (ESX-1 substrate secretion) | phagosomal membrane / pore complex | macrophage (CL:0000235) | phagosome / cytosol (lung) | — | Microbiology Spectrum doi:10.1128/spectrum.01188-24; Nov 2024 (jiang2024mycobacteriumtuberculosisvii pages 1-2) |
| Effector protein | Rv2347c / EsxP (Rv2347c) | Blocks phagosome maturation, promotes phagosome escape → activates STING/TBK1 → ↑IFN-β and inhibits autophagy | GO:0034138 type I interferon signaling pathway; GO:0006914 autophagy (inhibition) | phagosome / cytosol; STING-associated membranes | macrophage (CL:0000235) | alveolus of lung (UBERON:0008952) | — | Microbiology Spectrum doi:10.1128/spectrum.01188-24; Nov 2024 (jiang2024mycobacteriumtuberculosisvii pages 1-2) |
| Cytosolic DNA sensor axis | cGAS–STING–TBK1–IRF3 → IFN-β | Cytosolic DNA sensing of escaped Mtb triggers type I IFN responses that can be host-protective or pathologic depending on timing/amount | GO:0034138 type I interferon signaling pathway | cytosol; ER-Golgi/ STING localization | macrophage (CL:0000235), dendritic cell | lung parenchyma / granuloma core | interferon-β (ChEBI:interferon-β) | Microbiology Spectrum doi:10.1128/spectrum.01188-24; Nov 2024; Cell Reports summary (jiang2024mycobacteriumtuberculosisvii pages 1-2, saqib2025pathogenicrolefor pages 26-27) |
| Autophagy | Host autophagy (xenophagy) | Autophagy is inhibited by ESX effectors (promotes Mtb survival); restoration is an HDT target | GO:0006914 autophagy | autophagosome / lysosome (GO:0005764) | macrophage (CL:0000235) | intracellular compartment (lung) | mTOR inhibitors / autophagy inducers (e.g., rapamycin) | Microbiology Spectrum doi:10.1128/spectrum.01188-24; Nov 2024 (jiang2024mycobacteriumtuberculosisvii pages 1-2) |
| Lipid uptake receptor | CD36 (CD36) | Scavenger receptor mediating uptake of lipids/cholesterol → supports foamy macrophage phenotype that favours Mtb persistence | GO:0006629 lipid metabolic process | plasma membrane; endocytic vesicles | macrophage (CL:0000235) | alveolus of lung (UBERON:0008952) | cholesterol (ChEBI:28694) | Frontiers in Immunology doi:10.3389/fimmu.2024.1402024; May 2024 (chen2024theimpactof pages 1-2) |
| Lipid handling protein | APOE (apolipoprotein E) | Mediates lipid trafficking; part of TREM2+/foamy macrophage signature and linked to permissive intracellular niche | GO:0006629 lipid metabolic process | lipid particles / extracellular region | macrophage (CL:0000235) | alveolar space (UBERON:0008952) | cholesterol / apolipoproteins (ChEBI:28694) | Spatial/transcriptomic data (TREM2+ program) doi:10.1101/2025.07.15.664002; Aug 2025 (teles2025spatialprofilingreveals pages 5-8) |
| Intracellular lipid transporter | NPC2 (NPC2) | Lysosomal cholesterol handling; part of foamy macrophage / lipid-droplet program associated with permissive Mtb niches | GO:0030301 cholesterol transport | lysosome / lipid droplet | macrophage (CL:0000235) | alveolus / macrophage lipid droplet | cholesterol (ChEBI:28694) | Spatial/transcriptomic data doi:10.1101/2025.07.15.664002; Aug 2025 (teles2025spatialprofilingreveals pages 5-8) |
| Lipid droplet marker | PLIN2 (perilipin-2) | Marks lipid droplets / foamy macrophages that harbor Mtb antigens; indicates altered host lipid storage | GO:0006629 lipid metabolic process | lipid droplet (GO:0005811) | macrophage (CL:0000235) | alveoli / pneumonia regions (UBERON:0008952) | neutral lipids (ChEBI:5891) | Spatial/transcriptomic data doi:10.1101/2025.07.15.664002; Aug 2025 (teles2025spatialprofilingreveals pages 5-8) |
| Lipase / lipid catabolism | LIPA (lysosomal acid lipase) | Lysosomal hydrolysis of cholesteryl esters / triglycerides; dysregulated in infected macrophages | GO:0006631 fatty acid metabolic process | lysosome | macrophage (CL:0000235) | alveolus / phagolysosome | cholesterol esters (ChEBI:??) | Frontiers in Immunology doi:10.3389/fimmu.2024.1402024; May 2024 (chen2024theimpactof pages 1-2) |
| Cholesterol efflux | ABC transporters (e.g., ABCA1/ABCG1) | Reduced expression during Mtb infection → impaired cholesterol efflux → foam cell formation | GO:0030301 cholesterol transport | plasma membrane / lipid raft | macrophage (CL:0000235) | alveolus / lung | cholesterol (ChEBI:28694) | Frontiers in Immunology doi:10.3389/fimmu.2024.1402024; May 2024 (chen2024theimpactof pages 1-2) |
| Macrophage subset | TREM2+ foamy macrophages | Lipid-laden, permissive macrophage population concentrated in alveoli; colocalize with Mtb antigens and lipid droplets | GO:0006629 lipid metabolic process | lipid droplets; phagolysosome | macrophage (CL:0000235; TREM2+ subset) | alveolus of lung (UBERON:0008952) | — | Spatial/transcriptomic & proteomics doi:10.1101/2025.07.15.664002; Aug 2025 (teles2025spatialprofilingreveals pages 5-8) |
| Neutrophil effector structures | NETs (MPO, neutrophil elastase; PAD4-dependent) | NETosis characterizes caseating granulomas; contributes to tissue damage, immunothrombosis and relapse risk | GO:0043312 neutrophil degranulation / NET formation | extracellular traps (extracellular region) | neutrophil (CL:0000775) | granuloma core / pulmonary vessels | PAD4 inhibitors (e.g., Cl-amidine) | Cell Reports / review summaries doi:10.1016/j.celrep.2024.115072; Jan 2025 (saqib2025pathogenicrolefor pages 26-27) |
| Inflammasome pathway | NLRP3 / AIM2 → caspase-1 → IL-1β | Canonical inflammasomes mature IL-1β/IL-18 and drive pyroptosis; dual role (control vs tissue damage); candidate HDT targets | (inflammasome activation; IL-1β maturation) | inflammasome complex (cytosol) | macrophage / DC (CL:0000235; CL:0001056) | granuloma / lung | IL-1β (ChEBI:17052) | Int J Mol Sci doi:10.3390/ijms25158196; Jul 2024 (cebani2024canweexploit pages 1-2) |
| Spatial compartments | Alveoli (pneumonia) vs granuloma core (lesion) | Distinct programs: alveoli enriched for lipid metabolism/foamy macrophages; granuloma core enriched for IFN-driven antimicrobial programs and SPP1+/IFN-activated macrophages | alveoli: lipid metabolism (GO:0006629); core: type I/II IFN & antimicrobial responses (GO:0034138) | alveolar lumen vs granuloma core | alveolar macrophage (CL:0000235); IFN-activated macrophage | alveolus of lung (UBERON:0008952); granulomatous lesion (region) | — | Spatial single-cell & ROI profiling doi:10.1101/2025.07.15.664002; Aug 2025 (teles2025spatialprofilingreveals pages 5-8) |
| Host-directed therapy (HDT) targets | HDT (autophagy inducers, lipid modulators, inflammasome modulators) | Therapeutic strategies to restore autophagy, limit pathological inflammation, or reprogram macrophage lipid handling | autophagy promotion; inflammasome modulation; metabolic reprogramming | various (autophagosome, inflammasome) | macrophage, neutrophil, DC | lung / systemic | candidate drugs cited in reviews (repurposed agents) | Frontiers in Immunology (HDT review) doi:10.3389/fimmu.2023.1305325; Jan 2024 (zhao2024hostdirectedtherapyagainst pages 14-14) |


*Table: Concise ontology-ready annotations linking key TB mechanisms, genes/proteins, cell types, compartments, and candidate chemicals with source DOIs and context IDs; useful for knowledge‑base ingestion and evidence-traced curation.*

Abbreviations and Ontologies
- HGNC: TREM2, APOE, NPC2, PLIN2, LIPA, CD36, TBK1, IRF3, IL1B.
- GO: GO:0034138 (type I IFN signaling); GO:0006914 (autophagy); GO:0006629 (lipid metabolism); GO:0030301 (cholesterol transport); GO:0043312 (neutrophil degranulation/NET formation).
- CL: CL:0000235 (macrophage); CL:0000775 (neutrophil).
- UBERON: UBERON:0008952 (alveolus of lung).
- CHEBI: CHEBI:28694 (cholesterol).

Limitations and Open Questions
- Although type I IFN signatures and NETs are implicated in pathogenesis, the precise windows where IFN or NET modulation improves clinical outcomes remain to be defined in humans (saqib2025pathogenicrolefor pages 26-27).
- Spatial single-cell findings are compelling but include preprint data; further peer-reviewed validation and integration with clinical phenotypes are needed (teles2025spatialprofilingreveals pages 5-8, teles2025spatialprofilingreveals pages 8-11).

Overall, contemporary evidence supports a model in which ESX-1–driven cytosolic access and cGAS–STING activation, macrophage lipid reprogramming to TREM2+ foamy states, and type I IFN–linked neutrophil/NET programs collectively drive TB progression, while inflammasome and autophagy pathways offer promising HDT entry points (jiang2024mycobacteriumtuberculosisvii pages 1-2, chen2024theimpactof pages 1-2, teles2025spatialprofilingreveals pages 5-8, saqib2025pathogenicrolefor pages 26-27, cebani2024canweexploit pages 1-2, zhao2024hostdirectedtherapyagainst pages 14-14).

References

1. (jiang2024mycobacteriumtuberculosisvii pages 1-2): Zhiyong Jiang, Junfeng Zhen, Yuerigu Abulikena, Chaoyun Gao, Lingxi Huang, Tingting Huang, and Jianping Xie. <i>mycobacterium tuberculosis</i> vii secretion system effector molecule rv2347c blocks the maturation of phagosomes and activates the sting/tbk1 signaling pathway to inhibit cell autophagy. Microbiology Spectrum, Nov 2024. URL: https://doi.org/10.1128/spectrum.01188-24, doi:10.1128/spectrum.01188-24. This article has 8 citations and is from a domain leading peer-reviewed journal.

2. (chen2024theimpactof pages 1-2): Zhanpeng Chen, Xingxing Kong, Quan Ma, Jinyun Chen, Yuqin Zeng, Huazhen Liu, Xiaomin Wang, and Shuihua Lu. The impact of mycobacterium tuberculosis on the macrophage cholesterol metabolism pathway. Frontiers in Immunology, May 2024. URL: https://doi.org/10.3389/fimmu.2024.1402024, doi:10.3389/fimmu.2024.1402024. This article has 19 citations and is from a peer-reviewed journal.

3. (teles2025spatialprofilingreveals pages 5-8): Rosane M. B. Teles, Chaouki Benabdessalem, Jonathan Perrie, Cenfu Wei, Julie West, Bruno J. de Andrade Silva, Priscila R. Andrade, Lilah A. Mansky, Prajan Divakar, Linda Fischbacher, Karen Lam, Feiyang Ma, Kimia Rategh, Aparna Pillai, Samuel M. French, Emna Romdhane, Mohamed-Ridha Barbouche, Eynav Klechevsky, Marco Colonna, Adrie J. C. Steyn, Steven J. Bensinger, Daniel L. Barber, Soumaya Rammeh, Parambir S. Dulai, Bryan D. Bryson, Matteo Pellegrini, John T. Belisle, Barry R. Bloom, and Robert L. Modlin. Spatial profiling reveals trem2+ macrophages as central to mycobacterium tuberculosis pathogenesis in human pulmonary tuberculosis. bioRxiv : the preprint server for biology, Aug 2025. URL: https://doi.org/10.1101/2025.07.15.664002, doi:10.1101/2025.07.15.664002. This article has 0 citations.

4. (teles2025spatialprofilingreveals pages 8-11): Rosane M. B. Teles, Chaouki Benabdessalem, Jonathan Perrie, Cenfu Wei, Julie West, Bruno J. de Andrade Silva, Priscila R. Andrade, Lilah A. Mansky, Prajan Divakar, Linda Fischbacher, Karen Lam, Feiyang Ma, Kimia Rategh, Aparna Pillai, Samuel M. French, Emna Romdhane, Mohamed-Ridha Barbouche, Eynav Klechevsky, Marco Colonna, Adrie J. C. Steyn, Steven J. Bensinger, Daniel L. Barber, Soumaya Rammeh, Parambir S. Dulai, Bryan D. Bryson, Matteo Pellegrini, John T. Belisle, Barry R. Bloom, and Robert L. Modlin. Spatial profiling reveals trem2+ macrophages as central to mycobacterium tuberculosis pathogenesis in human pulmonary tuberculosis. bioRxiv : the preprint server for biology, Aug 2025. URL: https://doi.org/10.1101/2025.07.15.664002, doi:10.1101/2025.07.15.664002. This article has 0 citations.

5. (saqib2025pathogenicrolefor pages 26-27): Mohd Saqib, Shreya Das, Tanvir N. Nafiz, Elizabeth McDonough, Poornima Sankar, Lokesh K. Mishra, Ximeng Zhang, Yi Cai, Selvakumar Subbian, and Bibhuti B. Mishra. Pathogenic role for cd101-negative neutrophils in the type i interferon-mediated immunopathogenesis of tuberculosis. Cell Reports, 44:115072, Jan 2025. URL: https://doi.org/10.1016/j.celrep.2024.115072, doi:10.1016/j.celrep.2024.115072. This article has 16 citations and is from a highest quality peer-reviewed journal.

6. (cebani2024canweexploit pages 1-2): Lilitha Cebani and Nontobeko E. Mvubu. Can we exploit inflammasomes for host-directed therapy in the fight against mycobacterium tuberculosis infection? International Journal of Molecular Sciences, 25:8196, Jul 2024. URL: https://doi.org/10.3390/ijms25158196, doi:10.3390/ijms25158196. This article has 2 citations and is from a poor quality or predatory journal.

7. (zhao2024hostdirectedtherapyagainst pages 14-14): Li Zhao, Ke Fan, Xuezhi Sun, Wei Li, Fenfen Qin, Liwen Shi, Feng Gao, and Chunlan Zheng. Host-directed therapy against mycobacterium tuberculosis infections with diabetes mellitus. Frontiers in Immunology, Jan 2024. URL: https://doi.org/10.3389/fimmu.2023.1305325, doi:10.3389/fimmu.2023.1305325. This article has 13 citations and is from a peer-reviewed journal.