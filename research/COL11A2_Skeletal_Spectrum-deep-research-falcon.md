---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-08T10:16:48.562745'
end_time: '2026-05-08T10:32:12.369477'
duration_seconds: 923.81
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: COL11A2-Related Skeletal Spectrum
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 46
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** COL11A2-Related Skeletal Spectrum
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **COL11A2-Related Skeletal Spectrum** covering all of the
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
- **Disease Name:** COL11A2-Related Skeletal Spectrum
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **COL11A2-Related Skeletal Spectrum** covering all of the
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


# COL11A2-Related Skeletal Spectrum — Comprehensive Research Report (2026-05-08)

## Scope note
“COL11A2-related skeletal spectrum” is not a single universally standardized disease label; it is best represented as an allelic spectrum anchored by **COL11A2** pathogenic variants, spanning (i) non-ocular **Stickler syndrome type 3** (often equated with an autosomal dominant form of OSMED) and (ii) **autosomal recessive otospondylomegaepiphyseal dysplasia (OSMED)**, with additional COL11A2-associated phenotypes including dominant and recessive nonsyndromic hearing loss and emerging associations such as congenital scoliosis/vertebral malformations. (soh2022dominantsticklersyndrome. pages 8-10, selvam2020novelcol11a2pathogenic pages 1-2, su2023casereportautosomal pages 1-2, rebello2023col11a2asa pages 2-4)

| Entity / preferred label | Common synonyms / overlapping labels | Identifiers (OMIM/MONDO where available) | Typical inheritance reported | Ocular involvement | Hearing phenotype | Skeletal / craniofacial phenotype highlights | Key source(s) and URL |
|---|---|---|---|---|---|---|---|
| COL11A2-related skeletal spectrum | COL11A2-related non-ocular Stickler/OSMED spectrum | Stickler syndrome MONDO: MONDO_0019354; Stickler syndrome type 3 / non-ocular Stickler commonly linked to OMIM 184840; autosomal recessive OSMED linked to OMIM 215150 (OpenTargets Search: Stickler syndrome,otospondylomegaepiphyseal dysplasia-COL11A2, soh2022dominantsticklersyndrome. pages 1-2, selvam2020novelcol11a2pathogenic pages 1-2) | Autosomal dominant and autosomal recessive forms both reported (selvam2020novelcol11a2pathogenic pages 1-2, su2023casereportautosomal pages 1-2, soh2022dominantsticklersyndrome. pages 1-2) | Usually absent or minimal in COL11A2-related disease because COL11A2 is not expressed in vitreous (soh2022dominantsticklersyndrome. pages 8-10, sheppard2021sticklersyndrome pages 3-4) | Frequent; often congenital or childhood-onset sensorineural hearing loss (soh2022dominantsticklersyndrome. pages 8-10, acke2022hearinglossin pages 2-4) | Connective tissue skeletal phenotype with arthropathy/epiphyseal-spinal abnormalities across the spectrum (soh2022dominantsticklersyndrome. pages 8-10, selvam2020novelcol11a2pathogenic pages 1-2) | Melkoniemi 2000 https://doi.org/10.1086/302750; Selvam 2020 https://doi.org/10.1055/s-0039-1698446; Soh 2022 https://doi.org/10.17863/cam.86865; Acke 2022 https://doi.org/10.3390/genes13091571; Su 2023 https://doi.org/10.3389/fgene.2023.1154087 |
| Stickler syndrome type 3 | Non-ocular Stickler syndrome; dominant OSMED; autosomal dominant otospondylomegaepiphyseal dysplasia | OMIM 184840; disease-target evidence mapped under Stickler syndrome / dominant Stickler in Open Targets (OpenTargets Search: Stickler syndrome,otospondylomegaepiphyseal dysplasia-COL11A2, soh2022dominantsticklersyndrome. pages 1-2) | Usually autosomal dominant in reviews, though recessive COL11A2 type 3 cases also reported (su2023casereportautosomal pages 1-2, acke2022hearinglossin pages 2-4, soh2022dominantsticklersyndrome. pages 1-2) | No ocular symptoms / normal vitreous emphasized as distinguishing feature (acke2022hearinglossin pages 2-4, soh2022dominantsticklersyndrome. pages 1-2) | Moderate, predominantly symmetric sensorineural hearing loss; low/mid frequencies mild-moderate and high frequencies moderate-severe; hearing loss reported in 69-83% when STL2 and STL3 are grouped, and 94.1% in one type 3 review excerpt (soh2022dominantsticklersyndrome. pages 8-10, acke2022hearinglossin pages 2-4) | Deafness, cleft palate, arthropathy; non-ocular connective tissue disorder with skeletal involvement (soh2022dominantsticklersyndrome. pages 8-10, soh2022dominantsticklersyndrome. pages 1-2) | Soh 2022 https://doi.org/10.17863/cam.86865; Acke 2022 https://doi.org/10.3390/genes13091571 |
| Otospondylomegaepiphyseal dysplasia (OSMED), autosomal recessive form | Autosomal recessive OSMED; OSMED type B; historically overlapping labels include Weissenbacher-Zweymuller syndrome, Nance-Insley syndrome, Nance-Sweeney chondrodysplasia, chondrodystrophy with sensorineural deafness (selvam2020novelcol11a2pathogenic pages 1-2) | OMIM 215150 (melkoniemi2000autosomalrecessivedisorder pages 1-2, selvam2020novelcol11a2pathogenic pages 1-2) | Autosomal recessive; homozygous or compound heterozygous COL11A2 variants; recurrence risk ~25% in families (melkoniemi2000autosomalrecessivedisorder pages 6-9, melkoniemi2000autosomalrecessivedisorder pages 1-2) | Absent in foundational and reviewed recessive cohorts; helps distinguish from ocular Stickler syndromes (selvam2020novelcol11a2pathogenic pages 1-2, selvam2020novelcol11a2pathogenic pages 3-4, melkoniemi2000autosomalrecessivedisorder pages 1-2) | Severe bilateral sensorineural hearing loss, often present from birth; 10/10 in Melkoniemi cohort and 10/10 in Selvam review table excerpt (melkoniemi2000autosomalrecessivedisorder pages 4-6, selvam2020novelcol11a2pathogenic pages 3-4) | Disproportionately short limbs, enlarged joints, vertebral anomalies/platyspondyly/coronal clefts, large epiphyses, metaphyseal flaring, dumbbell femurs, midface hypoplasia, depressed nasal bridge, micrognathia, cleft palate/bifid uvula, early osteoarthritis; many features 10/10 in Melkoniemi cohort (melkoniemi2000autosomalrecessivedisorder pages 4-6, melkoniemi2000autosomalrecessivedisorder pages 6-9, selvam2020novelcol11a2pathogenic pages 1-2) | Melkoniemi 2000 https://doi.org/10.1086/302750; Selvam 2020 https://doi.org/10.1055/s-0039-1698446 |
| Autosomal recessive Stickler syndrome type 3 due to COL11A2 | Recessive non-ocular Stickler syndrome; recessive COL11A2-OSMED overlap | Reported as Stickler syndrome type 3 / COL11A2-related, overlapping with OMIM 184840 and OSMED spectrum (su2023casereportautosomal pages 1-2, su2023casereportautosomal pages 6-6) | Autosomal recessive; compound heterozygous COL11A2 variants reported (su2023casereportautosomal pages 1-2, su2023casereportautosomal pages 6-6) | Non-ocular in reported case/review context (su2023casereportautosomal pages 1-2, su2023casereportautosomal pages 6-6) | Hearing impairment from childhood; report references non-progressive hearing impairment and broader literature of sensorineural deafness (su2023casereportautosomal pages 1-2) | Spondyloepiphyseal dysplasia with large epiphyses, platyspondyly, degenerative osteoarthritis, enlarged interphalangeal joints, O-shaped legs, back/knee/ankle pain, sunken nasal bridge (su2023casereportautosomal pages 1-2) | Su 2023 https://doi.org/10.3389/fgene.2023.1154087 |
| COL11A2-associated hearing-loss end of spectrum | DFNA13; DFNB53; nonsyndromic hearing loss associated with COL11A2 | Named in reviews/case reports as allelic conditions within COL11A2 spectrum; specific OMIM IDs not provided in available context (selvam2020novelcol11a2pathogenic pages 1-2, su2023casereportautosomal pages 6-6) | Both autosomal dominant (DFNA13) and autosomal recessive (DFNB53) reported across COL11A2 disease spectrum (selvam2020novelcol11a2pathogenic pages 1-2, su2023casereportautosomal pages 6-6) | None expected in isolated hearing-loss presentations based on non-ocular COL11A2 biology, but not fully characterized here (su2023casereportautosomal pages 6-6) | Hearing loss may occur as isolated or predominant feature; COL11A2 spectrum ranges from mild deafness to full OSMED phenotype (selvam2020novelcol11a2pathogenic pages 1-2) | Skeletal dysplasia absent or much less prominent in nonsyndromic forms compared with OSMED/Stickler type 3 spectrum (selvam2020novelcol11a2pathogenic pages 1-2, su2023casereportautosomal pages 6-6) | Selvam 2020 https://doi.org/10.1055/s-0039-1698446; Su 2023 https://doi.org/10.3389/fgene.2023.1154087 |


*Table: This table summarizes the main disease entities within the COL11A2-related skeletal spectrum, including overlapping names, identifiers, inheritance, and distinguishing ocular, hearing, and skeletal features. It is useful for harmonizing non-ocular Stickler syndrome type 3 and OSMED terminology in a disease knowledge base.*

## 1. Disease Information
### 1.1 Definition and overview
COL11A2-related skeletal spectrum comprises **heritable type XI collagenopathies** caused by pathogenic variants in **COL11A2** (collagen type XI alpha 2 chain), typically presenting with combinations of **skeletal dysplasia/arthropathy**, **craniofacial anomalies (often cleft palate/micrognathia)**, and **sensorineural hearing loss**, with **minimal/absent ocular involvement** as a key differentiator from other Stickler syndromes because COL11A2 is not expressed in the vitreous. (soh2022dominantsticklersyndrome. pages 8-10, sheppard2021sticklersyndrome pages 3-4, melkoniemi2000autosomalrecessivedisorder pages 1-2)

### 1.2 Key identifiers (available in retrieved sources)
- **Stickler syndrome (broad)**: **MONDO_0019354** (Open Targets mapping). (OpenTargets Search: Stickler syndrome,otospondylomegaepiphyseal dysplasia-COL11A2)
- **Stickler syndrome type 3 (non-ocular Stickler; COL11A2)**: cited as **OMIM/MIM 184840** in Stickler reviews. (soh2022dominantsticklersyndrome. pages 1-2)
- **Autosomal recessive OSMED**: **OMIM/MIM 215150**. (melkoniemi2000autosomalrecessivedisorder pages 1-2)

*Note:* Orphanet / ICD / MeSH identifiers were not directly retrievable from the currently available full-text evidence in this run; the above identifiers come from primary/review literature and Open Targets mapping. (OpenTargets Search: Stickler syndrome,otospondylomegaepiphyseal dysplasia-COL11A2, soh2022dominantsticklersyndrome. pages 1-2, melkoniemi2000autosomalrecessivedisorder pages 1-2)

### 1.3 Synonyms and alternative names
- Stickler syndrome type 3 = **non-ocular Stickler syndrome** and is also termed **autosomal dominant otospondylomegaepiphyseal dysplasia (OSMED)** in major reviews. (soh2022dominantsticklersyndrome. pages 1-2, soh2022dominantsticklersyndrome. pages 8-10)
- Autosomal recessive OSMED has historical synonyms (as used in case series/reviews) including **Weissenbacher–Zweymüller syndrome**, **Nance–Insley syndrome**, **Nance–Sweeney chondrodysplasia**, and **chondrodystrophy with sensorineural deafness**. (selvam2020novelcol11a2pathogenic pages 1-2)

### 1.4 Evidence source type
The information summarized here is derived from **aggregated disease-level resources** (reviews, case series) and **individual patient reports/case series** with genetic confirmation; it is not derived from EHR-only sources in the retrieved evidence. (soh2022dominantsticklersyndrome. pages 8-10, melkoniemi2000autosomalrecessivedisorder pages 4-6, su2023casereportautosomal pages 1-2)

## 2. Etiology
### 2.1 Disease causal factors
**Primary cause:** germline pathogenic variants in **COL11A2**.
- **Autosomal recessive OSMED** is strongly associated with **loss-of-function (LoF)** mechanisms: in a foundational AJHG cohort, **10 distinct COL11A2 mutations** were identified across 7 families; **nine created premature termination codons** and **one altered a splicing consensus sequence**, with homozygous or compound heterozygous inheritance. (melkoniemi2000autosomalrecessivedisorder pages 6-9)
- **Autosomal dominant non-ocular Stickler/OSMED** is commonly conceptualized as a **dominant-negative collagen mechanism** (e.g., missense or in-frame exon-skipping/in-frame deletions in the triple helical region), leading to dysfunctional heterotrimers. (soh2022dominantsticklersyndrome. pages 8-10)

**Abstract support (example):** In a diagnostic-methods paper on COL11A2 splicing, the abstract states: “*Type 2 SS and the SS variant otospondylomegaepiphyseal dysplasia (OSMED) are caused by deleterious variants in COL11A1 and COL11A2, respectively.*” (Genes, 2020-12; https://doi.org/10.3390/genes11121513) (micale2020exontrappingassayimproves pages 1-3)

### 2.2 Risk factors
- **Genetic:** biallelic COL11A2 pathogenic variants confer risk for autosomal recessive OSMED, with typical Mendelian recurrence risk (~25% for siblings) in affected families. (melkoniemi2000autosomalrecessivedisorder pages 6-9)
- **Environmental/lifestyle:** No disease-specific environmental risk factors or protective factors were identified in the retrieved evidence; phenotype is primarily genetically determined. (melkoniemi2000autosomalrecessivedisorder pages 1-2, soh2022dominantsticklersyndrome. pages 8-10)

### 2.3 Protective factors / gene–environment interactions
No validated protective factors or gene–environment interactions specific to COL11A2-related skeletal spectrum were identified in the retrieved sources. (melkoniemi2000autosomalrecessivedisorder pages 1-2, soh2022dominantsticklersyndrome. pages 8-10)

## 3. Phenotypes (clinical spectrum)
### 3.1 Core phenotype domains
**A. Skeletal / growth / joint disease**
- Autosomal recessive OSMED is described as a skeletal dysplasia with **disproportionately short limbs**, **enlarged epiphyses**, **vertebral anomalies**, and early joint disease. (melkoniemi2000autosomalrecessivedisorder pages 1-2, melkoniemi2000autosomalrecessivedisorder pages 6-9)
- Quantitative phenotype frequencies in one foundational cohort: **10/10** with disproportionate short limbs, enlarged joints, vertebral body anomalies, and cleft palate/bifid uvula; additional findings include small chin in **7/10**. (melkoniemi2000autosomalrecessivedisorder pages 4-6)
- Dominant non-ocular Stickler/OSMED includes **arthropathy** and predisposition to **premature osteoarthritis**, mechanistically linked to abnormal cartilage collagen organization. (soh2022dominantsticklersyndrome. pages 8-10, soh2022dominantsticklersyndrome. pages 1-2)

**B. Craniofacial / orofacial**
- Features repeatedly described include **midface hypoplasia**, **depressed nasal bridge**, **micrognathia/small chin**, and **cleft palate/bifid uvula** (particularly prominent in recessive OSMED). (melkoniemi2000autosomalrecessivedisorder pages 4-6, selvam2020novelcol11a2pathogenic pages 1-2, melkoniemi2000autosomalrecessivedisorder pages 6-9)

**C. Hearing**
- Hearing loss is a hallmark. In a dominant non-ocular Stickler/OSMED review excerpt, hearing loss is reported as childhood-onset and present in **94.1%** of patients. (soh2022dominantsticklersyndrome. pages 8-10)
- In a recessive OSMED cohort, **sensorineural hearing loss (SNHL) occurred in 10/10**. (melkoniemi2000autosomalrecessivedisorder pages 4-6)
- A focused Stickler hearing review (Genes, 2022-09; https://doi.org/10.3390/genes13091571) summarizes that for COL11A2 (type 3) hearing loss is typically **moderate** with audiograms often showing **mild–moderate loss at low/mid frequencies** and **moderate–severe loss at high frequencies**; U-shaped audiograms are reported in some patients. (acke2022hearinglossin pages 2-4)

**D. Ocular**
- **Minimal/absent ocular involvement** is a key discriminator for COL11A2-related disease, consistent with COL11A2 not being expressed in vitreous. (sheppard2021sticklersyndrome pages 3-4, soh2022dominantsticklersyndrome. pages 8-10)
- Recessive OSMED cohorts largely lack major ocular findings; the Selvam review table notes **0/10** with ocular findings in the summarized cohort, with only minor refractive/strabismus findings sporadically reported. (selvam2020novelcol11a2pathogenic pages 3-4, selvam2020novelcol11a2pathogenic media b73d0cc6)

### 3.2 Onset, severity, progression
- **OSMED (AR):** typically congenital/early childhood onset with dysmorphism and skeletal dysplasia recognized early; SNHL often noted at birth. (selvam2020novelcol11a2pathogenic pages 1-2, melkoniemi2000autosomalrecessivedisorder pages 4-6)
- **Non-ocular Stickler (AD, COL11A2):** hearing loss is commonly childhood-onset and described as **non-progressive** in a dominant Stickler review excerpt, although other reviews note childhood onset/progression can occur and that adults show limited progression for STL2/3. (soh2022dominantsticklersyndrome. pages 8-10, acke2022hearinglossin pages 4-6)

### 3.3 Suggested HPO terms (non-exhaustive)
(terms suggested based on described clinical features in evidence)
- Sensorineural hearing impairment (**HP:0000407**) (melkoniemi2000autosomalrecessivedisorder pages 4-6, acke2022hearinglossin pages 2-4)
- Cleft palate (**HP:0000175**) / bifid uvula (**HP:0000193**) (melkoniemi2000autosomalrecessivedisorder pages 4-6)
- Midface hypoplasia (**HP:0000309**) (melkoniemi2000autosomalrecessivedisorder pages 4-6, melkoniemi2000autosomalrecessivedisorder pages 6-9)
- Depressed nasal bridge (**HP:0005280**) (selvam2020novelcol11a2pathogenic pages 1-2)
- Micrognathia (**HP:0000347**) / small chin (**HP:0000308**) (melkoniemi2000autosomalrecessivedisorder pages 4-6)
- Disproportionate short stature (**HP:0003498**) / short limbs (**HP:0009826**) (melkoniemi2000autosomalrecessivedisorder pages 4-6)
- Platyspondyly (**HP:0000926**) / vertebral segmentation anomalies (**HP:0003312**) (melkoniemi2000autosomalrecessivedisorder pages 6-9, su2023casereportautosomal pages 1-2)
- Enlarged epiphyses / epiphyseal dysplasia (**HP:0002654**) (melkoniemi2000autosomalrecessivedisorder pages 6-9, su2023casereportautosomal pages 1-2)
- Early-onset osteoarthritis (**HP:0002758**) / arthropathy (**HP:0001367**) (soh2022dominantsticklersyndrome. pages 8-10, su2023casereportautosomal pages 1-2)

### 3.4 Quality-of-life impact
Direct validated QoL instrument results (EQ-5D/SF-36/PROMIS) were not found in the retrieved evidence; however, the combination of SNHL, cleft palate-related feeding/speech issues, and early arthropathy implies substantial functional impact and need for multidisciplinary support. (sheppard2021sticklersyndrome pages 7-8, soh2022dominantsticklersyndrome. pages 8-10)

## 4. Genetic / Molecular Information
### 4.1 Causal gene
- **COL11A2** encodes the **α2(XI) chain** of type XI collagen. (melkoniemi2000autosomalrecessivedisorder pages 1-2)

### 4.2 Variant types and functional consequences
**Autosomal recessive OSMED (LoF-enriched):**
- In the AJHG cohort, **10 distinct mutations** were identified; **most predicted premature truncation**, and RNA studies showed splicing defects (e.g., exon skipping or cryptic splice use causing frameshift and premature stop), leading authors to predict absence or truncation of the α2(XI) chain. (melkoniemi2000autosomalrecessivedisorder pages 6-9, melkoniemi2000autosomalrecessivedisorder pages 2-4)

**Splice-region variants and in-frame deletions:**
- Exon-trapping (minigene) assays can demonstrate splicing outcomes for COL11A2 intronic variants; for example, c.4392+1G>A was shown to cause **skipping of 54 bp of exon 60**. (Genes, 2020-12; https://doi.org/10.3390/genes11121513) (micale2020exontrappingassayimproves pages 11-13)

**Dominant-negative concept for COL11A2 Stickler type 3:**
- A dominant Stickler review excerpt explains that COL11A2 variants often act via **dominant negative effects** (missense or in-frame exon skipping/in-frame deletions) affecting the helical domain and disrupting heterotrimer formation. (soh2022dominantsticklersyndrome. pages 8-10)

### 4.3 Genotype–phenotype correlations (current evidence limits)
- Recessive LoF variants are associated with a relatively homogeneous severe OSMED phenotype with high frequencies of cleft palate, SNHL, and skeletal dysplasia. (melkoniemi2000autosomalrecessivedisorder pages 4-6, melkoniemi2000autosomalrecessivedisorder pages 6-9)
- Heterozygous missense variants can present with variable penetrance and may contribute to vertebral malformations/congenital scoliosis (see §6). (rebello2023col11a2asa pages 2-4)

### 4.4 Population genetics / allele frequency
- In a 2023 congenital scoliosis study, authors reported **gnomAD pLI = 0.7** for COL11A2, consistent with constraint considerations for interpreting variants. (rebello2023col11a2asa pages 2-4)

### 4.5 Modifier genes / epigenetics
No validated modifier genes or disease-specific epigenetic signatures were identified in the retrieved evidence for COL11A2-related skeletal spectrum.

## 5. Environmental Information
No disease-specific environmental, lifestyle, or infectious contributors were identified in the retrieved sources; COL11A2-related skeletal spectrum is primarily Mendelian/genetic in etiology. (melkoniemi2000autosomalrecessivedisorder pages 1-2)

## 6. Mechanism / Pathophysiology
### 6.1 Current mechanistic understanding (collagen XI biology)
- Type XI collagen is a heterotrimeric collagen important for **fibrillogenesis and regulation of collagen fibril structure**; in recessive OSMED, LoF variants likely reduce/abolish α2(XI), disrupting cartilage and ear matrix structure. (melkoniemi2000autosomalrecessivedisorder pages 1-2, melkoniemi2000autosomalrecessivedisorder pages 6-9)
- In dominant non-ocular Stickler/OSMED, a review excerpt links abnormal type XI collagen to downstream cartilage pathology: disorganized collagen patterns, decreased joint space, articular cartilage degradation and predisposition to early osteoarthritis. (soh2022dominantsticklersyndrome. pages 8-10)

### 6.2 Hearing-loss mechanism
COL11A2 is expressed in inner-ear structures (including the tectorial membrane); pathogenic variants are linked to abnormal collagen distribution in this extracellular matrix, consistent with sensorineural hearing loss. (soh2022dominantsticklersyndrome. pages 8-10, li2001targeteddisruptionof pages 3-4)

### 6.3 Recent mechanistic/functional advances (2023)
A 2023 study used CRISPR loss-of-function zebrafish models and transgenic rescue to support pathogenicity of human missense variants:
- Homozygous zebrafish col11a2 LOF alleles produce vertebral fusions; heterozygous deletion alleles also increase fusion penetrance (haploinsufficiency). (rebello2023col11a2asa pages 4-6)
- Wildtype col11a2 transgenes suppress vertebral fusions, but patient missense-variant transgenes fail to rescue, providing functional support for variant pathogenicity and linking COL11A2 to vertebral development/mineralization boundary maintenance. (rebello2023col11a2asa pages 1-2, rebello2023col11a2asa pages 8-11)

### 6.4 Suggested ontology mappings
**GO Biological Process (suggested):**
- extracellular matrix organization (GO:0030198)
- collagen fibril organization (GO:0030199)
- cartilage development (GO:0051216)
- skeletal system development (GO:0001501)
- auditory receptor cell development / inner ear development (e.g., inner ear morphogenesis GO:0048839)

**Cell Ontology (CL) (suggested):**
- chondrocyte (CL:0000138) (growth plate/articular cartilage involvement) (li2001targeteddisruptionof pages 6-8)
- osteoblast (CL:0000062) (vertebral mineralization context in zebrafish) (rebello2023col11a2asa pages 8-11)
- cochlear hair cell (CL:0000601) / supporting cells (for SNHL context; indirect) (acke2022hearinglossin pages 6-7)

## 7. Anatomical Structures Affected
### 7.1 Organ/system level
- **Skeletal system:** spine/vertebrae (platyspondyly, vertebral anomalies; vertebral fusions in models), long bones/epiphyses/metaphyses, joints (arthropathy/early OA). (melkoniemi2000autosomalrecessivedisorder pages 6-9, su2023casereportautosomal pages 1-2, rebello2023col11a2asa pages 4-6)
- **Craniofacial/orofacial:** palate and mandible. (melkoniemi2000autosomalrecessivedisorder pages 4-6, sheppard2021sticklersyndrome pages 7-8)
- **Auditory system:** cochlea/tectorial membrane. (li2001targeteddisruptionof pages 3-4, soh2022dominantsticklersyndrome. pages 8-10)

### 7.2 UBERON suggestions
- cartilage tissue (UBERON:0002416)
- growth plate cartilage (UBERON:0003584)
- vertebra (UBERON:0001093)
- palate (UBERON:0001718)
- cochlea (UBERON:0001845)

## 8. Temporal Development
- **Typical onset:** congenital/infancy/early childhood for OSMED with recognizable dysmorphism, skeletal findings and SNHL. (melkoniemi2000autosomalrecessivedisorder pages 4-6, selvam2020novelcol11a2pathogenic pages 1-2)
- **Course:** chronic lifelong condition; musculoskeletal pain and degenerative osteoarthritis may emerge/progress with age (reported in COL11A2-related Stickler/OSMED contexts). (soh2022dominantsticklersyndrome. pages 8-10, su2023casereportautosomal pages 1-2)

## 9. Inheritance and Population
### 9.1 Inheritance
- **Autosomal recessive OSMED:** homozygous or compound heterozygous COL11A2 variants; recurrence risk ~25% in families. (melkoniemi2000autosomalrecessivedisorder pages 6-9)
- **Autosomal dominant non-ocular Stickler/OSMED:** COL11A2 heterozygous variants; reviews emphasize AD inheritance. (acke2022hearinglossin pages 2-4, soh2022dominantsticklersyndrome. pages 1-2)

### 9.2 Epidemiology
- Stickler syndrome overall incidence is cited as about **1 in 7,500–9,000 newborns** in a dominant Stickler review excerpt; this estimate is not specific to COL11A2 subtypes. (soh2022dominantsticklersyndrome. pages 1-2)
- Recessive COL11A2 Stickler type 3 is described as “ultra-rare” in a 2023 case report excerpt; no robust prevalence/incidence estimates were available from retrieved sources. (su2023casereportautosomal pages 1-2)

## 10. Diagnostics
### 10.1 Clinical and imaging evaluation
- **Radiographs** are central for OSMED characterization (epiphyseal/metaphyseal/spinal changes); in a Selvam summary table, radiographic abnormalities were documented in **6/10** with missing detail for **4/10**. (selvam2020novelcol11a2pathogenic pages 3-4, selvam2020novelcol11a2pathogenic media b73d0cc6)
- CT of temporal bones typically does not show anomalies in Stickler hearing loss; thus SNHL may be “functional/microstructural” rather than grossly anatomic. (acke2022hearinglossin pages 4-6)

### 10.2 Genetic testing approaches (real-world implementation)
**Skeletal dysplasia workflows (generalizable to COL11A2):**
- A radiogenomics-era skeletal dysplasia cohort implemented tiered analysis: clinician-directed gene(s) on WES data → 222-gene virtual panel → HPO-driven agnostic exome search, emphasizing multidisciplinary radiology–genetics review; overall diagnostic yield was **53.3% (8/15)** with **46.7% definite** and **6.7% likely** diagnoses. (BMC Med Genomics, 2021-06; https://doi.org/10.1186/s12920-021-00993-0) (sabir2021diagnosticyieldof pages 2-4)
- Re-analysis of WES can yield additional diagnoses (~10–15% uplift in prior-negative cases), and WGS is increasingly used (especially trio WGS). (sabir2021diagnosticyieldof pages 9-12)

**COL11A2 splice-region variant interpretation (functional validation):**
- For intronic/splice variants, minigene/exon-trapping assays are presented as a practical method when patient RNA is unavailable; this can materially affect ACMG/AMP classification (e.g., evidence of exon skipping/in-frame deletions). (Genes, 2020-12; https://doi.org/10.3390/genes11121513) (micale2020exontrappingassayimproves pages 11-13, micale2020exontrappingassayimproves pages 3-5)

**2023 update relevant to diagnostics:**
- A 2023 congenital scoliosis/vertebral malformation study suggests including **COL11A2** in gene lists/panels for vertebral malformations, supported by functional zebrafish rescue assays and noting incomplete penetrance in at least one family. (Human Molecular Genetics, 2023-07; https://doi.org/10.1093/hmg/ddad117) (rebello2023col11a2asa pages 2-4)

### 10.3 Differential diagnosis (conceptual)
- Other collagenopathies with overlapping skeletal and hearing features include COL2A1/COL11A1 Stickler/Marshall phenotypes; ocular involvement and vitreous phenotype help distinguish non-ocular COL11A2 disease. (soh2022dominantsticklersyndrome. pages 1-2, melkoniemi2000autosomalrecessivedisorder pages 1-2)

## 11. Outcomes / Prognosis
Quantitative survival/mortality estimates were not found in the retrieved evidence. Available sources emphasize chronic morbidity from:
- **Hearing impairment** (risk of speech/language impact without early intervention) (sheppard2021sticklersyndrome pages 7-8)
- **Musculoskeletal degeneration/pain and early osteoarthritis** (soh2022dominantsticklersyndrome. pages 8-10, su2023casereportautosomal pages 1-2)

## 12. Treatment
No disease-modifying pharmacotherapy or gene therapy was identified in the retrieved sources.

### 12.1 Supportive and rehabilitative care (current practice)
**Hearing and ENT management (Stickler/OSMED-relevant):**
- Management guidance emphasizes **early otolaryngology and audiology evaluation** (e.g., within 3–6 months for infants with cleft palate), repeated audiometry, and prompt treatment of otitis media with antibiotics; recurrent cases managed with ventilation tubes as indicated. (sheppard2021sticklersyndrome pages 7-8)
- Hearing interventions: hearing aids/vibrotactile devices for milder losses, and **cochlear implants may be considered** for children >12 months with severe-to-profound deafness. (sheppard2021sticklersyndrome pages 7-8)
- Given newborn screening may miss mild losses and childhood onset/progression can occur, ongoing surveillance beyond newborn screening is emphasized in hearing-focused reviews. (acke2022hearinglossin pages 4-6)

**Cleft palate / craniofacial interventions:**
- Cleft palate surgery timing is individualized; one management source cites typical repair around **12–18 months**, with near-universal need for speech therapy in cleft-affected children. (sheppard2021sticklersyndrome pages 8-9)
- In recessive OSMED case management, specific interventions reported include **palatoplasty and mandibular distraction** in an affected child. (selvam2020novelcol11a2pathogenic pages 1-2)

**Musculoskeletal management:**
- Evidence in retrieved sources supports risk of early arthropathy/osteoarthritis, implying orthopedic monitoring and symptomatic treatment; however, specific evidence-based algorithms for COL11A2 were not identified in retrieved sources. (soh2022dominantsticklersyndrome. pages 8-10)

### 12.2 MAXO term suggestions
- Hearing aid therapy (**MAXO:0000787**) / cochlear implantation (**MAXO:0000558**) (sheppard2021sticklersyndrome pages 7-8)
- Tympanostomy tube insertion / ventilation tubes (**MAXO:0000580**) (sheppard2021sticklersyndrome pages 7-8)
- Palatoplasty (**MAXO:0000495**) (selvam2020novelcol11a2pathogenic pages 1-2, sheppard2021sticklersyndrome pages 8-9)
- Mandibular distraction osteogenesis (**MAXO:0001080**) (selvam2020novelcol11a2pathogenic pages 1-2)
- Physical therapy/rehabilitation (**MAXO:0000018**) (inferred supportive need; not directly evidenced as COL11A2-specific in retrieved texts)

### 12.3 Clinical trials
No interventional clinical trials specific to COL11A2/OSMED/Stickler type 3 were identified in the retrieved ClinicalTrials.gov search results in this run (the returned trials were unrelated dental/implant studies). (clinical trial search output; not citeable as evidence)

## 13. Prevention
Primary prevention is not applicable in the classic sense for a Mendelian disorder; prevention focuses on **genetic counseling** and **reproductive options**.
- Genetic diagnosis supports **cascade testing**, recurrence-risk counseling, and consideration of prenatal or preimplantation genetic testing. (melkoniemi2000autosomalrecessivedisorder pages 6-9, gyokova2026prenatalmoleculardiagnosis pages 6-7)
- Secondary/tertiary prevention includes early identification and management of hearing loss and middle-ear disease to reduce developmental impact, and proactive cleft feeding/speech interventions. (sheppard2021sticklersyndrome pages 7-8, sheppard2021sticklersyndrome pages 6-7)

## 14. Other species / natural disease
No naturally occurring COL11A2-driven veterinary disease was identified in the retrieved evidence (a 2023 canine Stickler-like condition involved COL11A1, not COL11A2). (OpenTargets Search: Stickler syndrome,otospondylomegaepiphyseal dysplasia-COL11A2)

## 15. Model organisms
### 15.1 Mouse model
A Col11a2 targeted-disruption mouse model shows phenotypes consistent with COL11A2-related disease mechanisms:
- Homozygotes lack intact α2(XI) chains and show reduced size, craniofacial changes, disorganized growth-plate chondrocytes, thinner articular cartilage, and hearing impairment (ABR-confirmed), with tectorial membrane collagen fibril disorganization cited as a mechanism. (Dev Dyn, 2001-10; https://doi.org/10.1002/dvdy.1178) (li2001targeteddisruptionof pages 3-4, li2001targeteddisruptionof pages 6-8)

### 15.2 Zebrafish model (recent functional platform)
- CRISPR col11a2 LOF zebrafish show high-penetrance caudal vertebral fusions driven by mineralization across intervertebral segments; heterozygous deletion alleles show increased penetrance consistent with haploinsufficiency. (rebello2023col11a2asa pages 4-6)
- Patient missense variants fail to rescue LOF phenotypes in transgenic assays, supporting pathogenicity assessment utility. (rebello2023col11a2asa pages 1-2, rebello2023col11a2asa pages 8-11)

## Key recent developments (prioritizing 2023–2024)
1. **Expansion of phenotype toward vertebral malformations/congenital scoliosis:** human missense variants + zebrafish functional rescue/LOF data provide a mechanistic and diagnostic rationale to include COL11A2 in congenital scoliosis/vertebral malformation gene lists (Human Molecular Genetics, 2023-07-01; https://doi.org/10.1093/hmg/ddad117). (rebello2023col11a2asa pages 2-4)
2. **Continued recognition of autosomal recessive COL11A2 Stickler type 3:** a 2023 case report frames COL11A2-associated type 3 Stickler as ultra-rare and highlights diagnostic challenges and the importance of comprehensive sequencing for overlooked variants. (Frontiers in Genetics, 2023-06; https://doi.org/10.3389/fgene.2023.1154087) (su2023casereportautosomal pages 1-2)

## Data and statistics (selected)
- Recessive OSMED clinical feature frequencies (foundational cohort): disproportionate short limbs 10/10; enlarged joints 10/10; vertebral anomalies 10/10; cleft palate/bifid uvula 10/10; midface hypoplasia 10/10; SNHL 10/10; small chin 7/10. (melkoniemi2000autosomalrecessivedisorder pages 4-6)
- Stickler type 3 hearing: hearing loss prevalence 94.1% in one review excerpt; and 69–83% when STL2/STL3 grouped, typically moderate with characteristic audiogram shapes. (soh2022dominantsticklersyndrome. pages 8-10, acke2022hearinglossin pages 2-4)
- Skeletal dysplasia WES diagnostic yield in one radiogenomics cohort: 53.3% (8/15) total; 46.7% (7/15) definite; 6.7% (1/15) likely; yield higher when diagnosis suspected pre-test (7/10 vs 1/5). (sabir2021diagnosticyieldof pages 2-4, sabir2021diagnosticyieldof pages 1-2)

## Figure/Table evidence note
A curated table of autosomal recessive OSMED features and frequencies is available in Selvam et al. (2020), including 10/10 SNHL and 0/10 ocular findings in the summarized cohort. (selvam2020novelcol11a2pathogenic media b73d0cc6)

## Expert opinion / authoritative synthesis (from reviews and clinical management texts)
- COL11A2-related Stickler type 3 is framed as a **non-ocular** collagenopathy because COL11A2 is not expressed in vitreous; thus vitreous/ocular phenotype-based classification can help direct gene testing and counseling. (sheppard2021sticklersyndrome pages 3-4, soh2022dominantsticklersyndrome. pages 1-2)
- Hearing loss should be **actively sought and treated** due to high prevalence and potential early-life developmental impact; cleft palate and middle-ear disease necessitate proactive ENT pathways (e.g., early otolaryngology evaluation, audiometry, ventilation tubes). (sheppard2021sticklersyndrome pages 7-8, acke2022hearinglossin pages 2-4)

## Primary literature and key URLs (retrieved in this run)
- Melkoniemi M. et al. *Am J Hum Genet.* 2000-02. “Autosomal recessive disorder otospondylomegaepiphyseal dysplasia is associated with loss-of-function mutations in the COL11A2 gene.” https://doi.org/10.1086/302750 (melkoniemi2000autosomalrecessivedisorder pages 1-2)
- Li S-W. et al. *Dev Dyn.* 2001-10. “Targeted disruption of Col11a2 produces a mild cartilage phenotype in transgenic mice…” https://doi.org/10.1002/dvdy.1178 (li2001targeteddisruptionof pages 3-4)
- Selvam P. et al. *J Pediatr Genet.* 2020-10. “Novel COL11A2 Pathogenic Variants… A Review of the Literature.” https://doi.org/10.1055/s-0039-1698446 (selvam2020novelcol11a2pathogenic pages 1-2)
- Micale L. et al. *Genes.* 2020-12. “Exon-Trapping Assay Improves Clinical Interpretation of COL11A1 and COL11A2 Intronic Variants…” https://doi.org/10.3390/genes11121513 (micale2020exontrappingassayimproves pages 1-3)
- Sabir A.H. et al. *BMC Med Genomics.* 2021-06. “Diagnostic yield of rare skeletal dysplasia conditions in the radiogenomics era.” https://doi.org/10.1186/s12920-021-00993-0 (sabir2021diagnosticyieldof pages 2-4)
- Acke F.R.E. & De Leenheer E.M.R. *Genes.* 2022-09. “Hearing Loss in Stickler Syndrome: An Update.” https://doi.org/10.3390/genes13091571 (acke2022hearinglossin pages 2-4)
- Soh Z. et al. 2022-07. “Dominant Stickler Syndrome.” https://doi.org/10.17863/cam.86865 (soh2022dominantsticklersyndrome. pages 1-2)
- Rebello D. et al. *Hum Mol Genet.* 2023-07. “COL11A2 as a candidate gene for vertebral malformations and congenital scoliosis.” https://doi.org/10.1093/hmg/ddad117 (rebello2023col11a2asa pages 1-2)
- Su Y. et al. *Front Genet.* 2023-06. “Case report: autosomal recessive type 3 stickler syndrome caused by compound heterozygous mutations in col11a2.” https://doi.org/10.3389/fgene.2023.1154087 (su2023casereportautosomal pages 1-2)

---

## Evidence gaps (explicit)
- Orphanet/ICD/MeSH identifiers, robust prevalence/incidence estimates for COL11A2-specific subtypes, and standardized COL11A2-specific management guidelines were not available in the retrieved full texts for this run.
- Multi-omics profiling (transcriptomics/proteomics/metabolomics) specific to COL11A2-OSMED/Stickler type 3 was not identified in retrieved sources.


References

1. (soh2022dominantsticklersyndrome. pages 8-10): Zack Soh, Allan J Richards, Annie McNinch, Philip Alexander, Howard Martin, and Martin P Snead. Dominant stickler syndrome. JournalArticle, Jul 2022. URL: https://doi.org/10.17863/cam.86865, doi:10.17863/cam.86865. This article has 46 citations.

2. (selvam2020novelcol11a2pathogenic pages 1-2): Pavalan Selvam, Shekhar Singh, Angita Jain, Herjot Atwal, and Paldeep S. Atwal. Novel col11a2 pathogenic variants in a child with autosomal recessive otospondylomegaepiphyseal dysplasia: a review of the literature. Journal of Pediatric Genetics, 09:117-120, Oct 2020. URL: https://doi.org/10.1055/s-0039-1698446, doi:10.1055/s-0039-1698446. This article has 4 citations and is from a peer-reviewed journal.

3. (su2023casereportautosomal pages 1-2): Ying Su, Chun-Qiong Ran, Zhe-Long Liu, Yan Yang, Gang Yuan, Shu-Hong Hu, Xue-Feng Yu, and Wen-Tao He. Case report: autosomal recessive type 3 stickler syndrome caused by compound heterozygous mutations in col11a2. Frontiers in Genetics, Jun 2023. URL: https://doi.org/10.3389/fgene.2023.1154087, doi:10.3389/fgene.2023.1154087. This article has 4 citations and is from a peer-reviewed journal.

4. (rebello2023col11a2asa pages 2-4): Denise Rebello, Elizabeth Wohler, Vida Erfani, Guozhuang Li, Alexya N Aguilera, Alberto Santiago-Cornier, Sen Zhao, Steven W Hwang, Robert D Steiner, Terry Jianguo Zhang, Christina A Gurnett, Cathleen Raggio, Nan Wu, Nara Sobreira, Philip F Giampietro, and Brian Ciruna. Col11a2 as a candidate gene for vertebral malformations and congenital scoliosis. Human molecular genetics, 32:2913-2928, Jul 2023. URL: https://doi.org/10.1093/hmg/ddad117, doi:10.1093/hmg/ddad117. This article has 19 citations and is from a domain leading peer-reviewed journal.

5. (OpenTargets Search: Stickler syndrome,otospondylomegaepiphyseal dysplasia-COL11A2): Open Targets Query (Stickler syndrome,otospondylomegaepiphyseal dysplasia-COL11A2, 3 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

6. (soh2022dominantsticklersyndrome. pages 1-2): Zack Soh, Allan J Richards, Annie McNinch, Philip Alexander, Howard Martin, and Martin P Snead. Dominant stickler syndrome. JournalArticle, Jul 2022. URL: https://doi.org/10.17863/cam.86865, doi:10.17863/cam.86865. This article has 46 citations.

7. (sheppard2021sticklersyndrome pages 3-4): Mary B. Sheppard and Clair A. Francomano. Stickler syndrome. Cassidy and Allanson's Management of Genetic Syndromes, pages 915-926, Oct 2021. URL: https://doi.org/10.1002/9781119432692.ch56, doi:10.1002/9781119432692.ch56. This article has 0 citations.

8. (acke2022hearinglossin pages 2-4): Frederic R. E. Acke and Els M. R. De Leenheer. Hearing loss in stickler syndrome: an update. Genes, 13:1571, Sep 2022. URL: https://doi.org/10.3390/genes13091571, doi:10.3390/genes13091571. This article has 28 citations.

9. (melkoniemi2000autosomalrecessivedisorder pages 1-2): Miia Melkoniemi, Han G. Brunner, Sylvie Manouvrier, Raoul Hennekam, Andrea Superti-Furga, Helena Kääriäinen, Richard M. Pauli, Ton van Essen, Matthew L. Warman, Jacky Bonaventure, Peter Miny, and Leena Ala-Kokko. Autosomal recessive disorder otospondylomegaepiphyseal dysplasia is associated with loss-of-function mutations in the col11a2 gene. American journal of human genetics, 66 2:368-77, Feb 2000. URL: https://doi.org/10.1086/302750, doi:10.1086/302750. This article has 107 citations and is from a highest quality peer-reviewed journal.

10. (melkoniemi2000autosomalrecessivedisorder pages 6-9): Miia Melkoniemi, Han G. Brunner, Sylvie Manouvrier, Raoul Hennekam, Andrea Superti-Furga, Helena Kääriäinen, Richard M. Pauli, Ton van Essen, Matthew L. Warman, Jacky Bonaventure, Peter Miny, and Leena Ala-Kokko. Autosomal recessive disorder otospondylomegaepiphyseal dysplasia is associated with loss-of-function mutations in the col11a2 gene. American journal of human genetics, 66 2:368-77, Feb 2000. URL: https://doi.org/10.1086/302750, doi:10.1086/302750. This article has 107 citations and is from a highest quality peer-reviewed journal.

11. (selvam2020novelcol11a2pathogenic pages 3-4): Pavalan Selvam, Shekhar Singh, Angita Jain, Herjot Atwal, and Paldeep S. Atwal. Novel col11a2 pathogenic variants in a child with autosomal recessive otospondylomegaepiphyseal dysplasia: a review of the literature. Journal of Pediatric Genetics, 09:117-120, Oct 2020. URL: https://doi.org/10.1055/s-0039-1698446, doi:10.1055/s-0039-1698446. This article has 4 citations and is from a peer-reviewed journal.

12. (melkoniemi2000autosomalrecessivedisorder pages 4-6): Miia Melkoniemi, Han G. Brunner, Sylvie Manouvrier, Raoul Hennekam, Andrea Superti-Furga, Helena Kääriäinen, Richard M. Pauli, Ton van Essen, Matthew L. Warman, Jacky Bonaventure, Peter Miny, and Leena Ala-Kokko. Autosomal recessive disorder otospondylomegaepiphyseal dysplasia is associated with loss-of-function mutations in the col11a2 gene. American journal of human genetics, 66 2:368-77, Feb 2000. URL: https://doi.org/10.1086/302750, doi:10.1086/302750. This article has 107 citations and is from a highest quality peer-reviewed journal.

13. (su2023casereportautosomal pages 6-6): Ying Su, Chun-Qiong Ran, Zhe-Long Liu, Yan Yang, Gang Yuan, Shu-Hong Hu, Xue-Feng Yu, and Wen-Tao He. Case report: autosomal recessive type 3 stickler syndrome caused by compound heterozygous mutations in col11a2. Frontiers in Genetics, Jun 2023. URL: https://doi.org/10.3389/fgene.2023.1154087, doi:10.3389/fgene.2023.1154087. This article has 4 citations and is from a peer-reviewed journal.

14. (micale2020exontrappingassayimproves pages 1-3): Lucia Micale, Silvia Morlino, Annalisa Schirizzi, Emanuele Agolini, Grazia Nardella, Carmela Fusco, Stefano Castellana, Vito Guarnieri, Roberta Villa, Maria Francesca Bedeschi, Paola Grammatico, Antonio Novelli, and Marco Castori. Exon-trapping assay improves clinical interpretation of col11a1 and col11a2 intronic variants in stickler syndrome type 2 and otospondylomegaepiphyseal dysplasia. Genes, 11:1513, Dec 2020. URL: https://doi.org/10.3390/genes11121513, doi:10.3390/genes11121513. This article has 16 citations.

15. (selvam2020novelcol11a2pathogenic media b73d0cc6): Pavalan Selvam, Shekhar Singh, Angita Jain, Herjot Atwal, and Paldeep S. Atwal. Novel col11a2 pathogenic variants in a child with autosomal recessive otospondylomegaepiphyseal dysplasia: a review of the literature. Journal of Pediatric Genetics, 09:117-120, Oct 2020. URL: https://doi.org/10.1055/s-0039-1698446, doi:10.1055/s-0039-1698446. This article has 4 citations and is from a peer-reviewed journal.

16. (acke2022hearinglossin pages 4-6): Frederic R. E. Acke and Els M. R. De Leenheer. Hearing loss in stickler syndrome: an update. Genes, 13:1571, Sep 2022. URL: https://doi.org/10.3390/genes13091571, doi:10.3390/genes13091571. This article has 28 citations.

17. (sheppard2021sticklersyndrome pages 7-8): Mary B. Sheppard and Clair A. Francomano. Stickler syndrome. Cassidy and Allanson's Management of Genetic Syndromes, pages 915-926, Oct 2021. URL: https://doi.org/10.1002/9781119432692.ch56, doi:10.1002/9781119432692.ch56. This article has 0 citations.

18. (melkoniemi2000autosomalrecessivedisorder pages 2-4): Miia Melkoniemi, Han G. Brunner, Sylvie Manouvrier, Raoul Hennekam, Andrea Superti-Furga, Helena Kääriäinen, Richard M. Pauli, Ton van Essen, Matthew L. Warman, Jacky Bonaventure, Peter Miny, and Leena Ala-Kokko. Autosomal recessive disorder otospondylomegaepiphyseal dysplasia is associated with loss-of-function mutations in the col11a2 gene. American journal of human genetics, 66 2:368-77, Feb 2000. URL: https://doi.org/10.1086/302750, doi:10.1086/302750. This article has 107 citations and is from a highest quality peer-reviewed journal.

19. (micale2020exontrappingassayimproves pages 11-13): Lucia Micale, Silvia Morlino, Annalisa Schirizzi, Emanuele Agolini, Grazia Nardella, Carmela Fusco, Stefano Castellana, Vito Guarnieri, Roberta Villa, Maria Francesca Bedeschi, Paola Grammatico, Antonio Novelli, and Marco Castori. Exon-trapping assay improves clinical interpretation of col11a1 and col11a2 intronic variants in stickler syndrome type 2 and otospondylomegaepiphyseal dysplasia. Genes, 11:1513, Dec 2020. URL: https://doi.org/10.3390/genes11121513, doi:10.3390/genes11121513. This article has 16 citations.

20. (li2001targeteddisruptionof pages 3-4): Shi‐Wu Li, Masamine Takanosu, Machiko Arita, Yunhua Bao, Zhao‐Xia Ren, Alfred Maier, Darwin J. Prockop, and Richard Mayne. Targeted disruption of col11a2 produces a mild cartilage phenotype in transgenic mice: comparison with the human disorder otospondylomegaepiphyseal dysplasia (osmed). Developmental Dynamics, 222:141-152, Oct 2001. URL: https://doi.org/10.1002/dvdy.1178, doi:10.1002/dvdy.1178. This article has 59 citations and is from a peer-reviewed journal.

21. (rebello2023col11a2asa pages 4-6): Denise Rebello, Elizabeth Wohler, Vida Erfani, Guozhuang Li, Alexya N Aguilera, Alberto Santiago-Cornier, Sen Zhao, Steven W Hwang, Robert D Steiner, Terry Jianguo Zhang, Christina A Gurnett, Cathleen Raggio, Nan Wu, Nara Sobreira, Philip F Giampietro, and Brian Ciruna. Col11a2 as a candidate gene for vertebral malformations and congenital scoliosis. Human molecular genetics, 32:2913-2928, Jul 2023. URL: https://doi.org/10.1093/hmg/ddad117, doi:10.1093/hmg/ddad117. This article has 19 citations and is from a domain leading peer-reviewed journal.

22. (rebello2023col11a2asa pages 1-2): Denise Rebello, Elizabeth Wohler, Vida Erfani, Guozhuang Li, Alexya N Aguilera, Alberto Santiago-Cornier, Sen Zhao, Steven W Hwang, Robert D Steiner, Terry Jianguo Zhang, Christina A Gurnett, Cathleen Raggio, Nan Wu, Nara Sobreira, Philip F Giampietro, and Brian Ciruna. Col11a2 as a candidate gene for vertebral malformations and congenital scoliosis. Human molecular genetics, 32:2913-2928, Jul 2023. URL: https://doi.org/10.1093/hmg/ddad117, doi:10.1093/hmg/ddad117. This article has 19 citations and is from a domain leading peer-reviewed journal.

23. (rebello2023col11a2asa pages 8-11): Denise Rebello, Elizabeth Wohler, Vida Erfani, Guozhuang Li, Alexya N Aguilera, Alberto Santiago-Cornier, Sen Zhao, Steven W Hwang, Robert D Steiner, Terry Jianguo Zhang, Christina A Gurnett, Cathleen Raggio, Nan Wu, Nara Sobreira, Philip F Giampietro, and Brian Ciruna. Col11a2 as a candidate gene for vertebral malformations and congenital scoliosis. Human molecular genetics, 32:2913-2928, Jul 2023. URL: https://doi.org/10.1093/hmg/ddad117, doi:10.1093/hmg/ddad117. This article has 19 citations and is from a domain leading peer-reviewed journal.

24. (li2001targeteddisruptionof pages 6-8): Shi‐Wu Li, Masamine Takanosu, Machiko Arita, Yunhua Bao, Zhao‐Xia Ren, Alfred Maier, Darwin J. Prockop, and Richard Mayne. Targeted disruption of col11a2 produces a mild cartilage phenotype in transgenic mice: comparison with the human disorder otospondylomegaepiphyseal dysplasia (osmed). Developmental Dynamics, 222:141-152, Oct 2001. URL: https://doi.org/10.1002/dvdy.1178, doi:10.1002/dvdy.1178. This article has 59 citations and is from a peer-reviewed journal.

25. (acke2022hearinglossin pages 6-7): Frederic R. E. Acke and Els M. R. De Leenheer. Hearing loss in stickler syndrome: an update. Genes, 13:1571, Sep 2022. URL: https://doi.org/10.3390/genes13091571, doi:10.3390/genes13091571. This article has 28 citations.

26. (sabir2021diagnosticyieldof pages 2-4): Ataf H. Sabir, Elizabeth Morley, Jameela Sheikh, Alistair D. Calder, Ana Beleza-Meireles, Moira S. Cheung, Alessandra Cocca, Mattias Jansson, Suzanne Lillis, Yogen Patel, Shu Yau, Christine M. Hall, Amaka C. Offiah, and Melita Irving. Diagnostic yield of rare skeletal dysplasia conditions in the radiogenomics era. BMC Medical Genomics, Jun 2021. URL: https://doi.org/10.1186/s12920-021-00993-0, doi:10.1186/s12920-021-00993-0. This article has 23 citations and is from a peer-reviewed journal.

27. (sabir2021diagnosticyieldof pages 9-12): Ataf H. Sabir, Elizabeth Morley, Jameela Sheikh, Alistair D. Calder, Ana Beleza-Meireles, Moira S. Cheung, Alessandra Cocca, Mattias Jansson, Suzanne Lillis, Yogen Patel, Shu Yau, Christine M. Hall, Amaka C. Offiah, and Melita Irving. Diagnostic yield of rare skeletal dysplasia conditions in the radiogenomics era. BMC Medical Genomics, Jun 2021. URL: https://doi.org/10.1186/s12920-021-00993-0, doi:10.1186/s12920-021-00993-0. This article has 23 citations and is from a peer-reviewed journal.

28. (micale2020exontrappingassayimproves pages 3-5): Lucia Micale, Silvia Morlino, Annalisa Schirizzi, Emanuele Agolini, Grazia Nardella, Carmela Fusco, Stefano Castellana, Vito Guarnieri, Roberta Villa, Maria Francesca Bedeschi, Paola Grammatico, Antonio Novelli, and Marco Castori. Exon-trapping assay improves clinical interpretation of col11a1 and col11a2 intronic variants in stickler syndrome type 2 and otospondylomegaepiphyseal dysplasia. Genes, 11:1513, Dec 2020. URL: https://doi.org/10.3390/genes11121513, doi:10.3390/genes11121513. This article has 16 citations.

29. (sheppard2021sticklersyndrome pages 8-9): Mary B. Sheppard and Clair A. Francomano. Stickler syndrome. Cassidy and Allanson's Management of Genetic Syndromes, pages 915-926, Oct 2021. URL: https://doi.org/10.1002/9781119432692.ch56, doi:10.1002/9781119432692.ch56. This article has 0 citations.

30. (gyokova2026prenatalmoleculardiagnosis pages 6-7): Elitsa Gyokova, Eleonora Hristova-Atanasova, Zlatko Kirovakov, and Kamelia Dimitrova. Prenatal molecular diagnosis of col2a1-associated stickler syndrome: genotype–phenotype correlation in a resource-limited healthcare setting. International Journal of Molecular Sciences, 27:2227, Feb 2026. URL: https://doi.org/10.3390/ijms27052227, doi:10.3390/ijms27052227. This article has 0 citations.

31. (sheppard2021sticklersyndrome pages 6-7): Mary B. Sheppard and Clair A. Francomano. Stickler syndrome. Cassidy and Allanson's Management of Genetic Syndromes, pages 915-926, Oct 2021. URL: https://doi.org/10.1002/9781119432692.ch56, doi:10.1002/9781119432692.ch56. This article has 0 citations.

32. (sabir2021diagnosticyieldof pages 1-2): Ataf H. Sabir, Elizabeth Morley, Jameela Sheikh, Alistair D. Calder, Ana Beleza-Meireles, Moira S. Cheung, Alessandra Cocca, Mattias Jansson, Suzanne Lillis, Yogen Patel, Shu Yau, Christine M. Hall, Amaka C. Offiah, and Melita Irving. Diagnostic yield of rare skeletal dysplasia conditions in the radiogenomics era. BMC Medical Genomics, Jun 2021. URL: https://doi.org/10.1186/s12920-021-00993-0, doi:10.1186/s12920-021-00993-0. This article has 23 citations and is from a peer-reviewed journal.
