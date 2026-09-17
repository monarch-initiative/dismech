---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-22T04:45:14.852960'
end_time: '2026-08-22T04:48:48.971935'
duration_seconds: 214.12
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Paraneoplastic Pemphigus
  mondo_id: ''
  category: Autoimmune
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    claude_executable: claude
    skip_permissions: false
    allowed_tools:
    - WebSearch
    - WebFetch
    add_dirs: []
    timeout: 1800
    min_report_chars: 200
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 13
  num_turns: 18
  total_cost_usd: 1.1817533999999998
  session_id: 6f8bf895-3ab0-55cb-a154-acb932b43f03
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 23
reference_validation:
  total_references: 16
  verified: 16
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 16
  on_topic: 11
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Paraneoplastic Pemphigus
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on **Paraneoplastic Pemphigus** covering all of the
disease characteristics listed below. This report will be used to populate a disease knowledge
base entry. Be thorough and cite primary literature (PMID preferred) for all claims.

For each section, **suggested databases/resources** are listed. These are the first places
you should search for information on each topic.

---

### 1. Disease Information
> **Search first:** OMIM, Orphanet, ICD-10/ICD-11, MeSH, PubMed

- What is the disease? Provide a concise overview.
- What are the key identifiers? (OMIM, Orphanet, ICD-10/ICD-11, MeSH, Mondo)
- What are the common synonyms and alternative names?
- Is the information derived from individual patients (e.g., EHR) or aggregated disease-level resources?

### 2. Etiology

- **Disease Causal Factors**: What are the primary causes? (genetic, environmental, infectious, mechanistic)
- **Risk Factors**:
  > **Search first:** PubMed, Cochrane Library, UpToDate, clinical guidelines, ClinVar, ClinGen, GWAS Catalog, PheGenI, CTD, CDC, WHO, epidemiological databases
  - Genetic risk factors (causal variants, susceptibility loci, modifier genes)
  - Environmental risk factors (toxins, lifestyle, occupational exposures, age, sex, family history)
- **Protective Factors**:
  > **Search first:** PubMed, Cochrane Library, clinical trial databases, GWAS Catalog, gnomAD, WHO, CDC, nutrition databases
  - Genetic protective factors (protective variants, modifier alleles)
  - Environmental protective factors (diet, lifestyle, exposures that reduce risk)
- **Gene-Environment Interactions**: How do genetic and environmental factors interact to influence disease?
  > **Search first:** CTD, PubMed, PheGenI, GxE databases

### 3. Phenotypes
> **Search first:** HPO (Human Phenotype Ontology), OMIM, Orphanet, PubMed, clinicaltrials.gov, MedDRA, SNOMED CT, DECIPHER, LOINC

For each phenotype, provide:
- **Phenotype type**: symptoms, clinical signs, physical manifestations, behavioral changes, or laboratory abnormalities
  > For symptoms/signs: HPO, OMIM, Orphanet, PubMed
  > For behavioral changes: HPO, DSM, RDoC (Research Domain Criteria), PubMed
  > For laboratory abnormalities: LOINC, SNOMED CT, LabTests Online, PubMed
- **Phenotype characteristics**:
  > **Search first:** OMIM, Orphanet, HPO, PubMed
  - Age of symptom onset (neonatal, childhood, adult-onset, late-onset)
  - Symptom severity (mild, moderate, severe, variable)
  - Symptom progression (stable, progressive, episodic, fluctuating)
  - Frequency among affected individuals (percentage or qualitative)
- **Quality of life impact**: Effects on daily functioning and well-being (per-phenotype when possible)
  > **Search first:** EQ-5D database, SF-36, WHO QOL databases, PubMed
- Suggest HPO (Human Phenotype Ontology) terms for each phenotype

### 4. Genetic/Molecular Information

- **Causal Genes**: Gene mutations or chromosomal abnormalities responsible for disease (gene symbols, OMIM IDs)
  > **Search first:** OMIM, ClinVar, HGMD, Ensembl, NCBI Gene
- **Pathogenic Variants**:
  - Affected genes (gene symbols, HGNC IDs)
    > **Search first:** OMIM, NCBI Gene, Ensembl, HGNC, UniProt, GeneCards
  - Variant classification (pathogenic, likely pathogenic, VUS per ACMG/AMP guidelines)
    > **Search first:** ClinVar, ClinGen, ACMG/AMP guidelines, VarSome
  - Variant type/class (missense, frameshift, nonsense, splice-site, structural)
  - Allele frequency in population databases
    > **Search first:** gnomAD, 1000 Genomes, ExAC, TOPMed, dbSNP
  - Somatic vs germline origin
    > **Search first:** COSMIC (somatic), ClinVar, ICGC, TCGA
  - Functional consequences (loss of function, gain of function, dominant negative)
- **Modifier Genes**: Genes that modify disease severity or expression
- **Epigenetic Information**: DNA methylation, histone modifications, chromatin changes affecting disease
  > **Search first:** ENCODE, Roadmap Epigenomics, MethBase, DiseaseMeth
- **Chromosomal Abnormalities**: Large-scale genetic changes (aneuploidy, translocations, inversions)
  > **Search first:** DECIPHER, ClinVar, ECARUCA, UCSC Genome Browser

### 5. Environmental Information

- **Environmental Factors**: Non-genetic contributing factors (toxins, radiation, pollution, occupational exposure)
  > **Search first:** CTD (Comparative Toxicogenomics Database), TOXNET, PubMed, EPA databases
- **Lifestyle Factors**: Behavioral factors (smoking, diet, exercise, alcohol consumption)
  > **Search first:** CDC databases, WHO, PubMed, NHANES
- **Infectious Agents**: If applicable, pathogens causing or triggering disease (bacteria, viruses, fungi, parasites)
  > **Search first:** NCBI Taxonomy, ViPR, BV-BRC, MicrobeDB, GIDEON

### 6. Mechanism / Pathophysiology

- **Molecular Pathways**: Specific signaling cascades or biochemical pathways involved (Wnt, MAPK, mTOR, PI3K-AKT, etc.)
  > **Search first:** KEGG, Reactome, WikiPathways, PathBank, BioCyc
- **Cellular Processes**: Cell-level mechanisms (apoptosis, autophagy, cell cycle dysregulation, inflammation, etc.)
  > **Search first:** Gene Ontology (GO), Reactome, KEGG, PubMed
- **Protein Dysfunction**: How protein structure or function is altered (misfolding, aggregation, loss of function, gain of function)
  > **Search first:** UniProt, PDB (Protein Data Bank), InterPro, Pfam, AlphaFold
- **Metabolic Changes**: Alterations in metabolic processes (energy metabolism, lipid metabolism, amino acid metabolism)
  > **Search first:** KEGG, BioCyc, HMDB (Human Metabolome Database), BRENDA
- **Immune System Involvement**: Role of immune response (autoimmunity, immunodeficiency, chronic inflammation)
  > **Search first:** ImmPort, Immunome Database, IEDB, Gene Ontology
- **Tissue Damage Mechanisms**: How tissues/ are injured (oxidative stress, ischemia, fibrosis, necrosis)
  > **Search first:** PubMed, Gene Ontology, Reactome
- **Biochemical Abnormalities**: Specific molecular defects (enzyme deficiencies, receptor dysfunction, ion channel defects)
  > **Search first:** BRENDA, UniProt, KEGG, OMIM, PubMed
- **Epigenetic Changes**: DNA methylation, histone modifications affecting gene expression in disease
  > **Search first:** ENCODE, Roadmap Epigenomics, MethBase, DiseaseMeth
- **Molecular Profiling** (if available):
  - Transcriptomics/gene expression changes
    > **Search first:** GEO (Gene Expression Omnibus), ArrayExpress, GTEx, Human Cell Atlas, SRA
  - Proteomics findings
    > **Search first:** PRIDE, ProteomeXchange, Human Protein Atlas, STRING, BioGRID
  - Metabolomics signatures
    > **Search first:** MetaboLights, Metabolomics Workbench, HMDB, METLIN
  - Lipidomics alterations
    > **Search first:** LIPID MAPS, SwissLipids, LipidHome, Metabolomics Workbench
  - Genomic structural features
    > **Search first:** UCSC Genome Browser, Ensembl, NCBI, dbVar, DGV
- **Advanced Technologies** (if applicable):
  - Single-cell analysis findings (cell-type specific mechanisms, cellular heterogeneity)
    > **Search first:** Human Cell Atlas, Single Cell Portal, GEO, CELLxGENE
  - Spatial transcriptomics findings
    > **Search first:** GEO, Spatial Research, Vizgen, 10x Genomics data
  - Multi-omics integration results
    > **Search first:** TCGA, ICGC, cBioPortal, LinkedOmics, PubMed
  - Functional genomics screens (CRISPR, RNAi)
    > **Search first:** DepMap, GenomeRNAi, PubMed, BioGRID ORCS

For each mechanism, describe:
- The causal chain from initial trigger to clinical manifestation
- Which mechanisms are upstream vs downstream
- What cell types and biological processes are involved
- Suggest GO terms for biological processes and CL terms for cell types

### 7. Anatomical Structures Affected

- **Organ Level**:
  - Primary organs directly affected
  - Secondary organ involvement (complications, secondary effects)
  - Body systems involved (cardiovascular, nervous, digestive, respiratory, endocrine, etc.)
  > **Search first:** Uberon, FMA (Foundational Model of Anatomy), OMIM, HPO, ICD-11, MeSH, SNOMED CT
- **Tissue and Cell Level**:
  - Specific tissue types affected (epithelial, connective, muscle, nervous)
  - Specific cell populations targeted (with Cell Ontology terms)
  > **Search first:** Uberon, Human Protein Atlas, Cell Ontology, Human Cell Atlas, CellMarker, PanglaoDB
- **Subcellular Level**:
  - Cellular compartments involved (mitochondria, nucleus, ER, lysosomes) (with GO Cellular Component terms)
  > **Search first:** Gene Ontology (Cellular Component), UniProt, Human Protein Atlas
- **Localization**:
  - Specific anatomical sites (with UBERON terms)
    > **Search first:** FMA, Uberon, NeuroNames (for brain), SNOMED CT
  - Lateralization (unilateral, bilateral, asymmetric)
    > **Search first:** HPO, clinical literature, imaging databases

### 8. Temporal Development

- **Onset**:
  - Typical age of onset (congenital, pediatric, adult, geriatric)
  - Onset pattern (acute, subacute, chronic, insidious)
  > **Search first:** OMIM, Orphanet, HPO, PubMed
- **Progression**:
  - Disease stages (early, intermediate, advanced, end-stage)
    > **Search first:** Cancer Staging Manual (AJCC), WHO classifications, PubMed
  - Progression rate (rapid, slow, variable)
  - Disease course pattern (episodic, relapsing-remitting, progressive, stable)
  - Disease duration (self-limited, chronic lifelong)
  > **Search first:** Disease registries, longitudinal cohort databases, natural history studies, PubMed, Orphanet, OMIM
- **Patterns**:
  - Remission patterns (spontaneous, treatment-induced)
    > **Search first:** Clinical trial databases, disease registries, PubMed
  - Critical periods (time windows of vulnerability or opportunity for intervention)
    > **Search first:** PubMed, developmental biology databases, clinical guidelines

### 9. Inheritance and Population

- **Epidemiology**:
  - Prevalence (cases per 100,000 at given time)
  - Incidence (new cases per 100,000 per year)
  > **Search first:** Orphanet, CDC, WHO, GBD (Global Burden of Disease), national registries, SEER, disease registries
- **For Genetic Etiology**:
  - Inheritance pattern (AD, AR, X-linked, mitochondrial, multifactorial, polygenic)
    > **Search first:** OMIM, Orphanet, ClinVar, GTR (Genetic Testing Registry)
  - Penetrance (complete, incomplete, age-dependent)
    > **Search first:** ClinVar, OMIM, PubMed, ClinGen
  - Expressivity (variable, consistent)
    > **Search first:** OMIM, ClinVar, PubMed
  - Genetic anticipation (increasing severity in successive generations)
    > **Search first:** OMIM, PubMed (especially for repeat expansion disorders)
  - Germline mosaicism
    > **Search first:** ClinVar, OMIM, genetic counseling literature, PubMed
  - Founder effects (population-specific mutations)
    > **Search first:** gnomAD, population genetics databases, PubMed
  - Consanguinity role
    > **Search first:** OMIM, population studies, genetic counseling resources
  - Carrier frequency
    > **Search first:** gnomAD, carrier screening databases, GeneReviews, GTR
- **Population Demographics**:
  - Affected populations (ethnic or demographic groups with higher prevalence)
    > **Search first:** gnomAD, 1000 Genomes, PAGE Study, PubMed, population registries
  - Geographic distribution (endemic areas, regional variation)
    > **Search first:** WHO, CDC, GBD, Orphanet, geographic epidemiology databases
  - Geographic distribution of specific variants
  - Sex ratio (male:female)
    > **Search first:** Disease registries, OMIM, PubMed, epidemiological databases
  - Age distribution of affected individuals
    > **Search first:** CDC, disease registries, SEER, Orphanet

### 10. Diagnostics

- **Clinical Tests**:
  - Laboratory tests (blood, urine, tissue chemistry, specific enzyme assays)
    > **Search first:** LOINC, LabTests Online, PubMed
  - Biomarkers (proteins, metabolites, genetic markers, circulating biomarkers)
    > **Search first:** FDA Biomarker List, BEST (Biomarkers, EndpointS, and other Tools), PubMed
  - Imaging studies (X-ray, CT, MRI, PET, ultrasound)
    > **Search first:** RadLex, DICOM, Radiopaedia, imaging databases
  - Functional tests (pulmonary function, cardiac stress tests)
    > **Search first:** LOINC, clinical guidelines, PubMed
  - Electrophysiology (EEG, EMG, ECG, nerve conduction studies)
    > **Search first:** LOINC, clinical neurophysiology databases, PubMed
  - Biopsy findings (histopathology, immunohistochemistry)
    > **Search first:** SNOMED CT, College of American Pathologists resources, PubMed
  - Pathology findings (microscopic examination)
    > **Search first:** SNOMED CT, Digital Pathology databases, PubMed
- **Genetic Testing**:
  > **Search first:** GTR (Genetic Testing Registry), GeneReviews, ClinGen
  - Overview of recommended genetic testing approach
  - Whole genome sequencing (WGS) utility
    > **Search first:** GTR, ClinVar, GEL (Genomics England), gnomAD
  - Whole exome sequencing (WES) utility
    > **Search first:** GTR, ClinVar, OMIM, GeneMatcher
  - Gene panels (which panels, which genes)
    > **Search first:** GTR, ClinVar, laboratory-specific databases
  - Single gene testing
    > **Search first:** GTR, ClinVar, OMIM, GeneReviews
  - Chromosomal microarray (CMA)
    > **Search first:** DECIPHER, ClinVar, dbVar, ECARUCA
  - Karyotyping
    > **Search first:** Chromosome Abnormality Database, ClinVar, cytogenetics resources
  - FISH
    > **Search first:** ClinVar, cytogenetics databases, PubMed
  - Mitochondrial DNA testing
    > **Search first:** MITOMAP, MSeqDR, ClinVar, GTR
  - Repeat expansion testing
    > **Search first:** GTR, ClinVar, repeat expansion databases, PubMed
- **Omics-Based Diagnostics** (if applicable):
  - RNA sequencing / transcriptomics
    > **Search first:** GEO, ArrayExpress, GTEx, RNA-seq databases
  - Proteomics
    > **Search first:** PRIDE, ProteomeXchange, FDA Biomarker database
  - Metabolomics
    > **Search first:** MetaboLights, Metabolomics Workbench, HMDB
  - Epigenomics
    > **Search first:** GEO, ENCODE, Roadmap Epigenomics, MethBase
  - Liquid biopsy
    > **Search first:** COSMIC, ClinVar, liquid biopsy databases, PubMed
- **Clinical Criteria**:
  - Standardized diagnostic criteria (DSM, ICD, society guidelines)
    > **Search first:** DSM-5, ICD-11, clinical society guidelines, UpToDate
  - Differential diagnosis (other conditions to rule out, with distinguishing features)
    > **Search first:** DynaMed, UpToDate, clinical decision support systems
- **Screening**:
  - Screening methods for asymptomatic individuals (newborn screening, carrier screening, cascade screening)
    > **Search first:** ACMG recommendations, CDC newborn screening, GTR

### 11. Outcome/Prognosis

- **Survival and Mortality**:
  - Survival rate (5-year, 10-year, overall)
    > **Search first:** SEER, cancer registries, disease-specific registries, PubMed
  - Life expectancy (with and without treatment if applicable)
    > **Search first:** Orphanet, disease registries, actuarial databases, PubMed
  - Mortality rate
    > **Search first:** CDC, WHO, GBD, national mortality databases
  - Disease-specific mortality (deaths directly attributable to disease)
    > **Search first:** Disease registries, CDC Wonder, GBD, PubMed
- **Morbidity and Function**:
  - Morbidity (disease-related disability and health impacts)
    > **Search first:** GBD, WHO, disability databases, PubMed
  - Disability outcomes (long-term functional impairments)
    > **Search first:** ICF (International Classification of Functioning), disability registries
  - Quality of life measures (EQ-5D, SF-36, PROMIS, disease-specific tools)
    > **Search first:** EQ-5D database, SF-36, PROMIS, PubMed
- **Disease Course**:
  - Complications (secondary problems: infections, organ failure, etc.)
    > **Search first:** ICD codes, disease registries, clinical databases, PubMed
  - Recovery potential (likelihood and extent of recovery, with vs without treatment)
    > **Search first:** Natural history studies, rehabilitation databases, PubMed
- **Prediction**:
  - Prognostic factors (age, disease severity, biomarkers, treatment response)
    > **Search first:** Prognostic models databases, clinical calculators, PubMed
  - Prognostic biomarkers (molecular markers predicting disease course)
    > **Search first:** FDA Biomarker database, PubMed, cancer prognostic databases

### 12. Treatment

- **Pharmacotherapy**:
  - Pharmacological treatments (drug names, drug classes, mechanisms of action)
    > **Search first:** DrugBank, RxNorm, ATC classification, DailyMed, FDA databases
  - Pharmacogenomics (how genetic variants affect drug metabolism, efficacy, toxicity)
    > **Search first:** PharmGKB, CPIC (Clinical Pharmacogenetics), FDA Table of PGx Biomarkers
- **Advanced Therapeutics**:
  - Gene therapy (viral vectors, CRISPR, gene replacement, gene editing)
    > **Search first:** ClinicalTrials.gov, FDA gene therapy database, ASGCT resources
  - Cell therapy (stem cell transplant, CAR-T, cellular therapeutics)
    > **Search first:** ClinicalTrials.gov, FDA cell therapy database, FACT standards
  - RNA-based therapies (ASOs, siRNA, mRNA therapies)
    > **Search first:** ClinicalTrials.gov, FDA approvals, PubMed
  - Targeted therapies (treatments directed at specific molecular targets)
    > **Search first:** My Cancer Genome, OncoKB, ClinicalTrials.gov, FDA approvals
  - Immunotherapies (checkpoint inhibitors, monoclonal antibodies)
    > **Search first:** Cancer Immunotherapy Database, FDA approvals, ClinicalTrials.gov
- **Surgical and Interventional**:
  - Surgical interventions (types of surgery, timing, outcomes)
    > **Search first:** CPT codes, surgical registries, clinical guidelines, PubMed
- **Supportive and Rehabilitative**:
  - Supportive care (symptom management, pain control, nutrition)
    > **Search first:** Clinical guidelines, Cochrane Library, PubMed
  - Rehabilitation (physical therapy, occupational therapy, speech therapy)
    > **Search first:** Rehabilitation medicine databases, clinical guidelines, PubMed
- **Experimental**:
  - Experimental treatments in clinical trials (with NCT identifiers if available)
    > **Search first:** ClinicalTrials.gov, EU Clinical Trials Register, WHO ICTRP
- **Treatment Outcomes**:
  - Treatment response rates
    > **Search first:** Clinical trial databases, FDA reviews, systematic reviews, PubMed
  - Side effects and adverse events
    > **Search first:** FDA Adverse Event Reporting System (FAERS), MedWatch, PubMed
- **Treatment Strategy**:
  - Treatment algorithms (clinical pathways, decision trees)
    > **Search first:** Clinical practice guidelines, NCCN Guidelines, UpToDate
  - Combination therapies
    > **Search first:** ClinicalTrials.gov, treatment guidelines, PubMed
  - Personalized medicine approaches (genotype-guided treatment)
    > **Search first:** My Cancer Genome, CIViC, PharmGKB, precision medicine databases

For each treatment, suggest NCIT (NCI Thesaurus) clinical-intervention terms where applicable.

### 13. Prevention

- **Prevention Levels**:
  - Primary prevention (preventing disease occurrence: vaccination, risk factor modification)
    > **Search first:** CDC, WHO, USPSTF recommendations, Cochrane Library
  - Secondary prevention (early detection and treatment: screening programs, early intervention)
    > **Search first:** USPSTF, CDC screening guidelines, WHO
  - Tertiary prevention (preventing complications in those with disease)
    > **Search first:** Clinical guidelines, disease management protocols, PubMed
- **Immunization**: Vaccine strategies (if applicable)
  > **Search first:** CDC vaccine schedules, WHO immunization, FDA vaccine database
- **Screening and Early Detection**:
  - Screening programs (population-based: newborn screening, cancer screening)
    > **Search first:** CDC screening programs, USPSTF, cancer screening databases
  - Genetic screening (carrier screening, preimplantation genetic diagnosis, prenatal testing)
    > **Search first:** ACMG recommendations, ACOG guidelines, GTR
  - Risk stratification (identifying high-risk individuals for targeted prevention)
    > **Search first:** Risk prediction models, clinical calculators, PubMed
- **Behavioral Interventions**: Lifestyle modifications to reduce risk
  > **Search first:** CDC, WHO, behavioral intervention databases, Cochrane Library
- **Counseling**: Genetic counseling (risk assessment, family planning guidance)
  > **Search first:** NSGC resources, ACMG guidelines, GeneReviews
- **Public Health**:
  - Public health interventions (sanitation, vector control, health education)
    > **Search first:** CDC, WHO, public health databases, PubMed
  - Environmental interventions (reducing environmental risk factors)
    > **Search first:** EPA databases, WHO environmental health, PubMed
- **Prophylaxis**: Preventive medications or procedures
  > **Search first:** Clinical guidelines, FDA approvals, PubMed

### 14. Other Species / Natural Disease

- **Taxonomy**: Species affected (with NCBI Taxon identifiers)
  > **Search first:** NCBI Taxonomy
- **Breed**: Specific breeds affected (with VBO identifiers if applicable)
  > **Search first:** VBO (Vertebrate Breed Ontology)
- **Gene**: Orthologous genes in other species (with NCBI Gene IDs)
  > **Search first:** NCBI Gene
- **Natural Disease**:
  - Naturally occurring disease in other species (companion animals, wildlife)
    > **Search first:** OMIA (Online Mendelian Inheritance in Animals), VetCompass, PubMed
  - Veterinary relevance and importance in animal health
    > **Search first:** OMIA, veterinary databases, PubMed
- **Comparative Biology**:
  - Comparative pathology (similarities and differences across species)
    > **Search first:** OMIA, comparative pathology databases, PubMed
  - Evolutionary conservation of disease mechanisms
    > **Search first:** HomoloGene, OrthoMCL, Alliance of Genome Resources
- **Transmission** (if applicable):
  - Zoonotic potential
    > **Search first:** CDC zoonotic diseases, WHO zoonoses, GIDEON
  - Cross-species susceptibility
    > **Search first:** NCBI Taxonomy, veterinary databases, PubMed

### 15. Model Organisms

- **Model Types**:
  - Model organism type (mammalian, invertebrate, cellular, in vitro)
    > **Search first:** Alliance of Genome Resources, model organism databases
  - Specific model systems (mouse, rat, zebrafish, Drosophila, C. elegans, yeast, cell lines, organoids, iPSCs)
    > **Search first:** MGI, RGD, ZFIN, FlyBase, WormBase, SGD, ATCC, Cellosaurus
  - Induced models (drug treatment, surgical intervention, environmental manipulation)
    > **Search first:** MGI, model organism databases, PubMed
- **Genetic Models**:
  - Types available (knockout, knock-in, transgenic, conditional, humanized)
    > **Search first:** MGI, IMPC, KOMP, EuMMCR, IMSR
- **Model Characteristics**:
  - Phenotype recapitulation (how well model reproduces human disease features)
    > **Search first:** Model organism databases, comparative studies, PubMed
  - Model limitations (aspects of human disease not captured)
    > **Search first:** Model organism databases, PubMed, review articles
- **Applications**:
  - Research applications (what aspects of disease can be studied)
    > **Search first:** Model organism databases, PubMed
- **Resources**:
  - Model databases
    > **Search first:** MGI, RGD, ZFIN, FlyBase, WormBase, IMSR, EMMA, MMRRC

---

## Citation Requirements

- Cite primary literature (PMID preferred) for all mechanistic and clinical claims
- Prioritize recent reviews and landmark papers
- Include direct quotes from abstracts where possible to support key statements
- Distinguish evidence source types: human clinical, model organism, in vitro, computational

## Output Format

Structure your response as a comprehensive narrative organized by the sections above.
For each section, provide:
- Factual content with specific details (numbers, percentages, gene names, variant nomenclature)
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, NCIT, MONDO) where applicable
- Evidence citations with PMIDs
- Direct quotes from abstracts to support key claims
- Clear indication when information is not available or not applicable for this disease

This report will be used to populate a disease knowledge base entry with:
- Pathophysiology descriptions with causal chains
- Gene/protein annotations (HGNC, GO terms)
- Phenotype associations (HP terms) with frequencies
- Cell type involvement (CL terms)
- Anatomical locations (UBERON terms)
- Chemical entities (CHEBI terms)
- Treatment annotations (NCIT terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


## Output

I'll research Paraneoplastic Pemphigus comprehensively, starting with key searches across the major topic areas.

I now have comprehensive material across all sections. I'll compile the full research report.

# Paraneoplastic Pemphigus (PNP) / Paraneoplastic Autoimmune Multiorgan Syndrome (PAMS): Comprehensive Research Report

## 1. Disease Information

**Overview:** Paraneoplastic pemphigus (PNP), also increasingly termed paraneoplastic autoimmune multiorgan syndrome (PAMS), is a rare, highly fatal autoimmune mucocutaneous blistering disease that arises in patients with an underlying benign or malignant neoplasm — most commonly a lymphoproliferative disorder. First described by Anhalt et al. in 1990, it is immunologically and clinically distinct from other pemphigus variants, defined by circulating autoantibodies against desmosomal cadherins (desmogleins 1 and 3) **and** the plakin family of cytoskeletal-linker proteins, combined with a strong cell-mediated (cytotoxic T-cell) component. The term PAMS, proposed in 2001, was introduced to capture the disease's polymorphous mucocutaneous presentation, immunologic abnormalities, and potential for multi-organ (notably pulmonary) involvement, distinguishing it from "classic" pemphigus that happens to co-occur with a tumor ([StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK546694/); [JAAD Part I, PMID:37597771](https://pubmed.ncbi.nlm.nih.gov/37597771/)).

**Key identifiers:**
| Resource | ID |
|---|---|
| MONDO | MONDO:0018974 |
| Orphanet | ORPHA:63455 |
| ICD-11 | EB40.2 |
| ICD-10-CM | L10.81 |
| OMIM | Not listed (not a monogenic/Mendelian disorder) |
| MeSH | Pemphigus, subheading "Paraneoplastic" (D016883 parent) |

Sources: [Orphanet](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=EN&Expert=63455), [ICD10Data](https://www.icd10data.com/ICD10CM/Codes/L00-L99/L10-L14/L10-/L10.81), [Wikidata Q1394580](https://www.wikidata.org/wiki/Q1394580)

**Synonyms:** Paraneoplastic autoimmune multiorgan syndrome (PAMS); PNP; paraneoplastic autoimmune bullous disease.

**Evidence base:** Because PNP is exceedingly rare, virtually all data derive from aggregated case reports, case series, and retrospective cohort studies (largest series ~144–149 patients) rather than large prospective EHR-derived cohorts; there are no population-based registries.

---

## 2. Etiology

### Disease Causal Factors
PNP is not caused by a germline mutation; it is a tumor-triggered autoimmune syndrome. An underlying neoplasm — most often lymphoproliferative — is believed to trigger aberrant B-cell and T-cell responses that cross-react with epithelial adhesion-complex proteins (molecular mimicry / epitope spreading hypothesis), producing pathogenic autoantibodies and autoreactive cytotoxic T cells (StatPearls; JAAD Part I).

### Associated Neoplasms (Risk Factor: presence of these tumors)
Across pooled case series, the underlying neoplasm distribution is approximately:
- **Non-Hodgkin lymphoma** — 38.6% (largest series with hematologic malignancy: 52.78%)
- **Chronic lymphocytic leukemia (CLL)** — 18.4% (up to 22.92% in some series)
- **Castleman disease** — 18.4% (up to 18.60%); this is the **dominant association in children and adolescents**, given Castleman disease's rarity in the general population but disproportionate co-occurrence with pediatric PNP
- **Thymoma** — 5.5%
- **Waldenström macroglobulinemia** — 1.2%
- **Hodgkin lymphoma** — 0.6%
- **Monoclonal gammopathy** — 0.6%
- Solid tumors: follicular dendritic cell sarcoma, squamous cell carcinoma, and carcinomas of lung, stomach, colon

Lymphoproliferative neoplasms overall account for ~84% of PNP cases (StatPearls). In ~30% of cases, PNP is the **first clinical manifestation** of an occult neoplasm, meaning the skin/mucosal disease precedes cancer diagnosis. Sources: [PMC11587122](https://pmc.ncbi.nlm.nih.gov/articles/PMC11587122/), [Risk factors for death and survival, PMID:30981429](https://pubmed.ncbi.nlm.nih.gov/30981429/).

### Genetic Risk Factors
- **HLA-DRB1\*03** — associated with increased PNP susceptibility in French Caucasian populations
- **HLA-Cw\*14** — associated in Chinese populations
- In Chinese Han patients, HLA-B\*4002/B\*4004, B\*51, B\*52, Cw\*14, DQB1\*0301, DRB1\*08, and DRB1\*11 were relatively enriched versus controls
- Notably, **HLA-DR4 and DR1/DR14**, which confer risk for pemphigus vulgaris and pemphigus foliaceus, show **no association** with PNP — underscoring PNP's distinct immunogenetic basis from classic pemphigus

Source: [PMC7341728, "Beyond the HLA polymorphism"](https://pmc.ncbi.nlm.nih.gov/articles/PMC7341728/); [StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK546694/).

### Environmental / Age / Sex Risk Factors
- Age: typical onset 45–70 years (mean ~64.7 years); pediatric cases occur, strongly linked to Castleman disease
- Sex: roughly equal male:female distribution (no strong sex predilection reported)
- No established toxin, occupational, or infectious trigger independent of the neoplasm itself

### Protective Factors
No specific genetic or environmental protective factors have been established in the literature; this is consistent with PNP's status as a rare, tumor-driven paraneoplastic syndrome rather than a polygenic/environmentally-modulated common disease.

### Gene-Environment Interactions
Not well characterized beyond the HLA-neoplasm relationship above; the operative model is that neoplasm-driven immune dysregulation (particularly IL-6-producing lymphoproliferative tissue, as in Castleman disease) interacts with HLA-restricted antigen presentation to drive autoreactive B- and T-cell clones.

---

## 3. Phenotypes

### Mucosal (earliest and most consistent feature)
PNP "almost always presents with early mucosal involvement," typically severe, painful, treatment-refractory **oral mucosal erosions/ulcerations** that may be the sole presenting sign. Involvement can extend to the vermilion border, tongue, oropharynx, nasopharynx, esophagus, conjunctiva, and anogenital mucosa (StatPearls).
- Suggested HPO terms: **HP:0032247** (Oral mucosal blister-like lesion) / HP:0002745 (Ulcerated skin lesion) — oral erosions specifically map best to general mucosal ulceration/erosion terms; conjunctival scarring maps to **HP:0007957** (corneal/conjunctival scarring-type terms) or **HP:0000581** (Blepharophimosis-adjacent conjunctival terms; more precisely conjunctival scarring/symblepharon).

### Cutaneous — Five Clinical Subtypes (polymorphous)
1. **Pemphigus-like**: flaccid vesicles/bullae, crusted erosions (intraepidermal/suprabasal acantholysis)
2. **Pemphigoid-like**: tense subepidermal blisters, scaling erythematous plaques
3. **Erythema multiforme-like** (**most common presentation, ~56%**): polymorphic targetoid/erythematous lesions with dyskeratosis
4. **Graft-versus-host disease-like**: diffuse dusky, scaly papules
5. **Lichen planus-like**: violaceous flat-topped papules with lichenoid infiltrate

Source: StatPearls; DermNet.

### Extracutaneous/Multi-organ Involvement (the "multiorgan" in PAMS)
- **Ocular**: up to 70% of patients; pseudomembranous conjunctivitis, progressive cicatrizing conjunctival scarring, corneal erosion, pterygium — potential for **irreversible blindness**
- **Pulmonary**: 59.1–92.8% of cases; dyspnea, dry cough, obstructive lung disease progressing to **bronchiolitis obliterans** (incidence estimates 27–93% across studies) — a leading cause of death
- **Myasthenic symptoms**: 39% of studied patients report symptoms; 35% meet criteria for myasthenia gravis by anti-acetylcholine-receptor antibody titer, especially with thymoma-associated PNP
- **Gastrointestinal**: esophageal erosions, dysphagia
- Additional reported organ involvement: thyroid, kidney

Source: StatPearls; [PMC11277726 (airway involvement)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11277726/).

### Laboratory/Immunologic Abnormalities
Circulating autoantibodies against plakin-family proteins and desmogleins (see Section 4); elevated inflammatory markers related to the underlying lymphoproliferative disease.

### Phenotype Characteristics
- **Onset**: adult (45–70y peak) but can occur in children/adolescents (Castleman-associated)
- **Severity**: variable but generally severe; extensive mucocutaneous involvement is an adverse prognostic sign
- **Progression**: often relapsing/progressive; cutaneous lesions may improve within ~12 weeks of treatment, but **mucosal disease is frequently refractory**
- **Frequency of specific manifestations**: erythema multiforme-like cutaneous pattern in 56%; ocular in up to 70%; pulmonary in 59–93%; myasthenic symptoms in 39%

### Quality of Life Impact
Severe painful oral erosions impair eating/nutrition (frequently requiring nasogastric feeding); ocular scarring can cause permanent visual impairment; bronchiolitis obliterans causes progressive, often fatal, respiratory disability; extensive skin denudation requires burn-unit–level wound care and carries infection/sepsis risk.

Suggested HPO terms for pathophysiology-related phenotypes: **HP:0200042** (Skin ulcer), **HP:0100836** (Blistering) type terms, **HP:0002206** (Pulmonary fibrosis/obliterans-adjacent — bronchiolitis obliterans itself has no precise dedicated HPO term but maps near obstructive lung disease terms), **HP:0000546** (Blindness), **HP:0003324** (Generalized muscle weakness — myasthenic).

---

## 4. Genetic/Molecular Information

PNP is **not a Mendelian genetic disease** — there is no single causal gene. Instead, disease-defining molecular features are the **autoantibody targets**:

### Target Antigens (Plakin Family + Desmosomal Cadherins)
| Antigen | MW | Notes |
|---|---|---|
| Desmoplakin I | 250 kDa | Most consistently detected by immunoprecipitation |
| BP230 (bullous pemphigoid antigen 1) | 230 kDa | Also targeted in bullous pemphigoid |
| Desmoplakin II | 210 kDa | |
| Envoplakin | 210 kDa | Along with periplakin, the **most characteristic/consistently recognized** PNP antigen |
| Periplakin | 190 kDa | |
| Plectin | ~500 kDa | |
| Epiplakin | — | Specifically associated with **bronchiolitis obliterans** development |
| α2-macroglobulin-like-1 (A2ML1) | 170 kDa | A protease inhibitor, not a classic plakin |
| Desmoglein 3 (Dsg3) | — | Shared with pemphigus vulgaris |
| Desmoglein 1 (Dsg1) | — | Shared with pemphigus foliaceus |

Sources: [PMC6558011](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6558011/); [PMC9332891 — anti-desmoplakin C-terminus antibodies induce acantholysis in vivo](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9332891/); [Frontiers 10.3389/fimmu.2022.886226](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2022.886226/full).

### Functional Consequence
Plakin proteins are cytolinkers connecting the keratin intermediate filament cytoskeleton to desmosomes and hemidesmosomes. Autoantibody binding — particularly against the desmoplakin C-terminus — directly disrupts desmosomal adhesion, producing **acantholysis** (loss of keratinocyte cell-cell adhesion), demonstrated experimentally in murine models (dose-dependent blister/acantholysis induction and keratinocyte apoptosis after antibody injection in neonatal mice).

### Modifier/Susceptibility Genes
HLA-DRB1\*03 (Caucasian), HLA-Cw\*14 (Chinese) — see Section 2.

### Epigenetics / Chromosomal Abnormalities
Not specifically characterized for PNP; the underlying lymphoproliferative neoplasm (e.g., CLL, follicular lymphoma) may carry its own somatic cytogenetic lesions (e.g., t(14;18) in follicular lymphoma), but these are neoplasm-intrinsic rather than PNP-defining.

Suggested gene/protein annotation terms (HGNC): DSP (desmoplakin), EVPL (envoplakin), PPL (periplakin), DST/BPAG1 (BP230/dystonin), PLEC (plectin), PKP1-3 (plakophilins, less characteristic), DSG1, DSG3, A2ML1.

---

## 5. Environmental Information

There is no established environmental toxin, radiation, or occupational exposure directly implicated in PNP etiology. The dominant "environmental" trigger, functionally, is the presence of the associated neoplasm itself (see Section 2), which is presumed to drive antigen release/molecular mimicry and cytokine-driven (e.g., IL-6, particularly relevant in Castleman disease) immune dysregulation. No specific infectious agent has been established as causal for PNP itself (distinct from its associated neoplasms, some of which — e.g., certain lymphomas — may have viral associations such as EBV, though this is not PNP-specific).

---

## 6. Mechanism / Pathophysiology

### Causal Chain (Trigger → Manifestation)
1. **Underlying neoplasm** (lymphoproliferative disorder, thymoma, or Castleman disease) → dysregulated B- and T-cell immunity
2. **Autoantibody production** against plakin-family desmosomal/hemidesmosomal linker proteins (envoplakin, periplakin, desmoplakins, BP230, plectin, epiplakin) and desmogleins (Dsg1/Dsg3) — proposed mechanism includes molecular mimicry between tumor antigens and epithelial adhesion proteins
3. **Autoantibody binding** disrupts desmosome-cytoskeleton linkage → **acantholysis** (intraepidermal keratinocyte separation) — directly demonstrated for anti-desmoplakin C-terminus antibodies in vivo (murine skin) and in vitro
4. **Concurrent cell-mediated cytotoxicity**: autoreactive CD4+ and CD8+ T cells (including a Th17-skewed, T follicular helper-like Dsg3-reactive population) infiltrate lesional tissue, producing **interface dermatitis** with keratinocyte apoptosis/necrosis — a histologic and mechanistic feature that distinguishes PNP from antibody-only-mediated pemphigus vulgaris
5. **Multi-organ epithelial targeting**: because plakins/desmosomes are expressed broadly across stratified and transitional epithelia (skin, oral/esophageal mucosa, conjunctiva) and — critically — in **bronchial epithelium**, the same autoimmune attack extends to the respiratory tract, producing **bronchiolitis obliterans** (epiplakin autoantibodies specifically implicated), the dominant driver of PNP mortality.

### Molecular/Cellular Processes
- Loss of keratinocyte-keratinocyte adhesion (desmosome disruption)
- Keratinocyte apoptosis/necrosis (dyskeratosis)
- Basal layer vacuolization (interface dermatitis pattern)
- Lymphocytic exocytosis into epithelium
- Bronchiolar epithelial injury, fibrosis, and obliteration (bronchiolitis obliterans) — lung biopsy shows bronchiole fibrosis, dense lymphohistiocytic infiltrates, and autoantibody deposition

Suggested GO terms: **GO:0007156** (homophilic cell adhesion via plasma membrane adhesion molecules), **GO:0030057** (desmosome), **GO:0006915** (apoptotic process), **GO:0002250** (adaptive immune response), **GO:0042113** (B cell activation).

Suggested CL terms: **CL:0000312** (keratinocyte), **CL:0000000** downstream — specifically stratified squamous epithelial cell; **CL:0000784** (plasmacytoid... not applicable) — better: **CL:0000542** (lymphocyte), **CL:0000625** (CD8-positive alpha-beta T cell), **CL:0000546** (T-helper cell).

Suggested UBERON terms: **UBERON:0001003** (skin epidermis), **UBERON:0001744** (tonsil/oral mucosa-adjacent), **UBERON:0006562** (oral mucosa), **UBERON:0002185** (bronchiole), **UBERON:0001772** (conjunctiva).

### Molecular Profiling / Advanced Technologies
The literature on PNP is dominated by immunoprecipitation/immunoblot and ELISA-based antigen characterization rather than modern multi-omic (transcriptomic/proteomic/single-cell) profiling; no major GEO/single-cell atlas datasets specific to PNP were identified in this search. This represents a notable data gap relative to other autoimmune skin diseases.

Source: [PMC6558011](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6558011/); [PMC9332891](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9332891/); [JCI 29403 — Dsg3-specific CD4+ T cells induce pemphigus and interface dermatitis in mice](https://www.jci.org/articles/29403); [PMC10107879 — T cell autoimmunity to Dsg3](https://pmc.ncbi.nlm.nih.gov/articles/PMC10107879/).

---

## 7. Anatomical Structures Affected

- **Organ level**: skin (epidermis), oral cavity, oropharynx, nasopharynx, esophagus, conjunctiva/cornea, anogenital mucosa, lungs/bronchioles, and (via associated myasthenia gravis) neuromuscular junction; kidney and thyroid involvement reported less commonly
- **Body systems**: integumentary, mucosal/gastrointestinal, ocular, respiratory, and (secondarily) neuromuscular
- **Tissue/cell level**: stratified squamous epithelium (skin, oral mucosa, esophagus, conjunctiva), transitional epithelium (bladder — relevant diagnostically, see Section 10), bronchiolar epithelium; keratinocytes are the principal targeted cell population
- **Subcellular**: desmosomes and hemidesmosomes (cell junction complexes); keratin intermediate filament cytoskeleton
- **Localization**: bilateral/diffuse, non-lateralized involvement typical

Suggested UBERON: UBERON:0001003 (epidermis), UBERON:0006562 (oral mucosa), UBERON:0001043 (esophagus), UBERON:0001772 (conjunctiva), UBERON:0002185 (bronchiole), UBERON:0001255 (urinary bladder — diagnostic substrate).

---

## 8. Temporal Development

- **Onset**: adult, typically 45–70 years; pediatric onset associated with Castleman disease; onset is typically **subacute**, beginning with refractory oral mucositis
- **Progression**: cutaneous lesions may resolve within ~12 weeks of treatment; **mucosal lesions are frequently persistent/poorly responsive**; pulmonary disease (bronchiolitis obliterans) is often **progressive and irreversible**
- **Disease course pattern**: variable — can be relapsing or steadily progressive; "there is not always a parallel evolution between PNP severity and the malignancy's treatment response," meaning cutaneous/mucosal/pulmonary disease can progress even after successful cancer treatment (StatPearls)
- **Duration**: chronic when survived; however most patients die within one year of diagnosis
- **Remission**: possible with successful resection/treatment of a benign underlying tumor (e.g., Castleman disease, localized thymoma), which offers the best prognosis

---

## 9. Inheritance and Population

### Epidemiology
- PNP accounts for only **3–5%** of all pemphigus cases (pemphigus overall is itself rare)
- No formal population-based incidence/prevalence rate has been established (extremely rare disease, case-series-based literature only)

### Inheritance
- **Not a Mendelian inherited disease** — no defined inheritance pattern (AD/AR/X-linked); susceptibility is polygenic/immunogenetic (HLA-associated) combined with an acquired triggering neoplasm
- No known penetrance, expressivity, anticipation, mosaicism, or carrier-frequency concepts apply, as this is an acquired paraneoplastic autoimmune disease, not a germline genetic disorder

### Population Demographics
- Sex ratio: approximately equal (M:F ~1:1)
- Age distribution: mean age at diagnosis ~64.7 years in adult series; a distinct pediatric/adolescent cluster exists, driven by Castleman disease association
- Ethnic/geographic variation is reflected mainly in differing HLA-risk-allele profiles (Caucasian: DRB1\*03; Chinese: Cw\*14 and related alleles) rather than differential prevalence data

Sources: StatPearls; [PMC7341728](https://pmc.ncbi.nlm.nih.gov/articles/PMC7341728/).

---

## 10. Diagnostics

### Diagnostic Criteria Frameworks
Three overlapping criteria systems are used:

**1. Anhalt's original criteria (5 components):**
- Clinical: painful mucosal erosions ± polymorphous cutaneous lesions with an underlying malignancy
- Histopathology: suprabasal acantholysis, interface dermatitis, keratinocyte necrosis
- Direct immunofluorescence (DIF): IgG/C3 in intercellular spaces ± basement membrane zone
- Indirect immunofluorescence (IIF) on rat/murine bladder transitional epithelium
- Immunoprecipitation: characteristic plakin protein pattern (250, 230, 210, 190, 170 kDa bands)

**2. Joly criteria** (high specificity 84–100%, sensitivity 82–86%): (a) underlying lymphoproliferative disorder, (b) IIF-positive on rat bladder, (c) anti-periplakin/anti-envoplakin autoantibodies by immunoblot.

**3. Camisa and Helm major/minor criteria**: requires 3 major, or 2 major + 2 minor criteria (major: polymorphic mucocutaneous eruption, concomitant neoplasm, characteristic immunoprecipitation pattern; minor: histologic acantholysis, DIF pattern, positive rat bladder IIF).

### Key Test Characteristics
- **DIF** can be **negative in up to 50%** of cases — a negative DIF does NOT exclude PNP
- **IIF on rodent/murine bladder**: sensitivity ~75%, specificity ~83%; negative/indeterminate in up to one-fourth of patients — an adequate screening test but not conclusive alone; useful for discriminating PNP from pemphigus vulgaris/foliaceus (which are typically negative on this substrate)
- **Immunoblot** is considered the **gold standard**, detecting anti-envoplakin (210 kDa)/anti-periplakin (190 kDa) reactivity with high sensitivity/specificity
- **ELISA** assays for anti-envoplakin/anti-periplakin antibodies are also available and increasingly used

### Additional Malignancy Workup
Once PNP is suspected: CBC, LDH, flow cytometry, and cross-sectional imaging (chest/abdomen/pelvis) to identify an occult neoplasm.

### Differential Diagnosis
Stevens-Johnson syndrome/toxic epidermal necrolysis (erythema multiforme-like PNP is often mistaken for these), erythema multiforme, lichen planus, graft-versus-host disease, HSV infection, drug-induced pemphigus, pemphigus vulgaris, mucous membrane pemphigoid, bullous pemphigoid, staphylococcal scalded skin syndrome, chemotherapy-induced stomatitis.

Sources: StatPearls; [ScienceDirect (S0365059620306310)](https://www.sciencedirect.com/science/article/pii/S0365059620306310); [Accuracy of IIF, ScienceDirect 0190962295900667](https://www.sciencedirect.com/science/article/pii/0190962295900667).

---

## 11. Outcome/Prognosis

- **Mortality**: 70–90% (StatPearls cites "approaching 90%"); one large hematologic-malignancy-associated cohort (n=144) reported an overall mortality rate of **57%**. **Most patients die within one year of diagnosis.**
- **Causes of death**: widespread cutaneous infection/sepsis (loss of skin barrier), progression of the underlying malignancy, and **bronchiolitis obliterans-related respiratory failure** — the latter is frequently cited as the single most common proximate cause of death
- **Adverse prognostic factors**: keratinocyte necrosis on histology, erythema multiforme-like or TEN-like or bullous-pemphigoid-like cutaneous presentation, extensive mucocutaneous disease at presentation, presence of **envoplakin autoantibodies**, and development of bronchiolitis obliterans
- **Favorable factors**: resectable/benign underlying tumor (localized Castleman disease, encapsulated thymoma) is associated with markedly better outcomes than diffuse lymphoproliferative malignancy
- **Bronchiolitis obliterans** specifically: affects 27–93% of patients across studies (StatPearls cites 30–90%); may require lung transplantation in severe cases
- **Complication burden**: irreversible blindness (ocular scarring), fluid/electrolyte derangement from cutaneous erosions, malnutrition from oral involvement (often requiring NG feeding), contractures requiring rehabilitation

Sources: [Risk factors for death, PMID:30981429](https://pubmed.ncbi.nlm.nih.gov/30981429/); [PMC9060127 — BO requiring lung transplant](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9060127/); StatPearls.

---

## 12. Treatment

### First-Line
**High-dose systemic corticosteroids** remain first-line therapy for PNP disease control (StatPearls; 2025 systematic review). NCIT term: **NCIT:C15986** (Pharmacotherapy) with therapeutic_agent bound to corticosteroid class (e.g., **NCIT:C2280** Prednisone / **NCIT:C2322** Corticosteroid class).

### Steroid-Sparing / Immunosuppressive Agents
- Azathioprine, mycophenolate mofetil, cyclosporine, cyclophosphamide — added for steroid-refractory disease
- NCIT: **NCIT:C15632** (Chemotherapy) or **NCIT:C15986** (Pharmacotherapy) + therapeutic_agent

### Biologics
- **Rituximab** (anti-CD20 monoclonal antibody) — shown efficacious particularly in lymphoproliferative-malignancy-associated PNP; NCIT: **NCIT:C1932** (Rituximab); therapeutic_modality: MONOCLONAL_ANTIBODY
- **Alemtuzumab** (anti-CD52) — used in select cases
- A 2025 systematic review (Advances in Rheumatology) of rituximab + IVIG combination therapy across autoimmune bullous disease found **positive outcomes in all but one reported PNP case**, though infection risk (e.g., *P. jirovecii* pneumonia) was noted as a safety concern

### Intravenous Immunoglobulin (IVIG)
Used both as adjunct therapy and, notably, **peri-operatively** (before/after surgical resection of the underlying tumor) — proposed to reduce bronchiolitis-obliterans risk by neutralizing released autoantibodies at the time of tumor lysis. NCIT: **NCIT:C15986**/therapeutic_agent immunoglobulin.

### Plasmapheresis
Used adjunctively in refractory/severe disease.

### Malignancy-Directed Therapy
Early diagnosis and definitive treatment of the underlying neoplasm is paramount — surgical resection for solid/localized tumors (thymoma, Castleman disease), and lymphoma/CLL-directed chemoimmunotherapy (e.g., R-CHOP regimens) for lymphoproliferative disease. Notably, mucocutaneous disease does not always parallel malignancy treatment response.

### Supportive/Wound Care (burn-unit level)
Occlusive hydrating dressings, warm-water compresses, low-adhesive/petrolatum dressings, silver antimicrobial dressings, topical corticosteroids/calcineurin inhibitors, triamcinolone gel and analgesic mouthwash for oral lesions, nasogastric feeding, pressure-ulcer prevention, antiseptic care, and systemic antibiotics for secondary infection.

### Multidisciplinary Team
Oncology, dermatology, ophthalmology, pulmonology, gastroenterology, urology, infectious disease, wound care nursing, nutrition, and mental health support.

### Experimental / Emerging
Lung transplantation has been reported for end-stage bronchiolitis obliterans in PNP associated with Castleman disease. Newer B-cell-depleting agents used in refractory classic pemphigus (e.g., inebilizumab) are an area of emerging interest but lack dedicated PNP data.

Sources: StatPearls; [Advances in Rheumatology systematic review, 2025](https://link.springer.com/article/10.1186/s42358-025-00450-x); [PMC9060127](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9060127/); [International Journal of Hematology — R-CHOP long-term survival case](https://link.springer.com/article/10.1007/s12185-017-2305-2).

---

## 13. Prevention

There is no established primary prevention strategy for PNP, as it arises unpredictably in association with an underlying neoplasm. The literature emphasizes:
- **Secondary prevention / early detection**: prompt malignancy workup (CBC, LDH, flow cytometry, imaging) in any patient presenting with refractory mucocutaneous erosions and a polymorphous eruption, since PNP precedes malignancy diagnosis in ~30% of cases
- **Tertiary prevention**: perioperative IVIG administration around tumor resection, proposed to blunt autoantibody-mediated bronchiolar injury and reduce bronchiolitis obliterans risk
- Genetic counseling is not applicable given the non-Mendelian, acquired nature of the disease
- Ophthalmology and pulmonology surveillance are recommended early in the disease course to catch ocular scarring and early bronchiolitis obliterans before irreversible damage occurs

---

## 14. Other Species / Natural Disease

PNP is one of the few paraneoplastic autoimmune blistering diseases with **documented spontaneous veterinary analogs**:
- **Dogs**: paraneoplastic pemphigus has been reported in association with splenic sarcoma and other neoplasms; canine disease shares clinical and immunopathologic features with human PNP ([Elmore et al. 2005, Vet Pathol](https://journals.sagepub.com/doi/10.1354/vp.42-1-88))
- **Cats and horses**: also reported, reviewed comprehensively alongside canine/feline/equine pemphigus vulgaris and pemphigus vegetans in a 2020 BMC Veterinary Research review ([PMID:33228633](https://pubmed.ncbi.nlm.nih.gov/33228633/); [PMC7686683](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7686683/))
- Prognosis in veterinary PNP is described as "grave," paralleling the poor human prognosis; treatment follows similar high-dose glucocorticoid ± immunosuppressant principles as pemphigus vulgaris/vegetans in animals, though PNP itself is noted as rare in dogs specifically associated with neoplasia

NCBI Taxon: dog (NCBITaxon:9615), cat (NCBITaxon:9685), horse (NCBITaxon:9796). No OMIA (Online Mendelian Inheritance in Animals) entry was surfaced, consistent with PNP's non-Mendelian, acquired etiology in animals as in humans.

---

## 15. Model Organisms

- **In vivo murine models**: Neonatal/adult mouse skin injection models have been used to demonstrate pathogenicity of PNP autoantibodies — specifically, **anti-desmoplakin C-terminus IgG** induced dose-dependent blister formation and acantholysis in mouse skin, with keratinocyte apoptosis observed in neonatal mice after antibody passive transfer ([PMC9332891](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9332891/); [Frontiers 10.3389/fimmu.2022.886226](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2022.886226/full)). These are **passive-transfer/induced models**, not genetic knockouts, and directly recapitulate acantholysis and blister formation but not the full multi-organ (pulmonary/ocular) phenotype or the underlying neoplasm trigger.
- **Related pemphigus vulgaris T-cell models**: Dsg3-specific CD4+ T-cell transfer models in mice induce pemphigus-like blistering **and interface dermatitis**, a histologic hallmark shared with PNP, providing a mechanistic model for the T-cell-mediated component of PNP pathogenesis even though these studies were performed in a pemphigus vulgaris (not PNP) context ([JCI 29403](https://www.jci.org/articles/29403); [PMC10107879](https://pmc.ncbi.nlm.nih.gov/articles/PMC10107879/)).
- **Limitations**: No model fully recapitulates the tumor-triggered, multi-antigen (plakin + desmoglein), multi-organ (skin + mucosa + lung) nature of human PNP; existing models isolate single antibody specificities or T-cell clones rather than the full autoimmune repertoire seen clinically. No PNP-specific knockout, transgenic, humanized, or organoid/iPSC model system was identified in this search — representing a clear research gap relative to pemphigus vulgaris, for which more developed genetic mouse models exist.

---

## Summary of Suggested Ontology Term Bindings for KB Curation

| Category | Suggested terms |
|---|---|
| Disease | MONDO:0018974 |
| Causal genes (autoantigens) | hgnc: DSP, EVPL, PPL, DST (BP230), PLEC, DSG1, DSG3, A2ML1 |
| Phenotypes (HP) | oral/mucosal erosion, conjunctival scarring, blindness, obstructive lung disease/bronchiolitis obliterans (nearest available term), generalized muscle weakness (myasthenic) |
| Cell types (CL) | CL:0000312 (keratinocyte), CL:0000625 (CD8+ T cell), CL:0000546 (T-helper cell), CL:0000236 (B cell) |
| Biological processes (GO) | GO:0007156 (cell-cell adhesion), GO:0030057 (desmosome), GO:0006915 (apoptosis) |
| Anatomy (UBERON) | UBERON:0001003 (epidermis), UBERON:0006562 (oral mucosa), UBERON:0002185 (bronchiole), UBERON:0001772 (conjunctiva) |
| Treatments (NCIT) | NCIT:C15986 (Pharmacotherapy) + therapeutic_agent (corticosteroid, rituximab NCIT:C1932, IVIG), NCIT:C15329 (Surgical Procedure) for tumor resection |

---

## Key Citations
- [Anhalt/PAMS Part I — Clinical overview and pathophysiology, PMID:37597771](https://pubmed.ncbi.nlm.nih.gov/37597771/) (JAAD, 2024)
- [PAMS Part II — Diagnosis and management, PMID:37714216](https://pubmed.ncbi.nlm.nih.gov/37714216/) (JAAD, 2024)
- [Paraneoplastic Pemphigus — StatPearls (NCBI Bookshelf NBK546694)](https://www.ncbi.nlm.nih.gov/books/NBK546694/)
- [Oral Paraneoplastic Pemphigus: Scoping Review, PMC11587122](https://pmc.ncbi.nlm.nih.gov/articles/PMC11587122/)
- [Paraneoplastic Pemphigus: Paraneoplastic Autoimmune Disease of the Skin and Mucosa, PMC6558011](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6558011/)
- [Anti-desmoplakin C-terminus autoantibodies induce acantholysis in vitro/in vivo, PMC9332891](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9332891/)
- [Risk factors for death and survival in PNP with hematologic malignancy, PMID:30981429](https://pubmed.ncbi.nlm.nih.gov/30981429/)
- [Beyond HLA polymorphism — genetic susceptibility to pemphigus, PMC7341728](https://pmc.ncbi.nlm.nih.gov/articles/PMC7341728/)
- [Clinical/pathological features of BO requiring lung transplant in PNP with Castleman disease, PMC9060127](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9060127/)
- [Deep pemphigus in dogs, cats, and horses — comprehensive review, PMID:33228633](https://pubmed.ncbi.nlm.nih.gov/33228633/)
- [Rituximab + IVIG in autoimmune diseases — systematic review, 2025](https://link.springer.com/article/10.1186/s42358-025-00450-x)
- [Orphanet: Paraneoplastic pemphigus (ORPHA:63455)](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=EN&Expert=63455)
- [Desmoglein 3-specific CD4+ T cells induce pemphigus vulgaris and interface dermatitis in mice, JCI 29403](https://www.jci.org/articles/29403)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 16 |
| On topic | 11 |
| Off topic | 0 |

All extracted references resolved successfully.