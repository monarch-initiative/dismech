---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-11T12:31:19.021709'
end_time: '2026-05-11T12:44:11.480867'
duration_seconds: 772.46
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: ALG9-congenital disorder of glycosylation
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 22
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** ALG9-congenital disorder of glycosylation
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **ALG9-congenital disorder of glycosylation** covering all of the
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
- **Disease Name:** ALG9-congenital disorder of glycosylation
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **ALG9-congenital disorder of glycosylation** covering all of the
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


# ALG9–congenital disorder of glycosylation (ALG9-CDG; historical CDG-IL) — Disease Characteristics Research Report

## Target disease
- **Disease name:** ALG9–congenital disorder of glycosylation (ALG9-CDG)
- **Category:** Mendelian, inborn error of metabolism; N-linked glycosylation defect (CDG type I pattern on transferrin testing) (frank2004identificationandfunctional pages 1-2, davis2017alg9cdgnewclinical pages 5-6)
- **MONDO ID:** Not retrievable with the available tools in this run (gap)

## Executive summary
ALG9-CDG is an autosomal recessive congenital disorder of glycosylation caused by biallelic pathogenic variants in **ALG9**, which encodes an ER **α1,2-mannosyltransferase** required for stepwise assembly of the dolichol-linked oligosaccharide precursor for **N-glycosylation**. The disorder shows a broad phenotypic spectrum ranging from a liveborn multisystem neurodevelopmental disorder (developmental delay, hypotonia, seizures, progressive microcephaly, hepatomegaly; often renal cystic disease and pericardial effusion) to **prenatal-lethal skeletal dysplasia with polycystic kidneys and multiple malformations** (tham2016anovelphenotype pages 1-2, weinstein2005cdg‐ilaninfant pages 1-2). Diagnostic hallmarks include **type I** transferrin isoelectric focusing abnormalities, accumulation of truncated lipid-linked oligosaccharide intermediates (DolPP-GlcNAc2Man6/Man8), and N-glycan profiling showing truncation with relative enrichment of smaller high-mannose species (Man4–Man6) and depletion of Man7–Man9 (frank2004identificationandfunctional pages 2-5, davis2017alg9cdgnewclinical pages 5-6).

## Evidence map (structured summary)
| Disease / identifier | Gene | Inheritance | Key pathogenic variant(s) reported | Core phenotypes reported | Biochemical / diagnostic findings | Evidence type | Year | Key citation(s) |
|---|---|---|---|---|---|---|---|---|
| ALG9-congenital disorder of glycosylation; ALG9-CDG; former name CDG-IL | **ALG9** (alpha-1,2-mannosyltransferase) | Autosomal recessive | General disease definition; multiple homozygous variants across reports | Multisystem N-glycosylation disorder with neurodevelopmental impairment and variable visceral involvement | Type I CDG on transferrin isoelectric focusing; abnormal N-glycosylation due to defective dolichol-linked oligosaccharide assembly (frank2004identificationandfunctional pages 1-2, francisco2023congenitaldisordersof pages 1-2) | Human disease definition / review | 2004, 2023 | (frank2004identificationandfunctional pages 1-2, francisco2023congenitaldisordersof pages 1-2) |
| Initial molecularly defined liveborn case | **ALG9** | Autosomal recessive (homozygous variant) | c.1567G>A, p.Glu523Lys (also described in secondary summaries as p.E523K) | Developmental delay, central hypotonia, seizures, severe microcephaly, hepatomegaly, bronchial asthma | Serum transferrin IEF: increased disialo- and asialo-transferrin consistent with CDG-I; fibroblast LLO accumulation of DolPP-GlcNAc2Man6 and DolPP-GlcNAc2Man8; transfer of truncated glycans to protein; yeast complementation confirmed functional defect (frank2004identificationandfunctional pages 1-2, frank2004identificationandfunctional pages 2-5) | Human case report with functional validation | 2004 | (frank2004identificationandfunctional pages 1-2, frank2004identificationandfunctional pages 2-5) |
| Second liveborn case expanding phenotype | **ALG9** | Autosomal recessive (homozygous variant) | c.860A>G, p.Tyr286Cys / p.Y286C | Psychomotor retardation, seizures, hypotonia, diffuse cerebral and cerebellar atrophy with delayed myelination, failure to thrive, pericardial effusion, cystic renal disease, hepatosplenomegaly, esotropia, inverted nipples; progressive microcephaly later documented | Typical CDG type I transferrin pattern by IEF; ALG9 defect suggested by DolPP-GlcNAc2Man6 and DolPP-GlcNAc2Man8 accumulation; molecular confirmation by yeast complementation (weinstein2005cdg‐ilaninfant pages 1-2) | Human case report | 2005 | (weinstein2005cdg‐ilaninfant pages 1-2) |
| Later liveborn case with glycomics confirmation | **ALG9** | Autosomal recessive (homozygous variant; both parents carriers) | c.860A>G, p.Tyr287Cys / p.Y287C | Facial dysmorphism, CNS involvement, developmental delay, failure to thrive; MRI with moderate global cerebral atrophy; prenatal renal cysts/minor cardiac malformations reported in broader review of literature | Transferrin IEF type I: decreased tetrasialo-Tf with increased disialo-Tf and small asialo-Tf; plasma and fibroblast LC-MS N-glycan profiling showed increased Man4-Man6 with absent/reduced Man7-Man9, consistent with ALG9 block (davis2017alg9cdgnewclinical pages 5-6, davis2017alg9cdgnewclinical media b6fa124e, davis2017alg9cdgnewclinical media 966d80b6) | Human case report / glycomics | 2017 | (davis2017alg9cdgnewclinical pages 5-6, davis2017alg9cdgnewclinical media b6fa124e, davis2017alg9cdgnewclinical media 966d80b6) |
| Lethal fetal skeletal dysplasia / Gillessen-Kaesbach–Nishimura syndrome end of spectrum | **ALG9** | Autosomal recessive (homozygous splice variant) | c.1173+2T>A (reported as c.1173+2T4A in extracted text due to formatting), splice donor; exon 10 skipping | Lethal fetal phenotype with skeletal dysplasia, polycystic kidneys, multiple malformations; characteristic round pelvis, mesomelic upper-limb shortening, defective cervical vertebral ossification; demonstrates severe prenatal end of ALG9-CDG spectrum | Mass spectrometric transferrin analysis showed increased monoglycosylated transferrin, confirming CDG; RNA analysis demonstrated exon 10 skipping (tham2016anovelphenotype pages 1-2) | Fetal pathology / exome / RNA study | 2016 | (tham2016anovelphenotype pages 1-2) |
| Saudi cohort / recurrent founder-like variant series | **ALG9** | Autosomal recessive (all homozygous in this cohort) | c.1075G>A, p.Glu359Lys / p.E359K | Eight patients from four unrelated families: dysmorphic features, early-onset refractory epilepsy, progressive microcephaly, severe developmental disability, failure to thrive, skeletal dysplasia, mild hepatomegaly with normal transaminases, hydrops fetalis; brain MRI with delayed myelination and cerebral/cerebellar atrophy | Clinical series emphasized phenotype; biochemical details not provided in extracted cohort text (alsubhi2017congenitaldisordersof pages 6-6) | Human case series | 2017 | (alsubhi2017congenitaldisordersof pages 6-6) |
| Cross-report phenotype synthesis | **ALG9** | Autosomal recessive | Missense variants (p.Y286C/p.Y287C, p.E523K/p.E530K) generally associated with liveborn disease; splice variant c.1173+2T>A associated with prenatal lethal presentation; recurrent p.E359K in Saudi cohort | Recurrent features across reports: neurodevelopmental delay/disability, hypotonia, seizures, progressive microcephaly, renal cysts/cystic kidneys, hepatomegaly, failure to thrive, pericardial effusion/cardiac tamponade, hydrops fetalis, and severe skeletal dysplasia/lethal fetal disease at the most severe end | Core diagnostic signature across reports: abnormal transferrin glycoforms (type I pattern or increased monoglycosylated transferrin), truncated LLO intermediates (Man6/Man8), and glycomics showing buildup of shorter high-mannose species (Man4-6) with loss of Man7-9 (tham2016anovelphenotype pages 1-2, davis2017alg9cdgnewclinical pages 7-9, davis2017alg9cdgnewclinical pages 1-2) | Human literature synthesis | 2016–2017 | (tham2016anovelphenotype pages 1-2, davis2017alg9cdgnewclinical pages 7-9, davis2017alg9cdgnewclinical pages 1-2) |


*Table: This table summarizes the main knowledge-base fields for ALG9-CDG/CDG-IL, including identifiers, inheritance, reported pathogenic variants, phenotype spectrum, and hallmark biochemical findings. It condenses the available human case reports, fetal pathology evidence, and broader literature synthesis into a citation-linked reference.*

---

## 1. Disease information
### 1.1 What is the disease?
ALG9-CDG is a congenital disorder of N-linked glycosylation due to defective **lipid-linked oligosaccharide (LLO)** assembly in the endoplasmic reticulum, leading to transfer of incomplete glycan precursors to proteins and under-occupancy of N-glycosylation sites (a “CDG type I” biochemical pattern) (frank2004identificationandfunctional pages 1-2, frank2004identificationandfunctional pages 2-5).

### 1.2 Key identifiers (available from retrieved sources)
- **Gene:** ALG9 (α1,2-mannosyltransferase) (tham2016anovelphenotype pages 1-2)
- **Historical disease name:** **CDG-IL** (defined as a novel CDG-I subtype in 2004) (frank2004identificationandfunctional pages 1-2)
- **Current naming convention:** gene-based “ALG9-CDG” used in modern CDG nosology (francisco2023congenitaldisordersof pages 1-2)

**Not retrievable in this run (gaps needing external database lookup):** OMIM disease number, Orphanet ID, ICD-10/ICD-11 code, MeSH, MONDO.

### 1.3 Synonyms / alternative names
- ALG9-CDG
- CDG-IL (historical subtype name)
- In the fetal-lethal extreme: Gillessen-Kaesbach–Nishimura syndrome due to ALG9 variants (as framed by Tham et al.) (tham2016anovelphenotype pages 1-2)

### 1.4 Evidence source type
The currently retrievable evidence is primarily **individual patients and small case series**, including fetal autopsy/genomics studies and country-specific cohorts, rather than large aggregated natural-history datasets specific to ALG9-CDG (tham2016anovelphenotype pages 1-2, weinstein2005cdg‐ilaninfant pages 1-2, alsubhi2017congenitaldisordersof pages 6-6).

---

## 2. Etiology
### 2.1 Disease causal factors
- **Genetic cause:** biallelic loss-of-function or deleterious missense/splice variants in **ALG9** impair LLO assembly and N-glycosylation (frank2004identificationandfunctional pages 1-2, tham2016anovelphenotype pages 1-2).
- **Mechanistic cause:** defects in ALG9 α1,2-mannosyltransferase activity lead to intracellular accumulation of truncated LLO intermediates (notably DolPP-GlcNAc2Man6 and DolPP-GlcNAc2Man8) and transfer of incomplete precursors to proteins (frank2004identificationandfunctional pages 2-5).

### 2.2 Risk factors
- **Consanguinity/family recurrence:** multiple reports involve homozygous variants and familial clustering, consistent with autosomal recessive inheritance and increased risk in consanguineous settings (davis2017alg9cdgnewclinical pages 1-2, alsubhi2017congenitaldisordersof pages 6-6).

### 2.3 Protective factors
No protective genetic or environmental factors were identified in the retrieved evidence.

### 2.4 Gene–environment interactions
No gene–environment interaction evidence specific to ALG9-CDG was identified in the retrieved sources.

---

## 3. Phenotypes
### 3.1 Phenotype spectrum (current understanding)
The phenotype spectrum spans:
- **Liveborn multisystem neurodevelopmental disease**: developmental delay/psychomotor retardation, hypotonia, seizures/epilepsy, progressive microcephaly, failure to thrive, and hepatomegaly (frank2004identificationandfunctional pages 1-2, weinstein2005cdg‐ilaninfant pages 1-2, alsubhi2017congenitaldisordersof pages 6-6).
- **Renal phenotype**: cystic kidneys/cystic renal disease and multiple small renal cysts (weinstein2005cdg‐ilaninfant pages 1-2, tham2016anovelphenotype pages 1-2).
- **Cardiac phenotype**: pericardial effusion (including prenatal detection) and progression to cardiac tamponade in at least one reported infant (weinstein2005cdg‐ilaninfant pages 1-2).
- **Severe prenatal end**: lethal fetal skeletal dysplasia with polycystic kidneys and multiple malformations (Gillessen-Kaesbach–Nishimura syndrome) (tham2016anovelphenotype pages 1-2).

### 3.2 Phenotype characteristics (onset, severity, progression)
- **Onset:** often prenatal (hydrops fetalis; pericardial effusion; renal cysts detectable by fetal imaging) to early infancy (failure to thrive, hypotonia, seizures) (weinstein2005cdg‐ilaninfant pages 1-2, alsubhi2017congenitaldisordersof pages 6-6).
- **Severity:** ranges from survivable but severe neurodevelopmental disability to **prenatal/neonatal lethality** in the skeletal dysplasia phenotype (tham2016anovelphenotype pages 1-2).
- **Progression:** progressive microcephaly has been emphasized in case reports/series; seizure control can be difficult (weinstein2005cdg‐ilaninfant pages 1-2, alsubhi2017congenitaldisordersof pages 6-6).

### 3.3 Approximate frequency of features (from the retrieved evidence)
Formal pooled percentages for ALG9-CDG features were not extractable from the retrieved texts. However, a Saudi cohort described **8 patients from 4 unrelated families** with a shared homozygous variant and recurrent features including refractory epilepsy, progressive microcephaly, skeletal dysplasia, and hydrops fetalis (alsubhi2017congenitaldisordersof pages 6-6).

### 3.4 Suggested HPO terms (non-exhaustive)
Based on the described phenotypes:
- **Seizures** (HP:0001250)
- **Developmental delay / intellectual disability** (HP:0001263 / HP:0001249)
- **Hypotonia** (HP:0001252)
- **Progressive microcephaly / microcephaly** (HP:0000252)
- **Failure to thrive** (HP:0001508)
- **Hepatomegaly** (HP:0002240)
- **Renal cysts / cystic kidney disease** (HP:0000107)
- **Pericardial effusion** (HP:0001698)
- **Hydrops fetalis** (HP:0001789)
- **Skeletal dysplasia / limb shortening / mesomelia** (e.g., HP:0002652; HP:0003027)

### 3.5 Quality-of-life impact
Direct validated quality-of-life instruments (e.g., EQ-5D, SF-36) were not found in the retrieved sources for ALG9-CDG. Nonetheless, severe developmental disability, refractory epilepsy, and multisystem involvement imply high caregiver burden and profound impairment in daily functioning (alsubhi2017congenitaldisordersof pages 6-6, weinstein2005cdg‐ilaninfant pages 1-2).

---

## 4. Genetic / molecular information
### 4.1 Causal gene
- **ALG9** encodes an ER α1,2-mannosyltransferase involved in **LLO biosynthesis** for N-glycosylation and is required for proper human development and physiology (frank2004identificationandfunctional pages 1-2).

### 4.2 Pathogenic variants (from retrieved primary reports)
Reported homozygous variants include:
- **c.1567G>A (p.Glu523Lys / E523K)** in the defining 2004 case (frank2004identificationandfunctional pages 2-5).
- **c.860A>G (p.Tyr286Cys / p.Y286C)** in the 2005 case (weinstein2005cdg‐ilaninfant pages 1-2).
- **c.860A>G (p.Tyr287Cys / p.Y287C)** in the 2017 case report with detailed glycomics (davis2017alg9cdgnewclinical pages 5-6).
- **c.1173+2T>A (splice donor; exon 10 skipping)** associated with lethal fetal skeletal dysplasia (tham2016anovelphenotype pages 1-2).
- **c.1075G>A (p.Glu359Lys / p.E359K)** in 8 Saudi patients (alsubhi2017congenitaldisordersof pages 6-6).

### 4.3 Variant type/class and functional consequences
- Variants include **missense** substitutions and **splice-site** disruption causing exon skipping and predicted frameshift/out-of-frame transcript (tham2016anovelphenotype pages 1-2).
- Functional validation in the defining work used **yeast complementation**, demonstrating that the patient allele impairs ALG9 function (residual activity noted), consistent with a loss-of-function/hypomorphic mechanism (frank2004identificationandfunctional pages 2-5).

### 4.4 Population allele frequency
One missense allele (Y287C) is described as very rare in population data (ExAC allele frequency reported in the 2017 review/case context), consistent with ultra-rare recessive disease (davis2017alg9cdgnewclinical pages 7-9).

### 4.5 Modifier genes / epigenetics / chromosomal abnormalities
No ALG9-CDG-specific modifier genes, epigenetic signatures, or recurrent chromosomal abnormalities were identified in the retrieved sources.

---

## 5. Environmental information
No environmental, lifestyle, toxin, radiation, or infectious triggers were identified as contributing factors in the retrieved evidence. ALG9-CDG is best supported as a primary monogenic disorder (frank2004identificationandfunctional pages 1-2, weinstein2005cdg‐ilaninfant pages 1-2).

---

## 6. Mechanism / pathophysiology
### 6.1 Pathway placement and biochemical chain of causality
1) **Primary trigger:** biallelic pathogenic ALG9 variants (frank2004identificationandfunctional pages 2-5, tham2016anovelphenotype pages 1-2).
2) **Molecular defect:** reduced ALG9 α1,2-mannosyltransferase function during ER LLO assembly; human ALG9 catalyzes mannose transfer onto at least two acceptor substrates (DolPP-GlcNAc2Man6 and DolPP-GlcNAc2Man8), consistent with dual-step involvement (frank2004identificationandfunctional pages 2-5).
3) **Biochemical consequence:** accumulation of truncated LLO intermediates (DolPP-GlcNAc2Man6 and DolPP-GlcNAc2Man8) and transfer of incomplete precursors to protein N-glycosylation sites (frank2004identificationandfunctional pages 2-5).
4) **Cellular consequence:** protein underglycosylation and aberrant glycan structures can perturb ER quality control (calnexin/calreticulin cycle), glycoprotein folding/trafficking, and ER-associated degradation (ERAD), proposed as contributors to phenotype (frank2004identificationandfunctional pages 2-5).
5) **Tissue/organ outcomes:** multisystem developmental and organ dysfunction, with prominent neurologic involvement; renal cystic disease; cardiac involvement such as pericardial effusion; and, in severe fetal cases, skeletal dysplasia with visceral malformations (tham2016anovelphenotype pages 1-2, weinstein2005cdg‐ilaninfant pages 1-2).

### 6.2 Direct abstract-quoted mechanistic evidence
- Defining paper (2004) explicitly ties mechanism to LLO intermediates: it reports “**a deficiency of the ALG9 α1,2 mannosyltransferase enzyme, which causes an accumulation of lipid-linked-GlcNAc2Man6 and -GlcNAc2Man8 structures**” and notes this was “**paralleled by the transfer of incomplete oligosaccharides precursors to protein**” (frank2004identificationandfunctional pages 1-2).
- 2017 case report glycomics: “**N-glycan profile… showed significant increase…Man4…Man5…Man6 with absence of…Man7…Man8…Man9**” and interprets “**blockage of N-glycan biosynthesis after Man6 indicated a probable defect in ALG9**” (davis2017alg9cdgnewclinical pages 5-6).
- Fetal-lethal phenotype: “**Mass spectrometric analysis showed an increase in monoglycosylated transferrin… confirming that this is a congenital disorder of glycosylation (CDG)**” and “**RNA analysis demonstrated skipping of exon 10**” for the splice variant (tham2016anovelphenotype pages 1-2).

### 6.3 Ontology suggestions
- **GO Biological Process:** protein N-linked glycosylation; dolichol-linked oligosaccharide biosynthetic process; glycoprotein folding/quality control (supported mechanistically) (frank2004identificationandfunctional pages 2-5).
- **GO Cellular Component:** endoplasmic reticulum membrane/lumen (ALG9 is a multispanning ER protein in the N-glycosylation pathway) (frank2004identificationandfunctional pages 2-5).
- **CL (cell types):** broad systemic involvement; evidence does not specify a single primary cell type, but fibroblast biochemical studies are commonly used diagnostically (patient fibroblasts studied) (frank2004identificationandfunctional pages 2-5, davis2017alg9cdgnewclinical pages 5-6).

### 6.4 Molecular profiling (omics)
Targeted N-glycan profiling by LC-MS in plasma and fibroblasts demonstrates a truncation signature (Man4–Man6 enrichment; Man7–Man9 depletion) consistent with pathway blockade at ALG9 (davis2017alg9cdgnewclinical pages 5-6).

---

## 7. Anatomical structures affected
### 7.1 Organ systems (supported by case literature)
- **Central nervous system:** diffuse brain atrophy, delayed myelination (weinstein2005cdg‐ilaninfant pages 1-2).
- **Kidney:** cystic renal disease / polycystic kidneys in severe fetal phenotype (tham2016anovelphenotype pages 1-2, weinstein2005cdg‐ilaninfant pages 1-2).
- **Heart/pericardium:** pericardial effusion and tamponade (weinstein2005cdg‐ilaninfant pages 1-2).
- **Liver/spleen:** hepatomegaly and hepatosplenomegaly (weinstein2005cdg‐ilaninfant pages 1-2, frank2004identificationandfunctional pages 1-2).
- **Skeletal system:** lethal fetal skeletal dysplasia phenotype; skeletal dysplasia also reported in pediatric cohort (tham2016anovelphenotype pages 1-2, alsubhi2017congenitaldisordersof pages 6-6).

### 7.2 UBERON suggestions (non-exhaustive)
- Brain; kidney; liver; heart/pericardium; skeletal system (supported by multi-organ clinical findings) (tham2016anovelphenotype pages 1-2, weinstein2005cdg‐ilaninfant pages 1-2).

### 7.3 Subcellular localization
Endoplasmic reticulum (ER) LLO assembly pathway (frank2004identificationandfunctional pages 2-5).

---

## 8. Temporal development
- **Prenatal manifestations:** pericardial effusion; renal cysts; hydrops fetalis; fetal skeletal dysplasia with lethality for severe splice variant cases (tham2016anovelphenotype pages 1-2, weinstein2005cdg‐ilaninfant pages 1-2, alsubhi2017congenitaldisordersof pages 6-6).
- **Infant/childhood course:** hypotonia, failure to thrive, seizures with difficult control, progressive microcephaly and neurodevelopmental impairment (weinstein2005cdg‐ilaninfant pages 1-2, alsubhi2017congenitaldisordersof pages 6-6).

---

## 9. Inheritance and population
### 9.1 Inheritance
Autosomal recessive inheritance is supported by homozygous variants in affected children/fetuses and parental heterozygosity in families (davis2017alg9cdgnewclinical pages 5-6, weinstein2005cdg‐ilaninfant pages 1-2).

### 9.2 Epidemiology
ALG9-CDG is ultra-rare; early literature comprised a small number of families, but notable aggregation has been reported in regional cohorts. In a Saudi CDG cohort, ALG9-CDG accounted for **8 patients from 4 unrelated families**, reported as **28.5% of the cohort’s CDG population** (cohort composition rather than population prevalence) (alsubhi2017congenitaldisordersof pages 6-6). CDG-wide epidemiology reviews emphasize that generating robust prevalence/incidence data for CDG is challenging and often relies on case reports/series and allelic frequency, and also provide context that CDG are collectively rare inherited metabolic disorders (piedade2022epidemiologyofcongenital pages 1-2).

### 9.3 Population genetics
No robust carrier-frequency estimates for ALG9-CDG were extractable from the retrieved texts; one reported allele is extremely rare in population databases (ExAC) (davis2017alg9cdgnewclinical pages 7-9).

---

## 10. Diagnostics
### 10.1 Biochemical testing
- **Transferrin isoelectric focusing (TIEF):** characteristic **CDG type I pattern**, e.g., increased disialo-/asialo-transferrin and decreased tetrasialo-transferrin (frank2004identificationandfunctional pages 2-5, davis2017alg9cdgnewclinical pages 5-6).
- **LLO analysis in patient fibroblasts:** accumulation of **DolPP-GlcNAc2Man6** and **DolPP-GlcNAc2Man8** (frank2004identificationandfunctional pages 2-5, weinstein2005cdg‐ilaninfant pages 1-2).
- **Mass spectrometry glycomics / N-glycan profiling:** truncation signature consistent with ALG9 blockade, including increased Man4–Man6 and depletion/absence of Man7–Man9 (davis2017alg9cdgnewclinical pages 5-6, davis2017alg9cdgnewclinical media b6fa124e).

**Image evidence (real-world implementation of glycomics):** Figures demonstrating the diagnostic N-glycan signature in plasma and fibroblasts are available from the 2017 clinical case report (davis2017alg9cdgnewclinical media b6fa124e, davis2017alg9cdgnewclinical media 966d80b6).

### 10.2 Genetic testing
- Confirmatory molecular diagnosis was achieved via targeted sequencing after biochemical suspicion (davis2017alg9cdgnewclinical pages 5-6) and via exome + RNA studies in fetal cases (tham2016anovelphenotype pages 1-2).
- Modern CDG practice has shifted from purely transferrin-pattern based naming to gene-based nosology, reflecting widespread adoption of NGS (francisco2023congenitaldisordersof pages 1-2).

### 10.3 Differential diagnosis
The fetal skeletal dysplasia phenotype overlaps with ALG3- and ALG12-CDG skeletal features, motivating a diagnostic grouping of certain N-glycosylation disorders within skeletal dysplasias (tham2016anovelphenotype pages 1-2).

---

## 11. Outcome / prognosis
Prognosis is variable:
- **Prenatal-lethal** outcomes are documented for severe splice-variant-associated skeletal dysplasia with visceral malformations (tham2016anovelphenotype pages 1-2).
- **Survival with severe neurodevelopmental impairment** is documented in liveborn cases; severe epilepsy and progressive microcephaly can occur, and cardiac tamponade secondary to pericardial effusion is a life-threatening complication (weinstein2005cdg‐ilaninfant pages 1-2).

Quantitative survival curves or life expectancy data were not available in the retrieved evidence.

---

## 12. Treatment
### 12.1 Disease-specific therapy
No ALG9-CDG-specific targeted therapy was identified in the retrieved sources.

### 12.2 Supportive/standard-of-care elements (real-world implementations)
- **Epilepsy management:** antiepileptic therapy is used; seizure control may be difficult (weinstein2005cdg‐ilaninfant pages 1-2, alsubhi2017congenitaldisordersof pages 6-6).
- **Management of pericardial effusion/tamponade:** pericardiocentesis was required in at least one case due to tamponade (weinstein2005cdg‐ilaninfant pages 1-2).
- **Nutritional support / failure-to-thrive management:** failure to thrive is prominent in reported cases and requires supportive care, although specific protocols were not detailed in the retrieved texts (weinstein2005cdg‐ilaninfant pages 1-2, alsubhi2017congenitaldisordersof pages 6-6).

### 12.3 CDG expert recommendations relevant to ALG9-CDG (2024)
A 2024 analysis from the Frontiers in Congenital Disorders of Glycosylation Consortium (FCDGC) provides expert recommendations for **baseline and longitudinal cardiac surveillance** (echocardiogram and ECG at diagnosis; annual in early childhood with spacing later) due to cardiomyopathy/pericardial effusion risks in CDG broadly (zemet2024cardiomyopathyanuncommon pages 1-3). While ALG9-CDG was not among the cardiomyopathy cases listed, pericardial effusion is clearly part of ALG9-CDG phenotypes, making structured cardiac surveillance clinically prudent (weinstein2005cdg‐ilaninfant pages 1-2, zemet2024cardiomyopathyanuncommon pages 1-3).

### 12.4 Suggested MAXO terms (examples)
- Antiepileptic drug therapy (MAXO: antiepileptic therapy)
- Pericardiocentesis / pericardial drainage procedure
- Nutritional support / enteral nutrition
- Cardiac surveillance (echocardiography; electrocardiography)

---

## 13. Prevention
No primary prevention is currently established for ALG9-CDG. Prevention focuses on **genetic counseling and reproductive options**:
- **Carrier testing and cascade testing** in families with a known pathogenic variant.
- **Prenatal diagnosis** is feasible (fetal ultrasound findings plus molecular testing), and fetal presentation has been described for severe cases (tham2016anovelphenotype pages 1-2, weinstein2005cdg‐ilaninfant pages 1-2).

---

## 14. Other species / natural disease
No naturally occurring ALG9-CDG-like disease in non-human species was identified in the retrieved evidence.

---

## 15. Model organisms
### 15.1 Functional models used in the evidence base
- **Yeast complementation assays** were used to demonstrate functional homology between human and yeast ALG9 and the deleterious effect of patient variants, providing strong mechanistic support (frank2004identificationandfunctional pages 2-5).

### 15.2 Translational relevance and limitations
Yeast assays robustly establish enzymatic pathway function and variant impact but do not recapitulate the multi-organ developmental phenotypes; vertebrate models were not retrieved in this run.

---

## Recent developments (2023–2024 prioritized)
### 2023: CDG field state-of-the-art (context relevant to ALG9-CDG)
A 2023 “state of the art in 2022” review emphasizes that CDG are a heterogeneous family of rare metabolic diseases and highlights that **multi-omics advances** have accelerated progress but **targeted therapies remain a major unmet need**; it also documents the modern **gene-based nomenclature** and challenges in CDG classification (francisco2023congenitaldisordersof pages 1-2).

### 2024: Expert guidance on cardiac monitoring in CDG
A 2024 FCDGC study identified cardiomyopathy in approximately **~6%** of 305 molecularly confirmed CDG patients in their cohort and proposed standardized cardiac screening/follow-up (zemet2024cardiomyopathyanuncommon pages 1-3). Even though ALG9-CDG was not specifically represented among their cardiomyopathy subset, the presence of pericardial effusion/tamponade in ALG9-CDG case reports supports heightened cardiac vigilance (weinstein2005cdg‐ilaninfant pages 1-2).

---

## URLs and publication dates (where available from retrieved texts)
- Frank CG et al. *Am J Hum Genet* (published electronically **May 17, 2004**). https://doi.org/10.1086/422367 (frank2004identificationandfunctional pages 1-2)
- Weinstein M et al. *Am J Med Genet A* (**2005**). https://doi.org/10.1002/ajmg.a.30851 (weinstein2005cdg‐ilaninfant pages 1-2)
- Tham E et al. *Eur J Hum Genet* (published online **May 13, 2015**; journal issue **2016**). https://doi.org/10.1038/ejhg.2015.91 (tham2016anovelphenotype pages 1-2)
- Davis K et al. *Mol Genet Metab Rep* (**Dec 2017**). https://doi.org/10.1016/j.ymgmr.2017.08.004 (davis2017alg9cdgnewclinical pages 1-2)
- Francisco R et al. *Orphanet J Rare Dis* (**Oct 2023**). https://doi.org/10.1186/s13023-023-02879-z (francisco2023congenitaldisordersof pages 1-2)
- Zemet R et al. *Mol Genet Metab* (**Aug 2024**). https://doi.org/10.1016/j.ymgme.2024.108513 (zemet2024cardiomyopathyanuncommon pages 1-3)
- Piedade A et al. *Journal of Rare Diseases* (**Dec 2022**). https://doi.org/10.1007/s44162-022-00003-6 (piedade2022epidemiologyofcongenital pages 1-2)

---

## Limitations of this report (important for knowledge-base curation)
1) **Ontology IDs** (OMIM/Orphanet/MONDO/ICD/MeSH) and **PMIDs** were not retrievable with the available tools in this run; the report therefore prioritizes DOI/URLs and direct excerpts from accessible full text. 
2) ALG9-CDG remains ultra-rare; **feature frequencies, survival statistics, and validated QoL metrics** are not well defined in the retrieved primary literature.
3) **ALG9-specific 2023–2024 primary case expansions** were not retrievable here; “latest research” sections therefore focus on CDG-wide advances and consensus recommendations.


References

1. (frank2004identificationandfunctional pages 1-2): Christian G. Frank, Wafaa Eyaid, Eric G. Berger, Markus Aebi, Claudia E. Grubenmann, and Thierry Hennet. Identification and functional analysis of a defect in the human alg9 gene: definition of congenital disorder of glycosylation type il. The American Journal of Human Genetics, 75:146-150, Jul 2004. URL: https://doi.org/10.1086/422367, doi:10.1086/422367. This article has 117 citations.

2. (davis2017alg9cdgnewclinical pages 5-6): Kellie Davis, Duncan Webster, Chris Smith, Sheryl Jackson, David Sinasac, Lorne Seargeant, Xing-Chang Wei, Patrick Ferreira, Julian Midgley, Yolanda Foster, Xueli Li, Miao He, and Walla Al-Hertani. Alg9-cdg: new clinical case and review of the literature. Molecular Genetics and Metabolism Reports, 13:55-63, Dec 2017. URL: https://doi.org/10.1016/j.ymgmr.2017.08.004, doi:10.1016/j.ymgmr.2017.08.004. This article has 29 citations.

3. (tham2016anovelphenotype pages 1-2): Emma Tham, Erik A Eklund, Anna Hammarsjö, Per Bengtson, Stefan Geiberger, Kristina Lagerstedt-Robinson, Helena Malmgren, Daniel Nilsson, Gintautas Grigelionis, Peter Conner, Peter Lindgren, Anna Lindstrand, Anna Wedell, Margareta Albåge, Katarzyna Zielinska, Ann Nordgren, Nikos Papadogiannakis, Gen Nishimura, and Giedre Grigelioniene. A novel phenotype in n-glycosylation disorders: gillessen-kaesbach–nishimura skeletal dysplasia due to pathogenic variants in alg9. European Journal of Human Genetics, 24:198-207, May 2016. URL: https://doi.org/10.1038/ejhg.2015.91, doi:10.1038/ejhg.2015.91. This article has 44 citations and is from a domain leading peer-reviewed journal.

4. (weinstein2005cdg‐ilaninfant pages 1-2): Michael Weinstein, Els Schollen, Gert Matthijs, Christine Neupert, Thierry Hennet, Claudia E. Grubenmann, Christian G. Frank, Markus Aebi, Joe T. R. Clarke, Anne Griffiths, Lorne Seargeant, and Nicola Poplawski. Cdg‐il: an infant with a novel mutation in the alg9 gene and additional phenotypic features. American Journal of Medical Genetics Part A, 136A:194-197, Jul 2005. URL: https://doi.org/10.1002/ajmg.a.30851, doi:10.1002/ajmg.a.30851. This article has 55 citations.

5. (frank2004identificationandfunctional pages 2-5): Christian G. Frank, Wafaa Eyaid, Eric G. Berger, Markus Aebi, Claudia E. Grubenmann, and Thierry Hennet. Identification and functional analysis of a defect in the human alg9 gene: definition of congenital disorder of glycosylation type il. The American Journal of Human Genetics, 75:146-150, Jul 2004. URL: https://doi.org/10.1086/422367, doi:10.1086/422367. This article has 117 citations.

6. (francisco2023congenitaldisordersof pages 1-2): Rita Francisco, Sandra Brasil, Joana Poejo, Jaak Jaeken, Carlota Pascoal, Paula A. Videira, and Vanessa dos Reis Ferreira. Congenital disorders of glycosylation (cdg): state of the art in 2022. Orphanet Journal of Rare Diseases, Oct 2023. URL: https://doi.org/10.1186/s13023-023-02879-z, doi:10.1186/s13023-023-02879-z. This article has 72 citations and is from a peer-reviewed journal.

7. (davis2017alg9cdgnewclinical media b6fa124e): Kellie Davis, Duncan Webster, Chris Smith, Sheryl Jackson, David Sinasac, Lorne Seargeant, Xing-Chang Wei, Patrick Ferreira, Julian Midgley, Yolanda Foster, Xueli Li, Miao He, and Walla Al-Hertani. Alg9-cdg: new clinical case and review of the literature. Molecular Genetics and Metabolism Reports, 13:55-63, Dec 2017. URL: https://doi.org/10.1016/j.ymgmr.2017.08.004, doi:10.1016/j.ymgmr.2017.08.004. This article has 29 citations.

8. (davis2017alg9cdgnewclinical media 966d80b6): Kellie Davis, Duncan Webster, Chris Smith, Sheryl Jackson, David Sinasac, Lorne Seargeant, Xing-Chang Wei, Patrick Ferreira, Julian Midgley, Yolanda Foster, Xueli Li, Miao He, and Walla Al-Hertani. Alg9-cdg: new clinical case and review of the literature. Molecular Genetics and Metabolism Reports, 13:55-63, Dec 2017. URL: https://doi.org/10.1016/j.ymgmr.2017.08.004, doi:10.1016/j.ymgmr.2017.08.004. This article has 29 citations.

9. (alsubhi2017congenitaldisordersof pages 6-6): Sarah Alsubhi, Amal Alhashem, Eissa Faqeih, Majid Alfadhel, Abdullah Alfaifi, Waleed Altuwaijri, Saud Alsahli, Hesham Aldhalaan, Fowzan S. Alkuraya, Khalid Hundallah, Adel Mahmoud, Ali Alasmari, Fuad Al Mutairi, Hanem Abduraouf, Layan AlRasheed, Saad Alshahwan, and Brahim Tabarki. Congenital disorders of glycosylation: the saudi experience. American Journal of Medical Genetics Part A, 173:2614-2621, Jul 2017. URL: https://doi.org/10.1002/ajmg.a.38358, doi:10.1002/ajmg.a.38358. This article has 45 citations.

10. (davis2017alg9cdgnewclinical pages 7-9): Kellie Davis, Duncan Webster, Chris Smith, Sheryl Jackson, David Sinasac, Lorne Seargeant, Xing-Chang Wei, Patrick Ferreira, Julian Midgley, Yolanda Foster, Xueli Li, Miao He, and Walla Al-Hertani. Alg9-cdg: new clinical case and review of the literature. Molecular Genetics and Metabolism Reports, 13:55-63, Dec 2017. URL: https://doi.org/10.1016/j.ymgmr.2017.08.004, doi:10.1016/j.ymgmr.2017.08.004. This article has 29 citations.

11. (davis2017alg9cdgnewclinical pages 1-2): Kellie Davis, Duncan Webster, Chris Smith, Sheryl Jackson, David Sinasac, Lorne Seargeant, Xing-Chang Wei, Patrick Ferreira, Julian Midgley, Yolanda Foster, Xueli Li, Miao He, and Walla Al-Hertani. Alg9-cdg: new clinical case and review of the literature. Molecular Genetics and Metabolism Reports, 13:55-63, Dec 2017. URL: https://doi.org/10.1016/j.ymgmr.2017.08.004, doi:10.1016/j.ymgmr.2017.08.004. This article has 29 citations.

12. (piedade2022epidemiologyofcongenital pages 1-2): Ana Piedade, Rita Francisco, Jaak Jaeken, Peymaneh Sarkhail, Sandra Brasil, Carlos R. Ferreira, Tatiana Rijoff, Carlota Pascoal, Alexandre Gil, Ana Beatriz Lourenço, Marta Abreu, Mafalda Gomes, Paula A. Videira, and Vanessa dos Reis Ferreira. Epidemiology of congenital disorders of glycosylation (cdg)—overview and perspectives. Journal of Rare Diseases, Dec 2022. URL: https://doi.org/10.1007/s44162-022-00003-6, doi:10.1007/s44162-022-00003-6. This article has 35 citations.

13. (zemet2024cardiomyopathyanuncommon pages 1-3): Roni Zemet, Kyle D. Hope, Andrew C. Edmondson, Rameen Shah, Maria Patino, Abigail M. Yesso, Justin H. Berger, Kyriakie Sarafoglou, Austin Larson, Christina Lam, Eva Morava, and Fernando Scaglia. Cardiomyopathy, an uncommon phenotype of congenital disorders of glycosylation: recommendations for baseline screening and follow-up evaluation. Molecular Genetics and Metabolism, 142:108513, Aug 2024. URL: https://doi.org/10.1016/j.ymgme.2024.108513, doi:10.1016/j.ymgme.2024.108513. This article has 14 citations and is from a peer-reviewed journal.