---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-05T22:16:24.168452'
end_time: '2026-04-05T22:33:16.853494'
duration_seconds: 1012.69
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: RET-Rearranged Non-Small Cell Lung Cancer
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 55
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** RET-Rearranged Non-Small Cell Lung Cancer
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **RET-Rearranged Non-Small Cell Lung Cancer** covering all of the
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
- **Disease Name:** RET-Rearranged Non-Small Cell Lung Cancer
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **RET-Rearranged Non-Small Cell Lung Cancer** covering all of the
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


# Disease Characteristics Research Report: RET‑Rearranged Non‑Small Cell Lung Cancer (RET fusion‑positive NSCLC)

**Target disease:** RET‑Rearranged Non‑Small Cell Lung Cancer  
**Category:** Molecularly defined subtype of NSCLC (oncogene‑addicted lung cancer) (novello2023retfusionpositivenonsmall pages 1-2, chen2024retinhibitorsin pages 3-5)  
**MONDO ID:** A specific MONDO term for “RET fusion‑positive NSCLC” was **not** identified in the retrieved evidence; broader parent terms are provided below (novello2023retfusionpositivenonsmall pages 1-2).

---

## 1. Disease Information

### 1.1 Concise overview
RET‑rearranged NSCLC is a subset of non‑small cell lung cancers driven by oncogenic **RET gene fusions** (chromosomal rearrangements) that create constitutively active RET kinase signaling and act as a targetable driver alteration (novello2023retfusionpositivenonsmall pages 1-2, chen2024retinhibitorsin pages 3-5). RET fusions are uncommon in unselected NSCLC but clinically important due to high response rates to selective RET tyrosine kinase inhibitors (TKIs) (rocco2023treatmentofadvanced pages 5-6, zhou2023firstlineselpercatinibor pages 1-3).

### 1.2 Key identifiers and ontology mapping
A structured mapping of the disease concept, synonyms, and parent ontology terms captured in the retrieved evidence is provided here:

| Preferred name | Synonyms / alternative names | Specific disease identifier | Parent disease / broader ontology term | Parent identifier | Note | Data source |
|---|---|---|---|---|---|---|
| RET-rearranged non-small cell lung cancer | RET+ NSCLC; RET fusion-positive NSCLC; RET-rearranged NSCLC; NSCLC harboring RET gene fusion | Not identified in gathered evidence | non-small cell lung carcinoma | EFO_0003060 | RET is an associated target for non-small cell lung carcinoma in Open Targets; disease-specific RET-fusion child term not retrieved | (novello2023retfusionpositivenonsmall pages 1-2) |
| RET-rearranged non-small cell lung cancer | RET+ NSCLC; RET fusion-positive NSCLC; RET-rearranged NSCLC; NSCLC harboring RET gene fusion | Not identified in gathered evidence | lung cancer | MONDO_0008903 | Open Targets returned lung cancer as a broader parent disease associated with RET | (novello2023retfusionpositivenonsmall pages 1-2) |
| RET-rearranged non-small cell lung cancer | RET+ NSCLC; RET fusion-positive NSCLC; RET-rearranged NSCLC; NSCLC harboring RET gene fusion | Not identified in gathered evidence | non-small cell squamous lung carcinoma | MONDO_0056806 | Returned in Open Targets results, but RET fusion-positive disease is typically discussed within NSCLC overall and especially adenocarcinoma-focused literature | (novello2023retfusionpositivenonsmall pages 1-2, chen2024retinhibitorsin pages 3-5) |
| RET-rearranged non-small cell lung cancer | RET+ NSCLC; RET fusion-positive NSCLC; RET-rearranged NSCLC; NSCLC harboring RET gene fusion | Specific MONDO term not found in gathered evidence | Disease concept used in recent reviews and trials | N/A | Gathered evidence supports this as a molecularly defined NSCLC subtype, but a specific MONDO term for RET fusion-positive NSCLC was not found in the retrieved context | (novello2023retfusionpositivenonsmall pages 1-2, chen2024retinhibitorsin pages 3-5) |


*Table: This table summarizes the naming conventions and ontology context for RET-rearranged NSCLC using the gathered evidence. It is useful for mapping the disease concept to broader ontology terms when a specific MONDO entry was not identified in the retrieved sources.*

**Notes:** The retrieved Open Targets output associates **RET** with non‑small cell lung carcinoma (EFO_0003060) and broader lung cancer MONDO terms, but did not surface a dedicated “RET fusion‑positive NSCLC” MONDO child term in the available context (novello2023retfusionpositivenonsmall pages 1-2).

### 1.3 Synonyms / alternative names
Common names used in recent reviews and trials include **RET fusion‑positive NSCLC**, **RET‑rearranged NSCLC**, and **NSCLC harboring RET gene fusion** (novello2023retfusionpositivenonsmall pages 1-2, chen2024retinhibitorsin pages 3-5, spitaleri2024nonsmallcelllungcancers pages 1-2).

### 1.4 Evidence provenance
Most information below is derived from **aggregated disease‑level resources** (peer‑reviewed reviews, prospective clinical trials, retrospective real‑world cohorts), rather than single‑patient EHRs. The report includes both trial datasets (e.g., LIBRETTO‑431) and real‑world retrospective chart reviews (lei2024efficacyandsafety pages 1-2, zhou2023firstlineselpercatinibor pages 1-3).

---

## 2. Etiology

### 2.1 Disease causal factors
**Primary causal factor:** somatic **RET gene fusion/rearrangement** in lung tumor tissue, producing a chimeric oncoprotein with ligand‑independent kinase activity and downstream proliferative signaling (novello2023retfusionpositivenonsmall pages 1-2, chen2024retinhibitorsin pages 3-5).

RET activation pathways include **in‑frame gene fusions**, point mutations, and overexpression; in RET‑rearranged NSCLC the dominant mechanism is gene fusion (shen2024recentprogressof pages 1-3, chen2024retinhibitorsin pages 1-3).

### 2.2 Risk factors
RET fusion‑positive NSCLC is enriched among patients with:
- **Adenocarcinoma histology**, **younger age**, and **never/light smoking** history (novello2023retfusionpositivenonsmall pages 1-2, chen2024retinhibitorsin pages 3-5).
- A high propensity for **CNS metastases** (see Phenotypes) (novello2023retfusionpositivenonsmall pages 1-2, clark2023selectiveretinhibitors pages 1-2).

These are best considered **clinical correlates/enriching features**, not established causal environmental risk factors for acquiring a RET fusion.

### 2.3 Protective factors
No specific protective genetic variants or environmental protective factors were identified in the retrieved evidence.

### 2.4 Gene–environment interactions
No explicit RET‑fusion gene–environment interaction findings were retrieved.

---

## 3. Phenotypes

### 3.1 Core clinical phenotype and frequencies
RET fusion‑positive NSCLC shares “fusion‑driven NSCLC” clinical features: younger age, adenocarcinoma histology, low tobacco exposure, and elevated risk of brain metastases (spitaleri2024nonsmallcelllungcancers pages 1-2, spitaleri2024nonsmallcelllungcancers pages 2-4).

Reported CNS metastasis burden:
- Brain metastasis present in ~**25%** at stage IV diagnosis and **46%** lifetime prevalence in some summaries (gouda2023precisiononcologywith pages 2-4, clark2023selectiveretinhibitors pages 1-2).

Common metastatic sites in one cohort summary included lung (~50%), bone (~43%), pleura (~40%) (clark2023selectiveretinhibitors pages 1-2).

### 3.2 Suggested HPO term mapping
A phenotype-to-HPO structured mapping is provided here:

| Feature | Frequency/notes | Suggested HPO term(s) | Evidence citation |
|---|---|---|---|
| Adenocarcinoma histology | RET fusions occur most commonly in lung adenocarcinoma; molecular subtype is predominantly adenocarcinoma in multiple reviews and cohorts | HP:0034347 Lung adenocarcinoma | (novello2023retfusionpositivenonsmall pages 1-2, chen2024retinhibitorsin pages 3-5) |
| Younger age at presentation | Patients are generally younger than unselected NSCLC cohorts; reviews describe age \<=60 years, and one cohort summary reported median age 63 years | HP:0003596 Middle age onset; HP:0011462 Young adult onset | (clark2023selectiveretinhibitors pages 1-2, novello2023retfusionpositivenonsmall pages 1-2, chen2024retinhibitorsin pages 3-5) |
| Never/light smoking history | Enriched in never-smokers or patients with minimal tobacco exposure; one review notes ~40% smokers, implying majority never/light smokers | HP:0034433 History of tobacco smoking (annotate as often absent/minimal exposure in this subtype) | (clark2023selectiveretinhibitors pages 1-2, novello2023retfusionpositivenonsmall pages 1-2, chen2024retinhibitorsin pages 3-5) |
| Female predominance | Female predominance reported; one untreated cohort summary noted 56% female | HP:0000132 Female sex (phenotypic descriptor often used in cohort annotation rather than disease phenotype) | (clark2023selectiveretinhibitors pages 1-2, rocha2023importanceofthe pages 16-19) |
| Brain metastases at diagnosis | About 25% of patients with stage IV RET fusion-positive NSCLC have brain metastases at diagnosis | HP:0002518 Brain neoplasm; HP:0012735 Metastasis to brain | (gouda2023precisiononcologywith pages 2-4, clark2023selectiveretinhibitors pages 1-2, chen2024retinhibitorsin pages 3-5) |
| Brain metastases over lifetime | Lifetime prevalence of brain metastases reported as 46% | HP:0012735 Metastasis to brain | (novello2023retfusionpositivenonsmall pages 1-2) |
| Pulmonary metastatic involvement | In advanced disease, lung was a common metastatic site in ~50% | HP:0032264 Pulmonary metastases | (clark2023selectiveretinhibitors pages 1-2) |
| Bone metastases | Bone metastases reported in ~43% | HP:0002664 Neoplasm of bone; HP:0012762 Bone metastases | (clark2023selectiveretinhibitors pages 1-2) |
| Pleural metastases / pleural involvement | Pleural metastatic involvement reported in ~40% | HP:0032252 Pleural neoplasm; HP:0032263 Pleural metastases | (clark2023selectiveretinhibitors pages 1-2) |
| Low PD-L1 expression | Cohort summaries describe generally low PD-L1 expression, consistent with limited benefit from immunotherapy in many RET-driven tumors | HP term not well matched; consider non-HPO biomarker annotation: low PD-L1 expression | (clark2023selectiveretinhibitors pages 1-2) |
| Low tumor mutational burden | Cohort summaries describe generally low TMB | HP term not well matched; consider non-HPO biomarker annotation: low tumor mutational burden | (clark2023selectiveretinhibitors pages 1-2) |


*Table: This table maps common clinical and demographic features of RET fusion-positive NSCLC to suggested HPO terms where possible. It is useful for structuring phenotype annotations while distinguishing features better captured as cohort descriptors or biomarkers rather than classic HPO disease phenotypes.*

**Quality‑of‑life impact:** Quality‑of‑life (QoL) outcomes are increasingly reported in first‑line trials; LIBRETTO‑431 commentary notes fewer patients reported worsening with selpercatinib compared with chemotherapy (lee2024libretto431confirmingthe pages 2-4).

---

## 4. Genetic / Molecular Information

### 4.1 Causal gene(s)
- **RET** (ret proto‑oncogene) is the causal driver gene in this molecular subtype (chen2024retinhibitorsin pages 3-5).

### 4.2 Pathogenic alteration class
- **Somatic structural variants (gene fusions/rearrangements)** involving the 3′ RET kinase domain fused to a 5′ partner that can provide a dimerization domain and transcriptional activity (chen2024retinhibitorsin pages 1-3, chen2024retinhibitorsin pages 3-5).

### 4.3 Common fusion partners
Frequent partners reported in recent reviews/cohorts:
- **KIF5B‑RET** (often dominant; e.g., 40–70% in one review; 70–90% in another; 59.4% in a China real‑world cohort) (novello2023retfusionpositivenonsmall pages 1-2, chen2024retinhibitorsin pages 3-5, wang2024evolutionoftreatment pages 1-2).
- **CCDC6‑RET** (often ~15–30% or lower depending on cohort) and **NCOA4‑RET** (less frequent) (novello2023retfusionpositivenonsmall pages 1-2, chen2024retinhibitorsin pages 3-5, lei2024efficacyandsafety pages 1-2).

### 4.4 Functional consequences and pathways
RET fusion signaling activates multiple downstream pathways (examples from recent mechanistic reviews):
- **RAS/MAPK**, **PI3K/AKT**, and **JAK/STAT** (shen2024recentprogressof pages 1-3, chen2024retinhibitorsin pages 1-3, spitaleri2024nonsmallcelllungcancers pages 1-2).

Spitaleri et al. detail RET phosphotyrosine sites linked to specific pathways (e.g., Y1062 to Ras/MAPK and PI3K/AKT; Y752/Y928 to STAT3) (spitaleri2024nonsmallcelllungcancers pages 1-2).

### 4.5 Resistance mechanisms (current understanding)
Acquired resistance to first‑generation selective RET inhibitors includes:
- **On‑target kinase mutations**, notably **solvent‑front mutations at RET G810 (G810C/S/R)** (shen2024recentprogressof pages 1-3, novello2023retfusionpositivenonsmall pages 8-9).
- **Gatekeeper mutation V804M** and other resistance‑associated positions (chen2024retinhibitorsin pages 1-3, novello2023retfusionpositivenonsmall pages 8-9).
- **Off‑target/bypass mechanisms** such as **MET amplification**, EGFR/AXL activation, and FGFR‑driven signaling with JAK/STAT activation described in model systems (rocco2023treatmentofadvanced pages 8-10, novello2023retfusionpositivenonsmall pages 8-9).

### 4.6 Model systems (mechanistic and resistance research)
- **Cell lines / patient-derived models** used to study adaptive resistance include LC‑2/ad (CCDC6‑RET), ponatinib‑resistant derivatives, and patient‑derived RET‑fusion NSCLC lines (e.g., CUTO series) (rocco2023treatmentofadvanced pages 8-10).
- **Mouse model:** a lung‑specific **KIF5B‑RET transgenic mouse** (SPC promoter) develops multifocal lung lesions and tumors; vandetanib reduced tumor burden in this model (saito2014amousemodel pages 1-2).

---

## 5. Environmental Information

RET fusion‑positive NSCLC is enriched in never/light smokers, suggesting it is not primarily tobacco‑driven; however, no specific environmental toxin, infectious, or lifestyle exposure was identified as causal for RET rearrangement in the retrieved evidence (novello2023retfusionpositivenonsmall pages 1-2, chen2024retinhibitorsin pages 3-5).

---

## 6. Mechanism / Pathophysiology

### 6.1 Causal chain (high-level)
1. Chromosomal rearrangement creates an expressed **RET fusion** retaining the RET kinase domain (chen2024retinhibitorsin pages 3-5, chen2024retinhibitorsin pages 1-3).  
2. Fusion partner contributes dimerization/transcriptional activation → **ligand‑independent RET activation** (chen2024retinhibitorsin pages 1-3, chen2024retinhibitorsin pages 3-5).  
3. Activated RET drives MAPK/PI3K/JAK‑STAT signaling → proliferation, survival, metastatic behavior (shen2024recentprogressof pages 1-3, spitaleri2024nonsmallcelllungcancers pages 1-2).  
4. Selective RET inhibition induces tumor regression; resistance emerges via on‑target mutation or bypass signaling (rocco2023treatmentofadvanced pages 8-10, novello2023retfusionpositivenonsmall pages 8-9).

### 6.2 Suggested GO biological process terms (examples)
- GO:0008283 cell population proliferation  
- GO:0007165 signal transduction  
- GO:0070371 ERK1 and ERK2 cascade  
- GO:0014065 phosphatidylinositol 3‑kinase signaling  
- GO:0097696 STAT cascade  
(Mechanistic basis: activation of MAPK/PI3K/JAK‑STAT in RET fusion signaling) (shen2024recentprogressof pages 1-3, spitaleri2024nonsmallcelllungcancers pages 1-2).

### 6.3 Suggested Cell Ontology (CL) terms (examples)
- CL:0000084 T cell (for immunotherapy context, tumor microenvironment studies)  
- CL:0002062 lung epithelial cell / alveolar type II cell context (SPC promoter lung model suggests alveolar epithelial targeting) (saito2014amousemodel pages 1-2).

---

## 7. Anatomical Structures Affected

### 7.1 Primary organ/system
- **Lung** (respiratory system), most commonly non‑small cell lung adenocarcinoma (novello2023retfusionpositivenonsmall pages 1-2, chen2024retinhibitorsin pages 3-5).

**Suggested UBERON:** UBERON:0002048 lung.

### 7.2 Secondary organ involvement
- **Brain/CNS metastases** are frequent (25% at diagnosis in advanced disease; ~46% lifetime in some reports) (novello2023retfusionpositivenonsmall pages 1-2, clark2023selectiveretinhibitors pages 1-2).

**Suggested UBERON:** UBERON:0000955 brain.

### 7.3 Common metastatic sites
- Bone and pleura are commonly involved in advanced disease summaries (clark2023selectiveretinhibitors pages 1-2).

---

## 8. Temporal Development

### 8.1 Onset
Typically **adult‑onset** lung cancer, enriched in younger adults compared with unselected NSCLC cohorts (novello2023retfusionpositivenonsmall pages 1-2, chen2024retinhibitorsin pages 3-5).

### 8.2 Progression
Often diagnosed at **advanced stage**; CNS metastases may be present at diagnosis and frequently develop during the disease course (clark2023selectiveretinhibitors pages 1-2, spitaleri2024nonsmallcelllungcancers pages 2-4).

---

## 9. Inheritance and Population

### 9.1 Epidemiology (RET fusion prevalence)
- RET fusions occur in approximately **1–2%** of NSCLC (novello2023retfusionpositivenonsmall pages 1-2, chen2024retinhibitorsin pages 3-5).
- In Chinese NSCLC series, prevalence reported as **1.4% (84/6125)** and **1.77% (167/9431)** (wang2024evolutionoftreatment pages 1-2).

### 9.2 Inheritance
This is not a Mendelian inherited disorder; RET fusions in NSCLC are **somatic** cancer alterations.

### 9.3 Demographic patterns
RET fusion‑positive NSCLC is associated with adenocarcinoma histology, never/light smoking status, and female predominance in several cohorts/reviews (clark2023selectiveretinhibitors pages 1-2, wang2024evolutionoftreatment pages 1-2, novello2023retfusionpositivenonsmall pages 1-2).

---

## 10. Diagnostics

### 10.1 Recommended approach (current understanding)
Broad **multiplex molecular profiling** is emphasized in guidelines/reviews, with **RNA‑based NGS** commonly positioned as the preferred method for RET fusion detection because it detects expressed fusions and identifies fusion partners (novello2023retfusionpositivenonsmall pages 1-2, chen2024retinhibitorsin pages 3-5).

A structured comparison of modalities:

| Modality | What it detects | Strengths | Key limitations/pitfalls | Guideline/recommendation notes | Evidence citations |
|---|---|---|---|---|---|
| RNA-based NGS | Expressed RET fusion transcripts, fusion partners, and transcript structure | Preferred assay for RET fusions because of high sensitivity/specificity for expressed fusions; identifies known and novel partners; multiplexes with other actionable drivers; can clarify cases missed by DNA testing | Requires high-quality RNA; FFPE degradation and low RNA yield can reduce assay success | ESMO-cited guidance in reviews identifies RNA-NGS as the first-choice assay for RET fusion detection in NSCLC; broad multiplex testing is recommended in advanced NSCLC (novello2023retfusionpositivenonsmall pages 1-2, chen2024retinhibitorsin pages 3-5) | (novello2023retfusionpositivenonsmall pages 1-2, chen2024retinhibitorsin pages 3-5) |
| DNA-based NGS | Genomic rearrangements involving RET breakpoints and other co-alterations | Broad genomic profiling in one test; useful when RNA is unavailable; concurrently detects mutations, copy-number changes, and co-mutations | Lower sensitivity for fusion detection than RNA-based methods; intronic breakpoint complexity can cause false negatives; may not confirm transcriptionally active fusion | Acceptable when RNA testing is unavailable, but reviews emphasize RNA-based NGS as preferable for RET fusions (novello2023retfusionpositivenonsmall pages 1-2, chen2024retinhibitorsin pages 3-5) | (novello2023retfusionpositivenonsmall pages 1-2, chen2024retinhibitorsin pages 3-5) |
| RT-PCR | Known RET fusion transcripts targeted by specific primers | Rapid, relatively accessible, and can be highly sensitive for predefined fusion events; used in practice and in studies alongside NGS | Detects only known/targeted fusions; misses novel partners; imbalance assays are less reliable; does not provide broad profiling | Can be used where NGS is unavailable; in LIBRETTO-431 RET testing was done locally by NGS (58%) or RT-PCR (42%), showing real-world use in trial enrollment (spitaleri2024nonsmallcelllungcancers pages 9-11, chen2024retinhibitorsin pages 3-5) | (spitaleri2024nonsmallcelllungcancers pages 9-11, lei2024efficacyandsafety pages 1-2, chen2024retinhibitorsin pages 3-5) |
| FISH | RET rearrangement at the DNA level via break-apart probes | Historically used; can detect rearrangement without prior knowledge of partner; available in many pathology labs | Cannot identify fusion partner, exact breakpoint, or transcriptional activity; sensitivity varies by fusion partner; lower performance for some partners such as NCOA4; interpretation thresholds matter | Considered an alternative where NGS is unavailable, but not preferred over multiplex NGS for contemporary practice (rocha2023importanceofthe pages 16-19, chen2024retinhibitorsin pages 3-5) | (rocha2023importanceofthe pages 16-19, chen2024retinhibitorsin pages 3-5) |
| IHC | RET protein expression | Tissue-based, fast, and widely available as a pathology platform | Poor standardization; false positives and false negatives reported; protein expression does not reliably indicate oncogenic RET fusion | Reviews state IHC is not recommended as a screening tool for RET fusion-positive NSCLC (rocha2023importanceofthe pages 16-19, chen2024retinhibitorsin pages 3-5) | (rocha2023importanceofthe pages 16-19, chen2024retinhibitorsin pages 3-5) |
| Liquid biopsy (cfDNA/cfRNA) | Circulating RET alterations/fusions in plasma | Minimally invasive; useful when tissue is limited or repeat biopsy is difficult; can support real-time monitoring and resistance assessment | Negative plasma result does not exclude RET fusion because shedding/yield may be low; cfDNA may underperform for some fusions; cfRNA assays are less widely implemented | Reviews note NGS can be applied to liquid samples, but tissue testing remains important if plasma is negative and suspicion remains high (gouda2023precisiononcologywith pages 2-4, rocha2023importanceofthe pages 16-19, novello2023retfusionpositivenonsmall pages 1-2) | (gouda2023precisiononcologywith pages 2-4, rocha2023importanceofthe pages 16-19, novello2023retfusionpositivenonsmall pages 1-2) |


*Table: This table compares the main methods used to detect RET fusions in NSCLC, highlighting what each test measures, practical strengths, major pitfalls, and how recent reviews frame their clinical use. It is useful for understanding why RNA-based NGS is generally preferred while showing where RT-PCR, FISH, IHC, and liquid biopsy still fit in practice.*

### 10.2 Recent development: rapid automated fusion testing (2024)
A 12‑center European evaluation of the automated RNA‑based **Idylla™ GeneFusion Assay** (RT‑PCR) in 326 FFPE advanced NSCLC samples reported RET fusion **sensitivity 100%** and **specificity 99.3%**, with ~3‑hour turnaround and low failure rate (0.9%) (melchior2024multicenterevaluationof pages 1-2).

### 10.3 Liquid biopsy
Liquid biopsy can detect RET alterations, but negative plasma testing does not exclude RET fusion due to variable ctDNA/cfRNA shedding; tissue testing remains important when feasible (gouda2023precisiononcologywith pages 2-4, rocha2023importanceofthe pages 16-19).

### 10.4 Differential diagnosis
Differential diagnosis is primarily at the molecular subtype level (other oncogene‑addicted NSCLCs such as EGFR/ALK/ROS1). RET fusions are often mutually exclusive with major other drivers, supporting their role as primary oncogenic drivers when present (chen2024retinhibitorsin pages 3-5).

---

## 11. Outcome / Prognosis

### 11.1 Outcomes with non‑RET inhibitor standards of care (historical / natural history)
- In a registry described in Novello et al., chemotherapy outcomes included **ORR 52%**, **PFS 6.6 months**, and **OS 23.6 months** (novello2023retfusionpositivenonsmall pages 4-5).
- Immunotherapy outcomes are often poor in RET‑driven tumors; a review summarizes real‑world/retrospective ICI activity of **0–23%**, and reports IMMUNOTARGET ORR 6% and median PFS 2.1 months (chen2024retinhibitorsin pages 5-6).

### 11.2 Outcomes with selective RET inhibitors
Key recent efficacy/safety outcomes (2023–2024 and real‑world) are summarized here:

| Study/type | Setting/line | Drug | N (if available) | ORR | mPFS | OS metrics | CNS/intracranial outcomes | Notable grade >=3 AEs | Publication (year, journal) and URL | Citation |
|---|---|---|---:|---|---|---|---|---|---|---|
| LIBRETTO-431, randomized phase III trial | 1L advanced/metastatic RET fusion+ NSCLC; selpercatinib vs platinum/pemetrexed +/- pembrolizumab | Selpercatinib vs chemo +/- pembro | ITT ~261; 158 vs 98; ITT-pembrolizumab ~212; 129 vs 83 | 84% vs 65% | 24.8 vs 11.2 months; HR ~0.46-0.48 | OS not mature/not reported in retrieved evidence | Without baseline CNS metastases: 12-mo cumulative CNS progression 1.1% vs 14.7% (HR 0.17); with baseline CNS metastases: intracranial ORR 81% vs 57%; reported CNS-protective effect | Grade >=3 AEs 70% with selpercatinib; common lab abnormalities AST/ALT ~60%; hypertension 48%; dose reductions 51%, discontinuation 10% | Pérol et al. 2024, J Clin Oncol; Spitaleri et al. 2024, Cancers. https://doi.org/10.1200/jco.24.00724 ; https://doi.org/10.3390/cancers16162877 | (spitaleri2024nonsmallcelllungcancers pages 9-11) |
| ARROW, phase I/II trial (high-level) | Advanced RET fusion+ NSCLC; treatment-naive and previously platinum-treated cohorts | Pralsetinib | Trial enrollment overall 590 on ClinicalTrials.gov; NSCLC cohort N not consistently extractable from retrieved context | 72% treatment-naive; 59% prior platinum | 13.0 months treatment-naive; 16.5 months prior chemo | Not reported in retrieved evidence | Intracranial ORR 70%; median intracranial PFS 10.5 months | Grade >=3 TRAEs included neutropenia, hypertension, anemia | ARROW/NCT03037385; Chen et al. 2024, Drugs. https://clinicaltrials.gov/study/NCT03037385 ; https://doi.org/10.1007/s40265-024-02040-5 | (chen2024retinhibitorsin pages 8-10, NCT03037385 chunk 1) |
| LIBRETTO-001, phase I/II trial (high-level) | Advanced RET fusion+ NSCLC; untreated and previously treated cohorts | Selpercatinib | ~316 total in one review summary; previously treated cohort 247 in one table excerpt | Untreated 84%; previously treated ~61-61.5% | Previously treated ~26.2 months in one review summary | Not reported in retrieved evidence | Intracranial ORR 85%; median intracranial PFS 19.4 months | Common adverse reactions >=25% included edema, diarrhea, fatigue, dry mouth, hypertension | Clark et al. 2023, Cancers; Chen et al. 2024, Drugs. https://doi.org/10.3390/cancers16010031 ; https://doi.org/10.1007/s40265-024-02040-5 | (clark2023selectiveretinhibitors pages 4-5, chen2024retinhibitorsin pages 8-10, spitaleri2024nonsmallcelllungcancers pages 9-11) |
| Real-world retrospective chart review, China | 1L advanced RET-rearranged NSCLC | RET-TKI (study abstract indicates RET-TKI; retrieved context does not cleanly separate agent-specific outcomes) | 51 | 73.1% | 22.7 months (95% CI 11.7-33.7) | Not reported | Baseline brain metastasis subgroup: intracranial ORR 50%, DCR 100%; brain metastasis was a common treatment-failure pattern | Grade >=3 decreased neutrophil count 11.4%; anemia 11.4% | Lei et al. 2024, BMC Cancer. https://doi.org/10.1186/s12885-024-13155-z | (lei2024efficacyandsafety pages 1-2) |
| Real-world retrospective chart review, China | 2L advanced RET-rearranged NSCLC | RET-TKI | 51 total cohort | 58.3% | 17.7 months (95% CI 9.1-26.2) | Not reported | Brain metastasis common at progression; baseline brain metastasis subgroup intracranial ORR 50% | Grade >=3 decreased neutrophil count 11.4%; anemia 11.4% | Lei et al. 2024, BMC Cancer. https://doi.org/10.1186/s12885-024-13155-z | (lei2024efficacyandsafety pages 1-2) |
| Real-world retrospective chart review, China | Later-line advanced RET-rearranged NSCLC | RET-TKI | 51 total cohort | 55.6% | 14.7 months (95% CI 12.6-16.8) | Not reported | Brain metastasis common at progression | Grade >=3 decreased neutrophil count 11.4%; anemia 11.4% | Lei et al. 2024, BMC Cancer. https://doi.org/10.1186/s12885-024-13155-z | (lei2024efficacyandsafety pages 1-2) |
| Real-world multicenter analysis, China | Advanced RET-rearranged NSCLC, mixed lines | Pralsetinib monotherapy | 64 total RET-rearranged NSCLC patients; pralsetinib used in 48.4% | Not reported in retrieved excerpt | 16.03 months; vs chemotherapy 2.87 months, chemo+anti-angiogenic 6.90 months, multikinase inhibitors 2.50 months | 1-year OS 64.3%; 2-year OS 46.4% | Not reported in retrieved excerpt | Any AE 71.0%; grade 3-4 AEs 45.2%; common AEs hemoglobin reduction 35.5%, neutropenia 32.3%; no AE-related deaths | Wang et al. 2024, BMC Pulm Med. https://doi.org/10.1186/s12890-024-03371-5 | (wang2024evolutionoftreatment pages 1-2) |
| Meta-analysis | RET fusion+ NSCLC, pooled selective RET inhibitors | Selpercatinib + pralsetinib (pooled) | 8 studies pooled | 67% pooled ORR | 16.09 months pooled mPFS | Not reported | Intracranial ORR 86% pooled | Major grade 3-4 AEs: neutropenia 13%, anemia 13% | Ke et al. 2023, Investig New Drugs. https://doi.org/10.1007/s10637-023-01390-3 | (novello2023retfusionpositivenonsmall pages 1-2) |
| Exploratory comparative effectiveness analysis | 1L advanced/metastatic RET-activated cancers; NSCLC subgroup | Selpercatinib vs standard therapies | Not extractable for NSCLC subgroup from retrieved context | 85.3% vs 39.7% (NSCLC) | TTP HR 0.54; TTD HR 0.29; TTNT-D HR 0.48 | Not directly reported | Not reported | Not detailed in retrieved excerpt | Braud et al. 2023, Cancers. https://doi.org/10.3390/cancers16010140 | (clark2023selectiveretinhibitors pages 4-5) |


*Table: This table summarizes key efficacy, CNS activity, and safety outcomes for selective RET inhibitors in RET fusion-positive NSCLC, emphasizing 2023-2024 trial and real-world evidence. It is useful for comparing first-line randomized data with retrospective practice-based outcomes and pooled estimates.*

**Definitive first‑line randomized evidence:** NEJM 2023 LIBRETTO‑431 abstract states: “**Treatment with selpercatinib led to significantly longer progression‑free survival than platinum‑based chemotherapy with or without pembrolizumab among patients with advanced RET fusion‑positive NSCLC**” and reports median PFS **24.8 vs 11.2 months** (HR 0.46; P<0.001) with ORR **84% vs 65%** (zhou2023firstlineselpercatinibor pages 1-3).

### 11.3 Prognostic factors
- **Fusion partner** may be prognostic: Chen et al. summarize median OS differences by partner (e.g., 52.8 vs 38.5 vs 19.1 months for CCDC6 vs other vs KIF5B in a cited dataset) (chen2024retinhibitorsin pages 8-10).
- **Performance status:** In a 2024 China real‑world cohort, poor ECOG performance status was associated with shorter PFS (P=0.018) (lei2024efficacyandsafety pages 1-2).

---

## 12. Treatment

### 12.1 Standard targeted therapies (current practice)
Recent authoritative reviews state that selective RET inhibitors **selpercatinib** and **pralsetinib** are preferred first‑line options for metastatic RET fusion‑positive NSCLC and recommended subsequently if not used first‑line (novello2023retfusionpositivenonsmall pages 1-2, novello2023retfusionpositivenonsmall pages 8-9).

**Mechanism/class:** selective RET TKIs (ATP‑competitive RET kinase inhibition) (gouda2023precisiononcologywith pages 2-4).

**MAXO suggestions:**
- MAXO:0001020 pharmacotherapy  
- MAXO:0000148 targeted therapy (suggested)  
- MAXO:0000747 tyrosine kinase inhibitor therapy (suggested)

### 12.2 Key 2023–2024 developments
- **Phase III first‑line superiority and CNS protection:** LIBRETTO‑431 showed improved PFS and reduced CNS progression with selpercatinib (zhou2023firstlineselpercatinibor pages 1-3, perol2024cnsprotectiveeffect pages 3-4).
- **CNS outcomes:** In patients without baseline CNS metastases, 12‑month cumulative incidence of CNS progression was 1.1% vs 14.7% (cause‑specific HR 0.17) (perol2024cnsprotectiveeffect pages 3-4, spitaleri2024nonsmallcelllungcancers pages 9-11).

### 12.3 Treatment sequencing after progression
After progression on selective RET inhibitors, evidence‑synthesis reviews commonly cite:
- **Chemotherapy**, especially **pemetrexed‑based** regimens, as a reasonable option in the refractory setting (chen2024retinhibitorsin pages 6-8, chen2024retinhibitorsin pages 5-6).
- **Resistance‑directed strategies** under investigation: next‑generation RET inhibitors (e.g., TPX‑0046, LOXO‑260, TAS0953/HM06) intended to overcome solvent‑front resistance (novello2023retfusionpositivenonsmall pages 8-9).
- **Combination strategies** for bypass or acquired fusions (e.g., selpercatinib + osimertinib for EGFR‑mutant NSCLC with acquired RET fusion; reported response rate 50% in evaluable patients, median duration of response 11 months) (novello2023retfusionpositivenonsmall pages 8-9).

### 12.4 Real-world implementation and treatment patterns
A 2024 multicenter China cohort (n=64) reported use of pralsetinib in 48.4% of patients and substantially longer median PFS with pralsetinib than chemotherapy or multitarget inhibitors (wang2024evolutionoftreatment pages 1-2).

---

## 13. Prevention

RET fusions themselves are not currently preventable at the molecular level; prevention is primarily through **lung cancer risk reduction** and **early detection**.

### 13.1 Primary prevention
- **Smoking cessation** is emphasized in lung cancer prevention and screening guidance; ACS recommends cessation counseling and pharmacotherapy for current smokers considering screening (wolf2024screeningforlung pages 7-7).

### 13.2 Secondary prevention (screening / early detection)
**American Cancer Society (ACS) guideline update (published Nov 2024; “2023 guideline update”):** recommends **annual low‑dose CT (LDCT)** for asymptomatic individuals aged **50–80** with **≥20 pack‑year** smoking history (current or former smokers), and recommends not using years‑since‑quitting as an eligibility criterion (wolf2024screeningforlung pages 7-7, wolf2024screeningforlung pages 2-3).

This screening guidance is not RET‑specific, but determines the population in which early lung cancer (including RET‑rearranged disease) may be detected.

---

## 14. Other Species / Natural Disease

No naturally occurring RET fusion‑driven lung cancer in non‑human species was identified in the retrieved evidence.

---

## 15. Model Organisms

### 15.1 Engineered mouse models
A lung‑specific **KIF5B‑RET transgenic mouse model** (SPC promoter; C57BL/6J background) develops multifocal lung hyperplasias/adenomas/adenocarcinomas; this model was used to test vandetanib treatment and tumor suppression (saito2014amousemodel pages 1-2).

### 15.2 Cellular models (in vitro)
Multiple RET fusion‑positive NSCLC cell models (including LC‑2/ad and patient‑derived lines) have been used to study pathway inhibition, adaptive resistance, and bypass activation (rocco2023treatmentofadvanced pages 8-10).

---

# Key recent statistics (2023–2024 emphasis)

- RET fusion prevalence in NSCLC: ~**1–2%** (novello2023retfusionpositivenonsmall pages 1-2, chen2024retinhibitorsin pages 3-5).  
- China prevalence series: **1.4% (84/6125)** and **1.77% (167/9431)** (wang2024evolutionoftreatment pages 1-2).  
- Brain metastasis: **~25% at diagnosis** (advanced) and **46% lifetime** (novello2023retfusionpositivenonsmall pages 1-2, clark2023selectiveretinhibitors pages 1-2).  
- NEJM 2023 LIBRETTO‑431: median PFS **24.8 vs 11.2 months**; ORR **84% vs 65%**; CNS progression HR **0.28** (zhou2023firstlineselpercatinibor pages 1-3).  
- JCO 2024 CNS update: 12‑month CNS progression **1.1% vs 14.7%**, cause‑specific HR **0.17** (perol2024cnsprotectiveeffect pages 3-4).  
- Real‑world China (2024) first‑line RET‑TKI: ORR **73.1%**, mPFS **22.7 months** (lei2024efficacyandsafety pages 1-2).  
- Rapid diagnostic assay (Virchows Arch 2024): RET fusion sensitivity **100%**, specificity **99.3%**; ~3 hour turnaround (melchior2024multicenterevaluationof pages 1-2).

---

# Evidence notes and gaps

- **PMIDs:** The retrieved context includes DOI/journal metadata and narrative claims but does not consistently provide PMIDs. Where PMIDs are required for every claim, additional PubMed cross‑referencing would be needed beyond the current retrieved evidence set.
- **ICD‑10/ICD‑11/MeSH/Orphanet/OMIM/MONDO child term:** Specific identifiers for “RET fusion‑positive NSCLC” were not present in the retrieved evidence; only parent NSCLC terms were identified via Open Targets output (novello2023retfusionpositivenonsmall pages 1-2).

---

# URLs and publication dates (selected primary sources)

- Zhou et al. “First‑Line Selpercatinib or Chemotherapy and Pembrolizumab in RET Fusion–Positive NSCLC.” **NEJM** (Nov 2023). https://doi.org/10.1056/NEJMoa2309457 (zhou2023firstlineselpercatinibor pages 1-3)
- Pérol et al. “CNS Protective Effect of Selpercatinib…” **J Clin Oncol** (Jul 2024). https://doi.org/10.1200/JCO.24.00724 (perol2024cnsprotectiveeffect pages 3-4)
- Lei et al. “Efficacy and safety of RET‑TKI… real‑world…” **BMC Cancer** (Nov 2024). https://doi.org/10.1186/s12885-024-13155-z (lei2024efficacyandsafety pages 1-2)
- Wang et al. “Evolution of treatment strategies… China real‑world…” **BMC Pulm Med** (Nov 2024). https://doi.org/10.1186/s12890-024-03371-5 (wang2024evolutionoftreatment pages 1-2)
- Chen et al. “RET inhibitors in RET fusion‑positive lung cancers: Past, Present, and Future.” **Drugs** (Jul 2024). https://doi.org/10.1007/s40265-024-02040-5 (chen2024retinhibitorsin pages 5-6)
- Spitaleri et al. “NSCLCs harboring RET gene fusion…” **Cancers** (Aug 2024). https://doi.org/10.3390/cancers16162877 (spitaleri2024nonsmallcelllungcancers pages 9-11)
- Wolf et al. “Screening for lung cancer: 2023 guideline update from the American Cancer Society.” **CA Cancer J Clin** (Nov 2024). https://doi.org/10.3322/caac.21811 (wolf2024screeningforlung pages 7-7)
- Melchior et al. “Multicenter evaluation… Idylla GeneFusion Assay…” **Virchows Archiv** (Mar 2024). https://doi.org/10.1007/s00428-024-03778-9 (melchior2024multicenterevaluationof pages 1-2)
- Saito et al. “A mouse model of KIF5B‑RET fusion‑dependent lung tumorigenesis.” **Carcinogenesis** (Nov 2014). https://doi.org/10.1093/carcin/bgu158 (saito2014amousemodel pages 1-2)


References

1. (novello2023retfusionpositivenonsmall pages 1-2): Silvia Novello, Raffaele Califano, Niels Reinmuth, Antonella Tamma, and Tarun Puri. Ret fusion-positive non-small cell lung cancer: the evolving treatment landscape. The Oncologist, 28:402-413, Feb 2023. URL: https://doi.org/10.1093/oncolo/oyac264, doi:10.1093/oncolo/oyac264. This article has 51 citations.

2. (chen2024retinhibitorsin pages 3-5): Monica F. Chen, Matteo Repetto, Clare Wilhelm, and Alexander Drilon. Ret inhibitors in ret fusion-positive lung cancers: past, present, and future. Drugs, 84:1035-1053, Jul 2024. URL: https://doi.org/10.1007/s40265-024-02040-5, doi:10.1007/s40265-024-02040-5. This article has 13 citations and is from a domain leading peer-reviewed journal.

3. (rocco2023treatmentofadvanced pages 5-6): Danilo Rocco, Luigi Sapio, Luigi Della Gravara, Silvio Naviglio, and Cesare Gridelli. Treatment of advanced non-small cell lung cancer with ret fusions: reality and hopes. International Journal of Molecular Sciences, 24:2433, Jan 2023. URL: https://doi.org/10.3390/ijms24032433, doi:10.3390/ijms24032433. This article has 20 citations.

4. (zhou2023firstlineselpercatinibor pages 1-3): Caicun Zhou, Benjamin Solomon, Herbert H. Loong, Keunchil Park, Maurice Pérol, Edurne Arriola, Silvia Novello, Baohui Han, Jianying Zhou, Andrea Ardizzoni, M. Perez Mak, Fernando C. Santini, Yasir Y. Elamin, Alexander Drilon, Jürgen Wolf, Nalin Payakachat, Minji K. Uh, Deborah Rajakumar, Hongmei Han, Tarun Puri, Victoria Soldatenkova, A. Bence Lin, Boris K. Lin, and Koichi Goto. First-line selpercatinib or chemotherapy and pembrolizumab in <i>ret</i> fusion–positive nsclc. New England Journal of Medicine, 389:1839-1850, Nov 2023. URL: https://doi.org/10.1056/nejmoa2309457, doi:10.1056/nejmoa2309457. This article has 218 citations and is from a highest quality peer-reviewed journal.

5. (spitaleri2024nonsmallcelllungcancers pages 1-2): Gianluca Spitaleri, Pamela Trillo Aliaga, Ilaria Attili, Ester Del Signore, Carla Corvaja, Gloria Pellizzari, Jalissa Katrini, Antonio Passaro, and Filippo de Marinis. Non-small-cell lung cancers (nsclcs) harboring ret gene fusion, from their discovery to the advent of new selective potent ret inhibitors: “shadows and fogs”. Cancers, 16:2877, Aug 2024. URL: https://doi.org/10.3390/cancers16162877, doi:10.3390/cancers16162877. This article has 7 citations.

6. (lei2024efficacyandsafety pages 1-2): Siyu Lei, Linyan Tian, Lu Yang, Yaning Yang, Junling Li, Xingsheng Hu, Xuezhi Hao, Haiyan Xu, and Yan Wang. Efficacy and safety of ret-tki in advanced ret-rearranged non-small cell lung cancer in china: a real-world retrospective chart review. BMC Cancer, Nov 2024. URL: https://doi.org/10.1186/s12885-024-13155-z, doi:10.1186/s12885-024-13155-z. This article has 0 citations and is from a peer-reviewed journal.

7. (shen2024recentprogressof pages 1-3): Jiayi Shen, Liping Chen, Yulan Song, Sheng Chen, Wei Guo, and Yongdong Li. Recent progress of small-molecule of ret inhibitors against non-small cell lung cancer. AAPS Open, Jun 2024. URL: https://doi.org/10.1186/s41120-024-00094-z, doi:10.1186/s41120-024-00094-z. This article has 3 citations.

8. (chen2024retinhibitorsin pages 1-3): Monica F. Chen, Matteo Repetto, Clare Wilhelm, and Alexander Drilon. Ret inhibitors in ret fusion-positive lung cancers: past, present, and future. Drugs, 84:1035-1053, Jul 2024. URL: https://doi.org/10.1007/s40265-024-02040-5, doi:10.1007/s40265-024-02040-5. This article has 13 citations and is from a domain leading peer-reviewed journal.

9. (clark2023selectiveretinhibitors pages 1-2): Lisa Clark, Geoff Fisher, Sue Brook, Sital Patel, and Hendrik-Tobias Arkenau. Selective ret inhibitors (sris) in cancer: a journey from multi-kinase inhibitors to the next generation of sris. Cancers, 16:31, Dec 2023. URL: https://doi.org/10.3390/cancers16010031, doi:10.3390/cancers16010031. This article has 10 citations.

10. (spitaleri2024nonsmallcelllungcancers pages 2-4): Gianluca Spitaleri, Pamela Trillo Aliaga, Ilaria Attili, Ester Del Signore, Carla Corvaja, Gloria Pellizzari, Jalissa Katrini, Antonio Passaro, and Filippo de Marinis. Non-small-cell lung cancers (nsclcs) harboring ret gene fusion, from their discovery to the advent of new selective potent ret inhibitors: “shadows and fogs”. Cancers, 16:2877, Aug 2024. URL: https://doi.org/10.3390/cancers16162877, doi:10.3390/cancers16162877. This article has 7 citations.

11. (gouda2023precisiononcologywith pages 2-4): Mohamed A. Gouda and Vivek Subbiah. Precision oncology with selective ret inhibitor selpercatinib in ret-rearranged cancers. Therapeutic Advances in Medical Oncology, Jun 2023. URL: https://doi.org/10.1177/17588359231177015, doi:10.1177/17588359231177015. This article has 21 citations and is from a peer-reviewed journal.

12. (rocha2023importanceofthe pages 16-19): ABMA Rocha. Importance of the ret mutation in lung cancer. Unknown journal, 2023.

13. (lee2024libretto431confirmingthe pages 2-4): Alexandria Lee and Sai-Hong Ou. Libretto-431: confirming the superiority of selpercatinib to chemotherapy and the lack of efficacy of immune checkpoint inhibitors in advanced ret fusion-positive (ret+) nsclc, another unique never-smoker predominant molecular subtype of nsclc. Lung Cancer: Targets and Therapy, 15:75-80, May 2024. URL: https://doi.org/10.2147/lctt.s460147, doi:10.2147/lctt.s460147. This article has 6 citations.

14. (wang2024evolutionoftreatment pages 1-2): An Wang, Tao Li, Yun-ye Mao, Ming Gao, Sheng Shu, Chang-hong Xia, Yi Dong, Min Liu, Jin-liang Wang, Jun-xun Ma, and Yi Hu. Evolution of treatment strategies for solid tumors with ret rearrangement in china and real-world treatment status of non-small cell lung cancer (nsclc). BMC Pulmonary Medicine, Nov 2024. URL: https://doi.org/10.1186/s12890-024-03371-5, doi:10.1186/s12890-024-03371-5. This article has 2 citations and is from a peer-reviewed journal.

15. (novello2023retfusionpositivenonsmall pages 8-9): Silvia Novello, Raffaele Califano, Niels Reinmuth, Antonella Tamma, and Tarun Puri. Ret fusion-positive non-small cell lung cancer: the evolving treatment landscape. The Oncologist, 28:402-413, Feb 2023. URL: https://doi.org/10.1093/oncolo/oyac264, doi:10.1093/oncolo/oyac264. This article has 51 citations.

16. (rocco2023treatmentofadvanced pages 8-10): Danilo Rocco, Luigi Sapio, Luigi Della Gravara, Silvio Naviglio, and Cesare Gridelli. Treatment of advanced non-small cell lung cancer with ret fusions: reality and hopes. International Journal of Molecular Sciences, 24:2433, Jan 2023. URL: https://doi.org/10.3390/ijms24032433, doi:10.3390/ijms24032433. This article has 20 citations.

17. (saito2014amousemodel pages 1-2): Motonobu Saito, Teruhide Ishigame, Koji Tsuta, Kensuke Kumamoto, Toshio Imai, and Takashi Kohno. A mouse model of kif5b-ret fusion-dependent lung tumorigenesis. Carcinogenesis, 35 11:2452-6, Nov 2014. URL: https://doi.org/10.1093/carcin/bgu158, doi:10.1093/carcin/bgu158. This article has 59 citations and is from a peer-reviewed journal.

18. (spitaleri2024nonsmallcelllungcancers pages 9-11): Gianluca Spitaleri, Pamela Trillo Aliaga, Ilaria Attili, Ester Del Signore, Carla Corvaja, Gloria Pellizzari, Jalissa Katrini, Antonio Passaro, and Filippo de Marinis. Non-small-cell lung cancers (nsclcs) harboring ret gene fusion, from their discovery to the advent of new selective potent ret inhibitors: “shadows and fogs”. Cancers, 16:2877, Aug 2024. URL: https://doi.org/10.3390/cancers16162877, doi:10.3390/cancers16162877. This article has 7 citations.

19. (melchior2024multicenterevaluationof pages 1-2): Linea Melchior, Astrid Hirschmann, Paul Hofman, Christophe Bontoux, Angel Concha, Salima Mrabet-Dahbi, Pascal Vannuffel, Emmanuel Watkin, Martina Putzová, Stefania Scarpino, Anne Cayre, Paloma Martin, Robert Stoehr, and Arndt Hartmann. Multicenter evaluation of an automated, multiplex, rna-based molecular assay for detection of alk, ros1, ret fusions and met exon 14 skipping in nsclc. Virchows Archiv, 484:677-686, Mar 2024. URL: https://doi.org/10.1007/s00428-024-03778-9, doi:10.1007/s00428-024-03778-9. This article has 5 citations and is from a peer-reviewed journal.

20. (novello2023retfusionpositivenonsmall pages 4-5): Silvia Novello, Raffaele Califano, Niels Reinmuth, Antonella Tamma, and Tarun Puri. Ret fusion-positive non-small cell lung cancer: the evolving treatment landscape. The Oncologist, 28:402-413, Feb 2023. URL: https://doi.org/10.1093/oncolo/oyac264, doi:10.1093/oncolo/oyac264. This article has 51 citations.

21. (chen2024retinhibitorsin pages 5-6): Monica F. Chen, Matteo Repetto, Clare Wilhelm, and Alexander Drilon. Ret inhibitors in ret fusion-positive lung cancers: past, present, and future. Drugs, 84:1035-1053, Jul 2024. URL: https://doi.org/10.1007/s40265-024-02040-5, doi:10.1007/s40265-024-02040-5. This article has 13 citations and is from a domain leading peer-reviewed journal.

22. (chen2024retinhibitorsin pages 8-10): Monica F. Chen, Matteo Repetto, Clare Wilhelm, and Alexander Drilon. Ret inhibitors in ret fusion-positive lung cancers: past, present, and future. Drugs, 84:1035-1053, Jul 2024. URL: https://doi.org/10.1007/s40265-024-02040-5, doi:10.1007/s40265-024-02040-5. This article has 13 citations and is from a domain leading peer-reviewed journal.

23. (NCT03037385 chunk 1):  Phase 1/2 Study of the Highly-selective RET Inhibitor, Pralsetinib (BLU-667), in Participants With Thyroid Cancer, Non-Small Cell Lung Cancer, and Other Advanced Solid Tumors. Hoffmann-La Roche. 2017. ClinicalTrials.gov Identifier: NCT03037385

24. (clark2023selectiveretinhibitors pages 4-5): Lisa Clark, Geoff Fisher, Sue Brook, Sital Patel, and Hendrik-Tobias Arkenau. Selective ret inhibitors (sris) in cancer: a journey from multi-kinase inhibitors to the next generation of sris. Cancers, 16:31, Dec 2023. URL: https://doi.org/10.3390/cancers16010031, doi:10.3390/cancers16010031. This article has 10 citations.

25. (perol2024cnsprotectiveeffect pages 3-4): Maurice Pérol, Benjamin J. Solomon, Koichi Goto, Keunchil Park, Ernest Nadal, Emilio Bria, Claudio Martin, Jair Bar, Justin N. Williams, Tarun Puri, Jian Li, Minji K. Uh, Boris K. Lin, and Caicun Zhou. Cns protective effect of selpercatinib in first-line <i>ret</i> fusion-positive advanced non–small cell lung cancer. Journal of Clinical Oncology, 42:2500-2505, Jul 2024. URL: https://doi.org/10.1200/jco.24.00724, doi:10.1200/jco.24.00724. This article has 14 citations and is from a highest quality peer-reviewed journal.

26. (chen2024retinhibitorsin pages 6-8): Monica F. Chen, Matteo Repetto, Clare Wilhelm, and Alexander Drilon. Ret inhibitors in ret fusion-positive lung cancers: past, present, and future. Drugs, 84:1035-1053, Jul 2024. URL: https://doi.org/10.1007/s40265-024-02040-5, doi:10.1007/s40265-024-02040-5. This article has 13 citations and is from a domain leading peer-reviewed journal.

27. (wolf2024screeningforlung pages 7-7): Andrew M. D. Wolf, Kevin C. Oeffinger, Tina Ya‐Chen Shih, Louise C. Walter, Timothy R. Church, Elizabeth T. H. Fontham, Elena B. Elkin, Ruth D. Etzioni, Carmen E. Guerra, Rebecca B. Perkins, Karli K. Kondo, Tyler B. Kratzer, Deana Manassaram‐Baptiste, William L. Dahut, and Robert A. Smith. Screening for lung cancer: 2023 guideline update from the american cancer society. CA: A Cancer Journal for Clinicians, 74:50-81, Nov 2024. URL: https://doi.org/10.3322/caac.21811, doi:10.3322/caac.21811. This article has 398 citations and is from a domain leading peer-reviewed journal.

28. (wolf2024screeningforlung pages 2-3): Andrew M. D. Wolf, Kevin C. Oeffinger, Tina Ya‐Chen Shih, Louise C. Walter, Timothy R. Church, Elizabeth T. H. Fontham, Elena B. Elkin, Ruth D. Etzioni, Carmen E. Guerra, Rebecca B. Perkins, Karli K. Kondo, Tyler B. Kratzer, Deana Manassaram‐Baptiste, William L. Dahut, and Robert A. Smith. Screening for lung cancer: 2023 guideline update from the american cancer society. CA: A Cancer Journal for Clinicians, 74:50-81, Nov 2024. URL: https://doi.org/10.3322/caac.21811, doi:10.3322/caac.21811. This article has 398 citations and is from a domain leading peer-reviewed journal.
