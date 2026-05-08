---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-08T07:56:24.433259'
end_time: '2026-05-08T08:09:04.551073'
duration_seconds: 760.12
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Autosomal Dominant Osteopetrosis Type II
  mondo_id: ''
  category: Mendelian
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
- **Disease Name:** Autosomal Dominant Osteopetrosis Type II
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Dominant Osteopetrosis Type II** covering all of the
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
- **Disease Name:** Autosomal Dominant Osteopetrosis Type II
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Dominant Osteopetrosis Type II** covering all of the
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


# Autosomal Dominant Osteopetrosis Type II (ADO2) — Comprehensive Disease Characteristics Report

## Target Disease
- **Disease name:** Autosomal Dominant Osteopetrosis Type II (ADO2)
- **Category:** Mendelian (autosomal dominant)
- **MONDO ID:** **MONDO:0008156** (“autosomal dominant osteopetrosis 2”) (OpenTargets Search: autosomal dominant osteopetrosis type II,Albers-Schönberg disease-CLCN7)

---

## 1. Disease Information

### 1.1 Definition / overview
Autosomal dominant osteopetrosis type II (ADO2) is a rare high–bone-mass skeletal disorder caused by impaired osteoclast-mediated bone resorption, leading to radiographically dense but mechanically fragile bone with frequent fractures and characteristic imaging findings (e.g., “sandwich vertebrae” and “bone-in-bone”). It is also referred to as **Albers–Schönberg disease** and is described as the **commonest adult form** of osteopetrosis (funckbrentanoUnknownyearppelmandikstranm pages 1-3, funckbrentanoUnknownyearppelmandikstranm pages 3-4, kang2019acaseof pages 1-3).

**Current understanding (key concept):** Osteopetrosis represents a group of disorders in which osteoclast formation/function is impaired, resulting in increased bone mass but compromised bone quality, with downstream complications including fractures, cranial nerve compression, and (less commonly in ADO2) marrow compromise (funckbrentanoUnknownyearppelmandikstranm pages 1-3, nadyrshina2023clinicalgeneticaspects pages 2-3).

### 1.2 Key identifiers
- **OMIM/MIM:** **MIM 166600** (ADO2) (wang2022naturalhistoryof pages 1-2)
- **MONDO:** **MONDO:0008156** (OpenTargets Search: autosomal dominant osteopetrosis type II,Albers-Schönberg disease-CLCN7)
- **ICD-10:** Osteopetrosis is listed as **ICD-10-78.2** in a 2023 review (note: this is for osteopetrosis as a category; ADO2-specific ICD granularity was not captured in retrieved evidence) (nadyrshina2023clinicalgeneticaspects pages 1-2)
- **Orphanet / MeSH / ICD-11:** Not available in the retrieved full-text evidence set; should be filled from Orphanet/MeSH/ICD-11 directly.

### 1.3 Common synonyms / alternative names
- Autosomal dominant osteopetrosis type II
- ADO II / ADO2
- Albers–Schönberg disease (funckbrentanoUnknownyearppelmandikstranm pages 1-3, kang2019acaseof pages 1-3)

### 1.4 Source type of information
This report integrates:
- **Aggregated resources and expert reviews** (2023–2024) (funckbrentanoUnknownyearppelmandikstranm pages 1-3, nadyrshina2023clinicalgeneticaspects pages 1-2, ma2023molecularmechanismsof pages 2-4)
- **Human cohort / natural history studies** (2022; plus a later natural-history biomarker report) (wang2022naturalhistoryof pages 1-2, wang2022naturalhistoryof pages 8-9, econs2026fracturesarehighly pages 1-3)
- **Case reports** (illustrating variable expressivity and reduced penetrance) (kang2019acaseof pages 1-3)
- **Model organism and mechanistic synthesis** (mouse models; craniofacial/dental mechanisms) (ma2023molecularmechanismsof pages 2-4, ma2023molecularmechanismsof pages 8-10)

---

## 2. Etiology

### 2.1 Disease causal factors
**Primary cause:** germline **heterozygous pathogenic variants in CLCN7** (Cl−/H+ antiporter 7; historically described as a “chloride channel”), causing osteoclast dysfunction with impaired resorption lacuna acidification (wang2022naturalhistoryof pages 1-2, funckbrentanoUnknownyearppelmandikstranm pages 1-3, funckbrentanoUnknownyearppelmandikstranm pages 3-4). A 2024 adult osteopetrosis review notes that **“more than 34 CLCN7 mutations have been reported”** in ADO (funckbrentanoUnknownyearppelmandikstranm pages 1-3).

**Key mechanistic etiologic statement (quoted):** “**Mutation in CLCN7 may disrupt acidiﬁcation of the osteoclast resorption lacunae, resulting in impaired bone degradation**” (ADO II, MIM166600) (wang2022naturalhistoryof pages 1-2).

**Additional required component:** The **OSTM1** subunit is described as required for ClC-7/CLCN7 trafficking to the osteoclast ruffled border (funckbrentanoUnknownyearppelmandikstranm pages 1-3, funckbrentanoUnknownyearppelmandikstranm pages 3-4).

### 2.2 Risk factors
- **Genetic:** carrying a pathogenic **CLCN7** variant is the principal risk factor (Mendelian causal). Penetrance is incomplete and expressivity is variable (funckbrentanoUnknownyearppelmandikstranm pages 3-4, econs2026fracturesarehighly pages 1-3).
- **Non-genetic/environmental:** The retrieved evidence did not identify consistent environmental risk factors for ADO2 onset; clinical risk is dominated by genotype.

### 2.3 Protective factors
No genetic or environmental protective factors were identified in the retrieved evidence.

### 2.4 Gene–environment interactions
No specific gene–environment interactions were identified in the retrieved evidence.

---

## 3. Phenotypes

### 3.1 Core clinical phenotypes (with characteristics)
**Skeletal fragility/fracture (symptom/sign):**
- Fracture is a defining complication despite very high BMD (funckbrentanoUnknownyearppelmandikstranm pages 3-4, wang2022naturalhistoryof pages 8-9).
- In a Chinese cohort (n=36), fracture frequency was **55.6% (20/36)** (wang2022naturalhistoryof pages 8-9).
- A 2024 review summarizes fractures in **~46%** of patients and notes delayed healing (funckbrentanoUnknownyearppelmandikstranm pages 3-4).
- Fracture risk is not reliably predicted by BMD in at least one follow-up subset: BMD stable over ~6 years, yet **5/15** sustained new fractures (funckbrentanoUnknownyearppelmandikstranm pages 3-4, wang2022naturalhistoryof pages 5-6).

**Delayed fracture healing (clinical course):**
- Fractures may show delayed consolidation, sometimes “months to years” per adult osteopetrosis review (funckbrentanoUnknownyearppelmandikstranm pages 3-4).

**Osteomyelitis (especially mandibular) / dental infection:**
- Mandibular osteomyelitis is highlighted as a difficult complication requiring prolonged treatment (funckbrentanoUnknownyearppelmandikstranma pages 4-5).

**Cranial nerve compression / skull-base complications:**
- Vision loss, hearing loss, and facial palsy can occur from skull base sclerosis and foraminal narrowing (wang2022naturalhistoryof pages 8-9, funckbrentanoUnknownyearppelmandikstranma pages 4-5, nadyrshina2023clinicalgeneticaspects pages 2-3).
- In the Chinese cohort, visual loss was **1/36** and bone marrow failure **2/36** (wang2022naturalhistoryof pages 1-2).

**Degenerative joint disease / hip osteoarthritis:**
- Hip osteoarthritis and joint discomfort are reported clinical characteristics (wang2022naturalhistoryof pages 1-2, wang2022naturalhistoryof pages 5-6).

**Hematologic features (less common in ADO2):**
- Reduced marrow space can contribute to anemia/hepatosplenomegaly in osteopetrosis broadly; adult ADO2 marrow failure is noted as uncommon but possible (funckbrentanoUnknownyearppelmandikstranm pages 3-4, nadyrshina2023clinicalgeneticaspects pages 2-3).

### 3.2 Craniofacial and dental phenotypes (2023 synthesis)
A 2023 craniofacial/dental review explicitly catalogs craniofacial and dental abnormalities across osteopetrosis subtypes and includes ADO2/OPTA2 (OMIM #166600). It emphasizes that ion channels/transporters including **TCIRG1, CLCN7, OSTM1, SLC4A2** “**may control osteoclastic acidification**” (ma2023molecularmechanismsof pages 1-2). It also recommends dental attention to prevent missed diagnoses: “**It is recommended that dentists pay attention to the craniofacial condition of osteopetrosis patients to reduce missed diagnoses**” (ma2023molecularmechanismsof pages 12-13).

### 3.3 Suggested HPO terms (non-exhaustive)
(IDs should be verified against current HPO release during KB ingestion.)
- **Increased bone mineral density / osteosclerosis** (e.g., Osteosclerosis)
- **Pathologic fracture / recurrent fractures**
- **Delayed fracture healing**
- **Osteomyelitis of the jaw / mandibular osteomyelitis**
- **Visual impairment / optic atrophy** (optic canal narrowing mechanism noted) (wang2022naturalhistoryof pages 8-9)
- **Hearing impairment**
- **Facial palsy**
- **Dental anomalies:** delayed tooth eruption, hypodontia/dental agenesis, caries, malocclusion (funckbrentanoUnknownyearppelmandikstranma pages 4-5, ma2023molecularmechanismsof pages 8-10)

### 3.4 Quality of life impacts
Direct QoL instrument data (e.g., SF-36, PROMIS) were not present in the retrieved evidence set; however, fracture burden, chronic osteomyelitis, and sensory impairment are expected to be major drivers of disability (funckbrentanoUnknownyearppelmandikstranm pages 1-3, funckbrentanoUnknownyearppelmandikstranm pages 3-4).

---

## 4. Genetic / Molecular Information

### 4.1 Causal gene(s)
- **CLCN7** (Cl−/H+ antiporter 7) is the principal ADO2 gene (funckbrentanoUnknownyearppelmandikstranm pages 1-3, wang2022naturalhistoryof pages 1-2, OpenTargets Search: autosomal dominant osteopetrosis type II,Albers-Schönberg disease-CLCN7).

### 4.2 Pathogenic variants and genotype–phenotype
**Variant spectrum and frequencies (cohort-level):** In a single-center Chinese cohort (n=36), **21 disease-causing CLCN7 mutations** were detected (wang2022naturalhistoryof pages 5-6).
- c.2299C>T (p.Arg767Trp): **16.2%**
- c.296A>G (p.Tyr99Cys): **10.8%**
- c.857G>A (p.Arg286Gln): **10.8%**
- c.937G>A (p.Glu313Lys): **8.1%** (wang2022naturalhistoryof pages 5-6, wang2022naturalhistoryof pages 8-9)

**Reported genotype–phenotype link (example):** c.937G>A (p.Glu313Lys) was associated with “severe fractures, haematological defects and cranial palsy” in this cohort (wang2022naturalhistoryof pages 1-2).

**Penetrance / expressivity:**
- Incomplete penetrance (~66% symptomatic carriers) (funckbrentanoUnknownyearppelmandikstranm pages 3-4, funckbrentanoUnknownyearppelmandikstranm pages 1-3)
- Penetrance estimate 69.23% in one cohort (wang2022naturalhistoryof pages 2-3)
- Familial penetrance reported range **60–90%** in a case report review (kang2019acaseof pages 1-3)

**Expert interpretation:** A later natural-history biomarker study emphasizes marked intrafamilial variability and reports no significant phenotype differences between the most common variant in that cohort (G215R) vs other variants across fracture/BMD/biochemical markers (econs2026fracturesarehighly pages 1-3).

### 4.3 Modifier genes / protective variants
No validated modifier genes or protective variants specific to ADO2 were identified in the retrieved evidence.

### 4.4 Epigenetics / chromosomal abnormalities
Not identified for ADO2 in the retrieved evidence.

---

## 5. Environmental Information
No disease-specific environmental, lifestyle, or infectious triggers were identified in the retrieved evidence set. Clinical risks in ADO2 are primarily genetically determined.

---

## 6. Mechanism / Pathophysiology

### 6.1 Causal chain (genotype → cellular defect → clinical manifestations)
1. **Trigger:** Germline heterozygous **CLCN7** pathogenic variant (wang2022naturalhistoryof pages 1-2).
2. **Upstream cellular mechanism:** Disruption of osteoclast acidification/resorption lacuna function; impaired ruffled border function/trafficking (including requirement for OSTM1) (funckbrentanoUnknownyearppelmandikstranm pages 3-4, funckbrentanoUnknownyearppelmandikstranm pages 1-3).
3. **Tissue-level consequences:** Failure to resorb mineralized bone and calcified cartilage → osteosclerosis/high bone mass with abnormal microarchitecture (“bone islets”; persistent calcified cartilage as a hallmark of osteoclast failure) (funckbrentanoUnknownyearppelmandikstranm pages 4-5, funckbrentanoUnknownyearppelmandikstranma pages 4-5).
4. **Clinical phenotype:** Dense but brittle bone with frequent fractures and delayed repair; skull base sclerosis with foraminal narrowing and cranial neuropathies; mandibular/dental complications; occasional marrow space compromise (funckbrentanoUnknownyearppelmandikstranm pages 3-4, funckbrentanoUnknownyearppelmandikstranma pages 4-5, nadyrshina2023clinicalgeneticaspects pages 2-3).

### 6.2 Pathways and molecular components
A 2023 craniofacial/dental mechanisms review describes core acidification machinery: CA2 generates H+; V-ATPase pumps H+; CLCN7/OSTM1 functions as a **2Cl−/H+ antiporter** contributing to acidification and resorption processes; SLC4A2 supports Cl− flux and downstream protease activation and cytoskeletal/podosome dynamics (ma2023molecularmechanismsof pages 8-10).

### 6.3 Biomarkers / biochemical abnormalities
- **TRAP5b:** A 2024 review states “**TRAP5b levels are always above the normal range in ADO**” and recommends monitoring (funckbrentanoUnknownyearppelmandikstranma pages 4-5).
- A natural history biomarker study (n=54) found correlations with fracture burden: TRAP correlated positively with fractures (r=0.52), while resorption markers CTX and NTx/Cr correlated inversely (econs2026fracturesarehighly pages 1-3).

### 6.4 Cell types (Cell Ontology suggestions)
- **Osteoclast** (primary effector cell; CL term: osteoclast)
- Osteoblast/osteocyte (secondary remodeling context)

### 6.5 GO term suggestions (verify IDs during curation)
- Bone resorption
- Osteoclast differentiation
- Proton transmembrane transport / lysosomal acidification
- Chloride transmembrane transport

### 6.6 -omics / advanced technologies
- Human iPSC disease modeling exists for ADO2 and includes proteomic profiling of patient-derived iPSCs (Ou et al., 2019; not a 2023–2024 development but a relevant real-world model platform) (ou2019genotypinggenerationand…; see retrieved corpus).

---

## 7. Anatomical Structures Affected

### 7.1 Organ/system level
- **Skeletal system** (primary): spine, pelvis, long bones, skull base (funckbrentanoUnknownyearppelmandikstranm pages 3-4, wang2022naturalhistoryof pages 8-9)
- **Cranial nerve pathways** (secondary): optic canal narrowing with optic atrophy; auditory/facial nerve impingement (wang2022naturalhistoryof pages 8-9, funckbrentanoUnknownyearppelmandikstranma pages 4-5)
- **Orofacial/dental**: mandible and dentition (osteomyelitis, dental anomalies) (funckbrentanoUnknownyearppelmandikstranma pages 4-5, ma2023molecularmechanismsof pages 8-10)
- **Hematopoietic system** (variable/less common in ADO2 adults): marrow space compromise and cytopenias in more severe cases (funckbrentanoUnknownyearppelmandikstranm pages 3-4, wang2022naturalhistoryof pages 1-2)

### 7.2 UBERON suggestions (verify IDs)
- Bone of vertebral column; lumbar vertebra
- Pelvic bone
- Skull base
- Mandible
- Bone marrow

---

## 8. Temporal Development (Natural History)
- **Typical onset:** late childhood/adolescence to adulthood (ADO described as milder/benign adult form) (nadyrshina2023clinicalgeneticaspects pages 1-2, ma2023molecularmechanismsof pages 2-4).
- **Course:** Often described as relatively stable; however, fractures can occur repeatedly, and fracture healing may be prolonged (funckbrentanoUnknownyearppelmandikstranm pages 3-4, wang2022naturalhistoryof pages 1-2).
- In a retrospective cohort with follow-up (mean ~6.3 years), incident fractures occurred despite stable BMD (funckbrentanoUnknownyearppelmandikstranm pages 3-4, wang2022naturalhistoryof pages 5-6).

---

## 9. Inheritance and Population

### 9.1 Inheritance
- **Autosomal dominant** with **incomplete penetrance** and variable expressivity (funckbrentanoUnknownyearppelmandikstranm pages 3-4, kang2019acaseof pages 1-3).

### 9.2 Epidemiology
- **Incidence estimate:** ~**1 in 20,000 births** reported for ADO in multiple reviews/studies (funckbrentanoUnknownyearppelmandikstranm pages 1-3, nadyrshina2023clinicalgeneticaspects pages 1-2, econs2026fracturesarehighly pages 1-3).
- A 2023 craniofacial/dental review cites a **frequency ~5.5 per 100,000** for OPTA2/ADO2 (ma2023molecularmechanismsof pages 2-4).

**Demographics:** A Chinese cohort reports fractures often occurring at ≤18 years among those who fracture (age distribution for fractures presented as “≤18/>18: 37/7”) (wang2022naturalhistoryof pages 8-9). Sex ratio and geographic/ancestry enrichment were not available in the retrieved evidence.

---

## 10. Diagnostics

### 10.1 Clinical criteria and imaging
**Radiographic hallmarks** (diagnostic cornerstone):
- “Sandwich vertebrae”/vertebral endplate sclerosis; “bone-in-bone” appearances; skull base densification; Erlenmeyer-flask changes (funckbrentanoUnknownyearppelmandikstranm pages 3-4, funckbrentanoUnknownyearppelmandikstranma pages 4-5).

**Imaging for complications:** MRI/CT/tomodensitometry to monitor optic foramina and cranial nerve compression (funckbrentanoUnknownyearppelmandikstranm pages 3-4).

### 10.2 DXA and bone density
DXA typically shows markedly increased BMD (e.g., Z-score > +2), but BMD may not reliably predict fracture risk and routine serial BMD is not recommended for fracture-risk monitoring by one expert review (funckbrentanoUnknownyearppelmandikstranm pages 3-4).

### 10.3 Laboratory evaluation / biomarkers
- Suggested monitoring includes **blood count** and **PTH** (funckbrentanoUnknownyearppelmandikstranma pages 4-5).
- **TRAP5b** may be elevated and is suggested as a useful marker of osteoclast number in ADO (funckbrentanoUnknownyearppelmandikstranma pages 4-5).

### 10.4 Genetic testing
A cohort states: “**The diagnosis of ADOII depends on clinical manifestations, typical imaging examinations and CLCN7 gene mutation**” (wang2022naturalhistoryof pages 2-3). Practical approach: targeted CLCN7 testing or broader skeletal dysplasia/osteoclast disorder panels or exome sequencing depending on context.

### 10.5 Differential diagnosis
Not comprehensively captured in retrieved evidence; key clinical differentials include other osteosclerotic disorders and other osteopetrosis genetic subtypes (e.g., LRP5-driven OPTA1; recessive TCIRG1/OSTM1 forms), which differ in severity, hematologic involvement, and transplant responsiveness (nadyrshina2023clinicalgeneticaspects pages 2-3, ma2023molecularmechanismsof pages 12-13).

---

## 11. Outcome / Prognosis
- ADO2 is generally considered **milder** than infantile recessive osteopetrosis, but morbidity can be substantial due to fracture burden and cranial/dental complications (nadyrshina2023clinicalgeneticaspects pages 1-2, funckbrentanoUnknownyearppelmandikstranm pages 1-3).
- In one cohort, severe outcomes (visual loss 1/36; marrow failure 2/36) were uncommon but present (wang2022naturalhistoryof pages 1-2).

Quantitative survival/life expectancy statistics specific to ADO2 were not available in the retrieved evidence set.

---

## 12. Treatment

### 12.1 Current applications and real-world implementations (adult ADO2)
**Consensus from adult osteopetrosis expert review:** Adult ADO2 care is largely **supportive and multidisciplinary**, ideally in specialized centers, focusing on monitoring and managing fractures, dental/mandibular infections, and cranial nerve complications (funckbrentanoUnknownyearppelmandikstranm pages 1-3, funckbrentanoUnknownyearppelmandikstranma pages 4-5).

**Examples of real-world management needs:**
- Mandibular osteomyelitis may require “long-term antibiotic therapy and surgical debridement” (funckbrentanoUnknownyearppelmandikstranma pages 4-5).
- Skull base/cranial foramina involvement may require specialized ophthalmologic/ENT monitoring and, in some cases, surgical decompression or neurosurgical intervention (funckbrentanoUnknownyearppelmandikstranma pages 4-5).

### 12.2 HSCT (contextual, not typical for adult ADO2)
A 2023 review notes HSCT “**is recognized as the most effective treatment, which allows restoration of bone resorption by cells of donor origin**,” but also emphasizes genotype-specific contraindications (e.g., severe neurological disorders in TNFSF11/OSTM1) (nadyrshina2023clinicalgeneticaspects pages 2-3). Adult ADO2 (CLCN7) is generally managed conservatively rather than transplanted in the reviewed expert summary (funckbrentanoUnknownyearppelmandikstranm pages 1-3).

### 12.3 Experimental / emerging (research directions)
Expert reviews emphasize knowledge gaps and the need for therapies that restore osteoclast resorptive capacity and for better natural history/endpoint development (funckbrentanoUnknownyearppelmandikstranm pages 1-3, econs2026fracturesarehighly pages 1-3).

### 12.4 MAXO term suggestions (verify IDs)
- Orthopedic fracture management
- Surgical debridement (mandibular osteomyelitis)
- Long-term antibiotic therapy
- Ophthalmologic monitoring; ENT monitoring
- Genetic counseling

---

## 13. Prevention
No primary prevention exists for a Mendelian causal disorder; practical prevention is **tertiary prevention** of complications via surveillance and prompt management:
- Prevent/manage dental infection and avoid high-risk dental trauma when possible; early referral for mandibular infection (funckbrentanoUnknownyearppelmandikstranma pages 4-5, ma2023molecularmechanismsof pages 12-13)
- Monitor for cranial nerve compromise (vision/hearing) (funckbrentanoUnknownyearppelmandikstranma pages 4-5)
- Genetic counseling for affected families due to AD inheritance and incomplete penetrance (kang2019acaseof pages 1-3)

---

## 14. Other Species / Natural Disease
No naturally occurring veterinary ADO2 analogs were identified in the retrieved evidence set.

---

## 15. Model Organisms
- **Mouse (Clcn7-deficient models):** described as recapitulating high bone density and multisystem phenotypes including neurodegeneration and dental/retinal abnormalities, supporting mechanistic relevance for CLCN7-dependent osteopetrosis (ma2023molecularmechanismsof pages 2-4).
- **Myeloid cell-specific Clcn7 mutant mouse (e.g., Clcn7G763R):** used to validate pathway-level findings in CLCN7-mutant osteopetrosis research (basit2026geneticsofosteopetrosis pages 8-9).
- **Human iPSC models:** ADO2-specific iPSCs with proteomic profiling exist, enabling disease modeling and therapeutic screening (Ou et al., 2019; see retrieved corpus).

---

## Key quantitative evidence summary (for KB ingestion)
The following table consolidates incidence, penetrance, fracture burden, and recurrent CLCN7 variant frequencies and phenotype notes.

| Finding | Value | Population/Study | Year | PMID/DOI/URL | Evidence ID |
|---|---:|---|---:|---|---|
| Estimated incidence of ADO/ADO2 | ~1 in 20,000 births | Adult osteopetrosis review; ADO2/Albers–Schönberg disease described as the common adult form | 2024 | Eur J Med Genet review URL not fully available in context; OpenTargets disease mapping available: https://platform.opentargets.org/disease/MONDO_0008156 | (funckbrentanoUnknownyearppelmandikstranm pages 1-3, OpenTargets Search: autosomal dominant osteopetrosis type II,Albers-Schönberg disease-CLCN7) |
| Penetrance of CLCN7-associated ADO2 | ~66% symptomatic carriers | Review summary of mutation carriers with incomplete penetrance | 2024 | Review URL not fully available in context | (funckbrentanoUnknownyearppelmandikstranm pages 3-4, funckbrentanoUnknownyearppelmandikstranm pages 1-3) |
| Penetrance in single-center Chinese cohort | 69.23% | 36 patients from 28 unrelated families with ADOII | 2022 | DOI: 10.3389/fendo.2022.819641; https://doi.org/10.3389/fendo.2022.819641 | (wang2022naturalhistoryof pages 2-3) |
| Penetrance range reported in families | 60–90% | Family/case-based literature summarized in Korean case report | 2019 | DOI: 10.4274/jcrpe.galenos.2019.2018.0229; https://doi.org/10.4274/jcrpe.galenos.2019.2018.0229 | (kang2019acaseof pages 1-3) |
| Overall fracture frequency in ADO2 | ~46% | Review summary of ADO2 patients | 2024 | Review URL not fully available in context | (funckbrentanoUnknownyearppelmandikstranm pages 3-4, funckbrentanoUnknownyearppelmandikstranma pages 3-4) |
| Fracture frequency in Chinese ADO2 cohort | 55.6% (20/36) | 36 Chinese patients with ADO II | 2022 | DOI: 10.3389/fendo.2022.819641; https://doi.org/10.3389/fendo.2022.819641 | (wang2022naturalhistoryof pages 8-9) |
| Fracture frequency by age group in prior series | 53% affected children; 98% affected adults | Prior ADO cohort summarized in natural-history/biomarker study | 2026 | DOI: 10.1093/jbmr/zjaf123; https://doi.org/10.1093/jbmr/zjaf123 | (econs2026fracturesarehighly pages 8-10) |
| Severe fractures by age group in prior series | 16% children; 49% adults | Prior ADO cohort summarized in natural-history/biomarker study | 2026 | DOI: 10.1093/jbmr/zjaf123; https://doi.org/10.1093/jbmr/zjaf123 | (econs2026fracturesarehighly pages 8-10) |
| Fracture frequency in Benichou series | 78% | 42 ADO patients summarized in biomarker study | 2026 | DOI: 10.1093/jbmr/zjaf123; https://doi.org/10.1093/jbmr/zjaf123 | (econs2026fracturesarehighly pages 8-10) |
| Visual loss frequency in Chinese ADO2 cohort | 1/36 (2.8%) | 36 Chinese patients with ADO II | 2022 | DOI: 10.3389/fendo.2022.819641; https://doi.org/10.3389/fendo.2022.819641 | (wang2022naturalhistoryof pages 1-2) |
| Bone marrow failure frequency in Chinese ADO2 cohort | 2/36 (5.6%) | 36 Chinese patients with ADO II | 2022 | DOI: 10.3389/fendo.2022.819641; https://doi.org/10.3389/fendo.2022.819641 | (wang2022naturalhistoryof pages 1-2) |
| Key retrospective cohort size | 36 patients; 28 unrelated families | Single-center ADO II natural history study | 2022 | DOI: 10.3389/fendo.2022.819641; https://doi.org/10.3389/fendo.2022.819641 | (wang2022naturalhistoryof pages 2-3) |
| Longitudinal follow-up subset | 15 patients; mean follow-up 6.3 years (range 1–14 years) | Subset of the Chinese ADO II cohort | 2022 | DOI: 10.3389/fendo.2022.819641; https://doi.org/10.3389/fendo.2022.819641 | (wang2022naturalhistoryof pages 1-2, wang2022naturalhistoryof pages 5-6) |
| New fractures during follow-up | 5/15 | Followed patients in Chinese ADO II cohort | 2022 | DOI: 10.3389/fendo.2022.819641; https://doi.org/10.3389/fendo.2022.819641 | (wang2022naturalhistoryof pages 5-6) |
| Baseline natural-history/biomarker cohort size | 54 total (42 adults, 12 children); 37 adults with disease-causing CLCN7 variants | Cross-sectional baseline analysis in ADO natural history study | 2026 | DOI: 10.1093/jbmr/zjaf123; https://doi.org/10.1093/jbmr/zjaf123 | (econs2026fracturesarehighly pages 1-3) |
| Number of disease-causing CLCN7 mutations identified | 21 mutations | 36 Chinese ADO II patients | 2022 | DOI: 10.3389/fendo.2022.819641; https://doi.org/10.3389/fendo.2022.819641 | (wang2022naturalhistoryof pages 5-6, wang2022naturalhistoryof pages 1-2) |
| Reported number of CLCN7 mutations in ADO overall | >34 mutations reported | Review summary | 2024 | Review URL not fully available in context | (funckbrentanoUnknownyearppelmandikstranm pages 1-3) |
| Most frequent CLCN7 variant | c.2299C>T (p.Arg767Trp), 16.2% (6 cases) | Chinese ADO II cohort | 2022 | DOI: 10.3389/fendo.2022.819641; https://doi.org/10.3389/fendo.2022.819641 | (wang2022naturalhistoryof pages 5-6, wang2022naturalhistoryof pages 8-9, wang2022naturalhistoryof pages 1-2) |
| Phenotype of c.2299C>T (p.Arg767Trp) | Joint discomfort/osteoarthritis common; 4/6 fractured, including 1 multiple fractures | Chinese ADO II cohort | 2022 | DOI: 10.3389/fendo.2022.819641; https://doi.org/10.3389/fendo.2022.819641 | (wang2022naturalhistoryof pages 5-6) |
| Second recurrent CLCN7 variant | c.296A>G (p.Tyr99Cys), 10.8% (4 cases) | Chinese ADO II cohort | 2022 | DOI: 10.3389/fendo.2022.819641; https://doi.org/10.3389/fendo.2022.819641 | (wang2022naturalhistoryof pages 5-6, wang2022naturalhistoryof pages 8-9) |
| Phenotype of c.296A>G (p.Tyr99Cys) | Fractures in 2 patients | Chinese ADO II cohort | 2022 | DOI: 10.3389/fendo.2022.819641; https://doi.org/10.3389/fendo.2022.819641 | (wang2022naturalhistoryof pages 5-6) |
| Third recurrent CLCN7 variant | c.857G>A (p.Arg286Gln), 10.8% (4 cases) | Chinese ADO II cohort | 2022 | DOI: 10.3389/fendo.2022.819641; https://doi.org/10.3389/fendo.2022.819641 | (wang2022naturalhistoryof pages 5-6, wang2022naturalhistoryof pages 8-9) |
| Phenotype of c.857G>A (p.Arg286Gln) | Mild symptoms; fewer fractures and lower FN/TH BMD Z-scores than p.Arg767Trp group | Chinese ADO II cohort | 2022 | DOI: 10.3389/fendo.2022.819641; https://doi.org/10.3389/fendo.2022.819641 | (wang2022naturalhistoryof pages 5-6, wang2022naturalhistoryof pages 8-9) |
| Fourth recurrent CLCN7 variant | c.937G>A (p.Glu313Lys), 8.1% (3 cases) | Chinese ADO II cohort | 2022 | DOI: 10.3389/fendo.2022.819641; https://doi.org/10.3389/fendo.2022.819641 | (wang2022naturalhistoryof pages 5-6, wang2022naturalhistoryof pages 8-9, wang2022naturalhistoryof pages 1-2) |
| Phenotype of c.937G>A (p.Glu313Lys) | Severe phenotype: severe fractures, visual loss, hematological defects, cranial palsy | Chinese ADO II cohort | 2022 | DOI: 10.3389/fendo.2022.819641; https://doi.org/10.3389/fendo.2022.819641 | (wang2022naturalhistoryof pages 5-6, wang2022naturalhistoryof pages 1-2) |
| Common variant in 2026 registry/natural-history cohort | G215R most common (N=14 among CLCN7 variant carriers analyzed) | Adult ADO natural-history/biomarker cohort | 2026 | DOI: 10.1093/jbmr/zjaf123; https://doi.org/10.1093/jbmr/zjaf123 | (econs2026fracturesarehighly pages 8-10, econs2026fracturesarehighly pages 1-3) |
| Genotype–phenotype conclusion for G215R | No significant difference vs other CLCN7 variants for fracture, BMD, or bone turnover markers | Adult ADO natural-history/biomarker cohort | 2026 | DOI: 10.1093/jbmr/zjaf123; https://doi.org/10.1093/jbmr/zjaf123 | (econs2026fracturesarehighly pages 1-3) |


*Table: This table compiles key quantitative data for autosomal dominant osteopetrosis type II, including incidence, penetrance, fracture burden, cohort sizes, and recurrent CLCN7 variants with associated phenotypes. It is useful as a quick evidence map for disease characterization and genotype-phenotype interpretation.*

---

## Visual evidence (radiographic and variant tables)
The ADO2 natural history cohort paper includes radiographic examples (sandwich vertebrae; bone-in-bone) and tables summarizing CLCN7 variants and their associated clinical/biochemical features (wang2022naturalhistoryof media 01f471f9, wang2022naturalhistoryof media 1e172433, wang2022naturalhistoryof media 154a27d0).

---

## Recent developments and expert perspectives (2023–2024 emphasis)
- **2024 adult osteopetrosis review (European expert perspective):** emphasizes ADO2 as the common adult osteopetrosis subtype; highlights incomplete penetrance, high fracture burden with delayed repair, cranial nerve/dental complications, and recommends multidisciplinary specialized follow-up; also underscores evidence gaps in natural history and need for improved clinical studies/endpoints (funckbrentanoUnknownyearppelmandikstranm pages 1-3, funckbrentanoUnknownyearppelmandikstranm pages 3-4).
- **2023 craniofacial/dental mechanisms review:** reframes osteopetrosis diagnosis through “telltale” craniofacial/dental abnormalities and mechanistically groups causal genes (including CLCN7/TCIRG1/OSTM1) as controllers of osteoclastic acidification; recommends dental vigilance to reduce missed diagnoses (ma2023molecularmechanismsof pages 1-2, ma2023molecularmechanismsof pages 12-13).
- **2023 genetics/pathogenesis review:** stresses genotype-guided care, noting HSCT efficacy and contraindications depend on genetic subtype and neurologic involvement (nadyrshina2023clinicalgeneticaspects pages 2-3).

---

## Evidence limitations (explicit)
- Formal identifiers beyond **MIM 166600**, **MONDO:0008156**, and an osteopetrosis-category **ICD-10-78.2** were not present in retrieved texts.
- Recent (2023–2024) ADO2-specific prospective interventional trials were not retrieved; management evidence is predominantly expert review and cohort/case literature.
- QoL instruments and population-level prevalence/incidence beyond estimates (1:20,000 births; 5.5/100,000 frequency cited) were not captured in the retrieved evidence set.


References

1. (OpenTargets Search: autosomal dominant osteopetrosis type II,Albers-Schönberg disease-CLCN7): Open Targets Query (autosomal dominant osteopetrosis type II,Albers-Schönberg disease-CLCN7, 6 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (funckbrentanoUnknownyearppelmandikstranm pages 1-3): T Funck-Brentano and MC Zillikens. Ppelman-di kstra, nm, & cohen-solal, m.(2024). Unknown journal, Unknown year.

3. (funckbrentanoUnknownyearppelmandikstranm pages 3-4): T Funck-Brentano and MC Zillikens. Ppelman-di kstra, nm, & cohen-solal, m.(2024). Unknown journal, Unknown year.

4. (kang2019acaseof pages 1-3): Sol Kang, Young Kyung Kang, Jun Ah Lee, Dong Ho Kim, and Jung Sub Lim. A case of autosomal dominant osteopetrosis type 2 with a &lt;i&gt;clcn7&lt;/i&gt; gene mutation. Journal of Clinical Research in Pediatric Endocrinology, 11:439-443, Dec 2019. URL: https://doi.org/10.4274/jcrpe.galenos.2019.2018.0229, doi:10.4274/jcrpe.galenos.2019.2018.0229. This article has 8 citations.

5. (nadyrshina2023clinicalgeneticaspects pages 2-3): D. D. Nadyrshina and R. I. Khusainova. Clinical, genetic aspects and molecular pathogenesis of osteopetrosis. Vavilov Journal of Genetics and Breeding, 27:383-392, Jul 2023. URL: https://doi.org/10.18699/vjgb-23-46, doi:10.18699/vjgb-23-46. This article has 13 citations.

6. (wang2022naturalhistoryof pages 1-2): Ziyuan Wang, Xiang Li, Ya Wang, Wenzhen Fu, Yujuan Liu, Zhenlin Zhang, and Chun Wang. Natural history of type ii autosomal dominant osteopetrosis: a single center retrospective study. Frontiers in Endocrinology, Mar 2022. URL: https://doi.org/10.3389/fendo.2022.819641, doi:10.3389/fendo.2022.819641. This article has 13 citations.

7. (nadyrshina2023clinicalgeneticaspects pages 1-2): D. D. Nadyrshina and R. I. Khusainova. Clinical, genetic aspects and molecular pathogenesis of osteopetrosis. Vavilov Journal of Genetics and Breeding, 27:383-392, Jul 2023. URL: https://doi.org/10.18699/vjgb-23-46, doi:10.18699/vjgb-23-46. This article has 13 citations.

8. (ma2023molecularmechanismsof pages 2-4): Yu Ma, Yali Xu, Yanli Zhang, and Xiaohong Duan. Molecular mechanisms of craniofacial and dental abnormalities in osteopetrosis. International Journal of Molecular Sciences, 24:10412, Jun 2023. URL: https://doi.org/10.3390/ijms241210412, doi:10.3390/ijms241210412. This article has 21 citations.

9. (wang2022naturalhistoryof pages 8-9): Ziyuan Wang, Xiang Li, Ya Wang, Wenzhen Fu, Yujuan Liu, Zhenlin Zhang, and Chun Wang. Natural history of type ii autosomal dominant osteopetrosis: a single center retrospective study. Frontiers in Endocrinology, Mar 2022. URL: https://doi.org/10.3389/fendo.2022.819641, doi:10.3389/fendo.2022.819641. This article has 13 citations.

10. (econs2026fracturesarehighly pages 1-3): Michael J Econs, Stuart J Warden, Ziyue Liu, Paul J Niziolek, Corinne Parks-Schenck, Netsanet Gebregziabher, Rita L Gerard-O'Riley, Marian Hart, Lynda E Polgreen, and Erik A Imel. Fractures are highly correlated with bone density and inversely correlated with bone turnover markers in autosomal dominant osteopetrosis. Journal of Bone and Mineral Research, 41:150-157, Sep 2026. URL: https://doi.org/10.1093/jbmr/zjaf123, doi:10.1093/jbmr/zjaf123. This article has 0 citations and is from a highest quality peer-reviewed journal.

11. (ma2023molecularmechanismsof pages 8-10): Yu Ma, Yali Xu, Yanli Zhang, and Xiaohong Duan. Molecular mechanisms of craniofacial and dental abnormalities in osteopetrosis. International Journal of Molecular Sciences, 24:10412, Jun 2023. URL: https://doi.org/10.3390/ijms241210412, doi:10.3390/ijms241210412. This article has 21 citations.

12. (wang2022naturalhistoryof pages 5-6): Ziyuan Wang, Xiang Li, Ya Wang, Wenzhen Fu, Yujuan Liu, Zhenlin Zhang, and Chun Wang. Natural history of type ii autosomal dominant osteopetrosis: a single center retrospective study. Frontiers in Endocrinology, Mar 2022. URL: https://doi.org/10.3389/fendo.2022.819641, doi:10.3389/fendo.2022.819641. This article has 13 citations.

13. (funckbrentanoUnknownyearppelmandikstranma pages 4-5): T Funck-Brentano and MC Zillikens. Ppelman-di kstra, nm, & cohen-solal, m.(2024). Unknown journal, Unknown year.

14. (ma2023molecularmechanismsof pages 1-2): Yu Ma, Yali Xu, Yanli Zhang, and Xiaohong Duan. Molecular mechanisms of craniofacial and dental abnormalities in osteopetrosis. International Journal of Molecular Sciences, 24:10412, Jun 2023. URL: https://doi.org/10.3390/ijms241210412, doi:10.3390/ijms241210412. This article has 21 citations.

15. (ma2023molecularmechanismsof pages 12-13): Yu Ma, Yali Xu, Yanli Zhang, and Xiaohong Duan. Molecular mechanisms of craniofacial and dental abnormalities in osteopetrosis. International Journal of Molecular Sciences, 24:10412, Jun 2023. URL: https://doi.org/10.3390/ijms241210412, doi:10.3390/ijms241210412. This article has 21 citations.

16. (wang2022naturalhistoryof pages 2-3): Ziyuan Wang, Xiang Li, Ya Wang, Wenzhen Fu, Yujuan Liu, Zhenlin Zhang, and Chun Wang. Natural history of type ii autosomal dominant osteopetrosis: a single center retrospective study. Frontiers in Endocrinology, Mar 2022. URL: https://doi.org/10.3389/fendo.2022.819641, doi:10.3389/fendo.2022.819641. This article has 13 citations.

17. (funckbrentanoUnknownyearppelmandikstranm pages 4-5): T Funck-Brentano and MC Zillikens. Ppelman-di kstra, nm, & cohen-solal, m.(2024). Unknown journal, Unknown year.

18. (basit2026geneticsofosteopetrosis pages 8-9): Sulman Basit and Khalid I. Khoshhal. Genetics of osteopetrosis: molecular insights and clinical implications. Journal of Musculoskeletal Surgery and Research, 10:40-50, Nov 2026. URL: https://doi.org/10.25259/jmsr\_357\_2025, doi:10.25259/jmsr\_357\_2025. This article has 0 citations.

19. (funckbrentanoUnknownyearppelmandikstranma pages 3-4): T Funck-Brentano and MC Zillikens. Ppelman-di kstra, nm, & cohen-solal, m.(2024). Unknown journal, Unknown year.

20. (econs2026fracturesarehighly pages 8-10): Michael J Econs, Stuart J Warden, Ziyue Liu, Paul J Niziolek, Corinne Parks-Schenck, Netsanet Gebregziabher, Rita L Gerard-O'Riley, Marian Hart, Lynda E Polgreen, and Erik A Imel. Fractures are highly correlated with bone density and inversely correlated with bone turnover markers in autosomal dominant osteopetrosis. Journal of Bone and Mineral Research, 41:150-157, Sep 2026. URL: https://doi.org/10.1093/jbmr/zjaf123, doi:10.1093/jbmr/zjaf123. This article has 0 citations and is from a highest quality peer-reviewed journal.

21. (wang2022naturalhistoryof media 01f471f9): Ziyuan Wang, Xiang Li, Ya Wang, Wenzhen Fu, Yujuan Liu, Zhenlin Zhang, and Chun Wang. Natural history of type ii autosomal dominant osteopetrosis: a single center retrospective study. Frontiers in Endocrinology, Mar 2022. URL: https://doi.org/10.3389/fendo.2022.819641, doi:10.3389/fendo.2022.819641. This article has 13 citations.

22. (wang2022naturalhistoryof media 1e172433): Ziyuan Wang, Xiang Li, Ya Wang, Wenzhen Fu, Yujuan Liu, Zhenlin Zhang, and Chun Wang. Natural history of type ii autosomal dominant osteopetrosis: a single center retrospective study. Frontiers in Endocrinology, Mar 2022. URL: https://doi.org/10.3389/fendo.2022.819641, doi:10.3389/fendo.2022.819641. This article has 13 citations.

23. (wang2022naturalhistoryof media 154a27d0): Ziyuan Wang, Xiang Li, Ya Wang, Wenzhen Fu, Yujuan Liu, Zhenlin Zhang, and Chun Wang. Natural history of type ii autosomal dominant osteopetrosis: a single center retrospective study. Frontiers in Endocrinology, Mar 2022. URL: https://doi.org/10.3389/fendo.2022.819641, doi:10.3389/fendo.2022.819641. This article has 13 citations.
