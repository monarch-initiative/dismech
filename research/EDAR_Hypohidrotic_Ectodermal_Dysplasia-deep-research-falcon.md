---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-24T18:06:32.181722'
end_time: '2026-04-24T18:18:37.772668'
duration_seconds: 725.59
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: EDAR-Related Hypohidrotic Ectodermal Dysplasia
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 48
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** EDAR-Related Hypohidrotic Ectodermal Dysplasia
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **EDAR-Related Hypohidrotic Ectodermal Dysplasia** covering all of the
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
- **Disease Name:** EDAR-Related Hypohidrotic Ectodermal Dysplasia
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **EDAR-Related Hypohidrotic Ectodermal Dysplasia** covering all of the
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


# EDAR-Related Hypohidrotic Ectodermal Dysplasia (EDAR-HED)

## Executive summary
EDAR-related hypohidrotic ectodermal dysplasia (EDAR-HED) is an autosomal dominant or autosomal recessive subtype within the broader group of hypohidrotic/anhidrotic ectodermal dysplasias (HED) characterized by impaired development of ectoderm-derived appendages—classically reduced sweating (hypohidrosis/anhidrosis), sparse hair (hypotrichosis), and missing/malformed teeth (hypodontia/oligodontia). EDAR encodes the ectodysplasin A receptor, a core component of the EDA–EDAR–EDARADD signaling module that activates NF-κB and related pathways during fetal ectodermal organ development. (salasalanis2015mutationsineda pages 1-3, higashino2017advancesinthe pages 12-16, reyes‐reali2018hypohidroticectodermaldysplasia pages 1-2)

A key 2023 mechanistic advance was the determination of the human EDA-A1–EDAR ligand–receptor complex crystal structure, providing an atomic-level explanation of how disease-causing variants disrupt binding and downstream NF-κB signaling. (yu2023structuralinsightsinto pages 1-3, yu2023structuralinsightsinto pages 3-4)

A major 2024 clinical development is the operationalization of phenotype-driven genomic testing strategies (targeted EDA/EDAR first-line for classic triad; WES/WGS and CNV-aware assays for atypical/negative cases), supported by quantitative yield data from a Korean cohort. (kim2024geneticprofilingand pages 1-2, kim2024geneticprofilingand pages 7-8)

## Quick reference (identifiers and core facts)
| Item | Key identifiers and core facts | Primary source | URL |
|---|---|---|---|
| Disease/term | EDAR-related hypohidrotic ectodermal dysplasia (HED); a subset of hypohidrotic ectodermal dysplasia involving pathogenic variants in **EDAR**; clinically overlaps with broader HED characterized by ectodermal appendage defects (higashino2017advancesinthe pages 12-16, reyes‐reali2018hypohidroticectodermaldysplasia pages 1-2) | Higashino et al. 2017; Reyes-Reali et al. 2018 | https://doi.org/10.1080/21678707.2017.1405806; https://doi.org/10.1111/ijd.14048 |
| MONDO ID | Broad disease: **hypohidrotic ectodermal dysplasia = MONDO_0016535**; EDAR-related disease maps most directly to **autosomal dominant hypohidrotic ectodermal dysplasia = MONDO_0015884** and **autosomal recessive hypohidrotic ectodermal dysplasia = MONDO_0016619**; Open Targets also lists **ectodermal dysplasia 10A, hypohidrotic/hair/nail type, autosomal dominant = MONDO_0007509** for EDAR-associated disease (martinezromero2019edaedaredaradd pages 1-2) | Open Targets disease-target associations | https://platform.opentargets.org |
| Gene(s) | Core pathway genes: **EDAR** (ectodysplasin A receptor), **EDARADD** (EDAR-associated death domain adaptor), **EDA** (ligand). EDAR is on **2q11-q13**; EDAR/EDARADD are autosomal pathway genes, while EDA is X-linked (salasalanis2015mutationsineda pages 1-3, ahmed2021genemutationsof pages 1-2, reyes‐reali2018hypohidroticectodermaldysplasia pages 1-2, martinezromero2019edaedaredaradd pages 1-2) | Salas-Alanis et al. 2015; Ahmed et al. 2021; Reyes-Reali et al. 2018; Martínez-Romero et al. 2019 | https://doi.org/10.5021/ad.2015.27.4.474; https://doi.org/10.3390/genes12091389; https://doi.org/10.1111/ijd.14048; https://doi.org/10.1186/s13023-019-1251-x |
| Inheritance patterns | HED may be **X-linked, autosomal dominant, or autosomal recessive**; **EDAR-related HED specifically occurs in autosomal dominant and autosomal recessive forms** (salasalanis2015mutationsineda pages 1-3, higashino2017advancesinthe pages 12-16, reyes‐reali2018hypohidroticectodermaldysplasia pages 1-2) | Salas-Alanis et al. 2015; Higashino et al. 2017; Reyes-Reali et al. 2018 | https://doi.org/10.5021/ad.2015.27.4.474; https://doi.org/10.1080/21678707.2017.1405806; https://doi.org/10.1111/ijd.14048 |
| Hallmark triad | **Hypohidrosis/anhidrosis**, **hypotrichosis** (sparse hair), and **hypodontia/anodontia/oligodontia** are the cardinal triad; additional features can include dry skin, dry eyes/airways, abnormal tooth shape, frontal bossing, saddle nose, prominent lips, and heat intolerance (salasalanis2015mutationsineda pages 1-3, ahmed2021genemutationsof pages 1-2, reyes‐reali2018hypohidroticectodermaldysplasia pages 2-4, reyes‐reali2018hypohidroticectodermaldysplasia pages 1-2) | Salas-Alanis et al. 2015; Ahmed et al. 2021; Reyes-Reali et al. 2018 | https://doi.org/10.5021/ad.2015.27.4.474; https://doi.org/10.3390/genes12091389; https://doi.org/10.1111/ijd.14048 |
| Key epidemiology figures from evidence | Reported figures vary by source and may reflect different definitions: **ectodermal dysplasias overall ~1.6 per 100,000** (kovalskaia2023molecularbasisand pages 2-4); **HED prevalence 1–9 per 100,000 births** (ahmed2021genemutationsof pages 1-2); **XLHED incidence 1/50,000–100,000 males** (martinezromero2019edaedaredaradd pages 1-2); **XLHED frequency ~1/17,000 live births** (reyes‐reali2018hypohidroticectodermaldysplasia pages 1-2); **HED ~7 per 10,000 live births** reported in one review (higashino2017advancesinthe pages 1-7) | Kovalskaia et al. 2023; Ahmed et al. 2021; Martínez-Romero et al. 2019; Reyes-Reali et al. 2018; Higashino et al. 2017 | https://doi.org/10.18699/vjgb-23-78; https://doi.org/10.3390/genes12091389; https://doi.org/10.1186/s13023-019-1251-x; https://doi.org/10.1111/ijd.14048; https://doi.org/10.1080/21678707.2017.1405806 |
| Key diagnostic yield stats (Korea cohort, 2024) | In 27 Korean ED patients, **overall molecular diagnostic yield = 74.1% (20/27)**; **EDA/EDAR variants accounted for 80% of positive cases (16/20)**; among patients with the complete hair/skin/dental triad, **94.1% (16/17)** had detectable **EDA/EDAR** mutations; among patients lacking the full triad, **0% (0/10)** had EDA/EDAR mutations; **23.1% (3/13) of EDA-positive cases had copy-number variants** (kim2024geneticprofilingand pages 1-2, kim2024geneticprofilingand pages 7-8, kim2024geneticprofilingand pages 2-4, kim2024geneticprofilingand pages 4-6, kim2024geneticprofilingand pages 6-7) | Kim et al. 2024 | https://doi.org/10.1186/s13023-024-03331-6 |
| Diagnostic approach implications | For **classical triad presentations**, targeted **EDA/EDAR** testing is recommended first-line; for atypical/non-triad cases, **WES** is preferred; CNV-aware methods such as **MLPA** should be considered when standard sequencing is negative, especially because **EDA CNVs** can be missed (reyes‐reali2018hypohidroticectodermaldysplasia pages 2-4, kim2024geneticprofilingand pages 1-2, kim2024geneticprofilingand pages 7-8, kim2024geneticprofilingand pages 2-4) | Reyes-Reali et al. 2018; Kim et al. 2024 | https://doi.org/10.1111/ijd.14048; https://doi.org/10.1186/s13023-024-03331-6 |
| Pathway role | EDAR is the receptor in the **EDA–EDAR–EDARADD–NF-κB** pathway. EDA binds EDAR, EDAR recruits EDARADD, and downstream signaling activates **NF-κB/JNK** to regulate development of hair follicles, teeth, nails, and eccrine sweat glands; disruption causes HED phenotypes (kovalskaia2023molecularbasisand pages 2-4, higashino2017advancesinthe pages 12-16, reyes‐reali2018hypohidroticectodermaldysplasia pages 1-2) | Kovalskaia et al. 2023; Higashino et al. 2017; Reyes-Reali et al. 2018 | https://doi.org/10.18699/vjgb-23-78; https://doi.org/10.1080/21678707.2017.1405806; https://doi.org/10.1111/ijd.14048 |


*Table: This table summarizes the main identifiers, inheritance, hallmark features, epidemiology, pathway biology, and diagnostic yield figures relevant to EDAR-related hypohidrotic ectodermal dysplasia. It is useful as a quick reference for disease knowledge-base curation and clinical interpretation.*

## 1. Disease information
### 1.1 Overview / definition
HED is described as a genetic disorder affecting ectoderm-derived structures (hair, teeth, eccrine sweat glands) and presenting with the classical triad of hypotrichosis, hypohidrosis/anhidrosis, and hypodontia/oligodontia. (salasalanis2015mutationsineda pages 1-3, reyes‐reali2018hypohidroticectodermaldysplasia pages 2-4, reyes‐reali2018hypohidroticectodermaldysplasia pages 1-2)

EDAR-related HED refers to HED caused by pathogenic variants in **EDAR** (ectodysplasin A receptor), producing autosomal dominant (AD) and autosomal recessive (AR) disease forms that are clinically largely indistinguishable from X-linked EDA-related HED. (salasalanis2015mutationsineda pages 1-3, higashino2017advancesinthe pages 12-16, reyes‐reali2018hypohidroticectodermaldysplasia pages 1-2)

### 1.2 Key identifiers
- **MONDO** (from Open Targets):
  - Hypohidrotic ectodermal dysplasia: **MONDO_0016535** (broad concept) (kovalskaia2023molecularbasisand pages 2-4)
  - Autosomal dominant hypohidrotic ectodermal dysplasia: **MONDO_0015884** (EDAR can be causal) (kovalskaia2023molecularbasisand pages 2-4)
  - Autosomal recessive hypohidrotic ectodermal dysplasia: **MONDO_0016619** (EDAR can be causal) (kovalskaia2023molecularbasisand pages 2-4)

**Not retrieved with the available tools in this run:** OMIM number(s), Orphanet identifier(s), ICD-10/ICD-11 codes, MeSH terms.

### 1.3 Synonyms / alternative names
- Hypohidrotic ectodermal dysplasia (HED)
- Anhidrotic ectodermal dysplasia / hypohidrotic-anhidrotic ED (used interchangeably in clinical literature) (salasalanis2015mutationsineda pages 1-3, reyes‐reali2018hypohidroticectodermaldysplasia pages 1-2)
- “ED/EDA” or “HED/EDA1” in some older usage, reflecting historical emphasis on the EDA pathway (reyes‐reali2018hypohidroticectodermaldysplasia pages 1-2)

### 1.4 Evidence type note (individual patient vs aggregated)
Evidence in the retrieved corpus is primarily **aggregated disease-level** review synthesis plus **cohort-based genetics studies** and **clinical trial registry records** (e.g., diagnostic yields, variant proportions, trial endpoints), rather than EHR-derived real-world datasets. (kim2024geneticprofilingand pages 1-2, NCT04980638 chunk 1, NCT02099552 chunk 1)

## 2. Etiology
### 2.1 Disease causal factors
EDAR-HED is a **monogenic developmental disorder** caused by germline pathogenic variants affecting the EDA signaling pathway. EDAR encodes the receptor for ectodysplasin A (EDA), and EDAR recruits the adaptor EDARADD to activate downstream signaling such as NF-κB and JNK/AP-1, crucial for ectodermal appendage development. (higashino2017advancesinthe pages 12-16, reyes‐reali2018hypohidroticectodermaldysplasia pages 1-2)

EDAR is located on chromosome **2q11–q13** (commonly cited as 2q11-q13 or 2q11–13). (salasalanis2015mutationsineda pages 1-3, ahmed2021genemutationsof pages 1-2, reyes‐reali2018hypohidroticectodermaldysplasia pages 1-2)

### 2.2 Risk factors
The dominant “risk factor” is **inheritance of a pathogenic EDAR variant** (AD or AR) or having a family history consistent with these patterns. HED overall can be X-linked, autosomal dominant, or autosomal recessive. (salasalanis2015mutationsineda pages 1-3, reyes‐reali2018hypohidroticectodermaldysplasia pages 1-2)

Population-level observations suggest that **consanguinity** may increase the contribution of autosomal recessive forms in some cohorts. (ahmed2021genemutationsof pages 1-2, guven2019turkishectodermaldysplasia pages 5-6)

### 2.3 Protective factors and gene–environment interactions
No protective genetic variants or robust gene–environment interaction mechanisms specific to EDAR-HED were identified in the retrieved sources.

## 3. Phenotypes
### 3.1 Core phenotypes and typical timing
HED is typically **congenital/early-onset**, though clinical diagnosis may be made “after infancy” once ectodermal features are evident. (reyes‐reali2018hypohidroticectodermaldysplasia pages 2-4)

The **cardinal triad** is:
- Reduced sweating (hypohidrosis/anhidrosis) (salasalanis2015mutationsineda pages 1-3, reyes‐reali2018hypohidroticectodermaldysplasia pages 1-2)
- Sparse/abnormal hair (hypotrichosis) (salasalanis2015mutationsineda pages 1-3, reyes‐reali2018hypohidroticectodermaldysplasia pages 1-2)
- Missing/malformed teeth (hypodontia/oligodontia; abnormal tooth shape) (salasalanis2015mutationsineda pages 1-3, ahmed2021genemutationsof pages 1-2)

### 3.2 Additional features and complications
Reported additional manifestations include dryness of skin/eyes/airways/mucous membranes; characteristic craniofacial features (e.g., frontal bossing, saddle nose, prominent lips); and in some cases fever, seizures, and rarely death (likely related to thermoregulation and systemic complications). (salasalanis2015mutationsineda pages 1-3, ahmed2021genemutationsof pages 1-2)

### 3.3 Quantitative phenotype-linked statistics (proxy for frequency)
A practical, clinically relevant “frequency” estimate comes from molecular-diagnostic stratification:
- In a Korean ectodermal dysplasia cohort (2018–2022), **94.1% (16/17)** of patients manifesting the complete **hair/skin/dental triad** had detectable **EDA/EDAR** mutations, versus **0% (0/10)** among those without the full triad; overall diagnostic yield was **74.1% (20/27)**. (kim2024geneticprofilingand pages 1-2, kim2024geneticprofilingand pages 7-8)

### 3.4 Quality of life (QoL)
Direct validated QoL scores (e.g., SF-36, EQ-5D, PROMIS) for EDAR-HED were not present in the retrieved evidence; however, trial outcomes and observational endpoints emphasize clinically meaningful impacts including thermoregulation, dry eye, salivation, eczema severity, and hospitalizations. (NCT04980638 chunk 1, NCT02099552 chunk 1)

### 3.5 Suggested HPO terms (non-exhaustive)
- Hypohidrosis: **HP:0000971**
- Anhidrosis: **HP:0000970**
- Hypotrichosis: **HP:0001006**
- Hypodontia: **HP:0000668**
- Oligodontia: **HP:0000677**
- Conical teeth: **HP:0000691**
- Heat intolerance: **HP:0002046**
- Xerosis cutis (dry skin): **HP:0000958**

## 4. Genetic / molecular information
### 4.1 Causal genes and pathway
- **EDAR** (ectodysplasin A receptor): receptor for EDA-A1; can cause both AD- and AR-HED. (higashino2017advancesinthe pages 12-16, reyes‐reali2018hypohidroticectodermaldysplasia pages 1-2)
- **EDARADD**: adaptor protein interacting with EDAR; part of the EDAR signaling complex. (higashino2017advancesinthe pages 12-16, salasalanis2015mutationsineda pages 1-3)
- **EDA**: ligand (classically X-linked HED), but mechanistically central to EDAR activation. (salasalanis2015mutationsineda pages 1-3, reyes‐reali2018hypohidroticectodermaldysplasia pages 1-2)

### 4.2 Pathogenic variant classes (EDAR)
A review summarizes that **>50 EDAR mutations** have been reported, predominantly missense/nonsense, with additional deletions, splice changes, insertions, and indels. (higashino2017advancesinthe pages 12-16)

### 4.3 Recent mechanistic advance (2023): atomic structure of EDA-A1–EDAR complex
Yu et al. (Nature Communications, **Feb 2023**, URL: https://doi.org/10.1038/s41467-023-36367-6) solved the EDA·A1 TNF homology domain (THD) bound to EDAR cysteine-rich domains (CRDs), providing a structural basis for ligand–receptor specificity and for interpreting pathogenic variants. (yu2023structuralinsightsinto pages 1-3)

Key findings include:
- A heterohexameric architecture (EDA trimer with three EDAR CRDs), solved at **2.8 Å**; binding affinity **KD ≈ 18.5 nM** by SPR. (yu2023structuralinsightsinto pages 3-4)
- Interface-pathogenic variants (e.g., A259E, D265G) can abolish interaction and reduce downstream signaling readouts (NF-κB reporter), explaining graded phenotypic severity. (yu2023structuralinsightsinto pages 4-6, yu2023structuralinsightsinto pages 7-9)

#### Visual evidence
Figure depicting the EDA-A1–EDAR complex structure and domain organization (Yu et al., 2023): (yu2023structuralinsightsinto media b524539c)

### 4.4 Modifier genes / epigenetics / chromosomal abnormalities
No EDAR-HED-specific modifier genes, epigenetic mechanisms, or recurrent chromosomal abnormalities were identified in the retrieved sources.

## 5. Environmental information
HED/EDAR-HED is primarily genetic. The retrieved sources focus on congenital developmental mechanisms rather than environmental triggers; no specific toxins, infections, lifestyle factors, or GxE interactions were supported by the retrieved evidence.

## 6. Mechanism / pathophysiology
### 6.1 Causal chain (upstream → downstream)
1. **Ligand–receptor step:** EDA (especially isoform EDA-A1) binds EDAR. (higashino2017advancesinthe pages 12-16, reyes‐reali2018hypohidroticectodermaldysplasia pages 1-2)
2. **Signalosome assembly:** EDAR recruits EDARADD and activates downstream signaling including NF-κB and JNK/AP-1. (higashino2017advancesinthe pages 12-16)
3. **Developmental outcome:** signaling drives epithelial–mesenchymal communication necessary for initiation/morphogenesis/differentiation of ectodermal organs (hair follicles, teeth, sweat glands, nails). (reyes‐reali2018hypohidroticectodermaldysplasia pages 1-2)
4. **Clinical phenotype:** impaired organogenesis yields the triad (hypohidrosis, hypotrichosis, hypodontia) and associated complications (dryness, heat intolerance, infections). (salasalanis2015mutationsineda pages 1-3, ahmed2021genemutationsof pages 1-2)

### 6.2 Suggested GO biological process terms
- NF-kappaB signaling: **GO:0043122** (regulation of IκB kinase/NF-κB signaling)
- Epithelial–mesenchymal signaling involved in organ morphogenesis: **GO:0002009** (morphogenesis of an epithelium) / **GO:0007423** (sensory organ development; for teeth/hair specialized ontologies may also apply)
- Hair follicle development: **GO:0001942**
- Tooth development: **GO:0042476**
- Sweat gland development: (may require more specific GO mapping depending on ontology versions)

### 6.3 Suggested CL cell types (examples)
- Keratinocyte: **CL:0000312** (epidermal keratinocyte)
- Dermal fibroblast / mesenchymal progenitors: e.g., fibroblast **CL:0000057**

### 6.4 Suggested UBERON anatomical structures
- Eccrine sweat gland: **UBERON:0002789**
- Tooth: **UBERON:0001091**
- Hair follicle: **UBERON:0002075**
- Skin: **UBERON:0002097**

## 7. Anatomical structures affected
Primary involvement includes ectoderm-derived appendages and glands: hair follicles, teeth, eccrine sweat glands, and other exocrine structures (lacrimal/salivary/bronchial glands highlighted in translational studies). (salasalanis2015mutationsineda pages 1-3, higashino2017advancesinthe pages 26-30)

## 8. Temporal development
The disorder is developmental/congenital, though clinical recognition may become apparent after infancy when ectodermal features can be assessed. (reyes‐reali2018hypohidroticectodermaldysplasia pages 2-4)

A key therapeutic implication of the developmental timing is that **earlier treatment (prenatal/perinatal) appears more effective** at rescuing organ development than later postnatal administration in models and early trials. (higashino2017advancesinthe pages 26-30)

## 9. Inheritance and population
### 9.1 Inheritance
HED occurs in X-linked, autosomal dominant, and autosomal recessive forms; EDAR is implicated in AD and AR forms. (salasalanis2015mutationsineda pages 1-3, reyes‐reali2018hypohidroticectodermaldysplasia pages 1-2)

### 9.2 Epidemiology (reported ranges; heterogeneous definitions)
Reported figures from the retrieved literature include:
- Ectodermal dysplasias overall: **~1.6 per 100,000** (kovalskaia2023molecularbasisand pages 2-4)
- HED prevalence: **1–9 per 100,000 births** (ahmed2021genemutationsof pages 1-2)
- XLHED incidence: **1/50,000–100,000 males** (martinezromero2019edaedaredaradd pages 1-2)
- XLHED frequency: **~1 per 17,000 live births** (reyes‐reali2018hypohidroticectodermaldysplasia pages 1-2)
- HED: **~7 per 10,000 live births** (higashino2017advancesinthe pages 1-7)

These estimates are not EDAR-specific and likely reflect different ascertainment and subtype definitions. (higashino2017advancesinthe pages 1-7, ahmed2021genemutationsof pages 1-2)

### 9.3 Population genetics signals for EDAR (cohort-based)
- In a Spanish cohort, EDAR variants comprised **7.8% (4/51)** of genetically solved cases. (martinezromero2019edaedaredaradd pages 2-4)
- In an Egyptian cohort, EDAR accounted for **~5%** of identified molecular causes. (ahmed2021genemutationsof pages 1-2)
- A Russian cohort reported recurrent EDAR alleles in multiple unrelated patients, suggesting regional enrichment (founder/recurrent effects), although formal founder analysis is not provided in the excerpt. (kovalskaia2026mutationalspectrumof pages 6-7)

## 10. Diagnostics
### 10.1 Clinical recognition and functional testing
- Sweat testing: starch–iodine testing can demonstrate hypohidrosis/anhidrosis; in affected individuals, the test can show “scarcity or absence of purple color,” while normal subjects develop purple coloration. (reyes‐reali2018hypohidroticectodermaldysplasia pages 2-4)
- Histopathology: biopsy can show orthokeratotic hypertrophy of stratum corneum and atrophic/immature eccrine sweat glands. (reyes‐reali2018hypohidroticectodermaldysplasia pages 2-4)

Additional sweat quantification methods and objective measures noted in a differential-diagnosis resource include pilocarpine-induced sweat measurement and sweat pore density assessment. (peschel2024differentialdiagnostischeeinordnungektodermaler pages 23-25)

### 10.2 Molecular confirmation (EDAR-relevant)
A diagnostic confirmation rule described in a clinical/molecular review: diagnosis can be confirmed by finding a hemizygous EDA variant in an affected male or **biallelic EDAR/EDARADD/WNT10A pathogenic variants** in an affected individual, consistent with autosomal recessive inheritance for those genes. (reyes‐reali2018hypohidroticectodermaldysplasia pages 2-4)

### 10.3 Testing strategy (recent implementation guidance, 2024)
In a Korean cohort (Orphanet Journal of Rare Diseases, **Sep 2024**, URL: https://doi.org/10.1186/s13023-024-03331-6), diagnostic yield data support:
- **Targeted EDA/EDAR sequencing** as first-line when the classical hair/skin/dental triad is present (high yield: 94.1%). (kim2024geneticprofilingand pages 6-7, kim2024geneticprofilingand pages 7-8)
- **WES** for cases lacking classic triad or with atypical involvement. (kim2024geneticprofilingand pages 7-8)
- Considering **CNV/structural variant detection** (e.g., MLPA, WGS) when classic phenotype is present but sequencing is negative, since CNVs may be missed. (kim2024geneticprofilingand pages 7-8)

A Spanish cohort similarly used Sanger sequencing plus MLPA across EDA/EDAR/EDARADD/WNT10A and emphasized the need for NGS to solve remaining cases. (martinezromero2019edaedaredaradd pages 1-2)

### 10.4 Differential diagnosis (syndromic overlaps)
Differential diagnosis includes other ED syndromes and ED-like disorders (e.g., TP63-related syndromes, IKBKG/NEMO-related immunodeficiency-associated ED, and other hair/tooth disorders). (higashino2017advancesinthe pages 16-21)

## 11. Outcome / prognosis
Specific EDAR-HED survival estimates were not identified in the retrieved sources. The retrieved clinical literature emphasizes morbidity related to thermoregulation, mucosal dryness, ocular and respiratory involvement, and dental function; these domains are reflected in natural history and clinical trial endpoints. (NCT04980638 chunk 1, NCT02099552 chunk 1)

## 12. Treatment
### 12.1 Current real-world management (supportive)
Supportive care is multidisciplinary and may include:
- Thermoregulation and heat-illness prevention strategies (inferred by emphasis on hypohidrosis/anhidrosis risk and early diagnosis). (higashino2017advancesinthe pages 12-16)
- Dental rehabilitation planning for hypodontia/oligodontia (not quantitatively detailed in the retrieved excerpts).
- Management of dry eye and other glandular dysfunction, reflected in trial outcome selection. (NCT04980638 chunk 1)

### 12.2 Disease-modifying / developmental therapies (clinical trials; largely XLHED-focused but pathway-relevant)
Although EDAR-HED is EDAR-driven and many interventional programs target EDA replacement (primarily XLHED), these efforts represent the most advanced pathway-directed translational work and are mechanistically relevant to EDAR signaling.

**Prenatal/perinatal EDA-A1 replacement (ER004/EDI200):**
- ClinicalTrials.gov **NCT04980638** (EspeRare Foundation; Phase 2; recruiting as of the record): intra-amniotic ER004 to male fetuses with XLHED; dosing 100 mg/kg estimated fetal weight per injection, three injections beginning at gestational week 26; primary endpoint mean sweat volume at 6 months; secondary endpoints include sweat pore density, dentition (erupted teeth, tooth germs), Meibomian glands, ocular surface, salivation, eczema severity (EASI), hospitalizations, and safety. (NCT04980638 chunk 1)

**Neonatal dosing trial:**
- ClinicalTrials.gov **NCT01775462** (Edimer Pharmaceuticals; Phase 2; completed): open-label dose-escalation EDI200 given to male neonates (48 hours to 14 days) with efficacy endpoints including dentition, craniofacial development, sweat duct density, sweat rate, dry eye measures, thermoregulation, and skin biopsy expression profiles. (NCT01775462 chunk 1)

**Adult safety/PK trial:**
- ClinicalTrials.gov **NCT01564225** (Edimer Pharmaceuticals; Phase 1; completed): adults with XLHED, focusing on safety/PK and exploratory ectodermal outcomes (hair, sweat duct density/rate, salivation, tearing, pulmonary markers). (NCT01564225 chunk 1)

**Expert analysis (timing as critical):**
A translational review notes that in models, prenatal/intra-amniotic delivery can rescue development more effectively, whereas postnatal human dosing showed limited improvements and was considered “too late” for certain structures. (higashino2017advancesinthe pages 26-30)

### 12.3 Suggested MAXO terms (examples)
- Genetic testing: **MAXO:0000127** (genetic test)
- Prenatal therapy / intra-amniotic drug administration: (MAXO mapping depends on the MAXO version; candidate: intra-amniotic administration)
- Protein replacement therapy (for ectodysplasin A1 replacement)
- Dental prosthetic rehabilitation / dental restoration (for hypodontia)

## 13. Prevention
Primary prevention of EDAR-HED is not currently feasible biologically (genetic etiology). Secondary/tertiary prevention focuses on early diagnosis to mitigate overheating risk and manage dental/ocular/skin complications, supported by recommendations for early genetic diagnosis and phenotype-driven testing. (higashino2017advancesinthe pages 12-16, kim2024geneticprofilingand pages 7-8)

Genetic counseling and prenatal diagnosis options are discussed in clinical reviews, including invasive prenatal testing options with counseling. (morandini2025ectodermaldysplasiaa pages 6-7)

## 14. Other species / natural disease
A translational review describes a naturally occurring canine X-linked HED model that closely mirrors human ectodermal phenotypes (absence of sweat glands; dental and bronchial gland abnormalities; infections), supporting comparative pathology and therapy testing. (higashino2017advancesinthe pages 26-30)

## 15. Model organisms
### 15.1 Mouse models (mechanism and therapy testing)
- Tabby mouse (EDA-deficient) is a canonical model for HED, with phenotypes in teeth, sweat glands, and hair, and is used to test EDA replacement and anti-EDAR agonist antibodies. (higashino2017advancesinthe pages 26-30, higashino2017advancesinthe pages 21-26)
- CRISPR-engineered Eda point-mutant mice (A259E, D265G, R276C) show graded phenotypes consistent with human severity differences; severe defects include loss of eccrine sweat glands and dental agenesis in knockout and D265G models. (yu2023structuralinsightsinto pages 7-9)

### 15.2 Canine model
A canine XLHED model is emphasized as phenotypically closer to humans than mice (notably secondary dentition and glandular phenotypes) and was used to evaluate postnatal EDA replacement effects on secondary dentition and glands. (higashino2017advancesinthe pages 26-30)

---

## Evidence gaps and limitations of this tool run
1. **PMIDs:** Many retrieved excerpts did not include PubMed IDs explicitly; therefore, PMIDs could not be reliably listed for most claims despite being derived from peer-reviewed articles. URLs/DOIs and publication months/years are provided where available. (yu2023structuralinsightsinto pages 1-3, kim2024geneticprofilingand pages 1-2)
2. **Disease identifiers:** OMIM/Orphanet/ICD/MeSH identifiers were not retrievable with the currently available tools.
3. **EDAR-specific epidemiology:** Most prevalence/incidence statistics are reported for HED overall or XLHED, not specifically EDAR-HED.

## Key references (most relevant, recent/high-authority)
- Yu K et al. *Nature Communications* (Feb 2023). “Structural insights into pathogenic mechanism of hypohidrotic ectodermal dysplasia caused by ectodysplasin A variants.” https://doi.org/10.1038/s41467-023-36367-6 (yu2023structuralinsightsinto pages 1-3)
- Kim MJ et al. *Orphanet Journal of Rare Diseases* (Sep 2024). “Genetic profiling and diagnostic strategies for patients with ectodermal dysplasias in Korea.” https://doi.org/10.1186/s13023-024-03331-6 (kim2024geneticprofilingand pages 1-2)
- ClinicalTrials.gov NCT04980638 (ER004 intra-amniotic; Phase 2). https://clinicaltrials.gov/study/NCT04980638 (NCT04980638 chunk 1)
- Reyes-Reali J et al. *International Journal of Dermatology* (May 2018). Clinical/molecular review and diagnostic testing. https://doi.org/10.1111/ijd.14048 (reyes‐reali2018hypohidroticectodermaldysplasia pages 2-4)
- Martínez-Romero MC et al. *Orphanet Journal of Rare Diseases* (Dec 2019). Spain cohort sequencing + MLPA. https://doi.org/10.1186/s13023-019-1251-x (martinezromero2019edaedaredaradd pages 1-2)


References

1. (salasalanis2015mutationsineda pages 1-3): Julio C Salas-Alanis, Eva Wozniak, Charles A Mein, Carola C Duran Mckinster, Jorge Ocampo-Candiani, David P Kelsell, Rong Hua, Maria L Garza-Rodriguez, Keith A Choate, and Hugo A Barrera Saldaña. Mutations in eda and edar genes in a large mexican hispanic cohort with hypohidrotic ectodermal dysplasia. Annals of Dermatology, 27:474-477, Jul 2015. URL: https://doi.org/10.5021/ad.2015.27.4.474, doi:10.5021/ad.2015.27.4.474. This article has 23 citations and is from a peer-reviewed journal.

2. (higashino2017advancesinthe pages 12-16): Toshihide Higashino, John Y. W. Lee, and John A. McGrath. Advances in the genetic understanding of hypohidrotic ectodermal dysplasia. Expert Opinion on Orphan Drugs, 5:967-975, Nov 2017. URL: https://doi.org/10.1080/21678707.2017.1405806, doi:10.1080/21678707.2017.1405806. This article has 2 citations.

3. (reyes‐reali2018hypohidroticectodermaldysplasia pages 1-2): Julia Reyes‐Reali, María Isabel Mendoza‐Ramos, Efraín Garrido‐Guerrero, Claudia F. Méndez‐Catalá, Adolfo R. Méndez‐Cruz, and Glustein Pozo‐Molina. Hypohidrotic ectodermal dysplasia: clinical and molecular review. International Journal of Dermatology, 57:965-972, May 2018. URL: https://doi.org/10.1111/ijd.14048, doi:10.1111/ijd.14048. This article has 124 citations and is from a peer-reviewed journal.

4. (yu2023structuralinsightsinto pages 1-3): Kang Yu, Chenhui Huang, Futang Wan, Cailing Jiang, Juan Chen, Xiuping Li, Feng Wang, Jian Wu, Ming Lei, and Yiqun Wu. Structural insights into pathogenic mechanism of hypohidrotic ectodermal dysplasia caused by ectodysplasin a variants. Nature Communications, Feb 2023. URL: https://doi.org/10.1038/s41467-023-36367-6, doi:10.1038/s41467-023-36367-6. This article has 28 citations and is from a highest quality peer-reviewed journal.

5. (yu2023structuralinsightsinto pages 3-4): Kang Yu, Chenhui Huang, Futang Wan, Cailing Jiang, Juan Chen, Xiuping Li, Feng Wang, Jian Wu, Ming Lei, and Yiqun Wu. Structural insights into pathogenic mechanism of hypohidrotic ectodermal dysplasia caused by ectodysplasin a variants. Nature Communications, Feb 2023. URL: https://doi.org/10.1038/s41467-023-36367-6, doi:10.1038/s41467-023-36367-6. This article has 28 citations and is from a highest quality peer-reviewed journal.

6. (kim2024geneticprofilingand pages 1-2): Man Jin Kim, Jee-Soo Lee, Seung Won Chae, Sung Im Cho, Jangsup Moon, Jung Min Ko, Jong-Hee Chae, and Moon-Woo Seong. Genetic profiling and diagnostic strategies for patients with ectodermal dysplasias in korea. Orphanet Journal of Rare Diseases, Sep 2024. URL: https://doi.org/10.1186/s13023-024-03331-6, doi:10.1186/s13023-024-03331-6. This article has 1 citations and is from a peer-reviewed journal.

7. (kim2024geneticprofilingand pages 7-8): Man Jin Kim, Jee-Soo Lee, Seung Won Chae, Sung Im Cho, Jangsup Moon, Jung Min Ko, Jong-Hee Chae, and Moon-Woo Seong. Genetic profiling and diagnostic strategies for patients with ectodermal dysplasias in korea. Orphanet Journal of Rare Diseases, Sep 2024. URL: https://doi.org/10.1186/s13023-024-03331-6, doi:10.1186/s13023-024-03331-6. This article has 1 citations and is from a peer-reviewed journal.

8. (martinezromero2019edaedaredaradd pages 1-2): M. C. Martínez-Romero, M. Ballesta-Martínez, V. López‐González, M. J. Sánchez-Soler, A. T. Serrano-Antón, M. Barreda-Sánchez, L. Rodríguez-Peña, M. T. Martínez-Menchon, J. Frías-Iniesta, P. Sánchez‐Pedreño, Pablo Carbonell-Meseguer, G. Glover-López, E. Guillén-Navarro, Rebeca Ana Jaime Blanca Angela Pablo Isabel Sabel Antonio Alcalá-García Barcia-Ramírez Cruz-Rojo Gener-Quero, Rebeca Alcalá-García, Ana Barcia-Ramírez, J. Cruz-Rojo, Blanca Gener-Querol, Á. Hernández-Martín, Pablo Lapunzina-Badía, Isabel Llanos-Rivas, Sabel Lorda-Sánchez, Antonio Martínez-Carrascal, J. Mascaró-Galy, L. Noguera‐Morel, M. A. Rodríguez-González, J. S. del Pozo, Verónica Seidel, A. Torrelo, and M. Trujillo-Tiebas. Eda, edar, edaradd and wnt10a allelic variants in patients with ectodermal derivative impairment in the spanish population. Orphanet Journal of Rare Diseases, Dec 2019. URL: https://doi.org/10.1186/s13023-019-1251-x, doi:10.1186/s13023-019-1251-x. This article has 53 citations and is from a peer-reviewed journal.

9. (ahmed2021genemutationsof pages 1-2): Hoda A. Ahmed, Ghada Y. El-Kamah, Eman Rabie, Mostafa I. Mostafa, Maha R. Abouzaid, Nehal F. Hassib, Mennat I. Mehrez, Mohamed A. Abdel-Kader, Yasmine H. Mohsen, Suher K. Zada, Khalda S. Amr, and Inas S. M. Sayed. Gene mutations of the three ectodysplasin pathway key players (eda, edar, and edaradd) account for more than 60% of egyptian ectodermal dysplasia: a report of seven novel mutations. Genes, 12:1389, Sep 2021. URL: https://doi.org/10.3390/genes12091389, doi:10.3390/genes12091389. This article has 26 citations.

10. (reyes‐reali2018hypohidroticectodermaldysplasia pages 2-4): Julia Reyes‐Reali, María Isabel Mendoza‐Ramos, Efraín Garrido‐Guerrero, Claudia F. Méndez‐Catalá, Adolfo R. Méndez‐Cruz, and Glustein Pozo‐Molina. Hypohidrotic ectodermal dysplasia: clinical and molecular review. International Journal of Dermatology, 57:965-972, May 2018. URL: https://doi.org/10.1111/ijd.14048, doi:10.1111/ijd.14048. This article has 124 citations and is from a peer-reviewed journal.

11. (kovalskaia2023molecularbasisand pages 2-4): V. A. Kovalskaia, T. Cherevatova, A. V. Polyakov, and O. P. Ryzhkova. Molecular basis and genetics of hypohidrotic ectodermal dysplasias. Vavilov Journal of Genetics and Breeding, 27:676-683, Nov 2023. URL: https://doi.org/10.18699/vjgb-23-78, doi:10.18699/vjgb-23-78. This article has 6 citations.

12. (higashino2017advancesinthe pages 1-7): Toshihide Higashino, John Y. W. Lee, and John A. McGrath. Advances in the genetic understanding of hypohidrotic ectodermal dysplasia. Expert Opinion on Orphan Drugs, 5:967-975, Nov 2017. URL: https://doi.org/10.1080/21678707.2017.1405806, doi:10.1080/21678707.2017.1405806. This article has 2 citations.

13. (kim2024geneticprofilingand pages 2-4): Man Jin Kim, Jee-Soo Lee, Seung Won Chae, Sung Im Cho, Jangsup Moon, Jung Min Ko, Jong-Hee Chae, and Moon-Woo Seong. Genetic profiling and diagnostic strategies for patients with ectodermal dysplasias in korea. Orphanet Journal of Rare Diseases, Sep 2024. URL: https://doi.org/10.1186/s13023-024-03331-6, doi:10.1186/s13023-024-03331-6. This article has 1 citations and is from a peer-reviewed journal.

14. (kim2024geneticprofilingand pages 4-6): Man Jin Kim, Jee-Soo Lee, Seung Won Chae, Sung Im Cho, Jangsup Moon, Jung Min Ko, Jong-Hee Chae, and Moon-Woo Seong. Genetic profiling and diagnostic strategies for patients with ectodermal dysplasias in korea. Orphanet Journal of Rare Diseases, Sep 2024. URL: https://doi.org/10.1186/s13023-024-03331-6, doi:10.1186/s13023-024-03331-6. This article has 1 citations and is from a peer-reviewed journal.

15. (kim2024geneticprofilingand pages 6-7): Man Jin Kim, Jee-Soo Lee, Seung Won Chae, Sung Im Cho, Jangsup Moon, Jung Min Ko, Jong-Hee Chae, and Moon-Woo Seong. Genetic profiling and diagnostic strategies for patients with ectodermal dysplasias in korea. Orphanet Journal of Rare Diseases, Sep 2024. URL: https://doi.org/10.1186/s13023-024-03331-6, doi:10.1186/s13023-024-03331-6. This article has 1 citations and is from a peer-reviewed journal.

16. (NCT04980638 chunk 1):  Intraamniotic Administrations of ER004 to Male Subjects With X-linked Hypohidrotic Ectodermal Dysplasia. EspeRare Foundation. 2022. ClinicalTrials.gov Identifier: NCT04980638

17. (NCT02099552 chunk 1):  Natural History and Outcomes in X-Linked Hypohidrotic Ectodermal Dysplasia. Edimer Pharmaceuticals. 2014. ClinicalTrials.gov Identifier: NCT02099552

18. (guven2019turkishectodermaldysplasia pages 5-6): Yeliz Güven, Elodie Bal, Umut Altunoglu, Esra Yücel, Smail Hadj-Rabia, Mine Koruyucu, Elif Bahar Tuna, Şule Çıldır, Oya Aktören, Christine Bodemer, Zehra O. Uyguner, Asma Smahi, and Hülya Kayserili. Turkish ectodermal dysplasia cohort: from phenotype to genotype in 17 families. Cytogenetic and Genome Research, 157:189-196, Apr 2019. URL: https://doi.org/10.1159/000499325, doi:10.1159/000499325. This article has 19 citations and is from a peer-reviewed journal.

19. (yu2023structuralinsightsinto pages 4-6): Kang Yu, Chenhui Huang, Futang Wan, Cailing Jiang, Juan Chen, Xiuping Li, Feng Wang, Jian Wu, Ming Lei, and Yiqun Wu. Structural insights into pathogenic mechanism of hypohidrotic ectodermal dysplasia caused by ectodysplasin a variants. Nature Communications, Feb 2023. URL: https://doi.org/10.1038/s41467-023-36367-6, doi:10.1038/s41467-023-36367-6. This article has 28 citations and is from a highest quality peer-reviewed journal.

20. (yu2023structuralinsightsinto pages 7-9): Kang Yu, Chenhui Huang, Futang Wan, Cailing Jiang, Juan Chen, Xiuping Li, Feng Wang, Jian Wu, Ming Lei, and Yiqun Wu. Structural insights into pathogenic mechanism of hypohidrotic ectodermal dysplasia caused by ectodysplasin a variants. Nature Communications, Feb 2023. URL: https://doi.org/10.1038/s41467-023-36367-6, doi:10.1038/s41467-023-36367-6. This article has 28 citations and is from a highest quality peer-reviewed journal.

21. (yu2023structuralinsightsinto media b524539c): Kang Yu, Chenhui Huang, Futang Wan, Cailing Jiang, Juan Chen, Xiuping Li, Feng Wang, Jian Wu, Ming Lei, and Yiqun Wu. Structural insights into pathogenic mechanism of hypohidrotic ectodermal dysplasia caused by ectodysplasin a variants. Nature Communications, Feb 2023. URL: https://doi.org/10.1038/s41467-023-36367-6, doi:10.1038/s41467-023-36367-6. This article has 28 citations and is from a highest quality peer-reviewed journal.

22. (higashino2017advancesinthe pages 26-30): Toshihide Higashino, John Y. W. Lee, and John A. McGrath. Advances in the genetic understanding of hypohidrotic ectodermal dysplasia. Expert Opinion on Orphan Drugs, 5:967-975, Nov 2017. URL: https://doi.org/10.1080/21678707.2017.1405806, doi:10.1080/21678707.2017.1405806. This article has 2 citations.

23. (martinezromero2019edaedaredaradd pages 2-4): M. C. Martínez-Romero, M. Ballesta-Martínez, V. López‐González, M. J. Sánchez-Soler, A. T. Serrano-Antón, M. Barreda-Sánchez, L. Rodríguez-Peña, M. T. Martínez-Menchon, J. Frías-Iniesta, P. Sánchez‐Pedreño, Pablo Carbonell-Meseguer, G. Glover-López, E. Guillén-Navarro, Rebeca Ana Jaime Blanca Angela Pablo Isabel Sabel Antonio Alcalá-García Barcia-Ramírez Cruz-Rojo Gener-Quero, Rebeca Alcalá-García, Ana Barcia-Ramírez, J. Cruz-Rojo, Blanca Gener-Querol, Á. Hernández-Martín, Pablo Lapunzina-Badía, Isabel Llanos-Rivas, Sabel Lorda-Sánchez, Antonio Martínez-Carrascal, J. Mascaró-Galy, L. Noguera‐Morel, M. A. Rodríguez-González, J. S. del Pozo, Verónica Seidel, A. Torrelo, and M. Trujillo-Tiebas. Eda, edar, edaradd and wnt10a allelic variants in patients with ectodermal derivative impairment in the spanish population. Orphanet Journal of Rare Diseases, Dec 2019. URL: https://doi.org/10.1186/s13023-019-1251-x, doi:10.1186/s13023-019-1251-x. This article has 53 citations and is from a peer-reviewed journal.

24. (kovalskaia2026mutationalspectrumof pages 6-7): Valeriia A. Kovalskaia, Tatiana B. Cherevatova, Elena V. Zinina, Olga A. Shagina, Ekaterina O. Vorontsova, Galina N. Matyushchenko, Nina A. Demina, Marina P. Petukhova, Tatiana V. Markova, Daria M. Guseva, Varvara A. Galkina, Inga V. Anisimova, Anna A. Stepanova, Alena L. Chuhrova, Margarita V. Sharova, Fatima M. Bostanova, Anahit E. Voskanyan, Aleksander V. Polyakov, and Oxana P. Ryzhkova. Mutational spectrum of eda, edar, edaradd, and wnt10a genes in the largest cohort of russian patients with hypohidrotic ectodermal dysplasia. Orphanet Journal of Rare Diseases, Feb 2026. URL: https://doi.org/10.1186/s13023-026-04211-x, doi:10.1186/s13023-026-04211-x. This article has 0 citations and is from a peer-reviewed journal.

25. (peschel2024differentialdiagnostischeeinordnungektodermaler pages 23-25): Nicolai Peschel. Differentialdiagnostische einordnung ektodermaler dysplasien auf der basis molekularer signalwege. Text, Jan 2024. URL: https://doi.org/10.25593/open-fau-805, doi:10.25593/open-fau-805. This article has 0 citations and is from a peer-reviewed journal.

26. (higashino2017advancesinthe pages 16-21): Toshihide Higashino, John Y. W. Lee, and John A. McGrath. Advances in the genetic understanding of hypohidrotic ectodermal dysplasia. Expert Opinion on Orphan Drugs, 5:967-975, Nov 2017. URL: https://doi.org/10.1080/21678707.2017.1405806, doi:10.1080/21678707.2017.1405806. This article has 2 citations.

27. (NCT01775462 chunk 1):  Phase 2 Study to Evaluate Safety, Pharmacokinetics, Immunogenicity and Pharmacodynamics/Efficacy of EDI200 in Male Infants With X-Linked Hypohidrotic Ectodermal Dysplasia (XLHED). Edimer Pharmaceuticals. 2013. ClinicalTrials.gov Identifier: NCT01775462

28. (NCT01564225 chunk 1):  A Phase 1, Open-label, Multicenter, Safety and Pharmacokinetic Study of EDI200. Edimer Pharmaceuticals. 2012. ClinicalTrials.gov Identifier: NCT01564225

29. (morandini2025ectodermaldysplasiaa pages 6-7): Ana Carolina Morandini, Oluwatomisin Adeogun, Megan Black, Emily Holman, Kaitlyn Collins, Wesley James, Laura Lally, Ashley Fordyce, Rachel Dobbs, Eve McDaniel, Hannah Putnam, and Michael Milano. Ectodermal dysplasia: a narrative review of the clinical and biological aspects relevant to oral health. Frontiers in Pediatrics, Feb 2025. URL: https://doi.org/10.3389/fped.2025.1523313, doi:10.3389/fped.2025.1523313. This article has 3 citations.

30. (higashino2017advancesinthe pages 21-26): Toshihide Higashino, John Y. W. Lee, and John A. McGrath. Advances in the genetic understanding of hypohidrotic ectodermal dysplasia. Expert Opinion on Orphan Drugs, 5:967-975, Nov 2017. URL: https://doi.org/10.1080/21678707.2017.1405806, doi:10.1080/21678707.2017.1405806. This article has 2 citations.