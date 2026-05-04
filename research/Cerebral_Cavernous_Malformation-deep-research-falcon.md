---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-04T18:26:49.305894'
end_time: '2026-05-04T18:49:11.462815'
duration_seconds: 1342.16
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Cerebral Cavernous Malformation
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 63
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Cerebral Cavernous Malformation
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Cerebral Cavernous Malformation** covering all of the
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
- **Disease Name:** Cerebral Cavernous Malformation
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Cerebral Cavernous Malformation** covering all of the
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


# Cerebral Cavernous Malformation (CCM): Disease Characteristics Research Report (2023–2024 emphasis)

## Executive summary
Cerebral cavernous malformation (CCM) is a cerebrovascular disorder characterized by clusters of thin-walled, dilated capillary/capillary–venous channels lined by a single endothelial layer with deficient mural support and barrier dysfunction, predisposing to microbleeds and intracranial hemorrhage. (min2023endothelialcellpericyteinteractions pages 1-2, montagnoli2023therapeuticperspectiveson pages 2-4, montagnoli2023therapeuticperspectiveson pages 1-2)
The Mendelian (familial) form is typically autosomal dominant with incomplete penetrance and is caused by loss-of-function variants in KRIT1 (CCM1), CCM2, or PDCD10 (CCM3), consistent with a two-hit lesion model in which somatic biallelic loss occurs in lesion-forming endothelial cells. (min2023endothelialcellpericyteinteractions pages 1-2, shapeti2024forcemediatedangiogenesislinking pages 39-43)
Recent 2023–2024 literature emphasizes convergent endothelial signaling nodes—MEKK3–MEK5–ERK5–KLF2/4, RhoA/ROCK, EndMT, oxidative stress/redox and autophagy defects, ECM (hyaluronic acid/versican)–dependent modulation, and gut microbiome–linked inflammatory signaling—while clinical translational efforts increasingly rely on susceptibility-based MRI biomarkers (e.g., SWI/QSM) and pilot clinical trials of repurposed or novel agents. (abdelilahseyfried2024arenaissanceof pages 1-3, ayata2024roleofrhoassociated pages 1-2, perrelli2023krit1atraffic pages 15-16, yordanov2024hyaluronicacidturnover pages 1-3, srinath2023plasmametaboliteswith pages 2-3, NCT02603328 chunk 1)

---

## 1. Disease information
### 1.1 What is the disease?
CCMs are vascular lesions described as “clusters of enlarged, dilated capillary channels formed by a single layer of endothelium,” lacking key supporting elements (smooth muscle/pericytes, intact basal lamina), leading to thin, leaky vessels. (min2023endothelialcellpericyteinteractions pages 1-2, montagnoli2023therapeuticperspectiveson pages 2-4)
A 2023 review describes CCMs as “developmental venous dysplasias” and emphasizes that lesions are angiographically occult and typically detected by MRI. (montagnoli2023therapeuticperspectiveson pages 1-2)

### 1.2 Key identifiers
- **MONDO (from OpenTargets):**
  - Cerebral cavernous malformation: **MONDO:0000820** (abdelilahseyfried2024arenaissanceof pages 1-3)
  - Familial cerebral cavernous malformations: **MONDO:0031037** (abdelilahseyfried2024arenaissanceof pages 1-3)
  - Cerebral cavernous malformation 1 (KRIT1-related): **MONDO:0020724** (abdelilahseyfried2024arenaissanceof pages 1-3)

**Not retrieved in current tool context:** OMIM / Orphanet / ICD-10 / ICD-11 / MeSH identifiers were not directly accessible via the tool outputs used here; MONDO IDs above are provided as stable ontology identifiers for knowledge base linkage.

### 1.3 Synonyms / alternative names
Common synonyms include **cavernous malformation**, **cavernoma**, **cavernous angioma**, and **cavernous hemangioma**. (shapeti2024forcemediatedangiogenesislinking pages 39-43, montagnoli2023therapeuticperspectiveson pages 1-2)
“CASH” (cavernous angioma with symptomatic hemorrhage) is commonly used to denote a clinically aggressive/symptomatic hemorrhage subgroup, especially in biomarker studies. (srinath2023plasmametaboliteswith pages 1-2)

### 1.4 Evidence source type
Information in this report comes from:
- **Aggregated disease-level resources and reviews** (mechanisms, diagnostic standards). (min2023endothelialcellpericyteinteractions pages 1-2, abdelilahseyfried2024arenaissanceof pages 1-3, perrelli2023krit1atraffic pages 1-3)
- **Human cohorts** (natural history, risk factors, medication associations). (gillespie2023predictorsoffuture pages 1-2, santos2023naturalcourseof pages 3-4, alalfi2023clinicalpresentationhemorrhage pages 2-3, zuurbier2023femalehormonetherapy pages 3-5)
- **Model organism / in vitro / engineered human vessel models** (mechanistic dissection; preclinical interventions). (min2023endothelialcellpericyteinteractions pages 1-2, grdseloff2023impairedretinoicacid pages 4-5, grdseloff2023impairedretinoicacid pages 6-7, yordanov2024hyaluronicacidturnover pages 1-3)
- **ClinicalTrials.gov records** (ongoing/completed interventional studies). (NCT05085561 chunk 1, NCT02603328 chunk 1, NCT03589014 chunk 2)

---

## 2. Etiology
### 2.1 Disease causal factors
#### Mendelian familial CCM
Inherited CCM is attributed to loss-of-function mutations in **CCM1/KRIT1, CCM2, and CCM3/PDCD10** (autosomal dominant), with endothelial cell–intrinsic biology central to lesion formation. (min2023endothelialcellpericyteinteractions pages 1-2, abdelilahseyfried2024arenaissanceof pages 1-3)

#### Two-hit (and “third-hit”) lesion biology
A “two-hit” mechanism is supported for familial CCM: germline heterozygous loss plus **somatic biallelic loss** in lesion-forming endothelial cells/clones. (shapeti2024forcemediatedangiogenesislinking pages 39-43, min2023endothelialcellpericyteinteractions pages 1-2)
More recent models highlight additional somatic drivers: co-occurring **PIK3CA gain-of-function** with CCM loss-of-function alleles and **MAP3K3/MEKK3** alterations are discussed as accelerating lesion growth (“third-hit/cooperating driver” concept). (abdelilahseyfried2024arenaissanceof pages 1-3, shapeti2024forcemediatedangiogenesislinking pages 39-43)

### 2.2 Risk factors
#### Genetic risk factors
- Germline loss-of-function in **KRIT1, CCM2, PDCD10** for familial CCM. (min2023endothelialcellpericyteinteractions pages 1-2)
- Pediatric familial CCM cohort suggests higher 5-year cumulative hemorrhage risk in those with **CCM2 genotype (33.3%)** and prior symptomatic hemorrhage (33.3%). (geraldo2023naturalhistoryof pages 1-2)

#### Environmental/medication/physiologic risk factors
- **Female hormone therapy** exposure was associated with increased subsequent intracranial hemorrhage risk in a prospective multicenter cohort (adjusted HR 1.56; oral contraceptives age 10–44 adjusted HR 2.00). (zuurbier2023femalehormonetherapy pages 3-5)
- In a conservative cohort, symptomatic hemorrhage at presentation and lesion localization (brainstem/spinal) are strong predictors of future bleeding. (gillespie2023predictorsoffuture pages 1-2, santos2023naturalcourseof pages 3-4)

### 2.3 Protective factors
Definitive protective environmental factors were not established in the extracted texts. Some observational studies hypothesize protective medication associations (e.g., antithrombotics/beta-blockers in some cohorts), but evidence is inconsistent and not sufficient here to assert protective effects as generalizable. (montagnoli2023therapeuticperspectiveson pages 2-4)

### 2.4 Gene–environment interactions
Gut microbiome–linked inflammatory signaling has been proposed to interface with endothelial signaling in cavernous angioma/CCM, including “TLR4-MEKK3-KLF2/4 signaling, driven by the gut microbiome via gram-negative bacterial lipopolysaccharide.” (srinath2023plasmametaboliteswith pages 11-13)

---

## 3. Phenotypes
### 3.1 Core clinical phenotypes and suggested HPO terms
Below, “HPO suggestions” are ontology recommendations; exact HPO IDs should be verified against the HPO browser.

1) **Intracranial hemorrhage / symptomatic hemorrhage** (clinical sign/outcome)
- HPO suggestions: *Intracranial hemorrhage*; *Cerebral hemorrhage*.
- Frequency/risk examples:
  - Overall annual symptomatic hemorrhage rate **1.00% per lesion-year** in a 545-patient cohort; higher when symptomatic at presentation (**1.50%** vs **0.29%**). (gillespie2023predictorsoffuture pages 1-2)
  - Conservatively managed 10-year cohort: overall 10-year cumulative risk **30%**; brainstem 10-year risk **33%**; spinal 10-year risk **67%**; asymptomatic **0%**. (santos2023naturalcourseof pages 3-4)
  - Pediatric familial cohort: 5-year cumulative symptomatic hemorrhage risk **17.1%** (higher with prior hemorrhage or CCM2 genotype). (geraldo2023naturalhistoryof pages 1-2)

2) **Seizures / epilepsy** (symptom)
- HPO suggestions: *Seizure*; *Epilepsy*.
- Frequency examples:
  - Familial cohort: seizures at presentation **22.7%**; total ever seizure burden **32%** over follow-up; new seizure disorder occurred in 7 patients. (alalfi2023clinicalpresentationhemorrhage pages 2-3)
  - 10-year conservatively managed cohort reported baseline cavernoma-related epilepsy **28.6%**. (santos2023naturalcourseof pages 3-4)
  - Pediatric familial cohort: seizures at last follow-up **29.3%**; refractory in **16.7%** of those with seizures (2/12). (geraldo2023naturalhistoryof pages 4-5)

3) **Focal neurologic deficits** (clinical sign)
- HPO suggestions: *Focal neurological deficit*; potentially *Hemiparesis* / *Ataxia* depending on location.
- Strongly associated with hemorrhagic events and lesion location (e.g., brainstem/spinal); quantitative deficit rates were not extracted in the provided texts.

4) **Lesion multiplicity** (imaging phenotype)
- HPO suggestions: *Multiple cerebral cavernous malformations* (verify exact term).
- Examples:
  - 545-patient cohort: **15.0%** had multiple lesions. (gillespie2023predictorsoffuture pages 1-2)
  - 10-year cohort: multiple CM in **49.5%**; familial disease in **28.6%**. (santos2023naturalcourseof pages 2-3)

### 3.2 Age of onset and progression
Familial CCM can present in childhood; pediatric familial cohort median age at presentation **7.7 years** and demonstrated clinically relevant hemorrhage and seizure burden during follow-up. (geraldo2023naturalhistoryof pages 4-5)
Clinical course is heterogeneous: a 10-year untreated follow-up cohort observed increasing cumulative hemorrhage probability over time, especially after bleeding at presentation and with spinal localization. (santos2023naturalcourseof pages 1-2)

### 3.3 Quality of life impact
Formal QoL instruments were not extracted from cohort papers in this evidence set; however, major QoL impacts are implied by hemorrhage, seizure burden, and neurologic deficits. Trials increasingly incorporate patient-reported outcomes and functional scales (e.g., CCM Health Index; mRS). (NCT05085561 chunk 1)

---

## 4. Genetic / molecular information
### 4.1 Causal genes (familial CCM; Mendelian)
Familial CCM is associated with loss-of-function variants in:
- **KRIT1 (CCM1)**
- **CCM2**
- **PDCD10 (CCM3)** (min2023endothelialcellpericyteinteractions pages 1-2, abdelilahseyfried2024arenaissanceof pages 1-3)

### 4.2 Pathogenic variants (examples from retrieved primary papers)
- **KRIT1 c.1119dupT (p.L374Sfs*9)** frameshift predicted to generate truncated protein (familial CCM family). (abdelilahseyfried2024arenaissanceof pages 1-3)
- **KRIT1 c.1159C>T (p.Q387X)** nonsense variant causing premature termination (hereditary CCM family). (geraldo2023naturalhistoryof pages 1-2)

Variant classification per ACMG/AMP was referenced in a case report for KRIT1 truncation (deleterious under ACMG/AMP 2015), but population allele frequencies were not extracted here. (geraldo2023naturalhistoryof pages 1-2)

### 4.3 Modifier genes / additional somatic drivers
Somatic **PIK3CA** gain-of-function variants and altered **MAP3K3/MEKK3** signaling are discussed as lesion drivers/accelerators in modern CCM biology. (abdelilahseyfried2024arenaissanceof pages 1-3, ayata2024roleofrhoassociated pages 1-2, shapeti2024forcemediatedangiogenesislinking pages 39-43)

### 4.4 Epigenetic information / chromosomal abnormalities
Not specifically reported in extracted evidence.

---

## 5. Environmental information
Direct environmental toxicant/radiation exposures were not comprehensively extracted. A 2023 review notes prior radiotherapy is associated with increased CCM prevalence (reported as a 6-fold increase in that review), supporting radiation-induced CCM as a distinct context. (montagnoli2023therapeuticperspectiveson pages 2-4)
Lifestyle/microbiome axis: biomarker studies link cavernous angioma/CCM to a permissive gut microbiome and “leaky gut” concept with inflammatory signaling (TLR4–MEKK3–KLF2/4) proposed to influence disease activity. (srinath2023plasmametaboliteswith pages 1-2, srinath2023plasmametaboliteswith pages 11-13)

---

## 6. Mechanism / pathophysiology
### 6.1 Core causal chain (current synthesis)
**Initiating genetic lesions** (germline CCM gene LOF ± somatic “second hit,” sometimes with additional somatic “third-hit” drivers) lead to **endothelial signaling dysregulation**. This includes gain/overactivation of **MEKK3–MEK5–ERK5** signaling with induction of **KLF2/KLF4**, promoting maladaptive endothelial transcriptional programs and endothelial-to-mesenchymal transition (EndMT), with downstream barrier dysfunction and bleeding. (abdelilahseyfried2024arenaissanceof pages 1-3, ayata2024roleofrhoassociated pages 1-2, shapeti2024forcemediatedangiogenesislinking pages 39-43)
In parallel, loss of CCM complex function can cause **RhoA/ROCK overactivation**, stress fiber formation, junction instability, and a ROCK2-associated senescence-associated secretory phenotype (SASP) characterized by inflammation, leukocyte chemotaxis, and extracellular matrix degradation. (ayata2024roleofrhoassociated pages 1-2)
These processes converge on **blood–brain barrier disruption**, vascular hyperpermeability, hemosiderin deposition, and clinical manifestations (microbleeds, hemorrhage, seizures, focal deficits). (montagnoli2023therapeuticperspectiveson pages 2-4, montagnoli2023therapeuticperspectiveson pages 1-2)

### 6.2 Pathways and processes (with suggested ontology terms)
#### A) MEKK3–MEK5–ERK5–KLF2/4 axis and EndMT
A 2024 commentary summarizes: “Activation of MEKK3 triggers MEK5 and ERK5 signaling, which then induces expression of KLF2 and KLF4,” and “excessive KLF2/4 activation is necessary to cause CCM-like phenotypes and induce bleeding.” (abdelilahseyfried2024arenaissanceof pages 1-3)
- Suggested GO biological processes: *response to fluid shear stress*; *endothelial cell differentiation*; *endothelial-to-mesenchymal transition*.

#### B) RhoA/ROCK cytoskeletal/junctional dysfunction
A 2024 review states that a common downstream process of CCM gene LOF is “overactivation of RhoA and its effector Rho-associated kinase (ROCK)” leading to “formation of stress fibers that contribute to endothelial junction instability.” (ayata2024roleofrhoassociated pages 1-2)
- Suggested GO processes: *actin cytoskeleton organization*; *regulation of endothelial barrier establishment*.

#### C) Redox signaling, oxidative stress, inflammation, and autophagy
A 2023 redox-focused review states that KRIT1 loss-of-function is linked to impaired redox homeostasis and increased sensitivity to oxidative stress and inflammation, and that KRIT1 helps “maintain endothelial barrier integrity by stabilizing adherens junctions and suppressing actin stress fiber formation.” (perrelli2023krit1atraffic pages 1-3)
It further states there is “compelling evidence that KRIT1 deficiency exerts pleiotropic effects… by affecting key redox-sensitive molecular pathways… against oxidative stress and inflammation,” and that KRIT1 LOF phenotypes are rescuable by antioxidant compounds and pro-autophagic mTOR inhibitors (e.g., rapamycin). (perrelli2023krit1atraffic pages 6-7)
- Suggested GO processes: *response to oxidative stress*; *autophagy*; *inflammatory response*.

#### D) Retinoic acid signaling dysregulation and dose-dependent therapeutic effects
A 2023 Scientific Reports study concludes: “components of the retinoic acid synthesis and degradation pathway are transcriptionally misregulated across disease models of CCM,” and that high-dose retinoic acid worsened lesions in an adult chronic mouse model, highlighting regimen sensitivity. (grdseloff2023impairedretinoicacid pages 1-2)
Model-specific findings include beneficial effects in siCCM2 HUVECs and krit1 mutant zebrafish when RA levels were increased, but worsened lesion burden/hemorrhage at ~20 mg/kg/day RA dosing in chronic mouse CCM. (grdseloff2023impairedretinoicacid pages 7-9, grdseloff2023impairedretinoicacid pages 6-7)
- Suggested GO process: *retinoid metabolic process* (explicitly enriched in the paper’s analyses). (grdseloff2023impairedretinoicacid pages 4-5)

#### E) Extracellular matrix (ECM) modulation: hyaluronic acid turnover
A 2024 engineered human microvessel study reports CCM endothelial hallmarks (“overactive MEKK3 kinase and KLF2/4 transcription factor signaling”) and finds that supplementing ECM with distinct hyaluronic acid forms “inhibits pathological cell spreading and rescues barrier function,” suggesting ECM composition modulates lesion severity. (yordanov2024hyaluronicacidturnover pages 1-3)
- Suggested GO process: *extracellular matrix organization*.
- Suggested CHEBI terms: *hyaluronic acid* (verify CHEBI ID).

#### F) Endothelial–pericyte interactions (especially CCM3)
A 2023 review reports that “Ccm3 deletion in pericytes (PCs) also induces CCM lesions” and “CCM3 deletion in ECs or PCs destabilizes PC–EC associations,” via mechanisms including angiopoietin-2 exocytosis and impaired pericyte migration, linking mural cell biology to BBB instability. (min2023endothelialcellpericyteinteractions pages 1-2)
- Suggested Cell Ontology terms: *brain microvascular endothelial cell*; *pericyte*.

#### G) Biomarkers / metabolomics / microbiome
A 2023 Communications Medicine metabolomics study identified plasma metabolites distinguishing cavernous angioma/CCM states; it reports a metabolite diagnostic score with **87.5% sensitivity and 89% specificity** (metabolite-only model) and integrative multi-omic models achieving up to **85% sensitivity and 80% specificity**, linking metabolites to inflammatory signaling and microbiome features. (srinath2023plasmametaboliteswith pages 7-9, srinath2023plasmametaboliteswith pages 1-2)

---

## 7. Anatomical structures affected
### 7.1 Organ/tissue/cell level
- Primary: **central nervous system vasculature** (brain; can include spinal cord). (montagnoli2023therapeuticperspectiveson pages 1-2, santos2023naturalcourseof pages 3-4)
- Tissue: microvascular structures with defective endothelial junctions and reduced mural support. (min2023endothelialcellpericyteinteractions pages 1-2, montagnoli2023therapeuticperspectiveson pages 2-4)
- Cell types: endothelial cells are central; pericytes contribute (especially PDCD10/CCM3 contexts). (min2023endothelialcellpericyteinteractions pages 1-2)
- Suggested UBERON terms: *brain*; *cerebral cortex*; *brainstem*; *spinal cord*; *cerebral microvasculature* (verify exact UBERON IDs).

---

## 8. Temporal development
- Course can be asymptomatic for years but may become symptomatic through hemorrhage or seizure onset. (montagnoli2023therapeuticperspectiveson pages 2-4)
- Longitudinal risk increases after an initial hemorrhage and in higher-risk locations (brainstem/spinal). (santos2023naturalcourseof pages 3-4, gillespie2023predictorsoffuture pages 1-2)

---

## 9. Inheritance and population
### 9.1 Inheritance
Familial CCM is described as **autosomal dominant with incomplete penetrance**, caused by germline LOF in KRIT1/CCM1, CCM2, or PDCD10/CCM3. (min2023endothelialcellpericyteinteractions pages 1-2)

### 9.2 Epidemiology
A 2023 review reports prevalence **2–9 per 1,000** and incidence **5–6 new diagnoses per million adults per year**, with pediatric cases comprising **25–35%** of people living with CCM; familial CCM accounts for ~20% of cases in that review. (montagnoli2023therapeuticperspectiveson pages 1-2)

---

## 10. Diagnostics
### 10.1 Imaging
MRI is the primary diagnostic modality. Susceptibility-sensitive sequences (e.g., **SWI/SWAN** or **T2*-GRE**) improve detection and show characteristic “blooming” from hemosiderin. (demir2024giantintracranialcavernous pages 1-2, demir2024giantintracranialcavernous pages 2-3)
A 2024 radiology review describes the classic “popcorn” lesion with a hemosiderin rim and notes classification into types (I–IV), with type IV being punctate hypointense foci best seen on SWI. (demir2024giantintracranialcavernous pages 2-3)
Digital subtraction angiography is generally not recommended for CCM diagnosis except to exclude AVM. (demir2024giantintracranialcavernous pages 2-3)

**Visual evidence (MRI classification and SWI blooming):** Table/figure extracts from Demir et al. 2024 are provided. (demir2024giantintracranialcavernous media cdc7d79b, demir2024giantintracranialcavernous media ee42a4a3)

### 10.2 Differential diagnosis
Familial CCM can mimic cerebral amyloid angiopathy (CAA) on susceptibility imaging; a 2024 Acta Neurochirurgica study emphasizes applying Boston criteria for CAA and proposes FCCM-specific criteria using lesion distribution and Zabramski patterns (e.g., presence of type 2 lesions in FCCM, lesion distribution ratios). (flemming2024clinicalandradiologic pages 5-7, flemming2024clinicalandradiologic pages 1-3)

### 10.3 Genetic testing
The extracted literature supports confirmatory genetic testing for suspected familial CCM syndromes and diagnostic classification based on family history and/or pathogenic CCM1–3 variants, especially in pediatric FCCM cohorts and in FCCM-vs-CAA diagnostic frameworks. (geraldo2023naturalhistoryof pages 1-2, flemming2024clinicalandradiologic pages 7-9)

---

## 11. Outcome / prognosis
Prognosis is driven by hemorrhage recurrence risk, lesion location, and seizure burden.
- In a 545-patient cohort, eloquent location (HR 2.63) and symptomatic hemorrhage at presentation (HR 5.37) strongly predicted future symptomatic hemorrhage. (gillespie2023predictorsoffuture pages 1-2)
- In a complete 10-year follow-up cohort, spinal localization and hemorrhage at diagnosis independently predicted (re)hemorrhage; 10-year cumulative bleeding risk was 30% overall and 67% for intramedullary spinal lesions. (santos2023naturalcourseof pages 1-2, santos2023naturalcourseof pages 3-4)

---

## 12. Treatment
### 12.1 Current real-world clinical management
A 2023 review notes there is “no cure” and that surgical treatment is typically recommended only for superficial cortical lesions, reflecting practical constraints/risks for deeply seated lesions. (montagnoli2023therapeuticperspectiveson pages 1-2)

### 12.2 Pharmacotherapy / targeted approaches (emerging)
There is no FDA- or EU-approved pharmacologic treatment for CCM noted in recent mechanistic reviews; ROCK is a key proposed target with both direct inhibitors (e.g., fasudil) and indirect inhibitors (e.g., statins) showing preclinical efficacy, and clinical studies underway/planned. (ayata2024roleofrhoassociated pages 1-2)

### 12.3 Clinical trials and implementations (selected)
Key interventional trials captured from ClinicalTrials.gov include:
- **REC-994** Phase 2 trial in symptomatic CCM (NCT05085561) evaluating safety and MRI/clinical outcomes. (NCT05085561 chunk 1)
- **Atorvastatin (AT CASH EPOC)** randomized Phase I/II trial (NCT02603328) using **QSM** as a primary endpoint and permeability/mRS/QoL and ROCK activity as secondary endpoints; results were posted on ClinicalTrials.gov in 2025. (NCT02603328 chunk 1)
- **Propranolol** (Treat_CCM; NCT03589014) Phase 2 pilot in familial CCM; a separate preoperative propranolol molecular-response trial (NCT03474614) was terminated due to lack of accrual. (NCT03589014 chunk 2, NCT03474614 chunk 1)

**Suggested MAXO terms (examples; verify IDs):** *microsurgical resection*; *stereotactic radiosurgery*; *magnetic resonance imaging*; *genetic testing*; *statin therapy*; *beta-adrenergic receptor antagonist therapy*.

---

## 13. Prevention
No established primary prevention exists for inherited CCM beyond genetic counseling and avoidance of modifiable risk exposures when evidence supports risk.
- Secondary/tertiary prevention focuses on surveillance and risk reduction (e.g., MRI monitoring; counseling about medications that may increase hemorrhage risk).
- Given observed association of hormone therapy with hemorrhage risk, counseling about oral contraceptives/menopausal hormone therapy may be clinically relevant in women with CCM. (zuurbier2023femalehormonetherapy pages 3-5)

---

## 14. Other species / natural disease
The extracted evidence focuses on experimental models rather than naturally occurring veterinary disease; no OMIA/animal natural disease evidence was retrieved.

---

## 15. Model organisms and experimental systems
- **Mouse models:** acute and chronic CCM2 conditional knockout models were used to test retinoic acid regimens, demonstrating dose- and regimen-dependent effects including worsening at high dose in chronic adult models. (grdseloff2023impairedretinoicacid pages 6-7)
- **Zebrafish models:** krit1/ccm2-related phenotypes respond to RA pathway manipulation (e.g., Cyp26 inhibition/talarozole) with beneficial effects at certain regimens and developmental toxicity at higher RA exposures. (grdseloff2023impairedretinoicacid pages 4-5, grdseloff2023impairedretinoicacid pages 5-6)
- **Human endothelial in vitro models:** siCCM2 HUVECs show RA-responsive rescue of stress fiber/cell morphology with optimal dosing reported (100 nM) but persistent KLF2/4 elevation. (grdseloff2023impairedretinoicacid pages 7-9)
- **Pericyte-specific genetic models:** Ccm3 deletion in pericytes can induce lesions, supporting mural cell contribution beyond endothelial autonomy. (min2023endothelialcellpericyteinteractions pages 1-2)
- **Bioengineered human microvessels (3D microfluidics):** CCM1-deficient human microvessels in distinct ECMs show rescue of barrier function by hyaluronic acid supplementation, highlighting CNS-like ECM influence. (yordanov2024hyaluronicacidturnover pages 1-3)

---

## Structured tables (artifacts)
The following structured tables can be used to populate a disease knowledge base entry.

| Entity | Identifier | Common synonyms / nomenclature | Brief pathology definition |
|---|---|---|---|
| Cerebral cavernous malformation | MONDO:0000820 | cerebral cavernous malformation; cavernous malformation; cavernoma; cavernous angioma; cavernous hemangioma; capillary-venous cavernoma (shapeti2024forcemediatedangiogenesislinking pages 39-43, min2023endothelialcellpericyteinteractions pages 1-2, montagnoli2023therapeuticperspectiveson pages 2-4, montagnoli2023therapeuticperspectiveson pages 1-2) | Low-flow cerebrovascular lesion composed of thin-walled, dilated capillary/capillary-venous channels lined by a single endothelial layer, lacking intervening brain parenchyma and typically deficient in smooth muscle/pericytes with defective/discontinuous basal lamina and a leaky blood-brain barrier prone to edema and hemorrhage (min2023endothelialcellpericyteinteractions pages 1-2, montagnoli2023therapeuticperspectiveson pages 2-4, montagnoli2023therapeuticperspectiveson pages 1-2) |
| Familial cerebral cavernous malformations | MONDO:0031037 | familial cerebral cavernous malformation; familial CCM; FCCM; familial cavernous malformation syndrome (min2023endothelialcellpericyteinteractions pages 1-2, flemming2024clinicalandradiologic pages 1-3) | Inherited form of CCM, usually autosomal dominant, characterized by multiple hemorrhagic cavernous lesions with the same core pathology as CCM and often greater lesion multiplicity/burden (min2023endothelialcellpericyteinteractions pages 1-2, flemming2024clinicalandradiologic pages 1-3, flemming2024clinicalandradiologic pages 7-9) |
| Cerebral cavernous malformation 1 | MONDO:0020724 | CCM1; KRIT1-related cerebral cavernous malformation; cerebral cavernous malformation 1 (abdelilahseyfried2024arenaissanceof pages 1-3, min2023endothelialcellpericyteinteractions pages 1-2) | Gene-defined Mendelian subtype caused by KRIT1 loss-of-function; lesions share the canonical CCM histology of dilated endothelial caverns with barrier failure and hemorrhagic tendency (abdelilahseyfried2024arenaissanceof pages 1-3, min2023endothelialcellpericyteinteractions pages 1-2, perrelli2023krit1atraffic pages 1-3) |
| Cavernous angioma with symptomatic hemorrhage | No MONDO ID established in retrieved evidence | CASH; cavernous angioma with symptomatic hemorrhage; symptomatic hemorrhagic CCM subgroup (srinath2023plasmametaboliteswith pages 7-9, srinath2023plasmametaboliteswith pages 2-3, srinath2023plasmametaboliteswith pages 1-2) | Clinical state referring to CCM/cavernous angioma patients with recent symptomatic lesional bleeding; used particularly in biomarker and trial-readiness studies rather than as a separate pathology entity (srinath2023plasmametaboliteswith pages 7-9, srinath2023plasmametaboliteswith pages 2-3, srinath2023plasmametaboliteswith pages 1-2) |


*Table: This table summarizes the main disease identifiers, synonyms, and pathology wording for cerebral cavernous malformation and closely related named entities. It is useful for standardizing terminology in a disease knowledge base and linking general CCM, familial CCM, CCM1, and the CASH clinical subgroup.*

| Gene / concept | Role in CCM genetics | Inheritance / penetrance | Typical pathogenic mechanism | Example variant(s) from retrieved studies | Somatic / clonal notes | URL / DOI | Evidence |
|---|---|---|---|---|---|---|---|
| **KRIT1 (CCM1)** | One of the 3 core Mendelian familial CCM genes; recent reviews state inherited CCM is caused by loss-of-function variants in **CCM1/KRIT1, CCM2, CCM3/PDCD10** (abdelilahseyfried2024arenaissanceof pages 1-3, min2023endothelialcellpericyteinteractions pages 1-2) | **Autosomal dominant** with **incomplete penetrance** in familial CCM (min2023endothelialcellpericyteinteractions pages 1-2) | Predominantly **loss-of-function** with truncating consequences; KRIT1 loss destabilizes endothelial junction/barrier programs and is central to CCM pathogenesis (perrelli2023krit1atraffic pages 1-3, perrelli2023krit1atraffic pages 3-4) | **c.1119dupT, p.L374Sfs*9** — **frameshift**, predicted truncated KRIT1 protein of 381 aa; **c.1159C>T, p.Q387X** — **nonsense**, premature termination/truncation (variant examples reported in Chinese familial CCM and hereditary CCM studies) | Familial lesions fit a **two-hit model** with germline KRIT1 loss plus **somatic biallelic loss** in lesion-forming endothelial cells/clones (shapeti2024forcemediatedangiogenesislinking pages 39-43, min2023endothelialcellpericyteinteractions pages 1-2, yordanov2024hyaluronicacidturnover pages 14-14) | https://doi.org/10.3389/fnins.2023.1184333 ; https://doi.org/10.3389/fonc.2023.1141488 | (abdelilahseyfried2024arenaissanceof pages 1-3, min2023endothelialcellpericyteinteractions pages 1-2, perrelli2023krit1atraffic pages 1-3, perrelli2023krit1atraffic pages 3-4) |
| **CCM2** | Core Mendelian familial CCM gene; part of the CCM protein complex regulating endothelial signaling (abdelilahseyfried2024arenaissanceof pages 1-3, min2023endothelialcellpericyteinteractions pages 1-2) | **Autosomal dominant** with **incomplete penetrance** in familial CCM (min2023endothelialcellpericyteinteractions pages 1-2) | Predominantly **loss-of-function**; CCM2 deficiency contributes to CCM via dysregulated MEKK3-KLF2/4 and related endothelial programs (min2023endothelialcellpericyteinteractions pages 1-2, grdseloff2023impairedretinoicacid pages 2-3) | No specific example variant retrieved in the provided evidence set | Familial disease aligns with **germline + somatic second-hit** biology; acute/chronic **Ccm2** mouse and endothelial models support lesion formation after CCM2 loss (min2023endothelialcellpericyteinteractions pages 1-2, grdseloff2023impairedretinoicacid pages 2-3, grdseloff2023impairedretinoicacid pages 6-7) | https://doi.org/10.1101/cshperspect.a041188 ; https://doi.org/10.1038/s41598-023-31905-0 | (min2023endothelialcellpericyteinteractions pages 1-2, grdseloff2023impairedretinoicacid pages 2-3, grdseloff2023impairedretinoicacid pages 6-7) |
| **PDCD10 (CCM3)** | Third core Mendelian familial CCM gene; associated with CCM and often emphasized as capable of severe phenotypes in models (min2023endothelialcellpericyteinteractions pages 1-2) | **Autosomal dominant** with **incomplete penetrance** in familial CCM (min2023endothelialcellpericyteinteractions pages 1-2) | Predominantly **loss-of-function**; CCM3 loss disrupts endothelial/pericyte interactions, BBB stability, and lesion biology (min2023endothelialcellpericyteinteractions pages 1-2) | No specific example variant retrieved in the provided evidence set | **Somatic biallelic loss** and **clonal expansion** are implicated; endothelial or pericyte **Ccm3/Pdcd10** deletion can induce lesions in models (min2023endothelialcellpericyteinteractions pages 1-2) | https://doi.org/10.1101/cshperspect.a041188 | (min2023endothelialcellpericyteinteractions pages 1-2) |
| **Two-hit mechanism** | Current model for familial CCM lesion genesis: inherited pathogenic variant in a CCM gene plus **somatic loss of the remaining allele** in susceptible cells | Applies to **familial CCM**; inherited first hit followed by lesion-specific second hit | Produces **biallelic loss** of CCM gene function in lesion-forming endothelium | Not a single variant; mechanism supported across CCM genes | Supported by mouse and human lesion studies; endothelial clonal expansion is part of lesion development (shapeti2024forcemediatedangiogenesislinking pages 39-43, min2023endothelialcellpericyteinteractions pages 1-2, yordanov2024hyaluronicacidturnover pages 14-14) | https://doi.org/10.1101/cshperspect.a041188 ; https://doi.org/10.1063/5.0159330 | (shapeti2024forcemediatedangiogenesislinking pages 39-43, min2023endothelialcellpericyteinteractions pages 1-2, yordanov2024hyaluronicacidturnover pages 14-14) |
| **Additional somatic driver: PIK3CA GOF** | Recent work/reviews identify **somatic gain-of-function PIK3CA** variants in sporadic/aggressive CCM biology, often co-occurring with CCM loss-of-function alleles (abdelilahseyfried2024arenaissanceof pages 1-3, shapeti2024forcemediatedangiogenesislinking pages 39-43, ayata2024roleofrhoassociated pages 1-2) | Not inherited Mendelian driver in classic familial CCM; **somatic** lesion-associated driver | **Gain-of-function** activating PI3K signaling; linked to lesion growth and hemorrhage risk (ayata2024roleofrhoassociated pages 1-2, abdelilahseyfried2024arenaissanceof pages 1-3) | Specific PIK3CA variant not provided in extracted evidence | Proposed as a **third-hit / cooperating driver** that can fuel cavernoma growth together with CCM loss (shapeti2024forcemediatedangiogenesislinking pages 39-43, abdelilahseyfried2024arenaissanceof pages 1-3) | https://doi.org/10.1038/s44161-024-00504-1 ; https://doi.org/10.1212/nxg.0000000000200121 | (abdelilahseyfried2024arenaissanceof pages 1-3, shapeti2024forcemediatedangiogenesislinking pages 39-43, ayata2024roleofrhoassociated pages 1-2) |
| **Additional somatic driver: MAP3K3 / MEKK3 GOF** | Recent literature notes **MAP3K3 (MEKK3) gain-of-function** as another somatic driver relevant to CCM pathogenesis (abdelilahseyfried2024arenaissanceof pages 1-3, shapeti2024forcemediatedangiogenesislinking pages 46-49) | **Somatic** rather than classic familial inherited driver | **Gain-of-function** with activation of MEKK3-MEK5-ERK5-KLF2/4 and downstream CCM-like signaling (abdelilahseyfried2024arenaissanceof pages 1-3, shapeti2024forcemediatedangiogenesislinking pages 46-49) | Specific MAP3K3 variant not available in extracted evidence | Reported as potentially **sufficient to initiate lesions even without CCM loss** in some contexts; also intersects PI3K-mTOR signaling (shapeti2024forcemediatedangiogenesislinking pages 39-43, shapeti2024forcemediatedangiogenesislinking pages 46-49) | https://doi.org/10.1038/s44161-024-00504-1 | (abdelilahseyfried2024arenaissanceof pages 1-3, shapeti2024forcemediatedangiogenesislinking pages 39-43, shapeti2024forcemediatedangiogenesislinking pages 46-49) |


*Table: This table summarizes the core Mendelian CCM genes, their inheritance and loss-of-function pattern, the two-hit lesion model, and newer somatic drivers such as PIK3CA and MAP3K3. It also includes example KRIT1 truncating variants reported in recent retrieved studies with DOI links.*

| Study | Population | N | Follow-up | Hemorrhage rate / cumulative risk | Seizure data | Key prognostic factors | URL / DOI |
|---|---|---:|---|---|---|---|---|
| Gillespie 2023, *Neurosurgical Review* | Mixed adult CCM cohort (mostly sporadic/clinical referral cohort) | 545 patients; 734 lesions | Median 46 months (IQR 19–85) | Annual symptomatic hemorrhage rate 1.00% per lesion-year (25 events/2512 lesion-years); 1.50% per lesion-year in symptomatic-at-presentation vs 0.29% in non-symptomatic-at-presentation | Not reported in extracted evidence | Larger lesion size HR 1.04 (95% CI 1.01–1.07); eloquent location HR 2.63 (95% CI 1.12–6.16); symptomatic hemorrhage at presentation HR 5.37 (95% CI 2.40–11.99) (gillespie2023predictorsoffuture pages 1-2) | https://doi.org/10.1007/s10143-023-01949-x |
| Santos 2023, *Scientific Reports* | Conservatively managed cerebral and spinal cavernous malformations | 91 | Complete 10-year follow-up; 910 person-years | Overall 10-year cumulative hemorrhage risk 30% (95% CI 21–40%); annual (re)hemorrhage 3.5% (32/910 person-years); subgroup annual rates: bleeding at presentation 4.5%, brainstem 4.1%, spinal 6.7%, familial 3.8%, asymptomatic 0%; subgroup 10-year cumulative risk: spinal 67%, brainstem 33%, familial 31%, asymptomatic 0% (santos2023naturalcourseof pages 2-3, santos2023naturalcourseof pages 3-4, santos2023naturalcourseof pages 1-2) | Baseline cavernoma-related epilepsy 26/91 (28.6%); no prospective seizure rate extracted (santos2023naturalcourseof pages 2-3, santos2023naturalcourseof pages 3-4) | Hemorrhage at diagnosis aOR 2.41, aHR 2.31; spinal localization aOR 4.20, aHR 3.91; also reported as predictors in adjusted models p=0.039 and p=0.010, remaining significant in Cox regression p=0.049 and p=0.016 (santos2023naturalcourseof pages 3-4, santos2023naturalcourseof pages 1-2) | https://doi.org/10.1038/s41598-023-42594-0 |
| Geraldo 2023, *Neuroradiology* | Pediatric familial CCM (FCCM) multicenter cohort | 41 | 140.5 person-years; median 54.3 months (range 4.0–205.4) | Seven symptomatic hemorrhages during follow-up; annual hemorrhage rate 5.0% per person-year; cumulative symptomatic hemorrhage risk 7.3% at 1 year, 14.6% at 2 years, 17.1% at 5 years; 5-year risk higher with prior symptomatic hemorrhage 33.3%, CCM2 genotype 33.3%, positive family history 20.7% (geraldo2023naturalhistoryof pages 1-2, geraldo2023naturalhistoryof pages 4-5) | Seizures at last follow-up in 12/41 (29.3%); 10/12 medically controlled, 2/12 refractory; one death (2.4%) from sudden unexpected death in refractory epilepsy (geraldo2023naturalhistoryof pages 4-5) | Number of brainstem CCM at first MRI adjusted HR 1.37 (P=0.005); number of posterior fossa CCM adjusted HR 1.64 (P=0.004) (geraldo2023naturalhistoryof pages 1-2) | https://doi.org/10.1007/s00234-022-03056-y |
| Alalfi 2023, *Journal of Neurosurgery* | Familial cavernous malformation (FCM) prospective cohort | 75 | Median 9.9 years total follow-up; 949.2 patient-years; censored hemorrhage analysis 739.9 patient-years | First prospective hemorrhage rate 4.0% per patient-year; 30 patients had first prospective hemorrhage at median 5.3 years after diagnosis (alalfi2023clinicalpresentationhemorrhage pages 2-3) | 17/75 (22.7%) had seizures at presentation; 7 developed new seizure disorder at mean 4.3 years; total ever-seizure burden 24/75 (32%) (alalfi2023clinicalpresentationhemorrhage pages 2-3) | Kaplan–Meier comparison by hemorrhage-at-presentation performed, but no extracted HR/OR available (alalfi2023clinicalpresentationhemorrhage pages 2-3) | https://doi.org/10.3171/2023.1.jns222434 |
| Zuurbier 2023, *Neurology* | Female CCM cohort evaluating hormone exposure | 722 females (137 exposed; 585 unexposed) | Mean 3.33 years; 2400 person-years | Prospective intracranial hemorrhage: 46/137 (33.6%) exposed vs 91/585 (15.6%) unexposed; incidence 7.44 vs 5.11 per 100 person-years; adjusted HR for female hormone therapy 1.56 (95% CI 1.09–2.24); oral contraceptives age 10–44 adjusted HR 2.00 (95% CI 1.26–3.17); excluding transdermal users adjusted HR 1.73 (95% CI 1.20–2.50) (zuurbier2023femalehormonetherapy pages 3-5) | Not reported in extracted evidence | Menopausal hormone therapy nonsignificant in one extracted analysis: adjusted HR 1.44 (95% CI 0.68–3.05); another extracted subgroup analysis reported oral MHT adjusted HR 2.39 (95% CI 1.11–5.14); smoker-restricted oral contraceptive adjusted HR 2.71 (95% CI 1.01–7.28) (zuurbier2023femalehormonetherapy pages 3-5) | https://doi.org/10.1212/WNL.0000000000206888 |


*Table: This table summarizes the main quantitative natural-history and prognostic findings from recent 2023 studies on cerebral cavernous malformation, including familial and pediatric cohorts. It is useful for comparing hemorrhage risk, seizure burden, and major prognostic factors across study populations.*

| Intervention | Mechanistic rationale | NCT ID | Phase | Status | Enrollment | Primary endpoint(s) | Key secondary endpoint(s) | ClinicalTrials.gov URL | Evidence |
|---|---|---|---|---|---:|---|---|---|---|
| REC-994 (oral, 200 mg QD or 400 mg QD) vs placebo | Investigational medical therapy for symptomatic CCM; trial emphasizes safety, hemorrhagic-event monitoring, lesion burden, and patient-reported/functional outcomes, consistent with a barrier-stabilization/anti-lesion strategy in symptomatic disease (NCT05085561 chunk 1) | NCT05085561 | Phase 2 | Completed | 62 | Incidence and severity of adverse events up to 24 months | MRI-confirmed cerebral hemorrhagic events; lesion size/number on MRI; Cerebral Cavernous Malformation Health Index; modified Rankin Scale; SymptoMScreen; plasma PK of REC-994 (NCT05085561 chunk 1) | https://clinicaltrials.gov/ct2/show/NCT05085561 | (NCT05085561 chunk 1) |
| Atorvastatin (40–80 mg once daily) vs placebo | Indirect ROCK-pathway modulation is a key CCM therapeutic concept; trial includes ROCK activity in peripheral blood leukocytes as a biomarker and MRI QSM/permeability readouts for lesional activity (ayata2024roleofrhoassociated pages 1-2, NCT02603328 chunk 1) | NCT02603328 | Phase 1/2 | Completed | 80 | Percent change in mean lesional QSM score over 2 years | Percent change in DCEQP lesional vascular permeability; modified Rankin Scale at years 1 and 2; EQ-VAS; compliance; mean percent change in ROCK activity in peripheral blood leukocytes (NCT02603328 chunk 1) | https://clinicaltrials.gov/ct2/show/NCT02603328 | (ayata2024roleofrhoassociated pages 1-2, NCT02603328 chunk 1) |
| Propranolol in familial CCM (Treat_CCM) | Repurposed pharmacologic therapy tested in familial CCM; trial record confirms phase 2 pilot design and later publication of safety/efficacy report, but extracted chunk does not provide endpoint details (NCT03589014 chunk 2) | NCT03589014 | Phase 2 pilot | Completed | 71 | Not specified in extracted trial chunk | Not specified in extracted trial chunk; record notes protocol and Lancet Neurology 2023 report of safety/efficacy study (NCT03589014 chunk 2) | https://clinicaltrials.gov/ct2/show/NCT03589014 | (NCT03589014 chunk 2) |
| Oral propranolol 60 mg ER daily for 7–10 days preoperatively vs control | Short-course preoperative propranolol assessed as a translational biologic-response study in symptomatic cavernous malformation tissue/blood rather than a lesion-outcome efficacy trial (NCT03474614 chunk 1) | NCT03474614 | Phase 2 | Terminated (lack of accrual) | 4 | Effect of low-dose oral propranolol on global mRNA and miRNA expression in blood and CCM tissue | Correlation of treatment response with established CCM gene mutations; adverse events related to propranolol (NCT03474614 chunk 1) | https://clinicaltrials.gov/ct2/show/NCT03474614 | (NCT03474614 chunk 1) |


*Table: This table summarizes the CCM interventional trials retrieved from ClinicalTrials.gov for REC-994, atorvastatin, and propranolol. It highlights trial design, endpoints, enrollment, and mechanistic rationale relevant to current translational and clinical development.*

---

## Notes on evidence limitations
- Several requested identifiers (OMIM/Orphanet/ICD/MeSH) were not retrievable in the current tool context; MONDO IDs are provided.
- Many mechanistic statements are best supported by reviews; where possible, this report includes primary cohort statistics and model-system experimental findings.
- Some recent high-impact reviews (e.g., NEJM 2024) and specific primary genetics papers (e.g., MAP3K3 somatic driver paper in *Brain* 2023) were listed as unobtainable in tool retrieval and therefore are not cited.


References

1. (min2023endothelialcellpericyteinteractions pages 1-2): Wang Min and Jenny Huanjiao Zhou. Endothelial cell-pericyte interactions in the pathogenesis of cerebral cavernous malformations (ccms). Cold Spring Harbor perspectives in medicine, 13:a041188, Jun 2023. URL: https://doi.org/10.1101/cshperspect.a041188, doi:10.1101/cshperspect.a041188. This article has 9 citations and is from a peer-reviewed journal.

2. (montagnoli2023therapeuticperspectiveson pages 2-4): Tadeu L. Montagnoli, Daniela R. de Oliveira, and Carlos A. Manssour Fraga. Therapeutic perspectives on rock inhibition for cerebral cavernous malformations. Kinases and Phosphatases, 1:72-96, Feb 2023. URL: https://doi.org/10.3390/kinasesphosphatases1010006, doi:10.3390/kinasesphosphatases1010006. This article has 8 citations.

3. (montagnoli2023therapeuticperspectiveson pages 1-2): Tadeu L. Montagnoli, Daniela R. de Oliveira, and Carlos A. Manssour Fraga. Therapeutic perspectives on rock inhibition for cerebral cavernous malformations. Kinases and Phosphatases, 1:72-96, Feb 2023. URL: https://doi.org/10.3390/kinasesphosphatases1010006, doi:10.3390/kinasesphosphatases1010006. This article has 8 citations.

4. (shapeti2024forcemediatedangiogenesislinking pages 39-43): A Shapeti, H Van Oosterwyck, A Ranga, and E Faurobert. Force-mediated angiogenesis: linking mechanical mechanisms to vascular lesion growth. Unknown journal, 2024.

5. (abdelilahseyfried2024arenaissanceof pages 1-3): Salim Abdelilah-Seyfried and Hanjoong Jo. A renaissance of cerebral cavernous malformation proteins in vascular physiology. Nature cardiovascular research, 3 7:771-773, Jun 2024. URL: https://doi.org/10.1038/s44161-024-00504-1, doi:10.1038/s44161-024-00504-1. This article has 3 citations and is from a peer-reviewed journal.

6. (ayata2024roleofrhoassociated pages 1-2): Cenk Ayata, Helen Kim, Leslie Morrison, James K. Liao, Juan Gutierrez, Miguel Lopez-Toledano, Enrique Carrazana, Adrian L. Rabinowicz, and Issam A. Awad. Role of rho-associated kinase in the pathophysiology of cerebral cavernous malformations. Neurology Genetics, Feb 2024. URL: https://doi.org/10.1212/nxg.0000000000200121, doi:10.1212/nxg.0000000000200121. This article has 21 citations.

7. (perrelli2023krit1atraffic pages 15-16): Andrea Perrelli, Chiara Ferraris, Elisa Berni, Angela J. Glading, and Saverio Francesco Retta. Krit1: a traffic warden at the busy crossroads between redox signaling and the pathogenesis of cerebral cavernous malformation disease. Antioxidants &amp; Redox Signaling, Nov 2023. URL: https://doi.org/10.1089/ars.2021.0263, doi:10.1089/ars.2021.0263. This article has 16 citations and is from a domain leading peer-reviewed journal.

8. (yordanov2024hyaluronicacidturnover pages 1-3): Teodor E. Yordanov, Marco A. E. Martinez, Tyron Esposito, Juliann B. Tefft, Larisa I. Labzin, Samantha J. Stehbens, Alan E. Rowan, Benjamin M. Hogan, Christopher S. Chen, Jan Lauko, and Anne K. Lagendijk. Hyaluronic acid turnover controls the severity of cerebral cavernous malformations in bioengineered human micro-vessels. APL Bioengineering, Oct 2024. URL: https://doi.org/10.1063/5.0159330, doi:10.1063/5.0159330. This article has 5 citations.

9. (srinath2023plasmametaboliteswith pages 2-3): Abhinav Srinath, Bingqing Xie, Ying Li, Je Yeong Sone, Sharbel Romanos, Chang Chen, Anukriti Sharma, Sean Polster, Pieter C. Dorrestein, Kelly C. Weldon, Dorothy DeBiasse, Thomas Moore, Rhonda Lightle, Janne Koskimäki, Dongdong Zhang, Agnieszka Stadnik, Kristina Piedad, Matthew Hagan, Abdallah Shkoukani, Julián Carrión-Penagos, Dehua Bi, Le Shen, Robert Shenkar, Yuan Ji, Ashley Sidebottom, Eric Pamer, Jack A. Gilbert, Mark L. Kahn, Mark D’Souza, Dinanath Sulakhe, Issam A. Awad, and Romuald Girard. Plasma metabolites with mechanistic and clinical links to the neurovascular disease cavernous angioma. Communications Medicine, Mar 2023. URL: https://doi.org/10.1038/s43856-023-00265-1, doi:10.1038/s43856-023-00265-1. This article has 19 citations and is from a peer-reviewed journal.

10. (NCT02603328 chunk 1):  Atorvastatin Treatment of Cavernous Angiomas With Symptomatic Hemorrhage Exploratory Proof of Concept (AT CASH EPOC) Trial. University of Chicago. 2018. ClinicalTrials.gov Identifier: NCT02603328

11. (srinath2023plasmametaboliteswith pages 1-2): Abhinav Srinath, Bingqing Xie, Ying Li, Je Yeong Sone, Sharbel Romanos, Chang Chen, Anukriti Sharma, Sean Polster, Pieter C. Dorrestein, Kelly C. Weldon, Dorothy DeBiasse, Thomas Moore, Rhonda Lightle, Janne Koskimäki, Dongdong Zhang, Agnieszka Stadnik, Kristina Piedad, Matthew Hagan, Abdallah Shkoukani, Julián Carrión-Penagos, Dehua Bi, Le Shen, Robert Shenkar, Yuan Ji, Ashley Sidebottom, Eric Pamer, Jack A. Gilbert, Mark L. Kahn, Mark D’Souza, Dinanath Sulakhe, Issam A. Awad, and Romuald Girard. Plasma metabolites with mechanistic and clinical links to the neurovascular disease cavernous angioma. Communications Medicine, Mar 2023. URL: https://doi.org/10.1038/s43856-023-00265-1, doi:10.1038/s43856-023-00265-1. This article has 19 citations and is from a peer-reviewed journal.

12. (perrelli2023krit1atraffic pages 1-3): Andrea Perrelli, Chiara Ferraris, Elisa Berni, Angela J. Glading, and Saverio Francesco Retta. Krit1: a traffic warden at the busy crossroads between redox signaling and the pathogenesis of cerebral cavernous malformation disease. Antioxidants &amp; Redox Signaling, Nov 2023. URL: https://doi.org/10.1089/ars.2021.0263, doi:10.1089/ars.2021.0263. This article has 16 citations and is from a domain leading peer-reviewed journal.

13. (gillespie2023predictorsoffuture pages 1-2): Conor S. Gillespie, Khalifa E. Alnaham, George E. Richardson, Mohammad A. Mustafa, Basel A. Taweel, Abdurrahman I. Islim, Cathal John Hannan, and Emmanuel Chavredakis. Predictors of future haemorrhage from cerebral cavernous malformations: a retrospective cohort study. Neurosurgical Review, Feb 2023. URL: https://doi.org/10.1007/s10143-023-01949-x, doi:10.1007/s10143-023-01949-x. This article has 8 citations and is from a peer-reviewed journal.

14. (santos2023naturalcourseof pages 3-4): Alejandro N. Santos, Laurèl Rauschenbach, Hanah H. Gull, Angelina Olbrich, Thiemo F. Dinger, Marvin Darkwah Oppong, Christoph Rieß, Bixia Chen, Annika Lenkeit, Börge Schmidt, Yan Li, Ramazan Jabbarli, Karsten H. Wrede, Adrian Siegel, Ulrich Sure, and Philipp Dammann. Natural course of cerebral and spinal cavernous malformations: a complete ten-year follow-up study. Scientific Reports, Sep 2023. URL: https://doi.org/10.1038/s41598-023-42594-0, doi:10.1038/s41598-023-42594-0. This article has 15 citations and is from a peer-reviewed journal.

15. (alalfi2023clinicalpresentationhemorrhage pages 2-3): Mohammed O. Alalfi, Giuseppe Lanzino, and Kelly D. Flemming. Clinical presentation, hemorrhage risk, and outcome in patients with familial cavernous malformations: a pragmatic prospective analysis of 75 patients. Journal of Neurosurgery, 139:1018-1024, Oct 2023. URL: https://doi.org/10.3171/2023.1.jns222434, doi:10.3171/2023.1.jns222434. This article has 17 citations and is from a domain leading peer-reviewed journal.

16. (zuurbier2023femalehormonetherapy pages 3-5): Susanna M. Zuurbier, Alejandro N. Santos, Kelly D. Flemming, Börge Schmidt, Ramazan Jabbarli, Giuseppe Lanzino, Ulrich Sure, and Philipp Dammann. Female hormone therapy and risk of intracranial hemorrhage from cerebral cavernous malformations. Neurology, Apr 2023. URL: https://doi.org/10.1212/wnl.0000000000206888, doi:10.1212/wnl.0000000000206888. This article has 31 citations and is from a highest quality peer-reviewed journal.

17. (grdseloff2023impairedretinoicacid pages 4-5): Nastasja Grdseloff, Gwenola Boulday, Claudia J. Rödel, Cécile Otten, Daphné Raphaelle Vannier, Cécile Cardoso, Eva Faurobert, Deepika Dogra, Elisabeth Tournier-Lasserve, and Salim Abdelilah-Seyfried. Impaired retinoic acid signaling in cerebral cavernous malformations. Scientific Reports, Apr 2023. URL: https://doi.org/10.1038/s41598-023-31905-0, doi:10.1038/s41598-023-31905-0. This article has 4 citations and is from a peer-reviewed journal.

18. (grdseloff2023impairedretinoicacid pages 6-7): Nastasja Grdseloff, Gwenola Boulday, Claudia J. Rödel, Cécile Otten, Daphné Raphaelle Vannier, Cécile Cardoso, Eva Faurobert, Deepika Dogra, Elisabeth Tournier-Lasserve, and Salim Abdelilah-Seyfried. Impaired retinoic acid signaling in cerebral cavernous malformations. Scientific Reports, Apr 2023. URL: https://doi.org/10.1038/s41598-023-31905-0, doi:10.1038/s41598-023-31905-0. This article has 4 citations and is from a peer-reviewed journal.

19. (NCT05085561 chunk 1):  The Symptomatic Cerebral Cavernous Malformation Trial of REC-994. Recursion Pharmaceuticals Inc.. 2022. ClinicalTrials.gov Identifier: NCT05085561

20. (NCT03589014 chunk 2):  Treat_CCM: Propranolol in Familial Cerebral Cavernous Malformation. Mario Negri Institute for Pharmacological Research. 2018. ClinicalTrials.gov Identifier: NCT03589014

21. (geraldo2023naturalhistoryof pages 1-2): Ana Filipa Geraldo, Cesar Augusto P. F. Alves, Aysha Luis, Domenico Tortora, Joana Guimarães, Daisy Abreu, Sofia Reimão, Marco Pavanello, Patrizia de Marco, Marcello Scala, Valeria Capra, Rui Vaz, Andrea Rossi, Erin Simon Schwartz, Kshitij Mankad, and Mariasavina Severino. Natural history of familial cerebral cavernous malformation syndrome in children: a multicenter cohort study. Neuroradiology, 65:401-414, Oct 2023. URL: https://doi.org/10.1007/s00234-022-03056-y, doi:10.1007/s00234-022-03056-y. This article has 17 citations and is from a peer-reviewed journal.

22. (srinath2023plasmametaboliteswith pages 11-13): Abhinav Srinath, Bingqing Xie, Ying Li, Je Yeong Sone, Sharbel Romanos, Chang Chen, Anukriti Sharma, Sean Polster, Pieter C. Dorrestein, Kelly C. Weldon, Dorothy DeBiasse, Thomas Moore, Rhonda Lightle, Janne Koskimäki, Dongdong Zhang, Agnieszka Stadnik, Kristina Piedad, Matthew Hagan, Abdallah Shkoukani, Julián Carrión-Penagos, Dehua Bi, Le Shen, Robert Shenkar, Yuan Ji, Ashley Sidebottom, Eric Pamer, Jack A. Gilbert, Mark L. Kahn, Mark D’Souza, Dinanath Sulakhe, Issam A. Awad, and Romuald Girard. Plasma metabolites with mechanistic and clinical links to the neurovascular disease cavernous angioma. Communications Medicine, Mar 2023. URL: https://doi.org/10.1038/s43856-023-00265-1, doi:10.1038/s43856-023-00265-1. This article has 19 citations and is from a peer-reviewed journal.

23. (geraldo2023naturalhistoryof pages 4-5): Ana Filipa Geraldo, Cesar Augusto P. F. Alves, Aysha Luis, Domenico Tortora, Joana Guimarães, Daisy Abreu, Sofia Reimão, Marco Pavanello, Patrizia de Marco, Marcello Scala, Valeria Capra, Rui Vaz, Andrea Rossi, Erin Simon Schwartz, Kshitij Mankad, and Mariasavina Severino. Natural history of familial cerebral cavernous malformation syndrome in children: a multicenter cohort study. Neuroradiology, 65:401-414, Oct 2023. URL: https://doi.org/10.1007/s00234-022-03056-y, doi:10.1007/s00234-022-03056-y. This article has 17 citations and is from a peer-reviewed journal.

24. (santos2023naturalcourseof pages 2-3): Alejandro N. Santos, Laurèl Rauschenbach, Hanah H. Gull, Angelina Olbrich, Thiemo F. Dinger, Marvin Darkwah Oppong, Christoph Rieß, Bixia Chen, Annika Lenkeit, Börge Schmidt, Yan Li, Ramazan Jabbarli, Karsten H. Wrede, Adrian Siegel, Ulrich Sure, and Philipp Dammann. Natural course of cerebral and spinal cavernous malformations: a complete ten-year follow-up study. Scientific Reports, Sep 2023. URL: https://doi.org/10.1038/s41598-023-42594-0, doi:10.1038/s41598-023-42594-0. This article has 15 citations and is from a peer-reviewed journal.

25. (santos2023naturalcourseof pages 1-2): Alejandro N. Santos, Laurèl Rauschenbach, Hanah H. Gull, Angelina Olbrich, Thiemo F. Dinger, Marvin Darkwah Oppong, Christoph Rieß, Bixia Chen, Annika Lenkeit, Börge Schmidt, Yan Li, Ramazan Jabbarli, Karsten H. Wrede, Adrian Siegel, Ulrich Sure, and Philipp Dammann. Natural course of cerebral and spinal cavernous malformations: a complete ten-year follow-up study. Scientific Reports, Sep 2023. URL: https://doi.org/10.1038/s41598-023-42594-0, doi:10.1038/s41598-023-42594-0. This article has 15 citations and is from a peer-reviewed journal.

26. (perrelli2023krit1atraffic pages 6-7): Andrea Perrelli, Chiara Ferraris, Elisa Berni, Angela J. Glading, and Saverio Francesco Retta. Krit1: a traffic warden at the busy crossroads between redox signaling and the pathogenesis of cerebral cavernous malformation disease. Antioxidants &amp; Redox Signaling, Nov 2023. URL: https://doi.org/10.1089/ars.2021.0263, doi:10.1089/ars.2021.0263. This article has 16 citations and is from a domain leading peer-reviewed journal.

27. (grdseloff2023impairedretinoicacid pages 1-2): Nastasja Grdseloff, Gwenola Boulday, Claudia J. Rödel, Cécile Otten, Daphné Raphaelle Vannier, Cécile Cardoso, Eva Faurobert, Deepika Dogra, Elisabeth Tournier-Lasserve, and Salim Abdelilah-Seyfried. Impaired retinoic acid signaling in cerebral cavernous malformations. Scientific Reports, Apr 2023. URL: https://doi.org/10.1038/s41598-023-31905-0, doi:10.1038/s41598-023-31905-0. This article has 4 citations and is from a peer-reviewed journal.

28. (grdseloff2023impairedretinoicacid pages 7-9): Nastasja Grdseloff, Gwenola Boulday, Claudia J. Rödel, Cécile Otten, Daphné Raphaelle Vannier, Cécile Cardoso, Eva Faurobert, Deepika Dogra, Elisabeth Tournier-Lasserve, and Salim Abdelilah-Seyfried. Impaired retinoic acid signaling in cerebral cavernous malformations. Scientific Reports, Apr 2023. URL: https://doi.org/10.1038/s41598-023-31905-0, doi:10.1038/s41598-023-31905-0. This article has 4 citations and is from a peer-reviewed journal.

29. (srinath2023plasmametaboliteswith pages 7-9): Abhinav Srinath, Bingqing Xie, Ying Li, Je Yeong Sone, Sharbel Romanos, Chang Chen, Anukriti Sharma, Sean Polster, Pieter C. Dorrestein, Kelly C. Weldon, Dorothy DeBiasse, Thomas Moore, Rhonda Lightle, Janne Koskimäki, Dongdong Zhang, Agnieszka Stadnik, Kristina Piedad, Matthew Hagan, Abdallah Shkoukani, Julián Carrión-Penagos, Dehua Bi, Le Shen, Robert Shenkar, Yuan Ji, Ashley Sidebottom, Eric Pamer, Jack A. Gilbert, Mark L. Kahn, Mark D’Souza, Dinanath Sulakhe, Issam A. Awad, and Romuald Girard. Plasma metabolites with mechanistic and clinical links to the neurovascular disease cavernous angioma. Communications Medicine, Mar 2023. URL: https://doi.org/10.1038/s43856-023-00265-1, doi:10.1038/s43856-023-00265-1. This article has 19 citations and is from a peer-reviewed journal.

30. (demir2024giantintracranialcavernous pages 1-2): Mustafa Kemal Demir, Deniz Kılıc, Emre Zorlu, and Turker Kılıc. Giant intracranial cavernous malformations: a review on magnetic resonance imaging characteristics. Indian Journal of Radiology and Imaging, 34:511-521, Feb 2024. URL: https://doi.org/10.1055/s-0044-1779587, doi:10.1055/s-0044-1779587. This article has 4 citations.

31. (demir2024giantintracranialcavernous pages 2-3): Mustafa Kemal Demir, Deniz Kılıc, Emre Zorlu, and Turker Kılıc. Giant intracranial cavernous malformations: a review on magnetic resonance imaging characteristics. Indian Journal of Radiology and Imaging, 34:511-521, Feb 2024. URL: https://doi.org/10.1055/s-0044-1779587, doi:10.1055/s-0044-1779587. This article has 4 citations.

32. (demir2024giantintracranialcavernous media cdc7d79b): Mustafa Kemal Demir, Deniz Kılıc, Emre Zorlu, and Turker Kılıc. Giant intracranial cavernous malformations: a review on magnetic resonance imaging characteristics. Indian Journal of Radiology and Imaging, 34:511-521, Feb 2024. URL: https://doi.org/10.1055/s-0044-1779587, doi:10.1055/s-0044-1779587. This article has 4 citations.

33. (demir2024giantintracranialcavernous media ee42a4a3): Mustafa Kemal Demir, Deniz Kılıc, Emre Zorlu, and Turker Kılıc. Giant intracranial cavernous malformations: a review on magnetic resonance imaging characteristics. Indian Journal of Radiology and Imaging, 34:511-521, Feb 2024. URL: https://doi.org/10.1055/s-0044-1779587, doi:10.1055/s-0044-1779587. This article has 4 citations.

34. (flemming2024clinicalandradiologic pages 5-7): KD Flemming, Jonathan Graff Radford, Ross Reichard, James Klaas, Sherri Braksick, Petrice Cogswell, and Giuseppe Lanzino. Clinical and radiologic distinctions between familial cavernous malformation syndrome and cerebral amyloid angiopathy. Acta Neurochirurgica, Dec 2024. URL: https://doi.org/10.1007/s00701-024-06400-8, doi:10.1007/s00701-024-06400-8. This article has 0 citations and is from a peer-reviewed journal.

35. (flemming2024clinicalandradiologic pages 1-3): KD Flemming, Jonathan Graff Radford, Ross Reichard, James Klaas, Sherri Braksick, Petrice Cogswell, and Giuseppe Lanzino. Clinical and radiologic distinctions between familial cavernous malformation syndrome and cerebral amyloid angiopathy. Acta Neurochirurgica, Dec 2024. URL: https://doi.org/10.1007/s00701-024-06400-8, doi:10.1007/s00701-024-06400-8. This article has 0 citations and is from a peer-reviewed journal.

36. (flemming2024clinicalandradiologic pages 7-9): KD Flemming, Jonathan Graff Radford, Ross Reichard, James Klaas, Sherri Braksick, Petrice Cogswell, and Giuseppe Lanzino. Clinical and radiologic distinctions between familial cavernous malformation syndrome and cerebral amyloid angiopathy. Acta Neurochirurgica, Dec 2024. URL: https://doi.org/10.1007/s00701-024-06400-8, doi:10.1007/s00701-024-06400-8. This article has 0 citations and is from a peer-reviewed journal.

37. (NCT03474614 chunk 1): Lori Wood. Effect of Oral Propranolol on mRNA Expresssion in Symptomatic Cavernous Malformation. St. Joseph's Hospital and Medical Center, Phoenix. 2018. ClinicalTrials.gov Identifier: NCT03474614

38. (grdseloff2023impairedretinoicacid pages 5-6): Nastasja Grdseloff, Gwenola Boulday, Claudia J. Rödel, Cécile Otten, Daphné Raphaelle Vannier, Cécile Cardoso, Eva Faurobert, Deepika Dogra, Elisabeth Tournier-Lasserve, and Salim Abdelilah-Seyfried. Impaired retinoic acid signaling in cerebral cavernous malformations. Scientific Reports, Apr 2023. URL: https://doi.org/10.1038/s41598-023-31905-0, doi:10.1038/s41598-023-31905-0. This article has 4 citations and is from a peer-reviewed journal.

39. (perrelli2023krit1atraffic pages 3-4): Andrea Perrelli, Chiara Ferraris, Elisa Berni, Angela J. Glading, and Saverio Francesco Retta. Krit1: a traffic warden at the busy crossroads between redox signaling and the pathogenesis of cerebral cavernous malformation disease. Antioxidants &amp; Redox Signaling, Nov 2023. URL: https://doi.org/10.1089/ars.2021.0263, doi:10.1089/ars.2021.0263. This article has 16 citations and is from a domain leading peer-reviewed journal.

40. (yordanov2024hyaluronicacidturnover pages 14-14): Teodor E. Yordanov, Marco A. E. Martinez, Tyron Esposito, Juliann B. Tefft, Larisa I. Labzin, Samantha J. Stehbens, Alan E. Rowan, Benjamin M. Hogan, Christopher S. Chen, Jan Lauko, and Anne K. Lagendijk. Hyaluronic acid turnover controls the severity of cerebral cavernous malformations in bioengineered human micro-vessels. APL Bioengineering, Oct 2024. URL: https://doi.org/10.1063/5.0159330, doi:10.1063/5.0159330. This article has 5 citations.

41. (grdseloff2023impairedretinoicacid pages 2-3): Nastasja Grdseloff, Gwenola Boulday, Claudia J. Rödel, Cécile Otten, Daphné Raphaelle Vannier, Cécile Cardoso, Eva Faurobert, Deepika Dogra, Elisabeth Tournier-Lasserve, and Salim Abdelilah-Seyfried. Impaired retinoic acid signaling in cerebral cavernous malformations. Scientific Reports, Apr 2023. URL: https://doi.org/10.1038/s41598-023-31905-0, doi:10.1038/s41598-023-31905-0. This article has 4 citations and is from a peer-reviewed journal.

42. (shapeti2024forcemediatedangiogenesislinking pages 46-49): A Shapeti, H Van Oosterwyck, A Ranga, and E Faurobert. Force-mediated angiogenesis: linking mechanical mechanisms to vascular lesion growth. Unknown journal, 2024.