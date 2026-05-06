---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-05T23:14:06.451693'
end_time: '2026-05-05T23:25:05.911807'
duration_seconds: 659.46
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Idiopathic Spontaneous Coronary Artery Dissection
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 32
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Idiopathic Spontaneous Coronary Artery Dissection
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Idiopathic Spontaneous Coronary Artery Dissection** covering all of the
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
- **Disease Name:** Idiopathic Spontaneous Coronary Artery Dissection
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Idiopathic Spontaneous Coronary Artery Dissection** covering all of the
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


# Idiopathic Spontaneous Coronary Artery Dissection (SCAD): Disease Characteristics Research Report

## Executive summary
Idiopathic spontaneous coronary artery dissection (SCAD) is a non-atherosclerotic cause of acute coronary syndrome (ACS) caused by separation within the coronary arterial wall that produces an intramural hematoma and/or intimal tear, compressing the true lumen and causing myocardial ischemia/infarction. Contemporary evidence supports conservative-first management for clinically stable patients due to high spontaneous healing rates, with selective revascularization for high-risk anatomy or ongoing ischemia; systematic screening for extracoronary arteriopathies—especially fibromuscular dysplasia (FMD)—is commonly recommended. Despite rapidly growing registry-based knowledge, randomized controlled trial (RCT) evidence remains limited, and many recommendations are based on expert consensus and observational studies. (morena2024advancesinthe pages 1-2, dang2024spontaneouscoronaryartery pages 6-6, smirnova2023spontaneouscoronaryartery pages 1-2, petrovic2024managementandoutcomes pages 1-2)

## 1. Disease information
### 1.1 Definition and overview
SCAD is described as a non-atherosclerotic, non-traumatic, non-iatrogenic separation of the coronary arterial wall resulting in a false lumen and/or intramural hematoma that compresses the true lumen and presents as ACS. (morena2024advancesinthe pages 1-2, smirnova2023spontaneouscoronaryartery pages 1-2, pender2025spontaneouscoronaryartery pages 1-2)

**Abstract-supported quotes**
- “SCAD is caused by separation occurring within or between any of the three tunics of the coronary artery wall. This leads to intramural hematoma and/or formation of false lumen in the artery, which leads to ischemic changes or infarction of the myocardium.” (Frontiers review abstract) (dang2024spontaneouscoronaryartery pages 6-7)
- “Spontaneous coronary artery dissection (SCAD) is a non-traumatic and non-iatrogenic separation of the coronary arterial wall.” (systematic review/meta-analysis abstract) (apostolovic2024spontaneouscoronaryartery pages 1-2)

### 1.2 Key identifiers (from retrieved evidence)
- **ICD-10-CM:** **I25.42** used to identify SCAD in U.S. administrative datasets. (mughal2022contemporarytrendsin pages 1-3, krittanawong2020recurrentspontaneouscoronary pages 1-2)
- **ICD-9-CM:** **414.12** used to identify SCAD before the ICD-10 transition. (mughal2022contemporarytrendsin pages 1-3, krittanawong2020recurrentspontaneouscoronary pages 1-2)

**Not confirmed in retrieved full texts:** MeSH term(s), MONDO ID, Orphanet ID, OMIM entry specifically for “idiopathic SCAD” (these identifiers exist in external ontologies but are not present in the retrieved documents and are not inferred here). (mughal2022contemporarytrendsin pages 1-3, krittanawong2020recurrentspontaneouscoronary pages 1-2)

### 1.3 Synonyms / alternative names
- Spontaneous coronary artery dissection (SCAD) (morena2024advancesinthe pages 1-2)
- Non-atherosclerotic coronary artery dissection / non-iatrogenic coronary artery dissection (descriptive usage across reviews) (smirnova2023spontaneouscoronaryartery pages 1-2, pender2025spontaneouscoronaryartery pages 1-2)

### 1.4 Evidence provenance
The current understanding summarized here is derived largely from **aggregated disease-level evidence**: systematic reviews/meta-analyses, narrative reviews, and registry/administrative cohort analyses, with some mechanistic inference from intracoronary imaging and pathology discussions. (dang2024spontaneouscoronaryartery pages 6-6, petrovic2024managementandoutcomes pages 1-2)

## 2. Etiology
### 2.1 Disease causal factors (current mechanistic framing)
SCAD is thought to arise via two nonexclusive mechanisms:
1) **“Inside–out”**: an intimal tear allows blood to enter the arterial wall, forming a false lumen.
2) **“Outside–in”**: spontaneous hemorrhage (e.g., from vasa vasorum) causes intramural hematoma within the media, compressing the lumen. (rusali2025spontaneouscoronaryartery pages 3-5, pender2025spontaneouscoronaryartery pages 1-2)

### 2.2 Risk factors
#### Predisposing conditions (non-exhaustive)
- **Fibromuscular dysplasia (FMD)**: the most consistently associated extracoronary arteriopathy; prevalence among SCAD patients varies widely (in part due to screening modality/intensity). (dang2024spontaneouscoronaryartery pages 6-6, gori2023contemporaryreviewon pages 3-4)
- **Pregnancy/peripartum state** (pregnancy-associated SCAD often more severe). (smirnova2023spontaneouscoronaryartery pages 1-2, gori2023contemporaryreviewon pages 3-4, apostolovic2024spontaneouscoronaryartery pages 1-2)
- **Inherited connective tissue disorders** (rare; often in syndromic/non-syndromic connective tissue disease contexts). (smirnova2023spontaneouscoronaryartery pages 1-2, gori2023contemporaryreviewon pages 3-4)
- **Hypertension** (frequent “traditional” risk factor reported in multiple reviews). (gori2023contemporaryreviewon pages 3-4)
- **Migraine** and other neuropsychiatric conditions are reported in SCAD cohorts and may associate with recurrence risk. (dang2024spontaneouscoronaryartery pages 6-6, krittanawong2020recurrentspontaneouscoronary pages 1-2)

#### Precipitating triggers
Reviews report that **emotional stress** (more often in women) and **physical stress/exertion** (more often in men) commonly precede symptoms; stimulant exposure (e.g., cocaine/amphetamines) is also discussed as a precipitating factor in risk-factor reviews. (gori2023contemporaryreviewon pages 3-4)

### 2.3 Protective factors
No specific protective genetic variants or protective exposures were identified in the retrieved evidence set.

### 2.4 Gene–environment interactions
The retrieved evidence supports a conceptual model of **arterial vulnerability (predisposition) + trigger (stress/hemodynamic/hormonal changes)** but does not provide quantified gene–environment interaction estimates. (rusali2025spontaneouscoronaryartery pages 3-5, gori2023contemporaryreviewon pages 3-4)

## 3. Phenotypes
### 3.1 Clinical presentation
SCAD most commonly presents as ACS with chest pain and biomarker/ECG changes consistent with MI.

**Abstract-supported quote**
- “Spontaneous coronary artery dissection (SCAD) represents a quite rare event but with potentially serious prognostic implications. Meanwhile, SCAD typically presents as an acute coronary syndrome (ACS).” (review abstract) (morena2024advancesinthe pages 1-2)

#### Frequencies / ranges reported in recent syntheses
- Systematic review (n=1,801): **NSTEMI ~48.5%**, **STEMI ~36.8%**, unstable angina ~3.4%, stable angina ~0.56%. (petrovic2024managementandoutcomes pages 1-2)
- In women of reproductive age meta-analysis (n=2,145): **STEMI ~47.4%** (pooled). (apostolovic2024spontaneouscoronaryartery pages 1-2)

#### Complications/severe presentations (examples)
A 2023 review reports cardiogenic shock (~2%), sudden cardiac death (~0.8% in autopsy series), and ventricular arrhythmias (~5%) among reported presentations/complications, and notes Takotsubo syndrome overlap. (smirnova2023spontaneouscoronaryartery pages 1-2)

### 3.2 Quality-of-life impacts
Post-event psychological morbidity is common; a 2024 narrative review highlights depression/anxiety/PTSD and recommends mental-health screening and peer support as part of follow-up care. (dang2024spontaneouscoronaryartery pages 6-6)

### 3.3 Suggested HPO terms (for knowledge base entry; not exhaustive)
- Chest pain **HP:0100749**
- Acute myocardial infarction **HP:0001658**
- ST elevation **HP:0031557** / Abnormal ST segment **HP:0031425**
- Elevated cardiac troponin **HP:0031195**
- Ventricular arrhythmia **HP:0001663**
- Cardiogenic shock **HP:0030144**
- Dyspnea **HP:0002094**
- Nausea **HP:0002018**

(These HPO codes are provided as ontology suggestions; they were not explicitly enumerated in the retrieved articles.)

## 4. Genetic / molecular information
### 4.1 Current understanding
SCAD is generally **not strongly inherited**; familial cases are uncommon in the reviewed literature, and monogenic causes are considered rare and more often linked to connective tissue disorders. (gori2023contemporaryreviewon pages 3-4, smirnova2023spontaneouscoronaryartery pages 1-2)

A 2024 narrative review discusses reported genetic associations/case reports including **PHACTR1/EDN1 locus**, **SMAD3 mutation** cases, and variants in fibrillar collagens; however, the excerpted evidence does not provide a comprehensive gene list or variant-level frequencies. (dang2024spontaneouscoronaryartery pages 6-7)

### 4.2 When to consider genetic testing (practice-oriented guidance)
Genetic testing is described as **low-yield and not routine**, but may be considered in SCAD patients with recurrent SCAD, multivessel disease, extracoronary vascular abnormalities, or a family history/features suggestive of a heritable connective tissue disorder, with appropriate counselling and possible aortopathy/connective tissue gene panels. (dang2024spontaneouscoronaryartery pages 6-6)

### 4.3 Variants/modifier genes/epigenetics/chromosomal abnormalities
The retrieved evidence does not provide curated variant-level data (e.g., ACMG classifications, allele frequencies) or epigenetic/chromosomal abnormality findings specific to idiopathic SCAD.

## 5. Environmental information
### 5.1 Environmental/lifestyle factors
The evidence set primarily emphasizes **stress-related triggers** (emotional/physical) rather than classic lifestyle risk factors; traditional atherosclerotic risk factors are often less prevalent, though hypertension is frequently reported. (gori2023contemporaryreviewon pages 3-4)

### 5.2 Infectious agents
No specific infectious agent etiology was identified in the retrieved evidence.

## 6. Mechanism / pathophysiology
### 6.1 Causal chain (high-level)
**Predisposing arteriopathy/hormonal milieu/stress exposure** → **arterial wall vulnerability** → **intramural bleeding and/or intimal disruption** → **intramural hematoma/false lumen** → **true-lumen compression** → **myocardial ischemia/infarction** → **ACS presentation and complications**. (rusali2025spontaneouscoronaryartery pages 3-5, pender2025spontaneouscoronaryartery pages 1-2, smirnova2023spontaneouscoronaryartery pages 1-2)

### 6.2 Cellular processes and tissue injury (conceptual mapping)
- Vessel wall injury leading to intramural hematoma with downstream ischemia is central to SCAD pathophysiology. (rusali2025spontaneouscoronaryartery pages 3-5, pender2025spontaneouscoronaryartery pages 1-2)

### 6.3 Suggested GO (biological process) and CL (cell type) terms (ontology suggestions)
- GO:0001525 **angiogenesis** (vasa vasorum biology; conceptual)
- GO:0007596 **blood coagulation** (intramural hemorrhage context; conceptual)
- GO:0006954 **inflammatory response** (discussed as unclear/variable in reviews; conceptual) (rusali2025spontaneouscoronaryartery pages 3-5)
- CL:0002131 **vascular smooth muscle cell**
- CL:0002543 **endothelial cell**

(These are ontology suggestions; the retrieved evidence does not provide explicit GO/CL annotations.)

## 7. Anatomical structures affected
### 7.1 Primary structures
- **Coronary arteries** (often LAD as culprit). (petrovic2024managementandoutcomes pages 1-2, apostolovic2024spontaneouscoronaryartery pages 1-2)

### 7.2 Secondary involvement/complications
- **Myocardium** (ischemia/infarction); potential for heart failure, arrhythmias, cardiogenic shock. (smirnova2023spontaneouscoronaryartery pages 1-2, petrovic2024managementandoutcomes pages 1-2)

### 7.3 Suggested UBERON terms (ontology suggestions)
- Coronary artery **UBERON:0001621**
- Left anterior descending coronary artery (LAD) (UBERON term varies by subset; provide as “LAD coronary artery” mapping in your implementation)
- Myocardium **UBERON:0002349**

## 8. Diagnostics
### 8.1 Imaging and diagnostic approach
- **Invasive coronary angiography (ICA)** is emphasized as the diagnostic gold standard, with adjunctive intracoronary imaging (**IVUS/OCT**) improving diagnostic performance and clarifying mechanism. (morena2024advancesinthe pages 1-2, bollati2024spontaneouscoronarydissection pages 4-7)
- **Extracoronary vascular imaging**: head-to-pelvis CT angiography is described as a method for FMD screening; MRA is an alternative but may have lower spatial resolution. (dang2024spontaneouscoronaryartery pages 6-6)

### 8.2 Angiographic classification (Saw types)
Recent reviews describe an ICA-based SCAD classification (Types 1–4) used in practice; Table/Figure evidence is available from a 2024 review, including examples of Types 1, 2A, 3, and 4 and management flow-chart context. (bollati2024spontaneouscoronarydissection pages 4-7, bollati2024spontaneouscoronarydissection media ffbb95a5, bollati2024spontaneouscoronarydissection media 8d0f25c2, bollati2024spontaneouscoronarydissection media 8c541a8a, bollati2024spontaneouscoronarydissection media 353fb04a, bollati2024spontaneouscoronarydissection media 94fd0b42, bollati2024spontaneouscoronarydissection media df824cb3)

### 8.3 Differential diagnosis
SCAD can mimic atherosclerotic ACS and requires careful angiographic interpretation; intracoronary imaging can help in ambiguous cases. (gori2023contemporaryreviewon pages 3-4)

## 9. Treatment
### 9.1 Acute management strategy (current practice pattern)
- **Conservative management is preferred** in clinically stable SCAD because spontaneous healing is common, while PCI success is limited by technical challenges and risks of propagation/iatrogenic dissection. (bollati2024spontaneouscoronarydissection pages 4-7, petrovic2024managementandoutcomes pages 1-2)
- **Revascularization (PCI; CABG rarely)** is reserved for high-risk presentations (e.g., left main/proximal multivessel, TIMI 0/1 flow, hemodynamic/electrical instability, ongoing ischemia). (bollati2024spontaneouscoronarydissection pages 4-7, bollati2024spontaneouscoronarydissection pages 7-8)

### 9.2 Medical therapy themes
- Beta-blockers are commonly used; observational evidence associates beta-blockers with lower recurrence. (dang2024spontaneouscoronaryartery pages 6-6)
- ACE inhibitor/ARB is recommended when LVEF is reduced after SCAD-related ACS. (dang2024spontaneouscoronaryartery pages 6-6)
- Antiplatelet strategy in conservatively managed SCAD remains debated in reviews due to concern about intramural hematoma expansion; practice varies and RCT data are limited. (morena2024advancesinthe pages 1-2, bollati2024spontaneouscoronarydissection pages 4-7)
- Statins are generally not routine unless indicated for dyslipidemia/atherosclerotic disease. (smirnova2023spontaneouscoronaryartery pages 1-2)

### 9.3 Cardiac rehabilitation and psychosocial care
Cardiac rehabilitation is described as safe and recommended for SCAD patients; low/moderate-intensity aerobic and low-resistance programs are favored, along with avoidance of high-intensity abrupt-movement activities, and psychological screening/support is emphasized. (dang2024spontaneouscoronaryartery pages 6-6)

### 9.4 Current clinical trials (real-world implementations of evidence generation)
- **NCT04850417**: “Randomized Study of Beta-Blockers and Antiplatelets in Patients With Spontaneous Coronary Artery Dissection” (Phase 4; planned enrollment 600; Spanish Society of Cardiology). (clinical trial record) (dang2024spontaneouscoronaryartery pages 6-6)
- **NCT06955663**: Exercise support/rehabilitation after SCAD (planned enrollment 120). (dang2024spontaneouscoronaryartery pages 6-6)
- **NCT04251039**: RESPONSE observational study in SCAD patients undergoing complex PCI. (dang2024spontaneouscoronaryartery pages 6-6)

### 9.5 Suggested MAXO terms (ontology suggestions)
- Conservative management / medical management (MAXO “medical therapy” class; implement with local MAXO mapping)
- Percutaneous coronary intervention **PCI**
- Coronary artery bypass grafting **CABG**
- Cardiac rehabilitation
- CT angiography screening for extracoronary arteriopathy

## 10. Prevention
### 10.1 Primary prevention
No established primary prevention is supported by RCT evidence in the retrieved set; prevention is largely framed as managing predispositions (e.g., blood pressure), avoiding extreme triggers, and individualized counselling. (dang2024spontaneouscoronaryartery pages 6-6, gori2023contemporaryreviewon pages 3-4)

### 10.2 Secondary/tertiary prevention
- **Recurrence risk mitigation**: beta-blockers are associated with lower recurrence in observational data and are commonly used; follow-up and monitoring are emphasized. (dang2024spontaneouscoronaryartery pages 6-6)
- **Screening for FMD and other extracoronary vascular abnormalities** is commonly recommended; FMD is associated with higher recurrence risk in review-level evidence. (dang2024spontaneouscoronaryartery pages 6-6)

## 11. Outcomes / prognosis
### 11.1 Mortality and major adverse cardiovascular events
A 2024 systematic review (13 observational studies, n=1,801) reported **in-hospital mortality ~1.2%** and **follow-up mortality ~1.3%**, with MACE including recurrent SCAD up to 31% across studies and other events (ACS, target vessel revascularization, HF, stroke) reported variably. (petrovic2024managementandoutcomes pages 1-2)

A 2024 meta-analysis in reproductive-age women reported pooled **recurrent SCAD ~15.2%** (95% CI 9.1–21.3). (apostolovic2024spontaneouscoronaryartery pages 1-2)

### 11.2 Recurrence and prognostic factors
- Reviews report recurrence risk persists for years and may vary widely depending on definitions and cohorts; recurrence has been reported up to ~30% historically, with more recent prospective series reporting lower values in certain follow-up windows. (smirnova2023spontaneouscoronaryartery pages 1-2)
- FMD is linked to higher recurrence risk (RR 2.02 in review summary). (dang2024spontaneouscoronaryartery pages 6-6)

## 12. Temporal development
### 12.1 Onset
SCAD often occurs in younger to middle-aged adults, with strong female predominance and particular relevance in peripartum settings. (smirnova2023spontaneouscoronaryartery pages 1-2, apostolovic2024spontaneouscoronaryartery pages 1-2)

### 12.2 Course
- Early in-hospital period: risk of early extension/worsening in the first days is noted in reviews (reported ~5–10% in one review summary). (bollati2024spontaneouscoronarydissection pages 4-7)
- Longer term: recurrence risk and chronic symptoms (e.g., persistent chest pain syndromes discussed in later reviews) can require ongoing follow-up care. (rusali2025spontaneouscoronaryartery pages 14-16)

## 13. Inheritance and population
### 13.1 Epidemiology
- SCAD is commonly cited as accounting for ~1–4% of ACS. (gori2023contemporaryreviewon pages 3-4)
- Administrative incidence trend analysis (U.S. National Inpatient Sample) reported rising crude incidence per 1,000,000 discharges from ~4.95 (2010) to ~14.81 (2017), identified using ICD-9/10 SCAD codes. (mughal2022contemporarytrendsin pages 1-3)

### 13.2 Demographics
- Female predominance is consistently reported; many reviews cite ~80–90% of cases in women. (gori2023contemporaryreviewon pages 3-4, petrovic2024managementandoutcomes pages 1-2)

### 13.3 Inheritance pattern
The evidence supports **mostly complex/polygenic susceptibility with rare monogenic syndromic cases**, rather than a single Mendelian inheritance pattern for idiopathic SCAD. (smirnova2023spontaneouscoronaryartery pages 1-2, gori2023contemporaryreviewon pages 3-4)

## 14. Other species / natural disease
No evidence for naturally occurring SCAD as a defined veterinary disease entity was identified in the retrieved materials.

## 15. Model organisms
No SCAD-specific validated animal model descriptions were found in the retrieved evidence excerpts; current literature in this evidence set emphasizes human imaging/registry studies and connective-tissue disease genetics rather than experimental organism models. (dang2024spontaneouscoronaryartery pages 6-6, petrovic2024managementandoutcomes pages 1-2)

## Visual evidence (angiographic types and management algorithm)
The following extracted visuals provide practical depictions of SCAD angiographic types and a management flow chart from a 2024 review; they can be used to support knowledge base UI elements and clinician-facing summaries. (bollati2024spontaneouscoronarydissection media ffbb95a5, bollati2024spontaneouscoronarydissection media 8d0f25c2, bollati2024spontaneouscoronarydissection media df824cb3)

## Structured evidence table
| Domain | Compact summary | Key figures / structured items |
|---|---|---|
| Definition & epidemiology | SCAD is a **non-atherosclerotic, non-traumatic, non-iatrogenic** separation of the coronary arterial wall causing **intramural hematoma and/or intimal tear**, compression of the true lumen, myocardial ischemia, and ACS. It is increasingly recognized but still underdiagnosed. Women predominate, typically younger to middle-aged and often without classic atherosclerotic risk factors. (morena2024advancesinthe pages 1-2, singulane2025spontaneouscoronaryartery pages 1-2, smirnova2023spontaneouscoronaryartery pages 1-2, pender2025spontaneouscoronaryartery pages 1-2) | **ACS contribution:** ~1–4% overall; ~22–43% of AMI/ACS in younger women depending on cohort/age definition; up to ~35% of MI/ACS in women <50 in some summaries. **Sex:** ~88–91% female. **Typical age:** mean ~49–50 years; reviews cite onset often 44–55 years. **Culprit vessel:** LAD most common (~50–51%). (morena2024advancesinthe pages 1-2, smirnova2023spontaneouscoronaryartery pages 1-2, mughal2022contemporarytrendsin pages 1-3, krittanawong2020recurrentspontaneouscoronary pages 1-2) |
| Risk factors / predisposition / triggers | Strongest associated arteriopathy is **fibromuscular dysplasia (FMD)**; other predispositions include inherited connective-tissue disorders, pregnancy/peripartum state, hormonal exposure, migraine, hypertension, and less commonly systemic inflammatory/autoimmune disease. Triggers differ by sex pattern in reviews: **emotional stress** commonly reported in women and **physical stress/exertion** in men; stimulant use (cocaine/amphetamines) also reported. (dang2024spontaneouscoronaryartery pages 6-7, rusali2025spontaneouscoronaryartery pages 3-5, smirnova2023spontaneouscoronaryartery pages 1-2, dang2024spontaneouscoronaryartery pages 6-6) | **FMD prevalence in SCAD:** ~25%–86% across studies/screening strategies. **Recurrence predictors:** FMD RR 2.02 (95% CI 1.03–3.94) in review; migraine HR 3.4 and FMD HR 5.1 for recurrent SCAD in one cohort. **Pregnancy-associated SCAD:** <5–17% of SCAD overall in reviews/meta-analyses; postpartum clustering recognized. (dang2024spontaneouscoronaryartery pages 6-6, pender2025spontaneouscoronaryartery pages 1-2, krittanawong2020recurrentspontaneouscoronary pages 1-2) |
| Diagnostics & angiographic types | **Invasive coronary angiography (ICA)** is the diagnostic gold standard in suspected SCAD; **OCT** and **IVUS** help confirm intimal tear, false lumen, and intramural hematoma and guide PCI when needed. Extracoronary vascular imaging (often **head-to-pelvis CTA**, with MRA alternative) is recommended to detect FMD/other arteriopathies. (morena2024advancesinthe pages 1-2, dang2024spontaneouscoronaryartery pages 6-7, dang2024spontaneouscoronaryartery pages 6-6, bollati2024spontaneouscoronarydissection pages 4-7, bollati2024spontaneouscoronarydissection pages 7-8) | **Saw/ICA angiographic types:** **Type 1** = classic radiolucent lumen/contrast staining; **Type 2** = long diffuse smooth narrowing (most common; includes 2A/2B); **Type 3** = focal stenosis mimicking atherosclerosis; **Type 4** = distal vessel occlusion. Review cited Type 1 ~29% and Type 3 ~4%. ICA “golden rules”: gentle catheter handling, minimize injections, use nitro to distinguish spasm, consider OCT/IVUS. (morena2024advancesinthe pages 1-2, bollati2024spontaneouscoronarydissection pages 4-7, bollati2024spontaneouscoronarydissection media ffbb95a5) |
| Management, recurrence & outcomes | **Conservative therapy** is preferred for clinically stable patients because spontaneous healing is common; **PCI** is reserved for ongoing ischemia, recurrent chest pain/ST elevation, hemodynamic/electrical instability, left main/proximal multivessel disease, or TIMI 0/1 flow. **CABG** is considered when PCI is not feasible/failed, especially left main or proximal disease. Beta-blockers are commonly used; ACEi/ARB for reduced LVEF; statins only for standard indications; antiplatelet strategy remains debated in conservatively managed SCAD. **Cardiac rehabilitation** and psychological support are recommended. (morena2024advancesinthe pages 1-2, smirnova2023spontaneouscoronaryartery pages 1-2, dang2024spontaneouscoronaryartery pages 6-6, bollati2024spontaneouscoronarydissection pages 4-7, bollati2024spontaneouscoronarydissection pages 7-8) | **Healing:** angiographic healing in ~70–97% over months. **Early extension/worsening:** ~5–10% in first days. **PCI technical failure/complexity:** Mayo series failure 53%; European series 27% technical failure and 9% emergency CABG. **Mortality:** in systematic review, in-hospital ~1.2% and follow-up ~1.3%; 3-year mortality 0.8% in one review. **Recurrence:** often ~10–20% within ~4 years; systematic review reported recurrent SCAD up to 31% across studies; one cohort 10.6% over median 4.7 years. **Rehab/screening uptake in meta-analysis:** antiplatelet 92.1%, beta-blocker 78.0%, FMD screening 54.4%, rehab referral 70.2%. (smirnova2023spontaneouscoronaryartery pages 1-2, dang2024spontaneouscoronaryartery pages 6-6, bollati2024spontaneouscoronarydissection pages 4-7, bollati2024spontaneouscoronarydissection pages 7-8) |
| Coding identifiers & active trials | Administrative studies identify SCAD using **ICD-9-CM 414.12** and **ICD-10-CM I25.42**; iatrogenic coronary laceration/dissection is commonly excluded with **ICD-9-CM 998.2** / **ICD-10-CM I97.51** in database analyses. No explicit MONDO/Orphanet identifier was confirmed in the retrieved evidence. (mughal2022contemporarytrendsin pages 1-3, krittanawong2020recurrentspontaneouscoronary pages 1-2) | **Trial NCTs:** **NCT04850417** (BA-SCAD; randomized study of beta-blockers and antiplatelets in SCAD, phase 4, planned n=600); **NCT06955663** (exercise support/rehabilitation after SCAD, planned n=120); **NCT04251039** (RESPONSE observational study in SCAD patients undergoing complex PCI). (dang2024spontaneouscoronaryartery pages 6-6) |


*Table: This table condenses high-yield evidence on spontaneous coronary artery dissection, including definition, epidemiology, risk factors, diagnostics, management, outcomes, coding, and current trial identifiers. It is useful as a compact reference for building a structured disease knowledge base entry.*

## Recent developments and expert analysis (2023–2024 emphasis)
- Registry-driven science has accelerated SCAD understanding, but reviews emphasize that **RCT evidence is still scarce**, prompting active trials such as BA-SCAD. (dang2024spontaneouscoronaryartery pages 6-6)
- Reviews highlight **system-level care gaps and practice variation**, including incomplete FMD screening and variable rehabilitation referral; meta-analytic estimates suggest substantial heterogeneity across regions and eras. (petrovic2024managementandoutcomes pages 1-2)

## URLs and publication dates (from retrieved sources)
- Dang Q. et al. *npj Cardiovascular Health* (May 2024). https://doi.org/10.1038/s44325-024-00004-y (dang2024spontaneouscoronaryartery pages 6-6)
- Petrović M. et al. *Frontiers in Cardiovascular Medicine* (Jan 2024). https://doi.org/10.3389/fcvm.2024.1276521 (petrovic2024managementandoutcomes pages 1-2)
- Apostolović S. et al. *Frontiers in Cardiovascular Medicine* (Feb 2024). https://doi.org/10.3389/fcvm.2024.1277604 (apostolovic2024spontaneouscoronaryartery pages 1-2)
- Smirnova A. et al. *European Heart Journal Supplements* (Apr 2023). https://doi.org/10.1093/eurheartjsupp/suad059 (smirnova2023spontaneouscoronaryartery pages 1-2)
- Mughal M.S. et al. *Expert Review of Cardiovascular Therapy* (May 2022). https://doi.org/10.1080/14779072.2022.2080055 (mughal2022contemporarytrendsin pages 1-3)

## Evidence gaps (important for knowledge base provenance)
- **MONDO/MeSH/Orphanet/OMIM** identifiers were not extractable from the retrieved full texts; adding them will require direct ontology lookups outside this evidence set.
- Variant-level genetics (ClinVar-style curation), epigenetic signatures, and experimental model organism evidence are not provided in the retrieved excerpts and remain incomplete here.


References

1. (morena2024advancesinthe pages 1-2): Arianna Morena, Federico Giacobbe, Ovidio De Filippo, Filippo Angelini, Francesco Bruno, Stefano Siliano, Giuseppe Giannino, Veronica Dusi, Matteo Bianco, Carloalberto Biolé, Ferdinando Varbella, Enrico Cerrato, Fabrizio D’Ascenzo, and Gaetano Maria De Ferrari. Advances in the management of spontaneous coronary artery dissection (scad): a comprehensive review. Reviews in Cardiovascular Medicine, Sep 2024. URL: https://doi.org/10.31083/j.rcm2509345, doi:10.31083/j.rcm2509345. This article has 11 citations and is from a peer-reviewed journal.

2. (dang2024spontaneouscoronaryartery pages 6-6): Quan Dang, Sonya Burgess, Peter J. Psaltis, Sarah Fairley, Jacqueline Saw, and Sarah Zaman. Spontaneous coronary artery dissection: a clinically oriented narrative review. npj Cardiovascular Health, May 2024. URL: https://doi.org/10.1038/s44325-024-00004-y, doi:10.1038/s44325-024-00004-y. This article has 14 citations.

3. (smirnova2023spontaneouscoronaryartery pages 1-2): Alexandra Smirnova, Flaminia Aliberti, Claudia Cavaliere, Ilaria Gatti, Viviana Vilardo, Carmelina Giorgianni, Chiara Cassani, Alessandra Repetto, Nupoor Narula, Lorenzo Giuliani, Mario Urtis, Yukio Ozaki, Francesco Prati, Eloisa Arbustini, and Michela Ferrari. Spontaneous coronary artery dissection: an unpredictable event. European Heart Journal Supplements : Journal of the European Society of Cardiology, 25:B7-B11, Apr 2023. URL: https://doi.org/10.1093/eurheartjsupp/suad059, doi:10.1093/eurheartjsupp/suad059. This article has 11 citations.

4. (petrovic2024managementandoutcomes pages 1-2): Milovan Petrović, Tatjana Miljković, Aleksandra Ilić, Mila Kovačević, Milenko Čanković, Dragana Dabović, Anastazija Stojšić Milosavljević, Snežana Čemerlić Maksimović, Milana Jaraković, Dragica Andrić, Miodrag Golubović, Marija Bjelobrk, Snežana Bjelić, Snežana Tadić, Jelena Slankamenac, Svetlana Apostolović, Vladimir Djurović, and Aleksandra Milovančev. Management and outcomes of spontaneous coronary artery dissection: a systematic review of the literature. Frontiers in Cardiovascular Medicine, Jan 2024. URL: https://doi.org/10.3389/fcvm.2024.1276521, doi:10.3389/fcvm.2024.1276521. This article has 17 citations and is from a peer-reviewed journal.

5. (pender2025spontaneouscoronaryartery pages 1-2): Patrick Pender, Mithila Zaheen, Quan M. Dang, Viet Dang, James Xu, Matthew Hollings, Sidney Lo, Kazuaki Negishi, and Sarah Zaman. Spontaneous coronary artery dissection: a narrative review of epidemiology and public health implications. Medicina, 61:650, Apr 2025. URL: https://doi.org/10.3390/medicina61040650, doi:10.3390/medicina61040650. This article has 7 citations.

6. (dang2024spontaneouscoronaryartery pages 6-7): Quan Dang, Sonya Burgess, Peter J. Psaltis, Sarah Fairley, Jacqueline Saw, and Sarah Zaman. Spontaneous coronary artery dissection: a clinically oriented narrative review. npj Cardiovascular Health, May 2024. URL: https://doi.org/10.1038/s44325-024-00004-y, doi:10.1038/s44325-024-00004-y. This article has 14 citations.

7. (apostolovic2024spontaneouscoronaryartery pages 1-2): Svetlana Apostolović, Aleksandra Ignjatović, Dragana Stanojević, Danijela Djordjević Radojković, Miroslav Nikolić, Jelena Milošević, Tamara Filipović, Katarina Kostić, Ivana Miljković, Aleksandra Djoković, Gordana Krljanac, Zlatko Mehmedbegović, Ivan Ilić, Srdjan Aleksandrić, and Valeria Paradies. Spontaneous coronary artery dissection in women in the generative period: clinical characteristics, treatment, and outcome—a systematic review and meta-analysis. Frontiers in Cardiovascular Medicine, Feb 2024. URL: https://doi.org/10.3389/fcvm.2024.1277604, doi:10.3389/fcvm.2024.1277604. This article has 16 citations and is from a peer-reviewed journal.

8. (mughal2022contemporarytrendsin pages 1-3): Mohsin S Mughal, Hafsa Akbar, Ikwinder P Kaur, Ali R Ghani, Hasan Mirza, Weiyi Xia, Mohammed Haris Usman, Mahboob Alam, and Tarek Helmy. Contemporary trends in the incidence of spontaneous coronary artery dissection (scad) – ethnic and household income disparities. Expert Review of Cardiovascular Therapy, 20:485-489, May 2022. URL: https://doi.org/10.1080/14779072.2022.2080055, doi:10.1080/14779072.2022.2080055. This article has 9 citations and is from a peer-reviewed journal.

9. (krittanawong2020recurrentspontaneouscoronary pages 1-2): Chayakrit Krittanawong, Anirudh Kumar, Hafeez Ul Hassan Virk, Zhen Wang, Kipp W. Johnson, Bing Yue, and Deepak L. Bhatt. Recurrent spontaneous coronary artery dissection in the united states. International Journal of Cardiology, 301:34-37, Feb 2020. URL: https://doi.org/10.1016/j.ijcard.2019.10.052, doi:10.1016/j.ijcard.2019.10.052. This article has 28 citations and is from a peer-reviewed journal.

10. (rusali2025spontaneouscoronaryartery pages 3-5): Andrei Constantin Rusali, Ioana Caterina Lupu, Lavinia Maria Rusali, and Lucia Cojocaru. Spontaneous coronary artery dissection unveiled: pathophysiology, imaging, and evolving management strategies. Jun 2025. URL: https://doi.org/10.20944/preprints202506.0355.v1, doi:10.20944/preprints202506.0355.v1.

11. (gori2023contemporaryreviewon pages 3-4): Tommaso Gori, Luca Bergamaschi, Jarakovic Milovancev Cankovic Petrovic Bjelobrk Ilic Srdanov Kovacevic, M. Kovačević, M. Jarakovic, A. Milovančev, M. Čanković, M. Petrovic, M. Bjelobrk, A. Ilić, I. Srdanović, S. Tadić, D. Dabović, B. Crnomarković, N. Komazec, N. Dračina, S. Apostolovic, D. Stanojević, and V. Kunadian. Contemporary review on spontaneous coronary artery dissection: insights into the angiographic finding and differential diagnosis. Frontiers in Cardiovascular Medicine, Nov 2023. URL: https://doi.org/10.3389/fcvm.2023.1278453, doi:10.3389/fcvm.2023.1278453. This article has 14 citations and is from a peer-reviewed journal.

12. (bollati2024spontaneouscoronarydissection pages 4-7): Mario Bollati, Vincenzo Ercolano, and Pietro Mazzarotto. Spontaneous coronary dissection review: a complex picture. Reviews in Cardiovascular Medicine, Dec 2024. URL: https://doi.org/10.31083/j.rcm2512448, doi:10.31083/j.rcm2512448. This article has 6 citations and is from a peer-reviewed journal.

13. (bollati2024spontaneouscoronarydissection media ffbb95a5): Mario Bollati, Vincenzo Ercolano, and Pietro Mazzarotto. Spontaneous coronary dissection review: a complex picture. Reviews in Cardiovascular Medicine, Dec 2024. URL: https://doi.org/10.31083/j.rcm2512448, doi:10.31083/j.rcm2512448. This article has 6 citations and is from a peer-reviewed journal.

14. (bollati2024spontaneouscoronarydissection media 8d0f25c2): Mario Bollati, Vincenzo Ercolano, and Pietro Mazzarotto. Spontaneous coronary dissection review: a complex picture. Reviews in Cardiovascular Medicine, Dec 2024. URL: https://doi.org/10.31083/j.rcm2512448, doi:10.31083/j.rcm2512448. This article has 6 citations and is from a peer-reviewed journal.

15. (bollati2024spontaneouscoronarydissection media 8c541a8a): Mario Bollati, Vincenzo Ercolano, and Pietro Mazzarotto. Spontaneous coronary dissection review: a complex picture. Reviews in Cardiovascular Medicine, Dec 2024. URL: https://doi.org/10.31083/j.rcm2512448, doi:10.31083/j.rcm2512448. This article has 6 citations and is from a peer-reviewed journal.

16. (bollati2024spontaneouscoronarydissection media 353fb04a): Mario Bollati, Vincenzo Ercolano, and Pietro Mazzarotto. Spontaneous coronary dissection review: a complex picture. Reviews in Cardiovascular Medicine, Dec 2024. URL: https://doi.org/10.31083/j.rcm2512448, doi:10.31083/j.rcm2512448. This article has 6 citations and is from a peer-reviewed journal.

17. (bollati2024spontaneouscoronarydissection media 94fd0b42): Mario Bollati, Vincenzo Ercolano, and Pietro Mazzarotto. Spontaneous coronary dissection review: a complex picture. Reviews in Cardiovascular Medicine, Dec 2024. URL: https://doi.org/10.31083/j.rcm2512448, doi:10.31083/j.rcm2512448. This article has 6 citations and is from a peer-reviewed journal.

18. (bollati2024spontaneouscoronarydissection media df824cb3): Mario Bollati, Vincenzo Ercolano, and Pietro Mazzarotto. Spontaneous coronary dissection review: a complex picture. Reviews in Cardiovascular Medicine, Dec 2024. URL: https://doi.org/10.31083/j.rcm2512448, doi:10.31083/j.rcm2512448. This article has 6 citations and is from a peer-reviewed journal.

19. (bollati2024spontaneouscoronarydissection pages 7-8): Mario Bollati, Vincenzo Ercolano, and Pietro Mazzarotto. Spontaneous coronary dissection review: a complex picture. Reviews in Cardiovascular Medicine, Dec 2024. URL: https://doi.org/10.31083/j.rcm2512448, doi:10.31083/j.rcm2512448. This article has 6 citations and is from a peer-reviewed journal.

20. (rusali2025spontaneouscoronaryartery pages 14-16): Andrei Constantin Rusali, Ioana Caterina Lupu, Lavinia Maria Rusali, and Lucia Cojocaru. Spontaneous coronary artery dissection unveiled: pathophysiology, imaging, and evolving management strategies. Jun 2025. URL: https://doi.org/10.20944/preprints202506.0355.v1, doi:10.20944/preprints202506.0355.v1.

21. (singulane2025spontaneouscoronaryartery pages 1-2): Cristiane C. Singulane, Shuo Wang, Kelsey Watts, Macy E. Stahl, LeAnn Denlinger, Rachel Lloyd, Pranavi Pallinti, Lauren Preston, Mohamed Morsy, Odayme Quesada, Angela Taylor, Randy K. Ramcharitar, Mete Civelek, and Patricia F. Rodriguez-Lozano. Spontaneous coronary artery dissection (scad): unveiling the enigma of the unexpected coronary event. Current Atherosclerosis Reports, Aug 2025. URL: https://doi.org/10.1007/s11883-025-01328-5, doi:10.1007/s11883-025-01328-5. This article has 8 citations and is from a peer-reviewed journal.