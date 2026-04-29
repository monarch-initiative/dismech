---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-24T18:20:31.101854'
end_time: '2026-04-24T18:28:31.663602'
duration_seconds: 480.56
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: KRT85-Related Pure Hair-Nail Ectodermal Dysplasia
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 17
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** KRT85-Related Pure Hair-Nail Ectodermal Dysplasia
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **KRT85-Related Pure Hair-Nail Ectodermal Dysplasia** covering all of the
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
- **Disease Name:** KRT85-Related Pure Hair-Nail Ectodermal Dysplasia
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **KRT85-Related Pure Hair-Nail Ectodermal Dysplasia** covering all of the
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


# Comprehensive Research Report: KRT85-Related Pure Hair–Nail Ectodermal Dysplasia

## 1. Disease Information

### 1.1 Overview (current understanding)
KRT85-related pure hair–nail ectodermal dysplasia (PHNED; also written PHNEC) is a congenital genetic disorder characterized primarily by hypotrichosis/atrichia (ranging from sparse fragile hair to complete alopecia) and nail dystrophy, with other ectodermal structures (e.g., teeth and sweating) typically spared (“pure” hair–nail involvement). (shimomura2010mutationsinthe pages 1-2, amico2019compoundheterozygosityfor pages 1-3)

### 1.2 Key identifiers and nomenclature
Evidence-supported identifiers and names from the retrieved literature are summarized in the table artifact below.

| Recommended disease name | Synonyms / alternative names | OMIM disease ID | OMIM gene ID (KRT85) | Historical gene names | Chromosomal locus / region | MONDO ID from evidence | Evidence citation IDs | Key source URLs |
|---|---|---:|---:|---|---|---|---|---|
| KRT85-related pure hair and nail ectodermal dysplasia | Pure hair and nail ectodermal dysplasia (PHNED); Pure hair and nail ectodermal dysplasia / PHNEC; Ectodermal dysplasia of hair and nail type; Ectodermal dysplasia 4, hair/nail type (ECTD4) | 602032 | 602767 | KRT85; KRTHB5; hHb5 | KRT85 resides in the type II keratin cluster at 12q13 / 12q13.13; disease locus mapped in reports to 12q12-q14.1 and 12p11.1-q21.1 / 12q13 region | Not specifically identified for this disease in retrieved evidence; only broader Open Targets association to ectodermal dysplasia syndrome MONDO_0019287 was returned, so disease-specific MONDO should be treated as unavailable from current evidence | (shimomura2010mutationsinthe pages 1-2, naeem2006amutationin pages 1-2, amico2019compoundheterozygosityfor pages 1-3, naeem2006amutationin pages 3-4, lin2012lossoffunctionmutationsin pages 1-2) | https://doi.org/10.1038/jid.2009.341 ; https://doi.org/10.1136/jmg.2005.033381 ; https://doi.org/10.1111/jdv.15777 ; https://doi.org/10.1016/j.ajhg.2012.08.029 |


*Table: This table summarizes the core identifiers, synonyms, historical nomenclature, and locus information for KRT85-related pure hair and nail ectodermal dysplasia. It is useful as a normalization artifact for a disease knowledge base entry, with evidence-linked terminology and source URLs.*

**Notes on disease identifiers not recovered from tools:** 
* Disease-specific MONDO, Orphanet, MeSH, and ICD-10/ICD-11 codes were not present in the retrieved full-text excerpts; only a broad Open Targets disease label (“ectodermal dysplasia syndrome”, MONDO_0019287) was returned and should not be treated as disease-specific for KRT85-PHNED. (artifact-00)

### 1.3 Evidence source type
The KRT85-related entity is supported mainly by (i) human family-based linkage and candidate-gene sequencing studies and (ii) subsequent NGS-panel diagnosis reports. (naeem2006amutationin pages 1-2, shimomura2010mutationsinthe pages 1-2, amico2019compoundheterozygosityfor pages 1-3)

## 2. Etiology

### 2.1 Disease causal factors
**Primary cause:** biallelic pathogenic variants in **KRT85** (historical name **KRTHB5/hHb5**; OMIM gene MIM 602767) disrupt hard-keratin intermediate filament biology in hair and nail. (shimomura2010mutationsinthe pages 1-2, naeem2006amutationin pages 1-2)

**Mode of inheritance:** most documented KRT85 cases are **autosomal recessive**, often in consanguineous families. (naeem2006amutationin pages 1-2, shimomura2010mutationsinthe pages 1-2)

### 2.2 Risk factors
**Genetic risk factors:** consanguinity/familial carrier status increases risk of homozygosity for pathogenic alleles (as illustrated by large consanguineous Pakistani pedigrees). (naeem2006amutationin pages 1-2, shimomura2010mutationsinthe pages 1-2)

**Environmental risk factors:** no disease-specific environmental triggers have been established in the retrieved primary literature. One report noted worsening of alopecia after febrile episodes in affected siblings with compound heterozygous KRT85 variants; this observation does not establish causality but suggests symptoms can fluctuate with systemic stressors. (amico2019compoundheterozygosityfor pages 1-3)

### 2.3 Protective factors
No genetic or environmental protective factors were identified in the retrieved evidence.

### 2.4 Gene–environment interactions
No validated gene–environment interaction studies specific to KRT85-PHNED were identified in the retrieved evidence.

## 3. Phenotypes

### 3.1 Core phenotypic spectrum
Across reported KRT85-PHNED families, phenotypes include:
* **Congenital hypotrichosis/atrichia**: scalp, facial (including eyebrows/eyelashes), and body hair can be sparse to absent; some families show complete alopecia. (naeem2006amutationin pages 2-3, shimomura2010mutationsinthe pages 1-2)
* **Hair-shaft fragility and structural abnormalities**: scanning electron microscopy (SEM) demonstrated inconsistent hair-shaft thickness (not periodic like monilethrix) in one family; clinically hair is thin/fragile and breaks easily. (shimomura2010mutationsinthe pages 1-2, amico2019compoundheterozygosityfor pages 1-3)
* **Nail dystrophy**: irregularly shaped, fragile nails; can include micronychia, koilonychia, distal onycholysis; severe nail deformities reported in severe cases. (shimomura2010mutationsinthe pages 1-2, amico2019compoundheterozygosityfor pages 1-3)
* **Relative sparing of other ectodermal structures**: normal teeth and normal sweating are repeatedly reported in KRT85-PHNED families. (shimomura2010mutationsinthe pages 1-2, amico2019compoundheterozygosityfor pages 1-3)

#### Visual evidence
Pedigrees, clinical photos, and SEM hair images supporting these features are shown in Shimomura et al. 2010 (Figure 1), and the KRT85 variant evidence is shown in their Figure 2. (shimomura2010mutationsinthe media b5f82a0b, shimomura2010mutationsinthe media a9ef3a76)

### 3.2 Phenotype onset, progression, and severity
* **Onset:** typically **since birth** for both hair and nail findings in multiple families. (shimomura2010mutationsinthe pages 1-2)
* **Severity:** variable even across families; one family showed sparse hair and mild nail fragility while another showed complete alopecia with severe nail deformities. (shimomura2010mutationsinthe pages 1-2)
* **Course:** at least one sibling pair showed partial improvement (normalization of hair growth) after puberty, suggesting possible age-related modulation in some individuals. (amico2019compoundheterozygosityfor pages 1-3)

### 3.3 Suggested HPO terms (non-exhaustive)
* Hypotrichosis (HP:0001006)
* Alopecia (HP:0001596)
* Atrichia (HP:0001598)
* Abnormal hair shaft morphology (HP:0011354)
* Onychodystrophy (HP:0001806)
* Koilonychia (HP:0001805)
* Micronychia (HP:0001800)
* Onycholysis (HP:0001804)
* Keratosis pilaris (HP:0000964) / follicular papules (if present)

### 3.4 Quality-of-life impact
No disease-specific quantitative QoL instruments (e.g., DLQI, SF-36) were identified in the retrieved primary literature; given visible alopecia and nail fragility, psychosocial and functional impacts are plausible but not evidenced quantitatively here.

## 4. Genetic / Molecular Information

### 4.1 Causal gene
**KRT85** encodes a **type II hair keratin** expressed in hair matrix/precortex/cuticle cells; impaired availability of functional type II hair keratin to pair with type I partners is proposed to underlie the abnormal hair phenotype. (amico2019compoundheterozygosityfor pages 1-3)

### 4.2 Pathogenic variants (human)
**Pathogenic/likely pathogenic variants reported in retrieved primary/clinical literature include:**
* **c.233G>A (p.Arg78His)**, exon 1: homozygous in a large consanguineous Pakistani pedigree with complete alopecia and nail dystrophy; absent in 100 unrelated controls (200 chromosomes). (naeem2006amutationin pages 3-4)
* **c.1448_1449delCT (p.Pro483Argfs*18)**, exon 9: homozygous frameshift predicted to truncate the protein; reported in consanguineous Pakistani families and absent from 100 healthy Pakistani controls in one study. (shimomura2010mutationsinthe pages 1-2)
* **c.502_525del (p.del168_175)** (in-frame deletion) and **c.886A>G (p.Lys296Glu)** (missense): compound heterozygosity in two sisters from a non-consanguineous French family; both reported absent from gnomAD. (amico2019compoundheterozygosityfor pages 1-3)

**Variant classes:** missense, frameshift, and in-frame deletion are represented among reported alleles. (shimomura2010mutationsinthe pages 1-2, amico2019compoundheterozygosityfor pages 1-3)

**Population frequency statements:** 
* c.233G>A was not detected in 100 unrelated controls in the original linkage/candidate gene report. (naeem2006amutationin pages 3-4)
* The 2019 report states both compound heterozygous variants were absent from gnomAD. (amico2019compoundheterozygosityfor pages 1-3)

**Somatic vs germline:** all reported variants are germline and segregate with disease in families. (naeem2006amutationin pages 1-2, shimomura2010mutationsinthe pages 1-2, amico2019compoundheterozygosityfor pages 1-3)

### 4.3 Modifier genes / epigenetics / chromosomal abnormalities
No validated modifier genes, epigenetic signatures, or chromosomal abnormalities specific to KRT85-PHNED were identified in the retrieved evidence.

## 5. Mechanism / Pathophysiology

### 5.1 Causal chain (gene → cell → tissue → phenotype)
A coherent mechanism supported by available evidence is:
1. **Biallelic KRT85 variants** (frameshift or missense) alter K85 structure/function. (shimomura2010mutationsinthe pages 1-2)
2. K85 dysfunction is proposed to impair **intermediate filament assembly/heterodimer formation** in hard-keratinizing structures (hair shaft and nails), consistent with keratin biology and with a truncation predicted to alter the C-terminal tail (loss of cysteine residues) and thus disrupt keratin interactions. (shimomura2010mutationsinthe pages 1-2)
3. The result is **abnormal hair-shaft formation and fragility** and **nail dystrophy**, manifesting clinically as hypotrichosis/alopecia and dystrophic nails. (shimomura2010mutationsinthe pages 1-2, amico2019compoundheterozygosityfor pages 1-3)

### 5.2 Pathways and processes (ontology suggestions)
**Suggested GO Biological Process terms (examples):**
* keratinization (GO:0031424)
* hair follicle development (GO:0001942)
* hair cycle process (GO:0022405)
* intermediate filament organization (GO:0045109)

**Suggested GO Cellular Component terms:**
* intermediate filament (GO:0005882)
* keratin filament (GO:0045095)

**Suggested Cell Ontology (CL) terms (examples):**
* keratinocyte (CL:0000312)
* hair follicle keratinocyte (more specific subtypes vary by ontology version)

## 6. Environmental Information
No specific environmental, lifestyle, or infectious contributors were identified for KRT85-PHNED in the retrieved evidence. One family reported symptom worsening after febrile episodes. (amico2019compoundheterozygosityfor pages 1-3)

## 7. Anatomical Structures Affected

### 7.1 Organ/tissue level
Primary structures affected are **hair follicles** (hair shaft production) and **nail unit** (nail matrix/plate). KRT85 is described as a hair keratin expressed in hair matrix/precortex/cuticle; clinical findings are limited to hair and nails without broader ectodermal involvement in the cases described. (amico2019compoundheterozygosityfor pages 1-3, shimomura2010mutationsinthe pages 1-2)

### 7.2 Suggested UBERON terms
* hair follicle (UBERON:0002070)
* nail (UBERON:0001700)
* nail matrix (UBERON:0001524)

## 8. Temporal Development

* **Typical onset:** congenital/early life, with hair and nail dystrophy present since birth. (shimomura2010mutationsinthe pages 1-2)
* **Course:** appears lifelong, but some individuals may show partial improvement after puberty. (amico2019compoundheterozygosityfor pages 1-3)

No formal staging systems or longitudinal natural history cohorts were identified.

## 9. Inheritance and Population

### 9.1 Inheritance
Human reports support **autosomal recessive inheritance** for KRT85-PHNED. (naeem2006amutationin pages 1-2, shimomura2010mutationsinthe pages 1-2)

### 9.2 Epidemiology
No prevalence or incidence estimates specific to KRT85-PHNED were available in the retrieved evidence. A contemporary ectodermal dysplasia classification review highlights that many EDs are **ultra-rare** with **missing prevalence data** and may be underdiagnosed, while providing prevalence estimates for hypohidrotic ED as context (not for KRT85-PHNED). (peschel2022molecularpathwaybasedclassification pages 1-2)

### 9.3 Founder effects / carrier frequency
No carrier frequency estimates, founder effects, or population-based prevalence statistics for KRT85 pathogenic variants were identified in the retrieved evidence.

## 10. Diagnostics

### 10.1 Clinical diagnosis
Diagnosis is suspected clinically based on the combination of congenital hypotrichosis/alopecia and nail dystrophy with normal teeth and sweating and no major additional ectodermal findings. (shimomura2010mutationsinthe pages 1-2, amico2019compoundheterozygosityfor pages 1-3)

### 10.2 Genetic testing approaches (real-world implementations)
Evidence-supported approaches include:
* **Linkage mapping + candidate gene Sanger sequencing** in large pedigrees (historical approach). (naeem2006amutationin pages 1-2, shimomura2010mutationsinthe pages 1-2)
* **Targeted next-generation sequencing (NGS) panel testing**: a “gene chip-based next-generation sequencing” panel of 22 hypotrichosis genes was used to identify compound heterozygous KRT85 variants in siblings, enabling rapid molecular confirmation and informing genetic counseling. (amico2019compoundheterozygosityfor pages 1-3)

**Differential diagnosis (evidence-informed):** other “pure” hair–nail ectodermal dysplasias due to **HOXC13** or **KRT74**, and other congenital alopecia/hair-shaft disorders (e.g., monilethrix) are relevant considerations; within PHNED, genetic heterogeneity is emphasized. (amico2019compoundheterozygosityfor pages 1-3, lin2012lossoffunctionmutationsin pages 1-2)

## 11. Outcome / Prognosis

No mortality signal or systemic organ involvement is described in the retrieved KRT85-focused families; affected individuals are described as otherwise healthy with normal intelligence and normal routine lab tests in at least one large pedigree. (naeem2006amutationin pages 2-3)

Quantitative prognosis metrics (survival, morbidity indices) are not available from the retrieved evidence.

## 12. Treatment

### 12.1 Disease-modifying therapy
No disease-modifying pharmacologic, gene, or cell therapies were identified in the retrieved evidence for KRT85-PHNED.

### 12.2 Supportive care (evidence limits)
The retrieved primary literature and brief reports did not provide detailed management algorithms. The strongest evidence-based “intervention” discussed is **genetic counseling** enabled by molecular diagnosis. (amico2019compoundheterozygosityfor pages 1-3)

**Suggested MAXO terms (as knowledge-base annotations; not asserted as evidence-based efficacy):**
* genetic counseling (MAXO:0000747)
* molecular genetic testing (MAXO:0000059)
* wig/hair prosthesis use (supportive)
* nail care / protective measures (supportive)

## 13. Prevention

No primary prevention exists because the disorder is monogenic. Secondary/tertiary prevention is primarily through:
* **Carrier testing and cascade testing** in families once a pathogenic variant is identified (supported indirectly by segregation and counseling emphasis). (amico2019compoundheterozygosityfor pages 1-3)

## 14. Other Species / Natural Disease
No naturally occurring veterinary disease analogs for KRT85-PHNED were identified in the retrieved evidence.

## 15. Model Organisms
Direct KRT85 disease models were not identified in the retrieved evidence. However, the broader PHNED genetic landscape includes HOXC13-related models (e.g., Hoxc13 mutant mice) used to study hair/nail biology; these inform shared pathway biology but are not KRT85-specific. (lin2012lossoffunctionmutationsin pages 1-2)

## 16. Recent Developments (prioritizing 2023–2024)

* **2023–2024 primary human KRT85-PHNED reports:** A 2023 European Journal of Dermatology report (“Two homozygous KRT85 mutations in a Chinese patient…”, DOI: 10.1684/ejd.2023.4416) was surfaced by search but was **not obtainable** via the current toolchain, so its details cannot be verified/cited here.
* **Recent authoritative synthesis:** A 2022 expert-panel update on ectodermal dysplasia classification underscores the growing role of exome/genome analysis in improving diagnostic accuracy and notes that many EDs remain ultra-rare and underdiagnosed (contextual but not KRT85-specific). (peschel2022molecularpathwaybasedclassification pages 1-2)
* **Real-world diagnostic implementation trend:** The 2019 KRT85 compound heterozygosity report illustrates deployment of an NGS hypotrichosis gene panel in clinical practice to confirm diagnosis and guide counseling. (amico2019compoundheterozygosityfor pages 1-3)

## 17. Direct abstract-supported quotes (from retrieved evidence)
Because several key KRT85-PHNED papers were retrieved as full-text pages without clearly captured abstract fields, direct abstract quotations are limited. One available direct abstract quote relevant to “pure hair and nail ectodermal dysplasia” definition (not specific to KRT85 but defining PHNED) is:
* “Pure hair and nail ectodermal dysplasia (PHNED) comprises a heterogeneous group of rare heritable disorders characterized by brittle hair, hypotrichosis, onychodystrophy and micronychia.” (Raykova et al., 2014; KRT74-related PHNED subtype) (lin2012lossoffunctionmutationsin pages 1-2)

## 18. Key statistics/data points from primary studies
* Linkage strength in the original KRTHB5/KRT85 pedigree: maximum multipoint LOD reported as **8.2** (chromosome 12q12–q14.1 region). (naeem2006amutationin pages 1-2)
* Control screening: the KRT85/KRTHB5 **R78H** change was absent from **100 unrelated controls (200 chromosomes)** in the original report; the c.1448_1449delCT variant was absent from **100 healthy Pakistani controls** in a later report. (naeem2006amutationin pages 3-4, shimomura2010mutationsinthe pages 1-2)
* Population database check: two novel KRT85 variants in compound heterozygosity were reported absent from **gnomAD**. (amico2019compoundheterozygosityfor pages 1-3)

## 19. Expert opinion / authoritative analysis
An expert-panel ectodermal dysplasia classification update emphasizes that ED diagnosis based on phenotype alone is challenging and that exome/genome analysis improves diagnostic accuracy—supporting the shift toward molecular confirmation in rare EDs. (peschel2022molecularpathwaybasedclassification pages 1-2)

---

## Key References (with URLs and publication dates)
* Naeem M, et al. *J Med Genet.* 2006-08. “A mutation in the hair matrix and cuticle keratin KRTHB5 gene causes ectodermal dysplasia of hair and nail type.” https://doi.org/10.1136/jmg.2005.033381 (naeem2006amutationin pages 1-2)
* Shimomura Y, et al. *J Invest Dermatol.* Published online 2009-10-29; print 2010-03. “Mutations in the keratin 85 (KRT85/hHb5) gene underlie pure hair and nail ectodermal dysplasia.” https://doi.org/10.1038/jid.2009.341 (shimomura2010mutationsinthe pages 1-2)
* Amico S, et al. *JEADV.* 2019-07. “Compound heterozygosity for novel KRT85 variants associated with pure hair and nail ectodermal dysplasia.” https://doi.org/10.1111/jdv.15777 (amico2019compoundheterozygosityfor pages 1-3)
* Peschel N, et al. *Genes (Basel).* 2022-12-10. “Molecular Pathway-Based Classification of Ectodermal Dysplasias: First Five-Yearly Update.” https://doi.org/10.3390/genes13122327 (peschel2022molecularpathwaybasedclassification pages 1-2)

## Evidence limitations
* The tool-retrieved excerpts did not include PMIDs for key KRT85 papers; therefore, this report cites DOIs/URLs and the tool-provided context IDs.
* Several potentially relevant 2023–2024 KRT85 case reports were discovered but not obtainable in full text via tools, so they are not cited for factual claims.
* Prevalence/incidence, standardized diagnostic criteria, and treatment outcome statistics are not available from the retrieved disease-specific evidence.


References

1. (shimomura2010mutationsinthe pages 1-2): Yutaka Shimomura, Muhammad Wajid, Mazen Kurban, Nobuyuki Sato, and Angela M. Christiano. Mutations in the keratin 85 (krt85/hhb5) gene underlie pure hair and nail ectodermal dysplasia. The Journal of investigative dermatology, 130 3:892-5, Mar 2010. URL: https://doi.org/10.1038/jid.2009.341, doi:10.1038/jid.2009.341. This article has 50 citations.

2. (amico2019compoundheterozygosityfor pages 1-3): S. Amico, C. Ged, A. Taïeb, and F. Morice‐Picard. Compound heterozygosity for novel krt85 variants associated with pure hair and nail ectodermal dysplasia. Journal of the European Academy of Dermatology and Venereology, Jul 2019. URL: https://doi.org/10.1111/jdv.15777, doi:10.1111/jdv.15777. This article has 7 citations and is from a domain leading peer-reviewed journal.

3. (naeem2006amutationin pages 1-2): M. Naeem, M. Wajid, K. Lee, S. Leal, and W. Ahmad. A mutation in the hair matrix and cuticle keratin krthb5 gene causes ectodermal dysplasia of hair and nail type. Journal of Medical Genetics, 43:274-279, Aug 2006. URL: https://doi.org/10.1136/jmg.2005.033381, doi:10.1136/jmg.2005.033381. This article has 72 citations and is from a domain leading peer-reviewed journal.

4. (naeem2006amutationin pages 3-4): M. Naeem, M. Wajid, K. Lee, S. Leal, and W. Ahmad. A mutation in the hair matrix and cuticle keratin krthb5 gene causes ectodermal dysplasia of hair and nail type. Journal of Medical Genetics, 43:274-279, Aug 2006. URL: https://doi.org/10.1136/jmg.2005.033381, doi:10.1136/jmg.2005.033381. This article has 72 citations and is from a domain leading peer-reviewed journal.

5. (lin2012lossoffunctionmutationsin pages 1-2): Zhimiao Lin, Quan Chen, Lei Shi, Mingyang Lee, Kathrin A. Giehl, Zhanli Tang, Huijun Wang, Jie Zhang, Jinghua Yin, Lingshen Wu, Ruo Xiao, Xuanzhu Liu, Lanlan Dai, Xuejun Zhu, Ruoyu Li, Regina C. Betz, Xue Zhang, and Yong Yang. Loss-of-function mutations in hoxc13 cause pure hair and nail ectodermal dysplasia. American journal of human genetics, 91 5:906-11, Nov 2012. URL: https://doi.org/10.1016/j.ajhg.2012.08.029, doi:10.1016/j.ajhg.2012.08.029. This article has 87 citations and is from a highest quality peer-reviewed journal.

6. (naeem2006amutationin pages 2-3): M. Naeem, M. Wajid, K. Lee, S. Leal, and W. Ahmad. A mutation in the hair matrix and cuticle keratin krthb5 gene causes ectodermal dysplasia of hair and nail type. Journal of Medical Genetics, 43:274-279, Aug 2006. URL: https://doi.org/10.1136/jmg.2005.033381, doi:10.1136/jmg.2005.033381. This article has 72 citations and is from a domain leading peer-reviewed journal.

7. (shimomura2010mutationsinthe media b5f82a0b): Yutaka Shimomura, Muhammad Wajid, Mazen Kurban, Nobuyuki Sato, and Angela M. Christiano. Mutations in the keratin 85 (krt85/hhb5) gene underlie pure hair and nail ectodermal dysplasia. The Journal of investigative dermatology, 130 3:892-5, Mar 2010. URL: https://doi.org/10.1038/jid.2009.341, doi:10.1038/jid.2009.341. This article has 50 citations.

8. (shimomura2010mutationsinthe media a9ef3a76): Yutaka Shimomura, Muhammad Wajid, Mazen Kurban, Nobuyuki Sato, and Angela M. Christiano. Mutations in the keratin 85 (krt85/hhb5) gene underlie pure hair and nail ectodermal dysplasia. The Journal of investigative dermatology, 130 3:892-5, Mar 2010. URL: https://doi.org/10.1038/jid.2009.341, doi:10.1038/jid.2009.341. This article has 50 citations.

9. (peschel2022molecularpathwaybasedclassification pages 1-2): Nicolai Peschel, John T. Wright, Maranke I. Koster, Angus J. Clarke, Gianluca Tadini, Mary Fete, Smail Hadj-Rabia, Virginia P. Sybert, Johanna Norderyd, Sigrun Maier-Wohlfart, Timothy J. Fete, Nina Pagnan, Atila F. Visinoni, and Holm Schneider. Molecular pathway-based classification of ectodermal dysplasias: first five-yearly update. Genes, 13:2327, Dec 2022. URL: https://doi.org/10.3390/genes13122327, doi:10.3390/genes13122327. This article has 61 citations.