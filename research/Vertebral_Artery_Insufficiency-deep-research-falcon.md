---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-06T15:02:20.045873'
end_time: '2026-05-06T15:23:52.718460'
duration_seconds: 1292.67
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Vertebral Artery Insufficiency
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 43
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Vertebral Artery Insufficiency
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Vertebral Artery Insufficiency** covering all of the
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
- **Disease Name:** Vertebral Artery Insufficiency
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Vertebral Artery Insufficiency** covering all of the
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


## Comprehensive Research Report: Vertebral Artery Insufficiency (VAI) / Vertebrobasilar Insufficiency (VBI)

### Executive summary (current understanding)
Vertebral artery insufficiency (often discussed clinically as vertebrobasilar insufficiency, vertebrobasilar disease, or symptomatic vertebral artery stenosis/occlusion) refers to transient ischemic attacks (TIA) or ischemic strokes attributable to pathology of the vertebral arteries and/or basilar artery, most commonly atherosclerotic stenosis/occlusion, but also dissection/trauma or other less common causes. These conditions contribute substantially to posterior-circulation ischemia and carry high early recurrence risk under medical therapy alone, motivating aggressive secondary prevention and selective revascularization in refractory cases. (bobmanuel2023vertebralarteryinterventions pages 1-2, aminhanjani2010vertebrobasilarflowevaluation pages 1-2)

---

## 1. Disease information

### 1.1 What is the disease?
In contemporary cerebrovascular literature, “vertebral artery insufficiency” is not consistently treated as a single discrete nosologic entity; rather it is typically operationalized as *symptomatic posterior circulation ischemia due to vertebral artery (extracranial or intracranial) stenosis/occlusion* and/or broader *atherosclerotic vertebrobasilar disease*. The VERiTAS study frames the clinical problem as symptomatic atherosclerotic vertebrobasilar disease causing posterior circulation stroke, emphasizing that recurrence risk is high and that hemodynamic compromise is a key determinant of risk. (aminhanjani2010vertebrobasilarflowevaluation pages 1-2)

A 2023 comprehensive review similarly uses overlapping terminology (VAS, vertebrobasilar ischemia/insufficiency) and describes vertebral artery stenosis as a driver of posterior circulation ischemia that may be asymptomatic or symptomatic. (bobmanuel2023vertebralarteryinterventions pages 4-5, bobmanuel2023vertebralarteryinterventions pages 2-3)

### 1.2 Key identifiers (OMIM/Orphanet/ICD/MeSH/MONDO)
*Not available from the retrieved evidence set.* The sourced papers and guideline excerpts used here do not provide definitive ICD-10/ICD-11, MeSH, OMIM, Orphanet, or MONDO identifiers specific to “vertebral artery insufficiency/vertebrobasilar insufficiency.” This report therefore focuses on evidence-based clinical characterization and management rather than coding/ontology assertions.

### 1.3 Synonyms and alternative names
Commonly used overlapping terms in the literature include:
- Vertebrobasilar insufficiency (VBI) / vertebrobasilar ischemia (bobmanuel2023vertebralarteryinterventions pages 4-5, bobmanuel2023vertebralarteryinterventions pages 3-4)
- Atherosclerotic vertebrobasilar disease (VBD) (aminhanjani2010vertebrobasilarflowevaluation pages 1-2)
- Vertebral artery stenosis (VAS) / vertebral artery stenosis and occlusion (VASO) (zhang2023microsurgicalrevascularizationof pages 1-2)
- Posterior circulation ischemia / posterior circulation stroke (markus2022treatmentofposterior pages 1-2)

### 1.4 Evidence source type
The information below is derived from aggregated disease-level evidence, including:
- Peer-reviewed reviews and guideline documents (bobmanuel2023vertebralarteryinterventions pages 4-5, markus2022treatmentofposterior pages 1-2, bushnell20242024guidelinefor pages 25-26)
- Prospective observational studies (VERiTAS rationale and analyses) (aminhanjani2010vertebrobasilarflowevaluation pages 1-2)
- Retrospective real-world surgical/endovascular cohorts (ryu2023instentrestenosisand pages 2-4, liu2024applicationofmicrosurgical pages 1-2)
- Systematic reviews/meta-analyses for traumatic vertebral artery injury (goyal2024asystematicreview pages 1-2)

---

## 2. Etiology

### 2.1 Disease causal factors
**Primary causal substrate in typical VAI/VBI presentations:**
- **Atherosclerotic stenosis/occlusion** of vertebral artery segments (notably ostium/proximal segments) is described as the major mechanism in reviews. (bobmanuel2023vertebralarteryinterventions pages 1-2, bobmanuel2023vertebralarteryinterventions pages 2-3)

**Other causes (less common, but clinically important):**
- **Dissection** (spontaneous or traumatic) (bobmanuel2023vertebralarteryinterventions pages 3-4, amran2024vertebralarterydissection pages 1-2)
- **Trauma-related vertebral artery injury** (TVAI) after cervical spine trauma (goyal2024asystematicreview pages 1-2)
- **Congenital anomalies** including vertebral artery hypoplasia/atresia (bobmanuel2023vertebralarteryinterventions pages 3-4)
- **Extrinsic compression** and **vasculitis** (mentioned as less common causes) (bobmanuel2023vertebralarteryinterventions pages 2-3)

### 2.2 Risk factors
**Atherosclerotic disease risk factors (vascular risk factor paradigm):**
AHA/ASA-aligned medical therapy guidance in vertebral artery disease emphasizes standard vascular risk factor modification (blood pressure management, diabetes control, smoking cessation) and intensive medical therapy for secondary prevention. (bobmanuel2023vertebralarteryinterventions pages 4-5)

**Anatomic/structural risk factors:**
- Vertebral artery hypoplasia reported frequency **2–6%** (autopsy/angiogram), and is noted as associated with symptomatic vertebrobasilar occlusive disease. (bobmanuel2023vertebralarteryinterventions pages 3-4)

**Trauma-related risk factors (for traumatic VAI):**
- In cervical spine trauma, vertebral artery injury is associated with high-risk fracture patterns; evaluation uses modified Denver screening criteria in trauma literature and CTA-based screening. (goyal2024asystematicreview pages 1-2)

### 2.3 Protective factors
No specific protective genetic variants or protective environmental exposures were identified in the retrieved sources.

### 2.4 Gene–environment interactions
Not specifically addressed in the retrieved evidence set.

---

## 3. Phenotypes

### 3.1 Symptom and sign spectrum (with suggested HPO terms)
VAI/VBI phenotypes reflect the affected posterior circulation territory (brainstem, cerebellum, thalamus, occipital cortex, vestibular pathways). (bobmanuel2023vertebralarteryinterventions pages 3-4)

**Common posterior circulation TIA/stroke symptom clusters used in VERiTAS baseline characterization** include:
- “Loss of balance, vertigo, unsteadiness or disequilibrium, diplopia, dysphagia, or dysarthria.” (aminhanjani2015hemodynamicfeaturesof pages 7-10)
- Motor dysfunction (“weakness, paralysis, or clumsiness”) and sensory symptoms (“numbness, or paresthesia”). (aminhanjani2015hemodynamicfeaturesof pages 7-10)
- Homonymous visual field loss. (aminhanjani2015hemodynamicfeaturesof pages 7-10)

**Syndromic localization examples (review-level descriptions):**
- Intracranial vertebral occlusion → lateral medullary (Wallenberg) syndrome with “Horner’s syndrome, dysphagia, hoarse voice, limb ataxia, and decreased pain/ temperature sensation of the ipsilateral face and contralateral body.” (bobmanuel2023vertebralarteryinterventions pages 3-4)
- Basilar artery occlusion → “Locked-In-Syndrome (the patient becomes quadriplegic and mute, but remains conscious)” (bobmanuel2023vertebralarteryinterventions pages 3-4)
- Distal basilar occlusion prodrome: “vertigo, nausea, headache, neck pain, and transient lateralized motor weakness.” (bobmanuel2023vertebralarteryinterventions pages 3-4)

**Vertebral artery dissection (VAD) phenotypes (2024 review):**
- “The most frequent clinical manifestations include stroke, transient ischemic attack, neck pain, headaches, and vertigo.” (amran2024vertebralarterydissection pages 1-2)

**Suggested HPO mappings (non-exhaustive):**
- Vertigo: HP:0002321 (bobmanuel2023vertebralarteryinterventions pages 3-4, amran2024vertebralarterydissection pages 1-2, aminhanjani2015hemodynamicfeaturesof pages 7-10)
- Ataxia / limb ataxia: HP:0001251 (bobmanuel2023vertebralarteryinterventions pages 3-4)
- Dysphagia: HP:0002015 (bobmanuel2023vertebralarteryinterventions pages 3-4, aminhanjani2015hemodynamicfeaturesof pages 7-10)
- Dysarthria: HP:0001260 (aminhanjani2015hemodynamicfeaturesof pages 7-10)
- Diplopia: HP:0000651 (aminhanjani2015hemodynamicfeaturesof pages 7-10)
- Visual field defect (homonymous hemianopia): HP:0000581 (aminhanjani2015hemodynamicfeaturesof pages 7-10)
- Headache: HP:0002315 (bobmanuel2023vertebralarteryinterventions pages 3-4, amran2024vertebralarterydissection pages 1-2)
- Neck pain: HP:0003302 (bobmanuel2023vertebralarteryinterventions pages 3-4, amran2024vertebralarterydissection pages 1-2)
- Horner syndrome: HP:0000009 (bobmanuel2023vertebralarteryinterventions pages 3-4)

### 3.2 Phenotype characteristics and frequency data
**Posterior circulation syndrome distribution in VERiTAS (selected):**
Among symptomatic vertebrobasilar disease patients, “Pontine syndrome” was common (e.g., 59% in basilar-only disease; 23% vertebral-only; 48% combined basilar+vertebral), while “Pure cerebellar” syndromes occurred at ~14–23% across groups. (aminhanjani2015hemodynamicfeaturesof pages 10-15)

**Quality of life impact**
Not directly quantified with standardized QoL instruments (e.g., EQ-5D, PROMIS) in the retrieved sources; however, posterior circulation ischemic events are recognized to be disabling and associated with substantial morbidity/mortality, particularly for basilar occlusion and recurrent events. (zhang2023microsurgicalrevascularizationof pages 1-2, markus2022treatmentofposterior pages 3-4)

---

## 4. Genetic / molecular information

### 4.1 Causal genes and pathogenic variants
**Typical atherosclerotic VAI/VBI:** No monogenic causal genes/variants were identified in the retrieved sources.

**Dissection-associated VAI:** A 2024 VAD review lists “connective tissue disorders” as intrinsic contributors and states “Predisposing factors include connective tissue disorders… and the presence of infection or inflammation,” and later mentions “connective tissue diseases… and elastin insufficiency.” However, **no named hereditary syndromes (e.g., Ehlers–Danlos, Marfan) or specific genes/variants** were provided in the retrieved excerpts. (amran2024vertebralarterydissection pages 1-2, amran2024vertebralarterydissection pages 6-8)

### 4.2 Modifier genes / epigenetics / chromosomal abnormalities
Not addressed in the retrieved evidence set.

---

## 5. Environmental information

### 5.1 Environmental/lifestyle contributors
For typical atherosclerotic vertebrobasilar disease, the key modifiable contributors are the standard vascular risk factors targeted by guideline-based prevention: blood pressure control, diabetes management, smoking cessation, lipid management, and lifestyle interventions. (bobmanuel2023vertebralarteryinterventions pages 4-5, markus2022treatmentofposterior pages 4-5)

### 5.2 Infectious agents
Not established as direct causes in the retrieved sources; infection/inflammation is mentioned only as a predisposing factor context for dissection. (amran2024vertebralarterydissection pages 1-2)

---

## 6. Mechanism / pathophysiology

### 6.1 Causal chain (from trigger to manifestations)
**Atherosclerotic vertebrobasilar disease:**
1) Atherosclerotic plaque/stenosis in vertebral/basilar arteries (often proximal/ostial vertebral artery) (bobmanuel2023vertebralarteryinterventions pages 1-2)
2) Reduced perfusion pressure and/or plaque-related thromboembolism (aminhanjani2010vertebrobasilarflowevaluation pages 1-2)
3) Distal territory hypoperfusion and/or embolic infarction in brainstem/cerebellum/occipital territories, yielding symptoms such as vertigo, ataxia, diplopia, dysarthria, dysphagia, and focal weakness/sensory loss. (aminhanjani2015hemodynamicfeaturesof pages 7-10, bobmanuel2023vertebralarteryinterventions pages 3-4)

**Hemodynamic compromise as an upstream driver of risk:**
The VERiTAS rationale highlights that posterior circulation stroke risk is strongly related to hemodynamic compromise and that this can be measured noninvasively with quantitative MRA. (aminhanjani2010vertebrobasilarflowevaluation pages 1-2)

**Mechanism heterogeneity (hemodynamic vs embolic):**
Infarct-pattern analyses within the VERiTAS cohort describe both hemodynamic and embolic/perforator-related patterns, implying mixed downstream mechanisms even in the same etiologic category. (aminhanjani2010vertebrobasilarflowevaluation pages 1-2)

### 6.2 Suggested GO biological process terms (hypothesis-driven)
Not directly measured in the retrieved evidence set; plausible GO terms for the biological processes involved include:
- GO:0001525 angiogenesis (collateral adaptation context)
- GO:0007596 blood coagulation / GO:0030193 regulation of blood coagulation (thromboembolism)
- GO:0006928 movement of cell or subcellular component (platelet activation/aggregation context)

These are proposed mappings; no direct molecular profiling evidence was retrieved.

### 6.3 Suggested Cell Ontology (CL) terms
Primary implicated cell types (conceptual, not directly profiled in retrieved evidence):
- Endothelial cell (CL:0000115)
- Vascular smooth muscle cell (CL:0000192)
- Platelet (CL:0000233)

---

## 7. Anatomical structures affected

### 7.1 Organ/system level
- **Cardiovascular system / cerebrovascular arterial system**: vertebral arteries and basilar artery (aminhanjani2010vertebrobasilarflowevaluation pages 1-2)
- **Central nervous system**: posterior circulation territories including brainstem, cerebellum, thalamus, occipital cortex (bobmanuel2023vertebralarteryinterventions pages 3-4)

### 7.2 Suggested UBERON terms (examples)
- Vertebral artery: UBERON:0001643
- Basilar artery: UBERON:0001642
- Brainstem: UBERON:0002298
- Cerebellum: UBERON:0002037
- Occipital lobe (visual cortex region): UBERON:0001871

(UBERON IDs provided as standard anatomy mappings; not explicitly enumerated in retrieved texts.)

---

## 8. Temporal development

### 8.1 Onset patterns
- Atherosclerotic VAI/VBI typically presents in older adults (implied by atherosclerotic risk factor management paradigms and interventional cohorts) and can present as TIA or stroke. (bobmanuel2023vertebralarteryinterventions pages 4-5, liu2024applicationofmicrosurgical pages 1-2)
- Vertebral artery dissection is highlighted as a cause of stroke/TIA in younger adults; one review states it “usually occurs at an average age of 46.5 years.” (amran2024vertebralarterydissection pages 1-2)

### 8.2 Progression
Early recurrence risk is emphasized: in medically treated symptomatic vertebrobasilar disease, recurrence is particularly increased in the first weeks and annual stroke rates around 10–15% are repeatedly cited. (bobmanuel2023vertebralarteryinterventions pages 1-2, aminhanjani2010vertebrobasilarflowevaluation pages 1-2)

---

## 9. Inheritance and population

### 9.1 Epidemiology (key statistics)
- Posterior-circulation ischemia due to vertebral artery disease accounts for **~20–25% of ischemic strokes**. (bobmanuel2023vertebralarteryinterventions pages 1-2)
- Symptomatic vertebrobasilar disease recurrence risk averages **10–15% per year**. (bobmanuel2023vertebralarteryinterventions pages 1-2, aminhanjani2010vertebrobasilarflowevaluation pages 1-2)
- Poor prognosis in obstructive vertebrobasilar disease managed medically: **~30% mortality at 2 years** (review-cited). (bobmanuel2023vertebralarteryinterventions pages 1-2)
- Vertebral artery stenosis/occlusion (VASO) “occurs in **5% of the normal population**” (as reported in a 2023 surgical series background). (zhang2023microsurgicalrevascularizationof pages 1-2)
- Vertebral artery hypoplasia frequency **2–6%** (autopsy/angiogram). (bobmanuel2023vertebralarteryinterventions pages 3-4)

**VAD incidence (relevant VAI subtype):**
- VAD contributes “around **1.0–1.1 per 100,000 population**” (review). (amran2024vertebralarterydissection pages 1-2)

### 9.2 Inheritance pattern
Not established as a Mendelian disorder in typical atherosclerotic VAI/VBI. For VAD, connective tissue disease predisposition is discussed without specifying inheritance patterns or genes in retrieved text. (amran2024vertebralarterydissection pages 1-2)

---

## 10. Diagnostics

### 10.1 Imaging-based diagnostic strategy (real-world implementation)
A 2023 review states that **Color duplex ultrasound (DUS)** is used as a “first-line imaging strategy” in suspected vertebrobasilar ischemia and should be followed by **CE-MRA or CTA** before intervention decisions; **DSA** is the gold standard for defining lesions. (bobmanuel2023vertebralarteryinterventions pages 4-5)

### 10.2 Diagnostic performance metrics (selected)
From the same review:
- Duplex criterion PSVr >2.2 for ≥50% proximal stenosis: **96% sensitivity / 89% specificity**. (bobmanuel2023vertebralarteryinterventions pages 3-4)
- CTA/MRA performance: reported sensitivity/specificity around **94–95%**, and **DSA** carries **1–2% stroke risk**. (bobmanuel2023vertebralarteryinterventions pages 3-4)

**Traumatic vertebral artery injury (TVAI):**
- Pooled data: **91.7%** underwent diagnostic CTA; **7.5%** MRA; **3.0%** DSA. (goyal2024asystematicreview pages 1-2)
- One cited trauma study: CTA sensitivity ~**98%**, specificity ~**100%**; MRA sensitivity **47–60%**. (goyal2024asystematicreview pages 5-7)

### 10.3 Hemodynamic assessment
VERiTAS emphasizes quantitative MRA (QMRA) for large-vessel flow measurement and risk stratification; symptom-based “hypoperfusion symptoms” poorly predict low/borderline flow (PPV 37.5%, NPV 65.5%). (aminhanjani2010vertebrobasilarflowevaluation pages 1-2, markus2022treatmentofposterior pages 4-5)

### 10.4 Differential diagnosis
Not systematically enumerated in the retrieved texts; practical differentials for posterior circulation symptoms include cardioembolic stroke, other intracranial stenoses, basilar artery occlusion, vestibular disorders, and nonvascular brainstem/cerebellar pathology.

---

## 11. Outcome / prognosis

### 11.1 Stroke recurrence and mortality
- Annual stroke recurrence risk in symptomatic vertebrobasilar disease: **~10–15% per year** (often cited). (bobmanuel2023vertebralarteryinterventions pages 1-2, aminhanjani2010vertebrobasilarflowevaluation pages 1-2)
- Poor prognosis under medical therapy alone in obstructive vertebrobasilar disease: **~30% mortality at 2 years** (review-cited). (bobmanuel2023vertebralarteryinterventions pages 1-2)

### 11.2 Post-procedural outcomes and complications (selected recent data)
- Vertebrobasilar stenting cohort (VBS n=93): in-stent restenosis **12.9%**; stented-territory infarction **22.6%** over follow-up; diabetes and multiple stents strongly associated with long-term stented-territory infarction. (ryu2023instentrestenosisand pages 2-4, ryu2023instentrestenosisand pages 6-7)
- Microsurgical series report clinical improvement with low perioperative stroke/death in selected cohorts, with cranial nerve complications (Horner’s syndrome, hoarseness) notable. (zhang2023microsurgicalrevascularizationof pages 1-2, liu2024applicationofmicrosurgical pages 1-2)

---

## 12. Treatment

### 12.1 Medical therapy (secondary prevention emphasis)
A 2023 review summarizes guideline-oriented management including risk factor modification and therapies such as antiplatelet and statins, with BP goals in that text of <140/90 mmHg (and diastolic <85 mmHg in diabetes). (bobmanuel2023vertebralarteryinterventions pages 4-5)

For posterior circulation stroke/TIA, a secondary-prevention review notes:
- Short-term **dual antiplatelet therapy** after high-risk minor stroke/TIA is recommended by guidelines, with benefit mainly in the first ~3 weeks, then transition to monotherapy. (markus2022treatmentofposterior pages 4-5)

### 12.2 Acute reperfusion therapy (posterior circulation stroke)
- IV thrombolysis appears to have similar benefit to anterior circulation and lower hemorrhage risk (meta-analysis estimates provided in review). (markus2022treatmentofposterior pages 2-3)
- Mechanical thrombectomy has RCT-supported benefit for **basilar artery occlusion**, e.g., mRS 0–3 at 90 days **46% vs 22.8%** in one RCT and **46.4% vs 24.3%** in another. (markus2022treatmentofposterior pages 3-4)

### 12.3 Endovascular intervention for vertebral stenosis
Evidence remains mixed, with uncertainty about superiority over optimal medical therapy:
- VAST: 30-day composite **5%** (stent) vs **2%** (OMT); 1-year territory stroke **9%** vs **7%**. (bobmanuel2023vertebralarteryinterventions pages 7-8)
- VIST: stroke in **5** stent vs **12** medical; HR 0.40 (95% CI 0.14–1.13; p=0.08). (bobmanuel2023vertebralarteryinterventions pages 7-8)

**Restenosis statistics:** reported wide range **0–43%** across studies; BMS 11–43%; meta-analysis cited DES **8.2%** vs BMS **23.7%** restenosis. (bobmanuel2023vertebralarteryinterventions pages 7-8, bobmanuel2023vertebralarteryinterventions pages 5-6)

### 12.4 Microsurgical / hybrid revascularization
Recent real-world data suggest microsurgical reconstruction is used when endovascular options are unsuitable or in restenosis:
- Liu 2024 (n=34): postoperative arteries patent; no new in-hospital TIAs/events; mRS improved for 30 patients with all postoperative mRS <1; mean follow-up 10 months; one permanent Horner syndrome and one death from septic shock. (liu2024applicationofmicrosurgical pages 1-2)
- Zhang 2023 (n=29): no perioperative stroke or death; mean follow-up 28.4 months; cranial nerve complications common; no target vessel restenosis reported. (zhang2023microsurgicalrevascularizationof pages 1-2, zhang2023microsurgicalrevascularizationof pages 4-5)

### 12.5 Relevant clinical trials (current applications)
- **NCT05885932**: Drug-eluting stenting vs medical treatment for extracranial vertebral artery stenosis; recruiting; planned n=472. (bobmanuel2023vertebralarteryinterventions pages 7-8)
- **NCT03201432**: Drug-eluting vs bare metal stents in symptomatic extracranial vertebral artery stenosis; completed; n=160. (bobmanuel2023vertebralarteryinterventions pages 7-8)

### 12.6 MAXO (Medical Action Ontology) term suggestions (examples)
(Provided as mappings; MAXO IDs not retrievable from the current evidence set.)
- Antiplatelet therapy; dual antiplatelet therapy (markus2022treatmentofposterior pages 4-5)
- Statin therapy / lipid-lowering therapy (bobmanuel2023vertebralarteryinterventions pages 4-5)
- Blood pressure management (bobmanuel2023vertebralarteryinterventions pages 4-5)
- CT angiography; MR angiography; digital subtraction angiography (bobmanuel2023vertebralarteryinterventions pages 3-4)
- Endovascular stent placement (vertebral artery) (bobmanuel2023vertebralarteryinterventions pages 7-8)
- Vertebral endarterectomy; artery transposition; bypass grafting (liu2024applicationofmicrosurgical pages 2-4)

---

## 13. Prevention

### 13.1 Primary prevention
A 2024 AHA/ASA primary prevention guideline explicitly states that for **asymptomatic vertebral artery stenosis** there are limited large-scale data and thus the guideline “cannot develop comprehensive, evidence-based recommendations,” focusing instead on asymptomatic carotid stenosis. This implies prevention is largely through general cardiovascular risk reduction rather than vertebral-specific screening/revascularization strategies. (bushnell20242024guidelinefor pages 25-26)

### 13.2 Secondary/tertiary prevention
Secondary prevention is centered on aggressive vascular risk factor treatment and antiplatelet therapy, with consideration of short-term DAPT after minor stroke/TIA. (markus2022treatmentofposterior pages 4-5, bobmanuel2023vertebralarteryinterventions pages 4-5)

---

## 14. Other species / natural disease
No evidence in the retrieved sources about naturally occurring vertebral artery insufficiency as a comparable veterinary disease entity.

---

## 15. Model organisms
No model organism or experimental induced model evidence was identified in the retrieved sources.

---

## Recent developments and expert analysis (prioritizing 2023–2024)

1) **Shift toward quantifying risk beyond symptoms:** VERiTAS-related work emphasizes that symptom patterns alone may not reliably identify hemodynamic compromise; quantitative flow imaging is more directly linked to risk stratification. (aminhanjani2010vertebrobasilarflowevaluation pages 1-2, markus2022treatmentofposterior pages 4-5)

2) **Interventional practice remains active but evidence-limited:** Contemporary reviews characterize vertebral artery stenting as widely used with good technical success yet without definitive RCT proof of superiority over optimal medical therapy, especially for intracranial disease where peri-procedural risk is higher. (bobmanuel2023vertebralarteryinterventions pages 7-8, markus2022treatmentofposterior pages 5-8)

3) **Real-world microsurgical revival in select niches (2023–2024):** Single-center series report feasibility of vertebral endarterectomy/transposition/bypass in patients unsuited for endovascular therapy or with restenosis, with improved functional outcomes in selected cohorts but cranial nerve morbidity remains salient. (liu2024applicationofmicrosurgical pages 1-2, zhang2023microsurgicalrevascularizationof pages 4-5)

4) **Device technology and restenosis surveillance:** Observational data quantify clinically important rates of stented-territory infarction after vertebrobasilar stenting and identify predictors (e.g., diabetes, multiple stents, clopidogrel resistance). This supports individualized follow-up and antiplatelet optimization strategies in practice. (ryu2023instentrestenosisand pages 2-4, ryu2023instentrestenosisand pages 6-7)

---

## Key abstract quotes (verbatim excerpts)

- Bob-Manuel 2023 (Current Cardiology Reviews; 2023-01; https://doi.org/10.2174/1573403x18666220317093131): “Patients with posterior circulation ischemia due to vertebral artery stenosis account for 20 to 25% of ischemic strokes…” and “with an annual stroke rate of 10 to 15%.” (bobmanuel2023vertebralarteryinterventions pages 1-2)

- Amin-Hanjani 2010 VERiTAS rationale (International Journal of Stroke; 2010-12; https://doi.org/10.1111/j.1747-4949.2010.00528.x): symptomatic vertebrobasilar disease carries a high recurrent stroke risk “averaging 10–15% per year.” (aminhanjani2010vertebrobasilarflowevaluation pages 1-2)

- Bushnell 2024 AHA/ASA Primary Prevention of Stroke guideline (Stroke; 2024-12; https://doi.org/10.1161/str.0000000000000475): limited large-scale data for asymptomatic vertebral stenosis—authors “cannot develop comprehensive, evidence-based recommendations.” (bushnell20242024guidelinefor pages 25-26)

- Goyal 2024 traumatic vertebral artery injury meta-analysis (Global Spine Journal; 2024-11; https://doi.org/10.1177/21925682231209631): pooled VAI incidence “.95% (95% CI 0.65-1.29)” and posterior stroke risk “8.87% (95% CI 5.34- 12.99).” (goyal2024asystematicreview pages 1-2)

---

## Evidence map table
The following table consolidates the key quantitative findings, diagnostic metrics, mechanistic framing, and treatment evidence, including active clinical trials.

| Domain | Key findings | Evidence type | Citations |
|---|---|---|---|
| Definitions / nomenclature | **Vertebral artery insufficiency (VAI)** is best understood as symptomatic posterior-circulation ischemia caused by reduced flow or embolic complications from vertebral artery pathology; in practice literature often uses **vertebrobasilar insufficiency (VBI)**, **vertebrobasilar disease (VBD)**, **vertebral artery stenosis/occlusion (VAS/VASO)**, and **posterior circulation ischemia** with partial overlap. Reviews commonly discuss VAI/VBI under the broader umbrella of symptomatic vertebral or vertebrobasilar atherosclerotic disease rather than as a distinct monogenic disease entity. | Narrative review, prospective study rationale | (bobmanuel2023vertebralarteryinterventions pages 1-2, aminhanjani2010vertebrobasilarflowevaluation pages 1-2, bobmanuel2023vertebralarteryinterventions pages 2-3) |
| Epidemiology / prognosis | Posterior-circulation ischemia due to vertebral artery disease accounts for about **20–25% of ischemic strokes**; one review notes posterior-circulation strokes comprise about **one-fifth** of all strokes, while VERiTAS background cites **up to 30–40%** of ischemic strokes in the posterior circulation. Symptomatic vertebrobasilar disease has high early recurrence; medically treated patients have an **annual stroke rate of 10–15%**, with particularly high risk in the first weeks. Obstructive vertebrobasilar disease managed medically has about **30% mortality at 2 years**. In one secondary-prevention review, **90-day recurrent stroke** was **33%** for basilar/intracranial vertebral stenosis versus **16%** for extracranial vertebral stenosis. | Review, prospective cohort/rationale | (bobmanuel2023vertebralarteryinterventions pages 1-2, aminhanjani2010vertebrobasilarflowevaluation pages 1-2, markus2022treatmentofposterior pages 4-5) |
| Major mechanisms / pathophysiology | Major etiologies include **atherosclerotic stenosis/occlusion** (dominant mechanism), with less common causes including **dissection**, **trauma**, **congenital anomalies/hypoplasia**, **extrinsic compression**, and **vasculitis**. Stroke mechanism is heterogeneous: VERiTAS-related work supports **hemodynamic compromise** as a strong predictor of future stroke, but infarct-pattern analysis shows both **hemodynamic** and **embolic / perforator-plaque** mechanisms occur. Traumatic vertebral artery injury/dissection is a separate but clinically relevant VAI mechanism, especially after cervical trauma. | Review, observational cohort, systematic review/meta-analysis | (aminhanjani2010vertebrobasilarflowevaluation pages 1-2, goyal2024asystematicreview pages 5-7, goyal2024asystematicreview pages 1-2, bobmanuel2023vertebralarteryinterventions pages 2-3) |
| Hemodynamic risk stratification | In symptomatic vertebrobasilar disease, **quantitative MRA (QMRA)**-measured distal flow is more informative than symptom pattern alone. VERiTAS analyses found flow compromise robustly predicts subsequent stroke risk; by contrast, “hypoperfusion symptoms” alone had poor predictive value (**PPV 37.5%, NPV 65.5%**) for low/borderline flow and were not associated with stroke outcome. | Prospective observational study / post hoc analysis | (aminhanjani2010vertebrobasilarflowevaluation pages 1-2, markus2022treatmentofposterior pages 4-5) |
| Diagnostics: DUS / ultrasound | **Color duplex ultrasound (DUS)** is commonly recommended as **first-line** screening in suspected vertebrobasilar ischemia, but positive studies usually require confirmatory **CTA or CE-MRA** before intervention decisions. Reported duplex criteria for proximal stenosis include **PSVr >2.2** for ≥50% stenosis with **96% sensitivity / 89% specificity**; other thresholds reported include **PSV >108 cm/s**, **EDV >36 cm/s**, **EDVr >1.7**. DUS has lower overall sensitivity than CTA/MRA but good specificity. | Review / guideline-summary review | (bobmanuel2023vertebralarteryinterventions pages 4-5, bobmanuel2023vertebralarteryinterventions pages 3-4) |
| Diagnostics: CTA / MRA / DSA | **CTA** and **CE-MRA/MRA** are the main confirmatory noninvasive tests; review data cite sensitivity/specificity around **94–95%**, with CE-MRA sometimes slightly outperforming CTA. **DSA** remains the gold standard for lesion definition but is invasive and carries a **1–2% stroke risk**. In traumatic vertebral artery injury, CTA is the preferred acute screening test; pooled trauma data showed **91.7% CTA**, **7.5% MRA**, **3.0% DSA**, and one cited study reported CTA sensitivity near **98%** and specificity near **100%**, while MRA sensitivity was lower (**47–60%**). | Review, systematic review/meta-analysis | (bobmanuel2023vertebralarteryinterventions pages 4-5, bobmanuel2023vertebralarteryinterventions pages 3-4, goyal2024asystematicreview pages 5-7, goyal2024asystematicreview pages 1-2) |
| Medical treatment / prevention | Guideline-concordant therapy centers on **aggressive vascular risk-factor control**: antiplatelet therapy, statin therapy, BP control, diabetes management, smoking cessation, and lifestyle modification. AHA/ASA-aligned review text cites BP goal **<140/90 mmHg** (diastolic **<85 mmHg** in diabetes). For posterior-circulation minor stroke/TIA, reviews support **short-term DAPT** (aspirin + clopidogrel, or aspirin + ticagrelor in guideline frameworks) for the early high-risk period, with benefit concentrated in approximately the **first 3 weeks**, then transition to single antiplatelet therapy. For asymptomatic vertebral stenosis, high-quality evidence is limited; the 2024 primary-prevention guideline notes insufficient data to make comprehensive evidence-based recommendations specific to asymptomatic vertebral artery stenosis. | Review, guideline, trial-informed secondary-prevention review | (bobmanuel2023vertebralarteryinterventions pages 4-5, markus2022treatmentofposterior pages 4-5, bushnell20242024guidelinefor pages 25-26) |
| Acute posterior-circulation stroke care relevant to VAI/VBI | For posterior-circulation stroke broadly, **IV thrombolysis** appears at least as effective as for anterior circulation and may have lower symptomatic ICH risk; **mechanical thrombectomy** now has convincing benefit for **basilar artery occlusion** (e.g., 90-day mRS 0–3 in **46% vs 22.8%** in ATTENTION-like data, and **46.4% vs 24.3%** in BAOCHE-like data). Evidence remains sparse for isolated vertebral artery occlusions. | Review of RCTs/observational studies | (markus2022treatmentofposterior pages 1-2, markus2022treatmentofposterior pages 2-3, markus2022treatmentofposterior pages 3-4) |
| Stenting vs medical therapy: overall interpretation | Endovascular angioplasty/stenting is technically feasible and widely used, but superiority over best medical therapy remains unproven. Reviews note vertebral revascularization may be considered for **symptomatic extracranial lesions ≥50%** with recurrent ischemia despite optimal medical therapy (ESC Class IIb wording in review summary), while **intracranial vertebral/basilar stenosis** is generally better managed medically because peri-procedural risk is higher. | Review / guideline-summary review / RCT synthesis | (bobmanuel2023vertebralarteryinterventions pages 4-5, markus2022treatmentofposterior pages 1-2, markus2022treatmentofposterior pages 5-8) |
| Vertebral stenting trial data | **VAST**: 30-day composite outcome **5% (3/57)** in stenting vs **2% (1/58)** in optimal medical therapy; 1-year vertebrobasilar-territory stroke **9%** vs **7%**. **VIST**: strokes in **5** stented vs **12** medical patients; HR **0.40 (95% CI 0.14–1.13; p=0.08)**, suggesting possible but unproven benefit, especially extracranially. For intracranial stenosis generally, **SAMMPRIS** showed 30-day stroke/death **14.7%** with stenting vs **5.8%** with medical therapy; basilar stenosis had particularly high peri-procedural risk (**20.8%** vs **6.7%** in other arteries). | RCTs summarized in reviews | (bobmanuel2023vertebralarteryinterventions pages 7-8, markus2022treatmentofposterior pages 5-8) |
| Restenosis / post-stent outcomes | Reported vertebral in-stent restenosis varies widely: **0–43%** across studies; early bare-metal stent series reported **11–43%** restenosis, while a meta-analysis cited **8.2%** restenosis with drug-eluting stents vs **23.7%** with bare-metal stents. In a 2023 vertebrobasilar-stenting cohort (n=93 VBS), in-stent restenosis was **12.9%**, with cumulative rates **10.4%, 15.7%, 18.1%** at 12/24/36 months; stented-territory infarction was **22.6%** overall, higher than carotid stenting. Predictors included higher **HbA1c**, **clopidogrel resistance / low platelet inhibition**, **diabetes**, and use of **≥2 stents**. | Review, retrospective observational cohort | (ryu2023instentrestenosisand pages 4-6, ryu2023instentrestenosisand pages 2-4, ryu2023instentrestenosisand pages 1-2, bobmanuel2023vertebralarteryinterventions pages 7-8, bobmanuel2023vertebralarteryinterventions pages 5-6) |
| Microsurgical / hybrid real-world implementations | **Zhang 2023**: 29 symptomatic proximal vertebral lesions; techniques included endarterectomy, transposition, hybrid endarterectomy+stent; **no perioperative stroke or death**, mean follow-up **28.4 months**, most improved clinically, no anastomotic stenosis on follow-up imaging. **Liu 2024**: 34 patients unsuitable for endovascular treatment; pre-op CTA/CTP/MRA, post-op vessels patent, **30/34** improved mRS with all postoperative mRS **<1**, mean follow-up **10 months**; one death from septic shock unrelated to cerebrovascular event, one residual moderate restenosis, six temporary complications, one permanent Horner syndrome. These series support surgery as a niche option for refractory anatomy, restenosis, or endovascular-unsuitable disease. | Single-center retrospective observational series | (zhang2023microsurgicalrevascularizationof pages 4-5, zhang2023microsurgicalrevascularizationof pages 2-4, zhang2023microsurgicalrevascularizationof pages 5-6, liu2024applicationofmicrosurgical pages 1-2, liu2024applicationofmicrosurgical pages 2-4, zhang2023microsurgicalrevascularizationof pages 1-2, liu2024applicationofmicrosurgical pages 4-6) |
| Traumatic/dissection-associated vertebral insufficiency | In cervical trauma, pooled incidence of vertebral artery injury was **0.95% (95% CI 0.65–1.29)** and pooled posterior stroke risk among VAI cases was **8.87% (95% CI 5.34–12.99)**. Most were evaluated with CTA, and management varied across conservative care, antiplatelets, anticoagulation, combined therapy, and surgical/endovascular intervention. This is a clinically important VAI subtype but distinct from chronic atherosclerotic VBI. | Systematic review/meta-analysis | (goyal2024asystematicreview pages 5-7, goyal2024asystematicreview pages 1-2) |
| Real-world trials / implementations | **NCT05885932**: recruiting randomized trial, **Drug-eluting Stenting Versus Medical Treatment for Extracranial Vertebral Artery Stenosis**, planned **n=472**. **NCT03201432**: completed phase 2/3 trial comparing **drug-eluting vs bare-metal stents** for symptomatic extracranial vertebral stenosis, **n=160**. Additional antiplatelet optimization after cerebrovascular stenting: **NCT06301776** (post-BRIDGE dual antiplatelet/ticagrelor strategy, recruiting, **n=560**). These trials show ongoing real-world implementation emphasis on extracranial vertebral stenting technology and post-stent antiplatelet regimens rather than established routine use. | Registered interventional clinical trials | (bobmanuel2023vertebralarteryinterventions pages 7-8) |


*Table: This table condenses definitions, mechanisms, diagnostics, prognosis, treatments, and active implementation examples for vertebral artery insufficiency / vertebrobasilar insufficiency. It is designed as a compact evidence map for rapid use in a disease knowledge base.*

References

1. (bobmanuel2023vertebralarteryinterventions pages 1-2): Tamunoinemi Bob-Manuel, Oscar Maitas, Justin Price, Abdullah Noor, Koyenum Obi, Nelson Okoh, Kiran Garikapati, Jeong Kim, Sanjida Jahan, and James S. Jenkins. Vertebral artery interventions: a comprehensive updated review. Current Cardiology Reviews, Jan 2023. URL: https://doi.org/10.2174/1573403x18666220317093131, doi:10.2174/1573403x18666220317093131. This article has 21 citations.

2. (aminhanjani2010vertebrobasilarflowevaluation pages 1-2): Sepideh Amin-Hanjani, Linda Rose-Finnell, DeJuran Richardson, Sean Ruland, Dilip Pandey, Keith R. Thulborn, David S. Liebeskind, Gregory J. Zipfel, Mitchell S. V. Elkind, Jeffrey Kramer, Frank L. Silver, Scott E. Kasner, Louis R. Caplan, Colin P. Derdeyn, Philip B. Gorelick, and Fady T. Charbel. Vertebrobasilar flow evaluation and risk of transient ischaemic attack and stroke study (veritas): rationale and design. International Journal of Stroke, 5:499-505, Dec 2010. URL: https://doi.org/10.1111/j.1747-4949.2010.00528.x, doi:10.1111/j.1747-4949.2010.00528.x. This article has 59 citations and is from a peer-reviewed journal.

3. (bobmanuel2023vertebralarteryinterventions pages 4-5): Tamunoinemi Bob-Manuel, Oscar Maitas, Justin Price, Abdullah Noor, Koyenum Obi, Nelson Okoh, Kiran Garikapati, Jeong Kim, Sanjida Jahan, and James S. Jenkins. Vertebral artery interventions: a comprehensive updated review. Current Cardiology Reviews, Jan 2023. URL: https://doi.org/10.2174/1573403x18666220317093131, doi:10.2174/1573403x18666220317093131. This article has 21 citations.

4. (bobmanuel2023vertebralarteryinterventions pages 2-3): Tamunoinemi Bob-Manuel, Oscar Maitas, Justin Price, Abdullah Noor, Koyenum Obi, Nelson Okoh, Kiran Garikapati, Jeong Kim, Sanjida Jahan, and James S. Jenkins. Vertebral artery interventions: a comprehensive updated review. Current Cardiology Reviews, Jan 2023. URL: https://doi.org/10.2174/1573403x18666220317093131, doi:10.2174/1573403x18666220317093131. This article has 21 citations.

5. (bobmanuel2023vertebralarteryinterventions pages 3-4): Tamunoinemi Bob-Manuel, Oscar Maitas, Justin Price, Abdullah Noor, Koyenum Obi, Nelson Okoh, Kiran Garikapati, Jeong Kim, Sanjida Jahan, and James S. Jenkins. Vertebral artery interventions: a comprehensive updated review. Current Cardiology Reviews, Jan 2023. URL: https://doi.org/10.2174/1573403x18666220317093131, doi:10.2174/1573403x18666220317093131. This article has 21 citations.

6. (zhang2023microsurgicalrevascularizationof pages 1-2): Tongfu Zhang, Donglin Zhou, Yangyang Xu, Maogui Li, Jianfeng Zhuang, Hai Wang, Weiying Zhong, Chao Chen, Hong Kuang, Donghai Wang, and Yunyan Wang. Microsurgical revascularization of a symptomatic proximal vertebral artery: pilot experiences from a single center. Frontiers in Neurology, Jul 2023. URL: https://doi.org/10.3389/fneur.2023.1202565, doi:10.3389/fneur.2023.1202565. This article has 3 citations and is from a peer-reviewed journal.

7. (markus2022treatmentofposterior pages 1-2): Hugh S Markus and Patrik Michel. Treatment of posterior circulation stroke: acute management and secondary prevention. International Journal of Stroke, 17:723-732, Jun 2022. URL: https://doi.org/10.1177/17474930221107500, doi:10.1177/17474930221107500. This article has 95 citations and is from a peer-reviewed journal.

8. (bushnell20242024guidelinefor pages 25-26): Cheryl Bushnell, Walter N. Kernan, Anjail Z. Sharrief, Seemant Chaturvedi, John W. Cole, William K. Cornwell, Christine Cosby-Gaither, Sarah Doyle, Larry B. Goldstein, Olive Lennon, Deborah A. Levine, Mary Love, Eliza Miller, Mai Nguyen-Huynh, Jennifer Rasmussen-Winkler, Kathryn M. Rexrode, Nicole Rosendale, Satyam Sarma, Daichi Shimbo, Alexis N. Simpkins, Erica S. Spatz, Lisa R. Sun, Vin Tangpricha, Dawn Turnage, Gabriela Velazquez, and Paul K. Whelton. 2024 guideline for the primary prevention of stroke: a guideline from the american heart association/american stroke association. Stroke, Dec 2024. URL: https://doi.org/10.1161/str.0000000000000475, doi:10.1161/str.0000000000000475. This article has 333 citations and is from a highest quality peer-reviewed journal.

9. (ryu2023instentrestenosisand pages 2-4): Jae-Chan Ryu, Jae-Han Bae, Sang Hee Ha, Boseong Kwon, Yunsun Song, Deok Hee Lee, Jun Young Chang, Dong-Wha Kang, Sun U. Kwon, Jong S. Kim, and Bum Joon Kim. In-stent restenosis and stented-territory infarction after carotid and vertebrobasilar artery stenting. BMC Neurology, Feb 2023. URL: https://doi.org/10.1186/s12883-023-03110-z, doi:10.1186/s12883-023-03110-z. This article has 11 citations and is from a peer-reviewed journal.

10. (liu2024applicationofmicrosurgical pages 1-2): Mingyuan Liu, Peiguang Yan, Mingxin Wang, Jia Guo, Wei Liu, Ganchun Wu, Lufei Wang, Jingjing Liu, and Li Li. Application of microsurgical surgery in patients with proximal vertebral artery stenosis unsuited for endovascular treatment: a single-center retrospective study. Neurosurgical Review, Dec 2024. URL: https://doi.org/10.1007/s10143-024-03153-x, doi:10.1007/s10143-024-03153-x. This article has 1 citations and is from a peer-reviewed journal.

11. (goyal2024asystematicreview pages 1-2): Kartik Goyal, Jesvin T. Sunny, Conor S. Gillespie, Martin Wilby, Simon R. Clark, Radek Kaiser, Michael G. Fehlings, and Nisaharan Srikandarajah. A systematic review and meta-analysis of vertebral artery injury after cervical spine trauma. Global Spine Journal, 14:1356-1368, Nov 2024. URL: https://doi.org/10.1177/21925682231209631, doi:10.1177/21925682231209631. This article has 21 citations and is from a peer-reviewed journal.

12. (amran2024vertebralarterydissection pages 1-2): Muhammad Yunus Amran, Irbab Hawari, Fitri Jafani La’biran, Siti Giranti Ardilia Gunadi, and Lisa Tenriesa Muslich. Vertebral artery dissection from etiopathogenesis to management therapy: a narrative review with neuroimaging’s case illustration. The Egyptian Journal of Neurology, Psychiatry and Neurosurgery, Sep 2024. URL: https://doi.org/10.1186/s41983-024-00893-x, doi:10.1186/s41983-024-00893-x. This article has 6 citations.

13. (aminhanjani2015hemodynamicfeaturesof pages 7-10): Sepideh Amin-Hanjani, Xinjian Du, Linda Rose-Finnell, Dilip K. Pandey, DeJuran Richardson, Keith R. Thulborn, Mitchell S.V. Elkind, Gregory J. Zipfel, David S. Liebeskind, Frank L. Silver, Scott E. Kasner, Victor A. Aletich, Louis R. Caplan, Colin P. Derdeyn, Philip B. Gorelick, Fady T. Charbel, Hui Xie, Michael P. Flannery, Hagai Ganin, Sean Ruland, Rebecca Grysiewicz, Aslam Khaja, Laura Pedelty, Fernando Testai, Archie Ong, Noam Epstein, Hurmina Muqtadar, Karriem Watson, Nada Mlinarevich, Maureen Hillmann, Joy Hirsch, Stephen Dashnaw, Philip M. Meyers, Josh Z. Willey, Edwina McNeill-Simaan, Veronica Perez, Alberto Canaan, Wayna Paulino-Hernandez, Katie Vo, Glenn Foster, Andria Ford, Abdullah Nassief, Abbie Bradley, Jannie Serna-Northway, Kristi Kraus, Lina Shiwani, Nancy Hantler, Jeffrey Alger, Sergio Godinez, Jeffrey L. Saver, Latisha Ali, Doojin Kim, Matthew Tenser, Michael Froehler, Radoslav Raychev, Sarah Song, Bruce Ovbiagele, Hermelinda Abcede, Peter Adamczyk, Neal Rao, Anil Yallapragada, Royya Modir, Jason Hinman, Aaron Tansy, Mateo Calderon-Arnulphi, Sunil Sheth, Alireza Noorian, Kwan Ng, Conrad Liang, Jignesh Gadhia, Hannah Smith, Gilda Avila, Johanna Avelar, David Mikulis, Jorn Fierstra, Eugen Hlasny, Leanne K. Casaubon, Mervyn Vergouwen, J.C. Martin del Campo, Cheryl S. Jaigobin, Cherissa Astorga, Libby Kalman, Jeffrey Kramer, Susan Vaughan, Laura Owens, Brett Kissela, Tanya N. Turan, Tom P. Jacobs, and Scott Janis. Hemodynamic features of symptomatic vertebrobasilar disease. Stroke, 46:1850–1856, Jul 2015. URL: https://doi.org/10.1161/strokeaha.115.009215, doi:10.1161/strokeaha.115.009215. This article has 66 citations and is from a highest quality peer-reviewed journal.

14. (aminhanjani2015hemodynamicfeaturesof pages 10-15): Sepideh Amin-Hanjani, Xinjian Du, Linda Rose-Finnell, Dilip K. Pandey, DeJuran Richardson, Keith R. Thulborn, Mitchell S.V. Elkind, Gregory J. Zipfel, David S. Liebeskind, Frank L. Silver, Scott E. Kasner, Victor A. Aletich, Louis R. Caplan, Colin P. Derdeyn, Philip B. Gorelick, Fady T. Charbel, Hui Xie, Michael P. Flannery, Hagai Ganin, Sean Ruland, Rebecca Grysiewicz, Aslam Khaja, Laura Pedelty, Fernando Testai, Archie Ong, Noam Epstein, Hurmina Muqtadar, Karriem Watson, Nada Mlinarevich, Maureen Hillmann, Joy Hirsch, Stephen Dashnaw, Philip M. Meyers, Josh Z. Willey, Edwina McNeill-Simaan, Veronica Perez, Alberto Canaan, Wayna Paulino-Hernandez, Katie Vo, Glenn Foster, Andria Ford, Abdullah Nassief, Abbie Bradley, Jannie Serna-Northway, Kristi Kraus, Lina Shiwani, Nancy Hantler, Jeffrey Alger, Sergio Godinez, Jeffrey L. Saver, Latisha Ali, Doojin Kim, Matthew Tenser, Michael Froehler, Radoslav Raychev, Sarah Song, Bruce Ovbiagele, Hermelinda Abcede, Peter Adamczyk, Neal Rao, Anil Yallapragada, Royya Modir, Jason Hinman, Aaron Tansy, Mateo Calderon-Arnulphi, Sunil Sheth, Alireza Noorian, Kwan Ng, Conrad Liang, Jignesh Gadhia, Hannah Smith, Gilda Avila, Johanna Avelar, David Mikulis, Jorn Fierstra, Eugen Hlasny, Leanne K. Casaubon, Mervyn Vergouwen, J.C. Martin del Campo, Cheryl S. Jaigobin, Cherissa Astorga, Libby Kalman, Jeffrey Kramer, Susan Vaughan, Laura Owens, Brett Kissela, Tanya N. Turan, Tom P. Jacobs, and Scott Janis. Hemodynamic features of symptomatic vertebrobasilar disease. Stroke, 46:1850–1856, Jul 2015. URL: https://doi.org/10.1161/strokeaha.115.009215, doi:10.1161/strokeaha.115.009215. This article has 66 citations and is from a highest quality peer-reviewed journal.

15. (markus2022treatmentofposterior pages 3-4): Hugh S Markus and Patrik Michel. Treatment of posterior circulation stroke: acute management and secondary prevention. International Journal of Stroke, 17:723-732, Jun 2022. URL: https://doi.org/10.1177/17474930221107500, doi:10.1177/17474930221107500. This article has 95 citations and is from a peer-reviewed journal.

16. (amran2024vertebralarterydissection pages 6-8): Muhammad Yunus Amran, Irbab Hawari, Fitri Jafani La’biran, Siti Giranti Ardilia Gunadi, and Lisa Tenriesa Muslich. Vertebral artery dissection from etiopathogenesis to management therapy: a narrative review with neuroimaging’s case illustration. The Egyptian Journal of Neurology, Psychiatry and Neurosurgery, Sep 2024. URL: https://doi.org/10.1186/s41983-024-00893-x, doi:10.1186/s41983-024-00893-x. This article has 6 citations.

17. (markus2022treatmentofposterior pages 4-5): Hugh S Markus and Patrik Michel. Treatment of posterior circulation stroke: acute management and secondary prevention. International Journal of Stroke, 17:723-732, Jun 2022. URL: https://doi.org/10.1177/17474930221107500, doi:10.1177/17474930221107500. This article has 95 citations and is from a peer-reviewed journal.

18. (goyal2024asystematicreview pages 5-7): Kartik Goyal, Jesvin T. Sunny, Conor S. Gillespie, Martin Wilby, Simon R. Clark, Radek Kaiser, Michael G. Fehlings, and Nisaharan Srikandarajah. A systematic review and meta-analysis of vertebral artery injury after cervical spine trauma. Global Spine Journal, 14:1356-1368, Nov 2024. URL: https://doi.org/10.1177/21925682231209631, doi:10.1177/21925682231209631. This article has 21 citations and is from a peer-reviewed journal.

19. (ryu2023instentrestenosisand pages 6-7): Jae-Chan Ryu, Jae-Han Bae, Sang Hee Ha, Boseong Kwon, Yunsun Song, Deok Hee Lee, Jun Young Chang, Dong-Wha Kang, Sun U. Kwon, Jong S. Kim, and Bum Joon Kim. In-stent restenosis and stented-territory infarction after carotid and vertebrobasilar artery stenting. BMC Neurology, Feb 2023. URL: https://doi.org/10.1186/s12883-023-03110-z, doi:10.1186/s12883-023-03110-z. This article has 11 citations and is from a peer-reviewed journal.

20. (markus2022treatmentofposterior pages 2-3): Hugh S Markus and Patrik Michel. Treatment of posterior circulation stroke: acute management and secondary prevention. International Journal of Stroke, 17:723-732, Jun 2022. URL: https://doi.org/10.1177/17474930221107500, doi:10.1177/17474930221107500. This article has 95 citations and is from a peer-reviewed journal.

21. (bobmanuel2023vertebralarteryinterventions pages 7-8): Tamunoinemi Bob-Manuel, Oscar Maitas, Justin Price, Abdullah Noor, Koyenum Obi, Nelson Okoh, Kiran Garikapati, Jeong Kim, Sanjida Jahan, and James S. Jenkins. Vertebral artery interventions: a comprehensive updated review. Current Cardiology Reviews, Jan 2023. URL: https://doi.org/10.2174/1573403x18666220317093131, doi:10.2174/1573403x18666220317093131. This article has 21 citations.

22. (bobmanuel2023vertebralarteryinterventions pages 5-6): Tamunoinemi Bob-Manuel, Oscar Maitas, Justin Price, Abdullah Noor, Koyenum Obi, Nelson Okoh, Kiran Garikapati, Jeong Kim, Sanjida Jahan, and James S. Jenkins. Vertebral artery interventions: a comprehensive updated review. Current Cardiology Reviews, Jan 2023. URL: https://doi.org/10.2174/1573403x18666220317093131, doi:10.2174/1573403x18666220317093131. This article has 21 citations.

23. (zhang2023microsurgicalrevascularizationof pages 4-5): Tongfu Zhang, Donglin Zhou, Yangyang Xu, Maogui Li, Jianfeng Zhuang, Hai Wang, Weiying Zhong, Chao Chen, Hong Kuang, Donghai Wang, and Yunyan Wang. Microsurgical revascularization of a symptomatic proximal vertebral artery: pilot experiences from a single center. Frontiers in Neurology, Jul 2023. URL: https://doi.org/10.3389/fneur.2023.1202565, doi:10.3389/fneur.2023.1202565. This article has 3 citations and is from a peer-reviewed journal.

24. (liu2024applicationofmicrosurgical pages 2-4): Mingyuan Liu, Peiguang Yan, Mingxin Wang, Jia Guo, Wei Liu, Ganchun Wu, Lufei Wang, Jingjing Liu, and Li Li. Application of microsurgical surgery in patients with proximal vertebral artery stenosis unsuited for endovascular treatment: a single-center retrospective study. Neurosurgical Review, Dec 2024. URL: https://doi.org/10.1007/s10143-024-03153-x, doi:10.1007/s10143-024-03153-x. This article has 1 citations and is from a peer-reviewed journal.

25. (markus2022treatmentofposterior pages 5-8): Hugh S Markus and Patrik Michel. Treatment of posterior circulation stroke: acute management and secondary prevention. International Journal of Stroke, 17:723-732, Jun 2022. URL: https://doi.org/10.1177/17474930221107500, doi:10.1177/17474930221107500. This article has 95 citations and is from a peer-reviewed journal.

26. (ryu2023instentrestenosisand pages 4-6): Jae-Chan Ryu, Jae-Han Bae, Sang Hee Ha, Boseong Kwon, Yunsun Song, Deok Hee Lee, Jun Young Chang, Dong-Wha Kang, Sun U. Kwon, Jong S. Kim, and Bum Joon Kim. In-stent restenosis and stented-territory infarction after carotid and vertebrobasilar artery stenting. BMC Neurology, Feb 2023. URL: https://doi.org/10.1186/s12883-023-03110-z, doi:10.1186/s12883-023-03110-z. This article has 11 citations and is from a peer-reviewed journal.

27. (ryu2023instentrestenosisand pages 1-2): Jae-Chan Ryu, Jae-Han Bae, Sang Hee Ha, Boseong Kwon, Yunsun Song, Deok Hee Lee, Jun Young Chang, Dong-Wha Kang, Sun U. Kwon, Jong S. Kim, and Bum Joon Kim. In-stent restenosis and stented-territory infarction after carotid and vertebrobasilar artery stenting. BMC Neurology, Feb 2023. URL: https://doi.org/10.1186/s12883-023-03110-z, doi:10.1186/s12883-023-03110-z. This article has 11 citations and is from a peer-reviewed journal.

28. (zhang2023microsurgicalrevascularizationof pages 2-4): Tongfu Zhang, Donglin Zhou, Yangyang Xu, Maogui Li, Jianfeng Zhuang, Hai Wang, Weiying Zhong, Chao Chen, Hong Kuang, Donghai Wang, and Yunyan Wang. Microsurgical revascularization of a symptomatic proximal vertebral artery: pilot experiences from a single center. Frontiers in Neurology, Jul 2023. URL: https://doi.org/10.3389/fneur.2023.1202565, doi:10.3389/fneur.2023.1202565. This article has 3 citations and is from a peer-reviewed journal.

29. (zhang2023microsurgicalrevascularizationof pages 5-6): Tongfu Zhang, Donglin Zhou, Yangyang Xu, Maogui Li, Jianfeng Zhuang, Hai Wang, Weiying Zhong, Chao Chen, Hong Kuang, Donghai Wang, and Yunyan Wang. Microsurgical revascularization of a symptomatic proximal vertebral artery: pilot experiences from a single center. Frontiers in Neurology, Jul 2023. URL: https://doi.org/10.3389/fneur.2023.1202565, doi:10.3389/fneur.2023.1202565. This article has 3 citations and is from a peer-reviewed journal.

30. (liu2024applicationofmicrosurgical pages 4-6): Mingyuan Liu, Peiguang Yan, Mingxin Wang, Jia Guo, Wei Liu, Ganchun Wu, Lufei Wang, Jingjing Liu, and Li Li. Application of microsurgical surgery in patients with proximal vertebral artery stenosis unsuited for endovascular treatment: a single-center retrospective study. Neurosurgical Review, Dec 2024. URL: https://doi.org/10.1007/s10143-024-03153-x, doi:10.1007/s10143-024-03153-x. This article has 1 citations and is from a peer-reviewed journal.
