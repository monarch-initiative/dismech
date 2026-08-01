---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-31T23:37:39.390668'
end_time: '2026-07-31T23:46:36.348976'
duration_seconds: 536.96
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Autosomal Dominant Progressive External Ophthalmoplegia
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 20
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Autosomal_Dominant_Progressive_External_Ophthalmoplegia-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autosomal Dominant Progressive External Ophthalmoplegia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Dominant Progressive External Ophthalmoplegia** covering all of the
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
- **Disease Name:** Autosomal Dominant Progressive External Ophthalmoplegia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Dominant Progressive External Ophthalmoplegia** covering all of the
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


# Autosomal Dominant Progressive External Ophthalmoplegia: Disease-Characteristics Report

## Executive summary and scope

Autosomal dominant progressive external ophthalmoplegia (adPEO; often written adCPEO) is a genetically heterogeneous, usually adult-onset mitochondrial myopathy caused by heterozygous defects in nuclear genes required for mitochondrial-DNA (mtDNA) replication, nucleotide supply, membrane transport, or mitochondrial dynamics. Its defining clinical pattern is slowly progressive, usually symmetric bilateral ptosis and limitation of extraocular movements. Its defining molecular pattern is the accumulation of multiple secondary mtDNA deletions in post-mitotic tissue, particularly skeletal muscle. The principal established classic adPEO genes are **POLG, TWNK, SLC25A4, POLG2, DNA2, and RRM2B**; **OPA1** causes an overlapping dominant optic-atrophy-plus/CPEO syndrome. Because “CPEO” is a phenotype rather than one molecular disease, sporadic single-large-scale-mtDNA-deletion disease, recessive PEO, Kearns–Sayre syndrome (KSS), and other mitochondrial syndromes must not be conflated with adPEO. (viscomi2017mtdnamaintenancedefectssyndromes pages 2-4, ali2024mitochondrialchronicprogressive pages 3-5)

The most consequential 2024 therapeutic development was an exploratory genotype-specific analysis of MMPOWER-3: participants with nuclear replisome defects and CPEO improved by **37.3 ± 9.5 m** on the six-minute walk test (6MWT), versus **−8.0 ± 10.7 m** with placebo at week 24 (**p=0.0024**). This was a post-hoc subgroup result after the heterogeneous parent trial failed its primary endpoints; it is therefore hypothesis-generating, not proof of efficacy or an approved adPEO treatment. (karaa2024genotypespecificeffectsof pages 2-5, karaa2024genotypespecificeffectsof pages 1-2)

| Domain/Gene | Primary function or defect | Inheritance and mtDNA consequence | Characteristic clinical features | Key identifiers/evidence |
|---|---|---|---|---|
| **POLG** | Catalytic subunit of mitochondrial DNA polymerase gamma; replisome defect impairing mtDNA replication/repair | **AD** adPEO/adCPEO; typically associated with **multiple mtDNA deletions** in muscle | Ptosis and progressive ophthalmoparesis/ophthalmoplegia, generalized muscle weakness; variable ataxia, hearing loss, cataracts, hypogonadism, peripheral neuropathy, parkinsonism, psychiatric features; usual onset **20–40 y** and progressive with age (viscomi2017mtdnamaintenancedefectssyndromes pages 2-4, ali2024mitochondrialchronicprogressive pages 6-8) | **OMIM 157640**; listed as AD multiple-deletions adCPEO gene (viscomi2017mtdnamaintenancedefectssyndromes pages 2-4) |
| **TWNK (C10orf2 / Twinkle)** | Mitochondrial DNA helicase of the replisome; defective mtDNA unwinding/maintenance | **AD** adPEO; usually causes **multiple mtDNA deletions** | Adult-onset isolated or syndromic CPEO/adPEO with ptosis/ophthalmoplegia; may include muscle weakness, dysarthria, dysphagia, and occasional cardiac involvement (viscomi2017mtdnamaintenancedefectssyndromes pages 2-4, ali2024mitochondrialchronicprogressive pages 6-8) | **OMIM 609286**; listed as AD multiple-deletions adCPEO gene (viscomi2017mtdnamaintenancedefectssyndromes pages 2-4) |
| **SLC25A4 (ANT1)** | Mitochondrial adenine nucleotide translocator; membrane/nucleotide transport defect affecting mtDNA maintenance | **AD** and AR forms reported; AD disease associated with **multiple mtDNA deletions** and classic adPEO/CPEO phenotype (viscomi2017mtdnamaintenancedefectssyndromes pages 2-4, ali2024mitochondrialchronicprogressive pages 3-5) | Ptosis/ophthalmoplegia with mitochondrial myopathy; broader reports include cardiomyopathy in other inheritance contexts and neuropsychiatric associations in some families/models (viscomi2017mtdnamaintenancedefectssyndromes pages 2-4) | **Associated with OMIM 157640** in adPEO framework; gene table lists **SLC25A4 AD adCPEO** with multiple deletions (viscomi2017mtdnamaintenancedefectssyndromes pages 2-4) |
| **POLG2** | Accessory subunit of polymerase gamma; replisome processivity defect | **AD**; **multiple mtDNA deletions** | adCPEO phenotype centered on ptosis/ophthalmoplegia and mitochondrial myopathy; detailed frequency data limited in retrieved sources (ali2024mitochondrialchronicprogressive pages 3-5, viscomi2017mtdnamaintenancedefectssyndromes pages 2-4) | **OMIM 610131**; listed as AD multiple-deletions adCPEO gene (viscomi2017mtdnamaintenancedefectssyndromes pages 2-4) |
| **DNA2** | Mitochondrial nuclease/helicase involved in primer/flap processing during mtDNA replication | **AD**; **multiple mtDNA deletions** | adCPEO phenotype; usually adult-onset external ophthalmoplegia/myopathy spectrum, with limited quantitative phenotyping in retrieved sources (ali2024mitochondrialchronicprogressive pages 3-5, viscomi2017mtdnamaintenancedefectssyndromes pages 2-4) | **OMIM 615156**; listed as AD multiple-deletions adCPEO gene (viscomi2017mtdnamaintenancedefectssyndromes pages 2-4) |
| **RRM2B** | p53-inducible ribonucleotide reductase small subunit; dNTP supply defect for mtDNA synthesis | **AD** adPEO with **multiple mtDNA deletions**; AR forms can cause depletion or more severe disease | Ophthalmoplegia and ptosis are common; AD cases often have **bulbar dysfunction, hearing loss, and gastrointestinal dysmotility** (ali2024mitochondrialchronicprogressive pages 6-8, ali2024mitochondrialchronicprogressive pages 8-9, viscomi2017mtdnamaintenancedefectssyndromes pages 2-4) | **OMIM 613077**; listed as AD multiple-deletions adCPEO gene (viscomi2017mtdnamaintenancedefectssyndromes pages 2-4) |
| **OPA1 (DOA-plus spectrum)** | Inner mitochondrial membrane dynamin-like GTPase regulating mitochondrial fusion, energetics, and genome stability | **AD**; can cause **multiple mtDNA deletions** in DOA-plus/CPEO spectrum rather than classic isolated adPEO | Bilateral progressive visual loss/optic atrophy with additional CPEO, deafness, ataxia, neuropathy; some families develop parkinsonism/dementia; fibroblasts show mitochondrial fragmentation, impaired bioenergetics, increased autophagy/mitophagy (carelli2015syndromicparkinsonismand pages 1-2, ali2024mitochondrialchronicprogressive pages 8-9, viscomi2017mtdnamaintenancedefectssyndromes pages 2-4) | **DOA-plus OMIM 125250**; gene table lists **OPA1 AD multiple deletions** (viscomi2017mtdnamaintenancedefectssyndromes pages 2-4) |
| **Diagnostic / treatment evidence** | Disease-level hallmark is **secondary mtDNA maintenance failure** causing respiratory-chain dysfunction in post-mitotic tissues | Typical Mendelian adCPEO mechanism is **multiple mtDNA deletions**; biopsy often shows **ragged-red fibers** and scattered **COX-negative fibers**; genetic sequencing is current diagnostic gold standard, with **FGF21/GDF15** useful as first-line adjunct biomarkers (ali2024mitochondrialchronicprogressive pages 1-3, viscomi2017mtdnamaintenancedefectssyndromes pages 2-4, lehtonen2021diagnosticvalueof pages 1-8) | Hallmark phenotype: slowly progressive bilateral ptosis and ophthalmoplegia, often without diplopia; onset commonly **20–40 y**; symptom management includes ptosis surgery, prisms/strabismus care, supportive mitochondrial-disease management (viscomi2017mtdnamaintenancedefectssyndromes pages 2-4, ali2024mitochondrialchronicprogressive pages 3-5) | **2024 post-hoc elamipretide signal:** in MMPOWER-3, subjects with replisome variants plus CPEO improved **37.3 ± 9.5 m** on 6MWT vs **−8.0 ± 10.7 m** for placebo at week 24 (**p = 0.0024**); however this was a **post-hoc subgroup finding** after the overall heterogeneous Phase 3 trial was negative, so it is hypothesis-generating rather than definitive (karaa2024genotypespecificeffectsof pages 2-5, karaa2024genotypespecificeffectsof pages 1-2, NCT05162768 chunk 1) |


*Table: This table summarizes the core genes, mechanisms, clinical hallmarks, and key diagnostic/treatment evidence for autosomal dominant progressive external ophthalmoplegia. It is designed for rapid knowledge-base ingestion and highlights both established mtDNA-maintenance biology and the 2024 exploratory elamipretide signal with appropriate caution.*

## 1. Disease information

### Definition

adPEO is an autosomal dominant mtDNA-maintenance disorder. Historically, dominant inheritance was established when affected males transmitted CPEO to offspring, excluding maternal mtDNA inheritance. The syndrome is clinically defined by adult-onset CPEO, genetically by dominant transmission, and molecularly by multiple mtDNA deletions. (viscomi2017mtdnamaintenancedefectssyndromes pages 2-4)

The current clinical concept distinguishes:

* **Isolated adPEO:** ptosis/ophthalmoparesis with limited systemic disease.
* **adPEO-plus:** additional myopathy, dysphagia, neuropathy, ataxia, hearing loss, cataracts, parkinsonism, psychiatric disease, or endocrine abnormalities.
* **OPA1 “DOA-plus”:** optic atrophy with CPEO and other neurologic manifestations.
* **Not adPEO:** sporadic CPEO from a single large-scale mtDNA deletion; maternally inherited mtDNA point-variant disease; KSS; and autosomal recessive PEO syndromes. (viscomi2017mtdnamaintenancedefectssyndromes pages 2-4, ali2024mitochondrialchronicprogressive pages 8-9, ali2024mitochondrialchronicprogressive pages 3-5)

### Identifiers and synonyms

* **Preferred name:** autosomal dominant progressive external ophthalmoplegia.
* **Synonyms:** adPEO, autosomal dominant chronic progressive external ophthalmoplegia, adCPEO, dominant PEO, progressive external ophthalmoplegia with multiple mtDNA deletions.
* **MeSH phenotype:** *Ophthalmoplegia, Chronic Progressive External*, **D017246**. (NCT02161848 chunk 1)
* **OMIM phenotypic series represented by gene-specific entries:** POLG/SLC25A4-associated dominant PEO **157640**; TWNK **609286**; POLG2 **610131**; DNA2 **615156**; RRM2B **613077**. OPA1 DOA-plus is **125250** and should be represented as an overlapping disorder rather than indiscriminately merged with classic isolated adPEO. (viscomi2017mtdnamaintenancedefectssyndromes pages 2-4)
* **MONDO:** a single stable MONDO identifier for the entire genetically heterogeneous umbrella was not verified in the retrieved evidence; knowledge-base ingestion should map gene-specific disease entities rather than assign an unverified umbrella ID.
* **Orphanet/ICD:** no adPEO-specific Orphanet or ICD-10/ICD-11 identifier was verified. Coding generally falls under mitochondrial myopathy/mitochondrial disease or progressive external ophthalmoplegia.

The evidence summarized here is **aggregated disease-level literature, cohorts, reviews, and trial records**, not individual EHR-derived information.

## 2. Etiology, risk, protective factors, and environment

### Primary cause

The cause is a heterozygous pathogenic germline variant in a nuclear-encoded mitochondrial maintenance gene. Functionally, affected genes fall into three major modules:

1. **mtDNA replisome/processing:** POLG, POLG2, TWNK, DNA2.
2. **Nucleotide supply or transport:** RRM2B and SLC25A4/ANT1.
3. **Mitochondrial dynamics/genome organization:** OPA1 in the DOA-plus overlap phenotype. (viscomi2017mtdnamaintenancedefectssyndromes pages 2-4, ali2024mitochondrialchronicprogressive pages 3-5)

The broader CPEO differential includes recessive defects in RNASEH1, MGME1, TK2, DGUOK, MPV17, TYMP and other genes, but these should not be annotated as causes of classic autosomal dominant PEO without variant- and inheritance-specific evidence. (ali2024mitochondrialchronicprogressive pages 1-3, ali2024mitochondrialchronicprogressive pages 8-9, viscomi2017mtdnamaintenancedefectssyndromes pages 2-4)

### Genetic risk factors

A pathogenic heterozygous variant and an affected first-degree relative are the principal risk factors. Most disease variants are rare or absent from population databases; no single population allele frequency or carrier frequency can validly represent this heterogeneous disorder. Variant interpretation should use ACMG/AMP criteria, ClinVar assertions, segregation, phenotype concordance, population rarity, and functional evidence. Variants of uncertain significance must not be treated as diagnostic.

Mechanism varies by gene and allele. Dominant POLG, TWNK and POLG2 alleles often impair replisome function through dominant-negative or deleterious heterozygous effects; SLC25A4 variants impair adenine-nucleotide transport and can destabilize mtDNA; RRM2B variants disturb dNTP supply; OPA1 variants disturb inner-membrane fusion, bioenergetics and mtDNA stability. Exact mechanism cannot be assumed from gene name alone and should be assigned at variant level. (carelli2015syndromicparkinsonismand pages 1-2, ali2024mitochondrialchronicprogressive pages 3-5, viscomi2017mtdnamaintenancedefectssyndromes pages 2-4)

### Environmental, infectious, lifestyle, and protective factors

No environmental toxin, infectious agent, diet, sex, occupation, smoking exposure, or common lifestyle factor is established as a primary cause of adPEO. No validated protective nuclear allele, modifier locus, diet, supplement, or prophylactic drug prevents penetrance. Physiological aging plausibly permits progressive clonal expansion of mtDNA deletions, but this is part of disease expression rather than an established preventable exposure.

Avoidance of mitochondrial stressors, maintenance of activity within tolerance, and management of cardiovascular/metabolic risks are prudent supportive measures, not proven primary prevention. A ketogenic diet should not be generalized to deletion-associated mitochondrial myopathy; broader evidence reports rhabdomyolysis in adults with mtDNA-deletion myopathy.

### Gene–environment interaction

Robust adPEO-specific gene–environment interaction studies are unavailable. Energy demand, aging, illness, fasting, anesthesia, and mitochondrial-toxic medications may unmask or worsen mitochondrial dysfunction clinically, but quantitative interaction estimates for adPEO have not been established.

## 3. Phenotypes

### Core manifestations

* **Progressive external ophthalmoplegia/ophthalmoparesis — HP:0000590:** bilateral, usually symmetric, omnidirectional limitation of gaze; progressive and effectively universal in clinically defined adCPEO. Slowed, incomplete saccades may precede obvious ophthalmoplegia. Symmetry makes diplopia less common than expected. (ali2024mitochondrialchronicprogressive pages 3-5, viscomi2017mtdnamaintenancedefectssyndromes pages 2-4)
* **Ptosis — HP:0000508:** usually bilateral and progressive; described as present in all patients in the adCPEO clinical definition. Levator excursion may be **<8–10 mm**, compared with normal **≥12 mm**. Severe ptosis impairs the superior visual field, reading, driving, mobility, and social interaction. (ali2024mitochondrialchronicprogressive pages 3-5, viscomi2017mtdnamaintenancedefectssyndromes pages 2-4)
* **Muscle weakness — HP:0001324; proximal weakness HP:0003701:** frequent but not obligatory; commonly accompanied by exercise intolerance (**HP:0003546**) and fatigue. Functional consequences include reduced walking endurance and difficulty climbing stairs or rising from a chair. (karaa2024genotypespecificeffectsof pages 2-5, karaa2024genotypespecificeffectsof pages 1-2, viscomi2017mtdnamaintenancedefectssyndromes pages 2-4)

### Variable “PEO-plus” manifestations

Reported features include dysphagia (**HP:0002015**), dysarthria (**HP:0001260**), dysphonia (**HP:0001618**), facial weakness (**HP:0000297**), peripheral neuropathy (**HP:0009830**), sensory ataxia/cerebellar ataxia (**HP:0001251**), sensorineural hearing loss (**HP:0000407**), cataract (**HP:0000518**), hypogonadism (**HP:0000135**), parkinsonism (**HP:0001300**), depression (**HP:0000716**), and psychiatric abnormalities. RRM2B-dominant PEO particularly associates with bulbar dysfunction, hearing loss, and gastrointestinal dysmotility. TWNK disease ranges from isolated CPEO to weakness, dysarthria, dysphagia, and occasional cardiac involvement. (ali2024mitochondrialchronicprogressive pages 6-8, ali2024mitochondrialchronicprogressive pages 8-9, viscomi2017mtdnamaintenancedefectssyndromes pages 2-4)

OPA1-related dominant CPEO may additionally produce optic atrophy (**HP:0000648**), progressive central/color-vision loss, deafness, neuropathy, ataxia, parkinsonism and dementia. A primary study of two Italian OPA1 families included **21 affected individuals** and documented CPEO with mitochondrial myopathy and neurodegenerative features. (carelli2015syndromicparkinsonismand pages 1-2, ali2024mitochondrialchronicprogressive pages 8-9)

### Laboratory and pathology phenotypes

* Multiple mtDNA deletions in muscle.
* Ragged-red fibers (**HP:0003200**) caused by subsarcolemmal mitochondrial proliferation.
* Scattered cytochrome-c-oxidase-negative fibers (**HP:0003688**).
* Respiratory-chain activities can range from normal to about **50% of control mean** in muscle homogenate.
* Resting hyperlactatemia (**HP:0002151**) is generally confined to severely affected patients and is neither sensitive nor specific. (lehtonen2021diagnosticvalueof pages 1-8, viscomi2017mtdnamaintenancedefectssyndromes pages 2-4)

### Frequency and quality-of-life evidence

Ptosis and eye-movement restriction are core/universal by clinical definition; generalized weakness is described as frequent. Reliable percentages for most extraocular manifestations are unavailable because published cohorts are small and genotype-heterogeneous. Formal adPEO-specific EQ-5D, SF-36 or PROMIS estimates were not retrieved. Nevertheless, physical function and quality of life are adversely affected by ptosis, visual-field restriction, dysphagia, fatigue, weakness and reduced exercise capacity. (karaa2024genotypespecificeffectsof pages 1-2, viscomi2017mtdnamaintenancedefectssyndromes pages 2-4)

## 4. Genetic and molecular information

### Causal genes and molecular consequences

The gene-level summary is provided in the artifact above. The best-established classic dominant entities are:

* **POLG:** catalytic polymerase-γ subunit; dominant PEO, multiple mtDNA deletions; OMIM 157640.
* **TWNK/C10orf2:** mitochondrial helicase; dominant adult-onset PEO, multiple deletions; OMIM 609286.
* **SLC25A4/ANT1:** adenine-nucleotide translocator; dominant PEO with multiple deletions; associated with OMIM 157640.
* **POLG2:** polymerase-γ accessory subunit; dominant PEO, multiple deletions; OMIM 610131.
* **DNA2:** nuclease/helicase involved in flap and primer processing; dominant PEO; OMIM 615156.
* **RRM2B:** ribonucleotide-reductase small subunit controlling dNTP supply; dominant PEO; OMIM 613077.
* **OPA1:** mitochondrial inner-membrane fusion GTPase; dominant optic-atrophy-plus with CPEO and multiple deletions; OMIM 125250. (ali2024mitochondrialchronicprogressive pages 3-5, viscomi2017mtdnamaintenancedefectssyndromes pages 2-4)

### Variant classes and origin

Disease-associated alleles include missense, nonsense, frameshift and splice variants, depending on gene. The causal variants are constitutional/germline, not somatic cancer variants. The **secondary mtDNA deletions are somatically accumulated and clonally expanded within affected post-mitotic cells**, explaining tissue mosaicism and why blood can be diagnostically insensitive. Variant-specific ClinVar classification and gnomAD frequency must be recorded at the exact HGVS allele level; no universal adPEO allele frequency exists.

### Modifiers, epigenetics, and chromosomes

No validated modifier gene or protective allele is established for routine clinical use. Phenotypic variability likely reflects allele-specific activity, nuclear background, tissue-specific mtDNA deletion burden, age, and stochastic clonal expansion. No reproducible adPEO-specific DNA-methylation, histone, chromatin or episignature is established. Large chromosomal abnormalities, aneuploidy, balanced translocations, karyotyping and FISH are not characteristic diagnostic targets.

## 5. Environmental information

adPEO is a primary genetic mitochondrial disorder. Environmental pollutants, radiation, toxins and infectious pathogens are not established causes. Lifestyle is more relevant to management than etiology: prolonged inactivity can worsen deconditioning, whereas excessive exertion may exacerbate fatigue. Medication review should be individualized by a mitochondrial specialist. There is no vaccine, antimicrobial therapy, exposure-remediation program, or public-health control measure specific to adPEO.

## 6. Mechanism and pathophysiology

### Causal chain

**Upstream genetic defect → mtDNA-maintenance failure → multiple mtDNA deletions → mosaic respiratory-chain deficiency → ATP shortfall and stress responses → selective dysfunction of high-energy post-mitotic cells → ptosis, ophthalmoplegia, myopathy and genotype-dependent multisystem disease.**

POLG/POLG2/TWNK/DNA2 directly impair mtDNA replication or processing; RRM2B alters dNTP supply; SLC25A4 alters adenine-nucleotide exchange and mitochondrial homeostasis; OPA1 alters inner-membrane fusion, cristae structure, genome maintenance and quality control. (ramon2021therapyprospectsfor pages 1-2, ali2024mitochondrialchronicprogressive pages 3-5, viscomi2017mtdnamaintenancedefectssyndromes pages 2-4)

Deletion-bearing mtDNA molecules clonally expand within individual fibers until a biochemical threshold is crossed. Complexes containing mtDNA-encoded subunits—respiratory complexes I, III, IV and V—then become deficient. This compromises oxidative phosphorylation, lowers ATP-generating capacity, and promotes compensatory mitochondrial proliferation, producing ragged-red fibers. Extraocular muscles are especially vulnerable because of their continuous activity and unusual mitochondrial/physiological demands. (ramon2021therapyprospectsfor pages 1-2, viscomi2017mtdnamaintenancedefectssyndromes pages 2-4)

### Cellular and tissue mechanisms

Relevant processes and suggested GO annotations include:

* mtDNA replication — **GO:0006264**;
* mitochondrial genome maintenance — **GO:0000002**;
* mitochondrial DNA repair — **GO:0043504**;
* oxidative phosphorylation — **GO:0006119**;
* respiratory electron transport chain — **GO:0022904**;
* ATP metabolic process — **GO:0046034**;
* mitochondrial fusion — **GO:0008053**;
* mitophagy — **GO:0000423**;
* response to oxidative stress — **GO:0006979**.

OPA1 patient fibroblasts provide human in-vitro evidence of reduced OPA1 protein, fragmented mitochondria, impaired bioenergetics and increased autophagy/mitophagy. Muscle from affected families showed multiple mtDNA deletions and COX-negative fibers. (carelli2015syndromicparkinsonismand pages 1-2)

Suggested cellular annotations are skeletal muscle fiber/myocyte (**CL:0000188**), extraocular skeletal muscle fiber, motor neuron (**CL:0000100**) where neuropathy is present, retinal ganglion cell (**CL:0000740**) in OPA1 disease, and cochlear sensory hair cell for hearing involvement.

### Immune, biochemical and omics evidence

Autoimmunity and primary immunodeficiency are not central mechanisms. Secondary oxidative stress and mitochondrial integrated stress-response signaling occur, but inflammatory biomarkers are not validated diagnostic or prognostic measures. FGF21 and GDF15 reflect mitochondrial stress and muscle-manifesting mtDNA-expression disease rather than a disease-specific immune process. (lehtonen2021diagnosticvalueof pages 1-8)

No mature adPEO-specific single-cell atlas, spatial-transcriptomic map, lipidomic diagnostic signature, integrated multi-omic classifier, or CRISPR-screen-derived treatment is established. Tissue-level histochemistry, mtDNA deletion analysis and fibroblast bioenergetics remain more developed than advanced cell-resolved profiling.

## 7. Anatomical structures affected

### Primary sites

* **Extraocular muscles**—bilateral levator palpebrae superioris and multiple rectus/oblique muscles; suggested UBERON: extraocular muscle **UBERON:0001627**.
* **Upper eyelid/levator apparatus**—ptosis.
* **Skeletal muscle**—axial, proximal limb, facial and bulbar muscle to variable degrees; **UBERON:0001134**.

### Secondary/genotype-dependent sites

Peripheral nerves, cerebellum, basal ganglia, cochlea, optic nerve/retinal ganglion-cell layer, gastrointestinal smooth-muscle/enteric system, endocrine organs and occasionally heart can be involved. OPA1 disease particularly affects the optic nerve and retinal ganglion cells; RRM2B may involve bulbar and gastrointestinal systems. (carelli2015syndromicparkinsonismand pages 1-2, ali2024mitochondrialchronicprogressive pages 6-8, ali2024mitochondrialchronicprogressive pages 8-9)

### Subcellular localization

The principal compartment is the mitochondrion (**GO:0005739**), especially mitochondrial matrix (**GO:0005759**) for the replisome, inner mitochondrial membrane (**GO:0005743**) for SLC25A4 and OPA1-associated processes, and mitochondrial nucleoid (**GO:0042645**). Nuclear DNA carries the inherited variant, whereas the downstream deletions occur in mtDNA.

Disease is characteristically bilateral and broadly symmetric; marked asymmetry or isolated cranial-nerve-pattern ophthalmoplegia should prompt reconsideration of the diagnosis. (ali2024mitochondrialchronicprogressive pages 3-5)

## 8. Temporal development

Typical onset is insidious between **20 and 40 years**, although earlier and later onset occur. Slowed saccades and ptosis may precede fixed ophthalmoplegia. Symptoms progress slowly with age over decades; the course is chronic and lifelong, not relapsing-remitting. (viscomi2017mtdnamaintenancedefectssyndromes pages 2-4, ali2024mitochondrialchronicprogressive pages 3-5)

A practical staging scheme, although not formally validated, is:

1. **Early:** subtle bilateral ptosis, reduced saccadic velocity or exercise intolerance.
2. **Intermediate:** obvious multidirectional ophthalmoparesis, visual-field obstruction, limb/axial weakness.
3. **Advanced:** near-complete external ophthalmoplegia, severe ptosis and genotype-dependent bulbar, respiratory, neuropathic or neurologic complications.

There is no spontaneous biological remission. Surgical correction can improve ptosis or strabismus but does not stop mtDNA-deletion accumulation. No validated presymptomatic intervention window has been established, although early molecular diagnosis enables surveillance and reproductive counseling.

## 9. Inheritance and population

Inheritance is autosomal dominant: each child of a heterozygous affected individual has a theoretical **50% chance** of inheriting the variant. Penetrance is often age-dependent and may be incomplete; expressivity is markedly variable within and between families. Male-to-male transmission can occur. Genetic anticipation is not established. Germline mosaicism is theoretically possible but not quantified. Consanguinity is not a typical risk factor for dominant disease, although it matters in recessive PEO differentials. (viscomi2017mtdnamaintenancedefectssyndromes pages 2-4)

No robust adPEO-specific prevalence or incidence estimate was found. Broader primary mitochondrial myopathy has been estimated at **1–2 per 10,000**, while all adult mitochondrial disease has been estimated near **1 in 4,300**; these values must not be presented as adPEO prevalence. (karaa2024genotypespecificeffectsof pages 1-2, lim2021riskofcardiac pages 1-2)

No consistent sex bias or globally restricted ethnic distribution is established. Founder variants may exist in individual pedigrees or populations but do not define the overall disorder. Carrier frequency cannot be summarized without selecting a gene and exact pathogenic allele.

## 10. Diagnostics

### Clinical recognition and differential diagnosis

Suspect adPEO in chronic, symmetric bilateral ptosis plus progressive multidirectional ophthalmoparesis, especially with a dominant pedigree, exercise intolerance, proximal weakness, hearing loss, neuropathy, ataxia or dysphagia.

Important differentials are myasthenia gravis, oculopharyngeal muscular dystrophy, congenital fibrosis of the extraocular muscles, thyroid eye disease, cranial neuropathy, brainstem disease, muscular dystrophy, KSS, sporadic single-mtDNA-deletion CPEO, recessive PEO, and OPA1 optic-atrophy-plus disease. Fluctuation and fatigability suggest myasthenia; a PABPN1 expansion and prominent pharyngeal weakness suggest oculopharyngeal muscular dystrophy; onset before 20 years with pigmentary retinopathy and cardiac conduction disease suggests KSS. (ali2024mitochondrialchronicprogressive pages 3-5)

### Recommended testing pathway

1. **Phenotype and pedigree:** neuro-ophthalmic examination, eyelid excursion, saccades, diplopia/strabismus, muscle strength, gait, hearing, swallowing and neuropathy assessment.
2. **Genetic testing first:** a nuclear mtDNA-maintenance/mitochondrial myopathy panel or WES/WGS with analysis of **POLG, TWNK, SLC25A4, POLG2, DNA2, RRM2B**, and relevant overlapping/recessive genes. Concurrent full mtDNA sequencing and deletion analysis helps distinguish dominant nuclear disease from primary mtDNA disease. Genetic sequencing is considered the diagnostic gold standard. (ali2024mitochondrialchronicprogressive pages 1-3)
3. **Tissue-aware mtDNA analysis:** if blood is negative but suspicion remains high, test skeletal muscle—or another informative tissue—for multiple mtDNA deletions and heteroplasmy. Standard short-read WES may miss mtDNA rearrangements, repeat expansions, or poorly covered regions.
4. **Serum adjuncts:** lactate, CK, FGF21 and GDF15. In a 194-sample study, only **39%** of genetically verified mitochondrial cases had mitochondrial pathology on muscle histology, versus biomarker elevation in **62%**. In myopathic disease with at least one elevated biomarker, an mtDNA-expression disorder was the cause with **94% probability**. When biomarker sampling and biopsy were within 12 months, biomarkers would identify **70%**, compared with **50%** by biopsy alone. Normal values do not exclude disease. (lehtonen2021diagnosticvalueof pages 1-8)
5. **Muscle biopsy when genetics is unresolved:** modified Gomori trichrome for ragged-red fibers, COX/SDH histochemistry, respiratory-chain enzymology, mtDNA copy number and long-range PCR/NGS for multiple deletions. (ali2024mitochondrialchronicprogressive pages 1-3, viscomi2017mtdnamaintenancedefectssyndromes pages 2-4)
6. **Targeted ancillary testing:** EMG/NCS, audiology, ECG/echocardiography when indicated, pulmonary function and sleep studies for respiratory weakness, swallow assessment, brain MRI for neurologic disease, and OCT/visual testing for OPA1 phenotypes.

A completed CPEO MRI study, **NCT02161848**, enrolled 133 participants and evaluated extraocular-muscle volume, limb-muscle fat fraction and strength; its principal CPEO arm involved verified single large-scale mtDNA deletions, so it demonstrates real-world quantitative imaging implementation but is not adPEO-specific. (NCT02161848 chunk 1)

CMA, karyotyping and FISH have low expected yield absent syndromic evidence of a chromosomal disorder. Repeat-expansion testing is not an adPEO test but may be needed for differential diagnoses. RNA sequencing can resolve splice variants in selected cases; proteomics, metabolomics, epigenomics and liquid biopsy are not validated routine tests.

### Screening

There is no newborn or population screening. Once a familial pathogenic variant is known, targeted cascade testing is appropriate for adult relatives and, with counseling, minors when childhood surveillance would alter management. Prenatal diagnosis and preimplantation genetic testing for monogenic disease are technically feasible for a known nuclear variant.

## 11. Outcome and prognosis

adPEO is usually slowly progressive and compatible with long survival, but no reliable disease-specific five-year survival, mortality rate or life-expectancy estimate is available. Prognosis depends more on systemic genotype-specific involvement than on ophthalmoplegia itself. Isolated disease mainly causes chronic visual and physical disability; bulbar or respiratory weakness, severe neuropathy, parkinsonism/dementia, or cardiac involvement increases morbidity.

In a cohort of **146 adults** with nuclear-gene mitochondrial disease, cardiac abnormalities occurred in **14 (9.6%)**, but only **7 (4.8%)** had early manifestations attributed to the genetic disorder; the study concluded that cardiac risk was genotype-specific rather than uniformly high. This cohort included TWNK, POLG, RRM2B and OPA1, but its aggregate rate should not be treated as an adPEO-specific estimate. (lim2021riskofcardiac pages 1-2)

Recovery of lost ocular motility is generally not expected. Ptosis and strabismus surgery can improve function, but recurrence or exposure keratopathy may occur because the underlying myopathy progresses. No validated molecular prognostic biomarker predicts individual progression. Age at onset, burden of systemic manifestations, respiratory/bulbar involvement, and exact genotype are the most clinically useful prognostic factors.

## 12. Treatment

### Current standard care

There is no approved curative or disease-modifying therapy specifically for adPEO. Management is multidisciplinary and symptom-directed. The 2024 review states that no definitive mitochondrial-disease treatment is available and emphasizes genetic diagnosis, lifestyle-risk modification, supportive supplementation and ptosis correction. (ali2024mitochondrialchronicprogressive pages 1-3)

* **Ptosis:** eyelid crutches may be tried but often have poor comfort/cosmesis. Mild levator dysfunction may be treated with levator resection; severe dysfunction commonly requires frontalis suspension using fascia lata or silicone. Corneal exposure risk must be assessed because orbicularis weakness and poor Bell phenomenon can make overcorrection hazardous. Suggested NCIT concepts: *Ptosis Repair*, *Frontalis Suspension Procedure*.
* **Diplopia/strabismus:** prisms for small deviations; selected strabismus surgery for persistent symptomatic malalignment. Suggested NCIT: *Strabismus Surgery*.
* **Myopathy:** individualized aerobic and resistance activity below overexertion thresholds, physical and occupational therapy, mobility aids and fall prevention. Suggested NCIT: *Physical Therapy*, *Occupational Therapy*, *Exercise Therapy*.
* **Bulbar/respiratory disease:** speech/swallow therapy, dietetic support, aspiration precautions, pulmonary testing and non-invasive ventilation when indicated.
* **Hearing loss:** hearing aids or cochlear implantation as clinically appropriate.
* **Neuropathy/parkinsonism/endocrine complications:** standard symptom-specific treatment; parkinsonism in some mitochondrial CPEO syndromes can be levodopa responsive. (carelli2015syndromicparkinsonismand pages 1-2, ali2024mitochondrialchronicprogressive pages 3-5)

No adPEO-specific pharmacogenomic guideline exists. Supplement “mitochondrial cocktails” have uncertain efficacy and should not substitute for surveillance or rehabilitation.

### Elamipretide and recent clinical development

MMPOWER-3 was a 24-week, randomized, double-blind trial of subcutaneous elamipretide 40 mg/day. The overall heterogeneous PMM population did **not** meet primary 6MWT or fatigue endpoints. In exploratory analyses, the nDNA cohort (**n=59**) improved by 25.2 m versus 0.3 m with placebo (**p=0.03**). The strongest signal was the replisome-plus-CPEO subgroup: elamipretide **n=18**, baseline 316.5±17.5 m, improved **37.3±9.5 m**; placebo **n=14**, baseline 324.0±23.4 m, changed **−8.0±10.7 m**, **p=0.0024**. A weak exposure-response correlation was observed (**r=0.308; p=0.0262**). These analyses were published in November 2024, DOI: https://doi.org/10.1186/s13023-024-03421-5; parent trial **NCT03323749**. (karaa2024genotypespecificeffectsof pages 2-5, karaa2024genotypespecificeffectsof pages 1-2)

NuPOWER, **NCT05162768**, was a 48-week Phase 3, quadruple-masked trial of elamipretide **60 mg subcutaneously daily** versus placebo in nuclear-DNA PMM with PEO and weakness/exercise intolerance. It enrolled **102 participants**, began 29 April 2022, completed 4 December 2024, and is listed as completed; included genes encompassed POLG1/2, TWNK, RRM2B, RNASEH1, DNA2 and SLC25A4. Registry results were not available in the retrieved record, so efficacy cannot be inferred from completion status. https://clinicaltrials.gov/study/NCT05162768. (NCT05162768 chunk 1)

Gene replacement, gene editing, RNA therapy, substrate enhancement and mitochondrial genome manipulation remain experimental. No adPEO gene therapy or cell therapy has regulatory approval. Therapeutic development is complicated by dominant alleles, multiple causal genes, tissue distribution and the need to prevent or reverse clonally expanded mtDNA deletions. (ramon2021therapyprospectsfor pages 1-2)

## 13. Prevention

Primary prevention by lifestyle change is not possible because adPEO is a germline Mendelian disease. There is no immunization or chemoprophylaxis.

**Secondary prevention** consists of cascade testing, early recognition of systemic disease, and genotype-directed surveillance. **Tertiary prevention** includes fall prevention, aspiration precautions, respiratory support, corneal-protection strategies, hearing support, rehabilitation, and prompt treatment of endocrine or cardiac complications.

Genetic counseling should explain autosomal dominant transmission, age-dependent penetrance, variable expressivity and a 50% transmission probability. For a known familial variant, reproductive options include natural conception with prenatal testing, preimplantation genetic testing, donor gametes and adoption. These nuclear-gene options differ fundamentally from mitochondrial-donation strategies used for maternally inherited mtDNA variants.

## 14. Other species and natural disease

No well-established naturally occurring veterinary syndrome equivalent to human genetically confirmed adPEO was identified in the retrieved evidence. Therefore, breed associations, VBO terms, incidence in companion animals, and veterinary screening recommendations remain unavailable. The disease is noninfectious and has no zoonotic or cross-species transmission potential.

The underlying proteins are evolutionarily conserved in mammals and lower eukaryotes, enabling mechanistic modeling. Relevant taxa include *Mus musculus* (**NCBI Taxonomy 10090**), *Saccharomyces cerevisiae* (**559292**) and *Podospora anserina* (**5145**).

## 15. Model organisms and experimental systems

### Mouse models

* **Ant1/SLC25A4-deficient mice:** reproduce mitochondrial myopathy features, COX-negative fibers and mtDNA instability, but may retain normal ocular motility despite CPEO-like pathology. This is an important limitation: muscle pathology does not guarantee faithful reproduction of the human extraocular phenotype.
* **Brain-specific Ant1 heterozygous conditional knockout:** shows COX-negative dorsal-raphe cells, neuronal hyperexcitability and altered serotonergic signaling, useful for investigating neuropsychiatric manifestations but not a complete adPEO model.
* **Twinkle “Deletor” transgenic mice:** accumulate multiple mtDNA deletions and develop late-onset mitochondrial myopathy; valuable for deletion dynamics, aging and therapeutic studies, but disease tempo and ocular phenotype differ from humans.
* **POLG mutator models:** useful for mtDNA mutation burden, aging and mitochondrial dysfunction, but proofreading-deficient models are not exact replicas of most heterozygous human adPEO alleles.

### Cellular and lower-eukaryote models

Patient fibroblasts and myoblasts support variant validation, mitochondrial morphology, respiration, mtDNA copy/deletion and mitophagy studies. OPA1-family fibroblasts demonstrated fragmentation, impaired bioenergetics and increased autophagy/mitophagy, providing direct human cellular evidence. (carelli2015syndromicparkinsonismand pages 1-2)

Yeast provides rapid functional complementation and drug-screening assays for conserved mitochondrial maintenance genes. It is cost-effective and scalable but lacks extraocular muscles and mammalian tissue physiology. Organoids and iPSC-derived myotubes are promising but not yet validated as predictive adPEO treatment platforms.

## Evidence limitations and expert interpretation

The evidence base is constrained by rare-disease sample sizes, allelic heterogeneity, inconsistent use of “PEO” and “CPEO,” and frequent pooling of dominant nuclear disease with single-mtDNA-deletion or recessive syndromes. Consequently, phenotype percentages, penetrance, incidence, life expectancy and treatment-response rates remain poorly defined. The most defensible knowledge-base architecture is **gene- and inheritance-specific**, with adPEO represented as a clinical/molecular umbrella linked to distinct entities rather than as one homogeneous disease.

Key abstract-supported statements include the 2024 review’s conclusion that “genetic sequencing is the gold standard” and that “no definitive treatment option is available,” the biomarker study’s recommendation that “FGF21 and GDF15 together should be first-line diagnostic investigations,” and the 2024 elamipretide paper’s conclusion that genotype-specific findings justify targeted trials. These statements support current expert practice but should be interpreted alongside the limitations above. (ali2024mitochondrialchronicprogressive pages 1-3, karaa2024genotypespecificeffectsof pages 1-2, lehtonen2021diagnosticvalueof pages 1-8)

References

1. (viscomi2017mtdnamaintenancedefectssyndromes pages 2-4): Carlo Viscomi and Massimo Zeviani. Mtdna-maintenance defects: syndromes and genes. Journal of Inherited Metabolic Disease, 40:587-599, Mar 2017. URL: https://doi.org/10.1007/s10545-017-0027-5, doi:10.1007/s10545-017-0027-5. This article has 226 citations and is from a peer-reviewed journal.

2. (ali2024mitochondrialchronicprogressive pages 3-5): Ali Ali, Ali Esmaeil, and Raed Behbehani. Mitochondrial chronic progressive external ophthalmoplegia. Brain Sciences, 14:135, Jan 2024. URL: https://doi.org/10.3390/brainsci14020135, doi:10.3390/brainsci14020135. This article has 25 citations.

3. (karaa2024genotypespecificeffectsof pages 2-5): Amel Karaa, Enrico Bertini, Valerio Carelli, Bruce Cohen, Gregory M. Ennes, Marni J. Falk, Amy Goldstein, Gráinne Gorman, Richard Haas, Michio Hirano, Thomas Klopstock, Mary Kay Koenig, Cornelia Kornblum, Costanza Lamperti, Anna Lehman, Nicola Longo, Maria Judit Molnar, Sumit Parikh, Han Phan, Robert D. S. Pitceathly, Russekk Saneto, Fernando Scaglia, Serenella Servidei, Mark Tarnopolsky, Antonio Toscano, Johan L. K. Van Hove, John Vissing, Jerry Vockley, Jeffrey S. Finman, Anthony Abbruscato, David A. Brown, Alana Sullivan, James A. Shiffer, and Michelango Mancuso. Genotype-specific effects of elamipretide in patients with primary mitochondrial myopathy: a post hoc analysis of the mmpower-3 trial. Orphanet Journal of Rare Diseases, Nov 2024. URL: https://doi.org/10.1186/s13023-024-03421-5, doi:10.1186/s13023-024-03421-5. This article has 15 citations and is from a peer-reviewed journal.

4. (karaa2024genotypespecificeffectsof pages 1-2): Amel Karaa, Enrico Bertini, Valerio Carelli, Bruce Cohen, Gregory M. Ennes, Marni J. Falk, Amy Goldstein, Gráinne Gorman, Richard Haas, Michio Hirano, Thomas Klopstock, Mary Kay Koenig, Cornelia Kornblum, Costanza Lamperti, Anna Lehman, Nicola Longo, Maria Judit Molnar, Sumit Parikh, Han Phan, Robert D. S. Pitceathly, Russekk Saneto, Fernando Scaglia, Serenella Servidei, Mark Tarnopolsky, Antonio Toscano, Johan L. K. Van Hove, John Vissing, Jerry Vockley, Jeffrey S. Finman, Anthony Abbruscato, David A. Brown, Alana Sullivan, James A. Shiffer, and Michelango Mancuso. Genotype-specific effects of elamipretide in patients with primary mitochondrial myopathy: a post hoc analysis of the mmpower-3 trial. Orphanet Journal of Rare Diseases, Nov 2024. URL: https://doi.org/10.1186/s13023-024-03421-5, doi:10.1186/s13023-024-03421-5. This article has 15 citations and is from a peer-reviewed journal.

5. (ali2024mitochondrialchronicprogressive pages 6-8): Ali Ali, Ali Esmaeil, and Raed Behbehani. Mitochondrial chronic progressive external ophthalmoplegia. Brain Sciences, 14:135, Jan 2024. URL: https://doi.org/10.3390/brainsci14020135, doi:10.3390/brainsci14020135. This article has 25 citations.

6. (ali2024mitochondrialchronicprogressive pages 8-9): Ali Ali, Ali Esmaeil, and Raed Behbehani. Mitochondrial chronic progressive external ophthalmoplegia. Brain Sciences, 14:135, Jan 2024. URL: https://doi.org/10.3390/brainsci14020135, doi:10.3390/brainsci14020135. This article has 25 citations.

7. (carelli2015syndromicparkinsonismand pages 1-2): Valerio Carelli, Olimpia Musumeci, Leonardo Caporali, Claudia Zanna, Chiara La Morgia, Valentina Del Dotto, Anna Maria Porcelli, Michela Rugolo, Maria Lucia Valentino, Luisa Iommarini, Alessandra Maresca, Piero Barboni, Michele Carbonelli, Costantino Trombetta, Enza Maria Valente, Simone Patergnani, Carlotta Giorgi, Paolo Pinton, Giovanni Rizzo, Caterina Tonon, Raffaele Lodi, Patrizia Avoni, Rocco Liguori, Agostino Baruzzi, Antonio Toscano, and Massimo Zeviani. Syndromic parkinsonism and dementia associated with opa 1 missense mutations. Annals of Neurology, 78:21-38, Jun 2015. URL: https://doi.org/10.1002/ana.24410, doi:10.1002/ana.24410. This article has 219 citations and is from a highest quality peer-reviewed journal.

8. (ali2024mitochondrialchronicprogressive pages 1-3): Ali Ali, Ali Esmaeil, and Raed Behbehani. Mitochondrial chronic progressive external ophthalmoplegia. Brain Sciences, 14:135, Jan 2024. URL: https://doi.org/10.3390/brainsci14020135, doi:10.3390/brainsci14020135. This article has 25 citations.

9. (lehtonen2021diagnosticvalueof pages 1-8): Jenni M. Lehtonen, Mari Auranen, Niklas Darin, Kalliopi Sofou, Laurence Bindoff, Omar Hikmat, Johanna Uusimaa, Päivi Vieira, Már Tulinius, Tuula Lönnqvist, Irenaeus F. de Coo, Anu Suomalainen, and Pirjo Isohanni. Diagnostic value of serum biomarkers <scp>fgf21</scp> and <scp>gdf15</scp> compared to muscle sample in mitochondrial disease. Sep 2021. URL: https://doi.org/10.1002/jimd.12307, doi:10.1002/jimd.12307. This article has 77 citations and is from a peer-reviewed journal.

10. (NCT05162768 chunk 1):  Study to Evaluate Efficacy and Safety of Elamipretide in Subjects With Primary Mitochondrial Disease From Nuclear DNA Mutations (nPMD). Stealth BioTherapeutics Inc.. 2022. ClinicalTrials.gov Identifier: NCT05162768

11. (NCT02161848 chunk 1): Gitte Hedermann Pedersen. MRI Study - Chronic Progressive External Ophthalmoplegia. Rigshospitalet, Denmark. 2014. ClinicalTrials.gov Identifier: NCT02161848

12. (ramon2021therapyprospectsfor pages 1-2): Javier Ramón, Ferran Vila-Julià, David Molina-Granada, Miguel Molina-Berenguer, Maria Jesús Melià, Elena García-Arumí, Javier Torres-Torronteras, Yolanda Cámara, and Ramon Martí. Therapy prospects for mitochondrial dna maintenance disorders. International Journal of Molecular Sciences, 22:6447, Jun 2021. URL: https://doi.org/10.3390/ijms22126447, doi:10.3390/ijms22126447. This article has 37 citations.

13. (lim2021riskofcardiac pages 1-2): Albert Zishen Lim, Daniel M Jones, Matthew G D Bates, Andrew M Schaefer, John O'Sullivan, Catherine Feeney, Maria E Farrugia, John P Bourke, Doug M Turnbull, Gráinne S Gorman, Robert McFarland, and Yi Shiau Ng. Risk of cardiac manifestations in adult mitochondrial disease caused by nuclear genetic defects. Open Heart, 8:e001510, Apr 2021. URL: https://doi.org/10.1136/openhrt-2020-001510, doi:10.1136/openhrt-2020-001510. This article has 7 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Autosomal_Dominant_Progressive_External_Ophthalmoplegia-deep-research-falcon_artifacts/artifact-00.md)