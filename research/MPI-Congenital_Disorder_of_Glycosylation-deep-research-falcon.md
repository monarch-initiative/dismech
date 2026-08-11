---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-01T17:05:49.199439'
end_time: '2026-08-01T17:15:37.072549'
duration_seconds: 587.87
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: MPI-congenital disorder of glycosylation
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
  path: MPI-Congenital_Disorder_of_Glycosylation-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** MPI-congenital disorder of glycosylation
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **MPI-congenital disorder of glycosylation** covering all of the
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
- **Disease Name:** MPI-congenital disorder of glycosylation
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **MPI-congenital disorder of glycosylation** covering all of the
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


# MPI-congenital disorder of glycosylation (MPI-CDG): comprehensive disease-characteristics report

## Executive summary

MPI-CDG is an autosomal-recessive disorder of protein N-glycosylation caused by biallelic pathogenic variants in **MPI**, encoding mannose-phosphate isomerase. It is clinically distinctive among CDGs: gastrointestinal disease, congenital/developmental hepatic fibrosis, hypoglycemia—often hyperinsulinemic—and mixed coagulopathy predominate, while intellectual disability and primary neurologic impairment are usually absent. Oral D-mannose bypasses the metabolic block and commonly produces rapid improvement in diarrhea, protein-losing enteropathy, hypoglycemia, and coagulation abnormalities, but it does not reliably prevent progressive liver fibrosis or portal hypertension. Evidence remains dominated by case reports, small series, expert consensus, and approximately 35–52 published patients rather than controlled trials. (lu2023mannosephosphateisomerase pages 1-2, cechova2020consensusguidelinefor pages 4-6, cechova2020consensusguidelinefor pages 1-3, cechova2020consensusguidelinefor pages 19-20)

| Topic | Key facts | Ontology / IDs | Key sources |
|---|---|---|---|
| Identity / overview | MPI-congenital disorder of glycosylation (MPI-CDG) is a rare disorder of protein N-glycosylation caused by pathogenic variants in **MPI**; unlike many other CDGs, it is dominated by gastrointestinal, hepatic, endocrine, and coagulation manifestations, with usually no intellectual disability or major neurologic impairment. Former names include **CDG-Ib**, **CDG type Ib**, **carbohydrate-deficient glycoprotein syndrome type Ib**, **phosphomannose isomerase deficiency / mannose phosphate isomerase deficiency**, **protein-losing enteropathy-hepatic fibrosis syndrome**, and **Saguenay-Lac Saint-Jean syndrome**. | **OMIM:** 602579; MeSH in trial browse: “Congenital disorder of glycosylation type 1B”; suggested disease label: MPI-CDG | (cechova2020consensusguidelinefor pages 1-3, NCT03404869 chunk 1) |
| Inheritance / gene | **Autosomal recessive** disorder due to biallelic pathogenic variants in **MPI** on chromosome 15q. The MPI gene has **8 exons** and spans ~**5 kb**. | Suggested gene: **MPI**; inheritance: AR | (cechova2020consensusguidelinefor pages 1-3, cechova2020consensusguidelinefor pages 17-19) |
| Core mechanism | MPI catalyzes **fructose-6-phosphate ↔ mannose-6-phosphate**, the first step toward GDP-mannose synthesis for N-glycosylation. MPI deficiency lowers intracellular mannose availability; in patients, endogenous mannose is insufficient, leading to **protein N-hypoglycosylation**. Consensus guideline notes plasma mannose is **<10 μmol/L** in MPI-CDG vs **50–100 μmol/L** in healthy individuals; glycosylation can be normalized when serum mannose exceeds **~200 μmol/L**. Excess mannose can cause **Man-6-P accumulation**, glycolytic inhibition, ATP depletion, and neurologic toxicity (“honeybee effect”). | Suggested GO terms: **protein N-linked glycosylation**, **mannose metabolic process**; suggested CHEBI concept: **D-mannose** | (cechova2020consensusguidelinefor pages 3-4) |
| Typical onset / course | Symptoms begin in **infancy** in the large majority; consensus review found **93%** infantile onset with mean onset **1.2 years**, but adolescent presentations and asymptomatic adults have been reported. In the 2023 review, onset ranged **birth to 15 years**, with **43/50** cases starting before age 2. Diagnostic delay ranged **0–30 years** (median **2.15 years**). | Suggested onset terms: congenital/infantile; chronic multisystem course | (cechova2020consensusguidelinefor pages 4-6, lu2023mannosephosphateisomerase pages 1-2) |
| Hallmark phenotypes (2023 frequencies) | 2023 literature review of 52 patients reported: **chronic diarrhea 41/46**, **vomiting 23/27**, **hepatomegaly 39/44**, **hepatic fibrosis 20/37**, **protein-losing enteropathy 30/36**, **elevated transaminases 24/34**, **hyperinsulinemic hypoglycemia 24/34**, **hypoalbuminemia 33/38**, **prolonged coagulation 26/30**, **splenomegaly 13/21**, **non-pitting edema 14/20**, **failure to thrive 13/36**, **portal hypertension 4/9**, **epilepsy 2/17**, **thrombosis 12/14**, **elevated leukocytes 5**; **intellectual disability 0/28**. | Reliable phenotype suggestions: **hepatomegaly**, **diarrhea**, **vomiting**, **protein-losing enteropathy**, **hypoglycemia**, **hypoalbuminemia**, **hepatic fibrosis**, **portal hypertension**, **thrombosis** | (lu2023mannosephosphateisomerase pages 1-2, lu2023mannosephosphateisomerase pages 3-5) |
| Diagnostics | First-line biochemical screen: **serum/plasma transferrin isoelectric focusing (TIEF)** showing **CDG type I pattern** (decreased tetrasialotransferrin, increased disialo-/asialotransferrin); reported **100% sensitivity** in described genotyped patients, but non-specific vs other CDG-I disorders. **HPLC/capillary electrophoresis** for CDT% also reported **100% sensitivity** in described patients. Confirmation: **MPI enzyme assay** in fibroblasts/leukocytes or **MPI gene testing**; enzyme activity usually **<10%** of normal, though **14–21%** residual activity has been reported in some severe cases. Differential diagnosis includes **PMM2-CDG**, **galactosemia**, **hereditary fructose intolerance**, liver disease, chronic alcohol abuse, and other causes of hypoglycemia/PLE/hepatopathy. | Suggested lab/ontology terms: transferrin IEF, carbohydrate-deficient transferrin; gene: **MPI** | (cechova2020consensusguidelinefor pages 16-17, cechova2020consensusguidelinefor pages 17-19, cechova2020consensusguidelinefor pages 11-13, cechova2020consensusguidelinefor pages 10-11) |
| First-line treatment / dose | Standard disease-specific treatment is **oral D-mannose**. Consensus recommended dose: **150–170 mg/kg/dose, 4–5 times daily**. In the 2023 review, **26/30** treated patients improved clinically/laboratorily; symptoms in the index case resolved within **1 week**. Monitoring every 3 months during oral therapy includes **unconjugated bilirubin, blood count, HbA1C, and mannose levels**; target mannose levels suggested as **T0 >20 μmol/L** and **T1h >100 μmol/L**. | Suggested treatment term: **D-mannose**; NCIT suggestion only where available concept exists for mannose | (cechova2020consensusguidelinefor pages 19-20, lu2023mannosephosphateisomerase pages 2-3, lu2023mannosephosphateisomerase pages 5-6) |
| Key limitation / persistent liver disease | Mannose improves many clinical and biochemical abnormalities but **does not reliably halt liver disease**. Consensus guideline states patients may still develop **progressive liver fibrosis**, likely because characteristic lesions reflect **ductal plate malformation / congenital hepatic fibrosis**, which do not respond to mannose. Selected severe cases may require **liver transplantation**, especially for **portal hypertension with hepatopulmonary syndrome**. | Suggested anatomy: **liver**; suggested pathology: **hepatic fibrosis**, **portal hypertension** | (cechova2020consensusguidelinefor pages 8-10, cechova2020consensusguidelinefor pages 6-8) |
| Prognosis / mortality | Consensus review of 35 patients found **mortality 23.5% (8/35)**; all deaths occurred in infancy/early childhood at **4 months to 5 years** (median **2.2 years**). Causes, when known, included **hepatic failure (n=2)** and **sepsis (n=1)**; many deaths occurred before diagnosis/treatment. In the 2023 review, **8/11 untreated** patients died, supporting major benefit from timely diagnosis and mannose therapy. | Suggested outcome terms: mortality, hepatic failure, sepsis | (cechova2020consensusguidelinefor pages 4-6, lu2023mannosephosphateisomerase pages 5-6) |
| Clinical trial / implementation | **NCT03404869**: “**Study of ORL-1M (D-mannose) in Patients With CDG-Ib**,” sponsor **Orpha Labs**; **Phase 1/2**, single-group, open-label, estimated **n=5**; primary outcome: improvement in **hypoglycemia, diarrhea and vomiting** at **6 months**; secondary outcome: improved **serum transferrin glycosylation** at **30 days**. Registry overall status is currently listed **UNKNOWN**; last known status **RECRUITING**; first posted **2018-01-19**. | **NCT03404869** | (NCT03404869 chunk 1) |
| Animal / experimental models | **Zebrafish mpi morphants**: **13% residual Mpi activity** at 4 dpf, **50% embryonic lethality** by 4 dpf, and multisystem abnormalities in **82%** of survivors (small eyes, dysmorphic jaws, pericardial edema, small liver, curled tails); phenotypes were rescued by mannose **only if given before 24 hpf**. **Mouse models**: complete **Mpi knockout** is embryonic lethal; **hypomorphic mice** with patient-like residual activity appeared largely normal but had ~**15% embryonic lethality**. Mannose exposure worsened outcomes, reducing litter size and survival to weaning by **40%** and **66%**, respectively, and ~**50%** of survivors developed ocular defects/blindness, highlighting species-specific toxicity and caution in pregnancy. | Suggested model systems: **Danio rerio**, **Mus musculus** | (chu2013azebrafishmodel pages 1-2, sharma2014mannosesupplementsinduce pages 1-2, brasil2018cdgtherapiesfrom pages 3-4) |


*Table: This table condenses the most actionable disease-characterization points for MPI-CDG, including identity, mechanism, phenotype frequencies, diagnosis, treatment, prognosis, trial activity, and model systems. It is formatted for direct use in a disease knowledge-base entry and cites the supporting evidence contexts.*

## Evidence scope and recency

The most disease-specific authoritative source is the international consensus guideline by Čechová et al., accepted April 3, 2020 and published in *Journal of Inherited Metabolic Disease* 43:671–693, DOI [10.1002/jimd.12241](https://doi.org/10.1002/jimd.12241). It combined a systematic review with opinions from 21 experts across nine countries; the authors emphasized that most evidence was low-level because it consisted of case reports and case series. The newest detailed synthesis retrieved was Lu et al., published April 2023 in *Frontiers in Pediatrics*, DOI [10.3389/fped.2023.1150367](https://doi.org/10.3389/fped.2023.1150367), which reviewed 52 reported patients from 17 countries. No MPI-CDG-specific 2024 natural-history cohort, randomized trial, single-cell study, or spatial-omics study was identified in the retrieved literature. (lu2023mannosephosphateisomerase pages 1-2, cechova2020consensusguidelinefor pages 3-4, cechova2020consensusguidelinefor pages 1-3)

---

## 1. Disease information

### Definition and identifiers

MPI-CDG is a Mendelian disorder of protein N-glycosylation caused by deficient mannose-phosphate isomerase activity. The consensus guideline explicitly describes it as “a rare subtype of congenital disorders of protein N-glycosylation” characterized by pathogenic **MPI** variants and dominant gastrointestinal and hepatic involvement without the usual intellectual or neurologic impairment seen in many CDGs. (cechova2020consensusguidelinefor pages 1-3)

* **OMIM phenotype:** **602579**.
* **Gene:** **MPI**, chromosome 15q; eight exons spanning approximately 5 kb.
* **MeSH/ClinicalTrials.gov browse term:** “Congenital disorder of glycosylation type 1B,” MeSH C535740.
* **MONDO:** A specific MONDO identifier was not verified in the retrieved source text and should therefore be resolved directly against the current MONDO release before database deposition.
* **Orphanet:** A disease-specific ORPHA number was not verified in the retrieved evidence.
* **ICD-10/ICD-11:** No uniquely disease-specific code was established in the retrieved sources; MPI-CDG is generally captured under broader congenital glycosylation/metabolic-disorder categories.

Synonyms include **CDG-Ib**, **CDG1B**, **congenital disorder of glycosylation type Ib**, **carbohydrate-deficient glycoprotein syndrome type Ib**, **phosphomannose isomerase deficiency**, **mannose-phosphate isomerase deficiency**, **protein-losing enteropathy–hepatic fibrosis syndrome**, and **Saguenay–Lac-Saint-Jean syndrome**. (cechova2020consensusguidelinefor pages 3-4, cechova2020consensusguidelinefor pages 1-3, NCT03404869 chunk 1)

### Provenance

This entry is based on aggregated disease-level resources, published case reports/series, an international expert guideline, and a trial registry—not individual-level EHR data. The 2023 frequencies are literature-derived denominators that vary by phenotype because not every feature was assessed in every patient. (lu2023mannosephosphateisomerase pages 3-5, lu2023mannosephosphateisomerase pages 1-2)

---

## 2. Etiology, risk, protective factors, and gene–environment interaction

### Primary cause

The sole established primary cause is **biallelic germline loss-of-function/hypomorphic variation in MPI**. MPI catalyzes fructose-6-phosphate ↔ mannose-6-phosphate; reduced activity limits mannose-6-phosphate and downstream GDP-mannose availability for lipid-linked oligosaccharide synthesis and N-glycosylation. Pathogenic alleles are predominantly missense variants, consistent with survival requiring residual activity. (cechova2020consensusguidelinefor pages 3-4, cechova2020consensusguidelinefor pages 17-19)

### Genetic risk factors

Risk is highest for a child inheriting one pathogenic allele from each carrier parent. Among 28 genotyped published patients in the 2020 review, 13 were homozygous; parental consanguinity was reported for nine patients. Twenty pathogenic variants comprised 17 missense variants, two frameshift-causing variants, and one splice defect. (cechova2020consensusguidelinefor pages 17-19)

Potentially mild **p.Arg219Gln** homozygosity was observed in two asymptomatic adults, suggesting incomplete penetrance or substantial modifier effects. However, neither residual enzyme activity nor carbohydrate-deficient transferrin reliably predicted clinical severity, and no validated modifier gene is known. (cechova2020consensusguidelinefor pages 17-19)

### Environmental and protective factors

There are no established toxins, infections, lifestyle exposures, age, or sex factors that cause MPI-CDG. Exogenous dietary mannose is protective at the biochemical level because it bypasses the endogenous MPI-dependent route. Conversely, dehydration and acute infection can precipitate hypoglycemia and destabilize the mixed coagulation defect, increasing thrombosis risk. Alcohol and hepatotoxic drugs can add secondary liver injury and should be avoided. (cechova2020consensusguidelinefor pages 8-10, cechova2020consensusguidelinefor pages 13-14)

A clinically important gene–environment interaction is **dose-dependent mannose rescue versus toxicity**. Therapeutic oral mannose restores substrate for glycosylation, but excessive intracellular mannose-6-phosphate can inhibit hexokinase, phosphoglucose isomerase, and glucose-6-phosphate dehydrogenase, reduce glycolytic flux, deplete ATP, and cause energy failure—the “honeybee effect.” Pregnancy exposure warrants caution because adverse developmental effects occurred in MPI-deficient mice, although comparable human teratogenicity has not been demonstrated. (cechova2020consensusguidelinefor pages 3-4, sharma2014mannosesupplementsinduce pages 1-2)

No validated protective variant, environmental prevention strategy, or lifestyle measure prevents disease occurrence in a person with a disease-causing biallelic genotype.

---

## 3. Phenotypes

### Quantitative clinical spectrum

The 2023 review reported the following frequencies: chronic diarrhea **41/46 (89%)**; vomiting **23/27 (85%)**; hepatomegaly **39/44 (89%)**; hepatic fibrosis **20/37 (54%)**; protein-losing enteropathy **30/36 (83%)**; elevated transaminases **24/34 (71%)**; hyperinsulinemic hypoglycemia **24/34 (71%)**; hypoalbuminemia **33/38 (87%)**; prolonged coagulation **26/30 (87%)**; splenomegaly **13/21 (62%)**; non-pitting edema **14/20 (70%)**; failure to thrive **13/36 (36%)**; portal hypertension **4/9 (44%)**; epilepsy/seizures **2/17 (12%)**; thrombosis **12/14 (86%)**; and intellectual disability **0/28**. These proportions may be enriched by reporting and ascertainment bias and should not be interpreted as population prevalence. (lu2023mannosephosphateisomerase pages 3-5, lu2023mannosephosphateisomerase pages 1-2)

### Phenotype characterization and ontology suggestions

* **Chronic or cyclic diarrhea/vomiting:** usually infantile, recurrent or episodic, ranging from moderate to life-threatening dehydration; often the presenting feature. Suggested HPO: **Diarrhea HP:0002014**, **Vomiting HP:0002013**. It causes recurrent admissions, feeding difficulty, and major family burden. (cechova2020consensusguidelinefor pages 8-10, cechova2020consensusguidelinefor pages 10-11)
* **Protein-losing enteropathy:** infantile and fluctuating, causing hypoalbuminemia, edema, malnutrition, and sometimes hypogammaglobulinemia. Stool alpha-1-antitrypsin may be 3- to 20-fold elevated. Suggested HPO: **Protein-losing enteropathy HP:0002243**, **Hypoalbuminemia HP:0003073**, **Edema HP:0000969**. (cechova2020consensusguidelinefor pages 10-11)
* **Failure to thrive/growth restriction:** typically secondary to enteropathy, vomiting, and hypoglycemia; approximately two-thirds in the older consensus dataset but 13/36 in the expanded 2023 review. Suggested HPO: **Failure to thrive HP:0001508**, **Growth delay HP:0001510**. (lu2023mannosephosphateisomerase pages 1-2, cechova2020consensusguidelinefor pages 10-11)
* **Hepatomegaly, fibrosis, and portal hypertension:** chronic and potentially progressive despite therapy. Fibrosis may produce splenomegaly, thrombocytopenia, esophageal varices, hepatopulmonary syndrome, and variceal hemorrhage. Suggested HPO: **Hepatomegaly HP:0002240**, **Hepatic fibrosis HP:0001395**, **Portal hypertension HP:0001409**, **Splenomegaly HP:0001744**. (cechova2020consensusguidelinefor pages 6-8, cechova2020consensusguidelinefor pages 8-10)
* **Transaminase elevation:** commonly 1.5–5 times the upper limit, but as high as 30–40-fold during acute decompensation; bilirubin and GGT are often normal. Suggested HPO: **Elevated hepatic transaminase HP:0002910**. (cechova2020consensusguidelinefor pages 6-8)
* **Hypoglycemia/hyperinsulinism:** onset from the perinatal period through three years, mean 6.8 months in the consensus review; severity ranges from asymptomatic biochemical hypoglycemia to apnea, unresponsiveness, or seizures. Suggested HPO: **Hypoglycemia HP:0001943**, **Hyperinsulinemic hypoglycemia HP:0000825**. (cechova2020consensusguidelinefor pages 11-13)
* **Mixed coagulopathy:** almost constant in the consensus experience; commonly low antithrombin, protein C, factor XI, and sometimes protein S. It can produce both thrombosis and bleeding in the same patient. Suggested HPO: **Abnormality of coagulation HP:0001928**, **Thrombosis HP:0001977**, and **Gastrointestinal hemorrhage HP:0002239**. (cechova2020consensusguidelinefor pages 11-13, cechova2020consensusguidelinefor pages 13-14)
* **Neurologic findings:** primary neurologic disease is atypical. Mild developmental delay was reported in four cases and hypotonia in five; seizures were secondary to hypoglycemia, cerebral thrombosis, fever, or intravenous-mannose toxicity. Brain imaging was normal in ten reported patients, without cerebellar hypoplasia. Suggested HPO only when present: **Global developmental delay HP:0001263**, **Hypotonia HP:0001252**, **Seizure HP:0001250**. (cechova2020consensusguidelinefor pages 13-14)
* **Renal/cardiac/immune findings:** renal echogenicity, nephromegaly, cysts, or tubular acidosis occurred sporadically; one severe patient had hypertrophic cardiomyopathy. Recurrent unusual infections and PLE-related hypogammaglobulinemia occur, but a primary MPI-specific immunodeficiency is unproven. (cechova2020consensusguidelinefor pages 14-16)

Formal EQ-5D, SF-36, PROMIS, or disease-specific quality-of-life measurements were not identified. Nonetheless, recurrent admissions, diarrhea, hypoglycemia surveillance, bleeding/thrombosis risk, and four-to-five-times-daily mannose dosing clearly affect daily function and treatment burden.

---

## 4. Genetic and molecular information

### Gene and protein

**MPI** encodes a mainly cytosolic enzyme that can also localize to the plasma membrane. The enzyme initiates endogenous mannose production by interconverting fructose-6-phosphate and mannose-6-phosphate. The disorder results from reduced enzymatic function, not a gain-of-function or dominant-negative mechanism. (cechova2020consensusguidelinefor pages 3-4)

### Variant spectrum

In the 2020 consensus dataset, three recurrent missense variants accounted for approximately half of known alleles:

* **c.656G>A (p.Arg219Gln): 12 alleles; 21.4%**.
* **c.457G>A (p.Arg152Gln): 9 alleles; 16.1%**.
* **c.884G>A (p.Arg295His): 8 alleles; 14.3%**.

Other reported variants included p.Ile398Thr, p.Ser102Leu, p.Met138Thr, p.Met51Thr, p.Asp131Asn, p.Ile140Thr, p.Ala288Val, p.Gln14Pro, p.Arg56fs, p.Tyr129Cys, p.Glu156Lys, c.488-1G>C, p.Gly250Ser, p.Tyr255Cys, p.Gly281del, p.Arg418His, and p.Arg418Cys. The 2023 case added compound heterozygous **c.455G>T (p.Arg152Leu)**, classified as likely pathogenic, and **c.884G>A (p.Arg295His)**, classified as pathogenic. (lu2023mannosephosphateisomerase pages 2-3, cechova2020consensusguidelinefor pages 17-19)

These are constitutional germline variants. No somatic disease mechanism is established. Exact current ClinVar assertions and gnomAD allele frequencies should be retrieved variant-by-variant from live databases; the source set did not provide dependable contemporary population frequencies.

### Genotype–phenotype, modifiers, and epigenetics

Clinical severity is not reliably predicted by genotype, residual enzyme activity, or CDT value. Homozygous p.Arg219Gln may be mild or asymptomatic, but this observation rests on very few adults. No validated modifier gene, epigenetic signature, repeat expansion, aneuploidy, recurrent copy-number variant, or structural chromosomal cause is established. (cechova2020consensusguidelinefor pages 17-19)

Suggested molecular ontology: **GO:0006487 protein N-linked glycosylation**, **GO:0009298 GDP-mannose biosynthetic process** where applicable, **GO:0005975 carbohydrate metabolic process**, and MPI enzyme activity/mannose-6-phosphate isomerase activity. Database curators should validate exact GO identifiers against the current release.

---

## 5. Environmental, lifestyle, and infectious information

MPI-CDG is not caused by pollution, radiation, occupational exposure, smoking, alcohol, diet, or infection. Acute gastrointestinal infection, poor intake, dehydration, surgery, and fasting can nevertheless trigger metabolic and hemostatic decompensation. Alcohol and hepatotoxic medications are avoidable secondary insults in a disease with progressive liver vulnerability. Hepatitis A and B vaccination is recommended to prevent additional hepatic injury. (cechova2020consensusguidelinefor pages 11-13, cechova2020consensusguidelinefor pages 8-10)

No infectious agent is etiologic, and the disease is neither contagious nor zoonotic.

---

## 6. Mechanism and pathophysiology

### Upstream causal chain

1. **Biallelic hypomorphic MPI variants** reduce mannose-phosphate isomerase activity.
2. Conversion of **fructose-6-phosphate to mannose-6-phosphate** falls.
3. GDP-mannose and lipid-linked oligosaccharide supply become insufficient.
4. Nascent secretory and membrane proteins receive too few N-glycan chains.
5. Hypoglycosylated proteins have altered folding, stability, trafficking, secretion, or function.
6. Tissue-specific consequences emerge in enterocytes, hepatocytes/biliary developmental structures, pancreatic beta-cell physiology, vascular/hemostatic proteins, and endocrine transport proteins. (cechova2020consensusguidelinefor pages 3-4, chu2013azebrafishmodel pages 1-2)

Plasma mannose was reported as **<10 μmol/L** in MPI-CDG versus **50–100 μmol/L** in controls. Serum mannose above approximately **200 μmol/L** can normalize glycosylation experimentally/clinically, explaining the substrate-bypass treatment. (cechova2020consensusguidelinefor pages 3-4)

### Downstream organ mechanisms

* **Intestine:** reduced glycoproteins on enterocyte membranes and/or intestinal lymphangiectasia compromise barrier integrity, causing protein leakage, hypoalbuminemia, edema, immunoglobulin loss, and malnutrition. Suggested cells: **enterocyte (CL:0000584)**; processes: epithelial barrier maintenance, protein absorption, glycoprotein biosynthesis. (cechova2020consensusguidelinefor pages 10-11)
* **Liver/biliary tract:** the characteristic lesion resembles congenital hepatic fibrosis with ductal-plate configuration and von Meyenburg complexes. This likely represents a developmental malformation, explaining why fibrosis and portal hypertension can progress even after systemic biochemical rescue. Suggested cells include **hepatocyte (CL:0000182)** and **cholangiocyte**; processes include bile-duct morphogenesis, extracellular-matrix organization, and fibrosis. (cechova2020consensusguidelinefor pages 6-8, cechova2020consensusguidelinefor pages 8-10)
* **Pancreatic endocrine system:** hyperinsulinism may reflect hypoglycosylation of membrane proteins such as SUR1, but the exact mechanism remains uncertain. In vitro murine beta-cell evidence shows that hypoglycosylation can alter insulin secretion. Suggested cell: **pancreatic beta cell (CL:0000169)**. (cechova2020consensusguidelinefor pages 11-13)
* **Hemostasis:** hypoglycosylation reduces abundance/stability of antithrombin, protein C, factor XI, and protein S; increased platelet aggregation may compound the imbalance. Infection, dehydration, PLE, and hepatic dysfunction further destabilize hemostasis. (cechova2020consensusguidelinefor pages 11-13, cechova2020consensusguidelinefor pages 13-14)
* **Endocrine transport/growth:** hypoglycosylated IGFBP-3, acid-labile subunit, and thyroxine-binding globulin can contribute to growth restriction and abnormal laboratory hormone values. (cechova2020consensusguidelinefor pages 11-13, cechova2020consensusguidelinefor pages 10-11)

### Subcellular and metabolic localization

MPI acts predominantly in the **cytosol** upstream of endoplasmic-reticulum N-glycan assembly. Relevant compartments are cytosol, ER membrane/lumen, secretory pathway, and plasma membrane. Suggested GO cellular components include cytosol and endoplasmic reticulum.

### Molecular profiling and advanced technologies

Transferrin glycoform profiling is the principal disease biomarker. A 2021 longitudinal study of 32 CDG patients, including three with MPI-CDG, found that mannose in two MPI-CDG patients significantly lowered asialo-, monosialo-, and disialotransferrin while increasing tetra- and pentasialotransferrin toward reference ranges. (bogdanska2021clinicalbiochemicaland pages 1-2)

No robust MPI-CDG-specific transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, CRISPR-screen, or integrated multi-omics signature was identified. This is an important research gap rather than evidence of absence.

---

## 7. Anatomical structures affected

### Primary organs and tissues

* **Small intestine and gastrointestinal tract:** enterocyte surface and intestinal lymphatics; UBERON suggestions: small intestine, duodenum, intestinal epithelium.
* **Liver and intrahepatic bile ducts:** portal tracts, ductal plate, biliary structures, and hepatic vasculature; UBERON: liver **UBERON:0002107** and bile duct.
* **Pancreatic islets:** beta-cell insulin regulation; UBERON: endocrine pancreas/pancreatic islet.
* **Blood and vascular system:** circulating glycoproteins, platelets, and venous vasculature.

Secondary involvement includes spleen from portal hypertension; esophagus through varices; lung through hepatopulmonary syndrome; brain secondary to hypoglycemia or thrombosis; kidney and heart in occasional cases. There is no characteristic lateralization. (cechova2020consensusguidelinefor pages 6-8, cechova2020consensusguidelinefor pages 11-13, cechova2020consensusguidelinefor pages 14-16, cechova2020consensusguidelinefor pages 13-14)

At the subcellular level, the initial metabolic block is cytosolic, whereas the glycan-assembly consequence is expressed in the ER/secretory pathway and on secreted or cell-surface glycoproteins.

---

## 8. Temporal development

Symptoms begin in infancy in **93%** of patients in the 2020 review, with mean onset at **1.2 years**. The 2023 expanded review found onset from birth to age 15 and onset before age two in **43/50**. Two adolescent presentations and asymptomatic adults into their early forties demonstrate very variable expressivity. (lu2023mannosephosphateisomerase pages 1-2, cechova2020consensusguidelinefor pages 4-6)

The gastrointestinal and hypoglycemic course is often episodic, with infection, fasting, or dehydration producing exacerbations. Mannose usually improves clinical symptoms within approximately one week, while biochemical stabilization takes months. Hepatic fibrosis is chronic and can remain progressive despite correction of extrahepatic features. (cechova2020consensusguidelinefor pages 8-10, cechova2020consensusguidelinefor pages 19-20)

There is no validated staging system. Pragmatic stages are: early gastrointestinal/endocrine presentation; established multisystem disease with PLE/coagulopathy; and advanced portal-hypertensive disease with varices or hepatopulmonary syndrome. Early diagnosis is the critical therapeutic window; animal evidence also suggests developmental timing matters, but the zebrafish pre-24-hour rescue window cannot be directly extrapolated to humans. (chu2013azebrafishmodel pages 1-2)

---

## 9. Inheritance and population

MPI-CDG is **autosomal recessive**. For two confirmed carriers, each pregnancy has a 25% probability of an affected child, 50% probability of a carrier child, and 25% probability of inheriting neither familial pathogenic allele. Anticipation is not expected. Germline mosaicism has not emerged as a characteristic mechanism, although low residual recurrence risk from parental mosaicism cannot be excluded generically.

The 2020 review included 35 patients from 30 families and described the disease as panethnic. The 2023 review found 52 patients across 17 countries. True prevalence, incidence, carrier frequency, and population-specific penetrance remain unknown. (lu2023mannosephosphateisomerase pages 1-2, cechova2020consensusguidelinefor pages 3-4, cechova2020consensusguidelinefor pages 4-6)

The 2020 sample included 18 females and nine males, with sex unspecified in eight; the authors considered the apparent 2:1 ratio likely due to small sample size rather than sex-biased biology. Consanguinity contributed to homozygosity in some families. Although “Saguenay–Lac-Saint-Jean syndrome” reflects an early regional cluster, no sufficiently quantified founder prevalence was retrieved. (cechova2020consensusguidelinefor pages 4-6, cechova2020consensusguidelinefor pages 17-19)

---

## 10. Diagnostics

### When to suspect MPI-CDG

Test children or adults with combinations of recurrent/cyclic diarrhea or vomiting, PLE/hypoalbuminemia, hepatomegaly or congenital hepatic fibrosis, hyperinsulinemic hypoglycemia, unexplained prolonged coagulation, low antithrombin/protein C/factor XI, thrombosis, or portal hypertension—especially when neurodevelopment is normal. (cechova2020consensusguidelinefor pages 1-3, cechova2020consensusguidelinefor pages 11-13, cechova2020consensusguidelinefor pages 10-11)

### Biochemical testing

1. **Serum/plasma transferrin isoelectric focusing:** preferred screen. The type-I pattern shows reduced tetrasialotransferrin and increased disialo- and asialotransferrin. Sensitivity was reported as 100% among described genotyped patients, but specificity is poor because PMM2-CDG and other CDG-I disorders are indistinguishable. (cechova2020consensusguidelinefor pages 14-16, cechova2020consensusguidelinefor pages 16-17)
2. **HPLC or capillary electrophoresis/CDT%:** quantitative alternatives, also reported as 100% sensitive in described cases. CDT can be 38–50% in severe disease versus 7–20% in oligo-/asymptomatic adults. (cechova2020consensusguidelinefor pages 16-17)
3. **MPI enzyme activity:** confirmatory testing in fresh leukocytes or fibroblasts. Most reported patients had <10% normal activity, although 14–21% occurred in some severe cases. Parental activity was typically intermediate, 30–83%, median 50%. (cechova2020consensusguidelinefor pages 16-17)
4. **Molecular confirmation:** sequence **MPI** by single-gene testing, a CDG/hypoglycemia/liver-disease panel, WES, or WGS. Sanger confirmation and parental segregation are appropriate. (cechova2020consensusguidelinefor pages 17-19)

WES diagnosed the 2023 index case and is useful for atypical disease. WGS may detect noncoding or structural alleles missed by exon-focused assays, but disease-specific diagnostic-yield data are unavailable. CMA, karyotyping, FISH, mitochondrial sequencing, and repeat-expansion testing are not routine tests because MPI-CDG is usually a small-sequence-variant disorder.

### False positives and differential diagnosis

Transferrin variants, sample contamination by neuraminidase-producing microorganisms, untreated galactosemia, hereditary fructose intolerance, severe infection, chronic liver disease, and alcohol exposure can produce abnormal transferrin patterns. Repeat testing on an independent sample, neuraminidase treatment, and parental transferrin analysis can resolve some ambiguities. (cechova2020consensusguidelinefor pages 14-16, cechova2020consensusguidelinefor pages 16-17)

Clinical differentials include PMM2-CDG; PGM1-, ALG6-, TMEM199-, CCDC115-, and ATP6AP1-CDG; celiac disease; intestinal lymphangiectasia; inflammatory/infectious enteropathy; glycogen storage disease; fatty-acid oxidation disorders; galactosemia; hereditary fructose intolerance; congenital hyperinsulinism; alpha-1-antitrypsin deficiency; Wilson disease; cystic fibrosis; congenital hepatic fibrosis/ARPKD; and other metabolic liver disorders. (cechova2020consensusguidelinefor pages 6-8, cechova2020consensusguidelinefor pages 11-13, cechova2020consensusguidelinefor pages 10-11)

### Surveillance after diagnosis

Consensus recommendations include liver chemistry, AFP, prothrombin time, and ultrasound every six months; annual elastography when transaminases remain elevated; annual endoscopy initially in portal hypertension and thereafter at least every three years; albumin every three months during active PLE; glucose monitoring and critical hypoglycemia samples; annual broad hemostasis testing; and annual thyroid/IGF-axis, renal, immune, developmental, and nutritional assessment as clinically indicated. (cechova2020consensusguidelinefor pages 6-8, cechova2020consensusguidelinefor pages 4-6, cechova2020consensusguidelinefor pages 11-13)

### Screening

MPI-CDG is not a standard population newborn-screening condition. The Early Check trial retrieved in the search was broad expanded newborn screening and does not establish routine MPI-CDG screening. Cascade testing, carrier testing, prenatal diagnosis, and preimplantation genetic testing are feasible once familial variants are known.

---

## 11. Outcome and prognosis

In the 2020 review, mortality was **23.5% (8/35)**. All deaths occurred between four months and five years, median 2.2 years; known causes included hepatic failure in two and sepsis in one. Six of eight died before the disorder and mannose treatment were recognized. The 2023 review found **8/11 untreated patients died**, compared with improvement in **26/30 treated patients**. These uncontrolled comparisons strongly favor early treatment but are vulnerable to era, severity, and publication bias. (lu2023mannosephosphateisomerase pages 5-6, cechova2020consensusguidelinefor pages 4-6)

Survival into adulthood, normal pregnancy, and even asymptomatic adulthood are documented. No reliable five- or ten-year survival curve or life-expectancy estimate exists. Prognosis is driven by timeliness of diagnosis, severity of PLE and hypoglycemia, infection/dehydration exposure, thrombosis/bleeding, and especially progression of congenital hepatic fibrosis and portal hypertension. (cechova2020consensusguidelinefor pages 4-6, cechova2020consensusguidelinefor pages 10-11, cechova2020consensusguidelinefor pages 17-19)

Mannose offers substantial recovery potential for gastrointestinal, endocrine, and coagulation abnormalities, but established ductal-plate malformation and fibrosis may be irreversible. Formal disability and quality-of-life datasets are absent.

---

## 12. Treatment

### Oral D-mannose: standard disease-specific therapy

The consensus dose is **150–170 mg/kg per dose orally four to five times daily**, started as soon as diagnosis is made. Oral mannose enters a complementary pathway through hexokinase to form mannose-6-phosphate, bypassing deficient MPI. Clinical response often begins within a week; biochemical abnormalities may take months to stabilize. In the 2023 case, diarrhea and vomiting resolved completely within one week without reported adverse effects. (lu2023mannosephosphateisomerase pages 2-3, cechova2020consensusguidelinefor pages 11-13, cechova2020consensusguidelinefor pages 19-20)

**Effects:** regression of diarrhea, vomiting, PLE, hypoalbuminemia, hypoglycemia, and coagulopathy; improved growth and transferrin glycosylation. In the 2023 synthesis, 26/30 treated patients improved. However, abnormal transferrin profiles rarely normalize completely, and liver fibrosis may progress. (lu2023mannosephosphateisomerase pages 5-6, cechova2020consensusguidelinefor pages 8-10, cechova2020consensusguidelinefor pages 16-17, bogdanska2021clinicalbiochemicaland pages 1-2)

**Monitoring:** every three months, assess unconjugated bilirubin, CBC, HbA1C, and mannose. Suggested targets are trough/T0 >20 μmol/L and one-hour/T1 >100 μmol/L. Abdominal pain and diarrhea occurred in approximately 40% and usually improved spontaneously or after dose adjustment. (cechova2020consensusguidelinefor pages 19-20)

Suggested annotations: CHEBI **D-mannose**; NCIT intervention concept **Mannose** or **Dietary Supplementation**, subject to terminology-service validation.

### Intravenous mannose

Not recommended for stable disease. It may be considered only in life-threatening situations when oral treatment is impossible, using continuous infusion up to **1 g/kg/day** with individualized IV glucose. Severe hemolysis occurred in one patient and seizures/stupor in another; daily neurologic, bilirubin, CBC, and hexosuria monitoring is required. (cechova2020consensusguidelinefor pages 8-10, cechova2020consensusguidelinefor pages 19-20, cechova2020consensusguidelinefor pages 17-19)

### Hypoglycemia management

Frequent feeding and complex carbohydrate supplementation are useful. Acute illness, perioperative fasting, or inability to feed requires continuous IV glucose to maintain glucose above 4 mmol/L; severe episodes target 4–6 mmol/L. Confirmed hyperinsulinism may require diazoxide **4–15 mg/kg/day** in three or four divided doses. (cechova2020consensusguidelinefor pages 11-13, cechova2020consensusguidelinefor pages 8-10)

### Gastrointestinal and nutritional support

Severe malnutrition may require enteral tube feeding or parenteral nutrition. Albumin infusion can bridge severe PLE with edema; the consensus table specifies 20% albumin when serum albumin is <2 g/dL. Immunoglobulin replacement may be used for significant PLE-related hypogammaglobulinemia. Experimental heparin improved PLE in one report but carries bleeding risk and is not routine disease-modifying treatment. (cechova2020consensusguidelinefor pages 8-10, cechova2020consensusguidelinefor pages 10-11)

### Coagulation management

Mannose usually corrects coagulation abnormalities within weeks. Treat thrombosis with unfractionated or low-molecular-weight heparin; vitamin-K antagonists require caution in patients with ulcers or varices. Severe bleeding may require local control and fresh frozen plasma. Factor XI concentrate and recombinant factor VIIa are discouraged because of thrombosis risk. Perioperative plans should be individualized with hematology input. (cechova2020consensusguidelinefor pages 13-14)

### Liver-directed treatment

Monitor and treat varices and portal-hypertensive complications according to standard hepatology practice. **Liver transplantation** is an option for selected patients with liver failure or portal hypertension with hepatopulmonary syndrome. In the reported transplant recipient, pulmonary function, coagulation, and transferrin IEF normalized, but extrahepatic MPI deficiency persisted. (cechova2020consensusguidelinefor pages 6-8, cechova2020consensusguidelinefor pages 8-10)

Suggested NCIT concepts include **Liver Transplantation**, **Parenteral Nutrition**, **Albumin Infusion**, **Diazoxide**, **Heparin**, and **Glucose Infusion**, with exact codes requiring current NCIT validation.

### Experimental and advanced therapy

No approved gene, RNA, genome-editing, enzyme-replacement, or cell therapy was identified. **NCT03404869**, “Study of ORL-1M (D-mannose) in Patients With CDG-Ib,” is a Phase 1/2, open-label, single-group study with estimated enrollment of five participants younger than 18. The primary endpoint was improvement in hypoglycemia, diarrhea, and vomiting at six months; the secondary endpoint was transferrin-glycosylation improvement at 30 days. It started March 31, 2015, was first posted January 19, 2018, and is currently listed as **unknown status**, last known recruiting. No posted results were retrieved. Registry URL: [ClinicalTrials.gov NCT03404869](https://clinicaltrials.gov/study/NCT03404869). (NCT03404869 chunk 1)

---

## 13. Prevention

Primary prevention of disease in an already conceived affected individual is not available because the cause is inherited. Reproductive prevention options include carrier testing for relatives, genetic counseling, prenatal diagnosis, and preimplantation genetic testing once familial variants are established.

Secondary prevention centers on early recognition and prompt mannose therapy before severe PLE, hypoglycemic brain injury, thrombosis, or irreversible portal-hypertensive complications. There is no established population newborn screen.

Tertiary prevention includes avoiding fasting and dehydration; sick-day glucose plans; rapid treatment of infection; regular liver, glucose, nutrition, and coagulation surveillance; thromboprophylaxis in appropriate high-risk settings; hepatitis A/B vaccination; alcohol abstinence; avoidance of hepatotoxic drugs; and screening/treatment of esophageal varices. (cechova2020consensusguidelinefor pages 6-8, cechova2020consensusguidelinefor pages 8-10, cechova2020consensusguidelinefor pages 13-14)

No MPI-CDG-specific vaccine, public-health sanitation measure, or environmental remediation is applicable.

---

## 14. Other species and natural disease

No naturally occurring MPI-CDG-equivalent veterinary disease in a defined companion-animal breed or wildlife population was established in the retrieved evidence. Accordingly, no VBO breed annotation is justified. There is no transmission or zoonotic potential.

The MPI pathway is evolutionarily conserved from fungi and invertebrates to fish, mice, and humans, but comparative observations such as natural mannose toxicity in honeybees are mechanistic analogies rather than homologous clinical disease. Suggested taxa for experimental evidence are **Homo sapiens NCBI:9606**, **Mus musculus NCBI:10090**, and **Danio rerio NCBI:7955**.

---

## 15. Model organisms and experimental systems

### Mouse

Complete **Mpi** knockout causes embryonic death around E11.5 with placental and embryonic abnormalities; mannose cannot rescue it because toxic mannose-6-phosphate accumulates and inhibits ATP production. This model demonstrates developmental essentiality but poorly reproduces viable human hypomorphic disease. (sharma2014mannosesupplementsinduce pages 1-2, cechova2020consensusguidelinefor pages 20-21)

A patient-relevant hypomorphic mouse had near-patient residual activity and appeared mostly normal, apart from approximately **15% embryonic lethality**. Providing pregnant dams 1–2% mannose reduced litter size by **40%** and survival to weaning by **66%**; **50% of survivors** developed eye defects. Starting mannose after eye development avoided ocular toxicity. These findings support a developmental window and pregnancy caution, but the lack of human-like liver/intestinal disease and species-specific mannose sensitivity limit translational generalization. The paper was published in January 2014, *FASEB Journal* 28:1854–1869, DOI [10.1096/fj.13-245514](https://doi.org/10.1096/fj.13-245514). (sharma2014mannosesupplementsinduce pages 1-2)

### Zebrafish

Morpholino-mediated **mpi** depletion generated **13% residual Mpi activity** at four days post-fertilization, reduced lipid-linked oligosaccharides and N-glycans, **50% embryonic lethality**, and abnormalities in **82% of surviving larvae**, including small eyes, dysmorphic jaws, pericardial edema, small liver, and curled tails. Mannose rescued the phenotype only when provided before 24 hours post-fertilization. The model is useful for developmental timing, glycan biochemistry, and treatment screening, but transient morpholino knockdown and embryonic phenotypes do not reproduce chronic human portal-hypertensive disease. Published in 2013, *Disease Models & Mechanisms* 6:95–105, DOI [10.1242/dmm.010116](https://doi.org/10.1242/dmm.010116). (chu2013azebrafishmodel pages 1-2)

### Cellular models

Patient fibroblasts and fresh leukocytes are used for enzyme activity and mannose-rescue studies. They reproduce reduced MPI activity and glycosylation but cannot model multicellular intestinal leakage, ductal-plate malformation, portal hypertension, or whole-body hypoglycemia. No MPI-CDG iPSC, organoid, humanized mouse, or validated CRISPR knock-in model with comprehensive human phenotype recapitulation was identified.

---

## Key expert interpretation and research priorities

The international consensus is that oral mannose is strongly indicated despite low formal evidence grades because the biochemical rationale, rapid within-patient response, long clinical experience, and untreated mortality are compelling. The most consequential misconception is that biochemical correction equals cure: MPI-CDG remains a progressive hepatic disorder in some patients because congenital ductal-plate pathology appears mannose-insensitive. (cechova2020consensusguidelinefor pages 8-10, cechova2020consensusguidelinefor pages 19-20)

Priorities for 2025-era research include an international prospective natural-history registry; validated patient-reported outcomes; current variant-level ClinVar/gnomAD curation; pharmacokinetic optimization or sustained-release mannose; pregnancy safety data; biomarkers predicting fibrosis and portal hypertension; liver/intestinal organoids; and controlled studies separating mannose-responsive systemic hypoglycosylation from mannose-resistant developmental liver pathology.

## Selected direct source quotations

* Čechová et al. 2020: “The manifestation of MPI-CDG is different from other CDGs as the patients suffer dominantly from gastrointestinal and hepatic involvement whereas they usually do not present intellectual disability or neurological impairment.” DOI [10.1002/jimd.12241](https://doi.org/10.1002/jimd.12241). (cechova2020consensusguidelinefor pages 1-3)
* Lu et al. 2023: after mannose initiation, “the vomiting and diarrhea symptoms disappeared completely” within one week. DOI [10.3389/fped.2023.1150367](https://doi.org/10.3389/fped.2023.1150367). (lu2023mannosephosphateisomerase pages 1-2)
* Chu et al. 2013: mannose restored glycosylation and rescued zebrafish abnormalities, but “mannose was only effective if provided prior to 24 hpf.” DOI [10.1242/dmm.010116](https://doi.org/10.1242/dmm.010116). (chu2013azebrafishmodel pages 1-2)
* Bogdańska et al. 2021: “Mannose supplementation in MPI-CDG patients… improved patients’ clinical picture and Tf isoform profiles.” DOI [10.1186/s13023-020-01657-5](https://doi.org/10.1186/s13023-020-01657-5). (bogdanska2021clinicalbiochemicaland pages 1-2)

**Evidence caveat:** Exact PMIDs were not consistently exposed in the retrieved full-text records. DOIs and registry URLs are therefore supplied where verified; PMIDs should be added through a live PubMed cross-check before final production database release.

References

1. (lu2023mannosephosphateisomerase pages 1-2): Siliang Lu, Shuheng Liang, Yi Wu, Jinyi Liu, Lin Lin, Guosheng Huang, and Huaijun Ning. Mannose phosphate isomerase gene mutation leads to a congenital disorder of glycosylation: a rare case report and literature review. Frontiers in Pediatrics, Apr 2023. URL: https://doi.org/10.3389/fped.2023.1150367, doi:10.3389/fped.2023.1150367. This article has 8 citations.

2. (cechova2020consensusguidelinefor pages 4-6): Anna Čechová, Ruqaiah Altassan, Delphine Borgel, Arnaud Bruneel, Joana Correia, Muriel Girard, Annie Harroche, Beata Kiec‐Wilk, Klaus Mohnike, Tiffany Pascreau, Łukasz Pawliński, Silvia Radenkovic, Sandrine Vuillaumier‐Barrot, Luis Aldamiz‐Echevarria, Maria Luz Couce, Esmeralda G. Martins, Dulce Quelhas, Eva Morava, Pascale de Lonlay, Peter Witters, and Tomáš Honzík. Consensus guideline for the diagnosis and management of mannose phosphate isomerase‐congenital disorder of glycosylation. Journal of Inherited Metabolic Disease, 43:671-693, Apr 2020. URL: https://doi.org/10.1002/jimd.12241, doi:10.1002/jimd.12241. This article has 73 citations and is from a peer-reviewed journal.

3. (cechova2020consensusguidelinefor pages 1-3): Anna Čechová, Ruqaiah Altassan, Delphine Borgel, Arnaud Bruneel, Joana Correia, Muriel Girard, Annie Harroche, Beata Kiec‐Wilk, Klaus Mohnike, Tiffany Pascreau, Łukasz Pawliński, Silvia Radenkovic, Sandrine Vuillaumier‐Barrot, Luis Aldamiz‐Echevarria, Maria Luz Couce, Esmeralda G. Martins, Dulce Quelhas, Eva Morava, Pascale de Lonlay, Peter Witters, and Tomáš Honzík. Consensus guideline for the diagnosis and management of mannose phosphate isomerase‐congenital disorder of glycosylation. Journal of Inherited Metabolic Disease, 43:671-693, Apr 2020. URL: https://doi.org/10.1002/jimd.12241, doi:10.1002/jimd.12241. This article has 73 citations and is from a peer-reviewed journal.

4. (cechova2020consensusguidelinefor pages 19-20): Anna Čechová, Ruqaiah Altassan, Delphine Borgel, Arnaud Bruneel, Joana Correia, Muriel Girard, Annie Harroche, Beata Kiec‐Wilk, Klaus Mohnike, Tiffany Pascreau, Łukasz Pawliński, Silvia Radenkovic, Sandrine Vuillaumier‐Barrot, Luis Aldamiz‐Echevarria, Maria Luz Couce, Esmeralda G. Martins, Dulce Quelhas, Eva Morava, Pascale de Lonlay, Peter Witters, and Tomáš Honzík. Consensus guideline for the diagnosis and management of mannose phosphate isomerase‐congenital disorder of glycosylation. Journal of Inherited Metabolic Disease, 43:671-693, Apr 2020. URL: https://doi.org/10.1002/jimd.12241, doi:10.1002/jimd.12241. This article has 73 citations and is from a peer-reviewed journal.

5. (NCT03404869 chunk 1):  Study of ORL-1M (D-mannose) in Patients With CDG-Ib. Orpha Labs. 2015. ClinicalTrials.gov Identifier: NCT03404869

6. (cechova2020consensusguidelinefor pages 17-19): Anna Čechová, Ruqaiah Altassan, Delphine Borgel, Arnaud Bruneel, Joana Correia, Muriel Girard, Annie Harroche, Beata Kiec‐Wilk, Klaus Mohnike, Tiffany Pascreau, Łukasz Pawliński, Silvia Radenkovic, Sandrine Vuillaumier‐Barrot, Luis Aldamiz‐Echevarria, Maria Luz Couce, Esmeralda G. Martins, Dulce Quelhas, Eva Morava, Pascale de Lonlay, Peter Witters, and Tomáš Honzík. Consensus guideline for the diagnosis and management of mannose phosphate isomerase‐congenital disorder of glycosylation. Journal of Inherited Metabolic Disease, 43:671-693, Apr 2020. URL: https://doi.org/10.1002/jimd.12241, doi:10.1002/jimd.12241. This article has 73 citations and is from a peer-reviewed journal.

7. (cechova2020consensusguidelinefor pages 3-4): Anna Čechová, Ruqaiah Altassan, Delphine Borgel, Arnaud Bruneel, Joana Correia, Muriel Girard, Annie Harroche, Beata Kiec‐Wilk, Klaus Mohnike, Tiffany Pascreau, Łukasz Pawliński, Silvia Radenkovic, Sandrine Vuillaumier‐Barrot, Luis Aldamiz‐Echevarria, Maria Luz Couce, Esmeralda G. Martins, Dulce Quelhas, Eva Morava, Pascale de Lonlay, Peter Witters, and Tomáš Honzík. Consensus guideline for the diagnosis and management of mannose phosphate isomerase‐congenital disorder of glycosylation. Journal of Inherited Metabolic Disease, 43:671-693, Apr 2020. URL: https://doi.org/10.1002/jimd.12241, doi:10.1002/jimd.12241. This article has 73 citations and is from a peer-reviewed journal.

8. (lu2023mannosephosphateisomerase pages 3-5): Siliang Lu, Shuheng Liang, Yi Wu, Jinyi Liu, Lin Lin, Guosheng Huang, and Huaijun Ning. Mannose phosphate isomerase gene mutation leads to a congenital disorder of glycosylation: a rare case report and literature review. Frontiers in Pediatrics, Apr 2023. URL: https://doi.org/10.3389/fped.2023.1150367, doi:10.3389/fped.2023.1150367. This article has 8 citations.

9. (cechova2020consensusguidelinefor pages 16-17): Anna Čechová, Ruqaiah Altassan, Delphine Borgel, Arnaud Bruneel, Joana Correia, Muriel Girard, Annie Harroche, Beata Kiec‐Wilk, Klaus Mohnike, Tiffany Pascreau, Łukasz Pawliński, Silvia Radenkovic, Sandrine Vuillaumier‐Barrot, Luis Aldamiz‐Echevarria, Maria Luz Couce, Esmeralda G. Martins, Dulce Quelhas, Eva Morava, Pascale de Lonlay, Peter Witters, and Tomáš Honzík. Consensus guideline for the diagnosis and management of mannose phosphate isomerase‐congenital disorder of glycosylation. Journal of Inherited Metabolic Disease, 43:671-693, Apr 2020. URL: https://doi.org/10.1002/jimd.12241, doi:10.1002/jimd.12241. This article has 73 citations and is from a peer-reviewed journal.

10. (cechova2020consensusguidelinefor pages 11-13): Anna Čechová, Ruqaiah Altassan, Delphine Borgel, Arnaud Bruneel, Joana Correia, Muriel Girard, Annie Harroche, Beata Kiec‐Wilk, Klaus Mohnike, Tiffany Pascreau, Łukasz Pawliński, Silvia Radenkovic, Sandrine Vuillaumier‐Barrot, Luis Aldamiz‐Echevarria, Maria Luz Couce, Esmeralda G. Martins, Dulce Quelhas, Eva Morava, Pascale de Lonlay, Peter Witters, and Tomáš Honzík. Consensus guideline for the diagnosis and management of mannose phosphate isomerase‐congenital disorder of glycosylation. Journal of Inherited Metabolic Disease, 43:671-693, Apr 2020. URL: https://doi.org/10.1002/jimd.12241, doi:10.1002/jimd.12241. This article has 73 citations and is from a peer-reviewed journal.

11. (cechova2020consensusguidelinefor pages 10-11): Anna Čechová, Ruqaiah Altassan, Delphine Borgel, Arnaud Bruneel, Joana Correia, Muriel Girard, Annie Harroche, Beata Kiec‐Wilk, Klaus Mohnike, Tiffany Pascreau, Łukasz Pawliński, Silvia Radenkovic, Sandrine Vuillaumier‐Barrot, Luis Aldamiz‐Echevarria, Maria Luz Couce, Esmeralda G. Martins, Dulce Quelhas, Eva Morava, Pascale de Lonlay, Peter Witters, and Tomáš Honzík. Consensus guideline for the diagnosis and management of mannose phosphate isomerase‐congenital disorder of glycosylation. Journal of Inherited Metabolic Disease, 43:671-693, Apr 2020. URL: https://doi.org/10.1002/jimd.12241, doi:10.1002/jimd.12241. This article has 73 citations and is from a peer-reviewed journal.

12. (lu2023mannosephosphateisomerase pages 2-3): Siliang Lu, Shuheng Liang, Yi Wu, Jinyi Liu, Lin Lin, Guosheng Huang, and Huaijun Ning. Mannose phosphate isomerase gene mutation leads to a congenital disorder of glycosylation: a rare case report and literature review. Frontiers in Pediatrics, Apr 2023. URL: https://doi.org/10.3389/fped.2023.1150367, doi:10.3389/fped.2023.1150367. This article has 8 citations.

13. (lu2023mannosephosphateisomerase pages 5-6): Siliang Lu, Shuheng Liang, Yi Wu, Jinyi Liu, Lin Lin, Guosheng Huang, and Huaijun Ning. Mannose phosphate isomerase gene mutation leads to a congenital disorder of glycosylation: a rare case report and literature review. Frontiers in Pediatrics, Apr 2023. URL: https://doi.org/10.3389/fped.2023.1150367, doi:10.3389/fped.2023.1150367. This article has 8 citations.

14. (cechova2020consensusguidelinefor pages 8-10): Anna Čechová, Ruqaiah Altassan, Delphine Borgel, Arnaud Bruneel, Joana Correia, Muriel Girard, Annie Harroche, Beata Kiec‐Wilk, Klaus Mohnike, Tiffany Pascreau, Łukasz Pawliński, Silvia Radenkovic, Sandrine Vuillaumier‐Barrot, Luis Aldamiz‐Echevarria, Maria Luz Couce, Esmeralda G. Martins, Dulce Quelhas, Eva Morava, Pascale de Lonlay, Peter Witters, and Tomáš Honzík. Consensus guideline for the diagnosis and management of mannose phosphate isomerase‐congenital disorder of glycosylation. Journal of Inherited Metabolic Disease, 43:671-693, Apr 2020. URL: https://doi.org/10.1002/jimd.12241, doi:10.1002/jimd.12241. This article has 73 citations and is from a peer-reviewed journal.

15. (cechova2020consensusguidelinefor pages 6-8): Anna Čechová, Ruqaiah Altassan, Delphine Borgel, Arnaud Bruneel, Joana Correia, Muriel Girard, Annie Harroche, Beata Kiec‐Wilk, Klaus Mohnike, Tiffany Pascreau, Łukasz Pawliński, Silvia Radenkovic, Sandrine Vuillaumier‐Barrot, Luis Aldamiz‐Echevarria, Maria Luz Couce, Esmeralda G. Martins, Dulce Quelhas, Eva Morava, Pascale de Lonlay, Peter Witters, and Tomáš Honzík. Consensus guideline for the diagnosis and management of mannose phosphate isomerase‐congenital disorder of glycosylation. Journal of Inherited Metabolic Disease, 43:671-693, Apr 2020. URL: https://doi.org/10.1002/jimd.12241, doi:10.1002/jimd.12241. This article has 73 citations and is from a peer-reviewed journal.

16. (chu2013azebrafishmodel pages 1-2): Jaime Chu, Alexander Mir, Ningguo Gao, Sabrina Rosa, Christopher Monson, Vandana Sharma, Richard Steet, Hudson H. Freeze, Mark A. Lehrman, and Kirsten C. Sadler. A zebrafish model of congenital disorders of glycosylation with phosphomannose isomerase deficiency reveals an early opportunity for corrective mannose supplementation. Disease Models & Mechanisms, 6:95-105, Aug 2013. URL: https://doi.org/10.1242/dmm.010116, doi:10.1242/dmm.010116. This article has 44 citations and is from a domain leading peer-reviewed journal.

17. (sharma2014mannosesupplementsinduce pages 1-2): Vandana Sharma, Jonamani Nayak, Charles DeRossi, Adriana Charbono, Mie Ichikawa, Bobby G. Ng, Erika Grajales‐Esquivel, Anand Srivastava, Ling Wang, Ping He, David A. Scott, Joseph Russell, Emily Contreras, Cherise M. Guess, Stan Krajewski, Katia Del Rio‐Tsonis, and Hudson H. Freeze. Mannose supplements induce embryonic lethality and blindness in phosphomannose isomerase hypomorphic mice. The FASEB Journal, 28:1854-1869, Jan 2014. URL: https://doi.org/10.1096/fj.13-245514, doi:10.1096/fj.13-245514. This article has 39 citations.

18. (brasil2018cdgtherapiesfrom pages 3-4): Sandra Brasil, Carlota Pascoal, Rita Francisco, Dorinda Marques-da-Silva, Giuseppina Andreotti, Paula A. Videira, Eva Morava, Jaak Jaeken, and Vanessa Dos Reis Ferreira. Cdg therapies: from bench to bedside. International Journal of Molecular Sciences, 19:1304, Apr 2018. URL: https://doi.org/10.3390/ijms19051304, doi:10.3390/ijms19051304. This article has 120 citations.

19. (cechova2020consensusguidelinefor pages 13-14): Anna Čechová, Ruqaiah Altassan, Delphine Borgel, Arnaud Bruneel, Joana Correia, Muriel Girard, Annie Harroche, Beata Kiec‐Wilk, Klaus Mohnike, Tiffany Pascreau, Łukasz Pawliński, Silvia Radenkovic, Sandrine Vuillaumier‐Barrot, Luis Aldamiz‐Echevarria, Maria Luz Couce, Esmeralda G. Martins, Dulce Quelhas, Eva Morava, Pascale de Lonlay, Peter Witters, and Tomáš Honzík. Consensus guideline for the diagnosis and management of mannose phosphate isomerase‐congenital disorder of glycosylation. Journal of Inherited Metabolic Disease, 43:671-693, Apr 2020. URL: https://doi.org/10.1002/jimd.12241, doi:10.1002/jimd.12241. This article has 73 citations and is from a peer-reviewed journal.

20. (cechova2020consensusguidelinefor pages 14-16): Anna Čechová, Ruqaiah Altassan, Delphine Borgel, Arnaud Bruneel, Joana Correia, Muriel Girard, Annie Harroche, Beata Kiec‐Wilk, Klaus Mohnike, Tiffany Pascreau, Łukasz Pawliński, Silvia Radenkovic, Sandrine Vuillaumier‐Barrot, Luis Aldamiz‐Echevarria, Maria Luz Couce, Esmeralda G. Martins, Dulce Quelhas, Eva Morava, Pascale de Lonlay, Peter Witters, and Tomáš Honzík. Consensus guideline for the diagnosis and management of mannose phosphate isomerase‐congenital disorder of glycosylation. Journal of Inherited Metabolic Disease, 43:671-693, Apr 2020. URL: https://doi.org/10.1002/jimd.12241, doi:10.1002/jimd.12241. This article has 73 citations and is from a peer-reviewed journal.

21. (bogdanska2021clinicalbiochemicaland pages 1-2): Anna Bogdańska, Patryk Lipiński, Paulina Szymańska-Rożek, Aleksandra Jezela-Stanek, Dariusz Rokicki, Piotr Socha, and Anna Tylki-Szymańska. Clinical, biochemical and molecular phenotype of congenital disorders of glycosylation: long-term follow-up. Orphanet Journal of Rare Diseases, Jan 2021. URL: https://doi.org/10.1186/s13023-020-01657-5, doi:10.1186/s13023-020-01657-5. This article has 50 citations and is from a peer-reviewed journal.

22. (cechova2020consensusguidelinefor pages 20-21): Anna Čechová, Ruqaiah Altassan, Delphine Borgel, Arnaud Bruneel, Joana Correia, Muriel Girard, Annie Harroche, Beata Kiec‐Wilk, Klaus Mohnike, Tiffany Pascreau, Łukasz Pawliński, Silvia Radenkovic, Sandrine Vuillaumier‐Barrot, Luis Aldamiz‐Echevarria, Maria Luz Couce, Esmeralda G. Martins, Dulce Quelhas, Eva Morava, Pascale de Lonlay, Peter Witters, and Tomáš Honzík. Consensus guideline for the diagnosis and management of mannose phosphate isomerase‐congenital disorder of glycosylation. Journal of Inherited Metabolic Disease, 43:671-693, Apr 2020. URL: https://doi.org/10.1002/jimd.12241, doi:10.1002/jimd.12241. This article has 73 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](MPI-Congenital_Disorder_of_Glycosylation-deep-research-falcon_artifacts/artifact-00.md)