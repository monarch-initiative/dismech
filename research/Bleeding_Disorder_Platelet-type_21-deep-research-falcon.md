---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-23T03:55:00.213161'
end_time: '2026-08-23T04:04:09.974410'
duration_seconds: 549.76
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Bleeding disorder, platelet-type, 21
  mondo_id: MONDO:0054577
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 24
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Bleeding_Disorder_Platelet-type_21-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Bleeding disorder, platelet-type, 21
- **MONDO ID:** MONDO:0054577 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Bleeding disorder, platelet-type, 21** covering all of the
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

For each treatment, suggest NCIT (NCI Thesaurus) clinical-intervention terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, NCIT, MONDO) where applicable
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
- Treatment annotations (NCIT terms)
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
- **Disease Name:** Bleeding disorder, platelet-type, 21
- **MONDO ID:** MONDO:0054577 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Bleeding disorder, platelet-type, 21** covering all of the
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

For each treatment, suggest NCIT (NCI Thesaurus) clinical-intervention terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, NCIT, MONDO) where applicable
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
- Treatment annotations (NCIT terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


# Bleeding disorder, platelet-type, 21: disease-characteristics report

## Executive summary

**Bleeding disorder, platelet-type, 21 (BDPLT21)** is an exceptionally rare, constitutional platelet disorder caused by pathogenic germline variants in **FLI1**, a hematopoietic ETS-family transcription factor. The usual phenotype combines variable mucocutaneous bleeding, mild-to-moderate thrombocytopenia with enlarged platelets, defective platelet aggregation/secretion, and profound platelet dense-granule deficiency. Most molecularly defined families have heterozygous disease consistent with autosomal-dominant inheritance, although a rare recessive FLI1 phenotype has also been described. The evidence base consists principally of a few families and mechanistic studies rather than registries or clinical trials. (gabinaud2025fli1andgata1 pages 1-5, saultier2017macrothrombocytopeniaanddense pages 1-2, rabbolini2016thrombocytopeniacausedby pages 6-7)

The major recent mechanistic advance is the identification of defective **FLI1–GATA1 cooperation and TLN1/talin-1 deficiency**. Single-cell RNA sequencing of patient-derived megakaryocytes found 626 differentially expressed genes, with platelet activation the most downregulated pathway; talin-1 protein was reduced by 88% in patient platelets, providing a mechanistic bridge from transcription-factor dysfunction to defective αIIbβ3-integrin activation and bleeding. This work was published online from a 2024 manuscript and in *Haematologica* in January 2025. (gabinaud2025fli1andgata1 pages 5-9, gabinaud2025fli1andgata1 pages 1-5, gabinaud2025fli1andgata1 pages 9-12)

| Domain | Disease-specific finding | Evidence type and key quantitative data | Suggested ontology terms |
|---|---|---|---|
| Identity / identifiers | Bleeding disorder, platelet-type, 21 (BDPLT21) is a rare constitutional FLI1-related inherited platelet disorder; supported identifiers include MONDO:0054577 and OMIM 617443. | Human disease synthesis from primary human reports and recent review-level curation; 2025 study explicitly describes “FLI1-related platelet disorder BDPLT21” and 2020 review links heterozygous FLI1 mutations to “Bleeding disorder platelet-type 21” (gabinaud2025fli1andgata1 pages 1-5, gabinaud2025fli1andgata1 pages 5-9) | MONDO:0054577; inherited platelet function disorder; inherited thrombocytopenia |
| Gene / inheritance | Causal gene: FLI1. Most reported families show heterozygous dominant disease; rare recessive FLI1 disease has been reported/mentioned for related phenotypes. | Human family studies with variant-level evidence in multiple families; 2025 report notes dominant or recessive inheritance patterns in FLI1-related platelet disease (gabinaud2025fli1andgata1 pages 12-15, rabbolini2016thrombocytopeniacausedby pages 6-7) | FLI1; autosomal dominant inheritance; autosomal recessive inheritance |
| Core phenotype | Variable mucocutaneous and bleeding phenotype with mild-to-moderate thrombocytopenia and macrothrombocytopenia; reported manifestations include purpura, epistaxis, menorrhagia, postpartum hemorrhage, pulmonary hemorrhage, and cutaneous/mucosal bleeding. | Human clinical evidence from several families; one recent patient had platelet counts 83–147 ×10^9/L and MPV 13.3 fL; one case required RBC transfusion, showing severity can occasionally be substantial (gabinaud2025fli1andgata1 pages 47-48, gabinaud2025fli1andgata1 pages 5-9, gabinaud2025fli1andgata1 pages 12-15) | HP:0001873 Thrombocytopenia; HP:0001904 Increased mean platelet volume; HP:0000978 Bruising susceptibility; HP:0000421 Epistaxis; HP:0000132 Menorrhagia; HP:0012147 Postpartum hemorrhage |
| Platelet laboratory signature | Dense-granule secretion/storage-pool defect with impaired aggregation and secretion, often alongside enlarged/abnormal granules. | Primary human platelet studies: reduced aggregation to low-dose ADP, collagen, and TRAP; reduced ATP secretion; reduced mepacrine uptake/release; reduced CD63 after stimulation; nearly absent dense granules; 25–29% giant α-granules; 7–9% vacuoles; 0–3% autophagosome-like structures (saultier2017macrothrombocytopeniaanddense pages 1-2, stockley2013enrichmentoffli1 pages 3-4, gabinaud2025fli1andgata1 pages 5-9) | HP:0003542 Platelet dense granule deficiency; HP:0011875 Abnormal platelet aggregation; HP:0001878 Abnormal platelet morphology |
| Key pathogenic variants | Reported pathogenic/likely pathogenic FLI1 ETS-domain variants include p.R337Q, p.K345E, p.R340C, p.G307R; additional FLI1 alterations reported include p.R337W, p.Y343C, and a frameshift deletion. | Human genetics plus functional assays; recent structural/functional study found p.R340C and p.K345E disruptive (ΔΔG about 1.49 and 1.48 kcal/mol), while p.G307R impaired homodimerization (ΔΔG 3.59 kcal/mol) (gabinaud2025fli1andgata1 pages 9-12, stockley2013enrichmentoffli1 pages 3-4, gabinaud2025fli1andgata1 pages 47-48) | FLI1 missense variant; FLI1 frameshift variant; ETS DNA-binding domain |
| Molecular mechanism | FLI1 dysfunction impairs megakaryopoiesis and platelet activation through reduced nuclear localization and/or stability, reduced transcriptional activity, impaired cooperation with GATA1, and reduced TLN1/talin-1 expression, causing defective αIIbβ3 integrin activation and granule abnormalities. | Human platelets, CD34+ megakaryocytes, scRNA-seq, and reporter assays: 626 differentially expressed genes; platelet activation pathway most downregulated; talin-1 reduced by 88% in patient platelets; G307R and K345E showed ~60% decreased half-life; fibrinogen binding reduced in K345E and R340C carriers (gabinaud2025fli1andgata1 pages 5-9, gabinaud2025fli1andgata1 pages 1-5, gabinaud2025fli1andgata1 pages 9-12, gabinaud2025fli1andgata1 pages 12-15) | GO:0045654 regulation of megakaryocyte differentiation; GO:0030168 platelet activation; GO:0007596 blood coagulation; GO:0008360 regulation of cell shape; megakaryocyte; platelet |
| Diagnostics | Diagnosis requires combined clinical and specialized platelet evaluation plus molecular testing; useful disease-focused clues include MYH10 positivity, dense-granule deficiency on EM, and secretion/aggregation defects. | Human disease-specific and general inherited platelet disorder evidence: intracellular flow cytometry for MYH10 can distinguish affected individuals; LTA remains a gold-standard platelet function test; dense-granule studies, flow cytometry, CBC/smear, and ultrastructure are recommended; NGS/gene panels are important because routine tests alone are insufficient (saultier2017macrothrombocytopeniaanddense pages 9-10, bourguignon2022screeninganddiagnosis pages 1-3, bourguignon2022screeninganddiagnosis pages 10-12, bury2021learningtheropes pages 12-13) | HP:0032180 Abnormal platelet dense granules; MYH10 biomarker; light transmission aggregometry; transmission electron microscopy; next-generation sequencing |
| Management | No BDPLT21-specific molecular therapy or trial-based standard exists; current care is supportive and extrapolated from inherited platelet disorder practice. | Review-based management evidence: avoid aspirin/NSAIDs; use local hemostatic measures and tranexamic acid; hormonal therapy may help menorrhagia; severe situations may require transfusion-oriented support; pregnancy/postpartum and surgery warrant planning. IT cohorts show surgical bleeding 19.7% vs 1.4–6% in controls and postpartum hemorrhage 6.8–14.2% vs 3–7% in controls (bury2021learningtheropes pages 15-17) | tranexamic acid; platelet transfusion; hemostatic support; genetic counseling |
| Epidemiology / prognosis gaps | Population prevalence, incidence, penetrance, sex ratio, long-term survival, formal quality-of-life measures, and malignancy risk are not well defined for BDPLT21. Emerging non-hematologic findings may include cardiac anomalies in some families. | Explicit evidence gap from recent case series/reports: only small numbers of patients/families described; cardiac findings reported include valvular malformation, interventricular communication, and bicuspid aortic valve with ascending aorta dilation (gabinaud2025fli1andgata1 pages 12-15, gabinaud2025fli1andgata1 pages 5-9) | evidence gap; cardiac abnormality; variable expressivity |
| Models | Key models include Fli1 mouse models, patient-derived and isogenic human iPSC megakaryocytes, primary human CD34+ megakaryocytes, and transfected cell-line assays. No established natural veterinary disease model was identified in the gathered evidence. | Mouse limitation: Fli1−/− embryonic lethal at E11.5; Fli1+/− mice may be minimally affected. Human iPSC/megakaryocyte models recapitulate decreased megakaryocyte yield, reduced platelet release, impaired colony formation, shortened platelet half-life, reduced ploidy, and reduced proplatelet formation (vo2017fli1levelduring pages 1-2, vo2017fli1levelduring pages 2-3, vo2017fli1levelduring pages 3-4, saultier2017macrothrombocytopeniaanddense pages 5-7, gabinaud2025fli1andgata1 pages 1-5) | model organism; induced pluripotent stem cell-derived megakaryocyte; megakaryocyte differentiation assay; platelet model |


*Table: This compact table summarizes the highest-value disease facts for Bleeding disorder, platelet-type, 21, including identity, genetics, phenotype, mechanism, diagnostics, management, and evidence gaps. It is designed for rapid knowledge-base population using only evidence gathered in the conversation.*

## 1. Disease information

### Definition and identifiers

* **Preferred name:** Bleeding disorder, platelet-type, 21
* **Abbreviation:** BDPLT21
* **MONDO:** **MONDO:0054577**, as supplied in the target record
* **OMIM phenotype:** **617443**
* **Causal gene:** **FLI1**
* **Useful synonyms:** FLI1-related platelet disorder; FLI1-related thrombocytopenia; FLI1-associated macrothrombocytopenia and dense-granule deficiency; FLI1-related platelet dysfunction.

“Paris–Trousseau thrombocytopenia” should be used cautiously as a synonym. That phenotype classically occurs in Jacobsen syndrome/terminal 11q deletion involving FLI1, whereas BDPLT21 generally denotes disease from germline sequence-level FLI1 variants. The disorders overlap mechanistically and phenotypically but are not always nosologically identical. (rabbolini2016thrombocytopeniacausedby pages 6-7, vo2017fli1levelduring pages 1-2)

No dedicated Orphanet, MeSH, ICD-10, or ICD-11 code was established from the retrieved evidence. In practice, nonspecific codes for inherited platelet-function disorder or thrombocytopenia may be used, but these should not be represented as disease-specific identifiers.

The available information is **aggregated disease-level evidence reconstructed from a very small number of individual patients and families**, not EHR-derived population evidence. The principal studies include three UK families in 2013, two French families in 2017, and additional families characterized in the recent mechanistic investigation. (saultier2017macrothrombocytopeniaanddense pages 1-2, stockley2013enrichmentoffli1 pages 3-4, gabinaud2025fli1andgata1 pages 5-9)

## 2. Etiology, risk, and protective factors

### Primary cause

BDPLT21 is a **Mendelian genetic disorder** caused by germline FLI1 dysfunction. Most reported variants affect the ETS DNA-binding domain and reduce nuclear localization, DNA-dependent transcription, protein stability, homodimerization, or cooperation with GATA1. Reported sequence variants include:

* **c.1009C>T, p.Arg337Gln (R337Q)**
* **c.1033A>G, p.Lys345Glu (K345E)**
* **c.1018C>T, p.Arg340Cys (R340C)**
* **c.919G>A, p.Gly307Arg (G307R)**
* Earlier reports also identified **p.Arg337Trp**, **p.Tyr343Cys**, and a frameshift deletion. (gabinaud2025fli1andgata1 pages 5-9, gabinaud2025fli1andgata1 pages 9-12, stockley2013enrichmentoffli1 pages 3-4)

R340C and K345E were structurally disruptive at the DNA–FLI1 interface, with calculated ΔΔG values of approximately 1.49 and 1.48 kcal/mol; G307R had a larger predicted effect on homodimerization, ΔΔG 3.59 kcal/mol. G307R and K345E reduced protein half-life by about 60%. These are functional-study results, not clinical prognostic thresholds. (gabinaud2025fli1andgata1 pages 12-15, gabinaud2025fli1andgata1 pages 9-12, gabinaud2025fli1andgata1 pages 47-48)

### Risk factors and modifiers

* **Genetic risk:** carrying a pathogenic germline FLI1 allele; family history of thrombocytopenia, platelet storage-pool disease, or disproportionate mucocutaneous/procedural bleeding.
* **Environmental/lifestyle triggers:** no exposure causes the Mendelian disorder. Trauma, surgery, childbirth, menstruation, and platelet-inhibiting medicines can unmask or exacerbate bleeding.
* **Protective factors:** no protective allele or validated disease-specific environmental factor is known. Avoidance of aspirin and nonsteroidal anti-inflammatory drugs reduces avoidable impairment of residual platelet function. (bury2021learningtheropes pages 15-17)
* **Gene–environment interaction:** conceptually, congenital impairment of platelet production and secretion lowers hemostatic reserve, while surgery, injury, mucosal inflammation, menstruation, or antiplatelet exposure increases demand or further suppresses platelet function. This interaction is clinically plausible but has not been quantified specifically in BDPLT21.
* **Modifier genes/epigenetics:** no validated modifier gene, methylation signature, histone abnormality, or protective variant has been reported.
* **Infection:** no infectious cause, trigger, reservoir, or zoonotic mechanism applies.

## 3. Phenotypes

### Core clinical phenotypes

| Phenotype | Type and characteristics | Suggested HPO term |
|---|---|---|
| Thrombocytopenia | Laboratory abnormality; usually mild-to-moderate and lifelong. One recent patient ranged from 83–147 ×10⁹/L. | HP:0001873 |
| Enlarged platelets/macrothrombocytopenia | Laboratory/morphologic sign; MPV 13.3 fL in one patient, reference 8–12 fL. | HP:0001904; HP:0001878 |
| Mucocutaneous bleeding | Symptom/sign; variable purpura, bruising and mucosal bleeding, generally episodic rather than progressive. | HP:0000978; HP:0001892 |
| Epistaxis | Symptom; recurrent in reported patients. | HP:0000421 |
| Menorrhagia | Symptom in affected females; may materially impair daily activity and cause anemia. | HP:0000132 |
| Postpartum hemorrhage | Complication reported in affected women; requires anticipatory obstetric planning. | HP:0012147 |
| Pulmonary hemorrhage | Rare severe manifestation; recurrent episodes in one patient required hospitalization and red-cell transfusion. | HP:0040223 |
| Defective platelet aggregation | Functional laboratory phenotype, particularly with low-dose ADP, collagen, and TRAP. | HP:0011875 |
| Dense-granule deficiency/storage-pool defect | Structural and secretion abnormality; dense granules can be nearly absent. | HP:0003542 |
| Cardiac anomaly | Emerging, incompletely established association: bicuspid aortic valve, ascending-aortic dilation, valvular malformation, and interventricular communication have been reported. | HP:0001647; HP:0004942; HP:0010445 |

The phenotype is **congenital and lifelong**, although clinical recognition can occur in childhood or adulthood after bleeding challenge. Five patients in one recent series were 10–44 years old. Severity is variable: some have mainly mild mucocutaneous bleeding, whereas occasional patients experience postpartum or pulmonary hemorrhage and require transfusion. There is no evidence of an intrinsically progressive platelet disorder, but bleeding is episodic and exposure-dependent. (gabinaud2025fli1andgata1 pages 12-15, gabinaud2025fli1andgata1 pages 5-9)

### Laboratory and ultrastructural phenotype

In the 2017 primary study, platelets had reduced aggregation after low-dose ADP, collagen, and TRAP; impaired ATP secretion; reduced mepacrine uptake and release; and reduced activation-induced CD63. Dense granules were nearly absent. **Giant α-granules occurred in 25–29% of platelets, vacuoles in 7–9%, and autophagosome-like structures in 0–3%.** (saultier2017macrothrombocytopeniaanddense pages 1-2)

One recent G307R carrier had ATP content of **0 nmol/10⁸ platelets** and serotonin of **0.087 μg/10⁹ platelets** versus a stated reference of 0.3–1.2, illustrating severe storage-pool depletion even where some conventional aggregation responses remain near reference limits. (gabinaud2025fli1andgata1 pages 47-48)

Patient-derived megakaryocytes also show reduced size, ploidy, maturation, and proplatelet formation. At day 14 in one experiment, high-ploidy cells were 11.3% in controls versus 6.2% and 4.5% in two affected individuals. (saultier2017macrothrombocytopeniaanddense pages 5-7)

### Frequency and quality of life

No reliable phenotype percentages can be assigned because denominators are very small and ascertainment is bleeding-clinic based. Formal EQ-5D, SF-36, PROMIS, disability, or disease-specific quality-of-life measurements have not been reported. Likely burdens include recurrent epistaxis/bruising, menstrual restriction, anxiety around procedures and pregnancy, hospitalization for severe hemorrhage, and avoidance of contact activities; these are reasonable clinical consequences but not quantified BDPLT21 outcomes.

## 4. Genetic and molecular information

**FLI1** encodes Friend leukemia integration 1, an ETS-family transcription factor essential to megakaryocyte differentiation, thrombopoiesis, platelet granule biology, and vascular development. Disease alleles are germline. No evidence supports a somatic origin for constitutional BDPLT21, although acquired hematopoietic alterations involving FLI1 may phenocopy platelet disease and should not be conflated with inherited disease.

Most known BDPLT21 alleles are missense variants clustered in the ETS domain; a frameshift allele has also been reported. Disease mechanisms include haploinsufficiency, reduced stability, defective nuclear import, and impaired/dominant-interfering transcriptional function. Exact ClinVar classifications and population allele frequencies were not recoverable from the gathered literature and should be checked against the current ClinVar and gnomAD record for the precise transcript before database ingestion. Given the rarity and functional severity, established disease alleles are expected to be absent or extremely rare in population databases, but no numerical frequency should be inferred without direct database verification.

No recurrent chromosomal abnormality defines sequence-level BDPLT21. A terminal 11q deletion encompassing FLI1 causes the related Paris–Trousseau/Jacobsen phenotype. CMA or genome-wide CNV analysis is therefore appropriate when syndromic features suggest a larger deletion. No disease-specific epigenetic signature is known.

## 5. Environmental information

No toxin, radiation exposure, pollutant, occupation, diet, smoking pattern, alcohol exposure, or pathogen is known to cause BDPLT21. Clinically important aggravators are platelet-inhibiting drugs, trauma, invasive procedures, menstruation, and delivery. Alcohol excess could theoretically worsen platelet function or injury risk, but this has not been studied in BDPLT21. Environmental mitigation is therefore directed at **bleeding-risk reduction**, not prevention of the genotype.

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream genetic lesion:** germline FLI1 variant, commonly in the ETS DNA-binding domain.
2. **Protein dysfunction:** reduced stability, faulty nuclear localization, impaired DNA binding/homodimerization, or reduced transcriptional cooperation with GATA1.
3. **Megakaryocyte transcriptional dysregulation:** altered expression begins at megakaryocyte–erythroid progenitor/megakaryocyte stages. Recent scRNA-seq identified **626 differentially expressed genes**, with platelet activation the most downregulated pathway. (gabinaud2025fli1andgata1 pages 5-9, gabinaud2025fli1andgata1 pages 9-12)
4. **Defective megakaryopoiesis:** reduced megakaryocyte yield, size, ploidy, maturation, and proplatelet formation.
5. **Granule and activation defects:** nearly absent dense granules, giant/fused α-granules, reduced ATP/serotonin content and release, and deficient CD63 response.
6. **TLN1/talin-1 axis:** FLI1 and GATA1 normally cooperate at an intronic TLN1 regulatory region. Variant FLI1 reduces TLN1 transcription; patient platelets showed an **88% reduction in talin-1 protein**. (gabinaud2025fli1andgata1 pages 1-5, gabinaud2025fli1andgata1 pages 9-12)
7. **Downstream functional failure:** impaired inside-out activation of platelet αIIbβ3 integrin, reduced fibrinogen binding, defective aggregation and thrombus stabilization.
8. **Clinical endpoint:** thrombocytopenia plus qualitative platelet dysfunction produces mucocutaneous, menstrual, obstetric, traumatic, or procedural bleeding.

This model is supported by human patient platelets and primary CD34+-derived megakaryocytes, scRNA-seq, luciferase assays, structural modeling, and cell localization/stability experiments. It is stronger than a mechanism inferred solely from animal models. (gabinaud2025fli1andgata1 pages 9-12, gabinaud2025fli1andgata1 pages 5-9, saultier2017macrothrombocytopeniaanddense pages 5-7)

### Suggested controlled vocabulary

* **GO biological process:** megakaryocyte differentiation; platelet formation; platelet activation (**GO:0030168**); platelet aggregation (**GO:0070527**); blood coagulation (**GO:0007596**); integrin activation; regulated exocytosis; dense-granule organization.
* **Cell Ontology:** megakaryocyte (**CL:0000556**); platelet (**CL:0000233**); megakaryocyte–erythroid progenitor.
* **GO cellular components:** nucleus; platelet dense granule; platelet α-granule; cytoplasm; integrin complex; cytoskeleton.
* **Anatomy:** bone marrow (**UBERON:0002371**), blood (**UBERON:0000178**), vascular system.

No disease-specific metabolomic, lipidomic, proteomic atlas, spatial-transcriptomic study, CRISPR screen, or validated circulating molecular biomarker panel was identified. The recent scRNA-seq/TLN1 work is currently the most informative molecular-profile dataset.

## 7. Anatomical structures affected

The primary system is hematologic/hemostatic:

* **Organ/tissue:** bone marrow megakaryopoietic compartment and circulating blood.
* **Cells:** megakaryocyte progenitors, mature megakaryocytes, and platelets.
* **Subcellular structures:** FLI1-containing nucleus, dense granules, α-granules, cytoskeleton, and talin–αIIbβ3 adhesion machinery.
* **Secondary sites:** skin and mucosal surfaces manifest bleeding; uterus is relevant to menorrhagia/postpartum hemorrhage; lungs were involved in one severe hemorrhagic phenotype.
* **Possible developmental involvement:** cardiac valves, ventricular septum, and ascending aorta, based on a few cases. Cardiac causality remains provisional. (gabinaud2025fli1andgata1 pages 12-15, gabinaud2025fli1andgata1 pages 5-9)

There is no meaningful lateralization.

## 8. Temporal development

The molecular defect is present from conception and the platelet phenotype is expected from early life. Recognition may be delayed because thrombocytopenia can be mild and bleeding often emerges with hemostatic challenge. The course is chronic/lifelong and generally stable, with episodic bleeding rather than defined stages, remission, or end-stage disease. Critical periods include surgery, dental extraction, menarche and menstruation, pregnancy/delivery, trauma, and initiation of antiplatelet medication. No evidence supports spontaneous molecular remission.

## 9. Inheritance and population

Most sequence-level cases support **autosomal-dominant inheritance** from heterozygous FLI1 variants. Rare biallelic/recessive FLI1 disease can phenocopy Paris–Trousseau thrombocytopenia, but it should be separately annotated where both alleles and segregation are demonstrated. (rabbolini2016thrombocytopeniacausedby pages 6-7, gabinaud2025fli1andgata1 pages 12-15)

Penetrance has not been numerically estimated. The observation of excessive bleeding among index cases and affected relatives supports clinically relevant penetrance, while differences in platelet counts and bleeding severity indicate **variable expressivity**. No anticipation mechanism, repeat expansion, founder effect, germline-mosaicism estimate, carrier frequency, consanguinity effect, sex ratio, ethnic enrichment, or geographic concentration is established. (gabinaud2025fli1andgata1 pages 12-15, stockley2013enrichmentoffli1 pages 3-4)

Prevalence and incidence per 100,000 are unknown. The disease is best designated **ultra-rare**, based on only a small number of molecularly characterized families rather than population surveillance. Sexes should be considered equally genetically susceptible; female reproductive bleeding creates sex-specific clinical burden.

## 10. Diagnostics

### Recommended workflow

1. **Clinical assessment:** document lifelong bleeding, surgery/dental bleeding, epistaxis, bruising, menorrhagia, postpartum hemorrhage, and three-generation family history; use an ISTH bleeding-assessment tool where feasible.
2. **First-line laboratory testing:** repeat CBC with platelet count and MPV; manually inspect the smear for large platelets; obtain PT, aPTT, fibrinogen, and von Willebrand studies to exclude common coagulation and VWF disorders.
3. **Platelet function:** light-transmission aggregometry remains a gold-standard method. Include ADP, collagen, TRAP/thrombin-pathway agonists, arachidonic acid, and ristocetin. Pair aggregation with ATP-release luminometry because secretion can be more abnormal than maximal aggregation. (bourguignon2022screeninganddiagnosis pages 1-3, bourguignon2022screeninganddiagnosis pages 10-12)
4. **Granule assessment:** mepacrine uptake/release, platelet serotonin/ATP content, activation-induced CD63 flow cytometry, and whole-mount or transmission electron microscopy for δ-granules and giant α-granules.
5. **FLI1-focused biomarker:** intracellular platelet **MYH10** flow cytometry can rapidly distinguish FLI1-altered platelets using relatively little blood; it is a supportive biomarker, not a standalone genetic diagnosis. (saultier2017macrothrombocytopeniaanddense pages 9-10, bury2021learningtheropes pages 12-13)
6. **Molecular confirmation:** an inherited bleeding/thrombocytopenia multigene panel including FLI1 is usually the efficient first test. Sequence data require ACMG/AMP classification, segregation analysis, phenotype matching, and functional evidence.
7. **Escalation:** WES or WGS is appropriate when the panel is negative or the phenotype is atypical. CNV-sensitive analysis/CMA is appropriate for syndromic features suggesting an 11q deletion. Karyotyping or FISH is not routine for isolated sequence-level disease but may confirm a suspected large 11q lesion.
8. **Family testing:** targeted testing of relatives after identification of the familial variant; genetic counseling before predictive testing of minors should account for immediate bleeding-management benefits.

General high-throughput sequencing data demonstrate clinical utility but not a BDPLT21-specific yield. In one inherited platelet-disorder cohort, sequencing produced a molecular diagnosis in 70% overall and 90% among patients suspected of a defined disorder; those figures must not be applied as BDPLT21 sensitivity. Routine phenotype and screening tests alone are insufficient for a definitive FLI1 diagnosis. (saultier2017macrothrombocytopeniaanddense pages 9-10)

### Differential diagnosis

Important alternatives include immune thrombocytopenia; von Willebrand disease; MYH9-related disease; Bernard–Soulier syndrome; gray platelet syndrome; Hermansky–Pudlak and other storage-pool disorders; RUNX1-, GATA1-, GFI1B-, ETV6-, and ANKRD26-related thrombocytopenias; and Paris–Trousseau thrombocytopenia from an 11q deletion. Features favoring FLI1 disease are dominant familial bleeding, mild macrothrombocytopenia, severe dense-granule secretion deficiency, giant α-granules, platelet MYH10 expression, and a functionally supported germline FLI1 variant.

Imaging, electrophysiology, tissue biopsy, liquid biopsy, mitochondrial testing, and repeat-expansion testing have no routine role. Given recent cardiac observations, baseline echocardiography and assessment of the aortic root/ascending aorta are reasonable expert-driven considerations, although this is not yet a validated society guideline. (gabinaud2025fli1andgata1 pages 12-15)

## 11. Outcome and prognosis

No 5- or 10-year survival rates, disease-specific mortality estimates, or validated prognostic models exist. Life expectancy is probably not intrinsically reduced in mildly affected individuals, but that is an inference rather than measured evidence. Major morbidity comes from hemorrhage, anemia/transfusion, surgical complications, heavy menstrual bleeding, and pregnancy-related bleeding.

The strongest individual prognostic indicators are likely personal bleeding history, platelet count, secretion defect, prior surgical/obstetric hemorrhage, and exposure to hemostatic challenges. Variant-specific effects on protein stability/localization are biologically important but have not been validated as clinical prognostic biomarkers.

No convincing disease-specific risk of MDS/AML has been established for isolated FLI1 BDPLT21. This differs from RUNX1-, ANKRD26-, and ETV6-related thrombocytopenias; extrapolating their malignancy surveillance protocols to FLI1 carriers is not evidence based.

## 12. Treatment

No therapy corrects the underlying FLI1 defect, and no BDPLT21-specific randomized trial, gene therapy, RNA therapy, cell therapy, or approved targeted drug was identified. Management is individualized supportive care, preferably through a specialist inherited-bleeding-disorder center.

### Practical strategy

* Provide an emergency/bleeding plan and alert card.
* Avoid aspirin and nonessential NSAIDs; review supplements and medicines that impair platelets.
* Use compression, topical hemostatic agents, fibrin sealants, gelatin sponges, and tranexamic-acid-soaked gauze for accessible bleeding.
* Consider systemic **tranexamic acid** for mucosal, dental, menstrual, or perioperative bleeding when not contraindicated.
* Hormonal menstrual suppression may reduce heavy menstrual bleeding.
* Plan surgery and delivery jointly with hematology, anesthesia, surgery/obstetrics, transfusion medicine, and the laboratory.
* Platelet transfusion is reserved for major bleeding or high-risk procedures because repeated exposure carries alloimmunization and transfusion risks. Red-cell transfusion treats clinically significant blood loss/anemia, not the platelet defect.
* Desmopressin or recombinant factor VIIa may be considered in selected inherited platelet disorders under specialist direction, but BDPLT21-specific response and safety data are absent.

Suggested NCIT intervention concepts include tranexamic-acid therapy, platelet transfusion, red-blood-cell transfusion, hormonal therapy, local hemostatic procedure, and genetic counseling.

In broad inherited-thrombocytopenia cohorts, surgical bleeding occurred in **19.7%**, compared with 1.4–6% in controls, and postpartum hemorrhage in **6.8–14.2%**, compared with 3–7% in controls. These statistics justify anticipatory planning but are not BDPLT21-specific event rates. (bury2021learningtheropes pages 15-17)

## 13. Prevention

Primary prevention of the germline disorder is not possible after conception. Reproductive options following identification of a pathogenic familial variant include preconception counseling, targeted prenatal diagnosis, and preimplantation genetic testing, subject to local law and family preferences.

Secondary prevention consists of early recognition, targeted/cascade testing, documenting baseline platelet phenotype, avoiding misdiagnosis as immune thrombocytopenia, and considering baseline cardiac/aortic ultrasound. Tertiary prevention includes medication avoidance, dental hygiene, procedural planning, menstrual management, trauma precautions, and rapid treatment of hemorrhage. There is no applicable vaccine, population newborn screen, prophylactic chronic drug regimen, or public-health environmental intervention.

## 14. Other species and natural disease

No established naturally occurring veterinary counterpart, breed association, OMIA syndrome, cross-species transmission, or zoonotic potential was identified. FLI1 orthologues are evolutionarily conserved, but experimental models—not spontaneous animal disease—provide the comparative evidence.

## 15. Model organisms and experimental systems

### Mouse

Complete **Fli1−/−** mice die around embryonic day 11.5 with abnormal vasculature and thrombocytopenia; heterozygous mice can be minimally affected. Mice lacking a carboxy-terminal regulatory domain develop thrombocytopenia and defective platelet activation/aggregation. These models establish FLI1’s roles in vascular and megakaryocytic development, but embryonic lethality and the weak heterozygous phenotype limit direct modeling of human dominant BDPLT21. (vo2017fli1levelduring pages 1-2, gabinaud2025fli1andgata1 pages 1-5, saultier2017macrothrombocytopeniaanddense pages 11-11)

### Human iPSC models

Patient-derived Paris–Trousseau iPSCs and isogenic TALEN-generated FLI1+/− lines were differentiated into megakaryocytes. They reproduced decreased megakaryocyte yield, reduced platelet release per cell, impaired large CFU-megakaryocyte formation, altered MPL expression, in-vivo platelet dysfunction, and shortened platelet-like-particle survival after infusion into NSG mice. FLI1 rescue/overexpression lines support causal attribution, although in-vitro platelet-like particles do not fully reproduce native human platelet production. (vo2017fli1levelduring pages 2-3, vo2017fli1levelduring pages 1-2, vo2017fli1levelduring pages 3-4)

### Primary human and in-vitro systems

Patient CD34+-derived megakaryocytes demonstrate reduced high ploidy and proplatelet formation and have enabled disease-stage scRNA-seq. Transfected GripTite293/MSR and H9C2 cells have been used for nuclear localization, stability, and reporter assays. These systems are valuable for variant classification but cannot independently establish clinical penetrance or treatment response. (saultier2017macrothrombocytopeniaanddense pages 5-7, gabinaud2025fli1andgata1 pages 5-9)

## Recent developments and authoritative interpretation

The most important recent study is Gabinaud et al., *Haematologica*, published January 2025 from a 2024 manuscript, DOI [10.3324/haematol.2024.286372](https://doi.org/10.3324/haematol.2024.286372). Its abstract states: **“A total of 626 genes were differentially expressed in patient megakaryocytes, including genes associated with the platelet activation pathway,”** and **“TLN1 was among the most down-regulated genes, with an 88% reduction in talin-1 protein levels.”** The authors propose talin-1 as a potential functional biomarker for classifying FLI1 variants. This is compelling mechanistic evidence, but replication across more alleles and independent cohorts is needed before talin-1 becomes a clinical diagnostic standard. (gabinaud2025fli1andgata1 pages 5-9, gabinaud2025fli1andgata1 pages 1-5)

The foundational ultrastructural study is Saultier et al., *Haematologica*, June 2017, DOI [10.3324/haematol.2016.153577](https://doi.org/10.3324/haematol.2016.153577). Its abstract reports that **“dense granules were nearly absent in the carriers’ platelets”** and that **“25–29% of the platelets displayed giant α-granules.”** This remains the strongest disease-specific evidence for the characteristic granule phenotype. (saultier2017macrothrombocytopeniaanddense pages 1-2)

The early family evidence is Stockley et al., *Blood*, December 2013, DOI [10.1182/blood-2013-06-506873](https://doi.org/10.1182/blood-2013-06-506873), which identified heterozygous FLI1 alterations in families with excessive bleeding and dense-granule secretion defects. (stockley2013enrichmentoffli1 pages 3-4)

For current diagnostic practice, Bourguignon et al., *Critical Reviews in Clinical Laboratory Sciences*, March 2022, DOI [10.1080/10408363.2022.2049199](https://doi.org/10.1080/10408363.2022.2049199), supports combined clinical assessment, CBC/smear, light-transmission aggregometry, secretion and granule studies, flow cytometry, ultrastructure, and molecular testing rather than reliance on a single assay. (bourguignon2022screeninganddiagnosis pages 1-3, bourguignon2022screeninganddiagnosis pages 10-12)

## Evidence limitations

BDPLT21 lacks population epidemiology, prospective natural-history cohorts, formal penetrance estimates, standardized phenotype frequencies, controlled treatment studies, quality-of-life data, and disease-specific clinical trials. Cardiac involvement is biologically plausible and reported in several recent patients but remains an emerging association. Variant interpretation should therefore integrate segregation, rarity, domain location, patient platelet phenotype, and functional assays rather than assuming every rare FLI1 variant is pathogenic. The report’s quantitative clinical-management statistics derive from broader inherited-thrombocytopenia cohorts and must not be entered as BDPLT21-specific incidence values.

References

1. (gabinaud2025fli1andgata1 pages 1-5): Elisa Gabinaud, Laurent Hannouche, Mathilde Veneziano-Broccia, Johannes Van Agthoven, Justine Suffit, Julien Maurizio, Delphine Potier, Dominique Payet-Bornet, Delphine Bastelica, Elisa Andersen, Manal Ibrahim-Kosta, Timothée Bigot, Céline Falaise, Anne Vincenot, Pierre-Emmanuel Morange, Paul Saultier, Marie-Christine Alessi, Marjorie Poggi, and Hemostasis Unit Of Lille. Fli1 and gata1 govern tln1 transcription: new insights into fli1-related platelet disorders. Haematologica, 110:1584-1595, Jan 2025. URL: https://doi.org/10.3324/haematol.2024.286372, doi:10.3324/haematol.2024.286372. This article has 6 citations.

2. (saultier2017macrothrombocytopeniaanddense pages 1-2): Paul Saultier, Léa Vidal, Matthias Canault, Denis Bernot, Céline Falaise, Catherine Pouymayou, Jean-Claude Bordet, Noémie Saut, Agathe Rostan, Véronique Baccini, Franck Peiretti, Marie Favier, Pauline Lucca, Jean-François Deleuze, Robert Olaso, Anne Boland, Pierre Emmanuel Morange, Christian Gachet, Fabrice Malergue, Sixtine Fauré, Anita Eckly, David-Alexandre Trégouët, Marjorie Poggi, and Marie-Christine Alessi. Macrothrombocytopenia and dense granule deficiency associated with fli1 variants: ultrastructural and pathogenic features. Haematologica, 102:1006-1016, Jun 2017. URL: https://doi.org/10.3324/haematol.2016.153577, doi:10.3324/haematol.2016.153577. This article has 64 citations.

3. (rabbolini2016thrombocytopeniacausedby pages 6-7): David J. Rabbolini, Christopher M. Ward, and William S. Stevenson. Thrombocytopenia caused by inherited haematopoietic transcription factor mutation: clinical phenotypes and diagnostic considerations. EMJ Hematology, pages 100-109, Jul 2016. URL: https://doi.org/10.33590/emjhematol/10314585, doi:10.33590/emjhematol/10314585. This article has 3 citations.

4. (gabinaud2025fli1andgata1 pages 5-9): Elisa Gabinaud, Laurent Hannouche, Mathilde Veneziano-Broccia, Johannes Van Agthoven, Justine Suffit, Julien Maurizio, Delphine Potier, Dominique Payet-Bornet, Delphine Bastelica, Elisa Andersen, Manal Ibrahim-Kosta, Timothée Bigot, Céline Falaise, Anne Vincenot, Pierre-Emmanuel Morange, Paul Saultier, Marie-Christine Alessi, Marjorie Poggi, and Hemostasis Unit Of Lille. Fli1 and gata1 govern tln1 transcription: new insights into fli1-related platelet disorders. Haematologica, 110:1584-1595, Jan 2025. URL: https://doi.org/10.3324/haematol.2024.286372, doi:10.3324/haematol.2024.286372. This article has 6 citations.

5. (gabinaud2025fli1andgata1 pages 9-12): Elisa Gabinaud, Laurent Hannouche, Mathilde Veneziano-Broccia, Johannes Van Agthoven, Justine Suffit, Julien Maurizio, Delphine Potier, Dominique Payet-Bornet, Delphine Bastelica, Elisa Andersen, Manal Ibrahim-Kosta, Timothée Bigot, Céline Falaise, Anne Vincenot, Pierre-Emmanuel Morange, Paul Saultier, Marie-Christine Alessi, Marjorie Poggi, and Hemostasis Unit Of Lille. Fli1 and gata1 govern tln1 transcription: new insights into fli1-related platelet disorders. Haematologica, 110:1584-1595, Jan 2025. URL: https://doi.org/10.3324/haematol.2024.286372, doi:10.3324/haematol.2024.286372. This article has 6 citations.

6. (gabinaud2025fli1andgata1 pages 12-15): Elisa Gabinaud, Laurent Hannouche, Mathilde Veneziano-Broccia, Johannes Van Agthoven, Justine Suffit, Julien Maurizio, Delphine Potier, Dominique Payet-Bornet, Delphine Bastelica, Elisa Andersen, Manal Ibrahim-Kosta, Timothée Bigot, Céline Falaise, Anne Vincenot, Pierre-Emmanuel Morange, Paul Saultier, Marie-Christine Alessi, Marjorie Poggi, and Hemostasis Unit Of Lille. Fli1 and gata1 govern tln1 transcription: new insights into fli1-related platelet disorders. Haematologica, 110:1584-1595, Jan 2025. URL: https://doi.org/10.3324/haematol.2024.286372, doi:10.3324/haematol.2024.286372. This article has 6 citations.

7. (gabinaud2025fli1andgata1 pages 47-48): Elisa Gabinaud, Laurent Hannouche, Mathilde Veneziano-Broccia, Johannes Van Agthoven, Justine Suffit, Julien Maurizio, Delphine Potier, Dominique Payet-Bornet, Delphine Bastelica, Elisa Andersen, Manal Ibrahim-Kosta, Timothée Bigot, Céline Falaise, Anne Vincenot, Pierre-Emmanuel Morange, Paul Saultier, Marie-Christine Alessi, Marjorie Poggi, and Hemostasis Unit Of Lille. Fli1 and gata1 govern tln1 transcription: new insights into fli1-related platelet disorders. Haematologica, 110:1584-1595, Jan 2025. URL: https://doi.org/10.3324/haematol.2024.286372, doi:10.3324/haematol.2024.286372. This article has 6 citations.

8. (stockley2013enrichmentoffli1 pages 3-4): Jacqueline Stockley, Neil V. Morgan, Danai Bem, Gillian C. Lowe, Marie Lordkipanidzé, Ban Dawood, Michael A. Simpson, Kirsty Macfarlane, Kevin Horner, Vincenzo C. Leo, Katherine Talks, Jayashree Motwani, Jonathan T. Wilde, Peter W. Collins, Michael Makris, Steve P. Watson, and Martina E. Daly. Enrichment of fli1 and runx1 mutations in families with excessive bleeding and platelet dense granule secretion defects. Blood, 122 25:4090-3, Dec 2013. URL: https://doi.org/10.1182/blood-2013-06-506873, doi:10.1182/blood-2013-06-506873. This article has 153 citations and is from a highest quality peer-reviewed journal.

9. (saultier2017macrothrombocytopeniaanddense pages 9-10): Paul Saultier, Léa Vidal, Matthias Canault, Denis Bernot, Céline Falaise, Catherine Pouymayou, Jean-Claude Bordet, Noémie Saut, Agathe Rostan, Véronique Baccini, Franck Peiretti, Marie Favier, Pauline Lucca, Jean-François Deleuze, Robert Olaso, Anne Boland, Pierre Emmanuel Morange, Christian Gachet, Fabrice Malergue, Sixtine Fauré, Anita Eckly, David-Alexandre Trégouët, Marjorie Poggi, and Marie-Christine Alessi. Macrothrombocytopenia and dense granule deficiency associated with fli1 variants: ultrastructural and pathogenic features. Haematologica, 102:1006-1016, Jun 2017. URL: https://doi.org/10.3324/haematol.2016.153577, doi:10.3324/haematol.2016.153577. This article has 64 citations.

10. (bourguignon2022screeninganddiagnosis pages 1-3): Alex Bourguignon, Subia Tasneem, and Catherine P. Hayward. Screening and diagnosis of inherited platelet disorders. Critical Reviews in Clinical Laboratory Sciences, 59:405-444, Mar 2022. URL: https://doi.org/10.1080/10408363.2022.2049199, doi:10.1080/10408363.2022.2049199. This article has 46 citations and is from a peer-reviewed journal.

11. (bourguignon2022screeninganddiagnosis pages 10-12): Alex Bourguignon, Subia Tasneem, and Catherine P. Hayward. Screening and diagnosis of inherited platelet disorders. Critical Reviews in Clinical Laboratory Sciences, 59:405-444, Mar 2022. URL: https://doi.org/10.1080/10408363.2022.2049199, doi:10.1080/10408363.2022.2049199. This article has 46 citations and is from a peer-reviewed journal.

12. (bury2021learningtheropes pages 12-13): Loredana Bury, Emanuela Falcinelli, and Paolo Gresele. Learning the ropes of platelet count regulation: inherited thrombocytopenias. Journal of Clinical Medicine, 10:533, Feb 2021. URL: https://doi.org/10.3390/jcm10030533, doi:10.3390/jcm10030533. This article has 36 citations.

13. (bury2021learningtheropes pages 15-17): Loredana Bury, Emanuela Falcinelli, and Paolo Gresele. Learning the ropes of platelet count regulation: inherited thrombocytopenias. Journal of Clinical Medicine, 10:533, Feb 2021. URL: https://doi.org/10.3390/jcm10030533, doi:10.3390/jcm10030533. This article has 36 citations.

14. (vo2017fli1levelduring pages 1-2): Karen K. Vo, Danuta J. Jarocha, Randolph B. Lyde, Vincent Hayes, Christopher S. Thom, Spencer K. Sullivan, Deborah L. French, and Mortimer Poncz. Fli1 level during megakaryopoiesis affects thrombopoiesis and platelet biology. Blood, 129 26:3486-3494, Jun 2017. URL: https://doi.org/10.1182/blood-2017-02-770958, doi:10.1182/blood-2017-02-770958. This article has 66 citations and is from a highest quality peer-reviewed journal.

15. (vo2017fli1levelduring pages 2-3): Karen K. Vo, Danuta J. Jarocha, Randolph B. Lyde, Vincent Hayes, Christopher S. Thom, Spencer K. Sullivan, Deborah L. French, and Mortimer Poncz. Fli1 level during megakaryopoiesis affects thrombopoiesis and platelet biology. Blood, 129 26:3486-3494, Jun 2017. URL: https://doi.org/10.1182/blood-2017-02-770958, doi:10.1182/blood-2017-02-770958. This article has 66 citations and is from a highest quality peer-reviewed journal.

16. (vo2017fli1levelduring pages 3-4): Karen K. Vo, Danuta J. Jarocha, Randolph B. Lyde, Vincent Hayes, Christopher S. Thom, Spencer K. Sullivan, Deborah L. French, and Mortimer Poncz. Fli1 level during megakaryopoiesis affects thrombopoiesis and platelet biology. Blood, 129 26:3486-3494, Jun 2017. URL: https://doi.org/10.1182/blood-2017-02-770958, doi:10.1182/blood-2017-02-770958. This article has 66 citations and is from a highest quality peer-reviewed journal.

17. (saultier2017macrothrombocytopeniaanddense pages 5-7): Paul Saultier, Léa Vidal, Matthias Canault, Denis Bernot, Céline Falaise, Catherine Pouymayou, Jean-Claude Bordet, Noémie Saut, Agathe Rostan, Véronique Baccini, Franck Peiretti, Marie Favier, Pauline Lucca, Jean-François Deleuze, Robert Olaso, Anne Boland, Pierre Emmanuel Morange, Christian Gachet, Fabrice Malergue, Sixtine Fauré, Anita Eckly, David-Alexandre Trégouët, Marjorie Poggi, and Marie-Christine Alessi. Macrothrombocytopenia and dense granule deficiency associated with fli1 variants: ultrastructural and pathogenic features. Haematologica, 102:1006-1016, Jun 2017. URL: https://doi.org/10.3324/haematol.2016.153577, doi:10.3324/haematol.2016.153577. This article has 64 citations.

18. (saultier2017macrothrombocytopeniaanddense pages 11-11): Paul Saultier, Léa Vidal, Matthias Canault, Denis Bernot, Céline Falaise, Catherine Pouymayou, Jean-Claude Bordet, Noémie Saut, Agathe Rostan, Véronique Baccini, Franck Peiretti, Marie Favier, Pauline Lucca, Jean-François Deleuze, Robert Olaso, Anne Boland, Pierre Emmanuel Morange, Christian Gachet, Fabrice Malergue, Sixtine Fauré, Anita Eckly, David-Alexandre Trégouët, Marjorie Poggi, and Marie-Christine Alessi. Macrothrombocytopenia and dense granule deficiency associated with fli1 variants: ultrastructural and pathogenic features. Haematologica, 102:1006-1016, Jun 2017. URL: https://doi.org/10.3324/haematol.2016.153577, doi:10.3324/haematol.2016.153577. This article has 64 citations.

## Artifacts

- [Edison artifact artifact-00](Bleeding_Disorder_Platelet-type_21-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. bury2021learningtheropes pages 15-17
2. saultier2017macrothrombocytopeniaanddense pages 1-2
3. saultier2017macrothrombocytopeniaanddense pages 5-7
4. saultier2017macrothrombocytopeniaanddense pages 9-10
5. rabbolini2016thrombocytopeniacausedby pages 6-7
6. bourguignon2022screeninganddiagnosis pages 1-3
7. bourguignon2022screeninganddiagnosis pages 10-12
8. bury2021learningtheropes pages 12-13
9. saultier2017macrothrombocytopeniaanddense pages 11-11
10. 10.3324/haematol.2024.286372
11. 10.3324/haematol.2016.153577
12. 10.1182/blood-2013-06-506873
13. 10.1080/10408363.2022.2049199
14. https://doi.org/10.3324/haematol.2024.286372
15. https://doi.org/10.3324/haematol.2016.153577
16. https://doi.org/10.1182/blood-2013-06-506873
17. https://doi.org/10.1080/10408363.2022.2049199
18. https://doi.org/10.3324/haematol.2024.286372,
19. https://doi.org/10.3324/haematol.2016.153577,
20. https://doi.org/10.33590/emjhematol/10314585,
21. https://doi.org/10.1182/blood-2013-06-506873,
22. https://doi.org/10.1080/10408363.2022.2049199,
23. https://doi.org/10.3390/jcm10030533,
24. https://doi.org/10.1182/blood-2017-02-770958,

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 7 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 7 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.
