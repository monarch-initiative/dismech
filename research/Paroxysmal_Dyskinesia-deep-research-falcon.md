---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-01T07:32:55.910902'
end_time: '2026-08-01T07:39:50.064356'
duration_seconds: 414.15
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Paroxysmal Dyskinesia
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 37
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Paroxysmal_Dyskinesia-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Paroxysmal Dyskinesia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Paroxysmal Dyskinesia** covering all of the
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
- **Disease Name:** Paroxysmal Dyskinesia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Paroxysmal Dyskinesia** covering all of the
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


# Paroxysmal Dyskinesia: comprehensive disease-characteristics report

**Scope note.** *Paroxysmal dyskinesia* (PD/PxD) is an umbrella phenotype rather than one molecular disease. The classic primary forms are paroxysmal kinesigenic dyskinesia (PKD), paroxysmal non-kinesigenic dyskinesia (PNKD), and paroxysmal exercise-induced dyskinesia (PED); older classifications also include paroxysmal hypnogenic dyskinesia (PHD). Accordingly, identifiers, inheritance, mechanisms, and treatment should be recorded at both umbrella and gene-defined subtype levels.

## 1. Disease information

PDs are rare hyperkinetic disorders characterized by recurrent, abrupt attacks of dystonia, chorea, athetosis, ballism, or combinations thereof, generally with preserved consciousness and a normal interictal examination. Classification is primarily by trigger: sudden voluntary movement/startle in PKD; alcohol, caffeine, stress, fatigue, or no clear trigger in PNKD; sustained exercise in PED; and sleep-related attacks in PHD. A recent systematic review states that PDs are “rare, episodic movement disorders characterized by sudden and involuntary hyperkinetic motor events.” (harvey2021paroxysmalmovementdisorders pages 1-2, pisano2025paroxysmaldyskinesiasin pages 1-2, xu2024paroxysmalkinesigenicdyskinesia pages 1-3)

**Suggested identifiers and terminology**

- **MONDO:** use the MONDO umbrella concept for *paroxysmal dyskinesia* if available in the implementation’s current MONDO release, but retain separate descendant records for PKD, PNKD, and GLUT1-related PED. A stable umbrella MONDO identifier was not verified in the retrieved literature.
- **OMIM:** subtype-level records are preferable; examples include PRRT2-associated PKD/PKD with infantile convulsions, PNKD-associated PNKD, KCNMA1-associated PNKD3, and SLC2A1/GLUT1 deficiency. OMIM gene IDs directly supported in retrieved text include **PNKD, MIM 609023**, and **SLC2A1, MIM 138140**. (harvey2021paroxysmalmovementdisorders pages 2-3, harvey2021paroxysmalmovementdisorders pages 3-4)
- **MeSH:** *Dyskinesias* (**D020820**), with *Chorea* (**D002819**) and *Movement Disorders* as related concepts. (NCT06701851 chunk 1)
- **ICD:** no single highly specific ICD-10 disease code covers all inherited PDs; coding commonly falls under **G24.8, other dystonia**, or another movement-disorder code plus the molecular syndrome. ICD-11 should likewise use the most specific dystonia/movement-disorder entity available and append genetic etiology.
- **Synonyms:** paroxysmal dyskinesias; episodic dyskinesia; paroxysmal movement disorder; PKD/paroxysmal kinesigenic choreoathetosis; PNKD/paroxysmal dystonic choreoathetosis; PED/paroxysmal exertion-induced dyskinesia.
- **Source granularity:** the evidence is predominantly aggregated disease-level literature, family studies, case series, systematic reviews, and registries—not routinely extracted individual EHR data.

## 2. Etiology, risk, protective factors, and gene–environment interaction

### Causal factors

Primary PD is predominantly genetic. Core causes are **PRRT2** and **TMEM151A** for PKD, **PNKD** for classic PNKD, **KCNMA1** for PNKD3, and **SLC2A1** for PED/GLUT1 deficiency. Additional established or reported causes include **ADCY5, GNAO1, SCN8A, KCNA1, CACNA1A, ATP1A3, RHOBTB2, TBC1D24, PDE2A, DEPDC5, FGF14, GCH1, PARK2, ECHS1, PDHA1/PDHX/DLAT, GLDC, BCKD-complex genes, SLC20A2**, and **PIGN**. These latter disorders often include epilepsy, developmental impairment, persistent movement disorder, metabolic disease, or structural abnormalities rather than isolated PD. (pisano2025paroxysmaldyskinesiasin pages 8-11, harvey2021paroxysmalmovementdisorders pages 2-3, harvey2021paroxysmalmovementdisorders pages 3-4)

Secondary PD can follow demyelination, stroke, trauma, infection, autoimmune disease, metabolic disturbance, structural brain lesions, or medication/toxin exposure. Adult onset, inconsistent triggers, changing phenomenology, or abnormal interictal findings should therefore prompt evaluation for secondary or functional disorders. (gusmao2019paroxysmalmovementdisorders pages 31-34)

### Risk factors

- **Family history/causal genotype:** strongest risk factor for primary disease.
- **Sex:** PKD has a reported male:female ratio of approximately **2–4:1**. Why male expression is greater remains unresolved. (xu2024paroxysmalkinesigenicdyskinesia pages 9-10, xu2024paroxysmalkinesigenicdyskinesia pages 1-3)
- **Age:** onset is usually childhood or adolescence, although infancy and adult onset occur.
- **Provoking exposures:** sudden movement/startle in PKD; caffeine, alcohol, emotional stress, sleep deprivation, and fatigue in PNKD; exercise and sometimes fasting in SLC2A1-related PED; fever or illness in selected channelopathies/metabolic disorders. These are attack triggers, not generally causes of the inherited disease. (harvey2021paroxysmalmovementdisorders pages 2-3, harvey2021paroxysmalmovementdisorders pages 3-4)

### Protective factors

No validated germline “protective variants” are established. Apparent environmental protection is mainly avoidance of individual triggers, adequate sleep, regular meals/avoidance of fasting in GLUT1 deficiency, and adherence to genotype-directed treatment. Evidence for exercise, smoking, alcohol, or nutritional factors as modifiers of disease acquisition is absent; alcohol and caffeine can instead provoke PNKD.

### Gene–environment interaction

PD provides a strong trigger-threshold model: a pathogenic variant creates latent neuronal-network instability, while movement, stress, stimulants, alcohol, sleep loss, exercise, or fasting acutely pushes the network beyond the attack threshold. Incomplete penetrance—approximately **74.5–77.6% for PRRT2**, **53.8% for TMEM151A**, and approximately **95% for recurrent PNKD variants**—implies contributions from background genotype, development, epigenetics, and exposures, although specific human modifier genes have not been validated. (xu2024paroxysmalkinesigenicdyskinesia pages 3-5, harvey2021paroxysmalmovementdisorders pages 3-4, harvey2021paroxysmalmovementdisorders pages 11-12)

## 3. Phenotypes

| Phenotype | Characteristics and frequency | Suggested HPO terms |
|---|---|---|
| Paroxysmal dystonia/chorea | Core episodic manifestation; consciousness normally preserved. In PRRT2-PKD, attacks comprised dystonia **17.6%**, chorea **15.2%**, and both **67.1%** in summarized cohorts. (harvey2021paroxysmalmovementdisorders pages 1-2, harvey2021paroxysmalmovementdisorders pages 2-3) | Paroxysmal dystonia; Chorea **HP:0002072**; Athetosis **HP:0002305**; Ballism |
| PKD attacks | Triggered by sudden voluntary movement or startle; usually **<1 minute**, often daily; onset mean **9.9 years**, range **1–40**; frequently declines in adulthood. Sensory aura may occur. (xu2024paroxysmalkinesigenicdyskinesia pages 1-3, harvey2021paroxysmalmovementdisorders pages 2-3) | Kinesigenic dyskinesia; Childhood onset **HP:0011463**; Episodic course |
| PNKD attacks | Stress, caffeine, alcohol, tea, fatigue, or emotion; usually **10 minutes–1 hour**, occasionally up to **12 hours**; often only a few attacks/year; mean onset about **5 years**, range **6 months–35 years**. (harvey2021paroxysmalmovementdisorders pages 3-4) | Non-kinesigenic dyskinesia; Dystonia **HP:0001332** |
| PED | Exercise/fatigue-provoked, often leg-predominant dystonia/choreoathetosis; SLC2A1 cases may have epilepsy, intellectual disability, spasticity, microcephaly, or ataxia. (harvey2021paroxysmalmovementdisorders pages 3-4, suls2008paroxysmalexerciseinduceddyskinesia pages 1-2) | Exercise-induced dystonia; Gait disturbance **HP:0001288**; Spasticity **HP:0001257** |
| Epilepsy | Infantile seizures occur in approximately **30% of PRRT2-associated PKD**; absence epilepsy is prominent in KCNMA1-D434G and SLC2A1 disease. In one D434G family, 9/16 had absence epilepsy, 12/16 PNKD, and 5/16 both. (harvey2021paroxysmalmovementdisorders pages 2-3, dong2022neuronalmechanismof pages 1-2) | Seizure **HP:0001250**; Absence seizure **HP:0002121**; Infantile-onset seizure |
| Neurodevelopmental manifestations | Usually absent in isolated heterozygous PRRT2/PNKD disease, but intellectual disability, developmental delay, hypotonia, or persistent dyskinesia occur with biallelic PRRT2, 16p11.2 deletion, GNAO1, ADCY5, SCN8A, RHOBTB2, PIGN, and metabolic etiologies. (xu2024paroxysmalkinesigenicdyskinesia pages 3-5, harvey2021paroxysmalmovementdisorders pages 3-4) | Global developmental delay **HP:0001263**; Intellectual disability **HP:0001249**; Hypotonia **HP:0001252** |
| Interictal state | Often neurologically normal in classic primary PD; abnormal interictal ataxia, myokymia, spasticity, or persistent chorea suggests a pleiotropic gene or secondary disease. (harvey2021paroxysmalmovementdisorders pages 1-2, gusmao2019paroxysmalmovementdisorders pages 31-34) | Normal interictal examination; Ataxia **HP:0001251**; Myokymia **HP:0002411** |

In a 2025 pediatric systematic review of 112 studies/605 patients, PKD represented **343/604 (56.8%)**, PNKD **142/604 (23.5%)**, and PED **119/604 (19.7%)**; among 476 with reported sex, **63.4% were male**. Mean onset was **5.99 years**, median 5 years, range 10 days–17 years. These figures describe the published pediatric literature, not population prevalence, and may be affected by referral/publication bias. (pisano2025paroxysmaldyskinesiasin pages 4-6)

**Quality of life.** Attacks can impair walking, school/work attendance, driving, sports, and social participation, and falls can cause injury. Anticipatory anxiety and trigger avoidance may be substantial even when examination is normal. Standardized EQ-5D/SF-36 data specific to classic PD are sparse; the recent review notes clinically important nonmotor and quality-of-life effects but does not provide a pooled instrument score. (pisano2025paroxysmaldyskinesiasin pages 11-12, harvey2021paroxysmalmovementdisorders pages 11-12)

## 4. Genetic and molecular information

| Clinical entity / trigger | Principal gene(s) and inheritance | Typical attack / onset features | Mechanism | Practical treatment |
|---|---|---|---|---|
| **PKD**; sudden voluntary movement or startle | **PRRT2** (usually AD, incomplete penetrance ~74.5%–77.6%; recurrent **c.649dupC** common, up to ~80% of PRRT2 mutation carriers), **TMEM151A** (AD, lower penetrance ~53.8%) | Brief recurrent dystonia/choreoathetosis; attacks usually **<1 min**; onset typically childhood/early adolescence; male:female about **2–4:1**; PKD prevalence estimated **~1:150,000**. PRRT2-PKD tends to have earlier onset, longer duration, choreoathetosis, bilateral involvement; TMEM151A cases tend to be purer dystonia with shorter attacks and more sporadic presentation. | PRRT2 loss-of-function/haploinsufficiency disrupts presynaptic signaling and neuronal excitability: altered **Nav1.2/Nav1.6** regulation, impaired **Na+/K+ ATPase** activity, and abnormal synaptic vesicle docking/SNARE-associated release; PKD is viewed as both **channelopathy and synaptopathy**. TMEM151A data support loss-of-function/haploinsufficiency, but protein function remains less defined. Cerebellar and basal ganglia-thalamo-cortical circuits are implicated. | **Carbamazepine** or **oxcarbazepine** are first-line; often highly effective, especially in PRRT2-related PKD, sometimes at low dose. TMEM151A-linked disease also improves, though complete remission may be less consistent. Trigger avoidance (sleep deprivation, stress, stimulants if relevant); genetic counseling. (xu2024paroxysmalkinesigenicdyskinesia pages 9-10, xu2024paroxysmalkinesigenicdyskinesia pages 3-5, xu2024paroxysmalkinesigenicdyskinesia pages 5-6, xu2024paroxysmalkinesigenicdyskinesia pages 1-3, harvey2021paroxysmalmovementdisorders pages 2-3, NCT04023656 chunk 1) |
| **PNKD**; no clear kinesigenic trigger, commonly stress/alcohol/caffeine/strong emotion | **PNKD** (AD, near-complete penetrance ~95%; recurrent **p.Ala7Val** and **p.Ala9Val**), **KCNMA1** (AD; PNKD3) | PNKD attacks are longer than PKD, typically **10 min to 1 h**, but may last up to **12 h**; onset from childhood to early adolescence (mean about **5 years**, range **6 months–35 years**); attacks may be infrequent, only a few per year. KCNMA1-associated disease may include paroxysmal dyskinesia with or without epilepsy and “drop-attack”/immobility-like episodes. | **PNKD** protein is synaptic and linked to regulation of neurotransmitter release/cellular redox-stress pathways. In mouse PNKD models, dyskinesia is associated with **striatal indirect pathway (iMSN) hypoactivity** and aberrant **endocannabinoid-mediated suppression** of glutamatergic input. **KCNMA1** variants alter **BK potassium channel** function: GOF alleles (e.g., **N999S**, **D434G**) increase neuronal firing and lower seizure threshold; cortical pyramidal and cerebellar Purkinje cell hyperexcitability are implicated. | Avoid/limit **alcohol, caffeine, emotional stress** where relevant. Classic PNKD often responds poorly to medication but may improve with age. For KCNMA1-related disease, case-guided symptomatic therapy may include **dextroamphetamine** for immobility/drop-attack phenotype; mechanistic studies suggest **BK inhibition** as a future precision approach, but this is not established clinical standard. (gusmao2019paroxysmalmovementdisorders pages 1-6, harvey2021paroxysmalmovementdisorders pages 3-4, nelson2022striatalindirectpathway pages 1-2, park2022bkchannelproperties pages 1-2, dong2022neuronalmechanismof pages 1-2) |
| **PED**; prolonged exercise/fatigue, sometimes fasting | **SLC2A1** (usually AD; rare AR reported), metabolic mimics including **ECHS1** (AR), **PDHA1/PDHX/DLAT** (X-linked/AR pyruvate dehydrogenase complex disorders), **BCKD complex** genes (AR), **GLDC** (AR) | Often leg-predominant chorea/dystonia after exertion; may coexist with epilepsy. In SLC2A1-related PED, median CSF:blood glucose ratio reported **0.52** (normal **>0.60**); GLUT1 phenotype spectrum includes PED, PKD/PNKD, epilepsy/absence epilepsy, intellectual/developmental issues, and spasticity. | **SLC2A1/GLUT1** deficiency reduces glucose transport across the **blood-brain barrier**, causing brain energy failure; imaging implicated **corticostriate glucose metabolism** abnormalities in PED. Metabolic mimics reflect impaired mitochondrial/pyruvate or amino acid metabolism. | **Ketogenic diet** is the key disease-modifying therapy for SLC2A1-related PED; early diagnosis matters. In the original SLC2A1 PED/epilepsy series, **3 patients** were successfully treated with ketogenic diet. Consider targeted metabolic therapy in mimics (e.g., **thiamine** in pyruvate dehydrogenase deficiency; dietary manipulation in MSUD-related disease) and avoidance of provoking exertion/fasting. (harvey2021paroxysmalmovementdisorders pages 3-4, harvey2021paroxysmalmovementdisorders pages 7-8, suls2008paroxysmalexerciseinduceddyskinesia pages 1-2) |
| **Pleiotropic paroxysmal dyskinesias**; mixed triggers including sleep, exertion, stress, spontaneous episodes | **ADCY5** (AD), **GNAO1** (AD), **SCN8A** (AD) | Often broader neurodevelopmental/epileptic phenotypes rather than isolated dyskinesia. ADCY5 can cause **PKD, PED, PNKD, nocturnal paroxysmal movements**, facial/orofacial dyskinesia, hypotonia, developmental delay. GNAO1 commonly presents with severe hyperkinetic episodes plus developmental and epileptic encephalopathy. SCN8A may cause infantile seizures with later PKD/PKD-like episodes. | **ADCY5** affects striatal **cAMP signaling**; **GNAO1** perturbs G-protein signaling with network hyperkinetic instability; **SCN8A** alters **Nav1.6** sodium channel excitability. These genes exemplify the overlap between movement-disorder, epilepsy, and developmental phenotypes. | **ADCY5:** caffeine may reduce symptoms; **clonazepam**, **acetazolamide**, and selected severe cases **DBS** are used in practice. **GNAO1:** severe hyperkinetic crises may lead to consideration of **DBS**. **SCN8A:** **carbamazepine/oxcarbazepine** may help when sodium-channel hyperexcitability is suspected. Broad NGS-based diagnosis is especially useful because treatment is genotype-informed rather than purely phenomenologic. (pisano2025paroxysmaldyskinesiasin pages 11-12, pisano2025paroxysmaldyskinesiasin pages 8-11, harvey2021paroxysmalmovementdisorders pages 3-4, harvey2021paroxysmalmovementdisorders pages 11-12) |


*Table: This table summarizes the major inherited paroxysmal dyskinesia entities by trigger pattern, principal genes, mechanism, and practical treatment implications. It is designed as a compact genotype-guided reference for differentiating classic PKD/PNKD/PED from pleiotropic dyskinesia syndromes.*

### Major genes and variants

- **PRRT2 (16p11.2):** usually heterozygous autosomal-dominant loss of function/haploinsufficiency. More than 100 variants have been catalogued; frameshift/nonsense alleles predominate. **NM_145239.3:c.649dupC** is the recurrent hotspot, reported as up to 80% of PRRT2 mutation carriers in the 2024 review. Truncating proteins undergo proteasomal degradation; pathogenic missense alleles cluster toward the C-terminus and can mislocalize protein from membrane to cytoplasm. Rare biallelic variants produce more severe PKD, prolonged ataxia, epilepsy, and intellectual disability. A 16p11.2 deletion encompassing PRRT2 is an important structural cause. (xu2024paroxysmalkinesigenicdyskinesia pages 3-5, xu2024paroxysmalkinesigenicdyskinesia pages 1-3)
- **TMEM151A (11q13.2):** more than 50 truncating, missense, and in-frame deletion variants reported. Patient transcript analysis for **c.606_607insA** showed approximately half-normal mRNA; available evidence supports loss of function/haploinsufficiency. Penetrance is estimated at **53.8%**. (xu2024paroxysmalkinesigenicdyskinesia pages 3-5)
- **PNKD (2q35; MIM 609023):** classic recurrent missense variants **p.Ala7Val** and **p.Ala9Val**, autosomal dominant with approximately 95% penetrance. Pathogenic PNKD variants account for about **70%** of classic familial PNKD in the cited review. (harvey2021paroxysmalmovementdisorders pages 3-4)
- **SLC2A1 (1p34.2; MIM 138140):** predominantly heterozygous/de novo or autosomal dominant loss-of-function variants; rare recessive disease occurs. Missense, nonsense, frameshift, splice, and deletion variants reduce GLUT1-mediated blood–brain-barrier glucose transport. (harvey2021paroxysmalmovementdisorders pages 3-4, suls2008paroxysmalexerciseinduceddyskinesia pages 1-2)
- **KCNMA1 (10q22.3):** generally heterozygous/de novo or dominant channelopathy. **p.Asp434Gly** and **p.Asn999Ser** are gain-of-function BK-channel variants; **p.His444Gln** is loss of function in experimental systems. Variant effect—not merely gene name—is necessary for mechanistic and therapeutic interpretation. (park2022bkchannelproperties pages 1-2, dong2022neuronalmechanismof pages 1-2)

These are constitutional/germline disorders; somatic origin is not typical, although low-level mosaicism can be missed without deep sequencing. Population allele frequencies should be retrieved variant-by-variant from the current gnomAD release; pathogenic dominant alleles are expected to be absent or extremely rare. The retrieved literature does not provide reliable gnomAD frequencies for individual alleles, and none should be inferred.

### Modifiers, epigenetics, and chromosomal abnormalities

Specific modifier genes and reproducible disease-associated methylation or chromatin signatures are not established. Reduced penetrance and intrafamilial variability support modifiers, but this remains an open research area. Copy-number analysis is important for **16p11.2 deletion/duplication**, especially in PRRT2-negative sporadic PKD with developmental features. The 2025 pediatric review found 16p11.2 abnormalities in ten patients. (pisano2025paroxysmaldyskinesiasin pages 6-8, harvey2021paroxysmalmovementdisorders pages 11-12)

## 5. Environmental, lifestyle, and infectious information

There is no evidence that pollution, radiation, occupational exposure, smoking, or an infectious agent is a general cause of Mendelian PD. Alcohol and caffeine are reproducible PNKD precipitants; fatigue, stress, excitement, sleep deprivation, startle, exercise, fasting, fever, and meals can be subtype-specific triggers. Drugs, toxins, metabolic derangement, encephalitis, or structural lesions can cause secondary dyskinesia. Infection is therefore relevant primarily as an acquired neurologic trigger/differential, not as a transmissible cause. (gusmao2019paroxysmalmovementdisorders pages 31-34, harvey2021paroxysmalmovementdisorders pages 3-4)

## 6. Mechanism and pathophysiology

### Upstream-to-downstream causal chains

1. **PRRT2-PKD—synaptopathy/channelopathy:** truncating or mislocalized PRRT2 → reduced presynaptic PRRT2 → impaired regulation of NaV1.2/NaV1.6, Na+/K+-ATPase, P/Q-type calcium channels, and SNARE-associated proteins SNAP25, VAMP2, STX1A, and synaptotagmins → reduced action-potential threshold, abnormal vesicle docking/release, and network instability → trigger-induced spreading depolarization/circuit discharge → brief dystonia/choreoathetosis. Human PRRT2-null iPSC neurons showed increased sodium-current density and reduced action-potential threshold. (xu2024paroxysmalkinesigenicdyskinesia pages 5-6)
2. **PNKD-PNKD—striatal synaptic dysfunction:** altered PNKD protein stability/cleavage and stress-response/redox function → abnormal presynaptic transmission → excessive endocannabinoid suppression of glutamatergic input to indirect-pathway medium spiny neurons (iMSNs) → reduced iMSN firing and basal-ganglia indirect-pathway output → alcohol/caffeine/stress-provoked dyskinesia. The iMSN/endocannabinoid chain is compelling mouse evidence but is not yet a validated human biomarker. (nelson2022striatalindirectpathway pages 1-2)
3. **SLC2A1-PED—transportopathy:** reduced endothelial GLUT1 → impaired glucose entry across the blood–brain barrier → low CSF glucose and deficient cerebral energy availability, accentuated by exertion/fasting → corticostriatal energetic failure → leg-predominant PED and, in broader phenotypes, epilepsy/developmental impairment. A human family study reported median CSF:blood glucose ratio **0.52**, versus normal **>0.60**, and reduced mutant-transporter glucose uptake in Xenopus oocytes. (suls2008paroxysmalexerciseinduceddyskinesia pages 1-2)
4. **KCNMA1-PNKD3—channelopathy:** BK-channel GOF (D434G/N999S) → enhanced BK activity, altered action-potential repolarization and increased firing in selected neuronal populations → cortical/Purkinje-cell hyperexcitability, lower seizure threshold, and dyskinesia. D434G was autosomal dominant; in mice, BK inhibition suppressed hyperexcitability and motor/seizure phenotypes. (park2022bkchannelproperties pages 1-2, dong2022neuronalmechanismof pages 1-2)

**Suggested GO terms:** chemical synaptic transmission **GO:0007268**; synaptic vesicle exocytosis **GO:0016079**; regulation of membrane potential **GO:0042391**; action potential **GO:0001508**; sodium-ion transport **GO:0006814**; potassium-ion transport **GO:0006813**; glucose transmembrane transport **GO:1904659**; endocannabinoid signaling; long-term synaptic depression.

**Suggested cell terms:** neuron **CL:0000540**; glutamatergic neuron **CL:0000679**; medium spiny neuron **CL:0000549**; Purkinje cell **CL:0000121**; cerebellar granule cell; cerebral-cortex pyramidal neuron; brain microvascular endothelial cell.

### Omics and advanced technologies

Human disease-specific bulk/single-cell transcriptomic, proteomic, lipidomic, spatial-transcriptomic, and epigenomic signatures are not sufficiently replicated for diagnostic use. Current mechanistic evidence is driven mainly by genetics, heterologous electrophysiology, patient-derived neurons, rodent neurophysiology, chemogenetics, and imaging. Experts explicitly call for functional and multi-omics studies at scale. (xu2024paroxysmalkinesigenicdyskinesia pages 5-6, harvey2021paroxysmalmovementdisorders pages 11-12)

## 7. Anatomical structures affected

PD is a **functional central nervous-system network disorder** rather than a destructive muscle disease. Principal circuits include cerebellum, striatum/basal ganglia, thalamus, motor/premotor cortex, and their reciprocal connections. PRRT2 work emphasizes the cerebellar granule-cell→Purkinje-cell→deep-nuclear pathway and spreading depolarization, while imaging also implicates basal-ganglia–thalamo-cortical and cerebello-thalamic networks. PNKD mouse evidence localizes a critical deficit to striatal iMSNs; SLC2A1 adds the brain microvascular endothelium/BBB and corticostriatal metabolic pathway. (xu2024paroxysmalkinesigenicdyskinesia pages 9-10, xu2024paroxysmalkinesigenicdyskinesia pages 5-6, nelson2022striatalindirectpathway pages 1-2)

**Suggested anatomy terms:** brain **UBERON:0000955**; cerebral cortex **UBERON:0000956**; cerebellum **UBERON:0002037**; striatum **UBERON:0002435**; thalamus **UBERON:0001897**; basal ganglion; blood–brain barrier. **Subcellular compartments:** presynaptic active zone **GO:0048786**, synaptic vesicle **GO:0008021**, axon initial segment **GO:0043194**, plasma membrane **GO:0005886**, voltage-gated channel complex. Attacks may be unilateral, bilateral, or generalized; PRRT2-positive PKD is comparatively associated with bilateral involvement. (xu2024paroxysmalkinesigenicdyskinesia pages 3-5)

## 8. Temporal development

Classic PD usually begins acutely with individual attacks against an otherwise normal background, but the inherited predisposition is chronic. PKD commonly starts in later childhood/early adolescence, peaks during adolescence, and often becomes less frequent in the third decade. PNKD generally begins in childhood and also frequently improves with age. SLC2A1, KCNMA1, PIGN, and pleiotropic developmental disorders can begin in infancy and persist. There are no formal early/intermediate/end stages; the appropriate course annotation is **episodic, nonprogressive or improving**, unless the molecular syndrome includes neurodevelopmental or neurodegenerative disease. (harvey2021paroxysmalmovementdisorders pages 1-2, gusmao2019paroxysmalmovementdisorders pages 1-6, NCT04023656 chunk 1)

The key intervention window is early molecular diagnosis: immediate sodium-channel-blocker therapy can restore function in PKD, while early ketogenic treatment in GLUT1 deficiency may prevent avoidable, potentially irreversible neurologic impairment.

## 9. Inheritance and population

- **Epidemiology:** PKD prevalence is estimated at approximately **1:150,000**. Reliable population-wide incidence/prevalence estimates for umbrella PD, PNKD, and PED are unavailable. (xu2024paroxysmalkinesigenicdyskinesia pages 1-3, NCT04023656 chunk 1)
- **Inheritance:** predominantly autosomal dominant for PRRT2, TMEM151A, PNKD, KCNMA1, SLC2A1, ADCY5, GNAO1, SCN8A, KCNA1, and CACNA1A; autosomal recessive or X-linked inheritance occurs in metabolic and selected synaptic disorders. (harvey2021paroxysmalmovementdisorders pages 2-3, harvey2021paroxysmalmovementdisorders pages 3-4)
- **Penetrance/expressivity:** incomplete and age dependent for PRRT2 and TMEM151A; high but not absolute for classic PNKD. Expressivity is markedly variable, including infantile seizures, migraine, episodic ataxia, or isolated dyskinesia within one PRRT2 family. (xu2024paroxysmalkinesigenicdyskinesia pages 3-5, xu2024paroxysmalkinesigenicdyskinesia pages 1-3)
- **Anticipation:** not established for classic PD.
- **Mosaicism/germline mosaicism:** possible in apparently de novo disease but not quantified.
- **Founder effects:** recurrent PRRT2 c.649dupC reflects a mutable homopolymer hotspot rather than one proven worldwide founder. Population-specific founder alleles may exist but were not established by the retrieved evidence.
- **Carrier frequency:** no reliable general estimate; obtain from current population databases for recessive genes and counsel using variant-specific frequencies.
- **Consanguinity:** relevant to biallelic PRRT2, TBC1D24, PDE2A, ECHS1, BCKD-complex, GLDC, PIGN, and other recessive causes.
- **Population:** disease occurs worldwide. Published pediatric data show male predominance, but no ancestry is known to be universally protected or at high risk.

## 10. Diagnostics

### Clinical diagnosis

Document attack phenomenology, awareness, trigger, duration, frequency, distribution, aura, family history, interictal examination, and treatment response; smartphone video is highly valuable. Classic PKD criteria include a recognized kinesigenic trigger, short attacks, preserved consciousness, no pain, normal examination between attacks, exclusion of secondary disease, and often response to carbamazepine. The foundational diagnostic-criteria paper is Bruno et al., 28 December 2004, **PMID 15623687**. (NCT04023656 chunk 1)

### Investigations

- **EEG/video-EEG:** usually normal during dyskinesia; indicated where epilepsy, altered awareness, or sleep attacks are suspected. It is especially important for differentiating sleep-related dyskinesia from sleep-related hypermotor epilepsy. (pisano2025paroxysmaldyskinesiasin pages 6-8, suls2008paroxysmalexerciseinduceddyskinesia pages 1-2)
- **MRI brain:** typically normal in primary disease; obtain for adult/atypical onset, focal deficit, progressive course, or suspected secondary cause.
- **EMG:** not routine, but myotonic discharges support myotonia congenita rather than PKD. (xu2024paroxysmalkinesigenicdyskinesia pages 3-5)
- **Metabolic tests:** fasting serum glucose with paired CSF glucose and lactate when GLUT1 deficiency is suspected; lactate, amino/organic acids, acylcarnitines, and targeted enzyme/cofactor studies for metabolic PED/PNKD.
- **Biomarkers:** hypoglycorrhachia/low CSF:blood glucose ratio is the most established biochemical marker for SLC2A1 disease. There is no validated circulating biomarker for PRRT2-, TMEM151A-, or PNKD-related disease.

### Genetic testing algorithm

1. Use a multigene paroxysmal movement-disorder/epilepsy panel including at minimum **PRRT2, TMEM151A, PNKD, SLC2A1, KCNMA1, ADCY5, GNAO1, SCN8A, KCNA1, CACNA1A, ATP1A3, RHOBTB2, TBC1D24, PDE2A, DEPDC5, FGF14, GCH1**, and relevant metabolic genes.
2. Ensure deletion/duplication analysis, particularly **16p11.2/PRRT2** and **SLC2A1**.
3. If phenotype is classic familial PKD, PRRT2 sequencing including c.649dupC is a reasonable rapid first test; test TMEM151A in PRRT2-negative cases.
4. Use trio WES/WGS for complex, developmental, or panel-negative disease. WGS offers better CNV, deep-intronic, repeat, and noncoding coverage. Consider high-depth sequencing/another tissue for mosaicism.
5. Interpret variants under ACMG/AMP criteria with segregation and functional evidence. Reduced penetrance means an unaffected carrier does not automatically refute pathogenicity.

NGS diagnostic yields vary from **11–51%** across cohorts; in a literature-enriched 2025 pediatric systematic review, 505/605 (**83.5%**) had a genetic diagnosis involving 38 genes. The difference illustrates major ascertainment effects. (pisano2025paroxysmaldyskinesiasin pages 6-8, harvey2021paroxysmalmovementdisorders pages 1-2)

### Differential diagnosis

Epileptic seizures—including frontal/sleep-related hypermotor epilepsy—functional movement disorder, tics/stereotypies, episodic ataxia, migraine aura/hemiplegic migraine, myotonia, dopa-responsive dystonia, hyperekplexia, panic attacks, syncope, transient ischemia, multiple sclerosis, stroke, structural basal-ganglia lesions, autoimmune encephalitis, drug-induced dyskinesia, and metabolic crises should be considered. Preserved awareness, trigger consistency, normal ictal EEG, and absence of postictal confusion favor PD but are not individually definitive. (gusmao2019paroxysmalmovementdisorders pages 31-34)

**Screening:** no population newborn screen exists. Cascade testing is appropriate after a pathogenic familial variant is identified; prenatal and preimplantation testing are technically possible following genetic counseling.

## 11. Outcome and prognosis

Classic PKD and PNKD do not usually shorten life expectancy, and disease-specific mortality statistics are unavailable. PKD prognosis is generally favorable: attacks respond to treatment and commonly decline between ages 20–30. PNKD often improves with age but may remain medication resistant. GLUT1 deficiency prognosis depends on prompt metabolic treatment and associated developmental/epileptic burden. Severe GNAO1, PIGN, biallelic PRRT2, or developmental channelopathy phenotypes derive morbidity from encephalopathy, epilepsy, status dystonicus, falls, and persistent disability rather than episodic attacks alone. (gusmao2019paroxysmalmovementdisorders pages 1-6, NCT04023656 chunk 1)

Prognostic factors include genotype, biallelic versus monoallelic state, developmental impairment, epilepsy, structural/CNV findings, and treatment response. No validated molecular prognostic biomarker exists. A Korean prospective registry, **NCT04023656**, targets 100 adults and follows remission, ≥50% improvement, worsening, and medication use for up to ten years. (NCT04023656 chunk 1)

## 12. Treatment

### Practical genotype-directed strategy

- **PRRT2/TMEM151A PKD:** low-dose **carbamazepine** or **oxcarbazepine** is first line; lamotrigine, phenytoin, or another antiseizure agent may be alternatives when intolerant. Sodium-channel inhibition is mechanistically consistent with PRRT2-dependent NaV1.2/NaV1.6 dysregulation. Monitor sedation, dizziness, rash, hyponatremia, hepatic/hematologic toxicity, interactions, and ancestry-appropriate HLA risk before carbamazepine. (xu2024paroxysmalkinesigenicdyskinesia pages 5-6, xu2024paroxysmalkinesigenicdyskinesia pages 1-3)
- **Classic PNKD:** avoid caffeine/alcohol and individualized triggers. Clonazepam, diazepam, levetiracetam, valproate, or oxcarbazepine have anecdotal benefit, but response is less reliable than in PKD. (gusmao2019paroxysmalmovementdisorders pages 1-6, harvey2021paroxysmalmovementdisorders pages 2-3)
- **SLC2A1/GLUT1 deficiency:** ketogenic dietary therapy is disease directed; modified Atkins/other ketogenic formulations may be individualized by a metabolic/ketogenic team. Three patients in the landmark SLC2A1 PED/epilepsy study were successfully treated. (suls2008paroxysmalexerciseinduceddyskinesia pages 1-2)
- **ADCY5:** caffeine can paradoxically reduce dyskinesia through adenosine A2A signaling; clonazepam or acetazolamide may help. Severe refractory disease may be considered for globus pallidus deep-brain stimulation (DBS).
- **GNAO1/severe hyperkinetic crises:** intensive supportive management and, in selected refractory cases, DBS.
- **KCNMA1:** dextroamphetamine has helped selected N999S-associated immobility/drop attacks, but evidence is limited. BK-channel inhibition improved D434G mouse phenotypes and remains experimental—not standard human treatment. (park2022bkchannelproperties pages 1-2, dong2022neuronalmechanismof pages 1-2)
- **Metabolic mimics:** treat the defect—e.g., thiamine-responsive pyruvate-dehydrogenase deficiency or dietary management for intermittent maple-syrup-urine disease—rather than treating phenomenology alone. (harvey2021paroxysmalmovementdisorders pages 13-14, harvey2021paroxysmalmovementdisorders pages 3-4)

In the 2025 pediatric review, 97/112 studies reported treatment; 67 used carbamazepine/oxcarbazepine, and 40 studies reported complete resolution, particularly in PRRT2-positive cases. These are study-level—not patient-level—response proportions and should not be interpreted as an unbiased trial rate. (pisano2025paroxysmaldyskinesiasin pages 8-11)

**Advanced therapy:** no approved gene, RNA, or cell therapy exists. Physical/occupational therapy, fall prevention, school/work accommodations, and psychological support address disability; botulinum toxin is rarely relevant unless persistent focal dystonia exists.

**Suggested NCIT intervention concepts:** Carbamazepine; Oxcarbazepine; Clonazepam; Ketogenic Diet; Deep Brain Stimulation; Physical Therapy; Occupational Therapy; Genetic Counseling. Suggested CHEBI entities include carbamazepine **CHEBI:3387**, caffeine **CHEBI:27732**, ethanol **CHEBI:16236**, glucose **CHEBI:17234**, and ketone bodies.

### Current studies

**NCT06701851 (TRIGGER)**, first posted 22 November 2024, is a recruiting French basic-science fMRI/EEG study of controllable PRRT2-related attacks, examining cerebellar, basal-ganglia, cortical, and striato-cerebellar activity; planned enrollment is at least one highly selected participant, so it is mechanistic rather than therapeutic. **NCT04023656** is the Korean ten-year prognosis registry described above. No robust phase II/III disease-modifying drug trial was identified. (NCT06701851 chunk 1, NCT04023656 chunk 1)

## 13. Prevention

Primary prevention of a de novo or inherited pathogenic variant is not available. Reproductive options include cascade testing, partner testing for recessive disease, prenatal diagnosis, and preimplantation genetic testing after nondirective counseling. Secondary prevention consists of early recognition—especially of treatable SLC2A1 disease—and early genotype-directed therapy. Tertiary prevention includes trigger avoidance, medication/diet adherence, seizure control, fall precautions, and emergency plans for severe dyskinetic crises. Vaccination, antimicrobial prophylaxis, and public-health environmental interventions are not disease-specific preventive measures.

## 14. Other species and natural disease

Naturally occurring PD is well documented in **dogs (Canis lupus familiaris; NCBI Taxonomy 9615)** and reported in cats (**Felis catus; Taxonomy 9685**). The 2024 canine review recognizes kinesigenic, non-kinesigenic, and exertion-related forms and recommends history plus video documentation; dogs normally remain conscious and have no postictal phase. (mandigers2024canineparoxysmaldyskinesia—a pages 1-2)

A particularly informative natural model is autosomal-recessive PNKD-like disease in Soft-Coated Wheaten Terriers caused by homozygous **PIGN c.398C>T**, predicted **p.Thr133Ile**. All 25 affected dogs were homozygous, versus 0/1,185 dogs without known PD; attacks lasted minutes to >4 hours and could occur >10/day. The variant reduced cell-surface CD59 in PIGN-null cells, connecting defective GPI-anchor biosynthesis to dyskinesia. This is analogous mechanistically—but not phenotypically identical—to human PIGN developmental epileptic-dyskinetic disease. (kolicheski2017ahomozygouspign pages 1-2)

Other canine entities include BCAN-associated episodic falling and breed-associated syndromes in Border Terriers, Maltese dogs, Markiesjes, Labrador Retrievers, and Jack Russell Terriers; inheritance is not solved in all. There is no zoonotic transmission.

## 15. Model organisms and experimental systems

- **PRRT2 knockout/knockdown mice and patient iPSC neurons:** reproduce increased intrinsic excitability, altered axon-initial-segment/Nav function, abnormal synaptic vesicle handling, and cerebellar network instability. They are strong mechanistic models but do not capture all human trigger specificity or incomplete penetrance. (xu2024paroxysmalkinesigenicdyskinesia pages 5-6)
- **PNKD transgenic mice:** caffeine/alcohol provoke attacks resembling human PNKD. Optical recording showed reduced striatal iMSN firing; chemogenetic iMSN inhibition triggered dyskinesia, and aberrant endocannabinoid-dependent suppression of glutamatergic input was implicated. This is direct cell-type causal evidence in mice. (nelson2022striatalindirectpathway pages 1-2)
- **Kcnma1 knock-in mice:** N999S and D434G GOF models show increased BK current/firing and reduced seizure threshold; N999S mice exhibit stress-induced immobility rescued by acute dextroamphetamine. D434G mice show cortical pyramidal and Purkinje-cell hyperexcitability; paxilline improved seizures and locomotor deficits. Translation is limited because paxilline is not an established safe human therapy. (park2022bkchannelproperties pages 1-2, dong2022neuronalmechanismof pages 1-2)
- **SLC2A1 systems:** Xenopus-oocyte transporter assays establish reduced glucose uptake; mouse models and metabolic studies test cerebral energy failure and ketogenic rescue. (suls2008paroxysmalexerciseinduceddyskinesia pages 1-2)
- **Natural canine PIGN disease:** offers a large-animal, spontaneous recessive model of GPI-anchor-associated PNKD, although canine progression can be more severe than classic human PNKD. (kolicheski2017ahomozygouspign pages 1-2)

Useful resources are MGI/IMSR/MMRRC for mouse alleles, OMIA for inherited animal disease, and breed-specific DNA-test registries. Zebrafish, Drosophila, organoid, and CRISPR-screen findings were not sufficiently represented in the retrieved evidence to support disease-specific conclusions.

## Evidence appraisal and recent developments

The strongest recent advance is the **2024 synthesis of PRRT2 and TMEM151A PKD mechanisms**, integrating ion-channel, transporter, synaptic-vesicle, cerebellar, and systems-circuit evidence. The emerging consensus is that gene-defined PDs are not one “basal-ganglia disease”: they are convergent **synaptopathies, channelopathies, and transportopathies** acting across cerebellar–striatal–cortical networks. (xu2024paroxysmalkinesigenicdyskinesia pages 9-10, xu2024paroxysmalkinesigenicdyskinesia pages 5-6)

The principal limitations are small cohorts, referral bias, limited controlled treatment trials, sparse standardized quality-of-life measurement, and little replicated human multi-omics. Much treatment evidence remains observational. Nonetheless, molecular diagnosis already has immediate real-world utility: PRRT2/TMEM151A predicts sodium-channel-blocker responsiveness, SLC2A1 identifies a treatable cerebral-energy disorder, and pleiotropic genes trigger surveillance for epilepsy and developmental complications. (pisano2025paroxysmaldyskinesiasin pages 8-11, harvey2021paroxysmalmovementdisorders pages 11-12)

**Key primary-literature PMIDs explicitly available in retrieved records:** Bruno diagnostic criteria—**PMID 15623687**; Mao genotype–phenotype cohort—**PMID 24661410**; Li PRRT2/drug response—**PMID 23535490**; Gardiner clinical/genetic heterogeneity—**PMID 26598494**; Méneret European PRRT2 cohort—**PMID 22744660**. Full DOI/URL examples include Xu et al., published online 13 December 2023/2024 issue, https://doi.org/10.1007/s12264-023-01157-z; Nelson et al., 30 March 2022, https://doi.org/10.1523/JNEUROSCI.1614-20.2022; Park et al., 12 July 2022, https://doi.org/10.7554/eLife.77953; Suls et al., 26 June 2008, https://doi.org/10.1093/brain/awn113; and Mandigers et al., 18 July 2024, https://doi.org/10.3389/fvets.2024.1441332. (xu2024paroxysmalkinesigenicdyskinesia pages 1-3, nelson2022striatalindirectpathway pages 1-2, mandigers2024canineparoxysmaldyskinesia—a pages 1-2, park2022bkchannelproperties pages 1-2, NCT04023656 chunk 1)

References

1. (harvey2021paroxysmalmovementdisorders pages 1-2): Susan Harvey, Mary D. King, and Kathleen M. Gorman. Paroxysmal movement disorders. Jun 2021. URL: https://doi.org/10.3389/fneur.2021.659064, doi:10.3389/fneur.2021.659064. This article has 47 citations and is from a peer-reviewed journal.

2. (pisano2025paroxysmaldyskinesiasin pages 1-2): Giulia Pisanò, Martina Gnazzo, Giulia Sigona, Carlo Alberto Cesaroni, Agnese Pantani, Anna Cavalli, Susanna Rizzi, Daniele Frattini, and Carlo Fusco. Paroxysmal dyskinesias in paediatric age: a systematic review. Journal of Clinical Medicine, 14:5925, Aug 2025. URL: https://doi.org/10.3390/jcm14175925, doi:10.3390/jcm14175925. This article has 6 citations.

3. (xu2024paroxysmalkinesigenicdyskinesia pages 1-3): Jiao-Jiao Xu, Hong-Fu Li, and Zhi-Ying Wu. Paroxysmal kinesigenic dyskinesia: genetics and pathophysiological mechanisms. Neuroscience Bulletin, 40:952-962, Dec 2024. URL: https://doi.org/10.1007/s12264-023-01157-z, doi:10.1007/s12264-023-01157-z. This article has 28 citations and is from a peer-reviewed journal.

4. (harvey2021paroxysmalmovementdisorders pages 2-3): Susan Harvey, Mary D. King, and Kathleen M. Gorman. Paroxysmal movement disorders. Jun 2021. URL: https://doi.org/10.3389/fneur.2021.659064, doi:10.3389/fneur.2021.659064. This article has 47 citations and is from a peer-reviewed journal.

5. (harvey2021paroxysmalmovementdisorders pages 3-4): Susan Harvey, Mary D. King, and Kathleen M. Gorman. Paroxysmal movement disorders. Jun 2021. URL: https://doi.org/10.3389/fneur.2021.659064, doi:10.3389/fneur.2021.659064. This article has 47 citations and is from a peer-reviewed journal.

6. (NCT06701851 chunk 1):  Neural Correlates of Movement Disorders Associated With PRRT2 Related Paroxysmal Kinesigenic Dyskinesia - an Ancillary Study of AMEDYST Research. Institut National de la Santé Et de la Recherche Médicale, France. 2025. ClinicalTrials.gov Identifier: NCT06701851

7. (pisano2025paroxysmaldyskinesiasin pages 8-11): Giulia Pisanò, Martina Gnazzo, Giulia Sigona, Carlo Alberto Cesaroni, Agnese Pantani, Anna Cavalli, Susanna Rizzi, Daniele Frattini, and Carlo Fusco. Paroxysmal dyskinesias in paediatric age: a systematic review. Journal of Clinical Medicine, 14:5925, Aug 2025. URL: https://doi.org/10.3390/jcm14175925, doi:10.3390/jcm14175925. This article has 6 citations.

8. (gusmao2019paroxysmalmovementdisorders pages 31-34): Claudio M. De Gusmao and Laura Silveira-Moriyama. Paroxysmal movement disorders – practical update on diagnosis and management. Expert Review of Neurotherapeutics, 19:807-822, Aug 2019. URL: https://doi.org/10.1080/14737175.2019.1648211, doi:10.1080/14737175.2019.1648211. This article has 39 citations and is from a peer-reviewed journal.

9. (xu2024paroxysmalkinesigenicdyskinesia pages 9-10): Jiao-Jiao Xu, Hong-Fu Li, and Zhi-Ying Wu. Paroxysmal kinesigenic dyskinesia: genetics and pathophysiological mechanisms. Neuroscience Bulletin, 40:952-962, Dec 2024. URL: https://doi.org/10.1007/s12264-023-01157-z, doi:10.1007/s12264-023-01157-z. This article has 28 citations and is from a peer-reviewed journal.

10. (xu2024paroxysmalkinesigenicdyskinesia pages 3-5): Jiao-Jiao Xu, Hong-Fu Li, and Zhi-Ying Wu. Paroxysmal kinesigenic dyskinesia: genetics and pathophysiological mechanisms. Neuroscience Bulletin, 40:952-962, Dec 2024. URL: https://doi.org/10.1007/s12264-023-01157-z, doi:10.1007/s12264-023-01157-z. This article has 28 citations and is from a peer-reviewed journal.

11. (harvey2021paroxysmalmovementdisorders pages 11-12): Susan Harvey, Mary D. King, and Kathleen M. Gorman. Paroxysmal movement disorders. Jun 2021. URL: https://doi.org/10.3389/fneur.2021.659064, doi:10.3389/fneur.2021.659064. This article has 47 citations and is from a peer-reviewed journal.

12. (suls2008paroxysmalexerciseinduceddyskinesia pages 1-2): A. Suls, P. Dedeken, K. Goffin, H. Van Esch, P. Dupont, D. Cassiman, J. Kempfle, T. V. Wuttke, Y. Weber, H. Lerche, Z. Afawi, W. Vandenberghe, A. D. Korczyn, S. F. Berkovic, D. Ekstein, S. Kivity, P. Ryvlin, L. R. F. Claes, L. Deprez, S. Maljevic, A. Vargas, T. Van Dyck, D. Goossens, J. Del-Favero, K. Van Laere, P. De Jonghe, and W. Van Paesschen. Paroxysmal exercise-induced dyskinesia and epilepsy is due to mutations in slc2a1, encoding the glucose transporter glut1. Brain, 131:1831-1844, Jun 2008. URL: https://doi.org/10.1093/brain/awn113, doi:10.1093/brain/awn113. This article has 419 citations and is from a highest quality peer-reviewed journal.

13. (dong2022neuronalmechanismof pages 1-2): Ping Dong, Yang Zhang, Arsen S. Hunanyan, Mohamad A. Mikati, Jianmin Cui, and Huanghe Yang. Neuronal mechanism of a bk channelopathy in absence epilepsy and dyskinesia. Proceedings of the National Academy of Sciences of the United States of America, Mar 2022. URL: https://doi.org/10.1073/pnas.2200140119, doi:10.1073/pnas.2200140119. This article has 35 citations and is from a highest quality peer-reviewed journal.

14. (pisano2025paroxysmaldyskinesiasin pages 4-6): Giulia Pisanò, Martina Gnazzo, Giulia Sigona, Carlo Alberto Cesaroni, Agnese Pantani, Anna Cavalli, Susanna Rizzi, Daniele Frattini, and Carlo Fusco. Paroxysmal dyskinesias in paediatric age: a systematic review. Journal of Clinical Medicine, 14:5925, Aug 2025. URL: https://doi.org/10.3390/jcm14175925, doi:10.3390/jcm14175925. This article has 6 citations.

15. (pisano2025paroxysmaldyskinesiasin pages 11-12): Giulia Pisanò, Martina Gnazzo, Giulia Sigona, Carlo Alberto Cesaroni, Agnese Pantani, Anna Cavalli, Susanna Rizzi, Daniele Frattini, and Carlo Fusco. Paroxysmal dyskinesias in paediatric age: a systematic review. Journal of Clinical Medicine, 14:5925, Aug 2025. URL: https://doi.org/10.3390/jcm14175925, doi:10.3390/jcm14175925. This article has 6 citations.

16. (xu2024paroxysmalkinesigenicdyskinesia pages 5-6): Jiao-Jiao Xu, Hong-Fu Li, and Zhi-Ying Wu. Paroxysmal kinesigenic dyskinesia: genetics and pathophysiological mechanisms. Neuroscience Bulletin, 40:952-962, Dec 2024. URL: https://doi.org/10.1007/s12264-023-01157-z, doi:10.1007/s12264-023-01157-z. This article has 28 citations and is from a peer-reviewed journal.

17. (NCT04023656 chunk 1): Han-Joon Kim. Prognosis of Paroxysmal Kinesigenic Choreoathetosis in Korea. Seoul National University Hospital. 2016. ClinicalTrials.gov Identifier: NCT04023656

18. (gusmao2019paroxysmalmovementdisorders pages 1-6): Claudio M. De Gusmao and Laura Silveira-Moriyama. Paroxysmal movement disorders – practical update on diagnosis and management. Expert Review of Neurotherapeutics, 19:807-822, Aug 2019. URL: https://doi.org/10.1080/14737175.2019.1648211, doi:10.1080/14737175.2019.1648211. This article has 39 citations and is from a peer-reviewed journal.

19. (nelson2022striatalindirectpathway pages 1-2): Alexandra B. Nelson, Allison E. Girasole, Hsien-Yang Lee, Louis J. Ptáček, and Anatol C. Kreitzer. Striatal indirect pathway dysfunction underlies motor deficits in a mouse model of paroxysmal dyskinesia. The Journal of Neuroscience, 42:2835-2848, Feb 2022. URL: https://doi.org/10.1523/jneurosci.1614-20.2022, doi:10.1523/jneurosci.1614-20.2022. This article has 17 citations.

20. (park2022bkchannelproperties pages 1-2): Su Mi Park, Cooper E Roache, Philip H Iffland, Hans J Moldenhauer, Katia K Matychak, Amber E Plante, Abby G Lieberman, Peter B Crino, and Andrea Meredith. Bk channel properties correlate with neurobehavioral severity in three kcnma1-linked channelopathy mouse models. Jul 2022. URL: https://doi.org/10.7554/elife.77953, doi:10.7554/elife.77953. This article has 37 citations and is from a domain leading peer-reviewed journal.

21. (harvey2021paroxysmalmovementdisorders pages 7-8): Susan Harvey, Mary D. King, and Kathleen M. Gorman. Paroxysmal movement disorders. Jun 2021. URL: https://doi.org/10.3389/fneur.2021.659064, doi:10.3389/fneur.2021.659064. This article has 47 citations and is from a peer-reviewed journal.

22. (pisano2025paroxysmaldyskinesiasin pages 6-8): Giulia Pisanò, Martina Gnazzo, Giulia Sigona, Carlo Alberto Cesaroni, Agnese Pantani, Anna Cavalli, Susanna Rizzi, Daniele Frattini, and Carlo Fusco. Paroxysmal dyskinesias in paediatric age: a systematic review. Journal of Clinical Medicine, 14:5925, Aug 2025. URL: https://doi.org/10.3390/jcm14175925, doi:10.3390/jcm14175925. This article has 6 citations.

23. (harvey2021paroxysmalmovementdisorders pages 13-14): Susan Harvey, Mary D. King, and Kathleen M. Gorman. Paroxysmal movement disorders. Jun 2021. URL: https://doi.org/10.3389/fneur.2021.659064, doi:10.3389/fneur.2021.659064. This article has 47 citations and is from a peer-reviewed journal.

24. (mandigers2024canineparoxysmaldyskinesia—a pages 1-2): Paul J. J. Mandigers, Koen M. Santifort, Mark Lowrie, and Laurent Garosi. Canine paroxysmal dyskinesia—a review. Frontiers in Veterinary Science, Jul 2024. URL: https://doi.org/10.3389/fvets.2024.1441332, doi:10.3389/fvets.2024.1441332. This article has 11 citations and is from a peer-reviewed journal.

25. (kolicheski2017ahomozygouspign pages 1-2): Ana L. Kolicheski, Gary S. Johnson, Tendai Mhlanga-Mutangadura, Jeremy F. Taylor, Robert D. Schnabel, Taroh Kinoshita, Yoshiko Murakami, and Dennis P. O’Brien. A homozygous pign missense mutation in soft-coated wheaten terriers with a canine paroxysmal dyskinesia. Neurogenetics, 18:39-47, Nov 2017. URL: https://doi.org/10.1007/s10048-016-0502-4, doi:10.1007/s10048-016-0502-4. This article has 41 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Paroxysmal_Dyskinesia-deep-research-falcon_artifacts/artifact-00.md)