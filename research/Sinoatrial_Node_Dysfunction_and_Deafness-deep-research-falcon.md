---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-01T18:26:33.263948'
end_time: '2026-08-01T18:36:07.983678'
duration_seconds: 574.72
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Sinoatrial Node Dysfunction and Deafness
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 19
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Sinoatrial_Node_Dysfunction_and_Deafness-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Sinoatrial Node Dysfunction and Deafness
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Sinoatrial Node Dysfunction and Deafness** covering all of the
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

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Sinoatrial Node Dysfunction and Deafness
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Sinoatrial Node Dysfunction and Deafness** covering all of the
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


# Sinoatrial Node Dysfunction and Deafness (SANDD): Comprehensive Disease-Characteristics Report

## Executive summary and evidence scope

**Sinoatrial node dysfunction and deafness (SANDD)** is an ultra-rare, autosomal-recessive calcium-channelopathy caused by **biallelic loss-of-function variants in CACNA1D**, which encodes the pore-forming α1D subunit of the CaV1.3 L-type voltage-gated calcium channel. The defining manifestations are congenital sensorineural deafness and early-onset sinoatrial-node dysfunction, often accompanied by atrioventricular conduction disease. The strongest human evidence remains a small number of consanguineous families; therefore, prevalence, penetrance, long-term survival, quality-of-life, and treatment-response estimates are not available at population level. Open Targets maps only CACNA1D to this disease, supported principally by the original human study, PMID **21131953**. (OpenTargets Search: Sinoatrial node dysfunction and deafness-CACNA1D, torrente2020channelopathiesofvoltagegated pages 5-7)

This report distinguishes **classic SANDD—biallelic CACNA1D loss of function—from dominant/de novo CACNA1D disorders** caused by gain of function or transcript-dependent mixed effects. Those disorders may produce epilepsy, autism, developmental disability, primary aldosteronism, or hyperinsulinism and must not be merged with SANDD. (rinne2022wholeexomesequencing pages 2-4, rinne2022wholeexomesequencing pages 1-2, rinne2022wholeexomesequencing pages 9-11)

The following table provides a knowledge-base-oriented synopsis.

| Domain | Key finding | Suggested ontology/ID(s) | Evidence type | Citation |
|---|---|---|---|---|
| Disease identifier | Sinoatrial node dysfunction and deafness (SANDD); ultra-rare Mendelian channelopathy caused by CACNA1D loss of function; MONDO disease mapping available | MONDO:0013960; OMIM:614896 | Established human disease mapping | (OpenTargets Search: Sinoatrial node dysfunction and deafness-CACNA1D, torrente2020channelopathiesofvoltagegated pages 5-7) |
| Synonyms | SANDD; sino-atrial node dysfunction and deafness; sinus node dysfunction and deafness | MONDO:0013960 | Aggregated disease resource + literature | (OpenTargets Search: Sinoatrial node dysfunction and deafness-CACNA1D, mesirca2016rescuingcardiacautomaticity pages 1-2) |
| Causal gene | CACNA1D encodes CaV1.3/L-type voltage-gated calcium channel alpha1D, the only consistently implicated disease gene | HGNC:1392; Ensembl:ENSG00000157388 | Established human genetics | (OpenTargets Search: Sinoatrial node dysfunction and deafness-CACNA1D, torrente2020channelopathiesofvoltagegated pages 5-7) |
| Core molecular mechanism | Biallelic CACNA1D loss of function abolishes or markedly reduces CaV1.3-mediated inward Ca2+ current in sinoatrial/atrioventricular nodal cells and cochlear inner hair cells, impairing pacemaking and auditory transduction/development | GO:0005245 voltage-gated calcium channel activity; GO:0060048 cardiac muscle contraction?; GO:0086001 cardiac muscle cell action potential; GO:0006816 calcium ion transport | Human functional inference supported by model/heterologous data | (torrente2020channelopathiesofvoltagegated pages 7-9, torrente2020channelopathiesofvoltagegated pages 5-7, rinne2022wholeexomesequencing pages 1-2, torrente2020channelopathiesofvoltagegated pages 22-24) |
| Pathogenic variants | Recurrent SANDD variant reported as p.Gly403dup / p.403_404insGly / p.403-404InsGly (3-bp insertion in alternatively spliced exon 8B); another reported SANDD-associated missense variant p.Ala376Val | HGVS protein: p.Gly403dup; p.Ala376Val | Established human variant-level evidence | (torrente2020channelopathiesofvoltagegated pages 5-7, torrente2020channelopathiesofvoltagegated pages 7-9) |
| Variant effect | p.Gly403dup mutant channels traffic to plasma membrane but are electrically silent/non-conducting; likely uncouples gating from pore opening or sterically impairs ion permeation | GO:1901385 regulation of membrane depolarization? | Human mutation with in vitro functional evidence | (torrente2020channelopathiesofvoltagegated pages 7-9, torrente2020channelopathiesofvoltagegated pages 5-7) |
| Inheritance | Autosomal recessive / biallelic disease; heterozygous relatives reported as clinically unaffected in classic SANDD families | HP:0000007 Autosomal recessive inheritance | Established human pedigree evidence | (torrente2020channelopathiesofvoltagegated pages 7-9, torrente2020channelopathiesofvoltagegated pages 5-7) |
| Population / founder context | Reported in seven consanguineous Pakistani families from Khyber Pakhtunkhwa province; indicates strong founder/consanguinity contribution in known cases | HP:0003765 Increased consanguinity | Established human family-series evidence | (torrente2020channelopathiesofvoltagegated pages 5-7) |
| Epidemiology | No robust prevalence or incidence estimates identified; evidence limited to a handful of families/case reports | MONDO:0013960 | Evidence gap | (torrente2020channelopathiesofvoltagegated pages 5-7) |
| Cardiac phenotype | Severe sinus bradycardia, sinus node dysfunction, sinus pauses, SAN exit block, atrioventricular conduction disease ranging from 2nd-degree AV block to complete heart block; exercise-related dizziness/fatigue/syncope reported | HP:0001649 Bradycardia; HP:0001677 Cardiac syncope; HP:0011706 Second degree atrioventricular block; HP:0004762 Complete atrioventricular block | Established human clinical evidence | (torrente2020channelopathiesofvoltagegated pages 7-9) |
| Quantitative cardiac data | Reported daytime heart rates ~38-52 bpm and nocturnal heart rates below 35 bpm in homozygous affected individuals | HP:0001649 Bradycardia | Established human quantitative evidence | (torrente2020channelopathiesofvoltagegated pages 7-9) |
| Auditory phenotype | Congenital/profound sensorineural deafness or hearing loss is a defining feature of classic SANDD | HP:0000407 Sensorineural hearing impairment; HP:0008619 Congenital hearing impairment | Established human clinical evidence | (rinne2022wholeexomesequencing pages 2-4, rinne2022wholeexomesequencing pages 1-2) |
| Typical onset/course | Congenital or early-life onset for deafness; cardiac conduction disease present in childhood and appears chronic/lifelong rather than remitting | HP:0003577 Congenital onset | Human cases + inference from syndrome description | (rinne2022wholeexomesequencing pages 2-4, torrente2020channelopathiesofvoltagegated pages 7-9, rinne2022wholeexomesequencing pages 1-2) |
| Key affected organs | Heart conduction system and inner ear/cochlea are primary organs directly affected | UBERON:0000948 heart; UBERON:0001844 inner ear; UBERON:0001690 cochlea | Established from human and model evidence | (torrente2020channelopathiesofvoltagegated pages 7-9, rinne2022wholeexomesequencing pages 1-2, torrente2020channelopathiesofvoltagegated pages 22-24) |
| Key tissues/cells | Sinoatrial node pacemaker cells, atrioventricular nodal cells, cochlear inner hair cells | UBERON:0000079 sinoatrial node; UBERON:0000086 atrioventricular node; CL:0000586 hearing receptor cell; inner hair cell term not asserted with confidence | Human/mechanistic/model evidence | (mesirca2016rescuingcardiacautomaticity pages 3-5, torrente2020channelopathiesofvoltagegated pages 5-7, rinne2022wholeexomesequencing pages 1-2) |
| SAN electrophysiology | CaV1.3 activates at more negative voltages than CaV1.2 (about -45 mV vs -25 mV), contributing directly to diastolic depolarization; under beta-adrenergic stimulation threshold may extend to about -55 to -60 mV | GO:0086012 membrane depolarization during cardiac muscle cell action potential | Mechanistic evidence from experimental studies summarized in reviews | (torrente2020channelopathiesofvoltagegated pages 5-7, torrente2020channelopathiesofvoltagegated pages 9-11) |
| Upstream/downstream causal chain | CACNA1D LoF -> reduced nodal diastolic inward Ca2+ current and impaired RyR2/NCX-coupled pacemaker activity -> slowed SAN automaticity and AV conduction -> bradycardia, pauses, syncope; CACNA1D LoF in inner hair cells -> absent L-type Ca2+ signaling and arrested maturation/degeneration -> congenital deafness | GO:0006936 muscle contraction process not specific; GO:0001508 action potential; GO:0006816 calcium ion transport | Mechanistic synthesis from human, in vitro, and model evidence | (torrente2020channelopathiesofvoltagegated pages 7-9, torrente2020channelopathiesofvoltagegated pages 5-7, torrente2020channelopathiesofvoltagegated pages 9-11, torrente2020channelopathiesofvoltagegated pages 22-24) |
| Diagnostics: clinical | ECG/Holter monitoring for sinus bradycardia, pauses, SAN exit block, and AV block; audiologic testing for congenital sensorineural deafness; family history and consanguinity assessment are relevant | LOINC/ECG not asserted; HP:0001649; HP:0000407 | Established clinical practice inference from reported phenotypes | (torrente2020channelopathiesofvoltagegated pages 7-9, mesirca2016rescuingcardiacautomaticity pages 1-2) |
| Diagnostics: genetic | Priority testing methods: CACNA1D single-gene analysis if syndrome suspected; broader arrhythmia/deafness panels, WES/WGS if phenotype nonspecific; testing should distinguish recessive LoF SANDD from dominant CACNA1D gain-of-function neurodevelopmental syndromes | HGNC:1392; MONDO:0013960 | Expert/clinical inference anchored in known gene-disease relationship | (OpenTargets Search: Sinoatrial node dysfunction and deafness-CACNA1D, rinne2022wholeexomesequencing pages 2-4, rinne2022wholeexomesequencing pages 1-2) |
| Management | No disease-specific drug therapy established; symptomatic management centers on pacemaker implantation for clinically significant sinus node dysfunction/conduction disease; hearing rehabilitation may include hearing aids/cochlear implant based on audiology, though syndrome-specific outcome data are lacking | NCIT:C17754 Cardiac Pacemaker Implantation | Standard-of-care inference + SND review evidence | (mesirca2016rescuingcardiacautomaticity pages 1-2, torrente2020channelopathiesofvoltagegated pages 7-9) |
| Prognosis | Morbidity likely driven by chronic bradyarrhythmia/syncope and lifelong deafness; syndrome-specific survival, QoL, and natural-history statistics not identified | MONDO:0013960 | Evidence gap with cautious inference | (torrente2020channelopathiesofvoltagegated pages 7-9, mesirca2016rescuingcardiacautomaticity pages 1-2) |
| Distinction from other CACNA1D disorders | Classic SANDD is biallelic loss-of-function with deafness and nodal disease; distinct from heterozygous CACNA1D disorders such as dominant mixed LoF/GoF sinus node dysfunction with epilepsy (p.Arg930His) and de novo gain-of-function neurodevelopmental/endocrine syndromes, which may lack deafness | MONDO:0013960 | Established genotype-phenotype distinction | (rinne2022wholeexomesequencing pages 2-4, rinne2022wholeexomesequencing pages 1-2, rinne2022wholeexomesequencing pages 9-11, ortner2024iscav1.3a pages 6-6) |
| Animal model: global knockout | Cacna1d/CaV1.3-null mice recapitulate bradycardia, sinoatrial dysfunction, AV block, and deafness; useful for mechanism and therapeutic proof-of-concept | NCBITaxon:10090 | Established model-organism evidence | (mesirca2016rescuingcardiacautomaticity pages 3-5, torrente2020channelopathiesofvoltagegated pages 7-9, mesirca2016rescuingcardiacautomaticity pages 1-2, torrente2020channelopathiesofvoltagegated pages 22-24) |
| Quantitative model data | Global CaV1.3 knockout mice show ~60-70% reduction in SAN ICa,L density | GO:0005245 | Model quantitative evidence | (mesirca2016rescuingcardiacautomaticity pages 3-5) |
| Auditory model findings | Systemic and cochlea-specific Cacna1d deletion causes profound hearing loss; inner hair cells remain immature with absent BK upregulation and persistent SK2 expression; degeneration can occur in systemic null mice | GO:0042491 inner ear auditory receptor cell differentiation; GO:0005249 voltage-gated potassium channel activity | Established model evidence | (rinne2022wholeexomesequencing pages 1-2) |
| Experimental therapy signals | In mice, IKACh inhibition rescued bradycardia/automaticity in CaV1.3 channelopathy models; this is preclinical and not established for human SANDD | NCIT not asserted; GO:0005227 calcium-activated cation channel activity not specific | Model/preclinical evidence | (mesirca2016rescuingcardiacautomaticity pages 1-2, torrente2020channelopathiesofvoltagegated pages 9-11) |
| Recent developments (2023-2024) | Recent reviews emphasize CaV1.3 as a nodal-specific therapeutic target and summarize new CACNA1D variant models; 2024 isradipine work pertains to CACNA1D gain-of-function neurodevelopmental/endocrine disease, not SANDD loss of function | MONDO:0013960 | Recent expert analysis; indirect relevance | (ortner2024iscav1.3a pages 6-6) |
| Environmental / infectious factors | No convincing environmental, lifestyle, toxin, or infectious causes identified for classic SANDD; gene-environment and epigenetic modifiers remain unproven | Not applicable | Evidence gap | (torrente2020channelopathiesofvoltagegated pages 5-7, torrente2020channelopathiesofvoltagegated pages 7-9) |
| Data provenance | Information derives from aggregated disease/gene resources plus a very small number of human families and supporting in vitro/mouse studies, not EHR-scale cohorts | MONDO:0013960 | Evidence appraisal | (OpenTargets Search: Sinoatrial node dysfunction and deafness-CACNA1D, torrente2020channelopathiesofvoltagegated pages 5-7, mesirca2016rescuingcardiacautomaticity pages 1-2) |


*Table: This table condenses the most actionable disease-knowledge elements for Sinoatrial Node Dysfunction and Deafness, including identifiers, gene-mechanism links, phenotypes, models, and explicit evidence gaps. It is designed for direct knowledge-base extraction while separating established human evidence from model-supported inference.*

## 1. Disease information

### Definition and identifiers

SANDD is a congenital syndromic disorder linking failure of cardiac pacemaking with deafness. It is classified as a Mendelian channelopathy.

- **Preferred name:** Sinoatrial node dysfunction and deafness
- **Synonyms:** SANDD; SANDD syndrome; sinus node dysfunction and deafness; sino-atrial node dysfunction and deafness
- **MONDO:** **MONDO:0013960**
- **OMIM phenotype:** **614896**
- **Causal gene:** **CACNA1D**, Ensembl **ENSG00000157388**, encoding calcium voltage-gated channel subunit α1D/CaV1.3 (OpenTargets Search: Sinoatrial node dysfunction and deafness-CACNA1D, torrente2020channelopathiesofvoltagegated pages 5-7)
- **MeSH:** No disease-specific MeSH descriptor was identified; broader descriptors include *Sick Sinus Syndrome*, *Bradycardia*, and *Hearing Loss, Sensorineural*.
- **ICD-10/ICD-11:** No SANDD-specific code was identified. Component manifestations would ordinarily be coded separately—for example, sick sinus syndrome/conduction disease and congenital sensorineural hearing loss.
- **Orphanet:** No confidently verified disease-specific Orphanet identifier was recovered in the searched evidence; it should not be inferred from OMIM or MONDO.

### Data provenance

The evidence is **aggregated disease-level information derived from published pedigrees, functional expression studies, and animal models**, not an EHR-scale patient dataset. Seven consanguineous Pakistani families have been described in the literature synthesis, but detailed denominators and standardized phenotype frequencies are unavailable. (torrente2020channelopathiesofvoltagegated pages 5-7)

## 2. Etiology, risk, and protective factors

### Causal factor

The primary cause is **germline biallelic CACNA1D loss of function**. The best-characterized recurrent lesion is a three-base-pair insertion in alternatively spliced exon 8B, variously reported as **p.Gly403dup**, **p.403_404insGly**, or **p.403-404InsGly**. The mutant protein reaches the plasma membrane but generates no functional Ca²⁺ current, indicating a channel-conduction/gating defect rather than simple trafficking failure. A second reported SANDD-associated missense variant is **p.Ala376Val**. (rinne2022wholeexomesequencing pages 9-11, torrente2020channelopathiesofvoltagegated pages 7-9, torrente2020channelopathiesofvoltagegated pages 5-7)

### Risk factors

- **Genetic:** Homozygosity or compound biallelic pathogenic CACNA1D loss-of-function variants is the principal risk. Heterozygous relatives in the classic pedigrees were clinically unaffected, supporting recessive inheritance. (torrente2020channelopathiesofvoltagegated pages 7-9)
- **Family structure:** Consanguinity and ancestry from a founder population are important ascertainment/risk factors in the known families. The recurrent insertion has been reported across seven consanguineous families from Khyber Pakhtunkhwa, Pakistan. (torrente2020channelopathiesofvoltagegated pages 5-7)
- **Environmental, infectious, occupational, lifestyle, age, or sex risks:** None are established for occurrence of this congenital Mendelian disorder.
- **Modifiers:** No validated modifier genes are known. Variable cardiac severity could plausibly reflect other pacemaker-current genes, autonomic tone, medications, or epigenetic background, but this remains unproven for SANDD.

### Protective factors and gene–environment interactions

No protective allele, diet, exposure, medication, or lifestyle intervention has been shown to prevent SANDD. Avoidance of drugs that further depress sinoatrial or atrioventricular conduction is clinically prudent but is tertiary risk management, not primary prevention. No SANDD-specific gene–environment interaction has been demonstrated.

## 3. Phenotypes

### Core phenotype profile

1. **Congenital sensorineural hearing impairment/deafness**—a defining, generally severe-to-profound phenotype. Suggested terms: **HP:0000407 Sensorineural hearing impairment**, **HP:0008619 Congenital hearing impairment**. Mouse and human evidence localizes the defect to CaV1.3-dependent cochlear inner-hair-cell physiology. (rinne2022wholeexomesequencing pages 2-4, rinne2022wholeexomesequencing pages 1-2)
2. **Sinus bradycardia/sinoatrial-node dysfunction**—reported daytime rates were approximately **38–52 beats/min**, falling below **35 beats/min at night** in affected homozygotes. Suggested terms: **HP:0001649 Bradycardia** and a suitable HPO term for sick sinus syndrome/sinus-node dysfunction. (torrente2020channelopathiesofvoltagegated pages 7-9)
3. **Sinus pauses and sinoatrial exit block**—episodic manifestations superimposed on chronic bradycardia. (torrente2020channelopathiesofvoltagegated pages 7-9)
4. **Atrioventricular conduction disease**—severity ranges from second-degree AV block to complete heart block. Suggested terms: **HP:0011706 Second-degree atrioventricular block** and **HP:0004762 Complete atrioventricular block**. (torrente2020channelopathiesofvoltagegated pages 7-9)
5. **Exercise intolerance, dizziness, fatigue, and syncope**—downstream symptoms of bradycardia and chronotropic incompetence; exercise-associated syncope was reported. Suggested terms include **HP:0001279 Syncope**, fatigue, dizziness, and exercise intolerance. (torrente2020channelopathiesofvoltagegated pages 7-9)

Precise percentages cannot be responsibly assigned because published evidence lacks a complete standardized denominator. Congenital deafness and sinus-node disease define classic SANDD, whereas AV block and symptomatic syncope vary in severity.

### Onset, severity, progression, and quality of life

Deafness is congenital. Cardiac disease is congenital or recognized in childhood and appears chronic, with variable severity and episodic pauses/syncope. There is no evidence for spontaneous remission. Deafness affects communication and education, while bradycardia, syncope, and exercise intolerance restrict physical activity and create injury risk. No SANDD-specific EQ-5D, SF-36, PROMIS, or hearing-related quality-of-life study was identified.

## 4. Genetic and molecular information

### Gene and protein

**CACNA1D** encodes CaV1.3, an L-type voltage-gated calcium-channel α1 subunit. CaV1.3 is particularly important in adult atrial, sinoatrial, and atrioventricular nodal tissue and in cochlear inner hair cells. (mesirca2016rescuingcardiacautomaticity pages 3-5, rinne2022wholeexomesequencing pages 1-2)

### Variant interpretation

- **p.Gly403dup/p.403_404insGly:** homozygous germline in affected families; three-base-pair in-frame insertion; functionally electrically silent despite membrane localization. This constitutes strong pathogenic evidence from segregation, phenotype specificity, and functional assay. (torrente2020channelopathiesofvoltagegated pages 7-9, torrente2020channelopathiesofvoltagegated pages 5-7)
- **p.Ala376Val:** reported in another family with the same SANDD phenotype, but the retrieved evidence provides less detailed segregation and functional information than for p.Gly403dup. (rinne2022wholeexomesequencing pages 9-11, torrente2020channelopathiesofvoltagegated pages 7-9)

Current ClinVar classifications and exact gnomAD allele counts were not recovered and should be checked against the current transcript and genome build before database ingestion. The recurrent variant’s multiple protein descriptions also require HGVS normalization against the selected CACNA1D transcript. The disease alleles are **germline**, not somatic.

No established chromosomal rearrangement, copy-number syndrome, repeat expansion, mitochondrial variant, modifier gene, or disease-specific epigenetic signature is known. No anticipation or germline mosaicism has been reported. Carrier frequency cannot be calculated from the family reports.

### Important allelic distinction

A heterozygous **p.Arg930His** CACNA1D variant was reported in an autosomal-dominant family with sinus-node dysfunction, epilepsy, learning problems, and ADHD but not classic congenital deafness. It produced gain of function in the short, brain-enriched isoform and loss of function in the long isoform. This is mechanistically and clinically distinct from recessive SANDD. (rinne2022wholeexomesequencing pages 2-4, rinne2022wholeexomesequencing pages 1-2, rinne2022wholeexomesequencing pages 11-12)

## 5. Environmental information

No toxin, radiation exposure, pollutant, occupation, diet, smoking pattern, alcohol use, or infectious agent is known to cause classic SANDD. Such factors can independently worsen acquired bradyarrhythmia or hearing loss, but there is no evidence that they initiate the CACNA1D syndrome. Consequently, environmental and infectious-agent fields should be populated as **not established/not applicable**, rather than as negative causal claims.

## 6. Mechanism and pathophysiology

### Cardiac causal chain

**Upstream:** biallelic CACNA1D loss of function → absent or markedly reduced CaV1.3-mediated L-type Ca²⁺ current.

**Cellular:** CaV1.3 normally activates at more negative voltages than CaV1.2—approximately **−45 mV versus −25 mV**—allowing it to contribute during diastolic depolarization of sinoatrial pacemaker cells. Under β-adrenergic activation, relevant CaV1.3 activity can extend to approximately −55 to −60 mV. CaV1.3 also supports RyR2-dependent local Ca²⁺ release and NCX-mediated inward current and contributes to sustained inward current. (torrente2020channelopathiesofvoltagegated pages 5-7, torrente2020channelopathiesofvoltagegated pages 9-11)

**Downstream:** reduced diastolic inward current and impaired Ca²⁺-clock/membrane-clock coupling → slowed spontaneous pacemaker depolarization → sinus bradycardia, pauses, exit block, and chronotropic incompetence. Loss of CaV1.3 in atrioventricular nodal cells similarly slows or blocks conduction. In global knockout mice, SAN L-type current density is reduced by approximately **60–70%**. (mesirca2016rescuingcardiacautomaticity pages 3-5, torrente2020channelopathiesofvoltagegated pages 22-24)

Suggested GO annotations include **GO:0005245 voltage-gated calcium-channel activity**, **GO:0006816 calcium-ion transport**, cardiac action-potential regulation, membrane depolarization, regulation of heart rate, and calcium-dependent exocytosis.

### Auditory causal chain

CACNA1D loss → failure of CaV1.3-mediated Ca²⁺ entry in cochlear inner hair cells → impaired presynaptic ribbon-synapse transmitter release and abnormal pre-hearing Ca²⁺ action potentials/gene-expression programs → arrested inner-hair-cell maturation, altered BK/SK2 channel expression, and eventual hair-cell degeneration → congenital severe-to-profound sensorineural deafness. (rinne2022wholeexomesequencing pages 1-2)

Suggested cells and processes are **CL:0000586 hearing receptor cell**, cochlear inner hair cell, sensory perception of sound, inner-ear receptor-cell differentiation, calcium-dependent exocytosis, and ribbon-synapse transmission.

### Other mechanistic domains

No SANDD-specific immune, inflammatory, fibrotic, metabolic, lipidomic, metabolomic, proteomic, single-cell, spatial-transcriptomic, or epigenomic signature has been established. The primary abnormality is an ion-channel conduction defect, not inflammation or energy-metabolism failure.

## 7. Anatomical structures affected

- **Heart/conduction system:** heart (**UBERON:0000948**), sinoatrial node, atrioventricular node, atrial conduction tissue; principal cells are specialized nodal pacemaker/conduction cardiomyocytes. (mesirca2016rescuingcardiacautomaticity pages 3-5, rinne2022wholeexomesequencing pages 1-2)
- **Inner ear:** inner ear (**UBERON:0001844**), cochlea (**UBERON:0001690**), organ of Corti, and especially bilateral cochlear inner hair cells and their ribbon synapses. (rinne2022wholeexomesequencing pages 1-2)
- **Subcellular localization:** CaV1.3 resides in the plasma membrane; disease-relevant signaling also involves presynaptic active zones/ribbon synapses, sarcolemmal ion-channel complexes, sarcoplasmic-reticulum RyR2 release sites, and NCX-containing membrane microdomains.
- **Lateralization:** Hearing loss is expected to be bilateral; no consistent cardiac anatomical lateralization applies.

## 8. Temporal development

The auditory phenotype begins prenatally or at birth, reflecting developmental failure of inner-hair-cell function and maturation. Cardiac bradyarrhythmia is congenital/childhood-onset and chronic. Severity can fluctuate with sleep, exercise, autonomic state, and intermittent conduction block; the documented lower nocturnal heart rates illustrate physiologic modulation of an underlying fixed channel defect. (torrente2020channelopathiesofvoltagegated pages 7-9)

No validated staging system exists. A practical clinical sequence is: congenital deafness and baseline bradycardia → recognition of pauses/chronotropic incompetence or AV block → symptomatic dizziness, exercise intolerance, or syncope → pacemaker consideration. Disease duration is lifelong, and no spontaneous remission window is documented.

## 9. Inheritance and population

Inheritance is **autosomal recessive**. Heterozygous relatives in classic families were reported as phenotypically normal, suggesting that one functional allele is usually sufficient, although formal lifelong penetrance studies are unavailable. (torrente2020channelopathiesofvoltagegated pages 7-9)

The recurrent variant was found in seven consanguineous families from Khyber Pakhtunkhwa, Pakistan, consistent with a founder effect or geographically concentrated allele. No unbiased prevalence, incidence, carrier-frequency, sex-ratio, or age-distribution estimate exists. There is no evidence of sex-limited expression, anticipation, or a broad endemic distribution. (torrente2020channelopathiesofvoltagegated pages 5-7)

For counseling, when both parents are confirmed heterozygous carriers, each pregnancy has the standard autosomal-recessive probabilities: **25% affected, 50% carrier, and 25% unaffected/non-carrier**.

## 10. Diagnostics

### Clinical evaluation

1. **Cardiac:** resting 12-lead ECG; prolonged Holter/event monitoring to quantify minimum and mean heart rates, sinus pauses, exit block, and AV block; exercise testing for chronotropic incompetence; echocardiography to evaluate structural heart disease and alternative causes. Electrophysiology study may be considered when noninvasive findings are inconclusive.
2. **Audiology:** newborn or diagnostic auditory brainstem response, otoacoustic emissions, pure-tone audiometry when developmentally appropriate, tympanometry, speech testing, and assessment for cochlear implantation.
3. **Laboratory exclusion:** electrolytes, thyroid function, medication review, and other tests directed at acquired bradycardia; these do not diagnose SANDD.

### Genetic testing strategy

- When congenital bilateral sensorineural deafness co-occurs with marked sinus bradycardia or AV block, perform **CACNA1D sequencing with deletion/duplication analysis** or a combined hearing-loss/arrhythmia panel.
- WES or WGS is appropriate when the phenotype is atypical, panel testing is negative, or a second diagnosis is possible. WES identified a distinct dominant CACNA1D syndrome in a sinus-node-dysfunction cohort, illustrating the value of broad testing but also the need for mechanism-specific interpretation. (rinne2022wholeexomesequencing pages 2-4, rinne2022wholeexomesequencing pages 1-2)
- Confirm phase and segregation by parental testing. A molecular diagnosis of recessive SANDD requires two pathogenic/likely pathogenic loss-of-function alleles in trans plus compatible phenotype.
- CMA, karyotype, FISH, mitochondrial testing, repeat-expansion testing, RNA sequencing, proteomics, metabolomics, and liquid biopsy are not first-line unless another diagnosis is suspected.

### Differential diagnosis

Important alternatives include isolated congenital deafness plus unrelated bradycardia; **Jervell and Lange-Nielsen syndrome** (biallelic KCNQ1/KCNE1, deafness with prolonged QT); HCN4-related sinus-node disease; SCN5A-related conduction disease; LMNA-related conduction/cardiomyopathy; mitochondrial deafness syndromes; and dominant CACNA1D neurodevelopmental/endocrine channelopathy. The ECG QT interval, neurologic/endocrine phenotype, inheritance, and molecular findings distinguish these conditions. CACNA1D’s recessive-versus-dominant allelic spectrum is analogous to other channel genes in which dosage and functional direction determine phenotype. (rinne2022wholeexomesequencing pages 9-11)

Cascade testing of relatives is appropriate; universal population or newborn genomic screening for SANDD is not established.

## 11. Outcome and prognosis

No disease-specific 5- or 10-year survival, mortality, life-expectancy, hospitalization, or quality-of-life estimates exist. Likely major morbidities are recurrent syncope/injury, exercise limitation, progression of conduction disease, pacemaker dependence, and lifelong communication disability. Atrial fibrillation was inducible in Cacna1d-null mice but was not reported in the summarized human SANDD cases, so it should not be coded as an established human feature. (torrente2020channelopathiesofvoltagegated pages 7-9)

Prognosis is expected to improve substantially with recognition and treatment of clinically important bradyarrhythmia and with early hearing rehabilitation, but syndrome-specific response rates are unavailable. Severity of bradycardia, pause duration, high-grade AV block, syncope, and failure of heart rate to rise with exercise are clinically relevant risk indicators; no molecular prognostic biomarker beyond causal genotype has been validated.

## 12. Treatment

### Current real-world management

- **Permanent cardiac pacemaker:** standard definitive therapy for symptomatic sinus-node dysfunction, clinically consequential pauses, chronotropic incompetence, or advanced AV block. This treats the electrical consequence but does not restore CACNA1D function or hearing. Suggested NCIT concept: cardiac pacemaker implantation. Reviews emphasize that current SND management is primarily symptomatic and that electronic pacing remains the established intervention. (mesirca2016rescuingcardiacautomaticity pages 1-2)
- **Acute symptomatic bradycardia:** managed under standard resuscitation/cardiology protocols; atropine or temporary pacing may be used according to clinical context, but no SANDD-specific evidence exists.
- **Hearing care:** early audiology, hearing devices when residual function permits, cochlear-implant evaluation for severe/profound loss, speech-language therapy, educational accommodations, and communication support. Syndrome-specific cochlear-implant outcomes have not been published in the recovered literature.
- **Medication review:** avoid or carefully supervise drugs that further slow sinus or AV nodal function.

### Experimental and precision approaches

In Cacna1d-null mice, inhibition of the acetylcholine-activated potassium current **IKACh**—including experimental inhibitors such as tertiapin-Q—restored a more favorable inward/outward current balance and rescued bradycardia. This is preclinical proof of concept, not approved SANDD treatment. (mesirca2016rescuingcardiacautomaticity pages 1-2, torrente2020channelopathiesofvoltagegated pages 9-11)

No SANDD-specific gene therapy, RNA therapy, CRISPR trial, cell therapy, or registered interventional clinical trial was identified. CaV1.3 blockers such as isradipine are being explored for **gain-of-function** CACNA1D neurodevelopmental/endocrine disease; blocking an already loss-of-function channel is not a rational SANDD treatment. In 2024 expert analysis, isradipine benefit was discussed in a gain-of-function mouse model, whereas human CaV1.3 loss of function remained a distinct bradycardia-deafness syndrome. (ortner2024iscav1.3a pages 6-6)

## 13. Prevention

Primary prevention by lifestyle modification, vaccination, or prophylactic medication is not possible for a germline recessive channelopathy. Relevant measures are:

- **Genetic counseling and carrier testing** in affected families.
- **Reproductive options:** prenatal diagnosis or preimplantation genetic testing when familial variants are known.
- **Secondary prevention:** newborn hearing screening, early ECG/Holter evaluation in at-risk children, and cascade genetic testing.
- **Tertiary prevention:** timely pacing to prevent bradycardic syncope and high-grade block; early hearing intervention to reduce language and educational consequences; avoidance of conduction-slowing drugs when possible.

There is no applicable vaccine, infectious prophylaxis, or population-wide public-health screening program specific to SANDD.

## 14. Other species and natural disease

No naturally occurring veterinary SANDD syndrome or breed-associated CACNA1D disorder was identified. The principal comparative species is the laboratory mouse, **Mus musculus (NCBI Taxonomy 10090)**, with ortholog **Cacna1d**. The cardiac and cochlear functions of CaV1.3 are evolutionarily conserved, but existing mouse disease is experimentally engineered rather than naturally occurring. There is no infectious transmission or zoonotic potential.

## 15. Model organisms and experimental systems

### Mouse models

**Global Cacna1d/CaV1.3 knockout mice** reproduce major human features: bradycardia, sinoatrial dysfunction, AV block, and deafness. SAN L-type Ca²⁺ current is reduced by approximately 60–70%, making this a strong mechanistic model for membrane-clock/Ca²⁺-clock coupling and for preclinical pacemaker-current interventions. (mesirca2016rescuingcardiacautomaticity pages 3-5, torrente2020channelopathiesofvoltagegated pages 7-9, torrente2020channelopathiesofvoltagegated pages 22-24)

**Cochlea-specific Cacna1d deletion** produces profound hearing loss, absent normal BK-channel upregulation, persistence of immature SK2 expression, and arrested inner-hair-cell differentiation. This demonstrates a cochlea-autonomous requirement for CaV1.3, although complex Cre/reporter constructs can themselves alter expression or cause GFP toxicity and therefore require careful controls. (rinne2022wholeexomesequencing pages 1-2)

### In-vitro systems

Heterologous channel-expression and patch-clamp studies show that the recurrent p.Gly403dup protein reaches the cell surface but produces no measurable Ca²⁺ current. These assays provide direct evidence of loss of channel conductance but do not reproduce the multicellular architecture or autonomic regulation of the SAN and cochlea. (torrente2020channelopathiesofvoltagegated pages 7-9, torrente2020channelopathiesofvoltagegated pages 5-7)

No validated SANDD patient-derived iPSC pacemaker-cell model, cochlear organoid, large-animal model, CRISPR screen, or disease-specific multi-omics model was identified in the retrieved evidence.

## Recent developments and expert assessment, 2023–2024

Recent cardiac reviews continue to identify CaV1.3 as unusually attractive for nodal-selective mechanistic study because adult cardiac expression is concentrated in atrial and nodal tissue rather than being ubiquitous across ventricular myocardium. Nonetheless, therapeutic work in 2023–2024 has focused more heavily on **CACNA1D gain-of-function neurodevelopmental disease** than on SANDD. The emerging expert consensus is therefore that molecular direction matters: CaV1.3 inhibition may be relevant to gain-of-function disease, whereas SANDD requires restoration or compensation of deficient pacemaker and cochlear signaling. (ortner2024iscav1.3a pages 6-6)

The most mature SANDD-relevant translational idea remains **compensatory ion-channel targeting**, exemplified by IKACh inhibition in knockout mice. Gene replacement or editing is conceptually attractive but faces the challenge of delivering therapy to two specialized targets—cardiac nodal cells and cochlear inner hair cells—potentially during different developmental windows. (mesirca2016rescuingcardiacautomaticity pages 1-2, torrente2020channelopathiesofvoltagegated pages 9-11)

## Key sources, dates, and URLs

1. **Baig et al.** “Loss of CaV1.3 (CACNA1D) function in a human channelopathy with bradycardia and congenital deafness.” *Nature Neuroscience*. Published December 2010/January 2011 issue. PMID **21131953**. DOI: https://doi.org/10.1038/nn.2694. This is the landmark primary human report underlying the disease association. (OpenTargets Search: Sinoatrial node dysfunction and deafness-CACNA1D)
2. **Torrente et al.** “Channelopathies of voltage-gated L-type CaV1.3/α1D and T-type CaV3.1/α1G Ca²⁺ channels in dysfunction of heart automaticity.” *Pflügers Archiv*. Published June 2020. DOI: https://doi.org/10.1007/s00424-020-02421-1. (torrente2020channelopathiesofvoltagegated pages 5-7, torrente2020channelopathiesofvoltagegated pages 7-9)
3. **Mesirca et al.** “Rescuing cardiac automaticity in L-type CaV1.3 channelopathies and beyond.” *Journal of Physiology*. Published October 2016. DOI: https://doi.org/10.1113/JP270678. (mesirca2016rescuingcardiacautomaticity pages 3-5, mesirca2016rescuingcardiacautomaticity pages 1-2)
4. **Rinné et al.** “Whole Exome Sequencing Identifies a Heterozygous Variant in the CaV1.3 Gene CACNA1D Associated with Familial Sinus Node Dysfunction and Focal Idiopathic Epilepsy.” *International Journal of Molecular Sciences*. Published November 2022. DOI: https://doi.org/10.3390/ijms232214215. Its abstract states: “So far, homozygous loss of function mutations in CACNA1D encoding the CaV1.3 α1-subunit are described in congenital sinus node dysfunction and deafness.” This source is especially useful for separating classic SANDD from dominant mixed-effect disease. (rinne2022wholeexomesequencing pages 2-4, rinne2022wholeexomesequencing pages 1-2)
5. **Ortner.** “Is CaV1.3 a feasible therapeutic target for a rare neurodevelopmental disorder?” *Expert Opinion on Therapeutic Targets*. Published December 2024. DOI: https://doi.org/10.1080/14728222.2024.2442428. This is authoritative recent analysis but pertains primarily to CACNA1D gain-of-function disease, not SANDD therapy. (ortner2024iscav1.3a pages 6-6)

## Evidence limitations

SANDD has not been characterized through registries, prospective natural-history cohorts, randomized trials, or population screening. Consequently, disease prevalence, incidence, exact phenotype frequencies, penetrance by age, carrier frequency, sex ratio, survival, mortality, quality-of-life scores, cochlear-implant outcomes, and genotype-specific prognosis remain unknown. Database fields for those domains should be marked **“not available—ultra-rare family-level evidence”**, not zero. The most secure knowledge-base assertions are the MONDO/OMIM mapping, recessive CACNA1D loss-of-function mechanism, congenital deafness, severe sinus bradycardia with possible AV block, and recapitulation in Cacna1d-null mice. (OpenTargets Search: Sinoatrial node dysfunction and deafness-CACNA1D, torrente2020channelopathiesofvoltagegated pages 5-7, torrente2020channelopathiesofvoltagegated pages 7-9)

References

1. (OpenTargets Search: Sinoatrial node dysfunction and deafness-CACNA1D): Open Targets Query (Sinoatrial node dysfunction and deafness-CACNA1D, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (torrente2020channelopathiesofvoltagegated pages 5-7): Angelo G. Torrente, Pietro Mesirca, Isabelle Bidaud, and Matteo E. Mangoni. Channelopathies of voltage-gated l-type cav1.3/α1d and t-type cav3.1/α1g ca2+ channels in dysfunction of heart automaticity. Pflügers Archiv - European Journal of Physiology, 472:817-830, Jun 2020. URL: https://doi.org/10.1007/s00424-020-02421-1, doi:10.1007/s00424-020-02421-1. This article has 32 citations.

3. (rinne2022wholeexomesequencing pages 2-4): Susanne Rinné, Birgit Stallmeyer, Alexandra Pinggera, Michael F. Netter, Lina A. Matschke, Sven Dittmann, Uwe Kirchhefer, Ulrich Neudorf, Joachim Opp, Jörg Striessnig, Niels Decher, and Eric Schulze-Bahr. Whole exome sequencing identifies a heterozygous variant in the cav1.3 gene cacna1d associated with familial sinus node dysfunction and focal idiopathic epilepsy. International Journal of Molecular Sciences, 23:14215, Nov 2022. URL: https://doi.org/10.3390/ijms232214215, doi:10.3390/ijms232214215. This article has 22 citations.

4. (rinne2022wholeexomesequencing pages 1-2): Susanne Rinné, Birgit Stallmeyer, Alexandra Pinggera, Michael F. Netter, Lina A. Matschke, Sven Dittmann, Uwe Kirchhefer, Ulrich Neudorf, Joachim Opp, Jörg Striessnig, Niels Decher, and Eric Schulze-Bahr. Whole exome sequencing identifies a heterozygous variant in the cav1.3 gene cacna1d associated with familial sinus node dysfunction and focal idiopathic epilepsy. International Journal of Molecular Sciences, 23:14215, Nov 2022. URL: https://doi.org/10.3390/ijms232214215, doi:10.3390/ijms232214215. This article has 22 citations.

5. (rinne2022wholeexomesequencing pages 9-11): Susanne Rinné, Birgit Stallmeyer, Alexandra Pinggera, Michael F. Netter, Lina A. Matschke, Sven Dittmann, Uwe Kirchhefer, Ulrich Neudorf, Joachim Opp, Jörg Striessnig, Niels Decher, and Eric Schulze-Bahr. Whole exome sequencing identifies a heterozygous variant in the cav1.3 gene cacna1d associated with familial sinus node dysfunction and focal idiopathic epilepsy. International Journal of Molecular Sciences, 23:14215, Nov 2022. URL: https://doi.org/10.3390/ijms232214215, doi:10.3390/ijms232214215. This article has 22 citations.

6. (mesirca2016rescuingcardiacautomaticity pages 1-2): Pietro Mesirca, Isabelle Bidaud, and Matteo E. Mangoni. Rescuing cardiac automaticity in l‐type cav1.3 channelopathies and beyond. The Journal of Physiology, 594:5869-5879, Oct 2016. URL: https://doi.org/10.1113/jp270678, doi:10.1113/jp270678. This article has 31 citations.

7. (torrente2020channelopathiesofvoltagegated pages 7-9): Angelo G. Torrente, Pietro Mesirca, Isabelle Bidaud, and Matteo E. Mangoni. Channelopathies of voltage-gated l-type cav1.3/α1d and t-type cav3.1/α1g ca2+ channels in dysfunction of heart automaticity. Pflügers Archiv - European Journal of Physiology, 472:817-830, Jun 2020. URL: https://doi.org/10.1007/s00424-020-02421-1, doi:10.1007/s00424-020-02421-1. This article has 32 citations.

8. (torrente2020channelopathiesofvoltagegated pages 22-24): Angelo G. Torrente, Pietro Mesirca, Isabelle Bidaud, and Matteo E. Mangoni. Channelopathies of voltage-gated l-type cav1.3/α1d and t-type cav3.1/α1g ca2+ channels in dysfunction of heart automaticity. Pflügers Archiv - European Journal of Physiology, 472:817-830, Jun 2020. URL: https://doi.org/10.1007/s00424-020-02421-1, doi:10.1007/s00424-020-02421-1. This article has 32 citations.

9. (mesirca2016rescuingcardiacautomaticity pages 3-5): Pietro Mesirca, Isabelle Bidaud, and Matteo E. Mangoni. Rescuing cardiac automaticity in l‐type cav1.3 channelopathies and beyond. The Journal of Physiology, 594:5869-5879, Oct 2016. URL: https://doi.org/10.1113/jp270678, doi:10.1113/jp270678. This article has 31 citations.

10. (torrente2020channelopathiesofvoltagegated pages 9-11): Angelo G. Torrente, Pietro Mesirca, Isabelle Bidaud, and Matteo E. Mangoni. Channelopathies of voltage-gated l-type cav1.3/α1d and t-type cav3.1/α1g ca2+ channels in dysfunction of heart automaticity. Pflügers Archiv - European Journal of Physiology, 472:817-830, Jun 2020. URL: https://doi.org/10.1007/s00424-020-02421-1, doi:10.1007/s00424-020-02421-1. This article has 32 citations.

11. (ortner2024iscav1.3a pages 6-6): Nadine J. Ortner. Is cav1.3 a feasible therapeutic target for a rare neurodevelopmental disorder? Expert Opinion on Therapeutic Targets, 28:1021-1025, Dec 2024. URL: https://doi.org/10.1080/14728222.2024.2442428, doi:10.1080/14728222.2024.2442428. This article has 0 citations and is from a peer-reviewed journal.

12. (rinne2022wholeexomesequencing pages 11-12): Susanne Rinné, Birgit Stallmeyer, Alexandra Pinggera, Michael F. Netter, Lina A. Matschke, Sven Dittmann, Uwe Kirchhefer, Ulrich Neudorf, Joachim Opp, Jörg Striessnig, Niels Decher, and Eric Schulze-Bahr. Whole exome sequencing identifies a heterozygous variant in the cav1.3 gene cacna1d associated with familial sinus node dysfunction and focal idiopathic epilepsy. International Journal of Molecular Sciences, 23:14215, Nov 2022. URL: https://doi.org/10.3390/ijms232214215, doi:10.3390/ijms232214215. This article has 22 citations.

## Artifacts

- [Edison artifact artifact-00](Sinoatrial_Node_Dysfunction_and_Deafness-deep-research-falcon_artifacts/artifact-00.md)