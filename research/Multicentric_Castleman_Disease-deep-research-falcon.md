---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-10T05:44:07.637251'
end_time: '2026-05-10T06:07:06.282467'
duration_seconds: 1378.65
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Multicentric Castleman Disease
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 56
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Multicentric Castleman Disease
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Multicentric Castleman Disease** covering all of the
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
- **Disease Name:** Multicentric Castleman Disease
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Multicentric Castleman Disease** covering all of the
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


# Multicentric Castleman Disease (MCD) — Comprehensive Disease Characteristics Report (2026-05-10)

## Target disease
- **Disease name:** Multicentric Castleman disease (MCD)
- **Category:** Complex (immune-mediated/lymphoproliferative)
- **Key related entities:** unicentric Castleman disease (UCD); idiopathic MCD (iMCD; HHV-8-negative); HHV-8/KSHV-associated MCD; POEMS-associated MCD (hoffmann2024theclinicalpicture pages 1-2, fajgenbaum2017internationalevidencebasedconsensus pages 1-4)
- **MONDO identifiers (available):**
  - Castleman disease: **MONDO_0015564** (OpenTargets Search: Multicentric Castleman disease)
  - Idiopathic multicentric Castleman disease: **MONDO_0035838** (OpenTargets Search: Multicentric Castleman disease)
- **ICD-10-CM:** **D47.Z2 (Castleman disease)**; effective **2016-10-01** (simpson2018epidemiologyofcastleman pages 1-4, carbone2021castlemandisease pages 1-2)
- **Data provenance note:** Much contemporary MCD knowledge is aggregated from consensus criteria, systematic reviews/meta-analyses, and small cohorts/registries due to rarity; some epidemiology comes from administrative claims using ICD coding + algorithmic case definitions (mukherjee2022epidemiologyandtreatment pages 1-2, hoffmann2024theclinicalpicture pages 1-2).

## 1. Disease information

### 1.1 Concise overview (current understanding)
Castleman disease (CD) is a spectrum of rare disorders characterized by characteristic lymph node histopathology and enlarged lymph nodes; it is clinically categorized into **unicentric CD** (single nodal region) and **multicentric CD** (multiple nodal regions with systemic inflammation and organ dysfunction). MCD can be life-threatening and is heterogeneous, with major subtypes defined by **HHV-8/KSHV status** and associated conditions such as **POEMS**; **iMCD** denotes HHV-8-negative MCD without another identified cause (hoffmann2024theclinicalpicture pages 1-2, fajgenbaum2017internationalevidencebasedconsensus pages 1-4).

### 1.2 Synonyms/alternative names
- **HHV-8-associated MCD** is also described as **KSHV-associated MCD** (Kaposi sarcoma–associated herpesvirus) (polizzotto2012clinicalmanifestationsof pages 1-2).
- iMCD is also referred to as **HHV-8-negative/idiopathic MCD** (fajgenbaum2017internationalevidencebasedconsensus pages 1-4).

### 1.3 Subtype structure and key definitions (high-level)
| Entity/subtype | Core definition/driver | Key diagnostic elements | Typical clinical/lab features | First-line therapy |
|---|---|---|---|---|
| UCD | Localized Castleman disease involving a single enlarged lymph node region; generally less symptomatic than multicentric disease (hoffmann2024theclinicalpicture pages 1-2) | Single-site lymphadenopathy; lymph node histology in the Castleman spectrum; differentiate from MCD by extent of nodal involvement on imaging (CT/PET-CT) and absence of multicentric criteria (hoffmann2024theclinicalpicture pages 1-2, fajgenbaum2018novelinsightsand pages 3-3) | Often asymptomatic or mild symptoms; fewer laboratory abnormalities than MCD, though symptoms/lab abnormalities can occur in a minority and may be more pronounced in pediatric UCD (hoffmann2024theclinicalpicture pages 1-2) | Primarily surgical resection in UCD (denaro2025castlemandiseaseand pages 4-6) |
| iMCD (HHV-8-negative/idiopathic MCD) | Cytokine-driven multicentric Castleman disease with no HHV-8 infection or other identified cause; IL-6 dysregulation is a key pathogenic mechanism (fajgenbaum2017internationalevidencebasedconsensus pages 1-4, rhee2022siltuximabisassociated pages 1-2) | Requires both major criteria: characteristic lymph node histopathology and enlarged lymph nodes >1 cm in at least 2 stations; plus >=2 of 11 minor criteria including >=1 laboratory abnormality; must exclude infectious, autoimmune/autoinflammatory, and malignant mimics. Recommended workup includes CBC, renal/liver function, CRP/ESR, fibrinogen, immunoglobulins/free light chains, albumin, ferritin, HIV serology, HHV-8 qPCR, EBER/LANA-1 in lymph node, IL-6/VEGF where relevant, CT or PET-CT, and organ-function assessment (hoffmann2024theclinicalpicture pages 2-3, fajgenbaum2017internationalevidencebasedconsensus pages 27-29, fajgenbaum2017internationalevidencebasedconsensus pages 1-4) | Constitutional symptoms; hepatosplenomegaly; edema/anasarca/ascites/pleural effusions; anemia; thrombocytopenia or thrombocytosis; hypoalbuminemia; renal dysfunction/proteinuria; polyclonal hypergammaglobulinemia; elevated CRP/ESR; lymphocytic interstitial pneumonitis; can present with cytokine storm and multiorgan dysfunction (fajgenbaum2017internationalevidencebasedconsensus pages 27-29, fajgenbaum2017internationalevidencebasedconsensus pages 1-4, rhee2022siltuximabisassociated pages 1-2) | Siltuximab (anti-IL-6) is recommended first-line/frontline for iMCD; tocilizumab is an alternative in some settings (jitaru2024siltuximabinidiopathic pages 1-2, rhee2022siltuximabisassociated pages 1-2, denaro2025castlemandiseaseand pages 4-6) |
| HHV-8/KSHV-associated MCD | Systemic polyclonal lymphoproliferative disorder driven by HHV-8/KSHV infection, often in HIV-positive or other immunosuppressed patients; viral IL-6 contributes to hypercytokinemia (rigney2025areviewof pages 10-12, estebansampedro2025castlemansdiseaseone pages 6-7, carbone2021castlemandisease pages 4-5) | No formal consensus criteria cited, but experts consider compatible systemic inflammatory syndrome plus HHV-8 evidence sufficient: lymph node biopsy with HHV-8 LANA-1-positive plasmablasts/plasmacytic features, detectable HHV-8 viremia by qPCR, HIV testing, excisional biopsy preferred, CT/PET-CT for multicentric lymphadenopathy (hoffmann2024theclinicalpicture pages 2-3, rigney2025areviewof pages 12-14, rigney2025areviewof pages 10-12) | Generalized lymphadenopathy, splenomegaly/hepatosplenomegaly, effusions/edema, fever/constitutional symptoms, hypoalbuminemia, anemia, thrombocytopenia, elevated CRP, polyclonal hypergammaglobulinemia, high IL-6/IL-10/vIL-6; relapsing-remitting flares may occur (rigney2025areviewof pages 10-12, rigney2025areviewof pages 12-14) | Rituximab-based therapy is first-line; antiretroviral therapy is recommended in HIV-associated disease; liposomal doxorubicin/etoposide or other chemotherapy may be added in severe disease or concurrent Kaposi sarcoma; tocilizumab has also been studied (denaro2025castlemandiseaseand pages 4-6, rigney2025areviewof pages 12-14, NCT04585893 chunk 2) |
| POEMS-associated MCD | MCD occurring in association with POEMS syndrome/plasma cell neoplasm rather than idiopathic disease (hoffmann2024theclinicalpicture pages 1-2, fajgenbaum2017internationalevidencebasedconsensus pages 29-39) | Evaluate Castleman-spectrum lymph node histology with multicentric involvement together with evidence of POEMS/plasma cell disorder; VEGF and monoclonal gammopathy assessment are relevant in workup; POEMS-associated MCD is excluded from iMCD classification (hoffmann2024theclinicalpicture pages 2-3, fajgenbaum2017internationalevidencebasedconsensus pages 29-39) | Shares multicentric lymphadenopathy and inflammatory features of MCD, but occurs with POEMS manifestations and plasma cell dyscrasia/monoclonal gammopathy (hoffmann2024theclinicalpicture pages 1-2, fajgenbaum2017internationalevidencebasedconsensus pages 29-39) | Treat the underlying plasma cell neoplasm/POEMS-associated disease rather than as iMCD; anti-myeloma approaches are referenced for CD subtypes linked to plasma cell disorders (hoffmann2024theclinicalpicture pages 1-2, denaro2025castlemandiseaseand pages 4-6) |


*Table: This table summarizes the major Castleman disease entities relevant to multicentric disease, highlighting drivers, diagnostic workup, typical features, and first-line treatment. It is useful as a compact evidence-based reference for distinguishing iMCD from HHV-8-associated and POEMS-associated forms.*

## 2. Etiology

### 2.1 Disease causal factors
**MCD is etiologically heterogeneous**:
- **HHV-8/KSHV-associated MCD:** driven by **KSHV infection** and associated hypercytokinemia; a viral IL-6 homologue (vIL-6) contributes to systemic inflammation (hoffmann2024theclinicalpicture pages 1-2, polizzotto2012clinicalmanifestationsof pages 1-2).
- **Idiopathic MCD (iMCD):** etiology is unknown but is widely characterized as **cytokine-driven** (often involving IL-6 dysregulation) (fajgenbaum2017internationalevidencebasedconsensus pages 1-4, rhee2022siltuximabisassociated pages 1-2).

**Direct abstract quote (iMCD definition/driver):**
> “Human herpesvirus-8 (HHV-8)–negative, idiopathic multicentric Castleman disease (iMCD) is a rare and life-threatening disorder involving systemic inflammatory symptoms, polyclonal lymphoproliferation, cytopenias, and multiple organ system dysfunction caused by a cytokine storm often including interleukin-6.” (Blood, 2017-03; URL: https://doi.org/10.1182/blood-2016-10-746933) (fajgenbaum2017internationalevidencebasedconsensus pages 1-4)

### 2.2 Risk factors
- **HHV-8/KSHV-associated MCD** often occurs in the setting of **HIV infection or other immunosuppression** and has been described in immunocompromised populations including transplant recipients (hoffmann2024theclinicalpicture pages 1-2, mularoni2026hhv‐8kshvinsolid pages 5-6, atamna2023preventionofoncogenic pages 1-2).
- **Transplant-related risk:** in solid organ transplantation (SOT), **primary HHV-8 infection post-transplant** increases risk of KSHV-associated diseases (including MCD), and donor-derived transmission has been documented (atamna2023preventionofoncogenic pages 1-2, mularoni2026hhv‐8kshvinsolid pages 5-6).

### 2.3 Protective factors / gene–environment interactions
- No well-established protective genetic variants or gene–environment interactions were identified in the retrieved evidence; current literature emphasizes heterogeneity and incomplete understanding, especially for iMCD (fajgenbaum2017internationalevidencebasedconsensus pages 1-4).

## 3. Phenotypes (clinical + laboratory) with ontology suggestions

### 3.1 Core phenotype domains (from consensus criteria and meta-analysis)
The iMCD international consensus criteria provide a structured phenotype set (major criteria + minor criteria), which also describes common MCD clinical/lab manifestations (fajgenbaum2017internationalevidencebasedconsensus pages 27-29, fajgenbaum2017internationalevidencebasedconsensus pages 1-4).

#### Major phenotype anchors (diagnostic “major criteria” for iMCD)
- **Multicentric lymphadenopathy** (enlarged nodes >1 cm in ≥2 nodal stations) (fajgenbaum2017internationalevidencebasedconsensus pages 27-29)
- **Characteristic lymph node histopathology** within the iMCD spectrum (hypervascular/plasmacytic/mixed) (fajgenbaum2017internationalevidencebasedconsensus pages 27-29)

#### Minor clinical phenotypes (HPO suggestions)
From the iMCD consensus criteria (fajgenbaum2017internationalevidencebasedconsensus pages 27-29, fajgenbaum2017internationalevidencebasedconsensus pages 1-4):
- **Constitutional symptoms (“B symptoms”)**: fever, night sweats, weight loss, fatigue
  - HPO: *Fever* (HP:0001945), *Night sweats* (HP:0030166), *Weight loss* (HP:0001824), *Fatigue* (HP:0012378)
- **Organomegaly:** splenomegaly/hepatomegaly
  - HPO: *Splenomegaly* (HP:0001744), *Hepatomegaly* (HP:0002240)
- **Fluid accumulation:** edema/anasarca/ascites/pleural effusion
  - HPO: *Edema* (HP:0000969), *Anasarca* (HP:0007430), *Ascites* (HP:0001541), *Pleural effusion* (HP:0002202)
- **Pulmonary involvement:** lymphocytic interstitial pneumonitis
  - HPO: *Interstitial lung disease* (HP:0006530) (used as a pragmatic mapping)
- **Cutaneous vascular lesions:** eruptive cherry hemangiomatosis / violaceous papules
  - HPO: *Hemangioma* (HP:0001028), *Violaceous skin discoloration* (no exact single HPO term; may map to *Purpura* HP:0000979 depending on clinical description)

#### Minor laboratory phenotypes (HPO suggestions)
From the iMCD consensus criteria (fajgenbaum2017internationalevidencebasedconsensus pages 27-29):
- **Elevated CRP/ESR**
  - HPO: *Elevated C-reactive protein level* (HP:0011227), *Elevated erythrocyte sedimentation rate* (HP:0003565)
- **Anemia**
  - HPO: *Anemia* (HP:0001903)
- **Thrombocytopenia or thrombocytosis**
  - HPO: *Thrombocytopenia* (HP:0001873), *Thrombocytosis* (HP:0001894)
- **Hypoalbuminemia**
  - HPO: *Hypoalbuminemia* (HP:0003073)
- **Renal dysfunction / proteinuria**
  - HPO: *Proteinuria* (HP:0000093), *Renal insufficiency* (HP:0000083)
- **Polyclonal hypergammaglobulinemia**
  - HPO: *Hypergammaglobulinemia* (HP:0004313)

### 3.2 Frequency data (recent, quantitative)
A 2024 systematic review/meta-analysis (32 studies; 559 UCD, 1023 iMCD, 416 HHV8+ MCD) estimated frequencies of criteria-level features and compared iMCD vs HHV8+ MCD (Blood Advances; published online 2024-07-10; URL: https://doi.org/10.1182/bloodadvances.2024013548):
- **Constitutional symptoms:** iMCD **46.6%** vs HHV8+ MCD **98.6%** (P=.038) (hoffmann2024theclinicalpicture pages 1-2)
- **Splenomegaly:** iMCD **48.2%** vs HHV8+ MCD **89.2%** (P=.031) (hoffmann2024theclinicalpicture pages 1-2)
- **Renal dysfunction:** iMCD **36.9%** vs HHV8+ MCD **17.4%** (P=.04 before adjustment) (hoffmann2024theclinicalpicture pages 1-2)

## 4. Genetic / molecular information

### 4.1 Causal genes (germline) and inherited forms
- **No established Mendelian causal gene** is supported by the retrieved evidence for iMCD as a primary genetic disorder. Current frameworks emphasize cytokine dysregulation and exclusion of mimics rather than a defined germline etiology (fajgenbaum2017internationalevidencebasedconsensus pages 1-4).

### 4.2 Somatic genetics and clonality (especially relevant to HHV-8 MCD and transformation)
- HHV-8/KSHV-associated MCD is typically a **polyclonal lymphoproliferation**, but it can occur alongside focal clonal proliferations (“microlymphoma”) and is associated with risk of progression to HHV-8+ lymphomas (carbone2021castlemandisease pages 4-5, rigney2025areviewof pages 10-12).
- A 2024 molecular case report of HHV8-associated MCD with microlymphoma documented:
  - **Somatically hypermutated monoclonal IGH rearrangement** representing ~**4%** of the B-cell population in the lymph node, and also detected in bone marrow (rogges2024molecularfeaturesof pages 1-2, rogges2024molecularfeaturesof pages 5-6).
  - A **pathogenic KMT2D frameshift variant** plus additional VUS in **KMT2D, FOXO1, ARID1A, KMT2A** (rogges2024molecularfeaturesof pages 1-2, rogges2024molecularfeaturesof pages 5-6).
  - Interpretation that HHV-8 alone is insufficient for transformation (“additional genetic events” likely required), consistent with the notion that clonal progression is a key step in lymphomagenesis (rogges2024molecularfeaturesof pages 6-7).

## 5. Environmental information

### 5.1 Infectious agents
- **HHV-8/KSHV** is a causal infectious agent for a major MCD subtype (KSHV–MCD). The clinical presentation is dominated by systemic inflammatory symptoms and laboratory abnormalities, with infected plasmacytoid cells in lymph nodes and elevated peripheral blood viral loads (polizzotto2012clinicalmanifestationsof pages 1-2).

## 6. Mechanism / pathophysiology

### 6.1 Causal chain (overview)
1. **Upstream triggers** differ by subtype:
   - **KSHV–MCD:** KSHV infection of B-cell lineage populations with lytic activation in a subset; expression of viral products including **vIL-6**; elevated KSHV viral loads in peripheral blood (polizzotto2012clinicalmanifestationsof pages 1-2).
   - **iMCD:** unknown upstream trigger(s); consensus view is a **cytokine storm** with IL-6 often involved (fajgenbaum2017internationalevidencebasedconsensus pages 1-4).
2. **Intermediate mechanisms:** hypercytokinemia (IL-6, and in KSHV–MCD also vIL-6; often IL-10) leading to acute-phase response, cytopenias, vascular permeability/edema, and immune-cell activation (fajgenbaum2017internationalevidencebasedconsensus pages 1-4, polizzotto2012clinicalmanifestationsof pages 1-2, rigney2025areviewof pages 10-12).
3. **Downstream clinical manifestations:** constitutional symptoms, organomegaly, effusions/anasarca, organ dysfunction (kidney, lung), and risk of critical illness (cytokine storm phenotype) (fajgenbaum2017internationalevidencebasedconsensus pages 27-29, rhee2022siltuximabisassociated pages 1-2).

### 6.2 Key molecular pathways (with ontology suggestions)
- **IL-6 signaling** (core):
  - GO: *interleukin-6-mediated signaling pathway* (GO:0070102)
- **JAK/STAT** (noted as activated in MCD-related cytokine signaling; also cited in broader MCD pathway summaries) (denaro2025castlemandiseaseand pages 4-6, lossos2024idiopathicmulticentriccastleman pages 1-2).
  - GO: *JAK-STAT cascade* (GO:0007259)
- **PI3K/AKT/mTOR** (highlighted particularly in some mechanistic summaries and in iMCD-TAFRO biomarker work) (denaro2025castlemandiseaseand pages 4-6, lossos2024idiopathicmulticentriccastleman pages 1-2).
  - GO: *TOR signaling* (GO:0031929)

### 6.3 Cell types involved (CL suggestions)
- **B cells / plasmablast-lineage cells** (especially in KSHV–MCD):
  - CL: *B cell* (CL:0000236), *plasmablast* (CL:0000980)
- **Follicular dendritic cells** (histologic emphasis in iMCD spectrum):
  - CL: *follicular dendritic cell* (CL:0000449)

### 6.4 Recent mechanistic development (2024): iMCD-TAFRO endotheliopathy, immunothrombosis, and mTOR activation
A 2024 report identified candidate mechanistic biomarkers and processes in **iMCD-TAFRO**, including:
- **Marked elevation of SVEP1** (~15-fold vs controls), proposed as an **mTOR activator**; SVEP1 biology connects to **PI3K/AKT/mTOR signaling in vascular cells and platelets** (Blood Vessels, Thrombosis & Hemostasis; 2024-06; URL: https://doi.org/10.1016/j.bvth.2024.100006) (lossos2024idiopathicmulticentriccastleman pages 1-2, lossos2024idiopathicmulticentriccastleman pages 2-3).
- **Immunothrombosis/endotheliopathy signatures**, including microparticles expressing functional **tissue factor**, endothelial injury markers, complement activation, and endothelial activation markers (lossos2024idiopathicmulticentriccastleman pages 1-2).
- The authors explicitly conclude: “The findings suggest that immunothrombosis plays a role in iMCD-TAFRO.” (lossos2024idiopathicmulticentriccastleman pages 2-3).

## 7. Anatomical structures affected

### 7.1 Organ level (UBERON suggestions)
- **Lymph nodes** (UBERON:0000029) — central disease tissue (major diagnostic criterion in iMCD) (fajgenbaum2017internationalevidencebasedconsensus pages 27-29).
- **Spleen** (UBERON:0002106) and **liver** (UBERON:0002107) — organomegaly is a minor criterion; splenomegaly differs by subtype frequency (hoffmann2024theclinicalpicture pages 1-2, fajgenbaum2017internationalevidencebasedconsensus pages 27-29).
- **Kidney** (UBERON:0002113) — renal dysfunction/proteinuria is a minor criterion and differs in frequency between iMCD and HHV8+ MCD (hoffmann2024theclinicalpicture pages 1-2, fajgenbaum2017internationalevidencebasedconsensus pages 27-29).
- **Lung** (UBERON:0002048) — lymphocytic interstitial pneumonitis is a minor criterion (fajgenbaum2017internationalevidencebasedconsensus pages 27-29).

### 7.2 Tissue/cell level
- Lymph node microanatomy with germinal center regression/hyperplasia, follicular dendritic cell prominence, hypervascularization, and polytypic plasmacytosis in iMCD spectrum (fajgenbaum2017internationalevidencebasedconsensus pages 27-29).

## 8. Temporal development

### 8.1 Onset and course
- iMCD may be episodic or progressive and can range from mild to **acute multiorgan dysfunction** requiring intensive care; this is highlighted in analyses of iMCD heterogeneity and the siltuximab trial population characterization (rhee2022siltuximabisassociated pages 1-2).
- KSHV/HHV8-associated MCD can have a **relapsing–remitting** course with flares correlating with hypercytokinemia and viral load (rigney2025areviewof pages 10-12).

## 9. Inheritance and population

### 9.1 Epidemiology (statistics)
Because of rarity and coding changes, incidence estimates vary by method:
- **iMCD incidence and prevalence from US claims algorithm (MarketScan; 2017–2018):**
  - **Incidence:** **3.4 per million/year** (95% CI 1.4–9.2)
  - **Prevalence:** **6.9 per million** (95% CI 3.7–13.3)
  - Treatment patterns: 39% corticosteroid monotherapy; 33.1% no iMCD-directed treatment; 9.8% IL-6–targeted therapy; **siltuximab used in 8.7%** despite being the only FDA-approved therapy (Blood Advances; 2022-01; URL: https://doi.org/10.1182/bloodadvances.2021004441) (mukherjee2022epidemiologyandtreatment pages 1-2).
- **Castleman disease overall incidence estimates (older claims-based work; limitations emphasized):** 21–25 per million person-years with extrapolated US case counts; this work predates or is complicated by the introduction of disease-specific coding and consensus criteria (simpson2018epidemiologyofcastleman pages 1-4).

## 10. Diagnostics

### 10.1 Standardized diagnostic criteria (iMCD)
The 2017 international consensus diagnostic criteria for iMCD require:
- **Both major criteria** (histopathology + multicentric lymphadenopathy)
- **≥2 of 11 minor criteria**, including **≥1 laboratory** abnormality
- **Exclusion** of infection-associated, autoimmune/autoinflammatory, and malignant mimics (Blood; 2017-03; URL: https://doi.org/10.1182/blood-2016-10-746933) (fajgenbaum2017internationalevidencebasedconsensus pages 27-29, fajgenbaum2017internationalevidencebasedconsensus pages 1-4).

**Direct abstract quote (criteria structure):**
> “The proposed consensus criteria require both Major Criteria (characteristic lymph node histopathology and multicentric lymphadenopathy), at least 2 of 11 Minor Criteria with at least 1 laboratory abnormality, and exclusion of infectious, malignant, and autoimmune disorders that can mimic iMCD.” (fajgenbaum2017internationalevidencebasedconsensus pages 1-4)

### 10.2 Diagnostic workup and tests (real-world implementation)
A practical workup commonly includes inflammatory markers and organ function tests, virologic testing for HIV/HHV-8, and imaging (CT/PET-CT) plus excisional biopsy (hoffmann2024theclinicalpicture pages 2-3, denaro2025castlemandiseaseand pages 4-6).

**Visual evidence (tables):** The following images show a recommended diagnostic workup and the iMCD consensus criteria as reproduced in a 2024 systematic review/meta-analysis (hoffmann2024theclinicalpicture media 2c791a41, hoffmann2024theclinicalpicture media 375d262e).

### 10.3 Biomarkers
- **CRP/ESR:** part of iMCD minor criteria; CRP tracking is recommended (fajgenbaum2017internationalevidencebasedconsensus pages 27-29, fajgenbaum2017internationalevidencebasedconsensus pages 12-16).
- **IL-6 and VEGF:** included in diagnostic workup summaries (cytokine profile) and are often measured clinically; VEGF is especially relevant when evaluating POEMS overlap (hoffmann2024theclinicalpicture pages 2-3).
- **HHV-8 testing in suspected MCD:** HHV-8 qPCR (blood) and lymph node immunohistochemistry for **LANA-1** are used to classify HHV-8-associated MCD vs iMCD (hoffmann2024theclinicalpicture pages 2-3, ohemengdapaah2024theenigmaof pages 4-5).

### 10.4 Differential diagnosis (must-exclude conditions)
Consensus exclusion categories include (examples): infections such as HHV-8 and other uncontrolled infections; autoimmune diseases such as SLE/RA; malignancies including lymphoma and myeloma; and POEMS syndrome (fajgenbaum2017internationalevidencebasedconsensus pages 27-29, fajgenbaum2017internationalevidencebasedconsensus pages 29-39).

## 11. Outcomes / prognosis

### 11.1 Survival and mortality (statistics)
- A 2022 analysis of the randomized trial dataset reiterates historical poor outcomes: “35% of patients with iMCD die within 5 years of diagnosis, and 60% die within 10 years.” (Blood Advances; 2022-08; URL: https://doi.org/10.1182/bloodadvances.2022007112) (rhee2022siltuximabisassociated pages 1-2).
- A 2024 real-world European iMCD cohort (n=48) treated with siltuximab reported:
  - **Overall response rate (ORR): 71.1%** (55.3% complete response; 15.8% partial response)
  - **Estimated 3-year overall survival: 74%**
  - **Median survival: 123 months** (J Hematol; 2024-10-21 online; URL: https://doi.org/10.14740/jh1343) (jitaru2024siltuximabinidiopathic pages 1-2).
- For HHV-8-associated MCD, modern rituximab-era survival has improved substantially; a review summary reports 5-year survival ~90–92% with rituximab plus ART (rigney2025areviewof pages 12-14).

### 11.2 Complications
- **Organ dysfunction** is part of core disease definition and criteria (renal dysfunction/proteinuria; pulmonary involvement; effusions/anasarca) (fajgenbaum2017internationalevidencebasedconsensus pages 27-29).
- **Transformation risk:** HHV-8-associated MCD lesions are typically polyclonal, but monoclonal transformation (HHV-8+ DLBCL) can occur (rigney2025areviewof pages 10-12, rogges2024molecularfeaturesof pages 1-2).

## 12. Treatment

### 12.1 Pharmacotherapy (current standard practice)
- **iMCD first-line targeted therapy:** **siltuximab** (anti–IL-6 monoclonal antibody) is recommended frontline and is supported by randomized trial evidence and real-world studies (jitaru2024siltuximabinidiopathic pages 1-2, rhee2014siltuximabformulticentric pages 1-2).
  - Randomized trial (Lancet Oncology; 2014-07-18 online; URL: https://doi.org/10.1016/S1470-2045(14)70319-5): durable tumor + symptomatic responses **34%** (18/53) in siltuximab vs **0%** in placebo (rhee2014siltuximabformulticentric pages 1-2).
  - Post hoc trial analysis (Blood Advances; 2022-08; URL: https://doi.org/10.1182/bloodadvances.2022007112): PFS significantly improved; median PFS **14.5 months** (placebo) vs **not reached** (siltuximab) (rhee2022siltuximabisassociated pages 1-2).
- **HHV-8/KSHV-associated MCD:** **rituximab-based therapy** is widely regarded as first-line; ART is recommended when HIV-associated; chemo may be added for severe disease or concurrent Kaposi sarcoma (rigney2025areviewof pages 12-14, denaro2025castlemandiseaseand pages 4-6).

### 12.2 Emerging/experimental and trials (real-world implementation)
Representative clinical trials from ClinicalTrials.gov include:
- **Ruxolitinib (JAK inhibitor) for anti–IL-6–refractory iMCD:** NCT07085039 (Phase 2; open-label; recruiting; start 2025-12-18). Primary endpoint: Clinical Benefit Response at 12 months (NCT07085039 chunk 1).
- **Sirolimus (mTOR inhibitor) for anti–IL-6–refractory iMCD:** NCT03933904 (University of Pennsylvania; for patients failed/refractory/relapsed/intolerant to anti–IL-6/IL-6R therapy) (NCT03933904 chunk 2).
- **Tocilizumab for KSHV-associated MCD:** NCT01441063 (completed; identified in trial list) (ha2023arepatientswith pages 2-4).
- **Rituximab-based management in Malawi for KSHV-associated MCD:** NCT04585893 includes response definitions, safety, PROMIS Global-10 QoL, and labs (CRP, KSHV viral load) with follow-up to 24 months (NCT04585893 chunk 2).

### 12.3 Treatment outcome data (recent statistics)
- Real-world iMCD siltuximab outcomes (Greece/Romania; 2017–2022; follow-up through Oct 2023): ORR 71.1%, CR 55.3%, PR 15.8% (jitaru2024siltuximabinidiopathic pages 1-2).

### 12.4 MAXO suggestions (treatment action ontology)
- **Anti–IL-6 monoclonal antibody therapy** (siltuximab) — MAXO: *monoclonal antibody therapy* (general mapping)
- **Anti-CD20 therapy** (rituximab)
- **mTOR inhibitor therapy** (sirolimus)
- **JAK inhibitor therapy** (ruxolitinib)
- **Antiretroviral therapy** (HIV-associated disease)

## 13. Prevention

### 13.1 Primary prevention
- **No established primary prevention for iMCD** given unknown etiology (fajgenbaum2017internationalevidencebasedconsensus pages 1-4).
- For HHV-8/KSHV-associated disease, primary prevention could theoretically include **KSHV vaccination**, but this remains investigational.
  - Vaccine landscape (NPJ Vaccines; 2022-09; URL: https://doi.org/10.1038/s41541-022-00535-4): workshop consensus that KSHV is “potentially vaccine-preventable,” but “no well-developed KSHV vaccine candidates” currently exist in the excerpted evidence (casper2022kshv(hhv8)vaccine pages 1-2).

### 13.2 Secondary/tertiary prevention (monitoring and risk mitigation in immunosuppressed populations)
- **Solid organ transplant setting (2023 review):** AST guidance gives a **weak recommendation** for **donor/recipient serologic screening** in endemic regions, and targeted screening in non-endemic regions for higher-risk groups (e.g., MSM, people with HIV, injection drug users, immigrants from endemic countries). Practical barriers include lack of standardized assays and limited management algorithms (Transplant International; 2023-11; URL: https://doi.org/10.3389/ti.2023.11856) (atamna2023preventionofoncogenic pages 1-2).
- **SOT outcome observations:** severe disease treated only with immunosuppression tapering had poor outcomes, while milder disease treated with rituximab/antivirals/chemotherapy had better survival; switching to **mTOR inhibitors** is noted to help resolve KSHV-related lesions in transplant recipients (mularoni2026hhv‐8kshvinsolid pages 5-6).

## 14. Other species / natural disease
- No naturally occurring veterinary analogue of MCD was identified in the retrieved evidence.

## 15. Model organisms
- The retrieved evidence set did not include full-text excerpts with direct experimental details of specific MCD animal models (e.g., vIL-6 transgenic mice) sufficient for citation here; therefore, no model organism claims are made in this report.

---

## Expert opinion and analysis (integrated)
1. **The single most important clinical step is correct subtype classification**, because iMCD and KSHV–MCD have different primary drivers (idiopathic cytokine storm vs viral-driven hypercytokinemia) and therefore different first-line therapies (anti–IL-6 vs anti-CD20/viral management) (fajgenbaum2017internationalevidencebasedconsensus pages 1-4, rigney2025areviewof pages 12-14, denaro2025castlemandiseaseand pages 4-6).
2. **Diagnostic certainty depends on combining histopathology with clinical/laboratory context and explicit exclusion of mimics.** Consensus iMCD criteria were developed explicitly to solve the historical problem that “no standard diagnostic criteria or diagnostic biomarkers currently exist” and because of overlap with malignancy/infection/autoimmunity (fajgenbaum2017internationalevidencebasedconsensus pages 1-4).
3. **Recent mechanistic work in iMCD-TAFRO suggests a vascular/inflammatory thrombosis axis** (endotheliopathy, tissue factor, complement activation) with an mTOR-activating signal (SVEP1), providing a rational bridge from biology to use of mTOR inhibitors in refractory disease and motivating targeted trials (lossos2024idiopathicmulticentriccastleman pages 1-2, NCT03933904 chunk 2).

---

## Key URLs (selected)
- iMCD consensus diagnostic criteria (Blood, 2017-03): https://doi.org/10.1182/blood-2016-10-746933 (fajgenbaum2017internationalevidencebasedconsensus pages 1-4)
- Systematic review/meta-analysis of CD clinical picture (Blood Advances, 2024-09 issue; online 2024-07-10): https://doi.org/10.1182/bloodadvances.2024013548 (hoffmann2024theclinicalpicture pages 1-2)
- Siltuximab RCT (Lancet Oncology, 2014-07-18 online): https://doi.org/10.1016/S1470-2045(14)70319-5 (rhee2014siltuximabformulticentric pages 1-2)
- Real-world iMCD siltuximab cohort (J Hematol, 2024-10-21 online): https://doi.org/10.14740/jh1343 (jitaru2024siltuximabinidiopathic pages 1-2)
- iMCD-TAFRO SVEP1/tissue factor/endotheliopathy (Blood Vessels Thromb Hemost, 2024-06): https://doi.org/10.1016/j.bvth.2024.100006 (lossos2024idiopathicmulticentriccastleman pages 1-2)
- HHV-8 prevention in transplant recipients (Transplant International, 2023-11): https://doi.org/10.3389/ti.2023.11856 (atamna2023preventionofoncogenic pages 1-2)
- KSHV vaccine perspective (NPJ Vaccines, 2022-09): https://doi.org/10.1038/s41541-022-00535-4 (casper2022kshv(hhv8)vaccine pages 1-2)

---

## Evidence gaps / not available in retrieved sources
- **Orphanet/MeSH identifiers** were not directly retrievable from the current evidence excerpts; MONDO and ICD-10-CM identifiers are provided where supported (OpenTargets Search: Multicentric Castleman disease, simpson2018epidemiologyofcastleman pages 1-4).
- **Model organism evidence** for MCD-like disease (e.g., vIL-6 transgenic mice) was not available as citeable excerpted text in this run.
- **Large prospective registries and 2023–2024 iMCD refractory-therapy cohorts** (e.g., sirolimus retrospective series) were not available as full-text evidence in the retrieved context; only trial registry entries and mechanistic reports could be cited.


References

1. (hoffmann2024theclinicalpicture pages 1-2): Christian Hoffmann, Eric Oksenhendler, Sarah Littler, Lisa Grant, Karan Kanhai, and David C. Fajgenbaum. The clinical picture of castleman disease: a systematic review and meta-analysis. Blood Advances, 8:4924-4935, Sep 2024. URL: https://doi.org/10.1182/bloodadvances.2024013548, doi:10.1182/bloodadvances.2024013548. This article has 28 citations and is from a peer-reviewed journal.

2. (fajgenbaum2017internationalevidencebasedconsensus pages 1-4): David C. Fajgenbaum, Thomas S. Uldrick, Adam Bagg, Dale Frank, David Wu, Gordan Srkalovic, David Simpson, Amy Y. Liu, David Menke, Shanmuganathan Chandrakasan, Mary Jo Lechowicz, Raymond S. M. Wong, Sheila Pierson, Michele Paessler, Jean-François Rossi, Makoto Ide, Jason Ruth, Michael Croglio, Alexander Suarez, Vera Krymskaya, Amy Chadburn, Gisele Colleoni, Sunita Nasta, Raj Jayanthan, Christopher S. Nabel, Corey Casper, Angela Dispenzieri, Alexander Fosså, Dermot Kelleher, Razelle Kurzrock, Peter Voorhees, Ahmet Dogan, Kazuyuki Yoshizaki, Frits van Rhee, Eric Oksenhendler, Elaine S. Jaffe, Kojo S. J. Elenitoba-Johnson, and Megan S. Lim. International, evidence-based consensus diagnostic criteria for hhv-8-negative/idiopathic multicentric castleman disease. Blood, 129 12:1646-1657, Mar 2017. URL: https://doi.org/10.1182/blood-2016-10-746933, doi:10.1182/blood-2016-10-746933. This article has 753 citations and is from a highest quality peer-reviewed journal.

3. (OpenTargets Search: Multicentric Castleman disease): Open Targets Query (Multicentric Castleman disease, 13 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

4. (simpson2018epidemiologyofcastleman pages 1-4): David Simpson. Epidemiology of castleman disease. Hematology/oncology clinics of North America, 32 1:1-10, Feb 2018. URL: https://doi.org/10.1016/j.hoc.2017.09.001, doi:10.1016/j.hoc.2017.09.001. This article has 151 citations.

5. (carbone2021castlemandisease pages 1-2): Antonino Carbone, Margaret Borok, Blossom Damania, Annunziata Gloghini, Mark N. Polizzotto, Raj K. Jayanthan, David C. Fajgenbaum, and Mark Bower. Castleman disease. Nature Reviews Disease Primers, 7:1-18, Nov 2021. URL: https://doi.org/10.1038/s41572-021-00317-7, doi:10.1038/s41572-021-00317-7. This article has 238 citations.

6. (mukherjee2022epidemiologyandtreatment pages 1-2): Sudipto Mukherjee, Rabecka Martin, Brenda Sande, Jeremy S. Paige, and David C. Fajgenbaum. Epidemiology and treatment patterns of idiopathic multicentric castleman disease in the era of il-6–directed therapy. Blood Advances, 6:359-367, Jan 2022. URL: https://doi.org/10.1182/bloodadvances.2021004441, doi:10.1182/bloodadvances.2021004441. This article has 75 citations and is from a peer-reviewed journal.

7. (polizzotto2012clinicalmanifestationsof pages 1-2): Mark N. Polizzotto, Thomas S. Uldrick, Duosha Hu, and Robert Yarchoan. Clinical manifestations of kaposi sarcoma herpesvirus lytic activation: multicentric castleman disease (kshv–mcd) and the kshv inflammatory cytokine syndrome. Frontiers in Microbiology, Jan 2012. URL: https://doi.org/10.3389/fmicb.2012.00073, doi:10.3389/fmicb.2012.00073. This article has 241 citations and is from a peer-reviewed journal.

8. (fajgenbaum2018novelinsightsand pages 3-3): David C. Fajgenbaum. Novel insights and therapeutic approaches in idiopathic multicentric castleman disease. Hematology. American Society of Hematology. Education Program, 2018 1:318-325, Nov 2018. URL: https://doi.org/10.1182/asheducation-2018.1.318, doi:10.1182/asheducation-2018.1.318. This article has 179 citations.

9. (denaro2025castlemandiseaseand pages 4-6): Nerina Denaro, Lucia Brambilla, Federica Scarfì, Athanasia Tourlaki, Antonio Muscatello, Cinzia Solinas, Nicolò Rampi, Alessandra Bandera, and Ornella Garrone. Castleman disease and kaposi sarcoma: a review of the literature and a case series. Journal of Clinical Medicine, 14:6563, Sep 2025. URL: https://doi.org/10.3390/jcm14186563, doi:10.3390/jcm14186563. This article has 5 citations.

10. (rhee2022siltuximabisassociated pages 1-2): Frits van Rhee, Adam Rosenthal, Karan Kanhai, Rabecka Martin, Katherine Nishimura, Antje Hoering, and David C. Fajgenbaum. Siltuximab is associated with improved progression-free survival in idiopathic multicentric castleman disease. Blood Advances, 6:4773-4781, Aug 2022. URL: https://doi.org/10.1182/bloodadvances.2022007112, doi:10.1182/bloodadvances.2022007112. This article has 49 citations and is from a peer-reviewed journal.

11. (hoffmann2024theclinicalpicture pages 2-3): Christian Hoffmann, Eric Oksenhendler, Sarah Littler, Lisa Grant, Karan Kanhai, and David C. Fajgenbaum. The clinical picture of castleman disease: a systematic review and meta-analysis. Blood Advances, 8:4924-4935, Sep 2024. URL: https://doi.org/10.1182/bloodadvances.2024013548, doi:10.1182/bloodadvances.2024013548. This article has 28 citations and is from a peer-reviewed journal.

12. (fajgenbaum2017internationalevidencebasedconsensus pages 27-29): David C. Fajgenbaum, Thomas S. Uldrick, Adam Bagg, Dale Frank, David Wu, Gordan Srkalovic, David Simpson, Amy Y. Liu, David Menke, Shanmuganathan Chandrakasan, Mary Jo Lechowicz, Raymond S. M. Wong, Sheila Pierson, Michele Paessler, Jean-François Rossi, Makoto Ide, Jason Ruth, Michael Croglio, Alexander Suarez, Vera Krymskaya, Amy Chadburn, Gisele Colleoni, Sunita Nasta, Raj Jayanthan, Christopher S. Nabel, Corey Casper, Angela Dispenzieri, Alexander Fosså, Dermot Kelleher, Razelle Kurzrock, Peter Voorhees, Ahmet Dogan, Kazuyuki Yoshizaki, Frits van Rhee, Eric Oksenhendler, Elaine S. Jaffe, Kojo S. J. Elenitoba-Johnson, and Megan S. Lim. International, evidence-based consensus diagnostic criteria for hhv-8-negative/idiopathic multicentric castleman disease. Blood, 129 12:1646-1657, Mar 2017. URL: https://doi.org/10.1182/blood-2016-10-746933, doi:10.1182/blood-2016-10-746933. This article has 753 citations and is from a highest quality peer-reviewed journal.

13. (jitaru2024siltuximabinidiopathic pages 1-2): Ciprian Jitaru, Argyris Symeonidis, Sorina Badelita, Eirini Katodritou, Andrei Colita, Anastasia Mpanti, Anamaria Bancos, Bogdan Tigu, Petra Rotariu, Laura Urian, Ioana Rus, Delia Dima, Anca Bojan, Marc Damian, Vasiliki Labropoulou, Mihai Stefan Muresan, Despina Fotiou, Bogdan Fetica, Bobe Petrushev, Angela Dascalescu, Dimitra Dalampira, Sanda Buruiana, Catalin Constantinescu, Mihnea Zdrenghea, Meletios A. Dimopoulos, Ciprian Tomuleasa, and Evangelos Terpos. Siltuximab in idiopathic multicentric castleman disease: real-world experience. Journal of Hematology, 13:207-215, Oct 2024. URL: https://doi.org/10.14740/jh1343, doi:10.14740/jh1343. This article has 8 citations.

14. (rigney2025areviewof pages 10-12): Jamie Rigney, Kevin Zhang, Michael Greas, and Yan Liu. A review of kshv/hhv8-associated neoplasms and related lymphoproliferative lesions. Lymphatics, Jul 2025. URL: https://doi.org/10.3390/lymphatics3030020, doi:10.3390/lymphatics3030020. This article has 4 citations.

15. (estebansampedro2025castlemansdiseaseone pages 6-7): Jorge Esteban-Sampedro, Mario MartÃ­n-PortuguÃ©s, Pedro DurÃ¡n-del Campo, RomÃ¡n FernÃ¡ndez-GuÌitiÃ¡n, Jaime E. Ruiz-Becerra, and Victor Moreno-Torres. Castleman's disease: one disease, multiple etiologies. Aids Reviews, Feb 2025. URL: https://doi.org/10.24875/aidsrev.m25000079, doi:10.24875/aidsrev.m25000079. This article has 1 citations and is from a peer-reviewed journal.

16. (carbone2021castlemandisease pages 4-5): Antonino Carbone, Margaret Borok, Blossom Damania, Annunziata Gloghini, Mark N. Polizzotto, Raj K. Jayanthan, David C. Fajgenbaum, and Mark Bower. Castleman disease. Nature Reviews Disease Primers, 7:1-18, Nov 2021. URL: https://doi.org/10.1038/s41572-021-00317-7, doi:10.1038/s41572-021-00317-7. This article has 238 citations.

17. (rigney2025areviewof pages 12-14): Jamie Rigney, Kevin Zhang, Michael Greas, and Yan Liu. A review of kshv/hhv8-associated neoplasms and related lymphoproliferative lesions. Lymphatics, Jul 2025. URL: https://doi.org/10.3390/lymphatics3030020, doi:10.3390/lymphatics3030020. This article has 4 citations.

18. (NCT04585893 chunk 2):  Safety and Efficacy of Rituximab for Treatment of Multicentric Castleman Disease in Malawi. UNC Lineberger Comprehensive Cancer Center. 2021. ClinicalTrials.gov Identifier: NCT04585893

19. (fajgenbaum2017internationalevidencebasedconsensus pages 29-39): David C. Fajgenbaum, Thomas S. Uldrick, Adam Bagg, Dale Frank, David Wu, Gordan Srkalovic, David Simpson, Amy Y. Liu, David Menke, Shanmuganathan Chandrakasan, Mary Jo Lechowicz, Raymond S. M. Wong, Sheila Pierson, Michele Paessler, Jean-François Rossi, Makoto Ide, Jason Ruth, Michael Croglio, Alexander Suarez, Vera Krymskaya, Amy Chadburn, Gisele Colleoni, Sunita Nasta, Raj Jayanthan, Christopher S. Nabel, Corey Casper, Angela Dispenzieri, Alexander Fosså, Dermot Kelleher, Razelle Kurzrock, Peter Voorhees, Ahmet Dogan, Kazuyuki Yoshizaki, Frits van Rhee, Eric Oksenhendler, Elaine S. Jaffe, Kojo S. J. Elenitoba-Johnson, and Megan S. Lim. International, evidence-based consensus diagnostic criteria for hhv-8-negative/idiopathic multicentric castleman disease. Blood, 129 12:1646-1657, Mar 2017. URL: https://doi.org/10.1182/blood-2016-10-746933, doi:10.1182/blood-2016-10-746933. This article has 753 citations and is from a highest quality peer-reviewed journal.

20. (mularoni2026hhv‐8kshvinsolid pages 5-6): Alessandra Mularoni, Andrea Cona, Malgorzata Mikulska, Francesca Pecoraro, Carlotta Piazza, Elda De Vita, Giada Pietrosi, Matteo Bulati, Tiziana Lazzarotto, and Mario Luppi. Hhv‐8/kshv in solid organ transplantation: current gaps of knowledge and future directions. Transplant Infectious Disease, Jan 2026. URL: https://doi.org/10.1111/tid.70179, doi:10.1111/tid.70179. This article has 2 citations and is from a peer-reviewed journal.

21. (atamna2023preventionofoncogenic pages 1-2): Alaa Atamna, Dafna Yahav, and Cédric Hirzel. Prevention of oncogenic gammaherpesvirinae (ebv and hhv8) associated disease in solid organ transplant recipients. Transplant International, Nov 2023. URL: https://doi.org/10.3389/ti.2023.11856, doi:10.3389/ti.2023.11856. This article has 10 citations and is from a peer-reviewed journal.

22. (rogges2024molecularfeaturesof pages 1-2): Evelina Rogges, Sabrina Pelliccia, Camilla Savio, Gianluca Lopez, Irene Della Starza, Giacinto La Verde, and Arianna Di Napoli. Molecular features of hhv8 monoclonal microlymphoma associated with kaposi sarcoma and multicentric castleman disease in an hiv-negative patient. International Journal of Molecular Sciences, 25:3775, Mar 2024. URL: https://doi.org/10.3390/ijms25073775, doi:10.3390/ijms25073775. This article has 3 citations.

23. (rogges2024molecularfeaturesof pages 5-6): Evelina Rogges, Sabrina Pelliccia, Camilla Savio, Gianluca Lopez, Irene Della Starza, Giacinto La Verde, and Arianna Di Napoli. Molecular features of hhv8 monoclonal microlymphoma associated with kaposi sarcoma and multicentric castleman disease in an hiv-negative patient. International Journal of Molecular Sciences, 25:3775, Mar 2024. URL: https://doi.org/10.3390/ijms25073775, doi:10.3390/ijms25073775. This article has 3 citations.

24. (rogges2024molecularfeaturesof pages 6-7): Evelina Rogges, Sabrina Pelliccia, Camilla Savio, Gianluca Lopez, Irene Della Starza, Giacinto La Verde, and Arianna Di Napoli. Molecular features of hhv8 monoclonal microlymphoma associated with kaposi sarcoma and multicentric castleman disease in an hiv-negative patient. International Journal of Molecular Sciences, 25:3775, Mar 2024. URL: https://doi.org/10.3390/ijms25073775, doi:10.3390/ijms25073775. This article has 3 citations.

25. (lossos2024idiopathicmulticentriccastleman pages 1-2): Chen Lossos, Jenna Brown, Sara Sheikhbahaei, Anne Hubben, Sharon C. Liu, Keith R. McCrae, Shruti Chaturvedi, Rakhi P. Naik, and Ivo M.B. Francischetti. Idiopathic multicentric castleman disease - tafro results in high levels of mtor activator svep1, tissue factor, and endotheliopathy. Blood Vessels, Thrombosis &amp; Hemostasis, 1:100006, Jun 2024. URL: https://doi.org/10.1016/j.bvth.2024.100006, doi:10.1016/j.bvth.2024.100006. This article has 2 citations.

26. (lossos2024idiopathicmulticentriccastleman pages 2-3): Chen Lossos, Jenna Brown, Sara Sheikhbahaei, Anne Hubben, Sharon C. Liu, Keith R. McCrae, Shruti Chaturvedi, Rakhi P. Naik, and Ivo M.B. Francischetti. Idiopathic multicentric castleman disease - tafro results in high levels of mtor activator svep1, tissue factor, and endotheliopathy. Blood Vessels, Thrombosis &amp; Hemostasis, 1:100006, Jun 2024. URL: https://doi.org/10.1016/j.bvth.2024.100006, doi:10.1016/j.bvth.2024.100006. This article has 2 citations.

27. (hoffmann2024theclinicalpicture media 2c791a41): Christian Hoffmann, Eric Oksenhendler, Sarah Littler, Lisa Grant, Karan Kanhai, and David C. Fajgenbaum. The clinical picture of castleman disease: a systematic review and meta-analysis. Blood Advances, 8:4924-4935, Sep 2024. URL: https://doi.org/10.1182/bloodadvances.2024013548, doi:10.1182/bloodadvances.2024013548. This article has 28 citations and is from a peer-reviewed journal.

28. (hoffmann2024theclinicalpicture media 375d262e): Christian Hoffmann, Eric Oksenhendler, Sarah Littler, Lisa Grant, Karan Kanhai, and David C. Fajgenbaum. The clinical picture of castleman disease: a systematic review and meta-analysis. Blood Advances, 8:4924-4935, Sep 2024. URL: https://doi.org/10.1182/bloodadvances.2024013548, doi:10.1182/bloodadvances.2024013548. This article has 28 citations and is from a peer-reviewed journal.

29. (fajgenbaum2017internationalevidencebasedconsensus pages 12-16): David C. Fajgenbaum, Thomas S. Uldrick, Adam Bagg, Dale Frank, David Wu, Gordan Srkalovic, David Simpson, Amy Y. Liu, David Menke, Shanmuganathan Chandrakasan, Mary Jo Lechowicz, Raymond S. M. Wong, Sheila Pierson, Michele Paessler, Jean-François Rossi, Makoto Ide, Jason Ruth, Michael Croglio, Alexander Suarez, Vera Krymskaya, Amy Chadburn, Gisele Colleoni, Sunita Nasta, Raj Jayanthan, Christopher S. Nabel, Corey Casper, Angela Dispenzieri, Alexander Fosså, Dermot Kelleher, Razelle Kurzrock, Peter Voorhees, Ahmet Dogan, Kazuyuki Yoshizaki, Frits van Rhee, Eric Oksenhendler, Elaine S. Jaffe, Kojo S. J. Elenitoba-Johnson, and Megan S. Lim. International, evidence-based consensus diagnostic criteria for hhv-8-negative/idiopathic multicentric castleman disease. Blood, 129 12:1646-1657, Mar 2017. URL: https://doi.org/10.1182/blood-2016-10-746933, doi:10.1182/blood-2016-10-746933. This article has 753 citations and is from a highest quality peer-reviewed journal.

30. (ohemengdapaah2024theenigmaof pages 4-5): Jessica Ohemeng-Dapaah, Afoma Onyechi, Ayesha Kang, Alexandre Lacasse, and Jyotsana Sinha. The enigma of idiopathic multicentric castleman disease: an elusive diagnosis. Cureus, Nov 2024. URL: https://doi.org/10.7759/cureus.73156, doi:10.7759/cureus.73156. This article has 0 citations.

31. (rhee2014siltuximabformulticentric pages 1-2): Frits van Rhee, Raymond S Wong, Nikhil Munshi, Jean-Francois Rossi, Xiao-Yan Ke, Alexander Fosså, David Simpson, Marcelo Capra, Ting Liu, Ruey Kuen Hsieh, Yeow Tee Goh, Jun Zhu, Seok-Goo Cho, Hanyun Ren, James Cavet, Rajesh Bandekar, Margaret Rothman, Thomas A Puchalski, Manjula Reddy, Helgi van de Velde, Jessica Vermeulen, and Corey Casper. Siltuximab for multicentric castleman's disease: a randomised, double-blind, placebo-controlled trial. The Lancet. Oncology, 15 9:966-74, Aug 2014. URL: https://doi.org/10.1016/s1470-2045(14)70319-5, doi:10.1016/s1470-2045(14)70319-5. This article has 562 citations.

32. (NCT07085039 chunk 1):  Ruxolitinib in Previously Treated Idiopathic Multicentric Castleman Disease. University of Pennsylvania. 2025. ClinicalTrials.gov Identifier: NCT07085039

33. (NCT03933904 chunk 2):  Sirolimus in Previously Treated Idiopathic Multicentric Castleman Disease. University of Pennsylvania. 2019. ClinicalTrials.gov Identifier: NCT03933904

34. (ha2023arepatientswith pages 2-4): Gavin Ha, Kelsey Kwong, Bryce Tanaka, Yoshito Nishimura, and Christina Chong. Are patients with hhv-8 associated castleman disease successfully treated with rituximab at risk of subsequently developing hhv-8 negative (idiopathic) castleman disease? European Journal of Case Reports in Internal Medicine, Jun 2023. URL: https://doi.org/10.12890/2023\_003904, doi:10.12890/2023\_003904. This article has 0 citations.

35. (casper2022kshv(hhv8)vaccine pages 1-2): Corey Casper, Lawrence Corey, Jeffrey I. Cohen, Blossom Damania, Anne A. Gershon, David C. Kaslow, Laurie T. Krug, Jeffrey Martin, Sam M. Mbulaiteye, Edward S. Mocarski, Patrick S. Moore, Javier Gordon Ogembo, Warren Phipps, Denise Whitby, and Charles Wood. Kshv (hhv8) vaccine: promises and potential pitfalls for a new anti-cancer vaccine. NPJ Vaccines, Sep 2022. URL: https://doi.org/10.1038/s41541-022-00535-4, doi:10.1038/s41541-022-00535-4. This article has 58 citations and is from a peer-reviewed journal.
