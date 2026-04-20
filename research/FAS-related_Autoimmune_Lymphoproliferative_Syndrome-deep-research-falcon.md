---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-16T12:24:54.773318'
end_time: '2026-04-16T12:37:47.669853'
duration_seconds: 772.9
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: FAS-related Autoimmune Lymphoproliferative Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 39
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** FAS-related Autoimmune Lymphoproliferative Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **FAS-related Autoimmune Lymphoproliferative Syndrome** covering all of the
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
- **Disease Name:** FAS-related Autoimmune Lymphoproliferative Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **FAS-related Autoimmune Lymphoproliferative Syndrome** covering all of the
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


# Comprehensive Research Report: FAS-related Autoimmune Lymphoproliferative Syndrome (ALPS-FAS)

## Executive summary
FAS-related autoimmune lymphoproliferative syndrome (ALPS-FAS) is an inborn error of immunity (primary immune regulatory disorder) caused by impaired FAS-mediated apoptosis (extrinsic apoptotic pathway), leading to chronic nonmalignant lymphoproliferation, autoimmune cytopenias, characteristic expansion of TCRαβ+ CD4−CD8− double-negative T cells (DNTs), and elevated risk of lymphoma. Recent (2023–2024) work emphasizes (i) biomarker-driven case finding (especially sFASL with vitamin B12 and DNTs), (ii) practical NGS panel yields in large referral cohorts, and (iii) recognition of complex genetic architectures including somatic “second hits” (e.g., somatic loss of heterozygosity) that can be missed by standard exome sequencing. (rao2024beyondfascinatingadvances pages 1-3, fernandez2024lookingforalps pages 1-2, xu2024genetictestingin pages 1-2)

**Key evidence statistics from recent/major cohorts**
- **NGS panel yield (Cincinnati Children’s, 2014–2023 submissions):** 62/802 (7.7%) definite molecular diagnoses; 52/802 (6.5%) with pathogenic/likely pathogenic **germline FAS** variants; 17/37 (46%) diagnostic FAS variants were novel. Diagnostic yield increased to **30%** among those meeting abnormal ALPS immunology criteria. (xu2024genetictestingin pages 1-2, xu2024genetictestingin pages 4-6)
- **Rapamycin/sirolimus outcomes (28 ALPS-FAS patients):** 79% complete remission and 21% partial remission at 6–9 months; relapse occurred rapidly upon stopping therapy. (klemann2017evolutionofdisease pages 6-10)

## Target disease
- **Disease name:** FAS-related Autoimmune Lymphoproliferative Syndrome
- **Category:** Mendelian (inborn error of immunity / primary immune regulatory disorder)
- **MONDO ID:** Not available from retrieved sources in this run.

---

## 1. Disease information
### 1.1 What is the disease?
ALPS is a rare immune dysregulation disorder characterized by defective FAS signaling and consequent failure of FAS-mediated lymphocyte apoptosis, producing chronic, nonmalignant lymphoproliferation with autoimmunity (often autoimmune cytopenias) and expansion of αβ DNT cells, with increased risk of malignancy (notably lymphoma). (elgharbawy2023casereportneonatal pages 1-2, fernandez2024lookingforalps pages 1-2, rao2024beyondfascinatingadvances pages 1-3)

**Direct abstract quote (definition):** “Autoimmune lymphoproliferative syndrome (ALPS) is a rare primary immune disorder caused by defect of the extrinsic apoptotic pathway.” (Pediatric Allergy and Immunology; May 2024; https://doi.org/10.1111/pai.14135) (fernandez2024lookingforalps pages 1-2)

### 1.2 Key identifiers
Curated disease identifiers were not directly retrievable from OMIM/Orphanet/MeSH/ICD/MONDO within the documents available to this run.

### 1.3 Synonyms / alternative names
- Autoimmune lymphoproliferative syndrome (ALPS) (elgharbawy2023casereportneonatal pages 1-2, fernandez2024lookingforalps pages 1-2)
- ALPS-FAS (germline FAS pathogenic variants) (fernandez2024lookingforalps pages 1-2, xu2024genetictestingin pages 1-2)
- ALPS-sFAS (somatic FAS pathogenic variants) (fernandez2024lookingforalps pages 1-2, rao2024beyondfascinatingadvances pages 1-3)
- “FAS deficiency” / “FAS-pathway apoptosis defect” (rao2011howitreat pages 2-3, rao2024beyondfascinatingadvances pages 1-3)

### 1.4 Evidence sources
Most information summarized here comes from **aggregated disease-level resources** (cohorts, consensus criteria papers, expert reviews) rather than single EHR-derived observations, though illustrative case reports are included for severe biallelic disease and sirolimus response. (price2014naturalhistoryof pages 3-4, klemann2017evolutionofdisease pages 6-10, elgharbawy2023casereportneonatal pages 1-2)

---

## 2. Etiology
### 2.1 Disease causal factors
**Primary cause:** Pathogenic variants affecting the FAS-mediated extrinsic apoptotic pathway, most commonly **FAS** (TNFRSF6) variants that abrogate FAS expression or function, resulting in impaired activation-induced cell death and defective termination of immune responses. (rao2024beyondfascinatingadvances pages 1-3, rieuxlaucat2018theautoimmunelymphoproliferative pages 1-2, casamayorpolo2021immunologicevaluationand pages 3-5)

### 2.2 Risk factors
#### Genetic risk factors
- **Germline FAS variants** (typically autosomal dominant with incomplete penetrance). In the NIH natural history cohort, penetrance among mutation-positive individuals was variable and **sex-dependent** (69% males vs 46% females among mutation carriers reported in the excerpt). (price2014naturalhistoryof pages 3-4)
- **Somatic FAS defects** (ALPS-sFAS) and **second-hit mechanisms** in monoallelic disease, including somatic loss of heterozygosity (sLOH) reported as common in expert synthesis. (rao2024beyondfascinatingadvances pages 1-3)

**Recent diagnostic-yield data:** In a 2024 NGS panel study of 802 referrals, 52/802 (6.5%) had diagnostic germline FAS pathogenic/likely pathogenic variants; 46% of diagnostic FAS variants were novel. (xu2024genetictestingin pages 1-2, xu2024genetictestingin pages 4-6)

#### Environmental/infectious risk factors
No specific environmental toxin/lifestyle risk factors were identified in the retrieved ALPS-FAS sources. Infection risk is clinically relevant as a complication/modifier, especially post-splenectomy, but not a primary etiologic trigger in available evidence. (price2014naturalhistoryof pages 1-3, rieuxlaucat2018theautoimmunelymphoproliferative pages 5-6)

### 2.3 Protective factors
Not specifically identified in the retrieved evidence.

### 2.4 Gene–environment interactions
Not well characterized in the retrieved ALPS-FAS sources; contemporary reviews of inborn errors of immunity emphasize that penetrance/expressivity can reflect multiple factors over time, including somatic events and environmental exposures, but ALPS-FAS-specific quantitative GxE data were not retrieved here. (rao2024beyondfascinatingadvances pages 1-3)

---

## 3. Phenotypes
### 3.1 Core clinical phenotypes (with frequency when available)
Key phenotypes (HPO suggestions in parentheses):
- **Chronic lymphadenopathy** (~96%) (HP:0002716) (rao2011howitreat pages 2-3)
- **Splenomegaly** (~95%) (HP:0001744) (rao2011howitreat pages 2-3)
- **Hepatomegaly** (~72%) (HP:0002240) (rao2011howitreat pages 2-3)
- **Autoimmune cytopenias** (HP:0001871)
  - Autoimmune hemolytic anemia ~29% (HP:0001890) (rao2011howitreat pages 2-3)
  - Immune thrombocytopenia ~23% (HP:0001873) (rao2011howitreat pages 2-3)
  - Neutropenia ~19% (HP:0001875) (rao2011howitreat pages 2-3)
- **Polyclonal hypergammaglobulinemia** (HP:0004315); in NIH cohort, IgG elevated in 58%, IgA in 45%, IgM in 10% (HP:0004313/HP:0004312 patterns) (price2014naturalhistoryof pages 6-7)

Additional lab/immune abnormalities reported in the NIH cohort include DAT positivity (40%), RF positivity (32%), eosinophilia (24%), and elevated monocyte count (38%). (price2014naturalhistoryof pages 6-7)

### 3.2 Age of onset and course
- Usually **early childhood onset**; one review excerpt reports a **median age of onset of ~3 years**. (rieuxlaucat2018theautoimmunelymphoproliferative pages 5-6)
- Rare severe cases can present **neonatally** with biallelic loss-of-function FAS variants. (elgharbawy2023casereportneonatal pages 1-2)
- Disease course is typically **chronic** (>6 months) with fluctuating activity and risk of autoimmune relapses; stopping mTOR inhibition can lead to rapid relapse in treated patients. (klemann2017evolutionofdisease pages 6-10, price2014naturalhistoryof pages 3-4)

### 3.3 Quality of life impact / complications
Formal QoL instruments were not retrieved. Clinically impactful complications include refractory cytopenias requiring immunosuppression, organomegaly, infection risk, and malignancy surveillance burden. Reviews emphasize avoidance of splenectomy when possible due to septicemia risk and loss of anti-polysaccharide responses. (rieuxlaucat2018theautoimmunelymphoproliferative pages 5-6, price2014naturalhistoryof pages 1-3)

---

## 4. Genetic / molecular information
### 4.1 Causal genes
- **FAS (TNFRSF6)** is the principal causal gene for ALPS-FAS. (fernandez2024lookingforalps pages 1-2, xu2024genetictestingin pages 1-2)
- Other extrinsic apoptosis pathway genes associated with ALPS spectrum (not FAS-related subtype specifically) include **FASLG, FADD, CASP10**, though they are much less frequent. (fernandez2024lookingforalps pages 1-2, price2014naturalhistoryof pages 3-4)

### 4.2 Pathogenic variants (classes and examples)
- In a 2024 referral cohort, most diagnostic FAS variants were truncating or missense variants located in the intracellular domain, often the death domain. (xu2024genetictestingin pages 4-6)
- Severe early-onset disease can be caused by **biallelic loss-of-function** variants: e.g., a neonatal case with **FAS exon 9 c.775del leading to p.(Ile259*)**. (elgharbawy2023casereportneonatal pages 1-2)

### 4.3 Germline vs somatic origin
- Germline FAS variants are common; **somatic FAS variants** also occur and may require analysis of sorted DNTs or sensitive sequencing approaches. (rieuxlaucat2018theautoimmunelymphoproliferative pages 7-8, rao2024beyondfascinatingadvances pages 1-3)
- In expert synthesis, **somatic second hits** such as **sLOH** (often via uniparental disomy) are highlighted and can be missed by exome sequencing. (rao2024beyondfascinatingadvances pages 1-3)

### 4.4 Modifier genes and debated genes
A 2024 Cell Death & Disease study challenges the role of common CASP10 variants in ALPS pathogenesis, concluding caspase-10 is dispensable for FAS-mediated apoptosis and CASP10 defects are unlikely to contribute to ALPS when they do not impair apoptosis. (consonni2024studyofthe pages 1-2)

---

## 5. Environmental information
No ALPS-FAS-specific environmental toxin/lifestyle/infectious causal triggers were identified in the retrieved evidence. The key clinically relevant “environmental” dimension is **infectious risk** under immunosuppression and after splenectomy. (rieuxlaucat2018theautoimmunelymphoproliferative pages 5-6, price2014naturalhistoryof pages 1-3)

---

## 6. Mechanism / pathophysiology
### 6.1 Causal chain (from trigger to manifestations)
1. **FAS ligation and signaling failure:** Normally, FAS–FASL interaction triggers receptor trimerization and recruitment of **FADD** and initiator **procaspase-8/10** into the **DISC**, leading to initiator caspase activation and effector caspase cascade. (rieuxlaucat2018theautoimmunelymphoproliferative pages 1-2, casamayorpolo2021immunologicevaluationand pages 3-5)
2. **Defective activation-induced cell death (AICD):** Failure to eliminate activated lymphocytes impairs immune contraction and tolerance. (lambert2021presentationanddiagnosis pages 3-4, casamayorpolo2021immunologicevaluationand pages 3-5)
3. **Accumulation/expansion of DNT cells and autoreactive lymphocytes:** This manifests as lymphadenopathy/splenomegaly and autoimmune cytopenias. (bride2017autoimmunelymphoproliferativesyndrome pages 1-3, rao2011howitreat pages 2-3)
4. **Downstream proliferative signaling:** DNT subsets show evidence of proliferative/survival pathway engagement (mTOR, STAT3), supporting targeted mTOR inhibition as therapy. (lambert2021presentationanddiagnosis pages 3-4, klemann2017evolutionofdisease pages 6-10)

### 6.2 Pathways and processes (ontology suggestions)
- GO: **extrinsic apoptotic signaling pathway** (GO:0097191)
- GO: **activation-induced cell death of T cells** (concept supported; see AICD discussion) (lambert2021presentationanddiagnosis pages 3-4)
- GO: **regulation of lymphocyte apoptosis** / **immune tolerance** (mechanistic basis) (casamayorpolo2021immunologicevaluationand pages 3-5)
- CL: **double negative T cell** (TCRαβ+ CD4−CD8−; pathogenic expansion) (xu2024genetictestingin pages 1-2, price2014naturalhistoryof pages 3-4)

### 6.3 Model organisms / experimental systems
Murine Fas/FasL-deficient models recapitulate key ALPS-like features (lymphoproliferation, autoimmunity, DNT accumulation), including **MRL/lpr** (Fas-deficient) and **MRL/gld** (FasL-deficient) models. (bride2017autoimmunelymphoproliferativesyndrome pages 1-3, rieuxlaucat2018theautoimmunelymphoproliferative pages 1-2)

A 2024 modifier study in **Faslpr** mice (iScience, Nov 2024) shows that altering B-cell apoptosis/activation regulators (EAF2) can modulate lymphoproliferation and nephritis, illustrating potential modifier pathways (Akt/survival genes) in a Fas-deficient background. (luan2024eaf2deficiencyattenuates pages 1-2)

---

## 7. Anatomical structures affected
### 7.1 Organ/system level (UBERON suggestions)
Primary:
- **Spleen** (UBERON:0002106) – splenomegaly/hypersplenism, sequestration cytopenias (rao2011howitreat pages 2-3)
- **Lymph nodes** (UBERON:0000029) – chronic lymphadenopathy (rao2011howitreat pages 2-3)
Secondary/variable:
- **Liver** (UBERON:0002107) – hepatomegaly; occasional liver dysfunction (rao2011howitreat pages 2-3)
- **Bone marrow / hematologic system** – autoimmune cytopenias (rao2011howitreat pages 2-3)

### 7.2 Tissue/cell level (CL suggestions)
- **TCRαβ DNT cells** (CL: T cell subset concept) (xu2024genetictestingin pages 1-2, price2014naturalhistoryof pages 3-4)
- Activated T cells undergoing (failed) AICD; B cell activation/plasma cells in models (luan2024eaf2deficiencyattenuates pages 1-2)

### 7.3 Subcellular level (GO-CC suggestions)
- **Death-inducing signaling complex (DISC)** (complex; DISC discussed mechanistically) (rieuxlaucat2018theautoimmunelymphoproliferative pages 1-2)

---

## 8. Temporal development
- **Onset:** most often pediatric with chronic course; median onset ~3 years in one review excerpt; severe biallelic disease can present neonatally. (rieuxlaucat2018theautoimmunelymphoproliferative pages 5-6, elgharbawy2023casereportneonatal pages 1-2)
- **Progression/course:** chronic lymphoproliferation and episodic/relapsing autoimmune cytopenias; long-term malignancy surveillance required. (price2014naturalhistoryof pages 3-4, rao2011howitreat pages 2-3)

---

## 9. Inheritance and population
### 9.1 Inheritance pattern
- Typical ALPS-FAS: **autosomal dominant** with incomplete penetrance (price2014naturalhistoryof pages 3-4)
- Rare severe biallelic FAS loss-of-function can follow **autosomal recessive** inheritance (as in the neonatal homozygous truncating case report). (elgharbawy2023casereportneonatal pages 1-2)

### 9.2 Penetrance/expressivity
- NIH cohort data indicate **variable penetrance** with sex differences among mutation carriers (69% males vs 46% females in excerpt). (price2014naturalhistoryof pages 3-4)
- 2024 expert review emphasizes somatic second hits (including sLOH) and complex variants that may explain variable expression and diagnostic gaps. (rao2024beyondfascinatingadvances pages 1-3)

### 9.3 Epidemiology (incidence/prevalence)
No population incidence/prevalence estimates were identified in the retrieved sources for this run.

---

## 10. Diagnostics
### 10.1 Standardized diagnostic criteria (NIH 2009 revised)
NIH 2009 revised criteria (as reproduced in the ALPS-FAS natural history study) define:
- **Required criteria:** chronic (>6 months) nonmalignant, noninfectious lymphadenopathy and/or splenomegaly; plus elevated TCRαβ DNT cells (>1.5% of total lymphocytes or >2.5% of CD3+ lymphocytes) with normal/elevated lymphocyte count. (price2014naturalhistoryof pages 3-4)
- **Primary accessory:** defective FAS-induced apoptosis or pathogenic germline/somatic mutation in FAS/FASL/FADD/CASP10. (price2014naturalhistoryof pages 3-4)
- **Secondary accessory:** elevated biomarkers including sFASL (>200 pg/mL), IL-10 (>20 pg/mL), vitamin B12 (>1500 pg/mL), typical histopathology, autoimmune cytopenias, hypergammaglobulinemia, family history. (price2014naturalhistoryof pages 3-4)

**Visual evidence:** Table 1 (cropped) in Price et al. 2014 reproduces these thresholds and criteria components. (price2014naturalhistoryof media e08f037f)

### 10.2 Biomarkers and real-world screening strategies (recent)
A 2024 pediatric study screened 398 patients with autoimmune cytopenia/lymphoproliferation using DNT cells plus sFASL; sFASL correlated strongly with vitamin B12, and sFASL with vitamin B12 were “the most discriminating biomarkers” among confirmed cases in their cohort. (fernandez2024lookingforalps pages 1-2)

### 10.3 Genetic testing approaches
A 15-gene ALPS NGS panel experience (802 cases) showed a 7.7% definite diagnostic yield overall, increasing to 30% when abnormal ALPS immunology criteria were met; it also identified non-FAS ALPID diagnoses (ADA2, CTLA4, KRAS, MAGT1, NRAS) in 1.2%. (xu2024genetictestingin pages 1-2)

### 10.4 Differential diagnosis
Differentials include ALPS-like/autoimmune lymphoproliferative immunodeficiency (ALPID) conditions with overlapping lymphoproliferation and cytopenias, including RAS pathway disorders and CTLA4/LRBA-related immune dysregulation (highlighted in the 2024 NGS panel cohort). (xu2024genetictestingin pages 1-2)

---

## 11. Outcome / prognosis
### 11.1 Morbidity and mortality drivers
In the NIH natural history study, major morbidity/mortality drivers include **overwhelming postsplenectomy sepsis** and development of **lymphoma**; thus, avoiding splenectomy when possible and using steroid-sparing approaches is emphasized. (price2014naturalhistoryof pages 1-3)

### 11.2 Malignancy risk
ALPS-FAS carries increased lymphoma risk; clinical warning features include systemic symptoms and sudden focal lymph node enlargement in established lymphadenopathy. (price2014naturalhistoryof pages 6-7)

No specific numeric lifetime lymphoma incidence was extracted from the retrieved excerpts (the full paper contains SEER O/E analyses but exact values were not captured in the evidence snippets). (price2014naturalhistoryof pages 3-4)

---

## 12. Treatment
### 12.1 Pharmacotherapy (current practice and evidence)
**mTOR inhibition (sirolimus/rapamycin)**
- In a 28-patient ALPS-FAS cohort, rapamycin achieved **complete remission in 79%** and **partial remission in 21%** at 6–9 months; all who stopped relapsed rapidly; biomarker normalization was incomplete in many (e.g., DNT normalized in 33%). (klemann2017evolutionofdisease pages 6-10)
- A 2024 ASH Hematology review notes rapamycin (sirolimus) and mycophenolate mofetil as long-term steroid-sparing measures used successfully over two decades. (rao2024beyondfascinatingadvances pages 1-3)

**Mycophenolate mofetil (MMF)**
Used as a steroid-sparing agent in ALPS management in expert review summaries. (rao2024beyondfascinatingadvances pages 1-3)

**Supportive / avoidance strategies**
Avoid splenectomy when possible due to infection risk; management includes surveillance for malignancy. (rieuxlaucat2018theautoimmunelymphoproliferative pages 5-6, price2014naturalhistoryof pages 1-3)

### 12.2 Real-world implementations (recent case reports)
A 2023 neonatal severe ALPS-FAS case with homozygous truncating FAS variant improved clinically with sirolimus with “obvious reduction” in DNT percentage. (elgharbawy2023casereportneonatal pages 1-2)

### 12.3 Clinical trials (registered)
- **NCT00392951** (CHOP; started Dec 2006; completed Feb 2016; results posted Dec 6, 2017): Phase 1/2 pilot of oral sirolimus for refractory autoimmune cytopenias including ALPS; targeted trough 5–15 ng/mL; primary outcome grade 3–4 toxicities over 6 months; secondary outcomes included CR/PR response and lymphoproliferation response. https://clinicaltrials.gov/study/NCT00392951 (NCT00392951 chunk 1)
- **NCT02579967** (NCI; started Nov 19, 2015; recruiting): Phase 2 allo-BMT trial for primary immunodeficiencies listing “Autoimmune Lymphoproliferative” among conditions; primary endpoint aGVHD-free, graft-failure–free survival at day +180. https://clinicaltrials.gov/study/NCT02579967 (NCT02579967 chunk 1, NCT02579967 chunk 2)

**Emerging targeted therapy direction:** PI3Kδ inhibition is highlighted as a successful paradigm in related IEIs (leniolisib FDA-licensed in 2023 for APDS), and preclinical work supports evaluation in ALPS (NCT06549114 referenced in murine work; not retrievable as a full CT record in this run). (rao2024beyondfascinatingadvances pages 1-3)

### 12.4 MAXO suggestions (treatment/action ontology)
- mTOR inhibitor therapy (sirolimus/rapamycin) (supported by rapamycin cohort and trial) (klemann2017evolutionofdisease pages 6-10, NCT00392951 chunk 1)
- Immunosuppressive therapy (MMF; steroids) (rao2024beyondfascinatingadvances pages 1-3)
- Hematopoietic stem cell transplantation / allo-BMT (for severe PID/immune dysregulation in selected cases) (NCT02579967 chunk 1)

---

## 13. Prevention
Primary prevention is not generally applicable for Mendelian ALPS-FAS beyond reproductive options. Secondary/tertiary prevention includes:
- **Genetic counseling** and cascade testing of relatives; family studies can identify at-risk family members and assist variant classification. (xu2024genetictestingin pages 1-2)
- Avoidance of splenectomy when possible and infection prophylaxis strategies as clinically indicated. (rieuxlaucat2018theautoimmunelymphoproliferative pages 5-6, price2014naturalhistoryof pages 1-3)

---

## 14. Other species / natural disease
No naturally occurring veterinary ALPS-FAS cases were retrieved in obtainable texts in this run.

---

## 15. Model organisms
### 15.1 Core models
- **MRL/lpr** (Fas-deficient) and **MRL/gld** (FasL-deficient) mice recapitulate lymphoproliferation, autoimmunity, DNT expansion, and organ pathology (e.g., glomerulonephritis) relevant to ALPS mechanisms. (bride2017autoimmunelymphoproliferativesyndrome pages 1-3, rieuxlaucat2018theautoimmunelymphoproliferative pages 1-2)

### 15.2 Recent model-organism development (2024)
A 2024 iScience study used Faslpr mice to demonstrate that EAF2 deficiency can attenuate autoimmune disease features by modulating B-cell activation and apoptosis, providing a modifier pathway example in a Fas-deficient background. (luan2024eaf2deficiencyattenuates pages 1-2)

---

## Recent developments (2023–2024 focus) and expert analysis
1. **Biomarker strategy refinement:** A 2024 study argues that existing ALPS criteria are sensitive but have low PPV and supports combined biochemical marker screening, particularly sFASL with vitamin B12 (plus DNTs). (fernandez2024lookingforalps pages 1-2)
2. **Large-scale NGS diagnostic yield:** The 2024 802-patient NGS panel experience quantifies real-world yields and highlights that adding immunology pre-screening increases molecular diagnostic efficiency (30% yield in immunology-abnormal subgroup). (xu2024genetictestingin pages 1-2)
3. **Complex genetics and “missed” variants:** 2024 ASH Hematology review emphasizes that promoter/deep intronic variants, deletions/duplications, and somatic second hits (including sLOH) can be missed by exome sequencing, motivating extended testing strategies. (rao2024beyondfascinatingadvances pages 1-3)

---

## Structured reference table (diagnostics/genetics)
The following table compacts the core naming, NIH criteria, key biomarkers, and genetics for ALPS-FAS.

| Domain | Summary | Key thresholds/details | Supporting citations |
|---|---|---|---|
| Disease name / synonyms | **FAS-related Autoimmune Lymphoproliferative Syndrome**; commonly referred to as **ALPS-FAS** or **autoimmune lymphoproliferative syndrome due to FAS defect/deficiency**. Core disease concept: inborn error of immunity with defective Fas-mediated apoptosis causing chronic nonmalignant lymphoproliferation, autoimmune cytopenias, expanded αβ double-negative T cells, and increased lymphoma risk. | Usually childhood-onset, but presentation can occur at any age. | (rao2024beyondfascinatingadvances pages 1-3, xu2024genetictestingin pages 1-2, fernandez2024lookingforalps pages 1-2) |
| NIH 2009 required criteria | Both are required for ALPS diagnosis framework. | 1) Chronic >6 months, nonmalignant, noninfectious lymphadenopathy and/or splenomegaly. 2) Elevated **CD3+ TCRαβ+ CD4− CD8− DNT cells** with normal/elevated lymphocyte counts: **>1.5% of total lymphocytes or >2.5% of CD3+ lymphocytes**. | (price2014naturalhistoryof pages 3-4, rao2011howitreat pages 2-3) |
| NIH 2009 primary accessory criteria | Supports **definitive** diagnosis when combined with both required criteria. | 1) Defective Fas-mediated apoptosis in 2 separate assays; **or** 2) pathogenic **somatic or germline** mutation in **FAS, FASLG, FADD, or CASP10**. | (price2014naturalhistoryof pages 3-4, rao2011howitreat pages 2-3) |
| NIH 2009 secondary accessory criteria | Supports **probable** diagnosis when combined with both required criteria. | Elevated **sFASL >200 pg/mL**, **IL-10 >20 pg/mL**, **vitamin B12 >1500 pg/mL/ng/L**; typical immunohistopathology; autoimmune cytopenias with elevated IgG/polyclonal hypergammaglobulinemia; family history of nonmalignant/noninfectious lymphoproliferation. IL-18 >500 pg/mL is also noted in later diagnostic summaries. | (price2014naturalhistoryof pages 3-4, rao2011howitreat pages 2-3, fernandez2024lookingforalps pages 1-2) |
| Key biomarker: DNT cells | Hallmark immunophenotypic marker of ALPS-FAS; reflects expansion of apoptosis-resistant αβ T cells and is central to screening/diagnosis. | Often markedly elevated in ALPS-FAS; in one molecularly defined cohort median **7.5%** in ALPS-FAS vs **2.7%** in ALPS-U. Flow panel cutoffs used clinically include **TCRαβ DNT >2% or >68 cells/µL**. | (xu2024genetictestingin pages 1-2, molnar2020keydiagnosticmarkers pages 17-19) |
| Key biomarker: soluble Fas ligand (sFASL) | Indicates Fas-pathway dysregulation; especially useful for predicting **FAS-mutated** disease when paired with apoptosis testing. | NIH threshold **>200 pg/mL**; ALPS-FAS can show very high values, with molecular cohort median **>1000 pg/mL** versus **152 pg/mL** in ALPS-U. | (fernandez2024lookingforalps pages 1-2, molnar2020keydiagnosticmarkers pages 17-19) |
| Key biomarker: IL-10 | Reflects immune activation/lymphoproliferative dysregulation; useful supportive biomarker but less specific than sFASL for FAS-mutant disease. | NIH threshold **>20 pg/mL**. Elevated in ALPS generally; in one comparison it was less discriminatory between ALPS-FAS and ALPS-U than sFASL or apoptosis testing. | (fernandez2024lookingforalps pages 1-2, rao2011howitreat pages 2-3, molnar2020keydiagnosticmarkers pages 17-19) |
| Key biomarker: vitamin B12 | Readily measurable supportive biomarker; often persistently elevated in ALPS-FAS and useful in biomarker-based triage for FAS testing. | NIH threshold **>1500 pg/mL/ng/L**. Price et al. identified elevated vitamin B12 as a reliable biomarker of ALPS-FAS. | (price2014naturalhistoryof pages 3-4, price2014naturalhistoryof pages 1-3, fernandez2024lookingforalps pages 1-2) |
| Genetics summary: germline FAS | Major genetic cause of ALPS. Most diagnosed molecular cases are due to **germline FAS pathogenic/likely pathogenic variants**, often affecting the intracellular death domain; inheritance usually **autosomal dominant with incomplete penetrance**, though recessive severe early-onset cases occur. | In a 2024 cohort of **802** referred patients, **62/802 (7.7%)** had definite molecular diagnoses; **52/62 (84%)** had germline **FAS** variants, including **37 unique variants**, **46% novel**. Penetrance in an NIH natural-history cohort was **<60%** overall; sex difference reported **69% males vs 46% females**. | (xu2024genetictestingin pages 1-2, xu2024genetictestingin pages 4-6, price2014naturalhistoryof pages 1-3, price2014naturalhistoryof pages 3-4) |
| Genetics summary: somatic FAS / ALPS-sFAS | A clinically important subset has **somatic FAS** variants, often enriched in sorted DNT cells, explaining apparently mutation-negative blood testing and delayed diagnosis. | Somatic **FAS** changes reported in about **15–20%** of ALPS patients in recent summaries; testing sorted DNT cells may be required when whole blood is negative or variant allele fraction is low. | (rao2024beyondfascinatingadvances pages 1-3, fernandez2024lookingforalps pages 1-2) |
| Genetics summary: second hits / sLOH | Additional somatic events can worsen penetrance and disease expression in monoallelic FAS disease. | **Somatic loss of heterozygosity (sLOH)**, often due to uniparental disomy duplicating the mutated allele, is reported in roughly **80%** of relevant somatic-event cases in recent expert review summaries. | (rao2024beyondfascinatingadvances pages 1-3) |


*Table: This table compacts the core disease labels, NIH 2009 diagnostic framework, biomarker interpretation, and genetics of FAS-related autoimmune lymphoproliferative syndrome. It is useful as a quick reference for case curation and knowledge-base population.*

---

## Evidence gaps / not available in retrieved sources
- Curated cross-ontology identifiers (OMIM/Orphanet/MeSH/ICD/MONDO) were not directly extractable in this run.
- Population-level prevalence/incidence estimates were not present in retrieved excerpts.
- QoL statistics (EQ-5D/SF-36/PROMIS) were not identified in retrieved ALPS-FAS sources.

---

## Key primary literature and authoritative sources (with dates/URLs)
- Price et al. **Blood** (Mar 2014): Natural history of ALPS-FAS; includes NIH 2009 criteria table and cohort lab frequencies. https://doi.org/10.1182/blood-2013-10-535393 (price2014naturalhistoryof pages 3-4, price2014naturalhistoryof pages 6-7)
- Xu et al. **Journal of Clinical Immunology** (Jul 2024): 802-patient ALPS NGS panel diagnostic yield. https://doi.org/10.1007/s10875-024-01772-z (xu2024genetictestingin pages 1-2)
- Rao et al. **ASH Hematology** (Dec 2024): Expert review on advances in diagnosis/management; emphasizes complex genetics and sLOH. https://doi.org/10.1182/hematology.2024000537 (rao2024beyondfascinatingadvances pages 1-3)
- Fernandez & Touzot **Pediatric Allergy and Immunology** (May 2024): Combined biomarker assessment (DNT+sFASL) in a screened pediatric cohort. https://doi.org/10.1111/pai.14135 (fernandez2024lookingforalps pages 1-2)
- Klemann et al. **Haematologica** (Feb 2017): Rapamycin outcomes and biomarker evolution in 28 ALPS-FAS patients. https://doi.org/10.3324/haematol.2016.153411 (klemann2017evolutionofdisease pages 6-10)
- ClinicalTrials.gov **NCT00392951** (results posted Dec 6, 2017; last update Nov 19, 2019): Sirolimus for autoimmune disease of blood cells including ALPS. https://clinicaltrials.gov/study/NCT00392951 (NCT00392951 chunk 1)


References

1. (rao2024beyondfascinatingadvances pages 1-3): V. Koneti Rao, Stefania Pittaluga, and Gulbu Uzel. Beyond fascinating: advances in diagnosis and management of autoimmune lymphoproliferative syndrome and activated pi3 kinase δ syndrome. Hematology, 2024:126-136, Dec 2024. URL: https://doi.org/10.1182/hematology.2024000537, doi:10.1182/hematology.2024000537. This article has 9 citations and is from a peer-reviewed journal.

2. (fernandez2024lookingforalps pages 1-2): Isabel Fernandez and Fabien Touzot. Looking for alps: the value of a combined assessment of biochemical markers. Pediatric Allergy and Immunology, May 2024. URL: https://doi.org/10.1111/pai.14135, doi:10.1111/pai.14135. This article has 0 citations and is from a domain leading peer-reviewed journal.

3. (xu2024genetictestingin pages 1-2): Xinxiu Xu, James Denton, Yaning Wu, Jie Liu, Qiaoning Guan, D. Brian Dawson, Jack Bleesing, and Wenying Zhang. Genetic testing in patients with autoimmune lymphoproliferative syndrome: experience of 802 patients at cincinnati children’s hospital medical center. Journal of Clinical Immunology, Jul 2024. URL: https://doi.org/10.1007/s10875-024-01772-z, doi:10.1007/s10875-024-01772-z. This article has 4 citations and is from a domain leading peer-reviewed journal.

4. (xu2024genetictestingin pages 4-6): Xinxiu Xu, James Denton, Yaning Wu, Jie Liu, Qiaoning Guan, D. Brian Dawson, Jack Bleesing, and Wenying Zhang. Genetic testing in patients with autoimmune lymphoproliferative syndrome: experience of 802 patients at cincinnati children’s hospital medical center. Journal of Clinical Immunology, Jul 2024. URL: https://doi.org/10.1007/s10875-024-01772-z, doi:10.1007/s10875-024-01772-z. This article has 4 citations and is from a domain leading peer-reviewed journal.

5. (klemann2017evolutionofdisease pages 6-10): Christian Klemann, Myrian Esquivel, Aude Magerus-Chatinet, Myriam R. Lorenz, Ilka Fuchs, Nathalie Neveux, Martin Castelle, Jan Rohr, Claudia Bettoni da Cunha, Martin Ebinger, Robin Kobbe, Bernhard Kremens, Florian Kollert, Eleonora Gambineri, Kai Lehmberg, Markus G. Seidel, Kathrin Siepermann, Thomas Voelker, Volker Schuster, Sigune Goldacker, Klaus Schwarz, Carsten Speckmann, Capucine Picard, Alain Fischer, Frederic Rieux-Laucat, Stephan Ehl, Anne Rensing-Ehl, and Benedicte Neven. Evolution of disease activity and biomarkers on and off rapamycin in 28 patients with autoimmune lymphoproliferative syndrome. Haematologica, 102:e52-e56, Feb 2017. URL: https://doi.org/10.3324/haematol.2016.153411, doi:10.3324/haematol.2016.153411. This article has 68 citations.

6. (elgharbawy2023casereportneonatal pages 1-2): Fawzia M. Elgharbawy, Mohammed Yousuf Karim, Dina Sameh Soliman, Amel Siddik Hassan, Anoop Sudarsanan, and Ashraf Gad. Case report: neonatal autoimmune lymphoproliferative syndrome with a novel pathogenic homozygous fas variant effectively treated with sirolimus. Frontiers in Pediatrics, Apr 2023. URL: https://doi.org/10.3389/fped.2023.1150179, doi:10.3389/fped.2023.1150179. This article has 4 citations.

7. (rao2011howitreat pages 2-3): V. Koneti Rao and João Bosco Oliveira. How i treat autoimmune lymphoproliferative syndrome. Blood, 118 22:5741-51, Nov 2011. URL: https://doi.org/10.1182/blood-2011-07-325217, doi:10.1182/blood-2011-07-325217. This article has 240 citations and is from a highest quality peer-reviewed journal.

8. (price2014naturalhistoryof pages 3-4): Susan Price, Pamela A. Shaw, Amy Seitz, Gyan Joshi, Joie Davis, Julie E. Niemela, Katie Perkins, Ronald L. Hornung, Les Folio, Philip S. Rosenberg, Jennifer M. Puck, Amy P. Hsu, Bernice Lo, Stefania Pittaluga, Elaine S. Jaffe, Thomas A. Fleisher, V. Koneti Rao, and Michael J. Lenardo. Natural history of autoimmune lymphoproliferative syndrome associated with fas gene mutations. Blood, 123 13:1989-99, Mar 2014. URL: https://doi.org/10.1182/blood-2013-10-535393, doi:10.1182/blood-2013-10-535393. This article has 270 citations and is from a highest quality peer-reviewed journal.

9. (rieuxlaucat2018theautoimmunelymphoproliferative pages 1-2): Frédéric Rieux-Laucat, Aude Magérus-Chatinet, and Bénédicte Neven. The autoimmune lymphoproliferative syndrome with defective fas or fas-ligand functions. Journal of Clinical Immunology, 38:558-568, Jun 2018. URL: https://doi.org/10.1007/s10875-018-0523-x, doi:10.1007/s10875-018-0523-x. This article has 100 citations and is from a domain leading peer-reviewed journal.

10. (casamayorpolo2021immunologicevaluationand pages 3-5): Laura Casamayor-Polo, Marta López-Nevado, Estela Paz-Artal, Alberto Anel, Frederic Rieux-Laucat, and Luis M. Allende. Immunologic evaluation and genetic defects of apoptosis in patients with autoimmune lymphoproliferative syndrome (alps). Critical Reviews in Clinical Laboratory Sciences, 58:253-274, Dec 2021. URL: https://doi.org/10.1080/10408363.2020.1855623, doi:10.1080/10408363.2020.1855623. This article has 29 citations and is from a peer-reviewed journal.

11. (price2014naturalhistoryof pages 1-3): Susan Price, Pamela A. Shaw, Amy Seitz, Gyan Joshi, Joie Davis, Julie E. Niemela, Katie Perkins, Ronald L. Hornung, Les Folio, Philip S. Rosenberg, Jennifer M. Puck, Amy P. Hsu, Bernice Lo, Stefania Pittaluga, Elaine S. Jaffe, Thomas A. Fleisher, V. Koneti Rao, and Michael J. Lenardo. Natural history of autoimmune lymphoproliferative syndrome associated with fas gene mutations. Blood, 123 13:1989-99, Mar 2014. URL: https://doi.org/10.1182/blood-2013-10-535393, doi:10.1182/blood-2013-10-535393. This article has 270 citations and is from a highest quality peer-reviewed journal.

12. (rieuxlaucat2018theautoimmunelymphoproliferative pages 5-6): Frédéric Rieux-Laucat, Aude Magérus-Chatinet, and Bénédicte Neven. The autoimmune lymphoproliferative syndrome with defective fas or fas-ligand functions. Journal of Clinical Immunology, 38:558-568, Jun 2018. URL: https://doi.org/10.1007/s10875-018-0523-x, doi:10.1007/s10875-018-0523-x. This article has 100 citations and is from a domain leading peer-reviewed journal.

13. (price2014naturalhistoryof pages 6-7): Susan Price, Pamela A. Shaw, Amy Seitz, Gyan Joshi, Joie Davis, Julie E. Niemela, Katie Perkins, Ronald L. Hornung, Les Folio, Philip S. Rosenberg, Jennifer M. Puck, Amy P. Hsu, Bernice Lo, Stefania Pittaluga, Elaine S. Jaffe, Thomas A. Fleisher, V. Koneti Rao, and Michael J. Lenardo. Natural history of autoimmune lymphoproliferative syndrome associated with fas gene mutations. Blood, 123 13:1989-99, Mar 2014. URL: https://doi.org/10.1182/blood-2013-10-535393, doi:10.1182/blood-2013-10-535393. This article has 270 citations and is from a highest quality peer-reviewed journal.

14. (rieuxlaucat2018theautoimmunelymphoproliferative pages 7-8): Frédéric Rieux-Laucat, Aude Magérus-Chatinet, and Bénédicte Neven. The autoimmune lymphoproliferative syndrome with defective fas or fas-ligand functions. Journal of Clinical Immunology, 38:558-568, Jun 2018. URL: https://doi.org/10.1007/s10875-018-0523-x, doi:10.1007/s10875-018-0523-x. This article has 100 citations and is from a domain leading peer-reviewed journal.

15. (consonni2024studyofthe pages 1-2): Filippo Consonni, Solange Moreno, Blanca Vinuales Colell, Marie-Claude Stolzenberg, Alicia Fernandes, Mélanie Parisot, Cécile Masson, Nathalie Neveux, Jérémie Rosain, Sarah Bamberger, Marie-Gabrielle Vigue, Marion Malphettes, Pierre Quartier, Capucine Picard, Frédéric Rieux-Laucat, and Aude Magerus. Study of the potential role of caspase-10 mutations in the development of autoimmune lymphoproliferative syndrome. Cell Death &amp; Disease, May 2024. URL: https://doi.org/10.1038/s41419-024-06679-6, doi:10.1038/s41419-024-06679-6. This article has 7 citations and is from a peer-reviewed journal.

16. (lambert2021presentationanddiagnosis pages 3-4): Michele P. Lambert. Presentation and diagnosis of autoimmune lymphoproliferative syndrome (alps). Expert Review of Clinical Immunology, 17:1163-1173, Sep 2021. URL: https://doi.org/10.1080/1744666x.2021.1978842, doi:10.1080/1744666x.2021.1978842. This article has 27 citations and is from a peer-reviewed journal.

17. (bride2017autoimmunelymphoproliferativesyndrome pages 1-3): Karen Bride and David Teachey. Autoimmune lymphoproliferative syndrome: more than a fascinating disease. F1000Research, 6:1928, Nov 2017. URL: https://doi.org/10.12688/f1000research.11545.1, doi:10.12688/f1000research.11545.1. This article has 129 citations and is from a peer-reviewed journal.

18. (luan2024eaf2deficiencyattenuates pages 1-2): Yingying Luan, Qing Min, Runyun Zhang, Zichao Wen, Xin Meng, Ziying Hu, Xiaoqian Feng, Meiping Yu, Lulu Dong, and Ji-Yang Wang. Eaf2 deficiency attenuates autoimmune disease in faslpr mice by modulating b cell activation and apoptosis. iScience, 27:111220, Nov 2024. URL: https://doi.org/10.1016/j.isci.2024.111220, doi:10.1016/j.isci.2024.111220. This article has 1 citations and is from a peer-reviewed journal.

19. (price2014naturalhistoryof media e08f037f): Susan Price, Pamela A. Shaw, Amy Seitz, Gyan Joshi, Joie Davis, Julie E. Niemela, Katie Perkins, Ronald L. Hornung, Les Folio, Philip S. Rosenberg, Jennifer M. Puck, Amy P. Hsu, Bernice Lo, Stefania Pittaluga, Elaine S. Jaffe, Thomas A. Fleisher, V. Koneti Rao, and Michael J. Lenardo. Natural history of autoimmune lymphoproliferative syndrome associated with fas gene mutations. Blood, 123 13:1989-99, Mar 2014. URL: https://doi.org/10.1182/blood-2013-10-535393, doi:10.1182/blood-2013-10-535393. This article has 270 citations and is from a highest quality peer-reviewed journal.

20. (NCT00392951 chunk 1):  Sirolimus for Autoimmune Disease of Blood Cells. Children's Hospital of Philadelphia. 2006. ClinicalTrials.gov Identifier: NCT00392951

21. (NCT02579967 chunk 1):  Pilot Trial of Allogeneic Blood or Marrow Transplantation for Primary Immunodeficiencies. National Cancer Institute (NCI). 2015. ClinicalTrials.gov Identifier: NCT02579967

22. (NCT02579967 chunk 2):  Pilot Trial of Allogeneic Blood or Marrow Transplantation for Primary Immunodeficiencies. National Cancer Institute (NCI). 2015. ClinicalTrials.gov Identifier: NCT02579967

23. (molnar2020keydiagnosticmarkers pages 17-19): Emese Molnár, Nesrine Radwan, Gábor Kovács, Hajnalka Andrikovics, Frances Henriquez, Anton Zarafov, Matthew Hayman, Daniela Linzner, Adrian J. Thrasher, Matthew Buckland, Siobhan O. Burns, and Kimberly C. Gilmour. Key diagnostic markers for autoimmune lymphoproliferative syndrome with molecular genetic diagnosis. Blood, 136:1933-1945, Oct 2020. URL: https://doi.org/10.1182/blood.2020005486, doi:10.1182/blood.2020005486. This article has 44 citations and is from a highest quality peer-reviewed journal.
