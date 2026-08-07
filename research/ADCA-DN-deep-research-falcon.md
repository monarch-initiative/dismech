---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-31T18:37:00.724220'
end_time: '2026-07-31T18:45:47.463741'
duration_seconds: 526.74
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Autosomal Dominant Cerebellar Ataxia Deafness and Narcolepsy
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 39
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: ADCA-DN-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autosomal Dominant Cerebellar Ataxia Deafness and Narcolepsy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Dominant Cerebellar Ataxia Deafness and Narcolepsy** covering all of the
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
- **Disease Name:** Autosomal Dominant Cerebellar Ataxia Deafness and Narcolepsy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Dominant Cerebellar Ataxia Deafness and Narcolepsy** covering all of the
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


# Autosomal Dominant Cerebellar Ataxia, Deafness and Narcolepsy (ADCA-DN)

## Executive summary

ADCA-DN is an ultra-rare, progressive, autosomal-dominant neurodegenerative disorder caused by heterozygous **DNMT1** variants, classically missense variants in exon 21 encoding the C-terminal portion of the replication-foci targeting sequence (**RFTS**) domain. The characteristic sequence is adult-onset narcolepsy with cataplexy and sensorineural hearing loss, usually followed by cerebellar ataxia and cognitive/behavioral decline. Optic atrophy, sensory neuropathy, psychiatric manifestations, seizures, dysautonomia, diabetes, and lymphedema broaden the phenotype. ADCA-DN overlaps clinically and mechanistically with hereditary sensory and autonomic neuropathy type 1E (HSAN1E); collectively these are increasingly called **DNMT1-complex disorder**. However, evidence from broader DNMT1 cohorts should not automatically be treated as ADCA-DN-specific. (winkelmann2012mutationsindnmt1 pages 1-2, baets2015defectsofmutant pages 13-14, bi2020expandedgeneticinsight pages 1-2)

The most important recent advance is a 2023 study of patient fibroblasts, induced pluripotent stem cells (iPSCs), and induced neurons, which demonstrated cell-type-specific methylomic and transcriptomic abnormalities and nominated phenotype-related genes including **PDGFB, PRDM8, NR2F1**, and **ZFP57**. A 2024 systematic review independently reaffirmed exon-21 DNMT1 variants as the strongest monogenic methylation-related association with hearing loss. No disease-modifying treatment or disease-specific clinical trial was identified; care remains multidisciplinary and symptomatic. (davis2023mutationsinhuman pages 1-2, patil2024asystematicreview pages 1-2)

| domain | established finding | evidence type/sample | key quantitative detail or variant | source/date/DOI |
|---|---|---|---|---|
| Identity / IDs | ADCA-DN is a rare Mendelian neurodegenerative syndrome caused by DNMT1; Open Targets maps the disease as MONDO_0011397 and the classic phenotype identifier is OMIM 604121 | Disease database mapping plus human discovery families | DNMT1 is the only associated target in Open Targets evidence returned here; OMIM phenotype number 604121 stated in primary literature | Open Targets association, accessed in tool output (OpenTargets Search: autosomal dominant cerebellar ataxia deafness and narcolepsy-DNMT1); Winkelmann et al., 2012, *Hum Mol Genet*, May 2012, https://doi.org/10.1093/hmg/dds035 (winkelmann2012mutationsindnmt1 pages 1-2) |
| Synonyms / nomenclature | Common names include “autosomal dominant cerebellar ataxia, deafness and narcolepsy” and “ADCA-DN”; later literature places it within broader “DNMT1-complex disorder” because of overlap with HSAN1E | Narrative disease-level synthesis from human cohorts | Distinction remains useful: ADCA-DN classically maps to exon 21 / C-terminal RFTS variants, HSAN1E more often exon 20 / N-terminal-middle RFTS variants | Baets et al., 2015, *Brain*, Apr 2015, https://doi.org/10.1093/brain/awv010 (baets2015defectsofmutant pages 13-14, baets2015defectsofmutant pages 1-1, baets2015defectsofmutant pages 14-15); Bi et al., 2020, *Neurol Genet*, Aug 2020, https://doi.org/10.1212/NXG.0000000000000456 (bi2020expandedgeneticinsight pages 1-2) |
| Causal gene / variants | The landmark ADCA-DN variants are heterozygous missense DNMT1 exon 21 variants affecting the RFTS domain | Human exome/Sanger family studies | p.Ala570Val, p.Gly605Ala, p.Val606Phe; one report described a de novo exon 21 mutation in a Brazilian patient | Winkelmann et al., 2012, May 2012, https://doi.org/10.1093/hmg/dds035 (winkelmann2012mutationsindnmt1 pages 1-2, winkelmann2012mutationsindnmt1 pages 2-3); Pedroso et al., 2013, *Sleep*, Aug 2013, https://doi.org/10.5665/sleep.2898 |
| Inheritance / onset | Autosomal dominant inheritance with age-dependent, usually adult onset | Human pedigrees | Typical onset in 30s–40s; narcolepsy-cataplexy and deafness often precede ataxia and dementia | Winkelmann et al., 2012, May 2012, https://doi.org/10.1093/hmg/dds035 (winkelmann2012mutationsindnmt1 pages 1-2, winkelmann2012mutationsindnmt1 pages 2-3); Moghadam et al., 2014, *Sleep Med*, May 2014, https://doi.org/10.1016/j.sleep.2013.09.028 (moghadam2014polysomnographicandneurometabolic pages 1-2) |
| Clinical course | Disease is progressive and multisystem neurologic involvement expands over time | Human family cohorts and expanded case series | Early symptoms: narcolepsy/deafness; later cerebellar ataxia, cognitive decline/dementia, optic atrophy, neuropathy, psychiatric manifestations, diabetes mellitus | Winkelmann et al., 2012, May 2012, https://doi.org/10.1093/hmg/dds035 (winkelmann2012mutationsindnmt1 pages 1-2); Davis et al., 2023, *Hum Mol Genet*, Aug 2023, https://doi.org/10.1093/hmg/ddad123 (davis2023mutationsinhuman pages 1-2) |
| Core phenotypes | Canonical phenotype triad is narcolepsy/cataplexy, sensorineural deafness, and cerebellar ataxia; dementia is frequent later | Human clinical cohorts | CSF hypocretin-1 reported low/undetectable in the discovery paper; additional features can include optic atrophy, hallucinations, seizures, lymphedema, neuropathy | Winkelmann et al., 2012, May 2012, https://doi.org/10.1093/hmg/dds035 (winkelmann2012mutationsindnmt1 pages 1-2, winkelmann2012mutationsindnmt1 pages 4-5); Baets et al., 2015, Apr 2015, https://doi.org/10.1093/brain/awv010 (baets2015defectsofmutant pages 13-14, baets2015defectsofmutant pages 14-15) |
| Presymptomatic / early markers | Sleep and metabolic abnormalities may predate overt neurologic symptoms in mutation carriers | Human presymptomatic family study | In 2 asymptomatic daughters, SOREMPs were detected and proton MRS showed increased cerebellar myoinositol despite normal neurologic exam, audiometry, ophthalmology, and structural MRI | Moghadam et al., 2014, May 2014, https://doi.org/10.1016/j.sleep.2013.09.028 (moghadam2014polysomnographicandneurometabolic pages 1-2) |
| Imaging / neurophysiology | Neuroimaging can show brain or spinal changes; neurophysiology often supports sensory axonal neuropathy | Human case series | Global brain atrophy in 12/14 MRI cases in broader DNMT1 disorder cohort; case reports include T2 hyperintense enhancing lesions, PET hypometabolism, posterior column atrophy, abnormal evoked potentials | Baets et al., 2015, Apr 2015, https://doi.org/10.1093/brain/awv010 (baets2015defectsofmutant pages 1-1); Bi et al., 2020, Aug 2020, https://doi.org/10.1212/NXG.0000000000000456 (bi2020expandedgeneticinsight pages 1-2) |
| Prognosis / natural history | Available natural-history evidence suggests substantial morbidity and reduced survival, but data are sparse and mostly from aggregated DNMT1-complex cohorts rather than pure ADCA-DN cohorts | Human retrospective cohort | Mean onset 37.7 years and average survival 53.6 years in Baets et al.; cognitive decline in 89% by age 45 in that broader cohort | Baets et al., 2015, Apr 2015, https://doi.org/10.1093/brain/awv010 (baets2015defectsofmutant pages 1-1) |
| Molecular mechanism | ADCA-DN variants localize to the DNMT1 RFTS domain, disrupting maintenance methylation and protein behavior; disease mechanism is not simple haploinsufficiency | Human genetics, cell biology, mechanistic review | A570V/G605A/V606F weaken RFTS-catalytic domain interaction; mutant DNMT1 can mislocalize, lose heterochromatin binding, aggregate, and drive aggresome/autophagy-related proteostasis defects | Baets et al., 2015, Apr 2015, https://doi.org/10.1093/brain/awv010 (baets2015defectsofmutant pages 1-1); Davletgildeeva & Kuznetsov, 2024, *Biomolecules*, Sep 2024, https://doi.org/10.3390/biom14091117 (davletgildeeva2024theroleof pages 5-7) |
| 2023 iPSC / iNeuron omics | Patient-derived fibroblasts, iPSCs, and induced neurons show cell-type-specific methylome/transcriptome disruption in ADCA-DN | Human in vitro disease models | Variants studied: Ala570Val, Gly605Ala, Val606Phe; methylation and expression were negatively correlated in iPSCs/iNs; ZFP57 promoter hypomethylation/upregulation; phenotype-linked genes included PDGFB, PRDM8, NR2F1 | Davis et al., 2023, Aug 2023, https://doi.org/10.1093/hmg/ddad123 (davis2023mutationsinhuman pages 1-2) |
| Additional mechanistic models | RFTS mutations can trigger instability and internal cleavage of DNMT1, implying mixed loss- and gain-of-function effects | Mouse and cell models, primarily HSAN1E-oriented but mechanistically relevant to DNMT1 RFTS disease | Specific truncated ~75–80 kDa DNMT1 species near aa ~501 proposed; heterozygous knock-in mice had reduced DNMT1 and impaired learning/memory; homozygous mutants died around E10.5 | Wang et al., 2021, *Sci Adv*, Sep 2021, https://doi.org/10.1126/sciadv.abe8511 (wang2021mutationinduceddnmt1cleavage pages 12-13, wang2021mutationinduceddnmt1cleavage pages 1-2) |
| Diagnostics | Diagnosis is primarily molecular, supported by characteristic sleep/hearing/ataxia/cognitive phenotype and family history; WES/WGS can be especially useful when phenotype is atypical or overlaps neuromuscular disease | Human genetics case reports and clinic practice article | Sanger sequencing of DNMT1 exon 21 was used in targeted familial testing; later literature emphasizes WES/WGS to improve diagnostic yield in adults | Moghadam et al., 2014, May 2014, https://doi.org/10.1016/j.sleep.2013.09.028 (moghadam2014polysomnographicandneurometabolic pages 1-2); Dratch et al., 2024, *Biology*, Feb 2024, https://doi.org/10.3390/biology13020093 (dratch2024theimportanceof pages 1-2) |
| Real-world intervention | Cochlear implantation can improve hearing in DNMT1-complex disorder and is the clearest disease-specific real-world intervention reported in the retrieved evidence | Human case report within clinical series | One patient with p.T497P had “significant hearing improvements at all tested frequencies (250–6,000 Hz)” after left cochlear implant | Bi et al., 2020, Aug 2020, https://doi.org/10.1212/NXG.0000000000000456 (bi2020expandedgeneticinsight pages 1-2) |
| Supportive care / implementation | Management remains symptomatic and multidisciplinary: sleep medicine, audiology, neurogenetics, rehabilitation, neuropsychology, and genetic counseling | Case-series based care observations | Example supportive measures reported include IV immunoglobulin for hypogammaglobulinemia in one DNMT1-complex case and use of advanced imaging/neurophysiology for surveillance | Bi et al., 2020, Aug 2020, https://doi.org/10.1212/NXG.0000000000000456 (bi2020expandedgeneticinsight pages 1-2); Dratch et al., 2024, Feb 2024, https://doi.org/10.3390/biology13020093 (dratch2024theimportanceof pages 1-2) |
| Epidemiology gap | Extremely rare disease with very few pedigrees described; robust prevalence/incidence estimates are not available in the retrieved evidence | Literature review and early family reports | Moghadam 2014 states only the original Swedish family plus five further pedigrees recognized worldwide at that time | Moghadam et al., 2014, May 2014, https://doi.org/10.1016/j.sleep.2013.09.028 (moghadam2014polysomnographicandneurometabolic pages 1-2); Patil et al., 2024, Jul 2024, https://doi.org/10.1186/s13148-024-01697-9 (patil2024asystematicreview pages 1-2) |
| Trials gap | No disease-specific interventional clinical trials for ADCA-DN were identified in the retrieved tool results | Clinical trials search result | Tool search found no relevant ADCA-DN/DNMT1 ataxia-deafness-narcolepsy intervention trial | ClinicalTrials.gov tool search in conversation returned no relevant trials (OpenTargets Search: autosomal dominant cerebellar ataxia deafness and narcolepsy-DNMT1) |
| Model limitations | Current models are informative but incomplete for ADCA-DN | Mouse/cell model interpretation | 2021 knock-in mice modeled HSAN1E-equivalent RFTS mutations and noted that full neuronal phenotypes, “including hearing, remain to be determined”; cognitive defects were modest relative to human disease | Wang et al., 2021, Sep 2021, https://doi.org/10.1126/sciadv.abe8511 (wang2021mutationinduceddnmt1cleavage pages 12-13, wang2021mutationinduceddnmt1cleavage pages 1-2) |


*Table: This compact table summarizes the most actionable and best-supported findings for autosomal dominant cerebellar ataxia, deafness and narcolepsy across identity, phenotype, mechanism, diagnostics, and care. It emphasizes where evidence is strong, where newer 2023-2024 data add insight, and where important gaps remain.*

## 1. Disease information

### Definition and classification

ADCA-DN is a Mendelian, multisystem neurological disorder characterized by narcolepsy-cataplexy, sensorineural deafness, cerebellar ataxia, and later dementia or other cognitive-behavioral deterioration. The landmark molecular study described it as a late-onset disorder, typically beginning at 30–40 years, and identified heterozygous DNMT1 mutations in affected members of several kindreds. (winkelmann2012mutationsindnmt1 pages 1-2, winkelmann2012mutationsindnmt1 pages 2-3)

**Recommended identifiers and names**

- **MONDO:** MONDO:0011397.
- **OMIM phenotype:** 604121.
- **Causal gene:** **DNMT1**, Ensembl ENSG00000130816; approved name *DNA methyltransferase 1*.
- **Preferred name:** autosomal dominant cerebellar ataxia, deafness and narcolepsy.
- **Synonyms:** ADCA-DN; cerebellar ataxia–deafness–narcolepsy syndrome; DNMT1-related ADCA-DN.
- **Broader grouping:** DNMT1-complex disorder, encompassing overlapping ADCA-DN and HSAN1E phenotypes.
- **Orphanet, MeSH, ICD-10/ICD-11:** a dedicated code was not established in the retrieved evidence. In practice, component manifestations may be coded separately, but these are not equivalent to a molecular disease identifier. Open Targets returned DNMT1 as the single associated target for MONDO:0011397, supported by five evidence records. (OpenTargets Search: autosomal dominant cerebellar ataxia deafness and narcolepsy-DNMT1)

The evidence is primarily **aggregated disease-level literature derived from small pedigrees and case series**, not population-scale EHR data. Individual-patient observations are embedded in those reports, including presymptomatic carriers and sporadic/de-novo cases. (winkelmann2012mutationsindnmt1 pages 1-2, bi2020expandedgeneticinsight pages 1-2, moghadam2014polysomnographicandneurometabolic pages 1-2)

## 2. Etiology, risk, and protective factors

### Primary cause

The established cause is a heterozygous germline pathogenic variant in **DNMT1**. The original ADCA-DN variants were **p.Ala570Val, p.Gly605Ala, and p.Val606Phe**, all conserved missense changes in exon 21 and spatially clustered in the RFTS domain. A de-novo occurrence of p.Ala570Val and a separate de-novo exon-21 case demonstrate that a negative family history does not exclude the diagnosis. (winkelmann2012mutationsindnmt1 pages 1-2, winkelmann2012mutationsindnmt1 pages 2-3)

### Genetic risk factors

- Carrying a pathogenic DNMT1 allele is the dominant risk factor.
- Classical ADCA-DN variants occur toward the C-terminal RFTS region; HSAN1E variants tend to occur in exon 20 or the N-terminal/middle RFTS region. This relationship is useful but not absolute because expanding case series show overlapping phenotypes and variants outside the classical region. (davis2023mutationsinhuman pages 1-2, baets2015defectsofmutant pages 1-1, bi2020expandedgeneticinsight pages 1-2)
- No validated modifier gene, polygenic risk score, anticipation mechanism, founder allele, or protective allele has been established.
- Population allele-frequency estimates for the individual variants were not available in the retrieved evidence. Their rarity, segregation, de-novo occurrence, conservation, and functional effects support pathogenicity; current classification should be checked in ClinVar/gnomAD using the exact transcript and HGVS expression before clinical reporting.

### Environmental, lifestyle, infectious, and protective factors

No environmental toxin, infection, diet, smoking behavior, occupation, or lifestyle exposure is established as causing or preventing ADCA-DN. Family history is informative because of dominant inheritance, but is not itself an environmental risk factor. Noise exposure can independently worsen hearing, and common DNMT1/DNMT3A polymorphisms have been studied in noise-induced hearing loss, but that evidence concerns a different, multifactorial condition and should not be interpreted as a demonstrated ADCA-DN gene–environment interaction. The 2024 hearing-loss review concluded that broader evidence for functional methylation effects in complex hearing loss remains limited. (patil2024asystematicreview pages 1-2)

## 3. Phenotypes

Because reported cohorts are extremely small, robust ADCA-DN-specific percentages generally do not exist. “Common” below means recurrent across pedigrees, not a validated population frequency.

### Core and expanded manifestations

| Manifestation | Type and typical behavior | Suggested HPO term |
|---|---|---|
| Narcolepsy | Symptom/physiological disorder; often an early manifestation in the third to fifth decade; progressive or persistent | Narcolepsy, **HP:0030050** |
| Cataplexy | Emotion-triggered episodic loss of muscle tone; may accompany narcolepsy and occasionally be prolonged | Cataplexy, **HP:0002524** |
| Excessive daytime sleepiness | Symptom; chronic, functionally disabling | Excessive daytime sleepiness, **HP:0002189** |
| Sensorineural hearing loss | Clinical sign; usually bilateral and progressive; frequently early | Sensorineural hearing impairment, **HP:0000407** |
| Cerebellar ataxia | Sign; usually follows narcolepsy/deafness and progresses | Cerebellar ataxia, **HP:0001251** |
| Gait ataxia/falls | Functional manifestation; progressive, potentially requiring aids or caregiver support | Gait ataxia, **HP:0002066** |
| Cognitive decline/dementia | Behavioral/cognitive manifestation; generally later and progressive, sometimes frontotemporal-like | Progressive cognitive impairment, **HP:0001268**; Dementia, **HP:0000726** |
| Sensory axonal neuropathy | Sign/electrophysiological abnormality; variable and progressive | Peripheral axonal neuropathy, **HP:0003477**; Sensory neuropathy, **HP:0000763** |
| Optic atrophy | Ophthalmic sign; variable | Optic atrophy, **HP:0000648** |
| Psychiatric/behavioral change | Hallucinations, psychosis, personality change or executive dysfunction; variable | Hallucinations, **HP:0000738**; Psychosis, **HP:0000709** |
| Seizures/myoclonus | Episodic neurological sign; variable, sometimes treatment-refractory | Seizure, **HP:0001250**; Myoclonus, **HP:0001336** |
| Dysautonomia | Sign; variable, especially across DNMT1-complex disorder | Autonomic dysfunction, **HP:0002270** |
| Diabetes mellitus | Laboratory/clinical metabolic phenotype; reported but not universal | Diabetes mellitus, **HP:0000819** |
| Lower-limb lymphedema | Physical manifestation; reported in some families | Lymphedema, **HP:0001004** |
| Brain/cerebellar atrophy | Imaging abnormality; variable and progressive | Cerebral atrophy, **HP:0002059**; Cerebellar atrophy, **HP:0001272** |

The original report stated that narcolepsy and deafness appeared first in all studied pedigrees, followed by ataxia; low or undetectable CSF hypocretin-1 supported hypothalamic hypocretin-system dysfunction. Additional recognized manifestations include optic atrophy, sensorimotor polyneuropathy, psychosis, dementia, and diabetes mellitus. (winkelmann2012mutationsindnmt1 pages 1-2, davis2023mutationsinhuman pages 1-2)

A presymptomatic study examined two clinically unaffected carriers aged 28 and 23. Both had sleep-onset REM periods and increased cerebellar myoinositol on proton MR spectroscopy despite normal neurological examination, audiometry, ophthalmic evaluation, and structural MRI. The authors concluded: **“SOREMPs may precede the clinical picture of ADCA-DN as an early polysomnographic marker.”** This is promising but based on only two carriers and is not a validated screening biomarker. (moghadam2014polysomnographicandneurometabolic pages 1-2)

### Quality-of-life impact

No ADCA-DN-specific EQ-5D, SF-36, PROMIS, or utility study was found. Expected major burdens are inability to remain awake reliably, driving/work restrictions, communication impairment, imbalance and falls, loss of independent mobility, neuropsychiatric symptoms, and eventual need for assistance with daily activities. In a broader DNMT1 case series, one individual progressed to inability to walk and required caregiver assistance. These are clinically important observations but not standardized quality-of-life measurements. (bi2020expandedgeneticinsight pages 1-2)

## 4. Genetic and molecular information

### Causal gene and protein

**DNMT1** encodes the principal maintenance DNA methyltransferase, which preferentially restores symmetrical CpG methylation on hemimethylated DNA after replication and participates in DNA repair, imprint maintenance, genome stability, differentiation, and transcriptional repression. Its RFTS domain regulates recruitment to replication foci and interactions involving UHRF1, ubiquitinated histones, and replication-associated machinery. (bi2020expandedgeneticinsight pages 1-2, wang2021mutationinduceddnmt1cleavage pages 1-2)

### Pathogenic variants

The best-established ADCA-DN variants are germline, heterozygous missense variants **p.Ala570Val, p.Gly605Ala, and p.Val606Phe**. Evidence supports a pathogenic mechanism more complex than simple haploinsufficiency: impaired methyltransferase function coexists with altered folding, localization, stability, aggregation, and possibly toxic cleavage products. No recurrent nonsense variant pattern supports pure loss of function. (winkelmann2012mutationsindnmt1 pages 2-3, davletgildeeva2024theroleof pages 5-7, wang2021mutationinduceddnmt1cleavage pages 12-13)

Broader DNMT1-complex variants include p.C353F, p.T481P, p.P491L, p.Y524D, p.I531N, p.E510K, p.P1546A, p.T497P, and p.Y511H, among others. These should not all be labeled classical ADCA-DN: some were reported in HSAN1E or overlapping phenotypes, and p.P1546A was the first reported outside the targeting-sequence domain. (baets2015defectsofmutant pages 1-1, bi2020expandedgeneticinsight pages 1-2)

No disease-causing chromosomal aneuploidy, translocation, inversion, repeat expansion, mitochondrial variant, or somatic driver has been established. No validated modifier gene or disease-specific methylation “episignature” suitable for routine diagnosis was found.

## 5. Environmental information

ADCA-DN is not infectious, transmissible, occupational, or toxin-induced. No causal pathogen, radiation exposure, pollutant, diet, alcohol pattern, smoking exposure, or exercise pattern is established. General measures—hearing protection, fall prevention, regular activity within safe limits, sleep scheduling, and avoidance of sedating substances—may reduce secondary harm but do not prevent the genetic disease.

## 6. Mechanism and pathophysiology

### Proposed causal chain

1. **Upstream genetic lesion:** a heterozygous missense variant alters the DNMT1 RFTS regulatory domain.
2. **Protein-level dysfunction:** altered RFTS conformation weakens regulatory interactions, may reduce catalytic activity, impairs heterochromatin association, promotes abnormal cytoplasmic or nucleolar localization, and can cause protein aggregation or susceptibility to internal cleavage. (baets2015defectsofmutant pages 1-1, davletgildeeva2024theroleof pages 5-7, wang2021mutationinduceddnmt1cleavage pages 12-13)
3. **Epigenomic disturbance:** maintenance CpG methylation becomes abnormal in a cell-type-specific manner, producing both hypo- and locus-specific dysmethylation and altered transcription.
4. **Proteostasis and cellular injury:** mutant protein may form aggresomes and engage autophagy; cleavage may generate an N-terminal 75–80-kDa product with proposed gain-of-function effects. Neural progenitor maintenance, neuronal survival, and differentiated-neuron gene regulation may consequently fail. (baets2015defectsofmutant pages 1-1, wang2021mutationinduceddnmt1cleavage pages 12-13, wang2021mutationinduceddnmt1cleavage pages 1-2)
5. **Circuit/tissue failure:** dysfunction of hypothalamic hypocretin circuitry produces narcolepsy-cataplexy; auditory-system injury causes sensorineural deafness; cerebellar and broader CNS degeneration causes ataxia and cognitive/behavioral deterioration; peripheral sensory neurons may also be involved.
6. **Downstream clinical progression:** sleep and hearing abnormalities often precede gait ataxia, dementia, neuropathy, and multisystem disability. (winkelmann2012mutationsindnmt1 pages 1-2, moghadam2014polysomnographicandneurometabolic pages 1-2)

### 2023 molecular profiling

Davis and colleagues studied fibroblasts, iPSCs, and induced neurons from patients carrying Ala570Val, Gly605Ala, or Val606Phe. They reported cell-type-specific methylation and expression changes, with negative correlation between methylation and expression in iPSCs and induced neurons. **ZFP57** promoters were hypomethylated and ZFP57 expression increased; nominated phenotype-associated genes included **PDGFB** and **PRDM8** for ataxia/psychosis/dementia and **NR2F1** for deafness/optic atrophy. These are mechanistic candidates, not validated diagnostic or prognostic biomarkers. (davis2023mutationsinhuman pages 1-2)

### Suggested GO and Cell Ontology annotations

- **GO biological processes:** maintenance of DNA methylation (**GO:0010216**); DNA methylation (**GO:0006306**); regulation of gene expression, epigenetic (**GO:0040029**); chromatin organization (**GO:0006325**); neurogenesis (**GO:0022008**); autophagy (**GO:0006914**); protein localization to heterochromatin; neuron death (**GO:0070997**).
- **GO cellular components:** nucleus (**GO:0005634**), chromatin (**GO:0000785**), heterochromatin (**GO:0000792**), replication fork (**GO:0005657**), nucleolus (**GO:0005730**), aggresome (**GO:0016235**).
- **Candidate CL terms:** neuron (**CL:0000540**), neural stem cell (**CL:0000047**), cerebellar Purkinje cell (**CL:0000121**), sensory neuron (**CL:0000101**), oligodendrocyte (**CL:0000128**), microglial cell (**CL:0000129**), regulatory T cell (**CL:0000815**), and hypothalamic hypocretin/orexin neuron where supported by a local ontology extension.

Immune dysfunction remains speculative for classical ADCA-DN. DNMT1 is important in immune-cell biology and one hypothesis links impaired regulatory T-cell differentiation with hypocretin-neuron vulnerability, but direct proof of an autoimmune causal chain in ADCA-DN is lacking. (winkelmann2012mutationsindnmt1 pages 4-5)

## 7. Anatomical structures affected

**Primary organs/system:** central and peripheral nervous systems, with secondary auditory and visual-system involvement.

- **Hypothalamus/hypocretin system:** implicated by narcolepsy and low CSF hypocretin-1. Suggested UBERON: hypothalamus, **UBERON:0001898**.
- **Cerebellum:** ataxia, cerebellar metabolic change, and possible atrophy. Suggested UBERON: cerebellum, **UBERON:0002037**.
- **Cerebral cortex/frontosubcortical networks:** cognitive decline, psychosis, executive dysfunction, brain atrophy, and PET hypometabolism.
- **Auditory apparatus and pathways:** bilateral sensorineural hearing loss; precise lesion localization may vary between cochlea, auditory nerve/pathway, and cortex. Suggested UBERON: inner ear, **UBERON:0001846**; cochlea, **UBERON:0001844**.
- **Optic nerve/retinal ganglion-cell pathway:** optic atrophy in some patients. Suggested UBERON: optic nerve, **UBERON:0000962**.
- **Peripheral sensory nerves and dorsal columns:** sensory axonal neuropathy, posterior-column/fasciculus gracilis abnormalities in broader DNMT1-complex cases.

Global brain atrophy occurred in 12 of 14 MRI-evaluated individuals in a broader DNMT1 cohort. A separate five-case series described asymmetric cerebral atrophy, enhancing T2 lesions, regional PET hypometabolism, and posterior-column spinal atrophy. These findings illustrate the spectrum but are neither universal nor specific for classical ADCA-DN. (baets2015defectsofmutant pages 1-1, bi2020expandedgeneticinsight pages 1-2)

There is no characteristic lateralization; manifestations are generally bilateral/systemic, although asymmetric brain atrophy has been reported in an expanded DNMT1 phenotype.

## 8. Temporal development

Classical onset is chronic and insidious, generally in the fourth or fifth decade, although onset varies and childhood presentations occur in broader DNMT1-complex disorder. Narcolepsy-cataplexy and hearing loss usually emerge first; cerebellar ataxia, neuropathy, cognitive decline, psychiatric disease, and multisystem complications accumulate over years. (winkelmann2012mutationsindnmt1 pages 1-2, bi2020expandedgeneticinsight pages 1-2, moghadam2014polysomnographicandneurometabolic pages 1-2)

A useful nonvalidated staging model is:

1. **Presymptomatic carrier:** possible SOREMPs and elevated cerebellar myoinositol.
2. **Early clinical:** excessive sleepiness/cataplexy and progressive hearing impairment.
3. **Intermediate:** gait/cerebellar ataxia, falls, optic or peripheral sensory involvement.
4. **Advanced:** dementia/behavioral deterioration, severe mobility and communication disability, seizures or dysautonomia.

No spontaneous remission is documented. Cataplexy is episodic, but the underlying disease course is progressive and lifelong. The presymptomatic interval might be an intervention window, but no preventive therapy has been validated.

## 9. Inheritance and population

Inheritance is **autosomal dominant**. A heterozygous affected individual ordinarily has a 50% probability of transmitting the allele in each pregnancy. Penetrance appears strongly age-dependent, but a precise estimate is unavailable. Expressivity is variable, including within families. No repeat expansion is involved, so genetic anticipation is not established. De-novo disease occurs; germline mosaicism has not been quantified. Consanguinity is not etiologically relevant to dominant transmission. (winkelmann2012mutationsindnmt1 pages 1-2, winkelmann2012mutationsindnmt1 pages 2-3)

ADCA-DN is ultra-rare. As of the 2014 presymptomatic study, only the original Swedish family and five additional pedigrees were recognized worldwide. There are no reliable prevalence, incidence, carrier-frequency, sex-ratio, or ethnicity-specific estimates. Cases have been described in European, Brazilian, Chinese, and other populations, arguing against restriction to one ancestry, but this is case-report geography rather than epidemiology. (moghadam2014polysomnographicandneurometabolic pages 1-2)

## 10. Diagnostics

### Clinical evaluation

Suspect ADCA-DN when adult-onset narcolepsy/cataplexy or unexplained daytime sleepiness co-occurs with progressive sensorineural hearing loss, cerebellar ataxia, dementia, optic atrophy, or sensory neuropathy—especially with dominant family history.

Recommended assessment includes:

- Neurological, cerebellar, cognitive, psychiatric, autonomic, and ophthalmic examinations.
- Pure-tone and speech audiometry; auditory electrophysiology where indicated.
- Overnight polysomnography followed by multiple sleep latency testing for suspected narcolepsy; CSF hypocretin-1 can support narcolepsy type 1 when diagnostic uncertainty remains.
- Brain MRI, with attention to cerebellar and cerebral atrophy; spinal MRI if dorsal-column disease is suspected. MRS/PET remain investigational rather than routine.
- Nerve-conduction studies/EMG and somatosensory evoked potentials for neuropathy/posterior-column involvement.
- EEG if seizures, myoclonus, or episodic altered awareness occur.
- Screening guided by phenotype for diabetes, immunoglobulin deficiency, cardiomyopathy, dysautonomia, and lymphedema. (winkelmann2012mutationsindnmt1 pages 1-2, bi2020expandedgeneticinsight pages 1-2, moghadam2014polysomnographicandneurometabolic pages 1-2)

### Genetic testing strategy

1. **Known familial variant:** targeted Sanger or validated next-generation sequencing assay.
2. **Strong classical phenotype:** sequence and deletion/duplication analysis of **DNMT1**, ensuring high-quality coverage of exons 20–21.
3. **Overlapping ataxia/neuropathy/dementia phenotype:** a multigene ataxia, neuropathy, dementia, or sleep-disorder panel that includes DNMT1.
4. **Atypical or unresolved disease:** trio/family-aware WES or preferably WGS, with CNV and structural-variant analysis. A 2024 adult neuromuscular-clinic report emphasized that exome/genome sequencing can resolve DNMT1-related disease missed by narrower approaches. (dratch2024theimportanceof pages 1-2)
5. **Repeat expansions:** test separately when the differential includes common spinocerebellar ataxias; standard WES may not detect them reliably.

CMA, karyotyping, FISH, and mitochondrial testing are not first-line tests for a classic DNMT1 phenotype unless other findings suggest chromosomal or mitochondrial disease. RNA sequencing, methylome profiling, proteomics, and metabolomics are research tools, not validated clinical diagnostics.

### Differential diagnosis

Key alternatives include dominant spinocerebellar ataxias, RFC1-related CANVAS, Friedreich ataxia, POLG/mitochondrial disease, superficial siderosis, multisystem atrophy–cerebellar type, hereditary sensory neuropathies, adult-onset leukodystrophies, autoimmune/paraneoplastic ataxia, and sporadic narcolepsy type 1. The combination of narcolepsy-cataplexy, deafness, ataxia, neuropathy/dementia, and a heterozygous DNMT1 variant is strongly distinguishing.

There are no independently validated formal clinical diagnostic criteria. Molecular confirmation is central.

## 11. Outcome and prognosis

ADCA-DN causes progressive morbidity involving sleep-wake control, hearing, balance, cognition, and independent living. Recovery of the neurodegenerative syndrome is not expected with current treatment. Quantitative survival data are sparse: in a broader DNMT1-complex cohort, mean onset was 37.7 years, average survival 53.6 years, and cognitive decline was reported in 89% by age 45. These values must not be treated as precise ADCA-DN natural-history estimates because the cohort included phenotypic overlap with HSAN1E. (baets2015defectsofmutant pages 1-1)

Potential complications include falls and injury, loss of communication, immobility, aspiration risk in advanced neurological disease, psychiatric crisis, seizures, autonomic complications, and caregiver burden. No validated prognostic biomarker exists. Earlier onset, severe cognitive involvement, seizures, and widespread CNS/PNS disease may plausibly indicate a more severe course, but formal prognostic models are absent.

## 12. Treatment and current applications

### Disease-modifying treatment

No approved disease-modifying drug, gene therapy, cell therapy, RNA therapy, epigenome-editing treatment, or DNMT1-targeted intervention exists for ADCA-DN. No relevant disease-specific interventional trial was identified by the ClinicalTrials.gov search; an unrelated DNMT1-associated oncology study was excluded.

### Symptomatic multidisciplinary care

- **Narcolepsy/cataplexy:** management by a sleep specialist using standard narcolepsy therapies according to local guidelines—wake-promoting medication for excessive sleepiness and anticataplectic therapy where needed—plus scheduled sleep, driving/work risk counseling, and avoidance of sedating drugs. These treatments have not been systematically studied specifically in ADCA-DN.
- **Hearing loss:** hearing aids, assistive communication technology, and cochlear-implant evaluation. In one p.T497P DNMT1-complex case, cochlear implantation produced significant improvement across all tested frequencies from 250 to 6,000 Hz. This is the clearest reported real-world intervention, but it is a single-case result. Suggested NCIT concepts: Hearing Aid Device; Cochlear Implantation. (bi2020expandedgeneticinsight pages 1-2)
- **Ataxia and mobility:** physical therapy, balance/gait training, walking aids, home safety review, fall prevention, and occupational therapy. Suggested NCIT concepts: Physical Therapy; Occupational Therapy; Rehabilitation Therapy.
- **Speech/swallowing:** speech-language therapy, augmentative communication, and swallowing assessment when indicated.
- **Cognitive/psychiatric disease:** neuropsychological monitoring, psychiatric treatment, caregiver education, and advance-care planning.
- **Neuropathy/dysautonomia:** foot and skin surveillance, neuropathic-pain treatment, orthostatic and autonomic management.
- **Seizures:** standard antiseizure treatment individualized to seizure type; one broader DNMT1 case improved after perampanel, but this is not disease-specific efficacy evidence. (bi2020expandedgeneticinsight pages 1-2)

Pharmacogenomic guidance specific to DNMT1 variants is unavailable. Broad DNMT inhibitors used in oncology are not rational routine therapy: systemic interference with maintenance methylation could be harmful, and the disease mechanism includes both deficient function and potentially toxic mutant-protein effects.

## 13. Prevention

There is no vaccine, prophylactic drug, lifestyle intervention, or population-screening program that prevents ADCA-DN.

- **Primary prevention:** reproductive genetic counseling; options may include preimplantation genetic testing for a known familial variant, prenatal diagnosis, donor gametes, or natural conception with or without testing.
- **Secondary prevention/early detection:** cascade testing of consenting adult relatives after counseling, followed by baseline sleep, hearing, neurological, cognitive, and ophthalmic assessment. Predictive testing of minors requires careful ethical review because classical disease is adult-onset and no preventive therapy exists.
- **Tertiary prevention:** hearing rehabilitation, fall prevention, safe-driving counseling, seizure precautions, mobility support, and surveillance for swallowing, autonomic, metabolic, psychiatric, and caregiver complications.

Population newborn or carrier screening is not justified by current prevalence and actionability data.

## 14. Other species and natural disease

No naturally occurring veterinary counterpart of ADCA-DN was identified, and no breed-associated syndrome, zoonotic potential, or cross-species transmission applies. DNMT1 orthologues are evolutionarily conserved across mammals and other vertebrates, supporting comparative functional research, but conserved gene function is not evidence of naturally occurring homologous disease. Suggested taxonomy terms for experimental species include *Homo sapiens* NCBI Taxon 9606 and *Mus musculus* NCBI Taxon 10090.

## 15. Model organisms and experimental systems

### Human cellular models

The most disease-relevant models currently retrieved are patient fibroblasts, iPSCs, and induced neurons carrying Ala570Val, Gly605Ala, or Val606Phe. These reproduce cell-type-specific methylome and transcriptome disturbances and permit study of developmental stage and neural-cell context. Limitations include incomplete brain maturation, absence of intact cerebellar/hypothalamic circuits, and inability to reproduce decades-long progression. (davis2023mutationsinhuman pages 1-2)

### Mouse and cellular knock-in models

Wang and colleagues generated CRISPR knock-in mice modeling HSAN1E-equivalent RFTS variants: mouse Tyr500Cys corresponding to human Y495C and Pro496Tyr corresponding to human D490E/P491Y. Heterozygotes had reduced DNMT1 and impaired learning/memory; homozygotes died around embryonic day 10.5. The study implicated mutation-induced internal cleavage near amino acid 501 and a combination of reduced maintenance methylation with gain-of-function toxicity from truncated protein. (wang2021mutationinduceddnmt1cleavage pages 12-13, wang2021mutationinduceddnmt1cleavage pages 1-2)

These are **not exact ADCA-DN variant models**. The authors stated that the full spectrum, “including hearing, remain[s] to be determined,” and cognitive defects were milder than in affected humans. Thus they support an RFTS-disease mechanism but do not establish complete recapitulation of narcolepsy, deafness, and cerebellar ataxia. (wang2021mutationinduceddnmt1cleavage pages 12-13)

Relevant resources for future model discovery include MGI, IMPC, KOMP, IMSR/MMRRC, ZFIN, FlyBase, and patient-derived iPSC repositories. A major unmet need is a heterozygous knock-in model carrying an exact ADCA-DN variant and assessed longitudinally for sleep architecture, hypocretin circuitry, auditory function, cerebellar degeneration, cognition, and methylome changes.

## Recent developments and evidence gaps

The 2023 patient-derived neural-cell study provides the strongest modern disease-specific mechanistic advance, moving the field from a generic “global hypomethylation” model toward cell-type- and locus-specific dysregulation. The 2024 systematic review found 25 qualifying hearing-loss methylation records from 661 screened articles—12 human methylation studies, five animal studies, and eight DNMT1 mutation studies—and concluded that pathogenic exon-21 DNMT1 variants are independently confirmed, whereas methylation evidence in complex hearing loss remains much less secure. A separate 2024 clinical article highlighted practical implementation of exome/genome sequencing in adults with unresolved neuromuscular phenotypes. (davis2023mutationsinhuman pages 1-2, patil2024asystematicreview pages 1-2, dratch2024theimportanceof pages 1-2)

Critical gaps are the absence of a registry-scale natural-history cohort, variant-specific penetrance estimates, validated biomarkers, standardized outcomes, exact-variant animal models, controlled treatment studies, and disease-specific clinical trials. Accordingly, frequency, prognosis, and treatment claims should be represented in a knowledge base with explicit evidence levels and with ADCA-DN distinguished from the broader DNMT1-complex spectrum.

## Key references and publication details

1. Winkelmann J, et al. “Mutations in DNMT1 cause autosomal dominant cerebellar ataxia, deafness and narcolepsy.” *Human Molecular Genetics*. Published May 2012. DOI: https://doi.org/10.1093/hmg/dds035. PMID **22328086**. (OpenTargets Search: autosomal dominant cerebellar ataxia deafness and narcolepsy-DNMT1, winkelmann2012mutationsindnmt1 pages 1-2)
2. Pedroso JL, et al. “A novel de novo exon 21 DNMT1 mutation causes cerebellar ataxia, deafness, and narcolepsy in a Brazilian patient.” *Sleep*. Published August 2013. DOI: https://doi.org/10.5665/sleep.2898. PMID **23904686**. (OpenTargets Search: autosomal dominant cerebellar ataxia deafness and narcolepsy-DNMT1)
3. Moghadam KK, et al. “Polysomnographic and neurometabolic features may mark preclinical autosomal dominant cerebellar ataxia, deafness, and narcolepsy…” *Sleep Medicine*. Published May 2014. DOI: https://doi.org/10.1016/j.sleep.2013.09.028. (moghadam2014polysomnographicandneurometabolic pages 1-2)
4. Baets J, et al. “Defects of mutant DNMT1 are linked to a spectrum of neurological disorders.” *Brain*. Published April 2015. DOI: https://doi.org/10.1093/brain/awv010. (baets2015defectsofmutant pages 1-1)
5. Bi H, et al. “Expanded genetic insight and clinical experience of DNMT1-complex disorder.” *Neurology Genetics*. Published August 2020. DOI: https://doi.org/10.1212/NXG.0000000000000456. PMID **31984424**. (OpenTargets Search: autosomal dominant cerebellar ataxia deafness and narcolepsy-DNMT1, bi2020expandedgeneticinsight pages 1-2)
6. Wang W, et al. “Mutation-induced DNMT1 cleavage drives neurodegenerative disease.” *Science Advances*. Published September 1, 2021. DOI: https://doi.org/10.1126/sciadv.abe8511. (wang2021mutationinduceddnmt1cleavage pages 12-13, wang2021mutationinduceddnmt1cleavage pages 1-2)
7. Davis KN, et al. “Mutations in human DNA methyltransferase DNMT1 induce specific genome-wide epigenomic and transcriptomic changes in neurodevelopment.” *Human Molecular Genetics*. Published August 2023. DOI: https://doi.org/10.1093/hmg/ddad123. (davis2023mutationsinhuman pages 1-2)
8. Dratch L, et al. “The Importance of Offering Exome or Genome Sequencing in Adult Neuromuscular Clinics.” *Biology*. Published February 2, 2024. DOI: https://doi.org/10.3390/biology13020093. (dratch2024theimportanceof pages 1-2)
9. Patil V, et al. “A systematic review on the contribution of DNA methylation to hearing loss.” *Clinical Epigenetics*. Published July 2024. DOI: https://doi.org/10.1186/s13148-024-01697-9. (patil2024asystematicreview pages 1-2)
10. Davletgildeeva AT, Kuznetsov NA. “The Role of DNMT Methyltransferases and TET Dioxygenases in the Maintenance of the DNA Methylation Level.” *Biomolecules*. Published September 2024. DOI: https://doi.org/10.3390/biom14091117. (davletgildeeva2024theroleof pages 5-7)

References

1. (winkelmann2012mutationsindnmt1 pages 1-2): Juliane Winkelmann, Ling Lin, Barbara Schormair, Birgitte R. Kornum, Juliette Faraco, Giuseppe Plazzi, Atle Melberg, Ferdinando Cornelio, Alexander E. Urban, Fabio Pizza, Francesca Poli, Fabian Grubert, Thomas Wieland, Elisabeth Graf, Joachim Hallmayer, Tim M. Strom, and Emmanuel Mignot. Mutations in dnmt1 cause autosomal dominant cerebellar ataxia, deafness and narcolepsy. Human molecular genetics, 21 10:2205-10, May 2012. URL: https://doi.org/10.1093/hmg/dds035, doi:10.1093/hmg/dds035. This article has 306 citations and is from a domain leading peer-reviewed journal.

2. (baets2015defectsofmutant pages 13-14): Jonathan Baets, Xiaohui Duan, Yanhong Wu, Gordon Smith, William W. Seeley, Inès Mademan, Nicole M. McGrath, Noah C. Beadell, Julie Khoury, Maria-Victoria Botuyan, Georges Mer, Gregory A. Worrell, Kaori Hojo, Jessica DeLeon, Matilde Laura, Yo-Tsen Liu, Jan Senderek, Joachim Weis, Peter Van den Bergh, Shana L. Merrill, Mary M. Reilly, Henry Houlden, Murray Grossman, Steven S. Scherer, Peter De Jonghe, Peter J. Dyck, and Christopher J. Klein. Defects of mutant dnmt1 are linked to a spectrum of neurological disorders. Brain : a journal of neurology, 138 Pt 4:845-61, Apr 2015. URL: https://doi.org/10.1093/brain/awv010, doi:10.1093/brain/awv010. This article has 152 citations.

3. (bi2020expandedgeneticinsight pages 1-2): Hongyan Bi, Kaori Hojo, Masashi Watanabe, Christina Yee, Kiran Maski, Sadaf Saba, Jonathan Graff-Radford, Mary M. Machulda, Erik K. St Louis, Ilona Spitsyna Humes, Eoin P. Flanagan, Stefan Nicolau, David T. Jones, Marc C. Patterson, Suresh Kotagal, Yael Raz, Zhiyv Niu, Jun Li, and Christopher J. Klein. Expanded genetic insight and clinical experience of dnmt1-complex disorder. Neurology Genetics, Aug 2020. URL: https://doi.org/10.1212/nxg.0000000000000456, doi:10.1212/nxg.0000000000000456. This article has 20 citations.

4. (davis2023mutationsinhuman pages 1-2): Kasey N Davis, Ping-Ping Qu, Shining Ma, Ling Lin, Melanie Plastini, Niklas Dahl, Giuseppe Plazzi, Fabio Pizza, Ruth O’Hara, Wing Hung Wong, Joachim Hallmayer, Emmanuel Mignot, Xianglong Zhang, and Alexander E Urban. Mutations in human dna methyltransferase dnmt1 induce specific genome-wide epigenomic and transcriptomic changes in neurodevelopment. Human molecular genetics, 32:3105-3120, Aug 2023. URL: https://doi.org/10.1093/hmg/ddad123, doi:10.1093/hmg/ddad123. This article has 7 citations and is from a domain leading peer-reviewed journal.

5. (patil2024asystematicreview pages 1-2): Vibha Patil, Patricia Perez-Carpena, and Jose A. Lopez-Escamez. A systematic review on the contribution of dna methylation to hearing loss. Clinical Epigenetics, Jul 2024. URL: https://doi.org/10.1186/s13148-024-01697-9, doi:10.1186/s13148-024-01697-9. This article has 9 citations and is from a peer-reviewed journal.

6. (OpenTargets Search: autosomal dominant cerebellar ataxia deafness and narcolepsy-DNMT1): Open Targets Query (autosomal dominant cerebellar ataxia deafness and narcolepsy-DNMT1, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

7. (baets2015defectsofmutant pages 1-1): Jonathan Baets, Xiaohui Duan, Yanhong Wu, Gordon Smith, William W. Seeley, Inès Mademan, Nicole M. McGrath, Noah C. Beadell, Julie Khoury, Maria-Victoria Botuyan, Georges Mer, Gregory A. Worrell, Kaori Hojo, Jessica DeLeon, Matilde Laura, Yo-Tsen Liu, Jan Senderek, Joachim Weis, Peter Van den Bergh, Shana L. Merrill, Mary M. Reilly, Henry Houlden, Murray Grossman, Steven S. Scherer, Peter De Jonghe, Peter J. Dyck, and Christopher J. Klein. Defects of mutant dnmt1 are linked to a spectrum of neurological disorders. Brain : a journal of neurology, 138 Pt 4:845-61, Apr 2015. URL: https://doi.org/10.1093/brain/awv010, doi:10.1093/brain/awv010. This article has 152 citations.

8. (baets2015defectsofmutant pages 14-15): Jonathan Baets, Xiaohui Duan, Yanhong Wu, Gordon Smith, William W. Seeley, Inès Mademan, Nicole M. McGrath, Noah C. Beadell, Julie Khoury, Maria-Victoria Botuyan, Georges Mer, Gregory A. Worrell, Kaori Hojo, Jessica DeLeon, Matilde Laura, Yo-Tsen Liu, Jan Senderek, Joachim Weis, Peter Van den Bergh, Shana L. Merrill, Mary M. Reilly, Henry Houlden, Murray Grossman, Steven S. Scherer, Peter De Jonghe, Peter J. Dyck, and Christopher J. Klein. Defects of mutant dnmt1 are linked to a spectrum of neurological disorders. Brain : a journal of neurology, 138 Pt 4:845-61, Apr 2015. URL: https://doi.org/10.1093/brain/awv010, doi:10.1093/brain/awv010. This article has 152 citations.

9. (winkelmann2012mutationsindnmt1 pages 2-3): Juliane Winkelmann, Ling Lin, Barbara Schormair, Birgitte R. Kornum, Juliette Faraco, Giuseppe Plazzi, Atle Melberg, Ferdinando Cornelio, Alexander E. Urban, Fabio Pizza, Francesca Poli, Fabian Grubert, Thomas Wieland, Elisabeth Graf, Joachim Hallmayer, Tim M. Strom, and Emmanuel Mignot. Mutations in dnmt1 cause autosomal dominant cerebellar ataxia, deafness and narcolepsy. Human molecular genetics, 21 10:2205-10, May 2012. URL: https://doi.org/10.1093/hmg/dds035, doi:10.1093/hmg/dds035. This article has 306 citations and is from a domain leading peer-reviewed journal.

10. (moghadam2014polysomnographicandneurometabolic pages 1-2): Keivan Kaveh Moghadam, Fabio Pizza, Caterina Tonon, Raffaele Lodi, Valerio Carelli, Francesca Poli, Christian Franceschini, Piero Barboni, Marco Seri, Simona Ferrari, Chiara La Morgia, Claudia Testa, Ferdinando Cornelio, Rocco Liguori, Juliane Winkelmann, Ling Lin, Emmanuel Mignot, and Giuseppe Plazzi. Polysomnographic and neurometabolic features may mark preclinical autosomal dominant cerebellar ataxia, deafness, and narcolepsy due to a mutation in the dna (cytosine-5-)-methyltransferase gene, dnmt1. Sleep Medicine, 15(5):582-585, May 2014. URL: https://doi.org/10.1016/j.sleep.2013.09.028, doi:10.1016/j.sleep.2013.09.028. This article has 10 citations and is from a peer-reviewed journal.

11. (winkelmann2012mutationsindnmt1 pages 4-5): Juliane Winkelmann, Ling Lin, Barbara Schormair, Birgitte R. Kornum, Juliette Faraco, Giuseppe Plazzi, Atle Melberg, Ferdinando Cornelio, Alexander E. Urban, Fabio Pizza, Francesca Poli, Fabian Grubert, Thomas Wieland, Elisabeth Graf, Joachim Hallmayer, Tim M. Strom, and Emmanuel Mignot. Mutations in dnmt1 cause autosomal dominant cerebellar ataxia, deafness and narcolepsy. Human molecular genetics, 21 10:2205-10, May 2012. URL: https://doi.org/10.1093/hmg/dds035, doi:10.1093/hmg/dds035. This article has 306 citations and is from a domain leading peer-reviewed journal.

12. (davletgildeeva2024theroleof pages 5-7): Anastasiia T. Davletgildeeva and Nikita A. Kuznetsov. The role of dnmt methyltransferases and tet dioxygenases in the maintenance of the dna methylation level. Biomolecules, 14:1117, Sep 2024. URL: https://doi.org/10.3390/biom14091117, doi:10.3390/biom14091117. This article has 76 citations.

13. (wang2021mutationinduceddnmt1cleavage pages 12-13): Wencai Wang, Xingsen Zhao, Yanjiao Shao, Xiaoya Duan, Yaling Wang, Jialun Li, Jiwen Li, Dali Li, Xuekun Li, and Jiemin Wong. Mutation-induced dnmt1 cleavage drives neurodegenerative disease. Science Advances, Sep 2021. URL: https://doi.org/10.1126/sciadv.abe8511, doi:10.1126/sciadv.abe8511. This article has 18 citations and is from a highest quality peer-reviewed journal.

14. (wang2021mutationinduceddnmt1cleavage pages 1-2): Wencai Wang, Xingsen Zhao, Yanjiao Shao, Xiaoya Duan, Yaling Wang, Jialun Li, Jiwen Li, Dali Li, Xuekun Li, and Jiemin Wong. Mutation-induced dnmt1 cleavage drives neurodegenerative disease. Science Advances, Sep 2021. URL: https://doi.org/10.1126/sciadv.abe8511, doi:10.1126/sciadv.abe8511. This article has 18 citations and is from a highest quality peer-reviewed journal.

15. (dratch2024theimportanceof pages 1-2): Laynie Dratch, Tanya M Bardakjian, Kelsey Johnson, Nareen Babaian, Pedro Gonzalez-Alegre, Lauren B. Elman, Colin C. Quinn, Michael Guo, Steven S Scherer, and Defne A. Amado. The importance of offering exome or genome sequencing in adult neuromuscular clinics. Biology, Feb 2024. URL: https://doi.org/10.3390/biology13020093, doi:10.3390/biology13020093. This article has 2 citations.

## Artifacts

- [Edison artifact artifact-00](ADCA-DN-deep-research-falcon_artifacts/artifact-00.md)