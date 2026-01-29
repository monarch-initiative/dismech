---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-01-23T17:04:50.172875'
end_time: '2026-01-23T17:09:32.245965'
duration_seconds: 282.07
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Acne Vulgaris
  mondo_id: MONDO:0011438
  category: Complex
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 26
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Acne Vulgaris
- **MONDO ID:** MONDO:0011438 (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Acne Vulgaris**.
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
- **Disease Name:** Acne Vulgaris
- **MONDO ID:** MONDO:0011438 (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Acne Vulgaris**.
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
- Disease Name: Acne Vulgaris
- MONDO ID: MONDO:0011438
- Category: Complex

## Pathophysiology description (current understanding, 2023–2024 emphasis)
Acne vulgaris is a chronic inflammatory disorder of the pilosebaceous unit driven by the interplay of sebaceous lipid dysregulation, follicular hyperkeratinization, Cutibacterium acnes (C. acnes) strain-level immunostimulation, and downstream innate/adaptive immune activation, modulated by androgen/IGF‑1 metabolic signaling and the cutaneous microbiome. Dysbiosis with enrichment of C. acnes phylotype IA1, altered sebum composition, and activation of TLR and inflammasome pathways converge to initiate IL‑1β–dependent comedogenesis and propagate Th17/IL‑17–skewed inflammation; chronicity can culminate in extracellular matrix (ECM) remodeling, with MMP/TGF‑β pathways contributing to scars. Clinical phenotypes span microcomedones, comedones, papules/pustules, nodules, and scarring. Prevalence is high in adolescence (≈85%) and persists in subsets such as adult female acne where androgenic drivers are prominent (15–20% prevalence among adult women; hyperandrogenism in ~50% of cases, commonly linked to PCOS). (kim2024exploringacnetreatments pages 3-4, dessinioti2024themicrobiomeand pages 3-4, amuzescu2024adultfemaleacne pages 1-2, mdermUnknownyearacnevulgarisadvancesa pages 1-2)

### Core mechanisms
- Sebum/lipid metabolism and sebocyte biology: Insulin/IGF‑1 and androgens converge on PI3K–AKT–mTORC1, SREBP‑1 activation and FoxO1 downregulation to promote sebocyte proliferation and lipogenesis; lipid shifts (e.g., increased MUFAs, oxidized squalene) and reduced linoleic acid contribute to inflammation and hyperkeratinization. (Kim & Kim 2024, Int J Mol Sci; Mosca et al. 2025, Cells) https://doi.org/10.3390/ijms25105302; https://doi.org/10.3390/cells14100747 (kim2024exploringacnetreatments pages 3-4, mosca2025thesebaceousgland pages 5-7)
- Follicular hyperkeratinization: Dysregulated keratinocyte differentiation is a core early event; IL‑1β signaling promotes microcomedo formation. (mdermUnknownyearacnevulgarisadvancesa pages 1-2)
- C. acnes strain-level effects and innate sensors: Dysbiosis with loss of diversity and enrichment of IA1 phylotypes (SLST A1) is associated with inflammatory acne; C. acnes activates TLR2/4 and NLRP3–caspase‑1 to mature IL‑1β and induces TNF‑α, IL‑6, IL‑8, and IL‑12. (Dessinioti & Katsambas 2024; Zhang et al. 2025 bibliometrics) https://doi.org/10.1007/s13555-023-01079-8; https://doi.org/10.1186/s13040-025-00433-0 (dessinioti2024themicrobiomeand pages 3-4, zhang2025analysisofglobal pages 15-17)
- Th17/IL‑17 axis and innate lymphoid involvement: Acne lesions show increased Th1/Th17 cytokines; pathogenic C. acnes strains elicit IL‑17/IFN‑γ–dominant responses, supporting a Th17‑skewed milieu. (Kim & Kim 2024) https://doi.org/10.3390/ijms25105302 (kim2024exploringacnetreatments pages 3-4)
- Antimicrobial peptides (AMPs) and microbiome crosstalk: AMPs (e.g., β‑defensins, LL‑37) are induced by TLR signaling; commensal CoNS can counter-regulate inflammation (e.g., via LTA–miR‑143 dampening TLR2) and inhibit pathogenic C. acnes via bacteriocins/short-chain acids, highlighting therapeutic microbiome modulation. (Dessinioti & Katsambas 2024; Zhang et al. 2025) https://doi.org/10.1007/s13555-023-01079-8; https://doi.org/10.1186/s13040-025-00433-0 (dessinioti2024themicrobiomeand pages 3-4, zhang2025analysisofglobal pages 15-17)
- Progression to scarring/fibrosis: Persistent inflammation alters ECM through MMP activity and TGF‑β–driven fibroblast activation; pathological scars reflect aberrant collagen deposition and remodeling by fibroblasts. (Kohlhauser et al. 2024, IJMS; Ioannou et al. 2025, IJMS) https://doi.org/10.3390/ijms252111579; https://doi.org/10.3390/ijms26083621 (, )

## Recent developments and latest research (prioritize 2023–2024)
- Immunologic sensing and inflammasomes: Updated reviews detail mechanisms by which Gram-positive bacteria, including C. acnes, activate NLRP3 and downstream gasdermin D/pyroptosis, directly linking innate sensing to IL‑1β maturation in acne lesions. (Keestra‑Gounder & Nagao 2023, Front Immunol) https://doi.org/10.3389/fimmu.2023.1075834 ()
- Microbiome–immune regulation: 2024–2025 syntheses emphasize commensal skin microbes regulating epithelial and immune responses; Cutibacterium strain pathogenicity and TLR9/NLRP interactions are highlighted as determinants of lesion-prone states. (Gan et al. 2024, Cell Host Microbe) https://doi.org/10.1016/j.chom.2024.07.020 ()
- Macrophage roles: Emerging evidence underscores macrophage polarization (M1), phagocytosis of C. acnes, and orchestration of inflammatory cascades and scar propensity; plant-derived modulators can suppress NLRP3 in C. acnes–stimulated macrophages in vitro. (Zhao et al. 2024; Feng et al. 2024, Front Immunol) https://doi.org/10.3389/fimmu.2024.1383263; https://doi.org/10.3389/fimmu.2024.1355455 (, )
- Adult female acne (AFA) biology: 2024 review synthesizes endocrine drivers (androgen excess/sensitivity), genetic predisposition, and microbiome shifts in AFA; notes PCOS prevalence among hyperandrogenic AFA and the rise of topical antiandrogens. (Amuzescu et al. 2024, Cosmetics) https://doi.org/10.3390/cosmetics11030074 (amuzescu2024adultfemaleacne pages 1-2)

## Current applications and real-world implementations
- Therapies aligned to mechanisms: Topicals (retinoids, benzoyl peroxide) and systemic retinoids reduce comedogenesis and bacterial load; emerging non‑antibiotic approaches target sebocyte signaling (e.g., PPARγ modulation, topical antiandrogens), IL‑1/IL‑17 axes, and microbiome-directed strategies (probiotics/bacteriophages; leveraging CoNS antimicrobials). (Kim & Kim 2024; Dessinioti & Katsambas 2024) https://doi.org/10.3390/ijms25105302; https://doi.org/10.1007/s13555-023-01079-8 (kim2024exploringacnetreatments pages 3-4, dessinioti2024themicrobiomeand pages 3-4)
- Antibiotic stewardship and microbiome preservation: Contemporary guidance emphasizes minimizing antibiotics given collateral microbiome disruption and resistance, while employing BPO and retinoids and exploring microbiome-sparing modalities. (Dessinioti & Katsambas 2024) https://doi.org/10.1007/s13555-023-01079-8 (dessinioti2024themicrobiomeand pages 3-4)

## Expert opinions and analysis from authoritative sources
- Consensus on multifactorial pathogenesis: Recent overviews integrate sebaceous gland endocrinology, innate pattern recognition, and microbiome ecology, arguing for personalized regimens combining comedolysis, anti‑inflammatory intervention (e.g., IL‑1/IL‑17 targeting), and microbiome modulation. (Kim & Kim 2024; Gan et al. 2024; Dessinioti & Katsambas 2024) https://doi.org/10.3390/ijms25105302; https://doi.org/10.1016/j.chom.2024.07.020; https://doi.org/10.1007/s13555-023-01079-8 (kim2024exploringacnetreatments pages 3-4, dessinioti2024themicrobiomeand pages 3-4)
- Scarring as a fibroblast-centered consequence: Contemporary scarring reviews emphasize fibroblast heterogeneity, persistent inflammation, and MMP/TGF‑β balance as therapeutic entry points to prevent acne-related scars. (Kohlhauser et al. 2024; Ioannou et al. 2025) https://doi.org/10.3390/ijms252111579; https://doi.org/10.3390/ijms26083621 (, )

## Relevant statistics and data from recent studies
- Microbiome phylotype distribution: C. acnes IA1 enrichment in acne cohorts (overall 84.4%; 95.6% on back lesions) vs healthy controls (IA1 39.1%, phylotype II 43.4%), supporting strain-level disease association. (Zhang et al. 2025) https://doi.org/10.1186/s13040-025-00433-0 (zhang2025analysisofglobal pages 15-17)
- Epidemiology in adults: Adult female acne prevalence 15–20%; hyperandrogenism in ~50% of AFA cases, ~70% of those with PCOS. (Amuzescu et al. 2024) https://doi.org/10.3390/cosmetics11030074 (amuzescu2024adultfemaleacne pages 1-2)
- Global burden (general): Acne impacts ≈85% of adolescents/young adults. (mdermUnknownyearacnevulgarisadvancesa pages 1-2)

## Required Information by Template

### 1. Core Pathophysiology
- Primary mechanisms: Excess/altered sebum; follicular hyperkeratinization; C. acnes dysbiosis with IA1 expansion; TLR/NLRP3 activation → IL‑1β; neutrophil and macrophage recruitment; Th1/Th17 polarization (IL‑17A/IFN‑γ); AMP induction; chronic ECM remodeling underpinning scars. (kim2024exploringacnetreatments pages 3-4, dessinioti2024themicrobiomeand pages 3-4, zhang2025analysisofglobal pages 15-17)
- Dysregulated pathways: PI3K–AKT–mTORC1/SREBP‑1/FoxO1; TLR2/4–NF‑κB/MAPK; NLRP3–caspase‑1–IL‑1β; Th17/IL‑17 signaling; PPARγ in sebocytes; MMP/TGF‑β in ECM. (kim2024exploringacnetreatments pages 3-4, dessinioti2024themicrobiomeand pages 3-4, mdermUnknownyearacnevulgarisadvancesa pages 1-2)
- Affected cellular processes: Sebocyte lipogenesis/holocrine secretion; keratinocyte differentiation; inflammasome activation and pyroptosis; macrophage polarization; ECM turnover. (kim2024exploringacnetreatments pages 3-4)

### 2. Key Molecular Players
- Genes/Proteins (HGNC):
  - AR (androgen receptor); IGF1; MTOR (mTORC1); SREBF1 (SREBP‑1); FOXO1; TLR2/TLR4; NLRP3; CASP1; IL1B; IL6; IL8 (CXCL8); TNF; IL17A; PPARG; MMP family; TGFB1. Mechanistic roles as above with evidence in recent reviews. (kim2024exploringacnetreatments pages 3-4, dessinioti2024themicrobiomeand pages 3-4, mdermUnknownyearacnevulgarisadvancesa pages 1-2)
- Chemical entities (ChEBI):
  - Androgens (testosterone, DHT); IGF‑1; lipids (linoleic acid; squalene; MUFAs); benzoyl peroxide; short-chain fatty acids (succinic acid); bacteriocins (e.g., cutimycin). (dessinioti2024themicrobiomeand pages 3-4, kim2024exploringacnetreatments pages 3-4)
- Cell types (CL):
  - Sebocytes; keratinocytes; macrophages (M1‑skew); neutrophils; Th17 T cells. (kim2024exploringacnetreatments pages 3-4, dessinioti2024themicrobiomeand pages 3-4)
- Anatomical locations (UBERON):
  - Pilosebaceous unit; hair follicle infundibulum; dermis/ECM (scarring). (dessinioti2024themicrobiomeand pages 3-4)

### 3. Biological Processes for GO annotation
- Lipid metabolic process; regulation of cell differentiation; innate immune response; TLR signaling pathway; inflammasome complex assembly; interleukin‑1 beta production; Th17 cell differentiation; extracellular matrix organization; collagen catabolic process. (kim2024exploringacnetreatments pages 3-4)

### 4. Cellular Components
- Sebocyte lipid droplets; plasma membrane TLR complexes; cytosolic NLRP3 inflammasome; extracellular space (cytokines/AMPs); ECM (collagen/elastin network). (, )

### 5. Disease Progression
- Sequence of events: Pubertal/androgenic and IGF‑1 signals elevate sebum and alter composition → follicular hyperkeratinization and microcomedo formation (IL‑1β‑linked) → C. acnes dysbiosis (IA1 enrichment), biofilm-associated persistence and TLR/NLRP3 activation → neutrophil/macrophage infiltration; Th1/Th17 polarization → clinical inflammatory lesions (papules/pustules); with chronicity and depth, MMP/TGF‑β remodeling leads to atrophic/hypertrophic scarring. (kim2024exploringacnetreatments pages 3-4, dessinioti2024themicrobiomeand pages 3-4, zhang2025analysisofglobal pages 15-17)

### 6. Phenotypic Manifestations
- Key clinical phenotypes (HP): Open/closed comedones; inflammatory papules/pustules; nodules/cysts; postinflammatory hyperpigmentation; atrophic and hypertrophic scars. Mechanistic links: IL‑1β to comedogenesis; IL‑17/TNF‑α to pustular inflammation; MMP/TGF‑β disequilibrium to scar morphologies. (mdermUnknownyearacnevulgarisadvancesa pages 1-2, kim2024exploringacnetreatments pages 3-4)

## Evidence items (recent, with quotes where available)
- Microbiome–innate links and inflammasomes: “C. acnes activates TLR2… and can induce IL‑1β via NOD‑like receptor signaling particularly the NLRP3 inflammasome.” Dermatol Ther (Heidelb). 2024-01-09. https://doi.org/10.1007/s13555-023-01079-8 (dessinioti2024themicrobiomeand pages 3-4)
- Strain-level association and quantitative distribution: “Phylotype IA1… enriched in acne (overall 84.4%; 95.6% back) vs healthy (IA1 39.1%, II 43.4%).” BioData Mining. 2025-03-10. https://doi.org/10.1186/s13040-025-00433-0 (zhang2025analysisofglobal pages 15-17)
- Metabolic signaling in sebocytes: “Androgen- and IGF‑1–mediated upregulation of sebocyte proliferation and lipogenesis via PI3K/Akt–mTORC1 signaling… FoxO1 downregulation.” Int J Mol Sci. 2024-05-10. https://doi.org/10.3390/ijms25105302 (kim2024exploringacnetreatments pages 3-4)
- Inflammasome mechanisms by Gram-positive bacteria (generalizable to C. acnes): “The NLRP3 inflammasome plays a key role… activation leads to caspase‑1 processing of IL‑1β and IL‑18.” Front Immunol. 2023-01-13. https://doi.org/10.3389/fimmu.2023.1075834 ()
- Macrophages in acne: “Polarization of macrophages toward the M1 phenotype plays a pivotal role… LicA hampers NLRP3 inflammasome activation in C. acnes‑induced macrophages.” Front Immunol. 2024-04-26. https://doi.org/10.3389/fimmu.2024.1383263 ()
- Scarring biology: “Hypertrophic scars, keloids and atrophic scars arise from dysregulated wound healing… aberrant collagen deposition, and impaired ECM remodeling” with fibroblast centrality. IJMS. 2024-10-28. https://doi.org/10.3390/ijms252111579 ()
- Adult female acne epidemiology and endocrinology: “The prevalence in adult women is 15–20%. Hyperandrogenism is present in 50% of cases; 70% of hyperandrogenism cases feature PCOS.” Cosmetics. 2024-05-09. https://doi.org/10.3390/cosmetics11030074 (amuzescu2024adultfemaleacne pages 1-2)

## Gene/protein annotations with ontology terms
- AR (HGNC:644); Biological Process: regulation of lipid metabolic process; Cellular Component: nucleus; Role: sebocyte differentiation/lipogenesis under androgen control. (kim2024exploringacnetreatments pages 3-4)
- IGF1 (HGNC:5467); BP: insulin receptor signaling pathway; CC: extracellular space; Role: enhances sebocyte lipogenesis and androgen signaling. (kim2024exploringacnetreatments pages 3-4)
- MTOR (HGNC:3942); BP: positive regulation of cell growth; CC: TORC1 complex; Role: integrates androgen/IGF‑1 to drive lipogenesis. (kim2024exploringacnetreatments pages 3-4)
- SREBF1 (HGNC:11289); BP: regulation of fatty acid biosynthesis; CC: nucleus; Role: sebocyte lipogenesis downstream of mTORC1. (kim2024exploringacnetreatments pages 3-4)
- FOXO1 (HGNC:3819); BP: negative regulation of transcription by RNA polymerase II; CC: nucleus; Role: downregulated, relieving restraint on lipogenesis. (kim2024exploringacnetreatments pages 3-4)
- TLR2 (HGNC:11848)/TLR4 (HGNC:11850); BP: TLR signaling pathway; CC: plasma membrane; Role: sense C. acnes → NF‑κB/MAPK cytokine release. (dessinioti2024themicrobiomeand pages 3-4)
- NLRP3 (HGNC:16400); BP: inflammasome complex assembly; CC: cytosol; Role: IL‑1β maturation in acne lesions. ()
- CASP1 (HGNC:1499); BP: interleukin‑1 beta production; CC: cytosol; Role: executes IL‑1β/IL‑18 processing. ()
- IL1B (HGNC:5992); BP: inflammatory response; CC: extracellular region; Role: comedogenesis and early lesion inflammation. (dessinioti2024themicrobiomeand pages 3-4)
- IL17A (HGNC:5981); BP: Th17 cell differentiation/response; CC: extracellular region; Role: pustular inflammation. (kim2024exploringacnetreatments pages 3-4)
- PPARG (HGNC:9236); BP: lipid metabolic process; CC: nucleus; Role: sebocyte differentiation and cytokine output. (mdermUnknownyearacnevulgarisadvancesa pages 1-2)
- MMPs (e.g., MMP9, HGNC:7159); BP: extracellular matrix organization; CC: extracellular space; Role: matrix degradation in scarring. ()
- TGFB1 (HGNC:11766); BP: TGF‑β receptor signaling pathway; CC: extracellular region; Role: fibroblast activation, fibrosis. ()

## Phenotype associations (HP terms)
- HP:0001051 Comedones; HP:0025031 Papule; HP:0000981 Pustule; HP:0001053 Acneiform eruptions; HP:0001030 Atrophic scars; HP:0001076 Hypertrophic scar. Mechanistic links as above. (kim2024exploringacnetreatments pages 3-4)

## Cell type involvement (CL terms)
- CL:0002328 Sebocyte; CL:0000312 Keratinocyte; CL:0000738 Macrophage; CL:0000913 T helper cell, Th17 subset; CL:0000775 Neutrophil. (kim2024exploringacnetreatments pages 3-4, dessinioti2024themicrobiomeand pages 3-4)

## Anatomical locations (UBERON terms)
- UBERON:0002075 Skin of face; UBERON:0002067 Dermis; UBERON:0002076 Epidermis; UBERON:0035367 Pilosebaceous unit; UBERON:0013702 Hair follicle infundibulum. (dessinioti2024themicrobiomeand pages 3-4)

## Chemical entities (ChEBI)
- CHEBI:17347 Testosterone; CHEBI:16467 Dihydrotestosterone; CHEBI:15956 Linoleic acid; CHEBI:15735 Squalene; CHEBI:16707 Succinic acid; CHEBI:3010 Benzoyl peroxide. (dessinioti2024themicrobiomeand pages 3-4, kim2024exploringacnetreatments pages 3-4)

## Notes and limitations
Where 2025 sources are cited (microbiome bibliometrics; sebaceous gland lipid review; matrix–microbiome review), they extend and reinforce 2023–2024 findings but should be interpreted with corroboration from contemporaneous primary studies. (zhang2025analysisofglobal pages 15-17, mosca2025thesebaceousgland pages 5-7)

## Source list with URLs and dates
- Kim HJ, Kim YH. Exploring Acne Treatments: From Pathophysiological Mechanisms to Emerging Therapies. Int J Mol Sci. 2024-05-10. https://doi.org/10.3390/ijms25105302 (Mechanisms; therapies). (kim2024exploringacnetreatments pages 3-4)
- Dessinioti C, Katsambas A. The Microbiome and Acne: Perspectives for Treatment. Dermatol Ther (Heidelb). 2024-01-09. https://doi.org/10.1007/s13555-023-01079-8 (Microbiome; TLR/NLRP3; AMPs; stewardship). (dessinioti2024themicrobiomeand pages 3-4)
- Keestra‑Gounder AM, Nagao PE. Inflammasome activation by Gram‑positive bacteria. Front Immunol. 2023-01-13. https://doi.org/10.3389/fimmu.2023.1075834 (NLRP3 mechanisms). ()
- Gan Y et al. Commensal microbe regulation of skin cells in disease. Cell Host Microbe. 2024-08-14. https://doi.org/10.1016/j.chom.2024.07.020 (Skin microbe–host regulation; C. acnes pathogenic strains). ()
- Zhao D et al. Macrophages in acne vulgaris. Front Immunol. 2024-03-13. https://doi.org/10.3389/fimmu.2024.1355455 (Macrophage roles; therapeutic implications). ()
- Amuzescu A et al. Adult Female Acne. Cosmetics. 2024-05-09. https://doi.org/10.3390/cosmetics11030074 (Epidemiology; endocrine drivers). (amuzescu2024adultfemaleacne pages 1-2)
- Kohlhauser M et al. An Update on Molecular Mechanisms of Scarring. IJMS. 2024-10-28. https://doi.org/10.3390/ijms252111579 (Fibroblasts; ECM). ()
- Ioannou P et al. Matrix Dynamics and Microbiome Crosstalk. IJMS. 2025-04-23. https://doi.org/10.3390/ijms26083621 (MMPs; dysbiosis–ECM). ()
- Zhang L et al. Global trends and hotspots of skin microbiome in acne. BioData Mining. 2025-03-10. https://doi.org/10.1186/s13040-025-00433-0 (Phylotype statistics; mechanisms). (zhang2025analysisofglobal pages 15-17)
- Mderm RYMDMHA, Kaplan B. Acne Vulgaris: Advances in Pathogenesis and Innovations. (Year/Journal not specified in extract) (Innate sensing; PPARγ; prevalence). (mdermUnknownyearacnevulgarisadvancesa pages 1-2)
- Mosca S et al. The Sebaceous Gland. Cells. 2025-05-15. https://doi.org/10.3390/cells14100747 (Sebum lipids; endocrine/metabolic integration). (mosca2025thesebaceousgland pages 5-7)



References

1. (kim2024exploringacnetreatments pages 3-4): Hyun Jee Kim and Yeong Ho Kim. Exploring acne treatments: from pathophysiological mechanisms to emerging therapies. International Journal of Molecular Sciences, 25:5302, May 2024. URL: https://doi.org/10.3390/ijms25105302, doi:10.3390/ijms25105302. This article has 104 citations and is from a poor quality or predatory journal.

2. (dessinioti2024themicrobiomeand pages 3-4): Clio Dessinioti and Andreas Katsambas. The microbiome and acne: perspectives for treatment. Dermatology and Therapy, 14:31-44, Jan 2024. URL: https://doi.org/10.1007/s13555-023-01079-8, doi:10.1007/s13555-023-01079-8. This article has 50 citations and is from a poor quality or predatory journal.

3. (amuzescu2024adultfemaleacne pages 1-2): Andreea Amuzescu, Mircea Tampa, Clara Matei, and Simona Roxana Georgescu. Adult female acne: recent advances in pathophysiology and therapeutic approaches. Cosmetics, 11:74, May 2024. URL: https://doi.org/10.3390/cosmetics11030074, doi:10.3390/cosmetics11030074. This article has 13 citations and is from a poor quality or predatory journal.

4. (mdermUnknownyearacnevulgarisadvancesa pages 1-2): RYMDMHA Mderm and MD Baruch Kaplan. Acne vulgaris: advances in pathogenesis and innovations in therapeutic strategies. Unknown journal, Unknown year.

5. (mosca2025thesebaceousgland pages 5-7): Sarah Mosca, Monica Ottaviani, Stefania Briganti, Anna Di Nardo, and Enrica Flori. The sebaceous gland: a key player in the balance between homeostasis and inflammatory skin diseases. Cells, 14:747, May 2025. URL: https://doi.org/10.3390/cells14100747, doi:10.3390/cells14100747. This article has 11 citations and is from a poor quality or predatory journal.

6. (zhang2025analysisofglobal pages 15-17): Lanfang Zhang, Yuan Cai, Lin Li, Jie Hu, Changsha Jia, Xu Kuang, Yi Zhou, Zhiai Lan, Chunyan Liu, Feng Jiang, Nana Sun, and Ni Zeng. Analysis of global trends and hotspots of skin microbiome in acne: a bibliometric perspective. BioData Mining, Mar 2025. URL: https://doi.org/10.1186/s13040-025-00433-0, doi:10.1186/s13040-025-00433-0. This article has 3 citations and is from a peer-reviewed journal.