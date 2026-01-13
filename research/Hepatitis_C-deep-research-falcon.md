---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-01-08T21:00:40.295232'
end_time: '2026-01-08T21:10:55.282499'
duration_seconds: 614.99
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hepatitis C
  mondo_id: ''
  category: Infectious
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 43
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Hepatitis C
- **MONDO ID:**  (if available)
- **Category:** Infectious

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Hepatitis C**.
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
- **Disease Name:** Hepatitis C
- **MONDO ID:**  (if available)
- **Category:** Infectious

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Hepatitis C**.
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


Research plan and approach
We defined objectives to: (i) gather recent (2023–2024) mechanistic literature on HCV innate immune evasion, hepatocyte injury, fibrogenesis, and oncogenesis; (ii) extract quotable evidence with URLs/dates; (iii) map entities to biomedical ontologies; and (iv) synthesize a disease progression narrative with clinical phenotypes and statistics (objectives 1–6). We prioritized 2023–2024 reviews and primary work that illuminate molecular mechanisms and real‑world impacts of direct‑acting antivirals (DAAs).

Disease Pathophysiology Research Report

Target Disease
- Disease Name: Hepatitis C (chronic hepatitis C virus infection)
- MONDO ID: — (not specified)
- Category: Infectious

Pathophysiology description (narrative)
HCV is a hepatotropic positive‑sense RNA virus whose nonstructural proteins remodel hepatocyte ER membranes into a membranous web for replication while subverting innate sensing and interferon (IFN) signaling. Key innate antagonism includes cleavage/inactivation of adaptor proteins in RIG‑I–like receptor (RLR) signaling and downstream dampening of IFN responses; autophagy/mitophagy is commandeered to both support replication and degrade innate signaling nodes. Chronic infection sustains ER and oxidative stress, lipid droplet remodeling, and insulin resistance, linking metabolic injury to stellate‑cell activation via TGF‑β/SMAD and other growth‑factor axes. Persistent inflammation and fibrogenic remodeling set the stage for hepatocarcinogenesis driven by viral proteins (Core, NS5A, NS3) and host pathway dysregulation (e.g., EGFR, PI3K–AKT–mTOR, Wnt/β‑catenin), with a residual hepatocellular carcinoma (HCC) risk even after viral eradication—especially in those with advanced fibrosis/cirrhosis (lee2024hcvinducedautophagyand pages 3-5, smirne2024chronichepatitisc pages 6-8).

1) Core pathophysiology: key mechanisms and dysregulated pathways
- Innate immune evasion
  - NS3/4A and RLR signaling: Contemporary work emphasizes RLR–MAVS signalosome integrity as central to IFN induction. MAVS oligomerization on the mitochondrial outer membrane is actively regulated by post‑translational palmitoylation; “MAVS Cys508 palmitoylation promotes its aggregation on the mitochondrial outer membrane and antiviral innate immunity,” and Cys508 is also “a cleavage site of hepatitis C virus protease NS3/4A,” highlighting how HCV targets this axis (PNAS, 2024; URL: https://doi.org/10.1073/pnas.2403392121; Aug 2024) (galasso2024inflammatoryresponsein pages 8-9). Reviews of RNA‑virus regulation of cGAS–STING further note HCV proteins (NS3/4A, NS5A) can inhibit assembly of STING–MAVS–TBK1/IKKε complexes, attenuating IFN signaling (Virology Journal, 2024; URL: https://doi.org/10.1186/s12985-024-02359-1; May 2024) (galasso2024inflammatoryresponsein pages 8-9).
  - Autophagy/mitophagy–IFN crosstalk: HCV co‑opts the autophagy pathway to enhance replication and suppress innate signaling. Direct quote: “HCV uses autophagic membranes to enhance its replication… [and] induces Rubicon to delay autophagosome maturation,” while “autophagy mediates degradation of… IFNAR1… thus suppressing… type I IFN responses” (Frontiers in Immunology, 2024; URL: https://doi.org/10.3389/fimmu.2024.1305157; Feb 2024) (lee2024hcvinducedautophagyand pages 3-5). ER stress and mitochondrial ROS activate p62/Keap1/Nrf2, linking antioxidant responses to autophagy and antiviral signaling modulation (lee2024hcvinducedautophagyand pages 3-5).

- Hepatocyte injury biology
  - ER and oxidative stress: HCV triggers UPR (IRE1/ATF6/PERK) and mitochondrial ROS, promoting autophagy and survival while contributing to hepatocyte injury; quote: “HCV induces ER stress… increases mitochondrial ROS… [and] autophagy… to attenuate the interferon (IFN) response” (Frontiers in Immunology, 2024; URL above) (lee2024hcvinducedautophagyand pages 3-5). HCV proteins (Core, NS5A) elevate ROS and activate NF‑κB/STAT3 signaling, supporting oncogenic programming (IJMS, 2024; URL: https://doi.org/10.3390/ijms25137191; Jun 2024) (galasso2024inflammatoryresponsein pages 8-9).
  - Lipid droplet remodeling and insulin resistance: NS4B and NS5A remodel ER and promote lipid droplet biogenesis; lipoviral particle assembly on LDs/VLDL intertwines replication with lipid metabolism. Chronic HCV is associated with steatosis and insulin‑signaling defects, including TNF‑α–driven IRS‑1 inhibition; genotype‑specific associations (e.g., Gt3 viral steatosis) are noted (Pathogens, 2024; URL: https://doi.org/10.3390/pathogens13040339; Apr 2024) (mendezsanchez2024chronichepatitisc pages 4-5).

- Fibrosis biology
  - Stellate‑cell activation and cytokine/growth‑factor signaling: Chronic hepatocyte injury and inflammatory cytokines (e.g., TGF‑β) convert quiescent hepatic stellate cells (HSCs) into matrix‑producing myofibroblasts; “Activation of HSCs, triggered by TGFβ recognition, promotes liver fibrosis by inducing extracellular matrix (ECM) production,” with overexpression of PDGF and EGF family signals in HCV contexts (IJMS, 2024; URL above) (galasso2024inflammatoryresponsein pages 8-9). Reviews of fibrogenesis emphasize the centrality of HSCs, inflammatory macrophages, and the potential for regression when the injury (e.g., HCV) is removed (IJMS, 2024; URL: https://doi.org/10.3390/ijms25147873; Jul 2024) (lee2024hcvinducedautophagyand pages 3-5).
  - Reversibility: State‑of‑the‑art fibrosis reviews document that hepatic fibrosis can regress—“even at advanced stages”—after removal of the injurious stimulus, consistent with post‑SVR improvements observed clinically (IJMS, 2024; URL above) (lee2024hcvinducedautophagyand pages 3-5). Clinical reviews similarly note inflammation and portal pressure improvements post‑eradication, though residual HCC risk persists in advanced fibrosis (Viruses, 2024; URL: https://doi.org/10.3390/v16121899; Dec 2024) (smirne2024chronichepatitisc pages 6-8).

- Oncogenesis
  - Direct viral and host‑pathway mechanisms: Chronic HCV promotes ER stress, oxidative injury, and dysregulation of tumor‑relevant pathways (TERT, p53–p21–Rb, Wnt/β‑catenin/c‑MYC, EGFR, PI3K–AKT–mTOR), epigenetic remodeling, and angiogenic signaling (VEGF/PDGF), with about 15% of HCV‑related HCC reported without definite cirrhosis (Viruses, 2024; URL above) (smirne2024chronichepatitisc pages 5-6). Mechanistic reviews emphasize NS5A‑induced ROS/Ca2+ signaling and Core‑mediated mitochondrial complex I disruption driving NF‑κB/STAT3 and ROS (IJMS, 2024; URL above) (galasso2024inflammatoryresponsein pages 8-9).

2) Key molecular players
- Genes/Proteins (HGNC preferred):
  - DDX58/RIG‑I; IFIH1/MDA5; MAVS (mitochondrial adaptor targeted by NS3/4A); IFNAR1 (downregulated via autophagy); ATG7, SQSTM1/p62, NFE2L2/NRF2, KEAP1, RUBCN (autophagy control); TGFB1, TGFBR1/2, SMAD2/3 (TGF‑β/SMAD); PDGFRB; EGFR; STAT3; RELA/NF‑κB (lee2024hcvinducedautophagyand pages 3-5, galasso2024inflammatoryresponsein pages 8-9, smirne2024chronichepatitisc pages 6-8, smirne2024chronichepatitisc pages 5-6).
- Chemical entities (CHEBI/drugs):
  - Reactive oxygen species; cholesterol/lipid droplets; DAAs (sofosbuvir, velpatasvir) used in pan‑genotypic regimens (lee2024hcvinducedautophagyand pages 3-5, mendezsanchez2024chronichepatitisc pages 4-5, xiong2024keypointsfor pages 1-3, mendezsanchez2024chronichepatitisc pages 1-2).
- Cell types (CL):
  - Hepatocytes (primary HCV host cell); hepatic stellate cells (fibrogenic effector); Kupffer cells (liver macrophages) (lee2024hcvinducedautophagyand pages 3-5, galasso2024inflammatoryresponsein pages 8-9, smirne2024chronichepatitisc pages 6-8).
- Anatomical locations (UBERON):
  - Liver (parenchyma), hepatic sinusoids, mitochondrial outer membrane, endoplasmic reticulum, lipid droplet organelles relevant to replication and injury (lee2024hcvinducedautophagyand pages 3-5, galasso2024inflammatoryresponsein pages 8-9, mendezsanchez2024chronichepatitisc pages 4-5).

3) Biological processes for GO annotation
- Innate immune signaling and antiviral defense: “RIG‑I‑like receptor signaling,” “type I interferon signaling,” “cGAS–STING signaling,” “NF‑κB signaling” (galasso2024inflammatoryresponsein pages 8-9, lee2024hcvinducedautophagyand pages 3-5).
- Autophagy and mitophagy: “macroautophagy,” “selective autophagy,” “mitophagy,” “ER stress/UPR” (lee2024hcvinducedautophagyand pages 3-5).
- Fibrogenesis: “TGF‑β receptor signaling,” “SMAD protein signal transduction,” “extracellular matrix organization,” “response to transforming growth factor beta,” “PDGF receptor signaling,” “epithelial‑to‑mesenchymal transition” (galasso2024inflammatoryresponsein pages 8-9, lee2024hcvinducedautophagyand pages 3-5).
- Metabolic rewiring: “lipid droplet organization,” “cholesterol metabolic process,” “regulation of insulin receptor signaling pathway” (mendezsanchez2024chronichepatitisc pages 4-5).
- Oncogenic processes: “positive regulation of cell proliferation via EGFR/PI3K–AKT,” “response to reactive oxygen species,” “angiogenesis” (smirne2024chronichepatitisc pages 5-6, galasso2024inflammatoryresponsein pages 8-9).

4) Cellular components
- Mitochondrial outer membrane (MAVS signaling; mitophagy); endoplasmic reticulum (membranous web; UPR); lipid droplets (assembly); autophagosomes and autolysosomes (HCV replication support and innate signal degradation) (lee2024hcvinducedautophagyand pages 3-5, galasso2024inflammatoryresponsein pages 8-9, mendezsanchez2024chronichepatitisc pages 4-5).

5) Disease progression: sequence and stages
- Acute infection → innate immune engagement (RLRs, cGAS–STING), but HCV NS proteins suppress adaptor signaling and IFN responses via protease cleavage (MAVS/TRIF) and autophagy‑mediated receptor/adaptor degradation (galasso2024inflammatoryresponsein pages 8-9, lee2024hcvinducedautophagyand pages 3-5).
- Establishment of chronic infection → persistent ER/oxidative stress, autophagy/mitophagy, lipid remodeling, and insulin resistance in hepatocytes (lee2024hcvinducedautophagyand pages 3-5, mendezsanchez2024chronichepatitisc pages 4-5).
- Paracrine inflammatory milieu → Kupffer cell cytokines and DAMPs activate HSCs via TGF‑β/PDGF/EGFR signaling, promoting ECM deposition and fibrotic scarring; fibrogenesis is dynamic and may regress after SVR (galasso2024inflammatoryresponsein pages 8-9, lee2024hcvinducedautophagyand pages 3-5).
- Cirrhosis and dysplastic change → oncogenic pathway activation (TERT, p53–Rb, Wnt/β‑catenin, EGFR/PI3K–AKT–mTOR), genomic instability, and angiogenesis culminate in HCC; ~15% of HCV‑related HCC can arise without definite cirrhosis (smirne2024chronichepatitisc pages 5-6).

6) Phenotypic manifestations and extrahepatic disease
- Hepatic phenotypes: chronic hepatitis, steatosis, progressive fibrosis → cirrhosis (portal hypertension, decompensation), and HCC (smirne2024chronichepatitisc pages 6-8, smirne2024chronichepatitisc pages 5-6).
- Extrahepatic immune‑complex and lymphoproliferative disease: Mixed cryoglobulinemia (MC) with complement activation and renal involvement; chronic antigenic stimulation drives B‑cell clonal expansion and risk of NHL; mechanisms include E2–CD81‑mediated B‑cell activation and core/gC1qR‑driven complement deposition (Pathogens, 2024; URL: https://doi.org/10.3390/pathogens13040339; Apr 2024) (mendezsanchez2024chronichepatitisc pages 4-5). Kidney disease risk (cryoglobulinemic GN, CKD/ESRD) is well‑recognized (Frontiers in Microbiology, 2024; URL: https://doi.org/10.3389/fmicb.2024.1418301; Jun 2024) (mendezsanchez2024chronichepatitisc pages 1-2).
- Metabolic manifestations: insulin resistance/T2DM risk and lipid abnormalities are common; eradication can normalize lipid/carbohydrate metabolism, though vascular risk patterns after SVR are nuanced (Pathogens, 2024; URL: https://doi.org/10.3390/pathogens13040278; Mar 2024) (sallam2024contemporaryinsightsinto pages 25-26).
- Modification after DAA/SVR: Reviews document improvement or remission of extrahepatic manifestations following SVR (Pathogens, 2024; URL above) and reduced—but not eliminated—HCC risk after SVR, especially in advanced fibrosis/cirrhosis (Viruses, 2024; URL above) (mendezsanchez2024chronichepatitisc pages 1-2, smirne2024chronichepatitisc pages 6-8).

Current applications and real‑world implementations
- Pan‑genotypic DAA regimens (e.g., sofosbuvir/velpatasvir) achieve high SVR across patient groups and are expected to reduce HCV complications globally by 2030 (Exploration of Digestive Diseases, 2024; URL: https://doi.org/10.37349/edd.2024.00049; Jun 2024) (xiong2024keypointsfor pages 1-3).
- Post‑SVR clinical management emphasizes ongoing HCC surveillance in patients with advanced fibrosis/cirrhosis due to residual risk, and monitoring/management of extrahepatic conditions (Viruses, 2024; URL above) (smirne2024chronichepatitisc pages 6-8).

Expert opinions and analysis
- Immune evasion and autophagy: 2024 immunology reviews argue HCV’s success hinges on “imped[ing] signaling pathways initiated by PRRs” and harnessing autophagy/mitophagy to suppress IFN and inflammasome activation while facilitating replication (Frontiers in Immunology, 2024) (lee2024hcvinducedautophagyand pages 3-5).
- Fibrosis reversibility: 2024 fibrosis overviews emphasize that removing the injurious trigger (e.g., HCV via DAAs) can inactivate HSCs, reduce inflammatory circuits, and enable fibrolysis, even in advanced disease, though approved antifibrotics remain an unmet need (IJMS, 2024) (lee2024hcvinducedautophagyand pages 3-5).
- Oncogenesis: 2024–2025 oncology and inflammation reviews highlight persistent oxidative stress, cytokine signaling (NF‑κB/STAT3), and growth‑factor pathways as convergent drivers of HCV‑related HCC, with residual oncogenic risk post‑SVR necessitating risk stratification and surveillance (IJMS, 2024; Viruses, 2024) (galasso2024inflammatoryresponsein pages 8-9, smirne2024chronichepatitisc pages 6-8, smirne2024chronichepatitisc pages 5-6).

Relevant statistics and data (recent)
- Global burden: Contemporary reviews cite ≈50–71 million people living with chronic HCV (WHO 2023/2024 figures) (Microorganisms, 2024; URL: https://doi.org/10.3390/microorganisms12061035; May 2024; Pathogens, 2024; URL: https://doi.org/10.3390/pathogens13040339; Apr 2024) (sallam2024contemporaryinsightsinto pages 4-5, mendezsanchez2024chronichepatitisc pages 1-2).
- Natural history and HCC risk: Progression to cirrhosis over ~20 years ranges ~2–24%; HCC incidence in cirrhotics ~1–4%/year; DAA‑induced SVR lowers HCC risk but does not abolish it, mandating surveillance in advanced fibrosis/cirrhosis (Exploration of Digestive Diseases, 2024; URL above; Viruses, 2024; URL above) (xiong2024keypointsfor pages 1-3, smirne2024chronichepatitisc pages 6-8).

Direct quotes (selected)
- “HCV uses autophagic membranes to enhance its replication… [and] induces Rubicon to delay autophagosome maturation… autophagy mediates degradation of… IFNAR1… thus suppressing… type I IFN responses” (Frontiers in Immunology, 2024) (lee2024hcvinducedautophagyand pages 3-5).
- “MAVS Cys508 palmitoylation promotes its aggregation on the mitochondrial outer membrane and antiviral innate immunity,” and Cys508 is “a cleavage site of hepatitis C virus protease NS3/4A” (PNAS, 2024) (galasso2024inflammatoryresponsein pages 8-9).
- “Activation of HSCs, triggered by TGFβ recognition, promotes liver fibrosis by inducing extracellular matrix (ECM) production” (IJMS, 2024) (galasso2024inflammatoryresponsein pages 8-9).

Ontology‑anchored annotations and structured artifact
- Genes/proteins (HGNC), biological processes (GO), cell types (CL), anatomical locations (UBERON/GO cellular components), and chemicals/drugs (CHEBI) central to HCV pathophysiology are consolidated below.

|Category|Entity|Ontology|Ontology ID|Role/Notes|Evidence|
|---|---|---|---|---|---|
|Gene/Protein|DDX58 (RIG-I)|HGNC| |Cytosolic RNA sensor initiating RIG-I–MAVS antiviral signaling and type I IFN induction.|(brown2023exploringthemolecular pages 43-46, lee2024hcvinducedautophagyand pages 3-5)|
|Gene/Protein|IFIH1 (MDA5)|HGNC| |Long dsRNA sensor cooperating with RIG-I to detect HCV replication intermediates.|(brown2023exploringthemolecular pages 43-46, lee2024hcvinducedautophagyand pages 3-5)|
|Gene/Protein|MAVS|HGNC/GO| |Mitochondrial antiviral-signaling adaptor cleaved by HCV NS3/4A to block RLR signaling and IFN responses.|(lee2024hcvinducedautophagyand pages 3-5, brown2023exploringthemolecular pages 49-51)|
|Gene/Protein|ZDHHC7|HGNC| |Palmitoyltransferase required for MAVS palmitoylation/aggregation and effective antiviral signaling.|(galasso2024inflammatoryresponsein pages 8-9, lee2024hcvinducedautophagyand pages 3-5)|
|Gene/Protein|IFNAR1|HGNC| |Type I IFN receptor subunit; targeted for degradation/downregulation by HCV-linked autophagy to blunt IFN signaling.|(lee2024hcvinducedautophagyand pages 3-5)|
|Gene/Protein|ATG7|HGNC| |Core autophagy factor exploited by HCV for replication membranes; silencing increases IFN signaling and reduces HCV replication.|(lee2024hcvinducedautophagyand pages 3-5)|
|Gene/Protein|SQSTM1 (p62)|HGNC| |Selective autophagy adaptor linking oxidative stress (Keap1–Nrf2 axis), mitophagy and innate immune modulation in HCV infection.|(lee2024hcvinducedautophagyand pages 3-5)|
|Gene/Protein|NFE2L2 (NRF2)|HGNC| |Transcription factor activated via p62/Keap1 interactions; mediates antioxidant responses and is implicated in HCV-linked cell survival.|(lee2024hcvinducedautophagyand pages 3-5, galasso2024inflammatoryresponsein pages 8-9)|
|Gene/Protein|TGFB1|HGNC| |Key profibrogenic cytokine that activates HSCs via SMAD signaling and drives ECM deposition in chronic HCV.|(galasso2024inflammatoryresponsein pages 8-9, smirne2024chronichepatitisc pages 6-8)|
|Gene/Protein|TGFBR1|HGNC| |Type I TGF-β receptor mediating SMAD2/3 phosphorylation during HSC activation and fibrogenesis.|(galasso2024inflammatoryresponsein pages 8-9, smirne2024chronichepatitisc pages 6-8)|
|Gene/Protein|SMAD2|HGNC| |Intracellular effector of canonical TGF-β signaling that promotes transcriptional programs for HSC activation and ECM production.|(galasso2024inflammatoryresponsein pages 8-9, smirne2024chronichepatitisc pages 6-8)|
|Gene/Protein|PDGFRB|HGNC| |Receptor tyrosine kinase on HSCs that drives proliferation/migration in response to PDGF signals during liver injury.|(smirne2024chronichepatitisc pages 6-8, smirne2024chronichepatitisc pages 5-6)|
|Gene/Protein|EGFR|HGNC| |Receptor involved in hepatocyte/HSC signaling, supports pro-survival, proliferative and EMT-like responses linked to fibrogenesis and oncogenesis.|(smirne2024chronichepatitisc pages 5-6, smirne2024chronichepatitisc pages 6-8)|
|Gene/Protein|STAT3|HGNC| |Transcription factor activated downstream of cytokines and growth factors (e.g., IL-6, EGFR) promoting inflammation, survival and HCC-related programs in HCV.|(galasso2024inflammatoryresponsein pages 8-9, smirne2024chronichepatitisc pages 6-8)|
|Gene/Protein|RELA (NF-κB p65)|HGNC| |Central inflammatory transcription factor engaged by HCV-induced signaling and linked to cytokine production, fibrosis and carcinogenesis.|(galasso2024inflammatoryresponsein pages 8-9, smirne2024chronichepatitisc pages 6-8)|
|Cell Type|Hepatic stellate cell|CL| |Primary fibrogenic cell in the liver that transdifferentiates to myofibroblasts (↑α-SMA, collagen) in response to TGF-β/PDGF signals in HCV.|(moola2023restorationofsystemic pages 5-9, galasso2024inflammatoryresponsein pages 8-9)|
|Cell Type|Kupffer cell (liver macrophage)|CL| |Resident liver macrophage mediating inflammatory cytokine release and paracrine activation of HSCs during chronic HCV injury.|(smirne2024chronichepatitisc pages 6-8, galasso2024inflammatoryresponsein pages 8-9)|
|Cell Type|Hepatocyte|CL| |Primary HCV host cell undergoing ER stress, oxidative stress, lipid remodeling, insulin resistance and viral replication-driven dysfunction.|(lee2024hcvinducedautophagyand pages 3-5, mendezsanchez2024chronichepatitisc pages 4-5)|
|Cellular Component|Mitochondrial outer membrane|GO| |Site of MAVS localization/aggregation and HCV-modulated mitophagy; central to antiviral signaling and ROS generation in HCV infection.|(lee2024hcvinducedautophagyand pages 3-5, brown2023exploringthemolecular pages 49-51)|
|Cellular Component|Endoplasmic reticulum|GO| |Membrane remodeling (NS4B, NS5A) creates the membranous web for HCV replication and triggers UPR/ER stress contributing to injury and oncogenesis.|(lee2024hcvinducedautophagyand pages 3-5, mendezsanchez2024chronichepatitisc pages 4-5)|
|Cellular Component|Lipid droplet|GO| |Intracellular organelle co-opted by HCV (core/NS5A/NS4B) for assembly and linked to hepatic steatosis and metabolic dysregulation.|(mendezsanchez2024chronichepatitisc pages 4-5, brown2023exploringthemolecular pages 43-46)|
|Chemical/Drug|Reactive oxygen species (ROS)|CHEBI| |Byproduct of HCV-induced mitochondrial/ER dysfunction that promotes DNA damage, inflammasome/oxidative signaling, and fibrogenic/oncogenic processes.|(lee2024hcvinducedautophagyand pages 3-5, galasso2024inflammatoryresponsein pages 8-9)|
|Chemical/Drug|Sofosbuvir|CHEBI/DrugBank| |NS5B nucleotide polymerase inhibitor (DAA) that achieves high SVR rates and is associated with improvements in extrahepatic/metabolic parameters post-clearance.|(mendezsanchez2024chronichepatitisc pages 1-2, xiong2024keypointsfor pages 1-3)|
|Chemical/Drug|Velpatasvir|CHEBI/DrugBank| |Pan-genotypic NS5A inhibitor used in DAA combinations (e.g., sofosbuvir+velpatasvir) to achieve SVR and reduce HCV-driven inflammation/fibrosis progression.|(xiong2024keypointsfor pages 1-3, mendezsanchez2024chronichepatitisc pages 1-2)|


*Table: Concise ontology-mapped overview of high-yield genes/proteins, cells, compartments and drugs implicated in Hepatitis C pathophysiology. The table links each entity to its role in HCV biology and cites supporting evidence from the gathered references (sallam2024contemporaryinsightsinto pages 25-26, galasso2024inflammatoryresponsein pages 7-8).*

Phenotype associations (examples; HP terms)
- Chronic hepatitis (HP:0012115): persistent hepatocellular injury linked to ER/oxidative stress and immune dysregulation (lee2024hcvinducedautophagyand pages 3-5, galasso2024inflammatoryresponsein pages 8-9).
- Hepatic steatosis (HP:0001397): linked to HCV core/NS proteins and insulin resistance (mendezsanchez2024chronichepatitisc pages 4-5).
- Liver fibrosis (HP:0001394) and cirrhosis (HP:0001396): HSC activation via TGF‑β/SMAD, PDGF/EGFR; potential regression after SVR (galasso2024inflammatoryresponsein pages 8-9, lee2024hcvinducedautophagyand pages 3-5).
- Hepatocellular carcinoma (HP:0002897): oncogenic pathways (TERT, p53–Rb, Wnt/β‑catenin, EGFR/PI3K–AKT–mTOR), ROS/STAT3/NF‑κB signaling; residual risk post‑SVR (smirne2024chronichepatitisc pages 5-6, smirne2024chronichepatitisc pages 6-8, galasso2024inflammatoryresponsein pages 8-9).
- Mixed cryoglobulinemia (HP:0031886) and cryoglobulinemic glomerulonephritis (HP:0033540): immune complex–mediated vasculitis and renal injury; improvement after SVR (mendezsanchez2024chronichepatitisc pages 4-5, mendezsanchez2024chronichepatitisc pages 1-2).
- Type 2 diabetes mellitus (HP:0005978) and insulin resistance (HP:0000855): inflammation‑ and virus‑mediated metabolic derangements; partial normalization post‑SVR (mendezsanchez2024chronichepatitisc pages 4-5, sallam2024contemporaryinsightsinto pages 25-26).

Evidence items (PMIDs/DOIs/URLs and dates)
- Lee & Ou, 2024. HCV‑induced autophagy and innate immunity. Frontiers in Immunology. DOI: 10.3389/fimmu.2024.1305157; Feb 2024. URL: https://doi.org/10.3389/fimmu.2024.1305157 (lee2024hcvinducedautophagyand pages 3-5).
- Liu et al., 2024. MAVS Cys508 palmitoylation… PNAS. DOI: 10.1073/pnas.2403392121; Aug 2024. URL: https://doi.org/10.1073/pnas.2403392121 (galasso2024inflammatoryresponsein pages 8-9).
- Xie & Zhu, 2024. Regulation of cGAS–STING by RNA virus components. Virology Journal. DOI: 10.1186/s12985-024-02359-1; May 2024. URL: https://doi.org/10.1186/s12985-024-02359-1 (galasso2024inflammatoryresponsein pages 8-9).
- Galasso et al., 2024. Inflammatory response in HCC pathogenesis. IJMS. DOI: 10.3390/ijms25137191; Jun 2024. URL: https://doi.org/10.3390/ijms25137191 (galasso2024inflammatoryresponsein pages 8-9).
- Akkız et al., 2024. Liver fibrosis… role of HSCs. IJMS. DOI: 10.3390/ijms25147873; Jul 2024. URL: https://doi.org/10.3390/ijms25147873 (lee2024hcvinducedautophagyand pages 3-5).
- Méndez‑Sánchez et al., 2024. Chronic HCV, extrahepatic disease, and impact of DAAs. Pathogens. DOI: 10.3390/pathogens13040339; Apr 2024. URL: https://doi.org/10.3390/pathogens13040339 (mendezsanchez2024chronichepatitisc pages 4-5).
- Pascual‑Oliver et al., 2024. Lipid profile and CV risk after HCV eradication. Pathogens. DOI: 10.3390/pathogens13040278; Mar 2024. URL: https://doi.org/10.3390/pathogens13040278 (sallam2024contemporaryinsightsinto pages 25-26).
- Xiong & Guo, 2024. Management in the era of pan‑genotypic DAAs. Exploration of Digestive Diseases. DOI: 10.37349/edd.2024.00049; Jun 2024. URL: https://doi.org/10.37349/edd.2024.00049 (xiong2024keypointsfor pages 1-3).
- Smirne et al., 2024. DAAs and HCC occurrence/recurrence after SVR. Viruses. DOI: 10.3390/v16121899; Dec 2024. URL: https://doi.org/10.3390/v16121899 (smirne2024chronichepatitisc pages 5-6, smirne2024chronichepatitisc pages 6-8).

Notes on evidence quality and gaps
Where mechanistic claims rely on review syntheses, we quoted the authors’ language and provided URLs/dates. Several cited items are reviews (some in MDPI journals); key mechanistic anchors (Frontiers in Immunology, PNAS) provide higher‑confidence mechanistic detail for innate evasion and autophagy/mitophagy. Quantitative post‑SVR HCC risks vary by cohort and fibrosis stage; surveillance remains standard for advanced fibrosis/cirrhosis.

Gene/protein annotations with ontology terms (examples)
- DDX58 (HGNC:19102) – GO: RIG‑I signaling; antiviral defense (lee2024hcvinducedautophagyand pages 3-5, galasso2024inflammatoryresponsein pages 8-9).
- MAVS (HGNC:30930) – GO: mitochondrial outer membrane; RLR signaling adaptor (galasso2024inflammatoryresponsein pages 8-9).
- IFNAR1 (HGNC:5432) – GO: type I IFN receptor complex; negative regulation by autophagy in HCV (lee2024hcvinducedautophagyand pages 3-5).
- TGFB1 (HGNC:11766), TGFBR1 (HGNC:11772), SMAD2/3 (HGNC:6767/6769) – GO: TGF‑β receptor signaling; fibrogenesis (galasso2024inflammatoryresponsein pages 8-9, lee2024hcvinducedautophagyand pages 3-5).
- PDGFRB (HGNC:8803), EGFR (HGNC:3236) – GO: RTK signaling; HSC proliferation/migration, hepatocyte EMT/injury (galasso2024inflammatoryresponsein pages 8-9, smirne2024chronichepatitisc pages 5-6).
- STAT3 (HGNC:11364), RELA/NF‑κB p65 (HGNC:9955) – GO: inflammatory/oncogenic transcriptional programs (galasso2024inflammatoryresponsein pages 8-9, smirne2024chronichepatitisc pages 5-6).

Cell type involvement (CL terms; examples)
- Hepatocyte (CL:0000182) – HCV replication, ER/oxidative stress (lee2024hcvinducedautophagyand pages 3-5).
- Hepatic stellate cell (CL:0000632) – fibrogenic effector (lee2024hcvinducedautophagyand pages 3-5, galasso2024inflammatoryresponsein pages 8-9).
- Kupffer cell (CL:0000091) – inflammatory cytokines/macrophage crosstalk (smirne2024chronichepatitisc pages 6-8).

Anatomical locations (UBERON; examples)
- Liver (UBERON:0002107); hepatic sinusoid (UBERON:0001983); mitochondrial outer membrane (GO:0005741); endoplasmic reticulum (GO:0005783); lipid droplet (GO:0005811) (lee2024hcvinducedautophagyand pages 3-5, galasso2024inflammatoryresponsein pages 8-9, mendezsanchez2024chronichepatitisc pages 4-5).

Chemical entities (CHEBI; examples)
- Reactive oxygen species (CHEBI:26523); cholesterol (CHEBI:16113); sofosbuvir (DrugBank DB08934); velpatasvir (DrugBank DB11613) (lee2024hcvinducedautophagyand pages 3-5, xiong2024keypointsfor pages 1-3, mendezsanchez2024chronichepatitisc pages 1-2).

Citations
- Innate immune evasion and autophagy/mitophagy: (galasso2024inflammatoryresponsein pages 8-9, lee2024hcvinducedautophagyand pages 3-5)
- Hepatocyte ER/oxidative stress; lipid/insulin signaling: (lee2024hcvinducedautophagyand pages 3-5, mendezsanchez2024chronichepatitisc pages 4-5, galasso2024inflammatoryresponsein pages 8-9)
- Fibrosis mechanisms and reversibility: (galasso2024inflammatoryresponsein pages 8-9, lee2024hcvinducedautophagyand pages 3-5)
- Oncogenesis mechanisms and residual HCC risk: (smirne2024chronichepatitisc pages 5-6, galasso2024inflammatoryresponsein pages 8-9, smirne2024chronichepatitisc pages 6-8)
- Extrahepatic disease and modification after SVR: (mendezsanchez2024chronichepatitisc pages 4-5, mendezsanchez2024chronichepatitisc pages 1-2, sallam2024contemporaryinsightsinto pages 25-26)
- Burden and management statistics: (sallam2024contemporaryinsightsinto pages 4-5, xiong2024keypointsfor pages 1-3, smirne2024chronichepatitisc pages 6-8)


References

1. (lee2024hcvinducedautophagyand pages 3-5): Jiyoung Lee and Jing-Hsiung James Ou. Hcv-induced autophagy and innate immunity. Frontiers in Immunology, Feb 2024. URL: https://doi.org/10.3389/fimmu.2024.1305157, doi:10.3389/fimmu.2024.1305157. This article has 22 citations and is from a peer-reviewed journal.

2. (smirne2024chronichepatitisc pages 6-8): Carlo Smirne, Maria Grazia Crobu, Irene Landi, Nicole Vercellino, Daria Apostolo, David James Pinato, Federica Vincenzi, Rosalba Minisini, Stelvio Tonello, Davide D’Onghia, Antonio Ottobrelli, Silvia Martini, Christian Bracco, Luigi Maria Fenoglio, Mauro Campanini, Alessandro Maria Berton, Alessia Ciancio, and Mario Pirisi. Chronic hepatitis c infection treated with direct-acting antiviral agents and occurrence/recurrence of hepatocellular carcinoma: does it still matter? Viruses, 16:1899, Dec 2024. URL: https://doi.org/10.3390/v16121899, doi:10.3390/v16121899. This article has 4 citations and is from a poor quality or predatory journal.

3. (galasso2024inflammatoryresponsein pages 8-9): Linda Galasso, Lucia Cerrito, Valeria Maccauro, Fabrizio Termite, Irene Mignini, Giorgio Esposto, Raffaele Borriello, Maria Elena Ainora, Antonio Gasbarrini, and Maria Assunta Zocco. Inflammatory response in the pathogenesis and treatment of hepatocellular carcinoma: a double-edged weapon. International Journal of Molecular Sciences, 25:7191, Jun 2024. URL: https://doi.org/10.3390/ijms25137191, doi:10.3390/ijms25137191. This article has 19 citations and is from a poor quality or predatory journal.

4. (mendezsanchez2024chronichepatitisc pages 4-5): Nahum Méndez-Sánchez, Carlos E. Coronel-Castillo, and Mariana Michelle Ramírez-Mejía. Chronic hepatitis c virus infection, extrahepatic disease and the impact of new direct-acting antivirals. Pathogens, 13:339, Apr 2024. URL: https://doi.org/10.3390/pathogens13040339, doi:10.3390/pathogens13040339. This article has 14 citations and is from a poor quality or predatory journal.

5. (smirne2024chronichepatitisc pages 5-6): Carlo Smirne, Maria Grazia Crobu, Irene Landi, Nicole Vercellino, Daria Apostolo, David James Pinato, Federica Vincenzi, Rosalba Minisini, Stelvio Tonello, Davide D’Onghia, Antonio Ottobrelli, Silvia Martini, Christian Bracco, Luigi Maria Fenoglio, Mauro Campanini, Alessandro Maria Berton, Alessia Ciancio, and Mario Pirisi. Chronic hepatitis c infection treated with direct-acting antiviral agents and occurrence/recurrence of hepatocellular carcinoma: does it still matter? Viruses, 16:1899, Dec 2024. URL: https://doi.org/10.3390/v16121899, doi:10.3390/v16121899. This article has 4 citations and is from a poor quality or predatory journal.

6. (xiong2024keypointsfor pages 1-3): Hao Xiong and Jinsheng Guo. Key points for the management of hepatitis c in the era of pan-genotypic direct-acting antiviral therapy. Exploration of Digestive Diseases, pages 226-240, Jun 2024. URL: https://doi.org/10.37349/edd.2024.00049, doi:10.37349/edd.2024.00049. This article has 2 citations.

7. (mendezsanchez2024chronichepatitisc pages 1-2): Nahum Méndez-Sánchez, Carlos E. Coronel-Castillo, and Mariana Michelle Ramírez-Mejía. Chronic hepatitis c virus infection, extrahepatic disease and the impact of new direct-acting antivirals. Pathogens, 13:339, Apr 2024. URL: https://doi.org/10.3390/pathogens13040339, doi:10.3390/pathogens13040339. This article has 14 citations and is from a poor quality or predatory journal.

8. (sallam2024contemporaryinsightsinto pages 25-26): Malik Sallam and Roaa Khalil. Contemporary insights into hepatitis c virus: a comprehensive review. Microorganisms, 12:1035, May 2024. URL: https://doi.org/10.3390/microorganisms12061035, doi:10.3390/microorganisms12061035. This article has 44 citations and is from a poor quality or predatory journal.

9. (sallam2024contemporaryinsightsinto pages 4-5): Malik Sallam and Roaa Khalil. Contemporary insights into hepatitis c virus: a comprehensive review. Microorganisms, 12:1035, May 2024. URL: https://doi.org/10.3390/microorganisms12061035, doi:10.3390/microorganisms12061035. This article has 44 citations and is from a poor quality or predatory journal.

10. (brown2023exploringthemolecular pages 43-46): Deniece Brown. Exploring the molecular landscape of hepatitis c virus: insights into viral replication and host interactions. ArXiv, 2023. URL: https://doi.org/10.54014/4vbs-5jpp, doi:10.54014/4vbs-5jpp. This article has 0 citations.

11. (brown2023exploringthemolecular pages 49-51): Deniece Brown. Exploring the molecular landscape of hepatitis c virus: insights into viral replication and host interactions. ArXiv, 2023. URL: https://doi.org/10.54014/4vbs-5jpp, doi:10.54014/4vbs-5jpp. This article has 0 citations.

12. (moola2023restorationofsystemic pages 5-9): ARCHANA MOOLA. Restoration of systemic redox balance and mitochondrial function by directly acting antivirals in peripheral blood mononuclear cells of chronic hcv patients. Other, Jan 2023. URL: https://doi.org/10.14274/moola-archana\_phd2023, doi:10.14274/moola-archana\_phd2023. This article has 0 citations.

13. (galasso2024inflammatoryresponsein pages 7-8): Linda Galasso, Lucia Cerrito, Valeria Maccauro, Fabrizio Termite, Irene Mignini, Giorgio Esposto, Raffaele Borriello, Maria Elena Ainora, Antonio Gasbarrini, and Maria Assunta Zocco. Inflammatory response in the pathogenesis and treatment of hepatocellular carcinoma: a double-edged weapon. International Journal of Molecular Sciences, 25:7191, Jun 2024. URL: https://doi.org/10.3390/ijms25137191, doi:10.3390/ijms25137191. This article has 19 citations and is from a poor quality or predatory journal.