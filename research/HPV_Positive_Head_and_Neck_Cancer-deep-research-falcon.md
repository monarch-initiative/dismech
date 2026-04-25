---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-05T16:34:11.031933'
end_time: '2026-04-05T16:41:40.966188'
duration_seconds: 449.93
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: HPV-Positive Head and Neck Cancer
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 33
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** HPV-Positive Head and Neck Cancer
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **HPV-Positive Head and Neck Cancer** covering all of the
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
- **Disease Name:** HPV-Positive Head and Neck Cancer
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **HPV-Positive Head and Neck Cancer** covering all of the
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


# HPV-Positive Head and Neck Cancer (HPV+ HNSCC) — Disease Characteristics Research Report

## Target Disease
- **Disease Name:** HPV-Positive Head and Neck Cancer (HPV+ HNSCC), with emphasis on **HPV-positive oropharyngeal squamous cell carcinoma (HPV+ OPSCC)**, the dominant clinical entity in most datasets.
- **MONDO ID:** Not retrieved in the available evidence corpus.
- **Category:** Virus-associated squamous cell carcinoma (upper aerodigestive tract), primarily oropharynx.

---

## 1. Disease Information

### Overview (current understanding)
HPV-positive head and neck squamous cell carcinoma is a subset of HNSCC in which oncogenic high-risk HPV infection is an etiologic driver; clinically this is most strongly associated with **oropharyngeal** squamous cell carcinoma (tonsil and base of tongue). Single-cell and translational studies treat HPV+ OPSCC as a **distinct disease entity** with unique immune and molecular features and generally more favorable outcomes compared with HPV-negative OPSCC. (yan2024decipheringtheinterplay pages 1-2, ndon2023humanpapillomavirusassociatedoropharyngeal pages 1-3)

**Abstract-quotable definition/epidemiology framing:**
- Yan et al. (2024) open with: “Human papillomavirus (HPV) infection has become an important etiological driver of oropharyngeal squamous cell carcinoma (OPSCC), leading to unique tumor characteristics.” (Published online 6 Aug 2024; https://doi.org/10.1007/s00262-024-03789-0) (yan2024decipheringtheinterplay pages 1-2)

### Synonyms / alternative names
- HPV-associated head and neck squamous cell carcinoma
- HPV-mediated oropharyngeal squamous cell carcinoma
- HPV-positive oropharyngeal cancer / HPV-associated OPSCC

### Key identifiers (ontologies)
The provided evidence did not include explicit ontology identifiers (ICD-10/ICD-11, MeSH, MONDO). Consequently, this section is **incomplete** for identifiers. The staging context emphasizes **AJCC/UICC TNM 8th edition** separation/stratification of HPV-associated OPSCC (via p16 surrogate testing), but the manual itself was not retrieved in full as a citable source in this run. (Craig et al. discuss TNM8 implications) (craig2019recommendationsfordetermining pages 1-2)

### Evidence provenance
Evidence here is derived primarily from:
- Aggregated resources (registry/SEER/NCDB-like cohorts and reviews) (kim2024aseerbasedanalysis pages 1-2, ndon2023humanpapillomavirusassociatedoropharyngeal pages 1-3)
- Single-center retrospective cohorts (cleere2024hpvovertakessmoking pages 1-2)
- Clinical trial registry entries (ClinicalTrials.gov) (NCT01898494 chunk 1, NCT02215265 chunk 1)
- Molecular/translational datasets (single-cell RNA-seq) (yan2024decipheringtheinterplay pages 1-2)

---

## 2. Etiology

### Disease causal factors
**Primary cause:** persistent infection with oncogenic high-risk HPV (especially HPV16) leading to malignant transformation of oropharyngeal mucosa. (ndon2023humanpapillomavirusassociatedoropharyngeal pages 1-3, wu2024deescalationstrategiesin pages 1-2)

Mechanistic causal factors (viral-host interactions):
- Viral oncogenes **E6** and **E7** promote malignant transformation through canonical tumor suppressor interference (p53 and RB axis). Wu et al. explicitly summarize: “E6 was found to specifically degrade p53” and “E7 binds to the unphosphorylated region of retinoblastoma (Rb).” (wu2024deescalationstrategiesin pages 1-2)

### Risk factors
- **HPV exposure** (sexually transmitted; oropharyngeal exposure linked to sexual behavior). OPSCC tumors driven by HPV contrast with conventional carcinogen-driven OPSCC (alcohol/tobacco). (yan2024decipheringtheinterplay pages 1-2, krsek2024thenextchapter pages 1-2)
- **Tobacco/alcohol** remain important external risk factors for HNSCC broadly, and for HPV-negative OPSCC in particular; HPV-negative OPSCC is “caused primarily by conventional carcinogens like alcohol or tobacco exposure.” (yan2024decipheringtheinterplay pages 1-2)

### Protective factors
- **Prophylactic HPV vaccination** is the primary prevention strategy; Ndon et al. state: “HPV vaccination is currently the main preventative approach for HPV-associated oropharyngeal cancer.” (Published 13 Aug 2023; https://doi.org/10.3390/cancers15164080) (ndon2023humanpapillomavirusassociatedoropharyngeal pages 1-3)

### Gene–environment / virus–environment interaction (evidence-supported components)
- HPV-negative vs HPV-positive disease reflects different etiologic exposures (tobacco/alcohol vs HPV). (yan2024decipheringtheinterplay pages 1-2)
- HPV integration biology (see Mechanisms) suggests a viral–host genome interaction that influences immune infiltration and outcomes. (tabatabaeian2024navigatingtherapeuticstrategies pages 1-2)

---

## 3. Phenotypes

### Clinical presentation (limited by available evidence)
The retrieved texts emphasized epidemiology, diagnostics, immune biology, and treatment strategy rather than symptom frequencies. Nonetheless, several clinically relevant patterns were present:

- **Nodal disease prominence (clinical behavior):** HPV+ OPSCC often presents with clinically significant cervical nodal disease despite favorable prognosis (not quantified in the evidence corpus here).
- **Treatment-related morbidity affecting quality of life:** major toxicities motivating de-intensification include swallowing dysfunction and other head-and-neck functional sequelae. E3311 includes swallowing/QOL endpoints, and PATHOS explicitly centers swallowing function (MDADI). (NCT01898494 chunk 1, NCT02215265 chunk 1)

### Quality of life impact (evidence-supported)
- PATHOS’ stated main objective: “To assess whether swallowing function can be improved … by reducing the intensity of adjuvant treatment protocols.” (NCT02215265 chunk 1)

### Suggested HPO terms (expert-curated; not directly asserted with frequencies in the retrieved evidence)
- Dysphagia — **HP:0002015**
- Odynophagia — **HP:0033050**
- Cervical lymphadenopathy — **HP:0000453**
- Weight loss — **HP:0001824**
- Xerostomia (treatment-related, esp. radiotherapy) — **HP:0000217**
- Dysarthria — **HP:0001260**

*Note:* Frequencies and onset distributions were not extractable from the current evidence set.

---

## 4. Genetic/Molecular Information

### Viral molecular drivers
- High-risk HPV, particularly **HPV16**, is the dominant subtype in OPSCC; Ndon et al. state: “an estimated 30% of oropharyngeal squamous cell carcinomas … are driven by HPV, with HPV16 being the most common subtype associated with malignancy.” (ndon2023humanpapillomavirusassociatedoropharyngeal pages 1-3)
- E6/E7 oncogene activity is central to oncogenic mechanism (p53/RB axis). (wu2024deescalationstrategiesin pages 1-2)

### Viral integration status (clinically important subtype concept)
Tabatabaeian et al. describe three HPV genome states in tumors: “integrated … episomal … or a mixture,” and highlight outcome differences: “patients with HPV-positive head and neck cancers generally have a good prognosis except for a group of patients with fully integrated HPV who show worst clinical outcomes. Those patients present with lowered expression of viral genes and limited infiltration of cytotoxic T cells.” (Published online 20 Apr 2024; https://doi.org/10.1038/s41416-024-02655-1) (tabatabaeian2024navigatingtherapeuticstrategies pages 1-2)

### Host genomic alterations
The current evidence set does not provide primary data on specific recurrent somatic driver frequencies (e.g., PIK3CA, TRAF3, CYLD) in HPV+ OPSCC. (Reference lists hint at these topics but without extractable numeric evidence.) (atique2024comprehensiveanalysisof pages 55-58, cleere2024hpvovertakessmoking pages 9-9)

### Epigenetics
Not directly extractable from retrieved primary evidence; discussed as a general biomarker domain in diagnostic reviews. (krsek2024thenextchapter pages 1-2)

---

## 5. Mechanism / Pathophysiology

### Causal chain (evidence-based backbone)
1. **Exposure and infection** of oropharyngeal mucosa with high-risk HPV (often HPV16). (ndon2023humanpapillomavirusassociatedoropharyngeal pages 1-3)
2. **Viral oncogene expression (E6/E7)** disrupts tumor suppressor pathways: p53 degradation and RB-axis interference. (wu2024deescalationstrategiesin pages 1-2)
3. **Tumor evolution with distinct immune microenvironment**, often immune-infiltrated (“immune hot” concept is widely discussed in this field; in the evidence here, the immune-rich TME is directly analyzed by single-cell methods). (yan2024decipheringtheinterplay pages 1-2)
4. **Clinical phenotype**: HPV+ OPSCC tends to have more favorable prognosis overall, but with heterogeneity (e.g., integration status, discordant biomarker subsets). (craig2019recommendationsfordetermining pages 1-2, tabatabaeian2024navigatingtherapeuticstrategies pages 1-2)

### Immune microenvironment (2024 single-cell evidence)
Yan et al. performed scRNA-seq on HPV+ and HPV− OPSCC (3 tumors each + normal tonsil), finding:
- “HPV+ OPSCC tumor cells manifest an enhanced interferon response and elevated expression of the major histocompatibility complex II (MHC-II)” (yan2024decipheringtheinterplay pages 1-2)
- They identify “a CXCL13+CD4+ T cell subset …” and report that interaction with HPV+ tumor cells “amplifies CXCL13 and IFNγ release … fostering a pro-inflammatory TME.” (yan2024decipheringtheinterplay pages 1-2)
- They also note real-world clinical limitation: “the actual response rates of [immune checkpoint blockade] … remained relatively low (approximately 20%).” (yan2024decipheringtheinterplay pages 1-2)

### Pathways / processes (ontology suggestions)
**GO Biological Process (examples):**
- Interferon-gamma-mediated signaling pathway — GO:0060333 (supported conceptually by IFNγ/interferon response findings) (yan2024decipheringtheinterplay pages 1-2)
- Antigen processing and presentation of peptide antigen via MHC class II — GO:0002495 (MHC-II elevation) (yan2024decipheringtheinterplay pages 1-2)
- Regulation of T cell activation — GO:0050863 (CXCL13+ CD4+ interactions) (yan2024decipheringtheinterplay pages 1-2)

**Cell Ontology (CL) suggestions:**
- CD4-positive, alpha-beta T cell — CL:0000624 (yan2024decipheringtheinterplay pages 1-2)
- Cytotoxic T cell (CD8+ T cell) — CL:0000625 (integration-associated reduced cytotoxic T infiltration concept) (tabatabaeian2024navigatingtherapeuticstrategies pages 1-2)

**GO Cellular Component suggestions:**
- MHC protein complex — GO:0042611 (yan2024decipheringtheinterplay pages 1-2)

---

## 6. Diagnostics

### Current standard concepts (tissue-based)
- p16 immunohistochemistry is widely used as a practical surrogate marker, but discordance exists (p16+ may not always indicate transcriptionally active HPV). Craig et al. emphasize TNM8’s use of p16 as surrogate and demonstrate prognostic misclassification when HPV is not transcriptionally active. (craig2019recommendationsfordetermining pages 1-2)

### Quantitative performance evidence (2023)
Yang et al. compared **Aptima HR-HPV E6/E7 mRNA testing** on cytology specimens with **p16 IHC** on biopsies in 60 HNSCC patients (39 OPSCC):
- “overall concordance rate … 95.0%” (yang2023aptimahrhpvtesting pages 1-2)
- “sensitivity and negative predictive values … consistent at 100%” (Aptima and p16 IHC) (yang2023aptimahrhpvtesting pages 1-2)
- “specificity and positive predictive values were 96.9% and 96.6% versus 93.8% and 93.3%, respectively.” (Aptima vs p16 IHC) (Published online 13 Dec 2022 in Acta Cytologica 2023; https://doi.org/10.1159/000527951) (yang2023aptimahrhpvtesting pages 1-2)

### Clinical importance of p16/HPV discordance (2019, staging-relevant)
Craig et al. show that a p16+ but HPV− (transcriptionally inactive HPV) subgroup has significantly worse survival:
- “Patients who tested p16+ but were HPV− (n = 20) had significantly reduced five-year survival (33%) compared to p16+ patients (77%) but not p16− patients (35%).” (craig2019recommendationsfordetermining pages 1-2)
- They conclude these findings are relevant for de-escalation because p16-only staging can downstage biologically higher-risk patients. (craig2019recommendationsfordetermining pages 1-2)

### Suggested diagnostic tests / biomarkers (evidence-based categories)
- p16 IHC (screening surrogate) (yang2023aptimahrhpvtesting pages 1-2)
- HPV E6/E7 mRNA assays (e.g., Aptima; RNA-based evidence of transcriptional activity) (yang2023aptimahrhpvtesting pages 1-2)
- HPV DNA and genotyping (PCR-based in Yan et al. patient classification; HPV DNA detection used to confirm HPV status) (yan2024decipheringtheinterplay pages 1-2)

---

## 7. Treatment

### Standard modalities (current practice)
Standard treatment remains multimodal (surgery and/or radiotherapy ± chemotherapy), and HPV+ disease’s better prognosis has motivated attempts to reduce treatment morbidity while maintaining control. (krsek2024thenextchapter pages 1-2, wu2024deescalationstrategiesin pages 1-2)

### De-intensification / risk-adapted treatment (real-world implementation: ongoing trials)
**ECOG-ACRIN E3311 (NCT01898494; Phase II; p16+ locally advanced, resectable OPC)**
- Official title: “Phase II Randomized Trial of Transoral Surgical Resection Followed by Low-Dose or Standard-Dose IMRT in Resectable p16+ Locally Advanced Oropharynx Cancer” (NCT01898494 chunk 1)
- Key design: all patients undergo transoral surgery, then risk stratification:
  - Intermediate-risk randomized: **50 Gy/25 fx** vs **60 Gy/30 fx** IMRT (NCT01898494 chunk 1)
  - High-risk: **66 Gy/33 fx** IMRT + weekly cisplatin (days 1, 8, 15, 22, 29, 36, 43) (NCT01898494 chunk 1)
- Enrollment: 519; status ACTIVE_NOT_RECRUITING; results posted 28 Sep 2022 (registry metadata). (NCT01898494 chunk 1)

**PATHOS (NCT02215265; Phase III; post-operative risk-stratified adjuvant therapy after transoral surgery)**
- Official title: “A Phase III Trial of Risk-stratified, Reduced Intensity Adjuvant Treatment … HPV-Positive Oropharyngeal Cancer” (NCT02215265 chunk 1)
- Objective includes swallowing/QoL and non-inferiority for survival: “To demonstrate the non-inferiority of reducing the intensity of adjuvant treatment protocols in terms of overall survival …” (NCT02215265 chunk 1)
- Radiation de-escalation arms:
  - Group B: PORT **60 Gy/30 fx** vs **50 Gy/25 fx** (NCT02215265 chunk 1)
  - Group C: POCRT **60 Gy/30 fx + cisplatin** vs PORT **60 Gy/30 fx without chemotherapy** (NCT02215265 chunk 1)
- Target enrollment increased to **1269** (protocol amendment March 2024). (NCT02215265 chunk 1)

### Immunotherapy considerations
Despite immune infiltration in HPV+ OPSCC, checkpoint blockade responses are heterogeneous and “approximately 20%” in the Yan et al. framing, motivating deeper TME stratification and biomarker development. (yan2024decipheringtheinterplay pages 1-2)

### Suggested MAXO terms (ontology suggestions)
- Radiotherapy — **MAXO:0000027**
- Chemotherapy — **MAXO:0000077**
- Surgical resection — **MAXO:0000445**
- Immunotherapy — **MAXO:0000127**
- Swallowing rehabilitation — **MAXO:0000746**

---

## 8. Outcome / Prognosis

### Survival differences (HPV+ vs HPV−)
- In an Irish single-center cohort (2012–2021), HPV+ OPSCC had higher short-term survival:
  - “2-year OS (83.9% vs. 54.9%; p < 0.001)” and “2-year DFS (73.5% vs. 45.6%; p < 0.001)” for HPV+ vs HPV−. (Cleere et al., 2024; https://doi.org/10.1007/s11845-024-03715-4) (cleere2024hpvovertakessmoking pages 1-2)

### Prognostic pitfalls of surrogate testing (p16 discordance)
Craig et al. demonstrate clinically important survival divergence:
- “p16+/HPV− … five-year survival (33%) compared to p16+ patients (77%)” and similar to p16− (35%). (craig2019recommendationsfordetermining pages 1-2)
- Mortality risk under TNM8 downstaging: “mortality rate twice (HR 2.66 [95% CI: 1.37–5.15]) that of p16+/HPV+ patients …” (craig2019recommendationsfordetermining pages 1-2)

### Molecularly informed prognosis (integration status)
Tabatabaeian et al. emphasize that fully integrated HPV correlates with “worst clinical outcomes” and limited cytotoxic T-cell infiltration, suggesting integration status is a candidate prognostic and predictive biomarker beyond HPV positivity alone. (tabatabaeian2024navigatingtherapeuticstrategies pages 1-2)

---

## 9. Inheritance and Population

### Epidemiology and incidence trends (recent quantitative data)

**United States (SEER 2010–2017 OPSCC; 2024 analysis)**
- HPV testing uptake increased from **21.95% (2010)** to **51.37% (2014)**.
- HPV positivity among tested OPSCC increased from **66.37% (2010)** to **79.32% (2016)**.
- Higher HPV positivity in **tonsil** and **base of tongue** vs posterior pharyngeal wall / soft palate. (Kim et al., 2024; https://doi.org/10.1186/s13027-024-00592-5) (kim2024aseerbasedanalysis pages 1-2)

**Ireland (Dublin tertiary center, 2012–2021)**
- HPV+ proportion: **59.5% (175/294)**.
- HPV-linked OPSCC proportion rose from **50.4% (2012–2016)** to **65.4% (2017–2021)** (p=0.011). (cleere2024hpvovertakessmoking pages 1-2)

**Global estimates and regional variation (review synthesis, 2023)**
- Ndon et al.: “Across the globe, an estimated 30% of oropharyngeal squamous cell carcinomas … are driven by HPV …” (ndon2023humanpapillomavirusassociatedoropharyngeal pages 1-3)
- North America ASIR and attributable fraction (as summarized in the paper’s extracted text): “ASIR … 3.41 per 100,000 in males and 0.71 in females … ~63% [attributable fraction].” (ndon2023humanpapillomavirusassociatedoropharyngeal pages 1-3)

### Population demographics and disparities (limited by evidence)
Age/sex and policy disparities were discussed at a high level; detailed race/ethnicity-specific incidence or prevalence was not retrieved as primary evidence in this run.

---

## 10. Prevention

### Primary prevention: HPV vaccination
Ndon et al. emphasize vaccination as primary prevention and highlight policy gaps:
- “HPV vaccinations are the primary mode of prevention for HPV-associated OPSCC …” (ndon2023humanpapillomavirusassociatedoropharyngeal pages 10-12)
- “As of 2022, 122 of 195 (63%) WHO member states had incorporated HPV vaccinations nationally; of these, 41 of 122 (34%) member states have introduced gender-neutral vaccine coverage.” (ndon2023humanpapillomavirusassociatedoropharyngeal pages 1-3)

They also cite oral infection impact: “Studies have shown that HPV vaccinations have an efficacy of 88–93% against oral HPV infection …” (ndon2023humanpapillomavirusassociatedoropharyngeal pages 1-3)

### Real-world implementation gaps (2024 US example)
Adekanmbi et al. (Texas, 2006–2022 vaccination; 2016–2020 cancer IR) show wide geographic variation:
- County-level 2021–2022 initiation ranges: **6.3%–69.1% (females)** and **7.0%–77.6% (males)** ages 9–17.
- Up-to-date ranges: **1.6%–30.4% (females)** and **2.1%–34.8% (males)**.
- Counties with lower vaccination had higher HPV-related cancer incidence, raising equity concerns. (Published 5 Sep 2024; https://doi.org/10.1001/jamanetworkopen.2024.31807) (adekanmbi2024humanpapillomavirusvaccination pages 1-2)

---

## 11. Other Species / Natural Disease
Not addressed in the retrieved evidence corpus.

---

## 12. Model Organisms / Experimental Systems
The retrieved evidence set did not include explicit descriptions of animal models or organoid systems for HPV+ OPSCC. This section is therefore **not evidence-complete** in the current run.

---

## Evidence Synthesis Artifact
The following evidence table consolidates the most directly supported quantitative statements and implementation-relevant facts extracted in this run.

| Domain | Key findings | Key source | Identifier |
|---|---|---|---|
| Epidemiology | In the US SEER 2010-2017 cohort of 13,081 OPSCC cases, HPV testing increased from 21.95% (2010) to 51.37% (2014), and HPV positivity among tested OPSCC cases increased from 66.37% (2010) to 79.32% (2016); positivity was higher in tonsil/base of tongue than soft palate/posterior pharyngeal wall (kim2024aseerbasedanalysis pages 1-2) | Kim et al., 2024, *Infectious Agents and Cancer* | DOI: 10.1186/s13027-024-00592-5 |
| Epidemiology | In a Dublin tertiary-center series (2012-2021, n=294), 59.5% (175/294) of OPSCC cases were HPV-positive; the proportion of HPV-linked OPSCC rose from 50.4% in 2012-2016 to 65.4% in 2017-2021 (p=0.011) (cleere2024hpvovertakessmoking pages 1-2) | Cleere et al., 2024, *Irish Journal of Medical Science* | DOI: 10.1007/s11845-024-03715-4 |
| Epidemiology | Globally, ~30% of OPSCC is HPV-driven; incidence is highest in North America, Europe, and Oceania. North America ASIR was 3.41/100,000 in males and 0.71/100,000 in females, with an attributable fraction of ~63% (ndon2023humanpapillomavirusassociatedoropharyngeal pages 1-3) | Ndon et al., 2023, *Cancers* | DOI: 10.3390/cancers15164080 |
| Etiology/Mechanism | HPV16 is the dominant high-risk subtype; HPV genomes in tumors can be integrated, episomal, or mixed. Fully integrated HPV is associated with worse outcomes, lower viral gene expression, and reduced cytotoxic T-cell infiltration (tabatabaeian2024navigatingtherapeuticstrategies pages 1-2) | Tabatabaeian et al., 2024, *British Journal of Cancer* | DOI: 10.1038/s41416-024-02655-1 |
| Etiology/Mechanism | Single-cell RNA-seq of 3 HPV+ and 3 HPV- OPSCC tumors plus normal tonsil showed HPV+ tumor cells have enhanced interferon response, elevated MHC-II expression, and crosstalk with CXCL13+CD4+ T cells; ICB response rates in HPV+ OPSCC remain only ~20% despite immune-rich TME (yan2024decipheringtheinterplay pages 1-2) | Yan et al., 2024, *Cancer Immunology, Immunotherapy* | DOI: 10.1007/s00262-024-03789-0 |
| Diagnostics | In 60 HNSCC cases (39 OPSCC), Aptima E6/E7 mRNA testing and p16 IHC were 95.0% concordant. Sensitivity and NPV were 100% for both; specificity/PPV were 96.9%/96.6% for Aptima versus 93.8%/93.3% for p16 IHC. HPV prevalence was 61.5% (24/39) in OPSCC (yang2023aptimahrhpvtesting pages 1-2) | Yang et al., 2023, *Acta Cytologica* | DOI: 10.1159/000527951 |
| Diagnostics | A UK OPSCC cohort showed up to ~20% of p16+ OPSCC may lack transcriptionally active HPV; p16+/HPV- patients had markedly inferior outcomes, supporting two-tier testing with HPV-specific assays (RNA/DNA ISH) rather than p16 alone for staging/de-escalation decisions (craig2019recommendationsfordetermining pages 1-2) | Craig et al., 2019, *British Journal of Cancer* | DOI: 10.1038/s41416-019-0414-9 |
| Prognosis | In the Dublin series, HPV+ OPSCC had better 2-year overall survival (83.9% vs 54.9%) and disease-free survival (73.5% vs 45.6%) than HPV- disease (both p<0.001) (cleere2024hpvovertakessmoking pages 1-2) | Cleere et al., 2024, *Irish Journal of Medical Science* | DOI: 10.1007/s11845-024-03715-4 |
| Prognosis | In p16+/HPV- OPSCC (n=20), 5-year survival was 33% versus 77% in p16+/HPV+ disease; 95% were downstaged by TNM8 despite mortality about twice that of p16+/HPV+ patients (HR 2.66, 95% CI 1.37-5.15) (craig2019recommendationsfordetermining pages 1-2) | Craig et al., 2019, *British Journal of Cancer* | DOI: 10.1038/s41416-019-0414-9 |
| Treatment/Trials | ECOG-ACRIN E3311 is a phase II randomized trial in resectable p16+ locally advanced OPC: all patients undergo transoral surgery, then risk-adapted therapy. Intermediate-risk patients are randomized to 50 Gy/25 fractions versus 60 Gy/30 fractions IMRT; high-risk patients receive 66 Gy plus cisplatin. Enrollment: 519 (NCT01898494 chunk 1) | ECOG-ACRIN E3311 registry entry | NCT01898494 |
| Treatment/Trials | PATHOS is a phase III risk-stratified post-transoral surgery trial in HPV+ OPSCC. Intermediate-risk group: PORT 60 Gy/30 fractions vs 50 Gy/25 fractions; high-risk group: POCRT 60 Gy with cisplatin vs PORT 60 Gy alone. Co-primary endpoints include MDADI swallowing score and overall survival. Target enrollment increased to 1269 (NCT02215265 chunk 1) | PATHOS registry entry | NCT02215265 |
| Prevention/Policy | HPV vaccination is the main preventive strategy; studies cited in the review report 88-93% efficacy against oral HPV infection when given prior to sexual debut (ndon2023humanpapillomavirusassociatedoropharyngeal pages 1-3) | Ndon et al., 2023, *Cancers* | DOI: 10.3390/cancers15164080 |
| Prevention/Policy | As of 2022, 122/195 (63%) WHO member states had national HPV vaccination programs, but only 41/122 (34%) had gender-neutral vaccination coverage (ndon2023humanpapillomavirusassociatedoropharyngeal pages 1-3, ndon2023humanpapillomavirusassociatedoropharyngeal pages 10-12) | Ndon et al., 2023, *Cancers* | DOI: 10.3390/cancers15164080 |
| Prevention/Policy | In Texas, county-level HPV vaccine initiation in 2021-2022 ranged from 6.3%-69.1% in females and 7.0%-77.6% in males aged 9-17; up-to-date coverage ranged from 1.6%-30.4% in females and 2.1%-34.8% in males, underscoring prevention gaps (adekanmbi2024humanpapillomavirusvaccination pages 1-2) | Adekanmbi et al., 2024, *JAMA Network Open* | DOI: 10.1001/jamanetworkopen.2024.31807 |


*Table: This table compiles concise, evidence-backed facts on HPV-positive head and neck squamous cell carcinoma, with emphasis on HPV-positive OPSCC. It highlights the most actionable findings from the gathered sources across epidemiology, mechanism, diagnostics, prognosis, trials, and prevention.*

---

## Expert analysis and key takeaways (evidence-grounded)
1. **HPV+ OPSCC is expanding as a public health burden**, with increasing HPV positivity proportions in US SEER OPSCC and rising HPV-linked fractions in institutional cohorts. (kim2024aseerbasedanalysis pages 1-2, cleere2024hpvovertakessmoking pages 1-2)
2. **Biological heterogeneity matters**: HPV integration status may identify a poorer-prognosis subgroup with reduced cytotoxic T infiltration, suggesting that “HPV-positive” is not a sufficient classifier for therapeutic decision-making. (tabatabaeian2024navigatingtherapeuticstrategies pages 1-2)
3. **Testing strategy has direct clinical consequences**: p16-only classification can mis-stage biologically distinct tumors; p16+/HPV− tumors have survival closer to HPV-negative disease, supporting two-tier HPV testing. (craig2019recommendationsfordetermining pages 1-2, yang2023aptimahrhpvtesting pages 1-2)
4. **Immune biology is complex**: scRNA-seq supports enhanced interferon/MHC-II programs in HPV+ tumor cells and CXCL13+CD4+ interactions, but checkpoint inhibitor response rates remain ~20%, reinforcing the need for better predictive biomarkers. (yan2024decipheringtheinterplay pages 1-2)
5. **De-intensification is being operationalized through risk-stratified surgical pathways** (E3311, PATHOS), with co-primary functional outcomes (swallowing) embedded—reflecting a mature shift from purely survival endpoints toward survivorship optimization. (NCT01898494 chunk 1, NCT02215265 chunk 1)

---

## Limitations of this report
Several template elements (ontology IDs, detailed phenotype frequencies, specific host somatic driver gene frequencies, animal models) were not retrievable from the current tool-acquired evidence corpus and are therefore explicitly not fully populated. Where ontology terms were suggested, they are presented as **candidate mappings** rather than evidence-derived annotations.


References

1. (yan2024decipheringtheinterplay pages 1-2): Shida Yan, Xing Zhang, Qiaohong Lin, Mingyuan Du, Yiqi Li, Shuai He, Jingtao Chen, Xiyuan Li, Jinxin Bei, Shuwei Chen, and Ming Song. Deciphering the interplay of hpv infection, mhc-ii expression, and cxcl13+ cd4+ t cell activation in oropharyngeal cancer: implications for immunotherapy. Cancer Immunology, Immunotherapy : CII, Aug 2024. URL: https://doi.org/10.1007/s00262-024-03789-0, doi:10.1007/s00262-024-03789-0. This article has 11 citations.

2. (ndon2023humanpapillomavirusassociatedoropharyngeal pages 1-3): Sifon Ndon, Amritpal Singh, Patrick K. Ha, Joyce Aswani, Jason Ying-Kuen Chan, and Mary Jue Xu. Human papillomavirus-associated oropharyngeal cancer: global epidemiology and public policy implications. Cancers, 15:4080, Aug 2023. URL: https://doi.org/10.3390/cancers15164080, doi:10.3390/cancers15164080. This article has 58 citations.

3. (craig2019recommendationsfordetermining pages 1-2): Stephanie G. Craig, Lesley A. Anderson, Andrew G. Schache, Michael Moran, Laura Graham, Keith Currie, Keith Rooney, Max Robinson, Navdeep S. Upile, Rachel Brooker, Mina Mesri, Victoria Bingham, Stephen McQuaid, Terry Jones, Dennis J. McCance, Manuel Salto-Tellez, Simon S. McDade, and Jacqueline A. James. Recommendations for determining hpv status in patients with oropharyngeal cancers under tnm8 guidelines: a two-tier approach. British Journal of Cancer, 120:827-833, Mar 2019. URL: https://doi.org/10.1038/s41416-019-0414-9, doi:10.1038/s41416-019-0414-9. This article has 121 citations and is from a domain leading peer-reviewed journal.

4. (kim2024aseerbasedanalysis pages 1-2): Su Il Kim, Jung Woo Lee, Young-Gyu Eun, and Young Chan Lee. A seer-based analysis of trends in hpv-associated oropharyngeal squamous cell carcinoma. Infectious Agents and Cancer, Jun 2024. URL: https://doi.org/10.1186/s13027-024-00592-5, doi:10.1186/s13027-024-00592-5. This article has 12 citations and is from a peer-reviewed journal.

5. (cleere2024hpvovertakessmoking pages 1-2): Eoin F. Cleere, Josh Murphy, Thomas J. Crotty, Justin M. Hintze, Conrad V. I. Timon, John Kinsella, Conall W. R. Fitzgerald, and Paul Lennon. Hpv overtakes smoking as the leading cause of oropharyngeal cancer in ireland: experience of a head and neck surgery tertiary referral centre. Irish Journal of Medical Science, 193:2161-2169, May 2024. URL: https://doi.org/10.1007/s11845-024-03715-4, doi:10.1007/s11845-024-03715-4. This article has 5 citations and is from a peer-reviewed journal.

6. (NCT01898494 chunk 1):  Transoral Surgery Followed By Low-Dose or Standard-Dose Radiation Therapy With or Without Chemotherapy in Treating Patients With HPV Positive Stage III-IVA Oropharyngeal Cancer. ECOG-ACRIN Cancer Research Group. 2014. ClinicalTrials.gov Identifier: NCT01898494

7. (NCT02215265 chunk 1): Lisette Nixon. Post-operative Adjuvant Treatment for HPV-positive Tumours (PATHOS). Lisette Nixon. 2015. ClinicalTrials.gov Identifier: NCT02215265

8. (wu2024deescalationstrategiesin pages 1-2): Clinton Wu, Paulina Kuzmin, and Ricklie Julian. De-escalation strategies in hpv-associated oropharynx cancer: a historical perspective with future direction. Cancers, 16:2733, Aug 2024. URL: https://doi.org/10.3390/cancers16152733, doi:10.3390/cancers16152733. This article has 10 citations.

9. (krsek2024thenextchapter pages 1-2): Antea Krsek, Lara Baticic, Tamara Braut, and Vlatka Sotosek. The next chapter in cancer diagnostics: advances in hpv-positive head and neck cancer. Biomolecules, 14:925, Jul 2024. URL: https://doi.org/10.3390/biom14080925, doi:10.3390/biom14080925. This article has 12 citations.

10. (tabatabaeian2024navigatingtherapeuticstrategies pages 1-2): Hossein Tabatabaeian, Yuchen Bai, Ruihong Huang, Akhilanand Chaurasia, and Charbel Darido. Navigating therapeutic strategies: hpv classification in head and neck cancer. British Journal of Cancer, 131:220-230, Apr 2024. URL: https://doi.org/10.1038/s41416-024-02655-1, doi:10.1038/s41416-024-02655-1. This article has 36 citations and is from a domain leading peer-reviewed journal.

11. (atique2024comprehensiveanalysisof pages 55-58): M Atique. Comprehensive analysis of genetic mutations in hpv-positive and hpv-negative oropharyngeal squamous cell carcinoma: a literature review. Unknown journal, 2024.

12. (cleere2024hpvovertakessmoking pages 9-9): Eoin F. Cleere, Josh Murphy, Thomas J. Crotty, Justin M. Hintze, Conrad V. I. Timon, John Kinsella, Conall W. R. Fitzgerald, and Paul Lennon. Hpv overtakes smoking as the leading cause of oropharyngeal cancer in ireland: experience of a head and neck surgery tertiary referral centre. Irish Journal of Medical Science, 193:2161-2169, May 2024. URL: https://doi.org/10.1007/s11845-024-03715-4, doi:10.1007/s11845-024-03715-4. This article has 5 citations and is from a peer-reviewed journal.

13. (yang2023aptimahrhpvtesting pages 1-2): Xin Yang, Chunfang Hu, Huan Zhao, Zhi-hui Zhang, LinLin Zhao, Jing Yu, Xiaoguang Ni, and Huiqin Guo. Aptima hr-hpv testing of cytology specimens is an effective supplement for p16 staining to improve diagnostic accuracy for hpv-related oropharyngeal squamous cell carcinoma. Acta Cytologica, 67:321-332, Dec 2023. URL: https://doi.org/10.1159/000527951, doi:10.1159/000527951. This article has 7 citations and is from a peer-reviewed journal.

14. (ndon2023humanpapillomavirusassociatedoropharyngeal pages 10-12): Sifon Ndon, Amritpal Singh, Patrick K. Ha, Joyce Aswani, Jason Ying-Kuen Chan, and Mary Jue Xu. Human papillomavirus-associated oropharyngeal cancer: global epidemiology and public policy implications. Cancers, 15:4080, Aug 2023. URL: https://doi.org/10.3390/cancers15164080, doi:10.3390/cancers15164080. This article has 58 citations.

15. (adekanmbi2024humanpapillomavirusvaccination pages 1-2): Victor Adekanmbi, Itunu Sokale, Fangjian Guo, Jessica Ngo, Thao N. Hoang, Christine D. Hsu, Abiodun Oluyomi, and Abbey B. Berenson. Human papillomavirus vaccination and human papillomavirus–related cancer rates. JAMA Network Open, 7:e2431807, Sep 2024. URL: https://doi.org/10.1001/jamanetworkopen.2024.31807, doi:10.1001/jamanetworkopen.2024.31807. This article has 13 citations and is from a peer-reviewed journal.
