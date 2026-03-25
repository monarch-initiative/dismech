---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-01-20T14:03:12.216370'
end_time: '2026-01-20T14:07:47.683659'
duration_seconds: 275.47
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Shigellosis
  mondo_id: ''
  category: Infectious
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 22
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Shigellosis
- **MONDO ID:**  (if available)
- **Category:** Infectious

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Shigellosis**.
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
- **Disease Name:** Shigellosis
- **MONDO ID:**  (if available)
- **Category:** Infectious

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Shigellosis**.
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


Disease Pathophysiology Research Template

Target Disease
- Disease Name: Shigellosis
- MONDO ID: 
- Category: Infectious

Pathophysiology description
Shigellosis is caused by Shigella spp., which are enteric Gram-negative bacteria that reach and invade the colonic mucosa after surviving gastric acidity and crossing the follicle-associated epithelium via M cells. Subepithelial macrophages phagocytose Shigella; the pathogen’s plasmid-encoded type III secretion system (T3SS) delivers effectors (e.g., IpaB, IpaC, IpaD) that induce macrophage cell death and basolateral release, enabling invasion of adjacent intestinal epithelial cells (IECs). Within IECs, Shigella uses T3SS effectors to remodel the cytoskeleton and subvert immune signaling, escapes into the cytosol, replicates, and spreads laterally via actin-based motility driven by the polar adhesin IcsA/VirG and regulated by IcsP, causing epithelial fenestration and mucosal ulceration. Neutrophil recruitment, driven by IL-1β/IL-18 and IL-8, further disrupts barrier integrity, exacerbating diarrhea and dysentery. Innate inflammasome pathways (NAIP/NLRC4 and NLRP3) and non-canonical caspase-4/5 sensing of cytosolic LPS trigger gasdermin D–dependent pore formation and pyroptosis; Shigella both activates and antagonizes these pathways (e.g., via IpaH family) to modulate inflammation and survival in host cells. Recent clinical and translational studies underscore persistent stool cytokine elevation in children, rising antimicrobial resistance, and progress in vaccines and host-directed strategies. (hendrick2025shigellosis pages 8-9, hendrick2025shigellosis pages 17-18, lu2024shigellavaccinesthe pages 4-5, worley2023immuneevasionand pages 31-32, odonovan2023identificationofhost pages 43-47)

1) Core Pathophysiology
- Primary mechanisms
  - T3SS-mediated invasion and vacuolar escape: The mxi-spa T3SS uses IpaB/IpaC to form a translocon pore and inject effectors; IpaC activates small GTPases and actin nucleation for uptake; IpaB also contributes to vacuolar membrane disruption and caspase-1 activation in phagocytes. “IpaB and IpaC assemble a funnel-shaped pore in target membranes through which the injectisome docks to deliver effectors,” and “IpaB mediates phagosomal membrane insertion and escape.” (DOI:10.17863/cam.102175, Oct 2023; URL: https://doi.org/10.17863/cam.102175) (odonovan2023identificationofhost pages 43-47). Reviews and recent clinical syntheses concur that Shigella’s virulence plasmid-encoded T3SS controls invasion, signaling, and host cell death. (DOI:10.1016/S0140-6736(25)01033-5, Oct 2025; URL: https://doi.org/10.1016/s0140-6736(25)01033-5) (hendrick2025shigellosis pages 8-9, hendrick2025shigellosis pages 17-18)
  - Cytoskeletal remodeling and cell uptake: Shigella triggers membrane ruffling and macropinocytosis through IpaC and other effectors (e.g., IpgB1/2 as Rho GEF mimics; IpgD altering phosphoinositides), facilitating entry into IECs. (DOI:10.3390/ijms25084329, Apr 2024; URL: https://doi.org/10.3390/ijms25084329) (lu2024shigellavaccinesthe pages 18-20); (DOI:10.1080/19490976.2022.2163839, Jan 2023; URL: https://doi.org/10.1080/19490976.2022.2163839) (worley2023immuneevasionand pages 31-32)
  - Intracellular replication and actin-based spread: IcsA/VirG recruits N-WASP and Arp2/3 to drive actin comet tails, pushing Shigella into adjacent cells. IcsP controls IcsA surface distribution; IcsB aids autophagy evasion. (DOI:10.17918/00010587, 2024; URL: https://doi.org/10.17918/00010587) (reghunathan2024towardsinvitroreconstitution pages 26-32); (DOI:10.3390/ijms25084329, Apr 2024; URL: https://doi.org/10.3390/ijms25084329) (lu2024shigellavaccinesthe pages 18-20)
  - Epithelial barrier disruption and neutrophil influx: Macrophage caspase-1 activation and IL-1β/IL-18 release, plus epithelial chemokines (e.g., IL‑8), recruit neutrophils that transmigrate and damage tight junctions, amplifying mucosal injury. Clinical syntheses report high stool cytokines and prolonged inflammation, particularly in children. (DOI:10.1016/S0140-6736(25)01033-5, Oct 2025; URL: https://doi.org/10.1016/s0140-6736(25)01033-5) (hendrick2025shigellosis pages 8-9, hendrick2025shigellosis pages 17-18)
  - Inflammasome sensing and evasion: Cytosolic detection of T3SS components by NAIP/NLRC4 and damage signals that engage NLRP3 leads to caspase-1 activation; non-canonical caspase-4/5 senses cytosolic LPS. Gasdermin D cleavage mediates pore formation, cytokine release, and pyroptosis. Shigella effectors (e.g., IpaH7.8) modulate inflammasome signaling to favor survival or dissemination. “Cytosolic detection of T3SS components (MxiH/MxiI) activates NAIP/NLRC4… IpaB can directly activate caspase-1… inflammatory caspases cleave gasdermin D to form membrane pores.” (DOI:10.17863/cam.102175, Oct 2023; URL: https://doi.org/10.17863/cam.102175) (odonovan2023identificationofhost pages 43-47)

- Molecular pathways dysregulated
  - Actin dynamics and Rho GTPase signaling (IpaC, IpgB1/2; host N-WASP/WASL, Arp2/3). (reghunathan2024towardsinvitroreconstitution pages 26-32, lu2024shigellavaccinesthe pages 18-20)
  - Innate immune signaling and inflammasomes (NAIP/NLRC4, NLRP3; caspase-1, caspase‑4/5; gasdermin D). (odonovan2023identificationofhost pages 43-47, hendrick2025shigellosis pages 8-9)
  - Epithelial junction and barrier integrity pathways (tight junction disruption during neutrophil transmigration/inflammation). (hendrick2025shigellosis pages 8-9, hendrick2025shigellosis pages 17-18)

- Cellular processes affected
  - Phagocyte pyroptosis and cytokine release; IEC invasion, vacuole escape, cytosolic replication; actin-based motility; neutrophil chemotaxis/transmigration; autophagy evasion. (odonovan2023identificationofhost pages 43-47, hendrick2025shigellosis pages 8-9, reghunathan2024towardsinvitroreconstitution pages 26-32)

2) Key Molecular Players
- Genes/Proteins (bacterial and host)
  - Bacterial T3SS and effectors: IpaB, IpaC, IpaD (tip/translocon/invasion); IpgB1/IpgB2 (Rho GEF mimics); IpgD (phosphoinositide phosphatase); OspF/OspG (immune modulation); IpaH family (E3 ligases; includes IpaH7.8); IcsA/VirG (actin motility), IcsP (IcsA protease), IcsB (autophagy evasion). Evidence: invasion pore and effector delivery (odonovan2023identificationofhost pages 43-47); immune modulation and actin spread (lu2024shigellavaccinesthe pages 18-20, reghunathan2024towardsinvitroreconstitution pages 26-32, worley2023immuneevasionand pages 31-32).
  - Host factors: NAIP/NLRC4 and NLRP3 inflammasomes; caspase‑1, caspase‑4/5; Gasdermin D (GSDMD); N-WASP/WASL; Arp2/3; PI3K/Akt signaling (IpgD-induced); epithelial chemokines (IL‑8). Evidence: inflammasome detection of T3SS and GSDMD pore formation (odonovan2023identificationofhost pages 43-47); PI3K/Akt and IpgD (worley2023immuneevasionand pages 31-32); epithelial cytokines and inflammation (hendrick2025shigellosis pages 8-9, hendrick2025shigellosis pages 17-18).

- Chemical Entities
  - Lipopolysaccharide (LPS; non-canonical inflammasome ligand in cytosol). (odonovan2023identificationofhost pages 43-47)
  - Antibiotics/therapeutics mentioned in recent syntheses: azithromycin, ciprofloxacin; adjunctive butyrate; bacteriophage therapy under early testing. (hendrick2025shigellosis pages 17-18, lu2024shigellavaccinesthe pages 4-5)

- Cell Types (CL terms)
  - Intestinal epithelial cells (CL:0002669); macrophages (CL:0000235); neutrophils (CL:0000775). (hendrick2025shigellosis pages 8-9, hendrick2025shigellosis pages 17-18)

- Anatomical Locations (UBERON terms)
  - Colon (UBERON:0001155); Peyer’s patch/follicle-associated epithelium (UBERON:0001259); lamina propria (UBERON:0001231). (hendrick2025shigellosis pages 8-9)

3) Biological Processes (GO annotation)
- GO:0030257 type III protein secretion system; GO:0030041 actin filament polymerization; GO:0006909 phagocytosis; GO:0043312 neutrophil degranulation/GO:0030593 chemotaxis; GO:0070269 pyroptosis; GO:0061702 inflammasome complex; GO:0070830 tight junction assembly; GO:0009626 inflammatory response to bacterium. Supported by mechanistic descriptions of T3SS invasion, actin-based motility, neutrophil recruitment, inflammasome activation, and epithelial barrier disruption. (odonovan2023identificationofhost pages 43-47, reghunathan2024towardsinvitroreconstitution pages 26-32, hendrick2025shigellosis pages 8-9, hendrick2025shigellosis pages 17-18)

4) Cellular Components
- Bacterial injectisome and translocon at host plasma membrane (T3SS pore; IpaB/IpaC). (odonovan2023identificationofhost pages 43-47)
- Host cytosol (Shigella replication; actin comet tails); plasma membrane (GSDMD pores); tight junctions/adherens junctions of IECs. (reghunathan2024towardsinvitroreconstitution pages 26-32, odonovan2023identificationofhost pages 43-47, hendrick2025shigellosis pages 8-9)

5) Disease Progression
- Sequence of events
  1) Ingestion → acid survival → targeting follicle-associated epithelium. 2) Transcytosis via M cells; uptake by macrophages. 3) T3SS activation: IpaB/IpaC translocon, effector injection; macrophage pyroptosis with basolateral release. 4) IEC invasion, vacuole escape, cytosolic replication. 5) Actin-based cell-to-cell spread via IcsA, widening foci of infection. 6) Neutrophil influx (IL‑1β/IL‑18, IL‑8) and barrier breakdown → watery diarrhea/ dysentery; persistent mucosal inflammation in children. (hendrick2025shigellosis pages 8-9, hendrick2025shigellosis pages 17-18, odonovan2023identificationofhost pages 43-47, reghunathan2024towardsinvitroreconstitution pages 26-32)
- Stages/phases: initial watery diarrhea (enterotoxins, early inflammation) → invasive colitis with blood/mucus (epithelial damage, neutrophils) → convalescence with prolonged cytokine elevation in some patients. (hendrick2025shigellosis pages 8-9, hendrick2025shigellosis pages 17-18)

6) Phenotypic Manifestations (HP terms)
- HP:0002014 Diarrhea; HP:0002239 Abdominal pain; HP:0001945 Dehydration; HP:0001873 Bloody stool (dysentery). Mechanistic links include epithelial invasion, cytokine-driven neutrophil transmigration, and mucosal injury. (hendrick2025shigellosis pages 8-9, hendrick2025shigellosis pages 17-18)

Recent developments and latest research (2023–2024 focus)
- Mechanistic updates using modern models: Genome-wide CRISPR screens in human macrophage-like cells identified TLR1/2, interferon/TNF signaling, and metabolic pathways required for Shigella-induced cell death, and detailed T3SS sensing by NAIP/NLRC4, NLRP3, and non-canonical caspase‑4/5, with GSDMD as the executioner of pyroptosis. (DOI:10.17863/cam.102175, Oct 2023; URL: https://doi.org/10.17863/cam.102175) (odonovan2023identificationofhost pages 43-47)
- Contemporary synthesis of immune evasion: Shigella IpaD/IpgD manipulate phagocyte apoptosis and host PI3K/Akt, respectively, contributing to persistence and immune evasion in the gut; reviews integrate models relevant to pediatric disease and nutrition (e.g., zinc deficiency). (DOI:10.1080/19490976.2022.2163839, Jan 2023; URL: https://doi.org/10.1080/19490976.2022.2163839) (worley2023immuneevasionand pages 31-32)
- Clinical immunopathology and host-directed therapy: High stool cytokines and prolonged inflammation in children; butyrate-induced antimicrobial peptide upregulation and early-phase bacteriophage therapy discussed as adjunctive strategies; emphasis on culture with susceptibility testing given AMR. (DOI:10.1016/S0140-6736(25)01033-5, Oct 2025; URL: https://doi.org/10.1016/s0140-6736(25)01033-5) (hendrick2025shigellosis pages 17-18)
- Vaccine antigens and correlates: Up-to-date review highlights T3SS tip and translocator proteins (IpaD, IpaB) and LPS O-antigen targets; pediatric conjugate candidates and thresholds for serum anti-LPS IgG associated with protection. (DOI:10.3390/ijms25084329, Apr 2024; URL: https://doi.org/10.3390/ijms25084329) (lu2024shigellavaccinesthe pages 18-20)

Current applications and real-world implementations
- Diagnostics and susceptibility testing: Culture with AST remains essential in light of rising resistance; ipaH is a molecular diagnostic marker. (DOI:10.1016/S0140-6736(25)01033-5, Oct 2025; URL: https://doi.org/10.1016/s0140-6736(25)01033-5) (hendrick2025shigellosis pages 8-9); (mason2025thegenomicepidemiology pages 219-222)
- Therapeutics: Empiric therapy increasingly constrained by AMR; adjunctive host-directed approaches (e.g., butyrate) and phage products are being explored. (hendrick2025shigellosis pages 17-18)
- Vaccines: Multiple platforms in clinical and preclinical evaluation, including synthetic carbohydrate conjugates and protein subunits targeting IpaD/IpaB and LPS O-antigen; immunologic thresholds for protection are being refined. (lu2024shigellavaccinesthe pages 18-20)

Expert opinions and analysis
- Authoritative syntheses emphasize that Shigella pathogenesis hinges on T3SS-dependent manipulation of host signaling and cell death and that actin-based motility is central to mucosal spread and ulceration; inflammatory cascades in children can persist beyond clinical resolution. These insights support prioritizing vaccine antigens that intercept invasion (T3SS proteins) and spread (IcsA) and underscore the need for robust AMR surveillance guiding therapy. (hendrick2025shigellosis pages 8-9, hendrick2025shigellosis pages 17-18, lu2024shigellavaccinesthe pages 18-20)

Relevant statistics and data (recent sources)
- Burden and inflammation: “Stool cytokines are markedly elevated and inflammation can persist >1 month, especially in children,” highlighting the clinical impact of mucosal immunopathology. (DOI:10.1016/S0140-6736(25)01033-5, Oct 2025; URL: https://doi.org/10.1016/s0140-6736(25)01033-5) (hendrick2025shigellosis pages 8-9)
- Antimicrobial resistance: US reports estimate approximately 77,000 antibiotic-resistant Shigella infections, with azithromycin resistance reaching 20% in New York (2013–2015), prompting calls for AST-guided therapy and vaccine acceleration. (DOI:10.3390/ijms25084329, Apr 2024; URL: https://doi.org/10.3390/ijms25084329) (lu2024shigellavaccinesthe pages 4-5)

Gene/protein annotations with ontology terms
- Host (HGNC):
  - NLRC4 (HGNC:16401): NAIP/NLRC4 inflammasome sensor mediating caspase‑1 activation in response to T3SS/flagellin. GO:0061702 inflammasome complex; GO:0006954 inflammatory response. Evidence: detection of T3SS components and inflammasome activation during Shigella infection. (odonovan2023identificationofhost pages 43-47)
  - NLRP3 (HGNC:16400): danger-sensing inflammasome engaged during infection. GO:0061702; GO:0070269 pyroptosis. (odonovan2023identificationofhost pages 43-47)
  - CASP4 (HGNC:1504) and CASP5 (HGNC:1506): non-canonical inflammasome caspases sensing cytosolic LPS; execute GSDMD cleavage. GO:0006915 apoptotic process; GO:0070269 pyroptosis. (odonovan2023identificationofhost pages 43-47)
  - CASP1 (HGNC:1503): canonical inflammasome protease releasing IL‑1β/IL‑18 and cleaving GSDMD. GO:0035871 IL‑1β secretion; GO:0070269. (odonovan2023identificationofhost pages 43-47)
  - GSDMD (HGNC:25505): pore-forming executioner of pyroptosis. GO:0140714 pore-forming activity; GO:0070269. (odonovan2023identificationofhost pages 43-47)
  - WASL/N‑WASP (HGNC:12733): actin nucleation-promoting factor recruited by IcsA to drive comet tails. GO:0034314 Arp2/3-mediated actin nucleation. (reghunathan2024towardsinvitroreconstitution pages 26-32)

- Bacterial (functional categories; non-HGNC):
  - IpaB/IpaC/IpaD (T3SS translocon/tip); IpgB1/IpgB2/IpgD; OspF/OspG; IpaH family (incl. IpaH7.8); IcsA (VirG)/IcsP/IcsB. GO processes mapped by function: GO:0030257 T3SS; GO:0030041 actin polymerization; GO:0006955 immune response modulation. (odonovan2023identificationofhost pages 43-47, lu2024shigellavaccinesthe pages 18-20, reghunathan2024towardsinvitroreconstitution pages 26-32, worley2023immuneevasionand pages 31-32)

Phenotype associations (HP terms)
- HP:0002014 Diarrhea; HP:0001873 Hematochezia (bloody stool); HP:0002019 Abdominal cramping; HP:0001945 Dehydration—linked to epithelial barrier failure and neutrophilic inflammation. (hendrick2025shigellosis pages 8-9, hendrick2025shigellosis pages 17-18)

Cell type involvement (CL terms)
- CL:0002669 Intestinal epithelial cell; CL:0000235 Macrophage; CL:0000775 Neutrophil—primary host cells mediating invasion, pyroptosis, and tissue damage. (hendrick2025shigellosis pages 8-9, hendrick2025shigellosis pages 17-18)

Anatomical locations (UBERON terms)
- UBERON:0001155 Colon; UBERON:0001259 Peyer’s patch/follicle-associated epithelium; UBERON:0001231 Lamina propria—key niches for invasion and inflammation. (hendrick2025shigellosis pages 8-9)

Chemical entities (CHEBI terms)
- CHEBI:16412 Lipopolysaccharide (LPS)—ligand of non-canonical inflammasome; antibiotics discussed (azithromycin, ciprofloxacin; CHEBI names). (odonovan2023identificationofhost pages 43-47, lu2024shigellavaccinesthe pages 4-5)

Evidence items with PMIDs/DOIs/URLs and dates
- Hendrick et al., “Shigellosis,” The Lancet, Oct 2025. DOI:10.1016/S0140-6736(25)01033-5; URL: https://doi.org/10.1016/s0140-6736(25)01033-5. Key mechanisms; clinical immunopathology; adjunct therapies; diagnostic guidance. (hendrick2025shigellosis pages 8-9, hendrick2025shigellosis pages 17-18)
- O’Donovan, “Identification of host factors required for cytosol entry by Shigella flexneri,” Dissertation, Oct 2023. DOI:10.17863/cam.102175; URL: https://doi.org/10.17863/cam.102175. T3SS translocon; NAIP/NLRC4, NLRP3, caspase‑4/5; GSDMD. (odonovan2023identificationofhost pages 43-47)
- Lu et al., “Shigella Vaccines: The Continuing Unmet Challenge,” IJMS, Apr 2024. DOI:10.3390/ijms25084329; URL: https://doi.org/10.3390/ijms25084329. Vaccine antigens, epidemiology/AMR context. (lu2024shigellavaccinesthe pages 4-5, lu2024shigellavaccinesthe pages 18-20)
- Worley, “Immune evasion and persistence in enteric bacterial pathogens,” Gut Microbes, Jan 2023. DOI:10.1080/19490976.2022.2163839; URL: https://doi.org/10.1080/19490976.2022.2163839. IpaD/IpgD; immune evasion; model systems. (worley2023immuneevasionand pages 31-32)
- Reghunathan, “Towards In-Vitro Reconstitution of Actin Comet Tail Formation and Septin Caging in Shigella,” 2024. DOI:10.17918/00010587; URL: https://doi.org/10.17918/00010587. Detailed actin motility mechanisms (IcsA/N‑WASP/Arp2/3). (reghunathan2024towardsinvitroreconstitution pages 26-32)
- Mason (thesis excerpts on genomic epidemiology and ipaH): 2025. Genomics of AMR and molecular diagnostics (ipaH). (mason2025thegenomicepidemiology pages 219-222)

Direct quotes (from evidence where present)
- “IpaB and IpaC assemble a funnel-shaped pore in target membranes through which the injectisome docks to deliver effectors.” (DOI:10.17863/cam.102175, Oct 2023; URL: https://doi.org/10.17863/cam.102175) (odonovan2023identificationofhost pages 43-47)
- “Cytosolic detection of T3SS components (MxiH/MxiI) activates NAIP/NLRC4… [and] inflammatory caspases cleave gasdermin D to form membrane pores.” (DOI:10.17863/cam.102175, Oct 2023; URL: https://doi.org/10.17863/cam.102175) (odonovan2023identificationofhost pages 43-47)
- “Stool cytokines are markedly elevated and inflammation can persist >1 month, especially in children.” (DOI:10.1016/S0140-6736(25)01033-5, Oct 2025; URL: https://doi.org/10.1016/s0140-6736(25)01033-5) (hendrick2025shigellosis pages 8-9)

Limitations and open questions
- While mechanistic frameworks for T3SS-driven invasion, inflammasome sensing, and actin-based spread are well supported, cell type–specific inflammasome roles within the human colonic epithelium and the balance of protective versus pathologic pyroptosis in vivo remain active areas of research. Translational correlation of emerging vaccine correlates (e.g., anti-LPS IgG thresholds) with field efficacy across serotypes is ongoing. (lu2024shigellavaccinesthe pages 18-20, hendrick2025shigellosis pages 8-9)

Overall, the cellular microbiology and immunology of shigellosis converge on T3SS-enabled intracellular lifestyle, actin-based lateral dissemination, and inflammasome-modulated inflammation that together drive mucosal pathology. Rising AMR strengthens the case for prevention and host-directed interventions alongside vaccines focused on conserved invasion machinery. (hendrick2025shigellosis pages 8-9, hendrick2025shigellosis pages 17-18, lu2024shigellavaccinesthe pages 18-20, odonovan2023identificationofhost pages 43-47)

References

1. (hendrick2025shigellosis pages 8-9): Jennifer Hendrick, Rubhana Raqib, Zannatun Noor, A S G Faruque, Rashidul Haque, and William A Petri. Shigellosis. The Lancet, 406:1508-1519, Oct 2025. URL: https://doi.org/10.1016/s0140-6736(25)01033-5, doi:10.1016/s0140-6736(25)01033-5. This article has 0 citations and is from a highest quality peer-reviewed journal.

2. (hendrick2025shigellosis pages 17-18): Jennifer Hendrick, Rubhana Raqib, Zannatun Noor, A S G Faruque, Rashidul Haque, and William A Petri. Shigellosis. The Lancet, 406:1508-1519, Oct 2025. URL: https://doi.org/10.1016/s0140-6736(25)01033-5, doi:10.1016/s0140-6736(25)01033-5. This article has 0 citations and is from a highest quality peer-reviewed journal.

3. (lu2024shigellavaccinesthe pages 4-5): Ti Lu, Sayan Das, Debaki R. Howlader, William D. Picking, and Wendy L. Picking. Shigella vaccines: the continuing unmet challenge. International Journal of Molecular Sciences, 25:4329, Apr 2024. URL: https://doi.org/10.3390/ijms25084329, doi:10.3390/ijms25084329. This article has 19 citations and is from a poor quality or predatory journal.

4. (worley2023immuneevasionand pages 31-32): Micah J. Worley. Immune evasion and persistence in enteric bacterial pathogens. Gut Microbes, Jan 2023. URL: https://doi.org/10.1080/19490976.2022.2163839, doi:10.1080/19490976.2022.2163839. This article has 26 citations and is from a peer-reviewed journal.

5. (odonovan2023identificationofhost pages 43-47): Conor O'Donovan. Identification of host factors required for cytosol entry by shigella flexneri: results of a genome-wide crispr/cas9 screen. Dissertation, Oct 2023. URL: https://doi.org/10.17863/cam.102175, doi:10.17863/cam.102175. This article has 0 citations.

6. (lu2024shigellavaccinesthe pages 18-20): Ti Lu, Sayan Das, Debaki R. Howlader, William D. Picking, and Wendy L. Picking. Shigella vaccines: the continuing unmet challenge. International Journal of Molecular Sciences, 25:4329, Apr 2024. URL: https://doi.org/10.3390/ijms25084329, doi:10.3390/ijms25084329. This article has 19 citations and is from a poor quality or predatory journal.

7. (reghunathan2024towardsinvitroreconstitution pages 26-32): Sarath Reghunathan. Towards in-vitro reconstitution of actin comet tail formation and septin caging in shigella. ArXiv, 2024. URL: https://doi.org/10.17918/00010587, doi:10.17918/00010587. This article has 0 citations.

8. (mason2025thegenomicepidemiology pages 219-222): L Mason. The genomic epidemiology of antimicrobial resistant sexually transmissible shigellosis. Unknown journal, 2025.