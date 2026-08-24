---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-01T18:27:00.558813'
end_time: '2026-08-01T18:33:29.840748'
duration_seconds: 389.28
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Mucopolysaccharidosis-Plus Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 18
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Mucopolysaccharidosis-Plus_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Mucopolysaccharidosis-Plus Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Mucopolysaccharidosis-Plus Syndrome** covering all of the
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
- **Disease Name:** Mucopolysaccharidosis-Plus Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Mucopolysaccharidosis-Plus Syndrome** covering all of the
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


# Mucopolysaccharidosis-Plus Syndrome (MPSPS): Disease Characteristics Report

## Executive summary

Mucopolysaccharidosis-plus syndrome (MPSPS) is an ultra-rare, autosomal-recessive lysosomal/endolysosomal trafficking disorder caused by biallelic **VPS33A** variants. It resembles classical mucopolysaccharidoses because glycosaminoglycans (GAGs) accumulate and are excessively excreted, but differs fundamentally because activities of the known GAG-degrading lysosomal enzymes remain normal. The “plus” phenotype comprises particularly prominent congenital cardiac disease, nephrotic/renal disease, and hematologic abnormalities. The severe founder form, caused by **VPS33A c.1492C>T (p.Arg498Trp; R498W)**, usually begins in infancy and historically caused death from cardiorespiratory failure at approximately 10–20 months. A 2024 review counted **41 reported patients** and described two patients with **c.599G>C (p.Arg200Pro)** and a milder juvenile phenotype. Evidence remains dominated by small case series, patient fibroblasts, and reviews; there is no approved disease-modifying treatment or validated population-screening program. (vasilev2020mucopolysaccharidosisplussyndrome pages 5-9, cyske2024mucopolysaccharidosisplussyndromeis pages 1-2, cyske2024mucopolysaccharidosisplussyndromeis pages 2-3, pavlova2019thelysosomaldisease pages 7-10)

| domain | established finding | evidence type/strength | key ontology suggestions |
|---|---|---|---|
| Definition / classification | Mucopolysaccharidosis-plus syndrome (MPSPS) is an ultra-rare autosomal-recessive lysosomal/endolysosomal trafficking disorder with MPS-like glycosaminoglycan accumulation but without deficiency of known lysosomal GAG-degrading enzymes; reviews note debate over whether it is a true MPS subtype or a distinct metabolic disease (vasilev2020mucopolysaccharidosisplussyndrome pages 1-3, cyske2024mucopolysaccharidosisplussyndromeis pages 1-2) | Human disease review + mechanistic primary study; moderate-strong for disease definition, moderate for classification debate (vasilev2020mucopolysaccharidosisplussyndrome pages 1-3, cyske2024mucopolysaccharidosisplussyndromeis pages 1-2, pavlova2019thelysosomaldisease pages 7-10) | Lysosomal storage disease; endolysosomal transport disorder; possible MONDO term search: “mucopolysaccharidosis-plus syndrome”; GO: lysosomal transport, endosome organization |
| VPS33A variants and inheritance | Established severe infantile form is caused by homozygous VPS33A c.1492C>T (p.Arg498Trp / p.R498W); 2024 review additionally reports VPS33A c.599G>C (p.Arg200Pro) in 2 juvenile milder cases. Inheritance is autosomal recessive (vasilev2020mucopolysaccharidosisplussyndrome pages 1-3, cyske2024mucopolysaccharidosisplussyndromeis pages 2-3) | Human case series/reviews; strong for p.Arg498Trp, moderate for p.Arg200Pro pending broader replication (vasilev2020mucopolysaccharidosisplussyndrome pages 1-3, cyske2024mucopolysaccharidosisplussyndromeis pages 2-3) | HGNC: VPS33A; SO: missense_variant; inheritance: autosomal recessive inheritance |
| Epidemiology | By 2024, 41 patients had been described; strong founder effect in the Yakut population is reported, with most early cases from Yakutia and a birth incidence estimate of ~1 in 12,100 in Yakuts for p.Arg498Trp. Sex distribution in one 16-patient Yakut cohort was 8 female / 8 male (cyske2024mucopolysaccharidosisplussyndromeis pages 1-2, cyske2024mucopolysaccharidosisplussyndromeis pages 2-3, vasilev2020mucopolysaccharidosisplussyndrome pages 5-9) | Human cohort/review; moderate because numbers are small and literature is rapidly evolving (cyske2024mucopolysaccharidosisplussyndromeis pages 1-2, cyske2024mucopolysaccharidosisplussyndromeis pages 2-3, vasilev2020mucopolysaccharidosisplussyndrome pages 5-9) | Founder effect; rare disease; population of interest: Yakut/Sakha |
| Core phenotypes | Multisystem phenotype includes coarse facial features, short neck/nose, periorbital puffiness, macroglossia, growth deficiency, hepatosplenomegaly, dysostosis multiplex, kyphosis/lordosis, barrel chest, joint contractures/stiffness, clawed fingers, developmental delay/regression, hypotonia, nystagmus, recurrent respiratory infections, congenital heart disease, renal disease/nephrotic syndrome, and hematologic abnormalities including anemia, thrombocytopenia, neutropenia/coagulation defects (vasilev2020mucopolysaccharidosisplussyndrome pages 5-9, vasilev2020mucopolysaccharidosisplussyndrome pages 9-11, cyske2024mucopolysaccharidosisplussyndromeis pages 3-5, cyske2024mucopolysaccharidosisplussyndromeis pages 5-7) | Human case series and focused review; strong for infantile p.Arg498Trp phenotype (vasilev2020mucopolysaccharidosisplussyndrome pages 5-9, vasilev2020mucopolysaccharidosisplussyndrome pages 9-11) | HPO suggestions: Coarse facial features; Macroglossia; Dysostosis multiplex; Joint contracture; Hepatosplenomegaly; Developmental delay; Hypotonia; Nystagmus; Recurrent respiratory infections; Congenital heart defect; Nephrotic syndrome; Anemia; Thrombocytopenia; Neutropenia |
| Biomarkers / diagnosis | Characteristic laboratory pattern: elevated urinary GAGs, especially heparan sulfate and dermatan sulfate, with very high plasma heparan sulfate; additional reports note increased sialooligosaccharides/sialic acid. A key distinguishing feature is normal activities of known lysosomal enzymes for GAG degradation. Diagnosis is based on MPS-like clinical presentation plus biochemical findings and confirmatory molecular testing for VPS33A; prenatal diagnosis is reported as available (vasilev2020mucopolysaccharidosisplussyndrome pages 9-11, cyske2024mucopolysaccharidosisplussyndromeis pages 2-3) | Human clinical/biochemical evidence; strong for elevated GAGs with normal lysosomal enzyme assays (vasilev2020mucopolysaccharidosisplussyndrome pages 9-11, cyske2024mucopolysaccharidosisplussyndromeis pages 2-3) | HPO: Elevated urinary glycosaminoglycan; Proteinuria; Hypoalbuminemia; Delayed myelination. Diagnostic concepts: urine GAG analysis, plasma HS quantification, VPS33A sequencing |
| Mechanism | VPS33A is a core HOPS/CORVET subunit. p.Arg498Trp is predicted to destabilize VPS33A, reducing full-length VPS33A and other HOPS/CORVET components, causing disordered endolysosomal compartments, abnormal lactosylceramide trafficking, cholesterol/sphingolipid abnormalities, autophagy-endosomal dysfunction, and impaired intracellular handling of GAGs despite normal enzyme activities. Some mechanistic details remain uncertain (pavlova2019thelysosomaldisease pages 7-10, cyske2024mucopolysaccharidosisplussyndromeis pages 2-3, cyske2024mucopolysaccharidosisplussyndromeis pages 3-5) | Primary human fibroblast mechanistic study + focused review; strong for VPS33A instability/HOPS-CORVET depletion and trafficking defects, moderate for full causal chain to GAG accumulation (pavlova2019thelysosomaldisease pages 7-10, cyske2024mucopolysaccharidosisplussyndromeis pages 2-3, cyske2024mucopolysaccharidosisplussyndromeis pages 3-5) | GO suggestions: endocytic vesicle fusion; lysosomal transport; autophagosome-lysosome fusion; endosome organization. Cellular compartment: lysosome, late endosome, autophagosome |
| Prognosis / natural history | Typical severe p.Arg498Trp disease begins in early infancy with recurrent respiratory problems around 2–6 months and progresses rapidly; most reported patients died from cardiorespiratory failure at about 10–20 months. Juvenile cases linked to p.Arg200Pro appear milder/longer-surviving but remain very limited (vasilev2020mucopolysaccharidosisplussyndrome pages 5-9, vasilev2020mucopolysaccharidosisplussyndrome pages 9-11, cyske2024mucopolysaccharidosisplussyndromeis pages 2-3) | Human cohort/review; strong for poor prognosis of infantile founder variant, weak-moderate for variant-specific milder prognosis due to only 2 cases (vasilev2020mucopolysaccharidosisplussyndrome pages 5-9, vasilev2020mucopolysaccharidosisplussyndrome pages 9-11, cyske2024mucopolysaccharidosisplussyndromeis pages 2-3) | HPO suggestions: Infantile onset; Progressive course; Early death |
| Treatment | No approved disease-modifying therapy or relevant clinical trial was identified in retrieved evidence. Current management is supportive/symptomatic: respiratory support, antibiotics, oxygen, vitamins, ACE inhibitors, transfusions, and selected cardiac surgery. Experimental in vitro rescue of patient fibroblast defects has been reported with bortezomib and eliglustat; these findings are preclinical and should not be interpreted as established clinical therapy (vasilev2020mucopolysaccharidosisplussyndrome pages 9-11, pavlova2019thelysosomaldisease pages 7-10) | Human supportive-care evidence + preclinical cell data; strong that no specific established therapy exists, weak-moderate for translational promise of bortezomib/eliglustat because evidence is in vitro only (vasilev2020mucopolysaccharidosisplussyndrome pages 9-11, pavlova2019thelysosomaldisease pages 7-10) | NCIT-style intervention suggestions: Supportive care; Oxygen therapy; Anti-infective therapy; Blood transfusion; Cardiac surgical procedure; Proteasome inhibitor (experimental); Glucosylceramide synthase inhibitor (experimental) |


*Table: This table condenses the strongest available evidence for key disease-characteristic domains in mucopolysaccharidosis-plus syndrome. It separates established human findings from experimental or still-uncertain observations and suggests ontology mappings useful for knowledge-base curation.*

## 1. Disease information

### Definition and classification

MPSPS is a Mendelian, multisystem lysosomal storage/vesicular-trafficking disease. Unlike classical MPS, its primary defect is not a hydrolase deficiency but impaired intracellular membrane trafficking associated with deficient or unstable VPS33A and disturbed HOPS/CORVET function. Whether MPSPS should be classified as an MPS subtype or as a separate metabolic trafficking disorder remains debated. The most defensible current knowledge-base classification is **VPS33A-related lysosomal/endolysosomal trafficking disorder with MPS-like GAG storage**. (cyske2024mucopolysaccharidosisplussyndromeis pages 1-2, vasilev2020mucopolysaccharidosisplussyndrome pages 1-3, pavlova2019thelysosomaldisease pages 7-10)

A direct abstract statement from the 2024 focused review is: **“Patients with MPSPS exhibited excessive excretion of glycosaminoglycans (GAGs) in the urine and exceptionally high levels of heparan sulfate in the plasma, but the accumulation of substrates is not caused by a decrease in the activity of any lysosomal enzymes.”** (cyske2024mucopolysaccharidosisplussyndromeis pages 1-2)

### Names and identifiers

- Preferred name: **Mucopolysaccharidosis-plus syndrome**.
- Synonyms: **MPS-plus syndrome**, **MPSPS**, **MPS-PS**, **VPS33A-related mucopolysaccharidosis-plus syndrome**, and **lysosomal disease caused by mutant VPS33A**.
- **OMIM:** the focused 2020 review identifies the disease as **OMIM #617303**. One retrieved passage from the 2019 paper was indexed as #610034, which likely reflects a gene/disease-record conflation; **#617303 should therefore be used provisionally and independently verified in OMIM before production ingestion**. (vasilev2020mucopolysaccharidosisplussyndrome pages 1-3, pavlova2019thelysosomaldisease pages 7-10)
- **Gene location:** VPS33A, chromosome **12q24.31**; the founder variant is in exon 12. (vasilev2020mucopolysaccharidosisplussyndrome pages 1-3)
- **MONDO, Orphanet, MeSH, ICD-10/ICD-11:** no reliable disease-specific identifiers were recovered from the accessed primary literature. Do not infer them. Generic coding may fall under mucopolysaccharidosis or other lysosomal storage disorders, but that lacks MPSPS specificity.

The evidence is principally **aggregated disease-level literature**, derived from published case reports/series and experimental studies of patient-derived fibroblasts—not longitudinal EHR-scale cohorts.

## 2. Etiology

MPSPS is caused by **biallelic germline VPS33A variants** and follows autosomal-recessive inheritance. The best-established severe allele is **NM_022916.4:c.1492C>T, p.(Arg498Trp)**; transcript version should be verified in the reporting laboratory. The 2024 review states that this variant occurred in **39 of 41** reported patients and that two milder juvenile patients carried **c.599G>C, p.(Arg200Pro)**. Evidence for p.Arg498Trp is strong; p.Arg200Pro remains based on only two reported patients. (vasilev2020mucopolysaccharidosisplussyndrome pages 1-3, cyske2024mucopolysaccharidosisplussyndromeis pages 2-3)

The Yakut/Sakha enrichment is consistent with a **founder effect and geographic isolation**. The 2020 review reported an allele frequency of approximately **1:81** in the Yakut population; this should be interpreted as a population-specific estimate, not a global frequency. A 2024 review estimated incidence at approximately **1 per 12,100 births in Yakuts**. (vasilev2020mucopolysaccharidosisplussyndrome pages 1-3, cyske2024mucopolysaccharidosisplussyndromeis pages 2-3)

No environmental, infectious, dietary, occupational, sex-specific, or lifestyle cause is established. No protective genetic variants, environmental protective factors, modifier genes, or reproducible gene–environment interactions have been demonstrated. Viral or respiratory infections may precipitate clinical deterioration in affected children but are complications/triggers, not primary causes. Consanguinity is not required: the early 16-patient Yakut cohort included children of healthy, reportedly non-consanguineous parents. (vasilev2020mucopolysaccharidosisplussyndrome pages 5-9)

## 3. Phenotypes

The phenotype is progressive and multisystemic. Frequencies below are qualitative unless a denominator is explicitly available; publication bias and repeated reporting of the same patients preclude reliable pooled percentages.

### Craniofacial, skeletal, and growth manifestations

- Coarse facial features, prominent forehead, short nose/neck, periorbital puffiness, macroglossia, facial/limb edema, and loose skin.
- Growth deficiency/short stature.
- Dysostosis multiplex, barrel chest, kyphosis/lordosis, bullet-shaped phalanges, joint stiffness or contractures, clawed fingers, and frequent falls.
- Suggested HPO: **Coarse facial features (HP:0000280)**, **Macroglossia (HP:0000158)**, **Short stature (HP:0004322)**, **Dysostosis multiplex (HP:0000943)**, **Kyphosis (HP:0002808)**, **Joint contracture (HP:0001371)**. (cyske2024mucopolysaccharidosisplussyndromeis pages 3-5, cyske2024mucopolysaccharidosisplussyndromeis pages 5-7, vasilev2020mucopolysaccharidosisplussyndrome pages 5-9)

### Neurologic and developmental manifestations

Developmental delay or regression, psychomotor retardation, hypotonia, cognitive impairment, poor memory/concentration, autistic features, nystagmus, hydrocephalus, and delayed speech have been reported. Milestones in longer-surviving cases included sitting at 10–13 months, walking at 22–28 months, and delayed speech. MRI/CT findings include delayed myelination, cerebral/cerebellar abnormalities, global atrophy, and basal-ganglia or other intracranial calcification. Suggested HPO: **Global developmental delay (HP:0001263)**, **Developmental regression (HP:0002376)**, **Hypotonia (HP:0001252)**, **Delayed CNS myelination (HP:0002188)**, **Brain atrophy (HP:0012444)**, **Nystagmus (HP:0000639)**. (vasilev2020mucopolysaccharidosisplussyndrome pages 9-11, cyske2024mucopolysaccharidosisplussyndromeis pages 5-7, vasilev2020mucopolysaccharidosisplussyndrome pages 5-9)

### Respiratory and infectious manifestations

Recurrent upper/lower respiratory infections, bronchial obstruction, dyspnea, and progressive respiratory failure are prominent. In the early cohort, respiratory symptoms commonly emerged at **2–6 months**. Suggested HPO: **Recurrent respiratory infections (HP:0002205)**, **Dyspnea (HP:0002094)**, **Bronchial obstruction**, and **Respiratory failure (HP:0002878)**. (vasilev2020mucopolysaccharidosisplussyndrome pages 5-9)

### Cardiovascular manifestations

Congenital heart disease includes atrial septal defect, patent foramen ovale, valve regurgitation/insufficiency, and pulmonary hypertension. Cardiac disease may progress substantially over only 3–4 months and contributes to early mortality. Suggested HPO: **Congenital heart defect (HP:0001627)**, **Atrial septal defect (HP:0001631)**, **Pulmonary hypertension (HP:0002092)**, and valve-regurgitation terms. (vasilev2020mucopolysaccharidosisplussyndrome pages 9-11, vasilev2020mucopolysaccharidosisplussyndrome pages 5-9)

### Renal manifestations

Renal disease is one of the most discriminating “plus” features. Reports describe nephromegaly, nephrotic syndrome, marked proteinuria, hypoalbuminemia, elevated creatinine and uric acid, calcium deficiency, and occasional tubular disease. Histopathology includes glomerular destruction, periglomerular fibrosis, interstitial inflammation, and foam cells in podocytes. Suggested HPO: **Nephrotic syndrome (HP:0000100)**, **Proteinuria (HP:0000093)**, **Hypoalbuminemia (HP:0003073)**, **Nephromegaly (HP:0000105)**, and **Renal insufficiency (HP:0000083)**. (pavlova2019thelysosomaldisease pages 7-10, cyske2024mucopolysaccharidosisplussyndromeis pages 8-10)

### Hematologic and immune manifestations

Normocytic anemia, thrombocytopenia, neutropenia/leukopenia, coagulation abnormalities, hypogammaglobulinemia, and hypoplastic marrow have been reported. Suggested HPO: **Anemia (HP:0001903)**, **Thrombocytopenia (HP:0001873)**, **Neutropenia (HP:0001875)**, **Abnormality of coagulation (HP:0001928)**, and **Hypogammaglobulinemia (HP:0004313)**. (vasilev2020mucopolysaccharidosisplussyndrome pages 9-11, cyske2024mucopolysaccharidosisplussyndromeis pages 3-5, cyske2024mucopolysaccharidosisplussyndromeis pages 5-7)

### Other manifestations and functional impact

Hepatomegaly/hepatosplenomegaly, subclinical hypothyroidism, retinal hypopigmentation, and peripheral or retrocochlear hearing impairment occur. Suggested HPO: **Hepatomegaly (HP:0002240)**, **Splenomegaly (HP:0001744)**, **Hypothyroidism (HP:0000821)**, and **Hearing impairment (HP:0000365)**. (cyske2024mucopolysaccharidosisplussyndromeis pages 8-10, cyske2024mucopolysaccharidosisplussyndromeis pages 5-7)

No validated MPSPS-specific EQ-5D, SF-36, PROMIS, caregiver-burden, or health-utility data were found. Nevertheless, developmental impairment, severe cardiorespiratory disease, recurrent hospitalization/infection, mobility limitation, transfusion requirements, and very early mortality imply profound effects on child and family quality of life.

## 4. Genetic and molecular information

**Causal gene:** **VPS33A**, encoding a 596-amino-acid, approximately 67-kDa Sec1/Munc18-family protein and core component of both HOPS and CORVET tethering complexes. (cyske2024mucopolysaccharidosisplussyndromeis pages 2-3)

**Pathogenic variants:**

1. **c.1492C>T; p.Arg498Trp (R498W)**—homozygous missense, germline, severe infantile phenotype. Structural modeling predicts destabilized folding; patient cells show reduced full-length VPS33A and secondary reduction of VPS18/VPS41 and other complex components. Functional consequence is best described as **hypomorphic loss of function through protein instability/proteasomal degradation**, rather than gain of function or dominant-negative activity. (vasilev2020mucopolysaccharidosisplussyndrome pages 1-3, pavlova2019thelysosomaldisease pages 7-10)
2. **c.599G>C; p.Arg200Pro**—homozygous missense reported in two juvenile patients with milder, longer-surviving disease. Classification and population frequency should be checked directly in ClinVar/gnomAD before clinical use. (cyske2024mucopolysaccharidosisplussyndromeis pages 2-3)

Global gnomAD/TOPMed/1000 Genomes frequencies, ClinVar review status, HGNC numerical identifier, and ACMG evidence codes were not recoverable from the accessed literature. Both are constitutional/germline variants; no somatic etiology is implicated. No established modifier genes, epigenetic signature, methylation abnormality, chromosomal rearrangement, CNV, anticipation, or germline mosaicism has been documented.

## 5. Environmental information

MPSPS is monogenic. There is no evidence that toxins, radiation, air pollution, smoking, alcohol, diet, exercise, occupation, or infectious agents cause the disorder. Respiratory infections are frequent complications and can worsen cardiorespiratory status. Routine vaccination and infection avoidance are reasonable supportive measures, but neither prevents the inherited molecular defect.

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream genetic lesion:** biallelic VPS33A missense variant.
2. **Protein-level defect:** p.Arg498Trp destabilizes VPS33A folding and promotes proteasomal degradation.
3. **Complex instability:** reduced VPS33A lowers HOPS/CORVET components such as VPS18 and VPS41.
4. **Cellular trafficking dysfunction:** late endosomal/lysosomal compartment organization and lipid cargo trafficking become abnormal; patient fibroblasts show vacuolation and defective lactosylceramide trafficking.
5. **Metabolic storage:** heparan, dermatan, and chondroitin sulfates accumulate despite normal cognate lysosomal hydrolases; sialylated conjugates, cholesterol, sphingolipids, β-D-galactosylsphingosine/psychosine, and deacylated galactosylceramide abnormalities have also been reported.
6. **Downstream injury:** lysosomal/endosomal stress, altered lipid/GAG homeostasis, probable autophagic dysfunction, inflammation/fibrosis, and cell-type-specific injury produce dysostosis, myelin/neurologic injury, nephrotic disease, cytopenias, cardiac disease, and respiratory failure. The precise link between trafficking failure and GAG accumulation remains incompletely resolved. (cyske2024mucopolysaccharidosisplussyndromeis pages 2-3, pavlova2019thelysosomaldisease pages 7-10, cyske2024mucopolysaccharidosisplussyndromeis pages 3-5, cyske2024mucopolysaccharidosisplussyndromeis pages 8-10)

The 2019 primary-study abstract states that patient fibroblasts showed **“vacuolation with disordered endosomal/lysosomal compartments”**, while the p.Arg498Trp replacement was predicted to **“de-stabilize VPS33A folding.”** It further proposed that disease results from **“diminished intracellular abundance of intact VPS33A.”** (pavlova2019thelysosomaldisease pages 7-10)

Suggested GO terms include **vesicle-mediated transport (GO:0016192)**, **endosome organization (GO:0007032)**, **lysosomal transport (GO:0007041)**, **endosome-to-lysosome transport (GO:0008333)**, **autophagosome–lysosome fusion**, and **regulation of macroautophagy (GO:0016241)**. Relevant compartments include **lysosome (GO:0005764)**, **late endosome (GO:0005770)**, **autophagosome (GO:0005776)**, HOPS, and CORVET complexes.

### Evidence boundaries

The strongest MPSPS-specific mechanistic evidence comes from structural modeling, biochemical assays, lipidomics, microscopy, and trafficking assays in patient fibroblasts. Broad transcriptomic, single-cell, spatial-transcriptomic, proteomic, epigenomic, CRISPR-screen, and multi-omics maps specific to MPSPS were not found. General MPS transcriptomic findings should not be automatically transferred to MPSPS.

## 7. Anatomical structures affected

Primary systems include:

- **Kidney:** glomeruli, podocytes, tubulointerstitium; UBERON suggestions: kidney (**UBERON:0002113**), renal glomerulus (**UBERON:0000074**). Candidate CL terms: **podocyte (CL:0000653)** and renal tubular epithelial cell.
- **Heart and pulmonary vasculature:** valves, septa, myocardium, pulmonary arteries; heart (**UBERON:0000948**).
- **Respiratory tract/lung:** bronchi and lungs; lung (**UBERON:0002048**).
- **Skeleton/connective tissue:** vertebral column, ribs, long bones, hands, joints, cartilage; bone tissue (**UBERON:0002481**) and articular cartilage.
- **CNS and peripheral nervous system:** cerebral white matter, basal ganglia, cerebellum, peripheral nerves; brain (**UBERON:0000955**), cerebral white matter (**UBERON:0002437**). Candidate cells include oligodendrocytes (**CL:0000128**) and neurons, although direct MPSPS cell-specific proof is limited.
- **Liver/spleen and hematopoietic tissues:** liver (**UBERON:0002107**), spleen (**UBERON:0002106**), bone marrow (**UBERON:0002371**); erythroid, megakaryocytic, and neutrophil lineages.

Subcellular localization centers on endosomes, lysosomes, autophagosomes, and HOPS/CORVET-associated membrane-fusion machinery. Findings are generally bilateral/systemic rather than lateralized. (vasilev2020mucopolysaccharidosisplussyndrome pages 9-11, cyske2024mucopolysaccharidosisplussyndromeis pages 8-10, cyske2024mucopolysaccharidosisplussyndromeis pages 5-7)

## 8. Temporal development

Prenatal findings can include ascites from approximately **11–24 weeks**, congenital cardiac abnormalities/valve regurgitation, and increased nuchal, nasal, or prenasal thickness. Many affected newborns are delivered at term with normal Apgar scores, followed by an insidious but rapidly progressive infantile course. (vasilev2020mucopolysaccharidosisplussyndrome pages 5-9, cyske2024mucopolysaccharidosisplussyndromeis pages 5-7)

For p.Arg498Trp disease, respiratory and systemic manifestations generally become evident in the first months, often at 2–6 months. Cardiac, renal, skeletal, hematologic, and neurodevelopmental disease then progresses, with death commonly at 10–20 months. Disease is lifelong and progressive; spontaneous remission is not established. p.Arg200Pro may produce a juvenile, slower phenotype, but evidence is too sparse to define stages reliably. (vasilev2020mucopolysaccharidosisplussyndrome pages 5-9, cyske2024mucopolysaccharidosisplussyndromeis pages 2-3)

The critical intervention window is likely prenatal or very early infancy because irreversible organ injury develops rapidly. This is a biologically plausible expert inference, not a demonstrated treatment-window statistic.

## 9. Inheritance and population

Inheritance is **autosomal recessive**. For two heterozygous parents, each pregnancy has the standard Mendelian probabilities of 25% affected, 50% carrier, and 25% unaffected/non-carrier, assuming no unusual reproductive mechanism. Penetrance of homozygous p.Arg498Trp appears high in reported families, but formal age-dependent penetrance estimates do not exist. Expressivity varies, especially between p.Arg498Trp and p.Arg200Pro. Anticipation is not expected and has not been observed. Germline mosaicism has not been reported but cannot be excluded as a general counseling possibility.

By September 2024, **41 patients** had been described. Earlier data included 17 Yakut and two Turkish patients, while the foundational 16-patient Yakut series had an equal sex distribution—eight girls and eight boys—consistent with autosomal inheritance. There is a marked Yakut/Sakha founder concentration, with additional Turkish, Mediterranean, and Polish-origin cases. Global prevalence, annual incidence, carrier frequency, and sex ratio are unknown. (cyske2024mucopolysaccharidosisplussyndromeis pages 1-2, vasilev2020mucopolysaccharidosisplussyndrome pages 1-3, cyske2024mucopolysaccharidosisplussyndromeis pages 2-3, vasilev2020mucopolysaccharidosisplussyndrome pages 5-9)

## 10. Diagnostics

### Recommended diagnostic workflow

1. **Clinical suspicion:** early MPS-like facies, dysostosis, hepatosplenomegaly, developmental delay, and recurrent respiratory disease combined with congenital heart disease, nephrotic syndrome/proteinuria, or cytopenias.
2. **Urine/plasma biochemistry:** quantify urinary total GAGs and characterize fractions by electrophoresis or LC-MS/MS. Elevated urinary heparan and dermatan sulfate—and sometimes chondroitin sulfate—plus exceptionally elevated plasma heparan sulfate support MPSPS. Sialooligosaccharides/sialic acid may also be increased. (vasilev2020mucopolysaccharidosisplussyndrome pages 9-11, cyske2024mucopolysaccharidosisplussyndromeis pages 2-3, cyske2024mucopolysaccharidosisplussyndromeis pages 3-5)
3. **Lysosomal enzyme panel:** demonstrate normal activities of known GAG-degrading enzymes. This is a defining discriminator from classical MPS but does not independently establish MPSPS. (cyske2024mucopolysaccharidosisplussyndromeis pages 1-2, cyske2024mucopolysaccharidosisplussyndromeis pages 2-3)
4. **Molecular confirmation:** sequence **VPS33A**, initially by targeted testing for p.Arg498Trp in Yakut families or known familial variants. Otherwise use a lysosomal-storage/vesicular-trafficking panel or WES/WGS, with deletion/duplication analysis if sequencing is nondiagnostic.
5. **Functional assessment when necessary:** VPS33A abundance, HOPS/CORVET proteins, trafficking assays, or RNA/protein studies in fibroblasts may help resolve a VUS, but these are research-level tests.

WES identified the disorder historically and is appropriate when the phenotype is atypical. WGS may detect noncoding or structural lesions but has no demonstrated MPSPS-specific yield advantage. CMA, karyotyping, FISH, mitochondrial sequencing, and repeat-expansion testing are not first-line unless another diagnosis is suspected.

### Organ evaluation

Recommended baseline studies, guided by reported manifestations, include CBC/differential, coagulation profile, immunoglobulins, creatinine/electrolytes, albumin, urinalysis and urine protein quantification; ECG and echocardiography; chest/airway and pulmonary assessment; skeletal survey; brain MRI and hearing/ophthalmologic evaluation; abdominal and renal ultrasonography. Renal biopsy is not required for genetic diagnosis but can characterize unexplained nephrotic disease.

### Differential diagnosis

Classical MPS I, II, III, IV, VI, VII, IX/X; mucolipidoses; oligosaccharidoses/sialidosis; Niemann–Pick disease; Gaucher disease; Krabbe disease; and other HOPS/CORVET-subunit disorders—especially biallelic **VPS16** disease—should be considered. The combination of MPS-like storage, normal lysosomal hydrolase activities, severe renal/hematologic disease, and biallelic VPS33A variants is distinguishing. (vasilev2020mucopolysaccharidosisplussyndrome pages 9-11, cyske2024mucopolysaccharidosisplussyndromeis pages 8-10, sofou2021bi‐allelicvps16variants pages 2-3)

### Prenatal and screening applications

Targeted prenatal diagnosis through chorionic-villus or amniotic-fluid DNA is feasible when familial variants are known. A 2023 publication specifically reported prenatal diagnosis of MPSPS, although its full text was unavailable in the retrieved corpus. Preimplantation genetic testing for monogenic disease is conceptually available. There is no established universal newborn-screening program or validated DBS enzyme assay, because the defining defect is not a missing GAG hydrolase. Cascade testing and targeted carrier screening are most relevant in Yakut families and communities with known founder ancestry. (vasilev2020mucopolysaccharidosisplussyndrome pages 9-11, lipinski2025mucopolysaccharidoses—whatcliniciansneed pages 12-13)

## 11. Outcome and prognosis

The p.Arg498Trp infantile phenotype has a very poor prognosis. In early series, most children died from **cardiorespiratory failure at 10–20 months**. No valid five- or ten-year survival curves, mortality rates per person-year, or treatment-stratified life-expectancy estimates exist. (vasilev2020mucopolysaccharidosisplussyndrome pages 5-9, vasilev2020mucopolysaccharidosisplussyndrome pages 9-11)

Major morbidity includes developmental disability/regression, impaired mobility, skeletal deformity, recurrent infections, respiratory insufficiency, congenital/progressive cardiac disease, nephrotic syndrome/renal failure, and cytopenias. Recovery is not expected without correction of the molecular defect; supportive interventions can transiently stabilize complications. Likely adverse prognostic factors include p.Arg498Trp genotype, early cardiorespiratory involvement, pulmonary hypertension, nephrotic disease, and severe hematologic dysfunction, but no validated prognostic model or biomarker exists. Plasma/urine GAGs and proteinuria are candidate monitoring biomarkers, not validated surrogate endpoints.

## 12. Treatment

### Current real-world management

There is **no approved disease-modifying therapy**. Care is multidisciplinary and supportive:

- airway clearance/bronchial drainage, oxygen and ventilatory support where required;
- prompt antibiotics for bacterial respiratory infections;
- nutritional and developmental support;
- ACE inhibitors or other standard cardiac/renal management when indicated;
- red-cell or platelet transfusion for clinically significant cytopenia;
- selected corrective/palliative cardiac surgery;
- physical, occupational, speech, and respiratory therapy;
- hearing, vision, renal, cardiac, pulmonary, and hematologic surveillance. (vasilev2020mucopolysaccharidosisplussyndrome pages 9-11)

Suggested NCIT intervention concepts include **Supportive Care**, **Oxygen Therapy**, **Antibiotic Therapy**, **Blood Transfusion**, **Physical Therapy**, **Occupational Therapy**, **Speech Therapy**, and **Cardiac Surgical Procedure**. Exact NCIT codes should be resolved against the current NCIt release rather than inferred.

A prolonged corticosteroid course was reported in a single child in 2022 with a claimed favorable clinical impact, but the full article was not retrievable here and this does not establish efficacy. Steroids should not be represented as standard therapy.

### Experimental approaches

In patient-derived fibroblasts, the proteasome inhibitor **bortezomib** increased/rescued mutant protein and the glucosylceramide-synthase inhibitor **eliglustat** partially corrected abnormal lactosylceramide trafficking; the reported eliglustat concentration was 50 nM. These are **in vitro observations only**, not evidence of clinical safety or benefit in infants with MPSPS. Bortezomib’s toxicity and eliglustat’s indication-specific pharmacology make off-label use unsupported outside formal research. (pavlova2019thelysosomaldisease pages 7-10)

The primary paper’s abstract states: **“Exposure of patient-derived fibroblasts to the clinically approved proteasome inhibitor, bortezomib, or inhibition of glucosylceramide synthesis with eliglustat, partially corrected the impaired lactosylceramide trafficking defect.”** (pavlova2019thelysosomaldisease pages 7-10)

No MPSPS-specific enzyme-replacement therapy is logical at present because no single hydrolase is deficient. No clinical evidence supports hematopoietic stem-cell transplantation, AAV gene therapy, lentiviral therapy, CRISPR editing, ASOs, siRNA, or mRNA therapy. These remain conceptual strategies. The clinical-trial search found **no relevant registered MPSPS interventional trial**.

## 13. Prevention

Primary lifestyle or environmental prevention is not possible. Prevention is reproductive/genetic:

- identify carriers through cascade testing and targeted founder-variant testing;
- provide nondirective genetic counseling;
- offer prenatal diagnosis or PGT-M when parental variants are known;
- consider community-tailored carrier screening in high-risk Yakut/Sakha populations, subject to local consent, ethics, and health-system validation.

Secondary prevention consists of early molecular diagnosis and rapid surveillance for cardiac, renal, respiratory, and hematologic complications. Tertiary prevention includes vaccination according to routine schedules, prompt infection treatment, respiratory support, renal/cardiac management, transfusion support, rehabilitation, and avoidance of nephrotoxic or respiratory-depressant exposures when possible. No vaccine or prophylactic drug prevents MPSPS itself.

## 14. Other species and natural disease

No naturally occurring VPS33A-related MPSPS was identified in companion animals, livestock, or wildlife. Therefore, no veterinary breed association, VBO term, zoonotic potential, or cross-species transmission applies. VPS33A is evolutionarily conserved and HOPS/CORVET membrane-fusion biology is conserved across eukaryotes, but conservation alone is not evidence of natural animal disease.

## 15. Model organisms and experimental systems

### MPSPS-specific systems

The principal disease model is **patient-derived skin fibroblasts**, which reproduce VPS33A depletion, reduction of HOPS/CORVET components, vacuolated/disordered endolysosomal compartments, abnormal lactosylceramide trafficking, and lipid/GAG abnormalities. HeLa cells expressing mutant VPS33A have been used to show proteasomal degradation and pharmacologic rescue. These systems are valuable for trafficking, protein-stability, lipidomic, and drug-screen studies but do not reproduce organ-level cardiopulmonary, renal, skeletal, or neurodevelopmental disease. (pavlova2019thelysosomaldisease pages 7-10)

### Related—not equivalent—models

A biallelic **VPS16** MPS-like disorder provides mechanistically related evidence: patient fibroblasts had reduced HOPS/CORVET subunits, defective transferrin uptake, and lysosome/autophagosome accumulation, rescued by VPS16 re-expression. Disrupted **vps16** in zebrafish caused impaired development/myelination and lysosome/autophagosome accumulation, especially in glia. This supports HOPS/CORVET biology but is **not a VPS33A MPSPS model**. (sofou2021bi‐allelicvps16variants pages 2-3)

No well-validated VPS33A p.Arg498Trp knock-in mouse, rat, zebrafish, Drosophila, organoid, or iPSC model that recapitulates the full human syndrome was identified in the retrieved literature. Developing knock-in and patient-iPSC models is a high research priority.

## Evidence appraisal and recent developments

The most important 2023–2024 development is expansion from 19 known patients in the 2020 review to **41 by 2024**, together with recognition of **p.Arg200Pro-associated juvenile disease**, prenatal-diagnosis implementation, and a sharper mechanistic distinction between enzyme-deficient classical MPS and a trafficking-deficient MPS-like disorder. (cyske2024mucopolysaccharidosisplussyndromeis pages 1-2, vasilev2020mucopolysaccharidosisplussyndrome pages 1-3, cyske2024mucopolysaccharidosisplussyndromeis pages 2-3)

Authoritative expert interpretation in the 2024 review is that the nosology remains unsettled: GAG storage argues for inclusion among MPS, whereas normal lysosomal GAG-hydrolase activity and primary vesicle-trafficking dysfunction argue for a separate metabolic disease. For knowledge-base purposes, both relationships should be represented rather than forcing a single unqualified parent class. (cyske2024mucopolysaccharidosisplussyndromeis pages 1-2)

### Key sources and publication details

1. **Cyske Z, et al.** “Mucopolysaccharidosis-Plus Syndrome: Is This a Type of Mucopolysaccharidosis or a Separate Kind of Metabolic Disease?” *International Journal of Molecular Sciences*. Published September 2024. DOI/URL: https://doi.org/10.3390/ijms25179570. Focused current review; patient count, second variant, phenotype and mechanistic synthesis. (cyske2024mucopolysaccharidosisplussyndromeis pages 1-2, cyske2024mucopolysaccharidosisplussyndromeis pages 2-3)
2. **Vasilev F, Sukhomyasova A, Otomo T.** “Mucopolysaccharidosis-Plus Syndrome.” *International Journal of Molecular Sciences*. Published January 9, 2020. DOI/URL: https://doi.org/10.3390/ijms21020421. Foundational disease review and clinical summary. (vasilev2020mucopolysaccharidosisplussyndrome pages 5-9, vasilev2020mucopolysaccharidosisplussyndrome pages 1-3)
3. **Pavlova EV, et al.** “The lysosomal disease caused by mutant VPS33A.” *Human Molecular Genetics*. Published online April 2019; 28:2514–2530. DOI/URL: https://doi.org/10.1093/hmg/ddz077. Primary human-fibroblast, structural, lipidomic, and pharmacologic study. (pavlova2019thelysosomaldisease pages 7-10)
4. **Sofou K, et al.** “Bi-allelic VPS16 variants limit HOPS/CORVET levels and cause a mucopolysaccharidosis-like disease.” *EMBO Molecular Medicine*. Published May 2021. DOI/URL: https://doi.org/10.15252/emmm.202013376. Related HOPS/CORVET disease and zebrafish evidence, not MPSPS itself. (sofou2021bi‐allelicvps16variants pages 2-3)

**Important limitations:** The literature is very small, reported cohorts overlap, phenotype frequencies are not consistently denominated, and several recent reports were unavailable in full text. PMID values were not exposed by the retrieved records and therefore are not fabricated here; DOI URLs are supplied instead. Database identifiers, ClinVar classifications, transcript accessions, allele frequencies, and ontology codes should undergo direct database validation before production release.

References

1. (vasilev2020mucopolysaccharidosisplussyndrome pages 5-9): Filipp Vasilev, Aitalina Sukhomyasova, and Takanobu Otomo. Mucopolysaccharidosis-plus syndrome. International Journal of Molecular Sciences, 21:421, Jan 2020. URL: https://doi.org/10.3390/ijms21020421, doi:10.3390/ijms21020421. This article has 47 citations.

2. (cyske2024mucopolysaccharidosisplussyndromeis pages 1-2): Zuzanna Cyske, Lidia Gaffke, Karolina Pierzynowska, and Grzegorz Węgrzyn. Mucopolysaccharidosis-plus syndrome: is this a type of mucopolysaccharidosis or a separate kind of metabolic disease? International Journal of Molecular Sciences, 25:9570, Sep 2024. URL: https://doi.org/10.3390/ijms25179570, doi:10.3390/ijms25179570. This article has 13 citations.

3. (cyske2024mucopolysaccharidosisplussyndromeis pages 2-3): Zuzanna Cyske, Lidia Gaffke, Karolina Pierzynowska, and Grzegorz Węgrzyn. Mucopolysaccharidosis-plus syndrome: is this a type of mucopolysaccharidosis or a separate kind of metabolic disease? International Journal of Molecular Sciences, 25:9570, Sep 2024. URL: https://doi.org/10.3390/ijms25179570, doi:10.3390/ijms25179570. This article has 13 citations.

4. (pavlova2019thelysosomaldisease pages 7-10): Elena V Pavlova, Aleksey Shatunov, Lena Wartosch, Alena I Moskvina, Lena E Nikolaeva, Nicholas A Bright, Karen L Tylee, Heather J Church, Andrea Ballabio, J Paul Luzio, and Timothy M Cox. The lysosomal disease caused by mutant vps33a. Human Molecular Genetics, 28:2514-2530, Apr 2019. URL: https://doi.org/10.1093/hmg/ddz077, doi:10.1093/hmg/ddz077. This article has 42 citations and is from a domain leading peer-reviewed journal.

5. (vasilev2020mucopolysaccharidosisplussyndrome pages 1-3): Filipp Vasilev, Aitalina Sukhomyasova, and Takanobu Otomo. Mucopolysaccharidosis-plus syndrome. International Journal of Molecular Sciences, 21:421, Jan 2020. URL: https://doi.org/10.3390/ijms21020421, doi:10.3390/ijms21020421. This article has 47 citations.

6. (vasilev2020mucopolysaccharidosisplussyndrome pages 9-11): Filipp Vasilev, Aitalina Sukhomyasova, and Takanobu Otomo. Mucopolysaccharidosis-plus syndrome. International Journal of Molecular Sciences, 21:421, Jan 2020. URL: https://doi.org/10.3390/ijms21020421, doi:10.3390/ijms21020421. This article has 47 citations.

7. (cyske2024mucopolysaccharidosisplussyndromeis pages 3-5): Zuzanna Cyske, Lidia Gaffke, Karolina Pierzynowska, and Grzegorz Węgrzyn. Mucopolysaccharidosis-plus syndrome: is this a type of mucopolysaccharidosis or a separate kind of metabolic disease? International Journal of Molecular Sciences, 25:9570, Sep 2024. URL: https://doi.org/10.3390/ijms25179570, doi:10.3390/ijms25179570. This article has 13 citations.

8. (cyske2024mucopolysaccharidosisplussyndromeis pages 5-7): Zuzanna Cyske, Lidia Gaffke, Karolina Pierzynowska, and Grzegorz Węgrzyn. Mucopolysaccharidosis-plus syndrome: is this a type of mucopolysaccharidosis or a separate kind of metabolic disease? International Journal of Molecular Sciences, 25:9570, Sep 2024. URL: https://doi.org/10.3390/ijms25179570, doi:10.3390/ijms25179570. This article has 13 citations.

9. (cyske2024mucopolysaccharidosisplussyndromeis pages 8-10): Zuzanna Cyske, Lidia Gaffke, Karolina Pierzynowska, and Grzegorz Węgrzyn. Mucopolysaccharidosis-plus syndrome: is this a type of mucopolysaccharidosis or a separate kind of metabolic disease? International Journal of Molecular Sciences, 25:9570, Sep 2024. URL: https://doi.org/10.3390/ijms25179570, doi:10.3390/ijms25179570. This article has 13 citations.

10. (sofou2021bi‐allelicvps16variants pages 2-3): Kalliopi Sofou, Kolja Meier, Leslie E Sanderson, Debora Kaminski, Laia Montoliu‐Gaya, Emma Samuelsson, Maria Blomqvist, Lotta Agholme, Jutta Gärtner, Chris Mühlhausen, Niklas Darin, Tahsin Stefan Barakat, Lars Schlotawa, Tjakko van Ham, Jorge Asin Cayuela, and Fredrik H Sterky. Bi‐allelic vps16 variants limit hops/corvet levels and cause a mucopolysaccharidosis‐like disease. EMBO Molecular Medicine, May 2021. URL: https://doi.org/10.15252/emmm.202013376, doi:10.15252/emmm.202013376. This article has 36 citations and is from a highest quality peer-reviewed journal.

11. (lipinski2025mucopolysaccharidoses—whatcliniciansneed pages 12-13): Patryk Lipiński, Agnieszka Różdżyńska-Świątkowska, Karolina Wiśniewska, Joanna Rusecka, Agnieszka Ługowska, Zbigniew Żuber, Aleksandra Jezela-Stanek, Zuzanna Cyske, Lidia Gaffke, Karolina Pierzynowska, Grzegorz Węgrzyn, and Anna Tylki-Szymańska. Mucopolysaccharidoses—what clinicians need to know: a clinical, biochemical, and molecular overview. Biomolecules, 15:1448, Oct 2025. URL: https://doi.org/10.3390/biom15101448, doi:10.3390/biom15101448. This article has 9 citations.

## Artifacts

- [Edison artifact artifact-00](Mucopolysaccharidosis-Plus_Syndrome-deep-research-falcon_artifacts/artifact-00.md)