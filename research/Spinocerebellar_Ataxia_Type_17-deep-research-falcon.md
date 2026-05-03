---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-30T20:26:34.565779'
end_time: '2026-04-30T20:36:51.237259'
duration_seconds: 616.67
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Spinocerebellar ataxia type 17
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 18
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Spinocerebellar ataxia type 17
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Spinocerebellar ataxia type 17** covering all of the
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
- **Disease Name:** Spinocerebellar ataxia type 17
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Spinocerebellar ataxia type 17** covering all of the
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


# Spinocerebellar ataxia type 17 (SCA17; ATX‑TBP; Huntington disease–like 4) — Disease Characteristics Research Report

## Executive summary
Spinocerebellar ataxia type 17 (SCA17) is a rare, autosomal dominant neurodegenerative polyglutamine (polyQ) disorder caused by expansion of a mixed CAG/CAA repeat in **TBP** (TATA‑box binding protein), historically also termed **Huntington disease–like 4 (HDL4)** because chorea, psychiatric symptoms, and dementia can mimic Huntington disease. (toyoshima2018spinocerebellarataxiatype pages 1-5, nethisinghe2018complexityofthe pages 1-2, rossi2023genotype–phenotypecorrelationsfor pages 1-1)

A major recent development is a 2023 Movement Disorders Society Genetic Mutation Database (MDSGene) systematic review (346 curated patients) proposing revised repeat-size penetrance thresholds—**reduced penetrance 41–45** and **full penetrance 46–66**—to guide diagnosis, counseling, and trial design. (rossi2023genotype–phenotypecorrelationsfor pages 1-1, rossi2023genotype–phenotypecorrelationsfor media 82dfeaa1)

A second 2024 advance is refined interpretation of the *repeat tract structure* (not only repeat count): a literature-based sequence analysis of reported alleles proposed a 3‑unit organization of the TBP repeat region and argued this structural annotation may help predict intergenerational stability and anticipation risk. (hoffmanzacharska2024thenewface pages 1-2)

---

## 1. Disease information
### What is the disease?
SCA17 is an autosomal dominant cerebellar ataxia caused by a polyglutamine expansion in **TBP**, a general transcription initiation factor. A review chapter notes: “**In 1999, a polyglutamine expansion was identiﬁed in the transcription factor TATA-binding protein (TBP)**” in SCA17. (toyoshima2018spinocerebellarataxiatype pages 1-5)

### Synonyms / alternative names
* Spinocerebellar ataxia type 17 (SCA17) (toyoshima2018spinocerebellarataxiatype pages 1-5)
* ATX‑TBP (rossi2023genotype–phenotypecorrelationsfor pages 1-1)
* Huntington disease–like 4 (HDL4) (toyoshima2018spinocerebellarataxiatype pages 1-5, rossi2023genotype–phenotypecorrelationsfor pages 2-2)

### Key identifiers (OMIM, Orphanet, ICD, MeSH, MONDO)
The provided tool-retrieved sources did not include OMIM/Orphanet/ICD/MeSH/MONDO identifiers; therefore these identifiers cannot be asserted from the current evidence set.

### Evidence source type
The 2023 MDSGene systematic review is derived from aggregated literature (case reports and family studies) curated into a standardized database. (rossi2023genotype–phenotypecorrelationsfor pages 1-1, rossi2023genotype–phenotypecorrelationsfor pages 8-8)

---

## 2. Etiology
### Disease causal factors
**Primary cause (genetic):** germline expansion of a mixed **CAG/CAA repeat** in exon 3 of **TBP**, encoding an expanded polyglutamine tract. (nethisinghe2018complexityofthe pages 1-2, rossi2023genotype–phenotypecorrelationsfor pages 1-1)

**Mechanistic framing:** SCA17 is one of the “triplet repeat diseases,” where repeat tracts can form non‑B DNA structures that predispose to instability during replication/repair, promoting dynamic mutation. (hoffmanzacharska2024thenewface pages 1-2)

### Risk factors
* **Repeat size / penetrance:** The 2023 MDSGene review reports that “**97.7% of the patients had ≥41 repeats**” and proposes a reduced‑penetrance “gray zone” between 41 and 45 repeats, with full penetrance above this range. (rossi2023genotype–phenotypecorrelationsfor pages 1-1)
* **Family history:** SCA17 is typically autosomal dominant; however, reduced penetrance and variable expressivity can yield asymptomatic carriers in families. (nethisinghe2018complexityofthe pages 1-2)

### Protective factors
No protective genetic variants or modifiable protective environmental factors were identified in the provided evidence set.

### Gene–environment interactions
The UK cohort paper reports marked intrafamilial variability (including discordant monozygotic twins) and suggests environmental/epigenetic influences may contribute, but does not specify a particular exposure. (nethisinghe2018complexityofthe pages 1-2)

---

## 3. Phenotypes
### Core phenotype spectrum
A 2018 review chapter reports broad clinical heterogeneity and provides approximate frequencies for selected manifestations:
* **Cerebellar ataxia:** “**most of the patients (>90%) developed ataxia**.” (toyoshima2018spinocerebellarataxiatype pages 1-5)
* **Dementia/cognitive decline:** “**dementia is the second most common symptom (73%)**.” (toyoshima2018spinocerebellarataxiatype pages 1-5)
* **Seizures/epilepsy:** ~20% (toyoshima2018spinocerebellarataxiatype pages 1-5)
* **Autonomic dysfunction:** ~9% (toyoshima2018spinocerebellarataxiatype pages 1-5)
* **Apraxia:** ~7% (toyoshima2018spinocerebellarataxiatype pages 1-5)
* **Peripheral nerve involvement:** ~3% (toyoshima2018spinocerebellarataxiatype pages 1-5)

The 2023 MDSGene review emphasizes non‑ataxic presentations also occur, including “pure parkinsonism or chorea associated with dementia,” and notes psychiatric/cognitive manifestations such as psychosis and depression. (rossi2023genotype–phenotypecorrelationsfor pages 2-2)

#### Phenotype characteristics
* **Age of onset:** very broad; review sources report onset approximately from childhood to later adulthood (e.g., 3–60 years). (toyoshima2018spinocerebellarataxiatype pages 1-5, grassini2024cognitivedysfunctionsocial pages 1-3)
* **Progression:** progressive neurodegenerative disorder with variable severity across individuals and within families. (nethisinghe2018complexityofthe pages 1-2)

### Genotype–phenotype notes (clinical)
* The MDSGene systematic review proposes that **pure parkinsonism** is more common among carriers with 41–45 repeats, whereas carriers with ≥46 repeats more often show a complex mixed movement disorder phenotype. (rossi2023genotype–phenotypecorrelationsfor pages 1-1)
* A review chapter reports that among repeat sizes **43–50**, “more than 75%” had intellectual deterioration; among repeat sizes **50–60**, 75% had reduced intellectual function. (toyoshima2018spinocerebellarataxiatype pages 1-5)

### Quality of life impact
A 2024 case report noted preserved basic activities of daily living but impaired instrumental ADLs (IADL 4/8) in one patient, consistent with functional impact from cognitive/social-cognition deficits. (grassini2024cognitivedysfunctionsocial pages 1-3)

### Suggested HPO terms (non-exhaustive; evidence-backed)
* Cerebellar ataxia — **HP:0001251** (toyoshima2018spinocerebellarataxiatype pages 1-5)
* Gait ataxia — **HP:0002066** (rossi2023genotype–phenotypecorrelationsfor pages 2-2)
* Dysarthria — **HP:0001260** (rossi2023genotype–phenotypecorrelationsfor pages 2-2)
* Abnormality of eye movement — **HP:0000496** (rossi2023genotype–phenotypecorrelationsfor pages 2-2)
* Dementia — **HP:0000726** (toyoshima2018spinocerebellarataxiatype pages 1-5)
* Cognitive impairment — **HP:0100543** (rossi2023genotype–phenotypecorrelationsfor pages 2-2)
* Parkinsonism — **HP:0001300** (rossi2023genotype–phenotypecorrelationsfor pages 1-1)
* Chorea — **HP:0002072** (toyoshima2018spinocerebellarataxiatype pages 1-5)
* Seizure — **HP:0001250** (toyoshima2018spinocerebellarataxiatype pages 1-5)
* Depression — **HP:0000716** (rossi2023genotype–phenotypecorrelationsfor pages 2-2)
* Psychosis — **HP:0000709** (rossi2023genotype–phenotypecorrelationsfor pages 2-2)

---

## 4. Genetic / molecular information
### Causal gene
* **TBP** (TATA‑box binding protein). (toyoshima2018spinocerebellarataxiatype pages 1-5, nethisinghe2018complexityofthe pages 1-2)

### Pathogenic variant class
* **Repeat expansion** of a mixed CAG/CAA tract (polyQ‑encoding) in TBP. (rossi2023genotype–phenotypecorrelationsfor pages 1-1, hoffmanzacharska2024thenewface pages 1-2)

### Repeat length interpretation (current practice trend)
The 2023 MDSGene systematic review provides a data-driven reinterpretation of TBP repeat cutoffs:
* “**97.7% of the patients had ≥41 repeats**” (curated cases) (rossi2023genotype–phenotypecorrelationsfor pages 1-1)
* Proposed thresholds: **reduced penetrance 41–45** and **full penetrance 46–66** (rossi2023genotype–phenotypecorrelationsfor pages 1-1)
* Comparative cohorts: “**99.6% of patients with PD and 99.9% of healthy individuals had ≤42 repeats**” (rossi2023genotype–phenotypecorrelationsfor pages 1-1)

A visual summary of clinical features across revised repeat groups (Figure 3) and an accompanying table of features by repeat group (Table 2) were extracted from the MDSGene review. (rossi2023genotype–phenotypecorrelationsfor media 82dfeaa1, rossi2023genotype–phenotypecorrelationsfor media 1829bb84)

### Repeat structure (2024 development)
A 2024 IJMS paper argues that repeat composition and motif organization should be annotated to improve prognostic counseling, stating that “**detailed analysis of the CAG/CAA repeat structure, not just the number of repeats, in TBP-expanded alleles should be performed**” due to potential relevance for stability/anticipation. (hoffmanzacharska2024thenewface pages 1-2)

### Modifier genes / digenic inheritance
A 2024 SCA17 case report summarizes literature suggesting intermediate TBP expansions may require co-occurring **STUB1** variants to cause disease (digenic TBP/STUB1), implying modifier or digenic mechanisms in borderline repeat-size cases. (grassini2024cognitivedysfunctionsocial pages 1-3)

### Suggested ontology terms
* Gene: **TBP** (HGNC:11588; not provided in evidence set—listed here as a standard identifier and should be verified against HGNC directly)
* Disease mechanism: trinucleotide repeat expansion (sequence feature)

---

## 5. Environmental information
No specific environmental toxins, lifestyle factors, or infectious triggers for SCA17 were identified in the provided evidence set; SCA17 is primarily genetic. (toyoshima2018spinocerebellarataxiatype pages 1-5, rossi2023genotype–phenotypecorrelationsfor pages 1-1)

---

## 6. Mechanism / pathophysiology
### Current mechanistic concepts (disease-relevant)
* **Dynamic mutation biology:** repeat tracts can form “unusual DNA structures” and undergo instability, motivating the concept of repeat unit organization and its relationship to transmission stability. (hoffmanzacharska2024thenewface pages 1-2)
* **PolyQ protein toxicity:** SCA17 belongs to the polyQ disorders in which expanded glutamine tracts alter protein behavior, with downstream processes in polyQ SCAs broadly including transcriptional dysregulation, impaired protein quality control, mitochondrial dysfunction, and neuronal dysfunction (discussed across SCA reviews). (cui2024spinocerebellarataxiasfrom pages 1-2)

### Causal chain (high-level)
TBP mixed CAG/CAA repeat expansion → expanded polyglutamine tract in TBP → altered TBP conformational/interaction behavior and/or nuclear localization/aggregation (supported in model systems) → neuronal dysfunction and neurodegeneration affecting cerebellar and extra-cerebellar circuits → progressive ataxia with cognitive/psychiatric and movement-disorder manifestations. (patel2023phenotypicdefectsfrom pages 1-2, cui2024spinocerebellarataxiasfrom pages 1-2)

### Suggested GO biological process terms (candidates; align to evidence themes)
* Transcription initiation from RNA polymerase II promoter — **GO:0006367** (TBP function; mechanistic relevance implied) (toyoshima2018spinocerebellarataxiatype pages 1-5)
* Protein aggregation — **GO:0070848** (model evidence of aggregation-prone TBP) (patel2023phenotypicdefectsfrom pages 1-2)
* Neuron death / neurodegeneration — **GO:1901214** (disease-level phenotype; implied) (cui2024spinocerebellarataxiasfrom pages 1-2)

### Suggested Cell Ontology (CL) terms (candidates)
Primary vulnerable cells are not explicitly enumerated in the provided excerpts; broadly, cerebellar neuronal populations are implicated. Candidate CL terms that should be verified/expanded with additional neuropathology sources include:
* Purkinje cell — **CL:0000121**

---

## 7. Anatomical structures affected
### Organ/system level
* Nervous system, with cerebellar and extra-cerebellar involvement (dementia/psychiatric features and chorea/parkinsonism imply wider network degeneration). (toyoshima2018spinocerebellarataxiatype pages 1-5, rossi2023genotype–phenotypecorrelationsfor pages 2-2)

### Imaging-supported structures (examples)
A 2024 case report described MRI atrophy of frontal cortex/hippocampus/cerebellum/brainstem and FDG‑PET with striatal hypometabolism and thalamic hypermetabolism (Huntington-like pattern). (grassini2024cognitivedysfunctionsocial pages 1-3)

### Suggested UBERON terms (candidates)
* Cerebellum — **UBERON:0002037** (toyoshima2018spinocerebellarataxiatype pages 1-5)
* Striatum — **UBERON:0002435** (grassini2024cognitivedysfunctionsocial pages 1-3)

---

## 8. Temporal development
### Onset
Broad onset range is reported (including childhood onset in rare cases with long expansions) with substantial heterogeneity. (toyoshima2018spinocerebellarataxiatype pages 1-5, grassini2024cognitivedysfunctionsocial pages 1-3)

### Progression / course
Progressive neurodegenerative course with variable expressivity even within families; anticipation is described as uncommon compared with other polyQ disorders. (nethisinghe2018complexityofthe pages 1-2)

---

## 9. Inheritance and population
### Inheritance
Autosomal dominant inheritance is repeatedly described, with reduced penetrance for small/intermediate repeat sizes and variable expressivity. (toyoshima2018spinocerebellarataxiatype pages 1-5, rossi2023genotype–phenotypecorrelationsfor pages 1-1)

### Epidemiology statistics (limited by available evidence)
* UK cohort allele frequency: fully penetrant pathogenic alleles were “**5 in 1,316 chromosomes; 0.38%**” in an ataxia cohort (not population prevalence). (nethisinghe2018complexityofthe pages 1-2)
* A review chapter reports that in an HD-phenocopy series, **1.8% (5/285)** had TBP expansions. (toyoshima2018spinocerebellarataxiatype pages 1-5)

Robust population prevalence/incidence estimates were not available in the provided evidence set.

---

## 10. Diagnostics
### Genetic testing
Given the narrow normal–pathogenic repeat gap and phenotypic overlap with Huntington disease-like syndromes, genetic testing of TBP is central. A review chapter states: “**If patients with HD-like disease have no mutations in huntingtin, the TBP and C9orf72 genes should be examined**.” (toyoshima2018spinocerebellarataxiatype pages 1-5)

### Repeat expansion interpretation (clinical counseling)
The 2023 MDSGene review emphasizes that establishing a strict cut-off has been challenging and proposes revised penetrance ranges with a reduced-penetrance “gray zone.” (rossi2023genotype–phenotypecorrelationsfor pages 1-1, rossi2023genotype–phenotypecorrelationsfor pages 2-2)

### Imaging/biomarkers (emerging)
A 2024 case report highlights that FDG‑PET patterns may be atypical (Huntington-like striatal hypometabolism and thalamic hypermetabolism) even without marked cerebellar hypometabolism. (grassini2024cognitivedysfunctionsocial pages 1-3)

### Differential diagnosis
SCA17 can phenocopy Huntington disease, including chorea/psychiatric/dementia features; the literature explicitly categorizes ATX‑TBP among Huntington disease-like syndromes. (toyoshima2018spinocerebellarataxiatype pages 1-5, rossi2023genotype–phenotypecorrelationsfor pages 2-2)

---

## 11. Outcome / prognosis
Detailed survival and quantitative progression rates were not available in the provided evidence set. The disease is progressive with substantial heterogeneity and potential severe early-onset forms in very large expansions. (toyoshima2018spinocerebellarataxiatype pages 1-5, nethisinghe2018complexityofthe pages 1-2)

---

## 12. Treatment
### Current standard of care
No disease-modifying therapy is established; care is primarily symptomatic and supportive (as described broadly for SCAs). (cui2024spinocerebellarataxiasfrom pages 1-2)

### Experimental / clinical trials (registry evidence)
**CAD‑1883 (Synchrony‑1) — includes SCA17 explicitly**
* Trial: “Study of CAD‑1883 for Spinocerebellar Ataxia”
* ClinicalTrials.gov ID: **NCT04301284**
* Phase: **2**; randomized, double-blind, placebo-controlled
* Status: **Withdrawn**; “As part of a pipeline reassessment, the Synchrony‑1 trial will not proceed as initially scheduled.”
* Eligibility included multiple SCA genotypes and explicitly listed “**Spinocerebellar Ataxia Type 17**.”
* URL: https://clinicaltrials.gov/study/NCT04301284 (registry URL format)
* Trial record publication year in excerpt: 2021 (NCT04301284 chunk 1)

**Troriluzole — broad hereditary SCA program (SCA17 not listed in excerpted inclusion genotypes)**
* Trial: “Troriluzole in Adult Participants With Spinocerebellar Ataxia”
* ClinicalTrials.gov ID: **NCT03701399**
* Phase: **3**; quadruple-masked randomized trial with open-label extension
* Status: **Active, not recruiting**; Enrollment **299**
* Included genotypes (as listed in excerpt): SCA1, SCA2, SCA3, SCA6, SCA7, SCA8, SCA10
* URL: https://clinicaltrials.gov/study/NCT03701399
* Trial record publication year in excerpt: 2019 (NCT03701399 chunk 1)

### Recent research directions (2023–2024 reviews; not SCA17-specific efficacy)
Recent SCA therapeutic reviews emphasize disease-modifying approaches under development across polyQ SCAs, including gene editing, RNA interference, antisense oligonucleotides (ASOs), and stem cell approaches, while acknowledging delivery and off-target limitations. (cui2024spinocerebellarataxiasfrom pages 6-7, cui2024spinocerebellarataxiasfrom pages 9-10, cui2024spinocerebellarataxiasfrom pages 1-2)

### Suggested MAXO terms (candidates)
* Genetic testing — **MAXO:0000127** (genetic diagnostic action)
* Physical therapy — **MAXO:0000011** (supportive care; common in SCA management though not detailed in provided SCA17-specific excerpts)
* Occupational therapy — **MAXO:0000014**
* Speech therapy — **MAXO:0000121**

---

## 13. Prevention
No primary prevention is available for germline repeat-expansion disorders. Secondary prevention centers on early detection in at-risk families and genetic counseling. (rossi2023genotype–phenotypecorrelationsfor pages 1-1)

---

## 14. Other species / natural disease
No naturally occurring SCA17-like disease in non-human species was identified in the provided evidence set.

---

## 15. Model organisms
### Drosophila models (SCA17-specific)
A 2023 peer-reviewed study reports new Drosophila models expressing human TBP in wild-type versus SCA17-range polyQ lengths. The abstract states: “**Here, we report two new Drosophila models that express human TBP with polyQ repeats in either wild-type or SCA17 patient range.**” It further reports that “**SCA17 model flies accumulate more aggregation prone TBP, with a greater proportion localizing to the nucleus.**” (patel2023phenotypicdefectsfrom pages 1-2)

These models provide a platform for mechanistic dissection (aggregation, nuclear localization, tissue-specific neurodegeneration) and therapeutic target discovery. (patel2023phenotypicdefectsfrom pages 1-2)

---

## Key compiled facts table (evidence-backed)
| Item | Details | Evidence (PMID/DOI, year) |
|---|---|---|
| Disease / synonyms | Spinocerebellar ataxia type 17; ATX-TBP; Huntington disease-like 4 (HDL4); described as a rare autosomal dominant polyglutamine disorder with marked clinical heterogeneity. | DOI:10.1002/mds.29278, 2023 (rossi2023genotype–phenotypecorrelationsfor pages 1-1, rossi2023genotype–phenotypecorrelationsfor pages 2-2); DOI:10.1007/978-3-319-71779-1_10, 2018 (toyoshima2018spinocerebellarataxiatype pages 1-5) |
| Causal gene | **TBP** (TATA-box binding protein), chromosome 6q; expansion occurs in exon 3 and encodes an expanded polyglutamine tract. | DOI:10.3389/fncel.2018.00429, 2018 (nethisinghe2018complexityofthe pages 1-2); DOI:10.1007/978-3-319-71779-1_10, 2018 (toyoshima2018spinocerebellarataxiatype pages 1-5) |
| Mutation type | Germline mixed **CAG/CAA repeat expansion** in **TBP**; expansion of the polyglutamine-encoding tract causes SCA17. | DOI:10.3390/ijms25158190, 2024 (hoffmanzacharska2024thenewface pages 1-2); DOI:10.1002/mds.29278, 2023 (rossi2023genotype–phenotypecorrelationsfor pages 1-1) |
| Repeat-size categories: historical EMQN ranges | Earlier recommendations summarized as normal **25–42**, reduced penetrance **43–48**, full penetrance **49–66** CAG/CAA repeats. | DOI:10.1002/mds.29278, 2023 (rossi2023genotype–phenotypecorrelationsfor pages 2-2) |
| Repeat-size categories: updated 2023 MDSGene proposal | Updated cutoffs proposed from systematic review: reduced penetrance **41–45** repeats; full penetrance **46–66** repeats. Among curated cases, **97.7%** had **≥41** repeats; **99.6%** of PD patients and **99.9%** of healthy individuals had **≤42** repeats. | DOI:10.1002/mds.29278, 2023 (rossi2023genotype–phenotypecorrelationsfor pages 1-1, rossi2023genotype–phenotypecorrelationsfor media 82dfeaa1, rossi2023genotype–phenotypecorrelationsfor media 1829bb84) |
| Pathogenic range / uncertainty | Highest reported expanded alleles reach about **66** repeats. Because the normal–pathogenic gap is narrow, defining a strict cutoff is challenging; some studies/cases suggest variable penetrance and uncertainty around intermediate/small-expanded alleles. | DOI:10.1007/978-3-319-71779-1_10, 2018 (toyoshima2018spinocerebellarataxiatype pages 1-5); DOI:10.3389/fncel.2018.00429, 2018 (nethisinghe2018complexityofthe pages 1-2); DOI:10.1007/s10072-024-07453-4, 2024 (grassini2024cognitivedysfunctionsocial pages 1-3) |
| Core clinical feature: ataxia | Ataxia is the dominant phenotype; reported in **>90%** of patients in a review. Supportive cerebellar signs include dysarthria and eye-movement abnormalities. | DOI:10.1007/978-3-319-71779-1_10, 2018 (toyoshima2018spinocerebellarataxiatype pages 1-5); DOI:10.1002/mds.29278, 2023 (rossi2023genotype–phenotypecorrelationsfor pages 2-2) |
| Cognitive / dementia features | Dementia or intellectual deterioration is a major feature; dementia reported in **73%** overall in one review. For repeats **43–50**, **>75%** had intellectual deterioration; for **50–60**, **75%** had reduced intellectual function. | DOI:10.1007/978-3-319-71779-1_10, 2018 (toyoshima2018spinocerebellarataxiatype pages 1-5) |
| Psychiatric / behavioral features | Psychiatric symptoms are characteristic and may include psychosis, depression, and behavioral/social-cognition abnormalities; these contribute to the Huntington-like presentation. | DOI:10.1002/mds.29278, 2023 (rossi2023genotype–phenotypecorrelationsfor pages 2-2); DOI:10.1007/s10072-024-07453-4, 2024 (grassini2024cognitivedysfunctionsocial pages 1-3) |
| Hyperkinetic / parkinsonian features | Chorea and parkinsonism are well recognized. Pure parkinsonism is more common in carriers with **41–45** repeats, whereas carriers with **≥46** repeats more often show a complex mixed movement-disorder phenotype. | DOI:10.1002/mds.29278, 2023 (rossi2023genotype–phenotypecorrelationsfor pages 1-1); DOI:10.1007/978-3-319-71779-1_10, 2018 (toyoshima2018spinocerebellarataxiatype pages 1-5) |
| Other less-common features | Epilepsy/seizures about **20%**; autonomic dysfunction **9%**; apraxia **7%**; peripheral nerve involvement **3%** in one review. | DOI:10.1007/978-3-319-71779-1_10, 2018 (toyoshima2018spinocerebellarataxiatype pages 1-5) |
| Age at onset / progression | Very broad onset range, approximately **3–60** years in reviews/case reports, with juvenile severe disease often associated with very long repeats; disease is progressive and clinically variable even within families. | DOI:10.1007/978-3-319-71779-1_10, 2018 (toyoshima2018spinocerebellarataxiatype pages 1-5); DOI:10.3389/fncel.2018.00429, 2018 (nethisinghe2018complexityofthe pages 1-2); DOI:10.1007/s10072-024-07453-4, 2024 (grassini2024cognitivedysfunctionsocial pages 1-3) |
| Genotype–phenotype correlation | Total repeat length shows a negative correlation with age at onset in some cohorts, but phenotype is highly variable; contiguous CAG tract length did **not** correlate with age at onset in the UK cohort. | DOI:10.3389/fncel.2018.00429, 2018 (nethisinghe2018complexityofthe pages 1-2) |
| Anticipation / transmission | Genetic anticipation is less prominent than in several other polyQ disorders; repeat interruptions (CAA) are thought to reduce instability. | DOI:10.3389/fncel.2018.00429, 2018 (nethisinghe2018complexityofthe pages 1-2); DOI:10.3390/ijms25158190, 2024 (hoffmanzacharska2024thenewface pages 1-2) |
| 2024 repeat-structure development | A 2024 review reanalyzed **67** cases from **19** reports and proposed an alternative **three-unit** organization of the TBP repeat tract, arguing that **repeat structure/composition**, not only repeat count, may help predict transmission stability and anticipation. | DOI:10.3390/ijms25158190, 2024 (hoffmanzacharska2024thenewface pages 1-2) |
| 2023–2024 clinically relevant development | The 2023 MDSGene systematic review curated **346** patients and recommended revised penetrance thresholds, which have direct implications for diagnosis, counseling, and clinical-trial design. | DOI:10.1002/mds.29278, 2023 (rossi2023genotype–phenotypecorrelationsfor pages 1-1, rossi2023genotype–phenotypecorrelationsfor media 82dfeaa1, rossi2023genotype–phenotypecorrelationsfor media 1829bb84) |


*Table: This table summarizes core disease-definition, genetics, repeat-size interpretation, phenotype, and recent 2023-2024 updates for Spinocerebellar ataxia type 17. It is useful as a compact evidence-backed reference for knowledge-base population and diagnostic interpretation.*

---

## Evidence-based figure/table note
An extracted **Figure 3** and **Table 2** from the 2023 MDSGene systematic review provide a visual schematic of clinical features across revised repeat-size penetrance groups and a tabular summary of clinical features by the 41–45 vs 46–66 repeat categories. (rossi2023genotype–phenotypecorrelationsfor media 82dfeaa1, rossi2023genotype–phenotypecorrelationsfor media 1829bb84)

---

## Gaps / limitations of this report (based on available evidence set)
* OMIM/Orphanet/ICD/MeSH/MONDO identifiers were not retrieved by the current tool context and are therefore not asserted here.
* Robust prevalence/incidence estimates, survival statistics, and formal staging/progression rates were not available in the provided evidence set.
* Detailed biomarker and neuropathology summaries (e.g., Purkinje cell pathology, protein inclusions across brain regions) would require additional full-text sources beyond those retrieved here.


References

1. (toyoshima2018spinocerebellarataxiatype pages 1-5): Yasuko Toyoshima and Hitoshi Takahashi. Spinocerebellar ataxia type 17 (sca17). Advances in experimental medicine and biology, 1049:219-231, Jan 2018. URL: https://doi.org/10.1007/978-3-319-71779-1\_10, doi:10.1007/978-3-319-71779-1\_10. This article has 50 citations and is from a peer-reviewed journal.

2. (nethisinghe2018complexityofthe pages 1-2): Suran Nethisinghe, Wei N. Lim, Heather Ging, Anna Zeitlberger, Rosella Abeti, Sally Pemble, Mary G. Sweeney, Robyn Labrum, Charisse Cervera, Henry Houlden, Elisabeth Rosser, Patricia Limousin, Angus Kennedy, Michael P. Lunn, Kailash P. Bhatia, Nicholas W. Wood, John Hardy, James M. Polke, Liana Veneziano, Alfredo Brusco, Mary B. Davis, and Paola Giunti. Complexity of the genetics and clinical presentation of spinocerebellar ataxia 17. Frontiers in Cellular Neuroscience, Nov 2018. URL: https://doi.org/10.3389/fncel.2018.00429, doi:10.3389/fncel.2018.00429. This article has 30 citations.

3. (rossi2023genotype–phenotypecorrelationsfor pages 1-1): Malco Rossi, Moath Hamed, Jon Rodríguez‐Antigüedad, Mario Cornejo‐Olivas, Marianthi Breza, Katja Lohmann, Christine Klein, Rajasumi Rajalingam, Connie Marras, and Bart P. van de Warrenburg. Genotype–phenotype correlations for atx‐tbp (sca17): mdsgene systematic review. Movement Disorders, 38:368-377, Nov 2023. URL: https://doi.org/10.1002/mds.29278, doi:10.1002/mds.29278. This article has 22 citations and is from a highest quality peer-reviewed journal.

4. (rossi2023genotype–phenotypecorrelationsfor media 82dfeaa1): Malco Rossi, Moath Hamed, Jon Rodríguez‐Antigüedad, Mario Cornejo‐Olivas, Marianthi Breza, Katja Lohmann, Christine Klein, Rajasumi Rajalingam, Connie Marras, and Bart P. van de Warrenburg. Genotype–phenotype correlations for atx‐tbp (sca17): mdsgene systematic review. Movement Disorders, 38:368-377, Nov 2023. URL: https://doi.org/10.1002/mds.29278, doi:10.1002/mds.29278. This article has 22 citations and is from a highest quality peer-reviewed journal.

5. (hoffmanzacharska2024thenewface pages 1-2): Dorota Hoffman-Zacharska and Anna Sułek. The new face of dynamic mutation—the caa [cag]n caa cag motif as a mutable unit in the tbp gene causative for spino-cerebellar ataxia type 17. International Journal of Molecular Sciences, 25:8190, Jul 2024. URL: https://doi.org/10.3390/ijms25158190, doi:10.3390/ijms25158190. This article has 1 citations.

6. (rossi2023genotype–phenotypecorrelationsfor pages 2-2): Malco Rossi, Moath Hamed, Jon Rodríguez‐Antigüedad, Mario Cornejo‐Olivas, Marianthi Breza, Katja Lohmann, Christine Klein, Rajasumi Rajalingam, Connie Marras, and Bart P. van de Warrenburg. Genotype–phenotype correlations for atx‐tbp (sca17): mdsgene systematic review. Movement Disorders, 38:368-377, Nov 2023. URL: https://doi.org/10.1002/mds.29278, doi:10.1002/mds.29278. This article has 22 citations and is from a highest quality peer-reviewed journal.

7. (rossi2023genotype–phenotypecorrelationsfor pages 8-8): Malco Rossi, Moath Hamed, Jon Rodríguez‐Antigüedad, Mario Cornejo‐Olivas, Marianthi Breza, Katja Lohmann, Christine Klein, Rajasumi Rajalingam, Connie Marras, and Bart P. van de Warrenburg. Genotype–phenotype correlations for atx‐tbp (sca17): mdsgene systematic review. Movement Disorders, 38:368-377, Nov 2023. URL: https://doi.org/10.1002/mds.29278, doi:10.1002/mds.29278. This article has 22 citations and is from a highest quality peer-reviewed journal.

8. (grassini2024cognitivedysfunctionsocial pages 1-3): Alberto Grassini, Aurora Cermelli, Fausto Roveta, Michela Zotta, Adriana Lesca, Andrea Marcinnò, Fabio Ferrandes, Elisa Piella, Silvia Boschi, Chiara Lombardo, Alfredo Brusco, Salvatore Gallone, Elisa Rubino, Amalia Bruni, and Innocenzo Rainero. Cognitive dysfunction, social behavior disorder, cerebellar ataxia, and atypical brain fdg-pet presentation in spinocerebellar ataxia 17: a case report. Neurological sciences : official journal of the Italian Neurological Society and of the Italian Society of Clinical Neurophysiology, 45:2877-2880, Mar 2024. URL: https://doi.org/10.1007/s10072-024-07453-4, doi:10.1007/s10072-024-07453-4. This article has 2 citations.

9. (rossi2023genotype–phenotypecorrelationsfor media 1829bb84): Malco Rossi, Moath Hamed, Jon Rodríguez‐Antigüedad, Mario Cornejo‐Olivas, Marianthi Breza, Katja Lohmann, Christine Klein, Rajasumi Rajalingam, Connie Marras, and Bart P. van de Warrenburg. Genotype–phenotype correlations for atx‐tbp (sca17): mdsgene systematic review. Movement Disorders, 38:368-377, Nov 2023. URL: https://doi.org/10.1002/mds.29278, doi:10.1002/mds.29278. This article has 22 citations and is from a highest quality peer-reviewed journal.

10. (cui2024spinocerebellarataxiasfrom pages 1-2): Zi-Ting Cui, Zong-Tao Mao, Rong Yang, Jia-Jia Li, Shan-Shan Jia, Jian-Li Zhao, Fang-Tian Zhong, Peng Yu, and Ming Dong. Spinocerebellar ataxias: from pathogenesis to recent therapeutic advances. Frontiers in Neuroscience, Jun 2024. URL: https://doi.org/10.3389/fnins.2024.1422442, doi:10.3389/fnins.2024.1422442. This article has 32 citations and is from a peer-reviewed journal.

11. (patel2023phenotypicdefectsfrom pages 1-2): Nikhil C. Patel, Nadir Alam, Kozeta Libohova, Ryan O. Dulay, Sokol V. Todi, and A. Sujkowski. Phenotypic defects from the expression of wild-type and pathogenic tata-binding proteins in new <i>drosophila</i> models of spinocerebellar ataxia type 17. G3: Genes, Genomes, Genetics, Aug 2023. URL: https://doi.org/10.1093/g3journal/jkad180, doi:10.1093/g3journal/jkad180. This article has 11 citations and is from a domain leading peer-reviewed journal.

12. (NCT04301284 chunk 1):  Study of CAD-1883 for Spinocerebellar Ataxia. Cadent Therapeutics. 2021. ClinicalTrials.gov Identifier: NCT04301284

13. (NCT03701399 chunk 1):  Troriluzole in Adult Participants With Spinocerebellar Ataxia. Biohaven Pharmaceuticals, Inc.. 2019. ClinicalTrials.gov Identifier: NCT03701399

14. (cui2024spinocerebellarataxiasfrom pages 6-7): Zi-Ting Cui, Zong-Tao Mao, Rong Yang, Jia-Jia Li, Shan-Shan Jia, Jian-Li Zhao, Fang-Tian Zhong, Peng Yu, and Ming Dong. Spinocerebellar ataxias: from pathogenesis to recent therapeutic advances. Frontiers in Neuroscience, Jun 2024. URL: https://doi.org/10.3389/fnins.2024.1422442, doi:10.3389/fnins.2024.1422442. This article has 32 citations and is from a peer-reviewed journal.

15. (cui2024spinocerebellarataxiasfrom pages 9-10): Zi-Ting Cui, Zong-Tao Mao, Rong Yang, Jia-Jia Li, Shan-Shan Jia, Jian-Li Zhao, Fang-Tian Zhong, Peng Yu, and Ming Dong. Spinocerebellar ataxias: from pathogenesis to recent therapeutic advances. Frontiers in Neuroscience, Jun 2024. URL: https://doi.org/10.3389/fnins.2024.1422442, doi:10.3389/fnins.2024.1422442. This article has 32 citations and is from a peer-reviewed journal.