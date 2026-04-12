---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-05T14:02:08.751406'
end_time: '2026-04-05T14:07:25.487255'
duration_seconds: 316.74
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Clear Cell Sarcoma
  mondo_id: ''
  category: ''
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
- **Disease Name:** Clear Cell Sarcoma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Clear Cell Sarcoma** covering all of the
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
- **Disease Name:** Clear Cell Sarcoma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Clear Cell Sarcoma** covering all of the
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


## Clear Cell Sarcoma (CCS) — Comprehensive Disease Characteristics Research Report

### Target Disease
- **Disease Name:** Clear cell sarcoma (of soft tissue; “clear cell sarcoma of tendons and aponeuroses”)
- **MONDO ID:** Not retrieved in the available evidence in this run (would require querying MONDO/OLS/Orphanet directly).
- **Category:** Rare malignant soft-tissue sarcoma with melanocytic differentiation; fusion-driven sarcoma. (thway2012tumorswithewsr1creb1 pages 3-5, gonzaga2018theepidemiologyand pages 1-2, ozenberger2023ewsr1atf1orchestratesthe pages 1-2)

---

## 1. Disease Information

### 1.1 Concise overview (current understanding)
Clear cell sarcoma (CCS) is a rare, aggressive malignant soft-tissue sarcoma that typically arises in deep soft tissues associated with tendons/aponeuroses and most often occurs in the extremities (notably lower extremity/foot–ankle region). It shows melanocytic differentiation and is a major diagnostic mimic of malignant melanoma. (cazzato2025clearcellsarcoma pages 1-2, thway2012tumorswithewsr1creb1 pages 3-5, gonzaga2018theepidemiologyand pages 1-2, ozenberger2023ewsr1atf1orchestratesthe pages 1-2)

**Direct abstract quote (molecularly defining feature):** “Clear cell sarcoma (CCS)… is characterized by the expression of the oncogenic driver fusion gene **EWSR1::ATF1**.” (Mae et al., 2023, *Cancer Research Communications*, published Jul 2023, https://doi.org/10.1158/2767-9764.crc-22-0518) (mae2023targetingtheclear pages 1-2)

### 1.2 Key identifiers
The following identifiers were not captured in the retrieved excerpts, so cannot be reliably asserted here:
- **OMIM / Orphanet / ICD-10 / ICD-11 / MONDO**: not available in current evidence.
- **MeSH**: ClinicalTrials.gov condition browse lists **MeSH term “Sarcoma, Clear Cell” (MeSH ID D018227)** for this condition. (NCT05963035 chunk 1)

### 1.3 Synonyms / alternative names
- Clear cell sarcoma of soft tissue (CCS) (cazzato2025clearcellsarcoma pages 1-2)
- Clear cell sarcoma of tendons and aponeuroses (grothues2024prognosticfactorsin pages 1-2)
- “Malignant melanoma of soft parts” / “soft tissue melanoma” (historical) (mae2023targetingtheclear pages 1-2, gonzaga2018theepidemiologyand pages 1-2)

### 1.4 Evidence source type
Most disease-level definitions and management statements in this report derive from aggregated resources (reviews), registry/cohort analyses, and clinical trial registry entries rather than single-patient EHR-derived sources. (cazzato2025clearcellsarcoma pages 1-2, gonzaga2018theepidemiologyand pages 1-2, ozenberger2023ewsr1atf1orchestratesthe pages 1-2, NCT05963035 chunk 1)

---

## 2. Etiology

### 2.1 Disease causal factors (genetic/mechanistic)
CCS is primarily a **fusion-driven sarcoma**, most commonly defined by **EWSR1::ATF1** (EWSR1 fused to ATF1), usually arising from **t(12;22)(q13;q12)**; rarer variants include EWSR1::CREB1 or EWSR1::CREM. (mae2023targetingtheclear pages 1-2, ozenberger2023ewsr1atf1orchestratesthe pages 1-2)

**Direct abstract quote (fusion defines and drives disease):** “It is defined and driven by expression of… translocation-generated fusion oncogenes, the most common of which is **EWSR1::ATF1**.” (Ozenberger et al., 2023, *Cancers*, published Dec 2023, https://doi.org/10.3390/cancers15245750) (ozenberger2023ewsr1atf1orchestratesthe pages 1-2)

**Frequency of hallmark fusion:** One 2023 genomic/functional review states: “Nearly **90%** of CCS harbor an **EWSR1-ATF1** translocation-mediated fusion gene, although **EWSR1-CREB1** is also observed.” (Rasmussen et al., 2023, *British Journal of Cancer*, published Mar 2023, https://doi.org/10.1038/s41416-023-02222-0) (rasmussen2023functionalgenomicsof pages 1-2)

### 2.2 Risk factors
No robust environmental/behavioral risk factors were identified in the retrieved evidence. Available evidence emphasizes oncogenic fusion as the major causal event. (rasmussen2023functionalgenomicsof pages 1-2, ozenberger2023ewsr1atf1orchestratesthe pages 1-2)

### 2.3 Protective factors / gene–environment interaction
No protective factors or gene–environment interactions were identified in the retrieved evidence. (rasmussen2023functionalgenomicsof pages 1-2)

---

## 3. Phenotypes

### 3.1 Core clinical phenotype spectrum
Common presentations include a deep soft-tissue mass in an extremity and association with tendons/aponeuroses. Pain may be present (one review describes “a painful, rapidly growing mass” in typical locations). (bianco2024ewsr1atf1translocationa pages 12-13, gonzaga2018theepidemiologyand pages 1-2)

**Typical sites / demographics (examples):**
- CCS “arises in muscle compartments, tendons, or aponeuroses, most frequently in the extremities.” (Ozenberger et al., 2023) (ozenberger2023ewsr1atf1orchestratesthe pages 1-2)
- In an NCDB cohort, **lower limb/hip** was the most frequent primary site (**53%**). (Gonzaga et al., 2018, https://doi.org/10.1007/s00432-018-2693-6) (gonzaga2018theepidemiologyand pages 1-2)

### 3.2 Suggested HPO terms (non-exhaustive; based on clinical descriptions)
Because the retrieved evidence is not structured as HPO annotations, the following are suggested mappings from described clinical manifestations:
- **Soft tissue mass** → *Soft tissue neoplasm* (candidate HPO mapping; specific HPO ID not available in evidence)
- **Painful mass** → *Pain* (candidate)
- **Local recurrence / metastasis** → *Neoplasm metastasis* (candidate)

**Note:** Exact HPO IDs require ontology lookup not performed in this run.

### 3.3 Quality-of-life impact
Formal QoL instruments (e.g., EQ-5D/SF-36) were not reported in the retrieved CCS-specific papers; however, QoL is included as an outcome in at least one CCS immunotherapy trial protocol (EORTC QLQ-C30 and EQ-5D). (NCT04274023 chunk 1)

---

## 4. Genetic / Molecular Information

### 4.1 Causal genes / chromosomal abnormalities
- **EWSR1::ATF1** fusion (EWSR1 and ATF1 genes) from **t(12;22)(q13;q12)** is the central hallmark for CCS. (mae2023targetingtheclear pages 1-2, ozenberger2023ewsr1atf1orchestratesthe pages 1-2)
- Rarer: **EWSR1::CREB1** and **EWSR1::CREM**. (ozenberger2023ewsr1atf1orchestratesthe pages 1-2)

### 4.2 Pathogenic variant class
The dominant pathogenic event is a **structural rearrangement** generating an oncogenic **fusion transcription factor** (chimeric transcriptional regulator). (mae2023targetingtheclear pages 1-2, ozenberger2023ewsr1atf1orchestratesthe pages 1-2)

### 4.3 Functional consequences / downstream programs
Mechanistically, evidence supports that EWSR1::ATF1 reprograms transcription and is sufficient to initiate sarcomagenesis in model systems. (ozenberger2023ewsr1atf1orchestratesthe pages 1-2)

**Direct abstract quote (transcriptional reprogramming):** “The EWSR1::ATF1 fusion oncoprotein **reprograms transcription**.” (Ozenberger et al., 2023) (ozenberger2023ewsr1atf1orchestratesthe pages 1-2)

### 4.4 Additional recurrent genomic features (from functional genomics)
A 2023 functional genomics study reports frequent copy gains involving MITF and MYC loci in human CCS samples (e.g., MYC gain in 62% and MITF gain in 55% of a set of tumors described in the excerpt). (rasmussen2023functionalgenomicsof pages 1-2)

---

## 5. Environmental Information
No specific environmental/lifestyle/infectious contributors were identified in the retrieved evidence. CCS is primarily discussed as a fusion-oncogene-driven malignancy. (rasmussen2023functionalgenomicsof pages 1-2, ozenberger2023ewsr1atf1orchestratesthe pages 1-2)

---

## 6. Mechanism / Pathophysiology

### 6.1 High-level causal chain (fusion → transcriptional/epigenetic rewiring → phenotype)
1. **Chromosomal translocation** generates **EWSR1::ATF1** fusion. (mae2023targetingtheclear pages 1-2, ozenberger2023ewsr1atf1orchestratesthe pages 1-2)
2. Fusion functions as an aberrant transcriptional regulator that **reprograms transcription** and sustains tumor state. (ozenberger2023ewsr1atf1orchestratesthe pages 1-2)
3. Tumor develops melanocytic differentiation (shared IHC markers with melanoma) and demonstrates aggressive behavior with local recurrence and metastasis risk. (thway2012tumorswithewsr1creb1 pages 3-5, gonzaga2018theepidemiologyand pages 1-2)

### 6.2 Epigenetic/transcriptional dependencies and therapeutic implications (recent)
A 2023 study used high-throughput screening and found that **HDAC inhibition** can suppress the fusion program.

**Direct abstract quote (screening and lead drug):** “we performed a high-throughput drug screening, finding that the histone deacetylase inhibitor **vorinostat** exerted an antiproliferation effect with the reduced expression of **EWSR1::ATF1**.” (Mae et al., 2023, https://doi.org/10.1158/2767-9764.crc-22-0518) (mae2023targetingtheclear pages 1-2)

### 6.3 Suggested GO / CL terms (conceptual; require ontology lookup)
Based on the evidence that CCS is fusion-transcription-factor driven and involves melanocytic differentiation markers:
- **GO Biological Process (candidate):** regulation of transcription, chromatin organization, melanocyte differentiation
- **CL (candidate):** neural crest-derived cell lineages (proposed by epigenetic/3D regulation studies; not fully extracted here)

---

## 7. Anatomical Structures Affected

### 7.1 Organ/tissue level
- Predominantly **deep soft tissue** of **extremities**; commonly near **tendons and aponeuroses**. (cazzato2025clearcellsarcoma pages 1-2, thway2012tumorswithewsr1creb1 pages 3-5, gonzaga2018theepidemiologyand pages 1-2, ozenberger2023ewsr1atf1orchestratesthe pages 1-2)

### 7.2 Suggested UBERON terms (conceptual)
- Extremity soft tissue; tendon; aponeurosis (exact UBERON IDs not retrieved).

---

## 8. Temporal Development

### 8.1 Onset
Typically affects adolescents/young adults but can occur across a broad range. Reported mean age 22 (range 2–83) in one 2023 review; median age 39 in NCDB (1973–2014 cohort analysis); median age 42 in a 2024 single-center cohort. (rasmussen2023functionalgenomicsof pages 1-2, gonzaga2018theepidemiologyand pages 1-2, grothues2024prognosticfactorsin pages 1-2)

### 8.2 Progression
Evidence emphasizes frequent **local recurrence** and **late metastasis**, with poor long-term survival in many cohorts. (rasmussen2023functionalgenomicsof pages 1-2, gonzaga2018theepidemiologyand pages 1-2, grothues2024prognosticfactorsin pages 1-2)

---

## 9. Inheritance and Population

### 9.1 Epidemiology (key quantitative data)
CCS is very rare. One paper states it is “less than one percent of soft-tissue sarcomas” and reports “fewer than 100 cases… annually in the United States.” (Ozenberger et al., 2023) (ozenberger2023ewsr1atf1orchestratesthe pages 1-2)

A SEER-based analysis reported population-adjusted incidence range **0.012/100,000 to 0.027/100,000** (2000–2019). (gonzaga2018theepidemiologyand pages 1-2)

### 9.2 Demographics
NCDB review: median age 39, sexes approximately equal, and race distribution 78% Caucasian and 15% Black. (gonzaga2018theepidemiologyand pages 1-2)

### 9.3 Inheritance
CCS is not presented as an inherited Mendelian disorder in the retrieved evidence; it is driven by a somatic fusion. Germline predisposition was not identified here. (ozenberger2023ewsr1atf1orchestratesthe pages 1-2)

---

## 10. Diagnostics

### 10.1 Pathology and immunohistochemistry
CCS is a melanoma mimic; classic IHC profile overlaps melanoma.

From a high-citation pathology review: “most CCSs show diffuse **S100 protein, HMB45, MelanA and MiTF expression** and are immunohistochemically indistinguishable from melanoma.” (Thway & Fisher, 2012, *Am J Surg Pathol*, https://doi.org/10.1097/pas.0b013e31825485c5) (thway2012tumorswithewsr1creb1 pages 3-5)

### 10.2 Molecular diagnostics
Molecular confirmation is emphasized for distinguishing CCS from melanoma:

**Direct abstract quote:** “the use of fluorescence in situ hybridization (FISH) or reverse transcription polymerase chain reaction (RT-PCR) is essential for diagnosis and distinguishing CCS from primary and/or metastatic melanoma.” (Gonzaga et al., 2018, https://doi.org/10.1007/s00432-018-2693-6) (gonzaga2018theepidemiologyand pages 1-2)

### 10.3 Differential diagnosis
Primary differential is malignant melanoma due to shared morphology and melanocytic markers; molecular demonstration of EWSR1 fusion is key. (cazzato2025clearcellsarcoma pages 1-2, thway2012tumorswithewsr1creb1 pages 3-5, gonzaga2018theepidemiologyand pages 1-2)

### 10.4 Emerging/adjunct markers and tools
Recent narrative review emphasizes PRAME as an adjunct marker in differential diagnosis with melanoma, while noting PRAME positivity is relatively rare in CCS. (cazzato2025clearcellsarcoma pages 1-2, cazzato2025clearcellsarcoma pages 8-10)

### 10.5 Imaging and staging innovations (real-world implementation)
A prospective diagnostic study is evaluating melanin-targeted PET imaging.

- **NCT05963035** (posted 2023-07-27; start 2023-06-21): prospective study of **18F-PFPN PET/MR** versus **18F-FDG** for diagnosis and staging in CCS of soft tissue (planned n=10). (ClinicalTrials.gov record) (NCT05963035 chunk 1)

---

## 11. Outcomes / Prognosis

### 11.1 Survival statistics
Multiple sources converge on poor long-term outcomes.

- A widely repeated summary: **5-year ~50%**, **10-year ~38%** overall survival. (mae2023targetingtheclear pages 1-2, bianco2024ewsr1atf1translocationa pages 12-13, gonzaga2018theepidemiologyand pages 1-2, ozenberger2023ewsr1atf1orchestratesthe pages 1-2)
- A 2024 single-center cohort (43 CCS/GINET patients) reported: “median follow-up of 35mo and a **5y-OS-rate of 42%**.” (Grothues et al., 2024, https://doi.org/10.1007/s00432-024-05980-3) (grothues2024prognosticfactorsin pages 1-2)

### 11.2 Metastasis and lymphatic spread (quantitative)
- 2024 cohort: “**18.6%** of patients showed lymphatic spread and **20.9%** distant metastases.” (Grothues et al., 2024) (grothues2024prognosticfactorsin pages 1-2)
- NCDB review summarizes that lymph node metastases are unusually frequent for STS (estimated 12–43% across prior literature) and reports 15% distant organ metastases in the cohort (lung most common 4%). (gonzaga2018theepidemiologyand pages 1-2)

### 11.3 Prognostic factors (recent quantitative evidence)
- Initial metastatic disease is strongly adverse: “Presence of initial M+ was associated with a dismal survival of **1.4 years (M+) vs 7.1 years (M0; p < .001)**.” (Grothues et al., 2024) (grothues2024prognosticfactorsin pages 1-2)
- Completeness of surgery matters in localized disease: “Final R0 status correlated significantly… with longer survival… (N0M0, **5-yr OS 0% vs 64%** [R+ vs R0]).” (Grothues et al., 2024) (grothues2024prognosticfactorsin pages 1-2)

---

## 12. Treatment

### 12.1 Current standard of care / real-world implementation
Across reviews and cohort analyses, **surgery with negative margins** is the main curative-intent treatment for localized CCS. (cazzato2025clearcellsarcoma pages 1-2, gonzaga2018theepidemiologyand pages 1-2, grothues2024prognosticfactorsin pages 1-2)

- NCDB treatment patterns: surgery 83%, radiation 34%, chemotherapy 20%. (gonzaga2018theepidemiologyand pages 1-2)

### 12.2 Radiotherapy and chemotherapy
Conventional radiotherapy and chemotherapy are often described as having **limited benefit**.

- “Traditional chemo- and radiotherapies have minimal benefit in CCS.” (Bianco et al., 2024, https://doi.org/10.3390/ijms252413693) (bianco2024ewsr1atf1translocationa pages 12-13)
- 2024 cohort: “Radiation and systemic treatment had limited antitumor effects…” (Grothues et al., 2024) (grothues2024prognosticfactorsin pages 1-2)

### 12.3 Investigational and emerging strategies (2023–2024 emphasis)
Epigenetic/transcriptional targeting is supported by preclinical evidence:
- HDAC inhibitor **vorinostat** suppressing EWSR1::ATF1 and inhibiting proliferation in CCS models. (mae2023targetingtheclear pages 1-2)

Targeted therapy and immunotherapy are being explored due to lack of effective systemic options in metastatic disease. (cazzato2025clearcellsarcoma pages 8-10, grothues2024prognosticfactorsin pages 1-2)

### 12.4 Clinical trials (selected, with real-world status)
- **NCT04593758** (posted 2020-10-20; completion 2023-03-09): devimistat (CPI-613) + hydroxychloroquine for relapsed/refractory CCS; phase I/II; n=16; completed. (NCT04593758 chunk 1)
- **NCT04274023** (posted 2020-02-18; status updated 2024-02-01): anti-PD-1 TSR-042 in advanced CCS; phase II; terminated due to enrollment difficulty; n=3. (NCT04274023 chunk 1)
- **NCT03132155** (results posted 2024-05-24): AMG 337 for advanced/metastatic CCS with EWSR1-ATF1 fusion; phase II; “terminated due to lack of therapeutic effect”; n=8. (NCT03132155 chunk 1)
- **NCT04458922** (results first posted 2023-10-23): atezolizumab phase II study in CCS/chondrosarcoma; includes tumor microenvironment correlatives (CD8 and PD-1/PD-L1); active not recruiting; n=27 total. (NCT04458922 chunk 1)

**MAXO term suggestions (conceptual):**
- Surgical excision; radiotherapy; systemic chemotherapy; immune checkpoint inhibitor therapy; targeted therapy (MET inhibition); PET imaging (diagnostic). (Trial and review evidence supports these intervention classes) (cazzato2025clearcellsarcoma pages 8-10, NCT05963035 chunk 1, NCT04274023 chunk 1, NCT04458922 chunk 1)

---

## 13. Prevention
No established primary prevention strategies were identified in the retrieved evidence; CCS is rare and primarily defined by a somatic fusion event. Secondary prevention is effectively early detection and expert referral for accurate diagnosis and complete surgical management. (gonzaga2018theepidemiologyand pages 1-2, grothues2024prognosticfactorsin pages 1-2)

---

## 14. Other Species / Natural Disease
No comparative veterinary/natural disease evidence was retrieved in this run.

---

## 15. Model Organisms
Evidence in this run supports the existence of mouse genetic models and preclinical approaches centered on EWSR1::ATF1-driven tumor programs (including studies describing initiation of sarcomagenesis and transcriptome recapitulation). (ozenberger2023ewsr1atf1orchestratesthe pages 1-2)

---

## Structured summary table (for knowledge base ingestion)
The following table consolidates key facts (definition, epidemiology, diagnostics, prognosis, therapies, and NCT trials) into a single scaffold.

| Domain | Item | Key details | Source/year | Citation |
|---|---|---|---|---|
| Definition / synonyms / hallmark fusion | Disease overview | Rare, aggressive soft-tissue sarcoma with melanocytic differentiation; classically arises in tendons/aponeuroses or deep soft tissue of extremities; historically confused with melanoma/“melanoma of soft parts.” | Reviews and cohort summaries, 2018-2025 | (cazzato2025clearcellsarcoma pages 1-2, thway2012tumorswithewsr1creb1 pages 3-5, mae2023targetingtheclear pages 1-2, gonzaga2018theepidemiologyand pages 1-2, ozenberger2023ewsr1atf1orchestratesthe pages 1-2) |
| Definition / synonyms / hallmark fusion | Common synonyms | Clear cell sarcoma of soft tissue; clear-cell sarcoma of tendons and aponeuroses; malignant melanoma of soft parts / soft tissue melanoma (historical). | 2018, 2022, 2025 | (mae2023targetingtheclear pages 1-2, gonzaga2018theepidemiologyand pages 1-2) |
| Definition / synonyms / hallmark fusion | Hallmark molecular event | Definitional/pathognomonic fusion is usually **EWSR1::ATF1** from **t(12;22)(q13;q12)**; **EWSR1::CREB1** is a rarer alternative; **EWSR1::CREM** reported rarely. | 2023-2025 | (cazzato2025clearcellsarcoma pages 1-2, rasmussen2023functionalgenomicsof pages 1-2, mae2023targetingtheclear pages 1-2, ozenberger2023ewsr1atf1orchestratesthe pages 1-2) |
| Epidemiology / clinical stats | Rarity | Accounts for **<1% of soft-tissue sarcomas**; **fewer than 100 cases/year in the US** reported in one review/modeling paper. | 2023 | (ozenberger2023ewsr1atf1orchestratesthe pages 1-2) |
| Epidemiology / clinical stats | Incidence | SEER 2000-2019: population-adjusted incidence ranged **0.012-0.027 per 100,000**; annual percent change **0.561%**. | Wang 2025 | (gonzaga2018theepidemiologyand pages 1-2) |
| Epidemiology / clinical stats | Age distribution | Mean age reported as **22 years (range 2-83)** in one genomic review; NCDB median age **39 years**; another 2024 cohort median age **42 years**. | 2018, 2023, 2024 | (rasmussen2023functionalgenomicsof pages 1-2, gonzaga2018theepidemiologyand pages 1-2) |
| Epidemiology / clinical stats | Sex / race | NCDB review: males and females approximately equally affected; race distribution **78% Caucasian, 15% Black**. | Gonzaga 2018 | (gonzaga2018theepidemiologyand pages 1-2) |
| Epidemiology / clinical stats | Primary location | Lower limb/hip **53%** in NCDB; distant extremities affected in **72.5%** in a 2024 cohort; commonly foot/ankle/shin, tendons and aponeuroses. | 2018, 2024, 2024 review | (thway2012tumorswithewsr1creb1 pages 3-5, gonzaga2018theepidemiologyand pages 1-2, ozenberger2023ewsr1atf1orchestratesthe pages 1-2) |
| Epidemiology / clinical stats | Metastasis at diagnosis | Up to **30%** may present with metastasis at diagnosis (review); NCDB reported **15%** with distant organ metastases, lung most common (**4%**); 2024 cohort reported **20.9%** distant metastases at presentation. | 2018, 2023, 2024 | (rasmussen2023functionalgenomicsof pages 1-2, gonzaga2018theepidemiologyand pages 1-2) |
| Epidemiology / clinical stats | Lymph node spread | Lymph node metastases estimated **12-43%** in prior literature summarized by NCDB review; another study cited **16.8%** LNM for clear cell sarcoma among STS of head/neck/extremities; 2024 cohort reported **18.6%** lymphatic spread. | 2018, 2022, 2024 | (gonzaga2018theepidemiologyand pages 1-2) |
| Epidemiology / clinical stats | Survival | Frequently cited OS rates: **5-year ~50% and 10-year ~38%**; broader review range **5-year 47-67%, 10-year 33%, 20-year 10%**; SEER 2000-2019 survival **1-year 78.4%, 3-year 62.0%, 5-year 57.1%**. | 2023, 2025 | (rasmussen2023functionalgenomicsof pages 1-2, mae2023targetingtheclear pages 1-2, bianco2024ewsr1atf1translocationa pages 12-13, gonzaga2018theepidemiologyand pages 1-2, ozenberger2023ewsr1atf1orchestratesthe pages 1-2) |
| Epidemiology / clinical stats | Prognostic factors | Worse outcomes associated with metastases, larger tumors (>4 cm in SEER), trunk location, and non-R0 resection; in localized CCS, 5-year OS **0% vs 64%** for R+ vs R0 in one 2024 cohort. | 2018, 2024, 2025 | (gonzaga2018theepidemiologyand pages 1-2) |
| Diagnostics | Histopathology | Lobular/nested/organoid growth of spindle-to-epithelioid cells with clear to amphophilic cytoplasm; melanin may be present; often low mitotic activity. | 2012, 2025 | (cazzato2025clearcellsarcoma pages 1-2, thway2012tumorswithewsr1creb1 pages 3-5) |
| Diagnostics | Core IHC markers | Commonly positive: **S100**, **HMB45**, **MelanA**, **MiTF**; tyrosinase also noted in fusion-associated melanocytic program. These markers make CCS immunophenotypically similar to melanoma. | 2012, 2024 | (thway2012tumorswithewsr1creb1 pages 3-5, bianco2024ewsr1atf1translocationa pages 12-13) |
| Diagnostics | Emerging / adjunct IHC | **PRAME** may help in differential diagnosis versus melanoma, but expression in CCS is relatively rare / imperfectly specific. | 2023-2025 | (cazzato2025clearcellsarcoma pages 1-2, cazzato2025clearcellsarcoma pages 8-10) |
| Diagnostics | Molecular confirmation | Diagnosis commonly requires **FISH**, **RT-PCR**, or RNA-based molecular methods to identify **EWSR1** rearrangement/fusion and distinguish CCS from melanoma. | 2018, trial protocols | (gonzaga2018theepidemiologyand pages 1-2, NCT03132155 chunk 1) |
| Diagnostics | Differential diagnosis | Main differential is **malignant melanoma** due to overlapping melanocytic morphology/IHC; molecular demonstration of **EWSR1::ATF1** or related fusion is key discriminator. | 2018-2025 | (cazzato2025clearcellsarcoma pages 1-2, thway2012tumorswithewsr1creb1 pages 3-5, cazzato2025clearcellsarcoma pages 8-10, gonzaga2018theepidemiologyand pages 1-2) |
| Standard treatment | Localized disease | **Wide/radical surgical excision with negative margins** is the treatment cornerstone; expert multidisciplinary management recommended. | 2018-2025 | (cazzato2025clearcellsarcoma pages 1-2, mae2023targetingtheclear pages 1-2, cazzato2025clearcellsarcoma pages 8-10, gonzaga2018theepidemiologyand pages 1-2) |
| Standard treatment | Radiotherapy | Used selectively/adjuvantly, especially when recurrence risk is high or margins are inadequate; antitumor effect often limited in CCS-specific cohorts. | 2012, 2024, 2025 | (thway2012tumorswithewsr1creb1 pages 3-5, cazzato2025clearcellsarcoma pages 8-10, gonzaga2018theepidemiologyand pages 1-2) |
| Standard treatment | Chemotherapy | Conventional / classical chemotherapy has **limited efficacy** and CCS is often described as chemo-resistant. | 2022-2025 | (cazzato2025clearcellsarcoma pages 1-2, mae2023targetingtheclear pages 1-2, bianco2024ewsr1atf1translocationa pages 12-13, cazzato2025clearcellsarcoma pages 8-10) |
| Standard treatment | Nodal staging consideration | Sentinel lymph node biopsy may aid staging because of propensity for lymphatic spread; radical lymphadenectomy considered if nodal metastases present. | 2024 review | (cazzato2025clearcellsarcoma pages 8-10) |
| Investigational therapy / trials | Epigenetic targeting | Preclinical 2023 work identified **vorinostat** (HDAC inhibitor) suppressing **EWSR1::ATF1**; **JQ1**/BRD4 inhibition also reduced fusion expression, with synergy in combination. | Mae 2023 | (mae2023targetingtheclear pages 1-2) |
| Investigational therapy / trials | Targeted therapy rationale | CCS biology linked in some reports to **MET/c-MET** activation; investigational approaches include MET inhibitors and TKIs. | 2022-2025 | (mae2023targetingtheclear pages 1-2, cazzato2025clearcellsarcoma pages 8-10) |
| Investigational therapy / trials | Cabozantinib + immunotherapy | Case report: metastatic CCS achieved initial partial response and was progression-free for **2 years** on cabozantinib plus tumor vaccine/nivolumab-based strategy. | Muskatel 2022 | (mae2023targetingtheclear pages 1-2) |
| Investigational therapy / trials | Devimistat + hydroxychloroquine | **NCT04593758**; phase I/II; relapsed/refractory CCS; completed; enrolled **16**; assessed MTD, toxicity, and ORR. | ClinicalTrials.gov, updated 2023 | (NCT04593758 chunk 1) |
| Investigational therapy / trials | Anti-PD-1 TSR-042 | **NCT04274023**; phase II single-arm in advanced/metastatic CCS; terminated for enrollment difficulty; enrolled **3**. | ClinicalTrials.gov, updated 2024 | (NCT04274023 chunk 1) |
| Investigational therapy / trials | Tebentafusp | **NCT06942442**; recruiting phase II in **HLA-A*02:01-positive** unresectable/metastatic CCS; planned enrollment **47**. | ClinicalTrials.gov, posted 2025 | (NCT06942442 chunk 1) |
| Investigational therapy / trials | AMG 337 (MET inhibitor) | **NCT03132155**; phase II in advanced/metastatic CCS with **EWSR1-ATF1** fusion; terminated due to **lack of therapeutic effect**; enrolled **8**. | ClinicalTrials.gov, results posted 2024 | (NCT03132155 chunk 1) |
| Investigational therapy / trials | Atezolizumab | **NCT04458922**; phase II NCI study of anti-PD-L1 antibody in CCS/chondrosarcoma; active, not recruiting; enrolled **27** total; includes correlative CD8/PD-1/PD-L1 analyses. | ClinicalTrials.gov, results first posted 2023 | (NCT04458922 chunk 1) |
| Investigational therapy / trials | Vebreltinib | **NCT07153887**; recruiting exploratory phase II for locally advanced/metastatic CCS; MET abnormality testing built into protocol; planned enrollment **30**. | ClinicalTrials.gov, posted 2025 | (NCT07153887 chunk 1) |
| Investigational therapy / trials | Melanin-targeted imaging | **NCT05963035**; diagnostic interventional study of **18F-PFPN PET** for diagnosis/staging versus 18F-FDG; planned enrollment **10**. | ClinicalTrials.gov, posted 2023 | (NCT05963035 chunk 1) |


*Table: This table compiles the core disease-definition, epidemiology, diagnostics, and treatment/trial information for clear cell sarcoma using only the retrieved evidence snippets and clinical trial records. It is useful as a compact knowledge-base scaffold with direct context-ID citations for traceability.*


References

1. (thway2012tumorswithewsr1creb1 pages 3-5): Khin Thway and Cyril Fisher. Tumors with ewsr1-creb1 and ewsr1-atf1 fusions: the current status. The American Journal of Surgical Pathology, 36:e1–e11, Jul 2012. URL: https://doi.org/10.1097/pas.0b013e31825485c5, doi:10.1097/pas.0b013e31825485c5. This article has 267 citations.

2. (gonzaga2018theepidemiologyand pages 1-2): M. Isabel Gonzaga, Leah Grant, Christina Curtin, Jonathan Gootee, Peter Silberstein, and Elida Voth. The epidemiology and survivorship of clear cell sarcoma: a national cancer database (ncdb) review. Journal of Cancer Research and Clinical Oncology, 144:1711-1716, Jun 2018. URL: https://doi.org/10.1007/s00432-018-2693-6, doi:10.1007/s00432-018-2693-6. This article has 72 citations and is from a peer-reviewed journal.

3. (ozenberger2023ewsr1atf1orchestratesthe pages 1-2): Benjamin B. Ozenberger, Li Li, Emily R. Wilson, Alexander J. Lazar, Jared J. Barrott, and Kevin B. Jones. Ewsr1::atf1 orchestrates the clear cell sarcoma transcriptome in human tumors and a mouse genetic model. Cancers, 15:5750, Dec 2023. URL: https://doi.org/10.3390/cancers15245750, doi:10.3390/cancers15245750. This article has 14 citations.

4. (cazzato2025clearcellsarcoma pages 1-2): Gerardo Cazzato, Francesco Piscazzi, Alessandra Filosa, Anna Colagrande, Paolo Del Fiore, Francesca Ambrogio, Chiara Battilotti, Andrea Danese, Serena Federico, and Fortunato Cassalia. Clear cell sarcoma (ccs) of the soft tissue: an update narrative review with emphasis on the utility of prame in differential diagnosis. Journal of Clinical Medicine, 14:1233, Feb 2025. URL: https://doi.org/10.3390/jcm14041233, doi:10.3390/jcm14041233. This article has 8 citations.

5. (mae2023targetingtheclear pages 1-2): Hirokazu Mae, Hidetatsu Outani, Yoshinori Imura, Ryota Chijimatsu, Akitomo Inoue, Yuki Kotani, Naohiro Yasuda, Sho Nakai, Takaaki Nakai, Satoshi Takenaka, and Seiji Okada. Targeting the clear cell sarcoma oncogenic driver fusion gene <i>ewsr1::atf1</i> by hdac inhibition. Cancer Research Communications, 3:1152-1165, Jul 2023. URL: https://doi.org/10.1158/2767-9764.crc-22-0518, doi:10.1158/2767-9764.crc-22-0518. This article has 15 citations and is from a peer-reviewed journal.

6. (NCT05963035 chunk 1):  Clinical Application of 18F-PFPN PET Imaging in Diagnosis and Staging of Clear Cell Sarcoma of Soft Tissue. Union Hospital, Tongji Medical College, Huazhong University of Science and Technology. 2023. ClinicalTrials.gov Identifier: NCT05963035

7. (grothues2024prognosticfactorsin pages 1-2): Janik Grothues, Jendrik Hardes, Abbas Agaimy, Stephane Collaud, Lars Podleska, Farhad Farzalyev, Nina Myline Engel, Rainer Hamacher, Benjamin Fletcher, Christoph Pöttgen, Stefanie Bertram, Hans-Ulrich Schildhaus, Arne Streitbürger, Sebastian Bauer, and Johanna Falkenhorst. Prognostic factors in clear cell sarcoma: an analysis of soft tissue sarcoma in 43 cases. Journal of Cancer Research and Clinical Oncology, Nov 2024. URL: https://doi.org/10.1007/s00432-024-05980-3, doi:10.1007/s00432-024-05980-3. This article has 6 citations and is from a peer-reviewed journal.

8. (rasmussen2023functionalgenomicsof pages 1-2): Samuel V. Rasmussen, Agnieszka Wozniak, Melvin Lathara, Joshua M. Goldenberg, Benjamin M. Samudio, Lissett R. Bickford, Kiyo Nagamori, Hollis Wright, Andrew D. Woods, Shefali Chauhan, Che-Jui Lee, Erin R. Rudzinski, Michael K. Swift, Tadashi Kondo, David E. Fisher, Evgeny Imyanitov, Isidro Machado, Antonio Llombart-Bosch, Irene L. Andrulis, Nalan Gokgoz, Jay Wunder, Hiroshi Mirotaki, Takuro Nakamura, Ganapati Srinivasa, Khin Thway, Robin L. Jones, Paul H. Huang, Noah E. Berlow, Patrick Schöffski, and Charles Keller. Functional genomics of human clear cell sarcoma: genomic, transcriptomic and chemical biology landscape for clear cell sarcoma. British Journal of Cancer, 128:1941-1954, Mar 2023. URL: https://doi.org/10.1038/s41416-023-02222-0, doi:10.1038/s41416-023-02222-0. This article has 4 citations and is from a domain leading peer-reviewed journal.

9. (bianco2024ewsr1atf1translocationa pages 12-13): Julia Raffaella Bianco, YiJing Li, Agota Petranyi, and Zsolt Fabian. Ewsr1::atf1 translocation: a common tumor driver of distinct human neoplasms. International Journal of Molecular Sciences, 25:13693, Dec 2024. URL: https://doi.org/10.3390/ijms252413693, doi:10.3390/ijms252413693. This article has 1 citations.

10. (NCT04274023 chunk 1):  Study on TSR-042 in Advanced Clear Cell Sarcoma. Italian Sarcoma Group. 2024. ClinicalTrials.gov Identifier: NCT04274023

11. (cazzato2025clearcellsarcoma pages 8-10): Gerardo Cazzato, Francesco Piscazzi, Alessandra Filosa, Anna Colagrande, Paolo Del Fiore, Francesca Ambrogio, Chiara Battilotti, Andrea Danese, Serena Federico, and Fortunato Cassalia. Clear cell sarcoma (ccs) of the soft tissue: an update narrative review with emphasis on the utility of prame in differential diagnosis. Journal of Clinical Medicine, 14:1233, Feb 2025. URL: https://doi.org/10.3390/jcm14041233, doi:10.3390/jcm14041233. This article has 8 citations.

12. (NCT04593758 chunk 1):  To Evaluate Maximally Tolerated Dose (MTD), Safety and Efficacy of CPI-613® (Devimistat) Plus Hydroxychloroquine in Patients With Relapsed or Refractory Clear Cell Sarcoma of Soft Tissue. Cornerstone Pharmaceuticals. 2021. ClinicalTrials.gov Identifier: NCT04593758

13. (NCT03132155 chunk 1):  QUILT-3.031: AMG 337 in Subjects With Advanced or Metastatic Clear Cell Sarcoma. NantPharma, LLC. 2018. ClinicalTrials.gov Identifier: NCT03132155

14. (NCT04458922 chunk 1):  Testing Atezolizumab in People 2-17 Years Old With Clear Cell Sarcoma or Advanced Chondrosarcoma. National Cancer Institute (NCI). 2020. ClinicalTrials.gov Identifier: NCT04458922

15. (NCT06942442 chunk 1):  A Phase II Trial of Tebentafusp in HLA-A*02:01 Positive Patients With Advanced Clear Cell Sarcoma. Sarcoma Alliance for Research through Collaboration. 2025. ClinicalTrials.gov Identifier: NCT06942442

16. (NCT07153887 chunk 1):  Vebreltinib for Advanced or Metastatic CCS. Second Affiliated Hospital, School of Medicine, Zhejiang University. 2025. ClinicalTrials.gov Identifier: NCT07153887
