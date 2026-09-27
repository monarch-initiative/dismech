---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-01T18:21:11.593943'
end_time: '2026-08-01T18:30:42.988906'
duration_seconds: 571.4
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: PUS3-Related Neurodevelopmental Disorder
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 15
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: PUS3-Related_Neurodevelopmental_Disorder-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** PUS3-Related Neurodevelopmental Disorder
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **PUS3-Related Neurodevelopmental Disorder** covering all of the
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
- **Disease Name:** PUS3-Related Neurodevelopmental Disorder
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **PUS3-Related Neurodevelopmental Disorder** covering all of the
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


# PUS3-Related Neurodevelopmental Disorder: Disease-Characteristics Report

## Executive summary

PUS3-related neurodevelopmental disorder is an ultra-rare autosomal-recessive Mendelian condition caused by biallelic pathogenic or likely pathogenic variants in **PUS3**, which encodes pseudouridine synthase 3. The established phenotype comprises developmental delay/intellectual disability, severe speech impairment, motor delay, hypotonia, epilepsy, microcephaly, variable brain MRI abnormalities, growth restriction, scoliosis, behavioral abnormalities, and nonspecific facial dysmorphism. The OMIM name is **neurodevelopmental disorder with microcephaly and gray sclera (NEDMIGS), OMIM #617051**, although gray sclera occurs in only a minority and should not be required for diagnosis. The largest disease-specific synthesis included 21 individuals from 15 families; thus, frequencies below are provisional and vulnerable to ascertainment and missing-data bias. (nøstvik2021clinicalandmolecular pages 2-3, nøstvik2021clinicalandmolecular pages 1-2)

The strongest mechanistic evidence comes from patient fibroblasts and recombinant-protein experiments. PUS3 normally installs pseudouridine at positions 38–39 in the tRNA anticodon loop. The recurrent p.Tyr71Cys substitution retained near-normal catalytic activity in purified-protein assays but destabilized the protein in cells, whereas p.Ile299Thr promoted aggregation. Both were associated with markedly reduced PUS3 protein and PUS3-dependent tRNA pseudouridylation in patient fibroblasts. (lin2022destabilizationofmutated pages 13-13, lin2022destabilizationofmutated pages 2-3, lin2022destabilizationofmutated pages 1-2)

No disease-specific therapy, validated biomarker, natural-history study, prevalence estimate, management guideline, or relevant registered interventional trial was identified. Current practice is molecular diagnosis, individualized symptomatic treatment, developmental rehabilitation, surveillance, and genetic counseling.

| Domain | Best current finding | Quantitative detail | Evidence type/strength |
|---|---|---|---|
| Disease identity | PUS3-related neurodevelopmental disorder is the same entity referred to in OMIM as NEDMIGS: neurodevelopmental disorder with microcephaly and gray sclera (OMIM #617051); gray sclera is not consistently present | 21 reported individuals from 15 families in the main aggregate cohort; gray/blue sclera in 7 individuals overall | Human clinical aggregate cohort; strongest disease-level summary currently available (nøstvik2021clinicalandmolecular pages 2-3, nøstvik2021clinicalandmolecular pages 1-2) |
| Gene and inheritance | Caused by biallelic PUS3 variants; autosomal recessive pattern supported by homozygous and compound-heterozygous cases with unaffected parents | 10/21 homozygous; 11/21 compound heterozygous | Human genetic evidence from multiple families; strong (nøstvik2021clinicalandmolecular pages 3-5, lin2022destabilizationofmutated pages 7-8) |
| Cohort size/demographics | Largest delineation collected published and new cases internationally | Age at evaluation 8 months-44 years; median 13 years; no sex difference | Human clinical cohort; moderate-strong for phenotype frequencies, limited by retrospective aggregation (nøstvik2021clinicalandmolecular pages 2-3) |
| Core neurodevelopmental phenotype | Disorder is dominated by intellectual disability/global developmental delay, speech impairment, motor delay, hypotonia, microcephaly, and facial dysmorphism | ID 19/19 (100% among assessed); impaired speech 11/11 (100%); motor delay 16/18 (88%); hypotonia 10/13 (77%); microcephaly/anencephaly 13/18 (72%); facial dysmorphism 17/18 (94%) | Human clinical aggregate evidence; strong for recurrent features, but denominators vary by reported assessment (nøstvik2021clinicalandmolecular pages 1-2, nøstvik2021clinicalandmolecular pages 2-3) |
| Epilepsy | Epilepsy is common but variable in onset, seizure type, and treatment response | 13/18 (72%); onset 1.5 months-18 years, median 22.5 months; 3/7 with available data achieved seizure freedom on treatment; EEG documented in 9, epileptiform discharges in 3 | Human clinical evidence; moderate due to incomplete ascertainment and heterogeneous follow-up (nøstvik2021clinicalandmolecular pages 2-3) |
| Neuroimaging and ancillary findings | Brain MRI may be normal or abnormal; common reported abnormalities include atrophy/hypoplasia and white-matter changes; growth/skeletal/behavioral issues are frequent | MRI abnormal 11/15 (73%), normal 4/15; short stature 10/17 (59%); scoliosis 8/10 (80%); behavioral features in 11/19; autism features in 4/6 assessed | Human clinical aggregate evidence; moderate (nøstvik2021clinicalandmolecular pages 3-5, nøstvik2021clinicalandmolecular pages 2-3) |
| Severe infant presentation | One reported Chinese infant had a severe epileptic encephalopathy/malformation presentation that broadens severity spectrum | Male infant, 8 months; compound heterozygous c.55C>T (p.Arg19*) and c.620dupT (p.Thr208fs); MRI with dilated cisterna magna and bilateral frontotemporal extracerebral space; metabolic screens normal | Single-patient case report; useful for edge phenotype, lower generalizability (fang2020compoundheterozygousmutations pages 1-3) |
| Variant spectrum | Broad allelic heterogeneity with missense and loss-of-function alleles; several recurrent variants exist | 17 distinct PUS3 variants in 21 individuals: 8 missense, 7 protein-truncating, 1 splice, 1 initiation-codon substitution | Human aggregate genetics; strong descriptive evidence (nøstvik2021clinicalandmolecular pages 3-5, nøstvik2021clinicalandmolecular pages 5-6) |
| Direct functional mechanism | Pathogenic variants can reduce PUS3 function by destabilizing or aggregating the protein, causing depletion of cellular PUS3 and reduced PUS3-dependent pseudouridylation in patient fibroblasts despite near-normal in vitro catalytic behavior for Y71C | In 3 patients, p.Tyr71Cys and p.Ile299Thr were linked to strongly reduced PUS3 protein and reduced PUS3-dependent Ψ levels in fibroblasts; Y71C preserved in vitro tRNA binding/activity but impaired thermostability; I299T promoted aggregation | Patient fibroblasts + recombinant protein assays; strongest direct mechanistic evidence available (lin2022destabilizationofmutated pages 13-13, lin2022destabilizationofmutated pages 2-3, lin2022destabilizationofmutated pages 10-10, lin2022destabilizationofmutated pages 1-2) |
| Molecular function/pathophysiology | PUS3 is a TruA/Pus3-family pseudouridine synthase that modifies tRNA anticodon-loop uridines (positions 38-39); deficiency likely impairs tRNA stabilization/biogenesis and downstream translation important for brain development; mitochondrial contribution remains plausible but unproven | PUS3 modifies U38/U39 of tRNA; localized in cytoplasm and mitochondria according to disease review/case synthesis | Integrated human genetics + biochemical inference; moderate, with some steps still inferential (nøstvik2021clinicalandmolecular pages 1-2, nøstvik2021clinicalandmolecular pages 3-5) |
| Diagnosis | Diagnosis currently depends on molecular testing rather than a pathognomonic clinical signature | Identified by exome sequencing, whole-genome sequencing, or virtual gene panels; parental testing performed in reported families | Human real-world diagnostic implementation; strong for current practice (nøstvik2021clinicalandmolecular pages 1-2, nøstvik2021clinicalandmolecular pages 2-3) |
| Treatment and real-world management | No disease-specific therapy exists; care is supportive and symptom-directed, especially antiseizure therapy and rehabilitation | In the severe infant case, sodium valproate gave incomplete control with seizures about every 3 months; in the pooled cohort, seizure control was variable and 3/7 achieved seizure freedom | Human case-based management evidence only; weak for treatment efficacy (fang2020compoundheterozygousmutations pages 1-3, nøstvik2021clinicalandmolecular pages 2-3) |
| Trials and translational pipeline | No relevant interventional clinical trials were identified for PUS3-related disorder | 0 relevant PUS3-specific trials found in tool search | Trial search evidence; strong for current absence of registered disease-specific trials in searched sources (tool search result summarized in conversation; no context ID available for citation, so omitted from citation field) |
| Major evidence gaps | No robust prevalence/incidence estimates, natural-history cohorts, validated biomarkers, genotype-specific management guidelines, or established disease animal models were identified; newer 2023-2024 literature is mostly broad RNA-modification review rather than disease-specific clinical advance | Epidemiology unknown; no disease-modifying therapy; no validated single-cell/spatial/multi-omics disease datasets identified in reviewed evidence | Evidence-gap synthesis from available human/mechanistic literature; moderate confidence in absence from searched sources (nøstvik2021clinicalandmolecular pages 2-3, nøstvik2021clinicalandmolecular pages 3-5, nøstvik2021clinicalandmolecular pages 1-2) |


*Table: This table summarizes the strongest currently available evidence for PUS3-related neurodevelopmental disorder across identity, genetics, phenotype, mechanism, diagnosis, treatment, and gaps. It is useful as a compact knowledge-base scaffold because the literature is sparse and distributed across a few key reports.*

## 1. Disease information

### Definition and nomenclature

The preferred descriptive name is **PUS3-related neurodevelopmental disorder** or **PUS3-associated neurodevelopmental disorder**. Synonyms include:

- **Neurodevelopmental disorder with microcephaly and gray sclera**
- **NEDMIGS**
- **PUS3-related intellectual disability**
- **Autosomal-recessive intellectual disability due to PUS3 deficiency**

The 2021 aggregate study states directly: “Biallelic variants in PUS3 have recently been recognized as a rare cause of neurodevelopmental disorders.” It also concluded that “homozygous and compound heterozygous PUS3 variants lead to a rare neurodevelopmental disorder.” (nøstvik2021clinicalandmolecular pages 1-2)

### Identifiers

- **OMIM:** #617051, NEDMIGS.
- **Causal gene:** **PUS3**; reference transcript used by the principal cohort was **NM_031307.4** and protein NP_112597.4. (lin2022destabilizationofmutated pages 2-3, nøstvik2021clinicalandmolecular pages 2-3)
- **MONDO:** A disease-specific MONDO identifier could not be verified from the retrieved authoritative evidence; use an exact MONDO term only after direct MONDO validation.
- **Orphanet:** No dedicated identifier was established in the retrieved literature.
- **ICD-10/ICD-11/MeSH:** No PUS3-specific code or heading was identified. In clinical systems, manifestations may be coded under developmental disorder/intellectual disability, epilepsy, microcephaly, or genetic syndrome categories rather than a disease-specific code.

### Evidence provenance

The evidence is primarily **aggregated disease-level literature assembled from individually evaluated patients**, not an EHR-derived population dataset. The largest study combined seven new and 14 previously reported individuals; local clinicians performed phenotyping, and genetic findings came from clinical or research next-generation sequencing. Some data arose through routine clinical care, whereas other cases were recruited through collaborations and GeneMatcher. (nøstvik2021clinicalandmolecular pages 1-2, nøstvik2021clinicalandmolecular pages 2-3)

## 2. Etiology, risk, and protective factors

### Causal factor

The primary and currently sufficient cause is **biallelic germline PUS3 dysfunction**. Both homozygous and compound-heterozygous genotypes occur, establishing autosomal-recessive inheritance. In the 21-person cohort, 10 individuals were homozygous and 11 were compound heterozygous. (nøstvik2021clinicalandmolecular pages 3-5)

The pathogenic mechanism is predominantly loss of effective PUS3 function through truncation, altered initiation/splicing, protein destabilization, or aggregation. Direct cellular evidence shows that some missense alleles can behave as loss-of-function variants through protein instability even when purified enzyme activity appears preserved. (lin2022destabilizationofmutated pages 2-3, lin2022destabilizationofmutated pages 1-2)

### Genetic risk factors

- Two pathogenic/likely pathogenic alleles in trans constitute the principal risk.
- Consanguinity can increase the probability of homozygous disease alleles, as expected for an autosomal-recessive disorder, but it is not required because compound-heterozygous patients are common.
- A recurrent **c.212A>G, p.Tyr71Cys** allele was reported at approximately 0.0001 in Europeans in gnomAD; the 2021 cohort found all disease-associated variants absent or extremely rare and none homozygous in gnomAD. (lin2022destabilizationofmutated pages 13-13, nøstvik2021clinicalandmolecular pages 3-5)
- No validated modifier gene, susceptibility locus, protective allele, founder effect, or penetrance-reducing allele has been demonstrated.

### Environmental, lifestyle, infectious, and protective factors

No environmental toxin, infection, diet, activity pattern, parental age effect, or lifestyle exposure is known to cause or materially modify PUS3-related disorder. Fever triggered seizures in one severely affected infant, but this represents a seizure precipitant rather than disease causation. No genetic or environmental protective factors have been established. (fang2020compoundheterozygousmutations pages 1-3)

There is no demonstrated gene–environment interaction. The report of anencephaly in four affected fetuses was explicitly interpreted cautiously because other genetic or environmental contributors could not be excluded. (nøstvik2021clinicalandmolecular pages 2-3)

## 3. Phenotypes

The following frequencies derive mainly from the heterogeneous 21-person cohort and use the number actually assessed as denominator. They should not be treated as population prevalence estimates. (nøstvik2021clinicalandmolecular pages 1-2, nøstvik2021clinicalandmolecular pages 2-3)

### Neurodevelopment and behavior

- **Intellectual disability/global developmental delay:** 19/19 assessed (100%). Severity was severe in 9, moderate–severe in 2, moderate in 4, and unspecified in 4; measured IQ in seven ranged from <20 to 58. Suggested HPO: **Intellectual disability, HP:0001249**; **Global developmental delay, HP:0001263**. (nøstvik2021clinicalandmolecular pages 3-5, nøstvik2021clinicalandmolecular pages 2-3)
- **Speech impairment:** 11/11 documented (100%), often severe; one child spoke first single words at age eight. Suggested HPO: **Delayed speech and language development, HP:0000750**; absent or severely limited speech where applicable. (lin2022destabilizationofmutated pages 7-8, nøstvik2021clinicalandmolecular pages 1-2)
- **Motor delay:** 16/18 (88%). Suggested HPO: **Motor delay, HP:0001270**. (nøstvik2021clinicalandmolecular pages 2-3)
- **Behavioral abnormalities:** anxiety, attention disorder, or aggression in 11 individuals; autism-spectrum features in 4/6 specifically assessed. Suggested HPO: **Abnormality of behavior, HP:0000708**, **Autistic behavior, HP:0000729**, anxiety, attention deficit, and aggressive behavior terms. These findings affect education, social participation, supervision needs, and family burden, although no formal EQ-5D, SF-36, PROMIS, or caregiver-burden study exists. (nøstvik2021clinicalandmolecular pages 3-5)

### Neurologic features

- **Hypotonia:** 10/13 (77%); three patients reportedly improved, indicating that hypotonia need not be relentlessly progressive. One individual had upper-extremity hypertonia. Suggested HPO: **Hypotonia, HP:0001252**. (nøstvik2021clinicalandmolecular pages 3-5, nøstvik2021clinicalandmolecular pages 1-2)
- **Epilepsy:** 13/18 (72%). Onset ranged from 1.5 months to 18 years, with reported median 22.5 months. Tonic, generalized tonic-clonic, focal, atypical absence, infantile spasms, myoclonic, and atonic seizures occurred. Frequency ranged from multiple daily events to monthly seizures. Suggested HPO: **Seizure, HP:0001250**, with seizure-subtype terms assigned patient by patient. (nøstvik2021clinicalandmolecular pages 2-3)
- **EEG:** Nine had documented EEGs; three showed epileptiform discharges, including multifocal abnormalities or generalized spike-and-slow-wave activity. A severely affected infant had slow background rhythm. (fang2020compoundheterozygousmutations pages 1-3, nøstvik2021clinicalandmolecular pages 2-3)
- **Microcephaly:** 12 individuals had head circumference at or below the third percentile; the aggregate microcephaly/anencephaly count was 13/18 (72%). Suggested HPO: **Microcephaly, HP:0000252**. Four fetuses classified as one study individual had anencephaly, but causation by PUS3 alone remains uncertain. (nøstvik2021clinicalandmolecular pages 2-3)

### Imaging, growth, skeletal, ocular, and other findings

- **Brain MRI abnormality:** 11/15 (73%), versus four normal scans. Hypoplasia or atrophy occurred in seven and white-matter abnormalities in five. Other isolated findings included dilated cisterna magna and enlarged frontotemporal extracerebral spaces. Normal MRI does not exclude the disorder. Suggested HPO: cerebral atrophy, white-matter abnormality, and mega cisterna magna terms as appropriate. (fang2020compoundheterozygousmutations pages 1-3, nøstvik2021clinicalandmolecular pages 2-3)
- **Short stature:** 10/17 (59%); eight had height at or below the third percentile. Suggested HPO: **Short stature, HP:0004322**. (nøstvik2021clinicalandmolecular pages 2-3)
- **Scoliosis:** 8/10 (80%), ranging from mild to severe. Whether primary or secondary to hypotonia, neurologic impairment, and immobility is unresolved. Suggested HPO: **Scoliosis, HP:0002650**. (nøstvik2021clinicalandmolecular pages 2-3)
- **Facial dysmorphism:** 17/18 (94%), but without a recognizable gestalt. Suggested HPO: **Abnormal facial shape, HP:0001999**, followed by patient-specific features such as depressed nasal bridge or micrognathia. (fang2020compoundheterozygousmutations pages 1-3, nøstvik2021clinicalandmolecular pages 2-3)
- **Gray/blue sclera:** only seven individuals overall, making it neither sensitive nor obligatory despite inclusion in NEDMIGS. Suggested HPO: **Blue sclerae, HP:0000592**. (nøstvik2021clinicalandmolecular pages 2-3, nøstvik2021clinicalandmolecular pages 1-2)
- Reported additional findings include nystagmus, optic-disc pallor, astigmatism, hearing loss, excessive drooling, incontinence, atrial septal defect, patent foramen ovale, delayed bone age, and nephropathy in isolated reports. Evidence is insufficient to define their disease-wide frequencies. (fang2020compoundheterozygousmutations pages 1-3, lin2022destabilizationofmutated pages 7-8, nøstvik2021clinicalandmolecular pages 5-6)

## 4. Genetic and molecular information

### Gene and protein

**PUS3** encodes a highly conserved, 481-amino-acid TruA/Pus3-family pseudouridine synthase. It is reported in cytoplasmic and mitochondrial compartments and modifies tRNA anticodon-loop uridines, particularly positions 38 and 39. (nøstvik2021clinicalandmolecular pages 1-2)

Suggested annotations include:

- Gene: **PUS3**; verify current HGNC identifier directly in HGNC before database loading.
- GO molecular function: pseudouridine synthase activity; RNA binding; tRNA binding.
- GO biological process: tRNA pseudouridine synthesis, tRNA modification, tRNA stabilization, translation.
- GO cellular component: cytoplasm and mitochondrion, noting that disease-specific compartmental effects remain incompletely tested.

### Variant spectrum

The 2021 series contained **17 distinct variants**: eight missense, seven protein-truncating variants—three nonsense, two single-base deletions, and two single-base duplications—one splice-region variant, and one initiation-codon substitution. Eight families carried at least one null allele; seven families carried two missense alleles. (nøstvik2021clinicalandmolecular pages 3-5)

Documented examples include:

- **c.1303C>T, p.Arg435Ter**, homozygous, foundational Saudi-family truncating allele.
- **c.55C>T, p.Arg19Ter** and **c.620dupT, p.Thr208AsnfsTer14**, compound heterozygous in a severely affected Chinese infant. (fang2020compoundheterozygousmutations pages 1-3)
- **c.212A>G, p.Tyr71Cys**, homozygous or in trans with **c.896T>C, p.Ile299Thr**. (lin2022destabilizationofmutated pages 13-13, lin2022destabilizationofmutated pages 2-3)
- Additional reported alleles include p.Tyr160Ter, p.Arg280Ter, p.Arg193Gln, p.Leu21Arg, p.Cys190Tyr, p.Val279Phe, p.Leu366Pro, and p.Ser394CysfsTer18. (nøstvik2021clinicalandmolecular pages 3-5, nøstvik2021clinicalandmolecular pages 5-6)

Variants are germline. No disease-causing somatic PUS3 mechanism, chromosomal rearrangement, aneuploidy, repeat expansion, or mitochondrial-DNA variant has been established. ACMG/AMP classifications should be assigned per variant and laboratory evidence; the cohort used ACMG/AMP interpretation, gnomAD, CADD, SpliceAI, segregation testing, and HGVS nomenclature. (nøstvik2021clinicalandmolecular pages 2-3)

### Functional consequences

For p.Tyr71Cys, purified PUS3 showed similar tRNA binding and pseudouridylation to wild type, but reduced thermostability and near-complete depletion in patient fibroblasts. p.Ile299Thr promoted aggregation. Patient cells had markedly reduced PUS3-dependent pseudouridine, providing direct functional support for loss of effective enzyme activity. Structural modeling placed residues 71–88 and 227–238 in predicted tRNA-binding finger loops analogous to bacterial TruA. (lin2022destabilizationofmutated pages 10-10, lin2022destabilizationofmutated pages 2-3, lin2022destabilizationofmutated pages 7-8, lin2022destabilizationofmutated pages 1-2)

No validated modifier genes, disease-associated methylation signature, chromatin abnormality, or recurrent large PUS3-containing copy-number alteration was identified.

## 5. Environmental information

PUS3-related disorder is genetic, not infectious, toxic, occupational, nutritional, or lifestyle-mediated. No smoking, alcohol, exercise, diet, pollution, radiation, or infectious-agent relationship has been demonstrated. Standard healthy-lifestyle measures remain appropriate for general health but are not primary prevention of the molecular disorder.

## 6. Mechanism and pathophysiology

### Supported causal chain

1. **Upstream trigger:** biallelic pathogenic PUS3 variants.
2. **Protein-level defect:** absent/truncated protein or missense-induced instability/aggregation.
3. **Biochemical defect:** deficient PUS3-mediated conversion of uridine to pseudouridine in tRNA, especially anticodon-loop U38/U39.
4. **RNA-level consequence:** impaired tRNA stabilization, maturation/biogenesis, anticodon-loop function, and translational efficiency or accuracy.
5. **Cellular consequence:** altered protein synthesis and cellular homeostasis during development; mitochondrial dysfunction has been proposed because PUS3 is also localized to mitochondria, but it has not been directly demonstrated in disease cells.
6. **Tissue consequence:** disproportionate impairment of developing nervous-system function, producing developmental delay, intellectual disability, epilepsy, hypotonia, microcephaly, and variable structural brain abnormalities. (lin2022destabilizationofmutated pages 2-3, nøstvik2021clinicalandmolecular pages 3-5, nøstvik2021clinicalandmolecular pages 1-2)

The 2021 paper concluded that biallelic variants likely cause “inefficient post-transcriptional modification of tRNA resulting in an impaired tRNA biogenesis,” followed by abnormal brain development. The 2022 study provided the missing direct bridge by showing reduced PUS3 protein and pseudouridine in patient cells. (lin2022destabilizationofmutated pages 1-2, nøstvik2021clinicalandmolecular pages 3-5)

### What remains inferential

No PUS3-specific evidence establishes activation of Wnt, MAPK, mTOR, PI3K–AKT, apoptosis, autophagy, inflammation, oxidative stress, fibrosis, or immune pathways. Likewise, no disease-specific metabolomic, lipidomic, proteomic, transcriptomic, single-cell, spatial-transcriptomic, organoid, or integrated multi-omic signature has been validated. Human mRNA targets of PUS3 were explicitly described as still requiring investigation. (lin2022destabilizationofmutated pages 13-14)

Suggested GO processes include tRNA pseudouridylation, tRNA modification, RNA stabilization, translation, nervous-system development, and cognition. Candidate cell-type annotations should be conservative: **neuron (CL:0000540)** and neural progenitor cell are biologically plausible, but no patient single-cell study identifies a selectively vulnerable cell population.

## 7. Anatomical structures affected

The **central nervous system** is primary. Suggested anatomy terms include brain (**UBERON:0000955**), cerebral cortex, cerebral white matter, and cerebellum only when supported by individual imaging. The abnormalities can be diffuse or region-specific, and no consistent lateralization is reported. (nøstvik2021clinicalandmolecular pages 2-3)

Secondary systems may include skeletal muscle/tone regulation, axial skeleton, growth, eye, hearing, and—rarely—heart or kidney. Evidence does not establish a single primary non-neural target organ. At the subcellular level, the relevant compartments are cytoplasm and mitochondria; the direct biochemical substrate is tRNA. (nøstvik2021clinicalandmolecular pages 1-2, fang2020compoundheterozygousmutations pages 1-3, nøstvik2021clinicalandmolecular pages 5-6)

## 8. Temporal development

The disorder is congenital in molecular origin, with clinical recognition usually in infancy or childhood through delayed milestones, hypotonia, growth abnormalities, microcephaly, or seizures. Epilepsy onset is highly variable, from 1.5 months to 18 years. (nøstvik2021clinicalandmolecular pages 2-3)

The available age range—8 months to 44 years—shows survival into adulthood but is insufficient for life-expectancy estimates. Developmental disability is chronic and likely lifelong. Hypotonia improved in three patients, whereas developmental gains may continue slowly; there is no evidence of remission of the underlying disorder. White-matter abnormalities or atrophy do not yet establish a progressive neurodegenerative course. (nøstvik2021clinicalandmolecular pages 3-5, nøstvik2021clinicalandmolecular pages 2-3)

No validated disease stages, progression rate, critical therapeutic window, or longitudinal natural-history trajectory exists.

## 9. Inheritance and population

Inheritance is **autosomal recessive**. For two heterozygous carrier parents, standard Mendelian counseling gives a 25% affected, 50% carrier, and 25% non-carrier probability for each pregnancy, assuming both familial alleles are confirmed and no unusual mechanism intervenes.

Penetrance among individuals with clearly deleterious biallelic variants appears high, but the dataset is too small and clinically ascertained to quantify penetrance. Expressivity is variable, ranging from moderate intellectual disability to severe epileptic encephalopathy with multiple anomalies. Anticipation is not expected and has not been reported. Germline mosaicism has not been documented but cannot be excluded in apparently de novo situations.

No incidence or prevalence per 100,000 is available. At least 21 individuals from 15 families were synthesized in 2021, but this is a literature count, not epidemiology. Ages ranged from 8 months to 44 years, with no observed sex difference. Cases originated from multiple geographic and ancestral backgrounds, including Saudi, Ukrainian/European, Chinese, and other international families; no robust ethnic risk or founder distribution is established. (nøstvik2021clinicalandmolecular pages 2-3)

## 10. Diagnostics

### Clinical suspicion

Consider PUS3 testing in unexplained developmental delay/intellectual disability—especially severe speech delay—with any combination of epilepsy, hypotonia, microcephaly, short stature, scoliosis, behavioral abnormalities, or nonspecific dysmorphism. Gray sclera can support suspicion but its absence is not exclusionary. Normal MRI and a non-epileptiform routine EEG also do not exclude the condition. (lin2022destabilizationofmutated pages 7-8, nøstvik2021clinicalandmolecular pages 1-2, nøstvik2021clinicalandmolecular pages 2-3)

### Recommended molecular approach

1. **Trio exome or genome sequencing** is the most efficient approach because the phenotype is nonspecific and genetically heterogeneous.
2. A comprehensive neurodevelopmental-disorder/intellectual-disability/epilepsy panel should include **PUS3** and detect single-nucleotide and small insertion/deletion variants.
3. Confirm candidate variants by an orthogonal method where required and perform parental segregation/phasing to establish biallelic inheritance in trans.
4. Ensure copy-number calling or deletion/duplication analysis if only one pathogenic allele is found.
5. RNA studies may clarify suspected splice variants; patient fibroblast protein or pseudouridine assays remain research-level functional tests rather than routine diagnostics.

The principal cohort used exome sequencing, whole-genome sequencing, or virtual gene panels, followed by family testing. (nøstvik2021clinicalandmolecular pages 2-3)

CMA can detect alternative diagnoses and large deletions but will miss most PUS3 sequence variants. Karyotype, FISH, mitochondrial DNA analysis, and repeat-expansion assays are not disease-specific tests. No blood metabolite, enzyme assay, biopsy, proteomic, epigenomic, or liquid-biopsy biomarker is validated; one severe infant had normal blood and urine metabolic screening. (fang2020compoundheterozygousmutations pages 1-3)

### Differential diagnosis

The differential includes other tRNA-modification and RNA-processing disorders, PUS7-related neurodevelopmental disorder, PUS1-associated MLASA, aminoacyl-tRNA synthetase disorders, mitochondrial disease, developmental and epileptic encephalopathies, pontocerebellar hypoplasias, and syndromic microcephaly. Distinction requires molecular testing because the clinical gestalt is not specific.

## 11. Outcome and prognosis

No survival curves, mortality rate, life-expectancy estimate, or five-/ten-year outcome data exist. Survival to age 44 years was represented in the aggregate cohort, but this does not establish normal longevity. (nøstvik2021clinicalandmolecular pages 2-3)

Long-term morbidity is principally neurodevelopmental: intellectual disability, limited communication, epilepsy, motor impairment, behavioral difficulties, scoliosis, and dependence in activities of daily living. Some individuals require continence support and intensive rehabilitation. Formal quality-of-life instruments have not been reported. (lin2022destabilizationofmutated pages 7-8, nøstvik2021clinicalandmolecular pages 3-5)

Seizure outcome is variable: only 3/7 individuals with available treatment-response data achieved seizure freedom. Prognostic biomarkers and reliable genotype–phenotype rules are unavailable. Null alleles and very early epileptic encephalopathy may indicate greater severity, but available numbers do not justify a definitive prediction. (fang2020compoundheterozygousmutations pages 1-3, nøstvik2021clinicalandmolecular pages 2-3)

## 12. Treatment

No therapy corrects PUS3 deficiency or restores tRNA pseudouridylation in patients. No gene replacement, gene editing, RNA therapy, cell therapy, targeted small molecule, or immunotherapy has entered disease-specific clinical testing.

Current management is multidisciplinary and symptom-directed:

- **Epilepsy:** antiseizure medication selected by seizure type and standard pediatric/adult epilepsy practice; EEG follow-up when clinically indicated. Sodium valproate produced incomplete control in one infant, while aggregate response varied and 3/7 became seizure-free. This is insufficient to recommend one preferred drug. Suggested NCIT concepts: anticonvulsant therapy and seizure management. (fang2020compoundheterozygousmutations pages 1-3, nøstvik2021clinicalandmolecular pages 2-3)
- **Development:** early physical, occupational, speech/language, augmentative-communication, behavioral, and educational intervention. One reported child received intensive rehabilitation. Suggested NCIT concepts: physical therapy, occupational therapy, speech therapy, rehabilitation therapy. (lin2022destabilizationofmutated pages 7-8)
- **Nutrition/growth:** monitor feeding, weight, stature, and bone health; intervene for dysphagia or inadequate intake.
- **Musculoskeletal:** serial examination for scoliosis and contractures, with physiotherapy, orthotics, and orthopedic referral as needed.
- **Vision/hearing:** baseline and symptom-driven ophthalmologic and audiologic assessment.
- **Cardiac/renal:** evaluate when clinically indicated rather than assuming universal involvement.
- **Behavior/sleep:** standard neurodevelopmental behavioral assessment and individualized interventions.

No PUS3-specific pharmacogenomic recommendation or treatment-response rate exists beyond sparse case data.

## 13. Prevention

Primary prevention by lifestyle change, vaccination, toxin avoidance, or prophylactic medication is not applicable. The principal preventive strategy is **genetic counseling and reproductive risk assessment**.

Once familial variants are known, options include carrier testing of adult relatives, cascade testing, prenatal diagnosis, and preimplantation genetic testing for monogenic disease. Early molecular diagnosis is secondary prevention in the sense that it can prompt epilepsy surveillance, developmental therapy, hearing/vision assessment, and scoliosis monitoring before avoidable complications accumulate. Tertiary prevention consists of seizure control, mobility support, communication intervention, nutritional management, and orthopedic surveillance.

Population newborn screening is not available or justified by current evidence. Routine population carrier screening has not been established; targeted testing is most appropriate in known families.

## 14. Other species and natural disease

PUS3/TruA-family enzymes are evolutionarily conserved across bacteria, yeast, plants, invertebrates, and mammals. Comparative proteins referenced in structural analyses include mouse Pus3, Drosophila Pus3, yeast Deg1, bacterial TruA, Arabidopsis Pus, and archaeal homologs. (lin2022destabilizationofmutated pages 7-8)

No naturally occurring veterinary PUS3 neurodevelopmental syndrome, breed association, zoonotic transmission, or cross-species infectious susceptibility was identified. Zoonosis is not applicable.

## 15. Model organisms and experimental models

No validated **Pus3** knockout or knock-in animal model that demonstrably recapitulates the human syndrome was identified in the reviewed evidence. Consequently, there are no established mouse, zebrafish, Drosophila, organoid, or iPSC resources for therapeutic efficacy testing specific to this disorder.

Existing experimental systems include:

- Patient-derived fibroblasts for PUS3 protein abundance, mRNA expression, and PUS3-dependent pseudouridine measurements.
- Recombinant wild-type and mutant human PUS3 expressed in insect cells.
- In-vitro-transcribed human and yeast tRNA substrates.
- EMSA and microscale thermophoresis for tRNA binding, pseudouridylation assays, gel filtration, nanoDSF/DLS for stability and aggregation, western blotting, quantitative PCR, and AlphaFold2-guided structural interpretation. (lin2022destabilizationofmutated pages 10-10, lin2022destabilizationofmutated pages 5-6, lin2022destabilizationofmutated pages 1-2)

These systems establish biochemical pathogenicity but cannot model brain development, circuit dysfunction, seizures, cognition, or whole-organism treatment response. Priority models are patient iPSC-derived neural progenitors and neurons, cerebral organoids, and a viable conditional Pus3 loss-of-function mouse or zebrafish model.

## Recent developments and evidence gaps

The most important disease-specific advances remain the 2021 clinical delineation and the 2022 patient-cell mechanism study. The latter’s key abstract conclusion was that the results “directly illustrate the link between the identified PUS3 variants and reduced Ψ levels in the patient cells.” (lin2022destabilizationofmutated pages 1-2)

Recent 2023–2024 work in the broader field has emphasized RNA modification as a developmental and neurologic regulatory layer, but no comparably large 2023–2024 PUS3 clinical cohort, natural-history study, trial, or therapeutic implementation was identified. The highest priorities are prospective international registry development; standardized HPO phenotyping; longitudinal epilepsy, MRI, growth, and functional outcomes; functional classification of all missense/splice alleles; direct mapping of PUS3-dependent RNA targets in neural cells; mitochondrial studies; and disease-relevant animal and iPSC models.

## Key publications and URLs

1. **Nøstvik et al. Clinical and molecular delineation of PUS3-associated neurodevelopmental disorders.** *Clinical Genetics*. Published online August 2021; 100:628–633. DOI/URL: https://doi.org/10.1111/cge.14051. This is the principal 21-individual clinical synthesis. (nøstvik2021clinicalandmolecular pages 1-2)
2. **Lin et al. Destabilization of mutated human PUS3 protein causes intellectual disability.** *Human Mutation*. Published October 2022; 43:2063–2078. DOI/URL: https://doi.org/10.1002/humu.24471. This provides the strongest patient-cell and recombinant-protein mechanism evidence. (lin2022destabilizationofmutated pages 13-13, lin2022destabilizationofmutated pages 1-2)
3. **Fang et al. Compound heterozygous mutations in PUS3 gene identified in a Chinese infant with severe epileptic encephalopathy and multiple malformations.** *Neurological Sciences*. 2020;41:465–467. DOI/URL: https://doi.org/10.1007/s10072-019-04049-1. (fang2020compoundheterozygousmutations pages 1-3)
4. **Shaheen et al. A homozygous truncating mutation in PUS3 expands the role of tRNA modification in normal cognition.** *Human Genetics*. 2016;135:707–713. DOI/URL: https://doi.org/10.1007/s00439-016-1665-7. The report introduced the homozygous p.Arg435Ter association and demonstrated reduced post-transcriptional tRNA modification, as summarized in the later cohort. (nøstvik2021clinicalandmolecular pages 3-5, nøstvik2021clinicalandmolecular pages 5-6)

PMIDs were not present in the retrieved full-text evidence and therefore are not supplied rather than risk introducing unverified identifiers.

References

1. (nøstvik2021clinicalandmolecular pages 2-3): Miriam Nøstvik, Sarah M. Kateta, Bitten Schönewolf‐Greulich, Alexandra Afenjar, Magalie Barth, Felix Boschann, Diane Doummar, Tobias B. Haack, Boris Keren, Ludmila A. Livshits, Davide Mei, Joohyun Park, Tiziana Pisano, Clement Prouteau, Muhammad Umair, Ahmed Waqas, Alban Ziegler, Renzo Guerrini, Rikke S. Møller, and Zeynep Tümer. Clinical and molecular delineation of <scp><i>pus3</i></scp>‐associated neurodevelopmental disorders. Clinical Genetics, 100:628-633, Aug 2021. URL: https://doi.org/10.1111/cge.14051, doi:10.1111/cge.14051. This article has 40 citations and is from a peer-reviewed journal.

2. (nøstvik2021clinicalandmolecular pages 1-2): Miriam Nøstvik, Sarah M. Kateta, Bitten Schönewolf‐Greulich, Alexandra Afenjar, Magalie Barth, Felix Boschann, Diane Doummar, Tobias B. Haack, Boris Keren, Ludmila A. Livshits, Davide Mei, Joohyun Park, Tiziana Pisano, Clement Prouteau, Muhammad Umair, Ahmed Waqas, Alban Ziegler, Renzo Guerrini, Rikke S. Møller, and Zeynep Tümer. Clinical and molecular delineation of <scp><i>pus3</i></scp>‐associated neurodevelopmental disorders. Clinical Genetics, 100:628-633, Aug 2021. URL: https://doi.org/10.1111/cge.14051, doi:10.1111/cge.14051. This article has 40 citations and is from a peer-reviewed journal.

3. (lin2022destabilizationofmutated pages 13-13): Ting‐Yu Lin, Robert Smigiel, Bozena Kuzniewska, Joanna J. Chmielewska, Joanna Kosińska, Mateusz Biela, Anna Biela, Anna Kościelniak, Dominika Dobosz, Izabela Laczmanska, Andrzej Chramiec‐Głąbik, Jakub Jeżowski, Jakub Nowak, Monika Gos, Sylwia Rzonca‐Niewczas, Magdalena Dziembowska, Rafał Ploski, and Sebastian Glatt. Destabilization of mutated human pus3 protein causes intellectual disability. Human Mutation, 43:2063-2078, Oct 2022. URL: https://doi.org/10.1002/humu.24471, doi:10.1002/humu.24471. This article has 30 citations and is from a domain leading peer-reviewed journal.

4. (lin2022destabilizationofmutated pages 2-3): Ting‐Yu Lin, Robert Smigiel, Bozena Kuzniewska, Joanna J. Chmielewska, Joanna Kosińska, Mateusz Biela, Anna Biela, Anna Kościelniak, Dominika Dobosz, Izabela Laczmanska, Andrzej Chramiec‐Głąbik, Jakub Jeżowski, Jakub Nowak, Monika Gos, Sylwia Rzonca‐Niewczas, Magdalena Dziembowska, Rafał Ploski, and Sebastian Glatt. Destabilization of mutated human pus3 protein causes intellectual disability. Human Mutation, 43:2063-2078, Oct 2022. URL: https://doi.org/10.1002/humu.24471, doi:10.1002/humu.24471. This article has 30 citations and is from a domain leading peer-reviewed journal.

5. (lin2022destabilizationofmutated pages 1-2): Ting‐Yu Lin, Robert Smigiel, Bozena Kuzniewska, Joanna J. Chmielewska, Joanna Kosińska, Mateusz Biela, Anna Biela, Anna Kościelniak, Dominika Dobosz, Izabela Laczmanska, Andrzej Chramiec‐Głąbik, Jakub Jeżowski, Jakub Nowak, Monika Gos, Sylwia Rzonca‐Niewczas, Magdalena Dziembowska, Rafał Ploski, and Sebastian Glatt. Destabilization of mutated human pus3 protein causes intellectual disability. Human Mutation, 43:2063-2078, Oct 2022. URL: https://doi.org/10.1002/humu.24471, doi:10.1002/humu.24471. This article has 30 citations and is from a domain leading peer-reviewed journal.

6. (nøstvik2021clinicalandmolecular pages 3-5): Miriam Nøstvik, Sarah M. Kateta, Bitten Schönewolf‐Greulich, Alexandra Afenjar, Magalie Barth, Felix Boschann, Diane Doummar, Tobias B. Haack, Boris Keren, Ludmila A. Livshits, Davide Mei, Joohyun Park, Tiziana Pisano, Clement Prouteau, Muhammad Umair, Ahmed Waqas, Alban Ziegler, Renzo Guerrini, Rikke S. Møller, and Zeynep Tümer. Clinical and molecular delineation of <scp><i>pus3</i></scp>‐associated neurodevelopmental disorders. Clinical Genetics, 100:628-633, Aug 2021. URL: https://doi.org/10.1111/cge.14051, doi:10.1111/cge.14051. This article has 40 citations and is from a peer-reviewed journal.

7. (lin2022destabilizationofmutated pages 7-8): Ting‐Yu Lin, Robert Smigiel, Bozena Kuzniewska, Joanna J. Chmielewska, Joanna Kosińska, Mateusz Biela, Anna Biela, Anna Kościelniak, Dominika Dobosz, Izabela Laczmanska, Andrzej Chramiec‐Głąbik, Jakub Jeżowski, Jakub Nowak, Monika Gos, Sylwia Rzonca‐Niewczas, Magdalena Dziembowska, Rafał Ploski, and Sebastian Glatt. Destabilization of mutated human pus3 protein causes intellectual disability. Human Mutation, 43:2063-2078, Oct 2022. URL: https://doi.org/10.1002/humu.24471, doi:10.1002/humu.24471. This article has 30 citations and is from a domain leading peer-reviewed journal.

8. (fang2020compoundheterozygousmutations pages 1-3): Hongjun Fang, Lily Zhang, Bo Xiao, Hongyu Long, and Liming Yang. Compound heterozygous mutations in pus3 gene identified in a chinese infant with severe epileptic encephalopathy and multiple malformations. Neurological Sciences, 41:465-467, Aug 2020. URL: https://doi.org/10.1007/s10072-019-04049-1, doi:10.1007/s10072-019-04049-1. This article has 11 citations and is from a peer-reviewed journal.

9. (nøstvik2021clinicalandmolecular pages 5-6): Miriam Nøstvik, Sarah M. Kateta, Bitten Schönewolf‐Greulich, Alexandra Afenjar, Magalie Barth, Felix Boschann, Diane Doummar, Tobias B. Haack, Boris Keren, Ludmila A. Livshits, Davide Mei, Joohyun Park, Tiziana Pisano, Clement Prouteau, Muhammad Umair, Ahmed Waqas, Alban Ziegler, Renzo Guerrini, Rikke S. Møller, and Zeynep Tümer. Clinical and molecular delineation of <scp><i>pus3</i></scp>‐associated neurodevelopmental disorders. Clinical Genetics, 100:628-633, Aug 2021. URL: https://doi.org/10.1111/cge.14051, doi:10.1111/cge.14051. This article has 40 citations and is from a peer-reviewed journal.

10. (lin2022destabilizationofmutated pages 10-10): Ting‐Yu Lin, Robert Smigiel, Bozena Kuzniewska, Joanna J. Chmielewska, Joanna Kosińska, Mateusz Biela, Anna Biela, Anna Kościelniak, Dominika Dobosz, Izabela Laczmanska, Andrzej Chramiec‐Głąbik, Jakub Jeżowski, Jakub Nowak, Monika Gos, Sylwia Rzonca‐Niewczas, Magdalena Dziembowska, Rafał Ploski, and Sebastian Glatt. Destabilization of mutated human pus3 protein causes intellectual disability. Human Mutation, 43:2063-2078, Oct 2022. URL: https://doi.org/10.1002/humu.24471, doi:10.1002/humu.24471. This article has 30 citations and is from a domain leading peer-reviewed journal.

11. (lin2022destabilizationofmutated pages 13-14): Ting‐Yu Lin, Robert Smigiel, Bozena Kuzniewska, Joanna J. Chmielewska, Joanna Kosińska, Mateusz Biela, Anna Biela, Anna Kościelniak, Dominika Dobosz, Izabela Laczmanska, Andrzej Chramiec‐Głąbik, Jakub Jeżowski, Jakub Nowak, Monika Gos, Sylwia Rzonca‐Niewczas, Magdalena Dziembowska, Rafał Ploski, and Sebastian Glatt. Destabilization of mutated human pus3 protein causes intellectual disability. Human Mutation, 43:2063-2078, Oct 2022. URL: https://doi.org/10.1002/humu.24471, doi:10.1002/humu.24471. This article has 30 citations and is from a domain leading peer-reviewed journal.

12. (lin2022destabilizationofmutated pages 5-6): Ting‐Yu Lin, Robert Smigiel, Bozena Kuzniewska, Joanna J. Chmielewska, Joanna Kosińska, Mateusz Biela, Anna Biela, Anna Kościelniak, Dominika Dobosz, Izabela Laczmanska, Andrzej Chramiec‐Głąbik, Jakub Jeżowski, Jakub Nowak, Monika Gos, Sylwia Rzonca‐Niewczas, Magdalena Dziembowska, Rafał Ploski, and Sebastian Glatt. Destabilization of mutated human pus3 protein causes intellectual disability. Human Mutation, 43:2063-2078, Oct 2022. URL: https://doi.org/10.1002/humu.24471, doi:10.1002/humu.24471. This article has 30 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](PUS3-Related_Neurodevelopmental_Disorder-deep-research-falcon_artifacts/artifact-00.md)