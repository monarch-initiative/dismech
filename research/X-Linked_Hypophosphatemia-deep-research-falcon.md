---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-02-10T18:08:39.918692'
end_time: '2026-02-10T18:25:30.703332'
duration_seconds: 1010.79
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: X-Linked Hypophosphatemia
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 21
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** X-Linked Hypophosphatemia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **X-Linked Hypophosphatemia**.
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
- **Disease Name:** X-Linked Hypophosphatemia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **X-Linked Hypophosphatemia**.
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
- Disease Name: X-Linked Hypophosphatemia (XLH)
- MONDO ID: MONDO_0010619 (X-linked dominant hypophosphatemic rickets)
- Category: Mendelian

Overview and current understanding
XLH is an X-linked dominant, phosphate-wasting osteomalacic/rickets disorder driven by excess osteocyte-derived FGF23 consequent to loss-of-function variants in PHEX. Elevated FGF23 reduces renal phosphate reabsorption and suppresses 1,25-dihydroxyvitamin D [1,25(OH)2D] synthesis, impairing skeletal and dental mineralization from infancy through adulthood. “Loss-of-function mutations in the PHEX gene … result in upregulated FGF23 serum levels and consequent hypophosphatemia” (Orphanet J Rare Dis, 2025; URL: https://doi.org/10.1186/s13023-025-03952-5; published Oct 2025) (brandi2025xlinkedhypophosphatemiaand pages 2-4). Conventional therapy (oral phosphate plus active vitamin D) improves some features but does not correct high FGF23, whereas the FGF23-neutralizing monoclonal antibody burosumab restores phosphate balance and increases endogenous 1,25(OH)2D (Front Endocrinol, 2024; URL: https://doi.org/10.3389/fendo.2024.1414509; published Aug 2024; BDJ Open, 2024; URL: https://doi.org/10.1038/s41405-024-00223-6; published May 2024) (wang2024metaanalysisandsystematic pages 1-2, arhar2024characteristicsoforal pages 8-9).

1) Core Pathophysiology
- Primary mechanisms
  - PHEX loss-of-function in osteocytes/odontoblasts leads to increased circulating FGF23 and accumulation of matrix mineralization inhibitors (e.g., SIBLING-derived ASARM peptides, osteopontin), producing systemic hypophosphatemia and local hypomineralization in bone and teeth (BDJ Open, 2024; URL: https://doi.org/10.1038/s41405-024-00223-6; EJPD, 2025; URL: https://doi.org/10.23804/ejpd.2025.2348) (arhar2024characteristicsoforal pages 8-9, defabianis2025xlinkedhypophosphatemiain pages 1-2).
  - Excess FGF23 acts on FGFR1c–Klotho in renal proximal tubule and parathyroid to: decrease phosphate reabsorption (downregulating NaPi-IIa/SLC34A1 and NaPi-IIc/SLC34A3), suppress CYP27B1 (1α-hydroxylase), and induce CYP24A1 (24-hydroxylase), lowering 1,25(OH)2D and intestinal phosphate absorption (Front Endocrinol, 2024; Orphanet J Rare Dis, 2025; URLs above) (wang2024metaanalysisandsystematic pages 1-2, brandi2025xlinkedhypophosphatemiaand pages 2-4, wang2024metaanalysisandsystematic pages 18-18).
- Dysregulated pathways
  - Osteocyte endocrine axis: PHEX–FGF23–Klotho/FGFR1c signaling (kidney, parathyroid) (Orphanet J Rare Dis, 2025; Front Endocrinol, 2024) (brandi2025xlinkedhypophosphatemiaand pages 2-4, wang2024metaanalysisandsystematic pages 1-2, wang2024metaanalysisandsystematic pages 18-18).
  - Mineralization regulators: MEPE/ASARM, DMP1, ENPP1-mediated pyrophosphate (PPi) balance, and osteopontin accumulation act locally to inhibit hydroxyapatite crystal growth (BDJ Open, 2024) (arhar2024characteristicsoforal pages 8-9, arhar2024characteristicsoforal pages 10-11).
- Affected cellular processes
  - Renal tubular phosphate transport (reduced TmP/GFR), vitamin D activation/catabolism (CYP27B1↓, CYP24A1↑), and matrix mineralization (inhibited nucleation/fusion of calcospherites) (Front Endocrinol, 2024; BDJ Open, 2024) (wang2024metaanalysisandsystematic pages 1-2, arhar2024characteristicsoforal pages 8-9).

2) Key Molecular Players
- Genes/Proteins (HGNC)
  - PHEX (HGNC:8860): Causal gene; loss-of-function increases FGF23 and allows accumulation of ASARM peptides/osteopontin that inhibit mineralization (Orphanet J Rare Dis, 2025; BDJ Open, 2024) (brandi2025xlinkedhypophosphatemiaand pages 2-4, arhar2024characteristicsoforal pages 8-9, arhar2024characteristicsoforal pages 10-11).
  - FGF23 (HGNC:3689): Endocrine phosphatonin from osteocytes; reduces renal phosphate reabsorption and 1,25(OH)2D synthesis (Front Endocrinol, 2024; Orphanet J Rare Dis, 2025) (wang2024metaanalysisandsystematic pages 1-2, brandi2025xlinkedhypophosphatemiaand pages 2-4, wang2024metaanalysisandsystematic pages 18-18).
  - FGFR1 (HGNC:3688) and KLOTHO (HGNC:6353): Co-receptor complex confers FGF23 target specificity in kidney and parathyroid (Front Endocrinol, 2024) (wang2024metaanalysisandsystematic pages 18-18).
  - SLC34A1/NaPi-IIa (HGNC:11039), SLC34A3/NaPi-IIc (HGNC:11041): Proximal-tubule phosphate cotransporters downregulated by FGF23 (Front Endocrinol, 2024) (wang2024metaanalysisandsystematic pages 18-18).
  - CYP27B1 (HGNC:2593), CYP24A1 (HGNC:2594): Vitamin D metabolic enzymes suppressed/induced by FGF23 respectively (Front Endocrinol, 2024) (wang2024metaanalysisandsystematic pages 18-18).
  - MEPE (HGNC:13323), DMP1 (HGNC:2936), ENPP1 (HGNC:3352), SPP1/Osteopontin (HGNC:11255): Matrix regulators linked to impaired mineralization in XLH (BDJ Open, 2024) (arhar2024characteristicsoforal pages 8-9, arhar2024characteristicsoforal pages 10-11).
- Chemical entities (ChEBI)
  - Phosphate (ChEBI:18367), calcitriol/1,25(OH)2D3 (ChEBI:17933/28940), and burosumab (ChEBI:132958) are central to mechanism and therapy (Front Endocrinol, 2024; BDJ Open, 2024) (wang2024metaanalysisandsystematic pages 1-2, arhar2024characteristicsoforal pages 8-9).
- Cell types (CL)
  - Osteocytes and osteoblasts (bone); renal proximal tubule epithelial cells; parathyroid chief cells; odontoblasts/ameloblasts/cementoblasts (dental) are primary cell actors (Orphanet J Rare Dis, 2025; BDJ Open, 2024) (brandi2025xlinkedhypophosphatemiaand pages 2-4, arhar2024characteristicsoforal pages 8-9, arhar2024characteristicsoforal pages 10-11).
- Anatomical locations (UBERON)
  - Bone, kidney (proximal tubule), parathyroid, growth plate, tooth (dentin, cementum), and entheses are key sites (Orphanet J Rare Dis, 2025; BDJ Open, 2024) (brandi2025xlinkedhypophosphatemiaand pages 2-4, arhar2024characteristicsoforal pages 8-9).

3) Biological Processes (for GO annotation)
- Hormone-mediated signaling: FGF23–FGFR1c–Klotho signaling (GO:0005179 ligand activity; GO:0007173 transmembrane receptor protein tyrosine kinase signaling) leading to ERK/MAPK activation in renal proximal tubule/parathyroid (Front Endocrinol, 2024) (wang2024metaanalysisandsystematic pages 18-18).
- Phosphate homeostasis and transport: negative regulation of phosphate ion transmembrane transport (GO:0035435) by downregulation of SLC34A1/SLC34A3; decreased renal tubular phosphate reabsorption (reflected by low TmP/GFR) (Front Endocrinol, 2024; Orphanet J Rare Dis, 2025) (wang2024metaanalysisandsystematic pages 18-18, brandi2025xlinkedhypophosphatemiaand pages 2-4).
- Vitamin D metabolic process: negative regulation of 1α-hydroxylase (CYP27B1) and positive regulation of 24-hydroxylase (CYP24A1) (GO:0038180 regulation of vitamin D biosynthetic process) (Front Endocrinol, 2024) (wang2024metaanalysisandsystematic pages 18-18).
- Biomineralization: extracellular matrix organization and mineralization (GO:0030198; GO:0030282), inhibited by MEPE/ASARM, osteopontin, and altered PPi balance (BDJ Open, 2024) (arhar2024characteristicsoforal pages 8-9, arhar2024characteristicsoforal pages 10-11).

4) Cellular Components (GO)
- Sites of action: osteocyte lacunar–canalicular system and bone matrix (extracellular region; GO:0005576), renal proximal tubular apical membrane (plasma membrane; GO:0005886) hosting NaPi-IIa/IIc, parathyroid gland tissues, and dental hard tissues (dentin/cementum) where PHEX and mineralization inhibitors operate (BDJ Open, 2024; Orphanet J Rare Dis, 2025) (arhar2024characteristicsoforal pages 8-9, brandi2025xlinkedhypophosphatemiaand pages 2-4).

5) Disease Progression
- Sequence of events
  1) Genetic trigger: PHEX loss-of-function in osteocytes/odontoblasts → overproduction of FGF23 and accumulation of ASARM/osteopontin (BDJ Open, 2024) (arhar2024characteristicsoforal pages 8-9, arhar2024characteristicsoforal pages 10-11).
  2) Endocrine effects: FGF23→FGFR1c–Klotho signaling in kidney/parathyroid → phosphaturia (NaPi-IIa/IIc↓), low 1,25(OH)2D (CYP27B1↓, CYP24A1↑), disordered PTH feedback (Front Endocrinol, 2024; Orphanet J Rare Dis, 2025) (wang2024metaanalysisandsystematic pages 18-18, brandi2025xlinkedhypophosphatemiaand pages 2-4).
  3) Tissue consequences: impaired mineralization in growth plates (rickets) and bone (osteomalacia); dental dentin/enamel/cementum hypomineralization → abscesses; adult enthesopathy, pseudofractures, osteoarthritis (BDJ Open, 2024; Orphanet J Rare Dis, 2025) (arhar2024characteristicsoforal pages 8-9, brandi2025xlinkedhypophosphatemiaand pages 2-4, arcidiacono2025potentialpredictorsof pages 16-20).
- Phases
  - Childhood: limb deformities, rickets, short stature, delayed motor development; “typical childhood manifestations include limb growth retardation, abnormal walking patterns, bone pain, and rickets” (Orphanet J Rare Dis, 2025) (brandi2025xlinkedhypophosphatemiaand pages 2-4).
  - Adulthood: persistent osteomalacia, musculoskeletal pain, pseudofractures, enthesopathies, early osteoarthritis; complications from prior therapy (nephrocalcinosis, hyperparathyroidism) (Unknown journal, 2025) (arcidiacono2025potentialpredictorsof pages 16-20).

6) Phenotypic Manifestations (with HP terms)
- Biochemical hallmark: Hypophosphatemia (HP:0002148) with decreased TmP/GFR due to FGF23 excess (Orphanet J Rare Dis, 2025; Front Endocrinol, 2024) (brandi2025xlinkedhypophosphatemiaand pages 2-4, wang2024metaanalysisandsystematic pages 1-2, wang2024metaanalysisandsystematic pages 18-18).
- Skeletal: Rickets (HP:0002748) in children and Osteomalacia (HP:0002649) in adults; bowing of long bones (HP:0002970), short stature (HP:0004322), pseudofractures (HP:0002757), enthesopathy (HP:0002657) (Orphanet J Rare Dis, 2025; Unknown journal, 2025) (brandi2025xlinkedhypophosphatemiaand pages 2-4, arcidiacono2025potentialpredictorsof pages 16-20).
- Dental/craniofacial: spontaneous periapical dental abscesses (HP:0001088), hypomineralized dentin, enamel cracks, aberrant cementum; craniosynostosis reported in some cohorts (BDJ Open, 2024; EJPD, 2025) (arhar2024characteristicsoforal pages 8-9, defabianis2025xlinkedhypophosphatemiain pages 1-2, arhar2024characteristicsoforal pages 10-11).
- Renal/endocrine complications (often therapy-related): nephrocalcinosis (HP:0000121), secondary/tertiary hyperparathyroidism (HP:0000829) (Front Endocrinol, 2024; BDJ Open, 2024) (wang2024metaanalysisandsystematic pages 1-2, arhar2024characteristicsoforal pages 8-9).

Recent developments and latest research (prioritized 2023–2024)
- Pathophysiology-focused updates
  - Contemporary reviews reinforce the centrality of FGF23 as the driver of renal phosphate wasting and reduced 1,25(OH)2D in XLH and emphasize standardized biochemical assessment including intact FGF23 and TmP/GFR (Orphanet J Rare Dis, 2025; Front Endocrinol, 2025 review of biochemical evaluation; URLs: https://doi.org/10.1186/s13023-025-03952-5; https://doi.org/10.3389/fendo.2025.1702656) (brandi2025xlinkedhypophosphatemiaand pages 2-4, brandi2025xlinkedhypophosphatemiaand pages 14-14).
  - Dental mechanistic literature in 2024 highlights that PHEX is expressed in teeth and that mineralization defects reflect “inadequate mineralisation, uneven dentin tubules, and cracks and chipping in the enamel,” with FGF23 mRNA detected in ameloblasts and odontoblasts (BDJ Open, 2024; URL: https://doi.org/10.1038/s41405-024-00223-6; published May 2024) (arhar2024characteristicsoforal pages 8-9).
- Therapeutics and outcomes (2024)
  - Meta-analyses/systematic reviews in 2024 show burosumab improves serum phosphorus, TmP/GFR, 1,25(OH)2D, alkaline phosphatase, rickets severity scores, and functional capacity (6-minute walk test) in children; “burosumab’s superiority in managing XLH in pediatric populations” is supported, though long-term growth and quality-of-life effects require further study (Front Endocrinol, 2024; URL: https://doi.org/10.3389/fendo.2024.1414509; published Aug 2024) (wang2024metaanalysisandsystematic pages 1-2, wang2024metaanalysisandsystematic pages 18-18).

Current applications and real-world implementations
- Diagnostic practice: Routine panels include serum phosphate, calcium, ALP, PTH, 25(OH)D, 1,25(OH)2D, creatinine, intact FGF23, and estimation of TmP/GFR to document renal phosphate wasting; genetic testing confirms PHEX variants (Orphanet J Rare Dis, 2025; URL above; EJPD, 2025; URL: https://doi.org/10.23804/ejpd.2025.2348) (brandi2025xlinkedhypophosphatemiaand pages 2-4, defabianis2025xlinkedhypophosphatemiain pages 1-2).
- Conventional therapy: divided-dose oral phosphate plus active vitamin D analogs remains in use but may raise FGF23 and carries risks (hypercalciuria, nephrocalcinosis, hyperparathyroidism) (BDJ Open, 2024; Front Endocrinol, 2024) (arhar2024characteristicsoforal pages 8-9, wang2024metaanalysisandsystematic pages 1-2).
- Targeted therapy: Burosumab (anti-FGF23 mAb) is approved; it “neutralises elevated FGF23 levels, resulting in better phosphate reabsorption in the renal tubules … increased serum phosphate levels and the synthesis of endogenous 1,25(OH)2 vitamin D” (BDJ Open, 2024; URL above) (arhar2024characteristicsoforal pages 8-9). Randomized and cohort evidence summarized in 2024 meta-analyses demonstrates consistent biochemical and radiographic improvements in pediatric XLH (Front Endocrinol, 2024) (wang2024metaanalysisandsystematic pages 1-2, wang2024metaanalysisandsystematic pages 18-18).

Expert opinions and analysis
- Narrative review and expert opinion (Orphanet J Rare Dis, 2025) emphasizes that anti-FGF23 therapy “has revolutionized the traditional approach” to XLH/TIO management and urges standardized biochemical evaluation including intact FGF23 and TmP/GFR to guide care (URL above) (brandi2025xlinkedhypophosphatemiaand pages 2-4, brandi2025xlinkedhypophosphatemiaand pages 14-14).
- Dental experts underscore that XLH dental disease is frequent and persists despite conventional therapy, reinforcing early, multidisciplinary management and consideration of burosumab’s potential oral-health benefits reported in emerging studies (BDJ Open, 2024) (arhar2024characteristicsoforal pages 8-9, arhar2024characteristicsoforal pages 10-11).

Relevant statistics and data (recent where available)
- Epidemiology: XLH affects up to ~1 in 20,000 individuals and accounts for ~80% of hypophosphatemic rickets (Orphanet J Rare Dis, 2025; URL above) (brandi2025xlinkedhypophosphatemiaand pages 2-4).
- Dental involvement: Reports range widely (e.g., “dental involvement in 23–67% of patients; 40–50% of children and 60–85% of adults affected”), with histology showing “reduced dentin mineralisation … cracks and chipping in the enamel” (EJPD, 2025; BDJ Open, 2024; URLs above) (defabianis2025xlinkedhypophosphatemiain pages 1-2, arhar2024characteristicsoforal pages 8-9).
- Therapeutic outcomes: Pediatric burosumab meta-analysis indicates superiority over conventional therapy for improving serum phosphorus, TmP/GFR, ALP, rickets severity scores, and 6MWT; long-term height/QOL data remain limited (Front Endocrinol, 2024; URL above) (wang2024metaanalysisandsystematic pages 1-2, wang2024metaanalysisandsystematic pages 18-18).

Direct quotes (for key statements)
- “Loss-of-function mutations in the PHEX gene … result in upregulated FGF23 serum levels and consequent hypophosphatemia.” (Orphanet J Rare Dis, 2025) (brandi2025xlinkedhypophosphatemiaand pages 2-4).
- “Burosumab neutralises elevated FGF23 levels, resulting in better phosphate reabsorption in the renal tubules … increased serum phosphate levels and the synthesis of endogenous 1,25(OH)2 vitamin D.” (BDJ Open, 2024) (arhar2024characteristicsoforal pages 8-9).
- Dental histology: “Inadequate mineralisation, uneven dentin tubules, and cracks and chipping in the enamel were observed, indicating mineralisation deviations.” (BDJ Open, 2024) (arhar2024characteristicsoforal pages 8-9).

Ontology-annotated knowledge elements
- Embedded artifact with HGNC (genes/proteins), GO (processes), CL (cell types), UBERON (anatomy), HPO (phenotypes), and ChEBI (chemicals):
| Category | Entity (preferred name) | Identifier (prefix:ID) | Role in XLH pathophysiology (1–2 lines) | Supporting sources |
|---|---|---|---|---|
| Gene/Protein | PHEX | HGNC:8860 | Loss-of-function mutations in PHEX (osteocytes/odontoblasts) lead to elevated FGF23 and accumulation of mineralization inhibitors (e.g., ASARM peptides), causing hypomineralization. | (arhar2024characteristicsoforal pages 8-9, arhar2024characteristicsoforal pages 10-11, brandi2025xlinkedhypophosphatemiaand pages 2-4) |
| Gene/Protein | FGF23 | HGNC:3689 | Osteocyte-derived hormone that reduces renal phosphate reabsorption and suppresses 1,25(OH)2D synthesis; central driver of XLH hypophosphatemia. | (wang2024metaanalysisandsystematic pages 18-18, wang2024metaanalysisandsystematic pages 1-2, brandi2025xlinkedhypophosphatemiaand pages 2-4) |
| Gene/Protein | FGFR1 | HGNC:3688 | FGFR1c (with Klotho) mediates FGF23 signalling in kidney/parathyroid, altering phosphate and vitamin D handling. | (wang2024metaanalysisandsystematic pages 18-18, brandi2025xlinkedhypophosphatemiaand pages 2-4) |
| Gene/Protein | KLOTHO | HGNC:6353 | Co-receptor for FGF23 that confers tissue specificity (renal proximal tubule and parathyroid) for FGF23 effects. | (wang2024metaanalysisandsystematic pages 18-18, brandi2025xlinkedhypophosphatemiaand pages 2-4) |
| Gene/Protein | SLC34A1 (NaPi-IIa) | HGNC:11039 | Renal proximal-tubule sodium-phosphate cotransporter downregulated by FGF23 → decreased phosphate reabsorption (low TmP/GFR). | (wang2024metaanalysisandsystematic pages 18-18, brandi2025xlinkedhypophosphatemiaand pages 2-4) |
| Gene/Protein | SLC34A3 (NaPi-IIc) | HGNC:11041 | Alternate proximal-tubule phosphate transporter contributing to renal phosphate handling; mutations cause other hypophosphatemias and are relevant to renal phenotype. | (brandi2025xlinkedhypophosphatemiaand pages 2-4) |
| Gene/Protein | CYP27B1 | HGNC:2593 | Encodes 1α-hydroxylase; FGF23 suppresses CYP27B1, lowering 1,25(OH)2D and reducing intestinal phosphate/calcium absorption. | (wang2024metaanalysisandsystematic pages 18-18, brandi2025xlinkedhypophosphatemiaand pages 2-4) |
| Gene/Protein | CYP24A1 | HGNC:2594 | Encodes 24‑hydroxylase; FGF23 upregulates CYP24A1, increasing catabolism of 1,25(OH)2D and contributing to low calcitriol. | (wang2024metaanalysisandsystematic pages 18-18, brandi2025xlinkedhypophosphatemiaand pages 2-4) |
| Gene/Protein | MEPE | HGNC:13323 | Matrix protein whose ASARM-derived peptides (when not degraded by PHEX) inhibit hydroxyapatite formation and impair mineralization. | (arhar2024characteristicsoforal pages 8-9, arhar2024characteristicsoforal pages 10-11) |
| Gene/Protein | DMP1 | HGNC:2936 | Osteocyte matrix protein; loss-of-function forms cause FGF23 dysregulation in hereditary hypophosphatemias and modulate mineralization. | (arhar2024characteristicsoforal pages 8-9, arhar2024characteristicsoforal pages 10-11) |
| Gene/Protein | ENPP1 | HGNC:3352 | Regulates extracellular pyrophosphate (PPi); dysregulation affects mineralization balance and can interact with FGF23-related pathways. | (arhar2024characteristicsoforal pages 8-9, arhar2024characteristicsoforal pages 10-11) |
| Gene/Protein | SPP1 (Osteopontin) | HGNC:11255 | Accumulates when PHEX activity is reduced; binds mineral and can inhibit crystal growth, contributing to defective mineralization. | (arhar2024characteristicsoforal pages 8-9, arhar2024characteristicsoforal pages 10-11) |
| Cell type | Osteocyte | CL:0000121 | Principal source of FGF23 and site of PHEX expression; dysfunctional osteocytes drive endocrine and local mineralization defects. | (arhar2024characteristicsoforal pages 8-9, brandi2025xlinkedhypophosphatemiaand pages 2-4) |
| Cell type | Osteoblast | CL:0000062 | Bone-forming cell interacting with osteocytes and matrix SIBLING proteins; contributes to defective mineral deposition in XLH. | (arhar2024characteristicsoforal pages 8-9, arhar2024characteristicsoforal pages 10-11) |
| Cell type | Chondrocyte | CL:0000138 | Growth-plate chondrocytes are affected by phosphate deficiency, causing rickets and growth-plate abnormalities in children. | (brandi2025xlinkedhypophosphatemiaand pages 2-4) |
| Cell type | Renal proximal tubule epithelial cell | CL:0002306 | Primary renal target where FGF23–Klotho–FGFR1c signalling downregulates NaPi transporters, causing phosphaturia. | (wang2024metaanalysisandsystematic pages 18-18, brandi2025xlinkedhypophosphatemiaand pages 2-4) |
| Cell type | Parathyroid chief cell | CL:0000772 | Parathyroid is a target of FGF23; altered FGF23/PTH interplay contributes to mineral metabolism dysregulation and secondary hyperparathyroidism risk. | (wang2024metaanalysisandsystematic pages 18-18, brandi2025xlinkedhypophosphatemiaand pages 2-4) |
| Cell type | Odontoblast | CL:0000115 | Dental cell expressing PHEX and FGF23 mRNA; PHEX dysfunction leads to dentin hypomineralization and increased dental abscess risk. | (arhar2024characteristicsoforal pages 8-9, arhar2024characteristicsoforal pages 10-11, defabianis2025xlinkedhypophosphatemiain pages 1-2) |
| Cell type | Ameloblast | CL:0002494 | Enamel-forming cell where FGF23 expression has been detected; contributes to dental phenotype alongside odontoblast defects. | (arhar2024characteristicsoforal pages 8-9, arhar2024characteristicsoforal pages 10-11) |
| Cell type | Cementoblast | CL:0009011 | Cementum-forming cell implicated in abnormal cementum observed in XLH models, contributing to periodontal/dentoalveolar pathology. | (arhar2024characteristicsoforal pages 10-11) |
| Anatomy | Bone | UBERON:0001474 | Primary affected tissue: impaired mineralization (rickets in children, osteomalacia in adults) due to systemic hypophosphatemia and local inhibitors. | (brandi2025xlinkedhypophosphatemiaand pages 2-4, arhar2024characteristicsoforal pages 8-9) |
| Anatomy | Kidney | UBERON:0002113 | Site of phosphate wasting via proximal-tubule transporter downregulation and altered vitamin D metabolism from FGF23 action. | (wang2024metaanalysisandsystematic pages 18-18, brandi2025xlinkedhypophosphatemiaand pages 2-4) |
| Anatomy | Renal proximal tubule | UBERON:0001285 | Anatomical location of NaPi transporters and Klotho expression where FGF23 exerts phosphaturic effects. | (wang2024metaanalysisandsystematic pages 18-18, brandi2025xlinkedhypophosphatemiaand pages 2-4) |
| Anatomy | Growth plate | UBERON:0003616 | Phosphate-dependent cartilage mineralization occurs here; deficiency leads to widening/irregularity and rickets. | (brandi2025xlinkedhypophosphatemiaand pages 2-4) |
| Anatomy | Parathyroid gland | UBERON:0001132 | Interacts with FGF23/vitamin D axis; PTH disturbances (secondary/tertiary hyperparathyroidism) are clinical concerns with therapy. | (wang2024metaanalysisandsystematic pages 18-18, arcidiacono2025potentialpredictorsof pages 16-20) |
| Anatomy | Tooth | UBERON:0001091 | Dentition displays hypomineralized dentin, enamel defects, and increased periapical pathology in XLH. | (arhar2024characteristicsoforal pages 8-9, arhar2024characteristicsoforal pages 10-11, defabianis2025xlinkedhypophosphatemiain pages 1-2) |
| Anatomy | Dentin | UBERON:0001750 | Site of defective mineralization (reduced dentin mineral density, abnormal tubules) linked to PHEX/ASARM effects. | (arhar2024characteristicsoforal pages 8-9, arhar2024characteristicsoforal pages 10-11) |
| Anatomy | Cementum | UBERON:0001751 | Abnormal cementum reported in hyp mouse and human studies, contributing to periodontal/dental sequelae. | (arhar2024characteristicsoforal pages 10-11) |
| Anatomy | Enthesis | UBERON:0002185 | Enthesopathies (calcific enthesopathy) are common adult complications related to chronic mineral imbalance and mechanical stress. | (arcidiacono2025potentialpredictorsof pages 16-20, brandi2025xlinkedhypophosphatemiaand pages 2-4) |
| Phenotype | Hypophosphatemia | HPO:HP:0002148 | Biochemical hallmark caused by FGF23-driven renal phosphate wasting; central diagnostic feature (low serum phosphate, low TmP/GFR). | (wang2024metaanalysisandsystematic pages 18-18, brandi2025xlinkedhypophosphatemiaand pages 2-4) |
| Phenotype | Rickets | HPO:HP:0002748 | Pediatric manifestation from impaired growth-plate mineralization leading to bowing, deformity, and delayed motor milestones. | (brandi2025xlinkedhypophosphatemiaand pages 2-4, arcidiacono2025potentialpredictorsof pages 16-20) |
| Phenotype | Osteomalacia | HPO:HP:0002649 | Adult manifestation of defective bone mineralization with bone pain, fractures, and pseudofractures. | (brandi2025xlinkedhypophosphatemiaand pages 2-4, arcidiacono2025potentialpredictorsof pages 16-20) |
| Phenotype | Short stature | HPO:HP:0004322 | Growth impairment from chronic phosphate deficiency and rickets in pediatric patients. | (arcidiacono2025potentialpredictorsof pages 16-20, brandi2025xlinkedhypophosphatemiaand pages 2-4) |
| Phenotype | Bowing of long bone | HPO:HP:0002970 | Classic orthopedic deformity in untreated/under-treated pediatric XLH due to growth-plate pathology. | (brandi2025xlinkedhypophosphatemiaand pages 2-4) |
| Phenotype | Dental abscess | HPO:HP:0001088 | Frequent spontaneous periapical infections linked to hypomineralized dentin and pulp exposures. | (arhar2024characteristicsoforal pages 8-9, arhar2024characteristicsoforal pages 10-11, defabianis2025xlinkedhypophosphatemiain pages 1-2) |
| Phenotype | Craniosynostosis | HPO:HP:0001363 | Reported comorbidity in some cohorts; linked to abnormal skull growth/mineralization in XLH. | (arcidiacono2025potentialpredictorsof pages 16-20, brandi2025xlinkedhypophosphatemiaand pages 2-4) |
| Phenotype | Enthesopathy | HPO:HP:0002657 | Calcific enthesopathies and joint problems arise in adults with long-standing disease. | (arcidiacono2025potentialpredictorsof pages 16-20, brandi2025xlinkedhypophosphatemiaand pages 2-4) |
| Phenotype | Pseudofractures | HPO:HP:0002757 | Insufficiency fractures due to impaired bone strength from osteomalacia. | (arcidiacono2025potentialpredictorsof pages 16-20, brandi2025xlinkedhypophosphatemiaand pages 2-4) |
| Phenotype | Nephrocalcinosis | HPO:HP:0000121 | Potential complication of conventional phosphate/vitamin D therapy (and monitoring concern). | (wang2024metaanalysisandsystematic pages 18-18, wang2024metaanalysisandsystematic pages 1-2) |
| Phenotype | Hyperparathyroidism | HPO:HP:0000829 | Secondary/tertiary hyperparathyroidism can arise from therapy or chronic mineral dysregulation. | (wang2024metaanalysisandsystematic pages 18-18, arcidiacono2025potentialpredictorsof pages 16-20) |
| Phenotype | Hearing impairment | HPO:HP:0000365 | Reported extracranial manifestation in XLH cohorts (sensorineural/conductive elements described). | (arcidiacono2025potentialpredictorsof pages 16-20) |
| Chemical | Phosphate | ChEBI:18367 | Essential mineral depleted in XLH due to renal wasting; low serum phosphate drives clinical manifestations. | (wang2024metaanalysisandsystematic pages 18-18, brandi2025xlinkedhypophosphatemiaand pages 2-4) |
| Chemical | 1,25-dihydroxyvitamin D3 (calcitriol) | ChEBI:28940 / ChEBI:17933 | Active vitamin D reduced in XLH (FGF23 suppresses synthesis/increases catabolism), lowering intestinal phosphate/calcium absorption. | (wang2024metaanalysisandsystematic pages 18-18, brandi2025xlinkedhypophosphatemiaand pages 2-4) |
| Chemical | Calcitriol (therapeutic) | ChEBI:17933 | Used therapeutically with oral phosphate to boost mineralization but does not target FGF23 and carries risk of hypercalciuria. | (wang2024metaanalysisandsystematic pages 18-18, wang2024metaanalysisandsystematic pages 1-2) |
| Chemical | Burosumab (anti-FGF23 antibody) | ChEBI:132958 | FGF23-neutralizing monoclonal antibody that restores renal phosphate reabsorption, raises serum phosphate and 1,25(OH)2D, improving rickets/osteomalacia. | (wang2024metaanalysisandsystematic pages 18-18, wang2024metaanalysisandsystematic pages 1-2, brandi2025xlinkedhypophosphatemiaand pages 2-4) |


*Table: A compact mapping of key genes, cell types, anatomical sites, phenotypes, and chemicals for X-linked hypophosphatemia (XLH), linked to standard ontology identifiers and primary supporting evidence from gathered sources. This table is intended for knowledge‑base annotation and mechanistic reference (arhar2024characteristicsoforal pages 8-9, brandi2025xlinkedhypophosphatemiaand pages 2-4).*

Mechanism of action and outcomes of burosumab
- Mechanism: Anti-FGF23 monoclonal antibody that restores renal phosphate handling (NaPi-IIa/IIc expression indirectly via FGF23 blockade) and increases endogenous 1,25(OH)2D by relieving CYP27B1 suppression/CYP24A1 induction (BDJ Open, 2024; Front Endocrinol, 2024) (arhar2024characteristicsoforal pages 8-9, wang2024metaanalysisandsystematic pages 1-2, wang2024metaanalysisandsystematic pages 18-18).
- Outcomes: In children, improved serum phosphate, TmP/GFR, ALP, rickets severity scores, and functional capacity; favorable safety compared with conventional therapy, with ongoing assessment of long-term growth and QOL (Front Endocrinol, 2024) (wang2024metaanalysisandsystematic pages 1-2, wang2024metaanalysisandsystematic pages 18-18).

Evidence items (with PMIDs/DOIs/URLs/dates)
- Brandi ML et al. X-linked hypophosphatemia and tumor-induced osteomalacia: narrative review/expert opinion. Orphanet J Rare Dis. Published Oct 2025. DOI: 10.1186/s13023-025-03952-5. URL: https://doi.org/10.1186/s13023-025-03952-5 (brandi2025xlinkedhypophosphatemiaand pages 2-4, brandi2025xlinkedhypophosphatemiaand pages 14-14).
- Wang K et al. Meta-analysis and systematic review: burosumab in children with XLH. Front Endocrinol. Published Aug 2024. DOI: 10.3389/fendo.2024.1414509. URL: https://doi.org/10.3389/fendo.2024.1414509 (wang2024metaanalysisandsystematic pages 1-2, wang2024metaanalysisandsystematic pages 18-18).
- Arhar A et al. Characteristics of oral health of patients with XLH. BDJ Open. Published May 2024. DOI: 10.1038/s41405-024-00223-6. URL: https://doi.org/10.1038/s41405-024-00223-6 (arhar2024characteristicsoforal pages 8-9, arhar2024characteristicsoforal pages 10-11).
- Defabianis P et al. XLH in childhood: dental involvement, diagnosis, and treatment. Eur J Paediatr Dent. Published Dec 2025. DOI: 10.23804/ejpd.2025.2348. URL: https://doi.org/10.23804/ejpd.2025.2348 (defabianis2025xlinkedhypophosphatemiain pages 1-2).
- Arcidiacono GP. Potential predictors of response to burosumab in adults with XLH. 2025. (arcidiacono2025potentialpredictorsof pages 16-20).

Limitations
- Some 2025 sources are narrative/expert reviews. Where randomized and meta-analytic evidence is summarized, we prioritized 2024 systematic reviews/meta-analyses. Long-term outcomes (adult skeletal structure, enthesopathy reversal, dental organ regeneration) require further longitudinal data (Front Endocrinol, 2024) (wang2024metaanalysisandsystematic pages 1-2).

Pathophysiology description (knowledge-base ready)
- XLH results from PHEX (HGNC:8860) loss-of-function in osteocytes/odontoblasts, elevating FGF23 (HGNC:3689), which activates FGFR1 (HGNC:3688) with KLOTHO (HGNC:6353) in renal proximal tubule (UBERON:0001285) and parathyroid (UBERON:0001132), reducing NaPi-IIa (SLC34A1; HGNC:11039)/NaPi-IIc (SLC34A3; HGNC:11041) activity and suppressing CYP27B1 (HGNC:2593) while inducing CYP24A1 (HGNC:2594). Systemic effects are hypophosphatemia (HP:0002148) and low/normal 1,25(OH)2D, with local matrix inhibition by MEPE/ASARM (HGNC:13323) and osteopontin/SPP1 (HGNC:11255), and contributions from DMP1 (HGNC:2936) and ENPP1 (HGNC:3352) to PPi balance, leading to rickets (HP:0002748) and osteomalacia (HP:0002649), dental abscesses (HP:0001088), and adult enthesopathy (HP:0002657) (Orphanet J Rare Dis, 2025; Front Endocrinol, 2024; BDJ Open, 2024) (brandi2025xlinkedhypophosphatemiaand pages 2-4, wang2024metaanalysisandsystematic pages 1-2, wang2024metaanalysisandsystematic pages 18-18, arhar2024characteristicsoforal pages 8-9, arhar2024characteristicsoforal pages 10-11).


References

1. (brandi2025xlinkedhypophosphatemiaand pages 2-4): Maria Luisa Brandi, Cristina Eller Vainicher, Danilo Fintini, Andrea Giusti, Andrea Magnolato, Salvatore Minisola, and Sandro Giannini. X-linked hypophosphatemia and tumor-induced osteomalacia: a narrative review and expert opinion on the diagnostic and therapeutic challenges in the era of burosumab. Orphanet Journal of Rare Diseases, Oct 2025. URL: https://doi.org/10.1186/s13023-025-03952-5, doi:10.1186/s13023-025-03952-5. This article has 0 citations and is from a peer-reviewed journal.

2. (wang2024metaanalysisandsystematic pages 1-2): Kangning Wang, Runze Zhang, Ziyi Chen, Yi Bai, and Qing He. Meta-analysis and systematic review: burosumab as a promising treatment for children with x-linked hypophosphatemia. Frontiers in Endocrinology, Aug 2024. URL: https://doi.org/10.3389/fendo.2024.1414509, doi:10.3389/fendo.2024.1414509. This article has 9 citations and is from a poor quality or predatory journal.

3. (arhar2024characteristicsoforal pages 8-9): Ana Arhar, Alenka Pavlič, and Luka Hočevar. Characteristics of oral health of patients with x-linked hypophosphatemia: case reports and literature review. BDJ Open, May 2024. URL: https://doi.org/10.1038/s41405-024-00223-6, doi:10.1038/s41405-024-00223-6. This article has 5 citations and is from a peer-reviewed journal.

4. (defabianis2025xlinkedhypophosphatemiain pages 1-2): P. Defabianis, N. Bocca, and R. Ninivaggi. X-linked hypophosphatemia in childhood: dental involvement, diagnosis, and treatment. European journal of paediatric dentistry, pages 1, Dec 2025. URL: https://doi.org/10.23804/ejpd.2025.2348, doi:10.23804/ejpd.2025.2348. This article has 0 citations and is from a peer-reviewed journal.

5. (wang2024metaanalysisandsystematic pages 18-18): Kangning Wang, Runze Zhang, Ziyi Chen, Yi Bai, and Qing He. Meta-analysis and systematic review: burosumab as a promising treatment for children with x-linked hypophosphatemia. Frontiers in Endocrinology, Aug 2024. URL: https://doi.org/10.3389/fendo.2024.1414509, doi:10.3389/fendo.2024.1414509. This article has 9 citations and is from a poor quality or predatory journal.

6. (arhar2024characteristicsoforal pages 10-11): Ana Arhar, Alenka Pavlič, and Luka Hočevar. Characteristics of oral health of patients with x-linked hypophosphatemia: case reports and literature review. BDJ Open, May 2024. URL: https://doi.org/10.1038/s41405-024-00223-6, doi:10.1038/s41405-024-00223-6. This article has 5 citations and is from a peer-reviewed journal.

7. (arcidiacono2025potentialpredictorsof pages 16-20): GP Arcidiacono. Potential predictors of response to burosumab treatment in adult patients with x-linked hypophosphatemia. Unknown journal, 2025.

8. (brandi2025xlinkedhypophosphatemiaand pages 14-14): Maria Luisa Brandi, Cristina Eller Vainicher, Danilo Fintini, Andrea Giusti, Andrea Magnolato, Salvatore Minisola, and Sandro Giannini. X-linked hypophosphatemia and tumor-induced osteomalacia: a narrative review and expert opinion on the diagnostic and therapeutic challenges in the era of burosumab. Orphanet Journal of Rare Diseases, Oct 2025. URL: https://doi.org/10.1186/s13023-025-03952-5, doi:10.1186/s13023-025-03952-5. This article has 0 citations and is from a peer-reviewed journal.