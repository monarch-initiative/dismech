---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-06T15:01:13.933311'
end_time: '2026-05-06T15:24:15.070511'
duration_seconds: 1381.14
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Renal Artery Obstruction
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 37
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Renal Artery Obstruction
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Renal Artery Obstruction** covering all of the
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
- **Disease Name:** Renal Artery Obstruction
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Renal Artery Obstruction** covering all of the
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


## Comprehensive Research Report: Renal Artery Obstruction (Renal Artery Obstruction / Renal Artery Stenosis / Renal Artery Occlusion)

### Executive summary (current understanding)
Renal artery obstruction (RAO) is a vascular condition in which blood flow to the kidney is limited by stenosis or occlusion of the main renal artery or major branches. In practice, RAO is an umbrella term encompassing (i) chronic, usually atherosclerotic renal artery stenosis (often discussed as atherosclerotic renovascular disease, ARVD), (ii) non-atherosclerotic stenosis such as renal-artery fibromuscular dysplasia (FMD), and (iii) acute occlusion from thromboembolism/thrombosis causing renal infarction. The clinical syndromes range from asymptomatic disease to renovascular hypertension, progressive chronic kidney disease (ischaemic nephropathy), acute kidney injury, and cardiac destabilisation syndromes including recurrent “flash” pulmonary oedema (Pickering syndrome). Evidence from large randomized trials shows that routine renal-artery stenting in unselected ARVD does not reduce major renal/cardiovascular events compared with optimized medical therapy, but contemporary guidelines and recent cohort data support revascularization for carefully selected high-risk presentations (e.g., flash pulmonary oedema, refractory hypertension, rapid loss of kidney function). (cooper2014stentingandmedical pages 1-2, theodorakopoulou2024guidelinesforthe pages 10-11, bhailis2024improvingoutcomesin pages 10-11)

### 1. Disease information

#### 1.1 Definition and scope
- **Renal Artery Obstruction (RAO)** refers to partial or complete obstruction of renal arterial blood flow. In clinical literature this is often operationalized as **renal artery stenosis (RAS)** (luminal narrowing) or **renal artery occlusion** (complete obstruction), and frequently discussed under the syndromic term **atherosclerotic renovascular disease (ARVD)** when atherosclerosis is the underlying cause. (pappaccogli2023endovascularversusmedical pages 1-5, kumar2010naturalhistoryand pages 2-2)

#### 1.2 Key identifiers and ontology mappings
- **MeSH (Medical Subject Headings)**: *Renal Artery Obstruction* **D012078** (explicitly listed in multiple ClinicalTrials.gov records). (NCT00885768 chunk 1, NCT01208714 chunk 3)
- **MONDO**: In OpenTargets, “renal artery obstruction” appears as an EFO disease concept, but no MONDO identifier for renal artery obstruction was retrieved in the available evidence. (NCT00885768 chunk 1)
- **ICD-10/ICD-11, OMIM, Orphanet**: Not retrieved in the available full-text evidence in this run; these identifiers should be populated from dedicated ontology resources (ICD/Orphanet/OMIM) in a separate lookup step.

#### 1.3 Synonyms and alternative names (as used in evidence)
Controlled vocabulary and common terms used to describe the entity include:
- “**renal artery obstruction**” (MeSH term)
- “**renal artery stenosis**” / “renal-artery stenosis” (often abbreviated **RAS**)
- “**renovascular disease**”
- “**renal artery occlusion**”
- “**atherosclerotic renovascular disease**” / “atherosclerotic renal artery stenosis” (ARVD/ARAS)
These terms were explicitly used as MeSH/text-word definitions for ARVD in the natural-history review and in clinical trial registries. (kumar2010naturalhistoryand pages 2-2, NCT01208714 chunk 3)

#### 1.4 Evidence source types
The information summarized here is derived from:
- **Aggregated disease-level evidence**: reviews and guidelines (2023–2024 prioritized), systematic reviews, and randomized trial reports. (pappaccogli2023endovascularversusmedical pages 1-5, theodorakopoulou2024guidelinesforthe pages 10-11, cooper2014stentingandmedical pages 1-2)
- **Clinical trial registries** (ClinicalTrials.gov) with MeSH ontology tagging and eligibility thresholds. (NCT01208714 chunk 3)
- **Cohort/real-world observational evidence** including multidisciplinary-team (MDT) selection for revascularization. (bhailis2024improvingoutcomesin pages 10-11)

### 2. Etiology

#### 2.1 Disease causal factors (primary causes)
1) **Atherosclerotic renal artery stenosis / ARVD**
- ARVD is described as the **most frequent cause of renovascular hypertension** and is typically part of systemic atherosclerosis. (pappaccogli2023endovascularversusmedical pages 1-5)

2) **Fibromuscular dysplasia (FMD)-related renal artery stenosis**
- FMD is a **non-atherosclerotic arteriopathy** commonly affecting renal arteries (and carotid arteries), typically diagnosed by angiographic features such as a “string-of-beads” appearance in adults. (theodorakopoulou2024guidelinesforthe pages 10-11, pytlos2024renalarterystenosis pages 1-2)

3) **Acute thrombotic/embolic obstruction → renal infarction**
- Renal infarction is defined as a **blood clot in the main renal artery or branches causing partial/complete obstruction of blood supply**, often due to cardiovascular disease or renal vascular disorders, and described as increasingly recognized in the SARS-CoV-2 era. (richer2020anovelrecurrent pages 8-9)

#### 2.2 Risk factors
**For ARVD (atherosclerotic RAO)**
- **Age**: prevalence increases with age. (pappaccogli2023endovascularversusmedical pages 1-5)
- **Systemic atherosclerotic disease**: enriched in patients with coronary artery disease and heart failure. (pappaccogli2023endovascularversusmedical pages 1-5)
- **Diabetes and baseline renal dysfunction** are associated with worse progression/outcomes in natural-history data. (kumar2010naturalhistoryand pages 4-5)

**For renal infarction (acute occlusion)**
- In the COVID-era systematic review, renal infarction was framed as thrombotic disease, often occurring despite thromboprophylaxis and sometimes with extrarenal thromboembolism. (richer2020anovelrecurrent pages 8-9)

**Pediatric renovascular disease**
- Etiologies in children include FMD, mid-aortic syndrome (MAS), Takayasu arteritis, Kawasaki disease, syndromic causes (e.g., NF1), trauma, radiation, and extraluminal tumor compression. (pytlos2024renalarterystenosis pages 1-2)

#### 2.3 Protective factors
No explicit genetic or environmental protective factors were identified in the retrieved evidence.

#### 2.4 Gene–environment interactions
No explicit gene–environment interaction evidence was identified in the retrieved sources.

### 3. Phenotypes (clinical presentation)

#### 3.1 Core phenotypes for ARVD / chronic RAO
Clinical manifestations span:
- **Renovascular hypertension**, including resistant/uncontrolled hypertension. (bhailis2024improvingoutcomesin pages 2-3)
- **Ischaemic nephropathy** (progressive kidney dysfunction downstream of stenosis). (bhailis2024improvingoutcomesin pages 1-2)
- **Cardiac destabilisation syndromes** including **sudden pulmonary oedema** and recurrent heart-failure admissions. (bhailis2024improvingoutcomesin pages 2-3)
- Severe presentations noted in reviews include “**recurrent flash pulmonary oedema, rapidly progressive chronic kidney disease or acute kidney injury**.” (direct quote from abstract-level content summarized in the ARVD review) (pappaccogli2023endovascularversusmedical pages 1-5)

**HPO term suggestions (non-exhaustive)**
- Hypertension (**HP:0000822**)
- Resistant hypertension (not a canonical single HPO term; map to **HP:0000822** plus clinical modifier)
- Pulmonary edema (**HP:0002204**)
- Congestive heart failure (**HP:0001635**)
- Chronic kidney disease (**HP:0012622**)
- Acute kidney injury (**HP:0001919**)

#### 3.2 Phenotypes for acute renal artery occlusion / renal infarction
In the COVID-era systematic review and case literature, renal infarction is commonly symptomatic and often presents with nonspecific symptoms.
- The 2023 case report review noted renal infarction is “extremely rare,” and that **“more than 95% of cases are symptomatic”** (quote from abstract). (richer2020anovelrecurrent pages 8-9)

**HPO term suggestions**
- Flank pain (**HP:0030834**)
- Abdominal pain (**HP:0002027**)
- Hematuria (**HP:0000790**)
- Fever (**HP:0001945**)
- Elevated lactate dehydrogenase (LDH) (map to laboratory phenotype; HPO has **HP:0031950** “Elevated circulating lactate dehydrogenase level”)
- Acute kidney injury (**HP:0001919**)
- Anuria (**HP:0003779**) (for bilateral occlusion presentations)

#### 3.3 Pediatric renovascular disease phenotypes
RAS and MAS are described as “significant yet under-recognized causes of pediatric hypertension.” (pytlos2024renalarterystenosis pages 1-2)

**HPO term suggestions**
- Pediatric hypertension (map to **HP:0000822** with age-of-onset annotation)

### 4. Genetic / molecular information

#### 4.1 Causal genes
Renal artery obstruction as a broad category is not primarily a Mendelian disease. However, **FMD-spectrum arteriopathy** may include monogenic contributors/modifiers.

**COL5A1 (collagen type V alpha 1 chain)**
- Richer et al. reported recurrent **COL5A1 c.1540G>A, p.(Gly514Ser)** associated with a dysplasia-associated arterial disease with **multifocal FMD** and dissections. (richer2020anovelrecurrent pages 1-2)

#### 4.2 Pathogenic variants and variant details (FMD-spectrum)
- Variant: **COL5A1 c.1540G>A, p.(Gly514Ser)** (also referred to as **G514S**). (richer2020anovelrecurrent pages 1-2)
- In an mFMD exome cohort (n=264), deleterious COL5A1 variants were identified in **≈2.7%** of cases and were associated with arterial dissections (**P=0.005**). (richer2020anovelrecurrent pages 1-2)
- The paper notes the recurring variant is absent from gnomAD and lies on a shared haplotype consistent with a founder effect. (richer2020anovelrecurrent pages 1-2)

**Mechanistic inference (protein-level) reported**
- Structural modeling suggested Gly→Ser substitution “create[s] an externalized residue” in the collagenous region, plausibly affecting collagen fibrillogenesis and vascular integrity. (richer2020anovelrecurrent pages 5-7)

#### 4.3 Modifier genes / epigenetics / chromosomal abnormalities
No additional modifiers, epigenetic changes, or chromosomal abnormalities were found in the retrieved evidence.

### 5. Environmental information
ARVD is strongly linked to systemic atherosclerosis; however, explicit environmental exposures (toxins/pollution) were not discussed in the retrieved evidence. Acute renal infarction can occur in systemic prothrombotic states and was described in association with SARS-CoV-2 infection. (richer2020anovelrecurrent pages 8-9)

### 6. Mechanism / pathophysiology

#### 6.1 ARVD causal chain (hemodynamic ischemia → kidney dysfunction and systemic effects)
- **Trigger**: atherosclerotic narrowing of renal artery reduces perfusion.
- **Intermediate processes**: kidney ischemia/hypoxia and progressive parenchymal and microvascular damage (ischaemic nephropathy).
- **Downstream clinical syndromes**: resistant hypertension, progressive CKD, AKI, and cardiac destabilisation syndromes (flash pulmonary oedema/heart failure). (bhailis2024improvingoutcomesin pages 2-3, pappaccogli2023endovascularversusmedical pages 15-20)

A key emerging concept is the **renal “penumbra”**—a post-stenotic kidney that is hypoxic yet potentially salvageable. Pappaccogli et al. summarize functional imaging proposals, including BOLD-MRI to:
- “**Assess kidney’s renal oxygenation**” and
- “**Differentiate hypoxic but still functionable and salvable poststenotic kidney from hypoxic and functionally dead and unsalvable poststenotic kidney**.” (direct quotes) (pappaccogli2023endovascularversusmedical pages 32-35)

**RAAS involvement**
- RAAS involvement is referenced in the ARVD decisional framework and broader hypertension/CKD context; detailed RAAS molecular cascade was not explicitly delineated in retrieved full text. (pappaccogli2023endovascularversusmedical pages 32-35)

#### 6.2 FMD-spectrum vascular wall pathology
Richer et al. report histology consistent with medial fibroplasia and vascular wall structural abnormalities in COL5A1 variant carriers, including increased medial collagen, smooth muscle cell disorganization, and elastin fragmentation. (richer2020anovelrecurrent pages 7-8)

#### 6.3 GO / CL term suggestions (mechanism-linked)
**GO Biological Process (suggested)**
- Response to hypoxia (GO:0001666)
- Renin–angiotensin system regulation of blood pressure (GO mapping not provided in evidence; suggested)
- Extracellular matrix organization (GO:0030198)
- Collagen fibril organization (GO:0030199)

**Cell types (CL; suggested)**
- Vascular smooth muscle cell (CL:0000192)
- Endothelial cell (CL:0000115)
- Renal tubular epithelial cell (broad; e.g., proximal tubule epithelial cell CL:0002308)

### 7. Anatomical structures affected

**Primary**
- Renal artery (main renal artery and branches) and downstream kidney parenchyma. (richer2020anovelrecurrent pages 8-9)

**Secondary**
- Cardiovascular system: heart failure/pulmonary oedema syndromes in ARVD. (bhailis2024improvingoutcomesin pages 2-3)

**UBERON suggestions**
- Kidney (UBERON:0002113)
- Renal artery (UBERON term; exact ID not retrieved in evidence)
- Renal cortex (UBERON:0001225)

### 8. Temporal development

**ARVD**
- Often chronic and progressive; natural history includes progression of stenosis and possible total occlusion over years. (kumar2010naturalhistoryand pages 2-2)

**Renal infarction**
- Often acute/subacute onset; COVID-era cases were commonly diagnosed within a month of infection. (richer2020anovelrecurrent pages 8-9)

### 9. Inheritance and population

#### 9.1 Epidemiology (selected quantitative data)
**ARVD prevalence estimates (adult)**
- In the 2023 Hypertension review, ARVD is estimated to account for **~1–2% of hypertension** overall, and **~7% of adults >65 years** have RAS >60%. Higher prevalence is reported in specific populations: **10–12%** in end-stage renal disease, **15–30%** with coronary artery disease, and **up to 50%** in heart failure. (pappaccogli2023endovascularversusmedical pages 1-5)

**Pediatric**
- Pediatric arterial hypertension prevalence is ~**4%**; renovascular disease accounts for **5–10%** of secondary hypertension in children; MAS is **0.5–2%** of aortic stenosis; **20–48%** of children with renovascular hypertension may have combined renal-artery and mid-aortic narrowing. (pytlos2024renalarterystenosis pages 1-2)

#### 9.2 Natural history/progression (ARVD)
- In one cohort summarized in the natural history review: progression occurred in **44%** over mean **52 months**, with **16%** progressing to total occlusion; progression to complete occlusion was **39%** in the **75–99%** stenosis group vs **5%** in the **<50%** group. (kumar2010naturalhistoryand pages 2-2)

#### 9.3 Genetic etiology population notes
- COL5A1 c.1540G>A p.(Gly514Ser) is described as recurring on a shared haplotype consistent with a founder effect; deleterious COL5A1 variants appear in ≈2.7% of an mFMD cohort. (richer2020anovelrecurrent pages 1-2)

### 10. Diagnostics

#### 10.1 Clinical tests and biomarkers
**ARVD/stenosis**
- The diagnostic approach emphasizes imaging confirmation and evaluation of kidney viability.
- Proteinuria/albuminuria is used as a marker of established parenchymal damage in ischemic nephropathy phenotyping (ACR >30 mg/mmol or PCR >50 mg/mol). (bhailis2024improvingoutcomesin pages 2-3)

**Renal infarction**
- The COVID-era review notes serum LDH and D-dimers are frequently elevated; contrast-enhanced CT is a key diagnostic modality. (richer2020anovelrecurrent pages 8-9)

#### 10.2 Imaging
- **Angiography** is described as the gold standard in registry documentation. (NCT00885768 chunk 1)
- **CTA and contrast-enhanced MRA** are preferred imaging modalities in the 2024 MDT cohort. (bhailis2024improvingoutcomesin pages 2-3)
- **Non-contrast MRA** is used for advanced CKD (GFR <30) in that cohort. (bhailis2024improvingoutcomesin pages 2-3)
- Duplex ultrasound parameters noted in a 2024 review excerpt include renal–aortic ratio (RAR) ≥3.5 and flow velocities, and caution that CTA/MRA may overestimate stenosis. (piechocki2024…peripheral pages 13-15)

#### 10.3 Functional/advanced diagnostics (emerging)
- Functional imaging proposals include **BOLD-MRI** for renal oxygenation/penumbra detection and physiologic assessment via translesional pressure gradients, plus biomarkers such as NGAL and FGF-23. (pappaccogli2023endovascularversusmedical pages 32-35)

#### 10.4 Diagnostic thresholds used in trials/registries
Examples:
- >50% stenosis used as clinically significant in multiple protocols/cohort selection. (bhailis2024improvingoutcomesin pages 2-3, NCT06822205 chunk 1)
- ≥70% stenosis used as “high-grade” inclusion in multiple trial records. (NCT01208714 chunk 3, NCT05603221 chunk 1)
- CORAL required stenosis ≥60% and enrolled high-grade lesions; subgroup definitions included >80%. (cooper2014stentingandmedical pages 8-9)

### 11. Outcome / prognosis

#### 11.1 ARVD (trial and cohort outcomes)
**Randomized trial evidence (CORAL)**
- CORAL randomized 947 patients to stenting+medical therapy vs medical therapy alone and found no difference in the primary composite endpoint: **35.1% vs 35.8%** (HR **0.94**, 95% CI 0.76–1.17; P=0.58) over median 43 months; systolic BP was modestly lower in the stent group (−2.3 mmHg). (cooper2014stentingandmedical pages 1-2)

**Real-world phenotype-targeted outcomes (2024 MDT cohort)**
- Among revascularized patients, phenotype-specific improvements were reported: BP improvement in severe hypertension, attenuation of GFR decline in ischemic nephropathy, and no further HF admissions in heart-failure syndrome subgroup. (bhailis2024improvingoutcomesin pages 10-11)

**Prognostic factors / predictors**
- Factors indicating lower benefit: atrophic kidney (length <8 cm) and significant proteinuria/albuminuria indicating irreversible parenchymal damage. (bhailis2024improvingoutcomesin pages 2-3)
- Natural-history risk factors for progression/worse outcomes include high-grade stenosis, severe systolic hypertension, diabetes, abnormal baseline creatinine, and bilateral disease. (kumar2010naturalhistoryand pages 4-5)

#### 11.2 Renal infarction outcomes (COVID-era case systematic review)
- 35 cases were included; 5 deaths occurred; renal function preserved in 17; renal impairment in 5; kidney replacement therapy in 5; invasive therapies performed in 2. (richer2020anovelrecurrent pages 8-9)

### 12. Treatment

#### 12.1 Medical therapy (ARVD)
Standard of care includes multifactorial cardiovascular risk reduction: antihypertensive, antiplatelet, and lipid-lowering agents, with diabetes optimization when relevant. (pappaccogli2023endovascularversusmedical pages 1-5)

#### 12.2 Revascularization (ARVD): evidence base and indications
**Evidence (CORAL)**
- No reduction in major renal/cardiovascular outcomes with routine stenting in addition to optimized medical therapy; small BP difference. (cooper2014stentingandmedical pages 1-2)

**Guideline-oriented selection (2023 ESH as summarized in 2024 CKJ review)**
- **Atherosclerotic renovascular disease**: offer revascularization *in addition to medical therapy* for patients with documented secondary hypertension from ARVD or high-risk clinical presentations such as **flash pulmonary edema, refractory hypertension, or rapid loss of kidney function**, when stenosis is **high-grade (≥70%)**. (theodorakopoulou2024guidelinesforthe pages 10-11)
- **FMD and critical renal artery stenosis**: recommended **balloon angioplasty without stenting**. (theodorakopoulou2024guidelinesforthe pages 10-11)

**Implementation/real-world practice (MDT cohort)**
- Multidisciplinary review selected patients based on clinical phenotype, lesion severity, and downstream kidney state; 79% had presentation-specific benefit after revascularization in their retrospective series. (bhailis2024improvingoutcomesin pages 1-2)

#### 12.3 Renal infarction (acute occlusion)
- Conservative therapy dominated, with **low molecular weight heparin** common, and a minority receiving thrombus aspiration or catheter-directed thrombolysis; authors conclude conservative measures often suffice but severe cases may need aggressive therapy. (richer2020anovelrecurrent pages 8-9)

#### 12.4 MAXO term suggestions (treatments/actions)
- Percutaneous transluminal angioplasty (renal) (MAXO: term not retrieved; suggested)
- Renal artery stent placement (MAXO suggested)
- Antihypertensive therapy (MAXO suggested)
- Antiplatelet therapy (MAXO suggested)
- Lipid-lowering therapy (MAXO suggested)
- Anticoagulation therapy (MAXO suggested)
- Thrombolytic therapy (MAXO suggested)

#### 12.5 Ongoing/registered clinical studies (examples)
- **METRAS** (Medical and Endovascular Treatment of Atherosclerotic Renal Artery Stenosis), NCT01208714: randomized PTRAS vs optimal medical treatment with long-term follow-up and eligibility based on angio-CT stenosis thresholds and Doppler resistance index criteria. (NCT01208714 chunk 3)
- **European/International FMD Registry and Initiative**, NCT04804683: recruiting registry/initiative (interventional designation in record). (ClinicalTrials.gov record retrieved; see trial list) (NCT01208714 chunk 3)

### 13. Prevention
No RAO-specific primary prevention interventions were detailed in retrieved sources beyond general **atherosclerotic cardiovascular risk-factor control** inherent to ARVD management (lipids, BP, antiplatelet where indicated). (pappaccogli2023endovascularversusmedical pages 1-5)

### 14. Other species / natural disease
No naturally occurring veterinary disease evidence for renal artery obstruction was identified in the retrieved evidence.

### 15. Model organisms
No animal or in vitro model organism data were identified in the retrieved evidence set.

---

## Key recent developments (2023–2024 emphasis)

1) **Refined patient selection for revascularization**
- 2024 MDT cohort emphasizes that outcomes depend on **clinical presentation** and downstream kidney state, reporting high proportions of phenotype-specific improvement after revascularization when selected by MDT review. (bhailis2024improvingoutcomesin pages 1-2, bhailis2024improvingoutcomesin pages 10-11)

2) **Guideline clarification for high-risk ARVD**
- The 2024 CKJ guideline review of 2023 ESH guidance supports revascularization for high-risk phenotypes with **≥70%** stenosis and recommends angioplasty without stenting for **FMD**. (theodorakopoulou2024guidelinesforthe pages 10-11)

3) **Emerging diagnostics and “renal penumbra” concept**
- The 2023 Hypertension review highlights functional imaging (e.g., BOLD-MRI) to distinguish salvageable post-stenotic kidney (“renal penumbra”), and lists candidate biomarkers (NGAL, FGF-23) and novel therapeutic adjuncts (cell/growth factor approaches). (pappaccogli2023endovascularversusmedical pages 15-20, pappaccogli2023endovascularversusmedical pages 32-35)

---

## Evidence map table
The following table compacts etiologies, clinical syndromes, diagnostics, and outcomes with key statistics.

| Etiologic subtype | Typical patient profile / risk factors | Hallmark clinical presentations / phenotypes | Key diagnostics and thresholds | Key quantitative data | Key evidence (year, journal, PMID/DOI, URL) |
|---|---|---|---|---|---|
| Atherosclerotic renovascular disease (ARVD) / atherosclerotic renal artery stenosis | Usually older adults; prevalence rises with age; enriched in end-stage CKD, coronary artery disease, heart failure; generalized atherosclerosis; resistant/secondary hypertension risk context (pappaccogli2023endovascularversusmedical pages 1-5, NCT00885768 chunk 1) | Asymptomatic disease to renovascular hypertension, malignant/resistant hypertension, recurrent flash pulmonary edema, rapidly progressive CKD, AKI; may present with heart-failure syndromes (“Pickering syndrome”) (pappaccogli2023endovascularversusmedical pages 1-5, pappaccogli2023endovascularversusmedical pages 12-15) | MeSH term: Renal Artery Obstruction (D012078); angiography gold standard; trial/registry thresholds commonly >50%, ≥60%, ≥70%, ≥80%; CORAL enrolled stenosis ≥60%; METRAS: >70% on angio-CT or <70% with post-stenotic dilatation plus Doppler RI criteria; high-risk revascularization guideline phenotype: high-grade stenosis ≥70% with flash pulmonary edema, refractory hypertension, or rapid renal decline (NCT00885768 chunk 1, NCT01208714 chunk 3, cooper2014stentingandmedical pages 1-2, theodorakopoulou2024guidelinesforthe pages 10-11) | Prevalence: ~1–2% of all hypertension; ~7% of adults >65 have RAS >60%; 10–12% in ESRD; 15–30% with CAD; up to 50% in heart failure. Natural history: progression in 44% over mean 52 months; 16% to total occlusion; occlusion 39% in 75–99% stenosis vs 5% in <50% group. CORAL: primary composite events 35.1% stent+medical vs 35.8% medical only, HR 0.94 (95% CI 0.76–1.17), median follow-up 43 months; SBP difference −2.3 mmHg favoring stent (pappaccogli2023endovascularversusmedical pages 1-5, kumar2010naturalhistoryand pages 2-2, cooper2014stentingandmedical pages 1-2) | Pappaccogli et al., 2023, *Hypertension*, DOI: 10.1161/HYPERTENSIONAHA.122.17965, https://doi.org/10.1161/HYPERTENSIONAHA.122.17965; Cooper et al., 2014, *N Engl J Med*, DOI: 10.1056/NEJMoa1310753, https://doi.org/10.1056/NEJMoa1310753; Kumar et al., 2010, *Nephrology*, DOI: 10.1111/j.1440-1797.2009.01242.x, https://doi.org/10.1111/j.1440-1797.2009.01242.x (pappaccogli2023endovascularversusmedical pages 1-5, cooper2014stentingandmedical pages 1-2, kumar2010naturalhistoryand pages 2-2) |
| Fibromuscular dysplasia (FMD)-related renal artery stenosis | More typical in younger patients, especially women; nonatherosclerotic, noninflammatory arteriopathy; can be multifocal (“string-of-beads”); associated systemic arteriopathy/dissection burden; pediatric FMD may differ from adult FMD (theodorakopoulou2024guidelinesforthe pages 10-11, pytlos2024renalarterystenosis pages 1-2) | Renovascular/resistant hypertension, renal artery stenosis, occasionally renal infarction; multifocal disease, dissections, aneurysms; characteristic angiographic “string-of-beads” in adults; may coexist with cerebrovascular/cervical lesions (theodorakopoulou2024guidelinesforthe pages 10-11, pytlos2024renalarterystenosis pages 1-2) | ESH 2023/2024 synopsis: for FMD and critical RAS, balloon angioplasty without stenting; brain-to-pelvis imaging and antiplatelet therapy discussed in 2024 review; diagnosis/classification relies on angiographic features after excluding mimics (theodorakopoulou2024guidelinesforthe pages 10-11) | Evidence in chat is mainly qualitative; case-report summary notes angioplasty may alleviate hypertension in up to 80% of cases; pediatric review emphasizes heterogeneity and under-recognition rather than firm prevalence for adult renal FMD (pytlos2024renalarterystenosis pages 1-2) | Theodorakopoulou et al., 2024, *Clin Kidney J*, DOI: 10.1093/ckj/sfae278, https://doi.org/10.1093/ckj/sfae278; Pytlos et al., 2024, *J Clin Med*, DOI: 10.3390/jcm13226778, https://doi.org/10.3390/jcm13226778; Østergaard et al., 2024, *J Clin Hypertens*, DOI: 10.1111/jch.14865, https://doi.org/10.1111/jch.14865 (theodorakopoulou2024guidelinesforthe pages 10-11, pytlos2024renalarterystenosis pages 1-2) |
| Acute renal artery thrombosis / embolism / renal infarction | Often linked to cardioembolic disease (especially atrial fibrillation), thrombosis, hypercoagulable states, aortic dissection, trauma or iatrogenic injury; COVID-19-associated thrombosis reported; can also occur with FMD (pappaccogli2023endovascularversusmedical pages 1-5, richer2020anovelrecurrent pages 8-9) | Acute flank/abdominal pain, nausea/vomiting, fever, hematuria, hypertension, AKI; can be misdiagnosed as nephrolithiasis or appendicitis; some asymptomatic incidental cases reported; bilateral occlusion may cause severe kidney failure/anuria (richer2020anovelrecurrent pages 8-9) | Contrast-enhanced CT is repeatedly described as the key/gold-standard imaging modality; lab clues include elevated LDH, inflammatory markers, hematuria; DSA/CTA may define occlusion and guide thrombolysis/thrombectomy; inclusion studies distinguish high-grade stenosis from complete occlusion (NCT05603221 chunk 1, richer2020anovelrecurrent pages 8-9) | COVID-era systematic review: 35 cases in 33 reports; diagnosed within 1 month of SARS-CoV-2 in most cases; laterality right 7, left 15, bilateral 8, allograft 5; 17/35 had extrarenal thromboembolism; kidney replacement therapy in 5; invasive aspiration/thrombolysis in 2; 5 deaths; total renal function preserved in 17, renal impairment in 5. Renal infarction is symptomatic in >95% in one 2023 case review (richer2020anovelrecurrent pages 8-9) | Kozyrakis et al., 2023, *Arch Ital Urol Androl*, DOI: 10.4081/aiua.2023.11625, https://doi.org/10.4081/aiua.2023.11625; Mizusugi & Kenzaka, 2023, *Medicina*, DOI: 10.3390/medicina59061176, https://doi.org/10.3390/medicina59061176 (richer2020anovelrecurrent pages 8-9) |
| Pediatric renal artery stenosis / pediatric renovascular disease | Children with secondary hypertension; etiologies differ from adults and include FMD, mid-aortic syndrome (MAS), Takayasu arteritis, Kawasaki disease, segmental arterial mediolysis, neurofibromatosis type 1, renal artery aneurysm, trauma, radiation, tumor compression (pytlos2024renalarterystenosis pages 1-2) | Under-recognized cause of pediatric hypertension; can present with severe/refractory hypertension and target-organ damage; combined renal-artery and aortic narrowing in MAS; pharmacotherapy often partial only (pytlos2024renalarterystenosis pages 1-2) | Advanced imaging emphasized; Doppler velocity thresholds vary with age/size/circulatory state; multidisciplinary evaluation recommended; interventions include angioplasty, renal artery reimplantation, aorto-aortic bypass depending on pathology/extent (pytlos2024renalarterystenosis pages 1-2) | Pediatric arterial hypertension prevalence ~4%; renovascular disease causes 5–10% of secondary hypertension in children; MAS accounts for 0.5–2% of aortic stenosis; 20–48% of children with renovascular hypertension may have combined renal artery and mid-aortic narrowing (pytlos2024renalarterystenosis pages 1-2) | Pytlos et al., 2024, *J Clin Med*, DOI: 10.3390/jcm13226778, https://doi.org/10.3390/jcm13226778 (pytlos2024renalarterystenosis pages 1-2) |
| High-risk ARVD subgroup likely to benefit from revascularization | Patients selected by multidisciplinary review; anatomically significant stenosis with adequately sized kidney and one of: uncontrollable hypertension, deteriorating kidney function, or heart-failure syndrome; exclusion of atrophic/nonviable kidneys improves yield (pappaccogli2023endovascularversusmedical pages 12-15, richer2020anovelrecurrent pages 12-13) | Severe hypertension, progressive ischemic nephropathy, recurrent heart-failure admissions/flash pulmonary edema, ACEi/ARB-associated acute GFR fall (esp. bilateral disease/solitary kidney) (pappaccogli2023endovascularversusmedical pages 12-15, richer2020anovelrecurrent pages 12-13) | Predictors of limited benefit: kidney length <8 cm, cortical thickness <0.5 cm, renal resistive index >0.8, proteinuria >1 g/day; MDT series used stenosis ≥50% for review and international-guideline-based selection for revascularization (pappaccogli2023endovascularversusmedical pages 12-15, richer2020anovelrecurrent pages 12-13) | In 2024 MDT retrospective cohort, 127 patients with stenosis ≥50% were reviewed and 57 revascularized; 79% had presentation-specific benefit; BP improved in 82% with severe hypertension; 72% with progressive ischemic nephropathy had attenuated GFR decline; no further HF admissions in heart-failure subgroup; among those revascularized for high-grade stenosis alone, 78% had better BP control and 55% renal functional benefit (richer2020anovelrecurrent pages 12-13) | de Bhailis et al., 2024, *J Nephrol*, DOI: 10.1007/s40620-024-01902-1, https://doi.org/10.1007/s40620-024-01902-1; Pappaccogli et al., 2023, *Hypertension*, DOI: 10.1161/HYPERTENSIONAHA.122.17965, https://doi.org/10.1161/HYPERTENSIONAHA.122.17965 (richer2020anovelrecurrent pages 12-13, pappaccogli2023endovascularversusmedical pages 12-15) |


*Table: This table compacts the major clinical subtypes of renal artery obstruction and compares their risk factors, phenotypes, diagnostic thresholds, and quantitative evidence. It is useful as a quick-reference evidence map linking etiologic subtype to presentation, workup, and outcomes.*

---

## Visual evidence (diagnostic/decision algorithms)
Pappaccogli et al. (Hypertension 2023) include a decisional algorithm and a table summarizing diagnostic tests and novel strategies for ARVD management (Table 2 and Figure 3). These were retrieved as cropped images. (pappaccogli2023endovascularversusmedical media 2c3b7fe8, pappaccogli2023endovascularversusmedical media affaa2a8)

---

## Important limitations / data not retrieved in this run
- ICD-10/ICD-11, Orphanet, and MONDO identifiers for “renal artery obstruction” were not retrieved from the current evidence set and should be added via dedicated ontology lookup.
- High-resolution incidence/prevalence estimates for adult renal infarction outside case series, and robust population statistics for renal FMD, were not retrieved.
- Multi-omics (transcriptomics/proteomics/metabolomics), epigenetic signatures, and validated model-organism systems for RAO were not present in the retrieved texts.


References

1. (cooper2014stentingandmedical pages 1-2): Christopher J. Cooper, Timothy P. Murphy, Donald E. Cutlip, Kenneth Jamerson, William Henrich, Diane M. Reid, David J. Cohen, Alan H. Matsumoto, Michael Steffes, Michael R. Jaff, Martin R. Prince, Eldrin F. Lewis, Katherine R. Tuttle, Joseph I. Shapiro, John H. Rundback, Joseph M. Massaro, Ralph B. D'Agostino, and Lance D. Dworkin. Stenting and medical therapy for atherosclerotic renal-artery stenosis. The New England journal of medicine, 370 1:13-22, Jan 2014. URL: https://doi.org/10.1056/nejmoa1310753, doi:10.1056/nejmoa1310753. This article has 1274 citations and is from a highest quality peer-reviewed journal.

2. (theodorakopoulou2024guidelinesforthe pages 10-11): Marieta Theodorakopoulou, Alberto Ortiz, Beatriz Fernandez-Fernandez, Mehmet Kanbay, Roberto Minutolo, and Pantelis A Sarafidis. Guidelines for the management of hypertension in ckd patients: where do we stand in 2024? Clinical Kidney Journal, 17:ii36-ii50, Nov 2024. URL: https://doi.org/10.1093/ckj/sfae278, doi:10.1093/ckj/sfae278. This article has 41 citations and is from a peer-reviewed journal.

3. (bhailis2024improvingoutcomesin pages 10-11): Áine M. de Bhailis, Edward Lake, Constantina Chrysochou, Darren Green, Rajkumar Chinnadurai, and Philip A. Kalra. Improving outcomes in atherosclerotic renovascular disease: importance of clinical presentation and multi-disciplinary review. Journal of Nephrology, 37:1093-1105, Apr 2024. URL: https://doi.org/10.1007/s40620-024-01902-1, doi:10.1007/s40620-024-01902-1. This article has 7 citations and is from a peer-reviewed journal.

4. (pappaccogli2023endovascularversusmedical pages 1-5): Marco Pappaccogli, Tom Robberechts, Jean-Philippe Lengelé, Patricia Van der Niepen, Pantelis Sarafidis, Franco Rabbia, and Alexandre Persu. Endovascular versus medical management of atherosclerotic renovascular disease: update and emerging concepts. Hypertension, 80:1150-1161, Jun 2023. URL: https://doi.org/10.1161/hypertensionaha.122.17965, doi:10.1161/hypertensionaha.122.17965. This article has 38 citations and is from a domain leading peer-reviewed journal.

5. (kumar2010naturalhistoryand pages 2-2): Subramanian Karthik Kumar, Robert MacGinley, Murty Mantha, Peter Mount, Matthew Roberts, and George Mangos. Natural history and progression of atherosclerotic renal vascular stenosis. Nephrology, Apr 2010. URL: https://doi.org/10.1111/j.1440-1797.2009.01242.x, doi:10.1111/j.1440-1797.2009.01242.x. This article has 4 citations and is from a peer-reviewed journal.

6. (NCT00885768 chunk 1):  Prevalence of Renal Artery Stenosis in Patients Referred for Cardiac Catheterization. Imam Khomeini Hospital. 2008. ClinicalTrials.gov Identifier: NCT00885768

7. (NCT01208714 chunk 3):  Medical and Endovascular Treatment of Atherosclerotic Renal Artery Stenosis (METRAS Study). University Hospital Padova. 2010. ClinicalTrials.gov Identifier: NCT01208714

8. (pytlos2024renalarterystenosis pages 1-2): Jakub Pytlos, Aneta Michalczewska, Piotr Majcher, Mariusz Furmanek, and Piotr Skrzypczyk. Renal artery stenosis and mid-aortic syndrome in children—a review. Journal of Clinical Medicine, 13:6778, Nov 2024. URL: https://doi.org/10.3390/jcm13226778, doi:10.3390/jcm13226778. This article has 6 citations.

9. (richer2020anovelrecurrent pages 8-9): Julie Richer, Hannah L. Hill, Yu Wang, Min-Lee Yang, Kristina L. Hunker, Jamie Lane, Susan Blackburn, Dawn M. Coleman, Jonathan Eliason, Guillaume Sillon, Maria-Daniela D’Agostino, Prasad Jetty, François-Pierre Mongeon, Anne-Marie Laberge, Stephen E. Ryan, Natalia Fendrikova-Mahlay, Thais Coutinho, Michael R. Mathis, Matthew Zawistowski, Stanley L. Hazen, Alexander E. Katz, Heather L. Gornik, Chad M. Brummett, Goncalo Abecasis, Ingrid L. Bergin, James C. Stanley, Jun Z. Li, and Santhi K. Ganesh. A novel recurrent <i>col5a1</i> genetic variant is associated with a dysplasia-associated arterial disease exhibiting dissections and fibromuscular dysplasia. Arteriosclerosis, Thrombosis, and Vascular Biology, 40:2686-2699, Nov 2020. URL: https://doi.org/10.1161/atvbaha.119.313885, doi:10.1161/atvbaha.119.313885. This article has 50 citations and is from a domain leading peer-reviewed journal.

10. (kumar2010naturalhistoryand pages 4-5): Subramanian Karthik Kumar, Robert MacGinley, Murty Mantha, Peter Mount, Matthew Roberts, and George Mangos. Natural history and progression of atherosclerotic renal vascular stenosis. Nephrology, Apr 2010. URL: https://doi.org/10.1111/j.1440-1797.2009.01242.x, doi:10.1111/j.1440-1797.2009.01242.x. This article has 4 citations and is from a peer-reviewed journal.

11. (bhailis2024improvingoutcomesin pages 2-3): Áine M. de Bhailis, Edward Lake, Constantina Chrysochou, Darren Green, Rajkumar Chinnadurai, and Philip A. Kalra. Improving outcomes in atherosclerotic renovascular disease: importance of clinical presentation and multi-disciplinary review. Journal of Nephrology, 37:1093-1105, Apr 2024. URL: https://doi.org/10.1007/s40620-024-01902-1, doi:10.1007/s40620-024-01902-1. This article has 7 citations and is from a peer-reviewed journal.

12. (bhailis2024improvingoutcomesin pages 1-2): Áine M. de Bhailis, Edward Lake, Constantina Chrysochou, Darren Green, Rajkumar Chinnadurai, and Philip A. Kalra. Improving outcomes in atherosclerotic renovascular disease: importance of clinical presentation and multi-disciplinary review. Journal of Nephrology, 37:1093-1105, Apr 2024. URL: https://doi.org/10.1007/s40620-024-01902-1, doi:10.1007/s40620-024-01902-1. This article has 7 citations and is from a peer-reviewed journal.

13. (richer2020anovelrecurrent pages 1-2): Julie Richer, Hannah L. Hill, Yu Wang, Min-Lee Yang, Kristina L. Hunker, Jamie Lane, Susan Blackburn, Dawn M. Coleman, Jonathan Eliason, Guillaume Sillon, Maria-Daniela D’Agostino, Prasad Jetty, François-Pierre Mongeon, Anne-Marie Laberge, Stephen E. Ryan, Natalia Fendrikova-Mahlay, Thais Coutinho, Michael R. Mathis, Matthew Zawistowski, Stanley L. Hazen, Alexander E. Katz, Heather L. Gornik, Chad M. Brummett, Goncalo Abecasis, Ingrid L. Bergin, James C. Stanley, Jun Z. Li, and Santhi K. Ganesh. A novel recurrent <i>col5a1</i> genetic variant is associated with a dysplasia-associated arterial disease exhibiting dissections and fibromuscular dysplasia. Arteriosclerosis, Thrombosis, and Vascular Biology, 40:2686-2699, Nov 2020. URL: https://doi.org/10.1161/atvbaha.119.313885, doi:10.1161/atvbaha.119.313885. This article has 50 citations and is from a domain leading peer-reviewed journal.

14. (richer2020anovelrecurrent pages 5-7): Julie Richer, Hannah L. Hill, Yu Wang, Min-Lee Yang, Kristina L. Hunker, Jamie Lane, Susan Blackburn, Dawn M. Coleman, Jonathan Eliason, Guillaume Sillon, Maria-Daniela D’Agostino, Prasad Jetty, François-Pierre Mongeon, Anne-Marie Laberge, Stephen E. Ryan, Natalia Fendrikova-Mahlay, Thais Coutinho, Michael R. Mathis, Matthew Zawistowski, Stanley L. Hazen, Alexander E. Katz, Heather L. Gornik, Chad M. Brummett, Goncalo Abecasis, Ingrid L. Bergin, James C. Stanley, Jun Z. Li, and Santhi K. Ganesh. A novel recurrent <i>col5a1</i> genetic variant is associated with a dysplasia-associated arterial disease exhibiting dissections and fibromuscular dysplasia. Arteriosclerosis, Thrombosis, and Vascular Biology, 40:2686-2699, Nov 2020. URL: https://doi.org/10.1161/atvbaha.119.313885, doi:10.1161/atvbaha.119.313885. This article has 50 citations and is from a domain leading peer-reviewed journal.

15. (pappaccogli2023endovascularversusmedical pages 15-20): Marco Pappaccogli, Tom Robberechts, Jean-Philippe Lengelé, Patricia Van der Niepen, Pantelis Sarafidis, Franco Rabbia, and Alexandre Persu. Endovascular versus medical management of atherosclerotic renovascular disease: update and emerging concepts. Hypertension, 80:1150-1161, Jun 2023. URL: https://doi.org/10.1161/hypertensionaha.122.17965, doi:10.1161/hypertensionaha.122.17965. This article has 38 citations and is from a domain leading peer-reviewed journal.

16. (pappaccogli2023endovascularversusmedical pages 32-35): Marco Pappaccogli, Tom Robberechts, Jean-Philippe Lengelé, Patricia Van der Niepen, Pantelis Sarafidis, Franco Rabbia, and Alexandre Persu. Endovascular versus medical management of atherosclerotic renovascular disease: update and emerging concepts. Hypertension, 80:1150-1161, Jun 2023. URL: https://doi.org/10.1161/hypertensionaha.122.17965, doi:10.1161/hypertensionaha.122.17965. This article has 38 citations and is from a domain leading peer-reviewed journal.

17. (richer2020anovelrecurrent pages 7-8): Julie Richer, Hannah L. Hill, Yu Wang, Min-Lee Yang, Kristina L. Hunker, Jamie Lane, Susan Blackburn, Dawn M. Coleman, Jonathan Eliason, Guillaume Sillon, Maria-Daniela D’Agostino, Prasad Jetty, François-Pierre Mongeon, Anne-Marie Laberge, Stephen E. Ryan, Natalia Fendrikova-Mahlay, Thais Coutinho, Michael R. Mathis, Matthew Zawistowski, Stanley L. Hazen, Alexander E. Katz, Heather L. Gornik, Chad M. Brummett, Goncalo Abecasis, Ingrid L. Bergin, James C. Stanley, Jun Z. Li, and Santhi K. Ganesh. A novel recurrent <i>col5a1</i> genetic variant is associated with a dysplasia-associated arterial disease exhibiting dissections and fibromuscular dysplasia. Arteriosclerosis, Thrombosis, and Vascular Biology, 40:2686-2699, Nov 2020. URL: https://doi.org/10.1161/atvbaha.119.313885, doi:10.1161/atvbaha.119.313885. This article has 50 citations and is from a domain leading peer-reviewed journal.

18. (piechocki2024…peripheral pages 13-15): M Piechocki, T Przewłocki, and P Pieniążek. … , peripheral arterial atherosclerotic disease (carotid, renal, lower limb) in elderly patients—a review: part i—epidemiology, risk factors, and atherosclerosis …. Unknown journal, 2024.

19. (NCT06822205 chunk 1):  Identification and Treatment of Renal Stenosis in Transplanted Kidneys. IRCCS Azienda Ospedaliero-Universitaria di Bologna. 2023. ClinicalTrials.gov Identifier: NCT06822205

20. (NCT05603221 chunk 1):  Renal Perfusion Assessment in the Endovascular Treatment of Renal Artery Stenosis. Peking Union Medical College Hospital. 2020. ClinicalTrials.gov Identifier: NCT05603221

21. (cooper2014stentingandmedical pages 8-9): Christopher J. Cooper, Timothy P. Murphy, Donald E. Cutlip, Kenneth Jamerson, William Henrich, Diane M. Reid, David J. Cohen, Alan H. Matsumoto, Michael Steffes, Michael R. Jaff, Martin R. Prince, Eldrin F. Lewis, Katherine R. Tuttle, Joseph I. Shapiro, John H. Rundback, Joseph M. Massaro, Ralph B. D'Agostino, and Lance D. Dworkin. Stenting and medical therapy for atherosclerotic renal-artery stenosis. The New England journal of medicine, 370 1:13-22, Jan 2014. URL: https://doi.org/10.1056/nejmoa1310753, doi:10.1056/nejmoa1310753. This article has 1274 citations and is from a highest quality peer-reviewed journal.

22. (pappaccogli2023endovascularversusmedical pages 12-15): Marco Pappaccogli, Tom Robberechts, Jean-Philippe Lengelé, Patricia Van der Niepen, Pantelis Sarafidis, Franco Rabbia, and Alexandre Persu. Endovascular versus medical management of atherosclerotic renovascular disease: update and emerging concepts. Hypertension, 80:1150-1161, Jun 2023. URL: https://doi.org/10.1161/hypertensionaha.122.17965, doi:10.1161/hypertensionaha.122.17965. This article has 38 citations and is from a domain leading peer-reviewed journal.

23. (richer2020anovelrecurrent pages 12-13): Julie Richer, Hannah L. Hill, Yu Wang, Min-Lee Yang, Kristina L. Hunker, Jamie Lane, Susan Blackburn, Dawn M. Coleman, Jonathan Eliason, Guillaume Sillon, Maria-Daniela D’Agostino, Prasad Jetty, François-Pierre Mongeon, Anne-Marie Laberge, Stephen E. Ryan, Natalia Fendrikova-Mahlay, Thais Coutinho, Michael R. Mathis, Matthew Zawistowski, Stanley L. Hazen, Alexander E. Katz, Heather L. Gornik, Chad M. Brummett, Goncalo Abecasis, Ingrid L. Bergin, James C. Stanley, Jun Z. Li, and Santhi K. Ganesh. A novel recurrent <i>col5a1</i> genetic variant is associated with a dysplasia-associated arterial disease exhibiting dissections and fibromuscular dysplasia. Arteriosclerosis, Thrombosis, and Vascular Biology, 40:2686-2699, Nov 2020. URL: https://doi.org/10.1161/atvbaha.119.313885, doi:10.1161/atvbaha.119.313885. This article has 50 citations and is from a domain leading peer-reviewed journal.

24. (pappaccogli2023endovascularversusmedical media 2c3b7fe8): Marco Pappaccogli, Tom Robberechts, Jean-Philippe Lengelé, Patricia Van der Niepen, Pantelis Sarafidis, Franco Rabbia, and Alexandre Persu. Endovascular versus medical management of atherosclerotic renovascular disease: update and emerging concepts. Hypertension, 80:1150-1161, Jun 2023. URL: https://doi.org/10.1161/hypertensionaha.122.17965, doi:10.1161/hypertensionaha.122.17965. This article has 38 citations and is from a domain leading peer-reviewed journal.

25. (pappaccogli2023endovascularversusmedical media affaa2a8): Marco Pappaccogli, Tom Robberechts, Jean-Philippe Lengelé, Patricia Van der Niepen, Pantelis Sarafidis, Franco Rabbia, and Alexandre Persu. Endovascular versus medical management of atherosclerotic renovascular disease: update and emerging concepts. Hypertension, 80:1150-1161, Jun 2023. URL: https://doi.org/10.1161/hypertensionaha.122.17965, doi:10.1161/hypertensionaha.122.17965. This article has 38 citations and is from a domain leading peer-reviewed journal.