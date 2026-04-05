---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-04T16:13:46.135096'
end_time: '2026-04-04T16:23:52.600176'
duration_seconds: 606.47
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Scabies
  mondo_id: ''
  category: Infectious Disease
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 47
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Scabies
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Scabies** covering all of the
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
- **Disease Name:** Scabies
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Scabies** covering all of the
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


# Scabies — Comprehensive Disease Characteristics Report (2023–2024 prioritized)

## Target disease
- **Disease name:** Scabies
- **Category:** Infectious disease (ectoparasitic infestation)
- **Causal agent:** *Sarcoptes scabiei* var. *hominis* (mite) (mitchell2024scabiescurrentknowledge pages 1-2, schneider2023prevalenceofscabies pages 1-2)
- **MONDO ID:** Not retrieved from the tool-accessible literature set in this run (gap).

---

## 1. Disease information

### Concise overview (current understanding)
Scabies is a parasitic skin disease caused by infestation with the mite *Sarcoptes scabiei* var. *hominis*, characterized clinically by pruritus and typical lesion distributions, and it can lead to secondary bacterial skin infections such as impetigo. (mitchell2024scabiescurrentknowledge pages 1-2, li2024thedisabilityadjustedlife pages 1-2)

**WHO/NTD status:** Scabies was added to the WHO neglected tropical diseases (NTD) portfolio in 2017, and it is included in NTD control discussions and targets toward 2030. (mitchell2024scabiescurrentknowledge pages 1-2, sharaf2024scabiesvaccineswhere pages 1-2)

### Key identifiers (ontology / coding)
- **IACS (International Alliance for the Control of Scabies) diagnostic framework:** Three diagnostic certainty levels are widely referenced: confirmed, clinical, suspected. (engelman2021aframeworkfor pages 2-4, li2024thedisabilityadjustedlife pages 1-2)
- **ICD / MeSH / MONDO:** Not reliably extractable from the retrieved evidence set in this run; should be populated from ICD/MeSH/MONDO registries directly (gap).

### Common synonyms / alternative names
- **Crusted scabies** is also described as **Norwegian scabies** in clinical and guideline literature. (simonart2024escalatingthreatof pages 1-5)

### Evidence source type
Most content here is derived from **aggregated disease-level resources** (systematic reviews, WHO/NTD frameworks, GBD analyses, guidelines) rather than individual EHR-only sources. (li2024thedisabilityadjustedlife pages 1-2, engelman2021aframeworkfor pages 2-4, mitchell2024scabiescurrentknowledge pages 1-2)

---

## 2. Etiology

### Primary cause
Infestation by *Sarcoptes scabiei* var. *hominis*; gravid females burrow in the stratum corneum and lay eggs; clinical manifestations are driven largely by host inflammatory/hypersensitivity responses. (mitchell2024scabiescurrentknowledge pages 1-2, engelman2021aframeworkfor pages 2-4, sharaf2024scabiesimmunopathogenesisand pages 4-6)

### Transmission (infectious / environmental)
**Direct skin-to-skin contact** is the primary route; indirect transmission via contaminated items is possible but less prominent. (li2024thedisabilityadjustedlife pages 1-2, mitchell2024scabiescurrentknowledge pages 1-2)

**Timing:** Symptom onset can be delayed in first infestation (up to 4–8 weeks), and more rapid (days) with prior exposure. (mitchell2024scabiescurrentknowledge pages 1-2)

### Risk factors (recent and authoritative)
Consistent risk factors across recent reviews and epidemiologic studies include:
- **Overcrowding / communal living** (e.g., schools, prisons, aged care facilities, refugee camps) (mitchell2024scabiescurrentknowledge pages 1-2, li2024thedisabilityadjustedlife pages 1-2)
- **Poverty / low socioeconomic status and limited access to clean water** (li2024thedisabilityadjustedlife pages 1-2, dejen2024assessmentofscabies pages 1-2)
- **Immunosuppression** (increases risk of crusted scabies and major transmission) (mitchell2024scabiescurrentknowledge pages 1-2, simonart2024escalatingthreatof pages 1-5)

**Quantified risk factor evidence (example; community study):** In southern Ethiopia (Sept–Nov 2023 survey), scabies odds were higher with low/middle wealth index, overcrowding index >1.5, unimproved water source, washing hands with water only, and sleeping on the floor. (dejen2024assessmentofscabies pages 1-2)

### Protective factors (emerging)
A case-control study in southwest Ethiopia reported higher daily household water consumption (≥25 L per person/day) as strongly protective (AOR 0.06). (dejen2024assessmentofscabies pages 2-4)

### Genetic risk/protective factors & gene–environment interaction
Scabies is not primarily a Mendelian genetic disease; however, **host immune genetic variation** may influence susceptibility. A 2024 study of 154 patients (Iraq; 2022–2023) reported cytokine polymorphism associations including **IL-10 GA genotype protective (OR 0.61)** and **IL-13 TT genotype associated with susceptibility (OR 2.14)**. (sharaf2024scabiesimmunopathogenesisand pages 2-4)

Interpretation: these findings suggest a **gene–environment interaction** where exposure (crowding/contact) intersects with host immune regulation (Th2/anti-inflammatory cytokine pathways) to shape risk and/or severity, but replication across populations is needed. (sharaf2024scabiesimmunopathogenesisand pages 2-4, sharaf2024scabiesimmunopathogenesisand pages 4-6)

---

## 3. Phenotypes

### Core phenotypes (symptoms/signs) and suggested HPO terms
Below are common scabies phenotypes with ontology suggestions; frequencies vary by setting.

1) **Pruritus (often worse at night)**
- **Type:** Symptom
- **Characteristics:** often severe; may cause insomnia and impaired QoL; particularly prominent in ordinary scabies (li2024thedisabilityadjustedlife pages 1-2, dejen2024assessmentofscabies pages 1-2)
- **HPO:** *Pruritus* (HP:0000989); *Insomnia* (HP:0100785)

2) **Papules / vesicles / pustules in characteristic sites (interdigital spaces, wrists, elbows, etc.)**
- **Type:** Clinical signs
- **Characteristic distribution:** interdigital spaces, flexor wrists, elbows reported as frequent sites in a 2023 community survey (dejen2024assessmentofscabies pages 1-2)
- **HPO:** *Papule* (HP:0200033), *Vesicle* (HP:0200042), *Pustule* (HP:0000967)

3) **Burrows**
- **Type:** Physical manifestation
- **Role:** key diagnostic clue used in simplified mapping/exam approaches (mitchell2024scabiescurrentknowledge pages 5-6)
- **HPO:** *Skin burrow* (not always represented as a single HPO term; map to scabies-specific phenotype extensions if needed)

4) **Crusted (Norwegian) scabies**
- **Type:** Severe clinical subtype
- **Characteristics:** hyperkeratotic/crusted lesions, very high mite burden; may be less itchy; major outbreak risk; associated with immunosuppression or debility (simonart2024escalatingthreatof pages 1-5)
- **HPO:** *Hyperkeratosis* (HP:0000962), *Palmoplantar keratoderma* (HP:0000982) (clinical examples supported by crusted scabies descriptions and histopathology) (sharaf2024scabiesimmunopathogenesisand media 34ad7ec0)

### Severity and quality-of-life (QoL) impact
A community-based study in north-western Ethiopia (2024; 86 adults with scabies) found mean DLQI **9.2 (SD 7.6)** (moderate impairment). **54.7%** had moderate/severe QoL impact and **27%** reported extremely severe impact; the most affected domains were “symptoms and feelings” and “daily activity”. (yirgu2024qualityoflife pages 1-2, yirgu2024qualityoflife pages 5-7)

---

## 4. Genetic / molecular information

### Causal genes
Not applicable in the Mendelian sense: scabies is caused by a parasite rather than an inherited human gene defect. (mitchell2024scabiescurrentknowledge pages 1-2)

### Parasite molecular mechanisms relevant to drug response (key recent development)
**Permethrin tolerance/resistance via target-site mutation:** Riebenbauer et al. (JEADV; **July 2023**; https://doi.org/10.1111/jdv.19288) reported a **VGSC/VSSC “kdr-type” mutation M918L** in *S. scabiei* var. *hominis*, detected in **97.0% (65/67)** mites sampled from 64 patients in their dataset; the paper states the mutation “is associated with resistance of the kdr type”. (riebenbauer2023detectionofa pages 3-4, riebenbauer2023detectionofa pages 6-7)

Implication: This supports a plausible genetic basis for declining permethrin effectiveness in at least some settings and motivates resistance surveillance. (riebenbauer2023detectionofa pages 1-2)

---

## 5. Environmental information

### Environmental/lifestyle contributors
Crowded living conditions and limited access to water/hygiene resources repeatedly emerge as key determinants (global review + local surveys). (mitchell2024scabiescurrentknowledge pages 1-2, dejen2024assessmentofscabies pages 1-2)

### Infectious agents and co-infections
Scabies is itself an infestation; a major downstream effect is predisposition to bacterial SSTIs. Scabies-associated skin barrier disruption and immune modulation can increase risk of impetigo and other pyoderma; mites and burrows may harbor bacteria including *Staphylococcus aureus* and group A streptococci. (sharaf2024scabiesimmunopathogenesisand pages 7-8)

---

## 6. Mechanism / pathophysiology

### High-level causal chain (current understanding)
1) **Mite infestation and burrowing** in the **stratum corneum** → deposition of mite products/antigens. (mitchell2024scabiescurrentknowledge pages 1-2, sharaf2024scabiesimmunopathogenesisand pages 4-6)
2) **Innate immune activation** in epidermis (keratinocytes, dendritic cells/Langerhans cells) and antigen presentation to lymph nodes → adaptive responses. (sharaf2024scabiesimmunopathogenesisand pages 2-4)
3) **Inflammatory infiltrates** (eosinophils, mast cells, basophils, macrophages, neutrophils) and cytokine production → **pruritus and dermatitis**. (sharaf2024scabiesimmunopathogenesisand pages 2-4, sharaf2024scabiesimmunopathogenesisand pages 7-8)
4) **Excoriation + barrier injury + mite-mediated complement/immune modulation** → secondary bacterial infection risk and systemic sequelae in some contexts. (sharaf2024scabiesimmunopathogenesisand pages 6-7, sharaf2024scabiesimmunopathogenesisand pages 7-8)

### Ordinary vs crusted scabies: immune polarization
Sharaf (Parasitology Research; **March 2024**; https://doi.org/10.1007/s00436-024-08173-6) synthesizes evidence that:
- **Ordinary scabies** is associated with **Th1-type responses** (IFN-γ, TNF-α, IL-2). (sharaf2024scabiesimmunopathogenesisand pages 4-6)
- **Crusted scabies** is associated with **Th2-skewed** cytokines (IL-4, IL-5, IL-13; also IL-31) and dysregulated cellular immunity; Th17 axis involvement is also implicated, particularly when IL-10 is reduced and Treg/Th17 balance is disrupted. (sharaf2024scabiesimmunopathogenesisand pages 4-6, sharaf2024scabiesimmunopathogenesisand pages 6-7)

Mite immune evasion mechanisms described include complement inhibition (serine protease inhibitors blocking complement pathways) and induction of anti-inflammatory mediators such as IL-10 and IL-1 receptor antagonist. (sharaf2024scabiesimmunopathogenesisand pages 6-7, sharaf2024scabiesvaccineswhere pages 1-2)

### Suggested ontology terms
- **GO biological process (examples):** *inflammatory response*; *T cell activation*; *type I hypersensitivity*; *complement activation*; *keratinocyte proliferation* (supported by described cytokines/immune infiltrates and crusted scabies hyperkeratosis) (sharaf2024scabiesimmunopathogenesisand pages 4-6, sharaf2024scabiesimmunopathogenesisand pages 7-8)
- **Cell Ontology (CL) (examples):** *keratinocyte*; *Langerhans cell*; *dendritic cell*; *CD4-positive, αβ T cell*; *CD8-positive T cell*; *eosinophil*; *mast cell*; *neutrophil* (sharaf2024scabiesimmunopathogenesisand pages 2-4, sharaf2024scabiesimmunopathogenesisand pages 4-6)

### Visual evidence (figure/table)
- A schematic summarizing immunopathogenesis and mite/host interactions (Sharaf 2024, Figure 3) is available (sharaf2024scabiesimmunopathogenesisand media 29abd1ed).
- Histopathology showing crusted scabies with heavy mite infestation and hyperkeratosis (Sharaf 2024, Figure 2) is available (sharaf2024scabiesimmunopathogenesisand media 34ad7ec0).

---

## 7. Anatomical structures affected

### Primary structures
- **Skin** (epidermis/stratum corneum) is the primary site of mite burrowing and immune response. (mitchell2024scabiescurrentknowledge pages 1-2, sharaf2024scabiesimmunopathogenesisand pages 4-6)

### Tissue/cell level
- Epidermal keratinocytes and antigen-presenting cells (dendritic/Langerhans) initiate and shape immune responses; dermis shows mixed inflammatory infiltrates. (sharaf2024scabiesimmunopathogenesisand pages 2-4, sharaf2024scabiesimmunopathogenesisand pages 7-8)

### UBERON suggestions
- *Skin* (UBERON:0002097)
- *Epidermis* (UBERON:0001003)
- *Stratum corneum* (UBERON:0002068)

---

## 8. Temporal development

- **Onset pattern:** delayed after first infestation (weeks) but rapid with reinfestation (days). (mitchell2024scabiescurrentknowledge pages 1-2)
- **Course:** can be persistent without treatment; crusted scabies may progress with massive mite burden and prolonged undiagnosed periods, increasing outbreak risk. (simonart2024escalatingthreatof pages 1-5)

---

## 9. Inheritance and population

### Global epidemiology (recent statistics)
A systematic analysis of scabies burden using **GBD 2021** data (PLOS NTD; **Dec 2024**; https://doi.org/10.1371/journal.pntd.0012775) estimated that in **2021** scabies caused:
- **5.3 million DALYs**
- **206.6 million prevalent cases**
- **622.5 million incident cases**
with burden concentrated in tropical regions and particularly affecting children and young people. (li2024thedisabilityadjustedlife pages 1-2)

### Prevalence range in population-based surveys
A 2023 systematic review (JEADV; **May 2023**; https://doi.org/10.1111/jdv.19167) included 43 population-based studies and reported very wide prevalence variation, including **71.0%** in five Ghanaian communities and **76.9%** in an Indonesian boarding school (children-only study), with a low of **0.18%** in Uganda. (schneider2023prevalenceofscabies pages 1-2)

### High-risk settings
Congregate settings (schools, prisons, aged-care facilities, refugee camps) and overcrowded housing are repeatedly cited as high-risk contexts. (mitchell2024scabiescurrentknowledge pages 1-2)

---

## 10. Diagnostics

### Clinical criteria / standardized case definitions
- The **2020 IACS criteria** provide standardized diagnostic certainty strata (confirmed/clinical/suspected) and are recommended as a standard for surveys and programs. (engelman2021aframeworkfor pages 2-4, cox2021estimatingtheglobal pages 5-9)
- A community study in Ethiopia explicitly applied **IACS diagnostic criteria** for prevalence estimation and risk-factor analysis. (dejen2024assessmentofscabies pages 1-2)

### Confirmatory tests
- **Microscopy of skin scrapings** remains a reference standard for confirmation by identifying mites/eggs/feces, but may be impractical and have limited sensitivity in field use. (cox2021estimatingtheglobal pages 5-9, engelman2021aframeworkfor pages 2-4)

### Newer/advanced diagnostic approaches (recent synthesis)
A 2024 systematic review (preprint) summarizes increased use of **noninvasive imaging** (dermoscopy, video dermoscopy, reflectance confocal microscopy, optical coherence tomography) and **PCR assays for mite DNA** as diagnostic advances. (kumari2024titleimpactof pages 28-32, kumari2024titleimpactof pages 1-4)

### Differential diagnosis (high-level)
Differential diagnosis often includes other pruritic dermatoses (e.g., eczema/dermatitis) and other infestations; standardized criteria and confirmatory testing help reduce misclassification. (cox2021estimatingtheglobal pages 5-9)

### LOINC/SNOMED-style test mapping (suggestions)
Not directly retrievable from the provided evidence set; suggested mapping targets include “skin scraping microscopy for mite/egg/scybala” and “PCR for *Sarcoptes scabiei* DNA,” to be aligned with local laboratory coding systems. (cox2021estimatingtheglobal pages 5-9, kumari2024titleimpactof pages 28-32)

---

## 11. Outcome / prognosis

### Complications and morbidity
- Scabies can predispose to **impetigo and other SSTIs**, with downstream severe outcomes in some settings (including cellulitis, lymphangitis, acute glomerulonephritis; rarely death), especially in crusted scabies with fissures and heavy infestation. (sharaf2024scabiesimmunopathogenesisand pages 7-8, simonart2024escalatingthreatof pages 1-5)

### Quality of life (recent data)
As above (DLQI study; 2024 Ethiopia): mean DLQI 9.2; 27% extremely severe QoL impact. (yirgu2024qualityoflife pages 1-2, yirgu2024qualityoflife pages 5-7)

### Health-system economic burden (real-world implementation)
Fiji national extrapolation from Big SHIFT surveillance (PLOS Global Public Health; **Oct 2024**; https://doi.org/10.1371/journal.pgph.0003706) estimated:
- **US$3.0 million annual direct healthcare costs** attributable to scabies and related SSTIs (~**US$3.3 per capita**)
- **US$17.7** average cost per primary healthcare presentation for scabies
- **US$439** average cost per hospital admission for potentially scabies-related SSTI (akpan2024costsofprimary pages 1-2)

---

## 12. Treatment

### Standard pharmacotherapy and regimens (current practice)
A 2024 review summarizing current practice describes:
- **Topical permethrin 5%**: whole-body application for 8–12 hours; often repeated after 7–14 days. (mitchell2024scabiescurrentknowledge pages 5-6)
- **Oral ivermectin**: active against mites but not eggs; short half-life necessitating repeat dosing 7–14 days apart; generally avoided in pregnancy and children <15 kg in many guidelines. (mitchell2024scabiescurrentknowledge pages 5-6)
- **Benzyl benzoate**: topical alternative used in some programs/guidelines. (mitchell2024scabiescurrentknowledge pages 5-6)

**Comparative effectiveness:** A 2018 Cochrane review is summarized as finding no difference between permethrin and ivermectin in efficacy. (mitchell2024scabiescurrentknowledge pages 5-6)

### Mass drug administration (MDA) as a public-health control strategy
Evidence syntheses emphasize MDA as effective in highly endemic settings.
- A 2024 scabies control review describes strong evidence including a Fiji trial with **94% reduction** (32% to <2%) at 12 months and a meta-analysis with relative reductions **79% for scabies** and **66% for impetigo**. (mitchell2024scabiescurrentknowledge pages 6-7)
- A scabies control framework recommends piloting MDA at **community prevalence ≥10%**, with suggested stopping threshold **<2%** and a commonly used regimen **two doses ivermectin 200 μg/kg 7–14 days apart** (and topical alternatives for ineligible groups). (engelman2021aframeworkfor pages 4-5)

### Drug resistance (major 2023–2024 development)
- **Molecular evidence:** kdr-type VGSC mutation M918L associated with permethrin tolerance in human scabies mites (2023). (riebenbauer2023detectionofa pages 6-7, riebenbauer2023detectionofa pages 3-4)
- **Programmatic implication:** the need for resistance monitoring and potential alternative strategies, including combination regimens and investigation of new oral agents. (mitchell2024scabiescurrentknowledge pages 6-7)

### Emerging therapeutics / future directions
**Moxidectin** is highlighted as a promising oral alternative with longer half-life and potential for single-dose treatment, relevant to improving MDA feasibility and adherence. (mitchell2024scabiescurrentknowledge pages 6-7)

### Treatment ontology suggestions (MAXO)
- **Topical antiparasitic therapy** (permethrin application)
- **Systemic antiparasitic therapy** (oral ivermectin)
- **Mass drug administration** (community-wide ivermectin-based MDA)
- **Contact tracing and treatment of close contacts**
(these are conceptual MAXO mappings; exact IDs should be selected from MAXO catalog during curation). (mitchell2024scabiescurrentknowledge pages 5-6, engelman2021aframeworkfor pages 4-5)

### Clinical trials (real-world pipeline; selected)
- **NCT04332068** (University of Oxford; Phase 2; started 2023-11-18; completed 2025-04-04): oral ivermectin vs permethrin in children 5 to <15 kg (includes dose escalation up to 800 μg/kg at some sites); primary outcome adverse events; includes population PK and WGS pharmacogenomics. (NCT04332068 chunk 1, NCT04332068 chunk 2)
- **NCT05819983** (Universitas Padjadjaran; Phase 4; completed 2023): compares 3-dose ivermectin vs 2-dose ivermectin vs permethrin 5% (days 1 and 8) in ≥6 years/≥15 kg; outcomes include lesion severity and pruritus (5 weeks); no results posted in the record excerpt. (NCT05819983 chunk 1)
- **NCT07145736** (Kirby Institute; recruiting; Angola; includes scabies among conditions): moxidectin vs ivermectin for MDA in onchocerciasis/other NTDs; operational eligibility information provided; no results posted. (NCT07145736 chunk 2)

---

## 13. Prevention

### Individual and household prevention
Key prevention principles include rapid case identification and **simultaneous treatment of close/household contacts**, plus environmental measures (laundering/drying linens/clothes) that may help but have limited evidence. (mitchell2024scabiescurrentknowledge pages 5-6, mitchell2024scabiescurrentknowledge pages 6-7)

### Community-level prevention (MDA thresholds)
WHO-aligned frameworks recommend:
- individual/household management for prevalence **<10%**
- community-wide MDA where prevalence is **≥10%** (mitchell2024scabiescurrentknowledge pages 6-7, engelman2021aframeworkfor pages 4-5)

### Cost-effectiveness threshold evidence (2024)
A decision-analytic model for Ethiopia (Frontiers in Health Services; **Sep 2024**; https://doi.org/10.3389/frhs.2024.1279762) found ivermectin-based MDA to be cost-effective in a base case (population 100,000; prevalence 15%) and suggested initiating MDA at prevalence **>10%**; MDA was not cost-effective below 10% prevalence or when effectiveness <85%. (hounsome2024costeffectivenessofmass pages 1-2)

---

## 14. Other species / natural disease
Scabies-like infestation occurs in many mammals ("sarcoptic mange"), but cross-species taxonomy, zoonotic potential, and OMIA/NCBI taxon details were not retrievable from the current evidence set and should be populated from veterinary/parasitology resources (gap).

---

## 15. Model organisms
Porcine models are used for mechanistic studies and transcriptomics; a 2023 commentary summarizes that transcriptomic analyses support Th2 signatures in both ordinary and crusted scabies and increased IL-17 pathway magnitude in crusted disease, with time-dependent immune activation patterns. (mounsey2023commentarytranscriptomeanalysis pages 2-3)

---

## Expert opinions / analysis (authoritative synthesis)
Recent authoritative syntheses converge on several expert-level conclusions:
1) **Standardized diagnosis is essential** for burden estimation and control planning; IACS criteria address longstanding inconsistencies and enable mapping strategies. (cox2021estimatingtheglobal pages 5-9, engelman2021aframeworkfor pages 2-4)
2) **MDA is among the most impactful control tools** for high-prevalence settings, but two-dose ivermectin schedules and contraindicated groups constrain implementation; longer-acting oral agents could be transformative. (mitchell2024scabiescurrentknowledge pages 6-7, engelman2021aframeworkfor pages 4-5)
3) **Resistance surveillance is now a priority**: molecular evidence (VGSC kdr mutation) supports a plausible biologic basis for permethrin tolerance, reinforcing the need for monitoring and diversified treatment approaches. (riebenbauer2023detectionofa pages 6-7, mitchell2024scabiescurrentknowledge pages 6-7)

---

## Abstract-quotable statements (verbatim snippets available from retrieved texts)
- **GBD 2021 (PLOS NTD; Dec 2024):** “In 2021, scabies caused **5.3 million DALYs**, **206.6 million prevalence**, and **622.5 million incidence** …” (as quoted in the evidence extraction). (li2024thedisabilityadjustedlife pages 1-2)
- **Riebenbauer 2023 (JEADV; Jul 2023):** M918L mutation “**is associated with resistance of the kdr type**.” (riebenbauer2023detectionofa pages 6-7)

---

## Limitations / gaps in this run
- **Ontology IDs (MONDO, MeSH, ICD-10/ICD-11)** were not directly retrievable from the tool-accessible literature set and should be supplemented from dedicated ontology registries.
- Some “latest” sources (e.g., certain 2024 BJD meta-analyses and Nature Reviews Disease Primers) were flagged as unobtainable in the search results and therefore could not be cited here.


References

1. (mitchell2024scabiescurrentknowledge pages 1-2): Elke Mitchell, Miranda Wallace, Justine Marshall, Margot Whitfeld, and Lucia Romani. Scabies: current knowledge and future directions. Frontiers in Tropical Diseases, Jul 2024. URL: https://doi.org/10.3389/fitd.2024.1429266, doi:10.3389/fitd.2024.1429266. This article has 17 citations.

2. (schneider2023prevalenceofscabies pages 1-2): S. Schneider, J. Wu, L. Tizek, S. Ziehfreund, and A. Zink. Prevalence of scabies worldwide—an updated systematic literature review in 2022. Journal of the European Academy of Dermatology and Venereology, 37:1749-1757, May 2023. URL: https://doi.org/10.1111/jdv.19167, doi:10.1111/jdv.19167. This article has 80 citations and is from a domain leading peer-reviewed journal.

3. (li2024thedisabilityadjustedlife pages 1-2): Jiajia Li, Zehu Liu, and Xiujiao Xia. The disability-adjusted life years (dalys), prevalence and incidence of scabies, 1990–2021: a systematic analysis from the global burden of disease study 2021. PLOS Neglected Tropical Diseases, 18:e0012775, Dec 2024. URL: https://doi.org/10.1371/journal.pntd.0012775, doi:10.1371/journal.pntd.0012775. This article has 25 citations and is from a domain leading peer-reviewed journal.

4. (sharaf2024scabiesvaccineswhere pages 1-2): Mahmoud Shafeik Sharaf. Scabies vaccines: where we stand and challenges ahead. Parasitology Research, Jul 2024. URL: https://doi.org/10.1007/s00436-024-08298-8, doi:10.1007/s00436-024-08298-8. This article has 8 citations and is from a peer-reviewed journal.

5. (engelman2021aframeworkfor pages 2-4): Daniel Engelman, Michael Marks, Andrew C. Steer, Abate Beshah, Gautam Biswas, Olivier Chosidow, Luc E. Coffeng, Belen Lardizabal Dofitas, Wendemagegn Enbiale, Mosoka Fallah, Elkhan Gasimov, Adrian Hopkins, Julie Jacobson, John M. Kaldor, Fatimata Ly, Charles D. Mackenzie, Jodie McVernon, Matthew Parnaby, Merelesita Rainima-Qaniuci, Oliver Sokana, Dieudonne Sankara, Rie Yotsu, Aya Yajima, and Paul T. Cantey. A framework for scabies control. PLOS Neglected Tropical Diseases, 15:e0009661, Sep 2021. URL: https://doi.org/10.1371/journal.pntd.0009661, doi:10.1371/journal.pntd.0009661. This article has 103 citations and is from a domain leading peer-reviewed journal.

6. (simonart2024escalatingthreatof pages 1-5): Thierry Simonart and Xuân-Lan Lam Hoai. Escalating threat of drug-resistant human scabies: current insights and future directions. Journal of Clinical Medicine, 13:5511, Sep 2024. URL: https://doi.org/10.3390/jcm13185511, doi:10.3390/jcm13185511. This article has 26 citations.

7. (sharaf2024scabiesimmunopathogenesisand pages 4-6): Mahmoud Shafeik Sharaf. Scabies: immunopathogenesis and pathological changes. Parasitology Research, Mar 2024. URL: https://doi.org/10.1007/s00436-024-08173-6, doi:10.1007/s00436-024-08173-6. This article has 42 citations and is from a peer-reviewed journal.

8. (dejen2024assessmentofscabies pages 1-2): Philmon Dejen, Mekonnen Girma, Adane Chernet, Susana Vaz Nery, and Techalew Shimelis. Assessment of scabies and its associated factors in hawassa zuria district, southern ethiopia: a cross-sectional study. PLOS ONE, 19:e0314140, Nov 2024. URL: https://doi.org/10.1371/journal.pone.0314140, doi:10.1371/journal.pone.0314140. This article has 3 citations and is from a peer-reviewed journal.

9. (dejen2024assessmentofscabies pages 2-4): Philmon Dejen, Mekonnen Girma, Adane Chernet, Susana Vaz Nery, and Techalew Shimelis. Assessment of scabies and its associated factors in hawassa zuria district, southern ethiopia: a cross-sectional study. PLOS ONE, 19:e0314140, Nov 2024. URL: https://doi.org/10.1371/journal.pone.0314140, doi:10.1371/journal.pone.0314140. This article has 3 citations and is from a peer-reviewed journal.

10. (sharaf2024scabiesimmunopathogenesisand pages 2-4): Mahmoud Shafeik Sharaf. Scabies: immunopathogenesis and pathological changes. Parasitology Research, Mar 2024. URL: https://doi.org/10.1007/s00436-024-08173-6, doi:10.1007/s00436-024-08173-6. This article has 42 citations and is from a peer-reviewed journal.

11. (mitchell2024scabiescurrentknowledge pages 5-6): Elke Mitchell, Miranda Wallace, Justine Marshall, Margot Whitfeld, and Lucia Romani. Scabies: current knowledge and future directions. Frontiers in Tropical Diseases, Jul 2024. URL: https://doi.org/10.3389/fitd.2024.1429266, doi:10.3389/fitd.2024.1429266. This article has 17 citations.

12. (sharaf2024scabiesimmunopathogenesisand media 34ad7ec0): Mahmoud Shafeik Sharaf. Scabies: immunopathogenesis and pathological changes. Parasitology Research, Mar 2024. URL: https://doi.org/10.1007/s00436-024-08173-6, doi:10.1007/s00436-024-08173-6. This article has 42 citations and is from a peer-reviewed journal.

13. (yirgu2024qualityoflife pages 1-2): Robel Yirgu, Jo Middleton, Jackie A. Cassell, Stephen Bremner, Gail Davey, and Abebaw Fekadu. Quality of life among adults with scabies: a community-based cross-sectional study in north-western ethiopia. PLOS Neglected Tropical Diseases, 18:e0012429, Aug 2024. URL: https://doi.org/10.1371/journal.pntd.0012429, doi:10.1371/journal.pntd.0012429. This article has 11 citations and is from a domain leading peer-reviewed journal.

14. (yirgu2024qualityoflife pages 5-7): Robel Yirgu, Jo Middleton, Jackie A. Cassell, Stephen Bremner, Gail Davey, and Abebaw Fekadu. Quality of life among adults with scabies: a community-based cross-sectional study in north-western ethiopia. PLOS Neglected Tropical Diseases, 18:e0012429, Aug 2024. URL: https://doi.org/10.1371/journal.pntd.0012429, doi:10.1371/journal.pntd.0012429. This article has 11 citations and is from a domain leading peer-reviewed journal.

15. (riebenbauer2023detectionofa pages 3-4): K. Riebenbauer, K. Purkhauser, J. Walochnik, N. Urban, P. Weber, T. Stamm, A. Handisurya, and P. Weber. Detection of a knockdown mutation in the voltage‐sensitive sodium channel associated with permethrin tolerance in <i>sarcoptes scabiei</i> var. <i>hominis</i> mites. Journal of the European Academy of Dermatology and Venereology, 37:2355-2361, Jul 2023. URL: https://doi.org/10.1111/jdv.19288, doi:10.1111/jdv.19288. This article has 24 citations and is from a domain leading peer-reviewed journal.

16. (riebenbauer2023detectionofa pages 6-7): K. Riebenbauer, K. Purkhauser, J. Walochnik, N. Urban, P. Weber, T. Stamm, A. Handisurya, and P. Weber. Detection of a knockdown mutation in the voltage‐sensitive sodium channel associated with permethrin tolerance in <i>sarcoptes scabiei</i> var. <i>hominis</i> mites. Journal of the European Academy of Dermatology and Venereology, 37:2355-2361, Jul 2023. URL: https://doi.org/10.1111/jdv.19288, doi:10.1111/jdv.19288. This article has 24 citations and is from a domain leading peer-reviewed journal.

17. (riebenbauer2023detectionofa pages 1-2): K. Riebenbauer, K. Purkhauser, J. Walochnik, N. Urban, P. Weber, T. Stamm, A. Handisurya, and P. Weber. Detection of a knockdown mutation in the voltage‐sensitive sodium channel associated with permethrin tolerance in <i>sarcoptes scabiei</i> var. <i>hominis</i> mites. Journal of the European Academy of Dermatology and Venereology, 37:2355-2361, Jul 2023. URL: https://doi.org/10.1111/jdv.19288, doi:10.1111/jdv.19288. This article has 24 citations and is from a domain leading peer-reviewed journal.

18. (sharaf2024scabiesimmunopathogenesisand pages 7-8): Mahmoud Shafeik Sharaf. Scabies: immunopathogenesis and pathological changes. Parasitology Research, Mar 2024. URL: https://doi.org/10.1007/s00436-024-08173-6, doi:10.1007/s00436-024-08173-6. This article has 42 citations and is from a peer-reviewed journal.

19. (sharaf2024scabiesimmunopathogenesisand pages 6-7): Mahmoud Shafeik Sharaf. Scabies: immunopathogenesis and pathological changes. Parasitology Research, Mar 2024. URL: https://doi.org/10.1007/s00436-024-08173-6, doi:10.1007/s00436-024-08173-6. This article has 42 citations and is from a peer-reviewed journal.

20. (sharaf2024scabiesimmunopathogenesisand media 29abd1ed): Mahmoud Shafeik Sharaf. Scabies: immunopathogenesis and pathological changes. Parasitology Research, Mar 2024. URL: https://doi.org/10.1007/s00436-024-08173-6, doi:10.1007/s00436-024-08173-6. This article has 42 citations and is from a peer-reviewed journal.

21. (cox2021estimatingtheglobal pages 5-9): V. Cox, L. C. Fuller, Daniel Engelman, A. Steer, and Roderick J Hay. Estimating the global burden of scabies: what else do we need?*. British Journal of Dermatology, 184:237-242, Jul 2021. URL: https://doi.org/10.1111/bjd.19170, doi:10.1111/bjd.19170. This article has 71 citations and is from a highest quality peer-reviewed journal.

22. (kumari2024titleimpactof pages 28-32): Sakshi Kumari, Swathi Srinivas, Zainab Siddiqua, Muhammad Saeed Qazi, Mahin Sheikh, Shree Rath, Maham Khan, Muhammad Daim Jawaid, Nayanika Tummala, and Madho Mal. Title: impact of scabies on quality of life and recent advances in management: a systematic review. MedRxiv, Nov 2024. URL: https://doi.org/10.1101/2024.11.25.24317899, doi:10.1101/2024.11.25.24317899. This article has 2 citations.

23. (kumari2024titleimpactof pages 1-4): Sakshi Kumari, Swathi Srinivas, Zainab Siddiqua, Muhammad Saeed Qazi, Mahin Sheikh, Shree Rath, Maham Khan, Muhammad Daim Jawaid, Nayanika Tummala, and Madho Mal. Title: impact of scabies on quality of life and recent advances in management: a systematic review. MedRxiv, Nov 2024. URL: https://doi.org/10.1101/2024.11.25.24317899, doi:10.1101/2024.11.25.24317899. This article has 2 citations.

24. (akpan2024costsofprimary pages 1-2): Edifofon Akpan, Li Jun Thean, Rabindra Baskota, Jyotishna Mani, Maria Mow, Mike Kama, Meciusela Tuicakau, Joseph Kado, Lucia Romani, John Kaldor, Daniel Engelman, Andrew C. Steer, and Natalie Carvalho. Costs of primary healthcare presentations and hospital admissions for scabies and related skin infections in fiji, 2018–2019. PLOS Global Public Health, 4:e0003706, Oct 2024. URL: https://doi.org/10.1371/journal.pgph.0003706, doi:10.1371/journal.pgph.0003706. This article has 2 citations and is from a peer-reviewed journal.

25. (mitchell2024scabiescurrentknowledge pages 6-7): Elke Mitchell, Miranda Wallace, Justine Marshall, Margot Whitfeld, and Lucia Romani. Scabies: current knowledge and future directions. Frontiers in Tropical Diseases, Jul 2024. URL: https://doi.org/10.3389/fitd.2024.1429266, doi:10.3389/fitd.2024.1429266. This article has 17 citations.

26. (engelman2021aframeworkfor pages 4-5): Daniel Engelman, Michael Marks, Andrew C. Steer, Abate Beshah, Gautam Biswas, Olivier Chosidow, Luc E. Coffeng, Belen Lardizabal Dofitas, Wendemagegn Enbiale, Mosoka Fallah, Elkhan Gasimov, Adrian Hopkins, Julie Jacobson, John M. Kaldor, Fatimata Ly, Charles D. Mackenzie, Jodie McVernon, Matthew Parnaby, Merelesita Rainima-Qaniuci, Oliver Sokana, Dieudonne Sankara, Rie Yotsu, Aya Yajima, and Paul T. Cantey. A framework for scabies control. PLOS Neglected Tropical Diseases, 15:e0009661, Sep 2021. URL: https://doi.org/10.1371/journal.pntd.0009661, doi:10.1371/journal.pntd.0009661. This article has 103 citations and is from a domain leading peer-reviewed journal.

27. (NCT04332068 chunk 1):  Ivermectin Safety in Small Children. University of Oxford. 2023. ClinicalTrials.gov Identifier: NCT04332068

28. (NCT04332068 chunk 2):  Ivermectin Safety in Small Children. University of Oxford. 2023. ClinicalTrials.gov Identifier: NCT04332068

29. (NCT05819983 chunk 1):  Ivermectin/ Permethrin for Scabies. Universitas Padjadjaran. 2023. ClinicalTrials.gov Identifier: NCT05819983

30. (NCT07145736 chunk 2):  Moxidectin Versus Ivermectin as Mass Drug Administration for the Control of Onchocerciasis and Other Neglected Tropical Diseases. Kirby Institute. 2025. ClinicalTrials.gov Identifier: NCT07145736

31. (hounsome2024costeffectivenessofmass pages 1-2): Natalia Hounsome, Robel Yirgu, Jo Middleton, Jackie A. Cassell, Abebaw Fekadu, and Gail Davey. Cost-effectiveness of mass drug administration for control of scabies in ethiopia: a decision-analytic model. Frontiers in Health Services, Sep 2024. URL: https://doi.org/10.3389/frhs.2024.1279762, doi:10.3389/frhs.2024.1279762. This article has 2 citations.

32. (mounsey2023commentarytranscriptomeanalysis pages 2-3): Kate E. Mounsey. Commentary: transcriptome analysis of host inflammatory responses to the ectoparasitic mite sarcoptes scabiei var. hominis. Frontiers in Immunology, Feb 2023. URL: https://doi.org/10.3389/fimmu.2023.1128688, doi:10.3389/fimmu.2023.1128688. This article has 3 citations and is from a peer-reviewed journal.
