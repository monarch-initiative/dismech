---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-04T21:37:00.619523'
end_time: '2026-05-04T21:48:24.025787'
duration_seconds: 683.41
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Patent Ductus Arteriosus
  mondo_id: ''
  category: Congenital
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 35
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Patent Ductus Arteriosus
- **MONDO ID:**  (if available)
- **Category:** Congenital

## Research Objectives

Please provide a comprehensive research report on **Patent Ductus Arteriosus** covering all of the
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
- **Disease Name:** Patent Ductus Arteriosus
- **MONDO ID:**  (if available)
- **Category:** Congenital

## Research Objectives

Please provide a comprehensive research report on **Patent Ductus Arteriosus** covering all of the
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


# Patent Ductus Arteriosus (PDA) — Comprehensive Disease Characteristics Report (Congenital)

## Executive summary
Patent ductus arteriosus (PDA) is the postnatal persistence of the fetal ductus arteriosus (DA), a conduit between the pulmonary artery and descending aorta. In preterm infants, PDA is common and strongly related to gestational age/birth weight; controversy persists regarding what constitutes a *hemodynamically significant PDA* (hsPDA), optimal timing of treatment, and whether early pharmacologic closure improves longer-term outcomes. Recent work emphasizes physiology-guided diagnosis (targeted neonatal echocardiography and combined hemodynamic models), increasing real-world use of transcatheter closure in very small infants, and active investigation of prophylactic/targeted acetaminophen strategies. (chen2025combinationofechocardiography pages 1-2, dani2025diagnosisofpatent pages 1-2, trahan2025patentductusarteriosus pages 4-5, baruteau2024deviceclosureof pages 1-2)

---

## 1. Disease information
### 1.1 What is the disease?
*Patent ductus arteriosus* is persistence of patency of the DA after birth, resulting in (typically) a left-to-right shunt from the aorta to pulmonary artery once pulmonary vascular resistance falls. The DA is defined as a fetal vessel connecting the main pulmonary artery to the proximal descending aorta. (cucerea2025serumbiomarkersin pages 1-2)

### 1.2 Key identifiers and synonyms
**Synonyms/alternate names in contemporary literature:** “PDA”, “persistent ductus arteriosus”, and “ductal patency/persistent patency of the ductus arteriosus” are used interchangeably in recent reviews and trials. (cucerea2025serumbiomarkersin pages 1-2, ursino2025treocapaprophylactictreatment pages 1-2)

**ICD/MeSH/MONDO/OMIM/Orphanet identifiers:** Not reliably retrievable from the full-text evidence captured in the current tool session; therefore, no identifier values are asserted here to avoid uncited claims.

### 1.3 Evidence-source characterization
The information below is derived primarily from:
- **Aggregated disease-level resources** (systematic reviews and narrative reviews) for mechanisms and treatment syntheses (baruteau2024deviceclosureof pages 1-2, luo2024theimpactof pages 1-2, pugnaloni2024ductusarteriosusin pages 5-8, cucerea2025serumbiomarkersin pages 1-2)
- **Human clinical cohorts/trials** for quantified outcomes and practice variation (chesi2024patentductusarteriosus pages 1-2, dani2025diagnosisofpatent pages 1-2, chen2025combinationofechocardiography pages 1-2)
- **Model organism primary studies** for causal molecular regulators of DA closure (mouse developmental genetics) (zou2023prdm6drivesductus pages 1-2)

---

## 2. Etiology
### 2.1 Disease causal factors (mechanistic)
PDA arises when normal physiologic DA constriction and subsequent anatomic remodeling/closure fail. Birth-related rise in oxygen tension and reduced circulating prostaglandins normally trigger DA vasoconstriction (via inhibition of potassium channels, increased Ca2+ influx) and later remodeling into the ligamentum arteriosum. (cucerea2025serumbiomarkersin pages 1-2)

Preterm DA tissue is described as *thinner and less muscular* with smooth muscle cells (SMCs) more sensitive to circulating vasodilators (PGE2 and nitric oxide), contributing to prolonged patency in prematurity. (pugnaloni2024ductusarteriosusin pages 5-8)

### 2.2 Risk factors
**Prematurity / low birth weight:** PDA prevalence inversely correlates with gestational age and birth weight. In one prospective cohort background, PDA affected ~65% of very-low-birth-weight infants (<1500 g), and hsPDA prevalence has been reported to reach ~50% in infants <28 weeks. (chen2025combinationofechocardiography pages 1-2)

**Perinatal/clinical risk factors for hsPDA progression (early life):** In a prospective study combining echocardiography and noninvasive hemodynamic monitoring, independent risk factors included maternal eclampsia/preeclampsia, surfactant use, echocardiographic size/LA:Ao metrics, and total body water percentage at 48–72 h. (chen2025combinationofechocardiography pages 1-2)

**Systemic inflammation / mediator milieu:** Reviews describe that systemic inflammation (e.g., TNFα) can increase vasodilatory mediators (PGE2, NO), increasing patency risk in preterms. (pugnaloni2024ductusarteriosusin pages 5-8)

**Other proposed contributors in preterm infants:** adrenal insufficiency/altered cortisol, thrombocytopenia/platelet dysfunction, and clinical interventions that affect transductal flow/diameter (e.g., surfactant) are discussed as contributors to prolonged patency and hemodynamic sequelae. (pugnaloni2024ductusarteriosusin pages 5-8)

### 2.3 Protective factors
No robust “protective factor” interventions with quantified effect sizes were identified in the retrieved evidence set. However, the physiologic transition itself—loss of placental prostaglandins and increased oxygen tension—acts as a natural pro-closure shift. (cucerea2025serumbiomarkersin pages 1-2)

### 2.4 Gene–environment interactions
Direct gene–environment interaction studies (formal GxE) were not clearly represented in the retrieved evidence set. The contemporary mechanistic framing supports interaction between **genetic variation in prostaglandin/SMC programs** and **environmental/perinatal exposures that alter oxygen tension, inflammation, and vasodilator signaling**, but specific interaction effect sizes were not available. (pugnaloni2024ductusarteriosusin pages 5-8, minta2025associationbetweengenetic pages 1-2, zou2023prdm6drivesductus pages 1-2)

---

## 3. Phenotypes
### 3.1 Major clinical phenotypes and HPO suggestions
In preterm infants, PDA phenotypes range from asymptomatic ductal patency to hemodynamically significant shunting with pulmonary overcirculation and systemic hypoperfusion. Contemporary echocardiography-based definitions operationalize “pulmonary overcirculation” and “systemic steal/hypoperfusion” patterns. (chesi2024patentductusarteriosus pages 2-4, mukherjee2025…paracetamoland pages 57-62)

**Common phenotype domains and candidate HPO terms (suggestions):**
- Cardiac murmur (clinical sign): *Heart murmur* (HP:0001642) — described as “machinery murmur” in clinical descriptions embedded in trial methods. (mukherjee2025…paracetamoland pages 57-62)
- Wide pulse pressure / bounding pulses (clinical signs): *Increased pulse pressure* (HP:0031232), *Bounding pulse* (HP:0025502) — described as common clinical signs in hsPDA screening contexts. (mukherjee2025…paracetamoland pages 57-62)
- Respiratory morbidity association: *Respiratory distress* (HP:0002098), *Bronchopulmonary dysplasia* (HP:0012099). Persistent left-to-right shunt is linked to worse respiratory failure and higher BPD risk. (dani2025diagnosisofpatent pages 1-2, chesi2024patentductusarteriosus pages 1-2)
- Neurologic/retinal complications (in preterm context): *Intraventricular hemorrhage* (HP:0001344), *Retinopathy of prematurity* (HP:0000593). (chesi2024patentductusarteriosus pages 1-2)

**Frequency/severity notes:**
- hsPDA incidence estimates vary strongly with diagnostic criteria and timing. A study directly comparing criteria found hsPDA incidence ~34–35% across three approaches but emphasized that different criteria/timing diagnose different infants at different times. (dani2025diagnosisofpatent pages 1-2)

### 3.2 Quality-of-life impact
Direct patient-reported QoL instruments are uncommon in neonatal PDA literature; the principal QoL-related impacts discussed are mediated via prematurity complications (BPD, IVH, ROP) and long-term neurodevelopment. Persistent shunting is linked to pulmonary hypertension and impaired neurodevelopment in broad clinical association statements. (dani2025diagnosisofpatent pages 1-2)

---

## 4. Genetic / molecular information
### 4.1 Causal genes and pathways (current evidence)
**PRDM6 (model organism causality; human relevance suggested):** In a mouse developmental model, Wnt1-lineage deletion of *Prdm6* caused perinatal lethality with a fully penetrant patent ductus arteriosus phenotype, attributed to reduced DA tone/contractility and downregulation of a DA-enriched smooth-muscle contractile gene program. The paper also maps an SMC-selective enhancer in *Prdm6* with allele-specific activity and highlights a GWAS SNP (rs17149944) as potentially causal at the PRDM6 locus. (zou2023prdm6drivesductus pages 1-2)

**Prostaglandin pathway genes (human association in preterms):** A 2025 association study in 99 preterm neonates investigated prostaglandin-pathway polymorphisms (phospholipase A2, COX-1, prostaglandin synthase 2, EP4/PTGER4) and reported associations of selected polymorphisms with PDA risk; one excerpt notes rs1051931 in a phospholipase A2 gene associated with increased PDA risk (OR ~2.49) in their analysis. (minta2025associationbetweengenetic pages 1-2, minta2025associationbetweengenetic pages 7-9)

### 4.2 Mechanistic molecular chain (upstream → downstream)
A synthesis of recent reviews:
1) **Fetal patency maintenance:** relative hypoxia + PGE2 signaling (EP4 receptor) and other vasodilatory pathways (cAMP/cGMP) maintain DA relaxation; NO and CO contribute. (cucerea2025serumbiomarkersin pages 1-2)
2) **Immediate postnatal functional closure:** increased oxygen tension and reduced prostaglandins promote DA SMC constriction through inhibition of K+ channels and increased Ca2+ influx; oxygen also increases endothelin-1 and reactive oxygen species, generating isoprostanes. (cucerea2025serumbiomarkersin pages 1-2)
3) **Anatomic closure/remodeling:** over days–weeks, closure involves SMC migration/proliferation, extracellular matrix production, endothelial proliferation, and disruption of the internal elastic lamina. (pugnaloni2024ductusarteriosusin pages 5-8)
4) **Failure points in prematurity:** immature DA structure (thinner/less muscular), heightened sensitivity to PGE2/NO, and inflammatory and endocrine perturbations increase risk of persistent patency and hsPDA physiology. (pugnaloni2024ductusarteriosusin pages 5-8)

### 4.3 Ontology suggestions (molecular/cellular)
- **GO Biological Process (suggestions):** “smooth muscle contraction”, “regulation of blood vessel diameter”, “prostaglandin biosynthetic process”, “response to oxygen levels”, “vascular remodeling” (supported mechanistically by DA constriction/remodeling narratives). (pugnaloni2024ductusarteriosusin pages 5-8, cucerea2025serumbiomarkersin pages 1-2, zou2023prdm6drivesductus pages 1-2)
- **Cell Ontology (CL) (suggestions):** vascular smooth muscle cell; endothelial cell (DA remodeling/closure depends on SMC and EC processes). (pugnaloni2024ductusarteriosusin pages 5-8, cucerea2025serumbiomarkersin pages 1-2)

### 4.4 Epigenetics
Specific disease-associated DNA methylation/histone marks were not identified in the retrieved evidence set.

### 4.5 Abstract-supported key quotes
- “Fetal DA patency is maintained by … Prostaglandin E2 (PGE2) signaling via the EP4 receptor…” (from review excerpt) (cucerea2025serumbiomarkersin pages 1-2)
- “Prdm6 depletion … resulted in perinatal lethality and a completely penetrant patent ductus arteriosus (DA) phenotype.” (abstract text) (zou2023prdm6drivesductus pages 1-2)

---

## 5. Environmental information
The retrieved evidence emphasizes **perinatal physiologic environment** (oxygen tension, inflammation, endocrine milieu) over classic adult-style lifestyle exposures.

- **Oxygen tension change at birth** is a central environmental/physiologic driver of closure. (cucerea2025serumbiomarkersin pages 1-2)
- **Inflammation (e.g., TNFα)** may increase PGE2 and NO, promoting patency. (pugnaloni2024ductusarteriosusin pages 5-8)
- **Clinical exposures** (e.g., surfactant use; fluid intake; ventilation) appear associated with hsPDA development in prospective neonatal cohorts. (chen2025combinationofechocardiography pages 1-2)

---

## 6. Mechanism / pathophysiology
### 6.1 Current consensus concepts
**Hemodynamic significance is a physiology construct.** There is “no consensus regarding the timing and diagnostic criteria for identifying hemodynamically significant PDA (hsPDA)” and different criteria identify different infants at different postnatal times, which contributes to inter-center variability. (dani2025diagnosisofpatent pages 1-2)

**Composite echocardiographic approaches:** Recent clinical studies operationalize hsPDA through DA diameter/flow patterns plus indices of pulmonary overcirculation and systemic hypoperfusion. For example, one multicenter cohort defined hsPDA as PDA ≥1.6 mm with pulsatile/growing flow plus ≥2/3 indices of overcirculation/hypoperfusion. (chesi2024patentductusarteriosus pages 1-2)

### 6.2 Early risk stratification and quantitative models
A prospective study combining echocardiographic and systemic hemodynamic parameters within 72 h showed that a combined model (maternal factors + surfactant + DA diameter/weight ratio + LA/Ao + TBW%) achieved AUC 0.981 with sensitivity 100% and specificity 90.0% for predicting hsPDA development. (chen2025combinationofechocardiography pages 1-2)

### 6.3 Visualization evidence (tables/criteria)
The cohort definitions and adjusted odds ratios for outcomes by PDA category are tabulated in the Chesi 2024 paper (see extracted tables). (chesi2024patentductusarteriosus media 56412072, chesi2024patentductusarteriosus media 692abe13)

---

## 7. Anatomical structures affected
### 7.1 Organ/system level
- **Primary structure:** ductus arteriosus (vascular conduit between pulmonary artery and proximal descending aorta). (cucerea2025serumbiomarkersin pages 1-2)
- **Systemic involvement (downstream):** pulmonary circulation (overcirculation), systemic organ perfusion (hypoperfusion/“steal”), and complications involving lung (BPD), brain (IVH), and retina (ROP) in preterm infants. (chesi2024patentductusarteriosus pages 1-2)

### 7.2 UBERON suggestions
- ductus arteriosus; pulmonary artery; aorta (proximal descending aorta) (supported anatomically by definition). (cucerea2025serumbiomarkersin pages 1-2)

---

## 8. Temporal development
### 8.1 Onset
Congenital: DA is physiologically present in utero; PDA refers to failure of closure after birth.

### 8.2 Natural history / progression
Anatomic closure typically requires days to weeks via remodeling processes (SMC/EC/ECM changes). (pugnaloni2024ductusarteriosusin pages 5-8)

### 8.3 Critical windows
Early postnatal time (first 72–84 hours) is a key window in preterm infants for echocardiographic assessment; however, criteria/timing materially alter hsPDA classification. (dani2025diagnosisofpatent pages 1-2)

---

## 9. Inheritance and population
### 9.1 Epidemiology (recent quantitative data)
- Day-4 PDA prevalence by gestational age (reported in a diagnostic comparison paper): ~10% (30–37 weeks), ~80% (25–28 weeks), >90% (24 weeks). (dani2025diagnosisofpatent pages 1-2)
- PDA in VLBW infants: ~65% (<1500 g) in background estimates; hsPDA prevalence can reach ~50% in <28 weeks. (chen2025combinationofechocardiography pages 1-2)
- Large multi-hospital consortium report (2011–2022): among 54,813 infants (23–32 weeks), 36% had a PDA diagnosis. (trahan2025patentductusarteriosus pages 4-5)

### 9.2 Genetics/inheritance
A heritable component is supported by twin and animal-model evidence (cited in the prostaglandin-pathway association paper), and by developmental gene-regulatory causality (PRDM6 mouse model). However, specific Mendelian inheritance patterns for “isolated PDA” were not established from the retrieved evidence set. (minta2025associationbetweengenetic pages 1-2, zou2023prdm6drivesductus pages 1-2)

---

## 10. Diagnostics
### 10.1 Echocardiography (core diagnostic modality)
Diagnosis and hemodynamic assessment are echo-based, with emphasis on ductal size and flow direction/pattern, pulmonary overcirculation indices (e.g., LA/Ao), and systemic hypoperfusion indices. (chen2025combinationofechocardiography pages 1-2, chesi2024patentductusarteriosus pages 1-2, mukherjee2025…paracetamoland pages 57-62)

**Practice variation / criteria uncertainty:** Comparing different criteria sets shows stable overall incidence (~34–35%) but changing concordance and patient-level classification by time and criteria, underscoring the need for standardized definitions for hsPDA. (dani2025diagnosisofpatent pages 1-2)

### 10.2 Biomarkers (emerging adjuncts)
A 2025 narrative review summarizes candidate serum biomarkers (e.g., natriuretic peptides, troponin, vasoactive and inflammatory markers) as correlates of PDA physiology, but emphasizes that clinical judgment must integrate these with echocardiography. (cucerea2025serumbiomarkersin pages 1-2)

### 10.3 Differential diagnosis
Not comprehensively covered in the retrieved evidence set. Clinically, confounding early-day factors (persistent pulmonary hypertension, ventilator pressures, vasoactive infusions) can mask shunt direction/magnitude and complicate interpretation. (chesi2024patentductusarteriosus pages 10-11)

---

## 11. Outcome / prognosis
### 11.1 Complications and quantified associations
A multicenter VLBW cohort study reported strong adjusted associations between PDA categories and outcomes:
- **Non-hsPDA vs no PDA:** ~15-fold higher risk of death. (chesi2024patentductusarteriosus pages 1-2)
- **hsPDA vs no PDA:** ~6-fold higher BPD occurrence. (chesi2024patentductusarteriosus pages 1-2)
- **Most significant hsPDA physiology (systemic hypoperfusion + pulmonary overcirculation):** grade ≥3 IVH risk increased 8.7-fold and grade ≥3 ROP risk increased 18-fold. (chesi2024patentductusarteriosus pages 1-2)

These associations and the exact categorization/criteria are presented in the paper’s tables (image-extracted). (chesi2024patentductusarteriosus media 56412072, chesi2024patentductusarteriosus media 692abe13)

---

## 12. Treatment
### 12.1 Pharmacotherapy (NSAIDs and acetaminophen)
**Route effects (ibuprofen):** A 2024 systematic review/meta-analysis (n=630) found oral ibuprofen had higher initial-course closure rates than IV ibuprofen (RR 1.27; 95% CI 1.13–1.44; p<0.0001) without statistically significant differences in adverse events or need for surgery after a full course. (luo2024theimpactof pages 1-2)

**Route effects (acetaminophen/paracetamol):** The same meta-analysis found no significant difference between oral vs IV acetaminophen/paracetamol for closure (RR 0.86; 95% CI 0.38–1.91). (luo2024theimpactof pages 1-2)

**Contemporary overview (extremely preterm):** A 2025 review reports that acetaminophen response rates exceed 50% across gestational ages in some series (with 47% response at 21–22 weeks in one cohort cited), but ductal reopening and nonresponse remain common (e.g., 37% reopening among initial responders; 20–30% remain patent despite therapy). The same review highlights diminishing returns with repeated courses (failure rates after first/second/third courses reported as 38%/76%/92% for ibuprofen or acetaminophen courses). (trahan2025patentductusarteriosus pages 4-5)

**Expert consensus framing:** A 2024 device-closure review states that first-line medical therapy (COX inhibitors or acetaminophen) has “moderate closure success” around 60–70%, and notes important adverse event concerns (bleeding, NEC, renal impairment) that contribute to conservative strategies and interventional escalation. (baruteau2024deviceclosureof pages 1-2)

**MAXO suggestions (treatment actions):**
- Pharmacologic closure of PDA (COX inhibition; acetaminophen therapy)
- Transcatheter closure of PDA
- Surgical ligation of PDA
(These are ontology suggestions; not asserted as exact MAXO IDs due to lack of identifier evidence in retrieved texts.)

### 12.2 Interventional and surgical closure
**Transcatheter closure outcomes (Piccolo trial follow-up):** 3-year follow-up of 200 infants ≥700 g undergoing transcatheter PDA closure with Amplatzer Piccolo reported implant success 95.5% (191/200), and among those evaluated at 3 years, PDA closure 100% (33/33); overall survival >95% with 9 deaths not adjudicated device/procedure-related; notable events included aortic obstruction (2, requiring stent) and increased tricuspid regurgitation (5). (francescato2023transcatheterclosurein pages 1-2)

**Real-world implementation trends (Children’s Hospitals Neonatal Consortium, 2011–2022):** Among 54,813 infants (23–32 weeks), 36% had PDA; pharmacotherapy use increased 44% (relative) over time, “mostly with increased acetaminophen use”; transcatheter closure increased from 0 to 20.3%, and surgical ligation decreased from 25.1% to 3.6%. (trahan2025patentductusarteriosus pages 4-5)

**Practice shift / expert opinion:** Contemporary reviews emphasize rapid adoption of transcatheter closure (particularly after approval of Amplatzer Piccolo) and its role as an alternative to surgical ligation in experienced centers, while acknowledging ongoing questions around timing, patient selection, and complications at extremely low weights. (baruteau2024deviceclosureof pages 1-2, francescato2023transcatheterclosurein pages 1-2)

---

## 13. Prevention
No established population-level primary prevention strategy was identified in the retrieved evidence set (PDA in prematurity reflects developmental physiology). The active research direction is **secondary prevention / early targeted therapy** to prevent severe morbidity.

A major example is prophylactic acetaminophen in extremely preterm infants (TREOCAPA) to improve survival without severe morbidity. (ursino2025treocapaprophylactictreatment pages 1-2)

---

## 14. Other species / natural disease
The evidence set primarily addresses human PDA, but mechanistic conclusions are supported by **animal models** (mouse developmental genetics; cited animal evidence for prostaglandin/EP4 pathway disruption). (minta2025associationbetweengenetic pages 1-2, zou2023prdm6drivesductus pages 1-2)

---

## 15. Model organisms
### 15.1 Mouse developmental model (genetic)
- **Model:** Wnt1-lineage Prdm6 conditional deletion.
- **Phenotype:** Completely penetrant PDA with reduced DA tone/contractility.
- **Use:** Demonstrates causal role of SMC identity/contractility programs in DA closure; links human-associated GWAS enhancer activity to DA biology.
(zou2023prdm6drivesductus pages 1-2)

---

## Recent developments (2023–2024 emphasis)
1) **Quantified outcome associations even in “non-hsPDA”:** A 2024 multicenter cohort reported strong associations between PDA categories and mortality/BPD/IVH/ROP, and highlighted potential inadequacy of early hsPDA criteria in the first days of life. (chesi2024patentductusarteriosus pages 1-2, chesi2024patentductusarteriosus pages 10-11)
2) **Evolving transcatheter closure evidence base:** 2023–2024 work and reviews emphasize Piccolo-enabled closure in very small infants and continued follow-up on safety/complications. (francescato2023transcatheterclosurein pages 1-2, baruteau2024deviceclosureof pages 1-2)
3) **Route-of-administration evidence for ibuprofen:** 2024 meta-analysis suggests oral ibuprofen may be more effective than IV for initial closure without increased adverse events. (luo2024theimpactof pages 1-2)

---

## Current applications and real-world implementations
- **NICU physiology-guided echocardiography:** Diagnostic practice increasingly relies on echocardiographic plus systemic hemodynamic indices (e.g., DA diameter/weight, LA/Ao; systemic indices like TBW%, TPRI) to predict hsPDA evolution and guide individualized decisions. (chen2025combinationofechocardiography pages 1-2, chesi2024patentductusarteriosus pages 1-2)
- **Health-system treatment shifts:** Multicenter consortium data show large shifts from surgical ligation to transcatheter closure and increased acetaminophen use over 2011–2022. (trahan2025patentductusarteriosus pages 4-5)

---

## Clinical trials landscape (selected, with URLs)
- **TREOCAPA prophylactic acetaminophen** (NCT04459117; Trials statistical analysis plan published Feb 2025): Phase III, randomized, multicenter, double-blind, placebo-controlled; 803 infants at 23–28 weeks GA; primary outcome survival without severe morbidity at 36 weeks PMA (BPD grade 3, NEC II/III, IVH III–IV, or cystic leukomalacia). URL: https://clinicaltrials.gov/study/NCT04459117 (trial registry ID referenced in paper). (ursino2025treocapaprophylactictreatment pages 1-2)
- **U.S. PDA Registry** (NCT04205877): Observational registry targeting infants ~700–2000 g for transcatheter closure outcomes and safety endpoints (vascular/device-related) and effectiveness (closure by 6 months). URL: https://clinicaltrials.gov/study/NCT04205877 (NCT04205877 chunk 1)
- **PREEMIE device study** (NCT06587282): Prospective single-arm study of Bloom Micro Occluder System in premature infants 600–2500 g, outcomes include 30-day MAE and 6-month clinical success. URL: https://clinicaltrials.gov/study/NCT06587282 (NCT06587282 chunk 1)
- **Recent pharmacologic comparative RCT (Pakistan)** (NCT06601114): Oral paracetamol vs oral ibuprofen; estimated n=254; closure by Doppler at day 3. URL: https://clinicaltrials.gov/study/NCT06601114 (NCT06601114 chunk 1)

---

## Data-rich summary table artifact
The following table is designed for direct knowledge-base ingestion.

| Domain | Key points (with numbers) | Population/context | Source (first author year, journal) | URL |
|---|---|---|---|---|
| hsPDA definition/criteria | **Chesi 2024:** hsPDA defined as PDA **≥1.6 mm** at pulmonary end with **growing/pulsatile flow** **plus ≥2/3** indices of pulmonary overcirculation and/or systemic hypoperfusion; early treatment decisions remained partly discordant with ultrasound, with **up to 40%** treated in week 1 not meeting hsPDA criteria on ultrasound. (chesi2024patentductusarteriosus pages 1-2, chesi2024patentductusarteriosus pages 2-4) | Multicenter prospective cohort of **218 VLBW infants** | Chesi 2024, *PLOS ONE* | https://doi.org/10.1371/journal.pone.0306769 |
| hsPDA definition/criteria | **Dani 2025:** Florence criteria = left-to-right shunt + ductal size **≥1.4 mm/kg** **plus ≥2** other echocardiographic criteria; Paris criteria use **2 echocardiographic criteria + gestational age**; incidence of hsPDA was similar across methods: **35% (Florence)**, **34% (Paris)**, **35% (El-Khuffash score)**. (dani2025diagnosisofpatent pages 1-2) | Very preterm infants **<32 weeks**; echo at **24–48 h** and **72–84 h** | Dani 2025, *European Journal of Pediatrics* | https://doi.org/10.1007/s00431-025-06485-y |
| Epidemiology by GA/BW | PDA prevalence is inversely related to maturity: at day 4, about **10%** in infants **30–37 weeks**, **~80%** in **25–28 weeks**, and **>90%** at **24 weeks**; 2024 VON data cited: **31%** of infants **<30 weeks** received pharmacologic treatment and **3%** had surgical closure. (dani2025diagnosisofpatent pages 1-2) | Preterm infants, especially very preterm | Dani 2025, *European Journal of Pediatrics* | https://doi.org/10.1007/s00431-025-06485-y |
| Epidemiology by BW/GA | PDA affected **~65%** of VLBW infants (**<1,500 g**); hsPDA prevalence may reach **~50%** in infants **<28 weeks**. In the prospective cohort, **85/98** had PDA at **24 h**, and **30/98** progressed to hsPDA. (chen2025combinationofechocardiography pages 1-2) | Prospective cohort, GA **≤32 weeks**, BW **≤1,500 g** | Chen 2025, *Frontiers in Pediatrics* | https://doi.org/10.3389/fped.2025.1616706 |
| Echo/hemodynamic markers | Infants progressing to hsPDA had larger **DA diameter**, higher **DA diameter/weight ratio** at **48 and 72 h**, higher **LA/Ao** at **24, 48, and 72 h**; systemic hemodynamics showed increased **stroke index**, **cardiac output index**, **TBW%**, and reduced **TPRI** at **48–72 h**. (chen2025combinationofechocardiography pages 1-2) | Same Chen cohort; serial echo + NICaS monitoring in first 72 h | Chen 2025, *Frontiers in Pediatrics* | https://doi.org/10.3389/fped.2025.1616706 |
| Independent risk factors/prediction | Independent predictors of hsPDA included **maternal eclampsia/preeclampsia**, **surfactant use**, **DA diameter/weight ratio**, **LA/Ao**, and **TBW%** at **48–72 h**. Combined echo + hemodynamic model performance: **AUC 0.981**, **sensitivity 100%**, **specificity 90.0%**. (chen2025combinationofechocardiography pages 1-2) | Same Chen cohort | Chen 2025, *Frontiers in Pediatrics* | https://doi.org/10.3389/fped.2025.1616706 |
| Outcome associations | **Non-hsPDA** carried a **15-fold** higher risk of death vs no PDA; by contrast, mortality risk in **hsPDA** was similar to no PDA in adjusted analyses. (chesi2024patentductusarteriosus pages 1-2, chesi2024patentductusarteriosus pages 10-11, chesi2024patentductusarteriosus pages 11-13) | Multicenter VLBW cohort | Chesi 2024, *PLOS ONE* | https://doi.org/10.1371/journal.pone.0306769 |
| Outcome associations | **BPD** occurrence was **6-fold** higher with hsPDA vs no PDA; when both systemic hypoperfusion and pulmonary overcirculation were present, risk of **grade ≥3 IVH** increased **8.7-fold** and **grade ≥3 ROP** increased **18-fold**. (chesi2024patentductusarteriosus pages 1-2, chesi2024patentductusarteriosus pages 10-11, chesi2024patentductusarteriosus pages 11-13) | Multicenter VLBW cohort | Chesi 2024, *PLOS ONE* | https://doi.org/10.1371/journal.pone.0306769 |


*Table: This table condenses recent, quantitative evidence for defining hemodynamically significant PDA, estimating risk by prematurity, and interpreting echocardiographic/hemodynamic predictors and outcome associations. It is designed as a compact knowledge-base-ready summary anchored to recent cohort studies and diagnostic comparisons.*

---

## Key gaps and uncertainties (evidence-based)
- **Definition instability:** hsPDA remains definitionally unstable across criteria and timepoints, affecting who is treated and when. (dani2025diagnosisofpatent pages 1-2)
- **Outcome causality vs association:** Strong associations between PDA categories and prematurity morbidities exist, but randomized evidence summarized in reviews has not consistently shown improved long-term outcomes with early medical closure vs expectant approaches, motivating ongoing trials and physiology-guided strategies. (trahan2025patentductusarteriosus pages 2-4, francescato2023transcatheterclosurein pages 1-2)
- **Genetic architecture:** Mechanistic causality is strong in some developmental gene models (e.g., PRDM6), while human neonatal genetic association results are emerging and may be population- and phenotype-definition dependent. (zou2023prdm6drivesductus pages 1-2, minta2025associationbetweengenetic pages 1-2)


References

1. (chen2025combinationofechocardiography pages 1-2): Cuie Chen, Yuechong Cui, Shujun Chen, Jiaonv Chen, Lirong Zhao, Yuanyuan Sun, Liuqing Ji, and Guoliang Wang. Combination of echocardiography with systemic hemodynamic parameters for early risk stratification of hemodynamically significant patent ductus arteriosus in preterm infants. Frontiers in Pediatrics, Sep 2025. URL: https://doi.org/10.3389/fped.2025.1616706, doi:10.3389/fped.2025.1616706. This article has 0 citations.

2. (dani2025diagnosisofpatent pages 1-2): Carlo Dani, Davide Sarcina, Iuri Corsini, Simone Pratesi, Chiara Poggi, Simona Montano, Barbara Loi, Giulia Regiroli, and Daniele De Luca. Diagnosis of patent ductus arteriosus by different echocardiographic methods in very preterm infants. European Journal of Pediatrics, Sep 2025. URL: https://doi.org/10.1007/s00431-025-06485-y, doi:10.1007/s00431-025-06485-y. This article has 3 citations and is from a peer-reviewed journal.

3. (trahan2025patentductusarteriosus pages 4-5): Kimberly Fernandez Trahan, Elaine L. Shelton, and Maria Gillam-Krakauer. Patent ductus arteriosus in extremely preterm infants: update on current diagnostic and treatment options. Current Treatment Options in Cardiovascular Medicine, Jul 2025. URL: https://doi.org/10.1007/s11936-025-01101-6, doi:10.1007/s11936-025-01101-6. This article has 3 citations and is from a peer-reviewed journal.

4. (baruteau2024deviceclosureof pages 1-2): Alban-Elouen Baruteau, Mathilde Méot, Nadir Benbrik, Céline Grunenwald, Naychi Lwin, Juliana Patkai, Jean-Christophe Rozé, Damien Bonnet, and Sophie Malekzadeh-Milani. Device closure of hemodynamically significant patent ductus arteriosus in premature infants. JACC: Advances, 3:101211, Oct 2024. URL: https://doi.org/10.1016/j.jacadv.2024.101211, doi:10.1016/j.jacadv.2024.101211. This article has 16 citations.

5. (cucerea2025serumbiomarkersin pages 1-2): Manuela Cucerea, Raluca Marian, Marta Simon, Madalina Anciuc-Crauciuc, Andreea Racean, Andrea Toth, Zsuzsánna Simon-Szabó, Mihaela-Georgiana Fadur, Valeriu Moldovan, and Elena Moldovan. Serum biomarkers in patent ductus arteriosus in preterm infants: a narrative review. Biomedicines, 13:670, Mar 2025. URL: https://doi.org/10.3390/biomedicines13030670, doi:10.3390/biomedicines13030670. This article has 4 citations.

6. (ursino2025treocapaprophylactictreatment pages 1-2): Moreno Ursino, Corinne Alberti, Gilles Cambonie, Ruth Kemp, Aure Vanhecke, Lea Levoyer, Alpha Diallo, Mikko Hallman, Jean-Christophe Rozé, Corine Alberti, Ricardo Carbajal, Pierre Kuhn, Alban Baruteau, Andrei Morgan, Pierre-Yves Ancel, Jennifer Zeilin, Naim Bouazza, Olivier Baud, Olivier Claris, Jean-Charles Picaud, Pierre-Henri Jarreau, Gene Dempsey, Naouel Bouafia, Regis Hankard, Tobias Muehlbacher, Aline Rideau, Kevin Leduc, Sebastien Joye, Cyril Flamant, Geraldine Gascoin, Isabelle Ligi, Juliana Patkai, Charlotte Kruse, Heloise Torchin, Pille Andresson, Antoine Bouissou, Elisa Proenca, Marine Vincent, Evgeniya Babacheva, Nadia Mazille, Magali Reynold De Seresin, Mirka Lumia, Christoph Rüegger, Claudia Knoepfli, Marco Bartocci, Georgi Nellis, Kim Nguyen, Ulla Sankilampi, Vincent Rigo, Francisca Barcos, Christoph Binder, Laure Simon, Hanna Soukka, Arnaud Callies, Maria Fintzou, Andre Graça, Marina Malakozi, Marie Moreau, Anne Murray, Katja Ovaskainen, Sauli Palmu, Manon Tauzin, Outi Aikio, Siw Helen Eger, Barthelemy Tosello, Louis Baraton, Alain Beuchee, Susanne Kirschenhofer, Kelly Mellul, Gaelle Sorin, Ludovic Treluyer, David Healy, Mari Liis Ilmoja, Elsa Kermorvant, Vito Mondì, Dimitrios Rallis, Nuria Torre, Helene Yager, Elodie Zana-Taieb, Laure Carneiro, Cecile Cipierre, Araceli Corredera, Gilles Dassieu, Rim Debbiche, Fabrice Decobert, Leif Evaggelidis, Aurelie Garbi, Maarja Hallik, Emilie Jourdes, Claire Langlet Muteau, Bertrand Leboucher, Jurate Panaviene, Marion Plourde, Outi Tammela, Geraldine Apprioual, Clemence Auzet, Claire Bellanger, Melinda Benard, Valerie Biran, Farid Boubred, Marine Butin, Melissa David, Marie Amelie Detristan, Odile Dicky, Laurence Dillenseger, Izaskun Dorronsoro, Xavier Durrmeyer, Sophie Laborie, Carine Lallemant, Noemie Lefevre, Sandra Lescure, Nathalie Montjaux, Corinne Ragouilliaux, Marta Sarda, Helene Schieber, Hans Jorgen Stensvold, Kenneth Strommen, Joao Virtuoso, Noura Zayat, Julie Abbal, Nahla Ahmed, Alberto Berenguer, Roberto Chioma, Yshwarya Stapleton, Sophie Delorme, Elodie Garnier, Joana Gil, Raquel Gouveia, Isabelle Grand Vuillemin, Shushanik Hovhannisyan, Andrei Morgan, Piermichele Paoulillo, Chiara Passarella, Anne Sophie Pellot, Simonetta Picone, Nikolaos Podimatas, Ana Rita Prior, Monica Rebelo, Angela Sainz, Edmundo Santos, Juliette Suhard, Camille Theveniaut, Tiina Ukkonen, and Mathilde Yverneau. Treocapa: prophylactic treatment of the ductus arteriosus in preterm infants by acetaminophen—statistical analysis plan for the randomized phase iii group sequential trial. Trials, Feb 2025. URL: https://doi.org/10.1186/s13063-025-08751-8, doi:10.1186/s13063-025-08751-8. This article has 5 citations and is from a peer-reviewed journal.

7. (luo2024theimpactof pages 1-2): Hanwen Luo, Jianghua He, Xiaoming Xu, Hongju Chen, and Jing Shi. The impact of the route of administration on the efficacy and safety of the drug therapy for patent ductus arteriosus in premature infants: a systematic review and meta-analysis. PeerJ, 12:e16591, Jan 2024. URL: https://doi.org/10.7717/peerj.16591, doi:10.7717/peerj.16591. This article has 6 citations and is from a peer-reviewed journal.

8. (pugnaloni2024ductusarteriosusin pages 5-8): Flaminia Pugnaloni, Daniela Doni, Mariella Lucente, Stefano Fiocchi, and Irma Capolupo. Ductus arteriosus in fetal and perinatal life. Journal of Cardiovascular Development and Disease, 11:113, Apr 2024. URL: https://doi.org/10.3390/jcdd11040113, doi:10.3390/jcdd11040113. This article has 17 citations.

9. (chesi2024patentductusarteriosus pages 1-2): Elena Chesi, Katia Rossi, Gina Ancora, Cecilia Baraldi, Mara Corradi, Francesco Di Dio, Giorgia Di Fazzio, Silvia Galletti, Giovanna Mescoli, Irene Papa, Agostina Solinas, Luca Braglia, Antonella Di Caprio, Riccardo Cuoghi Costantini, Francesca Miselli, Alberto Berardi, and Giancarlo Gargano. Patent ductus arteriosus (also non-hemodynamically significant) correlates with poor outcomes in very low birth weight infants. a multicenter cohort study. PLOS ONE, 19:e0306769, Jul 2024. URL: https://doi.org/10.1371/journal.pone.0306769, doi:10.1371/journal.pone.0306769. This article has 11 citations and is from a peer-reviewed journal.

10. (zou2023prdm6drivesductus pages 1-2): Meng Zou, Kevin D. Mangum, Justin C. Magin, Heidi H. Cao, Michael T. Yarboro, Elaine L. Shelton, Joan M. Taylor, Jeff Reese, Terrence S. Furey, and Christopher P. Mack. Prdm6 drives ductus arteriosus closure by promoting ductus arteriosus smooth muscle cell identity and contractility. JCI Insight, Mar 2023. URL: https://doi.org/10.1172/jci.insight.163454, doi:10.1172/jci.insight.163454. This article has 13 citations and is from a domain leading peer-reviewed journal.

11. (minta2025associationbetweengenetic pages 1-2): Marcin Minta, Grażyna Kurzawińska, Zuzanna-Banach Minta, Agnieszka Seremak Mrozikiewicz, and Dawid Szpecht. Association between genetic polymorphisms in the prostaglandin pathway and the development of patent ductus arteriosus in preterm infants. International Journal of Molecular Sciences, 26:9274, Sep 2025. URL: https://doi.org/10.3390/ijms26199274, doi:10.3390/ijms26199274. This article has 0 citations.

12. (chesi2024patentductusarteriosus pages 2-4): Elena Chesi, Katia Rossi, Gina Ancora, Cecilia Baraldi, Mara Corradi, Francesco Di Dio, Giorgia Di Fazzio, Silvia Galletti, Giovanna Mescoli, Irene Papa, Agostina Solinas, Luca Braglia, Antonella Di Caprio, Riccardo Cuoghi Costantini, Francesca Miselli, Alberto Berardi, and Giancarlo Gargano. Patent ductus arteriosus (also non-hemodynamically significant) correlates with poor outcomes in very low birth weight infants. a multicenter cohort study. PLOS ONE, 19:e0306769, Jul 2024. URL: https://doi.org/10.1371/journal.pone.0306769, doi:10.1371/journal.pone.0306769. This article has 11 citations and is from a peer-reviewed journal.

13. (mukherjee2025…paracetamoland pages 57-62): A Mukherjee. … paracetamol and ibuprofen research) trial: a comparative study on the use of paracetamol versus ibuprofen in treating patent ductus arteriosus in premature infants. Unknown journal, 2025.

14. (minta2025associationbetweengenetic pages 7-9): Marcin Minta, Grażyna Kurzawińska, Zuzanna-Banach Minta, Agnieszka Seremak Mrozikiewicz, and Dawid Szpecht. Association between genetic polymorphisms in the prostaglandin pathway and the development of patent ductus arteriosus in preterm infants. International Journal of Molecular Sciences, 26:9274, Sep 2025. URL: https://doi.org/10.3390/ijms26199274, doi:10.3390/ijms26199274. This article has 0 citations.

15. (chesi2024patentductusarteriosus media 56412072): Elena Chesi, Katia Rossi, Gina Ancora, Cecilia Baraldi, Mara Corradi, Francesco Di Dio, Giorgia Di Fazzio, Silvia Galletti, Giovanna Mescoli, Irene Papa, Agostina Solinas, Luca Braglia, Antonella Di Caprio, Riccardo Cuoghi Costantini, Francesca Miselli, Alberto Berardi, and Giancarlo Gargano. Patent ductus arteriosus (also non-hemodynamically significant) correlates with poor outcomes in very low birth weight infants. a multicenter cohort study. PLOS ONE, 19:e0306769, Jul 2024. URL: https://doi.org/10.1371/journal.pone.0306769, doi:10.1371/journal.pone.0306769. This article has 11 citations and is from a peer-reviewed journal.

16. (chesi2024patentductusarteriosus media 692abe13): Elena Chesi, Katia Rossi, Gina Ancora, Cecilia Baraldi, Mara Corradi, Francesco Di Dio, Giorgia Di Fazzio, Silvia Galletti, Giovanna Mescoli, Irene Papa, Agostina Solinas, Luca Braglia, Antonella Di Caprio, Riccardo Cuoghi Costantini, Francesca Miselli, Alberto Berardi, and Giancarlo Gargano. Patent ductus arteriosus (also non-hemodynamically significant) correlates with poor outcomes in very low birth weight infants. a multicenter cohort study. PLOS ONE, 19:e0306769, Jul 2024. URL: https://doi.org/10.1371/journal.pone.0306769, doi:10.1371/journal.pone.0306769. This article has 11 citations and is from a peer-reviewed journal.

17. (chesi2024patentductusarteriosus pages 10-11): Elena Chesi, Katia Rossi, Gina Ancora, Cecilia Baraldi, Mara Corradi, Francesco Di Dio, Giorgia Di Fazzio, Silvia Galletti, Giovanna Mescoli, Irene Papa, Agostina Solinas, Luca Braglia, Antonella Di Caprio, Riccardo Cuoghi Costantini, Francesca Miselli, Alberto Berardi, and Giancarlo Gargano. Patent ductus arteriosus (also non-hemodynamically significant) correlates with poor outcomes in very low birth weight infants. a multicenter cohort study. PLOS ONE, 19:e0306769, Jul 2024. URL: https://doi.org/10.1371/journal.pone.0306769, doi:10.1371/journal.pone.0306769. This article has 11 citations and is from a peer-reviewed journal.

18. (francescato2023transcatheterclosurein pages 1-2): Gaia Francescato, Daniela Doni, Giuseppe Annoni, Irma Capolupo, Elena Ciarmoli, Iuri Corsini, Italo Francesco Gatelli, Sabrina Salvadori, Alberto Testa, and Gianfranco Butera. Transcatheter closure in preterm infants with patent ductus arteriosus: feasibility, results, hemodynamic monitoring and future prospectives. Italian Journal of Pediatrics, Nov 2023. URL: https://doi.org/10.1186/s13052-023-01552-2, doi:10.1186/s13052-023-01552-2. This article has 7 citations and is from a peer-reviewed journal.

19. (NCT04205877 chunk 1): Shyam K. Sathanandam, MD. The U.S. PDA Registry. Le Bonheur Children's Hospital. 2020. ClinicalTrials.gov Identifier: NCT04205877

20. (NCT06587282 chunk 1):  PREEMIE: Study for Treatment of PDA in Premature Infants. Merit Medical Systems, Inc.. 2025. ClinicalTrials.gov Identifier: NCT06587282

21. (NCT06601114 chunk 1): Arooj Khan. The Effectiveness of Paracetamol Versus Ibuprofen in Management of Patent Ductus Arteriosus in Preterm Neonates. Arooj Khan. 2024. ClinicalTrials.gov Identifier: NCT06601114

22. (chesi2024patentductusarteriosus pages 11-13): Elena Chesi, Katia Rossi, Gina Ancora, Cecilia Baraldi, Mara Corradi, Francesco Di Dio, Giorgia Di Fazzio, Silvia Galletti, Giovanna Mescoli, Irene Papa, Agostina Solinas, Luca Braglia, Antonella Di Caprio, Riccardo Cuoghi Costantini, Francesca Miselli, Alberto Berardi, and Giancarlo Gargano. Patent ductus arteriosus (also non-hemodynamically significant) correlates with poor outcomes in very low birth weight infants. a multicenter cohort study. PLOS ONE, 19:e0306769, Jul 2024. URL: https://doi.org/10.1371/journal.pone.0306769, doi:10.1371/journal.pone.0306769. This article has 11 citations and is from a peer-reviewed journal.

23. (trahan2025patentductusarteriosus pages 2-4): Kimberly Fernandez Trahan, Elaine L. Shelton, and Maria Gillam-Krakauer. Patent ductus arteriosus in extremely preterm infants: update on current diagnostic and treatment options. Current Treatment Options in Cardiovascular Medicine, Jul 2025. URL: https://doi.org/10.1007/s11936-025-01101-6, doi:10.1007/s11936-025-01101-6. This article has 3 citations and is from a peer-reviewed journal.