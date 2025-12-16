---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-15T09:26:29.820429'
end_time: '2025-12-15T09:34:12.783296'
duration_seconds: 462.96
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Kawasaki Disease
  mondo_id: ''
  category: Pediatric Condition
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 21
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Kawasaki Disease
- **MONDO ID:**  (if available)
- **Category:** Pediatric Condition

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Kawasaki Disease**.
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
- **Disease Name:** Kawasaki Disease
- **MONDO ID:**  (if available)
- **Category:** Pediatric Condition

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Kawasaki Disease**.
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


# Disease Pathophysiology Research Template

## Target Disease
- Disease Name: Kawasaki Disease (KD)
- MONDO ID: not confirmed in this report
- Category: Pediatric Condition

## Pathophysiology description (current understanding)
Kawasaki disease is an acute, self-limited, systemic vasculitis of medium-sized arteries with a predilection for the coronary arteries, driven by a genetically primed, dysregulated innate and adaptive immune response to one or more infectious/environmental triggers that culminates in endothelial activation/dysfunction and layered coronary-artery wall inflammation and remodeling (necrotizing arteritis, subacute/chronic vasculitis, luminal myofibroblast proliferation) (burns2024theetiologiesof pages 4-5, paolini2024endothelialdysfunctionmolecular pages 2-4, paolini2024endothelialdysfunctionmolecular pages 4-5, philip2023anupdateon pages 4-6). Recent reviews emphasize heterogeneous etiologies with epidemiologic signals for a respiratory-transmitted trigger and convergent, antigen-driven plasmablast responses in some patients, while genetic susceptibility (e.g., ITPKC, FCGR, HLA, CD40, BLK; Ca2+/NFAT, FcγR, and TGF-β pathway variants) shapes endotypes and clinical risk (burns2024theetiologiesof pages 4-5, paolini2024endothelialdysfunctionmolecular pages 2-4, vankova2023pathophysiologicalandclinical pages 13-17). Endothelial dysfunction is central: proinflammatory cytokines (IL‑1β, TNF‑α, IL‑6, IL‑17) induce adhesion molecules (ICAM‑1/VCAM‑1), oxidative stress, reduced NO bioavailability, and endothelin‑1 signaling, promoting leukocyte recruitment, thrombosis, and arterial stiffness; endothelial-to-mesenchymal transition and TGF‑β-mediated remodeling contribute to aneurysm/stenosis (paolini2024endothelialdysfunctionmolecular pages 4-5, paolini2024endothelialdysfunctionmolecular pages 5-7). Immune-complex deposition with FcγR-driven myeloid activation, complement fixation, platelet aggregation, and neutrophil degranulation likely participate in coronary arteritis; coronary lesions contain monocytes/macrophages, dendritic cells, neutrophils, CD8+ T cells, and IgA plasma cells (philip2023anupdateon pages 4-6). Emerging work highlights gut barrier dysfunction and dysbiosis as upstream modulators of systemic inflammation in KD, with putative links to Th17 skewing and treatment resistance, although causality requires further study (vankova2023pathophysiologicalandclinical pages 13-17).

## 1. Core Pathophysiology
- Primary mechanisms: genetically primed innate/adaptive hyperinflammation to infectious/environmental antigens; endothelial activation/dysfunction; immune complex–mediated vasculitis; cytokine cascades (IL‑1, TNF, IL‑6, IL‑17) driving vascular injury; maladaptive wound repair with EndMT and myofibroblast proliferation (burns2024theetiologiesof pages 4-5, paolini2024endothelialdysfunctionmolecular pages 4-5, philip2023anupdateon pages 4-6, paolini2024endothelialdysfunctionmolecular pages 5-7, paolini2024endothelialdysfunctionmolecular pages 2-4).
- Dysregulated molecular pathways: IL‑1 and NLRP3 inflammasome; TNF‑α/NF‑κB; Th17/IL‑17–IL‑23; Ca2+/calcineurin–NFAT (ITPKC, ORAI1, STIM1); FcγR signaling in IC handling; TGF‑β signaling in vascular remodeling (paolini2024endothelialdysfunctionmolecular pages 4-5, philip2023anupdateon pages 4-6, paolini2024endothelialdysfunctionmolecular pages 2-4, burns2024theetiologiesof pages 4-5, vankova2023pathophysiologicalandclinical pages 13-17).
- Affected cellular processes: endothelial activation (adhesion, permeability, NO imbalance), leukocyte adhesion/transmigration, neutrophil activation/degranulation and probable NET formation, monocyte/macrophage cytokine production and inflammasome activation, T‑cell activation and Th17/Treg imbalance, B‑cell/plasmablast responses including IgA and anti-endothelial antibodies, complement activation, platelet activation/thrombosis (paolini2024endothelialdysfunctionmolecular pages 4-5, philip2023anupdateon pages 4-6, paolini2024endothelialdysfunctionmolecular pages 2-4, vankova2023pathophysiologicalandclinical pages 13-17).

## 2. Key Molecular Players
- Genes/Proteins and pathways: see the artifact mapping principal genes to pathways and mechanisms.
| HGNC symbol | Protein/Gene name | Pathway/process (GO) | Mechanistic role in KD | Therapeutic implications | Evidence (DOI/URL, year) |
|---|---|---|---|---|---|
| ITPKC | Inositol 1,4,5-trisphosphate 3-kinase C | Ca2+ signaling / NFAT regulation | Risk variants reduce negative regulation of Ca2+/NFAT → enhanced T‑cell activation and hyperinflammation linked to coronary lesions | Rationale for calcineurin inhibitors (e.g., cyclosporine) or other modulators of Ca2+/NFAT signaling | https://doi.org/10.3390/ijms252413322 (2024); https://doi.org/10.1172/jci176938 (2024) (paolini2024endothelialdysfunctionmolecular pages 2-4, burns2024theetiologiesof pages 4-5) |
| FCGR2A / FCGR3A | Fc gamma receptors IIa / IIIa | FcγR signaling / immune complex handling | Mediate immune‑complex driven neutrophil/monocyte activation and Fc‑dependent inflammation; genetic association with susceptibility | Mechanistic basis for IVIG competing at FcγRs; informs IVIG resistance research and Fc‑targeted strategies | https://doi.org/10.3390/ijms252413322 (2024); https://doi.org/10.1111/1756-185x.14816 (2023) (paolini2024endothelialdysfunctionmolecular pages 2-4, philip2023anupdateon pages 4-6) |
| BLK | B lymphoid tyrosine kinase | B‑cell receptor signaling | Genetic locus implicated in altered B‑cell/plasmablast responses and antibody production | Suggests B‑cell–directed approaches may be relevant for specific endotypes (research use) | https://doi.org/10.1172/jci176938 (2024) (burns2024theetiologiesof pages 4-5) |
| CD40 | CD40 molecule | CD40–CD40L co‑stimulation | Promotes B/T cell and endothelial activation; CD40L on T cells linked to EC activation and inflammation | Anti‑CD40/CD40L approaches are experimental; informs rationale for therapies that dampen T–B co‑stimulation | https://doi.org/10.3390/ijms252413322 (2024); https://doi.org/10.1172/jci176938 (2024) (paolini2024endothelialdysfunctionmolecular pages 2-4, burns2024theetiologiesof pages 4-5) |
| HLA‑B | Major histocompatibility complex, class I, B | Antigen presentation / adaptive immune response | HLA associations support antigen‑driven or superantigen‑like T‑cell responses shaping disease susceptibility | Useful for dissecting trigger(s) and host response subtypes; not directly therapeutic | https://doi.org/10.1172/jci176938 (2024) (burns2024theetiologiesof pages 4-5) |
| CASP3 | Caspase‑3 | Apoptotic execution / programmed cell death | Implicated via genetics and pathology in EC/apoptosis and vascular remodeling during acute vasculitis | Apoptosis modulation is investigational; informs mechanisms of vessel wall injury | https://doi.org/10.1016/j.pedneo.2023.05.002 (2023); https://doi.org/10.3390/ijms252413322 (2024) (vankova2023pathophysiologicalandclinical pages 13-17, paolini2024endothelialdysfunctionmolecular pages 2-4) |
| ORAI1 / STIM1 | ORAI1 / STIM1 (SOCE components) | Store‑operated Ca2+ entry / T‑cell activation | Variants alter SOCE → dysregulated Ca2+ signaling and heightened T‑cell responses contributing to hyperinflammation | Points to SOCE or downstream calcineurin/NFAT modulation (e.g., cyclosporine) as therapeutic options | https://doi.org/10.1172/jci176938 (2024); https://doi.org/10.1016/j.pedneo.2023.05.002 (2023) (burns2024theetiologiesof pages 4-5, vankova2023pathophysiologicalandclinical pages 13-17) |
| TGFBR2 / SMAD3 / TGFB2 | TGF‑β receptor / signaling mediators | TGF‑β signaling / endothelial‑to‑mesenchymal transition (EndMT) | Drive EndMT, luminal myofibroblast proliferation and chronic vascular remodeling (stenosis/aneurysm formation) | Anti‑fibrotic or TGF‑β pathway modulation is theoretical; informs long‑term vascular remodeling targets | https://doi.org/10.3390/ijms252413322 (2024) (paolini2024endothelialdysfunctionmolecular pages 4-5, paolini2024endothelialdysfunctionmolecular pages 5-7) |
| IL1B / IL1R1 | Interleukin‑1β / receptor | IL‑1 signaling; downstream of inflammasome (GO: inflammasome activation) | IL‑1β promotes endothelial injury, inflammation and remodeling; NLRP3 inflammasome contributes to IL‑1 activation | Direct IL‑1 blockade (anakinra) has mechanistic and clinical rationale for IVIG‑resistant KD | https://doi.org/10.3390/ijms252413322 (2024); https://doi.org/10.1111/1756-185x.14816 (2023) (paolini2024endothelialdysfunctionmolecular pages 5-7, philip2023anupdateon pages 4-6) |
| TNF (TNF) | Tumor necrosis factor alpha | TNF signaling / NF‑κB activation | Induces EC expression of ICAM‑1/VCAM‑1, iNOS and proinflammatory cascade → endothelial dysfunction and thrombosis | Anti‑TNF therapy (infliximab) used for IVIG‑resistant cases to reduce TNF‑driven EC activation | https://doi.org/10.3390/ijms252413322 (2024); https://doi.org/10.3389/fped.2024.1415941 (2024) (paolini2024endothelialdysfunctionmolecular pages 4-5, yi2024researchperspectivein pages 2-3) |
| IL17A / IL23A | Interleukin‑17A / IL‑23A | Th17 axis / IL‑17 signaling | Th17 expansion and elevated IL‑17 associate with coronary damage and IVIG resistance; promotes neutrophil recruitment | IL‑17/IL‑23 pathway inhibitors are a potential investigational approach in select patients | https://doi.org/10.3390/ijms252413322 (2024); https://doi.org/10.1016/j.pedneo.2023.05.002 (2023) (paolini2024endothelialdysfunctionmolecular pages 4-5, vankova2023pathophysiologicalandclinical pages 13-17) |
| NLRP3 | NLRP3 inflammasome | Inflammasome activation / IL‑1β maturation | NLRP3 activation → IL‑1β release, pyroptosis and amplified vascular inflammation | NLRP3 or IL‑1 pathway inhibition offers a mechanistic target (supports use of anakinra) | https://doi.org/10.3390/ijms252413322 (2024); https://doi.org/10.1111/1756-185x.14816 (2023) (paolini2024endothelialdysfunctionmolecular pages 4-5, philip2023anupdateon pages 4-6) |
| NOS3 | Nitric oxide synthase 3 (eNOS) | NO biosynthesis / endothelial homeostasis | Reduced eNOS expression/activity → decreased NO, vasoconstriction, thrombosis and endothelial dysfunction in KD with CAA | Supports vascular‑protective strategies and monitoring of endothelial function | https://doi.org/10.3390/ijms252413322 (2024) (paolini2024endothelialdysfunctionmolecular pages 4-5) |
| ICAM1 / VCAM1 | Intercellular adhesion molecule 1 / Vascular cell adhesion molecule 1 | Endothelial activation / leukocyte adhesion | Upregulated by TNF/IL‑1 leading to leukocyte recruitment, endothelial dysfunction and vascular injury | Adhesion‑inflammation axis is a biomarker and potential target for anti‑inflammatory interventions | https://doi.org/10.3390/ijms252413322 (2024) (paolini2024endothelialdysfunctionmolecular pages 4-5) |


*Table: Table mapping principal genes/proteins to pathways, mechanistic roles in Kawasaki disease, therapeutic implications, and source DOIs (2023–2024); useful for ontology annotation and evidence‑based knowledgebase curation.*
- Chemical entities (examples): acetylsalicylic acid (aspirin) for antiplatelet/anti-inflammatory effects; intravenous immunoglobulin (IVIG) competing at FcγRs and modulating immune pathways; infliximab (anti‑TNF) to blunt TNF‑driven endothelial activation; anakinra (IL‑1 receptor antagonist) to inhibit IL‑1–mediated endothelial injury; corticosteroids to broadly suppress cytokine networks; cyclosporine to inhibit calcineurin–NFAT signaling in genetically susceptible endotypes; nitric oxide bioavailability and endothelin‑1 as endothelial tone mediators (paolini2024endothelialdysfunctionmolecular pages 5-7, yi2024researchperspectivein pages 2-3, paolini2024endothelialdysfunctionmolecular pages 4-5, paolini2024endothelialdysfunctionmolecular pages 2-4).
- Cell types: vascular endothelial cells; neutrophils; monocytes/macrophages and dendritic cells; CD8+ T cells; Th17 and regulatory T cells; B cells/plasmablasts including IgA plasma cells (philip2023anupdateon pages 4-6, paolini2024endothelialdysfunctionmolecular pages 2-4, vankova2023pathophysiologicalandclinical pages 13-17, burns2024theetiologiesof pages 4-5).
- Anatomical locations: coronary artery wall (intima, media, adventitia), vasa vasorum, bronchial epithelium (candidate antigen reservoirs), intestinal barrier/gut mucosa; myocardium and other medium/small arteries may be involved (philip2023anupdateon pages 4-6, burns2024theetiologiesof pages 4-5, vankova2023pathophysiologicalandclinical pages 13-17, paolini2024endothelialdysfunctionmolecular pages 2-4).

## 3. Biological Processes (candidate GO annotations)
- Inflammatory response; cytokine production (IL‑1, TNF, IL‑6, IL‑17); NF‑κB signaling; NLRP3 inflammasome activation and pyroptosis; leukocyte adhesion to endothelium; endothelial cell activation and permeability; neutrophil degranulation and extracellular trap formation; complement activation; platelet activation; antigen processing/presentation; store‑operated Ca2+ entry and calcineurin–NFAT signaling; endothelial-to-mesenchymal transition and extracellular matrix organization (paolini2024endothelialdysfunctionmolecular pages 4-5, philip2023anupdateon pages 4-6, paolini2024endothelialdysfunctionmolecular pages 2-4, vankova2023pathophysiologicalandclinical pages 13-17).

## 4. Cellular Components (where processes occur)
- Endothelial cell plasma membrane/junctions (ICAM‑1/VCAM‑1, VE‑cadherin), caveolae; mitochondria (apoptosis/oxidative stress); inflammasome complex (cytosolic); extracellular space (immune complexes, complement, cytokines, microparticles); platelet granules; vascular wall layers (intima/media/adventitia) and vasa vasorum (paolini2024endothelialdysfunctionmolecular pages 4-5, philip2023anupdateon pages 4-6, paolini2024endothelialdysfunctionmolecular pages 2-4).

## 5. Disease Progression
- Sequence of events: trigger exposure in genetically susceptible host → innate sensing and myeloid activation (monocytes/neutrophils), cytokine surge and endothelial activation → immune complex deposition and complement fixation in coronary microvessels and vasa vasorum with leukocyte recruitment → histologic phases: necrotizing arteritis in the first 1–2 weeks, followed by subacute/chronic vasculitis and luminal myofibroblast proliferation leading to coronary aneurysm or stenosis → chronic endothelial dysfunction and arterial stiffness in some patients (philip2023anupdateon pages 4-6, paolini2024endothelialdysfunctionmolecular pages 2-4, paolini2024endothelialdysfunctionmolecular pages 4-5).
- Phases: acute febrile vasculitis; subacute/chronic vasculitis; chronic remodeling (EndMT/myofibroblast proliferation) (philip2023anupdateon pages 4-6, paolini2024endothelialdysfunctionmolecular pages 2-4, paolini2024endothelialdysfunctionmolecular pages 4-5).

## 6. Phenotypic Manifestations and Outcomes
- Key clinical phenotypes: persistent fever, conjunctival injection, polymorphous rash, oral mucosal changes (strawberry tongue, fissured lips), extremity changes (erythema/edema), cervical lymphadenopathy; laboratory: elevated CRP/ESR, leukocytosis, thrombocytosis; cardiovascular: coronary artery dilatation/aneurysm, myocarditis; incomplete KD remains at risk for coronary involvement (yi2024researchperspectivein pages 2-3, alzamzami2024etiologypathophysiologydiagnosis pages 1-2).
- Relation to mechanisms: cytokine-driven endothelial activation explains mucocutaneous inflammation and vascular leak; TNF/IL‑1 induce adhesion molecules and NO imbalance; immune complexes and complement contribute to coronary arteritis; Th17 skewing associates with coronary damage and possible IVIG resistance; TGF‑β–mediated EndMT underlies chronic remodeling (paolini2024endothelialdysfunctionmolecular pages 4-5, philip2023anupdateon pages 4-6, paolini2024endothelialdysfunctionmolecular pages 2-4).
- Coronary outcomes and IVIG: first-line IVIG (2 g/kg) within the first 10 days is recommended to reduce coronary complications; guidelines emphasize timely IVIG to prevent aneurysm, and contemporary European initiatives are testing early corticosteroid adjuncts to lower CAA rates in unselected patients (yi2024researchperspectivein pages 2-3, burns2024theetiologiesof pages 4-5).

## Current applications and real-world implementations
- Standard of care: prompt IVIG plus aspirin, echocardiographic monitoring; risk stratification for IVIG resistance and coronary risk guides adjunctive therapy in some centers (yi2024researchperspectivein pages 2-3, alzamzami2024etiologypathophysiologydiagnosis pages 1-2).
- Adjunct/second-line therapies: corticosteroids for high-risk or IVIG-resistant cases; anti‑TNF (infliximab) for persistent inflammation; IL‑1 blockade (anakinra) in IVIG-resistant patients with mechanistic evidence of IL‑1–driven endothelial injury; calcineurin inhibitors (cyclosporine) for Ca2+/NFAT‑driven endotypes; ongoing trials are evaluating up‑front steroid addition to reduce CAA (paolini2024endothelialdysfunctionmolecular pages 5-7, yi2024researchperspectivein pages 2-3, paolini2024endothelialdysfunctionmolecular pages 2-4).

## Expert opinions and analyses
- Burns (JCI, 2024) argues for heterogeneous etiologies with epidemiologic evidence of respiratory transmission and convergent plasmablast responses in a subset, highlighting the need to define triggers for precision diagnostics/therapeutics (burns2024theetiologiesof pages 4-5). Vaňková et al. (2023) synthesize overlaps and distinctions between KD and MIS‑C, noting shared IL‑1/Th17 axes and genetic susceptibility in Ca2+ signaling, supporting targeted immunomodulation in selected phenotypes (vankova2023pathophysiologicalandclinical pages 13-17). Paolini et al. (2024) present endothelial dysfunction as the central, targetable hub linking cytokines, oxidative stress, adhesion, NO/ET‑1 imbalance, and EndMT to long-term vascular sequelae (paolini2024endothelialdysfunctionmolecular pages 2-4, paolini2024endothelialdysfunctionmolecular pages 4-5, paolini2024endothelialdysfunctionmolecular pages 5-7). Philip et al. (2023) re‑elevate immune complex–mediated vasculitis as a plausible driver of coronary lesions with supportive patient and model data (philip2023anupdateon pages 4-6).

## Relevant statistics and data (recent)
- IVIG timing: guidelines emphasize administration within 10 days of fever onset to prevent coronary artery aneurysm; late treatment and IVIG non‑response are associated with increased coronary risk (burns2024theetiologiesof pages 4-5). 
- Genetic evidence: FCGR2A p.His166 is associated with KD susceptibility but does not robustly predict IVIG resistance or aneurysm across cohorts in meta‑analysis, indicating limited utility for risk prediction at this locus (philip2023anupdateon pages 4-6).
- Endothelial dysfunction biomarkers: elevated circulating endothelial cells, endothelial microparticles, and asymmetric dimethylarginine, with impaired endothelial function particularly in patients with aneurysms, underscore persistent vascular risk (paolini2024endothelialdysfunctionmolecular pages 5-7, paolini2024endothelialdysfunctionmolecular pages 4-5).

## Ontology-oriented annotations
- Genes/Proteins (HGNC): ITPKC; FCGR2A/FCGR3A; BLK; CD40; HLA‑B; CASP3; ORAI1; STIM1; TGFBR2; SMAD3; TGFB2; IL1B; IL1R1; TNF; IL17A; IL23A; NLRP3; NOS3; ICAM1; VCAM1 (see artifact for roles and citations) (paolini2024endothelialdysfunctionmolecular pages 2-4, paolini2024endothelialdysfunctionmolecular pages 4-5, philip2023anupdateon pages 4-6, burns2024theetiologiesof pages 4-5, vankova2023pathophysiologicalandclinical pages 13-17).
- Biological Processes (GO): inflammatory response; IL‑1/TNF/IL‑17 signaling; NF‑κB activation; NLRP3 inflammasome activation; leukocyte adhesion/transendothelial migration; endothelial activation/permeability; neutrophil degranulation and extracellular trap formation; complement activation; platelet activation; antigen processing/presentation; store‑operated Ca2+ entry and calcineurin–NFAT signaling; endothelial‑to‑mesenchymal transition (paolini2024endothelialdysfunctionmolecular pages 4-5, philip2023anupdateon pages 4-6, paolini2024endothelialdysfunctionmolecular pages 2-4, vankova2023pathophysiologicalandclinical pages 13-17).
- Cellular Components (GO): plasma membrane (endothelial junctional complexes); inflammasome complex; mitochondrion; extracellular space/exosomes; platelet granules (paolini2024endothelialdysfunctionmolecular pages 4-5, philip2023anupdateon pages 4-6, paolini2024endothelialdysfunctionmolecular pages 2-4).
- Cell types (CL): vascular endothelial cell; neutrophil; monocyte/macrophage; dendritic cell; CD8+ T cell; Th17 cell; regulatory T cell; plasmablast/plasma cell (philip2023anupdateon pages 4-6, paolini2024endothelialdysfunctionmolecular pages 2-4, vankova2023pathophysiologicalandclinical pages 13-17).
- Anatomical Locations (UBERON): coronary artery; tunica intima/media/adventitia; vasa vasorum; bronchial epithelium; intestinal mucosal barrier; myocardium (philip2023anupdateon pages 4-6, burns2024theetiologiesof pages 4-5, vankova2023pathophysiologicalandclinical pages 13-17, paolini2024endothelialdysfunctionmolecular pages 2-4).
- Phenotype associations (HP): fever; conjunctival injection; polymorphous exanthem; strawberry tongue; cervical lymphadenopathy; extremity erythema/edema; thrombocytosis; coronary artery dilatation/aneurysm; myocarditis (yi2024researchperspectivein pages 2-3, alzamzami2024etiologypathophysiologydiagnosis pages 1-2).
- Chemical entities (CHEBI, examples): acetylsalicylic acid (aspirin); nitric oxide; asymmetric dimethylarginine; endothelin‑1 (paolini2024endothelialdysfunctionmolecular pages 4-5, paolini2024endothelialdysfunctionmolecular pages 5-7).

## Evidence items
- Burns JC. The etiologies of Kawasaki disease. J Clin Invest. 2024-03. DOI:10.1172/jci176938. URL: https://doi.org/10.1172/jci176938 (burns2024theetiologiesof pages 4-5).
- Paolini L, et al. Endothelial dysfunction: molecular mechanisms and therapeutic strategies in Kawasaki disease. Int J Mol Sci. 2024-12. DOI:10.3390/ijms252413322. URL: https://doi.org/10.3390/ijms252413322 (paolini2024endothelialdysfunctionmolecular pages 2-4, paolini2024endothelialdysfunctionmolecular pages 4-5, paolini2024endothelialdysfunctionmolecular pages 5-7).
- Philip S, et al. An update on understanding the pathophysiology in Kawasaki disease: role of immune complexes revisited. Int J Rheum Dis. 2023-07. DOI:10.1111/1756-185x.14816. URL: https://doi.org/10.1111/1756-185x.14816 (philip2023anupdateon pages 4-6).
- Vaňková L, et al. Pathophysiological and clinical point of view on Kawasaki disease and MIS‑C. Pediatrics & Neonatology. 2023-09. DOI:10.1016/j.pedneo.2023.05.002. URL: https://doi.org/10.1016/j.pedneo.2023.05.002 (vankova2023pathophysiologicalandclinical pages 13-17).
- Yi X, et al. Research perspective in the clinical management of Kawasaki disease. Front Pediatr. 2024-07. DOI:10.3389/fped.2024.1415941. URL: https://doi.org/10.3389/fped.2024.1415941 (yi2024researchperspectivein pages 2-3).
- Alzamzami A, et al. Etiology, pathophysiology, diagnosis and management of Kawasaki disease. J Healthc Sci. 2024-01. DOI:10.52533/johs.2024.40109. URL: https://doi.org/10.52533/johs.2024.40109 (alzamzami2024etiologypathophysiologydiagnosis pages 1-2).
- Uittenbogaard P, et al. FCGR2/3 polymorphisms and KD susceptibility; lack of prediction for IVIG resistance/CAA. Front Immunol. 2024-09. DOI:10.3389/fimmu.2024.1323171. URL: https://doi.org/10.3389/fimmu.2024.1323171 (philip2023anupdateon pages 4-6).

Notes on open questions
- A single KD trigger remains unproven; evidence suggests heterogeneous etiologies and host-response endotypes that may benefit from tailored immunomodulation (burns2024theetiologiesof pages 4-5). Better integration of endothelial biology with gut–immune axes and precise genetic risk mapping may enable endotype-specific therapies (paolini2024endothelialdysfunctionmolecular pages 2-4, vankova2023pathophysiologicalandclinical pages 13-17).


References

1. (burns2024theetiologiesof pages 4-5): Jane C. Burns. The etiologies of kawasaki disease. The Journal of Clinical Investigation, Mar 2024. URL: https://doi.org/10.1172/jci176938, doi:10.1172/jci176938. This article has 54 citations.

2. (paolini2024endothelialdysfunctionmolecular pages 2-4): Lucia Paolini, Fiorentina Guida, Antonino Calvaruso, Laura Andreozzi, Luca Pierantoni, Marcello Lanari, and Marianna Fabi. Endothelial dysfunction: molecular mechanisms and therapeutic strategies in kawasaki disease. International Journal of Molecular Sciences, 25:13322, Dec 2024. URL: https://doi.org/10.3390/ijms252413322, doi:10.3390/ijms252413322. This article has 3 citations and is from a poor quality or predatory journal.

3. (paolini2024endothelialdysfunctionmolecular pages 4-5): Lucia Paolini, Fiorentina Guida, Antonino Calvaruso, Laura Andreozzi, Luca Pierantoni, Marcello Lanari, and Marianna Fabi. Endothelial dysfunction: molecular mechanisms and therapeutic strategies in kawasaki disease. International Journal of Molecular Sciences, 25:13322, Dec 2024. URL: https://doi.org/10.3390/ijms252413322, doi:10.3390/ijms252413322. This article has 3 citations and is from a poor quality or predatory journal.

4. (philip2023anupdateon pages 4-6): Saji Philip, Ankur Jindal, and Raman Krishna Kumar. An update on understanding the pathophysiology in kawasaki disease: possible role of immune complexes in coronary artery lesion revisited. International Journal of Rheumatic Diseases, 26:1453-1463, Jul 2023. URL: https://doi.org/10.1111/1756-185x.14816, doi:10.1111/1756-185x.14816. This article has 16 citations and is from a peer-reviewed journal.

5. (vankova2023pathophysiologicalandclinical pages 13-17): Lenka Vaňková, Jiří Bufka, and Věra Křížková. Pathophysiological and clinical point of view on kawasaki disease and mis-c. Pediatrics &amp; Neonatology, 64:495-504, Sep 2023. URL: https://doi.org/10.1016/j.pedneo.2023.05.002, doi:10.1016/j.pedneo.2023.05.002. This article has 14 citations and is from a peer-reviewed journal.

6. (paolini2024endothelialdysfunctionmolecular pages 5-7): Lucia Paolini, Fiorentina Guida, Antonino Calvaruso, Laura Andreozzi, Luca Pierantoni, Marcello Lanari, and Marianna Fabi. Endothelial dysfunction: molecular mechanisms and therapeutic strategies in kawasaki disease. International Journal of Molecular Sciences, 25:13322, Dec 2024. URL: https://doi.org/10.3390/ijms252413322, doi:10.3390/ijms252413322. This article has 3 citations and is from a poor quality or predatory journal.

7. (yi2024researchperspectivein pages 2-3): Xiong-xiong Yi, Wen-rong Zhang, Dong-mei Wang, Xiu-ping Wang, and Fen-xia Zhang. Research perspective in the clinical management of kawasaki disease. Frontiers in Pediatrics, Jul 2024. URL: https://doi.org/10.3389/fped.2024.1415941, doi:10.3389/fped.2024.1415941. This article has 6 citations and is from a poor quality or predatory journal.

8. (alzamzami2024etiologypathophysiologydiagnosis pages 1-2): Abdulghani Alzamzami, Osama Almuqaytib, Ahmad Alsaadi, Ahmed Alasmari, Khalid Alsuwat, Ahmed Al Abdullah, Abdulaziz Alomair, Asalah Alomair, Noor Alawami, Anas Alamodi, Abdullah Alismail, and Bandar Alenezi. Etiology, pathophysiology, diagnosis and management of kawasaki disease. JOURNAL OF HEALTHCARE SCIENCES, 04:71-76, Jan 2024. URL: https://doi.org/10.52533/johs.2024.40109, doi:10.52533/johs.2024.40109. This article has 0 citations.