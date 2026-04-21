---
provider: falcon
model: Edison Scientific Literature
cached: true
start_time: '2026-04-17T09:12:57.342268'
end_time: '2026-04-17T09:12:57.345558'
duration_seconds: 0.0
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Pentanucleotide Repeat Familial Adult Myoclonus Epilepsy
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 58
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Pentanucleotide Repeat Familial Adult Myoclonus Epilepsy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Pentanucleotide Repeat Familial Adult Myoclonus Epilepsy** covering all of the
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
- **Disease Name:** Pentanucleotide Repeat Familial Adult Myoclonus Epilepsy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Pentanucleotide Repeat Familial Adult Myoclonus Epilepsy** covering all of the
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


# Comprehensive Research Report: Pentanucleotide Repeat Familial Adult Myoclonus Epilepsy (FAME/BAFME/FCMTE)

## Executive summary
Pentanucleotide repeat familial adult myoclonus epilepsy (FAME), also widely reported as benign adult familial myoclonic epilepsy (BAFME) or familial cortical myoclonic tremor with epilepsy (FCMTE), is an autosomal dominant epilepsy/movement disorder characterized by a cortical tremor/cortical myoclonus phenotype and infrequent generalized seizures. The defining molecular etiology is a *non-coding intronic pentanucleotide repeat expansion*—typically an expanded (TTTTA)n tract with an *inserted* (TTTCA)n (or related motifs such as ATTTC or TTTGA) occurring in multiple unrelated genes, suggesting a gene-independent repeat-toxicity mechanism. Recent work (2024) expanded the list of causal loci to include **RAI1** (BAFME8), emphasizing ongoing locus discovery and the diagnostic importance of long-read sequencing and repeat-primed PCR. (cuccurullo2023familialadultmyoclonus pages 1-2, corbett2023geneticsoffamilial pages 2-4, yeetong2024pentanucleotiderepeatinsertions pages 1-3)

## 1. Disease information

### 1.1 What is the disease?
FAME/BAFME/FCMTE is a rare, typically slowly progressive autosomal dominant disorder with a core phenotype of *cortical tremor and cortical myoclonus* and later-onset *epileptic seizures*. A 2023 review summarizes: “FAME is characterized by cortical tremor and myoclonus usually manifesting within the second decade of life, and infrequent seizures by the third or fourth decade.” (cuccurullo2023familialadultmyoclonus pages 1-2)

### 1.2 Synonyms and alternative names
Commonly used names/acronyms include:
- Familial adult myoclonus epilepsy (FAME) (cuccurullo2023familialadultmyoclonus pages 1-2, uzun2023familialadultmyoclonic pages 1-2)
- Benign adult familial myoclonic epilepsy (BAFME) (cuccurullo2023familialadultmyoclonus pages 1-2, depienne2023maagdenberg pages 1-3)
- Familial cortical myoclonic tremor with epilepsy (FCMTE) (yeetong2024pentanucleotiderepeatinsertions pages 1-3, depienne2023maagdenberg pages 1-3)
- Autosomal dominant cortical myoclonus and epilepsy (ADCME) (yeetong2024pentanucleotiderepeatinsertions pages 1-3)
- Familial essential myoclonus and epilepsy (FEME) (cuccurullo2023familialadultmyoclonus pages 1-2, uzun2023familialadultmyoclonic pages 1-2)

### 1.3 Key identifiers (OMIM, Orphanet, ICD, MeSH, MONDO)
In the retrieved evidence, *numeric* identifiers (OMIM/Orphanet/MONDO/ICD/MeSH codes) were not accessible. However, multiple sources explicitly describe classic linkage loci corresponding to historical subtype nomenclature:
- FAME1 (8q23.3–q24.1)
- FAME2 (2p11.1–q12.1)
- FAME3 (5p15.31–p15.1)
- FAME4 (3q26.32–3q28)
(cuccurullo2023familialadultmyoclonus pages 1-2)

### 1.4 Evidence source type
The current synthesis is derived primarily from *aggregated disease-level resources* (reviews and multi-family genetic studies) and also includes *pedigree-based primary human studies* (e.g., multi-generation families, segregation analyses). (cuccurullo2023familialadultmyoclonus pages 1-2, corbett2019intronicatttcrepeat pages 1-2, liu2020tttcarepeatexpansion pages 3-4)

## 2. Etiology

### 2.1 Disease causal factors (genetic/mechanistic)
FAME is a Mendelian disorder driven by *intronic non-coding repeat expansions* with common pathogenic motifs (TTTTA/TTTCA and related) inserted/expanded in multiple genes. A 2023 Cells review states: “the genetic mechanism underlying FAME consists of the expansion of similar non-coding pentanucleotide repeats, TTTCA and TTTTA, in different genes.” (cuccurullo2023familialadultmyoclonus pages 1-2)

Multiple lines of evidence support that the repeat itself is pathogenic and that simple loss-of-function of the host gene is unlikely:
- STARD7 FAME2 study reports RNA-seq in patient fibroblasts showing no accumulation of repeat RNA and no reduction of STARD7 expression, supporting a repeat-driven mechanism rather than straightforward gene expression loss. (corbett2019intronicatttcrepeat pages 1-2)
- RAI1 BAFME8 study reports leukocyte RAI1 RNA levels in affected individuals similar to controls and concludes “haploinsufficiency is unlikely to be the main pathomechanism of BAFME.” (yeetong2024pentanucleotiderepeatinsertions pages 1-3)

### 2.2 Risk factors
- **Genetic risk factor:** autosomal dominant inheritance with pathogenic repeat expansions. (cuccurullo2023familialadultmyoclonus pages 1-2, peters2022familialadultmyoclonic pages 1-2)
- **Trigger/risk modifiers for seizures:** photic stimulation, sleep deprivation, alcohol, and emotional stress are commonly reported triggers. (uzun2023familialadultmyoclonic pages 1-2, cuccurullo2023familialadultmyoclonus pages 4-6)

Environmental causal risk factors are not established in the available evidence.

### 2.3 Protective factors
No validated protective genetic or environmental factors were identified in the retrieved evidence.

### 2.4 Gene–environment interaction
No direct gene–environment interaction studies were identified in the retrieved evidence; however, seizures/myoclonus are often trigger-sensitive (photic stimulation, stress, alcohol, sleep deprivation), indicating that environmental exposures can modulate symptom expression in genetically affected individuals. (uzun2023familialadultmyoclonic pages 1-2, cuccurullo2023familialadultmyoclonus pages 4-6)

## 3. Phenotypes (clinical features)

### 3.1 Core phenotype
FAME is defined by cortical tremor and multifocal cortical myoclonus with distal predominance, often affecting hands/fingers and sometimes eyelids/face and lower limbs. (cuccurullo2023familialadultmyoclonus pages 4-6)

Seizures are typically less frequent than the movement phenotype; a 2023 review reports seizures can be infrequent, sometimes “5–10 episodes over a lifetime,” generally responsive to monotherapy. (cuccurullo2023familialadultmyoclonus pages 4-6)

### 3.2 Onset, progression, severity
- Onset is often in the **second decade**, but broad ranges are reported (e.g., 10–60 years; 3–70 years). (uzun2023familialadultmyoclonic pages 1-2, peters2022familialadultmyoclonic pages 1-2)
- Disease course is usually **slowly progressive** over decades. (peters2022familialadultmyoclonic pages 1-2, lagorio2019familialadultmyoclonic pages 2-3)
- Functional impact: progressive worsening of tremor/myoclonus can impair fine motor skills (writing, buttoning), and in advanced age may affect gait; frequent falls can impair quality of life. (cuccurullo2023familialadultmyoclonus pages 4-6, lagorio2019familialadultmyoclonic pages 2-3, uzun2023familialadultmyoclonic pages 1-2)

### 3.3 Comorbidities (expanded phenotype)
Reported comorbidities across pedigrees include migraine, psychiatric symptoms (anxiety/depression/personality traits), subtle cerebellar signs (postural ataxia; downbeat nystagmus), rare night blindness, and cognitive impairment especially in older individuals. (cuccurullo2023familialadultmyoclonus pages 4-6, uzun2023familialadultmyoclonic pages 1-2)

### 3.4 Neurophysiologic hallmarks supporting cortical origin
Multiple sources support cortical hyperexcitability with quantitative markers:
- EMG bursts ~15–60 ms (often ~50 ms). (peters2022familialadultmyoclonic pages 1-2, lagorio2019familialadultmyoclonic pages 2-3)
- Giant somatosensory evoked potentials (SEPs), with thresholds reported as N20–P25 >8.6 µV or P25–N33 >8.4 µV. (cuccurullo2023familialadultmyoclonus pages 6-7)
- Jerk-locked back averaging: cortical spikes preceding jerks (latency ≈20 ms hand; ≈30 ms leg). (cuccurullo2023familialadultmyoclonus pages 6-7)

### 3.5 Suggested HPO term mappings
A structured phenotype-to-HPO mapping based on the retrieved evidence is provided in the artifact table below.

| Phenotype (plain language) | Suggested HPO term(s) | Typical onset | Notes on frequency / severity / progression | Key supporting evidence / statistics | Supporting citations |
|---|---|---|---|---|---|
| Cortical tremor of hands/fingers, often tremor-like but irregular | HP:0001337 Tremor; HP:0002342 Action tremor | Usually 2nd decade; broader reported range 10–60 years or 3–70 years | Core and often first symptom; distal upper limbs predominate; can involve proximal arms and face; slowly progressive and impairs fine motor tasks such as writing/buttoning; often mistaken for essential tremor but lacks true rhythmicity and responds poorly to beta-blockers | Low-amplitude, continuous-arrhythmic finger movements; posture/action enhanced; may worsen with age; slow progression over decades; prevalence estimated <1/35,000 in reviews | (uzun2023familialadultmyoclonic pages 1-2, peters2022familialadultmyoclonic pages 1-2, cuccurullo2023familialadultmyoclonus pages 4-6, lagorio2019familialadultmyoclonic pages 2-3) |
| Multifocal cortical myoclonus | HP:0001336 Myoclonus; HP:0001251 Ataxia? | Usually after or with tremor in adolescence/young adulthood; second to third decade typical | Defining feature; multifocal jerks affect fingers, arms, axial muscles, eyelids, and legs; worsens gradually; can interfere with daily activities and occasionally gait in old age | EMG bursts typically ~15–60 ms, commonly ~50 ms; high-frequency arrhythmic/semi-rhythmic jerks around ~10/s; synchronous agonist/antagonist activation; triggered by posture, movement, tendon tap, and sensory stimuli | (peters2022familialadultmyoclonic pages 1-2, cuccurullo2023familialadultmyoclonus pages 4-6, lagorio2019familialadultmyoclonic pages 2-3, cuccurullo2023familialadultmyoclonus pages 6-7) |
| Generalized tonic-clonic seizures | HP:0002069 Generalized tonic-clonic seizure | Usually later than tremor/myoclonus, often 3rd–4th decade; adult onset common | Seizures are often less frequent than myoclonus; usually responsive to monotherapy, but refractory or drug-resistant cases occur in some families | Reported as relatively infrequent, ~5–10 lifetime episodes in review; in one Chinese pedigree all seizures were generalized tonic-clonic, 1–3/year, mean seizure onset 35 ± 5.52 years; GTCS frequency across families reported 15–100% in STARD7 paper summary | (cuccurullo2023familialadultmyoclonus pages 4-6, liu2020tttcarepeatexpansion pages 3-4, corbett2019intronicatttcrepeat pages 1-2) |
| Myoclonic seizures / myoclonic clusters | HP:0002123 Myoclonic seizure | Usually after onset of cortical tremor/myoclonus | Less common than cortical tremor; may precede bilateral tonic-clonic seizures and can cause falls in some patients | Reviews note myoclonic clusters preceding convulsive seizures and photic-provoked myoclonic seizures with falls in some pedigrees | (cuccurullo2023familialadultmyoclonus pages 4-6, cuccurullo2023familialadultmyoclonusa pages 4-6) |
| Photosensitivity / stimulus-sensitive attacks | HP:0000613 Photophobia; HP:0007348 Increased susceptibility to photic-induced seizures | Variable; usually after disease onset | Common trigger-related feature rather than constant phenotype | Triggers include photic stimulation, emotional stress, alcohol, and sleep deprivation; interictal generalized epileptiform discharges and photosensitivity may occur on EEG | (uzun2023familialadultmyoclonic pages 1-2, peters2022familialadultmyoclonic pages 1-2, cuccurullo2023familialadultmyoclonus pages 4-6, cuccurullo2023familialadultmyoclonus pages 6-7) |
| Cerebellar signs (postural ataxia, eye movement abnormalities) | HP:0001251 Ataxia; HP:0002418 Nystagmus; HP:0000648 Smooth pursuit pursuit interrupted? | Usually later in disease course, often subtle | Supportive but not universal; may emerge with progression, especially in older individuals | Reported subtle cerebellar signs include postural ataxia, downbeat nystagmus, and impaired smooth pursuit; walking impairment may occur in very old age but patients generally are not bedridden | (cuccurullo2023familialadultmyoclonus pages 4-6, cuccurullo2023familialadultmyoclonusa pages 4-6, lagorio2019familialadultmyoclonic pages 2-3) |
| Cognitive decline / memory-visuospatial impairment | HP:0001268 Mental deterioration; HP:0002354 Memory impairment | Usually late, especially older affected individuals | Not universal; slow progression when present | Reviews describe slow cognitive decline, visuospatial and memory deficits, and in some older patients slow-progressive dementia | (cuccurullo2023familialadultmyoclonus pages 4-6, cuccurullo2023familialadultmyoclonusa pages 4-6, lagorio2019familialadultmyoclonic pages 2-3) |
| Psychiatric symptoms (anxiety, depression, personality changes) | HP:0000739 Anxiety; HP:0000716 Depression | Variable, often recognized during chronic disease | Reported relatively frequently in some pedigrees; associated with poorer quality of life | Anxiety, depression, and personality traits reported; myoclonus severity correlated with anxiety; psychiatric burden can worsen functional impact and QoL | (cuccurullo2023familialadultmyoclonus pages 4-6, cuccurullo2023familialadultmyoclonusa pages 4-6, lagorio2019familialadultmyoclonic pages 2-3) |
| Migraine | HP:0002076 Migraine | Variable | Comorbidity; not core diagnostic feature | Reported in multiple pedigrees/reviews as part of expanded phenotype | (uzun2023familialadultmyoclonic pages 1-2, cuccurullo2023familialadultmyoclonus pages 4-6, lagorio2019familialadultmyoclonic pages 2-3) |
| Night blindness / retinal dysfunction | HP:0000662 Nyctalopia | Variable, uncommon | Rare associated phenotype | Review notes rare night blindness and reduced ERG b-wave in some families | (uzun2023familialadultmyoclonic pages 1-2, cuccurullo2023familialadultmyoclonus pages 4-6, cuccurullo2023familialadultmyoclonusa pages 4-6) |
| Falls / injury from myoclonus or seizures | HP:0002527 Falls | Later with progression or during provoked seizures | Important quality-of-life impact | Frequent falls can impair QoL; photic-induced myoclonic seizures may cause falls | (uzun2023familialadultmyoclonic pages 1-2, cuccurullo2023familialadultmyoclonusa pages 4-6) |
| EEG evidence of cortical hyperexcitability | HP:0010848 Abnormal EEG | Usually detectable after symptom onset; may evolve over years | Supportive diagnostic biomarker | EEG background may be normal early; later mild slowing occurs; generalized spike-wave frequency reported 4.3 ± 1.0 Hz; JLBA shows contralateral sensorimotor cortical spikes preceding jerks by ~20 ms in hand and ~30 ms in leg | (uzun2023familialadultmyoclonic pages 1-2, cuccurullo2023familialadultmyoclonus pages 1-2, cuccurullo2023familialadultmyoclonus pages 6-7) |
| Giant somatosensory evoked potentials (SEPs) | HP:0033694 Abnormal somatosensory evoked potentials | After symptom onset | Classic electrophysiologic hallmark of cortical myoclonus | Giant SEP thresholds reported as N20–P25 >8.6 µV or P25–N33 >8.4 µV; older review notes P25–N33 larger than 8.5–15 µV | (cuccurullo2023familialadultmyoclonus pages 1-2, lagorio2019familialadultmyoclonic pages 2-3, cuccurullo2023familialadultmyoclonus pages 6-7) |
| Enhanced long-latency reflex / C-reflex | HP:0034248 Abnormal long loop reflex? | After symptom onset | Supportive electrophysiologic sign of cortical origin | Presence of long-latency reflex I (C reflex) at rest or enhanced long-latency reflexes repeatedly cited as supportive of cortical tremor/myoclonus | (cuccurullo2023familialadultmyoclonus pages 1-2, lagorio2019familialadultmyoclonic pages 2-3, cuccurullo2023familialadultmyoclonus pages 6-7) |


*Table: This table summarizes the key clinical phenotypes and neurophysiologic hallmarks reported for pentanucleotide repeat familial adult myoclonus epilepsy (FAME/BAFME/FCMTE). It maps each phenotype to suggested HPO terms, typical onset, progression, quantitative supporting details, and the context citations available in this session.*

## 4. Genetic / molecular information

### 4.1 Causal genes and repeat motifs
FAME is genetically heterogeneous at the locus/gene level but mechanistically convergent on similar repeat expansions. A 2023 Epilepsia review summarizes the discovery of “noncoding TTTTA and inserted TTTCA pentanucleotide repeat expansions within six different genes to date (SAMD12, STARD7, MARCHF6, YEATS2, TNRC6A, and RAPGEF2).” (corbett2023geneticsoffamilial pages 1-2)

A key 2024 development is the identification of **RAI1** repeat insertions (BAFME8) in a Malian pedigree. (yeetong2024pentanucleotiderepeatinsertions pages 1-3)

A structured gene/motif/subtype table is provided here:

| Subtype name(s) | Locus / chromosome | Gene | Repeat motif configuration | Inheritance | Key supporting evidence | Key citations |
|---|---|---|---|---|---|---|
| FAME1 / BAFME1 / FCMTE1 | 8q23.3–q24.1; intron 4 locus on chr8 | SAMD12 | Expanded TTTTA with inserted TTTCA; rare alternative pathogenic configurations include TTTGA-containing insertions in some pedigrees | Autosomal dominant | Japanese consortium identified expansions in 85 affected individuals from 49 families; expansions ranged ~2.2–18.4 kb and TTTCA was absent in 1000 controls; additional Chinese pedigree showed cosegregation in all 12 living affected members, with maternal anticipation in 6 mother/child pairs; >200 families overall now genetically confirmed across FAME genes (scheffer2018thekeyto pages 2-2, liu2020tttcarepeatexpansion pages 1-3, corbett2023geneticsoffamilial pages 2-4) | Ishiura et al. 2018, Nat Genet, DOI: https://doi.org/10.1038/s41588-018-0067-2; Liu et al. 2020, Front Neurol, DOI: https://doi.org/10.3389/fneur.2020.00068; Corbett et al. 2023, Epilepsia, DOI: https://doi.org/10.1111/epi.17610 |
| FAME2 / BAFME2 / ADCME | 2p11.1–q12.1; chr2-linked locus | STARD7 | ATTTC expansion (reported with ATTTT/ATTTC context; review literature groups FAME motifs under TTTTA/TTTCA/ATTTC pentanucleotide expansions) | Autosomal dominant | ATTTC expansion in STARD7 segregated in 158/158 affected individuals from 22 pedigrees worldwide; RNA-seq from fibroblasts showed no reduction of STARD7 expression, supporting repeat-driven pathogenesis rather than simple loss of gene function (corbett2019intronicatttcrepeat pages 1-2, depienne2023maagdenberg pages 3-3) | Corbett et al. 2019, Nat Commun, DOI: https://doi.org/10.1038/s41467-019-12671-y |
| FAME3 / BAFME3 / FCMTE3 | 5p15.31–p15.1; first intron on chr5 | MARCHF6 (also written MARCH6/MARCHF6) | 5′-(TTTTA)exp(TTTCA)exp-3′; unstable mixed TTTTA/TTTCA expansion | Autosomal dominant | Identified in 4 European families; nanopore sequencing and molecular combing showed average expansion sizes ~3.3–14 kb; family-level evidence included 24 affected in one pedigree (16 sampled), 14 affected in another (9 sampled), and marked somatic instability with nearby micro-rearrangements in ~20% of cells (florian2019unstablettttatttcaexpansions pages 1-2, florian2019unstablettttatttcaexpansions pages 10-10) | Florian et al. 2019, Nat Commun, DOI: https://doi.org/10.1038/s41467-019-12763-9 |
| FAME4 / BAFME4 | 3q26.32–3q28 | YEATS2 | Review evidence states pathogenic intronic pentanucleotide repeat expansions of the FAME type (TTTTA with inserted TTTCA) occur in YEATS2 | Autosomal dominant | 2023 review lists YEATS2 among the six confirmed genes harboring FAME-causing noncoding pentanucleotide repeat expansions; no segregation counts were provided in the available evidence excerpt (corbett2023geneticsoffamilial pages 1-2, yeetong2024pentanucleotiderepeatinsertions pages 1-3) | Corbett et al. 2023, Epilepsia, DOI: https://doi.org/10.1111/epi.17610; Yeetong et al. 2024, Mov Disord, DOI: https://doi.org/10.1002/mds.29654 |
| FAME6 / BAFME6 | Not specified in available evidence excerpt | TNRC6A | Review evidence states pathogenic intronic pentanucleotide repeat expansions of the FAME type (TTTTA with inserted TTTCA); separate evidence notes nonpathogenic TTTTA expansion can occur at TNRC6A in some contexts | Autosomal dominant | Included among six confirmed FAME genes in 2023 review; available evidence excerpt does not provide family counts here, and one 2021 study noted associations between pathogenic SAMD12 TTTCA insertion and nonpathogenic TTTTA expansion in TNRC6A (corbett2023geneticsoffamilial pages 1-2) | Corbett et al. 2023, Epilepsia, DOI: https://doi.org/10.1111/epi.17610 |
| FAME7 / BAFME7 | Intron 14 locus (chromosome not specified in available evidence excerpt) | RAPGEF2 | Review evidence states pathogenic intronic pentanucleotide repeat expansions of the FAME type (TTTTA with inserted TTTCA) | Autosomal dominant | Included among six confirmed FAME genes; notable because the expansion is reported in intron 14 rather than intron 1/4 as in most other loci; no segregation counts available in the provided evidence excerpt (corbett2023geneticsoffamilial pages 2-4, corbett2023geneticsoffamilial pages 1-2) | Corbett et al. 2023, Epilepsia, DOI: https://doi.org/10.1111/epi.17610 |
| FAME8 / BAFME8 | Intron 4 of RAI1 | RAI1 | TTTTA repeat expansions with TTTCA repeat insertions | Autosomal dominant | Large Malian pedigree with 10 affected members; repeat changes in intron 4 of RAI1 co-segregated with disease; TTTCA repeats were absent in 200 Malian controls; somatic instability observed (yeetong2024pentanucleotiderepeatinsertions pages 1-3) | Yeetong et al. 2024, Mov Disord, DOI: https://doi.org/10.1002/mds.29654 |
| Variant motif pedigree within FAME1 spectrum | SAMD12 intron 4 | SAMD12 | TTTGA insertion/expansion reported instead of TTTCA in at least one large Chinese pedigree; review notes pathogenic expansions can include two or more motifs such as TTTCA and TTTGA | Autosomal dominant | Available review evidence states a 5′-(TTTTA)exp(TTTGA)exp-3′ configuration segregated with FAME in a large Chinese pedigree; this is presented as a rare motif variant within SAMD12-associated disease (depienne2023maagdenberg pages 4-4, yeetong2024pentanucleotiderepeatinsertions pages 1-3) | Yeetong et al. 2024, Mov Disord, DOI: https://doi.org/10.1002/mds.29654 |
| Distinct non-pentanucleotide-repeat entity sometimes labeled BAFME5 (not part of pentanucleotide-repeat FAME group) | Not specified in available evidence excerpt | CNTN2 | Homozygous frameshift variant; not a pentanucleotide repeat expansion | Autosomal recessive | 2024 review/evidence explicitly distinguishes BAFME5 as a recessive disorder caused by homozygous CNTN2 frameshift with adolescent-onset seizures then cortical myoclonus, unlike the dominant repeat-expansion forms above (yeetong2024pentanucleotiderepeatinsertions pages 1-3) | Yeetong et al. 2024, Mov Disord, DOI: https://doi.org/10.1002/mds.29654 |


*Table: This table summarizes the currently supported genetic etiologies for pentanucleotide-repeat familial adult myoclonus epilepsy syndromes, including subtype names, loci, genes, repeat configurations, inheritance, and supporting segregation evidence. It is useful for distinguishing confirmed repeat-expansion forms from related but genetically distinct entities.*

### 4.2 Pathogenic variant class, allele size, instability, and anticipation
The pathogenic lesion is best conceptualized as a structural variant: *intronic tandem repeat insertion/expansion*.

Quantitative data from the retrieved evidence include:
- **SAMD12 (FAME1/BAFME1):** expansions reported at 2.2–18.4 kb (≈440–3680 repeat units) in affected individuals; evidence of somatic instability; TTTCA absent in 1000 controls while TTTTA expansions present in 5.9% of controls. (scheffer2018thekeyto pages 2-2)
- **MARCHF6 (FAME3):** average expansion sizes ~3.3–14 kb; high somatic instability and micro-rearrangements near expansions in ~20% of cells. (florian2019unstablettttatttcaexpansions pages 1-2)
- **STARD7 (FAME2):** ATTTC expansions segregated in 158/158 affected individuals from 22 pedigrees. (corbett2019intronicatttcrepeat pages 1-2)

Anticipation/instability:
- Repeat length inversely correlated with age at onset in SAMD12-linked disease and intergenerational instability consistent with anticipation has been described. (scheffer2018thekeyto pages 2-2)
- A Chinese SAMD12 pedigree study reported clinical anticipation of tremor and seizures (average 14 years and 5 years, respectively) and molecular instability across transmissions; another Chinese pedigree also reported maternal anticipation. (liu2020tttcarepeatexpansion pages 3-4, liu2020tttcarepeatexpansion pages 1-3)

### 4.3 Modifier genes / epigenetics / chromosomal abnormalities
No specific modifier genes or epigenetic signatures were identified in the retrieved evidence. The expansion is frequently described as gene-independent in effect, though repeat length/configuration correlates with severity. (corbett2023geneticsoffamilial pages 1-2, depienne2023maagdenberg pages 4-4)

## 5. Environmental information
No established environmental causes are reported. However, symptom provocation by triggers (photic stimulation, alcohol, sleep deprivation, stress) is frequently described and is clinically relevant. (uzun2023familialadultmyoclonic pages 1-2, cuccurullo2023familialadultmyoclonus pages 4-6)

## 6. Mechanism / pathophysiology

### 6.1 Current mechanistic model (causal chain)
A convergent model supported by recent reviews and postmortem observations is:
1) Intronic pentanucleotide repeat insertion/expansion →
2) Transcription of repeat-containing RNA (UUUCA-containing RNAs in some subtypes) →
3) Formation of nuclear RNA foci and sequestration of RNA-binding proteins (RNA toxicity) →
4) Cerebellar pathology (including Purkinje cell loss in some pedigrees) and cerebello–thalamo–cortical network dysfunction →
5) Reduced sensorimotor cortical inhibition and cortical hyperexcitability →
6) Cortical tremor/cortical myoclonus and generalized seizures. (cuccurullo2023familialadultmyoclonus pages 9-10, cuccurullo2023familialadultmyoclonus pages 1-2)

### 6.2 RNA-mediated toxicity and cell types
Evidence from postmortem FAME1 brains shows RNA foci and repeats in both cortical neurons and cerebellar Purkinje cells, supporting involvement of these neuronal populations. (depienne2023maagdenberg pages 4-4)

Suggested cell type ontology (CL) terms (inferred from evidence mentioning these cell types):
- Purkinje cell: CL:0000121
- Cortical neuron (broad): CL:0000540 (generic neuron) / cortical pyramidal neuron terms may apply depending on specificity

### 6.3 Cerebellar–thalamic–cortical loop dysfunction
A 2023 Cells review emphasizes imaging and neuropathology suggesting cerebellar alterations and abnormal cerebello-cerebral connectivity, motivating a hypothesis of decreased sensorimotor cortical inhibition through dysfunction of the cerebellar–thalamic–cortical loop. (cuccurullo2023familialadultmyoclonus pages 1-2, cuccurullo2023familialadultmyoclonus pages 9-10)

### 6.4 Phase separation and broader repeat-expansion biology
A broader 2022 pentanucleotide-repeat review notes that RNA foci formation in repeat disorders has been linked to phase separation and perturbation of nuclear membraneless organelles. (loureiro2022molecularmechanismsin pages 1-3)

### 6.5 RAN translation (expert interpretation)
Repeat-associated non-AUG (RAN) translation is discussed as a plausible pathogenic mechanism for repeat disorders and is explicitly raised as a possibility for FAME repeats, but is also noted as **not yet demonstrated in FAME** in the retrieved excerpt. (depienne2023maagdenberg pages 5-6)

### 6.6 Suggested GO terms (biological process and cellular component)
Based on the described mechanisms (RNA foci, neuronal dysfunction, altered inhibition/circuitry), plausible GO terms include:
- GO:0003723 RNA binding (for sequestered RBPs; mechanistic context) (loureiro2022molecularmechanismsin pages 1-3)
- GO:0010608 posttranscriptional regulation of gene expression (repeat-RNA effects) (loureiro2022molecularmechanismsin pages 1-3)
- GO:0007611 learning or memory / GO:0007399 nervous system development (if pursuing cerebellar/cortical circuitry hypotheses)
- Cellular component terms relevant to RNA foci: nuclear speck / nucleus (broad)

These GO terms are suggested as ontology anchors; direct GO-annotated experimental evidence was not retrieved in this session.

## 7. Anatomical structures affected

### 7.1 Organ/system level
Primary system: nervous system. Evidence highlights:
- Sensorimotor cortex hyperexcitability (neurophysiology) (cuccurullo2023familialadultmyoclonus pages 6-7)
- Cerebellar involvement, including Purkinje cell loss and abnormal connectivity (cuccurullo2023familialadultmyoclonus pages 9-10)

Suggested UBERON terms:
- Cerebellum: UBERON:0002037
- Cerebral cortex: UBERON:0000956
- Thalamus: UBERON:0001898

### 7.2 Tissue/cell level
- Neuronal populations in cortex and cerebellum (including Purkinje cells) implicated by RNA foci and neuropathology. (depienne2023maagdenberg pages 4-4, cuccurullo2023familialadultmyoclonus pages 9-10)

### 7.3 Subcellular level
- Nucleus/nuclear RNA foci (repeat-RNA aggregates). (depienne2023maagdenberg pages 4-4, loureiro2022molecularmechanismsin pages 1-3)

## 8. Temporal development (natural history)
- Onset: typically adolescence/young adulthood (second decade), but can vary broadly (3–70 reported). (cuccurullo2023familialadultmyoclonus pages 1-2, peters2022familialadultmyoclonic pages 1-2)
- Course: slow progression over decades; worsening tremor/myoclonus, possible later ataxia/cognitive decline in some families. (cuccurullo2023familialadultmyoclonus pages 4-6, lagorio2019familialadultmyoclonic pages 2-3)
- Anticipation: some pedigrees show clinical anticipation; repeat length/configuration correlates with earlier onset and greater severity. (liu2020tttcarepeatexpansion pages 3-4, corbett2023geneticsoffamilial pages 1-2)

## 9. Inheritance and population

### 9.1 Inheritance pattern
Autosomal dominant inheritance is repeatedly emphasized across reviews and primary genetic studies. (cuccurullo2023familialadultmyoclonus pages 1-2, corbett2019intronicatttcrepeat pages 1-2, liu2020tttcarepeatexpansion pages 1-3)

### 9.2 Penetrance and expressivity
Reviews describe high penetrance but with variable expressivity, including individuals with cortical tremor without epilepsy in some pedigrees. (cuccurullo2023familialadultmyoclonus pages 1-2, florian2019unstablettttatttcaexpansions pages 10-10)

### 9.3 Epidemiology and distribution
- Prevalence is estimated as **<1/35,000** in two independent reviews. (uzun2023familialadultmyoclonic pages 1-2, peters2022familialadultmyoclonic pages 1-2)
- FAME occurs worldwide, with regional distributions by gene locus (e.g., SAMD12 predominating in Asian populations; FAME2/FAME3 more prominent in European cohorts in some summaries). (leitao2024identificationandcharacterization pages 3-6, corbett2023geneticsoffamilial pages 1-2)

### 9.4 Founder effects and repeat origin
A 2023 Epilepsia review reports founder-effect evidence and timing estimates:
- FAME1 expansion estimated ~16,800 years old and predicted to have arrived in Japan ~4,300 years ago. (corbett2023geneticsoffamilial pages 2-4)
- Founder effect evidence is reported for Italian FAME2 families. (corbett2023geneticsoffamilial pages 2-4)

## 10. Diagnostics

### 10.1 Clinical and electrophysiology
Diagnostic evaluation relies on recognition of cortical tremor/cortical myoclonus with supportive neurophysiology:
- JLBA, corticomuscular coherence, giant SEPs, and long-latency reflexes/C-reflex support cortical origin. (cuccurullo2023familialadultmyoclonus pages 1-2, cuccurullo2023familialadultmyoclonus pages 6-7)

### 10.2 Genetic testing strategy (repeat expansion testing)
A modern diagnostic strategy is often *multi-modal*:
1) **Clinical suspicion** based on phenotype + electrophysiology (giant SEPs, JLBA). (cuccurullo2023familialadultmyoclonus pages 6-7)
2) **Targeted repeat assays** (repeat-primed PCR) for known motifs/loci.
3) **Sequencing-based confirmation and characterization**:
   - Short-read WGS + repeat callers (ExpansionHunter, exSTRa) for screening/outlier detection, acknowledging limitations for long or complex repeats. (corbett2019intronicatttcrepeat pages 6-6, leitao2024identificationandcharacterization pages 10-12)
   - Long-read sequencing (ONT/PacBio HiFi) with enrichment or whole-genome approaches to size repeats, resolve motif interruptions, and detect mosaicism. (leitao2024identificationandcharacterization pages 8-10, yeetong2024pentanucleotiderepeatinsertions pages 3-5)

A key real-world implementation point is that conventional WES may miss these intronic repeats. In a Chinese pedigree study: “Neither causal mutations cosegregated with the disease in the family nor any novel mutation was identified through WES, while an abnormal TTTCA expansion in SAMD12 was identified by RP-PCR and then proved to be cosegregated in the pedigree.” (liu2020tttcarepeatexpansion pages 1-3)

### 10.3 Methods landscape (2024 update)
A 2024 methods review (Revue Neurologique; Leitão et al., May 2024; https://doi.org/10.1016/j.neurol.2024.03.005) summarizes trade-offs:
- RP-PCR: high-throughput screening but cannot accurately size expansions. (leitao2024identificationandcharacterization pages 8-10)
- Fragment analysis: sizing up to ~700–800 bp. (leitao2024identificationandcharacterization pages 8-10)
- Long-range PCR: amplifies ~10–15 kb with bias toward smaller alleles; useful when paired with long-read sequencing to resolve motif composition and mosaicism. (leitao2024identificationandcharacterization pages 8-10)
- Southern blot: sizes large expansions but laborious, requires large DNA amounts, lacks sequence context. (leitao2024identificationandcharacterization pages 8-10)
- Long-read sequencing: provides direct sizing and motif structure but requires high molecular weight DNA and sufficient coverage and is costlier. (leitao2024identificationandcharacterization pages 10-12)

### 10.4 Differential diagnosis (clinical)
FAME can be misdiagnosed as:
- Essential tremor (phenotypic overlap), but FAME tremor lacks true rhythmicity and has cortical neurophysiology. (cuccurullo2023familialadultmyoclonus pages 4-6)
- Juvenile myoclonic epilepsy and other myoclonic epilepsies; progressive myoclonic epilepsies. (uzun2023familialadultmyoclonic pages 1-2)

## 11. Outcome / prognosis
FAME is often described as “benign” historically, but multiple reviews emphasize slow progression and potential late complications:
- Gradual worsening of tremor/myoclonus with impaired fine motor skills; possible late ataxia or cognitive decline in some families; rare drug-resistant epilepsy and status epilepticus have been described. (lagorio2019familialadultmyoclonic pages 2-3, uzun2023familialadultmyoclonic pages 1-2)

Robust survival statistics and standardized QoL instruments (EQ-5D/SF-36) were not identified in the retrieved evidence.

## 12. Treatment

### 12.1 Pharmacotherapy (symptomatic)
Evidence from reviews supports:
- First-line anti-seizure medications: **valproate**, **levetiracetam**, and **benzodiazepines** for seizure and myoclonus control. (lagorio2019familialadultmyoclonic pages 2-3)
- Some agents may worsen myoclonus or precipitate severe events:
  - **Carbamazepine** and **gabapentin** reported in association with convulsive/status epilepticus in BAFME/FAME. (cuccurullo2023familialadultmyoclonusa pages 16-16, lagorio2019familialadultmyoclonic pages 2-3)
- Other symptomatic strategies:
  - A nationwide trial evaluated **piracetam** for myoclonus. (cuccurullo2023familialadultmyoclonusb pages 16-16)
  - Low-dose **perampanel** has been reported to improve refractory cortical myoclonus (review-cited). (cuccurullo2023familialadultmyoclonus pages 13-14)

Suggested MAXO terms (examples):
- Anti-epileptic drug therapy (MAXO:0000747; approximate)
- Benzodiazepine therapy (MAXO term selection depends on MAXO version)
- Repetitive transcranial magnetic stimulation (rTMS) (MAXO neuromodulation term)

### 12.2 Neuromodulation
Low-frequency repetitive TMS over premotor cortex “can improve cortical tremor” (review-cited). (cuccurullo2023familialadultmyoclonusb pages 16-16)

### 12.3 Disease-modifying / experimental approaches
Because RNA-mediated toxicity is the leading hypothesis, RNA-targeting approaches (e.g., antisense oligonucleotides; RNA-targeting Cas9) are discussed as conceptual future directions, but no FAME-specific clinical trials were identified in the retrieved evidence. (cuccurullo2023familialadultmyoclonusb pages 16-16)

### 12.4 Real-world implementation
Seizures often diminish with anti-seizure medications but may not fully cease, as described in a large SAMD12 family followed longitudinally. (zhou2021clinicalandgenomic pages 1-5)

## 13. Prevention
Primary prevention is not currently feasible for a dominantly inherited repeat-expansion disorder.

Applicable prevention strategies include:
- **Genetic counseling** and cascade testing in families once a pathogenic expansion is identified. (implied by autosomal dominant inheritance and repeat-based testing; (liu2020tttcarepeatexpansion pages 1-3))
- **Trigger avoidance** (sleep deprivation, photic stimulation, alcohol, stress) as a practical seizure prevention strategy. (uzun2023familialadultmyoclonic pages 1-2, cuccurullo2023familialadultmyoclonus pages 4-6)

## 14. Other species / natural disease
No naturally occurring veterinary analogs were identified in the retrieved evidence.

## 15. Model organisms
Direct model details were not retrievable in this session, but a 2023 mechanistic review notes that progress will require appropriate neuronal models and mentions animal models including mouse, Drosophila, and zebrafish as relevant platforms, and suggests iPSC-derived neurons for mechanistic study because peripheral tissues may not show repeat expression. (depienne2023maagdenberg pages 1-3)

## Recent developments (2023–2024 emphasis)
- **Genetics synthesis (2023):** comprehensive review of locus discovery, geographic distributions, instability, and diagnostic challenges. (Corbett et al., Apr 2023, Epilepsia; https://doi.org/10.1111/epi.17610) (corbett2023geneticsoffamilial pages 1-2)
- **Mechanistic synthesis (2023):** cerebellar–thalamic–cortical loop hypothesis and RNA-toxicity framing in FAME. (Cuccurullo et al., Jun 2023, Cells; https://doi.org/10.3390/cells12121617) (cuccurullo2023familialadultmyoclonus pages 9-10)
- **New locus discovery (2024):** RAI1 intronic TTTTA/TTTCA repeat insertions defining BAFME8 in an African pedigree. (Yeetong et al., Nov 2024, Movement Disorders; https://doi.org/10.1002/mds.29654) (yeetong2024pentanucleotiderepeatinsertions pages 1-3)
- **Diagnostics technology update (2024):** modern methodological landscape for repeat expansion discovery/validation, emphasizing long-read sequencing and limitations of short-read methods. (Leitão et al., May 2024, Revue Neurologique; https://doi.org/10.1016/j.neurol.2024.03.005) (leitao2024identificationandcharacterization pages 8-10, leitao2024identificationandcharacterization pages 10-12)

## Key verbatim evidence quotes (for knowledge-base curation)
> "the genetic mechanism underlying FAME consists of the expansion of similar non-coding pentanucleotide repeats, TTTCA and TTTTA, in different genes" [source: pqac-00000000] (cuccurullo2023familialadultmyoclonus pages 1-2)
> "FAME is characterized by cortical tremor and myoclonus usually manifesting within the second decade of life, and infrequent seizures by the third or fourth decade." [source: pqac-00000000] (cuccurullo2023familialadultmyoclonus pages 1-2)
> "The ATTTC expansions segregate in 158/158 individuals typically affected by FAME from 22 pedigrees" [source: pqac-00000001] (corbett2019intronicatttcrepeat pages 1-2)
> "TTTTA repeat expansions and TTTCA repeat insertions in intron 4 of the RAI1gene that co-segregated with disease status in this family." [source: pqac-00000009] (yeetong2024pentanucleotiderepeatinsertions pages 1-3)
> "Neither causal mutations cosegregated with the disease in the family nor any novel mutation was identified through WES, while an abnormal TTTCA expansion in SAMD12 was identified by RP-PCR and then proved to be cosegregated in the pedigree." [source: pqac-00000024] (liu2020tttcarepeatexpansion pages 1-3)
> "Using PacBio HiFi long-read whole-genome sequencing and the tandem repeat genotyping tool TRGT, we identified a pathogenic MARCHF6 intronic expansion." [source: pqac-00000017] (florian2019unstablettttatttcaexpansions pages 1-2)


*Blockquote: This artifact compiles verbatim quotes supporting the core genetics, phenotype, segregation evidence, recent RAI1 discovery, and modern diagnostic methods for pentanucleotide repeat familial adult myoclonus epilepsy.*

## Limitations of this report
- Numeric ontology/database identifiers (OMIM/Orphanet/MONDO/ICD/MeSH) could not be retrieved with the available tooling and evidence set.
- Some high-value 2023 Epilepsia review articles (neurophysiology, differential diagnosis, imaging/neuropathology, treatment options) were listed as unobtainable in the search results and thus could not be quoted directly.
- No FAME-specific interventional clinical trials were identified via ClinicalTrials.gov search because “FAME” is widely used as an unrelated acronym in trials; repeat-expansion targeted therapies remain conceptual in the retrieved evidence.


References

1. (cuccurullo2023familialadultmyoclonus pages 1-2): Claudia Cuccurullo, Pasquale Striano, and Antonietta Coppola. Familial adult myoclonus epilepsy: a non-coding repeat expansion disorder of cerebellar–thalamic–cortical loop. Cells, 12:1617, Jun 2023. URL: https://doi.org/10.3390/cells12121617, doi:10.3390/cells12121617. This article has 14 citations.

2. (corbett2023geneticsoffamilial pages 2-4): Mark A. Corbett, Christel Depienne, Liana Veneziano, Karl Martin Klein, Francesco Brancati, Renzo Guerrini, Federico Zara, Shoji Tsuji, and Jozef Gecz. Genetics of familial adult myoclonus epilepsy: from linkage studies to noncoding repeat expansions. Epilepsia, Apr 2023. URL: https://doi.org/10.1111/epi.17610, doi:10.1111/epi.17610. This article has 26 citations and is from a domain leading peer-reviewed journal.

3. (yeetong2024pentanucleotiderepeatinsertions pages 1-3): Patra Yeetong, Mohamed E. Dembélé, Monnat Pongpanich, Lassana Cissé, Chalurmpon Srichomthong, Alassane B. Maiga, Kékouta Dembélé, Adjima Assawapitaksakul, Salia Bamba, Abdoulaye Yalcouyé, Salimata Diarra, Samuel Ephrata Mefoung, Supphakorn Rakwongkhachon, Oumou Traoré, Siraprapa Tongkobpetch, Kenneth H. Fischbeck, William A. Gahl, Cheick O. Guinto, Vorasuk Shotelersuk, and Guida Landouré. Pentanucleotide repeat insertions in rai1 cause benign adult familial myoclonic epilepsy type 8. Movement Disorders, 39:164-172, Nov 2024. URL: https://doi.org/10.1002/mds.29654, doi:10.1002/mds.29654. This article has 26 citations and is from a highest quality peer-reviewed journal.

4. (uzun2023familialadultmyoclonic pages 1-2): GÜNEŞ ALTIOKKA UZUN and BETÜL BAYKAN. Familial adult myoclonic epilepsy: clinical and genetic approach to an under-recognized disease. Noro psikiyatri arsivi, 60 2:174-177, Jan 2023. URL: https://doi.org/10.29399/npa.28252, doi:10.29399/npa.28252. This article has 3 citations.

5. (depienne2023maagdenberg pages 1-3): C Depienne. Maagdenberg. Unknown journal, 2023.

6. (corbett2019intronicatttcrepeat pages 1-2): Mark A. Corbett, Thessa Kroes, Liana Veneziano, Mark F. Bennett, Rahel Florian, Amy L. Schneider, Antonietta Coppola, Laura Licchetta, Silvana Franceschetti, Antonio Suppa, Aaron Wenger, Davide Mei, Manuela Pendziwiat, Sabine Kaya, Massimo Delledonne, Rachel Straussberg, Luciano Xumerle, Brigid Regan, Douglas Crompton, Anne-Fleur van Rootselaar, Anthony Correll, Rachael Catford, Francesca Bisulli, Shreyasee Chakraborty, Sara Baldassari, Paolo Tinuper, Kirston Barton, Shaun Carswell, Martin Smith, Alfredo Berardelli, Renee Carroll, Alison Gardner, Kathryn L. Friend, Ilan Blatt, Michele Iacomino, Carlo Di Bonaventura, Salvatore Striano, Julien Buratti, Boris Keren, Caroline Nava, Sylvie Forlani, Gabrielle Rudolf, Edouard Hirsch, Eric Leguern, Pierre Labauge, Simona Balestrini, Josemir W. Sander, Zaid Afawi, Ingo Helbig, Hiroyuki Ishiura, Shoji Tsuji, Sanjay M. Sisodiya, Giorgio Casari, Lynette G. Sadleir, Riaan van Coller, Marina A. J. Tijssen, Karl Martin Klein, Arn M. J. M. van den Maagdenberg, Federico Zara, Renzo Guerrini, Samuel F. Berkovic, Tommaso Pippucci, Laura Canafoglia, Melanie Bahlo, Pasquale Striano, Ingrid E. Scheffer, Francesco Brancati, Christel Depienne, and Jozef Gecz. Intronic atttc repeat expansions in stard7 in familial adult myoclonic epilepsy linked to chromosome 2. Nature Communications, Oct 2019. URL: https://doi.org/10.1038/s41467-019-12671-y, doi:10.1038/s41467-019-12671-y. This article has 167 citations and is from a highest quality peer-reviewed journal.

7. (liu2020tttcarepeatexpansion pages 3-4): Chaorong Liu, Yanmin Song, Ying Yuan, Ying Peng, Nan Pang, Ranhui Duan, Wen Huang, Xuehui Qin, Wenbiao Xiao, Hongyu Long, Sha Huang, Pinting Zhou, Lili Long, and Bo Xiao. Tttca repeat expansion of samd12 in a new benign adult familial myoclonic epilepsy pedigree. Frontiers in Neurology, Feb 2020. URL: https://doi.org/10.3389/fneur.2020.00068, doi:10.3389/fneur.2020.00068. This article has 10 citations and is from a peer-reviewed journal.

8. (peters2022familialadultmyoclonic pages 1-2): Lorenz Peters, Christel Depienne, and Stephan Klebe. Familial adult myoclonic epilepsy (fame): clinical features, molecular characteristics, pathophysiological aspects and diagnostic work-up. Medizinische Genetik, 33:311-318, Dec 2022. URL: https://doi.org/10.1515/medgen-2021-2100, doi:10.1515/medgen-2021-2100. This article has 17 citations.

9. (cuccurullo2023familialadultmyoclonus pages 4-6): Claudia Cuccurullo, Pasquale Striano, and Antonietta Coppola. Familial adult myoclonus epilepsy: a non-coding repeat expansion disorder of cerebellar–thalamic–cortical loop. Cells, 12:1617, Jun 2023. URL: https://doi.org/10.3390/cells12121617, doi:10.3390/cells12121617. This article has 14 citations.

10. (lagorio2019familialadultmyoclonic pages 2-3): Ilaria Lagorio, Federico Zara, Salvatore Striano, and Pasquale Striano. Familial adult myoclonic epilepsy: a new expansion repeats disorder. Seizure, 67:73-77, Apr 2019. URL: https://doi.org/10.1016/j.seizure.2019.03.009, doi:10.1016/j.seizure.2019.03.009. This article has 30 citations.

11. (cuccurullo2023familialadultmyoclonus pages 6-7): Claudia Cuccurullo, Pasquale Striano, and Antonietta Coppola. Familial adult myoclonus epilepsy: a non-coding repeat expansion disorder of cerebellar–thalamic–cortical loop. Cells, 12:1617, Jun 2023. URL: https://doi.org/10.3390/cells12121617, doi:10.3390/cells12121617. This article has 14 citations.

12. (cuccurullo2023familialadultmyoclonusa pages 4-6): C Cuccurullo, P Striano, and A Coppola. Familial adult myoclonus epilepsy: a non-coding repeat expansion disorder of cerebellar–thalamic–cortical loop. cells 2023, 12, 1617. Unknown journal, 2023.

13. (corbett2023geneticsoffamilial pages 1-2): Mark A. Corbett, Christel Depienne, Liana Veneziano, Karl Martin Klein, Francesco Brancati, Renzo Guerrini, Federico Zara, Shoji Tsuji, and Jozef Gecz. Genetics of familial adult myoclonus epilepsy: from linkage studies to noncoding repeat expansions. Epilepsia, Apr 2023. URL: https://doi.org/10.1111/epi.17610, doi:10.1111/epi.17610. This article has 26 citations and is from a domain leading peer-reviewed journal.

14. (scheffer2018thekeyto pages 2-2): Ingrid E. Scheffer. The key to fame: intronic repeat expansions cause human epilepsies. Epilepsy Currents, 18:238-239, Jul 2018. URL: https://doi.org/10.5698/1535-7597.18.4.238, doi:10.5698/1535-7597.18.4.238. This article has 1 citations and is from a peer-reviewed journal.

15. (liu2020tttcarepeatexpansion pages 1-3): Chaorong Liu, Yanmin Song, Ying Yuan, Ying Peng, Nan Pang, Ranhui Duan, Wen Huang, Xuehui Qin, Wenbiao Xiao, Hongyu Long, Sha Huang, Pinting Zhou, Lili Long, and Bo Xiao. Tttca repeat expansion of samd12 in a new benign adult familial myoclonic epilepsy pedigree. Frontiers in Neurology, Feb 2020. URL: https://doi.org/10.3389/fneur.2020.00068, doi:10.3389/fneur.2020.00068. This article has 10 citations and is from a peer-reviewed journal.

16. (depienne2023maagdenberg pages 3-3): C Depienne. Maagdenberg. Unknown journal, 2023.

17. (florian2019unstablettttatttcaexpansions pages 1-2): Rahel T. Florian, Florian Kraft, Elsa Leitão, Sabine Kaya, Stephan Klebe, Eloi Magnin, Anne-Fleur van Rootselaar, Julien Buratti, Theresa Kühnel, Christopher Schröder, Sebastian Giesselmann, Nikolai Tschernoster, Janine Altmueller, Anaide Lamiral, Boris Keren, Caroline Nava, Delphine Bouteiller, Sylvie Forlani, Ludmila Jornea, Regina Kubica, Tao Ye, Damien Plassard, Bernard Jost, Vincent Meyer, Jean-François Deleuze, Yannick Delpu, Mario D. M. Avarello, Lisanne S. Vijfhuizen, Gabrielle Rudolf, Edouard Hirsch, Thessa Kroes, Philipp S. Reif, Felix Rosenow, Christos Ganos, Marie Vidailhet, Lionel Thivard, Alexandre Mathieu, Thomas Bourgeron, Ingo Kurth, Haloom Rafehi, Laura Steenpass, Bernhard Horsthemke, Samuel F. Berkovic, Francesca Bisulli, Francesco Brancati, Laura Canafoglia, Giorgio Casari, Renzo Guerrini, Hiroyuki Ishiura, Laura Licchetta, Davide Mei, Tommaso Pippucci, Lynette Sadleir, Ingrid E. Scheffer, Pasquale Striano, Paolo Tinuper, Shoji Tsuji, Federico Zara, Eric LeGuern, Karl Martin Klein, Pierre Labauge, Mark F. Bennett, Melanie Bahlo, Jozef Gecz, Mark A. Corbett, Marina A. J. Tijssen, Arn M. J. M. van den Maagdenberg, and Christel Depienne. Unstable tttta/tttca expansions in march6 are associated with familial adult myoclonic epilepsy type 3. Nature Communications, Oct 2019. URL: https://doi.org/10.1038/s41467-019-12763-9, doi:10.1038/s41467-019-12763-9. This article has 174 citations and is from a highest quality peer-reviewed journal.

18. (florian2019unstablettttatttcaexpansions pages 10-10): Rahel T. Florian, Florian Kraft, Elsa Leitão, Sabine Kaya, Stephan Klebe, Eloi Magnin, Anne-Fleur van Rootselaar, Julien Buratti, Theresa Kühnel, Christopher Schröder, Sebastian Giesselmann, Nikolai Tschernoster, Janine Altmueller, Anaide Lamiral, Boris Keren, Caroline Nava, Delphine Bouteiller, Sylvie Forlani, Ludmila Jornea, Regina Kubica, Tao Ye, Damien Plassard, Bernard Jost, Vincent Meyer, Jean-François Deleuze, Yannick Delpu, Mario D. M. Avarello, Lisanne S. Vijfhuizen, Gabrielle Rudolf, Edouard Hirsch, Thessa Kroes, Philipp S. Reif, Felix Rosenow, Christos Ganos, Marie Vidailhet, Lionel Thivard, Alexandre Mathieu, Thomas Bourgeron, Ingo Kurth, Haloom Rafehi, Laura Steenpass, Bernhard Horsthemke, Samuel F. Berkovic, Francesca Bisulli, Francesco Brancati, Laura Canafoglia, Giorgio Casari, Renzo Guerrini, Hiroyuki Ishiura, Laura Licchetta, Davide Mei, Tommaso Pippucci, Lynette Sadleir, Ingrid E. Scheffer, Pasquale Striano, Paolo Tinuper, Shoji Tsuji, Federico Zara, Eric LeGuern, Karl Martin Klein, Pierre Labauge, Mark F. Bennett, Melanie Bahlo, Jozef Gecz, Mark A. Corbett, Marina A. J. Tijssen, Arn M. J. M. van den Maagdenberg, and Christel Depienne. Unstable tttta/tttca expansions in march6 are associated with familial adult myoclonic epilepsy type 3. Nature Communications, Oct 2019. URL: https://doi.org/10.1038/s41467-019-12763-9, doi:10.1038/s41467-019-12763-9. This article has 174 citations and is from a highest quality peer-reviewed journal.

19. (depienne2023maagdenberg pages 4-4): C Depienne. Maagdenberg. Unknown journal, 2023.

20. (cuccurullo2023familialadultmyoclonus pages 9-10): Claudia Cuccurullo, Pasquale Striano, and Antonietta Coppola. Familial adult myoclonus epilepsy: a non-coding repeat expansion disorder of cerebellar–thalamic–cortical loop. Cells, 12:1617, Jun 2023. URL: https://doi.org/10.3390/cells12121617, doi:10.3390/cells12121617. This article has 14 citations.

21. (loureiro2022molecularmechanismsin pages 1-3): Joana R. Loureiro, Ana F. Castro, Ana S. Figueiredo, and Isabel Silveira. Molecular mechanisms in pentanucleotide repeat diseases. Cells, 11:205, Jan 2022. URL: https://doi.org/10.3390/cells11020205, doi:10.3390/cells11020205. This article has 36 citations.

22. (depienne2023maagdenberg pages 5-6): C Depienne. Maagdenberg. Unknown journal, 2023.

23. (leitao2024identificationandcharacterization pages 3-6): E. Leitão, C. Schröder, and C. Depienne. Identification and characterization of repeat expansions in neurological disorders: methodologies, tools, and strategies. Revue Neurologique, 180:383-392, May 2024. URL: https://doi.org/10.1016/j.neurol.2024.03.005, doi:10.1016/j.neurol.2024.03.005. This article has 20 citations and is from a peer-reviewed journal.

24. (corbett2019intronicatttcrepeat pages 6-6): Mark A. Corbett, Thessa Kroes, Liana Veneziano, Mark F. Bennett, Rahel Florian, Amy L. Schneider, Antonietta Coppola, Laura Licchetta, Silvana Franceschetti, Antonio Suppa, Aaron Wenger, Davide Mei, Manuela Pendziwiat, Sabine Kaya, Massimo Delledonne, Rachel Straussberg, Luciano Xumerle, Brigid Regan, Douglas Crompton, Anne-Fleur van Rootselaar, Anthony Correll, Rachael Catford, Francesca Bisulli, Shreyasee Chakraborty, Sara Baldassari, Paolo Tinuper, Kirston Barton, Shaun Carswell, Martin Smith, Alfredo Berardelli, Renee Carroll, Alison Gardner, Kathryn L. Friend, Ilan Blatt, Michele Iacomino, Carlo Di Bonaventura, Salvatore Striano, Julien Buratti, Boris Keren, Caroline Nava, Sylvie Forlani, Gabrielle Rudolf, Edouard Hirsch, Eric Leguern, Pierre Labauge, Simona Balestrini, Josemir W. Sander, Zaid Afawi, Ingo Helbig, Hiroyuki Ishiura, Shoji Tsuji, Sanjay M. Sisodiya, Giorgio Casari, Lynette G. Sadleir, Riaan van Coller, Marina A. J. Tijssen, Karl Martin Klein, Arn M. J. M. van den Maagdenberg, Federico Zara, Renzo Guerrini, Samuel F. Berkovic, Tommaso Pippucci, Laura Canafoglia, Melanie Bahlo, Pasquale Striano, Ingrid E. Scheffer, Francesco Brancati, Christel Depienne, and Jozef Gecz. Intronic atttc repeat expansions in stard7 in familial adult myoclonic epilepsy linked to chromosome 2. Nature Communications, Oct 2019. URL: https://doi.org/10.1038/s41467-019-12671-y, doi:10.1038/s41467-019-12671-y. This article has 167 citations and is from a highest quality peer-reviewed journal.

25. (leitao2024identificationandcharacterization pages 10-12): E. Leitão, C. Schröder, and C. Depienne. Identification and characterization of repeat expansions in neurological disorders: methodologies, tools, and strategies. Revue Neurologique, 180:383-392, May 2024. URL: https://doi.org/10.1016/j.neurol.2024.03.005, doi:10.1016/j.neurol.2024.03.005. This article has 20 citations and is from a peer-reviewed journal.

26. (leitao2024identificationandcharacterization pages 8-10): E. Leitão, C. Schröder, and C. Depienne. Identification and characterization of repeat expansions in neurological disorders: methodologies, tools, and strategies. Revue Neurologique, 180:383-392, May 2024. URL: https://doi.org/10.1016/j.neurol.2024.03.005, doi:10.1016/j.neurol.2024.03.005. This article has 20 citations and is from a peer-reviewed journal.

27. (yeetong2024pentanucleotiderepeatinsertions pages 3-5): Patra Yeetong, Mohamed E. Dembélé, Monnat Pongpanich, Lassana Cissé, Chalurmpon Srichomthong, Alassane B. Maiga, Kékouta Dembélé, Adjima Assawapitaksakul, Salia Bamba, Abdoulaye Yalcouyé, Salimata Diarra, Samuel Ephrata Mefoung, Supphakorn Rakwongkhachon, Oumou Traoré, Siraprapa Tongkobpetch, Kenneth H. Fischbeck, William A. Gahl, Cheick O. Guinto, Vorasuk Shotelersuk, and Guida Landouré. Pentanucleotide repeat insertions in rai1 cause benign adult familial myoclonic epilepsy type 8. Movement Disorders, 39:164-172, Nov 2024. URL: https://doi.org/10.1002/mds.29654, doi:10.1002/mds.29654. This article has 26 citations and is from a highest quality peer-reviewed journal.

28. (cuccurullo2023familialadultmyoclonusa pages 16-16): C Cuccurullo, P Striano, and A Coppola. Familial adult myoclonus epilepsy: a non-coding repeat expansion disorder of cerebellar–thalamic–cortical loop. cells 2023, 12, 1617. Unknown journal, 2023.

29. (cuccurullo2023familialadultmyoclonusb pages 16-16): C Cuccurullo, P Striano, and A Coppola. Familial adult myoclonus epilepsy: a non-coding repeat expansion disorder of cerebellar–thalamic–cortical loop. cells 2023, 12, 1617. Unknown journal, 2023.

30. (cuccurullo2023familialadultmyoclonus pages 13-14): Claudia Cuccurullo, Pasquale Striano, and Antonietta Coppola. Familial adult myoclonus epilepsy: a non-coding repeat expansion disorder of cerebellar–thalamic–cortical loop. Cells, 12:1617, Jun 2023. URL: https://doi.org/10.3390/cells12121617, doi:10.3390/cells12121617. This article has 14 citations.

31. (zhou2021clinicalandgenomic pages 1-5): Yongxing Zhou, Raman Sood, Qun Wang, Blake Carrington, Morgan Park, Alice C. Young, Daniel Birnbaum, Zhao Liu, Tetsuo Ashizawa, James C. Mullikin, Mohamad Z. Koubeissi, and Paul Liu. Clinical and genomic analysis of a large chinese family with familial cortical myoclonic tremor with epilepsy and <i>samd12</i> intronic repeat expansion. Epilepsia Open, 6:102-111, Feb 2021. URL: https://doi.org/10.1002/epi4.12450, doi:10.1002/epi4.12450. This article has 15 citations and is from a peer-reviewed journal.