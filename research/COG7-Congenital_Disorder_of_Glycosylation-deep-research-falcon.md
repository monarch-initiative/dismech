---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-09T08:46:39.966581'
end_time: '2026-05-09T09:03:50.707690'
duration_seconds: 1030.74
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: COG7-congenital disorder of glycosylation
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
- **Disease Name:** COG7-congenital disorder of glycosylation
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **COG7-congenital disorder of glycosylation** covering all of the
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
- **Disease Name:** COG7-congenital disorder of glycosylation
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **COG7-congenital disorder of glycosylation** covering all of the
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


# COG7–Congenital Disorder of Glycosylation (COG7-CDG) — Comprehensive Research Report

## Target disease
**Name:** COG7-congenital disorder of glycosylation (COG7-CDG) (spaapen2005clinicalandbiochemical pages 3-6, francisco2023congenitaldisordersof pages 4-6)  
**Category:** Mendelian (autosomal recessive) (wu2004mutationofthe pages 3-4, zeevaert2008deficienciesinsubunits pages 2-3)  
**Known identifier in retrieved sources:** **MIM/OMIM 608779** (unsal2026endocrineimplicationsof pages 15-16, francisco2023congenitaldisordersof pages 4-6)  
**MONDO ID:** Not identified in retrieved sources (no MONDO cross-reference present in the documents retrieved for this run).  

---

## 1. Disease information
### Overview (current understanding)
COG7-CDG is a severe, typically neonatal-onset congenital disorder of glycosylation caused by loss of function of **COG7**, a subunit of the **conserved oligomeric Golgi (COG) complex**, leading to impaired Golgi trafficking and combined **N- and O-glycosylation** defects (wu2004mutationofthe pages 2-3, francisco2023congenitaldisordersof pages 2-4).

### Synonyms / alternative names
* **COG-7 deficiency** (spaapen2005clinicalandbiochemical pages 3-6)  
* **CDG type IIe / CDG-IIe** (historical subtype naming; noted as proposed nomenclature in early COG7-deficiency literature) (spaapen2005clinicalandbiochemical pages 3-6)

### Key identifiers (from available evidence)
* **OMIM/MIM:** 608779 (unsal2026endocrineimplicationsof pages 15-16, francisco2023congenitaldisordersof pages 4-6)

**Not found in retrieved texts for this run:** Orphanet number, ICD-10/ICD-11 code, MeSH disease heading, MONDO ID.

### Evidence provenance
Most disease-specific information available here is **aggregated from published case reports/series and reviews**, rather than EHR-derived cohorts (e.g., index families and a 6-patient founder series) (wu2004mutationofthe pages 1-2, zeevaert2008deficienciesinsubunits pages 3-5).

---

## 2. Etiology
### Disease causal factors
**Primary cause:** biallelic pathogenic variants in **COG7** impair COG complex integrity and Golgi trafficking, producing broad glycosylation abnormalities (wu2004mutationofthe pages 2-3, wu2004mutationofthe pages 3-4).

**Inheritance:** autosomal recessive; multiple affected families are consanguineous and show homozygosity for the recurrent splice variant (wu2004mutationofthe pages 3-4, zeevaert2008deficienciesinsubunits pages 3-5).

### Risk factors
* **Genetic:** COG7 loss-of-function variants; a recurrent splice variant is associated with multiple families (zeevaert2008deficienciesinsubunits pages 3-5).
* **Environmental:** Not established/expected as a primary driver in this Mendelian disorder; no gene–environment interaction evidence was identified in retrieved sources.

### Protective factors
No genetic or environmental protective factors were identified in retrieved sources.

---

## 3. Phenotypes (clinical spectrum)
### Typical onset, course, and severity
COG7-CDG is classically a **rapidly progressive neonatal multisystem disorder** with early lethality (weeks to months) (wu2004mutationofthe pages 1-2, zeevaert2008deficienciesinsubunits pages 3-5).

### Key clinical manifestations (human)
Case reports and a North African founder series describe a consistent phenotype including:
* **Growth impairment / prenatal growth retardation** (HPO suggestion: HP:0001511 Intrauterine growth restriction) (wu2004mutationofthe pages 1-2, zeevaert2008deficienciesinsubunits pages 3-5)
* **Progressive microcephaly** (HP:0000252 Microcephaly) (unsal2026endocrineimplicationsof pages 15-16, zeevaert2008deficienciesinsubunits pages 3-5)
* **Dysmorphic features** (e.g., micrognathia; low-set/dysplastic ears; loose/wrinkled skin reported) (HP:0000347 Micrognathia; HP:0000369 Low-set ears; HP:0000974 Hyperelastic skin / cutis laxa-like features) (wu2004mutationofthe pages 1-2, zeevaert2008deficienciesinsubunits pages 3-5)
* **Generalized hypotonia** (HP:0001252 Hypotonia) (wu2004mutationofthe pages 1-2, zeevaert2008deficienciesinsubunits pages 3-5)
* **Severe encephalopathy / seizures / epilepsy** (HP:0001298 Encephalopathy; HP:0001250 Seizures) (wu2004mutationofthe pages 1-2, zeevaert2008deficienciesinsubunits pages 3-5)
* **Cholestatic liver disease / hepatopathy** (HP:0001396 Cholestasis; HP:0001402 Hepatomegaly) (spaapen2005clinicalandbiochemical pages 3-6, zeevaert2008deficienciesinsubunits pages 3-5)
* **Recurrent infections** (HP:0002719 Recurrent infections) (wu2004mutationofthe pages 1-2)
* **Cardiac defects** including **ASD/VSD** (HP:0001631 Atrial septal defect; HP:0001629 Ventricular septal defect) (zeevaert2008deficienciesinsubunits pages 3-5)
* **Episodes of hyperthermia** (HP:0001945 Fever / hyperthermia episodes) (zeevaert2008deficienciesinsubunits pages 3-5)
* **Hand anomalies** including **adducted thumbs/overlapping fingers/ulnar deviation/contractures** (HP:0001184 Adducted thumbs; HP:0009484 Ulnar deviation of the hand) (unsal2026endocrineimplicationsof pages 15-16)

### Frequency information (available)
* A founder series reported **6 patients from 4 families** (North Africa) with a shared homozygous splice variant and highly similar severe phenotype (zeevaert2008deficienciesinsubunits pages 3-5).  
* Reported laboratory abnormality frequencies include **elevated CK in 4/6** and **transaminase elevation in 6/6** (zeevaert2008deficienciesinsubunits pages 3-5).

### Quality of life impact
Direct QoL instrument results specific to COG7-CDG were not found; however, the reported severe neonatal encephalopathy, cholestatic liver disease, seizures, and early death imply profound impairment (wu2004mutationofthe pages 1-2, zeevaert2008deficienciesinsubunits pages 3-5).

---

## 4. Genetic / molecular information
### Causal gene
* **COG7** (component of the conserved oligomeric Golgi complex) (unsal2026endocrineimplicationsof pages 15-16, wu2004mutationofthe pages 2-3)

### Pathogenic variants (human)
A recurrent homozygous splice variant is prominent:
* **IVS1+4A>C** (also reported as **c.169+4A>C**) → aberrant splicing with a **19-bp deletion in mRNA** and marked reduction/absence of COG7 protein (wu2004mutationofthe pages 2-3, zeevaert2008deficienciesinsubunits pages 3-5).

**Functional consequence:** loss of COG7 destabilizes the COG complex, disrupts Golgi trafficking, reduces nucleotide-sugar transport into the Golgi, and reduces glycosyltransferase activities, producing combined N- and O-glycosylation defects (wu2004mutationofthe pages 2-3, wu2004mutationofthe pages 4-6).

### Modifier genes / epigenetics / chromosomal abnormalities
No modifier genes, epigenetic mechanisms, or chromosomal abnormalities specific to COG7-CDG were identified in retrieved sources.

---

## 5. Environmental information
COG7-CDG is a monogenic disorder; non-genetic environmental contributors or infectious triggers were not reported in the retrieved evidence.

---

## 6. Mechanism / pathophysiology
### Mechanistic causal chain (gene → cell biology → biochemical signature → clinical phenotype)
1. **COG7 deficiency** reduces/abolishes COG7 protein and destabilizes the COG complex (wu2004mutationofthe pages 2-3).  
2. This impairs **ER–Golgi and intra-Golgi trafficking** (e.g., slowed trafficking of a Golgi sialyltransferase reporter ST-GFP) (wu2004mutationofthe pages 2-3, wu2004mutationofthe pages 3-4).  
3. Disrupted Golgi homeostasis leads to **defective glycosylation enzyme function/localization**, including reduced activities of O-glycan Core1GalT and ST3Gal-I and impaired nucleotide-sugar transport into the Golgi (~30% of normal in patient fibroblasts) (wu2004mutationofthe pages 2-3).  
4. The net result is **combined N- and O-hypoglycosylation**, especially hyposialylation/galactosylation defects, measurable in plasma glycoproteins (transferrin, apoC-III) and reflected in systemic multi-organ disease (wu2004mutationofthe pages 2-3, spaapen2005clinicalandbiochemical pages 3-6).

### Key cellular/biochemical findings (selected quantitative data)
* **Golgi nucleotide-sugar transport** ~30% of normal for CMP-sialic acid/UDP-galactose in one patient’s fibroblasts (wu2004mutationofthe pages 2-3).  
* **Glycosyltransferase activities** reduced (Core1GalT and ST3Gal-I reductions reported) (wu2004mutationofthe pages 2-3).  
* **Total serum sialic acid** reduced two- to fivefold in the index family, with transferrin glycoforms distributed across 0–4 sialic acids (wu2004mutationofthe pages 1-2, wu2004mutationofthe pages 2-3).

### Ontology suggestions
**GO Biological Process (examples):**
* Golgi organization; vesicle tethering / retrograde vesicle-mediated transport, Golgi to ER; protein glycosylation; protein sialylation (mechanistically implied by trafficking and sialylation defects) (wu2004mutationofthe pages 2-3, francisco2023congenitaldisordersof pages 2-4).

**Cell types (CL, examples):**
* Fibroblast (patient-derived dermal fibroblasts are the key experimental system) (wu2004mutationofthe pages 2-3, spaapen2005clinicalandbiochemical pages 1-3).  
* Hepatocyte; neuron (inferred from dominant liver and CNS involvement described clinically; direct cellular profiling not found) (zeevaert2008deficienciesinsubunits pages 3-5, francisco2023congenitaldisordersof pages 1-2).

---

## 7. Anatomical structures affected
Based on multisystem involvement reported:
* **Brain/CNS** (encephalopathy, seizures; cerebral/cerebellar atrophy described in summaries) (UBERON examples: UBERON:0000955 brain; UBERON:0002037 cerebellum) (unsal2026endocrineimplicationsof pages 15-16, zeevaert2008deficienciesinsubunits pages 3-5).
* **Liver** (cholestasis, elevated transaminases, hepatopathy) (UBERON:0002107 liver) (spaapen2005clinicalandbiochemical pages 3-6, zeevaert2008deficienciesinsubunits pages 3-5).
* **Heart** (ASD/VSD; cardiac insufficiency) (UBERON:0000948 heart) (wu2004mutationofthe pages 1-2, zeevaert2008deficienciesinsubunits pages 3-5).
* **Immune/host defense** (recurrent infections) (wu2004mutationofthe pages 1-2).

Subcellular localization central to pathogenesis: **Golgi apparatus** (GO cellular component: Golgi apparatus) (wu2004mutationofthe pages 2-3).

---

## 8. Temporal development
* **Onset:** congenital/neonatal (wu2004mutationofthe pages 1-2, zeevaert2008deficienciesinsubunits pages 3-5).  
* **Course:** rapidly progressive, multi-organ deterioration (wu2004mutationofthe pages 1-2, zeevaert2008deficienciesinsubunits pages 3-5).  
* **Duration:** typically weeks to months in classic cases (wu2004mutationofthe pages 1-2, zeevaert2008deficienciesinsubunits pages 3-5).

---

## 9. Inheritance and population
### Inheritance
Autosomal recessive, frequently in consanguineous families (zeevaert2008deficienciesinsubunits pages 2-3, zeevaert2008deficienciesinsubunits pages 3-5).

### Epidemiology (available data)
Population prevalence/incidence estimates were **not identified** in retrieved evidence.

### Variant distribution / founder effect
A cohort described **6 patients** (2 Tunisia, 4 Morocco) all homozygous for **IVS1+4A>C / c.169+4A>C**, and haplotyping suggested a shared ancestral haplotype consistent with a founder effect in North Africa (zeevaert2008deficienciesinsubunits pages 3-5).

### Case fatality / prognosis statistics
Deaths were reported between **5 weeks and 9 months** in the 6-patient series (zeevaert2008deficienciesinsubunits pages 3-5); the index sibling pair died at **5 and 10 weeks** (wu2004mutationofthe pages 1-2).

---

## 10. Diagnostics
### Core clinical laboratory tests / biomarkers
**1) Serum transferrin isoforms (IEF)**
* Abnormal **type II / type 2-like CDG** pattern is a key screening biomarker for processing/trafficking CDGs (wu2004mutationofthe pages 1-2, spaapen2005clinicalandbiochemical pages 3-6).  
* Visual evidence: transferrin IEF patterns from affected siblings are shown in Spaapen et al. 2005 (spaapen2005clinicalandbiochemical media a32196a0, spaapen2005clinicalandbiochemical media 9596aac9).

**2) Apolipoprotein C-III isoforms (IEF)**
* ApoC-III IEF demonstrates **O-glycan hyposialylation**, supporting combined N- and O-glycosylation involvement (spaapen2005clinicalandbiochemical pages 3-6).  
* Visual evidence: apoC-III IEF figure in Spaapen et al. 2005 (spaapen2005clinicalandbiochemical media a32196a0, spaapen2005clinicalandbiochemical media 9596aac9).

**3) Sialic acid quantitation (blood/urine)**
* Low total plasma sialic acid reported in affected siblings (e.g., 321 and 599 µmol/L vs reference range) and increased urinary free sialic acid in one patient (spaapen2005clinicalandbiochemical pages 3-6).  

**4) Supportive labs**
* Elevated transaminases (200–890 U/L in the 6-patient series) and elevated CK in 4/6 (zeevaert2008deficienciesinsubunits pages 3-5).

### Genetic testing
Disease confirmation is via molecular detection of biallelic COG7 pathogenic variants (e.g., IVS1+4A>C) (wu2004mutationofthe pages 2-3, spaapen2005clinicalandbiochemical pages 3-6).

### Current diagnostic practice trends (2023–2024 emphasis)
A 2023 state-of-the-art review highlights that while transferrin IEF historically underpinned CDG screening, **genomic sequencing (WES/WGS)** is now “very powerful” and may be the only route when biochemical biomarkers are absent (francisco2023congenitaldisordersof pages 4-6). The same review notes expanding glycomics biomarkers (e.g., ESI-QTOF-MS glycan profiling; additional glycoprotein biomarkers) (francisco2023congenitaldisordersof pages 4-6).

### Differential diagnosis
Not systematically enumerated in retrieved texts; however, differential diagnosis typically includes other **Golgi/trafficking CDG** and other causes of neonatal cholestasis/encephalopathy with abnormal transferrin IEF (supported generally by the CDG classification context) (francisco2023congenitaldisordersof pages 2-4, paprocka2021congenitaldisordersof pages 2-4).

---

## 11. Outcome / prognosis
COG7-CDG is most often **lethal in early infancy** in the classic phenotype, with fatality occurring as early as 5–10 weeks in initial siblings and by 9 months in the founder series (wu2004mutationofthe pages 1-2, zeevaert2008deficienciesinsubunits pages 3-5).

Prognostic biomarkers specific to COG7-CDG were not identified; severity is largely defined clinically and by multi-organ involvement (zeevaert2008deficienciesinsubunits pages 3-5).

---

## 12. Treatment
### Disease-specific therapy
No COG7-CDG-specific disease-modifying therapy was identified in the retrieved evidence.

### General CDG treatment landscape (expert consensus from authoritative reviews)
A 2023 Orphanet Journal of Rare Diseases review states the urgency of developing targeted therapies and indicates that CDG patients often require ongoing management for multi-organ complications (francisco2023congenitaldisordersof pages 1-2). The review also states CDG treatment remains almost entirely symptomatic/supportive, with mannose supplementation for MPI-CDG as a key established exception (francisco2023congenitaldisordersof pages 2-4).

### Supportive care (real-world implementations; inferred from phenotype)
Given the presentation, standard practice typically includes:
* seizure management (anti-seizure medications) (general CDG neurology management context) (paprocka2021congenitaldisordersof pages 2-4)
* nutritional support / failure-to-thrive management
* management of cholestasis and hepatic dysfunction
* infection prevention and treatment
* cardiology management for structural defects/heart failure
These are consistent with the reported multi-organ involvement and severe neonatal course, though explicit COG7-CDG management protocols were not found in retrieved sources (wu2004mutationofthe pages 1-2, zeevaert2008deficienciesinsubunits pages 3-5).

### Clinical trials / registries relevant to CDG (and applicability to COG7-CDG)
* **NCT04199000** (“Clinical and Basic Investigations Into Congenital Disorders of Glycosylation”), observational natural history study; **start date 2019-10-08**; **recruiting**; **estimated enrollment 500**. Key aims include measuring progression/severity using the Nijmegen CDG rating scale and collecting patient-reported outcomes (PROMIS) and biospecimens for biomarkers (NCT04199000 chunk 1). The record requires a genetically/enzymatically/molecularly confirmed CDG diagnosis, making it plausibly inclusive of rare CDG subtypes even if COG7 is not explicitly listed among keywords in the excerpt (NCT04199000 chunk 1).

### MAXO suggestions (supportive)
* MAXO:0000758 anticonvulsant therapy (for seizures; generalized CDG epilepsy management context) (paprocka2021congenitaldisordersof pages 2-4)  
* MAXO:0000472 nutritional support / feeding support  
* MAXO:0000464 supportive care  
(These MAXO mappings are suggested conceptually; explicit MAXO-coded statements were not present in the retrieved texts.)

---

## 13. Prevention
Primary prevention is not applicable in the usual sense for a recessive Mendelian disorder; the principal prevention strategies are **genetic counseling** and **carrier/prenatal testing** in at-risk families (implied by AR inheritance and founder effect) (zeevaert2008deficienciesinsubunits pages 3-5).

---

## 14. Other species / natural disease
No naturally occurring veterinary disease analogs specifically tied to COG7 were identified in retrieved sources.

---

## 15. Model organisms and experimental systems
### Cellular models (human)
Patient-derived dermal fibroblasts are the principal model system; mechanistic assays include:
* trafficking assays (ST-GFP fluorescence recovery/photobleaching approaches)
* nucleotide-sugar transport assays into Golgi
* glycosyltransferase activity assays
* lectin binding/neuraminidase treatment
Importantly, **complementation with wild-type COG7 cDNA rescues trafficking and glycosylation defects**, supporting causality (wu2004mutationofthe pages 2-3, wu2004mutationofthe pages 4-6).

### Comparative models
COG biology and phenotypes are also studied in CHO cell mutants (ldlB/ldlC), yeast, and animal models including Drosophila and C. elegans (general COG modeling context) (zeevaert2008deficienciesinsubunits pages 2-3).

---

## Recent developments and latest research emphasis (2023–2024)
### Field-level advances relevant to COG7-CDG
A 2023 “state of the art” review highlights rapid progress driven by multi-omics and expanding gene discovery, and explicitly notes the unmet need for targeted therapies: **“targeted therapies’ discovery and approval being the most urgent unmet need.”** (published Oct 2023; URL: https://doi.org/10.1186/s13023-023-02879-z) (francisco2023congenitaldisordersof pages 1-2). The same review reports substantial expansion of known CDG genes/phenotypes (**163 genes; 193 phenotypes**) and emphasizes genomic sequencing as a key diagnostic route (francisco2023congenitaldisordersof pages 1-2, francisco2023congenitaldisordersof pages 4-6).

For trafficking-related CDG classification, the review places vesicular transport defects (including COG defects) within an “other (including multiple)” category (francisco2023congenitaldisordersof pages 2-4).

---

## Key structured summary table
| Category | Structured fact | Evidence / key references |
|---|---|---|
| Disease name / synonyms | **COG7-congenital disorder of glycosylation (COG7-CDG)**; older nomenclature includes **CDG type IIe / CDG-IIe** and **COG-7 deficiency** (spaapen2005clinicalandbiochemical pages 3-6) | Spaapen et al., 2005, *J Inherit Metab Dis*, DOI: https://doi.org/10.1007/s10545-005-0015-z (spaapen2005clinicalandbiochemical pages 3-6) |
| Identifier(s) | **MIM/OMIM: 608779** reported for COG7-CDG in recent review tables (unsal2026endocrineimplicationsof pages 15-16, francisco2023congenitaldisordersof pages 4-6) | Ünsal & Özön, 2026, DOI: https://doi.org/10.4274/jcrpe.galenos.2025.2024-10-7; Francisco et al., 2023, DOI: https://doi.org/10.1186/s13023-023-02879-z (unsal2026endocrineimplicationsof pages 15-16, francisco2023congenitaldisordersof pages 4-6) |
| Disease class | Trafficking-related / Golgi homeostasis CDG affecting **combined N- and O-glycosylation** through COG complex dysfunction (wu2004mutationofthe pages 2-3, francisco2023congenitaldisordersof pages 2-4) | Wu et al., 2004, *Nat Med*, DOI: https://doi.org/10.1038/nm1041; Francisco et al., 2023, DOI: https://doi.org/10.1186/s13023-023-02879-z (wu2004mutationofthe pages 2-3, francisco2023congenitaldisordersof pages 2-4) |
| Inheritance | **Autosomal recessive**; reported in affected siblings and multiple consanguineous families (wu2004mutationofthe pages 3-4, zeevaert2008deficienciesinsubunits pages 2-3) | Wu et al., 2004, DOI: https://doi.org/10.1038/nm1041; Zeevaert et al., 2008, DOI: https://doi.org/10.1016/j.ymgme.2007.08.118 (wu2004mutationofthe pages 3-4, zeevaert2008deficienciesinsubunits pages 2-3) |
| Key pathogenic variant | Recurrent homozygous splice variant **IVS1+4A>C**, also reported as **c.169+4A>C**, causing aberrant splicing with a **19-bp deletion in mRNA** and marked reduction/absence of COG7 protein (wu2004mutationofthe pages 2-3, spaapen2005clinicalandbiochemical pages 3-6, zeevaert2008deficienciesinsubunits pages 3-5) | Wu et al., 2004, DOI: https://doi.org/10.1038/nm1041; Spaapen et al., 2005, DOI: https://doi.org/10.1007/s10545-005-0015-z; Zeevaert et al., 2008, DOI: https://doi.org/10.1016/j.ymgme.2007.08.118 (wu2004mutationofthe pages 2-3, spaapen2005clinicalandbiochemical pages 3-6, zeevaert2008deficienciesinsubunits pages 3-5) |
| Molecular consequence | COG7 loss destabilizes COG complex integrity and impairs Golgi trafficking, with slowed ER-to-Golgi/Golgi transport and broad glycosylation abnormalities (wu2004mutationofthe pages 3-4, wu2004mutationofthe pages 2-3) | Wu et al., 2004, DOI: https://doi.org/10.1038/nm1041 (wu2004mutationofthe pages 3-4, wu2004mutationofthe pages 2-3) |
| Core clinical features | Severe neonatal multisystem disease: **prenatal growth retardation/IUGR, microcephaly, dysmorphic facial features, loose/wrinkled skin, hypotonia, seizures/epilepsy, cholestatic liver disease/hepatopathy, recurrent infections, cardiac insufficiency**, cerebellar/brain abnormalities (wu2004mutationofthe pages 1-2, zeevaert2008deficienciesinsubunits pages 2-3, zeevaert2008deficienciesinsubunits pages 3-5) | Wu et al., 2004, DOI: https://doi.org/10.1038/nm1041; Zeevaert et al., 2008, DOI: https://doi.org/10.1016/j.ymgme.2007.08.118 (wu2004mutationofthe pages 1-2, zeevaert2008deficienciesinsubunits pages 2-3, zeevaert2008deficienciesinsubunits pages 3-5) |
| Recognizable phenotype clues | Frequently highlighted pattern: **microcephaly, growth impairment, adducted thumbs/hand anomalies, ventricular septal defect (VSD), and episodes of hyperthermia** (zeevaert2008deficienciesinsubunits pages 3-5) | Zeevaert et al., 2008, DOI: https://doi.org/10.1016/j.ymgme.2007.08.118 (zeevaert2008deficienciesinsubunits pages 3-5) |
| Additional neurodevelopmental / structural findings | Reported features include **global developmental delay, cerebral/cerebellar atrophy, hypoplasia of the corpus callosum, delayed myelination**, and skeletal/hand abnormalities (unsal2026endocrineimplicationsof pages 15-16) | Ünsal & Özön, 2026, DOI: https://doi.org/10.4274/jcrpe.galenos.2025.2024-10-7 (unsal2026endocrineimplicationsof pages 15-16) |
| Transferrin IEF biomarker | **Abnormal serum transferrin isoelectric focusing (IEF)** showing a **type II / type 2-like CDG pattern**; one report described an approximately equal distribution of transferrin glycoforms with **0–4 sialic acids** (wu2004mutationofthe pages 1-2, wu2004mutationofthe pages 2-3, spaapen2005clinicalandbiochemical pages 3-6, spaapen2005clinicalandbiochemical media a32196a0) | Wu et al., 2004, DOI: https://doi.org/10.1038/nm1041; Spaapen et al., 2005, DOI: https://doi.org/10.1007/s10545-005-0015-z (wu2004mutationofthe pages 1-2, wu2004mutationofthe pages 2-3, spaapen2005clinicalandbiochemical pages 3-6, spaapen2005clinicalandbiochemical media a32196a0) |
| ApoC-III IEF biomarker | **Aberrant apolipoprotein C-III IEF** demonstrating **hyposialylation of O-linked glycans** (spaapen2005clinicalandbiochemical pages 3-6, spaapen2005clinicalandbiochemical media a32196a0) | Spaapen et al., 2005, DOI: https://doi.org/10.1007/s10545-005-0015-z (spaapen2005clinicalandbiochemical pages 3-6, spaapen2005clinicalandbiochemical media a32196a0) |
| Sialic acid abnormalities | **Low total plasma sialic acid** reported: **321 µmol/L** and **599 µmol/L** in two siblings (reference **1620–2940 µmol/L**); **two- to fivefold reduction** in total serum sialic acid also described; **urinary free sialic acid increased** in one patient (**182 µmol/mmol creatinine**) (wu2004mutationofthe pages 1-2, spaapen2005clinicalandbiochemical pages 3-6) | Wu et al., 2004, DOI: https://doi.org/10.1038/nm1041; Spaapen et al., 2005, DOI: https://doi.org/10.1007/s10545-005-0015-z (wu2004mutationofthe pages 1-2, spaapen2005clinicalandbiochemical pages 3-6) |
| Other biochemical / cellular findings | Partial **N-glycan sialylation defect**, decreased **O-glycan sialylation**, increased **RCA-I lectin binding**, elevated **CMP-sialic acid** (2–3×), reduced Golgi nucleotide-sugar transport (~**30% of normal**), and reduced **Core1GalT** (~40%) and **ST3Gal-I** (~62%) activities (wu2004mutationofthe pages 2-3) | Wu et al., 2004, DOI: https://doi.org/10.1038/nm1041 (wu2004mutationofthe pages 2-3) |
| Liver / muscle laboratory abnormalities | **Markedly elevated transaminases** in all six patients (**200–890 U/L**, normal <40) and **elevated CK** in **4/6** patients (zeevaert2008deficienciesinsubunits pages 3-5) | Zeevaert et al., 2008, DOI: https://doi.org/10.1016/j.ymgme.2007.08.118 (zeevaert2008deficienciesinsubunits pages 3-5) |
| Prognosis | Usually **rapidly progressive and lethal in infancy**; reported deaths occurred from **5 weeks to 9 months**; initial sibling report described death at **5 and 10 weeks** (wu2004mutationofthe pages 1-2, zeevaert2008deficienciesinsubunits pages 2-3, zeevaert2008deficienciesinsubunits pages 3-5) | Wu et al., 2004, DOI: https://doi.org/10.1038/nm1041; Zeevaert et al., 2008, DOI: https://doi.org/10.1016/j.ymgme.2007.08.118 (wu2004mutationofthe pages 1-2, zeevaert2008deficienciesinsubunits pages 2-3, zeevaert2008deficienciesinsubunits pages 3-5) |
| Notable populations / founder effect | Early series identified **6 patients from 4 families**, all with consanguinity and originating from **North Africa** (**2 Tunisia, 4 Morocco**); shared haplotype suggested a **founder effect / shared ancestral haplotype** for **c.169+4A>C** (zeevaert2008deficienciesinsubunits pages 2-3, zeevaert2008deficienciesinsubunits pages 3-5) | Zeevaert et al., 2008, DOI: https://doi.org/10.1016/j.ymgme.2007.08.118 (zeevaert2008deficienciesinsubunits pages 2-3, zeevaert2008deficienciesinsubunits pages 3-5) |
| Frequency data available | In one screened cohort of **35 CDG-IIx** cases, **5/35 (~14%)** had a COG-subunit defect; COG7 was described as the **most frequent COG-related defect** in that series (zeevaert2008deficienciesinsubunits pages 2-3) | Zeevaert et al., 2008, DOI: https://doi.org/10.1016/j.ymgme.2007.08.118 (zeevaert2008deficienciesinsubunits pages 2-3) |
| Diagnostic practice notes | Recent CDG reviews indicate a shift from reliance on **transferrin IEF** alone toward **WES/WGS** and broader biochemical glycomics; however, transferrin IEF remains an important first-line screen for many N-glycosylation defects (francisco2023congenitaldisordersof pages 4-6, paprocka2021congenitaldisordersof pages 2-4) | Francisco et al., 2023, DOI: https://doi.org/10.1186/s13023-023-02879-z; Paprocka et al., 2021, DOI: https://doi.org/10.3390/brainsci11010088 (francisco2023congenitaldisordersof pages 4-6, paprocka2021congenitaldisordersof pages 2-4) |
| Key references | **Wu et al., 2004** (Nature Medicine; discovery of lethal COG7 disorder; DOI: https://doi.org/10.1038/nm1041); **Spaapen et al., 2005** (clinical/biochemical siblings report; DOI: https://doi.org/10.1007/s10545-005-0015-z); **Zeevaert et al., 2008** (6-patient/founder-effect cohort; DOI: https://doi.org/10.1016/j.ymgme.2007.08.118); **Francisco et al., 2023** (state-of-the-art CDG review; DOI: https://doi.org/10.1186/s13023-023-02879-z) | PMID not available in gathered evidence; URLs/DOIs supported by context (wu2004mutationofthe pages 2-3, spaapen2005clinicalandbiochemical pages 3-6, zeevaert2008deficienciesinsubunits pages 3-5, francisco2023congenitaldisordersof pages 4-6) |


*Table: This table compiles the core structured facts for COG7-congenital disorder of glycosylation, including identifiers, inheritance, recurrent pathogenic variant, clinical and laboratory hallmarks, prognosis, and population observations. It is designed as a concise evidence-backed summary for knowledge-base curation.*

---

## Key diagnostic figure evidence (visual)
Transferrin IEF (type II-like pattern) and apoC-III IEF (O-glycan hyposialylation) in COG7 deficiency are shown in Spaapen et al. 2005 (spaapen2005clinicalandbiochemical media a32196a0, spaapen2005clinicalandbiochemical media 9596aac9).

---

## Evidence gaps / not available in retrieved sources
* MONDO, Orphanet, ICD-10/ICD-11, and MeSH identifiers for COG7-CDG were not found in retrieved texts during this run.
* Population prevalence/incidence and long-term survivorship data beyond infancy were not identified.
* No COG7-specific interventional trials were identified; available trial evidence is CDG-wide natural history/registry infrastructure.


References

1. (spaapen2005clinicalandbiochemical pages 3-6): L. J. M. Spaapen, J. A. Bakker, S. B. van der Meer, H. J. Sijstermans, R. A. Steet, R. A. Wevers, and J. Jaeken. Clinical and biochemical presentation of siblings with cog-7 deficiency, a lethal multiple o- and n-glycosylation disorder. Journal of Inherited Metabolic Disease, 28:707-714, Sep 2005. URL: https://doi.org/10.1007/s10545-005-0015-z, doi:10.1007/s10545-005-0015-z. This article has 73 citations and is from a peer-reviewed journal.

2. (francisco2023congenitaldisordersof pages 4-6): Rita Francisco, Sandra Brasil, Joana Poejo, Jaak Jaeken, Carlota Pascoal, Paula A. Videira, and Vanessa dos Reis Ferreira. Congenital disorders of glycosylation (cdg): state of the art in 2022. Orphanet Journal of Rare Diseases, Oct 2023. URL: https://doi.org/10.1186/s13023-023-02879-z, doi:10.1186/s13023-023-02879-z. This article has 71 citations and is from a peer-reviewed journal.

3. (wu2004mutationofthe pages 3-4): Xiaohua Wu, Richard A Steet, Ognian Bohorov, Jaap Bakker, John Newell, Monty Krieger, Leo Spaapen, Stuart Kornfeld, and Hudson H Freeze. Mutation of the cog complex subunit gene cog7 causes a lethal congenital disorder. Nature Medicine, 10:518-523, Apr 2004. URL: https://doi.org/10.1038/nm1041, doi:10.1038/nm1041. This article has 360 citations and is from a highest quality peer-reviewed journal.

4. (zeevaert2008deficienciesinsubunits pages 2-3): Renate Zeevaert, François Foulquier, Jaak Jaeken, and Gert Matthijs. Deficiencies in subunits of the conserved oligomeric golgi (cog) complex define a novel group of congenital disorders of glycosylation. Molecular genetics and metabolism, 93 1:15-21, Jan 2008. URL: https://doi.org/10.1016/j.ymgme.2007.08.118, doi:10.1016/j.ymgme.2007.08.118. This article has 126 citations and is from a peer-reviewed journal.

5. (unsal2026endocrineimplicationsof pages 15-16): Yağmur Ünsal and Zeynep Alev Özön. Endocrine implications of congenital disorders of glycosylation. Journal of clinical research in pediatric endocrinology, Feb 2026. URL: https://doi.org/10.4274/jcrpe.galenos.2025.2024-10-7, doi:10.4274/jcrpe.galenos.2025.2024-10-7. This article has 2 citations.

6. (wu2004mutationofthe pages 2-3): Xiaohua Wu, Richard A Steet, Ognian Bohorov, Jaap Bakker, John Newell, Monty Krieger, Leo Spaapen, Stuart Kornfeld, and Hudson H Freeze. Mutation of the cog complex subunit gene cog7 causes a lethal congenital disorder. Nature Medicine, 10:518-523, Apr 2004. URL: https://doi.org/10.1038/nm1041, doi:10.1038/nm1041. This article has 360 citations and is from a highest quality peer-reviewed journal.

7. (francisco2023congenitaldisordersof pages 2-4): Rita Francisco, Sandra Brasil, Joana Poejo, Jaak Jaeken, Carlota Pascoal, Paula A. Videira, and Vanessa dos Reis Ferreira. Congenital disorders of glycosylation (cdg): state of the art in 2022. Orphanet Journal of Rare Diseases, Oct 2023. URL: https://doi.org/10.1186/s13023-023-02879-z, doi:10.1186/s13023-023-02879-z. This article has 71 citations and is from a peer-reviewed journal.

8. (wu2004mutationofthe pages 1-2): Xiaohua Wu, Richard A Steet, Ognian Bohorov, Jaap Bakker, John Newell, Monty Krieger, Leo Spaapen, Stuart Kornfeld, and Hudson H Freeze. Mutation of the cog complex subunit gene cog7 causes a lethal congenital disorder. Nature Medicine, 10:518-523, Apr 2004. URL: https://doi.org/10.1038/nm1041, doi:10.1038/nm1041. This article has 360 citations and is from a highest quality peer-reviewed journal.

9. (zeevaert2008deficienciesinsubunits pages 3-5): Renate Zeevaert, François Foulquier, Jaak Jaeken, and Gert Matthijs. Deficiencies in subunits of the conserved oligomeric golgi (cog) complex define a novel group of congenital disorders of glycosylation. Molecular genetics and metabolism, 93 1:15-21, Jan 2008. URL: https://doi.org/10.1016/j.ymgme.2007.08.118, doi:10.1016/j.ymgme.2007.08.118. This article has 126 citations and is from a peer-reviewed journal.

10. (wu2004mutationofthe pages 4-6): Xiaohua Wu, Richard A Steet, Ognian Bohorov, Jaap Bakker, John Newell, Monty Krieger, Leo Spaapen, Stuart Kornfeld, and Hudson H Freeze. Mutation of the cog complex subunit gene cog7 causes a lethal congenital disorder. Nature Medicine, 10:518-523, Apr 2004. URL: https://doi.org/10.1038/nm1041, doi:10.1038/nm1041. This article has 360 citations and is from a highest quality peer-reviewed journal.

11. (spaapen2005clinicalandbiochemical pages 1-3): L. J. M. Spaapen, J. A. Bakker, S. B. van der Meer, H. J. Sijstermans, R. A. Steet, R. A. Wevers, and J. Jaeken. Clinical and biochemical presentation of siblings with cog-7 deficiency, a lethal multiple o- and n-glycosylation disorder. Journal of Inherited Metabolic Disease, 28:707-714, Sep 2005. URL: https://doi.org/10.1007/s10545-005-0015-z, doi:10.1007/s10545-005-0015-z. This article has 73 citations and is from a peer-reviewed journal.

12. (francisco2023congenitaldisordersof pages 1-2): Rita Francisco, Sandra Brasil, Joana Poejo, Jaak Jaeken, Carlota Pascoal, Paula A. Videira, and Vanessa dos Reis Ferreira. Congenital disorders of glycosylation (cdg): state of the art in 2022. Orphanet Journal of Rare Diseases, Oct 2023. URL: https://doi.org/10.1186/s13023-023-02879-z, doi:10.1186/s13023-023-02879-z. This article has 71 citations and is from a peer-reviewed journal.

13. (spaapen2005clinicalandbiochemical media a32196a0): L. J. M. Spaapen, J. A. Bakker, S. B. van der Meer, H. J. Sijstermans, R. A. Steet, R. A. Wevers, and J. Jaeken. Clinical and biochemical presentation of siblings with cog-7 deficiency, a lethal multiple o- and n-glycosylation disorder. Journal of Inherited Metabolic Disease, 28:707-714, Sep 2005. URL: https://doi.org/10.1007/s10545-005-0015-z, doi:10.1007/s10545-005-0015-z. This article has 73 citations and is from a peer-reviewed journal.

14. (spaapen2005clinicalandbiochemical media 9596aac9): L. J. M. Spaapen, J. A. Bakker, S. B. van der Meer, H. J. Sijstermans, R. A. Steet, R. A. Wevers, and J. Jaeken. Clinical and biochemical presentation of siblings with cog-7 deficiency, a lethal multiple o- and n-glycosylation disorder. Journal of Inherited Metabolic Disease, 28:707-714, Sep 2005. URL: https://doi.org/10.1007/s10545-005-0015-z, doi:10.1007/s10545-005-0015-z. This article has 73 citations and is from a peer-reviewed journal.

15. (paprocka2021congenitaldisordersof pages 2-4): Justyna Paprocka, Aleksandra Jezela-Stanek, Anna Tylki-Szymańska, and Stephanie Grunewald. Congenital disorders of glycosylation from a neurological perspective. Brain Sciences, 11:88, Jan 2021. URL: https://doi.org/10.3390/brainsci11010088, doi:10.3390/brainsci11010088. This article has 131 citations.

16. (NCT04199000 chunk 1): Eva Morava-Kozicz. Clinical and Basic Investigations Into Congenital Disorders of Glycosylation. Icahn School of Medicine at Mount Sinai. 2019. ClinicalTrials.gov Identifier: NCT04199000