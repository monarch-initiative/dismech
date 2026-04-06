---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-02-10T08:03:42.121263'
end_time: '2026-02-10T08:11:31.316951'
duration_seconds: 469.2
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hypophosphatasia
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 31
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Hypophosphatasia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Hypophosphatasia**.
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
- **Disease Name:** Hypophosphatasia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Hypophosphatasia**.
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
- Disease Name: Hypophosphatasia (HPP)
- MONDO ID: MONDO:0007522
- Category: Mendelian

Pathophysiology description
Hypophosphatasia is a systemic metabolic bone and dental disease caused by loss-of-function variants in ALPL encoding tissue-nonspecific alkaline phosphatase (TNSALP/TNAP). TNAP is a cell-surface, GPI-anchored ectoenzyme highly expressed on osteoblasts and other cells; it hydrolyzes three key physiological substrates—inorganic pyrophosphate (PPi), pyridoxal 5′-phosphate (PLP), and phosphoethanolamine (PEA). Deficiency of TNAP activity leads to PPi accumulation and a reduced local Pi:PPi ratio, which directly inhibits hydroxyapatite nucleation and extracellular matrix mineralization in bone and teeth, producing rickets in children and osteomalacia and pseudofractures in older patients. Diagnostic biochemical features include persistently low age/sex-adjusted serum ALP with elevated ALP substrates (PPi, serum PLP, and urine PEA). Impaired dephosphorylation of PLP also contributes mechanistically to vitamin B6–responsive neonatal seizures; chronically elevated PPi promotes calcium pyrophosphate (CPP) crystal deposition causing chondrocalcinosis/pseudogout. Mineral imbalance (hypercalcemia, hypercalciuria) predisposes to nephrocalcinosis. Craniosynostosis reflects disordered skull bone mineralization. As one expert consensus summarizes, HPP “results from LOF variants in ALPL causing deficient tissue-nonspecific alkaline phosphatase… [whose] substrates include PPi, PLP, and PEA,” and the altered phosphate:PPi balance “inhibits bone and tooth mineralization.” Updates also emphasize technical pitfalls (e.g., EDTA/oxalate tubes artifactually lowering ALP) and the value of integrated clinical–biochemical–radiographic–genetic diagnosis to reduce delays (Osteoporosis International, Nov 2024; https://doi.org/10.1007/s00198-023-06844-1). (khan2024hypophosphatasiadiagnosiscurrent pages 1-2)

Core mechanisms: molecular and cellular
- Enzyme deficiency: TNAP deficiency from ALPL LOF variants causes PPi accumulation in the extracellular milieu; elevated PPi inhibits hydroxyapatite crystal formation at matrix vesicles and within collagenous matrix. Clinically: rickets/osteomalacia, deformities, pseudofractures, delayed fracture healing. (Calcified Tissue International, Mar 2025; https://doi.org/10.1007/s00223-025-01356-y). (seefried2025diagnosisandtreatment pages 1-2)
- Substrate biology: PPi is the proximate inhibitor of mineralization; PLP is a TNAP substrate whose CNS handling explains vitamin B6–responsive seizures; PEA serves as a supportive diagnostic marker though its mechanistic role is less defined. A 2025 medical management review reiterates that the “accumulation of TNSALP substrates PPi, PLP, and PEA” underlies disease, and that elevated PPi “inhibits hydroxyapatite formation.” (Current Osteoporosis Reports, Mar 2025; https://doi.org/10.1007/s11914-025-00906-5). (dahir2025medicalmanagementof pages 1-2)
- Dental mineralization: TNAP maintains the local Pi:PPi ratio crucial for cementogenesis. Cementum hypoplasia leads to pathognomonic premature exfoliation of fully rooted primary teeth; the dentin and alveolar bone are variably affected. “Premature tooth loss of fully rooted teeth is pathognomonic for HPP,” and effects of systemically delivered ERT on dental tissues “remain poorly defined,” motivating gene-therapy exploration (JBMR Plus, Jan 2025; https://doi.org/10.1093/jbmrpl/ziae180). (santos2025dentalmanifestationsof pages 1-3, santos2025dentalmanifestationsof pages 3-4)
- CPPD link: sustained PPi excess favors calcium pyrophosphate dihydrate crystallization, clinically observed as chondrocalcinosis/pseudogout in some patients. (Osteoporosis International, Nov 2024; https://doi.org/10.1007/s00198-023-06844-1; Calcified Tissue International, Mar 2025; https://doi.org/10.1007/s00223-025-01356-y). (khan2024hypophosphatasiadiagnosiscurrent pages 1-2, seefried2025diagnosisandtreatment pages 1-2)

2023–2024 developments and latest research
- Updated diagnosis criteria: An International Working Group (IWG) proposed major/minor criteria integrating clinical features, persistently low ALP (age/sex adjusted), elevated ALP substrates (PPi/PLP/PEA), characteristic imaging, and ALPL genetics, aiming to reduce a median ~5.7-year diagnostic delay noted previously. Practical lab guidance highlights avoiding EDTA/oxalate tubes that artifactually lower ALP. (Osteoporosis International, Nov 2024; https://doi.org/10.1007/s00198-023-06844-1). (khan2024hypophosphatasiadiagnosiscurrent pages 2-4, khan2024hypophosphatasiadiagnosiscurrent pages 1-2)
- Genetics beyond coding regions: In a 2024 whole-genome sequencing (WGS) study of 16 adults with clinical HPP phenotypes and low ALP but negative prior ALPL testing, WGS “did not identify any novel disease-causing ALPL variants,” though variants in other genes (e.g., COL1A1, NLRP12, SCN9A, P3H1, SGCE, VDR) were found in four patients, underscoring residual diagnostic gaps and the potential for alternative or modifying mechanisms (Molecular Biology Reports, Sep 2024; https://doi.org/10.1007/s11033-024-09906-7). (seefried2024wholegenomesequencing pages 1-2)
- Therapy and outcomes: Real-world and registry syntheses report that asfotase alfa improves survival and rickets in severely affected children and improves physical function, pain, and quality-of-life (QoL) across age-of-onset groups; expert reviews also note clinical testing of a long-acting TNAP (efzimfotase alfa/ALXN1850) in trials aiming to reduce treatment burden (Current Osteoporosis Reports, Mar 2025; https://doi.org/10.1007/s11914-025-00906-5). (dahir2025medicalmanagementof pages 1-2) Additional clinical perspective reviews emphasize non-skeletal burdens (pain, fatigue, neuropsychiatric and GI symptoms) and the need to address them in care pathways (Calcified Tissue International, Mar 2025; https://doi.org/10.1007/s00223-025-01356-y). (seefried2025diagnosisandtreatment pages 1-2)
- Dental/craniofacial insights: Translational advances from animal models and clinical series clarify cementum dependence on TNAP and reinforce that odonto-HPP can present without overt skeletal disease; the literature highlights knowledge gaps regarding ERT penetration into dental tissues and motivates gene-therapy approaches under preclinical evaluation (JBMR Plus, Jan 2025; https://doi.org/10.1093/jbmrpl/ziae180). (santos2025dentalmanifestationsof pages 1-3, santos2025dentalmanifestationsof pages 3-4)

Current applications and real-world implementation
- Enzyme replacement therapy (ERT): Asfotase alfa is standard-of-care for severe pediatric-onset HPP and is increasingly used in adults with significant disease burden. Syntheses of observational cohorts and registry data indicate sustained improvements in radiographic rickets, growth and respiratory survival in infants, and in adults, reductions in pain and improvements in function and QoL across age-of-onset categories. The same review notes that initiation criteria are being formalized and that a long-acting enzyme (efzimfotase alfa/ALXN1850) is in clinical testing to reduce dosing frequency (Current Osteoporosis Reports, Mar 2025; https://doi.org/10.1007/s11914-025-00906-5). (dahir2025medicalmanagementof pages 1-2)
- Diagnostic standardization: The 2024 IWG criteria provide a harmonized diagnostic framework adopted by expert centers to shorten time-to-diagnosis and to improve enrollment fidelity for trials and registries (Osteoporosis International, Nov 2024; https://doi.org/10.1007/s00198-023-06844-1). (khan2024hypophosphatasiadiagnosiscurrent pages 1-2)

Expert opinions and authoritative analysis
- The International Working Group’s consensus underscores integrating clinical phenotype with biochemistry and genetics, acknowledging that “gene sequencing is not positive in all clinically diagnosed patients,” and urging measured interpretation of VUS and negative tests in the setting of classic phenotypes (Osteoporosis International, Nov 2024; https://doi.org/10.1007/s00198-023-06844-1). (khan2024hypophosphatasiadiagnosiscurrent pages 1-2)
- Seefried et al. highlight expanding adult HPP recognition with prominent pain/fatigue and emphasize the need to clarify mechanisms and improve substitution strategies beyond current ERT (Calcified Tissue International, Mar 2025; https://doi.org/10.1007/s00223-025-01356-y). (seefried2025diagnosisandtreatment pages 1-2)
- Dahir and Dunbar synthesize registry evidence supporting clinical benefits of ERT across ages and note ongoing development of long-acting TNAP constructs (efzimfotase/ALXN1850) to address treatment burden (Current Osteoporosis Reports, Mar 2025; https://doi.org/10.1007/s11914-025-00906-5). (dahir2025medicalmanagementof pages 1-2)

Relevant statistics and data (selected, with quotes where available)
- Diagnostic challenge and delay: The IWG paper documents substantial diagnostic delays and proposes criteria to “assist in establishing a clinical diagnosis of HPP in adults and children,” with systematic review methodology and GRADE-informed consensus (Osteoporosis International, Nov 2024; https://doi.org/10.1007/s00198-023-06844-1). (khan2024hypophosphatasiadiagnosiscurrent pages 1-2)
- WGS-negative cohort: In 16 clinically diagnosed adults with low ALP but negative prior testing, “WGS did not identify any novel disease-causing ALPL variants,” identifying variants in non-ALPL genes in 4/16, illustrating a residual genetic diagnostic gap with standard techniques (Molecular Biology Reports, Sep 2024; https://doi.org/10.1007/s11033-024-09906-7). (seefried2024wholegenomesequencing pages 1-2)
- ERT outcomes: Summaries from the Global HPP Registry and other cohorts show ERT improves physical function and QoL in adults regardless of onset age, and improves survival and rickets in severely affected children, as consolidated in a 2025 review (Current Osteoporosis Reports, Mar 2025; https://doi.org/10.1007/s11914-025-00906-5). (dahir2025medicalmanagementof pages 1-2) Pathophysiology and clinical spectrum including CPPD, craniosynostosis, and seizures are reiterated in expert reviews (Calcified Tissue International, Mar 2025; https://doi.org/10.1007/s00223-025-01356-y; JBMR Plus, Jan 2025; https://doi.org/10.1093/jbmrpl/ziae180). (seefried2025diagnosisandtreatment pages 1-2, santos2025dentalmanifestationsof pages 1-3)

Key concepts and definitions
- Tissue-nonspecific alkaline phosphatase (TNSALP/TNAP): A GPI-anchored ectoenzyme at the plasma membrane, highly expressed on osteoblasts; dephosphorylates PPi, PLP, PEA, regulating mineralization via the Pi:PPi ratio. (Osteoporosis International, Nov 2024; https://doi.org/10.1007/s00198-023-06844-1; Calcified Tissue International, Mar 2025; https://doi.org/10.1007/s00223-025-01356-y). (khan2024hypophosphatasiadiagnosiscurrent pages 1-2, seefried2025diagnosisandtreatment pages 1-2)
- Inorganic pyrophosphate (PPi): Potent mineralization inhibitor; excess PPi from TNAP deficiency suppresses hydroxyapatite crystal growth. (Current Osteoporosis Reports, Mar 2025; https://doi.org/10.1007/s11914-025-00906-5). (dahir2025medicalmanagementof pages 1-2)
- Pyridoxal 5′-phosphate (PLP): Active vitamin B6; TNAP-mediated dephosphorylation is important for neuronal availability; impaired handling leads to vitamin B6–responsive neonatal seizures. (Osteoporosis International, Nov 2024; https://doi.org/10.1007/s00198-023-06844-1). (khan2024hypophosphatasiadiagnosiscurrent pages 1-2)
- Phosphoethanolamine (PEA): TNAP substrate measurable in urine; supportive biomarker of HPP. (Calcified Tissue International, Mar 2025; https://doi.org/10.1007/s00223-025-01356-y). (seefried2025diagnosisandtreatment pages 1-2)

Key molecular players and affected systems
- Genes/Proteins: ALPL/TNSALP (HGNC:436). (khan2024hypophosphatasiadiagnosiscurrent pages 1-2)
- Chemical entities: PPi, PLP, PEA, orthophosphate (Pi), hydroxyapatite, calcium pyrophosphate crystals. (khan2024hypophosphatasiadiagnosiscurrent pages 1-2, seefried2025diagnosisandtreatment pages 1-2, dahir2025medicalmanagementof pages 1-2)
- Cell types: Osteoblasts, chondrocytes, osteocytes. (khan2024hypophosphatasiadiagnosiscurrent pages 1-2, seefried2025diagnosisandtreatment pages 1-2)
- Anatomical sites: Bone (including growth plates), dentoalveolar complex (cementum, dentin, alveolar bone), joints, kidney, brain, cranial sutures. (khan2024hypophosphatasiadiagnosiscurrent pages 1-2, seefried2025diagnosisandtreatment pages 1-2, santos2025dentalmanifestationsof pages 1-3)

Biological processes (GO) and cellular components
- Disrupted processes: Bone mineralization (GO:0030282); extracellular matrix mineralization (GO:0030198); ossification (GO:0001503); phosphate-containing compound metabolic process (GO:0006796); pyridoxal phosphate metabolic process (GO:0042823). (khan2024hypophosphatasiadiagnosiscurrent pages 1-2, seefried2025diagnosisandtreatment pages 1-2, santos2025dentalmanifestationsof pages 1-3)
- Cellular components: Plasma membrane (GO:0005886; TNAP is GPI-anchored); extracellular region (GO:0005576; PPi accumulates and inhibits mineral deposition); matrix vesicle (GO:0070062; initial mineral nucleation site dependent on local TNAP activity). (khan2024hypophosphatasiadiagnosiscurrent pages 1-2, seefried2025diagnosisandtreatment pages 1-2, santos2025dentalmanifestationsof pages 1-3)

Cell type involvement (CL) and anatomical locations (UBERON); chemical entities (CHEBI)
- See structured ontology mapping below.

| Category | Entity (name) | Identifier | Role / Relevance | Supporting Sources |
|---|---|---|---|---|
| Gene / Protein | ALPL / TNSALP | HGNC:436 | Causal gene encoding tissue-nonspecific alkaline phosphatase; loss-of-function causes HPP | (khan2024hypophosphatasiadiagnosiscurrent pages 1-2, seefried2025diagnosisandtreatment pages 1-2) |
| Metabolite | Inorganic pyrophosphate | CHEBI:18361 | Pathogenic substrate that accumulates when TNAP is deficient; inhibits hydroxyapatite formation and mineralization | (khan2024hypophosphatasiadiagnosiscurrent pages 1-2, seefried2025diagnosisandtreatment pages 1-2, dahir2025medicalmanagementof pages 1-2) |
| Metabolite | Pyridoxal 5'-phosphate (PLP) | CHEBI:18405 | TNAP substrate; impaired dephosphorylation linked to vitamin B6–responsive seizures in infants | (khan2024hypophosphatasiadiagnosiscurrent pages 1-2, seefried2025diagnosisandtreatment pages 1-2, dahir2025medicalmanagementof pages 1-2) |
| Metabolite | Phosphoethanolamine (PEA) | CHEBI:16311 | Urinary biomarker elevated in HPP; diagnostic substrate of TNAP | (seefried2025diagnosisandtreatment pages 1-2, dahir2025medicalmanagementof pages 1-2) |
| Metabolite | Orthophosphate (Pi) | CHEBI:18367 | Product of PPi hydrolysis by TNAP; Pi:PPi balance is critical for mineralization | (khan2024hypophosphatasiadiagnosiscurrent pages 1-2, seefried2025diagnosisandtreatment pages 1-2) |
| Metabolite | Hydroxyapatite | CHEBI:52255 | Mineral phase of bone/teeth formation inhibited by excess PPi | (khan2024hypophosphatasiadiagnosiscurrent pages 1-2, santos2025dentalmanifestationsof pages 1-3) |
| Metabolite | Calcium pyrophosphate | CHEBI:3311 | Crystal species promoted by elevated PPi; linked to chondrocalcinosis/CPPD in HPP | (khan2024hypophosphatasiadiagnosiscurrent pages 1-2, seefried2025diagnosisandtreatment pages 1-2) |
| Cell type | Osteoblast | CL:0000062 | Primary bone-forming cell expressing membrane-anchored TNAP; defective mineralization when TNAP low | (khan2024hypophosphatasiadiagnosiscurrent pages 1-2, seefried2025diagnosisandtreatment pages 1-2) |
| Cell type | Chondrocyte | CL:0000138 | Growth-plate and cartilage cells affected in rickets-like changes due to altered Pi:PPi | (khan2024hypophosphatasiadiagnosiscurrent pages 1-2, lipinski2026hypophosphatasiainchildren pages 1-2) |
| Cell type | Osteocyte | CL:0000127 | Mature bone cell within mineralized matrix; contributes to bone homeostasis affected by hypomineralization | (khan2024hypophosphatasiadiagnosiscurrent pages 1-2, lipinski2026hypophosphatasiainchildren pages 1-2) |
| Anatomical | Bone | UBERON:0001474 | Primary organ affected: defective extracellular matrix mineralization → rickets/osteomalacia, fractures | (khan2024hypophosphatasiadiagnosiscurrent pages 1-2, seefried2025diagnosisandtreatment pages 1-2) |
| Anatomical | Growth plate | UBERON:0003949 | Site of endochondral ossification; rickets-like metaphyseal changes occur in pediatric HPP | (khan2024hypophosphatasiadiagnosiscurrent pages 1-2, lipinski2026hypophosphatasiainchildren pages 1-2) |
| Anatomical | Cementum | UBERON:0008768 | Tooth-supporting mineralized tissue; hypoplasia → premature loss of deciduous teeth (pathognomonic) | (santos2025dentalmanifestationsof pages 1-3, santos2025dentalmanifestationsof pages 3-4) |
| Anatomical | Dentin | UBERON:0001754 | Mineralized tooth tissue affected in odonto-HPP phenotypes | (santos2025dentalmanifestationsof pages 1-3) |
| Anatomical | Alveolar bone | UBERON:0008060 | Tooth socket bone affected leading to early tooth loss and periodontal issues | (santos2025dentalmanifestationsof pages 1-3) |
| Anatomical | Kidney | UBERON:0002113 | Site of nephrocalcinosis and disturbances in calcium/phosphate handling in some HPP patients | (khan2024hypophosphatasiadiagnosiscurrent pages 1-2, seefried2025diagnosisandtreatment pages 1-2) |
| Anatomical | Brain | UBERON:0000955 | Indirectly affected via PLP metabolism; PLP deficiency underlies pyridoxine‑responsive seizures | (khan2024hypophosphatasiadiagnosiscurrent pages 1-2, dahir2025medicalmanagementof pages 1-2) |
| Anatomical | Joint | UBERON:0000982 | CPP crystal deposition (chondrocalcinosis) and inflammatory arthropathy linked to PPi accumulation | (khan2024hypophosphatasiadiagnosiscurrent pages 1-2, seefried2025diagnosisandtreatment pages 1-2) |
| Anatomical | Cranial suture | UBERON:0003687 | Craniosynostosis observed in some pediatric HPP cases related to abnormal skull bone mineralization | (seefried2025diagnosisandtreatment pages 1-2, santos2025dentalmanifestationsof pages 1-3) |
| GO Process | Bone mineralization | GO:0030282 | Biological process directly impaired by TNAP deficiency and PPi accumulation | (khan2024hypophosphatasiadiagnosiscurrent pages 1-2, seefried2025diagnosisandtreatment pages 1-2) |
| GO Process | Extracellular matrix mineralization | GO:0030198 | General mineralization pathway disrupted in bone and dentoalveolar tissues | (khan2024hypophosphatasiadiagnosiscurrent pages 1-2, santos2025dentalmanifestationsof pages 1-3) |
| GO Process | Ossification | GO:0001503 | Endochondral and intramembranous bone formation processes affected, producing rickets/cranial anomalies | (khan2024hypophosphatasiadiagnosiscurrent pages 1-2, lipinski2026hypophosphatasiainchildren pages 1-2) |
| GO Process | Pyridoxal phosphate metabolic process | GO:0042823 | PLP metabolism impacted by TNAP activity → neurological manifestations | (khan2024hypophosphatasiadiagnosiscurrent pages 1-2, dahir2025medicalmanagementof pages 1-2) |
| GO Process | Phosphate-containing compound metabolic process | GO:0006796 | Broad category encompassing PPi/Pi balance controlled by TNAP | (khan2024hypophosphatasiadiagnosiscurrent pages 1-2, seefried2025diagnosisandtreatment pages 1-2) |
| Cellular Component | Plasma membrane | GO:0005886 | TNAP is a GPI‑anchored/membrane-associated enzyme on osteoblasts and other cells | (khan2024hypophosphatasiadiagnosiscurrent pages 1-2, seefried2025diagnosisandtreatment pages 1-2) |
| Cellular Component | Extracellular region | GO:0005576 | Matrix and extracellular milieu where PPi accumulates and inhibits mineral deposition | (khan2024hypophosphatasiadiagnosiscurrent pages 1-2, seefried2025diagnosisandtreatment pages 1-2) |
| Cellular Component | Matrix vesicle | GO:0070062 | Sites of initial mineral nucleation in bone; TNAP activity in/near vesicles is critical for hydroxyapatite formation | (khan2024hypophosphatasiadiagnosiscurrent pages 1-2, lipinski2026hypophosphatasiainchildren pages 1-2) |


*Table: Concise mapping of key HPP molecular entities, cell/tissue sites, GO processes and ontology identifiers with brief roles and supporting source IDs; useful for knowledge‑base annotation and downstream GO/HGNC/UBERON/CL/CHEBI mapping.*

Disease progression
- Initiating trigger: ALPL loss-of-function reduces cell-surface TNAP on osteoblasts/chondrocytes. (khan2024hypophosphatasiadiagnosiscurrent pages 1-2)
- Molecular cascade: PPi accumulates; Pi:PPi balance shifts; hydroxyapatite nucleation in matrix vesicles is inhibited; extracellular matrix fails to mineralize. (seefried2025diagnosisandtreatment pages 1-2)
- Tissue-level effects: Pediatric growth plates develop rickets-like metaphyseal changes; adults develop osteomalacia with fractures/pseudofractures and delayed healing. (khan2024hypophosphatasiadiagnosiscurrent pages 1-2, seefried2025diagnosisandtreatment pages 1-2)
- Dentition: Cementum hypoplasia leads to early loss of fully rooted primary teeth; dentin/alveolar bone involvement varies (odonto-HPP may be dental-restricted). (santos2025dentalmanifestationsof pages 1-3)
- Systemic sequelae: PLP handling deficits produce neonatal vitamin B6–responsive seizures; mineral dysregulation predisposes to hypercalcemia/hypercalciuria and nephrocalcinosis; chronic PPi excess fosters CPPD/chondrocalcinosis. (khan2024hypophosphatasiadiagnosiscurrent pages 1-2, seefried2025diagnosisandtreatment pages 1-2)

Phenotypic manifestations (with HP terms)
- Rickets (HP:0000938), osteomalacia (HP:0000938), fractures/pseudofractures (HP:0002659), delayed fracture healing (HP:0000940). Mechanism: PPi-mediated inhibition of mineralization. (khan2024hypophosphatasiadiagnosiscurrent pages 1-2, seefried2025diagnosisandtreatment pages 1-2)
- Craniosynostosis (HP:0001363). Mechanism: disordered intramembranous ossification of cranial sutures. (seefried2025diagnosisandtreatment pages 1-2)
- Premature exfoliation of primary teeth (HP:0006354), enlarged pulp chambers (HP:0006297), cementum hypoplasia. Mechanism: disrupted Pi:PPi at cementogenesis. (santos2025dentalmanifestationsof pages 1-3)
- Vitamin B6–responsive seizures (HP:0001250). Mechanism: impaired PLP dephosphorylation/availability. (khan2024hypophosphatasiadiagnosiscurrent pages 1-2)
- Hypercalcemia (HP:0003072), hypercalciuria (HP:0002150), nephrocalcinosis (HP:0000121). Mechanism: mineral imbalance in poorly mineralizing skeleton. (khan2024hypophosphatasiadiagnosiscurrent pages 1-2)
- Chondrocalcinosis/CPPD (HP:0100762). Mechanism: elevated PPi and CPP crystal formation. (khan2024hypophosphatasiadiagnosiscurrent pages 1-2, seefried2025diagnosisandtreatment pages 1-2)

Evidence items (primary/review sources with dates/URLs)
- Khan AA et al. Hypophosphatasia diagnosis: current state of the art and proposed diagnostic criteria for children and adults. Osteoporosis International. Published Nov 2024. URL: https://doi.org/10.1007/s00198-023-06844-1. (khan2024hypophosphatasiadiagnosiscurrent pages 1-2)
- Seefried L et al. Diagnosis and treatment of hypophosphatasia. Calcified Tissue International. Published Mar 2025. URL: https://doi.org/10.1007/s00223-025-01356-y. (seefried2025diagnosisandtreatment pages 1-2)
- Dahir KM, Dunbar NS. Medical management of hypophosphatasia: review of data on asfotase alfa. Current Osteoporosis Reports. Published Mar 2025. URL: https://doi.org/10.1007/s11914-025-00906-5. (dahir2025medicalmanagementof pages 1-2)
- Seefried L et al. Whole genome sequencing in adults with clinical hallmarks of hypophosphatasia negative for ALPL variants. Molecular Biology Reports. Published Sep 2024. URL: https://doi.org/10.1007/s11033-024-09906-7. (seefried2024wholegenomesequencing pages 1-2)
- dos Santos EJL et al. Dental manifestations of hypophosphatasia: translational and clinical advances. JBMR Plus. Published Jan 2025. URL: https://doi.org/10.1093/jbmrpl/ziae180. (santos2025dentalmanifestationsof pages 1-3, santos2025dentalmanifestationsof pages 3-4)

Direct supporting quotes
- “The diagnosis of HPP is made on the basis of integrating clinical features, laboratory profile, radiographic features of the condition, and DNA analysis identifying the presence of a pathogenic variant of the tissue nonspecific alkaline phosphatase gene (ALPL).” (Osteoporosis International, Nov 2024; https://doi.org/10.1007/s00198-023-06844-1). (khan2024hypophosphatasiadiagnosiscurrent pages 1-2)
- “HPP… [is] characterized by deficient activity of tissue-nonspecific alkaline phosphatase (TNAP) caused by variants in the ALPL gene… [with] elevated levels of ALP substrates, specifically inorganic pyrophosphate (PPi), pyridoxal 5′-phosphate (PLP) or urine phosphoethanolamine (PEA).” (Calcified Tissue International, Mar 2025; https://doi.org/10.1007/s00223-025-01356-y). (seefried2025diagnosisandtreatment pages 1-2)
- “Elevated PPi inhibits hydroxyapatite formation, causing skeletal and dental hypomineralization,” and “treatment for HPP relies on enzyme replacement asfotase alfa… long-term safety and efficacy… [with] a derivative, efzimfotase alfa, currently undergoes clinical testing.” (Current Osteoporosis Reports, Mar 2025; https://doi.org/10.1007/s11914-025-00906-5). (dahir2025medicalmanagementof pages 1-2)
- “Premature tooth loss of fully rooted teeth is pathognomonic for HPP… [and] effects of ERT on dental tissues remain poorly defined,” motivating exploration of gene therapy. (JBMR Plus, Jan 2025; https://doi.org/10.1093/jbmrpl/ziae180). (santos2025dentalmanifestationsof pages 1-3)

Gene/protein annotations with ontology terms
- ALPL (HGNC:436); Protein: tissue-nonspecific alkaline phosphatase (TNAP). Function/process: bone mineralization (GO:0030282); extracellular matrix mineralization (GO:0030198); phosphate-containing compound metabolic process (GO:0006796); pyridoxal phosphate metabolic process (GO:0042823). Cellular component: plasma membrane (GO:0005886), matrix vesicle (GO:0070062), extracellular region (GO:0005576). (khan2024hypophosphatasiadiagnosiscurrent pages 1-2, seefried2025diagnosisandtreatment pages 1-2, santos2025dentalmanifestationsof pages 1-3)

Phenotype associations (HP terms)
- HP:0000938 (Rickets/Osteomalacia), HP:0002659 (Pseudofractures), HP:0000940 (Delayed bone healing/Nonunion), HP:0001363 (Craniosynostosis), HP:0006354 (Premature loss of primary teeth), HP:0006297 (Enlarged pulp chambers), HP:0001250 (Seizures), HP:0003072 (Hypercalcemia), HP:0002150 (Hypercalciuria), HP:0000121 (Nephrocalcinosis), HP:0100762 (Chondrocalcinosis). Mechanistic links detailed above. (khan2024hypophosphatasiadiagnosiscurrent pages 1-2, seefried2025diagnosisandtreatment pages 1-2, santos2025dentalmanifestationsof pages 1-3)

Cell type involvement (CL terms)
- Osteoblast (CL:0000062), Chondrocyte (CL:0000138), Osteocyte (CL:0000127). (khan2024hypophosphatasiadiagnosiscurrent pages 1-2, seefried2025diagnosisandtreatment pages 1-2)

Anatomical locations (UBERON terms)
- Bone (UBERON:0001474), Growth plate (UBERON:0003949), Cementum (UBERON:0008768), Dentin (UBERON:0001754), Alveolar bone (UBERON:0008060), Joint (UBERON:0000982), Kidney (UBERON:0002113), Brain (UBERON:0000955), Cranial suture (UBERON:0003687). (khan2024hypophosphatasiadiagnosiscurrent pages 1-2, seefried2025diagnosisandtreatment pages 1-2, santos2025dentalmanifestationsof pages 1-3)

Chemical entities (CHEBI terms)
- Inorganic pyrophosphate (CHEBI:18361), Pyridoxal 5′-phosphate (CHEBI:18405), Phosphoethanolamine (CHEBI:16311), Orthophosphate (CHEBI:18367), Hydroxyapatite (CHEBI:52255), Calcium pyrophosphate (CHEBI:3311). (khan2024hypophosphatasiadiagnosiscurrent pages 1-2, seefried2025diagnosisandtreatment pages 1-2, dahir2025medicalmanagementof pages 1-2)

Open questions and future directions
- Genetics: Persistent fraction of clinically definite HPP remains ALPL-negative by standard sequencing and even WGS, suggesting undetected regulatory/structural variants or genetic modifiers; expanded assays and functional genomics are needed (Molecular Biology Reports, Sep 2024; https://doi.org/10.1007/s11033-024-09906-7). (seefried2024wholegenomesequencing pages 1-2)
- Therapies: While ERT has transformed outcomes, optimizing access, long-acting formulations (efzimfotase/ALXN1850), and approaches addressing dental tissues and adult non-skeletal symptom burden remain priorities; preclinical gene-therapy strategies are under investigation (Current Osteoporosis Reports, Mar 2025; https://doi.org/10.1007/s11914-025-00906-5; JBMR Plus, Jan 2025; https://doi.org/10.1093/jbmrpl/ziae180). (dahir2025medicalmanagementof pages 1-2, santos2025dentalmanifestationsof pages 1-3)

Overall synthesis
HPP pathophysiology centers on deficient TNAP activity and consequent PPi accumulation, which disrupts extracellular matrix mineralization across bone and dental tissues and secondarily perturbs PLP metabolism and systemic mineral homeostasis. The 2024 consensus criteria codify a modern diagnostic framework integrating biochemistry, imaging, and genetics, while 2024 WGS data underscore ongoing genetic diagnostic gaps. Real-world evidence consolidates ERT’s benefits in survival, mineralization, function, and QoL, with long-acting TNAP under clinical evaluation and gene-therapy approaches emerging to address remaining needs, including dental tissue targeting and adult symptom burden (Osteoporosis International, Nov 2024; Calcified Tissue International, Mar 2025; Current Osteoporosis Reports, Mar 2025; JBMR Plus, Jan 2025). (khan2024hypophosphatasiadiagnosiscurrent pages 1-2, seefried2025diagnosisandtreatment pages 1-2, dahir2025medicalmanagementof pages 1-2, santos2025dentalmanifestationsof pages 1-3)

References

1. (khan2024hypophosphatasiadiagnosiscurrent pages 1-2): Aliya A. Khan, Maria Luisa Brandi, Eric T. Rush, Dalal S. Ali, Hatim Al-Alwani, Khulod Almonaei, Farah Alsarraf, Severine Bacrot, Kathryn M. Dahir, Karel Dandurand, Chad Deal, Serge Livio Ferrari, Francesca Giusti, Gordon Guyatt, Erin Hatcher, Steven W. Ing, Muhammad Kassim Javaid, Sarah Khan, Roland Kocijan, Agnes Linglart, Iman M’Hiri, Francesca Marini, Mark E. Nunes, Cheryl Rockman-Greenberg, Christian Roux, Lothar Seefried, Jill H. Simmons, Susan R. Starling, Leanne M. Ward, Liang Yao, Romina Brignardello-Petersen, and E. Michael Lewiecki. Hypophosphatasia diagnosis: current state of the art and proposed diagnostic criteria for children and adults. Osteoporosis International, 35:431-438, Nov 2024. URL: https://doi.org/10.1007/s00198-023-06844-1, doi:10.1007/s00198-023-06844-1. This article has 75 citations and is from a domain leading peer-reviewed journal.

2. (seefried2025diagnosisandtreatment pages 1-2): L. Seefried, F. Genest, C. Hofmann, M. L. Brandi, and E. Rush. Diagnosis and treatment of hypophosphatasia. Calcified Tissue International, Mar 2025. URL: https://doi.org/10.1007/s00223-025-01356-y, doi:10.1007/s00223-025-01356-y. This article has 13 citations and is from a peer-reviewed journal.

3. (dahir2025medicalmanagementof pages 1-2): Kathryn McCrystal Dahir and Nancy S. Dunbar. Medical management of hypophosphatasia: review of data on asfotase alfa. Current Osteoporosis Reports, Mar 2025. URL: https://doi.org/10.1007/s11914-025-00906-5, doi:10.1007/s11914-025-00906-5. This article has 8 citations and is from a peer-reviewed journal.

4. (santos2025dentalmanifestationsof pages 1-3): Elis J Lira dos Santos, Fatma F Mohamed, Kaitrin Kramer, and Brian L Foster. Dental manifestations of hypophosphatasia: translational and clinical advances. JBMR Plus, Jan 2025. URL: https://doi.org/10.1093/jbmrpl/ziae180, doi:10.1093/jbmrpl/ziae180. This article has 8 citations and is from a peer-reviewed journal.

5. (santos2025dentalmanifestationsof pages 3-4): Elis J Lira dos Santos, Fatma F Mohamed, Kaitrin Kramer, and Brian L Foster. Dental manifestations of hypophosphatasia: translational and clinical advances. JBMR Plus, Jan 2025. URL: https://doi.org/10.1093/jbmrpl/ziae180, doi:10.1093/jbmrpl/ziae180. This article has 8 citations and is from a peer-reviewed journal.

6. (khan2024hypophosphatasiadiagnosiscurrent pages 2-4): Aliya A. Khan, Maria Luisa Brandi, Eric T. Rush, Dalal S. Ali, Hatim Al-Alwani, Khulod Almonaei, Farah Alsarraf, Severine Bacrot, Kathryn M. Dahir, Karel Dandurand, Chad Deal, Serge Livio Ferrari, Francesca Giusti, Gordon Guyatt, Erin Hatcher, Steven W. Ing, Muhammad Kassim Javaid, Sarah Khan, Roland Kocijan, Agnes Linglart, Iman M’Hiri, Francesca Marini, Mark E. Nunes, Cheryl Rockman-Greenberg, Christian Roux, Lothar Seefried, Jill H. Simmons, Susan R. Starling, Leanne M. Ward, Liang Yao, Romina Brignardello-Petersen, and E. Michael Lewiecki. Hypophosphatasia diagnosis: current state of the art and proposed diagnostic criteria for children and adults. Osteoporosis International, 35:431-438, Nov 2024. URL: https://doi.org/10.1007/s00198-023-06844-1, doi:10.1007/s00198-023-06844-1. This article has 75 citations and is from a domain leading peer-reviewed journal.

7. (seefried2024wholegenomesequencing pages 1-2): Lothar Seefried, Anna Petryk, Guillermo del Angel, Felix Reder, and Peter Bauer. Whole genome sequencing in adults with clinical hallmarks of hypophosphatasia negative for alpl variants. Molecular Biology Reports, Sep 2024. URL: https://doi.org/10.1007/s11033-024-09906-7, doi:10.1007/s11033-024-09906-7. This article has 5 citations and is from a peer-reviewed journal.

8. (lipinski2026hypophosphatasiainchildren pages 1-2): Patryk Lipiński, Joanna Rusecka, Zbigniew Michał Żuber, and Robert Stanisław Śmigiel. Hypophosphatasia in children: from low alkaline phosphatase activity to diagnosis, genetic testing, and treatment options. a narrative review. Advances in Clinical and Experimental Medicine, 35:0-0, Jan 2026. URL: https://doi.org/10.17219/acem/205341, doi:10.17219/acem/205341. This article has 0 citations and is from a peer-reviewed journal.