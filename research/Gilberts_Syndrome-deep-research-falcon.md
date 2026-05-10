---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-09T08:48:34.405643'
end_time: '2026-05-09T09:05:32.387438'
duration_seconds: 1017.98
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Gilbert's Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 20
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Gilbert's Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Gilbert's Syndrome** covering all of the
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
- **Disease Name:** Gilbert's Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Gilbert's Syndrome** covering all of the
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


# Gilbert’s Syndrome (GS): Disease Characteristics Research Report

## Target disease
- **Disease name:** Gilbert’s syndrome (GS)
- **Category:** Mendelian (UGT1A1-related bilirubin conjugation deficiency)

---

## 1. Disease Information

### 1.1 Concise overview (current understanding)
Gilbert’s syndrome is a common, generally benign inherited condition characterized by **intermittent, non-hemolytic, predominantly unconjugated hyperbilirubinemia** in the setting of otherwise normal liver biochemistry and no evidence of hemolysis. Typical total bilirubin values are mild (often in the ~1.2–5.3 mg/dL range) and may fluctuate with physiologic stressors. (gonzaleziglesias2024geneticvariationin pages 1-2, beutler2024gilbertssyndromebrightand pages 1-4)

### 1.2 Key identifiers and terminology
- **OMIM disease:** **Gilbert syndrome (OMIM #143500)** is explicitly referenced in multiple papers in the retrieved corpus. (yao2023geneticvariationsunderlying pages 1-2)
- **Causal gene OMIM:** **UGT1A1 (OMIM *191740)**, located on **chromosome 2q37**, is repeatedly cited as the causal gene for GS-spectrum unconjugated hyperbilirubinemia. (yao2023geneticvariationsunderlying pages 1-2, gonzaleziglesias2024geneticvariationin pages 1-2)
- **OpenTargets / EFO:** OpenTargets returns an association between **Gilbert syndrome (EFO_0005556)** and **UGT1A1** (and also UGT1A10 in a smaller evidence set), with literature-linked evidence. (OpenTargets Search: Gilbert syndrome-UGT1A1)
- **MONDO:** In OpenTargets, a related entity **hereditary hyperbilirubinemia** maps to **MONDO_0002408** and is also associated with UGT1A1. A distinct MONDO identifier for “Gilbert syndrome” itself was not obtained from the retrieved sources in this run. (OpenTargets Search: Gilbert syndrome-UGT1A1)
- **ICD-10/ICD-11, MeSH, Orphanet:** These identifiers were not directly captured from the retrieved full-text chunks; therefore they cannot be reported with primary-source citations here.

### 1.3 Synonyms / alternative names (from clinical usage)
In the retrieved literature, the disease is referred to as **Gilbert syndrome** and **Gilbert’s syndrome**. (beutler2024gilbertssyndromebrightand pages 1-4, yao2023geneticvariationsunderlying pages 1-2)

### 1.4 Evidence provenance
Evidence summarized below is derived from a mixture of:
- **Primary human studies** (e.g., infant prolonged jaundice cohort; HBV outcome association; healthy volunteer genotype-biochemistry study) (yao2023geneticvariationsunderlying pages 1-2, kim2024shouldweconsider pages 1-2, gonzaleziglesias2024geneticvariationin pages 1-2)
- **Systematic review** of clinical trials related to nutrition/fasting effects in GS (goluch2024nutritioningilbert’s pages 1-2, goluch2024nutritioningilbert’s media eb15b11f)
- **ClinicalTrials.gov records** for UGT1A1 pharmacogenomics studies (NCT05148767 chunk 1, NCT01523431 chunk 1, NCT02680795 chunk 1)

---

## 2. Etiology

### 2.1 Disease causal factors
**Primary cause:** inherited reduction of **UGT1A1** activity/expression, the key UDP-glucuronosyltransferase responsible for bilirubin glucuronidation in humans. (yao2023geneticvariationsunderlying pages 1-2, goluch2024nutritioningilbert’s pages 1-2)

**Key causal/associated variants (current consensus in retrieved sources):**
- **UGT1A1*28 promoter TA-repeat expansion** (TATA-box; often described as A(TA)7TAA or duplication of TA in promoter) is a principal GS-associated genotype, particularly in European/Caucasian ancestry groups. (goluch2024nutritioningilbert’s pages 2-3, kim2024shouldweconsider pages 1-2)
- **UGT1A1*6 (c.211G>A; p.Gly71Arg / p.G71R)** is emphasized as a common GS-relevant coding variant in East Asian populations and in neonatal/prolonged jaundice workups. (kim2024shouldweconsider pages 1-2)

### 2.2 Risk factors
**Genetic risk factors:** reduced-function UGT1A1 alleles/haplotypes, including *28 and *6; additional disease-causing variants are documented in sequencing studies of unconjugated hyperbilirubinemia cohorts (e.g., *27, *63, *7 reported in a 2023 study context). (yao2023geneticvariationsunderlying pages 1-2)

**Environmental/physiologic risk factors (gene–environment interaction):** caloric restriction/fasting, dehydration, intercurrent illness/infection, stress, surgery/anesthesia, pregnancy, sleep deprivation, and intense physical exertion can precipitate jaundice episodes and transient bilirubin rises in genetically predisposed individuals. (goluch2024nutritioningilbert’s pages 2-3, beutler2024gilbertssyndromebrightand pages 1-4)

### 2.3 Protective factors
The retrieved evidence supports an active research theme that mildly elevated bilirubin may have **cytoprotective/antioxidant and immunomodulatory** properties. A 2023 cross-sectional HBV-exposed cohort study reported markedly lower cirrhosis/HCC incidence among individuals carrying disease-causing UGT1A1 variants versus wild type, suggesting a potentially protective association (not necessarily causal for GS itself). (yao2023geneticvariationsunderlying pages 1-2)

### 2.4 Gene–environment interactions
The 2024 nutrition-focused systematic review explicitly frames GS as a **“genetically induced, nutritionally exacerbated”** disorder, where caloric restriction can rapidly increase bilirubin levels in affected individuals. (goluch2024nutritioningilbert’s pages 1-2, goluch2024nutritioningilbert’s pages 2-3)

---

## 3. Phenotypes

### 3.1 Core phenotype spectrum (with suggested HPO terms)
1. **Intermittent jaundice** (scleral/skin), often painless and non-pruritic.
   - Suggested HPO: **Jaundice (HP:0000952)**
   - Evidence: described as intermittent mild jaundice with otherwise normal liver tests. (beutler2024gilbertssyndromebrightand pages 1-4)

2. **Laboratory abnormality: unconjugated hyperbilirubinemia**
   - Suggested HPO: **Unconjugated hyperbilirubinemia (HP:0003154)**
   - Suggested LOINC (generic): serum/plasma **total bilirubin** and **direct bilirubin** measurement (implementation-specific codes)
   - Evidence: mild bilirubin elevation typical of GS; normal bilirubin stated as ~0.1–1.2 mg/dL; GS typically ~1.2–5.3 mg/dL, often not exceeding ~5–6 mg/dL. (gonzaleziglesias2024geneticvariationin pages 1-2, goluch2024nutritioningilbert’s pages 2-3)

3. **Normal liver enzymes (important negative phenotype)**
   - Suggested LOINC (generic): ALT/AST/ALP/GGT panel
   - Evidence: A 2024 study in 773 healthy volunteers found higher bilirubin in genotype-inferred intermediate/poor UGT1A1 metabolizers without association with liver enzyme abnormalities. (gonzaleziglesias2024geneticvariationin pages 1-2)

4. **Trigger sensitivity** (fasting/caloric restriction/stress-related episodes)
   - Suggested HPO: could be represented as episodic worsening of jaundice/hyperbilirubinemia; may be modeled as exposure-linked exacerbation in a KB schema
   - Evidence: calorie reduction can cause a 2–3× bilirubin rise within 48 hours; multiple triggers listed above. (goluch2024nutritioningilbert’s pages 2-3)

### 3.2 Age of onset, severity, and course
- Often recognized in adolescence/young adulthood (triggered episodic phenotype); in pediatrics, UGT1A1 variants can be prominent in the setting of prolonged jaundice evaluation. (goluch2024nutritioningilbert’s pages 1-2, kim2024shouldweconsider pages 1-2)
- Severity is typically mild and fluctuating; severe neonatal unconjugated hyperbilirubinemia may reflect different variant combinations or overlap with Crigler–Najjar spectrum disorders rather than classic adult GS. (kim2024shouldweconsider pages 1-2)

### 3.3 Quality of life impact
The 2024 systematic review states that **episodes of jaundice in GS negatively affect quality of life** and focuses on nutritional strategies to reduce episode frequency. (goluch2024nutritioningilbert’s pages 1-2)

---

## 4. Genetic / Molecular Information

### 4.1 Causal genes
- **UGT1A1** (UDP glucuronosyltransferase family 1 member A1) is the key gene in the retrieved evidence base for GS. (yao2023geneticvariationsunderlying pages 1-2, OpenTargets Search: Gilbert syndrome-UGT1A1)

### 4.2 Pathogenic/associated variants (examples from retrieved sources)
A structured summary is provided in the artifact below.

| Gene (HGNC symbol) | Locus/OMIM (if available from context) | Common pathogenic/associated variants (HGVS and star allele where available) | Variant type (promoter STR, missense, etc.) | Ethnic distribution notes | Functional effect on UGT1A1 activity | Clinical implications (bilirubin levels, drug toxicity) |
|---|---|---|---|---|---|---|
| UGT1A1 | Chromosome 2q37; OMIM *191740; Gilbert syndrome OMIM #143500 | A(TA)7TAA promoter repeat, commonly referred to as **UGT1A1*28**; also described as c.-40_-39dupTA / c.-41_-40dupTA in retrieved texts | Promoter short tandem repeat / insertion in TATA box | Predominant GS-associated allele in Caucasian and many African/European populations; prevalence estimates in Europeans ~5–10%, Sub-Saharan Africans 15–25% for GS-related prevalence context; “almost all” GS individuals in Caucasian/African groups in review context are homozygous for *28 (goluch2024nutritioningilbert’s pages 1-2, gonzaleziglesias2024geneticvariationin pages 1-2, kim2024shouldweconsider pages 1-2) | Reduces UGT1A1 expression/activity; one 2024 review states *28 homozygosity is present in ~90% of GS patients and promoter variant can reduce activity to ~30% of normal; bilirubin glucuronidation reported as ~50% of wild-type in 7/7 vs 6/6 genotype (goluch2024nutritioningilbert’s pages 1-2, beutler2024gilbertssyndromebrightand pages 1-4, gonzaleziglesias2024geneticvariationin pages 2-3, goluch2024nutritioningilbert’s pages 2-3) | Main molecular basis of intermittent unconjugated hyperbilirubinemia in GS; bilirubin often ~1.2–5.3 mg/dL and usually <5–6 mg/dL; relevant pharmacogenomic risk allele for **irinotecan** toxicity and **atazanavir**-associated hyperbilirubinemia; useful diagnostically when liver enzymes are otherwise normal (goluch2024nutritioningilbert’s pages 2-3, silva2025gilbert’ssyndromethe pages 5-6, beutler2024gilbertssyndromebrightand pages 1-4, gonzaleziglesias2024geneticvariationin pages 1-2) |
| UGT1A1 | Chromosome 2q37; OMIM *191740 | **c.211G>A (p.Gly71Arg, p.G71R), UGT1A1*6** | Missense variant in exon 1 | Common in East Asian populations; highlighted as more prevalent in Asians/Koreans/Chinese than in Caucasians (kim2024shouldweconsider pages 1-2, goluch2024nutritioningilbert’s pages 1-2, silva2025gilbert’ssyndromethe pages 3-5) | Decreases UGT1A1 enzymatic activity; contributes to mild bilirubin conjugation deficiency and GS phenotype; in East Asians accounts for a notable fraction of bilirubin variability (goluch2024nutritioningilbert’s pages 2-3, kim2024shouldweconsider pages 1-2, gonzaleziglesias2024geneticvariationin pages 1-2) | Associated with prolonged neonatal jaundice and adult GS; in a 2024 infant cohort it was the most common variant (46.5% among detected variants); also implicated in irinotecan toxicity literature via reduced SN-38 glucuronidation (kim2024shouldweconsider pages 1-2, gonzaleziglesias2024geneticvariationin pages 1-2) |
| UGT1A1 | Chromosome 2q37; OMIM *191740 | **c.-3275T>G** (PBREM/enhancer-region variant; often discussed with GS haplotypes) | Regulatory/promoter-enhancer variant | Reported in Asian infant cohorts with prolonged jaundice; second most common variant in one Korean infant series (30.2%) (kim2024shouldweconsider pages 1-2) | Presumed reduction in transcription/expression when part of GS-associated haplotypes; contributes to reduced bilirubin conjugation (kim2024shouldweconsider pages 1-2) | Seen in prolonged unconjugated neonatal hyperbilirubinemia and supports molecular diagnosis of GS-spectrum bilirubin disorders when routine workup is unrevealing (kim2024shouldweconsider pages 1-2) |
| UGT1A1 | Chromosome 2q37; OMIM *191740 | **UGT1A1*80 (rs887829)**, used as proxy for *28 in one 2024 pharmacogenetic study | Regulatory SNP in strong linkage disequilibrium with promoter allele | Reported as being in near-complete LD with *28 (r² 0.99) in studied populations; used as a surrogate marker rather than a direct causal assignment in the retrieved study (gonzaleziglesias2024geneticvariationin pages 2-3, gonzaleziglesias2024geneticvariationin pages 1-2) | Serves as indicator of reduced-function *28 haplotype / genotype-informed intermediate or poor metabolizer status (gonzaleziglesias2024geneticvariationin pages 2-3, gonzaleziglesias2024geneticvariationin pages 1-2) | Higher bilirubin in intermediate/poor metabolizers; no associated elevation of liver enzymes in healthy volunteers, supporting benignity of GS-like biochemical phenotype in trial screening contexts (gonzaleziglesias2024geneticvariationin pages 2-3, gonzaleziglesias2024geneticvariationin pages 1-2) |
| UGT1A1 | Chromosome 2q37; OMIM *191740 | **UGT1A1*27, UGT1A1*63, UGT1A1*7** | Mixed coding/regulatory disease-causing variants (exact HGVS not provided in retrieved context) | Identified in a 2023 Chinese HBV/GS cross-sectional sequencing study among patients with unconjugated hyperbilirubinemia (yao2023geneticvariationsunderlying pages 1-2) | Disease-causing variants associated with greater UGT1A1 deficiency; study inferred that accumulation/rarity of variants correlated with stronger biologic effect (yao2023geneticvariationsunderlying pages 1-2) | In HBV-exposed individuals, carriers had lower LC/HCC incidence (13.14% vs 78.95%) and some achieved HBsAg clearance only in the variant group; these findings concern comorbidity/outcomes rather than routine GS diagnosis (yao2023geneticvariationsunderlying pages 1-2) |
| UGT1A1 | Chromosome 2q37; OMIM *191740 | **c.1091C>T (p.Pro364Leu, P364L)** | Missense variant | Reported in Chinese neonates with severe prolonged unconjugated hyperbilirubinemia; may blur GS vs Crigler-Najjar type II boundaries (kim2024shouldweconsider pages 1-2) | Residual activity reported in retrieved context as ~35.6% of wild-type enzyme activity (kim2024shouldweconsider pages 1-2) | Can present with bilirubin >15 mg/dL in neonates and respond to phenobarbital, later normalizing; illustrates that some UGT1A1 variants produce phenotypes overlapping GS and CN-II rather than classic mild adult GS alone (kim2024shouldweconsider pages 1-2) |
| UGT1A1 | Chromosome 2q37; OMIM *191740 | **UGT1A1*36** [A(TA)6TAA], **UGT1A1*37** [A(TA)9TAA] | Promoter STR alleles | Mentioned as alternative promoter-repeat alleles in pharmacogenetic context rather than classic GS-causing variants; *36 aligns with normal-function haplotypes, *37 with reduced-function haplotypes (gonzaleziglesias2024geneticvariationin pages 2-3) | *36 generally reflects more normal promoter configuration; *37 associates with reduced activity via linkage with low-function haplotypes (gonzaleziglesias2024geneticvariationin pages 2-3) | Important for genotype interpretation in pharmacogenomics and bilirubin phenotyping; less central than *28/*6 for classic GS diagnosis in retrieved evidence (gonzaleziglesias2024geneticvariationin pages 2-3) |


*Table: This table summarizes the main UGT1A1 variants linked to Gilbert syndrome and related unconjugated hyperbilirubinemia phenotypes, including population patterns, functional effects, and pharmacogenomic relevance. It is useful for mapping disease genetics to clinical interpretation and drug-response implications.*

### 4.3 Functional consequences
Reduced-function variants decrease bilirubin glucuronidation capacity; one review/source describes a promoter-repeat variant reducing activity to ~30% of normal, and genotype-activity relationships are reported (e.g., ~50% activity for 7/7 vs 6/6; ~80% for 6/7 vs 6/6). (goluch2024nutritioningilbert’s pages 2-3, gonzaleziglesias2024geneticvariationin pages 2-3)

### 4.4 Modifier genes / epigenetics / chromosomal abnormalities
No specific modifier genes or epigenetic mechanisms were captured in the retrieved GS-focused evidence snippets in this run.

---

## 5. Environmental Information

### 5.1 Lifestyle and nutritional factors
A 2024 PRISMA-based systematic review of GS-related clinical trials (1963–2023) emphasizes that **caloric restriction and dietary composition** can meaningfully alter bilirubin levels in GS and suggests practical strategies to reduce episodes (avoid excessive calorie restriction; consider dietary fats and bioactive compounds in certain plant families). (goluch2024nutritioningilbert’s pages 1-2, goluch2024nutritioningilbert’s media eb15b11f)

**Visual evidence (systematic review evidence base):** PRISMA flow diagram and trial-summary tables are available from the review.
- PRISMA diagram and trial tables: (goluch2024nutritioningilbert’s media eb15b11f)

---

## 6. Mechanism / Pathophysiology

### 6.1 Causal chain (from trigger to phenotype)
1. **Heme/hemoglobin catabolism** produces bilirubin.
2. Unconjugated bilirubin must be **taken up by hepatocytes** and **conjugated with glucuronic acid** to become bile-soluble.
3. **UGT1A1** is the key enzyme mediating bilirubin glucuronidation; **reduced UGT1A1 activity/expression** yields impaired conjugation and accumulation of unconjugated bilirubin.
4. Physiologic stressors (fasting/calorie restriction, illness, dehydration, exertion, etc.) transiently increase bilirubin or reduce clearance, triggering **episodic jaundice** in genetically predisposed individuals.

This mechanistic framing and the “bottleneck” concept at hepatic conjugation are explicitly described in the 2024 systematic review background. (goluch2024nutritioningilbert’s pages 1-2, goluch2024nutritioningilbert’s pages 2-3)

### 6.2 Molecular pathways and ontology suggestions
- Suggested GO (process/function level): **bilirubin metabolic process**; **glucuronosyltransferase activity**; **bilirubin glucuronosyltransferase activity** (GO term IDs not retrieved in evidence chunks). (goluch2024nutritioningilbert’s pages 1-2)
- Primary organ/cell type: liver and **hepatocytes**.
  - Suggested UBERON: **liver (UBERON:0002107)**
  - Suggested CL: **hepatocyte (CL:0000182)**
  - Evidence: UGT1A1 described as key hepatic conjugation enzyme. (yao2023geneticvariationsunderlying pages 1-2, gonzaleziglesias2024geneticvariationin pages 1-2)

### 6.3 Pharmacogenomics mechanism (drug metabolism)
UGT1A1 also glucuronidates drugs and xenobiotics; thus, reduced UGT1A1 function can increase exposure/toxicity of some UGT1A1 substrates (notably irinotecan’s active metabolite SN-38 in oncology pharmacogenomics literature). (takano2017ugt1a1polymorphismsin pages 1-2)

---

## 7. Anatomical Structures Affected

### 7.1 Organ/tissue/cell
- **Primary:** liver (bilirubin conjugation) and hepatocytes. (gonzaleziglesias2024geneticvariationin pages 1-2)
- **Secondary/clinical manifestation site:** skin/sclera (visible jaundice) as a downstream manifestation of hyperbilirubinemia. (beutler2024gilbertssyndromebrightand pages 1-4)

---

## 8. Temporal Development

- **Onset pattern:** typically chronic lifelong predisposition with **episodic** hyperbilirubinemia; episodes can be triggered by environmental/physiologic stressors. (beutler2024gilbertssyndromebrightand pages 1-4, goluch2024nutritioningilbert’s pages 2-3)
- **Course:** fluctuating; bilirubin may normalize after trigger resolution/diet normalization. (goluch2024nutritioningilbert’s pages 2-3)

---

## 9. Inheritance and Population

### 9.1 Inheritance
The retrieved sources treat GS as a genetically determined disorder due to UGT1A1 variants; a specific Mendelian inheritance label (e.g., autosomal recessive vs complex haplotype) was not consistently provided in the excerpts captured in this run.

### 9.2 Epidemiology (recently summarized)
Reported prevalence varies substantially by ancestry and region:
- One 2024 primary-source background section summarizes ethnic prevalence patterns: **Sub-Saharan African ~15–25%**, **Europeans ~5–10%**, **East Asian ~0–5%**. (gonzaleziglesias2024geneticvariationin pages 1-2)
- The 2024 systematic review summarizes wider ranges: **~3–16% overall**, **~2% in East Asians**, and up to **~20%** in India/South Asia/Middle East. (goluch2024nutritioningilbert’s pages 1-2)

Sex differences are repeatedly noted, with male predominance in diagnosis; the nutrition systematic review reports male:female diagnosis ratios and example prevalence estimates by sex in secondary summaries. (goluch2024nutritioningilbert’s pages 1-2)

---

## 10. Diagnostics

### 10.1 Clinical tests and laboratory findings
Typical diagnostic pattern is repeated demonstration of **isolated, predominantly unconjugated hyperbilirubinemia** with **normal liver enzymes** and absence of hemolysis or structural liver disease. (goluch2024nutritioningilbert’s pages 2-3, gonzaleziglesias2024geneticvariationin pages 1-2)

Quantitative diagnostic context captured:
- Normal bilirubin: ~0.1–1.2 mg/dL; GS often ~1.2–5.3 mg/dL. (gonzaleziglesias2024geneticvariationin pages 1-2)
- GS-compatible ranges cited in one review: unconjugated hyperbilirubinemia usually ≤4–5 mg/dL with normal liver tests. (beutler2024gilbertssyndromebrightand pages 1-4)

### 10.2 Genetic testing (real-world implementation)
UGT1A1 genotyping/sequencing is used in selected clinical scenarios:
- In a Korean infant cohort with prolonged jaundice (>21 days), **30/33 tested infants (90.9%)** had UGT1A1 variants; the most frequent was **c.211G>A (46.5%)**, followed by **c.-3275T>G (30.2%)**. (kim2024shouldweconsider pages 1-2)

**Direct abstract quote (Kim 2024):** “Thirty-three infants agreed to UGT1A1 mutation analysis, and 30 (90.9%) were positive for UGT1A1 mutations.” (kim2024shouldweconsider pages 1-2)

### 10.3 Differential diagnosis
Reviews emphasize diagnosis by exclusion, including excluding hemolysis and other hereditary jaundice disorders such as Crigler–Najjar syndrome, Rotor syndrome, and Dubin–Johnson syndrome. (beutler2024gilbertssyndromebrightand pages 1-4)

---

## 11. Outcome / Prognosis

Overall, GS is described as **benign** with no evidence of liver injury and typically no disease-specific treatment requirement. (beutler2024gilbertssyndromebrightand pages 1-4, gonzaleziglesias2024geneticvariationin pages 1-2)

A key clinically relevant outcome is drug-related toxicity risk for certain UGT1A1 substrates/inhibitors (see Treatment/Applications). (takano2017ugt1a1polymorphismsin pages 1-2)

---

## 12. Treatment

### 12.1 Standard management
No disease-specific pharmacotherapy is typically required; management centers on reassurance, avoidance of triggers (e.g., prolonged fasting/caloric restriction), and appropriate diagnostic workup to exclude other causes. (goluch2024nutritioningilbert’s pages 1-2, beutler2024gilbertssyndromebrightand pages 1-4)

**MAXO suggestions (knowledge-base oriented):**
- Patient education / counseling
- Dietary modification / avoidance of prolonged fasting
- Genetic testing (selected contexts)

(ontology suggestions summarized in artifact below).

| Item (phenotype/diagnostic test/mechanism) | Suggested ontology term(s) | Brief description | Evidence notes |
|---|---|---|---|
| Intermittent jaundice | HPO: Jaundice (HP:0000952); HPO: Intermittent jaundice (suggested specific child term if used locally) | Episodic mild scleral/skin icterus, usually benign and fluctuating | Typical GS presentation is intermittent jaundice with otherwise normal liver tests; bilirubin usually ~1.2–5.3 mg/dL and often ≤4–5 mg/dL in adults (gonzaleziglesias2024geneticvariationin pages 1-2, beutler2024gilbertssyndromebrightand pages 1-4) |
| Unconjugated hyperbilirubinemia | HPO: Hyperbilirubinemia (HP:0002904); HPO: Unconjugated hyperbilirubinemia (HP:0003154); LOINC: Total bilirubin in Serum/Plasma; Direct bilirubin in Serum/Plasma | Core laboratory abnormality with predominantly indirect bilirubin elevation | GS is defined by mild unconjugated hyperbilirubinemia; diagnostic ranges cited include bilirubin <5–6 mg/dL with direct bilirubin <0.7 mg/dL and no hemolysis/liver disease (goluch2024nutritioningilbert’s pages 2-3) |
| Normal liver enzymes | HPO: Abnormality of liver physiology (negated/normal finding in local schema); LOINC: ALT, AST, ALP, GGT panels | Absence of hepatocellular injury markers helps distinguish GS from liver disease | 2024 healthy-volunteer study found higher bilirubin in UGT1A1 IM/PM phenotypes but no association with liver enzyme abnormalities (gonzaleziglesias2024geneticvariationin pages 1-2) |
| Triggered bilirubin rises with fasting/stress | HPO: Abnormality of metabolism/homeostasis (context-dependent); MAXO: Dietary modification / avoidance of fasting (suggested); LOINC: serial bilirubin measurement | Hyperbilirubinemia worsens during fasting, illness, dehydration, exertion, surgery, stress | Caloric restriction can increase bilirubin 2–3-fold within 48 h; triggers include fasting >12 h, dehydration, infection, intense exercise, surgery, pregnancy, stress, alcohol, sleep deprivation (goluch2024nutritioningilbert’s pages 2-3, beutler2024gilbertssyndromebrightand pages 1-4) |
| Gallstones / cholelithiasis risk | HPO: Cholelithiasis (HP:0001081) | Recognized complication/comorbidity, especially with coexisting hemolysis | UK Biobank analysis found cholelithiasis significantly higher in men with GS, OR 1.50 (95% CI 1.3–1.7); review sources also note gallstone risk (goluch2024nutritioningilbert’s pages 2-3, beutler2024gilbertssyndromebrightand pages 1-4) |
| UGT1A1 deficiency / reduced bilirubin glucuronidation | GO: bilirubin glucuronosyltransferase activity; GO: glucuronosyltransferase activity; GO: bilirubin metabolic process | Molecular defect is reduced UGT1A1-mediated conjugation of bilirubin | Common variants include promoter TA repeat *28 and coding variant *6; promoter variant may reduce activity to ~30% of normal, with 7/7 genotype ~50% bilirubin glucuronidation relative to 6/6 (gonzaleziglesias2024geneticvariationin pages 2-3, goluch2024nutritioningilbert’s pages 2-3, yao2023geneticvariationsunderlying pages 1-2) |
| Hepatocyte involvement | UBERON: liver (UBERON:0002107); CL: hepatocyte (CL:0000182); GO Cellular Component: endoplasmic reticulum membrane | Primary affected cell type and organ for bilirubin conjugation | UGT1A1 is the key bilirubin-conjugating enzyme in liver; GS reflects reduced hepatic glucuronidation rather than structural liver disease (yao2023geneticvariationsunderlying pages 1-2, gonzaleziglesias2024geneticvariationin pages 1-2) |
| Genetic confirmation / UGT1A1 testing | LOINC: Molecular genetics tests for UGT1A1 (local implementation-specific); MAXO: Genetic testing; HPO: Abnormality of bilirubin metabolism | Sequencing/genotyping can support diagnosis, especially atypical or prolonged cases | Common tested variants include UGT1A1*28, *6, c.-3275T>G, c.211G>A; in prolonged infant jaundice, 30/33 tested infants had UGT1A1 variants (kim2024shouldweconsider pages 1-2) |
| Differential diagnosis exclusion | MAXO: Diagnostic laboratory testing; HPO terms for hemolysis/liver disease used as exclusions | Diagnosis is typically by exclusion of hemolysis and other hereditary/acquired jaundice disorders | Reviews emphasize ruling out hemolysis, Crigler–Najjar syndrome, Rotor syndrome, Dubin–Johnson syndrome, and other liver disease before labeling GS (beutler2024gilbertssyndromebrightand pages 1-4, silva2025gilbert’ssyndromethe pages 3-5) |
| Supportive management / reassurance | MAXO: Patient education; MAXO: Counseling; MAXO: Dietary modification | Usually no disease-specific pharmacotherapy required; management focuses on education and trigger avoidance | GS is generally benign, no hepatic toxicity demonstrated in 2024 volunteer data; avoiding excessive calorie restriction may reduce jaundice episodes (goluch2024nutritioningilbert’s pages 1-2, gonzaleziglesias2024geneticvariationin pages 1-2) |


*Table: This table maps the core clinical features, diagnostics, and mechanisms of Gilbert syndrome to practical ontology suggestions (HPO, LOINC, GO, UBERON, CL, MAXO). It is useful for structuring disease knowledge-base entries and annotating phenotypes, pathways, and clinical workflows with recent evidence.*

### 12.2 Pharmacogenomics / precision medicine applications (real-world)
UGT1A1 genotyping is widely implemented in oncology and other drug-safety contexts; many trials and clinical programs use UGT1A1 (*28/*6) status to mitigate toxicity.

**ClinicalTrials.gov examples (UGT1A1-guided dosing/PK; not GS-specific interventions):**
- **NCT05148767** (posted 2022; recruiting; Phase 4): UGT1A1-guided irinotecan dosing in neoadjuvant chemoradiotherapy for locally advanced rectal cancer; requires UGT1A1 *6 and *28 testing and assigns irinotecan dose by genotype. (NCT05148767 chunk 1)
- **NCT01523431** (posted 2012; completed; Phase 2/3): genotype-guided irinotecan dosing in metastatic colorectal cancer; homozygotes randomized to standard vs 50% reduced irinotecan dose. (NCT01523431 chunk 1)
- **NCT02680795** (posted 2016; completed; Phase 1): belinostat PK/safety stratified by UGT1A1*28 genotype. (NCT02680795 chunk 1)

### 12.3 Experimental / advanced therapeutics
For severe UGT1A1 deficiency disorders (Crigler–Najjar type I), gene replacement is under study (not GS):
- **NCT06641154** (posted 2024; recruiting; Phase 1/2): AAV8 vector carrying normal human UGT1A1 for Crigler–Najjar type I. (NCT06641154 chunk 1)

---

## 13. Prevention
Primary prevention of GS is not applicable (genetic predisposition). Practical prevention of symptomatic episodes is framed as **trigger avoidance**, particularly avoiding excessive caloric restriction/fasting and dehydration. (goluch2024nutritioningilbert’s pages 2-3)

---

## 14. Other Species / Natural Disease
No naturally occurring GS-equivalent disease in non-human species was captured in the retrieved GS-specific snippets; however, Ugt1a1 deficiency models exist (see Model Organisms).

---

## 15. Model Organisms
Model systems in the retrieved literature largely address **UGT1A1 deficiency** and neonatal hyperbilirubinemia (often more severe than classic GS), and also include **humanized UGT1A1*28 mouse models** used for drug-metabolism work.

Examples retrieved (not fully extracted as evidence snippets in this run but available as papers in the corpus):
- Humanized UGT1 mouse models expressing human UGT1 locus and/or UGT1A1*28 allele for studying bilirubin metabolism and drug clearance. (silva2025gilbert’ssyndromethe pages 8-9)
- Ugt1 locus knockout mice modeling severe unconjugated hyperbilirubinemia (Crigler–Najjar type I-like). (silva2025gilbert’ssyndromethe pages 8-9)

---

## Recent developments and latest research (2023–2024 prioritized)

The table below summarizes key recent (2023–2024) evidence sources captured in this run.

| Year | First author | Type (primary study/review/systematic review) | Population/setting | Key findings (quantitative where possible) | PMID/DOI/URL | Notes |
|---|---|---|---|---|---|---|
| 2024 | Goluch | Systematic review of clinical trials | Clinical studies in people with Gilbert syndrome, literature 1963–2023; 19 studies included | GS described as the most common benign hyperbilirubinemia due to reduced UGT1A1 activity; prevalence reported as 3–16% overall, ~2% in East Asians, up to ~20% in India/South Asia/Middle East; ~90% of GS patients carry homozygous A(TA)7TAA (*28); fasting/caloric restriction can raise bilirubin 2–3× within 48 h; avoiding excessive calorie restriction and consuming certain fats/bioactive plant compounds may reduce jaundice episodes; episodes negatively affect quality of life (goluch2024nutritioningilbert’s pages 2-3, goluch2024nutritioningilbert’s pages 1-2, goluch2024nutritioningilbert’s media eb15b11f) | DOI: 10.3390/nu16142247; https://doi.org/10.3390/nu16142247 | Diet/nutrition; triggers; QoL; ethnicity-specific genetics |
| 2024 | González-Iglesias | Primary study | 773 healthy volunteers in 29 bioequivalence trials, Spain | Bilirubin higher in UGT1A1 intermediate and poor metabolizers vs normal metabolizers; decreased uric acid in poor metabolizers; no association between UGT1A1 phenotype and liver enzyme levels; supports inclusion of likely GS participants in bioequivalence studies; paper cites prevalence by ancestry: Sub-Saharan African 15–25%, Europeans 5–10%, East Asian 0–5% (gonzaleziglesias2024geneticvariationin pages 2-3, gonzaleziglesias2024geneticvariationin pages 1-2) | DOI: 10.3389/fphar.2024.1389968; https://doi.org/10.3389/fphar.2024.1389968 | Pharmacogenomics; real-world trial eligibility; benign liver biochemistry |
| 2024 | Kim | Primary study | 74 Korean infants with prolonged jaundice >21 days; 33 underwent UGT1A1 testing | 30/33 tested infants (90.9%) had UGT1A1 mutations; common variants were c.211G>A (46.5%) and c.-3275T>G (30.2%); breastfeeding was the only significant factor associated with mutation-positive cases (P=0.027); supports utility of UGT1A1 testing in prolonged unexplained neonatal jaundice (kim2024shouldweconsider pages 1-2) | DOI: 10.5385/nm.2024.31.1.1; https://doi.org/10.5385/nm.2024.31.1.1 | Neonatal/prolonged jaundice; East Asian variant spectrum |
| 2024 | Beutler | Review | Literature review | GS summarized as the most common inherited jaundice affecting ~5–10% of people, more common in men; common promoter variant reduces UGT activity to ~30% of normal; typical unconjugated bilirubin usually up to ~4–5 mg/dL with normal liver tests; triggers include stress, alcohol, dehydration, heavy exercise, surgery, sleep deprivation, starvation; notes gallstones/cholelithiasis and hemolytic anemia associations (beutler2024gilbertssyndromebrightand pages 1-4) | 2024 review; journal/PMID not available in context | Clinical overview; triggers; comorbidity; protective vs adverse aspects |
| 2023 | Poynard | Primary study | UK Biobank, apparently healthy middle-aged Europeans with liver data (n=138,125) | GS phenotypically defined using stratified total bilirubin centiles; in women, stratified approach identified 10% GS (7,741/76,809) vs 3.7% using the historical ≥1 mg/dL cutoff; after adjustment/Mendelian randomization, only cholelithiasis remained significantly higher in men with GS (OR 1.50, 95% CI 1.3–1.7; P=0.001); no adjusted survival difference over 15 years (poynard2023clinicalandgenetic pages 1-1) | DOI: 10.1097/HC9.0000000000000245; https://doi.org/10.1097/HC9.0000000000000245 | Population definition; sex-specific diagnostic thresholds; gallstones risk |
| 2023 | Yao | Primary study | Single-ethnic Chinese cross-sectional study; 2,792 screened for unconjugated hyperbilirubinemia, 175 with confirmed HBV exposure analyzed | Five disease-causing UGT1A1 variants detected (*28, *6, *27, *63, *7); cirrhosis/HCC incidence lower in UGT1A1-variant hosts than wild type (13.14% vs 78.95%, P<0.0001); HBsAg clearance in non-cirrhotic patients seen only in variant group (12.32% vs 0%); suggests mildly elevated bilirubin may be protective in HBV outcomes (yao2023geneticvariationsunderlying pages 1-2) | DOI: 10.3389/fgene.2023.1265268; https://doi.org/10.3389/fgene.2023.1265268 | Comorbidity/prognosis; potential protective biology of mild hyperbilirubinemia |


*Table: This table summarizes key 2023–2024 evidence sources for Gilbert syndrome, prioritizing recent primary studies and systematic reviews. It highlights epidemiology, genetics, triggers, diagnostics, pharmacogenomics, and comorbidity findings useful for a disease knowledge base.*

**Important note:** Some identifier-level items (e.g., ICD/MeSH/Orphanet codes) and some mechanistic details (e.g., detailed transcriptional regulation of the TA-repeat promoter) were not directly available in the retrieved full-text snippets; this report avoids asserting those details without primary-source capture.


References

1. (gonzaleziglesias2024geneticvariationin pages 1-2): Eva González-Iglesias, Dolores Ochoa, Manuel Román, Paula Soria-Chacartegui, Samuel Martín-Vilchez, Marcos Navares-Gómez, Alejandro De Miguel, Pablo Zubiaur, Andrea Rodríguez-Lopez, Francisco Abad-Santos, and Jesús Novalbos. Genetic variation in ugt1a1 is not associated with altered liver biochemical parameters in healthy volunteers participating in bioequivalence trials. Frontiers in Pharmacology, May 2024. URL: https://doi.org/10.3389/fphar.2024.1389968, doi:10.3389/fphar.2024.1389968. This article has 3 citations.

2. (beutler2024gilbertssyndromebrightand pages 1-4): K Beutler and J Lewandowski. Gilbert's syndrome-bright and dark sides of the disease-literature review. Unknown journal, 2024.

3. (yao2023geneticvariationsunderlying pages 1-2): Bilian Yao, Qi Xu, Xinxin Zhang, and Yue Han. Genetic variations underlying gilbert syndrome and hbv infection outcomes: a cross-sectional study. Frontiers in Genetics, Nov 2023. URL: https://doi.org/10.3389/fgene.2023.1265268, doi:10.3389/fgene.2023.1265268. This article has 3 citations and is from a peer-reviewed journal.

4. (OpenTargets Search: Gilbert syndrome-UGT1A1): Open Targets Query (Gilbert syndrome-UGT1A1, 4 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

5. (kim2024shouldweconsider pages 1-2): Young Don Kim. Should we consider ugt1a1 mutation analysis in evaluating the prolonged jaundice of newborn infants? Neonatal Medicine, 31:1-8, Feb 2024. URL: https://doi.org/10.5385/nm.2024.31.1.1, doi:10.5385/nm.2024.31.1.1. This article has 0 citations.

6. (goluch2024nutritioningilbert’s pages 1-2): Zuzanna Goluch, Aldona Wierzbicka-Rucińska, and Ewelina Książek. Nutrition in gilbert’s syndrome—a systematic review of clinical trials according to the prisma statement. Nutrients, 16:2247, Jul 2024. URL: https://doi.org/10.3390/nu16142247, doi:10.3390/nu16142247. This article has 2 citations.

7. (goluch2024nutritioningilbert’s media eb15b11f): Zuzanna Goluch, Aldona Wierzbicka-Rucińska, and Ewelina Książek. Nutrition in gilbert’s syndrome—a systematic review of clinical trials according to the prisma statement. Nutrients, 16:2247, Jul 2024. URL: https://doi.org/10.3390/nu16142247, doi:10.3390/nu16142247. This article has 2 citations.

8. (NCT05148767 chunk 1): Ji Zhu, MD. UGT1A1-Based Irinotecan Therapy for Locally Advanced Rectal Cancer. Zhejiang Cancer Hospital. 2022. ClinicalTrials.gov Identifier: NCT05148767

9. (NCT01523431 chunk 1): Xu jianming. Individual Dosage Selection of Irinotecan (CPT-11) Based on UGT1A1 Genotype in Metastatic Colorectal Cancer Patients. The Affiliated Hospital of the Chinese Academy of Military Medical Sciences. 2012. ClinicalTrials.gov Identifier: NCT01523431

10. (NCT02680795 chunk 1):  Establish the PK of Belinostat in Patients With Wild-type, Heterozygous, and Homozygous UGT1A1*28 Genotypes. Acrotech Biopharma Inc.. 2016. ClinicalTrials.gov Identifier: NCT02680795

11. (goluch2024nutritioningilbert’s pages 2-3): Zuzanna Goluch, Aldona Wierzbicka-Rucińska, and Ewelina Książek. Nutrition in gilbert’s syndrome—a systematic review of clinical trials according to the prisma statement. Nutrients, 16:2247, Jul 2024. URL: https://doi.org/10.3390/nu16142247, doi:10.3390/nu16142247. This article has 2 citations.

12. (gonzaleziglesias2024geneticvariationin pages 2-3): Eva González-Iglesias, Dolores Ochoa, Manuel Román, Paula Soria-Chacartegui, Samuel Martín-Vilchez, Marcos Navares-Gómez, Alejandro De Miguel, Pablo Zubiaur, Andrea Rodríguez-Lopez, Francisco Abad-Santos, and Jesús Novalbos. Genetic variation in ugt1a1 is not associated with altered liver biochemical parameters in healthy volunteers participating in bioequivalence trials. Frontiers in Pharmacology, May 2024. URL: https://doi.org/10.3389/fphar.2024.1389968, doi:10.3389/fphar.2024.1389968. This article has 3 citations.

13. (silva2025gilbert’ssyndromethe pages 5-6): Arjuna P De Silva, Nilushi Nuwanshika, Madunil A Niriella, and Janaka H De Silva. Gilbert’s syndrome: the good, the bad and the ugly. Unknown journal, May 2025. URL: https://doi.org/10.20944/preprints202405.0500.v1, doi:10.20944/preprints202405.0500.v1.

14. (silva2025gilbert’ssyndromethe pages 3-5): Arjuna P De Silva, Nilushi Nuwanshika, Madunil A Niriella, and Janaka H De Silva. Gilbert’s syndrome: the good, the bad and the ugly. Unknown journal, May 2025. URL: https://doi.org/10.20944/preprints202405.0500.v1, doi:10.20944/preprints202405.0500.v1.

15. (takano2017ugt1a1polymorphismsin pages 1-2): Masashi Takano and Toru Sugiyama. Ugt1a1 polymorphisms in cancer: impact on irinotecan treatment. Pharmacogenomics and Personalized Medicine, 10:61-68, Feb 2017. URL: https://doi.org/10.2147/pgpm.s108656, doi:10.2147/pgpm.s108656. This article has 141 citations and is from a peer-reviewed journal.

16. (NCT06641154 chunk 1):  Gene Therapy for Crigler Najjar Syndrome Type I (AlphaCN). Federal State Budget Institution Research Center for Obstetrics, Gynecology and Perinatology Ministry of Healthcare. 2024. ClinicalTrials.gov Identifier: NCT06641154

17. (silva2025gilbert’ssyndromethe pages 8-9): Arjuna P De Silva, Nilushi Nuwanshika, Madunil A Niriella, and Janaka H De Silva. Gilbert’s syndrome: the good, the bad and the ugly. Unknown journal, May 2025. URL: https://doi.org/10.20944/preprints202405.0500.v1, doi:10.20944/preprints202405.0500.v1.

18. (poynard2023clinicalandgenetic pages 1-1): Thierry Poynard, Olivier Deckmyn, Valentina Peta, Mehdi Sakka, Pascal Lebray, Joseph Moussalli, Raluca Pais, Chantal Housset, Vlad Ratziu, Eric Pasmant, and Dominique Thabut. Clinical and genetic definition of serum bilirubin levels for the diagnosis of gilbert syndrome and hypobilirubinemia. Hepatology Communications, Sep 2023. URL: https://doi.org/10.1097/hc9.0000000000000245, doi:10.1097/hc9.0000000000000245. This article has 8 citations and is from a peer-reviewed journal.
