---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-10T14:46:21.177298'
end_time: '2026-05-10T15:01:10.953148'
duration_seconds: 889.78
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Combined Pituitary Hormone Deficiencies, Genetic Form
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 39
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Combined Pituitary Hormone Deficiencies, Genetic Form
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Combined Pituitary Hormone Deficiencies, Genetic Form** covering all of the
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
- **Disease Name:** Combined Pituitary Hormone Deficiencies, Genetic Form
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Combined Pituitary Hormone Deficiencies, Genetic Form** covering all of the
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


## Combined Pituitary Hormone Deficiencies, Genetic Form (congenital/genetic CPHD/MPHD): Comprehensive Research Report

### Target disease and scope
This entry covers **congenital/genetic combined pituitary hormone deficiency (CPHD)** / **multiple pituitary hormone deficiency (MPHD)**—a Mendelian/monogenic-leaning but genetically heterogeneous set of disorders characterized by **deficiency of ≥2 pituitary hormones**, typically beginning in infancy/childhood and sometimes accompanied by **midline brain/pituitary structural anomalies** and **extrapituitary syndromic features**. Evidence below is primarily from **aggregated disease-level resources** (reviews, cohorts) and **individual/family case-based genetic discovery** studies rather than EHR-only phenotyping. (lee2024clinicalandgenetic pages 1-2, plachy2024etiologyofcombined pages 2-3)

### Key identifiers (limitations)
* **MONDO ID:** not retrieved in the accessible full texts used here.
* **Orphanet/ORPHA ID:** not retrieved in the accessible full texts used here.
* **OMIM identifiers:** gene-level OMIM IDs are referenced in some sources, but comprehensive OMIM disease-number crosswalks for “CPHD genetic form” were not extractable from the retrieved evidence corpus.
* **ICD-10/ICD-11 / MeSH:** not retrieved in the accessible full texts used here.

### Common synonyms and alternative names
* Combined pituitary hormone deficiency (CPHD) (plachy2024etiologyofcombined pages 2-3, lee2024clinicalandgenetic pages 1-2)
* Congenital combined pituitary hormone deficiency (cCPHD) (lee2024clinicalandgenetic pages 1-2)
* Multiple pituitary hormone deficiency (MPHD) (tuz2023longtermfollowupdata pages 9-9, santoro2025anovelmissense pages 1-2)
* Congenital hypopituitarism (CH) / congenital hypopituitarism with CPHD (aguilarriera2025progressionfromisolated pages 1-2, martinezmayer2024knockoutmicewith pages 1-2)
* Pituitary stalk interruption syndrome (PSIS) is a frequent *radiologic syndrome* overlapping with congenital hypopituitarism/CPHD rather than a synonym (lee2024clinicalandgenetic pages 1-2)

---

## 1) Disease information (overview; current understanding)
**Definition (clinical concept):**
* A 2024 Korean cohort defines cCPHD as **“the nonacquired deficiency of more than one hormone produced by the anterior pituitary gland or released from the posterior pituitary gland.”** (Lee et al., *Ann Pediatr Endocrinol Metab*, 2024-12, https://doi.org/10.6065/apem.2448008.004) (lee2024clinicalandgenetic pages 1-2)
* A 2024 Czech cohort operationalizes congenital CPHD as **“GHD associated with a deficit of at least one other pituitary hormone”**, providing explicit biochemical cutoffs for several axes. (Plachy et al., *Endocrine Connections*, 2024-07, https://doi.org/10.1530/ec-24-0217) (plachy2024etiologyofcombined pages 2-3)

**Diagnostic framing:** Genetic CPHD is not a single-gene disease; it is a spectrum caused by disruption of pituitary/hypothalamic development genes and, in some cases, broader syndromic genes. A 2024 Genome Medicine study notes: **“Variants in 67 genes are associated with CH, but a vast majority of CH cases lack a genetic diagnosis.”** (Martinez‑Mayer et al., *Genome Medicine*, 2024-05, https://doi.org/10.1186/s13073-024-01347-y) (martinezmayer2024knockoutmicewith pages 1-2)

---

## 2) Etiology
### 2.1 Disease causal factors
**Primary causal factor:** germline genetic variants impacting hypothalamo–pituitary development, pituitary lineage specification, or hypothalamic signaling; less often chromosomal abnormalities (e.g., microdeletions). (plachy2024etiologyofcombined pages 2-3)

**Operational etiologic categories used clinically:**
1) **Transcription factor/lineage genes** (e.g., PROP1, POU1F1, HESX1, LHX3/LHX4) (nguyen2025identificationofpou1f1 pages 2-4, lee2024clinicalandgenetic pages 1-2)
2) **Signaling / morphogen pathway genes** (e.g., GLI2/SHH-related, FGFR1/FGF8-related) often with midline anomalies (arzilli2025diagnosticchallengesof pages 7-8, arzilli2025diagnosticchallengesof pages 8-10)
3) **Chromatin/epigenetic regulators and other pathways (newer)** revealed by mouse-to-human discovery (e.g., SETD5, MORC2) (martinezmayer2024knockoutmicewith pages 15-17)
4) **Chromosomal CNVs/microdeletions** can underlie some congenital hypopituitarism presentations (example: 14q microdeletion involving OTX2) (plachy2024etiologyofcombined pages 1-2)

### 2.2 Risk factors
**Genetic/familial risk:** family history, consanguinity, and known pathogenic variants in CPHD genes. Some genes show incomplete penetrance and oligogenicity in congenital pituitary malformations (e.g., GLI2 variants inherited from unaffected parents) (santoro2025anovelmissense pages 1-2).

**Non-genetic risk factors:** For the specifically *genetic form*, robust environmental risk factors are not well-established in the evidence retrieved here.

### 2.3 Protective factors and gene–environment interactions
No protective alleles or gene–environment interactions were directly extractable from the retrieved corpus.

---

## 3) Phenotypes (clinical spectrum; HPO suggestions)
### 3.1 Core endocrine phenotypes
Most individuals have **GH deficiency** as a prominent or earliest deficit; additional deficits accumulate variably.

**Korean congenital CPHD cohort (n=43):**
* **GHD:** 42/43 (97.7%) (lee2024clinicalandgenetic pages 1-2)
* **≥3 hormone deficiencies:** 33/43 (76.7%) (lee2024clinicalandgenetic pages 1-2)
* **Extrapituitary phenotypes:** 31/43 (72.1%) (lee2024clinicalandgenetic pages 1-2)

**Long-term MPHD cohort (n=45; admission frequencies):**
* GH deficiency 88.9%, TSH deficiency 77.8%, ACTH deficiency 33.3%, FSH/LH deficiency 22.2%, PRL deficiency 17.8%; and **62%** developed additional deficits during follow-up. (Tuz et al., *Andes Pediatrica*, 2023-12, https://doi.org/10.32641/andespediatr.v94i6.4680) (tuz2023longtermfollowupdata pages 9-9)

**HPO term suggestions (non-exhaustive):**
* Growth hormone deficiency: **HP:0000824**
* Central hypothyroidism: **HP:0000852**
* Secondary adrenal insufficiency (ACTH deficiency): **HP:0000846**
* Hypogonadotropic hypogonadism: **HP:0000044**
* Prolactin deficiency / hypoprolactinemia: **HP:0000934** (often catalogued as hypoprolactinemia)
* Diabetes insipidus (central): **HP:0000869**

### 3.2 Presenting features and age of onset
* In Lee et al. 2024, the **mean age at diagnosis** was 3.2 years and **41.9%** were diagnosed at <1 year. Short stature was the most frequent initial presentation (37.2%), but >50% had neonatal features suggestive of hypopituitarism. (lee2024clinicalandgenetic pages 1-2)

**HPO suggestions for neonatal presentations:**
* Neonatal hypoglycemia: **HP:0001998** (supported as a neonatal feature in congenital GHD/CPHD reviews) (stagi2023managementofneonatal pages 10-11)
* Micropenis: **HP:0000054** (stagi2023managementofneonatal pages 10-11)
* Neonatal cholestasis: **HP:0006550** (stagi2023managementofneonatal pages 10-11)

### 3.3 MRI/neuroanatomical phenotypes
* Lee et al. 2024 reports **brain MRI abnormalities in 80.5%** of congenital cases, correlating with more hormone deficiencies. (lee2024clinicalandgenetic pages 1-2)
* PSIS definition: **“a combination of hypoplasia or aplasia of the anterior pituitary gland, ectopic pituitary gland, and a thin stalk.”** (lee2024clinicalandgenetic pages 1-2)

**HPO suggestions:**
* Pituitary hypoplasia: **HP:0000835**
* Ectopic posterior pituitary: **HP:0006827**
* Absent/thin pituitary stalk: **HP:0000866**
* Septo-optic dysplasia: **HP:0000600**

### 3.4 Quality-of-life (QoL)
Direct disease-specific QoL measures for congenital genetic CPHD were not extractable in the retrieved evidence. However, updated clinical reviews emphasize that appropriate hormone replacement “significantly” improves QoL in hypopituitarism broadly. (Iglesias 2024) (iglesias2024anupdateon pages 15-16)

---

## 4) Genetic / molecular information
### 4.1 Causal genes (high-level)
**Known gene set size:** Martinez‑Mayer et al. (2024) states **67 genes** associated with congenital hypopituitarism as of 2023. (martinezmayer2024knockoutmicewith pages 1-2)

**Examples of repeatedly implicated CPHD genes (not exhaustive):**
* **PROP1, POU1F1, HESX1, LHX3, LHX4, OTX2, GLI2, SOX3** (nguyen2025identificationofpou1f1 pages 2-4)
* Additional candidates and broader etiologic gene lists for CPHD/CH include genes in cilia, axon guidance, chromatin regulation, and hypothalamic signaling (arzilli2025diagnosticchallengesof pages 8-10, martinezmayer2024knockoutmicewith pages 10-12).

A visual gene compendium is available in Martinez‑Mayer et al. 2024 **Table 1 (≈70 genes)** listing “Human genes implicated in hypothalamic-pituitary abnormalities.” (martinezmayer2024knockoutmicewith media 20fb156a, martinezmayer2024knockoutmicewith media 13ff31db, martinezmayer2024knockoutmicewith media 471988ef, martinezmayer2024knockoutmicewith media 9f0cb61f)

### 4.2 Inheritance patterns
Inheritance is gene-dependent:
* **POU1F1** can be autosomal dominant (heterozygous) or autosomal recessive (biallelic): Nguyen et al. notes **“heterozygous mutations, representing the autosomal dominant form”** vs **“homozygous or compound heterozygous mutations… inherited in an autosomal recessive manner.”** (Nguyen et al., 2025-03, https://doi.org/10.3390/ijms26062406) (nguyen2025identificationofpou1f1 pages 2-4)
* **PROP1** is typically recessive; a 2024 pediatric cohort provides examples of homozygous and compound heterozygous PROP1 genotypes. (zygmuntgorska2024comparisonofclinical pages 4-6)
* **GLI2** shows incomplete penetrance in ectopic posterior pituitary / PSIS contexts. (santoro2025anovelmissense pages 1-2)

### 4.3 Genotype–phenotype correlations (example: PROP1 vs non-PROP1)
A 2024 cohort directly compares PROP1-CPHD with non-PROP1 etiologies:
* PROP1 group had **lower baseline TSH** and **markedly lower prolactin** (TSH 1.8 vs 2.4 µIU/mL; PRL 128 vs 416.3 µIU/mL) and less frequent neonatal hypoglycemia than non-PROP1 (0 vs 16%). (Zygmunt‑Górska et al., *Hormones*, 2024-12, https://doi.org/10.1007/s42000-023-00510-1) (zygmuntgorska2024comparisonofclinical pages 1-2, zygmuntgorska2024comparisonofclinical pages 4-6)
* Secondary adrenal insufficiency was less frequent and later in PROP1 (age 13.4 vs 10.4 years). (zygmuntgorska2024comparisonofclinical pages 1-2)
* MRI in PROP1 can be variable (small pituitary, enlargement, occasional stalk interruption/ectopy, or normal). (zygmuntgorska2024comparisonofclinical pages 1-2)

### 4.4 Variant types and interpretation
CPHD involves diverse variant classes (frameshift, splice, missense, CNVs). In Plachy et al. 2024, variants were evaluated using ACMG standards and a chromosomal aberration (14q microdeletion involving OTX2) was among solved cases. (plachy2024etiologyofcombined pages 1-2)

**Population allele frequencies / carrier frequencies:** not extractable from the retrieved evidence (gnomAD-level frequencies not available in the corpus).

---

## 5) Environmental information
For the genetic form, specific non-genetic environmental contributors are not established in the retrieved evidence.

---

## 6) Mechanism / pathophysiology
### 6.1 Conceptual causal chain (upstream → downstream)
**Upstream:** germline disruption of pituitary organogenesis and lineage specification genes (transcription factors, signaling, chromatin) →
**Midstream:** abnormal pituitary morphogenesis (hypoplasia, stalk interruption, ectopic posterior pituitary) and/or selective failure of endocrine cell differentiation (somatotroph, thyrotroph, lactotroph, gonadotroph, corticotroph) →
**Downstream:** combined hormone deficits (GH, TSH, ACTH, LH/FSH, PRL ± AVP) → clinical manifestations such as growth failure, neonatal hypoglycemia, micropenis/cryptorchidism, central hypothyroidism, adrenal crisis risk, pubertal failure, and DI.

**Evidence for developmental-stage effect:** Lee et al. emphasizes that **“mutations in the late stages of pituitary development cause only hormonal defects”**, whereas earlier perturbations can cause hormonal and extrapituitary defects. (lee2024clinicalandgenetic pages 1-2)

### 6.2 Newly emphasized pathways (2023–2024 research)
Martinez‑Mayer et al. (2024) used embryonic lethal IMPC/DMDD mouse lines to discover candidate genes and pathways:
* Screened 209 knockout lines and found 51 with embryonic pituitary malformations (martinezmayer2024knockoutmicewith pages 4-6)
* Found functional enrichment clusters including **ciliary function, amino acid metabolism, and epigenetics** (martinezmayer2024knockoutmicewith pages 15-17)
* Highlighted **serine–glycine/one-carbon metabolism** genes (e.g., PSAT1/PSPH/GLDC) as newly enriched in candidate sets (martinezmayer2024knockoutmicewith pages 10-12, martinezmayer2024knockoutmicewith pages 18-21)

### 6.3 GO / CL suggestions
**GO Biological Process suggestions:**
* Pituitary gland development (GO:0021983)
* Endocrine pancreas development is not relevant; instead consider endocrine system development (GO:0035270)
* Cilium organization (GO:0044782) for cilia-enriched candidate sets (martinezmayer2024knockoutmicewith pages 10-12)
* Chromatin organization (GO:0006325) / regulation of transcription (GO:0006355) for epigenetic clusters (martinezmayer2024knockoutmicewith pages 10-12)
* Serine biosynthetic process (GO:0006564) / one-carbon metabolic process (GO:0006730) for the metabolic cluster (martinezmayer2024knockoutmicewith pages 18-21)

**CL (cell types) suggestions:**
* Somatotroph (CL:0000826)
* Thyrotroph (CL:0002412)
* Lactotroph (CL:0000665)
* Gonadotroph (CL:0000592)
* Corticotroph (CL:0002406)

---

## 7) Anatomical structures affected
**Primary:** pituitary gland (anterior pituitary and posterior pituitary/neurohypophysis) and hypothalamic–pituitary axis (lee2024clinicalandgenetic pages 1-2, plachy2024etiologyofcombined pages 2-3).

**UBERON suggestions:**
* Pituitary gland: UBERON:0000007
* Anterior pituitary: UBERON:0001983
* Posterior pituitary: UBERON:0001984
* Hypothalamus: UBERON:0001898

**Subcellular (GO CC) suggestions (mechanism-dependent):** primary cilium (GO:0005929) for cilia-associated candidate mechanisms (martinezmayer2024knockoutmicewith pages 10-12).

---

## 8) Temporal development
**Onset:** often congenital/neonatal or early childhood. In Lee et al. 2024, ~42% diagnosed <1 year; >50% had neonatal features but not all were diagnosed in infancy. (lee2024clinicalandgenetic pages 1-2)

**Progression:** hormone deficits may accrue over time. In Tuz et al. 2023, 62% developed additional deficiencies during follow-up. (tuz2023longtermfollowupdata pages 9-9)

---

## 9) Inheritance and population
### 9.1 Epidemiology
Available estimates (heterogeneous definitions):
* CH incidence reported as **1 per 3,000–10,000 live births** in a pediatric MRI-abnormality cohort paper (Aguilar‑Riera et al., 2025-07, https://doi.org/10.1186/s12902-025-01980-7). (aguilarriera2025progressionfromisolated pages 1-2)
* MPHD prevalence estimated at **~1/8,000 worldwide** (Tuz et al., 2023-12). (tuz2023longtermfollowupdata pages 9-9)

### 9.2 Penetrance/expressivity
Incomplete penetrance is highlighted for some variants (e.g., GLI2) and variable expressivity is common across CPHD genes. (santoro2025anovelmissense pages 1-2)

### 9.3 Founder effects / carrier frequency / sex ratio
Not extractable from the retrieved evidence.

---

## 10) Diagnostics (current practice; real-world implementation)
### 10.1 Core clinical and biochemical testing
Diagnosis is based on clinical suspicion plus endocrine testing to identify deficient axes. A practical congenital CPHD definition used by Plachy et al. includes:
* IGF‑1 <0 SDS and stimulated GH <10 µg/L (their cutoff) (plachy2024etiologyofcombined pages 2-3)
* Central hypothyroidism: low free T4 with inappropriately low/normal TSH (plachy2024etiologyofcombined pages 2-3)

**LOINC suggestions (examples; local labs differ):**
* IGF-1 in Serum/Plasma (commonly LOINC 14159-1)
* Cortisol (e.g., 2143-6)
* Free T4 (e.g., 3024-7)
* Prolactin (e.g., 2842-3)

### 10.2 Imaging
MRI is strongly emphasized when hypopituitarism is documented: **“All patients with documented hypopituitarism warrant an MRI.”** (Gan et al., 2019, Brook’s Clinical Pediatric Endocrinology, https://doi.org/10.1002/9781119152712.ch5) (gan2019disordersofhypothalamo‐pituitary pages 40-42)

### 10.3 Genetic testing strategy
Evidence from cohorts indicates modest diagnostic yield even with modern sequencing:
* Lee et al. 2024: pathogenic variants in 5/26 tested (19.2%) using targeted panel/WES (lee2024clinicalandgenetic pages 1-2)
* Plachy et al. 2024: solved 7/34 (21%) with tiered testing and NGS panel (plachy2024etiologyofcombined pages 1-2)
* Review-level statement: Sanger-based approaches historically <15% yield; NGS can increase yield toward ~19% (nguyen2025identificationofpou1f1 pages 2-4)

### 10.4 Differential diagnosis
Not fully developed in the accessible evidence corpus; in practice includes acquired hypopituitarism, pituitary tumors, infiltrative lesions, traumatic brain injury, and syndromic neurodevelopmental disorders where pituitary deficits are secondary.

---

## 11) Outcomes / prognosis
Direct survival estimates for congenital genetic CPHD were not extractable from the retrieved evidence. Available longitudinal cohort evidence emphasizes that:
* Additional hormone deficits may develop years after initial diagnosis, necessitating long-term monitoring (tuz2023longtermfollowupdata pages 9-9)
* Appropriate replacement mitigates morbidity; neonatal/childhood management focuses on preventing hypoglycemia/adrenal crisis and optimizing growth/development (stagi2023managementofneonatal pages 10-11)

---

## 12) Treatment (standard of care; real-world use)
Treatment is predominantly **hormone replacement**, tailored to which axes are deficient.

### 12.1 Glucocorticoid replacement (central adrenal insufficiency)
Neonatal/infant management review provides explicit dosing and emergency instructions:
* Maintenance hydrocortisone: **9–12 mg/m²/day** divided into 3–4 doses (stagi2023managementofneonatal pages 10-11)
* Emergency IM hydrocortisone: **25 mg (<1 year), 25–50 mg (1–5 years), 100 mg (>5 years)** (stagi2023managementofneonatal pages 10-11)

A broader updated adult hypopituitarism management review also details stress dosing protocols (e.g., high-dose IV regimens in crisis) and notes modified-release hydrocortisone options. (Iglesias 2024-10, https://doi.org/10.3390/jcm13206161) (iglesias2024anupdateon pages 15-16)

**Clinical pearl:** ACTH deficiency may mask diabetes insipidus until glucocorticoids are started; thus DI can “appear” after starting hydrocortisone, requiring close fluid/electrolyte monitoring. (stagi2023managementofneonatal pages 10-11, gan2019disordersofhypothalamo‐pituitary pages 40-42)

### 12.2 Thyroid hormone replacement (central hypothyroidism)
Levothyroxine is standard; dosing is titrated by free T4 rather than TSH in central hypothyroidism (gan2019disordersofhypothalamo‐pituitary pages 40-42, iglesias2024anupdateon pages 15-16).

### 12.3 GH replacement
Early rhGH therapy is emphasized in neonatal/early-life disease:
* Proposed neonatal dosing in one review: **25–50 µg/kg/day** during the first year (Stagi et al., 2023-06, https://doi.org/10.3390/ijms241210114) (stagi2023managementofneonatal pages 10-11)

Real-world safety/implementation (from cited observational data summarized in a CPHD genetics paper): adverse events reported in 14.4% of treated patients; discontinuation for adverse events 1.6%; common events included headache (0.4%) and scoliosis (0.2%). (nguyen2025identificationofpou1f1 pages 2-4)

### 12.4 Gonadal axis and micropenis/cryptorchidism (selected cases)
Neonatal androgen therapy options include testosterone IM or topical DHT; orchidopexy ideally by ~18 months for cryptorchidism. (stagi2023managementofneonatal pages 10-11)

### 12.5 AVP deficiency (central diabetes insipidus)
Desmopressin is used with careful titration and attention to osmolality and thirst/adipsia issues. (gan2019disordersofhypothalamo‐pituitary pages 40-42, iglesias2024anupdateon pages 15-16)

### 12.6 MAXO suggestions (management actions)
* Hormone replacement therapy: **MAXO:0000058** (general)
* Growth hormone therapy: **MAXO:0000424** (if available in your MAXO version)
* Hydrocortisone therapy / glucocorticoid replacement: map under hormone replacement
* Levothyroxine therapy: map under hormone replacement
* Desmopressin therapy: map under pharmacotherapy
* Pituitary MRI: map under diagnostic imaging

### 12.7 Advanced therapeutics / gene therapy
No interventional gene-therapy trials specific to genetic CPHD were identified in the clinical trial search results available here.

---

## 13) Prevention
Primary prevention is not established for most genetic CPHD. Secondary/tertiary prevention focuses on:
* Early recognition of neonatal features (hypoglycemia, cholestasis, micropenis) and urgent management (stagi2023managementofneonatal pages 10-11, lee2024clinicalandgenetic pages 1-2)
* Genetic counseling for families with identified pathogenic variants

---

## 14) Other species / natural disease
Not systematically retrievable from the available evidence corpus.

---

## 15) Model organisms
Martinez‑Mayer et al. (2024) demonstrates a scalable model-organism approach: screening embryonic lethal/sub-viable mouse knockouts for pituitary malformations. They report **51/209** knockout lines with embryonic pituitary defects and demonstrate translation to human candidates (MORC2 and SETD5). (martinezmayer2024knockoutmicewith pages 4-6, martinezmayer2024knockoutmicewith pages 15-17, martinezmayer2024knockoutmicewith pages 1-2)

---

## Key 2023–2024 developments (prioritized)
1) **2024 cohort quantification of congenital CPHD burden and phenotype:** high rates of MRI abnormalities (80.5%), high neonatal feature frequency (53.5%), and frequent extrapituitary phenotypes (72.1%) in a tertiary-center congenital cohort. (Lee 2024) (lee2024clinicalandgenetic pages 1-2)
2) **2024 candidate-gene expansion via IMPC/DMDD mouse phenomics:** discovery of 51 pituitary-malformation genes from embryonic lethal screens, highlighting cilia, epigenetic regulation, and serine–glycine metabolism as candidate pathway classes. (Martinez‑Mayer 2024) (martinezmayer2024knockoutmicewith pages 10-12, martinezmayer2024knockoutmicewith pages 4-6)
3) **2024 identification of potential new CPHD candidate gene GNAO1** in a congenital CPHD cohort with ACMG-classified variants and midline MRI defects. (Plachy 2024) (plachy2024etiologyofcombined pages 1-2)
4) **2024 PROP1 vs non-PROP1 phenotype differences** that may guide targeted genetic workup and anticipate late ACTH deficiency. (Zygmunt‑Górska 2024) (zygmuntgorska2024comparisonofclinical pages 1-2, zygmuntgorska2024comparisonofclinical pages 4-6)

---

## Evidence synthesis table
| Study | Year | Journal | URL | Core definition / diagnostic criteria | Key genes implicated / inheritance notes | Common phenotypes / MRI findings | Key epidemiology / diagnostic yield / numeric data | Citation |
|---|---:|---|---|---|---|---|---|---|
| Lee et al. | 2024 | *Annals of Pediatric Endocrinology & Metabolism* | https://doi.org/10.6065/apem.2448008.004 | cCPHD defined as nonacquired deficiency of >1 pituitary hormone; diagnosis anchored to time of first hormone deficiency identification | Cohort pathogenic variants in **POU1F1, GLI2, HESX1, TBC1D32, ROBO1**; developmental-stage concept noted: earlier genes more often syndromic, later genes more often hormone-limited | Initial presentation: short stature **37.2%**; neonatal hypopituitarism features **53.5%**; GHD **97.7%**; >=3 hormone deficits **76.7%**; extrapituitary phenotypes **72.1%**; brain MRI abnormalities **80.5%**; PSIS defined as anterior pituitary hypoplasia/aplasia + ectopic posterior pituitary + thin stalk | 444 CPHD records screened; 43 congenital cases included; genetic diagnosis in tested subset **5/26 (19.2%)**; prior literature cited genetic abnormality rate **1.3%–7.3%** | (lee2024clinicalandgenetic pages 1-2) |
| Plachy et al. | 2024 | *Endocrine Connections* | https://doi.org/10.1530/ec-24-0217 | CPHD defined as **GHD + at least one other pituitary hormone deficit**; GHD supported by low IGF-1 and stimulated GH **<10 µg/L**; central hypothyroidism = low free T4 with inappropriately low/normal TSH; explicit criteria provided for central adrenal insufficiency, HH, and DI | Confirmed causes included **OTX2** 14q microdeletion and variants in **GLI2, PROP1, POU1F1, TBX3, PMM2, GNAO1**; **GNAO1** proposed as novel candidate; inheritance not detailed in excerpt | In 34 children: central adrenal insufficiency **30/34**; central hypothyroidism **27/34**; hypogonadotropic hypogonadism **10/34**; central DI **3/34**; midline MRI defect **26/34** | Genetic etiology solved in **7/34 (21%)**; authors note reported molecular detection rates across studies **0%–65%**; >**80%** of congenital CPHD cases still lack molecular diagnosis; PROP1 only **1/34 (3%)** in this cohort | (plachy2024etiologyofcombined pages 1-2, plachy2024etiologyofcombined pages 2-3) |
| Stagi et al. | 2023 | *International Journal of Molecular Sciences* | https://doi.org/10.3390/ijms241210114 | Review of neonatal isolated/combined GHD; diagnosis should rely on laboratory assessment of GH and other pituitary hormones rather than MRI alone; early replacement emphasized | Genes highlighted include **HESX1, LHX3, LHX4, SOX2, SOX3, GLI2, OTX2, PROP1, POU1F1**; early-development genes more often syndromic, later-stage genes often produce endocrine-only phenotypes | Neonatal clues: hypoglycemia, cholestasis, micropenis; cortisol deficiency can mask DI; DI may emerge after glucocorticoid treatment | Congenital GHD described as rare and more often part of multiple pituitary hormone deficiency; treatment details include rhGH **25–50 µg/kg/day** in first year; hydrocortisone maintenance **9–12 mg/m2/day**; emergency IM hydrocortisone: **25 mg** (<1 y), **25–50 mg** (1–5 y), **100 mg** (>5 y) | (stagi2023managementofneonatal pages 10-11) |
| Tuz et al. | 2023 | *Andes Pediatrica* | https://doi.org/10.32641/andespediatr.v94i6.4680 | MPHD defined as deficiency of **>=2 pituitary hormones** | Gene-level data not emphasized in excerpt | At admission: GH deficiency **88.9%**, TSH deficiency **77.8%**, ACTH deficiency **33.3%**, FSH/LH deficiency **22.2%**, PRL deficiency **17.8%**; additional deficits accrued over follow-up | Prevalence estimated at **~1/8,000 worldwide**; 45 patients; mean age at presentation **5.6 ± 3.9 y**; mean follow-up **9.18 ± 3.6 y**; **62%** developed additional hormonal deficiencies during follow-up | (tuz2023longtermfollowupdata pages 9-9) |
| Aguilar-Riera et al. | 2025 | *BMC Endocrine Disorders* | https://doi.org/10.1186/s12902-025-01980-7 | CH defined as deficiency of one or more pituitary hormones due to fetal developmental events; CPHD = **>=2 pituitary deficiencies**; GHD in study defined by dynamic GH test **<7.4 ng/mL** plus short stature context | Broad developmental gene list provided: early genes (**HESX1, SOX2/3, PITX1/2, OTX2, RAX, LHX3/4, GLI2, PAX6, BMP4, FGFR1** etc.) and later genes (**POU1F1, PROP1, GH1, GHRHR, TBX19, POMC** etc.); one cohort patient had pathogenic **GLI2** variant | MRI syndromes/features highlighted: **PSIS, septo-optic dysplasia, holoprosencephaly, anterior pituitary hypoplasia**; progression from isolated GHD to CPHD documented, with TSH deficiency most frequent additional deficit | CH incidence stated as **1 per 3,000–10,000 live births**; in cohort, CPHD emerged after about **5 years** on average; among those progressing, TSH deficiency **80%**, then gonadotropins, with ACTH and AVP less frequent | (aguilarriera2025progressionfromisolated pages 1-2) |
| Nguyen et al. | 2025 | *International Journal of Molecular Sciences* | https://doi.org/10.3390/ijms26062406 | CPHD/MPHD described as disorders where pathogenic variants in pituitary-development genes cause deficiency of one or more pituitary hormones; POU1F1-associated disease often involves GH, PRL, TSH deficits and anterior pituitary hypoplasia | States **~70 genes** linked to hypopituitarism; **PROP1** is most common, accounting for up to **55%** of CPHD cases; recurrent genes include **POU1F1, HESX1, LHX3, LHX4, OTX2, GLI2, SOX3**; **POU1F1** may be autosomal dominant (heterozygous) or autosomal recessive (homozygous/compound heterozygous) | POU1F1 phenotype: severe short stature, facial dysmorphism, poor feeding in infancy; MRI: anterior pituitary hypoplasia | Historical Sanger sequencing yield **<15%**; next-generation sequencing yield up to **19.1%**; ~**70 genes** implicated overall; adverse events during rhGH treatment reported in **14.4%** of patients in cited real-world data | (nguyen2025identificationofpou1f1 pages 2-4) |
| Martinez-Mayer et al. | 2024 | *Genome Medicine* | https://doi.org/10.1186/s13073-024-01347-y | Congenital hypopituitarism/CPHD framed as genetically heterogeneous midline developmental disorder; study used mouse embryonic phenotyping to expand candidate-gene discovery rather than provide clinical diagnostic cutoffs | States **67 genes** associated with CH by 2023; IMPC/DMDD screen of **209** embryonic lethal/subviable knockout lines identified **51** genes with pituitary malformations; human candidate validation found variants in **MORC2** and **SETD5**; pathways enriched included cilia-related functions, chromatin/epigenetic regulation, and serine-glycine metabolism | Mouse malformations included absent, hypoplastic, and dysmorphic anterior/posterior pituitary; candidate pathways suggest mechanisms for human pituitary malformation and syndromic CH/CPHD | “Vast majority” of CH cases remain genetically unsolved; **51/209** knockout lines abnormal (~**24.4%**); among candidate genes, **32/51 (63%)** associated with human disease; known CH genes had risen to **67** | (martinezmayer2024knockoutmicewith pages 10-12, martinezmayer2024knockoutmicewith pages 15-17, martinezmayer2024knockoutmicewith pages 4-6, martinezmayer2024knockoutmicewith pages 18-21, martinezmayer2024knockoutmicewith pages 1-2) |


*Table: This table compiles the most useful disease-characteristics evidence for congenital/genetic CPHD/MPHD across recent cohort, review, and discovery studies. It highlights how the disorder is defined, which genes are implicated, what phenotypes and MRI findings are common, and the main epidemiology and diagnostic-yield numbers relevant for a knowledge base.*

---

## Visual evidence (gene compendium)
Martinez‑Mayer et al. 2024 provides a curated table of “Human genes implicated in hypothalamic-pituitary abnormalities,” useful as a gene list reference for panels/WES interpretation. (martinezmayer2024knockoutmicewith media 20fb156a, martinezmayer2024knockoutmicewith media 13ff31db)

---

## Evidence gaps (for KB completion)
* Standardized disease IDs (MONDO/ORPHA/ICD/MeSH) and comprehensive OMIM crosswalks were not retrievable from the accessible full texts in this run.
* Population genetics (carrier frequencies; founder variants) and disease-specific QoL statistics remain under-captured in the retrieved corpus.
* Differential diagnosis and standardized diagnostic criteria statements from endocrine society pediatric congenital hypopituitarism guidelines were not fully accessible in the retrieved full texts.


References

1. (lee2024clinicalandgenetic pages 1-2): Yoonha Lee, Young Ah Lee, Jung Min Ko, Choong Ho Shin, and Yun Jeong Lee. Clinical and genetic features of childhood-onset congenital combined pituitary hormone deficiency: a retrospective, single-center cohort study. Annals of Pediatric Endocrinology &amp; Metabolism, 29:379-386, Dec 2024. URL: https://doi.org/10.6065/apem.2448008.004, doi:10.6065/apem.2448008.004. This article has 6 citations.

2. (plachy2024etiologyofcombined pages 2-3): Lukas Plachy, Petra Dusatkova, Klara Maratova, Shenali Anne Amaratunga, Dana Zemkova, Vit Neuman, Stanislava Kolouskova, Barbora Obermannova, Marta Snajderova, Zdenek Sumnik, Jan Lebl, and Stepanka Pruhova. Etiology of combined pituitary hormone deficiency: gnao1 as a novel candidate gene. Endocrine Connections, Jul 2024. URL: https://doi.org/10.1530/ec-24-0217, doi:10.1530/ec-24-0217. This article has 1 citations and is from a peer-reviewed journal.

3. (tuz2023longtermfollowupdata pages 9-9): Aysegul Elvan Tuz, Elvan Bayramoğlu, and Semra Çetinkaya. Long-term follow-up data of patients with multiple pituitary hormone deficiency. Andes Pediatrica, 94:689, Dec 2023. URL: https://doi.org/10.32641/andespediatr.v94i6.4680, doi:10.32641/andespediatr.v94i6.4680. This article has 0 citations.

4. (santoro2025anovelmissense pages 1-2): Claudia Santoro, Francesca Aiello, Antonella Farina, Emanuele Miraglia del Giudice, Filomena Pascarella, Maria Rosaria Licenziati, Nicola Improda, Giulio Piluso, Annalaura Torella, Francesca Del Vecchio Blanco, Mario Cirillo, Vincenzo Nigro, and Anna Grandone. A novel missense variant in lhx4 in three children with multiple pituitary hormone deficiency belonging to two unrelated families and contribution of additional gli2 and igfr1 variant. Children, 12:364, Mar 2025. URL: https://doi.org/10.3390/children12030364, doi:10.3390/children12030364. This article has 0 citations.

5. (aguilarriera2025progressionfromisolated pages 1-2): Cristina Aguilar-Riera, Diego Yeste, Núria González-Llorens, Eduard Mogas, Ariadna Campos-Martorell, Paula Fernandez-Alvarez, Elida Vázquez, and María Clemente. Progression from isolated growth hormone deficiency to a combined pituitary hormone deficiency in a cohort of paediatrics patients with pituitary morphology abnormalities on mri. BMC Endocrine Disorders, Jul 2025. URL: https://doi.org/10.1186/s12902-025-01980-7, doi:10.1186/s12902-025-01980-7. This article has 0 citations and is from a peer-reviewed journal.

6. (martinezmayer2024knockoutmicewith pages 1-2): Julian Martinez-Mayer, Michelle L. Brinkmeier, Sean P. O’Connell, Arnold Ukagwu, Marcelo A. Marti, Mirta Miras, Maria V. Forclaz, Maria G. Benzrihen, Leonard Y. M. Cheung, Sally A. Camper, Buffy S. Ellsworth, Lori T. Raetzman, Maria I. Pérez-Millán, and Shannon W. Davis. Knockout mice with pituitary malformations help identify human cases of hypopituitarism. Genome Medicine, May 2024. URL: https://doi.org/10.1186/s13073-024-01347-y, doi:10.1186/s13073-024-01347-y. This article has 7 citations and is from a highest quality peer-reviewed journal.

7. (nguyen2025identificationofpou1f1 pages 2-4): Ha Thu Nguyen, Khanh Ngoc Nguyen, Tran Minh Dien, Thi Bich Ngoc Can, Thi Thanh Ngan Nguyen, Nguyen Thi Kim Lien, Nguyen Van Tung, Nguyen Thi Xuan, Nguyen Thien Tao, Ngoc Lan Nguyen, Van Khanh Tran, Tran Thi Chi Mai, Van Anh Tran, Huy Hoang Nguyen, and Chi Dung Vu. Identification of pou1f1 variants in vietnamese patients with combined pituitary hormone deficiency. International Journal of Molecular Sciences, Mar 2025. URL: https://doi.org/10.3390/ijms26062406, doi:10.3390/ijms26062406. This article has 0 citations.

8. (arzilli2025diagnosticchallengesof pages 7-8): Federica Arzilli, Giulia De Fortuna, Ignazio Cammisa, Luca Vagnozzi, Giorgio Sodero, Donato Rigante, and Clelia Cipolla. Diagnostic challenges of short stature and growth hormone insufficiency across different genetic etiologies. Biomedicines, 13:1937, Aug 2025. URL: https://doi.org/10.3390/biomedicines13081937, doi:10.3390/biomedicines13081937. This article has 4 citations.

9. (arzilli2025diagnosticchallengesof pages 8-10): Federica Arzilli, Giulia De Fortuna, Ignazio Cammisa, Luca Vagnozzi, Giorgio Sodero, Donato Rigante, and Clelia Cipolla. Diagnostic challenges of short stature and growth hormone insufficiency across different genetic etiologies. Biomedicines, 13:1937, Aug 2025. URL: https://doi.org/10.3390/biomedicines13081937, doi:10.3390/biomedicines13081937. This article has 4 citations.

10. (martinezmayer2024knockoutmicewith pages 15-17): Julian Martinez-Mayer, Michelle L. Brinkmeier, Sean P. O’Connell, Arnold Ukagwu, Marcelo A. Marti, Mirta Miras, Maria V. Forclaz, Maria G. Benzrihen, Leonard Y. M. Cheung, Sally A. Camper, Buffy S. Ellsworth, Lori T. Raetzman, Maria I. Pérez-Millán, and Shannon W. Davis. Knockout mice with pituitary malformations help identify human cases of hypopituitarism. Genome Medicine, May 2024. URL: https://doi.org/10.1186/s13073-024-01347-y, doi:10.1186/s13073-024-01347-y. This article has 7 citations and is from a highest quality peer-reviewed journal.

11. (plachy2024etiologyofcombined pages 1-2): Lukas Plachy, Petra Dusatkova, Klara Maratova, Shenali Anne Amaratunga, Dana Zemkova, Vit Neuman, Stanislava Kolouskova, Barbora Obermannova, Marta Snajderova, Zdenek Sumnik, Jan Lebl, and Stepanka Pruhova. Etiology of combined pituitary hormone deficiency: gnao1 as a novel candidate gene. Endocrine Connections, Jul 2024. URL: https://doi.org/10.1530/ec-24-0217, doi:10.1530/ec-24-0217. This article has 1 citations and is from a peer-reviewed journal.

12. (stagi2023managementofneonatal pages 10-11): Stefano Stagi, Maria Tufano, Nicolò Chiti, Matteo Cerutti, Alessandra Li Pomi, Tommaso Aversa, and Malgorzata Wasniewska. Management of neonatal isolated and combined growth hormone deficiency: current status. International Journal of Molecular Sciences, 24:10114, Jun 2023. URL: https://doi.org/10.3390/ijms241210114, doi:10.3390/ijms241210114. This article has 9 citations.

13. (iglesias2024anupdateon pages 15-16): Pedro Iglesias. An update on advances in hypopituitarism: etiology, diagnosis, and current management. Journal of Clinical Medicine, 13:6161, Oct 2024. URL: https://doi.org/10.3390/jcm13206161, doi:10.3390/jcm13206161. This article has 33 citations.

14. (martinezmayer2024knockoutmicewith pages 10-12): Julian Martinez-Mayer, Michelle L. Brinkmeier, Sean P. O’Connell, Arnold Ukagwu, Marcelo A. Marti, Mirta Miras, Maria V. Forclaz, Maria G. Benzrihen, Leonard Y. M. Cheung, Sally A. Camper, Buffy S. Ellsworth, Lori T. Raetzman, Maria I. Pérez-Millán, and Shannon W. Davis. Knockout mice with pituitary malformations help identify human cases of hypopituitarism. Genome Medicine, May 2024. URL: https://doi.org/10.1186/s13073-024-01347-y, doi:10.1186/s13073-024-01347-y. This article has 7 citations and is from a highest quality peer-reviewed journal.

15. (martinezmayer2024knockoutmicewith media 20fb156a): Julian Martinez-Mayer, Michelle L. Brinkmeier, Sean P. O’Connell, Arnold Ukagwu, Marcelo A. Marti, Mirta Miras, Maria V. Forclaz, Maria G. Benzrihen, Leonard Y. M. Cheung, Sally A. Camper, Buffy S. Ellsworth, Lori T. Raetzman, Maria I. Pérez-Millán, and Shannon W. Davis. Knockout mice with pituitary malformations help identify human cases of hypopituitarism. Genome Medicine, May 2024. URL: https://doi.org/10.1186/s13073-024-01347-y, doi:10.1186/s13073-024-01347-y. This article has 7 citations and is from a highest quality peer-reviewed journal.

16. (martinezmayer2024knockoutmicewith media 13ff31db): Julian Martinez-Mayer, Michelle L. Brinkmeier, Sean P. O’Connell, Arnold Ukagwu, Marcelo A. Marti, Mirta Miras, Maria V. Forclaz, Maria G. Benzrihen, Leonard Y. M. Cheung, Sally A. Camper, Buffy S. Ellsworth, Lori T. Raetzman, Maria I. Pérez-Millán, and Shannon W. Davis. Knockout mice with pituitary malformations help identify human cases of hypopituitarism. Genome Medicine, May 2024. URL: https://doi.org/10.1186/s13073-024-01347-y, doi:10.1186/s13073-024-01347-y. This article has 7 citations and is from a highest quality peer-reviewed journal.

17. (martinezmayer2024knockoutmicewith media 471988ef): Julian Martinez-Mayer, Michelle L. Brinkmeier, Sean P. O’Connell, Arnold Ukagwu, Marcelo A. Marti, Mirta Miras, Maria V. Forclaz, Maria G. Benzrihen, Leonard Y. M. Cheung, Sally A. Camper, Buffy S. Ellsworth, Lori T. Raetzman, Maria I. Pérez-Millán, and Shannon W. Davis. Knockout mice with pituitary malformations help identify human cases of hypopituitarism. Genome Medicine, May 2024. URL: https://doi.org/10.1186/s13073-024-01347-y, doi:10.1186/s13073-024-01347-y. This article has 7 citations and is from a highest quality peer-reviewed journal.

18. (martinezmayer2024knockoutmicewith media 9f0cb61f): Julian Martinez-Mayer, Michelle L. Brinkmeier, Sean P. O’Connell, Arnold Ukagwu, Marcelo A. Marti, Mirta Miras, Maria V. Forclaz, Maria G. Benzrihen, Leonard Y. M. Cheung, Sally A. Camper, Buffy S. Ellsworth, Lori T. Raetzman, Maria I. Pérez-Millán, and Shannon W. Davis. Knockout mice with pituitary malformations help identify human cases of hypopituitarism. Genome Medicine, May 2024. URL: https://doi.org/10.1186/s13073-024-01347-y, doi:10.1186/s13073-024-01347-y. This article has 7 citations and is from a highest quality peer-reviewed journal.

19. (zygmuntgorska2024comparisonofclinical pages 4-6): Agata Zygmunt-Górska, Małgorzata Wójcik, Aleksandra Gilis-Januszewska, Anna Starmach, Mirosław Bik-Multanowski, and Jerzy B. Starzyk. Comparison of clinical characteristics of a pediatric cohort with combined pituitary hormone deficiency caused by mutation of the prop1 gene or of other origins. Hormones, 23:69-79, Dec 2024. URL: https://doi.org/10.1007/s42000-023-00510-1, doi:10.1007/s42000-023-00510-1. This article has 3 citations and is from a peer-reviewed journal.

20. (zygmuntgorska2024comparisonofclinical pages 1-2): Agata Zygmunt-Górska, Małgorzata Wójcik, Aleksandra Gilis-Januszewska, Anna Starmach, Mirosław Bik-Multanowski, and Jerzy B. Starzyk. Comparison of clinical characteristics of a pediatric cohort with combined pituitary hormone deficiency caused by mutation of the prop1 gene or of other origins. Hormones, 23:69-79, Dec 2024. URL: https://doi.org/10.1007/s42000-023-00510-1, doi:10.1007/s42000-023-00510-1. This article has 3 citations and is from a peer-reviewed journal.

21. (martinezmayer2024knockoutmicewith pages 4-6): Julian Martinez-Mayer, Michelle L. Brinkmeier, Sean P. O’Connell, Arnold Ukagwu, Marcelo A. Marti, Mirta Miras, Maria V. Forclaz, Maria G. Benzrihen, Leonard Y. M. Cheung, Sally A. Camper, Buffy S. Ellsworth, Lori T. Raetzman, Maria I. Pérez-Millán, and Shannon W. Davis. Knockout mice with pituitary malformations help identify human cases of hypopituitarism. Genome Medicine, May 2024. URL: https://doi.org/10.1186/s13073-024-01347-y, doi:10.1186/s13073-024-01347-y. This article has 7 citations and is from a highest quality peer-reviewed journal.

22. (martinezmayer2024knockoutmicewith pages 18-21): Julian Martinez-Mayer, Michelle L. Brinkmeier, Sean P. O’Connell, Arnold Ukagwu, Marcelo A. Marti, Mirta Miras, Maria V. Forclaz, Maria G. Benzrihen, Leonard Y. M. Cheung, Sally A. Camper, Buffy S. Ellsworth, Lori T. Raetzman, Maria I. Pérez-Millán, and Shannon W. Davis. Knockout mice with pituitary malformations help identify human cases of hypopituitarism. Genome Medicine, May 2024. URL: https://doi.org/10.1186/s13073-024-01347-y, doi:10.1186/s13073-024-01347-y. This article has 7 citations and is from a highest quality peer-reviewed journal.

23. (gan2019disordersofhypothalamo‐pituitary pages 40-42): Hoong‐Wei Gan, Kyriaki‐Sandy Alatzoglou, and Mehul T. Dattani. Disorders of hypothalamo‐pituitary axis. Brook's Clinical Pediatric Endocrinology, pages 133-198, Aug 2019. URL: https://doi.org/10.1002/9781119152712.ch5, doi:10.1002/9781119152712.ch5. This article has 8 citations.