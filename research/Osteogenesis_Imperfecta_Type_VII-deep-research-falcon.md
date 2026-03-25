---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-02-04T19:33:46.654546'
end_time: '2026-02-04T19:43:40.924086'
duration_seconds: 594.27
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Osteogenesis Imperfecta Type VII
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 30
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Osteogenesis Imperfecta Type VII
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Osteogenesis Imperfecta Type VII**.
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
- **Disease Name:** Osteogenesis Imperfecta Type VII
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Osteogenesis Imperfecta Type VII**.
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


# Disease Pathophysiology Research Report

## Target Disease
- Disease Name: Osteogenesis Imperfecta Type VII (OI type VII; CRTAP-related)
- MONDO ID: Not explicitly stated in cited texts; OI as a group is represented in MONDO. Nosology assigns CRTAP-related OI as Type VII in 2024 ISDS framework (dyadic nosology). (jovanovic2024updateonthe pages 8-9)
- Category: Mendelian, autosomal recessive

## Pathophysiology Description (Narrative)

Osteogenesis imperfecta type VII is a recessive collagen-processing disorder caused by biallelic variants in CRTAP that disrupt an endoplasmic reticulum (ER) prolyl 3‑hydroxylation complex composed of P3H1/LEPRE1 (catalytic subunit), CRTAP (stabilizing/helper subunit), and cyclophilin B/PPIB (prolyl isomerase/chaperone). This complex 3‑hydroxylates Pro986 on each α1(I) chain of type I collagen and supports procollagen folding. Loss of CRTAP destabilizes the complex, reduces or abolishes α1(I) Pro986 3‑hydroxyproline, delays helix folding with “over‑modification,” impairs collagen secretion and matrix deposition, alters fibril structure and crosslinking, and ultimately weakens bone. Mouse and human studies show resultant osteoblast dysfunction with reduced osteoid, growth‑plate cartilage disorganization causing rhizomelia, and extraskeletal involvement such as primary lung parenchymal defects; excessive TGF‑β signaling is implicated as a shared downstream mechanism linking matrix abnormalities to cell signaling. (zhou2024geneticanalysisphenotypic pages 1-1, marini2010nullmutationsin pages 4-5, marini2010nullmutationsin pages 2-4, valli2012deficiencyofcrtap pages 1-2, barnes2006deficiencyofcartilageassociated pages 1-2, dimori2020respiratorydefectsin pages 1-6)

| Category | Entity (ontology) | Mechanism / Role | Key Findings | Source (Year, DOI/URL) | Citation ID |
|---|---|---|---|---|---|
| Gene / Protein | CRTAP (HGNC:2387) | ER-resident cofactor that stabilizes P3H1 in the prolyl 3‑hydroxylation complex | Biallelic CRTAP loss → markedly reduced CRTAP mRNA/protein, loss/reduction of Pro986 3‑hydroxylation on COL1A1, impaired collagen folding/secretion, reduced osteoid and osteoblast numbers, severe osteoporosis and deformity in patients | 2024, Zhou et al., J Clin Endocrinol Metab, DOI: 10.1210/clinem/dgae025; 2006, Barnes et al., NEJM, DOI: 10.1056/NEJMoa063804 | (zhou2024geneticanalysisphenotypic pages 1-1, barnes2006deficiencyofcartilageassociated pages 1-2) |
| Gene / Protein | LEPRE1 / P3H1 (HGNC:18684) | Catalytic subunit of the P3H1–CRTAP–CyPB complex performing Pro986 3‑hydroxylation | Loss/null mutations abolish Pro986 3‑hydroxylation, produce recessive OI phenotypes (growth deficiency, osteopenia, cartilage disorganization) | 2010, Marini et al., Cell Tissue Res, DOI: 10.1007/s00441-009-0872-0; 2024, Jovanovic & Marini review, DOI: 10.1007/s00223-024-01266-5 | (marini2010nullmutationsin pages 4-5, jovanovic2024updateonthe pages 8-9) |
| Gene / Protein | PPIB / Cyclophilin B (HGNC:9250) | Peptidyl‑prolyl isomerase / chaperone in the complex that aids procollagen folding | Participates in complex with P3H1 and CRTAP; loss or dysfunction perturbs folding/isomerization contributing to overmodified collagen and matrix defects | 2010, Marini et al., DOI: 10.1007/s00441-009-0872-0; 2012, Valli et al., Clin Genet, DOI: 10.1111/j.1399-0004.2011.01794.x | (marini2010nullmutationsin pages 4-5, valli2012deficiencyofcrtap pages 1-2) |
| Substrate / Structural | Type I collagen COL1A1 (HGNC:2197) | Major fibrillar collagen; Pro986 in α1(I) is 3‑hydroxylated by the complex | Lack of Pro986 3‑hydroxylation → delayed helix formation, helical overmodification, altered crosslinking and fibril diameter, poor matrix deposition → weaker bone | 2024, Zhou et al., DOI: 10.1210/clinem/dgae025; 2012, Valli et al., DOI: 10.1111/j.1399-0004.2011.01794.x; 2006, Barnes et al., DOI: 10.1056/NEJMoa063804 | (zhou2024geneticanalysisphenotypic pages 1-1, valli2012deficiencyofcrtap pages 1-2, barnes2006deficiencyofcartilageassociated pages 1-2) |
| Cell type | Osteoblast (CL:0000062) | Primary cell synthesizing type I collagen and mineralizing matrix | CRTAP-deficient osteoblasts: ↓CRTAP expression, ↓osteoid volume and osteoblast numbers, impaired matrix formation; some CRTAP-null cells show altered proliferation/protein secretion (functional perturbation of osteoblast biology) | 2024, Zhou et al., J Clin Endocrinol Metab, DOI: 10.1210/clinem/dgae025; 2006, Barnes et al., NEJM, DOI: 10.1056/NEJMoa063804 | (zhou2024geneticanalysisphenotypic pages 1-1, barnes2006deficiencyofcartilageassociated pages 1-2) |
| Cell type | Chondrocyte (CL:0000138) | Growth‑plate cartilage cells reliant on properly modified collagen | Crtap−/− mice: disorganized proliferative chondrocytes, metaphyseal/growth‑plate abnormalities and rhizomelic shortening → contributes to short stature / limb deformities in type VII OI | 2010, Marini et al., DOI: 10.1007/s00441-009-0872-0 | (marini2010nullmutationsin pages 4-5) |
| Tissue / Cell | Lung fibroblast (CL:0002553) / Lung (UBERON:0002048) | Synthesis of interstitial collagen in lung parenchyma | CrtapKO mice show altered collagen PTMs in lung fibroblasts, emphysema‑like parenchymal changes, abnormal lung mechanics; increased TGF‑β signaling seen and anti‑TGF‑β partially rescues phenotype | 2020, Dimori et al., Am J Physiol Lung Cell Mol Physiol, DOI: 10.1152/ajplung.00313.2019; 2024, Zhou et al. (discussion of lung findings) DOI: 10.1210/clinem/dgae025 | (dimori2020respiratorydefectsin pages 1-6, zhou2024geneticanalysisphenotypic pages 1-1) |
| Tissue | Growth plate cartilage (UBERON:0002429) | Site of endochondral growth dependent on ECM integrity | Patient and mouse data: metaphyseal enlargement, 'popcorn' epiphyses, femoral/tibial deformities indicating growth‑plate disruption from abnormal collagen matrix | 2024, Zhou et al., DOI: 10.1210/clinem/dgae025; 2010, Marini et al., DOI: 10.1007/s00441-009-0872-0 | (zhou2024geneticanalysisphenotypic pages 1-1, marini2010nullmutationsin pages 4-5) |
| Cellular component / ECM | ECM / Collagen fibril (GO:0005583 / GO:0030199) | Extracellular assembly of collagen fibrils that determine bone matrix quality | CRTAP deficiency → markedly reduced collagen deposition into matrix, disorganized fibrils, altered fibril diameter and crosslinking → compromised bone mechanical properties | 2012, Valli et al., Clin Genet, DOI: 10.1111/j.1399-0004.2011.01794.x; 2006, Barnes et al., NEJM, DOI: 10.1056/NEJMoa063804; 2024, Zhou et al., DOI: 10.1210/clinem/dgae025 | (valli2012deficiencyofcrtap pages 1-2, barnes2006deficiencyofcartilageassociated pages 1-2, zhou2024geneticanalysisphenotypic pages 1-1) |
| Organelle / Compartment | Endoplasmic reticulum (GO:0005783) | Location of the CRTAP–P3H1–CyPB complex and collagen PTMs/folding | CRTAP/P3H1 complex loss → delayed procollagen folding (overmodification), ER perturbation/UPR signals; chemical chaperone (4‑phenylbutyrate) shown to reduce ER stress/overmodified collagen in models | 2012, Valli et al., DOI: 10.1111/j.1399-0004.2011.01794.x; 2024, Zhou et al., DOI: 10.1210/clinem/dgae025 | (valli2012deficiencyofcrtap pages 1-2, zhou2024geneticanalysisphenotypic pages 9-9) |
| Pathway / Process | Prolyl 3‑hydroxylation (GO:0019794) | Post‑translational hydroxylation of Pro986 on α1(I) by P3H1 within complex | Essential PTM for correct helix assembly; absent/reduced in CRTAP or P3H1 nulls → biochemical signature of recessive OI type VII/VIII | 2010, Marini et al., DOI: 10.1007/s00441-009-0872-0; 2006, Barnes et al., NEJM, DOI: 10.1056/NEJMoa063804; 2024, Zhou et al., DOI: 10.1210/clinem/dgae025 | (marini2010nullmutationsin pages 4-5, barnes2006deficiencyofcartilageassociated pages 1-2, zhou2024geneticanalysisphenotypic pages 1-1) |
| Pathway / Process | Protein folding / chaperone activity (GO:0006457) | CyPB isomerase + ER chaperones assist procollagen folding; folding rate influences extent of other PTMs | Delayed folding (due to complex loss) → helical overmodification; chemical chaperones partially correct aberrant modifications in models (e.g., 4‑PBA) | 2012, Valli et al., DOI: 10.1111/j.1399-0004.2011.01794.x; 2024, Zhou et al., DOI: 10.1210/clinem/dgae025 | (valli2012deficiencyofcrtap pages 1-2, zhou2024geneticanalysisphenotypic pages 9-9) |
| Pathway / Process | Collagen biosynthetic process (GO:0032964) | Encompasses PTMs, folding, secretion and matrix assembly | Disruption at PTM/folding step reduces matrix deposition and mineralized bone, causing fragility; phenotype connects molecular defect → cellular dysfunction → clinical fractures | 2010, Marini et al., DOI: 10.1007/s00441-009-0872-0; 2012, Valli et al., DOI: 10.1111/j.1399-0004.2011.01794.x | (marini2010nullmutationsin pages 4-5, valli2012deficiencyofcrtap pages 1-2) |
| Pathway / Process | TGF‑β signaling (GO:0007179) | Matrix‑cell signaling axis modulated by collagen–proteoglycan interactions | Excessive TGF‑β signaling observed in Crtap−/− models and contributes to bone (and lung) pathology; anti‑TGF‑β antibodies improve bone phenotype in mice (preclinical rationale) | 2014 (mechanistic landmark cited in reviews), and 2020/2024 model data showing elevated TGF‑β and partial rescue via anti‑TGF‑β (see Dimori 2020; Zhou 2024) DOI: 10.1152/ajplung.00313.2019; DOI: 10.1210/clinem/dgae025 | (dimori2020respiratorydefectsin pages 1-6, zhou2024geneticanalysisphenotypic pages 10-11, jovanovic2024updateonthe pages 8-9) |
| Pathway / Process | Bone mineralization (GO:0030282) | Downstream outcome of osteoblast function and matrix quality | CRTAP deficiency → low bone mass/osteoporosis and deformity; preclinical sclerostin antibody improves bone microarchitecture in Crtap−/− mice; clinical bisphosphonate use reported with vertebral reshaping and fracture reduction in small CRTAP case series | 2024, Zhou et al. (patient response to zoledronic acid) DOI: 10.1210/clinem/dgae025; preclinical sclerostin antibody cited in Zhou (2024) DOI: 10.1210/clinem/dgae025 | (zhou2024geneticanalysisphenotypic pages 4-5, zhou2024geneticanalysisphenotypic pages 10-11) |


*Table: A concise evidence‑mapping table summarizing molecular players, cells, compartments and pathways implicated in CRTAP‑related (Type VII) osteogenesis imperfecta, with key mechanistic findings and primary sources (2020–2024) for quick reference.*

## Structured Sections Aligned to Research Objectives

### 1. Core Pathophysiology
- Primary mechanisms: Loss of CRTAP disrupts the ER prolyl 3‑hydroxylation complex (P3H1–CRTAP–PPIB), eliminating or severely reducing 3‑hydroxylation of α1(I) Pro986; this leads to delayed procollagen folding (helical over‑modification), impaired secretion, and defective extracellular matrix (ECM) assembly with reduced collagen deposition and disorganized fibrils. (marini2010nullmutationsin pages 4-5, marini2010nullmutationsin pages 2-4, valli2012deficiencyofcrtap pages 1-2, barnes2006deficiencyofcartilageassociated pages 1-2)
- Dysregulated pathways: Collagen biosynthesis/processing (prolyl 3‑hydroxylation, protein folding), ECM organization, and TGF‑β signaling become aberrant. Excessive TGF‑β signaling was demonstrated as a common mechanism in OI, including Crtap−/− models, with anti‑TGF‑β antibodies rescuing bone and partially improving lung abnormalities in mice. (dimori2020respiratorydefectsin pages 1-6)
- Affected cellular processes: Osteoblast matrix production and osteoid formation are reduced in human CRTAP‑mutant bone; growth‑plate chondrocyte organization is disrupted in Crtap−/− mice; lung fibroblasts synthesize abnormally modified collagen leading to parenchymal and mechanical defects. (zhou2024geneticanalysisphenotypic pages 1-1, marini2010nullmutationsin pages 4-5, dimori2020respiratorydefectsin pages 1-6)

Direct quotes supporting key claims:
- “This is the first evidence that collagen defects in OI cause primary changes in lung parenchyma and several respiratory parameters and thus negatively impact lung function.” (Dimori et al., 2020; Am J Physiol Lung Cell Mol Physiol; https://doi.org/10.1152/ajplung.00313.2019) (dimori2020respiratorydefectsin pages 1-6)
- “Deficiency of cartilage‑associated protein [CRTAP]… [leads to] complete loss of Pro986 hydroxylation in α1(I)” with severe skeletal pathology in mouse and human recessive OI. (Barnes et al., 2006; N Engl J Med; https://doi.org/10.1056/NEJMoa063804) (barnes2006deficiencyofcartilageassociated pages 1-2)
- In patient bone: “significantly reduced prolyl 3‑hydroxylation at Pro986 in the α1 chain of type I collagen and invisible active bone formation in bone,” with decreased CRTAP mRNA/protein and reduced osteoid volume/osteoblast numbers. (Zhou et al., 2024; J Clin Endocrinol Metab; https://doi.org/10.1210/clinem/dgae025) (zhou2024geneticanalysisphenotypic pages 1-1)

### 2. Key Molecular Players
- Genes/Proteins (HGNC):
  - CRTAP (HGNC:2387): ER complex subunit stabilizing P3H1; loss causes OI type VII. (barnes2006deficiencyofcartilageassociated pages 1-2, zhou2024geneticanalysisphenotypic pages 1-1)
  - LEPRE1/P3H1 (HGNC:18684): catalytic prolyl 3‑hydroxylase 1 for α1(I) Pro986; null alleles cause recessive OI. (marini2010nullmutationsin pages 4-5)
  - PPIB/Cyclophilin B (HGNC:9250): peptidyl‑prolyl isomerase aiding procollagen folding; complex member. (marini2010nullmutationsin pages 4-5, valli2012deficiencyofcrtap pages 1-2)
  - COL1A1 (HGNC:2197): type I collagen α1 chain carrying the Pro986 3‑Hyp site; aberrant PTMs when complex is lost. (valli2012deficiencyofcrtap pages 1-2, zhou2024geneticanalysisphenotypic pages 1-1)
- Chemical entities (CHEBI; selected): 4‑phenylbutyrate (CHEBI:46195) as ER chemical chaperone rescue in models; zoledronic acid (CHEBI:46550) and denosumab (CHEBI:68481) in clinical management. (zhou2024geneticanalysisphenotypic pages 10-11, zhou2024geneticanalysisphenotypic pages 4-5)
- Cell types (CL): osteoblast (CL:0000062), chondrocyte (CL:0000138), lung fibroblast (CL:0002553). (zhou2024geneticanalysisphenotypic pages 1-1, marini2010nullmutationsin pages 4-5, dimori2020respiratorydefectsin pages 1-6)
- Anatomical locations (UBERON): bone (UBERON:0001474), lung (UBERON:0002048), growth plate cartilage (UBERON:0002429). (dimori2020respiratorydefectsin pages 1-6, marini2010nullmutationsin pages 4-5)

### 3. Biological Processes (for GO annotation)
- Prolyl 3‑hydroxylation (GO:0019794): modification of α1(I) Pro986 by P3H1 complex; absent/reduced in CRTAP or P3H1 loss. (marini2010nullmutationsin pages 4-5, barnes2006deficiencyofcartilageassociated pages 1-2)
- Protein folding (GO:0006457): CyPB‑assisted isomerization/folding; delayed folding underlies over‑modification. (valli2012deficiencyofcrtap pages 1-2)
- Collagen biosynthetic process (GO:0032964): includes PTMs, folding, secretion; impaired in CRTAP deficiency. (marini2010nullmutationsin pages 4-5, valli2012deficiencyofcrtap pages 1-2)
- TGF‑β receptor signaling pathway (GO:0007179): elevated activity contributes to bone/lung phenotypes; neutralization improves bone in models. (dimori2020respiratorydefectsin pages 1-6)
- Bone mineralization (GO:0030282): reduced due to impaired osteoblast matrix; improved in mice with sclerostin antibody; improved BMD/vertebral remodeling in human case on antiresorptives. (zhou2024geneticanalysisphenotypic pages 10-11, zhou2024geneticanalysisphenotypic pages 4-5)

### 4. Cellular Components
- Endoplasmic reticulum (GO:0005783): site of the P3H1–CRTAP–PPIB complex and procollagen PTMs/folding. (marini2010nullmutationsin pages 4-5)
- Extracellular matrix / collagen fibril (GO:0005583/GO:0030199): reduced collagen deposition and abnormal fibrillogenesis in CRTAP deficiency. (valli2012deficiencyofcrtap pages 1-2)

### 5. Disease Progression
- Initiation: Biallelic CRTAP variants reduce CRTAP expression/protein and destabilize the P3H1–CRTAP–PPIB complex. (zhou2024geneticanalysisphenotypic pages 1-1, marini2010nullmutationsin pages 4-5)
- Molecular consequence: Loss of α1(I) Pro986 3‑hydroxylation; delayed triple‑helix folding; helical over‑modification and abnormal crosslinking/fibril size. (marini2010nullmutationsin pages 4-5, valli2012deficiencyofcrtap pages 1-2)
- Cellular/tissue effects: Impaired secretion and ECM deposition; reduced osteoid and osteoblast numbers; growth‑plate disorganization; excess TGF‑β signaling; lung parenchymal defects and abnormal mechanics in CrtapKO mice. (zhou2024geneticanalysisphenotypic pages 1-1, marini2010nullmutationsin pages 4-5, dimori2020respiratorydefectsin pages 1-6)
- Clinical manifestation: Early‑onset recurrent fractures, severe osteoporosis, deformities, rhizomelia, metaphyseal enlargement/‘popcorn’ epiphyses; extraskeletal features variable (some series without dentinogenesis imperfecta/blue sclera). (zhou2024geneticanalysisphenotypic pages 1-1, marini2010nullmutationsin pages 4-5)

### 6. Phenotypic Manifestations (HPO terms)
- Recurrent fractures (HP:0002757) and osteopenia/low BMD (HP:0000938), severe osteoporosis with deformities. (zhou2024geneticanalysisphenotypic pages 1-1)
- Rhizomelia/proximal limb shortening (HP:0008915) and short stature (HP:0004322). (marini2010nullmutationsin pages 4-5)
- Metaphyseal widening/“popcorn” epiphyses (HP:0100660). (zhou2024geneticanalysisphenotypic pages 1-1)
- Variable extraskeletal features: absent dentinogenesis imperfecta and blue sclera in some CRTAP cases in 2024 series. (zhou2024geneticanalysisphenotypic pages 4-5)

## Recent Developments and Applications (2023–2024 priority)
- Genetics and nosology: 2024 updates emphasize CRTAP/P3H1/PPIB as the 3‑hydroxylation complex underlying recessive OI types VII–IX and integrate these into ISDS dyadic nosology. (Calcified Tissue Int 2024; https://doi.org/10.1007/s00223-024-01266-5) (jovanovic2024updateonthe pages 8-9)
- Human bone mechanistic study: 2024 bone‑specimen evidence links CRTAP loss to reduced α1(I) Pro986 3‑hyp, decreased osteoblast numbers/osteoid, and no active bone formation; novel CRTAP splice variant described. (J Clin Endocrinol Metab 2024; https://doi.org/10.1210/clinem/dgae025) (zhou2024geneticanalysisphenotypic pages 1-1)
- Clinical management signals (2024 case data): zoledronic acid associated with vertebral body reshaping and 3‑year fracture freedom; sequential zoledronic acid→teriparatide→denosumab increased femoral neck BMD in a CRTAP patient. (J Clin Endocrinol Metab 2024; https://doi.org/10.1210/clinem/dgae025) (zhou2024geneticanalysisphenotypic pages 4-5)
- Preclinical therapeutics: anti‑TGF‑β rescues bone (and partially lung) in Crtap−/−; sclerostin antibody improves bone microarchitecture in Crtap−/−; 4‑phenylbutyrate reduces ER stress/over‑modification in models. (Nature Med 2014; https://doi.org/10.1038/nm.3544; AJPLung 2020; https://doi.org/10.1152/ajplung.00313.2019; citations within 2024 JCEM) (dimori2020respiratorydefectsin pages 1-6, zhou2024geneticanalysisphenotypic pages 10-11)

## Expert Opinions/Quotes
- “Excessive transforming growth factor‑β signaling is a common mechanism in osteogenesis imperfecta,” with anti‑TGF‑β normalizing bone phenotypes in both dominant and recessive OI murine models, including Crtap−/−. (Nature Med 2014; https://doi.org/10.1038/nm.3544) (dimori2020respiratorydefectsin pages 1-6)
- “CRTAP is required for prolyl 3‑hydroxylation… [and] Prolyl 3‑hydroxylase 1 and CRTAP are mutually stabilizing” in the ER complex, explaining why CRTAP loss leads to loss of the collagen 3‑hyp mark and folding delays. (Synthesized from Marini 2010 and Zhou 2024; URLs: https://doi.org/10.1007/s00441-009-0872-0; https://doi.org/10.1210/clinem/dgae025) (marini2010nullmutationsin pages 4-5, zhou2024geneticanalysisphenotypic pages 9-10)
- “This is the first evidence that collagen defects in OI cause primary changes in lung parenchyma…” highlighting extraskeletal primary pathology in Crtap deficiency. (AJPLung 2020; https://doi.org/10.1152/ajplung.00313.2019) (dimori2020respiratorydefectsin pages 1-6)

## Statistics/Data Points
- Human bone from CRTAP‑mutant patient: significantly reduced CRTAP mRNA/protein; markedly reduced prolyl 3‑hydroxylation at α1(I) Pro986; reduced osteoid volume and osteoblast numbers; no active bone formation. (JCEM 2024; https://doi.org/10.1210/clinem/dgae025) (zhou2024geneticanalysisphenotypic pages 1-1)
- ECM deposition: CRTAP‑deficient fibroblasts deposit only ~10–15% of normal collagen into matrix with disorganized fibrils; 3‑hyp at Pro986 as low as ~5% in a non‑lethal CRTAP case. (Clin Genet 2012; https://doi.org/10.1111/j.1399-0004.2011.01794.x) (valli2012deficiencyofcrtap pages 1-2)
- Lung mechanics in CrtapKO: increased elastance, decreased compliance, altered breathing cycle parameters, and emphysema‑like parenchymal changes; partial rescue with anti‑TGF‑β. (AJPLung 2020; https://doi.org/10.1152/ajplung.00313.2019) (dimori2020respiratorydefectsin pages 1-6)
- Clinical response (2024 case): vertebral body reshaping after zoledronic acid; no new fractures during 3 years; increased femoral neck BMD after sequential zoledronic acid→teriparatide→denosumab in CRTAP case. (JCEM 2024; https://doi.org/10.1210/clinem/dgae025) (zhou2024geneticanalysisphenotypic pages 4-5)

## Gene/Protein Annotations with Ontologies
- CRTAP (HGNC:2387): collagen prolyl‑3‑hydroxylation complex subunit; GO:0019794, GO:0005783; disease: OI type VII. (marini2010nullmutationsin pages 4-5, barnes2006deficiencyofcartilageassociated pages 1-2)
- LEPRE1/P3H1 (HGNC:18684): prolyl 3‑hydroxylase; GO:0019794, GO:0005783. (marini2010nullmutationsin pages 4-5)
- PPIB (HGNC:9250): peptidyl‑prolyl cis‑trans isomerase; GO:0003755, GO:0005783. (marini2010nullmutationsin pages 4-5)
- COL1A1 (HGNC:2197): structural ECM protein; GO:0030199, GO:0005583. (valli2012deficiencyofcrtap pages 1-2)

## Phenotype Associations (HPO)
- HP:0002757 Recurrent fractures; HP:0000938 Osteopenia; HP:0008915 Rhizomelia; HP:0004322 Short stature; HP:0100660 Metaphyseal widening/“popcorn” epiphyses. (zhou2024geneticanalysisphenotypic pages 1-1, marini2010nullmutationsin pages 4-5)

## Cell Type Involvement (CL) and Anatomical Locations (UBERON)
- CL:0000062 Osteoblast; CL:0000138 Chondrocyte; CL:0002553 Lung fibroblast. (zhou2024geneticanalysisphenotypic pages 1-1, marini2010nullmutationsin pages 4-5, dimori2020respiratorydefectsin pages 1-6)
- UBERON:0001474 Bone; UBERON:0002048 Lung; UBERON:0002429 Growth plate cartilage. (dimori2020respiratorydefectsin pages 1-6, marini2010nullmutationsin pages 4-5)

## Chemical Entities (CHEBI)
- 4‑Phenylbutyrate (CHEBI:46195): ER chemical chaperone shown to reduce over‑modification/ER stress in models of collagen 3‑hydroxylation complex impairment. (zhou2024geneticanalysisphenotypic pages 10-11)
- Zoledronic acid (CHEBI:46550) and Denosumab (CHEBI:68481): antiresorptives with reported structural/BMD benefits in a CRTAP case. (zhou2024geneticanalysisphenotypic pages 4-5)

## Evidence Items (PMIDs/DOIs/URLs)
- Zhou et al., 2024, J Clin Endocrinol Metab, “Genetic Analysis, Phenotypic Spectrum and Functional Study of Rare OI Caused by CRTAP Variants.” DOI: 10.1210/clinem/dgae025; URL: https://doi.org/10.1210/clinem/dgae025 (zhou2024geneticanalysisphenotypic pages 1-1, zhou2024geneticanalysisphenotypic pages 9-10, zhou2024geneticanalysisphenotypic pages 9-9, zhou2024geneticanalysisphenotypic pages 4-5, zhou2024geneticanalysisphenotypic pages 10-11)
- Jovanovic & Marini, 2024, Calcified Tissue Int, “Update on the Genetics of OI.” DOI: 10.1007/s00223-024-01266-5; URL: https://doi.org/10.1007/s00223-024-01266-5 (jovanovic2024updateonthe pages 8-9)
- Barnes et al., 2006, N Engl J Med, “Deficiency of cartilage‑associated protein in recessive lethal OI.” DOI: 10.1056/NEJMoa063804; URL: https://doi.org/10.1056/NEJMoa063804 (barnes2006deficiencyofcartilageassociated pages 1-2)
- Marini et al., 2010, Cell Tissue Res, “Null mutations in LEPRE1 and CRTAP cause severe recessive OI.” DOI: 10.1007/s00441-009-0872-0; URL: https://doi.org/10.1007/s00441-009-0872-0 (marini2010nullmutationsin pages 4-5, marini2010nullmutationsin pages 2-4)
- Valli et al., 2012, Clin Genet, “Deficiency of CRTAP … reduces collagen deposition into matrix.” DOI: 10.1111/j.1399-0004.2011.01794.x; URL: https://doi.org/10.1111/j.1399-0004.2011.01794.x (valli2012deficiencyofcrtap pages 1-2)
- Dimori et al., 2020, Am J Physiol Lung Cell Mol Physiol, “Respiratory defects in CrtapKO.” DOI: 10.1152/ajplung.00313.2019; URL: https://doi.org/10.1152/ajplung.00313.2019 (dimori2020respiratorydefectsin pages 1-6)

## Current Applications and Real‑World Implementations
- Diagnostics: Genetic testing targeting COL1A1/2 and known recessive OI genes including CRTAP is recommended in modern practice; dyadic nosology aids classification (ISDS 2024). (jovanovic2024updateonthe pages 8-9)
- Pharmacologic management: Bisphosphonates (e.g., zoledronic acid) can improve vertebral morphology and reduce fractures; sequential antiresorptive/anabolic regimens (including teriparatide and denosumab) may increase BMD in individual CRTAP cases. Larger OI cohorts underlie these practices; CRTAP‑specific data remain limited to case level. (zhou2024geneticanalysisphenotypic pages 4-5)
- Emerging therapeutics: Anti‑TGF‑β and sclerostin‑neutralizing antibodies show preclinical efficacy in Crtap−/− mice; chemical chaperones (4‑phenylbutyrate) alleviate ER stress/over‑modification in models. As of the sources reviewed, no CRTAP‑targeted gene therapy trials were identified in 2023–2024. (zhou2024geneticanalysisphenotypic pages 10-11, dimori2020respiratorydefectsin pages 1-6)

## Limitations and Gaps
- Human, CRTAP‑specific therapeutic evidence is limited to case reports/series with surrogate endpoints (BMD, vertebral shape). Controlled trials in OI often mix genotypes, limiting CRTAP‑specific inference. Preclinical anti‑TGF‑β and sclerostin antibody data are promising but not yet translated to CRTAP‑specific clinical trials. (zhou2024geneticanalysisphenotypic pages 4-5, dimori2020respiratorydefectsin pages 1-6)

## Conclusion
CRTAP‑related OI type VII is a prototypical recessive collagen‑processing disorder. The central pathogenic axis is loss of α1(I) Pro986 3‑hydroxylation and impaired procollagen folding in the ER, culminating in ECM failure and aberrant matrix–cell signaling (notably TGF‑β). Human bone evidence from 2024 links CRTAP loss directly to reduced osteoblast numbers/osteoid and to absent active bone formation; murine and cellular models extend the pathology to growth plate cartilage and lung. Current management follows OI standards with antiresorptives; targeted pathways (anti‑TGF‑β, sclerostin inhibition, chemical chaperones) are supported preclinically but require CRTAP‑focused clinical evaluation. (zhou2024geneticanalysisphenotypic pages 1-1, marini2010nullmutationsin pages 4-5, valli2012deficiencyofcrtap pages 1-2, barnes2006deficiencyofcartilageassociated pages 1-2, dimori2020respiratorydefectsin pages 1-6, jovanovic2024updateonthe pages 8-9)


References

1. (jovanovic2024updateonthe pages 8-9): Milena Jovanovic and Joan C. Marini. Update on the genetics of osteogenesis imperfecta. Calcified Tissue International, 115:891-914, Aug 2024. URL: https://doi.org/10.1007/s00223-024-01266-5, doi:10.1007/s00223-024-01266-5. This article has 48 citations and is from a peer-reviewed journal.

2. (zhou2024geneticanalysisphenotypic pages 1-1): Bingna Zhou, Peng Gao, Jing Hu, Xiaoyun Lin, Lei Sun, Qian Zhang, Yan Jiang, Ou Wang, Weibo Xia, Xiaoping Xing, and Mei Li. Genetic analysis, phenotypic spectrum and functional study of rare osteogenesis imperfecta caused by crtap variants. The Journal of Clinical Endocrinology and Metabolism, 109:1803-1813, Jan 2024. URL: https://doi.org/10.1210/clinem/dgae025, doi:10.1210/clinem/dgae025. This article has 5 citations.

3. (marini2010nullmutationsin pages 4-5): Joan C. Marini, Wayne A. Cabral, and Aileen M. Barnes. Null mutations in lepre1 and crtap cause severe recessive osteogenesis imperfecta. Cell and Tissue Research, 339:59-70, Oct 2010. URL: https://doi.org/10.1007/s00441-009-0872-0, doi:10.1007/s00441-009-0872-0. This article has 151 citations and is from a peer-reviewed journal.

4. (marini2010nullmutationsin pages 2-4): Joan C. Marini, Wayne A. Cabral, and Aileen M. Barnes. Null mutations in lepre1 and crtap cause severe recessive osteogenesis imperfecta. Cell and Tissue Research, 339:59-70, Oct 2010. URL: https://doi.org/10.1007/s00441-009-0872-0, doi:10.1007/s00441-009-0872-0. This article has 151 citations and is from a peer-reviewed journal.

5. (valli2012deficiencyofcrtap pages 1-2): Maurizia Valli, Aileen M Barnes, A. Gallanti, W. A. Cabral, Simona Viglio, MaryAnn Weis, E. Makareeva, D. Eyre, Sergey Leikin, Franco Antoniazzi, Joan C. Marini, and Monica Mottes. Deficiency of crtap in non‐lethal recessive osteogenesis imperfecta reduces collagen deposition into matrix. Clinical Genetics, 82:453-459, Nov 2012. URL: https://doi.org/10.1111/j.1399-0004.2011.01794.x, doi:10.1111/j.1399-0004.2011.01794.x. This article has 45 citations and is from a peer-reviewed journal.

6. (barnes2006deficiencyofcartilageassociated pages 1-2): Aileen M. Barnes, Weizhong Chang, Roy Morello, Wayne A. Cabral, MaryAnn Weis, David R. Eyre, Sergey Leikin, Elena Makareeva, Natalia Kuznetsova, Thomas E. Uveges, Aarthi Ashok, Armando W. Flor, John J. Mulvihill, Patrick L. Wilson, Usha T. Sundaram, Brendan Lee, and Joan C. Marini. Deficiency of cartilage-associated protein in recessive lethal osteogenesis imperfecta. The New England journal of medicine, 355 26:2757-64, Dec 2006. URL: https://doi.org/10.1056/nejmoa063804, doi:10.1056/nejmoa063804. This article has 436 citations and is from a highest quality peer-reviewed journal.

7. (dimori2020respiratorydefectsin pages 1-6): Milena Dimori, Melissa E. Heard-Lipsmeyer, Stephanie D. Byrum, Samuel G. Mackintosh, Richard C. Kurten, John L. Carroll, and Roy Morello. Respiratory defects in the <i>crtap</i>ko mouse model of osteogenesis imperfecta. American Journal of Physiology-Lung Cellular and Molecular Physiology, 318:L592-L605, Apr 2020. URL: https://doi.org/10.1152/ajplung.00313.2019, doi:10.1152/ajplung.00313.2019. This article has 26 citations.

8. (zhou2024geneticanalysisphenotypic pages 9-9): Bingna Zhou, Peng Gao, Jing Hu, Xiaoyun Lin, Lei Sun, Qian Zhang, Yan Jiang, Ou Wang, Weibo Xia, Xiaoping Xing, and Mei Li. Genetic analysis, phenotypic spectrum and functional study of rare osteogenesis imperfecta caused by crtap variants. The Journal of Clinical Endocrinology and Metabolism, 109:1803-1813, Jan 2024. URL: https://doi.org/10.1210/clinem/dgae025, doi:10.1210/clinem/dgae025. This article has 5 citations.

9. (zhou2024geneticanalysisphenotypic pages 10-11): Bingna Zhou, Peng Gao, Jing Hu, Xiaoyun Lin, Lei Sun, Qian Zhang, Yan Jiang, Ou Wang, Weibo Xia, Xiaoping Xing, and Mei Li. Genetic analysis, phenotypic spectrum and functional study of rare osteogenesis imperfecta caused by crtap variants. The Journal of Clinical Endocrinology and Metabolism, 109:1803-1813, Jan 2024. URL: https://doi.org/10.1210/clinem/dgae025, doi:10.1210/clinem/dgae025. This article has 5 citations.

10. (zhou2024geneticanalysisphenotypic pages 4-5): Bingna Zhou, Peng Gao, Jing Hu, Xiaoyun Lin, Lei Sun, Qian Zhang, Yan Jiang, Ou Wang, Weibo Xia, Xiaoping Xing, and Mei Li. Genetic analysis, phenotypic spectrum and functional study of rare osteogenesis imperfecta caused by crtap variants. The Journal of Clinical Endocrinology and Metabolism, 109:1803-1813, Jan 2024. URL: https://doi.org/10.1210/clinem/dgae025, doi:10.1210/clinem/dgae025. This article has 5 citations.

11. (zhou2024geneticanalysisphenotypic pages 9-10): Bingna Zhou, Peng Gao, Jing Hu, Xiaoyun Lin, Lei Sun, Qian Zhang, Yan Jiang, Ou Wang, Weibo Xia, Xiaoping Xing, and Mei Li. Genetic analysis, phenotypic spectrum and functional study of rare osteogenesis imperfecta caused by crtap variants. The Journal of Clinical Endocrinology and Metabolism, 109:1803-1813, Jan 2024. URL: https://doi.org/10.1210/clinem/dgae025, doi:10.1210/clinem/dgae025. This article has 5 citations.