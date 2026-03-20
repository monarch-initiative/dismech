---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-02-18T18:26:45.175182'
end_time: '2026-02-18T18:35:28.259325'
duration_seconds: 523.08
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Furunculosis
  mondo_id: ''
  category: Infectious Disease
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 38
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Furunculosis
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Furunculosis**.
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
- **Disease Name:** Furunculosis
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Furunculosis**.
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


Comprehensive Research Report: Pathophysiology of Furunculosis (Infectious Disease)

Publication date: 2026-02-18

1. Key concepts and definitions (current understanding)

Terminology and scope
“Furunculosis” is used in two distinct biomedical contexts:

A. Human furunculosis (recurrent/chronic furunculosis): a deep bacterial infection of the hair follicle leading to a localized abscess (furuncle/boil). In a contemporary SSTI review, furunculosis is described as a deep folliculitis with “localized abscesses in the hypodermis” and tender erythematous nodules with a central pustule, most often caused by Staphylococcus aureus. (linz2023clinicalimpactof pages 3-5)

B. Fish (salmonid) furunculosis: a septicemic disease of fish caused by Aeromonas salmonicida, commonly producing systemic hemorrhage/necrosis and high mortality in aquaculture. (nikiforovnikishin2025dynamicsofpathomorphological pages 1-2, ahmed2025anoverviewon pages 15-17)

Ontology identifiers
No MONDO identifier for “furunculosis” could be confirmed from the retrieved sources alone. The term should be represented as two disease entities in a knowledge base: (i) human S. aureus furunculosis (skin abscess/furuncle) and (ii) fish furunculosis due to A. salmonicida. (nikiforovnikishin2025dynamicsofpathomorphological pages 1-2, linz2023clinicalimpactof pages 3-5)

2. Core pathophysiology (molecular and cellular mechanisms)

2A. Human furunculosis (S. aureus): host–pathogen interaction model

Initial trigger and colonization-to-infection transition
Human recurrent furunculosis is tightly linked to colonization reservoirs. Chronic/recurrent furunculosis is “strongly associated with nasal carriage of S. aureus.” (linz2023clinicalimpactof pages 3-5)
A high-authority 2024 review emphasizes that S. aureus colonization often precedes infection and that non-skin reservoirs (especially nose and intestine) can “seed recurrent infections.” (piewngam2024staphylococcusaureuscolonisation pages 1-3)

Colonization burden and sites (quantitative)
Nasal carriage burden is reported as ~10^2–10^6 CFU/swab (average ~10^4–10^5), while fecal counts are ~10^6–10^7 CFU per 100 g; intestinal burdens may exceed nasal burdens by orders of magnitude. (piewngam2024staphylococcusaureuscolonisation pages 3-4, piewngam2024staphylococcusaureuscolonisation media e0c0446d)
Permanent carriers are ~20% and intermittent carriers ~30%. (piewngam2024staphylococcusaureuscolonisation pages 3-4)

Epithelial barrier engagement and innate sensing
Keratinocytes and neutrophils dominate early responses in S. aureus SSTIs; dendritic cells and T cells contribute later. (linz2023clinicalimpactof pages 1-2)
Innate recognition includes TLR2 and NOD2; NOD2 deletion increased bacterial burden 5–10× and increased NF-κB activity in cited experimental systems, supporting NOD2-mediated antibacterial defense in skin infection. (linz2023clinicalimpactof pages 10-11)

Abscess formation and immune evasion: a “contained infection” strategy
S. aureus uses coagulases (Coa) and vWbp to activate prothrombin and generate fibrin, contributing to “abscess capsule formation” (a fibrin/host-derived barrier that can protect bacteria from immune clearance). (linz2023clinicalimpactof pages 10-11)
Protein A (SpA) supports immune evasion by binding IgG and can act as a B-cell superantigen, hindering effective adaptive responses; SpA also interacts with TNFR1 and alters keratinocyte cytokine responses. (linz2023clinicalimpactof pages 10-11)

Tissue damage and cytotoxicity
Panton–Valentine leukocidin (PVL) is described as a “cytotoxic virulence factor” and is strongly associated with furunculosis pathogenesis; reported PVL positivity in furunculosis is 40–90%. (linz2023clinicalimpactof pages 3-5)
Alpha-hemolysin (Hla) binds ADAM10; ADAM10 cleavage of E-cadherin disrupts epithelial adhesion and migration. Hla also induces keratinocyte necrosis via a Ca2+-dependent calpain pathway and is required for keratinocyte invasion in cited models. (linz2023clinicalimpactof pages 5-7, linz2023clinicalimpactof pages 10-11)

Biofilm-associated persistence and chronicity
Biofilm formation in SSTIs can occur via ica-dependent (PIA) and ica-independent mechanisms involving protein A, fibronectin-binding proteins, autolysin, extracellular DNA, and Bap. (linz2023clinicalimpactof pages 10-11)
Clinical isolates from chronic furunculosis commonly carry adhesins and biofilm/toxin genes, including bap (biofilm-associated protein) and pvl, supporting a mechanistic basis for recurrence/persistence through adhesion, toxin-driven inflammation, and biofilm-associated tolerance. (wcisłek2025phenotypicandgenotypic pages 12-13, wcisłek2025phenotypicandgenotypic pages 15-17)

Inflammatory signaling and cell recruitment
During SSTI progression, early cytokines include IL-6, CXCL1, CCL2/3, G-CSF, GM-CSF, and IL-1β; later IL-17A/F rise, consistent with a Th17-skewed antibacterial response. (linz2023clinicalimpactof pages 10-11)
IL-33 is described as promoting ROS and NETs; basophil-derived IL-4 can suppress IL-17-mediated defenses, suggesting a mechanism for impaired clearance in some host states. (linz2023clinicalimpactof pages 10-11)

Immune dysregulation in chronic disease
A recurrent furunculosis-focused review describes chronic furunculosis as a “complex mechanism based on S. aureus pathogenicity interacting with innate and adaptive immunity.” (nowicka2019staphylococcusaureusand pages 8-9)
It also highlights superantigenic enterotoxins as drivers of broad T-cell activation and downstream exhaustion/anergy, which can promote immune evasion and chronicity. (nowicka2019staphylococcusaureusand pages 8-9)

2B. Fish furunculosis (A. salmonicida): systemic cytotoxic sepsis model

Pathogen determinants and delivery systems
A. salmonicida strains can encode adhesion systems (type IV pili, fimbriae), toxins (aerolysin, hemolysins), and secretion systems such as type II secretion (T2SS); one experimental strain lacking T3SS was hypothesized to rely on T2SS-mediated exotoxin secretion leading to systemic cytotoxic damage. (nikiforovnikishin2025dynamicsofpathomorphological pages 1-2)
Other A. salmonicida virulence determinants highlighted in outbreak-focused genomics include T3SS components (AscC) and effector AexT on plasmid pAsa5; loss of the virulence plasmid can lead to avirulence, emphasizing plasmid-mediated virulence plasticity. (wojnarowski2024genomicanalysisof pages 11-12, wojnarowski2024genomicanalysisof pages 15-15)

Host tissue injury and septicaemia
Fish furunculosis is described as acute or chronic hemorrhagic septicemia with “widespread liquefactive necrosis,” external furuncles/ulcers and internal hemorrhages, with multi-organ pathology (e.g., splenomegaly, hepatic necrosis/hemorrhage, peritonitis, gill epithelial death and lamellar fusion, renal and intestinal epithelial collapse). (ahmed2025anoverviewon pages 15-17)

Staged disease progression with biochemical correlates (experimental)
In an in vivo rainbow trout infection model, the 4-day LD50 was 1.63 × 10^6 CFU/fish. Disease progressed through three stages: early (1–2 days post-infection) with maximal bacterial load and nonspecific immunity activation; acute stage (4 days) with severe septicemia and anemia plus systemic organ damage with peak AST/ALT; and recovery (6 days) with partial inflammation regression but persistent liver/kidney dysfunction. (nikiforovnikishin2025dynamicsofpathomorphological pages 1-2)

3. Key molecular players (genes/proteins, cell types, anatomical locations, chemicals)

3A. Human furunculosis (S. aureus)

Pathogen genes/proteins (examples; mechanisms supported in reviews and isolate studies)
Toxins/cytolysins: PVL (lukS-PV/lukF-PV), α-hemolysin (hla), γ-hemolysin (hlg), δ-hemolysin (hld). (linz2023clinicalimpactof pages 5-7, linz2023clinicalimpactof pages 3-5, wcisłek2025phenotypicandgenotypic pages 15-17)
Immune evasion/abscess architecture: coagulase (coa), von Willebrand factor-binding protein (vWbp), Protein A (spa). (linz2023clinicalimpactof pages 10-11, wcisłek2025phenotypicandgenotypic pages 15-17)
Adhesins: clumping factor B (clfB; binds SREC-1 and cytokeratin 10 in colonization models), fibronectin-binding proteins (fnbA/fnbB), collagen-binding adhesin (cna), extracellular adherence protein (eap). (piewngam2024staphylococcusaureuscolonisation pages 3-4, wcisłek2025phenotypicandgenotypic pages 12-13, wcisłek2025phenotypicandgenotypic pages 15-17)
Biofilm: ica/PIA pathway, Bap (bap), extracellular DNA. (linz2023clinicalimpactof pages 10-11, wcisłek2025phenotypicandgenotypic pages 15-17)
Regulatory: Agr quorum sensing affects colonization (notably intestinal) and virulence phenotypes. (piewngam2024staphylococcusaureuscolonisation pages 3-4)

Host pathways and immune mediators
Pattern recognition: TLR2; NOD2 → NF-κB signaling and antibacterial control. (linz2023clinicalimpactof pages 10-11)
Cytokines/chemokines: IL-1β, IL-6, CXCL1, G-CSF/GM-CSF early; IL-17A/F later. (linz2023clinicalimpactof pages 10-11)
Barrier/adhesion: ADAM10 and E-cadherin cleavage downstream of Hla. (linz2023clinicalimpactof pages 5-7)
Checkpoint/exhaustion concepts and superantigen effects are implicated in chronicity. (nowicka2019staphylococcusaureusand pages 8-9)

Cell types (CL terms; principal participants)
Keratinocytes (CL:0000312): first responders; internalization/proinflammatory signaling to S. aureus. (linz2023clinicalimpactof pages 1-2, linz2023clinicalimpactof pages 10-11)
Neutrophils (CL:0000775): early dominant infiltrate; targeted by PVL and leukotoxins. (linz2023clinicalimpactof pages 1-2, linz2023clinicalimpactof pages 3-5)
Macrophages (CL:0000235), dendritic cells (CL:0000451): later stages and antigen presentation. (linz2023clinicalimpactof pages 1-2, linz2023clinicalimpactof pages 10-11)
T lymphocytes (CL:0000084), including Th17-like responses (functional): later cytokine phases. (linz2023clinicalimpactof pages 10-11)

Anatomical locations (UBERON)
Hair follicle (UBERON:0002076) and hypodermis/subcutis (UBERON:0002193): core lesion site (“localized abscesses in the hypodermis”). (linz2023clinicalimpactof pages 3-5)
Common clinical sites: axilla and groin regions (moist skin colonization sites), gluteal region; nose and intestine are key reservoirs. (linz2023clinicalimpactof pages 3-5, piewngam2024staphylococcusaureuscolonisation pages 1-3, piewngam2024staphylococcusaureuscolonisation pages 4-6)

Relevant chemical entities (CHEBI; examples from prevention/treatment context)
Mupirocin (CHEBI:7025), chlorhexidine (CHEBI:3563), povidone-iodine/iodine (CHEBI:24859): common decolonization agents. (piewngam2024staphylococcusaureuscolonisation pages 6-7, piewngam2024staphylococcusaureuscolonisation pages 7-9, piewngam2024staphylococcusaureuscolonisation media 776be3f3)

3B. Fish furunculosis (A. salmonicida)

Pathogen factors
Toxins: aerolysin, hemolysins; secretion: T2SS (in some strains). (nikiforovnikishin2025dynamicsofpathomorphological pages 1-2)
T3SS machinery and effectors: AscC (pore), AexT (effector) often plasmid-associated; plasmid instability can alter virulence. (wojnarowski2024genomicanalysisof pages 11-12, wojnarowski2024genomicanalysisof pages 15-15)
Outer membrane proteins as immunogens: OmpA, OmpC, OmpF; antigenic variation can occur (e.g., vapA-absent strains impacting diagnostics/vaccination). (wojnarowski2024genomicanalysisof pages 6-11, wojnarowski2024genomicanalysisof pages 11-12, mancilla2025majorantigenicdifferences pages 1-2)

Host tissues
Gills (UBERON:0002535), kidney (UBERON:0002113), liver (UBERON:0002107), spleen (UBERON:0002106), intestine (UBERON:0000160): major target organs with characteristic pathology. (ahmed2025anoverviewon pages 15-17)

4. Biological processes (GO-style annotations; disrupted processes)

Human furunculosis (S. aureus) — candidate GO process mapping grounded in cited mechanisms
Innate immune response / pattern recognition receptor signaling (e.g., “TLR2 and NOD2 … NF-κB activity”). (linz2023clinicalimpactof pages 10-11)
Neutrophil chemotaxis and activation (early neutrophil predominance; CXCL1, G-CSF). (linz2023clinicalimpactof pages 1-2, linz2023clinicalimpactof pages 10-11)
IL-17-mediated signaling and antibacterial defense (later IL-17A/F). (linz2023clinicalimpactof pages 10-11)
Biofilm formation and extracellular matrix adhesion (PIA/ica-dependent and independent biofilm; fnbA/B; bap). (linz2023clinicalimpactof pages 10-11, wcisłek2025phenotypicandgenotypic pages 15-17)
Host cell–cell adhesion maintenance/disruption (Hla→ADAM10→E-cadherin cleavage). (linz2023clinicalimpactof pages 5-7)

Fish furunculosis (A. salmonicida)
Response to bacterium and systemic inflammatory response (nonspecific immunity activation early; septicemia). (nikiforovnikishin2025dynamicsofpathomorphological pages 1-2)
Cytolysis/toxin-mediated tissue injury (exotoxin-driven cytotoxic damage). (nikiforovnikishin2025dynamicsofpathomorphological pages 1-2)
Antigen processing and presentation / adaptive activation following vaccination (see Section 5 for vaccine-induced gene upregulation). (xiu2024evaluationofimmune pages 8-10)

5. Cellular components (where key processes occur)

Human
Extracellular space and bacterial surface: adhesins (ClfB/Fnb) binding host receptors and matrix; coagulase activity driving fibrin deposition around abscesses. (linz2023clinicalimpactof pages 10-11, piewngam2024staphylococcusaureuscolonisation pages 3-4)
Plasma membrane: Hla interaction with ADAM10; disruption of E-cadherin junctions. (linz2023clinicalimpactof pages 5-7)
Biofilm matrix: extracellular DNA, polysaccharides (PIA), and biofilm proteins (Bap). (linz2023clinicalimpactof pages 10-11, wcisłek2025phenotypicandgenotypic pages 15-17)

Fish
Secreted toxin compartment: T2SS-mediated exotoxin export (for strains lacking T3SS). (nikiforovnikishin2025dynamicsofpathomorphological pages 1-2)
Plasmid-encoded secretion systems: T3SS apparatus/effectors (AscC/AexT) associated with pAsa5. (wojnarowski2024genomicanalysisof pages 11-12)

6. Disease progression (sequence of events)

6A. Human furunculosis (S. aureus)

A practical mechanistic sequence consistent with current reviews:
Reservoir colonization (nose ± intestine ± moist skin sites such as axilla/groin) with measurable CFU burdens and carrier states. (piewngam2024staphylococcusaureuscolonisation pages 3-4, piewngam2024staphylococcusaureuscolonisation pages 1-3, piewngam2024staphylococcusaureuscolonisation pages 4-6)
Breach/follicular invasion leading to deep folliculitis and hypodermal abscess formation (furuncle). (linz2023clinicalimpactof pages 3-5)
Early innate response dominated by keratinocytes and neutrophils, with PRR signaling (TLR2/NOD2) and strong IL-1β/IL-6/CXCL1/G-CSF induction. (linz2023clinicalimpactof pages 1-2, linz2023clinicalimpactof pages 10-11)
Bacterial immune evasion and lesion maturation through toxins (PVL/Hla), abscess encapsulation (Coa/vWbp), and biofilm formation; later involvement of macrophages/dendritic cells/T cells and IL-17A/F responses. (linz2023clinicalimpactof pages 10-11, linz2023clinicalimpactof pages 3-5)
Recurrence/chronicity promoted by persistent colonization (re-seeding from reservoirs), biofilm-associated tolerance, and immune dysregulation (e.g., superantigen-driven T-cell exhaustion/anergy). (nowicka2019staphylococcusaureusand pages 8-9, piewngam2024staphylococcusaureuscolonisation pages 1-3, linz2023clinicalimpactof pages 10-11)

6B. Fish furunculosis (A. salmonicida)

Experimental staging data:
Early stage (1–2 DPI): maximal bacterial load; nonspecific immunity activation. (nikiforovnikishin2025dynamicsofpathomorphological pages 1-2)
Acute stage (4 DPI): severe septicemia and anemia; systemic organ damage with AST/ALT peaks. (nikiforovnikishin2025dynamicsofpathomorphological pages 1-2)
Recovery stage (6 DPI): partial regression of inflammation but persistent liver/kidney dysfunction. (nikiforovnikishin2025dynamicsofpathomorphological pages 1-2)

7. Phenotypic manifestations (clinical phenotypes and mechanistic links)

7A. Human phenotypes (HP-style; examples)
Furuncle/boil phenotype: tender erythematous nodule with central pustule; mechanistically linked to follicular invasion, neutrophilic inflammation, toxin-driven necrosis, and fibrin-encapsulated abscess formation. (linz2023clinicalimpactof pages 3-5, linz2023clinicalimpactof pages 10-11)
Recurrent boils and outbreaks: associated with PVL-positive S. aureus strains and colonization reservoirs. (linz2023clinicalimpactof pages 3-5, piewngam2024staphylococcusaureuscolonisation pages 1-3)
Carbuncle (coalescing furuncles) with deeper extension and possible sinus tracts; increased frequency in immunodeficiency contexts (e.g., hypogammaglobulinemia, chronic granulomatous disease). (linz2023clinicalimpactof pages 3-5)

7B. Fish phenotypes
External furuncles/ulcers and internal hemorrhages with septicemia; multi-organ necrosis and anemia (acute stage). (nikiforovnikishin2025dynamicsofpathomorphological pages 1-2, ahmed2025anoverviewon pages 15-17)

8. Recent developments (prioritizing 2023–2024) and authoritative expert analysis

8A. Human (2023–2024)

Updated epidemiology and burden (2023)
A 2023 review reports that recurrent SSTIs affect ~16–19% of healthy adults. (linz2023clinicalimpactof pages 1-2)
Hospitalization trends: MRSA SSTI hospitalizations declined from 3.8 to 3.0 per 1000 by 2014 and from 1.72 per 1000 (2016) to 1.32 per 1000 (2019) in U.S. datasets summarized in the review. (linz2023clinicalimpactof pages 1-2)
Global burden estimates summarized include >1,105,000 deaths attributed to S. aureus in 2019 and >100,000 deaths to MRSA in 2019; SSTI age-standardized mortality rate is given as 0.5. (linz2023clinicalimpactof pages 16-17, linz2023clinicalimpactof pages 2-3)

Contemporary mechanistic synthesis (2023)
Mechanistic pathways emphasized in 2023 include Hla–ADAM10–E-cadherin disruption, NOD2/NF-κB control of bacterial burden, and a time-phased cytokine program shifting toward IL-17A/F responses. (linz2023clinicalimpactof pages 5-7, linz2023clinicalimpactof pages 10-11)

Expert review perspective on colonization and prevention (2024)
A Lancet Microbe 2024 review underscores that “most infections arise from asymptomatic colonization,” positioning decolonization as a primary prevention lever, while noting controversial effectiveness, increasing resistance, and recolonization from extranasal reservoirs. (piewngam2024staphylococcusaureuscolonisation pages 1-3, piewngam2024staphylococcusaureuscolonisation pages 6-7)
The same review summarizes that ~80% of infectious isolates match colonizing strains, reinforcing the colonization→infection paradigm central to recurrent furunculosis. (piewngam2024staphylococcusaureuscolonisation pages 4-6)
Emerging, less microbiome-disruptive approaches include bacteriocin-producing commensals and probiotic strategies; in one cited trial, oral Bacillus subtilis spores eliminated “>95% of bodily S. aureus” without altering gut microbiota. (piewngam2024staphylococcusaureuscolonisation pages 9-11)

8B. Fish/aquaculture (2024)

Genomics-enabled outbreak management and vaccine strategy
A 2024 Pathogens study used nanopore WGS of 54 A. salmonicida isolates and concluded outbreaks likely represent a “single epidemiological unit,” and that “major immunogenic proteins … are highly conservative,” supporting consensus-isolate autogenous vaccine design; it also warns of plasmid-driven plasticity. (wojnarowski2024genomicanalysisof pages 12-13, wojnarowski2024genomicanalysisof pages 1-2)

Vaccination immunology and efficacy metrics
A 2024 Fishes study of a bivalent inactivated vaccine (A. salmonicida + V. vulnificus; Montanide ISA 763 AVG) reported RPS ~77% and measured upregulation of TLR5, MHCI, MHCII, and CD4 in kidney, alongside increased lysozyme and acid phosphatase activities and elevated antibody titers. (xiu2024evaluationofimmune pages 8-10, xiu2024evaluationofimmune pages 6-8)

9. Current applications and real-world implementations

Human healthcare
Decolonization protocols: mupirocin (typically 5-day intranasal course) plus skin antiseptics (chlorhexidine/povidone-iodine) are standard tools but limited by recolonization (often by 3 months), incomplete extranasal clearance, and resistance concerns. (piewngam2024staphylococcusaureuscolonisation pages 6-7, piewngam2024staphylococcusaureuscolonisation pages 7-9)
Program-level strategies: large trials summarized in 2024 include CLEAR (post-discharge decolonization + hygiene reduced MRSA infection by 30% over one year) and REDUCE-MRSA (universal decolonization reducing MRSA cultures more than targeted approaches, with mixed results for bloodstream infections). (piewngam2024staphylococcusaureuscolonisation pages 7-9)

Aquaculture
Routine vaccination and adjuvanted inactivated vaccines are implemented for furunculosis prevention, with measurable survival benefits (e.g., RPS ~77% in turbot vaccine study). (xiu2024evaluationofimmune pages 8-10)
Operational genomics: nanopore WGS is proposed as a practical field-forward method to rapidly characterize outbreak isolates and justify autogenous vaccines across multiple facilities under regulatory scrutiny. (wojnarowski2024genomicanalysisof pages 1-2)

10. Evidence items (with publication dates, URLs)

Human furunculosis/S. aureus
Linz MS et al. “Clinical Impact of Staphylococcus aureus Skin and Soft Tissue Infections.” Antibiotics. 2023-03. DOI:10.3390/antibiotics12030557 https://doi.org/10.3390/antibiotics12030557 (linz2023clinicalimpactof pages 1-2, linz2023clinicalimpactof pages 10-11, linz2023clinicalimpactof pages 3-5)
Piewngam P, Otto M. “Staphylococcus aureus colonisation and strategies for decolonisation.” The Lancet Microbe. 2024-06. DOI:10.1016/S2666-5247(24)00040-5 https://doi.org/10.1016/S2666-5247(24)00040-5 (piewngam2024staphylococcusaureuscolonisation pages 1-3, piewngam2024staphylococcusaureuscolonisation pages 6-7, piewngam2024staphylococcusaureuscolonisation pages 7-9)
Nowicka D, Grywalska E. “Staphylococcus aureus and Host Immunity in Recurrent Furunculosis.” Dermatology. 2019-04. DOI:10.1159/000499184 https://doi.org/10.1159/000499184 (nowicka2019staphylococcusaureusand pages 2-4, nowicka2019staphylococcusaureusand pages 8-9)

Fish furunculosis/A. salmonicida
Xiu Y et al. “Evaluation of Immune Protection of a Bivalent Inactivated Vaccine against Aeromonas salmonicida and Vibrio vulnificus in Turbot.” Fishes. 2024-04. DOI:10.3390/fishes9040131 https://doi.org/10.3390/fishes9040131 (xiu2024evaluationofimmune pages 8-10, xiu2024evaluationofimmune pages 6-8)
Wojnarowski K et al. “Genomic Analysis of Aeromonas salmonicida ssp. salmonicida Isolates…” Pathogens. 2024-10. DOI:10.3390/pathogens13100908 https://doi.org/10.3390/pathogens13100908 (wojnarowski2024genomicanalysisof pages 12-13, wojnarowski2024genomicanalysisof pages 11-12, wojnarowski2024genomicanalysisof pages 1-2)

11. Limitations relative to the requested PMID-centric output
The retrieved evidence set contains high-quality reviews and recent aquaculture studies but does not provide PMIDs in the extracted text snippets, and several key mechanistic primary studies are referenced only indirectly within those reviews. Therefore, mechanistic claims are supported here by DOI-cited sources; additional PMID-level extraction would require retrieving and parsing the underlying primary studies cited within these reviews.

Image evidence
S. aureus colonization burden/sites schematic and decolonization intervention figure(s) from Piewngam & Otto (Lancet Microbe 2024) are available as cropped figures. (piewngam2024staphylococcusaureuscolonisation media e0c0446d, piewngam2024staphylococcusaureuscolonisation media 776be3f3)

References

1. (linz2023clinicalimpactof pages 3-5): Matthew S. Linz, Arun Mattappallil, Diana Finkel, and Dane Parker. Clinical impact of staphylococcus aureus skin and soft tissue infections. Antibiotics, 12:557, Mar 2023. URL: https://doi.org/10.3390/antibiotics12030557, doi:10.3390/antibiotics12030557. This article has 274 citations.

2. (nikiforovnikishin2025dynamicsofpathomorphological pages 1-2): Dmitry Nikiforov-Nikishin, Nikita Kochetkov, Kirill Gavrilin, Viktoria Gaffarova, Kirill Medvedev, Svetlana Smorodinskaya, Anastasia Klimuk, Yuri Kuchikhin, Ivan Svinarev, Natalya Gladysh, Anna Kudryavtseva, Egor Shitikov, and Alexei Nikiforov-Nikishin. Dynamics of pathomorphological and pathophysiological alterations in rainbow trout (oncorhynchus mykiss) during acute aeromonas salmonicida infection. Biology, 14:1330, Sep 2025. URL: https://doi.org/10.3390/biology14101330, doi:10.3390/biology14101330. This article has 1 citations.

3. (ahmed2025anoverviewon pages 15-17): Imtiaz Ahmed, Shagufta Ishtiyaq, and Shabihul Fatma Sayed. An overview on understanding the major bacterial fish diseases in freshwater salmonids. Frontiers in Aquaculture, Mar 2025. URL: https://doi.org/10.3389/faquc.2025.1515831, doi:10.3389/faquc.2025.1515831. This article has 8 citations.

4. (piewngam2024staphylococcusaureuscolonisation pages 1-3): Pipat Piewngam and Michael Otto. Staphylococcus aureus colonisation and strategies for decolonisation. The Lancet Microbe, 5:e606-e618, Jun 2024. URL: https://doi.org/10.1016/s2666-5247(24)00040-5, doi:10.1016/s2666-5247(24)00040-5. This article has 143 citations.

5. (piewngam2024staphylococcusaureuscolonisation pages 3-4): Pipat Piewngam and Michael Otto. Staphylococcus aureus colonisation and strategies for decolonisation. The Lancet Microbe, 5:e606-e618, Jun 2024. URL: https://doi.org/10.1016/s2666-5247(24)00040-5, doi:10.1016/s2666-5247(24)00040-5. This article has 143 citations.

6. (piewngam2024staphylococcusaureuscolonisation media e0c0446d): Pipat Piewngam and Michael Otto. Staphylococcus aureus colonisation and strategies for decolonisation. The Lancet Microbe, 5:e606-e618, Jun 2024. URL: https://doi.org/10.1016/s2666-5247(24)00040-5, doi:10.1016/s2666-5247(24)00040-5. This article has 143 citations.

7. (linz2023clinicalimpactof pages 1-2): Matthew S. Linz, Arun Mattappallil, Diana Finkel, and Dane Parker. Clinical impact of staphylococcus aureus skin and soft tissue infections. Antibiotics, 12:557, Mar 2023. URL: https://doi.org/10.3390/antibiotics12030557, doi:10.3390/antibiotics12030557. This article has 274 citations.

8. (linz2023clinicalimpactof pages 10-11): Matthew S. Linz, Arun Mattappallil, Diana Finkel, and Dane Parker. Clinical impact of staphylococcus aureus skin and soft tissue infections. Antibiotics, 12:557, Mar 2023. URL: https://doi.org/10.3390/antibiotics12030557, doi:10.3390/antibiotics12030557. This article has 274 citations.

9. (linz2023clinicalimpactof pages 5-7): Matthew S. Linz, Arun Mattappallil, Diana Finkel, and Dane Parker. Clinical impact of staphylococcus aureus skin and soft tissue infections. Antibiotics, 12:557, Mar 2023. URL: https://doi.org/10.3390/antibiotics12030557, doi:10.3390/antibiotics12030557. This article has 274 citations.

10. (wcisłek2025phenotypicandgenotypic pages 12-13): Aleksandra Wcisłek, Joanna Jursa-Kulesza, Helena Masiuk, Bartłomiej Grygorcewicz, Beata Hukowska-Szematowicz, Piotr Prowans, Paweł Ziętek, and Danuta Kosik-Bogacka. Phenotypic and genotypic characterization of staphylococcus aureus isolated from patients with chronic furunculosis and osteomyelitis from northwestern poland. Pathogens, 14:923, Sep 2025. URL: https://doi.org/10.3390/pathogens14090923, doi:10.3390/pathogens14090923. This article has 0 citations.

11. (wcisłek2025phenotypicandgenotypic pages 15-17): Aleksandra Wcisłek, Joanna Jursa-Kulesza, Helena Masiuk, Bartłomiej Grygorcewicz, Beata Hukowska-Szematowicz, Piotr Prowans, Paweł Ziętek, and Danuta Kosik-Bogacka. Phenotypic and genotypic characterization of staphylococcus aureus isolated from patients with chronic furunculosis and osteomyelitis from northwestern poland. Pathogens, 14:923, Sep 2025. URL: https://doi.org/10.3390/pathogens14090923, doi:10.3390/pathogens14090923. This article has 0 citations.

12. (nowicka2019staphylococcusaureusand pages 8-9): Danuta Nowicka and Ewelina Grywalska. Staphylococcus aureus and host immunity in recurrent furunculosis. Dermatology, 235:295-305, Apr 2019. URL: https://doi.org/10.1159/000499184, doi:10.1159/000499184. This article has 64 citations and is from a peer-reviewed journal.

13. (wojnarowski2024genomicanalysisof pages 11-12): Konrad Wojnarowski, Paulina Cholewińska, Peter Steinbauer, Tobias Lautwein, Wanvisa Hussein, Lisa-Marie Streb, and Dušan Palić. Genomic analysis of aeromonas salmonicida ssp. salmonicida isolates collected during multiple clinical outbreaks supports association with a single epidemiological unit. Pathogens, 13:908, Oct 2024. URL: https://doi.org/10.3390/pathogens13100908, doi:10.3390/pathogens13100908. This article has 4 citations.

14. (wojnarowski2024genomicanalysisof pages 15-15): Konrad Wojnarowski, Paulina Cholewińska, Peter Steinbauer, Tobias Lautwein, Wanvisa Hussein, Lisa-Marie Streb, and Dušan Palić. Genomic analysis of aeromonas salmonicida ssp. salmonicida isolates collected during multiple clinical outbreaks supports association with a single epidemiological unit. Pathogens, 13:908, Oct 2024. URL: https://doi.org/10.3390/pathogens13100908, doi:10.3390/pathogens13100908. This article has 4 citations.

15. (piewngam2024staphylococcusaureuscolonisation pages 4-6): Pipat Piewngam and Michael Otto. Staphylococcus aureus colonisation and strategies for decolonisation. The Lancet Microbe, 5:e606-e618, Jun 2024. URL: https://doi.org/10.1016/s2666-5247(24)00040-5, doi:10.1016/s2666-5247(24)00040-5. This article has 143 citations.

16. (piewngam2024staphylococcusaureuscolonisation pages 6-7): Pipat Piewngam and Michael Otto. Staphylococcus aureus colonisation and strategies for decolonisation. The Lancet Microbe, 5:e606-e618, Jun 2024. URL: https://doi.org/10.1016/s2666-5247(24)00040-5, doi:10.1016/s2666-5247(24)00040-5. This article has 143 citations.

17. (piewngam2024staphylococcusaureuscolonisation pages 7-9): Pipat Piewngam and Michael Otto. Staphylococcus aureus colonisation and strategies for decolonisation. The Lancet Microbe, 5:e606-e618, Jun 2024. URL: https://doi.org/10.1016/s2666-5247(24)00040-5, doi:10.1016/s2666-5247(24)00040-5. This article has 143 citations.

18. (piewngam2024staphylococcusaureuscolonisation media 776be3f3): Pipat Piewngam and Michael Otto. Staphylococcus aureus colonisation and strategies for decolonisation. The Lancet Microbe, 5:e606-e618, Jun 2024. URL: https://doi.org/10.1016/s2666-5247(24)00040-5, doi:10.1016/s2666-5247(24)00040-5. This article has 143 citations.

19. (wojnarowski2024genomicanalysisof pages 6-11): Konrad Wojnarowski, Paulina Cholewińska, Peter Steinbauer, Tobias Lautwein, Wanvisa Hussein, Lisa-Marie Streb, and Dušan Palić. Genomic analysis of aeromonas salmonicida ssp. salmonicida isolates collected during multiple clinical outbreaks supports association with a single epidemiological unit. Pathogens, 13:908, Oct 2024. URL: https://doi.org/10.3390/pathogens13100908, doi:10.3390/pathogens13100908. This article has 4 citations.

20. (mancilla2025majorantigenicdifferences pages 1-2): Marcos Mancilla, Adriana Ojeda, Yassef Yuivar, Maritza Grandón, Horst Grothusen, Marcela Oyarzún, Alejandro Bisquertt, Juan A. Ugalde, Francisco Fuentes, Pablo Ibarra, and Patricio Bustos. Major antigenic differences in aeromonas salmonicida isolates correlate with the emergence of a new strain causing furunculosis in chilean salmon farms. Frontiers in Cellular and Infection Microbiology, Feb 2025. URL: https://doi.org/10.3389/fcimb.2025.1508135, doi:10.3389/fcimb.2025.1508135. This article has 1 citations.

21. (xiu2024evaluationofimmune pages 8-10): Yunji Xiu, Jingyuan Yi, Ruixin Feng, Jiaxue Song, Yunfei Pang, Peng Liu, and Shun Zhou. Evaluation of immune protection of a bivalent inactivated vaccine against aeromonas salmonicida and vibrio vulnificus in turbot. Fishes, 9:131, Apr 2024. URL: https://doi.org/10.3390/fishes9040131, doi:10.3390/fishes9040131. This article has 5 citations.

22. (linz2023clinicalimpactof pages 16-17): Matthew S. Linz, Arun Mattappallil, Diana Finkel, and Dane Parker. Clinical impact of staphylococcus aureus skin and soft tissue infections. Antibiotics, 12:557, Mar 2023. URL: https://doi.org/10.3390/antibiotics12030557, doi:10.3390/antibiotics12030557. This article has 274 citations.

23. (linz2023clinicalimpactof pages 2-3): Matthew S. Linz, Arun Mattappallil, Diana Finkel, and Dane Parker. Clinical impact of staphylococcus aureus skin and soft tissue infections. Antibiotics, 12:557, Mar 2023. URL: https://doi.org/10.3390/antibiotics12030557, doi:10.3390/antibiotics12030557. This article has 274 citations.

24. (piewngam2024staphylococcusaureuscolonisation pages 9-11): Pipat Piewngam and Michael Otto. Staphylococcus aureus colonisation and strategies for decolonisation. The Lancet Microbe, 5:e606-e618, Jun 2024. URL: https://doi.org/10.1016/s2666-5247(24)00040-5, doi:10.1016/s2666-5247(24)00040-5. This article has 143 citations.

25. (wojnarowski2024genomicanalysisof pages 12-13): Konrad Wojnarowski, Paulina Cholewińska, Peter Steinbauer, Tobias Lautwein, Wanvisa Hussein, Lisa-Marie Streb, and Dušan Palić. Genomic analysis of aeromonas salmonicida ssp. salmonicida isolates collected during multiple clinical outbreaks supports association with a single epidemiological unit. Pathogens, 13:908, Oct 2024. URL: https://doi.org/10.3390/pathogens13100908, doi:10.3390/pathogens13100908. This article has 4 citations.

26. (wojnarowski2024genomicanalysisof pages 1-2): Konrad Wojnarowski, Paulina Cholewińska, Peter Steinbauer, Tobias Lautwein, Wanvisa Hussein, Lisa-Marie Streb, and Dušan Palić. Genomic analysis of aeromonas salmonicida ssp. salmonicida isolates collected during multiple clinical outbreaks supports association with a single epidemiological unit. Pathogens, 13:908, Oct 2024. URL: https://doi.org/10.3390/pathogens13100908, doi:10.3390/pathogens13100908. This article has 4 citations.

27. (xiu2024evaluationofimmune pages 6-8): Yunji Xiu, Jingyuan Yi, Ruixin Feng, Jiaxue Song, Yunfei Pang, Peng Liu, and Shun Zhou. Evaluation of immune protection of a bivalent inactivated vaccine against aeromonas salmonicida and vibrio vulnificus in turbot. Fishes, 9:131, Apr 2024. URL: https://doi.org/10.3390/fishes9040131, doi:10.3390/fishes9040131. This article has 5 citations.

28. (nowicka2019staphylococcusaureusand pages 2-4): Danuta Nowicka and Ewelina Grywalska. Staphylococcus aureus and host immunity in recurrent furunculosis. Dermatology, 235:295-305, Apr 2019. URL: https://doi.org/10.1159/000499184, doi:10.1159/000499184. This article has 64 citations and is from a peer-reviewed journal.