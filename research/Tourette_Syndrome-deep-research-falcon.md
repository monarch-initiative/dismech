---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-24T17:00:53.803036'
end_time: '2026-04-24T17:16:47.024834'
duration_seconds: 953.22
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Tourette Syndrome
  mondo_id: ''
  category: Psychiatric
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 56
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Tourette Syndrome
- **MONDO ID:**  (if available)
- **Category:** Psychiatric

## Research Objectives

Please provide a comprehensive research report on **Tourette Syndrome** covering all of the
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
- **Disease Name:** Tourette Syndrome
- **MONDO ID:**  (if available)
- **Category:** Psychiatric

## Research Objectives

Please provide a comprehensive research report on **Tourette Syndrome** covering all of the
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


## Tourette Syndrome (TS) — Disease Characteristics Research Report

### 0. Executive summary
Tourette syndrome (TS; also “Gilles de la Tourette syndrome”) is a childhood-onset neurodevelopmental disorder defined by multiple motor tics plus at least one vocal/phonic tic, persisting for >1 year, with onset before age 18 and not attributable to substances or another medical condition. (abbasi2023prevalenceofdepression pages 1-2, jiang2024biomarkersandtourette pages 1-2)

In recent U.S. nationally representative survey data (NSCH 2016–2022), parent/guardian-reported clinician-diagnosed TS prevalence in ages 0–17 was 0.23% overall (0.35% in boys vs 0.11% in girls), with no significant prevalence change from 2016 to 2022. (xiong2024prevalenceoftourette pages 1-2)

---

## 1. Disease information

### 1.1 Disease overview (current understanding)
**Core definition (DSM-5 framing, as summarized in recent peer-reviewed literature):** multiple motor tics and one or more vocal tics, with onset before 18 years, tics persisting for >1 year, and symptoms not explained by substances or another neurological condition. (abbasi2023prevalenceofdepression pages 1-2)

**Key concept—tic:** tics are described in guidelines and systematic reviews as “sudden, rapid, recurrent, non-rhythmic motor movements or vocalisations/vocalizations.” (szejko2022europeanclinicalguidelines pages 1-2, amico2024efficacyofnonpharmacological pages 1-2)

**Evidence source type:** these definitions and broad disease characterizations are drawn from aggregated disease-level resources (clinical guidelines and systematic reviews/meta-analyses), not individual EHRs. (szejko2022europeanclinicalguidelines pages 6-8, abbasi2023prevalenceofdepression pages 1-2)

### 1.2 Synonyms / alternative names
- Tourette syndrome (TS) (xiong2024prevalenceoftourette pages 1-2)
- Gilles de la Tourette syndrome (GTS) (fichna2024structuralvariantsand pages 1-2)

### 1.3 Key identifiers (ontology / coding)
The retrieved evidence corpus explicitly notes alignment with DSM-5 and ICD-11 criteria in the European Society for the Study of Tourette Syndrome (ESSTS) guidelines update, but **does not include the exact ICD-10/ICD-11 codes, MeSH ID, OMIM ID(s), Orphanet ID, or MONDO ID** in the accessible text snippets. (mullervahl2022europeanclinicalguidelines pages 3-4)

**Actionable note for knowledge-base curation:** obtain these identifiers from authoritative terminologies (ICD-10/11 browser, MeSH, MONDO, OMIM, Orphanet). The ESSTS summary confirms DSM-5/ICD-11 harmonization but does not provide code strings in the retrieved passages. (mullervahl2022europeanclinicalguidelines pages 3-4)

---

## 2. Etiology

### 2.1 Causal factors (genetic, environmental, mechanistic)
TS is strongly familial and genetically influenced, but exhibits **complex architecture** spanning polygenic common-variant effects and rare/structural variants. (yilmaz2025epidemiologyoftourette pages 1-4, fichna2024structuralvariantsand pages 1-2)

- **Heritability:** an epidemiology review reports genome-wide study heritability estimates of 0.77–0.92 and monozygotic twin concordance of 64.3%. (yilmaz2025epidemiologyoftourette pages 1-4)
- **Polygenic architecture:** a large GWAS meta-analysis summarized in the evidence indicates SNP heritability ~13.8% and gene-level associations including BCL11B, NDFIP2, RBM26. (strom2025geneticriskof pages 73-75)
- **Rare/structural variants:** a 2024 familial whole-genome sequencing study found 70 putative pathogenic structural variants (SVs), including exonic deletions in LDLRAD4, B2M, USH2A, ZNF765 and recurrent insertions in GOLM1 and DISC1 that co-segregated in multiple families. (fichna2024structuralvariantsand pages 1-2)

**Direct abstract-quote support:** the 2024 familial SV study states: “Seventy putative pathogenic variants… were identified,” and highlights “uncommon insertions in GOLM1 and DISC1” and enriched processes including synaptic vesicle endocytosis and neurite outgrowth signaling. (fichna2024structuralvariantsand pages 1-2)

### 2.2 Risk factors

#### Genetic risk factors
- **Family clustering / heritability:** high heritability supports genetic susceptibility as a major risk factor. (yilmaz2025epidemiologyoftourette pages 1-4)
- **SV/CNV gene candidates and pathways:** SVs affecting genes such as NRXN3, DISC1, CACNA2D3, USH2A and immune-related B2M are implicated in familial TS, with enrichment in synaptic and neurite-related processes. (fichna2024structuralvariantsand pages 4-5)

#### Environmental / psychosocial risk factors
The ESSTS assessment guideline emphasizes differential diagnosis and clinical context but does not provide a quantitative catalog of environmental exposures causing TS. However, it highlights that functional tic-like movements may be associated with traumatic events and show poor response to anti-tic medication—important for diagnostic risk stratification and avoiding misattribution. (szejko2022europeanclinicalguidelines pages 6-8)

### 2.3 Protective factors
No specific genetic or environmental protective factors were identifiable in the retrieved evidence snippets.

### 2.4 Gene–environment interaction
A monozygotic twin design study (tic spectrum disorder, encompassing TS and chronic tic disorder) was explicitly motivated by “key uncertainties concerning the role of environmental influences,” and identified environmentally influenced transcriptional signals (e.g., RNY1 associated with tic severity), though with limited sample size and no multiple-testing significant methylation probes. (dalsberg2026transcriptomeandepigenomewide pages 1-2)

---

## 3. Phenotypes

### 3.1 Core phenotypes and HPO mapping (suggested)
**Core tic phenotypes (symptoms/signs):**
- Motor tics (HPO suggestion: *Motor tic*; commonly HP:0002459) (supported conceptually by TS definition) (abbasi2023prevalenceofdepression pages 1-2)
- Vocal/phonic tics (HPO suggestion: *Vocal tic*; commonly HP:0030220) (abbasi2023prevalenceofdepression pages 1-2)
- Premonitory urges (HPO suggestion: *Premonitory urge*; no specific HPO term confirmed in evidence; clinically captured by PUTS) (szejko2022europeanclinicalguidelines pages 11-12)

**Common neuropsychiatric comorbidities (behavioral/psychiatric phenotypes):**
- ADHD (HPO suggestion: *Attention deficit hyperactivity disorder*) (yilmaz2025epidemiologyoftourette pages 9-11)
- OCD/obsessive–compulsive symptoms (HPO suggestion: *Obsessive-compulsive behavior*) (yilmaz2025epidemiologyoftourette pages 9-11)
- Anxiety (HPO suggestion: *Anxiety*) (abbasi2023prevalenceofdepression pages 1-2)
- Depression (HPO suggestion: *Depressive episode*) (abbasi2023prevalenceofdepression pages 1-2)

### 3.2 Phenotype characteristics (onset, severity, course, frequency)
- **Typical onset:** tics usually begin around ages 4–6 (or ~5–6 in ESSTS assessment). (yilmaz2025epidemiologyoftourette pages 8-9, szejko2022europeanclinicalguidelines pages 1-2)
- **Peak severity:** typically around 8–12 years (often 10–12). (yilmaz2025epidemiologyoftourette pages 8-9, yilmaz2025epidemiologyoftourette pages 1-4)
- **Course:** waxing/waning; many improve in adolescence/young adulthood; ~one-third may be tic-free by adulthood, while 50–80% may have at least mild tics after age 16. (yilmaz2025epidemiologyoftourette pages 8-9)

### 3.3 Quality-of-life impact
A U.S. population study notes TS is associated with functional impairments “across physical, psychological, academic, family, and social domains” and increased bullying involvement. (xiong2024prevalenceoftourette pages 1-2)

### 3.4 Psychiatric comorbidity burden (statistics)
An epidemiology review reports ~85% with ≥1 psychiatric comorbidity and 57% with ≥2. (yilmaz2025epidemiologyoftourette pages 8-9)

A 2023 systematic review/meta-analysis estimated pooled prevalence of **depression 36.4%** and **anxiety 53.5%** in TS, increasing with mean age. (abbasi2023prevalenceofdepression pages 1-2)

---

## 4. Genetic / molecular information

### 4.1 Causal genes and pathogenic variants
TS is typically **not monogenic**. The familial SV study notes that “only single variants in HDC and SLITRK1 are currently classified as pathogenic by HPO,” emphasizing heterogeneity. (fichna2024structuralvariantsand pages 1-2)

### 4.2 Structural variants and implicated genes (2024 study)
In 17 multiplex families (80 patients), WGS-based SV analysis identified:
- Exonic deletions in **LDLRAD4, B2M, USH2A, ZNF765** (fichna2024structuralvariantsand pages 1-2)
- Recurrent insertions co-segregating in **GOLM1** and **DISC1** (fichna2024structuralvariantsand pages 1-2)
- Additional SV/SNV overlap genes highlighted include **NRXN3, CACNA2D3, PSD3, ZNF407, EYS** (fichna2024structuralvariantsand pages 4-5)

### 4.3 Polygenic risk and implicated loci (recent large-scale genetics)
A GWAS meta-analysis summary reports:
- SNP heritability ~13.8%
- Gene-level significant signals: **BCL11B, NDFIP2, RBM26**
- Enrichment in cortico-striato-thalamo-cortical (CSTC) circuit regions and neuronal cell types including medium spiny neurons. (strom2025geneticriskof pages 73-75)

### 4.4 Pathway/process annotations (GO/Reactome/KEGG suggestions)
Based on SV enrichment and GWAS enrichment summaries:
- GO biological process suggestions: **synaptic vesicle endocytosis**, **neurite outgrowth**, **neuronal migration**, **regulation of neurotransmission**, **dendritic spine organization** (fichna2024structuralvariantsand pages 4-5, fichna2024structuralvariantsand pages 1-2)
- KEGG/pathway suggestions: CSTC circuit functional modules (not a single KEGG pathway), and (from twin study enrichment) **ribosome**, **nucleocytoplasmic transport**, **nicotine addiction** (as an enriched KEGG set in peripheral blood transcriptome) (dalsberg2026transcriptomeandepigenomewide pages 1-2)

---

## 5. Environmental information
The retrieved sources did not provide a definitive exposure-based environmental etiology for primary TS. The ESSTS assessment guideline provides practical clinical differentiation from functional tic-like disorders (which may be triggered by psychosocial stressors/trauma and show atypical features), which is relevant to avoiding misclassification. (szejko2022europeanclinicalguidelines pages 6-8)

---

## 6. Mechanism / pathophysiology

### 6.1 Circuit-level mechanisms (current consensus)
Recent epidemiology and treatment sources converge on CSTC circuit dysfunction and dopaminergic involvement:
- A systematic review/meta-analysis on cannabis-based medicine states TS “is associated with structural and functional alterations in corticostriatal circuits and neurochemical imbalances.” (serag2024efficacyofcannabisbased pages 4-5)
- A behavioral-treatment systematic review likewise notes dysfunction of the “cortico–striatal–thalamus–cortical circuit” and dopaminergic/serotonergic dysregulation. (amico2024efficacyofnonpharmacological pages 1-2)

### 6.2 Neuroimmune and peripheral biomarker findings (2024)
A 2024 biomarker meta-analysis identified significant differences in several peripheral markers between TS and controls (e.g., T cell subsets, anti-streptolysin O antibodies, amino acids, ferritin/iron, zinc, lead, vitamin D, BDNF), while noting there is currently **no biological gold-standard test** for TS. (jiang2024biomarkersandtourette pages 1-2)

### 6.3 Proposed causal chain (integrated, evidence-aligned)
1) Genetic susceptibility (polygenic and rare/SV) impacts synaptic/neurodevelopmental processes and CSTC circuit development and function. (strom2025geneticriskof pages 73-75, fichna2024structuralvariantsand pages 4-5)
2) Circuit-level dysregulation (particularly dopaminergic modulation in CSTC pathways) alters motor control gating and tic suppression mechanisms. (amico2024efficacyofnonpharmacological pages 1-2, serag2024efficacyofcannabisbased pages 4-5)
3) Clinical manifestation: childhood-onset motor and vocal tics with waxing/waning course, commonly accompanied by ADHD/OCD/anxiety/depression that amplifies impairment and QoL impact. (yilmaz2025epidemiologyoftourette pages 8-9, abbasi2023prevalenceofdepression pages 1-2)

### 6.4 Cell types and CL term suggestions
- Medium spiny neurons (striatum) (CL suggestion: *striatal medium spiny neuron*) (strom2025geneticriskof pages 73-75)
- Cortical excitatory neurons / inhibitory interneurons (CL suggestions: *glutamatergic neuron*, *GABAergic interneuron*) (strom2025geneticriskof pages 73-75)

---

## 7. Anatomical structures affected
Primary involvement is within the central nervous system, particularly CSTC circuit nodes:
- Striatum (caudate, putamen, nucleus accumbens) and frontal cortical regions are implicated by post-GWAS enrichment. (strom2025geneticriskof pages 73-75)

**UBERON suggestions:**
- Striatum (UBERON:0002435), caudate nucleus (UBERON:0001876), putamen (UBERON:0001875), nucleus accumbens (UBERON:0001882), prefrontal cortex (UBERON:0001873) — suggested for annotation; exact IDs should be verified in Uberon.

---

## 8. Temporal development
- Onset: typically early childhood (~4–6 years). (yilmaz2025epidemiologyoftourette pages 8-9)
- Peak: late childhood/pre-adolescence (~8–12 years). (yilmaz2025epidemiologyoftourette pages 8-9)
- Progression: waxing/waning; many improve in late adolescence/early adulthood; persistence is common but often milder. (yilmaz2025epidemiologyoftourette pages 8-9)

---

## 9. Inheritance and population

### 9.1 Epidemiology (recent and quantitative)
| Domain | Metric | Quantitative finding | Population / notes | Evidence (citation id) | Source URL + year |
|---|---|---|---|---|---|
| Epidemiology | US diagnosed prevalence, ages 0–17 | **0.23%** overall | National Survey of Children’s Health (NSCH), parent/guardian-reported clinician diagnosis, United States, 2016–2022 | (xiong2024prevalenceoftourette pages 1-2) | https://doi.org/10.1186/s12889-024-20216-2 (2024) |
| Epidemiology | US prevalence by age | **<0.01%** (0–2 y); **0.05%** (3–5 y); **0.28%** (6–11 y); **0.38%** (12–17 y) | Weighted prevalence in NSCH 2016–2022 | (xiong2024prevalenceoftourette pages 1-2) | https://doi.org/10.1186/s12889-024-20216-2 (2024) |
| Epidemiology | US prevalence by sex | **0.35% boys** vs **0.11% girls** | NSCH 2016–2022 | (xiong2024prevalenceoftourette pages 1-2) | https://doi.org/10.1186/s12889-024-20216-2 (2024) |
| Epidemiology | US trend over time | **No significant change** from 2016 to 2022 | NSCH trend analysis | (xiong2024prevalenceoftourette pages 1-2) | https://doi.org/10.1186/s12889-024-20216-2 (2024) |
| Epidemiology | Global / literature prevalence in children & adolescents | About **0.3–0.77%** in meta-analytic estimates; broader study range **0.05%–1.1%** | Across population studies; estimates vary by ascertainment and methodology | (yilmaz2025epidemiologyoftourette pages 1-4) | https://doi.org/10.3390/brainsci15050426 (2025) |
| Epidemiology | Global prevalence in children/adolescents | Approximately **0.7%** | Review of biomarker literature cites global prevalence in children/adolescents | (jiang2024biomarkersandtourette pages 1-2) | https://doi.org/10.3389/fneur.2024.1262057 (2024) |
| Epidemiology | Adult prevalence | About **0.01%–0.011%** | Much lower than in childhood/adolescence | (yilmaz2025epidemiologyoftourette pages 1-4) | https://doi.org/10.3390/brainsci15050426 (2025) |
| Epidemiology | Male:female ratio | About **4:1** overall in childhood; reported study range **1.58:1 to 9.0:1**; falls to about **2.33:1** in adulthood | Sex difference is robust but magnitude varies across studies | (yilmaz2025epidemiologyoftourette pages 8-9, yilmaz2025epidemiologyoftourette pages 1-4) | https://doi.org/10.3390/brainsci15050426 (2025) |
| Comorbidity | Any psychiatric comorbidity | About **85%** have **≥1** psychiatric comorbidity; **57%** have **≥2** | Family/clinical cohorts summarized in epidemiology review | (yilmaz2025epidemiologyoftourette pages 8-9) | https://doi.org/10.3390/brainsci15050426 (2025) |
| Comorbidity | ADHD | About **50%** | Commonest neurodevelopmental comorbidity in TS | (yilmaz2025epidemiologyoftourette pages 9-11) | https://doi.org/10.3390/brainsci15050426 (2025) |
| Comorbidity | OCD | Reported prevalence **7%–50%** | Frequent and often disabling; about **10%** have both ADHD and OCD | (yilmaz2025epidemiologyoftourette pages 9-11) | https://doi.org/10.3390/brainsci15050426 (2025) |
| Comorbidity | Anxiety | Pooled prevalence **53.5%** (95% CI 39.9–66.6%) | Systematic review/meta-analysis, 12 studies, n=3812 | (abbasi2023prevalenceofdepression pages 1-2) | https://doi.org/10.1186/s13052-023-01562-0 (2023) |
| Comorbidity | Depression | Pooled prevalence **36.4%** (95% CI 21.1–54.9%) | Systematic review/meta-analysis, 12 studies, n=3812 | (abbasi2023prevalenceofdepression pages 1-2) | https://doi.org/10.1186/s13052-023-01562-0 (2023) |
| Natural history | Typical age at onset | Usually **4–6 years**; assessment guideline notes around **5–6 years** | Childhood-onset disorder | (yilmaz2025epidemiologyoftourette pages 8-9, szejko2022europeanclinicalguidelines pages 1-2) | https://doi.org/10.3390/brainsci15050426 (2025); https://doi.org/10.1007/s00787-021-01842-2 (2022) |
| Natural history | Age of peak severity | Around **8–12 years**; commonly **10–12 years** or “just before puberty” | Tic severity generally worsens into late childhood/pre-adolescence | (yilmaz2025epidemiologyoftourette pages 8-9, yilmaz2025epidemiologyoftourette pages 1-4) | https://doi.org/10.3390/brainsci15050426 (2025) |
| Natural history | Improvement by adulthood | About **three-quarters** improve in older teens/young adulthood | Many continue to have residual symptoms despite improvement | (xiong2024prevalenceoftourette pages 1-2, yilmaz2025epidemiologyoftourette pages 8-9) | https://doi.org/10.1186/s12889-024-20216-2 (2024); https://doi.org/10.3390/brainsci15050426 (2025) |
| Natural history | Tic-free by adulthood | Roughly **one-third** may be tic-free by adulthood | Review-based estimate | (yilmaz2025epidemiologyoftourette pages 8-9) | https://doi.org/10.3390/brainsci15050426 (2025) |
| Natural history | Persistent symptoms into adulthood | About **50–80%** of those >16 years have at least mild tics; another source notes roughly **three-quarters** still have tic symptoms into early adulthood | Persistence is common even when severity declines | (yilmaz2025epidemiologyoftourette pages 8-9, xiong2024prevalenceoftourette pages 1-2) | https://doi.org/10.3390/brainsci15050426 (2025); https://doi.org/10.1186/s12889-024-20216-2 (2024) |
| Natural history | Course pattern | **Waxing and waning / fluctuating** | Typical course rather than steadily progressive disease | (abbasi2023prevalenceofdepression pages 1-2, szejko2022europeanclinicalguidelines pages 1-2) | https://doi.org/10.1186/s13052-023-01562-0 (2023); https://doi.org/10.1007/s00787-021-01842-2 (2022) |


*Table: This table condenses recent quantitative data on Tourette syndrome prevalence, sex differences, psychiatric comorbidity burden, and typical clinical course. It is useful as a quick reference for population-level characteristics and disease trajectory when building a disease knowledge base entry.*

Key recent statistic (U.S.): prevalence 0.23% in ages 0–17 from 2016–2022 NSCH; stable over time; higher in boys than girls. (xiong2024prevalenceoftourette pages 1-2)

### 9.2 Sex ratio
Literature syntheses report a male:female ratio around ~4:1 in childhood, decreasing into adulthood. (yilmaz2025epidemiologyoftourette pages 8-9, yilmaz2025epidemiologyoftourette pages 1-4)

---

## 10. Diagnostics

### 10.1 Clinical criteria and assessment approach
Diagnosis is clinical, supported by careful phenomenology and comorbidity assessment. ESSTS assessment guidance states that routine neuroimaging/EEG “do not add value in establishing the diagnosis of a tic disorder” and should be performed only if clinically indicated. (szejko2022europeanclinicalguidelines pages 6-8)

### 10.2 Rating scales (ESSTS 2022)
Recommended tools include:
- **Yale Global Tic Severity Scale (YGTSS)** (gold standard; recommended) (szejko2022europeanclinicalguidelines pages 11-12)
- **Premonitory Urge for Tics Scale (PUTS)** (recommended) (szejko2022europeanclinicalguidelines pages 11-12)
- QoL measures: **GTS-QOL** and **C&A-GTS-QOL** (recommended) (szejko2022europeanclinicalguidelines pages 11-12)
- OCD severity: **Y-BOCS / CY-BOCS / CY-BOCS-II** (recommended) (szejko2022europeanclinicalguidelines pages 11-12)
- ADHD scales used by experts: SNAP, CAARS, CBRS, WURS (szejko2022europeanclinicalguidelines pages 11-12)

### 10.3 Differential diagnosis (including functional tic-like behaviors)
ESSTS guidance distinguishes primary tics from:
- **Stereotypies:** earlier onset (0–3 years), quasi-rhythmic, not typically associated with premonitory urge. (szejko2022europeanclinicalguidelines pages 6-8)
- **Functional tic-like movements/vocalizations:** atypical features include absent premonitory urges, inability to suppress, adult onset, female preponderance, and poor response to anti-tic medication; functional vocalisations may include speech blocking and association with traumatic events. (szejko2022europeanclinicalguidelines pages 6-8)

---

## 11. Outcome / prognosis
Most individuals improve in adolescence/young adulthood, but persistence of at least mild symptoms is common. (yilmaz2025epidemiologyoftourette pages 8-9)

Comorbid psychiatric disorders are common and materially influence disability and quality of life (e.g., pooled anxiety ~53.5% and depression ~36.4% in a 2023 meta-analysis). (abbasi2023prevalenceofdepression pages 1-2)

---

## 12. Treatment

### 12.1 Guideline-based treatment algorithm (ESSTS)
The ESSTS v2.0 summary provides an updated decision-tree algorithm for shared decision-making in TS treatment. (mullervahl2022europeanclinicalguidelines media b45307e9)

### 12.2 Evidence-based interventions and real-world implementation
| Intervention | Mechanism / class | Typical use-case / indication | Key efficacy statistics | Key safety / monitoring issues | Best supporting citation + URL/year |
|---|---|---|---|---|---|
| CBIT / HRT / ERP (behavior therapy) | Behavioral therapy; HRT/CBIT strengthen tic awareness and competing responses; ERP targets suppression while tolerating premonitory urges | First-line when psychoeducation alone is insufficient; recommended for children and adults with Tourette syndrome or chronic tic disorder | ESSTS: HRT/CBIT and ERP are recommended first-line psychological interventions; pediatric RCT/systematic-review evidence shows CBIT reduced YGTSS total tic score by **7.6 points vs 3.5** in controls; group CBIT produced **32% motor-tic reduction** maintained at 3 months; HRT improved motor tics but less consistent effect on vocal tics (amico2024efficacyofnonpharmacological pages 3-5, amico2024efficacyofnonpharmacological pages 5-6, amico2024efficacyofnonpharmacological pages 6-8, mullervahl2022europeanclinicalguidelines pages 1-3) | Requires trained therapists; access can be limited; dropout can reduce effectiveness in practice; monitor adherence, family support, and comorbid ADHD/OCD/anxiety that may affect engagement (amico2024efficacyofnonpharmacological pages 3-5, amico2024efficacyofnonpharmacological pages 6-8) | ESSTS psychological guideline: https://doi.org/10.1007/s00787-021-01845-z (2022); pediatric review: https://doi.org/10.3390/app14209466 (2024) |
| Telehealth / internet-delivered ERP or CBIT | Remote therapist-supported behavioral therapy via videoconference or internet platform | Useful when access to trained therapists or travel is a barrier; increasingly implemented in youth | Telehealth CBIT decreased YGTSS by **7.8 points** vs **6.5** face-to-face; CBIT-VoIP showed **7.25-point** fall vs **1.75** in controls; meta-analysis of therapist-supported remote therapy found pooled **YGTSS-TTSS MD -2.22** (95% CI -3.16 to -1.29), and versus online psychoeducation **MD -2.37** (95% CI -3.64 to -1.10) with similar efficacy to face-to-face care (amico2024efficacyofnonpharmacological pages 6-8, xu2025efficacyoftherapistsupported pages 5-6) | Improves access and continuity; requires caregiver cooperation, internet/device access, and therapist support; durability appears favorable but long-term follow-up remains important (xu2025efficacyoftherapistsupported pages 5-6, amico2024efficacyofnonpharmacological pages 3-5) | Telehealth meta-analysis: https://doi.org/10.3389/fpsyt.2025.1521947 (2025); pediatric review: https://doi.org/10.3390/app14209466 (2024) |
| Aripiprazole | Dopamine receptor blocking/modulating antipsychotic (partial D2 agonist) | Preferred first-line medication when behavioral therapy is ineffective, unavailable, or insufficient; commonly used in children and adults | ESSTS 2022: among medications, the **largest amount of evidence** supports dopamine-blocking agents, **preferably aripiprazole** because of a more favorable adverse-event profile; average expected tic reduction with medication is about **50%** overall, though individual response varies (roessner2022europeanclinicalguidelines pages 1-2, roessner2022europeanclinicalguidelines pages 8-9, mullervahl2022europeanclinicalguidelines pages 3-4) | Start low, go slow; monitor weight/metabolic effects, sedation, extrapyramidal symptoms, prolactin-related effects, cardiovascular/ECG issues; taper gradually to avoid withdrawal dyskinesia (roessner2022europeanclinicalguidelines pages 8-9) | ESSTS pharmacologic guideline: https://doi.org/10.1007/s00787-021-01899-z (2022) |
| Tiapride | Dopamine receptor antagonist (benzamide antipsychotic) | Medication option with established evidence, often used in Europe for tic reduction | ESSTS identifies **tiapride** among antipsychotics with best-established evidence/clinical experience; part of the medication group where average tic reduction is approximately **50%** (roessner2022europeanclinicalguidelines pages 8-9, roessner2022europeanclinicalguidelines pages 1-2) | Off-label in many settings; monitor EPS, sedation, cardiovascular effects, and general antipsychotic adverse effects; use lower doses than in psychosis and titrate slowly (roessner2022europeanclinicalguidelines pages 8-9) | ESSTS pharmacologic guideline: https://doi.org/10.1007/s00787-021-01899-z (2022) |
| Risperidone | Second-generation antipsychotic; dopamine/serotonin receptor antagonist | Evidence-based pharmacologic option for tic reduction; also considered when OCD symptoms coexist | ESSTS lists **risperidone** among recommended antipsychotics with substantial evidence; average medication-related tic reduction is around **50%** overall (roessner2022europeanclinicalguidelines pages 8-9, roessner2022europeanclinicalguidelines pages 1-2) | Higher concern for **weight gain/metabolic effects**, prolactin elevation, sedation, movement disorders, ECG/cardiovascular effects; taper gradually (roessner2022europeanclinicalguidelines pages 8-9) | ESSTS pharmacologic guideline: https://doi.org/10.1007/s00787-021-01899-z (2022) |
| Clonidine | Alpha-2 adrenergic agonist / noradrenergic agent | Especially useful for **mild-to-moderate tics with co-existing ADHD**; often favored in pediatric practice | ESSTS/AAN review gives moderate confidence for tic benefit vs placebo; recommended first-line pharmacologic option when ADHD co-occurs rather than for severe tics alone (roessner2022europeanclinicalguidelines pages 1-2, roessner2022europeanclinicalguidelines pages 8-9) | Monitor blood pressure, pulse, sedation, dizziness; taper carefully to avoid rebound hypertension; benefit for tics alone is limited compared with antipsychotics (roessner2022europeanclinicalguidelines pages 8-9) | ESSTS pharmacologic guideline: https://doi.org/10.1007/s00787-021-01899-z (2022) |
| Guanfacine | Alpha-2 adrenergic agonist | Similar role to clonidine, mainly when **ADHD coexists** and tics are mild-to-moderate | ESSTS highlights guanfacine for TS with ADHD, but evidence is weaker than for antipsychotics; useful as part of individualized treatment plans (roessner2022europeanclinicalguidelines pages 1-2, roessner2022europeanclinicalguidelines pages 8-9) | Monitor blood pressure, pulse, sedation/fatigue; overall evidence for tic reduction is less robust than for antipsychotics (roessner2022europeanclinicalguidelines pages 1-2, roessner2022europeanclinicalguidelines pages 8-9) | ESSTS pharmacologic guideline: https://doi.org/10.1007/s00787-021-01899-z (2022) |
| Botulinum toxin injections | Peripheral chemodenervation of overactive muscles / focal anti-tic intervention | Focal, bothersome, treatment-resistant motor or vocal tics | ESSTS lists botulinum toxin as an option with moderate confidence from AAN-reviewed evidence; typically used selectively for focal symptoms rather than generalized tic burden (roessner2022europeanclinicalguidelines pages 1-2, monfrini2025frompharmacologicaltreatment pages 1-2) | Local weakness, site-specific adverse effects, need for repeat injections; best for carefully selected focal tics (monfrini2025frompharmacologicaltreatment pages 1-2, roessner2022europeanclinicalguidelines pages 1-2) | ESSTS pharmacologic guideline: https://doi.org/10.1007/s00787-021-01899-z (2022) |
| Cannabis-based medicines (e.g., THC-containing formulations, nabiximols) | Cannabinoid-system modulation | Considered in selected, treatment-resistant cases; evidence remains limited and sample sizes are small | Meta-analysis: YGTSS tic severity **MD -13.88** (95% CI -23.07 to -4.68; P=0.003); YGTSS impairment **MD -18.71** (95% CI -28.21 to -9.21; P<0.001); PUTS **MD -5.36** (95% CI -8.46 to -2.27; P=0.0007); Y-BOCS change not significant (**MD -6.22**, P=0.06) (serag2024efficacyofcannabisbased pages 4-5) | Limited evidence base, small trials, heterogeneity; monitor cognitive/psychiatric adverse effects, sedation, and legal/regulatory issues; not a routine first-line therapy (serag2024efficacyofcannabisbased pages 4-5, monfrini2025frompharmacologicaltreatment pages 1-2) | Cannabis meta-analysis: https://doi.org/10.1007/s00228-024-03710-9 (2024) |
| Deep brain stimulation (DBS) | Neuromodulation of tic-related circuits; experimental/off-label surgical therapy for refractory disease | Reserved for **carefully selected, severely affected, treatment-resistant** patients after failure of behavioral and pharmacologic approaches | 102-case multicenter cohort: YGTSS total improved **45.2% at 6 months**, **51.6% at 12 months**, **55.5% at 24 months**, **55.6% at 36 months**, **57.8% at 48 months**, **61.4% at ≥60 months**; children had greater ≥60-month improvement (**70.1% vs 55.9%** adults) and faster time to 60% improvement (**6 vs 12 months**); QoL and OCD/depression scores also improved (monfrini2025frompharmacologicaltreatment pages 12-14, mullervahl2022europeanclinicalguidelines media b45307e9) | ESSTS considers DBS experimental; requires multidisciplinary expert center, careful patient selection, programming follow-up, and monitoring for device/procedure-related complications and psychiatric effects (monfrini2025frompharmacologicaltreatment pages 12-14, mullervahl2022europeanclinicalguidelines pages 3-4) | Cohort study: https://doi.org/10.1186/s12916-024-03432-w (2024); ESSTS DBS guideline: https://doi.org/10.1007/s00787-021-01881-9 (2022) |
| Emerging D1/VMAT2 strategies: ecopipam, valbenazine, deutetrabenazine | Ecopipam: selective D1 antagonist; valbenazine/deutetrabenazine: VMAT2 inhibitors | Investigational / emerging options for Tourette syndrome; not established first-line care | Ecopipam has completed pediatric Phase 2b and Phase 3 programs, including randomized-withdrawal design in ages **≥6 years** (NCT04007991; NCT05615220) (NCT04007991 chunk 1, NCT05615220 chunk 1). Valbenazine pediatric rollover was **terminated** after main study failed its primary endpoint, with no safety signal noted (NCT03732534 chunk 1). Deutetrabenazine pediatric RCT program completed but ESSTS summary notes deutetrabenazine **failed primary endpoints** in newer trials (mullervahl2022europeanclinicalguidelines pages 3-4, NCT02674321 chunk 1, NCT03452943 chunk 3) | Monitor agent-specific psychiatric, sleep/sedation, and movement-disorder adverse effects; these remain investigational or unsupported for routine use in Tourette syndrome at present (mullervahl2022europeanclinicalguidelines pages 3-4, NCT03732534 chunk 1, NCT02674321 chunk 1) | ClinicalTrials.gov: NCT04007991 (2019), NCT05615220 (2023), NCT03732534 (2018), NCT02674321 (2014) |


*Table: This table summarizes the main evidence-based Tourette syndrome treatments across behavioral, pharmacologic, cannabinoid, DBS, and emerging investigational approaches. It highlights practical use-cases, quantitative outcomes, and key monitoring issues with supporting context IDs and source URLs.*

Key points:
- **First-line:** psychoeducation and behavioral therapy (HRT/CBIT; ERP also recommended). (mullervahl2022europeanclinicalguidelines pages 1-3)
- **Medication when needed:** ESSTS emphasizes dopamine-blocking agents (aripiprazole favored for adverse-event profile), plus alpha-2 agonists for coexisting ADHD. (roessner2022europeanclinicalguidelines pages 1-2)
- **Telehealth:** videoconference/internet-delivered interventions show clinically meaningful reductions in tic severity and can improve access. (xu2025efficacyoftherapistsupported pages 5-6, amico2024efficacyofnonpharmacological pages 6-8)
- **DBS:** reserved for carefully selected, refractory cases; long-term multicenter outcomes show sustained YGTSS improvement over years. (monfrini2025frompharmacologicaltreatment pages 12-14)

### 12.3 Emerging therapies and clinical trials (ClinicalTrials.gov)
Selected trials identified in the retrieved corpus:
- **Ecopipam (D1 antagonist)**
  - Phase 2b pediatric RCT (NCT04007991; start 2019-06-28; completed 2021-09-23; ages ≥6 to <18; n=153; primary endpoint YGTSS-TTS change at Week 12). (NCT04007991 chunk 1)
  - Phase 3 randomized-withdrawal design (NCT05615220; start 2023-01-31; completed 2025-02-04; ages ≥6; n=216; primary endpoint time-to-relapse based on YGTSS criteria). (NCT05615220 chunk 1)
- **Valbenazine (VMAT2 inhibitor; NBI-98854)**
  - Open-label Phase 2 safety/tolerability study (NCT02879578; started 2016-07-25; completed 2017-11-01; n=155; pediatric/adolescent/adult dosing strata; primary outcome TEAEs). (NCT02879578 chunk 1)
  - Pediatric rollover open-label Phase 2 (NCT03732534; ages 6–18; n=6; terminated after main study failed primary endpoint; “no safety concerns identified”). (NCT03732534 chunk 1)
- **Deutetrabenazine (VMAT2 inhibitor; SD-809)**
  - Pilot Phase 1 open-label (NCT02674321; adolescents 12–18; n=23; completed; primary outcome safety/AEs; secondary outcomes include YGTSS changes). (NCT02674321 chunk 1)

**MAXO suggestions (treatment action ontology; verify IDs):**
- Behavioral therapy / habit reversal training / exposure and response prevention (CBIT/HRT/ERP) (amico2024efficacyofnonpharmacological pages 3-5)
- Antipsychotic therapy (aripiprazole/tiapride/risperidone) (roessner2022europeanclinicalguidelines pages 1-2)
- Alpha-2 agonist therapy (clonidine/guanfacine) (roessner2022europeanclinicalguidelines pages 1-2)
- Botulinum toxin injection (roessner2022europeanclinicalguidelines pages 1-2)
- Deep brain stimulation (monfrini2025frompharmacologicaltreatment pages 12-14)

---

## 13. Prevention
No established primary prevention strategies were identified in the retrieved sources. Secondary/tertiary prevention focuses on early recognition, differential diagnosis (including functional tic-like presentations), and early access to behavioral therapy to reduce impairment. (szejko2022europeanclinicalguidelines pages 6-8, mullervahl2022europeanclinicalguidelines pages 1-3)

---

## 14. Other species / natural disease
No naturally occurring TS-equivalent disease in non-human species was identified in the retrieved evidence corpus.

---

## 15. Model organisms
The retrieved evidence contains limited direct model-organism characterization. A treatment review references histidine decarboxylase (HDC) gene relevance and an HDC knockout mouse model in the context of TS pathogenesis discussion. (jiao2024progressinthe pages 1-3)

---

## Additional expert synthesis / interpretation (authoritative sources)
- The ESSTS guideline update highlights a field-wide shift toward non-pharmacological interventions and shared decision-making, reflecting both evidence accumulation and patient-centered care priorities. (mullervahl2022europeanclinicalguidelines pages 1-3, mullervahl2022europeanclinicalguidelines media b45307e9)
- The epidemiology review emphasizes that prevalence estimates vary widely due to ascertainment and diagnostic practices, implying that knowledge-base prevalence fields should record data provenance (survey-based vs clinician-assessed cohorts). (yilmaz2025epidemiologyoftourette pages 1-4, xiong2024prevalenceoftourette pages 1-2)

---

## Key references (URLs in-line; publication year)
- Xiong et al. *BMC Public Health* (2024-10): NSCH prevalence 2016–2022. https://doi.org/10.1186/s12889-024-20216-2 (xiong2024prevalenceoftourette pages 1-2)
- Jiang et al. *Frontiers in Neurology* (2024-02): biomarker meta-analysis; no gold-standard test. https://doi.org/10.3389/fneur.2024.1262057 (jiang2024biomarkersandtourette pages 1-2)
- Fichna et al. *Int J Mol Sci* (2024-05): familial WGS structural variants and enriched processes. https://doi.org/10.3390/ijms25115758 (fichna2024structuralvariantsand pages 1-2)
- Abbasi et al. *Italian Journal of Pediatrics* (2023-12): depression/anxiety prevalence meta-analysis. https://doi.org/10.1186/s13052-023-01562-0 (abbasi2023prevalenceofdepression pages 1-2)
- ESSTS guidelines v2.0 (2022): assessment (Part I), psychological (Part II), pharmacology (Part III), DBS (Part IV). https://doi.org/10.1007/s00787-021-01842-2; https://doi.org/10.1007/s00787-021-01845-z; https://doi.org/10.1007/s00787-021-01899-z; https://doi.org/10.1007/s00787-021-01881-9 (szejko2022europeanclinicalguidelines pages 11-12, szejko2022europeanclinicalguidelines pages 6-8, roessner2022europeanclinicalguidelines pages 1-2, monfrini2025frompharmacologicaltreatment pages 12-14)


References

1. (abbasi2023prevalenceofdepression pages 1-2): Parvin Abbasi, Sepideh Tanhaie, and Mohsen Kazeminia. Prevalence of depression and anxiety in patients with tourette syndrome; 1997 to 2022: a systematic review and meta-analysis. Italian Journal of Pediatrics, Dec 2023. URL: https://doi.org/10.1186/s13052-023-01562-0, doi:10.1186/s13052-023-01562-0. This article has 20 citations and is from a peer-reviewed journal.

2. (jiang2024biomarkersandtourette pages 1-2): Yanlin Jiang, Yuan Li, Xi Chen, Rui Zhai, Yaqi Peng, Ran Tai, Congxiao Zhou, and Junhong Wang. Biomarkers and tourette syndrome: a systematic review and meta-analysis. Frontiers in Neurology, Feb 2024. URL: https://doi.org/10.3389/fneur.2024.1262057, doi:10.3389/fneur.2024.1262057. This article has 12 citations and is from a peer-reviewed journal.

3. (xiong2024prevalenceoftourette pages 1-2): Yuhong Xiong, Matthew O’Brien, Wenhan Yang, Xiaodong Zang, Wei Bao, and Guifeng Xu. Prevalence of tourette syndrome among children and adolescents in the united states, 2016–2022. BMC Public Health, Oct 2024. URL: https://doi.org/10.1186/s12889-024-20216-2, doi:10.1186/s12889-024-20216-2. This article has 14 citations and is from a peer-reviewed journal.

4. (szejko2022europeanclinicalguidelines pages 1-2): Natalia Szejko, Sally Robinson, Andreas Hartmann, Christos Ganos, Nanette M. Debes, Liselotte Skov, Martina Haas, Renata Rizzo, Jeremy Stern, Alexander Münchau, Virginie Czernecki, Andrea Dietrich, Tara L. Murphy, Davide Martino, Zsanett Tarnok, Tammy Hedderly, Kirsten R. Müller-Vahl, and Danielle C. Cath. European clinical guidelines for tourette syndrome and other tic disorders—version 2.0. part i: assessment. European Child & Adolescent Psychiatry, 31:383-402, Oct 2022. URL: https://doi.org/10.1007/s00787-021-01842-2, doi:10.1007/s00787-021-01842-2. This article has 141 citations and is from a domain leading peer-reviewed journal.

5. (amico2024efficacyofnonpharmacological pages 1-2): Cecilia Amico, Chiara Crepaldi, Margherita Rinaldi, Elisa Buffone, Simona Scaini, Barbara Forresi, and Mauro Leoni. Efficacy of nonpharmacological treatment in children and adolescent with tic disorder: a systematic review. Applied Sciences, 14:9466, Oct 2024. URL: https://doi.org/10.3390/app14209466, doi:10.3390/app14209466. This article has 1 citations.

6. (szejko2022europeanclinicalguidelines pages 6-8): Natalia Szejko, Sally Robinson, Andreas Hartmann, Christos Ganos, Nanette M. Debes, Liselotte Skov, Martina Haas, Renata Rizzo, Jeremy Stern, Alexander Münchau, Virginie Czernecki, Andrea Dietrich, Tara L. Murphy, Davide Martino, Zsanett Tarnok, Tammy Hedderly, Kirsten R. Müller-Vahl, and Danielle C. Cath. European clinical guidelines for tourette syndrome and other tic disorders—version 2.0. part i: assessment. European Child & Adolescent Psychiatry, 31:383-402, Oct 2022. URL: https://doi.org/10.1007/s00787-021-01842-2, doi:10.1007/s00787-021-01842-2. This article has 141 citations and is from a domain leading peer-reviewed journal.

7. (fichna2024structuralvariantsand pages 1-2): Jakub P. Fichna, Mateusz Chiliński, Anup Kumar Halder, Paweł Cięszczyk, Dariusz Plewczynski, Cezary Żekanowski, and Piotr Janik. Structural variants and implicated processes associated with familial tourette syndrome. International Journal of Molecular Sciences, 25:5758, May 2024. URL: https://doi.org/10.3390/ijms25115758, doi:10.3390/ijms25115758. This article has 2 citations.

8. (mullervahl2022europeanclinicalguidelines pages 3-4): Kirsten R. Müller-Vahl, Natalia Szejko, Cara Verdellen, Veit Roessner, Pieter J. Hoekstra, Andreas Hartmann, and Danielle C. Cath. European clinical guidelines for tourette syndrome and other tic disorders: summary statement. European Child & Adolescent Psychiatry, 31:377-382, Jul 2022. URL: https://doi.org/10.1007/s00787-021-01832-4, doi:10.1007/s00787-021-01832-4. This article has 99 citations and is from a domain leading peer-reviewed journal.

9. (yilmaz2025epidemiologyoftourette pages 1-4): Abdullah Yasir Yilmaz and Joseph Jankovic. Epidemiology of tourette syndrome. Brain Sciences, 15:426, Apr 2025. URL: https://doi.org/10.3390/brainsci15050426, doi:10.3390/brainsci15050426. This article has 12 citations.

10. (strom2025geneticriskof pages 73-75): NI Strom. Genetic risk of obsessive-compulsive disorder and related psychiatric phenotypes-insights from large-scale genome-wide association studies. Unknown journal, 2025.

11. (fichna2024structuralvariantsand pages 4-5): Jakub P. Fichna, Mateusz Chiliński, Anup Kumar Halder, Paweł Cięszczyk, Dariusz Plewczynski, Cezary Żekanowski, and Piotr Janik. Structural variants and implicated processes associated with familial tourette syndrome. International Journal of Molecular Sciences, 25:5758, May 2024. URL: https://doi.org/10.3390/ijms25115758, doi:10.3390/ijms25115758. This article has 2 citations.

12. (dalsberg2026transcriptomeandepigenomewide pages 1-2): Jonas Dalsberg, Cathrine Jespersgaard, Amanda M. Levy, Anna Maria Asplund, Frederik Otzen Bagger, Nanette M. Debes, Qihua Tan, Zeynep Tümer, and Mathis Hildonen. Transcriptome- and epigenome-wide association studies of tic spectrum disorder in discordant monozygotic twins. Genes, 17:97, Jan 2026. URL: https://doi.org/10.3390/genes17010097, doi:10.3390/genes17010097. This article has 0 citations.

13. (szejko2022europeanclinicalguidelines pages 11-12): Natalia Szejko, Sally Robinson, Andreas Hartmann, Christos Ganos, Nanette M. Debes, Liselotte Skov, Martina Haas, Renata Rizzo, Jeremy Stern, Alexander Münchau, Virginie Czernecki, Andrea Dietrich, Tara L. Murphy, Davide Martino, Zsanett Tarnok, Tammy Hedderly, Kirsten R. Müller-Vahl, and Danielle C. Cath. European clinical guidelines for tourette syndrome and other tic disorders—version 2.0. part i: assessment. European Child & Adolescent Psychiatry, 31:383-402, Oct 2022. URL: https://doi.org/10.1007/s00787-021-01842-2, doi:10.1007/s00787-021-01842-2. This article has 141 citations and is from a domain leading peer-reviewed journal.

14. (yilmaz2025epidemiologyoftourette pages 9-11): Abdullah Yasir Yilmaz and Joseph Jankovic. Epidemiology of tourette syndrome. Brain Sciences, 15:426, Apr 2025. URL: https://doi.org/10.3390/brainsci15050426, doi:10.3390/brainsci15050426. This article has 12 citations.

15. (yilmaz2025epidemiologyoftourette pages 8-9): Abdullah Yasir Yilmaz and Joseph Jankovic. Epidemiology of tourette syndrome. Brain Sciences, 15:426, Apr 2025. URL: https://doi.org/10.3390/brainsci15050426, doi:10.3390/brainsci15050426. This article has 12 citations.

16. (serag2024efficacyofcannabisbased pages 4-5): Ibrahim Serag, Mona Mahmoud Elsakka, Mostafa Hossam El din Moawad, Hossam Tharwat Ali, Khalid Sarhan, Sally Shayeb, Islam Nadim, and Mohamed Abouzid. Efficacy of cannabis-based medicine in the treatment of tourette syndrome: a systematic review and meta-analysis. European Journal of Clinical Pharmacology, 80:1483-1493, Jul 2024. URL: https://doi.org/10.1007/s00228-024-03710-9, doi:10.1007/s00228-024-03710-9. This article has 10 citations and is from a peer-reviewed journal.

17. (mullervahl2022europeanclinicalguidelines media b45307e9): Kirsten R. Müller-Vahl, Natalia Szejko, Cara Verdellen, Veit Roessner, Pieter J. Hoekstra, Andreas Hartmann, and Danielle C. Cath. European clinical guidelines for tourette syndrome and other tic disorders: summary statement. European Child & Adolescent Psychiatry, 31:377-382, Jul 2022. URL: https://doi.org/10.1007/s00787-021-01832-4, doi:10.1007/s00787-021-01832-4. This article has 99 citations and is from a domain leading peer-reviewed journal.

18. (amico2024efficacyofnonpharmacological pages 3-5): Cecilia Amico, Chiara Crepaldi, Margherita Rinaldi, Elisa Buffone, Simona Scaini, Barbara Forresi, and Mauro Leoni. Efficacy of nonpharmacological treatment in children and adolescent with tic disorder: a systematic review. Applied Sciences, 14:9466, Oct 2024. URL: https://doi.org/10.3390/app14209466, doi:10.3390/app14209466. This article has 1 citations.

19. (amico2024efficacyofnonpharmacological pages 5-6): Cecilia Amico, Chiara Crepaldi, Margherita Rinaldi, Elisa Buffone, Simona Scaini, Barbara Forresi, and Mauro Leoni. Efficacy of nonpharmacological treatment in children and adolescent with tic disorder: a systematic review. Applied Sciences, 14:9466, Oct 2024. URL: https://doi.org/10.3390/app14209466, doi:10.3390/app14209466. This article has 1 citations.

20. (amico2024efficacyofnonpharmacological pages 6-8): Cecilia Amico, Chiara Crepaldi, Margherita Rinaldi, Elisa Buffone, Simona Scaini, Barbara Forresi, and Mauro Leoni. Efficacy of nonpharmacological treatment in children and adolescent with tic disorder: a systematic review. Applied Sciences, 14:9466, Oct 2024. URL: https://doi.org/10.3390/app14209466, doi:10.3390/app14209466. This article has 1 citations.

21. (mullervahl2022europeanclinicalguidelines pages 1-3): Kirsten R. Müller-Vahl, Natalia Szejko, Cara Verdellen, Veit Roessner, Pieter J. Hoekstra, Andreas Hartmann, and Danielle C. Cath. European clinical guidelines for tourette syndrome and other tic disorders: summary statement. European Child & Adolescent Psychiatry, 31:377-382, Jul 2022. URL: https://doi.org/10.1007/s00787-021-01832-4, doi:10.1007/s00787-021-01832-4. This article has 99 citations and is from a domain leading peer-reviewed journal.

22. (xu2025efficacyoftherapistsupported pages 5-6): Xiaolei Xu, Kangsheng Zhu, Weiyi Wang, Tianyu Zhao, and Congrui Fu. Efficacy of therapist-supported online remote behavioral therapy for tic disorders: a systematic review and meta-analysis. Frontiers in Psychiatry, Jun 2025. URL: https://doi.org/10.3389/fpsyt.2025.1521947, doi:10.3389/fpsyt.2025.1521947. This article has 0 citations.

23. (roessner2022europeanclinicalguidelines pages 1-2): Veit Roessner, Heike Eichele, Jeremy S. Stern, Liselotte Skov, Renata Rizzo, Nanette Mol Debes, Péter Nagy, Andrea E. Cavanna, Cristiano Termine, Christos Ganos, Alexander Münchau, Natalia Szejko, Danielle Cath, Kirsten R. Müller-Vahl, Cara Verdellen, Andreas Hartmann, Aribert Rothenberger, Pieter J. Hoekstra, and Kerstin J. Plessen. European clinical guidelines for tourette syndrome and other tic disorders—version 2.0. part iii: pharmacological treatment. European Child & Adolescent Psychiatry, 31:425-441, Nov 2022. URL: https://doi.org/10.1007/s00787-021-01899-z, doi:10.1007/s00787-021-01899-z. This article has 202 citations and is from a domain leading peer-reviewed journal.

24. (roessner2022europeanclinicalguidelines pages 8-9): Veit Roessner, Heike Eichele, Jeremy S. Stern, Liselotte Skov, Renata Rizzo, Nanette Mol Debes, Péter Nagy, Andrea E. Cavanna, Cristiano Termine, Christos Ganos, Alexander Münchau, Natalia Szejko, Danielle Cath, Kirsten R. Müller-Vahl, Cara Verdellen, Andreas Hartmann, Aribert Rothenberger, Pieter J. Hoekstra, and Kerstin J. Plessen. European clinical guidelines for tourette syndrome and other tic disorders—version 2.0. part iii: pharmacological treatment. European Child & Adolescent Psychiatry, 31:425-441, Nov 2022. URL: https://doi.org/10.1007/s00787-021-01899-z, doi:10.1007/s00787-021-01899-z. This article has 202 citations and is from a domain leading peer-reviewed journal.

25. (monfrini2025frompharmacologicaltreatment pages 1-2): E. Monfrini, Christian Saleh, D. Servello, Phillip Jaszczuk, M. Porta, Noriyuki Koibuchi, and V. Lessmann. From pharmacological treatment to neuromodulation: a comprehensive approach to managing gilles de la tourette syndrome. International Journal of Molecular Sciences, 26:8831, Sep 2025. URL: https://doi.org/10.3390/ijms26188831, doi:10.3390/ijms26188831. This article has 0 citations.

26. (monfrini2025frompharmacologicaltreatment pages 12-14): E. Monfrini, Christian Saleh, D. Servello, Phillip Jaszczuk, M. Porta, Noriyuki Koibuchi, and V. Lessmann. From pharmacological treatment to neuromodulation: a comprehensive approach to managing gilles de la tourette syndrome. International Journal of Molecular Sciences, 26:8831, Sep 2025. URL: https://doi.org/10.3390/ijms26188831, doi:10.3390/ijms26188831. This article has 0 citations.

27. (NCT04007991 chunk 1):  Ecopipam Tablets to Study Tourette's Syndrome in Children and Adolescents. Emalex Biosciences Inc.. 2019. ClinicalTrials.gov Identifier: NCT04007991

28. (NCT05615220 chunk 1):  Ecopipam Tablets to Study Tourette's Disorder in Children, Adolescents and Adults. Emalex Biosciences Inc.. 2023. ClinicalTrials.gov Identifier: NCT05615220

29. (NCT03732534 chunk 1):  Rollover Study for Continuing NBI-98854 Administration in Pediatric Subjects With Tourette Syndrome. Neurocrine Biosciences. 2018. ClinicalTrials.gov Identifier: NCT03732534

30. (NCT02674321 chunk 1):  A Pilot Study Of SD-809 (Deutetrabenazine) In Moderate To Severe Tourette Syndrome (TS). Auspex Pharmaceuticals, Inc.. 2014. ClinicalTrials.gov Identifier: NCT02674321

31. (NCT03452943 chunk 3):  Alternatives for Reducing Tics in Tourette Syndrome (TS): A Study of TEV-50717 (Deutetrabenazine) for the Treatment of Tourette Syndrome in Children and Adolescents. Teva Branded Pharmaceutical Products R&D, Inc.. 2018. ClinicalTrials.gov Identifier: NCT03452943

32. (NCT02879578 chunk 1):  Safety and Tolerability Study of NBI-98854 for the Treatment of Subjects With Tourette Syndrome. Neurocrine Biosciences. 2016. ClinicalTrials.gov Identifier: NCT02879578

33. (jiao2024progressinthe pages 1-3): Wenyan Jiao, Muhammetaly Agamedov, Guvanch D. Kerimov, Jia-Wei Zheng, Stefan Bittmann, Begench Annaye, and Fuyong Jiao. Progress in the treatment of tourette syndrome. Asian Journal of Pediatric Research, 14:39-45, Oct 2024. URL: https://doi.org/10.9734/ajpr/2024/v14i10395, doi:10.9734/ajpr/2024/v14i10395. This article has 0 citations.