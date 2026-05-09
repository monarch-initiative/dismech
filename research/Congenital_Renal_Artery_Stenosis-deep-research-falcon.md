---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-05T11:40:56.092833'
end_time: '2026-05-05T11:55:45.009515'
duration_seconds: 888.92
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Congenital Renal Artery Stenosis
  mondo_id: ''
  category: Congenital
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
- **Disease Name:** Congenital Renal Artery Stenosis
- **MONDO ID:**  (if available)
- **Category:** Congenital

## Research Objectives

Please provide a comprehensive research report on **Congenital Renal Artery Stenosis** covering all of the
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
- **Disease Name:** Congenital Renal Artery Stenosis
- **MONDO ID:**  (if available)
- **Category:** Congenital

## Research Objectives

Please provide a comprehensive research report on **Congenital Renal Artery Stenosis** covering all of the
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


# Comprehensive Disease Characteristics Report: Congenital Renal Artery Stenosis (CRAS)

## Executive summary
Congenital/pediatric renal artery stenosis (RAS) is a narrowing of the renal artery(ies) present from birth or developing in childhood, often manifesting as renovascular hypertension (RVH). The central pathophysiologic concept is reduced renal perfusion, which activates the renin–angiotensin–aldosterone system (RAAS) and drives severe or refractory hypertension, with risk of end-organ injury (kidney atrophy/CKD, cardiac remodeling/heart failure, cerebrovascular complications). In modern pediatric practice, digital subtraction angiography (catheter angiography) remains the diagnostic gold standard, while percutaneous transluminal renal angioplasty (PTRA) is a common first-line revascularization strategy in appropriately selected children; outcomes vary by etiology, and restenosis/reintervention is frequent in complex arteriopathies and mid-aortic syndrome (MAS). (goyal2023pediatricrenovascularhypertension pages 1-2, persu2021beyondatherosclerosisand pages 4-5, pytlos2024renalarterystenosis pages 12-14, redhead2024cardiovascularoutcomesimprove pages 1-2)

## Evidence quick reference (curated)
| Domain | Key finding | Value / statistic | Population / context | Citation |
|---|---|---:|---|---|
| Disease term / definition | Pediatric renal artery stenosis (RAS) | Narrowing of the renal arteries | Children with renovascular disease/hypertension | (pytlos2024renalarterystenosis pages 1-2) |
| Disease term / definition | Mid-aortic syndrome (MAS) | Stenosis of the abdominal aorta with branch involvement (“abdominal coarctation”) | Pediatric MAS often coexists with renal artery disease | (pytlos2024renalarterystenosis pages 1-2) |
| Epidemiology | Pediatric arterial hypertension prevalence | ~4% | General pediatric population | (pytlos2024renalarterystenosis pages 1-2) |
| Epidemiology | Renovascular disease among secondary pediatric hypertension | 5–10% | Childhood secondary hypertension | (pytlos2024renalarterystenosis pages 1-2, peco‐antic2016associatedextrarenalvascular pages 4-5) |
| Epidemiology | RVH among pediatric hypertension | Up to 10% | Pediatric hypertension overall | (goyal2023pediatricrenovascularhypertension pages 1-2) |
| Epidemiology | RVH among secondary pediatric hypertension etiologies | Close to one-fourth | Secondary causes of childhood hypertension | (goyal2023pediatricrenovascularhypertension pages 1-2) |
| Epidemiology | Incidence of pediatric RVH/RAS | 1.9 per million children/year | 25 cases over 13 years in hospitals serving ~1 million children | (peco‐antic2016associatedextrarenalvascular pages 4-5) |
| Epidemiology | MAS among aortic stenosis/coarctation cases | 0.5–2% | Rare pediatric vascular disorder | (pytlos2024renalarterystenosis pages 1-2) |
| Epidemiology | Children with RVH who also have renal-artery plus mid-aortic narrowing | 20–48% | Pediatric renovascular hypertension cohorts | (pytlos2024renalarterystenosis pages 1-2) |
| Etiology | Isolated/congenital developmental lesions | Congenital hypoplasia/deficiency and focal congenital stenosis described | Rare, often grouped with non-inflammatory pediatric RAS | (pytlos2024renalarterystenosis pages 1-2, goyal2023pediatricrenovascularhypertension pages 1-2) |
| Etiology | Fibromuscular dysplasia (FMD) | Major contributor to pediatric RAS in North America/Europe | Generalized non-inflammatory arteriopathy; commonest cause in developed settings | (pytlos2024renalarterystenosis pages 2-4, goyal2023pediatricrenovascularhypertension pages 1-2) |
| Etiology | Neurofibromatosis type 1 (NF1) | 12% of one pediatric RVH/RAS cohort; 17.1% of MAS families had NF1 mutations | Syndromic/monogenic pediatric renovascular disease | (peco‐antic2016associatedextrarenalvascular pages 4-5, warejko2018wholeexomesequencing pages 3-5) |
| Etiology | Williams syndrome / ELN / del(7q11.23) | Prevalence ~1 in 10,000; ELN/Williams deletions in 3/35 MAS families (8.6%) | Syndromic vascular stenosis with renal artery involvement | (persu2021beyondatherosclerosisand pages 4-5, warejko2018wholeexomesequencing pages 3-5) |
| Etiology | Alagille syndrome / JAG1 | JAG1 in 4/35 MAS families (11.4%) | Syndromic MAS/RAS; often progressive vasculopathy | (warejko2018wholeexomesequencing pages 3-5, persu2021beyondatherosclerosisand pages 4-5) |
| Etiology | Takayasu arteritis | Cause of pediatric RAS in some regional series: 73–89%; incidence 1–2/million/year in Europe/North America | Inflammatory large-vessel cause; more common in Asian/African settings | (pytlos2024renalarterystenosis pages 2-4, goyal2023pediatricrenovascularhypertension pages 1-2) |
| Etiology | Monogenic contribution to MAS | ~43% of 35 families | Whole-exome sequencing in pediatric MAS | (warejko2018wholeexomesequencing pages 5-6, warejko2018wholeexomesequencing pages 1-2) |
| Pathophysiology | Renin–angiotensin–aldosterone system activation | Central mechanism of renovascular hypertension | Renal hypoperfusion from stenosis drives renin-dependent hypertension | (goyal2023pediatricrenovascularhypertension pages 1-2, peco‐antic2016associatedextrarenalvascular pages 4-5) |
| Diagnostics | Duplex Doppler ultrasound findings | Tardus-parvus waveform, decreased peak systolic velocity; absent intrarenal flow in occlusion | Noninvasive screening/triage in pediatric RAS | (persu2021beyondatherosclerosisand pages 11-12) |
| Diagnostics | Cross-sectional angiography | CTA/MRA used; no single screening test is sufficient | Defines anatomy, extent, and associated lesions | (goyal2023pediatricrenovascularhypertension pages 1-2, persu2021beyondatherosclerosisand pages 4-5) |
| Diagnostics | Gold-standard test | Digital subtraction / catheter-based angiography | Definitive diagnosis or formal exclusion of RAS in children | (goyal2023pediatricrenovascularhypertension pages 1-2, persu2021beyondatherosclerosisand pages 4-5, persu2021beyondatherosclerosisand pages 11-12) |
| Treatment / safety | RAAS blockade contraindication | ACEi/ARB absolutely contraindicated | Bilateral RAS or RAS in a solitary kidney due to risk of acute renal failure/volume overload/pulmonary edema | (pytlos2024renalarterystenosis pages 12-14) |
| Treatment / outcomes | PTRA overall cure rate | 36% | Pediatric RAS series summarized in 2024 review | (pytlos2024renalarterystenosis pages 12-14) |
| Treatment / outcomes | PTRA BP improvement beyond cure | Additional 32% improved | Pediatric RAS series summarized in 2024 review | (pytlos2024renalarterystenosis pages 12-14) |
| Treatment / outcomes | Etiology-specific response to intervention | >50% idiopathic RAS; 36% FMD; 80% Takayasu; 71% NF1 | Pediatric endovascular outcomes by cause | (pytlos2024renalarterystenosis pages 12-14) |
| Treatment / outcomes | Restenosis after PTA | Up to 44% | Pediatric focal stenotic lesions/syndromic disease | (persu2021beyondatherosclerosisand pages 4-5) |
| Treatment / outcomes | Restenosis after stent placement | 35.5–37% | Pediatric stenting reserved for recoil/occlusion/early recurrence | (pytlos2024renalarterystenosis pages 12-14) |
| Treatment / outcomes | BP control after endovascular ± surgical intervention | 54.4% achieved BP control; 21.3% discontinued all antihypertensives; 45.9% reduced medications | 152 children in longitudinal observational study | (redhead2024cardiovascularoutcomesimprove pages 9-10) |
| Treatment / outcomes | MAS angioplasty burden | Angioplasty occurrence ~28%; reintervention up to 67% at 5 years | Pediatric MAS has lower durability than focal RAS | (pytlos2024renalarterystenosis pages 12-14) |


*Table: This table condenses the most actionable facts for congenital/pediatric renal artery stenosis and related renovascular hypertension, including definitions, epidemiology, etiologies, diagnostics, and treatment outcomes. It is useful as a quick-reference evidence summary with context-specific statistics and supporting citation IDs.*

## 1. Disease information
### 1.1 Definition and overview
* **Pediatric renal artery stenosis (RAS)** is defined as **narrowing of the renal arteries** and is an important cause of pediatric renovascular hypertension. (pytlos2024renalarterystenosis pages 1-2)
* **Middle aortic syndrome (MAS)** (also called **abdominal aortic coarctation / abdominal coarctation**) is defined as stenosis of the abdominal aorta with involvement of renal/visceral branches and is a key congenital/pediatric context in which RAS occurs. (pytlos2024renalarterystenosis pages 1-2)

### 1.2 Key identifiers (OMIM/Orphanet/ICD/MeSH/MONDO)
* **Limitation of current tool-retrieved corpus:** authoritative ontology identifiers (MONDO ID, MeSH descriptor/ID, ICD-10/ICD-11 codes, Orphanet, OMIM) specific to **“congenital renal artery stenosis”** were **not directly retrievable** from the available full-text evidence captured in this run. This report therefore provides evidence-based clinical definitions and syndromic genetic identifiers at the gene/syndrome level (e.g., NF1, ELN/Williams-Beuren, JAG1/Alagille), but cannot reliably populate a MONDO/MeSH/ICD mapping without additional database-specific retrieval. (pytlos2024renalarterystenosis pages 1-2, warejko2018wholeexomesequencing pages 3-5, coleman2022moleculargeneticevaluation pages 1-2)

### 1.3 Synonyms and alternative names (commonly used)
Common overlapping terms used in the literature include:
* **Renovascular hypertension (RVH)** in children (clinical syndrome of hypertension due to renovascular lesions) (goyal2023pediatricrenovascularhypertension pages 1-2)
* **Renal artery stenosis (RAS)** (pytlos2024renalarterystenosis pages 1-2)
* **Mid-aortic syndrome (MAS)** / **abdominal aortic coarctation** (pytlos2024renalarterystenosis pages 1-2)

### 1.4 Evidence source type (patient-level vs aggregated)
Most evidence for pediatric/congenital RAS is derived from:
* **Observational cohorts/series** (e.g., 152-child longitudinal cohort with echo follow-up after interventions) (redhead2024cardiovascularoutcomesimprove pages 1-2)
* **Retrospective pediatric series** (e.g., 25 cases over 13 years in a defined pediatric catchment) (peco‐antic2016associatedextrarenalvascular pages 4-5)
* **Systematic/structured reviews** synthesizing pediatric RAS/MAS data (pytlos2024renalarterystenosis pages 1-2, pytlos2024renalarterystenosis pages 12-14)
* **Genomic cohort studies** (e.g., WES in MAS families; NF1-focused molecular profiling of stenotic arteries) (warejko2018wholeexomesequencing pages 1-2, coleman2022moleculargeneticevaluation pages 1-2)

## 2. Etiology
### 2.1 Disease causal factors (current understanding)
Pediatric/congenital RAS is etiologically heterogeneous and can be classified into:
* **Non-inflammatory arteriopathies**: particularly **fibromuscular dysplasia (FMD)**, described as a major contributor to pediatric RAS in North America/Europe. (pytlos2024renalarterystenosis pages 2-4)
* **Inflammatory large-vessel vasculitis**: notably **Takayasu arteritis**, which is regionally prevalent in some pediatric series. (goyal2023pediatricrenovascularhypertension pages 1-2, pytlos2024renalarterystenosis pages 2-4)
* **Syndromic/genetic causes**: especially **neurofibromatosis type 1 (NF1)**, **Williams–Beuren syndrome (WBS; ELN region deletion)**, and **Alagille syndrome (JAG1/NOTCH pathway)**. (persu2021beyondatherosclerosisand pages 4-5, warejko2018wholeexomesequencing pages 3-5)
* **Anatomic distribution phenotypes**: focal stenosis vs multifocal disease; MAS is a congenital or acquired narrowing of the abdominal aorta often involving renal arteries. (goyal2023pediatricrenovascularhypertension pages 1-2, pytlos2024renalarterystenosis pages 1-2)

### 2.2 Risk factors
**Genetic/syndromic risk factors (monogenic contributors):**
* **MAS has a high monogenic yield** by whole-exome sequencing (WES): likely causal dominant mutations were found in **15/35 families (≈42.9%)**, involving **NF1, JAG1, ELN, GATA6, RNF213**. (warejko2018wholeexomesequencing pages 1-2)
* In the same MAS cohort, the most frequent gene was **NF1 (6/35 families; 17.1%)**, followed by **JAG1 (4/35; 11.4%)** and **ELN (3/35; 8.6%)**. (warejko2018wholeexomesequencing pages 3-5)

**Clinical epidemiologic risk context:**
* In one pediatric RVH/RAS cohort, **NF1 accounted for 12%** of cases. (peco‐antic2016associatedextrarenalvascular pages 4-5)

**Population/region-dependent etiologic spectrum:**
* A 2023 pediatric interventional radiology review notes that **FMD** is commonly reported in developed countries, whereas **Takayasu arteritis** is more common in parts of Asia/Africa. (goyal2023pediatricrenovascularhypertension pages 1-2)

### 2.3 Protective factors
No specific **protective genetic variants** or **environmental protective factors** for congenital/pediatric RAS were identified in the retrieved evidence set.

### 2.4 Gene–environment interactions
No gene–environment interaction studies specific to congenital/pediatric RAS were identified in the retrieved evidence set.

## 3. Phenotypes
### 3.1 Core clinical phenotype spectrum
Pediatric RAS/RVH may be clinically silent and detected only by blood pressure measurement; a pediatric cohort reported **~1/3 asymptomatic despite severe hypertension**, highlighting the importance of screening/measurement rather than symptom-driven diagnosis. (peco‐antic2016associatedextrarenalvascular pages 4-5, goyal2023pediatricrenovascularhypertension pages 1-2)

Key phenotype mappings to HPO terms are provided below.

| Phenotype / finding | Type | Suggested HPO term | HPO ID | Typical onset | Frequency / notes | Key citation(s) |
|---|---|---|---|---|---|---|
| Severe hypertension | Clinical sign | Severe systemic arterial hypertension | HP:0004970 | Childhood | Core presentation of pediatric renovascular hypertension; may be clinically silent, with elevated BP as the sole manifestation in some children; about one-third of children in one cohort were asymptomatic despite severe hypertension | (goyal2023pediatricrenovascularhypertension pages 1-2, peco‐antic2016associatedextrarenalvascular pages 4-5) |
| Headache | Symptom | Headache | HP:0002315 | Childhood | Common symptom of severe hypertension; pediatric NF1-associated RAS case presented with long-standing headache | (goyal2023pediatricrenovascularhypertension pages 1-2) |
| Abdominal bruit | Clinical sign | Abdominal bruit | HP:0031881 | Childhood | Supportive bedside clue in renovascular disease; highlighted in pediatric/syndromic RVH discussions | (persu2021beyondatherosclerosisand pages 1-2) |
| Left ventricular hypertrophy / cardiac remodeling | Imaging / cardiac phenotype | Left ventricular hypertrophy | HP:0001712 | Childhood | Cardiac remodeling occurs secondary to RAAS-driven hypertension; in a 152-patient cohort, IVSD, PWD, LVMI, RWT and FS improved after intervention; 6 children presented in heart failure | (redhead2024cardiovascularoutcomesimprove pages 1-2, redhead2024cardiovascularoutcomesimprove pages 9-10) |
| Heart failure | Clinical complication | Congestive heart failure | HP:0001635 | Childhood | Uncommon but important severe presentation; 6/152 children in the 2024 longitudinal cohort presented in heart failure | (redhead2024cardiovascularoutcomesimprove pages 1-2) |
| Kidney atrophy / small kidney | Imaging finding | Small kidney | HP:0000089 | Childhood | Reflects chronic renal hypoperfusion; may accompany unilateral stenosis/hypoplasia and progressive disease | (persu2021beyondatherosclerosisand pages 4-5, persu2021beyondatherosclerosisand pages 11-12) |
| Decreased glomerular filtration rate | Laboratory abnormality | Decreased glomerular filtration rate | HP:0012213 | Childhood | Reported especially in progressive syndromic disease such as Alagille-associated renovascular disease | (persu2021beyondatherosclerosisand pages 4-5) |
| Proteinuria | Laboratory abnormality | Proteinuria | HP:0000093 | Childhood | Can accompany RAAS activation and hyponatremic hypertensive syndrome in severe renovascular hypertension | (peco‐antic2016associatedextrarenalvascular pages 4-5) |
| Hyponatremic hypertensive syndrome | Laboratory / clinical syndrome | Hyponatremia; Polyuria; Proteinuria | HP:0002902; HP:0000103; HP:0000093 | Childhood | Severe RAAS activation may produce hyponatremic hypertensive syndrome with polyuria, electrolyte loss, and proteinuria | (peco‐antic2016associatedextrarenalvascular pages 4-5) |
| Bilateral renal artery stenosis | Imaging / vascular phenotype | Bilateral renal artery stenosis | HP:0012723 | Childhood / congenital | Reported in 24–78% of pediatric series; bilateral disease is clinically important because ACEi/ARB therapy is contraindicated in bilateral RAS or solitary-kidney RAS | (goyal2023pediatricrenovascularhypertension pages 1-2, pytlos2024renalarterystenosis pages 12-14) |
| Midaortic syndrome / abdominal aortic coarctation | Imaging / vascular phenotype | Abdominal aortic coarctation | HP:0002626 | Congenital / childhood | MAS is a rare but important cause of severe childhood hypertension; 20–48% of children with renovascular hypertension may have combined renal-artery and mid-aortic narrowing | (pytlos2024renalarterystenosis pages 1-2, pytlos2024renalarterystenosis pages 2-4) |
| Weak femoral pulses / upper-lower extremity BP gradient | Clinical sign | Decreased femoral pulse; Systolic blood pressure difference between upper and lower limbs | HP:0030971; HP:0033279 | Childhood | Suggestive of midaortic syndrome; described with weak femoral pulses and BP gradient between upper and lower extremities | (persu2021beyondatherosclerosisand pages 4-5) |
| Tardus-parvus intrarenal waveform / reduced peak systolic velocity | Imaging finding | Abnormal renal artery Doppler ultrasound | HP:0034059 | Childhood | Characteristic Doppler clue to hemodynamically significant stenosis; complete occlusion may show absent intrarenal flow | (persu2021beyondatherosclerosisand pages 11-12) |
| Absence of symptoms despite severe disease | Clinical course | Asymptomatic hypertension | HP:0000007 | Childhood | About one-third of children in one cohort remained asymptomatic despite severe hypertension, underscoring screening importance | (peco‐antic2016associatedextrarenalvascular pages 4-5) |


*Table: This table maps major pediatric/congenital renal artery stenosis and renovascular hypertension findings to suggested HPO terms, with onset and frequency notes where reported. It is useful for knowledge-base curation of phenotype annotations and evidence-backed clinical features.*

### 3.2 Frequency/severity/progression (selected quantitative data)
* **Bilateral RAS** is common in pediatric series (**24–78%** reported). (goyal2023pediatricrenovascularhypertension pages 1-2)
* Pediatric RVH can cause **cardiac remodeling**; in a 152-patient cohort, 6 children presented in heart failure, and multiple echocardiographic indices improved following intervention. (redhead2024cardiovascularoutcomesimprove pages 1-2)

### 3.3 Quality of life impact
Direct patient-reported outcome measures (e.g., PedsQL, PROMIS) were not identified in the retrieved sources. Indirectly, severe hypertension and need for repeated procedures/medications imply substantial burden. (pytlos2024renalarterystenosis pages 12-14, redhead2024cardiovascularoutcomesimprove pages 1-2)

## 4. Genetic / molecular information
### 4.1 Causal genes and syndromes (strongly supported)
**NF1 (neurofibromatosis type 1)**
* In a prospective cohort of 102 pediatric RVH patients with RAS ± abdominal aortic coarctation, **13 (12.5%)** had clinical NF1. (coleman2022moleculargeneticevaluation pages 1-2)

**JAG1 (Alagille syndrome)**
* JAG1 truncating variants were identified in multiple families with syndromic MAS in WES-based studies. (warejko2018wholeexomesequencing pages 5-6, warejko2018wholeexomesequencing pages 1-2)

**ELN region (Williams–Beuren syndrome; 7q11.23 deletion)**
* WES/CNV analysis in MAS families identified ELN/Williams-related deletions in a subset (3/35 families). (warejko2018wholeexomesequencing pages 3-5, warejko2018wholeexomesequencing pages 1-2)

**Additional monogenic genes reported in MAS WES cohorts**
* **GATA6** and **RNF213** were each identified in single MAS families in the WES study. (warejko2018wholeexomesequencing pages 1-2)

### 4.2 Pathogenic variants (examples, where available in evidence)
The MAS WES study reported a range of **NF1 variant types** (missense, splice-site, frameshift, truncating) and provided specific examples (e.g., c.1166A>G p.H389R; c.1260+5G>A; c.3457_3460del p.L1153Mfs*4). (warejko2018wholeexomesequencing pages 3-5)

### 4.3 Molecular mechanisms (authoritative mechanistic evidence)
**NF1 vasculopathy (human lesion ‘omics’ + histology):**
* Human stenotic renal arteries in NF1 show a consistent remodeling pattern (intimal thickening, disrupted internal elastic lamina, medial thinning) and transcriptomic evidence of NF1 haploinsufficiency and inflammatory/proliferative signaling: approximately **5-fold reduction in NF1 expression**, **MAPK pathway activation**, and **increased MCP1**. (coleman2022moleculargeneticevaluation pages 1-2)
* Immunostaining demonstrated markedly increased **pERK1** (Ras–MAPK pathway activity) in NF1 stenotic artery tissue. (coleman2022moleculargeneticevaluation pages 8-9)

**Causal chain (NF1 example):** germline NF1 variant → neurofibromin haploinsufficiency → Ras–MAPK activation + MCP1/CCR2-mediated monocyte recruitment and vascular smooth muscle proliferative responses → neointimal hyperplasia and arterial remodeling → renal hypoperfusion → RAAS activation → severe hypertension and downstream end-organ injury. (coleman2022moleculargeneticevaluation pages 8-9, redhead2024cardiovascularoutcomesimprove pages 1-2)

### 4.4 Epigenetics, modifier genes, and molecular profiling beyond NF1
No disease-specific epigenetic studies or multi-omics signatures (beyond NF1 arterial RNA-Seq in the retrieved corpus) were identified.

## 5. Environmental information
Congenital RAS is primarily developmental/genetic/structural in the retrieved sources. Environmental contributors (toxins, lifestyle) and infectious agents were not identified as primary causes in the retrieved evidence set.

## 6. Mechanism / pathophysiology
### 6.1 RAAS-driven renovascular hypertension
A central mechanistic statement supported in the pediatric literature is that renal artery stenosis reduces renal perfusion, activates the RAAS axis, and can drive severe hypertension and cardiac remodeling. (redhead2024cardiovascularoutcomesimprove pages 1-2, goyal2023pediatricrenovascularhypertension pages 1-2)

### 6.2 Suggested ontology mappings
**GO Biological Process (suggested):**
* renin secretion / renin-angiotensin system regulation
* regulation of systemic arterial blood pressure
* vascular smooth muscle cell proliferation
* inflammatory cell chemotaxis (monocyte chemotaxis)

**Cell Ontology (CL) (suggested):**
* vascular smooth muscle cell
* endothelial cell
* monocyte / macrophage (CCR2+ inflammatory monocyte subset conceptually relevant)

These are suggested based on the described mechanisms (RAAS activation; VSMC proliferation; MCP1/CCR2 monocyte infiltration) rather than explicitly enumerated ontology IDs in the retrieved papers. (coleman2022moleculargeneticevaluation pages 8-9, redhead2024cardiovascularoutcomesimprove pages 1-2)

## 7. Anatomical structures affected
**Organ/system level:**
* **Kidney** (renal parenchyma ischemia, atrophy) and **renal arteries** (primary lesion). (pytlos2024renalarterystenosis pages 1-2, persu2021beyondatherosclerosisand pages 11-12)
* **Cardiovascular system** (hypertension-related cardiac remodeling; sometimes heart failure). (redhead2024cardiovascularoutcomesimprove pages 1-2)
* **Aorta and branch vessels** in MAS (abdominal aorta, renal and visceral branch ostia). (pytlos2024renalarterystenosis pages 1-2)

**UBERON suggestions (non-exhaustive):** kidney; renal artery; abdominal aorta; heart left ventricle.

**Lateralization:**
* Both unilateral and bilateral disease occurs; bilateral stenosis can be common. (goyal2023pediatricrenovascularhypertension pages 1-2)

## 8. Temporal development
* **Onset:** congenital/childhood (by definition), often detected during childhood BP screening or workup for severe hypertension. (goyal2023pediatricrenovascularhypertension pages 1-2, pytlos2024renalarterystenosis pages 1-2)
* **Progression:** etiology-dependent; syndromic arteriopathies (e.g., NF1) can be progressive with recurrence/restenosis after intervention. (persu2021beyondatherosclerosisand pages 4-5)

## 9. Inheritance and population
### 9.1 Epidemiology (quantitative data available)
* **Childhood arterial hypertension prevalence:** ~4%. (pytlos2024renalarterystenosis pages 1-2)
* **Renovascular disease contribution:** 5–10% of secondary pediatric hypertension. (pytlos2024renalarterystenosis pages 1-2, peco‐antic2016associatedextrarenalvascular pages 4-5)
* **Incidence estimate (regional cohort):** 25 pediatric RVH/RAS cases over 13 years in hospitals serving ~1 million children → **~1.9 per million children/year**. (peco‐antic2016associatedextrarenalvascular pages 4-5)
* **MAS rarity:** ~0.5–2% of aortic stenosis cases; among pediatric RVH cohorts, **20–48%** may have combined renal artery plus mid-aortic narrowing. (pytlos2024renalarterystenosis pages 1-2)

### 9.2 Inheritance patterns (genetic etiologies)
* MAS WES findings support primarily **autosomal dominant** monogenic contributors (e.g., NF1, JAG1, ELN), with variable expressivity and syndromic vs isolated presentations. (warejko2018wholeexomesequencing pages 3-5, warejko2018wholeexomesequencing pages 1-2)
* NF1 variants in the NF1-RVH cohort were often novel; de novo variants were reported as common (about half in that cohort per extracted summary). (coleman2022moleculargeneticevaluation pages 7-8)

## 10. Diagnostics
### 10.1 Imaging and diagnostic strategy
* **No single screening test is uniformly accurate** for pediatric RVH; noninvasive imaging (ultrasound/CTA/MRA) is used for screening and anatomical definition. (goyal2023pediatricrenovascularhypertension pages 1-2, persu2021beyondatherosclerosisand pages 4-5)
* **Digital subtraction/catheter angiography** is repeatedly emphasized as the **diagnostic gold standard** for pediatric RVH/RAS and for definitive exclusion/confirmation. (goyal2023pediatricrenovascularhypertension pages 1-2, persu2021beyondatherosclerosisand pages 4-5, persu2021beyondatherosclerosisand pages 11-12)
* **Duplex Doppler ultrasound clues** include **tardus–parvus** waveforms and changes in peak systolic velocity; complete occlusion can show absent intrarenal flow. (persu2021beyondatherosclerosisand pages 11-12)

### 10.2 Differential diagnosis (etiologic breadth)
Differential includes non-inflammatory arteriopathies (FMD), vasculitis (Takayasu), syndromic vascular disease (NF1, WBS, Alagille), thromboembolism/catheter-related injury, extrinsic compression, trauma/radiation, and MAS. (pytlos2024renalarterystenosis pages 2-4, pytlos2024renalarterystenosis pages 1-2)

### 10.3 Genetic testing
For syndromic/diffuse disease and MAS phenotypes, reviews recommend evaluation for extrarenal involvement and referral for genetic evaluation/testing. (pytlos2024renalarterystenosis pages 2-4)

## 11. Outcome / prognosis
### 11.1 Blood pressure and cardiovascular outcomes after intervention
A 2024 longitudinal pediatric cohort (152 children with RVH undergoing ≥1 endovascular intervention, some with surgery) reported:
* **BP control achieved in 54.4%** post-intervention
* **45.9%** reduced antihypertensive medications
* **21.3%** discontinued all antihypertensive therapy
* Improvement in multiple echocardiographic parameters consistent with **reversal/improvement of cardiac remodeling**. (redhead2024cardiovascularoutcomesimprove pages 1-2)

### 11.2 Restenosis and reintervention
* Restenosis after PTA has been reported in up to **44%**. (persu2021beyondatherosclerosisand pages 4-5)
* For pediatric stenting (reserved indications), restenosis rates in summarized series were **~35.5–37%**. (pytlos2024renalarterystenosis pages 12-14)
* In MAS, reintervention burden is high (reintervention up to **67% at 5 years** in summarized data). (pytlos2024renalarterystenosis pages 12-14)

## 12. Treatment
### 12.1 Medical therapy
Children often require multi-drug antihypertensive therapy; however, medical therapy alone may be insufficient for durable BP control in anatomic lesions. (pytlos2024renalarterystenosis pages 1-2, pytlos2024renalarterystenosis pages 12-14)

**Critical safety constraint (RAAS blockade):**
* ACE inhibitors/ARBs are **absolutely contraindicated** in **bilateral RAS or RAS in a solitary kidney** due to risk of acute renal failure/volume overload/pulmonary edema. (pytlos2024renalarterystenosis pages 12-14)

### 12.2 Endovascular and surgical interventions (real-world implementation)
* **Angioplasty (PTRA)** is commonly described as the **treatment of choice** in selected pediatric patients; surgery is reserved for complex anatomy or failed endovascular approaches. (goyal2023pediatricrenovascularhypertension pages 1-2, persu2021beyondatherosclerosisand pages 4-5)

**Effectiveness (quantitative):**
* In a 2024 pediatric review synthesis, PTRA showed an **overall cure rate of 36%** and **BP improvement in an additional 32%**, with etiology-specific differences (e.g., higher success in Takayasu arteritis and NF1 than FMD in the summarized series). (pytlos2024renalarterystenosis pages 12-14)

### 12.3 MAXO (Medical Action Ontology) suggestions
* Percutaneous transluminal angioplasty
* Vascular stent placement
* Surgical vascular reconstruction / bypass
* Antihypertensive drug therapy
* Aspirin antiplatelet therapy / peri-procedural anticoagulation

These MAXO actions are suggested based on interventions described in pediatric reviews and cohorts. (goyal2023pediatricrenovascularhypertension pages 1-2, pytlos2024renalarterystenosis pages 12-14, redhead2024cardiovascularoutcomesimprove pages 1-2)

### 12.4 Trials
No pediatric congenital RAS-specific interventional clinical trials with extractable NCT identifiers were identified via the clinical trials search in this run.

## 13. Prevention
Primary prevention is generally not applicable for congenital developmental lesions. Secondary/tertiary prevention in practice consists of:
* routine pediatric BP measurement to avoid delayed diagnosis (given frequent asymptomatic presentation) (peco‐antic2016associatedextrarenalvascular pages 4-5)
* early imaging workup when RVH is suspected (goyal2023pediatricrenovascularhypertension pages 1-2)
* long-term surveillance for recurrence/restenosis in progressive syndromic vasculopathies (e.g., NF1) (persu2021beyondatherosclerosisand pages 4-5)

## 14. Other species / natural disease
No naturally occurring veterinary analogs or cross-species epidemiology were identified in the retrieved evidence set.

## 15. Model organisms
Mechanistic support for NF1 arteriopathy includes mouse model evidence implicating monocyte/macrophage lineage Nf1 haploinsufficiency, CCR2/MCP1-mediated inflammatory recruitment, and neointimal hyperplasia (as summarized within the NF1 molecular study). (coleman2022moleculargeneticevaluation pages 8-9)

## Recent developments and “latest research” emphasis (2023–2024)
Key 2023–2024 contributions in the retrieved set include:
* A 2023 pediatric interventional radiology perspective emphasizing that pediatric RVH is often silent, angiography remains gold standard, and angioplasty is a key therapy within multidisciplinary care. Publication date: **Aug 2023**. URL: https://doi.org/10.1055/s-0043-1772496 (goyal2023pediatricrenovascularhypertension pages 1-2)
* A 2024 pediatric cohort demonstrating measurable **improvement in cardiac remodeling** and medication reduction after endovascular ± surgical intervention, with **54.4% BP control**. Publication date: **Sep 2024** (online earlier per DOI record). URL: https://doi.org/10.1007/s00467-023-06123-5 (redhead2024cardiovascularoutcomesimprove pages 1-2)
* A 2024 pediatric review summarizing endovascular outcomes (cure/improvement rates, restenosis after stents, and RAAS blockade contraindications in bilateral/solitary kidney RAS). Publication date: **Nov 2024**. URL: https://doi.org/10.3390/jcm13226778 (pytlos2024renalarterystenosis pages 12-14)

## Notes on PMID availability
Several high-value sources in this run are available with DOI and journal metadata, but **PMIDs were not provided in the extracted evidence snippets**; therefore, PMID-based citation is not guaranteed here. URLs/DOIs and publication months/years are included where available.

---

## References (URLs in evidence)
* Pytlos J, et al. *Journal of Clinical Medicine* (Nov 2024). https://doi.org/10.3390/jcm13226778 (pytlos2024renalarterystenosis pages 1-2, pytlos2024renalarterystenosis pages 12-14)
* Redhead ECG, et al. *Pediatric Nephrology* (Sep 2024). https://doi.org/10.1007/s00467-023-06123-5 (redhead2024cardiovascularoutcomesimprove pages 1-2)
* Goyal K, et al. *Indian J Radiol Imaging* (Aug 2023). https://doi.org/10.1055/s-0043-1772496 (goyal2023pediatricrenovascularhypertension pages 1-2)
* Coleman DM, et al. *Human Molecular Genetics* (Sep 2022). https://doi.org/10.1093/hmg/ddab241 (coleman2022moleculargeneticevaluation pages 1-2, coleman2022moleculargeneticevaluation pages 8-9)
* Warejko JK, et al. *Hypertension* (Apr 2018). https://doi.org/10.1161/HYPERTENSIONAHA.117.10296 (warejko2018wholeexomesequencing pages 3-5, warejko2018wholeexomesequencing pages 1-2)
* Persu A, et al. *Hypertension* (Oct 2021). https://doi.org/10.1161/hypertensionaha.121.17004 (persu2021beyondatherosclerosisand pages 4-5, persu2021beyondatherosclerosisand pages 11-12)
* Peco-Antić A, et al. *Acta Paediatrica* (2016). https://doi.org/10.1111/apa.13229 (peco‐antic2016associatedextrarenalvascular pages 4-5)


References

1. (goyal2023pediatricrenovascularhypertension pages 1-2): Kanav Goyal, Taruna Yadav, Pawan Kumar Garg, Pushpinder Khera, Sarbesh Tiwari, and Rengarajan Rajagopal. Pediatric renovascular hypertension: a pediatric interventional radiologist's perspective. Indian Journal of Radiology and Imaging, 33:508-513, Aug 2023. URL: https://doi.org/10.1055/s-0043-1772496, doi:10.1055/s-0043-1772496. This article has 2 citations.

2. (persu2021beyondatherosclerosisand pages 4-5): Alexandre Persu, Caitriona Canning, Aleksander Prejbisz, Piotr Dobrowolski, Laurence Amar, Constantina Chrysochou, Jacek Kądziela, Mieczysław Litwin, Daan van Twist, Patricia Van der Niepen, Gregoire Wuerzner, Peter de Leeuw, Michel Azizi, Magda Januszewicz, and Andrzej Januszewicz. Beyond atherosclerosis and fibromuscular dysplasia: rare causes of renovascular hypertension. Hypertension, 78:898-911, Oct 2021. URL: https://doi.org/10.1161/hypertensionaha.121.17004, doi:10.1161/hypertensionaha.121.17004. This article has 41 citations and is from a domain leading peer-reviewed journal.

3. (pytlos2024renalarterystenosis pages 12-14): Jakub Pytlos, Aneta Michalczewska, Piotr Majcher, Mariusz Furmanek, and Piotr Skrzypczyk. Renal artery stenosis and mid-aortic syndrome in children—a review. Journal of Clinical Medicine, 13:6778, Nov 2024. URL: https://doi.org/10.3390/jcm13226778, doi:10.3390/jcm13226778. This article has 6 citations.

4. (redhead2024cardiovascularoutcomesimprove pages 1-2): Emily C. G. Redhead, Alicia Paessler, Zainab Arslan, Premal Patel, Kishore Minhas, Colin Forman, Paolo Hollis, Sebastiano Lava, Florin Ionescu, Devi Manuel, Samiran Ray, Nicos Kessaris, Alessandro Giardini, Vineetha Ratnamma, Nadine Dobby, Kjell Tullus, Jacob Simmonds, and Jelena Stojanovic. Cardiovascular outcomes improve in children with renovascular hypertension following endovascular and surgical interventions. Pediatric Nephrology (Berlin, Germany), 39:521-530, Sep 2024. URL: https://doi.org/10.1007/s00467-023-06123-5, doi:10.1007/s00467-023-06123-5. This article has 5 citations.

5. (pytlos2024renalarterystenosis pages 1-2): Jakub Pytlos, Aneta Michalczewska, Piotr Majcher, Mariusz Furmanek, and Piotr Skrzypczyk. Renal artery stenosis and mid-aortic syndrome in children—a review. Journal of Clinical Medicine, 13:6778, Nov 2024. URL: https://doi.org/10.3390/jcm13226778, doi:10.3390/jcm13226778. This article has 6 citations.

6. (peco‐antic2016associatedextrarenalvascular pages 4-5): Amira Peco‐Antić, Nataša Stajić, Zoran Krstić, Radovan Bogdanović, Gordana Miloševski‐Lomić, Milan Đukić, and Dušan Paripović. Associated extrarenal vascular diseases may complicate the treatment and outcome of renovascular hypertension. Acta Paediatrica, Jan 2016. URL: https://doi.org/10.1111/apa.13229, doi:10.1111/apa.13229. This article has 10 citations and is from a peer-reviewed journal.

7. (pytlos2024renalarterystenosis pages 2-4): Jakub Pytlos, Aneta Michalczewska, Piotr Majcher, Mariusz Furmanek, and Piotr Skrzypczyk. Renal artery stenosis and mid-aortic syndrome in children—a review. Journal of Clinical Medicine, 13:6778, Nov 2024. URL: https://doi.org/10.3390/jcm13226778, doi:10.3390/jcm13226778. This article has 6 citations.

8. (warejko2018wholeexomesequencing pages 3-5): Jillian K. Warejko, Markus Schueler, Asaf Vivante, Weizhen Tan, Ankana Daga, Jennifer A. Lawson, Daniela A. Braun, Shirlee Shril, Kassaundra Amann, Michael J.G. Somers, Nancy M. Rodig, Michelle A. Baum, Ghaleb Daouk, Avram Z. Traum, Heung Bae Kim, Khashayar Vakili, Diego Porras, James Lock, Michael J. Rivkin, Gulraiz Chaudry, Leslie B. Smoot, Michael N. Singh, Edward R. Smith, Shrikant M. Mane, Richard P. Lifton, Deborah R. Stein, Michael A. Ferguson, and Friedhelm Hildebrandt. Whole exome sequencing reveals a monogenic cause of disease in ≈43% of 35 families with midaortic syndrome. Hypertension, 71:691–699, Apr 2018. URL: https://doi.org/10.1161/hypertensionaha.117.10296, doi:10.1161/hypertensionaha.117.10296. This article has 35 citations and is from a domain leading peer-reviewed journal.

9. (warejko2018wholeexomesequencing pages 5-6): Jillian K. Warejko, Markus Schueler, Asaf Vivante, Weizhen Tan, Ankana Daga, Jennifer A. Lawson, Daniela A. Braun, Shirlee Shril, Kassaundra Amann, Michael J.G. Somers, Nancy M. Rodig, Michelle A. Baum, Ghaleb Daouk, Avram Z. Traum, Heung Bae Kim, Khashayar Vakili, Diego Porras, James Lock, Michael J. Rivkin, Gulraiz Chaudry, Leslie B. Smoot, Michael N. Singh, Edward R. Smith, Shrikant M. Mane, Richard P. Lifton, Deborah R. Stein, Michael A. Ferguson, and Friedhelm Hildebrandt. Whole exome sequencing reveals a monogenic cause of disease in ≈43% of 35 families with midaortic syndrome. Hypertension, 71:691–699, Apr 2018. URL: https://doi.org/10.1161/hypertensionaha.117.10296, doi:10.1161/hypertensionaha.117.10296. This article has 35 citations and is from a domain leading peer-reviewed journal.

10. (warejko2018wholeexomesequencing pages 1-2): Jillian K. Warejko, Markus Schueler, Asaf Vivante, Weizhen Tan, Ankana Daga, Jennifer A. Lawson, Daniela A. Braun, Shirlee Shril, Kassaundra Amann, Michael J.G. Somers, Nancy M. Rodig, Michelle A. Baum, Ghaleb Daouk, Avram Z. Traum, Heung Bae Kim, Khashayar Vakili, Diego Porras, James Lock, Michael J. Rivkin, Gulraiz Chaudry, Leslie B. Smoot, Michael N. Singh, Edward R. Smith, Shrikant M. Mane, Richard P. Lifton, Deborah R. Stein, Michael A. Ferguson, and Friedhelm Hildebrandt. Whole exome sequencing reveals a monogenic cause of disease in ≈43% of 35 families with midaortic syndrome. Hypertension, 71:691–699, Apr 2018. URL: https://doi.org/10.1161/hypertensionaha.117.10296, doi:10.1161/hypertensionaha.117.10296. This article has 35 citations and is from a domain leading peer-reviewed journal.

11. (persu2021beyondatherosclerosisand pages 11-12): Alexandre Persu, Caitriona Canning, Aleksander Prejbisz, Piotr Dobrowolski, Laurence Amar, Constantina Chrysochou, Jacek Kądziela, Mieczysław Litwin, Daan van Twist, Patricia Van der Niepen, Gregoire Wuerzner, Peter de Leeuw, Michel Azizi, Magda Januszewicz, and Andrzej Januszewicz. Beyond atherosclerosis and fibromuscular dysplasia: rare causes of renovascular hypertension. Hypertension, 78:898-911, Oct 2021. URL: https://doi.org/10.1161/hypertensionaha.121.17004, doi:10.1161/hypertensionaha.121.17004. This article has 41 citations and is from a domain leading peer-reviewed journal.

12. (redhead2024cardiovascularoutcomesimprove pages 9-10): Emily C. G. Redhead, Alicia Paessler, Zainab Arslan, Premal Patel, Kishore Minhas, Colin Forman, Paolo Hollis, Sebastiano Lava, Florin Ionescu, Devi Manuel, Samiran Ray, Nicos Kessaris, Alessandro Giardini, Vineetha Ratnamma, Nadine Dobby, Kjell Tullus, Jacob Simmonds, and Jelena Stojanovic. Cardiovascular outcomes improve in children with renovascular hypertension following endovascular and surgical interventions. Pediatric Nephrology (Berlin, Germany), 39:521-530, Sep 2024. URL: https://doi.org/10.1007/s00467-023-06123-5, doi:10.1007/s00467-023-06123-5. This article has 5 citations.

13. (coleman2022moleculargeneticevaluation pages 1-2): Dawn M Coleman, Yu Wang, Min-Lee Yang, Kristina L Hunker, Isabelle Birt, Ingrid L Bergin, Jun Z Li, James C Stanley, and Santhi K Ganesh. Molecular genetic evaluation of pediatric renovascular hypertension due to renal artery stenosis and abdominal aortic coarctation in neurofibromatosis type 1. Human molecular genetics, 31:334-346, Sep 2022. URL: https://doi.org/10.1093/hmg/ddab241, doi:10.1093/hmg/ddab241. This article has 8 citations and is from a domain leading peer-reviewed journal.

14. (persu2021beyondatherosclerosisand pages 1-2): Alexandre Persu, Caitriona Canning, Aleksander Prejbisz, Piotr Dobrowolski, Laurence Amar, Constantina Chrysochou, Jacek Kądziela, Mieczysław Litwin, Daan van Twist, Patricia Van der Niepen, Gregoire Wuerzner, Peter de Leeuw, Michel Azizi, Magda Januszewicz, and Andrzej Januszewicz. Beyond atherosclerosis and fibromuscular dysplasia: rare causes of renovascular hypertension. Hypertension, 78:898-911, Oct 2021. URL: https://doi.org/10.1161/hypertensionaha.121.17004, doi:10.1161/hypertensionaha.121.17004. This article has 41 citations and is from a domain leading peer-reviewed journal.

15. (coleman2022moleculargeneticevaluation pages 8-9): Dawn M Coleman, Yu Wang, Min-Lee Yang, Kristina L Hunker, Isabelle Birt, Ingrid L Bergin, Jun Z Li, James C Stanley, and Santhi K Ganesh. Molecular genetic evaluation of pediatric renovascular hypertension due to renal artery stenosis and abdominal aortic coarctation in neurofibromatosis type 1. Human molecular genetics, 31:334-346, Sep 2022. URL: https://doi.org/10.1093/hmg/ddab241, doi:10.1093/hmg/ddab241. This article has 8 citations and is from a domain leading peer-reviewed journal.

16. (coleman2022moleculargeneticevaluation pages 7-8): Dawn M Coleman, Yu Wang, Min-Lee Yang, Kristina L Hunker, Isabelle Birt, Ingrid L Bergin, Jun Z Li, James C Stanley, and Santhi K Ganesh. Molecular genetic evaluation of pediatric renovascular hypertension due to renal artery stenosis and abdominal aortic coarctation in neurofibromatosis type 1. Human molecular genetics, 31:334-346, Sep 2022. URL: https://doi.org/10.1093/hmg/ddab241, doi:10.1093/hmg/ddab241. This article has 8 citations and is from a domain leading peer-reviewed journal.