---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-11T11:04:56.086101'
end_time: '2026-05-11T11:20:39.224732'
duration_seconds: 943.14
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: MPDU1-congenital disorder of glycosylation
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 29
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** MPDU1-congenital disorder of glycosylation
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **MPDU1-congenital disorder of glycosylation** covering all of the
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
- **Disease Name:** MPDU1-congenital disorder of glycosylation
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **MPDU1-congenital disorder of glycosylation** covering all of the
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


## MPDU1-congenital disorder of glycosylation (MPDU1-CDG; historical CDG-If): comprehensive disease characteristics report

### Executive summary
MPDU1-congenital disorder of glycosylation is an ultra-rare, autosomal recessive disorder of endoplasmic-reticulum (ER) glycosylation caused by biallelic pathogenic variants in **MPDU1** (mannose-P-dolichol utilization defect 1). The central defect is impaired **utilization/bioavailability of dolichol-phosphate–linked sugar donors** (Dol-P-Man and Dol-P-Glc) required for N-glycosylation, with secondary disruption of other glycosylation-dependent pathways (including α-dystroglycan O-mannosylation and GPI-anchor maturation), producing a multisystem phenotype (neurodevelopmental delay, seizures, hypotonia, skin and ocular disease, hepatic/biliary disease, cardiomyopathy, and hematologic/coagulation abnormalities). Core diagnostic evidence includes a **CDG type I transferrin pattern** and a characteristic **lipid-linked oligosaccharide (LLO) profile** with accumulation of truncated intermediates (Man5GlcNAc2 and Man9GlcNAc2). (tol2019amutationin pages 1-2, tol2019amutationin pages 6-8, schenk2003mpdu1mutationsunderlie pages 6-8)

### Key identifiers and nomenclature (disease information)
**Disease name:** MPDU1-congenital disorder of glycosylation (OpenTargets Search: MPDU1-congenital disorder of glycosylation,congenital disorder of glycosylation-MPDU1)

**Key identifiers (available from tool-supported sources in this report):**
- **MONDO:** **MONDO:0012211** (“MPDU1-congenital disorder of glycosylation”) (OpenTargets Search: MPDU1-congenital disorder of glycosylation,congenital disorder of glycosylation-MPDU1)

**Historical/alternative names and synonyms (from primary/review literature):**
- **CDG-If / CDG-1f** (older CDG nomenclature) (tol2019amutationin pages 6-8, schenk2003mpdu1mutationsunderlie pages 1-2)
- **mannose-P-dolichol utilization defect 1**; MPDU1 is also referred to as the human homolog of hamster **Lec35** (haeuptle2009congenitaldisordersof pages 9-10, kranz2001amutationin pages 1-2)

**Evidence origin:** Most MPDU1-CDG disease knowledge is derived from individual case reports/series and small institutional cohorts rather than large EHR-derived datasets or population registries (tol2019amutationin pages 6-8, teneiji2017phenotypicandgenotypic pages 10-14).

**Important limitation:** OMIM/Orphanet/ICD identifiers were not directly retrievable using the available tools in this run; therefore, they are not asserted here.

### 1) Key concepts and definitions (current understanding)

#### Congenital disorders of glycosylation (CDG) and “CDG type I pattern”
MPDU1-CDG is classified among disorders of **N-glycan assembly/ER glycosylation** that typically produce a **CDG type I** serum transferrin pattern (reflecting under-occupancy of N-glycosylation sites). In the MPDU1 cases described, transferrin analysis showed reduced fully sialylated transferrin and increased asialo-/disialotransferrin. (tol2019amutationin pages 5-6, schenk2003mpdu1mutationsunderlie pages 5-6)

#### MPDU1 function and the dolichol-linked donor concept
MPDU1 encodes an ER membrane protein required for **efficient utilization** (bioavailability/presentation) of the lipid-linked monosaccharide donors **dolichol-P-mannose (Dol-P-Man)** and **dolichol-P-glucose (Dol-P-Glc)** in the ER. Evidence from patient cells and complementation experiments supports a role in **lateral distribution/chaperoning** of dolichol-linked donors rather than a simple “flippase” that translocates them across the ER membrane. (schenk2003mpdu1mutationsunderlie pages 6-8, kranz2001amutationin pages 5-7, kranz2001amutationin pages 1-2)

### 2) Etiology (causal factors, risk/protective factors, GxE)

#### Disease causal factors
- **Genetic etiology:** biallelic pathogenic variants in **MPDU1** cause MPDU1-CDG. The earliest definitive causal demonstrations used patient fibroblasts showing abnormal LLO profiles and **functional rescue** after expression of wild-type MPDU1/Lec35 cDNA. (schenk2003mpdu1mutationsunderlie pages 6-8, schenk2003mpdu1mutationsunderlie pages 1-2)

#### Inheritance and risk factors
- **Autosomal recessive inheritance** is supported by homozygous affected individuals with heterozygous parents, and by compound heterozygosity in some reported families. (kranz2001amutationin pages 5-7, schenk2003mpdu1mutationsunderlie pages 5-6)
- **Consanguinity** is reported in at least one family with homozygous p.G73E. (tol2019amutationin pages 1-2)

#### Protective factors and gene–environment interactions
No validated protective genetic variants, environmental protective factors, or gene–environment interactions specific to MPDU1-CDG were identified in the retrieved evidence. Given the Mendelian mechanism, environmental modifiers are plausible but currently undocumented for MPDU1-CDG in the sources available here.

### 3) Phenotypes (clinical spectrum; HPO suggestions; frequency where available)

#### Overview of clinical phenotype
Across reported MPDU1-CDG patients, commonly described features include neurodevelopmental impairment and seizures, hypotonia, dermatologic abnormalities (ichthyosis/scaling; variably present), ocular anomalies (including congenital glaucoma/buphthalmos), hepatic/biliary involvement (including massive biliary duct dilatation in some), cardiomyopathy, thrombocytopenia/coagulation abnormalities, and elevated creatine kinase. (tol2019amutationin pages 6-8, teneiji2017phenotypicandgenotypic pages 10-14)

A notable 2019 report explicitly highlights overlap with dystroglycanopathy. **Direct abstract quote:** “*Here, we report two MPDU1‐CDG patients without skin involvement, but with massive dilatation of the biliary duct system and dystroglycanopathy characteristics including hypotonia, elevated creatine kinase, dilated cardiomyopathy, buphthalmos, and congenital glaucoma.*” (van Tol et al., 2019; published Sep 2019; https://doi.org/10.1002/jmd2.12060) (tol2019amutationin pages 1-2)

#### Phenotype-by-phenotype with ontology suggestions
Below are representative phenotype categories; reported frequencies are limited because case counts are small.

1) **Neurodevelopmental delay / psychomotor retardation**
- Type: symptom/clinical sign
- Onset: typically infancy/early childhood in reported cases
- Suggested HPO: **HP:0001263** (Global developmental delay), **HP:0001249** (Intellectual disability)
- Evidence: psychomotor retardation/delay repeatedly noted in early and later case descriptions. (haeuptle2009congenitaldisordersof pages 9-10, kranz2001amutationin pages 1-2)

2) **Seizures / epilepsy; apnea with seizures**
- Type: symptom
- Suggested HPO: **HP:0001250** (Seizures), **HP:0002104** (Apnea)
- Course: can be severe; seizure-induced apnea contributed to death in at least one early case. (haeuptle2009congenitaldisordersof pages 9-10, kranz2001amutationin pages 1-2)

3) **Hypotonia and neuromuscular involvement**
- Type: clinical sign
- Suggested HPO: **HP:0001252** (Hypotonia)
- Evidence: hypotonia is common; dystroglycanopathy overlap suggests muscle involvement in some cases. (tol2019amutationin pages 1-2, tol2019amutationin pages 6-8)

4) **Skin involvement (ichthyosis/scaling/erythroderma/desquamation)**
- Type: physical manifestation
- Suggested HPO: **HP:0008064** (Ichthyosis), **HP:0000964** (Eczema) (if applicable), **HP:0000988** (Skin rash)
- Variability: may be absent in some MPDU1-CDG patients. (tol2019amutationin pages 1-2, teneiji2017phenotypicandgenotypic pages 10-14, kranz2001amutationin pages 1-2)

5) **Ocular disease (buphthalmos, congenital glaucoma, corneal clouding, visual impairment/amaurosis)**
- Type: physical manifestation
- Suggested HPO: **HP:0007721** (Congenital glaucoma), **HP:0000613** (Buphthalmos), **HP:0000518** (Visual impairment)
- Clinical importance: severe congenital glaucoma may require urgent intervention (trabeculectomy noted in compiled case summaries). (tol2019amutationin pages 6-8)

6) **Cardiac involvement (cardiomyopathy)**
- Type: clinical sign
- Suggested HPO: **HP:0001638** (Cardiomyopathy), **HP:0001644** (Dilated cardiomyopathy), **HP:0001639** (Hypertrophic cardiomyopathy)
- Evidence: cardiomyopathy present in multiple MPDU1-CDG cases; MPDU1 is also listed among CDG genes associated with cardiomyopathy in 2024 screening recommendations. (tol2019amutationin pages 5-6, tol2019amutationin pages 6-8, zemet2024cardiomyopathyanuncommon pages 3-5)

7) **Hepatic/biliary involvement**
- Type: clinical sign / imaging abnormality
- Suggested HPO: **HP:0001392** (Hepatomegaly) (if present), **HP:0003270** (Abnormality of the biliary tract), **HP:0002240** (Hepatic dysfunction)
- Evidence: hepatocellular/synthetic dysfunction noted in a cohort case; biliary duct dilatation emphasized in the 2019 siblings. (tol2019amutationin pages 1-2, teneiji2017phenotypicandgenotypic pages 10-14)

8) **Hematologic/coagulation abnormalities**
- Type: laboratory abnormality
- Suggested HPO: **HP:0001873** (Thrombocytopenia), **HP:0001928** (Coagulopathy)
- Evidence: thrombocytopenia and low antithrombin III reported. (tol2019amutationin pages 5-6, tol2019amutationin pages 6-8)

#### Quality-of-life impact
No MPDU1-CDG–specific quality-of-life instruments (e.g., EQ-5D/SF-36) were found in the retrieved evidence. However, severe neurodevelopmental impairment, feeding dependence, seizures, visual disability, and cardiomyopathy imply substantial functional limitation. (tol2019amutationin pages 5-6, kranz2001amutationin pages 1-2)

### 4) Genetic and molecular information

#### Causal gene
- **Gene:** MPDU1 (mannose-P-dolichol utilization defect 1) (haeuptle2009congenitaldisordersof pages 9-10)
- **Protein features (as summarized in reviewed evidence):** ER membrane protein; reviews describe multiple transmembrane domains and ER localization. (haeuptle2009congenitaldisordersof pages 9-10)

#### Pathogenic variants (examples explicitly captured in the retrieved evidence)
- **c.218G>A (p.G73E)** (recurrent; associated with severe early-lethal disease in multiple reported cases) (tol2019amutationin pages 5-6, tol2019amutationin pages 6-8, schenk2003mpdu1mutationsunderlie pages 5-6)
- **221T>C (p.L74S)** (homozygous in the initial 2001 JCI patient; parental heterozygosity shown) (kranz2001amutationin pages 5-7, kranz2001amutationin pages 1-2)
- **c.356T>C (p.L119P)** (homozygous in one of the 2003 JCI patients) (schenk2003mpdu1mutationsunderlie pages 5-6)
- **2T>C (p.M1T)** and **c.511delC (frameshift)** (compound heterozygosity in one 2003 JCI patient) (schenk2003mpdu1mutationsunderlie pages 5-6)
- Additional missense variants reported in an Arab molecularly characterized summary: **p.Gly104Ser** and **p.Gln126Pro** (bastaki2018single‐centerexperienceof pages 8-10)

**Variant types observed:** primarily missense; at least one frameshift (c.511delC) and start-loss (p.M1T) are reported. (schenk2003mpdu1mutationsunderlie pages 5-6)

**Allele frequencies in population databases:** not available in the retrieved evidence; therefore not asserted.

#### Functional consequences
Collectively, patient-cell studies indicate the molecular defect leads to impaired use of Dol-P-Man and Dol-P-Glc, causing truncated LLO assembly and downstream protein hypoglycosylation; a 2003 mechanistic proposal is that MPDU1 acts as a dolichol-sugar “chaperone” supporting lateral distribution of dolichol-linked donors in the ER membrane. (schenk2003mpdu1mutationsunderlie pages 6-8, kranz2001amutationin pages 1-2)

#### Modifier genes
No MPDU1-CDG–specific modifier genes were identified in the retrieved evidence. One broader glycosylation modifier discussion exists in other contexts (e.g., ALG6 F304S modifying DHDDS-related disease), but this is not specific to MPDU1-CDG pathogenesis. (hamzan2023epidemiologyandprevalence pages 5-7)

### 5) Environmental information
No environmental toxins, lifestyle exposures, or infectious triggers are established contributors to MPDU1-CDG in the retrieved evidence (consistent with a primary Mendelian etiology).

### 6) Mechanism / pathophysiology

#### Causal chain (from gene to clinical phenotype)
1) **Biallelic MPDU1 variants → MPDU1 loss/dysfunction** in the ER membrane (kranz2001amutationin pages 5-7, schenk2003mpdu1mutationsunderlie pages 5-6)
2) **Impaired utilization/bioavailability of Dol-P-Man and Dol-P-Glc** needed by ER mannosyl-/glucosyltransferases (schenk2003mpdu1mutationsunderlie pages 6-8, kranz2001amutationin pages 1-2)
3) **Characteristic LLO assembly defect** with accumulation of truncated dolichol-PP-linked intermediates (notably Man5GlcNAc2 and Man9GlcNAc2) and reduced/aberrant mature Glc3Man9GlcNAc2; incomplete oligosaccharides can be transferred to proteins (schenk2003mpdu1mutationsunderlie pages 6-8, schenk2003mpdu1mutationsunderlie pages 1-2, tol2019amutationin media 2abc4e54)
4) **Systemic glycoprotein hypoglycosylation**, detectable via serum transferrin isoform analysis (CDG-I pattern) (schenk2003mpdu1mutationsunderlie pages 5-6, tol2019amutationin media 2abc4e54)
5) **Multi-pathway downstream effects**, including reduced O-mannosylation of α-dystroglycan (explaining dystroglycanopathy overlap) and impaired GPI-anchor maturation (reduced surface CD59) (tol2019amutationin pages 6-8, schenk2003mpdu1mutationsunderlie pages 6-8)
6) **Organ dysfunction** (neurodevelopmental delay/seizures, ocular disease, skin barrier defects/ichthyosis in many, cardiac and hepatobiliary manifestations) (tol2019amutationin pages 6-8, teneiji2017phenotypicandgenotypic pages 10-14)

#### Molecular pathways/processes and ontology suggestions
- **N-linked glycosylation (ER LLO assembly and transfer)**
  - Suggested GO Biological Process: **GO:0006487** (protein N-linked glycosylation)
  - Suggested GO Cellular Component: **GO:0005783** (endoplasmic reticulum)
  - Evidence: truncated LLO intermediates and hypoglycosylated serum transferrin; rescue by wild-type MPDU1. (schenk2003mpdu1mutationsunderlie pages 6-8, schenk2003mpdu1mutationsunderlie pages 1-2)

- **Dolichol-linked monosaccharide utilization**
  - Suggested GO BP (closest plausible): **GO:0019673** (dolichol-linked oligosaccharide biosynthetic process) / **GO:0019358** (dolichol biosynthetic process) (note: MPDU1 affects utilization rather than synthesis)
  - Evidence: Dol-P-Man/Dol-P-Glc present but not efficiently used; proposed lateral distribution mechanism. (schenk2003mpdu1mutationsunderlie pages 6-8)

- **O-mannosylation of α-dystroglycan (dystroglycanopathy overlap)**
  - Suggested GO BP: **GO:0035269** (protein O-linked mannosylation)
  - Evidence: reduced IIH6/laminin overlay binding indicating reduced functional glycosylation of α-dystroglycan. (tol2019amutationin pages 6-8)

- **GPI-anchor biosynthesis (secondary)**
  - Suggested GO BP: **GO:0006506** (GPI anchor biosynthetic process)
  - Evidence: reduced cell-surface GPI-anchored CD59 in patient cells. (schenk2003mpdu1mutationsunderlie pages 6-8)

#### Cell types (CL suggestions)
Direct cell-type-specific pathology is not well established in the retrieved evidence. However, based on organ involvement:
- Suggested CL: **CL:0000540** (neuron), **CL:0000746** (cardiomyocyte), **CL:0000548** (hepatocyte), **CL:0000333** (fibroblast) (the main experimental patient cell type used). (tol2019amutationin pages 5-6, schenk2003mpdu1mutationsunderlie pages 6-8)

### 7) Anatomical structures affected (UBERON suggestions)
Evidence supports multisystem involvement:
- **Nervous system:** UBERON:0001016 (nervous system) (seizures, neurodevelopmental delay) (kranz2001amutationin pages 1-2)
- **Eye:** UBERON:0000970 (eye) (congenital glaucoma, buphthalmos, visual impairment) (tol2019amutationin pages 6-8)
- **Skin:** UBERON:0002097 (skin of body) (ichthyosis/scaling) (teneiji2017phenotypicandgenotypic pages 10-14, kranz2001amutationin pages 1-2)
- **Heart:** UBERON:0000948 (heart) (cardiomyopathy) (tol2019amutationin pages 5-6)
- **Liver/biliary system:** UBERON:0002107 (liver); UBERON:0000059 (bile duct) (liver dysfunction; biliary duct dilatation) (tol2019amutationin pages 1-2, teneiji2017phenotypicandgenotypic pages 10-14)

Subcellular localization emphasized in mechanism:
- **Endoplasmic reticulum membrane** (GO CC: ER membrane; MPDU1 is an ER membrane protein). (haeuptle2009congenitaldisordersof pages 9-10, kranz2001amutationin pages 1-2)

### 8) Temporal development
- **Typical onset:** congenital/infantile presentation is most consistent with reported cases (severe multisystem disease in infancy; early deaths in severe genotypes). (tol2019amutationin pages 5-6, tol2019amutationin pages 6-8)
- **Progression/course:** variable; p.G73E has been repeatedly associated with very severe early-lethal disease, while other alleles show mild-to-moderate disease in earlier series. (tol2019amutationin pages 6-8, haeuptle2009congenitaldisordersof pages 9-10)

### 9) Inheritance and population

#### Inheritance
Autosomal recessive inheritance is supported by segregation in families and by homozygous/compound heterozygous genotypes in affected individuals. (tol2019amutationin pages 5-6, kranz2001amutationin pages 5-7, schenk2003mpdu1mutationsunderlie pages 5-6)

#### Epidemiology
No MPDU1-specific population prevalence/incidence estimate was identified in the retrieved evidence (typical for ultra-rare CDGs). For contextual, country-level CDG screening prevalence:
- A 2018–2022 Malaysian national reference-lab dataset identified **2 confirmed CDG diagnoses among 548 suspected cases**, yielding a calculated **birth prevalence of 0.22 per 100,000 live births** for CDG overall (not MPDU1-specific), and 0.85 per 100,000 for combined abnormal transferrin patterns. (Hamzan 2023; published Apr 2023; https://doi.org/10.37231/ajmb.2023.7.1.601) (hamzan2023epidemiologyandprevalence pages 1-3, hamzan2023epidemiologyandprevalence pages 3-5)
- Direct abstract quote: “*Overall, the prevalence of CDG in Malaysia was low and may be underestimated yet consistent with other reported in other countries.*” (hamzan2023epidemiologyandprevalence pages 1-3)

#### Population/variant observations
- Recurrent **p.G73E (c.218G>A)** appears in multiple unrelated MPDU1-CDG patients and is repeatedly associated with severe early-lethal disease, suggesting either a recurrent mutational hotspot or possible population recurrence; detailed founder analysis was not available in retrieved evidence. (tol2019amutationin pages 6-8, teneiji2017phenotypicandgenotypic pages 33-37)
- Consanguinity is reported in at least one affected family with p.G73E. (tol2019amutationin pages 1-2)

### 10) Diagnostics

#### Clinical suspicion
Patients may present with a CDG-like multisystem phenotype (neurodevelopmental delay, seizures, hypotonia, failure to thrive, skin/eye disease, hepatic/biliary abnormalities) and/or dystroglycanopathy features (myopathy, elevated CK, cardiomyopathy), prompting biochemical and genetic testing. (tol2019amutationin pages 1-2, tol2019amutationin pages 6-8)

#### Biochemical testing (real-world implementation)
1) **Serum transferrin isoform analysis**
- Methods used: transferrin isoelectric focusing (TIEF/IEF), sometimes quantified by HPLC-based approaches; CDG-I pattern reported in MPDU1-CDG including increased disialotransferrin and reduced tetrasialotransferrin. (tol2019amutationin pages 5-6, teneiji2017phenotypicandgenotypic pages 10-14, teneiji2017phenotypicandgenotypic pages 6-10)
- Figure-based evidence: TIEF pattern is shown in van Tol et al. 2019 (Figure 1D). (tol2019amutationin media 2abc4e54)

2) **Lipid-linked oligosaccharide (LLO) profiling in patient fibroblasts**
- Methods: HPLC analysis of LLOs; thin-layer chromatography (TLC) for hydrophobic extracts including Dol-P-Man/Dol-P-Glc-related measures. (tol2019amutationin pages 5-6, tol2019amutationin pages 1-2)
- Figure-based evidence: LLO HPLC profile is shown in van Tol et al. 2019 (Figure 2A). (tol2019amutationin media 2abc4e54)

3) **Functional glycosylation of α-dystroglycan**
- Methods: IIH6 immunolabeling and laminin overlay assays in fibroblasts to show reduced O-mannosylation/functional glycosylation of α-dystroglycan. (tol2019amutationin pages 6-8)

#### Genetic testing
- Approaches in published cohorts/cases include single-gene testing, targeted next-generation sequencing panels for CDG genes, and whole-exome sequencing (WES) with segregation analysis. (tol2019amutationin pages 5-6, teneiji2017phenotypicandgenotypic pages 6-10)

#### Differential diagnosis
MPDU1-CDG can overlap clinically and biochemically with other **CDG type I** conditions and with **dystroglycanopathies** due to DPM synthesis/utilization defects (e.g., DOLK-, DPM1/2/3-related disorders). (tol2019amutationin pages 1-2, tol2019amutationin pages 6-8)

#### Screening
There is no evidence in retrieved sources that MPDU1-CDG is included in routine newborn screening panels. Population screening for CDG more broadly often uses transferrin isoform analysis (IEF/CZE/HPLC), but sensitivity varies by subtype; genetic testing is increasingly used for definitive diagnosis. (teneiji2017phenotypicandgenotypic pages 6-10, hamzan2023epidemiologyandprevalence pages 3-5)

### 11) Outcome / prognosis
Prognosis is **highly variable**. Severe disease with early infant death has been repeatedly described in p.G73E homozygous patients (deaths reported within the first year of life in some cases). (tol2019amutationin pages 5-6, tol2019amutationin pages 6-8)

A review of dolichol-linked oligosaccharide disorders notes variable severity and reports one patient dying in early childhood following seizure-induced apnea, while others had milder disease. (haeuptle2009congenitaldisordersof pages 9-10)

### 12) Treatment and management

#### Disease-modifying therapy
No established disease-specific or pathway-targeted therapy for MPDU1-CDG was identified in the retrieved evidence; management is therefore primarily supportive. (tol2019amutationin pages 6-8)

#### Supportive and multidisciplinary care (current real-world implementations)
Care is typically individualized and may include:
- **Neurology:** antiseizure management; monitoring for apnea/respiratory complications (MAXO suggestions: antiseizure therapy; respiratory support). (tol2019amutationin pages 5-6, kranz2001amutationin pages 1-2)
- **Nutrition/feeding:** feeding support including tube feeding when required (MAXO: enteral nutrition). (tol2019amutationin pages 5-6)
- **Ophthalmology:** early evaluation and management of congenital glaucoma (e.g., surgical intervention reported in compiled cases) (MAXO: glaucoma surgery; vision rehabilitation). (tol2019amutationin pages 6-8)
- **Cardiology:** surveillance and management of cardiomyopathy/heart failure where present (MAXO: cardiac monitoring; heart failure pharmacotherapy). (tol2019amutationin pages 5-6, zemet2024cardiomyopathyanuncommon pages 3-5)
- **Hepatology/Gastroenterology:** evaluation of hepatocellular dysfunction and biliary tract abnormalities. (tol2019amutationin pages 1-2, teneiji2017phenotypicandgenotypic pages 10-14)
- **Hematology:** monitoring thrombocytopenia and coagulation factors such as antithrombin III. (tol2019amutationin pages 5-6)

#### 2024 expert recommendations relevant to MPDU1-CDG (cardiac screening)
A 2024 expert recommendations paper on cardiomyopathy in CDG lists MPDU1 among CDG genes associated with cardiomyopathy and proposes **baseline and longitudinal cardiac surveillance** for CDG patients: echocardiogram and ECG at diagnosis, annual follow-up for the first 5 years, then every 2–3 years until adulthood if stable, and approximately every 5 years thereafter. (Zemet et al., Aug 2024; https://doi.org/10.1016/j.ymgme.2024.108513) (zemet2024cardiomyopathyanuncommon pages 3-5, zemet2024cardiomyopathyanuncommon pages 1-3)

### 13) Prevention
Primary prevention of MPDU1-CDG is not currently feasible outside genetic strategies. Secondary/tertiary prevention focuses on early diagnosis and proactive management of organ complications.

- **Genetic counseling (primary prevention at family level):** because inheritance is autosomal recessive, carrier testing in parents and at-risk relatives, reproductive counseling, and options such as prenatal diagnosis or preimplantation genetic testing are conceptually applicable (not directly evidenced in retrieved texts, but consistent with AR inheritance demonstrated in primary reports). (kranz2001amutationin pages 5-7)

### 14) Other species / natural disease
No naturally occurring animal disease analogs were identified in the retrieved evidence.

### 15) Model organisms and experimental systems
Although whole-animal disease models were not retrieved here, multiple experimental systems directly support MPDU1 biology:
- **Hamster CHO cell (Lec35) complementation system:** MPDU1 is orthologous to hamster Lec35; patient alleles show impaired correction of the Lec35 phenotype compared with wild-type MPDU1, supporting functional impact of human variants. (kranz2001amutationin pages 5-7, kranz2001amutationin pages 1-2)
- **Patient fibroblast rescue experiments:** expression of normal Lec35/MPDU1 cDNA restored normal LLO biosynthesis in patient fibroblasts, providing strong functional causality evidence. (schenk2003mpdu1mutationsunderlie pages 6-8)

### Recent developments and “latest research” emphasis (2023–2024)
Because MPDU1-CDG is extremely rare, MPDU1-specific 2023–2024 primary case reports were not retrievable within the available tool outputs in this run. However, important 2023–2024 developments relevant to MPDU1-CDG clinical practice include:
1) **2024 cardiomyopathy surveillance recommendations in CDG** (gene list includes MPDU1; provides longitudinal screening schedule). (zemet2024cardiomyopathyanuncommon pages 3-5, zemet2024cardiomyopathyanuncommon pages 1-3)
2) **ClinicalTrials.gov natural history infrastructure (NCT04199000)** explicitly includes MPDU1 in the targeted CDG spectrum and collects standardized clinical severity measures and biospecimens for biomarker research. (Study posted 2019; recruiting; https://clinicaltrials.gov/study/NCT04199000) (NCT04199000 chunk 1)
3) **2023 national reference-lab epidemiology data** illustrating how transferrin-based screening is implemented at scale and how prevalence estimates may be derived (though not MPDU1-specific). (hamzan2023epidemiologyandprevalence pages 1-3, hamzan2023epidemiologyandprevalence pages 3-5)

### Key statistics and data points (from retrieved evidence)
- In a CDG natural history cohort (FCDGC) of **305 molecularly confirmed CDG patients** (as of June 2023), **17 (5.6%)** had cardiomyopathy; MPDU1-CDG was not among the cardiomyopathy genotypes identified in that cohort subset, but MPDU1 is included among CDG genes reported with cardiomyopathy in the literature. (zemet2024cardiomyopathyanuncommon pages 5-6, zemet2024cardiomyopathyanuncommon pages 3-5)
- Malaysian screening-based birth prevalence estimates for CDG overall: **0.22 per 100,000 live births** (CDG overall) and **0.85 per 100,000 live births** (abnormal transferrin patterns), based on 2018–2022 reference-lab data. (hamzan2023epidemiologyandprevalence pages 1-3, hamzan2023epidemiologyandprevalence pages 3-5)

### Curated quick-reference table (variants/phenotypes/diagnostics/management)
| Category | Summary |
|---|---|
| Disease / names | **MPDU1-congenital disorder of glycosylation**; historical names: **CDG-If**, **MPDU1-CDG**, **mannose-P-dolichol utilization defect 1**; MONDO: **MONDO:0012211** (Open Targets disease association) (OpenTargets Search: MPDU1-congenital disorder of glycosylation,congenital disorder of glycosylation-MPDU1, haeuptle2009congenitaldisordersof pages 9-10, schenk2003mpdu1mutationsunderlie pages 1-2) |
| Evidence base | Ultra-rare, disease-level knowledge is derived primarily from individual case reports/series and small CDG cohorts rather than large epidemiologic datasets (tol2019amutationin pages 6-8, teneiji2017phenotypicandgenotypic pages 10-14, hamzan2023epidemiologyandprevalence pages 1-3) |
| Inheritance | **Autosomal recessive**; homozygous and compound-heterozygous MPDU1 variants reported, with parental heterozygosity/segregation shown in key families (tol2019amutationin pages 5-6, kranz2001amutationin pages 5-7, schenk2003mpdu1mutationsunderlie pages 5-6) |
| Causal gene | **MPDU1** encodes an ER membrane protein required for efficient utilization/lateral distribution of **dolichol-P-mannose (Dol-P-Man)** and **dolichol-P-glucose (Dol-P-Glc)** during glycosylation; orthologous to hamster **Lec35** (haeuptle2009congenitaldisordersof pages 9-10, schenk2003mpdu1mutationsunderlie pages 6-8, kranz2001amutationin pages 1-2) |
| Key reported variants | **c.218G>A (p.G73E)** recurrent severe variant; **221T>C (p.L74S)**; **c.356T>C (p.L119P)**; **2T>C (p.M1T)**; **c.511delC** frameshift; additional reported missense variants **p.Gly104Ser** and **p.Gln126Pro** in Arab summary literature (tol2019amutationin pages 5-6, teneiji2017phenotypicandgenotypic pages 33-37, kranz2001amutationin pages 5-7, schenk2003mpdu1mutationsunderlie pages 5-6, bastaki2018single‐centerexperienceof pages 8-10) |
| Core neurologic features | Psychomotor/neurodevelopmental delay or retardation, severe hypotonia, seizures/epilepsy, failure to thrive, apnea/respiratory compromise in severe cases (tol2019amutationin pages 6-8, haeuptle2009congenitaldisordersof pages 9-10, kranz2001amutationin pages 1-2) |
| Skin features | Ichthyosis, dry skin with scaling/erythroderma, patchy desquamation; skin involvement is variable and may be absent in some newer cases (tol2019amutationin pages 1-2, tol2019amutationin pages 6-8, teneiji2017phenotypicandgenotypic pages 10-14, schenk2003mpdu1mutationsunderlie pages 5-6, kranz2001amutationin pages 1-2) |
| Eye features | Visual impairment/amaurosis, enlarged cloudy corneae, **buphthalmos**, **congenital glaucoma**, other eye defects; glaucoma may require urgent ophthalmologic intervention (tol2019amutationin pages 5-6, tol2019amutationin pages 6-8, haeuptle2009congenitaldisordersof pages 9-10) |
| Cardiac features | Cardiomyopathy reported, including **dilated cardiomyopathy** and **hypertrophic cardiomyopathy**; MPDU1 is listed among CDG genes associated with cardiomyopathy in recent cardiac review/guidance (tol2019amutationin pages 5-6, tol2019amutationin pages 6-8, zemet2024cardiomyopathyanuncommon pages 3-5) |
| Hepatic / biliary features | Hepatocellular/synthetic liver dysfunction, increased liver echogenicity, and striking **biliary duct dilatation** in some cases (tol2019amutationin pages 1-2, teneiji2017phenotypicandgenotypic pages 10-14) |
| Hematologic / coagulation features | **Thrombocytopenia**, low **antithrombin III**, and coagulation abnormalities have been documented (tol2019amutationin pages 5-6, tol2019amutationin pages 6-8) |
| Additional organ involvement | Gastrointestinal problems, feeding dependence, small renal cysts, facial dysmorphism, elevated CK, pulmonary hypertension, VSD in some patients (tol2019amutationin pages 5-6, tol2019amutationin pages 6-8, teneiji2017phenotypicandgenotypic pages 10-14, haeuptle2009congenitaldisordersof pages 9-10) |
| Biochemical hallmark: transferrin | **CDG-I transferrin pattern** with hypoglycosylated serum transferrin; increased **asialo-/disialotransferrin** and reduced tetrasialotransferrin reported by TIEF/IEF and confirmed by ESI-MS in some patients (tol2019amutationin pages 5-6, teneiji2017phenotypicandgenotypic pages 10-14, schenk2003mpdu1mutationsunderlie pages 1-2, schenk2003mpdu1mutationsunderlie pages 5-6, tol2019amutationin media 2abc4e54) |
| Biochemical hallmark: LLO profile | Accumulation of truncated **lipid-linked oligosaccharides (LLOs)**, especially **Man5GlcNAc2** and **Man9GlcNAc2**; mature **Glc3Man9GlcNAc2** reduced/abnormal; incomplete oligosaccharides can be transferred to protein (tol2019amutationin pages 5-6, tol2019amutationin pages 6-8, haeuptle2009congenitaldisordersof pages 9-10, schenk2003mpdu1mutationsunderlie pages 6-8, schenk2003mpdu1mutationsunderlie pages 1-2, tol2019amutationin media 2abc4e54) |
| Functional defect | Impaired **utilization** rather than synthesis of **Dol-P-Man** and **Dol-P-Glc**; MPDU1 is proposed to act as a dolichol-sugar chaperone/lateral distributor in the ER rather than a simple flippase (haeuptle2009congenitaldisordersof pages 9-10, schenk2003mpdu1mutationsunderlie pages 6-8, kranz2001amutationin pages 5-7, kranz2001amutationin pages 1-2) |
| Other pathway effects | Reduced **O-mannosylation of α-dystroglycan** (dystroglycanopathy overlap) and reduced cell-surface **GPI-anchored CD59** have been shown in patient cells (tol2019amutationin pages 1-2, tol2019amutationin pages 6-8, schenk2003mpdu1mutationsunderlie pages 6-8) |
| Diagnostic modalities | Serum **TIEF/IEF** ± **HPLC/CZE** screening; **ESI-MS** transferrin analysis; fibroblast **LLO HPLC/TLC**; **WES** or targeted NGS; segregation analysis; functional complementation in fibroblasts/CHO cells; **IIH6 immunolabeling/laminin overlay** for α-dystroglycan (tol2019amutationin pages 5-6, tol2019amutationin pages 1-2, tol2019amutationin pages 6-8, teneiji2017phenotypicandgenotypic pages 33-37, kranz2001amutationin pages 5-7, tol2019amutationin media 2abc4e54, hamzan2023epidemiologyandprevalence pages 3-5) |
| Differential diagnostic context | Overlaps biochemically with other **CDG-I** defects and clinically with **dystroglycanopathies**, especially disorders affecting DPM synthesis/utilization (e.g., DOLK/DPM pathway disorders) (tol2019amutationin pages 1-2, tol2019amutationin pages 6-8) |
| Outcomes / prognosis | Prognosis is **variable but often severe**; recurrent **p.G73E** is associated with particularly severe disease and **early infant death** (reported deaths before ~11 months in some cases); one earlier patient died in early childhood following seizure-induced apnea (tol2019amutationin pages 5-6, tol2019amutationin pages 6-8, haeuptle2009congenitaldisordersof pages 9-10) |
| Management | No disease-modifying therapy established; current care is **supportive and multidisciplinary**: nutritional/feeding support, seizure management, ophthalmologic care, cardiology, hepatology, and coagulation monitoring as indicated (tol2019amutationin pages 5-6, tol2019amutationin pages 6-8) |
| Cardiac surveillance suggestion | Because MPDU1 is among CDG types linked to cardiomyopathy, recent CDG guidance recommends **baseline ECG + echocardiogram at diagnosis**, **annual cardiac follow-up for the first 5 years**, then **every 2–3 years until adulthood** if stable, and about **every 5 years thereafter**; ongoing cardiology care if cardiomyopathy is present (zemet2024cardiomyopathyanuncommon pages 3-5, zemet2024cardiomyopathyanuncommon pages 1-3) |
| Current research / implementation | MPDU1-CDG is included within the **Frontiers in CDG Consortium** natural history infrastructure and the observational study **NCT04199000**, which collects longitudinal clinical data and biospecimens across molecularly confirmed CDG subtypes (NCT04199000 chunk 1, zemet2024cardiomyopathyanuncommon pages 3-5, zemet2024cardiomyopathyanuncommon pages 1-3) |


*Table: This table condenses the main disease-defining, molecular, clinical, biochemical, diagnostic, prognostic, and management facts for MPDU1-congenital disorder of glycosylation. It is designed as a quick-reference artifact for knowledge-base curation and evidence tracing.*

### Figure/table evidence extracted from primary literature
- Transferrin IEF and LLO profiling figures and a multi-patient clinical feature table are available in the van Tol et al. 2019 report, supporting key biochemical hallmarks and clinical comparisons. (tol2019amutationin media 2abc4e54, tol2019amutationin media 23fb2f88, tol2019amutationin media 7782a19e, tol2019amutationin media 364fb774)

### References (URLs and publication dates where available)
- Kranz C, et al. *The Journal of Clinical Investigation* (Dec 2001). https://doi.org/10.1172/jci13635 (kranz2001amutationin pages 1-2, kranz2001amutationin pages 5-7)
- Schenk B, et al. *Journal of Clinical Investigation* (Mar 2003). https://doi.org/10.1172/jci200113419c (schenk2003mpdu1mutationsunderlie pages 1-2, schenk2003mpdu1mutationsunderlie pages 5-6, schenk2003mpdu1mutationsunderlie pages 6-8)
- van Tol W, et al. *JIMD Reports* (Sep 2019). https://doi.org/10.1002/jmd2.12060 (tol2019amutationin pages 1-2, tol2019amutationin pages 6-8)
- Hamzan NI. *Asian Journal of Medicine and Biomedicine* (Apr 2023). https://doi.org/10.37231/ajmb.2023.7.1.601 (hamzan2023epidemiologyandprevalence pages 1-3)
- Zemet R, et al. *Molecular Genetics and Metabolism* (Aug 2024). https://doi.org/10.1016/j.ymgme.2024.108513 (zemet2024cardiomyopathyanuncommon pages 3-5)
- ClinicalTrials.gov: NCT04199000 (posted 2019; recruiting as retrieved). https://clinicaltrials.gov/study/NCT04199000 (NCT04199000 chunk 1)



References

1. (tol2019amutationin pages 1-2): Walinka van Tol, Angel Ashikov, Eckhard Korsch, Nurulamin Abu Bakar, Michèl A. Willemsen, Christian Thiel, and Dirk J. Lefeber. A mutation in mannose‐phosphate‐dolichol utilization defect 1 reveals clinical symptoms of congenital disorders of glycosylation type i and dystroglycanopathy. JIMD Reports, 50:31-39, Sep 2019. URL: https://doi.org/10.1002/jmd2.12060, doi:10.1002/jmd2.12060. This article has 17 citations and is from a peer-reviewed journal.

2. (tol2019amutationin pages 6-8): Walinka van Tol, Angel Ashikov, Eckhard Korsch, Nurulamin Abu Bakar, Michèl A. Willemsen, Christian Thiel, and Dirk J. Lefeber. A mutation in mannose‐phosphate‐dolichol utilization defect 1 reveals clinical symptoms of congenital disorders of glycosylation type i and dystroglycanopathy. JIMD Reports, 50:31-39, Sep 2019. URL: https://doi.org/10.1002/jmd2.12060, doi:10.1002/jmd2.12060. This article has 17 citations and is from a peer-reviewed journal.

3. (schenk2003mpdu1mutationsunderlie pages 6-8): B. Schenk, T. Imbach, C. Frank, C. Grubenmann, G. Raymond, H. Hurvitz, I. Korn‐Lubetzki, S. Revel-Vik, A. Raas-Rotschild, A. Luder, J. Jaeken, E. Berger, G. Matthijs, T. Hennet, and M. Aebi. Mpdu1 mutations underlie a novel human congenital disorder of glycosylation, designated type if. Journal of Clinical Investigation, 111:925-a-925, Mar 2003. URL: https://doi.org/10.1172/jci200113419c, doi:10.1172/jci200113419c. This article has 186 citations and is from a highest quality peer-reviewed journal.

4. (OpenTargets Search: MPDU1-congenital disorder of glycosylation,congenital disorder of glycosylation-MPDU1): Open Targets Query (MPDU1-congenital disorder of glycosylation,congenital disorder of glycosylation-MPDU1, 23 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

5. (schenk2003mpdu1mutationsunderlie pages 1-2): B. Schenk, T. Imbach, C. Frank, C. Grubenmann, G. Raymond, H. Hurvitz, I. Korn‐Lubetzki, S. Revel-Vik, A. Raas-Rotschild, A. Luder, J. Jaeken, E. Berger, G. Matthijs, T. Hennet, and M. Aebi. Mpdu1 mutations underlie a novel human congenital disorder of glycosylation, designated type if. Journal of Clinical Investigation, 111:925-a-925, Mar 2003. URL: https://doi.org/10.1172/jci200113419c, doi:10.1172/jci200113419c. This article has 186 citations and is from a highest quality peer-reviewed journal.

6. (haeuptle2009congenitaldisordersof pages 9-10): Micha A. Haeuptle and Thierry Hennet. Congenital disorders of glycosylation: an update on defects affecting the biosynthesis of dolichol‐linked oligosaccharides. Human Mutation, 30:1628-1641, Dec 2009. URL: https://doi.org/10.1002/humu.21126, doi:10.1002/humu.21126. This article has 233 citations and is from a domain leading peer-reviewed journal.

7. (kranz2001amutationin pages 1-2): Christian Kranz, Jonas Denecke, Mark A. Lehrman, Sutapa Ray, Petra Kienz, Gunilla Kreissel, Dijana Sagi, Jasna Peter-Katalinic, Hudson H. Freeze, Thomas Schmid, Sabine Jackowski-Dohrmann, Erik Harms, and Thorsten Marquardt. A mutation in the human mpdu1 gene causes congenital disorder of glycosylation type if (cdg-if). The Journal of clinical investigation, 108 11:1613-9, Dec 2001. URL: https://doi.org/10.1172/jci13635, doi:10.1172/jci13635. This article has 160 citations.

8. (teneiji2017phenotypicandgenotypic pages 10-14): Amal Al Teneiji, Theodora U.J. Bruun, Sarah Sidky, Dawn Cordeiro, Ronald D Cohn, Roberto Mendoza-Londono, Mahendranath Moharir, Julian Raiman, Komudi Siriwardena, Lianna Kyriakopoulou, and Saadet Mercimek-Mahmutoglu. Phenotypic and genotypic spectrum of congenital disorders of glycosylation type i and type ii. Molecular genetics and metabolism, 120 3:235-242, Mar 2017. URL: https://doi.org/10.1016/j.ymgme.2016.12.014, doi:10.1016/j.ymgme.2016.12.014. This article has 80 citations and is from a peer-reviewed journal.

9. (tol2019amutationin pages 5-6): Walinka van Tol, Angel Ashikov, Eckhard Korsch, Nurulamin Abu Bakar, Michèl A. Willemsen, Christian Thiel, and Dirk J. Lefeber. A mutation in mannose‐phosphate‐dolichol utilization defect 1 reveals clinical symptoms of congenital disorders of glycosylation type i and dystroglycanopathy. JIMD Reports, 50:31-39, Sep 2019. URL: https://doi.org/10.1002/jmd2.12060, doi:10.1002/jmd2.12060. This article has 17 citations and is from a peer-reviewed journal.

10. (schenk2003mpdu1mutationsunderlie pages 5-6): B. Schenk, T. Imbach, C. Frank, C. Grubenmann, G. Raymond, H. Hurvitz, I. Korn‐Lubetzki, S. Revel-Vik, A. Raas-Rotschild, A. Luder, J. Jaeken, E. Berger, G. Matthijs, T. Hennet, and M. Aebi. Mpdu1 mutations underlie a novel human congenital disorder of glycosylation, designated type if. Journal of Clinical Investigation, 111:925-a-925, Mar 2003. URL: https://doi.org/10.1172/jci200113419c, doi:10.1172/jci200113419c. This article has 186 citations and is from a highest quality peer-reviewed journal.

11. (kranz2001amutationin pages 5-7): Christian Kranz, Jonas Denecke, Mark A. Lehrman, Sutapa Ray, Petra Kienz, Gunilla Kreissel, Dijana Sagi, Jasna Peter-Katalinic, Hudson H. Freeze, Thomas Schmid, Sabine Jackowski-Dohrmann, Erik Harms, and Thorsten Marquardt. A mutation in the human mpdu1 gene causes congenital disorder of glycosylation type if (cdg-if). The Journal of clinical investigation, 108 11:1613-9, Dec 2001. URL: https://doi.org/10.1172/jci13635, doi:10.1172/jci13635. This article has 160 citations.

12. (zemet2024cardiomyopathyanuncommon pages 3-5): Roni Zemet, Kyle D. Hope, Andrew C. Edmondson, Rameen Shah, Maria Patino, Abigail M. Yesso, Justin H. Berger, Kyriakie Sarafoglou, Austin Larson, Christina Lam, Eva Morava, and Fernando Scaglia. Cardiomyopathy, an uncommon phenotype of congenital disorders of glycosylation: recommendations for baseline screening and follow-up evaluation. Molecular Genetics and Metabolism, 142:108513, Aug 2024. URL: https://doi.org/10.1016/j.ymgme.2024.108513, doi:10.1016/j.ymgme.2024.108513. This article has 14 citations and is from a peer-reviewed journal.

13. (bastaki2018single‐centerexperienceof pages 8-10): Fatma Bastaki, Sami Bizzari, Sana Hamici, Pratibha Nair, Madiha Mohamed, Fatima Saif, Ethar Mustafa Malik, Mahmoud Taleb Al‐Ali, and Abdul Rezzak Hamzeh. Single‐center experience of n‐linked congenital disorders of glycosylation with a summary of molecularly characterized cases in arabs. Annals of Human Genetics, 82:35-47, Jan 2018. URL: https://doi.org/10.1111/ahg.12220, doi:10.1111/ahg.12220. This article has 33 citations and is from a peer-reviewed journal.

14. (hamzan2023epidemiologyandprevalence pages 5-7): Nurul Izzati Hamzan. Epidemiology and prevalence of patients with congenital disorders of glycosylation in malaysia. Asian Journal of Medicine and Biomedicine, 7:56-64, Apr 2023. URL: https://doi.org/10.37231/ajmb.2023.7.1.601, doi:10.37231/ajmb.2023.7.1.601. This article has 1 citations.

15. (tol2019amutationin media 2abc4e54): Walinka van Tol, Angel Ashikov, Eckhard Korsch, Nurulamin Abu Bakar, Michèl A. Willemsen, Christian Thiel, and Dirk J. Lefeber. A mutation in mannose‐phosphate‐dolichol utilization defect 1 reveals clinical symptoms of congenital disorders of glycosylation type i and dystroglycanopathy. JIMD Reports, 50:31-39, Sep 2019. URL: https://doi.org/10.1002/jmd2.12060, doi:10.1002/jmd2.12060. This article has 17 citations and is from a peer-reviewed journal.

16. (hamzan2023epidemiologyandprevalence pages 1-3): Nurul Izzati Hamzan. Epidemiology and prevalence of patients with congenital disorders of glycosylation in malaysia. Asian Journal of Medicine and Biomedicine, 7:56-64, Apr 2023. URL: https://doi.org/10.37231/ajmb.2023.7.1.601, doi:10.37231/ajmb.2023.7.1.601. This article has 1 citations.

17. (hamzan2023epidemiologyandprevalence pages 3-5): Nurul Izzati Hamzan. Epidemiology and prevalence of patients with congenital disorders of glycosylation in malaysia. Asian Journal of Medicine and Biomedicine, 7:56-64, Apr 2023. URL: https://doi.org/10.37231/ajmb.2023.7.1.601, doi:10.37231/ajmb.2023.7.1.601. This article has 1 citations.

18. (teneiji2017phenotypicandgenotypic pages 33-37): Amal Al Teneiji, Theodora U.J. Bruun, Sarah Sidky, Dawn Cordeiro, Ronald D Cohn, Roberto Mendoza-Londono, Mahendranath Moharir, Julian Raiman, Komudi Siriwardena, Lianna Kyriakopoulou, and Saadet Mercimek-Mahmutoglu. Phenotypic and genotypic spectrum of congenital disorders of glycosylation type i and type ii. Molecular genetics and metabolism, 120 3:235-242, Mar 2017. URL: https://doi.org/10.1016/j.ymgme.2016.12.014, doi:10.1016/j.ymgme.2016.12.014. This article has 80 citations and is from a peer-reviewed journal.

19. (teneiji2017phenotypicandgenotypic pages 6-10): Amal Al Teneiji, Theodora U.J. Bruun, Sarah Sidky, Dawn Cordeiro, Ronald D Cohn, Roberto Mendoza-Londono, Mahendranath Moharir, Julian Raiman, Komudi Siriwardena, Lianna Kyriakopoulou, and Saadet Mercimek-Mahmutoglu. Phenotypic and genotypic spectrum of congenital disorders of glycosylation type i and type ii. Molecular genetics and metabolism, 120 3:235-242, Mar 2017. URL: https://doi.org/10.1016/j.ymgme.2016.12.014, doi:10.1016/j.ymgme.2016.12.014. This article has 80 citations and is from a peer-reviewed journal.

20. (zemet2024cardiomyopathyanuncommon pages 1-3): Roni Zemet, Kyle D. Hope, Andrew C. Edmondson, Rameen Shah, Maria Patino, Abigail M. Yesso, Justin H. Berger, Kyriakie Sarafoglou, Austin Larson, Christina Lam, Eva Morava, and Fernando Scaglia. Cardiomyopathy, an uncommon phenotype of congenital disorders of glycosylation: recommendations for baseline screening and follow-up evaluation. Molecular Genetics and Metabolism, 142:108513, Aug 2024. URL: https://doi.org/10.1016/j.ymgme.2024.108513, doi:10.1016/j.ymgme.2024.108513. This article has 14 citations and is from a peer-reviewed journal.

21. (NCT04199000 chunk 1): Eva Morava-Kozicz. Clinical and Basic Investigations Into Congenital Disorders of Glycosylation. Icahn School of Medicine at Mount Sinai. 2019. ClinicalTrials.gov Identifier: NCT04199000

22. (zemet2024cardiomyopathyanuncommon pages 5-6): Roni Zemet, Kyle D. Hope, Andrew C. Edmondson, Rameen Shah, Maria Patino, Abigail M. Yesso, Justin H. Berger, Kyriakie Sarafoglou, Austin Larson, Christina Lam, Eva Morava, and Fernando Scaglia. Cardiomyopathy, an uncommon phenotype of congenital disorders of glycosylation: recommendations for baseline screening and follow-up evaluation. Molecular Genetics and Metabolism, 142:108513, Aug 2024. URL: https://doi.org/10.1016/j.ymgme.2024.108513, doi:10.1016/j.ymgme.2024.108513. This article has 14 citations and is from a peer-reviewed journal.

23. (tol2019amutationin media 23fb2f88): Walinka van Tol, Angel Ashikov, Eckhard Korsch, Nurulamin Abu Bakar, Michèl A. Willemsen, Christian Thiel, and Dirk J. Lefeber. A mutation in mannose‐phosphate‐dolichol utilization defect 1 reveals clinical symptoms of congenital disorders of glycosylation type i and dystroglycanopathy. JIMD Reports, 50:31-39, Sep 2019. URL: https://doi.org/10.1002/jmd2.12060, doi:10.1002/jmd2.12060. This article has 17 citations and is from a peer-reviewed journal.

24. (tol2019amutationin media 7782a19e): Walinka van Tol, Angel Ashikov, Eckhard Korsch, Nurulamin Abu Bakar, Michèl A. Willemsen, Christian Thiel, and Dirk J. Lefeber. A mutation in mannose‐phosphate‐dolichol utilization defect 1 reveals clinical symptoms of congenital disorders of glycosylation type i and dystroglycanopathy. JIMD Reports, 50:31-39, Sep 2019. URL: https://doi.org/10.1002/jmd2.12060, doi:10.1002/jmd2.12060. This article has 17 citations and is from a peer-reviewed journal.

25. (tol2019amutationin media 364fb774): Walinka van Tol, Angel Ashikov, Eckhard Korsch, Nurulamin Abu Bakar, Michèl A. Willemsen, Christian Thiel, and Dirk J. Lefeber. A mutation in mannose‐phosphate‐dolichol utilization defect 1 reveals clinical symptoms of congenital disorders of glycosylation type i and dystroglycanopathy. JIMD Reports, 50:31-39, Sep 2019. URL: https://doi.org/10.1002/jmd2.12060, doi:10.1002/jmd2.12060. This article has 17 citations and is from a peer-reviewed journal.