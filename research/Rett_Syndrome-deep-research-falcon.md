---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-25T22:18:12.945423'
end_time: '2026-04-25T22:29:03.465840'
duration_seconds: 650.52
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Rett Syndrome
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 33
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Rett Syndrome
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Rett Syndrome** covering all of the
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
- **Disease Name:** Rett Syndrome
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Rett Syndrome** covering all of the
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


# Rett Syndrome — Comprehensive Disease Characteristics Research Report (Genetic)

## Target Disease
- **Disease name:** Rett syndrome (RTT) (gold2024rettsyndrome pages 1-2)
- **Category:** Genetic neurodevelopmental disorder (gold2024rettsyndrome pages 1-2)
- **MONDO ID:** Not retrieved in the available evidence corpus; should be obtained from Mondo Disease Ontology (not available via current tool state).

## Executive overview
Rett syndrome is a severe, progressive neurodevelopmental disorder that predominantly affects females and is a common genetic cause of intellectual disability in girls. It is classically characterized by a period of apparently typical early development followed by developmental stagnation/regression with loss of spoken language and purposeful hand skills, emergence of stereotypic hand movements, and gait abnormalities. Most cases are caused by **de novo loss-of-function variants in the X-linked gene MECP2 (Xq28)**. (gold2024rettsyndrome pages 1-2, neul2023trofinetideforthe pages 1-2)

**Direct abstract quote (phase 3 trofinetide trial, 2023):** “Rett syndrome is a rare, genetic neurodevelopmental disorder.” (neul2023trofinetideforthe pages 1-2)

---

## 1. Disease information
### 1.1 What is the disease?
RTT is a multisystem neurodevelopmental disorder with prominent neurological, autonomic/respiratory, gastrointestinal, orthopedic, and behavioral comorbidities described in modern natural history and review literature. (percy2024rettsyndromethe pages 1-2, gold2024rettsyndrome pages 1-2)

### 1.2 Key identifiers
A partial set of identifiers is available from the retrieved sources:
- **OMIM:** **312750** (camillo2024profileoftrofinetide pages 1-2)
- **Causal gene/locus:** **MECP2**, **Xq28** (percy2024rettsyndromethe pages 1-2, gold2024rettsyndrome pages 1-2)

Other requested identifiers were **not directly retrievable from the current evidence set**:
- **Orphanet ID, ICD-10/ICD-11 code, MeSH descriptor, MONDO ID:** not present in retrieved texts; should be pulled from Orphanet/ICD/MeSH/Mondo resources.

### 1.3 Synonyms / alternative names
- RTT; **classic (typical) Rett syndrome**; **atypical Rett syndrome** (may2024characterizingthejourney pages 1-2)

### 1.4 Evidence provenance: individual vs aggregated
Most information in this report is derived from:
- **Aggregated disease-level resources and synthesis reviews** (Nature Reviews Disease Primers 2024; CNS Drugs 2024) (gold2024rettsyndrome pages 1-2, percy2024rettsyndromethe pages 1-2)
- **Aggregated registry/natural history data** (RNHS registry-based real-world evidence study, N=455 females) (may2024characterizingthejourney pages 1-2, may2024characterizingthejourney pages 2-4)
- **Randomized controlled trial evidence** for treatment (phase 3 LAVENDER trial of trofinetide) (neul2023trofinetideforthe pages 2-3, neul2023trofinetideforthe pages 1-2)

A compact identifiers summary table is provided here:

| Item | Value | Source publication year | URL | Source row citation |
|---|---|---:|---|---|
| Disease name | Rett syndrome (RTT) | 2024 | https://doi.org/10.1038/s41572-024-00568-0 | (gold2024rettsyndrome pages 1-2) |
| Synonyms / alternative names | RTT; classic Rett syndrome; atypical Rett syndrome | 2024 | https://doi.org/10.1186/s11689-024-09557-6 | (may2024characterizingthejourney pages 1-2) |
| OMIM number | OMIM #312750 | 2024 | https://doi.org/10.2147/DDDT.S383133 | (camillo2024profileoftrofinetide pages 1-2) |
| Causal gene and locus | MECP2; Xq28 | 2024 | https://doi.org/10.1007/s40263-024-01106-y | (percy2024rettsyndromethe pages 1-2) |
| Key diagnostic main criteria (4) | Loss of acquired purposeful hand skills; loss of spoken language; stereotypic hand movements; gait abnormalities | 2024 | https://doi.org/10.1186/s11689-024-09557-6 | (may2024characterizingthejourney pages 1-2) |
| Incidence | Approximately 1 in 10,000–15,000 live female births | 2024 | https://doi.org/10.1186/s11689-024-09557-6 | (may2024characterizingthejourney pages 1-2) |
| Prevalence | 7.1 per 100,000 females (95% CI 4.8–10.5) | 2023 | https://doi.org/10.1186/s13643-023-02169-6 | (petriti2023globalprevalenceof pages 1-2) |


*Table: This table summarizes core disease identifiers and nomenclature for Rett syndrome, including OMIM, causal gene locus, defining diagnostic criteria, and headline epidemiology figures. It is useful as a compact, citable reference for a disease knowledge base entry.*

---

## 2. Etiology
### 2.1 Disease causal factors
**Primary cause:** Pathogenic variants in **MECP2**, encoding methyl-CpG-binding protein 2 (MeCP2), a DNA-binding protein involved in epigenetic regulation of gene expression. (neul2023trofinetideforthe pages 1-2, gold2024rettsyndrome pages 1-2)

**Direct abstract quote (trofinetide development review, 2024):** “Rett syndrome (RTT) is rare neurodevelopmental disorder caused by mutations in the MECP2 gene that encodes methyl-CpG-binding protein 2 (MeCP2), a DNA-binding protein with roles in epigenetic regulation of gene expression.” (kennedy2024developmentoftrofinetide pages 1-2)

### 2.2 Risk factors
- **Sex:** Predominantly affects females; epidemiology commonly framed in females, and incidence estimates are reported for live female births. (neul2023trofinetideforthe pages 1-2, may2024characterizingthejourney pages 1-2)
- **Genetic:** Most classic RTT is caused by **spontaneous/de novo MECP2 mutation** on the X chromosome; real-world review notes “In 90–95% of classic RTT, a spontaneous MECP2 mutation on the X chromosome is causal.” (may2024characterizingthejourney pages 1-2)

### 2.3 Protective factors
No protective genetic variants or environmental protective factors were identified in the retrieved evidence set.

### 2.4 Gene–environment interactions
No gene–environment interaction evidence was identified in the retrieved evidence set.

### 2.5 Genetic architecture details (hotspots)
A 2024 disease primer reports that most cases are associated with **de novo loss-of-function variants in MECP2**, including **>300 LOF variants**, with **eight hotspot pathogenic variants** comprising **>60%** of documented cases; hotspots often reflect C-to-T transitions at methylated CpG sites. (gold2024rettsyndrome pages 1-2)

**Ontology suggestions (etiology):**
- **MONDO:** Rett syndrome (to be filled)
- **Gene:** MECP2 (HGNC symbol: MECP2; not retrieved here)

---

## 3. Phenotypes
### 3.1 Core phenotype set and natural history (symptoms/signs)
The classic developmental trajectory includes:
- **Apparently typical early development** for ~6 months
- **Failure to meet milestones** by 6–18 months
- **Regression** typically at ~12–30 months with loss of hand skills and spoken language and emergence of stereotypic hand movements and gait dysfunction
- **Relative stabilization** from ~5 years onward, with possible later loss of ambulation (neul2023trofinetideforthe pages 1-2)

### 3.2 Phenotype frequencies (from RNHS real-world cohort)
In the US RNHS registry cohort (N=455 females; 90.5% classic), high-prevalence clinical features included:
- **Loss of language:** 95.8%
- **Hand stereotypies:** 92.3%
- **Respiratory dysfunction:** 75.8%
- **Sleep disturbances:** 75.6%
- **Constipation:** 74.5% (may2024characterizingthejourney pages 2-4)

Classic RTT had higher prevalence than atypical RTT for several features (e.g., loss of language 99.5% vs 60.5%; hand stereotypies 94.4% vs 72.1%; respiratory dysfunction 79.1% vs 44.2%). (may2024characterizingthejourney pages 2-4)

### 3.3 Quality of life impact
Registry and review evidence indicates substantial burden and reliance on supportive therapies and healthcare encounters, consistent with significant functional impairment affecting communication, mobility, and daily living. (may2024characterizingthejourney pages 1-2, may2024characterizingthejourney pages 9-10)

### 3.4 Suggested HPO terms (examples)
(These are ontology suggestions; exact term IDs should be verified in HPO.)
- Loss of purposeful hand skills → *Loss of hand skills* / *Apraxia* (HPO suggestion)
- Loss of spoken language → *Absent speech* / *Loss of speech* (HPO suggestion)
- Hand stereotypies → *Stereotypy* / *Hand wringing* (HPO suggestion)
- Gait abnormalities → *Abnormal gait* (HPO suggestion)
- Breathing abnormalities/respiratory dysfunction → *Abnormal breathing pattern* (HPO suggestion)
- Constipation → *Constipation* (HPO suggestion)
- Sleep disturbance → *Sleep disturbance* (HPO suggestion)

---

## 4. Genetic / molecular information
### 4.1 Causal genes
- **MECP2** is the major causal gene for RTT. (gold2024rettsyndrome pages 1-2, neul2023trofinetideforthe pages 1-2)

### 4.2 Inheritance
RTT is typically discussed as an X-linked disorder with predominantly **de novo** variants in affected females; incidence is often cited as ~1 in 10,000–15,000 live female births. (neul2023trofinetideforthe pages 1-2, may2024characterizingthejourney pages 1-2)

### 4.3 Pathogenic variants (high-level)
- The 2024 primer describes extensive allelic heterogeneity with **>300 LOF variants** and concentration into **hotspot variants** (eight hotspots comprising >60% of cases). (gold2024rettsyndrome pages 1-2)

### 4.4 Modifier genes / epigenetics
- A 2024 study in a clinical care setting evaluated common MTHFR genotypes as potential associative modifiers of clinical severity (not a causal factor). (may2024characterizingthejourney pages 2-4)

Epigenetic mechanism is central because MeCP2 binds methylated DNA and links to histone deacetylation, functioning in transcriptional regulation; functional loss results in broad transcriptional dysregulation. (gold2024rettsyndrome pages 1-2, kennedy2024developmentoftrofinetide pages 1-2)

**Ontology suggestions:**
- **GO (molecular function/process examples):** DNA-binding; regulation of transcription; chromatin organization (suggestions grounded conceptually in MeCP2 biology; exact GO IDs not retrieved here). (gold2024rettsyndrome pages 1-2)

---

## 5. Environmental information
No specific environmental/lifestyle/infectious causal contributors were identified in the retrieved evidence set. RTT is primarily genetic, and available sources emphasize genetic causation. (gold2024rettsyndrome pages 1-2, kennedy2024developmentoftrofinetide pages 1-2)

---

## 6. Mechanism / pathophysiology
### 6.1 Current understanding (key concepts)
MeCP2 is highly expressed in brain and is described as a key regulator linking methylated DNA to chromatin/histone state; MeCP2 deficiency is associated with reduced brain size, smaller neurons, and alterations across neurotransmitter systems. (gold2024rettsyndrome pages 1-2)

A mechanistic chain consistent with the retrieved sources:
1) **De novo MECP2 loss-of-function** →
2) **Disrupted epigenetic/transcriptional regulation** (MeCP2 DNA binding; chromatin linking) →
3) **Abnormal neuronal maturation and plasticity** →
4) **Circuit-level dysfunction and multisystem manifestations** (communication/motor regression; breathing abnormalities; GI dysfunction; seizures). (kennedy2024developmentoftrofinetide pages 1-2, neul2023trofinetideforthe pages 1-2, percy2024rettsyndromethe pages 1-2)

### 6.2 Recent developments (2023–2024): single-cell transcriptomics of progression
Sharifi et al. (2024) used longitudinal cortical snRNA-seq in a construct-relevant Mecp2e1 mutant mouse model, analyzing **93,798 nuclei** across presymptomatic, onset, and late stages. They report strong sex- and stage-dependent transcriptional dysregulation, with **~6× more differentially expressed genes (DEGs) in mutant females than males**, and that female DEGs emerged **prior to symptoms** and were enriched for homeostatic pathways. They highlight prominent **non-cell-autonomous effects** across progression, consistent with mosaic X-inactivation biology. (sharifi2024sexspecificsinglecelllevel pages 1-2, sharifi2024sexspecificsinglecelllevel pages 3-4)

### 6.3 Suggested GO and CL terms (examples)
- **GO Biological Process (suggested):** regulation of transcription; synaptic signaling; neuronal development; homeostatic process (supported conceptually by transcriptomic enrichment descriptions). (sharifi2024sexspecificsinglecelllevel pages 1-2)
- **CL Cell types (suggested):** excitatory cortical neurons (layer-specific), inhibitory interneuron subtypes (e.g., Pvalb, Vip, Sst), oligodendrocytes (all explicitly analyzed in the study). (sharifi2024sexspecificsinglecelllevel pages 3-4, sharifi2024sexspecificsinglecelllevel pages 5-6)

---

## 7. Anatomical structures affected
### 7.1 Organ/system level
Central nervous system involvement is primary, but RTT is described as multisystem with comorbidities involving breathing/respiratory control, gastrointestinal dysfunction, and orthopedic issues (e.g., scoliosis). (percy2024rettsyndromethe pages 1-2, neul2023trofinetideforthe pages 1-2)

### 7.2 Tissue/cell level
Single-cell studies highlight diverse cortical neuronal and non-neuronal cell types impacted over disease progression, supporting cell-type-specific and non-cell-autonomous mechanisms. (sharifi2024sexspecificsinglecelllevel pages 1-2)

**UBERON term suggestions:**
- Cerebral cortex (UBERON suggestion)

---

## 8. Temporal development
RTT classically shows regression after early development, often described as:
- Early stagnation around **6–18 months** and regression around toddler years, with subsequent stabilization, consistent with both clinical trial background and review staging descriptions. (neul2023trofinetideforthe pages 1-2, camillo2024profileoftrofinetide pages 1-2)

In the RNHS cohort, mean age of motor/communication regression was **2.3 (0.8) years**. (may2024characterizingthejourney pages 2-4)

---

## 9. Inheritance and population
### 9.1 Epidemiology
- **Incidence:** commonly cited as **~1 in 10,000–15,000 live female births**. (neul2023trofinetideforthe pages 1-2, may2024characterizingthejourney pages 1-2)
- **Global prevalence (meta-analysis):** pooled prevalence **7.1 per 100,000 females (95% CI 4.8–10.5)** based on 10 studies totaling **9.57 million women** and **673 RTT cases**. (petriti2023globalprevalenceof pages 1-2)

Petriti et al. additionally summarize that estimates are broadly compatible with a prevalence range of **~5–10 per 100,000 females**. (petriti2023globalprevalenceof pages 1-2)

### 9.2 Survival / prognosis (headline)
Registry-based and review-level evidence indicates survival into adulthood is common, with a cited estimate that survival is **>70% at 45 years**. (may2024characterizingthejourney pages 1-2)

---

## 10. Diagnostics
### 10.1 Clinical criteria
Classic RTT diagnosis requires four main criteria:
- Loss of acquired purposeful hand skills
- Loss of spoken language
- Stereotypic hand movements
- Gait abnormalities (may2024characterizingthejourney pages 1-2)

Atypical RTT requires ≥2 main criteria plus ≥5 of 11 supportive criteria (supportive criteria list not retrieved in current evidence). (may2024characterizingthejourney pages 1-2)

### 10.2 Genetic testing
Genetic confirmation frequently involves identifying a pathogenic MECP2 variant; the RNHS cohort reports MECP2-positive status in **98.2%** (cohort with high classic RTT proportion). (may2024characterizingthejourney pages 2-4)

### 10.3 Biomarkers / imaging / electrophysiology
Specific validated biomarkers or imaging signatures were not extracted from the currently retrieved texts; the RNHS and trial literature emphasize clinical scales and caregiver/clinician-reported outcomes. (neul2023trofinetideforthe pages 2-3, may2024characterizingthejourney pages 1-2)

---

## 11. Outcome / prognosis
In the RNHS real-world evidence study, pediatric individuals showed increasing trends in clinical severity and motor-behavioral dysfunction over follow-up:
- CSS change/year in pediatrics: **0.24 (95% CI 0.03–0.44)**
- MBA change/year in pediatrics: **1.12 (95% CI 0.63–1.60)** (may2024characterizingthejourney pages 1-2)

Healthcare utilization burden was high: **44.6%** had a hospital or emergency room visit during median 4-year follow-up. (may2024characterizingthejourney pages 1-2)

---

## 12. Treatment
### 12.1 Approved pharmacotherapy: trofinetide (2023)
Trofinetide is the first FDA-approved therapy for RTT for patients aged ≥2 years, with approval noted as March 2023. (kennedy2024developmentoftrofinetide pages 1-2)

**Direct abstract quote (trofinetide development review, 2024):** “Trofinetide, a synthetic analog of glycine-proline-glutamate, was approved by the US Food and Drug Administration for the treatment of RTT in adult and pediatric patients aged 2 years and older.” (kennedy2024developmentoftrofinetide pages 1-2)

**Phase 3 efficacy and safety (LAVENDER; NCT04181723):**
- RSBQ LSM change: −4.9 vs −1.7 (P=0.0175; d=0.37)
- CGI-I: 3.5 vs 3.8 (P=0.0030; d=0.47)
- Key secondary CSBS-DP-IT Social Composite: −0.1 vs −1.1 (P=0.0064; d=0.43)
- Diarrhea: 80.6% vs 19.1%; vomiting: 26.9% vs 9.6% (neul2023trofinetideforthe pages 1-2, neul2023trofinetideforthe pages 5-6)

**MAXO suggestions:**
- Pharmacotherapy (trofinetide) (MAXO suggestion)
- Symptom management (MAXO suggestion)

### 12.2 Supportive and rehabilitative care (real-world implementation)
In the RNHS cohort, supportive therapy use was high, especially in pediatrics:
- Physical therapy 77.8% overall (87.3% pediatric vs 40.2% adult)
- Speech-language therapy 74.1% overall (86.8% pediatric vs 23.9% adult)
- Occupational therapy 70.5% overall (82.1% pediatric vs 25.0% adult) (may2024characterizingthejourney pages 4-5)

**MAXO suggestions:**
- Physical therapy; occupational therapy; speech therapy (MAXO suggestions)

### 12.3 Advanced therapeutics (gene therapy) — clinical trials
Current ClinicalTrials.gov entries in the retrieved corpus include:
- **NGN-401 (AAV9 MECP2 gene replacement; NCT05898620):** Phase 3 listed; recruiting; single ICV injection; 52-week responder endpoints include CGI-I and blinded video milestone attainment. (NCT05898620 chunk 1)
- **GCB-002 (scAAV9 full-length MECP2; NCT06739434):** enrolling by invitation; open-label dose escalation; intrathecal injection; primary outcome safety through 52 weeks; exploratory CGI-I/PGI-I/RSBQ at 52 weeks. (NCT06739434 chunk 1)
- **AAV-MECP2 (NCT06856759):** recruiting; single intrathecal injection; sequential dose escalation in ages 4–10; primary focus on safety/tolerability with DLT assessment. (NCT06856759 chunk 1)

A structured therapies/trials table is provided:

| Intervention / modality | Mechanism or purpose | Regulatory / phase / status | Population / age | Delivery route | Key efficacy / implementation findings | Key adverse events / safety notes | Trial ID | Publication date | URL | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|
| Trofinetide | Synthetic analog of glycine-proline-glutamate (GPE), an IGF-1–related tripeptide analog developed to improve core RTT symptoms and neuronal function | FDA approved, March 2023; phase 3 LAVENDER completed | Females with RTT; LAVENDER enrolled ages 5–20 years | Oral, twice daily | LAVENDER: RSBQ LSM change -4.9 vs -1.7 (P=0.0175; d=0.37); CGI-I 3.5 vs 3.8 (P=0.0030; d=0.47); CSBS-DP-IT Social Composite -0.1 vs -1.1 (P=0.0064; d=0.43); CGI-I responder rate 37.7% vs 15.2% | Diarrhea 80.6% vs 19.1%; vomiting 26.9% vs 9.6%; TEAEs leading to withdrawal 17.2% vs 2.1%; most GI events mild-moderate | NCT04181723 | 2023-06; 2024-01 | https://doi.org/10.1038/s41591-023-02398-1 ; https://doi.org/10.3389/fphar.2023.1341746 | (neul2023trofinetideforthe pages 2-3, neul2023trofinetideforthe pages 1-2, neul2023trofinetideforthe pages 5-6, kennedy2024developmentoftrofinetide pages 1-2) |
| Supportive therapies (real-world RNHS) | Multidisciplinary rehabilitation and supportive management to preserve mobility, communication, and function | Real-world implementation in RNHS registry cohort | Females with RTT; cohort N=455, pediatric and adult subgroups | Outpatient / community / rehabilitative services | Physical therapy 77.8%, speech-language therapy 74.1%, occupational therapy 70.5% overall; pediatric use exceeded adult use: PT 87.3% vs 40.2%, SLT 86.8% vs 23.9%, OT 82.1% vs 25.0%; nearly half (44.6%) had hospital/ER visit over median 4-year follow-up | Not an interventional treatment study; reflects care burden and utilization rather than treatment-emergent AEs | Not applicable | 2024-07 | https://doi.org/10.1186/s11689-024-09557-6 | (may2024characterizingthejourney pages 1-2, may2024characterizingthejourney pages 2-4, may2024characterizingthejourney pages 4-5) |
| NGN-401 gene therapy | Regulated AAV9 gene replacement carrying full-length human MECP2 with transgene regulation technology to avoid overexpression | Interventional; listed as phase 3 pivotal, open-label, single-arm; RECRUITING | Females with typical RTT caused by MECP2 mutations; pediatric and adolescent/adult cohorts | Single intracerebroventricular (ICV) injection under general anesthesia | Primary efficacy framework includes 52-week responder definition using CGI-I plus attainment of developmental milestones from blinded video assessment; followed for 3 years with planned long-term follow-up | Dose regulation emphasized because MECP2 is dosage-sensitive; one higher-dose pediatric cohort discontinued per registry record | NCT05898620 | 2023 | https://clinicaltrials.gov/study/NCT05898620 | (NCT05898620 chunk 1, NCT05898620 chunk 2) |
| GCB-002 gene therapy | Self-complementary AAV9 carrying full-length human MECP2 transgene product | Interventional; phase NA; ENROLLING_BY_INVITATION | Female children aged 2–10 years with pathogenic MECP2 mutations | Single intrathecal injection; open-label dose-escalation | Primary outcomes focus on drug-related adverse events through 52 weeks; exploratory efficacy includes CGI-I, PGI-I, and RSBQ at 52 weeks | Sentinel dosing, 30-day safety observation, 3+3 escalation/DLT rules; excludes anti-AAV9 neutralizing antibody titer >1:200 | NCT06739434 | 2024 | https://clinicaltrials.gov/study/NCT06739434 | (NCT06739434 chunk 1) |
| AAV-MECP2 gene therapy | AAV-MECP2 gene replacement intended to restore MeCP2 expression | Interventional; early-phase dose exploration; RECRUITING | Children aged 4–10 years; planned n=8 | Single intrathecal injection | Primary outcomes emphasize safety/tolerability with DLT assessment within 30 days; sequential dose escalation across two dose levels | DMC oversight; protocol cites preclinical survival benefit in knockout mice and monkey safety testing; broader field notes need for careful dose control | NCT06856759 | 2025 | https://clinicaltrials.gov/study/NCT06856759 | (NCT06856759 chunk 1) |


*Table: This table summarizes approved treatment, real-world supportive care use, and active gene therapy programs for Rett syndrome. It highlights efficacy, safety, implementation patterns, and current trial designs to support a knowledge-base or therapeutic landscape overview.*

### 12.4 Expert opinions / analysis (authoritative sources)
- The 2024 treatment-strategy review emphasizes that the NIH-funded Natural History Study enabled development of outcome measures, biomarkers/endpoints, and genotype–phenotype correlations, and frames current progress as moving from largely ineffective early trials to a landscape including FDA-approved trofinetide and multiple gene-based approaches (gene replacement, RNA editing, X-chromosome reactivation). (percy2024rettsyndromethe pages 1-2)

---

## 13. Prevention
Primary prevention is not generally feasible because most RTT cases arise from de novo pathogenic variants. Prevention strategies therefore primarily involve **genetic counseling** and reproductive options (not directly retrieved in the current evidence set). Evidence-based counseling details were not extracted from the current corpus.

---

## 14. Other species / natural disease
No naturally occurring RTT-equivalent disease in non-human species was identified in the retrieved evidence set.

---

## 15. Model organisms
### 15.1 Mouse models and single-cell progression studies (recent)
A Mecp2e1 mutant mouse model was used in 2024 to perform longitudinal single-nucleus transcriptomics of disease progression (93,798 nuclei), enabling cell-type specific analysis and investigation of mosaicism/non-cell-autonomous effects. (sharifi2024sexspecificsinglecelllevel pages 1-2)

---

## Key statistics (quick list)
- **Incidence:** ~1 in 10,000–15,000 live female births (neul2023trofinetideforthe pages 1-2)
- **Global prevalence meta-analysis:** 7.1 per 100,000 females (95% CI 4.8–10.5), based on 9.57 million women and 673 cases (petriti2023globalprevalenceof pages 1-2)
- **RNHS real-world cohort (US):** N=455 females; 90.5% classic; 44.6% hospital/ER visit over median 4-year follow-up (may2024characterizingthejourney pages 1-2)
- **Common RNHS phenotype prevalences:** loss of language 95.8%, hand stereotypies 92.3%, respiratory dysfunction 75.8%, constipation 74.5% (may2024characterizingthejourney pages 2-4)
- **Trofinetide LAVENDER trial:** diarrhea 80.6% vs 19.1%; RSBQ and CGI-I statistically significant improvements vs placebo at 12 weeks (neul2023trofinetideforthe pages 1-2, neul2023trofinetideforthe pages 5-6)

---

## Notes on evidence gaps and curation needs
- **PMIDs:** The retrieved texts did not include PubMed IDs in the excerpts available; therefore, PMID-preferred citations could not be supplied without additional PubMed/OMIM/Orphanet lookups.
- **Ontology IDs (MONDO, HPO IDs, GO IDs, UBERON IDs, MAXO IDs):** Suggested terms are provided, but the specific IDs should be confirmed against the respective ontology databases.
- **ICD/MeSH/Orphanet identifiers:** Not available in the current retrieved evidence and should be fetched from those databases directly.


References

1. (gold2024rettsyndrome pages 1-2): Wendy A. Gold, Alan K. Percy, Jeffrey L. Neul, Stuart R. Cobb, Lucas Pozzo-Miller, Jasmeen K. Issar, Bruria Ben-Zeev, Aglaia Vignoli, and Walter E. Kaufmann. Rett syndrome. Nature Reviews Disease Primers, Nov 2024. URL: https://doi.org/10.1038/s41572-024-00568-0, doi:10.1038/s41572-024-00568-0. This article has 60 citations.

2. (neul2023trofinetideforthe pages 1-2): Jeffrey L. Neul, Alan K. Percy, Timothy A. Benke, Elizabeth M. Berry-Kravis, Daniel G. Glaze, Eric D. Marsh, Tim Lin, Serge Stankovic, Kathie M. Bishop, and James M. Youakim. Trofinetide for the treatment of rett syndrome: a randomized phase 3 study. Nature Medicine, 29:1468-1475, Jun 2023. URL: https://doi.org/10.1038/s41591-023-02398-1, doi:10.1038/s41591-023-02398-1. This article has 241 citations and is from a highest quality peer-reviewed journal.

3. (percy2024rettsyndromethe pages 1-2): Alan K. Percy, Amitha Ananth, and Jeffrey L. Neul. Rett syndrome: the emerging landscape of treatment strategies. CNS Drugs, 38:851-867, Sep 2024. URL: https://doi.org/10.1007/s40263-024-01106-y, doi:10.1007/s40263-024-01106-y. This article has 34 citations and is from a peer-reviewed journal.

4. (camillo2024profileoftrofinetide pages 1-2): Laura Camillo, Marco Pozzi, Pia Bernardo, Simone Pisano, and Maria Nobile. Profile of trofinetide in the treatment of rett syndrome: design, development and potential place in therapy. Drug Design, Development and Therapy, 18:5023-5040, Nov 2024. URL: https://doi.org/10.2147/dddt.s383133, doi:10.2147/dddt.s383133. This article has 12 citations.

5. (may2024characterizingthejourney pages 1-2): Damian May, Kalé Kponee-Shovein, Jeffrey L. Neul, Alan K. Percy, Malena Mahendran, Nathaniel Downes, Grace Chen, Talissa Watson, Dominique C. Pichard, Melissa Kennedy, and Patrick Lefebvre. Characterizing the journey of rett syndrome among females in the united states: a real-world evidence study using the rett syndrome natural history study database. Journal of Neurodevelopmental Disorders, Jul 2024. URL: https://doi.org/10.1186/s11689-024-09557-6, doi:10.1186/s11689-024-09557-6. This article has 8 citations and is from a peer-reviewed journal.

6. (may2024characterizingthejourney pages 2-4): Damian May, Kalé Kponee-Shovein, Jeffrey L. Neul, Alan K. Percy, Malena Mahendran, Nathaniel Downes, Grace Chen, Talissa Watson, Dominique C. Pichard, Melissa Kennedy, and Patrick Lefebvre. Characterizing the journey of rett syndrome among females in the united states: a real-world evidence study using the rett syndrome natural history study database. Journal of Neurodevelopmental Disorders, Jul 2024. URL: https://doi.org/10.1186/s11689-024-09557-6, doi:10.1186/s11689-024-09557-6. This article has 8 citations and is from a peer-reviewed journal.

7. (neul2023trofinetideforthe pages 2-3): Jeffrey L. Neul, Alan K. Percy, Timothy A. Benke, Elizabeth M. Berry-Kravis, Daniel G. Glaze, Eric D. Marsh, Tim Lin, Serge Stankovic, Kathie M. Bishop, and James M. Youakim. Trofinetide for the treatment of rett syndrome: a randomized phase 3 study. Nature Medicine, 29:1468-1475, Jun 2023. URL: https://doi.org/10.1038/s41591-023-02398-1, doi:10.1038/s41591-023-02398-1. This article has 241 citations and is from a highest quality peer-reviewed journal.

8. (petriti2023globalprevalenceof pages 1-2): Uarda Petriti, Daniel C. Dudman, Emil Scosyrev, and Sandra Lopez-Leon. Global prevalence of rett syndrome: systematic review and meta-analysis. Systematic Reviews, Jan 2023. URL: https://doi.org/10.1186/s13643-023-02169-6, doi:10.1186/s13643-023-02169-6. This article has 120 citations and is from a peer-reviewed journal.

9. (kennedy2024developmentoftrofinetide pages 1-2): Melissa Kennedy, Larry Glass, Daniel G. Glaze, Steve Kaminsky, Alan K. Percy, Jeffrey L. Neul, Nancy E. Jones, Daniela Tropea, Joseph P. Horrigan, Paige Nues, Kathie M. Bishop, and James M. Youakim. Development of trofinetide for the treatment of rett syndrome: from bench to bedside. Frontiers in Pharmacology, Jan 2024. URL: https://doi.org/10.3389/fphar.2023.1341746, doi:10.3389/fphar.2023.1341746. This article has 16 citations.

10. (may2024characterizingthejourney pages 9-10): Damian May, Kalé Kponee-Shovein, Jeffrey L. Neul, Alan K. Percy, Malena Mahendran, Nathaniel Downes, Grace Chen, Talissa Watson, Dominique C. Pichard, Melissa Kennedy, and Patrick Lefebvre. Characterizing the journey of rett syndrome among females in the united states: a real-world evidence study using the rett syndrome natural history study database. Journal of Neurodevelopmental Disorders, Jul 2024. URL: https://doi.org/10.1186/s11689-024-09557-6, doi:10.1186/s11689-024-09557-6. This article has 8 citations and is from a peer-reviewed journal.

11. (sharifi2024sexspecificsinglecelllevel pages 1-2): Osman Sharifi, Viktoria Haghani, Kari E. Neier, Keith J. Fraga, Ian Korf, Sophia M. Hakam, Gerald Quon, Nelson Johansen, Dag H. Yasui, and Janine M. LaSalle. Sex-specific single cell-level transcriptomic signatures of rett syndrome disease progression. Communications Biology, Oct 2024. URL: https://doi.org/10.1038/s42003-024-06990-0, doi:10.1038/s42003-024-06990-0. This article has 15 citations and is from a peer-reviewed journal.

12. (sharifi2024sexspecificsinglecelllevel pages 3-4): Osman Sharifi, Viktoria Haghani, Kari E. Neier, Keith J. Fraga, Ian Korf, Sophia M. Hakam, Gerald Quon, Nelson Johansen, Dag H. Yasui, and Janine M. LaSalle. Sex-specific single cell-level transcriptomic signatures of rett syndrome disease progression. Communications Biology, Oct 2024. URL: https://doi.org/10.1038/s42003-024-06990-0, doi:10.1038/s42003-024-06990-0. This article has 15 citations and is from a peer-reviewed journal.

13. (sharifi2024sexspecificsinglecelllevel pages 5-6): Osman Sharifi, Viktoria Haghani, Kari E. Neier, Keith J. Fraga, Ian Korf, Sophia M. Hakam, Gerald Quon, Nelson Johansen, Dag H. Yasui, and Janine M. LaSalle. Sex-specific single cell-level transcriptomic signatures of rett syndrome disease progression. Communications Biology, Oct 2024. URL: https://doi.org/10.1038/s42003-024-06990-0, doi:10.1038/s42003-024-06990-0. This article has 15 citations and is from a peer-reviewed journal.

14. (neul2023trofinetideforthe pages 5-6): Jeffrey L. Neul, Alan K. Percy, Timothy A. Benke, Elizabeth M. Berry-Kravis, Daniel G. Glaze, Eric D. Marsh, Tim Lin, Serge Stankovic, Kathie M. Bishop, and James M. Youakim. Trofinetide for the treatment of rett syndrome: a randomized phase 3 study. Nature Medicine, 29:1468-1475, Jun 2023. URL: https://doi.org/10.1038/s41591-023-02398-1, doi:10.1038/s41591-023-02398-1. This article has 241 citations and is from a highest quality peer-reviewed journal.

15. (may2024characterizingthejourney pages 4-5): Damian May, Kalé Kponee-Shovein, Jeffrey L. Neul, Alan K. Percy, Malena Mahendran, Nathaniel Downes, Grace Chen, Talissa Watson, Dominique C. Pichard, Melissa Kennedy, and Patrick Lefebvre. Characterizing the journey of rett syndrome among females in the united states: a real-world evidence study using the rett syndrome natural history study database. Journal of Neurodevelopmental Disorders, Jul 2024. URL: https://doi.org/10.1186/s11689-024-09557-6, doi:10.1186/s11689-024-09557-6. This article has 8 citations and is from a peer-reviewed journal.

16. (NCT05898620 chunk 1):  A Novel, Regulated Gene Therapy (NGN-401) Study for Females With Rett Syndrome. Neurogene Inc.. 2023. ClinicalTrials.gov Identifier: NCT05898620

17. (NCT06739434 chunk 1):  GCB-002 in Treatment of Patients With Rett Syndrome. Genecombio Ltd.. 2024. ClinicalTrials.gov Identifier: NCT06739434

18. (NCT06856759 chunk 1):  Single-Dose AAV-MECP2 Safety/Tolerability and Efficacy in Rett Syndrome. Guangzhou Women and Children's Medical Center. 2025. ClinicalTrials.gov Identifier: NCT06856759

19. (NCT05898620 chunk 2):  A Novel, Regulated Gene Therapy (NGN-401) Study for Females With Rett Syndrome. Neurogene Inc.. 2023. ClinicalTrials.gov Identifier: NCT05898620
