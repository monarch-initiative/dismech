---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-09T10:21:13.840866'
end_time: '2026-05-09T10:37:52.499677'
duration_seconds: 998.66
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Liddle syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 32
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Liddle syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Liddle syndrome** covering all of the
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
- **Disease Name:** Liddle syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Liddle syndrome** covering all of the
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


# Comprehensive Research Report: Liddle syndrome (Mendelian)

## Executive summary
Liddle syndrome (LS) is a rare, typically autosomal-dominant, monogenic form of low-renin hypertension caused by gain-of-function variants in epithelial sodium channel (ENaC) subunits (SCNN1A/SCNN1B/SCNN1G). The canonical mechanism is disruption of the ENaC C-terminal PY motif (PPPxY) in β- or γ-ENaC, impairing NEDD4-2–mediated ubiquitination/endocytosis and increasing channel surface abundance and activity, resulting in sodium retention, hypertension, potassium wasting, metabolic alkalosis, and suppression of renin/aldosterone. Targeted therapy with ENaC blockers (amiloride, triamterene) plus sodium restriction is highly effective, while mineralocorticoid receptor antagonists are generally ineffective. Recent 2023–2024 literature emphasizes phenotypic heterogeneity (including neonatal and atypical presentations), systematic aggregation of case-level outcomes, and the practical diagnostic challenges in resource-limited settings. (lu2023aframeshiftmutation pages 1-2, ozdede2024monogenichypertensionlinked pages 5-6, steyn2023neonatalpresentationof pages 4-5, lemmensgruber2023theepithelialsodium pages 7-9)

| Category | Summary | Key details | Evidence |
|---|---|---|---|
| Disease identifiers and synonyms | Liddle syndrome is a rare Mendelian/monogenic form of hypertension caused by ENaC gain-of-function. MONDO identifier reported by Open Targets: **MONDO:0008323**; OMIM reported in retrieved literature: **OMIM #177200**. Orphanet prevalence statement available in retrieved evidence: classified as a rare disease with estimated global prevalence **<1/10^6**. ICD/MeSH identifiers were **not found in the retrieved sources used here**. Common names in retrieved literature include **Liddle syndrome**, **LS**, and descriptions such as **autosomal dominant monogenic hypertension** / **low-renin monogenic hypertension**. | MONDO disease-target association links LS with SCNN1A, SCNN1B, SCNN1G; OMIM #177200 explicitly cited in case literature; Orphanet rarity statement sourced from Hypertension founder-effect paper. | (OpenTargets Search: Liddle syndrome, pagani2018threereportedlyunrelated pages 1-2, fan2018liddlesyndromemisdiagnosed pages 1-2) |
| Causal genes and molecular mechanism | Core causal genes are **SCNN1A**, **SCNN1B**, and **SCNN1G**, encoding the α, β, and γ subunits of the epithelial sodium channel (**ENaC**). Disease mechanism is typically **gain-of-function**: variants—especially in the **PY motif (PPPxY)** of β/γ ENaC C-termini—impair **NEDD4-2/Nedd4-2** binding, reducing ubiquitination, endocytosis, and degradation, thereby increasing ENaC membrane abundance and channel activity. | Consequences: increased distal nephron sodium reabsorption, volume expansion, potassium wasting, metabolic alkalosis, suppressed renin and aldosterone. Recent reviews also note rarer **SCNN1A extracellular-domain** activating variants that increase basal ENaC activity without the classic PY-motif truncation mechanism. | (ozdede2024monogenichypertensionlinked pages 5-6, lu2023aframeshiftmutation pages 6-7, hanukoglu2023epithelialsodiumchannel pages 1-3, tian2024liddlesyndromewith pages 5-6, lemmensgruber2023theepithelialsodium pages 7-9) |
| Representative pathogenic / likely pathogenic variants in retrieved evidence | **SCNN1B**: c.1806dupG (**p.Pro603Alafs*5**) frameshift truncating β-ENaC and removing the PY motif; **SCNN1B**: c.1838delC (**p.Pro613Glnfs*675**) frameshift deleting the PY motif; **SCNN1B**: c.1852C>T (**p.Pro618Ser**) missense, pathogenic/de novo in a 2025 systematic review case, associated with atypical phenotype; **SCNN1B**: c.1711_1713delinsAA (**p.Tyr571Lysfs*105**) likely pathogenic frameshift abolishing the PY motif. | **SCNN1A**: c.1475G>A (**p.Arg492Gln**) missense reported in 2024 case review; **SCNN1A**: c.1000G>A (**p.Ala334Thr**) and c.1987A>G (**p.Thr663Ala**), plus **SCNN1B** c.1325G>T (**p.Gly442Val**) and c.7G>A (**p.Val3Met**) in a severe neonatal/compound-variant case. Variant interpretation in retrieved reports used ACMG/AMP-style criteria and segregation where available. | (lu2023aframeshiftmutation pages 1-2, steyn2023neonatalpresentationof pages 1-2, tang2025liddlesyndromewith pages 1-3, li2026novelframeshiftvariant pages 1-2, fan2018liddlesyndromemisdiagnosed pages 1-2, tian2024liddlesyndromewith pages 5-6, lu2023aframeshiftmutation pages 4-6) |
| Key clinical features | Hallmark phenotype: **early-onset, often salt-sensitive hypertension**, **hypokalemia**, **metabolic alkalosis**, **suppressed plasma renin**, and **low or inappropriately normal aldosterone**. Severity is variable; atypical presentations include **normotensive hypokalemia** and **neonatal presentation**. | Quantitative data from retrieved reviews: in one 2023 systematic review of **108 patients from 47 families**, hypertension occurred in **97.2%** and hypokalemia in **81.3%**; another review found median age **19 years** and median age at first hypertension diagnosis **17 years**. Founder effect and regional enrichment were documented in three Italian families sharing a common ancestor. | (lu2023aframeshiftmutation pages 6-7, pagani2018threereportedlyunrelated pages 1-2, tang2025liddlesyndromewith pages 1-3, steyn2023neonatalpresentationof pages 4-5) |
| Treatment and real-world implementation | First-line targeted treatment is **direct ENaC blockade** with **amiloride** or **triamterene**; **low-sodium diet** is routinely recommended. **Spironolactone/mineralocorticoid receptor antagonists are generally ineffective** because ENaC activation is aldosterone-independent. | Real-world reports show normalization or major improvement of blood pressure and potassium after amiloride/triamterene; e.g., one case normalized serum potassium within **10 days** on amiloride 10 mg/day, and family-based studies reported good long-term control without major adverse events during follow-up. In resource-limited settings, alternative antihypertensives and potassium supplementation provide only partial control when ENaC blockers are unavailable. | (lu2023aframeshiftmutation pages 1-2, prabowo2024challengesindiagnosing pages 1-2, tang2025liddlesyndromewith pages 1-3, ozdede2024monogenichypertensionlinked pages 5-6, steyn2023neonatalpresentationof pages 4-5) |


*Table: This table compiles the most actionable disease-level facts for Liddle syndrome from the retrieved evidence: identifiers, genes and mechanism, representative variants, core phenotype, and treatment. It is useful as a compact knowledge-base-ready summary with citation anchors to the supporting contexts.*

---

## 1. Disease information
### 1.1 Definition and current understanding
LS is a “monogenic hypertension” syndrome caused by ENaC hyperactivity in the distal nephron leading to aldosterone-independent sodium retention with downstream suppression of the renin–angiotensin–aldosterone system. Classic laboratory features are hyporeninemia and low (or inappropriately normal) aldosterone with hypokalemic metabolic alkalosis, although phenotype is variable. (steyn2023neonatalpresentationof pages 1-2, ozdede2024monogenichypertensionlinked pages 5-6, steyn2023neonatalpresentationof pages 4-5)

### 1.2 Key identifiers (available from retrieved sources)
- **MONDO**: **MONDO:0008323** (“Liddle syndrome”) as reported in Open Targets disease-target association output. (OpenTargets Search: Liddle syndrome)
- **OMIM**: **OMIM #177200** (explicitly reported in the retrieved Endocrine Connections case study excerpt). (fan2018liddlesyndromemisdiagnosed pages 1-2)
- **Orphanet**: Pagani et al. report LS “is classified by Orphanet as a rare disease” with an estimated global prevalence of “<1/10^6”. URL given in-text: http://www.orpha.net (as cited in the paper). (pagani2018threereportedlyunrelated pages 1-2)
- **ICD-10/ICD-11, MeSH**: **not found in the retrieved texts used here**; these should be filled by direct lookup in ICD and MeSH/NCBI resources during KB curation.

### 1.3 Synonyms / alternative names
- “Liddle syndrome”, “LS” (common). (pagani2018threereportedlyunrelated pages 1-2, fan2018liddlesyndromemisdiagnosed pages 1-2)
- Descriptive synonyms used in clinical literature: “autosomal dominant monogenic hypertension”, “low-renin hypertension / low-renin monogenic hypertension”. (lu2023aframeshiftmutation pages 1-2, ozdede2024monogenichypertensionlinked pages 5-6)

### 1.4 Evidence source type
Most information in the retrieved set is derived from:
- **Human case reports and pedigrees** with genetic testing (human clinical evidence). (lu2023aframeshiftmutation pages 1-2, steyn2023neonatalpresentationof pages 1-2, tian2024liddlesyndromewith pages 1-2)
- **Systematic reviews of published cases** (aggregated case-level evidence). (lu2023aframeshiftmutation pages 6-7)
- **Mechanistic reviews** of ENaC regulation integrating in vitro and animal-model data. (lemmensgruber2023theepithelialsodium pages 7-9)

---

## 2. Etiology
### 2.1 Disease causal factors
**Primary cause**: germline, gain-of-function variants in ENaC subunit genes **SCNN1A, SCNN1B, SCNN1G**. (lu2023aframeshiftmutation pages 1-2, ozdede2024monogenichypertensionlinked pages 2-3)

**Core mechanistic concept**: ENaC is normally downregulated through NEDD4-2 binding to PY motifs followed by ubiquitination, endocytosis and degradation. The 2023 IJMS review states: “Mutations associated with LS disrupt the PY motif in the C-terminal region of the β- or γ-subunit of ENaC, which impairs interaction of the channel with the ubiquitin ligase Nedd4-2, resulting in an increase in the expression of channels at the plasma membrane as well as an increase in channel Po”. (lemmensgruber2023theepithelialsodium pages 7-9)

### 2.2 Risk factors
- **Genetic**: carrying pathogenic/likely pathogenic ENaC variants (often truncating or frameshift variants that delete the PY motif). (lu2023aframeshiftmutation pages 1-2, lu2023aframeshiftmutation pages 4-6)
- **Family history** of early-onset or resistant hypertension is a major clinical clue in monogenic hypertension reviews. (ozdede2024monogenichypertensionlinked pages 2-3)
- **Salt intake** likely modulates severity because LS is described as salt-sensitive hypertension in multiple sources. (ozdede2024monogenichypertensionlinked pages 5-6, pagani2018threereportedlyunrelated pages 1-2)

### 2.3 Protective factors
No specific genetic “protective variants” were identified in the retrieved evidence set. Clinically, **sodium restriction** and **ENaC blockade** are disease-modifying and can prevent complications by controlling the downstream physiologic effects. (steyn2023neonatalpresentationof pages 4-5)

### 2.4 Gene–environment interactions
The retrieved set supports a plausible interaction between genotype-driven ENaC hyperactivity and **dietary sodium exposure** (salt-sensitivity), but it does not provide quantitative gene–environment interaction estimates. (pagani2018threereportedlyunrelated pages 1-2)

---

## 3. Phenotypes
### 3.1 Core phenotypic spectrum (with suggested HPO terms)
**Symptoms / clinical signs**
- Early-onset hypertension / salt-sensitive hypertension (HP:0000822 *Hypertension*; HP:0002633 *Elevated blood pressure*). (lu2023aframeshiftmutation pages 1-2, ozdede2024monogenichypertensionlinked pages 5-6)
- Muscle weakness (often secondary to hypokalemia) (HP:0001324 *Muscle weakness*). (prabowo2024challengesindiagnosing pages 1-2)

**Laboratory abnormalities**
- Hypokalemia (HP:0002900 *Hypokalemia*). (lu2023aframeshiftmutation pages 1-2, lu2023aframeshiftmutation pages 6-7)
- Metabolic alkalosis (HP:0001943 *Metabolic alkalosis*). (lu2023aframeshiftmutation pages 1-2, ozdede2024monogenichypertensionlinked pages 5-6)
- Low plasma renin / suppressed renin (HP:0031733 *Decreased renin activity*; term may vary by HPO version) and low aldosterone (HP:0003359 *Decreased aldosterone level*). (ozdede2024monogenichypertensionlinked pages 5-6, steyn2023neonatalpresentationof pages 4-5)
- Hypernatremia can occur in severe presentations (HP:0001987 *Hypernatremia*). (prabowo2024challengesindiagnosing pages 1-2)

### 3.2 Age of onset and progression
- Typical diagnosis is often during adolescence/young adulthood; one systematic review summarized median hypertension onset at ~18 years (IQR 14–23.5). (lu2023aframeshiftmutation pages 6-7)
- Neonatal presentation is possible; a 5-day-old neonate with severe hypernatremic dehydration later developed features consistent with LS. (steyn2023neonatalpresentationof pages 1-2)
- Phenotype is variable; atypical presentations include hypokalemia without hypertension. (tang2025liddlesyndromewith pages 1-3)

### 3.3 Frequency statistics from recent aggregated evidence
A 2023 systematic review of SCNN1B-related LS cases summarized **108 patients from 47 families**; **hypertension 97.2%** and **hypokalemia 81.3%** were reported in the excerpted results. (lu2023aframeshiftmutation pages 6-7)

### 3.4 Quality-of-life impact
Formal QoL instruments (SF-36/EQ-5D/PROMIS) were not reported in the retrieved LS-focused texts. Indirectly, uncontrolled disease can cause repeated admissions and chronic morbidity (e.g., poor adherence leading to numerous admissions in a pediatric case; persistent symptoms without ENaC blockers in a resource-limited setting). (steyn2023neonatalpresentationof pages 1-2, prabowo2024challengesindiagnosing pages 3-6)

---

## 4. Genetic / molecular information
### 4.1 Causal genes (HGNC symbols)
- **SCNN1A** (ENaC α subunit) (steyn2023neonatalpresentationof pages 1-2, tian2024liddlesyndromewith pages 1-2)
- **SCNN1B** (ENaC β subunit) (lu2023aframeshiftmutation pages 1-2, fan2018liddlesyndromemisdiagnosed pages 1-2)
- **SCNN1G** (ENaC γ subunit) (ozdede2024monogenichypertensionlinked pages 5-6, lemmensgruber2023theepithelialsodium pages 7-9)

Open Targets lists these genes as associated targets for LS (MONDO:0008323) and provides supporting PubMed IDs for association evidence (legacy/landmark literature). (OpenTargets Search: Liddle syndrome)

### 4.2 Pathogenic variant classes and consequences
- **Variant classes** include frameshift/truncating variants that eliminate the PY motif (classic), and missense variants that can increase ENaC basal activity or alter regulation. (tian2024liddlesyndromewith pages 5-6, lu2023aframeshiftmutation pages 4-6)
- **Functional consequence**: ENaC gain-of-function via increased membrane density and/or increased open probability (Po). (lemmensgruber2023theepithelialsodium pages 7-9, hanukoglu2023epithelialsodiumchannel pages 1-3)

### 4.3 Representative variants from retrieved sources (examples)
- **SCNN1B c.1806dupG (p.Pro603Alafs*5)**; truncation with loss of PY motif (family study + systematic review). (lu2023aframeshiftmutation pages 1-2)
- **SCNN1B c.1838delC (p.Pro613Glnfs*675)**; deletion of PY motif with protein elongation (misdiagnosed PA family). (fan2018liddlesyndromemisdiagnosed pages 1-2)
- **SCNN1A c.1475G>A (p.Arg492Gln)**; extracellular-domain missense (2024 case report; absent from population datasets cited by authors). (tian2024liddlesyndromewith pages 5-6)
- Multivariant/compound cases have been described (e.g., neonatal presentation with multiple ENaC variants across subunits). (steyn2023neonatalpresentationof pages 1-2)

### 4.4 Modifier genes / epigenetics / chromosomal abnormalities
No LS-specific modifier-gene, epigenetic, or chromosomal-abnormality findings were identified in the retrieved corpus.

---

## 5. Environmental information
LS is primarily genetic. Environmental/lifestyle modifiers most strongly supported in the retrieved corpus are:
- **Dietary sodium exposure** (salt sensitivity) as a severity modifier and treatment target (low-sodium diet). (ozdede2024monogenichypertensionlinked pages 5-6, prabowo2024challengesindiagnosing pages 3-6)
No infectious triggers were reported.

---

## 6. Mechanism / pathophysiology
### 6.1 Causal chain (upstream → downstream)
1. **Germline ENaC gain-of-function variant** (often β/γ PY-motif disruption). (lemmensgruber2023theepithelialsodium pages 7-9)
2. **Impaired NEDD4-2 binding → reduced ubiquitination/endocytosis/degradation → increased ENaC surface expression**, potentially increased Po. (lemmensgruber2023theepithelialsodium pages 7-9, hanukoglu2023epithelialsodiumchannel pages 1-3)
3. **Increased Na+ reabsorption in aldosterone-sensitive distal nephron** → extracellular volume expansion → **hypertension** with **suppressed renin and aldosterone** (secondary downregulation). (ozdede2024monogenichypertensionlinked pages 5-6, steyn2023neonatalpresentationof pages 4-5)
4. Coupled changes in distal nephron ion handling increase K+ secretion → **hypokalemia** and **metabolic alkalosis**. (ozdede2024monogenichypertensionlinked pages 5-6)

### 6.2 Molecular pathways and terms
Suggested GO Biological Process terms (examples; to be confirmed against GO IDs during KB build):
- **Regulation of sodium ion transmembrane transport** (GO:1904062 or related)
- **Ubiquitin-dependent protein catabolic process** (GO:0006511)
- **Endocytosis** (GO:0006897)
- **Regulation of blood pressure** (GO:0008217)

### 6.3 Cellular processes and cell types
- Primary affected epithelial cell type: **renal collecting duct principal cell** (Cell Ontology suggestion: CL:0000066 *renal principal cell*; verify current CL label).
- Key anatomical locus: **aldosterone-sensitive distal nephron / collecting duct** (UBERON suggestions: UBERON:0001285 *kidney collecting duct*; UBERON:0001225 *kidney*).

### 6.4 Visual mechanistic evidence (2023)
A schematic of ENaC regulation (including regulators such as Nedd4-2/SGK1) and a phosphorylation-site figure for α-ENaC were extracted from the 2023 IJMS review; these figures are useful for KB “mechanism” visualization and annotation support. (lemmensgruber2023theepithelialsodium media 822226f3, lemmensgruber2023theepithelialsodium media a9459ffe)

---

## 7. Anatomical structures affected
**Organ/system level**
- Primary: **Kidney (distal nephron/collecting duct)** and **cardiovascular system** (hypertension/end-organ risk). (ozdede2024monogenichypertensionlinked pages 5-6, pagani2018threereportedlyunrelated pages 1-2)

**Tissue/cell level**
- Distal nephron epithelium, especially ENaC-expressing segments; mechanism is described as ENaC accumulation at the apical membrane of the distal nephron. (ozdede2024monogenichypertensionlinked pages 5-6)

**Subcellular level**
- **Plasma membrane / apical membrane** ENaC abundance changes are central to pathogenesis. (ozdede2024monogenichypertensionlinked pages 5-6, lemmensgruber2023theepithelialsodium pages 7-9)

---

## 8. Temporal development
- **Onset**: often in childhood/adolescence; but neonatal onset has been reported. (steyn2023neonatalpresentationof pages 1-2, lu2023aframeshiftmutation pages 6-7)
- **Course**: chronic; complications arise from prolonged uncontrolled hypertension and electrolyte disturbances. Systematic follow-up data suggest that with targeted therapy, abnormal BP and serious adverse events may be prevented over ≥1 year follow-up windows in aggregated case series. (lu2023aframeshiftmutation pages 6-7)

---

## 9. Inheritance and population
### 9.1 Inheritance, penetrance, expressivity
- LS is repeatedly described as **autosomal dominant** in case reviews/systematic reviews. (lu2023aframeshiftmutation pages 1-2, ozdede2024monogenichypertensionlinked pages 2-3)
- **Variable expressivity / incomplete penetrance** is supported by reports of mutation carriers with normal blood pressure and by broad phenotype variability even within the same genotype. (steyn2023neonatalpresentationof pages 4-5, lu2023aframeshiftmutation pages 4-6)

### 9.2 Epidemiology / prevalence
- Orphanet classification in a leading Hypertension paper: global prevalence estimated **<1/10^6** (Orpha.net referenced). (pagani2018threereportedlyunrelated pages 1-2)
- A 2024 case report from Indonesia cites a prevalence estimate of **0.91%–1.52%**, but the excerpt does not clarify whether this is population prevalence or an enriched clinical cohort; this value should be interpreted cautiously and cross-checked against the primary epidemiology sources it cites. (prabowo2024challengesindiagnosing pages 1-2)

### 9.3 Founder effects / geographic enrichment
- A founder effect was documented in three Italian families, with a shared haplotype and an inferred common ancestor (~13 generations), implying local enrichment and potential underdiagnosis in the area. (pagani2018threereportedlyunrelated pages 1-2, pagani2018threereportedlyunrelated pages 7-11)

---

## 10. Diagnostics
### 10.1 Clinical/laboratory diagnostics
Typical diagnostic laboratory profile (pattern recognition):
- Hypertension with **hypokalemic metabolic alkalosis** (ozdede2024monogenichypertensionlinked pages 5-6)
- **Suppressed renin and aldosterone** (low renin/low aldosterone phenotype) (ozdede2024monogenichypertensionlinked pages 5-6, ozdede2024monogenichypertensionlinked pages 2-3)
- Supportive urinary measures: a **low urine aldosterone-to-potassium ratio** is noted as typical in affected individuals. (steyn2023neonatalpresentationof pages 4-5)

### 10.2 Differential diagnosis (key mimics)
Recent review content highlights differential diagnoses for low-renin hypokalemic hypertension including apparent mineralocorticoid excess (including licorice ingestion), congenital adrenal hyperplasia variants, familial cortisol resistance, and deoxycorticosterone-producing adrenal tumors. (ozdede2024monogenichypertensionlinked pages 5-6)

### 10.3 Genetic testing
- **Targeted sequencing** of SCNN1A/SCNN1B/SCNN1G is recommended in phenotype-driven approaches to monogenic hypertension. (ozdede2024monogenichypertensionlinked pages 2-3)
- Several reports demonstrate use of **WES/panels plus Sanger segregation testing** and **ACMG/AMP** criteria to classify variants (e.g., PVS1/PM2/PP1/PP3 in a truncating SCNN1B variant). (lu2023aframeshiftmutation pages 4-6)
- Resource-limited settings may rely on clinical/lab patterns and lack of response to spironolactone as a pragmatic clue, but the same report emphasizes that definitive diagnosis relies on genetic sequencing when available. (prabowo2024challengesindiagnosing pages 3-6)

---

## 11. Outcome / prognosis
Quantitative survival/life expectancy statistics were not available in the retrieved corpus. However:
- Case-based systematic evidence suggests that with targeted ENaC blockade, blood pressure and potassium often normalize, potentially preventing short-term clinical endpoint events in follow-up cohorts. (lu2023aframeshiftmutation pages 1-2, lu2023aframeshiftmutation pages 6-7)
- Inadequate access to ENaC blockers or poor adherence can lead to persistent electrolyte abnormalities and suboptimal control, which is expected to increase long-term risk (hypertensive end-organ complications). (steyn2023neonatalpresentationof pages 1-2, prabowo2024challengesindiagnosing pages 3-6)

---

## 12. Treatment
### 12.1 Pharmacotherapy (standard of care)
**Direct ENaC blockers**
- **Amiloride** (drug class: potassium-sparing diuretic/ENaC inhibitor): repeatedly reported as effective in improving blood pressure and correcting hypokalemia; one report describes potassium normalization within 10 days on amiloride 10 mg/day. (tang2025liddlesyndromewith pages 1-3)
- **Triamterene** (ENaC inhibitor): reported to significantly improve blood pressure control and normalize potassium in a SCNN1A-related LS case report. (tian2024liddlesyndromewith pages 1-2)

**Therapies often ineffective**
- **Mineralocorticoid receptor antagonists (e.g., spironolactone)** are noted as generally ineffective because ENaC activation is aldosterone-independent in LS. (ozdede2024monogenichypertensionlinked pages 5-6, steyn2023neonatalpresentationof pages 4-5)

**Non-pharmacologic**
- **Low-sodium diet** is a common recommendation, especially important when ENaC blockers are unavailable or as adjunct therapy. (prabowo2024challengesindiagnosing pages 3-6, steyn2023neonatalpresentationof pages 4-5)

### 12.2 Real-world implementation considerations (2024)
A 2024 resource-limited setting case report highlights that lack of access to ENaC blockers can force reliance on alternative antihypertensives and potassium supplementation with only modest improvement and persistent biochemical abnormalities, underscoring the importance of access to targeted therapy. (prabowo2024challengesindiagnosing pages 3-6)

### 12.3 MAXO term suggestions (examples)
- **ENaC inhibitor therapy / potassium-sparing diuretic therapy** (MAXO: “amiloride therapy”, “triamterene therapy” — verify exact MAXO IDs)
- **Dietary sodium restriction** (MAXO: “low sodium diet therapy” — verify)
- **Genetic counseling** (MAXO: genetic counseling intervention)

---

## 13. Prevention
Given the Mendelian etiology, prevention focuses on:
- **Secondary prevention**: early recognition of the phenotype (young-onset/resistant hypertension with hypokalemic alkalosis and low renin/aldosterone), early genetic confirmation, and prompt ENaC blockade to prevent end-organ damage. (steyn2023neonatalpresentationof pages 4-5, ozdede2024monogenichypertensionlinked pages 2-3)
- **Cascade screening / family screening** following identification of a pathogenic variant. (lu2023aframeshiftmutation pages 4-6)
- **Tertiary prevention**: sustained BP and electrolyte control via ENaC inhibition and sodium restriction to reduce complications. (lu2023aframeshiftmutation pages 1-2)

---

## 14. Other species / natural disease
The retrieved corpus did not contain clear evidence of naturally occurring LS analogs in non-human species.

---

## 15. Model organisms / experimental systems
### 15.1 Functional testing systems used in LS/ENaC research
- **Xenopus oocyte expression system** is repeatedly used for functional characterization of ENaC variants and ENaC regulation in the 2023 review. (lemmensgruber2023theepithelialsodium pages 13-15)
- Mouse kidney tissue/animal-model work is referenced in the ENaC ubiquitination discussion (e.g., ubiquitination studies in mouse/rat kidney and an LS mutation model referenced in the 2023 review). (lemmensgruber2023theepithelialsodium pages 7-9)

### 15.2 Translational landscape
A 2023 ENaC drug-target review notes that “Numerous test compounds have revealed encouraging results in vitro and in animal models but less in clinical settings” in the broader ENaC pharmacology landscape, indicating a gap between mechanistic ENaC modulation and clinical translation beyond established ENaC blockers. (lemmensgruber2023theepithelialsodium pages 1-2)

---

## Recent developments and “latest research” highlights (2023–2024)
1. **Systematic case aggregation (2023)**: A 2023 systematic review summarized 108 patients/47 families with SCNN1B pathogenic variants and reported high frequencies of hypertension (97.2%) and hypokalemia (81.3%), supporting both typical presentation and heterogeneity. (lu2023aframeshiftmutation pages 6-7)
2. **Neonatal/compound-variant presentation (2023)**: A neonatal case report described severe early presentation and later recognition based on response to amiloride, emphasizing diagnostic vigilance in pediatrics and interpretation challenges with multiple variants across ENaC subunits. (steyn2023neonatalpresentationof pages 1-2, steyn2023neonatalpresentationof pages 4-5)
3. **Mechanistic consolidation and ENaC regulation review (2023)**: The IJMS review provides updated mechanistic framing of PY motif–NEDD4-2 regulation and other ENaC modulators (post-translational modifications, kinases), which may inform future therapeutics. (lemmensgruber2023theepithelialsodium pages 7-9, lemmensgruber2023theepithelialsodium pages 9-11)
4. **Monogenic hypertension phenotype-driven diagnosis (2024)**: A 2024 review emphasizes recognition of low-renin/low-aldosterone patterns and targeted ENaC-blocker treatment; it also outlines key differential diagnoses for hypokalemic hypertension. (ozdede2024monogenichypertensionlinked pages 5-6, ozdede2024monogenichypertensionlinked pages 2-3)
5. **Implementation gap (2024)**: A 2024 case report from Indonesia highlights practical barriers to genetic testing and ENaC-blocker access, with measurable clinical consequences, arguing for health-system improvements. (prabowo2024challengesindiagnosing pages 3-6)

---

## Clinical trials / registries and real-world data infrastructure
- **NCT00448162 (Peking Union Medical College; observational; suspended)**: Designed to identify Chinese ENaC mutation “hotspots” causing LS and assess ENaC polymorphisms associated with hypertension; planned enrollment 2,000; suspended due to insufficient funding. (NCT00448162 chunk 1)
- **NCT06065852 (RaDaR, UK National Registry of Rare Kidney Diseases; recruiting)**: Large observational registry (estimated enrollment 35,000; 2009–2039) explicitly including LS, designed to collect longitudinal clinical data and can collect DNA in some groups; supports epidemiology, guideline development, and trial readiness. (NCT06065852 chunk 1)

---

## Limitations of this tool-based extraction
- ICD and MeSH identifiers, and an Orphanet numeric ID (ORPHA code), were not present in the retrieved full texts; these should be added via direct authoritative database lookup (OMIM/Orphanet/ICD/MeSH portals).
- Many mechanistic claims are supported by reviews that cite classic primary literature; the present extraction includes some legacy PubMed IDs via Open Targets but does not retrieve and quote those original primary articles directly. (OpenTargets Search: Liddle syndrome)


References

1. (lu2023aframeshiftmutation pages 1-2): Yiting Lu, Xinchang Liu, Lin Sun, Di Zhang, Peng Fan, Kunqi Yang, Lin Zhang, Yaxin Liu, and Xianliang Zhou. A frameshift mutation in the scnn1b gene in a family with liddle syndrome: a case report and systematic review. Molecular Medicine Reports, Dec 2023. URL: https://doi.org/10.3892/mmr.2023.13142, doi:10.3892/mmr.2023.13142. This article has 5 citations and is from a peer-reviewed journal.

2. (ozdede2024monogenichypertensionlinked pages 5-6): Murat Özdede. Monogenic hypertension linked to the renin–angiotensin–aldosterone system. Anatolian Journal of Cardiology, 28:417-428, Jun 2024. URL: https://doi.org/10.14744/anatoljcardiol.2024.4480, doi:10.14744/anatoljcardiol.2024.4480. This article has 0 citations.

3. (steyn2023neonatalpresentationof pages 4-5): Nicolene Steyn, Bettina Chale-Matsau, Aron B. Abera, Gertruida Van Biljon, and Tahir S. Pillay. Neonatal presentation of a patient with liddle syndrome, south africa. African Journal of Laboratory Medicine, Apr 2023. URL: https://doi.org/10.4102/ajlm.v12i1.1998, doi:10.4102/ajlm.v12i1.1998. This article has 5 citations.

4. (lemmensgruber2023theepithelialsodium pages 7-9): Rosa Lemmens-Gruber and Susan Tzotzos. The epithelial sodium channel—an underestimated drug target. International Journal of Molecular Sciences, 24:7775, Apr 2023. URL: https://doi.org/10.3390/ijms24097775, doi:10.3390/ijms24097775. This article has 29 citations.

5. (OpenTargets Search: Liddle syndrome): Open Targets Query (Liddle syndrome, 10 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

6. (pagani2018threereportedlyunrelated pages 1-2): Luca Pagani, Yoan Diekmann, Marco Sazzini, Sara De Fanti, Maurizio Rondinelli, Enrico Farnetti, Bruno Casali, Amelia Caretto, Francesca Novara, Orsetta Zuffardi, Paolo Garagnani, Franco Mantero, Mark G. Thomas, Donata Luiselli, and Ermanno Rossi. Three reportedly unrelated families with liddle syndrome inherited from a common ancestor. Hypertension, 71:273–279, Feb 2018. URL: https://doi.org/10.1161/hypertensionaha.117.10491, doi:10.1161/hypertensionaha.117.10491. This article has 25 citations and is from a domain leading peer-reviewed journal.

7. (fan2018liddlesyndromemisdiagnosed pages 1-2): Peng Fan, Chao-Xia Lu, Di Zhang, Kun-Qi Yang, Pei-Pei Lu, Ying Zhang, Xu Meng, Su-Fang Hao, Fang Luo, Ya-Xin Liu, Hui-Min Zhang, Lei Song, Jun Cai, Xue Zhang, and Xian-Liang Zhou. Liddle syndrome misdiagnosed as primary aldosteronism resulting from a novel frameshift mutation of scnn1b. Endocrine Connections, 7:1528-1534, Dec 2018. URL: https://doi.org/10.1530/ec-18-0484, doi:10.1530/ec-18-0484. This article has 17 citations and is from a peer-reviewed journal.

8. (lu2023aframeshiftmutation pages 6-7): Yiting Lu, Xinchang Liu, Lin Sun, Di Zhang, Peng Fan, Kunqi Yang, Lin Zhang, Yaxin Liu, and Xianliang Zhou. A frameshift mutation in the scnn1b gene in a family with liddle syndrome: a case report and systematic review. Molecular Medicine Reports, Dec 2023. URL: https://doi.org/10.3892/mmr.2023.13142, doi:10.3892/mmr.2023.13142. This article has 5 citations and is from a peer-reviewed journal.

9. (hanukoglu2023epithelialsodiumchannel pages 1-3): I Hanukoglu. Epithelial sodium channel (enac) in gtopdb v. 2023.1. Unknown journal, 2023.

10. (tian2024liddlesyndromewith pages 5-6): Jiajia Tian, Fei Xiang, Liandi Wang, Xueyi Wu, Lijuan Shao, Li Ma, and Chuwen Fang. Liddle syndrome with a scnn1a mutation: a case report and literature review. Kidney & blood pressure research, 49:1-16, Sep 2024. URL: https://doi.org/10.1159/000540522, doi:10.1159/000540522. This article has 2 citations and is from a peer-reviewed journal.

11. (steyn2023neonatalpresentationof pages 1-2): Nicolene Steyn, Bettina Chale-Matsau, Aron B. Abera, Gertruida Van Biljon, and Tahir S. Pillay. Neonatal presentation of a patient with liddle syndrome, south africa. African Journal of Laboratory Medicine, Apr 2023. URL: https://doi.org/10.4102/ajlm.v12i1.1998, doi:10.4102/ajlm.v12i1.1998. This article has 5 citations.

12. (tang2025liddlesyndromewith pages 1-3): Qian Tang, Yangfan Zhou, Lin Liu, Min Chen, Lin Liu, Yan Wang, Guangju Zhou, and Meijun Xie. Liddle syndrome with a scnn1b mutation: a case report and systematic review. BMC Nephrology, Jul 2025. URL: https://doi.org/10.1186/s12882-025-04252-7, doi:10.1186/s12882-025-04252-7. This article has 3 citations and is from a peer-reviewed journal.

13. (li2026novelframeshiftvariant pages 1-2): Ai Li, Xiaoli Wang, and Jing Li. Novel frameshift variant in the β subunit of epithelial sodium channels uncovers liddle syndrome in a young patient with metabolic syndrome: a case report with review of literature. Endocrine Journal, 73:571-576, Jan 2026. URL: https://doi.org/10.1507/endocrj.ej25-0509, doi:10.1507/endocrj.ej25-0509. This article has 0 citations and is from a peer-reviewed journal.

14. (lu2023aframeshiftmutation pages 4-6): Yiting Lu, Xinchang Liu, Lin Sun, Di Zhang, Peng Fan, Kunqi Yang, Lin Zhang, Yaxin Liu, and Xianliang Zhou. A frameshift mutation in the scnn1b gene in a family with liddle syndrome: a case report and systematic review. Molecular Medicine Reports, Dec 2023. URL: https://doi.org/10.3892/mmr.2023.13142, doi:10.3892/mmr.2023.13142. This article has 5 citations and is from a peer-reviewed journal.

15. (prabowo2024challengesindiagnosing pages 1-2): Nurhasan A. Prabowo, Wachid Putranto, Risalina Myrtha, Tonang D. Ardyanto, Coana S. Gautama, Evi L. Wulandari, Berty D. Hermawati, Desy P. Putri, Artika Ramadhani, and Herlina K. Dewi. Challenges in diagnosing and treating liddle syndrome in resource-limited settings: a case report from indonesia. Narra J, 4:e1000, Oct 2024. URL: https://doi.org/10.52225/narra.v4i3.1000, doi:10.52225/narra.v4i3.1000. This article has 5 citations.

16. (tian2024liddlesyndromewith pages 1-2): Jiajia Tian, Fei Xiang, Liandi Wang, Xueyi Wu, Lijuan Shao, Li Ma, and Chuwen Fang. Liddle syndrome with a scnn1a mutation: a case report and literature review. Kidney & blood pressure research, 49:1-16, Sep 2024. URL: https://doi.org/10.1159/000540522, doi:10.1159/000540522. This article has 2 citations and is from a peer-reviewed journal.

17. (ozdede2024monogenichypertensionlinked pages 2-3): Murat Özdede. Monogenic hypertension linked to the renin–angiotensin–aldosterone system. Anatolian Journal of Cardiology, 28:417-428, Jun 2024. URL: https://doi.org/10.14744/anatoljcardiol.2024.4480, doi:10.14744/anatoljcardiol.2024.4480. This article has 0 citations.

18. (prabowo2024challengesindiagnosing pages 3-6): Nurhasan A. Prabowo, Wachid Putranto, Risalina Myrtha, Tonang D. Ardyanto, Coana S. Gautama, Evi L. Wulandari, Berty D. Hermawati, Desy P. Putri, Artika Ramadhani, and Herlina K. Dewi. Challenges in diagnosing and treating liddle syndrome in resource-limited settings: a case report from indonesia. Narra J, 4:e1000, Oct 2024. URL: https://doi.org/10.52225/narra.v4i3.1000, doi:10.52225/narra.v4i3.1000. This article has 5 citations.

19. (lemmensgruber2023theepithelialsodium media 822226f3): Rosa Lemmens-Gruber and Susan Tzotzos. The epithelial sodium channel—an underestimated drug target. International Journal of Molecular Sciences, 24:7775, Apr 2023. URL: https://doi.org/10.3390/ijms24097775, doi:10.3390/ijms24097775. This article has 29 citations.

20. (lemmensgruber2023theepithelialsodium media a9459ffe): Rosa Lemmens-Gruber and Susan Tzotzos. The epithelial sodium channel—an underestimated drug target. International Journal of Molecular Sciences, 24:7775, Apr 2023. URL: https://doi.org/10.3390/ijms24097775, doi:10.3390/ijms24097775. This article has 29 citations.

21. (pagani2018threereportedlyunrelated pages 7-11): Luca Pagani, Yoan Diekmann, Marco Sazzini, Sara De Fanti, Maurizio Rondinelli, Enrico Farnetti, Bruno Casali, Amelia Caretto, Francesca Novara, Orsetta Zuffardi, Paolo Garagnani, Franco Mantero, Mark G. Thomas, Donata Luiselli, and Ermanno Rossi. Three reportedly unrelated families with liddle syndrome inherited from a common ancestor. Hypertension, 71:273–279, Feb 2018. URL: https://doi.org/10.1161/hypertensionaha.117.10491, doi:10.1161/hypertensionaha.117.10491. This article has 25 citations and is from a domain leading peer-reviewed journal.

22. (lemmensgruber2023theepithelialsodium pages 13-15): Rosa Lemmens-Gruber and Susan Tzotzos. The epithelial sodium channel—an underestimated drug target. International Journal of Molecular Sciences, 24:7775, Apr 2023. URL: https://doi.org/10.3390/ijms24097775, doi:10.3390/ijms24097775. This article has 29 citations.

23. (lemmensgruber2023theepithelialsodium pages 1-2): Rosa Lemmens-Gruber and Susan Tzotzos. The epithelial sodium channel—an underestimated drug target. International Journal of Molecular Sciences, 24:7775, Apr 2023. URL: https://doi.org/10.3390/ijms24097775, doi:10.3390/ijms24097775. This article has 29 citations.

24. (lemmensgruber2023theepithelialsodium pages 9-11): Rosa Lemmens-Gruber and Susan Tzotzos. The epithelial sodium channel—an underestimated drug target. International Journal of Molecular Sciences, 24:7775, Apr 2023. URL: https://doi.org/10.3390/ijms24097775, doi:10.3390/ijms24097775. This article has 29 citations.

25. (NCT00448162 chunk 1):  The Chinese Mutation Hotspot of ENaC Causing Liddle's Syndrome and the Association of ENaC Variations and Hypertension. Peking Union Medical College. 2005. ClinicalTrials.gov Identifier: NCT00448162

26. (NCT06065852 chunk 1):  National Registry of Rare Kidney Diseases. UK Kidney Association. 2009. ClinicalTrials.gov Identifier: NCT06065852
