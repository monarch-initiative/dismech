---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-01T06:39:53.376948'
end_time: '2026-08-01T06:46:45.348968'
duration_seconds: 411.97
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Adrenal Cortex Adenoma
  mondo_id: ''
  category: Neoplastic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 33
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Adrenal_Cortex_Adenoma-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Adrenal Cortex Adenoma
- **MONDO ID:**  (if available)
- **Category:** Neoplastic

## Research Objectives

Please provide a comprehensive research report on **Adrenal Cortex Adenoma** covering all of the
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
- **Disease Name:** Adrenal Cortex Adenoma
- **MONDO ID:**  (if available)
- **Category:** Neoplastic

## Research Objectives

Please provide a comprehensive research report on **Adrenal Cortex Adenoma** covering all of the
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


# Adrenocortical Adenoma: Comprehensive Disease-Characteristics Report

## Executive summary

An **adrenocortical adenoma (ACA)** is a benign, usually well-circumscribed neoplasm derived from steroidogenic cells of the adrenal cortex. Most are discovered incidentally and are nonfunctioning, but clinically important subsets autonomously produce cortisol or aldosterone. The central clinical tasks are therefore to establish (1) whether the lesion is radiologically benign, (2) whether it produces hormones, and (3) whether surgery would improve outcomes.

The 2023 European Society of Endocrinology (ESE) framework substantially simplified imaging follow-up: a homogeneous lesion measuring **≤10 Hounsfield units (HU) on unenhanced CT requires no further imaging follow-up, irrespective of size**. In patients without overt Cushing syndrome, post–1-mg dexamethasone cortisol **>50 nmol/L (>1.8 μg/dL)** is classified as mild autonomous cortisol secretion (MACS). Management of MACS is individualized according to age, general health, cortisol-related comorbidity, and patient preference. (park2023recentupdateson pages 5-6)

| domain | core finding | quantitative data/clinical threshold | suggested ontology terms |
|---|---|---|---|
| Disease identity | Adrenocortical adenoma (ACA) is a benign neoplasm of the adrenal cortex; in practice, many ACAs are detected as adrenal incidentalomas on imaging done for unrelated reasons. Distinguish disease-level entity (ACA) from imaging presentation (adrenal incidentaloma). (kim2024molecularandgenetics pages 4-7, yoshida2024diagnosisandmanagement pages 1-3, lee2017clinicalguidelinesfor pages 1-2) | Adrenal incidentaloma prevalence in imaging studies: 1–5%; older guideline summary: average 2% overall, rising to 4% in middle age and 10% in elderly. (yoshida2024diagnosisandmanagement pages 1-3, lee2017clinicalguidelinesfor pages 1-2) | MONDO: adrenocortical adenoma [suggested, ID not source-validated]; MeSH: Adrenocortical Adenoma [suggested]; UBERON: adrenal gland [suggested: UBERON:0002369]; NCIT: Adrenal Cortex Adenoma [suggested] |
| Functional subtypes | Functional ACAs include cortisol-producing adenoma (CPA; overt Cushing syndrome or mild autonomous cortisol secretion/MACS), aldosterone-producing adenoma (APA), and more rarely mixed steroid-secreting tumors; many lesions are nonfunctioning. (kim2024molecularandgenetics pages 4-7, yoshida2024diagnosisandmanagement pages 1-3, lee2017clinicalguidelinesfor pages 1-2) | Japanese survey proportions among incidentalomas: 75% benign, 25% functional; 10.5% cortisol-producing, 5.1% aldosterone-producing, 8.5% pheochromocytoma. Older guideline summary: ~80% nonfunctional benign adenomas; ~12% cortisol-secreting, 2.5% aldosterone-secreting, 7% pheochromocytoma, 8% carcinoma. (yoshida2024diagnosisandmanagement pages 1-3, lee2017clinicalguidelinesfor pages 1-2) | HPO: Hypercortisolism [suggested: HP:0001578]; Hyperaldosteronism [suggested: HP:0000848]; Hypertension [suggested: HP:0000822]; Hypokalemia [suggested: HP:0002900] |
| Cortisol genetics | CPA/MACS are strongly linked to cAMP/PKA pathway activation. PRKACA hotspot mutations are major drivers of cortisol-producing adenomas; GNAS is enriched in subclinical/MACS phenotypes; CTNNB1 also contributes in a subset. (kim2024molecularandgenetics pages 21-22, kim2024molecularandgenetics pages 9-11) | PRKACA mutations reported in 35–66% of CPA cases; GNAS mutations reported as most frequent in subclinical Cushing’s (~70% in the cited review summary); CTNNB1 accounts for ~23% of total CPA in the cited review summary. (kim2024molecularandgenetics pages 9-11) | HGNC/genes [all suggested]: PRKACA, GNAS, CTNNB1; GO: cAMP-dependent protein kinase activity [suggested]; GO: Wnt signaling pathway [suggested]; CL: adrenal cortex cell [suggested] |
| Aldosterone genetics | APA is driven by mutually exclusive somatic mutations in ion channel/pump genes causing membrane depolarization, calcium influx/signaling, aldosterone excess, and tumor growth in zona glomerulosa-lineage cells. Recurrently implicated genes include KCNJ5, CACNA1D, ATP1A1, ATP2B3, CACNA1H, and CLCN2; CTNNB1 activation occurs in a minority but β-catenin activation is broader. (kim2024molecularandgenetics pages 22-23, sousa2022colocalizationofwntβcatenin pages 18-23, leo2024molecularpathologyof pages 17-18) | KCNJ5 mutations account for ~40% of APAs and are especially associated with younger female patients; CTNNB1 mutations occur in ~5% of APAs, while β-catenin activation is present in the majority. Somatic CLCN2 variants were identified in 2/115 APAs (1.74%) in cited primary data referenced by the review set. (sousa2022colocalizationofwntβcatenin pages 18-23, leo2024molecularpathologyof pages 17-18) | HGNC/genes [all suggested]: KCNJ5, CACNA1D, ATP1A1, ATP2B3, CACNA1H, CLCN2, CTNNB1; GO: calcium ion transport [suggested]; GO: aldosterone biosynthetic process [suggested]; CL: zona glomerulosa cell [suggested] |
| Imaging | A homogeneous adrenal mass with low attenuation on non-contrast CT is strongly suggestive of benign adenoma. Indeterminate lesions require additional imaging rather than size-only management. (park2023recentupdateson pages 5-6, yoshida2024diagnosisandmanagement pages 1-3) | Benign criterion: homogeneous mass with ≤10 Hounsfield units (HU) on unenhanced CT, with no further follow-up required regardless of size per 2023 ESE update summary. Indeterminate: 11–20 HU; growth concerning on follow-up if >20% and at least ≥5 mm increase in maximum diameter. (park2023recentupdateson pages 5-6) | RadLex/non-ontology note: unenhanced adrenal CT [suggested]; UBERON: adrenal gland [suggested: UBERON:0002369]; NCIT: Computed Tomography of Abdomen [suggested] |
| Hormonal tests | Standard hormonal work-up aims to detect cortisol autonomy, primary aldosteronism, and pheochromocytoma when clinically indicated. (park2023recentupdateson pages 5-6, yoshida2024diagnosisandmanagement pages 1-3, lee2017clinicalguidelinesfor pages 1-2) | 1-mg overnight dexamethasone suppression: post-DST cortisol >50 nmol/L (>1.8 μg/dL) supports MACS; screening performance in one review summary: sensitivity 98.6%, specificity 90.6%. Plasma aldosterone-to-renin ratio: sensitivity 97%, specificity 80% for primary aldosteronism. Fractionated plasma-free metanephrines: sensitivity 95.7%, specificity 97.3% for pheochromocytoma. (park2023recentupdateson pages 5-6, yoshida2024diagnosisandmanagement pages 1-3) | LOINC-related tests [all suggested]: serum cortisol after dexamethasone; aldosterone/renin ratio; plasma free metanephrines; HPO: Elevated serum cortisol [suggested], Elevated aldosterone level [suggested] |
| Treatment | Management depends on function and malignancy risk. Benign hormone-secreting tumors are typically treated with adrenalectomy; benign-appearing nonfunctioning lesions may be observed. Multidisciplinary review and experienced/high-volume surgeons are recommended. (park2023recentupdateson pages 5-6, yoshida2024diagnosisandmanagement pages 1-3) | Minimally invasive adrenalectomy preferred for benign hormone-secreting tumors and suspicious masses ≤6 cm without invasion; recommended surgeon volume ≥12 adrenalectomies/year; perioperative glucocorticoid coverage advised for MACS patients undergoing surgery. (park2023recentupdateson pages 5-6) | NCIT [all suggested]: Adrenalectomy, Laparoscopic Adrenalectomy, Glucocorticoid Replacement Therapy, Active Surveillance |
| Prognosis | ACA prognosis is generally favorable because lesions are benign, but morbidity depends on hormonal excess and cardiovascular/metabolic complications rather than local tumor behavior. Functional disease requires correct diagnosis and perioperative management to avoid adrenal insufficiency or cardiovascular events. (yoshida2024diagnosisandmanagement pages 1-3) | No disease-specific ACA survival statistic was established in gathered evidence; prognostic concern is driven by cortisol or aldosterone excess comorbidities and by radiologic suspicion for non-adenoma pathology. (park2023recentupdateson pages 5-6, yoshida2024diagnosisandmanagement pages 1-3) | HPO: Cardiovascular abnormality [suggested], Adrenal insufficiency [suggested: HP:0000846]; NCIT: Cardiovascular Complication [suggested] |


*Table: This table condenses the key disease-knowledge elements for adrenocortical adenoma, including subtype-defining biology, current diagnostic thresholds, and management points. Ontology entries are explicitly marked as suggested when they were not source-validated in the gathered evidence.*

## 1. Disease information

### Definition and scope

ACA is a **benign neoplastic proliferation of adrenal cortical cells**. “Adrenal incidentaloma” is not synonymous with ACA: it is an imaging presentation—an unsuspected adrenal mass found during imaging for another reason—and includes adenoma, pheochromocytoma, myelolipoma, metastasis, adrenocortical carcinoma (ACC), cyst, hemorrhage, and other lesions. Approximately 75–80% of incidentally detected adrenal masses in major clinical series are benign/nonfunctioning adenomas, although the proportions vary with referral setting. (yoshida2024diagnosisandmanagement pages 1-3, lee2017clinicalguidelinesfor pages 1-2)

Functional classifications are:

* **Nonfunctioning adrenocortical adenoma (NFA/NFAT)**.
* **Cortisol-producing adenoma (CPA)** causing overt ACTH-independent Cushing syndrome or MACS.
* **Aldosterone-producing adenoma (APA; Conn adenoma)** causing unilateral primary aldosteronism.
* Rare androgen-, estrogen-, or mixed steroid-producing adenomas. Marked sex-steroid excess should increase concern for ACC rather than routine ACA.

### Identifiers and synonyms

* **Preferred name:** adrenocortical adenoma.
* **Synonyms:** adrenal cortical adenoma, adrenal cortex adenoma, cortical adrenal adenoma; functional forms include cortisol-producing adenoma and aldosterone-producing adenoma/Conn adenoma.
* **ICD-10-CM:** D35.0, benign neoplasm of adrenal gland; this code does not distinguish cortex from medulla or functional subtype.
* **ICD-11:** falls under benign neoplasms of endocrine glands/adrenal gland; the precise national-extension code should be validated against the implementation being used.
* **MeSH:** “Adrenocortical Adenoma”/the adrenal-cortex-neoplasm hierarchy should be mapped against the current MeSH release.
* **MONDO, OMIM, and Orphanet:** a stable disease-specific identifier was not established from the retrieved evidence and should not be inferred. ACA is usually sporadic and common enough that it is not conventionally treated as a single Mendelian or rare-disease entity. OMIM entries are more appropriate for predisposing syndromes such as Carney complex, MEN1, familial adenomatous polyposis, and familial hyperaldosteronism.
* **Suggested NCIt concept:** Adrenal Cortex Adenoma; validate the current NCIt code during ingestion.

This report synthesizes **aggregated disease-level literature and guidelines**, not individual EHR records. Some cited primary studies use patient-level clinical, imaging, pathology, or sequencing data.

## 2. Etiology

### Causal factors

Most ACAs are sporadic clonal neoplasms. Their best-supported proximal causes are acquired, subtype-specific somatic alterations:

1. **CPA:** constitutive cAMP–protein kinase A signaling, especially activating **PRKACA** variants; **GNAS** and **CTNNB1** alterations occur in additional subsets.
2. **APA:** mutually exclusive variants affecting potassium channels, calcium channels, or ATPases—principally **KCNJ5, CACNA1D, ATP1A1, ATP2B3**, and less often **CACNA1H** or **CLCN2**—produce membrane depolarization, calcium signaling, CYP11B2 induction, and aldosterone synthesis. (kim2024molecularandgenetics pages 9-11, leo2024molecularpathologyof pages 17-18)
3. **Nonfunctioning ACA:** molecularly heterogeneous; Wnt/β-catenin activation is found in a subset, but no single alteration defines all lesions.

### Genetic risk and predisposition

Routine ACA is not inherited. Germline testing becomes relevant with bilateral/multifocal disease, childhood or unusually young onset, syndromic features, or a strong family history. Relevant predisposition pathways include **PRKAR1A** in Carney complex/primary pigmented nodular adrenocortical disease, **MEN1**, **APC** in familial adenomatous polyposis, and familial-primary-aldosteronism genes. Germline PRKAR1A loss constitutively activates PKA; it accounts for more than 67% of Carney-complex index cases in the reviewed evidence, but this relates principally to nodular adrenal disease rather than ordinary unilateral ACA. (bonnetserrano2018geneticsoftumors pages 4-6)

### Demographic and environmental risk

Detection rises strongly with age and imaging use. Older studies report an average incidentaloma prevalence near 2%, approximately 4% in middle age and up to 10% in elderly populations; contemporary imaging-study estimates are 1–5%. No consistent sex difference was identified in the older guideline synthesis, although genotype-specific differences occur—**KCNJ5-mutant APA is enriched in younger women**. (yoshida2024diagnosisandmanagement pages 1-3, lee2017clinicalguidelinesfor pages 1-2, leo2024molecularpathologyof pages 17-18)

No toxin, infection, diet, smoking exposure, occupational exposure, or lifestyle factor has been established as a direct cause of ordinary ACA. Obesity, hypertension, and diabetes commonly coexist, but reverse causation is important because subtle cortisol secretion can itself produce these conditions.

### Protective factors and gene–environment interactions

No validated genetic or environmental factor prevents ACA. General cardiovascular risk reduction may lessen morbidity from MACS or primary aldosteronism but is not proven to prevent tumor formation. A notable physiologic interaction is the occurrence of **CTNNB1-mutant APA with GNAQ/GNA11 alterations around puberty, pregnancy, or menopause**, suggesting that hormonal environments can expose or amplify a genetically primed aldosterone-producing phenotype. (kim2024molecularandgenetics pages 22-23, sousa2022colocalizationofwntβcatenin pages 18-23)

## 3. Phenotypes

Nonfunctioning lesions are usually asymptomatic and stable; symptoms arise predominantly from hormone excess or, rarely, mass effect.

### Cortisol excess

* **MACS:** often lacks classic Cushing stigmata but is associated with hypertension, type 2 diabetes, dyslipidemia, obesity, cardiovascular risk, osteoporosis/osteopenia, and fractures. Severity is variable and usually chronic/insidious.
* **Overt Cushing syndrome:** proximal muscle weakness, easy bruising, facial plethora, wide violaceous striae, central adiposity, hypertension, diabetes, osteoporosis, infection susceptibility, and neuropsychiatric symptoms.
* **Suggested HPO terms:** Hypercortisolism (HP:0001578), Hypertension (HP:0000822), Type II diabetes mellitus (HP:0005978), Osteoporosis (HP:0000939), Proximal muscle weakness (HP:0003701), Easy bruising (HP:0000978), Abdominal obesity (HP:0012743), Depression (HP:0000716).

### Aldosterone excess

APA produces sustained or episodically recognized hypertension, suppressed renin, elevated aldosterone-to-renin ratio, and sometimes hypokalemia, metabolic alkalosis, muscle weakness, cramps, polyuria, or arrhythmia. Normokalemia does not exclude primary aldosteronism. Cardiovascular and renal injury is disproportionate to blood-pressure elevation because aldosterone has direct tissue effects.

* **Suggested HPO:** Hyperaldosteronism (HP:0000848), Hypertension (HP:0000822), Hypokalemia (HP:0002900), Metabolic alkalosis (HP:0200114), Muscle weakness (HP:0001324), Cardiac arrhythmia (HP:0011675), Polyuria (HP:0000103).

### Mass effects and mixed secretion

Large lesions can cause nonspecific flank or abdominal discomfort, although such symptoms are unusual in typical small ACA. Rare mixed steroid secretion can produce overlapping Cushing, mineralocorticoid, or sex-steroid phenotypes. Rapid virilization or feminization is a red flag for ACC.

### Quality of life

Quality-of-life impairment is mainly endocrine-mediated: fatigue, weakness, mood symptoms, metabolic disease, fractures, polypharmacy, and cardiovascular morbidity. Disease-specific EQ-5D or SF-36 reference values were not established in the retrieved evidence. Surgical decisions in MACS should therefore consider patient-reported burden as well as biochemical status.

## 4. Genetic and molecular information

### Principal somatic drivers

| Subtype | Gene/pathway | Functional consequence |
|---|---|---|
| CPA | **PRKACA**, usually activating hotspot changes around p.Leu206 | Impaired regulatory-subunit binding; constitutive catalytic PKA activity and CREB signaling |
| CPA/MACS | **GNAS** | Activating Gαs signaling, increased cAMP and PKA activity |
| CPA/NFA/APA subset | **CTNNB1** | Stabilized β-catenin and canonical Wnt transcription |
| APA | **KCNJ5** | Loss of potassium-channel selectivity, sodium entry, depolarization, calcium influx |
| APA | **CACNA1D/CACNA1H** | Increased voltage-gated calcium entry |
| APA | **ATP1A1/ATP2B3** | Abnormal ion gradients/depolarization and calcium signaling |
| APA | **CLCN2** | Altered chloride conductance and depolarization |

PRKACA alterations are reported in approximately **35–66% of CPA** in the 2024 synthesis. The same review reported GNAS enrichment in subclinical cortisol secretion and estimated that CTNNB1 contributes to roughly 23% of CPA, but exact frequencies vary substantially with phenotype definition and cohort selection. These figures should not be treated as universal population prevalences. (kim2024molecularandgenetics pages 9-11)

KCNJ5 is the most frequent APA driver, accounting for approximately **40%** overall and showing enrichment in younger female patients. In CYP11B2-guided sequencing, known aldosterone-driver alterations can explain about 90% of APA; rare somatic **CLCN2** variants were found in 2/115 tumors (1.74%). (leo2024molecularpathologyof pages 17-18)

### Variant interpretation

These tumor variants are ordinarily **somatic**, not germline, and should be reported using a somatic-oncology framework rather than automatically labeled “pathogenic germline” under ACMG/AMP constitutional criteria. Population allele frequency is generally not meaningful for tumor-only variants; paired normal tissue is needed to establish origin. Routine ACA care does not require tumor sequencing because genotype rarely changes present standard treatment.

### Modifiers, epigenetics, and chromosomal change

No clinically validated modifier gene is used to predict ACA severity. Pregnancy-associated DNA-methylation changes and additional candidate alterations have been reported, but they remain investigational. Broad copy-number instability, TP53 disruption, IGF2 overexpression, and extensive methylomic derangement favor ACC rather than ordinary ACA. (kim2024molecularandgenetics pages 22-23, kim2024molecularandgenetics pages 21-22)

## 5. Environmental information

There is no established infectious cause and no evidence for transmissibility. Radiation, pollutants, diet, smoking, and alcohol have not been proven causal for sporadic ACA. Exogenous glucocorticoids can mimic Cushing physiology and interfere with testing but do not constitute ACA. Licorice and medications affecting renin or aldosterone can confound primary-aldosteronism assessment. Prevention should consequently focus on avoiding diagnostic interference and controlling endocrine complications rather than avoiding a known carcinogen.

## 6. Mechanism and pathophysiology

### CPA causal chain

Somatic **PRKACA/GNAS** activation → ACTH-independent cAMP/PKA activity → CREB-dependent transcription and induction of steroidogenic regulators/enzymes, including STAR and CYP11B1 → autonomous cortisol synthesis → suppression of pituitary ACTH and contralateral adrenal cortex → chronic glucocorticoid effects on liver, muscle, fat, bone, immune, cardiovascular, and nervous systems. PRKACA hotspot variants disrupt normal catalytic–regulatory PKA interaction and permit cAMP-independent signaling. (kim2024molecularandgenetics pages 9-11)

Suggested terms: **GO:0019933 cAMP-mediated signaling; GO:0006468 protein phosphorylation; GO:0008202 steroid metabolic process; GO:0006694 steroid biosynthetic process; GO:0008210 estrogen metabolic process** where applicable. Relevant cells are steroidogenic adrenal cortical cells, especially zona fasciculata-like cells; suggested **CL: adrenal cortex cell** and **CL: steroid hormone-secreting cell** mappings should be validated.

### APA causal chain

Ion-channel/pump mutation → zona-glomerulosa-cell depolarization → opening of voltage-gated calcium channels and/or increased intracellular Ca²⁺ → calcium-dependent transcription → **CYP11B2** expression and aldosterone production → renal sodium retention, potassium and hydrogen-ion loss, volume expansion and renin suppression → hypertension, hypokalemia, alkalosis, and aldosterone-mediated cardiovascular/renal remodeling. The same signaling supports proliferation and adenoma formation. (leo2024molecularpathologyof pages 17-18)

Suggested terms: **GO:0006816 calcium ion transport; GO:0030007 cellular potassium-ion homeostasis; GO:0032342 aldosterone biosynthetic process; GO:0071372 cellular response to mineralocorticoid stimulus**. Cell: zona glomerulosa steroidogenic cell.

### Wnt/β-catenin and microenvironment

CTNNB1 mutation stabilizes β-catenin, but molecular activation is more common than mutation alone. CTNNB1 variants occur in about 5% of APA while β-catenin activation is found in most aldosterone-producing structures. In a primary multiplex-imaging study, CYP11B2-positive regions showed activated β-catenin, high MC2R in some heterogeneous tumors, dense vasculature, and mast cells adjacent to aldosterone-producing cells. This supports a model in which lineage identity, ACTH responsiveness, vascular supply, and mast-cell paracrine signals cooperate with tumor genotype. (sousa2022colocalizationofwntβcatenin pages 18-23)

### Omics and advanced technologies

Current applications include CYP11B2-guided sequencing, whole-exome sequencing, DNA methylation profiling, transcriptomics, steroid metabolomics, multiplex immunofluorescence, spatial proteomics, and machine-learning analysis of steroid profiles or CT. Steroid metabolomics by tandem mass spectrometry is promising for distinguishing benign from malignant adrenal disease but is not universally available. Spatial and single-cell methods are research tools rather than validated ACA diagnostics. (kim2024molecularandgenetics pages 22-23, park2023recentupdateson pages 5-6)

## 7. Anatomical structures affected

* **Primary organ:** adrenal gland—**UBERON:0002369** (suggested mapping).
* **Primary tissue:** adrenal cortex, particularly zona fasciculata-like cells in CPA and zona glomerulosa-lineage cells in APA.
* **Laterality:** commonly unilateral; bilateral or multinodular disease suggests hyperplasia or hereditary/syndromic disease and requires a different framework.
* **Secondary systems:** cardiovascular and renal systems in aldosterone excess; metabolic, musculoskeletal, immune, psychiatric, reproductive, and cardiovascular systems in cortisol excess.
* **Subcellular compartments:** plasma membrane ion channels/pumps in APA; cytosolic/nuclear β-catenin; cytosolic PKA complex and nuclear CREB; mitochondrial and smooth-ER steroidogenic machinery.
* **Suggested GO cellular components:** plasma membrane (GO:0005886), voltage-gated calcium-channel complex (GO:0005891), nucleus (GO:0005634), mitochondrion (GO:0005739), smooth endoplasmic reticulum (GO:0005790).

## 8. Temporal development

ACA is generally an **adult-onset, insidious, slowly evolving** lesion, with prevalence increasing markedly with age. Pediatric ACA is uncommon and should prompt careful malignancy and germline-predisposition assessment. There is no AJCC staging system for benign ACA.

A homogeneous ≤10-HU lesion has a sufficiently benign natural history that the 2023 ESE approach recommends no repeat imaging. For indeterminate lesions under surveillance, growth **>20% plus at least 5 mm** in maximum diameter is considered significant and prompts reconsideration. Hormonal evolution can occur, but repeated endocrine testing is generally symptom/comorbidity driven after an initially normal evaluation rather than performed indefinitely in every patient. (park2023recentupdateson pages 5-6)

Functional disease generally persists until the source is removed or medically controlled. Post-adrenalectomy hypothalamic–pituitary–adrenal recovery can take months; this is a clinically important treatment-induced phase rather than tumor recurrence.

## 9. Inheritance and population

Imaging-study prevalence is approximately **1–5%**, rising with age; historical estimates reach approximately 10% in older populations. A Japanese nationwide survey summarized in a 2024 review found 75% benign lesions and 25% functional lesions, including 10.5% cortisol-producing and 5.1% aldosterone-producing lesions; pheochromocytoma accounted for 8.5% but is medullary and not an ACA. (yoshida2024diagnosisandmanagement pages 1-3)

Incidence per 100,000 person-years is difficult to define because detection depends heavily on imaging. Ordinary unilateral ACA is **sporadic, multifactorial, and not assigned Mendelian inheritance, penetrance, carrier frequency, anticipation, consanguinity, or founder-effect parameters**. Such concepts apply only to the uncommon predisposing syndromes. KCNJ5-mutant APA has demographic enrichment in younger women, whereas mutation frequencies vary by ancestry; population-specific estimates should not be generalized without ancestry-matched cohorts. (leo2024molecularpathologyof pages 17-18, sousa2022colocalizationofwntβcatenin pages 23-25)

## 10. Diagnostics

### Imaging

1. **Unenhanced CT first:** homogeneous, lipid-rich lesions measuring ≤10 HU are benign by current guideline criteria and need no further imaging follow-up, regardless of size.
2. **Indeterminate lesions:** 11–20 HU or heterogeneous appearance warrants dedicated adrenal imaging—contrast washout CT, chemical-shift MRI, or selected PET—preferably after multidisciplinary review.
3. Features concerning for malignancy include heterogeneity, irregular margins, necrosis/hemorrhage, local invasion, metastases, and significant interval growth. Size contributes to risk but should not be the only determinant. (park2023recentupdateson pages 5-6)

### Hormonal evaluation

* **Cortisol:** 1-mg overnight dexamethasone-suppression test. Post-DST cortisol >50 nmol/L (>1.8 μg/dL) in a patient without overt Cushing signs supports MACS; confirm ACTH independence and consider confounders. The 2024 review reported sensitivity 98.6% and specificity 90.6% at this threshold. (park2023recentupdateson pages 5-6, yoshida2024diagnosisandmanagement pages 1-3)
* **Primary aldosteronism:** plasma aldosterone-to-renin ratio in patients with hypertension or unexplained hypokalemia, followed by confirmatory testing and subtype evaluation where required. Reported screening performance was 97% sensitivity and 80% specificity. (yoshida2024diagnosisandmanagement pages 1-3)
* **Pheochromocytoma exclusion:** plasma-free or urinary fractionated metanephrines when imaging is not unequivocally typical of benign adenoma or symptoms warrant testing. Reported plasma-free-metanephrine performance was 95.7% sensitivity and 97.3% specificity. (yoshida2024diagnosisandmanagement pages 1-3)
* **Sex steroids/steroid precursors:** test if virilization, feminization, or suspected ACC is present.

### Localization and pathology

In confirmed primary aldosteronism, CT alone cannot reliably identify the secreting side because nonfunctioning nodules become common with age. **Adrenal-vein sampling** is usually required before surgery unless a narrowly defined young patient has a compelling unilateral phenotype.

ACA is typically circumscribed and yellow owing to intracellular lipid. Histology shows bland cortical cells, low mitotic activity, absence of atypical mitoses, and no destructive capsular or vascular invasion. Immunohistochemical support for cortical origin includes SF-1, inhibin-α, Melan-A, and calretinin; CYP11B2 identifies aldosterone-producing tissue. The Weiss system and related algorithms distinguish adenoma from ACC but require expert endocrine pathology and are not screening tests.

### Differential diagnosis

ACC, pheochromocytoma, metastasis, myelolipoma, adrenal cyst/hemorrhage, ganglioneuroma, oncocytic adrenocortical neoplasm, adrenal hyperplasia, and renal or retroperitoneal masses must be considered. Percutaneous biopsy does **not** determine cortical adenoma versus ACC reliably and should never precede biochemical exclusion of pheochromocytoma.

### Genetic and omics testing

WES, WGS, chromosomal microarray, FISH, karyotyping, mitochondrial testing, and repeat-expansion testing are not routine. A focused germline panel is appropriate only when the presentation suggests a syndrome; potential genes include PRKAR1A, MEN1, APC, and familial-hyperaldosteronism genes selected according to phenotype. Tumor sequencing and steroid metabolomics remain specialist/research applications.

### Screening

No population-wide screening is recommended. Targeted biochemical screening for primary aldosteronism is appropriate in guideline-defined hypertensive groups. Cascade testing applies only after a pathogenic germline predisposition is identified.

## 11. Outcome and prognosis

A completely characterized benign ACA has an excellent tumor-specific prognosis: it does not metastasize, and disease-specific mortality or five-year cancer survival statistics are not meaningful. Published poor-survival statistics for ACC must not be applied to ACA.

Morbidity is instead driven by hormone exposure. MACS can contribute to diabetes, hypertension, cardiovascular disease, and skeletal fragility; APA increases cardiovascular and renal risk beyond that expected from blood pressure alone. Correct diagnosis is important because inadequate perioperative management can lead to cardiovascular events or adrenal insufficiency. (yoshida2024diagnosisandmanagement pages 1-3)

After unilateral adrenalectomy, biochemical cortisol or aldosterone excess is often corrected, although hypertension, diabetes, or osteoporosis may not fully reverse because of disease duration, age, and coexisting essential disease. Persistent hypertension after APA surgery does not necessarily mean persistent aldosterone excess. Key prognostic factors include duration/severity of hormonal excess, age, renal function, cardiometabolic comorbidity, contralateral adrenal suppression, and accurate unilateral localization.

## 12. Treatment

### Nonfunctioning benign ACA

No tumor-directed drug is indicated. A homogeneous ≤10-HU lesion receives reassurance and clinical care for unrelated comorbidities, without serial imaging under the 2023 ESE framework. Indeterminate lesions may undergo one-time additional imaging or interval surveillance. Suggested NCIt interventions: **Active Surveillance; Computed Tomography; Magnetic Resonance Imaging**. (park2023recentupdateson pages 5-6)

### Functional ACA

* **Adrenalectomy:** definitive treatment for unilateral APA and overt cortisol-producing adenoma; considered individually for MACS when relevant comorbidities are present. Minimally invasive adrenalectomy is preferred for benign hormone-secreting lesions and selected suspicious masses ≤6 cm without invasion. High-volume surgery—defined in the reviewed ESE summary as at least 12 adrenalectomies annually—is favored. Suggested NCIt: **Adrenalectomy; Laparoscopic Adrenalectomy**. (park2023recentupdateson pages 5-6)
* **Perioperative cortisol care:** patients with cortisol autonomy require stress-dose glucocorticoids followed by tapering based on hypothalamic–pituitary–adrenal recovery. Suggested NCIt: **Glucocorticoid Replacement Therapy**.
* **APA medical therapy:** mineralocorticoid-receptor antagonists—spironolactone or eplerenone—are used when surgery is not chosen, while awaiting localization/surgery, or for bilateral disease. Suggested NCIt: **Spironolactone Therapy; Eplerenone Therapy**. Hyperkalemia, renal dysfunction, gynecomastia, menstrual disturbance, and hypotension require monitoring.
* **Cortisol-lowering drugs:** metyrapone, osilodrostat, ketoconazole/levoketoconazole, or mifepristone can control selected severe hypercortisolism but are not routine definitive therapy for a resectable benign adenoma.

There is no approved gene, cell, RNA, immune, or genotype-guided therapy for ACA. Pharmacogenomic selection is not standard.

### Current research applications

ClinicalTrials.gov searches identified observational work on adrenal-disease cohorts (NCT03474237), steroid-panel diagnosis (NCT04948970), detection of MACS (NCT06344143), spatial proteomics of APA (NCT05927961), and bone effects of MACS (NCT04343560). Early imaging studies include [18F]CETO (NCT05361083). These are diagnostic or mechanistic studies, not evidence of an approved molecular ACA treatment.

## 13. Prevention

There is no proven primary prevention, vaccine, prophylactic drug, or population screening program for ACA. Secondary prevention consists of correct biochemical characterization of incidentally detected lesions and targeted primary-aldosteronism screening in high-risk hypertension. Tertiary prevention includes treatment of cortisol or aldosterone excess, blood-pressure and diabetes control, potassium normalization, cardiovascular-risk management, bone-density assessment, and perioperative prevention of adrenal crisis. Genetic counseling is reserved for young, bilateral, familial, or syndromic cases.

## 14. Other species and natural disease

Naturally occurring adrenocortical tumors occur in dogs and cats and may produce cortisol, aldosterone, progesterone, sex steroids, or combinations. A documented 14-year-old spayed female cat with a right adrenocortical tumor had hyperaldosteronism, hyperprogesteronism, evidence of cortisol excess, hypertension, and hypokalemia; unilateral adrenalectomy resolved the endocrine abnormalities. This supports conserved steroidogenic biology but represents case-level rather than population evidence.

Suggested taxonomy: **Homo sapiens—NCBI Taxon 9606; Mus musculus—10090; Rattus norvegicus—10116; Canis lupus familiaris—9615; Felis catus—9685**. Breed-specific VBO associations and robust veterinary incidence estimates were not established. These tumors are noninfectious and have no zoonotic potential.

## 15. Model organisms and experimental systems

### Mouse models

Genetically engineered mice with adrenal β-catenin activation develop cortical hyperplasia and, depending on model duration and cooperating events, macroscopic tumors. These models demonstrate causality for Wnt signaling but often fail to reproduce the full spectrum, latency, hormone phenotype, and benign-to-malignant evolution of human disease. PKA-pathway models interrogate PRKAR1A/PRKACA signaling and cortisol-producing disease. Conditional, cortex-specific systems are preferable because ubiquitous activation may be embryonic-lethal or cause nonadrenal phenotypes.

### Cellular systems

Human NCI-H295R and mouse Y1 adrenocortical cells are widely used to study steroidogenesis and Wnt/PKA signaling, but they are carcinoma-derived or transformed and therefore imperfect ACA models. In vitro Wnt/TCF inhibition reduces steroidogenesis and proliferation and increases apoptosis in adrenocortical tumor cells, demonstrating pathway dependence but not clinical efficacy in benign ACA.

### Organoids, spheroids, xenografts, and spatial models

Three-dimensional cultures and organoid-like systems improve tissue architecture and microenvironment modeling, while multiplex imaging and spatial proteomics can resolve CYP11B2-positive regions, vasculature, mast cells, and intratumoral heterogeneity. Most mature repositories and xenograft resources concern ACC rather than ACA. Patient-derived benign adenoma organoids, faithful APA models, and models integrating genotype with long-term endocrine phenotype remain major unmet needs.

## Recent developments and authoritative interpretation

The major 2023–2024 advances are: (1) removal of the historical size restriction for homogeneous ≤10-HU lesions; (2) adoption of a single >1.8-μg/dL post-DST threshold for MACS; (3) greater emphasis on comorbidity-based shared decisions rather than cortisol strata alone; (4) multidisciplinary, high-volume adrenal surgery; and (5) increasing use of steroid metabolomics, CYP11B2-guided sequencing, spatial proteomics, and machine learning. (park2023recentupdateson pages 5-6, kim2024molecularandgenetics pages 22-23)

The clearest guideline statement is: **“a homogeneous adrenal mass with ≤10 Hounsfield units on non-contrast computed tomography requires no further follow-up, irrespective of its size.”** The same 2023 review states that post-DST cortisol above 50 nmol/L (>1.8 μg/dL) should be regarded as MACS in patients without overt Cushing syndrome. (park2023recentupdateson pages 5-6)

Expert interpretation is that ACA should no longer be treated as a single biologic entity. Cortisol-producing, aldosterone-producing, and nonfunctioning adenomas have distinct initiating pathways, and an imaging diagnosis must remain separate from endocrine phenotype. Molecular profiling is rapidly clarifying pathogenesis, but—outside suspected hereditary disease—it has not yet displaced imaging, biochemical testing, adrenal-vein sampling, expert pathology, and individualized surgical judgment.

## Key sources and dates

1. Park SS, Kim JH. **Recent Updates on the Management of Adrenal Incidentalomas.** *Endocrinology and Metabolism*. Published August 2023. DOI/URL: https://doi.org/10.3803/enm.2023.1779. (park2023recentupdateson pages 5-6)
2. Yoshida Y, et al. **Diagnosis and management of adrenal incidentaloma: use of clinical judgment and evidence in dialog with the patient.** *Surgery Today*. Published December 2024. DOI/URL: https://doi.org/10.1007/s00595-023-02781-y. (yoshida2024diagnosisandmanagement pages 1-3)
3. Kim S, Chaudhary PK, Kim S. **Molecular and Genetics Perspectives on Primary Adrenocortical Hyperfunction Disorders.** *International Journal of Molecular Sciences*. Published October 2024. DOI/URL: https://doi.org/10.3390/ijms252111341. (kim2024molecularandgenetics pages 22-23, kim2024molecularandgenetics pages 9-11)
4. De Leo A, et al. **Molecular pathology of endocrine gland tumors: genetic alterations and clinicopathologic relevance.** *Virchows Archiv*. Published in volume 484 (2024); DOI registered December 2023. URL: https://doi.org/10.1007/s00428-023-03713-4. (leo2024molecularpathologyof pages 17-18)
5. De Sousa K, et al. **Colocalization of Wnt/β-Catenin and ACTH Signaling Pathways and Paracrine Regulation in Aldosterone-producing Adenoma.** *Journal of Clinical Endocrinology & Metabolism*. 2022. DOI/URL: https://doi.org/10.1210/clinem/dgab707. (sousa2022colocalizationofwntβcatenin pages 18-23)
6. Bonnet-Serrano F, Bertherat J. **Genetics of tumors of the adrenal cortex.** *Endocrine-Related Cancer*. Published March 2018. DOI/URL: https://doi.org/10.1530/ERC-17-0361. (bonnetserrano2018geneticsoftumors pages 4-6)
7. Lee JM, et al. **Clinical Guidelines for the Management of Adrenal Incidentaloma.** *Endocrinology and Metabolism*. Published June 2017. DOI/URL: https://doi.org/10.3803/enm.2017.32.2.200. (lee2017clinicalguidelinesfor pages 1-2)

PMIDs were not present in the retrieved source metadata and are therefore not invented here; DOI URLs provide stable primary identifiers. Ontology mappings marked “suggested” should be validated against the current releases of MONDO, HPO, GO, CL, UBERON, NCIt, LOINC, and MeSH before production ingestion.

References

1. (park2023recentupdateson pages 5-6): Seung Shin Park and Jung Hee Kim. Recent updates on the management of adrenal incidentalomas. Endocrinology and Metabolism, 38:373-380, Aug 2023. URL: https://doi.org/10.3803/enm.2023.1779, doi:10.3803/enm.2023.1779. This article has 43 citations and is from a peer-reviewed journal.

2. (kim2024molecularandgenetics pages 4-7): Sanggu Kim, Preeti Kumari Chaudhary, and Soochong Kim. Molecular and genetics perspectives on primary adrenocortical hyperfunction disorders. International Journal of Molecular Sciences, 25:11341, Oct 2024. URL: https://doi.org/10.3390/ijms252111341, doi:10.3390/ijms252111341. This article has 6 citations.

3. (yoshida2024diagnosisandmanagement pages 1-3): Yusaku Yoshida, Kiyomi Horiuchi, Michio Otsuki, and Takahiro Okamoto. Diagnosis and management of adrenal incidentaloma: use of clinical judgment and evidence in dialog with the patient. Surgery Today, 54:1417-1427, Dec 2024. URL: https://doi.org/10.1007/s00595-023-02781-y, doi:10.1007/s00595-023-02781-y. This article has 13 citations and is from a peer-reviewed journal.

4. (lee2017clinicalguidelinesfor pages 1-2): Jung-Min Lee, Mee Kyoung Kim, Seung-Hyun Ko, Jung-Min Koh, Bo-Yeon Kim, Sang Wan Kim, Soo-Kyung Kim, Hae Jin Kim, Ohk-Hyun Ryu, Juri Park, Jung Soo Lim, Seong Yeon Kim, Young Kee Shong, and Soon Jib Yoo. Clinical guidelines for the management of adrenal incidentaloma. Endocrinology and Metabolism, 32:200-218, Jun 2017. URL: https://doi.org/10.3803/enm.2017.32.2.200, doi:10.3803/enm.2017.32.2.200. This article has 189 citations and is from a peer-reviewed journal.

5. (kim2024molecularandgenetics pages 21-22): Sanggu Kim, Preeti Kumari Chaudhary, and Soochong Kim. Molecular and genetics perspectives on primary adrenocortical hyperfunction disorders. International Journal of Molecular Sciences, 25:11341, Oct 2024. URL: https://doi.org/10.3390/ijms252111341, doi:10.3390/ijms252111341. This article has 6 citations.

6. (kim2024molecularandgenetics pages 9-11): Sanggu Kim, Preeti Kumari Chaudhary, and Soochong Kim. Molecular and genetics perspectives on primary adrenocortical hyperfunction disorders. International Journal of Molecular Sciences, 25:11341, Oct 2024. URL: https://doi.org/10.3390/ijms252111341, doi:10.3390/ijms252111341. This article has 6 citations.

7. (kim2024molecularandgenetics pages 22-23): Sanggu Kim, Preeti Kumari Chaudhary, and Soochong Kim. Molecular and genetics perspectives on primary adrenocortical hyperfunction disorders. International Journal of Molecular Sciences, 25:11341, Oct 2024. URL: https://doi.org/10.3390/ijms252111341, doi:10.3390/ijms252111341. This article has 6 citations.

8. (sousa2022colocalizationofwntβcatenin pages 18-23): Kelly De Sousa, Alaa B Abdellatif, Isabelle Giscos-Douriez, Tchao Meatchi, Laurence Amar, Fabio L Fernandes-Rosa, Sheerazed Boulkroun, and Maria-Christina Zennaro. Colocalization of wnt/β-catenin and acth signaling pathways and paracrine regulation in aldosterone-producing adenoma. The Journal of Clinical Endocrinology &amp; Metabolism, 107:419-434, Sep 2022. URL: https://doi.org/10.1210/clinem/dgab707, doi:10.1210/clinem/dgab707. This article has 19 citations.

9. (leo2024molecularpathologyof pages 17-18): Antonio De Leo, Martina Ruscelli, Thais Maloberti, Sara Coluccelli, Andrea Repaci, Dario de Biase, and Giovanni Tallini. Molecular pathology of endocrine gland tumors: genetic alterations and clinicopathologic relevance. Virchows Archiv, 484:289-319, Dec 2024. URL: https://doi.org/10.1007/s00428-023-03713-4, doi:10.1007/s00428-023-03713-4. This article has 8 citations and is from a peer-reviewed journal.

10. (bonnetserrano2018geneticsoftumors pages 4-6): Fidéline Bonnet-Serrano and Jérôme Bertherat. Genetics of tumors of the adrenal cortex. Endocrine-Related Cancer, 25:R131-R152, Mar 2018. URL: https://doi.org/10.1530/erc-17-0361, doi:10.1530/erc-17-0361. This article has 81 citations and is from a domain leading peer-reviewed journal.

11. (sousa2022colocalizationofwntβcatenin pages 23-25): Kelly De Sousa, Alaa B Abdellatif, Isabelle Giscos-Douriez, Tchao Meatchi, Laurence Amar, Fabio L Fernandes-Rosa, Sheerazed Boulkroun, and Maria-Christina Zennaro. Colocalization of wnt/β-catenin and acth signaling pathways and paracrine regulation in aldosterone-producing adenoma. The Journal of Clinical Endocrinology &amp; Metabolism, 107:419-434, Sep 2022. URL: https://doi.org/10.1210/clinem/dgab707, doi:10.1210/clinem/dgab707. This article has 19 citations.

## Artifacts

- [Edison artifact artifact-00](Adrenal_Cortex_Adenoma-deep-research-falcon_artifacts/artifact-00.md)