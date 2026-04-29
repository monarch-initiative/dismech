---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-05T15:49:42.456412'
end_time: '2026-04-05T16:00:14.028317'
duration_seconds: 631.57
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: HER2-Positive Colorectal Cancer
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 37
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** HER2-Positive Colorectal Cancer
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **HER2-Positive Colorectal Cancer** covering all of the
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
- **Disease Name:** HER2-Positive Colorectal Cancer
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **HER2-Positive Colorectal Cancer** covering all of the
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


# HER2-Positive Colorectal Cancer (CRC): Comprehensive Disease Characteristics Report (2023–2024 prioritized)

## Target disease
- **Disease name:** HER2-Positive Colorectal Cancer (CRC)
- **Category:** Molecularly defined subtype of colorectal adenocarcinoma (often discussed in metastatic CRC precision oncology)
- **MONDO / OMIM / Orphanet / MeSH / ICD-10/11 identifiers:** Not retrieved from the available evidence in this tool run; the subtype is most consistently represented in the literature as *“HER2-positive CRC”*, *“ERBB2-amplified CRC”*, or *“HER2-amplified metastatic CRC”* rather than as a standalone ontology disease entity. (singh2024systematicliteraturereview pages 1-2, sun2023her2overexpressionamplificationstatus pages 2-4)

---

## 1. Disease information
### 1.1 Concise overview
HER2-positive colorectal cancer refers to CRCs with **ERBB2 (HER2) amplification and/or HER2 protein overexpression** that may act as an oncogenic driver and therapeutic target. In CRC, HER2 positivity is clinically used to select patients for HER2-directed therapy, particularly in **metastatic CRC (mCRC)** and often in the context of **RAS wild-type** disease. (singh2024systematicliteraturereview pages 1-2, singh2024rasrafcomutationand pages 2-4)

### 1.2 Common synonyms / alternative names
- **ERBB2-amplified CRC** (genomic definition) (singh2024rasrafcomutationand pages 2-4)
- **HER2-amplified metastatic colorectal cancer** (real-world genomic testing cohorts) (strickler2023realworldtreatmentpatterns pages 1-2)
- **HER2-expressing metastatic colorectal cancer** (trial language including IHC/ISH stratification) (yoshino2023finalresultsof pages 1-2)

### 1.3 Evidence source type
Information summarized here is primarily from:
- **Aggregated disease-level resources** (systematic review/meta-analysis) (singh2024systematicliteraturereview pages 1-2, singh2024systematicliteraturereview pages 4-7)
- **Human clinical trials and cohorts** (DESTINY-CRC01; large molecular cohorts; real-world clinico-genomic database) (yoshino2023finalresultsof pages 1-2, lee2024rasrafmutationsand pages 1-2, strickler2023realworldtreatmentpatterns pages 1-2)
- **Preclinical models** (isogenic cell lines and murine xenografts exploring co-mutations and drug sensitivity) (singh2024rasrafcomutationand pages 2-4, singh2024rasrafcomutationand pages 14-16)

---

## 2. Etiology
### 2.1 Disease causal factors (mechanistic / genetic)
- The defining molecular feature is **ERBB2/HER2 amplification** (and/or HER2 overexpression by IHC), which identifies a distinct molecular subgroup of CRC. (singh2024rasrafcomutationand pages 2-4)
- ERBB2 amplification can co-occur with other oncogenic alterations; importantly, **~20%** of ERBB2-amplified CRCs may harbor **co-occurring oncogenic RAS/RAF alterations**, which changes HER2 clonality/heterogeneity and therapeutic responsiveness. (singh2024rasrafcomutationand pages 2-4)

### 2.2 Risk factors / protective factors
Subtype-specific lifestyle/environmental risk factors (beyond general CRC risk factors) were not identified in the retrieved evidence.

### 2.3 Gene–environment interactions
No HER2-subtype-specific gene–environment interaction evidence was identified in the retrieved sources.

---

## 3. Phenotypes (clinical presentation)
### 3.1 Clinical phenotype (subtype-specific vs general CRC)
The retrieved evidence primarily characterizes HER2-positive CRC by **molecular profile, anatomic enrichment, and treatment response**, rather than distinct presenting symptoms.

**Subtype-associated patterns supported by evidence:**
- **Primary site enrichment:** HER2 amplification is enriched in **left-sided colon and rectum** (e.g., ~95% of HER2-amplified cases in left colon/rectum in a 992-patient primary CRC cohort). (lee2024rasrafmutationsand pages 1-2)
- **Microsatellite status:** HER2-amplified CRCs are predominantly **microsatellite-stable (MSS)** (e.g., 41/41 HER2-amplified cases MSS in a 992-patient cohort). (lee2024rasrafmutationsand pages 1-2, lee2024rasrafmutationsand pages 5-6)

**General CRC phenotypes (not subtype-specific in retrieved sources):** bleeding, anemia, bowel habit change, abdominal pain, obstruction, weight loss, fatigue.

### 3.2 Suggested HPO terms (general CRC; subtype-specific symptoms not evidenced here)
- Rectal bleeding: **HP:0002093** (suggested)
- Abdominal pain: **HP:0002027** (suggested)
- Diarrhea: **HP:0002014** (suggested)
- Constipation: **HP:0002019** (suggested)
- Iron deficiency anemia: **HP:0001891** (suggested)
- Weight loss: **HP:0001824** (suggested)

(These HPO terms are offered as knowledge-base placeholders; the retrieved HER2+ CRC sources did not quantify symptom frequencies.)

---

## 4. Genetic / molecular information
### 4.1 Core causal/driver gene(s)
- **ERBB2 (HER2)** amplification and/or overexpression defines the subtype. (singh2024systematicliteraturereview pages 1-2, singh2024rasrafcomutationand pages 2-4)

### 4.2 Testing definitions of HER2 positivity in CRC (current operational criteria)
**Trial operational definition (DESTINY-CRC01):**
- HER2-positive mCRC defined as **IHC 3+ or IHC 2+/ISH+** (cohort A). (yoshino2023finalresultsof pages 1-2, yoshino2023finalresultsof pages 3-4)

**CRC-specific HERACLES diagnostic criteria (IHC/FISH):**
- HERACLES positivity includes:
  1) **IHC 3+ in ≥50%** CRC cells;
  2) **IHC 3+ in 10–50%** plus **FISH HER2/CEP17 ≥2.0** in ≥50% cells;
  3) **>50% IHC 2+** plus **FISH HER2/CEP17 ≥2.0**. (sun2023her2overexpressionamplificationstatus pages 2-4)

**Common FISH positivity thresholds used in CRC scoring studies:**
- **HER2/CEP17 ratio ≥2.0** or **average HER2 copy number ≥6.0**. (sun2023her2overexpressionamplificationstatus pages 1-2, sun2023her2overexpressionamplificationstatus pages 4-6)

**Meta-analysis definition of HER2+ CRC (integrating IHC/ISH/NGS):**
- HER2+ defined as **(1) IHC 3+**, **(2) IHC 2+ and ISH+**, or **(3) NGS positive**. (singh2024systematicliteraturereview pages 1-2)

### 4.3 Prevalence and enrichment (recent data)
A 2024 systematic review/meta-analysis restricted to FDA-approved assays estimated:
- **Overall HER2+ rate:** **4.1%** (95% CI 3.4–5.0; n=17,589). (singh2024systematicliteraturereview pages 1-2)
- **RAS WT enrichment:** **6.1%** (95% CI 5.4–6.9) in RAS WT vs **1.1%** in RAS-mutant CRC (P<0.0001). (singh2024systematicliteraturereview pages 1-2)
- **Sidedness enrichment:** pooled **5.8%** in left-sided vs **2.7%** in right-sided CRC. (singh2024systematicliteraturereview pages 4-7)
- **MSS enrichment:** MSS comprised **~98.8–100% of HER2+ cases** in small included studies; MSI-H showed low HER2 rates. (singh2024systematicliteraturereview pages 7-8)

Large cohort confirmation (primary CRC):
- **HER2 amplification prevalence:** **4.1% (41/992)**; distribution: **right 1.0%, left 5.1%, rectum 4.8%**, and **all 41 amplified were MSS**. (lee2024rasrafmutationsand pages 1-2)

### 4.4 Co-alterations / molecular landscape
**HER2-amplified primary CRC cohort (n=41 HER2-amplified of 992):**
- KRAS activating mutations: **24.4% (10/41)**; TP53 alterations: **82.9% (34/41)**; APC: **51.2% (21/41)**; PIK3CA: **17.1% (7/41)**; NRAS/BRAF: **0%** in amplified cases. (lee2024rasrafmutationsand pages 2-3)

**Large Chinese sequencing cohort (n=2454):**
- ERBB2 amplification: **3.46% (85/2454)**; ERBB2 mutations: **2.24% (55/2454)**. (liu2024genomicprofilingof pages 1-2)
- MSI-H relationship differs by alteration type: **32.7% of ERBB2-mutant** CRCs were MSI-H, while **no ERBB2-amplified** cases were MSI-H. (liu2024genomicprofilingof pages 1-2)
- Co-alteration pattern differs: ERBB2 SNV cases had higher KRAS/PIK3CA co-alterations (KRAS **45.8%**, PIK3CA **31.2%**) than ERBB2 amplification cases (KRAS **14.1%**, PIK3CA **7.7%**); TP53 co-occurred more with amplification (**92.3%**) than mutation (**58.3%**). (liu2024genomicprofilingof pages 1-2)

**RAS/RAF co-alteration as a resistance-relevant subtype:**
- In ERBB2-amplified CRC, **~20%** harbor oncogenic **RAS/RAF co-alterations**, associated with **lower-level ERBB2 amplification, increased intratumoral heterogeneity, and interlesional discordance**, with implications for reduced response to trastuzumab-based combinations. (singh2024rasrafcomutationand pages 2-4)

---

## 5. Environmental information
No HER2-subtype-specific environmental exposures, infectious triggers, or protective factors were identified in the retrieved sources.

---

## 6. Mechanism / pathophysiology
### 6.1 Upstream-to-downstream causal chain (current understanding)
1) **ERBB2 amplification** increases HER2 receptor abundance and signaling competence (driver event defining the subtype). (singh2024rasrafcomutationand pages 2-4)
2) HER2 signaling can activate downstream proliferative pathways (e.g., MAPK/PI3K signaling); in CRC this is clinically relevant because HER2 amplification is linked to **resistance to EGFR-directed therapy** even in RAS WT tumors. (singh2024rasrafcomutationand pages 2-4)
3) Therapeutic blockade using HER2-directed antibodies, TKIs, and ADCs can produce objective responses in biomarker-defined HER2-positive mCRC. (yoshino2023finalresultsof pages 1-2, mo2024resistancetoantiher2 pages 5-6)

### 6.2 Resistance mechanisms and heterogeneity (recent evidence)
A key 2024 analysis proposes that **RAS/RAF co-alterations** define a distinct ERBB2-amplified CRC subgroup characterized by:
- **Lower ERBB2 copy number**, more **intratumoral heterogeneity**, and **interlesional discordance**, and
- **Resistance to trastuzumab-based combinations** (e.g., trastuzumab/tucatinib), while retaining sensitivity to **trastuzumab deruxtecan** in preclinical and some clinical contexts. (singh2024rasrafcomutationand pages 14-16, singh2024rasrafcomutationand pages 2-4)

### 6.3 Suggested ontology terms
**GO Biological Process (suggested):**
- ERBB2 signaling: *“ERBB2 signaling pathway”* (GO term exists; exact ID not retrieved here)
- Receptor tyrosine kinase signaling: *“transmembrane receptor protein tyrosine kinase signaling pathway”*

**Cell types (CL; suggested):**
- Colonic epithelial cell / colorectal adenocarcinoma cell (CL IDs not retrieved in the evidence run)

---

## 7. Anatomical structures affected
### 7.1 Organ/tissue localization
HER2 amplification is enriched in **left colon and rectum** (primary tumor localization), suggesting preferential anatomic distribution within the large intestine. (lee2024rasrafmutationsand pages 1-2, singh2024systematicliteraturereview pages 4-7)

**Suggested UBERON terms (placeholders):**
- Colon: **UBERON:0001155**
- Rectum: **UBERON:0001052**

---

## 8. Temporal development
### 8.1 Onset and course
HER2 positivity describes a molecular subtype rather than a unique age-of-onset category. The key time-course information in retrieved sources concerns **advanced/metastatic disease** and response in later treatment lines.

### 8.2 Disease staging
HER2-directed therapy evidence is largely in **previously treated metastatic CRC**, including trials after ≥2 prior regimens. (yoshino2023finalresultsof pages 1-2)

---

## 9. Inheritance and population
### 9.1 Epidemiology (subtype frequency)
Best supported contemporary estimate (FDA-assay restricted meta-analysis):
- **HER2+ CRC prevalence ~4.1%** overall, enriched to **~6.1%** in **RAS WT** CRC. (singh2024systematicliteraturereview pages 1-2)

### 9.2 Inheritance
HER2-positive CRC is predominantly driven by **somatic alterations** (amplification and/or somatic mutation); germline inheritance patterns are not a defining feature in the retrieved sources.

---

## 10. Diagnostics
### 10.1 Tissue-based HER2 assessment
**Practical workflow reflected in evidence:**
- IHC as screening; **IHC 2+ is equivocal** and generally requires reflex ISH/FISH confirmation; FISH positivity can be defined by **HER2/CEP17 ≥2.0 and/or copy number thresholds** (e.g., ≥6). (sun2023her2overexpressionamplificationstatus pages 4-6, quaquarini2024prognosticandpredictive pages 4-5)

**Scoring system variability and harmonization challenge:**
- A CRC cohort study compared multiple IHC criteria and concluded that the **IRS-p** approach may be more sensitive/specific versus other systems when benchmarked to FISH; discordance can occur due to heterogeneity and chromosome 17 copy-number changes. (sun2023her2overexpressionamplificationstatus pages 1-2, sun2023her2overexpressionamplificationstatus pages 10-12)

### 10.2 Genomic testing
NGS may define ERBB2 copy-number amplification and co-alterations relevant for predicting response/resistance (e.g., RAS/RAF co-alterations; ERBB2 SNV vs amplification differences; PRESSING-HER2 concept referenced in evidence base). (singh2024rasrafcomutationand pages 2-4, liu2024genomicprofilingof pages 1-2)

### 10.3 Liquid biopsy and real-world testing
A large real-world dataset used **blood-based Guardant360** to identify ERBB2 amplification in mCRC and link results to treatment claims and outcomes, demonstrating real-world implementation of ctDNA-guided subtype identification. (strickler2023realworldtreatmentpatterns pages 1-2)

---

## 11. Outcome / prognosis
### 11.1 Prognosis and predictive implications
- HER2 amplification is clinically important partly because it is linked to **reduced efficacy of anti-EGFR therapies** in RAS WT mCRC, making it a negative predictive biomarker for EGFR-directed regimens. (singh2024rasrafcomutationand pages 2-4, mo2024resistancetoantiher2 pages 5-6)

### 11.2 Survival outcomes under HER2-directed therapy (refractory mCRC)
In HER2-positive cohort A of DESTINY-CRC01 (IHC3+ or IHC2+/ISH+), median outcomes were:
- **PFS 6.9 months**, **OS 15.5 months**, with objective responses confined to HER2-positive (cohort A). (yoshino2023finalresultsof pages 1-2, yoshino2023finalresultsof pages 4-6)

A survival curve and cohort response table are shown in the DESTINY-CRC01 figure/table crops retrieved (PFS/OS curves and response table). (yoshino2023finalresultsof media ab04ee1c, yoshino2023finalresultsof media 2afcc8a6)

---

## 12. Treatment
### 12.1 Approved/implemented HER2-directed strategies (late-line mCRC)
**A. Tucatinib + trastuzumab (HER2+ mCRC; trial-defined)**
- Clinical efficacy benchmarks frequently cited in 2024–2025 literature include ORR ~38% and median PFS ~8 months for trastuzumab+tucatinib, with median OS ~24 months (from trial reporting summarized in recent sources). (mo2024resistancetoantiher2 pages 5-6, singh2024rasrafcomutationand pages 2-4)

**ClinicalTrials.gov implementation metadata (MOUNTAINEER; NCT03043313):**
- Phase 2, open-label; **status COMPLETED**; **enrollment 117**; primary endpoint **confirmed ORR** by BICR RECIST 1.1; secondary endpoints include DoR/PFS/OS and safety. Dates: start **2017-06-23**, primary completion **2022-03-28**, study completion **2023-11-02**; results first posted **2023-04-18**; last update posted **2024-11-26**. URL: https://clinicaltrials.gov/study/NCT03043313 (NCT03043313 chunk 1)

**B. Trastuzumab deruxtecan (T-DXd; ADC) (DESTINY-CRC01, NCT03384940)**
- DESTINY-CRC01 (Nature Communications, **publication date June 2023**, URL https://doi.org/10.1038/s41467-023-38032-4) enrolled 86 patients into IHC/ISH-defined cohorts and showed responses confined to the HER2-positive cohort. (yoshino2023finalresultsof pages 1-2)

**Key outcomes (DESTINY-CRC01):**
- Cohort A definition: **IHC 3+ or IHC 2+/ISH+** (n=53). (yoshino2023finalresultsof pages 1-2)
- **ORR 45.3%** (24/53; 95% CI 31.6–59.6). (yoshino2023finalresultsof pages 3-4)
- **Median PFS 6.9 months**; **median OS 15.5 months**; **median DoR 7.0 months**. (yoshino2023finalresultsof pages 1-2, yoshino2023finalresultsof pages 4-6)
- **No responses** in HER2-low cohorts (IHC2+/ISH− or IHC1+). (yoshino2023finalresultsof pages 1-2)

**Safety (DESTINY-CRC01):**
- Adjudicated drug-related ILD/pneumonitis: **9.3% (8/86)** including **3 grade 5 (3.5%)**; median time to onset reported as 66.5 days (range 7–165). (yoshino2023finalresultsof pages 3-4)
- Grade ≥3 TEAEs: **65.1% overall**; drug-related grade ≥3 TEAEs **48.8%**. (yoshino2023finalresultsof pages 4-6, yoshino2023finalresultsof pages 8-9)

The ILD/pneumonitis adjudication table crop and key efficacy table/curves were retrieved as images (Table/figure crops). (yoshino2023finalresultsof media ab04ee1c, yoshino2023finalresultsof media 821b3066)

**C. Trastuzumab deruxtecan dose-finding in CRC (DESTINY-CRC02; NCT04744831)**
ClinicalTrials.gov metadata (URL: https://clinicaltrials.gov/study/NCT04744831):
- Phase 2; multicenter randomized; two dose arms **5.4 mg/kg vs 6.4 mg/kg Q3W**; population **IHC3+ or IHC2+/ISH+** advanced/metastatic CRC; enrollment **122**; primary endpoint **ORR by BICR**; secondary endpoints include PFS/OS and safety. Dates: start **2021-03-05**, primary completion **2022-11-01**, study completion **2024-12-04**; results first posted **2024-01-02**. (NCT04744831 chunk 1)

### 12.2 Real-world implementation (United States)
A GuardantINFORM (Guardant360 + claims) study (JNCCN, **Aug 2023**, URL https://doi.org/10.6004/jnccn.2023.7022) evaluated 142 patients with ERBB2-amplified mCRC and showed:
- Regimens after HER2 confirmation were heterogeneous; most common were anti-VEGF±chemo (31.0%) and HER2-directed therapy+chemo (28.9%). (strickler2023realworldtreatmentpatterns pages 3-4)
- Adoption increased over time: HER2-directed therapy used in **22.8% pre-2018** vs **36.5% post-2018**, but many patients still did not receive HER2-directed therapy. (strickler2023realworldtreatmentpatterns pages 4-6, strickler2023realworldtreatmentpatterns pages 1-2)
- Median real-world time to next treatment (rwTTNT): **8.4 months overall**, **11.0 months** for HER2-directed therapy vs **7.2 months** for non–HER2-directed therapies (descriptive). (strickler2023realworldtreatmentpatterns pages 1-2)

### 12.3 MAXO treatment ontology terms (suggested)
- Anti-HER2 targeted therapy (monoclonal antibody): **MAXO:antibody therapy** (suggested)
- Tyrosine kinase inhibitor therapy: **MAXO:small molecule therapy** (suggested)
- Antibody–drug conjugate therapy: **MAXO:antibody-drug conjugate therapy** (suggested)

---

## 13. Prevention
No HER2-subtype-specific prevention strategies were identified. Prevention and screening remain those for CRC broadly (e.g., population CRC screening), but this was not addressed in the retrieved HER2+ subtype sources.

---

## 14. Other species / natural disease
No evidence retrieved.

---

## 15. Model organisms / preclinical models
A 2024 study integrating clinical cohorts with experimental systems used:
- **Isogenic CRC cell lines** and **murine xenograft models** to show that **RAS/RAF co-alterations** in ERBB2-amplified CRC are associated with resistance to trastuzumab-based combinations (e.g., trastuzumab/tucatinib) but retained sensitivity to trastuzumab deruxtecan, and to link these effects to **copy-number level and heterogeneity**. (singh2024rasrafcomutationand pages 14-16, singh2024rasrafcomutationand pages 2-4)

---

## Key quantitative findings (curation-ready)
The following table consolidates prevalence/enrichment, co-mutations, trial outcomes, and real-world adoption:

| Domain | Finding | Quantitative detail | Notes/definition | Citations |
|---|---|---:|---|---|
| Prevalence | Overall HER2-positive CRC | 4.1% (95% CI 3.4–5.0) | Meta-analysis definition: IHC 3+ or IHC 2+/ISH+ or NGS+ | (singh2024systematicliteraturereview pages 1-2, singh2024systematicliteraturereview pages 4-7) |
| Prevalence | HER2-positive in RAS wild-type CRC | 6.1% (95% CI 5.4–6.9) | Higher than RAS-mutant CRC | (singh2024systematicliteraturereview pages 1-2, singh2024systematicliteraturereview pages 4-7) |
| Prevalence | HER2-positive in RAS-mutant CRC | 1.1% (95% CI 0.3–4.4) | Significantly lower than RAS WT | (singh2024systematicliteraturereview pages 1-2, singh2024systematicliteraturereview pages 4-7) |
| Enrichment | Left-sided vs right-sided CRC | 5.8% vs 2.7% | Left-sided enrichment in pooled analysis | (singh2024systematicliteraturereview pages 4-7) |
| Enrichment | Rectal-only HER2-positive estimate | 4.7% (95% CI 2.8–8.0) | Rectal primaries also enriched | (singh2024systematicliteraturereview pages 7-8, singh2024systematicliteraturereview pages 4-7) |
| Enrichment | MSS vs MSI-H | MSS: 98.8%–100% of HER2+ cases in small studies; MSI-H: 0%–1.2% | Strong enrichment in microsatellite-stable tumors | (singh2024systematicliteraturereview pages 7-8) |
| Cohort study | HER2 amplification in primary CRC | 4.1% (41/992) | Large primary CRC cohort | (lee2024rasrafmutationsand pages 1-2, lee2024rasrafmutationsand pages 5-6) |
| Cohort study | Site distribution of HER2 amplification | Right colon 1.0%; left colon 5.1%; rectum 4.8% | ~95% of amplified tumors in left colon + rectum | (lee2024rasrafmutationsand pages 1-2) |
| Cohort study | MSI in HER2-amplified tumors | 0% MSI-H; 100% MSS | In 41/41 HER2-amplified CRCs | (lee2024rasrafmutationsand pages 1-2, lee2024rasrafmutationsand pages 5-6, lee2024rasrafmutationsand pages 2-3) |
| Molecular co-alteration | KRAS in HER2-amplified cohort | 24.4% (10/41) | HER2-amplified primary CRC cohort | (lee2024rasrafmutationsand pages 2-3, lee2024rasrafmutationsand pages 1-2) |
| Molecular co-alteration | TP53 in HER2-amplified cohort | 82.9% (34/41) | Frequent co-alteration | (lee2024rasrafmutationsand pages 2-3, lee2024rasrafmutationsand pages 1-2) |
| Molecular co-alteration | APC in HER2-amplified cohort | 51.2% (21/41) | HER2-amplified primary CRC cohort | (lee2024rasrafmutationsand pages 2-3) |
| Molecular co-alteration | PIK3CA in HER2-amplified cohort | 17.1% (7/41) | HER2-amplified primary CRC cohort | (lee2024rasrafmutationsand pages 2-3) |
| Molecular co-alteration | NRAS/BRAF in HER2-amplified cohort | 0% NRAS; 0% BRAF | In the 41-case HER2-amplified cohort | (lee2024rasrafmutationsand pages 2-3, lee2024rasrafmutationsand pages 7-9) |
| Molecular co-alteration | RAS/RAF co-alterations among ERBB2-amplified CRC | ~20% | Associated with lower ERBB2 copy number and greater heterogeneity | (singh2024rasrafcomutationand pages 2-4) |
| Large genomic cohort | ERBB2 amplification rate | 3.46% (85/2454) | Chinese CRC cohort | (liu2024genomicprofilingof pages 1-2, liu2024genomicprofilingof pages 2-3) |
| Large genomic cohort | ERBB2 mutation rate | 2.24% (55/2454) | Chinese CRC cohort | (liu2024genomicprofilingof pages 1-2, liu2024genomicprofilingof pages 2-3) |
| Large genomic cohort | MSI-H by ERBB2 alteration type | 32.7% of ERBB2-mutant cases; 0% of ERBB2-amplified cases | Distinct biology of mutation vs amplification | (liu2024genomicprofilingof pages 1-2, liu2024genomicprofilingof pages 2-3) |
| Large genomic cohort | KRAS/PIK3CA in ERBB2 SNV vs amplification | KRAS 45.8% vs 14.1%; PIK3CA 31.2% vs 7.7% | ERBB2-mutant tumors more often co-altered with KRAS/PIK3CA than amplified tumors | (liu2024genomicprofilingof pages 1-2) |
| Large genomic cohort | TP53 in ERBB2 amplification vs mutation | 92.3% vs 58.3% | TP53 especially enriched with ERBB2 amplification | (liu2024genomicprofilingof pages 1-2) |
| Testing/diagnosis | FISH positivity threshold | HER2/CEP17 ratio ≥2.0 or average HER2 copy number ≥6.0 | Used in CRC scoring comparison study | (sun2023her2overexpressionamplificationstatus pages 1-2, sun2023her2overexpressionamplificationstatus pages 4-6) |
| Testing/diagnosis | HER2 amplification rate by FISH in 664-case cohort | 7.08% (47/664) | Large unselected Chinese CRC cohort | (sun2023her2overexpressionamplificationstatus pages 1-2, sun2023her2overexpressionamplificationstatus pages 4-6) |
| DESTINY-CRC01 definition | Cohort A | HER2-positive: IHC 3+ or IHC 2+/ISH+ (n=53) | T-DXd 6.4 mg/kg q3w | (yoshino2023finalresultsof pages 1-2, yoshino2023finalresultsof pages 3-4, siena2024her2relatedbiomarkerspredict pages 1-2) |
| DESTINY-CRC01 definition | Cohort B | IHC 2+/ISH− (n=15) | HER2-low/nonamplified comparator cohort | (yoshino2023finalresultsof pages 1-2, yoshino2023finalresultsof pages 3-4, siena2024her2relatedbiomarkerspredict pages 1-2) |
| DESTINY-CRC01 definition | Cohort C | IHC 1+ (n=18) | HER2-low comparator cohort | (yoshino2023finalresultsof pages 1-2, yoshino2023finalresultsof pages 3-4, siena2024her2relatedbiomarkerspredict pages 1-2) |
| T-DXd efficacy | ORR in Cohort A | 45.3% (24/53; 95% CI 31.6–59.6) | No responses in cohorts B or C | (yoshino2023finalresultsof pages 1-2, yoshino2023finalresultsof pages 3-4) |
| T-DXd efficacy | ORR by baseline HER2 subgroup | IHC 3+: 57.5%; IHC 2+/ISH+: 7.7% | Higher activity in IHC 3+ disease | (yoshino2023finalresultsof pages 4-6, yoshino2023finalresultsof pages 8-9) |
| T-DXd efficacy | Disease control rate | 83.0% in Cohort A | Cohort B 60.0%; Cohort C 22.2% | (yoshino2023finalresultsof pages 3-4) |
| T-DXd efficacy | Median PFS | 6.9 months | Cohort A; B 2.1 months; C 1.4 months | (yoshino2023finalresultsof pages 1-2, yoshino2023finalresultsof pages 4-6, yoshino2023finalresultsof pages 8-9) |
| T-DXd efficacy | Median OS | 15.5 months | Cohort A | (yoshino2023finalresultsof pages 1-2, yoshino2023finalresultsof pages 4-6, yoshino2023finalresultsof pages 9-10) |
| T-DXd efficacy | Median duration of response | 7.0 months | Cohort A | (yoshino2023finalresultsof pages 1-2, yoshino2023finalresultsof pages 3-4) |
| T-DXd safety | Grade ≥3 TEAEs | 65.1% overall | Drug-related grade ≥3 TEAEs 48.8% | (yoshino2023finalresultsof pages 4-6, yoshino2023finalresultsof pages 8-9) |
| T-DXd safety | Drug-related ILD/pneumonitis | 9.3% (8/86) | 4 grade 2, 1 grade 3, 3 grade 5 | (yoshino2023finalresultsof pages 1-2, yoshino2023finalresultsof pages 3-4, yoshino2023finalresultsof pages 9-10) |
| T-DXd safety | Fatal drug-related ILD | 3.5% (3/86) | Three grade 5 cases | (yoshino2023finalresultsof pages 3-4, yoshino2023finalresultsof pages 9-10) |
| T-DXd safety | Most common grade ≥3 AEs | Decreased neutrophil count; anemia | Most frequently reported grade ≥3 TEAEs | (yoshino2023finalresultsof pages 1-2) |
| Real-world practice | Cohort size | 142 HER2-amplified mCRC patients | GuardantINFORM/claims database | (strickler2023realworldtreatmentpatterns pages 3-4, strickler2023realworldtreatmentpatterns pages 1-2) |
| Real-world practice | Most common regimen before 2018 | Anti-VEGF ± chemotherapy: 31.6% (n=25) | After HER2 confirmation | (strickler2023realworldtreatmentpatterns pages 3-4, strickler2023realworldtreatmentpatterns pages 1-2) |
| Real-world practice | HER2-directed therapy use after 2018 | 36.5% (n=23) | Became most common regimen post-2018 | (strickler2023realworldtreatmentpatterns pages 3-4, strickler2023realworldtreatmentpatterns pages 1-2) |
| Real-world practice | HER2-therapy uptake over time | 22.8% pre-2018 vs 36.5% post-2018 | Increased but still underused | (strickler2023realworldtreatmentpatterns pages 4-6) |
| Real-world practice | Median rwTTNT overall | 8.4 months (95% CI 6.5–10.0) | Across entire cohort | (strickler2023realworldtreatmentpatterns pages 3-4, strickler2023realworldtreatmentpatterns pages 1-2) |
| Real-world practice | Median rwTTNT by treatment type | HER2-directed 11.0 months vs non-HER2 7.2 months | Descriptive comparison | (strickler2023realworldtreatmentpatterns pages 3-4, strickler2023realworldtreatmentpatterns pages 1-2) |
| Real-world practice | Median rwTTNT in RAS WT subgroup | HER2-directed 11.6 months vs non-HER2 8.1 months | Suggests benefit in molecularly selected patients | (strickler2023realworldtreatmentpatterns pages 3-4) |


*Table: This table summarizes the most decision-relevant quantitative findings for HER2-positive colorectal cancer across epidemiology, molecular co-alterations, trastuzumab deruxtecan trial outcomes, and real-world treatment adoption. It is designed as a compact reference for disease knowledge base curation.*

---

## Evidence-backed abstract quotes (for knowledge-base support)
- Meta-analysis definition and prevalence: “**HER2+ was defined as 1) immunohistochemistry with a score of 3+, 2) immunohistochemistry with a score of 2+ and in situ hybridization+, or 3) next-generation sequencing positive**… **Estimated HER2+ rate was 4.1%**…” (JNCI Cancer Spectrum, 2024; URL https://doi.org/10.1093/jncics/pkad082). (singh2024systematicliteraturereview pages 1-2)
- DESTINY-CRC01 trial definition and outcomes: “**cohort A (HER2-positive, immunohistochemistry [IHC] 3+ or IHC 2+/in situ hybridization [ISH]+)**” and “**reporting an ORR of 45.3% in cohort A**… **Median progression-free survival, overall survival, and duration of response were 6.9, 15.5, and 7.0 months**…” (Nature Communications, 2023; URL https://doi.org/10.1038/s41467-023-38032-4). (yoshino2023finalresultsof pages 1-2)

---

## Gaps and limitations (explicit)
- Ontology identifiers (MONDO/MeSH/ICD/Orphanet) for the molecular subtype were not recovered in the retrieved documents; the subtype is predominantly represented as a biomarker-defined subgroup rather than a standalone disease entity. (singh2024systematicliteraturereview pages 1-2)
- Subtype-specific symptom frequencies, quality-of-life metrics, and prevention/screening recommendations specific to HER2-positive CRC were not present in the retrieved HER2-focused evidence.



References

1. (singh2024systematicliteraturereview pages 1-2): Harshabad Singh, Ashley Kang, Lisa Bloudek, Ling-I Hsu, Maria Corinna Palanca-Wessels, Michael Stecher, Muriel Siadak, and Kimmie Ng. Systematic literature review and meta-analysis of her2 amplification, overexpression, and positivity in colorectal cancer. JNCI Cancer Spectrum, Oct 2024. URL: https://doi.org/10.1093/jncics/pkad082, doi:10.1093/jncics/pkad082. This article has 16 citations and is from a peer-reviewed journal.

2. (sun2023her2overexpressionamplificationstatus pages 2-4): Qi Sun, Qi Li, Fuping Gao, Hongyan Wu, Yao Fu, Jun Yang, Xiangshan Fan, Xiaobin Cui, and Xiaohong Pu. Her2 overexpression/amplification status in colorectal cancer: a comparison between immunohistochemistry and fluorescence in situ hybridization using five different immunohistochemical scoring criteria. Journal of Cancer Research and Clinical Oncology, 149:579-592, Aug 2023. URL: https://doi.org/10.1007/s00432-022-04230-8, doi:10.1007/s00432-022-04230-8. This article has 8 citations and is from a peer-reviewed journal.

3. (singh2024rasrafcomutationand pages 2-4): Harshabad Singh, Pranshu Sahgal, Kevin Kapner, Steven M. Corsello, Hersh Gupta, Rahul Gujrathi, Yvonne Y. Li, Andrew D. Cherniack, Raquelle El Alam, Joseph Kerfoot, Elizabeth Andrews, Annette Lee, Chetan Nambiar, Alison M. Hannigan, Joshua Remland, Lauren Brais, Meghan E. Leahy, Douglas A. Rubinson, Benjamin L. Schlechter, Matthew Meyerson, Yanan Kuang, Cloud P. Paweletz, Jessica K. Lee, Julia C.F. Quintanilha, Andrew J. Aguirre, Kimberly J. Perez, Brandon M. Huffman, Humberto Rossi, Thomas A. Abrams, Sheheryar Kabraji, Livio Trusolino, Andrea Bertotti, Ewa T. Sicinska, Aparna R. Parikh, Brian M. Wolpin, Alexa B. Schrock, Marios Giannakis, Kimmie Ng, Jeffrey A. Meyerhardt, Jason L. Hornick, Nilay S. Sethi, and James M. Cleary. <i>ras/raf</i> comutation and <i>erbb2</i> copy number modulates her2 heterogeneity and responsiveness to her2-directed therapy in colorectal cancer. Clinical Cancer Research, 30:1669-1684, Feb 2024. URL: https://doi.org/10.1158/1078-0432.ccr-23-2581, doi:10.1158/1078-0432.ccr-23-2581. This article has 14 citations and is from a highest quality peer-reviewed journal.

4. (strickler2023realworldtreatmentpatterns pages 1-2): John H. Strickler, Ling-I Hsu, Phoebe Wright, Michael Stecher, Muriel F. Siadak, Maria Corinna Palanca-Wessels, Junhua Yu, Nicole Zhang, Carin R. Espenschied, Kathryn Lang, and Tanios S. Bekaii-Saab. Real-world treatment patterns in patients with her2-amplified metastatic colorectal cancer: a clinical-genomic database study. Journal of the National Comprehensive Cancer Network : JNCCN, 21 8:805-812.e1, Aug 2023. URL: https://doi.org/10.6004/jnccn.2023.7022, doi:10.6004/jnccn.2023.7022. This article has 7 citations.

5. (yoshino2023finalresultsof pages 1-2): Takayuki Yoshino, Maria Di Bartolomeo, Kanwal Raghav, Toshiki Masuishi, Fotios Loupakis, Hisato Kawakami, Kensei Yamaguchi, Tomohiro Nishina, Zev Wainberg, Elena Elez, Javier Rodriguez, Marwan Fakih, Fortunato Ciardiello, Kapil Saxena, Kojiro Kobayashi, Emarjola Bako, Yasuyuki Okuda, Gerold Meinhardt, Axel Grothey, Salvatore Siena, and Maria Di Bartolomeo. Final results of destiny-crc01 investigating trastuzumab deruxtecan in patients with her2-expressing metastatic colorectal cancer. Nature Communications, Jun 2023. URL: https://doi.org/10.1038/s41467-023-38032-4, doi:10.1038/s41467-023-38032-4. This article has 152 citations and is from a highest quality peer-reviewed journal.

6. (singh2024systematicliteraturereview pages 4-7): Harshabad Singh, Ashley Kang, Lisa Bloudek, Ling-I Hsu, Maria Corinna Palanca-Wessels, Michael Stecher, Muriel Siadak, and Kimmie Ng. Systematic literature review and meta-analysis of her2 amplification, overexpression, and positivity in colorectal cancer. JNCI Cancer Spectrum, Oct 2024. URL: https://doi.org/10.1093/jncics/pkad082, doi:10.1093/jncics/pkad082. This article has 16 citations and is from a peer-reviewed journal.

7. (lee2024rasrafmutationsand pages 1-2): Sun Mi Lee and Hyunjoo Oh. Ras/raf mutations and microsatellite instability status in primary colorectal cancers according to her2 amplification. Scientific Reports, May 2024. URL: https://doi.org/10.1038/s41598-024-62096-x, doi:10.1038/s41598-024-62096-x. This article has 10 citations and is from a peer-reviewed journal.

8. (singh2024rasrafcomutationand pages 14-16): Harshabad Singh, Pranshu Sahgal, Kevin Kapner, Steven M. Corsello, Hersh Gupta, Rahul Gujrathi, Yvonne Y. Li, Andrew D. Cherniack, Raquelle El Alam, Joseph Kerfoot, Elizabeth Andrews, Annette Lee, Chetan Nambiar, Alison M. Hannigan, Joshua Remland, Lauren Brais, Meghan E. Leahy, Douglas A. Rubinson, Benjamin L. Schlechter, Matthew Meyerson, Yanan Kuang, Cloud P. Paweletz, Jessica K. Lee, Julia C.F. Quintanilha, Andrew J. Aguirre, Kimberly J. Perez, Brandon M. Huffman, Humberto Rossi, Thomas A. Abrams, Sheheryar Kabraji, Livio Trusolino, Andrea Bertotti, Ewa T. Sicinska, Aparna R. Parikh, Brian M. Wolpin, Alexa B. Schrock, Marios Giannakis, Kimmie Ng, Jeffrey A. Meyerhardt, Jason L. Hornick, Nilay S. Sethi, and James M. Cleary. <i>ras/raf</i> comutation and <i>erbb2</i> copy number modulates her2 heterogeneity and responsiveness to her2-directed therapy in colorectal cancer. Clinical Cancer Research, 30:1669-1684, Feb 2024. URL: https://doi.org/10.1158/1078-0432.ccr-23-2581, doi:10.1158/1078-0432.ccr-23-2581. This article has 14 citations and is from a highest quality peer-reviewed journal.

9. (lee2024rasrafmutationsand pages 5-6): Sun Mi Lee and Hyunjoo Oh. Ras/raf mutations and microsatellite instability status in primary colorectal cancers according to her2 amplification. Scientific Reports, May 2024. URL: https://doi.org/10.1038/s41598-024-62096-x, doi:10.1038/s41598-024-62096-x. This article has 10 citations and is from a peer-reviewed journal.

10. (yoshino2023finalresultsof pages 3-4): Takayuki Yoshino, Maria Di Bartolomeo, Kanwal Raghav, Toshiki Masuishi, Fotios Loupakis, Hisato Kawakami, Kensei Yamaguchi, Tomohiro Nishina, Zev Wainberg, Elena Elez, Javier Rodriguez, Marwan Fakih, Fortunato Ciardiello, Kapil Saxena, Kojiro Kobayashi, Emarjola Bako, Yasuyuki Okuda, Gerold Meinhardt, Axel Grothey, Salvatore Siena, and Maria Di Bartolomeo. Final results of destiny-crc01 investigating trastuzumab deruxtecan in patients with her2-expressing metastatic colorectal cancer. Nature Communications, Jun 2023. URL: https://doi.org/10.1038/s41467-023-38032-4, doi:10.1038/s41467-023-38032-4. This article has 152 citations and is from a highest quality peer-reviewed journal.

11. (sun2023her2overexpressionamplificationstatus pages 1-2): Qi Sun, Qi Li, Fuping Gao, Hongyan Wu, Yao Fu, Jun Yang, Xiangshan Fan, Xiaobin Cui, and Xiaohong Pu. Her2 overexpression/amplification status in colorectal cancer: a comparison between immunohistochemistry and fluorescence in situ hybridization using five different immunohistochemical scoring criteria. Journal of Cancer Research and Clinical Oncology, 149:579-592, Aug 2023. URL: https://doi.org/10.1007/s00432-022-04230-8, doi:10.1007/s00432-022-04230-8. This article has 8 citations and is from a peer-reviewed journal.

12. (sun2023her2overexpressionamplificationstatus pages 4-6): Qi Sun, Qi Li, Fuping Gao, Hongyan Wu, Yao Fu, Jun Yang, Xiangshan Fan, Xiaobin Cui, and Xiaohong Pu. Her2 overexpression/amplification status in colorectal cancer: a comparison between immunohistochemistry and fluorescence in situ hybridization using five different immunohistochemical scoring criteria. Journal of Cancer Research and Clinical Oncology, 149:579-592, Aug 2023. URL: https://doi.org/10.1007/s00432-022-04230-8, doi:10.1007/s00432-022-04230-8. This article has 8 citations and is from a peer-reviewed journal.

13. (singh2024systematicliteraturereview pages 7-8): Harshabad Singh, Ashley Kang, Lisa Bloudek, Ling-I Hsu, Maria Corinna Palanca-Wessels, Michael Stecher, Muriel Siadak, and Kimmie Ng. Systematic literature review and meta-analysis of her2 amplification, overexpression, and positivity in colorectal cancer. JNCI Cancer Spectrum, Oct 2024. URL: https://doi.org/10.1093/jncics/pkad082, doi:10.1093/jncics/pkad082. This article has 16 citations and is from a peer-reviewed journal.

14. (lee2024rasrafmutationsand pages 2-3): Sun Mi Lee and Hyunjoo Oh. Ras/raf mutations and microsatellite instability status in primary colorectal cancers according to her2 amplification. Scientific Reports, May 2024. URL: https://doi.org/10.1038/s41598-024-62096-x, doi:10.1038/s41598-024-62096-x. This article has 10 citations and is from a peer-reviewed journal.

15. (liu2024genomicprofilingof pages 1-2): YUZHI LIU, EVELYNE BISCHOF, ZHIQIN CHEN, JIAHUAN ZHOU, BEI ZHANG, DING ZHANG, YONG GAO, and MING QUAN. Genomic profiling of colorectal cancer in large-scale chinese patients: amplification and somatic mutations in erbb2. Oncology Research, 32:1429-1438, Aug 2024. URL: https://doi.org/10.32604/or.2024.047309, doi:10.32604/or.2024.047309. This article has 1 citations and is from a peer-reviewed journal.

16. (mo2024resistancetoantiher2 pages 5-6): Christiana Mo, Michelle Sterpi, Hyein Jeon, and Fernand Bteich. Resistance to anti-her2 therapies in gastrointestinal malignancies. Cancers, 16:2854, Aug 2024. URL: https://doi.org/10.3390/cancers16162854, doi:10.3390/cancers16162854. This article has 6 citations.

17. (quaquarini2024prognosticandpredictive pages 4-5): Erica Quaquarini, Federica Grillo, Lorenzo Gervaso, Giovanni Arpa, Nicola Fazio, Alessandro Vanoli, and Paola Parente. Prognostic and predictive roles of her2 status in non-breast and non-gastroesophageal carcinomas. Cancers, 16:3145, Sep 2024. URL: https://doi.org/10.3390/cancers16183145, doi:10.3390/cancers16183145. This article has 10 citations.

18. (sun2023her2overexpressionamplificationstatus pages 10-12): Qi Sun, Qi Li, Fuping Gao, Hongyan Wu, Yao Fu, Jun Yang, Xiangshan Fan, Xiaobin Cui, and Xiaohong Pu. Her2 overexpression/amplification status in colorectal cancer: a comparison between immunohistochemistry and fluorescence in situ hybridization using five different immunohistochemical scoring criteria. Journal of Cancer Research and Clinical Oncology, 149:579-592, Aug 2023. URL: https://doi.org/10.1007/s00432-022-04230-8, doi:10.1007/s00432-022-04230-8. This article has 8 citations and is from a peer-reviewed journal.

19. (yoshino2023finalresultsof pages 4-6): Takayuki Yoshino, Maria Di Bartolomeo, Kanwal Raghav, Toshiki Masuishi, Fotios Loupakis, Hisato Kawakami, Kensei Yamaguchi, Tomohiro Nishina, Zev Wainberg, Elena Elez, Javier Rodriguez, Marwan Fakih, Fortunato Ciardiello, Kapil Saxena, Kojiro Kobayashi, Emarjola Bako, Yasuyuki Okuda, Gerold Meinhardt, Axel Grothey, Salvatore Siena, and Maria Di Bartolomeo. Final results of destiny-crc01 investigating trastuzumab deruxtecan in patients with her2-expressing metastatic colorectal cancer. Nature Communications, Jun 2023. URL: https://doi.org/10.1038/s41467-023-38032-4, doi:10.1038/s41467-023-38032-4. This article has 152 citations and is from a highest quality peer-reviewed journal.

20. (yoshino2023finalresultsof media ab04ee1c): Takayuki Yoshino, Maria Di Bartolomeo, Kanwal Raghav, Toshiki Masuishi, Fotios Loupakis, Hisato Kawakami, Kensei Yamaguchi, Tomohiro Nishina, Zev Wainberg, Elena Elez, Javier Rodriguez, Marwan Fakih, Fortunato Ciardiello, Kapil Saxena, Kojiro Kobayashi, Emarjola Bako, Yasuyuki Okuda, Gerold Meinhardt, Axel Grothey, Salvatore Siena, and Maria Di Bartolomeo. Final results of destiny-crc01 investigating trastuzumab deruxtecan in patients with her2-expressing metastatic colorectal cancer. Nature Communications, Jun 2023. URL: https://doi.org/10.1038/s41467-023-38032-4, doi:10.1038/s41467-023-38032-4. This article has 152 citations and is from a highest quality peer-reviewed journal.

21. (yoshino2023finalresultsof media 2afcc8a6): Takayuki Yoshino, Maria Di Bartolomeo, Kanwal Raghav, Toshiki Masuishi, Fotios Loupakis, Hisato Kawakami, Kensei Yamaguchi, Tomohiro Nishina, Zev Wainberg, Elena Elez, Javier Rodriguez, Marwan Fakih, Fortunato Ciardiello, Kapil Saxena, Kojiro Kobayashi, Emarjola Bako, Yasuyuki Okuda, Gerold Meinhardt, Axel Grothey, Salvatore Siena, and Maria Di Bartolomeo. Final results of destiny-crc01 investigating trastuzumab deruxtecan in patients with her2-expressing metastatic colorectal cancer. Nature Communications, Jun 2023. URL: https://doi.org/10.1038/s41467-023-38032-4, doi:10.1038/s41467-023-38032-4. This article has 152 citations and is from a highest quality peer-reviewed journal.

22. (NCT03043313 chunk 1):  Tucatinib Plus Trastuzumab in Patients With HER2+ Colorectal Cancer. Seagen Inc.. 2017. ClinicalTrials.gov Identifier: NCT03043313

23. (yoshino2023finalresultsof pages 8-9): Takayuki Yoshino, Maria Di Bartolomeo, Kanwal Raghav, Toshiki Masuishi, Fotios Loupakis, Hisato Kawakami, Kensei Yamaguchi, Tomohiro Nishina, Zev Wainberg, Elena Elez, Javier Rodriguez, Marwan Fakih, Fortunato Ciardiello, Kapil Saxena, Kojiro Kobayashi, Emarjola Bako, Yasuyuki Okuda, Gerold Meinhardt, Axel Grothey, Salvatore Siena, and Maria Di Bartolomeo. Final results of destiny-crc01 investigating trastuzumab deruxtecan in patients with her2-expressing metastatic colorectal cancer. Nature Communications, Jun 2023. URL: https://doi.org/10.1038/s41467-023-38032-4, doi:10.1038/s41467-023-38032-4. This article has 152 citations and is from a highest quality peer-reviewed journal.

24. (yoshino2023finalresultsof media 821b3066): Takayuki Yoshino, Maria Di Bartolomeo, Kanwal Raghav, Toshiki Masuishi, Fotios Loupakis, Hisato Kawakami, Kensei Yamaguchi, Tomohiro Nishina, Zev Wainberg, Elena Elez, Javier Rodriguez, Marwan Fakih, Fortunato Ciardiello, Kapil Saxena, Kojiro Kobayashi, Emarjola Bako, Yasuyuki Okuda, Gerold Meinhardt, Axel Grothey, Salvatore Siena, and Maria Di Bartolomeo. Final results of destiny-crc01 investigating trastuzumab deruxtecan in patients with her2-expressing metastatic colorectal cancer. Nature Communications, Jun 2023. URL: https://doi.org/10.1038/s41467-023-38032-4, doi:10.1038/s41467-023-38032-4. This article has 152 citations and is from a highest quality peer-reviewed journal.

25. (NCT04744831 chunk 1):  Trastuzumab Deruxtecan in Participants With HER2-overexpressing Advanced or Metastatic Colorectal Cancer. Daiichi Sankyo. 2021. ClinicalTrials.gov Identifier: NCT04744831

26. (strickler2023realworldtreatmentpatterns pages 3-4): John H. Strickler, Ling-I Hsu, Phoebe Wright, Michael Stecher, Muriel F. Siadak, Maria Corinna Palanca-Wessels, Junhua Yu, Nicole Zhang, Carin R. Espenschied, Kathryn Lang, and Tanios S. Bekaii-Saab. Real-world treatment patterns in patients with her2-amplified metastatic colorectal cancer: a clinical-genomic database study. Journal of the National Comprehensive Cancer Network : JNCCN, 21 8:805-812.e1, Aug 2023. URL: https://doi.org/10.6004/jnccn.2023.7022, doi:10.6004/jnccn.2023.7022. This article has 7 citations.

27. (strickler2023realworldtreatmentpatterns pages 4-6): John H. Strickler, Ling-I Hsu, Phoebe Wright, Michael Stecher, Muriel F. Siadak, Maria Corinna Palanca-Wessels, Junhua Yu, Nicole Zhang, Carin R. Espenschied, Kathryn Lang, and Tanios S. Bekaii-Saab. Real-world treatment patterns in patients with her2-amplified metastatic colorectal cancer: a clinical-genomic database study. Journal of the National Comprehensive Cancer Network : JNCCN, 21 8:805-812.e1, Aug 2023. URL: https://doi.org/10.6004/jnccn.2023.7022, doi:10.6004/jnccn.2023.7022. This article has 7 citations.

28. (lee2024rasrafmutationsand pages 7-9): Sun Mi Lee and Hyunjoo Oh. Ras/raf mutations and microsatellite instability status in primary colorectal cancers according to her2 amplification. Scientific Reports, May 2024. URL: https://doi.org/10.1038/s41598-024-62096-x, doi:10.1038/s41598-024-62096-x. This article has 10 citations and is from a peer-reviewed journal.

29. (liu2024genomicprofilingof pages 2-3): YUZHI LIU, EVELYNE BISCHOF, ZHIQIN CHEN, JIAHUAN ZHOU, BEI ZHANG, DING ZHANG, YONG GAO, and MING QUAN. Genomic profiling of colorectal cancer in large-scale chinese patients: amplification and somatic mutations in erbb2. Oncology Research, 32:1429-1438, Aug 2024. URL: https://doi.org/10.32604/or.2024.047309, doi:10.32604/or.2024.047309. This article has 1 citations and is from a peer-reviewed journal.

30. (siena2024her2relatedbiomarkerspredict pages 1-2): Salvatore Siena, Kanwal Raghav, Toshiki Masuishi, Kensei Yamaguchi, Tomohiro Nishina, Elena Elez, Javier Rodriguez, Ian Chau, Maria Di Bartolomeo, Hisato Kawakami, Fumitaka Suto, Makito Koga, Koichiro Inaki, Yusuke Kuwahara, Issey Takehara, Daniel Barrios, Kojiro Kobayashi, Axel Grothey, and Takayuki Yoshino. Her2-related biomarkers predict clinical outcomes with trastuzumab deruxtecan treatment in patients with her2-expressing metastatic colorectal cancer: biomarker analyses of destiny-crc01. Nature Communications, Nov 2024. URL: https://doi.org/10.1038/s41467-024-53223-3, doi:10.1038/s41467-024-53223-3. This article has 27 citations and is from a highest quality peer-reviewed journal.

31. (yoshino2023finalresultsof pages 9-10): Takayuki Yoshino, Maria Di Bartolomeo, Kanwal Raghav, Toshiki Masuishi, Fotios Loupakis, Hisato Kawakami, Kensei Yamaguchi, Tomohiro Nishina, Zev Wainberg, Elena Elez, Javier Rodriguez, Marwan Fakih, Fortunato Ciardiello, Kapil Saxena, Kojiro Kobayashi, Emarjola Bako, Yasuyuki Okuda, Gerold Meinhardt, Axel Grothey, Salvatore Siena, and Maria Di Bartolomeo. Final results of destiny-crc01 investigating trastuzumab deruxtecan in patients with her2-expressing metastatic colorectal cancer. Nature Communications, Jun 2023. URL: https://doi.org/10.1038/s41467-023-38032-4, doi:10.1038/s41467-023-38032-4. This article has 152 citations and is from a highest quality peer-reviewed journal.
