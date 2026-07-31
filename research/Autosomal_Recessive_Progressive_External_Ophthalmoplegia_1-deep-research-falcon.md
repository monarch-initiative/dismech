---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-31T16:09:29.630077'
end_time: '2026-07-31T16:24:10.353388'
duration_seconds: 880.72
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Autosomal Recessive Progressive External Ophthalmoplegia 1
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 36
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Autosomal_Recessive_Progressive_External_Ophthalmoplegia_1-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autosomal Recessive Progressive External Ophthalmoplegia 1
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Recessive Progressive External Ophthalmoplegia 1** covering all of the
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
- **Disease Name:** Autosomal Recessive Progressive External Ophthalmoplegia 1
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Recessive Progressive External Ophthalmoplegia 1** covering all of the
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


# Autosomal Recessive Progressive External Ophthalmoplegia 1: Disease-Characteristics Report

## Executive summary and evidence scope

**Autosomal recessive progressive external ophthalmoplegia 1 (arPEO1)** is a nuclear-encoded mitochondrial DNA-maintenance disorder caused by **biallelic germline variants in POLG**, which encodes the catalytic subunit of mitochondrial DNA polymerase γ. The defining manifestation is slowly progressive, usually bilateral ptosis and external ophthalmoparesis; limb, bulbar, peripheral-nerve, cerebellar, auditory, epileptic, or other systemic features produce a “PEO-plus” phenotype. POLG dysfunction causes secondary mitochondrial-DNA (mtDNA) deletions and sometimes depletion, followed by respiratory-chain failure in energy-demanding tissues. The entity is one phenotype on a continuous POLG-related disease spectrum rather than a sharply isolated syndrome. (wong2008molecularandclinical pages 1-2, kurtz2021wholeexomesequencingidentifies pages 7-7, ali2024mitochondrialchronicprogressive pages 6-8)

Evidence specific to molecularly confirmed arPEO1 is sparse. Accordingly, this report distinguishes **arPEO-specific evidence**, **broader POLG-spectrum evidence**, and **genetically heterogeneous PEO evidence**. The most recent disease-focused source retrieved was the January 2024 CPEO review (DOI [10.3390/brainsci14020135](https://doi.org/10.3390/brainsci14020135)); it is authoritative for current recognition and management but not arPEO1-specific. No arPEO1-specific randomized trial, population natural-history registry, or 2023–2024 mechanistic cohort was identified. (ali2024mitochondrialchronicprogressive pages 6-8, ali2024mitochondrialchronicprogressive pages 3-5, rahman2019polgrelateddisordersand pages 11-13)

The following table provides a knowledge-base-ready overview.

| Field | Summary | Suggested ontology/identifier(s) | Evidence |
|---|---|---|---|
| Scope / definition | Autosomal recessive progressive external ophthalmoplegia 1 is best resolved here as a POLG-related adult/late-onset mitochondrial disease phenotype within the broader POLG disorder spectrum, characterized by progressive weakness of extraocular muscles causing ptosis and ophthalmoparesis; it is distinct from dominant POLG PEO and from PEO caused by TWNK, RNASEH1, TK2, RRM2B, or primary mtDNA defects. | OMIM phenotype name: Autosomal recessive progressive external ophthalmoplegia 1; disease label also reported as arPEO / POLG-related arPEO. | (wong2008molecularandclinical pages 1-2, ali2024mitochondrialchronicprogressive pages 6-8, somai2025mitochondrialdnareplication pages 6-8, rodriguezlopez2020clinicalpathologicaland pages 2-3) |
| OMIM identifier | OMIM 258450 was explicitly associated with autosomal recessive progressive external ophthalmoplegia in the gathered evidence. | OMIM: 258450 | (wong2008molecularandclinical pages 1-2) |
| Likely MONDO mapping caveat | A MONDO term was not verified in the gathered evidence. If a MONDO mapping is added downstream, it should be manually checked because PEO entities are genetically heterogeneous and MONDO may group phenotype-level and gene-level concepts differently. | MONDO: not verified from gathered sources | (wong2008molecularandclinical pages 1-2, ali2024mitochondrialchronicprogressive pages 6-8) |
| Causal gene / protein | Causal gene: POLG, encoding the catalytic subunit of mitochondrial DNA polymerase gamma (DNA polymerase γA / POLγA), the only mitochondrial DNA polymerase responsible for mtDNA replication and repair. | Gene: POLG; Protein: DNA polymerase subunit gamma-1 / POLγA; HGNC/NCBI Gene IDs not verified from gathered sources | (wong2008molecularandclinical pages 1-2, rahman2019polgrelateddisordersand pages 10-11, chan2009dnapolymerasegamma pages 4-5) |
| Inheritance | Autosomal recessive; usually biallelic pathogenic germline variants, often compound heterozygous, though homozygous A467T cases occur. Yeast modeling of the A467T-analog supports recessive behavior. | Inheritance: autosomal recessive; germline | (wong2008molecularandclinical pages 1-2, rajakulendran2016aclinicalneuropathological pages 2-3, stuart2006mitochondrialandnuclear pages 8-9) |
| Hallmark phenotypes | Core phenotype: progressive external ophthalmoplegia/ophthalmoparesis with bilateral ptosis; early subtle slowed/incomplete saccades may occur. Additional POLG-associated “PEO-plus” features can include limb weakness, bulbar involvement, exercise intolerance, peripheral neuropathy, ataxia, hearing loss, tremor, seizures, and other multisystem manifestations, but these are not specific to arPEO1 alone. | HPO suggestions: Ptosis (HP:0000508, verified code not checked here), External ophthalmoplegia / Ophthalmoparesis (code not verified), Exercise intolerance (code not verified), Peripheral neuropathy (code not verified), Ataxia (code not verified), Sensorineural hearing impairment (code not verified), Tremor (code not verified), Seizure (code not verified) | (kurtz2021wholeexomesequencingidentifies pages 7-7, ali2024mitochondrialchronicprogressive pages 6-8, ali2024mitochondrialchronicprogressive pages 3-5, rodriguezlopez2020clinicalpathologicaland pages 2-3) |
| Common pathogenic variant themes | Recurrent POLG variants in broader POLG disease include A467T, W748S, G848S, and T251I-P587L; A467T is the most common disease-associated allele in Europeans and functionally recessive. W748S commonly occurs in cis with E1143G, which can modify severity. Variant-level pathogenic classifications were not systematically verified from ClinVar in gathered evidence. | Variant examples: A467T; W748S; G848S; T251I-P587L; E1143G modifier/polymorphic context | (rajakulendran2016aclinicalneuropathological pages 2-3, somai2025mitochondrialdnareplication pages 6-8, rahman2019polgrelateddisordersand pages 10-11, rajakulendran2016aclinicalneuropathological pages 11-13) |
| Mechanism / pathophysiology | Upstream defect: impaired POLγ-mediated mtDNA replication/maintenance. A467T reduces polymerase activity to ~4% of wild type and disrupts interaction with the POLG2 accessory subunit; W748S reduces catalytic activity/processivity and impairs DNA binding. Downstream consequences include multiple mtDNA deletions and sometimes mtDNA depletion, leading to respiratory-chain dysfunction in high-energy tissues such as extraocular muscle, skeletal muscle, and nervous system. | GO suggestions: mitochondrial DNA replication (GO code not verified), DNA repair (GO code not verified), oxidative phosphorylation (GO code not verified), mitochondrial genome maintenance (GO code not verified) | (kurtz2021wholeexomesequencingidentifies pages 7-7, somai2025mitochondrialdnareplication pages 6-8, rahman2019polgrelateddisordersand pages 10-11, chan2009dnapolymerasegamma pages 4-5) |
| Tissues / cells / compartments affected | Primary tissues: extraocular muscles and skeletal muscle; broader involvement can include peripheral and central nervous system, liver, and heart in the wider POLG spectrum. Cell populations likely implicated include skeletal muscle fibers and neurons, but exact CL terms were not verified. Key compartment: mitochondrion, especially mtDNA nucleoid/mitochondrial matrix replication machinery. | UBERON suggestions: extraocular muscle (code not verified), skeletal muscle tissue (code not verified), peripheral nerve (code not verified), brain (code not verified); CL suggestions: skeletal muscle cell / myofiber, neuron (codes not verified); GO cellular component suggestions: mitochondrion, mitochondrial matrix, mitochondrial nucleoid (codes not verified) | (wong2008molecularandclinical pages 1-2, ali2024mitochondrialchronicprogressive pages 6-8, rodriguezlopez2020clinicalpathologicaland pages 2-3) |
| Diagnostic signature | Diagnostic clues include progressive bilateral ptosis and ophthalmoparesis, often adult onset, with muscle biopsy frequently showing mitochondrial myopathy changes such as ragged-red/COX-negative fibers and molecular evidence of multiple mtDNA deletions; CK may be normal or elevated in broader PEO cohorts. Genetic confirmation relies on sequencing of POLG (now often via exome/genome/panel testing); muscle biopsy remains highly informative in broader mitochondrial PEO when etiology is uncertain. | Diagnostic modalities: POLG sequencing; mtDNA deletion analysis in muscle; muscle biopsy; WES/WGS/panel testing. Biomarker codes not verified. | (kurtz2021wholeexomesequencingidentifies pages 7-7, ali2024mitochondrialchronicprogressive pages 3-5, kierdaszuk2020progressiveexternalophthalmoplegia pages 2-4, rodriguezlopez2020clinicalpathologicaland pages 2-3) |
| Treatment / prevention | No disease-modifying therapy was identified. Current care is supportive: ptosis aids/crutches, ptosis surgery (levator procedures or frontalis suspension), prism or strabismus surgery if diplopia/strabismus occur, rehabilitation/exercise as tolerated, and multidisciplinary surveillance for extraocular and systemic complications. In the broader POLG spectrum, valproate is contraindicated because of risk of liver failure. Prevention is mainly reproductive/genetic: genetic counseling, carrier/family testing, and consideration of prenatal or preimplantation testing where appropriate. | NCIT suggestions: genetic counseling, ptosis surgery, strabismus surgery, physical therapy / rehabilitation (codes not verified); Prevention: cascade testing, prenatal diagnosis, PGT (codes not verified) | (ali2024mitochondrialchronicprogressive pages 3-5, rahman2019polgrelateddisordersand pages 11-13) |
| Epidemiology / frequency | Disease-specific prevalence for arPEO1 was not found in gathered evidence. For a major recurrent allele, A467T carrier frequency was reported around 0.2–0.3% in mixed European populations, up to 1.3–1.4% in Belgian/British populations, with predicted homozygote prevalence ~1 in 500,000 to 1,000,000; these figures describe a variant, not arPEO1 prevalence. | Epidemiology for disease: not established from gathered sources | (rajakulendran2016aclinicalneuropathological pages 2-3, rahman2019polgrelateddisordersand pages 10-11) |
| Model systems / translational evidence | Yeast MIP1 models reproduce recessive behavior and mtDNA instability of human POLG variants; the A467T-analog behaves as a mild recessive defect in diploids. Broader POLG mutator mice model mtDNA deletion-driven mitochondrial dysfunction and premature aging, but no model perfectly recapitulates human POLG disease. Patient fibroblast and biochemical assays support defective holoenzyme assembly and replication failure. | Model classes: yeast, mouse, patient fibroblasts, biochemical enzyme assays | (stuart2006mitochondrialandnuclear pages 1-2, stuart2006mitochondrialandnuclear pages 8-9, chan2009dnapolymerasegamma pages 4-5, rahman2019polgrelateddisordersand pages 8-10) |
| Key evidence limitations | Much evidence is for the broader POLG spectrum or heterogeneous mitochondrial PEO cohorts rather than arPEO1 alone. Verified MONDO/HPO/GO/CL/UBERON/HGNC codes were not directly retrieved in the gathered sources and should not be auto-filled without ontology lookup. No arPEO1-specific interventional trial, single-cell/spatial omics profile, validated protective factor, or robust natural-history epidemiology study was identified in gathered evidence. | Limitation flags: ontology IDs unverified; arPEO1-specific trials absent in gathered evidence | (ali2024mitochondrialchronicprogressive pages 6-8, rodriguezlopez2020clinicalpathologicaland pages 2-3, rahman2019polgrelateddisordersand pages 11-13, rahman2019polgrelateddisordersand pages 8-10) |


*Table: This table condenses the key knowledge-base fields for autosomal recessive progressive external ophthalmoplegia 1 as supported by the gathered POLG-related evidence. It highlights what is well supported, what is broader-spectrum rather than arPEO1-specific, and which ontology identifiers still require external verification.*

## 1. Disease information

### Definition and classification

arPEO1 is a **Mendelian, autosomal-recessive mitochondrial disease** in which impaired POLG-dependent mtDNA replication and maintenance predominantly injure extraocular and skeletal muscle. It is distinct from:

* autosomal-dominant PEO caused by dominant POLG variants;
* PEO caused by other nuclear genes, including **TWNK, POLG2, RNASEH1, SLC25A4, TK2,** and **RRM2B**;
* primary mtDNA point variants or single large-scale mtDNA deletions; and
* syndromic PEO such as Kearns–Sayre syndrome. (ali2024mitochondrialchronicprogressive pages 6-8, kierdaszuk2020progressiveexternalophthalmoplegia pages 2-4, rodriguezlopez2020clinicalpathologicaland pages 2-3)

### Identifiers and synonyms

* **OMIM:** **258450**, explicitly identified as POLG-associated arPEO in the retrieved primary literature. (wong2008molecularandclinical pages 1-2)
* **MONDO:** not verified in the retrieved corpus; manual ontology reconciliation is recommended because databases may represent PEO as a phenotype-level, gene-specific, or umbrella mitochondrial-disease concept.
* **Common names:** autosomal recessive progressive external ophthalmoplegia 1; PEOA1; arPEO; POLG-related autosomal recessive PEO; POLG-related PEO; chronic progressive external ophthalmoplegia when chronicity is emphasized.
* **ICD-10/ICD-11 and MeSH:** no uniquely specific arPEO1 code was verified; coding commonly falls under mitochondrial metabolism/myopathy or ophthalmoplegia categories. A generic code should not be represented as disease-specific without local terminology verification.

This report is synthesized from **aggregated disease-level literature, published cohorts, individual case reports, biochemical experiments, and model systems**, not from an individual EHR.

## 2. Etiology, risk, protective factors, and gene–environment interaction

### Primary cause

The cause is **two pathogenic or likely pathogenic POLG alleles in trans**. POLG encodes POLγA, the catalytic polymerase/proofreading component of the mitochondrial replisome. Recessive variants reduce polymerase activity, processivity, DNA binding, interaction with the POLG2 accessory subunit, or protein abundance, destabilizing mtDNA. In one approximately 350-patient referral series, two mutant alleles were found in 31 unrelated recessive cases, of whom **4/31 (13%)** had arPEO; this is a referral-series proportion, not population prevalence. (wong2008molecularandclinical pages 1-2)

### Genetic risk factors

Recurrent disease alleles across the broader POLG spectrum include **p.Ala467Thr (A467T), p.Trp748Ser (W748S), p.Gly848Ser (G848S),** and the **p.Thr251Ile–p.Pro587Leu** cis pair. A467T represented approximately **36% of disease-associated POLG alleles** in a major review; these four recurrent alleles together constituted about **50% of identified variants**, and roughly **75% of patients** carried at least one. These values concern all POLG-related disease, not arPEO1 alone. (rahman2019polgrelateddisordersand pages 10-11)

A467T carrier frequency was reported as approximately **0.2–0.3%** in mixed European populations and **1.3–1.4%** in Belgian/British populations, with a theoretical homozygote frequency of approximately **1:500,000–1:1,000,000**. This is allele epidemiology, not clinical arPEO1 prevalence, because homozygous A467T can cause widely differing POLG phenotypes. (rajakulendran2016aclinicalneuropathological pages 2-3, rajakulendran2016aclinicalneuropathological pages 11-13)

### Modifiers and protective factors

* **E1143G**, usually found in cis with W748S, partially compensates for biochemical impairment and may modify severity; it should not be treated as a stand-alone protective allele. (somai2025mitochondrialdnareplication pages 6-8, rahman2019polgrelateddisordersand pages 10-11)
* Homozygous A467T has produced Alpers–Huttenlocher syndrome, MELAS-like disease, MEMSA, and SANDO, implicating mtDNA haplotype, other nuclear variants, and environmental stress as modifiers. No validated clinical modifier panel exists. (rajakulendran2016aclinicalneuropathological pages 2-3, rajakulendran2016aclinicalneuropathological pages 11-13)
* No reproducible **genetic or environmental protective factor** specific to arPEO1 was identified.

### Environmental and lifestyle factors

No toxin, infection, diet, occupation, smoking pattern, alcohol exposure, or radiation exposure causes this Mendelian disorder. Physiological stress may unmask mitochondrial insufficiency, but arPEO1-specific gene–environment effect sizes are unavailable. The most consequential established drug interaction in the broader POLG spectrum is **valproate-associated hepatic failure**; valproate is therefore contraindicated in patients with pathogenic POLG variants. (rahman2019polgrelateddisordersand pages 11-13)

## 3. Phenotypes

### Core and associated manifestations

| Manifestation | Type and characteristics | Suggested HPO annotation |
|---|---|---|
| Progressive external ophthalmoplegia/ophthalmoparesis | Defining sign; bilateral, insidious, slowly progressive limitation of extraocular movement. Slowed or incomplete saccades can precede obvious restriction. | Progressive external ophthalmoplegia; Ophthalmoparesis |
| Ptosis | Common defining sign, usually bilateral and progressive; levator excursion may fall below 8–10 mm versus normal ≥12 mm in generic CPEO. | **HP:0000508 Ptosis**; Bilateral ptosis |
| Diplopia/strabismus | Variable and often less prominent than motility loss because restriction can be relatively symmetric. In a heterogeneous 89-person PEO cohort, more than one-third reported diplopia. | Diplopia; Strabismus |
| Exercise intolerance and myopathy | Variable PEO-plus manifestations; proximal limb, neck, facial, or generalized weakness can impair mobility and endurance. | Exercise intolerance; Proximal muscle weakness; Myopathy |
| Bulbar dysfunction | Dysarthria or dysphagia in syndromic/POLG PEO-plus disease. | Dysarthria; Dysphagia |
| Peripheral neuropathy/sensory ataxia | Particularly suggests a nuclear mtDNA-maintenance defect and can produce SANDO-spectrum disease. | Peripheral neuropathy; Sensory ataxia |
| Cerebellar ataxia/tremor | Variable PEO-plus neurological manifestations. | Cerebellar ataxia; Intention tremor |
| Sensorineural hearing loss | Recognized within the wider POLG spectrum, not established as uniformly frequent in arPEO1. | Sensorineural hearing impairment |
| Seizures/encephalopathy | Possible in broader POLG disease; their presence suggests substantial syndromic overlap rather than isolated arPEO. | Seizure; Encephalopathy |
| Laboratory/pathology abnormalities | CK may be normal or elevated; muscle may contain ragged-red and cytochrome-c-oxidase-negative fibers, multiple mtDNA deletions, and occasionally mtDNA depletion. | Elevated serum CK; Ragged-red muscle fibers; COX-negative muscle fibers; mtDNA depletion |

(kurtz2021wholeexomesequencingidentifies pages 7-7, ali2024mitochondrialchronicprogressive pages 6-8, ali2024mitochondrialchronicprogressive pages 3-5, rodriguezlopez2020clinicalpathologicaland pages 2-3)

### Onset, progression, frequency, and quality of life

The classic arPEO phenotype is generally **adult-onset**, chronic, and slowly progressive, although POLG disease spans infancy through late adulthood. Reliable phenotype percentages for arPEO1 alone are unavailable. A heterogeneous mitochondrial PEO cohort of 89 patients comprised **42% pure PEO, 10% Kearns–Sayre syndrome, 33% myopathic PEO-plus, 12% bulbar PEO-plus, and 3% other PEO-plus**; these figures should not be imported as arPEO1 frequencies. In that cohort, POLG was more often associated with PEO-plus than pure PEO. (rodriguezlopez2020clinicalpathologicaland pages 2-3)

Quality-of-life effects include impaired superior and peripheral visual fields from ptosis, abnormal head posture, difficulty reading/driving, fatigue, reduced walking endurance, falls from neuropathy/ataxia, dysphagia, and psychosocial burden. No arPEO1-specific EQ-5D, SF-36, PROMIS, or utility study was identified.

## 4. Genetic and molecular information

### Gene and protein

* **Gene:** POLG, chromosome 15q region; HGNC identifier should be verified directly before database import.
* **Protein:** catalytic subunit POLγA; it contains exonuclease, spacer, and polymerase domains and works with a POLG2-encoded accessory dimer.
* **Origin:** pathogenic variants are constitutional/germline, not somatic drivers.

### Variant classes and functional consequences

Reported pathogenic classes include missense, nonsense, frameshift, canonical/noncanonical splice, and small insertion/deletion variants. A 2021 adult PEO case carried compound-heterozygous **c.67_88del, p.Gly23Serfs*236** and **c.3104+3A>T**; the latter causes exon-19 skipping. Muscle showed mitochondrial myopathy, multiple mtDNA deletions, and depletion. (kurtz2021wholeexomesequencingidentifies pages 7-7)

A467T lies in the spacer domain. Recombinant enzyme retained only about **4% of wild-type polymerase activity**, had impaired DNA binding/processivity, and failed to interact normally with the POLG2 accessory subunit. W748S reduces polymerase activity, processivity, and DNA binding while retaining accessory-subunit interaction. These are primarily **loss-of-function/hypomorphic** mechanisms in recessive disease, not classic gain-of-function or dominant-negative effects. (rahman2019polgrelateddisordersand pages 10-11, rajakulendran2016aclinicalneuropathological pages 11-13, stuart2006mitochondrialandnuclear pages 8-9)

Population allele frequencies must be assessed variant by variant in gnomAD; the retrieved corpus did not provide validated gnomAD frequencies for every pathogenic allele. ClinVar classifications should likewise be imported per exact HGVS allele rather than assigning one classification to all variants.

### Other genomic and epigenetic findings

No recurrent chromosomal aneuploidy, translocation, inversion, repeat expansion, or disease-defining copy-number abnormality is established. No validated arPEO1-specific methylation episignature, histone signature, or chromatin defect was identified. A reported mtDNA-deletion case involving reduced POLG/SSBP1 expression and methylation is not sufficient to define an arPEO1 epigenetic mechanism.

## 5. Environmental information

Environmental exposures are not primary etiologic agents. There is no evidence that infection is causal or transmissible; **zoonotic transmission is not applicable**. Practical exposure management follows general mitochondrial-disease principles: avoid fasting, dehydration, excessive heat, and unaccustomed exhaustive exertion when these provoke decompensation, while maintaining safe activity. These are precautionary practices rather than proven arPEO1-preventive interventions. Valproate avoidance has the strongest POLG-specific evidence. (rahman2019polgrelateddisordersand pages 11-13)

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream genetic trigger:** biallelic POLG dysfunction.
2. **Primary biochemical defect:** reduced polymerase catalysis/processivity, DNA binding, proofreading in selected alleles, holoenzyme assembly, or protein abundance.
3. **Genome-maintenance failure:** replication fork stalling, mtDNA depletion and/or clonally expanded multiple mtDNA deletions in post-mitotic tissues.
4. **Respiratory defect:** loss or imbalance of mtDNA-encoded oxidative-phosphorylation subunits impairs electron transport and ATP production.
5. **Cellular injury:** energy failure, abnormal redox state, compensatory mitochondrial proliferation, and eventual myofiber/neuronal dysfunction or loss.
6. **Clinical expression:** extraocular-muscle weakness causes ptosis and ophthalmoplegia; broader skeletal-muscle and neural injury causes PEO-plus manifestations. (wong2008molecularandclinical pages 1-2, kurtz2021wholeexomesequencingidentifies pages 7-7, somai2025mitochondrialdnareplication pages 6-8, chan2009dnapolymerasegamma pages 4-5)

Extraocular muscles are especially vulnerable because of continuous activity, specialized motor units, and high oxidative demand. Adult-onset PEO has been associated with multiple deletions affecting more than **60% of muscle mtDNA genomes** in reviewed data, although this is not a universal diagnostic threshold. (somai2025mitochondrialdnareplication pages 6-8)

### Ontology suggestions

* **GO biological process:** mitochondrial DNA replication; mitochondrial genome maintenance; DNA repair; oxidative phosphorylation; ATP metabolic process; mitochondrial organization.
* **GO molecular function:** DNA-directed DNA polymerase activity; 3′–5′ exonuclease activity; DNA binding.
* **GO cellular component:** mitochondrion; mitochondrial matrix; mitochondrial nucleoid; mitochondrial respiratory-chain complex.
* **Cell Ontology:** skeletal muscle fiber/myocyte; extraocular skeletal muscle cell where supported; peripheral sensory neuron; cerebellar neuron.

Exact ontology accessions other than HP:0000508 were not verified in the retrieved literature and should undergo ontology-service validation.

### Molecular profiling and advanced technologies

Routine diagnosis measures mtDNA quantity/rearrangement and respiratory histochemistry rather than a validated transcriptomic, proteomic, metabolomic, or lipidomic signature. No arPEO1-specific single-cell atlas, spatial-transcriptomic map, integrated multi-omics classifier, or CRISPR-screen-derived clinical biomarker was identified. The absence of retrieved evidence should be encoded as **“not established,” not “normal.”**

## 7. Anatomical structures affected

* **Primary organ/tissue:** bilateral extraocular muscles and levator palpebrae superioris; skeletal muscle.
* **Secondary systems in PEO-plus disease:** peripheral and central nervous systems, auditory system, swallowing musculature, liver, heart, endocrine and renal systems—variable and not obligatory in isolated arPEO1. (ali2024mitochondrialchronicprogressive pages 6-8)
* **Subcellular site:** mitochondrial matrix/nucleoid and downstream inner-membrane respiratory-chain system.
* **Lateralization:** typically bilateral, often relatively symmetric; asymmetric ptosis can occur clinically.

Suggested anatomy annotations include extraocular muscle, levator palpebrae superioris, skeletal muscle tissue, peripheral nerve, cerebellum, brain, liver, and heart. UBERON/FMA accessions should be verified before import.

## 8. Temporal development

Onset is usually **insidious and adult**, beginning with subtle saccadic slowing, ptosis, or gaze limitation. Early disease may remain ocular; intermediate disease can add diplopia, exercise intolerance, and limb weakness; advanced PEO-plus disease can include bulbar dysfunction, neuropathy, ataxia, hearing loss, or other organ involvement. The course is chronic and usually slowly progressive rather than episodic or relapsing. Spontaneous remission is not expected, although ptosis and diplopia can improve symptomatically after intervention. (kurtz2021wholeexomesequencingidentifies pages 7-7, ali2024mitochondrialchronicprogressive pages 3-5)

There is no accepted staging system or validated arPEO1 progression-rate biomarker. Early molecular diagnosis is the main actionable window because it enables surveillance, avoids harmful treatment, and informs relatives before irreversible disability accumulates.

## 9. Inheritance and population

Inheritance is **autosomal recessive**. Parents of an affected individual are usually heterozygous carriers; each full sibling has a theoretical 25% probability of being affected, 50% of being an unaffected carrier, and 25% of inheriting neither familial allele, assuming both variants are confirmed in trans and standard Mendelian segregation applies.

Penetrance is likely high for genuinely pathogenic biallelic combinations but is **age- and allele-dependent**; expressivity is markedly variable. Anticipation is not established. Germline mosaicism has not emerged as a characteristic mechanism. Consanguinity increases the probability of homozygous rare alleles but is not required. Founder enrichment exists for selected alleles such as A467T in European-derived populations. No consistent sex bias is established. (rajakulendran2016aclinicalneuropathological pages 2-3, rahman2019polgrelateddisordersand pages 10-11)

Neither incidence nor prevalence of clinically defined arPEO1 is robustly known. Carrier-frequency estimates for A467T must not be converted directly into disease prevalence because penetrance, allelic heterogeneity, and phenotype heterogeneity intervene.

## 10. Diagnostics

### Recommended workflow

1. **Clinical recognition:** bilateral progressive ptosis plus external ophthalmoparesis, slowed saccades, exercise intolerance, neuropathy, ataxia, or family history.
2. **Exclude common mimics:** ocular myasthenia gravis, thyroid eye disease, oculopharyngeal muscular dystrophy, myotonic dystrophy, congenital cranial dysinnervation disorders, inflammatory/infiltrative orbital disease, and other mitochondrial PEO causes.
3. **First-line molecular testing:** a mitochondrial-disease/PEO nuclear panel that includes POLG plus complete mtDNA sequencing and deletion analysis, or exome/genome sequencing with reliable mtDNA and copy-number/rearrangement analysis. Definitive arPEO1 diagnosis requires two disease-causing POLG alleles in trans. WES identified the novel frameshift in the 2021 adult case. (kurtz2021wholeexomesequencingidentifies pages 7-7)
4. **Tissue-aware mtDNA testing:** blood can miss low-level or tissue-restricted deletions; skeletal muscle is often more informative for multiple mtDNA deletions and depletion.
5. **Muscle biopsy when genetics is unresolved or tissue mtDNA analysis is required:** modified Gomori trichrome, COX/SDH histochemistry, respiratory-chain studies, mtDNA copy number, and deletion testing.

In a heterogeneous 89-person PEO cohort, muscle biopsy showed mitochondrial dysfunction in **95%**, and a genetic diagnosis was reached in **96%**; **63%** had a single large mtDNA deletion, **26%** multiple deletions, and **7%** an mtDNA point variant. Among multiple-deletion cases, causal genes included TWNK (n=8), POLG (n=7), TK2 (n=6), and RRM2B (n=2). These data demonstrate diagnostic yield but are not arPEO1 prevalence estimates. (rodriguezlopez2020clinicalpathologicaland pages 2-3)

CK has limited sensitivity: in the same broader cohort, **31/68** had CK below 200 U/L; elevated results averaged 780 U/L and ranged from 203–5,195 U/L. Normal CK therefore does not exclude disease. FGF21 and GDF15 may support a mitochondrial diagnosis, but neither is specific for POLG arPEO1. (rodriguezlopez2020clinicalpathologicaland pages 2-3)

EMG may show myopathy or neuropathy; nerve-conduction testing is useful when sensory ataxia is present. ECG/echocardiography, audiology, swallowing assessment, pulmonary testing, EEG, and brain MRI should be driven by phenotype. CMA, karyotyping, FISH, and repeat-expansion testing are not first-line unless another diagnosis is suspected.

### Screening

Population and newborn screening are not established. Appropriate strategies are **cascade testing** for known familial variants, partner testing where relevant, and surveillance of genetically affected relatives. Carrier screening is targeted rather than universal.

## 11. Outcome and prognosis

Isolated adult arPEO is generally chronic and disabling but not necessarily life-shortening. Prognosis becomes less favorable with seizures, encephalopathy, severe neuropathy/ataxia, dysphagia, respiratory weakness, cardiomyopathy, or hepatic involvement. Published survival rates, median life expectancy, disease-specific mortality rates, and validated prognostic models for arPEO1 were not identified.

The major durable morbidity is ocular and neuromuscular disability. Recovery of lost mitochondrial myofibers is not expected; supportive interventions improve function rather than cure the molecular defect. Variant alone is an imperfect prognostic marker: even homozygous A467T produced four markedly different clinical phenotypes in a four-patient study. (rajakulendran2016aclinicalneuropathological pages 2-3, rajakulendran2016aclinicalneuropathological pages 11-13)

## 12. Treatment and current implementation

### Disease-modifying therapy

No approved disease-modifying pharmacotherapy, gene therapy, cell therapy, RNA therapy, or gene-editing treatment exists for arPEO1. An authoritative review stated that evidence-based POLG therapies were lacking and no randomized controlled trials had been performed. Vitamin/antioxidant “mitochondrial cocktails” are widely used but lack a proven arPEO1 response rate. (rahman2019polgrelateddisordersand pages 11-13)

### Symptomatic and supportive care

* **Ptosis:** eyelid crutches may be tried but are often poorly tolerated. Mild levator dysfunction may be treated by levator resection/advancement; severe dysfunction often requires frontalis/brow suspension. Corneal exposure risk must be balanced against visual-field benefit. Suggested NCIt concepts: Ptosis Repair; Frontalis Suspension Procedure; Supportive Care. (ali2024mitochondrialchronicprogressive pages 3-5, rahman2019polgrelateddisordersand pages 11-13)
* **Diplopia/strabismus:** prisms when feasible; selected patients may undergo strabismus surgery, with counseling that progression can alter alignment. Suggested NCIt: Prism Therapy; Strabismus Surgery. (ali2024mitochondrialchronicprogressive pages 3-5)
* **Rehabilitation:** individualized aerobic and resistance activity below symptom-provoking thresholds, physical/occupational therapy, falls prevention, and mobility aids. Suggested NCIt: Physical Therapy; Occupational Therapy; Rehabilitation Therapy.
* **Bulbar/respiratory care:** swallowing evaluation, diet modification, speech therapy, aspiration prevention, nutritional support, and noninvasive ventilation where indicated.
* **Hearing/cataract care:** hearing aids or cochlear assessment and cataract surgery when clinically appropriate. Cataract removal and brow suspension are specifically cited supportive interventions in POLG disease. (rahman2019polgrelateddisordersand pages 11-13)
* **Seizures:** specialist management; lamotrigine, clobazam, levetiracetam, or topiramate have been used, but comparative arPEO1 data are absent. **Valproate is absolutely contraindicated** because of potentially fatal hepatic failure. (rahman2019polgrelateddisordersand pages 11-13)
* **Monitoring:** periodic ophthalmology, neurology, mobility/falls, hearing, swallowing, nutrition, respiratory, cardiac, hepatic, endocrine, and mental-health assessment, tailored to phenotype.

No arPEO1-specific interventional trial was identified in the retrieved ClinicalTrials.gov search. Trials of elamipretide and other interventions enrolled broader primary mitochondrial myopathy or nuclear-DNA mitochondrial-disease populations; they should not be presented as demonstrated arPEO1 treatments.

## 13. Prevention

Primary prevention by lifestyle change is impossible once a pathogenic biallelic genotype is inherited. Evidence-based prevention is reproductive and familial:

* genetic counseling and confirmation that variants are in trans;
* parental and cascade testing;
* prenatal diagnosis or preimplantation genetic testing for a known familial genotype;
* donor gametes or other reproductive options according to patient values and jurisdiction.

Mitochondrial replacement therapy is not a logical targeted prevention for POLG arPEO1 because the causal variants are in **nuclear DNA**, not maternally inherited mtDNA. Secondary prevention comprises early molecular diagnosis and surveillance. Tertiary prevention includes valproate avoidance, falls/aspiration prevention, corneal protection, safe rehabilitation, and management of cardiac, respiratory, hepatic, auditory, and nutritional complications. Vaccination has no disease-specific preventive role beyond routine infection prevention.

## 14. Other species and natural disease

POLG is evolutionarily conserved, with functional orthologues in mammals, Drosophila, and yeast (**MIP1** in *Saccharomyces cerevisiae*, NCBI Taxonomy 4932). No well-established naturally occurring companion-animal or wildlife syndrome equivalent to human POLG arPEO1, no breed-specific VBO association, and no zoonotic potential were identified. Comparative relevance therefore comes primarily from engineered models rather than natural veterinary disease.

## 15. Model organisms and experimental systems

### Yeast

Human PEO-associated substitutions introduced into yeast **MIP1** reproduce mtDNA loss, respiratory-deficient “petite” colonies, altered mutability, and variant-specific dominance/recessivity. The yeast I416T analogue of human A467T was mild in haploids and nearly wild-type in diploids, consistent with recessive inheritance. Yeast models predict pathogenicity with reported accuracy of approximately **70–100%**, but are limited by nonconserved residues, simplified protein interactions, and absence of extraocular muscle and nervous-system phenotypes. (stuart2006mitochondrialandnuclear pages 1-2, stuart2006mitochondrialandnuclear pages 8-9, lodi2015dnapolymeraseγ pages 7-8, lodi2015dnapolymeraseγ pages 8-9)

A concise abstract-level statement from the yeast literature is that MIP1 models help in “**validating the pathological mutations found in human POLG**” and in defining their molecular defects. Chemical rescue with lipoic acid or MitoQ reduced petite frequency for selected yeast variants, but this is preclinical and not evidence of efficacy in arPEO1 patients. (lodi2015dnapolymeraseγ pages 9-10)

### Biochemical and patient-cell systems

Recombinant POLγ assays measure polymerase activity, processivity, DNA binding, proofreading, and POLG2 interaction. Patient fibroblasts have demonstrated nonsense-mediated decay, abnormal splicing, and reduced holoenzyme abundance; examples included approximately **75% reduction** with R232H/G848S and **45% reduction** with A467T/T914P combinations. These systems directly test variant function but do not reproduce lifelong tissue-selective deletion accumulation. (chan2009dnapolymerasegamma pages 4-5, lodi2015dnapolymeraseγ pages 9-10)

### Mouse models

Exonuclease-deficient POLG “mutator” mice develop premature aging at 6–9 months, including hearing loss, kyphosis, cardiomegaly, reduced body weight and bone density, and approximately **90-fold more mtDNA deletions**. Heterozygotes can remain asymptomatic despite markedly elevated mutation burden, demonstrating that mutagenesis alone does not determine phenotype. These models illuminate deletion-driven mitochondrial pathology but do **not** faithfully reproduce human arPEO1. (somai2025mitochondrialdnareplication pages 6-8, rahman2019polgrelateddisordersand pages 8-10)

### Key research gaps and current expert interpretation

The most important unresolved issue is why identical biallelic POLG genotypes produce isolated adult PEO in some people and catastrophic multisystem disease in others. Current evidence supports contributions from residual enzyme activity, allelic phase, mtDNA background, nuclear modifiers, tissue-specific deletion thresholds, aging, and environmental stress, but no validated predictive model exists. (rajakulendran2016aclinicalneuropathological pages 2-3, rahman2019polgrelateddisordersand pages 10-11, rajakulendran2016aclinicalneuropathological pages 11-13)

Recent clinical practice has moved toward broad sequencing and tissue-aware mtDNA analysis rather than sequential single-gene testing, while the therapeutic field remains supportive. Priorities are longitudinal genotype-stratified natural-history cohorts, quantitative ocular-motility endpoints, patient-derived myotube/iPSC models, single-cell and spatial profiling of affected muscle, and safe nuclear-gene replacement or editing strategies. The central current conclusion is therefore: **molecular diagnosis is clinically actionable for counseling, surveillance, and drug avoidance, but not yet for a proven genotype-directed cure.**

## Selected dated sources and URLs

1. Wong et al. **“Molecular and clinical genetics of mitochondrial diseases due to POLG mutations.”** *Human Mutation*. September 2008. DOI: [10.1002/humu.20824](https://doi.org/10.1002/humu.20824). Primary human referral series. (wong2008molecularandclinical pages 1-2)
2. Rahman & Copeland. **“POLG-related disorders and their neurological manifestations.”** *Nature Reviews Neurology*. Online November 2018/2019 volume. DOI: [10.1038/s41582-018-0101-0](https://doi.org/10.1038/s41582-018-0101-0). Authoritative review. (rahman2019polgrelateddisordersand pages 10-11, rahman2019polgrelateddisordersand pages 11-13)
3. Rodríguez-López et al. **“Clinical, pathological and genetic spectrum in 89 cases of mitochondrial progressive external ophthalmoplegia.”** *Journal of Medical Genetics*. March 2020; 57:643–646. DOI: [10.1136/jmedgenet-2019-106649](https://doi.org/10.1136/jmedgenet-2019-106649). Primary clinical cohort. (rodriguezlopez2020clinicalpathologicaland pages 2-3)
4. Kurtz et al. **“Whole-Exome Sequencing Identifies a Novel POLG Frameshift Variant…”** *Case Reports in Genetics*. November 2021. DOI: [10.1155/2021/9969071](https://doi.org/10.1155/2021/9969071). Primary human case and molecular study. (kurtz2021wholeexomesequencingidentifies pages 7-7)
5. Ali, Esmaeil & Behbehani. **“Mitochondrial Chronic Progressive External Ophthalmoplegia.”** *Brain Sciences*. January 2024;14:135. DOI: [10.3390/brainsci14020135](https://doi.org/10.3390/brainsci14020135). Recent clinical review. Its abstract states: “**Genetic sequencing is the gold standard for diagnosing mitochondrial encephalomyopathies**” and “**No definitive treatment option is available for mitochondrial diseases**.” (ali2024mitochondrialchronicprogressive pages 6-8, ali2024mitochondrialchronicprogressive pages 3-5)

PMIDs were not consistently exposed in the retrieved full-text metadata; DOI URLs are therefore supplied rather than risking incorrect PMID assignment.

References

1. (wong2008molecularandclinical pages 1-2): Lee-Jun C. Wong, Robert K. Naviaux, Nicola Brunetti-Pierri, Qing Zhang, Eric S. Schmitt, Cavatina Truong, Margherita Milone, Bruce H. Cohen, Beverly Wical, Jaya Ganesh, Alice A. Basinger, Barbara K. Burton, Kathryn Swoboda, Donald L. Gilbert, Adeline Vanderver, Russell P. Saneto, Bruno Maranda, Georgianne Arnold, Jose E. Abdenur, Paula J. Waters, and William C. Copeland. Molecular and clinical genetics of mitochondrial diseases due to polg mutations. Human Mutation, 29:E150-E172, Sep 2008. URL: https://doi.org/10.1002/humu.20824, doi:10.1002/humu.20824. This article has 366 citations and is from a domain leading peer-reviewed journal.

2. (kurtz2021wholeexomesequencingidentifies pages 7-7): Justin Kurtz, Joseph Americo Fernandes, Mahesh Mansukhani, William C. Copeland, and Ali B. Naini. Whole-exome sequencing identifies a novel polg frameshift variant in an adult patient presenting with progressive external ophthalmoplegia and mitochondrial dna depletion. Case Reports in Genetics, 2021:1-7, Nov 2021. URL: https://doi.org/10.1155/2021/9969071, doi:10.1155/2021/9969071. This article has 4 citations.

3. (ali2024mitochondrialchronicprogressive pages 6-8): Ali Ali, Ali Esmaeil, and Raed Behbehani. Mitochondrial chronic progressive external ophthalmoplegia. Brain Sciences, 14:135, Jan 2024. URL: https://doi.org/10.3390/brainsci14020135, doi:10.3390/brainsci14020135. This article has 25 citations.

4. (ali2024mitochondrialchronicprogressive pages 3-5): Ali Ali, Ali Esmaeil, and Raed Behbehani. Mitochondrial chronic progressive external ophthalmoplegia. Brain Sciences, 14:135, Jan 2024. URL: https://doi.org/10.3390/brainsci14020135, doi:10.3390/brainsci14020135. This article has 25 citations.

5. (rahman2019polgrelateddisordersand pages 11-13): Shamima Rahman and William C. Copeland. Polg-related disorders and their neurological manifestations. Nov 2019. URL: https://doi.org/10.1038/s41582-018-0101-0, doi:10.1038/s41582-018-0101-0. This article has 508 citations and is from a highest quality peer-reviewed journal.

6. (somai2025mitochondrialdnareplication pages 6-8): Shruti Somai, Chioma H. Aloh, Dillon E. King, and William C. Copeland. Mitochondrial dna replication and disease: a historical perspective on molecular insights and therapeutic advances. International Journal of Molecular Sciences, 26:10275, Oct 2025. URL: https://doi.org/10.3390/ijms262110275, doi:10.3390/ijms262110275. This article has 1 citations.

7. (rodriguezlopez2020clinicalpathologicaland pages 2-3): Claudia Rodríguez-López, Luis M. García-Cárdaba, Alberto Blázquez, Pablo Serrano-Lorenzo, Gerardo Gutiérrez-Gutiérrez, Beatriz San Millán-Tejado, Nuria Muelas, Aurelio Hernández-Laín, Juan J. Vílchez, Eduardo Gutiérrez-Rivas, Joaquín Arenas, Miguel A. Martín, and Cristina Domínguez-González. Clinical, pathological and genetic spectrum in 89 cases of mitochondrial progressive external ophthalmoplegia. Journal of Medical Genetics, 57(9):643-646, Mar 2020. URL: https://doi.org/10.1136/jmedgenet-2019-106649, doi:10.1136/jmedgenet-2019-106649. This article has 43 citations and is from a domain leading peer-reviewed journal.

8. (rahman2019polgrelateddisordersand pages 10-11): Shamima Rahman and William C. Copeland. Polg-related disorders and their neurological manifestations. Nov 2019. URL: https://doi.org/10.1038/s41582-018-0101-0, doi:10.1038/s41582-018-0101-0. This article has 508 citations and is from a highest quality peer-reviewed journal.

9. (chan2009dnapolymerasegamma pages 4-5): Sherine S.L. Chan and William C. Copeland. Dna polymerase gamma and mitochondrial disease: understanding the consequence of polg mutations. Biochimica et biophysica acta, 1787 5:312-9, May 2009. URL: https://doi.org/10.1016/j.bbabio.2008.10.007, doi:10.1016/j.bbabio.2008.10.007. This article has 249 citations.

10. (rajakulendran2016aclinicalneuropathological pages 2-3): Sanjeev Rajakulendran, Robert D. S. Pitceathly, Jan-Willem Taanman, Harry Costello, Mary G. Sweeney, Cathy E. Woodward, Zane Jaunmuktane, Janice L. Holton, Thomas S. Jacques, Brian N. Harding, Carl Fratter, Michael G. Hanna, and Shamima Rahman. A clinical, neuropathological and genetic study of homozygous a467t polg-related mitochondrial disease. PLoS ONE, 11:e0145500, Jan 2016. URL: https://doi.org/10.1371/journal.pone.0145500, doi:10.1371/journal.pone.0145500. This article has 67 citations and is from a peer-reviewed journal.

11. (stuart2006mitochondrialandnuclear pages 8-9): Gregory R. Stuart, Janine H. Santos, Micheline K. Strand, Bennett Van Houten, and William C. Copeland. Mitochondrial and nuclear dna defects in saccharomyces cerevisiae with mutations in dna polymerase γ associated with progressive external ophthalmoplegia. Human Molecular Genetics, 15:363-374, Jan 2006. URL: https://doi.org/10.1093/hmg/ddi454, doi:10.1093/hmg/ddi454. This article has 74 citations and is from a domain leading peer-reviewed journal.

12. (rajakulendran2016aclinicalneuropathological pages 11-13): Sanjeev Rajakulendran, Robert D. S. Pitceathly, Jan-Willem Taanman, Harry Costello, Mary G. Sweeney, Cathy E. Woodward, Zane Jaunmuktane, Janice L. Holton, Thomas S. Jacques, Brian N. Harding, Carl Fratter, Michael G. Hanna, and Shamima Rahman. A clinical, neuropathological and genetic study of homozygous a467t polg-related mitochondrial disease. PLoS ONE, 11:e0145500, Jan 2016. URL: https://doi.org/10.1371/journal.pone.0145500, doi:10.1371/journal.pone.0145500. This article has 67 citations and is from a peer-reviewed journal.

13. (kierdaszuk2020progressiveexternalophthalmoplegia pages 2-4): Biruta Kierdaszuk, Magdalena Kaliszewska, Joanna Rusecka, Joanna Kosińska, Ewa Bartnik, Katarzyna Tońska, Anna M. Kamińska, and Anna Kostera-Pruszczyk. Progressive external ophthalmoplegia in polish patients—from clinical evaluation to genetic confirmation. Genes, 12:54, Dec 2020. URL: https://doi.org/10.3390/genes12010054, doi:10.3390/genes12010054. This article has 6 citations.

14. (stuart2006mitochondrialandnuclear pages 1-2): Gregory R. Stuart, Janine H. Santos, Micheline K. Strand, Bennett Van Houten, and William C. Copeland. Mitochondrial and nuclear dna defects in saccharomyces cerevisiae with mutations in dna polymerase γ associated with progressive external ophthalmoplegia. Human Molecular Genetics, 15:363-374, Jan 2006. URL: https://doi.org/10.1093/hmg/ddi454, doi:10.1093/hmg/ddi454. This article has 74 citations and is from a domain leading peer-reviewed journal.

15. (rahman2019polgrelateddisordersand pages 8-10): Shamima Rahman and William C. Copeland. Polg-related disorders and their neurological manifestations. Nov 2019. URL: https://doi.org/10.1038/s41582-018-0101-0, doi:10.1038/s41582-018-0101-0. This article has 508 citations and is from a highest quality peer-reviewed journal.

16. (lodi2015dnapolymeraseγ pages 7-8): Tiziana Lodi, Cristina Dallabona, Cecilia Nolli, Paola Goffrini, Claudia Donnini, and Enrico Baruffini. Dna polymerase γ and disease: what we have learned from yeast. Frontiers in Genetics, Mar 2015. URL: https://doi.org/10.3389/fgene.2015.00106, doi:10.3389/fgene.2015.00106. This article has 41 citations and is from a peer-reviewed journal.

17. (lodi2015dnapolymeraseγ pages 8-9): Tiziana Lodi, Cristina Dallabona, Cecilia Nolli, Paola Goffrini, Claudia Donnini, and Enrico Baruffini. Dna polymerase γ and disease: what we have learned from yeast. Frontiers in Genetics, Mar 2015. URL: https://doi.org/10.3389/fgene.2015.00106, doi:10.3389/fgene.2015.00106. This article has 41 citations and is from a peer-reviewed journal.

18. (lodi2015dnapolymeraseγ pages 9-10): Tiziana Lodi, Cristina Dallabona, Cecilia Nolli, Paola Goffrini, Claudia Donnini, and Enrico Baruffini. Dna polymerase γ and disease: what we have learned from yeast. Frontiers in Genetics, Mar 2015. URL: https://doi.org/10.3389/fgene.2015.00106, doi:10.3389/fgene.2015.00106. This article has 41 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Autosomal_Recessive_Progressive_External_Ophthalmoplegia_1-deep-research-falcon_artifacts/artifact-00.md)