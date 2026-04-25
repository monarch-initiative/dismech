---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-24T18:07:05.120559'
end_time: '2026-04-24T18:28:17.971839'
duration_seconds: 1272.85
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Odonto-Onycho-Dermal Dysplasia
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 22
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Odonto-Onycho-Dermal Dysplasia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Odonto-Onycho-Dermal Dysplasia** covering all of the
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
- **Disease Name:** Odonto-Onycho-Dermal Dysplasia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Odonto-Onycho-Dermal Dysplasia** covering all of the
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


## Comprehensive Research Report: Odonto-Onycho-Dermal Dysplasia (OODD)

### Target disease
**Odonto-onycho-dermal dysplasia (OODD)** is a rare **autosomal recessive ectodermal dysplasia** characterized by congenital abnormalities predominantly involving **teeth, nails, hair, skin, sweating, and tongue papillae**, and caused by **biallelic pathogenic variants in WNT10A**. (adaimy2007mutationinwnt10a pages 1-4, bohring2009wnt10amutationsare pages 1-3, yu2019distinctimpactsof pages 1-2)


## 1. Disease Information

### 1.1 Definition and overview
OODD is described in the original gene-discovery paper as “a rare autosomal recessive syndrome” with **dry hair, severe hypodontia, smooth tongue with marked reduction of fungiform and filiform papillae, onychodysplasia, keratoderma, and hyperhidrosis of palms and soles**. (adaimy2007mutationinwnt10a pages 1-4)

Bohring et al. similarly summarize OODD (MIM 257980) as an autosomal recessive ectodermal dysplasia with **severe oligodontia**, **nail dystrophy**, **hypotrichosis**, **smooth tongue with reduced papillae**, and **palmoplantar hyperkeratosis with altered sweating**. (bohring2009wnt10amutationsare pages 1-3)

### 1.2 Key identifiers (as available in retrieved sources)
- **OMIM/MIM disease number:** **257980** (OODD) (yu2019distinctimpactsof pages 1-2, bohring2009wnt10amutationsare pages 1-3)
- **Causal gene:** **WNT10A** (chromosome **2q35**) (yu2019distinctimpactsof pages 1-2, kalaszi2026casereportnovel pages 1-2)
- **OMIM/MIM gene number:** **WNT10A *606268** (yu2019distinctimpactsof pages 1-2, bohring2009wnt10amutationsare pages 1-3)

*Note:* Orphanet, ICD-10/ICD-11, and MeSH identifiers were not explicitly present in the retrieved excerpts and therefore cannot be reliably asserted from this evidence set.

### 1.3 Synonyms / alternative names
The retrieved primary OODD papers mainly use “odonto-onycho-dermal dysplasia (OODD)” and situate it within a broader **WNT10A phenotypic spectrum** that overlaps with other ectodermal dysplasias (including Schöpf–Schulz–Passarge syndrome). (bohring2009wnt10amutationsare pages 1-3, tardieu2017dentalandextra‐oral pages 1-3)

### 1.4 Evidence source type
The disease description and genotype–phenotype relationships in this report are derived from:
- **Human primary clinical genetics** (affected families, case series, multicenter cohorts, case reports) (adaimy2007mutationinwnt10a pages 1-4, bohring2009wnt10amutationsare pages 1-3, tardieu2017dentalandextra‐oral pages 10-13)
- **Model organism evidence** (mouse Wnt10a knockout and Wnt10a/Wnt10b double mutants) (tardieu2017dentalandextra‐oral pages 10-13, yoshinaga2023effectsofwnt10a pages 2-4)


## 2. Etiology

### 2.1 Disease causal factors
OODD is caused by **biallelic pathogenic variants in WNT10A**, consistent with **autosomal recessive inheritance**. (adaimy2007mutationinwnt10a pages 1-4, bohring2009wnt10amutationsare pages 1-3, yu2019distinctimpactsof pages 1-2)

- In the initial linkage and sequencing study, all affected individuals from three consanguineous families carried the same homozygous nonsense variant **c.697G>T (p.Glu233X)** in exon 3 of **WNT10A**, predicted to truncate the protein (232 aa vs 417 aa). (adaimy2007mutationinwnt10a pages 4-6)

### 2.2 Genetic risk factors and genotype–phenotype considerations
- **Biallelic WNT10A variants** are associated with syndromic ectodermal dysplasia phenotypes including OODD, and can produce **very severe permanent tooth agenesis**, including **anodontia of permanent teeth**. (yu2019distinctimpactsof pages 1-2)
- **Heterozygous WNT10A variants** can be associated with milder ectodermal findings or isolated dental anomalies; in one ED cohort, about **half of heterozygotes (53.8%)** showed phenotypic manifestations, with sex-biased expression. (bohring2009wnt10amutationsare pages 1-3)

### 2.3 Protective factors
No genetic or environmental protective factors were identified in the retrieved evidence specific to OODD.

### 2.4 Gene–gene (modifier) interactions and recent developments (2023–2024 prioritized)
Recent case-based evidence suggests modifier/digenic effects influencing severity:
- **2023 (Children)**: a patient with prominent dental phenotype and mild ectodermal signs carried **compound heterozygous WNT10A variants** (c.310C>T; p.Arg104Cys and c.742C>T; p.Arg248Ter) and was homozygous for an **EDAR polymorphism** (c.1109T>C; p.Val370Ala). The authors state the EDAR370A allele “**might also attenuate the severity of other ED signs**.” (garciamartinez2023dentalphenotypewith pages 1-2)
- **2024 (BMC Oral Health)**: in two brothers with HED due to an **EDA** variant (c.878T>G), the more severe tooth agenesis phenotype occurred in the sibling with additional **compound heterozygous WNT10A missense variants**, and the authors conclude: “**Compound heterozygous WNT10A missense variations may exacerbate the number of missing teeth in HED caused by EDA variation**.” (liu2024compoundheterozygouswnt10a pages 1-2)


## 3. Phenotypes

### 3.1 Core phenotype spectrum (current understanding)
Across primary reports, OODD involves ectoderm-derived tissues:
- **Dental:** severe hypodontia/oligodontia/tooth agenesis; peg-shaped/conical teeth; enamel hypoplasia; retained primary teeth; and other dental morphology anomalies. (adaimy2007mutationinwnt10a pages 1-4, yu2019distinctimpactsof pages 1-2, yu2019distinctimpactsof pages 2-3)
- **Nails:** dystrophy/onych(o)dysplasia. (yu2019distinctimpactsof pages 2-3, bohring2009wnt10amutationsare pages 1-3)
- **Hair:** sparse/dry/thin hair, hypotrichosis. (adaimy2007mutationinwnt10a pages 1-4, yu2019distinctimpactsof pages 1-2)
- **Skin/palms/soles:** palmoplantar keratoderma/hyperkeratosis; xerosis; sometimes erythematous/atrophic facial patches. (bohring2009wnt10amutationsare pages 1-3, yu2019distinctimpactsof pages 1-2)
- **Sweating:** hypo- and/or hyperhidrosis. (bohring2009wnt10amutationsare pages 3-5, yu2019distinctimpactsof pages 2-3)
- **Tongue:** smooth tongue due to reduced papillae. (adaimy2007mutationinwnt10a pages 1-4, bohring2009wnt10amutationsare pages 3-5)

### 3.2 Phenotype frequencies / statistics from available cohorts
- In a 4-patient OODD case series with bi-allelic WNT10A variants, **peg-shaped teeth, microdontia, severe attrition, and dystrophic nails were present in 4/4**, while palmar/plantar hyperkeratosis occurred in **3/4** and hypohidrosis in **2/4**. (yu2019distinctimpactsof pages 2-3)
- In a multicenter cohort of **41 patients with WNT10A mutations**, major skeletal/cartilaginous anomalies were observed in **4 patients (~10%)**. (tardieu2017dentalandextra‐oral pages 10-13)

### 3.3 Onset and progression
- Clinical manifestations begin during development and are often recognized in childhood (e.g., early dental referral at 23 months in a WNT10A-deficient case). (garciamartinez2023dentalphenotypewith pages 2-6)
- In one OODD family description, palmoplantar hyperkeratosis appeared “**at around age 3 years**,” while growth and mental development were normal. (adaimy2007mutationinwnt10a pages 1-4)

### 3.4 Quality of life impacts (as available)
Formal QoL instruments were not identified in the retrieved excerpts. However, cohort descriptions report functional burdens including **painful palmoplantar lacerations** and **discomfort at warm temperatures**, consistent with keratoderma and sweating dysfunction. (bohring2009wnt10amutationsare pages 3-5)

### 3.5 Suggested HPO mapping
A curated HPO mapping table is provided below.

| Domain | Clinical feature | Suggested HPO term(s) | Evidence/frequency | Notes |
|---|---|---|---|---|
| Dentition | Oligodontia / severe tooth agenesis | HP:0000677 Oligodontia; HP:0009804 Tooth agenesis | Core OODD feature across reports; in a 41-patient WNT10A cohort, mild-to-severe oligodontia was observed in all patients with biallelic WNT10A variants; WNT10A variants are common in selective tooth agenesis (35–50%) (tardieu2017dentalandextra‐oral pages 10-13, tardieu2017dentalandextra‐oral pages 1-3) | Typically congenital/developmental and recognized in childhood when eruption is delayed or teeth are found to be absent on imaging. Severity is variable but often lifelong. |
| Dentition | Missing permanent teeth / anodontia of permanent dentition | HP:0011064 Agenesis of permanent teeth; HP:0009804 Tooth agenesis | Yu et al. reported retention of primary teeth with missing permanent teeth in 4/4 OODD patients; bi-allelic WNT10A mutations can cause complete anodontia of permanent teeth (yu2019distinctimpactsof pages 2-3, yu2019distinctimpactsof pages 1-2) | Permanent dentition is often more severely affected than primary dentition; developmental, non-remitting course. |
| Dentition | Missing deciduous teeth | HP:0006483 Hypodontia of primary teeth | In Yu et al. 2019, congenitally missing deciduous teeth were present in all 4 patients, with counts of 4, 2, 2, and 5 missing primary teeth (yu2019distinctimpactsof pages 2-3) | Suggests developmental involvement begins early, although primary dentition may be less severely affected than permanent dentition. |
| Dentition | Peg-shaped / conical teeth | HP:0006481 Conical tooth; HP:0000698 Peg-shaped teeth | Peg-shaped teeth were present in 4/4 OODD patients in Yu et al. 2019; conical primary/permanent anterior teeth also documented in a 2023 WNT10A-deficient case (yu2019distinctimpactsof pages 2-3, garciamartinez2023dentalphenotypewith pages 2-6) | Usually evident at eruption in childhood; stable structural abnormality. |
| Dentition | Microdontia | HP:0009827 Microdontia | Present in 4/4 OODD patients in Yu et al. 2019 (yu2019distinctimpactsof pages 2-3) | Developmental size abnormality; often accompanies peg-shaped teeth. |
| Dentition | Enamel hypoplasia | HP:0006297 Enamel hypoplasia | Present in 3/4 OODD patients in Yu et al. 2019 (yu2019distinctimpactsof pages 2-3) | Developmental enamel defect; contributes to attrition and restorative needs. |
| Dentition | Severe tooth wear / attrition | HP:0031359 Abnormal tooth wear | Severe attrition was present in 4/4 OODD patients in Yu et al. 2019 (yu2019distinctimpactsof pages 2-3) | Likely secondary to abnormal enamel and tooth morphology; cumulative over time. |
| Dentition | Retained primary teeth / delayed eruption pattern | HP:0006335 Delayed eruption of teeth; HP:0006349 Retained primary teeth | Retention of primary teeth with absence of permanent successors emphasized in OODD reports; recent pediatric case required monitoring and prosthetic management for eruption problems (yu2019distinctimpactsof pages 2-3, nurrahma2023prostheticsmanagementof pages 1-2, garciamartinez2023dentalphenotypewith pages 2-6) | Usually identified in childhood; may require long-term dental monitoring and intervention. |
| Dentition | Abnormal primary molar morphology | HP:0006344 Abnormality of primary teeth; HP:0006489 Abnormal dental morphology | Documented in the 2023 case with irregular coronal morphology and highly divergent roots (garciamartinez2023dentalphenotypewith pages 2-6) | Developmental anomaly recognized radiographically/clinically in childhood. |
| Oral cavity | Smooth tongue / reduced lingual papillae | HP:0010298 Smooth tongue | Classic OODD feature in the original family descriptions and broader WNT10A cohorts; also reported in the 2023 case (adaimy2007mutationinwnt10a pages 6-7, bohring2009wnt10amutationsare pages 3-5, garciamartinez2023dentalphenotypewith pages 2-6) | Congenital or early-presenting ectodermal manifestation; generally persistent. |
| Nails | Nail dystrophy / onychodysplasia | HP:0002164 Nail dysplasia; HP:0008386 Onychodystrophy | Dystrophic nails were present in 4/4 OODD patients in Yu et al. 2019; nail dysplasia is a defining OODD feature in discovery and cohort reports (yu2019distinctimpactsof pages 2-3, adaimy2007mutationinwnt10a pages 1-4, bohring2009wnt10amutationsare pages 3-5) | Usually congenital or early childhood onset; persistent with variable severity. |
| Hair | Sparse hair / hypotrichosis | HP:0001006 Hypotrichosis; HP:0008070 Sparse scalp hair | Sparse or dry/thin hair is a core OODD feature; Yu et al. and multiple cohort reports describe sparse hair, while original families noted very slow-growing short hair (yu2019distinctimpactsof pages 1-2, bohring2009wnt10amutationsare pages 3-5, adaimy2007mutationinwnt10a pages 6-7) | Often apparent in infancy/childhood; chronic, non-progressive or slowly evolving. |
| Hair | Sparse eyebrows | HP:0000647 Sparse eyebrow | Reported in WNT10A/OODD spectrum cohorts and the 2023 case (bohring2009wnt10amutationsare pages 3-5, garciamartinez2023dentalphenotypewith pages 2-6) | Mild-to-moderate ectodermal manifestation; usually persistent. |
| Skin (palms/soles) | Palmoplantar keratoderma / hyperkeratosis | HP:0000982 Palmoplantar keratoderma; HP:0000957 Palmoplantar hyperkeratosis | In Yu et al. 2019, palmar hyperkeratosis occurred in 3/4 and plantar hyperkeratosis in 3/4; original and later cohorts describe palmoplantar keratoderma as characteristic (yu2019distinctimpactsof pages 2-3, adaimy2007mutationinwnt10a pages 1-4, bohring2009wnt10amutationsare pages 3-5) | Often develops in childhood; may be painful when severe and can impair comfort/walking. |
| Skin | Dry skin / xerosis | HP:0001021 Hyperkeratosis; HP:0000958 Dry skin | Dry skin/xerosis reported in WNT10A cohorts and classic OODD descriptions (bohring2009wnt10amutationsare pages 3-5, tardieu2017dentalandextra‐oral pages 10-13) | Chronic ectodermal sign; may fluctuate with environment but generally persistent. |
| Sweating | Hypohidrosis | HP:0000979 Hypohidrosis | Present in 2/4 OODD patients in Yu et al. 2019; sweating dysfunction is part of the OODD spectrum (yu2019distinctimpactsof pages 2-3, yu2019distinctimpactsof pages 1-2) | Variable expressivity; can contribute to heat intolerance. |
| Sweating | Hyperhidrosis (especially palms/soles) | HP:0000975 Hyperhidrosis; HP:0007428 Palmoplantar hyperhidrosis | Hyperhidrosis of palms and soles was part of the original OODD description and broader WNT10A cohort spectrum (adaimy2007mutationinwnt10a pages 1-4, bohring2009wnt10amutationsare pages 3-5) | Variable even within families; may be worse at night or in warm environments. |
| Face / skin | Facial telangiectasia / atrophic facial patches | HP:0001009 Telangiectasia; HP:0001070 Atrophic skin patches | Bohring and Yu describe erythematous/atrophic facial lesions; the 2023 WNT10A-deficient case had facial telangiectases (bohring2009wnt10amutationsare pages 3-5, yu2019distinctimpactsof pages 1-2, garciamartinez2023dentalphenotypewith pages 2-6) | Variable and not universal; tends to be a stable ectodermal skin finding. |
| Functional impact | Painful fissures/lacerations of palms/soles | HP:0001071 Fissured skin | Painful palmoplantar lacerations were described in the WNT10A cohort spectrum (bohring2009wnt10amutationsare pages 3-5) | Important quality-of-life impact when keratoderma is severe; may affect mobility/manual function. |
| Functional impact | Heat intolerance / discomfort in warm temperatures | HP:0002046 Heat intolerance | Reported in cohort descriptions as discomfort at temperatures above 25°C in some affected individuals (bohring2009wnt10amutationsare pages 3-5) | Likely related to sweating dysfunction; episodic environmental trigger rather than progressive disease feature. |


*Table: This table maps major odonto-onycho-dermal dysplasia features to suggested HPO terms using only the cited evidence. It highlights which findings are core versus variable, and includes available frequency data such as the 4-patient OODD series from Yu et al. 2019.*


## 4. Genetic / Molecular Information

### 4.1 Causal gene
- **WNT10A** is the causal gene for OODD. (adaimy2007mutationinwnt10a pages 1-4, bohring2009wnt10amutationsare pages 1-3)

### 4.2 Pathogenic variants (examples from primary literature)
Reported OODD-associated WNT10A variants span nonsense and frameshift loss-of-function and deleterious missense alleles.

Key examples from the retrieved evidence include:
- **c.697G>T (p.Glu233X)** recurrent homozygous nonsense variant in Lebanese families (2007). (adaimy2007mutationinwnt10a pages 4-6)
- Additional variants reported in a 2009 spectrum study (e.g., **c.27G>A (p.W9X)**; **c.321C>A (p.C107X)**; **c.1128C>A (p.C376X)**; **c.383G>A (p.R128Q)**; **c.682T>A (p.F228I)**). (bohring2009wnt10amutationsare pages 1-3)
- 2019 report of **five novel variants**, including truncating and frameshift alleles (e.g., **c.742C>T (p.Arg248*)**, **c.1176C>A (p.Cys392*)**, **c.898-899delAT (p.Ile300Profs*126)**). (yu2019distinctimpactsof pages 1-2)

A concise evidence-constrained variant table is provided below.

| Category | Item | Details | Publication / URL | Evidence |
|---|---|---|---|---|
| Identifier | Disease name | Odonto-onycho-dermal dysplasia (OODD) | Adaimy et al., 2007; https://doi.org/10.1086/520064 | (yu2019distinctimpactsof pages 1-2, adaimy2007mutationinwnt10a pages 1-4) |
| Identifier | OMIM/MIM disease number | MIM/OMIM #257980 | Yu et al., 2019; https://doi.org/10.1002/ajmg.a.60682 | (yu2019distinctimpactsof pages 1-2, bohring2009wnt10amutationsare pages 1-3) |
| Genetic basis | Inheritance | Autosomal recessive | Adaimy et al., 2007; https://doi.org/10.1086/520064 | (yu2019distinctimpactsof pages 1-2, adaimy2007mutationinwnt10a pages 1-4, bohring2009wnt10amutationsare pages 1-3) |
| Genetic basis | Causal gene | WNT10A | Adaimy et al., 2007; https://doi.org/10.1086/520064 | (yu2019distinctimpactsof pages 1-2, adaimy2007mutationinwnt10a pages 1-4, bohring2009wnt10amutationsare pages 1-3) |
| Genetic basis | WNT10A OMIM gene number | OMIM/MIM *606268 | Yu et al., 2019; https://doi.org/10.1002/ajmg.a.60682 | (yu2019distinctimpactsof pages 1-2, bohring2009wnt10amutationsare pages 1-3) |
| Clinical features | Hallmark features | Severe hypodontia/oligodontia or tooth agenesis, peg-shaped/conical teeth, enamel hypoplasia, retained primary teeth, nail dystrophy/onychodysplasia, dry or sparse hair/hypotrichosis, palmoplantar keratoderma/hyperkeratosis, sweating abnormalities (hyperhidrosis or hypohidrosis), smooth tongue with reduced papillae | Adaimy et al., 2007; https://doi.org/10.1086/520064 | (yu2019distinctimpactsof pages 1-2, adaimy2007mutationinwnt10a pages 1-4, bohring2009wnt10amutationsare pages 1-3, adaimy2007mutationinwnt10a pages 4-6) |
| Pathogenic WNT10A variants | Recurrent founder-like variant | c.697G>T, p.Glu233X (reported as recurrent homozygous nonsense variant in three Lebanese families) | Adaimy et al., 2007; https://doi.org/10.1086/520064 | (adaimy2007mutationinwnt10a pages 1-4, adaimy2007mutationinwnt10a pages 4-6) |
| Pathogenic WNT10A variants | Truncating variant | c.27G>A, p.W9X | Bohring et al., 2009; https://doi.org/10.1016/j.ajhg.2009.06.001 | (bohring2009wnt10amutationsare pages 1-3) |
| Pathogenic WNT10A variants | Truncating variant | c.321C>A, p.C107X | Bohring et al., 2009; https://doi.org/10.1016/j.ajhg.2009.06.001 | (bohring2009wnt10amutationsare pages 1-3) |
| Pathogenic WNT10A variants | Truncating variant | c.1128C>A, p.C376X | Bohring et al., 2009; https://doi.org/10.1016/j.ajhg.2009.06.001 | (bohring2009wnt10amutationsare pages 1-3) |
| Pathogenic WNT10A variants | Missense variant | c.383G>A, p.R128Q | Bohring et al., 2009; https://doi.org/10.1016/j.ajhg.2009.06.001 | (bohring2009wnt10amutationsare pages 1-3) |
| Pathogenic WNT10A variants | Missense variant | c.682T>A, p.F228I | Bohring et al., 2009; https://doi.org/10.1016/j.ajhg.2009.06.001 | (bohring2009wnt10amutationsare pages 1-3) |
| Pathogenic WNT10A variants | Novel truncating variant | c.1176C>A, p.Cys392* | Yu et al., 2019; https://doi.org/10.1002/ajmg.a.60682 | (yu2019distinctimpactsof pages 1-2) |
| Pathogenic WNT10A variants | Novel truncating variant | c.742C>T, p.Arg248* | Yu et al., 2019; https://doi.org/10.1002/ajmg.a.60682 | (yu2019distinctimpactsof pages 1-2) |
| Pathogenic WNT10A variants | Novel frameshift variant | c.898-899delAT, p.Ile300Profs*126 | Yu et al., 2019; https://doi.org/10.1002/ajmg.a.60682 | (yu2019distinctimpactsof pages 1-2) |
| Pathogenic WNT10A variants | Novel compound-heterozygous variant | c.826T>A, p.Cys276Ser | Yu et al., 2019; https://doi.org/10.1002/ajmg.a.60682 | (yu2019distinctimpactsof pages 1-2) |
| Pathogenic WNT10A variants | Novel compound-heterozygous variant | c.949delG, p.Ala317Hisfs*121 | Yu et al., 2019; https://doi.org/10.1002/ajmg.a.60682 | (yu2019distinctimpactsof pages 1-2) |
| Recent related WNT10A deficiency report | Compound-heterozygous pathogenic variants in a mild ectodermal phenotype suggestive of WNT10A deficiency | c.310C>T, p.Arg104Cys; c.742C>T, p.Arg248Ter | García-Martínez et al., 2023; https://doi.org/10.3390/children10020356 | (garciamartinez2023dentalphenotypewith pages 1-2, garciamartinez2023dentalphenotypewith pages 2-6) |


*Table: This table compiles only evidence-supported identifiers, hallmark features, and reported WNT10A variants for odonto-onycho-dermal dysplasia from the retrieved snippets. It is useful as a citation-ready summary for disease knowledge base curation.*

### 4.3 Functional consequence (current understanding)
The clinical genetics evidence supports primarily **loss-of-function** mechanisms: truncating variants (nonsense/frameshift) and deleterious missense variants affecting conserved residues (often in compound heterozygosity with truncating alleles) are associated with OODD. (bohring2009wnt10amutationsare pages 1-3, tardieu2017dentalandextra‐oral pages 10-13)

### 4.4 Epigenetics, chromosomal abnormalities, modifier genes
- Epigenetic mechanisms and chromosomal structural abnormalities were not identified in the retrieved excerpts.
- Candidate modifiers suggested by case/cohort data include **EDAR** (Val370Ala) (garciamartinez2023dentalphenotypewith pages 1-2) and digenic interactions involving **EDA** with WNT10A (liu2024compoundheterozygouswnt10a pages 1-2).


## 5. Environmental Information
No specific environmental or lifestyle contributors were identified in the retrieved OODD evidence. OODD is supported as a primarily **genetic developmental disorder** due to WNT10A variants. (adaimy2007mutationinwnt10a pages 1-4, bohring2009wnt10amutationsare pages 1-3)


## 6. Mechanism / Pathophysiology

### 6.1 Pathway-level mechanism
WNT10A is a Wnt ligand acting through **canonical Wnt/β-catenin signaling**:
- Wnt proteins inhibit the β-catenin degradation complex; stabilized β-catenin partners with **LEF/TCF** transcription factors to regulate target gene expression. (bohring2009wnt10amutationsare pages 1-3)
- Wnt binds **Frizzled** and **LRP5/6**, stabilizes β-catenin, and via LEF-1/TCF can induce downstream osteogenic programs (e.g., RUNX2). (tardieu2017dentalandextra‐oral pages 3-7)

This signaling is central to **odontogenesis and ectodermal appendage development**, consistent with the restriction of clinical phenotypes to ectoderm-derived organs. (bohring2009wnt10amutationsare pages 1-3, yu2019distinctimpactsof pages 2-3)

### 6.2 Tissue/cell types implicated (ontology suggestions)
**Primary tissues/organs** (UBERON suggestions):
- Tooth (UBERON:0001091)
- Nail (UBERON:0001705)
- Skin (UBERON:0002097)
- Hair follicle (UBERON:0001034)
- Tongue (UBERON:0001723)

**Cell types (CL suggestions)** (inferred from described organ involvement and Wnt pathway context):
- Ameloblast (CL:0000148) (enamel defects)
- Odontoblast (CL:0000138) (dentin/root phenotypes; odontoblast-region expression described) (yoshinaga2023effectsofwnt10a pages 1-2)
- Keratinocyte (CL:0000312) (skin/nail/hair phenotypes)

**GO biological process suggestions** (based on pathway descriptions):
- Canonical Wnt signaling pathway (GO:0060070)
- Tooth development (GO:0042476)
- Hair follicle development (GO:0001942)
- Keratinization (GO:0031424)

### 6.3 Protein features relevant to disease
WNT10A has a **signal peptide (aa 1–35)** and a **Wnt domain (aa 60–417)**; disease-associated mutations include truncating variants expected to disrupt these functional regions, supporting a loss-of-function model. (bohring2009wnt10amutationsare pages 1-3)

### 6.4 Model organism evidence
- A **wnt10a−/− mouse** shows dental anomalies including molar microdontia, reduced cusp number, taurodontism and (in some reports) supernumerary molars, indicating conserved involvement of Wnt10a in odontogenesis with notable species differences from human tooth agenesis. (tardieu2017dentalandextra‐oral pages 10-13)
- **Wnt10a/Wnt10b double mutants** show severe enamel/root hypoplasia; double knockouts can exhibit a decreased number of teeth (e.g., missing upper incisor or third molar), consistent with functional redundancy. (yoshinaga2023effectsofwnt10a pages 1-2)


## 7. Anatomical Structures Affected

### 7.1 Organ systems
Primary affected systems are **integumentary and craniofacial/odontogenic**:
- Dentition (tooth agenesis, abnormal morphology) (yu2019distinctimpactsof pages 2-3)
- Skin/palms/soles (keratoderma, xerosis) (bohring2009wnt10amutationsare pages 3-5)
- Nails (dystrophy) (yu2019distinctimpactsof pages 2-3)
- Hair/eyebrows (hypotrichosis) (bohring2009wnt10amutationsare pages 3-5)
- Tongue (smooth tongue due to papillae reduction) (bohring2009wnt10amutationsare pages 3-5)

Secondary/variable involvement: skeletal/cartilaginous anomalies and other extra-ectodermal findings have been described in WNT10A cohorts (~10% for major skeletal/cartilaginous defects). (tardieu2017dentalandextra‐oral pages 10-13)


## 8. Temporal Development
OODD is a congenital/developmental condition with manifestations becoming apparent in infancy/childhood as dentition, hair, nails, and skin appendages develop. In one cohort description, early eruption timing of primary teeth (4–10 months) is reported in affected infants, and palmoplantar hyperkeratosis may develop around early childhood. (bohring2009wnt10amutationsare pages 3-5, adaimy2007mutationinwnt10a pages 1-4)


## 9. Inheritance and Population

### 9.1 Inheritance
OODD is **autosomal recessive** due to **biallelic WNT10A variants**. (adaimy2007mutationinwnt10a pages 1-4, yu2019distinctimpactsof pages 1-2)

### 9.2 Population and carrier manifestations
Heterozygous carriers may show milder manifestations; in one ectodermal dysplasia cohort, ~**53.8% of heterozygotes** showed phenotype manifestations with sex-biased patterns. (bohring2009wnt10amutationsare pages 1-3)

*Note:* Variant-specific geographic distributions and founder effects were not systematically extractable from the retrieved excerpts beyond the original observation of a recurrent variant in three families from the same community. (adaimy2007mutationinwnt10a pages 4-6)


## 10. Diagnostics

### 10.1 Clinical and radiographic evaluation
Typical work-up includes clinical examination of ectodermal structures and dental imaging (panoramic radiographs) to document absent/retained teeth and morphology. (yu2019distinctimpactsof pages 2-3)

### 10.2 Genetic testing approaches (real-world implementations)
Approaches documented across studies include:
- **Homozygosity mapping + Sanger sequencing** in consanguineous families to identify WNT10A founder variants. (adaimy2007mutationinwnt10a pages 1-4)
- **Targeted PCR/Sanger sequencing** of WNT10A with segregation analysis. (bohring2009wnt10amutationsare pages 1-3, tardieu2017dentalandextra‐oral pages 3-7)
- **Gene panels** (e.g., orodental NGS panel) in some families. (tardieu2017dentalandextra‐oral pages 3-7)
- **Whole-exome sequencing (WES)** in 2024 digenic HED report with ACMG-based evaluation. (liu2024compoundheterozygouswnt10a pages 1-2)

### 10.3 Differential diagnosis
A key differential is **Schöpf–Schulz–Passarge syndrome (SSPS)**, which overlaps clinically with OODD but is characterized by **multiple eyelid cysts / apocrine hidrocystomas** and has been associated with increased risk of skin tumors. The absence of eyelid cysts is used to favor an OODD diagnosis in WNT10A-related cases. (tardieu2017dentalandextra‐oral pages 1-3, yu2019distinctimpactsof pages 2-3, bohring2009wnt10amutationsare pages 1-3)


## 11. Outcome / Prognosis
OODD is generally compatible with normal growth and neurodevelopment in reported families, but is a chronic lifelong disorder requiring ongoing dental/dermatologic care (e.g., “Growth and mental development were normal”). (adaimy2007mutationinwnt10a pages 1-4)

Major determinants of morbidity are functional and psychosocial impacts of severe tooth agenesis, chewing/speech/aesthetic challenges, and skin/nail/hair symptoms. Formal survival or mortality statistics were not identified in the retrieved excerpts. (bohring2009wnt10amutationsare pages 3-5, nurrahma2023prostheticsmanagementof pages 1-2)


## 12. Treatment

### 12.1 Current standard of care
No curative therapy is described; management is supportive and multidisciplinary. A recent report states: “**Currently there is no curative treatment for OODD. Multidisciplinary supportive management remains the gold standard**.” (kalaszi2026casereportnovel pages 2-4)

### 12.2 Dental/prosthetic rehabilitation (real-world implementations; 2023 emphasis)
- **2023 pediatric OODD case report (Journal of Dentomaxillofacial Science; Dec 2023; https://doi.org/10.15562/jdmfs.v8i3.1638):** a 12-year-old received **removable dentures** (maxillary and mandibular). Reported short-term outcomes included eruption of maxillary molars after **3 months**, followed by denture perforation to accommodate erupting teeth; mandibular premolars erupted by **~1 month later**, with **surgical exposure** used to accelerate eruption. The authors emphasize interdisciplinary therapy. (nurrahma2023prostheticsmanagementof pages 1-2)
- **Monitoring and planning:** a 2023 WNT10A-deficient oligodontia case was monitored for jaw growth and planned future rehabilitation rather than immediate definitive prosthetics. (garciamartinez2023dentalphenotypewith pages 2-6)

**MAXO suggestions** (inferred for management actions described):
- Dental prosthesis therapy (MAXO term suggestion for removable dentures)
- Surgical exposure of tooth (MAXO term suggestion)
- Dental surveillance/monitoring (MAXO term suggestion)

### 12.3 Pharmacotherapy / advanced therapeutics
No OODD-specific pharmacologic or gene therapies were identified in the retrieved evidence. A case report references emerging regenerative approaches and related prenatal EDA trials in XLHED, but these are not OODD-specific. (kalaszi2026casereportnovel pages 2-4)

### 12.4 Clinical trials
A ClinicalTrials.gov search for “WNT10A”/“odonto-onycho-dermal dysplasia” did not identify OODD-targeted interventional trials in the retrieved trial set. (adaimy2007mutationinwnt10a media 078cd7b3)


## 13. Prevention
No primary prevention is available for a congenital Mendelian disorder; prevention focuses on:
- **Genetic counseling** for recurrence risk in families with identified WNT10A variants, and cascade testing of relatives (noted in clinical genetics practice in recent case-based reports). (kalaszi2026casereportnovel pages 2-4)
- **Secondary/tertiary prevention** of complications: early dental evaluation, caries prevention, and proactive prosthetic/orthodontic planning to reduce functional and psychosocial burden. (nurrahma2023prostheticsmanagementof pages 3-4)


## 14. Other Species / Natural Disease
Naturally occurring OODD analogs in non-human species were not identified in the retrieved excerpts.


## 15. Model Organisms

### Mouse models
- **Wnt10a knockout mice**: enamel hypoplasia, altered tooth shape, taurodontic roots; unexpected supernumerary teeth reported, highlighting species differences and pathway complexity. (yoshinaga2023effectsofwnt10a pages 2-4)
- **Wnt10a/Wnt10b double mutants**: severe enamel/root hypoplasia and reduced tooth number in double knockouts, supporting redundancy between paralogs. (yoshinaga2023effectsofwnt10a pages 1-2)


## Key visual evidence
A key figure/table set in the original gene-discovery report includes:
- **Table summarizing OODD clinical features across families** and sequencing chromatograms for the **c.697G>T (p.Glu233X)** mutation (adaimy2007mutationinwnt10a media 78f3e813, adaimy2007mutationinwnt10a media beb3a4f1).


## Summary of key 2023–2024 developments
- **2023:** recognition of “dental-dominant” WNT10A deficiency presentations with mild ectodermal signs and possible **modifier effects (EDAR Val370Ala)** (garciamartinez2023dentalphenotypewith pages 1-2).
- **2024:** evidence supporting **digenic/modifier interactions (EDA + WNT10A)** affecting tooth agenesis severity, with structural modeling implicating altered WNT10A–FZD5 interactions (liu2024compoundheterozygouswnt10a pages 1-2).


### Limitations of this evidence set
This report is limited to the retrieved primary texts and excerpts. Several requested identifiers (Orphanet/ICD/MeSH), formal prevalence/incidence estimates for OODD specifically, and rigorous QoL metrics were not present in the available excerpts and therefore are not asserted.


References

1. (adaimy2007mutationinwnt10a pages 1-4): Lynn Adaimy, Eliane Chouery, Hala Mégarbané, Salman Mroueh, Valérie Delague, Elsa Nicolas, Hanen Belguith, Philippe de Mazancourt, and André Mégarbané. Mutation in wnt10a is associated with an autosomal recessive ectodermal dysplasia: the odonto-onycho-dermal dysplasia. American journal of human genetics, 81 4:821-8, Oct 2007. URL: https://doi.org/10.1086/520064, doi:10.1086/520064. This article has 315 citations and is from a highest quality peer-reviewed journal.

2. (bohring2009wnt10amutationsare pages 1-3): Axel Bohring, Thomas Stamm, Christiane Spaich, Claudia Haase, Kerstin Spree, Ute Hehr, Mandy Hoffmann, Susanne Ledig, Saadettin Sel, Peter Wieacker, and Albrecht Röpke. Wnt10a mutations are a frequent cause of a broad spectrum of ectodermal dysplasias with sex-biased manifestation pattern in heterozygotes. American journal of human genetics, 85 1:97-105, Jul 2009. URL: https://doi.org/10.1016/j.ajhg.2009.06.001, doi:10.1016/j.ajhg.2009.06.001. This article has 275 citations and is from a highest quality peer-reviewed journal.

3. (yu2019distinctimpactsof pages 1-2): Miao Yu, Yang Liu, Haochen Liu, Sing‐Wai Wong, Huiying He, Xiaoxia Zhang, Yue Wang, Dong Han, and Hailan Feng. Distinct impacts of bi‐allelic wnt10a mutations on the permanent and primary dentitions in odonto‐onycho‐dermal dysplasia. American Journal of Medical Genetics Part A, 179:57-64, Jan 2019. URL: https://doi.org/10.1002/ajmg.a.60682, doi:10.1002/ajmg.a.60682. This article has 43 citations.

4. (kalaszi2026casereportnovel pages 1-2): Marianna Kalaszi, Ciaran Moore, Chrysoula Koniari, and Theodoros Mavridis. Case report: novel pathogenic variant in autosomal recessive wnt10a-related odonto-onycho-dermal dysplasia. Frontiers in Genetics, Mar 2026. URL: https://doi.org/10.3389/fgene.2026.1750692, doi:10.3389/fgene.2026.1750692. This article has 0 citations and is from a peer-reviewed journal.

5. (tardieu2017dentalandextra‐oral pages 1-3): C. Tardieu, Sophie Jung, K. Niederreither, Megana K. Prasad, S. Hadj-Rabia, N. Philip, A. Mallet, É. Consolino, E. Sfeir, B. Noueiri, N. Chassaing, H. Dollfus, M. Manière, M. Manière, A. Bloch-Zupan, and F. Clauss. Dental and extra‐oral clinical features in 41 patients with wnt10a gene mutations: a multicentric genotype–phenotype study. Clinical Genetics, 92:477-486, Nov 2017. URL: https://doi.org/10.1111/cge.12972, doi:10.1111/cge.12972. This article has 34 citations and is from a peer-reviewed journal.

6. (tardieu2017dentalandextra‐oral pages 10-13): C. Tardieu, Sophie Jung, K. Niederreither, Megana K. Prasad, S. Hadj-Rabia, N. Philip, A. Mallet, É. Consolino, E. Sfeir, B. Noueiri, N. Chassaing, H. Dollfus, M. Manière, M. Manière, A. Bloch-Zupan, and F. Clauss. Dental and extra‐oral clinical features in 41 patients with wnt10a gene mutations: a multicentric genotype–phenotype study. Clinical Genetics, 92:477-486, Nov 2017. URL: https://doi.org/10.1111/cge.12972, doi:10.1111/cge.12972. This article has 34 citations and is from a peer-reviewed journal.

7. (yoshinaga2023effectsofwnt10a pages 2-4): Kaoru Yoshinaga, Akihiro Yasue, Silvia Naomi Mitsui, Yoshiyuki Minegishi, Seiichi Oyadomari, Issei Imoto, and Eiji Tanaka. Effects of wnt10a and wnt10b double mutations on tooth development. Genes, 14:340, Jan 2023. URL: https://doi.org/10.3390/genes14020340, doi:10.3390/genes14020340. This article has 7 citations.

8. (adaimy2007mutationinwnt10a pages 4-6): Lynn Adaimy, Eliane Chouery, Hala Mégarbané, Salman Mroueh, Valérie Delague, Elsa Nicolas, Hanen Belguith, Philippe de Mazancourt, and André Mégarbané. Mutation in wnt10a is associated with an autosomal recessive ectodermal dysplasia: the odonto-onycho-dermal dysplasia. American journal of human genetics, 81 4:821-8, Oct 2007. URL: https://doi.org/10.1086/520064, doi:10.1086/520064. This article has 315 citations and is from a highest quality peer-reviewed journal.

9. (garciamartinez2023dentalphenotypewith pages 1-2): Victoria-Eugenia García-Martínez, Ximo Galiana-Vallés, Otilia Zomeño-Alcalá, Raquel Rodríguez-López, Carmen Llena, María del Carmen Martínez-Romero, and Encarna Guillén-Navarro. Dental phenotype with minor ectodermal symptoms suggestive of wnt10a deficiency. Children, 10:356, Feb 2023. URL: https://doi.org/10.3390/children10020356, doi:10.3390/children10020356. This article has 1 citations.

10. (liu2024compoundheterozygouswnt10a pages 1-2): Yiting Liu, Jing Sun, Caiqi Zhang, Yi Wu, Siyuan Ma, Xuechun Li, Xiaoshan Wu, and Qingping Gao. Compound heterozygous wnt10a missense variations exacerbated the tooth agenesis caused by hypohidrotic ectodermal dysplasia. BMC Oral Health, Jan 2024. URL: https://doi.org/10.1186/s12903-024-03888-5, doi:10.1186/s12903-024-03888-5. This article has 6 citations and is from a peer-reviewed journal.

11. (yu2019distinctimpactsof pages 2-3): Miao Yu, Yang Liu, Haochen Liu, Sing‐Wai Wong, Huiying He, Xiaoxia Zhang, Yue Wang, Dong Han, and Hailan Feng. Distinct impacts of bi‐allelic wnt10a mutations on the permanent and primary dentitions in odonto‐onycho‐dermal dysplasia. American Journal of Medical Genetics Part A, 179:57-64, Jan 2019. URL: https://doi.org/10.1002/ajmg.a.60682, doi:10.1002/ajmg.a.60682. This article has 43 citations.

12. (bohring2009wnt10amutationsare pages 3-5): Axel Bohring, Thomas Stamm, Christiane Spaich, Claudia Haase, Kerstin Spree, Ute Hehr, Mandy Hoffmann, Susanne Ledig, Saadettin Sel, Peter Wieacker, and Albrecht Röpke. Wnt10a mutations are a frequent cause of a broad spectrum of ectodermal dysplasias with sex-biased manifestation pattern in heterozygotes. American journal of human genetics, 85 1:97-105, Jul 2009. URL: https://doi.org/10.1016/j.ajhg.2009.06.001, doi:10.1016/j.ajhg.2009.06.001. This article has 275 citations and is from a highest quality peer-reviewed journal.

13. (garciamartinez2023dentalphenotypewith pages 2-6): Victoria-Eugenia García-Martínez, Ximo Galiana-Vallés, Otilia Zomeño-Alcalá, Raquel Rodríguez-López, Carmen Llena, María del Carmen Martínez-Romero, and Encarna Guillén-Navarro. Dental phenotype with minor ectodermal symptoms suggestive of wnt10a deficiency. Children, 10:356, Feb 2023. URL: https://doi.org/10.3390/children10020356, doi:10.3390/children10020356. This article has 1 citations.

14. (nurrahma2023prostheticsmanagementof pages 1-2): Rifaat Nurrahma, Syakriani Syahrir, Muhammad Ikbal, Edy Machmud, Irfan Dammar, Acing H. Mude, Ike D. Habar, Ludfia Ulfa, Nurimah Wahyuni, and Ainun Bazira. Prosthetics management of odonto-onycho-dermal dysplasia pediatric patient: a case report. Journal of Dentomaxillofacial Science, 8:196-199, Dec 2023. URL: https://doi.org/10.15562/jdmfs.v8i3.1638, doi:10.15562/jdmfs.v8i3.1638. This article has 0 citations.

15. (adaimy2007mutationinwnt10a pages 6-7): Lynn Adaimy, Eliane Chouery, Hala Mégarbané, Salman Mroueh, Valérie Delague, Elsa Nicolas, Hanen Belguith, Philippe de Mazancourt, and André Mégarbané. Mutation in wnt10a is associated with an autosomal recessive ectodermal dysplasia: the odonto-onycho-dermal dysplasia. American journal of human genetics, 81 4:821-8, Oct 2007. URL: https://doi.org/10.1086/520064, doi:10.1086/520064. This article has 315 citations and is from a highest quality peer-reviewed journal.

16. (tardieu2017dentalandextra‐oral pages 3-7): C. Tardieu, Sophie Jung, K. Niederreither, Megana K. Prasad, S. Hadj-Rabia, N. Philip, A. Mallet, É. Consolino, E. Sfeir, B. Noueiri, N. Chassaing, H. Dollfus, M. Manière, M. Manière, A. Bloch-Zupan, and F. Clauss. Dental and extra‐oral clinical features in 41 patients with wnt10a gene mutations: a multicentric genotype–phenotype study. Clinical Genetics, 92:477-486, Nov 2017. URL: https://doi.org/10.1111/cge.12972, doi:10.1111/cge.12972. This article has 34 citations and is from a peer-reviewed journal.

17. (yoshinaga2023effectsofwnt10a pages 1-2): Kaoru Yoshinaga, Akihiro Yasue, Silvia Naomi Mitsui, Yoshiyuki Minegishi, Seiichi Oyadomari, Issei Imoto, and Eiji Tanaka. Effects of wnt10a and wnt10b double mutations on tooth development. Genes, 14:340, Jan 2023. URL: https://doi.org/10.3390/genes14020340, doi:10.3390/genes14020340. This article has 7 citations.

18. (kalaszi2026casereportnovel pages 2-4): Marianna Kalaszi, Ciaran Moore, Chrysoula Koniari, and Theodoros Mavridis. Case report: novel pathogenic variant in autosomal recessive wnt10a-related odonto-onycho-dermal dysplasia. Frontiers in Genetics, Mar 2026. URL: https://doi.org/10.3389/fgene.2026.1750692, doi:10.3389/fgene.2026.1750692. This article has 0 citations and is from a peer-reviewed journal.

19. (adaimy2007mutationinwnt10a media 078cd7b3): Lynn Adaimy, Eliane Chouery, Hala Mégarbané, Salman Mroueh, Valérie Delague, Elsa Nicolas, Hanen Belguith, Philippe de Mazancourt, and André Mégarbané. Mutation in wnt10a is associated with an autosomal recessive ectodermal dysplasia: the odonto-onycho-dermal dysplasia. American journal of human genetics, 81 4:821-8, Oct 2007. URL: https://doi.org/10.1086/520064, doi:10.1086/520064. This article has 315 citations and is from a highest quality peer-reviewed journal.

20. (nurrahma2023prostheticsmanagementof pages 3-4): Rifaat Nurrahma, Syakriani Syahrir, Muhammad Ikbal, Edy Machmud, Irfan Dammar, Acing H. Mude, Ike D. Habar, Ludfia Ulfa, Nurimah Wahyuni, and Ainun Bazira. Prosthetics management of odonto-onycho-dermal dysplasia pediatric patient: a case report. Journal of Dentomaxillofacial Science, 8:196-199, Dec 2023. URL: https://doi.org/10.15562/jdmfs.v8i3.1638, doi:10.15562/jdmfs.v8i3.1638. This article has 0 citations.

21. (adaimy2007mutationinwnt10a media 78f3e813): Lynn Adaimy, Eliane Chouery, Hala Mégarbané, Salman Mroueh, Valérie Delague, Elsa Nicolas, Hanen Belguith, Philippe de Mazancourt, and André Mégarbané. Mutation in wnt10a is associated with an autosomal recessive ectodermal dysplasia: the odonto-onycho-dermal dysplasia. American journal of human genetics, 81 4:821-8, Oct 2007. URL: https://doi.org/10.1086/520064, doi:10.1086/520064. This article has 315 citations and is from a highest quality peer-reviewed journal.

22. (adaimy2007mutationinwnt10a media beb3a4f1): Lynn Adaimy, Eliane Chouery, Hala Mégarbané, Salman Mroueh, Valérie Delague, Elsa Nicolas, Hanen Belguith, Philippe de Mazancourt, and André Mégarbané. Mutation in wnt10a is associated with an autosomal recessive ectodermal dysplasia: the odonto-onycho-dermal dysplasia. American journal of human genetics, 81 4:821-8, Oct 2007. URL: https://doi.org/10.1086/520064, doi:10.1086/520064. This article has 315 citations and is from a highest quality peer-reviewed journal.