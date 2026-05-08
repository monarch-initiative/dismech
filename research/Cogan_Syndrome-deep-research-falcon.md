---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-08T13:17:23.900576'
end_time: '2026-05-08T13:25:55.412870'
duration_seconds: 511.51
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Cogan Syndrome
  mondo_id: ''
  category: Autoimmune
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
- **Disease Name:** Cogan Syndrome
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on **Cogan Syndrome** covering all of the
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
- **Disease Name:** Cogan Syndrome
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on **Cogan Syndrome** covering all of the
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


# Cogan Syndrome (Autoimmune/Immune‑mediated Vasculitis) — Disease Characteristics Research Report

## Executive summary
Cogan syndrome (CS) is a rare immune‑mediated disorder classically defined by inflammatory ocular disease (especially non‑syphilitic interstitial keratitis) together with audiovestibular dysfunction (often Ménière‑like episodes and progressive sensorineural hearing loss), with frequent systemic vasculitic involvement that can include potentially life‑threatening aortitis. (wang2023cogan’ssyndromeis pages 1-2, espinoza2020cogan’ssyndromeclinical pages 1-3, tayershifman2014coganssyndrome—clinicalguidelines pages 2-3)

Recent clinically actionable findings include (i) continued emphasis that diagnosis is clinical and by exclusion, with no single confirmatory biomarker; (ii) increasing use of biologics (especially anti‑TNF agents such as infliximab) for steroid‑refractory disease; and (iii) early hearing rehabilitation (cochlear implantation) when profound hearing loss occurs due to risk of intracochlear fibrosis/neo‑ossification. (espinoza2020cogan’ssyndromeclinical pages 4-5, shamriz2018autoimmuneinnerear pages 1-2, rucklova2023paediatriccogan´ssyndrome pages 2-4)


## 1. Disease Information
### 1.1 Overview / definition
**Core concept:** CS is a “variable vessel vasculitis” phenotype with primary involvement of the **eye** and **inner ear**, and with systemic vasculitis in a substantial subset. (ince2023coganssyndrome pages 1-2, tayershifman2014coganssyndrome—clinicalguidelines pages 2-3)

**Typical vs atypical CS (2‑year rule):**
- **Typical CS** is commonly defined by non‑syphilitic interstitial keratitis plus audiovestibular symptoms occurring within **2 years**. (wang2023cogan’ssyndromeis pages 1-2)
- **Atypical CS** includes (a) ocular inflammation other than interstitial keratitis and/or (b) **>2‑year** delay between ocular and audiovestibular manifestations, and is often described as more frequently systemic. (mendes2026atypicalcogan’ssyndrome pages 2-2, mendes2026atypicalcogan’ssyndrome pages 2-3)

**Direct abstract quotes supporting definition:**
- “Cogan’s syndrome (CS) is a rare autoimmune disorder characterized by audiovestibular dysfunction and ocular inflammation.” (Shamriz 2018, published 2018-04-23; https://doi.org/10.1155/2018/1498640) (shamriz2018autoimmuneinnerear pages 1-2)
- “Cogan´s syndrome is a rare, presumed autoimmune vasculitis of various vessels characterized by interstitial keratitis and vestibular impairment accompanied by sensorineural hearing loss.” (Rücklová 2023, published 2023-06; https://doi.org/10.1186/s12969-023-00830-x) (rucklova2023paediatriccogan´ssyndrome pages 2-4)

### 1.2 Key identifiers and controlled vocabulary
**Note:** In the evidence retrieved here, authoritative identifier mappings (e.g., MONDO, Orphanet ORPHA code, ICD‑10/ICD‑11, MeSH) were not directly available as primary sources. Therefore, **IDs are not asserted** in this report.

**Synonyms / alternative names (used in clinical literature):**
- Cogan’s syndrome
- Typical Cogan syndrome
- Atypical Cogan syndrome
- Cogan syndrome with aortitis / systemic vasculitis (wang2023cogan’ssyndromeis pages 1-2, tayershifman2014coganssyndrome—clinicalguidelines pages 2-3)

### 1.3 Evidence sources: individual vs aggregated
Because CS is rare, most treatment and phenotype evidence remains derived from **case reports/series and retrospective cohorts**, including systematic reviews that largely pool case reports. (marrerogonzalez2025audiovestibularoutcomesin pages 1-2, espinoza2020cogan’ssyndromeclinical pages 4-5)


## 2. Etiology
### 2.1 Disease causal factors (current understanding)
**Primary etiology:** CS is widely regarded as **autoimmune/immune‑mediated** with vasculitis as a key pathogenic mechanism. (espinoza2020cogan’ssyndromeclinical pages 1-3, greco2013coganssyndromean pages 2-3)

**Immunologic evidence discussed in authoritative reviews includes:**
- Autoantibodies reported against **corneal antigens**, **inner ear constituents**, and **endothelial antigens**. (Greco 2013; https://doi.org/10.1016/j.autrev.2012.07.012) (greco2013coganssyndromean pages 2-3, greco2013coganssyndromean pages 1-2)
- A proposed “Cogan peptide” with homology to **CD148** (PTPRJ) and **connexin 26** (GJB2), with reports that peptide‑specific antibodies can localize to the cochlea and transfer disease in animal models. (greco2013coganssyndromean pages 2-3)

**Infectious/trigger hypotheses (non‑causal, indirect):** Reviews discuss potential infection‑trigger models (e.g., viral triggers and molecular mimicry concepts), but evidence remains limited and non‑definitive. (tayershifman2014coganssyndrome—clinicalguidelines pages 1-2, tayershifman2014coganssyndrome—clinicalguidelines pages 2-3)

### 2.2 Risk factors
Robust population‑level risk factors are not established; epidemiology is rare and incidence is often described as unknown or not measurable due to the small number of cases. (ince2023coganssyndrome pages 1-2, tayershifman2014coganssyndrome—clinicalguidelines pages 1-2)

### 2.3 Protective factors
No validated protective genetic or environmental factors were identified in the retrieved evidence.

### 2.4 Gene–environment interactions
No validated gene–environment interaction data were identified in the retrieved evidence.


## 3. Phenotypes
### 3.1 Core phenotypic domains
CS phenotypes are commonly grouped as:
1) **Ocular inflammatory disease** (classically interstitial keratitis; also uveitis, episcleritis/scleritis, retinal vasculitis, etc.) (rucklova2023paediatriccogan´ssyndrome pages 2-4, tayershifman2014coganssyndrome—clinicalguidelines pages 2-3)
2) **Audiovestibular disease** (vertigo, tinnitus, nausea/vomiting, ataxia, progressive SNHL) (wang2023cogan’ssyndromeis pages 1-2, espinoza2020cogan’ssyndromeclinical pages 1-3)
3) **Systemic vasculitis / inflammatory manifestations** (fever, arthralgia, anemia, neurologic and gastrointestinal involvement; and aortitis) (wang2023cogan’ssyndromeis pages 1-2, wang2023cogan’ssyndromeis pages 2-5)

### 3.2 Phenotype characteristics with frequency (where available)
**Pediatric case‑based aggregate (n=55; Rücklová 2023):**
- Ocular findings: 55/55 (100%)
- Interstitial keratitis: 34/55 (62%)
- Sensorineural hearing deficit: 55/55 (100%)
- Vestibular symptoms: 37/54 (69%)
- Any systemic symptoms: 32/55 (58%)
- Aortitis: 9/55 (16%); 2/55 deaths reported (mortality 3.6%) (published 2023-06; https://doi.org/10.1186/s12969-023-00830-x) (rucklova2023paediatriccogan´ssyndrome pages 2-4)

**HPO term suggestions (non‑exhaustive):**
- Interstitial keratitis — **HP:0000496** (suggested)
- Uveitis — **HP:0000554** (suggested)
- Scleritis / episcleritis — **HP:0100537 / HP:0200042** (suggested)
- Sensorineural hearing loss — **HP:0000407** (suggested)
- Vertigo — **HP:0002321** (suggested)
- Tinnitus — **HP:0000360** (suggested)
- Aortitis — **HP:0004948** (suggested)
- Fever — **HP:0001945** (suggested)
- Arthralgia — **HP:0002829** (suggested)

### 3.3 Quality of life (QoL) impact
QoL is primarily affected by **permanent or fluctuating hearing loss**, vestibular dysfunction, and visual symptoms. A key clinical consequence emphasized in reviews is progression to **irreversible bilateral profound SNHL** in a substantial fraction of patients, driving cochlear implant candidacy. (shamriz2018autoimmuneinnerear pages 1-2, espinoza2020cogan’ssyndromeclinical pages 4-5)


## 4. Genetic/Molecular Information
### 4.1 Causal genes
No **monogenic causal gene** for CS is established in the retrieved evidence; CS is treated as an immune‑mediated syndrome rather than a Mendelian disorder. (tayershifman2014coganssyndrome—clinicalguidelines pages 1-2, shamriz2018autoimmuneinnerear pages 1-2)

### 4.2 Candidate autoantigens/biomarkers (not diagnostic)
**Key points:** No serum autoantibody is sufficiently validated for routine diagnosis. (shamriz2018autoimmuneinnerear pages 1-2)

- Anti‑HSP70 has been proposed in the context of autoimmune inner ear disease and studied in CS cohorts, with variable positivity across studies and higher positivity reported in typical CS in at least one cohort summarized by Shamriz et al. (2018). (shamriz2018autoimmuneinnerear pages 1-2)
- “Cogan peptide”/cross‑reactive targets (CD148/PTPRJ; connexin 26/GJB2) and endothelial antigen reactivity have been described in reviews. (greco2013coganssyndromean pages 2-3, tayershifman2014coganssyndrome—clinicalguidelines pages 1-2)
- Inflammatory markers (ESR/CRP) are commonly elevated during active disease; IL‑6 can be elevated and has been used as rationale for IL‑6 blockade in case reports/series contexts. (wang2023cogan’ssyndromeis pages 1-2, wang2023cogan’ssyndromeis pages 2-5)

**CHEBI suggestions (where relevant):**
- Prednisone (CHEBI term exists)
- Methylprednisolone (CHEBI term exists)
- Methotrexate (CHEBI term exists)
- Cyclophosphamide (CHEBI term exists)
- Tocilizumab (biologic; CHEBI mapping may exist depending on ontology version)

### 4.3 Epigenetics / chromosomal abnormalities
No CS‑specific epigenetic or chromosomal abnormality evidence was identified in the retrieved sources.


## 5. Environmental Information
No validated environmental toxins, lifestyle factors, or specific infectious agents were established as causal in the retrieved evidence. Reviews discuss infectious trigger hypotheses but without definitive confirmation. (tayershifman2014coganssyndrome—clinicalguidelines pages 1-2, greco2013coganssyndromean pages 1-2)


## 6. Mechanism / Pathophysiology
### 6.1 Mechanistic model (causal chain)
**Proposed upstream trigger(s):** immune activation possibly triggered by infection or other exposures in a susceptible host (hypothesized). (tayershifman2014coganssyndrome—clinicalguidelines pages 1-2)

**Core immune process:** autoimmune/immune‑mediated inflammation with vasculitic injury affecting eye and inner ear; systemic manifestations arise when larger/variable vessels are involved (including the aorta). (greco2013coganssyndromean pages 2-3, tayershifman2014coganssyndrome—clinicalguidelines pages 2-3)

**Downstream tissue injury and clinical manifestations:**
- **Corneal/ocular inflammation** → interstitial keratitis/uveitis/scleritis → pain, photophobia, blurred vision. (tayershifman2014coganssyndrome—clinicalguidelines pages 2-3, rucklova2023paediatriccogan´ssyndrome pages 2-4)
- **Inner ear inflammation/microvascular injury** → cochleovestibular dysfunction → vertigo/tinnitus and progressive SNHL → potential irreversible deafness. (wang2023cogan’ssyndromeis pages 1-2, shamriz2018autoimmuneinnerear pages 1-2)
- **Large vessel vasculitis (aortitis)** → aortic root/valvular dysfunction and vascular complications (aneurysm/stenosis) → morbidity/mortality risk. (wang2023cogan’ssyndromeis pages 1-2, espinoza2020cogan’ssyndromeclinical pages 4-5, tayershifman2014coganssyndrome—clinicalguidelines pages 2-3)

### 6.2 Pathways and cellular processes (ontology suggestions)
**GO Biological Process (suggested):**
- GO:0006954 inflammatory response
- GO:0002682 regulation of immune system process
- GO:0006955 immune response
- GO:0002526 acute inflammatory response
- GO:0006952 defense response
- GO:0050729 positive regulation of inflammatory response

**CL Cell types (suggested, consistent with inflammatory vasculitis):**
- Macrophage — CL:0000235
- T cell — CL:0000084
- B cell / plasma cell — CL:0000236 / CL:0000786
- Vascular endothelial cell — CL:0000115

### 6.3 Molecular profiling (transcriptomics/proteomics/metabolomics)
No validated CS‑specific multi‑omics signatures were identified in the retrieved evidence.


## 7. Anatomical Structures Affected
### 7.1 Organ/system level (primary)
- Eye (cornea; uvea; sclera) (tayershifman2014coganssyndrome—clinicalguidelines pages 2-3, rucklova2023paediatriccogan´ssyndrome pages 2-4)
- Inner ear (cochlea; vestibular apparatus) (shamriz2018autoimmuneinnerear pages 1-2, rucklova2023paediatriccogan´ssyndrome pages 2-4)
- Large vessels, especially aorta (aortitis/aortic root involvement) (wang2023cogan’ssyndromeis pages 1-2, tayershifman2014coganssyndrome—clinicalguidelines pages 2-3)

**UBERON suggestions:**
- Eye — UBERON:0000970
- Cornea — UBERON:0000964
- Inner ear — UBERON:0001845
- Cochlea — UBERON:0001846
- Aorta — UBERON:0000947

### 7.2 Tissue/cell level
Evidence supports inflammatory infiltration and vasculitic pathology in relevant tissues in some reports and reviews, consistent with immune‑mediated injury; definitive cell‑resolved mapping is not standardized. (greco2013coganssyndromean pages 4-4)

### 7.3 Subcellular level
No CS‑specific subcellular compartment pathology was identified.


## 8. Temporal Development
### 8.1 Onset and course
- Often described in **young adults** (20s–30s) but can occur in children and older adults. (wang2023cogan’ssyndromeis pages 1-2, shamriz2018autoimmuneinnerear pages 1-2)
- Course may be **relapsing** and evolve over years; early treatment is emphasized to limit irreversible hearing loss. (espinoza2020cogan’ssyndromeclinical pages 4-5)

**Pediatric timing:** pediatric literature review reports median age **12 years (range 3–18)**. (rucklova2023paediatriccogan´ssyndrome pages 2-4)

### 8.2 Typical vs atypical timing
- The “2‑year” separation is used to operationalize typical vs atypical disease, but some expert commentary suggests the distinction may be less important for long‑term management than prevention of disability and systemic complications. (espinoza2020cogan’ssyndromeclinical pages 4-5)


## 9. Inheritance and Population
### 9.1 Epidemiology
Population prevalence/incidence is not well defined in the retrieved sources.

**Case‑count estimates and age/sex:**
- Reviews describe **~250** reported cases (2018 review) and “few hundred” cases since 1945. (shamriz2018autoimmuneinnerear pages 1-2, wang2023cogan’ssyndromeis pages 2-5)
- One cohort summarized in Shamriz 2018: median onset **25 years (range 5–63)** and no clear gender predominance. (shamriz2018autoimmuneinnerear pages 1-2)
- Pediatric aggregation: male 31/54 (57%). (rucklova2023paediatriccogan´ssyndrome pages 2-4)

### 9.2 Inheritance
No Mendelian inheritance pattern is established; CS is treated as non‑Mendelian/immune‑mediated. (tayershifman2014coganssyndrome—clinicalguidelines pages 1-2, shamriz2018autoimmuneinnerear pages 1-2)


## 10. Diagnostics
### 10.1 Clinical criteria and diagnostic approach
Across reviews, CS diagnosis is **clinical**, requiring:
1) inflammatory ocular disease,
2) audiovestibular involvement (often rapidly progressing SNHL), and
3) **exclusion of alternative causes**, especially syphilis and other infectious/autoimmune mimics. (tayershifman2014coganssyndrome—clinicalguidelines pages 2-3, rucklova2023paediatriccogan´ssyndrome pages 2-4)

**Direct quote (review text):** “To date, since there is no specific test, the diagnosis of CS is based on clinical findings…” (Tayer‑Shifman 2014, published 2014-01; https://doi.org/10.1007/s12016-013-8406-7) (tayershifman2014coganssyndrome—clinicalguidelines pages 2-3)

### 10.2 Laboratory tests and biomarkers
- Inflammatory markers (ESR/CRP) are non‑specific but used to track disease activity. (wang2023cogan’ssyndromeis pages 1-2, rucklova2023paediatriccogan´ssyndrome pages 2-4)
- No single serum autoantibody is accepted for routine diagnostic workup. (shamriz2018autoimmuneinnerear pages 1-2)
- Workup frequently includes broad autoimmune serologies (ANA/ANCA/RF etc.) primarily to evaluate alternative diagnoses; positivity in larger CS studies is generally low per reviews. (shamriz2018autoimmuneinnerear pages 1-2, marrerogonzalez2025audiovestibularoutcomesin pages 2-4)

### 10.3 Imaging and functional testing
- **Audiometry** (pure tone audiogram) for quantification and follow‑up of SNHL. (tayershifman2014coganssyndrome—clinicalguidelines pages 2-3)
- **CT/MRI** head/inner ear to exclude other causes; MRI may show labyrinthitis or other inner ear changes though can be normal. (espinoza2020cogan’ssyndromeclinical pages 1-3, marrerogonzalez2025audiovestibularoutcomesin pages 2-4)
- **Echocardiography is emphasized** for aortitis/aortic valvular dysfunction assessment once CS suspected/diagnosed. (tayershifman2014coganssyndrome—clinicalguidelines pages 2-3, wang2023cogan’ssyndromeis pages 2-5)
- **FDG‑PET/CT** has been used/recommended in selected cases to detect aortitis or inflammatory activity (investigational/adjunct). (espinoza2020cogan’ssyndromeclinical pages 4-5, tayershifman2014coganssyndrome—clinicalguidelines pages 2-3)

### 10.4 Differential diagnosis (examples from pediatric diagnostic table)
Important exclusions include **syphilis**, tuberculosis, chlamydia, sarcoidosis, PAN, ANCA‑associated vasculitides, Behçet disease, Takayasu arteritis, Vogt‑Koyanagi‑Harada syndrome, Susac syndrome, and connective tissue disorders. (rucklova2023paediatriccogan´ssyndrome pages 2-4)

### 10.5 Genetic testing
Genetic testing is not a standard diagnostic tool for CS based on the retrieved evidence (no established causal gene). (tayershifman2014coganssyndrome—clinicalguidelines pages 1-2)


## 11. Outcome / Prognosis
### 11.1 Hearing and visual outcomes
- Hearing loss may progress to irreversible bilateral profound SNHL in **approximately half** of patients in at least one review. (shamriz2018autoimmuneinnerear pages 1-2)
- A 2023 literature review states “Nearly **43%** develop deafness” and “blindness has been reported in **8%**.” (Wang 2023, published 2023-05; https://doi.org/10.1186/s12886-023-02966-6) (wang2023cogan’ssyndromeis pages 1-2)

### 11.2 Systemic vasculitis complications
Systemic involvement is common in some series/reviews (often cited up to ~80%), with aortitis around ~10% in multiple reviews and higher rates in pediatric aggregation. (espinoza2020cogan’ssyndromeclinical pages 1-3, tayershifman2014coganssyndrome—clinicalguidelines pages 2-3, rucklova2023paediatriccogan´ssyndrome pages 2-4)


## 12. Treatment
### 12.1 Pharmacotherapy (current standard and escalation)
**First‑line:** high‑dose systemic corticosteroids for acute/active disease, with topical ocular steroids for mild ocular disease. (espinoza2020cogan’ssyndromeclinical pages 4-5, tayershifman2014coganssyndrome—clinicalguidelines pages 2-3)

**Timing matters for hearing:** high‑dose steroids given within **~2 weeks** of auditory symptom onset improve odds of hearing recovery. (espinoza2020cogan’ssyndromeclinical pages 4-5)

**Steroid‑sparing csDMARDs (examples):** methotrexate, azathioprine, cyclosporine, mycophenolate mofetil; cyclophosphamide for severe systemic vasculitis. (mendes2026atypicalcogan’ssyndrome pages 2-3, tayershifman2014coganssyndrome—clinicalguidelines pages 2-3, marrerogonzalez2025audiovestibularoutcomesin pages 2-4)

**Biologics (refractory disease):** anti‑TNF agents are most frequently emphasized; infliximab is highlighted as a leading option in multiple reviews. (espinoza2020cogan’ssyndromeclinical pages 4-5, tayershifman2014coganssyndrome—clinicalguidelines pages 1-2)

**Quantitative outcomes from treatment literature (selected):**
- Infliximab: **80% response rate at 6 months** for vestibuloauditory symptoms in a treatment review summary. (Espinoza 2020, published 2020-06; https://doi.org/10.1007/s11882-020-00945-1) (espinoza2020cogan’ssyndromeclinical pages 4-5)
- Adult systematic review of case reports (n=79): **60%** treated only with oral steroids had no audiologic improvement, while **85.7%** treated with biologic DMARDs improved audiologically. (Marrero‑Gonzalez 2025; https://doi.org/10.1007/s00405-024-08878-5) (marrerogonzalez2025audiovestibularoutcomesin pages 1-2)

**Newer/experimental approaches noted in recent reports:**
- IL‑6 blockade (tocilizumab) used in refractory cases; elevated IL‑6 reported in some cases and normalization of inflammatory markers after tocilizumab reported in case‑based narratives. (wang2023cogan’ssyndromeis pages 2-5)
- JAK inhibitors (e.g., tofacitinib) used in selected refractory cases for systemic/joint manifestations (hearing stabilization variable). (wang2023cogan’ssyndromeis pages 1-2)

### 12.2 Surgical and interventional
**Cochlear implantation (CI):**
- CI is recommended early in profound SNHL because inflammatory inner ear disease can cause intracochlear fibrosis/neo‑ossification, complicating later implantation. (shamriz2018autoimmuneinnerear pages 1-2)
- Pediatric case‑based report describes evaluation for unilateral CI after one ear remained deaf despite immunomodulatory therapy; MRI resolution of inflammation raised concern for intracochlear fibrosis, “emphasiz[ing] the urgency of CI.” (rucklova2023paediatriccogan´ssyndrome pages 2-4)

### 12.3 MAXO term suggestions (selected)
- Systemic glucocorticoid therapy — MAXO term exists (suggested)
- Immunosuppressive therapy — MAXO term exists (suggested)
- Tumor necrosis factor inhibitor therapy — MAXO term exists (suggested)
- Cochlear implantation — MAXO term exists (suggested)
- Echocardiography (for surveillance) — MAXO term exists (suggested)

### 12.4 Clinical trials
No CS‑specific interventional trials were identified in the retrieved ClinicalTrials.gov search results; current evidence base is dominated by observational data, case series, and case reports. (Evidence state: no relevant clinical trials retrieved)


## 13. Prevention
No established primary prevention strategy exists. Practical prevention is largely **tertiary prevention**: early recognition and immunosuppression to prevent irreversible SNHL and monitoring for aortitis/vascular complications. (espinoza2020cogan’ssyndromeclinical pages 4-5, tayershifman2014coganssyndrome—clinicalguidelines pages 2-3)


## 14. Other Species / Natural Disease
No naturally occurring CS equivalent in non‑human species was identified in the retrieved evidence.


## 15. Model Organisms
No standardized model organism resource or widely used experimental model for CS was identified in the retrieved evidence; however, immune reactivity to candidate antigens (“Cogan peptide”) and disease transfer/induction has been discussed in reviews, implying experimental work exists but is not established as a canonical model system. (greco2013coganssyndromean pages 2-3)


## Key quantitative/clinical facts table
| Data point | Value | Population/Study | Year | Source (first author) | DOI/URL | Citation context IDs |
|---|---:|---|---:|---|---|---|
| Typical Cogan syndrome definition | Ocular and audiovestibular symptoms occur within **2 years**; classically non-syphilitic interstitial keratitis plus Ménière-like audiovestibular disease | Clinical definition/review | 2023 | Wang | https://doi.org/10.1186/s12886-023-02966-6 | (wang2023cogan’ssyndromeis pages 1-2, espinoza2020cogan’ssyndromeclinical pages 1-3) |
| Atypical Cogan syndrome definition | Delay **>2 years** between ocular and audiovestibular manifestations and/or non-interstitial-keratitis ocular inflammation; systemic manifestations more frequent | Clinical definition/review | 2026 | Mendes | https://doi.org/10.1159/000551227 | (mendes2026atypicalcogan’ssyndrome pages 2-2, mendes2026atypicalcogan’ssyndrome pages 2-3) |
| Interstitial keratitis frequency | **34/55 (62%)** | Pediatric literature review cohort, n=55 | 2023 | Rücklová | https://doi.org/10.1186/s12969-023-00830-x | (rucklova2023paediatriccogan´ssyndrome pages 2-4) |
| Vestibular symptoms frequency | **37/54 (69%)** | Pediatric literature review cohort, n=55 | 2023 | Rücklová | https://doi.org/10.1186/s12969-023-00830-x | (rucklova2023paediatriccogan´ssyndrome pages 2-4) |
| Any systemic symptoms | **32/55 (58%)** | Pediatric literature review cohort, n=55 | 2023 | Rücklová | https://doi.org/10.1186/s12969-023-00830-x | (rucklova2023paediatriccogan´ssyndrome pages 2-4) |
| Aortitis frequency | **9/55 (16%)** | Pediatric literature review cohort, n=55 | 2023 | Rücklová | https://doi.org/10.1186/s12969-023-00830-x | (rucklova2023paediatriccogan´ssyndrome pages 2-4) |
| Mortality | **2/55 (3.6%)** | Pediatric literature review cohort, n=55 | 2023 | Rücklová | https://doi.org/10.1186/s12969-023-00830-x | (rucklova2023paediatriccogan´ssyndrome pages 2-4) |
| Biologic DMARD audiologic improvement | **12/14 (85.7%)** improved | Adult systematic review/case reports, n=79 total | 2025 | Marrero-Gonzalez | https://doi.org/10.1007/s00405-024-08878-5 | (marrerogonzalez2025audiovestibularoutcomesin pages 1-2, marrerogonzalez2025audiovestibularoutcomesin pages 2-4) |
| Oral steroids only: no audiologic improvement | **18/30 (60.0%)** had no improvement | Adult systematic review/case reports, n=79 total | 2025 | Marrero-Gonzalez | https://doi.org/10.1007/s00405-024-08878-5 | (marrerogonzalez2025audiovestibularoutcomesin pages 1-2) |
| Vestibular symptoms in steroid-resistant vs steroid-responsive patients | **79.5% vs 57.9%** | Adult systematic review/case reports, n=79 total | 2025 | Marrero-Gonzalez | https://doi.org/10.1007/s00405-024-08878-5 | (marrerogonzalez2025audiovestibularoutcomesin pages 1-2) |
| Deafness frequency | **~43%** develop deafness | Clinical review/literature review | 2023 | Wang | https://doi.org/10.1186/s12886-023-02966-6 | (wang2023cogan’ssyndromeis pages 1-2) |
| Blindness frequency | **8%** | Clinical review/literature review | 2023 | Wang | https://doi.org/10.1186/s12886-023-02966-6 | (wang2023cogan’ssyndromeis pages 1-2) |
| Infliximab vestibuloauditory response | **80% response at 6 months** | Review of treatment evidence | 2020 | Espinoza | https://doi.org/10.1007/s11882-020-00945-1 | (espinoza2020cogan’ssyndromeclinical pages 4-5) |
| Ocular response to steroids | **84%** | French series/review summarized in treatment review | 2020 | Espinoza | https://doi.org/10.1007/s11882-020-00945-1 | (espinoza2020cogan’ssyndromeclinical pages 4-5) |
| Ocular response to DMARDs | **90%** | French series/review summarized in treatment review | 2020 | Espinoza | https://doi.org/10.1007/s11882-020-00945-1 | (espinoza2020cogan’ssyndromeclinical pages 4-5) |
| Ocular response to biologics | **100%** | French series/review summarized in treatment review | 2020 | Espinoza | https://doi.org/10.1007/s11882-020-00945-1 | (espinoza2020cogan’ssyndromeclinical pages 4-5) |
| Hearing progression to irreversible bilateral profound SNHL | **Approximately half of patients** | Immunology review | 2018 | Shamriz | https://doi.org/10.1155/2018/1498640 | (shamriz2018autoimmuneinnerear pages 1-2) |


*Table: This table compiles the most actionable quantitative and definitional findings for Cogan syndrome from the retrieved evidence. It highlights diagnostic distinctions, pediatric and adult cohort statistics, and treatment/outcome figures useful for rapid knowledge-base entry.*


## Expert opinion / authoritative analysis (synthesis)
1) **Diagnosis remains syndromic and exclusionary**: multiple authoritative reviews emphasize there is *no specific diagnostic test*, and evaluation must exclude infections (syphilis, TB) and systemic inflammatory mimics while assessing for vasculitis (including echocardiographic screening for aortitis). (tayershifman2014coganssyndrome—clinicalguidelines pages 2-3, rucklova2023paediatriccogan´ssyndrome pages 2-4)
2) **Early immunosuppression is time‑critical for hearing**: steroid treatment in the first ~2 weeks of auditory symptom onset is repeatedly highlighted as improving hearing recovery odds, but many patients still progress to profound SNHL. (espinoza2020cogan’ssyndromeclinical pages 4-5, shamriz2018autoimmuneinnerear pages 1-2)
3) **Biologic therapy is increasingly used in refractory disease**: anti‑TNF therapy (especially infliximab) is the most consistently emphasized biologic across reviews, with aggregated evidence suggesting improved vestibuloauditory outcomes compared with steroids alone in case‑based evidence. (espinoza2020cogan’ssyndromeclinical pages 4-5, marrerogonzalez2025audiovestibularoutcomesin pages 1-2)


## Limitations of this report
- Authoritative disease identifier mappings (MONDO/Orphanet/ICD/MeSH) were not retrievable from the provided evidence set, so identifiers are not asserted.
- Many “latest developments” in 2023–2024 are case‑based; high‑quality randomized trials remain scarce or absent in the retrieved evidence, limiting certainty for comparative efficacy claims.


References

1. (wang2023cogan’ssyndromeis pages 1-2): Yanqing Wang, Shichao Tang, Chong Shao, and Yu Liu. Cogan’s syndrome is more than just keratitis: a case-based literature review. BMC Ophthalmology, May 2023. URL: https://doi.org/10.1186/s12886-023-02966-6, doi:10.1186/s12886-023-02966-6. This article has 12 citations and is from a peer-reviewed journal.

2. (espinoza2020cogan’ssyndromeclinical pages 1-3): Gabriela Mabel Espinoza, Joseph Wheeler, Katherine K. Temprano, and Angela Prost Keller. Cogan’s syndrome: clinical presentations and update on treatment. Current Allergy and Asthma Reports, 20:1-6, Jun 2020. URL: https://doi.org/10.1007/s11882-020-00945-1, doi:10.1007/s11882-020-00945-1. This article has 69 citations and is from a peer-reviewed journal.

3. (tayershifman2014coganssyndrome—clinicalguidelines pages 2-3): Oshrat E. Tayer-Shifman, Ophir Ilan, Hodaya Tovi, and Yuval Tal. Cogan's syndrome—clinical guidelines and novel therapeutic approaches. Clinical Reviews in Allergy & Immunology, 47:65-72, Jan 2014. URL: https://doi.org/10.1007/s12016-013-8406-7, doi:10.1007/s12016-013-8406-7. This article has 73 citations and is from a peer-reviewed journal.

4. (espinoza2020cogan’ssyndromeclinical pages 4-5): Gabriela Mabel Espinoza, Joseph Wheeler, Katherine K. Temprano, and Angela Prost Keller. Cogan’s syndrome: clinical presentations and update on treatment. Current Allergy and Asthma Reports, 20:1-6, Jun 2020. URL: https://doi.org/10.1007/s11882-020-00945-1, doi:10.1007/s11882-020-00945-1. This article has 69 citations and is from a peer-reviewed journal.

5. (shamriz2018autoimmuneinnerear pages 1-2): Oded Shamriz, Yuval Tal, and Menachem Gross. Autoimmune inner ear disease: immune biomarkers, audiovestibular aspects, and therapeutic modalities of cogan's syndrome. Journal of Immunology Research, 2018:1-8, Apr 2018. URL: https://doi.org/10.1155/2018/1498640, doi:10.1155/2018/1498640. This article has 52 citations and is from a peer-reviewed journal.

6. (rucklova2023paediatriccogan´ssyndrome pages 2-4): Kristina Rücklová, Thekla von Kalle, Assen Koitschev, Katrin Gekeler, Miriam Scheltdorf, Anita Heinkele, Friederike Blankenburg, Ina Kötter, and Anton Hospach. Paediatric cogan´s syndrome - review of literature, case report and practical approach to diagnosis and management. Pediatric Rheumatology Online Journal, Jun 2023. URL: https://doi.org/10.1186/s12969-023-00830-x, doi:10.1186/s12969-023-00830-x. This article has 7 citations.

7. (ince2023coganssyndrome pages 1-2): B İnce and S Kamalı. Cogan's syndrome. Unknown journal, 2023.

8. (mendes2026atypicalcogan’ssyndrome pages 2-2): João Mendes, Francisco Mendes, Diogo Valente Fortunato, João Vasco Garrido, Rita Condesso, and Augusto Candeias. Atypical cogan’s syndrome presenting as anterior scleritis: case report. Case Reports in Ophthalmology, 17:371-379, Mar 2026. URL: https://doi.org/10.1159/000551227, doi:10.1159/000551227. This article has 0 citations and is from a peer-reviewed journal.

9. (mendes2026atypicalcogan’ssyndrome pages 2-3): João Mendes, Francisco Mendes, Diogo Valente Fortunato, João Vasco Garrido, Rita Condesso, and Augusto Candeias. Atypical cogan’s syndrome presenting as anterior scleritis: case report. Case Reports in Ophthalmology, 17:371-379, Mar 2026. URL: https://doi.org/10.1159/000551227, doi:10.1159/000551227. This article has 0 citations and is from a peer-reviewed journal.

10. (marrerogonzalez2025audiovestibularoutcomesin pages 1-2): Alejandro R. Marrero-Gonzalez, Celine Ward, Shaun A. Nguyen, Seth S. Jeong, and Habib G. Rizk. Audiovestibular outcomes in adult patients with cogan syndrome: a systematic review. European Archives of Oto-Rhino-Laryngology, 282:23-35, Aug 2025. URL: https://doi.org/10.1007/s00405-024-08878-5, doi:10.1007/s00405-024-08878-5. This article has 6 citations and is from a peer-reviewed journal.

11. (greco2013coganssyndromean pages 2-3): A. Greco, A. Gallo, M. Fusconi, G. Magliulo, R. Turchetta, C. Marinelli, G.F. Macri, A. De Virgilio, and M. de Vincentiis. Cogan's syndrome: an autoimmune inner ear disease. Autoimmunity reviews, 12 3:396-400, Jan 2013. URL: https://doi.org/10.1016/j.autrev.2012.07.012, doi:10.1016/j.autrev.2012.07.012. This article has 160 citations and is from a peer-reviewed journal.

12. (greco2013coganssyndromean pages 1-2): A. Greco, A. Gallo, M. Fusconi, G. Magliulo, R. Turchetta, C. Marinelli, G.F. Macri, A. De Virgilio, and M. de Vincentiis. Cogan's syndrome: an autoimmune inner ear disease. Autoimmunity reviews, 12 3:396-400, Jan 2013. URL: https://doi.org/10.1016/j.autrev.2012.07.012, doi:10.1016/j.autrev.2012.07.012. This article has 160 citations and is from a peer-reviewed journal.

13. (tayershifman2014coganssyndrome—clinicalguidelines pages 1-2): Oshrat E. Tayer-Shifman, Ophir Ilan, Hodaya Tovi, and Yuval Tal. Cogan's syndrome—clinical guidelines and novel therapeutic approaches. Clinical Reviews in Allergy & Immunology, 47:65-72, Jan 2014. URL: https://doi.org/10.1007/s12016-013-8406-7, doi:10.1007/s12016-013-8406-7. This article has 73 citations and is from a peer-reviewed journal.

14. (wang2023cogan’ssyndromeis pages 2-5): Yanqing Wang, Shichao Tang, Chong Shao, and Yu Liu. Cogan’s syndrome is more than just keratitis: a case-based literature review. BMC Ophthalmology, May 2023. URL: https://doi.org/10.1186/s12886-023-02966-6, doi:10.1186/s12886-023-02966-6. This article has 12 citations and is from a peer-reviewed journal.

15. (greco2013coganssyndromean pages 4-4): A. Greco, A. Gallo, M. Fusconi, G. Magliulo, R. Turchetta, C. Marinelli, G.F. Macri, A. De Virgilio, and M. de Vincentiis. Cogan's syndrome: an autoimmune inner ear disease. Autoimmunity reviews, 12 3:396-400, Jan 2013. URL: https://doi.org/10.1016/j.autrev.2012.07.012, doi:10.1016/j.autrev.2012.07.012. This article has 160 citations and is from a peer-reviewed journal.

16. (marrerogonzalez2025audiovestibularoutcomesin pages 2-4): Alejandro R. Marrero-Gonzalez, Celine Ward, Shaun A. Nguyen, Seth S. Jeong, and Habib G. Rizk. Audiovestibular outcomes in adult patients with cogan syndrome: a systematic review. European Archives of Oto-Rhino-Laryngology, 282:23-35, Aug 2025. URL: https://doi.org/10.1007/s00405-024-08878-5, doi:10.1007/s00405-024-08878-5. This article has 6 citations and is from a peer-reviewed journal.
