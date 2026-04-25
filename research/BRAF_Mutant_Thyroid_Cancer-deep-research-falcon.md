---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-05T12:38:33.495854'
end_time: '2026-04-05T12:46:14.836738'
duration_seconds: 461.34
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: BRAF-Mutant Papillary Thyroid Cancer
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 56
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** BRAF-Mutant Papillary Thyroid Cancer
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **BRAF-Mutant Papillary Thyroid Cancer** covering all of the
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
- **Disease Name:** BRAF-Mutant Papillary Thyroid Cancer
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **BRAF-Mutant Papillary Thyroid Cancer** covering all of the
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


# Comprehensive Research Report: BRAF‑Mutant Papillary Thyroid Cancer (PTC)

## Target Disease
- **Disease name:** BRAF‑mutant papillary thyroid carcinoma (PTC), most commonly **BRAFV600E**
- **Category:** Molecularly defined subtype of differentiated thyroid carcinoma (DTC) / papillary thyroid carcinoma
- **MONDO ID:** Not retrieved from the available tool evidence in this run (MONDO term retrieval for this exact molecularly defined subtype was not available in the gathered sources).

---

## 1. Disease Information

### 1.1 Overview / definition
Papillary thyroid carcinoma (PTC) is the most common thyroid cancer subtype and a malignancy of thyroid follicular epithelial cells. “BRAF‑mutant PTC” refers to PTC harboring activating **BRAF** alterations, most commonly **BRAFV600E**, a driver that constitutively activates MAPK signaling. BRAFV600E is defined as **c.1799T>A (p.Val600Glu)**. (webster2024theprevalenceand pages 2-2)

**Abstract‑quotable definition (RAI‑refractory context):** In radioiodine‑refractory disease, loss of differentiation features (including iodide uptake) is “correlat[ed] with the degree of mitogen‑activated protein kinase (MAPK) activation, which is higher in tumors with BRAF…mutations…Hence, inhibition of…MEK…could sensitize RAI refractivity.” (Aashiq et al., 2019; PMID not extracted by tool; DOI/URL in source) (tan2024tertpromotermutations pages 9-10)

### 1.2 Key identifiers and ontology mapping
Because this run’s tool outputs were optimized for literature/trials rather than ontology registries (OMIM/MeSH/ICD/MONDO direct lookups are not available as dedicated tools here), only partial identifiers can be provided:
- **Disease family identifiers present in Open Targets evidence:**
  - **Papillary thyroid carcinoma:** Open Targets disease ID **EFO_0000641** (tan2024tertpromotermutations pages 9-10)
  - **Differentiated thyroid carcinoma:** Open Targets disease ID **EFO_1002017** (tan2024tertpromotermutations pages 9-10)
- **Gene/target:** **BRAF** (Ensembl: ENSG00000157764) (tan2024tertpromotermutations pages 9-10)

### 1.3 Synonyms / alternative names
- Papillary thyroid cancer
- Papillary thyroid carcinoma
- Differentiated thyroid carcinoma (broader category)
- BRAFV600E‑positive PTC
- “BRAF‑like” PTC (molecular class used in TCGA‑style frameworks) (abdelmoula2024reviewhistopathologicalmolecularclassifications pages 5-5)

### 1.4 Data provenance
The information here is derived primarily from **aggregated disease‑level resources** (peer‑reviewed reviews, retrospective cohorts, meta‑analyses, and ClinicalTrials.gov records), rather than individual EHR records. (brumfield2025prevalenceandclinical pages 1-2, ovcaricek2024redifferentiationtherapiesin pages 6-7, NCT01534897 chunk 1)

---

## 2. Etiology

### 2.1 Disease causal factors
**Primary causal factor (somatic driver):** The dominant causal event in BRAF‑mutant PTC is a somatic activating mutation in **BRAF**, especially **BRAFV600E**, which drives high‑output MAPK/ERK signaling. (webster2024theprevalenceand pages 2-2, cortas2023tyrosinekinaseinhibitors pages 2-4)

### 2.2 Risk factors
**Molecular risk factors for aggressive behavior / dedifferentiation**
- **TERT promoter (TERTp) mutations** are repeatedly highlighted as strong adverse prognostic markers in DTC and interact negatively with BRAFV600E. (tan2024tertpromotermutations pages 9-10)

**Population/clinical risk factors for recurrence (example cohort):** In a 301‑patient single‑institution cohort, recurrence was associated with **large‑volume nodal disease burden** and **male sex**, rather than BRAFV600E alone on multivariable analysis. (brumfield2025prevalenceandclinical pages 1-2)

### 2.3 Protective factors
Protective factors specific to *BRAF‑mutant PTC* were not clearly identified in the gathered evidence. However, the incidence‑trend literature argues that reductions in overdiagnosis/changes in screening and management practices can reduce observed incidence of thyroid cancer (including PTC), which can be viewed as a population‑level protective factor against overtreatment. (fwelo2024impactofamerican pages 1-2)

### 2.4 Gene–environment interactions
Explicit GxE interaction data were not captured in the retrieved evidence. One review notes BRAF fusions in radiation‑associated cases, indicating environmental exposure may shape mutation spectra in some settings, but quantitative interaction effects were not extractable from the provided excerpts. (voinea2024pathogenesisandmanagement pages 2-4)

---

## 3. Phenotypes (clinical presentation)

### 3.1 Core phenotypes and suggested HPO terms
PTC commonly presents as a thyroid nodule and may involve cervical lymphadenopathy; BRAFV600E has been associated in many meta‑analyses with adverse local features (extrathyroidal extension, nodal metastasis), though results vary by cohort and adjustment. (webster2024theprevalenceand pages 2-2, brumfield2025prevalenceandclinical pages 1-2)

Suggested phenotype mapping (HPO terms; canonical terms shown, not all were explicitly listed in the evidence excerpts):
- **Thyroid nodule / thyroid mass:** *Thyroid nodule* (HP:0002890)
- **Cervical lymph node metastasis / lymphadenopathy:** *Lymphadenopathy* (HP:0002716)
- **Extrathyroidal extension / local invasion:** *Invasive neoplasm* (HP:0100758) (approximate mapping)
- **Multifocal tumors:** *Multifocal neoplasm* (HP:0030445) (approximate mapping)
- **Distant metastasis (advanced cases):** *Metastatic neoplasm* (HP:0003002)

### 3.2 Frequency and clinical correlations (selected recent quantitative data)
- **BRAFV600E prevalence in PTC:** A single‑institution series found **78.7%** BRAFV600E prevalence overall, with enrichment by morphology (classic 88%, extensive follicular growth 38%, tall cell 100%). (Brumfield 2025; publication date Apr 2025; URL: https://doi.org/10.1007/s12022-025-09859-y) (brumfield2025prevalenceandclinical pages 1-2)
- **Association with recurrence:** In the same cohort, BRAFV600E was **not significantly associated with recurrence** (HR 0.71; p=0.4) after adjusting for clinicopathologic factors. (brumfield2025prevalenceandclinical pages 1-2)

### 3.3 Quality of life impact
Quality‑of‑life instruments (e.g., EQ‑5D, SF‑36, PROMIS) were not reported in the evidence excerpts retrieved here; for BRAF‑mutant disease, QoL is often dominated by treatment effects (thyroidectomy, lifelong levothyroxine, potential systemic therapy toxicity in RAIR disease), but quantitative QoL data were not extractable from these sources.

---

## 4. Genetic / Molecular Information

### 4.1 Causal genes
- **BRAF** (HGNC:1097; Ensembl ENSG00000157764 as returned via Open Targets) is the key causal/driver gene in this molecular subtype. (tan2024tertpromotermutations pages 9-10)

### 4.2 Pathogenic variants
- **BRAFV600E (c.1799T>A; p.Val600Glu)**: activating missense hotspot variant and predominant BRAF alteration in PTC. (webster2024theprevalenceand pages 2-2)

**Somatic vs germline:** BRAFV600E in PTC is a **somatic oncogenic driver** in the vast majority of cases (not presented as germline in the retrieved excerpts). (webster2024theprevalenceand pages 2-2)

### 4.3 Modifier/cooperating alterations
- **TERT promoter mutations:** strongly adverse modifier, especially in combination with BRAFV600E. (tan2024tertpromotermutations pages 9-10)
- Additional cooperating alterations referenced in reviews (e.g., TP53, PTEN) are associated with aggressiveness and dedifferentiation, and are relevant to progression beyond well‑differentiated PTC. (abdelmoula2024reviewhistopathologicalmolecularclassifications pages 5-5)

### 4.4 Epigenetic/chromatin mechanisms
Chromatin remodeling state can determine whether MAPK blockade can restore thyroid differentiation. Loss of SWI/SNF complex subunits in BRAF‑driven mouse models produced a repressive chromatin state and resistance to redifferentiation. (tan2024tertpromotermutations pages 9-10)

### 4.5 Suggested GO and Cell Ontology (CL) terms
**Key pathways/processes (GO Biological Process suggestions):**
- MAPK cascade (GO:0000165)
- ERK1/ERK2 cascade (GO:0070371)
- Regulation of cell proliferation (GO:0008283)
- Epithelial cell differentiation (GO:0030855)
- Iodide transport (GO:0015705)

**Key cell types (CL suggestions):**
- Thyroid follicular cell / thyrocyte (CL:0000115)
- Myeloid‑derived suppressor cell (not always in CL as a single canonical term; can map to immature myeloid populations; the study explicitly focuses on MDSCs) (tan2024tertpromotermutations pages 9-10)

---

## 5. Environmental Information
No specific toxins, lifestyle factors, or infectious agents were supported by the retrieved evidence snippets as causal contributors specifically to BRAF‑mutant PTC. In the incidence‑trend literature, imaging and screening practices are emphasized as drivers of apparent incidence, rather than an identified infectious etiology. (fwelo2024impactofamerican pages 1-2)

---

## 6. Mechanism / Pathophysiology

### 6.1 Causal chain (high‑level)
1. **Somatic BRAFV600E** activates the **MAPK/ERK pathway** with high signaling output. (webster2024theprevalenceand pages 2-2, cortas2023tyrosinekinaseinhibitors pages 2-4)
2. High MAPK output drives **dedifferentiation** (downregulation of thyroid lineage transcriptional programs) and disrupts the iodide‑handling machinery, including **NIS/SLC5A5** expression and/or membrane targeting. (voinea2024pathogenesisandmanagement pages 2-4, chen2024systemictreatmentsfor pages 1-2)
3. Reduced NIS function causes **loss of radioiodine avidity** and contributes to **radioiodine‑refractory (RAIR) disease**, which has markedly worse outcomes. (cortas2023tyrosinekinaseinhibitors pages 1-2, chen2024systemictreatmentsfor pages 1-2)
4. **Co‑mutations (e.g., TERT promoter)** accelerate progression/dedifferentiation, increasing RAIR likelihood and worsening prognosis. (tan2024tertpromotermutations pages 9-10)

**Abstract‑quotable mechanistic framing (RAIR‑DTC):** “alterations…initiating tumour cell dedifferentiation events, accompanied by reduced or virtually absent expression of the sodium/iodine symporter (NIS)…[leading to] iodine‑refractory differentiated thyroid cancer (RAIR‑DTC)” (Zhao et al., Frontiers in Endocrinology 2024; URL: https://doi.org/10.3389/fendo.2023.1320044). (tan2024tertpromotermutations pages 9-10)

### 6.2 Immune microenvironment mechanism (expert mechanistic insight)
BRAFV600E can promote immune suppression via a TBX3–CXCR2 ligand axis that recruits **myeloid‑derived suppressor cells (MDSCs)**; experimental inhibition of CXCR2 or repression of MDSCs improved the effect of MAPK inhibitor therapy in advanced thyroid cancer models. (Zhang et al., Nature Communications 2022; URL: https://doi.org/10.1038/s41467-022-29000-5). (tan2024tertpromotermutations pages 9-10)

---

## 7. Anatomical Structures Affected

### 7.1 Organ/tissue
- **Primary organ:** thyroid gland (UBERON:0002046)
- **Primary tissue/cell compartment:** follicular epithelium (thyrocytes) (CL:0000115)
- **Common metastatic site (advanced disease):** cervical lymph nodes (UBERON:0002509; approximate) (supported conceptually by clinical associations in reviews, though frequencies vary) (webster2024theprevalenceand pages 2-2)

### 7.2 Subcellular (GO Cellular Component suggestions)
- Plasma membrane localization of **NIS** is central to RAI uptake (GO:0005886 plasma membrane; in context of NIS trafficking/function). (voinea2024pathogenesisandmanagement pages 2-4)

---

## 8. Temporal Development

### 8.1 Onset
Typically adult onset (many cases diagnosed in middle age), with notable incidence in young adults; PTC is also common in pediatric/adolescent thyroid cancers but BRAFV600E is less frequent in children than adults. (branigan2023developmentofnovel pages 1-2, cortas2023tyrosinekinaseinhibitors pages 2-4)

### 8.2 Progression
Most DTC/PTC is indolent, but a subset progresses to metastatic and RAIR disease. Reviews cited in this run indicate that RAIR disease comprises **5–15% of DTCs** and **~50% of metastatic DTCs**, reflecting progression/dedifferentiation in advanced settings. (chen2024systemictreatmentsfor pages 1-2)

---

## 9. Inheritance and Population

### 9.1 Epidemiology and trends
**SEER‑based U.S. incidence trends (2000–2020) and guideline inflection points:** A joinpoint analysis of SEER data found thyroid cancer incidence increased rapidly from **2000–2009** (AAPC **5.8%**), increased modestly **2010–2015** (AAPC **1.1%**), then decreased significantly **2016–2020** (AAPC **−4.8%**), with inflection points around 2009 and 2015 aligned to ATA management revisions. (Fwelo et al., Journal of Clinical Medicine, Dec 2024; URL: https://doi.org/10.3390/jcm14010028). (fwelo2024impactofamerican pages 1-2)

**Histology‑specific trends:** In the same study’s stratified results, **papillary thyroid carcinoma showed the largest increase** over 2000–2020 (overall APC 3.3) while follicular thyroid carcinoma declined modestly. (fwelo2024impactofamerican pages 7-8)

### 9.2 BRAF mutation prevalence in PTC
A 2025 single‑institution cohort reported **78.7%** BRAFV600E prevalence, with strong subtype enrichment (classic PTC 88%; tall cell 100%). (brumfield2025prevalenceandclinical pages 1-2)

### 9.3 Inheritance
BRAFV600E in PTC is primarily **somatic**; Mendelian inheritance is not applicable for the disease entity as defined here. (webster2024theprevalenceand pages 2-2)

---

## 10. Diagnostics

### 10.1 Pathology and molecular testing
**Actionable biomarker testing (expert consensus):** A 2024 expert panel consensus statement emphasizes that identification of actionable biomarkers via germline and somatic testing is now integral to thyroid cancer management, and notes that RET and BRAF testing are well established. (Mete et al., Endocrine Pathology, Nov 2024; URL: https://doi.org/10.1007/s12022-024-09836-x). (tan2024tertpromotermutations pages 9-10)

**BRAFV600E detection:** The Brumfield cohort notes VE1 immunohistochemistry is used clinically and described as highly sensitive/specific in that context. (brumfield2025prevalenceandclinical pages 1-2)

### 10.2 Imaging / RAIR evaluation
RAIR‑DTC is characterized by absent or lost radioiodine uptake; reviews describe a diagnostic shift to alternative imaging (e.g., FDG PET/CT in RAIR contexts) and exploration of additional tracers, though specific performance statistics were not extractable from the cited excerpts. (tan2024tertpromotermutations pages 9-10)

---

## 11. Outcome / Prognosis

### 11.1 Prognostic biomarkers and statistics
**TERT promoter as major adverse prognostic marker and BRAFV600E synergy:**
- In a 243‑patient DTC NGS cohort, among those with TERTp mutations, **80% (20/25)** had RAIR‑DTC; RAIR‑DTC was **6.3% (9/143)** in BRAFV600E‑only vs **82.4% (14/17)** in BRAFV600E+TERTp. (Tan et al., Scientific Reports, Oct 2024; URL: https://doi.org/10.1038/s41598-024-75087-9). (tan2024tertpromotermutations pages 9-10)

**Stage‑system integration (expert analysis):** BRAFV600E alone did not correlate strongly with ATA/TNM staging and did not significantly predict persistent disease in one 296‑patient study, whereas TERTp (alone or with BRAFV600E) correlated with higher ATA/TNM stages and predicted persistent disease. (Mukhtar et al., Frontiers in Endocrinology, Oct 2023; URL: https://doi.org/10.3389/fendo.2023.1270796). (tan2024tertpromotermutations pages 9-10)

**RAIR prognosis:** Reviews in this run summarize markedly poor outcomes once RAIR develops (e.g., 5‑year OS reported as ~10% in one review excerpt; additional reviews report very poor long‑term survival). (cortas2023tyrosinekinaseinhibitors pages 1-2, tan2024tertpromotermutations pages 9-10)

---

## 12. Treatment

### 12.1 Standard real‑world management in differentiated thyroid cancer
- **Surgery** (thyroidectomy with risk‑adapted lymph node management)
- **Radioiodine (I‑131)** for appropriately selected cases
- **TSH suppression with levothyroxine** as standard adjunctive management
These are referenced as the standard backbone in RAIR‑DTC reviews as the pre‑RAIR state; specific surgical outcome statistics were not extractable from the evidence snippets in this run. (chen2024systemictreatmentsfor pages 1-2)

**MAXO suggestions:**
- Thyroidectomy (MAXO term suggestion: *thyroidectomy*)
- Radioiodine therapy (MAXO suggestion: *radioiodine therapy*)
- Thyroid hormone suppression therapy (MAXO suggestion: *hormone therapy*)

### 12.2 Systemic therapy for RAIR‑DTC (standards and targeted options)
Multiple contemporary reviews agree that for RAIR differentiated thyroid cancer:
- **Lenvatinib** and **sorafenib** are standard first‑line multitargeted TKIs.
- **Cabozantinib** is a standard second‑line option after progression on prior TKI therapy.
(Chen et al., Frontiers in Endocrinology 2024; URL: https://doi.org/10.3389/fendo.2024.1346476) (chen2024systemictreatmentsfor pages 1-2)

A 2023 review similarly states: “Currently, Lenvatinib and Sorafenib…represent the standard first‑line systemic treatment options…while Cabozantinib is the standard second‑line treatment option.” (Cortas & Charalambous, Life 2023; URL: https://doi.org/10.3390/life14010022) (cortas2023tyrosinekinaseinhibitors pages 1-2)

### 12.3 BRAF‑directed therapy and outcomes in BRAF‑mutant RAIR‑DTC
**Anti‑proliferative targeted therapy (not redifferentiation‑specific):**
- **Vemurafenib** in BRAF‑mutant RAIR‑DTC showed objective responses in a phase II experience summarized in a 2023 review: ORR **38.5%** (treatment‑naïve) and **27.3%** (previous VEGFR inhibitor), with toxicity including grade 3–4 AEs (65%) and secondary skin squamous cell carcinoma (27%). (cortas2023tyrosinekinaseinhibitors pages 10-12)
- A randomized phase II comparison of **dabrafenib vs dabrafenib+trametinib** reported ORRs in the ~30–48% range depending on response criteria (modified‑RECIST vs RECIST 1.1). (cortas2023tyrosinekinaseinhibitors pages 10-12)

### 12.4 Redifferentiation therapy (MAPK pathway inhibition to restore RAI uptake)
**Key concept:** Short‑course MAPK pathway inhibition (BRAF±MEK inhibition) can restore NIS function/iodide uptake in some BRAFV600E‑mutant RAIR tumors, enabling “salvage” I‑131 therapy. (cortas2023tyrosinekinaseinhibitors pages 14-15, ovcaricek2024redifferentiationtherapiesin pages 6-7)

**Recent/redifferentiation outcomes highlighted in 2024 review:**
- In a phase II BRAF‑mutant cohort (MERAIODE approach with dabrafenib + trametinib), post‑therapy uptake occurred in **20/21** evaluable patients; at 6 months: **PR 38% (8/21), SD 52% (11/21), PD 10% (2/21)**; PFS **82% at 1 year** and **68% at 2 years**. (Ovčariček et al., J Clin Med, Nov 2024; URL: https://doi.org/10.3390/jcm13237021) (ovcaricek2024redifferentiationtherapiesin pages 6-7)

**Real‑world implementation caution:** A Mayo Clinic retrospective series of 33 RAIR‑DTC patients receiving genotype‑guided inhibitors reported restored RAI uptake in **57.6%** overall, but only **38.9% (7/18)** of BRAF‑mutant tumors redifferentiated versus **100% (11/11)** RAS‑mutant tumors, suggesting BRAF‑mutant follicular‑lineage context and/or deeper dedifferentiation may limit redifferentiation success. (Toro‑Tobon et al., Thyroid, Jan 2024; URL: https://doi.org/10.1089/thy.2023.0456) (jesus2023addonradioiodineduring pages 1-3)

### 12.5 Ongoing and completed clinical trials (ClinicalTrials.gov)
Selected BRAF‑mutant PTC/DTC trials retrieved in this run:
- **NCT01534897 (completed; results posted 2017‑03‑15):** Dabrafenib (GSK2118436) redifferentiation strategy in radioiodine‑refractory BRAF V600E PTC; primary outcome = number of patients with increased RAI uptake after ~25 days of dabrafenib; designed to deliver therapeutic I‑131 if uptake restored. (ClinicalTrials.gov; https://clinicaltrials.gov/study/NCT01534897) (NCT01534897 chunk 1)
- **NCT01286753 (completed):** Vemurafenib in metastatic/unresectable BRAF V600 mutation PTC; clinical publication cited in the record (Brose et al., Lancet Oncology 2016). (https://clinicaltrials.gov/study/NCT01286753) (NCT01286753 chunk 2)
- **NCT04061980 (active/pending in review excerpt):** Encorafenib + binimetinib ± nivolumab in metastatic RAIR BRAF V600 mutant thyroid cancer; phase 2 with ORR primary endpoint. (https://clinicaltrials.gov/study/NCT04061980) (cortas2023tyrosinekinaseinhibitors pages 19-20)
- **NCT06440850 (recruiting; start 2024‑07‑15):** Vemurafenib + cobimetinib as a redifferentiation strategy before initial RAI in high‑risk BRAFV600E‑mutant DTC; primary outcome uses ATA response categories. (https://clinicaltrials.gov/study/NCT06440850) (NCT06440850 chunk 1)

---

## 13. Prevention
No disease‑specific primary prevention strategies exist for sporadic BRAFV600E‑mutant PTC. However, overdiagnosis mitigation (risk‑adapted ultrasound/FNA, refined biopsy criteria, and guideline‑driven management) is supported as a public‑health strategy to reduce unnecessary diagnosis/treatment burden. SEER trend inflection points aligned with ATA revisions support this interpretation. (fwelo2024impactofamerican pages 1-2, fwelo2024impactofamerican pages 2-4)

---

## 14. Other Species / Natural Disease
Natural companion‑animal disease analogs were not retrieved in the evidence excerpts. This report focuses on mechanistic translation using experimental models (see below).

---

## 15. Model Organisms / Model Systems

### 15.1 Mouse models
Authoritative review evidence indicates genetically engineered mouse models (GEMMs) with thyroid‑specific BRAFV600E expression closely phenocopy human PTC histology; in mice, Braf‑driven initiation depends on TSH receptor signaling, and MAPK inhibition can restore differentiation and radioiodine avidity. (Fagin et al., Nat Rev Cancer 2023; URL: https://doi.org/10.1038/s41568-023-00598-y) (fagin2023pathogenesisofcancers pages 24-25)

### 15.2 Murine BRAFV600E PTC cell lines from GEMMs (2023 development)
A 2023 study generated **six novel murine BRAFV600E‑driven PTC cell lines** derived from a **BrafV600E+/−/Pten+/−/TPO‑Cre** model; the lines span varied developmental stages/sexes and show differing differentiation and invasive potential, enabling preclinical therapeutic evaluation and transplantation into immunocompetent hosts. (Branigan et al., Cancers, Jan 2023; URL: https://doi.org/10.3390/cancers15030879) (branigan2023developmentofnovel pages 1-2)

### 15.3 Organoids
A 2024 Oncogene paper created thyroid organoids with inducible **murine BrafV637E** (human‑equivalent of BRAF V600E), reporting that Braf activation triggers MAPK activation and dedifferentiation, and that combining MAPK and PI3K inhibitors reversed dedifferentiation and restored follicle organization/function in vitro. (Lasolle et al., Oncogene, Nov 2024; URL: https://doi.org/10.1038/s41388-023-02889-y). (tan2024tertpromotermutations pages 9-10)

### 15.4 Engineered embryonic stem cell thyroid cancer systems
A Nature Communications 2023 study engineered thyroid progenitor cells with BRAF V600E (or NRAS Q61R) using CRISPR‑Cas9 to generate thyroid cancer histotypes in vitro/in vivo; BRAF V600E in thyroid progenitors generated papillary thyroid carcinoma‑like tumors, supporting a progenitor‑state susceptibility concept. (Veschi et al., Nat Commun, Mar 2023; URL: https://doi.org/10.1038/s41467-023-36922-1). (tan2024tertpromotermutations pages 9-10)

---

## Summary evidence map

| Feature | Evidence/Mechanism | Clinical implication | Key quantitative data (if available) | Key sources (include year, journal, DOI/URL) |
|---|---|---|---|---|
| **BRAFV600E definition** | Canonical activating **BRAF** missense hotspot caused by **c.1799T>A (p.Val600Glu)**; constitutively activates RAF kinase signaling and is the predominant BRAF alteration in PTC. | Defines a major molecular subtype of PTC; supports molecular diagnosis, prognostic contextualization, and eligibility for targeted/redifferentiation strategies. | BRAF mutations occur in **~45%** of PTC overall in one 2024 meta-analysis abstract; broader literature range for PTC **29%–83%**. | Webster 2024, *Head & Neck*, doi:10.1002/hed.27950, https://doi.org/10.1002/hed.27950 (webster2024theprevalenceand pages 2-2) |
| **MAPK pathway activation** | BRAFV600E drives constitutive **MAPK/ERK** signaling (RAS/RAF/MEK/ERK). TCGA-style molecular classification recognizes BRAF-like tumors as high MAPK-output tumors; BRAF is a principal truncal driver in PTC. | Promotes tumor initiation/progression, dedifferentiation, and aggressiveness; provides rationale for **BRAF/MEK inhibitor** therapy and short-course redifferentiation before RAI. | BRAF alterations described as the **single most common driver** in PTC; one review cites **58.5%** prevalence of BRAF alterations in PTC. | Cortas 2023, *Life*, doi:10.3390/life14010022, https://doi.org/10.3390/life14010022 (cortas2023tyrosinekinaseinhibitors pages 2-4); Voinea 2024, review excerpt (voinea2024pathogenesisandmanagement pages 2-4) |
| **NIS downregulation and RAI refractoriness** | High MAPK output from BRAFV600E suppresses thyroid-differentiation genes and impairs **NIS/SLC5A5** expression and/or membrane localization, causing loss of iodine uptake. Aberrant methylation and additional pathway changes can reinforce this state. | Major mechanistic basis for **radioiodine-refractory (RAIR)** disease; supports genotype-guided redifferentiation with MAPK inhibition. | Reviews cite RAIR disease in **5%–15% of DTCs** and **~50% of metastatic DTCs**; another review notes **~60%** of metastatic patients develop RAIR disease over time. | Voinea 2024, review excerpt (voinea2024pathogenesisandmanagement pages 2-4); Chen 2024, *Front Endocrinol*, doi:10.3389/fendo.2024.1346476, https://doi.org/10.3389/fendo.2024.1346476 (chen2024systemictreatmentsfor pages 1-2); de Jesus 2023, *Endocrine*, doi:10.1007/s12020-023-03388-6, https://doi.org/10.1007/s12020-023-03388-6 (jesus2023addonradioiodineduring pages 1-3) |
| **TERT promoter co-mutation synergy with BRAFV600E** | TERT promoter mutation is a strong progression marker; when combined with BRAFV600E it marks a highly aggressive molecular subset with faster dedifferentiation/RAIR conversion and poorer outcomes. | Helps identify patients at higher risk for persistent disease, distant spread, earlier RAIR transition, and worse prognosis; supports broader molecular profiling beyond BRAF alone. | In Tan 2024, among patients with **TERTp mutations**, **80% (20/25)** had RAIR-DTC; RAIR prevalence was **6.3% (9/143)** with **BRAFV600E alone** versus **82.4% (14/17)** with **BRAFV600E + TERTp**. Mukhtar 2023: TERTp present in **37.2%** with persistent disease vs **15.4%** without evidence of disease; BRAFV600E alone did **not** predict persistent disease. | Tan 2024, *Sci Rep*, doi:10.1038/s41598-024-75087-9, https://doi.org/10.1038/s41598-024-75087-9 (tan2024tertpromotermutations pages 9-10); Mukhtar 2023, *Front Endocrinol*, doi:10.3389/fendo.2023.1270796, https://doi.org/10.3389/fendo.2023.1270796 (tan2024tertpromotermutations pages 9-10) |
| **Histologic subtype enrichment** | BRAFV600E is enriched in classic and tall-cell PTC versus follicular-patterned tumors. | Subtype enrichment partly explains why BRAFV600E tracks with aggressive morphology but may not independently predict recurrence once major clinicopathologic factors are accounted for. | Brumfield 2025: **78.7%** overall BRAF p.V600E prevalence (301 cases); **88%** of classic PTC, **38%** of PTC with extensive follicular growth, **100%** of tall-cell subtype were BRAF-positive. | Brumfield 2025, *Endocrine Pathology*, doi:10.1007/s12022-025-09859-y, https://doi.org/10.1007/s12022-025-09859-y (brumfield2025prevalenceandclinical pages 1-2) |
| **Clinicopathologic aggressiveness associations** | Across meta-analytic/review literature, BRAFV600E is linked with adverse features such as **extrathyroidal extension**, advanced stage, lymph-node metastasis, and recurrence; however, effect sizes vary by cohort and covariate adjustment. | BRAF status is best interpreted together with stage, histology, nodal burden, and co-mutations rather than as a stand-alone prognostic biomarker. | Webster 2024 review/meta-analysis excerpt states association with extrathyroidal extension, advanced stage, lymph-node metastasis, and recurrence; Brumfield 2025 found no independent association with recurrence in multivariable analysis (**HR 0.71, 95% CI 0.31–1.65; p=0.4**) and no association with tumor size (**p=0.696**) or nodal burden (**p=0.962**). | Webster 2024, *Head & Neck*, doi:10.1002/hed.27950, https://doi.org/10.1002/hed.27950 (webster2024theprevalenceand pages 2-2); Brumfield 2025, *Endocrine Pathology*, doi:10.1007/s12022-025-09859-y, https://doi.org/10.1007/s12022-025-09859-y (brumfield2025prevalenceandclinical pages 1-2) |
| **Allele frequency / mutation burden within BRAF-positive tumors** | Higher mutant allele fraction may reflect clonality/tumor burden and correlate with aggressive phenotype. | May improve risk stratification among BRAF-positive PTCs beyond binary mutation status. | Abdulhaleem 2023: aggressive-feature nodules had mean BRAF V600E AF **25.8%** vs **10.25%** in non-aggressive group (**p=0.020**); positive sentinel LN **29%** vs negative sentinel LN **17.8%** (**p=0.021**). | Abdulhaleem 2023, *Cancers*, doi:10.3390/cancers16010113, https://doi.org/10.3390/cancers16010113 (derived from retrieved paper context summarized earlier; no context id available, so supporting citation omitted from parenthetical) |
| **RAIR prognosis** | Once dedifferentiation leads to RAIR-DTC, prognosis worsens markedly compared with conventional DTC. | Justifies earlier molecular testing, referral, and consideration of systemic therapy/redifferentiation protocols. | Reviews cited **5-year OS ~10%** after RAIR develops; another review states **mean life expectancy 3–5 years** for RAIR-TC and a **10-year survival <10%** in advanced RAIR-DTC. | Cortas 2023, *Life*, doi:10.3390/life14010022, https://doi.org/10.3390/life14010022 (cortas2023tyrosinekinaseinhibitors pages 1-2); Yu 2023, *Asia Pac J Clin Oncol*, doi:10.1111/ajco.13836, https://doi.org/10.1111/ajco.13836 (yu2023molecularbasisand pages 5-6); Zhao 2024, *Front Endocrinol*, doi:10.3389/fendo.2023.1320044, https://doi.org/10.3389/fendo.2023.1320044 |
| **Redifferentiation with BRAF/MEK inhibition** | Short-course inhibition of BRAFV600E/MAPK can restore NIS expression/iodine uptake in some RAIR tumors, enabling salvage RAI. | Important real-world and trial strategy for BRAFV600E-mutant RAIR PTC/DTC; response is incomplete and likely modified by lineage state and co-alterations. | Dabrafenib restored RAI uptake in **60% (6/10)** BRAF V600E cases; after RAI, **2 PR + 4 SD** at 6 months. MERAIODE BRAF-mutant cohort: uptake in **20/21** evaluable patients; 6-month **PR 38% (8/21)**, **SD 52% (11/21)**, **PD 10% (2/21)**; 1-year PFS **82%**, 2-year PFS **68%**. Mayo retrospective series: only **38.9% (7/18)** of BRAF-mutant tumors redifferentiated versus **100% (11/11)** RAS-mutant tumors. | Cortas 2023, *Life*, doi:10.3390/life14010022, https://doi.org/10.3390/life14010022 (cortas2023tyrosinekinaseinhibitors pages 14-15); Ovčariček 2024, *J Clin Med*, doi:10.3390/jcm13237021, https://doi.org/10.3390/jcm13237021 (ovcaricek2024redifferentiationtherapiesin pages 6-7); Toro-Tobon 2024, *Thyroid*, doi:10.1089/thy.2023.0456, https://doi.org/10.1089/thy.2023.0456 (jesus2023addonradioiodineduring pages 1-3) |
| **Immune suppression axis: TBX3–CXCR2 ligands–MDSCs** | BRAFV600E can foster an immunosuppressive microenvironment through **TBX3** reactivation and **CXCR2-ligand** induction, recruiting **myeloid-derived suppressor cells (MDSCs)**; CXCR2/MDSC targeting improves MAPKi response in models. | Suggests that resistance is not purely cell-intrinsic; supports combined targeted plus immune-microenvironment strategies. | Nature Communications study identified a BRAFV600E–TBX3–CXCLs–MDSCs axis and showed CXCR2 inhibition/MDSC repression improved MAPKi efficacy in advanced thyroid cancer models. | Zhang 2022, *Nat Commun*, doi:10.1038/s41467-022-29000-5, https://doi.org/10.1038/s41467-022-29000-5 (tan2024tertpromotermutations pages 9-10) |
| **Epigenetic/chromatin resistance: SWI/SNF loss** | In BRAF-driven thyroid cancer, loss of SWI/SNF subunits creates a repressive chromatin state with persistent loss of thyroid-lineage transcription/differentiation programs that is not reversed by MAPK blockade. | Mechanistic explanation for failure of redifferentiation despite BRAF/MEK inhibition; argues for multi-omics profiling in refractory disease. | Saqcena 2021 showed BrafV600E-mutant mouse PTCs have reduced lineage TF accessibility and radioiodine incorporation that is rescued by MAPK inhibition, but SWI/SNF loss rendered tumors insensitive to redifferentiation. | Saqcena 2021, *Cancer Discovery*, doi:10.1158/2159-8290.CD-20-0735, https://doi.org/10.1158/2159-8290.CD-20-0735 (tan2024tertpromotermutations pages 9-10) |
| **Actionable biomarker testing context** | Recent consensus guidance recommends systematic somatic biomarker assessment in thyroid cancer because actionable alterations (BRAF, RET, NTRK, others) now guide therapy. | In BRAF-mutant PTC, molecular testing is clinically useful not only diagnostically but also for trial access, targeted therapy selection, and redifferentiation planning. | 2024 consensus statement notes RET and BRAF testing are well established in thyroid cancer care; modern algorithms emphasize multidisciplinary integration. | Mete 2024, *Endocrine Pathology*, doi:10.1007/s12022-024-09836-x, https://doi.org/10.1007/s12022-024-09836-x (tan2024tertpromotermutations pages 9-10) |


*Table: This table summarizes the main molecular mechanisms and clinically relevant associations in BRAF-mutant papillary thyroid carcinoma, including dedifferentiation, radioiodine refractoriness, prognostic modifiers, and resistance biology. It is useful as a compact evidence map for knowledge-base curation and clinical interpretation.*

---

## Notes on evidence gaps
- Direct ontology identifiers (MeSH tree number, ICD‑10/ICD‑11 codes, Orphanet/OMIM entries) and disease‑specific MONDO IDs were not retrievable with the available tools in this run; the closest structured disease IDs obtained were Open Targets EFO IDs for papillary thyroid carcinoma and differentiated thyroid carcinoma. (tan2024tertpromotermutations pages 9-10)
- Detailed symptom frequencies, formal diagnostic criteria, and QoL metrics were not present in the excerpts captured; these typically require guideline PDFs or dedicated clinical cohorts focused on presentation/QoL.


References

1. (webster2024theprevalenceand pages 2-2): Alyssa Webster, Rami M. Elshazli, Dylan Pinion, Robert D. E. Clark, Grace Kelly, Peter P. Issa, Mohammad H. Hussein, Manal S. Fawzy, Eman A. Toraih, and Emad Kandil. The prevalence and prognostic implications of <i>braf</i><scp>k601e</scp> mutations in thyroid neoplasms: a systematic review and meta‐analysis. Head &amp; Neck, 46:3133-3145, Oct 2024. URL: https://doi.org/10.1002/hed.27950, doi:10.1002/hed.27950. This article has 2 citations.

2. (tan2024tertpromotermutations pages 9-10): Gongxun Tan, Bingquan Jin, Xiaoqin Qian, Yuguo Wang, Guoliang Zhang, Enock Adjei Agyekum, Feng Wang, Liang Shi, Yue Zhang, Zhenwei Mao, Chunhe Shi, Ying Xu, Xiuying Li, Lele Zhang, and Shaohua Li. Tert promoter mutations contribute to adverse clinical outcomes and poor prognosis in radioiodine refractory differentiated thyroid cancer. Scientific Reports, Oct 2024. URL: https://doi.org/10.1038/s41598-024-75087-9, doi:10.1038/s41598-024-75087-9. This article has 13 citations and is from a peer-reviewed journal.

3. (abdelmoula2024reviewhistopathologicalmolecularclassifications pages 5-5): NB Abdelmoula and B Abdelmoula. Review histopathological-molecular classifications of papillary thyroid cancers: challenges in genetic practice settings. Unknown journal, 2024.

4. (brumfield2025prevalenceandclinical pages 1-2): Alexandria Brumfield, Sara Abou Azar, Rachel Nordgren, Ronald N. Cohen, David Sarne, Xavier M. Keutgen, Megan Applewhite, Peter Angelos, and Nicole A. Cipriani. Prevalence and clinical impact of braf p.v600e mutation in papillary thyroid carcinoma. Endocrine Pathology, Apr 2025. URL: https://doi.org/10.1007/s12022-025-09859-y, doi:10.1007/s12022-025-09859-y. This article has 10 citations and is from a peer-reviewed journal.

5. (ovcaricek2024redifferentiationtherapiesin pages 6-7): Petra Petranović Ovčariček, Murat Tuncel, Atena Aghaee, Alfredo Campennì, and Luca Giovanella. Redifferentiation therapies in thyroid oncology: molecular and clinical aspects. Journal of Clinical Medicine, 13:7021, Nov 2024. URL: https://doi.org/10.3390/jcm13237021, doi:10.3390/jcm13237021. This article has 8 citations.

6. (NCT01534897 chunk 1): Lori J. Wirth, MD. Re-differentiation of Radioiodine-Refractory BRAF V600E-mutant Papillary Thyroid Carcinoma With GSK2118436. Massachusetts General Hospital. 2012. ClinicalTrials.gov Identifier: NCT01534897

7. (cortas2023tyrosinekinaseinhibitors pages 2-4): Christos Cortas and Haris Charalambous. Tyrosine kinase inhibitors for radioactive iodine refractory differentiated thyroid cancer. Life, 14:22, Dec 2023. URL: https://doi.org/10.3390/life14010022, doi:10.3390/life14010022. This article has 13 citations.

8. (fwelo2024impactofamerican pages 1-2): Pierre Fwelo, Natalia I. Heredia, Ruosha Li, Ayrton Bangolo, Vignesh K. Nagesh, Simcha Weissman, and Xianglin L. Du. Impact of american thyroid association’s revised cancer management guidelines on thyroid cancer incidence trends: a retrospective cohort study, 2000–2020. Journal of Clinical Medicine, 14:28, Dec 2024. URL: https://doi.org/10.3390/jcm14010028, doi:10.3390/jcm14010028. This article has 2 citations.

9. (voinea2024pathogenesisandmanagement pages 2-4): IA Voinea, E Petrova, N Dumitru, and A Cocoloș. Pathogenesis and management strategies in radioiodine-refractory differentiated thyroid cancer: from molecular mechanisms toward therapeutic approaches …. Unknown journal, 2024.

10. (chen2024systemictreatmentsfor pages 1-2): Piaohong Chen, Yu Yao, Huiwen Tan, and Jianwei Li. Systemic treatments for radioiodine-refractory thyroid cancers. Frontiers in Endocrinology, Oct 2024. URL: https://doi.org/10.3389/fendo.2024.1346476, doi:10.3389/fendo.2024.1346476. This article has 15 citations.

11. (cortas2023tyrosinekinaseinhibitors pages 1-2): Christos Cortas and Haris Charalambous. Tyrosine kinase inhibitors for radioactive iodine refractory differentiated thyroid cancer. Life, 14:22, Dec 2023. URL: https://doi.org/10.3390/life14010022, doi:10.3390/life14010022. This article has 13 citations.

12. (branigan2023developmentofnovel pages 1-2): Grace Purvis Branigan, Victoria Casado-Medrano, Alison B. O’Neill, Julio C. Ricarte-Filho, Nicole Massoll, Madeleine Salwen, Zachary Spangler, Michele Scheerer, Edward K. Williamson, Andrew J. Bauer, and Aime T. Franco. Development of novel murine brafv600e-driven papillary thyroid cancer cell lines for modeling of disease progression and preclinical evaluation of therapeutics. Cancers, 15:879, Jan 2023. URL: https://doi.org/10.3390/cancers15030879, doi:10.3390/cancers15030879. This article has 3 citations.

13. (fwelo2024impactofamerican pages 7-8): Pierre Fwelo, Natalia I. Heredia, Ruosha Li, Ayrton Bangolo, Vignesh K. Nagesh, Simcha Weissman, and Xianglin L. Du. Impact of american thyroid association’s revised cancer management guidelines on thyroid cancer incidence trends: a retrospective cohort study, 2000–2020. Journal of Clinical Medicine, 14:28, Dec 2024. URL: https://doi.org/10.3390/jcm14010028, doi:10.3390/jcm14010028. This article has 2 citations.

14. (cortas2023tyrosinekinaseinhibitors pages 10-12): Christos Cortas and Haris Charalambous. Tyrosine kinase inhibitors for radioactive iodine refractory differentiated thyroid cancer. Life, 14:22, Dec 2023. URL: https://doi.org/10.3390/life14010022, doi:10.3390/life14010022. This article has 13 citations.

15. (cortas2023tyrosinekinaseinhibitors pages 14-15): Christos Cortas and Haris Charalambous. Tyrosine kinase inhibitors for radioactive iodine refractory differentiated thyroid cancer. Life, 14:22, Dec 2023. URL: https://doi.org/10.3390/life14010022, doi:10.3390/life14010022. This article has 13 citations.

16. (jesus2023addonradioiodineduring pages 1-3): Filipe Miguel Montes de Jesus, Vittoria Espeli, Gaetano Paone, and Luca Giovanella. Add-on radioiodine during long-term braf/mek inhibition in patients with rai-refractory thyroid cancers: a reasonable option? Endocrine, 81:450-454, May 2023. URL: https://doi.org/10.1007/s12020-023-03388-6, doi:10.1007/s12020-023-03388-6. This article has 6 citations and is from a peer-reviewed journal.

17. (NCT01286753 chunk 2):  A Study of Vemurafenib (RO5185426) in Participants With Metastatic or Unresectable Papillary Thyroid Cancer Positive for the BRAF V600 Mutation. Hoffmann-La Roche. 2011. ClinicalTrials.gov Identifier: NCT01286753

18. (cortas2023tyrosinekinaseinhibitors pages 19-20): Christos Cortas and Haris Charalambous. Tyrosine kinase inhibitors for radioactive iodine refractory differentiated thyroid cancer. Life, 14:22, Dec 2023. URL: https://doi.org/10.3390/life14010022, doi:10.3390/life14010022. This article has 13 citations.

19. (NCT06440850 chunk 1):  Vemurafenib and Cobimetinib for the Treatment of Patients With High Risk Differentiated Thyroid Carcinoma With BRAFV600E Mutation. City of Hope Medical Center. 2024. ClinicalTrials.gov Identifier: NCT06440850

20. (fwelo2024impactofamerican pages 2-4): Pierre Fwelo, Natalia I. Heredia, Ruosha Li, Ayrton Bangolo, Vignesh K. Nagesh, Simcha Weissman, and Xianglin L. Du. Impact of american thyroid association’s revised cancer management guidelines on thyroid cancer incidence trends: a retrospective cohort study, 2000–2020. Journal of Clinical Medicine, 14:28, Dec 2024. URL: https://doi.org/10.3390/jcm14010028, doi:10.3390/jcm14010028. This article has 2 citations.

21. (fagin2023pathogenesisofcancers pages 24-25): James A. Fagin, Gnana P. Krishnamoorthy, and Iñigo Landa. Pathogenesis of cancers derived from thyroid follicular cells. Nature Reviews Cancer, 23:631-650, Jul 2023. URL: https://doi.org/10.1038/s41568-023-00598-y, doi:10.1038/s41568-023-00598-y. This article has 77 citations and is from a domain leading peer-reviewed journal.

22. (yu2023molecularbasisand pages 5-6): Qiuxiao Yu, Xuwen Zhang, Li Li, Chi-zhi Zhang, Jian Huang, and Wenting Huang. Molecular basis and targeted therapies for radioiodine refractory thyroid cancer. Asia‐Pacific Journal of Clinical Oncology, 19:279-289, Aug 2023. URL: https://doi.org/10.1111/ajco.13836, doi:10.1111/ajco.13836. This article has 16 citations.
