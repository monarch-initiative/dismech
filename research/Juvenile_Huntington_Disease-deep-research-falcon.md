---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-19T21:00:52.845252'
end_time: '2026-08-19T21:15:07.781662'
duration_seconds: 854.94
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Juvenile Huntington Disease (Westphal variant)
  mondo_id: MONDO:0016621
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 44
reference_validation:
  total_references: 17
  verified: 17
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 17
  on_topic: 10
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Juvenile_Huntington_Disease-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Juvenile Huntington Disease (Westphal variant)
- **MONDO ID:** MONDO:0016621 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Juvenile Huntington Disease (Westphal variant)** covering all of the
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
- **Disease Name:** Juvenile Huntington Disease (Westphal variant)
- **MONDO ID:** MONDO:0016621 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Juvenile Huntington Disease (Westphal variant)** covering all of the
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


# Juvenile Huntington Disease (Westphal Variant): Comprehensive Disease-Characteristics Report

## Executive summary

Juvenile-onset Huntington disease (JHD/JOHD) is the pediatric end of the Huntington disease (HD) spectrum, usually defined by unequivocal disease onset at **≤20 years** or, in some modern cohorts, **before 21 years**. “Westphal variant” traditionally denotes the characteristic akinetic-rigid juvenile presentation: rigidity, bradykinesia, dystonia, gait and bulbar dysfunction often dominate over chorea, while cognitive/behavioral deterioration and epilepsy are prominent. It is not a separate molecular disorder: it results from a germline **HTT exon-1 CAG-repeat expansion**, generally a large, uninterrupted expansion and frequently transmitted by the father. OpenTargets maps juvenile HD to **MONDO:0016621** and identifies **HTT (ENSG00000197386)** as the strongly supported causal target. (OpenTargets Search: juvenile Huntington disease,Huntington disease-HTT, schultz2023longitudinalclinicaland pages 1-1, furby2023comorbiditiesandclinical pages 1-2)

The strongest quantitative juvenile-specific findings are: (1) CAG length explained **84% of variance in age at motor onset** in Kids-JOHD; (2) a longitudinal cohort of 26 affected participants showed **3.99% annual striatal-volume loss** and a **7.29-point/year increase** in UHDRS Total Motor Score; and (3) Swedish registry data identified 45 juvenile cases among 1,492 HD diagnoses and showed excess epilepsy, constipation, and acute respiratory symptoms. (schultz2020theassociationbetween pages 3-5, schultz2023longitudinalclinicaland pages 1-1, furby2023comorbiditiesandclinical pages 1-2)

There is currently **no curative or proven disease-modifying treatment**, and the juvenile-specific evidence base is especially sparse. Care is individualized and multidisciplinary. Contemporary research emphasizes HTT lowering and suppression of somatic CAG expansion, particularly through MSH3, MLH1/MutL, PMS1, and FAN1 biology. These approaches remain experimental and generally have not been tested in children with JHD. (ferguson2024therapeuticvalidationof pages 1-3, aldous2024acagrepeat pages 1-2, kim2024posttranscriptionalregulationof pages 1-2, driscoll2024dosedependentreductionof pages 1-2, mclean2024splicemodulatorstarget pages 1-2)

---

## 1. Disease information

### Definition and scope

JHD is an autosomal-dominant, progressive, ultimately fatal neurodevelopmental-neurodegenerative disorder caused by an expanded HTT CAG tract. The age boundary varies slightly by resource: Swedish registry work used **≤20 years**, whereas Kids-JOHD used diagnosis before age 21. “Pediatric HD” is sometimes reserved for the most aggressive childhood cases, particularly those with **>80 CAG repeats**; “Westphal variant” refers to phenotype rather than a different genotype. (schultz2023longitudinalclinicaland pages 1-1, furby2023comorbiditiesandclinical pages 1-2, tramutola2023glut1changesin pages 1-2, luca2021anoveltripletprimed pages 1-2)

**Useful synonyms:** juvenile Huntington disease; juvenile-onset Huntington disease; JHD; JOHD; juvenile Huntington’s chorea; Westphal variant; Westphal form; akinetic-rigid juvenile Huntington disease; pediatric Huntington disease. “Huntington disease-like” disorders are phenocopies and should not be treated as synonyms.

### Identifiers

- **MONDO:** MONDO:0016621, juvenile Huntington disease.
- **OMIM disease:** Huntington disease, **OMIM 143100**; no consistently separate OMIM entry for the juvenile phenotype was established in the retrieved evidence.
- **Gene:** **HTT**, OMIM 613004; HGNC-approved symbol HTT; Ensembl ENSG00000197386.
- **ICD-10:** G10, Huntington disease. No robust juvenile-specific ICD-10 subcode; the Swedish study used routine ICD-10-coded registry data.
- **ICD-11:** classified under Huntington disease; a juvenile-specific billing subdivision should not be assumed without jurisdictional verification.
- **MeSH:** Huntington Disease; juvenile onset is normally represented as an age/phenotype qualifier rather than a separate MeSH disease.

OpenTargets reports five supporting evidence items for the HTT–juvenile-HD association and only a negligible, unsupported score for SLC6A4; HTT is therefore the disease-defining gene. (OpenTargets Search: juvenile Huntington disease,Huntington disease-HTT)

### Data provenance

Most statements here derive from **aggregated disease-level resources, published cohorts, registries, postmortem studies, and models**, not individual EHR records. The Swedish study used linked national patient, prescription, and cause-of-death registries; Kids-JOHD used prospectively characterized participants. Case reports are valuable for extreme phenotypes but should not determine population frequencies. (schultz2023longitudinalclinicaland pages 1-1, furby2023comorbiditiesandclinical pages 1-2)

---

## 2. Etiology, risk, protection, and gene–environment interaction

### Primary cause

The necessary cause is a **germline CAG-repeat expansion in exon 1 of HTT on chromosome 4**, which lengthens the N-terminal polyglutamine tract and produces toxic mutant huntingtin. Normal alleles extend through 35 repeats; 36–39 is reduced penetrance, and ≥40 is generally fully penetrant over a normal lifetime. Childhood/adolescent onset is usually associated with approximately **≥60–65 repeats**, while very early pediatric cases often carry >80 and occasionally >100–200 repeats. These are repeat expansions, not conventional missense, nonsense, or frameshift variants. (aldous2024acagrepeat pages 1-2, luca2021anoveltripletprimed pages 1-2, medina2022prevalenceandincidence pages 1-2)

The expansion is **constitutional/germline**, but its length becomes mosaic through additional **somatic expansion**, especially in vulnerable neurons. In JOHD, inherited repeat length is unusually predictive: Kids-JOHD reported **R²=0.84, p=2.63×10⁻¹⁰** for CAG length versus age at motor onset, compared with 57–59% variance explained in adult cohorts. At ≥80 repeats the relationship may flatten because severe developmental disease imposes a floor on observable motor-onset age. (schultz2020theassociationbetween pages 3-5)

### Genetic risk factors and modifiers

- **Repeat length and sequence:** the uninterrupted CAG length predicts onset better than polyglutamine length alone. Loss of a stabilizing CAA interruption accelerates onset; repeat-sequence-aware testing is consequently important.
- **Paternal transmission and anticipation:** expanded alleles are unstable in the male germline, making large intergenerational expansions and juvenile disease disproportionately associated with paternal inheritance. Anticipation is therefore genuine but probabilistic.
- **Somatic-instability modifiers:** MSH2, **MSH3**, MLH1, MLH3, PMS1, PMS2, LIG1, and **FAN1** alter repeat expansion and age at onset. In pediatric-HD-derived 125-CAG iPSCs, CRISPR interference against MSH2, MSH3, or MLH1 slowed expansion most strongly; lowering PMS1, PMS2, or MLH3 had smaller effects. (ferguson2024therapeuticvalidationof pages 1-3)
- A common onset-delaying **FAN1 15AM2 haplotype** is carried by approximately 50% of HD patients. Its rs3512 alternative allele reduces miR-124-3p repression, raises FAN1, stabilizes the CAG tract, and delays onset. Rare FAN1 variants that reduce DNA binding/nuclease activity instead hasten onset. This is a modifier, not a protective allele that prevents disease. (kim2024posttranscriptionalregulationof pages 1-2)

### Environmental, lifestyle, infectious, and protective factors

No environmental toxin, infection, radiation exposure, diet, smoking behavior, occupation, or pathogen is an established cause of JHD. No lifestyle intervention has been shown to prevent penetrance in a child carrying a highly expanded allele. Environmental effects may contribute to residual variation in onset or resilience, but their magnitude and pediatric relevance are uncertain relative to CAG length and DNA-repair modifiers. There is likewise no validated environmental “protective factor.” Exercise, adequate nutrition, sleep management, and social engagement may preserve function and well-being but should not be represented as preventing molecular disease.

Accordingly, **gene–environment interaction remains poorly quantified**. The defensible model is: inherited uninterrupted CAG length sets the dominant risk; germline instability determines intergenerational expansion; cell type, age, and DNA-repair genotype influence somatic expansion; systemic health and environment may influence reserve and complications but have no demonstrated disease-preventing effect.

---

## 3. Phenotypes

### Core juvenile/Westphal phenotype

| Phenotype | Type and course | Frequency/evidence | Suggested HPO term |
|---|---|---|---|
| Rigidity | Clinical sign; progressive, often severe | Characteristic and more prominent than in adult HD | HP:0002063 |
| Bradykinesia/parkinsonism | Sign; progressive | Prominent Westphal feature | HP:0002067; HP:0001300 |
| Dystonia | Sign; progressive | More severe in JHD than typical adult HD | HP:0001332 |
| Chorea | Sign; progressive/variable | May occur but is often absent early or less prominent | HP:0002072 |
| Gait impairment, falls | Sign/functional manifestation; progressive | Expected with rigidity, dystonia, and motor decline | HP:0001288; HP:0002527 |
| Cognitive decline/executive dysfunction | Neurocognitive sign; progressive | Common and may precede unmistakable motor signs | HP:0001268; HP:0000729 |
| Behavioral/psychiatric change | Behavioral symptom; variable then progressive | Irritability, apathy, depression, aggression, obsessive/perseverative behavior or psychosis may occur | HP:0000708; phenotype-specific child terms as applicable |
| Epileptic seizures | Neurological sign; episodic, often increasing burden | Significantly more frequent in JHD; Swedish registry showed excess epilepsy | HP:0001250 |
| Dysarthria and dysphagia | Bulbar signs; progressive | Important later causes of communication failure and aspiration risk | HP:0001260; HP:0002015 |
| Weight loss/cachexia | Physical/metabolic manifestation; progressive | Clinically important in HD; juvenile frequency is poorly quantified | HP:0001824 |
| Constipation | Symptom; recurrent/chronic | Increased incidence in Swedish JHD | HP:0002019 |
| Respiratory complications | Complication | Acute respiratory symptoms increased in Swedish JHD; aspiration and pneumonia are major late concerns | HP:0002093 or specific diagnosis term |

The strongest modern real-world evidence states: “Individuals with JoHD had higher incidence rates of epilepsy, constipation and acute respiratory symptoms.” The same cohort emphasizes early cognitive/behavioral difficulties and a rigid-bradykinetic-dystonic rather than predominantly choreic phenotype. (furby2023comorbiditiesandclinical pages 1-2)

### Age, severity, progression, and quality of life

Onset is usually insidious during childhood or adolescence. Extremely expanded alleles can cause neurodevelopmental delay, school regression, epilepsy, and motor abnormalities in early childhood. Severity is variable but generally increases with repeat length. JOHD often progresses faster than adult-onset HD. (furby2023comorbiditiesandclinical pages 1-2, tramutola2023glut1changesin pages 1-2, luca2021anoveltripletprimed pages 1-2)

Quality-of-life impairment is profound: loss of school participation, mobility, speech, swallowing, self-care, and independence; psychiatric distress; social isolation; and high caregiver burden. Juvenile-specific EQ-5D/SF-36 norms and per-phenotype utility values were not identified. Adult HD data should not be silently imputed to children.

---

## 4. Genetic and molecular information

### Causal gene and variant interpretation

**HTT** is the only established causal gene. The disease allele is described by repeat count and tract structure rather than standard short-variant HGVS alone. Clinically:

- ≤26: stable normal range.
- 27–35: intermediate/mutable; generally not expected to cause HD in the carrier but may expand in offspring.
- 36–39: reduced penetrance.
- ≥40: full-penetrance range.
- >60–65: strongly enriched in juvenile onset.
- >80: often highly aggressive pediatric disease.

Population databases such as gnomAD are not reliable frequency resources for very large expansions because conventional short-read pipelines under-detect them. These alleles are rare in the general population and should not be interpreted from an apparent gnomAD absence. The variant is constitutional, autosomal dominant, and subject to both germline and tissue-specific somatic mosaicism. (aldous2024acagrepeat pages 1-2, luca2021anoveltripletprimed pages 1-2)

### Functional consequence

The expansion produces a toxic **gain of function** through mutant huntingtin/polyglutamine and N-terminal fragments, accompanied by loss or perturbation of normal huntingtin functions. Aberrant processing generates aggregation-prone HTT exon-1 protein; RNA-mediated toxicity and RAN translation may contribute. Nuclear inclusions are markers of pathology, although the soluble/oligomeric species may be more directly toxic and inclusions can sometimes represent sequestration. (tabrizi2020huntingtondiseasenew pages 4-7, tabrizi2020huntingtondiseasenew pages 13-16, pengo2024beyondcagrepeats pages 7-8, aldous2024acagrepeat pages 1-2)

### Epigenetics and structural abnormalities

HD involves altered chromatin accessibility, histone acetylation, DNA methylation, and transcription-factor occupancy, but no epigenetic mark is currently diagnostic or validated as a juvenile-specific causal lesion. The FAN1 rs3512 mechanism is post-transcriptional regulation by miR-124-3p rather than classical DNA methylation. No recurrent aneuploidy, translocation, inversion, or copy-number abnormality defines JHD. (kim2024posttranscriptionalregulationof pages 1-2, matlik2024celltypespecificcagrepeat pages 1-2)

---

## 5. Environmental information

JHD is not infectious, immune-mediated, toxic, or occupational in origin. There is no zoonotic transmission and no public-health exposure control that prevents it. Environmental factors are relevant mainly to complication management: aspiration exposure, inactivity, malnutrition, sleep disruption, medication adverse effects, and caregiver/social context can worsen morbidity. Smoking, alcohol, diet, and pollution have not been established as juvenile-onset determinants.

---

## 6. Mechanism and pathophysiology

### Integrated causal chain

**Upstream:** inherited, usually uninterrupted HTT CAG expansion → expanded polyglutamine and aberrant HTT exon-1/RNA products → germline anticipation plus cell-specific somatic expansion governed by mismatch repair/FAN1 balance.

**Intermediate:** misfolding and toxic protein interactions; impaired transcription and nucleocytoplasmic transport; altered proteasome/autophagy; mitochondrial and glucose-metabolic dysfunction; defective axonal transport and synaptic signaling; glutamatergic excitotoxicity; glial activation and neuroinflammation.

**Downstream:** dysfunction and death of corticostriatal neurons, especially direct- and indirect-pathway medium spiny neurons → striatal atrophy and circuit failure → rigidity, bradykinesia, dystonia, cognitive/behavioral deterioration, seizures and later bulbar/systemic complications. (tabrizi2020huntingtondiseasenew pages 4-7, tong2024huntington’sdiseasecomplex pages 4-5, tabrizi2020huntingtondiseasenew pages 1-4, bates2015huntingtondisease pages 1-4)

### Somatic expansion and selective vulnerability: major 2024 advance

Human postmortem FANS/deep profiling showed expansion in medium spiny neurons, cholinergic interneurons, and cerebellar Purkinje neurons. In five HD donors with inherited 42–45 uninterrupted CAGs, glial and several interneuron populations generally gained <5 repeats, whereas about half of direct and indirect MSNs gained >20 repeats (mean gain approximately 22); cholinergic interneurons had a mean gain around 18 despite relative survival. Elevated MSH2/MSH3 in MSNs inhibited FAN1-mediated excision of slipped CAG structures. Thus expansion appears important but **not sufficient by itself** for cell death. (matlik2024celltypespecificcagrepeat pages 1-2)

This qualification matters in very-large-repeat JHD. In zQ175 mice carrying about 185 CAGs, complete Msh3 loss prevented expansion and 50% reduction slowed it, yet neither striatal aggregates nor the dysregulated transcriptional profile improved. The authors concluded that additional expansion is not required when the inherited repeat is already extremely long, noting that comparable human repeats can cause onset before age two. Early somatic-instability intervention may therefore be most relevant before a toxicity threshold is crossed. (aldous2024acagrepeat pages 1-2)

### Energy metabolism and pediatric-specific profiling

A 2023 observational case-control study compared cortex and fibroblasts from highly expanded pediatric HD (>80 CAG), JHD, adult HD, and controls. In highly expanded pediatric brain, GLUT1 and GLUT3 were reduced; mitochondrial complexes II–III and hexokinase-II were also reduced. JHD expression patterns were closer to adult HD than to the >80-CAG pediatric subgroup. The authors’ exact interpretation was: **“Our data suggest a dysfunctional hypometabolic state occurring specifically in paediatric Huntington disease brains.”** Samples were extremely small—brain n=2 for highly expanded pediatric HD and n=3 for JHD—so this is hypothesis-generating rather than a validated biomarker. (tramutola2023glut1changesin pages 1-2)

### Other mechanisms and suggested ontology terms

- Protein aggregation: GO:0097352.
- DNA mismatch repair: GO:0006298.
- Autophagy: GO:0006914; autophagosome GO:0005776.
- Mitochondrial ATP production/oxidative stress: GO:0042775; mitochondrion GO:0005739.
- Synaptic signaling: GO:0099536.
- Inflammatory response: GO:0050729.
- Transcription, DNA-templated: GO:0006351.
- Nucleus: GO:0005634; proteasome complex: GO:0000502.

HD brains and patient/model systems support reduced ATP production, respiratory-chain dysfunction, impaired mitochondrial movement, autophagy/UPS failure, transcription-factor sequestration, NMDA-receptor signaling abnormalities, and increased inflammatory markers such as CSF YKL-40, chitotriosidase, and IL-6. Most are general-HD findings; their precise contribution in JHD remains incompletely quantified. (tabrizi2020huntingtondiseasenew pages 4-7, tong2024huntington’sdiseasecomplex pages 4-5, tabrizi2020huntingtondiseasenew pages 16-19)

---

## 7. Anatomical structures affected

The principal system is the central nervous system. The earliest and most characteristic macroscopic injury is bilateral striatal degeneration involving **caudate nucleus (UBERON:0002420)** and **putamen (UBERON:0001874)**, collectively **striatum (UBERON:0002435)**. Cerebral cortex (UBERON:0000956), white matter, thalamic and other subcortical structures, and in severe pediatric disease cerebellar/developmental networks are also involved. Disease is generally bilateral and network-wide rather than unilateral. (matlik2024celltypespecificcagrepeat pages 1-2, schultz2023longitudinalclinicaland pages 1-1, bates2015huntingtondisease pages 1-4)

At cell level, direct- and indirect-pathway striatal medium spiny projection neurons are most vulnerable. Cholinergic interneurons can undergo repeat expansion yet remain relatively spared, showing that repeat expansion and toxicity are separable. Purkinje neurons also exhibit expansion. Astrocytes, microglia, and oligodendroglia participate in homeostatic and inflammatory dysfunction. (tabrizi2020huntingtondiseasenew pages 16-19, matlik2024celltypespecificcagrepeat pages 1-2)

Subcellular sites include nucleus/nuclear pores, cytoplasm, axons and synapses, mitochondria, autophagosomes, lysosomes, and proteasomes. (tabrizi2020huntingtondiseasenew pages 4-7, tong2024huntington’sdiseasecomplex pages 4-5, tabrizi2020huntingtondiseasenew pages 13-16)

---

## 8. Temporal development and natural history

The course is chronic, insidious, progressive, and lifelong; spontaneous remission is not expected. A practical staging narrative is:

1. **Genetic/developmental phase:** expanded HTT is present from conception; highly expanded alleles may alter brain development before clinical diagnosis.
2. **Premanifest/prodromal phase:** school, executive, behavioral, fine-motor, or subtle MRI changes may precede unequivocal motor diagnosis.
3. **Early manifest JHD:** cognitive/behavioral decline, rigidity/bradykinesia/dystonia, gait impairment, and sometimes seizures.
4. **Intermediate disease:** worsening motor score, striatal atrophy, communication and self-care loss, increasing seizures and nutritional burden.
5. **Advanced disease:** severe akinetic-rigid state, dysphagia, immobility, cachexia, aspiration/respiratory infection, complete dependence.

In 26 JOHD participants followed against 78 gene-non-expanded controls, striatal volume fell **3.99% per year versus 0.06%**, while UHDRS Total Motor Score increased **7.29 points/year versus −0.21**; both differences had FDR <0.0001. The authors concluded that structural imaging and clinical measures may serve as progression biomarkers, while stressing the need for larger collaborative validation. (schultz2023longitudinalclinicaland pages 1-1)

A specific median JHD survival estimate could not be robustly extracted from recent juvenile cohorts. General HD median survival is approximately 15–18 years after motor onset, but JHD—especially >80-CAG disease—often progresses faster and has reduced lifespan. Swedish data could not report all juvenile outcomes because of small cells and privacy/statistical constraints. (furby2023comorbiditiesandclinical pages 11-12, ferguson2024therapeuticvalidationof pages 1-3, luca2021anoveltripletprimed pages 1-2, bates2015huntingtondisease pages 1-4)

---

## 9. Inheritance and population

### Inheritance

Inheritance is **autosomal dominant**: each child of a heterozygous carrier has a 50% chance of inheriting that parental allele, although the repeat may change length. Penetrance is repeat-length- and age-dependent: reduced at 36–39, high/near complete at ≥40, and effectively complete with large juvenile-associated expansions. Expressivity is variable because uninterrupted repeat length, modifier genes, somatic expansion, and other factors influence onset and course. (luca2021anoveltripletprimed pages 1-2, medina2022prevalenceandincidence pages 1-2)

Anticipation is prominent, especially through paternal transmission. Germline/somatic mosaicism exists. Consanguinity is not a risk factor for this dominant disorder. “Carrier frequency” is not clinically analogous to a recessive carrier state: expansion-positive people are themselves at age-dependent risk. No single juvenile founder allele is established, although HD prevalence varies with ancestral HTT haplotypes and local founder populations.

### Epidemiology

A 2022 meta-analysis of 33 studies estimated overall HD incidence at **0.48/100,000 person-years (95% CI 0.33–0.63)** and prevalence at **4.88/100,000 (95% CI 3.38–7.06)**, with greater burden in Europe and North America than several Asian/African populations. (medina2022prevalenceandincidence pages 1-2)

Juvenile cases comprise approximately **1–9.6% of HD**, with older meta-analytic estimates often near 5%. Swedish 2018 HD prevalence was 10.2/100,000; among 1,492 diagnoses during 2002–2018, 45 (3.0%) were juvenile by diagnosis before age 20. These are not direct JHD prevalence/incidence estimates. Sex-linked inheritance is absent; no reproducible major sex ratio is established, although paternal origin is enriched. (furby2023comorbiditiesandclinical pages 1-2)

---

## 10. Diagnostics

### Recommended diagnostic pathway

1. Recognize progressive childhood/adolescent cognitive/behavioral decline, school regression, rigidity, dystonia, bradykinesia, gait dysfunction or seizures—particularly with an HD family history.
2. Obtain a three-generation pedigree, neurological/movement-disorder examination, neuropsychological/psychiatric assessment, and collateral history.
3. Provide pre-test genetic counseling appropriate to a symptomatic minor and family.
4. Confirm by **direct HTT CAG-repeat sizing** using validated PCR/capillary electrophoresis, with repeat-primed PCR or another large-expansion method when one allele is missing, apparent homozygosity occurs, or pediatric disease is suspected.
5. Characterize interruptions/uninterrupted CAG length where technically available, especially for genotype–phenotype discordance.

A triplet-primed assay accurately detected normal through very large alleles, including previously undisclosed expansions **>200 repeats**, and can avoid allele dropout caused by flanking variants. Flanking PCR alone becomes inefficient as repeat length increases. (luca2021anoveltripletprimed pages 1-2)

### Role of WES, WGS, panels, and cytogenetics

Routine WES is a poor first-line test because repeat expansions are not reliably captured. Short-read WGS may flag an expansion but still requires orthogonal sizing; specialized long-read sequencing can resolve count and interruptions. If HTT testing is negative, a movement-disorder/chorea/epilepsy panel or WES/WGS can investigate phenocopies. CMA, karyotype, FISH, and mitochondrial sequencing are not primary JHD tests unless another syndrome is suspected.

### Imaging, laboratory and functional biomarkers

- **MRI:** bilateral caudate/putamen atrophy, ventricular enlargement, cortical/white-matter changes; annual striatal-volume loss is currently the strongest juvenile-specific imaging progression candidate. (schultz2023longitudinalclinicaland pages 1-1)
- **Clinical scales:** UHDRS motor examination, modified juvenile UHDRS, cognitive tests, seizure tracking, swallowing/nutritional measures.
- **Biofluids:** CSF mutant huntingtin and CSF/plasma neurofilament light (NfL) track HD burden in adults and are under juvenile study, but neither replaces genetic confirmation. NCT05707663 includes NfL. (tabrizi2020huntingtondiseasenew pages 13-16, tabrizi2020huntingtondiseasenew pages 16-19, NCT05707663 chunk 1)
- **EEG:** indicated for seizures or episodic events; abnormalities are not diagnostic of JHD.
- **Metabolic assays:** GLUT1/GLUT3 and mitochondrial findings remain research measurements, not clinical tests. (tramutola2023glut1changesin pages 1-2)
- **Biopsy/pathology:** not required. Postmortem pathology shows severe striatal neuronal loss, gliosis, and nuclear/cytoplasmic huntingtin inclusions.

### Differential diagnosis

Important alternatives include Wilson disease, neurodegeneration with brain iron accumulation, juvenile parkinsonism (PRKN/PINK1/DJ-1), dopa-responsive dystonia, spinocerebellar ataxias including SCA17, dentatorubral-pallidoluysian atrophy, Huntington disease-like 2, C9orf72 disease, mitochondrial disease, neuronal ceroid lipofuscinosis, progressive myoclonus epilepsies, autoimmune/postinfectious chorea, medication/toxin effects, and primary psychiatric/neurodevelopmental disorders. A negative HTT expansion should trigger phenotype-guided investigation rather than a clinical label of JHD.

### Screening

There is no newborn or population screening. Cascade testing of adult relatives, predictive testing of competent adults, and diagnostic testing of symptomatic minors are appropriate with counseling. Predictive testing of an asymptomatic minor is generally deferred because no preventive childhood treatment exists. Prenatal diagnosis and PGT-M are available for families who choose them.

---

## 11. Outcome and prognosis

JHD causes progressive motor, cognitive, psychiatric, educational, and social disability, eventually leading to complete dependence. Recovery from the underlying neurodegeneration is not expected. Major complications include falls, fractures, seizures/status epilepticus, aspiration, pneumonia, constipation, malnutrition/cachexia, pressure injury, and psychiatric crisis. Swedish registry data showed progressive clinical burden and excess juvenile epilepsy/respiratory symptoms; in the broader HD cohort, pneumonia was associated with mortality (hazard ratio 2.16), but that estimate was not juvenile-specific. (furby2023comorbiditiesandclinical pages 1-2, furby2023comorbiditiesandclinical pages 11-12)

Prognosis is most strongly associated with uninterrupted CAG length and age at onset. Baseline motor/cognitive burden, rate of striatal atrophy, nutritional/swallowing status, seizures, respiratory complications, NfL, and CSF mHTT are candidate prognostic markers, but only CAG length has strong juvenile-specific quantitative support. (schultz2020theassociationbetween pages 3-5, schultz2023longitudinalclinicaland pages 1-1)

---

## 12. Treatment and current applications

### General strategy

There is no approved therapy that slows or stops JHD. Management should involve pediatric neurology/movement disorders, psychiatry/psychology, epilepsy care, clinical genetics, physiotherapy, occupational and speech/swallowing therapy, nutrition, social work, education services, palliative care, and caregiver support.

### Symptom-directed pharmacotherapy

- **Rigidity, dystonia, bradykinesia:** individualized trials of dopaminergic therapy in selected rigid-akinetic patients, baclofen/benzodiazepines, anticholinergics, or botulinum toxin for focal dystonia; evidence is mostly case-based.
- **Chorea:** VMAT2 inhibitors tetrabenazine or deutetrabenazine and dopamine-receptor antagonists can reduce adult HD chorea, but sedation, depression, akathisia and worsening parkinsonism require particular caution in Westphal JHD. A 2023 expert guideline favored tiapride in its practice setting and tetrabenazine if ineffective/not tolerated; it acknowledges limited RCT evidence and no trials of combination therapy. (saft2023symptomatictreatmentoptions pages 1-2)
- **Psychiatric symptoms:** SSRIs for depression/anxiety/obsessive symptoms; atypical antipsychotics for psychosis, aggression or severe irritability; mood stabilizers when indicated. Risperidone may help irritability/chorea/sleep, olanzapine may help weight loss and chorea, and quetiapine may provide mood/sleep benefits. Treatment must account for seizure threshold and motor adverse effects. (saft2023symptomatictreatmentoptions pages 1-2)
- **Epilepsy:** select antiseizure medication by seizure type and adverse-effect profile; no JHD-specific drug has proven superiority.
- **Nutrition/dysphagia:** texture modification, high-calorie support, swallowing therapy, aspiration precautions, and shared decision-making about gastrostomy.
- **Sleep, constipation, pain and spasticity:** standard symptom-specific approaches with careful polypharmacy review.

Suggested NCIT concepts include Genetic Counseling (NCIT:C15214), Genetic Testing (NCIT:C15709), MRI (NCIT:C16809), Antisense Oligonucleotide Therapy (NCIT:C129670), and RNA Interference (NCIT:C18250).

### Experimental disease modification

- **HTT lowering:** ASOs, siRNA/RNAi, viral microRNA and oral splice modulators aim to reduce mutant or total HTT. Human adult trials have demonstrated target engagement, but clinical benefit remains unproven and broad HTT lowering raises safety concerns. Branaplam’s adult VIBRANT-HD study was halted for safety concerns. (tabrizi2020huntingtondiseasenew pages 13-16, mclean2024splicemodulatorstarget pages 1-2)
- **Somatic-instability therapy:** reducing MSH3/MSH2/MLH1/MutL activity or increasing FAN1 is mechanistically compelling. In HdhQ111 mice, MSH3 siRNA produced an approximately one-to-one relationship between MSH3 reduction and suppressed expansion, but **75% MSH3 reduction did not change nuclear aggregates**. (driscoll2024dosedependentreductionof pages 1-2)
- **PMS1 splice modulation:** branaplam and risdiplam reduced CAG expansion in engineered cells through PMS1 pseudoexon inclusion rather than HTT lowering; homozygous, not heterozygous, PMS1 inactivation reduced expansion. Off-target splicing and cell-specific effects limit direct translation. (mclean2024splicemodulatorstarget pages 1-2)
- **Gene editing/cell therapy/autophagy/metabolic therapy:** CRISPR/TALEN/zinc-finger approaches, stem-cell strategies, autophagy enhancers and metabolic interventions remain preclinical or early experimental; none is established for JHD. (tong2024huntington’sdiseasecomplex pages 4-5, tabrizi2020huntingtondiseasenew pages 13-16)

### Juvenile-specific studies and trials

- **NCT05707663**, active but not recruiting: observational, 37 participants aged 4–30, 2020–2026; longitudinal MRI/DTI, cognition, behavior, UHDRS motor assessment and NfL across five US centers. It is not a treatment trial. (NCT05707663 chunk 1)
- **NCT01590602 (REGISTRY-JHD)**, completed: prospective observational study of 78 participants with onset ≤25 years, evaluating modified UHDRS sensitivity to progression. (NCT01590602 chunk 1)

No juvenile-specific interventional trial demonstrating disease modification was identified. This is a major implementation gap.

---

## 13. Prevention

**Primary prevention** through lifestyle or medication is not available. For families, reproductive options include genetic counseling, natural conception with or without prenatal testing, IVF with PGT-M, donor gametes, and adoption. These are preference-sensitive options, not recommendations.

**Secondary prevention** consists of earlier recognition in at-risk symptomatic children, careful cascade evaluation, seizure surveillance, and research biomarker monitoring; it cannot currently prevent molecular progression.

**Tertiary prevention** includes fall and aspiration prevention, vaccination and prompt infection treatment, nutritional maintenance, seizure control, contracture/pressure-injury prevention, mental-health and suicide-risk management, and advance-care planning. There is no disease-specific vaccine, chemoprophylaxis, or population-screening program.

---

## 14. Other species and natural disease

No well-established naturally occurring veterinary counterpart of HTT-expansion JHD was identified. HD is not zoonotic or transmissible. Huntingtin and its cellular functions are evolutionarily conserved, permitting engineered models in mammals, fish, flies, worms and yeast, but these are induced experimental systems rather than naturally acquired disease.

Relevant taxa include human **NCBI Taxon 9606**, mouse **10090**, rat **10116**, zebrafish **7955**, Drosophila melanogaster **7227**, Caenorhabditis elegans **6239**, and Saccharomyces cerevisiae **4932**. Orthologue Gene IDs and VBO breed terms should be pulled directly from current NCBI/Alliance/VBO releases during database implementation rather than inferred.

---

## 15. Model organisms and experimental systems

### Major models

- **R6/2 mouse:** N-terminal human HTT exon-1 transgene with a very large repeat; rapid motor decline, weight loss, inclusions, and short survival. Useful for aggressive juvenile-like toxicity and rapid screens, but transgene overexpression and fragment-only biology limit fidelity.
- **zQ175/HdhQ150 knock-in mice:** expanded repeat in endogenous Htt; progressive molecular, motor and striatal phenotypes. zQ175 has roughly 185–190 repeats and therefore molecularly resembles an extreme pediatric allele more than common adult HD. Its failure to improve aggregation/transcription after Msh3 deletion warns against assuming somatic-expansion therapy will reverse threshold-crossed disease. (aldous2024acagrepeat pages 1-2)
- **HdhQ111 knock-in mouse:** useful for quantifying somatic expansion and testing MSH3-directed interventions; di-siRNA reduced expansion without reducing aggregates. (driscoll2024dosedependentreductionof pages 1-2)
- **YAC128/BACHD:** full-length human mutant HTT; useful for circuit, excitotoxicity, behavior and longitudinal neurodegeneration, but repeat size/expression and mouse lifespan affect translation. (tong2024huntington’sdiseasecomplex pages 4-5)
- **Patient-derived fibroblasts/iPSCs/MSN cultures:** retain patient repeat architecture and permit human cell-specific target validation. The 125-CAG iPSC line was derived from a seven-year-old girl and demonstrated that therapeutically feasible MMR lowering slows expansion. Limitations include reprogramming-related age reset, culture immaturity and incomplete multicellular circuitry. (ferguson2024therapeuticvalidationof pages 1-3)
- **Organoids, Drosophila, C. elegans, zebrafish and yeast:** useful for development, aggregation, modifier screens, transport and toxicity; none reproduces the complete human cognitive/psychiatric phenotype or decades-long natural history.

### Applications and limitations

Models support target discovery, repeat-instability measurement, HTT lowering, pharmacology, biomarker translation and developmental-mechanism research. No single model captures the combination of human corticostrial development, paternal anticipation, cell-specific somatic expansion, epilepsy, behavioral disease and long-term neurodegeneration. Results should therefore be triangulated across human genetics, patient tissue, iPSC-derived neurons and multiple in-vivo models.

---

## Ontology-ready summary

The following artifact consolidates suggested MONDO, HPO, GO, CL, UBERON and NCIT annotations. IDs marked “verification required” should be checked against the ontology release used by the target knowledge base.

| domain | entity/phenotype/mechanism/anatomy/intervention | suggested ontology term and ID | evidence/qualification |
|---|---|---|---|
| disease | Juvenile Huntington disease (Westphal variant) | MONDO:0016621 juvenile Huntington disease | MONDO/OpenTargets association with HTT; juvenile form defined by onset before age 20-21 years in cohort literature; Westphal phenotype emphasizes rigidity/bradykinesia over chorea (OpenTargets Search: juvenile Huntington disease,Huntington disease-HTT, schultz2023longitudinalclinicaland pages 1-1, furby2023comorbiditiesandclinical pages 1-2) |
| phenotype | Juvenile onset | HPO: Childhood onset — ID verification required | JOHD defined as symptom onset before age 21 years in Kids-JOHD and before/at 20 years in Swedish registry; use age-at-onset qualifier in phenotype annotations (schultz2023longitudinalclinicaland pages 1-1, furby2023comorbiditiesandclinical pages 1-2) |
| phenotype | Rigidity | HP:0002063 Rigidity | More severe in JoHD/Westphal phenotype than typical adult choreic presentation (furby2023comorbiditiesandclinical pages 1-2) |
| phenotype | Bradykinesia | HP:0002067 Bradykinesia | Registry/review context indicates bradykinesia is prominent in JoHD (furby2023comorbiditiesandclinical pages 1-2) |
| phenotype | Dystonia | HP:0001332 Dystonia | More severe in JoHD than in typical adult-onset HD (furby2023comorbiditiesandclinical pages 1-2) |
| phenotype | Seizures/epilepsy | HP:0001250 Seizure | Higher incidence of epilepsy in JoHD; epileptic seizures are much more frequent (furby2023comorbiditiesandclinical pages 1-2) |
| phenotype | Cognitive decline | HP:0001268 Mental deterioration | Cognitive changes are common and often early; longitudinal/registry data support cognitive burden (schultz2023longitudinalclinicaland pages 1-1, furby2023comorbiditiesandclinical pages 1-2) |
| phenotype | Behavioral abnormality | HP:0000708 Behavioral abnormality | Behavioral problems are part of core juvenile phenotype and may precede motor diagnosis (furby2023comorbiditiesandclinical pages 1-2, bates2015huntingtondisease pages 1-4) |
| phenotype | Dysarthria | HP:0001260 Dysarthria | Common progressive bulbar/motor manifestation in HD/JOHD; include as suggested term, juvenile-specific frequency not quantified here (bates2015huntingtondisease pages 1-4) |
| phenotype | Dysphagia | HP:0002015 Dysphagia | Relevant progressive swallowing complication in manifest HD; juvenile-specific frequency not quantified here (bates2015huntingtondisease pages 1-4) |
| phenotype | Gait abnormality | HP:0001288 Gait disturbance | Expected with progressive parkinsonism/rigidity and motor decline; longitudinal motor worsening supports relevance (schultz2023longitudinalclinicaland pages 1-1, bates2015huntingtondisease pages 1-4) |
| phenotype | Chorea (less prominent) | HP:0002072 Chorea | Chorea can occur but is less prominent in Westphal/juvenile phenotype than rigidity-bradykinesia-dystonia (furby2023comorbiditiesandclinical pages 1-2) |
| phenotype | Weight loss | HP:0001824 Weight loss | Clinically relevant in HD and addressed in symptomatic management guidance; juvenile-specific frequency not quantified here (saft2023symptomatictreatmentoptions pages 1-2, bates2015huntingtondisease pages 1-4) |
| mechanism | Mutant huntingtin protein aggregation | GO:0097352 protein aggregation | Pathogenic HTT exon 1/polyQ protein is aggregation-prone; human and model evidence (aldous2024acagrepeat pages 1-2, bates2015huntingtondisease pages 1-4) |
| mechanism | Somatic CAG expansion / DNA mismatch repair | GO:0006298 mismatch repair | Strong human genetic and experimental evidence implicates MSH3, MLH1, PMS1/2, MLH3, FAN1 in somatic repeat instability and onset modification; no single GO term for “somatic CAG expansion” confidently assigned here (ferguson2024therapeuticvalidationof pages 1-3, kim2024posttranscriptionalregulationof pages 1-2, matlik2024celltypespecificcagrepeat pages 1-2, mclean2024splicemodulatorstarget pages 1-2) |
| mechanism | Autophagy dysfunction | GO:0006914 autophagy | Impaired autophagy and benefit from autophagy induction reported in HD models/patient-derived systems (tabrizi2020huntingtondiseasenew pages 4-7, tong2024huntington’sdiseasecomplex pages 4-5) |
| mechanism | Mitochondrial dysfunction | GO:0005739 mitochondrion / GO:0042775 mitochondrial ATP synthesis coupled electron transport | Human and model data support altered ATP production, respiratory chain defects, and pediatric hypometabolic signatures; process ID should be chosen per curation use case (tabrizi2020huntingtondiseasenew pages 4-7, tong2024huntington’sdiseasecomplex pages 4-5, tramutola2023glut1changesin pages 1-2) |
| mechanism | Transcriptional dysregulation | GO:0006351 transcription, DNA-templated | mHTT disrupts transcriptional regulation in human brain and models (tong2024huntington’sdiseasecomplex pages 4-5, bates2015huntingtondisease pages 1-4) |
| mechanism | Neuroinflammation | GO:0050729 positive regulation of inflammatory response | Elevated inflammatory proteins/microglial markers in HD; pediatric specificity not established but disease-relevant (tabrizi2020huntingtondiseasenew pages 16-19) |
| mechanism | Synaptic signaling dysfunction | GO:0099536 synaptic signaling | Synaptic dysfunction/excitotoxic signaling are established HD mechanisms (tong2024huntington’sdiseasecomplex pages 4-5, bates2015huntingtondisease pages 1-4) |
| cell type | Striatal medium spiny neuron | CL term and ID verification required | Human postmortem study directly implicates MSNs as major site of somatic expansion and vulnerability (matlik2024celltypespecificcagrepeat pages 1-2) |
| cell type | Cholinergic interneuron | CL term and ID verification required | Human postmortem study found large mHTT CAG expansions in striatal cholinergic interneurons despite relative sparing (matlik2024celltypespecificcagrepeat pages 1-2) |
| cell type | Purkinje cell | CL:0000121 Purkinje cell | Human postmortem study found expansions in cerebellar Purkinje neurons (matlik2024celltypespecificcagrepeat pages 1-2) |
| cell type | Astrocyte | CL:0000127 astrocyte | Glial/neuroinflammatory involvement widely reported; cell ontology term appropriate for annotation (tabrizi2020huntingtondiseasenew pages 16-19) |
| cell type | Microglia | CL:0000129 microglial cell | Microglial activation and inflammatory markers are documented in HD (tabrizi2020huntingtondiseasenew pages 16-19) |
| anatomy | Caudate nucleus | UBERON:0002420 caudate nucleus | Core vulnerable striatal structure in HD/JOHD (matlik2024celltypespecificcagrepeat pages 1-2, bates2015huntingtondisease pages 1-4) |
| anatomy | Putamen | UBERON:0001874 putamen | Core vulnerable striatal structure in HD/JOHD (matlik2024celltypespecificcagrepeat pages 1-2, bates2015huntingtondisease pages 1-4) |
| anatomy | Striatum | UBERON:0002435 striatum | Principal site of atrophy and biomarker change; annualized striatal volume loss in JOHD reported (schultz2023longitudinalclinicaland pages 1-1, bates2015huntingtondisease pages 1-4) |
| anatomy | Cerebral cortex | UBERON:0000956 cerebral cortex | Cortical involvement, transcriptional changes, and pediatric frontal cortical GLUT defects reported (tramutola2023glut1changesin pages 1-2, bates2015huntingtondisease pages 1-4) |
| anatomy | Cerebellum | UBERON:0002037 cerebellum | Purkinje-cell somatic expansion documented; region less classically affected than striatum (matlik2024celltypespecificcagrepeat pages 1-2) |
| cellular component | Nucleus | GO:0005634 nucleus | Nuclear inclusions/aggregation and transcriptional effects are central features (aldous2024acagrepeat pages 1-2, bates2015huntingtondisease pages 1-4) |
| cellular component | Mitochondrion | GO:0005739 mitochondrion | Mitochondrial defects and altered energy metabolism are repeatedly implicated (tabrizi2020huntingtondiseasenew pages 4-7, tramutola2023glut1changesin pages 1-2) |
| cellular component | Autophagosome | GO:0005776 autophagosome | Suitable component term for autophagy pathway annotation (tabrizi2020huntingtondiseasenew pages 4-7, tong2024huntington’sdiseasecomplex pages 4-5) |
| cellular component | Proteasome | GO:0000502 proteasome complex | UPS/proteasomal dysfunction is implicated in HD pathobiology (tong2024huntington’sdiseasecomplex pages 4-5) |
| intervention | Genetic testing | NCIT:C15709 Genetic Testing | Molecular confirmation by HTT CAG sizing is diagnostic cornerstone (luca2021anoveltripletprimed pages 1-2, medina2022prevalenceandincidence pages 1-2) |
| intervention | Brain MRI | NCIT:C16809 Magnetic Resonance Imaging | Structural MRI used for progression assessment; striatal volume is a candidate JOHD biomarker (NCT05707663 chunk 1, schultz2023longitudinalclinicaland pages 1-1) |
| intervention | Physical therapy | NCIT term ID verification required | Recommended supportive multidisciplinary care in HD guidelines; exact NCIT concept should be confirmed during implementation (saft2023symptomatictreatmentoptions pages 1-2, bates2015huntingtondisease pages 1-4) |
| intervention | Occupational therapy | NCIT term ID verification required | Part of supportive multidisciplinary management (furby2023comorbiditiesandclinical pages 1-2, bates2015huntingtondisease pages 1-4) |
| intervention | Speech therapy | NCIT term ID verification required | Relevant for dysarthria/dysphagia support; exact NCIT ID should be confirmed (bates2015huntingtondisease pages 1-4) |
| intervention | Antisense oligonucleotide therapy | NCIT:C129670 Antisense Oligonucleotide Therapy | Disease-modifying strategy under investigation for HTT lowering; not approved for JOHD (tabrizi2020huntingtondiseasenew pages 13-16, mclean2024splicemodulatorstarget pages 1-2) |
| intervention | RNA interference | NCIT:C18250 RNA Interference | Preclinical/therapeutic HTT-lowering strategy and MSH3-targeting silencing approach (driscoll2024dosedependentreductionof pages 1-2, mclean2024splicemodulatorstarget pages 1-2) |
| intervention | Genetic counseling | NCIT:C15214 Genetic Counseling | Essential for predictive testing, family planning, and juvenile/family cases (medina2022prevalenceandincidence pages 1-2, bates2015huntingtondisease pages 1-4) |


*Table: This table provides a compact ontology-oriented mapping for juvenile Huntington disease (Westphal variant), linking disease concepts, phenotypes, mechanisms, cell types, anatomy, and interventions to suggested ontology terms and IDs. It is designed to support structured knowledge-base curation while clearly flagging terms that require ID verification.*

---

## Key recent publications and direct abstract statements

1. **Schultz et al., Movement Disorders; published online November 2022/2023 volume. DOI:** https://doi.org/10.1002/mds.29251. Direct abstract conclusion: **“These findings demonstrate that structural brain imaging and clinical measures in JOHD may be potential biomarkers of disease progression for use in clinical trials.”** (schultz2023longitudinalclinicaland pages 1-1)
2. **Furby et al., Journal of Neurology; online 18 October 2022, 2023 volume. DOI:** https://doi.org/10.1007/s00415-022-11418-y. Direct result: **“Individuals with JoHD had higher incidence rates of epilepsy, constipation and acute respiratory symptoms.”** (furby2023comorbiditiesandclinical pages 1-2)
3. **Tramutola et al., eBioMedicine, November 2023. DOI:** https://doi.org/10.1016/j.ebiom.2023.104849. Direct interpretation: **“Our data suggest a dysfunctional hypometabolic state occurring specifically in paediatric Huntington disease brains.”** (tramutola2023glut1changesin pages 1-2)
4. **Mätlik et al., Nature Genetics, 30 January 2024. DOI:** https://doi.org/10.1038/s41588-024-01653-6. Direct conclusion: **“Our data support a model in which CAG expansions are necessary but may not be sufficient for cell death.”** (matlik2024celltypespecificcagrepeat pages 1-2)
5. **Ferguson et al., American Journal of Human Genetics, 6 June 2024. DOI:** https://doi.org/10.1016/j.ajhg.2024.04.015. Direct summary: lowering MSH2, MSH3, MLH1 and MutL factors slowed expansion in HD iPSCs and striatal cultures. (ferguson2024therapeuticvalidationof pages 1-3)
6. **Kim et al., PNAS, 12 April 2024. DOI:** https://doi.org/10.1073/pnas.2322924121. Direct mechanistic conclusion: the rs3512 alternative allele raises FAN1 by reducing miR-124-3p sensitivity and delays onset by reducing repeat instability. (kim2024posttranscriptionalregulationof pages 1-2)
7. **Aldous et al., Brain, 22 February 2024. DOI:** https://doi.org/10.1093/brain/awae063. Direct interpretation: extremely long inherited repeats can trigger pathology without further somatic expansion, supporting very early—not late rescue—intervention. (aldous2024acagrepeat pages 1-2)
8. **McLean et al., Nature Communications, April 2024. DOI:** https://doi.org/10.1038/s41467-024-47485-0. Direct finding: branaplam/risdiplam reduced expansion through PMS1 splice modulation, not simply HTT lowering. (mclean2024splicemodulatorstarget pages 1-2)

## Evidence limitations

JHD is ultra-rare, definitions vary between ≤20 and <21 or ≤25 years, and many studies combine heterogeneous childhood and adolescent cases. Phenotype percentages, survival, sex ratio, quality-of-life utilities, pharmacotherapy response rates, and juvenile-specific biomarker reference ranges remain inadequately established. Much treatment and mechanistic guidance is extrapolated from adult HD or preclinical models. The quantitative juvenile findings above should therefore be curated with cohort size, onset definition, and evidence type attached, rather than represented as universal frequencies.

References

1. (OpenTargets Search: juvenile Huntington disease,Huntington disease-HTT): Open Targets Query (juvenile Huntington disease,Huntington disease-HTT, 7 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (schultz2023longitudinalclinicaland pages 1-1): Jordan L. Schultz, Douglas R. Langbehn, Hend M. Al‐Kaylani, Ellen van der Plas, Timothy R. Koscik, Eric A. Epping, Patricia B. Espe‐Pfeifer, Erin P. Martin, David J. Moser, Vincent A. Magnotta, and Peggy C. Nopoulos. Longitudinal clinical and biological characteristics in juvenile‐onset huntington's disease. Movement Disorders, 38:113-122, Nov 2023. URL: https://doi.org/10.1002/mds.29251, doi:10.1002/mds.29251. This article has 20 citations and is from a highest quality peer-reviewed journal.

3. (furby2023comorbiditiesandclinical pages 1-2): Hannah Furby, Suzanne Moore, Anna-Lena Nordstroem, Richard Houghton, Dimitra Lambrelli, Sophie Graham, Per Svenningsson, and Åsa Petersén. Comorbidities and clinical outcomes in adult- and juvenile-onset huntington’s disease: a study of linked swedish national registries (2002–2019). Journal of Neurology, 270:864-876, Oct 2023. URL: https://doi.org/10.1007/s00415-022-11418-y, doi:10.1007/s00415-022-11418-y. This article has 22 citations and is from a domain leading peer-reviewed journal.

4. (schultz2020theassociationbetween pages 3-5): Jordan L. Schultz, Amelia D. Moser, and Peg C. Nopoulos. The association between cag repeat length and age of onset of juvenile-onset huntington’s disease. Brain Sciences, 10:575, Aug 2020. URL: https://doi.org/10.3390/brainsci10090575, doi:10.3390/brainsci10090575. This article has 20 citations.

5. (ferguson2024therapeuticvalidationof pages 1-3): Ross Ferguson, Robert Goold, Lucy Coupland, Michael Flower, and Sarah J. Tabrizi. Therapeutic validation of mmr-associated genetic modifiers in a human ex vivo model of huntington disease. Jun 2024. URL: https://doi.org/10.1016/j.ajhg.2024.04.015, doi:10.1016/j.ajhg.2024.04.015. This article has 49 citations.

6. (aldous2024acagrepeat pages 1-2): Sarah G Aldous, Edward J Smith, Christian Landles, Georgina F Osborne, Maria Cañibano-Pico, Iulia M Nita, Jemima Phillips, Yongwei Zhang, Bo Jin, Marissa B Hirst, Caroline L Benn, Brian C Bond, Winfried Edelmann, Jonathan R Greene, and Gillian P Bates. A cag repeat threshold for therapeutics targeting somatic instability in huntington's disease. Feb 2024. URL: https://doi.org/10.1093/brain/awae063, doi:10.1093/brain/awae063. This article has 75 citations and is from a highest quality peer-reviewed journal.

7. (kim2024posttranscriptionalregulationof pages 1-2): Kyung-Hee Kim, Eun Pyo Hong, Yukyeong Lee, Zachariah L. McLean, Emanuela Elezi, Ramee Lee, Seung Kwak, Branduff McAllister, Thomas H. Massey, Sergey Lobanov, Peter Holmans, Michael Orth, Marc Ciosi, Darren G. Monckton, Jeffrey D. Long, Diane Lucente, Vanessa C. Wheeler, Marcy E. MacDonald, James F. Gusella, and Jong-Min Lee. Posttranscriptional regulation of fan1 by mir-124-3p at rs3512 underlies onset-delaying genetic modification in huntington’s disease. Proceedings of the National Academy of Sciences of the United States of America, Apr 2024. URL: https://doi.org/10.1073/pnas.2322924121, doi:10.1073/pnas.2322924121. This article has 13 citations and is from a highest quality peer-reviewed journal.

8. (driscoll2024dosedependentreductionof pages 1-2): Rachelle Driscoll, Lucas Hampton, Neeta A. Abraham, J. Douglas Larigan, Nadine F. Joseph, Juan C. Hernandez-Vega, Sarah Geisler, Fu-Chia Yang, Matthew Deninger, David T. Tran, Natasha Khatri, Bruno M. D. C. Godinho, Garth A. Kinberger, Daniel R. Montagna, Warren D. Hirst, Catherine L. Guardado, Kelly E. Glajch, H. Moore Arnold, Corrie L. Gallant-Behm, and Andreas Weihofen. Dose-dependent reduction of somatic expansions but not htt aggregates by di-valent sirna-mediated silencing of msh3 in hdhq111 mice. Scientific Reports, Jan 2024. URL: https://doi.org/10.1038/s41598-024-52667-3, doi:10.1038/s41598-024-52667-3. This article has 19 citations and is from a peer-reviewed journal.

9. (mclean2024splicemodulatorstarget pages 1-2): Zachariah L. McLean, Dadi Gao, Kevin Correia, Jennie C. L. Roy, Shota Shibata, Iris N. Farnum, Zoe Valdepenas-Mellor, Marina Kovalenko, Manasa Rapuru, Elisabetta Morini, Jayla Ruliera, Tammy Gillis, Diane Lucente, Benjamin P. Kleinstiver, Jong-Min Lee, Marcy E. MacDonald, Vanessa C. Wheeler, Ricardo Mouro Pinto, and James F. Gusella. Splice modulators target pms1 to reduce somatic expansion of the huntington’s disease-associated cag repeat. Nature Communications, Apr 2024. URL: https://doi.org/10.1038/s41467-024-47485-0, doi:10.1038/s41467-024-47485-0. This article has 48 citations and is from a highest quality peer-reviewed journal.

10. (tramutola2023glut1changesin pages 1-2): Antonella Tramutola, Hannah S. Bakels, Federica Perrone, Michela Di Nottia, Tommaso Mazza, Maria Pia Abruzzese, Martina Zoccola, Sara Pagnotta, Rosalba Carrozzo, Susanne T. de Bot, Marzia Perluigi, Willeke M.C. van Roon-Mom, and Ferdinando Squitieri. Glut-1 changes in paediatric huntington disease brain cortex and fibroblasts: an observational case-control study. eBioMedicine, 97:104849, Nov 2023. URL: https://doi.org/10.1016/j.ebiom.2023.104849, doi:10.1016/j.ebiom.2023.104849. This article has 18 citations and is from a peer-reviewed journal.

11. (luca2021anoveltripletprimed pages 1-2): Alessandro De Luca, Annunziata Morella, Federica Consoli, Sergio Fanelli, Julie R. Thibert, Sarah Statt, Gary J. Latham, and Ferdinando Squitieri. A novel triplet-primed pcr assay to detect the full range of trinucleotide cag repeats in the huntingtin gene (htt). International Journal of Molecular Sciences, 22:1689, Feb 2021. URL: https://doi.org/10.3390/ijms22041689, doi:10.3390/ijms22041689. This article has 27 citations.

12. (medina2022prevalenceandincidence pages 1-2): Alex Medina, Yasamin Mahjoub, Larry Shaver, and Tamara Pringsheim. Prevalence and incidence of huntington's disease: an updated systematic review and meta‐analysis. Movement Disorders, 37:2327-2335, Sep 2022. URL: https://doi.org/10.1002/mds.29228, doi:10.1002/mds.29228. This article has 367 citations and is from a highest quality peer-reviewed journal.

13. (tabrizi2020huntingtondiseasenew pages 4-7): Sarah J. Tabrizi, Michael D. Flower, Christopher A. Ross, and Edward J. Wild. Huntington disease: new insights into molecular pathogenesis and therapeutic opportunities. Nature Reviews Neurology, pages 1-18, Aug 2020. URL: https://doi.org/10.1038/s41582-020-0389-4, doi:10.1038/s41582-020-0389-4. This article has 635 citations and is from a highest quality peer-reviewed journal.

14. (tabrizi2020huntingtondiseasenew pages 13-16): Sarah J. Tabrizi, Michael D. Flower, Christopher A. Ross, and Edward J. Wild. Huntington disease: new insights into molecular pathogenesis and therapeutic opportunities. Nature Reviews Neurology, pages 1-18, Aug 2020. URL: https://doi.org/10.1038/s41582-020-0389-4, doi:10.1038/s41582-020-0389-4. This article has 635 citations and is from a highest quality peer-reviewed journal.

15. (pengo2024beyondcagrepeats pages 7-8): Marta Pengo and Ferdinando Squitieri. Beyond cag repeats: the multifaceted role of genetics in huntington disease. Jun 2024. URL: https://doi.org/10.3390/genes15060807, doi:10.3390/genes15060807. This article has 26 citations.

16. (matlik2024celltypespecificcagrepeat pages 1-2): Kert Mätlik, Matthew Baffuto, Laura Kus, Amit Laxmikant Deshmukh, David A. Davis, Matthew R. Paul, Thomas S. Carroll, Marie-Christine Caron, Jean-Yves Masson, Christopher E. Pearson, and Nathaniel Heintz. Cell-type-specific cag repeat expansions and toxicity of mutant huntingtin in human striatum and cerebellum. Nature Genetics, 56:383-394, Jan 2024. URL: https://doi.org/10.1038/s41588-024-01653-6, doi:10.1038/s41588-024-01653-6. This article has 162 citations and is from a highest quality peer-reviewed journal.

17. (tong2024huntington’sdiseasecomplex pages 4-5): Huichun Tong, Tianqi Yang, Shuying Xu, Xinhui Li, Li Liu, Gongke Zhou, Sitong Yang, Shurui Yin, Xiao-Jiang Li, and Shihua Li. Huntington’s disease: complex pathogenesis and therapeutic strategies. International Journal of Molecular Sciences, 25:3845, Mar 2024. URL: https://doi.org/10.3390/ijms25073845, doi:10.3390/ijms25073845. This article has 143 citations.

18. (tabrizi2020huntingtondiseasenew pages 1-4): Sarah J. Tabrizi, Michael D. Flower, Christopher A. Ross, and Edward J. Wild. Huntington disease: new insights into molecular pathogenesis and therapeutic opportunities. Nature Reviews Neurology, pages 1-18, Aug 2020. URL: https://doi.org/10.1038/s41582-020-0389-4, doi:10.1038/s41582-020-0389-4. This article has 635 citations and is from a highest quality peer-reviewed journal.

19. (bates2015huntingtondisease pages 1-4): Gillian P. Bates, Ray Dorsey, James F. Gusella, Michael R. Hayden, Chris Kay, Blair R. Leavitt, Martha Nance, Christopher A. Ross, Rachael I. Scahill, Ronald Wetzel, Edward J. Wild, and Sarah J. Tabrizi. Huntington disease. Nature Reviews Disease Primers, Dec 2015. URL: https://doi.org/10.1038/nrdp.2015.5, doi:10.1038/nrdp.2015.5. This article has 2191 citations.

20. (tabrizi2020huntingtondiseasenew pages 16-19): Sarah J. Tabrizi, Michael D. Flower, Christopher A. Ross, and Edward J. Wild. Huntington disease: new insights into molecular pathogenesis and therapeutic opportunities. Nature Reviews Neurology, pages 1-18, Aug 2020. URL: https://doi.org/10.1038/s41582-020-0389-4, doi:10.1038/s41582-020-0389-4. This article has 635 citations and is from a highest quality peer-reviewed journal.

21. (furby2023comorbiditiesandclinical pages 11-12): Hannah Furby, Suzanne Moore, Anna-Lena Nordstroem, Richard Houghton, Dimitra Lambrelli, Sophie Graham, Per Svenningsson, and Åsa Petersén. Comorbidities and clinical outcomes in adult- and juvenile-onset huntington’s disease: a study of linked swedish national registries (2002–2019). Journal of Neurology, 270:864-876, Oct 2023. URL: https://doi.org/10.1007/s00415-022-11418-y, doi:10.1007/s00415-022-11418-y. This article has 22 citations and is from a domain leading peer-reviewed journal.

22. (NCT05707663 chunk 1): Peggy C Nopoulos. Longitudinal Assessment of Brain Structure and Function in Juvenile-onset Huntington's Disease. University of Iowa. 2020. ClinicalTrials.gov Identifier: NCT05707663

23. (saft2023symptomatictreatmentoptions pages 1-2): Carsten Saft, Jean-Marc Burgunder, Matthias Dose, Hans Heinrich Jung, Regina Katzenschlager, Josef Priller, Huu Phuc Nguyen, Kathrin Reetz, Ralf Reilmann, Klaus Seppi, and Georg Bernhard Landwehrmeyer. Symptomatic treatment options for huntington’s disease (guidelines of the german neurological society). Neurological Research and Practice, Nov 2023. URL: https://doi.org/10.1186/s42466-023-00285-1, doi:10.1186/s42466-023-00285-1. This article has 37 citations and is from a peer-reviewed journal.

24. (NCT01590602 chunk 1):  REGISTRY-JHD - an Observational Study of the European Huntington's Disease Network (EHDN). European Huntington's Disease Network. 2011. ClinicalTrials.gov Identifier: NCT01590602

## Artifacts

- [Edison artifact artifact-00](Juvenile_Huntington_Disease-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 17 |
| Resolved | 17 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 17 |
| On topic | 10 |
| Off topic | 0 |

All extracted references resolved successfully.