---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-09T09:25:07.035410'
end_time: '2026-05-09T09:41:57.662998'
duration_seconds: 1010.63
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Viral Hemorrhagic Fever
  mondo_id: ''
  category: Infectious
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 29
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Viral Hemorrhagic Fever
- **MONDO ID:**  (if available)
- **Category:** Infectious

## Research Objectives

Please provide a comprehensive research report on **Viral Hemorrhagic Fever** covering all of the
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
- **Disease Name:** Viral Hemorrhagic Fever
- **MONDO ID:**  (if available)
- **Category:** Infectious

## Research Objectives

Please provide a comprehensive research report on **Viral Hemorrhagic Fever** covering all of the
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


# Viral Hemorrhagic Fever (VHF): Comprehensive Disease Characteristics Report (Infectious)

## Target disease
**Disease name:** Viral Hemorrhagic Fever (VHF) — *a clinical syndrome/group of diseases*, not a single etiologic entity. (srivastav2024compendiummanagementof pages 1-3, perkins2026potentialmechanismsunderlying pages 1-3)

### Evidence base note
The report below is derived from **aggregated disease-level resources and the scientific literature** (mostly narrative reviews plus selected cohort/epidemiology studies), rather than EHR-derived single-patient datasets. (srivastav2024compendiummanagementof pages 1-3, alageedi2025viralhemorrhagicfever pages 9-11, fazlalipour2024crimeancongohaemorrhagicfever pages 1-2)

---

## 1. Disease information
### 1.1 Concise overview (definition)
VHF refers to a group of severe febrile illnesses characterized by **vascular dysregulation/damage** with variable hemorrhagic manifestations. One recent definition describes VHF as “a severe febrile illness characterized by aberrant vascular control, vascular damage, and hemorrhagic symptoms.” (srivastav2024compendiummanagementof pages 1-3)

A contemporary mechanistic framing emphasizes that **bleeding is not solely due to direct viral cytopathic effects**, but often results from **combined direct and host-response–mediated dysregulation of hemostasis** (coagulation factors, platelets, and endothelium). (perkins2026potentialmechanismsunderlying pages 1-3, perkins2026potentialmechanismsunderlying pages 6-8)

### 1.2 Causative virus families (current understanding)
Multiple virus families contain agents capable of producing VHF syndromes. Perkins & Mackman (2026) explicitly list **six** families: **Filoviridae, Nairoviridae, Phenuiviridae, Hantaviridae, Arenaviridae, Flaviviridae**. (perkins2026potentialmechanismsunderlying pages 1-3)

A separate 2024 review includes additional families in the broader “VHF” grouping (e.g., Paramyxoviridae) depending on taxonomy/classification usage. (srivastav2024compendiummanagementof pages 1-3)

### 1.3 Common synonyms / alternative names
- “Viral hemorrhagic fevers (VHFs)” (plural), “hemorrhagic fever viruses (HFVs)” (zaratesanchez2024vasculardysfunctionin pages 1-3)
- Historically for Ebola: “Ebola hemorrhagic fever” is cited as a synonym for “Ebola virus disease (EVD)”. (nicastri2019ebolavirusdisease pages 1-4)

### 1.4 Key identifiers (ontologies/codes)
**Limitations of retrieved evidence:** In the collected sources, explicit MeSH identifiers, MONDO IDs, ICD-10 codes, and a VHF-wide ICD-11 code were **not explicitly provided** for the umbrella syndrome “viral hemorrhagic fever.” (nicastri2019ebolavirusdisease pages 1-4)

However, ICD-11 is discussed in the context of filoviruses: a 2019 EVD review states that **substantial changes were proposed in ICD-11**, including an “innovative EVD case definition that links epidemiologic and clinical perspectives” to improve sensitivity relative to older hemorrhagic-fever–centric case definitions. (nicastri2019ebolavirusdisease pages 1-4)

**Ontology suggestions (for knowledge-base integration; not directly evidenced as exact codes in retrieved texts):**
- MONDO: likely exists as a grouped term (umbrella syndrome); not confirmed from evidence in this run.
- MeSH: “Hemorrhagic Fever, Viral” (commonly used); not confirmed with identifier string from evidence.

---

## 2. Etiology
### 2.1 Disease causal factors
**Primary cause:** infection with specific RNA viruses whose pathogenesis includes vascular/endothelial dysfunction, immune dysregulation, and/or coagulation abnormalities. (srivastav2024compendiummanagementof pages 1-3, perkins2026potentialmechanismsunderlying pages 1-3, zaratesanchez2024vasculardysfunctionin pages 1-3)

### 2.2 Risk factors
VHF risk is heavily driven by **ecologic exposure pathways**:
- **Zoonotic exposure to reservoirs** (e.g., rodent contact or aerosolized excreta for arenaviruses/hantaviruses). (srivastav2024compendiummanagementof pages 1-3, perkins2026potentialmechanismsunderlying pages 3-5)
- **Arthropod vectors** (mosquito- or tick-borne VHFs). (srivastav2024compendiummanagementof pages 1-3, perkins2026potentialmechanismsunderlying pages 3-5)
- **Nosocomial/occupational exposure** to blood/body fluids (particularly for CCHF and filoviruses). (srivastav2024compendiummanagementof pages 3-4, fazlalipour2024crimeancongohaemorrhagicfever pages 1-2)

**Healthcare worker exposure (quantitative, CCHF):** In an Iranian national reference-lab series (2000–2023), 12 confirmed HCW CCHF cases were linked to blood exposures; the most prevalent routes were needle-stick (3), mucosal blood splash (3), and skin contact with blood (3); median incubation 6.8 days (range 1–22). (fazlalipour2024crimeancongohaemorrhagicfever pages 1-2)

### 2.3 Protective factors
Protective factors are primarily **exposure and transmission control measures** and (for selected VHFs) **vaccination**.
- For Ebola (Zaire ebolavirus), **vaccination** with rVSV-ZEBOV (Ervebo) is a major protective intervention, with evidence from ring vaccination trials and outbreak deployment. (ayoubi2024recentadvancesin pages 5-6)

### 2.4 Gene–environment interactions
No robust, VHF-wide human gene–environment interaction loci were identified in the retrieved evidence for this run. The available sources emphasize exposure ecology and immune-pathogenesis rather than host genomic susceptibility. (perkins2026potentialmechanismsunderlying pages 1-3, zaratesanchez2024vasculardysfunctionin pages 1-3)

---

## 3. Phenotypes
### 3.1 Core clinical phenotype set (cross-VHF)
A typical VHF syndrome begins with **non-specific influenza-like illness** and can progress to shock and multi-organ failure.
- Early symptoms reported: fever, myalgia, headache, nausea/vomiting, diarrhea. (alageedi2025viralhemorrhagicfever pages 9-11, perkins2026potentialmechanismsunderlying pages 1-3)
- Hemorrhagic manifestations reported: petechiae, mucosal bleeding, GI bleeding, epistaxis, bruising, conjunctival injection. (alageedi2025viralhemorrhagicfever pages 9-11, perkins2026potentialmechanismsunderlying pages 1-3)
- Severe outcomes: shock, acute renal failure, neurological decline, multi-organ failure. (alageedi2025viralhemorrhagicfever pages 9-11)

**Abstract-quotable support (HFV vascular triad):** Zarate-Sanchez et al. (2024) describe HFVs as inducing “significant vascular dysfunction by affecting endothelial cells, altering immunity, and disrupting the clotting system.” (zaratesanchez2024vasculardysfunctionin pages 1-3)

### 3.2 Laboratory abnormalities (examples)
Across VHF agents, common abnormalities include **thrombocytopenia, coagulopathy, transaminase elevations, and leukopenia**.
- Perkins & Mackman emphasize thrombocytopenia/platelet dysfunction and coagulopathy in the bleeding phenotype across VHFs. (perkins2026potentialmechanismsunderlying pages 1-3, perkins2026potentialmechanismsunderlying pages 6-8)
- A 2024 review provides practical lab patterns: for EBOV/Sudan/CCHFV: leukopenia, thrombocytopenia, elevated ALT/AST; for dengue: platelet <100×10^9/L, prolonged aPTT with often normal PT, elevated ALT/AST. (srivastav2024compendiummanagementof pages 4-6)

**Quantitative HCW CCHF lab findings:** thrombocytopenia (100%), elevated aminotransferases (75%), leukopenia (66.7%); epistaxis was the most frequent hemorrhagic sign (41.7%). (fazlalipour2024crimeancongohaemorrhagicfever pages 2-3)

### 3.3 Age of onset / progression / frequency
Onset is typically **acute** (days to weeks after exposure) and severity varies by agent.
- Incubation examples: Ebola/Marburg 2–21 days; Lassa 1–3 weeks; CCHF 3–9 days after tick bite (5–13 after contact); yellow fever 3–6 days. (alageedi2025viralhemorrhagicfever pages 9-11)

### 3.4 Suggested HPO terms (examples; not exhaustive)
- Fever: **HP:0001945**
- Myalgia: **HP:0003326**
- Diarrhea: **HP:0002014**
- Vomiting: **HP:0002013**
- Petechiae: **HP:0000967**
- Epistaxis: **HP:0000421**
- Hematemesis: **HP:0002107**
- Melena/GI hemorrhage: **HP:0002249**
- Shock: **HP:0030149**
- Acute kidney injury: **HP:0001919**
- Thrombocytopenia: **HP:0001873**
- Leukopenia: **HP:0001882**
- Elevated hepatic transaminases: **HP:0002910**

(These HPO mappings are standard ontology suggestions; the supporting clinical findings are evidenced in the cited sources.) (alageedi2025viralhemorrhagicfever pages 9-11, perkins2026potentialmechanismsunderlying pages 1-3, srivastav2024compendiummanagementof pages 4-6, fazlalipour2024crimeancongohaemorrhagicfever pages 2-3)

---

## 4. Genetic / molecular information
### 4.1 Causal genes / variants
**Not applicable in the Mendelian sense**: VHF is infectious and not caused by germline pathogenic variants. The causal “genetic material” is viral genomes.

### 4.2 Viral proteins/mechanisms with host interaction (examples)
A 2024 review notes that VHF viruses target monocytes/macrophages/dendritic cells and endothelial cells, and that viral factors (example given: **VP35**) suppress type I interferon responses, contributing to cytokine activation and endothelial damage. (srivastav2024compendiummanagementof pages 4-6)

### 4.3 Host molecular biomarkers (examples)
- **Tissue factor (TF) induction** in PBMCs and extracellular vesicles is described for Ebola infection in nonhuman primate models. (perkins2026potentialmechanismsunderlying pages 1-3)

---

## 5. Environmental information
### 5.1 Environmental and exposure factors
- Rodent infestation in domiciles and food storage settings (rodent-borne transmission) (srivastav2024compendiummanagementof pages 1-3)
- Tick exposure in pastoral/rural settings (CCHF vectors such as Hyalomma ticks) (perkins2026potentialmechanismsunderlying pages 3-5)
- Mosquito exposure and livestock-associated ecology (RVF) (perkins2026potentialmechanismsunderlying pages 3-5)

### 5.2 Lifestyle / occupational factors
- Health-care work without adequate infection prevention and control (IPC) is a clear occupational risk (CCHF HCW series). (fazlalipour2024crimeancongohaemorrhagicfever pages 1-2)

---

## 6. Mechanism / pathophysiology
### 6.1 Unifying mechanistic framework (current understanding)
Across hemorrhagic fever viruses, a unifying framework is the **vascular triad**:
1) **Endothelial barrier disruption / vascular permeability**
2) **Derangement of blood clotting / hemostasis**
3) **Immune dysregulation**

This is explicitly stated in the 2024 Biofabrication review: “common features of the pathology include the triad of (1) disruption of the vascular endothelial barrier; (2) derangement of blood clotting; and (3) immune dysregulation.” (zaratesanchez2024vasculardysfunctionin pages 1-3)

### 6.2 Hemostasis/bleeding mechanisms (expert synthesis)
Perkins & Mackman (2026) summarize bleeding mechanisms in VHF as including:
- **Consumptive coagulopathy (DIC-like)**
- **Decreased coagulation factor production**
- **Thrombocytopenia and platelet dysfunction**
- **Endothelial activation/damage leading to increased vascular permeability**
They emphasize that both **direct viral infection effects** and **host responses** drive hemostatic dysregulation. (perkins2026potentialmechanismsunderlying pages 1-3)

### 6.3 Upstream-to-downstream causal chain (generalized)
**Exposure → infection of innate immune cells (dendritic cells/monocytes/macrophages) → impaired type I IFN signaling and immune evasion → cytokine amplification and tissue factor release → endothelial activation/damage + coagulation activation → microvascular instability and vascular leak → shock/multi-organ dysfunction; plus thrombocytopenia/consumptive coagulopathy → bleeding manifestations.** (srivastav2024compendiummanagementof pages 4-6, perkins2026potentialmechanismsunderlying pages 1-3, perkins2026potentialmechanismsunderlying pages 6-8)

### 6.4 Molecular pathways and ontology term suggestions
**GO Biological Process (suggested):**
- type I interferon signaling pathway (**GO:0060337**) (supported conceptually by IFN antagonism discussed in VHF pathogenesis) (srivastav2024compendiummanagementof pages 4-6)
- inflammatory response (**GO:0006954**) (srivastav2024compendiummanagementof pages 4-6)
- coagulation (**GO:0050817**) / hemostasis (**GO:0007599**) (perkins2026potentialmechanismsunderlying pages 6-8)
- platelet activation (**GO:0030168**) (perkins2026potentialmechanismsunderlying pages 6-8)
- regulation of vascular permeability (**GO:0043114**) / endothelial cell activation (**GO:0042118**) (perkins2026potentialmechanismsunderlying pages 1-3, zaratesanchez2024vasculardysfunctionin pages 1-3)

**Cell Ontology (CL) (suggested):**
- endothelial cell (**CL:0000115**) (zaratesanchez2024vasculardysfunctionin pages 1-3)
- monocyte (**CL:0000576**), macrophage (**CL:0000235**), dendritic cell (**CL:0000451**) (srivastav2024compendiummanagementof pages 4-6)
- platelet (**CL:0000233**) (perkins2026potentialmechanismsunderlying pages 6-8)

### 6.5 Recent development: organotypic modeling (2024)
The 2024 Biofabrication review argues that animal models and 2D cultures “fall short in replicating in vivo human vascular dynamics,” and highlights the emergence of **microphysiological systems (MPS)/organ-on-chip** to model HFV-induced vascular dysfunction and aid treatment development. (zaratesanchez2024vasculardysfunctionin pages 1-3)

---

## 7. Anatomical structures affected
### 7.1 Organ/system level
VHF is systemic and commonly involves multi-organ injury with prominent vascular/endothelial involvement.
- Commonly referenced organ involvement: liver, kidneys, heart, lungs in severe VHF presentations. (alageedi2025viralhemorrhagicfever pages 9-11)

**UBERON suggestions:**
- blood vessel (**UBERON:0001981**)
- endothelium (**UBERON:0001986**)
- liver (**UBERON:0002107**)
- kidney (**UBERON:0002113**)
- lung (**UBERON:0002048**)

### 7.2 Tissue/cellular targets
Endothelial cells and innate immune cells are repeatedly emphasized as key cellular compartments in pathogenesis. (srivastav2024compendiummanagementof pages 4-6, zaratesanchez2024vasculardysfunctionin pages 1-3)

---

## 8. Temporal development
### 8.1 Onset pattern
Typically **acute** with an incubation period of days to weeks depending on agent (see incubation examples above). (alageedi2025viralhemorrhagicfever pages 9-11)

### 8.2 Staging (example)
Marburg virus disease is described as having early/peak/resolution phases; several VHFs have characteristic stage-based clinical progression (e.g., HFRS phases). (perkins2026potentialmechanismsunderlying pages 3-5)

---

## 9. Inheritance and population
### 9.1 Epidemiology and burden (selected quantitative statistics)
VHF burden is outbreak-driven and varies greatly by virus and setting.

**Agent-level quantitative examples (from a mechanistic review table/summary):**
- Marburg virus disease: hemorrhagic manifestations 34–83%; average CFR ~50%. (perkins2026potentialmechanismsunderlying pages 3-5, perkins2026potentialmechanismsunderlying media b84e671f)
- Lassa: ~80% asymptomatic; ~20% progress to severe disease; overt bleeding up to 40% of cases (perkins2026potentialmechanismsunderlying pages 3-5); overall CFR values are context-dependent (quantitative summary appears in Table 2). (perkins2026potentialmechanismsunderlying media b84e671f)
- Rift Valley fever: <1% develop hemorrhagic manifestations; estimate of ~500,000 infections between 1997 and 2010. (perkins2026potentialmechanismsunderlying pages 3-5)
- Hantaan virus (HFRS): overall CFR ~1%. (perkins2026potentialmechanismsunderlying pages 3-5)

**Syndrome-level trend:** VHF incidence may increase with expanding vector ranges and increased contact with animal reservoirs/hosts. (perkins2026potentialmechanismsunderlying pages 1-3)

### 9.2 Demographics / high-risk groups
- Healthcare workers and caregivers have elevated risk during outbreaks (e.g., nosocomial CCHF exposures). (fazlalipour2024crimeancongohaemorrhagicfever pages 1-2)
- Populations in endemic rural settings with rodent or tick exposure and limited IPC resources are at high risk. (srivastav2024compendiummanagementof pages 1-3, perkins2026potentialmechanismsunderlying pages 3-5)

---

## 10. Diagnostics
### 10.1 Standard clinical and laboratory testing approach
VHF diagnosis is challenging early because symptoms overlap with many febrile illnesses. (alageedi2025viralhemorrhagicfever pages 9-11, wupori2026crisprbaseddetectionof pages 1-2)

**Preferred acute diagnostic modality:** RT-PCR on blood and other fluids is described as highly sensitive/specific in acute illness in a 2024 VHF management review; viral culture is restricted to high-containment laboratories. (srivastav2024compendiummanagementof pages 4-6)

**Serology limitations:** A 2025 VHF review notes that serology may be less helpful acutely and that ELISA can lack specificity due to cross-reactivity (notably within flaviviruses and bunyaviruses). (alageedi2025viralhemorrhagicfever pages 9-11)

**Real-world diagnostic yield (CCHF HCWs):** RT-PCR positive in 11/12 (91.7%); IgM ELISA positive in 3/12 (25%). (fazlalipour2024crimeancongohaemorrhagicfever pages 1-2)

### 10.2 Emerging diagnostics (point-of-care direction)
A 2026 review highlights that current molecular/serological tests “lack the characteristics required of a POC test” for rapid outbreak response, and argues that CRISPR-based diagnostics have attractive POCT features (sensitivity/specificity, adaptability, low cost, quick turnaround). (wupori2026crisprbaseddetectionof pages 1-2)

**Note:** This is later than the requested 2023–2024 window but provides a current synthesis of the POC diagnostics direction. (wupori2026crisprbaseddetectionof pages 1-2)

### 10.3 Suggested LOINC-style lab concepts (examples)
- Platelet count (thrombocytopenia)
- PT/INR and aPTT (coagulopathy)
- ALT/AST (transaminase elevation)
- Creatinine/BUN (renal impairment)
These test categories are explicitly referenced as part of clinical evaluation in VHF management reviews. (srivastav2024compendiummanagementof pages 4-6)

---

## 11. Outcome / prognosis
### 11.1 Mortality and CFR variability
Case fatality varies widely by virus and outbreak context.
- The mechanistic VHF review reports Ebola pooled CFR ~60% with hemorrhagic symptoms up to ~50% (summary). (perkins2026potentialmechanismsunderlying pages 1-3)
- In Ebola, delayed therapy is associated with worse outcomes; one review reports “increased the odds of death by 11% for each day of delayed…therapy.” (ayoubi2024recentadvancesin pages 1-2)

### 11.2 Complications and sequelae
- Severe disease may culminate in shock and multi-organ failure (liver, kidneys, heart, lungs). (alageedi2025viralhemorrhagicfever pages 9-11)
- Viral persistence in immune-privileged sites is noted as a post-acute concern in VHF clinical literature (general concept discussed in management reviews). (srivastav2024compendiummanagementof pages 3-4)

---

## 12. Treatment
### 12.1 General management
For most VHFs, **supportive care is the cornerstone** (fluids/electrolytes, monitoring, organ support), plus strict isolation and PPE. (alageedi2025viralhemorrhagicfever pages 9-11, srivastav2024compendiummanagementof pages 6-7)

### 12.2 Pathogen-targeted therapies (Ebola as the main approved example)
**FDA-approved Ebola therapeutics (Zaire ebolavirus):**
- **Inmazeb** (atoltivimab/maftivimab/odesivimab; REGN-EB3) — FDA approval 2020 (review summary). (ayoubi2024recentadvancesin pages 1-2)
- **Ebanga** (ansuvimab; mAb114) — FDA approval 2020 (review summary). (ayoubi2024recentadvancesin pages 1-2)

### 12.3 Vaccines and real-world implementation
**Ervebo (rVSV-ZEBOV) vaccine**
- Regulatory milestone: first FDA-approved vaccine for EBOV in 2019; expanded FDA approval for children ≥1 year in 2023 (reviewed). (ayoubi2024recentadvancesin pages 1-2, ayoubi2024recentadvancesin pages 5-6)
- Ring vaccination effectiveness: in Guinea 2015 trial, “none of 2,119 immediately vaccinated contacts developed EVD at 10 days versus 16 cases in delayed vaccination,” and outbreak deployments reported high effectiveness estimates (review summary). (ayoubi2024recentadvancesin pages 5-6)
- Implementation constraints: stringent cold chain (e.g., <−60°C long-term), limited stability after thaw. (ayoubi2024recentadvancesin pages 5-6)

### 12.4 Antivirals used/considered across VHFs
- **Ribavirin** is repeatedly cited as potentially helpful for Lassa fever and possibly CCHF, with variable evidence quality. (srivastav2024compendiummanagementof pages 4-6, alageedi2025viralhemorrhagicfever pages 9-11)
- **Favipiravir** and other candidates appear as investigational in VHF management discussions. (srivastav2024compendiummanagementof pages 4-6)

### 12.5 MAXO term suggestions (examples)
- Supportive care: **MAXO:0000058** (supportive therapy; generic)
- Intravenous fluid administration
- Administration of monoclonal antibody therapy
- Vaccination
- Infection control / isolation
(These are suggested mapping targets; intervention concepts are evidenced in cited sources.) (srivastav2024compendiummanagementof pages 6-7, ayoubi2024recentadvancesin pages 5-6)

### 12.6 Clinical trials (selected examples from ClinicalTrials.gov search results)
VHF-related vaccine trials present in the retrieved trial set include:
- Rift Valley fever vaccine studies: e.g., **NCT03609398** (Phase 2, recruiting), **NCT04672824**, **NCT04754776**, **NCT06799234**. (srivastav2024compendiummanagementof pages 3-4)
- Ebola/Marburg vaccine trials: e.g., **NCT00605514**, **NCT00997607**, **NCT04723602**. (srivastav2024compendiummanagementof pages 3-4)

---

## 13. Prevention
### 13.1 Primary prevention
- **Vaccination** where available (e.g., EBOV with Ervebo; yellow fever vaccine referenced as available in VHF reviews). (ayoubi2024recentadvancesin pages 5-6, alageedi2025viralhemorrhagicfever pages 9-11)
- **Vector control** (mosquito/tick) and **rodent control** in endemic settings to reduce spillover. (srivastav2024compendiummanagementof pages 1-3)

### 13.2 Secondary/tertiary prevention
- Early detection, isolation, contact tracing, and PPE/IPC to prevent transmission amplification and nosocomial spread. (srivastav2024compendiummanagementof pages 6-7, fazlalipour2024crimeancongohaemorrhagicfever pages 1-2)

---

## 14. Other species / natural disease
VHF ecology is frequently zoonotic with distinct reservoirs/vectors by agent:
- EBOV: fruit bats are thought reservoirs (srivastav2024compendiummanagementof pages 1-3)
- Lassa: multimammate rats (*Mastomys*) (perkins2026potentialmechanismsunderlying pages 3-5)
- CCHF: *Hyalomma* ticks (perkins2026potentialmechanismsunderlying pages 3-5)
- RVF: mosquitoes and livestock (perkins2026potentialmechanismsunderlying pages 3-5)

---

## 15. Model organisms
### 15.1 In vivo models
Nonhuman primate models are repeatedly emphasized for studying VHF-associated hemostatic dysregulation and biomarker dynamics (e.g., tissue factor induction in Ebola NHP models). (perkins2026potentialmechanismsunderlying pages 1-3)

### 15.2 Organotypic / in vitro advanced models (2024 development)
Microphysiological systems (“organ-on-chip”) are highlighted as a key emerging platform to capture **human vascular dynamics** not well represented in animals or 2D culture. (zaratesanchez2024vasculardysfunctionin pages 1-3, zaratesanchez2024vasculardysfunctionin pages 29-30)

---

## Cross-agent quantitative summary (evidence table)
The following table summarizes the major VHF families and representative agents, including reservoirs/vectors, transmission routes, diagnostic notes, and severity metrics.

| Virus family (ICTV) | Representative virus / disease | Typical reservoir / vector | Key transmission routes | Approx. CFR / hemorrhage frequency | Incubation period | Key diagnostic notes |
|---|---|---|---|---|---|---|
| **Filoviridae** | Ebola virus / Ebola virus disease | Fruit bats thought to be reservoir; humans accidental hosts | Person-to-person and nosocomial spread via body fluids; zoonotic spillover (srivastav2024compendiummanagementof pages 1-3, srivastav2024compendiummanagementof pages 6-7) | Pooled CFR ~60%; hemorrhagic symptoms in up to ~50% of cases (quantitative summary from Table 2) (perkins2026potentialmechanismsunderlying pages 1-3, perkins2026potentialmechanismsunderlying media b84e671f) | 2–21 days (alageedi2025viralhemorrhagicfever pages 9-11) | RT-PCR on blood/urine/saliva is highly sensitive/specific in acute illness; IgM/IgG usually appear around days 3 and 7; serology less sensitive acutely (srivastav2024compendiummanagementof pages 4-6) |
| **Filoviridae** | Marburg virus / Marburg virus disease | Not specified in gathered evidence | Person-to-person and nosocomial spread recognized within VHF syndrome (srivastav2024compendiummanagementof pages 1-3) | Average CFR ~50%; hemorrhagic manifestations 34–83% (quantitative summary from Table 2) (perkins2026potentialmechanismsunderlying pages 3-5, perkins2026potentialmechanismsunderlying media b84e671f) | 2–21 days (alageedi2025viralhemorrhagicfever pages 9-11) | Acute diagnosis prioritizes RT-PCR; serology supportive later, but acute serology is less useful (srivastav2024compendiummanagementof pages 4-6, alageedi2025viralhemorrhagicfever pages 9-11) |
| **Arenaviridae** | Lassa virus / Lassa fever | Multimammate rat (*Mastomys*); rodent-borne (perkins2026potentialmechanismsunderlying pages 3-5) | Contact with rodents or aerosolized excreta; secondary interhuman spread also occurs within VHF syndrome (srivastav2024compendiummanagementof pages 1-3, srivastav2024compendiummanagementof pages 3-4) | ~80% asymptomatic; ~20% progress to severe disease; overt bleeding up to 40% of cases; overall CFR ~1% in quantitative summary, but outbreak CFR can be much higher in some reports (perkins2026potentialmechanismsunderlying pages 3-5, perkins2026potentialmechanismsunderlying media b84e671f, srivastav2024compendiummanagementof pages 3-4) | 1–3 weeks (alageedi2025viralhemorrhagicfever pages 9-11) | RT-PCR preferred in acute phase; ribavirin noted as used clinically; serology less sensitive early (srivastav2024compendiummanagementof pages 4-6, srivastav2024compendiummanagementof pages 6-7) |
| **Nairoviridae** | Crimean-Congo hemorrhagic fever virus / CCHF | *Hyalomma* ticks (vector) (perkins2026potentialmechanismsunderlying pages 3-5) | Tick bite; contact with infected animal blood/tissues; human-to-human and occupational/nosocomial exposure via blood/body fluids (perkins2026potentialmechanismsunderlying pages 3-5, alageedi2025viralhemorrhagicfever pages 9-11) | Severe cases: hemorrhagic symptoms up to 50% of symptomatic individuals (<6% of all infections); severe cases may develop DIC; reported CFR ranges 5–50% or 10–40% across sources (perkins2026potentialmechanismsunderlying pages 3-5, alageedi2025viralhemorrhagicfever pages 9-11) | Typically 3–9 days after tick bite; 5–13 days after contact exposure (alageedi2025viralhemorrhagicfever pages 9-11) | RT-PCR is preferred acutely; IgM capture ELISA used, but serology may lack specificity/cross-react; ribavirin may be helpful (srivastav2024compendiummanagementof pages 4-6, alageedi2025viralhemorrhagicfever pages 9-11) |
| **Phenuiviridae** | Rift Valley fever virus / Rift Valley fever | *Aedes* mosquitoes and infected livestock (perkins2026potentialmechanismsunderlying pages 3-5) | Vector-borne and animal exposure (perkins2026potentialmechanismsunderlying pages 3-5, srivastav2024compendiummanagementof pages 1-3) | Most infections mild/subclinical; <1% develop hemorrhagic manifestations; estimates suggest ~500,000 infections during 1997–2010 (perkins2026potentialmechanismsunderlying pages 3-5) | Not specified in gathered evidence | Acute diagnosis generally favors RT-PCR; serology useful later but less reliable early in VHF settings (srivastav2024compendiummanagementof pages 4-6, alageedi2025viralhemorrhagicfever pages 9-11) |
| **Hantaviridae** | Hantaan virus / hemorrhagic fever with renal syndrome (HFRS) | Rodent hosts (Old World and New World rodent reservoirs noted) (perkins2026potentialmechanismsunderlying pages 3-5) | Rodent-associated exposure, including aerosolized excreta within VHF syndrome (srivastav2024compendiummanagementof pages 1-3, perkins2026potentialmechanismsunderlying pages 3-5) | Overall CFR for Hantaan infection ~1% (perkins2026potentialmechanismsunderlying pages 3-5) | Not specified in gathered evidence | RT-PCR preferred acutely; characteristic labs can include elevated BUN/creatinine in Hantaan/Seoul infections (srivastav2024compendiummanagementof pages 4-6) |
| **Flaviviridae** | Dengue virus / dengue hemorrhagic fever | Arthropod-borne; mosquito vector implied within VHF group (srivastav2024compendiummanagementof pages 1-3, srivastav2024compendiummanagementof pages 3-4) | Mosquito-borne transmission (srivastav2024compendiummanagementof pages 1-3) | CFR ~0.8–2.5%; thrombocytopenia/platelet dysfunction emphasized (srivastav2024compendiummanagementof pages 3-4, srivastav2024compendiummanagementof pages 1-3, srivastav2024compendiummanagementof pages 4-6) | Not specified in gathered evidence | Dengue often shows elevated ALT/AST, normal PT, prolonged aPTT, platelets <100 × 10^9/L; RT-PCR preferred acutely, serology may cross-react (srivastav2024compendiummanagementof pages 4-6, alageedi2025viralhemorrhagicfever pages 9-11) |
| **Flaviviridae** | Yellow fever / yellow fever hemorrhagic disease | Arthropod-borne; mosquito vector implied within VHF group (srivastav2024compendiummanagementof pages 1-3) | Mosquito-borne transmission (srivastav2024compendiummanagementof pages 1-3) | Quantitative CFR/hemorrhage frequency not specified in gathered evidence | 3–6 days (alageedi2025viralhemorrhagicfever pages 9-11) | Vaccine exists; acute VHF diagnosis still relies on molecular testing when available, while serology may cross-react in flaviviruses (alageedi2025viralhemorrhagicfever pages 9-11, srivastav2024compendiummanagementof pages 4-6) |
| **VHF syndrome (cross-pathogen summary)** | Viral hemorrhagic fever as a syndrome | Rodents, bats, ticks, mosquitoes, and infected animals are recurrent reservoirs/vectors depending on virus (srivastav2024compendiummanagementof pages 1-3, perkins2026potentialmechanismsunderlying pages 3-5) | Zoonotic spillover, arthropod-borne spread, and person-to-person/nosocomial transmission depending on agent (srivastav2024compendiummanagementof pages 3-4, srivastav2024compendiummanagementof pages 1-3) | Hallmarks include high-fatality potential, coagulopathy, thrombocytopenia, endothelial dysfunction, and DIC in severe disease (perkins2026potentialmechanismsunderlying pages 1-3, srivastav2024compendiummanagementof pages 4-6, perkins2026potentialmechanismsunderlying pages 6-8) | Variable by virus | General approach: RT-PCR is the main acute diagnostic test; serology (IgM/IgG ELISA) is more supportive later and may be less useful or less specific early in disease (srivastav2024compendiummanagementof pages 4-6, alageedi2025viralhemorrhagicfever pages 9-11) |


*Table: This table summarizes Viral Hemorrhagic Fever as a syndrome and the major causative virus families with representative agents, transmission ecology, approximate severity metrics, incubation periods, and diagnostic notes. It is useful as a compact disease-knowledge-base overview grounded in the gathered evidence, including quantitative values extracted from the Table 2 image in Perkins & Mackman 2026.*

A key quantitative source used for several CFR/hemorrhage frequency entries is **Table 2** from Perkins & Mackman (2026), retrieved as an image. (perkins2026potentialmechanismsunderlying media b84e671f)

---

## Expert opinion / analysis (authoritative synthesis)
1. **VHF is best treated as a syndrome defined by shared vascular/hemostatic failure pathways rather than by hemorrhage alone.** Hemorrhage can be absent or variable across agents and outbreaks; pathogenesis commonly involves coagulation and endothelial activation/dysfunction. (perkins2026potentialmechanismsunderlying pages 1-3, zaratesanchez2024vasculardysfunctionin pages 1-3)
2. **The main translational bottleneck is that broad disease-modifying therapies remain elusive,** while supportive care still dominates for most VHFs; Ebola is the major exception with approved mAbs and vaccines. (zaratesanchez2024vasculardysfunctionin pages 1-3, ayoubi2024recentadvancesin pages 1-2)
3. **Next-generation modeling and diagnostics are increasingly central to preparedness:** microphysiological vascular systems to improve mechanistic inference and therapy screening (2024) (zaratesanchez2024vasculardysfunctionin pages 1-3) and point-of-care molecular diagnostics (e.g., CRISPR-based) to reduce delays and improve biosafety during outbreaks (2026 synthesis). (wupori2026crisprbaseddetectionof pages 1-2)

---

## URLs and publication dates (selected high-priority sources used)
- Zarate-Sanchez E. et al. *Biofabrication* (Published 2024-06-05). https://doi.org/10.1088/1758-5090/ad4c0b (zaratesanchez2024vasculardysfunctionin pages 1-3)
- El Ayoubi L. W. E. et al. *PLOS Pathogens* (Published 2024-03). https://doi.org/10.1371/journal.ppat.1012038 (ayoubi2024recentadvancesin pages 1-2)
- Fazlalipour M. et al. *BMC Infectious Diseases* (Published 2024-11). https://doi.org/10.1186/s12879-024-10199-1 (fazlalipour2024crimeancongohaemorrhagicfever pages 1-2)
- Srivastav Y. et al. *Asian J Res Infect Dis* (Published 2024-03). https://doi.org/10.9734/ajrid/2024/v15i3334 (srivastav2024compendiummanagementof pages 1-3)
- Perkins M. V., Mackman N. *ATVB* (Published 2026-02). https://doi.org/10.1161/atvbaha.125.323625 (perkins2026potentialmechanismsunderlying pages 1-3)

---

## Gaps / items not fully resolved from retrieved evidence in this run
- **Explicit MONDO ID, MeSH IDs, and ICD-10/ICD-11 codes for the umbrella “viral hemorrhagic fever” entry** were not directly extractable from the gathered sources; ICD-11 changes were discussed mainly for EVD case definitions rather than VHF as a single ICD entity. (nicastri2019ebolavirusdisease pages 1-4)
- **Population-level global prevalence/incidence** for the VHF umbrella entity was not available in the retrieved evidence; agent-level outbreak statistics were available for some viruses. (perkins2026potentialmechanismsunderlying pages 3-5, ayoubi2024recentadvancesin pages 5-6)


References

1. (srivastav2024compendiummanagementof pages 1-3): Yash Srivastav, Aniket Kumar, Jaya Singh, Aditya Srivastav, and Mohd. Imtiyaz Ahmad. Compendium: management of viral hemorrhagic fever (viral fever), involving its pathogenesis. Asian Journal of Research in Infectious Diseases, 15:17-25, Mar 2024. URL: https://doi.org/10.9734/ajrid/2024/v15i3334, doi:10.9734/ajrid/2024/v15i3334. This article has 4 citations.

2. (perkins2026potentialmechanismsunderlying pages 1-3): Megan V. Perkins and Nigel Mackman. Potential mechanisms underlying bleeding during infection with hemorrhagic fever viruses. Arteriosclerosis, Thrombosis, and Vascular Biology, Feb 2026. URL: https://doi.org/10.1161/atvbaha.125.323625, doi:10.1161/atvbaha.125.323625. This article has 2 citations and is from a domain leading peer-reviewed journal.

3. (alageedi2025viralhemorrhagicfever pages 9-11): Neyaf Majid Alageedi, Samar Abdulwahab Abdulla Mutar, Huda Abdul Hameed, Ragda Ayad Taha, and Shahrazad Ahmed khalah. Viral hemorrhagic fever: a literature review. Osol Journal for Medical Sciences, 3:36-49, Jun 2025. URL: https://doi.org/10.69946/ojms/2025.03.004, doi:10.69946/ojms/2025.03.004. This article has 0 citations.

4. (fazlalipour2024crimeancongohaemorrhagicfever pages 1-2): Mehdi Fazlalipour, Tahmineh Jalali, Roger Hewson, Mohammad Hassan Pouriayevali, and Mostafa Salehi-Vaziri. Crimean-congo haemorrhagic fever among healthcare workers in iran 2000–2023, a report of national reference laboratory. BMC Infectious Diseases, Nov 2024. URL: https://doi.org/10.1186/s12879-024-10199-1, doi:10.1186/s12879-024-10199-1. This article has 10 citations and is from a peer-reviewed journal.

5. (perkins2026potentialmechanismsunderlying pages 6-8): Megan V. Perkins and Nigel Mackman. Potential mechanisms underlying bleeding during infection with hemorrhagic fever viruses. Arteriosclerosis, Thrombosis, and Vascular Biology, Feb 2026. URL: https://doi.org/10.1161/atvbaha.125.323625, doi:10.1161/atvbaha.125.323625. This article has 2 citations and is from a domain leading peer-reviewed journal.

6. (zaratesanchez2024vasculardysfunctionin pages 1-3): Evelyn Zarate-Sanchez, Steven C George, Monica L Moya, and Claire Robertson. Vascular dysfunction in hemorrhagic viral fevers: opportunities for organotypic modeling. Biofabrication, 16:032008, Jun 2024. URL: https://doi.org/10.1088/1758-5090/ad4c0b, doi:10.1088/1758-5090/ad4c0b. This article has 11 citations and is from a peer-reviewed journal.

7. (nicastri2019ebolavirusdisease pages 1-4): Emanuele Nicastri, Gary Kobinger, Francesco Vairo, Chiara Montaldo, Leonard E.G. Mboera, Rashid Ansunama, Alimuddin Zumla, and Giuseppe Ippolito. Ebola virus disease: epidemiology, clinical features, management, and prevention. Infectious disease clinics of North America, 33 4:953-976, Dec 2019. URL: https://doi.org/10.1016/j.idc.2019.08.005, doi:10.1016/j.idc.2019.08.005. This article has 96 citations and is from a peer-reviewed journal.

8. (perkins2026potentialmechanismsunderlying pages 3-5): Megan V. Perkins and Nigel Mackman. Potential mechanisms underlying bleeding during infection with hemorrhagic fever viruses. Arteriosclerosis, Thrombosis, and Vascular Biology, Feb 2026. URL: https://doi.org/10.1161/atvbaha.125.323625, doi:10.1161/atvbaha.125.323625. This article has 2 citations and is from a domain leading peer-reviewed journal.

9. (srivastav2024compendiummanagementof pages 3-4): Yash Srivastav, Aniket Kumar, Jaya Singh, Aditya Srivastav, and Mohd. Imtiyaz Ahmad. Compendium: management of viral hemorrhagic fever (viral fever), involving its pathogenesis. Asian Journal of Research in Infectious Diseases, 15:17-25, Mar 2024. URL: https://doi.org/10.9734/ajrid/2024/v15i3334, doi:10.9734/ajrid/2024/v15i3334. This article has 4 citations.

10. (ayoubi2024recentadvancesin pages 5-6): L’Emir Wassim El Ayoubi, Omar Mahmoud, Johnny Zakhour, and Souha S. Kanj. Recent advances in the treatment of ebola disease: a brief overview. PLOS Pathogens, 20:e1012038, Mar 2024. URL: https://doi.org/10.1371/journal.ppat.1012038, doi:10.1371/journal.ppat.1012038. This article has 49 citations and is from a highest quality peer-reviewed journal.

11. (srivastav2024compendiummanagementof pages 4-6): Yash Srivastav, Aniket Kumar, Jaya Singh, Aditya Srivastav, and Mohd. Imtiyaz Ahmad. Compendium: management of viral hemorrhagic fever (viral fever), involving its pathogenesis. Asian Journal of Research in Infectious Diseases, 15:17-25, Mar 2024. URL: https://doi.org/10.9734/ajrid/2024/v15i3334, doi:10.9734/ajrid/2024/v15i3334. This article has 4 citations.

12. (fazlalipour2024crimeancongohaemorrhagicfever pages 2-3): Mehdi Fazlalipour, Tahmineh Jalali, Roger Hewson, Mohammad Hassan Pouriayevali, and Mostafa Salehi-Vaziri. Crimean-congo haemorrhagic fever among healthcare workers in iran 2000–2023, a report of national reference laboratory. BMC Infectious Diseases, Nov 2024. URL: https://doi.org/10.1186/s12879-024-10199-1, doi:10.1186/s12879-024-10199-1. This article has 10 citations and is from a peer-reviewed journal.

13. (perkins2026potentialmechanismsunderlying media b84e671f): Megan V. Perkins and Nigel Mackman. Potential mechanisms underlying bleeding during infection with hemorrhagic fever viruses. Arteriosclerosis, Thrombosis, and Vascular Biology, Feb 2026. URL: https://doi.org/10.1161/atvbaha.125.323625, doi:10.1161/atvbaha.125.323625. This article has 2 citations and is from a domain leading peer-reviewed journal.

14. (wupori2026crisprbaseddetectionof pages 1-2): Kylene Wupori, Lauren Garnett, Alexander Bello, and James E. Strong. Crispr-based detection of viral hemorrhagic fevers at the point of care. Viruses, 18:218, Feb 2026. URL: https://doi.org/10.3390/v18020218, doi:10.3390/v18020218. This article has 0 citations.

15. (ayoubi2024recentadvancesin pages 1-2): L’Emir Wassim El Ayoubi, Omar Mahmoud, Johnny Zakhour, and Souha S. Kanj. Recent advances in the treatment of ebola disease: a brief overview. PLOS Pathogens, 20:e1012038, Mar 2024. URL: https://doi.org/10.1371/journal.ppat.1012038, doi:10.1371/journal.ppat.1012038. This article has 49 citations and is from a highest quality peer-reviewed journal.

16. (srivastav2024compendiummanagementof pages 6-7): Yash Srivastav, Aniket Kumar, Jaya Singh, Aditya Srivastav, and Mohd. Imtiyaz Ahmad. Compendium: management of viral hemorrhagic fever (viral fever), involving its pathogenesis. Asian Journal of Research in Infectious Diseases, 15:17-25, Mar 2024. URL: https://doi.org/10.9734/ajrid/2024/v15i3334, doi:10.9734/ajrid/2024/v15i3334. This article has 4 citations.

17. (zaratesanchez2024vasculardysfunctionin pages 29-30): Evelyn Zarate-Sanchez, Steven C George, Monica L Moya, and Claire Robertson. Vascular dysfunction in hemorrhagic viral fevers: opportunities for organotypic modeling. Biofabrication, 16:032008, Jun 2024. URL: https://doi.org/10.1088/1758-5090/ad4c0b, doi:10.1088/1758-5090/ad4c0b. This article has 11 citations and is from a peer-reviewed journal.