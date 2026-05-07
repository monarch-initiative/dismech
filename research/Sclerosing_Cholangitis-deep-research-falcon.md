---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-07T11:58:13.297730'
end_time: '2026-05-07T12:26:07.957198'
duration_seconds: 1674.67
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Sclerosing Cholangitis
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 53
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Sclerosing Cholangitis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Sclerosing Cholangitis** covering all of the
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
- **Disease Name:** Sclerosing Cholangitis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Sclerosing Cholangitis** covering all of the
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


# Comprehensive Disease Characteristics Report: Sclerosing Cholangitis (focus on Primary Sclerosing Cholangitis, PSC)

## Executive summary
Sclerosing cholangitis is a spectrum of chronic progressive cholestatic biliary diseases characterized by patchy bile-duct inflammation, fibrosis, and stricturing; it is classified as **primary** (PSC; no identifiable cause) or **secondary** (SSC; attributable to a specific insult such as ischemia, infection, toxins/drugs, or immune-mediated conditions including IgG4-related disease). (ludwig2023secondarysclerosingcholangitis pages 1-3, moller2023secondarysclerosingcholangitis pages 1-2)

PSC is strongly linked to inflammatory bowel disease (IBD) (commonly ulcerative colitis) and carries substantial risks of cirrhosis, need for liver transplantation, and hepatobiliary/colorectal malignancies. (crothers2024pastcurrentand pages 1-2, pitoni2025navigatingneoplasmrisk pages 1-2)

In 2023–2024, major advances include: (i) **new population-based epidemiology** showing increasing PSC-IBD prevalence with projections to 2027 in England; (ii) **microbiome + bile-acid multi-omic profiling** that quantifies functional changes in secondary bile acid metabolism in PSC-IBD; and (iii) expanding **clinical trial portfolios** emphasizing ALP-based endpoints, noninvasive fibrosis measures, and patient-reported outcomes (PROs). (crothers2024pastcurrentand pages 1-2, leibovitzh2024inflammatoryboweldisease pages 1-2, NCT03872921 chunk 1)

---

## 1. Disease information
### 1.1 Overview and definitions
* **Sclerosing cholangitis (SC)**: chronic cholestatic disease with stricturing, “beading,” and obliterative fibrosis affecting intrahepatic and/or extrahepatic bile ducts. (ludwig2023secondarysclerosingcholangitis pages 1-3, moller2023secondarysclerosingcholangitis pages 1-2)
* **Primary sclerosing cholangitis (PSC)**: SC in which **no underlying etiology** is identified; diagnosis combines a cholestatic lab pattern with characteristic cholangiographic findings on MRCP/ERCP in the absence of another cause. (ludwig2023secondarysclerosingcholangitis pages 1-3)
* **Secondary sclerosing cholangitis (SSC)**: SC with an **identifiable cause** (infectious, ischemic, toxic/drug-induced, immunologic—including IgG4-related disease—congenital, etc.). SSC can mimic PSC but often has worse prognosis; end-stage SSC leading to biliary cirrhosis is treatable only by liver transplantation. (ludwig2023secondarysclerosingcholangitis pages 3-4, ludwig2023secondarysclerosingcholangitis pages 1-3)
* **IgG4-related sclerosing cholangitis (IgG4-SC)**: immune-mediated biliary manifestation of IgG4-related disease; typically steroid responsive; often associated with autoimmune pancreatitis. (ludwig2023secondarysclerosingcholangitis pages 7-9, moller2023secondarysclerosingcholangitis pages 10-11)

### 1.2 Key identifiers (limited to retrieved evidence)
| Entity/scope | Common synonyms | MeSH ID/term | MONDO/EFO | Key distinguishing feature |
|---|---|---|---|---|
| Sclerosing cholangitis (umbrella entity) | SC; cholangitis, sclerosing | D015209 / **Cholangitis, Sclerosing** | **EFO_0004268** (sclerosing cholangitis) | Chronic cholestatic biliary disease spectrum with inflammation, fibrosis, stricturing, and beading of intrahepatic and/or extrahepatic bile ducts; includes primary and secondary forms. ICD codes: **not extracted from the provided sources**. Identifier note: limited to retrieved evidence. (ludwig2023secondarysclerosingcholangitis pages 1-3, moller2023secondarysclerosingcholangitis pages 1-2, OpenTargets Search: primary sclerosing cholangitis, NCT02424175 chunk 2) |
| Primary sclerosing cholangitis (PSC) | PSC; large-duct PSC; small-duct PSC | D015209 / **Cholangitis, Sclerosing** | No PSC-specific MONDO/EFO identifier extracted from the provided sources; umbrella mapping available as **EFO_0004268** | Diagnosed when characteristic cholangiographic multifocal short strictures/beading are present without another identifiable cause; small-duct PSC has normal cholangiography but PSC-consistent histology. Strong association with IBD. ICD codes: **not extracted from the provided sources**. Identifier note: limited to retrieved evidence. (naitoh2025the2024diagnostic pages 4-5, ludwig2023secondarysclerosingcholangitis pages 1-3, giorgio2026primarysclerosingcholangitis pages 2-4, naitoh2025the2024diagnostic media a72fe8f4) |
| Secondary sclerosing cholangitis (SSC) | SSC; ischemic cholangiopathy; SSC-CIP; COVID-19 SSC / SSC-COVID | D015209 / **Cholangitis, Sclerosing** | No SSC-specific MONDO/EFO identifier extracted from the provided sources; umbrella mapping available as **EFO_0004268** | PSC mimic with an identifiable cause such as ischemic, infectious, toxic/drug-induced, immunologic, congenital, or critical-illness-related injury; often worse prognosis, with biliary casts common in SSC-CIP/COVID-19 SSC. ICD codes: **not extracted from the provided sources**. Identifier note: limited to retrieved evidence. (ludwig2023secondarysclerosingcholangitis pages 3-4, ludwig2023secondarysclerosingcholangitis pages 7-9, hofstetter2024endoscopiccharacterizationand pages 6-7, leonhardt2023hepatobiliarylongtermconsequences pages 1-2) |
| IgG4-related sclerosing cholangitis (IgG4-SC) | IgG4-SC; IgG4-related SC; IgG4-related cholangitis | D015209 / **Cholangitis, Sclerosing** | No IgG4-SC-specific MONDO/EFO identifier extracted from the provided sources | Immune-mediated biliary manifestation of IgG4-related disease; typically long-segment continuous extrahepatic strictures with bile duct wall thickening, elevated serum IgG4 in many patients, frequent autoimmune pancreatitis overlap, and marked corticosteroid responsiveness. ICD codes: **not extracted from the provided sources**. Identifier note: limited to retrieved evidence. (ludwig2023secondarysclerosingcholangitis pages 7-9, moller2023secondarysclerosingcholangitis pages 8-10, moller2023secondarysclerosingcholangitis pages 10-11) |
| Hepatobiliary malignancy complication relevant to PSC surveillance | Cholangiocarcinoma; adenocarcinoma of gallbladder and extrahepatic biliary tract | Not extracted from the provided sources | **MONDO_0018536** (adenocarcinoma of gallbladder and extrahepatic biliary tract) | Included here because malignancy surveillance is central in PSC/PSC-IBD; this is a complication/comorbidity rather than a synonym of sclerosing cholangitis. Identifier note: limited to retrieved evidence. (giorgio2026primarysclerosingcholangitis pages 7-9, OpenTargets Search: primary sclerosing cholangitis,secondary sclerosing cholangitis) |


*Table: This table summarizes the identifiers and common names available in the retrieved evidence for the sclerosing cholangitis disease family, emphasizing PSC, SSC, and IgG4-SC. It is useful for knowledge-base normalization while explicitly flagging where ICD or subtype-specific ontology identifiers were not available from the provided sources.*

*Important limitation:* This tool-based review did **not** retrieve PSC-specific MONDO/Orphanet/OMIM identifiers. The OpenTargets/ontology mapping available in retrieved evidence covers the umbrella term “sclerosing cholangitis” (EFO_0004268) rather than PSC subtype-specific ontologies. (OpenTargets Search: primary sclerosing cholangitis)

### 1.3 ICD coding notes (administrative data pitfalls)
PSC has historically lacked a distinct ICD code and is frequently coded under ICD-10 **K83.0** (“cholangitis”), which also includes more common acute entities (e.g., ascending cholangitis), lowering specificity for true PSC ascertainment. (molodecky2011validityofadministrative pages 1-2)

In ICD-10-CA (Canadian modification), PSC and SSC appear as subcodes under K83.0: **K83.00 primary sclerosing cholangitis** and **K83.01 secondary sclerosing cholangitis**, alongside **K83.02 ascending cholangitis**. (molodecky2011validityofadministrative pages 7-8)

### 1.4 Source type
Evidence in this report is predominantly **aggregated disease-level** research: population-based registries (England, Ontario), prospective registries, clinical series, and interventional trial registries; individual-patient evidence is present mainly as clinical case series (e.g., COVID-19 SSC) and pilot trials. (crothers2024pastcurrentand pages 1-2, leung2025primarysclerosingcholangitis–inflammatory pages 1-2, hofstetter2024endoscopiccharacterizationand pages 1-2)

---

## 2. Etiology
### 2.1 Disease causal factors (current understanding)
PSC is best supported as a **complex, immune-mediated, polygenic disease** in which genetic susceptibility (strong HLA signal plus many non-HLA loci) interacts with gut–liver axis biology (microbiome, bile acids, mucosal immunity) to drive chronic cholangiocyte injury and periductal fibrosis. (fiorucci2024bileacidsbasedtherapies pages 2-4, okada2026distinctphenotypeof pages 5-7)

SSC is etiologically heterogeneous and arises from identifiable insults (e.g., ischemic cholangiopathy/critical illness, infection, toxins/drugs, immunologic disorders). (ludwig2023secondarysclerosingcholangitis pages 7-9, moller2023secondarysclerosingcholangitis pages 1-2)

### 2.2 Risk factors
#### Genetic risk factors (susceptibility)
* A major PSC HLA risk haplotype reported in recent synthesis is **HLA-DRB1*13:01-DQA1*01:03-DQB1*06:03**. (pitoni2025navigatingneoplasmrisk pages 5-7)
* PSC shows strong HLA association and multiple GWAS non-HLA loci in immune regulation and bile-acid/barrier pathways; examples cataloged in a 2024 therapy/pathogenesis review include **IL2/IL21/IL2RA, CD28, CTLA4, BACH2, SH2B3, NFKB1, CCL20, GPR35**, among others. (fiorucci2024bileacidsbasedtherapies pages 2-4)
* Mendelian randomization using GWAS instruments supports a **causal association** from genetically predicted PSC to ulcerative colitis risk (but not Crohn’s disease), with shared SNPs reported (rs3184504, rs9858213, rs725613, rs10909839, rs4147359). (dong2024investigatingtheshared pages 1-3)

Authoritative target-disease association resources (OpenTargets) also prioritize immune-related genes including **IL2RA, SH2B3, BACH2, IRF5, IL10** for “sclerosing cholangitis,” consistent with immune genetic architecture. (OpenTargets Search: primary sclerosing cholangitis)

#### Environmental/clinical risk factors
* PSC is most commonly associated with IBD in Western cohorts (≈60–70% reported in several summaries), and this comorbidity shapes phenotype and cancer risk. (okada2026distinctphenotypeof pages 1-2, pitoni2025navigatingneoplasmrisk pages 1-2)
* For SSC in critically ill COVID-19 patients (SSC-CIP/COVID-SSC), risk factors preceding onset include **systemic hypoxia**, multi-organ failure severity (SOFA), **high fibrinogen**, and **ketamine exposure**; multivariate analysis identified fibrinogen and LDH as independent risk factors. (leonhardt2023hepatobiliarylongtermconsequences pages 1-2)

### 2.3 Protective factors
Robust, generalizable protective factors for PSC are not established. However, mechanistic and translational evidence suggests microbiome-driven induction of regulatory pathways may modulate gut inflammation in PSC-IBD contexts; in experimental models, sclerosing cholangitis altered microbiota and increased Foxp3+ Treg expansion with attenuation of colitis. (bedke2024protectivefunctionof pages 1-2)

### 2.4 Gene–environment and gene–microbiome interactions
A contemporary synthesis links genetic susceptibility, bile-acid dysregulation, and microbiome perturbations: PSC-IBD patients show dysfunctional bile-acid metabolism and altered microbial conversion of secondary bile acids, and lymphocyte trafficking pathways (e.g., α4β7/MAdCAM-1) integrate gut-derived antigenic stimulation with hepatic biliary inflammation. (pitoni2025navigatingneoplasmrisk pages 5-7, fiorucci2024bileacidsbasedtherapies pages 2-4)

---

## 3. Phenotypes
### 3.1 PSC phenotype spectrum (human clinical)
**Symptoms/signs** (typical, variable; adult-onset common)
* Common cholestatic symptom cluster: abdominal pain, pruritus, and fatigue reported in ~three-quarters of patients in a recent clinical review; fever with these suggests acute bacterial cholangitis. (giorgio2026primarysclerosingcholangitis pages 2-4)
* Depressive-type symptoms reported in ~one-quarter of patients in the same review. (giorgio2026primarysclerosingcholangitis pages 2-4)

**Laboratory abnormalities**
* Typical cholestatic pattern: elevated ALP and GGT; bilirubin elevated in ~28–40% (rising with progression), but ~25% may have normal liver tests. (giorgio2026primarysclerosingcholangitis pages 2-4)

**Imaging features**
* Hallmark cholangiography findings: multifocal beading/strictures with bile duct wall thickening/enhancement; peripheral pruning in chronic disease. (ludwig2023secondarysclerosingcholangitis pages 1-3)

**Dominant/clinically relevant strictures**
* Dominant stricture definitions incorporate radiologic stenosis and/or biochemical and symptom criteria; ERCP-based criteria may include difficulty passing >5 Fr catheter, and improvement (~20% ALP/bilirubin at 2–4 weeks) after dilation/stenting is used as supportive evidence. (giorgio2026primarysclerosingcholangitis pages 2-4)

### 3.2 PSC-IBD phenotype (intestinal)
PSC-associated IBD often has a distinct phenotype: extensive colitis with right-sided predominance, rectal sparing, and backwash ileitis; disease may be clinically mild/asymptomatic despite extensive involvement, but neoplasia risk is high, motivating early intensive surveillance. (okada2026distinctphenotypeof pages 1-2)

### 3.3 SSC-CIP / COVID-19 SSC phenotype
COVID-19 SSC and SSC-CIP often present with cholestatic enzymes and characteristic cholangiographic findings including biliary casts and intrahepatic duct destruction/rarefaction. In one tertiary center case series, all ERCPs revealed biliary casts, with severe intrahepatic duct rarefication in 9/17. (hofstetter2024endoscopiccharacterizationand pages 1-2)

### 3.4 HPO term suggestions (non-exhaustive)
(These are ontology suggestions; phenotype-to-HPO mappings were not explicitly provided in retrieved sources.)
* Pruritus **HP:0000989**
* Fatigue **HP:0012378**
* Abdominal pain **HP:0002027**
* Cholestasis **HP:0001396**
* Elevated alkaline phosphatase **HP:0003155**
* Elevated gamma-glutamyltransferase **HP:0003285**
* Hyperbilirubinemia **HP:0002904**
* Cholangitis **HP:0006565**
* Biliary strictures **HP:0031377** (term may vary by HPO version)
* Liver fibrosis **HP:0001395**
* Cirrhosis **HP:0001394**

---

## 4. Genetic / molecular information
### 4.1 Causal genes vs susceptibility genes
PSC is typically **not monogenic**; current evidence supports **polygenic susceptibility** dominated by HLA associations and multiple immune-regulatory loci rather than single causal variants. (fiorucci2024bileacidsbasedtherapies pages 2-4)

### 4.2 Susceptibility loci and functional themes
Susceptibility loci and associated pathways cluster around: T-cell activation/co-stimulation (e.g., CD28/CTLA4 axis), cytokine signaling (IL2RA), innate immune regulation (NFKB1), and gut barrier/bile-acid signaling (e.g., GPBAR1/TGR5, GPR35). (fiorucci2024bileacidsbasedtherapies pages 2-4)

### 4.3 Variant classification and allele frequencies
ClinVar/gnomAD-level variant cataloging (ACMG/AMP classification, allele frequencies) was **not available** in retrieved sources for PSC; therefore specific pathogenic variant nomenclature and population frequencies cannot be reliably populated from the current evidence set.

### 4.4 Epigenetics
Epigenetic mechanisms are implicated in reviews of PSC pathogenesis, but explicit methylation/histone datasets were not extracted in this tool run.

---

## 5. Environmental information
### 5.1 Infectious agents / triggers
In SSC-CIP associated with severe COVID-19, mechanisms considered include direct cholangiocyte injury (ACE2 expression in cholangiocytes is discussed in reviews) plus ischemic and microthrombotic injury; causality of direct viral damage versus critical-illness-associated ischemia remains debated. (bartoli2023secondarysclerosingcholangitis pages 1-2, leonhardt2023hepatobiliarylongtermconsequences pages 12-13)

### 5.2 Lifestyle factors
No consistent lifestyle risk/protective factors for PSC were extracted in retrieved sources.

---

## 6. Mechanism / pathophysiology
### 6.1 Causal chain (PSC; current model)
A convergent model supported by recent authoritative reviews describes PSC as a **gut–liver axis disorder**:
1) **Barrier dysfunction and dysbiosis** allow microbial products/metabolites to reach portal circulation (leaky gut). (fousekis2025gut–liveraxismicrobiota pages 2-4)
2) **Innate immune activation** in the liver (Kupffer cells, sinusoidal endothelium, cholangiocytes) triggers inflammatory pathways including NF-κB and inflammasome signaling with pro-inflammatory cytokine production (e.g., IL-6, IL-1β, TNF-α). (fiorucci2024bileacidsbasedtherapies pages 2-4, fousekis2025gut–liveraxismicrobiota pages 2-4)
3) **Adaptive immune recruitment and trafficking**: mucosal homing pathways (MAdCAM-1/α4β7, CCR9/CCL25, VAP-1) misdirect gut-primed lymphocytes to the liver and biliary tree, sustaining antigen-driven cholangiocyte injury. (fiorucci2024bileacidsbasedtherapies pages 2-4, fousekis2025gut–liveraxismicrobiota pages 10-11)
4) **Cholangiocyte activation and fibrosis**: injured cholangiocytes produce pro-inflammatory and pro-fibrotic mediators (TNFα, IL-6, MCP-1, TGFβ), activating hepatic stellate cells/portal fibroblasts and driving periductal fibrosis and ductular reaction. (fiorucci2024bileacidsbasedtherapies pages 2-4)

### 6.2 Bile acid signaling and receptor biology
PSC shows altered bile-acid profiles (elevated serum primary/conjugated bile acids; reduced secondary bile acids; increased primary:secondary ratio) and dysregulated bile-acid receptor signaling through **FXR** and **GPBAR1/TGR5**, which modulate intestinal barrier integrity, immune activation, and cholangiocyte homeostasis. (fiorucci2024bileacidsbasedtherapies pages 9-10)

In particular, TGR5 on cholangiocytes supports chloride/bicarbonate secretion (“bicarbonate umbrella”) and anti-inflammatory barrier effects; downregulation is posited to contribute to PSC. (fousekis2025gut–liveraxismicrobiota pages 7-9)

### 6.3 Microbiome and bile acid metabolism (2024 evidence)
A 2024 metagenomic + bile acid mass spectrometry study (n=116; 54 IBD-PSC, 62 IBD-only) found:
* Reduced microbial gene richness (p=0.004)
* Significant compositional shift (PERMANOVA R2=0.01, p=0.03)
* Species differences: decreased *Blautia obeum*; increased *Veillonella atypica*, *Veillonella dispar*, and *Clostridium scindens* (q<0.05)
* Increased microbial gene abundance for secondary bile-acid metabolism
* Serum bile-acid differences (decreased sulphated secondary bile acids; increased conjugated secondary bile acids) associated with greater liver fibrosis. (leibovitzh2024inflammatoryboweldisease pages 1-2)

### 6.4 Cell types involved (CL term suggestions)
* Cholangiocyte / biliary epithelial cell (CL:0000062)
* Kupffer cell / liver macrophage (CL:0000235)
* Monocyte-derived macrophage (CL:0000863)
* Hepatic stellate cell (CL:0000632)
* CD4+ T cell (CL:0000624), Th17 cell (CL:0000899)
* Regulatory T cell (CL:0000815)
* NK cell (CL:0000623)
* Dendritic cell (CL:0000451)

### 6.5 GO biological process suggestions
* leukocyte migration (GO:0050900)
* inflammatory response (GO:0006954)
* NF-kappaB signaling (GO:0043122)
* cytokine-mediated signaling pathway (GO:0019221)
* bile acid metabolic process (GO:0008206)
* regulation of epithelial barrier function (e.g., tight junction organization GO:0120193)
* extracellular matrix organization (GO:0030198)
* collagen fibril organization (GO:0030199)
* fibrosis / wound healing (e.g., GO:0042060 wound healing)

---

## 7. Anatomical structures affected
### 7.1 Organ and system level
* Primary: intrahepatic and/or extrahepatic bile ducts; liver (digestive/hepatobiliary system). (ludwig2023secondarysclerosingcholangitis pages 1-3)
* Secondary (complications): colon/large intestine in PSC-IBD with high neoplasia risk. (okada2026distinctphenotypeof pages 1-2, pitoni2025navigatingneoplasmrisk pages 1-2)

### 7.2 Tissue/cellular level and UBERON suggestions
* bile duct (UBERON:0000059)
* intrahepatic bile duct (UBERON:0001230)
* extrahepatic bile duct (UBERON:0001103)
* liver (UBERON:0002107)
* colon (UBERON:0001155)

---

## 8. Temporal development
### PSC onset and course
PSC is generally chronic and progressive, with median transplant-free survival commonly reported as ~14–21 years from diagnosis (tertiary vs population-based settings). (crothers2024pastcurrentand pages 1-2, pitoni2025navigatingneoplasmrisk pages 1-2)

### SSC-CIP temporal profile
In SSC-CIP, bile duct destruction can begin within days of ICU care and progress rapidly; in COVID-19 SSC, cholangiopathy can present months after infection in reported cohorts and has poor outcomes. (hofstetter2024endoscopiccharacterizationand pages 6-7, bartoli2023secondarysclerosingcholangitis pages 7-8)

---

## 9. Inheritance and population
### 9.1 Epidemiology (recent quantitative data)
| Condition/subtype | Geography/source (with URL) | Study period | Key statistics (incidence/prevalence/AAPC or mortality/survival/HR) | Notes |
|---|---|---|---|---|
| PSC-IBD prevalence trends | England; Crothers et al. 2024, *Lancet Regional Health - Europe*; https://doi.org/10.1016/j.lanepe.2024.101002 | 2015–2027 forecast | Among ages 18–60, prevalence was 5.0/100,000 in 2015 (5.7 including IBD diagnosed after PSC) and 7.6/100,000 in 2020 (8.6 including subsequent IBD); AAPC 8.8% from 2015–2020; projected to reach 11.7/100,000 by 2027 (95% PI 10.8–12.7), or 13.3/100,000 including subsequent IBD; projected AAPC 6.4% (crothers2024pastcurrentand pages 1-2) | Nationwide population-based prevalence/projection study; also notes median transplant-free survival reported as 14–21 years from diagnosis (crothers2024pastcurrentand pages 1-2) |
| PSC-IBD epidemiology and outcomes | Ontario, Canada; Leung et al. 2025, *JHEP Reports*; https://doi.org/10.1016/j.jhepr.2024.101272 | 2002–2018 | Incidence 0.46/100,000 person-years; prevalence 5.53/100,000. About 1 PSC-IBD diagnosis per 50 new IBD diagnoses, and ~1 person with PSC-IBD per 100 people living with IBD. IBD diagnosed before PSC in 83%. Compared with IBD alone, PSC-IBD had 4.5-fold greater transplant/death risk. If IBD preceded PSC, transplant/death HR 1.34 and death HR 2.73 (leung2025primarysclerosingcholangitis–inflammatory pages 1-2) | Population-based study emphasizing diagnostic sequence; higher socioeconomic status associated with higher incidence and faster increase over time (leung2025primarysclerosingcholangitis–inflammatory pages 1-2) |
| Secondary sclerosing cholangitis in critically ill COVID-19 patients (SSC-CIP) | Berlin, Germany; Leonhardt et al. 2023, *Hepatology International*; https://doi.org/10.1007/s12072-023-10521-0 | COVID-19 cohort during pandemic; hospitalized patients including 1,082 ventilated cases | SSC occurred exclusively in invasively ventilated patients at 1 in 43 ventilated COVID-19 patients; 1-year transplant-free survival 40%. Additional outcome metrics reported: HR for death 3.91; median survival 5.7 vs 26.8 months; ~22% may require liver transplantation (leonhardt2023hepatobiliarylongtermconsequences pages 12-13, leonhardt2023hepatobiliarylongtermconsequences pages 1-2) | Risk factors preceding SSC-CIP included systemic hypoxia, high SOFA score, high fibrinogen, and ketamine exposure; fibrinogen and LDH were independent risk factors (leonhardt2023hepatobiliarylongtermconsequences pages 12-13, leonhardt2023hepatobiliarylongtermconsequences pages 1-2) |
| COVID-19-associated secondary sclerosing cholangitis | Single tertiary center; Hofstetter et al. 2024, *Journal of Gastrointestinal and Liver Diseases*; https://doi.org/10.15403/jgld-5476 | Feb 2020–Oct 2022 | Among 258 mechanically ventilated COVID-19 patients, COVID-19 SSC occurred in 2.6% (10 in-house cases; 7 referred total cohort n=17). Mortality was 14/17 (82%); 3 patients remained in follow-up for possible liver transplantation (hofstetter2024endoscopiccharacterizationand pages 1-2, hofstetter2024endoscopiccharacterizationand pages 6-7) | ERC showed biliary casts in all cases; many had severe rarefication of intrahepatic ducts (9/17) and strictures (4/17). Endoscopic therapy was used as a bridge to transplant but recurrence was common (hofstetter2024endoscopiccharacterizationand pages 1-2, hofstetter2024endoscopiccharacterizationand pages 6-7) |


*Table: This table summarizes recent population-based and clinical outcome data for PSC/PSC-IBD and SSC-CIP, highlighting prevalence trends, incidence, survival, and mortality. It is useful for quickly comparing burden and prognosis across major sclerosing cholangitis subtypes.*

### 9.2 Familial aggregation (genetic component)
Familial aggregation is supported by increased risk in first-degree relatives (reported as >10-fold increased in some summaries), consistent with polygenic inheritance. (okada2026distinctphenotypeof pages 5-7)

---

## 10. Diagnostics
### 10.1 Standard diagnostic approach
PSC diagnosis typically integrates:
* Cholestatic liver tests (ALP/GGT predominant pattern) and
* Cholangiographic findings on **MRCP** or **ERCP** showing multifocal strictures/beading,
* With exclusion of secondary causes (including IgG4-SC, malignancy, stones). (ludwig2023secondarysclerosingcholangitis pages 1-3, giorgio2026primarysclerosingcholangitis pages 2-4)

MRCP is preferred as a first-line noninvasive test. (ludwig2023secondarysclerosingcholangitis pages 1-3)

### 10.2 2024 diagnostic criteria (recent development)
The 2024 Japanese diagnostic criteria for PSC define **large-duct PSC** by strictures on cholangiography and **small-duct PSC** by normal cholangiography with PSC-consistent histology. Imaging criterion includes characteristic findings such as multifocal band-like strictures, beaded appearance, pruned-tree appearance, or diverticulum-like outpouching; laboratory criteria include elevated ALP (adults) or GGT (children) and histology may show onion-skin lesion/fibrous obliterative cholangitis. (naitoh2025the2024diagnostic pages 4-5)

Table summarizing these criteria is available as a cited figure/table capture. (naitoh2025the2024diagnostic media a72fe8f4)

### 10.3 Differential diagnosis (key mimics)
* SSC etiologies (ischemic, infectious, toxic, immunologic, congenital) can mimic PSC on imaging. (ludwig2023secondarysclerosingcholangitis pages 7-9)
* IgG4-SC often shows long-segment continuous strictures with circumferential wall thickening; serum IgG4 elevation occurs in ~70–80%; corticosteroids usually lead to dramatic response. (moller2023secondarysclerosingcholangitis pages 10-11)

### 10.4 Prognostic scoring / biomarkers (limited to retrieved evidence)
The Mayo Risk Score is widely used in PSC and is incorporated into several trials and observational studies for risk stratification. (NCT02424175 chunk 1, giorgio2026primarysclerosingcholangitis pages 2-4)

---

## 11. Outcome / prognosis
### 11.1 PSC survival and major outcomes
Population-based and tertiary-cohort summaries cite median transplant-free survival ~14–21 years. (pitoni2025navigatingneoplasmrisk pages 1-2)

### 11.2 Malignancy risks and surveillance-relevant outcomes
* PSC carries a substantial lifetime cholangiocarcinoma (CCA) risk (>20% in several summaries); annual CCA incidence is commonly cited at ~0.5–1.2%/year. (pitoni2025navigatingneoplasmrisk pages 1-2, giorgio2026primarysclerosingcholangitis pages 7-9)
* PSC-IBD markedly elevates colorectal cancer risk (reviewed estimates range ~4–10× vs IBD alone; some syntheses cite ~10-fold). (pitoni2025navigatingneoplasmrisk pages 1-2)

### 11.3 SSC-CIP / COVID-19 SSC outcomes
In COVID-19 SSC-CIP cohorts, prognosis is poor: incidence among invasively ventilated patients was ~1 in 43 with 1-year transplant-free survival ~40%. (leonhardt2023hepatobiliarylongtermconsequences pages 1-2)

In a tertiary-center COVID-19 SSC case series, mortality was 82% (14/17). (hofstetter2024endoscopiccharacterizationand pages 1-2)

---

## 12. Treatment
### 12.1 Current standard of care (real-world implementation)
* No established disease-modifying medical therapy has been proven to improve transplant-free survival; management is largely supportive with complication surveillance and liver transplantation when indicated. (pitoni2025navigatingneoplasmrisk pages 1-2, fiorucci2024bileacidsbasedtherapies pages 10-11)
* ERCP is used for dominant/clinically relevant strictures and to evaluate/exclude cholangiocarcinoma, including tissue sampling and therapeutic dilation/stenting as clinically appropriate. (giorgio2026primarysclerosingcholangitis pages 2-4)

### 12.2 Pharmacotherapy and investigational therapies (2023–2024 prioritized)
#### Bile-acid and nuclear receptor pathways
* **norUrsodeoxycholic acid (norUDCA)**: Phase 3 trial ongoing/active (NCT03872921); primary outcomes include prevention of disease progression assessed by partial normalization of serum ALP and liver histology over 2 years. (NCT03872921 chunk 1)
* **FXR agonists (e.g., cilofexor)**: Phase 2 completed; phase 3 program listed as terminated in a 2024 therapeutic landscape review. (NCT02943460 chunk 1, fiorucci2024bileacidsbasedtherapies pages 12-13)

#### Microbiome-directed therapies
* **FMT (pilot, completed)**: NCT02424175 open-label pilot (n=10) defined success as ≥50% improvement in ALP/bilirubin/ALT/AST; also assessed microbiome diversity and bile-acid metabolomics. (NCT02424175 chunk 1)
* **FMT (2023–2024 expansion)**: NCT06286709 (Phase 2, recruiting) uses reduction in ALP at 48 weeks as the primary endpoint with extensive fibrosis and PRO endpoints. (fiorucci2024bileacidsbasedtherapies pages 13-15)
* **Vancomycin**: a multicenter randomized placebo-controlled trial (NCT03710122; terminated due to funding) assessed ALP normalization and liver stiffness; a separate European trial VanC-IT (NCT05876182; recruiting) uses ALP change from baseline as primary outcome and includes bile acids, cytokines, immune phenotyping, and PROs. (NCT03710122 chunk 1, NCT05876182 chunk 1)

#### PPAR agonists / fibrates (evidence summarized)
A 2024 therapeutic review reports substantial ALP reduction in a fibrate trial (fenofibrate vs placebo) and ongoing bezafibrate and elafibranor programs. (fiorucci2024bileacidsbasedtherapies pages 16-18, fiorucci2024bileacidsbasedtherapies pages 11-12)

### 12.3 MAXO (Medical Action Ontology) term suggestions
(ontology suggestions)
* Liver transplantation (MAXO:0001175)
* Endoscopic retrograde cholangiopancreatography (MAXO:0000587)
* Balloon dilation of biliary stricture (procedure term; MAXO mapping may be institution-specific)
* Biliary stenting (procedure term)
* Colonoscopy surveillance (MAXO:0000507)
* Antibiotic therapy (MAXO:0000127)
* Fecal microbiota transplantation (MAXO:0000755)

---

## 13. Prevention
Primary prevention strategies for PSC are not established due to unclear etiology. Current preventive care is largely **secondary/tertiary prevention** via surveillance and complication prevention:
* Annual colonoscopy is widely recommended for PSC-IBD due to high CRC risk. (pitoni2025navigatingneoplasmrisk pages 1-2, pitoni2025navigatingneoplasmrisk pages 11-13)
* Hepatobiliary malignancy surveillance commonly uses MRI/MRCP every 6–12 months ± CA19-9; gallbladder ultrasound surveillance every 6–12 months is discussed in cancer-risk reviews. (pitoni2025navigatingneoplasmrisk pages 11-13)

---

## 14. Other species / natural disease
This tool run did not retrieve veterinary natural-history studies of sclerosing cholangitis across non-human species; therefore cross-species natural disease assertions cannot be made from the current evidence set.

---

## 15. Model organisms and experimental systems
### 15.1 Mouse models used for PSC-like cholangitis and mechanistic studies
* **Mdr2-deficient (Abcb4−/−) mouse**: widely used experimental sclerosing cholangitis model; used in 2024 mechanistic work interrogating how colitis interacts with cholangitis and fibrosis. ()
* Experimental colitis + cholangitis models (e.g., DDC-fed models) are used to probe gut–liver axis interactions. (bedke2024protectivefunctionof pages 1-2)

### 15.2 Organoid and ex vivo models (2023–2024)
* A 2023 study used **Mdr2−/− mice** plus **human intrahepatic cholangiocyte organoids** to test placental MSC therapy via TGR5 pathway, integrating RNA-seq and bile-acid LC-MS/MS. ()
* Patient-derived cholangiocyte organoid systems are being used to test immune pathways (e.g., IL-17 signaling) and therapeutic strategies, supporting organoids as translational PSC models. ()

---

## Direct quotes from abstracts (selected)
* SSC imaging review abstract: “Sclerosing cholangitis (SC) represents a spectrum of chronic progressive cholestatic diseases… characterized by patchy inflammation, fibrosis, and stricturing.” (Möller et al., 2023) (moller2023secondarysclerosingcholangitis pages 1-2)
* England epidemiology study notes PSC is “a rare, invariably progressive cholestatic liver disease…” with high cancer risk and transplantation relevance. (Crothers et al., 2024) (crothers2024pastcurrentand pages 1-2)
* COVID-19 SSC-CIP cohort: “One in every 43 invasively ventilated COVID-19 patients developed this complication… The 1-year transplant-free survival rate… was 40%.” (Leonhardt et al., 2023) (leonhardt2023hepatobiliarylongtermconsequences pages 1-2)
* PSC-IBD microbiome study: “Patients with IBD-PSC had reduced microbial gene richness… and… increased abundance of microbial genes involved in secondary BA metabolism.” (Leibovitzh et al., 2024) (leibovitzh2024inflammatoryboweldisease pages 1-2)

---

## Evidence gaps and limitations (important for knowledge base population)
1) PSC subtype-specific MONDO/Orphanet/OMIM identifiers were not retrieved in this tool run; only umbrella ontology mappings and MeSH were available. (OpenTargets Search: primary sclerosing cholangitis, NCT02943460 chunk 2)
2) ClinVar/gnomAD variant-level details (ACMG classes, allele frequencies) were not retrieved.
3) Some surveillance and guideline statements were available via reviews rather than primary guidelines; guideline PDFs (e.g., AASLD/EASL) were not directly retrieved in this run.



References

1. (ludwig2023secondarysclerosingcholangitis pages 1-3): Daniel R. Ludwig, Mark A. Anderson, Malak Itani, Kedar G. Sharbidre, Neeraj Lalwani, and Raj M. Paspulati. Secondary sclerosing cholangitis: mimics of primary sclerosing cholangitis. Abdominal Radiology (New York), 48:151-165, May 2023. URL: https://doi.org/10.1007/s00261-022-03551-z, doi:10.1007/s00261-022-03551-z. This article has 32 citations.

2. (moller2023secondarysclerosingcholangitis pages 1-2): Kathleen Möller, Barbara Braden, Emma L. Culver, Christian Jenssen, Ehsan Safai Zadeh, Amjad Alhyari, Christian Görg, André Ignee, Michael Hocke, Yi Dong, Siyu Sun, Siegbert Faiss, and Christoph F. Dietrich. Secondary sclerosing cholangitis and igg4-sclerosing cholangitis – a review of cholangiographic and ultrasound imaging. Endoscopic Ultrasound, 12:181-199, Dec 2023. URL: https://doi.org/10.4103/eus-d-22-00208, doi:10.4103/eus-d-22-00208. This article has 16 citations.

3. (crothers2024pastcurrentand pages 1-2): Hannah Crothers, James Ferguson, Mohammed Nabil Quraishi, Rachel Cooney, Tariq H. Iqbal, and Palak J. Trivedi. Past, current, and future trends in the prevalence of primary sclerosing cholangitis and inflammatory bowel disease across england (2015–2027): a nationwide, population-based study. The Lancet Regional Health - Europe, 44:101002, Sep 2024. URL: https://doi.org/10.1016/j.lanepe.2024.101002, doi:10.1016/j.lanepe.2024.101002. This article has 21 citations.

4. (pitoni2025navigatingneoplasmrisk pages 1-2): Demis Pitoni, Arianna Dal Buono, Roberto Gabbiadini, Vincenzo Ronca, Francesca Colapietro, Nicola Pugliese, Davide Giuseppe Ribaldone, Cristina Bezzio, Ana Lleo, and Alessandro Armuzzi. Navigating neoplasm risk in inflammatory bowel disease and primary sclerosing cholangitis. Cancers, 17:2165, Jun 2025. URL: https://doi.org/10.3390/cancers17132165, doi:10.3390/cancers17132165. This article has 1 citations.

5. (leibovitzh2024inflammatoryboweldisease pages 1-2): Haim Leibovitzh, Shadi Nayeri, Krzysztof Borowski, Cristian Hernandez-Rocha, Sun-Ho Lee, Williams Turpin, Joanne M Stempak, Iqbaljit Sandhu, Raquel Milgrom, Michelle I Smith, Kenneth Croitoru, Gideon M Hirschfield, Aliya Gulamhusein, and Mark S Silverberg. Inflammatory bowel disease associated with primary sclerosing cholangitis is associated with an altered gut microbiome and bile acid profile. Journal of Crohn's & Colitis, 18:1957-1966, Jul 2024. URL: https://doi.org/10.1093/ecco-jcc/jjae096, doi:10.1093/ecco-jcc/jjae096. This article has 22 citations.

6. (NCT03872921 chunk 1):  norUrsodeoxycholic Acid vs Placebo in PSC. Dr. Falk Pharma GmbH. 2018. ClinicalTrials.gov Identifier: NCT03872921

7. (ludwig2023secondarysclerosingcholangitis pages 3-4): Daniel R. Ludwig, Mark A. Anderson, Malak Itani, Kedar G. Sharbidre, Neeraj Lalwani, and Raj M. Paspulati. Secondary sclerosing cholangitis: mimics of primary sclerosing cholangitis. Abdominal Radiology (New York), 48:151-165, May 2023. URL: https://doi.org/10.1007/s00261-022-03551-z, doi:10.1007/s00261-022-03551-z. This article has 32 citations.

8. (ludwig2023secondarysclerosingcholangitis pages 7-9): Daniel R. Ludwig, Mark A. Anderson, Malak Itani, Kedar G. Sharbidre, Neeraj Lalwani, and Raj M. Paspulati. Secondary sclerosing cholangitis: mimics of primary sclerosing cholangitis. Abdominal Radiology (New York), 48:151-165, May 2023. URL: https://doi.org/10.1007/s00261-022-03551-z, doi:10.1007/s00261-022-03551-z. This article has 32 citations.

9. (moller2023secondarysclerosingcholangitis pages 10-11): Kathleen Möller, Barbara Braden, Emma L. Culver, Christian Jenssen, Ehsan Safai Zadeh, Amjad Alhyari, Christian Görg, André Ignee, Michael Hocke, Yi Dong, Siyu Sun, Siegbert Faiss, and Christoph F. Dietrich. Secondary sclerosing cholangitis and igg4-sclerosing cholangitis – a review of cholangiographic and ultrasound imaging. Endoscopic Ultrasound, 12:181-199, Dec 2023. URL: https://doi.org/10.4103/eus-d-22-00208, doi:10.4103/eus-d-22-00208. This article has 16 citations.

10. (OpenTargets Search: primary sclerosing cholangitis): Open Targets Query (primary sclerosing cholangitis, 25 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

11. (NCT02424175 chunk 2): Joshua Korzenik. Fecal Microbiota Transplantation for the Treatment of Primary Sclerosing Cholangitis.. Brigham and Women's Hospital. 2016. ClinicalTrials.gov Identifier: NCT02424175

12. (naitoh2025the2024diagnostic pages 4-5): Itaru Naitoh, Hiroyuki Isayama, Nobuhisa Akamatsu, Suguru Mizuno, Toshio Fujisawa, Nobuhiro Nakamoto, Yousuke Nakai, Shuichiro Umetsu, Mitsuyoshi Suzuki, Shintaro Yagi, Hironori Haga, Kenji Notohara, Katsuhiro Sano, Susumu Tazuma, Takahiro Nakazawa, and Atsushi Tanaka. The 2024 diagnostic criteria for primary sclerosing cholangitis. Journal of gastroenterology, Jun 2025. URL: https://doi.org/10.1007/s00535-025-02265-5, doi:10.1007/s00535-025-02265-5. This article has 12 citations and is from a domain leading peer-reviewed journal.

13. (giorgio2026primarysclerosingcholangitis pages 2-4): Sofia Svensson Di Giorgio, Chiara Maria Scandavini, Antonio Molinaro, Urban Arnelo, and Roberto Valente. Primary sclerosing cholangitis: diagnosis, management, and clinical challenges. Journal of Clinical Medicine, 15:1149, Feb 2026. URL: https://doi.org/10.3390/jcm15031149, doi:10.3390/jcm15031149. This article has 1 citations.

14. (naitoh2025the2024diagnostic media a72fe8f4): Itaru Naitoh, Hiroyuki Isayama, Nobuhisa Akamatsu, Suguru Mizuno, Toshio Fujisawa, Nobuhiro Nakamoto, Yousuke Nakai, Shuichiro Umetsu, Mitsuyoshi Suzuki, Shintaro Yagi, Hironori Haga, Kenji Notohara, Katsuhiro Sano, Susumu Tazuma, Takahiro Nakazawa, and Atsushi Tanaka. The 2024 diagnostic criteria for primary sclerosing cholangitis. Journal of gastroenterology, Jun 2025. URL: https://doi.org/10.1007/s00535-025-02265-5, doi:10.1007/s00535-025-02265-5. This article has 12 citations and is from a domain leading peer-reviewed journal.

15. (hofstetter2024endoscopiccharacterizationand pages 6-7): Pia Hofstetter, Ina Zuber-Jerger, Alexander Mehrl, Bernhard Graf, Dirk Lunz, Matthias Lubnow, Thomas Müller, Stephan Schmid, Martina Müller, and Arne Kandulski. Endoscopic characterization and outcome of covid-19 patients with secondary sclerosing cholangitis: a case series of a tertiary center. Journal of gastrointestinal and liver diseases : JGLD, 33 2:218-225, Jun 2024. URL: https://doi.org/10.15403/jgld-5476, doi:10.15403/jgld-5476. This article has 1 citations.

16. (leonhardt2023hepatobiliarylongtermconsequences pages 1-2): Silke Leonhardt, Christian Jürgensen, Josephine Frohme, Donata Grajecki, Andreas Adler, Michael Sigal, Julia Leonhardt, Julian M. Voll, Jan Matthias Kruse, Roland Körner, Kai-Uwe Eckardt, Hans-Joachim Janssen, Volker Gebhardt, Marc D. Schmittner, Stefan Hippenstiel, Martin Witzenrath, Norbert Suttorp, Elisa T. Helbig, Lena J. Lippert, Paula Stubbemann, Pinkus Tober-Lau, David Hillus, Sascha S. Haenel, Alexandra Horn, Willi M. Koch, Nadine Olk, Mirja Mittermaier, Fridolin Steinbeis, Tilman Lingscheid, Bettina Temmesfeld-Wollbrück, Thomas Zoller, Holger Müller-Redetzky, Alexander Uhrig, Daniel Grund, Christoph Ruwwe-Glösenkamp, Miriam S. Stegemann, Katrin M. Heim, Ralf H. Hübner, Christian Drosten, Victor M. Corman, Bastian Opitz, Martin Möckel, Felix Balzer, Claudia Spies, Steffen Weber-Carstens, Chantip Dang-Heine, Michael Hummel, Georg Schwanitz, Uwe D. Behrens, Maria Rönnefarth, Sein Schmidt, Alexander Krannich, Saskia Zvorc, Jenny Kollek, Christof von Kalle, Jan Doehn, Christoph Tabeling, Linda Jürgens, Malte Kleinschmidt, Sophy Denker, Moritz Pfeiffer, Belén Millet Pascual-Leone, Luisa Mrziglod, Felix Machleidt, Sebastian Albus, Felix Bremer, Tim Andermann, Carmen Garcia, Philipp Knape, Philipp M. Krause, Liron Lechtenberg, Yaosi Li, Panagiotis Pergantis, Till Jacobi, Teresa Ritter, Berna Yedikat, Lennart Pfannkuch, Christian Zobel, Ute Kellermann, Susanne Fieberg, Laure Bosquillon de Jarcy, Anne Wetzel, Markus C. Brack, Moritz Müller-Plathe, Daniel Zickler, Andreas Edel, Britta Stier, Nils B. Müller, Philipp Enghard, Lucie Kretzler, Lil A. Meyer-Arndt, Linna Li, Isabelle Wirsching, Denise Treue, Dana Briesemeister, Jenny Schlesinger, Daniel Wendisch, Anna L. Hiller, Sophie Brumhard, Christian Frey, Hendrik Müller-Ide, Michael Bauer, Charlotte Thibeault, Florian Kurth, Leif Erik Sander, Tobias Müller, and Frank Tacke. Hepatobiliary long-term consequences of covid-19: dramatically increased rate of secondary sclerosing cholangitis in critically ill covid-19 patients. Hepatology International, 17:1610-1625, Apr 2023. URL: https://doi.org/10.1007/s12072-023-10521-0, doi:10.1007/s12072-023-10521-0. This article has 26 citations and is from a peer-reviewed journal.

17. (moller2023secondarysclerosingcholangitis pages 8-10): Kathleen Möller, Barbara Braden, Emma L. Culver, Christian Jenssen, Ehsan Safai Zadeh, Amjad Alhyari, Christian Görg, André Ignee, Michael Hocke, Yi Dong, Siyu Sun, Siegbert Faiss, and Christoph F. Dietrich. Secondary sclerosing cholangitis and igg4-sclerosing cholangitis – a review of cholangiographic and ultrasound imaging. Endoscopic Ultrasound, 12:181-199, Dec 2023. URL: https://doi.org/10.4103/eus-d-22-00208, doi:10.4103/eus-d-22-00208. This article has 16 citations.

18. (giorgio2026primarysclerosingcholangitis pages 7-9): Sofia Svensson Di Giorgio, Chiara Maria Scandavini, Antonio Molinaro, Urban Arnelo, and Roberto Valente. Primary sclerosing cholangitis: diagnosis, management, and clinical challenges. Journal of Clinical Medicine, 15:1149, Feb 2026. URL: https://doi.org/10.3390/jcm15031149, doi:10.3390/jcm15031149. This article has 1 citations.

19. (OpenTargets Search: primary sclerosing cholangitis,secondary sclerosing cholangitis): Open Targets Query (primary sclerosing cholangitis,secondary sclerosing cholangitis, 25 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

20. (molodecky2011validityofadministrative pages 1-2): Natalie A. Molodecky, Robert P. Myers, Herman W. Barkema, Hude Quan, and Gilaad G. Kaplan. Validity of administrative data for the diagnosis of primary sclerosing cholangitis: a population‐based study. Liver International, 31:712-720, May 2011. URL: https://doi.org/10.1111/j.1478-3231.2011.02484.x, doi:10.1111/j.1478-3231.2011.02484.x. This article has 37 citations and is from a peer-reviewed journal.

21. (molodecky2011validityofadministrative pages 7-8): Natalie A. Molodecky, Robert P. Myers, Herman W. Barkema, Hude Quan, and Gilaad G. Kaplan. Validity of administrative data for the diagnosis of primary sclerosing cholangitis: a population‐based study. Liver International, 31:712-720, May 2011. URL: https://doi.org/10.1111/j.1478-3231.2011.02484.x, doi:10.1111/j.1478-3231.2011.02484.x. This article has 37 citations and is from a peer-reviewed journal.

22. (leung2025primarysclerosingcholangitis–inflammatory pages 1-2): Kristel K. Leung, Wenbin Li, Bettina Hansen, Aliya Gulamhusein, Lauren Lapointe-Shaw, Abdel Aziz Shaheen, Amanda Ricciuto, Eric I. Benchimol, Jennifer A. Flemming, and Gideon M. Hirschfield. Primary sclerosing cholangitis–inflammatory bowel disease: epidemiology, mortality, and impact of diagnostic sequence. JHEP Reports, 7:101272, Mar 2025. URL: https://doi.org/10.1016/j.jhepr.2024.101272, doi:10.1016/j.jhepr.2024.101272. This article has 16 citations and is from a peer-reviewed journal.

23. (hofstetter2024endoscopiccharacterizationand pages 1-2): Pia Hofstetter, Ina Zuber-Jerger, Alexander Mehrl, Bernhard Graf, Dirk Lunz, Matthias Lubnow, Thomas Müller, Stephan Schmid, Martina Müller, and Arne Kandulski. Endoscopic characterization and outcome of covid-19 patients with secondary sclerosing cholangitis: a case series of a tertiary center. Journal of gastrointestinal and liver diseases : JGLD, 33 2:218-225, Jun 2024. URL: https://doi.org/10.15403/jgld-5476, doi:10.15403/jgld-5476. This article has 1 citations.

24. (fiorucci2024bileacidsbasedtherapies pages 2-4): Stefano Fiorucci, Ginevra Urbani, Cristina Di Giorgio, Michele Biagioli, and Eleonora Distrutti. Bile acids-based therapies for primary sclerosing cholangitis: current landscape and future developments. Cells, 13:1650, Oct 2024. URL: https://doi.org/10.3390/cells13191650, doi:10.3390/cells13191650. This article has 16 citations.

25. (okada2026distinctphenotypeof pages 5-7): Haruka Okada, Shinya Sugimoto, Atsuto Kayashima, Yohei Mikami, Takanori Kanai, Nobuhiro Nakamoto, Yusuke Yoshimatsu, Hiroki Kiyohara, Yukie Nakadai, Ryosuke Kasuga, Nobuhito Taniki, Keisuke Ojiro, Shingo Usui, Shogo Sunaga, Ichiro Mizushima, Yuta Kaieda, Shohei Suzuki, Takaya Tabuchi, and Makoto Ueno. Distinct phenotype of primary sclerosing cholangitis-associated inflammatory bowel disease. Journal of Gastroenterology, Mar 2026. URL: https://doi.org/10.1007/s00535-026-02388-3, doi:10.1007/s00535-026-02388-3. This article has 0 citations and is from a domain leading peer-reviewed journal.

26. (pitoni2025navigatingneoplasmrisk pages 5-7): Demis Pitoni, Arianna Dal Buono, Roberto Gabbiadini, Vincenzo Ronca, Francesca Colapietro, Nicola Pugliese, Davide Giuseppe Ribaldone, Cristina Bezzio, Ana Lleo, and Alessandro Armuzzi. Navigating neoplasm risk in inflammatory bowel disease and primary sclerosing cholangitis. Cancers, 17:2165, Jun 2025. URL: https://doi.org/10.3390/cancers17132165, doi:10.3390/cancers17132165. This article has 1 citations.

27. (dong2024investigatingtheshared pages 1-3): Xuan Dong, Li-Li Gong, Mei-Zhu Hong, and Jin-Shui Pan. Investigating the shared genetic architecture between primary sclerosing cholangitis and inflammatory bowel diseases: a mendelian randomization study. BMC Gastroenterology, Feb 2024. URL: https://doi.org/10.1186/s12876-024-03162-6, doi:10.1186/s12876-024-03162-6. This article has 7 citations and is from a peer-reviewed journal.

28. (okada2026distinctphenotypeof pages 1-2): Haruka Okada, Shinya Sugimoto, Atsuto Kayashima, Yohei Mikami, Takanori Kanai, Nobuhiro Nakamoto, Yusuke Yoshimatsu, Hiroki Kiyohara, Yukie Nakadai, Ryosuke Kasuga, Nobuhito Taniki, Keisuke Ojiro, Shingo Usui, Shogo Sunaga, Ichiro Mizushima, Yuta Kaieda, Shohei Suzuki, Takaya Tabuchi, and Makoto Ueno. Distinct phenotype of primary sclerosing cholangitis-associated inflammatory bowel disease. Journal of Gastroenterology, Mar 2026. URL: https://doi.org/10.1007/s00535-026-02388-3, doi:10.1007/s00535-026-02388-3. This article has 0 citations and is from a domain leading peer-reviewed journal.

29. (bedke2024protectivefunctionof pages 1-2): Tanja Bedke, Friederike Stumme, Miriam Tomczak, Babett Steglich, Rongrong Jia, Simon Bohmann, Agnes Wittek, Jan Kempski, Emilia Göke, Marius Böttcher, Dominik Reher, Anissa Franke, Maximilian Lennartz, Till Clauditz, Guido Sauter, Thorben Fründt, Sören Weidemann, Gisa Tiegs, Christoph Schramm, Nicola Gagliani, Penelope Pelczar, and Samuel Huber. Protective function of sclerosing cholangitis on ibd. Gut, 73:1292-1301, Jun 2024. URL: https://doi.org/10.1136/gutjnl-2023-330856, doi:10.1136/gutjnl-2023-330856. This article has 38 citations and is from a highest quality peer-reviewed journal.

30. (bartoli2023secondarysclerosingcholangitis pages 1-2): Alessandra Bartoli, Carmela Cursaro, Hajrie Seferi, and Pietro Andreone. Secondary sclerosing cholangitis after sars-cov2: icu ketamine use or virus-specific biliary tropism and injury in the context of biliary ischemia in critically ill patients? Hepatic Medicine : Evidence and Research, 15:93-112, Aug 2023. URL: https://doi.org/10.2147/hmer.s384220, doi:10.2147/hmer.s384220. This article has 10 citations.

31. (leonhardt2023hepatobiliarylongtermconsequences pages 12-13): Silke Leonhardt, Christian Jürgensen, Josephine Frohme, Donata Grajecki, Andreas Adler, Michael Sigal, Julia Leonhardt, Julian M. Voll, Jan Matthias Kruse, Roland Körner, Kai-Uwe Eckardt, Hans-Joachim Janssen, Volker Gebhardt, Marc D. Schmittner, Stefan Hippenstiel, Martin Witzenrath, Norbert Suttorp, Elisa T. Helbig, Lena J. Lippert, Paula Stubbemann, Pinkus Tober-Lau, David Hillus, Sascha S. Haenel, Alexandra Horn, Willi M. Koch, Nadine Olk, Mirja Mittermaier, Fridolin Steinbeis, Tilman Lingscheid, Bettina Temmesfeld-Wollbrück, Thomas Zoller, Holger Müller-Redetzky, Alexander Uhrig, Daniel Grund, Christoph Ruwwe-Glösenkamp, Miriam S. Stegemann, Katrin M. Heim, Ralf H. Hübner, Christian Drosten, Victor M. Corman, Bastian Opitz, Martin Möckel, Felix Balzer, Claudia Spies, Steffen Weber-Carstens, Chantip Dang-Heine, Michael Hummel, Georg Schwanitz, Uwe D. Behrens, Maria Rönnefarth, Sein Schmidt, Alexander Krannich, Saskia Zvorc, Jenny Kollek, Christof von Kalle, Jan Doehn, Christoph Tabeling, Linda Jürgens, Malte Kleinschmidt, Sophy Denker, Moritz Pfeiffer, Belén Millet Pascual-Leone, Luisa Mrziglod, Felix Machleidt, Sebastian Albus, Felix Bremer, Tim Andermann, Carmen Garcia, Philipp Knape, Philipp M. Krause, Liron Lechtenberg, Yaosi Li, Panagiotis Pergantis, Till Jacobi, Teresa Ritter, Berna Yedikat, Lennart Pfannkuch, Christian Zobel, Ute Kellermann, Susanne Fieberg, Laure Bosquillon de Jarcy, Anne Wetzel, Markus C. Brack, Moritz Müller-Plathe, Daniel Zickler, Andreas Edel, Britta Stier, Nils B. Müller, Philipp Enghard, Lucie Kretzler, Lil A. Meyer-Arndt, Linna Li, Isabelle Wirsching, Denise Treue, Dana Briesemeister, Jenny Schlesinger, Daniel Wendisch, Anna L. Hiller, Sophie Brumhard, Christian Frey, Hendrik Müller-Ide, Michael Bauer, Charlotte Thibeault, Florian Kurth, Leif Erik Sander, Tobias Müller, and Frank Tacke. Hepatobiliary long-term consequences of covid-19: dramatically increased rate of secondary sclerosing cholangitis in critically ill covid-19 patients. Hepatology International, 17:1610-1625, Apr 2023. URL: https://doi.org/10.1007/s12072-023-10521-0, doi:10.1007/s12072-023-10521-0. This article has 26 citations and is from a peer-reviewed journal.

32. (fousekis2025gut–liveraxismicrobiota pages 2-4): Fotios S. Fousekis, Konstantinos Mpakogiannis, Georgios D. Lianos, Elisabetta Antonelli, Gabrio Bassotti, and Konstantinos H. Katsanos. Gut–liver axis, microbiota, bile acids, and immune response in pathogenesis of primary sclerosing cholangitis: an overview. Journal of Clinical Medicine, 14:7817, Nov 2025. URL: https://doi.org/10.3390/jcm14217817, doi:10.3390/jcm14217817. This article has 6 citations.

33. (fousekis2025gut–liveraxismicrobiota pages 10-11): Fotios S. Fousekis, Konstantinos Mpakogiannis, Georgios D. Lianos, Elisabetta Antonelli, Gabrio Bassotti, and Konstantinos H. Katsanos. Gut–liver axis, microbiota, bile acids, and immune response in pathogenesis of primary sclerosing cholangitis: an overview. Journal of Clinical Medicine, 14:7817, Nov 2025. URL: https://doi.org/10.3390/jcm14217817, doi:10.3390/jcm14217817. This article has 6 citations.

34. (fiorucci2024bileacidsbasedtherapies pages 9-10): Stefano Fiorucci, Ginevra Urbani, Cristina Di Giorgio, Michele Biagioli, and Eleonora Distrutti. Bile acids-based therapies for primary sclerosing cholangitis: current landscape and future developments. Cells, 13:1650, Oct 2024. URL: https://doi.org/10.3390/cells13191650, doi:10.3390/cells13191650. This article has 16 citations.

35. (fousekis2025gut–liveraxismicrobiota pages 7-9): Fotios S. Fousekis, Konstantinos Mpakogiannis, Georgios D. Lianos, Elisabetta Antonelli, Gabrio Bassotti, and Konstantinos H. Katsanos. Gut–liver axis, microbiota, bile acids, and immune response in pathogenesis of primary sclerosing cholangitis: an overview. Journal of Clinical Medicine, 14:7817, Nov 2025. URL: https://doi.org/10.3390/jcm14217817, doi:10.3390/jcm14217817. This article has 6 citations.

36. (bartoli2023secondarysclerosingcholangitis pages 7-8): Alessandra Bartoli, Carmela Cursaro, Hajrie Seferi, and Pietro Andreone. Secondary sclerosing cholangitis after sars-cov2: icu ketamine use or virus-specific biliary tropism and injury in the context of biliary ischemia in critically ill patients? Hepatic Medicine : Evidence and Research, 15:93-112, Aug 2023. URL: https://doi.org/10.2147/hmer.s384220, doi:10.2147/hmer.s384220. This article has 10 citations.

37. (NCT02424175 chunk 1): Joshua Korzenik. Fecal Microbiota Transplantation for the Treatment of Primary Sclerosing Cholangitis.. Brigham and Women's Hospital. 2016. ClinicalTrials.gov Identifier: NCT02424175

38. (fiorucci2024bileacidsbasedtherapies pages 10-11): Stefano Fiorucci, Ginevra Urbani, Cristina Di Giorgio, Michele Biagioli, and Eleonora Distrutti. Bile acids-based therapies for primary sclerosing cholangitis: current landscape and future developments. Cells, 13:1650, Oct 2024. URL: https://doi.org/10.3390/cells13191650, doi:10.3390/cells13191650. This article has 16 citations.

39. (NCT02943460 chunk 1):  Study to Evaluate the Safety, Tolerability, and Efficacy of Cilofexor in Adults With Primary Sclerosing Cholangitis Without Cirrhosis. Gilead Sciences. 2016. ClinicalTrials.gov Identifier: NCT02943460

40. (fiorucci2024bileacidsbasedtherapies pages 12-13): Stefano Fiorucci, Ginevra Urbani, Cristina Di Giorgio, Michele Biagioli, and Eleonora Distrutti. Bile acids-based therapies for primary sclerosing cholangitis: current landscape and future developments. Cells, 13:1650, Oct 2024. URL: https://doi.org/10.3390/cells13191650, doi:10.3390/cells13191650. This article has 16 citations.

41. (fiorucci2024bileacidsbasedtherapies pages 13-15): Stefano Fiorucci, Ginevra Urbani, Cristina Di Giorgio, Michele Biagioli, and Eleonora Distrutti. Bile acids-based therapies for primary sclerosing cholangitis: current landscape and future developments. Cells, 13:1650, Oct 2024. URL: https://doi.org/10.3390/cells13191650, doi:10.3390/cells13191650. This article has 16 citations.

42. (NCT03710122 chunk 1): Elizabeth Carey. Vancomycin for Primary Sclerosing Cholangitis. Elizabeth Carey. 2020. ClinicalTrials.gov Identifier: NCT03710122

43. (NCT05876182 chunk 1):  Vancomycin in Primary Sclerosing Cholangitis in Italy. University of Milano Bicocca. 2023. ClinicalTrials.gov Identifier: NCT05876182

44. (fiorucci2024bileacidsbasedtherapies pages 16-18): Stefano Fiorucci, Ginevra Urbani, Cristina Di Giorgio, Michele Biagioli, and Eleonora Distrutti. Bile acids-based therapies for primary sclerosing cholangitis: current landscape and future developments. Cells, 13:1650, Oct 2024. URL: https://doi.org/10.3390/cells13191650, doi:10.3390/cells13191650. This article has 16 citations.

45. (fiorucci2024bileacidsbasedtherapies pages 11-12): Stefano Fiorucci, Ginevra Urbani, Cristina Di Giorgio, Michele Biagioli, and Eleonora Distrutti. Bile acids-based therapies for primary sclerosing cholangitis: current landscape and future developments. Cells, 13:1650, Oct 2024. URL: https://doi.org/10.3390/cells13191650, doi:10.3390/cells13191650. This article has 16 citations.

46. (pitoni2025navigatingneoplasmrisk pages 11-13): Demis Pitoni, Arianna Dal Buono, Roberto Gabbiadini, Vincenzo Ronca, Francesca Colapietro, Nicola Pugliese, Davide Giuseppe Ribaldone, Cristina Bezzio, Ana Lleo, and Alessandro Armuzzi. Navigating neoplasm risk in inflammatory bowel disease and primary sclerosing cholangitis. Cancers, 17:2165, Jun 2025. URL: https://doi.org/10.3390/cancers17132165, doi:10.3390/cancers17132165. This article has 1 citations.

47. (NCT02943460 chunk 2):  Study to Evaluate the Safety, Tolerability, and Efficacy of Cilofexor in Adults With Primary Sclerosing Cholangitis Without Cirrhosis. Gilead Sciences. 2016. ClinicalTrials.gov Identifier: NCT02943460