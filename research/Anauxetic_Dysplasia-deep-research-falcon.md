---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-01T13:12:14.422490'
end_time: '2026-08-01T13:19:23.234207'
duration_seconds: 428.81
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Anauxetic dysplasia
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 25
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Anauxetic_Dysplasia-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Anauxetic dysplasia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Anauxetic dysplasia** covering all of the
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
- **Disease Name:** Anauxetic dysplasia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Anauxetic dysplasia** covering all of the
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


# Anauxetic Dysplasia: Disease-Characteristics Research Report

## Executive summary

Anauxetic dysplasia (ANXD) is an ultra-rare, congenital, autosomal-recessive skeletal dysplasia at the severe end of the cartilage-hair hypoplasia–anauxetic dysplasia (CHH–AD) spectrum. Three molecular forms are recognized: **ANXD1—RMRP**, **ANXD2—POP1**, and **ANXD3—NEPRO/C3orf17**. The shared phenotype comprises extreme disproportionate short stature, brachydactyly, ligamentous laxity, joint hypermobility/dislocation, and severe spondylo-epi-metaphyseal abnormalities. Unlike classic cartilage-hair hypoplasia, “pure” ANXD usually lacks hypotrichosis, anemia, clinically important immunodeficiency, intestinal dysmotility, and established cancer predisposition, although the boundary is a spectrum and isolated extraskeletal findings require continued surveillance. (remmelzwaal2023expandingthephenotype pages 1-2, thiel2007typeandlevel pages 1-2)

The best-supported causal chain is **biallelic disruption of an RNase-MRP component or interactor → defective pre-rRNA processing/ribosome biogenesis → impaired growth-plate chondrocyte differentiation and hypertrophy → disorganized endochondral ossification → severe short-limb dwarfism and skeletal deformity**. This mechanism is strongest for RMRP and POP1; the precise function of NEPRO remains less resolved. No disease-modifying therapy, approved targeted drug, or ANXD-specific interventional trial was identified. Current care is supportive, orthopedic, rehabilitative, dental, and surveillance-based.

| Subtype | Causal gene / product | OMIM disease ID | Inheritance | Defining phenotype | Representative variants | Key evidence / limitations |
|---|---|---|---|---|---|---|
| ANXD1 | **RMRP** / noncoding RNA component of RNase MRP | **607095** | **Autosomal recessive; ultra-rare** | Most severe end of the CHH-AD spectrum; prenatal-onset extreme disproportionate short stature, severe spondyloepimetaphyseal dysplasia, brachydactyly, joint laxity, hypodontia; typically lacks the immunodeficiency/anemia/malignancy predisposition more characteristic of CHH (thiel2007typeandlevel pages 1-2, remmelzwaal2023expandingthephenotype pages 1-2) | **g.111_112insACTGTAGACATTCCT**, **g.90_91AG>GC**, **g.254C>G**; severe case with **g.195C>T** plus null **g.254_263delCTCAGCGCGG** (thiel2007typeandlevel pages 5-6, thiel2007typeandlevel pages 3-4, thiel2007typeandlevel pages 1-2, thiel2007typeandlevel pages 6-8) | Best mechanistic evidence among ANXD subtypes: RMRP mutations impair RNase MRP-mediated **pre-rRNA cleavage**, correlating with bone-dysplasia severity; reduced **cyclin B2 mRNA cleavage** tracks more with hair/immuno-hematologic features than with ANXD itself (thiel2007typeandlevel pages 1-2, thiel2007typeandlevel pages 6-8). Limitation: much evidence derives from the broader CHH-AD spectrum rather than large ANXD1 cohorts. |
| ANXD2 | **POP1** / hPOP1 protein, shared subunit of RNase MRP and RNase P complexes | **617396** | **Autosomal recessive; ultra-rare** | ANXD-like skeletal dysplasia spanning mild to severe presentations, including severe short stature and extensive skeletal abnormalities; considered part of the RNase-MRP–related skeletal dysplasia spectrum (barrazagarcia2017broadeningthephenotypic pages 1-2, remmelzwaal2023expandingthephenotype pages 1-2) | **p.Pro582Ser**, **p.Glu870fs*5**, **p.Asp511Tyr** (biallelic) (barrazagarcia2017broadeningthephenotypic pages 1-2) | Human evidence shows **markedly reduced RMRP abundance** and **elevated pre-5.8S rRNA** in at least one proband, supporting disturbed ribosome/RNase-MRP biology (barrazagarcia2017broadeningthephenotypic pages 1-2). Limitation: very small number of reported families/patients; phenotypic boundaries between mild POP1 skeletal dysplasia and ANXD2 remain incompletely defined. |
| ANXD3 | **NEPRO (C3orf17)** / NEPRO protein, reported to interact with RNase MRP subunits | **618853** | **Autosomal recessive; ultra-rare** | Severe short stature, brachydactyly, skin laxity, joint hypermobility/dislocations, platyspondyly/ovoid vertebrae, hypoplastic ilia/acetabulae, small femoral epiphyses, irregular metaphyses; 2023 case expanded phenotype to **atlantoaxial subluxation**, **dental anomalies**, and **sagittal craniosynostosis/scaphocephaly** (remmelzwaal2023expandingthephenotype pages 1-2, remmelzwaal2023expandingthephenotype pages 4-4, remmelzwaal2023expandingthephenotype pages 3-4) | Homozygous **c.280C>T, p.Arg94Cys** (apparent recurrent/founder variant in several reported patients) (remmelzwaal2023expandingthephenotype pages 4-4, remmelzwaal2023expandingthephenotype pages 1-2) | Recent direct evidence is strongest at the case-report level: before the 2023 report, only **five** ANXD3 patients had been described; the 2023 paper added one more and broadened the recognized phenotype (remmelzwaal2023expandingthephenotype pages 1-2, remmelzwaal2023expandingthephenotype pages 4-4). Limitation: mechanism is less resolved than for RMRP; patient numbers remain extremely small. |
| Cross-subtype summary | **RMRP / POP1 / NEPRO** | ANXD1 **607095**; ANXD2 **617396**; ANXD3 **618853** | **All currently recognized ANXD subtypes are autosomal recessive and ultra-rare** | Shared core picture: severe prenatal/early-childhood growth failure with marked skeletal dysplasia; subtype-specific extraskeletal findings are limited and evidence is mostly from individual case reports or tiny series (remmelzwaal2023expandingthephenotype pages 1-2, thiel2007typeandlevel pages 1-2) | Subtype-defining variants are heterogeneous except for recurrent **NEPRO p.Arg94Cys** in ANXD3 and multiple recurrent **RMRP** alleles in the CHH-AD spectrum (remmelzwaal2023expandingthephenotype pages 4-4, thiel2007typeandlevel pages 2-3, thiel2007typeandlevel pages 1-2) | Knowledge base should treat ANXD as an **ultra-rare Mendelian skeletal dysplasia with sparse epidemiology**: prevalence/incidence, penetrance, survival, and genotype-specific prognosis are not well quantified in current literature (remmelzwaal2023expandingthephenotype pages 1-2, barrazagarcia2017broadeningthephenotypic pages 1-2). |


*Table: This table summarizes the three recognized anauxetic dysplasia subtypes by gene, OMIM identifier, inheritance, phenotype, representative variants, and evidence strength. It is useful as a compact knowledge-base overview while highlighting that all forms are autosomal recessive and exceptionally rare.*

## 1. Disease information

### Definition and classification

ANXD is a Mendelian skeletal disorder characterized by prenatal-onset growth failure and severe spondyloepimetaphyseal dysplasia. A 2023 primary report describes it as “a rare autosomal recessive skeletal disorder at the severe end” of the CHH–AD spectrum and recognizes three types. (remmelzwaal2023expandingthephenotype pages 1-2)

**Recognized molecular types and identifiers**

- **ANXD1:** OMIM **#607095**, caused by biallelic **RMRP** variants.
- **ANXD2:** OMIM **#617396**, caused by biallelic **POP1** variants.
- **ANXD3:** OMIM **#618853**, caused by biallelic **NEPRO**, formerly **C3orf17**, variants. (remmelzwaal2023expandingthephenotype pages 1-2)

A definitive MONDO identifier was not established in the retrieved primary literature and should be verified directly against the current MONDO release before database ingestion. Likewise, no dedicated MeSH, ICD-10, or ICD-11 code was demonstrated. In routine coding, ANXD will generally fall under broader congenital osteochondrodysplasia/skeletal-dysplasia categories; such parent codes should not be represented as disease-specific identifiers.

**Synonyms:** anauxetic dysplasia; anauxetic dysplasia type 1/2/3; ANXD/AD; RMRP-related anauxetic dysplasia; POP1-related skeletal dysplasia/anauxetic dysplasia; NEPRO-related anauxetic dysplasia; severe end of the cartilage-hair hypoplasia–anauxetic dysplasia spectrum. “AD” is ambiguous with autosomal dominant inheritance and should be avoided in knowledge-base displays.

**Source granularity:** OMIM/nosology-style statements are aggregated disease-level assertions, whereas much of the phenotype and natural-history evidence comes from individual patients or very small families. The 2023 ANXD3 publication was a single-patient case report; only five ANXD3 patients had been reported previously. (remmelzwaal2023expandingthephenotype pages 1-2, remmelzwaal2023expandingthephenotype pages 4-4)

## 2. Etiology

### Causal factors

ANXD is genetic. All recognized forms result from **germline biallelic variants** in genes connected to RNase MRP/ribosome biology:

1. **RMRP:** encodes the untranslated RNA component of RNase MRP.
2. **POP1:** encodes a protein subunit shared by RNase MRP and RNase P and involved in complex assembly/stability.
3. **NEPRO:** encodes an RNase-MRP-associated protein; its disease mechanism is incompletely defined. (remmelzwaal2023expandingthephenotype pages 1-2, barrazagarcia2017broadeningthephenotypic pages 1-2, steinbusch2017expressionofrmrp pages 1-2)

### Genetic risk

The principal risk factor is inheriting one pathogenic allele from each carrier parent. Consanguinity increases the chance that both parents carry the same rare allele. The recurrent homozygous **NEPRO c.280C>T, p.(Arg94Cys)** allele was found in several consanguineous Arabic families and was characterized as an apparent founder mutation. (remmelzwaal2023expandingthephenotype pages 4-4)

No validated susceptibility loci, polygenic-risk scores, or modifier genes are established. Variable manifestations with similar RMRP genotypes suggest possible nonallelic modifiers, but these remain unidentified. (thiel2007typeandlevel pages 6-8)

### Environmental, infectious, lifestyle, and protective factors

No toxin, infection, radiation exposure, diet, smoking behavior, or other environmental factor is known to cause ANXD. No genetic or environmental protective factor has been validated. Environmental circumstances may modify complications—falls or high-risk neck movement could worsen atlantoaxial instability—but do not cause the disorder. Gene–environment interaction studies specific to ANXD were not identified.

## 3. Phenotypes

### Core phenotype

The common phenotype comprises severe or extreme disproportionate short stature, short limbs, brachydactyly, skin laxity, ligamentous/joint laxity, joint hypermobility or dislocations, and extensive axial and appendicular skeletal dysplasia. (remmelzwaal2023expandingthephenotype pages 1-2)

| Manifestation | Type, onset, course, and impact | Suggested HPO term |
|---|---|---|
| Disproportionate short stature | Clinical sign; prenatal/congenital; severe and progressive relative growth deficit; major mobility and accessibility burden | Disproportionate short stature, **HP:0003498**; Short stature, **HP:0004322** |
| Short limbs/long-bone shortening | Sign; prenatal or neonatal; lifelong | Rhizomelia, **HP:0008905**, or mesomelia, **HP:0003027**, where anatomically documented |
| Brachydactyly; short broad/bullet-shaped phalanges | Physical/radiographic sign; childhood; persistent | Brachydactyly, **HP:0001156** |
| Metaphyseal irregularity/widening | Radiographic sign; childhood and progressive during growth | Metaphyseal abnormality, **HP:0000944** |
| Epiphyseal hypoplasia/premature fusion | Radiographic sign; childhood; can drive growth arrest and joint deformity | Small epiphyses, **HP:0010585**; premature epiphyseal fusion where supported |
| Spondyloepimetaphyseal dysplasia/vertebral abnormalities | Radiographic sign; congenital/childhood; scoliosis may progress | Platyspondyly, **HP:0000926**; Abnormal vertebral morphology, **HP:0003468** |
| Scoliosis/kyphosis/gibbus | Sign; often progressive | Scoliosis, **HP:0002650**; Kyphosis, **HP:0002808** |
| Coxa vara, hip dysplasia/ankylosis | Sign; childhood; may impair walking and cause pain | Coxa vara, **HP:0002812**; Hip dysplasia, **HP:0001385** |
| Joint hypermobility/laxity/dislocation | Sign; congenital/childhood; functional instability and pain | Joint hypermobility, **HP:0001382**; Joint dislocation, **HP:0001373** |
| Hypodontia/dental anomalies | Sign; childhood as dentition develops; impacts mastication and dental care | Hypodontia, **HP:0000668**; Microdontia, **HP:0000691**; Enamel hypoplasia, **HP:0006297** |
| Atlantoaxial instability/subluxation | Potentially severe complication; risk of cervical myelopathy and anesthesia-related injury | Atlantoaxial instability, **HP:0003467** |
| Craniosynostosis/scaphocephaly | Rare/newly expanded ANXD3 phenotype | Craniosynostosis, **HP:0001363**; Scaphocephaly, **HP:0030799** |
| Developmental delay/intellectual impairment | Not universal; mild delay reported in some cases | Global developmental delay, **HP:0001263**; Intellectual disability, **HP:0001249** |

In an RMRP-related 11-year-old, short limbs were visible by prenatal ultrasound at approximately 17 weeks. Birth length was 39 cm, below −5 SD; height at nine years was 83 cm, approximately −8 SD. She developed progressive scoliosis and lower-limb joint pain but had normal hair and psychomotor development. Radiographs showed shortened tubular bones, widened irregular metaphyses, small epiphyses, premature growth-plate fusion, brachydactyly, coxa vara, and dysplastic femoral heads. (thiel2007typeandlevel pages 2-3, thiel2007typeandlevel pages 3-4)

Historical descriptions place adult height below approximately 85 cm in severe RMRP-associated ANXD, but this is based on very small samples rather than a population estimate. (park2024cartilagehairhypoplasia–anauxeticdysplasia pages 2-4)

### ANXD3 phenotype expansion in 2023

A seven-year-old homozygous for **NEPRO p.Arg94Cys** had atlantoaxial subluxation, sagittal-suture craniosynostosis with scaphocephaly, Madelung deformity, and extensive dental abnormalities, including agenesis, microdontia, short roots, taurodontism, enamel hypoplasia, and abnormal crowns. The authors’ abstract states: “Greater awareness of the possibility of atlantoaxial subluxation, dental anomalies, and craniosynostosis may lead to more timely diagnosis and treatment.” (remmelzwaal2023expandingthephenotype pages 4-4, remmelzwaal2023expandingthephenotype pages 3-4)

Motor/cognitive delay and recurrent airway infections occurred in that patient, but congenital ichthyosis was attributable to a separate homozygous **ALOX12B** variant; therefore, those findings should not automatically be assigned to ANXD3. (remmelzwaal2023expandingthephenotype pages 4-4)

### Frequency and quality of life

Reliable percentages are unavailable because cohorts are exceptionally small. Severe short stature and skeletal abnormalities are defining and expected to be common; craniosynostosis, atlantoaxial subluxation, and detailed dental anomalies currently have case-level evidence. No ANXD-specific EQ-5D, SF-36, PROMIS, or disease-specific quality-of-life study was identified. Likely burdens include restricted mobility, pain, spinal and hip deformity, need for adapted environments, dental morbidity, repeated imaging/surgery, and cervical-safety concerns.

## 4. Genetic and molecular information

### Genes and representative variants

- **RMRP:** noncoding RNA gene on chromosome 9p13. Representative severe alleles include **g.111_112insACTGTAGACATTCCT**, **g.90_91AG>GC**, **g.254C>G**, and the null deletion **g.254_263delCTCAGCGCGG**. A severe patient was compound heterozygous for **g.195C>T** and **g.254_263delCTCAGCGCGG**; both were absent from 378 control chromosomes. (thiel2007typeandlevel pages 5-6, thiel2007typeandlevel pages 3-4, thiel2007typeandlevel pages 1-2)
- **POP1:** reported ANXD-spectrum variants include compound-heterozygous **p.Pro582Ser/p.Glu870fs*5** and homozygous **p.Asp511Tyr**. The former combines a missense and frameshift allele; the latter is missense. (barrazagarcia2017broadeningthephenotypic pages 1-2)
- **NEPRO:** homozygous **NM_015412.4:c.280C>T, p.(Arg94Cys)** is the best-documented recurrent ANXD3 allele. (remmelzwaal2023expandingthephenotype pages 4-4)

These are germline variants. There is no evidence that somatic mutation is relevant. Current population allele frequencies were not available in the retrieved papers and should be queried directly in gnomAD by transcript/build before ingestion. Given recessive severe disease and very small case numbers, causal alleles are expected to be rare, but absence from a population database alone is not proof of pathogenicity.

### Functional consequences

The RMRP deletion **g.254_263delCTCAGCGCGG** was undetectable by RT-PCR and interpreted as an unstable-RNA/null allele. Disease-causing RMRP changes cluster in conserved nucleotides or disrupt stem pairing, affecting RNA structure, protein binding, RNA stability, or transcription. (thiel2007typeandlevel pages 5-6, thiel2007typeandlevel pages 6-8)

In POP1-associated disease, **p.Pro582Ser/p.Glu870fs*5** was associated with markedly reduced RMRP abundance and increased pre-5.8S rRNA, supporting impaired RNase-MRP function. (barrazagarcia2017broadeningthephenotypic pages 1-2)

ClinVar classifications must be checked at accession level and date of use. The retrieved literature describes the RMRP and recurrent NEPRO alleles as pathogenic/disease-causing, while a 2024 broader CHH-spectrum case illustrates that WES can return a pathogenic allele paired with a VUS; such combinations require phenotype, segregation, and functional review rather than automatic confirmation. (park2024cartilagehairhypoplasia–anauxeticdysplasia pages 2-4)

No validated ANXD modifier gene, disease-specific epigenetic signature, recurrent chromosomal abnormality, methylation abnormality, or structural-variant mechanism was established.

## 5. Environmental information

ANXD is not an infectious, toxic, occupational, lifestyle, or nutritional disease. No causal infectious agent or preventable exposure is known. Standard nutrition and activity adapted to orthopedic limitations support general health but do not reverse the molecular defect. Cervical instability warrants avoidance of unassessed high-impact activities and careful airway/neck positioning, especially during anesthesia. (remmelzwaal2023expandingthephenotype pages 3-4)

## 6. Mechanism and pathophysiology

### Upstream molecular defect

RNase MRP is a ribonucleoprotein endoribonuclease containing RMRP lncRNA and protein subunits including POP1. It participates in ITS1 pre-rRNA cleavage and has reported roles in cyclin-B2 mRNA cleavage and cell-cycle regulation. (steinbusch2017expressionofrmrp pages 1-2)

For RMRP disease, functional testing of 13 variants found a strong negative correlation between bone-dysplasia severity and rRNA-cleavage activity (**R = −0.8346, P = .0008**). Impaired mRNA cleavage correlated with immunologic/hematologic abnormalities (**R = −0.8429, P = .0007**) and hair hypoplasia (**R = −0.8115, P = .001**). Thus, severe impairment of rRNA processing primarily predicts ANXD’s skeletal phenotype, whereas impaired mRNA/cell-cycle regulation better predicts CHH-like extraskeletal findings. (thiel2007typeandlevel pages 5-6, thiel2007typeandlevel pages 1-2)

A key direct statement from the landmark paper is: “the impairment of rRNA cleavage by RMRP mutations is the leading cause of bone dysplasia in patients with features in the CHH-AD spectrum.” (thiel2007typeandlevel pages 6-8)

### Cellular and tissue cascade

1. Biallelic RMRP/POP1/NEPRO dysfunction alters RNase-MRP-associated biology.
2. Pre-rRNA processing and ribosome production become abnormal; RMRP instability or reduced abundance may worsen the defect.
3. Highly proliferative growth-plate chondrocytes fail to execute normal proliferative-to-hypertrophic differentiation.
4. Columnization, matrix production/mineralization, and endochondral ossification are disrupted.
5. Longitudinal bone growth fails, producing severe metaphyseal, epiphyseal, vertebral, pelvic, and digital abnormalities.

Histologic description in ANXD includes few dispersed chondrocytes, almost absent columnization, and irregular osteochondral ossification. (thiel2007typeandlevel pages 1-2)

In ATDC5 chondrocytes, Rmrp knockdown increased RNase-MRP substrates and an ITS1 processing intermediate, reduced 18S and 5.8S rRNA, and decreased **Sox9, Col2a1, Runx2, Col10a1**, and **Alpl**, with particularly strong effects on hypertrophic differentiation. (steinbusch2017expressionofrmrp pages 7-9)

Rmrp promoter activity responded experimentally to developmental mediators: PTHrP −18%, FGF2 −35%, TGF-β3 +40%, BMP2 +105%, dorsomorphin −76%, WNT3A +45%, and WNT5A +26%. These data show pathway responsiveness, not that any of these factors is an established therapy. (steinbusch2017expressionofrmrp pages 7-9)

### Suggested ontology annotations

- **GO biological process:** rRNA processing (**GO:0006364**); ribosome biogenesis (**GO:0042254**); chondrocyte differentiation (**GO:0002062**); chondrocyte hypertrophy (**GO:0003415**); endochondral ossification (**GO:0001958**); regulation of cell cycle (**GO:0051726**).
- **GO cellular component:** RNase MRP complex (**GO:0000172**); nucleolus (**GO:0005730**); nucleus (**GO:0005634**).
- **Cell Ontology:** chondrocyte (**CL:0000138**); hypertrophic chondrocyte and osteoblast should be mapped to the current CL release.

No ANXD-specific single-cell, spatial-transcriptomic, proteomic, metabolomic, lipidomic, epigenomic, organoid, or multi-omics atlas was found. The available molecular profiling is targeted and preclinical.

## 7. Anatomical structures affected

**Primary system:** musculoskeletal/connective-tissue system, particularly growth plates and endochondrally formed skeleton.

**Primary sites:** vertebral column, metaphyses and epiphyses of long bones, pelvis/ilia/acetabula, proximal femur and femoral neck, knees, ankles, radius/ulna, metacarpals, phalanges, hips, and craniovertebral junction. Dentition and cranial sutures can be involved, especially in reported ANXD3. (remmelzwaal2023expandingthephenotype pages 1-2, remmelzwaal2023expandingthephenotype pages 3-4, thiel2007typeandlevel pages 3-4)

Suggested UBERON mappings include growth plate cartilage (**UBERON:0003986**), cartilage tissue (**UBERON:0002418**), vertebral column (**UBERON:0001130**), pelvis (**UBERON:0001270**), femur (**UBERON:0000981**), hand skeleton, tooth, and cranial suture; exact release-specific identifiers should be validated.

At tissue level, proliferative and hypertrophic growth-plate chondrocytes and their extracellular matrix are central. Downstream osteoblast/osteoclast remodeling is likely affected through abnormal cartilage scaffolding, but direct ANXD cell-specific evidence is limited. At subcellular level, the nucleolus/nucleus and RNase-MRP ribonucleoprotein complex are implicated. Findings are generally bilateral/generalized rather than unilateral; leg-length discrepancy can be asymmetric in individual patients. (remmelzwaal2023expandingthephenotype pages 3-4, steinbusch2017expressionofrmrp pages 1-2)

## 8. Temporal development

ANXD begins prenatally or congenitally and follows a chronic lifelong course. Short limbs may be recognized on second-trimester ultrasound, and extreme short length is present at birth. Skeletal disproportionality, scoliosis, joint pain, deformity, and premature growth-plate fusion become more apparent during childhood. (thiel2007typeandlevel pages 2-3, thiel2007typeandlevel pages 3-4)

There is no validated stage system. A practical clinical framework is:

- **Prenatal/neonatal:** short limbs and marked birth-length deficit.
- **Early childhood:** progressive growth failure, metaphyseal/epiphyseal changes, brachydactyly and laxity.
- **Later childhood/adolescence:** increasing scoliosis/kyphosis, hip and limb deformity, joint pain, premature physeal fusion, and possible cervical instability.
- **Adulthood:** lifelong extreme short stature and orthopedic disability; robust adult natural-history data are lacking.

There is no spontaneous remission. Growth-plate development is the key vulnerability window, but no proven molecular intervention exists during that period.

## 9. Inheritance and population

Inheritance is autosomal recessive. For two confirmed carrier parents, each pregnancy has a 25% probability of an affected child, 50% probability of an unaffected carrier, and 25% probability of inheriting neither familial allele.

Penetrance is presumed high for individuals with two severe pathogenic alleles, but it has not been quantified. Expressivity is variable, especially across RMRP and POP1 allelic combinations. Anticipation is not expected. Germline mosaicism has not been established; standard counseling should acknowledge a small residual recurrence risk after an apparently de novo result, although true de novo biallelic ANXD would be unusual.

ANXD-specific prevalence, incidence, carrier frequency, sex ratio, and survival distribution are unknown. ANXD3 had only five published patients before the 2023 case, underscoring its extreme rarity. (remmelzwaal2023expandingthephenotype pages 1-2, remmelzwaal2023expandingthephenotype pages 4-4)

Broader CHH-spectrum statistics must not be misassigned to ANXD: a 2024 review/case report cited CHH-spectrum prevalence of approximately **1:23,000** in Finland with carrier frequency **1:76**, and **1–2:1,000** in Amish populations with carrier frequency about **1:10**. Those figures reflect RMRP-associated CHH enrichment, not demonstrated ANXD prevalence. (park2024cartilagehairhypoplasia–anauxeticdysplasia pages 1-2)

No consistent sex bias exists for an autosomal-recessive disorder. Reported patients occur in multiple ancestries; apparent geographic clustering may reflect founder alleles, consanguinity, ascertainment, and publication bias.

## 10. Diagnostics

### Clinical and radiographic diagnosis

Suspect ANXD in prenatal or congenital extreme short stature with severe disproportion, brachydactyly, joint laxity/dislocation, and a generalized spondylo-epi-metaphyseal radiographic pattern. A skeletal survey should assess the spine, pelvis/hips, long bones, hands/feet, and—given the 2023 ANXD3 findings—the craniovertebral junction when clinically appropriate. (remmelzwaal2023expandingthephenotype pages 1-2, remmelzwaal2023expandingthephenotype pages 3-4)

Characteristic findings include ovoid or foreshortened vertebral bodies/platyspondyly, scoliosis, hypoplastic ilia and acetabula, coxa vara, short femoral necks, small/dysplastic epiphyses, irregular widened metaphyses, shortened tubular bones, short broad metacarpals/phalanges, and premature physeal fusion. (remmelzwaal2023expandingthephenotype pages 1-2, thiel2007typeandlevel pages 3-4)

Suggested baseline assessments are:

- Height, weight, body proportions, head circumference, joint range of motion, neurologic examination, and developmental assessment.
- Skeletal survey and serial targeted radiography; dynamic cervical imaging or MRI if instability is suspected.
- Dental examination and panoramic imaging.
- CBC with differential and immune evaluation to distinguish ANXD from CHH and detect spectrum overlap.
- Gastrointestinal history for Hirschsprung disease/chronic diarrhea; respiratory history and pulmonary assessment if recurrent infection occurs.

No specific serum enzyme assay, metabolite biomarker, electrophysiologic signature, or diagnostic biopsy is established.

### Molecular testing

1. **Preferred:** skeletal-dysplasia panel including **RMRP, POP1, and NEPRO**, with sequence and copy-number analysis and adequate coverage of the noncoding RMRP transcript and proximal promoter.
2. **Phenotype-directed testing:** RMRP sequencing for classic severe CHH–AD-spectrum radiology; POP1/NEPRO if RMRP is negative or subtype clues support them.
3. **WES:** useful for POP1/NEPRO and blended phenotypes, as demonstrated by ANXD3 diagnosis; standard exome pipelines may inadequately capture/promote interpretation of noncoding RMRP variants. (remmelzwaal2023expandingthephenotype pages 4-4, park2024cartilagehairhypoplasia–anauxeticdysplasia pages 2-4)
4. **WGS:** potentially advantageous for RMRP promoter/noncoding, copy-number, and structural variants, although ANXD-specific incremental-yield studies are absent.
5. Confirm candidate variants by orthogonal testing and perform parental segregation.

CMA and karyotyping are useful when the phenotype suggests a chromosomal syndrome but are not first-line confirmatory tests for typical ANXD. FISH, mitochondrial-DNA testing, repeat-expansion testing, liquid biopsy, and routine diagnostic transcriptomics/proteomics/metabolomics are not indicated unless another diagnosis is suspected.

### Differential diagnosis

Important differentials include cartilage-hair hypoplasia and metaphyseal dysplasia without hypotrichosis; other spondyloepimetaphyseal dysplasias; Schmid metaphyseal chondrodysplasia; achondroplasia/hypochondroplasia; pseudoachondroplasia; diastrophic dysplasia; and severe prenatal skeletal dysplasias. CHH is distinguished by hypotrichosis, anemia, immune deficiency, Hirschsprung disease, and cancer susceptibility; MDWH has milder metaphyseal disease without hair or immune abnormalities. RMRP-associated ANXD has more severe vertebral, pelvic, and epiphyseal involvement. (thiel2007typeandlevel pages 1-2)

No population or newborn screening program exists. Cascade testing is appropriate after familial variants are identified.

## 11. Outcome and prognosis

No reliable five- or ten-year survival, life-expectancy, mortality, hospitalization, or quality-of-life statistics are available. Published RMRP ANXD patients can survive through childhood and likely adulthood; however, the literature is too sparse to define survival distributions.

Major morbidity is orthopedic: profound short stature, scoliosis/kyphosis, hip dysplasia or ankylosis, coxa vara, limb bowing/inequality, pain, dislocations, and restricted mobility. Atlantoaxial instability can cause cervical myelopathy and creates procedural/anesthetic risk. Dental and craniosynostosis morbidity may occur in ANXD3. (remmelzwaal2023expandingthephenotype pages 3-4, remmelzwaal2023expandingthephenotype pages 4-5)

Unlike CHH, classic ANXD is generally not associated with clinically significant immunodeficiency, anemia, gastrointestinal manifestations, or established malignancy predisposition. Nevertheless, because molecular and phenotypic boundaries overlap, baseline CBC/immune assessment is prudent rather than assuming their absence. (remmelzwaal2023expandingthephenotype pages 1-2, thiel2007typeandlevel pages 5-6)

Prognosis is likely influenced by genotype/functional severity, spinal and cervical instability, hip disease, pain and mobility, access to orthopedic care, and any spectrum-overlap features. No validated prognostic biomarker or calculator exists.

## 12. Treatment

There is no curative or disease-modifying ANXD therapy and no evidence-based pharmacologic algorithm. Growth hormone has not been shown to correct the primary growth-plate ribosome-biogenesis defect; broader CHH-spectrum cases have normal stimulated GH responses, and treatment was not attempted in the 2024 Korean report. (park2024cartilagehairhypoplasia–anauxeticdysplasia pages 2-4)

### Current management

- **Orthopedic/spine care:** surveillance for scoliosis, kyphosis, hip dysplasia, coxa vara, limb deformity, contractures, dislocation, and pain; individualized bracing or corrective surgery.
- **Cervical care:** evaluate suspected atlantoaxial instability; consider immobilization or surgical fixation according to neurosurgical/orthopedic assessment; use cervical and airway precautions during anesthesia. (remmelzwaal2023expandingthephenotype pages 3-4)
- **Rehabilitation:** physical and occupational therapy, mobility aids, adaptive equipment, environmental modification, and low-impact activity adapted to joint/spine status.
- **Dental/craniofacial care:** preventive dentistry, orthodontic/prosthodontic planning, and craniofacial/neurosurgical assessment for craniosynostosis.
- **Symptomatic care:** pain management and monitoring for neurologic compromise.
- **Spectrum surveillance:** CBC, immune function, infection history, pulmonary status, and gastrointestinal symptoms when indicated.

Suggested NCIT intervention concepts include **Physical Therapy**, **Occupational Therapy**, **Orthopedic Surgery**, **Spinal Fusion**, **Dental Care**, **Genetic Counseling**, **Pain Management**, and **Surveillance**; exact NCIT codes should be validated against the current release.

No gene replacement, CRISPR therapy, cell therapy, ASO/siRNA therapy, targeted small molecule, or immunotherapy is clinically available. Modulating BMP/WNT/TGF-β based solely on promoter-reporter findings would be premature and potentially unsafe. (steinbusch2017expressionofrmrp pages 7-9)

The retrieved ClinicalTrials.gov record **NCT00001754**, “Clinical and Molecular Manifestations of Human Skeletal Dysplasias and Short Stature,” was a completed NIH observational study enrolling 600 participants across many skeletal disorders, including cartilage-hair hypoplasia. It evaluated phenotype, natural history, and genotype–phenotype relationships; it was not an ANXD treatment trial. URL: https://clinicaltrials.gov/study/NCT00001754. (NCT00001754 chunk 1)

## 13. Prevention

Primary prevention by lifestyle change, vaccination, or environmental control is not possible. Relevant prevention is reproductive and complication-directed:

- Genetic counseling and familial-variant confirmation.
- Carrier testing for adult relatives.
- Prenatal diagnosis by chorionic-villus sampling or amniocentesis once familial variants are known.
- Preimplantation genetic testing for monogenic disease where available.
- Early prenatal ultrasound can detect limb shortening but is not molecularly specific.
- Cascade testing in at-risk relatives.
- Tertiary prevention through early orthopedic, cervical, dental, respiratory, and rehabilitation surveillance.

No vaccine, prophylactic medication, or population screening program prevents ANXD. Standard immunizations remain appropriate unless an individual has immune dysfunction requiring specialist guidance.

## 14. Other species and natural disease

No naturally occurring veterinary disorder clearly equivalent to human ANXD was established in the retrieved evidence. There is no zoonotic potential or cross-species transmission because ANXD is inherited, not infectious.

Orthologues of **RMRP, POP1, and NEPRO** are evolutionarily conserved. RMRP sequences were compared across human, mouse, rat, rabbit, dog, armadillo, elephant, opossum, and frog; disease-associated nucleotides frequently mapped to conserved structural regions. (thiel2007typeandlevel pages 4-5, thiel2007typeandlevel pages 1-2)

Suggested taxa for comparative work include **Homo sapiens** (NCBI Taxon 9606), **Mus musculus** (10090), **Rattus norvegicus** (10116), and **Xenopus tropicalis** (8364). Species-specific NCBI Gene IDs and any OMIA/VBO entries should be verified directly before database loading.

## 15. Model organisms and experimental systems

### Cellular and mouse-derived models

- **ATDC5 mouse chondrogenic cells:** Rmrp RNAi causes accumulation of RNase-MRP substrates and ITS1 pre-rRNA intermediates, reduction of 18S/5.8S rRNA, and impaired chondrocyte differentiation—especially hypertrophy. This recapitulates a plausible cellular mechanism but not the full multisite human skeletal phenotype. (steinbusch2017expressionofrmrp pages 7-9)
- **MCT chondrocytes:** temperature-induced hypertrophy increases Rmrp expression; PTHrP suppresses both hypertrophy and Rmrp expression. (steinbusch2017expressionofrmrp pages 7-9)
- **Murine growth plate:** Rmrp and RNase-MRP proteins are expressed during growth-plate differentiation, supporting biological relevance. (steinbusch2017expressionofrmrp pages 1-2)
- **Human fibroblast assays:** transient expression of mutant RMRP constructs quantified ITS1/5.8S rRNA and cyclin-B2 mRNA cleavage; functional impairment correlated with clinical severity. These are strong genotype-function assays but do not recreate three-dimensional growth-plate architecture. (thiel2007typeandlevel pages 1-2, thiel2007typeandlevel pages 6-8)
- **Patient fibroblast chondrogenic transdifferentiation:** broader CHH evidence showed impaired hypertrophic differentiation and supports the same disease spectrum mechanism. (steinbusch2017expressionofrmrp pages 1-2)

No validated ANXD-specific knock-in mouse, zebrafish model, patient-derived iPSC growth-plate organoid, or in-vivo therapeutic-rescue model was demonstrated in the retrieved evidence. These constitute important research gaps. Priority applications include defining NEPRO function, resolving subtype-specific mechanisms, testing whether restoration of RNase-MRP activity rescues chondrocyte maturation, and developing preclinical cervical/spinal and growth-plate outcome measures.

## Recent developments and expert interpretation

The most consequential recent direct ANXD development was the 2023 expansion of ANXD3 to include atlantoaxial subluxation, extensive dental anomalies, and sagittal craniosynostosis. Its practical implication is that ANXD3 evaluation should extend beyond stature and limb radiographs to the craniovertebral junction, dentition, and cranial sutures. (remmelzwaal2023expandingthephenotype pages 1-2, remmelzwaal2023expandingthephenotype pages 3-4)

The 2023 skeletal-disorder nosology adopted gene–phenotype dyadic naming across 771 entities and 552 genes, an approach especially useful for ANXD because numbered subtypes can obscure distinct causal genes and overlapping phenotypes. URL: https://doi.org/10.1002/ajmg.a.63132; published February 2023. The preferred knowledge-base labels are therefore **RMRP-related anauxetic dysplasia**, **POP1-related anauxetic dysplasia**, and **NEPRO-related anauxetic dysplasia**.

The 2024 Korean report reinforces that extremely short stature from birth should prompt CHH–AD-spectrum testing even without hair or immune abnormalities and that WES plus RMRP-aware analysis can resolve atypical cases. Its cases were MDWH/CHH rather than pure ANXD, so their immune and anemia frequencies must not be generalized to ANXD. URL: https://doi.org/10.1097/MD.0000000000037247; received November 13, 2023, accepted January 23, 2024, published May 2024. (park2024cartilagehairhypoplasia–anauxeticdysplasia pages 2-4, park2024cartilagehairhypoplasia–anauxeticdysplasia pages 1-2)

## Principal evidence and exact abstract quotations

1. **Remmelzwaal et al., 2023, AJMG Part A.** DOI: https://doi.org/10.1002/ajmg.a.63316. Abstract: “The cartilage hair hypoplasia and anauxetic dysplasia (CHH-AD) spectrum encompasses a group of rare skeletal disorders, with anauxetic dysplasia (ANXD) at the most severe end of the spectrum.” It also states, “Thus far, only five patients with type 3 anauxetic dysplasia (ANXD3) have been reported.” This is direct human, single-case evidence. (remmelzwaal2023expandingthephenotype pages 1-2)
2. **Thiel et al., 2007, American Journal of Human Genetics.** DOI: https://doi.org/10.1086/521034. Abstract: “In vitro testing…revealed a strong correlation between the decrease in rRNA cleavage in ribosomal assembly and the degree of bone dysplasia.” Direct human genotype–phenotype data plus in-vitro functional assays. (thiel2007typeandlevel pages 1-2)
3. **Barraza-García et al., 2017, Clinical Genetics.** DOI: https://doi.org/10.1111/cge.12964. Human POP1 cases plus molecular assays; reduced RMRP abundance and increased pre-5.8S rRNA supported RNase-MRP dysfunction. (barrazagarcia2017broadeningthephenotypic pages 1-2)
4. **Steinbusch et al., 2017, Scientific Reports.** DOI: https://doi.org/10.1038/s41598-017-06809-5. Abstract: “Genetic interference with Rmrp RNA expression in ATDC5 cultures caused a deregulation of chondrogenic differentiation, with a prominent impact on hypertrophy and changes in pre-rRNA processing and rRNA levels.” This is preclinical cellular/mouse-derived evidence, not a clinical treatment study. (steinbusch2017expressionofrmrp pages 1-2)

## Evidence limitations

ANXD evidence is dominated by individual cases, a few families, and mechanistic studies spanning the broader CHH–AD spectrum. Consequently, phenotype percentages, penetrance, prevalence, life expectancy, treatment-response rates, and genotype-specific prognosis cannot currently be estimated reliably. Recent 2023–2024 reports improve phenotypic recognition but do not provide population-level natural history or therapeutic evidence. Assertions imported from cartilage-hair hypoplasia—especially immunodeficiency, anemia, Hirschsprung disease, and malignancy risk—must be explicitly labeled as spectrum-level evidence rather than assumed characteristics of pure ANXD.

References

1. (remmelzwaal2023expandingthephenotype pages 1-2): P. Christian Remmelzwaal, Martijn V. Verhagen, Jan D. H. Jongbloed, Peter C. van den Akker, Hermine E. Veenstra‐Knol, and Marrit M. Hitzert. Expanding the phenotype of anauxetic dysplasia caused by biallelic nepro mutations: a case report. American Journal of Medical Genetics Part A, 191:2440-2445, Jun 2023. URL: https://doi.org/10.1002/ajmg.a.63316, doi:10.1002/ajmg.a.63316. This article has 5 citations.

2. (thiel2007typeandlevel pages 1-2): Christian T. Thiel, Geert Mortier, Ilkka Kaitila, André Reis, and Anita Rauch. Type and level of rmrp functional impairment predicts phenotype in the cartilage hair hypoplasia-anauxetic dysplasia spectrum. American journal of human genetics, 81 3:519-29, Sep 2007. URL: https://doi.org/10.1086/521034, doi:10.1086/521034. This article has 114 citations and is from a highest quality peer-reviewed journal.

3. (thiel2007typeandlevel pages 5-6): Christian T. Thiel, Geert Mortier, Ilkka Kaitila, André Reis, and Anita Rauch. Type and level of rmrp functional impairment predicts phenotype in the cartilage hair hypoplasia-anauxetic dysplasia spectrum. American journal of human genetics, 81 3:519-29, Sep 2007. URL: https://doi.org/10.1086/521034, doi:10.1086/521034. This article has 114 citations and is from a highest quality peer-reviewed journal.

4. (thiel2007typeandlevel pages 3-4): Christian T. Thiel, Geert Mortier, Ilkka Kaitila, André Reis, and Anita Rauch. Type and level of rmrp functional impairment predicts phenotype in the cartilage hair hypoplasia-anauxetic dysplasia spectrum. American journal of human genetics, 81 3:519-29, Sep 2007. URL: https://doi.org/10.1086/521034, doi:10.1086/521034. This article has 114 citations and is from a highest quality peer-reviewed journal.

5. (thiel2007typeandlevel pages 6-8): Christian T. Thiel, Geert Mortier, Ilkka Kaitila, André Reis, and Anita Rauch. Type and level of rmrp functional impairment predicts phenotype in the cartilage hair hypoplasia-anauxetic dysplasia spectrum. American journal of human genetics, 81 3:519-29, Sep 2007. URL: https://doi.org/10.1086/521034, doi:10.1086/521034. This article has 114 citations and is from a highest quality peer-reviewed journal.

6. (barrazagarcia2017broadeningthephenotypic pages 1-2): J. Barraza-García, J. Barraza-García, J. Barraza-García, C. I. Rivera-Pedroza, C. I. Rivera-Pedroza, A. Hisado-Oliva, A. Hisado-Oliva, A. Hisado-Oliva, A. Belinchón-Martínez, A. Belinchón-Martínez, A. Belinchón-Martínez, L. Sentchordi-Montané, L. Sentchordi-Montané, Emma L Duncan, G. R. Clark, A. D. Pozo, A. D. Pozo, K. Ibáñez-Garikano, A. Offiah, P. Prieto-Matos, V. Cormier-Daire, K. E. Heath, K. E. Heath, and K. E. Heath. Broadening the phenotypic spectrum of pop1‐skeletal dysplasias: identification of pop1 mutations in a mild and severe skeletal dysplasia. Clinical Genetics, 92:91-98, Feb 2017. URL: https://doi.org/10.1111/cge.12964, doi:10.1111/cge.12964. This article has 24 citations and is from a peer-reviewed journal.

7. (remmelzwaal2023expandingthephenotype pages 4-4): P. Christian Remmelzwaal, Martijn V. Verhagen, Jan D. H. Jongbloed, Peter C. van den Akker, Hermine E. Veenstra‐Knol, and Marrit M. Hitzert. Expanding the phenotype of anauxetic dysplasia caused by biallelic nepro mutations: a case report. American Journal of Medical Genetics Part A, 191:2440-2445, Jun 2023. URL: https://doi.org/10.1002/ajmg.a.63316, doi:10.1002/ajmg.a.63316. This article has 5 citations.

8. (remmelzwaal2023expandingthephenotype pages 3-4): P. Christian Remmelzwaal, Martijn V. Verhagen, Jan D. H. Jongbloed, Peter C. van den Akker, Hermine E. Veenstra‐Knol, and Marrit M. Hitzert. Expanding the phenotype of anauxetic dysplasia caused by biallelic nepro mutations: a case report. American Journal of Medical Genetics Part A, 191:2440-2445, Jun 2023. URL: https://doi.org/10.1002/ajmg.a.63316, doi:10.1002/ajmg.a.63316. This article has 5 citations.

9. (thiel2007typeandlevel pages 2-3): Christian T. Thiel, Geert Mortier, Ilkka Kaitila, André Reis, and Anita Rauch. Type and level of rmrp functional impairment predicts phenotype in the cartilage hair hypoplasia-anauxetic dysplasia spectrum. American journal of human genetics, 81 3:519-29, Sep 2007. URL: https://doi.org/10.1086/521034, doi:10.1086/521034. This article has 114 citations and is from a highest quality peer-reviewed journal.

10. (steinbusch2017expressionofrmrp pages 1-2): Mandy M. F. Steinbusch, Marjolein M. J. Caron, Don A. M. Surtel, Franziska Friedrich, Ekkehart Lausch, Ger J. M. Pruijn, Wouter Verhesen, Blanche L. M. Schroen, Lodewijk W. van Rhijn, Bernhard Zabel, and Tim J. M. Welting. Expression of rmrp rna is regulated in chondrocyte hypertrophy and determines chondrogenic differentiation. Scientific Reports, Jul 2017. URL: https://doi.org/10.1038/s41598-017-06809-5, doi:10.1038/s41598-017-06809-5. This article has 56 citations and is from a peer-reviewed journal.

11. (park2024cartilagehairhypoplasia–anauxeticdysplasia pages 2-4): Ju Heon Park, Minji Im, Yae-Jean Kim, Ja-Hyun Jang, Sae-Mi Lee, Min-Sun Kim, and Sung Yoon Cho. Cartilage-hair hypoplasia–anauxetic dysplasia spectrum disorders harboring rmrp mutations in two korean children: a case report. Medicine, 103:e37247, May 2024. URL: https://doi.org/10.1097/md.0000000000037247, doi:10.1097/md.0000000000037247. This article has 4 citations and is from a peer-reviewed journal.

12. (steinbusch2017expressionofrmrp pages 7-9): Mandy M. F. Steinbusch, Marjolein M. J. Caron, Don A. M. Surtel, Franziska Friedrich, Ekkehart Lausch, Ger J. M. Pruijn, Wouter Verhesen, Blanche L. M. Schroen, Lodewijk W. van Rhijn, Bernhard Zabel, and Tim J. M. Welting. Expression of rmrp rna is regulated in chondrocyte hypertrophy and determines chondrogenic differentiation. Scientific Reports, Jul 2017. URL: https://doi.org/10.1038/s41598-017-06809-5, doi:10.1038/s41598-017-06809-5. This article has 56 citations and is from a peer-reviewed journal.

13. (park2024cartilagehairhypoplasia–anauxeticdysplasia pages 1-2): Ju Heon Park, Minji Im, Yae-Jean Kim, Ja-Hyun Jang, Sae-Mi Lee, Min-Sun Kim, and Sung Yoon Cho. Cartilage-hair hypoplasia–anauxetic dysplasia spectrum disorders harboring rmrp mutations in two korean children: a case report. Medicine, 103:e37247, May 2024. URL: https://doi.org/10.1097/md.0000000000037247, doi:10.1097/md.0000000000037247. This article has 4 citations and is from a peer-reviewed journal.

14. (remmelzwaal2023expandingthephenotype pages 4-5): P. Christian Remmelzwaal, Martijn V. Verhagen, Jan D. H. Jongbloed, Peter C. van den Akker, Hermine E. Veenstra‐Knol, and Marrit M. Hitzert. Expanding the phenotype of anauxetic dysplasia caused by biallelic nepro mutations: a case report. American Journal of Medical Genetics Part A, 191:2440-2445, Jun 2023. URL: https://doi.org/10.1002/ajmg.a.63316, doi:10.1002/ajmg.a.63316. This article has 5 citations.

15. (NCT00001754 chunk 1):  Study of Skeletal Disorders and Short Stature. National Human Genome Research Institute (NHGRI). 1998. ClinicalTrials.gov Identifier: NCT00001754

16. (thiel2007typeandlevel pages 4-5): Christian T. Thiel, Geert Mortier, Ilkka Kaitila, André Reis, and Anita Rauch. Type and level of rmrp functional impairment predicts phenotype in the cartilage hair hypoplasia-anauxetic dysplasia spectrum. American journal of human genetics, 81 3:519-29, Sep 2007. URL: https://doi.org/10.1086/521034, doi:10.1086/521034. This article has 114 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Anauxetic_Dysplasia-deep-research-falcon_artifacts/artifact-00.md)