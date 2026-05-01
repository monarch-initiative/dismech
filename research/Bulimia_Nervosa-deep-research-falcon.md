---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-28T09:45:49.869771'
end_time: '2026-04-28T10:13:45.410530'
duration_seconds: 1675.54
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Bulimia Nervosa
  mondo_id: ''
  category: Psychiatric
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_tokens: 5000
citation_count: 44
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Bulimia Nervosa
- **MONDO ID:**  (if available)
- **Category:** Psychiatric

## Research Objectives

Please provide a comprehensive research report on **Bulimia Nervosa** covering all of the
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
- **Disease Name:** Bulimia Nervosa
- **MONDO ID:**  (if available)
- **Category:** Psychiatric

## Research Objectives

Please provide a comprehensive research report on **Bulimia Nervosa** covering all of the
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


# Bulimia Nervosa (BN) — Disease Characteristics Research Report (Psychiatric)

## Executive summary
Bulimia nervosa (BN) is a feeding/eating disorder characterized by recurrent episodes of binge eating with loss of control followed by compensatory behaviors (e.g., self-induced vomiting, laxatives, fasting, excessive exercise), with self-evaluation unduly influenced by shape/weight concerns. DSM-5 requires symptoms on average at least weekly for 3 months; DSM-5 also grades severity by compensatory behavior frequency. BN is common, often undertreated, and associated with substantial morbidity including electrolyte abnormalities and cardiovascular complications, as well as elevated suicide risk. Recent (2023–2025) burden analyses using Global Burden of Disease (GBD) data show rising prevalence/incidence/DALYs globally, with pronounced SDI and regional heterogeneity. Evidence-based care is anchored in psychological therapies (CBT-E/CBT-BN; family-based therapy in adolescents) with adjunct pharmacotherapy (notably fluoxetine 60 mg/day) and emerging digital/neuromodulation approaches.

---

## 1. Disease information

### 1.1 Concise overview
BN is defined by recurrent binge-eating episodes with a sense of loss of control and compensatory behaviors to prevent weight gain, occurring at least weekly for at least 3 months, with undue influence of shape/weight on self-evaluation, and not occurring exclusively during anorexia nervosa. (wilson2024bulimianervosaand pages 2-3)

### 1.2 Key identifiers
- **ICD-11:** **6B81 Bulimia nervosa** (explicitly listed in a 2023 rapid review) (hay2023epidemiologyofeating pages 1-2)
- **ICD-10:** commonly mapped clinically as **F50.2** (note: not directly sourced in retrieved primary texts; included here only as a commonly used mapping and should be verified in an ICD crosswalk) (hay2023epidemiologyofeating pages 1-2)
- **MeSH / MONDO / OMIM / Orphanet:** Not retrieved in the available full-text sources within this tool run; should be added from ontology databases (gap).

### 1.3 Synonyms / alternative names
- “Bulimia”
- “Binge–purge disorder” (used descriptively in clinical contexts; not a distinct ICD-11 entity in the retrieved sources)

### 1.4 Evidence sources (patient-level vs aggregated)
This report synthesizes (i) aggregated epidemiology and burden estimates from GBD analyses (population-level modeling) and (ii) clinical trial and systematic review evidence from peer-reviewed literature (study-level aggregated clinical outcomes). (ge2025globalregionaland pages 2-4, goldstein1995longtermfluoxetinetreatment pages 1-2)

---

## 2. Etiology

### 2.1 Disease causal factors (current understanding)
BN is best understood as **multifactorial** with contributions from genetic liability, environmental exposures, and psychological traits. A 2023 pharmacotherapy meta-analysis background summarizes that eating disorders are “multifactorial, with genetic predisposition, environmental factors, and psychological characteristics involved.” (yu2023efficacyofpharmacotherapies pages 1-2)

### 2.2 Risk factors
**Psychological/behavioral and social-developmental risk factors (adolescents):**
A 2025 pediatric narrative review describes BN in youth as linked to emotional dysregulation, impulsivity, deficits in self-regulation, and psychosocial triggers including puberty-related challenges, peer pressure, and societal beauty ideals. (horovitz2025advancementsinthe pages 1-2)

**Mood disturbance and comorbidity (risk/maintenance):**
Binge eating may be “triggered by dysphoric mood” and accompanied by depression and self-criticism. A large review summarized comorbidity patterns with **mood disorders (43%) and anxiety disorders (53%)**, and that **~80–90% of BN patients** may have had at least one lifetime mood disorder episode (mostly depressive). (yu2023efficacyofpharmacotherapies pages 1-2)

### 2.3 Protective factors
Not clearly specified in the retrieved sources (gap). Prevention/intervention-focused public health strategies are suggested by GBD burden authors, but explicit protective factors are not enumerated. (liu2025globaltrendsand pages 2-3, ge2025globalregionaland pages 2-4)

### 2.4 Gene–environment interactions and epigenetic mediation
A 2024 review emphasizes that epigenetic mechanisms may mediate environmental and genetic risks across eating disorders, highlighting DNA methylation and stating that “epigenetic mechanisms serve as key mediators of environmental and genetic risk factors” and that dynamic methylation changes may influence disordered eating through altered gene expression. (wong2024epigeneticsofeating pages 1-2)

---

## 3. Phenotypes

### 3.1 Core behavioral and cognitive/affective phenotypes
- **Recurrent binge eating with loss of control** (DSM-aligned). (wilson2024bulimianervosaand pages 2-3)
- **Compensatory behaviors:** self-induced vomiting; misuse of laxatives/diuretics/enemas; fasting; excessive exercise. (wilson2024bulimianervosaand pages 1-2, wilson2024bulimianervosaand pages 2-3)
- **Self-evaluation strongly influenced by shape/weight.** (wilson2024bulimianervosaand pages 2-3)
- **Youth-associated affective features:** intense shame/guilt after binges, emotional dysregulation, impulsivity. (horovitz2025advancementsinthe pages 1-2)

### 3.2 Phenotype characteristics
- **Typical onset:** adolescence/early adulthood; one review reports median age of onset ~12.4 years. (wilson2024bulimianervosaand pages 1-2)
- **Course:** relapsing course is common; one review cites ~80% remission “with proper treatment,” but details vary by study and setting. (wilson2024bulimianervosaand pages 2-3)

### 3.3 Quality-of-life impact
Delayed identification reduces quality of life and increases comorbidity risk in primary care contexts; highlighted as a key rationale for screening/early intervention. (kozmer2025accuracyandsuitability pages 1-6)

### 3.4 Suggested HPO terms (examples; should be validated against HPO)
Behavioral:
- Binge eating → **HP:0033256 (Binge eating)** (suggested)
- Self-induced vomiting → **HP:0002013 (Vomiting)** (suggested)
- Laxative misuse (no single HPO term; may map to medication misuse / purging behavior)
Cognitive/affective:
- Body image disturbance (map to terms capturing distorted body image; specific HPO term should be confirmed)
- Impulsivity → **HP:0000710 (Impulsivity)** (suggested)

(horovitz2025advancementsinthe pages 1-2, wilson2024bulimianervosaand pages 2-3)

---

## 4. Genetic/molecular information

### 4.1 Genetic architecture (current evidence)
Heritability evidence supports a meaningful genetic component for BN.
- A 2024 epigenetics review reports twin-study heritability for BN **~55%–62%**. (wong2024epigeneticsofeating pages 1-2)
- A population-register study across Denmark/Sweden reports **moderate heritability** for BN diagnosis (~**39%**), and notes substantial heritability for core behaviors including binge eating and self-induced vomiting. (meijsen2025sharedgeneticarchitecture pages 1-4)
- Symptom-level heritability estimates reported include **self-induced vomiting ~72% in females** and a range for binge eating across sexes/samples; the authors emphasize that symptom genetics and clinical course remain under-studied. (davies2025mappingthegenetic pages 5-8)

### 4.2 Causal genes / pathogenic variants
No single-gene causal variants for BN were identified in the retrieved sources; BN is discussed as polygenic/multifactorial. (meijsen2025sharedgeneticarchitecture pages 1-4, wong2024epigeneticsofeating pages 1-2)

### 4.3 Epigenetics
DNA methylation is highlighted as a likely mediator of environmental/genetic risk in eating disorders broadly, with current limitations including sample size and biomarker scarcity. (wong2024epigeneticsofeating pages 1-2)

### 4.4 Gene–environment interactions
A 2025 symptom-onset genetics preprint emphasizes interplay: “genetic risk interacts with early environment and sex-at-birth” (general statement; not BN-specific mechanistic GxE). (davies2025mappingthegenetic pages 5-8)

**Suggested GO biological process terms (examples):**
- Regulation of feeding behavior (confirm GO ID)
- Reward processing / dopaminergic signaling (confirm GO IDs)
- DNA methylation (e.g., GO:0006306; confirm)

---

## 5. Environmental information

### 5.1 Environmental and lifestyle contributors
Recent reviews emphasize socio-cultural and personal experiential contributors (e.g., beauty ideals, peer pressure), with adolescence as a vulnerable developmental window. (horovitz2025advancementsinthe pages 1-2, wong2024epigeneticsofeating pages 1-2)

### 5.2 Infectious agents
Not applicable based on retrieved evidence (no pathogen-triggered etiology described).

---

## 6. Mechanism / pathophysiology

### 6.1 Conceptual causal chain (current consensus framing)
A practical mechanistic framing supported by the retrieved clinical literature is:
1) underlying vulnerability (genetic liability + environmental/psychological stressors) (yu2023efficacyofpharmacotherapies pages 1-2, meijsen2025sharedgeneticarchitecture pages 1-4)
2) episodes of loss-of-control eating (binge eating), often mood-triggered (yu2023efficacyofpharmacotherapies pages 1-2)
3) compensatory behaviors (purging/non-purging) leading to physiologic perturbations (dehydration, electrolyte abnormalities) (alharbi2024effectivetreatmentapproaches pages 5-6)
4) downstream medical complications (cardiovascular, dental/oral, GI, respiratory) and psychiatric morbidity/suicidality (wilson2024bulimianervosaand pages 1-2)

### 6.2 Epigenetic mediation hypothesis
Epigenetics is proposed as a bridge between environmental exposures and gene expression changes relevant to disordered eating behaviors, particularly via DNA methylation. (wong2024epigeneticsofeating pages 1-2)

### 6.3 Molecular profiling / biomarkers
The epigenetics review notes that biomarker research “significantly lags behind” for eating disorders; no validated BN biomarker diagnostic was identified in retrieved sources. (wong2024epigeneticsofeating pages 1-2)

**Suggested CL cell types (examples; confirm in Cell Ontology):**
- Neuron (CL:0000540)
- GABAergic neuron (as implicated in ED transcriptomics in related work; not BN-specific in retrieved evidence) (ahmed2025psychologicalapproachesfor pages 3-6)

---

## 7. Anatomical structures affected
BN affects multiple organ systems primarily through binge/purge behaviors.

### 7.1 Organ-level (examples)
- **Cardiovascular system:** electrolyte disturbances increase cardiovascular risk including ischemic heart disease; “abnormal heartbeat patterns” are cited in inpatient-indication criteria. (wilson2024bulimianervosaand pages 1-2, alharbi2024effectivetreatmentapproaches pages 5-6)
- **Oral cavity and salivary glands:** dental erosion; salivary gland hypertrophy. (wilson2024bulimianervosaand pages 1-2)
- **Pharynx/esophagus:** pharyngeal trauma; esophageal damage from vomiting. (wilson2024bulimianervosaand pages 1-2, horovitz2025advancementsinthe pages 1-2)
- **Respiratory system:** aspiration pneumonia risk. (wilson2024bulimianervosaand pages 1-2)
- **Gastrointestinal tract:** bloating, dysphagia, acid reflux. (wilson2024bulimianervosaand pages 2-3)
- **Reproductive/endocrine:** irregular menses. (wilson2024bulimianervosaand pages 2-3)

### 7.2 Suggested UBERON terms (examples; confirm)
- Heart (UBERON:0000948)
- Esophagus (UBERON:0001043)
- Salivary gland (UBERON:0001836)
- Tooth (UBERON:0001091)
- Stomach (UBERON:0000945)

---

## 8. Temporal development

### 8.1 Onset
Evidence indicates typical onset in adolescence/early adulthood, with median onset reported as ~12.4 years in one 2024 review; another synthesis reports average onset 16–17 years. (wilson2024bulimianervosaand pages 1-2, yu2023efficacyofpharmacotherapies pages 1-2)

### 8.2 Progression/course
BN can be chronic with relapse; prognosis is variable and influenced by psychological factors and treatment timing. (wilson2024bulimianervosaand pages 2-3)

---

## 9. Inheritance and population

### 9.1 Epidemiology (recent statistics)
**Sex-specific pooled prevalence (global):** A 2023 MJA review table reports BN prevalence estimates:
- **12-month:** women **0.7%**, men **0.4%**
- **Lifetime:** women **1.9%**, men **0.6%**
- **Point:** women **1.5%**, men **0.1%** (hay2023currentapproachesin pages 2-3, hay2023currentapproachesin media 4293f313)

**GBD 2021 global burden (BN-specific):**
A 2025 GBD analysis reports global increases from 1990 to 2021:
- Incident cases: **5,595,035 → 8,227,657**
- Prevalent cases: **7,416,420 → 12,367,024**
- DALYs: **1,564,211 → 2,604,702**
with increasing ASRs (EAPCs: prevalence 0.66; incidence 0.55; DALYs 0.67). (ge2025globalregionaland pages 2-4)

**SDI disparities (2021):** High-SDI ASPR **311.26/100,000** vs Low-SDI **96.69/100,000**; high-SDI DALYs rate **65.38/100,000** vs low-SDI **20.31/100,000**. (ge2025globalregionaland pages 2-4)

**Country example (Iran, GBD 2019):** BN ASPR **186.42/100,000** (2019). (amiri2025trendsprevalenceincidence pages 1-2)

### 9.2 Inheritance pattern
BN is consistent with **complex/polygenic** inheritance with moderate-to-high heritability estimates. (meijsen2025sharedgeneticarchitecture pages 1-4, wong2024epigeneticsofeating pages 1-2)

---

## 10. Diagnostics

### 10.1 Clinical criteria
DSM-5-aligned clinical features summarized in a 2024 review include: binge eating with loss of control, recurrent compensatory behaviors, frequency at least weekly for 3 months, undue influence of weight/shape on self-evaluation, and exclusion of anorexia nervosa. (wilson2024bulimianervosaand pages 2-3)

### 10.2 Diagnostic tests and instruments
- **EDE (Eating Disorder Examination) interview** is described as the **gold standard** diagnostic interview; **EDE-Q** is its self-report derivative used for diagnostic assessment/psychopathology. (hay2023currentapproachesin pages 2-3)

### 10.3 Screening in real-world settings (primary care)
- The MJA review states that screening measures “lack high levels of positive predictive power,” indicating false positives are common and positive screens should be followed by diagnostic evaluation. (hay2023currentapproachesin pages 2-3)
- A 2025 BJGP Open primary-care screening systematic review reports for **SCOFF** (BN): **sensitivity 97.88%–100%** and **specificity 89.6%–94.4%**, noting increased false positives and reporting low PPV (~24.4% in one study). It also identifies implementation barriers: time constraints, stigma, and lack of trust in screening/clinicians. (kozmer2025accuracyandsuitability pages 14-18, kozmer2025accuracyandsuitability pages 1-6)

### 10.4 Biomarkers / imaging
No validated biomarker diagnostics for BN were identified in the retrieved sources; biomarker research is described as lagging. (wong2024epigeneticsofeating pages 1-2)

---

## 11. Outcome / prognosis

### 11.1 Morbidity and mortality
BN is associated with medical complications of purging (electrolyte abnormalities, cardiovascular disease) and elevated mortality and suicide risk. A 2024 review reports standardized mortality in BN of **~1.5–2.5%** and suicide risk **~8-fold** versus the general population. (wilson2024bulimianervosaand pages 1-2)

### 11.2 Treatment seeking and disparities (real-world implementation)
A 2024 review reports that **~85–94%** of people with BN “never seek or delay treatment,” often delaying by **4–5 years**. Reviewed RCT samples were predominantly female and White, suggesting evidence gaps for males and racial minorities and potential disparities in access and representation. (wilson2024bulimianervosaand pages 1-2)

---

## 12. Treatment

### 12.1 Evidence-based psychological therapies
- CBT-E is described as first-line for adults and typically delivered over **~20 weekly sessions** for BN. (hay2023currentapproachesin pages 2-3)
- In adolescents, evidence supports **FBT-BN** and CBT variants. A 109-participant RCT reported end-of-treatment abstinence **39.4% (FBT-BN) vs 19.7% (CBT-A)** and 6-month abstinence **44% vs 25.4%**, favoring FBT-BN. (alharbi2024effectivetreatmentapproaches pages 5-6)

### 12.2 Pharmacotherapy
**Fluoxetine 60 mg/day:**
A multicenter double-blind placebo-controlled trial (1995) in DSM-III-R BN patients randomized **398** (3:1 fluoxetine 60 mg/day vs placebo) found significantly greater reductions in vomiting and binge-eating episodes, concluding fluoxetine was safe and effective up to 16 weeks. (goldstein1995longtermfluoxetinetreatment pages 1-2)

**Medication class evidence (meta-analysis):**
A 2023 systematic review/meta-analysis of 33 studies across multiple drug classes reported pooled improvements vs placebo in binge eating (SMD -0.40), vomiting (SMD -0.16), depressive symptoms (SMD -0.32), and weight (WMD -3.05 kg), with increased dropout due to adverse events (RR 1.66). (yu2023efficacyofpharmacotherapies pages 1-2)

### 12.3 Emerging interventions
Emerging/adjunct approaches include virtual reality-assisted therapy, neuromodulation (e.g., rTMS), and digitally delivered CBT (including guided internet-based CBT trial protocols), with evidence still developing. (lynch2025eatingdisordersclinical pages 3-4, wilson2024bulimianervosaand pages 2-3)

### 12.4 MAXO term suggestions
See Treatment Evidence Table (artifact-02).

---

## 13. Prevention

High-quality BN-specific primary prevention trials were not identified in the retrieved sources; however, burden analyses emphasize prevention and early intervention as priorities given projected increases. (liu2025globaltrendsand pages 2-3, ge2025globalregionaland pages 2-4)

Practical prevention-related actions supported by the diagnostic literature include:
- **Secondary prevention:** screening (with appropriate follow-up due to false positives) and early referral pathways in primary care. (kozmer2025accuracyandsuitability pages 14-18, hay2023currentapproachesin pages 2-3)

---

## 14. Other species / natural disease
No naturally occurring BN analogue in other species was identified in the retrieved sources (gap).

---

## 15. Model organisms
No BN-specific validated animal model details were retrieved in this tool run (gap).

---

## Recent developments (2023–2025 highlights)
1) **Global burden quantification and projections:** BN-specific GBD analyses (1990–2021; projections to 2030) quantify rising incident and prevalent cases and DALYs, with SDI and regional heterogeneity. (ge2025globalregionaland pages 2-4)
2) **Primary-care screening evidence synthesis:** Updated synthesis of screening tool accuracy/suitability in primary care highlights high sensitivity but imperfect specificity and implementation barriers. (kozmer2025accuracyandsuitability pages 14-18, kozmer2025accuracyandsuitability pages 1-6)
3) **Expanding mechanistic framing via epigenetics:** Reviews highlight DNA methylation and epigenetic mediation as a plausible pathway linking environment and genetic risk, while noting biomarker gaps. (wong2024epigeneticsofeating pages 1-2)

---

## Embedded summary artifacts

| Disease | Category | Key identifiers | DSM-5 core diagnostic features | DSM-5 severity specifier | Key diagnostic/screening instruments |
|---|---|---|---|---|---|
| Bulimia nervosa (BN) | Psychiatric; feeding/eating disorder | ICD-11: **6B81**; ICD-10 commonly mapped as **F50.2**; DSM-5 feeding and eating disorder (hay2023epidemiologyofeating pages 1-2) | Recurrent binge-eating episodes with loss of control **plus** recurrent inappropriate compensatory behaviors (for example self-induced vomiting, laxative/diuretic misuse, fasting, or excessive exercise), occurring on average **at least once weekly for 3 months**; self-evaluation unduly influenced by body shape/weight; disturbance does **not** occur exclusively during anorexia nervosa (wilson2024bulimianervosaand pages 2-3, yu2023efficacyofpharmacotherapies pages 1-2) | Severity based on average number of inappropriate compensatory behaviors per week: **Mild 1–3; Moderate 4–7; Severe 8–13; Extreme 14+** (wilson2024bulimianervosaand pages 1-2) | **EDE** (Eating Disorder Examination) diagnostic interview = gold standard; **EDE-Q** self-report derivative used for diagnostic assessment/psychopathology; brief screening tools: **SCOFF** and **SDE** (Screen for Disordered Eating), with SCOFF widely used and SDE noted as highly sensitive; SCOFF sensitivity for BN in primary care reported at **97.88%–100%** with specificity **89.6%–94.4%** (hay2023currentapproachesin pages 2-3, kozmer2025accuracyandsuitability pages 1-6) |


*Table: This table summarizes the core identifiers, DSM-5 diagnostic features, severity specifier, and commonly used diagnostic/screening tools for bulimia nervosa. It is useful as a compact reference for disease ontology mapping and clinical diagnosis.*

| Source | Year | Journal | URL / DOI | Population / scope | Key bulimia nervosa estimates | Citation |
|---|---:|---|---|---|---|---|
| Hay et al. | 2023 | *Medical Journal of Australia* | https://doi.org/10.5694/mja2.52008 | Global pooled prevalence estimates | **12-month prevalence:** women **0.7%**, men **0.4%**; **Lifetime prevalence:** women **1.9%**, men **0.6%**; **Point prevalence:** women **1.5%**, men **0.1%** | (hay2023currentapproachesin pages 2-3, hay2023currentapproachesin media 4293f313) |
| Ge et al. | 2025 | *Journal of Eating Disorders* | https://doi.org/10.1186/s40337-025-01289-9 | Global GBD 1990–2021 | Incident cases rose from **5,595,035 (1990)** to **8,227,657 (2021)**; prevalent cases from **7,416,420** to **12,367,024**; DALYs from **1,564,211** to **2,604,702**; global EAPCs: prevalence **0.66** (95% UI **0.61–0.71**), incidence **0.55** (**0.52–0.58**), DALYs **0.67** (**0.62–0.72**) | (ge2025globalregionaland pages 2-4) |
| Ge et al. | 2025 | *Journal of Eating Disorders* | https://doi.org/10.1186/s40337-025-01289-9 | 2021 SDI-stratified burden | **High SDI:** ASPR **311.26/100,000** (95% UI **211.22–435.75**), ASIR **159.5/100,000** (**101.9–230.34**), age-standardized DALYs **65.38/100,000** (**37.29–106.61**); **Low SDI:** ASPR **96.69/100,000** (**62.85–140.31**), ASIR **82.94/100,000** (**51.73–124.85**), age-standardized DALYs **20.31/100,000** (**11.42–33.98**) | (ge2025globalregionaland pages 2-4) |
| Amiri & Hosseini | 2025 | *Eating and Weight Disorders* | https://doi.org/10.1007/s40519-025-01769-6 | Iran, GBD 2019 | BN age-standardized prevalence rate (ASPR) **186.42 per 100,000** in **2019**; overall ED ASPR **254/100,000** (UI **189–328**); overall ED DALYs **53.94/100,000** (UI **33.53–80.20**) | (amiri2025trendsprevalenceincidence pages 1-2) |
| Liu et al. | 2025 | *The British Journal of Psychiatry* | https://doi.org/10.1192/bjp.2025.10450 | Ages **15–29 years**, global GBD 1990–2021 | BN incidence increased **44.68%** from **298.24** to **351.29 per 100,000**; ASR increase **17.79%**; incidence EAPC **0.56** (95% UI **0.53–0.58**); BN total cases increased **53.18%**; BN DALYs increased **53.12%** with ASR increase **22.39%** and DALY EAPC **0.72** | (liu2025globaltrendsand pages 2-3) |


*Table: This table compiles key recent bulimia nervosa epidemiology and burden estimates from pooled prevalence reviews and GBD-based analyses. It is useful for quickly comparing sex-specific prevalence, global burden trends, SDI disparities, and country-specific rates.*

| Treatment | Population / setting | Evidence / study details | Key outcomes | Suggested MAXO term | Citation |
|---|---|---|---|---|---|
| CBT-E / CBT-BN (first-line psychotherapy) | Adults with BN; typically outpatient | CBT-E is described as first-line for adults and is typically delivered over **20 weekly sessions** for bulimia nervosa; unified meta-analysis of CBT across adult mental disorders found effect sizes for BN **between 0.5 and 1.0** vs inactive controls | First-line adult psychotherapy; moderate efficacy range in meta-analysis; used in routine care and guidelines | MAXO: cognitive behavioral psychotherapy | (hay2023currentapproachesin pages 2-3) |
| FBT-BN vs CBT-A | Adolescents aged **12–18** with DSM-5 BN or partial BN | RCT summarized in 2024 review: **109 adolescents** randomized to **FBT-BN** or **CBT-A**, **18 sessions over 6 months** | Abstinence at end of treatment **39.4% vs 19.7%** (*p*=0.04) favoring FBT-BN; at 6 months **44.0% vs 25.4%** (*p*=0.03); no significant difference at 12 months | MAXO: family therapy | (alharbi2024effectivetreatmentapproaches pages 5-6) |
| Family-based therapy (FBT) vs CBT / supportive psychotherapy | Adolescents with BN | Three high-quality RCTs summarized in review | Remission higher with **FBT vs CBT: 39% vs 20%**; higher with **FBT vs supportive psychotherapy: 39% vs 18%**; similar to guided self-help CBT in one trial (**10% vs 14%**) | MAXO: family therapy | (alharbi2024effectivetreatmentapproaches pages 5-6) |
| Fluoxetine **60 mg/day** | Adult outpatients with BN | Double-blind multicenter trial at **15 US clinics**; **483 entered, 398 randomized** (3:1 fluoxetine 60 mg/day vs placebo), **225 completed** over **16 weeks** | Greater reductions in vomiting (**F[1,360]=14.73, P<0.0001**) and binge-eating (**F[1,360]=14.39, P=0.0002**) vs placebo; judged safe on adverse event, vital sign, and lab analyses | MAXO: selective serotonin reuptake inhibitor therapy | (goldstein1995longtermfluoxetinetreatment pages 1-2) |
| Pharmacotherapy overall (all drug classes pooled) | BN patients across RCTs | 2023 systematic review/meta-analysis of **33 studies**, **11 drugs**, 6 drug classes: TCAs, SSRIs, MAOIs, antiepileptics, lithium, fenfluramine | vs placebo: binge-eating frequency **SMD -0.40** (95% CI **-0.61 to -0.19**); vomiting **SMD -0.16** (**-0.30 to -0.03**); depressive symptoms **SMD -0.32** (**-0.51 to -0.13**); weight **WMD -3.05** kg (**-5.97 to -0.13**); dropout due to adverse events **RR 1.66** (**1.14 to 2.41**) | MAXO: pharmacotherapy | (yu2023efficacyofpharmacotherapies pages 1-2) |
| SSRIs (class; includes fluoxetine, citalopram, fluvoxamine) | BN patients in RCTs | Most studied drug class in 2023 meta-analysis (**14 SSRI trials**) | Contribute to pooled reductions in binge eating and vomiting; fluoxetine is the best-established SSRI and specifically supported at **60 mg/day** | MAXO: selective serotonin reuptake inhibitor therapy | (yu2023efficacyofpharmacotherapies pages 1-2, goldstein1995longtermfluoxetinetreatment pages 1-2) |
| TCAs / MAOIs / topiramate and other agents | BN patients in RCTs | Included in pooled 2023 meta-analysis: **8 TCA trials**, **6 MAOI trials**, **3 topiramate trials**, plus lithium and fenfluramine | Drug effects varied by class; pooled benefits were statistically favorable but authors concluded overall efficacy remained limited/heterogeneous | MAXO: antidepressant therapy / antiepileptic therapy | (yu2023efficacyofpharmacotherapies pages 1-2) |
| Guided internet-based CBT (ICBT) + treatment as usual | Women with BN; multicenter Japan trial protocol | 2023 multicenter assessor-blinded RCT protocol comparing **ICBT + TAU** vs **TAU** at **7 institutions**; outcomes include binge eating + purging, ED severity, depression, anxiety, QoL, satisfaction | Emerging digital implementation strategy aimed at improving access; efficacy results pending in protocol paper | MAXO: telehealth cognitive behavioral psychotherapy | (yu2023efficacyofpharmacotherapies pages 1-2) |
| Other emerging interventions (DBT, ICAT, VR, PED-t, rTMS, D-cycloserine, motivational interviewing) | Mostly outpatient adult BN studies | 2024 treatment-disparities review of **17 RCTs** reported trials of multiple psychosocial and adjunctive approaches beyond CBT | Evidence base is smaller than for CBT/FBT; reviewed as adjunctive or alternative modalities rather than established first-line care | MAXO: dialectical behavior therapy / virtual reality therapy / transcranial magnetic stimulation | (wilson2024bulimianervosaand pages 2-3, lynch2025eatingdisordersclinical pages 3-4) |


*Table: This table summarizes key bulimia nervosa treatments across psychotherapy, pharmacotherapy, and emerging digital or neuromodulatory approaches. It highlights study design, trial size, quantitative outcomes, and suggested MAXO mappings to support knowledge-base annotation.*

---

## Visual evidence
Bulimia nervosa sex-stratified prevalence estimates (12-month, lifetime, and point prevalence) are shown in the extracted Box 2 table from the 2023 MJA review. (hay2023currentapproachesin media 4293f313)

---

## Limitations of this report (evidence gaps)
- **MONDO/MeSH/OMIM/Orphanet identifiers** were not retrieved from ontology databases in this tool run; these should be added from authoritative ontology sources.
- **BN-specific GWAS loci/genes and variant-level annotations** were not available in retrieved sources; evidence here is largely heritability and conceptual mechanistic framing.
- **Model organisms and cross-species evidence** were not retrieved.
- **Biomarker diagnostics** are described as underdeveloped; no validated BN biomarker was identified.

---

## Key source URLs (selected)
- Hay et al., *Med J Aust* (2023-06): https://doi.org/10.5694/mja2.52008 (hay2023currentapproachesin pages 2-3)
- Hay et al., *J Eat Disord* (2023-02): https://doi.org/10.1186/s40337-023-00738-7 (hay2023epidemiologyofeating pages 1-2)
- Wilson & Kagabo, *Front Psychol* (2024-08): https://doi.org/10.3389/fpsyg.2024.1386347 (wilson2024bulimianervosaand pages 1-2)
- Ge et al., *J Eat Disord* (2025-06): https://doi.org/10.1186/s40337-025-01289-9 (ge2025globalregionaland pages 2-4)
- Yu et al., *BMC Pharmacol Toxicol* (2023-12): https://doi.org/10.1186/s40360-023-00713-7 (yu2023efficacyofpharmacotherapies pages 1-2)
- Goldstein et al., *Br J Psychiatry* (1995-05): https://doi.org/10.1192/bjp.166.5.660 (goldstein1995longtermfluoxetinetreatment pages 1-2)
- Kozmér et al., *BJGP Open* (2025-10): https://doi.org/10.3399/bjgpo.2025.0149 (kozmer2025accuracyandsuitability pages 1-6)


References

1. (wilson2024bulimianervosaand pages 2-3): Kim Wilson and Robert Kagabo. Bulimia nervosa and treatment-related disparities: a review. Frontiers in Psychology, Aug 2024. URL: https://doi.org/10.3389/fpsyg.2024.1386347, doi:10.3389/fpsyg.2024.1386347. This article has 11 citations and is from a peer-reviewed journal.

2. (hay2023epidemiologyofeating pages 1-2): Phillipa Hay, Phillip Aouad, Anvi Le, Peta Marks, Danielle Maloney, Sarah Barakat, Robert Boakes, Leah Brennan, Emma Bryant, Susan Byrne, Belinda Caldwell, Shannon Calvert, Bronny Carroll, David Castle, Ian Caterson, Belinda Chelius, Lyn Chiem, Simon Clarke, Janet Conti, Lexi Crouch, Genevieve Dammery, Natasha Dzajkovski, Jasmine Fardouly, John Feneley, Nasim Foroughi, Mathew Fuller-Tyszkiewicz, Anthea Fursland, Veronica Gonzalez-Arce, Bethanie Gouldthorp, Kelly Griffin, Scott Griffiths, Ashlea Hambleton, Amy Hannigan, Mel Hart, Susan Hart, Ian Hickie, Francis Kay-Lambkin, Ross King, Michael Kohn, Eyza Koreshe, Isabel Krug, Jake Linardon, Randall Long, Amanda Long, Sloane Madden, Siân McLean, Thy Meddick, Jane Miskovic-Wheatley, Deborah Mitchison, Richard O’Kearney, Roger Paterson, Susan Paxton, Melissa Pehlivan, Genevieve Pepin, Andrea Phillipou, Judith Piccone, Rebecca Pinkus, Bronwyn Raykos, Paul Rhodes, Elizabeth Rieger, Karen Rockett, Sarah Rodan, Janice Russell, Haley Russell, Fiona Salter, Susan Sawyer, Beth Shelton, Urvashnee Singh, Sophie Smith, Evelyn Smith, Karen Spielman, Sarah Squire, Juliette Thomson, Marika Tiggemann, Ranjani Utpala, Lenny Vartanian, Andrew Wallis, Warren Ward, Sarah Wells, Eleanor Wertheim, Simon Wilksch, Michelle Williams, Stephen Touyz, and Sarah Maguire. Epidemiology of eating disorders: population, prevalence, disease burden and quality of life informing public policy in australia—a rapid review. Journal of Eating Disorders, Feb 2023. URL: https://doi.org/10.1186/s40337-023-00738-7, doi:10.1186/s40337-023-00738-7. This article has 189 citations and is from a peer-reviewed journal.

3. (ge2025globalregionaland pages 2-4): Yihao Ge, Shanshan Zhang, Zekun Li, Hongmin Guo, Xiaohan Li, Zhiyong Li, Fang Dong, and Feng Zhang. Global, regional and national level burden of bulimia nervosa from 1990 to 2021 and their projections to 2030: analysis of the global burden of disease study. Journal of Eating Disorders, Jun 2025. URL: https://doi.org/10.1186/s40337-025-01289-9, doi:10.1186/s40337-025-01289-9. This article has 1 citations and is from a peer-reviewed journal.

4. (goldstein1995longtermfluoxetinetreatment pages 1-2): David J. Goldstein, Michael G. Wilson, Vicki L. Thompson, Janet H. Potvin, and Alvin H. Rampey. Long-term fluoxetine treatment of bulimia nervosa. British Journal of Psychiatry, 166:660-666, May 1995. URL: https://doi.org/10.1192/bjp.166.5.660, doi:10.1192/bjp.166.5.660. This article has 301 citations and is from a highest quality peer-reviewed journal.

5. (yu2023efficacyofpharmacotherapies pages 1-2): Sijie Yu, Yuhan Zhang, Chongkai Shen, and Fei Shao. Efficacy of pharmacotherapies for bulimia nervosa: a systematic review and meta-analysis. BMC Pharmacology and Toxicology, Dec 2023. URL: https://doi.org/10.1186/s40360-023-00713-7, doi:10.1186/s40360-023-00713-7. This article has 19 citations.

6. (horovitz2025advancementsinthe pages 1-2): Omer Horovitz. Advancements in the diagnosis and treatment of eating disorders in children and adolescents: challenges, progress, and future directions. Nutrients, 17:1744, May 2025. URL: https://doi.org/10.3390/nu17101744, doi:10.3390/nu17101744. This article has 10 citations.

7. (liu2025globaltrendsand pages 2-3): Lu Liu, Ke Wang, Mengqin Dai, Wenxiu Luo, Lei Tang, Xianghong Ding, Yun Liu, Liling Wu, Nian Liu, and Jiaming Luo. Global trends and future projections of eating disorders among adolescents and young adults: comprehensive analysis from 1990 to 2050 using eight machine-learning models. The British Journal of Psychiatry, pages 1-15, Nov 2025. URL: https://doi.org/10.1192/bjp.2025.10450, doi:10.1192/bjp.2025.10450. This article has 2 citations.

8. (wong2024epigeneticsofeating pages 1-2): Chloe Wong, Sang Hyuck Lee, Ying-Young Hui, Gerome Breen, and Moritz Herle. Epigenetics of eating disorders: from genetic and molecular pathways to therapeutic possibilities. Cutting Edge Psychiatry in Practice, 6:18-25, Dec 2024. URL: https://doi.org/10.65031/rzeq8592, doi:10.65031/rzeq8592. This article has 0 citations.

9. (wilson2024bulimianervosaand pages 1-2): Kim Wilson and Robert Kagabo. Bulimia nervosa and treatment-related disparities: a review. Frontiers in Psychology, Aug 2024. URL: https://doi.org/10.3389/fpsyg.2024.1386347, doi:10.3389/fpsyg.2024.1386347. This article has 11 citations and is from a peer-reviewed journal.

10. (kozmer2025accuracyandsuitability pages 1-6): Stella Kozmér, Ruichen Yin, Joseph Evans, Alex Burns, and Jane Smith. Accuracy and suitability of eating disorder screening tools for binge eating disorder and bulimia nervosa in a primary care setting: a systematic review and narrative summary. BJGP Open, pages BJGPO.2025.0149, Oct 2025. URL: https://doi.org/10.3399/bjgpo.2025.0149, doi:10.3399/bjgpo.2025.0149. This article has 0 citations and is from a peer-reviewed journal.

11. (meijsen2025sharedgeneticarchitecture pages 1-4): Joeri Meijsen, Kejia Hu, Dang Wei, Stefana Aicoboaie, Helena L Davies, Ruyue Zhang, Mischa Lundberg, Richard Zetterberg, Joëlle Pasman, Weimin Ye, Thomas Werge, Cynthia M. Bulik, Fang Fang, Alfonso Buil, and Nadia Micali. Shared genetic architecture between eating disorders, mental health conditions, and cardiometabolic diseases: a comprehensive population-wide study across two countries. MedRxiv, Oct 2025. URL: https://doi.org/10.1101/2024.10.20.24315825, doi:10.1101/2024.10.20.24315825. This article has 6 citations.

12. (davies2025mappingthegenetic pages 5-8): Helena L. Davies, Abigail R. ter Kuile, Sang Hyuck Lee, Rujia Wang, Jessica Mundy, Zain-Ul-Abideen Ahmad, Jonathan Coleman, Saakshi Kakar, Emily Kelly, Chelsea Mika Malouf, Gursharan Kalsi, Moritz Herle, Gerome Breen, and Christopher Hübel. Mapping the genetic landscape of the age at onset and severity of eating disorder symptoms. MedRxiv, Sep 2025. URL: https://doi.org/10.1101/2025.09.25.25336612, doi:10.1101/2025.09.25.25336612. This article has 0 citations.

13. (alharbi2024effectivetreatmentapproaches pages 5-6): Yara Alharbi, Fatema Saleh, and Khaled A Shahat. Effective treatment approaches for eating disorders in children and adolescents: a review article. Cureus, Nov 2024. URL: https://doi.org/10.7759/cureus.74003, doi:10.7759/cureus.74003. This article has 4 citations.

14. (ahmed2025psychologicalapproachesfor pages 3-6): Fatema Ahmed, Chen Wu, Li Li, Qingyuan Ye, Waleed Ksebe, and Kefang Wang. Psychological approaches for eating disorders: the role of body image, self-esteem, and quality of life. Psychotherapy in the Third Millennium - Cross-Cutting Themes and Proposals for Reflection, Mar 2025. URL: https://doi.org/10.5772/intechopen.1009601, doi:10.5772/intechopen.1009601. This article has 4 citations.

15. (hay2023currentapproachesin pages 2-3): Phillipa J. Hay, Rebekah M. Rankin, Lucie M. Ramjan, and J. Conti. Current approaches in the recognition and management of eating disorders. Medical Journal of Australia, 219:127-134, Jun 2023. URL: https://doi.org/10.5694/mja2.52008, doi:10.5694/mja2.52008. This article has 21 citations and is from a peer-reviewed journal.

16. (hay2023currentapproachesin media 4293f313): Phillipa J. Hay, Rebekah M. Rankin, Lucie M. Ramjan, and J. Conti. Current approaches in the recognition and management of eating disorders. Medical Journal of Australia, 219:127-134, Jun 2023. URL: https://doi.org/10.5694/mja2.52008, doi:10.5694/mja2.52008. This article has 21 citations and is from a peer-reviewed journal.

17. (amiri2025trendsprevalenceincidence pages 1-2): Sohrab Amiri and Seyed Morteza Hosseini. Trends, prevalence, incidence, and disability-adjusted life years of anorexia nervosa and bulimia nervosa in iran: global burden of disease study. Eating and Weight Disorders, Jul 2025. URL: https://doi.org/10.1007/s40519-025-01769-6, doi:10.1007/s40519-025-01769-6. This article has 0 citations.

18. (kozmer2025accuracyandsuitability pages 14-18): Stella Kozmér, Ruichen Yin, Joseph Evans, Alex Burns, and Jane Smith. Accuracy and suitability of eating disorder screening tools for binge eating disorder and bulimia nervosa in a primary care setting: a systematic review and narrative summary. BJGP Open, pages BJGPO.2025.0149, Oct 2025. URL: https://doi.org/10.3399/bjgpo.2025.0149, doi:10.3399/bjgpo.2025.0149. This article has 0 citations and is from a peer-reviewed journal.

19. (lynch2025eatingdisordersclinical pages 3-4): D. Lynch, H. Ogutlu, O. Gundogdu-Ogutlu, E. Barrett, and F. McNicholas. Eating disorders: clinical update. Irish Journal of Psychological Medicine, pages 1-5, Jan 2025. URL: https://doi.org/10.1017/ipm.2024.47, doi:10.1017/ipm.2024.47. This article has 2 citations.