---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-05T17:22:44.366714'
end_time: '2026-04-05T17:32:17.633874'
duration_seconds: 573.27
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: IDH-Mutant Cholangiocarcinoma
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 40
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** IDH-Mutant Cholangiocarcinoma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **IDH-Mutant Cholangiocarcinoma** covering all of the
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
- **Disease Name:** IDH-Mutant Cholangiocarcinoma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **IDH-Mutant Cholangiocarcinoma** covering all of the
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


# Comprehensive Research Report: IDH‑Mutant Cholangiocarcinoma (focus: intrahepatic cholangiocarcinoma, iCCA)

## Target Disease
- **Disease name:** IDH‑mutant cholangiocarcinoma (clinically, predominantly **IDH1‑mutant intrahepatic cholangiocarcinoma**) (casak2022fdaapprovalsummary pages 1-2, makawita2024comprehensiveimmunogenomicprofiling pages 1-2)
- **Category:** Malignant neoplasm of bile ducts / biliary tract cancer; molecular subtype defined by **IDH1/IDH2 hotspot mutation** (makawita2024comprehensiveimmunogenomicprofiling pages 1-2, vaquero2024decipheringtheroleb pages 29-32)
- **Ontology identifiers (retrieved in current evidence):**
  - Open Targets disease entity for **cholangiocarcinoma**: **EFO_0005221** (Open Targets evidence capture; not a PMID source in current corpus)
  - Open Targets disease entity for **intrahepatic cholangiocarcinoma**: **EFO_1001961** (Open Targets evidence capture)
  - Related MONDO entity returned by Open Targets: **MONDO_0018531** (“carcinoma of liver and intrahepatic biliary tract”) (Open Targets evidence capture)
- **Identifiers not retrieved in the available corpus:** a MONDO term explicitly named “IDH‑mutant cholangiocarcinoma”, and disease cross‑references (ICD‑10/ICD‑11, MeSH, Orphanet, OMIM) were **not** captured by the current tool evidence and therefore cannot be asserted here.

## Executive definition (current understanding)
**IDH‑mutant cholangiocarcinoma** is a subset of cholangiocarcinoma—most commonly **intrahepatic cholangiocarcinoma (iCCA)**—harboring hotspot mutations in **IDH1** (classically at **R132**, especially R132C) and less commonly **IDH2** (hotspots **R172** and **R140**) (makawita2024comprehensiveimmunogenomicprofiling pages 1-2, casak2022fdaapprovalsummary pages 1-2, vaquero2024decipheringtheroleb pages 29-32). Mutant IDH enzymes acquire **neomorphic** activity that converts **α‑ketoglutarate (α‑KG)** to the oncometabolite **D‑2‑hydroxyglutarate (2‑HG)**, leading to widespread epigenetic dysregulation and downstream tumorigenic and immune‑microenvironment effects (fan2024pharmacokineticspharmacodynamicsofivosidenib pages 1-2, vaquero2024decipheringtheroleb pages 29-32).

## 1. Disease Information
### Overview and classification
Cholangiocarcinoma (CCA) is a biliary tract cancer classified anatomically into **intrahepatic, perihilar, and distal** tumors. One recent review summarizes typical fractions as: intrahepatic **10–20%**, perihilar **50–60%**, distal **20–30%** (Oct 2023) (frampton2023ivosidenibareview pages 1-2). IDH mutations are enriched in iCCA relative to extrahepatic CCA (lavacchi2022ivosidenibinidh1mutated pages 2-3, vaquero2024decipheringtheroleb pages 29-32).

### Synonyms / alternative names (used in clinical research)
- “**IDH1‑mutated cholangiocarcinoma**” / “**IDH1‑mutant cholangiocarcinoma**” (casak2022fdaapprovalsummary pages 1-2)
- “**mIDH1 cholangiocarcinoma**” (mutant‑IDH1 cholangiocarcinoma) (fan2024pharmacokineticspharmacodynamicsofivosidenib pages 1-2, frampton2023ivosidenibareview pages 1-2)
- “**IDH1/2‑altered iCCA**” (makawita2024comprehensiveimmunogenomicprofiling pages 1-2)

### Evidence source types represented in this report
- **Aggregated disease‑level resources / large cohorts:** CGP cohort (n=3,067 iCCA) (makawita2024comprehensiveimmunogenomicprofiling pages 1-2)
- **Randomized phase III trial and regulatory summary:** ClarIDHy / FDA approval summary (casak2022fdaapprovalsummary pages 1-2, casak2022fdaapprovalsummary media 6fe1eb4a, casak2022fdaapprovalsummary media 2f70fd07)
- **Real‑world clinical practice cohort:** Italian experience (n=11) (muller2024sustainedclinicalresponse pages 1-2)
- **Mechanistic preclinical studies / models:** organoids/PDX/cell lines; GEMMs (luk2024srcinhibitionenables pages 1-2, vaquero2024decipheringtherole pages 25-29)
- **High‑risk population disease context (PSC‑CCA):** surveillance and risk estimates (catanzaro2023primarysclerosingcholangitisassociated pages 1-2, catanzaro2023primarysclerosingcholangitisassociated pages 9-11)

## 2. Etiology
### Molecular etiology (defining causal factor for the subtype)
- **Primary causal molecular factor:** somatic hotspot mutation in **IDH1** (R132 substitutions; most commonly R132C) and/or **IDH2** (R172, R140) (makawita2024comprehensiveimmunogenomicprofiling pages 1-2, casak2022fdaapprovalsummary pages 1-2).
- **Mechanistic hallmark:** mutant IDH converts α‑KG to **2‑HG**, which accumulates and disrupts α‑KG–dependent enzymes, including DNA/histone demethylases; this creates a hypermethylated state and altered differentiation programs (vaquero2024decipheringtheroleb pages 29-32).

### Clinical risk factors (general CCA / iCCA; subtype-specific data limited)
Direct epidemiologic risk-factor data **specific to IDH-mutant** iCCA were not identified in the available primary evidence. However, several strong risk factors for cholangiocarcinoma in general, and for specific etiologic subtypes, are well supported in the retrieved corpus:

1) **Primary sclerosing cholangitis (PSC)** (high-risk context for CCA overall)
- PSC confers a very large increase in CCA risk; one 2023 review reports **“400–600‑fold increased risk”** versus the general population and an **annual risk 0.5–1.5%** (Oct 2023) (catanzaro2023primarysclerosingcholangitisassociated pages 1-2).
- Reported PSC‑CCA lifetime prevalence in that review ranges **6–13%**, with a substantial fraction (**≈30–50%**) diagnosed within **the first year** after PSC diagnosis (catanzaro2023primarysclerosingcholangitisassociated pages 1-2, catanzaro2023primarysclerosingcholangitisassociated pages 2-4).

2) **Liver fluke infection** (etiologic driver for endemic fluke‑related CCA; largely perihilar/extrahepatic patterns in many settings; IDH-mutant enrichment in non-fluke iCCA is suggested in a review)
- A 2024 high‑risk community screening in Lao PDR (Opisthorchis viverrini endemic) reported a **prevalence of suspected CCA of 7.2%** among 3,400 participants and association with **O. viverrini infection (aOR 3.4, 95% CI 1.7–6.5)** (Nov 2024) (homsana2024; retrieved earlier but not in cite list—no context id available for citation in this run; therefore not asserted here).
- In the retrieved corpus, liver fluke infection is repeatedly described as a major cause in endemic regions (qualitative, not subtype-specific) (ciobica2024theconstellationof pages 2-3, catanzaro2023primarysclerosingcholangitisassociated pages 2-4).

3) **Chronic viral hepatitis and chronic liver disease**
- iCCA risk factors include chronic hepatitis B/C in a 2024 Liver Cancer review (Oct 2024) (nishida2024geneticepigeneticalterationand pages 1-2).

### Protective factors
Subtype‑specific protective genetic or environmental factors were **not identified** in the retrieved primary evidence.

### Gene–environment interactions
Direct evidence for gene–environment interactions specifically shaping **IDH‑mutant** cholangiocarcinoma was **not found** in the retrieved primary sources.

## 3. Phenotypes (clinical presentation; HPO mapping)
The retrieved sources emphasize that cholangiocarcinoma is often detected late and may be clinically silent early:
- iCCA is “**typically asymptomatic early and often diagnosed at an advanced stage**” (Oct 2024) (nishida2024geneticepigeneticalterationand pages 1-2).

However, **specific symptom frequencies** (e.g., jaundice, pruritus, RUQ pain, weight loss) and **phenotype prevalence statistics** for IDH‑mutant iCCA were **not present** in the retrieved evidence base used for this report.

### Practical phenotype/HPO suggestions (generic for cholangiocarcinoma; requires confirmation in dedicated clinical sources)
Because phenotype evidence was not captured by the current corpus, the following should be treated as **ontology placeholders** requiring confirmation from dedicated clinical phenotype literature:
- **Obstructive jaundice** (HPO: *Jaundice* HP:0000952)
- **Pruritus** (HP:0000989)
- **Abdominal pain** (HP:0002027)
- **Weight loss** (HP:0001824)
- **Elevated bilirubin / cholestasis labs** (e.g., *Hyperbilirubinemia* HP:0002904)

## 4. Genetic / Molecular Information
### Causal genes and mutation spectrum
- **Causal genes (somatic drivers for this molecular subtype):**
  - **IDH1** (isocitrate dehydrogenase (NADP(+)) 1)
  - **IDH2** (isocitrate dehydrogenase (NADP(+)) 2)

- **Large cohort frequencies (advanced iCCA):** in 3,067 iCCA cases, **IDH1 alterations 14%** and **IDH2 alterations 4%** (Mar 2024) (makawita2024comprehensiveimmunogenomicprofiling pages 1-2).
- **Variant spectrum (same cohort):**
  - **IDH1:** R132C **69%**; R132L/G/S/H/F **16%/7%/4%/3%/<1%** (makawita2024comprehensiveimmunogenomicprofiling pages 1-2).
  - **IDH2:** R172 **94.4%**; R140 **6.6%** (makawita2024comprehensiveimmunogenomicprofiling pages 1-2).

- **ClarIDHy trial baseline mutation distribution (IDH1‑mutant CCA):** R132C was predominant (68–74% depending on arm), with other R132 substitutions present (Mar 2022) (casak2022fdaapprovalsummary pages 1-2).

| Cohort / source | Disease cohort / setting | Sample size | % IDH1 | % IDH2 | Predominant variant(s) and proportions | Key associated features |
|---|---|---:|---:|---:|---|---|
| Makawita et al., *JCO Precision Oncology* 2024 | Advanced intrahepatic cholangiocarcinoma (comprehensive genomic profiling cohort) | 3,067 iCCA cases | 14% (426/3,067) | 4% (125/3,067) | **IDH1:** R132C 69%; R132L/G/S/H/F 16%/7%/4%/3%/<1%. **IDH2:** R172 94.4%; R140 6.6% (makawita2024comprehensiveimmunogenomicprofiling pages 1-2) | IDH1/2-altered tumors were described as **“immunologically cold”**; compared with IDH-wildtype iCCA they had lower MSI-High, lower TMB ≥10 mut/Mb, and lower PD-L1 positivity; co-mutation patterns differed from IDH-wildtype; no significant mOS difference in retrospective analysis (makawita2024comprehensiveimmunogenomicprofiling pages 1-2) |
| Casak et al., *Clinical Cancer Research* 2022 FDA approval summary (ClarIDHy baseline population) | Previously treated advanced unresectable/metastatic IDH1-mutant cholangiocarcinoma, predominantly intrahepatic | 185 total (124 ivosidenib; 61 placebo) | 100% by trial eligibility | Not reported / not eligible | **IDH1 arm distributions:** R132C 68% and 74% (ivosidenib/placebo), R132G 14% and 10%, R132L 17% and 11%, R132H 0% and 3%, R132S 2% and 2% (casak2022fdaapprovalsummary pages 1-2) | Population was predominantly intrahepatic (90–95%), metastatic (92–93%), with female predominance (~61–65%); this source is a treatment-registration cohort and does **not** report IDH2 frequency, immunogenomic phenotype, or co-mutation landscape (casak2022fdaapprovalsummary pages 1-2) |
| Lavacchi et al., *Pharmacology & Therapeutics* 2022 (review summarizing phase I and disease biology) | IDH1-mutant cholangiocarcinoma, mainly intrahepatic; includes phase I ivosidenib cohort and background epidemiology | Phase I cohort: 73 pretreated patients (89% intrahepatic) | ~10–20% of iCCA; <1% of extrahepatic CCA | Hotspots noted at IDH2 R140/R172, but cohort-level % IDH2 not given | In phase I background cohort, **R132C 77%** and **R132L 11%** were the most frequent IDH1 variants; hotspot codons emphasized: IDH1 R132, IDH2 R140/R172 (lavacchi2022ivosidenibinidh1mutated pages 2-3) | IDH mutations drive 2-HG accumulation and epigenetic dysregulation; reported baseline/acquired co-alterations included **PBRM1, ARID1A, PIK3CA, KRAS**; resistance mutations included **IDH2-R172V** and **IDH1-R132F** at progression (lavacchi2022ivosidenibinidh1mutated pages 2-3) |


*Table: This table compares key published sources on IDH1/IDH2 alterations in cholangiocarcinoma, emphasizing intrahepatic cholangiocarcinoma. It highlights mutation frequencies, dominant hotspot variants, and clinically relevant associated features such as immune phenotype and co-alteration patterns.*

### Somatic vs germline
All evidence in this report treats IDH1/2 alterations as **tumor genomic alterations** (somatic) in cholangiocarcinoma; germline causal IDH1/2 variants were not discussed in retrieved sources (makawita2024comprehensiveimmunogenomicprofiling pages 1-2, casak2022fdaapprovalsummary pages 1-2).

### Functional consequences and oncometabolite biology
A key mechanistic chain supported by multiple sources:
1) **Mutant IDH1** (cytosolic) converts α‑KG → **2‑HG** (fan2024pharmacokineticspharmacodynamicsofivosidenib pages 1-2, vaquero2024decipheringtheroleb pages 29-32).
2) 2‑HG accumulation inhibits α‑KG–dependent enzymes (including DNA/histone demethylases), producing **hypermethylation** and altered differentiation programs (vaquero2024decipheringtheroleb pages 29-32).
3) Immune consequences: IDH1/2 mutations are linked to hypermethylation and downregulation of antigen processing/presentation machinery and are enriched in **non‑inflamed (“cold”)** iCCA microenvironments (nishida2024geneticepigeneticalterationand pages 1-2, makawita2024comprehensiveimmunogenomicprofiling pages 1-2).

**Direct abstract quote (PK/PD mechanistic biomarker):** Fan et al. measured that in ivosidenib‑treated patients, “**mean plasma 2‑HG concentration was reduced from 1108 ng/mL at baseline to 97.7 ng/mL at C2D1… An average 2‑HG inhibition of 75.0% was observed at steady state**” (Jan 2024) (fan2024pharmacokineticspharmacodynamicsofivosidenib pages 1-2).

### Co-mutations / molecular context
- In a real‑world cohort of 11 IDH1‑mutant CCA treated with ivosidenib, common co‑alterations included **TP53, BAP1, CDKN2A, CDKN2B** (Jan 2023) (muller2024sustainedclinicalresponse pages 1-2).
- In the 2024 CGP cohort study, patterns of comutations differed between IDH1/2+ and IDH‑wildtype iCCA, though detailed lists were not fully captured in the excerpt (makawita2024comprehensiveimmunogenomicprofiling pages 1-2).

### Immunogenomic phenotype (2024 large-cohort evidence)
Compared with IDH‑wildtype iCCA, IDH1/2‑altered iCCA showed lower frequency of multiple immune biomarkers:
- **MSI‑High** lower (P=0.009)
- **TMB ≥10 mut/Mb** lower (P<0.0001)
- **PD‑L1 positivity** lower
and the authors conclude: “**IDH1-/2-mutated tumors appear immunologically cold**” (Mar 2024) (makawita2024comprehensiveimmunogenomicprofiling pages 1-2).

### Ontology suggestions (molecular processes and cell types)
**GO Biological Process (suggested):**
- DNA methylation / epigenetic regulation (supported by hypermethylation phenotype) (vaquero2024decipheringtheroleb pages 29-32)
- Antigen processing and presentation (downregulated/hypermethylated in IDH-mutant iCCA) (nishida2024geneticepigeneticalterationand pages 1-2)
- Translation / ribosomal signaling and S6 phosphorylation (IDHm dependency discussed below) (luk2024srcinhibitionenables pages 1-2)

**Cell Ontology (CL) candidates (supported by TME-class studies):**
- Macrophage populations enriched in certain IDH-enriched TME classes (“M2-like” macrophage enrichment) (martinserrano2023novelmicroenvironmentbasedclassification pages 1-3)

## 5. Environmental Information
Evidence captured here is largely for **general CCA etiologies**, not specifically IDH-mutant tumors.
- **Infectious agent exposure:** liver flukes as etiologic factors for CCA in endemic regions (qualitative) (ciobica2024theconstellationof pages 2-3, catanzaro2023primarysclerosingcholangitisassociated pages 2-4).
- **Autoimmune/inflammatory biliary disease:** PSC as a strong risk condition (catanzaro2023primarysclerosingcholangitisassociated pages 1-2).

## 6. Mechanism / Pathophysiology
### Causal chain (from mutation to phenotype)
A current integrated causal chain for IDH‑mutant iCCA supported by retrieved evidence:
1) **Somatic IDH1/2 hotspot mutation** →
2) **2‑HG accumulation** →
3) **Epigenetic reprogramming / hypermethylation** (TET/Jmj inhibition) and downstream differentiation programs (vaquero2024decipheringtheroleb pages 29-32) →
4) **Immune-cold tumor microenvironment** through hypermethylation/downregulation of antigen presentation machinery (nishida2024geneticepigeneticalterationand pages 1-2) →
5) Clinically relevant therapeutic vulnerability to **mutant IDH1 inhibition** (2‑HG suppression) and additional pathway dependencies (SRC/S6K) (fan2024pharmacokineticspharmacodynamicsofivosidenib pages 1-2, luk2024srcinhibitionenables pages 1-2).

### Immune microenvironment classification (iCCA)
A large transcriptomic meta‑analysis (~900 iCCAs) introduced a **TME-based “STIM” classification** with both inflamed and non‑inflamed classes (May 2023) (martinserrano2023novelmicroenvironmentbasedclassification pages 1-3). Of particular relevance:
- A non‑inflamed “**hepatic stem‑like**” class (~35%) is enriched in **IDH1/2 mutations** and **BAP1**, and includes enrichment of “M2‑like macrophages” (martinserrano2023novelmicroenvironmentbasedclassification pages 1-3).

### Mechanistic dependency discovered in 2024 (SRC → MAGI1‑PP2A → S6K/S6)
A 2024 Science Translational Medicine study reported an actionable dependency in IDH‑mutant iCCA:
- “**Mutant IDH (IDHm) ICC is dependent on SRC kinase for growth and survival and is hypersensitive to inhibition by dasatinib**” (May 2024) (luk2024srcinhibitionenables pages 1-2).
- Mechanism: SRC suppresses a tumor‑suppressive **MAGI1–PP2A** complex; SRC inhibition enables PP2A-mediated dephosphorylation of S6K, decreasing protein synthesis and promoting cell death; resistance correlates with increased pS6; combination of **dasatinib + M2698** showed enhanced inhibition in cell lines, organoids, and PDX (luk2024srcinhibitionenables pages 1-2).

### Ontology suggestions (GO/CL/UBERON)
- **UBERON (anatomy):** intrahepatic bile duct / liver intrahepatic biliary tree (not explicitly provided in the retrieved corpus; recommended as the primary affected site based on iCCA focus).
- **GO Cellular Component (suggested):** mitochondrion / cytosol (IDH isoform localization is relevant: IDH1 cytosolic; IDH2 mitochondrial) (vaquero2024decipheringtheroleb pages 29-32).

## 7. Anatomical Structures Affected
- Primary site for this molecular subtype in clinical datasets and trials is overwhelmingly **intrahepatic cholangiocarcinoma** (e.g., ClarIDHy population was 90–95% intrahepatic) (casak2022fdaapprovalsummary pages 1-2).

## 8. Temporal Development
- iCCA is frequently diagnosed at an advanced stage due to asymptomatic early course (nishida2024geneticepigeneticalterationand pages 1-2).
- In PSC high-risk populations, a large fraction of PSC‑CCA is diagnosed early after PSC diagnosis: **≈30–50% within the first year** (catanzaro2023primarysclerosingcholangitisassociated pages 1-2, catanzaro2023primarysclerosingcholangitisassociated pages 2-4).

## 9. Inheritance and Population
### Epidemiology (general CCA/iCCA; not IDH-specific incidence)
- Age-standardized incidence cited in one 2023 therapeutic review: **0.3–3.5 per 100,000** in EU/USA/Australasia (Oct 2023) (frampton2023ivosidenibareview pages 1-2).
- Another report (case-based) states incidence “approximately **6 per 100,000**” and rising (Jul 2024) (muller2024sustainedclinicalresponse pages 1-2).

### Proportion of iCCA with IDH mutations
- iCCA tumor frequency of IDH1/2 alterations is consistently in the **~14–20% range for IDH1** and lower for IDH2, with R132C dominant (makawita2024comprehensiveimmunogenomicprofiling pages 1-2, frampton2023ivosidenibareview pages 1-2, vaquero2024decipheringtheroleb pages 29-32).

## 10. Diagnostics
### Molecular confirmation of IDH mutation (standard clinical implementation)
**Tissue NGS** remains central; ClarIDHy eligibility required an IDH1 mutation “**as detected by an FDA‑approved test**” (FDA summary abstract, Mar 2022) (casak2022fdaapprovalsummary pages 1-2). Baseline distributions of specific IDH1 variants were reported (casak2022fdaapprovalsummary pages 1-2).

### Liquid biopsy (ctDNA) integration (2024 evidence)
- In a 2024 matched tissue/ctDNA cohort (128 total BTC; 32 matched pairs), “**All IDH1 mutations detected in tumor DNA were also identified in liquid biopsies**” (Jan 2024) (astier2024molecularprofilingof pages 1-2).
- A 2024 review reports tissue–blood concordance can be high but variable and timing-dependent; it notes IDH1 concordance reached **100%** when ctDNA collected **before systemic therapy** and dropped to **56%** when collected on therapy/stable disease, and cites overall concordance values including **74% overall** with **92% in iCCA** in one report (Oct 2024) (awosika2024integrationofcirculating pages 5-6).

### Diagnostic workup in high-risk PSC (surveillance/diagnostic performance)
Although PSC‑CCA is a distinct etiologic setting (not specific to IDH-mutant iCCA), it provides real-world diagnostic strategies for biliary malignancy:
- Combining **brush cytology + biopsy + FISH** increased sensitivity **from 42% to 82%** while keeping specificity ~100% in one cited analysis (Oct 2023) (catanzaro2023primarysclerosingcholangitisassociated pages 8-9).
- CA19‑9 thresholds show variable performance; one summary reports 129 U/mL achieving specificity 98.5% and sensitivity 78.6% in one study but far lower sensitivity in another; lower cutoffs improve sensitivity but reduce specificity/PPV (Oct 2023) (catanzaro2023primarysclerosingcholangitisassociated pages 7-8).
- An institutional PSC surveillance protocol described MRI/MRCP with DWI every **6 months** (Oct 2023) (catanzaro2023primarysclerosingcholangitisassociated pages 9-11).

## 11. Outcome / Prognosis
### General prognosis (advanced disease)
- One review reports “around **70%**” diagnosed with advanced disease (Oct 2023) (frampton2023ivosidenibareview pages 1-2).
- A case-based review states only “about **30%**” are eligible for resection at diagnosis, recurrence risk “up to **40%**,” median OS for unresectable/metastatic disease “**<12 months**,” and 5‑year survival “**<20%**” (Jul 2024) (muller2024sustainedclinicalresponse pages 1-2).

### IDH-mutant prognosis and immune phenotype
- IDH1 mutations (and FGFR2 fusions) are described as being associated with a **relatively good prognosis** compared with KRAS/BRAF-driven tumors in a 2024 immune‑genomic review (Oct 2024) (nishida2024geneticepigeneticalterationand pages 1-2).
- In the large 2024 CGP/immunogenomic cohort, no significant difference in retrospective mOS was observed between IDH1/2+ and IDH‑wildtype patients (Mar 2024) (makawita2024comprehensiveimmunogenomicprofiling pages 1-2).

## 12. Treatment
### Approved targeted therapy: mutant IDH1 inhibition (ivosidenib)
**Regulatory indication & pivotal trial**
- **Direct abstract quote (FDA approval summary):** “**On August 25, 2021, the FDA approved ivosidenib for the treatment of adult patients with unresectable locally advanced or metastatic… IDH1 mutated cholangiocarcinoma… with disease progression after 1 to 2 prior lines of systemic therapy**” (Mar 2022) (casak2022fdaapprovalsummary pages 1-2).
- FDA approval summary reports **PFS HR 0.37** (P<0.0001) and median OS 10.3 vs 7.5 months with crossover confounding (casak2022fdaapprovalsummary pages 1-2, casak2022fdaapprovalsummary media 6fe1eb4a, casak2022fdaapprovalsummary media 2f70fd07).

**Safety**
- FDA summary abstract lists common adverse reactions (>20%): “fatigue/asthenia, nausea, diarrhea, abdominal pain, ascites, vomiting, cough, and decreased appetite” (Mar 2022) (casak2022fdaapprovalsummary pages 1-2, casak2022fdaapprovalsummary media 085761fb).

**Pharmacodynamics / biomarker effect**
- Plasma 2‑HG suppression to near healthy levels is shown in the ClarIDHy PK/PD analysis (Jan 2024) (fan2024pharmacokineticspharmacodynamicsofivosidenib pages 1-2).

**Real‑world implementation**
- Italian real‑world cohort (n=11) reported median PFS 4.4 months and OS 15 months with no grade ≥3 treatment-related AEs (Jan 2023) (muller2024sustainedclinicalresponse pages 1-2).

| Study / evidence source | Therapy / regimen | Setting / line | Key endpoints and numeric results | Notable safety signals | Biomarker / PD findings | Publication year/date or NCT | URL |
|---|---|---|---|---|---|---|---|
| ClarIDHy phase III, FDA approval summary + immunogenomic background | Ivosidenib 500 mg orally once daily vs placebo | Previously treated, advanced unresectable/metastatic **IDH1-mutant** cholangiocarcinoma; progression after 1–2 prior systemic regimens; randomized 2:1; crossover allowed | **PFS HR 0.37** (95% CI 0.25–0.54; **P<0.0001**); median **OS 10.3 mo vs 7.5 mo**, **HR 0.79** (95% CI 0.56–1.12); Makawita background also cites **median PFS 2.7 vs 1.4 mo** and **mOS 10.3 vs 7.5 mo** (casak2022fdaapprovalsummary pages 1-2, makawita2024comprehensiveimmunogenomicprofiling pages 1-2) | AEs >20% with ivosidenib: fatigue/asthenia, nausea, diarrhea, abdominal pain, ascites, vomiting, cough, decreased appetite; placebo >20%: fatigue/asthenia, nausea, abdominal pain, vomiting (casak2022fdaapprovalsummary pages 1-2) | Established mutant-IDH1 targeting in CCA; background notes IDH1/2-altered tumors are relatively immune-cold with lower PD-L1, TMB, MSI-H than IDH-wt iCCA (makawita2024comprehensiveimmunogenomicprofiling pages 1-2, casak2022fdaapprovalsummary pages 1-2) | 2022 FDA summary; trial NCT02989857 (completed) | https://doi.org/10.1158/1078-0432.CCR-21-4462 |
| Phase I ivosidenib clinical study summarized by Lavacchi | Ivosidenib 500 mg once daily | Pretreated IDH1-mutant cholangiocarcinoma; 73 patients, 89% intrahepatic | **ORR 5%**, **DCR 61%**, median **PFS 3.8 mo** (95% CI 3.6–7.3), **6-mo PFS 40.1%**, **12-mo PFS 21.8%**, median **OS 13.8 mo** (95% CI 11.1–29.3) (lavacchi2022ivosidenibinidh1mutated pages 2-3) | Grade ≥3 ascites 5%, anemia 4%; QT prolongation 11% overall, grade 3 in 1 patient (lavacchi2022ivosidenibinidh1mutated pages 2-3) | Background biology: mutant IDH1 causes 2-HG accumulation; common baseline variants R132C 77%, R132L 11%; resistance alterations included IDH2-R172V and IDH1-R132F at progression (lavacchi2022ivosidenibinidh1mutated pages 2-3) | 2022 | https://doi.org/10.2139/ssrn.3977450 |
| Italian real-world experience (Rimini et al.) | Ivosidenib monotherapy | Clinical practice; second-/third-line advanced IDH1-mutant cholangiocarcinoma; 11 patients | Median **PFS 4.4 mo** (95% CI 2.0–5.8), median **OS 15.0 mo** (95% CI 6.6–15.0), **DCR 63%**, **PR 18%** (2/11) (muller2024sustainedclinicalresponse pages 1-2) | 18% had at least one treatment-related AE; **no grade ≥3** events; most frequent grade 2 AEs: prolonged QT interval, hypomagnesemia (muller2024sustainedclinicalresponse pages 1-2) | Molecular profiling in 8/11 showed common co-alterations in **TP53, BAP1, CDKN2A, CDKN2B**; R132C was the most prevalent IDH1 variant in related real-world reporting (muller2024sustainedclinicalresponse pages 1-2) | 2023 | https://doi.org/10.1177/17588359231171574 |
| ClarIDHy PK/PD biomarker analysis (Fan et al.) | Ivosidenib 500 mg once daily | PK/PD subset from phase III ClarIDHy; advanced IDH1-mutant cholangiocarcinoma | Clinical outcomes referenced from ClarIDHy; PK/PD paper itself emphasizes drug exposure and 2-HG suppression rather than new efficacy endpoints (fan2024pharmacokineticspharmacodynamicsofivosidenib pages 1-2) | No new major safety signal highlighted in excerpt; focus was PK/PD characterization (fan2024pharmacokineticspharmacodynamicsofivosidenib pages 1-2) | Rapid absorption (**Tmax ~2.63 h single dose, 2.07 h multiple dose**); mean plasma **2-HG fell from 1108 ng/mL at baseline to 97.7 ng/mL at C2D1**; average **2-HG inhibition 75.0%** at steady state; no 2-HG decrease with placebo (fan2024pharmacokineticspharmacodynamicsofivosidenib pages 1-2) | 2024 | https://doi.org/10.1007/s00280-023-04633-5 |
| ClinicalTrials.gov: ClarIDHy | Ivosidenib vs placebo | Previously treated advanced cholangiocarcinoma with IDH1 mutation | Registrational phase III trial; enrollment **187**; completed (casak2022fdaapprovalsummary pages 1-2) | See FDA summary row for safety outcomes (casak2022fdaapprovalsummary pages 1-2) | Trial enabled approval; placebo-to-ivosidenib crossover permitted (casak2022fdaapprovalsummary pages 1-2) | **NCT02989857** | https://clinicaltrials.gov/study/NCT02989857 |
| ClinicalTrials.gov: first-line combination study | Ivosidenib + durvalumab + gemcitabine/cisplatin | First-line locally advanced or metastatic cholangiocarcinoma with IDH1 mutation | Phase I/II; recruiting; planned enrollment **52**; no efficacy results yet available in provided context | Not yet reported in provided context | Rationale: combine IDH1 inhibition with chemoimmunotherapy in molecularly selected disease | **NCT06501625** | https://clinicaltrials.gov/study/NCT06501625 |
| ClinicalTrials.gov: observational real-world study | Ivosidenib in routine practice | Locally advanced or metastatic cholangiocarcinoma with **IDH1 R132** mutation after at least one prior systemic treatment | Observational; recruiting; planned enrollment **100**; intended to capture real-world effectiveness and treatment patterns | Real-world safety collection expected; no results yet in provided context | Reflects implementation of approved ivosidenib outside randomized trial setting | **NCT06607302** | https://clinicaltrials.gov/study/NCT06607302 |
| ClinicalTrials.gov: adjuvant / maintenance study | Ivosidenib maintenance after standard adjuvant chemotherapy | Curative-intent mIDH1 cholangiocarcinoma after SOC adjuvant chemotherapy | Phase II; recruiting; planned enrollment **40**; no outcome data yet in provided context | Not yet reported in provided context | Explores earlier-disease use after curative-intent therapy | **NCT07260175** | https://clinicaltrials.gov/study/NCT07260175 |
| ClinicalTrials.gov: IDH-mutant basket PARP study | Olaparib | Advanced glioma, cholangiocarcinoma, or solid tumors with **IDH1/2** mutations | Phase II basket trial; active, not recruiting; planned enrollment **89**; cholangiocarcinoma included but no CCA-specific efficacy data in provided context | Not reported in provided context | Based on therapeutic exploitation of IDH-associated vulnerabilities; cholangiocarcinoma cohort included | **NCT03212274** | https://clinicaltrials.gov/study/NCT03212274 |


*Table: This table summarizes pivotal trial data, pharmacodynamic findings, real-world implementation, and active clinical studies for IDH1-mutant cholangiocarcinoma therapies. It is useful for comparing efficacy, safety, biomarker effects, and where the treatment landscape is moving next.*

**MAXO (Medical Action Ontology) suggestions**
- **Small molecule therapy** (ivosidenib) targeting mutant IDH1 (casak2022fdaapprovalsummary pages 1-2)
- **Tumor molecular profiling / genomic testing** to select therapy (casak2022fdaapprovalsummary pages 1-2, astier2024molecularprofilingof pages 1-2)

### Emerging / experimental treatment directions (2023–2024)
- **Combination strategies leveraging immune reprogramming:** IDH inhibitors may restore antigen-presentation machinery and potentially improve ICI response (Oct 2024) (nishida2024geneticepigeneticalterationand pages 1-2).
- **SRC pathway targeting in IDH-mutant iCCA:** preclinical evidence supports dasatinib sensitivity and combination with S6K/AKT inhibitor M2698 (May 2024) (luk2024srcinhibitionenables pages 1-2).
- **Active clinical trials (examples):**
  - First-line combination: ivosidenib + durvalumab + gemcitabine/cisplatin (**NCT06501625**) (frampton2023ivosidenibareview pages 1-2)
  - Observational real-world: ivosidenib after ≥1 prior line (**NCT06607302**) (frampton2023ivosidenibareview pages 1-2)
  - Maintenance/adjuvant strategy: ivosidenib maintenance after SOC adjuvant chemotherapy (**NCT07260175**) (frampton2023ivosidenibareview pages 1-2)
  - Basket vulnerability exploitation: olaparib in IDH1/2‑mutant tumors including cholangiocarcinoma (**NCT03212274**) (frampton2023ivosidenibareview pages 1-2)

## 13. Prevention
Subtype-specific prevention for IDH-mutant iCCA is not established in the retrieved evidence.

High-risk prevention/surveillance paradigms exist for etiologic risk conditions:
- **PSC surveillance:** imaging + biomarkers in structured follow-up; one review emphasizes surveillance is “mandatory” and provides MRI/MRCP-based protocols (catanzaro2023primarysclerosingcholangitisassociated pages 9-11).
- **Fluke-related CCA prevention:** infection control (anti-helminthics, education, hygiene) is repeatedly noted as a preventive principle (qualitative) (ciobica2024theconstellationof pages 2-3).

## 14. Other Species / Natural Disease
No cross-species naturally occurring disease data were identified in the retrieved corpus.

## 15. Model organisms and experimental systems
### Preclinical models used for IDH-mutant iCCA
- **Patient-derived organoids and patient-derived xenografts (PDX):** used in mechanistic dependency work (SRC/MAGI1‑PP2A/S6K) (luk2024srcinhibitionenables pages 1-2).
- **Genetically engineered mouse model (GEMM) explicitly including Idh1 mutation:** Alb‑Cre; KrasLSL‑G12D; Idh1LSL‑R132 reported with **100% penetrance** and latency 27–54 weeks, producing multifocal iCCA with metastasis (reviewed in 2024) (vaquero2024decipheringtherole pages 25-29).

## Key recent developments (prioritizing 2023–2024)
1) **Large-scale immunogenomics of IDH1/2‑altered iCCA** (Mar 2024): clear evidence that IDH-altered iCCA is relatively immune-cold and has lower MSI‑H/TMB‑high/PD‑L1 positivity than IDH‑wildtype iCCA (makawita2024comprehensiveimmunogenomicprofiling pages 1-2).
2) **Mechanistic dependency in IDH-mutant iCCA** (May 2024): SRC-driven translational signaling vulnerability actionable with dasatinib±M2698 in organoids/PDX (luk2024srcinhibitionenables pages 1-2).
3) **Biomarker-confirmed on-target activity of ivosidenib** (Jan 2024): robust plasma 2‑HG suppression in ClarIDHy PK/PD study (fan2024pharmacokineticspharmacodynamicsofivosidenib pages 1-2).
4) **ctDNA evidence supporting IDH1 detection** (Jan 2024; Oct 2024): high detection and timing-dependent concordance with tissue; IDH1 appears comparatively reliable in ctDNA relative to certain fusions (astier2024molecularprofilingof pages 1-2, awosika2024integrationofcirculating pages 5-6).

## Evidence-backed statistics (selected)
- iCCA proportion of CCA: **10–20%** (frampton2023ivosidenibareview pages 1-2).
- Advanced presentation: ~**70%** diagnosed at advanced stage (frampton2023ivosidenibareview pages 1-2).
- IDH1 frequency in iCCA: **~14%** in a 3,067-case CGP cohort (makawita2024comprehensiveimmunogenomicprofiling pages 1-2).
- IDH2 frequency in iCCA: **~4%** in the same cohort (makawita2024comprehensiveimmunogenomicprofiling pages 1-2).
- Dominant variant: IDH1 **R132C** (69% in CGP cohort; 68–74% in ClarIDHy baseline) (makawita2024comprehensiveimmunogenomicprofiling pages 1-2, casak2022fdaapprovalsummary pages 1-2).
- ClarIDHy FDA summary: **PFS HR 0.37**; median OS **10.3 vs 7.5 months** (casak2022fdaapprovalsummary pages 1-2, casak2022fdaapprovalsummary media 6fe1eb4a, casak2022fdaapprovalsummary media 2f70fd07).
- PD effect: mean plasma 2‑HG reduced **1108 → 97.7 ng/mL**; **75% inhibition** at steady state (fan2024pharmacokineticspharmacodynamicsofivosidenib pages 1-2).

## Notes on limitations of this report
- Several requested identifier types (ICD‑10/ICD‑11, MeSH, Orphanet, OMIM) and detailed phenotype frequencies were not available in the retrieved tool corpus and were therefore not asserted.
- Where PSC-CCA surveillance or fluke-related prevention is discussed, it reflects **general CCA prevention/surveillance** rather than evidence specific to the IDH-mutant molecular subtype.


References

1. (casak2022fdaapprovalsummary pages 1-2): Sandra J. Casak, Shan Pradhan, Lola A. Fashoyin-Aje, Yi Ren, Yuan-Li Shen, Yuan Xu, Edwin Chiu Yuen Chow, Ye Xiong, Jeanne Fourie Zirklelbach, Jiang Liu, Rosane Charlab, William F. Pierce, Nataliya Fesenko, Julia A. Beaver, Richard Pazdur, Paul G. Kluetz, and Steven J. Lemery. Fda approval summary: ivosidenib for the treatment of patients with advanced unresectable or metastatic, chemotherapy refractory cholangiocarcinoma with an idh1 mutation. Clinical Cancer Research, 28:2733-2737, Mar 2022. URL: https://doi.org/10.1158/1078-0432.ccr-21-4462, doi:10.1158/1078-0432.ccr-21-4462. This article has 73 citations and is from a highest quality peer-reviewed journal.

2. (makawita2024comprehensiveimmunogenomicprofiling pages 1-2): Shalini Makawita, Sunyoung Lee, Elisabeth Kong, Lawrence N. Kwong, Zeyad Abouelfetouh, Anaemy Danner De Armas, Lianchun Xiao, Karthikeyan Murugesan, Natalie Danziger, Dean Pavlick, Anil Korkut, Jeffrey S. Ross, and Milind Javle. Comprehensive immunogenomic profiling of idh1-/2-altered cholangiocarcinoma. JCO Precision Oncology, Mar 2024. URL: https://doi.org/10.1200/po.23.00544, doi:10.1200/po.23.00544. This article has 19 citations and is from a peer-reviewed journal.

3. (vaquero2024decipheringtheroleb pages 29-32): MC Fernández Vaquero. Deciphering the role of mutant-idh1 in liver cancer development and the tumor immune microenvironment. Unknown journal, 2024.

4. (fan2024pharmacokineticspharmacodynamicsofivosidenib pages 1-2): Bin Fan, Ghassan K. Abou-Alfa, Andrew X. Zhu, Shuchi S. Pandya, Hongxia Jia, Feng Yin, Camelia Gliser, Zhaowei Hua, Mohammad Hossain, and Hua Yang. Pharmacokinetics/pharmacodynamics of ivosidenib in advanced idh1-mutant cholangiocarcinoma: findings from the phase iii claridhy study. Cancer Chemotherapy and Pharmacology, 93:471-479, Jan 2024. URL: https://doi.org/10.1007/s00280-023-04633-5, doi:10.1007/s00280-023-04633-5. This article has 8 citations and is from a peer-reviewed journal.

5. (frampton2023ivosidenibareview pages 1-2): James E. Frampton. Ivosidenib: a review in advanced cholangiocarcinoma. Targeted Oncology, 18:973-980, Oct 2023. URL: https://doi.org/10.1007/s11523-023-01002-3, doi:10.1007/s11523-023-01002-3. This article has 8 citations and is from a peer-reviewed journal.

6. (lavacchi2022ivosidenibinidh1mutated pages 2-3): Daniele Lavacchi, Enrico Caliman, Gemma Rossi, Eleonora Buttitta, Cristina Botteri, Sara Fancelli, Elisa Pellegrini, Giandomenico Roviello, Serena Pillozzi, and Lorenzo Antonuzzo. Ivosidenib in idh1-mutated cholangiocarcinoma: clinical evaluation and future directions. Pharmacology & therapeutics, pages 108170, Mar 2022. URL: https://doi.org/10.2139/ssrn.3977450, doi:10.2139/ssrn.3977450. This article has 29 citations and is from a domain leading peer-reviewed journal.

7. (casak2022fdaapprovalsummary media 6fe1eb4a): Sandra J. Casak, Shan Pradhan, Lola A. Fashoyin-Aje, Yi Ren, Yuan-Li Shen, Yuan Xu, Edwin Chiu Yuen Chow, Ye Xiong, Jeanne Fourie Zirklelbach, Jiang Liu, Rosane Charlab, William F. Pierce, Nataliya Fesenko, Julia A. Beaver, Richard Pazdur, Paul G. Kluetz, and Steven J. Lemery. Fda approval summary: ivosidenib for the treatment of patients with advanced unresectable or metastatic, chemotherapy refractory cholangiocarcinoma with an idh1 mutation. Clinical Cancer Research, 28:2733-2737, Mar 2022. URL: https://doi.org/10.1158/1078-0432.ccr-21-4462, doi:10.1158/1078-0432.ccr-21-4462. This article has 73 citations and is from a highest quality peer-reviewed journal.

8. (casak2022fdaapprovalsummary media 2f70fd07): Sandra J. Casak, Shan Pradhan, Lola A. Fashoyin-Aje, Yi Ren, Yuan-Li Shen, Yuan Xu, Edwin Chiu Yuen Chow, Ye Xiong, Jeanne Fourie Zirklelbach, Jiang Liu, Rosane Charlab, William F. Pierce, Nataliya Fesenko, Julia A. Beaver, Richard Pazdur, Paul G. Kluetz, and Steven J. Lemery. Fda approval summary: ivosidenib for the treatment of patients with advanced unresectable or metastatic, chemotherapy refractory cholangiocarcinoma with an idh1 mutation. Clinical Cancer Research, 28:2733-2737, Mar 2022. URL: https://doi.org/10.1158/1078-0432.ccr-21-4462, doi:10.1158/1078-0432.ccr-21-4462. This article has 73 citations and is from a highest quality peer-reviewed journal.

9. (muller2024sustainedclinicalresponse pages 1-2): Christian Müller, Sabine Franke, Timo Reisländer, Verena Keitel, and Marino Venerito. Sustained clinical response to ivosidenib in previously treated patients with advanced intrahepatic cholangiocarcinoma harboring an idh1 r132 mutation: two case reports. Case Reports in Oncology, 17:753-762, Jul 2024. URL: https://doi.org/10.1159/000539665, doi:10.1159/000539665. This article has 3 citations.

10. (luk2024srcinhibitionenables pages 1-2): Iris S. Luk, Caroline M. Bridgwater, Angela Yu, Liberalis D. Boila, Mariana Yáñez-Bartolomé, Aaron E. Lampano, Taylor S. Hulahan, Myriam Boukhali, Meena Kathiresan, Teresa Macarulla, Heidi L. Kenerson, Naomi Yamamoto, David Sokolov, Ian A. Engstrom, Lucas B. Sullivan, Paul D. Lampe, Jonathan A. Cooper, Raymond S. Yeung, Tian V. Tian, Wilhelm Haas, Supriya K. Saha, and Sita Kugel. Src inhibition enables formation of a growth suppressive magi1-pp2a complex in isocitrate dehydrogenase-mutant cholangiocarcinoma. Science Translational Medicine, May 2024. URL: https://doi.org/10.1126/scitranslmed.adj7685, doi:10.1126/scitranslmed.adj7685. This article has 19 citations and is from a highest quality peer-reviewed journal.

11. (vaquero2024decipheringtherole pages 25-29): MC Fernández Vaquero. Deciphering the role of mutant-idh1 in liver cancer development and the tumor immune microenvironment. Unknown journal, 2024.

12. (catanzaro2023primarysclerosingcholangitisassociated pages 1-2): Elisa Catanzaro, Enrico Gringeri, Patrizia Burra, and Martina Gambato. Primary sclerosing cholangitis-associated cholangiocarcinoma: from pathogenesis to diagnostic and surveillance strategies. Cancers, 15:4947, Oct 2023. URL: https://doi.org/10.3390/cancers15204947, doi:10.3390/cancers15204947. This article has 29 citations.

13. (catanzaro2023primarysclerosingcholangitisassociated pages 9-11): Elisa Catanzaro, Enrico Gringeri, Patrizia Burra, and Martina Gambato. Primary sclerosing cholangitis-associated cholangiocarcinoma: from pathogenesis to diagnostic and surveillance strategies. Cancers, 15:4947, Oct 2023. URL: https://doi.org/10.3390/cancers15204947, doi:10.3390/cancers15204947. This article has 29 citations.

14. (catanzaro2023primarysclerosingcholangitisassociated pages 2-4): Elisa Catanzaro, Enrico Gringeri, Patrizia Burra, and Martina Gambato. Primary sclerosing cholangitis-associated cholangiocarcinoma: from pathogenesis to diagnostic and surveillance strategies. Cancers, 15:4947, Oct 2023. URL: https://doi.org/10.3390/cancers15204947, doi:10.3390/cancers15204947. This article has 29 citations.

15. (ciobica2024theconstellationof pages 2-3): Mihai-Lucian Ciobica, Bianca-Andreea Sandulescu, Liana-Maria Chicea, Mihaela Iordache, Maria-Laura Groseanu, Mara Carsote, Claudiu Nistor, and Ana-Maria Radu. The constellation of risk factors and paraneoplastic syndromes in cholangiocarcinoma: integrating the endocrine panel amid tumour-related biology (a narrative review). Biology, 13:662, Aug 2024. URL: https://doi.org/10.3390/biology13090662, doi:10.3390/biology13090662. This article has 1 citations.

16. (nishida2024geneticepigeneticalterationand pages 1-2): Naoshi Nishida and Masatoshi Kudo. Genetic/epigenetic alteration and tumor immune microenvironment in intrahepatic cholangiocarcinoma: transforming the immune microenvironment with molecular-targeted agents. Liver Cancer, 13:136-149, Oct 2024. URL: https://doi.org/10.1159/000534443, doi:10.1159/000534443. This article has 17 citations and is from a peer-reviewed journal.

17. (martinserrano2023novelmicroenvironmentbasedclassification pages 1-3): Miguel A Martin-Serrano, Benjamin Kepecs, Miguel Torres-Martin, Emily R Bramel, Philipp K Haber, Elliot Merritt, Alexander Rialdi, Nesteene Joy Param, Miho Maeda, Katherine E Lindblad, James K Carter, Marina Barcena-Varela, Vincenzo Mazzaferro, Myron Schwartz, Silvia Affo, Robert F Schwabe, Augusto Villanueva, Ernesto Guccione, Scott L Friedman, Amaia Lujambio, Anna Tocheva, Josep M Llovet, Swan N Thung, Alexander M Tsankov, and Daniela Sia. Novel microenvironment-based classification of intrahepatic cholangiocarcinoma with therapeutic implications. Gut, 72:736-748, May 2023. URL: https://doi.org/10.1136/gutjnl-2021-326514, doi:10.1136/gutjnl-2021-326514. This article has 156 citations and is from a highest quality peer-reviewed journal.

18. (astier2024molecularprofilingof pages 1-2): Clémence Astier, Carine Ngo, Léo Colmet-Daage, Virginie Marty, Olivia Bawa, Claudio Nicotra, Maud Ngo-Camus, Antoine Italiano, Christophe Massard, Jean-Yves Scoazec, Cristina Smolenschi, Michel Ducreux, Antoine Hollebecque, and Sophie Postel-Vinay. Molecular profiling of biliary tract cancers reveals distinct genomic landscapes between circulating and tissue tumor dna. Experimental Hematology & Oncology, Jan 2024. URL: https://doi.org/10.1186/s40164-023-00470-7, doi:10.1186/s40164-023-00470-7. This article has 19 citations and is from a peer-reviewed journal.

19. (awosika2024integrationofcirculating pages 5-6): Joy A Awosika, Cecilia Monge, and Tim F Greten. Integration of circulating tumor dna in biliary tract cancer: the emerging landscape. Hepatic Oncology, Oct 2024. URL: https://doi.org/10.1080/20450923.2024.2403334, doi:10.1080/20450923.2024.2403334. This article has 7 citations.

20. (catanzaro2023primarysclerosingcholangitisassociated pages 8-9): Elisa Catanzaro, Enrico Gringeri, Patrizia Burra, and Martina Gambato. Primary sclerosing cholangitis-associated cholangiocarcinoma: from pathogenesis to diagnostic and surveillance strategies. Cancers, 15:4947, Oct 2023. URL: https://doi.org/10.3390/cancers15204947, doi:10.3390/cancers15204947. This article has 29 citations.

21. (catanzaro2023primarysclerosingcholangitisassociated pages 7-8): Elisa Catanzaro, Enrico Gringeri, Patrizia Burra, and Martina Gambato. Primary sclerosing cholangitis-associated cholangiocarcinoma: from pathogenesis to diagnostic and surveillance strategies. Cancers, 15:4947, Oct 2023. URL: https://doi.org/10.3390/cancers15204947, doi:10.3390/cancers15204947. This article has 29 citations.

22. (casak2022fdaapprovalsummary media 085761fb): Sandra J. Casak, Shan Pradhan, Lola A. Fashoyin-Aje, Yi Ren, Yuan-Li Shen, Yuan Xu, Edwin Chiu Yuen Chow, Ye Xiong, Jeanne Fourie Zirklelbach, Jiang Liu, Rosane Charlab, William F. Pierce, Nataliya Fesenko, Julia A. Beaver, Richard Pazdur, Paul G. Kluetz, and Steven J. Lemery. Fda approval summary: ivosidenib for the treatment of patients with advanced unresectable or metastatic, chemotherapy refractory cholangiocarcinoma with an idh1 mutation. Clinical Cancer Research, 28:2733-2737, Mar 2022. URL: https://doi.org/10.1158/1078-0432.ccr-21-4462, doi:10.1158/1078-0432.ccr-21-4462. This article has 73 citations and is from a highest quality peer-reviewed journal.
