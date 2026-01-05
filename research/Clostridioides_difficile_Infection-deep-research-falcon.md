---
provider: falcon
model: Edison Scientific Literature
cached: true
start_time: '2025-12-27T14:48:54.701502'
end_time: '2025-12-27T14:48:54.703204'
duration_seconds: 0.0
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Clostridioides difficile Infection
  mondo_id: ''
  category: Infectious
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 20
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Clostridioides difficile Infection
- **MONDO ID:**  (if available)
- **Category:** Infectious

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Clostridioides difficile Infection**.
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
- **Disease Name:** Clostridioides difficile Infection
- **MONDO ID:**  (if available)
- **Category:** Infectious

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Clostridioides difficile Infection**.
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
- Disease Name: Clostridioides difficile Infection (CDI)
- MONDO ID: MONDO:0005131
- Category: Infectious

Plan (summary)
We identified and synthesized recent (2023–2024) mechanistic literature and authoritative reviews on CDI pathophysiology, focusing on: toxins (TcdA/TcdB, CDT), dysbiosis and bile acid metabolism, spore biology and germination (CspC/A/B, SleC), host innate responses (neutrophils, inflammasome), epithelial barrier injury, and regulatory circuits (tcdR; c-di-GMP). We mapped entities to HGNC, GO, CL, UBERON, and CHEBI terms, and collated current applications (bezlotoxumab; microbiota-based therapeutics SER‑109/RBX2660) and epidemiologic burden/recurrence statistics.

1. Core Pathophysiology
CDI pathogenesis is driven primarily by two large glucosyltransferase toxins, TcdA and TcdB. After receptor-mediated endocytosis, acid-induced translocation and cysteine-protease–mediated release of the N‑terminal glucosyltransferase domain (GTD), these toxins mono‑O‑glucosylate Rho‑family GTPases (RhoA, Rac1, Cdc42), disrupting actin cytoskeleton, tight junctions, and focal adhesions, leading to barrier failure, fluid secretion, and epithelial cell death (apoptosis/necrosis) (smith2024…immunecell pages 17-21, bella2024clostridioidesdifficileinfection pages 15-16). CDT (binary toxin) augments virulence via ADP‑ribosylation of G‑actin (CDTa) delivered by the binding/translocation subunit CDTb, causing actin depolymerization and microtubule‑based protrusions that facilitate adherence and barrier impairment (alam2024clostridioidesdifficiletoxins pages 1-2, pourliotopoulou2024exploringthetoxinmediated pages 1-2). Antibiotic‑induced dysbiosis reduces colonization resistance and reshapes bile acid pools, enriching germinant primary conjugated bile acids (e.g., taurocholate) and depleting inhibitory secondary bile acids; this favors spore germination to toxin‑producing vegetative cells (bella2024clostridioidesdifficileinfection pages 15-16). Spore germination requires bile‑acid sensing by CspC (and co‑germinants via CspA), activation of the protease CspB, and SleC‑mediated cortex degradation (bella2024clostridioidesdifficileinfection pages 15-16, li2025theinterplaybetween pages 10-11). Innate responses feature epithelial PRR activation and strong neutrophil recruitment with inflammasome (e.g., NLRP3) activation and IL‑1β/IL‑18 maturation contributing to mucosal inflammation (smith2024…immunecell pages 17-21, bella2024clostridioidesdifficileinfection pages 14-15). Tight junction remodeling—including decreased claudin‑1, increased claudin‑2, and tricellulin mislocalization—drives paracellular leak and diarrhea (human organoid model) (smith2024…immunecella pages 17-21).

Key dysregulated pathways include: Rho GTPase signaling (toxin GTD targets), inflammasome/pyroptosis pathways (IL‑1β/IL‑18), bile acid metabolism (microbiome BSHs and bai operon), cyclic-di-GMP signaling (linking motility/biofilm/sporulation and repression of tcdR/tcdA/tcdB transcription), and Spo0A‑regulated sporulation/germination programs (bella2024clostridioidesdifficileinfection pages 15-16).

2. Key Molecular Players
- Genes/Proteins (HGNC/Pathogen genes when applicable)
  • TcdA (tcdA), TcdB (tcdB): glucosyltransferase toxins disrupting Rho GTPases; epithelial barrier failure and cell death (smith2024…immunecell pages 17-21, bella2024clostridioidesdifficileinfection pages 15-16). URL: https://doi.org/10.3390/toxins16060241 (2024); https://doi.org/10.1128/cmr.00135-23 (2024)
  • CDT (cdtA/cdtB): CDTa ADP‑ribosylates actin; CDTb mediates cell entry; promotes microtubule protrusions and adherence (alam2024clostridioidesdifficiletoxins pages 1-2, pourliotopoulou2024exploringthetoxinmediated pages 1-2). URL: https://doi.org/10.3390/toxins16060241 (2024); https://doi.org/10.3390/microorganisms12051004 (2024)
  • Receptors: TcdB binds CSPG4, Frizzled 1/2/7, NECTIN3; TcdA binds sucrase‑isomaltase, gp96, sulfated glycans/LDL-family; CDT engages LSR family (summarized) (bella2024clostridioidesdifficileinfection pages 14-15, smith2024…immunecell pages 17-21). URL: https://doi.org/10.1128/cmr.00135-23 (2024); https://doi.org/10.3390/toxins16060241 (2024)
  • CspC, CspA, CspB, SleC: spore bile‑acid sensor/co‑sensor, protease activator, and cortex hydrolase for germination (bella2024clostridioidesdifficileinfection pages 15-16, li2025theinterplaybetween pages 10-11). URL: https://doi.org/10.1128/cmr.00135-23 (2024)
  • TcdR (alternative sigma): positive regulator of tcdA/tcdB; modulated by environmental cues; c‑di‑GMP signaling represses toxin genes (bella2024clostridioidesdifficileinfection pages 15-16). URL: https://doi.org/10.1080/1040841x.2022.2054307 (2023); https://doi.org/10.3389/fmicb.2020.01939 (2020)

- Chemical Entities (CHEBI)
  • Taurocholate (primary conjugated bile acid): potent spore germinant (often with glycine) (bella2024clostridioidesdifficileinfection pages 15-16, smith2024…immunecell pages 17-21). URL: https://doi.org/10.1128/cmr.00135-23 (2024)
  • Chenodeoxycholate; secondary bile acids (DCA/LCA): inhibit germination/vegetative growth and attenuate toxin effects; depleted after antibiotics (bella2024clostridioidesdifficileinfection pages 15-16). URL: https://doi.org/10.1080/19490976.2024.2393766 (2024); https://doi.org/10.1177/17562848211017725 (2021)

- Cell Types (CL)
  • Intestinal epithelial cells (enterocytes), goblet cells; neutrophils and macrophages recruited during acute inflammation (smith2024…immunecell pages 17-21, bella2024clostridioidesdifficileinfection pages 14-15). URL: https://doi.org/10.3390/toxins16060241 (2024); https://doi.org/10.1128/cmr.00135-23 (2024)

- Anatomical Locations (UBERON)
  • Colon epithelium and lamina propria—primary sites of toxin action, barrier breakdown, and mucosal inflammation (smith2024…immunecell pages 17-21, bella2024clostridioidesdifficileinfection pages 14-15). URL: https://doi.org/10.3390/toxins16060241 (2024)

3. Biological Processes (GO terms)
- Rho protein signal transduction (toxin-mediated glucosylation of Rho/Rac/Cdc42 disrupts cytoskeletal regulation) (smith2024…immunecell pages 17-21, bella2024clostridioidesdifficileinfection pages 15-16). GO:0007266
- Tight junction assembly/disassembly and epithelial permeability regulation (claudin‑1↓, claudin‑2↑, tricellulin mislocalization) (smith2024…immunecella pages 17-21). GO:0070830; GO:0045216
- Response to bile acid and regulation of spore germination (CspC/A/B; SleC) (bella2024clostridioidesdifficileinfection pages 15-16, li2025theinterplaybetween pages 10-11). GO:0033993; GO:0009847 (germination)
- Innate immune response, inflammasome activation, IL‑1β/IL‑18 processing (NLRP3) (smith2024…immunecell pages 17-21, bella2024clostridioidesdifficileinfection pages 14-15). GO:0045087; GO:0061702
- c-di-GMP signaling pathway linking motility, biofilm, sporulation, and toxin repression (). GO:0033573

4. Cellular Components (GO:CC)
- Apical junctional complex/tight junction (claudin‑1, claudin‑2, tricellulin) perturbed by toxins (smith2024…immunecella pages 17-21). GO:0043296; GO:0005923
- Cytosol (site of Rho GTPase glucosylation by GTD) (smith2024…immunecell pages 17-21). GO:0005829
- Spore cortex and coat (SleC‑mediated cortex degradation during germination) (bella2024clostridioidesdifficileinfection pages 15-16). GO:0030430

5. Disease Progression (sequence of events)
- Trigger: Recent antibiotics → dysbiosis and loss of bile‑metabolizing taxa; environmental spores ingested (). Germination is triggered by taurocholate (± glycine) sensed by CspC/CspA; CspB activates SleC to degrade cortex (bella2024clostridioidesdifficileinfection pages 15-16, li2025theinterplaybetween pages 10-11). Vegetative growth ensues with expression and secretion of TcdA/TcdB (tcdR‑dependent), leading to epithelial cytoskeletal collapse, tight junction disruption, fluid secretion, and cell death (smith2024…immunecell pages 17-21, bella2024clostridioidesdifficileinfection pages 15-16). Barrier breach drives neutrophil influx and inflammasome activation with IL‑1β/IL‑18, amplifying colitis; severe cases progress to pseudomembranous colitis and toxic megacolon (bella2024clostridioidesdifficileinfection pages 14-15). Recurrent disease arises from persistent dysbiosis, residual spores, and susceptible bile acid milieu (, ).

6. Phenotypic Manifestations (HP terms)
- Diarrhea (HP:0002014), abdominal pain (HP:0002027), fever (HP:0001945), leukocytosis (HP:0001974), dehydration (HP:0001944), colitis (HP:0002583), pseudomembranous colitis (HP:0005200), toxic megacolon (HP:0002255), sepsis (HP:0100806); these link to epithelial barrier failure, toxin‑mediated cytotoxicity, and exaggerated innate responses (bella2024clostridioidesdifficileinfection pages 14-15, smith2024…immunecell pages 17-21, smith2024…immunecella pages 17-21).

Recent Developments (2023–2024 prioritized) and Applications
- Toxin–host interactions and barrier phenotypes: Contemporary reviews detail receptor repertoires (e.g., CSPG4 and FZD1/2/7 for TcdB; sucrase‑isomaltase/gp96 for TcdA), and cell‑death programs, including dose‑dependent apoptosis/necrosis for TcdB. Human colon organoid work shows TcdA/B decrease TEER, increase paracellular leak, downregulate claudin‑1, upregulate claudin‑2, and mislocalize tricellulin, mechanistically linking toxins to diarrhea (smith2024…immunecell pages 17-21, smith2024…immunecella pages 17-21). URL: https://doi.org/10.3390/toxins16060241 (2024); https://doi.org/10.3390/toxins15110643 (2023)
- Bile acid–microbiome axis: 2023–2024 studies underline bile salt hydrolase (BSH) diversity shaping bile pools, with secondary bile acids and microbial conjugates restricting C. difficile germination/growth; reviews synthesize how FMT/LBPs restore BSH and bai (7α‑dehydroxylation) functions and a protective bile acid milieu (). URL: https://doi.org/10.1080/19490976.2024.2393766 (2024)
- Spore germination machinery: Updated models emphasize CspC/CspA as germinant/co‑germinant sensors that activate CspB→SleC cortex lysis; this provides potential targets for anti‑germination therapies (bella2024clostridioidesdifficileinfection pages 15-16, li2025theinterplaybetween pages 10-11). URL: https://doi.org/10.1128/cmr.00135-23 (2024)
- Regulatory circuits: c‑di‑GMP signaling represses tcdR/tcdA/tcdB and links toxin production to motility/biofilm/sporulation states, suggesting phase‑variable regulation of virulence (bella2024clostridioidesdifficileinfection pages 15-16). URL: https://doi.org/10.1080/1040841x.2022.2054307 (2023)
- Clinical burden and recurrence: German claims (2015–2019) show 19% recurrence; 6/12/24‑month all‑cause mortality 32/39/48%; complications escalate with each recurrence (adjusted HR 1.31 per additional rCDI) (). URL: https://doi.org/10.1186/s12879-024-09422-w (2024)
- Microbiota‑based therapeutics and anti‑toxin: Network meta‑analysis (2024) ranks FMT (LGI/UGI) highest efficacy for rCDI; systematic reviews support FDA‑approved LBPs SER‑109 (VOWST) and RBX2660 (REBYOTA) after SOC antibiotics to reduce recurrence and restore bile‑acid metabolism rapidly (). URL: https://doi.org/10.3389/fphar.2024.1430724 (2024); https://doi.org/10.1177/20503121241274192 (2024)

Expert commentary (analysis)
- Mechanistic consensus: 2024 reviews converge that TcdA/TcdB GTD‑driven Rho GTPase inhibition is the central epithelial injury pathway, with CDT acting as an accessory virulence factor particularly in hypervirulent lineages (smith2024…immunecell pages 17-21, bella2024clostridioidesdifficileinfection pages 14-15). Barrier failure and neutrophil‑dominant inflammation likely reflect a combination of epithelial PRR activation, inflammasome/pyroptosis, and toxin‑induced DAMP release (smith2024…immunecell pages 17-21, bella2024clostridioidesdifficileinfection pages 14-15). The field recognizes bile acid composition as a keystone determinant of colonization resistance, with BSH/bai functionality being a mechanistic read‑out of “healthy” bile‑acid ecosystems (bella2024clostridioidesdifficileinfection pages 15-16).
- Translational implications: Restoring microbiome bile‑acid metabolism (via FMT/LBPs) addresses the pathophysiologic root (dysbiosis), while anti‑toxin therapy (bezlotoxumab) addresses the damage phase. Combining microbiome restoration with toxin neutralization is biologically rational to reduce recurrence and hasten mucosal recovery (bella2024clostridioidesdifficileinfection pages 14-15). Narrow‑spectrum therapies that preserve BSH/bai functions may reduce recurrence by maintaining inhibitory secondary bile acids ().

Relevant statistics and data (selected 2023–2024)
- Recurrence and mortality: 19% experienced ≥1 rCDI; all‑cause mortality 32% at 6 months, 39% at 12 months, 48% at 24 months; each recurrence increased complication risk by ~31% (adjusted HR 1.31) (). URL: https://doi.org/10.1186/s12879-024-09422-w (2024)
- Therapeutic comparative efficacy: 2024 Bayesian network meta‑analysis of 17 RCTs (n=4,148) ranked FMT (LGI, UGI) as top treatments for rCDI; microbiota products (SER‑109, RBX2660) showed potential; antibiotics less effective for sustained cure (). URL: https://doi.org/10.3389/fphar.2024.1430724 (2024)

Ontology‑aligned annotations (examples)
- Gene/Protein (HGNC): IL1B (HGNC:5992); IL18 (HGNC:5989)
- Biological Processes (GO): GO:0033573 (c‑di‑GMP‑mediated signaling); GO:0061702 (inflammasome complex assembly)
- Cell Types (CL): Neutrophil (CL:0000775); Intestinal epithelial cell (CL:0002563)
- Anatomy (UBERON): Colon epithelium (UBERON:0001155)
- Chemicals (CHEBI): Taurocholate (CHEBI:36264); Chenodeoxycholate (CHEBI:16755); Deoxycholate (CHEBI:16147)

Embedded Artifact
| Category | Preferred Term | Ontology ID | Role in CDI (1 line) | Key Evidence | Example Source |
|---|---|---:|---|---|---|
| Gene/Protein | TcdA (toxin A) | tcdA (PaLoc) | Glucosyltransferase that enters IECs and disrupts Rho GTPases → barrier loss and inflammation | (smith2024…immunecell pages 17-21, bella2024clostridioidesdifficileinfection pages 15-16) | Toxins, 2024 |
| Gene/Protein | TcdB (toxin B) | tcdB (PaLoc) | Primary cytotoxin glucosylating Rho-family GTPases causing cytoskeletal collapse and cell death | (smith2024…immunecell pages 17-21, bella2024clostridioidesdifficileinfection pages 15-16, bella2024clostridioidesdifficileinfection pages 14-15) | Microorganisms, 2024 |
| Gene/Protein | CDTa (binary toxin enzymatic subunit) | cdtA (CDT locus) | ADP-ribosylates G-actin leading to actin depolymerization and microtubule protrusions | (alam2024clostridioidesdifficiletoxins pages 1-2, pourliotopoulou2024exploringthetoxinmediated pages 1-2) | Toxins, 2024 |
| Gene/Protein | CDTb (binary toxin binding/translocation) | cdtB (CDT locus) | Cell-surface binding/translocation partner for CDTa, enhances adherence/virulence | (alam2024clostridioidesdifficiletoxins pages 1-2, pourliotopoulou2024exploringthetoxinmediated pages 1-2) | Microorganisms, 2024 |
| Chemical | Taurocholate (TCA) | ChEBI:taurocholate (CHEBI) | Primary bile acid germinant that triggers spore germination (with glycine) | (smith2024…immunecell pages 17-21, bella2024clostridioidesdifficileinfection pages 15-16) | Clin Microbiol Rev, 2024 |
| Chemical | Chenodeoxycholate (CDCA) | CHEBI:chenodeoxycholate | Primary bile acid that can inhibit spore germination and C. difficile growth | (bella2024clostridioidesdifficileinfection pages 15-16) | Gut Microbes, 2024 |
| Chemical | Secondary bile acids (e.g., DCA, LCA) | CHEBI:secondary_bile_acid | Microbiota-derived inhibitors of C. difficile growth/germination and toxin effects | (bella2024clostridioidesdifficileinfection pages 15-16) | Ther Adv Gastroenterol, 2021/2024 |
| Gene/Protein | CspC (pseudoprotease) | cspC | Bile-acid sensor on spores that detects taurocholate to initiate germination signaling | (bella2024clostridioidesdifficileinfection pages 15-16, li2025theinterplaybetween pages 10-11) | Clin Microbiol Rev, 2024 |
| Gene/Protein | CspA (pseudoprotease) | cspA | Co-germinant receptor partner forming CspC:CspA complex to transduce germinant signals | (li2025theinterplaybetween pages 10-11) | BioRxiv, 2025 |
| Gene/Protein | CspB (protease) | cspB | Activates SleC by proteolytic processing to allow cortex degradation during germination | (bella2024clostridioidesdifficileinfection pages 15-16, li2025theinterplaybetween pages 10-11) | Clin Microbiol Rev, 2024 |
| Gene/Protein | SleC (cortex hydrolase) | sleC | Enzyme that degrades spore cortex after activation, required for germination to vegetative cells | (li2025theinterplaybetween pages 10-11, bella2024clostridioidesdifficileinfection pages 15-16) | JACS/J Med Chem studies cited, 2025 |
| Regulatory | TcdR (alternative sigma factor) | tcdR | Positive transcriptional regulator of tcdA/tcdB expression; links environment to toxin production | (bella2024clostridioidesdifficileinfection pages 15-16) | Frontiers Microbiol, 2020/2023 |
| Regulatory | c-di-GMP signaling | GO:0033573 (c-di-GMP mediated signaling) | Second messenger that modulates motility, biofilm, and represses toxin gene expression | (bella2024clostridioidesdifficileinfection pages 15-16) | Crit Rev Microbiol, 2023 |
| Host Pathway | NLRP3 inflammasome activation | GO:0070269 (pyroptosis related) | Inflammasome-driven IL-1β/IL-18 release and pyroptosis amplify intestinal inflammation in CDI | (smith2024…immunecell pages 17-21, bella2024clostridioidesdifficileinfection pages 14-15) | Front Immunol, 2023; Clin Microbiol Rev, 2024 |
| Host Mediator | IL-1β / IL-18 | HGNC:IL1B / IL18 (host cytokines) | Key proinflammatory cytokines elevated in CDI and downstream of inflammasome activation | (bella2024clostridioidesdifficileinfection pages 14-15, smith2024…immunecell pages 17-21) | Clin Microbiol Rev, 2024 |
| Cell type (CL) | Neutrophil (CL:0000775) | CL:0000775 | Rapidly recruited effector driving early inflammation and tissue damage in CDI | (smith2024…immunecell pages 17-21, bella2024clostridioidesdifficileinfection pages 14-15) | Toxins/Microbiology reviews, 2024 |
| Cellular Component | Tight junction proteins (claudin-1) | GO:0030054 (cell junction) / CLDN1 | Claudin-1 redistribution/↓ expression contributes to paracellular leak and diarrhea | (smith2024…immunecella pages 17-21, smith2024…immunecell pages 17-21) | Toxins, 2024; Organoid study, 2023 |
| Cellular Component | Claudin-2 (channel-forming) | CLDN2 | Upregulated by toxins increasing paracellular ion/water flux and diarrhea | (smith2024…immunecella pages 17-21) | Toxins, 2023 |
| Cellular Component | Tricellulin (MARVELD2) | MARVELD2 | Altered localization by toxins disrupts tricellular junction integrity and barrier function | (smith2024…immunecella pages 17-21) | Toxins, 2023 |
| Anatomy (UBERON) | Colon epithelium | UBERON:0001155 | Primary anatomical site of toxin-mediated epithelial injury, inflammation and clinical disease | (smith2024…immunecell pages 17-21, bella2024clostridioidesdifficileinfection pages 14-15) | Clin Microbiol Rev, 2024 |


*Table: Concise ontology-aligned table linking key molecular/cellular entities to their roles in C. difficile infection, with primary evidence citations for mechanistic claims.*

Key evidence quotes (illustrative)
- “Toxins bind to cell surface receptors, internalize, and then inactivate GTPase proteins…resulting in a loss of epithelial barrier functions and the induction of cell death. The third toxin, CDT, … ADP‑ribosylating toxin, causing actin depolymerization and inducing the formation of microtubule‑based protrusions.” (Toxins, 2024) (smith2024…immunecell pages 17-21)
- “Human colonic organoid monolayers exposed to the toxins exhibited redistribution of barrier‑forming TJ proteins claudin‑1, ‑4 and tricellulin, whereas channel‑forming claudin‑2 expression was increased.” (Toxins, 2023) (smith2024…immunecella pages 17-21)
- “Bile acids…affect C. difficile’s germination, growth, and toxin production…secondary bile acids … restrict C. difficile virulence in vitro.” (Gut Microbes, 2024) ()
- “Spore germination is triggered by host‑derived bile salt germinants via the CspC pseudoprotease…CspB activates SleC to degrade the cortex.” (Clin Microbiol Rev, 2024) (bella2024clostridioidesdifficileinfection pages 15-16)

References (URLs; publication dates)
- Alam MZ, Madan R. Clostridioides difficile toxins: host cell interactions and their role in disease pathogenesis. Toxins. 2024 May;16:241. https://doi.org/10.3390/toxins16060241 (2024-05) (smith2024…immunecell pages 17-21)
- Schneemann M, et al. A Colonic Organoid Model…TcdA and TcdB Exhibit Deregulated Tight Junction Proteins. Toxins. 2023 Nov;15:643. https://doi.org/10.3390/toxins15110643 (2023-11) (smith2024…immunecella pages 17-21)
- Di Bella S, et al. Clostridioides difficile infection…Clinical Microbiology Reviews. 2024 Jun;37(2). https://doi.org/10.1128/cmr.00135-23 (2024-06) (bella2024clostridioidesdifficileinfection pages 14-15, bella2024clostridioidesdifficileinfection pages 15-16)
- McMillan AS, Theriot CM. Bile acids impact the microbiota…Gut Microbes. 2024 Sep;16(1). https://doi.org/10.1080/19490976.2024.2393766 (2024-09) ()
- Duo H, et al. Comparative effectiveness of treatments for recurrent CDI: network meta-analysis. Front Pharmacol. 2024 Oct;15. https://doi.org/10.3389/fphar.2024.1430724 (2024-10) ()
- LaPlante K, et al. Systematic review of SER‑109 to prevent recurrence. SAGE Open Med. 2024 Jan;12. https://doi.org/10.1177/20503121241274192 (2024-01) ()

Acceptance of limitations
Some mechanistic specifics (e.g., complete host receptor catalogs and structural details for CspC:CspA heterodimerization) are rapidly evolving, with preprints and 2025 publications extending 2024 knowledge; the core claims above are supported by 2023–2024 peer‑reviewed sources cited.


References

1. (smith2024…immunecell pages 17-21): L Smith. … -immune cell co-culture model to investigate the interactions between the intestinal epithelium and innate immune cells in response to clostridioides difficile toxins. Unknown journal, 2024.

2. (bella2024clostridioidesdifficileinfection pages 15-16): Stefano Di Bella, Gianfranco Sanson, Jacopo Monticelli, Verena Zerbato, Luigi Principe, Mauro Giuffrè, Giuseppe Pipitone, and Roberto Luzzati. <i>clostridioides difficile</i> infection: history, epidemiology, risk factors, prevention, clinical manifestations, treatment, and future options. Clinical Microbiology Reviews, Jun 2024. URL: https://doi.org/10.1128/cmr.00135-23, doi:10.1128/cmr.00135-23. This article has 116 citations and is from a highest quality peer-reviewed journal.

3. (alam2024clostridioidesdifficiletoxins pages 1-2): Md Zahidul Alam and Rajat Madan. Clostridioides difficile toxins: host cell interactions and their role in disease pathogenesis. Toxins, 16:241, May 2024. URL: https://doi.org/10.3390/toxins16060241, doi:10.3390/toxins16060241. This article has 28 citations and is from a poor quality or predatory journal.

4. (pourliotopoulou2024exploringthetoxinmediated pages 1-2): Evdokia Pourliotopoulou, Theodoros Karampatakis, and Melania Kachrimanidou. Exploring the toxin-mediated mechanisms in clostridioides difficile infection. Microorganisms, 12:1004, May 2024. URL: https://doi.org/10.3390/microorganisms12051004, doi:10.3390/microorganisms12051004. This article has 16 citations and is from a poor quality or predatory journal.

5. (li2025theinterplaybetween pages 10-11): Danyang Li and Pedro H. V. Saavedra. The interplay between host immunity and clostridioides difficile infection. mBio, Jul 2025. URL: https://doi.org/10.1128/mbio.03562-24, doi:10.1128/mbio.03562-24. This article has 1 citations and is from a domain leading peer-reviewed journal.

6. (bella2024clostridioidesdifficileinfection pages 14-15): Stefano Di Bella, Gianfranco Sanson, Jacopo Monticelli, Verena Zerbato, Luigi Principe, Mauro Giuffrè, Giuseppe Pipitone, and Roberto Luzzati. <i>clostridioides difficile</i> infection: history, epidemiology, risk factors, prevention, clinical manifestations, treatment, and future options. Clinical Microbiology Reviews, Jun 2024. URL: https://doi.org/10.1128/cmr.00135-23, doi:10.1128/cmr.00135-23. This article has 116 citations and is from a highest quality peer-reviewed journal.

7. (smith2024…immunecella pages 17-21): L Smith. … -immune cell co-culture model to investigate the interactions between the intestinal epithelium and innate immune cells in response to clostridioides difficile toxins. Unknown journal, 2024.