---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-18T14:04:58.498335'
end_time: '2025-12-18T14:13:29.074965'
duration_seconds: 510.58
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Small Intestinal Bacterial Overgrowth
  mondo_id: ''
  category: Complex
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 39
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Small Intestinal Bacterial Overgrowth
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Small Intestinal Bacterial Overgrowth**.
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
- **Disease Name:** Small Intestinal Bacterial Overgrowth
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Small Intestinal Bacterial Overgrowth**.
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


Disease Pathophysiology Research Report: Small Intestinal Bacterial Overgrowth (SIBO)

Target Disease
- Disease Name: Small Intestinal Bacterial Overgrowth (SIBO)
- MONDO ID: Not conclusively identified (multiple related entries; not standardized across recent literature)
- Category: Complex

Pathophysiology description
SIBO is classically defined as an abnormal increase in the number and/or composition of bacteria in the small intestine, with culture thresholds historically ranging from ≥10^3–10^5 CFU/mL and often cited at ≥10^5 CFU/mL, accompanied by qualitative shifts toward colonic-type taxa and enhanced fermentative metabolism. “Physiologic defenses that normally limit small intestinal colonization include acidic stomach pH, pancreatic enzymes, intestinal immune mechanisms, peristalsis, the ileocecal valve and the mucosal barrier,” such that disruption of gastric acid, motility (including migrating motor complex [MMC]), and the ileocecal barrier promotes overgrowth and malabsorption (URL: https://doi.org/10.20944/preprints202403.1571.v1; posted Mar 26, 2024). Mechanistically, SIBO features increased carbohydrate fermentation (H2, CO2), methanogenesis (CH4) by archaea, short-chain fatty acid production, and bile-acid deconjugation, which together impair digestion/absorption and irritate mucosa. Bacterial products such as lipopolysaccharide (LPS) activate innate receptors (TLR4/TLR2), promoting mucosal inflammation, barrier dysfunction, and—in some settings—endotoxin translocation along the gut–liver axis. Nutrient malabsorption is common, notably vitamin B12 deficiency and fat malabsorption due to bile-acid deconjugation. While SIBO is clearly established in settings of anatomic stasis and dysmotility (e.g., systemic sclerosis), the broader SIBO–IBS hypothesis remains debated, and diagnostic limitations of breath testing have been emphasized by expert groups (ESNM/ANMS) (URL: https://doi.org/10.1111/nmo.14817; May 2024). (roszkowska2024smallintestinalbacteriala pages 5-7, roszkowska2024smallintestinalbacteriala pages 7-9, kashyap2024criticalappraisalof pages 9-10)

1) Core Pathophysiology
- Primary mechanisms
  - Motility failure and stasis: Impaired small-intestinal motility/MCC (e.g., diabetes autonomic neuropathy, systemic sclerosis), anatomic stasis (surgical blind loops/diverticula, loss of ileocecal valve), and slowed transit permit bacterial accumulation and retrograde colonization. Expert update notes “primary or secondary small intestinal dysmotility,” altered anatomy, increased luminal pH (PPIs/achlorhydria), and loss of antibacterial defenses as core drivers (Neurogastroenterol Motil 2024). (nowakowski2024smallintestinalbacterial pages 4-7, kashyap2024criticalappraisalof pages 9-10)
  - Hypochlorhydria/PPIs: Reduced gastric acid permits survival of oropharyngeal/colonic bacteria into the small bowel; prolonged PPI use is associated with increased SIBO in observational syntheses (see statistics). (roszkowska2024smallintestinalbacteriala pages 5-7, efremova2023epidemiologyofsmall pages 2-4)
  - Microbial/metabolic alterations: Overgrowth increases fermentation of carbohydrates to hydrogen, methane, and short-chain fatty acids; bile-salt deconjugation impairs micellar fat absorption. The normal proximal small bowel milieu (bile, low microbial density) restricts “carbohydrate fermentation and bile deconjugation,” but perturbations raise density to 10^7–10^8 CFU/mL and shift composition. (kashyap2024criticalappraisalof pages 9-10, roszkowska2024smallintestinalbacteriala pages 5-7)
  - Host barrier and immune responses: LPS and other microbial products induce innate immune activation (TLR2/TLR4), mucosal inflammation, and increased epithelial permeability. “Activation of the immune system and prolonged inflammation… increase intestinal vascular permeability,” with potential for endotoxin-driven signaling and systemic effects. (roszkowska2024smallintestinalbacteriala pages 9-11, roszkowska2024smallintestinalbacteriala pages 7-9)
- Dysregulated molecular pathways
  - Innate immune signaling: LPS–TLR4/TLR2 pathways implicate NF-κB-driven inflammation and barrier disruption. (roszkowska2024smallintestinalbacteriala pages 9-11)
  - Bile-acid metabolism: Bacterial deconjugation alters BA pool properties and lipid absorption; bile-tolerant taxa can expand under impaired bile secretion (e.g., cirrhosis). (kashyap2024criticalappraisalof pages 9-10)
  - Fermentation and gas metabolism: Enhanced carbohydrate fermentation; methanogenesis (e.g., Methane-positive profiles linked to constipation phenotypes) and hydrogen production measurable by breath tests. (kashyap2024criticalappraisalof pages 9-10, roszkowska2024smallintestinalbacteriala pages 5-7)
- Affected cellular processes
  - Tight junction assembly and barrier integrity are compromised by inflammatory signaling and microbial metabolites; brush-border digestive and transport functions are impaired, causing malabsorption. (kashyap2024criticalappraisalof pages 9-10, roszkowska2024smallintestinalbacteriala pages 5-7)

2) Key Molecular Players
- Genes/Proteins (HGNC)
  - TLR4 (HGNC:11850) and TLR2 (HGNC:11848): epithelial/immune LPS and bacterial component sensors mediating innate immune activation in SIBO contexts. (roszkowska2024smallintestinalbacteriala pages 9-11)
  - Secretory IgA (IGHA1/IGHA2): mucosal immune exclusion; reduced function predisposes to SIBO. (kashyap2024criticalappraisalof pages 9-10)
- Chemical entities (CHEBI)
  - Lipopolysaccharide (LPS; CHEBI:16412): triggers TLR signaling; promotes mucosal inflammation and permeability. (roszkowska2024smallintestinalbacteriala pages 9-11)
  - Bile acids (CHEBI:15889): targets of bacterial deconjugation; altered pool impairs fat absorption. (kashyap2024criticalappraisalof pages 9-10)
  - Short-chain fatty acids (SCFAs; CHEBI:26666): microbial fermentation products; modulate epithelial/immune responses. (roszkowska2024smallintestinalbacteriala pages 5-7)
  - Hydrogen (CHEBI:18276) and Methane (CHEBI:16183): gaseous fermentation products measured in breath tests; methane production (methanogen overgrowth) is associated with altered transit. (kashyap2024criticalappraisalof pages 9-10, feng2025prevalenceandpredictors pages 14-14)
  - Vitamin B12/cobalamin (CHEBI:17697): deficiency from bacterial consumption/competition; macrocytic anemia. (roszkowska2024smallintestinalbacteriala pages 5-7)
- Cell types (CL)
  - Enterocytes (CL:0000584): absorptive epithelium; site of transport and barrier regulation affected in SIBO. (roszkowska2024smallintestinalbacteriala pages 5-7)
  - Paneth cells (CL:0000587): antimicrobial peptide secretion; part of intrinsic antibacterial defense. (kashyap2024criticalappraisalof pages 9-10)
  - IgA-producing plasma cells (CL:0000786): mucosal immunity; supports homeostasis. (kashyap2024criticalappraisalof pages 9-10)
- Anatomical locations (UBERON)
  - Small intestine (UBERON:0002108), jejunum (UBERON:0002115), ileum (UBERON:0002116), ileocecal valve (UBERON:0001276). (roszkowska2024smallintestinalbacteriala pages 3-5, roszkowska2024smallintestinalbacteriala pages 5-7)

SIBO molecular/cellular annotations
| Category | Name | Ontology ID | Mechanistic role in SIBO (1-2 sentences) | Evidence |
|---|---|---:|---|---|
| Gene/Protein | TLR4 | HGNC:11850 | Innate receptor recognizing lipopolysaccharide (LPS); activation by bacterial LPS can drive mucosal inflammation and systemic innate signalling contributing to SIBO-associated inflammation. | (roszkowska2024smallintestinalbacteriala pages 9-11, kashyap2024criticalappraisalof pages 9-10) |
| Gene/Protein | TLR2 | HGNC:11848 | Pattern-recognition receptor that detects bacterial cell-wall components; contributes to mucosal immune activation and inflammation in response to small-intestinal bacterial products. | (roszkowska2024smallintestinalbacteriala pages 9-11, kashyap2024criticalappraisalof pages 9-10) |
| Gene/Protein | IgA (secretory IgA; IGHA1/IGHA2) | IGHA1/IGHA2 (HGNC) | Mucosal antibody that limits bacterial adhesion and colonization in the small intestine; deficiency or impaired IgA responses permit overgrowth and translocation. | (kashyap2024criticalappraisalof pages 9-10, roszkowska2024smallintestinalbacteriala pages 5-7) |
| Cell Type | Paneth cell | CL:0000587 | Secrete antimicrobial peptides (e.g., defensins) that restrict small-bowel microbial density; dysfunction reduces antimicrobial defenses and promotes overgrowth. | (kashyap2024criticalappraisalof pages 9-10, roszkowska2024smallintestinalbacteriala pages 3-5) |
| Cell Type | Enterocyte | CL:0000584 | Main absorptive epithelial cell; site of nutrient absorption and barrier functions (brush border, tight junctions); affected by bacterial metabolites leading to malabsorption and barrier dysfunction. | (roszkowska2024smallintestinalbacteriala pages 5-7, roszkowska2024smallintestinalbacteriala pages 3-5) |
| Cell Type | Plasma cell (IgA-producing) | CL:0000786 | Produces secretory IgA at the mucosa; supports immune exclusion of luminal bacteria and maintenance of small-intestinal homeostasis. | (kashyap2024criticalappraisalof pages 9-10) |
| Biological Process (GO) | Bile acid metabolic process | GO:0006631 | Bacterial deconjugation of bile acids alters lipid digestion and fat absorption, promoting fat malabsorption and selection for bile-tolerant taxa in SIBO. | (kashyap2024criticalappraisalof pages 9-10, roszkowska2024smallintestinalbacteriala pages 5-7) |
| Biological Process (GO) | Carbohydrate fermentation | GO:1900271 | Overgrown small-intestinal fermenters metabolize carbohydrates to gases (H2, CH4) and SCFAs, causing bloating, altered transit, and symptomatic gas production. | (roszkowska2024smallintestinalbacteriala pages 5-7, kashyap2024criticalappraisalof pages 9-10) |
| Biological Process (GO) | Response to lipopolysaccharide | GO:0032496 | Enterocyte and immune-cell responses to LPS drive mucosal inflammation and increased permeability, linking microbial overgrowth to immune activation. | (roszkowska2024smallintestinalbacteriala pages 9-11, roszkowska2024smallintestinalbacteriala pages 5-7) |
| Biological Process (GO) | Tight junction assembly | GO:0070830 | Regulation and disruption of tight junctions modulate intestinal permeability; bacterial metabolites and inflammation can impair assembly leading to increased translocation. | (kashyap2024criticalappraisalof pages 9-10, roszkowska2024smallintestinalbacteriala pages 9-11) |
| Biological Process (GO) | Vitamin B12 transport | GO:0015889 | Disturbance of B12 absorption (bacterial consumption/deconjugation) leads to B12 deficiency and macrocytic anemia in chronic SIBO. | (roszkowska2024smallintestinalbacteriala pages 5-7, feng2025prevalenceandpredictors pages 14-14) |
| Cellular Component (GO-CC) | Brush border | GO:0031526 | Apical microvillus domain of enterocytes essential for digestion and absorption; damage or microbial-induced dysfunction contributes to malabsorption in SIBO. | (roszkowska2024smallintestinalbacteriala pages 5-7) |
| Cellular Component (GO-CC) | Tight junction | GO:0005923 | Intercellular junctions that maintain epithelial barrier; disruption by bacterial metabolites/inflammation increases permeability and endotoxin translocation. | (kashyap2024criticalappraisalof pages 9-10, roszkowska2024smallintestinalbacteriala pages 9-11) |
| Cellular Component (GO-CC) | Extracellular space | GO:0005615 | Lumenal/extracellular compartment where bacterial metabolites (LPS, SCFAs, gases) accumulate and interact with the epithelium. | (roszkowska2024smallintestinalbacteriala pages 5-7, roszkowska2024smallintestinalbacteriala pages 3-5) |
| Anatomical Site (UBERON) | Small intestine | UBERON:0002108 | Primary anatomical location of SIBO; normally low microbial density that, when disrupted by motility, anatomy, or acidity changes, permits overgrowth and malabsorption. | (roszkowska2024smallintestinalbacteriala pages 5-7, roszkowska2024smallintestinalbacteriala pages 7-9) |
| Anatomical Site (UBERON) | Jejunum | UBERON:0002115 | Segment frequently sampled/affected in SIBO where carbohydrate fermentation and nutrient malabsorption commonly occur. | (roszkowska2024smallintestinalbacteriala pages 5-7) |
| Anatomical Site (UBERON) | Ileum | UBERON:0002116 | Distal small intestine involved in bile acid and B12 absorption; bacterial deconjugation here promotes bile-acid–mediated malabsorption and B12 deficiency. | (roszkowska2024smallintestinalbacteriala pages 5-7, roszkowska2024smallintestinalbacteriala pages 9-11) |
| Anatomical Site (UBERON) | Ileocecal valve | UBERON:0001276 | Anatomical barrier preventing retrograde colonic bacterial entry; loss or dysfunction permits colon-type bacteria to colonize the small bowel. | (roszkowska2024smallintestinalbacteriala pages 3-5, roszkowska2024smallintestinalbacteriala pages 5-7) |
| Chemical Entity (CHEBI) | Lipopolysaccharide (LPS) | CHEBI:16412 | Bacterial endotoxin that activates TLR4/TLR2-driven inflammation and can increase intestinal permeability and systemic endotoxemia. | (roszkowska2024smallintestinalbacteriala pages 9-11, roszkowska2024smallintestinalbacteriala pages 5-7) |
| Chemical Entity (CHEBI) | Bile acid | CHEBI:15889 | Substrates for bacterial deconjugation; altered bile acid pool impairs fat digestion and selects for bile-resistant microbes in SIBO. | (kashyap2024criticalappraisalof pages 9-10, roszkowska2024smallintestinalbacteriala pages 5-7) |
| Chemical Entity (CHEBI) | Short-chain fatty acids (SCFAs) | CHEBI:26666 | Microbial metabolites (e.g., acetate, propionate) produced by fermentation; can modulate epithelial function, barrier integrity, and immune responses in SIBO. | (roszkowska2024smallintestinalbacteriala pages 5-7, roszkowska2024smallintestinalbacteriala pages 3-5) |
| Chemical Entity (CHEBI) | Methane | CHEBI:16183 | Product of methanogenic archaea (e.g., Methanobrevibacter) consuming H2; associated with altered transit (constipation-predominant symptoms) in small-intestinal overgrowth contexts. | (feng2025prevalenceandpredictors pages 14-14, roszkowska2024smallintestinalbacteriala pages 5-7) |
| Chemical Entity (CHEBI) | Hydrogen | CHEBI:18276 | Gas produced by bacterial fermentation; substrate for methanogenesis and a marker measured in breath tests for SIBO. | (roszkowska2024smallintestinalbacteriala pages 5-7, kashyap2024criticalappraisalof pages 9-10) |
| Chemical Entity (CHEBI) | Vitamin B12 (cobalamin) | CHEBI:17697 | Essential micronutrient whose intestinal availability is reduced by bacterial competition/consumption, leading to deficiency-related clinical features in SIBO. | (roszkowska2024smallintestinalbacteriala pages 5-7, feng2025prevalenceandpredictors pages 14-14) |


*Table: Concise table mapping genes/proteins, cell types, GO processes, cellular components, anatomical sites, and chemicals implicated in SIBO, with ontology IDs, brief mechanistic roles, and supporting evidence context IDs for use in a disease knowledge base.*

3) Biological Processes (GO) disrupted
- Carbohydrate fermentation (GO:1900271): excessive fermentation to H2/CH4/SCFAs in small intestine. (roszkowska2024smallintestinalbacteriala pages 5-7, kashyap2024criticalappraisalof pages 9-10)
- Bile acid metabolic process (GO:0006631): deconjugation reduces fat absorption and selects for bile-tolerant taxa. (kashyap2024criticalappraisalof pages 9-10)
- Response to lipopolysaccharide (GO:0032496): innate activation and mucosal inflammation. (roszkowska2024smallintestinalbacteriala pages 9-11)
- Tight junction assembly (GO:0070830) and epithelial barrier establishment (GO:0060627): inflammatory/metabolic disruption increases permeability. (kashyap2024criticalappraisalof pages 9-10, roszkowska2024smallintestinalbacteriala pages 9-11)
- Vitamin B12 transport (GO:0015889): bacterial competition and mucosal injury reduce B12 availability. (roszkowska2024smallintestinalbacteriala pages 5-7)

4) Cellular Components (GO-CC)
- Tight junction (GO:0005923) and brush border (GO:0031526): structural targets of barrier/digestive impairment. (roszkowska2024smallintestinalbacteriala pages 5-7, kashyap2024criticalappraisalof pages 9-10)
- Extracellular space (GO:0005615): lumenal compartment where microbial metabolites interact with epithelium. (roszkowska2024smallintestinalbacteriala pages 5-7)

5) Disease Progression (Sequence of events)
- Initiation: Predisposing factors (motility disorders with MMC failure, anatomic stasis including loss of ileocecal valve or surgical blind loops, hypochlorhydria/long-term PPI use, impaired bile flow/secretions, and immune deficiency) undermine small-intestinal antibacterial defenses. (nowakowski2024smallintestinalbacterial pages 4-7, kashyap2024criticalappraisalof pages 9-10)
- Overgrowth and metabolic shift: Increased bacterial density/compositional shift to fermenters; enhanced carbohydrate fermentation and gas production; bile-salt deconjugation drives fat malabsorption. (kashyap2024criticalappraisalof pages 9-10, roszkowska2024smallintestinalbacteriala pages 5-7)
- Epithelial/immune response: LPS and microbial metabolites induce innate (TLR2/TLR4) activation, mucosal inflammation, and tight-junction disruption; increased permeability with potential endotoxin translocation. (roszkowska2024smallintestinalbacteriala pages 9-11, roszkowska2024smallintestinalbacteriala pages 7-9)
- Clinical consequences: Malabsorption (vitamin B12 deficiency, fat-soluble vitamin deficiency), steatorrhea, weight loss, anemia; symptom clusters (bloating, pain, diarrhea/constipation). Chronic signaling through the gut–liver axis may contribute to hepatic injury, especially in susceptible hosts. (nowakowski2024smallintestinalbacterial pages 7-9, roszkowska2024smallintestinalbacteriala pages 5-7)

6) Phenotypic Manifestations (HP) with mechanistic links
- Abdominal pain (HP:0002027) and abdominal bloating (HP:0003270): due to gas production and luminal distention by fermentation products (H2/CH4/SCFAs). (roszkowska2024smallintestinalbacteriala pages 5-7)
- Diarrhea (HP:0002014) and/or constipation (HP:0002019): diarrhea from malabsorption and irritative metabolites; methane-associated slowed transit/constipation patterns in IMO. In SSc, diarrhea is significantly associated with SIBO (OR 5.9; 95% CI 2.9–16.0). (shah2023smallintestinalbacterial pages 5-11)
- Steatorrhea (HP:0002570) and weight loss (HP:0001824): bile-salt deconjugation and fat malabsorption with caloric loss. (roszkowska2024smallintestinalbacteriala pages 5-7)
- Macrocytic anemia (HP:0001993) from vitamin B12 deficiency; iron deficiency anemia (HP:0001930) from combined malabsorption/inflammation. (nowakowski2024smallintestinalbacterial pages 7-9, roszkowska2024smallintestinalbacteriala pages 5-7)
- Failure to thrive in pediatrics (HP:0001508): growth impacts via nutrient malabsorption. (roszkowska2024smallintestinalbacteriala pages 5-7)

Recent developments and latest research (2023–2024 priority)
- Expert practice update (ESNM/ANMS, 2024): Provides a critical appraisal of the SIBO hypothesis and cautions on overreliance on breath testing, emphasizing mechanistic heterogeneity (motility, acid suppression, altered bile, immune defenses) and the need for rigorous diagnostics. URL: https://doi.org/10.1111/nmo.14817 (May 2024). (kashyap2024criticalappraisalof pages 9-10)
- Broad disease associations (2023): A comprehensive epidemiologic review synthesizes condition-specific SIBO prevalence and risk factors across systemic, hepatic, cardiometabolic, and functional disorders, underscoring heterogeneity and diagnostic variability. URL: https://doi.org/10.3748/wjg.v29.i22.3400 (Jun 14, 2023). (efremova2023epidemiologyofsmall pages 10-12, efremova2023epidemiologyofsmall pages 4-6, efremova2023epidemiologyofsmall pages 2-4)
- Systemic sclerosis meta-analysis (2023): High SIBO prevalence in SSc by breath testing and a strong association with diarrhea; rifaximin more effective than rotating antibiotics in subgroup analyses, informing management. URL: https://doi.org/10.5056/jnm22168 (Apr 2023). (shah2023smallintestinalbacterial pages 1-5, shah2023smallintestinalbacterial pages 5-11)
- Integrative overviews (2024): Reviews connect SIBO with multiple disease groups and emphasize mechanisms: fermentation, SCFAs, bile deconjugation, LPS/TLR signaling, PPI exposure, and dysmotility/anatomy. URL: https://doi.org/10.20944/preprints202403.1571.v1 (Mar 2024). (roszkowska2024smallintestinalbacteriala pages 5-7, roszkowska2024smallintestinalbacteriala pages 7-9)

Current applications and real-world implementations
- Clinical evaluation: Breath testing (glucose, lactulose) widely used but with recognized limitations and heterogeneity in protocols and interpretation; direct culture remains a reference in select settings. Practice update urges careful test selection and interpretation. (kashyap2024criticalappraisalof pages 9-10)
- Therapeutic strategies: Target underlying cause (motility, acid suppression minimization, anatomic issues), antibiotics (e.g., rifaximin), and nutritional correction. Reviews emphasize prokinetics in dysmotility, cautious PPI use, and addressing risk factors in high-risk populations. (roszkowska2024smallintestinalbacteriala pages 7-9, nowakowski2024smallintestinalbacterial pages 7-9)

Expert opinions and analysis (authoritative sources)
- ESNM/ANMS clinical practice update (2024) highlights: the “SIBO-IBS hypothesis” spurred research but evidence for broad causality is limited by diagnostic imperfections; mechanistic contributors (dysmotility, bile, pH, immune defenses) should drive individualized evaluation and management. URL: https://doi.org/10.1111/nmo.14817 (May 2024). (kashyap2024criticalappraisalof pages 9-10)

Relevant statistics and data from recent studies
- Overall detection in gastroenterology clinic cohorts: ~33.8% by breath testing; IBS pooled prevalence ~31–37% with increased odds vs controls (pooled OR ≈ 3.7). URL: https://doi.org/10.3748/wjg.v29.i22.3400 (Jun 2023). (efremova2023epidemiologyofsmall pages 2-4, efremova2023epidemiologyofsmall pages 12-13)
- IBD association (meta-analyses): Pooled prevalence in IBD ~31.0% (95% CI 25.2–37.1) with OR 5.25 (95% CI 2.96–9.32) vs healthy controls; higher in Crohn’s disease (32.2%) than ulcerative colitis (27.8%). URL: https://doi.org/10.3389/fmed.2024.1490506 (Jan 2025, search through Mar 2024). (feng2025prevalenceandpredictors pages 14-14)
- Systemic sclerosis: SIBO prevalence ~44.4% by breath test; diarrhea risk increased (OR 5.9). URL: https://doi.org/10.5056/jnm22168 (Apr 2023). (shah2023smallintestinalbacterial pages 5-11, shah2023smallintestinalbacterial pages 1-5)
- PPI exposure: Meta-analytic signal for increased SIBO with PPIs (OR 1.71, 95% CI 1.20–2.43), with higher detection after >1 year continuous use; elderly cohorts showed higher breath-test positivity with continuous vs on-demand PPI therapy. URL: https://doi.org/10.3748/wjg.v29.i22.3400 (Jun 2023). (efremova2023epidemiologyofsmall pages 2-4)
- Broader risk estimates (preprint synthesis): PPI use associated with OR 7.59 (95% CI 1.81–31.89) vs non-users in selected cohorts; prevalence examples include functional dyspepsia 34.7%, IBS 36.7%, Crohn’s 25.3%, UC 14.3%, cirrhosis up to 51.1%. URL: https://doi.org/10.20944/preprints202504.0613.v2 (Apr 8, 2025). (zhang2025confusioninbreath pages 5-7)

Direct quotes supporting key statements
- “SIBO is manifested not only by a quantitative change in microorganisms but also by a qualitative change,” with fermentation generating “hydrogen and methane… [and] short‑chain fatty acids,” and LPS that “can further induce inflammation of enterocytes.” URL: https://doi.org/10.20944/preprints202403.1571.v1 (Mar 26, 2024). (roszkowska2024smallintestinalbacteriala pages 3-5, roszkowska2024smallintestinalbacteriala pages 7-9)
- Normal proximal small bowel milieu: “high concentrations of bile which is bacteriostatic… The low microbial density and diversity in the proximal small intestine restricts carbohydrate fermentation and bile deconjugation,” whereas perturbations increase density to “10^7–8 CFU/mL.” URL: https://doi.org/10.1111/nmo.14817 (May 2024). (kashyap2024criticalappraisalof pages 9-10)
- Predisposing factors to overgrowth include “altered anatomy… slower small intestinal transit,” “increase in pH due to… proton pump inhibitors,” and “loss of antibacterial defences.” URL: https://doi.org/10.1111/nmo.14817 (May 2024). (kashyap2024criticalappraisalof pages 9-10)

Gene/protein annotations with ontology terms
- TLR4 (HGNC:11850): GO:0032496 response to LPS; located at plasma membrane/epithelial and immune cells; role: innate activation and permeability increase in SIBO. (roszkowska2024smallintestinalbacteriala pages 9-11)
- TLR2 (HGNC:11848): GO:0032496; role: innate detection of bacterial components in SIBO mucosa. (roszkowska2024smallintestinalbacteriala pages 9-11)
- Secretory IgA (IGHA1/2): GO:0006955 immune response; role: immune exclusion—deficiency predisposes to SIBO. (kashyap2024criticalappraisalof pages 9-10)

Cell type involvement (CL terms)
- Enterocyte (CL:0000584): barrier and absorption dysfunction. (roszkowska2024smallintestinalbacteriala pages 5-7)
- Paneth cell (CL:0000587): antimicrobial defense; dysfunction facilitates overgrowth. (kashyap2024criticalappraisalof pages 9-10)
- Plasma cell (CL:0000786): mucosal IgA production. (kashyap2024criticalappraisalof pages 9-10)

Anatomical locations (UBERON terms)
- Small intestine (UBERON:0002108); jejunum (UBERON:0002115); ileum (UBERON:0002116); ileocecal valve (UBERON:0001276). (roszkowska2024smallintestinalbacteriala pages 3-5)

Chemical entities (CHEBI terms)
- LPS (CHEBI:16412); bile acids (CHEBI:15889); SCFAs (CHEBI:26666); hydrogen (CHEBI:18276); methane (CHEBI:16183); vitamin B12 (CHEBI:17697). (roszkowska2024smallintestinalbacteriala pages 5-7, kashyap2024criticalappraisalof pages 9-10, feng2025prevalenceandpredictors pages 14-14)

Phenotype associations (HP terms)
- Abdominal pain (HP:0002027), bloating (HP:0003270), diarrhea (HP:0002014), constipation (HP:0002019), steatorrhea (HP:0002570), weight loss (HP:0001824), macrocytic anemia (HP:0001993), failure to thrive (HP:0001508). (shah2023smallintestinalbacterial pages 5-11, roszkowska2024smallintestinalbacteriala pages 5-7)

Evidence items (PMIDs/DOIs/URLs and dates)
- Kashyap et al. Critical appraisal of the SIBO hypothesis and breath testing (ESNM/ANMS). Neurogastroenterol Motil. May 2024. DOI: 10.1111/nmo.14817; URL: https://doi.org/10.1111/nmo.14817. (kashyap2024criticalappraisalof pages 9-10)
- Efremova et al. Epidemiology of small intestinal bacterial overgrowth. World J Gastroenterol. Jun 14, 2023. DOI: 10.3748/wjg.v29.i22.3400; URL: https://doi.org/10.3748/wjg.v29.i22.3400. (efremova2023epidemiologyofsmall pages 2-4, efremova2023epidemiologyofsmall pages 4-6, efremova2023epidemiologyofsmall pages 12-13)
- Shah et al. SIBO complicating GI manifestations of systemic sclerosis: systematic review/meta-analysis. J Neurogastroenterol Motil. Apr 2023. DOI: 10.5056/jnm22168; URL: https://doi.org/10.5056/jnm22168. (shah2023smallintestinalbacterial pages 1-5, shah2023smallintestinalbacterial pages 5-11)
- Roszkowska et al. Small intestinal bacterial overgrowth and twelve groups of diseases—current state of knowledge (preprint). Posted Mar 26, 2024. DOI: 10.20944/preprints202403.1571.v1; URL: https://doi.org/10.20944/preprints202403.1571.v1. (roszkowska2024smallintestinalbacteriala pages 5-7, roszkowska2024smallintestinalbacteriala pages 7-9, roszkowska2024smallintestinalbacteriala pages 3-5, roszkowska2024smallintestinalbacteriala pages 9-11)
- Nowakowski et al. Small Intestinal Bacterial Overgrowth Syndrome: New Clinical Insights for Multimorbid and High-Risk Patients. Quality in Sport. Dec 2024. DOI: 10.12775/qs.2024.36.56729; URL: https://doi.org/10.12775/qs.2024.36.56729. (nowakowski2024smallintestinalbacterial pages 7-9, nowakowski2024smallintestinalbacterial pages 4-7)
- Feng et al. Prevalence and predictors of small intestinal bacterial overgrowth in inflammatory bowel disease: meta-analysis. Frontiers in Medicine. Jan 2025 (search through Mar 2024). DOI: 10.3389/fmed.2024.1490506; URL: https://doi.org/10.3389/fmed.2024.1490506. (feng2025prevalenceandpredictors pages 14-14)
- Zhang et al. Confusion in Breath Test for Diagnosing Bacterial Overgrowth in the Small Intestine (preprint). Posted Apr 8, 2025. DOI: 10.20944/preprints202504.0613.v2; URL: https://doi.org/10.20944/preprints202504.0613.v2. (zhang2025confusioninbreath pages 5-7)

Notes on evidence strength and gaps
- While mechanistic links (e.g., LPS–TLR signaling, bile-acid deconjugation) are biologically plausible and supported by thematic reviews, high-quality human studies directly connecting these pathways to SIBO clinical outcomes remain limited and confounded by diagnostic heterogeneity. The ESNM/ANMS update encourages careful attribution of symptoms to SIBO and judicious antibiotic use. (kashyap2024criticalappraisalof pages 9-10)


References

1. (roszkowska2024smallintestinalbacteriala pages 5-7): Paulina Roszkowska, Emilia Klimczak, Ewa Ostrycharz, Aleksandra Rączka, Iwona Wojciechowska-Koszko, Andrzej Dybus, Yeong-Hsiang Cheng, Yu-Hsiang Yu, Szymon Mazgaj, and Beata Hukowska-Szematowicz. Small intestinal bacterial overgrowth (sibo) and twelve groups of diseases related- current state of knowledge. Unknown journal, Mar 2024. URL: https://doi.org/10.20944/preprints202403.1571.v1, doi:10.20944/preprints202403.1571.v1.

2. (roszkowska2024smallintestinalbacteriala pages 7-9): Paulina Roszkowska, Emilia Klimczak, Ewa Ostrycharz, Aleksandra Rączka, Iwona Wojciechowska-Koszko, Andrzej Dybus, Yeong-Hsiang Cheng, Yu-Hsiang Yu, Szymon Mazgaj, and Beata Hukowska-Szematowicz. Small intestinal bacterial overgrowth (sibo) and twelve groups of diseases related- current state of knowledge. Unknown journal, Mar 2024. URL: https://doi.org/10.20944/preprints202403.1571.v1, doi:10.20944/preprints202403.1571.v1.

3. (kashyap2024criticalappraisalof pages 9-10): Purna Kashyap, Paul Moayyedi, Eamonn M. M. Quigley, Magnus Simren, and Stephen Vanner. Critical appraisal of the sibo hypothesis and breath testing: a clinical practice update endorsed by the european society of neurogastroenterology and motility (esnm) and the american neurogastroenterology and motility society (anms). Neurogastroenterology & Motility, May 2024. URL: https://doi.org/10.1111/nmo.14817, doi:10.1111/nmo.14817. This article has 48 citations and is from a peer-reviewed journal.

4. (nowakowski2024smallintestinalbacterial pages 4-7): Krzysztof Nowakowski, Zuzanna Mularczyk, Magdalena Reclik, Piotr Oleksy, and Maciej Tenderenda. Small intestinal bacterial overgrowth syndrome: new clinical insights for multimorbid and high-risk patients. Quality in Sport, 36:56729, Dec 2024. URL: https://doi.org/10.12775/qs.2024.36.56729, doi:10.12775/qs.2024.36.56729. This article has 1 citations.

5. (efremova2023epidemiologyofsmall pages 2-4): Irina Efremova, Roman Maslennikov, Elena Poluektova, Ekaterina Vasilieva, Yury Zharikov, Andrey Suslov, Yana Letyagina, Evgenii Kozlov, Anna Levshina, and Vladimir Ivashkin. Epidemiology of small intestinal bacterial overgrowth. World Journal of Gastroenterology, 29:3400-3421, Jun 2023. URL: https://doi.org/10.3748/wjg.v29.i22.3400, doi:10.3748/wjg.v29.i22.3400. This article has 107 citations and is from a poor quality or predatory journal.

6. (roszkowska2024smallintestinalbacteriala pages 9-11): Paulina Roszkowska, Emilia Klimczak, Ewa Ostrycharz, Aleksandra Rączka, Iwona Wojciechowska-Koszko, Andrzej Dybus, Yeong-Hsiang Cheng, Yu-Hsiang Yu, Szymon Mazgaj, and Beata Hukowska-Szematowicz. Small intestinal bacterial overgrowth (sibo) and twelve groups of diseases related- current state of knowledge. Unknown journal, Mar 2024. URL: https://doi.org/10.20944/preprints202403.1571.v1, doi:10.20944/preprints202403.1571.v1.

7. (feng2025prevalenceandpredictors pages 14-14): Xin Feng, Jie Hu, and Xin Zhang. Prevalence and predictors of small intestinal bacterial overgrowth in inflammatory bowel disease: a meta-analysis. Frontiers in Medicine, Jan 2025. URL: https://doi.org/10.3389/fmed.2024.1490506, doi:10.3389/fmed.2024.1490506. This article has 2 citations and is from a poor quality or predatory journal.

8. (roszkowska2024smallintestinalbacteriala pages 3-5): Paulina Roszkowska, Emilia Klimczak, Ewa Ostrycharz, Aleksandra Rączka, Iwona Wojciechowska-Koszko, Andrzej Dybus, Yeong-Hsiang Cheng, Yu-Hsiang Yu, Szymon Mazgaj, and Beata Hukowska-Szematowicz. Small intestinal bacterial overgrowth (sibo) and twelve groups of diseases related- current state of knowledge. Unknown journal, Mar 2024. URL: https://doi.org/10.20944/preprints202403.1571.v1, doi:10.20944/preprints202403.1571.v1.

9. (nowakowski2024smallintestinalbacterial pages 7-9): Krzysztof Nowakowski, Zuzanna Mularczyk, Magdalena Reclik, Piotr Oleksy, and Maciej Tenderenda. Small intestinal bacterial overgrowth syndrome: new clinical insights for multimorbid and high-risk patients. Quality in Sport, 36:56729, Dec 2024. URL: https://doi.org/10.12775/qs.2024.36.56729, doi:10.12775/qs.2024.36.56729. This article has 1 citations.

10. (shah2023smallintestinalbacterial pages 5-11): Ayesha Shah, Veenaa Pakeerathan, Michael P Jones, Purna C Kashyap, Kate Virgo, Thomas Fairlie, Mark Morrison, Uday C Ghoshal, and Gerald J Holtmann. Small intestinal bacterial overgrowth complicating gastrointestinal manifestations of systemic sclerosis: a systematic review and meta-analysis. Journal of Neurogastroenterology and Motility, 29:132-144, Apr 2023. URL: https://doi.org/10.5056/jnm22168, doi:10.5056/jnm22168. This article has 20 citations and is from a peer-reviewed journal.

11. (efremova2023epidemiologyofsmall pages 10-12): Irina Efremova, Roman Maslennikov, Elena Poluektova, Ekaterina Vasilieva, Yury Zharikov, Andrey Suslov, Yana Letyagina, Evgenii Kozlov, Anna Levshina, and Vladimir Ivashkin. Epidemiology of small intestinal bacterial overgrowth. World Journal of Gastroenterology, 29:3400-3421, Jun 2023. URL: https://doi.org/10.3748/wjg.v29.i22.3400, doi:10.3748/wjg.v29.i22.3400. This article has 107 citations and is from a poor quality or predatory journal.

12. (efremova2023epidemiologyofsmall pages 4-6): Irina Efremova, Roman Maslennikov, Elena Poluektova, Ekaterina Vasilieva, Yury Zharikov, Andrey Suslov, Yana Letyagina, Evgenii Kozlov, Anna Levshina, and Vladimir Ivashkin. Epidemiology of small intestinal bacterial overgrowth. World Journal of Gastroenterology, 29:3400-3421, Jun 2023. URL: https://doi.org/10.3748/wjg.v29.i22.3400, doi:10.3748/wjg.v29.i22.3400. This article has 107 citations and is from a poor quality or predatory journal.

13. (shah2023smallintestinalbacterial pages 1-5): Ayesha Shah, Veenaa Pakeerathan, Michael P Jones, Purna C Kashyap, Kate Virgo, Thomas Fairlie, Mark Morrison, Uday C Ghoshal, and Gerald J Holtmann. Small intestinal bacterial overgrowth complicating gastrointestinal manifestations of systemic sclerosis: a systematic review and meta-analysis. Journal of Neurogastroenterology and Motility, 29:132-144, Apr 2023. URL: https://doi.org/10.5056/jnm22168, doi:10.5056/jnm22168. This article has 20 citations and is from a peer-reviewed journal.

14. (efremova2023epidemiologyofsmall pages 12-13): Irina Efremova, Roman Maslennikov, Elena Poluektova, Ekaterina Vasilieva, Yury Zharikov, Andrey Suslov, Yana Letyagina, Evgenii Kozlov, Anna Levshina, and Vladimir Ivashkin. Epidemiology of small intestinal bacterial overgrowth. World Journal of Gastroenterology, 29:3400-3421, Jun 2023. URL: https://doi.org/10.3748/wjg.v29.i22.3400, doi:10.3748/wjg.v29.i22.3400. This article has 107 citations and is from a poor quality or predatory journal.

15. (zhang2025confusioninbreath pages 5-7): Yuanyuan Zhang, Pengchun Yang, Caihua Yan, Jing Wang, Xue Ran, Xiaoyan Gao, Gang Lei, Chunmei Ran, Tao Bai, Xiaohua Hou, and Chibing Dai. Confusion in breath test for diagnosing bacterial overgrowth in the small intestine. Apr 2025. URL: https://doi.org/10.20944/preprints202504.0613.v2, doi:10.20944/preprints202504.0613.v2.