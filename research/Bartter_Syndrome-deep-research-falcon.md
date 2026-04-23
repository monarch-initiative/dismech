---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-22T22:14:52.573377'
end_time: '2026-04-22T22:32:32.658435'
duration_seconds: 1060.09
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Bartter syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 51
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Bartter syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Bartter syndrome** covering all of the
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
- **Disease Name:** Bartter syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Bartter syndrome** covering all of the
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


## Comprehensive Research Report: Bartter syndrome (Mendelian salt‑losing tubulopathy)

### Executive summary
Bartter syndrome (BS) is a group of inherited renal tubular salt‑wasting disorders primarily caused by loss‑of‑function variants in ion transport proteins of the thick ascending limb (TAL) of Henle (and related segments), producing chronic volume depletion with hyperreninemic hyperaldosteronism, hypokalemic hypochloremic metabolic alkalosis, and variable hypercalciuria/nephrocalcinosis. Recent (2023–2024) literature adds (i) long‑term outcome statistics from a 54‑patient multicenter Korean cohort, (ii) a mechanistic 2024 review emphasizing NKCC2 endoplasmic‑reticulum (ER) quality control/ER‑associated degradation (ERAD), and (iii) prenatal genomic/functional evidence that intronic MAGED2 variants can cause transient antenatal BS via cryptic splicing. (choi2023longtermoutcomeof pages 1-2, laghmani2024proteinqualitycontrol pages 1-2, yan2024identificationofa pages 1-2)

---

## 1. Disease information

### 1.1 Definition and current understanding
Bartter syndrome is a “rare salt-wasting tubulopathy” characterized by polyuria/failure to thrive, hypokalemia, metabolic alkalosis, hyperreninemia and hyperaldosteronism; antenatal forms often show polyhydramnios and prematurity, while “classic” forms usually present in infancy/childhood. (Frontiers in Medicine, published 2023-03; https://doi.org/10.3389/fmed.2023.1099840) (choi2023longtermoutcomeof pages 1-2)

Recent mechanistic work reinforces the TAL as the principal site of dysfunction, where reduced NKCC2/ROMK/ClC-K–barttin–mediated NaCl reabsorption increases distal Na+ delivery, enhancing ENaC-mediated Na+ uptake in exchange for K+ and H+, thereby driving hypokalemia and metabolic alkalosis. (alla2023ararepresentation pages 2-3, laghmani2024proteinqualitycontrol pages 1-2)

### 1.2 Key identifiers and ontologies
- **MONDO**: **Bartter syndrome = MONDO_0015231** (Open Targets disease association record). (yang2026identificationofthree pages 12-14)
  - Subtypes also appear in Open Targets/MONDO, e.g. **Bartter disease type 3 = MONDO_0011822**, **Bartter syndrome type 4 = MONDO_0019524**. (yang2026identificationofthree pages 12-14)
- **OMIM gene entries frequently used in classification** (from a 2023 primary report):
  - **CLCNKB** (classic/type III context): OMIM **607364** (zhou2023amosaicmutation pages 1-2)
  - **SLC12A1**: OMIM **601678** (zhou2023amosaicmutation pages 1-2)
  - **KCNJ1**: OMIM **241200** (zhou2023amosaicmutation pages 1-2)
  - **BSND**: OMIM **602522** (zhou2023amosaicmutation pages 1-2)
  - **MAGED2**: OMIM **300971** (zhou2023amosaicmutation pages 1-2)

**Not available in the retrieved full texts**: Orphanet disease ID, ICD‑10/ICD‑11 codes, and MeSH descriptor IDs for Bartter syndrome. These should be curated directly from the relevant ontology/terminology sources (Orphanet/WHO ICD browser/MeSH). (choi2023longtermoutcomeof pages 1-2)

### 1.3 Synonyms and alternative names
Common clinical/grouping terms used in the contemporary literature include:
- “**Antenatal Bartter syndrome**” vs “**classic Bartter syndrome**” (phenotype grouping) (choi2023longtermoutcomeof pages 1-2)
- “**Type I–V Bartter syndrome**” (genotype‑linked classification; nomenclature varies, particularly for CASR vs MAGED2 assignments across sources) (qasba2023barttersyndromea pages 2-5, yan2024identificationofa pages 1-2)
- “**Gitelman-like syndrome (GLS)**” as a phenotypic label used in cohorts when overlap exists (choi2023longtermoutcomeof pages 1-2)

### 1.4 Evidence source type
Most evidence for BS characteristics comes from **aggregated disease-level resources** (reviews/cohorts) plus **individual case reports** for rare genotypes or atypical presentations. For example: a multicenter cohort of 54 Korean patients (aggregated clinical resource) (choi2023longtermoutcomeof pages 1-2) and newborn/adult case reports illustrating mosaicism or adult-onset disease (individual cases). (zhou2023amosaicmutation pages 1-2, jiang2024adultclassicbartter pages 1-2)

---

## 2. Etiology

### 2.1 Disease causal factors
**Primary cause: Mendelian genetic defects** in TAL (and related) transport proteins and regulators.

A 2023 systematic review summarized BS as “a rare group of autosomal-recessive disorders” with impaired TAL transport and heterogeneous genetic causes. (Medicina, published 2023-09; https://doi.org/10.3390/medicina59091638) (qasba2023barttersyndromea pages 1-2)

### 2.2 Risk factors
- **Genetic**: biallelic pathogenic variants in SLC12A1, KCNJ1, CLCNKB, BSND, CLCNKA+CLCNKB; X‑linked pathogenic variants in MAGED2 in transient antenatal BS; gain‑of‑function CASR variants in Bartter‑like disease with hypocalcemia/hypercalciuria. (qasba2023barttersyndromea pages 2-5, thimm2024untanglingtheuncertain pages 4-6, yan2024identificationofa pages 1-2)
- **Family structure/consanguinity**: In a 2012–2022 case report/series systematic review, 21/118 patients were from consanguineous unions (~18%). (qasba2023barttersyndromea pages 2-5)

### 2.3 Protective factors
Not established in the retrieved primary evidence. Some long‑term course improvements (e.g., decreasing potassium supplementation needs with age) reflect disease trajectory/management rather than protective factors. (choi2023longtermoutcomeof pages 4-6)

### 2.4 Gene–environment interactions
Well‑defined exogenous triggers are not typical for Mendelian BS, but fetal environment (hypoxia/oxygenation shift at birth) is mechanistically central for **MAGED2‑related transient antenatal BS**, where renal salt handling “completely normalizes after birth” in many survivors. (yan2024identificationofa pages 4-6)

---

## 3. Phenotypes (with HPO suggestions and frequencies when available)

### 3.1 Core biochemical and clinical phenotype
Key findings repeatedly used for diagnosis and phenotyping include:
- **Hypokalemia** (HPO: *HP:0001942*) (choi2023longtermoutcomeof pages 1-2, alla2023ararepresentation pages 2-3)
- **Metabolic alkalosis** (HPO: *HP:0001940*) (choi2023longtermoutcomeof pages 1-2, alla2023ararepresentation pages 2-3)
- **Hypochloremia** (HPO: *HP:0011421*) (alla2023ararepresentation pages 2-3)
- **Hyperreninemia / hyperaldosteronism** (HPO: *HP:0000875* for hyperaldosteronism; hyperreninemia may be captured as elevated renin activity) (choi2023longtermoutcomeof pages 1-2, alla2023ararepresentation pages 2-3)
- **Polyuria** (HPO: *HP:0000103*) and **polydipsia** (HPO: *HP:0001959*) (choi2023longtermoutcomeof pages 1-2, alla2023ararepresentation pages 2-3)
- **Failure to thrive / growth failure** (HPO: *HP:0001508*; *HP:0001510* for growth delay) (choi2023longtermoutcomeof pages 1-2, alla2023ararepresentation pages 2-3)

### 3.2 Antenatal/neonatal features (frequency from a 2023 multicenter cohort)
In the 54‑patient Korean cohort (Frontiers in Medicine; 2023-03; https://doi.org/10.3389/fmed.2023.1099840):
- **Polyhydramnios** (HPO: *HP:0001561*) occurred in **47% (18/38)** (choi2023longtermoutcomeof pages 2-3)
- **Preterm birth** (HPO: *HP:0001622*) occurred in **28% (13/46)** (choi2023longtermoutcomeof pages 2-3)

### 3.3 Renal complications and extrarenal findings (frequency from the 2023 cohort)
From the same 54‑patient cohort:
- **Nephrocalcinosis** (HPO: *HP:0000121*) at presentation: **41% (17/41)**; at last visit: **35% (15/43)**, with strong genotype dependence (e.g., 100% in BS1/BS2/BS4 groups reported in the paper). (choi2023longtermoutcomeof pages 2-3, choi2023longtermoutcomeof pages 4-6)
- **Short stature** (HPO: *HP:0004322*) at last follow‑up: **41% (22/54)**; among adults >19 years, **50% (5/10)** were short. (choi2023longtermoutcomeof pages 4-6)
- **Developmental delay** (HPO: *HP:0001263*): **15% (8/54)** (choi2023longtermoutcomeof pages 4-6)
- **Sensorineural hearing loss** (HPO: *HP:0000407*): **7% (4/54)** (choi2023longtermoutcomeof pages 4-6)
- **Chronic kidney disease / impaired kidney function** (HPO: *HP:0012624*): **11%** developed CKD G3–G5 (6 patients; 4 G3, 2 G5). (choi2023longtermoutcomeof pages 1-2, choi2023longtermoutcomeof pages 4-6)

### 3.4 Phenotypic heterogeneity (systematic review of 2012–2022 case reports/series)
A systematic review (Medicina; 2023-09; https://doi.org/10.3390/medicina59091638) aggregated 118 reported BS patients and highlighted heterogeneous presentation. It reported (among cases with genetic typing) a predominance of type III and common symptoms including polyuria, polydipsia, vomiting and dehydration, and noted antenatal features (polyhydramnios/prematurity). (qasba2023barttersyndromea pages 1-2, qasba2023barttersyndromea pages 2-5)

---

## 4. Genetic/molecular information

### 4.1 Causal genes and inheritance
A gene–subtype map is summarized in the table artifact below (with nephron localization and hallmark phenotypes), based on 2023–2024 sources and aligned to TAL transport physiology.

| Subtype (common name) | Gene(s) | Protein/transport function | Nephron segment & membrane localization | Inheritance | Hallmark phenotypes/biochemical features | Notes/2023-2024 updates |
|---|---|---|---|---|---|---|
| Type I (antenatal/neonatal Bartter syndrome) | **SLC12A1** | NKCC2, apical Na\+-K\+-2Cl\- cotransporter mediating a major fraction of TAL NaCl reabsorption; loss impairs lumen-positive voltage and downstream paracellular Ca2\+/Mg2\+ reabsorption (alla2023ararepresentation pages 2-3, thimm2024untanglingtheuncertain pages 4-6, laghmani2024proteinqualitycontrol pages 1-2) | Thick ascending limb (TAL), **apical membrane** of tubular epithelial cells; NKCC2 splice variants localize to medullary/cortical TAL and macula densa (thimm2024untanglingtheuncertain pages 4-6, laghmani2024proteinqualitycontrol pages 1-2) | Usually autosomal recessive (qasba2023barttersyndromea pages 1-2, thimm2024sodiumdeficiencydiseases pages 5-9) | Antenatal/neonatal presentation, polyhydramnios, prematurity, severe salt wasting, hypokalemic hypochloremic metabolic alkalosis, hyperreninemia/hyperaldosteronism, often hypercalciuria/nephrocalcinosis (choi2023longtermoutcomeof pages 1-2, qasba2023barttersyndromea pages 2-5, thimm2024untanglingtheuncertain pages 4-6) | 2024 mechanistic update: NKCC2 maturation is regulated by **ER export/protein quality control**; ER retention and **ER-associated degradation (ERAD)** are implicated in severe prenatal disease biology (laghmani2024proteinqualitycontrol pages 1-2) |
| Type II (antenatal Bartter syndrome) | **KCNJ1** | ROMK, apical inwardly rectifying K\+ channel recycling K\+ into tubular lumen to support NKCC2 activity and lumen-positive voltage (alla2023ararepresentation pages 2-3, thimm2024untanglingtheuncertain pages 4-6, laghmani2024proteinqualitycontrol pages 1-2) | TAL, **apical membrane** (thimm2024untanglingtheuncertain pages 4-6, laghmani2024proteinqualitycontrol pages 1-2) | Usually autosomal recessive (qasba2023barttersyndromea pages 1-2, thimm2024sodiumdeficiencydiseases pages 5-9) | Antenatal/neonatal salt wasting, hypokalemic metabolic alkalosis, hyperreninemia/hyperaldosteronism, polyhydramnios/prematurity; may have hypercalciuria/nephrocalcinosis (qasba2023barttersyndromea pages 2-5, thimm2024untanglingtheuncertain pages 4-6, choi2023longtermoutcomeof pages 1-2) | 2023-2024 literature continues to classify ROMK disease as neonatal/antenatal BS with RAAS activation and prostaglandin-linked physiology; no major subtype-specific therapeutic advance identified in gathered evidence (thimm2024untanglingtheuncertain pages 4-6, thimm2024untanglingtheuncertain pages 6-6) |
| Type III (classic Bartter syndrome) | **CLCNKB** | ClC-Kb chloride channel enabling basolateral chloride efflux from tubular epithelial cells to interstitium (zhou2023amosaicmutation pages 1-2) | Mainly TAL; **basolateral membrane** chloride channel in renal tubular epithelial cells (thimm2024untanglingtheuncertain pages 4-6, zhou2023amosaicmutation pages 1-2) | Usually autosomal recessive (qasba2023barttersyndromea pages 1-2, zhou2023amosaicmutation pages 1-2) | Often childhood-onset but can present later; hypokalemia, hypochloremic metabolic alkalosis, renal salt wasting, hyperreninemia/hyperaldosteronism with normal blood pressure, polyuria, polydipsia, failure to thrive; urinary calcium may be variable and overlap with Gitelman syndrome (zhou2023amosaicmutation pages 1-2, jiang2024adultclassicbartter pages 1-2) | Largest recent cohort signal: in Korean multicenter study, **33/39 genetically confirmed** cases had CLCNKB variants; CLCNKB was the dominant genotype, and a CLCNKB **W610X (c.1830G>A)** allele accounted for ~40-50% of alleles, suggesting a founder effect in Korea (choi2023longtermoutcomeof pages 4-6, choi2023longtermoutcomeof pages 1-2). 2023 case report described a **mosaic** CLCNKB nonsense variant with frameshift in a newborn; 2024 adult case reported homozygous **c.1052G>T (p.Arg351Leu)** and emphasized genetic testing for BS vs GS (zhou2023amosaicmutation pages 1-2, jiang2024adultclassicbartter pages 1-2) |
| Type IVa (Bartter syndrome with sensorineural deafness) | **BSND** | Barttin, accessory \β-subunit required for ClC-Ka/ClC-Kb chloride channel function (qasba2023barttersyndromea pages 2-5, thimm2024untanglingtheuncertain pages 4-6, zhou2023amosaicmutation pages 1-2) | TAL/basolateral chloride channel complex in kidney; also inner ear involvement explaining deafness (qasba2023barttersyndromea pages 2-5, thimm2024untanglingtheuncertain pages 4-6) | Usually autosomal recessive (qasba2023barttersyndromea pages 1-2, qasba2023barttersyndromea pages 2-5) | Severe salt wasting, antenatal features/polyhydramnios, hypokalemic metabolic alkalosis, hyperreninemia/hyperaldosteronism, and **sensorineural hearing loss** (qasba2023barttersyndromea pages 2-5, thimm2024untanglingtheuncertain pages 4-6) | In the Korean cohort, hearing loss was present in **4/54 (7%)** overall at last follow-up, including the BSND case; one additional patient developed hearing loss during follow-up (choi2023longtermoutcomeof pages 4-6) |
| Type IVb (combined chloride channel defect) | **CLCNKA + CLCNKB** | Combined defect of ClC-Ka and ClC-Kb chloride channels causing severe chloride transport impairment (qasba2023barttersyndromea pages 2-5, zhou2023amosaicmutation pages 1-2) | TAL/basolateral chloride channel system; urinary concentrating defect noted in review evidence (qasba2023barttersyndromea pages 2-5) | Usually autosomal recessive/digenic combined defect in reported cases (qasba2023barttersyndromea pages 2-5) | Severe salt wasting, polyhydramnios, preterm delivery, impaired urinary concentrating ability, deafness/severe phenotype resembling type IV spectrum (qasba2023barttersyndromea pages 2-5) | 2023 systematic review highlighted type IVb as a rare but severe form due to dysfunction of **two chloride channels**, with deafness and marked antenatal disease (qasba2023barttersyndromea pages 2-5) |
| Type V / transient antenatal Bartter syndrome | **MAGED2** | MAGED2 supports transporter expression/trafficking under fetal hypoxia; maintains Gαs-cAMP/PKA signaling that promotes **NKCC2/NCC** function and protects them from degradation (yan2024identificationofa pages 4-6, yang2026identificationofthree pages 1-2) | Functional effect on fetal renal salt transport in TAL/DCT pathways; disease is transient and linked to intrauterine hypoxic conditions rather than permanent postnatal dysfunction (yan2024identificationofa pages 4-6, yang2026identificationofthree pages 1-2) | X-linked; mostly affects males, though skewed X-inactivation can make heterozygous females symptomatic (yan2024identificationofa pages 1-2, yan2024identificationofa pages 4-6) | Severe fetal polyuria causing **early severe polyhydramnios**, extreme prematurity, high perinatal risk; postnatal electrolyte abnormalities are often transient with spontaneous recovery in survivors (yan2024identificationofa pages 1-2, yan2024identificationofa pages 4-6, yan2024identificationofa pages 2-4) | 2024 update: novel intronic variant **c.1271+4_1271+7delAGTA** shown pathogenic by **minigene assay**, activating a cryptic splice site and inserting 96 bp into mRNA, creating premature termination and predicted loss of MAGED2-Hsp40 interaction; authors recommend WES/trio-WES and intronic analysis when severe polyhydramnios is present (yan2024identificationofa pages 1-2, yan2024identificationofa pages 4-6, yan2024identificationofa pages 2-4) |
| Bartter syndrome with hypocalcemia / Bartter-like subtype | **CASR** | Gain-of-function calcium-sensing receptor signaling alters TAL salt handling and calcium balance (thimm2024untanglingtheuncertain pages 4-6) | **Basolateral** CaSR in TAL tubular cells (thimm2024untanglingtheuncertain pages 4-6) | Reported as type V in some older classifications within gathered reviews; inheritance not fully detailed in gathered evidence table (qasba2023barttersyndromea pages 2-5, thimm2024untanglingtheuncertain pages 4-6) | Hypokalemic metabolic alkalosis with salt wasting plus **hypocalcemia** and hypercalciuria in Bartter-like phenotype (thimm2024untanglingtheuncertain pages 4-6) | Classification differs across sources: Qasba 2023 lists CASR-associated disease as type V, whereas newer literature separately emphasizes MAGED2-associated transient antenatal BS; this reflects evolving nomenclature rather than a resolved consensus in the gathered evidence (qasba2023barttersyndromea pages 2-5, yan2024identificationofa pages 1-2, yang2026identificationofthree pages 1-2) |


*Table: This table summarizes the major genetic subtypes of Bartter syndrome, linking each gene to transporter function, nephron localization, inheritance, and clinical hallmarks. It also highlights recent 2023-2024 updates from cohort, mechanistic, and prenatal genetics studies.*

**Inheritance pattern**: Types 1–4 are predominantly autosomal recessive; **MAGED2‑related transient antenatal BS is X‑linked** (noted in contemporary discussions of transient antenatal BS). (qasba2023barttersyndromea pages 1-2, yan2024identificationofa pages 4-6)

### 4.2 Pathogenic variant classes and examples (recently reported)
- **CLCNKB (type III/classic BS)**
  - A 2023 case report described compound changes including a frameshift **c.1257delC (p.M421Cfs*58)** plus a **low‑level mosaic** nonsense **c.595G>T (p.E199*)**. (Frontiers in Pediatrics; 2023-04; https://doi.org/10.3389/fped.2023.1034923) (zhou2023amosaicmutation pages 1-2)
  - A 2024 adult case report reported a homozygous missense **CLCNKB c.1052G>T (p.Arg351Leu)**, emphasizing genetic testing when adult onset mimics Gitelman syndrome. (Endocrine Journal; 2024-03; https://doi.org/10.1507/endocrj.ej23-0631) (jiang2024adultclassicbartter pages 1-2)
- **MAGED2 (transient antenatal BS)**
  - A 2024 study identified a novel intronic deletion **MAGED2 c.1271+4_1271+7delAGTA** and showed, via **minigene assay**, activation of a cryptic splice site producing a 96 bp insertion in mature mRNA with premature termination. (BMC Medical Genomics; 2024-01; https://doi.org/10.1186/s12920-024-01797-8) (yan2024identificationofa pages 1-2, yan2024identificationofa pages 2-4)

### 4.3 Modifier genes / epigenetics
Not systematically characterized for BS in the retrieved 2023–2024 evidence. Some mechanistic discussions suggest that protein quality control pathways (ER export/ERAD) can modify transporter abundance and thus phenotype severity (e.g., NKCC2). (laghmani2024proteinqualitycontrol pages 1-2)

---

## 5. Environmental information
Bartter syndrome is primarily genetic; the retrieved sources emphasize differential diagnoses and phenocopies rather than environmental causation. Pseudo‑Bartter syndromes/phenocopies include cystic fibrosis and nephrotoxic drug exposures (e.g., aminoglycosides, amphotericin B, heavy metals). (alla2023ararepresentation pages 2-3)

---

## 6. Mechanism / pathophysiology

### 6.1 Causal chain (transport defect → biochemical phenotype)
1. **Primary transporter/channel dysfunction** in TAL salt reabsorption (NKCC2/ROMK/ClC-K/barttin; or regulatory mechanisms in transient antenatal BS). (thimm2024untanglingtheuncertain pages 4-6, laghmani2024proteinqualitycontrol pages 1-2, yan2024identificationofa pages 4-6)
2. **Renal salt wasting and volume depletion** → compensatory **RAAS activation** (hyperreninemia/hyperaldosteronism; juxtaglomerular apparatus hyperplasia in classic descriptions). (alla2023ararepresentation pages 2-3, thimm2024untanglingtheuncertain pages 4-6)
3. **Increased distal Na+ delivery** → enhanced ENaC-mediated Na+ uptake coupled to **K+ and H+ secretion** → **hypokalemia and metabolic alkalosis**. (alla2023ararepresentation pages 2-3)
4. TAL electrical/ionic changes can reduce lumen‑positive voltage, contributing to **hypercalciuria** and risk of **nephrocalcinosis**. (alla2023ararepresentation pages 2-3, laghmani2024proteinqualitycontrol pages 1-2)

### 6.2 Molecular and cellular processes (GO suggestions)
Evidence-supported processes from 2024 mechanistic literature include:
- **Protein folding / ER quality control / ERAD** regulating NKCC2 maturation and apical abundance (suggest GO: *protein folding*, *ER-associated protein catabolic process*). (laghmani2024proteinqualitycontrol pages 1-2)
- **Ion transport** (suggest GO: *sodium ion transmembrane transport*, *chloride transmembrane transport*, *potassium ion transport*). (laghmani2024proteinqualitycontrol pages 1-2, zhou2023amosaicmutation pages 1-2)
- **Renin–angiotensin–aldosterone system regulation** (suggest GO: *regulation of systemic arterial blood pressure*, *renin secretion*). (thimm2024untanglingtheuncertain pages 4-6)

### 6.3 Cell types (Cell Ontology suggestions)
Primary affected cell types in the retrieved mechanistic evidence:
- **Kidney TAL epithelial cells** (CL: *renal epithelial cell*; tissue‑specific annotation may use “thick ascending limb of loop of Henle epithelial cell” where available) (thimm2024untanglingtheuncertain pages 4-6, laghmani2024proteinqualitycontrol pages 1-2)
- **Macula densa cells** (NKCC2 splice variants noted in macula densa) (laghmani2024proteinqualitycontrol pages 1-2)

### 6.4 Anatomical structures (UBERON suggestions)
- **Kidney** (UBERON: *kidney*) and specifically:
  - **Loop of Henle—thick ascending limb** (UBERON term for TAL/loop of Henle segment) (thimm2024untanglingtheuncertain pages 4-6, laghmani2024proteinqualitycontrol pages 1-2)
  - **Distal convoluted tubule** (relevant especially for transient antenatal BS affecting NCC regulation) (yan2024identificationofa pages 4-6)

### 6.5 Recent mechanistic developments (2023–2024)
- **NKCC2 protein quality control**: A 2024 review highlights ER export as a rate‑limiting step in NKCC2 maturation and that ER retention/ERAD can prevent NKCC2 detection at the apical membrane in severe prenatal disease contexts, motivating interest in trafficking/quality‑control determinants. (Cells; 2024-05; https://doi.org/10.3390/cells13100818) (laghmani2024proteinqualitycontrol pages 1-2)
- **MAGED2 transient antenatal BS**: A 2024 functional genetics study supports that intronic splice‑altering variants can be pathogenic and suggests a molecular link to protection of NKCC2/NCC from ERAD (based on modeling/functional splicing results), consistent with a fetal‑environment–dependent mechanism. (yan2024identificationofa pages 4-6, yan2024identificationofa pages 2-4)

---

## 7. Anatomical structures affected

### 7.1 Primary organs/systems
- **Renal**: TAL and related salt handling segments are central. (thimm2024untanglingtheuncertain pages 4-6, laghmani2024proteinqualitycontrol pages 1-2)
- **Auditory system**: in BS type IV (BSND/barttin), **sensorineural hearing loss** is a defining complication. (choi2023longtermoutcomeof pages 4-6, nomura2013treatmentwith17allylamino17demethoxygeldanamycin pages 5-6)

### 7.2 Subcellular localization
- NKCC2: apical membrane; maturation/trafficking depend on ER export/quality control. (laghmani2024proteinqualitycontrol pages 1-2)
- ClC-Kb: basolateral membrane chloride efflux pathway in TAL epithelial cells. (zhou2023amosaicmutation pages 1-2)

---

## 8. Temporal development

### 8.1 Onset
- Often **neonatal/infantile**: Korean cohort median diagnosis age **5 months** (range 0–271 months). (choi2023longtermoutcomeof pages 1-2)
- **Antenatal**: polyhydramnios/prematurity are common in antenatal forms; MAGED2-related disease can be detected around ~20 weeks gestation with severe polyhydramnios. (choi2023longtermoutcomeof pages 2-3, yan2024identificationofa pages 2-4)
- **Adult onset is uncommon but documented**, typically requiring genetic testing to distinguish from Gitelman syndrome. (jiang2024adultclassicbartter pages 1-2)

### 8.2 Progression and course
Long-term cohort evidence indicates partial improvement in supplementation needs with age (potassium dosing declining from infancy to adolescence), yet a clinically meaningful minority develop CKD and growth impairment persists in many. (choi2023longtermoutcomeof pages 4-6)

---

## 9. Inheritance and population

### 9.1 Epidemiology
A 2023 multicenter cohort review text states a prevalence estimate of approximately **~1 in 100,000**. (choi2023longtermoutcomeof pages 1-2)

### 9.2 Population genetics / founder effects
In the Korean multicenter cohort, **CLCNKB** was the dominant genotype (33/39 genetically confirmed), and a CLCNKB **W610X (c.1830G>A)** variant accounted for ~40–50% of alleles, consistent with a possible founder effect in Korea. (choi2023longtermoutcomeof pages 4-6, choi2023longtermoutcomeof pages 1-2)

### 9.3 Sex ratio
In the 54‑patient Korean cohort the sex distribution was **33 male : 21 female**. (choi2023longtermoutcomeof pages 2-3)

---

## 10. Diagnostics

### 10.1 Clinical testing (lab features)
Evidence-based diagnostic features include:
- Serum: low K+, low Cl−, metabolic alkalosis (ABG), and often elevated renin/aldosterone. (alla2023ararepresentation pages 2-3, choi2023longtermoutcomeof pages 1-2)
- Urine: urinary electrolyte wasting; **24-hour urinary calcium** is useful to differentiate BS (often normal/high urinary Ca) from Gitelman syndrome (hypocalciuria), though overlap exists. (alla2023ararepresentation pages 2-3, das2024barttersyndromewith pages 2-5)
- Imaging: renal ultrasound for **nephrocalcinosis**. (jiang2024adultclassicbartter pages 1-2, choi2023longtermoutcomeof pages 4-6)

### 10.2 Genetic testing approach
Modern sources emphasize next-generation sequencing (NGS)–based multi‑gene testing because phenotypes overlap across BS types and with Gitelman syndrome. Panels commonly include **SLC12A1, KCNJ1, CLCNKB, CLCNKA, BSND, MAGED2**. (alla2023ararepresentation pages 2-3, das2024barttersyndromewith pages 2-5)

For severe prenatal polyhydramnios suggestive of transient antenatal BS, 2024 evidence supports WES/trio‑WES and careful intronic analysis; a minigene assay established pathogenic splicing for an intronic MAGED2 deletion. (yan2024identificationofa pages 4-6, yan2024identificationofa pages 2-4)

### 10.3 Differential diagnosis
- **Gitelman syndrome**: typically hypomagnesemia and hypocalciuria; BS often has normal Mg and normal/high urinary Ca; neonatal polyhydramnios supports BS. (das2024barttersyndromewith pages 2-5, thimm2024untanglingtheuncertain pages 6-6)
- **Pseudo‑Bartter**: cystic fibrosis and nephrotoxic exposures can mimic biochemical phenotype. (alla2023ararepresentation pages 2-3, alla2023ararepresentation pages 3-4)

**Figure/table evidence**: The extracted Table/Figure images from a 2024 review visually summarize genotype–phenotype distinctions and gene/subtype mapping. (thimm2024untanglingtheuncertain media ca88ecd5, thimm2024untanglingtheuncertain media 317ad3d1, thimm2024untanglingtheuncertain media 1cbedca4)

---

## 11. Outcome / prognosis

### 11.1 Long-term outcomes (statistics from 2023 multicenter cohort)
In the Korean 54‑patient study (median follow-up 8 years):
- **Short stature**: 41% (22/54) at last follow-up (choi2023longtermoutcomeof pages 4-6)
- **CKD (G3–G5)**: 11% overall (6/54) (choi2023longtermoutcomeof pages 4-6)
- **Nephrocalcinosis**: 35% at last follow-up (15/43) (choi2023longtermoutcomeof pages 4-6)
- **Sensorineural hearing loss**: 7% (4/54) (choi2023longtermoutcomeof pages 4-6)
- **Developmental delay**: 15% (8/54) (choi2023longtermoutcomeof pages 4-6)

The cohort also observed decreasing potassium needs with age and noted potential contributors to CKD (nephrocalcinosis, prolonged NSAID use, chronic hypokalemia, prematurity), though causal attribution is not definitive in this retrospective design. (choi2023longtermoutcomeof pages 4-6)

---

## 12. Treatment

### 12.1 Standard-of-care pharmacotherapy and supportive care (current practice)
Treatment is largely symptomatic, aiming to prevent dehydration and correct electrolyte/acid–base disturbance:
- **Potassium chloride supplementation** and often sodium supplementation (choi2023longtermoutcomeof pages 4-6)
- **NSAIDs** (e.g., indomethacin/ibuprofen/celecoxib) to counter prostaglandin-mediated renal losses; a 2023 cohort found no clear outcome differences among NSAID types used. (choi2023longtermoutcomeof pages 4-6)
- **Potassium-sparing agents** (spironolactone/eplerenone/amiloride) used in many settings, but one cohort cautions against routine use because of possible worsening salt wasting/polyuria. (choi2023longtermoutcomeof pages 4-6, alla2023ararepresentation pages 2-3)
- **ACE inhibitors/ARBs**: sometimes used (e.g., with proteinuria), but may risk hypotension/prerenal AKI in salt-wasting states. (alla2023ararepresentation pages 2-3)

**Real-world implementation (cohort statistics)**: In the Korean 54‑patient cohort, **94%** received potassium chloride supplementation and **68%** received potassium‑sparing diuretics; mean KCl dosing was **5.0 mEq/day/kg** in patients <18 years and **2.1 mEq/day/kg** in adults. (choi2023longtermoutcomeof pages 1-2)

### 12.2 Experimental/precision approaches (model-driven)
A BsndR8L/R8L knock-in mouse model of Bartter type IV demonstrated that pharmacologic chaperoning via the Hsp90 inhibitor **17‑AAG** improved membrane localization of mutant barttin and ameliorated low-salt–induced metabolic alkalosis/hypokalemia and partially rescued hearing after one week. (Biochem Biophys Res Commun; 2013-11; https://doi.org/10.1016/j.bbrc.2013.10.129) (nomura2013treatmentwith17allylamino17demethoxygeldanamycin pages 5-6)

### 12.3 Clinical trials (ClinicalTrials.gov)
- **NCT03847571** (first posted 2019-02-20; Tehran University of Medical Sciences): “Acetazolamide (AZ) for Management of Alkalosis in Bartter Syndrome” evaluates oral acetazolamide **5 mg/kg/day** for 4 weeks in a prospective case‑crossover observational design (estimated n=20; ages 1–10). Primary outcomes include change in serum bicarbonate and 24‑hour urine volume. (https://clinicaltrials.gov/study/NCT03847571) (NCT03847571 chunk 1)
- **NCT01021280** (planned 2013-01 start; Soroka University Medical Center): observational case‑control study of “Parathyroid Hormone (PTH) Homeostasis in Bartter Syndrome” using controlled calcium manipulations to study PTH regulation in BS type II vs type IV. Purpose statement includes the quote: “**to investigate the PT-gland function and regulation in BS**.” (https://clinicaltrials.gov/study/NCT01021280) (NCT01021280 chunk 1)

### 12.4 Suggested MAXO terms (non-exhaustive)
- Potassium supplementation: MAXO concept for electrolyte replacement therapy (supported by cohort practice). (choi2023longtermoutcomeof pages 1-2)
- NSAID therapy (prostaglandin inhibition) (choi2023longtermoutcomeof pages 4-6)
- Potassium-sparing diuretic therapy (choi2023longtermoutcomeof pages 1-2)
- Prenatal amnioreduction / indomethacin for severe polyhydramnios in MAGED2-related disease (yan2024identificationofa pages 1-2)

---

## 13. Prevention

### 13.1 Primary prevention
Not applicable in the classic public-health sense for most autosomal recessive BS. Primary prevention is largely limited to **reproductive counseling** and **carrier testing** in at-risk families.

### 13.2 Secondary prevention
- Early recognition and treatment of dehydration/electrolyte disturbance in neonates/infants to prevent acute kidney injury and complications. (choi2023longtermoutcomeof pages 4-6)
- Prenatal surveillance when severe polyhydramnios is present; for MAGED2-related disease, prenatal genetic diagnosis and management (indomethacin and amnioreduction described) may reduce prematurity-associated morbidity in selected cases. (yan2024identificationofa pages 1-2)

### 13.3 Tertiary prevention
- Prevent CKD progression by managing chronic hypokalemia, nephrocalcinosis risk, and avoiding iatrogenic hypotension or nephrotoxicity; cohort authors highlight these as plausible contributors to CKD. (choi2023longtermoutcomeof pages 4-6)

---

## 14. Other species / natural disease
A naturally occurring large-animal phenotype linked to SLC12A1 illustrates conserved biology:
- **Japanese Black cattle hydrallantois**: a recessive SLC12A1 missense variant (p.Pro372Leu) disrupts apical NKCC2 localization in fetal kidneys, causing impaired urine concentration and fetal polyuria with accumulation of urine in the allantoic cavity (hydrallantois). (BMC Genomics; 2016-09; https://doi.org/10.1186/s12864-016-3035-1) (sasaki2016amissensemutation pages 1-2, sasaki2016amissensemutation pages 11-12)

---

## 15. Model organisms

### 15.1 Mouse models (Slc12a1/NKCC2)
Multiple mouse models recapitulate aspects of type I Bartter syndrome, with phenotype severity depending on allele:
- ENU-derived **Slc12a1I299F** mice show “**MOUSE MODEL OF BARTTER SYNDROME**” features including severe polyuria and a urea-selective concentrating defect; they also show metabolic alkalosis, hypotension and other systemic features, while not always reproducing hyperreninemia. (Am J Physiol Renal Physiol; 2010-06; https://doi.org/10.1152/ajprenal.00522.2009) (kemter2010mutationofthe pages 3-4, kemter2010mutationofthe pages 1-2)
- Systematic phenotyping of Slc12a1I299F homozygotes reported kidney defects “highly similar to the late-onset manifestation” of human disease and additional phenotypes (low blood pressure, osteopenia, reduced body weight/fat). (J Biomed Sci; 2014-08; https://doi.org/10.1186/s12929-014-0068-0) (kemter2014standardizedsystemicphenotypic pages 1-2)

### 15.2 Mouse models (Bsnd/barttin) and therapeutic proof-of-concept
A BsndR8L/R8L knock-in mouse provides a model of type IV disease and supports therapeutic rescue via chaperone modulation (17‑AAG) with improvements in renal and auditory phenotypes. (nomura2013treatmentwith17allylamino17demethoxygeldanamycin pages 5-6)

---

## Expert opinion and analysis (authoritative synthesis from recent sources)
1. **Genetic testing is central** because adult-onset or atypical BS can mimic Gitelman syndrome; 2024 adult case literature explicitly frames genetic diagnosis as decisive for differential diagnosis and management. (jiang2024adultclassicbartter pages 1-2)
2. **Long-term morbidity is non-trivial**: even with treatment, 2023 multicenter cohort evidence shows high residual rates of growth impairment (41%) and measurable CKD risk (11%). (choi2023longtermoutcomeof pages 4-6)
3. **Mechanistic emphasis is shifting toward trafficking/quality control**: 2024 mechanistic review positions ER export/ERAD of NKCC2 as a key regulatory node, which is conceptually aligned with emerging chaperone-based strategies demonstrated for barttin in animal models. (laghmani2024proteinqualitycontrol pages 1-2, nomura2013treatmentwith17allylamino17demethoxygeldanamycin pages 5-6)

---

## Data/statistics highlights (recent)
- Korean multicenter cohort (Frontiers in Medicine; 2023-03): polyhydramnios 47% (18/38), preterm birth 28% (13/46), nephrocalcinosis 41% at presentation (17/41) and 35% at last visit (15/43), short stature 41% (22/54), developmental delay 15% (8/54), hearing loss 7% (4/54), CKD 11% (6/54). (choi2023longtermoutcomeof pages 2-3, choi2023longtermoutcomeof pages 4-6)
- Treatment utilization in that cohort: KCl 94%, potassium-sparing agents 68%, mean KCl dose 5.0 mEq/day/kg (<18y) and 2.1 mEq/day/kg (adults). (choi2023longtermoutcomeof pages 1-2)

---

## Limitations of this report (evidence access constraints)
- ICD-10/ICD-11, Orphanet disease IDs, and MeSH identifiers were not present in the retrieved full texts; these require direct extraction from those respective terminologies.
- Some mechanistic and variant-spectrum statements in secondary reviews cite additional primary sources that were not fully retrieved in this run; therefore, this report prioritizes claims directly supported by the cited context IDs.


References

1. (choi2023longtermoutcomeof pages 1-2): Naye Choi, Seong Heon Kim, Eun Hui Bae, Eun Mi Yang, Keum Hwa Lee, Sang-Ho Lee, Joo Hoon Lee, Yo Han Ahn, Hae Il Cheong, Hee Gyung Kang, Hye Sun Hyun, and Ji Hyun Kim. Long-term outcome of bartter syndrome in 54 patients: a multicenter study in korea. Frontiers in Medicine, Mar 2023. URL: https://doi.org/10.3389/fmed.2023.1099840, doi:10.3389/fmed.2023.1099840. This article has 12 citations.

2. (laghmani2024proteinqualitycontrol pages 1-2): Kamel Laghmani. Protein quality control of nkcc2 in bartter syndrome and blood pressure regulation. Cells, 13:818, May 2024. URL: https://doi.org/10.3390/cells13100818, doi:10.3390/cells13100818. This article has 0 citations.

3. (yan2024identificationofa pages 1-2): Xu Yan, Yueyue Hu, Xin Zhang, Xia Gao, Yang Zhao, Haiying Peng, Liu Ouyang, and Changjun Zhang. Identification of a novel intronic mutation of maged2 gene in a chinese family with antenatal bartter syndrome. BMC Medical Genomics, Jan 2024. URL: https://doi.org/10.1186/s12920-024-01797-8, doi:10.1186/s12920-024-01797-8. This article has 5 citations and is from a peer-reviewed journal.

4. (alla2023ararepresentation pages 2-3): Deekshitha Alla, Meghana Krishna Kesineni, Roopeessh Vempati, Hinal Patel, Shenelle Menezes, Sai Santhosha Mrudula Alla, Devkumar Patel, Srajan Gupta, Krish Patel, and Anju Pradeep. A rare presentation of adult-onset bartter syndrome: a case report. Cureus, Mar 2023. URL: https://doi.org/10.7759/cureus.36120, doi:10.7759/cureus.36120. This article has 6 citations.

5. (yang2026identificationofthree pages 12-14): Shu-fa Yang, Xiaojuan Li, Haili Jiang, Jiahui Cheng, Changlong Li, Xinyi Xie, and Xiaoqin Xiao. Identification of three novel maged2 variants causing antenatal bartter syndrome in three chinese families. Genes, 17:424, Apr 2026. URL: https://doi.org/10.3390/genes17040424, doi:10.3390/genes17040424. This article has 0 citations.

6. (zhou2023amosaicmutation pages 1-2): Lan Zhou, Xiaohui Chen, Jiao-Jiao Xiong, and Ling Lei. A mosaic mutation in the clcnkb gene causing bartter syndrome: a case report. Frontiers in Pediatrics, Apr 2023. URL: https://doi.org/10.3389/fped.2023.1034923, doi:10.3389/fped.2023.1034923. This article has 4 citations.

7. (qasba2023barttersyndromea pages 2-5): Rakhtan K. Qasba, Anna Carolina Flumignan Bucharles, Maria Victoria Ferreira Piccoli, Pranjal Sharma, Akshat Banga, Balakrishnan Kamaraj, Faisal A. Nawaz, Harshadayani Jagadish Kumar, Mahika Afrin Happy, Ruman K. Qasba, Gowthami Sai Kogilathota Jagirdhar, Mohammad Yasir Essar, Piyush Garg, Shiva Teja Reddy, Kaanthi Rama, Salim Surani, and Rahul Kashyap. Bartter syndrome: a systematic review of case reports and case series. Medicina, 59:1638, Sep 2023. URL: https://doi.org/10.3390/medicina59091638, doi:10.3390/medicina59091638. This article has 26 citations.

8. (jiang2024adultclassicbartter pages 1-2): Le Jiang, Dongmei Li, Qiansha Guo, Yunfeng Li, Lei Zan, and Rihan Ao. Adult classic bartter syndrome: a case report with 5-year follow-up and literature review. Endocrine journal, 71:537-542, Mar 2024. URL: https://doi.org/10.1507/endocrj.ej23-0631, doi:10.1507/endocrj.ej23-0631. This article has 6 citations and is from a peer-reviewed journal.

9. (qasba2023barttersyndromea pages 1-2): Rakhtan K. Qasba, Anna Carolina Flumignan Bucharles, Maria Victoria Ferreira Piccoli, Pranjal Sharma, Akshat Banga, Balakrishnan Kamaraj, Faisal A. Nawaz, Harshadayani Jagadish Kumar, Mahika Afrin Happy, Ruman K. Qasba, Gowthami Sai Kogilathota Jagirdhar, Mohammad Yasir Essar, Piyush Garg, Shiva Teja Reddy, Kaanthi Rama, Salim Surani, and Rahul Kashyap. Bartter syndrome: a systematic review of case reports and case series. Medicina, 59:1638, Sep 2023. URL: https://doi.org/10.3390/medicina59091638, doi:10.3390/medicina59091638. This article has 26 citations.

10. (thimm2024untanglingtheuncertain pages 4-6): Chantelle Thimm and James Adjaye. Untangling the uncertain role of overactivation of the renin–angiotensin–aldosterone system with the aging process based on sodium wasting human models. International Journal of Molecular Sciences, 25:9332, Aug 2024. URL: https://doi.org/10.3390/ijms25179332, doi:10.3390/ijms25179332. This article has 6 citations.

11. (choi2023longtermoutcomeof pages 4-6): Naye Choi, Seong Heon Kim, Eun Hui Bae, Eun Mi Yang, Keum Hwa Lee, Sang-Ho Lee, Joo Hoon Lee, Yo Han Ahn, Hae Il Cheong, Hee Gyung Kang, Hye Sun Hyun, and Ji Hyun Kim. Long-term outcome of bartter syndrome in 54 patients: a multicenter study in korea. Frontiers in Medicine, Mar 2023. URL: https://doi.org/10.3389/fmed.2023.1099840, doi:10.3389/fmed.2023.1099840. This article has 12 citations.

12. (yan2024identificationofa pages 4-6): Xu Yan, Yueyue Hu, Xin Zhang, Xia Gao, Yang Zhao, Haiying Peng, Liu Ouyang, and Changjun Zhang. Identification of a novel intronic mutation of maged2 gene in a chinese family with antenatal bartter syndrome. BMC Medical Genomics, Jan 2024. URL: https://doi.org/10.1186/s12920-024-01797-8, doi:10.1186/s12920-024-01797-8. This article has 5 citations and is from a peer-reviewed journal.

13. (choi2023longtermoutcomeof pages 2-3): Naye Choi, Seong Heon Kim, Eun Hui Bae, Eun Mi Yang, Keum Hwa Lee, Sang-Ho Lee, Joo Hoon Lee, Yo Han Ahn, Hae Il Cheong, Hee Gyung Kang, Hye Sun Hyun, and Ji Hyun Kim. Long-term outcome of bartter syndrome in 54 patients: a multicenter study in korea. Frontiers in Medicine, Mar 2023. URL: https://doi.org/10.3389/fmed.2023.1099840, doi:10.3389/fmed.2023.1099840. This article has 12 citations.

14. (thimm2024sodiumdeficiencydiseases pages 5-9): Chantelle Thimm and James Adjaye. Sodium deficiency diseases: the association with the renin-angiotensin-aldosterone system, aging and inflammation. Jul 2024. URL: https://doi.org/10.20944/preprints202407.1238.v1, doi:10.20944/preprints202407.1238.v1.

15. (thimm2024untanglingtheuncertain pages 6-6): Chantelle Thimm and James Adjaye. Untangling the uncertain role of overactivation of the renin–angiotensin–aldosterone system with the aging process based on sodium wasting human models. International Journal of Molecular Sciences, 25:9332, Aug 2024. URL: https://doi.org/10.3390/ijms25179332, doi:10.3390/ijms25179332. This article has 6 citations.

16. (yang2026identificationofthree pages 1-2): Shu-fa Yang, Xiaojuan Li, Haili Jiang, Jiahui Cheng, Changlong Li, Xinyi Xie, and Xiaoqin Xiao. Identification of three novel maged2 variants causing antenatal bartter syndrome in three chinese families. Genes, 17:424, Apr 2026. URL: https://doi.org/10.3390/genes17040424, doi:10.3390/genes17040424. This article has 0 citations.

17. (yan2024identificationofa pages 2-4): Xu Yan, Yueyue Hu, Xin Zhang, Xia Gao, Yang Zhao, Haiying Peng, Liu Ouyang, and Changjun Zhang. Identification of a novel intronic mutation of maged2 gene in a chinese family with antenatal bartter syndrome. BMC Medical Genomics, Jan 2024. URL: https://doi.org/10.1186/s12920-024-01797-8, doi:10.1186/s12920-024-01797-8. This article has 5 citations and is from a peer-reviewed journal.

18. (nomura2013treatmentwith17allylamino17demethoxygeldanamycin pages 5-6): Naohiro Nomura, Kazusaku Kamiya, Katsuhisa Ikeda, Naofumi Yui, Motoko Chiga, Eisei Sohara, Tatemitu Rai, Sei Sakaki, and Shinich Uchida. Treatment with 17-allylamino-17-demethoxygeldanamycin ameliorated symptoms of bartter syndrome type iv caused by mutated bsnd in mice. Biochemical and biophysical research communications, 441 3:544-9, Nov 2013. URL: https://doi.org/10.1016/j.bbrc.2013.10.129, doi:10.1016/j.bbrc.2013.10.129. This article has 19 citations and is from a peer-reviewed journal.

19. (das2024barttersyndromewith pages 2-5): Arki Das, Rohini R, and Somnath Panda. Bartter syndrome with recurrent hypokalemic periodic paralysis: a case report. Cureus, Oct 2024. URL: https://doi.org/10.7759/cureus.72406, doi:10.7759/cureus.72406. This article has 1 citations.

20. (alla2023ararepresentation pages 3-4): Deekshitha Alla, Meghana Krishna Kesineni, Roopeessh Vempati, Hinal Patel, Shenelle Menezes, Sai Santhosha Mrudula Alla, Devkumar Patel, Srajan Gupta, Krish Patel, and Anju Pradeep. A rare presentation of adult-onset bartter syndrome: a case report. Cureus, Mar 2023. URL: https://doi.org/10.7759/cureus.36120, doi:10.7759/cureus.36120. This article has 6 citations.

21. (thimm2024untanglingtheuncertain media ca88ecd5): Chantelle Thimm and James Adjaye. Untangling the uncertain role of overactivation of the renin–angiotensin–aldosterone system with the aging process based on sodium wasting human models. International Journal of Molecular Sciences, 25:9332, Aug 2024. URL: https://doi.org/10.3390/ijms25179332, doi:10.3390/ijms25179332. This article has 6 citations.

22. (thimm2024untanglingtheuncertain media 317ad3d1): Chantelle Thimm and James Adjaye. Untangling the uncertain role of overactivation of the renin–angiotensin–aldosterone system with the aging process based on sodium wasting human models. International Journal of Molecular Sciences, 25:9332, Aug 2024. URL: https://doi.org/10.3390/ijms25179332, doi:10.3390/ijms25179332. This article has 6 citations.

23. (thimm2024untanglingtheuncertain media 1cbedca4): Chantelle Thimm and James Adjaye. Untangling the uncertain role of overactivation of the renin–angiotensin–aldosterone system with the aging process based on sodium wasting human models. International Journal of Molecular Sciences, 25:9332, Aug 2024. URL: https://doi.org/10.3390/ijms25179332, doi:10.3390/ijms25179332. This article has 6 citations.

24. (NCT03847571 chunk 1):  Acetazolamide (AZ) for Management of Alkalosis in Bartter Syndrome. Tehran University of Medical Sciences. 2019. ClinicalTrials.gov Identifier: NCT03847571

25. (NCT01021280 chunk 1): Daniel Landau MD. Parathyroid Hormone (PTH) Homeostasis in Bartter Syndrome. Soroka University Medical Center. 2013. ClinicalTrials.gov Identifier: NCT01021280

26. (sasaki2016amissensemutation pages 1-2): Shinji Sasaki, Kiyotoshi Hasegawa, Tomoko Higashi, Yutaka Suzuki, Sumio Sugano, Yasuaki Yasuda, and Yoshikazu Sugimoto. A missense mutation in solute carrier family 12, member 1 (slc12a1) causes hydrallantois in japanese black cattle. BMC Genomics, Sep 2016. URL: https://doi.org/10.1186/s12864-016-3035-1, doi:10.1186/s12864-016-3035-1. This article has 28 citations and is from a peer-reviewed journal.

27. (sasaki2016amissensemutation pages 11-12): Shinji Sasaki, Kiyotoshi Hasegawa, Tomoko Higashi, Yutaka Suzuki, Sumio Sugano, Yasuaki Yasuda, and Yoshikazu Sugimoto. A missense mutation in solute carrier family 12, member 1 (slc12a1) causes hydrallantois in japanese black cattle. BMC Genomics, Sep 2016. URL: https://doi.org/10.1186/s12864-016-3035-1, doi:10.1186/s12864-016-3035-1. This article has 28 citations and is from a peer-reviewed journal.

28. (kemter2010mutationofthe pages 3-4): Elisabeth Kemter, Birgit Rathkolb, Lise Bankir, Anja Schrewe, Wolfgang Hans, Christina Landbrecht, Matthias Klaften, Boris Ivandic, Helmut Fuchs, Valérie Gailus-Durner, Martin Hrabé de Angelis, Eckhard Wolf, Ruediger Wanke, and Bernhard Aigner. Mutation of the na(+)-k(+)-2cl(-) cotransporter nkcc2 in mice is associated with severe polyuria and a urea-selective concentrating defect without hyperreninemia. American journal of physiology. Renal physiology, 298 6:F1405-15, Jun 2010. URL: https://doi.org/10.1152/ajprenal.00522.2009, doi:10.1152/ajprenal.00522.2009. This article has 48 citations.

29. (kemter2010mutationofthe pages 1-2): Elisabeth Kemter, Birgit Rathkolb, Lise Bankir, Anja Schrewe, Wolfgang Hans, Christina Landbrecht, Matthias Klaften, Boris Ivandic, Helmut Fuchs, Valérie Gailus-Durner, Martin Hrabé de Angelis, Eckhard Wolf, Ruediger Wanke, and Bernhard Aigner. Mutation of the na(+)-k(+)-2cl(-) cotransporter nkcc2 in mice is associated with severe polyuria and a urea-selective concentrating defect without hyperreninemia. American journal of physiology. Renal physiology, 298 6:F1405-15, Jun 2010. URL: https://doi.org/10.1152/ajprenal.00522.2009, doi:10.1152/ajprenal.00522.2009. This article has 48 citations.

30. (kemter2014standardizedsystemicphenotypic pages 1-2): Elisabeth Kemter, Birgit Rathkolb, Lore Becker, Ines Bolle, Dirk H Busch, Claudia Dalke, Ralf Elvert, Jack Favor, Jochen Graw, Wolfgang Hans, Boris Ivandic, Svetoslav Kalaydjiev, Thomas Klopstock, Ildikó Rácz, Jan Rozman, Anja Schrewe, Holger Schulz, Andreas Zimmer, Helmut Fuchs, Valérie Gailus-Durner, Martin Hrabé de Angelis, Eckhard Wolf, and Bernhard Aigner. Standardized, systemic phenotypic analysis of slc12a1i299f mutant mice. Journal of Biomedical Science, 21:68-68, Aug 2014. URL: https://doi.org/10.1186/s12929-014-0068-0, doi:10.1186/s12929-014-0068-0. This article has 9 citations and is from a domain leading peer-reviewed journal.