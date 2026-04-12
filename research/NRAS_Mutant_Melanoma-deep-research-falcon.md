---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-05T20:42:43.545273'
end_time: '2026-04-05T20:50:24.649220'
duration_seconds: 461.1
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: NRAS Mutant Melanoma
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 35
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** NRAS Mutant Melanoma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **NRAS Mutant Melanoma** covering all of the
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
- **Disease Name:** NRAS Mutant Melanoma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **NRAS Mutant Melanoma** covering all of the
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


## Comprehensive Research Report: NRAS Mutant Melanoma

### Target Disease
- **Disease name:** NRAS mutant melanoma (primarily discussed as NRAS-mutant cutaneous melanoma in the retrieved sources)
- **MONDO ID:** Not found in retrieved sources for the *molecular subtype* “NRAS-mutant melanoma” (see Identifiers section).
- **Category:** Malignant melanoma; molecularly defined subtype (RAS/MAPK-pathway driver-defined cutaneous melanoma subgroup).

---

## 1. Disease Information

### 1.1 Concise overview
NRAS-mutant melanoma is a molecular subset of melanoma (most often cutaneous melanoma in the available evidence) characterized by activating somatic mutations in **NRAS**, a small GTPase that drives constitutive downstream signaling—most prominently **MAPK (RAF–MEK–ERK)** and frequently **PI3K–AKT** pathway activity—leading to increased proliferation and survival. In contemporary clinical practice, it is recognized as a therapeutically important subgroup because (i) it represents ~15–20% of melanomas, (ii) **direct mutant-NRAS inhibitors have historically been lacking**, and (iii) treatment is typically centered on immune checkpoint blockade with targeted therapy options being limited and/or modest in efficacy. (phadke2023targetingnrasmutationsinadvanced pages 1-2, braud2023initialevidencefor pages 1-3)

A key molecular feature is that the predominant NRAS mutations in melanoma occur at **codon 61** (Q61), which impair intrinsic GTPase activity and keep NRAS in a GTP-bound “ON” state. (phadke2023targetingnrasmutationsinadvanced pages 1-2, zhao2021novelinsightsinto pages 3-4)

### 1.2 Key identifiers and cross-references
The retrieved literature did not provide canonical disease identifiers (ICD-10/ICD-11, MeSH, OMIM, Orphanet, MONDO) specifically for the *molecular subtype* “NRAS-mutant melanoma.” The Open Targets search returned broader melanoma concepts (e.g., melanoma and cutaneous melanoma) with evidence linked to NRAS, but not a dedicated “NRAS-mutant melanoma” MONDO identifier in the retrieved outputs. (phadke2023targetingnrasmutationsinadvanced pages 1-2, braud2023initialevidencefor pages 1-3)

**Ontology summary artifact:**

| Concept | Ontology/ID (MONDO/MeSH/ICD if available) | Notes |
|---|---|---|
| NRAS-mutant melanoma | MONDO: not found in retrieved sources | Molecularly defined melanoma subset; retrieved evidence describes it as a subtype of cutaneous melanoma driven by activating NRAS mutations, present in ~15%–20% of melanomas (phadke2023targetingnrasmutationsinadvanced pages 1-2, braud2023initialevidencefor pages 1-3) |
| NRAS-mutated melanoma | MONDO: not found in retrieved sources | Synonymous wording used in reviews and clinical trial literature for the same entity (phadke2023targetingnrasmutationsinadvanced pages 1-2, braud2023initialevidencefor pages 1-3) |
| NRAS-mutant cutaneous melanoma | ICD/MeSH/MONDO specific identifier for this molecular subtype: not found in retrieved sources | Most retrieved evidence concerns cutaneous melanoma specifically; one 2024 cohort classified cutaneous melanoma into BRAF-mutant, NRAS-mutant, NF1-mutant, and triple wild-type groups (haugh2024targeteddnasequencing pages 1-2) |
| NRAS Q61-mutant melanoma | MONDO: not found in retrieved sources | Common hotspot-defined synonym; codon 61 alterations account for the great majority of NRAS mutations in melanoma (>80% in one 2023 review; ~84% in one 2021 review) (phadke2023targetingnrasmutationsinadvanced pages 1-2, zhao2021novelinsightsinto pages 3-4) |
| NRAS Q61R/K/L-mutant melanoma | MONDO: not found in retrieved sources | More specific hotspot grouping; Q61R, Q61K, and Q61L are repeatedly highlighted as predominant melanoma-associated variants (phadke2023targetingnrasmutationsinadvanced pages 1-2, murphy2022enhancedbrafengagement pages 1-2) |
| Cutaneous melanoma | MeSH/ICD/MONDO specific identifier not retrieved; Open Targets disease ID for cutaneous melanoma: EFO_0000389 | Parent disease concept used by several retrieved sources when discussing the NRAS-mutant subgroup (haugh2024targeteddnasequencing pages 1-2) |
| Melanoma | MeSH/ICD/MONDO specific identifier not retrieved; Open Targets disease ID for melanoma: EFO_0000756 | Broader parent disease concept; disease-target association with NRAS was retrieved for melanoma generally (Open Targets result in prior tool output; molecular subgroup details supported by review evidence) (phadke2023targetingnrasmutationsinadvanced pages 1-2, braud2023initialevidencefor pages 1-3) |
| Superficial spreading melanoma | MONDO_0020638 | Retrieved as a melanoma histologic subtype in Open Targets output; not synonymous with NRAS-mutant melanoma, but relevant as a parent histologic melanoma concept distinct from the molecular subtype (supported context on melanoma subtyping) (haugh2024targeteddnasequencing pages 1-2) |


*Table: This table maps the disease naming used in the retrieved evidence for NRAS-mutant melanoma and related parent concepts. It is useful for ontology normalization because the retrieved sources support the molecular subtype terminology but did not provide a dedicated MONDO/MeSH/ICD identifier for the subtype itself.*

### 1.3 Synonyms / alternative names
Commonly used synonyms in the literature include:
- “NRAS-mutant melanoma” / “NRAS-mutated melanoma” (phadke2023targetingnrasmutationsinadvanced pages 1-2, braud2023initialevidencefor pages 1-3)
- “NRAS Q61-mutant melanoma” and variant-specific groupings such as “NRAS Q61R/K/L melanoma” (phadke2023targetingnrasmutationsinadvanced pages 1-2, murphy2022enhancedbrafengagement pages 1-2)

### 1.4 Evidence source type
The retrieved evidence is primarily:
- Aggregated disease-level resources (systematic review/meta-analysis of immunotherapy response) (jaeger2023objectiveresponseto pages 1-2)
- Prospective/retrospective human cohorts for clinicopathologic correlations and outcomes (devitt2011clinicaloutcomeand pages 1-3, haugh2024targeteddnasequencing pages 1-2)
- Interventional clinical trials for targeted therapy combinations (braud2023initialevidencefor pages 1-3, queirolo2017binimetinibforthe pages 9-11)
- Genetically engineered mouse models (GEMMs) and mechanistic studies (burd2014mutationspecificrasoncogenicity pages 1-3, murphy2022enhancedbrafengagement pages 1-2, johanna2021epigeneticcontrolof pages 1-2, yang2023cxcr2expressionduring pages 1-2)

---

## 2. Etiology

### 2.1 Disease causal factors
**Genetic (somatic) driver:** Activating somatic mutations in **NRAS** are a central causal factor defining the subtype. NRAS mutations are reported in ~15–20% of melanomas in multiple sources. (phadke2023targetingnrasmutationsinadvanced pages 1-2, braud2023initialevidencefor pages 1-3)

**Hotspot biology:** A 2023 JCO review states that the predominant alterations (>80%) occur at codon 61 (Q61R, Q61L, Q61K) and “serve to impair GTPase activity, locking the gene in a constitutively ON position.” (phadke2023targetingnrasmutationsinadvanced pages 1-2)

### 2.2 Risk factors
**Tumor/pathology-associated “risk correlates” for NRAS-mutant status (not necessarily causal exposures):**
- In a prospective cohort, NRAS-mutant primary cutaneous melanomas were associated with greater thickness and higher mitotic activity: “Seventy-five percentage of NRAS mutations occurred in tumors >1 mm thick …” and “Twenty-seven (75%) tumors with NRAS mutations had a mitotic count of >1/mm2 … (P = 0.001).” (devitt2011clinicaloutcomeand pages 1-3)
- NRAS mutations were enriched in nodular melanoma in this cohort: “9 (25%) of all NRAS mutations occurring in this subtype (P < 0.001).” (devitt2011clinicaloutcomeand pages 1-3)

**Ultraviolet (UV) exposure and chronic sun damage (CSD):** Evidence in retrieved sources is mixed depending on the study design and definition.
- Devitt et al. reported: “There was no association between chronic sun damage and NRAS mutations.” (devitt2011clinicaloutcomeand pages 1-3)
- A 2024 targeted-sequencing cohort notes a molecular classification context where “BRAF and NRAS mutant melanomas correlate with low cumulative sun damage (low-CSD), while NF1 mutants are high-CSD.” (haugh2024targeteddnasequencing pages 1-2)

Given these differences, UV is clearly etiologic for cutaneous melanoma broadly, but the *specific relationship* between chronic sun damage patterns and NRAS-mutant subtype varies across cohorts and should be represented as heterogeneous evidence rather than a single settled association. (devitt2011clinicaloutcomeand pages 1-3, haugh2024targeteddnasequencing pages 1-2)

### 2.3 Protective factors
No genotype-specific protective factors were identified in the retrieved sources.

### 2.4 Gene–environment interactions
Direct gene–environment interaction evidence specific to NRAS-mutant melanoma was not identified in the retrieved sources (beyond the broader context that UV contributes to melanoma mutagenesis and that NRAS hotspot variants are selected by functional constraints). (murphy2022enhancedbrafengagement pages 1-2)

---

## 3. Phenotypes

### 3.1 Clinical and pathological phenotype spectrum
NRAS-mutant melanoma generally presents clinically as cutaneous melanoma, with pathological correlates that may indicate a more aggressive primary tumor phenotype in multiple cohorts.

From Devitt et al. (prospective cohort):
- Greater tumor thickness: “Seventy-five percentage of NRAS mutations occurred in tumors >1 mm thick …” (devitt2011clinicaloutcomeand pages 1-3)
- Higher mitotic activity: “Twenty-seven (75%) tumors with NRAS mutations had a mitotic count of >1/mm2 … (P = 0.001).” (devitt2011clinicaloutcomeand pages 1-3)
- Nodular enrichment: “9 (25%) of all NRAS mutations occurring in this subtype (P < 0.001).” (devitt2011clinicaloutcomeand pages 1-3)

### 3.2 Onset, severity, progression
Specific age-of-onset distributions for the NRAS-mutant subgroup were not extracted from the retrieved evidence. However, the subgroup is repeatedly described as clinically challenging and (in multiple sources) as associated with poorer prognosis than NRAS-wildtype melanoma. (braud2023initialevidencefor pages 1-3, jaeger2023objectiveresponseto pages 1-2)

### 3.3 Quality of life impact
NRAS-mutant melanoma–specific quality-of-life measures were not identified in the retrieved sources.

### 3.4 Suggested HPO terms (phenotype representation suggestions)
These are suggested to structure typical melanoma features and aggressive primary features described above:
- **Cutaneous melanoma / malignant melanoma:** *no single HPO term asserted here from evidence; use clinical coding per knowledge base conventions*
- **Increased mitotic activity:** HP:0010644 (Increased mitotic activity) (maps to the cohort observation of higher mitotic count) (devitt2011clinicaloutcomeand pages 1-3)
- **Increased tumor thickness (Breslow):** represent as a quantitative pathology attribute (no specific HPO term was retrieved in evidence)
- **Nodular melanoma subtype:** represent as histologic subtype attribute (not strictly an HPO term)

---

## 4. Genetic / Molecular Information

### 4.1 Causal gene
- **NRAS** (NRAS proto-oncogene, GTPase) is the defining causal driver gene for the subtype. (phadke2023targetingnrasmutationsinadvanced pages 1-2, braud2023initialevidencefor pages 1-3)

### 4.2 Pathogenic variants (somatic)
**Hotspots:** Codon 61 is dominant.
- 2023 JCO review: predominant alterations (>80%) at codon 61 (Q61R, Q61L, Q61K). (phadke2023targetingnrasmutationsinadvanced pages 1-2)
- 2021 review excerpt: “The majority (~84%) of NRAS mutations occur at codon 61.” (zhao2021novelinsightsinto pages 3-4)

**Functional consequence:** Gain-of-function with impaired GTPase activity and increased signaling output.
- Direct quote: codon 61 variants “serve to impair GTPase activity, locking the gene in a constitutively ON position.” (phadke2023targetingnrasmutationsinadvanced pages 1-2)

### 4.3 Key downstream pathways and cellular programs
NRAS activation drives multiple signaling cascades.
- Devitt et al.: “NRAS ... leads to upregulation of the MAPK pathway, the phosphatidylinositol 3¢ kinase (PI3K) pathway and the RAL pathway.” (devitt2011clinicaloutcomeand pages 1-3)
- Phadke & Smalley emphasize strong MAPK activation and note NRAS-mutant melanomas signal via **CRAF rather than BRAF** (mechanistic framing in the excerpt). (phadke2023targetingnrasmutationsinadvanced pages 1-2)

### 4.4 Modifier genes / co-alterations (treatment-relevant)
A practical treatment-relevant modifier concept is cell-cycle gene co-alteration.
- In the ribociclib+binimetinib trial, response was higher in tumors with NRAS mutation plus concurrent alterations in **CDKN2A/CDK4/CCND1** (ORR 32.5% in that subgroup). (braud2023initialevidencefor pages 1-3)

### 4.5 Epigenetic information
A NRASQ61K;Cdkn2a−/− GEMM study links epigenetic regulation to invasiveness via SALL4 and HDAC2.
- “SALL4 negatively regulates invasiveness through interaction with the histone deacetylase (HDAC) 2 …” and “SALL4 loss induces a phenotype switch and the acquisition of an invasive phenotype.” (johanna2021epigeneticcontrolof pages 1-2)

### 4.6 Suggested ontology terms (GO/Reactome-style; representation suggestions)
Based on pathways explicitly described in evidence:
- **GO:0000165** (MAPK cascade) — supported by MAPK upregulation statements (devitt2011clinicaloutcomeand pages 1-3)
- **GO:0014065** (phosphatidylinositol 3-kinase signaling) — supported by PI3K pathway mention (devitt2011clinicaloutcomeand pages 1-3)
- **GO:0007264** (small GTPase mediated signal transduction) — aligns with NRAS biology (phadke2023targetingnrasmutationsinadvanced pages 1-2)

---

## 5. Environmental Information
The retrieved sources did not provide detailed environmental exposure quantification specific to NRAS-mutant melanoma beyond the mixed findings regarding chronic sun damage patterns in relation to NRAS-mutant status. (devitt2011clinicaloutcomeand pages 1-3, haugh2024targeteddnasequencing pages 1-2)

---

## 6. Mechanism / Pathophysiology

### 6.1 Causal chain (high-level)
1) **Somatic NRAS activating mutation** (most commonly codon 61) impairs GTPase activity, increasing the fraction of NRAS in the active GTP-bound state. (phadke2023targetingnrasmutationsinadvanced pages 1-2, burd2014mutationspecificrasoncogenicity pages 1-3)
2) Active NRAS drives downstream signaling through MAPK and other cascades (PI3K, RAL), increasing proliferation and survival. (devitt2011clinicaloutcomeand pages 1-3)
3) Additional cooperating alterations (e.g., loss of cell-cycle checkpoints such as Cdkn2a/INK4a in experimental models; cell-cycle co-alterations in human tumors) promote tumor initiation/progression and influence therapeutic vulnerabilities. (burd2014mutationspecificrasoncogenicity pages 1-3, braud2023initialevidencefor pages 1-3)

### 6.2 Codon-specific selection and RAF engagement (mechanistic advances)
Mechanistic work supports that melanoma-enriched NRAS Q61 variants have properties that favor melanoma initiation.
- Burd et al. (2014) found NRASQ61R is melanomagenic in vivo (especially with p16INK4a/Cdkn2a loss) while NRASG12D is not, and that enhanced GTP-bound state and stability contribute to oncogenicity. (burd2014mutationspecificrasoncogenicity pages 1-3)
- Murphy et al. (2022) used an allelic series of endogenous Nras knock-in models and report that common melanoma-associated Q61 mutants (Q61R, Q61K, Q61L) are potent drivers, and provide a mechanistic basis: melanomagenic Q61 mutants enhance BRAF binding and BRAF–CRAF dimer formation, increasing MAPK→ERK signaling. (murphy2022enhancedbrafengagement pages 1-2)

### 6.3 Immune microenvironment involvement (preclinical)
In an NRasQ61R/Ink4a−/− GEMM, modulating CXCR2 altered tumor induction and anti-tumor immunity.
- Genetic or pharmacologic inhibition of CXCR2 during induction “reduced tumor incidence/growth and increased anti-tumor immunity,” with mechanistic correlates including altered transcriptional programs and reduced AKT/mTOR activation. (yang2023cxcr2expressionduring pages 1-2)

### 6.4 Suggested Cell Ontology (CL) terms (representation suggestions)
- **CL:0000542** (lymphocyte) and **CL:0000624** (CD8-positive, alpha-beta T cell) — relevant given anti-tumor immunity and CD8+ involvement described in mouse immunology context (yang2023cxcr2expressionduring pages 1-2)
- **CL:0000235** (macrophage) — relevant to tumor immune microenvironment modulation studies (yang2023cxcr2expressionduring pages 1-2)

---

## 7. Anatomical Structures Affected

### 7.1 Organ/tissue level
NRAS-mutant melanoma in the retrieved evidence is largely discussed in the context of **cutaneous melanoma** with primary lesions in the skin and metastatic spread typical of melanoma (not systematically enumerated in the retrieved sources). (devitt2011clinicaloutcomeand pages 1-3, haugh2024targeteddnasequencing pages 1-2)

**Suggested UBERON terms (representation suggestions):**
- **UBERON:0002097** (skin of body)
- **UBERON:0000955** (brain) may be relevant for melanoma metastasis generally, but brain-metastasis-specific NRAS-mutant data were not retrieved here.

---

## 8. Temporal Development
Temporal staging/progression patterns specific to NRAS-mutant melanoma were not explicitly extracted from the retrieved sources beyond associations with primary tumor aggressiveness markers (thickness, mitotic rate) and worsened survival metrics in some cohorts. (devitt2011clinicaloutcomeand pages 1-3, haugh2024targeteddnasequencing pages 1-2)

---

## 9. Inheritance and Population

### 9.1 Epidemiology
The retrieved sources did not provide population incidence/prevalence for NRAS-mutant melanoma as a distinct entity. However, multiple sources converge that **NRAS mutations occur in ~15–20% of melanomas**, which can be used as an approximate subtype fraction among melanoma cases. (phadke2023targetingnrasmutationsinadvanced pages 1-2, braud2023initialevidencefor pages 1-3)

### 9.2 Inheritance
NRAS-mutant melanoma is primarily defined by **somatic** tumor mutations rather than a Mendelian inherited pattern in the retrieved evidence. (phadke2023targetingnrasmutationsinadvanced pages 1-2)

---

## 10. Diagnostics

### 10.1 Standard diagnostic approach (as supported in retrieved evidence)
The key diagnostic discriminator for this subtype is **tumor genomic testing** (targeted NGS panels or hotspot assays) to identify NRAS driver mutations.
- A 2024 clinical cohort explicitly uses molecular grouping of cutaneous melanoma into “BRAF mutant, NRAS mutant, NF1 loss, and triple wild type (TWT).” (haugh2024targeteddnasequencing pages 1-2)

### 10.2 Biomarkers and molecular stratification
- **NRAS mutation status** (particularly codon 61) is the defining biomarker. (phadke2023targetingnrasmutationsinadvanced pages 1-2, zhao2021novelinsightsinto pages 3-4)
- **Tumor mutational burden (TMB)** may be predictive for benefit from dual checkpoint blockade in melanoma broadly: in one cohort, “Elevated TMB correlated with improved progression-free survival on combination checkpoint inhibition (anti-PD1 plus anti-CTLA4).” (haugh2024targeteddnasequencing pages 1-2)

### 10.3 Suggested diagnostic ontology terms (representation suggestions)
- MAXO:0000136 (tumor genomic sequencing / next-generation sequencing) — suggested for molecular classification workflows (haugh2024targeteddnasequencing pages 1-2)

---

## 11. Outcome / Prognosis
NRAS mutation status has been associated with worse prognosis in multiple contexts, though effects can vary by cohort and treatment era.

- Devitt et al. reported NRAS mutations were independently associated with worse melanoma-specific survival: “(hazard ratio (HR) 2.96; P = 0.04).” (devitt2011clinicaloutcomeand pages 1-3)
- In a 2024 cohort (n=254), “NRAS mutant melanoma demonstrated significantly decreased overall survival on multivariable analysis (HR for death 2.95, 95% CI 1.13–7.69, p = 0.027).” (haugh2024targeteddnasequencing pages 1-2)

These findings support representing NRAS mutation as an adverse prognostic factor in at least some clinical populations, while noting that immunotherapy response may be comparable or better than NRAS-wildtype based on pooled response analyses (below). (haugh2024targeteddnasequencing pages 1-2, jaeger2023objectiveresponseto pages 1-2)

---

## 12. Treatment

### 12.1 Current standard-of-care and real-world implementation
The retrieved sources consistently position **immune checkpoint inhibitors (ICIs)** as the mainstay systemic therapy for advanced/metastatic NRAS-mutant melanoma, in the absence of an approved direct NRAS inhibitor. (phadke2023targetingnrasmutationsinadvanced pages 1-2, braud2023initialevidencefor pages 1-3)

**Evidence synthesis for ICI response by genotype:**
- Systematic review/meta-analysis (Frontiers in Medicine, Feb 2023): pooled data from 1,770 patients found NRAS-mutant melanoma had a higher likelihood of objective response compared with NRAS-wildtype, effect size **1.28 (95% CI 1.01–1.64)**. (jaeger2023objectiveresponseto pages 1-2)

### 12.2 Targeted therapies and combinations (key trials)
No approved targeted therapy for NRAS-mutant melanoma is asserted in the retrieved JCO sources; MEK inhibition has modest activity and is a common development backbone. (phadke2023targetingnrasmutationsinadvanced pages 1-2, braud2023initialevidencefor pages 1-3)

**Binimetinib (MEK inhibitor), NEMO trial benchmark:**
- Reported outcomes (as summarized in retrieved sources): median PFS **2.8 vs 1.5 months** (binimetinib vs dacarbazine; HR 0.62), ORR ~**15% vs 7%**, median OS **11.0 vs 10.1 months** (no OS benefit). (queirolo2017binimetinibforthe pages 9-11)
- Notable tolerability issues included higher discontinuation for toxicity (25% vs 8%) and frequent dose reductions/interruptions. (queirolo2017binimetinibforthe pages 9-11)

**Naporafenib (RAF inhibitor) + trametinib (MEK inhibitor):**
- In the JCO 2023 expansion arm, ORR reached **46.7% (7/15)** at naporafenib 200 mg BID + trametinib 1 mg daily with median PFS **5.52 months**; a higher-dose naporafenib cohort had lower ORR (13.3%). (braud2023initialevidencefor pages 1-3)

**Ribociclib (CDK4/6 inhibitor) + binimetinib:**
- Phase Ib/II: ORR **19.5% (8/41)** at RP2D; ORR **32.5%** in tumors with concurrent CDKN2A/CDK4/CCND1 alterations; median PFS **3.7 months**; median OS **11.3 months**. (braud2023initialevidencefor pages 1-3)

**Treatment evidence artifact (trial summary table):**

| Therapy/Approach | Study (first author, year, journal) | Population | Key efficacy results (ORR/PFS/OS with numbers) | Key safety signals | URL/DOI | Notes (e.g., line of therapy) |
|---|---|---|---|---|---|---|
| MEK inhibitor: binimetinib vs dacarbazine (NEMO phase III) | Dummer 2017, *Lancet Oncology*; summarized in Phadke 2023, *JCO* and Queirolo 2017, *Expert Rev Anticancer Ther* | 402 patients with advanced/unresectable or metastatic NRAS-mutant melanoma randomized 2:1 to binimetinib vs dacarbazine | Median PFS 2.8 vs 1.5 months (HR 0.62, 95% CI 0.47-0.80); ORR 15% vs 7% (or 15.2% vs 6.8% in summary source); DCR 58% vs 25%; median OS 11.0 vs 10.1 months (HR 1.00, 95% CI 0.75-1.33); prior-immunotherapy subgroup median PFS 5.5 months (phadke2023targetingnrasmutationsinadvanced pages 1-2, queirolo2017binimetinibforthe pages 6-9, queirolo2017binimetinibforthe pages 9-11) | More grade 3-4 AEs with binimetinib; increased CPK notable (19% vs 0%); dose reductions 61% vs 16%; interruptions 58% vs 29%; permanent discontinuation for toxicity 25% vs 8%; ocular and cardiac toxicities reported (queirolo2017binimetinibforthe pages 9-11) | https://doi.org/10.1016/S1470-2045(17)30180-8; https://doi.org/10.1200/JCO.23.00205; https://doi.org/10.1080/14737140.2017.1374177 | First phase III targeted-therapy trial showing activity in NRAS-mutant melanoma, but no OS benefit; generally considered after or outside standard immunotherapy pathways (phadke2023targetingnrasmutationsinadvanced pages 1-2, queirolo2017binimetinibforthe pages 9-11) |
| Pan-RAF inhibitor + MEK inhibitor: naporafenib + trametinib | de Braud 2023, *Journal of Clinical Oncology* | Phase Ib escalation/expansion in advanced/metastatic NRAS-mutant melanoma; expansion arm n=30 (15 per dose cohort) | At naporafenib 200 mg BID + trametinib 1 mg QD: ORR 46.7% (7/15; 95% CI 21.3-73.4), median DOR 3.75 months, median PFS 5.52 months. At naporafenib 400 mg BID + trametinib 0.5 mg QD: ORR 13.3% (2/15; 95% CI 1.7-40.5), median DOR 3.75 months, median PFS 4.21 months (braud2023initialevidencefor pages 1-3) | All 30 patients had treatment-related AEs; rash 80%; CPK increase, diarrhea, and nausea each 30%; grade >=3 DLTs in escalation included dermatitis acneiform, maculopapular rash, increased lipase, and Stevens-Johnson syndrome (braud2023initialevidencefor pages 1-3) | https://doi.org/10.1200/JCO.22.02018 | Early signal of higher response than historical MEK monotherapy; basis for later randomized development such as SEACRAFT-2 (trial not detailed here) (braud2023initialevidencefor pages 1-3) |
| MEK inhibitor + CDK4/6 inhibitor: ribociclib + binimetinib | Schuler 2022, *Clinical Cancer Research* | Phase Ib/II NRAS-mutant melanoma; phase II efficacy cohort n=41 at RP2D | ORR 19.5% (8/41; 95% CI 8.8-34.9) at RP2D; in patients with concurrent CDKN2A/CDK4/CCND1 alterations, ORR 32.5% (13/40; 95% CI 20.1-48.0); median PFS 3.7 months (95% CI 3.5-5.6); median OS 11.3 months (95% CI 9.3-14.2) (braud2023initialevidencefor pages 1-3) | Common toxicities included creatine phosphokinase elevation, rash, edema, anemia, nausea, diarrhea, and fatigue; 10 patients (16.4%) had dose-limiting toxicities in cycle 1 during phase Ib (braud2023initialevidencefor pages 1-3) | https://doi.org/10.1158/1078-0432.CCR-21-3872 | Rational combination for MAPK plus cell-cycle co-targeting; benefit may be enriched by cell-cycle co-alterations (braud2023initialevidencefor pages 1-3) |
| Immune checkpoint inhibitors (ICI), genotype-stratified evidence | Jaeger 2023, *Frontiers in Medicine* systematic review and meta-analysis | 10 studies; pooled data from 1,770 melanoma patients treated with ICIs comparing NRAS-mutant vs NRAS-wildtype disease | Pooled ORR effect size 1.28 (95% CI 1.01-1.64) favoring NRAS-mutant melanoma; conclusion: NRAS-mutant cutaneous melanoma had increased likelihood of partial or complete response relative to NRAS-wildtype melanoma (jaeger2023objectiveresponseto pages 1-2) | Meta-analysis focused on response, not pooled toxicity; safety signals not reported in retrieved excerpt (jaeger2023objectiveresponseto pages 1-2) | https://doi.org/10.3389/fmed.2023.1090737 | Supports current practice in which ICI remains standard of care for advanced NRAS-mutant melanoma despite lack of approved direct NRAS-targeted therapy (phadke2023targetingnrasmutationsinadvanced pages 1-2, jaeger2023objectiveresponseto pages 1-2) |


*Table: This table summarizes major therapeutic evidence in NRAS-mutant melanoma, including benchmark trial outcomes for MEK inhibition, emerging targeted combinations, and pooled immunotherapy response data. It is useful for comparing efficacy, toxicity, and clinical positioning of the main evidence-supported approaches.*

### 12.3 Suggested MAXO terms (treatment representation suggestions)
- Immune checkpoint inhibitor therapy (anti–PD-1 / anti–CTLA-4): MAXO terms depend on the ontology version used in the knowledge base; represent as “immune checkpoint blockade” supported as standard care (phadke2023targetingnrasmutationsinadvanced pages 1-2, jaeger2023objectiveresponseto pages 1-2)
- MEK inhibitor therapy: supported by NEMO and other MEK-inhibitor trials (queirolo2017binimetinibforthe pages 9-11)
- Combined RAF/MEK inhibition (nMRAS context: naporafenib+trametinib investigational): (braud2023initialevidencefor pages 1-3)
- CDK4/6 inhibitor + MEK inhibitor combination: (braud2023initialevidencefor pages 1-3)

---

## 13. Prevention
No NRAS-mutant–specific prevention strategies were identified in the retrieved sources. Prevention and screening would generally follow cutaneous melanoma recommendations (UV exposure reduction, skin surveillance), but genotype-specific prevention claims cannot be made from the retrieved evidence set.

---

## 14. Other Species / Natural Disease
Not addressed in retrieved sources.

---

## 15. Model Organisms
NRAS-mutant melanoma has multiple well-established genetically engineered mouse models used to study initiation, progression, metastasis, and immune regulation.

### 15.1 Key GEMMs and what they show
- **Endogenous conditional Nras Q61 allelic series (Tyr::CreERT2 activation; neonatal UVB cooperation):** Q61R, Q61K, Q61L are strong melanoma drivers with high penetrance; Q61P/Q61Q are not, and melanomagenic variants enhance BRAF engagement and BRAF–CRAF dimerization to increase ERK signaling. (murphy2022enhancedbrafengagement pages 1-2)
- **N-RasQ61R knock-in with Cdkn2a/p16INK4a loss:** Efficiently promotes melanoma in vivo, whereas N-RasG12D does not; supports codon-61 selection and the relevance of Q61 models for human NRAS-mutant melanoma. (burd2014mutationspecificrasoncogenicity pages 1-3)
- **Tyr::NrasQ61K; Cdkn2a−/− model in epigenetic invasiveness study:** Sall4 is re-expressed and “its expression is necessary for primary melanoma formation,” while Sall4 loss promotes micrometastases and induces an invasive phenotype via HDAC2-linked regulation. (johanna2021epigeneticcontrolof pages 1-2)
- **NRasQ61R/Ink4a−/− model in immune microenvironment modulation:** CXCR2 loss/inhibition during tumor induction reduces tumor incidence/growth and increases anti-tumor immunity, with associated transcriptional and signaling changes (including reduced AKT/mTOR activation). (yang2023cxcr2expressionduring pages 1-2)

### 15.2 Model limitations (from retrieved evidence)
Explicit limitations were not systematically discussed in the retrieved excerpts; however, several studies highlight that codon-specific biology and cooperating tumor suppressor contexts can strongly affect phenotype, emphasizing the need to match model genotype to the human tumor context (e.g., Cdkn2a/Ink4a loss, UV exposure paradigms). (burd2014mutationspecificrasoncogenicity pages 1-3, murphy2022enhancedbrafengagement pages 1-2)

---

## Recent Developments and “Latest Research” (prioritizing 2023–2024 in retrieved sources)

1) **Targeting strategies remain an unmet need; direct NRAS inhibitors historically lacking:** The 2023 JCO review emphasizes the lack of equivalent targeted inhibitors for mutant NRAS in melanoma and focuses on pathway targeting and emerging strategies. (phadke2023targetingnrasmutationsinadvanced pages 1-2)

2) **Genotype–immunotherapy response synthesis:** A 2023 systematic review/meta-analysis (Frontiers in Medicine; Feb 2023) pooled 10 studies/1,770 patients and found improved objective response likelihood for NRAS-mutant vs NRAS-wildtype melanoma (effect size 1.28). (jaeger2023objectiveresponseto pages 1-2)

3) **Emerging targeted combinations with higher response signals:** The 2023 JCO phase Ib expansion arm for **naporafenib+trametinib** reported ORR 46.7% in one dosing cohort, supporting ongoing randomized development. (braud2023initialevidencefor pages 1-3)

4) **Clinicogenomic outcome stratification in routine practice cohorts:** A 2024 cohort integrating targeted NGS and follow-up reported NRAS-mutant cutaneous melanoma had significantly worse overall survival (multivariable HR ~2.95) and that higher TMB predicted longer PFS on dual checkpoint blockade. (haugh2024targeteddnasequencing pages 1-2)

---

## Evidence gaps relative to the requested template (not found in retrieved sources)
- MONDO/MeSH/ICD identifiers specific to the “NRAS-mutant melanoma” subtype were not retrieved.
- Population-level incidence/prevalence statistics (e.g., SEER rates) were not retrieved.
- Detailed differential diagnosis and histopathology/IHC marker panels were not retrieved.
- NRAS-mutant–specific prevention and screening guidelines were not retrieved.

---

## URLs and publication dates (from retrieved evidence)
- Phadke MS, Smalley KSM. *Journal of Clinical Oncology*. **May 2023**. DOI: https://doi.org/10.1200/JCO.23.00205 (phadke2023targetingnrasmutationsinadvanced pages 1-2)
- de Braud F et al. *Journal of Clinical Oncology*. **May 2023**. DOI: https://doi.org/10.1200/JCO.22.02018 (braud2023initialevidencefor pages 1-3)
- Jaeger ZJ et al. *Frontiers in Medicine*. **Feb 2023**. DOI: https://doi.org/10.3389/fmed.2023.1090737 (jaeger2023objectiveresponseto pages 1-2)
- Devitt B et al. *Pigment Cell & Melanoma Research*. **Aug 2011**. DOI: https://doi.org/10.1111/j.1755-148X.2011.00873.x (devitt2011clinicaloutcomeand pages 1-3)
- Haugh AM et al. *Cancers*. **Jan 2024**. DOI: https://doi.org/10.3390/cancers16071347 (haugh2024targeteddnasequencing pages 1-2)
- Murphy BM et al. *Nature Communications*. **Jun 2022**. DOI: https://doi.org/10.1038/s41467-022-30881-9 (murphy2022enhancedbrafengagement pages 1-2)
- Burd CE et al. *Cancer Discovery*. **Dec 2014**. DOI: https://doi.org/10.1158/2159-8290.CD-14-0729 (burd2014mutationspecificrasoncogenicity pages 1-3)
- Diener J et al. *Nature Communications*. **Aug 2021**. DOI: https://doi.org/10.1038/s41467-021-25326-8 (johanna2021epigeneticcontrolof pages 1-2)
- Yang J et al. *Molecular Cancer*. **Jun 2023**. DOI: https://doi.org/10.1186/s12943-023-01789-9 (yang2023cxcr2expressionduring pages 1-2)
- Queirolo P, Spagnolo F. *Expert Review of Anticancer Therapy*. **Sep 2017**. DOI: https://doi.org/10.1080/14737140.2017.1374177 (queirolo2017binimetinibforthe pages 9-11)


References

1. (phadke2023targetingnrasmutationsinadvanced pages 1-2): Manali S. Phadke and Keiran S.M. Smalley. Targeting<i>nras</i>mutations in advanced melanoma. Journal of Clinical Oncology, 41:2661-2664, May 2023. URL: https://doi.org/10.1200/jco.23.00205, doi:10.1200/jco.23.00205. This article has 17 citations and is from a highest quality peer-reviewed journal.

2. (braud2023initialevidencefor pages 1-3): Filippo de Braud, Christophe Dooms, Rebecca S. Heist, Celeste Lebbe, Martin Wermke, Anas Gazzah, Dirk Schadendorf, Piotr Rutkowski, Jürgen Wolf, Paolo A. Ascierto, Ignacio Gil-Bazo, Shumei Kato, Maria Wolodarski, Meredith McKean, Eva Muñoz Couselo, Martin Sebastian, Armando Santoro, Vesselina Cooke, Luca Manganelli, Kitty Wan, Anil Gaur, Jaeyeon Kim, Giordano Caponigro, Xuân-Mai Couillebault, Helen Evans, Catarina D. Campbell, Sumit Basu, Michele Moschetta, and Adil Daud. Initial evidence for the efficacy of naporafenib in combination with trametinib in <i>nras</i>-mutant melanoma: results from the expansion arm of a phase ib, open-label study. Journal of Clinical Oncology, 41:2651-2660, May 2023. URL: https://doi.org/10.1200/jco.22.02018, doi:10.1200/jco.22.02018. This article has 57 citations and is from a highest quality peer-reviewed journal.

3. (zhao2021novelinsightsinto pages 3-4): Jeffrey Zhao, Carlos Galvez, Kathryn Eby Beckermann, Douglas B. Johnson, and Jeffrey A Sosman. Novel insights into the pathogenesis and treatment of nras mutant melanoma. Expert Review of Precision Medicine and Drug Development, 6:281-294, Jul 2021. URL: https://doi.org/10.1080/23808993.2021.1938545, doi:10.1080/23808993.2021.1938545. This article has 16 citations.

4. (haugh2024targeteddnasequencing pages 1-2): Alexandra M. Haugh, Robert C. Osorio, Rony A. Francois, Michael E. Tawil, Katy K. Tsai, Michael Tetzlaff, Adil Daud, and Harish N. Vasudevan. Targeted dna sequencing of cutaneous melanoma identifies prognostic and predictive alterations. Cancers, Jan 2024. URL: https://doi.org/10.3390/cancers16071347, doi:10.3390/cancers16071347. This article has 11 citations.

5. (murphy2022enhancedbrafengagement pages 1-2): Brandon M. Murphy, Elizabeth M. Terrell, Venkat R. Chirasani, Tirzah J. Weiss, Rachel E. Lew, Andrea M. Holderbaum, Aastha Dhakal, Valentina Posada, Marie Fort, Michael S. Bodnar, Leiah M. Carey, Min Chen, Craig J. Burd, Vincenzo Coppola, Deborah K. Morrison, Sharon L. Campbell, and Christin E. Burd. Enhanced braf engagement by nras mutants capable of promoting melanoma initiation. Nature Communications, Jun 2022. URL: https://doi.org/10.1038/s41467-022-30881-9, doi:10.1038/s41467-022-30881-9. This article has 53 citations and is from a highest quality peer-reviewed journal.

6. (jaeger2023objectiveresponseto pages 1-2): Zachary J. Jaeger, Neel S. Raval, Natalia K. A. Maverakis, David Y. Chen, George Ansstas, Angela Hardi, and Lynn A. Cornelius. Objective response to immune checkpoint inhibitor therapy in nras-mutant melanoma: a systematic review and meta-analysis. Frontiers in Medicine, Feb 2023. URL: https://doi.org/10.3389/fmed.2023.1090737, doi:10.3389/fmed.2023.1090737. This article has 20 citations.

7. (devitt2011clinicaloutcomeand pages 1-3): Bianca Devitt, Wendy Liu, Renato Salemi, Rory Wolfe, John Kelly, Chin‐Yuan Tzen, Alexander Dobrovic, and Grant McArthur. Clinical outcome and pathological features associated with nras mutation in cutaneous melanoma. Pigment Cell & Melanoma Research, 24:666-672, Aug 2011. URL: https://doi.org/10.1111/j.1755-148x.2011.00873.x, doi:10.1111/j.1755-148x.2011.00873.x. This article has 321 citations and is from a domain leading peer-reviewed journal.

8. (queirolo2017binimetinibforthe pages 9-11): Paola Queirolo and Francesco Spagnolo. Binimetinib for the treatment of nras-mutant melanoma. Expert Review of Anticancer Therapy, 17:985-990, Sep 2017. URL: https://doi.org/10.1080/14737140.2017.1374177, doi:10.1080/14737140.2017.1374177. This article has 30 citations and is from a peer-reviewed journal.

9. (burd2014mutationspecificrasoncogenicity pages 1-3): Christin E. Burd, Wenjin Liu, Minh V. Huynh, Meriam A. Waqas, James E. Gillahan, Kelly S. Clark, Kailing Fu, Brit L. Martin, William R. Jeck, George P. Souroullas, David B. Darr, Daniel C. Zedek, Michael J. Miley, Bruce C. Baguley, Sharon L. Campbell, and Norman E. Sharpless. Mutation-specific ras oncogenicity explains nras codon 61 selection in melanoma. Cancer discovery, 4 12:1418-29, Dec 2014. URL: https://doi.org/10.1158/2159-8290.cd-14-0729, doi:10.1158/2159-8290.cd-14-0729. This article has 262 citations and is from a highest quality peer-reviewed journal.

10. (johanna2021epigeneticcontrolof pages 1-2): Johanna Diener, Arianna Baggiolini, Mattias Pernebrink, Damian Dalcher, Luigi Lerra, Phil F Cheng, Sandra Varum, Jessica Häusel, Salome Stierli, Mathias Treier, Lorenz Studer, Konrad Basler, Mitchell P Levesque, Reinhard Dummer, Raffaella Santoro, Claudio Cantù, and Lukas Sommer. Epigenetic control of melanoma cell invasiveness by the stem cell factor sall4. Nature Communications, Aug 2021. URL: https://doi.org/10.1038/s41467-021-25326-8, doi:10.1038/s41467-021-25326-8. This article has 37 citations and is from a highest quality peer-reviewed journal.

11. (yang2023cxcr2expressionduring pages 1-2): J. Yang, K. Bergdorf, C. Yan, W. Luo, S. C. Chen, G.D. Ayers, Q. Liu, X. Liu, M. Boothby, V.L. Weiss, S. M. Groves, A. N. Oleskie, X. Zhang, D. Y. Maeda, J. A. Zebala, V. Quaranta, and A. Richmond. Cxcr2 expression during melanoma tumorigenesis controls transcriptional programs that facilitate tumor growth. Molecular Cancer, Jun 2023. URL: https://doi.org/10.1186/s12943-023-01789-9, doi:10.1186/s12943-023-01789-9. This article has 19 citations and is from a highest quality peer-reviewed journal.

12. (queirolo2017binimetinibforthe pages 6-9): Paola Queirolo and Francesco Spagnolo. Binimetinib for the treatment of nras-mutant melanoma. Expert Review of Anticancer Therapy, 17:985-990, Sep 2017. URL: https://doi.org/10.1080/14737140.2017.1374177, doi:10.1080/14737140.2017.1374177. This article has 30 citations and is from a peer-reviewed journal.
