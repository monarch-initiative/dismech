---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-10T12:54:31.222226'
end_time: '2026-05-10T13:05:27.483233'
duration_seconds: 656.26
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Free Sialic Acid Storage Disease
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 32
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Free Sialic Acid Storage Disease
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Free Sialic Acid Storage Disease** covering all of the
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
- **Disease Name:** Free Sialic Acid Storage Disease
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Free Sialic Acid Storage Disease** covering all of the
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


## Comprehensive Disease Characteristics Report: Free Sialic Acid Storage Disease (FSASD)

### Executive summary
Free sialic acid storage disease (FSASD) refers to an allelic spectrum of autosomal recessive lysosomal transporter disorders caused by biallelic pathogenic variants in **SLC17A5** (encoding **sialin**), leading to **lysosomal accumulation and increased urinary/CSF levels of free sialic acid (Neu5Ac/NANA)** and prominent neurodevelopmental/neurodegenerative manifestations including hypomyelination and cerebellar atrophy. The spectrum includes **Salla disease** (typically milder, often surviving into adulthood) and **infantile sialic acid storage disease / ISSD** (severe, multisystem, often lethal in early childhood). Recent 2023–2024 work has delivered **high-resolution cryo-EM structures of human sialin**, enabling structure-based interpretation of pathogenic mutations and potential therapeutic targeting. (aulanko2023psychiatricsymptomsin pages 1-2, hu2023themolecularmechanism pages 1-2, schmiege2024structureandinhibition pages 1-2, schmiege2023structuresandmechanisms pages 31-36)

| Domain | Entity / finding | Key details | Numeric data | Citation IDs |
|---|---|---|---|---|
| Disease spectrum | Salla disease (SD) | Mildest/slowly progressive lysosomal FSASD; mainly CNS disease with developmental delay, ataxia, cognitive impairment; life expectancy into adulthood | Symptoms often first detected at 3–12 months; >90% of Finnish SD patients carry homozygous SLC17A5 c.115C>T p.Arg39Cys founder variant | (aulanko2023psychiatricsymptomsin pages 1-2, schmiege2023structuresandmechanisms pages 31-36) |
| Disease spectrum | Intermediate / severe Salla phenotypes | Allelic forms between classic SD and ISSD; severe developmental delay with hypomyelination and variable neurologic severity | In a 6-patient series: ages at examination 15 months to 19 years; phenotypes included severe Salla disease (intermediate), Salla disease, and mild Salla disease | (mochel2010elevatedcsfnacetylaspartylglutamate pages 1-2) |
| Disease spectrum | Infantile free sialic acid storage disease (ISSD) | Most severe FSASD; multisystem infantile disorder with facial dysmorphism/coarse features, hepatosplenomegaly/visceromegaly, hypotonia; often lethal early | Typical lifespan usually no more than ~2 years | (schmiege2023structuresandmechanisms pages 31-36, valianpour2004quantificationoffree pages 1-2) |
| Genetics | Causal gene / protein | SLC17A5 encodes sialin, the lysosomal sialic acid transporter; biallelic pathogenic variants cause FSASD | Gene discovered in 1999; protein length 495 aa; chromosome 6q13/q14-q15 region reported | (verheijen1999anewgene pages 1-3, verheijen1999anewgene pages 1-1) |
| Genetics | Inheritance | FSASD/SD/ISSD are autosomal recessive disorders | Finnish SD commonly homozygous for p.Arg39Cys; ISSD and other phenotypes often compound heterozygous or homozygous for other pathogenic alleles | (aulanko2023psychiatricsymptomsin pages 1-2, verheijen1999anewgene pages 1-1, verheijen1999anewgene pages 1-3) |
| Diagnostics | Urine free sialic acid (reference ranges, controls) | Age-dependent urinary free sialic acid ranges support biochemical diagnosis | Controls: 31.3±16.6 mmol/mol creatinine at 0–1 y (range 0.7–56.9; n=20); 21.2±9.8 at 1–3 y (6.3–38.3; n=15); 14.4±8.2 at 3–10 y (1.7–32.9; n=25); 4.6±2.6 above 10 y (0–9.8; n=12) | (valianpour2004quantificationoffree pages 1-2) |
| Diagnostics | Urine free sialic acid (affected individuals) | SSD/FSASD patients show elevated urinary free sialic acid | 3 patients in Valianpour 2004: 111.5, 54.2, 36.1 mmol/mol creatinine at ages 1.2, 3.9, 12 y | (valianpour2004quantificationoffree pages 1-2) |
| Diagnostics | CSF/urine free sialic acid in leukodystrophy workup | Increased FSA in CSF or urine is a marker for FSASD in undiagnosed hypomyelinating leukodystrophy | In 6/41 patients with hypomyelination of unknown etiology, FSA was increased and all had SLC17A5 mutations; CSF FSA 15–40 µmol/L (reference <17); urine FSA 32–182 µmol/mmol creatinine depending on case | (mochel2010elevatedcsfnacetylaspartylglutamate pages 1-2) |
| Diagnostics | CSF NAAG | Elevated CSF N-acetylaspartylglutamate (NAAG) is an additional marker of a hypomyelinating subgroup including FSASD | CSF NAAG 13–114 µmol/L in all 6 SLC17A5-mutated patients (reference <12) | (mochel2010elevatedcsfnacetylaspartylglutamate pages 1-2, mochel2010elevatedcsfnacetylaspartylglutamate media ffd5dd78) |
| Phenotype statistics | Psychiatric symptoms in Salla disease | Psychiatric manifestations are underrecognized but relatively common in long-term SD cohorts | 10/24 (42%) psychiatric symptoms; sleeping disorders 8/24 (32%); aggressive behavior/restlessness 6/24 (25%); off-label antipsychotic use 4/24 (17%); psychosis described in 2 adolescents | (aulanko2023psychiatricsymptomsin pages 1-2) |
| Recent research (2023) | First high-resolution human Sialin structure | Cryo-EM structure explained proton coupling and effects of pathogenic mutations; proposed transport mechanism | 3.4 Å inward-facing partially open structure; identified critical residues E171 and E175 and role of cytosolic helix stabilization | (hu2023themolecularmechanism pages 1-2, hu2023themolecularmechanism pages 6-7) |
| Recent research (2024) | Multiple-state cryo-EM structures and inhibitor binding | Cryo-EM captured apo cytosol-open, apo lumen-open, NAAG-bound, and inhibitor-bound states; clarified dual transport modes | Structures at 3.2 Å (pH 5.0) and 2.8 Å (pH 7.5) for apo WT Sialin; identified Fmoc-Leu-OH inhibitor-binding and residues for sialic acid/NAAG recognition | (schmiege2024structureandinhibition pages 1-2) |
| Real-world implementation | Genomic diagnostics in leukodystrophy programs | Salla disease/FSASD included in leukodystrophy biorepository and WGS studies, supporting use of exome/genome sequencing when MRI suggests white matter disease | WGS leukodystrophy study enrolled 236 subjects; interim 26/34 diagnoses (76.5%, 95% CI 58.8–89.3%) with WGS+standard care in <4 months, showing utility of genome-first diagnostics for rare white matter disorders including Salla disease | (NCT02699190 chunk 1, NCT03047369 chunk 1) |


*Table: This table condenses the main disease entities, genetics, diagnostic biomarkers, phenotype statistics, and 2023–2024 mechanistic advances for free sialic acid storage disorders. It is useful as a database-ready summary with numeric findings and direct context-ID citations.*

---

## 1. Disease Information

### 1.1 What is the disease?
FSASD is a group of lysosomal storage disorders in which defective lysosomal export of free sialic acid results in **abnormal retention of free sialic acid in lysosomes** and **elevated free sialic acid in urine (often also CSF)** with a clinical spectrum ranging from Salla disease to ISSD. (mochel2010elevatedcsfnacetylaspartylglutamate pages 1-2, aulanko2023psychiatricsymptomsin pages 1-2, hu2023themolecularmechanism pages 1-2, verheijen1999anewgene pages 1-3)

### 1.2 Key identifiers
* **OMIM**
  * Salla disease: **OMIM 604369** (aulanko2023psychiatricsymptomsin pages 1-2, mochel2010elevatedcsfnacetylaspartylglutamate pages 1-2)
  * Infantile free sialic acid storage disease (ISSD): **OMIM 269920** (mochel2010elevatedcsfnacetylaspartylglutamate pages 1-2)
  * Causal gene: **SLC17A5 (OMIM 604322)** (zielonka2019acrosssectionalquantitative pages 3-4)
* **MONDO / Orphanet / MeSH / ICD-10/ICD-11**: not retrieved from the accessible full-text sources in this run; should be added from OMIM/Orphanet/MONDO database pages during curation.

### 1.3 Synonyms / alternative names used in the literature
* Free sialic acid storage diseases/disorders (FSASD/FSASDs) (hu2023themolecularmechanism pages 1-2, schmiege2023structuresandmechanisms pages 31-36)
* Sialic acid storage disease (SSD) (valianpour2004quantificationoffree pages 1-2)
* Salla disease; “Finnish disease heritage” disorder (aulanko2023psychiatricsymptomsin pages 1-2)
* Infantile sialic acid storage disease (ISSD) (mochel2010elevatedcsfnacetylaspartylglutamate pages 1-2, valianpour2004quantificationoffree pages 1-2)

### 1.4 Evidence source type
Most clinical characterization derives from **aggregated case reports/case series** and **literature-based cohorts** (e.g., cross-sectional natural history synthesis) rather than EHR-based population studies. (zielonka2019acrosssectionalquantitative pages 3-4, zielonka2019acrosssectionalquantitative pages 2-3)

---

## 2. Etiology

### 2.1 Disease causal factors
**Primary cause (genetic, Mendelian):** biallelic pathogenic variants in **SLC17A5**, encoding the lysosomal membrane transporter **sialin**, cause FSASD. (aulanko2023psychiatricsymptomsin pages 1-2, hu2023themolecularmechanism pages 1-2, verheijen1999anewgene pages 1-3)

**Foundational discovery:** The causal gene was identified in 1999: “**A new gene, encoding an anion transporter, is mutated in sialic acid storage diseases**,” establishing **SLC17A5/sialin** as the disease gene. (verheijen1999anewgene pages 1-1)

### 2.2 Risk factors
* **Genetic risk**: inheritance is autosomal recessive; Finnish founder effect is prominent for Salla disease.
  * In Finland, “**More than 90% of Finnish SD patients are homozygous for the pathogenic SLC17A5 c.115C>T; p.(Arg39Cys) … founder variant**.” (aulanko2023psychiatricsymptomsin pages 1-2)

* **Environmental risk factors / protective factors / gene–environment**: no specific environmental modifiers were identified in the retrieved sources; disease is primarily monogenic with severity driven largely by genotype and biochemical burden. Genotype–phenotype correlation has been discussed historically. (aula2000thespectrumof pages 9-9, aulanko2023psychiatricsymptomsin pages 1-2)

---

## 3. Phenotypes

### 3.1 Core phenotype spectrum (human)
**Salla disease (milder end of spectrum):** intellectual disability, ataxia, athetosis, nystagmus, and CNS demyelination/dysmyelination, with typical symptom detection in infancy.
* “**Salla disease (SD) is a rare lysosomal storage disorder characterised by intellectual disability ataxia, athetosis, nystagmus, and central nervous system demyelination**.” (aulanko2023psychiatricsymptomsin pages 1-2)
* “**The first symptoms are typically detected between the ages of 3–12 months**.” (aulanko2023psychiatricsymptomsin pages 1-2)

**ISSD (severe infantile form):** multisystem involvement with visceromegaly and coarse facial features; poor survival.
* ISSD is described as “clinically distinct and very serious… visceromegaly, coarse facial features, failure to thrive, and early death.” (valianpour2004quantificationoffree pages 1-2)

**Neuroimaging phenotype:** in FSASD/Salla disease, MRI frequently shows hypomyelination and atrophy.
* In undiagnosed leukodystrophy presentations, symptoms are “associated with **diffuse supratentorial hypomyelination, thin corpus callosum, and cortical and cerebellar atrophy**.” (mochel2010elevatedcsfnacetylaspartylglutamate pages 1-2)
* In a literature cohort, MRI abnormalities included brain atrophy (19.8%), hypomyelination (19%), and corpus callosum thinning (13.8%). (zielonka2019acrosssectionalquantitative pages 4-6)

### 3.2 Psychiatric/behavioral features (recent quantitative data)
A 24-patient Salla disease cohort review found psychiatric symptoms are common:
* “**Psychiatric symptoms were frequently associated with SD (10/24, 42%)**,” with sleeping disorders 8/24 (32%), aggressive behavior/restlessness 6/24 (25%), and off-label antipsychotic medication 4/24 (17%). (aulanko2023psychiatricsymptomsin pages 1-2)

### 3.3 Suggested HPO terms (non-exhaustive; for knowledge-base mapping)
* Intellectual disability (HP:0001249)
* Global developmental delay (HP:0001263)
* Nystagmus (HP:0000639)
* Cerebellar ataxia (HP:0001251)
* Hypotonia (HP:0001252)
* Spasticity (HP:0001257)
* Seizures (HP:0001250)
* Hypomyelination (HP:0003429)
* Thin corpus callosum / corpus callosum hypoplasia (HP:0002079 / HP:0002079-related)
* Cerebellar atrophy (HP:0001272)
* Hepatosplenomegaly (HP:0001433)
* Coarse facial features (HP:0000280)
* Psychosis (HP:0000709)
* Sleep disturbance (HP:0002360)

### 3.4 Quality-of-life impact
Direct QoL instrument data (EQ-5D/SF-36/PROMIS) were not located in retrieved texts; functional dependence and behavioral symptoms indicate high caregiver burden, and some individuals require assistance with activities of daily living. (aulanko2023psychiatricsymptomsin pages 1-2)

---

## 4. Genetic / Molecular Information

### 4.1 Causal gene
* **SLC17A5** (solute carrier family 17 member 5), encoding **sialin**—a transporter within the SLC17 family / major facilitator superfamily fold. (hu2023themolecularmechanism pages 1-2, schmiege2024structureandinhibition pages 1-2, verheijen1999anewgene pages 1-3)

### 4.2 Pathogenic variants and variant classes (examples from primary sources)
* **Founder variant in Finnish Salla disease:** c.115C>T, p.Arg39Cys. (aulanko2023psychiatricsymptomsin pages 1-2, verheijen1999anewgene pages 1-3)
* **ISSD-associated alleles** include truncating/frameshift and other missense variants in SLC17A5 (examples shown in the original gene discovery table). (verheijen1999anewgene pages 1-3)

Because ClinVar/gnomAD/HGMD were not directly queried via tools in this run, **allele frequencies and ClinVar pathogenicity classifications** are not provided here; they should be filled from ClinVar/gnomAD during curation.

### 4.3 Functional consequences
Pathogenic SLC17A5 variants impair lysosomal export of free sialic acid, causing storage.
* FSASD are characterized by “**enlarged cellular lysosomes and elevated levels of free sialic acids in urine**.” (hu2023themolecularmechanism pages 1-2)

Recent structural work provides mechanistic explanations for pathogenic mutations:
* 2023 cryo-EM work: “**By mapping known pathogenic mutations, we provide mechanistic explanations for corresponding functional defects**.” (hu2023themolecularmechanism pages 1-2)

### 4.4 Suggested GO terms (biological process; examples)
* Lysosomal transport (GO:0007040 / related)
* Carbohydrate derivative transport (GO:1901264)
* Lysosome organization (GO:0007040-related)
* Myelination (GO:0042552)

### 4.5 Suggested GO cellular component terms
* Lysosome (GO:0005764)
* Lysosomal membrane (GO:0005765)
* Synaptic vesicle (GO:0008021) (given sialin’s neurotransmitter transport roles) (schmiege2024structureandinhibition pages 1-2)

---

## 5. Environmental Information
No disease-specific environmental, lifestyle, or infectious triggers/protectors were identified in the retrieved sources; FSASD is primarily a monogenic lysosomal transporter disorder. (aulanko2023psychiatricsymptomsin pages 1-2, verheijen1999anewgene pages 1-3)

---

## 6. Mechanism / Pathophysiology

### 6.1 Core causal chain (current understanding)
1. **Biallelic SLC17A5 variants** →
2. **Defective sialin function** (lysosomal sialic acid exporter / proton-coupled transporter) →
3. **Retention/accumulation of free sialic acid in lysosomes**, with **elevated free sialic acid in urine and/or CSF** →
4. Downstream CNS pathology including **hypomyelination, thin corpus callosum, cortical/cerebellar atrophy**, and progressive neurodevelopmental impairment. (mochel2010elevatedcsfnacetylaspartylglutamate pages 1-2, hu2023themolecularmechanism pages 1-2, schmiege2024structureandinhibition pages 1-2)

### 6.2 Biochemical abnormalities and diagnostic markers
* “**The increase of free sialic acid in urine has been considered the biochemical hallmark**.” (mochel2010elevatedcsfnacetylaspartylglutamate pages 1-2)
* In a leukodystrophy workup study, CSF NAAG was elevated in all SLC17A5-mutated patients (see §10 Diagnostics for numeric ranges). (mochel2010elevatedcsfnacetylaspartylglutamate pages 1-2, mochel2010elevatedcsfnacetylaspartylglutamate media ffd5dd78)

### 6.3 Recent mechanistic developments (prioritize 2023–2024)
**2023 (Science Advances; published 20 Jan 2023; URL in BibTeX):** first high-resolution human SLC17 family structure.
* Abstract quote: “**we present the structure of human Sialin… determined by cryo–electron microscopy, representing the first high-resolution structure of any human SLC17 member**.” (hu2023themolecularmechanism pages 1-2)
* Abstract quote: “**The H+ coupling/sensing requires two highly conserved Glu residues (E171 and E175)**…” (hu2023themolecularmechanism pages 1-2)

**2024 (Nature Communications; accepted 3 May 2024; DOI URL):** multiple conformational states and inhibitor binding.
* Abstract quote: “**we present the cryogenic electron-microscopy structures of human Sialin: apo cytosol-open, apo lumen-open, NAAG–bound, and inhibitor–bound**.” (schmiege2024structureandinhibition pages 1-2)
* The work identifies an inhibitor-binding mode (“Sialin inhibitor Fmoc-Leu-OH”) and residues governing substrate recognition, supporting structure-guided drug discovery. (schmiege2024structureandinhibition pages 1-2)

### 6.4 Molecular profiling (available evidence)
Although beyond 2024, recent disease-modeling indicates glycosphingolipid (GSL) metabolism perturbation in patient iPSC-derived neural cells with striking astrocyte changes.
* Free sialic acid elevations vs controls were reported across cell types, including mature astrocytes (830% of healthy donors). (sabir2025lysosomalfreesialic pages 2-3)

### 6.5 Suggested cell types (CL terms; examples)
* Oligodendrocyte (CL:0000128) (white-matter pathology)
* Astrocyte (CL:0000127) (recent iPSC modeling suggests mature astrocyte vulnerability) (sabir2025lysosomalfreesialic pages 2-3)
* Neuron (CL:0000540)

---

## 7. Anatomical Structures Affected

### 7.1 Organ/system level
Primary: **central nervous system (brain white matter, cerebellum)** with hypomyelination and atrophy. (mochel2010elevatedcsfnacetylaspartylglutamate pages 1-2)

Secondary/multisystem (especially ISSD): **visceromegaly/hepatosplenomegaly** and coarse facial features. (valianpour2004quantificationoffree pages 1-2, verheijen1999anewgene pages 1-1)

### 7.2 Suggested UBERON terms (examples)
* Brain (UBERON:0000955)
* Cerebellum (UBERON:0002037)
* Corpus callosum (UBERON:0002330)
* Liver (UBERON:0002107)
* Spleen (UBERON:0002106)

### 7.3 Subcellular localization
Lysosomal lumen/membrane involvement is central (lysosomal free sialic acid accumulation; lysosomal membrane transporter). (schmiege2024structureandinhibition pages 1-2)

---

## 8. Temporal Development

### 8.1 Onset
In a large literature-based cohort (postnatally diagnosed), median onset was **0.17 years (~2 months)**. (zielonka2019acrosssectionalquantitative pages 1-2)

In Salla disease specifically, first symptoms are “**typically detected between the ages of 3–12 months**.” (aulanko2023psychiatricsymptomsin pages 1-2)

### 8.2 Progression and disease course
FSASD demonstrates a continuous phenotypic spectrum; ISSD is rapidly progressive with early mortality, while Salla disease can allow survival into adulthood. (hu2023themolecularmechanism pages 1-2, schmiege2023structuresandmechanisms pages 31-36, zielonka2019acrosssectionalquantitative pages 1-2)

### 8.3 Critical periods
Prenatal and perinatal manifestations occur in a substantial subset:
* Hydrops fetalis occurred as the first clinical sign in **20.7%** of cases in the literature cohort. (zielonka2019acrosssectionalquantitative pages 3-4, zielonka2019acrosssectionalquantitative pages 2-3)

---

## 9. Inheritance and Population

### 9.1 Inheritance
Autosomal recessive inheritance is consistently reported for Salla disease/FSASD.
* “**Salla disease… is a rare autosomal recessive lysosomal storage disorder**…” (aulanko2023psychiatricsymptomsin pages 1-2)

### 9.2 Epidemiology
Robust prevalence/incidence estimates were not retrieved from Orphanet/registry pages in this run; however:
* Literature synthesis notes Orphanet-listed case counts (~130 known cases) and panethnic distribution. (zielonka2019acrosssectionalquantitative pages 1-2, zielonka2019acrosssectionalquantitative pages 4-6)
* Salla disease is enriched in Finland (“Finnish disease heritage”), with the p.Arg39Cys founder variant accounting for >90% of Finnish SD cases. (aulanko2023psychiatricsymptomsin pages 1-2)

### 9.3 Sex ratio and demographics
A Finnish hospital-based cohort of 24 Salla disease patients was 75% male (18/24). This may reflect ascertainment/registry bias rather than true sex skew given autosomal recessive inheritance. (aulanko2023psychiatricsymptomsin pages 1-2)

---

## 10. Diagnostics

### 10.1 Biochemical testing (real-world implementations)
**Urine free sialic acid** quantification is central.
* A 2004 Clinical Chemistry method paper states: “**Defective free sialic acid transport can be established by quantification of free sialic acid in urine**.” (valianpour2004quantificationoffree pages 1-2)
* Age-dependent control ranges were established (n=72 controls). For example, ages 0–1 year: mean 31.3 mmol/mol creatinine (range 0.7–56.9; n=20). (valianpour2004quantificationoffree pages 1-2)
* In three SSD patients aged 1.2, 3.9, 12 years, urinary free sialic acid concentrations were 111.5, 54.2, and 36.1 mmol/mol creatinine. (valianpour2004quantificationoffree pages 1-2)

**CSF/urine screening in leukodystrophy workups:**
* In a cross-sectional leukodystrophy cohort (41 patients with hypomyelination of unknown etiology), **6/41** had increased free sialic acid in CSF or urine and all had SLC17A5 mutations. (mochel2010elevatedcsfnacetylaspartylglutamate pages 1-2)

**CSF NAAG as supportive biomarker:**
* “**H-NMRS revealed an increase of N-acetylaspartylglutamate in the CSF of all patients with SLC17A5 mutation (range 13–114 µmol/L, reference <12 µmol/L)**.” (mochel2010elevatedcsfnacetylaspartylglutamate pages 1-2)

Visual evidence for the Mochel et al. biochemical table and MR spectrum is available in the extracted figure/table crops. (mochel2010elevatedcsfnacetylaspartylglutamate media ffd5dd78, mochel2010elevatedcsfnacetylaspartylglutamate media de78242d)

### 10.2 Genetic testing
Diagnosis is confirmed by identifying biallelic pathogenic variants in SLC17A5.
* Foundational mutation discovery and examples (including R39C) were reported in 1999, with a mutation table for SD and ISSD. (verheijen1999anewgene pages 1-3)

For leukodystrophy presentations, **genome/exome-first strategies** are increasingly implemented in clinical programs that include Salla disease among target conditions.
* Clinical WGS study (LeukoSEQ; completed) enrolled 236 participants; interim analysis described diagnostic efficacy of WGS+standard care at 26/34 (76.5%; 95% CI 58.8–89.3%) within <4 months and faster time to diagnosis than standard care alone. (NCT02699190 chunk 1)

### 10.3 Differential diagnosis
Not comprehensively enumerated in retrieved sources; key differentials in hypomyelinating leukodystrophy evaluations include other genetic white-matter disorders. (mochel2010elevatedcsfnacetylaspartylglutamate pages 1-2, NCT02699190 chunk 1)

### 10.4 Screening
Not a standard newborn screening condition in the retrieved sources; prenatal presentation (hydrops fetalis) supports consideration in prenatal/NIHF workups with biochemical/genetic testing. (zielonka2019acrosssectionalquantitative pages 3-4)

---

## 11. Outcome / Prognosis

A 2019 quantitative natural-history analysis (116 published cases; 106 postnatally diagnosed) reported:
* **Median survival 11 years** (postnatally diagnosed subset). (zielonka2019acrosssectionalquantitative pages 3-4, zielonka2019acrosssectionalquantitative pages 2-3)
* **Median age at diagnosis 3 years** and **median diagnostic delay 2.5 years** (subset N=90 with data). (zielonka2019acrosssectionalquantitative pages 3-4, zielonka2019acrosssectionalquantitative pages 2-3)

Biomarker severity correlates with outcome:
* Urinary free sialic acid excretion <6.37-fold of normal (and fibroblast storage <7.37-fold) was associated with significantly longer survival in recursive partitioning analyses. (zielonka2019acrosssectionalquantitative pages 3-4)

---

## 12. Treatment

### 12.1 Current standard of care
No disease-modifying therapy was identified in the retrieved sources; management is primarily symptomatic/supportive.
* A lysosomal transporter review/thesis summary notes: “**Currently, there are only symptomatic treatments for these FSASDs**.” (schmiege2023structuresandmechanisms pages 31-36)
* 2019 natural-history synthesis reported no clinical trials or orphan drug designations as of 31 Dec 2017. (zielonka2019acrosssectionalquantitative pages 1-2, zielonka2019acrosssectionalquantitative pages 4-6)

### 12.2 Experimental/forward-looking approaches (expert analysis)
Structural biology now enables rational exploration of small-molecule modulation and mutation-specific rescue.
* 2024 Nature Communications work reports an “inhibitor–bound” structure and identifies a sialin inhibitor (Fmoc-Leu-OH), providing a foothold for structure-guided ligand development (though not yet a therapy). (schmiege2024structureandinhibition pages 1-2)

### 12.3 Suggested MAXO terms (examples)
* Supportive care (MAXO:0000004)
* Physical therapy (MAXO:0000014)
* Occupational therapy (MAXO:0000015)
* Genetic counseling (MAXO:0000071)
* Whole genome sequencing (MAXO:0000126)

---

## 13. Prevention

Primary prevention is not applicable in the usual sense for a recessive Mendelian disorder; prevention focuses on **genetic counseling and reproductive options**.
* Given autosomal recessive inheritance, family-based **carrier testing and prenatal diagnosis** are standard preventive strategies, especially in founder populations; prenatal/pregnancy presentations (hydrops fetalis) reinforce this clinical need. (aulanko2023psychiatricsymptomsin pages 1-2, zielonka2019acrosssectionalquantitative pages 3-4)

---

## 14. Other Species / Natural Disease
No naturally occurring veterinary disease analogs were identified in the retrieved sources.

---

## 15. Model Organisms

A sialin-deficient mouse model is referenced in natural-history synthesis:
* “sialin-/- mice show progressive leukoencephalopathy with decreased myelinated axons, oligodendrocyte apoptosis… coordination defects, seizures, and premature death.” (zielonka2019acrosssectionalquantitative pages 1-2, zielonka2019acrosssectionalquantitative pages 4-6)

Cellular models include patient-derived iPSC neural differentiation platforms (two FSASD lines vs two controls) enabling mechanistic studies of cell-type vulnerability (notably astrocytes). (sabir2025lysosomalfreesialic pages 1-2, sabir2025lysosomalfreesialic pages 2-3)

---

## Notes on evidence limitations (important for knowledge-base curation)
* **PMIDs** were not available in the tool-returned full texts for most citations in this run; DOIs/URLs and publication timing are provided from the retrieved PDFs/records. Curators should augment with PMIDs from PubMed.
* **MONDO/Orphanet/MeSH/ICD** identifiers were not retrievable from the accessible texts; these should be populated directly from the corresponding ontology/database pages.

---

## Key primary sources (with URLs and dates as available from retrieved texts)
* Verheijen et al. *Nature Genetics* (Dec 1999). “A new gene… mutated in sialic acid storage diseases.” https://doi.org/10.1038/70585 (verheijen1999anewgene pages 1-3)
* Valianpour et al. *Clinical Chemistry* (Feb 2004). Urine free sialic acid quantification by HPLC–MS/MS. https://doi.org/10.1373/clinchem.2003.027169 (valianpour2004quantificationoffree pages 1-2)
* Mochel et al. *Neurology* (Jan 2010). CSF NAAG elevation and 6/41 leukodystrophy screening yield. https://doi.org/10.1212/WNL.0b013e3181cbcdc4 (mochel2010elevatedcsfnacetylaspartylglutamate pages 1-2)
* Zielonka et al. *Genetics in Medicine* (Feb 2019). Natural history synthesis (116 cases; median survival 11 years). https://doi.org/10.1038/s41436-018-0051-3 (zielonka2019acrosssectionalquantitative pages 3-4)
* Hu et al. *Science Advances* (20 Jan 2023). First high-resolution human sialin structure. https://doi.org/10.1126/sciadv.ade8346 (hu2023themolecularmechanism pages 1-2)
* Aulanko et al. *European Child & Adolescent Psychiatry* (published online 7 Jul 2022; journal issue 2023). Psychiatric symptoms (10/24, 42%). https://doi.org/10.1007/s00787-022-02031-5 (aulanko2023psychiatricsymptomsin pages 1-2)
* Schmiege et al. *Nature Communications* (May 2024). Multiple-state structures and inhibition. https://doi.org/10.1038/s41467-024-48535-3 (schmiege2024structureandinhibition pages 1-2)


References

1. (aulanko2023psychiatricsymptomsin pages 1-2): Ida Aulanko, Elisa Rahikkala, and Jukka Moilanen. Psychiatric symptoms in salla disease. European Child & Adolescent Psychiatry, 32:2043-2047, Jul 2023. URL: https://doi.org/10.1007/s00787-022-02031-5, doi:10.1007/s00787-022-02031-5. This article has 4 citations and is from a domain leading peer-reviewed journal.

2. (hu2023themolecularmechanism pages 1-2): Wenxin Hu, Congwu Chi, Kunhua Song, and Hongjin Zheng. The molecular mechanism of sialic acid transport mediated by sialin. Science Advances, Jan 2023. URL: https://doi.org/10.1126/sciadv.ade8346, doi:10.1126/sciadv.ade8346. This article has 27 citations and is from a highest quality peer-reviewed journal.

3. (schmiege2024structureandinhibition pages 1-2): Philip Schmiege, Linda Donnelly, Nadia Elghobashi-Meinhardt, Chia-Hsueh Lee, and Xiaochun Li. Structure and inhibition of the human lysosomal transporter sialin. Nature Communications, May 2024. URL: https://doi.org/10.1038/s41467-024-48535-3, doi:10.1038/s41467-024-48535-3. This article has 13 citations and is from a highest quality peer-reviewed journal.

4. (schmiege2023structuresandmechanisms pages 31-36): PFP Schmiege. Structures and mechanisms of lysosomal transporters. Unknown journal, 2023.

5. (mochel2010elevatedcsfnacetylaspartylglutamate pages 1-2): F. Mochel, U.F.H. Engelke, J. Barritault, B. Yang, N. H. McNeill, J. N. Thompson, A. Vanderver, N. I. Wolf, M. A. Willemsen, F. W. Verheijen, F. Seguin, R. A. Wevers, and R. Schiffmann. Elevated csf n-acetylaspartylglutamate in patients with free sialic acid storage diseases. Neurology, 74:302-305, Jan 2010. URL: https://doi.org/10.1212/wnl.0b013e3181cbcdc4, doi:10.1212/wnl.0b013e3181cbcdc4. This article has 32 citations and is from a highest quality peer-reviewed journal.

6. (valianpour2004quantificationoffree pages 1-2): Fredoen Valianpour, Nicolaas G G M Abeling, Marinus Duran, Jan G M Huijmans, and Willem Kulik. Quantification of free sialic acid in urine by hplc-electrospray tandem mass spectrometry: a tool for the diagnosis of sialic acid storage disease. Clinical chemistry, 50 2:403-9, Feb 2004. URL: https://doi.org/10.1373/clinchem.2003.027169, doi:10.1373/clinchem.2003.027169. This article has 58 citations and is from a highest quality peer-reviewed journal.

7. (verheijen1999anewgene pages 1-3): Frans W. Verheijen, Elly Verbeek, Nina Aula, Cecile E.M.T. Beerens, Adrie C. Havelaar, Marijke Joosse, Leena Peltonen, Pertti Aula, Hans Galjaard, Peter J. van der Spek, and Grazia M.S. Mancini. A new gene, encoding an anion transporter, is mutated in sialic acid storage diseases. Nature Genetics, 23:462-465, Dec 1999. URL: https://doi.org/10.1038/70585, doi:10.1038/70585. This article has 351 citations and is from a highest quality peer-reviewed journal.

8. (verheijen1999anewgene pages 1-1): Frans W. Verheijen, Elly Verbeek, Nina Aula, Cecile E.M.T. Beerens, Adrie C. Havelaar, Marijke Joosse, Leena Peltonen, Pertti Aula, Hans Galjaard, Peter J. van der Spek, and Grazia M.S. Mancini. A new gene, encoding an anion transporter, is mutated in sialic acid storage diseases. Nature Genetics, 23:462-465, Dec 1999. URL: https://doi.org/10.1038/70585, doi:10.1038/70585. This article has 351 citations and is from a highest quality peer-reviewed journal.

9. (mochel2010elevatedcsfnacetylaspartylglutamate media ffd5dd78): F. Mochel, U.F.H. Engelke, J. Barritault, B. Yang, N. H. McNeill, J. N. Thompson, A. Vanderver, N. I. Wolf, M. A. Willemsen, F. W. Verheijen, F. Seguin, R. A. Wevers, and R. Schiffmann. Elevated csf n-acetylaspartylglutamate in patients with free sialic acid storage diseases. Neurology, 74:302-305, Jan 2010. URL: https://doi.org/10.1212/wnl.0b013e3181cbcdc4, doi:10.1212/wnl.0b013e3181cbcdc4. This article has 32 citations and is from a highest quality peer-reviewed journal.

10. (hu2023themolecularmechanism pages 6-7): Wenxin Hu, Congwu Chi, Kunhua Song, and Hongjin Zheng. The molecular mechanism of sialic acid transport mediated by sialin. Science Advances, Jan 2023. URL: https://doi.org/10.1126/sciadv.ade8346, doi:10.1126/sciadv.ade8346. This article has 27 citations and is from a highest quality peer-reviewed journal.

11. (NCT02699190 chunk 1): Adeline Vanderver, MD. LeukoSEQ: Whole Genome Sequencing as a First-Line Diagnostic Tool for Leukodystrophies. Children's Hospital of Philadelphia. 2017. ClinicalTrials.gov Identifier: NCT02699190

12. (NCT03047369 chunk 1): Adeline Vanderver, MD. The Myelin Disorders Biorepository Project. Children's Hospital of Philadelphia. 2016. ClinicalTrials.gov Identifier: NCT03047369

13. (zielonka2019acrosssectionalquantitative pages 3-4): Matthias Zielonka, Sven F. Garbade, Stefan Kölker, Georg F. Hoffmann, and Markus Ries. A cross-sectional quantitative analysis of the natural history of free sialic acid storage disease—an ultra-orphan multisystemic lysosomal storage disorder. Genetics in Medicine, 21:347-352, Feb 2019. URL: https://doi.org/10.1038/s41436-018-0051-3, doi:10.1038/s41436-018-0051-3. This article has 31 citations and is from a highest quality peer-reviewed journal.

14. (zielonka2019acrosssectionalquantitative pages 2-3): Matthias Zielonka, Sven F. Garbade, Stefan Kölker, Georg F. Hoffmann, and Markus Ries. A cross-sectional quantitative analysis of the natural history of free sialic acid storage disease—an ultra-orphan multisystemic lysosomal storage disorder. Genetics in Medicine, 21:347-352, Feb 2019. URL: https://doi.org/10.1038/s41436-018-0051-3, doi:10.1038/s41436-018-0051-3. This article has 31 citations and is from a highest quality peer-reviewed journal.

15. (aula2000thespectrumof pages 9-9): Nina Aula, Pirjo Salomäki, Ritva Timonen, Frans Verheijen, Grazia Mancini, Jan-Eric Månsson, Pertti Aula, and Leena Peltonen. The spectrum of slc17a5-gene mutations resulting in free sialic acid-storage diseases indicates some genotype-phenotype correlation. American journal of human genetics, 67 4:832-40, Oct 2000. URL: https://doi.org/10.1086/303077, doi:10.1086/303077. This article has 144 citations and is from a highest quality peer-reviewed journal.

16. (zielonka2019acrosssectionalquantitative pages 4-6): Matthias Zielonka, Sven F. Garbade, Stefan Kölker, Georg F. Hoffmann, and Markus Ries. A cross-sectional quantitative analysis of the natural history of free sialic acid storage disease—an ultra-orphan multisystemic lysosomal storage disorder. Genetics in Medicine, 21:347-352, Feb 2019. URL: https://doi.org/10.1038/s41436-018-0051-3, doi:10.1038/s41436-018-0051-3. This article has 31 citations and is from a highest quality peer-reviewed journal.

17. (sabir2025lysosomalfreesialic pages 2-3): M. Sabir, V. Jovanovic, Seungmi Ryu, Chaitali Sen, Pinar Ormanoglu, Laura Pollard, Richard Steet, William A. Gahl, M. Huizing, Carlos A. Tristan, Frances M. Platt, and M. Malicdan. Lysosomal free sialic acid storage disorder ipsc-derived neural cells display altered glycosphingolipid metabolism. Scientific Reports, Aug 2025. URL: https://doi.org/10.1038/s41598-025-12682-4, doi:10.1038/s41598-025-12682-4. This article has 2 citations and is from a peer-reviewed journal.

18. (zielonka2019acrosssectionalquantitative pages 1-2): Matthias Zielonka, Sven F. Garbade, Stefan Kölker, Georg F. Hoffmann, and Markus Ries. A cross-sectional quantitative analysis of the natural history of free sialic acid storage disease—an ultra-orphan multisystemic lysosomal storage disorder. Genetics in Medicine, 21:347-352, Feb 2019. URL: https://doi.org/10.1038/s41436-018-0051-3, doi:10.1038/s41436-018-0051-3. This article has 31 citations and is from a highest quality peer-reviewed journal.

19. (mochel2010elevatedcsfnacetylaspartylglutamate media de78242d): F. Mochel, U.F.H. Engelke, J. Barritault, B. Yang, N. H. McNeill, J. N. Thompson, A. Vanderver, N. I. Wolf, M. A. Willemsen, F. W. Verheijen, F. Seguin, R. A. Wevers, and R. Schiffmann. Elevated csf n-acetylaspartylglutamate in patients with free sialic acid storage diseases. Neurology, 74:302-305, Jan 2010. URL: https://doi.org/10.1212/wnl.0b013e3181cbcdc4, doi:10.1212/wnl.0b013e3181cbcdc4. This article has 32 citations and is from a highest quality peer-reviewed journal.

20. (sabir2025lysosomalfreesialic pages 1-2): M. Sabir, V. Jovanovic, Seungmi Ryu, Chaitali Sen, Pinar Ormanoglu, Laura Pollard, Richard Steet, William A. Gahl, M. Huizing, Carlos A. Tristan, Frances M. Platt, and M. Malicdan. Lysosomal free sialic acid storage disorder ipsc-derived neural cells display altered glycosphingolipid metabolism. Scientific Reports, Aug 2025. URL: https://doi.org/10.1038/s41598-025-12682-4, doi:10.1038/s41598-025-12682-4. This article has 2 citations and is from a peer-reviewed journal.