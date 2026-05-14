---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-08T08:09:07.336883'
end_time: '2026-05-08T08:40:14.762560'
duration_seconds: 1867.43
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Autosomal Recessive Osteopetrosis Type 2
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 38
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autosomal Recessive Osteopetrosis Type 2
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Recessive Osteopetrosis Type 2** covering all of the
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
- **Disease Name:** Autosomal Recessive Osteopetrosis Type 2
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Recessive Osteopetrosis Type 2** covering all of the
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


# Comprehensive Disease Characteristics Report: Autosomal Recessive Osteopetrosis Type 2 (ARO2; TCIRG1-related)

## 1. Disease information

### 1.1 Overview / definition
Autosomal recessive osteopetrosis type 2 (ARO2) is a severe, typically infantile-onset osteoclast dysfunction disorder characterized by markedly increased bone density (“marble bone”) due to failure of osteoclast-mediated bone resorption, leading to bone marrow space obliteration (cytopenias) and narrowing of cranial nerve foramina (progressive visual/hearing impairment). (capo2022osteoclastrichosteopetrosis pages 1-2, penna2021autosomalrecessiveosteopetrosis pages 1-2, orchard2015hematopoieticstemcell pages 1-6)

### 1.2 Key identifiers (with URLs / dates when available)
- **MONDO**:
  - *Autosomal recessive osteopetrosis 2*: **MONDO:0009816** (via Open Targets disease ontology mapping). (OpenTargets Search: autosomal recessive osteopetrosis-TCIRG1)
  - *Autosomal recessive osteopetrosis (broader)*: **MONDO:0019026**. (OpenTargets Search: autosomal recessive osteopetrosis-TCIRG1)
- **OMIM (disease)**: Infantile malignant autosomal recessive osteopetrosis / OPTB1: **MIM 259700**. (frattini2000defectsintcirg1 pages 1-2, capo2022osteoclastrichosteopetrosis pages 1-2)
- **OMIM (gene)**: **TCIRG1**: **MIM 604592**. (elkamah2023outliningtheclinical pages 1-2)
- **ICD-10**: Osteopetrosis is referenced as **ICD-10 M78.2** in a 2023 review (note: this is osteopetrosis broadly, not ARO2-specific). (nadyrshina2023clinicalgeneticaspects pages 1-2)
- **MeSH (ClinicalTrials.gov browse terms)**: Musculoskeletal Diseases (D009140), Bone Diseases (D001847), Hypocalcemia (D006996), Bone Marrow Failure Disorders (D000080983) are attached to a TCIRG1 gene-therapy trial record. (NCT04525352 chunk 1)

**Not found in retrieved evidence**: an explicit Orphanet identifier, ICD-11 code, and a single dedicated MeSH descriptor for “osteopetrosis” within the retrieved texts.

### 1.3 Synonyms / alternative names
Common alternative names and labels include:
- **Infantile malignant osteopetrosis** (frattini2000defectsintcirg1 pages 1-2, capo2022osteoclastrichosteopetrosis pages 1-2)
- **Autosomal recessive malignant osteopetrosis (arOP)** (frattini2000defectsintcirg1 pages 1-2)
- **Autosomal recessive osteopetrosis (ARO)** (capo2022osteoclastrichosteopetrosis pages 1-2)
- **OPTB1** / **TCIRG1 osteopetrosis (OPTB1 subgroup)** (capo2022osteoclastrichosteopetrosis pages 1-2)

### 1.4 Evidence origin (individual vs aggregated)
The report integrates **aggregated disease-level resources** (e.g., Open Targets MONDO mappings) (OpenTargets Search: autosomal recessive osteopetrosis-TCIRG1), **registry-based transplant cohorts** (CIBMTR/EBMT referenced in reviews and primary studies) (orchard2015hematopoieticstemcell pages 1-6, capo2022osteoclastrichosteopetrosis pages 5-6), and **individual/cohort clinical genetics series** (e.g., Egyptian pedigrees) (elkamah2023outliningtheclinical pages 4-7).

## 2. Etiology

### 2.1 Primary causal factors
ARO2 is caused by **biallelic loss-of-function variants in TCIRG1**, which encodes the **a3 subunit of the osteoclast vacuolar H+-ATPase (V-ATPase) V0 sector**, required for acidification of the resorption lacuna and thus mineral dissolution and matrix degradation during bone resorption. (capo2022osteoclastrichosteopetrosis pages 1-2, frattini2000defectsintcirg1 pages 1-2, penna2024correctionofosteopetrosis pages 1-2)

**Primary literature milestone**: Frattini et al. (Nature Genetics, 2000) demonstrated that **TCIRG1** is mutated in a substantial subset of patients with infantile malignant ARO and connects TCIRG1/OC116 to osteoclast lacunar acidification. **Direct abstract/text quote**: “*Infantile malignant autosomal recessive osteopetrosis (MIM 259700) is a severe bone disease with a fatal outcome, generally within the first decade of life… Here we show that TCIRG1, encoding the osteoclast-specific 116-kD subunit of the vacuolar proton pump, is mutated…*” (frattini2000defectsintcirg1 pages 1-2)

### 2.2 Risk factors
- **Genetic**: Having **biallelic pathogenic TCIRG1 variants** is causal. High rates of **consanguinity** can increase disease occurrence; in one TCIRG1 cohort, **90% of probands** were from consanguineous families. (elkamah2023outliningtheclinical pages 4-7)
- **Environmental**: No specific environmental risk factor is established in the retrieved evidence for this Mendelian disorder.

### 2.3 Protective factors
No validated genetic or environmental protective factors were identified in the retrieved evidence.

### 2.4 Gene–environment interactions
No specific gene–environment interactions were identified in the retrieved evidence.

## 3. Phenotypes (with suggested HPO terms)

### 3.1 Core phenotype spectrum (TCIRG1-related malignant/infantile ARO)
Phenotypes span skeletal, hematologic, neurologic/cranial nerve, dental, and metabolic domains, consistent with “osteoclast-rich” osteopetrosis where osteoclasts are present but nonfunctional. (capo2022osteoclastrichosteopetrosis pages 1-2, penna2021autosomalrecessiveosteopetrosis pages 1-2)

### 3.2 Phenotype frequencies from a 2023 TCIRG1 cohort (Egyptian families; n=16 affected)
Reported frequencies (useful for knowledge-base quantitative annotations):
- **Frontal bossing**: 16/16 (100%) → HPO: *Frontal bossing* (HP:0002007) (elkamah2023outliningtheclinical pages 4-7)
- **History of fractures**: 15/16 (94%) → HPO: *Bone fracture* (HP:0002653) (elkamah2023outliningtheclinical pages 4-7)
- **Short stature**: 13/16 (81%) → HPO: *Short stature* (HP:0004322) (elkamah2023outliningtheclinical pages 4-7)
- **Macrocephaly**: 13/16 (81%) → HPO: *Macrocephaly* (HP:0000256) (elkamah2023outliningtheclinical pages 4-7)
- **Anemia**: 12/16 (75%) → HPO: *Anemia* (HP:0001903) (elkamah2023outliningtheclinical pages 4-7)
- **Hepatosplenomegaly**: 9/16 (56%) → HPO: *Hepatosplenomegaly* (HP:0002240) (elkamah2023outliningtheclinical pages 4-7)
- **Neurological deficit**: 8/16 (50%), including **developmental delay (25%)**, **facial palsy (6.25%)**, **deafness (12.5%)**, **blindness (6.25%)** → HPO: *Global developmental delay* (HP:0001263), *Facial palsy* (HP:0007209), *Hearing impairment* (HP:0000365), *Blindness* (HP:0000618) (elkamah2023outliningtheclinical pages 4-7)
- Additional reported: cardiac anomalies 2/16 (12.5%), renal effects 1/16 (6%). (elkamah2023outliningtheclinical pages 4-7)

Dental findings were described in only 4 examined individuals (interpret cautiously): delayed eruption, enamel hypocalcification, high-arched palate, gingival recession, premature loss of deciduous teeth. Suggested HPO terms include *Delayed eruption of teeth* (HP:0006347), *Abnormality of dental enamel* (HP:0000682), *High arched palate* (HP:0000218), *Gingival recession* (HP:0030811), *Premature loss of deciduous teeth* (HP:0006293). (elkamah2023outliningtheclinical pages 4-7)

### 3.3 Radiologic hallmark phenotypes (HPO) and supporting figure
Radiographic features include generalized osteosclerosis/increased bone density, Erlenmeyer flask deformity, “bone-in-bone” appearance, straight mandibular angle, and acro-osteolysis. (elkamah2023outliningtheclinical pages 4-7)

**Visual evidence**: A multi-panel figure from the 2023 cohort displays these radiologic hallmarks (frontal bossing, increased density, Erlenmeyer flask deformity, bone-in-bone, acro-osteolysis). (elkamah2023outliningtheclinical media d9a10b41)

Suggested HPO terms: *Increased bone density* (HP:0010927), *Erlenmeyer flask deformity* (HP:0005612), *Bone-in-bone appearance* (HP:0002654), *Acro-osteolysis* (HP:0009777), *Abnormal mandibular morphology* (HP:0000303). (elkamah2023outliningtheclinical media d9a10b41, elkamah2023outliningtheclinical pages 4-7)

### 3.4 Age of onset, severity, progression
Presentation is typically in **early infancy** (e.g., “usually from 2.5 to 6 months-of-age” in a TCIRG1-focused review). (capo2022osteoclastrichosteopetrosis pages 1-2)
The course is **progressive and severe**, with high risk of early mortality without curative treatment. (orchard2015hematopoieticstemcell pages 1-6, balemans2005aclinicaland pages 1-2)

### 3.5 Quality-of-life impact
Quality-of-life is substantially impaired by transfusion dependence, fractures, infections, and progressive sensory loss; post-HSCT cohorts show persistent high rates of visual impairment among survivors (see Prognosis). (capo2022osteoclastrichosteopetrosis pages 5-6, orchard2015hematopoieticstemcell pages 1-6)

## 4. Genetic / molecular information

### 4.1 Causal gene(s)
- **TCIRG1** (V-ATPase V0 subunit a3; osteoclast-specific OC116 isoform) is the principal causal gene for ARO2/OPTB1. (frattini2000defectsintcirg1 pages 1-2, capo2022osteoclastrichosteopetrosis pages 1-2)

### 4.2 Pathogenic variant types and recent variant series
Multiple variant classes occur (missense, nonsense, frameshift, splice, deletions). Landmark cases include splice and frameshift/nonsense variants reported in the original Nature Genetics study. (frattini2000defectsintcirg1 pages 1-2)

A 2023 Egyptian series reported **14 TCIRG1 variants including 5 novel** across affected individuals and fetuses; notably, a missense variant p.Pro775Arg was frequent in that cohort (7/16; 44%). (elkamah2023outliningtheclinical pages 4-7)

### 4.3 Functional consequence
The dominant mechanism is **loss of function** leading to failure of osteoclast lacunar acidification and ruffled border/secretory lysosome trafficking, producing “osteoclast-rich” but non-resorbing osteoclasts. (capo2022osteoclastrichosteopetrosis pages 1-2, capo2022osteoclastrichosteopetrosis pages 3-3)

### 4.4 Modifier genes / epigenetics / chromosomal abnormalities
No validated modifier genes, epigenetic signatures, or recurrent chromosomal abnormalities specific to ARO2 were identified in the retrieved evidence.

## 5. Environmental information
No established environmental toxins, lifestyle factors, or infectious triggers were identified in the retrieved evidence for this Mendelian osteoclast disorder.

## 6. Mechanism / pathophysiology

### 6.1 Core causal chain (upstream → downstream)
1) **Biallelic TCIRG1 loss-of-function** → 2) defective V-ATPase a3–dependent **proton pumping** in osteoclast ruffled border and impaired secretory lysosome trafficking → 3) failure to acidify resorption lacuna (hydroxyapatite dissolution impaired) → 4) impaired bone resorption despite abundant multinucleated osteoclasts (“osteoclast-rich osteopetrosis”) → 5) progressive bone sclerosis and failure to remodel → 6) **marrow space obliteration and fibrosis** causing cytopenias and extramedullary hematopoiesis → 7) **cranial foramina narrowing** causing progressive cranial nerve compression (vision/hearing loss) and other complications. (capo2022osteoclastrichosteopetrosis pages 1-2, frattini2000defectsintcirg1 pages 1-2, penna2021autosomalrecessiveosteopetrosis pages 1-2)

**Direct quote supporting the mechanistic role of TCIRG1/OC116**: the Nature Genetics paper explains that V-ATPase mediates H+ transport into the resorption lacunae “*where a low pH is a prerequisite for the dissolution of hydroxyapatite crystals*.” (frattini2000defectsintcirg1 pages 1-2)

### 6.2 Cell types (CL terms suggestions)
- **Osteoclast** (CL:0000092)
- **Hematopoietic stem cell** (CL:0000037) / hematopoietic progenitor cells
- **Monocyte/macrophage lineage cells** (osteoclast precursors)
- **Mesenchymal stromal cell** (for niche alterations)

Support: patient-derived iPSC models show skewing in hematopoietic differentiation and niche-factor dysregulation relevant to engraftment biology. (zeytin2022alterationsinhematopoietic pages 1-2)

### 6.3 Biological process and cellular component suggestions (GO)
- **GO:0031589** (cell-substrate adhesion) and osteoclast cytoskeletal organization (ruffled border)
- **GO:0031929** (TOR signaling—general osteoclast biology; not directly evidenced here)
- More directly relevant (term names): *osteoclast differentiation*, *bone resorption*, *proton transmembrane transport*, *lysosomal transport/secretory lysosome trafficking*, *extramedullary hematopoiesis*

### 6.4 Bone marrow niche mechanism (engraftment relevance)
Patient-derived iPSC systems suggest that osteopetrosis involves disruption of both hematopoietic progenitor and mesenchymal stromal compartments, including altered expression of niche factors (Sdf-1, Jagged-1, Kit-L, Opn) that can be partially restored by coculture with healthy cells, providing a mechanistic basis for engraftment challenges after transplantation. (zeytin2022alterationsinhematopoietic pages 1-2)

### 6.5 Molecular profiling / multi-omics
No reproducible transcriptomic/proteomic/metabolomic signatures specific to ARO2 were identified in the retrieved evidence.

## 7. Anatomical structures affected (UBERON suggestions)

### 7.1 Organ/system level
- **Skeletal system** (bones throughout the body; diffuse osteosclerosis) (capo2022osteoclastrichosteopetrosis pages 1-2)
- **Bone marrow / hematopoietic system** (marrow cavity fibrosis/insufficient hematopoiesis) (orchard2015hematopoieticstemcell pages 1-6, capo2022osteoclastrichosteopetrosis pages 5-6)
- **Nervous system (cranial nerves; optic nerve)** due to skull foramina narrowing/impingement (orchard2015hematopoieticstemcell pages 1-6, capo2022osteoclastrichosteopetrosis pages 1-2)
- **Liver and spleen** (hepatosplenomegaly from extramedullary hematopoiesis) (orchard2015hematopoieticstemcell pages 1-6, elkamah2023outliningtheclinical pages 4-7)

### 7.2 Tissue/cell level
- Mineralized bone and osteoclast-bone interface (osteoclast ruffled border, resorption lacuna)

### 7.3 Subcellular level (GO-CC suggestions)
- **V-ATPase complex**
- **Lysosome / secretory lysosome**
- **Ruffled border membrane domain**

Support: TCIRG1 is a V-ATPase component essential for lacunar acidification and trafficking. (capo2022osteoclastrichosteopetrosis pages 1-2, frattini2000defectsintcirg1 pages 1-2)

## 8. Temporal development

### 8.1 Onset
Infantile onset is typical, reported around 2.5–6 months for severe TCIRG1-related ARO. (capo2022osteoclastrichosteopetrosis pages 1-2)

### 8.2 Progression
Progressive bone sclerosis and expanding skeletal tissue encroach on marrow and nerve foramina, leading to worsening cytopenias and neurologic deficits. (orchard2015hematopoieticstemcell pages 1-6, penna2021autosomalrecessiveosteopetrosis pages 1-2)

### 8.3 Critical period
Multiple sources emphasize the importance of **very early definitive therapy** (HSCT or potential gene therapy) to prevent irreversible cranial nerve damage. (capo2020expandedcirculatinghematopoietic pages 1-6, capo2022osteoclastrichosteopetrosis pages 5-6)

## 9. Inheritance and population

### 9.1 Inheritance
**Autosomal recessive** inheritance; affected individuals typically have biallelic pathogenic TCIRG1 variants. (capo2022osteoclastrichosteopetrosis pages 1-2, frattini2000defectsintcirg1 pages 1-2)

### 9.2 Epidemiology (statistics)
- Incidence estimates for ARO overall: **~1:250,000 live births**. (nadyrshina2023clinicalgeneticaspects pages 1-2, penna2021autosomalrecessiveosteopetrosis pages 1-2)
- Historical epidemiology for malignant ARO cited in a classic overview: **~1:200,000–1:300,000** average incidence; and a reported much higher local incidence in Costa Rica (**3.4 per 100,000**). (balemans2005aclinicaland pages 1-2)

### 9.3 Population factors
Founder effects/consanguinity can increase incidence in specific regions (e.g., Costa Rica, Middle East, Chuvash Republic) and consanguinity can be common in some cohorts. (capo2022osteoclastrichosteopetrosis pages 1-2, elkamah2023outliningtheclinical pages 4-7)

## 10. Diagnostics

### 10.1 Clinical evaluation
Red flags include early-onset macrocephaly/frontal bossing, fractures, failure to thrive, hepatosplenomegaly, cytopenias/infections/bleeding, and early visual impairment (nystagmus, inability to track). (orchard2015hematopoieticstemcell pages 1-6, elkamah2023outliningtheclinical pages 4-7)

### 10.2 Laboratory findings
- Cytopenias and marrow failure: anemia and thrombocytopenia are common; leukoerythroblastoid peripheral smear (nucleated RBCs, dacrocytes) can reflect marrow fibrosis. (capo2022osteoclastrichosteopetrosis pages 5-6, elkamah2023outliningtheclinical pages 4-7)
- Metabolic derangements may include hypocalcemia and osteopetrorickets. (capo2022osteoclastrichosteopetrosis pages 1-2, penna2021autosomalrecessiveosteopetrosis pages 1-2)

### 10.3 Imaging
Characteristic radiographs show diffuse osteosclerosis/increased density with classic signs (Erlenmeyer flask deformity, bone-in-bone, skull base sclerosis). (elkamah2023outliningtheclinical pages 4-7, chen2023casereportgene pages 4-5)

### 10.4 Pathology
- Bone marrow biopsy may show marrow fibrosis and abundant (but dysfunctional) osteoclasts; trabecular bone calcification can be prominent. (frattini2000defectsintcirg1 pages 1-2, chen2023casereportgene pages 1-2)

### 10.5 Genetic testing
Approaches in recent clinical genetics reports include:
- **Targeted TCIRG1 sequencing (coding exons and exon–intron boundaries)** using Sanger methods and reference sequences, used for diagnosis, carrier testing, and prenatal diagnosis. (elkamah2023outliningtheclinical pages 2-4)
- **Whole-exome sequencing (WES)** with ACMG interpretation and gnomAD filtering to identify biallelic TCIRG1 variants and distinguish TCIRG1 hematologic-predominant phenotypes from neurodegenerative forms (e.g., OSTM1/CLCN7). (sahinoglu2025theclinicaland pages 1-2)

### 10.6 Differential diagnosis
Conditions with overlapping presentations include other genetic osteopetroses (e.g., CLCN7, OSTM1, CA2) and hematologic disorders with cytopenias; one report notes overlap prompting consideration of juvenile myelomonocytic leukemia (JMML) and leukocyte adhesion deficiency (LAD) in differential diagnosis. (wang2023anovelcompound pages 1-2)

## 11. Outcome / prognosis

### 11.1 Natural history without definitive therapy
- Untreated ARO has high mortality; one transplant-cohort background statement reports **~70% mortality by age 6 years**, primarily from marrow failure. (orchard2015hematopoieticstemcell pages 1-6)
- A classic overview reports **~75% mortality by age 4** in malignant ARO (historical data). (balemans2005aclinicaland pages 1-2)

### 11.2 Outcomes after HSCT (real-world evidence)
From a large international series of **193 infants** transplanted 1990–2011:
- **5- and 10-year survival**: **62%/62%** after HLA-matched sibling vs **42%/39%** after alternative donors. (orchard2015hematopoieticstemcell pages 1-6)
- **Graft failure** was the leading cause of death (50% of matched-sibling deaths; 43% of alternative-donor deaths). (orchard2015hematopoieticstemcell pages 10-14)
- Among evaluable survivors: **70% visually impaired** and **10% had impaired hearing and gross motor delay**. (orchard2015hematopoieticstemcell pages 1-6)

A single-center haploidentical HSCT series (n=27) reported **5-year overall survival 73.9%**, with frequent but mostly mild acute GVHD and substantial infection burden; some sensory outcomes improved but often incompletely. (zhu2021haploidenticalhaematopoieticstem pages 4-5)

### 11.3 Prognostic factors
Donor type is a key determinant of survival in the large CIBMTR series. (orchard2015hematopoieticstemcell pages 1-6)
Pre-existing neurologic damage (e.g., vision loss) is clinically emphasized as a reason for early referral. (capo2022osteoclastrichosteopetrosis pages 5-6)

## 12. Treatment

### 12.1 Standard of care: allogeneic HSCT
HSCT corrects disease because osteoclasts derive from hematopoietic progenitors; functional osteoclast differentiation after transplant can restore remodeling and reverse pancytopenia/extramedullary hematopoiesis. (orchard2015hematopoieticstemcell pages 1-6)

Key outcome statistics and complications are summarized in the Prognosis section and include graft failure, VOD, interstitial pneumonitis, pulmonary hypertension, and calcium disturbances. (orchard2015hematopoieticstemcell pages 10-14, capo2022osteoclastrichosteopetrosis pages 5-6)

**MAXO suggestions (term names)**: Hematopoietic stem cell transplantation; Allogeneic bone marrow transplantation; Myeloablative conditioning regimen; GVHD prophylaxis; Supportive transfusion therapy.

### 12.2 Supportive / symptomatic care
Supportive management includes calcium/vitamin D management (osteopetrorickets), transfusions, antimicrobials, orthopedic and neurosurgical management, and pain management, but is not curative. (capo2022osteoclastrichosteopetrosis pages 5-6)

**Interferon-γ-1b**: A review notes that interferon gamma-1b had reduced tolerability and did not improve bone mineral density in reported use/trial context (with reference to a clinical study). (capo2022osteoclastrichosteopetrosis pages 5-6)

### 12.3 Emerging/experimental: autologous gene therapy for TCIRG1

#### 12.3.1 Clinical trial (terminated)
**NCT04525352** (Rocket Pharmaceuticals; UCLA; Phase 1; start 2020-11-19; status terminated; last update posted 2022-07-13) evaluated **autologous CD34+ cells transduced ex vivo with a lentiviral vector encoding TCIRG1 (RP-L401)** after myeloablative conditioning; discontinued due to feasibility. (NCT04525352 chunk 1)
ClinicalTrials.gov URL: https://clinicaltrials.gov/study/NCT04525352 (NCT04525352 chunk 1)

#### 12.3.2 2024 preclinical development (priority recent source)
A 2024 oc/oc neonatal mouse study reports that lentiviral gene therapy “*can revert the osteopetrotic bone phenotype, allowing long-term survival and reducing extramedullary haematopoiesis*,” and explores plerixafor mobilization and non-genotoxic conditioning to enable clinical translation in very young patients. (penna2024correctionofosteopetrosis pages 1-2)

**MAXO suggestions (term names)**: Gene therapy; Ex vivo gene transfer; Autologous hematopoietic stem cell transplantation.

## 13. Prevention
Primary prevention is not applicable in the usual sense for a Mendelian disorder, but **genetic counseling, carrier detection, and prenatal diagnosis** are key preventive strategies.
A 2023 TCIRG1 cohort reports use of **carrier detection** and **prenatal diagnosis** (amniotic fluid testing) enabling informed reproductive decisions. (elkamah2023outliningtheclinical pages 2-4)

## 14. Other species / natural disease
No naturally occurring TCIRG1 osteopetrosis in non-mouse species was identified in the retrieved evidence.

## 15. Model organisms and experimental models

### 15.1 Mouse models
- **oc/oc mouse (spontaneous Tcirg1 deletion)**: classic, severe osteopetrosis model; used widely for mechanistic studies and therapeutic development. (palagano2020generationofan pages 1-2, penna2024correctionofosteopetrosis pages 1-2)
- **Targeted Tcirg1/Atp6i disruption models** have also been used for pathogenesis and therapy development. (capo2022osteoclastrichosteopetrosis pages 1-2)
- **NSG oc/oc (immunodeficient) model**: developed to permit xenotransplantation; neonatal murine bone marrow transplant can rescue, but human CD34+ xenografts did not ameliorate bone pathology in reported work, highlighting rapid/severe course as a limitation. (palagano2020generationofan pages 1-2)

### 15.2 Patient-derived cellular models
- **Patient iPSC-derived osteoclasts** recapitulate functional defects (reduced CTSK/TRAP expression and reduced pit formation) and demonstrate rescue by transgenic TCIRG1 restoration, supporting proof-of-concept for autologous correction. (chen2019tcirg1transgenicrescue pages 1-3)
- iPSC-based niche models demonstrate defects in hematopoietic and mesenchymal stromal compartments that may relate to engraftment. (zeytin2022alterationsinhematopoietic pages 1-2)

### 15.3 Applications and limitations
These models are used to (i) validate causality and mechanism (acidification/resorption defects), (ii) optimize HSCT conditioning and engraftment strategies, and (iii) develop/test gene therapy approaches. Major limitations include rapid lethality of severe mouse models and incomplete support for human osteoclast differentiation in xenograft settings. (palagano2020generationofan pages 1-2, penna2021autosomalrecessiveosteopetrosis pages 6-7)

# Key recent developments (2023–2024 prioritized)
- **2023**: Detailed TCIRG1 cohort with phenotype frequencies, consanguinity patterns, and expanded variant spectrum (including novel variants). (elkamah2023outliningtheclinical pages 4-7)
- **2024**: Preclinical optimization of lentiviral TCIRG1 gene therapy in neonatal oc/oc mice, including mobilization and non-genotoxic conditioning strategies relevant to real-world translation. (penna2024correctionofosteopetrosis pages 1-2)

# Limitations of this report (due to retrieved evidence)
- Explicit **Orphanet ID**, **ICD-11**, and a dedicated **MeSH descriptor for osteopetrosis** were not present in the retrieved sources.
- Variant allele frequencies in population databases (gnomAD) and ClinVar classifications were described as part of methods in some reports but were not extractable as concrete per-variant AF numbers from the retrieved excerpts.
- Naturally occurring non-mouse animal cases were not identified within the retrieved evidence.



References

1. (capo2022osteoclastrichosteopetrosis pages 1-2): Valentina Capo, Mario Abinun, and Anna Villa. Osteoclast rich osteopetrosis due to defects in the tcirg1 gene. Bone, 165:116519, Dec 2022. URL: https://doi.org/10.1016/j.bone.2022.116519, doi:10.1016/j.bone.2022.116519. This article has 26 citations and is from a domain leading peer-reviewed journal.

2. (penna2021autosomalrecessiveosteopetrosis pages 1-2): Sara Penna, Anna Villa, and Valentina Capo. Autosomal recessive osteopetrosis: mechanisms and treatments. Disease Models & Mechanisms, May 2021. URL: https://doi.org/10.1242/dmm.048940, doi:10.1242/dmm.048940. This article has 70 citations and is from a domain leading peer-reviewed journal.

3. (orchard2015hematopoieticstemcell pages 1-6): Paul J. Orchard, Anders L. Fasth, Jennifer Le Rademacher, Wensheng He, Jaap Jan Boelens, Edwin M. Horwitz, Amal Al-Seraihy, Mouhab Ayas, Carmem M. Bonfim, Farid Boulad, Troy Lund, David K. Buchbinder, Neena Kapoor, Tracey A. O’Brien, Miguel A. Diaz Perez, Paul A. Veys, and Mary Eapen. Hematopoietic stem cell transplantation for infantile osteopetrosis. Blood, 126 2:270-6, Jul 2015. URL: https://doi.org/10.1182/blood-2015-01-625541, doi:10.1182/blood-2015-01-625541. This article has 130 citations and is from a highest quality peer-reviewed journal.

4. (OpenTargets Search: autosomal recessive osteopetrosis-TCIRG1): Open Targets Query (autosomal recessive osteopetrosis-TCIRG1, 6 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

5. (frattini2000defectsintcirg1 pages 1-2): Annalisa Frattini, Paul J. Orchard, Cristina Sobacchi, Silvia Giliani, Mario Abinun, Jan P. Mattsson, David J. Keeling, Ann-Katrin Andersson, Pia Wallbrandt, Luigi Zecca, Luigi D. Notarangelo, Paolo Vezzoni, and Anna Villa. Defects in tcirg1 subunit of the vacuolar proton pump are responsible for a subset of human autosomal recessive osteopetrosis. Nature Genetics, 25:343-346, Jul 2000. URL: https://doi.org/10.1038/77131, doi:10.1038/77131. This article has 871 citations and is from a highest quality peer-reviewed journal.

6. (elkamah2023outliningtheclinical pages 1-2): Ghada Y. El-Kamah, Mennat I. Mehrez, Mohamed B. Taher, Hala T. El-Bassyouni, Khaled R. Gaber, and Khalda S. Amr. Outlining the clinical profile of tcirg1 14 variants including 5 novels with overview of aro phenotype and ethnic impact in 20 egyptian families. Genes, 14:900, Apr 2023. URL: https://doi.org/10.3390/genes14040900, doi:10.3390/genes14040900. This article has 4 citations.

7. (nadyrshina2023clinicalgeneticaspects pages 1-2): D. D. Nadyrshina and R. I. Khusainova. Clinical, genetic aspects and molecular pathogenesis of osteopetrosis. Vavilov Journal of Genetics and Breeding, 27:383-392, Jul 2023. URL: https://doi.org/10.18699/vjgb-23-46, doi:10.18699/vjgb-23-46. This article has 13 citations.

8. (NCT04525352 chunk 1):  A Trial to Evaluate Safety and Efficacy of RP-L401-0120 in Subjects With Infantile Malignant Osteopetrosis. Rocket Pharmaceuticals Inc.. 2020. ClinicalTrials.gov Identifier: NCT04525352

9. (capo2022osteoclastrichosteopetrosis pages 5-6): Valentina Capo, Mario Abinun, and Anna Villa. Osteoclast rich osteopetrosis due to defects in the tcirg1 gene. Bone, 165:116519, Dec 2022. URL: https://doi.org/10.1016/j.bone.2022.116519, doi:10.1016/j.bone.2022.116519. This article has 26 citations and is from a domain leading peer-reviewed journal.

10. (elkamah2023outliningtheclinical pages 4-7): Ghada Y. El-Kamah, Mennat I. Mehrez, Mohamed B. Taher, Hala T. El-Bassyouni, Khaled R. Gaber, and Khalda S. Amr. Outlining the clinical profile of tcirg1 14 variants including 5 novels with overview of aro phenotype and ethnic impact in 20 egyptian families. Genes, 14:900, Apr 2023. URL: https://doi.org/10.3390/genes14040900, doi:10.3390/genes14040900. This article has 4 citations.

11. (penna2024correctionofosteopetrosis pages 1-2): Sara Penna, Alessandra Zecchillo, Martina Di Verniere, Elena Fontana, Valeria Iannello, Eleonora Palagano, Stefano Mantero, Andrea Cappelleri, Elena Rizzoli, Ludovica Santi, Laura Crisafulli, Marta Filibian, Antonella Forlino, Luca Basso-Ricci, Serena Scala, Eugenio Scanziani, Thorsten Schinke, Francesca Ficara, Cristina Sobacchi, Anna Villa, and Valentina Capo. Correction of osteopetrosis in the neonate oc/oc murine model after lentiviral vector gene therapy and non-genotoxic conditioning. Frontiers in Endocrinology, Sep 2024. URL: https://doi.org/10.3389/fendo.2024.1450349, doi:10.3389/fendo.2024.1450349. This article has 6 citations.

12. (elkamah2023outliningtheclinical media d9a10b41): Ghada Y. El-Kamah, Mennat I. Mehrez, Mohamed B. Taher, Hala T. El-Bassyouni, Khaled R. Gaber, and Khalda S. Amr. Outlining the clinical profile of tcirg1 14 variants including 5 novels with overview of aro phenotype and ethnic impact in 20 egyptian families. Genes, 14:900, Apr 2023. URL: https://doi.org/10.3390/genes14040900, doi:10.3390/genes14040900. This article has 4 citations.

13. (balemans2005aclinicaland pages 1-2): W. Balemans, L. Van Wesenbeeck, and W. Van Hul. A clinical and molecular overview of the human osteopetroses. Calcified Tissue International, 77:263-274, Nov 2005. URL: https://doi.org/10.1007/s00223-005-0027-6, doi:10.1007/s00223-005-0027-6. This article has 204 citations and is from a peer-reviewed journal.

14. (capo2022osteoclastrichosteopetrosis pages 3-3): Valentina Capo, Mario Abinun, and Anna Villa. Osteoclast rich osteopetrosis due to defects in the tcirg1 gene. Bone, 165:116519, Dec 2022. URL: https://doi.org/10.1016/j.bone.2022.116519, doi:10.1016/j.bone.2022.116519. This article has 26 citations and is from a domain leading peer-reviewed journal.

15. (zeytin2022alterationsinhematopoietic pages 1-2): Inci Cevher Zeytin, Berna Alkan, Cansu Ozdemir, Duygu Uckan Cetinkaya, and Fatma Visal Okur. Alterations in hematopoietic and mesenchymal stromal cell components of the osteopetrotic bone marrow niche. Stem Cells Translational Medicine, 11:310-321, Mar 2022. URL: https://doi.org/10.1093/stcltm/szab019, doi:10.1093/stcltm/szab019. This article has 10 citations and is from a domain leading peer-reviewed journal.

16. (capo2020expandedcirculatinghematopoietic pages 1-6): Valentina Capo, Sara Penna, Ivan Merelli, Matteo Barcella, Serena Scala, Luca Basso-Ricci, Elena Draghici, Eleonora Palagano, Erika Zonari, Giacomo Desantis, Paolo Uva, Roberto Cusano, Lucia Sergi Sergi, Laura Crisafulli, Despina Moshous, Polina Stepensky, Katarzyna Drabko, Zühre Kaya, Ekrem Unal, Alper Gezdirici, Giuseppe Menna, Marta Serafini, Alessandro Aiuti, Silvia Laura Locatelli, Carmelo Carlo-Stella, Ansgar S. Schulz, Francesca Ficara, Cristina Sobacchi, Bernhard Gentner, and Anna Villa. Expanded circulating hematopoietic stem/ progenitor cells as novel cell source for the treatment of tcirg1 osteopetrosis. Haematologica, 106:74-86, Jan 2020. URL: https://doi.org/10.3324/haematol.2019.238261, doi:10.3324/haematol.2019.238261. This article has 36 citations.

17. (chen2023casereportgene pages 4-5): Yu Chen, Lina Zhou, Xianmin Guan, Xianhao Wen, Jie Yu, and Ying Dou. Case report: gene mutations and clinical characteristics of four patients with osteopetrosis. Frontiers in Pediatrics, Mar 2023. URL: https://doi.org/10.3389/fped.2023.1096770, doi:10.3389/fped.2023.1096770. This article has 10 citations.

18. (chen2023casereportgene pages 1-2): Yu Chen, Lina Zhou, Xianmin Guan, Xianhao Wen, Jie Yu, and Ying Dou. Case report: gene mutations and clinical characteristics of four patients with osteopetrosis. Frontiers in Pediatrics, Mar 2023. URL: https://doi.org/10.3389/fped.2023.1096770, doi:10.3389/fped.2023.1096770. This article has 10 citations.

19. (elkamah2023outliningtheclinical pages 2-4): Ghada Y. El-Kamah, Mennat I. Mehrez, Mohamed B. Taher, Hala T. El-Bassyouni, Khaled R. Gaber, and Khalda S. Amr. Outlining the clinical profile of tcirg1 14 variants including 5 novels with overview of aro phenotype and ethnic impact in 20 egyptian families. Genes, 14:900, Apr 2023. URL: https://doi.org/10.3390/genes14040900, doi:10.3390/genes14040900. This article has 4 citations.

20. (sahinoglu2025theclinicaland pages 1-2): Esra Pekpak Şahinoğlu, Ayşe Ceyda Ören, Bahtiyar Şahinoğlu, Uğur Gümüş, Çağrı Damar, Mehmet Keskin, and Sinan Akbayram. The clinical and genetic spectrum of infantile osteopetrosis: a single-center experience including a novel tcirg1 mutation. Trends in Pediatrics, 6:151-158, Sep 2025. URL: https://doi.org/10.59213/tp.2025.249, doi:10.59213/tp.2025.249. This article has 0 citations.

21. (wang2023anovelcompound pages 1-2): Xia Wang, Yingcan Wang, Ting Xu, Yanjie Fan, Yifeng Ding, and Jihong Qian. A novel compound heterozygous mutation of the clcn7 gene is associated with autosomal recessive osteopetrosis. Frontiers in Pediatrics, Apr 2023. URL: https://doi.org/10.3389/fped.2023.978879, doi:10.3389/fped.2023.978879. This article has 5 citations.

22. (orchard2015hematopoieticstemcell pages 10-14): Paul J. Orchard, Anders L. Fasth, Jennifer Le Rademacher, Wensheng He, Jaap Jan Boelens, Edwin M. Horwitz, Amal Al-Seraihy, Mouhab Ayas, Carmem M. Bonfim, Farid Boulad, Troy Lund, David K. Buchbinder, Neena Kapoor, Tracey A. O’Brien, Miguel A. Diaz Perez, Paul A. Veys, and Mary Eapen. Hematopoietic stem cell transplantation for infantile osteopetrosis. Blood, 126 2:270-6, Jul 2015. URL: https://doi.org/10.1182/blood-2015-01-625541, doi:10.1182/blood-2015-01-625541. This article has 130 citations and is from a highest quality peer-reviewed journal.

23. (zhu2021haploidenticalhaematopoieticstem pages 4-5): Guanghua Zhu, Ang Wei, Bin Wang, Jun Yang, Yan Yan, Kai Wang, Chenguang Jia, Yanhui Luo, Sidan Li, Xuan Zhou, Tianyou Wang, Huyong Zheng, and Maoquan Qin. Haploidentical haematopoietic stem cell transplantation for malignant infantile osteopetrosis and intermediate osteopetrosis: a retrospective analysis of a single centre. Orphanet Journal of Rare Diseases, Jul 2021. URL: https://doi.org/10.1186/s13023-021-01955-6, doi:10.1186/s13023-021-01955-6. This article has 11 citations and is from a peer-reviewed journal.

24. (palagano2020generationofan pages 1-2): Eleonora Palagano, Sharon Muggeo, Laura Crisafulli, Irina L. Tourkova, Dario Strina, Stefano Mantero, Elena Fontana, Silvia L. Locatelli, Marta Monari, Emanuela Morenghi, Carmelo Carlo-Stella, John B. Barnett, Harry C. Blair, Paolo Vezzoni, Anna Villa, Cristina Sobacchi, and Francesca Ficara. Generation of an immunodeficient mouse model of tcirg1-deficient autosomal recessive osteopetrosis. Bone Reports, 12:100242, Jun 2020. URL: https://doi.org/10.1016/j.bonr.2020.100242, doi:10.1016/j.bonr.2020.100242. This article has 14 citations and is from a peer-reviewed journal.

25. (chen2019tcirg1transgenicrescue pages 1-3): Weili Chen, Kirk Twaroski, Cindy Eide, Megan J. Riddle, Paul J. Orchard, and Jakub Tolar. Tcirg1 transgenic rescue of osteoclast function using induced pluripotent stem cells derived from patients with infantile malignant autosomal recessive osteopetrosis. The Journal of bone and joint surgery. American volume, 101:1939-1947, Nov 2019. URL: https://doi.org/10.2106/jbjs.19.00558, doi:10.2106/jbjs.19.00558. This article has 16 citations.

26. (penna2021autosomalrecessiveosteopetrosis pages 6-7): Sara Penna, Anna Villa, and Valentina Capo. Autosomal recessive osteopetrosis: mechanisms and treatments. Disease Models & Mechanisms, May 2021. URL: https://doi.org/10.1242/dmm.048940, doi:10.1242/dmm.048940. This article has 70 citations and is from a domain leading peer-reviewed journal.
