---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-08T16:34:22.438113'
end_time: '2026-05-08T16:45:13.388266'
duration_seconds: 650.95
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: FLNA Intestinal Pseudoobstruction
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 36
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** FLNA Intestinal Pseudoobstruction
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **FLNA Intestinal Pseudoobstruction** covering all of the
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
- **Disease Name:** FLNA Intestinal Pseudoobstruction
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **FLNA Intestinal Pseudoobstruction** covering all of the
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


# FLNA Intestinal Pseudo-obstruction (FLNA-related CIPO): Comprehensive Disease Characteristics Report

## Executive summary
FLNA intestinal pseudo-obstruction refers to a rare, genetic, typically X-linked form of severe gastrointestinal dysmotility that clinically mimics mechanical obstruction but lacks an occluding lesion, and is caused by pathogenic variants in **FLNA** (filamin A). It is often described as an **X-linked chronic idiopathic intestinal pseudo-obstruction (CIIPX)** / **X-linked intestinal pseudo-obstruction**, and is frequently associated with a characteristic **visceral smooth muscle pathology (abnormal muscle layering)** and variable multisystem features (e.g., CNS, cardiovascular). (gargiulo2007filaminais pages 1-2, kapur2010diffuseabnormallayering pages 13-14, jenkins2018differentialregulationof pages 1-7)

---

## 1. Disease information
### 1.1 Definition / overview (current understanding)
A landmark description of the X-linked form defines chronic idiopathic intestinal pseudo-obstruction (CIIP) as a heterogeneous syndrome of severe GI dysmotility, diagnosed by objective evidence of intestinal obstruction **without mechanical occlusion** (radiologic/surgical/manometric evidence). (gargiulo2007filaminais pages 1-2)

A core anatomic-pathologic correlate in FLNA-associated X-linked cases is **“diffuse abnormal layering of small intestinal smooth muscle”**, supporting classification within **visceral myopathy / enteric neuromyopathy** rather than purely neuropathic disease. (kapur2010diffuseabnormallayering pages 13-14, kapur2010diffuseabnormallayering pages 14-14)

### 1.2 Key identifiers
* **MONDO:** Open Targets maps chronic intestinal pseudo-obstruction to **MONDO_0017574** and lists FLNA as an associated target for “chronic intestinal pseudoobstruction” and “intestinal pseudo-obstruction.” URL: https://platform.opentargets.org/ (association evidence in tool context). (OpenTargets Search: intestinal pseudo-obstruction,chronic intestinal pseudo-obstruction-FLNA)
* **MeSH:** ClinicalTrials.gov browse terms for pseudo-obstruction include **“Intestinal Pseudo-Obstruction”** (MeSH ID **D007418**). (NCT07448753 chunk 1)
* **OMIM / Orphanet / ICD-10/ICD-11:** Not directly retrievable in the current evidence set; these identifiers should be confirmed via OMIM/Orphanet/WHO ICD browser during knowledge-base curation.

### 1.3 Synonyms / alternative names
Common labels used in the literature include:
* **X-linked chronic idiopathic intestinal pseudo-obstruction (CIIPX)** (gargiulo2007filaminais pages 1-2)
* **X-linked intestinal pseudo-obstruction** (kapur2010diffuseabnormallayering pages 13-14)
* **FLNA-related chronic intestinal pseudo-obstruction (CIPO)** (jenkins2018differentialregulationof pages 1-7)
* Overlapping presentation: **congenital short bowel syndrome (CSBS) due to FLNA** in male patients (werf2013congenitalshortbowel pages 1-2)

### 1.4 Evidence sources
The disease characterization is derived primarily from:
* **Family-based human genetics** and case series (e.g., multigenerational kindreds, pathology cohorts). (gargiulo2007filaminais pages 1-2, kapur2010diffuseabnormallayering pages 13-14)
* **Aggregated cohort resources** describing FLNA loss-of-function multisystem disease (including GI features) in tertiary-care cohorts. (rijckmans2024counselingindividualswith pages 1-3)


| Concept | Details | Key citations (PMID/DOI/URL, year) |
|---|---|---|
| Disease label / scope | FLNA-associated X-linked intestinal pseudo-obstruction is a rare hereditary enteric motility disorder within the broader category of FLNA-related chronic intestinal pseudo-obstruction (CIPO); it is commonly framed as a visceral myopathy / enteric neuromyopathy phenotype caused by pathogenic FLNA variants. | Gargiulo et al., *Am J Hum Genet* (2007), DOI: https://doi.org/10.1086/513321; Jenkins et al., *Hum Mutat* (2018), DOI: https://doi.org/10.1002/humu.23355 (gargiulo2007filaminais pages 1-2, jenkins2018differentialregulationof pages 1-7) |
| Disease identifier | Open Targets lists FLNA as associated with **MONDO:0017574 chronic intestinal pseudoobstruction** and with intestinal pseudo-obstruction / familial visceral myopathy disease concepts. | Open Targets disease-target association for FLNA ↔ MONDO:0017574, URL: https://platform.opentargets.org/ (accessed via tool context, 2024-2026) (OpenTargets Search: intestinal pseudo-obstruction,chronic intestinal pseudo-obstruction-FLNA) |
| Common synonyms | X-linked chronic idiopathic intestinal pseudo-obstruction (CIIPX); X-linked intestinal pseudo-obstruction; FLNA-related chronic intestinal pseudo-obstruction; FLNA-related congenital intestinal pseudo-obstruction; FLNA-related visceral myopathy; FLNA-related congenital short bowel syndrome when shortened bowel is the presenting feature. | Gargiulo et al. (2007), DOI: https://doi.org/10.1086/513321; van der Werf et al. (2013), DOI: https://doi.org/10.1038/gim.2012.123; Jenkins et al. (2018), DOI: https://doi.org/10.1002/humu.23355 (gargiulo2007filaminais pages 1-2, werf2013congenitalshortbowel pages 1-2, jenkins2018differentialregulationof pages 1-7) |
| Primary gene | **FLNA** (filamin A), Xq28; encodes an actin-binding cytoskeletal scaffold protein important for smooth-muscle architecture, mechanotransduction, and tissue-specific developmental programs, including intestinal smooth muscle and motility. | Gargiulo et al. (2007), DOI: https://doi.org/10.1086/513321; Jenkins et al. (2018), DOI: https://doi.org/10.1002/humu.23355 (gargiulo2007filaminais pages 1-2, jenkins2018differentialregulationof pages 1-7) |
| Inheritance pattern | Predominantly **X-linked**. Classic intestinal pseudo-obstruction presentations are often described as X-linked recessive / male-limited severe disease in families, whereas FLNA loss-of-function more broadly behaves as X-linked dominant with marked male lethality and female multisystem manifestations. | Gargiulo et al. (2007), DOI: https://doi.org/10.1086/513321; Rijckmans et al. preprint (2024), DOI: https://doi.org/10.21203/rs.3.rs-4546691/v1 (gargiulo2007filaminais pages 1-2, rijckmans2024counselingindividualswith pages 1-3) |
| Sex effects | Affected **males** often have the most severe neonatal/infantile intestinal phenotype and high early mortality; surviving **females** with FLNA loss-of-function more often show PVNH and multisystem findings, though gastrointestinal symptoms such as constipation/CIPO can occur. Survival in males may depend on residual FLNA function or isoform-specific expression. | Gargiulo et al. (2007), DOI: https://doi.org/10.1086/513321; Jenkins et al. (2018), DOI: https://doi.org/10.1002/humu.23355; Rijckmans et al. preprint (2024), DOI: https://doi.org/10.21203/rs.3.rs-4546691/v1 (gargiulo2007filaminais pages 1-2, jenkins2018differentialregulationof pages 1-7, rijckmans2024counselingindividualswith pages 1-3) |
| Hallmark clinical phenotype | Functional intestinal obstruction without a lumen-occluding lesion, typically with recurrent or persistent abdominal distension, vomiting/feeding intolerance, severe dysmotility, failure to thrive, and inability to sustain enteral nutrition in severe cases. | Gargiulo et al. (2007), DOI: https://doi.org/10.1086/513321; Jenkins et al. (2018), DOI: https://doi.org/10.1002/humu.23355 (gargiulo2007filaminais pages 1-2, jenkins2018differentialregulationof pages 1-7) |
| Hallmark pathology | Characteristic **diffuse abnormal layering of small intestinal smooth muscle**; evidence supports a primarily **myopathic** mechanism in many FLNA intestinal cases. | Kapur et al., *Am J Surg Pathol* (2010), DOI: https://doi.org/10.1097/PAS.0b013e3181f0ae47 (kapur2010diffuseabnormallayering pages 11-12, kapur2010diffuseabnormallayering pages 13-14, kapur2010diffuseabnormallayering pages 14-14) |
| Associated bowel-development features | **Congenital short bowel syndrome** and **malrotation** can be part of the FLNA intestinal spectrum, especially in surviving males with 5′ FLNA variants. | van der Werf et al. (2013), DOI: https://doi.org/10.1038/gim.2012.123; Kapur et al. (2010), DOI: https://doi.org/10.1097/PAS.0b013e3181f0ae47 (werf2013congenitalshortbowel pages 1-2, kapur2010diffuseabnormallayering pages 14-14) |
| Variant classes reported | Small 5′ deletions/frameshifts in exon 2, splice-altering variants with exon skipping, intragenic duplications, and other hypomorphic loss-of-function alleles; several pathogenic mechanisms preserve some protein production and may permit male survival. | Gargiulo et al. (2007), DOI: https://doi.org/10.1086/513321; van der Werf et al. (2013), DOI: https://doi.org/10.1038/gim.2012.123; Jenkins et al. (2018), DOI: https://doi.org/10.1002/humu.23355; Kapur et al. (2010), DOI: https://doi.org/10.1097/PAS.0b013e3181f0ae47 (gargiulo2007filaminais pages 1-2, werf2013congenitalshortbowel pages 1-2, jenkins2018differentialregulationof pages 1-7, kapur2010diffuseabnormallayering pages 14-14) |
| Notable recurrent 5′ variants | Reported examples include **2-bp exon-2 deletions** such as **c.16_17delTC** and **c.65_66delAC**, causing frameshift/premature truncation in the N-terminus and linked to CIIP/CSBS phenotypes. | Gargiulo et al. (2007), DOI: https://doi.org/10.1086/513321; van der Werf et al. (2013), DOI: https://doi.org/10.1038/gim.2012.123 (gargiulo2007filaminais pages 1-2, werf2013congenitalshortbowel pages 1-2) |
| Mechanistic interpretation | Many intestinal disease alleles are best understood as **loss-of-function or hypomorphic** FLNA variants; tissue-specific expression of two FLNA transcripts/translation start sites likely helps explain why some variants preferentially produce intestinal phenotypes. | Jenkins et al. (2018), DOI: https://doi.org/10.1002/humu.23355; Gargiulo et al. (2007), DOI: https://doi.org/10.1086/513321 (jenkins2018differentialregulationof pages 1-7, gargiulo2007filaminais pages 1-2) |
| Extra-intestinal manifestations | Central nervous system involvement (especially **periventricular nodular heterotopia**), seizures or developmental findings, cardiovascular defects (e.g., PDA/ASD/valvular disease), pulmonary/connective-tissue features, megacystis/bladder dysfunction, and constipation may accompany intestinal disease. | Gargiulo et al. (2007), DOI: https://doi.org/10.1086/513321; Kapur et al. (2010), DOI: https://doi.org/10.1097/PAS.0b013e3181f0ae47; Rijckmans et al. preprint (2024), DOI: https://doi.org/10.21203/rs.3.rs-4546691/v1 (gargiulo2007filaminais pages 1-2, kapur2010diffuseabnormallayering pages 13-14, rijckmans2024counselingindividualswith pages 1-3) |
| Diagnostic evidence base | Diagnosis is supported by clinical pseudo-obstruction phenotype plus **FLNA molecular testing** and, when available, **full-thickness intestinal histopathology** showing smooth-muscle layering abnormalities. | Gargiulo et al. (2007), DOI: https://doi.org/10.1086/513321; Kapur et al. (2010), DOI: https://doi.org/10.1097/PAS.0b013e3181f0ae47; van der Werf et al. (2013), DOI: https://doi.org/10.1038/gim.2012.123 (gargiulo2007filaminais pages 1-2, kapur2010diffuseabnormallayering pages 11-12, werf2013congenitalshortbowel pages 1-2) |
| Cohort / family-level evidence | Landmark reports include an Italian kindred with **10 affected males across 4 generations** (9/10 died in early infancy), pathology series of FLNA-mutant patients with characteristic smooth-muscle abnormalities, and subsequent reports extending the phenotype to congenital short bowel and multisystem FLNA deficiency cohorts. | Gargiulo et al. (2007), DOI: https://doi.org/10.1086/513321; Kapur et al. (2010), DOI: https://doi.org/10.1097/PAS.0b013e3181f0ae47; Rijckmans et al. preprint (2024), DOI: https://doi.org/10.21203/rs.3.rs-4546691/v1 (gargiulo2007filaminais pages 1-2, kapur2010diffuseabnormallayering pages 13-14, rijckmans2024counselingindividualswith pages 1-3) |
| Management implications from reports | Severe cases may require **total parenteral nutrition**, repeated surgery/stoma procedures, and multidisciplinary surveillance for neurologic, cardiac, pulmonary, and gastrointestinal complications; the 2024 cohort emphasized lack of standardized follow-up guidelines. | Gargiulo et al. (2007), DOI: https://doi.org/10.1086/513321; Kapur et al. (2010), DOI: https://doi.org/10.1097/PAS.0b013e3181f0ae47; Rijckmans et al. preprint (2024), DOI: https://doi.org/10.21203/rs.3.rs-4546691/v1 (gargiulo2007filaminais pages 1-2, kapur2010diffuseabnormallayering pages 13-14, rijckmans2024counselingindividualswith pages 1-3) |


*Table: This table summarizes core identifiers, inheritance, defining clinical-pathology features, and landmark supporting publications for FLNA-associated X-linked intestinal pseudo-obstruction / FLNA-related CIPO. It is useful as a compact reference scaffold for a disease knowledge base entry.*

---

## 2. Etiology
### 2.1 Disease causal factors
**Primary cause: genetic**—pathogenic variants in **FLNA** (Xq28) encoding filamin A, an actin-binding cytoskeletal scaffold.

In the original CIIPX report, an X-linked recessive form mapped to Xq28 was shown to be caused by a **2-bp deletion in FLNA exon 2** producing a frameshift and predicted truncation near the N-terminus (with evidence for altered cytoskeletal actin organization in patient cells). (gargiulo2007filaminais pages 1-2)

### 2.2 Risk factors
**Genetic risk factor:** carrying pathogenic/hypomorphic FLNA variants that reduce effective filamin A function in intestinal smooth muscle.
* Example variant class: **exon 2 2-bp deletions** (frameshift/early stop), reported across CIIPX and CSBS presentations in males (e.g., c.16_17delTC; c.65_66delAC). (gargiulo2007filaminais pages 1-2, werf2013congenitalshortbowel pages 1-2)
* Structural variants: **intragenic duplications** and larger duplications including FLNA have been described in X-linked pseudo-obstruction pathology cohorts. (kapur2010diffuseabnormallayering pages 14-14, kapur2010diffuseabnormallayering pages 13-14)

**Non-genetic/environmental risk factors:** No FLNA-specific environmental risk factors were identified in the retrieved evidence; most work supports a monogenic etiology.

### 2.3 Protective factors
Not established for FLNA-related intestinal pseudo-obstruction in the retrieved literature. A conceptual “protective” mechanism is **residual FLNA function** (hypomorphic alleles / alternative transcript usage) permitting survival in hemizygous males, but this is genetic mechanism rather than an identified protective exposure. (jenkins2018differentialregulationof pages 1-7, kapur2010diffuseabnormallayering pages 14-14)

### 2.4 Gene–environment interactions
No specific GxE interactions for FLNA intestinal pseudo-obstruction were found in the retrieved evidence.

---

## 3. Phenotypes
### 3.1 Core gastrointestinal phenotype (symptoms/signs)
Typical features are those of functional obstruction:
* Abdominal distension, vomiting/feeding intolerance, constipation or altered bowel habits, failure to thrive, and recurrent “obstructive” episodes without a mechanical lesion. (gargiulo2007filaminais pages 1-2, jenkins2018differentialregulationof pages 1-7)

**HPO suggestions (non-exhaustive):**
* Intestinal pseudo-obstruction (HP:0004396)
* Vomiting (HP:0002013)
* Abdominal distension (HP:0003270)
* Constipation (HP:0002019)
* Failure to thrive (HP:0001508)

### 3.2 Developmental/anatomic GI manifestations
* **Congenital short bowel syndrome** (markedly shortened small intestine often with malrotation) can be the presenting feature in males with FLNA variants; van der Werf et al. cite normal neonatal small-bowel length ~275 cm versus ~50 cm in CSBS. (werf2013congenitalshortbowel pages 1-2)
* **Malrotation** is recurrently noted in the FLNA spectrum. (werf2013congenitalshortbowel pages 1-2, kapur2010diffuseabnormallayering pages 14-14)

**HPO suggestions:**
* Abnormality of intestinal length (HP:0012098)
* Intestinal malrotation (HP:0002566)

### 3.3 Extra-intestinal manifestations (multisystem)
Reported extracolonic features across FLNA loss-of-function cohorts and X-linked pseudo-obstruction pathology series include:
* **CNS involvement** (e.g., PVNH spectrum; seizures/developmental findings in some). (gargiulo2007filaminais pages 1-2, kapur2010diffuseabnormallayering pages 13-14)
* **Cardiovascular findings** (e.g., PDA/ASD in tabled cases; broader FLNA LOF cohorts report cardiovascular involvement). (kapur2010diffuseabnormallayering pages 13-14, rijckmans2024counselingindividualswith pages 1-3)
* **Urogenital/bladder** involvement such as megacystis reported in X-linked pseudo-obstruction case tables. (kapur2010diffuseabnormallayering pages 11-12)

**HPO suggestions:**
* Periventricular nodular heterotopia (HP:0002123)
* Patent ductus arteriosus (HP:0001643)
* Atrial septal defect (HP:0001631)
* Megacystis (HP:0002021)

### 3.4 Frequencies and quantitative phenotype data
Disease-specific phenotype frequencies for “FLNA intestinal pseudo-obstruction” are limited because published evidence is often family- or case-series-based.

However, in a recent **FLNA loss-of-function cohort** (monocentric, n=24 index patients), the authors reported **epilepsy in 84%** and **cardiovascular involvement in 56%** (not specific to CIPO, but relevant to systemic surveillance for FLNA deficiency). Publication date: Oct 2024 (preprint). URL: https://doi.org/10.21203/rs.3.rs-4546691/v1 (rijckmans2024counselingindividualswith pages 1-3)

---

## 4. Genetic / molecular information
### 4.1 Causal gene
* **FLNA** (filamin A). (gargiulo2007filaminais pages 1-2, jenkins2018differentialregulationof pages 1-7)

### 4.2 Pathogenic variant spectrum (reported classes)
Reported FLNA variant classes in X-linked intestinal pseudo-obstruction / FLNA-CIPO include:
* **Frameshift deletions in exon 2** (e.g., 2-bp deletions) causing early truncation/hypomorphic expression via alternative initiation. (gargiulo2007filaminais pages 1-2, werf2013congenitalshortbowel pages 1-2)
* **Splice-altering variants / exon skipping** producing atypical/hypomorphic loss-of-function effects. (jenkins2018differentialregulationof pages 1-7)
* **Intragenic duplications** and larger duplications including FLNA in pathology-defined X-linked pseudo-obstruction cohorts. (kapur2010diffuseabnormallayering pages 14-14, kapur2010diffuseabnormallayering pages 13-14)

### 4.3 Functional consequences (LOF vs GOF)
FLNA disorders are often framed as:
* **Loss-of-function (LOF)** variants: reduced/absent expression, associated with PVNH and multisystem findings, and can include CIPO/intestinal pseudo-obstruction phenotypes. (jenkins2018differentialregulationof pages 1-7, rijckmans2024counselingindividualswith pages 1-3)

A mechanistic clue to phenotype specificity is tissue-dependent regulation of **two FLNA transcripts / translation start sites**, with intestinal smooth muscle showing particular dependence on the long isoform; this provides a plausible explanation for why some 5′ variants produce prominent intestinal disease and male survivorship (hypomorphic alleles). (jenkins2018differentialregulationof pages 1-7)

### 4.4 Inheritance pattern
The original CIIPX kindred was described as **X-linked recessive** with 10 affected males across 4 generations. (gargiulo2007filaminais pages 1-2)

More broadly, “FLNA deficiency” due to LOF variants is commonly counseled as **X-linked dominant with male lethality**, with variable female multisystem involvement; GI symptoms including constipation and CIPO are included in the phenotype spectrum. (rijckmans2024counselingindividualswith pages 1-3)

### 4.5 Population allele frequency
Population allele-frequency values (e.g., gnomAD) for specific CIPO-associated FLNA variants were not retrievable from the current evidence set.

---

## 5. Environmental information
No non-genetic environmental contributors were identified in the retrieved evidence; FLNA intestinal pseudo-obstruction is best supported as a monogenic disorder with secondary complications (e.g., infections related to parenteral nutrition) rather than environmentally initiated disease.

---

## 6. Mechanism / pathophysiology
### 6.1 Causal chain (current model)
1. **Pathogenic FLNA variant** → reduced/hypomorphic filamin A function in intestinal smooth muscle (gargiulo2007filaminais pages 1-2, jenkins2018differentialregulationof pages 1-7)
2. **Cytoskeletal/contractile architecture disruption** (patient cells show abnormal actin cytoskeletal organization) (gargiulo2007filaminais pages 1-2)
3. **Visceral myopathy phenotype** with **abnormal smooth muscle layering** in small intestine (microanatomic correlate) (kapur2010diffuseabnormallayering pages 13-14, kapur2010diffuseabnormallayering pages 14-14)
4. **Impaired peristalsis** → clinical pseudo-obstruction, intestinal failure, and need for parenteral nutrition/surgical interventions (kapur2010diffuseabnormallayering pages 13-14, jenkins2018differentialregulationof pages 1-7)

### 6.2 Key tissues/cell types
* **Visceral smooth muscle cells** (primary effector tissue in myopathic cases). (kapur2010diffuseabnormallayering pages 13-14, jenkins2018differentialregulationof pages 1-7)
  * **CL suggestion:** Smooth muscle cell (CL:0000192)
* **Enteric nervous system (ENS)** may show abnormalities in some cases, but the hallmark pathology in FLNA-XIPO emphasizes smooth muscle layering/myopathy. (kapur2010diffuseabnormallayering pages 13-14, gargiulo2007filaminais pages 1-2)
  * **CL suggestion:** Enteric neuron (CL:0000700)

### 6.3 Pathways and ontology suggestions
**GO biological process (suggestions consistent with evidence):**
* Smooth muscle contraction (GO:0006939)
* Actin filament organization (GO:0007015)
* Regulation of cell migration (GO:0030334)

**GO cellular component (suggestions):**
* Actin cytoskeleton (GO:0015629)

---

## 7. Anatomical structures affected
### 7.1 Organ/system level
* Primary: **small intestine** (shortened length is “nearly constant” in CIIPX pathology series; abnormal layering described in small intestine). (kapur2010diffuseabnormallayering pages 14-14)
* Often involved: colon and other GI segments in broader CIPO phenotypes. (giorgio2011chronicintestinalpseudoobstruction pages 10-12)

**UBERON suggestions:**
* Small intestine (UBERON:0002108)
* Colon (UBERON:0001155)

### 7.2 Subcellular localization
Mechanistically centered on **actin cytoskeletal networks** (filamin A is an actin-binding scaffold), supported by cytoskeletal abnormalities in patient cells. (gargiulo2007filaminais pages 1-2)

---

## 8. Temporal development
### 8.1 Onset
In the CIIPX kindred, disease occurred in male infants with very early mortality (9/10 died in the first months of life). (gargiulo2007filaminais pages 1-2)

In broader pediatric pseudo-obstruction populations, neonatal onset is common (e.g., 26/43 neonatal onset in a national Dutch PIPO cohort, though not FLNA-specific). (demirok2025incidencediagnosticstherapeutic pages 1-2)

### 8.2 Progression / course
CIPO generally has prolonged diagnostic delay and high care burden; an adult CIPO review reports a **median 8-year delay to diagnosis** and that **~88% underwent ~3 unnecessary surgeries**, with **30–50% requiring long-term TPN/HPN** and **mortality ~10–34%** (general CIPO data; not FLNA-specific). (giorgio2011chronicintestinalpseudoobstruction pages 10-12)

---

## 9. Inheritance and population
### 9.1 Epidemiology
Disease-specific prevalence of FLNA intestinal pseudo-obstruction is not well quantified in the retrieved evidence.

For pediatric intestinal pseudo-obstruction broadly, a 20-year Dutch national cohort study reported:
* **Mean incidence:** **0.008/100,000/year** (Netherlands, 2000–2020; n=43) (demirok2025incidencediagnosticstherapeutic pages 1-2)
* **Mortality:** **6%** (2/43) (demirok2025incidencediagnosticstherapeutic pages 1-2)
* **Healthcare utilization:** median **22.5 admissions** (range 1–176) over long follow-up (demirok2025incidencediagnosticstherapeutic pages 1-2)

### 9.2 Sex ratio and penetrance
The CIIPX kindred and pathology series emphasize strong sex effects consistent with X-linked inheritance, with severe male involvement and survival depending on residual/hypomorphic expression in some variant classes. (gargiulo2007filaminais pages 1-2, jenkins2018differentialregulationof pages 1-7, kapur2010diffuseabnormallayering pages 14-14)

---

## 10. Diagnostics
### 10.1 Clinical evaluation and test modalities
**Core principle:** demonstrate obstruction-like phenotype while excluding mechanical obstruction.

**Imaging**
* Pediatric review: plain abdominal X-ray for air-fluid levels and dilated bowel; contrast studies to exclude mechanical obstruction; **CT/MRI enterography** proposed as first line; **cine-MRI** as non-invasive motility assessment. (turcotte2022pediatricintestinalpseudoobstruction pages 5-6)

**Manometry**
* Small-bowel / antroduodenal manometry helps classify neuropathic vs myopathic patterns (e.g., low amplitude patterns suggesting myopathy), but limitations include invasiveness and incomplete correlation with histology. (turcotte2022pediatricintestinalpseudoobstruction pages 5-6, giorgio2011chronicintestinalpseudoobstruction pages 10-12)

**Histopathology**
* Full-thickness biopsy can identify smooth muscle, ENS, or ICC abnormalities; ESPGHAN recommends specialized centers and labeling panels in pediatric contexts. (turcotte2022pediatricintestinalpseudoobstruction pages 5-6)
* In FLNA X-linked cases, hallmark smooth muscle abnormal layering supports diagnosis of a visceral myopathy subtype. (kapur2010diffuseabnormallayering pages 13-14, kapur2010diffuseabnormallayering pages 14-14)

**Genetic testing**
* In suspected hereditary CIPO/PIPO, metabolic and genetic screening are part of diagnostic strategies in cohort studies. (demirok2025incidencediagnosticstherapeutic pages 1-2)
* For FLNA disease, molecular diagnosis in a recent cohort relied on Sanger sequencing, MLPA, and NGS panels (for malformations of cortical development) rather than WES/WGS. (rijckmans2024counselingindividualswith pages 3-5)

### 10.2 Formal pediatric diagnostic criteria (PIPO)
A pediatric review reports that PIPO diagnostic criteria require **two of four** findings: (1) objective small-bowel neuromuscular involvement (manometry/histopath/transit); (2) recurrent/persistent small-bowel dilation with air-fluid levels; (3) known genetic/metabolic abnormality; (4) feeding intolerance requiring supplemental enteral or parenteral nutrition. (gamboa2019pediatricintestinalpseudoobstruction pages 1-2)

### 10.3 Differential diagnosis
Broader CIPO diagnostic workups explicitly screen for secondary causes including metabolic/endocrine and immune/paraneoplastic disorders and mitochondrial disease (e.g., MNGIE). (giorgio2011chronicintestinalpseudoobstruction pages 10-12)

---

## 11. Outcome / prognosis
### 11.1 Mortality and severe outcomes
* CIIPX kindred: **9/10 affected males died in the first months of life** (highly severe familial presentation). (gargiulo2007filaminais pages 1-2)
* General CIPO: adult review reports **mortality ~10–34%** and **30–50% long-term TPN/HPN** requirement (not FLNA-specific). (giorgio2011chronicintestinalpseudoobstruction pages 10-12)
* PIPO Netherlands cohort: **6% mortality** over long follow-up (not FLNA-specific). (demirok2025incidencediagnosticstherapeutic pages 1-2)

### 11.2 Morbidity / QoL
Parenteral nutrition is life-saving but has major risks (central line infection, thrombosis, liver disease) and contributes substantially to morbidity and quality-of-life burden in pediatric pseudo-obstruction. (turcotte2022pediatricintestinalpseudoobstruction pages 5-6)

---

## 12. Treatment
### 12.1 Supportive care (cornerstones)
In pediatric pseudo-obstruction cohorts, treatment is commonly structured around:
* **Nutritional support** (enteral when possible; PN in severe cases) and **surgical interventions** as “cornerstones” of care. (demirok2025incidencediagnosticstherapeutic pages 1-2)

**MAXO suggestions:**
* Parenteral nutrition (MAXO:0000878)
* Enteral nutrition (MAXO:0000879)

### 12.2 Pharmacotherapy
Evidence for CIPO (general, not FLNA-specific) includes use of prokinetics and other agents:
* Adult review cites studies of **cisapride**, **erythromycin** (positive response in small case series), and **octreotide** effects on motility/bacterial overgrowth; antibiotic management of SIBO (e.g., rifaximin) is also referenced. (giorgio2011chronicintestinalpseudoobstruction pages 20-21)

Pediatric review emphasizes that there is **no universally recommended prokinetic regimen** for most pediatric PIPO patients and highlights supportive goals. (turcotte2022pediatricintestinalpseudoobstruction pages 5-6)

**MAXO suggestions:**
* Prokinetic therapy (MAXO:0001020)
* Antibiotic therapy (MAXO:0000648)

### 12.3 Surgical and interventional options
Reported and referenced options in general CIPO/PIPO literature include:
* Stomas/ileostomy and other diversion or decompressive surgeries in severe cases (also seen in FLNA-XIPO pathology cohorts). (kapur2010diffuseabnormallayering pages 13-14)
* Intestinal transplantation / multivisceral transplantation in advanced intestinal failure (general CIPO references include a series of “100 multivisceral transplants at a single center”). (giorgio2011chronicintestinalpseudoobstruction pages 20-21)

**MAXO suggestions:**
* Ileostomy (MAXO:0001060)
* Intestinal transplantation (MAXO:0001109)

### 12.4 Real-world implementation / systems of care
A 2024 FLNA LOF cohort emphasizes that **systematic multidisciplinary follow-up** (notably cardiology screening) was often lacking and that less overt symptoms (e.g., constipation) may be underreported, arguing for standardized surveillance in FLNA deficiency. (rijckmans2024counselingindividualswith pages 1-3)

### 12.5 Clinical trials (FLNA-specific)
A prospective observational registry study (Italy) is assessing the **diagnostic yield of Sanger sequencing of ACTG2 and FLNA** in adult idiopathic CIPO with a myopathic phenotype suggested by reduced/absent distal esophageal contractility on HRM.
* **NCT ID:** NCT07448753
* **First posted:** 2026-03-04
* **Start date:** 2025-09-17
* ClinicalTrials.gov URL: https://clinicaltrials.gov/study/NCT07448753 (registry data captured in tool context). (NCT07448753 chunk 1)

---

## 13. Prevention
No primary prevention is currently established for monogenic FLNA intestinal pseudo-obstruction.

**Key prevention strategy is genetic counseling and surveillance** in families with pathogenic FLNA variants, given X-linked inheritance and multisystem risks; recent cohort evidence emphasizes the need for multidisciplinary follow-up and absence of uniform guidelines. (rijckmans2024counselingindividualswith pages 1-3)

**MAXO suggestions:**
* Genetic counseling (MAXO:0000079)
* Cascade genetic testing (MAXO:0000754)

---

## 14. Other species / natural disease
No evidence of FLNA-driven intestinal pseudo-obstruction in non-human species was retrieved.

A naturally occurring visceral smooth muscle disorder presenting as chronic intestinal pseudo-obstruction has been reported in a Bengal cat, illustrating comparative “visceral myopathy” pathology but not implicating FLNA. (OpenTargets Search: intestinal pseudo-obstruction,chronic intestinal pseudo-obstruction-FLNA)

---

## 15. Model organisms
A 2023 multidisciplinary forum report on visceral myopathy notes that **animal models are scarce**, limiting mechanistic and therapeutic development in this general disease area (not FLNA-specific). (OpenTargets Search: intestinal pseudo-obstruction,chronic intestinal pseudo-obstruction-FLNA)

No FLNA-specific intestinal pseudo-obstruction animal model evidence was retrievable in the current document set.

---

## 2023–2024 highlights (prioritized)
1. **2024 cohort-level expert perspective:** A cross-sectional cohort of **24 index patients with FLNA LOF** variants reported high rates of epilepsy (84%) and cardiovascular involvement (56%), and highlighted gaps in systematic multidisciplinary follow-up; GI manifestations included constipation and chronic intestinal pseudo-obstruction within the phenotypic spectrum. Publication date Oct 2024 (preprint). URL: https://doi.org/10.21203/rs.3.rs-4546691/v1 (rijckmans2024counselingindividualswith pages 1-3)
2. **2023 genomic medicine approach:** A WGS analysis of visceral myopathy phenotypes in the 100,000 Genomes Project screened a virtual panel including FLNA (n=76 VM phenotypes), supporting WGS/panel strategies for related motility disorders (though FLNA-specific hit rates were not provided in the excerpt). Publication date Jun 2023. URL: https://doi.org/10.1007/s44162-023-00012-z (geraghty2023useofwhole pages 1-2)

---

## Evidence limitations / gaps for knowledge-base completion
* **OMIM/Orphanet/ICD codes** for the specific “FLNA intestinal pseudo-obstruction” entity were not captured in the retrieved evidence and require database lookup.
* **Variant-level curation** (ClinVar assertions, allele frequencies, variant-to-phenotype mapping) was not available in the current texts.
* **2023–2024 FLNA intestine-mechanism papers** were referenced in the evidence stream but not retrievable in full text here (e.g., the 2023 Human Molecular Genetics paper on the long FLNA isoform and intestinal motility was flagged as unobtainable), limiting the ability to provide 2023–2024 primary mechanistic quotations.


References

1. (gargiulo2007filaminais pages 1-2): Annagiusi Gargiulo, Renata Auricchio, Maria Vittoria Barone, Gabriella Cotugno, William Reardon, Peter J. Milla, Andrea Ballabio, Alfredo Ciccodicola, and Alberto Auricchio. Filamin a is mutated in x-linked chronic idiopathic intestinal pseudo-obstruction with central nervous system involvement. American journal of human genetics, 80 4:751-8, Apr 2007. URL: https://doi.org/10.1086/513321, doi:10.1086/513321. This article has 148 citations and is from a highest quality peer-reviewed journal.

2. (kapur2010diffuseabnormallayering pages 13-14): Raj P. Kapur, Stephen P. Robertson, Mark C. Hannibal, Laura S. Finn, Timothy Morgan, Margriet van Kogelenberg, and David J. Loren. Diffuse abnormal layering of small intestinal smooth muscle is present in patients with flna mutations and x-linked intestinal pseudo-obstruction. The American Journal of Surgical Pathology, 34:1528-1543, Oct 2010. URL: https://doi.org/10.1097/pas.0b013e3181f0ae47, doi:10.1097/pas.0b013e3181f0ae47. This article has 77 citations.

3. (jenkins2018differentialregulationof pages 1-7): Zandra A Jenkins, Alison Macharg, Cheng-Yee Chang, Margriet van Kogelenberg, Tim Morgan, Sophia Frentz, Wenhua Wei, Jacek Pilch, Mark Hannibal, Nicola Foulds, George McGillivray, Richard J Leventer, Sixto García-Miñaúr, Stuart Sugito, Scott Nightingale, David M Markie, Tracy Dudding, Raj P Kapur, and Stephen P Robertson. Differential regulation of two flna transcripts explains some of the phenotypic heterogeneity in the loss‐of‐function filaminopathies. Human Mutation, 39:103-113, Jan 2018. URL: https://doi.org/10.1002/humu.23355, doi:10.1002/humu.23355. This article has 38 citations and is from a domain leading peer-reviewed journal.

4. (kapur2010diffuseabnormallayering pages 14-14): Raj P. Kapur, Stephen P. Robertson, Mark C. Hannibal, Laura S. Finn, Timothy Morgan, Margriet van Kogelenberg, and David J. Loren. Diffuse abnormal layering of small intestinal smooth muscle is present in patients with flna mutations and x-linked intestinal pseudo-obstruction. The American Journal of Surgical Pathology, 34:1528-1543, Oct 2010. URL: https://doi.org/10.1097/pas.0b013e3181f0ae47, doi:10.1097/pas.0b013e3181f0ae47. This article has 77 citations.

5. (OpenTargets Search: intestinal pseudo-obstruction,chronic intestinal pseudo-obstruction-FLNA): Open Targets Query (intestinal pseudo-obstruction,chronic intestinal pseudo-obstruction-FLNA, 4 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

6. (NCT07448753 chunk 1): Marina Coletta. ACTG2/FLNA Testing Yield in Adult Idiopathic Chronic Intestinal Pseudo-Obstruction (CIPO) With Reduced/Absent Distal Esophageal Contractility. Marina Coletta. 2025. ClinicalTrials.gov Identifier: NCT07448753

7. (werf2013congenitalshortbowel pages 1-2): Christine S. van der Werf, Yunia Sribudiani, Joke B.G.M. Verheij, Matthew Carroll, Edward O’Loughlin, Chien-Huan Chen, Alice S. Brooks, M. Kathryn Liszewski, John P. Atkinson, and Robert M.W. Hofstra. Congenital short bowel syndrome as the presenting symptom in male patients with flna mutations. Genetics in Medicine, 15:310-313, Apr 2013. URL: https://doi.org/10.1038/gim.2012.123, doi:10.1038/gim.2012.123. This article has 51 citations and is from a highest quality peer-reviewed journal.

8. (rijckmans2024counselingindividualswith pages 1-3): Ellen RIJCKMANS, Lars P. De Strooper, Kathelijn Keymolen, Jessica Rosenblum, Bart Loeys, Marije Meuwissen, Anna C. Jansen, and Katrien Stouffs. Counseling individuals with pathogenic loss-of-function variants in flna – learning points from a cross-sectional cohort study. Unknown journal, Oct 2024. URL: https://doi.org/10.21203/rs.3.rs-4546691/v1, doi:10.21203/rs.3.rs-4546691/v1.

9. (kapur2010diffuseabnormallayering pages 11-12): Raj P. Kapur, Stephen P. Robertson, Mark C. Hannibal, Laura S. Finn, Timothy Morgan, Margriet van Kogelenberg, and David J. Loren. Diffuse abnormal layering of small intestinal smooth muscle is present in patients with flna mutations and x-linked intestinal pseudo-obstruction. The American Journal of Surgical Pathology, 34:1528-1543, Oct 2010. URL: https://doi.org/10.1097/pas.0b013e3181f0ae47, doi:10.1097/pas.0b013e3181f0ae47. This article has 77 citations.

10. (giorgio2011chronicintestinalpseudoobstruction pages 10-12): Roberto De Giorgio, Rosanna F. Cogliandro, Giovanni Barbara, Roberto Corinaldesi, and Vincenzo Stanghellini. Chronic intestinal pseudo-obstruction: clinical features, diagnosis, and therapy. Gastroenterology clinics of North America, 40 4:787-807, Dec 2011. URL: https://doi.org/10.1016/j.gtc.2011.09.005, doi:10.1016/j.gtc.2011.09.005. This article has 185 citations and is from a peer-reviewed journal.

11. (demirok2025incidencediagnosticstherapeutic pages 1-2): Aysenur Demirok, Sjoerd C. J. Nagelkerke, Malou Veldt, Ramon Gorter, Justin R. de Jong, Gerard M. Damen, Barbara A. E. de Koning, Caroline Meijer, Patrick F. van Rheenen, Victorien M. Wolters, Marc A. Benninga, and Merit M. Tabbers. Incidence, diagnostics, therapeutic management and outcomes of paediatric intestinal pseudo‐obstruction in the netherlands: a 20‐year retrospective cohort study. Journal of Pediatric Gastroenterology and Nutrition, 80:34-45, Nov 2025. URL: https://doi.org/10.1002/jpn3.12400, doi:10.1002/jpn3.12400. This article has 6 citations and is from a peer-reviewed journal.

12. (turcotte2022pediatricintestinalpseudoobstruction pages 5-6): Marie-Catherine Turcotte and Christophe Faure. Pediatric intestinal pseudo-obstruction: progress and challenges. Frontiers in Pediatrics, Apr 2022. URL: https://doi.org/10.3389/fped.2022.837462, doi:10.3389/fped.2022.837462. This article has 31 citations.

13. (rijckmans2024counselingindividualswith pages 3-5): Ellen RIJCKMANS, Lars P. De Strooper, Kathelijn Keymolen, Jessica Rosenblum, Bart Loeys, Marije Meuwissen, Anna C. Jansen, and Katrien Stouffs. Counseling individuals with pathogenic loss-of-function variants in flna – learning points from a cross-sectional cohort study. Unknown journal, Oct 2024. URL: https://doi.org/10.21203/rs.3.rs-4546691/v1, doi:10.21203/rs.3.rs-4546691/v1.

14. (gamboa2019pediatricintestinalpseudoobstruction pages 1-2): Heidi E. Gamboa and Manu Sood. Pediatric intestinal pseudo-obstruction in the era of genetic sequencing. Current Gastroenterology Reports, Dec 2019. URL: https://doi.org/10.1007/s11894-019-0737-y, doi:10.1007/s11894-019-0737-y. This article has 43 citations.

15. (giorgio2011chronicintestinalpseudoobstruction pages 20-21): Roberto De Giorgio, Rosanna F. Cogliandro, Giovanni Barbara, Roberto Corinaldesi, and Vincenzo Stanghellini. Chronic intestinal pseudo-obstruction: clinical features, diagnosis, and therapy. Gastroenterology clinics of North America, 40 4:787-807, Dec 2011. URL: https://doi.org/10.1016/j.gtc.2011.09.005, doi:10.1016/j.gtc.2011.09.005. This article has 185 citations and is from a peer-reviewed journal.

16. (geraghty2023useofwhole pages 1-2): Robert M. Geraghty, Sarah Orr, Eric Olinger, Ruxandra Neatu, Miguel Barroso-Gil, Holly Mabillard, Genomics England Research Consortium, Ian Wilson, and John A. Sayer. Use of whole genome sequencing to determine the genetic basis of visceral myopathies including prune belly syndrome. Journal of Rare Diseases (Berlin, Germany), Jun 2023. URL: https://doi.org/10.1007/s44162-023-00012-z, doi:10.1007/s44162-023-00012-z. This article has 9 citations.
