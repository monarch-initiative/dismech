---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-07T15:00:25.320450'
end_time: '2026-05-07T15:31:20.716749'
duration_seconds: 1855.4
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: familial hyperaldosteronism
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 41
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** familial hyperaldosteronism
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **familial hyperaldosteronism** covering all of the
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
- **Disease Name:** familial hyperaldosteronism
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **familial hyperaldosteronism** covering all of the
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


# Familial Hyperaldosteronism (FH): Comprehensive Disease Characteristics Report

## 1. Disease information

### Overview / definition
Familial hyperaldosteronism (FH) is a group of inherited (typically autosomal-dominant) forms of **primary aldosteronism (PA)** characterized by inappropriate aldosterone production, **suppressed renin**, and hypertension; hypokalemia may be present depending on subtype and severity. (okorafor2024lowreninforms pages 2-3, araujocastro2024differencesinthe pages 3-5)

A practical clinical definition used in recent endocrine genetics reviews is that FH is suspected/identified when a person has PA and **≥1 first-degree relative** is also affected. (kim2024molecularandgenetics pages 11-12)

### Key identifiers
- **MONDO (Mondo Disease Ontology)**
  - Familial hyperaldosteronism: **MONDO:0016525** (OpenTargets Search: familial hyperaldosteronism)
  - Familial hyperaldosteronism type II: **MONDO:0011576** (OpenTargets Search: familial hyperaldosteronism)
  - Familial hyperaldosteronism type III: **MONDO:0013359** (OpenTargets Search: familial hyperaldosteronism)
  - Hyperaldosteronism, familial, type IV: **MONDO:0014875** (OpenTargets Search: familial hyperaldosteronism)
  - Glucocorticoid-remediable aldosteronism (GRA; FH-I): **MONDO:0007080** (OpenTargets Search: familial hyperaldosteronism)
- **OMIM (disease identifiers)**
  - FH-I / GRA: **OMIM #103900** (carvajal2012anewpresentation pages 1-3, monticone2018geneticsinendocrinology pages 1-5)
  - FH-II: **OMIM #605635** (santana2022pathogenesisofprimary pages 2-4, khandelwal2022monogenicformsof pages 6-7)
  - FH-III and FH-IV OMIM numbers are listed as part of the “type II–IV” group in one review (**#613677, #617027**), but the subtype-to-OMIM mapping is not explicitly resolved in the provided excerpt; use OMIM primary records to confirm exact subtype mapping. (khandelwal2022monogenicformsof pages 6-7)

**ICD-10/ICD-11 and MeSH identifiers were not retrievable from the current tool-accessible corpus** and should be added from OMIM/Orphanet/MeSH lookups in a follow-on curation step.

### Synonyms / alternative names
- **FH-I**: glucocorticoid-remediable aldosteronism (GRA); glucocorticoid-suppressible hyperaldosteronism. (kim2024molecularandgenetics pages 11-12, ekman2024whatweknow pages 2-4)
- FH is often described under the umbrella of “familial primary aldosteronism” in clinical literature. (araujocastro2024differencesinthe pages 2-3)

### Evidence provenance
The information summarized here is derived from aggregated disease-level resources (guidelines, cohort studies, systematic reviews) and primary research studies (genetic discovery, registry cohorts, and a complication study in FH-I). (adler2025primaryaldosteronisman pages 5-6, araujocastro2024differencesinthe pages 3-5, mulatero2011prevalenceandcharacteristics pages 1-2, aldosteronism1998intracranialaneurysmand pages 1-2)

## 2. Etiology

### Disease causal factors (genetic)
FH comprises multiple genetic subtypes defined by germline alterations that increase aldosterone biosynthesis:
- **FH-I (GRA)**: CYP11B1/CYP11B2 **chimeric fusion gene** created by unequal/asymmetric crossover. (kim2024molecularandgenetics pages 11-12, ekman2024whatweknow pages 2-4)
- **FH-II**: germline **CLCN2** gain-of-function variants (chloride channel). (kim2024molecularandgenetics pages 11-12, okorafor2024lowreninforms pages 2-3)
- **FH-III**: germline **KCNJ5** variants affecting a potassium channel (Kir3.4/GIRK4). Primary evidence shows distinct phenotypes for different variants at the same residue (G151R vs G151E). (scholl2012hypertensionwithor pages 1-2)
- **FH-IV**: germline **CACNA1H** variants (T-type Ca2+ channel, CaV3.2); the original report identified heterozygous variants in familial and early-onset PA and demonstrated functional effects. (daniil2016cacna1hmutationsare pages 1-2)

OpenTargets disease–gene association evidence (supporting MONDO mapping) lists strong associations for KCNJ5, CLCN2, CACNA1H, CYP11B2/CYP11B1 (via GRA), and other linked entities. (OpenTargets Search: familial hyperaldosteronism)

### Risk factors
Primary risk is **family history** of PA/FH and **young onset** hypertension/PA. A 2025 Endocrine Society guideline emphasizes genetic screening for familial forms and young-onset PA (see Diagnostics). (adler2025primaryaldosteronisman pages 5-6)

### Protective factors / gene–environment interactions
Specific protective variants or gene–environment interactions were **not identified** in the retrieved corpus.

## 3. Phenotypes

### Core clinical phenotype
- **Hypertension** (often early onset in FH)
- **Low renin** phenotype (suppressed PRA/DRC)
- **Elevated aldosterone** (plasma aldosterone concentration; PAC)
- **Hypokalemia** (variable by subtype; not required for diagnosis) (okorafor2024lowreninforms pages 2-3, araujocastro2024differencesinthe pages 3-5)

### Subtype-specific phenotypic patterns and frequencies (quantitative)
A large 2024 comparative analysis compiled **360 FH cases** (systematic review) vs **830 sporadic PA** patients (SPAIN-ALDO registry). (araujocastro2024differencesinthe pages 3-5)

**FH-I (GRA)**
- Younger age at diagnosis: **33.6 ± 18.07 vs 56.5 ± 4.76 years** (FH-I vs sporadic). (araujocastro2024differencesinthe pages 3-5)
- Hypokalemia prevalence: **11.6% vs 59.6%** (FH-I vs sporadic). (araujocastro2024differencesinthe pages 3-5)
- PAC: **29.5 ± 15.03 vs 44.4 ± 78.85 ng/dL** (FH-I vs sporadic). (araujocastro2024differencesinthe pages 3-5)
- PRA: **1.3 ± 6.81 vs 0.4 ± 0.86 ng/mL/h** (FH-I vs sporadic). (araujocastro2024differencesinthe pages 3-5)
- A synthesis within the same paper notes many FH-I patients may be normotensive (reported ~40%) and hypokalemia can be <12%. (araujocastro2024differencesinthe pages 5-6)

**FH-II (CLCN2-related)**
- Phenotype often resembles sporadic PA except younger age and higher diastolic BP; in the same cohort, mean age is markedly younger than sporadic (example values reported for FH-II: **33.6 ± 19.7 vs 56.5 ± 4.8 years**). (araujocastro2024differencesinthe pages 5-6)

**FH-III (KCNJ5-related)**
- Severe early-onset phenotype with **hypokalemia ~89.3%** and mean serum potassium ~2.6 mEq/L in the cohort. (araujocastro2024differencesinthe pages 3-5)
- High need for bilateral adrenalectomy in severe cases: **17/29** underwent bilateral adrenalectomy for BP control in the 2024 synthesis. (araujocastro2024differencesinthe pages 3-5)

**FH-IV (CACNA1H-related)**
- In the 2024 synthesis, phenotype was largely similar to sporadic PA, but with younger age, lower serum potassium and higher PRA. (araujocastro2024differencesinthe pages 5-6, araujocastro2024differencesinthe pages 3-5)

### Major complication phenotype (FH-I/GRA)
A landmark 1998 study of 27 GRA pedigrees reported major cerebrovascular morbidity:
- In genetically proven GRA subjects (**n=167**), **18 cerebrovascular events** occurred in **15 patients** vs **0 events** in GRA-negative relatives (P<0.001). (aldosteronism1998intracranialaneurysmand pages 1-2)
- **70%** of events were hemorrhagic; overall case fatality **61%**. (aldosteronism1998intracranialaneurysmand pages 1-2)
- The authors conclude GRA “is associated with high morbidity and mortality from early onset of hemorrhage stroke and ruptured intracranial aneurysms” and recommend aneurysm screening by MRA in genetically proven GRA. (aldosteronism1998intracranialaneurysmand pages 1-2)
- Hemorrhagic stroke incidence rates in proven GRA were markedly higher than Framingham (Framingham **0.020%** vs proven GRA **0.28%** in patient-years comparisons). (aldosteronism1998intracranialaneurysmand pages 4-5)

### Suggested HPO terms (examples)
The retrieved sources did not supply explicit HPO mappings; suggested terms for knowledge-base curation:
- Hypertension: **HP:0000822**
- Hyperaldosteronism: **HP:0000859**
- Hypokalemia: **HP:0002900**
- Low renin (as a lab phenotype; may map to “decreased renin”): **HP:0020031** (check exact HPO label in current HPO)
- Metabolic alkalosis: **HP:0001948** (not universal; more typical in mineralocorticoid excess syndromes) (okorafor2024lowreninforms pages 2-3)
- Intracranial aneurysm: **HP:0004944**; Hemorrhagic stroke: **HP:0001342** (FH-I/GRA complication) (aldosteronism1998intracranialaneurysmand pages 1-2)

### Quality-of-life impact
No FH-specific validated QoL instruments or quantified QoL outcomes were identified in the retrieved corpus.

## 4. Genetic / molecular information

### Causal genes by subtype
See subtype summary table below and genetic discovery evidence:
- FH-I: CYP11B1/CYP11B2 chimeric fusion (OMIM #103900). (carvajal2012anewpresentation pages 1-3)
- FH-II: CLCN2. (kim2024molecularandgenetics pages 11-12, okorafor2024lowreninforms pages 2-3)
- FH-III: KCNJ5. (scholl2012hypertensionwithor pages 1-2)
- FH-IV: CACNA1H. (daniil2016cacna1hmutationsare pages 1-2)

### Pathogenic variant examples (from tool-accessible sources)
- FH-II / CLCN2 examples listed in 2024 review: **p.Arg172Gln, p.Met22Lys, p.Tyr26Asn, p.Lys362del, p.Ser865Arg**. (kim2024molecularandgenetics pages 11-12)
- FH-III / KCNJ5: primary evidence identifies inherited **G151R** (severe phenotype) and **G151E** (milder) segregating with disease. (scholl2012hypertensionwithor pages 1-2)
- FH-IV / CACNA1H: heterozygous germline variants reported, including **p.Met1549Ile** (de novo in early-onset PA) and other variants in familial cases; functional studies demonstrate altered Ca2+ currents and increased aldosterone output in cell models. (daniil2016cacna1hmutationsare pages 1-2)

### Somatic vs germline
FH is defined by **germline** changes, but there is mechanistic overlap with **somatic** driver mutations in sporadic aldosterone-producing adenomas (APAs) (e.g., KCNJ5, CACNA1D), which converge on Ca2+ signaling and CYP11B2 upregulation. (ekman2024whatweknow pages 2-4, kim2024molecularandgenetics pages 11-12)

### Modifier genes / epigenetics / chromosomal abnormalities
No FH-specific modifier genes, epigenetic signatures, or chromosomal abnormalities were identified in the retrieved corpus.

## 5. Environmental information
No specific non-genetic environmental triggers for FH onset were identified; however, aldosterone excess phenotypes interact with salt intake and antihypertensive medications via ARR interpretation and downstream cardiovascular risk (primarily addressed in PA guidelines rather than FH-specific evidence). (adler2025primaryaldosteronisman pages 5-6, ylanenUnknownyeardiagnosticsofprimary pages 49-52)

## 6. Mechanism / pathophysiology

### Common mechanistic theme
Across most FH subtypes, causal variants affect **ion channels or transport** in adrenal zona glomerulosa (ZG) cells, leading to **membrane depolarization**, increased intracellular **Ca2+ signaling**, increased **CYP11B2 (aldosterone synthase)** expression, and aldosterone overproduction. (ekman2024whatweknow pages 2-4, kim2024molecularandgenetics pages 11-12)

### FH-I (GRA): ACTH-dependent aldosterone synthase misexpression
A CYP11B1/CYP11B2 chimeric gene results in aldosterone synthase activity being controlled by **ACTH** rather than angiotensin II/potassium, explaining dexamethasone suppressibility. (ekman2024whatweknow pages 2-4, kim2024molecularandgenetics pages 11-12)

### FH-II (CLCN2): chloride conductance → depolarization → Ca2+ influx
A 2024 review summarizes FH-II mechanism as a mutant chloride channel with increased permeability that causes depolarization and “influx of calcium intracellularly, resulting in the activation of aldosterone synthesis.” (okorafor2024lowreninforms pages 2-3)

### FH-III (KCNJ5): loss of K+ selectivity → Na+ influx → depolarization
Primary evidence shows KCNJ5 mutations disrupt the selectivity filter so channels conduct Na+, leading to depolarization and Ca2+ channel activation, which increases aldosterone production and can drive hyperplasia; phenotype differs by allele (G151R severe vs G151E mild). (scholl2012hypertensionwithor pages 1-2)

### FH-IV (CACNA1H): CaV3.2 gain-of-function → altered Ca2+ currents
CACNA1H variants alter Ca2+ current properties in electrophysiology studies and increase aldosterone production and steroidogenic enzyme expression in cell models, supporting a calcium-driven aldosteronism mechanism. (daniil2016cacna1hmutationsare pages 1-2)

### Proposed mechanisms for cerebrovascular aneurysm risk in GRA
The 1998 GRA complication study proposes multiple plausible contributors, including longstanding congenital hypertension, aldosterone-related vascular remodeling/fibrosis, or developmental effects of mineralocorticoid excess on cerebrovascular development; it draws a parallel to intracranial aneurysm risk in autosomal dominant polycystic kidney disease. (aldosteronism1998intracranialaneurysmand pages 4-5)

### Suggested ontology mappings (examples)
- **GO Biological Process**: aldosterone biosynthetic process (GO:0006694); regulation of membrane depolarization (various); cellular calcium ion homeostasis (GO:0006874); response to ACTH (mapped via melanocortin signaling; not explicitly in excerpts). (ekman2024whatweknow pages 2-4, scholl2012hypertensionwithor pages 1-2)
- **Cell type (CL)**: adrenal gland zona glomerulosa cell (CL term; exact CL ID to be verified during ontology curation). (ekman2024whatweknow pages 2-4, okorafor2024lowreninforms pages 2-3)

## 7. Anatomical structures affected

### Primary organs
- **Adrenal cortex**, especially **zona glomerulosa** (aldosterone production) and, in FH-I/GRA, aberrant aldosterone synthase expression in zona fasciculata is a key concept. (okorafor2024lowreninforms pages 2-3, monticone2018geneticsinendocrinology pages 1-5)

### Secondary organ involvement / complications
- Cardiovascular system and cerebrovasculature via sustained aldosterone excess and hypertension; notably intracranial aneurysm and hemorrhagic stroke in FH-I/GRA. (aldosteronism1998intracranialaneurysmand pages 1-2)

### Suggested UBERON terms (examples)
- Adrenal gland: UBERON:0002369
- Adrenal cortex: UBERON:0001234
- Zona glomerulosa: UBERON term to be verified in ontology curation

## 8. Temporal development
- FH often presents as **young-onset** hypertension/PA, especially FH-I and FH-III; FH-III can present in infancy/early childhood in some summaries. (okorafor2024lowreninforms pages 2-3, araujocastro2024differencesinthe pages 3-5)
- FH-I/GRA cerebrovascular events occur early (mean age at first event ~31.7 years in the 1998 study). (aldosteronism1998intracranialaneurysmand pages 1-2)

## 9. Inheritance and population

### Inheritance
FH subtypes are generally described as **autosomal dominant** with variable expressivity; FH-II and FH-IV are often noted to have **incomplete penetrance** in reviews. (okorafor2024lowreninforms pages 2-3, santana2022pathogenesisofprimary pages 4-5)

### Epidemiology
- PA prevalence varies by setting and phenotype; 2025 Endocrine Society guideline estimates include:
  - **Primary care hypertensives:** ~**5.9%** (range 3.2–14.0%)
  - **Referral-center hypertensives:** **7.2%** (0.7–21.9%)
  - **Young-onset hypertension (18–40):** **16.2%**
  - **Resistant hypertension:** **11.3–29.1%**
  - **Hypertension + hypokalemia:** **28.1%** (adler2025primaryaldosteronisman pages 10-10)
- PATOGEN (300 consecutive PA patients) found:
  - **FH-I/GRA prevalence 0.66%** among PA (2 index cases) plus 21 affected relatives found by cascade screening.
  - **FH-II** in **12 of 199 informative families (6%)** plus 15 additional relatives with confirmed PA. (mulatero2011prevalenceandcharacteristics pages 1-2)

### Demographics / geography / founder effects
Founder mutations, geographic clustering, and carrier frequencies were not extractable from the current corpus.

## 10. Diagnostics

### Biochemical screening for PA (relevant for FH case finding)
The 2025 Endocrine Society guideline emphasizes screening using **aldosterone, renin (PRA or DRC), and potassium**, with ARR interpretation in the context of pretest probability and medication effects; it provides guidance on repeating testing and medication washout where feasible. (adler2025primaryaldosteronisman pages 5-6)

### Confirmatory testing and subtyping
The 2025 guideline describes an individualized algorithm: patients likely to have PA who do not desire surgery can be treated with MRA without extensive confirmatory/subtyping; those pursuing surgery may proceed via probabilistic shared decision-making and consider aldosterone suppression testing, CT imaging, and AVS depending on likelihood of lateralizing disease. (adler2025primaryaldosteronisman pages 6-7)

Figure: Endocrine Society 2025 algorithm for likely PA management (includes pathways to MRA therapy vs CT/AVS workup). (adler2025primaryaldosteronisman media 47196b32)

### FH-specific genetic testing (guideline-based)
The 2025 Endocrine Society guideline states:
- “Aldosterone suppression testing is unnecessary in individuals from families with germline mutations associated with familial hyperaldosteronism.” (adler2025primaryaldosteronisman pages 5-6)
- “Genetic screening is recommended for all first-degree relatives of individuals with familial hyperaldosteronism and for individuals with young-onset PA (<20 years) to enable early diagnosis and treatment.” (adler2025primaryaldosteronisman pages 5-6)

Real-world implementation considerations: In Aotearoa/New Zealand, FH-I testing cost (NZD$127.91) was far lower than AVS (NZD$6663), supporting cost-effectiveness of early FH-I testing in young-onset PA without adrenal adenoma on imaging. (elston2024genetictestingfor pages 5-6)

### Differential diagnosis
The corpus included broader reviews of monogenic low-renin hypertension syndromes, emphasizing that multiple Mendelian disorders can present with low renin and hypertension (e.g., Liddle, apparent mineralocorticoid excess). FH is differentiated by aldosterone excess and genetic subtype testing. (okorafor2024lowreninforms pages 2-3)

## 11. Outcome / prognosis

### FH-I/GRA cerebrovascular prognosis
The 1998 pedigree study reported high morbidity and mortality:
- **18%** of genetically proven GRA patients had cerebrovascular complications.
- **61%** case fatality across events.
- Strong enrichment for hemorrhagic stroke and intracranial aneurysm. (aldosteronism1998intracranialaneurysmand pages 1-2)

### FH-II outcomes (PATOGEN)
FH-II families had clinically relevant complications: the cohort reported **stroke (3 patients)** and severe kidney damage in one patient among FH-II affected individuals (descriptive). (mulatero2011prevalenceandcharacteristics pages 3-4)

## 12. Treatment

### Pharmacotherapy
- **FH-I/GRA:** low-dose **glucocorticoids** (e.g., dexamethasone/prednisolone) to suppress ACTH-driven aldosterone; adjunct **mineralocorticoid receptor antagonists (MRAs)** such as spironolactone/eplerenone and ENaC blockers may be used for BP control. (okorafor2024lowreninforms pages 2-3)
- **FH (general) / PA targeted therapy:** Endocrine Society guideline emphasizes that PA-specific therapies are **MRAs** and (when appropriate) **unilateral adrenalectomy** for lateralizing disease. (adler2025primaryaldosteronisman pages 15-16)

### Surgical
- Severe FH-III frequently requires **bilateral adrenalectomy** for control (e.g., 17/29 in one synthesis). (araujocastro2024differencesinthe pages 3-5)

### Treatment outcomes
PATOGEN reports that very low-dose dexamethasone and/or MRAs controlled BP satisfactorily in FH-I families; FH-II cases more often had hypertension and higher complication burden. (mulatero2011prevalenceandcharacteristics pages 3-4)

### Suggested MAXO terms (examples)
- Mineralocorticoid receptor antagonist therapy (MAXO term to be verified)
- Glucocorticoid therapy (MAXO term to be verified)
- Adrenalectomy (MAXO term to be verified)

## 13. Prevention
Primary prevention is not applicable (genetic). Secondary/tertiary prevention focuses on:
- **Cascade genetic screening** of relatives per 2025 Endocrine Society guideline to enable early diagnosis and treatment. (adler2025primaryaldosteronisman pages 5-6)
- In FH-I/GRA, **intracranial aneurysm screening by MRA** in genetically proven cases is recommended in the 1998 study (beginning at puberty and repeated approximately every five years per the paper’s recommendations). (aldosteronism1998intracranialaneurysmand pages 4-5, aldosteronism1998intracranialaneurysmand pages 1-2)

## 14. Other species / natural disease
No naturally occurring FH analogs in non-human species were identified in the retrieved corpus.

## 15. Model organisms
FH subtype-relevant models were not systematically retrieved, but mechanistic animal/cellular models exist for channelopathies and are referenced in broader PA genetics literature; specific model details require additional targeted retrieval beyond the present corpus.

---

## Summary table of FH subtypes

| FH subtype | Alternative names / synonyms | Causal gene(s) and variant mechanism | Inheritance / penetrance | Key distinguishing clinical / biochemical features | Key citations (year) |
|---|---|---|---|---|---|
| **FH-I** | Glucocorticoid-remediable aldosteronism (GRA); glucocorticoid-suppressible hyperaldosteronism | **CYP11B1/CYP11B2 chimeric fusion gene** from unequal/asymmetric crossover; ACTH-regulated aldosterone synthase expression; functional **gain-of-function** of aldosterone production in zona fasciculata and glomerulosa (kim2024molecularandgenetics pages 11-12, ekman2024whatweknow pages 2-4, okorafor2024lowreninforms pages 2-3) | **Autosomal dominant**; marked **variable expressivity/phenotypic heterogeneity**; some affected individuals may be normotensive (okorafor2024lowreninforms pages 2-3, mulatero2011prevalenceandcharacteristics pages 1-2, monticone2018geneticsinendocrinology pages 1-5) | Earlier onset; often younger than sporadic PA; more common in women; **lower PAC**, **higher PRA**, **less frequent hypokalemia** than sporadic PA; hypokalemia reported in **<12%** in one synthesis and **40.3% may be normotensive** in one cohort; **ACTH-dependent** and **dexamethasone suppressible**; dexamethasone suppression / long-PCR useful diagnostically (araujocastro2024differencesinthe pages 2-3, araujocastro2024differencesinthe pages 5-6, kim2024molecularandgenetics pages 11-12, santana2022pathogenesisofprimary pages 2-4, adler2025primaryaldosteronisman pages 5-6) | Araujo-Castro *et al.* 2024, DOI:10.3389/fendo.2024.1336306; Kim *et al.* 2024, DOI:10.3390/ijms252111341; Ekman *et al.* 2024, DOI:10.3390/ijms25020900; PATOGEN 2011, DOI:10.1161/HYPERTENSIONAHA.111.175083; Endocrine Society guideline 2025, DOI:10.1210/clinem/dgaf284 (araujocastro2024differencesinthe pages 2-3, kim2024molecularandgenetics pages 11-12, ekman2024whatweknow pages 2-4, mulatero2011prevalenceandcharacteristics pages 1-2, adler2025primaryaldosteronisman pages 5-6) |
| **FH-II** | Familial hyperaldosteronism type II; nonglucocorticoid-remediable familial hyperaldosteronism | **CLCN2** (ClC-2 chloride channel) **gain-of-function** variants causing increased chloride permeability/efflux, depolarization, calcium influx, and aldosterone synthesis; variant examples include **p.Arg172Gln, p.Met22Lys, p.Tyr26Asn, p.Lys362del, p.Ser865Arg**, and **p.Gly24Asp** (kim2024molecularandgenetics pages 11-12, okorafor2024lowreninforms pages 2-3, santana2022pathogenesisofprimary pages 4-5) | Usually **autosomal dominant** with **incomplete penetrance** and variable expressivity (okorafor2024lowreninforms pages 2-3, santana2022pathogenesisofprimary pages 2-4) | Clinical and hormonal profile often **similar to sporadic PA**; younger age at presentation and somewhat higher diastolic BP in one cohort; PRA may be slightly higher than sporadic PA; not dexamethasone-remediable (araujocastro2024differencesinthe pages 2-3, araujocastro2024differencesinthe pages 5-6, kim2024molecularandgenetics pages 11-12) | Araujo-Castro *et al.* 2024, DOI:10.3389/fendo.2024.1336306; Kim *et al.* 2024, DOI:10.3390/ijms252111341; Okorafor 2024, DOI:10.23950/jcmk/14269; Santana 2022, DOI:10.3389/fendo.2022.927669 (araujocastro2024differencesinthe pages 2-3, kim2024molecularandgenetics pages 11-12, okorafor2024lowreninforms pages 2-3, santana2022pathogenesisofprimary pages 2-4, santana2022pathogenesisofprimary pages 4-5) |
| **FH-III** | Familial hyperaldosteronism type III | **KCNJ5** (GIRK4 / Kir3.4 potassium channel) germline variants causing loss of K+ selectivity, abnormal Na+ influx, membrane depolarization, and increased intracellular Ca2+; examples include **p.Gly151Arg, p.Gly151Glu, p.Tyr152Cys, p.Ile157Ser, p.Thr158Ala**; mechanism is pathogenic **gain-of-function for aldosterone production** (kim2024molecularandgenetics pages 11-12, ekman2024whatweknow pages 2-4, scholl2012hypertensionwithor pages 1-2, santana2022pathogenesisofprimary pages 4-5) | **Autosomal dominant**; marked **genotype-phenotype variability**; some variants cause massive hyperplasia and severe childhood disease, others milder controllable hypertension (scholl2012hypertensionwithor pages 1-2, santana2022pathogenesisofprimary pages 4-5) | Most severe classic FH subtype: **very early onset** (often infancy/childhood), **marked aldosterone excess**, **high PAC**, **low PRA**, **hypokalemia >85% / nearing 90%**, extensive adrenocortical hyperplasia, hybrid steroid synthesis; over **60% required bilateral adrenalectomy** in one synthesis; many cases resistant to pharmacotherapy (araujocastro2024differencesinthe pages 5-6, araujocastro2024differencesinthe pages 3-5, okorafor2024lowreninforms pages 2-3, scholl2012hypertensionwithor pages 1-2) | Scholl *et al.* 2012 PNAS, DOI:10.1073/pnas.1121407109; Araujo-Castro *et al.* 2024, DOI:10.3389/fendo.2024.1336306; Ekman *et al.* 2024, DOI:10.3390/ijms25020900; Santana 2022, DOI:10.3389/fendo.2022.927669 (scholl2012hypertensionwithor pages 1-2, araujocastro2024differencesinthe pages 2-3, araujocastro2024differencesinthe pages 5-6, ekman2024whatweknow pages 2-4, santana2022pathogenesisofprimary pages 4-5) |
| **FH-IV** | Familial hyperaldosteronism type IV | **CACNA1H** (CaV3.2 T-type calcium channel) germline **gain-of-function** variants increasing calcium influx and aldosterone biosynthesis; recurrent example **p.Met1549Val / p.Met1549Ile** and other heterozygous variants reported (okorafor2024lowreninforms pages 2-3, ekman2024whatweknow pages 2-4, daniil2016cacna1hmutationsare pages 1-2, santana2022pathogenesisofprimary pages 4-5) | **Autosomal dominant**; **incomplete / late penetrance** with variable expressivity (okorafor2024lowreninforms pages 2-3, santana2022pathogenesisofprimary pages 2-4, santana2022pathogenesisofprimary pages 4-5) | Often **early-onset hypertension**, but phenotype in 2024 comparative cohort was otherwise **similar to sporadic PA**, with younger age and lower serum potassium; not dexamethasone-remediable; no specific targeted therapy established in cited reviews (araujocastro2024differencesinthe pages 2-3, araujocastro2024differencesinthe pages 5-6, okorafor2024lowreninforms pages 2-3, daniil2016cacna1hmutationsare pages 1-2) | Daniil *et al.* 2016, DOI:10.1016/j.ebiom.2016.10.002; Araujo-Castro *et al.* 2024, DOI:10.3389/fendo.2024.1336306; Ekman *et al.* 2024, DOI:10.3390/ijms25020900; Santana 2022, DOI:10.3389/fendo.2022.927669 (daniil2016cacna1hmutationsare pages 1-2, araujocastro2024differencesinthe pages 2-3, ekman2024whatweknow pages 2-4, santana2022pathogenesisofprimary pages 4-5) |


*Table: This table summarizes the currently recognized Familial Hyperaldosteronism subtypes FH-I through FH-IV, including synonyms, causal genes and mechanisms, inheritance patterns, and distinguishing clinical features. It is useful for quickly comparing subtype-specific genetics and phenotype patterns using only the cited context sources.*

---

## Recent developments (prioritizing 2023–2025)

1. **2025 Endocrine Society PA guideline**: moves toward broader screening and explicitly recommends genetic screening of **all first-degree relatives** of FH cases and those with **young-onset PA (<20 years)**; also supports streamlined pathways where empirical MRA therapy can be initiated without extensive confirmatory testing in appropriate contexts. Publication date: July 2025. URL: https://doi.org/10.1210/clinem/dgaf284 (adler2025primaryaldosteronisman pages 5-6, adler2025primaryaldosteronisman pages 6-7)

2. **2024 phenotype synthesis (familial vs sporadic PA)**: largest compiled comparison in the retrieved corpus (360 FH cases) quantifies subtype-specific differences (e.g., very low hypokalemia in FH-I vs extreme hypokalemia and early onset in FH-III). Publication date: March 2024. URL: https://doi.org/10.3389/fendo.2024.1336306 (araujocastro2024differencesinthe pages 3-5)

3. **2024 real-world implementation work (New Zealand)**: highlights practical cost advantages of FH-I genetic testing compared with AVS and ethical/insurance considerations for testing. Publication date: Aug 2024. URL: https://doi.org/10.1111/imj.16511 (elston2024genetictestingfor pages 5-6)

4. **Large-scale implementation gap quantified (Taiwan, 7.8 million hypertensives)**: only **4.4%** ever screened for PA, despite high-risk features; annual screening only **0.75%** by 2022. Preprint date: Nov 2025. URL: https://doi.org/10.1101/2025.11.13.25340212 (tsai2025screeninganddiagnosis pages 1-6)

---

## Limitations / gaps relative to template
- ICD-10/ICD-11 and MeSH identifiers, Orphanet codes, population carrier frequencies, founder effects, and FH-specific QoL metrics were not present in the retrieved corpus and should be added via dedicated OMIM/Orphanet/MeSH lookups and/or additional targeted literature retrieval.
- Some 2023–2024 FH-specific systematic reviews were listed as unobtainable by the tool (e.g., 2024 EJE FH guideline; 2023 therapeutic systematic review), so their details could not be incorporated here.


References

1. (okorafor2024lowreninforms pages 2-3): Ugochi Chinenye Okorafor and Uchechi Chioma Okorafor. Low renin forms of monogenic hypertension: review of the evidence. Journal of Clinical Medicine of Kazakhstan, 21:14-20, Feb 2024. URL: https://doi.org/10.23950/jcmk/14269, doi:10.23950/jcmk/14269. This article has 0 citations.

2. (araujocastro2024differencesinthe pages 3-5): Marta Araujo-Castro, Paola Parra, Patricia Martín Rojas-Marcos, Miguel Paja Fano, Marga González Boillos, Eider Pascual-Corrales, Ana María García Cano, Jorge Gabriel Ruiz-Sanchez, Almudena Vicente Delgado, Emilia Gómez Hoyos, Rui Ferreira, Iñigo García Sanz, Mònica Recasens Sala, Rebeca Barahona San Millan, María José Picón César, Patricia Díaz Guardiola, Carolina M. Perdomo, Laura Manjón-Miguélez, Rogelio García Centeno, Ángel Rebollo Román, Paola Gracia Gimeno, Cristina Robles Lázaro, Manuel Morales-Ruiz, María Calatayud, Simone Andree Furio Collao, Diego Meneses, Miguel Sampedro Nuñez, Verónica Escudero Quesada, Elena Mena Ribas, Alicia Sanmartín Sánchez, Cesar Gonzalvo Diaz, Cristina Lamas, María del Castillo Tous, Joaquín Serrano Gotarredona, Theodora Michalopoulou Alevras, Eva María Moya Mateo, and Felicia A. Hanzu. Differences in the clinical and hormonal presentation of patients with familial and sporadic primary aldosteronism. Frontiers in Endocrinology, Mar 2024. URL: https://doi.org/10.3389/fendo.2024.1336306, doi:10.3389/fendo.2024.1336306. This article has 6 citations.

3. (kim2024molecularandgenetics pages 11-12): Sanggu Kim, Preeti Kumari Chaudhary, and Soochong Kim. Molecular and genetics perspectives on primary adrenocortical hyperfunction disorders. International Journal of Molecular Sciences, 25:11341, Oct 2024. URL: https://doi.org/10.3390/ijms252111341, doi:10.3390/ijms252111341. This article has 6 citations.

4. (OpenTargets Search: familial hyperaldosteronism): Open Targets Query (familial hyperaldosteronism, 15 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

5. (carvajal2012anewpresentation pages 1-3): Cristian A. Carvajal, Carmen Campino, Alejandro Martinez-Aguayo, Juan E. Tichauer, Rodrigo Bancalari, Carolina Valdivia, Pamela Trejo, Marlene Aglony, René Baudrand, Carlos F. Lagos, Cecilia Mellado, Hernán Garcia, and Carlos E. Fardella. A new presentation of the chimeric cyp11b1/cyp11b2 gene with low prevalence of primary aldosteronism and atypical gene segregation pattern. Hypertension, 59:85–91, Jan 2012. URL: https://doi.org/10.1161/hypertensionaha.111.180513, doi:10.1161/hypertensionaha.111.180513. This article has 36 citations and is from a domain leading peer-reviewed journal.

6. (monticone2018geneticsinendocrinology pages 1-5): Silvia Monticone, Fabrizio Buffolo, Martina Tetti, Franco Veglio, Barbara Pasini, and Paolo Mulatero. Genetics in endocrinology: the expanding genetic horizon of primary aldosteronism. European journal of endocrinology, 178 3:R101-R111, Mar 2018. URL: https://doi.org/10.1530/eje-17-0946, doi:10.1530/eje-17-0946. This article has 66 citations and is from a highest quality peer-reviewed journal.

7. (santana2022pathogenesisofprimary pages 2-4): Lucas S. Santana, Augusto G. Guimaraes, and Madson Q. Almeida. Pathogenesis of primary aldosteronism: impact on clinical outcome. Frontiers in Endocrinology, Jun 2022. URL: https://doi.org/10.3389/fendo.2022.927669, doi:10.3389/fendo.2022.927669. This article has 23 citations.

8. (khandelwal2022monogenicformsof pages 6-7): Priyanka Khandelwal and Jaap Deinum. Monogenic forms of low-renin hypertension: clinical and molecular insights. Pediatric Nephrology, 37:1495-1509, Aug 2022. URL: https://doi.org/10.1007/s00467-021-05246-x, doi:10.1007/s00467-021-05246-x. This article has 30 citations and is from a domain leading peer-reviewed journal.

9. (ekman2024whatweknow pages 2-4): Natalia Ekman, Ashley B. Grossman, and Dorota Dworakowska. What we know about and what is new in primary aldosteronism. International Journal of Molecular Sciences, 25:900, Jan 2024. URL: https://doi.org/10.3390/ijms25020900, doi:10.3390/ijms25020900. This article has 21 citations.

10. (araujocastro2024differencesinthe pages 2-3): Marta Araujo-Castro, Paola Parra, Patricia Martín Rojas-Marcos, Miguel Paja Fano, Marga González Boillos, Eider Pascual-Corrales, Ana María García Cano, Jorge Gabriel Ruiz-Sanchez, Almudena Vicente Delgado, Emilia Gómez Hoyos, Rui Ferreira, Iñigo García Sanz, Mònica Recasens Sala, Rebeca Barahona San Millan, María José Picón César, Patricia Díaz Guardiola, Carolina M. Perdomo, Laura Manjón-Miguélez, Rogelio García Centeno, Ángel Rebollo Román, Paola Gracia Gimeno, Cristina Robles Lázaro, Manuel Morales-Ruiz, María Calatayud, Simone Andree Furio Collao, Diego Meneses, Miguel Sampedro Nuñez, Verónica Escudero Quesada, Elena Mena Ribas, Alicia Sanmartín Sánchez, Cesar Gonzalvo Diaz, Cristina Lamas, María del Castillo Tous, Joaquín Serrano Gotarredona, Theodora Michalopoulou Alevras, Eva María Moya Mateo, and Felicia A. Hanzu. Differences in the clinical and hormonal presentation of patients with familial and sporadic primary aldosteronism. Frontiers in Endocrinology, Mar 2024. URL: https://doi.org/10.3389/fendo.2024.1336306, doi:10.3389/fendo.2024.1336306. This article has 6 citations.

11. (adler2025primaryaldosteronisman pages 5-6): Gail K Adler, Michael Stowasser, Ricardo R Correa, Nadia Khan, Gregory Kline, Michael J McGowan, Paolo Mulatero, M Hassan Murad, Rhian M Touyz, Anand Vaidya, Tracy A Williams, Jun Yang, William F Young, Maria-Christina Zennaro, and Juan P Brito. Primary aldosteronism: an endocrine society clinical practice guideline. The Journal of clinical endocrinology and metabolism, Jul 2025. URL: https://doi.org/10.1210/clinem/dgaf284, doi:10.1210/clinem/dgaf284. This article has 211 citations.

12. (mulatero2011prevalenceandcharacteristics pages 1-2): Paolo Mulatero, Davide Tizzani, Andrea Viola, Chiara Bertello, Silvia Monticone, Giulio Mengozzi, Domenica Schiavone, Tracy Ann Williams, Silvia Einaudi, Antonio La Grotta, Franco Rabbia, and Franco Veglio. Prevalence and characteristics of familial hyperaldosteronism: the patogen study (primary aldosteronism in torino-genetic forms). Hypertension, 58:797–803, Nov 2011. URL: https://doi.org/10.1161/hypertensionaha.111.175083, doi:10.1161/hypertensionaha.111.175083. This article has 189 citations and is from a domain leading peer-reviewed journal.

13. (aldosteronism1998intracranialaneurysmand pages 1-2): W. Aldosteronism, Reid, Lltchfield, Bruce, F. Anderson, Ruedlger, J. Weiss, Richard, P. Llfton, Robert, and Dluhy. Intracranial aneurysm and hemorrhagic stroke in glucocorticoid-remediable aldosteronism. Hypertension, 31 1 Pt 2:445-50, Jan 1998. URL: https://doi.org/10.1161/01.hyp.31.1.445, doi:10.1161/01.hyp.31.1.445. This article has 242 citations and is from a domain leading peer-reviewed journal.

14. (scholl2012hypertensionwithor pages 1-2): Ute I. Scholl, Carol Nelson-Williams, Peng Yue, Roger Grekin, Robert J. Wyatt, Michael J. Dillon, Robert Couch, Lisa K. Hammer, Frances L. Harley, Anita Farhi, Wen-Hui Wang, and Richard P. Lifton. Hypertension with or without adrenal hyperplasia due to different inherited mutations in the potassium channel kcnj5. Proceedings of the National Academy of Sciences, 109:2533-2538, Jan 2012. URL: https://doi.org/10.1073/pnas.1121407109, doi:10.1073/pnas.1121407109. This article has 304 citations and is from a highest quality peer-reviewed journal.

15. (daniil2016cacna1hmutationsare pages 1-2): Georgios Daniil, Fabio L Fernandes-Rosa, Jean Chemin, Iulia Blesneac, Jacques Beltrand, Michel Polak, Xavier Jeunemaitre, Sheerazed Boulkroun, Laurence Amar, Tim M Strom, Philippe Lory, and Maria-Christina Zennaro. Cacna1h mutations are associated with different forms of primary aldosteronism. EBioMedicine, 13:225-236, Nov 2016. URL: https://doi.org/10.1016/j.ebiom.2016.10.002, doi:10.1016/j.ebiom.2016.10.002. This article has 173 citations and is from a peer-reviewed journal.

16. (araujocastro2024differencesinthe pages 5-6): Marta Araujo-Castro, Paola Parra, Patricia Martín Rojas-Marcos, Miguel Paja Fano, Marga González Boillos, Eider Pascual-Corrales, Ana María García Cano, Jorge Gabriel Ruiz-Sanchez, Almudena Vicente Delgado, Emilia Gómez Hoyos, Rui Ferreira, Iñigo García Sanz, Mònica Recasens Sala, Rebeca Barahona San Millan, María José Picón César, Patricia Díaz Guardiola, Carolina M. Perdomo, Laura Manjón-Miguélez, Rogelio García Centeno, Ángel Rebollo Román, Paola Gracia Gimeno, Cristina Robles Lázaro, Manuel Morales-Ruiz, María Calatayud, Simone Andree Furio Collao, Diego Meneses, Miguel Sampedro Nuñez, Verónica Escudero Quesada, Elena Mena Ribas, Alicia Sanmartín Sánchez, Cesar Gonzalvo Diaz, Cristina Lamas, María del Castillo Tous, Joaquín Serrano Gotarredona, Theodora Michalopoulou Alevras, Eva María Moya Mateo, and Felicia A. Hanzu. Differences in the clinical and hormonal presentation of patients with familial and sporadic primary aldosteronism. Frontiers in Endocrinology, Mar 2024. URL: https://doi.org/10.3389/fendo.2024.1336306, doi:10.3389/fendo.2024.1336306. This article has 6 citations.

17. (aldosteronism1998intracranialaneurysmand pages 4-5): W. Aldosteronism, Reid, Lltchfield, Bruce, F. Anderson, Ruedlger, J. Weiss, Richard, P. Llfton, Robert, and Dluhy. Intracranial aneurysm and hemorrhagic stroke in glucocorticoid-remediable aldosteronism. Hypertension, 31 1 Pt 2:445-50, Jan 1998. URL: https://doi.org/10.1161/01.hyp.31.1.445, doi:10.1161/01.hyp.31.1.445. This article has 242 citations and is from a domain leading peer-reviewed journal.

18. (ylanenUnknownyeardiagnosticsofprimary pages 49-52): A YLÄNEN. Diagnostics of primary aldosteronism. Unknown journal, Unknown year.

19. (santana2022pathogenesisofprimary pages 4-5): Lucas S. Santana, Augusto G. Guimaraes, and Madson Q. Almeida. Pathogenesis of primary aldosteronism: impact on clinical outcome. Frontiers in Endocrinology, Jun 2022. URL: https://doi.org/10.3389/fendo.2022.927669, doi:10.3389/fendo.2022.927669. This article has 23 citations.

20. (adler2025primaryaldosteronisman pages 10-10): Gail K Adler, Michael Stowasser, Ricardo R Correa, Nadia Khan, Gregory Kline, Michael J McGowan, Paolo Mulatero, M Hassan Murad, Rhian M Touyz, Anand Vaidya, Tracy A Williams, Jun Yang, William F Young, Maria-Christina Zennaro, and Juan P Brito. Primary aldosteronism: an endocrine society clinical practice guideline. The Journal of clinical endocrinology and metabolism, Jul 2025. URL: https://doi.org/10.1210/clinem/dgaf284, doi:10.1210/clinem/dgaf284. This article has 211 citations.

21. (adler2025primaryaldosteronisman pages 6-7): Gail K Adler, Michael Stowasser, Ricardo R Correa, Nadia Khan, Gregory Kline, Michael J McGowan, Paolo Mulatero, M Hassan Murad, Rhian M Touyz, Anand Vaidya, Tracy A Williams, Jun Yang, William F Young, Maria-Christina Zennaro, and Juan P Brito. Primary aldosteronism: an endocrine society clinical practice guideline. The Journal of clinical endocrinology and metabolism, Jul 2025. URL: https://doi.org/10.1210/clinem/dgaf284, doi:10.1210/clinem/dgaf284. This article has 211 citations.

22. (adler2025primaryaldosteronisman media 47196b32): Gail K Adler, Michael Stowasser, Ricardo R Correa, Nadia Khan, Gregory Kline, Michael J McGowan, Paolo Mulatero, M Hassan Murad, Rhian M Touyz, Anand Vaidya, Tracy A Williams, Jun Yang, William F Young, Maria-Christina Zennaro, and Juan P Brito. Primary aldosteronism: an endocrine society clinical practice guideline. The Journal of clinical endocrinology and metabolism, Jul 2025. URL: https://doi.org/10.1210/clinem/dgaf284, doi:10.1210/clinem/dgaf284. This article has 211 citations.

23. (elston2024genetictestingfor pages 5-6): Marianne S. Elston, Jade A. U. Tamatea, Richard I. King, Chris M. Florkowski, and Veronica Boyle. Genetic testing for familial hyperaldosteronism type 1 in aotearoa/new zealand. Internal Medicine Journal, 54:1814-1820, Aug 2024. URL: https://doi.org/10.1111/imj.16511, doi:10.1111/imj.16511. This article has 3 citations and is from a peer-reviewed journal.

24. (mulatero2011prevalenceandcharacteristics pages 3-4): Paolo Mulatero, Davide Tizzani, Andrea Viola, Chiara Bertello, Silvia Monticone, Giulio Mengozzi, Domenica Schiavone, Tracy Ann Williams, Silvia Einaudi, Antonio La Grotta, Franco Rabbia, and Franco Veglio. Prevalence and characteristics of familial hyperaldosteronism: the patogen study (primary aldosteronism in torino-genetic forms). Hypertension, 58:797–803, Nov 2011. URL: https://doi.org/10.1161/hypertensionaha.111.175083, doi:10.1161/hypertensionaha.111.175083. This article has 189 citations and is from a domain leading peer-reviewed journal.

25. (adler2025primaryaldosteronisman pages 15-16): Gail K Adler, Michael Stowasser, Ricardo R Correa, Nadia Khan, Gregory Kline, Michael J McGowan, Paolo Mulatero, M Hassan Murad, Rhian M Touyz, Anand Vaidya, Tracy A Williams, Jun Yang, William F Young, Maria-Christina Zennaro, and Juan P Brito. Primary aldosteronism: an endocrine society clinical practice guideline. The Journal of clinical endocrinology and metabolism, Jul 2025. URL: https://doi.org/10.1210/clinem/dgaf284, doi:10.1210/clinem/dgaf284. This article has 211 citations.

26. (tsai2025screeninganddiagnosis pages 1-6): Cheng-Hsuan Tsai, Yu-Ching Chang, Zheng-Wei Chen, Stefanie Parisien-La Salle, Jenifer M Brown, Anand Vaidya, Vin-Cent Wu, and Yen-Hung Lin. Screening and diagnosis trends for primary aldosteronism: a longitudinal nationwide cohort study of 7.8 million people. MedRxiv, Nov 2025. URL: https://doi.org/10.1101/2025.11.13.25340212, doi:10.1101/2025.11.13.25340212. This article has 0 citations.