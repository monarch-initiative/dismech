---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-05T14:33:07.096608'
end_time: '2026-04-05T14:38:50.590465'
duration_seconds: 343.49
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: EBV-Associated Gastric Cancer
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 31
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** EBV-Associated Gastric Cancer
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **EBV-Associated Gastric Cancer** covering all of the
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
- **Disease Name:** EBV-Associated Gastric Cancer
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **EBV-Associated Gastric Cancer** covering all of the
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


# EBV-Associated Gastric Cancer (EBVaGC) — Disease Characteristics Research Report (2023–2024 prioritized)

## Target Disease
- **Disease name:** Epstein–Barr virus (EBV)-associated gastric cancer (EBVaGC) / EBV-positive gastric carcinoma
- **Category:** Infection-associated epithelial malignancy; molecular subtype of gastric adenocarcinoma
- **MONDO ID:** Not identified from the retrieved evidence in this run (additional ontology lookup required).

## 1. Disease information
### Overview (what is the disease?)
EBV-associated gastric cancer (EBVaGC) is a molecularly and clinicopathologically distinct subset of gastric cancer defined by the presence of EBV infection within the malignant epithelial (tumor) cells, typically demonstrated by in situ hybridization for EBV-encoded small RNAs (EBER) (saito2021landscapeofebvpositive pages 1-2, li2023assessingepstein–barrvirus pages 1-2). It is recognized as one of the major molecular subtypes in The Cancer Genome Atlas (TCGA) gastric cancer classification (saito2021landscapeofebvpositive pages 1-2, lee2024associationofpdl1 pages 1-2).

### Synonyms / alternative names
- EBV-positive gastric cancer (EBV(+) GC) (saito2021landscapeofebvpositive pages 1-2)
- EBV-associated gastric carcinoma (EBVaGC) (bai2022efficacyandpredictive pages 1-2)
- Gastric carcinoma with lymphoid stroma (GCLS) / carcinoma with lymphoid stroma (CLS) when presenting with prominent lymphoid infiltration (park2023geneticlandscapeand pages 1-2, lee2024associationofpdl1 pages 1-2)
- Lymphoepithelioma-like carcinoma (LELC) pattern in stomach (often overlaps with GCLS conceptually) (corallo2024unlockingthepotential pages 6-8, saito2021landscapeofebvpositive pages 1-2)

### Key identifiers (status)
- **ICD/MeSH/OMIM/Orphanet/MONDO:** Not reliably extractable from the retrieved primary/full-text evidence in this run; this report therefore focuses on primary literature definitions and diagnostic criteria.

### Evidence provenance
The information in this report is derived from **aggregated disease-level primary literature** (cohort studies, meta-analyses, and mechanistic studies), plus a small number of prospective/observational immunotherapy cohorts and clinical trial registry entries (xie2020positivestatusof pages 1-2, bai2022efficacyandpredictive pages 1-2, pyo2023prognosticimplicationof pages 1-2).


## 2. Etiology
### Primary causal factor
EBVaGC is causally linked to **EBV infection of gastric epithelial cells** with maintenance of EBV genomes/latency-associated gene expression in tumor cells; EBVaGC is considered an “infection-associated” cancer subtype with distinct molecular/immune features (salnikov2024theviraletiology pages 1-2).

### Risk factors
- **Infectious:** EBV infection in tumor cells is the defining etiologic factor; EBV positivity is observed in ~5–10% of gastric cancers in many series (mcmiller2024immunemicroenvironmentof pages 1-2).
- **Anatomic/clinical context:** EBV positivity appears enriched in **gastric remnant cancers** (post-distal gastrectomy), with EBV positivity reported as 18.7% in remnant cancers vs 6.0% in proximal non-remnant controls in a Norwegian population-based study (Bringeland et al. 2024; DOI: 10.3390/cancers16112000; retrieved in this run but not yet evidence-extracted beyond summary in artifact) (artifact-00).

### Protective factors
A meta-analysis suggests EBV-positive status is associated with **better overall survival** compared to EBV-negative gastric cancer (HR < 1), which is prognostic rather than strictly protective against disease occurrence (pyo2023prognosticimplicationof pages 1-2).

### Gene–environment / microbe–environment interactions
Direct gene–environment interaction statistics were not extractable from the retrieved texts. However, EBV-associated tumors show characteristic **host epigenetic reprogramming (hypermethylation) and immune pathway activation**, consistent with pathogen-driven remodeling of host gene regulation (corallo2024unlockingthepotential pages 3-5, salnikov2024theviraletiology pages 1-2).


## 3. Phenotypes (clinical and pathological presentation)
### Clinicopathologic phenotype (human)
Commonly reported features include:
- **Male predominance** (e.g., 72.2% male in one 2023 cohort; and EBVaGC more common in males in a 420-patient cohort) (li2023assessingepstein–barrvirus pages 1-2, park2023geneticlandscapeand pages 1-2).
- **Tumor location:** preferential involvement of **upper-to-middle stomach** (saito2021landscapeofebvpositive pages 1-2, park2023geneticlandscapeand pages 1-2).
- **Histology:** frequent association with **gastric carcinoma with lymphoid stroma (GCLS)** characterized by dense intra/peritumoral lymphocytic infiltration (park2023geneticlandscapeand pages 1-2, lee2024associationofpdl1 pages 1-2).
- **Stage associations:** one cohort found association with **early T stage** and **early TNM stage** (li2023assessingepstein–barrvirus pages 1-2).

### Suggested HPO terms (examples; mapping-level suggestions)
Because EBVaGC is a cancer subtype, phenotypes overlap with gastric cancer generally; the literature extracted here emphasized histology and immune infiltration.
- Gastric adenocarcinoma: **HP:0006753** (Malignant neoplasm of stomach; verify exact HPO term naming in curation pipeline)
- Gastrointestinal bleeding (particularly in remnant cancers): **HP:0002239** (artifact-00; Bringeland 2024 study context)
- Weight loss/anorexia (common in GC but not quantified here): **HP:0001824** (Weight loss), **HP:0004396** (Anorexia)
- Lymphocyte-rich tumor stroma (not a standard HPO clinical term; better captured via pathology ontologies)

### Frequency data
- EBV positivity in GCLS: 85% (181/214) in one large 2024 cohort (lee2024associationofpdl1 pages 1-2).


## 4. Genetic / molecular information
### “Causal genes”
EBVaGC is not a Mendelian disorder and does not have a single causal germline gene. Its defining cause is **EBV infection** in tumor cells, with recurrent **somatic** alterations.

### Key recurrent somatic alterations (current understanding)
Across genomic profiling and reviews, EBVaGC is characterized by:
- **PIK3CA and ARID1A recurrent mutations**, and relatively fewer TP53 mutations (saito2021landscapeofebvpositive pages 1-2, guo2024developmentofa pages 1-2).
- **9p24.1 amplifications** including **JAK2, CD274 (PD-L1), and PDCD1LG2 (PD-L2)**, contributing to immune evasion (corallo2024unlockingthepotential pages 3-5, mcmiller2024immunemicroenvironmentof pages 1-2).
- **Extensive DNA hypermethylation** (including CDKN2A promoter hypermethylation noted in TCGA summaries; MLH1 promoter hypermethylation is not a typical feature in EBV subtype as summarized in one review) (corallo2024unlockingthepotential pages 3-5).

One 2024 review summarized reported frequencies from prior genomic studies: **PIK3CA 80%, ARID1A 55%, BCOR 23%, and JAK2/CD274/PDCD1LG2 amplifications 15%** (corallo2024unlockingthepotential pages 3-5).

### Epigenetic information
EBVaGC is notable for **DNA hypermethylation** compared to other gastric cancer subtypes (corallo2024unlockingthepotential pages 3-5).


## 5. Mechanism / pathophysiology
### Core mechanistic themes
EBVaGC’s pathophysiology is shaped by combined viral oncogenic programs, host epigenetic remodeling, and immune microenvironment remodeling.

**Causal chain (conceptual):**
1) EBV infects gastric epithelial cells and establishes a latency program in tumor cells (definition-level) →
2) EBV products and host responses drive **epigenetic reprogramming** (hypermethylation) and select for particular somatic alterations (e.g., PIK3CA/ARID1A) →
3) Tumors develop an “immune-hot” yet immunoregulatory environment, often with strong lymphocyte infiltration and immune checkpoint activation/amplification (PD-L1/PD-L2; JAK2) →
4) This immune contexture can be associated with **higher responsiveness to checkpoint blockade** in some cohorts, but responses are heterogeneous (corallo2024unlockingthepotential pages 6-8, bai2022efficacyandpredictive pages 1-2, mcmiller2024immunemicroenvironmentof pages 1-2).

### Immune microenvironment (2024 primary study)
A 2024 JITC study comparing EBV+ vs EBV− primary gastric cancers reported:
- EBVaGC background prevalence “~5–10% of GCs,” and EBV+ tumors often harbor PD-L1/PD-L2 amplifications with robust CD8+ infiltrates (mcmiller2024immunemicroenvironmentof pages 1-2).
- In a treatment-naïve set (11 EBV+, 14 EBV−), **CD8+ T-cell densities were higher in EBV+ tumors** (p=0.044) (mcmiller2024immunemicroenvironmentof pages 1-2).
- PD-L1+ tumor cells were observed in **3/25 tumors (all EBV+)** (mcmiller2024immunemicroenvironmentof pages 1-2).
- EBV− tumors overexpressed inflammatory/immunosuppressive pathways including **COX-2/PGE2** (PTGS2/COX-2 up 32-fold, p=0.005) (mcmiller2024immunemicroenvironmentof pages 1-2).

### Recent developments (2023–2024)
- **Single-cell immunology in EBV(+) GC under therapy:** A 2023 study used longitudinal scRNA-seq/scTCR/BCR-seq in EBV(+) GC treated with immunochemotherapy and reported a baseline intratumoral **ISG-15+ CD8+ T-cell** population associated with immunotherapy responsiveness, and suggested potential benefit of **anti-LAG-3** in refractory EBV(+) GC (bai2022efficacyandpredictive pages 1-2).
- **Operationalizing TCGA subtyping in practice:** A 2024 NGS-based TCGA-surrogate classification study reported EBV subtype prevalence 5.2% in a real-world cohort and found **100% disease control rate** for ICI therapy in EBV and MSI subtypes in a small validation cohort (guo2024developmentofa pages 1-2).

### Suggested GO terms (mechanism-level; mapping suggestions)
- **GO:0006955** immune response
- **GO:0002682** regulation of immune system process
- **GO:0006325** chromatin organization (epigenetic remodeling)
- **GO:0006306** DNA methylation
- **GO:0008283** cell population proliferation

### Suggested CL terms (cell types)
- **CD8+ T cell** (CL:0000625)
- **Macrophage** (CL:0000235); M2-like macrophage signatures noted for immunosuppressive environments (mcmiller2024immunemicroenvironmentof pages 1-2)
- **Gastric epithelial cell** (use appropriate CL term for gastric mucosal epithelial lineage in curation)


## 6. Epidemiology, population, and prognosis
### Prevalence / proportion among gastric cancers
Estimates vary by region and detection methods.
- Meta-analysis (2023): EBV infection in **10.4%** of gastric carcinomas (95% CI 8.2%–13.1%) (pyo2023prognosticimplicationof pages 1-2).
- TCGA-surrogate NGS cohort (2024): EBV subtype **5.2%** (guo2024developmentofa pages 1-2).
- Individual cohorts can range widely (e.g., 12.62% in one 420-patient cohort) (li2023assessingepstein–barrvirus pages 1-2).

### Prognosis (statistics)
A 2023 systematic review/meta-analysis (57 studies; 22,943 patients) found EBV positivity associated with improved overall survival: **HR 0.890 (95% CI 0.816–0.970)** (pyo2023prognosticimplicationof pages 1-2). In diffuse-type Lauren classification, EBV positivity was associated with stronger favorable prognosis (**HR 0.400, 95% CI 0.300–0.534**) (pyo2023prognosticimplicationof pages 1-2).


## 7. Diagnostics
### Core diagnostic definition
**EBER in situ hybridization (EBER-ISH)** is repeatedly described as the reference method for defining EBV-positive tumor status.
- In a clinical cohort paper: “**EBV-encoded RNA (EBER) in situ hybridization method was used to evaluate the EBV status in GC**” (li2023assessingepstein–barrvirus pages 1-2).
- A 2022 immunotherapy biomarker study states EBER-ISH is “**regarded as the gold standard**” but has limitations for multiplex biomarker assessment (bai2022efficacyandpredictive pages 1-2).

### Biomarkers used alongside EBV status
- **PD-L1 IHC (CPS):** EBV+ GCLS shows high PD-L1 positivity; CPS ≥1/≥5/≥10 were 81.8%, 70.2%, 55.3% in EBV+ GCLS (lee2024associationofpdl1 pages 1-2).
- **MSI/MMR status:** EBV+ GCLS rarely MSI-high (0.6%), while EBV− GCLS often MSI-high (54.5%) (lee2024associationofpdl1 pages 1-2).

### Omics-based diagnostics / recent development
An NGS-based EBV detection algorithm (validated against EBER-ISH) achieved **sensitivity 95.7%** and **specificity 100%**, and enabled simultaneous evaluation of clinically relevant biomarkers (TMB, MSI, HER2, fusions) (bai2022efficacyandpredictive pages 1-2).

### Differential diagnosis
Differential considerations include MSI-high gastric cancers (which can also have prominent immune infiltration and PD-L1 positivity) and other histologic subtypes; in lymphoid-stroma–rich tumors, MSI-H is a key alternate subtype (lee2024associationofpdl1 pages 1-2).


## 8. Treatment and real-world implementation
### Standard-of-care context
EBVaGC is treated within standard gastric cancer algorithms (surgery/endoscopic resection for early disease; chemotherapy ± targeted therapy; immunotherapy in selected advanced settings). EBV positivity is increasingly used as a **biomarker** relevant to immunotherapy selection/stratification (bai2022efficacyandpredictive pages 1-2, mcmiller2024immunemicroenvironmentof pages 1-2).

### Immunotherapy (checkpoint blockade) — response statistics
Evidence suggests EBVaGC can show high response rates to ICI in some cohorts, but responses vary.
- In an EBV+/pMMR cohort receiving immunotherapy, **ORR 54.5% (12/22)** was reported (bai2022efficacyandpredictive pages 1-2).
- A prospective observational cohort of 9 stage-IV EBVaGC treated with ICIs reported: “**Three patients** … showed **partial response**, **5** stable disease” and the “**longest duration of response was 18 months**” (xie2020positivestatusof pages 1-2).
- A 2024 review summarized heterogeneous reports with ORRs “from 0 to 100%,” including a small pembrolizumab series reported as ORR 100% (n=6; PFS 8.5 months) and a small camrelizumab series with ORR 0% (n=6; DCR 67%; PFS 2.2 months; OS 6.8 months) (corallo2024unlockingthepotential pages 6-8).

### Translational/precision treatment implications
- EBV subtype tumors frequently have **PD-L1/PD-L2 amplification and inflamed immune phenotype**, which supports immunotherapy candidacy (mcmiller2024immunemicroenvironmentof pages 1-2).
- Practical molecular subtyping by NGS may support immunotherapy selection: in one validation cohort, **ICI disease control rate was 100% in MSI and EBV** subtypes (guo2024developmentofa pages 1-2).

### Clinical trials (real-world implementations; ClinicalTrials.gov)
Trials explicitly incorporating EBV status in gastric cancer include:
- **NCT05970627** (Phase 2): perioperative chemotherapy + toripalimab for EBV-associated locally advanced gastric/EGJ adenocarcinoma (NOT_YET_RECRUITING) (trial retrieved in this run).
- **NCT03257163** (Phase 2): pembrolizumab + capecitabine + radiation in mismatch-repair deficient and EBV-positive gastric cancer (ACTIVE_NOT_RECRUITING) (trial retrieved in this run).
- **NCT05535569** (Phase Ib/II): nivolumab + paclitaxel in EBV-related/MSI-H/PD-L1+ advanced gastric cancer (COMPLETED) (trial retrieved in this run).

### Suggested MAXO terms (treatment action ontology; mapping suggestions)
- Immune checkpoint inhibitor therapy (e.g., anti-PD-1): **MAXO term for immune checkpoint inhibitor therapy** (exact ID to be selected during ontology curation)
- Gastric cancer surgical resection / gastrectomy
- Endoscopic submucosal dissection (for select early lesions)
- Radiotherapy / chemoradiation


## 9. Model organisms and experimental models
### Mechanistic and translational models
Direct model-system inventories (specific EBV+ gastric cancer organoids, cell lines, or mouse models) were not comprehensively extractable from the retrieved evidence set. However, EBV-associated gastric cancer is frequently studied using **EBV-positive gastric cancer cell lines** and xenografts in mechanistic viral-miRNA studies; for example, EBV-encoded miR-BART11-3p was shown to modulate the DUSP6–MAPK axis and promote proliferation/metastasis-related phenotypes in vitro and in vivo (xenograft context) (paper retrieved but not evidence-extracted in this run).


## 10. Summary table artifact
Key quantitative facts from recent literature are consolidated below.

| Feature | Quantitative value(s) | Study/Population | PMID (if available; otherwise DOI) | Publication date | URL |
|---|---:|---|---|---|---|
| EBVaGC prevalence, global estimate | 2%–20%; average 8.9% | Review summarizing global prevalence; EBVaGC across gastric cancers (park2023geneticlandscapeand pages 1-2) | DOI: 10.1038/s41598-023-45930-6 | 2023-11 | https://doi.org/10.1038/s41598-023-45930-6 |
| EBVaGC prevalence, single-center cohort | 53/420 = 12.62% | Li et al.; gastric cancer cohort evaluated by EBER ISH (li2023assessingepstein–barrvirus pages 1-2) | DOI: 10.1186/s13027-023-00489-9 | 2023-02 | https://doi.org/10.1186/s13027-023-00489-9 |
| EBV prevalence in gastric carcinomas, meta-analysis | 10.4% (95% CI 8.2%–13.1%) | 57 studies; 22,943 patients (pyo2023prognosticimplicationof pages 1-2) | DOI: 10.3390/medicina59050834 | 2023-04 | https://doi.org/10.3390/medicina59050834 |
| EBV subtype prevalence by NGS-TCGA surrogate | 5.2% | 3DMed cohort, n=765 gastric cancers (guo2024developmentofa pages 1-2) | DOI: 10.21037/jgo-24-345 | 2024-10 | https://doi.org/10.21037/jgo-24-345 |
| EBV prevalence in gastric remnant vs proximal non-remnant controls | 18.7% vs 6.0% | Population-based Central Norway study; gastric remnant cancer vs controls | DOI: 10.3390/cancers16112000 | 2024-05 | https://doi.org/10.3390/cancers16112000 |
| EBVaGC prevalence, broad current estimate | ~5%–10% of gastric cancers | McMiller et al.; background statement for immune microenvironment study (mcmiller2024immunemicroenvironmentof pages 1-2) | DOI: 10.1136/jitc-2024-010201 | 2024-11 | https://doi.org/10.1136/jitc-2024-010201 |
| NGS-based EBV detection performance vs EBER-ISH | Sensitivity 95.7% (22/23); specificity 100% (53/53) | Bai et al.; training/validation cohorts for NGS EBV detection (bai2022efficacyandpredictive pages 1-2) | DOI: 10.1136/jitc-2021-004080 | 2022-03 | https://doi.org/10.1136/jitc-2021-004080 |
| Immunotherapy response in EBV+/pMMR advanced GC | ORR 54.5% (12/22) | Bai et al.; EBV+/pMMR patients receiving immunotherapy (bai2022efficacyandpredictive pages 1-2) | DOI: 10.1136/jitc-2021-004080 | 2022-03 | https://doi.org/10.1136/jitc-2021-004080 |
| Prospective ICI outcomes in stage IV EBVaGC | 3 PR; 5 SD; 1 non-measurable lesion with decreased ascites/tumor markers; longest response 18 months | Xie et al.; 9 stage-IV EBVaGC patients treated with ICIs (xie2020positivestatusof pages 1-2) | DOI: 10.1097/CJI.0000000000000316 | 2020-03 | https://doi.org/10.1097/CJI.0000000000000316 |
| Pembrolizumab in small EBVaGC cohort (reported in review) | ORR 100% (n=6); PFS 8.5 months | Kim et al. 2018, as summarized in Corallo 2024 review (corallo2024unlockingthepotential pages 6-8) | DOI: 10.3390/pathogens13090728 | 2024-08 | https://doi.org/10.3390/pathogens13090728 |
| Camrelizumab in small EBVaGC cohort (reported in review) | ORR 0% (n=6); DCR 67%; PFS 2.2 months; OS 6.8 months | Phase 2 result summarized in Corallo 2024 review (corallo2024unlockingthepotential pages 6-8) | DOI: 10.3390/pathogens13090728 | 2024-08 | https://doi.org/10.3390/pathogens13090728 |
| ICI disease control by molecular subtype | DCR 100% in MSI and EBV cases; 62.9% in GS; 12.5% in CIN | Korean validation cohort, n=55 (guo2024developmentofa pages 1-2) | DOI: 10.21037/jgo-24-345 | 2024-10 | https://doi.org/10.21037/jgo-24-345 |
| PD-L1 in EBV+ GCLS | CPS ≥1: 81.8%; CPS ≥5: 70.2%; CPS ≥10: 55.3% | Lee & Oh; 181 EBV+ GCLS among 214 GCLS cases (lee2024associationofpdl1 pages 1-2) | DOI: 10.1038/s41598-024-81764-6 | 2024-12 | https://doi.org/10.1038/s41598-024-81764-6 |
| MSI-H in GCLS by EBV status | 0.6% in EBV+ GCLS vs 54.5% in EBV− GCLS | Lee & Oh; GCLS cohort (lee2024associationofpdl1 pages 1-2) | DOI: 10.1038/s41598-024-81764-6 | 2024-12 | https://doi.org/10.1038/s41598-024-81764-6 |
| HER2 amplification in GCLS by EBV status | ~3.9% in EBV+ GCLS vs ~3.0% in EBV− GCLS; 13% in EBV− GAC controls | Lee & Oh; GCLS vs GAC (lee2024associationofpdl1 pages 1-2) | DOI: 10.1038/s41598-024-81764-6 | 2024-12 | https://doi.org/10.1038/s41598-024-81764-6 |
| CD8+ T-cell infiltration in EBV+ vs EBV− GC | Higher CD8+ density in EBV+ tumors; p=0.044 | McMiller et al.; 25 treatment-naïve specimens (11 EBV+, 14 EBV−) (mcmiller2024immunemicroenvironmentof pages 1-2) | DOI: 10.1136/jitc-2024-010201 | 2024-11 | https://doi.org/10.1136/jitc-2024-010201 |
| PD-L1+ tumor cells in immune microenvironment study | 3/25 tumors; all 3 were EBV+ | McMiller et al.; 25 treatment-naïve gastric cancers (mcmiller2024immunemicroenvironmentof pages 1-2) | DOI: 10.1136/jitc-2024-010201 | 2024-11 | https://doi.org/10.1136/jitc-2024-010201 |
| COX-2/PGE2 pathway enrichment in EBV− tumors | PTGS2/COX-2 up 32-fold (p=0.005); PTGER1 up 21-fold (p=0.015) | McMiller et al.; EBV− vs EBV+ immune microenvironment comparison (mcmiller2024immunemicroenvironmentof pages 1-2) | DOI: 10.1136/jitc-2024-010201 | 2024-11 | https://doi.org/10.1136/jitc-2024-010201 |
| Prognostic effect of EBV positivity | OS HR 0.890 (95% CI 0.816–0.970) | Pyo et al. meta-analysis; 57 studies, 22,943 patients (pyo2023prognosticimplicationof pages 1-2) | DOI: 10.3390/medicina59050834 | 2023-04 | https://doi.org/10.3390/medicina59050834 |
| Prognostic effect in diffuse-type Lauren classification | HR 0.400 (95% CI 0.300–0.534) | Pyo et al. subgroup analysis (pyo2023prognosticimplicationof pages 1-2) | DOI: 10.3390/medicina59050834 | 2023-04 | https://doi.org/10.3390/medicina59050834 |
| Recurrent molecular features of EBV subtype | Recurrent ARID1A and PIK3CA mutations; fewer TP53 mutations | Guo et al. NGS-based subtype classification (guo2024developmentofa pages 1-2) | DOI: 10.21037/jgo-24-345 | 2024-10 | https://doi.org/10.21037/jgo-24-345 |
| Frequent EBVaGC molecular alterations summarized in review | PIK3CA 80%; ARID1A 55%; BCOR 23%; JAK2/CD274/PDCD1LG2 amplifications 15% | Corallo 2024 review summarizing prior genomic studies (corallo2024unlockingthepotential pages 3-5) | DOI: 10.3390/pathogens13090728 | 2024-08 | https://doi.org/10.3390/pathogens13090728 |


*Table: This table consolidates key quantitative findings for EBV-associated gastric cancer across prevalence, molecular features, biomarkers, immune microenvironment, prognosis, and immunotherapy response. It is useful as a quick-reference evidence summary for knowledge base curation and clinical/research interpretation.*


## 11. Expert opinion / authoritative synthesis (2024 reviews)
A 2024 Frontiers in Immunology review emphasizes that EBVaGC is “immunologically, molecularly and pathologically distinct” and describes an overall “immune-hot” phenotype with improved prognosis relative to EBV-negative gastric cancers (salnikov2024theviraletiology pages 1-2). A 2024 Pathogens review highlights EBV status as a potential predictive biomarker for response to chemotherapy and immune checkpoint inhibitors, while emphasizing heterogeneity and the need for prospective validation (corallo2024unlockingthepotential pages 6-8).


## Data gaps and limitations (important for knowledge base curation)
- **Ontology identifiers (MONDO/MeSH/ICD)** were not obtainable from the retrieved full-text evidence in this run; dedicated ontology/database queries are needed.
- Several key statements in recent reviews summarize TCGA-era findings; where possible, this report relied on cohort studies/meta-analyses for quantitative estimates (pyo2023prognosticimplicationof pages 1-2, guo2024developmentofa pages 1-2, mcmiller2024immunemicroenvironmentof pages 1-2).
- Immunotherapy response estimates remain largely based on small cohorts and heterogeneous designs; even recent syntheses report ORRs ranging from 0–100% across small series (corallo2024unlockingthepotential pages 6-8, bai2022efficacyandpredictive pages 1-2).


References

1. (saito2021landscapeofebvpositive pages 1-2): Motonobu Saito and Koji Kono. Landscape of ebv-positive gastric cancer. Gastric Cancer, 24:983-989, Jul 2021. URL: https://doi.org/10.1007/s10120-021-01215-3, doi:10.1007/s10120-021-01215-3. This article has 92 citations and is from a domain leading peer-reviewed journal.

2. (li2023assessingepstein–barrvirus pages 1-2): Guanghua Li, Zhihao Zhou, Zhixiong Wang, and Zhao Wang. Assessing epstein–barr virus in gastric cancer: clinicopathological features and prognostic implications. Infectious Agents and Cancer, Feb 2023. URL: https://doi.org/10.1186/s13027-023-00489-9, doi:10.1186/s13027-023-00489-9. This article has 12 citations and is from a peer-reviewed journal.

3. (lee2024associationofpdl1 pages 1-2): Sun Mi Lee and Hyunjoo Oh. Association of pd-l1 positivity with epstein barr virus infection and microsatellite instability in gastric carcinomas with lymphoid stroma. Scientific Reports, Dec 2024. URL: https://doi.org/10.1038/s41598-024-81764-6, doi:10.1038/s41598-024-81764-6. This article has 5 citations and is from a peer-reviewed journal.

4. (bai2022efficacyandpredictive pages 1-2): Yuezong Bai, Tong Xie, Zhenghang Wang, Shuang Tong, Xiaochen Zhao, Feilong Zhao, Jinping Cai, Xiaofan Wei, Zhi Peng, and Lin Shen. Efficacy and predictive biomarkers of immunotherapy in epstein-barr virus-associated gastric cancer. Journal for Immunotherapy of Cancer, 10:e004080, Mar 2022. URL: https://doi.org/10.1136/jitc-2021-004080, doi:10.1136/jitc-2021-004080. This article has 114 citations and is from a domain leading peer-reviewed journal.

5. (park2023geneticlandscapeand pages 1-2): Ji Hyun Park, Hee Jin Cho, Jeonghwa Seo, Ki Bum Park, Yong Hwan Kwon, Han Ik Bae, An Na Seo, and Moonsik Kim. Genetic landscape and pd-l1 expression in epstein–barr virus-associated gastric cancer according to the histological pattern. Scientific Reports, Nov 2023. URL: https://doi.org/10.1038/s41598-023-45930-6, doi:10.1038/s41598-023-45930-6. This article has 6 citations and is from a peer-reviewed journal.

6. (corallo2024unlockingthepotential pages 6-8): Salvatore Corallo, Angioletta Lasagna, Beatrice Filippi, Domiziana Alaimo, Anna Tortorella, Francesco Serra, Alessandro Vanoli, and Paolo Pedrazzoli. Unlocking the potential: epstein-barr virus (ebv) in gastric cancer and future treatment prospects, a literature review. Pathogens, 13:728, Aug 2024. URL: https://doi.org/10.3390/pathogens13090728, doi:10.3390/pathogens13090728. This article has 18 citations.

7. (xie2020positivestatusof pages 1-2): Tong Xie, Yiqiang Liu, Zhening Zhang, Xiaotian Zhang, Jifang Gong, Changsong Qi, Jian Li, Lin Shen, and Zhi Peng. Positive status of epstein-barr virus as a biomarker for gastric cancer immunotherapy: a prospective observational study. Journal of Immunotherapy (Hagerstown, Md. : 1997), 43:139-144, Mar 2020. URL: https://doi.org/10.1097/cji.0000000000000316, doi:10.1097/cji.0000000000000316. This article has 107 citations.

8. (pyo2023prognosticimplicationof pages 1-2): Jung-Soo Pyo, Nae-Yu Kim, and Dong-Wook Kang. Prognostic implication of ebv infection in gastric carcinomas: a systematic review and meta-analysis. Medicina, 59:834, Apr 2023. URL: https://doi.org/10.3390/medicina59050834, doi:10.3390/medicina59050834. This article has 4 citations.

9. (salnikov2024theviraletiology pages 1-2): Mikhail Yuryevich Salnikov, Katelyn M. MacNeil, and J. Mymryk. The viral etiology of ebv-associated gastric cancers contributes to their unique pathology, clinical outcomes, treatment responses and immune landscape. Frontiers in Immunology, Mar 2024. URL: https://doi.org/10.3389/fimmu.2024.1358511, doi:10.3389/fimmu.2024.1358511. This article has 31 citations and is from a peer-reviewed journal.

10. (mcmiller2024immunemicroenvironmentof pages 1-2): Tracee L McMiller, Sepideh Besharati, Mark Yarchoan, Qingfeng Zhu, Keziban Ünsal-Kaçmaz, Ke Xu, Junghwa Lee, Feriyl Bhaijee, Logan L Engle, Janis M Taube, Alan E Berger, Robert A Anders, and Suzanne L Topalian. Immune microenvironment of epstein-barr virus (ebv)-negative compared to ebv-associated gastric cancers: implications for immunotherapy. Journal for Immunotherapy of Cancer, 12:e010201, Nov 2024. URL: https://doi.org/10.1136/jitc-2024-010201, doi:10.1136/jitc-2024-010201. This article has 7 citations and is from a domain leading peer-reviewed journal.

11. (corallo2024unlockingthepotential pages 3-5): Salvatore Corallo, Angioletta Lasagna, Beatrice Filippi, Domiziana Alaimo, Anna Tortorella, Francesco Serra, Alessandro Vanoli, and Paolo Pedrazzoli. Unlocking the potential: epstein-barr virus (ebv) in gastric cancer and future treatment prospects, a literature review. Pathogens, 13:728, Aug 2024. URL: https://doi.org/10.3390/pathogens13090728, doi:10.3390/pathogens13090728. This article has 18 citations.

12. (guo2024developmentofa pages 1-2): Pengda Guo, Yang Yang, Lu Wang, Yu Zhang, Bei Zhang, Jinping Cai, Fabrício Freire de Melo, Matthew R. Strickland, Min Huang, and Biao Liu. Development of a streamlined ngs-based tcga classification scheme for gastric cancer and its implications for personalized therapy. Journal of Gastrointestinal Oncology, 15:2053-2066, Oct 2024. URL: https://doi.org/10.21037/jgo-24-345, doi:10.21037/jgo-24-345. This article has 4 citations and is from a peer-reviewed journal.
