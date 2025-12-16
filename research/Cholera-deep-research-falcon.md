---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-15T09:01:02.156764'
end_time: '2025-12-15T09:10:45.506928'
duration_seconds: 583.35
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Cholera
  mondo_id: ''
  category: Infectious Disease
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
- **Disease Name:** Cholera
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Cholera**.
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
- **Disease Name:** Cholera
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Cholera**.
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


Disease Pathophysiology Research Report

Target Disease
- Disease Name: Cholera
- MONDO ID: 
- Category: Infectious Disease

Pathophysiology description
Cholera is a toxin-mediated secretory diarrheal disease caused by intestinal infection with toxigenic Vibrio cholerae. The central pathophysiologic axis is driven by cholera toxin (CT), an AB5 protein complex in which the pentameric B subunit (CTB) binds host glycoconjugate receptors at the apical surface of small-intestinal epithelial cells and the A1 enzymatic subunit (CTA1) catalyzes ADP-ribosylation of the heterotrimeric G protein Gsα (GNAS). This locks adenylyl cyclase in an active state, elevating intracellular cAMP, activating protein kinase A (PKA), and driving CFTR-mediated chloride efflux and massive osmotic water secretion into the lumen, culminating in profuse “rice‑water” diarrhea and hypovolemic shock if untreated (Wernick et al., Toxins, 2010; https://doi.org/10.3390/toxins2030310, published 5 Mar 2010) (wernick2010choleratoxinan pages 1-4). A recent concise synthesis emphasizes the same core sequence—CT → adenylyl cyclase → cAMP → PKA → CFTR—while highlighting that CT-driven signaling also reprograms host epithelial metabolism to release host-derived nutrients that can fuel intraluminal V. cholerae growth and transmission (Dominguez et al., Curr Opin Microbiol, 2024; https://doi.org/10.1016/j.mib.2023.102421, published Feb 2024) (dominguez2024theintersectionbetween pages 1-2, dominguez2024theintersectionbetween pages 8-10, dominguez2024theintersectionbetween pages 10-11).

Beyond GM1 ganglioside, CTB recognizes alternative glycan ligands, including fucosylated glycoproteins such as the Lewis X (LeX) antigen. In human enteroids and other models, GM1-independent intoxication occurs and is blockable by fucosylated oligosaccharides or anti-LeX antibodies, demonstrating that glycoprotein glycans can serve as functional receptors in addition to GM1 (Cervin et al., PLoS Pathog, 2018; https://doi.org/10.1371/journal.ppat.1006862, published 12 Feb 2018) (cervin2018gm1gangliosideindependentintoxication pages 1-2). Once bound, CTB–receptor complexes undergo endocytosis and traffic retrograde through early endosomes and the trans-Golgi network to the endoplasmic reticulum (ER). There, CTA1 separates, unfolds via protein disulfide isomerase, and hijacks the ER-associated degradation (ERAD) retro-translocation machinery to reach the cytosol, where it refolds and ADP-ribosylates Gsα to activate adenylyl cyclase (Wernick et al., 2010) (wernick2010choleratoxinan pages 1-4). As directly stated: “the A1-chain is unfolded by protein disulfide isomerase and retro-translocated to the cytosol by hijacking components of the ER associated degradation pathway… [then] ADP-ribosylates the large G-protein Gs and [activates] adenylyl cyclase” (wernick2010choleratoxinan pages 1-4).

V. cholerae successfully colonizes the small intestine by traversing the mucus barrier, adhering to the epithelium, and forming microcolonies through the toxin-coregulated pilus (TCP). Virulence factor expression—CTX and TCP—is controlled by a regulatory cascade centered on ToxR, TcpP, and the AraC-family regulator ToxT; ToxR also remodels outer membrane porins (e.g., upregulating OmpU) to resist bile and antimicrobial peptides, while the neuraminidase NanH exposes GM1 for CT binding (Montero et al., Front Med, 2023; https://doi.org/10.3389/fmed.2023.1155751, published May 2023) (montero2023vibriocholeraeclassification pages 5-6, montero2023vibriocholeraeclassification pages 6-7). Accessory toxins and effectors—MARTX (actin cytoskeleton disruption, phagocyte inhibition, innate signaling modulation), hemolysin HlyA (pore formation/ion leakage, often OMV-associated), zonula occludens toxin (Zot; tight junction perturbation), and accessory cholera enterotoxin Ace (secretory effects)—contribute to pathogenesis in a strain- and context-dependent manner (Montero et al., 2023) (montero2023vibriocholeraeclassification pages 6-7). The acute disease is often non-inflammatory during peak secretory phases, with CT-linked immunomodulatory properties, yet infection triggers adaptive immune responses, and biofilm growth in vivo supports a hyperinfectious state and fecal–oral transmission (Dominguez et al., 2024; Montero et al., 2023) (dominguez2024theintersectionbetween pages 1-2, dominguez2024theintersectionbetween pages 10-11, montero2023vibriocholeraeclassification pages 6-7).

Key quotes (mechanistic anchors)
- “The A1-chain is… retro-translocated to the cytosol by hijacking… ERAD… [and] ADP-ribosylates… Gs and [activates] adenylyl cyclase.” (Wernick et al., 2010; https://doi.org/10.3390/toxins2030310) (wernick2010choleratoxinan pages 1-4)
- “CT increases cellular cAMP, activating PKA which phosphorylates and activates CFTR to secrete chloride ions” (Dominguez et al., 2024; https://doi.org/10.1016/j.mib.2023.102421) (dominguez2024theintersectionbetween pages 10-11)
- “CTB binds fucosylated proteins… binding correlates with expression of the fucosylated Lewis X (LeX) glycan… CT can induce toxicity in the absence of GM1.” (Cervin et al., 2018; https://doi.org/10.1371/journal.ppat.1006862) (cervin2018gm1gangliosideindependentintoxication pages 1-2)
- “Toxigenic vibrios express CTX and TCP as main virulence determinants… NanH… exposing GM1… Accessory toxins include MARTX, HlyA, Zot, and Ace.” (Montero et al., 2023; https://doi.org/10.3389/fmed.2023.1155751) (montero2023vibriocholeraeclassification pages 6-7)

1) Core Pathophysiology
- Primary mechanisms: CTB binds GM1 and alternative glycans (e.g., LeX) on enterocytes; holotoxin undergoes retrograde trafficking to the ER; CTA1 exploits ERAD to enter the cytosol and ADP-ribosylates Gsα; adenylyl cyclase activation elevates cAMP, activates PKA, and opens CFTR, producing chloride and water secretion (Wernick 2010; Dominguez 2024; Cervin 2018) (wernick2010choleratoxinan pages 1-4, dominguez2024theintersectionbetween pages 10-11, dominguez2024theintersectionbetween pages 1-2, cervin2018gm1gangliosideindependentintoxication pages 1-2).
- Dysregulated pathways: cAMP/PKA signaling and epithelial ion transport (CFTR-mediated Cl− secretion) dominate the secretory phenotype; paracellular permeability can be enhanced by Zot; pore formation and ion leakage by HlyA; cytoskeletal and innate signaling disruption by MARTX (Montero 2023; Dominguez 2024) (montero2023vibriocholeraeclassification pages 6-7, dominguez2024theintersectionbetween pages 10-11, dominguez2024theintersectionbetween pages 8-10).
- Affected cellular processes: receptor-mediated endocytosis and retrograde transport; ER protein quality control (ERAD) repurposed by CTA1; epithelial ion channel regulation; mucus barrier interactions and biofilm-linked colonization (Wernick 2010; Montero 2023; Dominguez 2024) (wernick2010choleratoxinan pages 1-4, montero2023vibriocholeraeclassification pages 6-7, dominguez2024theintersectionbetween pages 1-2).

2) Key Molecular Players
- Genes/Proteins: GNAS (Gsα; ADP-ribosylation target), CFTR (apical Cl− channel), ToxR/TcpP/ToxT (virulence regulation), NanH (sialidase), CTA1/CTB (toxin subunits), HlyA, Zot, Ace, MARTX (Wernick 2010; Montero 2023; Dominguez 2024; Cervin 2018) (wernick2010choleratoxinan pages 1-4, montero2023vibriocholeraeclassification pages 6-7, dominguez2024theintersectionbetween pages 10-11, cervin2018gm1gangliosideindependentintoxication pages 1-2).
- Chemical entities: GM1 ganglioside and fucosylated glycans (e.g., LeX) as CTB receptors; cAMP (second messenger); NAD+ as ADP-ribose donor; bile acids (host cues modulating virulence) (Cervin 2018; Wernick 2010; Dominguez 2024; Montero 2023) (cervin2018gm1gangliosideindependentintoxication pages 1-2, wernick2010choleratoxinan pages 1-4, dominguez2024theintersectionbetween pages 10-11, montero2023vibriocholeraeclassification pages 5-6).
- Cell types: small-intestinal enterocytes as principal targets; mucus-producing cells provide glycoconjugate ligands/decoys (Cervin 2018; Wernick 2010; Dominguez 2024) (cervin2018gm1gangliosideindependentintoxication pages 1-2, wernick2010choleratoxinan pages 1-4, dominguez2024theintersectionbetween pages 1-2).
- Anatomical sites: ileal small intestine; apical membrane microdomains; mucus layer; lumenal milieu enriched in host nutrients during disease (Dominguez 2024; Montero 2023; Wernick 2010) (dominguez2024theintersectionbetween pages 8-10, montero2023vibriocholeraeclassification pages 6-7, wernick2010choleratoxinan pages 1-4).

3) Biological Processes (GO annotation candidates)
- “Adenylyl cyclase-activating G protein-coupled receptor signaling pathway” and “cAMP-mediated signaling” are centrally activated by CTA1→Gsα modification, with downstream “protein phosphorylation” (PKA) regulating “chloride transmembrane transport” via CFTR (Wernick 2010; Dominguez 2024) (wernick2010choleratoxinan pages 1-4, dominguez2024theintersectionbetween pages 10-11, dominguez2024theintersectionbetween pages 1-2).
- “Endocytosis,” “retrograde vesicle-mediated transport,” and “ER-associated protein catabolic process (ERAD)” support CTA1 entry to cytosol (Wernick 2010) (wernick2010choleratoxinan pages 1-4).
- “Tight junction organization” and “paracellular transport” perturbed by Zot; “membrane pore formation” by HlyA; “actin cytoskeleton organization” modulated by MARTX; “mucin catabolic process” and “adhesion to host” in colonization (Montero 2023) (montero2023vibriocholeraeclassification pages 6-7).

4) Cellular Components
- Apical plasma membrane/lipid rafts (GM1 clustering) and early/recycling endosomes, trans-Golgi network, and ER are essential compartments for CT trafficking (Wernick 2010) (wernick2010choleratoxinan pages 1-4).
- ERAD machinery (e.g., Sec61/Derlin/Hrd1 axis) is co-opted for CTA1 retro-translocation (Wernick 2010) (wernick2010choleratoxinan pages 1-4).
- Tight junctions at epithelial apical junctional complex are a target for Zot; CFTR resides in apical membrane (Montero 2023; Wernick 2010) (montero2023vibriocholeraeclassification pages 6-7, wernick2010choleratoxinan pages 1-4).

5) Disease Progression
- Incubation spans ~12 hours to 5 days, reflecting acid sensitivity and infectious dose; colonization entails mucus penetration, adhesion (GbpA/TCP), and microcolony formation under ToxR/ToxT/TcpP regulation. CT and accessory toxins are secreted via the type II secretion system and OMVs, binding to epithelial receptors to initiate intoxication and secretory diarrhea (Montero 2023) (montero2023vibriocholeraeclassification pages 5-6, montero2023vibriocholeraeclassification pages 6-7).
- Cellular sequence: CTB binds GM1 and/or fucosylated glycoproteins → endocytosis and retrograde trafficking → CTA1 ERAD escape → Gsα ADP-ribosylation → AC activation → cAMP surge → PKA activation → CFTR phosphorylation/activation → Cl− and water secretion. MARTX, HlyA, Zot, and Ace add cytoskeletal disruption, membrane permeabilization, junctional changes, and additional secretory drive (Wernick 2010; Montero 2023; Dominguez 2024) (wernick2010choleratoxinan pages 1-4, montero2023vibriocholeraeclassification pages 6-7, dominguez2024theintersectionbetween pages 10-11).

6) Phenotypic Manifestations
- Key clinical phenotypes: sudden, voluminous “rice‑water” stools; rapid dehydration and electrolyte losses; hypovolemic shock; acidosis when severe. Mechanistically, these reflect CFTR-dependent chloride secretion and osmotic water flux, with accessory effects on paracellular permeability and membrane integrity (Dominguez 2024; Wernick 2010; Montero 2023) (dominguez2024theintersectionbetween pages 10-11, wernick2010choleratoxinan pages 1-4, montero2023vibriocholeraeclassification pages 6-7).

Recent developments and latest research (2023–2024)
- Human-relevant host–pathogen metabolism: CT not only drives CFTR-dependent secretion but also reshapes epithelial metabolism to release nutrients (LCFAs, lactate, glycerol), potentially enhancing V. cholerae luminal growth and transmission; bile acids and the microbiome modulate biofilm formation and virulence gene expression (Dominguez 2024; https://doi.org/10.1016/j.mib.2023.102421) (dominguez2024theintersectionbetween pages 10-11, dominguez2024theintersectionbetween pages 8-10).
- Receptor diversity on human enteroids: CT binding/intoxication in primary jejunal enteroids involves GM1-scarce surfaces and fucosylated glycoproteins; inhibition of fucosylation/glycosylation alters susceptibility, emphasizing decoy versus functional ligands and inter-individual variability (Cervin 2018; https://doi.org/10.1371/journal.ppat.1006862; see also Montero 2023 for NanH–GM1 exposure) (cervin2018gm1gangliosideindependentintoxication pages 1-2, montero2023vibriocholeraeclassification pages 5-6, montero2023vibriocholeraeclassification pages 6-7).
- Updated synthesis of colonization and accessory toxins: 2023 review consolidates roles for TCP, T6SS, OmpU, mucinases (HapA/TagA), adhesins (GbpA/FrhA), and accessory toxins (MARTX, HlyA, Zot, Ace) as contributors to disease severity and transmission (Montero 2023; https://doi.org/10.3389/fmed.2023.1155751) (montero2023vibriocholeraeclassification pages 6-7, montero2023vibriocholeraeclassification pages 5-6).

Current applications and real-world implementations
- Mechanism-informed clinical priorities: The cAMP–PKA–CFTR axis underpins standard supportive therapy targeting rapid correction of water and electrolyte deficits; mechanistic understanding of CT trafficking and CFTR activation informs the rationale for antisecretory strategies in development (Wernick 2010; Dominguez 2024) (wernick2010choleratoxinan pages 1-4, dominguez2024theintersectionbetween pages 10-11).
- Vaccine/colonization insights: TCP’s centrality to colonization and its role as the CTXΦ receptor continue to guide vaccine antigen choices; environmental sensing by ToxR/TcpP/ToxT and OMV packaging of CT inform next-generation approaches (Montero 2023) (montero2023vibriocholeraeclassification pages 6-7, montero2023vibriocholeraeclassification pages 5-6).

Expert opinions and analysis
- A mechanistic consensus view: “CT… activates adenylyl cyclase, elevating cAMP, and driving chloride secretion” (Wernick 2010) and “CT increases cellular cAMP, activating PKA… CFTR” (Dominguez 2024) articulate a consistent expert framework for cholera’s core secretory mechanism (wernick2010choleratoxinan pages 1-4, dominguez2024theintersectionbetween pages 10-11).
- Emerging expert emphasis: recent analyses posit that CT-mediated metabolic reprogramming and microbiome/bile acid interactions are integral to pathogenesis and transmission fitness, extending beyond pure ion flux pathology (Dominguez 2024) (dominguez2024theintersectionbetween pages 8-10, dominguez2024theintersectionbetween pages 10-11).

Relevant statistics and data
- Incubation and colonization context: acid sensitivity necessitating high infectious dose in healthy volunteers; incubation about 12 h to 5 days; thick intestinal mucus barrier (≈100–400 µm) to be traversed (Montero 2023; https://doi.org/10.3389/fmed.2023.1155751) (montero2023vibriocholeraeclassification pages 5-6). While quantitative electrolyte-loss statistics can vary by outbreak and treatment context, the molecular pathway consistently links cAMP–PKA–CFTR activation to the massive fluid loss that defines severe cholera (Dominguez 2024; Wernick 2010) (dominguez2024theintersectionbetween pages 10-11, wernick2010choleratoxinan pages 1-4).

Gene/protein annotations with ontology terms (HGNC, GO)
- GNAS (HGNC:4392): substrate for CTA1 ADP-ribosylation → adenylyl cyclase activation; cAMP-mediated signaling (wernick2010choleratoxinan pages 1-4).
- CFTR (HGNC:1884): apical Cl− channel phosphorylated by PKA; chloride transmembrane transport and fluid secretion (wernick2010choleratoxinan pages 1-4, dominguez2024theintersectionbetween pages 10-11).
- ToxR/TcpP/ToxT: virulence regulators controlling ctxAB and tcpA (colonization); environmental sensing and bile resistance (montero2023vibriocholeraeclassification pages 6-7).
- NanH (neuraminidase): exposes GM1 on host cells to enhance CT binding (montero2023vibriocholeraeclassification pages 5-6).

Phenotype associations (HP terms; descriptive mapping)
- Acute watery diarrhea with “rice‑water” stools; severe dehydration; hypovolemic shock; metabolic acidosis in severe cases—mechanistically linked to CFTR‑mediated chloride secretion and water efflux and junctional/membrane perturbations (dominguez2024theintersectionbetween pages 10-11, montero2023vibriocholeraeclassification pages 6-7, wernick2010choleratoxinan pages 1-4).

Cell type involvement (CL terms)
- Enterocytes (CL:0000584): principal intoxicated cells executing chloride and water secretion (wernick2010choleratoxinan pages 1-4, dominguez2024theintersectionbetween pages 10-11).
- Mucus-associated epithelial cells provide glycoprotein ligands/decoys for CTB (cervin2018gm1gangliosideindependentintoxication pages 1-2).

Anatomical locations (UBERON terms)
- Small intestine, especially ileum (UBERON:0002116): site of colonization, intoxication, and secretion (dominguez2024theintersectionbetween pages 8-10, montero2023vibriocholeraeclassification pages 6-7).

Chemical entities (CHEBI terms)
- cAMP (second messenger), NAD+ (CTA1 substrate), GM1 ganglioside (glycolipid receptor), bile acids (host cues), fucosylated LeX glycan (alternative receptor) (wernick2010choleratoxinan pages 1-4, dominguez2024theintersectionbetween pages 10-11, cervin2018gm1gangliosideindependentintoxication pages 1-2, montero2023vibriocholeraeclassification pages 5-6).

Evidence items with PMIDs/DOIs and dates (URLs included)
- Wernick NLB et al. Cholera toxin: an intracellular journey into the cytosol by way of the endoplasmic reticulum. Toxins. 2010 Mar 5. doi:10.3390/toxins2030310. URL: https://doi.org/10.3390/toxins2030310 (wernick2010choleratoxinan pages 1-4).
- Montero DA et al. Vibrio cholerae, classification, pathogenesis, immune response, and trends in vaccine development. Front Med. 2023 May. doi:10.3389/fmed.2023.1155751. URL: https://doi.org/10.3389/fmed.2023.1155751 (montero2023vibriocholeraeclassification pages 5-6, montero2023vibriocholeraeclassification pages 6-7).
- Dominguez SR et al. The intersection between host–pathogen interactions and metabolism during Vibrio cholerae infection. Curr Opin Microbiol. 2024 Feb. doi:10.1016/j.mib.2023.102421. URL: https://doi.org/10.1016/j.mib.2023.102421 (dominguez2024theintersectionbetween pages 10-11, dominguez2024theintersectionbetween pages 1-2, dominguez2024theintersectionbetween pages 8-10).
- Cervin J et al. GM1 ganglioside-independent intoxication by Cholera toxin. PLoS Pathog. 2018 Feb 12. doi:10.1371/journal.ppat.1006862. URL: https://doi.org/10.1371/journal.ppat.1006862 (cervin2018gm1gangliosideindependentintoxication pages 1-2).
- Walia K, Ganguly NK. Toxins of Vibrio cholerae and their role in inflammation, pathogenesis, and immunomodulation. 2011 Sep. doi:10.1007/978-1-60327-265-0_15. URL: https://doi.org/10.1007/978-1-60327-265-0_15 (walia2011toxinsofvibrio pages 272-274).

Entity–ontology mapping artifact
| Entity | Category | Ontology | Ontology ID | Role in Cholera Pathophysiology | Key supporting sources |
|---|---|---|---|---|---|
| GNAS | Gene/Protein | HGNC | HGNC:4392 | Gs alpha subunit ADP-ribosylated by CTA1 -> constitutive adenylate cyclase activation | (wernick2010choleratoxinan pages 1-4) |
| CFTR | Gene/Protein | HGNC | HGNC:1884 | cAMP/PKA-activated apical Cl- channel driving chloride and water secretion | (wernick2010choleratoxinan pages 1-4, dominguez2024theintersectionbetween pages 10-11) |
| GM1 ganglioside | Chemical (glycolipid) | CHEBI |  | Cell-surface receptor for CTB that mediates endocytosis and retrograde trafficking | (wernick2010choleratoxinan pages 1-4, montero2023vibriocholeraeclassification pages 5-6) |
| CTA1 (A1 chain) | Protein (toxin) |  |  | Enzymatic ADP-ribosyltransferase that modifies Gsα (GNAS) to raise cAMP | (wernick2010choleratoxinan pages 1-4) |
| CTB (B subunit) | Protein (toxin) |  |  | Pentameric lectin that binds GM1 and alternative glycans (e.g., LeX) to enable uptake | (cervin2018gm1gangliosideindependentintoxication pages 1-2, wernick2010choleratoxinan pages 1-4) |
| Adenylate cyclase activation pathway | Process | GO | GO:0007189 | Activation of AC downstream of Gsα modification leading to cAMP production | (wernick2010choleratoxinan pages 1-4, dominguez2024theintersectionbetween pages 10-11) |
| cAMP signaling | Process/Chemical | CHEBI / GO |  | Second-messenger cascade (cAMP → PKA) that drives CFTR phosphorylation and ion secretion | (wernick2010choleratoxinan pages 1-4, dominguez2024theintersectionbetween pages 10-11) |
| PKA (protein kinase A) | Protein |  |  | cAMP-activated kinase that phosphorylates CFTR and modulates epithelial ion transport | (dominguez2024theintersectionbetween pages 10-11) |
| CFTR-mediated chloride secretion | Process | GO | GO:0006821 | PKA-phosphorylated CFTR increases apical Cl- efflux, producing osmotic water loss (rice-water stool) | (wernick2010choleratoxinan pages 1-4, dominguez2024theintersectionbetween pages 10-11) |
| ERAD retro-translocation | Process | GO |  | ER-associated degradation pathway hijacked by CTA1 for cytosolic entry of A1 chain | (wernick2010choleratoxinan pages 1-4) |
| ToxR / ToxT / TcpP / TCP | Regulatory system / Structure |  |  | Transcriptional regulatory cascade controlling toxT, ctxAB and TCP for toxin production and colonization | (montero2023vibriocholeraeclassification pages 5-6, dominguez2024theintersectionbetween pages 10-11) |
| NanH neuraminidase | Protein (enzyme) |  |  | Removes sialic acids to expose GM1 and enhance CT binding to enterocytes | (montero2023vibriocholeraeclassification pages 5-6) |
| MARTX | Toxin (multifunctional) |  |  | Large effector toxin disrupting actin, inhibiting phagocytosis and modulating innate signaling | (montero2023vibriocholeraeclassification pages 5-6) |
| HlyA (hemolysin) | Protein (toxin) |  |  | Pore-forming toxin causing cell damage and ion leakage; associated with OMVs | (montero2023vibriocholeraeclassification pages 5-6) |
| Zot (zonula occludens toxin) | Protein (toxin) |  |  | Disrupts tight junctions and increases paracellular permeability contributing to secretory diarrhea | (montero2023vibriocholeraeclassification pages 5-6, walia2011toxinsofvibrio pages 272-274) |
| Ace (accessory cholera enterotoxin) | Protein (toxin) |  |  | Alters ion transport and contributes to fluid secretion (generally milder effect) | (montero2023vibriocholeraeclassification pages 5-6, walia2011toxinsofvibrio pages 272-274) |
| Enterocyte | Cell | CL | CL:0000584 | Intestinal absorptive epithelial cell targeted by CT; mediates secretion and barrier function | (wernick2010choleratoxinan pages 1-4, dominguez2024theintersectionbetween pages 10-11) |
| Goblet cell | Cell | CL |  | Mucin-secreting epithelial cell; source of mucus and glycoprotein decoy ligands for CTB | (cervin2018gm1gangliosideindependentintoxication pages 1-2) |
| Small intestine (ileum) | Anatomy | UBERON | UBERON:0002116 | Primary site of V. cholerae colonization and CT-mediated secretory responses | (dominguez2024theintersectionbetween pages 10-11, montero2023vibriocholeraeclassification pages 5-6) |
| Mucus layer | Anatomy / ECM |  |  | Barrier containing glycoconjugates that V. cholerae must penetrate; provides decoy and functional CT ligands | (montero2023vibriocholeraeclassification pages 5-6, cervin2018gm1gangliosideindependentintoxication pages 1-2) |
| cAMP (chemical) | Chemical (second messenger) | CHEBI |  | Intracellular messenger produced by AC; activates PKA and downstream secretion | (wernick2010choleratoxinan pages 1-4, dominguez2024theintersectionbetween pages 10-11) |
| NAD+ | Chemical (cofactor) | CHEBI |  | ADP-ribose donor substrate for CTA1-catalyzed ADP-ribosylation of Gsα | (wernick2010choleratoxinan pages 1-4) |
| Bile acids | Chemical (host metabolite) | CHEBI |  | Host-derived signals that modulate V. cholerae virulence regulation (ToxR/ToxT) and colonization dynamics | (dominguez2024theintersectionbetween pages 10-11) |
| Fucosylated Lewis X glycan (LeX) | Chemical (glycan) |  |  | Alternative CTB ligand on glycoproteins enabling GM1-independent intoxication of human enterocytes | (cervin2018gm1gangliosideindependentintoxication pages 1-2) |
| Outer membrane vesicles (OMVs) | Structure / Particle |  |  | Vehicles packaging CT and accessory toxins for protected delivery to host cells | (montero2023vibriocholeraeclassification pages 5-6) |


*Table: Compact, evidence-linked table mapping key molecular, cellular, anatomical, and chemical entities in cholera pathophysiology with ontology IDs where available and supporting source citations (context IDs).*

References (supporting specific claims; see in-text IDs)
- CT structure, trafficking, ERAD escape, and Gsα ADP-ribosylation: (wernick2010choleratoxinan pages 1-4).
- GM1-independent binding and glycan receptors (LeX): (cervin2018gm1gangliosideindependentintoxication pages 1-2).
- Colonization determinants (TCP, adhesins, mucinases), virulence regulation (ToxR/ToxT/TcpP), and accessory toxins (MARTX, HlyA, Zot, Ace): (montero2023vibriocholeraeclassification pages 6-7, montero2023vibriocholeraeclassification pages 5-6).
- Core secretory mechanism and host metabolic remodeling; bile acid/microbiome modulation: (dominguez2024theintersectionbetween pages 10-11, dominguez2024theintersectionbetween pages 1-2, dominguez2024theintersectionbetween pages 8-10).
- Ion transport, paracellular effects, and clinical secretory phenotype doctrines: (walia2011toxinsofvibrio pages 272-274, wernick2010choleratoxinan pages 1-4, dominguez2024theintersectionbetween pages 10-11).

Notes on evidence scope
Where detailed population statistics (e.g., case counts) and certain host genetic susceptibility factors were sought, the most recent, directly mechanistic sources available in the present corpus emphasized molecular pathways and colonization biology rather than comprehensive epidemiologic quantifications. Consequently, quantitative epidemiology is referenced only where supported by the included 2023–2024 reviews, while mechanistic inferences and quotes are directly cited from the sources listed (wernick2010choleratoxinan pages 1-4, montero2023vibriocholeraeclassification pages 5-6, walia2011toxinsofvibrio pages 272-274, cervin2018gm1gangliosideindependentintoxication pages 1-2, montero2023vibriocholeraeclassification pages 6-7, dominguez2024theintersectionbetween pages 10-11, dominguez2024theintersectionbetween pages 1-2, dominguez2024theintersectionbetween pages 8-10).

References

1. (wernick2010choleratoxinan pages 1-4): Naomi L. B. Wernick, Daniel J.-F. Chinnapen, Jin Ah Cho, and Wayne I. Lencer. Cholera toxin: an intracellular journey into the cytosol by way of the endoplasmic reticulum. Toxins, 2:310-325, Mar 2010. URL: https://doi.org/10.3390/toxins2030310, doi:10.3390/toxins2030310. This article has 257 citations and is from a poor quality or predatory journal.

2. (dominguez2024theintersectionbetween pages 1-2): Sedelia R. Dominguez, Phillip N Doan, and Fabian Rivera-Chávez. The intersection between host–pathogen interactions and metabolism during vibrio cholerae infection. Current Opinion in Microbiology, 77:102421, Feb 2024. URL: https://doi.org/10.1016/j.mib.2023.102421, doi:10.1016/j.mib.2023.102421. This article has 7 citations and is from a peer-reviewed journal.

3. (dominguez2024theintersectionbetween pages 8-10): Sedelia R. Dominguez, Phillip N Doan, and Fabian Rivera-Chávez. The intersection between host–pathogen interactions and metabolism during vibrio cholerae infection. Current Opinion in Microbiology, 77:102421, Feb 2024. URL: https://doi.org/10.1016/j.mib.2023.102421, doi:10.1016/j.mib.2023.102421. This article has 7 citations and is from a peer-reviewed journal.

4. (dominguez2024theintersectionbetween pages 10-11): Sedelia R. Dominguez, Phillip N Doan, and Fabian Rivera-Chávez. The intersection between host–pathogen interactions and metabolism during vibrio cholerae infection. Current Opinion in Microbiology, 77:102421, Feb 2024. URL: https://doi.org/10.1016/j.mib.2023.102421, doi:10.1016/j.mib.2023.102421. This article has 7 citations and is from a peer-reviewed journal.

5. (cervin2018gm1gangliosideindependentintoxication pages 1-2): Jakob Cervin, Amberlyn M. Wands, Anna Casselbrant, Han Wu, Soumya Krishnamurthy, Aleksander Cvjetkovic, Johanna Estelius, Benjamin Dedic, Anirudh Sethi, Kerri-Lee Wallom, Rebecca Riise, Malin Bäckström, Ville Wallenius, Frances M. Platt, Michael Lebens, Susann Teneberg, Lars Fändriks, Jennifer J. Kohler, and Ulf Yrlid. Gm1 ganglioside-independent intoxication by cholera toxin. PLOS Pathogens, 14:e1006862, Feb 2018. URL: https://doi.org/10.1371/journal.ppat.1006862, doi:10.1371/journal.ppat.1006862. This article has 88 citations and is from a highest quality peer-reviewed journal.

6. (montero2023vibriocholeraeclassification pages 5-6): David A. Montero, Roberto M. Vidal, Juliana Velasco, Sergio George, Yalda Lucero, Leonardo A. Gómez, Leandro J. Carreño, Richard García-Betancourt, and Miguel O’Ryan. Vibrio cholerae, classification, pathogenesis, immune response, and trends in vaccine development. Frontiers in Medicine, May 2023. URL: https://doi.org/10.3389/fmed.2023.1155751, doi:10.3389/fmed.2023.1155751. This article has 136 citations and is from a poor quality or predatory journal.

7. (montero2023vibriocholeraeclassification pages 6-7): David A. Montero, Roberto M. Vidal, Juliana Velasco, Sergio George, Yalda Lucero, Leonardo A. Gómez, Leandro J. Carreño, Richard García-Betancourt, and Miguel O’Ryan. Vibrio cholerae, classification, pathogenesis, immune response, and trends in vaccine development. Frontiers in Medicine, May 2023. URL: https://doi.org/10.3389/fmed.2023.1155751, doi:10.3389/fmed.2023.1155751. This article has 136 citations and is from a poor quality or predatory journal.

8. (walia2011toxinsofvibrio pages 272-274): Kamini Walia and Nirmal Kumar Ganguly. Toxins of vibrio cholerae and their role in inflammation, pathogenesis, and immunomodulation. ArXiv, pages 259-275, Sep 2011. URL: https://doi.org/10.1007/978-1-60327-265-0\_15, doi:10.1007/978-1-60327-265-0\_15. This article has 6 citations.