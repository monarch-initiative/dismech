---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-04T12:24:54.208415'
end_time: '2026-04-04T12:41:57.499126'
duration_seconds: 1023.29
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: TP63-Related Ectodermal Dysplasia Spectrum
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 24
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** TP63-Related Ectodermal Dysplasia Spectrum
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **TP63-Related Ectodermal Dysplasia Spectrum** covering all of the
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
- **Disease Name:** TP63-Related Ectodermal Dysplasia Spectrum
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **TP63-Related Ectodermal Dysplasia Spectrum** covering all of the
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


# TP63-Related Ectodermal Dysplasia Spectrum — Disease Characteristics Research Report

## Target Disease
- **Disease name:** TP63-Related Ectodermal Dysplasia Spectrum (TP63-related disorders; p63-associated disorders) (cong2026p63inskin pages 12-14, zhuang2025molecularcharacterizationof pages 1-2)
- **Category:** Genetic, primarily ectodermal development / epithelial stem cell disorder (cong2026p63inskin pages 12-14, salois2023effectsoftp63 pages 3-4)
- **MONDO ID:** Not identified in the retrieved evidence set (no MONDO term was present in the ingested full texts).

---

## Executive summary
TP63-related ectodermal dysplasia spectrum comprises multiple autosomal-dominant developmental syndromes caused by heterozygous pathogenic variants in **TP63** (p63), a p53-family transcription factor essential for epithelial development and stem cell maintenance. The spectrum includes at least **EEC**, **AEC (Hay–Wells)**, **ADULT**, **limb–mammary syndrome**, **Rapp–Hodgkin syndrome**, and **split-hand/foot malformation 4 (SHFM4)**, with significant genotype–phenotype correlation by protein domain (DBD/OD vs SAM/TI) and allele-specific mechanisms (dominant-negative, gain-of-function, aggregation, isoform imbalance). Recent 2023–2024 work expands clinically actionable domains: (i) iPSC and in vivo models in AEC link **hemidesmosome/focal-adhesion downregulation** to skin erosions, (ii) rare neonatal **T-cell lymphopenia/athymia** presentations detected by newborn TREC screening with WES/WGS and treated with cultured thymus tissue implant, and (iii) a large 2023 cohort shows **TP63 gain-of-function variants contribute ~0.78% of idiopathic primary ovarian insufficiency cases** via constitutive TAp63α tetramerization and oocyte apoptosis. (salois2023effectsoftp63 pages 3-4, gall2024casereportartificial pages 2-3, huang2023tp63gainoffunctionmutations pages 2-3)

| Entity | Common synonym / expansion | OMIM / MIM noted in provided texts | Orphanet prevalence note in provided texts | Key TP63 domain(s) typically involved in provided texts | Notes / scope | Citations |
|---|---|---|---|---|---|---|
| TP63-related ectodermal dysplasia spectrum | TP63-related disorders; p63-associated disorders; TP63-associated syndromes | TP63 gene: MIM 603273 | Prenatal WES paper states the spectrum comprises six autosomal dominant syndromes | Predominantly DNA-binding domain (DBD) and sterile alpha motif (SAM); review notes ~80% of pathogenic changes affect DBD/OD, while AEC is strongly linked to SAM-domain lesions | Umbrella concept including EEC, AEC/Hay-Wells, Rapp-Hodgkin, ADULT, limb-mammary syndrome, and split-hand/foot malformation 4 | (cong2026p63inskin pages 12-14, gall2024casereportartificial pages 2-3) |
| EEC syndrome | Ectrodactyly-ectodermal dysplasia-clefting; ectrodactyly-ectodermal dysplasia-cleft lip/palate |  | ~1–9 per 100,000 newborns (Orpha.net, as quoted in 2023 ocular series) | DBD hotspot residues repeatedly noted (R204, R227, R279, R280, R304; also examples R279C/R279H/R340G) | Core triad is limb malformation, ectodermal dysplasia, and cleft lip/palate; important ocular morbidity includes limbal stem cell deficiency | (iorio2023…patientsaffected pages 9-11, cong2026p63inskin pages 12-14) |
| AEC syndrome | Ankyloblepharon-ectodermal defects-cleft lip/palate; Ankyloblepharon-ectodermal dysplasia-clefting; Hay-Wells syndrome |  |  | SAM domain mutations emphasized; example p.Gly600Val in exon 14; aggregation/misfolding mechanism also highlighted in review literature | Distinguished by ankyloblepharon and severe skin erosions/erythroderma with ectodermal defects and clefting | (cong2026p63inskin pages 12-14, ahuja2023ectrodactylyectodermaldysplasiaclefting pages 4-4) |
| Rapp-Hodgkin syndrome | RHS |  |  | Reported within TP63 SAM/other ectodermal-dysplasia-associated domains; 2026 review lists examples including 1709DelA and R279H | Historically considered overlapping with AEC; provided texts describe RHS as resembling AEC with mid-facial hypoplasia and no ankyloblepharon | (ahuja2023ectrodactylyectodermaldysplasiaclefting pages 2-4, cong2026p63inskin pages 14-16) |
| ADULT syndrome | Acro-dermato-ungual-lacrimal-tooth syndrome |  |  | Commonly DBD-associated in provided texts; recurrent residues listed include R298Q, R298G, R243W, R227Q; 2026 review highlights R298 and Q243W | Often includes lacrimal duct anomalies, nail/tooth defects, sparse hair, and mammary hypoplasia; freckling may help distinguish from EEC/AEC | (zhou2023casereportadult pages 2-4, cong2026p63inskin pages 14-16) |
| Limb-mammary syndrome | LMS | MIM #603543 (noted in provided text) |  | Mutations reported in provided review include R204Q and R227Q (DBD-associated examples) | Characterized by limb defects and mammary/nipple hypoplasia; cleft palate may occur with relatively limited skin involvement | (zhou2023casereportadult pages 2-4, ahuja2023ectrodactylyectodermaldysplasiaclefting pages 2-4) |
| Split-hand/foot malformation 4 | SHFM4 |  |  | Usually DBD-associated in the provided mechanistic literature; p.Arg319His and p.Met307Ile are examples discussed in recent/foundational reports | May occur as isolated limb malformation or overlap with broader TP63 syndromes; incomplete penetrance reported | (zhuang2025molecularcharacterizationof pages 9-10, gall2024casereportartificial pages 2-3) |


*Table: This table summarizes the umbrella TP63-related ectodermal dysplasia concept and the major named syndromes included in the spectrum. It highlights synonyms, any OMIM/MIM or prevalence details explicitly available in the retrieved texts, and the TP63 protein domains most often implicated.*

---

## 1. Disease information

### 1.1 What is the disease?
**TP63-related ectodermal dysplasia spectrum** is an umbrella term for clinically overlapping developmental syndromes caused by germline TP63 variants, characterized by variable combinations of:
- ectodermal defects (skin, hair, nails, teeth, sweat glands),
- craniofacial anomalies (cleft lip/palate),
- limb malformations (ectrodactyly/split-hand-foot),
- and, in some individuals, severe ocular surface disease (limbal stem cell deficiency) and rarer immune or gonadal phenotypes. (ahuja2023ectrodactylyectodermaldysplasiaclefting pages 2-4, iorio2023…patientsaffected pages 9-11, gall2024casereportartificial pages 2-3)

### 1.2 Key identifiers (from retrieved evidence)
- **TP63 gene:** OMIM/MIM **603273** (цабаи2025нарушенияполовогоразвития pages 10-10)
- **EEC3:** OMIM **#604292** (marakhonov2024ararecase pages 4-5)
- **Limb–mammary syndrome:** MIM **#603543** (ahuja2023ectrodactylyectodermaldysplasiaclefting pages 2-4)

**Not found in retrieved documents:** MONDO ID, MeSH ID, ICD-10/ICD-11 codes.

### 1.3 Synonyms and alternative names
- **EEC:** ectrodactyly–ectodermal dysplasia–clefting (iorio2023…patientsaffected pages 9-11)
- **AEC:** ankyloblepharon–ectodermal defects–cleft lip/palate; Hay–Wells syndrome (ahuja2023ectrodactylyectodermaldysplasiaclefting pages 4-4)
- **ADULT:** acro-dermato-ungual-lacrimal-tooth syndrome (zhou2023casereportadult pages 2-4)
- **SHFM4:** split-hand/foot malformation 4 (zhuang2025molecularcharacterizationof pages 1-2)

### 1.4 Evidence source types
The present synthesis draws on:
- **Human clinical reports/series (2023–2024):** ocular EEC/AEC series and multiple case reports including lacrimal surgery and newborn immunology presentations (iorio2023…patientsaffected pages 9-11, zhou2023casereportadult pages 2-4, gall2024casereportartificial pages 2-3)
- **Human genetics cohort study (2023):** TP63 gain-of-function variants in primary ovarian insufficiency (huang2023tp63gainoffunctionmutations pages 2-3)
- **Mechanistic experimental study (2023):** iPSC-derived keratinocytes, gene-corrected lines, and in vivo validation in mice for AEC skin erosions (salois2023effectsoftp63 pages 3-4)
- **Review synthesis (2025–2026):** domain/genotype correlations and isoform biology used as contextual “expert consensus” sources (cong2026p63inskin pages 12-14, murari2025p63amaster pages 4-6)

---

## 2. Etiology

### 2.1 Disease causal factors
- **Primary cause:** germline pathogenic variants in **TP63**. Disorders are usually **autosomal dominant**, including EEC and AEC (cong2026p63inskin pages 12-14).
- **Pathogenic mechanisms are allele- and domain-dependent**:
  - **DBD/OD variants** cluster at hotspot residues and can act via dominant-negative or loss-of-function effects (cong2026p63inskin pages 12-14, murari2025p63amaster pages 4-6).
  - **SAM-domain variants** (common in AEC) can lead to aggregation and functional loss, and (as shown experimentally) dysregulate adhesion gene programs (cong2026p63inskin pages 12-14, salois2023effectsoftp63 pages 3-4).
  - **TAp63α C-terminal/TID-disrupting variants** cause gain-of-function constitutive activation in oocytes, driving apoptosis and ovarian reserve depletion (huang2023tp63gainoffunctionmutations pages 2-3, vanderschelden2023heterozygoustp63pathogenic pages 1-2).

### 2.2 Risk factors
- **Genetic:** carrying a pathogenic TP63 variant. A SHFM4 family demonstrates **incomplete penetrance** for TP63 p.Arg319His (affected father/proband, unaffected carrier relatives), indicating variable expressivity and penetrance (zhuang2025molecularcharacterizationof pages 1-2, zhuang2025molecularcharacterizationof pages 4-6).
- **Environmental:** no direct gene–environment risk modifiers were identified in the retrieved evidence set.

### 2.3 Protective factors
No protective genetic or environmental factors were identified in the retrieved texts.

### 2.4 Gene–environment interactions
No direct GxE evidence was identified in the retrieved texts.

---

## 3. Phenotypes (with HPO suggestions)

Major phenotype groupings, onset patterns, and relevant HPO mappings are summarized below.

| Clinical feature | Suggested HPO term(s) | Typical syndromes | Onset/course notes | Evidence |
|---|---|---|---|---|
| Ectrodactyly / split-hand-foot malformation | Ectrodactyly (HP:0100259); Split hand (HP:0001171); Split foot (HP:0001839) | EEC, SHFM4, sometimes ADULT/LMS overlap | Congenital limb malformation; may occur in isolation (SHFM4) or with broader ectodermal findings; incomplete penetrance reported for SHFM4 | (zhuang2025molecularcharacterizationof pages 9-10, ahuja2023ectrodactylyectodermaldysplasiaclefting pages 2-4, zhou2023casereportadult pages 2-4) |
| Cleft lip and/or palate / high-arched palate | Cleft upper lip (HP:0000204); Cleft palate (HP:0000175); High palate / High-arched palate (HP:0000218) | EEC, AEC, LMS; high-arched palate reported in AEC/ADULT cases | Congenital craniofacial anomaly; clefting is part of classic EEC triad, while LMS may show cleft palate without extensive skin disease | (ahuja2023ectrodactylyectodermaldysplasiaclefting pages 2-4, zhou2023casereportadult pages 2-4, ahuja2023ectrodactylyectodermaldysplasiaclefting pages 4-4) |
| Skin erosions / fragile skin / xerosis | Skin erosion (HP:0008066); Xerosis (HP:0001024); Fragile skin | AEC, EEC | Usually neonatal/early childhood in AEC; may be chronic, recurrent, and wound-healing related; fragile/xerotic skin also described in EEC | (cong2026p63inskin pages 12-14, ahuja2023ectrodactylyectodermaldysplasiaclefting pages 2-4, salois2023effectsoftp63 pages 3-4, salois2023effectsoftp63 pages 4-6) |
| Sparse hair / hypotrichosis | Hypotrichosis (HP:0001006); Sparse scalp hair (HP:0008070) | EEC, AEC, ADULT | Congenital or early-childhood ectodermal manifestation; generally chronic/non-progressive though severity varies | (ahuja2023ectrodactylyectodermaldysplasiaclefting pages 2-4, zhou2023casereportadult pages 2-4) |
| Nail dystrophy / onychodystrophy | Nail dysplasia (HP:0002164); Onychodystrophy | EEC, AEC, ADULT, LMS | Congenital/childhood onset; persistent structural nail abnormality | (cong2026p63inskin pages 12-14, ahuja2023ectrodactylyectodermaldysplasiaclefting pages 2-4, zhou2023casereportadult pages 2-4) |
| Hypodontia / oligodontia / conical teeth | Hypodontia (HP:0009804); Oligodontia (HP:0000677); Conical tooth/teeth (HP:0000698) | EEC, AEC, ADULT | Usually recognized in childhood with tooth eruption failure/abnormal morphology; important functional and QoL impact on feeding, speech, dentition | (ahuja2023ectrodactylyectodermaldysplasiaclefting pages 2-4, zhou2023casereportadult pages 2-4) |
| Hypohidrosis | Hypohidrosis (HP:0000975) | AEC, ADULT, broader TP63-ED spectrum | Present from infancy/childhood; chronic reduced sweating may affect heat tolerance | (zhou2023casereportadult pages 2-4, ahuja2023ectrodactylyectodermaldysplasiaclefting pages 4-4) |
| Lacrimal duct anomalies / epiphora | Nasolacrimal duct obstruction; Lacrimal duct aplasia/atresia; Epiphora (HP:0001132) | ADULT, EEC | Congenital lacrimal outflow abnormality; may present with chronic tearing and require surgical correction | (ahuja2023ectrodactylyectodermaldysplasiaclefting pages 2-4, zhou2023casereportadult pages 2-4) |
| Ankyloblepharon / symblepharon | Ankyloblepharon (HP:0000627); Symblepharon | AEC, ADULT overlap, EEC ocular disease spectrum | Congenital eyelid fusion in AEC; symblepharon may complicate chronic ocular surface disease | (cong2026p63inskin pages 12-14, iorio2023…patientsaffected pages 9-11, zhou2023casereportadult pages 2-4) |
| Limbal stem cell deficiency / corneal neovascularization / pannus | Limbal stem cell deficiency; Corneal neovascularization (HP:0007710); Corneal pannus | EEC, broader TP63 ocular spectrum | Progressive ocular surface disease causing corneal thinning, conjunctivalization, neovascularization, pannus, and vision loss | (iorio2023…patientsaffected pages 9-11, iorio2023…patientsaffected pages 14-14) |
| Meibomian gland agenesis / dysfunction | Meibomian gland abnormality; Meibomian gland aplasia/agenesis | EEC, ADULT ocular involvement | Congenital adnexal abnormality contributing to tear-film instability and ocular surface desiccation | (iorio2023…patientsaffected pages 9-11, iorio2023…patientsaffected pages 14-14) |
| T-cell lymphopenia / athymia | T cell lymphopenia (HP:0005403); Athymia / Thymic hypoplasia | Overlapping TP63-related syndrome (EEC/AEC-like presentations) | Detected in newborn period by low/undetectable TREC; may reflect thymic stromal/epithelial defect and can be severe/persistent | (gall2024casereportartificial pages 2-3, marakhonov2024ararecase pages 1-2, marakhonov2024ararecase pages 10-10) |
| Mammary gland hypoplasia / absent nipples or breasts | Breast hypoplasia (HP:0000769); Nipple hypoplasia / Athelia | ADULT, LMS | Congenital developmental anomaly; often useful for syndrome differentiation from EEC/AEC | (ahuja2023ectrodactylyectodermaldysplasiaclefting pages 2-4, zhou2023casereportadult pages 2-4) |
| Primary ovarian insufficiency | Primary ovarian insufficiency (HP:0008209); Hypergonadotropic hypogonadism | TP63-related ovarian phenotype; may overlap with LMS or occur in isolated TP63-associated disease | Usually adolescent/adult presentation with amenorrhea/infertility; mechanistically linked to constitutive TAp63 activation and oocyte apoptosis | (цабаи2025нарушенияполовогоразвития pages 10-10, vanderschelden2023heterozygoustp63pathogenic pages 1-2) |


*Table: This table maps clinically important features reported across the TP63-related ectodermal dysplasia spectrum to suggested HPO terms, typical syndrome associations, and brief onset/course notes. It is useful as a structured phenotype curation aid for knowledge-base entry and differential diagnosis.*

Key clinically prominent phenotypes supported by 2023–2024 evidence include:
- **Progressive ocular surface disease in EEC**: progressive **limbal stem cell deficiency (LSCD)** is described as the most disabling manifestation in most patients, leading to corneal thinning, neovascularization, pannus, conjunctivalization, and gradual vision loss/blindness, compounded by meibomian gland agenesis and tear-film instability (human clinical series) (iorio2023…patientsaffected pages 9-11).
- **AEC skin erosions**: extensive skin erosions/fragility in AEC with molecularly defined adhesion defects (see Mechanisms) (salois2023effectsoftp63 pages 3-4).
- **Congenital lacrimal abnormalities in ADULT**: lacrimal duct aplasia/stenosis with chronic epiphora, treated surgically (zhou2023casereportadult pages 2-4).
- **Rare immune phenotype**: newborn-detected profound T-cell lymphopenia and suspected congenital athymia in TP63-related syndrome (gall2024casereportartificial pages 2-3).
- **Gonadal phenotype**: isolated primary ovarian insufficiency due to TP63 gain-of-function variants (huang2023tp63gainoffunctionmutations pages 2-3).

Quality-of-life impact is most explicitly documented for ocular disease (severe photophobia, marked vision impairment, multiple surgeries, and reports of total ocular surface impairment) (iorio2023…patientsaffected pages 9-11).

---

## 4. Genetic / molecular information

### 4.1 Causal gene
- **TP63** (tumor protein p63), a p53-family transcription factor; multiple isoforms including **TAp63** and **ΔNp63** with distinct functions (cong2026p63inskin pages 16-19, murari2025p63amaster pages 4-6).

### 4.2 Variant spectrum and genotype–phenotype correlations
- **Domain clustering:** A 2026 review synthesis reports that ~**80%** of disease-causing mutations cluster in **DNA-binding domain (DBD)** and **oligomerization domain (OD)**; AEC is strongly associated with **SAM-domain** lesions (cong2026p63inskin pages 12-14).
- **DBD hotspot residues:** R204, R227, R279, R280, R304 (cong2026p63inskin pages 12-14).
- **SHFM4 incomplete penetrance:** TP63 p.Arg319His demonstrates unaffected carriers in the same pedigree (zhuang2025molecularcharacterizationof pages 1-2).

### 4.3 Functional consequences (examples)
- **Dominant-negative / reduced transactivation (EEC3 example):** TP63 p.Arg343Trp (DBD) is reported to reduce transactivation activity in a dominant-negative manner and is associated with EEC and neonatal lymphopenia (marakhonov2024ararecase pages 1-2).
- **Gain-of-function (SHFM4 example):** p.Arg319His was hypothesized to act as a gain-of-function allele upregulating downstream targets (CDH3, DLX5), disrupting p63–DLX signaling and apical ectodermal ridge stratification (zhuang2025molecularcharacterizationof pages 1-2, zhuang2025molecularcharacterizationof pages 6-8).
- **Gain-of-function in oocytes (POI):** TID-disrupting variants cause constitutive TAp63α tetramers and oocyte apoptosis (huang2023tp63gainoffunctionmutations pages 2-3).

### 4.4 Population frequency
- Some variants are reported as absent from gnomAD (e.g., p.Arg343Trp) in clinical genetic evaluation (marakhonov2024ararecase pages 4-5).

### 4.5 Modifier genes / epigenetics
No explicit modifier genes or disease-specific epigenetic signatures were identified in the retrieved evidence set.

---

## 5. Environmental information
No non-genetic environmental contributors were identified in the retrieved evidence set; TP63 disorders are primarily monogenic developmental disorders.

---

## 6. Mechanism / pathophysiology

### 6.1 Core concepts (current understanding)
TP63 encodes multiple isoforms; **ΔNp63** is central to epithelial stemness and keratinocyte programs, whereas **TAp63α** plays a critical role in oocyte quality control and apoptosis. Isoform imbalance can alter keratinocyte fate decisions (cong2026p63inskin pages 12-14, murari2025p63amaster pages 4-6).

### 6.2 Mechanistic chains by major phenotype

#### A) Skin erosions in AEC (2023 mechanistic advance)
**Human iPSC + in vivo validation** demonstrate that AEC-associated TP63 SAM-domain mutations can drive a coordinated reduction of hemidesmosome and focal-adhesion programs:
- Salois et al. (Experimental Dermatology, 2023-07; https://doi.org/10.1111/exd.14885) used **patient-derived iPSC lines** (AEC mutations F513S, I537T, R598L), created **gene-corrected isogenic controls**, and differentiated both into keratinocytes. They identified downregulation of hemidesmosome components such as **ITGA6, ITGB4, COL17A1**, cytoplasmic adaptors **DST, PLEC**, and laminin-332 genes **LAMA3, LAMB3, LAMC2**, with impaired keratinocyte adhesion and migration across ECM substrates. They propose integrin defects weaken keratinocyte anchorage to basement membrane and contribute to erosions (salois2023effectsoftp63 pages 3-4, salois2023effectsoftp63 pages 4-6).
- These changes were corroborated in **chimeric mice** expressing TP63-AEC transgene and in AEC patient skin (salois2023effectsoftp63 pages 3-4, salois2023effectsoftp63 pages 7-11).

**Visual evidence:** figures summarizing downregulation and schematic model are available from the paper (salois2023effectsoftp63 media 83f76dc6, salois2023effectsoftp63 media e89fc6fc).

Suggested ontology terms:
- **GO biological process:** cell adhesion; epithelial cell migration; extracellular matrix organization; hemidesmosome assembly (supported mechanistically) (salois2023effectsoftp63 pages 3-4).
- **GO cellular component:** hemidesmosome; focal adhesion; basement membrane (salois2023effectsoftp63 pages 3-4).
- **CL cell types:** keratinocyte; epidermal basal cell (ΔNp63-high) (cong2026p63inskin pages 12-14, salois2023effectsoftp63 pages 3-4).

#### B) Limb malformations (EEC/SHFM4)
Mechanistic evidence links TP63 to apical ectodermal ridge (AER) programs and downstream transcription factors:
- SHFM4 p.Arg319His is hypothesized to disrupt the **p63–DLX signaling pathway**; DLX5 is a downstream gene altered in patient RNA-seq/qPCR (zhuang2025molecularcharacterizationof pages 1-2).
- The same study contextualizes prior work that p63 regulates AER targets and that p63 loss reduces FGF8 causing limb defects (zhuang2025molecularcharacterizationof pages 6-8).

Suggested GO/CL terms:
- **GO BP:** limb development; regulation of transcription involved in pattern specification.
- **CL:** ectodermal cell; limb bud epithelial cell.

#### C) Ocular surface disease (EEC)
- The 2023 ocular series emphasizes **progressive LSCD** as the main driver of corneal thinning, neovascularization, pannus, and conjunctivalization, leading to vision loss/blindness, with additional contribution from Meibomian gland agenesis and lacrimal dysfunction (iorio2023…patientsaffected pages 9-11).

#### D) Immune phenotype (rare): thymic epithelial dysfunction → T-cell lymphopenia
- A 2024 case report used newborn screening (undetectable TREC), rapid WGS, and an **artificial thymic organoid** assay, supporting a thymic stromal/epithelial rather than hematopoietic intrinsic defect; the patient received **allogenic cultured thymus tissue implant** with early evidence of thymopoiesis post-implant (gall2024casereportartificial pages 2-3).
- A separate 2024 report identified TP63 p.Arg343Trp (DBD) in a newborn with T-cell lymphopenia detected by TREC screening (marakhonov2024ararecase pages 1-2).

Suggested terms:
- **CL:** thymic epithelial cell; T cell.
- **GO BP:** thymus development; T cell differentiation.

#### E) Primary ovarian insufficiency (TAp63α gain-of-function)
- Huang et al. (J Clin Invest, 2023-03; https://doi.org/10.1172/jci162315) studied **1,030** women with POI and identified heterozygous TP63 variants; they report that gain-of-function TP63 mutations **“accounted for 0.78% (8 of 1,030) of the studied cases”** and that variants disrupting the **transactivation inhibitory domain (TID)** cause constitutive tetramerization/activation, upregulation of apoptosis programs, and oocyte depletion in mouse models (huang2023tp63gainoffunctionmutations pages 2-3, huang2023tp63gainoffunctionmutations pages 3-5).

Suggested terms:
- **GO BP:** intrinsic apoptotic signaling pathway; oocyte development.
- **CL:** oocyte.

---

## 7. Anatomical structures affected

Primary structures (with UBERON suggestions):
- **Skin / epidermis** (UBERON:0002097) and **basement membrane zone** (supported by hemidesmosome defects) (salois2023effectsoftp63 pages 3-4)
- **Hair follicles** and **nails** (ectodermal appendages) (ahuja2023ectrodactylyectodermaldysplasiaclefting pages 2-4)
- **Teeth** (tooth development defects: hypodontia/oligodontia) (ahuja2023ectrodactylyectodermaldysplasiaclefting pages 2-4)
- **Limb autopod** (split-hand/foot; ectrodactyly) (zhuang2025molecularcharacterizationof pages 1-2)
- **Eye / cornea / limbus / meibomian glands / lacrimal system** (progressive ocular surface disease; lacrimal duct anomalies) (iorio2023…patientsaffected pages 9-11, zhou2023casereportadult pages 2-4)
- **Thymus** (suspected congenital athymia; thymic epithelial involvement) (gall2024casereportartificial pages 2-3)
- **Ovary / oocytes** (POI due to TAp63α GOF variants) (huang2023tp63gainoffunctionmutations pages 2-3)

Subcellular/localization themes:
- **Nucleus** (transcription factor), **chromatin/enhancers** (p63 pioneer activity) (cong2026p63inskin pages 16-19)
- **Cell–matrix junctions**: hemidesmosomes, focal adhesions (salois2023effectsoftp63 pages 3-4)

---

## 8. Temporal development
- Most features are **congenital or childhood-onset** (limb, clefts, ectodermal appendage defects, skin erosions), but some complications are **progressive**:
  - **EEC ocular disease**: LSCD often progressive with severe impairment in adulthood (iorio2023…patientsaffected pages 9-11).
  - **POI**: amenorrhea in reported patients ranged from **13–29 years** (huang2023tp63gainoffunctionmutations pages 2-3).
  - **Immune phenotype**: T-cell lymphopenia identified at birth via newborn screening (gall2024casereportartificial pages 2-3, marakhonov2024ararecase pages 1-2).

---

## 9. Inheritance and population

### 9.1 Inheritance pattern
- Predominantly **autosomal dominant** for core syndromes such as EEC and AEC (cong2026p63inskin pages 12-14).
- **Incomplete penetrance/variable expressivity** documented in SHFM4 family with TP63 p.Arg319His (zhuang2025molecularcharacterizationof pages 1-2).

### 9.2 Epidemiology
- **EEC prevalence:** ~**1–9 per 100,000 newborns** (quoted from Orpha.net in a 2023 ocular clinical series) (iorio2023…patientsaffected pages 9-11).
- Robust prevalence/incidence estimates for AEC/ADULT/LMS/SHFM4 were not present in the retrieved evidence set.

---

## 10. Diagnostics

### 10.1 Clinical recognition
Key clinical patterns:
- EEC: ectrodactyly + ectodermal signs + clefting; high risk of ocular surface disease (ahuja2023ectrodactylyectodermaldysplasiaclefting pages 2-4, iorio2023…patientsaffected pages 9-11).
- AEC: ankyloblepharon and skin erosions prominent (ahuja2023ectrodactylyectodermaldysplasiaclefting pages 2-4, ahuja2023ectrodactylyectodermaldysplasiaclefting pages 4-4).
- ADULT: lacrimal anomalies and mammary hypoplasia; typically no clefting (ahuja2023ectrodactylyectodermaldysplasiaclefting pages 2-4, zhou2023casereportadult pages 2-4).

### 10.2 Genetic testing approaches used in recent reports
- **WES with Sanger confirmation:** used for ADULT diagnosis (TP63 p.G173V) (zhou2023casereportadult pages 2-4).
- **Newborn screening (TREC) → confirmatory immunophenotyping + WES/WGS:** detected TP63-associated T-cell lymphopenia (marakhonov2024ararecase pages 1-2, gall2024casereportartificial pages 2-3).
- **WES + karyotype/CMA + ACMG classification + RNA-seq/qPCR (research setting):** used to establish SHFM4 p.Arg319His with incomplete penetrance and proposed mechanism (zhuang2025molecularcharacterizationof pages 4-6, zhuang2025molecularcharacterizationof pages 1-2).

### 10.3 Differential diagnosis considerations
TP63 syndromes overlap; helpful differentiators described in clinical sources include:
- **AEC:** ankyloblepharon + skin erosions,
- **ADULT:** mammary/nipple hypoplasia and freckling with lacrimal disease and typically absent clefting,
- **LMS:** limb + mammary defects with limited skin involvement,
- **EEC:** classic triad and high ocular morbidity. (ahuja2023ectrodactylyectodermaldysplasiaclefting pages 2-4, zhou2023casereportadult pages 2-4)

---

## 11. Outcome / prognosis
- **Overall survival:** often described as non–life-threatening for EEC, but morbidity can be substantial (iorio2023…byp63associated pages 9-11).
- **Ocular prognosis:** progressive LSCD can lead to severe vision loss/blindness and major QoL impact; multiple procedures are often required (iorio2023…patientsaffected pages 9-11).
- **Immune phenotype:** when present, can be severe (SCID-like T-cell lymphopenia) and may require thymus implantation; early evidence of thymopoiesis post-implant was observed in the 2024 case report (gall2024casereportartificial pages 2-3).
- **Reproductive prognosis:** POI impacts fertility; mechanistic studies suggest TAp63α activation as potential therapeutic target, but no approved TP63-directed therapy is reported (huang2023tp63gainoffunctionmutations pages 10-11).

---

## 12. Treatment

### 12.1 Current applications and real-world implementations (documented)
- **Ocular surface management in EEC/AEC:** tear substitutes, steroid drops, tear plugs, tear duct flushing, corneal transplantation, amniotic membrane grafting, cataract surgery (iorio2023…patientsaffected pages 9-11).
- **Lacrimal surgery in ADULT:** binocular dacryocystorhinostomy with artificial lacrimal duct implantation with reported success (zhou2023casereportadult pages 2-4).
- **Immune-directed intervention for suspected athymia:** **allogenic cultured thymus tissue implant** after functional ATO assay supported thymic stromal defect (gall2024casereportartificial pages 2-3).

### 12.2 Experimental / emerging therapeutic directions (as reported in review/reference synthesis)
- Allele-specific siRNA strategies to restore mutant p63-associated stem cell function in ocular contexts are cited as a translational direction (iorio2023…patientsaffected pages 14-14).
- Broader genome editing/stem cell and small-molecule approaches are discussed in later review synthesis, but detailed clinical evidence is outside the 2023–2024 primary dataset retrieved here (cong2026p63inskin pages 14-16).

### 12.3 Suggested MAXO terms (examples)
See intervention mapping table:

| Domain / variant type | Example variants (from evidence) | Proposed mechanism | Associated phenotype / syndrome | Diagnostic approach used | Real-world intervention with suggested MAXO term name(s) | Evidence citations |
|---|---|---|---|---|---|---|
| DNA-binding domain missense hotspot | p.Arg279Cys, p.Arg279His, p.Arg340Gly | Reported as impairing p63 function; ocular series describes heterozygous missense mutations causing haploinsufficiency in tetrameric p63 complexes, with progressive limbal stem-cell deficiency as a major downstream consequence | EEC with severe ocular disease, including LSCD, corneal thinning/neovascularization, pannus, vision loss | Clinical phenotyping plus TP63 variant detection in affected patients | Ocular surface surveillance and reconstructive procedures reported in case series, including corneal transplantation / amniotic grafting; suggested MAXO: ophthalmologic examination, corneal transplantation, amniotic membrane transplantation | (iorio2023…patientsaffected pages 9-11, iorio2023…patientsaffected pages 14-14) |
| DNA-binding domain missense, de novo | p.Arg343Trp (c.1027C>T) | Reduced TP63 transactivation in a dominant-negative manner; structural modeling suggests loss of DNA-contact and destabilization | EEC3 / TP63-associated syndrome with neonatal T-cell lymphopenia | Newborn TREC screening followed by confirmatory immunophenotyping and WES | Comprehensive immunologic evaluation and longitudinal immune monitoring; suggested MAXO: immunologic monitoring, newborn screening, exome sequencing | (marakhonov2024ararecase pages 1-2, marakhonov2024ararecase pages 4-5) |
| DNA-binding domain missense, de novo | p.Cys347Tyr (c.1040G>A) | Thymic stromal / epithelial defect suspected rather than hematopoietic-intrinsic failure; TP63 expression restricted to thymic epithelial cells in referenced analysis | Overlapping TP63-related syndrome with profound neonatal T-cell lymphopenia / suspected congenital athymia | Undetectable TREC on newborn screen, flow cytometry, rapid WGS, artificial thymic organoid assay | Allogeneic cultured thymus tissue implant; suggested MAXO: thymus tissue transplantation, flow cytometry, genome sequencing | (gall2024casereportartificial pages 2-3) |
| SAM-domain missense | p.F513S, p.I537T, p.R598L | AEC-associated reduction of hemidesmosome/focal-adhesion components; impaired keratinocyte adhesion and migration; review literature also describes SAM mutations as causing pathological aggregation / functional loss | AEC (Hay-Wells) with skin erosions / fragility | Patient-derived iPSC generation, genome editing to create gene-corrected controls, RNA-seq, qRT-PCR, Western blot, validation in chimeric mice and patient skin | Supportive wound/skin care is implied standard care; experimental mechanism-guided approaches under development; suggested MAXO: wound care, skin barrier therapy, induced pluripotent stem cell assay | (salois2023effectsoftp63 pages 3-4, salois2023effectsoftp63 pages 1-3, salois2023effectsoftp63 pages 4-6, salois2023effectsoftp63 pages 7-11, cong2026p63inskin pages 12-14) |
| SAM-domain missense, de novo | p.Gly600Val (c.1799G>T) | Molecular modeling suggests local conformational distortion affecting protein-protein interactions | AEC with extensive skin erosions, erythroderma, nail dystrophy, xerophthalmia, oligodontia, hypohidrosis | Clinical evaluation plus TP63 sequencing and protein structural modeling | Symptomatic multidisciplinary care for skin, eye, dental, and craniofacial disease; suggested MAXO: dermatologic care, dental care, ophthalmologic care, cleft repair | (ahuja2023ectrodactylyectodermaldysplasiaclefting pages 4-4) |
| DNA-binding domain missense associated with ADULT | p.G173V (c.518G>T); recurrent ADULT residues listed include R298Q, R298G, R243W, R227Q, P127L, R337Q, V114M, N6H | Variant predicted deleterious; ADULT literature/reviews support gain-of-function transactivation for some ADULT alleles | ADULT syndrome with lacrimal duct aplasia/stenosis, symblepharon, sparse hair, nail dystrophy, oligodontia, mammary hypoplasia, digit anomalies | WES with Sanger confirmation | Binocular dacryocystorhinostomy with artificial tear duct implantation and duct excision; suggested MAXO: dacryocystorhinostomy, lacrimal duct stent placement, ophthalmologic surgery | (zhou2023casereportadult pages 2-4, murari2025p63amaster pages 4-6) |
| DNA-binding domain missense with incomplete penetrance | p.Arg319His (c.956G>A); related residue p.Arg319Cys | Family study proposes gain-of-function effect with upregulation of TP63 downstream genes (CDH3, DLX5), disrupting p63-DLX/AER biology; explicit incomplete penetrance and variable expressivity | SHFM4 with isolated limb malformations in some carriers and unaffected carriers in same family | WES, RNA-seq, qPCR, structural modeling, ACMG classification, exclusion of chromosomal abnormalities by karyotype/CMA | Genetic counseling and prenatal diagnosis relevance emphasized; suggested MAXO: genetic counseling, prenatal genetic testing, exome sequencing | (zhuang2025molecularcharacterizationof pages 1-2, zhuang2025molecularcharacterizationof pages 6-8, zhuang2025molecularcharacterizationof pages 4-6) |
| TAp63α C-terminal / transactivation inhibitory domain-disrupting variants | p.R647C and other TID-disrupting heterozygous mutations; truncating variants and intragenic CNV affecting TP63 also reported | Isoform-specific constitutive activation of TAp63α tetramers, driving oocyte apoptosis; loss of inactive dimeric conformation | Isolated primary ovarian insufficiency / hypergonadotropic hypogonadism; occasionally overlap with limb-mammary phenotypes | WES with CNV confirmation by long-range PCR and Sanger; cohort screening in POI patients | Reproductive / endocrine management and genetic counseling are the practical applications described; suggested MAXO: genetic counseling, fertility counseling, endocrine evaluation | (vanderschelden2023heterozygoustp63pathogenic pages 1-2, цабаи2025нарушенияполовогоразвития pages 10-10, murari2025p63amaster pages 4-6) |
| Mixed TP63 ectodermal dysplasia spectrum, mostly DBD or OD lesions | DBD hotspots R204, R227, R279, R280, R304; LMS examples R204Q, R227Q; ADULT examples R298/Q243W | Broadly loss-of-function, gain-of-function, isoform imbalance, and domain-specific aggregation mechanisms; ~80% of pathogenic mutations cluster in DBD/OD per review synthesis | EEC, AEC, ADULT, LMS, RHS, SHFM4 | Syndrome-directed molecular testing, panel/exome/genome sequencing depending presentation | Current care mainly supportive and surgical; emerging strategies include allele-specific siRNA, AAV-CRISPR/base editing, limbal stem-cell therapy, and small-molecule disaggregation approaches; suggested MAXO: supportive care, surgery, RNA interference therapy, gene editing therapy, stem cell therapy | (cong2026p63inskin pages 12-14, cong2026p63inskin pages 14-16, murari2025p63amaster pages 2-4) |


*Table: This table links TP63 variant classes and domain-specific mechanisms to the main syndromic phenotypes, diagnostic workflows, and real-world interventions reported across the TP63-related ectodermal dysplasia spectrum. It is useful for connecting molecular interpretation to practical disease management.*

---

## 13. Prevention
No primary prevention exists for germline TP63 disorders; prevention focuses on:
- **Genetic counseling** and discussion of recurrence risk, especially given variable expressivity/incomplete penetrance (zhuang2025molecularcharacterizationof pages 1-2).
- **Prenatal diagnosis** is implicated as relevant in TP63 disorders (noted in reference discussion) (iorio2023…patientsaffected pages 14-14).
- **Secondary prevention** through early detection of high-morbidity complications (ocular surveillance; newborn immune screening when applicable) (iorio2023…patientsaffected pages 9-11, gall2024casereportartificial pages 2-3).

---

## 14. Other species / natural disease
No naturally occurring non-human TP63 ectodermal dysplasia disease models or veterinary reports were identified in the retrieved evidence set.

---

## 15. Model organisms
Key model systems and their relevance:
- **AEC skin fragility models (2023):** patient iPSC-derived keratinocytes with gene-corrected controls; chimeric mice expressing TP63-AEC transgene; recapitulate adhesion defects implicated in erosions (salois2023effectsoftp63 pages 3-4, salois2023effectsoftp63 pages 7-11).
- **POI models (2023):** p63+/ΔTID and p63+/R647C mice show rapid postnatal oocyte depletion/POI-like phenotype, supporting gain-of-function mechanism in oocytes (huang2023tp63gainoffunctionmutations pages 3-5, huang2023tp63gainoffunctionmutations pages 5-7).
- **Developmental limb model context:** p63−/− mice associated with reduced AER FGF signaling and limb defects (cited mechanistic context) (zhuang2025molecularcharacterizationof pages 6-8).
- **Ex vivo functional assay model (2024):** artificial thymic organoid assay to separate hematopoietic vs thymic stromal causes of T-cell lymphopenia (gall2024casereportartificial pages 2-3).

---

## Key statistics (from recent studies)
- **EEC prevalence:** ~**1–9 per 100,000 newborns** (Orpha.net quote in 2023 clinical series) (iorio2023…patientsaffected pages 9-11).
- **Primary ovarian insufficiency:** TP63 gain-of-function variants **“accounted for 0.78% (8 of 1,030) of the studied cases”** in a 2023 cohort; age of amenorrhea **13–29 years** (huang2023tp63gainoffunctionmutations pages 2-3).

---

## Notable 2023–2024 developments (prioritized)
1. **AEC mechanism clarified in human iPSC models:** coordinated downregulation of hemidesmosome/focal adhesion genes with functional adhesion/migration impairment, validated in vivo and in patient skin (Salois et al., 2023-07; https://doi.org/10.1111/exd.14885) (salois2023effectsoftp63 pages 3-4, salois2023effectsoftp63 media 83f76dc6).
2. **Newborn screening + genomics revealing immune phenotypes:** TP63 variants identified in newborns with low/undetectable TREC; one 2024 case used ATO assay to guide thymus tissue implantation (Gall et al., 2024-09; https://doi.org/10.3389/fimmu.2024.1438383) (gall2024casereportartificial pages 2-3).
3. **Large POI cohort genetics:** TP63 GOF variants quantitatively implicated in idiopathic POI with mechanistic mouse validation (Huang et al., 2023-03; https://doi.org/10.1172/jci162315) (huang2023tp63gainoffunctionmutations pages 2-3).

---

## Evidence limitations (for knowledge base curation)
- MONDO/ICD/MeSH identifiers and comprehensive epidemiology for non-EEC syndromes were not available in the retrieved full texts.
- Many phenotype frequencies (percent affected, penetrance estimates beyond specific pedigrees) are not quantified in the 2023–2024 sources retrieved.
- Some “expert synthesis” in this report relies on 2025–2026 reviews for domain-level framing and isoform biology; primary mechanistic and clinical claims are grounded in the 2023–2024 studies cited above (cong2026p63inskin pages 12-14, salois2023effectsoftp63 pages 3-4).


References

1. (cong2026p63inskin pages 12-14): Yujia Cong, Zhenglin He, Hanming Hao, Haoran Chen, Anqi Chen, Chunyi Li, Yue Hu, and Xianling Cong. P63 in skin homeostasis and disease: molecular mechanisms and therapeutic potentials. Cell Death Discovery, Mar 2026. URL: https://doi.org/10.1038/s41420-026-03060-8, doi:10.1038/s41420-026-03060-8. This article has 0 citations and is from a peer-reviewed journal.

2. (zhuang2025molecularcharacterizationof pages 1-2): Jianlong Zhuang, Yanqing Li, Yu’e Chen, Hegan Zhang, Shufen Liu, Manman Hu, and Chunnuan Chen. Molecular characterization of a rare tp63 variant associated with split-hand/split-foot malformation 4 and incomplete penetrance: disruption of the p63-dlx signaling pathway. BMC Genomics, Feb 2025. URL: https://doi.org/10.1186/s12864-025-11297-3, doi:10.1186/s12864-025-11297-3. This article has 0 citations and is from a peer-reviewed journal.

3. (salois2023effectsoftp63 pages 3-4): Maddison N. Salois, Jessica A. Gugger, Saiphone Webb, Christina E. Sheldon, Shirley P. Parraga, G. Michael Lewitt, Dorothy K. Grange, Peter J. Koch, and Maranke I. Koster. Effects of tp63 mutations on keratinocyte adhesion and migration. Experimental Dermatology, 32:1575-1581, Jul 2023. URL: https://doi.org/10.1111/exd.14885, doi:10.1111/exd.14885. This article has 5 citations and is from a domain leading peer-reviewed journal.

4. (gall2024casereportartificial pages 2-3): Alevtina Gall, Marita Bosticardo, Stacey Ma, Karin Chen, Kayla Amini, Francesca Pala, Ottavia M. Delmonte, Tara Wenger, Michael Bamshad, John Sleasman, Matthew Blessing, Nicolai S. C. van Oers, Luigi D. Notarangelo, and M. Teresa de la Morena. Case report: artificial thymic organoids facilitate clinical decisions for a patient with a tp63 variant and severe persistent t cell lymphopenia. Frontiers in Immunology, Sep 2024. URL: https://doi.org/10.3389/fimmu.2024.1438383, doi:10.3389/fimmu.2024.1438383. This article has 3 citations and is from a peer-reviewed journal.

5. (huang2023tp63gainoffunctionmutations pages 2-3): Chengzi Huang, Simin Zhao, Yajuan Yang, T. Guo, Hanni Ke, Xinling Mi, Yingying Qin, Zi-Jiang Chen, and Shidou Zhao. Tp63 gain-of-function mutations cause premature ovarian insufficiency by inducing oocyte apoptosis. The Journal of Clinical Investigation, Mar 2023. URL: https://doi.org/10.1172/jci162315, doi:10.1172/jci162315. This article has 38 citations.

6. (iorio2023…patientsaffected pages 9-11): E Di Iorio, F Bonelli, and R Bievel-Radulescu. … patients affected by p63-associated disorders: ectrodactyly-ectodermal dysplasia-clefting (eec) and ankyloblepharon-ectodermal defects-cleft lip palate (aec …. Unknown journal, 2023.

7. (ahuja2023ectrodactylyectodermaldysplasiaclefting pages 4-4): S Ahuja. Ectrodactyly-ectodermal dysplasia clefting syndrome-a rare case. Unknown journal, 2023.

8. (ahuja2023ectrodactylyectodermaldysplasiaclefting pages 2-4): S Ahuja. Ectrodactyly-ectodermal dysplasia clefting syndrome-a rare case. Unknown journal, 2023.

9. (cong2026p63inskin pages 14-16): Yujia Cong, Zhenglin He, Hanming Hao, Haoran Chen, Anqi Chen, Chunyi Li, Yue Hu, and Xianling Cong. P63 in skin homeostasis and disease: molecular mechanisms and therapeutic potentials. Cell Death Discovery, Mar 2026. URL: https://doi.org/10.1038/s41420-026-03060-8, doi:10.1038/s41420-026-03060-8. This article has 0 citations and is from a peer-reviewed journal.

10. (zhou2023casereportadult pages 2-4): Jichao Zhou, Yuchen Wang, Yinghong Zhang, Debo You, and Yi Wang. Case report: adult syndrome: a rare case of congenital lacrimal duct abnormality. Frontiers in Genetics, Oct 2023. URL: https://doi.org/10.3389/fgene.2023.1150613, doi:10.3389/fgene.2023.1150613. This article has 5 citations and is from a peer-reviewed journal.

11. (zhuang2025molecularcharacterizationof pages 9-10): Jianlong Zhuang, Yanqing Li, Yu’e Chen, Hegan Zhang, Shufen Liu, Manman Hu, and Chunnuan Chen. Molecular characterization of a rare tp63 variant associated with split-hand/split-foot malformation 4 and incomplete penetrance: disruption of the p63-dlx signaling pathway. BMC Genomics, Feb 2025. URL: https://doi.org/10.1186/s12864-025-11297-3, doi:10.1186/s12864-025-11297-3. This article has 0 citations and is from a peer-reviewed journal.

12. (цабаи2025нарушенияполовогоразвития pages 10-10): П.Н. Цабай, А.А. Докшукина, Евгения Александровна Шубина, З. Х. Кумыкова, З. К. Батырова, Т. О. Кочеткова, А. Ю. Гольцов, С. В. Юренева, and Д. Ю. Трофимов. Нарушения полового развития у девочек-подростков, вызванные вариантами в гене tp63: серия клинических случаев. Педиатрия. Восточная Европа, 13:647-656, Dec 2025. URL: https://doi.org/10.34883/pi.2025.13.4.011, doi:10.34883/pi.2025.13.4.011. This article has 0 citations.

13. (marakhonov2024ararecase pages 4-5): Andrey Marakhonov, Elena Serebryakova, Anna Mukhina, Anastasia Vechkasova, Nikolai Prokhorov, Irina Efimova, Natalia Balinova, Anastasia Lobenskaya, Tatyana Vasilyeva, Victoria Zabnenkova, Oxana Ryzhkova, Yulia Rodina, Dmitry Pershin, Nadezhda Soloveva, Anna Fomenko, Djamila Saydaeva, Aset Ibisheva, Taisiya Irbaieva, Alexander Koroteev, Rena Zinchenko, Sergey Voronin, Anna Shcherbina, and Sergey Kutsev. A rare case of tp63-associated lymphopenia revealed by newborn screening using trec. International Journal of Molecular Sciences, 25:10844, Oct 2024. URL: https://doi.org/10.3390/ijms251910844, doi:10.3390/ijms251910844. This article has 4 citations.

14. (murari2025p63amaster pages 4-6): Lakshana Sruthi Sadu Murari, Sam Kunkel, Anala Shetty, Addison Bents, Aayush Bhandary, and Juan Carlos Rivera-Mulia. P63: a master regulator at the crossroads between development, senescence, aging, and cancer. Cells, 14:43, Jan 2025. URL: https://doi.org/10.3390/cells14010043, doi:10.3390/cells14010043. This article has 5 citations.

15. (vanderschelden2023heterozygoustp63pathogenic pages 1-2): Rachel K Vanderschelden, Marta Rodriguez-Escriba, Serena H. Chan, Andrea J. Berman, Aleksandar Rajkovic, and Svetlana A. Yatsenko. Heterozygous tp63 pathogenic variants in isolated primary ovarian insufficiency. Journal of Assisted Reproduction and Genetics, 40:2211-2218, Jul 2023. URL: https://doi.org/10.1007/s10815-023-02886-w, doi:10.1007/s10815-023-02886-w. This article has 6 citations and is from a peer-reviewed journal.

16. (zhuang2025molecularcharacterizationof pages 4-6): Jianlong Zhuang, Yanqing Li, Yu’e Chen, Hegan Zhang, Shufen Liu, Manman Hu, and Chunnuan Chen. Molecular characterization of a rare tp63 variant associated with split-hand/split-foot malformation 4 and incomplete penetrance: disruption of the p63-dlx signaling pathway. BMC Genomics, Feb 2025. URL: https://doi.org/10.1186/s12864-025-11297-3, doi:10.1186/s12864-025-11297-3. This article has 0 citations and is from a peer-reviewed journal.

17. (salois2023effectsoftp63 pages 4-6): Maddison N. Salois, Jessica A. Gugger, Saiphone Webb, Christina E. Sheldon, Shirley P. Parraga, G. Michael Lewitt, Dorothy K. Grange, Peter J. Koch, and Maranke I. Koster. Effects of tp63 mutations on keratinocyte adhesion and migration. Experimental Dermatology, 32:1575-1581, Jul 2023. URL: https://doi.org/10.1111/exd.14885, doi:10.1111/exd.14885. This article has 5 citations and is from a domain leading peer-reviewed journal.

18. (iorio2023…patientsaffected pages 14-14): E Di Iorio, F Bonelli, and R Bievel-Radulescu. … patients affected by p63-associated disorders: ectrodactyly-ectodermal dysplasia-clefting (eec) and ankyloblepharon-ectodermal defects-cleft lip palate (aec …. Unknown journal, 2023.

19. (marakhonov2024ararecase pages 1-2): Andrey Marakhonov, Elena Serebryakova, Anna Mukhina, Anastasia Vechkasova, Nikolai Prokhorov, Irina Efimova, Natalia Balinova, Anastasia Lobenskaya, Tatyana Vasilyeva, Victoria Zabnenkova, Oxana Ryzhkova, Yulia Rodina, Dmitry Pershin, Nadezhda Soloveva, Anna Fomenko, Djamila Saydaeva, Aset Ibisheva, Taisiya Irbaieva, Alexander Koroteev, Rena Zinchenko, Sergey Voronin, Anna Shcherbina, and Sergey Kutsev. A rare case of tp63-associated lymphopenia revealed by newborn screening using trec. International Journal of Molecular Sciences, 25:10844, Oct 2024. URL: https://doi.org/10.3390/ijms251910844, doi:10.3390/ijms251910844. This article has 4 citations.

20. (marakhonov2024ararecase pages 10-10): Andrey Marakhonov, Elena Serebryakova, Anna Mukhina, Anastasia Vechkasova, Nikolai Prokhorov, Irina Efimova, Natalia Balinova, Anastasia Lobenskaya, Tatyana Vasilyeva, Victoria Zabnenkova, Oxana Ryzhkova, Yulia Rodina, Dmitry Pershin, Nadezhda Soloveva, Anna Fomenko, Djamila Saydaeva, Aset Ibisheva, Taisiya Irbaieva, Alexander Koroteev, Rena Zinchenko, Sergey Voronin, Anna Shcherbina, and Sergey Kutsev. A rare case of tp63-associated lymphopenia revealed by newborn screening using trec. International Journal of Molecular Sciences, 25:10844, Oct 2024. URL: https://doi.org/10.3390/ijms251910844, doi:10.3390/ijms251910844. This article has 4 citations.

21. (cong2026p63inskin pages 16-19): Yujia Cong, Zhenglin He, Hanming Hao, Haoran Chen, Anqi Chen, Chunyi Li, Yue Hu, and Xianling Cong. P63 in skin homeostasis and disease: molecular mechanisms and therapeutic potentials. Cell Death Discovery, Mar 2026. URL: https://doi.org/10.1038/s41420-026-03060-8, doi:10.1038/s41420-026-03060-8. This article has 0 citations and is from a peer-reviewed journal.

22. (zhuang2025molecularcharacterizationof pages 6-8): Jianlong Zhuang, Yanqing Li, Yu’e Chen, Hegan Zhang, Shufen Liu, Manman Hu, and Chunnuan Chen. Molecular characterization of a rare tp63 variant associated with split-hand/split-foot malformation 4 and incomplete penetrance: disruption of the p63-dlx signaling pathway. BMC Genomics, Feb 2025. URL: https://doi.org/10.1186/s12864-025-11297-3, doi:10.1186/s12864-025-11297-3. This article has 0 citations and is from a peer-reviewed journal.

23. (salois2023effectsoftp63 pages 7-11): Maddison N. Salois, Jessica A. Gugger, Saiphone Webb, Christina E. Sheldon, Shirley P. Parraga, G. Michael Lewitt, Dorothy K. Grange, Peter J. Koch, and Maranke I. Koster. Effects of tp63 mutations on keratinocyte adhesion and migration. Experimental Dermatology, 32:1575-1581, Jul 2023. URL: https://doi.org/10.1111/exd.14885, doi:10.1111/exd.14885. This article has 5 citations and is from a domain leading peer-reviewed journal.

24. (salois2023effectsoftp63 media 83f76dc6): Maddison N. Salois, Jessica A. Gugger, Saiphone Webb, Christina E. Sheldon, Shirley P. Parraga, G. Michael Lewitt, Dorothy K. Grange, Peter J. Koch, and Maranke I. Koster. Effects of tp63 mutations on keratinocyte adhesion and migration. Experimental Dermatology, 32:1575-1581, Jul 2023. URL: https://doi.org/10.1111/exd.14885, doi:10.1111/exd.14885. This article has 5 citations and is from a domain leading peer-reviewed journal.

25. (salois2023effectsoftp63 media e89fc6fc): Maddison N. Salois, Jessica A. Gugger, Saiphone Webb, Christina E. Sheldon, Shirley P. Parraga, G. Michael Lewitt, Dorothy K. Grange, Peter J. Koch, and Maranke I. Koster. Effects of tp63 mutations on keratinocyte adhesion and migration. Experimental Dermatology, 32:1575-1581, Jul 2023. URL: https://doi.org/10.1111/exd.14885, doi:10.1111/exd.14885. This article has 5 citations and is from a domain leading peer-reviewed journal.

26. (huang2023tp63gainoffunctionmutations pages 3-5): Chengzi Huang, Simin Zhao, Yajuan Yang, T. Guo, Hanni Ke, Xinling Mi, Yingying Qin, Zi-Jiang Chen, and Shidou Zhao. Tp63 gain-of-function mutations cause premature ovarian insufficiency by inducing oocyte apoptosis. The Journal of Clinical Investigation, Mar 2023. URL: https://doi.org/10.1172/jci162315, doi:10.1172/jci162315. This article has 38 citations.

27. (iorio2023…byp63associated pages 9-11): E Di Iorio, F Bonelli, and R Bievel-Radulescu. … by p63-associated disorders: ectrodactyly-ectodermal dysplasia-clefting (eec) and ankyloblepharon-ectodermal defects-cleft lip palate (aec) syndromes. Unknown journal, 2023.

28. (huang2023tp63gainoffunctionmutations pages 10-11): Chengzi Huang, Simin Zhao, Yajuan Yang, T. Guo, Hanni Ke, Xinling Mi, Yingying Qin, Zi-Jiang Chen, and Shidou Zhao. Tp63 gain-of-function mutations cause premature ovarian insufficiency by inducing oocyte apoptosis. The Journal of Clinical Investigation, Mar 2023. URL: https://doi.org/10.1172/jci162315, doi:10.1172/jci162315. This article has 38 citations.

29. (salois2023effectsoftp63 pages 1-3): Maddison N. Salois, Jessica A. Gugger, Saiphone Webb, Christina E. Sheldon, Shirley P. Parraga, G. Michael Lewitt, Dorothy K. Grange, Peter J. Koch, and Maranke I. Koster. Effects of tp63 mutations on keratinocyte adhesion and migration. Experimental Dermatology, 32:1575-1581, Jul 2023. URL: https://doi.org/10.1111/exd.14885, doi:10.1111/exd.14885. This article has 5 citations and is from a domain leading peer-reviewed journal.

30. (murari2025p63amaster pages 2-4): Lakshana Sruthi Sadu Murari, Sam Kunkel, Anala Shetty, Addison Bents, Aayush Bhandary, and Juan Carlos Rivera-Mulia. P63: a master regulator at the crossroads between development, senescence, aging, and cancer. Cells, 14:43, Jan 2025. URL: https://doi.org/10.3390/cells14010043, doi:10.3390/cells14010043. This article has 5 citations.

31. (huang2023tp63gainoffunctionmutations pages 5-7): Chengzi Huang, Simin Zhao, Yajuan Yang, T. Guo, Hanni Ke, Xinling Mi, Yingying Qin, Zi-Jiang Chen, and Shidou Zhao. Tp63 gain-of-function mutations cause premature ovarian insufficiency by inducing oocyte apoptosis. The Journal of Clinical Investigation, Mar 2023. URL: https://doi.org/10.1172/jci162315, doi:10.1172/jci162315. This article has 38 citations.