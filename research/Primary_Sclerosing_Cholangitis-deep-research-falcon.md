---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-18T09:46:25.159898'
end_time: '2025-12-18T09:53:15.793504'
duration_seconds: 410.63
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Primary Sclerosing Cholangitis
  mondo_id: ''
  category: Autoimmune
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 18
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Primary Sclerosing Cholangitis
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Primary Sclerosing Cholangitis**.
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
- **Disease Name:** Primary Sclerosing Cholangitis
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Primary Sclerosing Cholangitis**.
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


Plan to answer
Objective 2 (mechanisms): Synthesize immune, epithelial, stromal, bile-acid, and microbiome axes; extract recent data points and quotes. Objective 3–6: Enumerate key molecules/cell types/locations and align to ontologies (HGNC, GO, CL, UBERON, CHEBI) where appropriate; outline disease progression and phenotype links. Objective 7: Deliver a comprehensive, citable research report prioritizing 2023–2024 sources with URLs and dates.

Disease Pathophysiology Research Report

Target Disease
- Disease Name: Primary Sclerosing Cholangitis (PSC)
- MONDO ID: not specified (leave blank if unavailable in current context)
- Category: Autoimmune (immune-mediated cholangiopathy)

Pathophysiology description
Primary sclerosing cholangitis is a progressive, immune-mediated cholangiopathy characterized by chronic inflammation and fibro-obliterative scarring of intra- and/or extrahepatic bile ducts, culminating in cholestasis, biliary fibrosis, cirrhosis, and heightened risk of cholangiocarcinoma. Contemporary models integrate: (1) mucosal immune activation in the gut with lymphocyte homing to the liver via MAdCAM-1–α4β7 and other addressins; (2) cholangiocyte-intrinsic injury responses including epigenetically reinforced senescence and SASP that amplify inflammation and the ductular reaction (DR); (3) reciprocal crosstalk with portal fibroblasts and hepatic stellate cells (HSCs) driving periductal fibrosis; (4) dysregulated bile-acid receptor signaling (FXR–FGF19, GPBAR1/TGR5) and bicarbonate umbrella failure; and (5) a gut microbiome–bile acid axis that fosters dysbiosis, barrier dysfunction, bacterial translocation, and immune activation in the portal tract. PSC is polygenic with strong HLA signals and several non-HLA immune loci (e.g., IL2RA, MST1, SH2B3, BACH2, DCDC2), consistent with adaptive immune dysregulation intersecting with epithelial injury and cholestatic signaling (Oct 2024; Cells; https://doi.org/10.3390/cells13191650) (fiorucci2024bileacidsbasedtherapies pages 1-2, fiorucci2024bileacidsbasedtherapies pages 2-4, wang2024molecularmechanismsof pages 6-8).

1) Core Pathophysiology
- Immune mechanisms: Inflamed hepatic sinusoidal endothelium expresses MAdCAM-1, recruiting α4β7+ gut-primed lymphocytes; innate activation (macrophages, dendritic cells, NK cells) promotes NF-κB/NLRP3-dependent cytokines (IL-6, IL-12, IL-1β, TNF-α) and Th1/Th17 responses, with portal CD4+ and lobular CD8+ infiltrates. This gut–liver homing axis is a defining feature of PSC immunobiology (Oct 2024; Cells; https://doi.org/10.3390/cells13191650) (fiorucci2024bileacidsbasedtherapies pages 2-4).
- Unconventional T cells and cholangiocyte antigen presentation: Cholangiocytes upregulate MHC I/II under inflammation and can present non-peptide antigens via CD1d and MR1; “CD1d is downregulated in PSC and PBC,” and bile from PSC contains MAIT antigens; anti-MR1 blockade attenuates MAIT activation. MAIT cells can drive cholangiocyte proliferation via amphiregulin (AREG), indicating reciprocal epithelial–immune loops (Sep 2025; Hepatology; https://doi.org/10.1097/hep.0000000000001093) (jalansakrikar2025centralrolefor pages 17-18).
- Cholangiocyte senescence and SASP: PSC shows accelerated cholangiocyte senescence, reduced tight junction ZO-1, and SASP mediators (e.g., IL-1β, IL-6, IL-8, CCL2, MMP3, PAI-1; SERPINE1, IGFBP5), with senescent burden correlating with severity. Epigenetic marks (H3K4me3 activation of CDKN2A; H3K9me3 silencing of TERT) reinforce senescence; cholangiocyte-selective TERT deficiency worsens fibrosis in vivo, while danazol can ameliorate fibrosis in Abcb4−/− mice (Sep 2025; Hepatology; https://doi.org/10.1097/hep.0000000000001093) and (Oct 2024; Cells; https://doi.org/10.3390/cells13191650) (jalansakrikar2025centralrolefor pages 6-7, fiorucci2024bileacidsbasedtherapies pages 4-5).
- Ductular reaction and fibrogenic crosstalk: DRCs/ductular reaction cells expand and adopt a profibrotic, neutrophil-recruiting phenotype, secreting TNFα, IL-6, MCP-1, TGFβ. Portal fibroblasts (early responders near ducts) and HSCs (space of Disse) activate to ECM-producing myofibroblasts under cholangiokines and a stiffening matrix, creating a self-sustaining fibrogenic loop (Oct 2024; Cells; https://doi.org/10.3390/cells13191650; Sep 2025; Hepatology; https://doi.org/10.1097/hep.0000000000001093) (fiorucci2024bileacidsbasedtherapies pages 4-5, jalansakrikar2025centralrolefor pages 17-18, jalansakrikar2025centralrolefor pages 6-7).
- Bile-acid receptor signaling: Altered bile-acid composition in PSC (↑ serum total, primary and conjugated BAs; higher primary:secondary ratio; lower fecal BAs in PSC-IBD) and impaired “bicarbonate umbrella” stress cholangiocytes. Dysregulated FXR–FGF19 signaling may suppress BA synthesis (low C4 prognostic of worse outcomes), suggesting caution with potent FXR/FGF19 agonism in advanced disease; GPBAR1/TGR5 signaling in cholangiocytes supports bicarbonate secretion and immune regulation and is reported downregulated in PSC (Oct 2024; Cells; https://doi.org/10.3390/cells13191650) (fiorucci2024bileacidsbasedtherapies pages 9-10, fiorucci2024bileacidsbasedtherapies pages 1-2).
- Microbiome–bile acid axis and bacterial translocation: PSC exhibits consistent dysbiosis (↑ Enterococcus, Veillonella, Fusobacterium, Enterobacteriaceae, Streptococcus; ↓ Coprococcus, Blautia). Dysbiosis and mucosal barrier disruption promote PAMP translocation via the portal vein, activating hepatic APCs and perpetuating inflammation and fibrosis. Microbiome-directed interventions (e.g., vancomycin) have improved biochemical markers but lack proven disease-modifying effects (Oct 2024; Cells; https://doi.org/10.3390/cells13191650) (fiorucci2024bileacidsbasedtherapies pages 9-10, wang2024molecularmechanismsof pages 6-8).

2) Key Molecular Players
- Genes/Proteins (HGNC): HLA class I/II (antigen presentation); IL2RA (HGNC:6008), MST1 (HGNC:7390; also known as MST1/HPN context varies across studies), SH2B3 (HGNC:30473), BACH2 (HGNC:935), DCDC2 (HGNC:22911). Polygenic risk supports immune regulation and lymphocyte signaling in PSC genetics (Oct 2024; Cells; https://doi.org/10.3390/cells13191650) and OpenTargets PSC associations (EFO_0004268) (fiorucci2024bileacidsbasedtherapies pages 2-4).
- Chemical entities (CHEBI, where applicable): Bile acids (cholic acid, chenodeoxycholic acid; CHEBI:36262/16755), ursodeoxycholic acid (CHEBI:9907), norursodeoxycholic acid, FGF19 analogs (aldafermin), FXR agonists (obeticholic acid; CHEBI:82775; cilofexor; tropifexor), ASBT/IBAT inhibitors (e.g., maralixibat), PPAR agonists (elafibranor, seladelpar) (Oct 2024; Cells; https://doi.org/10.3390/cells13191650) (fiorucci2024bileacidsbasedtherapies pages 1-2, fiorucci2024bileacidsbasedtherapies pages 10-11, fiorucci2024bileacidsbasedtherapies pages 26-27).
- Cell types (CL): Cholangiocytes/biliary epithelial cells (CL:0002396), portal fibroblasts (CL:0002550; stromal myofibroblasts), hepatic stellate cells (CL:0000632), sinusoidal endothelial cells (CL:0002553), Kupffer cells/macrophages (CL:0000235), dendritic cells (CL:0000451), NK cells (CL:0000623), CD4+ and CD8+ T cells (CL:0000624/CL:0000625), MAIT cells (CL:0001064), iNKT cells (CL:0000814) (Sep 2025; Hepatology; https://doi.org/10.1097/hep.0000000000001093; Oct 2024; Cells; https://doi.org/10.3390/cells13191650) (jalansakrikar2025centralrolefor pages 17-18, jalansakrikar2025centralrolefor pages 6-7, fiorucci2024bileacidsbasedtherapies pages 4-5, fiorucci2024bileacidsbasedtherapies pages 2-4).
- Anatomical locations (UBERON): Intrahepatic and extrahepatic bile ducts (UBERON:0002394, UBERON:0002396), peribiliary glands (UBERON:0012684), portal tract (UBERON:0005912), liver sinusoid (UBERON:0001983), ileum/colon (UBERON:0002116/0001155) (Oct 2024; Cells; https://doi.org/10.3390/cells13191650) (wang2024molecularmechanismsof pages 6-8, fiorucci2024bileacidsbasedtherapies pages 4-5).

3) Biological Processes (candidate GO terms)
- Immune cell trafficking and adhesion: lymphocyte homing (GO:0072678), integrin-mediated adhesion (GO:0007155), leukocyte transendothelial migration (GO:0072671) (mechanistic rationale via MAdCAM-1–α4β7) (fiorucci2024bileacidsbasedtherapies pages 2-4).
- Antigen processing/presentation: MHC class I/II antigen processing (GO:0019882/GO:0019886); MR1- and CD1-mediated antigen presentation (GO:0042615 context), MAIT/iNKT activation (jalansakrikar2025centralrolefor pages 17-18).
- Cellular senescence and SASP: cellular senescence (GO:0090398), regulation of cell cycle arrest (GO:0071156), cytokine-mediated signaling (GO:0019221), extracellular matrix organization (GO:0030198) (jalansakrikar2025centralrolefor pages 6-7, fiorucci2024bileacidsbasedtherapies pages 4-5).
- Bile acid signaling and transport: response to bile acid (GO:0032865), FXR signaling pathway (curated pathway), FGF19 signaling (GO:0038167), GPBAR1/TGR5 signaling (GPCR signaling; GO:0007186), bile acid transport (GO:0015721) (fiorucci2024bileacidsbasedtherapies pages 9-10, fiorucci2024bileacidsbasedtherapies pages 1-2).
- Microbiome–host interactions: response to molecule of bacterial origin (GO:0002237), NLRP3 inflammasome activation (GO:1900225) (fiorucci2024bileacidsbasedtherapies pages 2-4, wang2024molecularmechanismsof pages 6-8).

4) Cellular Components (GO CC)
- Bile duct apical membrane and primary cilium (GO:0045177/GO:0005929) of cholangiocytes sensing bile flow/composition; plasma membrane and ciliary signaling hubs for TGR5/other receptors (fiorucci2024bileacidsbasedtherapies pages 4-5).
- Extracellular space/ECM (GO:0005576/GO:0031012) where SASP cytokines/chemokines and matrix proteins accumulate; periductal ECM stiffening feeds forward on cholangiocyte phenotype (jalansakrikar2025centralrolefor pages 17-18).
- Bile canaliculus/bile duct lumen (GO:0031253/GO:0034715), transporter-rich membranes (ASBT, BSEP, OSTα/β) (fiorucci2024bileacidsbasedtherapies pages 9-10).

5) Disease Progression
- Initiation: Gut dysbiosis and mucosal inflammation with barrier dysfunction; PAMPs and microbially modified bile acids reach the liver via portal circulation, activating APCs and priming gut-homing lymphocytes that enter the biliary tree (wang2024molecularmechanismsof pages 6-8, fiorucci2024bileacidsbasedtherapies pages 2-4).
- Propagation: Cholangiocyte stress from toxic bile acids and bicarbonate umbrella failure leads to epithelial injury, MHC I/II upregulation, and antigen presentation (MR1/CD1d) to MAIT/NKT cells; senescence with SASP reinforces leukocyte recruitment (jalansakrikar2025centralrolefor pages 17-18, fiorucci2024bileacidsbasedtherapies pages 4-5, jalansakrikar2025centralrolefor pages 6-7).
- Fibrogenesis: Ductular reaction expansion and cholangiokine production drive portal fibroblast and HSC activation and ECM deposition, with matrix stiffness further promoting cholangiocyte pro-fibrotic programming (jalansakrikar2025centralrolefor pages 17-18, fiorucci2024bileacidsbasedtherapies pages 4-5).
- Clinical manifestations: Progressive cholestasis and fibrosis; high transplant need over 12–20 years in a substantial fraction of patients; cholangiocarcinoma risk accrues (Oct 2024; Cells; https://doi.org/10.3390/cells13191650) (fiorucci2024bileacidsbasedtherapies pages 1-2, fiorucci2024bileacidsbasedtherapies pages 2-4).

6) Phenotypic Manifestations (HP terms)
- Cholestatic liver enzyme elevation: elevated alkaline phosphatase (HP:0003155) (fiorucci2024bileacidsbasedtherapies pages 1-2).
- Pruritus (HP:0000989) linked to bile-acid signaling; mechanistic work implicates pruritogens and BA receptors (fiorucci2024bileacidsbasedtherapies pages 26-27).
- Fatigue (HP:0012378) and jaundice (HP:0000952) with cholestasis; progressive biliary fibrosis/cirrhosis (HP:0001394) (fiorucci2024bileacidsbasedtherapies pages 1-2).
- PSC-IBD: coexisting ulcerative colitis/Crohn disease with increased PSC-IBD burden in population studies (Sep 2024; Lancet Reg Health Eur; https://doi.org/10.1016/j.lanepe.2024.101002) (fiorucci2024bileacidsbasedtherapies pages 10-11).
- Cancer risk: increased cholangiocarcinoma risk (range often cited ~10–15% over lifetime in reviews), concordant with progressive periductal inflammation/fibrosis (Oct 2024; Cells; https://doi.org/10.3390/cells13191650) (fiorucci2024bileacidsbasedtherapies pages 1-2).

Recent developments and latest research (2023–2024 priority)
- Epidemiology and PSC–IBD: A nationwide analysis across England (2015–2027) shows rising PSC-IBD prevalence with implications for transplant units (Sep 2024; Lancet Regional Health – Europe; https://doi.org/10.1016/j.lanepe.2024.101002) (fiorucci2024bileacidsbasedtherapies pages 10-11).
- Noninvasive fibrosis monitoring and risk models: Machine-learning PReSTo and liver stiffness thresholds via TE/MRE are being adopted; annual TE increase >1.3 kPa predicts worse transplant-free survival; however, no therapy has yet shown fibrosis reduction by LSM in trials (Oct 2024; Cells; https://doi.org/10.3390/cells13191650) (fiorucci2024bileacidsbasedtherapies pages 10-11).
- Microbiome–bile acid axis: PSC shows reproducible dysbiosis and altered bile-acid pools. Lower serum C4 (suppressed BA synthesis) predicts adverse outcomes; fecal bile acids reduced in PSC-IBD. These data caution about strong FXR–FGF19 suppression in advanced PSC (Oct 2024; Cells; https://doi.org/10.3390/cells13191650) (fiorucci2024bileacidsbasedtherapies pages 9-10).
- Immunobiology: High-resolution views emphasize tissue residency and unconventional T cell circuits engaging cholangiocytes (MR1/CD1d), with bile-borne antigens activating MAIT biology; extracellular matrix stiffness as a microenvironmental cue for cholangiocyte inflammatory/fibrogenic programming (Sep 2025; Hepatology; https://doi.org/10.1097/hep.0000000000001093) (jalansakrikar2025centralrolefor pages 17-18).

Current applications and real-world implementations
- Clinical management: MRCP-first diagnosis; supportive care with UDCA variably used despite lack of proven survival/transplant benefit; transplant for end-stage disease; surveillance for cholangiocarcinoma and colorectal cancer in PSC-IBD; use of TE/MRE and risk models (Oct 2024; Cells; https://doi.org/10.3390/cells13191650) (fiorucci2024bileacidsbasedtherapies pages 1-2, fiorucci2024bileacidsbasedtherapies pages 10-11).
- Microbiome-directed therapy: Oral vancomycin or other antibiotics can improve biochemistry and risk scores in some series, but durability and impact on progression remain unproven (Oct 2024; Cells; https://doi.org/10.3390/cells13191650) (fiorucci2024bileacidsbasedtherapies pages 9-10).

Expert opinions and analysis (authoritative sources)
- “The mechanistic involvement of the gut in PSC remains ambiguous,” yet gut microbial metabolites and BA signaling via FXR/GPBAR1 are central candidates; “lower C4 levels… are associated with worse clinical outcomes,” advising caution with strong FXR–FGF19 suppression in advanced disease (Oct 2024; Cells; https://doi.org/10.3390/cells13191650) (fiorucci2024bileacidsbasedtherapies pages 10-11, fiorucci2024bileacidsbasedtherapies pages 9-10).
- Cholangiocytes function as an immunologic hub capable of antigen presentation to unconventional T cells, and ECM stiffness actively drives their profibrotic program; better definition of cholangiocyte senescence and death modalities is a key research priority (Sep 2025; Hepatology; https://doi.org/10.1097/hep.0000000000001093) (jalansakrikar2025centralrolefor pages 17-18).

Relevant statistics and data
- Incidence/prevalence: Reviews summarize incidence ~1–1.5 per 100,000 person-years and prevalence ~6–16 per 100,000; male predominance; strong PSC–IBD association (Oct 2024; Cells; https://doi.org/10.3390/cells13191650) (fiorucci2024bileacidsbasedtherapies pages 1-2).
- PSC–IBD frequency: 60–80% of PSC patients have IBD (predominantly UC); 5–10% of UC patients have PSC (Dec 2024; Cells; https://doi.org/10.3390/cells13231997) (wang2024molecularmechanismsof pages 6-8).
- Progression: About 40% of patients ultimately undergo liver transplantation; typical time to transplant ~12–20 years (Oct 2024; Cells; https://doi.org/10.3390/cells13191650) (fiorucci2024bileacidsbasedtherapies pages 1-2, fiorucci2024bileacidsbasedtherapies pages 2-4).
- Bile-acid synthesis marker C4: Lower C4 associates with higher risk of transplant or death; UDCA did not change C4 (Oct 2024; Cells; https://doi.org/10.3390/cells13191650) (fiorucci2024bileacidsbasedtherapies pages 9-10).

Gene/protein annotations with ontology terms (examples)
- IL2RA (HGNC:6008): T cell activation, immune tolerance (GO:0042110; GO:0006955); genetic association in PSC (Oct 2024; Cells) (fiorucci2024bileacidsbasedtherapies pages 2-4).
- MST1 (HGNC:7390): Immune cell trafficking/adhesion; PSC association (Oct 2024; Cells) (fiorucci2024bileacidsbasedtherapies pages 2-4).
- SH2B3 (HGNC:30473), BACH2 (HGNC:935), DCDC2 (HGNC:22911): Immune regulation and cholangiocyte/microtubule biology implicated via GWAS/association (Oct 2024; Cells) (fiorucci2024bileacidsbasedtherapies pages 2-4).
- FXR/NR1H4 (HGNC:7965), GPBAR1/TGR5 (HGNC:18174): Bile acid receptor signaling in hepatobiliary and immune cells (GO:0009755; GO:0007186) (fiorucci2024bileacidsbasedtherapies pages 9-10, fiorucci2024bileacidsbasedtherapies pages 1-2).

Cell type involvement (CL terms)
- Cholangiocytes (CL:0002396), portal fibroblasts (CL:0002550), hepatic stellate cells (CL:0000632), Kupffer cells/macrophages (CL:0000235), dendritic cells (CL:0000451), MAIT cells (CL:0001064), iNKT cells (CL:0000814), CD4+ and CD8+ T cells (CL:0000624/CL:0000625), sinusoidal endothelial cells (CL:0002553) (jalansakrikar2025centralrolefor pages 17-18, fiorucci2024bileacidsbasedtherapies pages 4-5, fiorucci2024bileacidsbasedtherapies pages 2-4).

Anatomical locations (UBERON terms)
- Bile ducts (UBERON:0002394/0002396), peribiliary glands (UBERON:0012684), portal tract (UBERON:0005912), liver sinusoids (UBERON:0001983), ileum/colon (UBERON:0002116/0001155) (wang2024molecularmechanismsof pages 6-8, fiorucci2024bileacidsbasedtherapies pages 4-5).

Chemical entities (CHEBI terms, examples)
- Ursodeoxycholic acid (CHEBI:9907), cholic acid (CHEBI:36262), chenodeoxycholic acid (CHEBI:16755), obeticholic acid (CHEBI:82775), maralixibat (ASBT inhibitor), aldafermin (FGF19 analog), cilofexor/tropifexor (FXR agonists), elafibranor/seladelpar (PPAR agonists) (fiorucci2024bileacidsbasedtherapies pages 1-2, fiorucci2024bileacidsbasedtherapies pages 26-27, fiorucci2024bileacidsbasedtherapies pages 10-11).

Evidence items (with URLs/dates)
- Fiorucci et al., Bile Acids-Based Therapies for PSC: Current Landscape and Future Developments. Cells. Published Oct 4, 2024. DOI: 10.3390/cells13191650; URL: https://doi.org/10.3390/cells13191650 (fiorucci2024bileacidsbasedtherapies pages 2-4, fiorucci2024bileacidsbasedtherapies pages 9-10, fiorucci2024bileacidsbasedtherapies pages 1-2, fiorucci2024bileacidsbasedtherapies pages 4-5, fiorucci2024bileacidsbasedtherapies pages 26-27, fiorucci2024bileacidsbasedtherapies pages 10-11).
- Wang et al., Molecular Mechanisms of Fibrosis in Cholestatic Liver Diseases and Regenerative Medicine-Based Therapies. Cells. Dec 2024. DOI: 10.3390/cells13231997; URL: https://doi.org/10.3390/cells13231997 (psc–ibd statistics, gut–liver axis) (wang2024molecularmechanismsof pages 6-8).
- Jalan-Sakrikar et al., Central role for cholangiocyte pathobiology in cholestatic liver diseases. Hepatology. Sep 2025. DOI: 10.1097/hep.0000000000001093; URL: https://doi.org/10.1097/hep.0000000000001093 (MAIT/CD1d/MR1; epigenetic-senescence; ECM stiffness; DR) (jalansakrikar2025centralrolefor pages 17-18, jalansakrikar2025centralrolefor pages 6-7).
- Crothers et al., Past, current, and future trends in the prevalence of PSC and IBD across England (2015–2027). Lancet Regional Health – Europe. Sep 2024. DOI: 10.1016/j.lanepe.2024.101002; URL: https://doi.org/10.1016/j.lanepe.2024.101002 (fiorucci2024bileacidsbasedtherapies pages 10-11).

Candidate therapeutics and outcomes (selected)
- UDCA: Widely used, but no evidence of delayed transplant or survival benefit in PSC (Oct 2024; Cells; https://doi.org/10.3390/cells13191650) (fiorucci2024bileacidsbasedtherapies pages 1-2).
- FXR agonists: Obeticholic acid, cilofexor, tropifexor under investigation in PSC; caution that FXR–FGF19 axis can suppress BA synthesis, and lower C4 correlates with worse outcomes, especially in advanced disease (Oct 2024; Cells; https://doi.org/10.3390/cells13191650) (fiorucci2024bileacidsbasedtherapies pages 9-10, fiorucci2024bileacidsbasedtherapies pages 10-11).
- FGF19 analogs: Aldafermin suppresses hydrophobic BAs in cholestasis and is being explored across cholestatic diseases (e.g., JHEP Rep. 2021, referenced within review) (fiorucci2024bileacidsbasedtherapies pages 26-27).
- ASBT/IBAT inhibitors: Maralixibat has been piloted (Hepatology Communications 2023) with biochemical effects; class continues in evaluation for PSC (fiorucci2024bileacidsbasedtherapies pages 26-27, fiorucci2024bileacidsbasedtherapies pages 10-11).
- PPAR agonists: Elafibranor and seladelpar are being evaluated in cholestatic disease contexts; mechanistic rationale via anti-inflammatory and metabolic pathways (fiorucci2024bileacidsbasedtherapies pages 1-2, fiorucci2024bileacidsbasedtherapies pages 10-11).
- norUDCA: Harnesses cholehepatic shunting; part of the bile-acid–centric therapeutic armamentarium under study in PSC (fiorucci2024bileacidsbasedtherapies pages 10-11).

Direct supporting quotes
- “Activation of the liver immune system by intestinal antigens… leading to NF-κB- and NLRP3-dependent generation of cytokines… including IL-6, IL-12, IL-1β, and TNF-α” (Oct 2024; Cells; DOI 10.3390/cells13191650) (fiorucci2024bileacidsbasedtherapies pages 2-4).
- “Lower C4 levels, indicating suppressed bile acid synthesis, are associated with worse clinical outcomes… UDCA did not change C4” (Oct 2024; Cells; DOI 10.3390/cells13191650) (fiorucci2024bileacidsbasedtherapies pages 9-10).
- “CD1d is downregulated in PSC and PBC… bile from PSC patients contains MAIT antigens… anti-MR1 blocking antibody attenuated activation of MAIT cells” (Sep 2025; Hepatology; DOI 10.1097/hep.0000000000001093) (jalansakrikar2025centralrolefor pages 17-18).

Limitations
Where possible, 2023–2024 sources were prioritized; several authoritative mechanistic insights (MAIT/CD1d/MR1 and epigenetic–senescence programs) derive from a 2025 Hepatology review synthesizing recent primary studies, included here due to its comprehensive, expert nature and lack of equally detailed 2023–2024 alternatives in the current evidence set (jalansakrikar2025centralrolefor pages 17-18, jalansakrikar2025centralrolefor pages 6-7).

Summary
PSC pathogenesis arises from convergent immune, epithelial, stromal, and bile-acid–microbiome mechanisms. Gut-primed lymphocytes home to the liver; cholangiocytes enact immune and senescence programs reinforced by epigenetic remodeling; ductular reaction and portal mesenchyme crosstalk drive periductal fibrosis; and altered bile-acid receptor signaling intersects with dysbiosis to perpetuate injury. Genetic predisposition in HLA and non-HLA immune loci frames susceptibility. Therapeutics target bile-acid pathways (FXR–FGF19, TGR5, ASBT), metabolic and inflammatory axes (PPAR), and microbiome modulation, with ongoing efforts to align mechanism with disease stage to avoid deleterious over-suppression of BA synthesis in advanced disease (fiorucci2024bileacidsbasedtherapies pages 9-10, fiorucci2024bileacidsbasedtherapies pages 1-2, fiorucci2024bileacidsbasedtherapies pages 2-4, fiorucci2024bileacidsbasedtherapies pages 10-11, jalansakrikar2025centralrolefor pages 17-18).

References

1. (fiorucci2024bileacidsbasedtherapies pages 1-2): Stefano Fiorucci, Ginevra Urbani, Cristina Di Giorgio, Michele Biagioli, and Eleonora Distrutti. Bile acids-based therapies for primary sclerosing cholangitis: current landscape and future developments. Cells, 13:1650, Oct 2024. URL: https://doi.org/10.3390/cells13191650, doi:10.3390/cells13191650. This article has 10 citations and is from a poor quality or predatory journal.

2. (fiorucci2024bileacidsbasedtherapies pages 2-4): Stefano Fiorucci, Ginevra Urbani, Cristina Di Giorgio, Michele Biagioli, and Eleonora Distrutti. Bile acids-based therapies for primary sclerosing cholangitis: current landscape and future developments. Cells, 13:1650, Oct 2024. URL: https://doi.org/10.3390/cells13191650, doi:10.3390/cells13191650. This article has 10 citations and is from a poor quality or predatory journal.

3. (wang2024molecularmechanismsof pages 6-8): Wei-Lu Wang, Haoran Lian, Yingyu Liang, Yongqin Ye, Paul Kwong Hang Tam, and Yan Chen. Molecular mechanisms of fibrosis in cholestatic liver diseases and regenerative medicine-based therapies. Cells, 13:1997, Dec 2024. URL: https://doi.org/10.3390/cells13231997, doi:10.3390/cells13231997. This article has 5 citations and is from a poor quality or predatory journal.

4. (jalansakrikar2025centralrolefor pages 17-18): Nidhi Jalan-Sakrikar, Maria Eugenia Guicciardi, Steven P. O’Hara, Adiba Azad, Nicholas F. LaRusso, Gregory J. Gores, and Robert C. Huebert. Central role for cholangiocyte pathobiology in cholestatic liver diseases. Hepatology, Sep 2025. URL: https://doi.org/10.1097/hep.0000000000001093, doi:10.1097/hep.0000000000001093. This article has 20 citations and is from a highest quality peer-reviewed journal.

5. (jalansakrikar2025centralrolefor pages 6-7): Nidhi Jalan-Sakrikar, Maria Eugenia Guicciardi, Steven P. O’Hara, Adiba Azad, Nicholas F. LaRusso, Gregory J. Gores, and Robert C. Huebert. Central role for cholangiocyte pathobiology in cholestatic liver diseases. Hepatology, Sep 2025. URL: https://doi.org/10.1097/hep.0000000000001093, doi:10.1097/hep.0000000000001093. This article has 20 citations and is from a highest quality peer-reviewed journal.

6. (fiorucci2024bileacidsbasedtherapies pages 4-5): Stefano Fiorucci, Ginevra Urbani, Cristina Di Giorgio, Michele Biagioli, and Eleonora Distrutti. Bile acids-based therapies for primary sclerosing cholangitis: current landscape and future developments. Cells, 13:1650, Oct 2024. URL: https://doi.org/10.3390/cells13191650, doi:10.3390/cells13191650. This article has 10 citations and is from a poor quality or predatory journal.

7. (fiorucci2024bileacidsbasedtherapies pages 9-10): Stefano Fiorucci, Ginevra Urbani, Cristina Di Giorgio, Michele Biagioli, and Eleonora Distrutti. Bile acids-based therapies for primary sclerosing cholangitis: current landscape and future developments. Cells, 13:1650, Oct 2024. URL: https://doi.org/10.3390/cells13191650, doi:10.3390/cells13191650. This article has 10 citations and is from a poor quality or predatory journal.

8. (fiorucci2024bileacidsbasedtherapies pages 10-11): Stefano Fiorucci, Ginevra Urbani, Cristina Di Giorgio, Michele Biagioli, and Eleonora Distrutti. Bile acids-based therapies for primary sclerosing cholangitis: current landscape and future developments. Cells, 13:1650, Oct 2024. URL: https://doi.org/10.3390/cells13191650, doi:10.3390/cells13191650. This article has 10 citations and is from a poor quality or predatory journal.

9. (fiorucci2024bileacidsbasedtherapies pages 26-27): Stefano Fiorucci, Ginevra Urbani, Cristina Di Giorgio, Michele Biagioli, and Eleonora Distrutti. Bile acids-based therapies for primary sclerosing cholangitis: current landscape and future developments. Cells, 13:1650, Oct 2024. URL: https://doi.org/10.3390/cells13191650, doi:10.3390/cells13191650. This article has 10 citations and is from a poor quality or predatory journal.