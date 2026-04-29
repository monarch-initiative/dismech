---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-05T17:42:13.558705'
end_time: '2026-04-05T17:54:20.903865'
duration_seconds: 727.35
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: KIT Mutant Melanoma
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
- **Disease Name:** KIT Mutant Melanoma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **KIT Mutant Melanoma** covering all of the
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
- **Disease Name:** KIT Mutant Melanoma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **KIT Mutant Melanoma** covering all of the
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


# KIT Mutant Melanoma — Disease Characteristics Research Report (2026-04-06)

## Target Disease
- **Disease name:** KIT-mutant melanoma (melanoma with activating KIT alterations)
- **Category:** Molecularly defined melanoma subtype; enriched in **acral** and **mucosal** melanomas and a subset of **chronically sun-damaged (CSD)** cutaneous melanomas.
- **MONDO / MeSH / ICD identifiers:** Not retrieved in the current evidence set; the sources accessed are primarily clinical-trial and review literature rather than ontology crosswalks.

---

## 1. Disease Information

### Overview / definition
KIT-mutant melanoma refers to melanoma in which **KIT (CD117) proto-oncogene receptor tyrosine kinase** is altered in a way that functionally drives tumor behavior (typically **activating point mutations/indels**, sometimes with concurrent copy-number gain). Clinically, KIT-driven melanomas are most often described in **mucosal**, **acral**, and **chronically sun-damaged** primary sites, and are therapeutically relevant because they can be sensitive to KIT tyrosine kinase inhibitors (TKIs) when **activating KIT mutations** are present. In a key phase II trial, the investigators framed the actionable setting as “metastatic mucosal, acral, or chronically sun-damaged (CSD) melanoma with KIT amplifications and/or mutations,” and concluded that such melanomas “should be assessed for KIT mutations” because imatinib “can be effective when tumors harbor KIT mutations, but not if KIT is amplified only.” (hodi2013imatinibformelanomas pages 1-2)

### Common synonyms / alternative names
- KIT-altered melanoma
- KIT-driven melanoma
- c-KIT-mutated melanoma / CD117-mutant melanoma
- KIT-mutant acral melanoma; KIT-mutant mucosal melanoma

### Aggregation level of evidence
The characterization here is derived primarily from **aggregated disease-level resources** (genomic subtype reviews) and **prospective clinical trials** enrolling defined KIT-altered populations, rather than individual EHR-derived case series (yang2023thegenomiclandscape pages 2-4, larkin2024nilotinibinkitdriven pages 3-5, guo2011phaseiiopenlabel pages 1-2, hodi2013imatinibformelanomas pages 1-2, guo2017efficacyandsafety pages 1-7).

---

## 2. Etiology

### Disease causal factors
**Primary causal factor (molecular):** somatic activating alterations in **KIT**, a receptor tyrosine kinase, producing constitutive or exaggerated pro-survival/proliferation signaling through canonical RTK pathways (PI3K/AKT, MAPK/ERK, JAK/STAT, SRC family pathways) (cilloni2024detectionofkit pages 3-5, abdellateif2023ckitreceptorsas pages 1-2).

### Risk factors
Evidence in the retrieved corpus supports **subtype and anatomic-site association** rather than classic exposure-based risk factors:
- KIT alterations are **uncommon overall** but **enriched** in mucosal and acral melanomas, and occur in a subset of melanomas on chronically sun-damaged skin (jung2022clinicalandgenomic pages 1-2).

### Protective factors / gene–environment interactions
Not identified in the retrieved sources.

---

## 3. Phenotypes (clinical presentation)

Because KIT-mutant melanoma is a molecular subtype spanning multiple anatomic melanoma subtypes, phenotype is best summarized by the **parent clinicopathologic subtype**.

### Acral melanoma phenotypes
Acral melanoma arises from palmar/plantar/nail unit melanocytes and has distinct biology and typically worse outcomes than non-acral cutaneous melanoma (yang2023thegenomiclandscape pages 2-4). Suggested phenotypes and ontology mappings:
- **Acral primary site involvement** (UBERON: e.g., *skin of palm*, *skin of sole*, *nail unit*).
- **Advanced-stage presentation** / metastatic disease at diagnosis (HPO: *Neoplasm metastasis* [HP:0003002]).

### Mucosal melanoma phenotypes
Mucosal melanoma arises from mucosal melanocytes (anatomic sites vary: sinonasal, anorectal, vulvovaginal, etc.). In molecular surveys, KIT is commonly the most frequent driver in mucosal melanoma (yang2023thegenomiclandscape pages 2-4).
Suggested mappings:
- **Mucosal primary site involvement** (UBERON: *mucosa* plus site-specific terms).
- **Local invasion and metastasis** (HPO: HP:0003002).

### HPO term suggestions (general melanoma manifestations)
- Neoplasm of the skin / melanoma: *Cutaneous melanoma* (disease concept; HPO terms may vary by knowledge base)
- Metastatic disease: **HP:0003002** (Neoplasm metastasis)
- Lymph node metastasis: **HP:0001416** (if present clinically)

**Frequency/severity/progression:** Specific symptom-level frequencies (pain, bleeding, etc.) are not quantified in the retrieved sources; the strongest quantitative phenotype-like data available are subtype distributions and treatment responses by subtype and genotype (jung2022clinicalandgenomic pages 4-5, larkin2024nilotinibinkitdriven pages 5-6).

---

## 4. Genetic / Molecular Information

### Causal gene
- **KIT** (KIT proto-oncogene, receptor tyrosine kinase)

### Pathogenic variant spectrum (melanoma)
KIT alterations in melanoma are heterogeneous and can involve multiple exons. Across imatinib- and nilotinib-era data, responses are enriched in **exon 11** and **exon 13** alterations, particularly **L576P (exon 11)** and **K642E (exon 13)** (jung2022clinicalandgenomic pages 1-2, guo2011phaseiiopenlabel pages 1-2).

**Subtype enrichment and mutation frequency:**
- In a 2023 genomic review summarizing multiple studies, KIT mutation frequency was **1.8%** in “UV-related” melanomas, **10.9–24.4%** in acral melanoma, and **19.1–23.1%** in mucosal melanoma (yang2023thegenomiclandscape pages 4-5, yang2023thegenomiclandscape media 3d8ffda1).
- Another 2022 pooled analysis summarizes that KIT alterations are ~**1–7% overall**, enriched to ~**10–20%** in mucosal and acral melanoma, and ~**1–2%** in melanomas arising from chronically sun-damaged skin (jung2022clinicalandgenomic pages 1-2).

### Somatic vs germline
The clinical trials and genomic reviews accessed describe KIT alterations as **tumor (somatic) alterations** in advanced melanoma populations (guo2011phaseiiopenlabel pages 1-2, hodi2013imatinibformelanomas pages 1-2, guo2017efficacyandsafety pages 1-7, janku2022efficacyandsafety pages 3-4). Germline predisposition was not addressed in the retrieved sources.

### Functional consequences / mechanism (molecular chain)
1. **Upstream trigger:** activating KIT mutation (e.g., juxtamembrane/kinase-domain variants) → ligand-independent or dysregulated RTK signaling.
2. **Receptor activation and phosphorylation:** SCF binding normally induces KIT dimerization and autophosphorylation; in cancer, gain-of-function KIT alterations can cause constitutive activation (cilloni2024detectionofkit pages 3-5, abdellateif2023ckitreceptorsas pages 1-2).
3. **Downstream signaling:** activation of PI3K/AKT (survival/proliferation), MAPK/ERK (transcription/proliferation), SRC kinases (motility/angiogenesis), and JAK/STAT (transcription programs) (cilloni2024detectionofkit pages 3-5, abdellateif2023ckitreceptorsas pages 1-2).
4. **Cellular outcomes:** sustained proliferation and apoptosis resistance → tumor growth and metastasis potential.

### Suggested GO (biological process) terms
- GO:0007169 **transmembrane receptor protein tyrosine kinase signaling pathway**
- GO:0008284 **positive regulation of cell population proliferation**
- GO:0043065 **positive regulation of apoptotic process** (context-specific; KIT signaling can inhibit apoptosis)
- GO:0000165 **MAPK cascade**
- GO:0014066 **regulation of phosphatidylinositol 3-kinase signaling**

### Suggested Cell Ontology (CL) terms
- CL:0000148 **melanocyte** (primary lineage cell)
- CL:0000236 **B cell** / CL:0000624 **CD8-positive, alpha-beta T cell** (relevant to tumor microenvironment discussions, especially when considering immunotherapy combinations; mechanistic immunology was not deeply quantified in retrieved sources)

---

## 5. Environmental Information
No KIT-mutant-specific environmental triggers were identified in the retrieved sources. KIT-mutant melanoma is instead primarily associated with **anatomic subtype** and **non-UV (acral/mucosal) biology** (yang2023thegenomiclandscape pages 2-4, jung2022clinicalandgenomic pages 1-2).

---

## 6. Mechanism / Pathophysiology

### Key pathways
- **PI3K/AKT** and **MAPK/ERK** are emphasized as principal downstream effector pathways of c-KIT signaling, promoting survival and proliferation, while SRC and JAK/STAT contribute to motility/angiogenesis and transcriptional programs (cilloni2024detectionofkit pages 3-5, abdellateif2023ckitreceptorsas pages 1-2).

### Resistance mechanisms (clinical inference)
- In the imatinib phase II trial across mucosal/acral/CSD melanoma, “NRAS mutations and KIT copy number gain may be mechanisms of therapeutic resistance to imatinib.” (hodi2013imatinibformelanomas pages 1-2)
- In the ripretinib phase I expansion, prior KIT inhibitor exposure was associated with lower ORR and shorter median PFS compared with KIT-inhibitor–naïve patients (janku2022efficacyandsafety pages 1-2, janku2022efficacyandsafety pages 4-5).

---

## 7. Anatomical Structures Affected

### Primary sites (by subtype)
- **Acral skin structures**: palm/sole/nail unit (UBERON mappings as above) (yang2023thegenomiclandscape pages 2-4)
- **Mucosal surfaces** (site-specific mucosa) (yang2023thegenomiclandscape pages 2-4)
- **Chronically sun-damaged skin** (head/neck or other chronically UV-exposed skin; CSD category used for trial eligibility) (hodi2013imatinibformelanomas pages 1-2)

### Metastatic sites
Common metastatic patterns are not enumerated in retrieved sources; advanced/metastatic disease is the predominant study population across trials (guo2011phaseiiopenlabel pages 1-2, hodi2013imatinibformelanomas pages 1-2, guo2017efficacyandsafety pages 1-7, janku2022efficacyandsafety pages 3-4).

---

## 8. Temporal Development

### Onset
Typically **adult-onset** melanoma; age distribution not comprehensively extracted in the present evidence set.

### Progression
KIT-mutant melanomas in trials are often **advanced/metastatic**. In multiple TKI trials, median PFS is generally on the order of months (see Treatment section), consistent with the common clinical observation that responses—when present—may be clinically meaningful but not uniformly durable (guo2011phaseiiopenlabel pages 1-2, hodi2013imatinibformelanomas pages 5-6, guo2017efficacyandsafety pages 1-7).

---

## 9. Inheritance and Population

### Epidemiology (mutation frequency by subtype)
A 2023 genomic synthesis reported KIT mutation frequencies by subtype (compiled from multiple cohorts):
- **UV-related melanoma:** **1.8%**
- **Acral melanoma:** **10.9–24.4%**
- **Mucosal melanoma:** **19.1–23.1%**
(Visual evidence: Table 2 in the review) (yang2023thegenomiclandscape pages 4-5, yang2023thegenomiclandscape media 3d8ffda1)

Another pooled clinical genomics analysis summarizes KIT alterations at:
- **~1–7% overall melanoma**
- **~10–20% in mucosal melanoma**
- **~10–20% in acral melanoma**
- **~1–2% in chronically sun-damaged skin melanomas**
(jung2022clinicalandgenomic pages 1-2)

### Population demographics
Not robustly extractable from the retrieved sources beyond subtype enrichment.

---

## 10. Diagnostics

### Molecular testing approach (tumor)
Key trials used **targeted KIT exon sequencing** to identify actionable mutations.
- NICAM eligibility required tumors with KIT mutations screened by “Sanger sequencing of exons 9, 11, 13 and 17” (larkin2024nilotinibinkitdriven pages 14-15).
- Hodi et al. enrolled patients with KIT “amplifications and/or mutations” but the strongest benefit was in mutation-positive disease (hodi2013imatinibformelanomas pages 1-2).

### KIT amplification assessment
- In NICAM, KIT amplification was assessed exploratorily by **FISH** on archival FFPE (larkin2024nilotinibinkitdriven pages 14-15).
- In Hodi et al., objective responses were absent in amplification-only tumors, supporting **mutation-first** prioritization for predicting TKI response (hodi2013imatinibformelanomas pages 1-2).

### Liquid biopsy / ctDNA (recent implementation)
NICAM provides notable contemporary evidence for ctDNA-based KIT testing:
- “concordance between ctDNA and matched FFPE tumor mutation calls was **100%**” (larkin2024nilotinibinkitdriven pages 6-8).
- Authors state that “ddPCR-based KIT analysis appears feasible and accu-rate for KIT testing in patients with metastatic MM and AM and could be proposed for liquid biopsies testing” (larkin2024nilotinibinkitdriven pages 9-10).

### Differential diagnosis
Not detailed in retrieved sources; in practice, differential diagnosis is dominated by distinguishing melanoma subtype and excluding alternative primary sites and other oncogene drivers (BRAF/NRAS/NF1), but detailed diagnostic criteria and pathology differentials were not accessed here.

---

## 11. Outcome / Prognosis

### Prognostic notes (treatment-linked)
Prognosis in KIT-mutant melanoma is heterogeneous and strongly influenced by stage and treatment responsiveness. Across KIT TKI trials, median OS values ranged from ~7–18 months depending on study era, population, and treatment line (e.g., NICAM 7.7 months; TEAM 18.0 months; Hodi imatinib 12.5 months) (larkin2024nilotinibinkitdriven pages 5-6, hodi2013imatinibformelanomas pages 5-6, guo2017efficacyandsafety pages 1-7).

---

## 12. Treatment

### Current applications (real-world implementation)
The principal real-world application is **genotype-guided use of KIT TKIs** in advanced KIT-mutant melanoma (especially acral/mucosal/CSD primary sites). A central practical point supported by a prospective trial is that **KIT amplification without activating mutation is not a reliable predictor of imatinib response** (hodi2013imatinibformelanomas pages 1-2).

### Key clinical evidence (prospective trials)
| Study (year, journal) | Population/subtype and KIT alteration eligibility | N | Key outcomes (ORR/BORR, DCR, median PFS/TTP, median OS) | Key genotype associations (exon/variant) | Notes |
|---|---|---:|---|---|---|
| Imatinib — Guo 2011, *J Clin Oncol* | Metastatic melanoma with c-KIT mutation or amplification; open-label single-arm phase II (guo2011phaseiiopenlabel pages 1-2) | 43 | ORR 23.3% (10/43); DCR 53.5% (10 PR + 13 SD); median PFS 3.5 mo; 6-mo PFS 36.6%; 1-y OS 51.0% (guo2011phaseiiopenlabel pages 1-2) | 9/10 PRs occurred in exon 11 or 13 mutations (guo2011phaseiiopenlabel pages 1-2) | Dose escalation to 800 mg/d rarely restored disease control (guo2011phaseiiopenlabel pages 1-2) |
| Imatinib — Hodi 2013, *J Clin Oncol* | Metastatic mucosal, acral, or chronically sun-damaged melanoma with KIT amplification and/or mutation; multicenter phase II (hodi2013imatinibformelanomas pages 1-2) | 25 enrolled; 24 evaluable | BORR 29% (21% excluding nonconfirmed responses); DCR 50%; overall TTP 3.7 mo; OS 12.5 mo (hodi2013imatinibformelanomas pages 1-2, hodi2013imatinibformelanomas pages 5-6) | KIT-mutated tumors: BORR 7/13 (54%), DCR 77%; KIT amplified-only tumors: BORR 0%, DCR 18% (hodi2013imatinibformelanomas pages 1-2, hodi2013imatinibformelanomas pages 3-4) | Amplification-only lacked objective responses; pretreatment NRAS mutations and KIT copy-number gain implicated in resistance (hodi2013imatinibformelanomas pages 1-2, hodi2013imatinibformelanomas pages 5-6) |
| Nilotinib — Carvajal 2015, *Clin Cancer Res* | Melanoma with KIT mutations or amplification after prior KIT inhibitor; cohort A refractory/intolerant to prior KIT inhibitor, cohort B brain metastases (carvajal2015phaseiistudy pages 1-3) | 20 enrolled; 19 treated | Cohort A primary endpoint achieved in 27%; cohort B 12.5%; ORR 18.2% in cohort A, 0 in cohort B; median TTP 3.3 mo; median OS 9.1 mo (carvajal2015phaseiistudy pages 1-3) | Maintains activity against a range of exon 9, 11, and 13 KIT mutations (carvajal2015phaseiistudy pages 1-3) | Limited efficacy in brain metastases (carvajal2015phaseiistudy pages 1-3) |
| Nilotinib — TEAM 2017, *Ann Oncol* | Advanced/inoperable KIT-mutated melanoma without prior KIT inhibitor; global single-arm phase II (guo2017efficacyandsafety pages 1-7) | 42 | ORR 26.2% (11/42); all responses PRs; median response duration 7.1 mo; median PFS 4.2 mo; 6-mo PFS 34.6%; median OS 18.0 mo (guo2017efficacyandsafety pages 7-12, guo2017efficacyandsafety pages 1-7) | 10/11 responders had exon 11 mutations; exon 11 PR rate 10/26 (38.5%), exon 13 PR rate 1/13 (7.7%), exon 9/17 no responses; 4 responders had L576P (guo2017efficacyandsafety pages 7-12, guo2017efficacyandsafety pages 1-7) | Activity similar to historical imatinib, strongest in exon 11/L576P (guo2017efficacyandsafety pages 1-7) |
| Nilotinib — NICAM 2024, *Cell Reports Medicine* | KIT-mutated metastatic mucosal and acral melanoma; single-arm phase II; prior TKI excluded; exploratory KIT amplification/FISH and ctDNA ddPCR analyses (larkin2024nilotinibinkitdriven pages 14-15, larkin2024nilotinibinkitdriven pages 1-3) | 29 treated; 26 evaluable | 6-mo PFS by local review 25%; by central review 29%; OR at 12 wk 19% (5/26); median PFS 3.7 mo; median OS 7.7 mo; 12-mo OS 44% (larkin2024nilotinibinkitdriven pages 3-5, larkin2024nilotinibinkitdriven pages 5-6) | Mutations concentrated in exon 11 (69%), exon 13 (14%), exon 17 (14%), exon 9 (3%); OR at 12 wk: exon 11 16%, exon 13 25%, exon 17 67%; median PFS: exon 11 2.9 mo, exon 13 2.3 mo, exon 17 5.4 mo; L576 in 31% (larkin2024nilotinibinkitdriven pages 3-5, larkin2024nilotinibinkitdriven pages 5-6, larkin2024nilotinibinkitdriven pages 8-9) | Acral tumors had worse median PFS/OS than mucosal; ctDNA/FFPE concordance 100%; KIT copy number not clearly associated with outcome (larkin2024nilotinibinkitdriven pages 5-6, larkin2024nilotinibinkitdriven pages 6-8, larkin2024nilotinibinkitdriven pages 8-9) |
| Dasatinib — E2607 2017, *Cancer* | Locally advanced or stage IV mucosal, acral, vulvovaginal melanoma; stage I included KIT-mutant and KIT−; stage II restricted to KIT+ (kalinsky2017aphase2 pages 1-2) | 51 analyzable stage I; 22 analyzable stage II; 73 evaluable overall | Stage I PR 3/51 (5.9%); stage II PR 4/22 (18.2%); median response duration 4.2 mo; median PFS 2.1 mo; median OS 7.5 mo (kalinsky2017aphase2 pages 1-2, kalinsky2017aphase2 pages 4-5) | Among exon 11 and/or 13 KIT mutations, PR rate 20%; median PFS 4.7 mo; no responses with common L576P and K642E in one analysis, but responses seen with P577-D579 deletion and dual exon 11/13 mutations (kalinsky2017aphase2 pages 4-5, kalinsky2017aphase2 pages 7-8) | Exploratory analyses found no significant PFS/OS difference by overall KIT status; authors concluded response rate lower than expected and imatinib should remain KIT TKI of choice (kalinsky2017aphase2 pages 7-8, kalinsky2017aphase2 pages 1-2) |
| Ripretinib — Janku 2022, *ESMO Open* | KIT-altered metastatic melanoma phase I expansion; KIT mutation and/or amplification; heavily pretreated; starting dose 150 mg QD, BID escalation after progression allowed (janku2022efficacyandsafety pages 1-2, janku2022efficacyandsafety pages 2-3) | 26 | Confirmed ORR 23% (95% CI 9–44); among patients with follow-up imaging ORR 32% (8/25; CR 1, PR 7); median duration of confirmed response 9.1 mo; median PFS 7.3 mo (janku2022efficacyandsafety pages 5-6, janku2022efficacyandsafety pages 1-2, janku2022efficacyandsafety pages 3-4) | Confirmed ORR 44% in exon 11 and 18% in exon 17; median PFS 10.2 mo (exon 11) and 13.6 mo (exon 17); examples of responses include exon 11 L576P, exon 17 D820Y, exon 17 Y823D; D816V associated with PD in one case (janku2022efficacyandsafety pages 5-6, janku2022efficacyandsafety pages 4-5, janku2022efficacyandsafety pages 3-4) | KIT-inhibitor–naive patients had ORR 29% and mPFS 10.2 mo vs prior KIT inhibitor ORR 11% and mPFS 2.9 mo (janku2022efficacyandsafety pages 1-2, janku2022efficacyandsafety pages 4-5) |


*Table: This table summarizes key prospective clinical evidence for KIT-altered melanoma therapies across major studies of imatinib, nilotinib, dasatinib, and ripretinib. It highlights outcomes, genotype-response patterns, and practical caveats such as amplification-only disease and prior KIT inhibitor exposure.*

#### Imatinib (KIT TKI)
- **Guo et al., JCO 2011 (published Jul 2011):** ORR 23.3%, DCR 53.5%, median PFS 3.5 months; 9/10 PRs in exon 11 or 13 (guo2011phaseiiopenlabel pages 1-2).
- **Hodi et al., JCO 2013 (published Sep 2013):** BORR 29% overall; BORR 54% in KIT-mutated vs 0% in amplification-only tumors; median TTP 3.7 months; median OS 12.5 months (hodi2013imatinibformelanomas pages 1-2, hodi2013imatinibformelanomas pages 5-6).

#### Nilotinib (KIT TKI)
- **TEAM trial, Annals of Oncology 2017 (published Mar 2017):** ORR 26.2%, median response duration 7.1 months, median PFS 4.2 months, median OS 18.0 months; responses concentrated in exon 11 (guo2017efficacyandsafety pages 1-7, guo2017efficacyandsafety pages 7-12).
- **NICAM, Cell Reports Medicine 2024 (published Feb 2024):** OR at 12 weeks 19% (5/26), median PFS 3.7 months, median OS 7.7 months; mutations concentrated in exon 11 (69%); ctDNA ddPCR feasibility and 100% ctDNA–FFPE concordance reported (larkin2024nilotinibinkitdriven pages 3-5, larkin2024nilotinibinkitdriven pages 5-6, larkin2024nilotinibinkitdriven pages 6-8).
- **Carvajal et al., Clin Cancer Res 2015 (published May 2015):** post-imatinib setting; ORR 18.2% in the prior KIT-inhibitor cohort; limited activity in brain metastases cohort; median TTP 3.3 months; median OS 9.1 months (carvajal2015phaseiistudy pages 1-3).

#### Dasatinib (multi-kinase/SRC and KIT activity)
- **E2607 (Cancer 2017, published Jul 2017):** modest activity; median PFS 2.1 months, median OS 7.5 months; authors conclude low response rate and recommend imatinib remain KIT TKI of choice in unresectable KIT+ melanoma (kalinsky2017aphase2 pages 1-2).

#### Ripretinib (switch-control TKI; KIT/PDGFRA)
- **Janku et al., ESMO Open 2022 (published Aug 2022):** confirmed ORR 23% (95% CI 9–44) with median PFS 7.3 months and median response duration 9.1 months; activity differed by exon and prior KIT inhibitor exposure (KIT-inhibitor–naïve ORR 29% and mPFS 10.2 months vs prior KIT inhibitor ORR 11% and mPFS 2.9 months) (janku2022efficacyandsafety pages 1-2, janku2022efficacyandsafety pages 4-5).

### MAXO term suggestions (treatments/actions)
- **Tyrosine kinase inhibitor therapy** (MAXO: TKI treatment)
- **Molecular targeted therapy** (MAXO: targeted therapy)
- **Tumor mutation profiling / genomic sequencing** (MAXO: genetic test / tumor genomic profiling)
- **Liquid biopsy** (MAXO: liquid biopsy testing)

---

## 13. Prevention
No KIT-mutant-specific prevention strategies were identified in the retrieved sources. General melanoma prevention and early detection principles apply, but are not addressed in the accessed KIT-focused literature.

---

## 14. Other Species / Natural Disease
Not supported by the retrieved evidence set.

---

## 15. Model Organisms
The retrieved evidence set does not provide detailed descriptions of KIT-mutant melanoma animal models or engineered systems. (This is a gap for the current report.)

---

## Recent Developments (2023–2024 emphasis)

1. **2024 NICAM trial (nilotinib; metastatic mucosal/acral KIT-mutant melanoma)** provides updated prospective efficacy estimates (median PFS 3.7 months; OR at 12 weeks 19%) and highlights a clinically actionable diagnostic development: **plasma ddPCR ctDNA testing** with **100% concordance** to tumor calls in available matched samples (larkin2024nilotinibinkitdriven pages 3-5, larkin2024nilotinibinkitdriven pages 5-6, larkin2024nilotinibinkitdriven pages 6-8).
2. **2023 genomic synthesis** consolidates KIT mutation frequency ranges across melanoma subtypes, providing a practical expectation for testing yield by subtype (yang2023thegenomiclandscape pages 4-5, yang2023thegenomiclandscape media 3d8ffda1).

---

## Visual evidence (mutation frequency by subtype)
The figure below (Table 2 from a 2023 review) provides the subtype-specific KIT mutation frequencies used in the epidemiology section (yang2023thegenomiclandscape media 3d8ffda1).

---

## Key Statistics (quick reference)
- KIT mutation frequency: **UV-related ~1.8%**, **acral 10.9–24.4%**, **mucosal 19.1–23.1%** (yang2023thegenomiclandscape pages 4-5, yang2023thegenomiclandscape media 3d8ffda1).
- Imatinib (KIT-mutated vs amplification-only): **BORR 54% vs 0%** in a phase II trial enrolling mucosal/acral/CSD melanoma with KIT alterations (hodi2013imatinibformelanomas pages 1-2).
- Nilotinib (TEAM trial): **ORR 26.2%**, median **PFS 4.2 months**, median **OS 18.0 months** (guo2017efficacyandsafety pages 1-7).
- Ripretinib phase I expansion: **confirmed ORR 23%**, median **PFS 7.3 months**; KIT-inhibitor–naïve subgroup had higher ORR and longer PFS (janku2022efficacyandsafety pages 1-2).

---

## Limitations of this report
- Formal ontology identifiers (MONDO/MeSH/ICD-10/11) and comprehensive phenotype/quality-of-life metrics were not available in the retrieved corpus and would require dedicated searches in OMIM/Orphanet/MeSH/MONDO resources.
- Model-organism and non-human disease information for KIT-mutant melanoma was not captured in the currently retrieved sources.


References

1. (hodi2013imatinibformelanomas pages 1-2): F. Stephen Hodi, Christopher L. Corless, Anita Giobbie-Hurder, Jonathan A. Fletcher, Meijun Zhu, Adrian Marino-Enriquez, Philip Friedlander, Rene Gonzalez, Jeffrey S. Weber, Thomas F. Gajewski, Steven J. O'Day, Kevin B. Kim, Donald Lawrence, Keith T. Flaherty, Jason J. Luke, Frances A. Collichio, Marc S. Ernstoff, Michael C. Heinrich, Carol Beadling, Katherine A. Zukotynski, Jeffrey T. Yap, Annick D. Van den Abbeele, George D. Demetri, and David E. Fisher. Imatinib for melanomas harboring mutationally activated or amplified kit arising on mucosal, acral, and chronically sun-damaged skin. Journal of clinical oncology : official journal of the American Society of Clinical Oncology, 31 26:3182-90, Sep 2013. URL: https://doi.org/10.1200/jco.2012.47.7836, doi:10.1200/jco.2012.47.7836. This article has 769 citations.

2. (yang2023thegenomiclandscape pages 2-4): Ting-Ting Yang, Sebastian Yu, Chiao-Li Khale Ke, and Shih-Tsung Cheng. The genomic landscape of melanoma and its therapeutic implications. Genes, 14:1021, Apr 2023. URL: https://doi.org/10.3390/genes14051021, doi:10.3390/genes14051021. This article has 29 citations.

3. (larkin2024nilotinibinkitdriven pages 3-5): James Larkin, Richard Marais, Nuria Porta, David Gonzalez de Castro, Lisa Parsons, Christina Messiou, Gordon Stamp, Lisa Thompson, Kim Edmonds, Sarah Sarker, Jane Banerji, Paul Lorigan, Thomas R Jeffry Evans, Pippa Corrie, Ernest Marshall, Mark R Middleton, Paul Nathan, Steve Nicholson, Christian Ottensmeier, Ruth Plummer, Judith Bliss, Sara Valpione, and Samra Turajlic. Nilotinib in kit-driven advanced melanoma: results from the phase ii single-arm nicam trial. Cell Reports Medicine, Feb 2024. URL: https://doi.org/10.1016/j.xcrm.2024.101435, doi:10.1016/j.xcrm.2024.101435. This article has 21 citations and is from a peer-reviewed journal.

4. (guo2011phaseiiopenlabel pages 1-2): Jun Guo, Lu Si, Yan Kong, Keith T. Flaherty, Xiaowei Xu, Yanyan Zhu, Christopher L. Corless, Li Li, Haifu Li, Xinan Sheng, Chuanliang Cui, Zhihong Chi, Siming Li, Mei Han, Lili Mao, Xuede Lin, Nan Du, Xiaoshi Zhang, Junling Li, Baocheng Wang, and Shukui Qin. Phase ii, open-label, single-arm trial of imatinib mesylate in patients with metastatic melanoma harboring c-kit mutation or amplification. Journal of clinical oncology : official journal of the American Society of Clinical Oncology, 29 21:2904-9, Jul 2011. URL: https://doi.org/10.1200/jco.2010.33.9275, doi:10.1200/jco.2010.33.9275. This article has 919 citations.

5. (guo2017efficacyandsafety pages 1-7): Jun Guo, Richard D. Carvajal, Reinhard Dummer, A. Hauschild, A. Daud, Boris C. Bastian, S. Markovic, P. Queirolo, A. Arance, Carola Berking, V. Camargo, D. Herchenhorn, T. M. Petrella, D. Schadendorf, W. Sharfman, Alessandro Testori, S. Novick, S. Hertle, C. Nourry, Q. Chen, and F. Hodi. Efficacy and safety of nilotinib in patients with kit-mutated metastatic or inoperable melanoma: final results from the global, single-arm, phase ii team trial. Annals of Oncology, 28:1380-1387, Mar 2017. URL: https://doi.org/10.1093/annonc/mdx079, doi:10.1093/annonc/mdx079. This article has 212 citations and is from a highest quality peer-reviewed journal.

6. (cilloni2024detectionofkit pages 3-5): Daniela Cilloni, Beatrice Maffeo, Arianna Savi, Alice Costanza Danzero, Valentina Bonuomo, and Carmen Fava. Detection of kit mutations in systemic mastocytosis: how, when, and why. International Journal of Molecular Sciences, 25:10885, Oct 2024. URL: https://doi.org/10.3390/ijms252010885, doi:10.3390/ijms252010885. This article has 14 citations.

7. (abdellateif2023ckitreceptorsas pages 1-2): Mona S. Abdellateif, Ahmed Bayoumi, and Mohammed Aly Mohammed. C-kit receptors as a therapeutic target in cancer: current insights. OncoTargets and Therapy, 16:785-799, Sep 2023. URL: https://doi.org/10.2147/ott.s404648, doi:10.2147/ott.s404648. This article has 21 citations.

8. (jung2022clinicalandgenomic pages 1-2): Seungyeon Jung, Emma Armstrong, Alexander Z. Wei, Fei Ye, Aaron Lee, Matteo S. Carlino, Ryan J. Sullivan, Richard D. Carvajal, Alexander N. Shoushtari, and Douglas B. Johnson. Clinical and genomic correlates of imatinib response in melanomas with kit alterations. British Journal of Cancer, 127:1726-1732, Aug 2022. URL: https://doi.org/10.1038/s41416-022-01942-z, doi:10.1038/s41416-022-01942-z. This article has 27 citations and is from a domain leading peer-reviewed journal.

9. (jung2022clinicalandgenomic pages 4-5): Seungyeon Jung, Emma Armstrong, Alexander Z. Wei, Fei Ye, Aaron Lee, Matteo S. Carlino, Ryan J. Sullivan, Richard D. Carvajal, Alexander N. Shoushtari, and Douglas B. Johnson. Clinical and genomic correlates of imatinib response in melanomas with kit alterations. British Journal of Cancer, 127:1726-1732, Aug 2022. URL: https://doi.org/10.1038/s41416-022-01942-z, doi:10.1038/s41416-022-01942-z. This article has 27 citations and is from a domain leading peer-reviewed journal.

10. (larkin2024nilotinibinkitdriven pages 5-6): James Larkin, Richard Marais, Nuria Porta, David Gonzalez de Castro, Lisa Parsons, Christina Messiou, Gordon Stamp, Lisa Thompson, Kim Edmonds, Sarah Sarker, Jane Banerji, Paul Lorigan, Thomas R Jeffry Evans, Pippa Corrie, Ernest Marshall, Mark R Middleton, Paul Nathan, Steve Nicholson, Christian Ottensmeier, Ruth Plummer, Judith Bliss, Sara Valpione, and Samra Turajlic. Nilotinib in kit-driven advanced melanoma: results from the phase ii single-arm nicam trial. Cell Reports Medicine, Feb 2024. URL: https://doi.org/10.1016/j.xcrm.2024.101435, doi:10.1016/j.xcrm.2024.101435. This article has 21 citations and is from a peer-reviewed journal.

11. (yang2023thegenomiclandscape pages 4-5): Ting-Ting Yang, Sebastian Yu, Chiao-Li Khale Ke, and Shih-Tsung Cheng. The genomic landscape of melanoma and its therapeutic implications. Genes, 14:1021, Apr 2023. URL: https://doi.org/10.3390/genes14051021, doi:10.3390/genes14051021. This article has 29 citations.

12. (yang2023thegenomiclandscape media 3d8ffda1): Ting-Ting Yang, Sebastian Yu, Chiao-Li Khale Ke, and Shih-Tsung Cheng. The genomic landscape of melanoma and its therapeutic implications. Genes, 14:1021, Apr 2023. URL: https://doi.org/10.3390/genes14051021, doi:10.3390/genes14051021. This article has 29 citations.

13. (janku2022efficacyandsafety pages 3-4): F. Janku, S. Bauer, K. Shoumariyeh, R.L. Jones, A. Spreafico, J. Jennings, C. Psoinos, J. Meade, R. Ruiz-Soto, and P. Chi. Efficacy and safety of ripretinib in patients with kit-altered metastatic melanoma. ESMO Open, 7:100520, Aug 2022. URL: https://doi.org/10.1016/j.esmoop.2022.100520, doi:10.1016/j.esmoop.2022.100520. This article has 18 citations and is from a domain leading peer-reviewed journal.

14. (janku2022efficacyandsafety pages 1-2): F. Janku, S. Bauer, K. Shoumariyeh, R.L. Jones, A. Spreafico, J. Jennings, C. Psoinos, J. Meade, R. Ruiz-Soto, and P. Chi. Efficacy and safety of ripretinib in patients with kit-altered metastatic melanoma. ESMO Open, 7:100520, Aug 2022. URL: https://doi.org/10.1016/j.esmoop.2022.100520, doi:10.1016/j.esmoop.2022.100520. This article has 18 citations and is from a domain leading peer-reviewed journal.

15. (janku2022efficacyandsafety pages 4-5): F. Janku, S. Bauer, K. Shoumariyeh, R.L. Jones, A. Spreafico, J. Jennings, C. Psoinos, J. Meade, R. Ruiz-Soto, and P. Chi. Efficacy and safety of ripretinib in patients with kit-altered metastatic melanoma. ESMO Open, 7:100520, Aug 2022. URL: https://doi.org/10.1016/j.esmoop.2022.100520, doi:10.1016/j.esmoop.2022.100520. This article has 18 citations and is from a domain leading peer-reviewed journal.

16. (hodi2013imatinibformelanomas pages 5-6): F. Stephen Hodi, Christopher L. Corless, Anita Giobbie-Hurder, Jonathan A. Fletcher, Meijun Zhu, Adrian Marino-Enriquez, Philip Friedlander, Rene Gonzalez, Jeffrey S. Weber, Thomas F. Gajewski, Steven J. O'Day, Kevin B. Kim, Donald Lawrence, Keith T. Flaherty, Jason J. Luke, Frances A. Collichio, Marc S. Ernstoff, Michael C. Heinrich, Carol Beadling, Katherine A. Zukotynski, Jeffrey T. Yap, Annick D. Van den Abbeele, George D. Demetri, and David E. Fisher. Imatinib for melanomas harboring mutationally activated or amplified kit arising on mucosal, acral, and chronically sun-damaged skin. Journal of clinical oncology : official journal of the American Society of Clinical Oncology, 31 26:3182-90, Sep 2013. URL: https://doi.org/10.1200/jco.2012.47.7836, doi:10.1200/jco.2012.47.7836. This article has 769 citations.

17. (larkin2024nilotinibinkitdriven pages 14-15): James Larkin, Richard Marais, Nuria Porta, David Gonzalez de Castro, Lisa Parsons, Christina Messiou, Gordon Stamp, Lisa Thompson, Kim Edmonds, Sarah Sarker, Jane Banerji, Paul Lorigan, Thomas R Jeffry Evans, Pippa Corrie, Ernest Marshall, Mark R Middleton, Paul Nathan, Steve Nicholson, Christian Ottensmeier, Ruth Plummer, Judith Bliss, Sara Valpione, and Samra Turajlic. Nilotinib in kit-driven advanced melanoma: results from the phase ii single-arm nicam trial. Cell Reports Medicine, Feb 2024. URL: https://doi.org/10.1016/j.xcrm.2024.101435, doi:10.1016/j.xcrm.2024.101435. This article has 21 citations and is from a peer-reviewed journal.

18. (larkin2024nilotinibinkitdriven pages 6-8): James Larkin, Richard Marais, Nuria Porta, David Gonzalez de Castro, Lisa Parsons, Christina Messiou, Gordon Stamp, Lisa Thompson, Kim Edmonds, Sarah Sarker, Jane Banerji, Paul Lorigan, Thomas R Jeffry Evans, Pippa Corrie, Ernest Marshall, Mark R Middleton, Paul Nathan, Steve Nicholson, Christian Ottensmeier, Ruth Plummer, Judith Bliss, Sara Valpione, and Samra Turajlic. Nilotinib in kit-driven advanced melanoma: results from the phase ii single-arm nicam trial. Cell Reports Medicine, Feb 2024. URL: https://doi.org/10.1016/j.xcrm.2024.101435, doi:10.1016/j.xcrm.2024.101435. This article has 21 citations and is from a peer-reviewed journal.

19. (larkin2024nilotinibinkitdriven pages 9-10): James Larkin, Richard Marais, Nuria Porta, David Gonzalez de Castro, Lisa Parsons, Christina Messiou, Gordon Stamp, Lisa Thompson, Kim Edmonds, Sarah Sarker, Jane Banerji, Paul Lorigan, Thomas R Jeffry Evans, Pippa Corrie, Ernest Marshall, Mark R Middleton, Paul Nathan, Steve Nicholson, Christian Ottensmeier, Ruth Plummer, Judith Bliss, Sara Valpione, and Samra Turajlic. Nilotinib in kit-driven advanced melanoma: results from the phase ii single-arm nicam trial. Cell Reports Medicine, Feb 2024. URL: https://doi.org/10.1016/j.xcrm.2024.101435, doi:10.1016/j.xcrm.2024.101435. This article has 21 citations and is from a peer-reviewed journal.

20. (hodi2013imatinibformelanomas pages 3-4): F. Stephen Hodi, Christopher L. Corless, Anita Giobbie-Hurder, Jonathan A. Fletcher, Meijun Zhu, Adrian Marino-Enriquez, Philip Friedlander, Rene Gonzalez, Jeffrey S. Weber, Thomas F. Gajewski, Steven J. O'Day, Kevin B. Kim, Donald Lawrence, Keith T. Flaherty, Jason J. Luke, Frances A. Collichio, Marc S. Ernstoff, Michael C. Heinrich, Carol Beadling, Katherine A. Zukotynski, Jeffrey T. Yap, Annick D. Van den Abbeele, George D. Demetri, and David E. Fisher. Imatinib for melanomas harboring mutationally activated or amplified kit arising on mucosal, acral, and chronically sun-damaged skin. Journal of clinical oncology : official journal of the American Society of Clinical Oncology, 31 26:3182-90, Sep 2013. URL: https://doi.org/10.1200/jco.2012.47.7836, doi:10.1200/jco.2012.47.7836. This article has 769 citations.

21. (carvajal2015phaseiistudy pages 1-3): Richard D. Carvajal, Donald P. Lawrence, Jeffrey S. Weber, Thomas F. Gajewski, Rene Gonzalez, Jose Lutzky, Steven J. O'Day, Omid Hamid, Jedd D. Wolchok, Paul B. Chapman, Ryan J. Sullivan, Jerrold B. Teitcher, Nikhil Ramaiya, Anita Giobbie-Hurder, Cristina R. Antonescu, Michael C. Heinrich, Boris C. Bastian, Christopher L. Corless, Jonathan A. Fletcher, and F. Stephen Hodi. Phase ii study of nilotinib in melanoma harboring kit alterations following progression to prior kit inhibition. Clinical Cancer Research, 21:2289-2296, May 2015. URL: https://doi.org/10.1158/1078-0432.ccr-14-1630, doi:10.1158/1078-0432.ccr-14-1630. This article has 187 citations and is from a highest quality peer-reviewed journal.

22. (guo2017efficacyandsafety pages 7-12): Jun Guo, Richard D. Carvajal, Reinhard Dummer, A. Hauschild, A. Daud, Boris C. Bastian, S. Markovic, P. Queirolo, A. Arance, Carola Berking, V. Camargo, D. Herchenhorn, T. M. Petrella, D. Schadendorf, W. Sharfman, Alessandro Testori, S. Novick, S. Hertle, C. Nourry, Q. Chen, and F. Hodi. Efficacy and safety of nilotinib in patients with kit-mutated metastatic or inoperable melanoma: final results from the global, single-arm, phase ii team trial. Annals of Oncology, 28:1380-1387, Mar 2017. URL: https://doi.org/10.1093/annonc/mdx079, doi:10.1093/annonc/mdx079. This article has 212 citations and is from a highest quality peer-reviewed journal.

23. (larkin2024nilotinibinkitdriven pages 1-3): James Larkin, Richard Marais, Nuria Porta, David Gonzalez de Castro, Lisa Parsons, Christina Messiou, Gordon Stamp, Lisa Thompson, Kim Edmonds, Sarah Sarker, Jane Banerji, Paul Lorigan, Thomas R Jeffry Evans, Pippa Corrie, Ernest Marshall, Mark R Middleton, Paul Nathan, Steve Nicholson, Christian Ottensmeier, Ruth Plummer, Judith Bliss, Sara Valpione, and Samra Turajlic. Nilotinib in kit-driven advanced melanoma: results from the phase ii single-arm nicam trial. Cell Reports Medicine, Feb 2024. URL: https://doi.org/10.1016/j.xcrm.2024.101435, doi:10.1016/j.xcrm.2024.101435. This article has 21 citations and is from a peer-reviewed journal.

24. (larkin2024nilotinibinkitdriven pages 8-9): James Larkin, Richard Marais, Nuria Porta, David Gonzalez de Castro, Lisa Parsons, Christina Messiou, Gordon Stamp, Lisa Thompson, Kim Edmonds, Sarah Sarker, Jane Banerji, Paul Lorigan, Thomas R Jeffry Evans, Pippa Corrie, Ernest Marshall, Mark R Middleton, Paul Nathan, Steve Nicholson, Christian Ottensmeier, Ruth Plummer, Judith Bliss, Sara Valpione, and Samra Turajlic. Nilotinib in kit-driven advanced melanoma: results from the phase ii single-arm nicam trial. Cell Reports Medicine, Feb 2024. URL: https://doi.org/10.1016/j.xcrm.2024.101435, doi:10.1016/j.xcrm.2024.101435. This article has 21 citations and is from a peer-reviewed journal.

25. (kalinsky2017aphase2 pages 1-2): Kevin Kalinsky, Sandra Lee, Krista M. Rubin, Donald P. Lawrence, Anthony J. Iafrarte, Darell R. Borger, Kim A. Margolin, Mario M. Leitao, Ahmad A. Tarhini, Henry B. Koon, Andrew L. Pecora, Anthony J. Jaslowski, Gary I. Cohen, Timothy M. Kuzel, Christopher D. Lao, and John M. Kirkwood. A phase 2 trial of dasatinib in patients with locally advanced or stage iv mucosal, acral, or vulvovaginal melanoma: a trial of the ecog‐acrin cancer research group (e2607). Cancer, 123:2688-2697, Jul 2017. URL: https://doi.org/10.1002/cncr.30663, doi:10.1002/cncr.30663. This article has 137 citations and is from a domain leading peer-reviewed journal.

26. (kalinsky2017aphase2 pages 4-5): Kevin Kalinsky, Sandra Lee, Krista M. Rubin, Donald P. Lawrence, Anthony J. Iafrarte, Darell R. Borger, Kim A. Margolin, Mario M. Leitao, Ahmad A. Tarhini, Henry B. Koon, Andrew L. Pecora, Anthony J. Jaslowski, Gary I. Cohen, Timothy M. Kuzel, Christopher D. Lao, and John M. Kirkwood. A phase 2 trial of dasatinib in patients with locally advanced or stage iv mucosal, acral, or vulvovaginal melanoma: a trial of the ecog‐acrin cancer research group (e2607). Cancer, 123:2688-2697, Jul 2017. URL: https://doi.org/10.1002/cncr.30663, doi:10.1002/cncr.30663. This article has 137 citations and is from a domain leading peer-reviewed journal.

27. (kalinsky2017aphase2 pages 7-8): Kevin Kalinsky, Sandra Lee, Krista M. Rubin, Donald P. Lawrence, Anthony J. Iafrarte, Darell R. Borger, Kim A. Margolin, Mario M. Leitao, Ahmad A. Tarhini, Henry B. Koon, Andrew L. Pecora, Anthony J. Jaslowski, Gary I. Cohen, Timothy M. Kuzel, Christopher D. Lao, and John M. Kirkwood. A phase 2 trial of dasatinib in patients with locally advanced or stage iv mucosal, acral, or vulvovaginal melanoma: a trial of the ecog‐acrin cancer research group (e2607). Cancer, 123:2688-2697, Jul 2017. URL: https://doi.org/10.1002/cncr.30663, doi:10.1002/cncr.30663. This article has 137 citations and is from a domain leading peer-reviewed journal.

28. (janku2022efficacyandsafety pages 2-3): F. Janku, S. Bauer, K. Shoumariyeh, R.L. Jones, A. Spreafico, J. Jennings, C. Psoinos, J. Meade, R. Ruiz-Soto, and P. Chi. Efficacy and safety of ripretinib in patients with kit-altered metastatic melanoma. ESMO Open, 7:100520, Aug 2022. URL: https://doi.org/10.1016/j.esmoop.2022.100520, doi:10.1016/j.esmoop.2022.100520. This article has 18 citations and is from a domain leading peer-reviewed journal.

29. (janku2022efficacyandsafety pages 5-6): F. Janku, S. Bauer, K. Shoumariyeh, R.L. Jones, A. Spreafico, J. Jennings, C. Psoinos, J. Meade, R. Ruiz-Soto, and P. Chi. Efficacy and safety of ripretinib in patients with kit-altered metastatic melanoma. ESMO Open, 7:100520, Aug 2022. URL: https://doi.org/10.1016/j.esmoop.2022.100520, doi:10.1016/j.esmoop.2022.100520. This article has 18 citations and is from a domain leading peer-reviewed journal.
