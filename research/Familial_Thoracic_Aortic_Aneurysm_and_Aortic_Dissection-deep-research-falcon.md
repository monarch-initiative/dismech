---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-05T11:40:56.097366'
end_time: '2026-05-05T11:54:04.952205'
duration_seconds: 788.85
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Familial Thoracic Aortic Aneurysm and Aortic Dissection
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

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Familial Thoracic Aortic Aneurysm and Aortic Dissection
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Familial Thoracic Aortic Aneurysm and Aortic Dissection** covering all of the
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

For each treatment, suggest MAXO (Medical Action Ontology) terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, MAXO, MONDO) where applicable
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
- Treatment annotations (MAXO terms)
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
- **Disease Name:** Familial Thoracic Aortic Aneurysm and Aortic Dissection
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Familial Thoracic Aortic Aneurysm and Aortic Dissection** covering all of the
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

For each treatment, suggest MAXO (Medical Action Ontology) terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, MAXO, MONDO) where applicable
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
- Treatment annotations (MAXO terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


# Comprehensive Research Report: Familial Thoracic Aortic Aneurysm and Aortic Dissection (FTAAD) / Heritable Thoracic Aortic Disease (HTAD)

## Target Disease
- **Disease name (requested):** Familial Thoracic Aortic Aneurysm and Aortic Dissection (FTAAD)
- **Category:** Mendelian (typically autosomal dominant, reduced penetrance)
- **MONDO ID:** **MONDO:0019625** (familial thoracic aortic aneurysm and aortic dissection) (isselbacher20222022accahaguideline pages 23-24)

## Executive summary
Familial thoracic aortic aneurysm and dissection (FTAAD) is a non-syndromic form within the broader umbrella of **heritable thoracic aortic disease (HTAD)**, characterized by predisposition to thoracic aortic aneurysm (TAA) and acute aortic dissection, commonly involving the **aortic root and ascending aorta**. Contemporary guidance emphasizes: (i) multigenerational family history, (ii) multigene panel testing for high-penetrance HTAD genes, (iii) cascade genetic testing and aortic imaging of at-risk relatives, and (iv) gene-informed management and prophylactic surgery decisions (isselbacher20222022accahaguideline pages 23-24).

---

## 1. Disease Information
### 1.1 Concise overview / definition
- **HTAD definition (used clinically to encompass FTAAD):** HTAD comprises disorders characterized by “aortic events, mainly represented by aneurysm or dissection,” usually involving the **ascending aorta**; disease may be **non-syndromic** (limited to aorta) or **syndromic** (extra-aortic features) (monda2023theroleof pages 1-3).
- **Familial/non-syndromic component:** 20–25% of patients with non-syndromic HTAD exhibit a family history of aortic disease, requiring evaluation of first-degree relatives to distinguish familial from sporadic cases (monda2023theroleof pages 1-3, butnariu2024identificationofgenetic pages 2-4).

### 1.2 Key identifiers (available in retrieved evidence)
- **MONDO:** MONDO:0019625 (familial thoracic aortic aneurysm and aortic dissection) (isselbacher20222022accahaguideline pages 23-24)
- Related MONDO familial-thoracic-aortic-aneurysm entities observed in Open Targets snapshot:
  - **MONDO:0012730** (aortic aneurysm, familial thoracic 6; ACTA2-related) (isselbacher20222022accahaguideline pages 23-24)
  - **MONDO:0007568** (aortic aneurysm, familial thoracic 4; MYH11-related) (isselbacher20222022accahaguideline pages 23-24)
  - **MONDO:0013418** (aortic aneurysm, familial thoracic 7; MYLK-related) (isselbacher20222022accahaguideline pages 23-24)

**Not retrieved in the current document set:** OMIM disease-number(s), Orphanet ID, ICD-10/ICD-11, and MeSH terms specific to “familial thoracic aortic aneurysm and dissection.” (These typically exist but were not present in the tool-retrieved excerpts; see limitations.)

### 1.3 Common synonyms / alternative names
- **Heritable thoracic aortic disease (HTAD)** (monda2023theroleof pages 1-3, isselbacher20222022accahaguideline pages 23-24)
- **Genetically triggered thoracic aortic disease** (used in clinical review context) (duarte2023geneticallytriggeredthoracic pages 1-3)
- **Non-syndromic heritable thoracic aortic aneurysm/dissection (ns-TAAD / ns-HTAD)** (levy2024currentunderstandingof pages 1-3, levy2024currentunderstandingof pages 3-5)

### 1.4 Evidence type / provenance
- **Aggregated disease-level resources and expert consensus:** 2022 ACC/AHA guideline (JACC; published Oct 2022; https://doi.org/10.1016/j.jacc.2022.08.004) (isselbacher20222022accahaguideline pages 23-24)
- **Peer-reviewed narrative reviews (2023–2024):** clinical genetics/testing and phenotype summaries (monda2023theroleof pages 1-3, duarte2023geneticallytriggeredthoracic pages 1-3, spaziani2024hereditarythoracicaortic pages 1-2)
- **Human cohort sequencing evidence (2024):** deep sequencing study in nonsyndromic adults (chen2024contributionsofgermline pages 1-2)

---

## 2. Etiology
### 2.1 Disease causal factors
**Primary cause:** germline pathogenic variants affecting aortic wall integrity pathways, with additional contribution from non-genetic risk factors.
- The 2022 ACC/AHA guideline identifies a pathogenic variant in genes predisposing to thoracic aortic disease as a “major risk factor” and recommends genetic testing for patients with aortic root/ascending aneurysm or dissection plus HTAD risk factors (Table 8/Figure 17 referenced) (isselbacher20222022accahaguideline pages 23-24).

### 2.2 Risk factors
#### Genetic risk factors (high-penetrance Mendelian genes)
The 2022 ACC/AHA guideline excerpt lists **11 genes “confirmed to confer a highly penetrant risk for TAD”**:
- **FBN1, LOX, COL3A1, TGFBR1, TGFBR2, SMAD3, TGFB2, ACTA2, MYH11, MYLK, PRKG1** (isselbacher20222022accahaguideline pages 23-24).

Additional genes are highlighted in 2023–2024 reviews as part of syndromic HTAD (e.g., Loeys–Dietz spectrum genes SMAD2, TGFB3) (duarte2023geneticallytriggeredthoracic pages 1-3) and broader thoracic-aortic-disease genetics (e.g., NOTCH1, MFAP5) (butnariu2024identificationofgenetic pages 4-5).

#### Environmental/clinical risk factors
A 2024 review notes additional risk factors for thoracic aortic aneurysm including **hypertension, smoking, hypercholesterolemia, male sex, older age (>65 years), and bicuspid aortic valve** (butnariu2024identificationofgenetic pages 4-5).

### 2.3 Protective factors
- **Evidence gap:** The ACC/AHA guideline notes growing interest in biomarkers and other predictors, but “biomarker expression has not been clearly associated with relevant clinical aortic events” and emphasizes limited randomized trial evidence for prevention strategies (isselbacher20222022accahaguideline pages 140-142).

### 2.4 Gene–environment interactions
- **Current understanding:** The ACC/AHA guideline explicitly notes that “environmental factors and lifestyle habits may contribute to aortic aneurysm formation” in addition to genetic variants, and highlights medication exposures (e.g., **fluoroquinolones**) as potentially increasing risk, with mechanisms still uncertain (isselbacher20222022accahaguideline pages 140-142).

---

## 3. Phenotypes (clinical spectrum)
### 3.1 Core vascular phenotype (FTAAD / ns-HTAD)
- **Key features:** thoracic aortic aneurysm (TAA), rapid aneurysm growth in some families, and acute type A dissection; familial expression is variable and dissections can occur at diameters <5.0 cm in some families (isselbacher20222022accahaguideline pages 23-24, levy2024currentunderstandingof pages 3-5).

**HPO term suggestions (vascular):**
- Thoracic aortic aneurysm; Aortic aneurysm; Aortic dissection; Ascending aortic aneurysm; Aortic root dilatation; Rapid aneurysm progression.

### 3.2 Syndromic HTAD phenotype examples (useful for differential diagnosis)
Because “HTAD can be classified as non-syndromic… and syndromic when associated with extra-aortic features,” syndromic features are important to recognize when labeling a case as FTAAD vs syndromic HTAD (monda2023theroleof pages 1-3).

**Marfan syndrome (FBN1):**
- Aortic root dilatation (Z-score ≥2), dissection; extra-aortic features include ectopia lentis, skeletal abnormalities, dural ectasia; mitral valve prolapse reported as **>50%** in one review summary; branch aneurysms reported in about **one-quarter**; descending/abdominal involvement in **10–20%** (monda2023theroleof pages 3-4).

**Loeys–Dietz syndrome (TGFBR1/2, SMAD2/3, TGFB2/3):**
- Arterial tortuosity, hypertelorism, bifid uvula/cleft palate; higher dissection risk; complications can occur at smaller diameters (duarte2023geneticallytriggeredthoracic pages 1-3, spaziani2024hereditarythoracicaortic pages 2-4).

**Vascular Ehlers–Danlos (COL3A1):**
- Severe arterial fragility/rupture; reduced median life expectancy in one summary (~51 years) (monda2023theroleof pages 4-6).

**HPO term suggestions (syndromic flags):**
- Ectopia lentis; Scoliosis; Pectus excavatum/carinatum; Joint hypermobility; Dural ectasia; Hypertelorism; Arterial tortuosity; Bifid uvula; Cleft palate; Easy bruising; Thin/translucent skin.

### 3.3 Age of onset, severity, progression
- HTAD clinical course can range “from… early-onset and aggressive to… late-onset, indolent aortic disease,” and age at onset of acute syndromes can vary even among carriers of the same pathogenic mutation (monda2023theroleof pages 1-3).
- Familial disease is typically autosomal dominant with decreased penetrance, “particularly in women,” and shows variable expression including varying age of onset and increased frequency of dissection at diameter <5.0 cm in some families (isselbacher20222022accahaguideline pages 23-24).

### 3.4 Quality-of-life (QoL)
- The 2022 ACC/AHA guideline states baseline HRQOL assessment in aortic disease is limited; evidence for QoL in “heritable TAA” is “narrow or limited only to patients with Marfan syndrome,” and scattered data exist for psychological interventions (isselbacher20222022accahaguideline pages 140-142).

---

## 4. Genetic/Molecular Information
### 4.1 Causal genes (curation-ready)
The most guideline-central “highly penetrant” HTAD genes are the 11-gene set listed above (isselbacher20222022accahaguideline pages 23-24). A 2024 HTAD genetics table further lists syndromic and non-syndromic genes with **OMIM gene entries** and inheritance patterns, including examples such as **FBN1 (AD), TGFBR2 (AD), TGFBR1 (AD), SMAD3 (AD), COL3A1 (AD), SLC2A10 (AR), MYH11 (AD), MYLK (AD), PRKG1 (AD), MFAP5 (AD), LOX (AD), ACTA2 (AD)** (butnariu2024identificationofgenetic pages 2-4, butnariu2024identificationofgenetic pages 4-5).

### 4.2 Pathogenic variant types / classification
- The 2022 guideline notes laboratories classify variants as “pathogenic, likely pathogenic, variant of uncertain/unknown significance, benign, and likely benign,” and that **VUS should not be used** to determine risk or guide management (isselbacher20222022accahaguideline pages 24-26).

### 4.3 Penetrance and expressivity
- HTAD in families is “typically inherited in an autosomal dominant manner, with decreased penetrance, particularly in women,” and exhibits variable expression (isselbacher20222022accahaguideline pages 23-24).

### 4.4 Recent development: mosaicism and broadened genetic architecture (2024)
A 2024 single-center study of nonsyndromic adults (<60 years) using deep sequencing reported:
- Likely genetic causes in **24%** (21% germline; 3% somatic mosaic) and enrichment vs controls for germline variants (OR **2.44**) and somatic mosaic variants (OR **4.71**) (chen2024contributionsofgermline pages 1-2).

### 4.5 Modifier genes / epigenetics / chromosomal abnormalities
- **Not established from retrieved excerpts.** Some reviews note genetic complexity and future directions, but specific modifier genes/epigenetic signatures were not extractable from the current tool-retrieved text set (isselbacher20222022accahaguideline pages 140-142).

---

## 5. Environmental Information
- Traditional vascular risk factors (hypertension, smoking, hypercholesterolemia, age/sex) are summarized for TAA risk (butnariu2024identificationofgenetic pages 4-5).
- The 2022 guideline highlights emerging evidence linking **fluoroquinolone use** to increased aneurysm/dissection risk, with unclear mechanisms (isselbacher20222022accahaguideline pages 140-142).

---

## 6. Mechanism / Pathophysiology
### 6.1 Core histopathology and tissue-level mechanism
A 2024 review describes thoracic aneurysm histopathology as:
- “medial cystic necrosis with fragmentation and focal loss of elastic fibers… accompanied by a decrease in vascular smooth muscle cells (VSMCs) and an increase in proteoglycans” (butnariu2024identificationofgenetic pages 4-5).

### 6.2 Key molecular pathway axes
1) **TGF-β signaling dysregulation (LDS spectrum; also overlaps broader HTAD):**
- Pathogenic mutations in **TGFBR1/TGFBR2** are described as causing a “pathological shift towards increased extracellular matrix degradations,” contributing to aneurysm formation and susceptibility to rupture (monda2023theroleof pages 1-3).

2) **Extracellular matrix (ECM) structural failure:**
- Genes such as **FBN1, LOX, COL3A1, MFAP5** affect microfibrils/collagen/crosslinking and aortic wall integrity (isselbacher20222022accahaguideline pages 23-24, butnariu2024identificationofgenetic pages 4-5).

3) **VSMC contractile apparatus / elastin–contractile unit disruption:**
- Mutations in **ACTA2, MYH11, MYLK, PRKG1** are cited as impacting VSMC adhesion/contraction and the “elastin contractile unit,” weakening the aortic wall (butnariu2024identificationofgenetic pages 4-5).

### 6.3 Upstream→downstream causal chain (knowledge-base ready)
- **Trigger:** germline pathogenic variant (or mosaic) affecting ECM/TGF-β/VSMC contractile genes (isselbacher20222022accahaguideline pages 23-24, chen2024contributionsofgermline pages 1-2)
- **Cellular/tissue changes:** VSMC dysfunction/loss, elastin fragmentation, proteoglycan accumulation, ECM degradation (butnariu2024identificationofgenetic pages 4-5)
- **Organ-level phenotype:** progressive thoracic aortic dilatation; risk of dissection/rupture, sometimes at smaller diameters than expected (butnariu2024identificationofgenetic pages 2-4, levy2024currentunderstandingof pages 3-5)

### 6.4 Ontology suggestions
- **GO Biological Process (suggestions):** extracellular matrix organization; elastic fiber formation; smooth muscle contraction; transforming growth factor beta receptor signaling pathway.
- **CL cell types (suggestions):** vascular smooth muscle cell.
- **UBERON anatomy (suggestions):** thoracic aorta; ascending aorta; aortic root.

---

## 7. Anatomical Structures Affected
- **Primary:** aortic root and ascending aorta are emphasized in guideline testing indications and HTAD surveillance context (isselbacher20222022accahaguideline pages 23-24).
- **Additional vascular beds:** reviews note peripheral/intracranial aneurysms as part of family history/risk assessment and gene-specific associations (e.g., TGFBR2 and other arterial aneurysms) (isselbacher20222022accahaguideline pages 23-24, isselbacher20222022accahaguideline pages 24-26).

**UBERON suggestions:** thoracic aorta; ascending aorta; aortic root; intracranial artery.

---

## 8. Temporal Development
- **Onset pattern:** asymptomatic dilation often discovered incidentally; acute dissection can be first presentation and may be fatal (duarte2023geneticallytriggeredthoracic pages 1-3).
- **Progression:** progressive dilation determines prognosis (monda2023theroleof pages 1-3).

---

## 9. Inheritance and Population
### 9.1 Epidemiology / burden
- **Incidence:** population study summarized in 2023 review: thoracic aortic aneurysm incidence **10.4 per 100,000 person-years** (duarte2023geneticallytriggeredthoracic pages 1-3).
- **Sex:** same review notes **51%** of thoracic aneurysm patients were women, recognized at older ages than men (duarte2023geneticallytriggeredthoracic pages 1-3).
- **Mortality:** thoracic dissection is highly lethal; a 2024 review summarizes pre-hospital mortality “up to 61%” and ~50% mortality within 30 days; emergent repair ~20% vs elective ~3% (levy2024currentunderstandingof pages 1-3).
- **US deaths/year:** nonsyndromic TAA paper notes ~“nearly 10,000 deaths in the United States per year” (chen2024contributionsofgermline pages 1-2).

### 9.2 Familiality and inheritance
- Among TAD patients without Marfan/LDS features, “13% to 20%… have similarly affected first-degree relatives,” and inheritance is “typically… autosomal dominant… decreased penetrance” (isselbacher20222022accahaguideline pages 23-24).
- Reviews similarly estimate **~20–25%** of non-syndromic HTAD cases have positive family history (monda2023theroleof pages 1-3, butnariu2024identificationofgenetic pages 2-4).

---

## 10. Diagnostics
### 10.1 Genetic testing (who to test; what test)
**Guideline-centered clinical workflow (ACC/AHA 2022):**
1) Obtain multigenerational family history of TAD, sudden deaths, and peripheral/intracranial aneurysms (isselbacher20222022accahaguideline pages 23-24).
2) For patients with aortic root/ascending aneurysm or dissection plus HTAD risk factors (Table 8/Figure 17 referenced), perform genetic testing for pathogenic/likely pathogenic variants (isselbacher20222022accahaguideline pages 23-24).
3) Use **multigene panel testing** as “most cost-effective and clinically useful” approach; manage and cascade-test based on **pathogenic/likely pathogenic** variants only (isselbacher20222022accahaguideline pages 23-24).
4) **VUS should not guide** family risk stratification (isselbacher20222022accahaguideline pages 24-26).

**Imaging modalities for relatives:**
- Aortic imaging with **TTE** if adequate visualization; otherwise **CT or MRI** (isselbacher20222022accahaguideline pages 23-24).
- If at-risk relatives have negative initial imaging, suggested repeat imaging is ~**5 years** in younger relatives and ~**10 years** in older relatives (isselbacher20222022accahaguideline pages 24-26).

**NGS modalities in current practice:** gene panels, WES, WGS increasingly used for heterogeneous HTAD etiologies (butnariu2024identificationofgenetic pages 2-4).

### 10.2 Differential diagnosis considerations
- Distinguish **non-syndromic** familial disease from syndromic HTAD (Marfan, LDS, vEDS) based on extra-aortic features and gene findings (monda2023theroleof pages 1-3, duarte2023geneticallytriggeredthoracic pages 1-3).

---

## 11. Outcome / Prognosis
- Prognosis in HTAD is determined by progressive aortic dilation leading to acute aortic events (dissection/rupture), and varies by underlying mutation (monda2023theroleof pages 1-3).
- High lethality of dissection and large differences between emergent vs elective operative mortality support aggressive prevention and surveillance strategies (levy2024currentunderstandingof pages 1-3).

---

## 12. Treatment
### 12.1 Surgical thresholds (available in retrieved excerpts)
- A 2024 review summarizing the 2022 guideline indicates prophylactic repair thresholds of **≥5.0 cm** for asymptomatic low-risk individuals and **≥4.5 cm** for high-risk individuals (levy2024currentunderstandingof pages 9-10).
- A 2023 review provides Marfan-specific thresholds: aortic sinus **≥50 mm** or **≥45 mm** with risk factors (monda2023theroleof pages 4-6).

**Important limitation:** The gene-specific thresholds table(s) referenced in the guideline (Table 8/Figure 17) could not be retrieved from the available excerpts or via image tools (isselbacher20222022accahaguideline pages 23-24).

### 12.2 Medical therapy / supportive care
- The ACC/AHA guideline emphasizes individualized exercise recommendations based on pathology, aortic diameter, growth rate, family history, and other high-risk features (isselbacher20222022accahaguideline pages 139-140).
- Post-aortic surgery cardiac rehabilitation can be useful; one recommendation is **3–5 METs**, avoiding strenuous lifting/exhaustion (isselbacher20222022accahaguideline pages 139-140).

### 12.3 Pharmacotherapy evidence example (vEDS)
- For vascular Ehlers–Danlos syndrome, a review summary reports trial evidence that **celiprolol reduced arterial events (20% vs 50%)** (monda2023theroleof pages 4-6).

### 12.4 Trials / experimental directions (ClinicalTrials.gov signals)
Interventional trials identified by search included, for example:
- **NCT05401500** (Familial Aortopathies and Cellular Exploration) (trial retrieved in tool run)
- **NCT05472519** (Immunopathology of Loeys-Dietz Syndrome) (trial retrieved)
- **NCT05809323** (Marfan Syndrome Moderate Exercise Trial II) (trial retrieved)
- **NCT07495267** (Nutritional Ketosis Marfan; not yet recruiting) (trial retrieved)

(Trial text chunks were retrieved by the tool, but detailed endpoints/results were not extracted in the present evidence set.)

### 12.5 MAXO suggestions (treatments/actions)
- Prophylactic aortic surgery; Aortic imaging surveillance; Genetic testing; Genetic counseling; Cascade screening; Exercise counseling / cardiac rehabilitation.

---

## 13. Prevention
- **Secondary prevention:** family-based genetic testing and cascade imaging is strongly recommended by ACC/AHA 2022 (isselbacher20222022accahaguideline pages 23-24).
- **Lifestyle/behavioral:** individualized exercise counseling; avoid maximal exertion/strenuous lifting; cardiac rehab post-surgery (isselbacher20222022accahaguideline pages 139-140).

---

## 14. Other Species / Natural Disease
- **Not available from retrieved evidence.**

---

## 15. Model Organisms
- The ACC/AHA guideline cites mouse Marfan studies where mild/moderate (not strenuous) aerobic exercise protected the aortic wall, with reduced elastin fragmentation and reduced MMP2/9 expression vs sedentary controls (isselbacher20222022accahaguideline pages 139-140).

---

## Recent developments and real-world implementations (prioritizing 2023–2024)
1) **Expanded genetic architecture in nonsyndromic adults (2024):** deep (>500×) sequencing identifies germline and mosaic contributions, supporting broader genetic evaluation beyond classic syndromic testing paradigms (chen2024contributionsofgermline pages 1-2).
2) **Point-of-care decision support (2023–2024):** a REDCap-based “Genomic Medicine Guidance” tool integrates ClinVar/ClinGen and guideline recommendations and curates thousands of pathogenic variants (reported **2,286** unique pathogenic mutations across 13 genes) to deliver gene-informed surveillance/therapy guidance in clinical workflows (patil2024developmentandassessment pages 1-5).

**Direct abstract quotes (for evidence anchoring):**
- “Heritable thoracic aortic disease (HTAD) is a term used to define a large group of disorders characterized by the occurrence of aortic events, mainly represented by aneurysm or dissection.” (Monda 2023; Diagnostics; published 17 Feb 2023; https://doi.org/10.3390/diagnostics13040772) (monda2023theroleof pages 1-3)
- “Likely genetic causes were present in 24% with nonsyndromic TAA, of which 21% arose from germline variants and 3% from somatic mosaic alleles.” (Chen 2024; JAHA; published 2024; https://doi.org/10.1161/JAHA.123.033232) (chen2024contributionsofgermline pages 1-2)
- “Up to 25% of patients with thoracic aortic disease have an underlying Mendelian pathogenic variant.” (Duarte 2023; Methodist DeBakey Cardiovasc J; published 2023; https://doi.org/10.14797/mdcvj.1218) (duarte2023geneticallytriggeredthoracic pages 1-3)

---

## Curator-oriented summary table
| Item type | Identifier/Gene | Notes | Key statistic (if any) | Primary supporting source (short cite: first author year + PMID if known) |
|---|---|---|---|---|
| Disease concept / ontology | MONDO:0019625 | Familial thoracic aortic aneurysm and aortic dissection; Open Targets evidence links this MONDO concept to core HTAD genes | 12 associated targets in Open Targets snapshot | Open Targets/MONDO (isselbacher20222022accahaguideline pages 23-24) |
| Disease concept / ontology | MONDO:0012730 | Aortic aneurysm, familial thoracic 6; corresponds to ACTA2-related familial thoracic aortic aneurysm entity | — | Open Targets/MONDO (isselbacher20222022accahaguideline pages 23-24) |
| Disease concept / ontology | MONDO:0007568 | Aortic aneurysm, familial thoracic 4; corresponds to MYH11-related familial thoracic aortic aneurysm entity | — | Open Targets/MONDO (isselbacher20222022accahaguideline pages 23-24) |
| Disease concept / ontology | MONDO:0013418 | Aortic aneurysm, familial thoracic 7; corresponds to MYLK-related familial thoracic aortic aneurysm entity | — | Open Targets/MONDO (isselbacher20222022accahaguideline pages 23-24) |
| Causal gene (ECM / connective tissue) | FBN1 | High-penetrance HTAD gene in 2022 ACC/AHA panel; classic Marfan syndrome gene, but some variants can present as isolated thoracic aortic disease | Marfan prevalence ~1 in 5,000 to 1 in 10,000; >95% of MFS cases due to FBN1 in review summaries | Isselbacher 2022; Monda 2023 (isselbacher20222022accahaguideline pages 23-24, monda2023theroleof pages 3-4) |
| Causal gene (ECM / connective tissue) | COL3A1 | High-penetrance HTAD gene; vascular Ehlers-Danlos syndrome with arterial fragility/rupture phenotype | vEDS represents <5% of EDS in one 2024 review | Isselbacher 2022; Duarte 2023; Spaziani 2024 (isselbacher20222022accahaguideline pages 23-24, duarte2023geneticallytriggeredthoracic pages 1-3, spaziani2024hereditarythoracicaortic pages 2-4) |
| Causal gene (ECM / connective tissue) | LOX | High-penetrance HTAD gene; lysyl oxidase, implicated in nonsyndromic familial thoracic aortic aneurysm | — | Isselbacher 2022; Duarte 2023 (isselbacher20222022accahaguideline pages 23-24, duarte2023geneticallytriggeredthoracic pages 1-3) |
| Causal gene (ECM / connective tissue) | MFAP5 | Listed in 2024 review table as AD AAT9; microfibril-associated protein 5, associated with TAA | — | Butnariu 2024 (butnariu2024identificationofgenetic pages 4-5) |
| Causal gene (TGF-β pathway) | TGFBR1 | High-penetrance HTAD gene; Loeys-Dietz syndrome; childhood burden may justify surveillance in first decade for pathogenic variants | LDS complications can occur at smaller diameters; pediatric onset described | Isselbacher 2022; Monda 2023; Spaziani 2024 (isselbacher20222022accahaguideline pages 23-24, monda2023theroleof pages 1-3, spaziani2024hereditarythoracicaortic pages 1-2) |
| Causal gene (TGF-β pathway) | TGFBR2 | High-penetrance HTAD gene; Loeys-Dietz syndrome; associated with intracranial/other arterial aneurysm risk in guideline summary | Acute complications may occur at smaller diameters and with faster growth | Isselbacher 2022; Spaziani 2024 (isselbacher20222022accahaguideline pages 24-26, spaziani2024hereditarythoracicaortic pages 1-2) |
| Causal gene (TGF-β pathway) | SMAD3 | High-penetrance HTAD gene; Loeys-Dietz spectrum / aneurysm-osteoarthritis phenotype | — | Isselbacher 2022; Duarte 2023 (isselbacher20222022accahaguideline pages 23-24, duarte2023geneticallytriggeredthoracic pages 1-3) |
| Causal gene (TGF-β pathway) | TGFB2 | High-penetrance HTAD gene in ACC/AHA panel | ~6–8% of nonsyndromic HTAD families for syndromic-gene group noted in guideline summary | Isselbacher 2022 (isselbacher20222022accahaguideline pages 24-26) |
| Causal gene (TGF-β pathway) | SMAD2 / TGFB3 | Included in 2023 review table for Loeys-Dietz syndrome spectrum; not part of the 11-gene highly penetrant ACC/AHA core list cited in excerpt | — | Duarte 2023 (duarte2023geneticallytriggeredthoracic pages 1-3) |
| Causal gene (VSMC contractile apparatus) | ACTA2 | High-penetrance HTAD gene; most frequently mutated nonsyndromic HTAD gene in 2023 review; associated with livedo reticularis, iris flocculi, PDA/BAV in review table | Missense ACTA2 variants reported in ~14% of inherited ascending TAD; ACTA2-linked familial entity mapped to MONDO:0012730 | Duarte 2023; Butnariu 2024; Open Targets/MONDO (duarte2023geneticallytriggeredthoracic pages 3-4, butnariu2024identificationofgenetic pages 4-5, isselbacher20222022accahaguideline pages 23-24) |
| Causal gene (VSMC contractile apparatus) | MYH11 | High-penetrance HTAD gene; associated with familial thoracic aneurysm/dissection and PDA | Familial thoracic aneurysm 4 entity mapped to MONDO:0007568 | Isselbacher 2022; Butnariu 2024; Open Targets/MONDO (isselbacher20222022accahaguideline pages 23-24, butnariu2024identificationofgenetic pages 4-5) |
| Causal gene (VSMC contractile apparatus) | MYLK | High-penetrance HTAD gene; nonsyndromic familial TAAD; can dissect at relatively small diameters in prior literature/guideline context | Familial thoracic aneurysm 7 entity mapped to MONDO:0013418 | Isselbacher 2022; Butnariu 2024; Open Targets/MONDO (isselbacher20222022accahaguideline pages 23-24, butnariu2024identificationofgenetic pages 4-5) |
| Causal gene (VSMC contractile apparatus) | PRKG1 | High-penetrance HTAD gene; nonsyndromic familial TAAD/AD | — | Isselbacher 2022; Duarte 2023 (isselbacher20222022accahaguideline pages 23-24, duarte2023geneticallytriggeredthoracic pages 1-3) |
| Epidemiology / burden | Thoracic aortic aneurysm incidence | Population incidence summarized in 2023 review | 10.4 per 100,000 person-years | Duarte 2023 (duarte2023geneticallytriggeredthoracic pages 1-3) |
| Epidemiology / burden | Female share in population study | Women were older at recognition than men in cited population study | 51% of thoracic aortic aneurysm patients were women | Duarte 2023 (duarte2023geneticallytriggeredthoracic pages 1-3) |
| Epidemiology / familiality | Non-syndromic HTAD with family history | Consistent estimate across 2023–2024 reviews | ~20–25% | Monda 2023; Butnariu 2024 (monda2023theroleof pages 1-3, butnariu2024identificationofgenetic pages 2-4) |
| Epidemiology / familiality | TAD patients without Marfan/LDS features having affected first-degree relatives | Guideline estimate supporting family screening | 13–20% | Isselbacher 2022 (isselbacher20222022accahaguideline pages 23-24) |
| Epidemiology / inheritance | Familial aggregation in TAAD cohorts | Familial pattern common; many pedigrees AD with variable expression | ~21% familial; ~77% of familial cases autosomal dominant | Levy 2024 (levy2024currentunderstandingof pages 3-5) |
| Epidemiology / clinical severity | Dissections below size thresholds | Diameter alone is an imperfect predictor of acute events | 60% of dissections <5.5 cm; 40% <5.0 cm | Levy 2024 (levy2024currentunderstandingof pages 3-5) |
| Epidemiology / growth | Familial aneurysm growth rate | Familial TAAD may enlarge faster than sporadic disease | ~0.21–0.22 cm/year | Levy 2024 (levy2024currentunderstandingof pages 3-5) |
| Epidemiology / mortality | Pre-hospital and early mortality of thoracic dissection | High lethality emphasizes preventive repair | Pre-hospital mortality up to 61%; ~50% die within 30 days; emergent repair mortality ~20% vs elective ~3% | Levy 2024 (levy2024currentunderstandingof pages 1-3) |
| Epidemiology / genetics yield | Deep sequencing in nonsyndromic adults <60 years | 2024 single-center study showing substantial germline and mosaic contribution | Likely genetic cause in 24% overall: 21% germline, 3% somatic mosaic; germline OR 2.44, mosaic OR 4.71 | Chen 2024 (chen2024contributionsofgermline pages 1-2) |
| Epidemiology / genetics yield | Most frequently mutated genes in nonsyndromic adult TAA cohort | 2024 targeted sequencing study | Top 3 genes: FLNA, NOTCH3, FBN1 | Chen 2024 (chen2024contributionsofgermline pages 1-2) |
| Epidemiology / clinical app | Point-of-care genomics implementation | 2024 app operationalized guideline recommendations across common HTAD genes | 13 most frequently mutated TAD genes; 2,286 unique pathogenic mutations curated | Patil 2024 (patil2024developmentandassessment pages 1-5) |


*Table: This table summarizes the core disease concept identifiers, major causal genes grouped by biological pathway, and key recent epidemiologic statistics for familial/heritable thoracic aortic aneurysm and dissection. It is designed as a compact curation aid for building a disease knowledge base entry.*

---

## Limitations of this tool-based report (important for knowledge-base curation)
1) **Ontology identifiers:** beyond MONDO, this evidence set did not contain explicit OMIM disease IDs, Orphanet IDs, ICD-10/ICD-11 codes, or MeSH terms for the specific “familial thoracic aortic aneurysm and dissection” concept.
2) **Gene-specific surgical thresholds:** the ACC/AHA guideline excerpt references Table 8/Figure 17 for HTAD risk factors and gene-informed management; however, the tool could not retrieve the relevant images/tables, preventing extraction of the complete gene-specific threshold matrix.
3) **Primary mechanistic PMIDs:** mechanistic statements are supported by recent reviews/guidelines in this evidence set, but the underlying primary experimental PMIDs were not consistently present in the retrieved chunks for direct citation.

---

## Key source URLs (publication dates as available in evidence)
- Isselbacher et al. **2022** ACC/AHA Aortic Disease Guideline (JACC; Oct 2022): https://doi.org/10.1016/j.jacc.2022.08.004 (isselbacher20222022accahaguideline pages 23-24)
- Monda et al. **2023-02-17** (Diagnostics): https://doi.org/10.3390/diagnostics13040772 (monda2023theroleof pages 1-3)
- Duarte et al. **2023** (Methodist DeBakey Cardiovasc J): https://doi.org/10.14797/mdcvj.1218 (duarte2023geneticallytriggeredthoracic pages 1-3)
- Spaziani et al. **2024-01** (Diagnostics): https://doi.org/10.3390/diagnostics14010112 (spaziani2024hereditarythoracicaortic pages 1-2)
- Levy et al. **2024-01** (Vessel Plus): https://doi.org/10.20517/2574-1209.2023.55 (levy2024currentunderstandingof pages 1-3)
- Chen et al. **2024-07** (JAHA): https://doi.org/10.1161/JAHA.123.033232 (chen2024contributionsofgermline pages 1-2)
- Butnariu et al. **2024-10** (Int J Mol Sci): https://doi.org/10.3390/ijms252011173 (butnariu2024identificationofgenetic pages 2-4)
- Patil et al. **2023-12-28** (JMIR preprint): https://doi.org/10.2196/preprints.55903 (patil2024developmentandassessment pages 1-5)


References

1. (isselbacher20222022accahaguideline pages 23-24): E. Isselbacher, O. Preventza, James Hamilton Black, J. Augoustides, A. Beck, M. Bolen, A. Braverman, B. Bray, Maya M Brown-Zimmerman, E. Chen, T. Collins, A. DeAnda, Christina L. Fanola, L. Girardi, C. Hicks, D. Hui, W. Schuyler Jones, V. Kalahasti, Karen M Kim, D. Milewicz, G. Oderich, Laura Ogbechie, S. Promes, Elsie Gyang Ross, M. Schermerhorn, Sabrina Singleton Times, E. Tseng, Grace J. Wang, and Y. Woo. 2022 acc/aha guideline for the diagnosis and management of aortic disease: a report of the american heart association/american college of cardiology joint committee on clinical practice guidelines. Journal of the American College of Cardiology, Oct 2022. URL: https://doi.org/10.1016/j.jacc.2022.08.004, doi:10.1016/j.jacc.2022.08.004. This article has 2576 citations and is from a highest quality peer-reviewed journal.

2. (monda2023theroleof pages 1-3): Emanuele Monda, Michele Lioncino, Federica Verrillo, Marta Rubino, Martina Caiazza, Alfredo Mauriello, Natale Guarnaccia, Adelaide Fusco, Annapaola Cirillo, Simona Covino, Ippolita Altobelli, Gaetano Diana, Giuseppe Palmiero, Francesca Dongiglio, Francesco Natale, Arturo Cesaro, Eduardo Bossone, Maria Giovanna Russo, Paolo Calabrò, and Giuseppe Limongelli. The role of genetic testing in patients with heritable thoracic aortic diseases. Diagnostics, 13:772, Feb 2023. URL: https://doi.org/10.3390/diagnostics13040772, doi:10.3390/diagnostics13040772. This article has 19 citations.

3. (butnariu2024identificationofgenetic pages 2-4): Lăcrămioara Ionela Butnariu, Georgiana Russu, Alina-Costina Luca, Constantin Sandu, Laura Mihaela Trandafir, Ioana Vasiliu, Setalia Popa, Gabriela Ghiga, Laura Bălănescu, and Elena Țarcă. Identification of genetic variants associated with hereditary thoracic aortic diseases (htads) using next generation sequencing (ngs) technology and genotype–phenotype correlations. International Journal of Molecular Sciences, 25:11173, Oct 2024. URL: https://doi.org/10.3390/ijms252011173, doi:10.3390/ijms252011173. This article has 4 citations.

4. (duarte2023geneticallytriggeredthoracic pages 1-3): Valeria E. Duarte, Raman Yousefzai, and Michael N. Singh. Genetically triggered thoracic aortic disease: who should be tested? Methodist DeBakey Cardiovascular Journal, 19:24-28, Mar 2023. URL: https://doi.org/10.14797/mdcvj.1218, doi:10.14797/mdcvj.1218. This article has 18 citations.

5. (levy2024currentunderstandingof pages 1-3): Lauren E. Levy, Megan Zak, and Jason P. Glotzbach. Current understanding of the genetics of thoracic aortic disease. Vessel Plus, Jan 2024. URL: https://doi.org/10.20517/2574-1209.2023.55, doi:10.20517/2574-1209.2023.55. This article has 4 citations.

6. (levy2024currentunderstandingof pages 3-5): Lauren E. Levy, Megan Zak, and Jason P. Glotzbach. Current understanding of the genetics of thoracic aortic disease. Vessel Plus, Jan 2024. URL: https://doi.org/10.20517/2574-1209.2023.55, doi:10.20517/2574-1209.2023.55. This article has 4 citations.

7. (spaziani2024hereditarythoracicaortic pages 1-2): Gaia Spaziani, Francesca Chiara Surace, Francesca Girolami, Francesco Bianco, Valentina Bucciarelli, Francesca Bonanni, Elena Bennati, Luigi Arcieri, and Silvia Favilli. Hereditary thoracic aortic diseases. Diagnostics, 14:112, Jan 2024. URL: https://doi.org/10.3390/diagnostics14010112, doi:10.3390/diagnostics14010112. This article has 2 citations.

8. (chen2024contributionsofgermline pages 1-2): Ming Hui Chen, Ellen S. Deng, Jessica M. Yamada, Sangita Choudhury, Julia Scotellaro, Lily Kelley, Eric Isselbacher, Mark E. Lindsay, Christopher A. Walsh, and Ryan N. Doan. Contributions of germline and somatic mosaic genetics to thoracic aortic aneurysms in nonsyndromic individuals. Journal of the American Heart Association, Jul 2024. URL: https://doi.org/10.1161/jaha.123.033232, doi:10.1161/jaha.123.033232. This article has 4 citations.

9. (butnariu2024identificationofgenetic pages 4-5): Lăcrămioara Ionela Butnariu, Georgiana Russu, Alina-Costina Luca, Constantin Sandu, Laura Mihaela Trandafir, Ioana Vasiliu, Setalia Popa, Gabriela Ghiga, Laura Bălănescu, and Elena Țarcă. Identification of genetic variants associated with hereditary thoracic aortic diseases (htads) using next generation sequencing (ngs) technology and genotype–phenotype correlations. International Journal of Molecular Sciences, 25:11173, Oct 2024. URL: https://doi.org/10.3390/ijms252011173, doi:10.3390/ijms252011173. This article has 4 citations.

10. (isselbacher20222022accahaguideline pages 140-142): E. Isselbacher, O. Preventza, James Hamilton Black, J. Augoustides, A. Beck, M. Bolen, A. Braverman, B. Bray, Maya M Brown-Zimmerman, E. Chen, T. Collins, A. DeAnda, Christina L. Fanola, L. Girardi, C. Hicks, D. Hui, W. Schuyler Jones, V. Kalahasti, Karen M Kim, D. Milewicz, G. Oderich, Laura Ogbechie, S. Promes, Elsie Gyang Ross, M. Schermerhorn, Sabrina Singleton Times, E. Tseng, Grace J. Wang, and Y. Woo. 2022 acc/aha guideline for the diagnosis and management of aortic disease: a report of the american heart association/american college of cardiology joint committee on clinical practice guidelines. Journal of the American College of Cardiology, Oct 2022. URL: https://doi.org/10.1016/j.jacc.2022.08.004, doi:10.1016/j.jacc.2022.08.004. This article has 2576 citations and is from a highest quality peer-reviewed journal.

11. (monda2023theroleof pages 3-4): Emanuele Monda, Michele Lioncino, Federica Verrillo, Marta Rubino, Martina Caiazza, Alfredo Mauriello, Natale Guarnaccia, Adelaide Fusco, Annapaola Cirillo, Simona Covino, Ippolita Altobelli, Gaetano Diana, Giuseppe Palmiero, Francesca Dongiglio, Francesco Natale, Arturo Cesaro, Eduardo Bossone, Maria Giovanna Russo, Paolo Calabrò, and Giuseppe Limongelli. The role of genetic testing in patients with heritable thoracic aortic diseases. Diagnostics, 13:772, Feb 2023. URL: https://doi.org/10.3390/diagnostics13040772, doi:10.3390/diagnostics13040772. This article has 19 citations.

12. (spaziani2024hereditarythoracicaortic pages 2-4): Gaia Spaziani, Francesca Chiara Surace, Francesca Girolami, Francesco Bianco, Valentina Bucciarelli, Francesca Bonanni, Elena Bennati, Luigi Arcieri, and Silvia Favilli. Hereditary thoracic aortic diseases. Diagnostics, 14:112, Jan 2024. URL: https://doi.org/10.3390/diagnostics14010112, doi:10.3390/diagnostics14010112. This article has 2 citations.

13. (monda2023theroleof pages 4-6): Emanuele Monda, Michele Lioncino, Federica Verrillo, Marta Rubino, Martina Caiazza, Alfredo Mauriello, Natale Guarnaccia, Adelaide Fusco, Annapaola Cirillo, Simona Covino, Ippolita Altobelli, Gaetano Diana, Giuseppe Palmiero, Francesca Dongiglio, Francesco Natale, Arturo Cesaro, Eduardo Bossone, Maria Giovanna Russo, Paolo Calabrò, and Giuseppe Limongelli. The role of genetic testing in patients with heritable thoracic aortic diseases. Diagnostics, 13:772, Feb 2023. URL: https://doi.org/10.3390/diagnostics13040772, doi:10.3390/diagnostics13040772. This article has 19 citations.

14. (isselbacher20222022accahaguideline pages 24-26): E. Isselbacher, O. Preventza, James Hamilton Black, J. Augoustides, A. Beck, M. Bolen, A. Braverman, B. Bray, Maya M Brown-Zimmerman, E. Chen, T. Collins, A. DeAnda, Christina L. Fanola, L. Girardi, C. Hicks, D. Hui, W. Schuyler Jones, V. Kalahasti, Karen M Kim, D. Milewicz, G. Oderich, Laura Ogbechie, S. Promes, Elsie Gyang Ross, M. Schermerhorn, Sabrina Singleton Times, E. Tseng, Grace J. Wang, and Y. Woo. 2022 acc/aha guideline for the diagnosis and management of aortic disease: a report of the american heart association/american college of cardiology joint committee on clinical practice guidelines. Journal of the American College of Cardiology, Oct 2022. URL: https://doi.org/10.1016/j.jacc.2022.08.004, doi:10.1016/j.jacc.2022.08.004. This article has 2576 citations and is from a highest quality peer-reviewed journal.

15. (levy2024currentunderstandingof pages 9-10): Lauren E. Levy, Megan Zak, and Jason P. Glotzbach. Current understanding of the genetics of thoracic aortic disease. Vessel Plus, Jan 2024. URL: https://doi.org/10.20517/2574-1209.2023.55, doi:10.20517/2574-1209.2023.55. This article has 4 citations.

16. (isselbacher20222022accahaguideline pages 139-140): E. Isselbacher, O. Preventza, James Hamilton Black, J. Augoustides, A. Beck, M. Bolen, A. Braverman, B. Bray, Maya M Brown-Zimmerman, E. Chen, T. Collins, A. DeAnda, Christina L. Fanola, L. Girardi, C. Hicks, D. Hui, W. Schuyler Jones, V. Kalahasti, Karen M Kim, D. Milewicz, G. Oderich, Laura Ogbechie, S. Promes, Elsie Gyang Ross, M. Schermerhorn, Sabrina Singleton Times, E. Tseng, Grace J. Wang, and Y. Woo. 2022 acc/aha guideline for the diagnosis and management of aortic disease: a report of the american heart association/american college of cardiology joint committee on clinical practice guidelines. Journal of the American College of Cardiology, Oct 2022. URL: https://doi.org/10.1016/j.jacc.2022.08.004, doi:10.1016/j.jacc.2022.08.004. This article has 2576 citations and is from a highest quality peer-reviewed journal.

17. (patil2024developmentandassessment pages 1-5): Rohan Patil, Fatima Ashraf, Samer Abu Dayeh, and Siddharth K Prakash. Development and assessment of a point-of-care application (genomic medicine guidance) for heritable thoracic aortic disease. JMIRx Med, 5:e55903-e55903, Oct 2024. URL: https://doi.org/10.2196/55903, doi:10.2196/55903. This article has 5 citations.

18. (duarte2023geneticallytriggeredthoracic pages 3-4): Valeria E. Duarte, Raman Yousefzai, and Michael N. Singh. Genetically triggered thoracic aortic disease: who should be tested? Methodist DeBakey Cardiovascular Journal, 19:24-28, Mar 2023. URL: https://doi.org/10.14797/mdcvj.1218, doi:10.14797/mdcvj.1218. This article has 18 citations.