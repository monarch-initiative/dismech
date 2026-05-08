---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-08T09:19:52.232033'
end_time: '2026-05-08T09:35:56.858177'
duration_seconds: 964.63
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Brucellosis
  mondo_id: ''
  category: Infectious
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 55
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Brucellosis
- **MONDO ID:**  (if available)
- **Category:** Infectious

## Research Objectives

Please provide a comprehensive research report on **Brucellosis** covering all of the
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
- **Disease Name:** Brucellosis
- **MONDO ID:**  (if available)
- **Category:** Infectious

## Research Objectives

Please provide a comprehensive research report on **Brucellosis** covering all of the
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


# Brucellosis (Disease Characteristics Research Report)

## Target disease
- **Disease name:** Brucellosis (human brucellosis)
- **Category:** Infectious; zoonotic bacterial disease
- **MONDO ID:** Not retrievable from the currently available, citable full-text corpus in this run (reported as unavailable rather than inferred) (ayoubi2024themanyfaces pages 1-2).

## Executive summary (current understanding; 2023–2024 priority)
Brucellosis is a multisystem zoonotic infection caused by *Brucella* spp. and remains widely endemic and underdiagnosed, with modern global modeling estimating **~2.1 million human cases/year**—substantially higher than historically assumed (Laine et al., **Sep 2023**, *Emerging Infectious Diseases*, https://doi.org/10.3201/eid2909.230052) (laine2023globalestimateof pages 1-2). Transmission is primarily foodborne (unpasteurized dairy) and occupational (animal contact), but documented additional routes include inhalation of aerosols and vertical transmission in special contexts (ayoubi2024themanyfaces pages 1-2, moriyon2023brucellosisandone pages 1-2, huy2024exploringtheimpact pages 1-2). Diagnostic progress in 2023–2024 emphasizes combining serologic tests and newer immunoassay approaches; pooled evidence suggests Rose Bengal, ELISA, and PCR can all perform well, but certainty of evidence is often low and algorithms outperform single tests in practice (Freire et al., **Mar 2024**, https://doi.org/10.1371/journal.pntd.0012030; Loubet et al., **Sep 2024**, https://doi.org/10.1371/journal.pntd.0012442) (freire2024diagnosisofhuman pages 9-11, loubet2024diagnosisofbrucellosis pages 1-2). Treatment evidence in 2024 network meta-analyses supports **aminoglycoside-containing doxycycline regimens** and some triple-therapy strategies as more effective than doxycycline–rifampicin for overall failure/relapse endpoints, though evidence certainty varies (Silva et al., **Mar 2024**, https://doi.org/10.1371/journal.pntd.0012010; Huang et al., **Aug 2024**, https://doi.org/10.1371/journal.pntd.0012405; Maduranga et al., **Aug 2024**, https://doi.org/10.1038/s41598-024-69669-w) (silva2024efficacyandsafety pages 18-21, huang2024updatedtherapeuticoptions pages 1-2, maduranga2024asystematicreview pages 3-6).

A compact table of key quantitative statistics is provided here:

| Domain | Key finding (with numbers) | Population/setting | Study type | Publication (first author year journal) | Publication date/month | URL | Citations |
|---|---|---|---|---|---|---|---|
| Global burden/incidence | Conservative global annual incidence estimate: **2.1 million cases/year**; highest burden in **Africa and Asia** | Global | Modeling study using international surveillance/public health data | Laine 2023 *Emerging Infectious Diseases* | 2023 Sep | https://doi.org/10.3201/eid2909.230052 | (laine2023globalestimateof pages 1-2) |
| Global prevalence | Pooled prevalence **15.49%** (95% CI **12.01–18.97**); Asia **16.65%**, Africa **16.28%**, Americas **11.09%**; male **19.11%** vs female **13.97%** | 69 studies worldwide | Systematic review and meta-analysis | Sherasiya 2024 preprint | 2024 Sep | https://doi.org/10.21203/rs.3.rs-4929733/v1 | (sherasiya2024globalprevalenceof pages 1-4, sherasiya2024globalprevalenceof pages 7-10) |
| National epidemiology | **2,489** culture-confirmed cases (2004–2022); **99.8%** bacteraemic; **64%** male; mean age **30.5 y**; **B. melitensis 99.6%**; annual incidence **1.6/100,000** overall, **6.6/100,000** Arab, **5.5/100,000** Druze, **0.18/100,000** Jewish; Arab South District peak **41.0/100,000** in 2012 | Israel national surveillance, 2004–2022 | National retrospective epidemiology study | Weinberger 2024 *Epidemiology and Infection* | 2024 May | https://doi.org/10.1017/S0950268824000803 | (weinberger2024nationalepidemiologyof pages 2-3, weinberger2024nationalepidemiologyof pages 1-2) |
| Regional epidemiology | Overall pooled seroprevalence **5.0%** (95% CI **3.0–6.0**); human **6.9%** (95% CI **4.9–8.8**); cattle **3.5%** (95% CI **2.2–4.7**); heterogeneity **I² 99.61%** | Ethiopia, 39 studies (2015–2024) | Systematic review and meta-analysis | Dagnaw 2024 *BMC Public Health* | 2024 Dec | https://doi.org/10.1186/s12889-024-21042-2 | (dagnaw2024humanandanimal pages 1-2) |
| Risk factors | Major risks: raw milk/unpasteurized dairy, contact with aborted materials/fetuses, occupation (livestock owners, abattoir workers, veterinarians), direct animal contact | Global/Ethiopia/Israel | Mixed: modeling, meta-analysis, national epidemiology | Multiple recent sources | 2023–2024 | https://doi.org/10.3201/eid2909.230052 | (weinberger2024nationalepidemiologyof pages 1-2, laine2023globalestimateof pages 1-2, sherasiya2024globalprevalenceof pages 1-4, dagnaw2024humanandanimal pages 1-2) |
| Diagnostic accuracy | **Rose Bengal** pooled sensitivity/specificity vs culture: **89.7% / 94.1%**; vs culture and/or SAT: **96.6% / 97.9%** | Symptomatic suspected human brucellosis | Systematic review and meta-analysis | Freire 2024 *PLOS Neglected Tropical Diseases* | 2024 Mar | https://doi.org/10.1371/journal.pntd.0012030 | (freire2024diagnosisofhuman pages 9-11, freire2024diagnosisofhuman pages 1-2) |
| Diagnostic accuracy | **SAT** pooled sensitivity/specificity vs culture: **89.2% / 95.6%** | Symptomatic suspected human brucellosis | Systematic review and meta-analysis | Freire 2024 *PLOS Neglected Tropical Diseases* | 2024 Mar | https://doi.org/10.1371/journal.pntd.0012030 | (freire2024diagnosisofhuman pages 9-11) |
| Diagnostic accuracy | **IgG ELISA** pooled sensitivity/specificity vs culture: **82.9% / 96.2%**; specificity vs culture and/or SAT reached **99.0%** | Symptomatic suspected human brucellosis | Systematic review and meta-analysis | Freire 2024 *PLOS Neglected Tropical Diseases* | 2024 Mar | https://doi.org/10.1371/journal.pntd.0012030 | (freire2024diagnosisofhuman pages 9-11) |
| Diagnostic accuracy | **IgM ELISA** pooled sensitivity/specificity vs culture: **84.5% / 95.3%** | Symptomatic suspected human brucellosis | Systematic review and meta-analysis | Freire 2024 *PLOS Neglected Tropical Diseases* | 2024 Mar | https://doi.org/10.1371/journal.pntd.0012030 | (freire2024diagnosisofhuman pages 9-11) |
| Diagnostic accuracy | **Qualitative PCR** pooled sensitivity/specificity vs culture: **96.4% / 98.1%**; **real-time PCR**: **81.9% / 91.5%** | Symptomatic suspected human brucellosis | Systematic review and meta-analysis | Freire 2024 *PLOS Neglected Tropical Diseases* | 2024 Mar | https://doi.org/10.1371/journal.pntd.0012030 | (freire2024diagnosisofhuman pages 9-11) |
| Diagnostic algorithm | Combined **RBT + Brucellacapt + ELISA IgM/IgG** achieved **90.5% sensitivity**, **99.7% specificity**, **92.4% PPV**, **99.6% NPV** | French National Reference Center, 3,587 sera; 148 confirmed cases | Retrospective diagnostic accuracy study | Loubet 2024 *PLOS Neglected Tropical Diseases* | 2024 Sep | https://doi.org/10.1371/journal.pntd.0012442 | (loubet2024diagnosisofbrucellosis pages 1-2) |
| Treatment comparative efficacy | Standard **doxycycline + rifampicin** had higher failure risk than triple therapy adding **streptomycin**: **RR 1.98** (95% CI **1.17–3.35**); and adding **levofloxacin**: **RR 2.98** (95% CI **1.67–5.32**) | Human brucellosis, 34 studies, 4,182 participants | Systematic review and meta-analysis | Maduranga 2024 *Scientific Reports* | 2024 Aug | https://doi.org/10.1038/s41598-024-69669-w | (maduranga2024asystematicreview pages 3-6, maduranga2024asystematicreview pages 1-2) |
| Treatment comparative efficacy | **Doxycycline + rifampicin** had higher relapse risk than triple therapy with **streptomycin**: **RR 22.12** (95% CI **3.48–140.52**); and with **levofloxacin**: **RR 4.61** (95% CI **2.20–9.66**) | Human brucellosis, 34 studies, 4,182 participants | Systematic review and meta-analysis | Maduranga 2024 *Scientific Reports* | 2024 Aug | https://doi.org/10.1038/s41598-024-69669-w | (maduranga2024asystematicreview pages 3-6, maduranga2024asystematicreview pages 1-2) |
| Treatment comparative efficacy | In NMA, **doxycycline + rifampicin** had higher failure risk than **doxycycline + streptomycin**: **RR 1.96** (95% CI **1.27–3.01**); **doxycycline + gentamicin** lower than doxycycline + rifampicin: **RR 0.30** (95% CI **0.14–0.62**) | 31 RCTs, 4,167 patients | Systematic review and network meta-analysis | Silva 2024 *PLOS Neglected Tropical Diseases* | 2024 Mar | https://doi.org/10.1371/journal.pntd.0012010 | (silva2024efficacyandsafety pages 18-21, silva2024efficacyandsafety pages 21-22, silva2024efficacyandsafety pages 22-24) |
| Treatment ranking | **Doxycycline + gentamicin** ranked best by SUCRA (**0.94**), followed by **triple therapy 0.87** and **doxycycline + streptomycin 0.78**; authors suggest **6 weeks doxycycline + 1–2 weeks gentamicin** or **2–3 weeks streptomycin** | 43 RCTs, 4,283 patients | Systematic review and network meta-analysis | Huang 2024 *PLOS Neglected Tropical Diseases* | 2024 Aug | https://doi.org/10.1371/journal.pntd.0012405 | (huang2024updatedtherapeuticoptions pages 1-2) |
| Bacteremic disease treatment | Oral **doxycycline–rifampicin** and IV **gentamicin–doxycycline–rifampicin** showed similar response; negative blood culture at 4 weeks **90.3%**, overall recovery **93.5%**, no deaths | 93 adults with brucellosis bacteremia | Observational comparative study | Nazir 2024 *Journal of University Medical & Dental College* | 2024 Aug | https://doi.org/10.37723/jumdc.v15i3.920 | (nazir2024responseofthe pages 1-2) |


*Table: This table compiles recent quantitative evidence on brucellosis burden, epidemiology, diagnostics, and treatment efficacy. It is designed as a compact reference for knowledge-base population and citation tracing.*

---

## 1. Disease information

### 1.1 What is brucellosis?
Brucellosis is a **zoonotic**, often **insidious**, **multisystem** infectious disease caused by bacteria of the genus *Brucella*. Contemporary clinical reviews emphasize its protean manifestations and diagnostic difficulty because presentations overlap with other febrile illnesses (Ayoubi et al., **Jul 2024**, *Current Opinion in Infectious Diseases*, https://doi.org/10.1097/QCO.0000000000001045) (ayoubi2024themanyfaces pages 1-2).

### 1.2 Common synonyms / alternative names
A 2024 clinical review explicitly lists: **“Mediterranean flaccid fever,” “Malta fever,” and “undulant fever.”** (Ayoubi et al., **Jul 2024**, https://doi.org/10.1097/QCO.0000000000001045) (ayoubi2024themanyfaces pages 1-2).

### 1.3 Key identifiers (OMIM / Orphanet / ICD / MeSH / MONDO)
- **ICD-10 / ICD-11 / MeSH / MONDO / Orphanet:** Not extractable with citable evidence from the retrieved corpus in this run. This report therefore does **not** assert specific codes without evidence.
- **Evidence note:** The retrieved peer‑reviewed sources focus on epidemiology, diagnostics, treatment, and One Health and do not provide standardized ontology IDs in the extracted text (ayoubi2024themanyfaces pages 1-2, qureshi2023brucellosisepidemiologypathogenesis pages 1-2).

### 1.4 Evidence source type
The information synthesized here is derived from **aggregated disease-level resources** (systematic reviews/meta-analyses, national surveillance analyses, and modeling studies) and some observational clinical studies, rather than patient‑level EHR-only sources (freire2024diagnosisofhuman pages 9-11, weinberger2024nationalepidemiologyof pages 1-2, laine2023globalestimateof pages 1-2).

---

## 2. Etiology

### 2.1 Disease causal factors
- **Cause:** Infection by *Brucella* spp. (Gram-negative, facultative intracellular bacteria) (huang2024updatedtherapeuticoptions pages 1-2, ayoubi2024themanyfaces pages 1-2).
- **Human-pathogenic species emphasized in recent reviews:** *B. melitensis, B. canis, B. abortus,* and *B. suis* (ayoubi2024themanyfaces pages 1-2, moriyon2023brucellosisandone pages 1-2).

### 2.2 Transmission and risk factors (human)
A 2024 review provides a broad, explicit list of transmission routes:
- “**direct contact with infected animal body fluids**,”
- “**consumption of unpasteurized dairy products and contaminated meats**,”
- “**inhalation of infected aerosol particles**,”
- “**sexual contact, breast milk, vertical transmission, bone marrow transplantation, and transfusion of blood products**” (Ayoubi et al., **Jul 2024**, https://doi.org/10.1097/QCO.0000000000001045) (ayoubi2024themanyfaces pages 1-2).

**Occupational and foodborne risk** are strongly emphasized by One Health sources: the general public is mainly affected by “**consuming raw milk and unpasteurized dairy products**,” whereas at-risk groups include “**breeders and their families, veterinarians, laboratory personnel and dairy and slaughterhouse workers**” (Moriyón et al., **Aug 2023**, *Microorganisms*, https://doi.org/10.3390/microorganisms11082070) (moriyon2023brucellosisandone pages 1-2).

**Risk groups in global incidence modeling:** “raw milk–product consumers, livestock owners, abattoir workers, and veterinarians” (Laine et al., **Sep 2023**, https://doi.org/10.3201/eid2909.230052) (laine2023globalestimateof pages 1-2).

### 2.3 Protective factors
Direct evidence for protective genetic variants or protective environmental factors was not present in the citable excerpts retrieved. However, prevention evidence strongly implies **pasteurization** and **animal control measures** reduce risk (moriyon2023brucellosisandone pages 1-2, qureshi2023brucellosisepidemiologypathogenesis pages 1-2).

### 2.4 Gene–environment interactions
No citable human GxE association results were retrieved in the current corpus; therefore, no specific GxE claims are made.

---

## 3. Phenotypes (clinical manifestations)

### 3.1 Core symptom complex and focal disease
Across recent evidence, typical illness is described as nonspecific and influenza-like:
- “**undulating fever, sweats, fatigue, and malaise**” (Laine et al., **Sep 2023**) (laine2023globalestimateof pages 1-2).
A 2024 global prevalence review also lists common manifestations (fever/fatigue/joint pain) and notes complications including endocarditis and arthritis (sherasiya2024globalprevalenceof pages 1-4).

A 2024 clinical review highlights the multi-system nature and the breadth of complications, emphasizing the need for a comprehensive diagnostic approach (ayoubi2024themanyfaces pages 1-2).

### 3.2 Temporal development / course
Evidence on untreated, asymptomatic seropositive individuals (useful for temporal course and secondary prevention) shows a meaningful risk of developing symptoms:
- Pooled prevalence of “**appearing symptomatic was 15.4%** (95% CI 2.1%–34.3%)” over “**0.5–18 months**,” and risk increases with follow-up duration (Li et al., **Mar 2023**, *Emerging Microbes & Infections*, https://doi.org/10.1080/22221751.2023.2185464) (li2023followupoutcomesof pages 1-2).

### 3.3 Quality-of-life impact
Direct validated QoL instrument statistics (e.g., SF‑36/EQ‑5D) were not present in the retrieved excerpts. Nevertheless, contemporary therapeutic reviews emphasize brucellosis’ “debilitating and disabling potential” and socioeconomic impact (Silva et al., **Mar 2024**) (silva2024efficacyandsafety pages 18-21).

### 3.4 HPO term suggestions (mapping)
These are **ontology mapping suggestions** based on the clinical descriptions in the cited sources:
- Fever: **HP:0001945** (from “undulating fever”) (laine2023globalestimateof pages 1-2)
- Hyperhidrosis / sweats: **HP:0000975** (laine2023globalestimateof pages 1-2)
- Fatigue: **HP:0012378** (laine2023globalestimateof pages 1-2)
- Malaise: **HP:0033834** (laine2023globalestimateof pages 1-2)
- Arthralgia: **HP:0002829** (implied by joint pain/arthritis) (sherasiya2024globalprevalenceof pages 1-4)
- Arthritis: **HP:0001369** (sherasiya2024globalprevalenceof pages 1-4)
- Endocarditis: **HP:0100584** (sherasiya2024globalprevalenceof pages 1-4)
- Meningitis/encephalitis (neurobrucellosis complications referenced): **HP:0001287 / HP:0002383** (sherasiya2024globalprevalenceof pages 1-4)

---

## 4. Genetic / molecular information
Brucellosis is an infectious disease (no single human causal gene). Molecular information is therefore focused on **pathogen virulence** and **host-response pathways**.

### 4.1 Key mechanistic concepts (current understanding)
- *Brucella* spp. are **intracellular pathogens** that survive in host cells (including macrophages), enabling persistence and chronicity (huang2024updatedtherapeuticoptions pages 1-2, ayoubi2024themanyfaces pages 1-2).
- **Host immune evasion and antigen presentation modulation:** A 2024 mechanistic study reports that *Brucella abortus* RNA reduces **IFN-γ–induced MHC-I surface expression** in multiple human cell types (bronchial/alveolar epithelium and endothelial microvasculature), and that in monocytes/macrophages this down-modulation occurs “**via the pathway of the Epidermal Growth Factor Receptor (EGFR)**,” with partial reversal by EGFR neutralization (Serafino et al., **Jul 2024**, *PLOS ONE*, https://doi.org/10.1371/journal.pone.0306429) (racasanu2024epidemiologydiagnosistreatment pages 4-5).
- **Macrophage signaling reprogramming:** A 2024 macrophage transcriptomics study reports strain-specific responses in THP-1 macrophages, including over-expression of “**anti-inflammatory pathways, such as cAMP signaling and PI3K-Akt pathway**” with down-regulation of inflammatory pathways involving IL1A and IL10 (Queijeiro‑Barroso et al., **Nov 2024**, https://doi.org/10.14715/cmb/2024.70.10.2) (qureshi2023brucellosisepidemiologypathogenesis pages 1-2).

### 4.2 Pathway/ontology suggestions (mapping)
**GO biological process (suggested):**
- Antigen processing and presentation via MHC class I: **GO:0002474** (racasanu2024epidemiologydiagnosistreatment pages 4-5)
- Negative regulation of antigen presentation: (conceptual mapping to MHC-I down-modulation) (racasanu2024epidemiologydiagnosistreatment pages 4-5)
- Regulation of cytokine production / inflammatory response: **GO:0006954** (racasanu2024epidemiologydiagnosistreatment pages 4-5, qureshi2023brucellosisepidemiologypathogenesis pages 1-2)

**Cell Ontology (CL) suggestions:**
- Macrophage: **CL:0000235** (intracellular niche; THP‑1 model) (qureshi2023brucellosisepidemiologypathogenesis pages 1-2)
- Monocyte: **CL:0000576** (racasanu2024epidemiologydiagnosistreatment pages 4-5)
- Endothelial cell: **CL:0000115** (racasanu2024epidemiologydiagnosistreatment pages 4-5)
- Epithelial cell (bronchial/alveolar): **CL:0000066** (racasanu2024epidemiologydiagnosistreatment pages 4-5)

**UBERON anatomy suggestions (based on implicated tissues):**
- Spleen (common systemic organ involvement and pathogen reservoir concept in literature; also a major immune organ): **UBERON:0002106** (supported indirectly by systemic infection framing and bacteremia) (laine2023globalestimateof pages 1-2, weinberger2024nationalepidemiologyof pages 1-2)
- Lung / respiratory epithelium: **UBERON:0002048** (racasanu2024epidemiologydiagnosistreatment pages 4-5)
- Blood (bacteremia): **UBERON:0000178** (weinberger2024nationalepidemiologyof pages 1-2)

---

## 5. Environmental information

### 5.1 Environmental/occupational factors
Risk is strongly tied to livestock production systems and occupational exposure. A national analysis in Israel describes community-level risk in sectors with small ruminant herding and unpasteurized dairy distribution, and demonstrates strong demographic disparities in incidence by ethnic sector (Weinberger et al., **May 2024**, https://doi.org/10.1017/S0950268824000803) (weinberger2024nationalepidemiologyof pages 1-2, weinberger2024nationalepidemiologyof pages 2-3).

### 5.2 Lifestyle factors
Consumption of **unpasteurized milk and dairy products** is repeatedly identified as a dominant lifestyle-related exposure risk (moriyon2023brucellosisandone pages 1-2, ayoubi2024themanyfaces pages 1-2).

### 5.3 Infectious agent(s)
- **Pathogen genus:** *Brucella* spp. (ayoubi2024themanyfaces pages 1-2).

---

## 6. Mechanism / pathophysiology (causal chain)

### 6.1 Causal chain (high-level)
1) **Exposure** via raw dairy, animal secretions/tissues, aerosols, or rarely vertical routes (ayoubi2024themanyfaces pages 1-2, moriyon2023brucellosisandone pages 1-2).
2) **Entry and dissemination** with frequent bloodstream involvement in culture-confirmed national data (Israel: 99.8% bacteraemic isolates) (weinberger2024nationalepidemiologyof pages 2-3).
3) **Intracellular survival** in immune cells (macrophages/monocytes) with host signaling shifts toward anti-inflammatory profiles (cAMP, PI3K-Akt) in some strain contexts (qureshi2023brucellosisepidemiologypathogenesis pages 1-2).
4) **Immune evasion** including reduced MHC-I surface expression in multiple cell types, potentially reducing CD8+ T cell surveillance; EGFR pathway implicated in this modulation (racasanu2024epidemiologydiagnosistreatment pages 4-5).
5) **Clinical manifestations** as systemic inflammatory illness (fever/sweats/fatigue) and potential focal complications (arthritis/endocarditis/neuroinfection) (laine2023globalestimateof pages 1-2, sherasiya2024globalprevalenceof pages 1-4).

### 6.2 Recent developments (2023–2024)
- Expansion of diagnostic technologies and algorithms (TR-FRET/FPA/artificial antigens) highlighted as active areas in 2024 expert review (ayoubi2024themanyfaces pages 1-2).
- Mechanistic work in 2024 demonstrates immune evasion beyond macrophages (epithelium/endothelium) (racasanu2024epidemiologydiagnosistreatment pages 4-5).

---

## 7. Anatomical structures affected
Based on clinical syndrome and mechanistic evidence, key involved systems include:
- **Blood / systemic circulation**: frequent bacteremia in culture-confirmed series (weinberger2024nationalepidemiologyof pages 1-2).
- **Musculoskeletal system**: joint pain/arthritis common in clinical descriptions (sherasiya2024globalprevalenceof pages 1-4).
- **Cardiovascular system**: endocarditis as a recognized severe complication (sherasiya2024globalprevalenceof pages 1-4).
- **Nervous system**: meningitis/encephalitis described as possible complications (sherasiya2024globalprevalenceof pages 1-4).
- **Respiratory epithelium and microvascular endothelium**: implicated in immune evasion study (racasanu2024epidemiologydiagnosistreatment pages 4-5).

Suggested UBERON mappings (see Section 4.2).

---

## 8. Temporal development
- **Onset:** Often insidious/nonspecific (laine2023globalestimateof pages 1-2).
- **Course patterns:** Can be acute or evolve with focal complications; relapse/failure is a key clinical concern driving multi-week combination therapy and comparative-effectiveness research (silva2024efficacyandsafety pages 18-21, maduranga2024asystematicreview pages 3-6).
- **Asymptomatic seropositivity:** Meta-analysis indicates nontrivial progression to symptomatic disease over months, rising with longer follow-up (li2023followupoutcomesof pages 1-2).

---

## 9. Inheritance and population
Not applicable as a Mendelian inherited disorder. Population characteristics are therefore epidemiologic.

### 9.1 Epidemiology: global and regional statistics
- **Global incidence estimate (model-based):** “**2.1 million**” cases/year (Laine et al., **Sep 2023**) (laine2023globalestimateof pages 1-2).
- **Global prevalence synthesis (study-based):** pooled prevalence **15.49%** (95% CI 12.01–18.97) across 69 studies (Sherasiya, **Sep 2024**, preprint) (sherasiya2024globalprevalenceof pages 1-4).
- **Israel (2004–2022):** 2,489 culture-confirmed cases; 64% male; mean age 30.5 years; incidence 1.6/100,000 overall, with major disparities (Arab 6.6/100,000; Jewish 0.18/100,000; IRR 36.4) (Weinberger et al., **May 2024**) (weinberger2024nationalepidemiologyof pages 1-2).
- **Ethiopia (2015–2024):** pooled seroprevalence overall 5.0%; human 6.9%; cattle 3.5% (Dagnaw et al., **Dec 2024**, https://doi.org/10.1186/s12889-024-21042-2) (dagnaw2024humanandanimal pages 1-2).

---

## 10. Diagnostics

### 10.1 Clinical and laboratory diagnosis: current evidence and performance
Freire et al. (2024) conducted a diagnostic test accuracy systematic review/meta-analysis and report high pooled performance for several tests (very low certainty overall):
- **Rose Bengal** vs culture: sensitivity **89.7%**, specificity **94.1%**; vs culture and/or SAT: sensitivity **96.6%**, specificity **97.9%** (freire2024diagnosisofhuman pages 9-11).
- **SAT** vs culture: sensitivity **89.2%**, specificity **95.6%** (freire2024diagnosisofhuman pages 9-11).
- **IgG ELISA** vs culture: sensitivity **82.9%**, specificity **96.2%** (freire2024diagnosisofhuman pages 9-11).
- **PCR:** qualitative PCR vs culture sensitivity **96.4%**, specificity **98.1%**; real-time PCR sensitivity **81.9%**, specificity **91.5%** (freire2024diagnosisofhuman pages 9-11).

### 10.2 Real-world diagnostic algorithms (implementation)
A French National Reference Center study (sera June 2012–June 2023) shows a practical algorithmic approach can deliver very high diagnostic performance:
- Algorithm combining **RBT + Brucellacapt + ELISA (IgM/IgG)** achieved **90.5% sensitivity**, **99.7% specificity**, **92.4% PPV**, **99.6% NPV** (Loubet et al., **Sep 2024**, https://doi.org/10.1371/journal.pntd.0012442) (loubet2024diagnosisofbrucellosis pages 1-2).

### 10.3 Expert analysis (interpretation challenges)
A 2024 expert review highlights advances (FPA, TR‑FRET, artificial antigens) but notes serology interpretation remains challenging (e.g., immunosuppression, blocking antibodies, prozone) and stresses a comprehensive diagnostic approach (ayoubi2024themanyfaces pages 1-2).

### 10.4 Differential diagnosis
Not systematically enumerated in the retrieved excerpts; however, the core problem of nonspecific febrile illness and the need for combined clinical + laboratory evaluation is emphasized (laine2023globalestimateof pages 1-2, ayoubi2024themanyfaces pages 1-2).

---

## 11. Outcome / prognosis

### 11.1 Mortality and severe outcomes
- Bacteremic cohort study (n=93) reported “**No death**” during the observed period; negative blood culture at 4 weeks 90.3%, recovery 93.5% (Nazir et al., **Aug 2024**, https://doi.org/10.37723/jumdc.v15i3.920) (nazir2024responseofthe pages 1-2). This is context-specific and not a global mortality estimate.

### 11.2 Relapse and treatment failure (key prognostic concern)
Relapse/failure drives guideline emphasis on combination therapy and adequate duration.
- Doxycycline+rifampicin vs doxycycline+streptomycin: higher failure risk with doxycycline+rifampicin (RR **1.96**, 95% CI 1.27–3.01) (Silva et al., **Mar 2024**) (silva2024efficacyandsafety pages 18-21).

### 11.3 Progression from asymptomatic infection
Untreated asymptomatic cases can become symptomatic over months (pooled 15.4%), with increasing rates at longer follow-up (li2023followupoutcomesof pages 1-2).

---

## 12. Treatment

### 12.1 Current applications and real-world implementations
Combination antibiotic therapy over weeks is standard, reflecting intracellular persistence and relapse risk. WHO guidance is referenced in recent observational work as recommending “doxycycline with rifampicin or an aminoglycoside” (Nazir et al., 2024) (nazir2024responseofthe pages 1-2).

### 12.2 Comparative effectiveness (2024 evidence)
**Meta-analysis of comparative clinical studies (Maduranga et al., Aug 2024):**
- Doxycycline+rifampicin had higher **treatment failure** risk than triple therapy adding streptomycin (RR **1.98**, 95% CI 1.17–3.35) and adding levofloxacin (RR **2.98**, 95% CI 1.67–5.32) (maduranga2024asystematicreview pages 1-2).
- Doxycycline+rifampicin had markedly higher **relapse** risk vs triple therapy adding streptomycin (RR **22.12**, 95% CI 3.48–140.52) and levofloxacin (RR **4.61**, 95% CI 2.20–9.66) (maduranga2024asystematicreview pages 3-6).

**Network meta-analysis (Silva et al., Mar 2024):**
- Doxycycline+rifampicin had higher failure risk than doxycycline+streptomycin (RR **1.96**, 95% CI 1.27–3.01) (silva2024efficacyandsafety pages 18-21).
- Doxycycline+gentamicin lower risk than doxycycline+rifampicin (RR **0.30**, 95% CI 0.14–0.62) (silva2024efficacyandsafety pages 18-21).

**Network meta-analysis (Huang et al., Aug 2024):**
- Ranking by SUCRA suggested **doxycycline + gentamicin** as best (0.94), then triple therapy (0.87), then doxycycline + streptomycin (0.78), and the authors state: “**6 weeks of doxycycline plus 1 to 2 weeks of gentamicin or plus 2 to 3 weeks of streptomycin is the best therapy**” (Huang et al., Aug 2024, https://doi.org/10.1371/journal.pntd.0012405) (huang2024updatedtherapeuticoptions pages 1-2).

### 12.3 Emerging/experimental strategies (expert opinion)
A 2024 expert review describes “**evolving treatment regimens such as the use of hydroxychloroquine as part of triple therapy**” and nano-delivery systems as approaches to reduce relapse and manage chronic cases (Ayoubi et al., **Jul 2024**) (ayoubi2024themanyfaces pages 1-2).

### 12.4 MAXO term suggestions (mapping)
- Antibiotic therapy: **MAXO:0001026** (anti-bacterial drug therapy)
- Combination antibiotic therapy: (combination therapy concept)
- Serologic testing / diagnostic assay: (diagnostic procedure concept)

(Note: MAXO identifiers are provided as mapping suggestions; specific IDs beyond general action terms were not present in the retrieved corpus.)

---

## 13. Prevention

### 13.1 Primary prevention
One Health sources emphasize that prevention must target animal reservoirs and food safety.
- “**The general public is mainly affected by consuming raw milk and unpasteurized dairy products**” (Moriyón et al., **Aug 2023**) (moriyon2023brucellosisandone pages 1-2).
- One Health implementation requires coordinated actors and correct use of “diagnostic, epidemiological and prophylactic tools” (moriyon2023brucellosisandone pages 1-2).

### 13.2 Secondary prevention
- Active screening and follow-up for seropositive individuals may be important in some contexts given progression risk (li2023followupoutcomesof pages 1-2).

### 13.3 Tertiary prevention
- Preventing relapse and focal complications relies on using effective combination regimens and adequate duration, supported by 2024 comparative evidence (maduranga2024asystematicreview pages 3-6, silva2024efficacyandsafety pages 18-21, huang2024updatedtherapeuticoptions pages 1-2).

---

## 14. Other species / natural disease
Brucellosis is fundamentally a multi-host zoonosis.
- Reservoir breadth: beyond classic domestic hosts, brucellae infect “**ruminants, swine, and dogs**,” and additional hosts include “camelids, seal and cetacean species… amphibians, foxes… desert rodent species, cave-dwelling bats and other wild animals” (Moriyón et al., **Aug 2023**) (moriyon2023brucellosisandone pages 1-2).

---

## 15. Model organisms
Direct, detailed model-organism phenotyping and limitations were not present in the citable excerpts used here. However, the retrieved 2024 mechanistic evidence demonstrates common experimental systems in active use:
- **Human macrophage-like cell models (THP‑1)** for transcriptomics and pathway analysis (qureshi2023brucellosisepidemiologypathogenesis pages 1-2).
- **Human epithelial and endothelial cell lines** to study immune evasion mechanisms (racasanu2024epidemiologydiagnosistreatment pages 4-5).

---

## Notes on evidence limits and missing items
1) **Ontology identifiers (MONDO/MeSH/ICD/Orphanet)** are not included because no citable extracted text in the current corpus provided them; they should be added from authoritative ontology resources in a follow-on curation step.
2) Several mechanistic claims are necessarily **high-level** given the excerpt-limited access; where pathway/cell-type/GO/CL/UBERON mappings are suggested, they are presented as **mappings** rather than asserted as experimentally proven beyond the cited text.
3) Some sources retrieved are preprints (e.g., Sherasiya 2024); quantitative results from such sources should be interpreted with appropriate caution.

---

## Key quoted abstract statements (verbatim excerpts)
- Global incidence: “**An evidence-based conservative estimate of the annual global incidence is 2.1 million**” (Laine et al., **Sep 2023**) (laine2023globalestimateof pages 1-2).
- Diagnostic algorithm performance: algorithm combining RBT, Brucellacapt, ELISA (IgM/IgG) achieved “**90.5% for sensitivity, 99.7% for specificity**” (Loubet et al., **Sep 2024**) (loubet2024diagnosisofbrucellosis pages 1-2).
- Asymptomatic progression: pooled prevalence of “**appearing symptomatic was 15.4%**” (Li et al., **Mar 2023**) (li2023followupoutcomesof pages 1-2).
- Treatment ranking statement: “**6 weeks of doxycycline plus 1 to 2 weeks of gentamicin or plus 2 to 3 weeks of streptomycin is the best therapy**” (Huang et al., **Aug 2024**) (huang2024updatedtherapeuticoptions pages 1-2).


References

1. (ayoubi2024themanyfaces pages 1-2): L’Emir Wassim El Ayoubi, Caren Challita, and Souha S. Kanj. The many faces of brucellosis: diagnostic and management approach. Current Opinion in Infectious Diseases, 37:474-484, Jul 2024. URL: https://doi.org/10.1097/qco.0000000000001045, doi:10.1097/qco.0000000000001045. This article has 10 citations and is from a peer-reviewed journal.

2. (laine2023globalestimateof pages 1-2): Christopher G. Laine, Valen E. Johnson, H. Morgan Scott, and Angela M. Arenas-Gamboa. Global estimate of human brucellosis incidence. Emerging Infectious Diseases, 29:1789-1797, Sep 2023. URL: https://doi.org/10.3201/eid2909.230052, doi:10.3201/eid2909.230052. This article has 360 citations and is from a domain leading peer-reviewed journal.

3. (moriyon2023brucellosisandone pages 1-2): Ignacio Moriyón, José María Blasco, Jean Jacques Letesson, Fabrizio De Massis, and Edgardo Moreno. Brucellosis and one health: inherited and future challenges. Microorganisms, 11:2070, Aug 2023. URL: https://doi.org/10.3390/microorganisms11082070, doi:10.3390/microorganisms11082070. This article has 79 citations.

4. (huy2024exploringtheimpact pages 1-2): Tran Xuan Ngoc Huy. Exploring the impact of brucellosis on maternal and child health: transmission mechanisms, patient effects, and current trends in drug use and resistance: a scoping review. Beni-Suef University Journal of Basic and Applied Sciences, Oct 2024. URL: https://doi.org/10.1186/s43088-024-00569-8, doi:10.1186/s43088-024-00569-8. This article has 5 citations.

5. (freire2024diagnosisofhuman pages 9-11): Mariana Lourenço Freire, Tália Santana Machado de Assis, Sarah Nascimento Silva, and Gláucia Cota. Diagnosis of human brucellosis: systematic review and meta-analysis. PLOS Neglected Tropical Diseases, 18:e0012030, Mar 2024. URL: https://doi.org/10.1371/journal.pntd.0012030, doi:10.1371/journal.pntd.0012030. This article has 53 citations and is from a domain leading peer-reviewed journal.

6. (loubet2024diagnosisofbrucellosis pages 1-2): Paul Loubet, Chloé Magnan, Florian Salipante, Théo Pastre, Anne Keriel, David O’Callaghan, Albert Sotto, and Jean-Philippe Lavigne. Diagnosis of brucellosis: combining tests to improve performance. PLOS Neglected Tropical Diseases, 18:e0012442, Sep 2024. URL: https://doi.org/10.1371/journal.pntd.0012442, doi:10.1371/journal.pntd.0012442. This article has 27 citations and is from a domain leading peer-reviewed journal.

7. (silva2024efficacyandsafety pages 18-21): Sarah Nascimento Silva, Gláucia Cota, Diego Mendes Xavier, Glaciele Maria de Souza, Marina Rocha Fonseca Souza, Moisés Willian Aparecido Gonçalves, Felipe Francisco Tuon, and Endi Lanza Galvão. Efficacy and safety of therapeutic strategies for human brucellosis: a systematic review and network meta-analysis. PLOS Neglected Tropical Diseases, 18:e0012010, Mar 2024. URL: https://doi.org/10.1371/journal.pntd.0012010, doi:10.1371/journal.pntd.0012010. This article has 14 citations and is from a domain leading peer-reviewed journal.

8. (huang2024updatedtherapeuticoptions pages 1-2): Shanjun Huang, Jiaying Xu, Hao Wang, Zhuo Li, Ruifang Song, Yiting Zhang, Menghan Lu, Xin Han, Tian Ma, Yingtong Wang, Jiaxin Hao, Shanshan Song, Qing Zhen, and Tiejun Shui. Updated therapeutic options for human brucellosis: a systematic review and network meta-analysis of randomized controlled trials. PLOS Neglected Tropical Diseases, 18:e0012405, Aug 2024. URL: https://doi.org/10.1371/journal.pntd.0012405, doi:10.1371/journal.pntd.0012405. This article has 22 citations and is from a domain leading peer-reviewed journal.

9. (maduranga2024asystematicreview pages 3-6): Sachith Maduranga, Braulio Mark Valencia, Xiaoying Li, Samaneh Moallemi, and Chaturaka Rodrigo. A systematic review and meta-analysis of comparative clinical studies on antibiotic treatment of brucellosis. Scientific Reports, Aug 2024. URL: https://doi.org/10.1038/s41598-024-69669-w, doi:10.1038/s41598-024-69669-w. This article has 22 citations and is from a peer-reviewed journal.

10. (sherasiya2024globalprevalenceof pages 1-4): Riyaz Sherasiya. Global prevalence of human brucellosis: a systematic review and meta-analysis. Sep 2024. URL: https://doi.org/10.21203/rs.3.rs-4929733/v1, doi:10.21203/rs.3.rs-4929733/v1.

11. (sherasiya2024globalprevalenceof pages 7-10): Riyaz Sherasiya. Global prevalence of human brucellosis: a systematic review and meta-analysis. Sep 2024. URL: https://doi.org/10.21203/rs.3.rs-4929733/v1, doi:10.21203/rs.3.rs-4929733/v1.

12. (weinberger2024nationalepidemiologyof pages 2-3): Miriam Weinberger, Jacob Moran-Gilad, Michal Perry Markovich, and Svetlana Bardenstein. National epidemiology of culture-confirmed brucellosis in israel, 2004–2022. Epidemiology and Infection, May 2024. URL: https://doi.org/10.1017/s0950268824000803, doi:10.1017/s0950268824000803. This article has 5 citations and is from a peer-reviewed journal.

13. (weinberger2024nationalepidemiologyof pages 1-2): Miriam Weinberger, Jacob Moran-Gilad, Michal Perry Markovich, and Svetlana Bardenstein. National epidemiology of culture-confirmed brucellosis in israel, 2004–2022. Epidemiology and Infection, May 2024. URL: https://doi.org/10.1017/s0950268824000803, doi:10.1017/s0950268824000803. This article has 5 citations and is from a peer-reviewed journal.

14. (dagnaw2024humanandanimal pages 1-2): Gashaw Getaneh Dagnaw, Yordanos Mamuye, and Haileyesus Dejene. Human and animal brucellosis and risk factors for human infection in ethiopia: a systematic review and meta-analysis (2015–2024). BMC Public Health, Dec 2024. URL: https://doi.org/10.1186/s12889-024-21042-2, doi:10.1186/s12889-024-21042-2. This article has 13 citations and is from a peer-reviewed journal.

15. (freire2024diagnosisofhuman pages 1-2): Mariana Lourenço Freire, Tália Santana Machado de Assis, Sarah Nascimento Silva, and Gláucia Cota. Diagnosis of human brucellosis: systematic review and meta-analysis. PLOS Neglected Tropical Diseases, 18:e0012030, Mar 2024. URL: https://doi.org/10.1371/journal.pntd.0012030, doi:10.1371/journal.pntd.0012030. This article has 53 citations and is from a domain leading peer-reviewed journal.

16. (maduranga2024asystematicreview pages 1-2): Sachith Maduranga, Braulio Mark Valencia, Xiaoying Li, Samaneh Moallemi, and Chaturaka Rodrigo. A systematic review and meta-analysis of comparative clinical studies on antibiotic treatment of brucellosis. Scientific Reports, Aug 2024. URL: https://doi.org/10.1038/s41598-024-69669-w, doi:10.1038/s41598-024-69669-w. This article has 22 citations and is from a peer-reviewed journal.

17. (silva2024efficacyandsafety pages 21-22): Sarah Nascimento Silva, Gláucia Cota, Diego Mendes Xavier, Glaciele Maria de Souza, Marina Rocha Fonseca Souza, Moisés Willian Aparecido Gonçalves, Felipe Francisco Tuon, and Endi Lanza Galvão. Efficacy and safety of therapeutic strategies for human brucellosis: a systematic review and network meta-analysis. PLOS Neglected Tropical Diseases, 18:e0012010, Mar 2024. URL: https://doi.org/10.1371/journal.pntd.0012010, doi:10.1371/journal.pntd.0012010. This article has 14 citations and is from a domain leading peer-reviewed journal.

18. (silva2024efficacyandsafety pages 22-24): Sarah Nascimento Silva, Gláucia Cota, Diego Mendes Xavier, Glaciele Maria de Souza, Marina Rocha Fonseca Souza, Moisés Willian Aparecido Gonçalves, Felipe Francisco Tuon, and Endi Lanza Galvão. Efficacy and safety of therapeutic strategies for human brucellosis: a systematic review and network meta-analysis. PLOS Neglected Tropical Diseases, 18:e0012010, Mar 2024. URL: https://doi.org/10.1371/journal.pntd.0012010, doi:10.1371/journal.pntd.0012010. This article has 14 citations and is from a domain leading peer-reviewed journal.

19. (nazir2024responseofthe pages 1-2): Dr. Imran Nazir, Mohammed A Al-Matrafi, Fozya Bashir Bashal, Dr. Ahmed Farouk Aboelazm, and Dr. Waleed Amasaib Mohammed Ahmed. Response of the intravenous versus oral antibiotic regimen in brucellosis bacteremia. Journal of University Medical &amp; Dental College, Aug 2024. URL: https://doi.org/10.37723/jumdc.v15i3.920, doi:10.37723/jumdc.v15i3.920. This article has 0 citations.

20. (qureshi2023brucellosisepidemiologypathogenesis pages 1-2): Kamal A. Qureshi, Adil Parvez, Nada A. Fahmy, Bassant H. Abdel Hady, Shweta Kumar, Anusmita Ganguly, Akhtar Atiya, Gamal O. Elhassan, Saeed O. Alfadly, Seppo Parkkila, and Ashok Aspatwar. Brucellosis: epidemiology, pathogenesis, diagnosis and treatment–a comprehensive review. Annals of Medicine, Dec 2023. URL: https://doi.org/10.1080/07853890.2023.2295398, doi:10.1080/07853890.2023.2295398. This article has 359 citations and is from a domain leading peer-reviewed journal.

21. (li2023followupoutcomesof pages 1-2): Fande Li, Lanping Du, Hua Zhen, Mujinyan Li, Shuqi An, Wenqi Fan, Yuke Yan, Meifang Zhao, Xin Han, Zhuo Li, Huixin Yang, Cui Zhang, Chao Guo, and Qing Zhen. Follow-up outcomes of asymptomatic brucellosis: a systematic review and meta-analysis. Emerging Microbes &amp; Infections, Mar 2023. URL: https://doi.org/10.1080/22221751.2023.2185464, doi:10.1080/22221751.2023.2185464. This article has 26 citations and is from a domain leading peer-reviewed journal.

22. (racasanu2024epidemiologydiagnosistreatment pages 4-5): I RĂCĂȘANU and DN ENEA. Epidemiology, diagnosis, treatment, control and economic impact of brucellosis. Unknown journal, 2024.