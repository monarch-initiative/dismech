---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-06T15:01:27.187809'
end_time: '2026-05-06T15:22:42.876213'
duration_seconds: 1275.7
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Splenic artery aneurysm
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 50
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Splenic artery aneurysm
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Splenic artery aneurysm** covering all of the
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
- **Disease Name:** Splenic artery aneurysm
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Splenic artery aneurysm** covering all of the
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


# Splenic Artery Aneurysm (SAA): Comprehensive Disease Characteristics Research Report

## Executive summary (current understanding)
Splenic artery aneurysm (SAA) is the most common visceral artery aneurysm and is often incidentally detected; despite a generally low rupture rate for true SAAs, rupture can be catastrophic, with particularly high maternal and fetal mortality in pregnancy. Contemporary expert guidance (SVS 2020; CIRSE 2024) recommends CTA-based diagnosis, aggressive management for pseudoaneurysms (treat regardless of size), and size-/risk-stratified treatment for true SAAs (treat ≥3 cm, symptomatic, enlarging, or in women of childbearing age). Endovascular therapy is generally preferred when anatomically feasible and is associated with lower perioperative morbidity and shorter length of stay, while open surgery remains crucial for rupture, hemodynamic instability, pregnancy-associated rupture, and distal/hilar anatomy. (chaer2020thesocietyfor pages 12-13, chaer2020thesocietyfor pages 13-15, rossi2024cirsestandardsof pages 1-3, hogendoorn2014openrepairendovascular pages 4-5, rinaldi2023endovascularandopen pages 1-3)

| Topic | Key points | Quantitative data | Key sources |
|---|---|---|---|
| Disease definition / identifiers / synonyms | Splenic artery aneurysm (SAA) is a dilation of the splenic artery; one review defines SAA as arterial dilation >50% of the normal splenic artery diameter. Distinguish **true SAA** from **splenic artery pseudoaneurysm (SAP/SAPA)**, which has a much higher rupture risk. Common synonyms: splenic artery aneurysm, SAA, true splenic artery aneurysm; pseudoaneurysm terms: splenic artery pseudoaneurysm, SAP. “Giant” SAA is variably defined, most often ≥5 cm, sometimes >10 cm. | Giant SAA definition used in literature: ≥5 cm in 62.5% of articles that specified a cutoff; >10 cm in 37.5%. | Rinaldi et al., *J Clin Med* 2024, DOI: 10.3390/jcm13195793, https://doi.org/10.3390/jcm13195793 (2024) (rinaldi2024thedefinitiondiagnosis pages 1-2, rinaldi2024thedefinitiondiagnosis pages 4-6, rinaldi2024thedefinitiondiagnosis pages 7-9) |
| Epidemiology / frequency | SAA is the most common visceral artery aneurysm. Population estimates vary by detection method; frequency has risen with modern imaging. | SAAs account for ~60% of visceral/splanchnic aneurysms; reported incidence 0.09% at autopsy and 0.78% on angiography; one older clinical paper cites incidence <0.8%. | Rinaldi et al., *J Clin Med* 2024, DOI: 10.3390/jcm13195793, https://doi.org/10.3390/jcm13195793 (2024); Sticco et al., *Vascular* 2016, DOI: 10.1177/1708538115613703, https://doi.org/10.1177/1708538115613703 (2016) (rinaldi2024thedefinitiondiagnosis pages 7-9, sticco2016acomparisonof pages 1-2) |
| Sex / age distribution | Classic SAA is more common in women, especially multiparous women; giant SAA series show more balanced sex distribution. Diagnosis is usually in adulthood/midlife. | Female predominance reported as ~4:1 for common SAA; giant SAA pooled review: 43 males / 39 females, median age 55.79 years. | Obara et al., *Surgery Today* 2020, DOI: 10.1007/s00595-019-01898-3, https://doi.org/10.1007/s00595-019-01898-3 (2020); Rinaldi et al., *J Clin Med* 2024, DOI: 10.3390/jcm13195793, https://doi.org/10.3390/jcm13195793 (2024) (obara2020currentmanagementstrategies pages 5-7, rinaldi2024thedefinitiondiagnosis pages 1-2) |
| Rupture risk and mortality | True SAA rupture risk is generally low but clinically important because rupture can be catastrophic. Pseudoaneurysms rupture much more often and are treated regardless of size. | Common true SAA rupture risk ~2–3%; older review cites ~3% in more recent series (historically ~10%). Pseudoaneurysm rupture risk reported 37–47%; SVS excerpt cites rupture 76.3% for pseudoaneurysm vs 3.1% for true aneurysm. Ruptured SAA mortality up to ~25% overall; older reports cite rupture mortality up to 30% or 36%. | Rinaldi et al., *J Clin Med* 2024, DOI: 10.3390/jcm13195793, https://doi.org/10.3390/jcm13195793 (2024); Chaer et al., *J Vasc Surg* 2020, DOI: 10.1016/j.jvs.2020.01.039, https://doi.org/10.1016/j.jvs.2020.01.039 (2020); Obara et al., *Surgery Today* 2020, DOI: 10.1007/s00595-019-01898-3, https://doi.org/10.1007/s00595-019-01898-3 (2020); Dave et al., *Ann Vasc Surg* 2000, DOI: 10.1007/s100169910039, https://doi.org/10.1007/s100169910039 (2000) (rinaldi2024thedefinitiondiagnosis pages 7-9, chaer2020thesocietyfor pages 12-13, chaer2020thesocietyfor pages 13-15, obara2020currentmanagementstrategies pages 5-7, dave2000splenicarteryaneurysm pages 4-5, sticco2016acomparisonof pages 1-2) |
| Pregnancy-associated risk | Pregnancy markedly increases rupture risk and is a major reason for aggressive treatment in women of childbearing age. Rupture often occurs in late pregnancy. | Pregnancy accounts for ~20–50% of ruptures in older literature/SVS excerpt; maternal mortality ~70–80%; fetal mortality ~90–95%. | Chaer et al., *J Vasc Surg* 2020, DOI: 10.1016/j.jvs.2020.01.039, https://doi.org/10.1016/j.jvs.2020.01.039 (2020); Rinaldi et al., *J Clin Med* 2024, DOI: 10.3390/jcm13195793, https://doi.org/10.3390/jcm13195793 (2024); Dave et al., *Ann Vasc Surg* 2000, DOI: 10.1007/s100169910039, https://doi.org/10.1007/s100169910039 (2000) (chaer2020thesocietyfor pages 12-13, rinaldi2024thedefinitiondiagnosis pages 7-9, dave2000splenicarteryaneurysm pages 4-5) |
| Portal hypertension / liver transplant association | Portal hypertension, cirrhosis, and liver transplantation are recurring associations and influence management because of higher rupture/growth concern. | Older review: portal hypertension present in up to 24% of SAA patients; incidence in cirrhosis/portal hypertension 7–20%; 8–13% of liver-transplant candidates have SAA. Another review cites 20.5% in liver-transplant recipients. | Dave et al., *Ann Vasc Surg* 2000, DOI: 10.1007/s100169910039, https://doi.org/10.1007/s100169910039 (2000); Obara et al., *Surgery Today* 2020, DOI: 10.1007/s00595-019-01898-3, https://doi.org/10.1007/s00595-019-01898-3 (2020) (dave2000splenicarteryaneurysm pages 4-5, obara2020currentmanagementstrategies pages 5-7, pratesi2024guidelinesonthe pages 51-53) |
| Other risk factors / associations | Reported associations include multiparity, pancreatitis/pseudocysts, prior surgery, trauma, infection, and nonatherosclerotic arteriopathies such as segmental arterial mediolysis. Pseudoaneurysms are particularly linked to pancreatitis and local inflammatory/surgical injury. | Giant SAA/SAP review: pancreatitis/pseudocysts present in 15.85% of pooled giant cases; giant pooled symptoms included pain in 59.76% and asymptomatic presentation in 17.07%. | Rinaldi et al., *J Clin Med* 2024, DOI: 10.3390/jcm13195793, https://doi.org/10.3390/jcm13195793 (2024); Rinaldi et al., *J Clin Med* 2023, DOI: 10.3390/jcm12186085, https://doi.org/10.3390/jcm12186085 (2023) (rinaldi2024thedefinitiondiagnosis pages 4-6, rinaldi2024thedefinitiondiagnosis pages 9-10, rinaldi2023endovascularandopen pages 1-3) |
| Clinical presentation | Most SAAs are asymptomatic and incidentally discovered, but symptomatic lesions usually present with abdominal or left upper quadrant/epigastric pain. Rupture can cause shock and hemoperitoneum. | Older review: 80–95% asymptomatic. Giant pooled series: pain 59.76%, palpable mass 28.05%, asymptomatic 17.07%. | Dave et al., *Ann Vasc Surg* 2000, DOI: 10.1007/s100169910039, https://doi.org/10.1007/s100169910039 (2000); Rinaldi et al., *J Clin Med* 2024, DOI: 10.3390/jcm13195793, https://doi.org/10.3390/jcm13195793 (2024) (dave2000splenicarteryaneurysm pages 4-5, rinaldi2024thedefinitiondiagnosis pages 4-6, rinaldi2024thedefinitiondiagnosis pages 9-10) |
| Diagnostic imaging | CTA is the preferred initial diagnostic test in most guidelines; MRA is preferred when iodinated contrast is contraindicated and is favored in pregnancy. Angiography is used when planning intervention or when noninvasive imaging is insufficient. Ultrasound/EcoColorDoppler can be first-line screening, but sensitivity for small SAA is limited. | CT used in 80.49% of giant pooled cases; selective angiography 54.88%; EcoColorDoppler 45.12%; MRI 3.66%. SVS excerpt notes ultrasound has poor sensitivity for SAA <3 cm. | Chaer et al., *J Vasc Surg* 2020, DOI: 10.1016/j.jvs.2020.01.039, https://doi.org/10.1016/j.jvs.2020.01.039 (2020); Rinaldi et al., *J Clin Med* 2024, DOI: 10.3390/jcm13195793, https://doi.org/10.3390/jcm13195793 (2024) (chaer2020thesocietyfor pages 12-13, rinaldi2024thedefinitiondiagnosis pages 9-10, rinaldi2024thedefinitiondiagnosis pages 4-6) |
| SVS 2020 treatment thresholds | Treat ruptured SAAs emergently; treat all splenic artery pseudoaneurysms regardless of size; treat all true SAAs in women of childbearing age regardless of size; treat true SAAs that are symptomatic, enlarging, or ≥3 cm. Observation is reasonable for small, stable, asymptomatic true SAAs in non-childbearing patients or those with limited life expectancy. Endovascular therapy is preferred initially when anatomically feasible; open surgery is favored for rupture, pregnancy-related rupture, or distal/hilar lesions. | Thresholds: pseudoaneurysm any size; true SAA in women of childbearing age any size; true SAA ≥3 cm; interval growth >0.5 cm/year is an indication. Nonoperative series cited by SVS: mean observed size 2.1 cm, mean follow-up 75 months. | Chaer et al., *J Vasc Surg* 2020, DOI: 10.1016/j.jvs.2020.01.039, https://doi.org/10.1016/j.jvs.2020.01.039 (2020) (chaer2020thesocietyfor pages 13-15, chaer2020thesocietyfor pages 12-13) |
| CIRSE 2024 thresholds / surveillance | Intervene for any symptomatic VAA/VAPA; for SAA specifically, treat asymptomatic lesions ≥2 cm, especially if saccular/distal/favorable anatomy; treat any VAA growing ≥0.5 cm/year; treat VAPAs regardless of symptoms; treat any asymptomatic VAA in women of childbearing age. After endovascular therapy, CTA or MRA surveillance is recommended. | Thresholds: SAA ≥2 cm; growth ≥0.5 cm/year. Surveillance after EVT: 3 months, 12 months, then yearly. | Rossi et al., *Cardiovasc Intervent Radiol* 2024, DOI: 10.1007/s00270-023-03620-w, https://doi.org/10.1007/s00270-023-03620-w (2024) (rossi2024cirsestandardsof pages 1-3) |
| Other 2024 guideline / review excerpts | 2024 guidance excerpts broadly support emergency treatment for rupture and symptomatic lesions; observation for stable asymptomatic SAAs <3 cm; intervention for SAAs >3 cm. Some sources advocate treatment at ≥2 cm in pregnant/fertile patients with portal hypertension or those awaiting liver transplant. | Usual cutoffs in 2024 excerpts: observe <3 cm if stable; treat >3 cm electively; lesions <2 cm often observed unless rapid growth. | Pratesi et al. guideline excerpt (2024) (pratesi2024guidelinesonthe pages 51-53); Rinaldi et al., *J Clin Med* 2024, DOI: 10.3390/jcm13195793, https://doi.org/10.3390/jcm13195793 (2024) (rinaldi2024thedefinitiondiagnosis pages 9-10) |
| Endovascular treatment | Endovascular therapy is now generally first-line for elective anatomically suitable SAAs. Techniques include coil embolization, sac/parent-artery embolization, plugs, covered stents/stent-grafts, glue/Lipidol, thrombin, stent-assisted coiling. Advantages include shorter length of stay and lower perioperative morbidity; drawbacks include splenic infarction, post-embolization syndrome, and higher reintervention risk in rupture. | Giant SAA pooled review: endovascular complication rate 23.08%, mean LOS 2.36 days, no recanalization during median follow-up 17.28 months. Stent-graft review: immediate technical/clinical success 90.2%, splenic infarction 4.9%, aneurysm exclusion 87.8%, no reinterventions. Wang 2024 cohort (63 pts): postembolization syndrome 10 pts; splenic infarction 7 pts; mean LOS 5.5 days; complete thrombosis in all at mean 17.2 months. | Rinaldi et al., *J Clin Med* 2024, DOI: 10.3390/jcm13195793, https://doi.org/10.3390/jcm13195793 (2024); Borghese et al., *J Clin Med* 2024, DOI: 10.3390/jcm13102802, https://doi.org/10.3390/jcm13102802 (2024); Wang et al., *CVIR Endovasc* 2024, DOI: 10.1186/s42155-024-00427-9, https://doi.org/10.1186/s42155-024-00427-9 (2024) (rinaldi2024thedefinitiondiagnosis pages 1-2, rinaldi2024thedefinitiondiagnosis pages 6-7) |
| Open surgery | Open repair remains important for ruptured SAAs, hemodynamic instability, pregnancy-associated rupture, and distal/hilar aneurysms where splenic preservation may not be feasible. Procedures include ligation, aneurysmectomy, splenectomy ± distal pancreatectomy, and selective reconstruction. | Giant pooled review: open complication rate 14.89%, mean LOS 12.29 days. In nationwide inpatient comparison, open repair had higher cardiac (6.9% vs 2.3%), pulmonary (16.1% vs 8.9%), and SSI (5.1% vs 0.6%) complication rates and longer LOS (6 vs 4 days), with similar in-hospital mortality (3% both) compared with endovascular repair. | Rinaldi et al., *J Clin Med* 2024, DOI: 10.3390/jcm13195793, https://doi.org/10.3390/jcm13195793 (2024); Sticco et al., *Vascular* 2016, DOI: 10.1177/1708538115613703, https://doi.org/10.1177/1708538115613703 (2016) (rinaldi2024thedefinitiondiagnosis pages 1-2, sticco2016acomparisonof pages 1-2) |
| Hybrid treatment | Hybrid approaches are used selectively for anatomically complex giant lesions. | Giant pooled review: hybrid used in 9/82 patients (10.98%), complication rate 22.22%, mean LOS 5 days. | Rinaldi et al., *J Clin Med* 2024, DOI: 10.3390/jcm13195793, https://doi.org/10.3390/jcm13195793 (2024) (rinaldi2024thedefinitiondiagnosis pages 1-2, rinaldi2024thedefinitiondiagnosis pages 6-7) |
| Comparative outcomes: intact/elective SAA | Comparative observational data generally favor endovascular repair for lower perioperative morbidity and shorter hospitalization, while open repair may offer fewer reinterventions/stronger primary technical success in some series. | Nationwide inpatient study: LOS 4 vs 6 days (EVT vs open), similar mortality 3% each; lower cardiac/pulmonary/SSI complications with EVT. Mixed VAA/RAA series: LOS 7.2±6.9 vs 11.8±6.7 days in elective cases; primary technical success 79.3% EVT vs 100% open. | Sticco et al., *Vascular* 2016, DOI: 10.1177/1708538115613703, https://doi.org/10.1177/1708538115613703 (2016); Wolk et al., *Langenbecks Arch Surg* 2021, DOI: 10.1007/s00423-021-02149-1, https://doi.org/10.1007/s00423-021-02149-1 (2021) (sticco2016acomparisonof pages 1-2) |
| Outcomes in ruptured SAA: open vs EVT | For ruptured SAA, available evidence shows similar mortality between open and EVT overall, but EVT has substantially more reinterventions/conversions; open repair remains preferred in hemodynamic instability and pregnancy-related rupture. | Systematic review of 350 ruptured SAA patients: overall mortality 10.6%; OSR 12.9% vs EVT 7.8% (p=0.84). Reinterventions after EVT 22.4% (37 total; many converted to laparotomy/splenectomy) vs 1.6% after OSR. | Rinaldi et al., *J Clin Med* 2023, DOI: 10.3390/jcm12186085, https://doi.org/10.3390/jcm12186085 (2023) (rinaldi2023endovascularandopen pages 1-3) |


*Table: This table summarizes high-yield, evidence-supported facts on splenic artery aneurysm, including epidemiology, major risk factors, imaging, guideline thresholds, and treatment outcomes. It is designed as a compact reference for disease knowledge-base curation and clinical/research synthesis.*

---

## 1. Disease information

### 1.1 Overview / definition
* **Definition:** A 2024 systematic review defines SAA as **“an arterial dilation exceeding 50% of the normal diameter of the splenic artery.”** (rinaldi2024thedefinitiondiagnosis pages 6-7)
* **True vs pseudoaneurysm:**
  * **True SAA** involves dilation of the artery with (by definition) the native wall layers; the 2024 review describes progressive degradation of elastic fibers and smooth muscle cells in the wall. (rinaldi2024thedefinitiondiagnosis pages 7-9)
  * **Splenic artery pseudoaneurysm (SAP/SAPA)** lacks at least one native wall layer and is replaced by fibrotic tissue; it is strongly linked to local arterial injury (pancreatitis/trauma/surgery/infection) and has substantially higher rupture risk. (rinaldi2024thedefinitiondiagnosis pages 7-9, chaer2020thesocietyfor pages 12-13)

### 1.2 Key identifiers (OMIM/Orphanet/ICD/MeSH/MONDO)
* **Data gap in retrieved corpus:** The provided full-text/guideline excerpts did **not** include explicit OMIM/Orphanet/MeSH/ICD-10/ICD-11/MONDO identifiers. This report therefore **cannot** cite authoritative codes from the current evidence set.

### 1.3 Synonyms / alternative names
* Splenic artery aneurysm; SAA; true splenic artery aneurysm. (rinaldi2024thedefinitiondiagnosis pages 1-2)
* Splenic artery pseudoaneurysm; SAP; splenic artery false aneurysm (in some surgical literature). (rinaldi2024thedefinitiondiagnosis pages 7-9, chaer2020thesocietyfor pages 13-15)
* **“Giant” SAA/SAP:** often defined as ≥5 cm (most common), sometimes >10 cm. (rinaldi2024thedefinitiondiagnosis pages 4-6, rinaldi2024thedefinitiondiagnosis pages 7-9)

### 1.4 Evidence provenance (individual patients vs aggregated resources)
Most available evidence for SAA derives from **aggregated disease-level sources** such as guidelines, systematic reviews/meta-analyses, and retrospective series; the rarity and heterogeneity of SAA limit randomized evidence. (marone2023currentdebatesin pages 1-4, hogendoorn2014openrepairendovascular pages 4-5)

---

## 2. Etiology

### 2.1 Disease causal factors (mechanistic)
SAA is a multifactorial vascular disease driven by arterial wall vulnerability and hemodynamic stress.

* **Arterial wall degeneration and stress:** An older but influential review attributes SAA formation to degenerative and dysplastic processes (e.g., atherosclerosis/calcification, fibromuscular dysplasia, cystic medial degeneration, myxoid degeneration) coupled with turbulent flow and mechanical injury. (dave2000splenicarteryaneurysm pages 4-5)
* **Portal hypertension/hyperdynamic flow:** Portal hypertension creates a “splenic hyperkinetic state” with increased splenic artery flow and diameter; Kóbori et al. link hyperkinetic flow to increased diameter and wall tension “according to the law of Laplace.” (dave2000splenicarteryaneurysm pages 4-5, kobori1997splenicarteryaneurysms pages 3-4)
* **Pregnancy-related hormonal and structural changes:** Increased estrogen/progesterone/relaxin (and other pregnancy-associated hormonal factors) are linked to structural weakening (e.g., fragmentation of internal elastic lamina, subendothelial thickening) plus increased third-trimester blood pressure. (rinaldi2024thedefinitiondiagnosis pages 7-9, dave2000splenicarteryaneurysm pages 4-5)
* **Pseudoaneurysm mechanism:** Pseudoaneurysms are mainly due to **focal wall disruption** from pancreatitis/pseudocysts, trauma, surgery, or infection. (rinaldi2024thedefinitiondiagnosis pages 7-9, uy2017vasculardiseasesof pages 4-5)
* **Segmental arterial mediolysis (SAM):** A noninflammatory arteriopathy in which “segmental lysis of the tunica media” and smooth muscle loss produce dissecting hematomas and aneurysmal dilatation; portal hypertension may amplify inflow into a pre-existing SAM lesion, precipitating rupture. (lohr2013rapidprogressionof pages 2-3, imai2005berrysplenicartery pages 4-5)

### 2.2 Risk factors (clinical associations)
* **Portal hypertension / cirrhosis / liver transplantation:** consistently associated with higher prevalence and is treated as a high-risk context in guidelines. (chaer2020thesocietyfor pages 12-13, kobori1997splenicarteryaneurysms pages 2-3, kaya2016prevalenceandpredictive pages 1-2)
* **Pregnancy and multiparity:** pregnancy is a major rupture-risk setting and drives recommendations to treat all true SAAs in women of childbearing age. (chaer2020thesocietyfor pages 12-13, obara2020currentmanagementstrategies pages 5-7)
* **Pancreatitis / trauma / surgery / infection:** particularly for pseudoaneurysm formation. (rinaldi2024thedefinitiondiagnosis pages 7-9, rinaldi2024thedefinitiondiagnosis pages 9-10)
* **Nonatherosclerotic etiologies (e.g., SAM):** guideline excerpts list nondegenerative etiologies as reasons for earlier treatment. (chaer2020thesocietyfor pages 13-15)

### 2.3 Protective factors
* **Data gap:** No protective genetic variants or environmental protective factors were identified in the retrieved evidence. One 2024 guideline excerpt notes debate on whether **arterial wall calcification** is protective, but does not resolve it with quantitative evidence in the excerpt. (pratesi2024guidelinesonthe pages 51-53)

### 2.4 Gene–environment interactions
* **Data gap:** No gene–environment interaction studies were present in the retrieved corpus.

---

## 3. Phenotypes

### 3.1 Core clinical phenotypes (with suggested HPO terms)
**A. Asymptomatic/incidental detection (common in non-giant SAAs)**
* Older review: **80–95%** asymptomatic and incidentally found. (dave2000splenicarteryaneurysm pages 4-5)
* Giant series differs: only **17.07%** asymptomatic. (rinaldi2024thedefinitiondiagnosis pages 4-6)
* **Suggested HPO:** *Asymptomatic* (HP:0000007).

**B. Abdominal pain (most common symptom in giant lesions)**
* Giant pooled review: pain in **59.76%** (left upper quadrant/epigastric common). (rinaldi2024thedefinitiondiagnosis pages 4-6)
* **Suggested HPO:** *Abdominal pain* (HP:0002027); *Left upper quadrant abdominal pain* (HP:0025404, if used);

**C. Palpable abdominal mass (giant lesions)**
* Giant pooled review: palpable mass **28.05%**. (rinaldi2024thedefinitiondiagnosis pages 4-6)
* **Suggested HPO:** *Abdominal mass* (HP:0003270).

**D. Rupture phenotype: hemorrhage and shock**
* Ruptured SAA commonly presents with severe abdominal pain, hypotension/hemorrhagic shock, anemia/coagulopathy; emergent CTA used for diagnosis. (rinaldi2023endovascularandopen pages 1-3)
* **Suggested HPO:** *Hemorrhagic shock* (HP:0001919); *Hypotension* (HP:0002615); *Anemia* (HP:0001903).

### 3.2 Temporal phenotype notes
* Rupture in pregnancy is most often in **third trimester/postpartum** in classic series and referenced guideline summaries. (dave2000splenicarteryaneurysm pages 4-5, chaer2020thesocietyfor pages 12-13)

### 3.3 Quality of life impact
* Direct QoL instrument data (SF-36/EQ-5D/PROMIS) were not identified in the retrieved sources. Impact is inferred from symptom burden (pain) and catastrophic rupture consequences. (rinaldi2023endovascularandopen pages 1-3, rinaldi2024thedefinitiondiagnosis pages 4-6)

---

## 4. Genetic / molecular information

### 4.1 Causal genes / pathogenic variants
* **Not established for isolated SAA in this evidence set.** The retrieved literature emphasizes **acquired hemodynamic/hormonal factors** and **arteriopathies** (e.g., SAM) rather than monogenic causation. (rinaldi2024thedefinitiondiagnosis pages 7-9, lohr2013rapidprogressionof pages 2-3)

### 4.2 Syndromic/associative conditions (non-exhaustive, from retrieved evidence)
Kaya et al. list associated conditions including **collagen vascular disease**, **arteritis**, **medial fibrodysplasia**, and **alpha-1 antitrypsin deficiency**, but do not provide gene/variant-level data in the excerpt. (kaya2016prevalenceandpredictive pages 5-6)

### 4.3 Epigenetics / omics
* **Data gap:** No epigenomic, transcriptomic, proteomic, or metabolomic signatures were identified in the retrieved corpus.

---

## 5. Environmental information

### 5.1 Environmental, lifestyle, occupational
* **Not specifically characterized** for SAA in the retrieved evidence.

### 5.2 Infectious agents
* Infection is cited as a potential cause of pseudoaneurysm via arterial wall injury in the 2024 systematic review (as part of SAP etiology), but no organism-specific data are provided. (rinaldi2024thedefinitiondiagnosis pages 7-9)

---

## 6. Mechanism / pathophysiology

### 6.1 Mechanistic causal chains (upstream → downstream)

**A. Portal hypertension-associated true SAA**
1. Chronic liver disease → portal hypertension → hyperdynamic splanchnic circulation and increased splenic venous flow (“splenic hyperkinetic state”). (dave2000splenicarteryaneurysm pages 4-5)
2. Hyperkinetic splenic arterial flow increases arterial diameter and wall tension (Laplace law) → progressive wall degeneration → aneurysm formation and increased rupture susceptibility. (kobori1997splenicarteryaneurysms pages 3-4, dave2000splenicarteryaneurysm pages 4-5)
3. Clinical manifestation: incidental aneurysm or rupture with hemoperitoneum/shock. (dave2000splenicarteryaneurysm pages 4-5, rinaldi2023endovascularandopen pages 1-3)

**B. Pregnancy-associated SAA rupture risk**
1. Pregnancy → elevated estrogen/progesterone/relaxin and other hormonal mediators → structural weakening (fragmented internal elastic lamina, subendothelial thickening) and altered elastin integrity. (rinaldi2024thedefinitiondiagnosis pages 7-9, dave2000splenicarteryaneurysm pages 4-5)
2. Concurrent late-pregnancy hemodynamic stress (increased blood volume/cardiac output, increased BP) → increased wall stress → rupture risk. (rinaldi2024thedefinitiondiagnosis pages 7-9)

**C. Pancreatitis-associated splenic artery pseudoaneurysm (SAP)**
1. Acute/chronic pancreatitis or pseudocyst → enzymatic/inflammatory injury to arterial wall or focal disruption → pseudoaneurysm formation. (rinaldi2024thedefinitiondiagnosis pages 7-9, uy2017vasculardiseasesof pages 4-5)
2. Clinical manifestation: hemorrhage, GI bleeding (e.g., hemosuccus pancreaticus), hemodynamic instability. (obara2020currentmanagementstrategies pages 5-7)

**D. Segmental arterial mediolysis (SAM) leading to SAA**
1. SAM: segmental medial lysis with smooth muscle loss → gaps/dissecting hematoma → aneurysmal dilation. (lohr2013rapidprogressionof pages 2-3)
2. Superimposed hemodynamic stress (BP surges; portal hypertension increasing inflow) → expansion/rupture. (lohr2013rapidprogressionof pages 2-3, imai2005berrysplenicartery pages 4-5)

### 6.2 Suggested ontology terms
* **GO biological processes (suggested):** *blood vessel remodeling*; *extracellular matrix organization*; *elastic fiber assembly*; *response to mechanical stimulus*; *smooth muscle cell apoptosis*; *inflammatory response* (for pseudoaneurysm etiologies). (rinaldi2024thedefinitiondiagnosis pages 7-9, dave2000splenicarteryaneurysm pages 4-5)
* **Cell types (suggested CL terms):** vascular smooth muscle cell; endothelial cell; fibroblast; macrophage (for pancreatitis/injury context). (rinaldi2024thedefinitiondiagnosis pages 7-9, lohr2013rapidprogressionof pages 2-3)

---

## 7. Anatomical structures affected

### 7.1 Primary anatomy (with suggested UBERON terms)
* **Splenic artery** (primary affected structure). Suggested UBERON: *splenic artery* (UBERON:0001621).
* **Spleen**: downstream ischemia/infarction risk after embolization or distal ligation. Suggested UBERON: *spleen* (UBERON:0002106). (chaer2020thesocietyfor pages 13-15)
* **Portal venous system** in portal hypertension context; splenic vein enlargement predicts SAA in cirrhosis. Suggested UBERON: *splenic vein* (UBERON:0001615), *portal vein* (UBERON:0001633). (kaya2016prevalenceandpredictive pages 1-2)
* **Pancreas**: pseudoaneurysm etiologies (pancreatitis), potential erosion/bleeding into pancreatic duct. Suggested UBERON: *pancreas* (UBERON:0001264). (obara2020currentmanagementstrategies pages 5-7, dave2000splenicarteryaneurysm pages 4-5)

### 7.2 Tissue/cell and subcellular
* Primary pathology involves arterial wall layers (intima/media/adventitia), with elastic lamina disruption and smooth muscle cell injury in some pathologic descriptions. (imai2005berrysplenicartery pages 4-5, rinaldi2024thedefinitiondiagnosis pages 7-9)

---

## 8. Temporal development

### 8.1 Onset
* Typically **adult-onset** and often detected incidentally due to imaging. (dave2000splenicarteryaneurysm pages 4-5, chaer2020thesocietyfor pages 12-13)

### 8.2 Progression
* Many small, stable true SAAs show minimal growth in observed cohorts; SVS excerpt summarizes mean observed size ~2.1 cm with mean follow-up 75 months in a nonoperative Mayo Clinic series. (chaer2020thesocietyfor pages 12-13)

### 8.3 Critical periods
* **Pregnancy (3rd trimester/postpartum)** is a critical risk window for rupture. (dave2000splenicarteryaneurysm pages 4-5, chaer2020thesocietyfor pages 12-13)

---

## 9. Inheritance and population

### 9.1 Epidemiology (general population)
* Incidence estimates vary by ascertainment method: **0.09%** (autopsy) and **0.78%** (angiographic) in a 2024 review excerpt. (rinaldi2024thedefinitiondiagnosis pages 7-9)
* Sticco et al. cite overall incidence **<0.8%**. (sticco2016acomparisonof pages 1-2)

### 9.2 Portal hypertension / cirrhosis / transplant populations
* **Liver transplant candidates/recipients:** Kóbori et al. (1997) found SAA in **45/337 (13%)** liver transplant patients; incidence **16%** among those with portal hypertension and **0%** without portal hypertension (p<0.001), with higher incidence in adults (17%) vs children (4%). (kobori1997splenicarteryaneurysms pages 2-3)
* **Cirrhosis cohort:** Kaya et al. (2016) found SAA in **27/171 (15.7%)** cirrhosis patients on four-phase CT; most were distal (74%), solitary (88.8%), and small (mean diameter 11.66 mm). (kaya2016prevalenceandpredictive pages 1-2)

### 9.3 Sex ratio / age distribution
* Classic SAA reported female predominance (about 4:1) and association with multiparity; giant SAA systematic review shows near-equal sex distribution. (obara2020currentmanagementstrategies pages 5-7, rinaldi2024thedefinitiondiagnosis pages 1-2)

### 9.4 Inheritance
* No Mendelian inheritance pattern is supported by the retrieved evidence for isolated SAA.

---

## 10. Diagnostics

### 10.1 Imaging (core diagnostic modality)
**SVS 2020 (key points from excerpt):**
* **CTA** recommended as initial diagnostic tool for SAA (thin sections if available). (chaer2020thesocietyfor pages 12-13)
* **MRA** recommended when iodinated contrast is contraindicated; **arteriography** reserved for unclear noninvasive results or when planning endovascular therapy. (chaer2020thesocietyfor pages 12-13)
* Ultrasound has **poor sensitivity for SAA <3 cm** in SVS excerpt. (chaer2020thesocietyfor pages 12-13)

**Giant SAA/SAP imaging patterns (2024 systematic review):** CT used in **80.49%**, angiography in **54.88%**, EcoColorDoppler in **45.12%**, MRI rarely (3.66%). (rinaldi2024thedefinitiondiagnosis pages 4-6)

### 10.2 Laboratory / biomarkers
* No specific laboratory biomarkers for diagnosis were identified in the retrieved corpus.

### 10.3 Differential diagnosis
* Not systematically enumerated in the retrieved excerpts; pseudoaneurysm vs true aneurysm distinction is clinically crucial because pseudoaneurysm rupture risk is much higher. (chaer2020thesocietyfor pages 13-15)

### 10.4 Screening
* SVS and related excerpts highlight special high-risk groups (women of childbearing age; portal hypertension/liver transplant candidates), but no population screening program is described in the retrieved evidence. (chaer2020thesocietyfor pages 12-13, chaer2020thesocietyfor pages 13-15)

---

## 11. Outcome / prognosis

### 11.1 Natural history and rupture outcomes
* True SAA rupture risk is often cited around **2–3%**; older and review sources note varying estimates and emphasize risk concentration in pregnancy and portal hypertension contexts. (rinaldi2024thedefinitiondiagnosis pages 7-9, dave2000splenicarteryaneurysm pages 4-5)
* Ruptured SAA mortality in SVS excerpt: overall mortality up to **~25%**. (chaer2020thesocietyfor pages 12-13)

### 11.2 Pregnancy-related prognosis
* Pregnancy rupture contributes disproportionately (SVS excerpt: **20–50%** of ruptures) and carries extremely high maternal/fetal mortality (e.g., maternal ~80%, fetal ~90% in SVS excerpt; similar ranges across reviews). (chaer2020thesocietyfor pages 12-13, dave2000splenicarteryaneurysm pages 4-5)

### 11.3 Prognostic factors
* High-risk contexts: pregnancy, portal hypertension/liver transplantation, pseudoaneurysm etiology, aneurysm growth. (chaer2020thesocietyfor pages 12-13, chaer2020thesocietyfor pages 13-15)

---

## 12. Treatment

### 12.1 Guideline-driven treatment thresholds (expert consensus)

**SVS 2020 (Journal of Vascular Surgery; published Jul 2020; DOI: 10.1016/j.jvs.2020.01.039):**
* Treat **ruptured SAA** emergently. (chaer2020thesocietyfor pages 12-13)
* Treat **splenic artery pseudoaneurysms of any size** (high rupture risk). (chaer2020thesocietyfor pages 12-13)
* Treat **all true SAAs in women of childbearing age regardless of size**. (chaer2020thesocietyfor pages 12-13)
* Treat true SAAs **≥3 cm**, those with **growth**, or those that are **symptomatic**. (chaer2020thesocietyfor pages 12-13)
* Observation suggested for small (<3 cm), stable, asymptomatic true SAAs or patients with limited life expectancy. (chaer2020thesocietyfor pages 12-13)

**CIRSE Standards of Practice (Cardiovascular and Interventional Radiology; Nov 2024; DOI: 10.1007/s00270-023-03620-w):**
* Treat any symptomatic VAA/VAPA; treat **SAA ≥2 cm** (particularly saccular/distal/favorable anatomy); treat lesions growing **≥0.5 cm/year**; treat VAPAs regardless of symptoms; treat asymptomatic VAAs in women of child-bearing age. (rossi2024cirsestandardsof pages 1-3)
* Post-endovascular surveillance suggested with CTA/MRA at **3 months, 12 months, then yearly**. (rossi2024cirsestandardsof pages 1-3)

**Guideline-collision commentary (May 2023; DOI: 10.3390/jcm12093267):**
* Notes discrepancies across ESVS vs SVS thresholds (e.g., SVS 3 cm threshold for SAA) and differences in surveillance intervals (SVS annual imaging vs ESVS every 2–3 years for small asymptomatic aneurysms). (marone2023currentdebatesin pages 1-4)

### 12.2 Endovascular treatment (current applications / real-world implementation)
* SVS and CIRSE emphasize endovascular-first where anatomy allows (coil embolization, parent vessel sacrifice vs preservation strategies, stent-grafts). (chaer2020thesocietyfor pages 13-15, rossi2024cirsestandardsof pages 1-3)
* Meta-analysis evidence (Hogendoorn 2014; J Vasc Surg; Dec 2014; DOI: 10.1016/j.jvs.2014.08.067):
  * OPEN vs EV: **30-day mortality 5.1% vs 0.6% (P<.001)**; hospital stay **9.8 vs 2.0 days**. (hogendoorn2014openrepairendovascular pages 4-5)
  * EV has more minor complications (post-embolization syndrome treated as minor; ~25.1% in the meta-analysis) and higher reinterventions per year (**3.2%/yr EV vs 0.5%/yr open**). (hogendoorn2014openrepairendovascular pages 4-5, hogendoorn2014openrepairendovascular pages 8-9)
* Comparative US inpatient data (Sticco 2016; DOI: 10.1177/1708538115613703) show lower perioperative morbidity and shorter LOS with endovascular repair with similar in-hospital mortality. (sticco2016acomparisonof pages 1-2)

**MAXO suggestions (non-exhaustive):**
* Endovascular embolization procedure; stent-graft placement; aneurysm repair (endovascular). (chaer2020thesocietyfor pages 13-15, rossi2024cirsestandardsof pages 1-3)

### 12.3 Open surgery
* Remains essential for rupture, hemodynamic instability, pregnancy-associated rupture, and distal/hilar anatomy. (chaer2020thesocietyfor pages 13-15, rinaldi2023endovascularandopen pages 1-3)

**MAXO suggestions:**
* Aneurysmectomy; arterial ligation; splenectomy; distal pancreatectomy (for select hilar lesions). (rinaldi2024thedefinitiondiagnosis pages 6-7, chaer2020thesocietyfor pages 13-15)

### 12.4 Treatment outcomes in ruptured SAA
* Systematic review (J Clin Med; Sep 2023; DOI: 10.3390/jcm12186085): 129 studies/350 patients; overall mortality **10.6%**; **12.9% open vs 7.8% EVT (p=0.84)**; reinterventions **22.4%** after EVT vs **1.6%** after open repair. (rinaldi2023endovascularandopen pages 1-3)

---

## 13. Prevention

### 13.1 Primary prevention
* No established primary prevention interventions were identified in the retrieved evidence; prevention focuses on risk recognition (pregnancy/portal hypertension) and addressing modifiable contributors to pancreatitis/trauma when applicable.

### 13.2 Secondary prevention (surveillance)
* Surveillance practices vary by guideline; CIRSE suggests CTA/MRA at 3 months, 12 months, then yearly post-EVT. (rossi2024cirsestandardsof pages 1-3)
* SVS vs ESVS surveillance intervals for small asymptomatic lesions differ (annual vs q2–3 years). (marone2023currentdebatesin pages 1-4)

---

## 14. Other species / natural disease
* **Data gap:** No veterinary or non-human natural disease evidence was identified in the retrieved corpus.

---

## 15. Model organisms
* **Data gap:** No model organism systems specific to SAA were identified in the retrieved corpus.

---

## Recent developments and expert analysis (2023–2024 emphasis)

1. **Guideline harmonization and persistent evidence gaps (2023):** A 2023 expert commentary highlights how rarity and heterogeneity impede high-level evidence and lead to threshold/surveillance disagreements across SVS vs ESVS, emphasizing the need for careful individualized decision-making. (marone2023currentdebatesin pages 1-4)
2. **Endovascular standardization (2024):** CIRSE’s 2024 standards codify endovascular indications, device options, and structured post-procedure surveillance schedules, reflecting the central role of interventional radiology in contemporary care. (rossi2024cirsestandardsof pages 1-3)
3. **Refined characterization of giant SAA/SAP (2024):** The 2024 systematic review quantifies presentation patterns, imaging choices (CT predominance), and comparative LOS/complication rates across open/endovascular/hybrid approaches for giant lesions, while underscoring inconsistent “giant” definitions. (rinaldi2024thedefinitiondiagnosis pages 1-2, rinaldi2024thedefinitiondiagnosis pages 4-6)

---

## Clinical trials / research in progress

* **NCT07053605 (ClinicalTrials.gov; first posted 2025-07-08; recruiting):** single-group interventional study of **laparoscopic resection of SAA with spleen preservation**; estimated enrollment 10; start 2025-06-23; primary completion 2027-06-30; primary outcomes emphasize immune function markers (C3/C4, immunoglobulins, lymphocyte subsets) across follow-up timepoints. URL: https://clinicaltrials.gov/study/NCT07053605 (NCT07053605 chunk 1)
* **NCT01387828 (ClinicalTrials.gov; posted 2011; completed):** randomized parallel trial comparing open vs laparoscopic splenic aneurysm repair; enrollment 29; start Jan 2001; completion Apr 2011; primary outcome postoperative morbidity (Dindo–Clavien). URL: https://clinicaltrials.gov/study/NCT01387828 (NCT01387828 chunk 1)

---

## Key limitations of this report (evidence availability)
* Formal **MeSH/ICD/ICD-11/MONDO/OMIM/Orphanet identifiers** were not present in the retrieved full-text excerpts; therefore, codes are not provided with citations.
* **Genetic variant-level evidence**, multi-omics profiling, model organism data, and validated QoL metrics were not found in the retrieved evidence set; the literature here is predominantly clinical and procedural.
* The report necessarily integrates older landmark sources (e.g., 1997–2000) for portal-hypertension/pregnancy epidemiology because those specific quantitative observations are widely cited and remain foundational; they are contextualized by 2020–2024 guideline syntheses.


References

1. (chaer2020thesocietyfor pages 12-13): Rabih A. Chaer, Christopher J. Abularrage, Dawn M. Coleman, Mohammad H. Eslami, Vikram S. Kashyap, Caron Rockman, and M. Hassan Murad. The society for vascular surgery clinical practice guidelines on the management of visceral aneurysms. Journal of Vascular Surgery, 72:3S-39S, Jul 2020. URL: https://doi.org/10.1016/j.jvs.2020.01.039, doi:10.1016/j.jvs.2020.01.039. This article has 660 citations and is from a domain leading peer-reviewed journal.

2. (chaer2020thesocietyfor pages 13-15): Rabih A. Chaer, Christopher J. Abularrage, Dawn M. Coleman, Mohammad H. Eslami, Vikram S. Kashyap, Caron Rockman, and M. Hassan Murad. The society for vascular surgery clinical practice guidelines on the management of visceral aneurysms. Journal of Vascular Surgery, 72:3S-39S, Jul 2020. URL: https://doi.org/10.1016/j.jvs.2020.01.039, doi:10.1016/j.jvs.2020.01.039. This article has 660 citations and is from a domain leading peer-reviewed journal.

3. (rossi2024cirsestandardsof pages 1-3): Michele Rossi, Miltiadis Krokidis, Elika Kashef, Bora Peynircioglu, and Marcello Andrea Tipaldi. Cirse standards of practice for the endovascular treatment of visceral and renal artery aneurysms and pseudoaneurysms. Cardiovascular and Interventional Radiology, 47:26-35, Nov 2024. URL: https://doi.org/10.1007/s00270-023-03620-w, doi:10.1007/s00270-023-03620-w. This article has 50 citations and is from a peer-reviewed journal.

4. (hogendoorn2014openrepairendovascular pages 4-5): Wouter Hogendoorn, Anthi Lavida, M.G. Myriam Hunink, Frans L. Moll, George Geroulakos, Bart E. Muhs, and Bauer E. Sumpio. Open repair, endovascular repair, and conservative management of true splenic artery aneurysms. Journal of vascular surgery, 60 6:1667-76.e1, Dec 2014. URL: https://doi.org/10.1016/j.jvs.2014.08.067, doi:10.1016/j.jvs.2014.08.067. This article has 164 citations and is from a domain leading peer-reviewed journal.

5. (rinaldi2023endovascularandopen pages 1-3): Luigi Federico Rinaldi, Chiara Brioschi, and Enrico Maria Marone. Endovascular and open surgical treatment of ruptured splenic artery aneurysms: a case report and a systematic literature review. Journal of Clinical Medicine, 12:6085, Sep 2023. URL: https://doi.org/10.3390/jcm12186085, doi:10.3390/jcm12186085. This article has 13 citations.

6. (rinaldi2024thedefinitiondiagnosis pages 1-2): Valerio Rinaldi, Giulio Illuminati, Roberto Caronna, Giampaolo Prezioso, Piergaspare Palumbo, Paolina Saullo, Vito D’Andrea, and Priscilla Nardi. The definition, diagnosis, and management of giant splenic artery aneurysms and pseudoaneurysms: a systematic review. Journal of Clinical Medicine, 13:5793, Sep 2024. URL: https://doi.org/10.3390/jcm13195793, doi:10.3390/jcm13195793. This article has 9 citations.

7. (rinaldi2024thedefinitiondiagnosis pages 4-6): Valerio Rinaldi, Giulio Illuminati, Roberto Caronna, Giampaolo Prezioso, Piergaspare Palumbo, Paolina Saullo, Vito D’Andrea, and Priscilla Nardi. The definition, diagnosis, and management of giant splenic artery aneurysms and pseudoaneurysms: a systematic review. Journal of Clinical Medicine, 13:5793, Sep 2024. URL: https://doi.org/10.3390/jcm13195793, doi:10.3390/jcm13195793. This article has 9 citations.

8. (rinaldi2024thedefinitiondiagnosis pages 7-9): Valerio Rinaldi, Giulio Illuminati, Roberto Caronna, Giampaolo Prezioso, Piergaspare Palumbo, Paolina Saullo, Vito D’Andrea, and Priscilla Nardi. The definition, diagnosis, and management of giant splenic artery aneurysms and pseudoaneurysms: a systematic review. Journal of Clinical Medicine, 13:5793, Sep 2024. URL: https://doi.org/10.3390/jcm13195793, doi:10.3390/jcm13195793. This article has 9 citations.

9. (sticco2016acomparisonof pages 1-2): Andrew Sticco, Alok Aggarwal, Michael D Shapiro, Abimbola Pratt, Donald Rissuci, and Marcus D'ayala. A comparison of open and endovascular treatment strategies for the management of splenic artery aneurysms. Vascular, 24:487-491, Jul 2016. URL: https://doi.org/10.1177/1708538115613703, doi:10.1177/1708538115613703. This article has 17 citations and is from a peer-reviewed journal.

10. (obara2020currentmanagementstrategies pages 5-7): Hideaki Obara, Matsubara Kentaro, Masanori Inoue, and Yuko Kitagawa. Current management strategies for visceral artery aneurysms: an overview. Surgery Today, 50:38-49, Oct 2020. URL: https://doi.org/10.1007/s00595-019-01898-3, doi:10.1007/s00595-019-01898-3. This article has 123 citations and is from a peer-reviewed journal.

11. (dave2000splenicarteryaneurysm pages 4-5): Sandeep P. Dave, Ernane D. Reis, Azhar Hossain, Peter J. Taub, Morris D. Kerstein, and Larry H. Hollier. Splenic artery aneurysm in the 1990s. Annals of Vascular Surgery, 14:223-229, May 2000. URL: https://doi.org/10.1007/s100169910039, doi:10.1007/s100169910039. This article has 229 citations and is from a peer-reviewed journal.

12. (pratesi2024guidelinesonthe pages 51-53): C Pratesi, D Esposito, R Martini, and C Novali. Guidelines on the diagnosis, treatment and management of visceral and renal arteries aneurysms: a joint assessment by the italian societies of vascular and …. Unknown journal, 2024.

13. (rinaldi2024thedefinitiondiagnosis pages 9-10): Valerio Rinaldi, Giulio Illuminati, Roberto Caronna, Giampaolo Prezioso, Piergaspare Palumbo, Paolina Saullo, Vito D’Andrea, and Priscilla Nardi. The definition, diagnosis, and management of giant splenic artery aneurysms and pseudoaneurysms: a systematic review. Journal of Clinical Medicine, 13:5793, Sep 2024. URL: https://doi.org/10.3390/jcm13195793, doi:10.3390/jcm13195793. This article has 9 citations.

14. (rinaldi2024thedefinitiondiagnosis pages 6-7): Valerio Rinaldi, Giulio Illuminati, Roberto Caronna, Giampaolo Prezioso, Piergaspare Palumbo, Paolina Saullo, Vito D’Andrea, and Priscilla Nardi. The definition, diagnosis, and management of giant splenic artery aneurysms and pseudoaneurysms: a systematic review. Journal of Clinical Medicine, 13:5793, Sep 2024. URL: https://doi.org/10.3390/jcm13195793, doi:10.3390/jcm13195793. This article has 9 citations.

15. (marone2023currentdebatesin pages 1-4): Enrico Maria Marone and Luigi Federico Rinaldi. Current debates in the management of visceral artery aneurysms: where the guidelines collide. Journal of Clinical Medicine, 12:3267, May 2023. URL: https://doi.org/10.3390/jcm12093267, doi:10.3390/jcm12093267. This article has 7 citations.

16. (kobori1997splenicarteryaneurysms pages 3-4): László Kóbori, Marjan J. van der Kolk, Koert P. de Jong, Paul M.J.G. Peeters, Ids J. Klompmaker, Theo Kok, Elizabeth B. Haagsma, and Maarten J.H. Slooff. Splenic artery aneurysms in liver transplant patients. Journal of Hepatology, 27:890-893, Nov 1997. URL: https://doi.org/10.1016/s0168-8278(97)80327-3, doi:10.1016/s0168-8278(97)80327-3. This article has 68 citations and is from a highest quality peer-reviewed journal.

17. (uy2017vasculardiseasesof pages 4-5): Pearl Princess D. Uy, Denise Marie Francisco, Anshu Trivedi, Michael O’Loughlin, and George Y. Wu. Vascular diseases of the spleen: a review. Journal of Clinical and Translational Hepatology, 5:152-164, Mar 2017. URL: https://doi.org/10.14218/jcth.2016.00062, doi:10.14218/jcth.2016.00062. This article has 67 citations.

18. (lohr2013rapidprogressionof pages 2-3): J.-Matthias Löhr, Dietmar Dinter, Steffen J. Diehl, Stephan L. Haas, Mira Veeser, Roland Pfützer, Jürgen Retter, Stefan O. Schönberg, Christoph Düber, Volker Keim, Dirk Schadendorf, and Heiko Witt. Rapid progression of a splenic aneurysm due to segmental arterial mediolysis: a rare cause of acute pancreatitis. Pancreatology : official journal of the International Association of Pancreatology (IAP) ... [et al.], 13 5:553-6, Sep 2013. URL: https://doi.org/10.1016/j.pan.2013.06.001, doi:10.1016/j.pan.2013.06.001. This article has 5 citations.

19. (imai2005berrysplenicartery pages 4-5): Miwa Akasofu Imai, Ei Kawahara, Shogo Katsuda, and Tatsuya Yamashita. Berry splenic artery aneurysm rupture in association with segmental arterial mediolysis and portal hypertension. Pathology International, 55:290-295, May 2005. URL: https://doi.org/10.1111/j.1440-1827.2005.01827.x, doi:10.1111/j.1440-1827.2005.01827.x. This article has 16 citations and is from a peer-reviewed journal.

20. (kobori1997splenicarteryaneurysms pages 2-3): László Kóbori, Marjan J. van der Kolk, Koert P. de Jong, Paul M.J.G. Peeters, Ids J. Klompmaker, Theo Kok, Elizabeth B. Haagsma, and Maarten J.H. Slooff. Splenic artery aneurysms in liver transplant patients. Journal of Hepatology, 27:890-893, Nov 1997. URL: https://doi.org/10.1016/s0168-8278(97)80327-3, doi:10.1016/s0168-8278(97)80327-3. This article has 68 citations and is from a highest quality peer-reviewed journal.

21. (kaya2016prevalenceandpredictive pages 1-2): Muhsin Kaya, Şengül Baran, Cemil Güya, and Mehmet Ali Kaplan. Prevalence and predictive factors for development of splenic artery aneurysms in cirrhosis. Indian Journal of Gastroenterology, 35:201-206, Jun 2016. URL: https://doi.org/10.1007/s12664-016-0670-z, doi:10.1007/s12664-016-0670-z. This article has 21 citations and is from a peer-reviewed journal.

22. (kaya2016prevalenceandpredictive pages 5-6): Muhsin Kaya, Şengül Baran, Cemil Güya, and Mehmet Ali Kaplan. Prevalence and predictive factors for development of splenic artery aneurysms in cirrhosis. Indian Journal of Gastroenterology, 35:201-206, Jun 2016. URL: https://doi.org/10.1007/s12664-016-0670-z, doi:10.1007/s12664-016-0670-z. This article has 21 citations and is from a peer-reviewed journal.

23. (hogendoorn2014openrepairendovascular pages 8-9): Wouter Hogendoorn, Anthi Lavida, M.G. Myriam Hunink, Frans L. Moll, George Geroulakos, Bart E. Muhs, and Bauer E. Sumpio. Open repair, endovascular repair, and conservative management of true splenic artery aneurysms. Journal of vascular surgery, 60 6:1667-76.e1, Dec 2014. URL: https://doi.org/10.1016/j.jvs.2014.08.067, doi:10.1016/j.jvs.2014.08.067. This article has 164 citations and is from a domain leading peer-reviewed journal.

24. (NCT07053605 chunk 1): Guo-Qing Jiang. Clinical Study on Laparoscopic Resection of Splenic Artery Aneurysm With Preservation of Spleen. Northern Jiangsu People's Hospital. 2025. ClinicalTrials.gov Identifier: NCT07053605

25. (NCT01387828 chunk 1):  Comparison Between Open and Laparoscopic Splenic Aneurysms Repair. Azienda Socio Sanitaria Territoriale degli Spedali Civili di Brescia. 2001. ClinicalTrials.gov Identifier: NCT01387828