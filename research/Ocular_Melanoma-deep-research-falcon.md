---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-01T04:59:03.929630'
end_time: '2026-08-01T05:10:32.159540'
duration_seconds: 688.23
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Ocular Melanoma
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 27
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Ocular_Melanoma-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Ocular Melanoma
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Ocular Melanoma** covering all of the
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
- **Disease Name:** Ocular Melanoma
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Ocular Melanoma** covering all of the
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


# Ocular Melanoma: Comprehensive Disease-Characteristics Report

**Scope and category.** “Ocular melanoma” is an umbrella term, not one homogeneous disease. It principally includes **uveal melanoma (UM)**—melanoma of the choroid, ciliary body, or iris—and **conjunctival melanoma (Co-M)**, an ocular-surface mucosal melanoma with different embryology, drivers, metastatic routes, and treatment. This report therefore treats them separately, emphasizing UM because it accounts for approximately 80% of ocular melanomas and has the larger evidence base. The evidence is aggregated disease-level literature and registry/trial data, not individual electronic-health-record data. (butt2024conjunctivalmelanomaa pages 1-2, pasalic2023geneticandepigenetic pages 1-2)

## Executive summary

UM is the commonest primary intraocular malignancy in adults, with incidence around 5–6 per million/year in the United States and Europe and marked enrichment in fair-skinned populations. Approximately 90% arise in the choroid. GNAQ/GNA11-pathway activation initiates most tumors; later BAP1, SF3B1, or EIF1AX alterations and chromosome 3/8q status largely determine metastatic risk. Local radiotherapy or surgery controls the ocular tumor, but roughly half of patients eventually develop hematogenous metastases, usually in the liver. Tebentafusp is the first systemic therapy to produce a randomized overall-survival benefit, but it applies only to HLA-A*02:01-positive unresectable/metastatic UM. Co-M is much rarer—approximately 0.46 cases per million/year—but its incidence is increasing; it often arises from conjunctival melanocytic intraepithelial lesions and has BRAF, NRAS, NF1, UV-related, and PD-L1 biology closer to cutaneous melanoma. (kastelan2024biologicalcharacteristicsand pages 2-3, fuentesrodriguez2024recentadvancesin pages 2-3, butt2024conjunctivalmelanomaa pages 1-2, hassel2023threeyearoverallsurvival pages 1-3)

## 1. Disease information

### Definition and identifiers

* **Uveal melanoma:** malignant melanocytic neoplasm arising in the **choroid, ciliary body, or iris**. Confirmed identifier: **MONDO:0006486**. Open Targets identifies BAP1, MBD4, GNA11, GNAQ, and SF3B1 among its strongest disease-associated targets. (OpenTargets Search: uveal melanoma,ocular melanoma,conjunctival melanoma, lissak2024whatsetsuveal pages 1-3)
* **Conjunctival melanoma:** invasive melanoma arising from basal melanocytes of conjunctival epithelium. It is a mucosal/ocular-surface melanoma, not a subtype of UM. (butt2024conjunctivalmelanomaa pages 1-2)
* **Synonyms:** ocular melanoma, eye melanoma, intraocular melanoma, uveal malignant melanoma, choroidal melanoma, ciliary-body melanoma, iris melanoma, and conjunctival melanoma. “Ocular melanoma” should remain a parent term in a knowledge base.
* **Coding:** ICD-10-CM generally uses the site-specific malignant-neoplasm-of-eye family **C69.x**; ICD-O morphology is melanoma-specific and topography depends on choroid, ciliary body, iris, or conjunctiva. Exact ICD-10/ICD-11, MeSH, OMIM, and Orphanet cross-references should be curator-verified because no single code covers all ocular melanoma subtypes. UM is usually sporadic and therefore does not have one Mendelian OMIM disease entry equivalent to BAP1 tumor-predisposition syndrome.

A concise structured mapping is provided below.

| Domain | Uveal melanoma key entity/fact | Conjunctival melanoma contrast | Suggested ontology term(s) |
|---|---|---|---|
| Disease entity | Uveal melanoma is the main intraocular melanoma in adults; MONDO confirmed as **MONDO:0006486**. Often treated as the dominant subtype within “ocular melanoma,” but biologically distinct from conjunctival melanoma (OpenTargets Search: uveal melanoma,ocular melanoma,conjunctival melanoma, lissak2024whatsetsuveal pages 1-3) | Conjunctival melanoma is an ocular-surface/mucosal melanoma, not a uveal tumor; review evidence emphasizes it is embryologically, biologically, and clinically distinct from UM (butt2024conjunctivalmelanomaa pages 1-2) | **MONDO:0006486** uveal melanoma; conjunctival melanoma: **suggest MONDO mapping needed** (do not infer exact ID) |
| Synonym/scope | “Uveal melanoma (UM)”; arises from melanocytes in iris, ciliary body, or choroid (lissak2024whatsetsuveal pages 1-3, kulbay2024uvealmelanomacomprehensive pages 2-5) | “Conjunctival melanoma (Co-M)”; ocular surface melanoma, often grouped historically with ocular melanoma but should be separated in KB design (butt2024conjunctivalmelanomaa pages 1-2) | MeSH/ICD/Orphanet exact cross-maps: **suggest curator lookup** |
| Anatomy | Most UM arises from choroid (~90%), then ciliary body (~7%), iris (~2–3%) (kulbay2024uvealmelanomacomprehensive pages 2-5, pasalic2023geneticandepigenetic pages 1-2) | Usually bulbar conjunctiva near limbus, but can involve any conjunctival region and adjacent tissues (butt2024conjunctivalmelanomaa pages 1-2) | **UBERON:** uvea; choroid; ciliary body; iris; conjunctiva; bulbar conjunctiva; limbus (**exact IDs should be curated if required**) |
| Epidemiology | Incidence ~5–6 per million/year in US/Europe; much higher in fair-skinned/Caucasian populations (pasalic2023geneticandepigenetic pages 1-2, lissak2024whatsetsuveal pages 3-7) | Incidence ~0.46 per 1,000,000 persons/year; increasing, especially in older adults (butt2024conjunctivalmelanomaa pages 1-2) | MONDO:0006486; phenotype annotation may use “adult onset” HPO term |
| Cell of origin | Malignancy of **uveal melanocytes**; early oncogenic events arise in melanocytes of choroid/ciliary body/iris (lissak2024whatsetsuveal pages 1-3, kulbay2024uvealmelanomacomprehensive pages 2-5) | Malignancy of **conjunctival epithelial/basal melanocytes**; often from C-MIN/PAM with atypia (butt2024conjunctivalmelanomaa pages 1-2) | **CL:** melanocyte; conjunctival epithelial cell; immune infiltrates incl. macrophage, T cell (**exact CL IDs to curate**) |
| Initiating gene driver | **GNA11** activating mutation, ~55% in one 2024 summary; mutually exclusive with GNAQ; early/initiating driver (kastelan2024biologicalcharacteristicsand pages 2-3, fuentesrodriguez2024recentadvancesin pages 2-3) | GNA11 is not a canonical frequent Co-M driver in recent reviews (butt2024conjunctivalmelanomaa pages 1-2) | HGNC:GNA11; **GO suggestions:** G protein-coupled receptor signaling pathway; MAPK cascade |
| Initiating gene driver | **GNAQ** activating mutation, ~40% in one 2024 summary; with GNA11 accounts for ~85–94% of UM across stages; early driver, not strongly prognostic by itself (kastelan2024biologicalcharacteristicsand pages 2-3, fuentesrodriguez2024recentadvancesin pages 2-3) | Not a typical major Co-M driver in current review summaries (butt2024conjunctivalmelanomaa pages 1-2) | HGNC:GNAQ; **GO:** MAPK cascade; phospholipase C-activating GPCR signaling pathway |
| Initiating gene driver | **CYSLTR2** mutation in ~2–4% of UM, usually in GNAQ/GNA11-wild-type tumors; initiating event (fuentesrodriguez2024recentadvancesin pages 2-3) | Not emphasized as a common Co-M driver in recent clinical reviews (butt2024conjunctivalmelanomaa pages 1-2) | HGNC:CYSLTR2; **GO:** leukotriene signaling / GPCR signaling (**exact process term to curate**) |
| Initiating gene driver | **PLCB4** mutation ~2.5% of UM; activating PLC/PKC/MAPK signaling (fuentesrodriguez2024recentadvancesin pages 2-3) | Not a defining frequent Co-M driver in 2024 review evidence (butt2024conjunctivalmelanomaa pages 1-2) | HGNC:PLCB4; **GO:** phosphatidylinositol-mediated signaling; protein kinase C signaling |
| Prognostic gene | **BAP1** loss/inactivating mutation: associated with aggressive disease, monosomy 3, high metastatic risk; ~38% primary and ~84% metastatic in one 2024 review summary (kastelan2024biologicalcharacteristicsand pages 2-3, lissak2024whatsetsuveal pages 3-7) | BAP1 is not the hallmark frequent Co-M driver pattern emphasized in current review summaries (butt2024conjunctivalmelanomaa pages 1-2) | HGNC:BAP1; **GO:** DNA repair; chromatin organization; deubiquitination |
| Prognostic gene | **SF3B1** mutation ~25%; intermediate/later metastasis risk and distinct molecular subgroup (lissak2024whatsetsuveal pages 3-7, fuentesrodriguez2024recentadvancesin pages 2-3) | Not a headline common Co-M mutation in recent clinical review summaries (butt2024conjunctivalmelanomaa pages 1-2) | HGNC:SF3B1; **GO:** mRNA splicing via spliceosome |
| Prognostic gene | **EIF1AX** mutation ~13%; associated with favorable prognosis and younger patients (kastelan2024biologicalcharacteristicsand pages 2-3, lissak2024whatsetsuveal pages 3-7) | Not a major defining Co-M driver in recent clinical review summaries (butt2024conjunctivalmelanomaa pages 1-2) | HGNC:EIF1AX; **GO:** translation initiation |
| Chromosomal alteration | **Monosomy 3** strongly linked to poor prognosis/BAP1-mutant disease (lissak2024whatsetsuveal pages 3-7, fuentesrodriguez2024recentadvancesin pages 2-3, pasalic2023geneticandepigenetic pages 1-2) | Copy-number variation occurs in Co-M, but chromosome-3-centric prognostic framework is mainly UM-focused (butt2024conjunctivalmelanomaa pages 1-2) | Cytogenetic annotation: monosomy 3 (**formal ontology/NCIt code should be curated**) |
| Chromosomal alteration | **8q gain/amplification** linked to metastatic risk; often with monosomy 3 in poor-risk classes (fuentesrodriguez2024recentadvancesin pages 2-3, pasalic2023geneticandepigenetic pages 1-2) | CNVs also occur in Co-M, but specific UM class system is not directly transferable (butt2024conjunctivalmelanomaa pages 1-2) | Cytogenetic annotation: 8q gain (**exact code to curate**) |
| Chromosomal alteration | **6p gain** seen in better-risk UM classes; 6q loss may accompany SF3B1-related structural patterns (lissak2024whatsetsuveal pages 3-7, fuentesrodriguez2024recentadvancesin pages 2-3) | No analogous standard clinical class scheme highlighted for Co-M (butt2024conjunctivalmelanomaa pages 1-2) | Cytogenetic annotation: 6p gain / 6q loss (**exact code to curate**) |
| Molecular class | DecisionDx-UM/GEP classes used for prognostic stratification: class 1A, 1B, 2 with increasing 5-year metastatic risk; transcriptomic classes 1–4/A–D also used (fuentesrodriguez2024recentadvancesin pages 2-3) | No comparably established routine prognostic GEP system highlighted in the 2024 Co-M review (butt2024conjunctivalmelanomaa pages 1-2) | **NCIT/diagnostic concept:** gene expression profiling (**exact NCIt term to curate**) |
| Core pathway | Gαq/Gα11 signaling activates **PKC**, **MAPK/ERK**, **PI3K/mTOR** networks driving proliferation and survival (kulbay2024uvealmelanomacomprehensive pages 2-5, fuentesrodriguez2024recentadvancesin pages 2-3) | Co-M more often resembles cutaneous melanoma genetics, especially UV-related **BRAF/NRAS/NF1** alterations (butt2024conjunctivalmelanomaa pages 1-2) | **GO:** MAPK cascade; PI3K signaling; TOR signaling; cell proliferation |
| Immune microenvironment | UM is immune-privileged/immune-cold; lymphocytic inflammatory phenotype, macrophages, HLA class I/II upregulation and NF-κB activity correlate with poor prognosis (lissak2024whatsetsuveal pages 1-3, kulbay2024uvealmelanomacomprehensive pages 2-5) | Co-M transcriptomic studies show **high PD-L1 expression** and immune-enriched subtypes (butt2024conjunctivalmelanomaa pages 1-2) | **CL:** T cell, CD8-positive T cell, macrophage, endothelial cell; **GO:** immune response, antigen processing/presentation, NF-kappaB signaling |
| Multi-omics/single-cell | scRNA-seq of **37,660 malignant cells from 17 UM tumors** revealed heterogeneous malignant programs and 2 intratumoral subtypes with prognostic/immune differences (karlsson2024patientderivedxenograftsand pages 1-2) | Equivalent single-cell evidence base for Co-M is less mature in the retrieved set (butt2024conjunctivalmelanomaa pages 1-2) | **NCIT/assay:** single-cell RNA sequencing (**exact term to curate**) |
| Metastatic tropism | About half of UM patients ultimately metastasize; liver is dominant metastatic site (~89% or more than 90% across sources) (pasalic2023geneticandepigenetic pages 1-2, hassel2023threeyearoverallsurvival pages 1-3) | Co-M more often spreads first to regional lymph nodes (~25%), but can also involve liver, lungs, brain (butt2024conjunctivalmelanomaa pages 1-2) | **HPO suggestions:** Hepatic metastasis; Lymph node metastasis; Pulmonary metastasis; Brain metastasis (**exact IDs to curate**) |
| Clinical phenotype | Up to ~30% asymptomatic; symptomatic disease can cause visual impairment/vision loss, exudation, retinal detachment; iris melanoma may present with heterochromia and corectopia (kastelan2024biologicalcharacteristicsand pages 1-2, kastelan2024biologicalcharacteristicsand pages 2-3) | Visible pigmented or amelanotic conjunctival lesion; may cause sight loss, eye loss, local invasion, disfigurement (butt2024conjunctivalmelanomaa pages 1-2) | **HPO suggestions:** decreased visual acuity; retinal detachment; heterochromia iridis; corectopia; conjunctival pigmentation; amelanotic melanoma (**exact IDs to curate**) |
| Histopathology/prognostic phenotype | Epithelioid or mixed cell type, extra-scleral extension, larger tumor size and chromosome 3/8q abnormalities increase metastatic risk (pasalic2023geneticandepigenetic pages 1-2) | High postoperative recurrence (33–45%) and lack of standardized therapy are emphasized (butt2024conjunctivalmelanomaa pages 1-2) | **HPO suggestions:** extrascleral extension; recurrent neoplasm; epithelioid morphology (**exact mappings to curate**) |
| Diagnostics | Ophthalmic exam plus ocular imaging and tissue/molecular prognostication; liquid biopsy, ctDNA, extracellular vesicles and AI-assisted methods are active research areas (kulbay2024uvealmelanomacomprehensive pages 2-5, pasalic2023geneticandepigenetic pages 1-2) | Histopathology is critical; clinical misdiagnosis/late diagnosis remains common; molecular pathology increasingly relevant (butt2024conjunctivalmelanomaa pages 1-2) | **NCIT/assay suggestions:** ultrasonography; fundus photography; biopsy; gene expression profiling; liquid biopsy |
| Prognosis | Historical metastatic median OS about 1 year; 5-year survival overall often 50–70%; metastatic prognosis poor (pasalic2023geneticandepigenetic pages 1-2, hassel2023threeyearoverallsurvival pages 1-3) | ~27% 5-year disease-specific mortality and recurrence 33–45% in review summary (butt2024conjunctivalmelanomaa pages 1-2) | **HPO suggestions:** reduced life expectancy; recurrent neoplasm; metastasis |
| Local treatment | Plaque brachytherapy and enucleation remain standard local therapies; globe-preserving radiotherapy common (kastelan2024biologicalcharacteristicsand pages 2-3, pasalic2023geneticandepigenetic pages 1-2) | Surgical excision ± cryotherapy, topical chemotherapy, brachytherapy, proton/photon radiotherapy; exenteration for advanced invasion (butt2024conjunctivalmelanomaa pages 1-2) | **NCIT suggestions:** Plaque Brachytherapy; Enucleation; Cryosurgery; Topical Chemotherapy; Proton Radiation Therapy; Orbital Exenteration |
| Systemic/metastatic treatment | **Tebentafusp** for HLA-A*02:01-positive unresectable/metastatic UM improved OS: median 21.6 vs 16.9 months; 3-year OS 27% vs 18% (phase 3) (hassel2023threeyearoverallsurvival pages 1-3) | No standard targeted/immunotherapy established; anti-BRAF/anti-MEK/anti-PD(L)1 evidence remains limited and often case-series level (butt2024conjunctivalmelanomaa pages 1-2) | **NCIT suggestions:** Tebentafusp; Pembrolizumab; Ipilimumab; Dacarbazine |
| Tebentafusp toxicity | Common AEs: rash 83%, pyrexia 76%, pruritus 70%, hypotension 38%; discontinuation low (2%) in phase 3 follow-up (hassel2023threeyearoverallsurvival pages 1-3) | Not directly applicable; Co-M systemic therapy toxicities depend on regimen used | **HPO/AE suggestions:** rash; pyrexia; pruritus; hypotension; cytokine release syndrome (**exact IDs to curate**) |
| Liver-directed treatment | Liver-directed therapy remains central for metastatic UM because liver is the dominant metastatic site (pasalic2023geneticandepigenetic pages 1-2, hassel2023threeyearoverallsurvival pages 1-3) | Co-M metastasis pattern is less liver-dominant than UM and more nodal at presentation of spread (butt2024conjunctivalmelanomaa pages 1-2) | **NCIT suggestions:** Hepatic Perfusion; Radiofrequency Ablation; Embolization; Hepatic-directed Therapy (**exact preferred term to curate**) |
| Current trial example | **Darovasertib (IDE196/LXS196)** neoadjuvant/adjuvant phase 2 for localized UM; PKC inhibitor; outcomes include eye salvage, dose reduction to critical structures, recurrence and metastasis follow-up (NCT05907954) (NCT05907954 chunk 1) | No matched conjunctival trial in retrieved evidence | **NCIT suggestions:** Darovasertib; Protein Kinase C Inhibitor Therapy |
| Current trial example | **Belzupacap sarotalocan (AU-011 / bel-sar)** phase 3 randomized sham-controlled trial for indeterminate lesions/small choroidal melanoma using suprachoroidal administration plus laser photoactivation (NCT06007690) (NCT06007690 chunk 1) | Not a conjunctival melanoma protocol | **NCIT suggestions:** Belzupacap sarotalocan; Suprachoroidal Injection; Laser Therapy |
| Current trial example | **Adjuvant melatonin** phase 3 prevention-oriented trial in high-risk primary UM with 5-year metastasis endpoint (NCT05502900) (NCT05502900 chunk 1) | No analogous Co-M adjuvant prevention trial in retrieved set | **NCIT suggestions:** Melatonin; Adjuvant Therapy |
| Model systems | PDX, zebrafish xenografts, and single-cell functional studies are active UM platforms; zebrafish UM PDX reproduced disseminating UM and enabled drug testing with navitoclax/everolimus (yin2023zebrafishpatientderivedxenograft pages 1-2, karlsson2024patientderivedxenograftsand pages 1-2) | No equally developed Co-M preclinical evidence highlighted in retrieved set | **NCIT/model suggestions:** Patient-Derived Xenograft Model; Zebrafish Model; Single-Cell Sequencing |
| Evidence note | UM ontology, molecular classes, and treatment evidence are substantially more mature than for Co-M in the retrieved 2023–2024 literature (fuentesrodriguez2024recentadvancesin pages 2-3, butt2024conjunctivalmelanomaa pages 1-2, hassel2023threeyearoverallsurvival pages 1-3) | Co-M should be represented as a distinct KB entity with separate genetics, anatomy, and management pathways (butt2024conjunctivalmelanomaa pages 1-2) | **Curation note:** exact IDs for uncertain ontology mappings should be validated before production use |


*Table: Compact knowledge-base mapping table contrasting uveal melanoma with conjunctival melanoma across disease identity, genes, anatomy, phenotypes, mechanisms, and treatments. It highlights confirmed and suggested ontology mappings while avoiding invention of uncertain IDs.*

## 2. Etiology

### Causal and susceptibility factors

UM is usually an acquired clonal cancer. Early activating mutations in **GNAQ, GNA11, CYSLTR2,** or **PLCB4** initiate melanocytic proliferation; subsequent chromosomal and tumor-suppressor/splicing alterations govern malignant progression. Germline **BAP1** pathogenic variants cause autosomal-dominant BAP1 tumor-predisposition syndrome, which increases risks of UM, cutaneous melanoma, mesothelioma, and clear-cell renal carcinoma. Rare inherited MBD4 and other DNA-repair predispositions are also reported, but most UM is not inherited. (OpenTargets Search: uveal melanoma,ocular melanoma,conjunctival melanoma, kulbay2024uvealmelanomacomprehensive pages 2-5, fuentesrodriguez2024recentadvancesin pages 2-3)

Established host associations include older age, fair skin, light iris color, poor tanning/sunburn sensitivity, iris or choroidal nevus, oculodermal melanocytosis/nevus of Ota, dysplastic-nevus phenotype, and family history of melanoma. Occupational associations with welding or irritant exposure have been reported, but causality is less certain. Direct solar causation remains debated and is substantially weaker than in cutaneous melanoma because most UM arises in the sun-shielded choroid and has low mutational burden. (sorrentino2024geneticfeaturesof pages 1-2, kulbay2024uvealmelanomacomprehensive pages 2-5, pasalic2023geneticandepigenetic pages 1-2)

For Co-M, fair skin, older age, UV exposure/signatures, and precursor conjunctival melanocytic intraepithelial lesion are important. Approximately 70% arise from C-MIN/PAM with atypia; the remainder arise from nevi or de novo. BRAF occurs in approximately 30% and NRAS in approximately 14–25%; NRAS-mutant disease may have greater metastatic risk. (butt2024conjunctivalmelanomaa pages 1-2)

### Protective factors and gene–environment interaction

No genetic variant, diet, medication, or lifestyle intervention is proven to prevent UM. UV-protective eyewear is sensible for general ocular health and may be more biologically relevant to conjunctival/iris disease, but evidence that it prevents posterior UM is insufficient. A plausible gene–environment distinction is that UV exposure contributes more strongly to Co-M’s BRAF/NRAS/NF1-like landscape, whereas inherited pigmentation phenotype and rare BAP1 susceptibility interact with largely non-UV initiating events in UM. Smoking, alcohol, infection, exercise, and diet are not established causal or protective determinants.

## 3. Phenotypes

UM is often **insidious and unilateral**. Up to approximately 30% of patients are asymptomatic and diagnosed on routine ophthalmic examination. Symptoms depend on size and location: blurred or reduced vision, photopsias, floaters, visual-field loss, metamorphopsia, pain, and occasionally a visible iris lesion. Exudation, macular involvement, vitreous hemorrhage, or retinal detachment can produce severe or progressive vision loss. Iris tumors may present 10–20 years earlier than posterior tumors and cause heterochromia, corectopia, secondary glaucoma, or a growing pigmented lesion. (kastelan2024biologicalcharacteristicsand pages 1-2, kastelan2024biologicalcharacteristicsand pages 2-3)

Suggested HPO annotations include **decreased visual acuity**, **visual-field defect**, **photopsia**, **vitreous floaters**, **retinal detachment**, **ocular pain**, **heterochromia iridis**, **corectopia**, **secondary glaucoma**, and **unilateral ocular abnormality**. Frequencies beyond the approximately 30% asymptomatic estimate vary substantially by tumor site and referral population.

Co-M usually presents as a growing amelanotic, brown, or black conjunctival lesion—most often bulbar and near the limbus—sometimes with feeder vessels, irritation, or invasion of eyelid/orbit. It can cause loss of vision or eye, facial disfigurement, and death. Recurrence occurs in approximately 33–45%, regional nodal metastasis in approximately 25%, and reported five-year disease-specific mortality is approximately 27%. Suggested HPO terms include **conjunctival pigmentation**, **conjunctival mass**, **decreased visual acuity**, **recurrent neoplasm**, and **lymph-node metastasis**. (butt2024conjunctivalmelanomaa pages 1-2)

Quality-of-life burdens include visual disability, monocular depth-perception loss, treatment-related retinopathy/optic neuropathy, cosmetic change, anxiety, depression, and fear of recurrence. A 2024 French prospective protocol is specifically measuring HADS, FCRI, EORTC QLQ-C30, QLQ-OPT30, information satisfaction, and communication in 250 UM survivors, illustrating that psychological surveillance is now a recognized component of care. (kastelan2024biologicalcharacteristicsand pages 1-2)

## 4. Genetic and molecular information

### Somatic drivers and prognostic alterations

* **GNAQ/GNA11:** mutually exclusive gain-of-function mutations, usually at Q209 or R183, occur collectively in approximately 85–94% of UM; individual summaries report GNA11 around 55% and GNAQ around 40%. These are early events found even in benign uveal nevi and are not by themselves strong metastatic predictors. (kastelan2024biologicalcharacteristicsand pages 2-3, fuentesrodriguez2024recentadvancesin pages 2-3)
* **CYSLTR2 p.Leu129** occurs in approximately 2–4%, usually in GNAQ/GNA11-wild-type tumors. **PLCB4 p.Asp630** occurs in approximately 2.5%. Both are activating initiating events. (fuentesrodriguez2024recentadvancesin pages 2-3)
* **BAP1:** somatic loss-of-function—nonsense, frameshift, splice, missense, deletion, or loss of chromosome 3—is associated with class-2 phenotype, epithelioid morphology, early metastasis, and poor survival. One 2024 synthesis reports BAP1 alteration in approximately 38% of primary and 84% of metastatic samples. Germline pathogenic variants are rare and absent from or extremely rare in general-population databases. (kastelan2024biologicalcharacteristicsand pages 2-3, lissak2024whatsetsuveal pages 3-7)
* **SF3B1:** recurrent hotspot missense variants occur in approximately 20–25%, alter RNA splicing, and confer intermediate/late metastatic risk. **EIF1AX** variants occur in approximately 8–13% and usually mark lower-risk, disomy-3 tumors. These alterations are generally mutually exclusive with BAP1 loss. (kastelan2024biologicalcharacteristicsand pages 2-3, lissak2024whatsetsuveal pages 3-7)
* **MBD4:** biallelic DNA-glycosylase loss creates a hypermutated subset and may increase immunogenicity; Open Targets ranks MBD4 strongly among UM disease associations. (OpenTargets Search: uveal melanoma,ocular melanoma,conjunctival melanoma)

Somatic-driver allele frequencies are tumor frequencies, not population frequencies. Germline variant classification must use ClinVar/ClinGen and ACMG/AMP criteria; tumor-only sequencing cannot establish germline origin. VUS should not direct prophylactic surgery or family testing without validated reclassification.

### Chromosomal and epigenetic abnormalities

**Monosomy 3**, particularly with **8q gain/amplification**, is the canonical high-risk cytogenetic pattern. **6p gain** is generally associated with a more favorable disomy-3 class; 6q loss and complex 8q alterations occur in intermediate-risk/SF3B1 tumors. BAP1 loss reshapes chromatin and DNA methylation; class-1 versus class-2 UM has distinct methylation, transcriptomic, miRNA, and histone-regulatory programs. Altered miRNAs are promising diagnostic/prognostic biomarkers but are not yet standard standalone tests. (fuentesrodriguez2024recentadvancesin pages 2-3, pasalic2023geneticandepigenetic pages 1-2)

DecisionDx-UM’s 12-gene expression profile stratifies tumors into class **1A, 1B, and 2**, with reported five-year metastatic risks of approximately **2%, 21%, and 72%**, respectively. TCGA-style integration further divides UM into four molecular groups spanning disomy-3/EIF1AX through monosomy-3/BAP1/8q-amplified disease. These are prognostic—not proof that adjuvant systemic therapy improves survival. (fuentesrodriguez2024recentadvancesin pages 2-3)

## 5. Environmental information

No infectious agent is known to cause UM or Co-M; vaccination and antimicrobial prophylaxis are therefore not applicable. UV radiation has uncertain relevance to posterior UM but a more convincing relationship to conjunctival melanoma. Welding and selected occupational exposures are epidemiological signals rather than established sufficient causes. There is no reproducible evidence that tobacco, alcohol, obesity, diet, or physical inactivity materially changes UM risk. (kulbay2024uvealmelanomacomprehensive pages 2-5, butt2024conjunctivalmelanomaa pages 1-2)

## 6. Mechanism and pathophysiology

### Causal chain

1. A uveal melanocyte acquires activating **GNAQ/GNA11**, **CYSLTR2**, or **PLCB4** alteration.
2. Constitutive Gαq/11–TRIO–Rho and PLCβ signaling activates **PKC**, **RASGRP3–RAF–MEK–ERK**, **PI3K–AKT–mTOR**, and **YAP/TAZ** programs, promoting proliferation, survival, motility, calcium signaling, and metabolic adaptation.
3. A later **BAP1**, **SF3B1**, or **EIF1AX** event plus chromosome 3/6/8 evolution establishes prognostic phenotype. BAP1 loss disrupts deubiquitination, chromatin regulation, DNA repair, calcium homeostasis, differentiation, and metabolism.
4. Tumor cells undergo extracellular-matrix remodeling, transendothelial migration, and hematogenous dissemination; absence of ocular lymphatics helps explain UM’s blood-borne, liver-dominant route.
5. Dormant hepatic micrometastases may remain clinically occult for years before angiogenic and immune escape produces detectable disease. (kulbay2024uvealmelanomacomprehensive pages 2-5, fuentesrodriguez2024recentadvancesin pages 2-3, pasalic2023geneticandepigenetic pages 1-2)

Suggested GO terms include **MAPK cascade**, **protein kinase C signaling**, **phosphatidylinositol-mediated signaling**, **TOR signaling**, **cell proliferation**, **negative regulation of apoptosis**, **chromatin organization**, **DNA repair**, **RNA splicing**, **angiogenesis**, **cell migration**, **extracellular-matrix organization**, and **immune-response regulation**.

### Immune, tissue, and metabolic biology

The eye is immune privileged, and UM generally has low tumor mutational burden—approximately 0.5 mutations/Mb and a median of about 32 coding mutations in one clinical synthesis. Infiltration by lymphocytes and macrophages, HLA-I/II upregulation, NF-κB activation, LAG-3, and galectin-3 can paradoxically mark aggressive disease. Tumor-derived extracellular vesicles promote proliferation, migration, and invasion; circulating hybrid cells and ctDNA are emerging markers. (carvajal2022clinicalandmolecular pages 1-2, kulbay2024uvealmelanomacomprehensive pages 2-5)

A 2024 single-cell/bulk study analyzed **37,660 malignant cells from 17 tumors**, identifying substantial intratumoral transcriptional heterogeneity and two states with different prognosis and immune context. A separate 2024 study combined single-cell RNA/TCR sequencing with metastatic PDX and coculture experiments, finding tumor-reactive T cells among activated, exhausted, and cytotoxic-effector populations—supporting rational TIL/TCR selection. These are human-tissue plus experimental-model findings, not yet validated clinical diagnostics. (karlsson2024patientderivedxenograftsand pages 1-2)

## 7. Anatomical structures affected

Primary UM affects the **uvea**: choroid approximately 90%, ciliary body approximately 7%, and iris approximately 2–3%. Secondary local structures include retina, macula, optic disc/nerve, vitreous, sclera, anterior chamber, and orbit. UM is usually unilateral. Dissemination most often affects liver (approximately 89% or more), followed by lung and bone; one review reports lung 29% and bone 17%. (kulbay2024uvealmelanomacomprehensive pages 2-5, pasalic2023geneticandepigenetic pages 1-2)

Co-M begins in conjunctival epithelium, commonly bulbar conjunctiva/limbus, and may invade cornea, eyelid, lacrimal drainage structures, orbit, regional nodes, lung, liver, or brain. (butt2024conjunctivalmelanomaa pages 1-2)

Suggested UBERON terms: **eye**, **uvea**, **choroid**, **ciliary body**, **iris**, **retina**, **sclera**, **conjunctiva**, **bulbar conjunctiva**, **orbit**, and **liver**. Suggested CL terms: **melanocyte**, **endothelial cell**, **fibroblast**, **macrophage**, **CD8-positive T cell**, and **hepatic stellate cell**. Relevant subcellular GO compartments include **plasma membrane**, **nucleus/chromatin**, **spliceosomal complex**, **mitochondrion**, and **extracellular vesicle**.

## 8. Temporal development

UM is predominantly adult/late-adult onset; median diagnosis is approximately 58–62 years, whereas iris melanoma tends to present 10–20 years earlier. Onset is usually chronic and clinically silent. AJCC eighth-edition staging incorporates tumor size/category, ciliary-body involvement, and extraocular extension; metastatic disease is stage IV. (kastelan2024biologicalcharacteristicsand pages 1-2, kastelan2024biologicalcharacteristicsand pages 2-3)

At primary diagnosis, fewer than 2% have radiologically detectable metastases, yet 32–45% may develop them within 15 years and some recur more than 30 years later. This supports an early-dissemination/dormancy model and lifelong risk-adapted follow-up. Spontaneous durable remission is exceptional; treatment-induced local control is common, but eradication of occult micrometastases is not assured. (NCT05502900 chunk 1, pasalic2023geneticandepigenetic pages 1-2)

## 9. Inheritance and population

UM incidence is approximately 5–6 per million/year in the United States/Europe, about 7 per million in Australia, and only 0.2–0.3 per million/year in much of Asia and Africa. A 2024 synthesis gives a range of 4.9–7.4 per million in high-incidence populations. Most patients are White/Caucasian; sex differences are small and inconsistent. (kastelan2024biologicalcharacteristicsand pages 2-3, pasalic2023geneticandepigenetic pages 1-2)

Most UM is sporadic and multifactorial. **BAP1 tumor-predisposition syndrome** is autosomal dominant, incompletely penetrant, age-dependent, and variably expressive; anticipation and consanguinity are not characteristic. Founder variants may exist in particular families/populations, but there is no population-wide “carrier frequency” suitable for general screening. Germline testing is most appropriate for young onset, bilateral/multifocal UM, strong family history, or personal/family histories of mesothelioma, renal-cell carcinoma, cutaneous melanoma, or BAP1-inactivated melanocytic tumors.

Co-M incidence is approximately 0.46 per million/year, with an increasing rate ratio around 1.4 and a particularly sharp rise after age 65. It represents approximately 0.25% of all melanomas and 5% of ocular melanomas. (butt2024conjunctivalmelanomaa pages 1-2)

## 10. Diagnostics

### Clinical diagnosis

UM is often diagnosed clinically by an ocular oncologist using dilated fundus examination, slit-lamp examination for anterior tumors, color fundus photography, optical coherence tomography, fundus autofluorescence, and A-/B-scan ultrasonography. MRI can characterize selected lesions; systemic CT/MRI/ultrasound evaluates metastases, especially liver. Biopsy is not always required for a classic lesion but is used for uncertain diagnosis and molecular prognostication.

Histology shows spindle, mixed, or epithelioid melanoma; epithelioid morphology, high mitotic activity, closed vascular loops, ciliary-body involvement, and extrascleral extension are adverse features. Immunohistochemistry includes melanocytic markers such as SOX10, S100, Melan-A/MART1, HMB45, and nuclear BAP1. Co-M requires excisional biopsy when feasible, careful margin/orientation assessment, and evaluation for pagetoid intraepithelial spread. (butt2024conjunctivalmelanomaa pages 1-2, pasalic2023geneticandepigenetic pages 1-2)

Differential diagnosis includes choroidal nevus, congenital hypertrophy of retinal pigment epithelium, melanocytoma, hemangioma, metastasis, lymphoma, retinal-pigment-epithelium lesions, inflammatory granuloma, and hemorrhagic retinal detachment. Co-M differentials include conjunctival nevus, C-MIN/PAM, complexion-associated melanosis, foreign-body pigmentation, and ocular-surface squamous neoplasia.

### Genetic and omics testing

Fine-needle aspiration or resection tissue may undergo chromosome 3/8/6 testing by FISH, SNP array, MLPA, or NGS; BAP1/SF3B1/EIF1AX sequencing; and validated GEP. Broad WES/WGS is useful for atypical cases, research, or metastatic precision oncology but is not required for every primary tumor. CMA can detect copy-number changes; conventional karyotyping has limited sensitivity; mitochondrial and repeat-expansion testing are not relevant. (fuentesrodriguez2024recentadvancesin pages 2-3)

Blood ctDNA, circulating tumor cells, extracellular vesicles, miRNA, and circulating hybrid cells are promising for disease monitoring. Early ctDNA decline during tebentafusp correlates with survival, but liquid biopsy does not yet replace imaging or tissue-based risk classification. Normal liver-function tests cannot exclude hepatic metastasis. (carvajal2022clinicalandmolecular pages 1-2, pasalic2023geneticandepigenetic pages 1-2)

There is no population screening program. High-risk BAP1 families merit genetic counseling, cascade testing for a confirmed pathogenic familial variant, dermatologic/ophthalmic surveillance, and syndrome-specific renal/mesothelioma surveillance.

## 11. Outcome and prognosis

Overall five-year survival for UM is often reported at **50–70%**, with localized-disease estimates around 70–80%. Approximately half ultimately metastasize. Historical median survival after metastatic diagnosis is approximately 6–12 months, with liver involvement driving mortality; older series report nearly 90% mortality by two years after hepatic metastasis. (kastelan2024biologicalcharacteristicsand pages 2-3, pasalic2023geneticandepigenetic pages 1-2)

Adverse prognostic factors are large basal diameter/thickness, ciliary-body involvement, extraocular extension, epithelioid morphology, high mitotic rate, monosomy 3, 8q gain, BAP1 loss, class-2 GEP, elevated LDH, high hepatic tumor burden, and poor performance status. Favorable factors include small iris-confined disease, disomy 3, 6p gain, EIF1AX mutation, and class-1A GEP. SF3B1 generally denotes intermediate and sometimes late relapse. (lissak2024whatsetsuveal pages 3-7, fuentesrodriguez2024recentadvancesin pages 2-3, pasalic2023geneticandepigenetic pages 1-2)

Morbidity includes irreversible visual-field loss, radiation retinopathy, maculopathy, optic neuropathy, cataract, glaucoma, dry eye, enucleation-related monocular disability, and psychological distress. Co-M adds repeated surface surgery, limbal-stem-cell injury, scarring, and possible orbital exenteration. (kastelan2024biologicalcharacteristicsand pages 1-2, butt2024conjunctivalmelanomaa pages 1-2)

## 12. Treatment

### Localized UM

Management is individualized by size, location, visual potential, extraocular extension, and patient preference. Options include observation of selected indeterminate/small lesions; plaque brachytherapy; proton-beam or stereotactic radiotherapy; transpupillary thermotherapy as an adjunct in selected small lesions; local resection; and enucleation for very large, painful, blind, or extensively invasive tumors. Local control does not eliminate pre-existing micrometastases. Suggested NCIT concepts include **Plaque Brachytherapy**, **Proton Radiation Therapy**, **Local Excision**, and **Enucleation**. (kastelan2024biologicalcharacteristicsand pages 2-3, pasalic2023geneticandepigenetic pages 1-2)

### Conjunctival melanoma

Preferred treatment is “no-touch” complete excision with margin control, often with adjuvant cryotherapy. Topical mitomycin-C or interferon, plaque/proton/photon radiotherapy, and exenteration are selected by intraepithelial spread, margins, multifocality, and invasion. Lifelong ocular and nodal surveillance is warranted. BRAF/MEK inhibition or PD-1-based immunotherapy may be considered for molecularly appropriate unresectable/metastatic disease, but evidence remains mainly case reports and small series. (butt2024conjunctivalmelanomaa pages 1-2)

### Metastatic UM

**Tebentafusp** is an engineered gp100–HLA-A*02:01 T-cell-receptor/CD3 bispecific and the preferred evidence-based systemic option for eligible HLA-A*02:01-positive, unresectable/metastatic UM. In the phase III long-term analysis, median overall survival was **21.6 versus 16.9 months** with control (HR 0.68, 95% CI 0.54–0.87), and three-year survival was **27% versus 18%**. Common adverse events were rash 83%, pyrexia 76%, pruritus 70%, and hypotension 38%; only 2% discontinued for toxicity, and there were no treatment-related deaths. Publication: 14 December 2023; DOI/URL: https://doi.org/10.1056/NEJMoa2304753; NCT03070392. The abstract concludes that the analysis “supported a continued long-term benefit of tebentafusp for overall survival.” (hassel2023threeyearoverallsurvival pages 1-3)

In a 127-patient phase II refractory cohort, objective response was only 5%, but one-year survival was 62% and median survival 16.8 months, illustrating that RECIST response underestimates benefit. Early ctDNA reduction correlated with survival. Publication: October 2022; DOI/URL: https://doi.org/10.1038/s41591-022-02015-7; NCT02570308. (carvajal2022clinicalandmolecular pages 1-2)

Checkpoint inhibitors—pembrolizumab/nivolumab, ipilimumab, or combinations—have substantially less activity than in cutaneous melanoma because UM is low-TMB and immunosuppressive, but they remain options when tebentafusp is unavailable/inapplicable or in trials. Cytotoxic chemotherapy has low response rates. Liver-dominant disease may be treated with resection/ablation in selected oligometastatic cases, embolization/radioembolization, immunoembolization, isolated or percutaneous hepatic perfusion with melphalan, or other center-specific liver-directed approaches. Multidisciplinary sequencing is essential. (kulbay2024uvealmelanomacomprehensive pages 2-5, pasalic2023geneticandepigenetic pages 1-2, hassel2023threeyearoverallsurvival pages 1-3)

### Active/late-phase development

* **Darovasertib**, an oral selective PKC inhibitor: phase II neoadjuvant/adjuvant trial in 160 localized-UM patients, testing tumor shrinkage, conversion from enucleation to radiation, reduction of radiation dose to critical structures, and long-term metastasis outcomes; **NCT05907954**. (NCT05907954 chunk 1)
* **Belzupacap sarotalocan/AU-011:** randomized, double-masked phase III suprachoroidal drug-plus-laser photoactivation study in 108 patients with indeterminate lesions or small choroidal melanoma; **NCT06007690**. (NCT06007690 chunk 1)
* **Adjuvant melatonin:** randomized open-label phase III trial of 20 mg nightly for five years in 100 high-risk patients, with metastasis incidence as the primary endpoint; **NCT05502900**. This is experimental, not preventive standard care. (NCT05502900 chunk 1)

No validated CPIC-style pharmacogenomic dosing guideline, approved gene therapy, CAR-T product, RNA therapy, or stem-cell therapy currently exists for ocular melanoma.

## 13. Prevention

**Primary prevention:** no intervention is proven to prevent UM. Sun-safe behavior and UV-blocking eyewear are reasonable, particularly for conjunctival/iris health, but should not be represented as proven posterior-UM prevention. There is no vaccine or chemoprophylaxis.

**Secondary prevention:** no population screening is recommended because the disease is rare. Routine eye examinations can detect asymptomatic tumors; targeted surveillance is appropriate for choroidal nevi with suspicious growth features, oculodermal melanocytosis, and BAP1 families. Prompt referral of suspicious conjunctival pigmentation prevents diagnostic delay.

**Tertiary prevention:** preserve vision through timely local treatment and manage radiation retinopathy, glaucoma, cataract, and psychosocial morbidity. Molecular risk stratification guides hepatic imaging every 3–12 months depending on risk; the 2024 GEP review suggests annual imaging for class 1A, every 6–12 months for class 1B, and every 3–6 months for class 2, although schedules vary by guideline and country. (fuentesrodriguez2024recentadvancesin pages 2-3)

## 14. Other species and natural disease

Naturally occurring ocular melanocytic neoplasms occur in dogs, cats, and horses. Canine anterior-uveal melanoma is often locally invasive but biologically less predictably metastatic than human posterior UM; feline diffuse iris melanoma can cause glaucoma and metastasis; equine ocular melanocytic disease has breed/color associations. These conditions are veterinary diseases and useful comparative pathology, but they are not exact orthologous models of human GNAQ/GNA11-driven, liver-tropic UM. No infectious transmission or zoonotic potential exists. Suggested taxa include **Homo sapiens (NCBI:9606)**, **Canis lupus familiaris (9615)**, **Felis catus (9685)**, **Equus caballus (9796)**, **Mus musculus (10090)**, and **Danio rerio (7955)**. Breed-specific VBO mappings require veterinary-database curation.

## 15. Model organisms

Model systems include established UM cell lines, three-dimensional spheroids/organoids, primary cultures, chicken chorioallantoic membrane assays, zebrafish xenografts/transgenics, mouse subcutaneous and orthotopic xenografts, PDX, syngeneic models, and genetically engineered GNAQ/GNA11-pathway models.

A 2023 zebrafish PDX platform generated spheroids from primary human UM within 24 hours, retained melanocytic markers, and produced a reproducible metastatic phenotype after intravenous implantation. Experiments used at least two biological replicates with more than 20 fish each; navitoclax and everolimus demonstrated utility for rapid drug-response screening. Publication: 15 April 2023; DOI/URL: https://doi.org/10.3390/ph16040598. The abstract states that the model “recapitulated molecular features of the disseminating UM.” (yin2023zebrafishpatientderivedxenograft pages 1-2)

Mouse PDX preserves patient-specific architecture/genomics and supports pharmacology, while orthotopic models reproduce ocular growth. Limitations include immunodeficiency, variable engraftment, cost, long latency, and incomplete hepatic tropism. Syngeneic models retain immunity but frequently use cutaneous melanoma cells whose genetics differ from UM. Zebrafish enables live imaging, small sample requirements, and high-throughput screening but differs in temperature, pharmacokinetics, adaptive immunity, and ocular/liver physiology. No single model reproduces the complete human genetic, histologic, immune, dormancy, and metastatic phenotype; convergent validation across organoid, zebrafish, PDX, and immune-competent systems is preferable. (yin2023zebrafishpatientderivedxenograft pages 1-2, karlsson2024patientderivedxenograftsand pages 1-2)

## Evidence-quality and curation notes

The strongest treatment evidence is the randomized phase III tebentafusp trial. Epidemiology, genetics, and natural history are supported by large aggregated cohorts and recent 2023–2024 reviews, whereas protective factors, Co-M systemic therapy, adjuvant prevention, liquid-biopsy surveillance, and many multi-omics signatures remain investigational. Direct abstract quotations were limited to short passages to preserve context. DOI URLs and publication dates are provided where retrieved; PMIDs were not consistently present in the retrieved metadata and should be added through PubMed cross-linking rather than inferred. Exact HPO, UBERON, CL, GO, NCIT, ICD-11, OMIM, Orphanet, and MeSH identifiers flagged as “suggested” should undergo ontology-service validation before production ingestion.

References

1. (butt2024conjunctivalmelanomaa pages 1-2): Karam Butt, Rumana Hussain, Sarah Ellen Coupland, and Yamini Krishna. Conjunctival melanoma: a clinical review and update. Cancers, Sep 2024. URL: https://doi.org/10.3390/cancers16183121, doi:10.3390/cancers16183121. This article has 20 citations.

2. (pasalic2023geneticandepigenetic pages 1-2): Daria Pašalić, Tamara Nikuševa-Martić, Ankica Sekovanić, and Snježana Kaštelan. Genetic and epigenetic features of uveal melanoma—an overview and clinical implications. International Journal of Molecular Sciences, 24:12807, Aug 2023. URL: https://doi.org/10.3390/ijms241612807, doi:10.3390/ijms241612807. This article has 23 citations.

3. (kastelan2024biologicalcharacteristicsand pages 2-3): SNJEŽANA KAŠTELAN, ANA DIDOVIĆ PAVIČIĆ, DARIA PAŠALIĆ, TAMARA NIKUŠEVA-MARTIĆ, SAMIR ČANOVIĆ, PETRA KOVAČEVIĆ, and SUZANA KONJEVODA. Biological characteristics and clinical management of uveal and conjunctival melanoma. Oncology Research, 32:1265-1285, Jul 2024. URL: https://doi.org/10.32604/or.2024.048437, doi:10.32604/or.2024.048437. This article has 9 citations and is from a peer-reviewed journal.

4. (fuentesrodriguez2024recentadvancesin pages 2-3): Aurélie Fuentes-Rodriguez, Andrew Mitchell, Sylvain L. Guérin, and Solange Landreville. Recent advances in molecular and genetic research on uveal melanoma. Cells, 13:1023, Jun 2024. URL: https://doi.org/10.3390/cells13121023, doi:10.3390/cells13121023. This article has 27 citations.

5. (hassel2023threeyearoverallsurvival pages 1-3): Jessica C. Hassel, Sophie Piperno-Neumann, Piotr Rutkowski, Jean-Francois Baurain, Max Schlaak, Marcus O. Butler, Ryan J. Sullivan, Reinhard Dummer, John M. Kirkwood, Marlana Orloff, Joseph J. Sacco, Sebastian Ochsenreither, Anthony M. Joshua, Lauris Gastaud, Brendan Curti, Josep M. Piulats, April K.S. Salama, Alexander N. Shoushtari, Lev Demidov, Mohammed Milhem, Bartosz Chmielowski, Kevin B. Kim, Richard D. Carvajal, Omid Hamid, Laura Collins, Koustubh Ranade, Chris Holland, Constance Pfeiffer, and Paul Nathan. Three-year overall survival with tebentafusp in metastatic uveal melanoma. New England Journal of Medicine, 389:2256-2266, Dec 2023. URL: https://doi.org/10.1056/nejmoa2304753, doi:10.1056/nejmoa2304753. This article has 341 citations and is from a highest quality peer-reviewed journal.

6. (OpenTargets Search: uveal melanoma,ocular melanoma,conjunctival melanoma): Open Targets Query (uveal melanoma,ocular melanoma,conjunctival melanoma, 31 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

7. (lissak2024whatsetsuveal pages 1-3): Karina Lissak, Zuzanna Szczepaniak, Agata Konopka, Natalia Wdowiak, Martyna Choinka, Małgorzata Komarów, Dominika Karasińska, Jakub Kalisiak, Mateusz Koralewicz, Milena Orzeł, and Bartłomiej Orzeł. What sets uveal melanoma apart, and how can we address it? a comprehensive review of pathophysiology, diagnosis and treatment. Quality in Sport, 23:55123, Sep 2024. URL: https://doi.org/10.12775/qs.2024.23.55123, doi:10.12775/qs.2024.23.55123. This article has 1 citations.

8. (kulbay2024uvealmelanomacomprehensive pages 2-5): Merve Kulbay, Emily Marcotte, Raheem Remtulla, Tsz Hin Alexander Lau, Manuel Paez-Escamilla, Kevin Y. Wu, and Miguel N. Burnier. Uveal melanoma: comprehensive review of its pathophysiology, diagnosis, treatment, and future perspectives. Biomedicines, 12:1758, Aug 2024. URL: https://doi.org/10.3390/biomedicines12081758, doi:10.3390/biomedicines12081758. This article has 48 citations.

9. (lissak2024whatsetsuveal pages 3-7): Karina Lissak, Zuzanna Szczepaniak, Agata Konopka, Natalia Wdowiak, Martyna Choinka, Małgorzata Komarów, Dominika Karasińska, Jakub Kalisiak, Mateusz Koralewicz, Milena Orzeł, and Bartłomiej Orzeł. What sets uveal melanoma apart, and how can we address it? a comprehensive review of pathophysiology, diagnosis and treatment. Quality in Sport, 23:55123, Sep 2024. URL: https://doi.org/10.12775/qs.2024.23.55123, doi:10.12775/qs.2024.23.55123. This article has 1 citations.

10. (karlsson2024patientderivedxenograftsand pages 1-2): Joakim Karlsson, Vasu R. Sah, Roger Olofsson Bagge, Munir Iqbal, Samuel Alsén, Sofia Stenqvist, Alka Saxena, Lars Ny, Lisa M. Nilsson, and Jonas A. Nilsson. Patient-derived xenografts and single-cell sequencing identifies three subtypes of tumor-reactive lymphocytes in uveal melanoma metastases. eLife, May 2024. URL: https://doi.org/10.7554/elife.91705, doi:10.7554/elife.91705. This article has 6 citations and is from a domain leading peer-reviewed journal.

11. (kastelan2024biologicalcharacteristicsand pages 1-2): SNJEŽANA KAŠTELAN, ANA DIDOVIĆ PAVIČIĆ, DARIA PAŠALIĆ, TAMARA NIKUŠEVA-MARTIĆ, SAMIR ČANOVIĆ, PETRA KOVAČEVIĆ, and SUZANA KONJEVODA. Biological characteristics and clinical management of uveal and conjunctival melanoma. Oncology Research, 32:1265-1285, Jul 2024. URL: https://doi.org/10.32604/or.2024.048437, doi:10.32604/or.2024.048437. This article has 9 citations and is from a peer-reviewed journal.

12. (NCT05907954 chunk 1):  (Neo)Adjuvant IDE196 (Darovasertib) in Patients With Localized Ocular Melanoma. IDEAYA Biosciences. 2023. ClinicalTrials.gov Identifier: NCT05907954

13. (NCT06007690 chunk 1):  A Phase 3 Randomized, Masked, Controlled Trial to Evaluate Efficacy and Safety of Belzupacap Sarotalocan (AU-011) Treatment Compared to Sham Control in Subjects With Primary Indeterminate Lesions or Small Choroidal Melanoma. Aura Biosciences. 2023. ClinicalTrials.gov Identifier: NCT06007690

14. (NCT05502900 chunk 1): Gustav Stalhammar. Adjuvant Melatonin for Uveal Melanoma. Gustav Stalhammar. 2022. ClinicalTrials.gov Identifier: NCT05502900

15. (yin2023zebrafishpatientderivedxenograft pages 1-2): Jie Yin, Gangyin Zhao, Helen Kalirai, Sarah E. Coupland, Aart G. Jochemsen, Gabriel Forn-Cuní, Annemijn P. A. Wierenga, Martine J. Jager, B. Ewa Snaar-Jagalska, and Arwin Groenewoud. Zebrafish patient-derived xenograft model as a preclinical platform for uveal melanoma drug discovery. Pharmaceuticals, 16:598, Apr 2023. URL: https://doi.org/10.3390/ph16040598, doi:10.3390/ph16040598. This article has 22 citations.

16. (sorrentino2024geneticfeaturesof pages 1-2): Francesco Saverio Sorrentino, Carola Culiersi, Antonio Florido, Katia De Nadai, Ginevra Giovanna Adamo, Francesco Nasini, Chiara Vivarelli, Marco Mura, and Francesco Parmeggiani. Genetic features of uveal melanoma. Genes, 15:1356, Oct 2024. URL: https://doi.org/10.3390/genes15111356, doi:10.3390/genes15111356. This article has 12 citations.

17. (carvajal2022clinicalandmolecular pages 1-2): Richard D. Carvajal, Marcus O. Butler, Alexander N. Shoushtari, Jessica C. Hassel, Alexandra Ikeguchi, Leonel Hernandez-Aya, Paul Nathan, Omid Hamid, Josep M. Piulats, Matthew Rioth, Douglas B. Johnson, Jason J. Luke, Enrique Espinosa, Serge Leyvraz, Laura Collins, Howard M. Goodall, Koustubh Ranade, Chris Holland, Shaad E. Abdullah, Joseph J. Sacco, and Takami Sato. Clinical and molecular response to tebentafusp in previously treated patients with metastatic uveal melanoma: a phase 2 trial. Nature Medicine, 28:2364-2373, Oct 2022. URL: https://doi.org/10.1038/s41591-022-02015-7, doi:10.1038/s41591-022-02015-7. This article has 196 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Ocular_Melanoma-deep-research-falcon_artifacts/artifact-00.md)