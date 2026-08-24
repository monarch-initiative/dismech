---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-01T18:21:53.153019'
end_time: '2026-08-01T18:32:39.625834'
duration_seconds: 646.47
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: KDM1A-Related Neurodevelopmental Disorder
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 21
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: KDM1A-Related_Neurodevelopmental_Disorder-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** KDM1A-Related Neurodevelopmental Disorder
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **KDM1A-Related Neurodevelopmental Disorder** covering all of the
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
- **Disease Name:** KDM1A-Related Neurodevelopmental Disorder
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **KDM1A-Related Neurodevelopmental Disorder** covering all of the
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


# KDM1A-Related Neurodevelopmental Disorder: Disease Characteristics Report

## Executive summary

**KDM1A-related neurodevelopmental disorder (KDM1A-RD)** is an ultra-rare, autosomal-dominant chromatin disorder caused by heterozygous germline variants in **KDM1A**, which encodes lysine-specific demethylase 1A (LSD1). The historical name is **cleft palate, psychomotor retardation, and distinctive facial features syndrome (CPRF syndrome; OMIM 616728)**. Its core manifestations are congenital or early-childhood hypotonia, global developmental delay, variable intellectual disability, and craniofacial dysmorphism. Cleft palate is characteristic but not obligatory: it occurred in the three original detailed patients but was absent in the fourth detailed case, published in 2025. The evidence base remains exceptionally small, preventing reliable prevalence, penetrance, prognosis, or phenotype-frequency estimates beyond this four-person series. (burkart2025phenotypicalandgenotypical pages 2-2, burkart2025phenotypicalandgenotypical pages 1-2, burkart2025phenotypicalandgenotypical pages 4-4)

The best-supported molecular mechanism is disruption of FAD-dependent histone demethylation and transcriptional regulation. Three original active-site variants markedly reduced enzyme activity, while newer experimental work shows that KDM1A is also required for neurogenesis, neurite architecture, memory-associated transcription, and maintenance of neuronal chromatin boundaries. No disease-modifying therapy or KDM1A-RD-specific clinical trial was identified; care is presently supportive and phenotype directed. (pilotto2016lsd1kdm1amutationsassociated pages 2-3, wilson2022reprogrammingofthe pages 17-19, blanco2024kdm1asafeguardsthe pages 1-2, burkart2025phenotypicalandgenotypical pages 2-2)

| Domain | Established finding | Evidence type/strength | Knowledge-base annotation |
|---|---|---|---|
| Disease ID/name | KDM1A-related neurodevelopmental disorder; CPRF syndrome; OMIM #616728. Unsupported identifiers (e.g., MONDO/Orphanet/ICD/MeSH) not confirmed here and therefore omitted. (wilson2022reprogrammingofthe pages 17-19, burkart2025phenotypicalandgenotypical pages 1-2) | Human disease literature + review support; moderate | Preferred label: **KDM1A-related neurodevelopmental disorder**; synonym: **CPRF syndrome**; OMIM: **616728** |
| Inheritance | Autosomal dominant, with reported detailed cases caused by **de novo heterozygous missense** variants in KDM1A. (burkart2025phenotypicalandgenotypical pages 2-2, pilotto2016lsd1kdm1amutationsassociated pages 2-3) | Human genetic evidence; moderate | Inheritance: **AD**; allelic origin: **germline, typically de novo** |
| Known detailed patient count | **4 detailed patients** are supported in the retrieved evidence set: 3 earlier detailed patients/functionally studied in 2016, plus 1 additional detailed case published in **2025** (latest available, outside the user’s 2023-2024 priority window). Four more ClinVar variants are mentioned without detailed phenotypes. (burkart2025phenotypicalandgenotypical pages 2-2) | Human case-level evidence; moderate | Minimum detailed case count in KB: **4**; note ascertainment uncertainty beyond retrieved sources |
| Variant spectrum | Reported disease-associated detailed variants: **c.1207G>A (p.Glu403Lys/E379K), c.1739A>G (p.Asp580Gly/D556G), c.2353T>C (p.Tyr785His/Y761H)**, plus **c.1844G>A (p.Arg615Gln)** in 2025. Variants cluster in the **amine oxidase/catalytic region**, including the **FAD-binding subdomain**. (pilotto2016lsd1kdm1amutationsassociated pages 2-3, pilotto2016lsd1kdm1amutationsassociated pages 1-2, burkart2025phenotypicalandgenotypical pages 2-2, burkart2025phenotypicalandgenotypical pages 4-4) | Human genetic + biochemical support; moderate-to-strong | Causal gene: **KDM1A**; variant class so far: **heterozygous missense**; hotspot concept: **catalytic/amino oxidase domain** |
| Cardinal phenotypes | Core phenotype includes **global developmental delay**, **intellectual disability/psychomotor retardation**, **hypotonia**, and **distinctive/variable craniofacial dysmorphism**. **Cleft palate is present in 3/4 detailed patients**; the 2025 case lacked palate abnormality, showing variable expressivity. Do **not** infer frequencies for other features from current evidence. (wilson2022reprogrammingofthe pages 17-19, burkart2025phenotypicalandgenotypical pages 1-2, burkart2025phenotypicalandgenotypical pages 2-2, burkart2025phenotypicalandgenotypical pages 4-4) | Human case reports/review; moderate | Suggested HPO anchors: developmental delay, intellectual disability, hypotonia, cleft palate, dysmorphic facies |
| Onset/course | Pediatric neurodevelopmental onset; in the 2025 case, **hypotonia at birth**, delayed first words (**2 years**), independent walking (**2.5 years**), and persistent mild ID at age 13 were reported. Available evidence supports a **chronic, developmental, variably expressive** course rather than degenerative episodes. (burkart2025phenotypicalandgenotypical pages 2-2) | Human case-level evidence; limited-to-moderate | Onset: **congenital/early childhood**; course: **lifelong neurodevelopmental disorder** |
| Molecular mechanism | KDM1A/LSD1 is a **FAD-dependent histone demethylase** acting mainly on **H3K4me1/2** (and context-dependently H3K9me1/2) within complexes such as **CoREST/REST**. Disease variants impair **demethylase activity** and can weaken binding to some transcription factors; E379K is most severe, while D556G and Y761H show ~**10-20-fold** lower catalytic efficiency. Variants near the **FAD-binding site** may disrupt cofactor affinity/stability and chromatin regulation. (pilotto2016lsd1kdm1amutationsassociated pages 2-3, pilotto2016lsd1kdm1amutationsassociated pages 1-2, wilson2022reprogrammingofthe pages 17-19, burkart2025phenotypicalandgenotypical pages 4-5) | Functional biochemistry + broader mechanistic biology; strong for enzyme defect, moderate for disease causal chain | Mechanism tag: **chromatinopathy / histone demethylase dysfunction**; likely effect: **loss-of-function or hypomorphic catalytic impairment** |
| Diagnosis | Current strongest diagnostic route is **genomic sequencing** (trio genome/exome style testing), with variant interpretation in clinical context. In the 2025 case, prior **karyotype, array, FMR1 repeat testing, metabolic workup, ENT and cardiac evaluation** were non-contributory/normal before diagnosis by trio genome sequencing. (burkart2025phenotypicalandgenotypical pages 2-2) | Human case-level clinical evidence; limited | Diagnostic strategy: **sequence-based molecular diagnosis** after nonspecific neurodevelopmental presentation |
| Treatment/trials | **No disease-specific therapy or clinical trials** for KDM1A-related neurodevelopmental disorder were identified in the retrieved evidence. Do **not** repurpose oncology LSD1 inhibitor trials as treatment evidence for this disorder. Management evidence in retrieved sources is sparse and largely supportive/diagnostic rather than interventional. (burkart2025phenotypicalandgenotypical pages 2-2, burkart2025phenotypicalandgenotypical pages 4-4) | Evidence gap; weak/absent | Treatment status: **supportive care only documented indirectly**; trial status: **no KDM1A-RD-specific trials identified** |
| Prognosis/epidemiology | The disorder is described as **ultra-rare**. Robust prevalence, incidence, life expectancy, mortality, and penetrance estimates were **not available** in the retrieved evidence. Available human data support **variable expressivity** and generally persistent neurodevelopmental impairment. (burkart2025phenotypicalandgenotypical pages 2-2, burkart2025phenotypicalandgenotypical pages 1-2, burkart2025phenotypicalandgenotypical pages 4-4) | Human evidence sparse; weak | Epidemiology: **unknown / ultra-rare**; prognosis: **developmental impairment persists, severity variable** |
| Key models | Broader KDM1A biology strongly supports neurodevelopmental relevance: mouse loss/knockdown studies show roles in **neurite morphogenesis**, **neuronal differentiation**, and **memory**; 2024 adult forebrain-neuron conditional KO multi-omics showed derepression of **PRC2-silenced nonneuronal genes** and altered chromatin boundary maintenance; zebrafish deficiency causes reduced neurogenesis, shorter motor axons, and locomotor/learning deficits. These are **supportive mechanism models**, not direct patient-specific disease models. (blanco2024kdm1asafeguardsthe pages 1-2, zou2025deficiencyofkdm1a pages 5-7, wilson2022reprogrammingofthe pages 17-19, swahari2019histonedemethylasesin pages 1-3) | Experimental model evidence; strong for gene function, indirect for human disorder | Model-organism evidence supports nervous-system vulnerability and chromatin dysregulation as disease-relevant biology |


*Table: This table summarizes the highest-confidence disease facts for KDM1A-related neurodevelopmental disorder/CPRF syndrome, separating direct human case evidence from broader KDM1A mechanistic model evidence. It is designed for rapid knowledge-base ingestion and flags major evidence gaps, especially for epidemiology and treatment.*

## 1. Disease information

### Definition and identifiers

| Field | Recommended entry |
|---|---|
| Preferred name | **KDM1A-related neurodevelopmental disorder** |
| Principal synonym | **Cleft palate, psychomotor retardation, and distinctive facial features syndrome** |
| Abbreviation | **CPRF syndrome** |
| OMIM | **616728** |
| Category | Mendelian neurodevelopmental disorder; chromatinopathy |
| Inheritance | Autosomal dominant, usually de novo in reported patients |
| Causal gene | **KDM1A/LSD1** |
| MONDO | A specific MONDO identifier was not verified in the retrieved literature; do not assign one without checking the current MONDO release. |
| Orphanet, MeSH, ICD-10/11 | No disease-specific identifiers were verified. Cases would ordinarily be coded under broader congenital/neurodevelopmental categories. |

CPRF is the historical phenotype-based label, but **KDM1A-related neurodevelopmental disorder** is preferable because cleft palate is variably expressive. The 2025 case was explicitly reported without any palate abnormality. (wilson2022reprogrammingofthe pages 17-19, burkart2025phenotypicalandgenotypical pages 4-4, burkart2025phenotypicalandgenotypical pages 1-2)

The present description is an **aggregated disease-level synthesis of published case reports and experimental studies**, not an EHR-derived patient profile. Only four individuals have sufficiently detailed published phenotypes in the retrieved evidence; four additional ClinVar missense variants were mentioned without detailed clinical records. (burkart2025phenotypicalandgenotypical pages 2-2)

## 2. Etiology

### Causal and genetic factors

The disorder is caused by heterozygous germline **KDM1A** variants. All sufficiently characterized alleles are missense substitutions affecting the catalytic amino-oxidase region:

- **c.1207G>A, p.Glu403Lys**—also numbered E379K in a shorter protein construct.
- **c.1739A>G, p.Asp580Gly**—D556G in the experimental construct.
- **c.2353T>C, p.Tyr785His**—Y761H in the experimental construct.
- **c.1844G>A, p.Arg615Gln**, a de novo likely pathogenic allele reported in 2025.

The first three substitutions affect active-site residues; p.Arg615Gln lies in the amino-oxidase domain and near its FAD-binding subdomain. (burkart2025phenotypicalandgenotypical pages 2-2, burkart2025phenotypicalandgenotypical pages 4-4, pilotto2016lsd1kdm1amutationsassociated pages 2-3, pilotto2016lsd1kdm1amutationsassociated pages 1-2)

The reported inheritance pattern is **autosomal dominant and de novo**. One original individual also carried a de novo **ANKRD11** deletion/variant and therefore had a potentially blended KDM1A/KBG phenotype, limiting the precision of phenotype attribution in that case. (pilotto2016lsd1kdm1amutationsassociated pages 2-3, vallianatos2015disruptedintricacyof pages 8-9)

### Environmental, lifestyle, infectious, and protective factors

No reproducible environmental, infectious, dietary, occupational, lifestyle, or gene–environment risk factor has been established. Likewise, no protective variant, modifier allele, founder effect, or protective exposure has been reported. This is expected for a highly penetrant-appearing monogenic developmental disorder, but penetrance cannot yet be quantified.

No evidence supports smoking, alcohol, diet, pollution, infection, or vaccination status as determinants of KDM1A-RD. General prenatal-health recommendations remain appropriate but should not be presented as disease-specific prevention.

## 3. Phenotypes

### Core phenotype and suggested HPO annotations

| Phenotype | Characteristics and evidence | Suggested HPO term |
|---|---|---|
| Global developmental delay | Early-childhood onset; apparently universal among detailed cases, but exact pooled frequency cannot be independently reconstructed | **HP:0001263** Global developmental delay |
| Intellectual disability | Variable; mild ID and IQ 57 in the 2025 case; described as cognitive impairment/ID in original cases | **HP:0001249** Intellectual disability |
| Delayed speech | First words at age 2 years in the 2025 case | **HP:0000750** Delayed speech and language development |
| Delayed walking | Independent walking at 2.5 years in the 2025 case | **HP:0002060** Delayed motor development |
| Generalized hypotonia | Congenital in the 2025 patient; part of the broader phenotype | **HP:0001252** Hypotonia |
| Cleft palate | Present in the three previously detailed patients and absent in the 2025 case: **3/4**, subject to severe ascertainment bias | **HP:0000175** Cleft palate |
| Facial dysmorphism | Variable: long face, small forehead, mild ptosis, long/small nose, short philtrum, and small low-set ears in the newest case | **HP:0001999** Abnormal facial shape; **HP:0000508** Ptosis; **HP:0000369** Low-set ears |
| Digital/nail anomalies | Broad fingertips, hypoplastic nails, finger/toe clinodactyly | **HP:0001212** Clinodactyly; **HP:0001792** Small nail |
| Kyphosis | Mild thoracic kyphosis in the newest case | **HP:0002808** Kyphosis |
| Myopia/visual impairment | Moderate myopia with mild visual impairment in the newest case | **HP:0000545** Myopia; **HP:0000505** Visual impairment |
| Social difficulties | Reported at ages 3–4 years in the newest case; insufficient evidence for an autism diagnosis | **HP:0012433** Social and occupational deterioration or a more specific behavioral term after formal assessment |

The newest patient had no seizures, recognized structural CNS abnormality, cardiac defect, hearing impairment, or persistent creatine-kinase elevation. Brain imaging was not performed in that report, so “no structural CNS abnormality” should not be interpreted as a definitive normal MRI. (burkart2025phenotypicalandgenotypical pages 2-2, burkart2025phenotypicalandgenotypical pages 3-4, burkart2025phenotypicalandgenotypical pages 1-2)

### Severity, progression, and quality of life

Severity is variable. The 13-year-old patient had mild developmental impairment and ID, while the original syndrome descriptions included psychomotor retardation and more conspicuous craniofacial anomalies. Available evidence suggests a **chronic, lifelong developmental disability**, not a proven neurodegenerative or episodic disorder. Formal longitudinal natural-history data are unavailable. (wilson2022reprogrammingofthe pages 17-19, burkart2025phenotypicalandgenotypical pages 1-2)

No EQ-5D, SF-36, PROMIS, adaptive-function, or disease-specific quality-of-life study has been published in the retrieved evidence. Functional effects can nevertheless include delayed mobility, communication limitations, educational needs, and social difficulties.

## 4. Genetic and molecular information

### Gene and protein

- **Gene:** KDM1A, also called LSD1.
- **Protein class:** FAD-dependent amine oxidase/histone lysine demethylase.
- **Substrates:** principally H3K4me1 and H3K4me2 in repressive complexes; H3K9me1/2 activity can occur in other protein contexts.
- **Major complexes:** CoREST/RCOR–REST and SIN3A/HDAC-associated transcriptional regulatory assemblies.
- **Subcellular location:** predominantly nucleus/chromatin.

Suggested annotations include **GO:0032452 histone demethylase activity**, **GO:0070544 histone H3-K4 demethylation**, **GO:0006355 regulation of DNA-templated transcription**, **GO:0005634 nucleus**, and **GO:0000785 chromatin**. FAD may be annotated as **CHEBI:57692** (FAD anion; database-release verification recommended). (zou2025deficiencyofkdm1a pages 5-7, wilson2022reprogrammingofthe pages 17-19, swahari2019histonedemethylasesin pages 1-3)

### Functional effects of pathogenic variants

Biochemical testing supplied unusually strong mechanistic evidence:

- E379K/p.Glu403Lys had barely detectable demethylase activity and severely impaired H3-tail binding.
- D556G/p.Asp580Gly and Y761H/p.Tyr785His were approximately **10–20-fold less catalytically efficient**, principally through reduced turnover.
- The variants retained gross structural integrity and CoREST binding, but showed differential impairment of transcription-factor interactions and reduced cellular stability/half-life.
- Tyr761 lies in the aromatic catalytic cage adjacent to FAD; Glu379 and Asp556 are near the histone-tail entrance.

Thus, the strongest interpretation is **hypomorphic or loss-of-function-like catalytic dysfunction**, rather than a uniform dominant-negative mechanism. A gain-of-function interpretation has occasionally been suggested for an individual allele, but the direct biochemical data overall favor impaired catalytic function and altered partner interactions. (pilotto2016lsd1kdm1amutationsassociated pages 2-3, pilotto2016lsd1kdm1amutationsassociated pages 1-2, wilson2022reprogrammingofthe pages 17-19)

Population frequencies were not supplied in the retrieved full texts. Given de novo occurrence and ultra-rarity, causative alleles are expected to be absent or extremely rare in gnomAD, but every candidate must be checked directly against the current gnomAD release. No somatic origin has been implicated in CPRF; somatic KDM1A biology in cancer is a separate subject.

### Structural, modifier, and epigenetic findings

No recurrent pathogenic deletion, duplication, translocation, inversion, or aneuploidy defining KDM1A-RD has been established. No validated modifier gene is known. The co-occurring ANKRD11 alteration in one patient is best regarded as a potential second diagnosis rather than a proven modifier. (vallianatos2015disruptedintricacyof pages 8-9)

A disease-specific blood DNA-methylation episignature has not yet been validated. The 2025 authors proposed episignature analysis as a future means of distinguishing pathogenic from benign KDM1A variants. (burkart2025phenotypicalandgenotypical pages 3-4)

## 5. Environmental information

Environmental causation is **not applicable on current evidence**. No toxin, radiation exposure, pollutant, infection, microbiome pattern, or lifestyle behavior is known to produce this Mendelian syndrome. Environmental accommodations—educational support, accessible communication, and rehabilitation—may strongly affect functional outcome, but they do not alter the underlying genetic cause.

## 6. Mechanism and pathophysiology

### Proposed causal chain

1. A de novo heterozygous variant alters the KDM1A amino-oxidase/catalytic domain.
2. FAD-dependent oxidative demethylation and/or recruitment of transcriptional partners is reduced.
3. H3K4me1/2 regulation and CoREST/REST-dependent repression become mistimed or locus inappropriate.
4. Neural progenitor differentiation, neuronal gene programs, neurite growth, synaptic transcription, and maintenance of mature neuronal identity are disrupted.
5. Altered neural-circuit development produces hypotonia, delayed milestones, ID, and behavioral/learning impairment.
6. Disturbed epigenetic control in cranial neural crest or craniofacial developmental programs plausibly contributes to cleft palate and dysmorphism, although this last link has not been demonstrated in a patient-variant craniofacial model. (pilotto2016lsd1kdm1amutationsassociated pages 2-3, wilson2022reprogrammingofthe pages 17-19, vallianatos2015disruptedintricacyof pages 8-9, swahari2019histonedemethylasesin pages 1-3)

### Upstream and downstream processes

The **upstream lesion** is defective chromatin-enzyme activity or partner binding. Intermediate processes include transcriptional derepression, abnormal histone methylation, impaired neural-progenitor differentiation, and neurite/synapse abnormalities. Developmental delay and craniofacial anomalies are downstream organism-level consequences.

KDM1A–CoREST can oppose Notch/HES1 signaling in cortical progenitors and support NGN2-associated neuronal differentiation. An RCOR2/KDM1A complex also regulates cortical neurogenesis partly through repression of **DLX2** and **SHH**. These findings identify candidate pathways, but they are not yet proven to be dysregulated in patient tissue. (swahari2019histonedemethylasesin pages 1-3)

Suggested biological-process terms include **GO:0022008 neurogenesis**, **GO:0030182 neuron differentiation**, **GO:0048666 neuron development**, **GO:0031175 neuron projection development**, and **GO:0007399 nervous system development**.

### 2024 multi-omics development

A March 2024 *Nature Communications* study used inducible, forebrain-restricted Kdm1a deletion with transcriptomics, epigenomics, chromatin-conformation analysis, and super-resolution microscopy. Loss of Kdm1a in adult excitatory neurons derepressed non-neuronal genes normally silenced by PRC2 and weakened their segregation from adjacent active chromatin. The N-terminal intrinsically disordered region was necessary for maintaining those topological boundaries, which also weakened during normal aging. This expands the model from a simple histone-demethylase defect to failure of **three-dimensional neuronal genome organization and cell-identity maintenance**. It is strong mechanistic evidence but not a direct model of any human CPRF allele. DOI: https://doi.org/10.1038/s41467-024-45773-3; published March 2024. (blanco2024kdm1asafeguardsthe pages 1-2)

The abstract’s key conclusion was: **“Kdm1a elimination causes the neuronal activation of nonneuronal genes that are silenced by the polycomb repressor complex and interspersed with active genes.”** (blanco2024kdm1asafeguardsthe pages 1-2)

No KDM1A-RD-specific patient transcriptome, proteome, metabolome, lipidome, single-cell atlas, spatial transcriptome, organoid study, or integrated multi-omics cohort was identified.

## 7. Anatomical structures affected

The principal affected system is the **nervous system**, particularly the developing brain and its neuronal circuits. Supporting model evidence implicates cerebral cortex, hippocampal circuits, neural progenitors, mature excitatory neurons, motor neurons, axons, dendrites, and synapses. Craniofacial structures—especially the secondary palate and facial skeleton/soft tissues—are also affected in many patients. Skeletal/digital, ocular, and muscular manifestations occur variably. (zou2025deficiencyofkdm1a pages 5-7, wilson2022reprogrammingofthe pages 17-19, swahari2019histonedemethylasesin pages 1-3, burkart2025phenotypicalandgenotypical pages 1-2)

Suggested anatomy/cell annotations:

- **UBERON:0000955 brain**
- **UBERON:0001890 forebrain**
- **UBERON:0001950 neocortex**
- **UBERON:0002421 hippocampal formation**
- **UBERON:0001716 secondary palate**
- **CL:0000540 neuron**
- **CL:0000679 glutamatergic neuron**
- **CL:0000127 astrocyte** only as a model-context candidate, not a proven primary patient cell
- **GO:0005634 nucleus** and **GO:0000785 chromatin** at subcellular level

There is no established lateralization pattern.

## 8. Temporal development

Onset is congenital or in early infancy. Hypotonia may be apparent from birth; developmental delay becomes evident as motor and language milestones are missed. Cleft palate and dysmorphic features are congenital. The disorder appears chronic and lifelong, with variable severity. There are no validated stages, remission pattern, or end-stage phenotype. (burkart2025phenotypicalandgenotypical pages 1-2, burkart2025phenotypicalandgenotypical pages 2-2)

Embryonic and early postnatal development are probable critical periods because KDM1A regulates zygotic genome activation, gastrulation, neural differentiation, and craniofacial development. Mature-neuron experiments indicate that KDM1A remains important later in life, raising the theoretical possibility that some functional abnormalities may remain modifiable; this is not yet clinical evidence of reversibility. (vallianatos2015disruptedintricacyof pages 8-9, blanco2024kdm1asafeguardsthe pages 1-2)

## 9. Inheritance, penetrance, and population

- **Inheritance:** autosomal dominant.
- **Origin:** de novo in documented cases.
- **Penetrance:** apparently high for neurodevelopmental manifestations among ascertained cases, but not measurable.
- **Expressivity:** demonstrably variable, particularly for cleft palate and severity of ID.
- **Anticipation:** not reported.
- **Germline mosaicism:** not documented, but low residual recurrence risk remains biologically possible for apparently de novo variants.
- **Founder effects/consanguinity:** none reported; consanguinity is not mechanistically relevant to typical de novo dominant disease.
- **Carrier frequency:** unknown and expected to be extremely low.
- **Sex ratio, ancestry, and geographic distribution:** cannot be estimated from four detailed cases.

No population prevalence or annual incidence has been established. “Ultra-rare” is more defensible than a numerical estimate. (burkart2025phenotypicalandgenotypical pages 2-2, burkart2025phenotypicalandgenotypical pages 1-2)

## 10. Diagnostics

### Recommended genetic approach

1. **Clinical recognition:** developmental delay/ID plus hypotonia and variable craniofacial, palate, digital, or nail abnormalities.
2. **First-line molecular test:** trio exome or genome sequencing with copy-number analysis. KDM1A should also be included on broad developmental-delay/ID, cleft-palate, and chromatinopathy panels.
3. **Variant assessment:** confirm heterozygosity and de novo status by parental testing; apply ACMG/AMP criteria; assess domain location, conservation, population frequency, computational evidence, and functional literature.
4. **Sanger confirmation** may be used depending on laboratory policy.
5. **CMA:** useful when sequencing does not include reliable CNV detection or when a blended diagnosis is suspected.
6. **Karyotype/FISH:** not routine unless a structural chromosome abnormality is clinically suspected.
7. **FMR1 repeat testing:** remains part of some unexplained-ID pathways but does not test KDM1A-RD.
8. Mitochondrial and repeat-expansion tests are not specifically indicated unless the phenotype suggests another disorder.

In the 2025 patient, trio genome sequencing found de novo p.Arg615Gln after karyotype, microarray, FMR1 analysis, and metabolic investigations were unrevealing. (burkart2025phenotypicalandgenotypical pages 2-2)

### Clinical evaluations

There is no diagnostic biochemical assay. Baseline assessment should include developmental and neuropsychological testing, speech/language evaluation, neurologic examination, hearing and vision screening, palate/feeding assessment, and musculoskeletal examination. EEG is symptom triggered; brain MRI is reasonable for seizures, focal findings, regression, abnormal head growth, or severe presentation. Echocardiography, metabolic studies, or CK measurement should be directed by clinical findings rather than assumed to be universally abnormal.

### Differential diagnosis

Important alternatives include:

- **Kabuki syndrome**—KMT2D or KDM6A; overlapping facial features, developmental delay, hypotonia, and palate anomalies.
- **KBG syndrome**—ANKRD11; macrodontia, skeletal findings, characteristic face, developmental delay.
- Other chromatinopathies involving KDM or KMT genes.
- Syndromic cleft-palate disorders, 22q11.2 deletion syndrome, and nonsyndromic developmental-delay etiologies.

The initial patient’s simultaneous ANKRD11 and KDM1A findings particularly emphasize the need to consider dual diagnoses. (wilson2022reprogrammingofthe pages 17-19, vallianatos2015disruptedintricacyof pages 8-9)

No formal clinical criteria, validated episignature, protein biomarker, metabolomic signature, prenatal ultrasound signature, newborn-screening assay, or population-screening program exists.

## 11. Outcome and prognosis

There are no survival curves, mortality estimates, or life-expectancy data. Nothing in the limited literature establishes disease-specific premature mortality, but absence of evidence is not proof of normal life expectancy. The principal recognized burden is persistent neurodevelopmental disability affecting learning, communication, motor development, education, and social functioning. (burkart2025phenotypicalandgenotypical pages 1-2, burkart2025phenotypicalandgenotypical pages 4-4)

Known severity predictors and prognostic biomarkers are unavailable. Catalytic impairment varies by allele in vitro, but a genotype–phenotype relationship cannot be inferred from four detailed patients. Cleft palate may require surgical treatment and can contribute to feeding, speech, and hearing morbidity. Seizures are not established as obligatory; the newest patient had none. (pilotto2016lsd1kdm1amutationsassociated pages 2-3, burkart2025phenotypicalandgenotypical pages 2-2)

## 12. Treatment

### Current management

No approved disease-modifying therapy or KDM1A-RD-specific treatment guideline exists. Recommended practice is individualized multidisciplinary care:

- Early developmental intervention.
- Physical therapy for hypotonia and gross-motor delay.
- Occupational therapy for fine-motor and adaptive skills.
- Speech-language therapy, including augmentative communication when required.
- Educational and neuropsychological support.
- Cleft-palate team management, including feeding, audiology, speech, dentistry, orthodontics, and surgery when indicated.
- Ophthalmologic treatment for myopia or other visual abnormalities.
- Orthopedic/physiatry monitoring for kyphosis, gait, and contractures.
- Standard antiseizure therapy only if epilepsy emerges.

Suggested NCIT intervention concepts include **Physical Therapy**, **Occupational Therapy**, **Speech Therapy**, **Developmental Intervention**, and **Cleft Palate Repair**; exact NCIT codes should be checked against the current release.

### Experimental therapeutics and trials

No gene therapy, CRISPR editing, ASO, RNA therapy, cell therapy, or targeted small-molecule trial has been reported for KDM1A-RD. Searches retrieved LSD1-inhibitor trials in leukemia and small-cell lung cancer, but these are oncology studies and **must not be construed as treatment trials for a KDM1A loss-of-function neurodevelopmental disorder**. Pharmacologic KDM1A inhibition could theoretically worsen insufficient KDM1A activity, depending on allele and developmental context. (pilotto2016lsd1kdm1amutationsassociated pages 2-3, burkart2025phenotypicalandgenotypical pages 2-2)

Inhibition of KDM1A has improved neurogenesis or memory in models of other chromatin disorders such as Kabuki syndrome, but that is mechanistically opposite and not evidence for treating KDM1A-RD. Genotype-specific functional studies are required before considering epigenetic drugs.

## 13. Prevention

Primary prevention by lifestyle change, vaccination, or environmental avoidance is not available. Appropriate strategies are genetic and developmental:

- **Genetic counseling:** explain dominant, usually de novo inheritance.
- **Parental testing:** confirms de novo status and identifies rare parental mosaicism.
- **Recurrence risk:** low but above the population baseline after an apparently de novo event because germline mosaicism cannot be excluded.
- **Reproductive options:** targeted prenatal diagnosis by chorionic-villus sampling or amniocentesis, and preimplantation genetic testing for a known familial variant.
- **Cascade testing:** appropriate if a parent is found to carry the variant or mosaicism is suspected.
- **Secondary/tertiary prevention:** early developmental assessment, therapy, hearing/vision surveillance, and proactive palate management to reduce avoidable complications.

KDM1A-RD is not currently suitable for population carrier or newborn screening because it is predominantly de novo, exceptionally rare, lacks a validated screening assay, and has no presymptomatic disease-modifying treatment.

## 14. Other species and natural disease

KDM1A is evolutionarily conserved, with experimentally studied orthologs including mouse **Kdm1a**, zebrafish **kdm1a**, and *C. elegans* **spr-5**. Relevant taxa include *Mus musculus* (NCBI Taxon 10090), *Danio rerio* (7955), and *Caenorhabditis elegans* (6239).

No naturally occurring veterinary counterpart or breed-associated KDM1A syndrome was identified. Consequently, there is no zoonotic potential or cross-species transmission. Comparative relevance comes from induced genetic models rather than natural animal disease.

## 15. Model organisms

### Mouse

Complete Kdm1a loss causes early embryonic lethality around gastrulation, limiting its utility as a direct CPRF model. Conditional or knockdown studies show impaired cortical neurogenesis, reduced dendritic arborization and neurite width, altered synaptic transcription, and memory deficits. Adult forebrain-specific deletion demonstrates derepression of non-neuronal PRC2 targets and impaired chromatin-domain segregation. These models strongly establish gene function but do not reproduce a specific human heterozygous missense allele. (wilson2022reprogrammingofthe pages 17-19, vallianatos2015disruptedintricacyof pages 8-9, swahari2019histonedemethylasesin pages 1-3, blanco2024kdm1asafeguardsthe pages 1-2)

### Zebrafish

A 2025 CRISPR kdm1a-deficiency model showed lower neuronal density, reduced neuronal reporter signal, shortened motor-neuron axons, locomotor abnormalities, and impaired learning/memory. Neurogenesis and maturation genes—including **neurod1, neurog1, elavl3, tuba1, gfap, gap43**, and **syn2a**—were downregulated, while autophagy/apoptosis-associated **beclin1** and caspase expression increased. This supports neuronal loss/dysfunction as a downstream mechanism, although the model is a knockout rather than a patient-specific heterozygous knock-in. DOI: https://doi.org/10.31083/jin44394; published November 2025. (zou2025deficiencyofkdm1a pages 5-7)

### Invertebrate and cellular models

*C. elegans spr-5* studies support an evolutionarily conserved role in erasing H3K4 methylation and preventing inappropriate transcriptional memory. Cultured neurons and cortical-progenitor experiments are useful for neurite morphology, partner binding, enzyme kinetics, and transcriptomic rescue studies. No patient-derived iPSC neuron, neural-crest cell, brain organoid, or palate organoid model was identified.

### Model limitations and research priorities

The principal limitation is the mismatch between severe knockout models and heterozygous human missense disease. Highest-priority resources are:

1. Patient-variant knock-in mouse and zebrafish lines.
2. Patient-derived iPSC cortical neurons and cranial neural-crest cells.
3. Isogenic correction controls.
4. H3K4me1/2 profiling, CUT&RUN, RNA-seq, and chromatin-conformation studies.
5. Single-cell and spatial analyses during cortical and palatal development.
6. Allele-specific assays to distinguish haploinsufficiency, dominant-negative effects, and altered substrate/partner specificity.

## Key evidence quotations and bibliography

- Pilotto et al., *Human Molecular Genetics*, June 2016: the three variants “**impair demethylase activity and binding to transcription factors**,” providing direct biochemical support for pathogenicity. DOI: https://doi.org/10.1093/hmg/ddw120. (pilotto2016lsd1kdm1amutationsassociated pages 2-3, pilotto2016lsd1kdm1amutationsassociated pages 1-2)
- Del Blanco et al., *Nature Communications*, March 2024: “**Kdm1a elimination causes the neuronal activation of nonneuronal genes that are silenced by the polycomb repressor complex and interspersed with active genes.**” DOI: https://doi.org/10.1038/s41467-024-45773-3. (blanco2024kdm1asafeguardsthe pages 1-2)
- Burkart et al., *American Journal of Medical Genetics Part A*, June 2025: the new patient carried a “**novel heterozygous, likely pathogenic germline missense variant**” and was the first detailed individual reported without palate abnormalities. DOI: https://doi.org/10.1002/ajmg.a.64144. (burkart2025phenotypicalandgenotypical pages 2-2, burkart2025phenotypicalandgenotypical pages 4-4)
- Wilson et al., *Critical Reviews in Biochemistry and Molecular Biology*, October 2022. DOI: https://doi.org/10.1080/10409238.2021.1979457. This review places CPRF among neurodevelopmental chromatinopathies and summarizes KDM1A–CoREST/REST biology. (wilson2022reprogrammingofthe pages 17-19)

PMIDs were not present in the retrieved full-text metadata and therefore are not supplied rather than risk assigning incorrect identifiers. DOI links above provide stable primary-source access.

## Overall evidence assessment

The gene–disease relationship is supported by multiple de novo alleles, clustering in a functionally critical domain, direct enzyme assays, and convergent neurodevelopmental model evidence. Nevertheless, clinical validity is constrained by the exceptionally small patient series, one potentially blended ANKRD11/KDM1A case, absence of systematic longitudinal follow-up, and lack of patient-derived molecular profiling. Phenotype frequencies other than the observed cleft-palate count of 3/4 should therefore be stored as **unknown**, not extrapolated percentages. The immediate clinical priorities are molecular diagnosis, careful documentation of additional cases, multidisciplinary supportive care, and international natural-history aggregation.

References

1. (burkart2025phenotypicalandgenotypical pages 2-2): Sebastian Burkart, Melanie Spanjaard, Lilian Kaufmann, Katrin Hinderhofer, Christian P. Schaaf, Markus Ries, and Maja Hempel. Phenotypical and genotypical expansion of autosomal-dominant kdm1a-related neurodevelopmental disorder spectrum: a case report. American journal of medical genetics. Part A, pages e64144, Jun 2025. URL: https://doi.org/10.1002/ajmg.a.64144, doi:10.1002/ajmg.a.64144. This article has 1 citations and is from a peer-reviewed journal.

2. (burkart2025phenotypicalandgenotypical pages 1-2): Sebastian Burkart, Melanie Spanjaard, Lilian Kaufmann, Katrin Hinderhofer, Christian P. Schaaf, Markus Ries, and Maja Hempel. Phenotypical and genotypical expansion of autosomal-dominant kdm1a-related neurodevelopmental disorder spectrum: a case report. American journal of medical genetics. Part A, pages e64144, Jun 2025. URL: https://doi.org/10.1002/ajmg.a.64144, doi:10.1002/ajmg.a.64144. This article has 1 citations and is from a peer-reviewed journal.

3. (burkart2025phenotypicalandgenotypical pages 4-4): Sebastian Burkart, Melanie Spanjaard, Lilian Kaufmann, Katrin Hinderhofer, Christian P. Schaaf, Markus Ries, and Maja Hempel. Phenotypical and genotypical expansion of autosomal-dominant kdm1a-related neurodevelopmental disorder spectrum: a case report. American journal of medical genetics. Part A, pages e64144, Jun 2025. URL: https://doi.org/10.1002/ajmg.a.64144, doi:10.1002/ajmg.a.64144. This article has 1 citations and is from a peer-reviewed journal.

4. (pilotto2016lsd1kdm1amutationsassociated pages 2-3): Simona Pilotto, Valentina Speranzini, Chiara Marabelli, Francesco Rusconi, Emanuela Toffolo, Barbara Grillo, Elena Battaglioli, and Andrea Mattevi. Lsd1/kdm1a mutations associated to a newly described form of intellectual disability impair demethylase activity and binding to transcription factors. Human molecular genetics, 25 12:2578-2587, Jun 2016. URL: https://doi.org/10.1093/hmg/ddw120, doi:10.1093/hmg/ddw120. This article has 66 citations and is from a domain leading peer-reviewed journal.

5. (wilson2022reprogrammingofthe pages 17-19): Khadija D. Wilson, Elizabeth G. Porter, and Benjamin A. Garcia. Reprogramming of the epigenome in neurodevelopmental disorders. Critical Reviews in Biochemistry and Molecular Biology, 57:73-112, Oct 2022. URL: https://doi.org/10.1080/10409238.2021.1979457, doi:10.1080/10409238.2021.1979457. This article has 31 citations and is from a peer-reviewed journal.

6. (blanco2024kdm1asafeguardsthe pages 1-2): Beatriz del Blanco, Sergio Niñerola, Ana M. Martín-González, Juan Paraíso-Luna, Minji Kim, Rafael Muñoz-Viana, Carina Racovac, Jose V. Sanchez-Mut, Yijun Ruan, and Ángel Barco. Kdm1a safeguards the topological boundaries of prc2-repressed genes and prevents aging-related euchromatinization in neurons. Nature Communications, Mar 2024. URL: https://doi.org/10.1038/s41467-024-45773-3, doi:10.1038/s41467-024-45773-3. This article has 16 citations and is from a highest quality peer-reviewed journal.

7. (pilotto2016lsd1kdm1amutationsassociated pages 1-2): Simona Pilotto, Valentina Speranzini, Chiara Marabelli, Francesco Rusconi, Emanuela Toffolo, Barbara Grillo, Elena Battaglioli, and Andrea Mattevi. Lsd1/kdm1a mutations associated to a newly described form of intellectual disability impair demethylase activity and binding to transcription factors. Human molecular genetics, 25 12:2578-2587, Jun 2016. URL: https://doi.org/10.1093/hmg/ddw120, doi:10.1093/hmg/ddw120. This article has 66 citations and is from a domain leading peer-reviewed journal.

8. (burkart2025phenotypicalandgenotypical pages 4-5): Sebastian Burkart, Melanie Spanjaard, Lilian Kaufmann, Katrin Hinderhofer, Christian P. Schaaf, Markus Ries, and Maja Hempel. Phenotypical and genotypical expansion of autosomal-dominant kdm1a-related neurodevelopmental disorder spectrum: a case report. American journal of medical genetics. Part A, pages e64144, Jun 2025. URL: https://doi.org/10.1002/ajmg.a.64144, doi:10.1002/ajmg.a.64144. This article has 1 citations and is from a peer-reviewed journal.

9. (zou2025deficiencyofkdm1a pages 5-7): Li Zou, Jingyu Wang, Mengmeng Yao, Qu Xu, Qin Hong, Jiansheng Zhu, and Xia Chi. Deficiency of kdm1a induces locomotor abnormalities and learning and memory deficits in zebrafish larvae. Journal of Integrative Neuroscience, 24:44394, Nov 2025. URL: https://doi.org/10.31083/jin44394, doi:10.31083/jin44394. This article has 1 citations and is from a peer-reviewed journal.

10. (swahari2019histonedemethylasesin pages 1-3): Vijay Swahari and Anne E West. Histone demethylases in neuronal differentiation, plasticity, and disease. Current Opinion in Neurobiology, 59:9-15, Dec 2019. URL: https://doi.org/10.1016/j.conb.2019.02.009, doi:10.1016/j.conb.2019.02.009. This article has 45 citations and is from a peer-reviewed journal.

11. (vallianatos2015disruptedintricacyof pages 8-9): Christina N. Vallianatos and Shigeki Iwase. Disrupted intricacy of histone h3k4 methylation in neurodevelopmental disorders. Epigenomics, 7 3:503-19, Jun 2015. URL: https://doi.org/10.2217/epi.15.1, doi:10.2217/epi.15.1. This article has 229 citations and is from a peer-reviewed journal.

12. (burkart2025phenotypicalandgenotypical pages 3-4): Sebastian Burkart, Melanie Spanjaard, Lilian Kaufmann, Katrin Hinderhofer, Christian P. Schaaf, Markus Ries, and Maja Hempel. Phenotypical and genotypical expansion of autosomal-dominant kdm1a-related neurodevelopmental disorder spectrum: a case report. American journal of medical genetics. Part A, pages e64144, Jun 2025. URL: https://doi.org/10.1002/ajmg.a.64144, doi:10.1002/ajmg.a.64144. This article has 1 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](KDM1A-Related_Neurodevelopmental_Disorder-deep-research-falcon_artifacts/artifact-00.md)