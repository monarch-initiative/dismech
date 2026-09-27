---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-01T05:01:08.359229'
end_time: '2026-08-01T05:22:07.035063'
duration_seconds: 1258.68
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Perrault Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 30
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Perrault_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Perrault Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Perrault Syndrome** covering all of the
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
- **Disease Name:** Perrault Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Perrault Syndrome** covering all of the
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


# Perrault Syndrome: Disease-Characteristics Research Report

## Executive summary

Perrault syndrome is a rare, clinically and genetically heterogeneous **autosomal-recessive, sex-influenced Mendelian disorder**. Its defining manifestations are bilateral sensorineural hearing loss (SNHL) in 46,XX and 46,XY individuals and hypergonadotropic ovarian insufficiency/dysgenesis in 46,XX individuals. Hearing loss ranges from congenital severe/profound disease to milder adult-onset loss; ovarian disease ranges from secondary amenorrhea to absent/streak ovaries, failed puberty, and primary amenorrhea. Neurologic, renal, growth, muscular, and other mitochondrial-system manifestations occur variably. The literature commonly distinguishes type 1 disease without neurologic involvement from type 2 disease with neurologic manifestations, but these clinical categories must not be confused with numbered OMIM molecular subtypes. (faridi2022newinsightsinto pages 1-3, kline2022integralroleof pages 1-2)

The best-supported 2022 core genes were **CLPP, ERAL1, GGPS1, HARS2, HSD17B4, LARS2, RMND1, and TWNK**. Depending on cohort definition, these explained only approximately 40–50% of clinically diagnosed cases. More recent work supports an expanded mitochondrial/peroxisomal spectrum involving **PRORP, TFAM, PEX6, MRPS7, MRPL50**, and—reported online in December 2024—**DAP3/MRPS29**. These expanded associations are not all equally curated and should not automatically be treated as equivalent to the core eight-gene set. (faridi2022newinsightsinto pages 1-3, kline2022integralroleof pages 1-2, smith2025biallelicvariantsin pages 1-2)

No disease-modifying treatment, approved targeted therapy, validated preventive medication, or Perrault-specific interventional trial was identified. Current implementation is multidisciplinary and supportive: hearing aids or cochlear implantation, estrogen/progestogen replacement when indicated, bone and cardiovascular protection, fertility counseling/assisted reproduction, rehabilitation, and genotype-directed neurologic, renal, hepatic, cardiac, and metabolic surveillance. (faridi2022newinsightsinto pages 11-13, oziebło2020twonovelpathogenic pages 1-3)

---

## 1. Disease information

### Definition and terminology

Perrault syndrome is also called **ovarian dysgenesis with sensorineural deafness**, **XX gonadal dysgenesis with deafness**, or **hearing loss–ovarian insufficiency syndrome**. The defining association is not merely infertility plus deafness: in 46,XX individuals, laboratory evidence generally demonstrates **hypergonadotropic hypogonadism**, reflecting primary ovarian rather than hypothalamic/pituitary failure. A succinct exact statement from Faridi et al. is: “Perrault syndrome is inherited as an autosomal recessive disorder characterized by bilateral mild to severe childhood sensorineural hearing loss with variable age of onset in both sexes and ovarian dysfunction in females who have a 46, XX karyotype.” (faridi2022newinsightsinto pages 1-3)

### Identifiers

* **MONDO:** **MONDO:0017312** (Perrault syndrome). Open Targets maps this entity to 12 associated targets, while retaining separate molecular subtype entries. (OpenTargets Search: Perrault syndrome)
* **OMIM clinical/molecular series:** commonly cited entries include **PRLTS1 #233400**, **PRLTS2 #614926**, **PRLTS4 #615300**, **PRLTS5 #616138**, and **PRLTS6 #617565**. The numbered subtype scheme is gene-based and is distinct from clinical “type 1/type 2” classification. (faridi2022newinsightsinto pages 1-3, forli2021ararecase pages 1-2)
* **Orphanet:** an Orphanet disease record exists, but its precise ORPHA number was not verified in the retrieved primary-text evidence and should be checked directly against the current Orphanet nomenclature release before database ingestion.
* **ICD-10/ICD-11:** no highly specific Perrault syndrome code was established in the retrieved evidence. Real-world coding generally requires component codes for congenital/hereditary SNHL, primary ovarian insufficiency/gonadal dysgenesis, and the relevant genetic syndrome.
* **MeSH:** no dedicated MeSH descriptor was verified; indexing commonly uses Sensorineural Hearing Loss, Primary Ovarian Insufficiency, Gonadal Dysgenesis, and mitochondrial/peroxisomal disease terms.

### Evidence provenance

The syndrome-level definition and gene lists are **aggregated disease-level knowledge** synthesized from literature and databases. Most frequencies and genotype–phenotype observations, however, derive from individual pedigrees, case reports, small case series, and sequencing cohorts—not EHR-scale population studies. Accordingly, ascertainment and publication bias are substantial.

---

## 2. Etiology, risk, protective factors, and gene–environment interaction

### Primary cause

The primary cause is **biallelic germline pathogenic or likely pathogenic variation** in genes governing mitochondrial translation, mitoribosome assembly, mitochondrial RNA processing, mtDNA maintenance, mitochondrial proteostasis/metabolism, or peroxisomal function. Somatic causation is not characteristic. (faridi2022newinsightsinto pages 1-3, kline2022integralroleof pages 1-2)

### Genetic risk factors

* An affected individual usually inherits one pathogenic allele from each heterozygous parent.
* Consanguinity increases the probability that both parents carry the same rare pathogenic allele and is represented in several reported families, but is not necessary; compound-heterozygous disease is well documented. (hochberg2021biallelicvariantsin pages 1-2, oziebło2020twonovelpathogenic pages 1-3)
* For two carrier parents, standard autosomal-recessive recurrence probabilities are 25% affected, 50% carrier, and 25% unaffected/non-carrier for each pregnancy. Ovarian manifestations are sex/karyotype influenced, whereas hearing and neurologic manifestations can occur in either sex.
* Variant severity can influence expressivity. More disruptive alleles in mitochondrial genes may produce broader combined oxidative-phosphorylation disease rather than the relatively restricted Perrault phenotype. (kline2022integralroleof pages 8-9, faridi2022newinsightsinto pages 1-3)

### Environmental, lifestyle, and infectious risks

No toxin, infection, radiation exposure, smoking pattern, diet, occupation, or lifestyle factor has been established as a cause of Mendelian Perrault syndrome. The 2022 review explicitly notes that environmental etiologies remain to be identified for unresolved cases, which is a research gap rather than evidence for a known environmental cause. There are no established protective alleles, diets, supplements, vaccines, or exposure modifications that prevent the syndrome. (faridi2022newinsightsinto pages 1-3)

### Gene–environment interaction

No reproducible Perrault-specific gene–environment interaction is known. General mitochondrial stressors could plausibly modify clinical expression, but this remains unproven. The 2024 CLPP-null metabolomics study proposed arginine/histidine supplementation as a hypothesis for growth deficits; this was model-derived and is **not clinical efficacy evidence**. (key2024clppnulleukaryoteswith pages 1-2)

---

## 3. Phenotypes

| Manifestation | Type, onset, course, frequency | Suggested HPO terms |
|---|---|---|
| Bilateral SNHL | Defining sign in both sexes; congenital to adult onset; mild to profound; often childhood-onset and may be progressive. A recent CLPP literature synthesis reported hearing loss in 31/32 evaluable patients (97%), but this is gene-specific, not syndrome-wide. | **HP:0000407** Sensorineural hearing impairment; **HP:0000365** Hearing impairment; **HP:0008619** Bilateral sensorineural hearing impairment; **HP:0001730** Progressive hearing impairment |
| Auditory neuropathy | Uncommon; documented with TWNK, HARS2, and CLPP. Newborn screening may initially be normal before progressive disease. | **HP:0012716** Auditory neuropathy |
| Primary ovarian insufficiency | Defining in affected 46,XX individuals; may become apparent during pubertal development or reproductive life. | **HP:0008209** Premature ovarian insufficiency; **HP:0000134** Female hypogonadism |
| Ovarian dysgenesis/streak or absent ovaries | Congenital developmental manifestation; variable from small ovaries to complete failure of development. | **HP:0000133** Gonadal dysgenesis; **HP:0008724** Hypoplasia of the ovary |
| Primary/secondary amenorrhea | Primary amenorrhea with failed puberty in severe disease; secondary amenorrhea in milder disease. | **HP:0000786** Primary amenorrhea; **HP:0000869** Secondary amenorrhea |
| Hypergonadotropic hypogonadism | Elevated FSH/LH and low estradiol. One MRPS7 case had FSH 102 IU/mL and estradiol 29 pg/mL. | **HP:0008213** Hypergonadotropic hypogonadism; **HP:0002925** Elevated circulating gonadotropin level; **HP:0003230** Decreased circulating estrogen level |
| Infertility | Common consequence of ovarian failure; CLPP-associated male azoospermia has also been reported, although normal XY reproductive development is typical in classic definitions. | **HP:0000789** Infertility; **HP:0000027** Azoospermia |
| Neurologic disease | Variable: developmental delay/intellectual disability, ataxia, peripheral/motor neuropathy, muscle weakness/atrophy, nystagmus/limited eye movement, seizures, leukodystrophy or cerebellar atrophy. May be progressive. CLPP synthesis: 16/29 (55%) neurologic disease. | **HP:0001250** Seizure; **HP:0001251** Ataxia; **HP:0001263** Global developmental delay; **HP:0000762** Decreased nerve conduction velocity; **HP:0001272** Cerebellar atrophy; **HP:0002415** Leukodystrophy |
| Renal disease | Genotype-dependent, especially RMND1 and severe mitoribosomal disease; chronic kidney disease or renal failure. | **HP:0012622** Chronic kidney disease; **HP:0000083** Renal insufficiency |
| Growth and multisystem disease | Short stature/growth restriction, hepatic disease, cardiomyopathy, lactic acidosis, muscular disease, cataract or neutropenia occur in selected expanded-spectrum genotypes. | **HP:0004322** Short stature; **HP:0003128** Lactic acidosis; **HP:0001638** Cardiomyopathy; **HP:0001392** Abnormal liver morphology |

The clinical impact is substantial: hearing loss affects communication, education, language development and employment; ovarian failure affects puberty, fertility, bone density, sexual health and psychosocial well-being; neurologic disease can impair gait and independent living. Nevertheless, no Perrault-specific EQ-5D, SF-36, PROMIS, or disease-specific quality-of-life cohort was identified. (faridi2022newinsightsinto pages 1-3, kline2022integralroleof pages 1-2, oziebło2020twonovelpathogenic pages 1-3, forli2021ararecase pages 1-2)

---

## 4. Genetic and molecular information

The following evidence-tiered table is appropriate for knowledge-base curation. “Expanded-spectrum/candidate” means that convincing case or functional evidence exists but the relationship may not yet have the same replication or expert-panel status as the core genes.

| Gene | Molecular role / compartment | Evidence status | Representative phenotype or variant evidence | Key source DOI / PMID |
|---|---|---|---|---|
| **CLPP** | Mitochondrial matrix peptidase; mitochondrial protein quality control | **Core established (2022 core set)** | Biallelic **CLPP** variants cause Perrault syndrome type 3 with SNHL and POI; human and mouse loss causes infertility/deafness/ataxia; recent Chinese series summarized **33 PRLTS3 patients**, with **97% hearing loss**, **55% neurologic disease**, **71% of females POI** (faridi2022newinsightsinto pages 1-3, key2024clppnulleukaryoteswith pages 1-2, key2022clppdepletioncauses pages 1-2) | Faridi 2022 DOI: **10.1007/s00439-021-02319-7**; Key 2024 DOI: **10.3390/biom14020241**; Key 2022/Cells 2023 DOI: **10.3390/cells12010052** |
| **ERAL1** | Mitochondrial 12S rRNA chaperone; small mitoribosomal subunit assembly | **Core established (2022 core set)** | Included among the eight genes with supporting evidence in the 2022 review; implicated in mitochondrial translation/ribosome assembly dysfunction in Perrault syndrome (faridi2022newinsightsinto pages 1-3, faridi2022newinsightsinto pages 11-13) | Faridi 2022 DOI: **10.1007/s00439-021-02319-7** |
| **GGPS1** | Lipid/isoprenoid synthesis; geranylgeranyl diphosphate synthase | **Core established (2022 core set)** | Included in the eight-gene core set; genomic sequencing review classified it among metabolic causes of Perrault syndrome (faridi2022newinsightsinto pages 1-3, tucker2020genomicsequencinghighlights pages 1-7) | Faridi 2022 DOI: **10.1007/s00439-021-02319-7**; Tucker 2020 DOI: **10.1007/s00439-020-02176-w** |
| **HARS2** | Mitochondrial histidyl-tRNA synthetase; mitochondrial translation | **Core established (2022 core set)** | Included in the eight-gene core set; Perrault syndrome review notes HARS2-associated disease often lacks neurologic features relative to other genes (faridi2022newinsightsinto pages 1-3, faridi2022newinsightsinto pages 11-13) | Faridi 2022 DOI: **10.1007/s00439-021-02319-7** |
| **HSD17B4** | Peroxisomal fatty-acid oxidation / steroid metabolism; peroxisome | **Core established (2022 core set)** | Included in the eight-gene core set; distinguished as a peroxisomal contributor to Perrault syndrome rather than a primary mitochondrial translation defect (faridi2022newinsightsinto pages 1-3, faridi2022newinsightsinto pages 11-13) | Faridi 2022 DOI: **10.1007/s00439-021-02319-7** |
| **LARS2** | Mitochondrial leucyl-tRNA synthetase; mitochondrial translation | **Core established (2022 core set)** | Biallelic **LARS2** mutations linked to premature ovarian failure and hearing loss in Perrault syndrome; repeatedly cited as a core mitochondrial translation gene (faridi2022newinsightsinto pages 1-3, key2022clppdepletioncauses pages 1-2) | Pierce 2013 DOI: **10.1016/j.ajhg.2013.03.007**; Faridi 2022 DOI: **10.1007/s00439-021-02319-7** |
| **RMND1** | Mitochondrial inner-membrane translation factor; couples mitochondrial transcript handling to translation | **Core established (2022 core set)** | Two adult sisters with compound heterozygous **RMND1** variants **c.583G>A (p.Gly195Arg)** and **c.818A>C (p.Tyr273Ser)** had SNHL, ovarian dysfunction, and chronic kidney disease, providing independent confirmation of causality (oziebło2020twonovelpathogenic pages 1-3, oziebło2020twonovelpathogenic pages 3-5) | Oziębło 2020 DOI: **10.3390/genes11091060** |
| **TWNK** | Twinkle mtDNA helicase; mitochondrial DNA maintenance / nucleoid | **Core established (2022 core set)** | Included in the eight-gene core set; recognized as an mtDNA maintenance cause of Perrault syndrome and auditory neuropathy-spectrum presentations in literature review (faridi2022newinsightsinto pages 1-3, forli2021ararecase pages 1-2) | Faridi 2022 DOI: **10.1007/s00439-021-02319-7** |
| **PRORP** | Mitochondrial RNase P catalytic subunit; mitochondrial tRNA 5′-processing | **Expanded-spectrum / newer established beyond 2022 core set** | Bi-allelic **PRORP** variants caused impaired mitochondrial tRNA processing with decreased protein levels, rescue by WT cDNA, and multisystem presentations including SNHL and POI; earlier family had **~35–45%** reduction in 5′-processed tRNA in RNase P assays (hochberg2021biallelicvariantsin pages 1-2) | Hochberg 2021 DOI: **10.1016/j.ajhg.2021.10.002**; preprint DOI: **10.1101/168252** |
| **TFAM** | Mitochondrial transcription factor A; mtDNA packaging/maintenance | **Expanded-spectrum / candidate** | Genomic sequencing paper highlighted **TFAM** among mtDNA maintenance/translation causes in Perrault syndrome pedigrees, but it was not part of the 2022 eight-gene core set (tucker2020genomicsequencinghighlights pages 1-7, kline2022integralroleof pages 1-2) | Tucker 2020 DOI: **10.1007/s00439-020-02176-w** |
| **PEX6** | Peroxisome biogenesis ATPase; peroxisome | **Expanded-spectrum / candidate** | Genomic sequencing study identified **PEX6** as a peroxisomal molecular cause in individuals labeled Perrault syndrome, supporting expansion beyond classic mitochondrial genes (tucker2020genomicsequencinghighlights pages 1-7, faridi2022newinsightsinto pages 11-13) | Tucker 2020 DOI: **10.1007/s00439-020-02176-w** |
| **MRPS7** | Mitochondrial ribosomal small-subunit protein 7; mitoribosome | **Expanded-spectrum / candidate** | Compound heterozygous **MRPS7** variants **c.373A>T (p.Lys125*)** and **c.536G>A (p.Arg179His)** in a 25-year-old woman with hearing loss and POI; authors state this “validates” MRPS7 as a cause of syndromic POI/Perrault syndrome (kline2022integralroleof pages 1-2, kline2022integralroleof pages 5-8, kline2022integralroleof pages 8-9) | Kline 2022 DOI: **10.3390/genes13112113** |
| **MRPL50** | Mitochondrial ribosomal large-subunit protein; mitoribosome | **Expanded-spectrum / candidate** | Mentioned in the 2025 DAP3 study summary as part of the broader Perrault-spectrum literature involving mitochondrial ribosomal defects, but detailed primary evidence was not retrieved here (smith2025biallelicvariantsin pages 15-16) | Cited in summary as Bakhshalizadeh 2023 DOI: **10.1007/s00439-023-02563-z** |
| **DAP3 / MRPS29** | Mitoribosomal small-subunit protein / GTPase-related apoptosis factor; mitochondrion | **Expanded-spectrum / candidate** | Five unrelated individuals with bi-allelic **DAP3** variants had phenotypes ranging from classic Perrault syndrome (SNHL + ovarian insufficiency) to childhood neurometabolic disease; fibroblasts showed reduced MRPS29 and combined complex I/IV deficiency (smith2025biallelicvariantsin pages 1-2, smith2025biallelicvariantsin pages 15-16) | Smith 2025 DOI: **10.1016/j.ajhg.2024.11.007** |
| **MRPL43** | Mitochondrial ribosomal large-subunit protein; mitoribosome | **Possible emerging association only** | Listed by Open Targets disease-target mapping for Perrault syndrome, but no supporting primary paper was retrieved in the present evidence set (OpenTargets Search: Perrault syndrome) | No primary source retrieved here |
| **MRPL49** | Mitochondrial ribosomal large-subunit protein; mitoribosome | **Possible emerging association only** | Listed by Open Targets disease-target mapping for Perrault syndrome, but no supporting primary paper was retrieved in the present evidence set (OpenTargets Search: Perrault syndrome) | No primary source retrieved here |


*Table: This table separates the 2022 eight-gene core Perrault syndrome set from expanded-spectrum and candidate genes supported by later mitochondrial/peroxisomal studies. It is useful for knowledge-base curation because it links each gene to its molecular role, evidence tier, representative phenotype evidence, and source citations.*

### Variant characteristics

The reported disease alleles include missense, nonsense, frameshift, splice-site, small indel, and large deletion variants. Examples include:

* **MRPS7:** compound heterozygous c.373A>T, p.(Lys125*) and c.536G>A, p.(Arg179His). The nonsense allele is predicted to undergo nonsense-mediated decay; structural analysis suggested p.Arg179His disrupts salt bridges and protein stability. (kline2022integralroleof pages 5-8, kline2022integralroleof pages 8-9)
* **RMND1:** compound heterozygous c.583G>A, p.(Gly195Arg) and c.818A>C, p.(Tyr273Ser), classified as likely pathogenic in the reported family; each was seen only in isolated heterozygous individuals in gnomAD. (oziebło2020twonovelpathogenic pages 3-5, oziebło2020twonovelpathogenic pages 1-3)
* **PRORP:** biallelic missense, duplication/frameshift and other alleles caused reduced protein, impaired mt-tRNA processing and downstream mitochondrial protein deficiency. (hochberg2021biallelicvariantsin pages 1-2)
* **CLPP:** both missense and truncating/splice/deletion alleles occur. Functional consequences include reduced or absent protease activity and failure of mitochondrial protein-quality control. (key2024clppnulleukaryoteswith pages 1-2, key2022clppdepletioncauses pages 1-2)

Exact gnomAD frequencies must be recorded per genomic build, transcript and variant; they should not be inferred from case reports. Pathogenic variants are expected to be absent or very rare and compatible with recessive disease. Variant interpretation should follow ACMG/AMP criteria using segregation, population frequency, phenotype specificity, computational/structural evidence and functional data. No validated somatic mechanism, repeat expansion, recurrent aneuploidy, or characteristic balanced translocation is known.

### Modifier and epigenetic information

No confirmed modifier gene or protective allele has been established. No reproducible disease-specific DNA-methylation episignature, histone signature, or chromatin abnormality is currently used diagnostically. Model findings of histone H3 cleavage and altered one-carbon metabolism are mechanistic observations, not a validated human epigenetic biomarker. (key2024clppnulleukaryoteswith pages 1-2, key2022clppdepletioncauses pages 1-2)

---

## 5. Environmental information

Perrault syndrome is not infectious, toxic, occupational, radiation induced, or lifestyle caused. No pathogen or zoonotic mechanism applies. General measures such as avoiding ototoxic exposure and optimizing nutrition may protect residual function or general health but do not prevent the inherited disorder. No Perrault-specific evidence links tobacco, alcohol, exercise, pollution, or diet to penetrance.

---

## 6. Mechanism and pathophysiology

### Unifying causal chain

**Biallelic germline variant → impaired mitochondrial/peroxisomal protein function → defective mtRNA processing, mitoribosome assembly/translation, mtDNA maintenance, proteostasis, lipid/fatty-acid metabolism, or peroxisome biogenesis → impaired oxidative phosphorylation and cellular stress → selective vulnerability of cochlear auditory cells/neurons and ovarian germ/follicular cells → SNHL and ovarian insufficiency; greater residual dysfunction produces neurologic, renal, muscular, hepatic, cardiac, or developmental disease.** (kline2022integralroleof pages 1-2, smith2025biallelicvariantsin pages 1-2, hochberg2021biallelicvariantsin pages 1-2)

### Upstream molecular modules

1. **Mitochondrial translation and mitoribosome assembly:** HARS2 and LARS2 aminoacylate mitochondrial tRNAs; ERAL1 supports 12S-rRNA/small-subunit assembly; MRPS7, MRPL50 and DAP3 are mitoribosomal proteins; RMND1 supports mitochondrial translation near the inner membrane. Deficiency decreases synthesis of the 13 mtDNA-encoded oxidative-phosphorylation subunits. (smith2025biallelicvariantsin pages 1-2, kline2022integralroleof pages 1-2, oziebło2020twonovelpathogenic pages 1-3)
2. **mtRNA processing:** PRORP is the metallonuclease subunit of mitochondrial RNase P and processes mitochondrial precursor-tRNA 5′ ends. Patient fibroblasts accumulated unprocessed transcripts and lost mitochondrial-encoded proteins; wild-type cDNA rescued these defects. (hochberg2021biallelicvariantsin pages 1-2)
3. **mtDNA maintenance:** TWNK helicase and TFAM support mtDNA replication, packaging and transcription.
4. **Proteostasis:** CLPP is the proteolytic component of the mitochondrial CLPXP complex. Its loss causes CLPX and nucleoid-associated protein accumulation, mtDNA/protein mispackaging, stress signaling and metabolic disruption. (key2024clppnulleukaryoteswith pages 1-2, key2022clppdepletioncauses pages 1-2)
5. **Peroxisomal/metabolic pathways:** HSD17B4 affects peroxisomal fatty-acid oxidation/steroid metabolism; PEX6 affects peroxisome biogenesis; GGPS1 affects isoprenoid/lipid metabolism. These findings show that Perrault is a convergent phenotype, not a single-pathway disorder. (kline2022integralroleof pages 1-2, tucker2020genomicsequencinghighlights pages 1-7)

### Downstream processes and tissue injury

Downstream mechanisms include combined respiratory-chain deficiency, ATP limitation, altered redox and metabolite homeostasis, mitochondrial stress, inappropriate apoptosis or altered apoptotic sensitivity, and—in CLPP models—mtDNA extrusion and cGAS–STING-related innate signaling. Deleting downstream STING/IFNAR did not rescue CLPP-null mouse infertility, indicating that inflammatory signaling is not the sole upstream driver. (smith2025biallelicvariantsin pages 1-2, key2022clppdepletioncauses pages 1-2)

### Molecular profiling and recent research

* **Proteomics/transcriptomics:** CLPP-null testis showed loss of meiotic proteins HSPA2, SHCBP1L, DMRT7 and HSF5, accumulation of AURKAIP1 and Perrault proteins ERAL1, PEO1/TWNK and HARS2, and no meiotic M-phase cells. (key2022clppdepletioncauses pages 1-2)
* **Metabolomics, 2024:** CLPP-null *Podospora anserina* and mouse cerebellum showed reduced arginine/histidine; mouse cerebellum additionally had reduced citrulline and accumulated protoporphyrin IX, supporting dysregulated CLPX–ALAS/OAT and heme/amino-acid metabolism. Translation to patients is unproven. Publication: 19 February 2024; DOI: https://doi.org/10.3390/biom14020241. (key2024clppnulleukaryoteswith pages 1-2)
* **Functional genomics, late 2024:** five unrelated individuals with biallelic DAP3 variants ranged from classic Perrault syndrome to childhood neurometabolic disease. Fibroblasts showed reduced MRPS29/DAP3, destabilization of the small mitoribosomal subunit and combined complex I/IV deficiency; wild-type DAP3 partially rescued molecular defects. Online publication was in December 2024; issue date 2 January 2025; DOI: https://doi.org/10.1016/j.ajhg.2024.11.007. (smith2025biallelicvariantsin pages 1-2)
* No mature Perrault-specific single-cell atlas, spatial-transcriptomic study, patient multi-omics classifier, CRISPR screen, proteomic diagnostic or metabolomic diagnostic was identified. The 2022 review did examine single-cell RNA-seq expression patterns for the eight core genes, but this remains mechanistic rather than diagnostic evidence. (faridi2022newinsightsinto pages 1-3)

### Suggested GO and Cell Ontology annotations

* GO biological processes: **mitochondrial translation (GO:0032543)**; **mitochondrial RNA processing (GO:0000963)**; **mitochondrial DNA replication (GO:0006264/mitochondrial child term)**; **protein quality control**; **oxidative phosphorylation (GO:0006119)**; **peroxisome organization (GO:0007031)**; **fatty-acid beta-oxidation (GO:0006635)**; **apoptotic process (GO:0006915)**; **meiotic cell cycle (GO:0051321)**.
* GO cellular components: **mitochondrion (GO:0005739)**; **mitochondrial matrix (GO:0005759)**; **mitochondrial inner membrane (GO:0005743)**; **mitochondrial ribosome (GO:0005761)**; **peroxisome (GO:0005777)**; **mitochondrial nucleoid (GO:0042645)**.
* Candidate CL terms: cochlear inner/outer hair cell, auditory neuron/spiral-ganglion neuron, ovarian granulosa cell, oocyte, germ cell, spermatocyte, renal tubular epithelial cell, cerebellar Purkinje cell and peripheral neuron. Exact current CL identifiers should be validated against the ontology release before loading.

---

## 7. Anatomical structures affected

### Primary anatomy

* **Inner ear/auditory system:** bilateral cochlear sensory epithelium, hair-cell synapses, auditory nerve/spiral ganglion; auditory neuropathy indicates that pre- or postsynaptic neural components can also be involved. Suggested UBERON: inner ear, cochlea, organ of Corti, vestibulocochlear nerve.
* **Ovary/reproductive axis:** ovaries, ovarian follicles/germ cells and secondary estrogen-dependent tissues. The endocrine defect is peripheral ovarian failure, not primarily pituitary disease. Suggested UBERON: ovary, ovarian follicle, uterus.

### Secondary/genotype-specific anatomy

Cerebellum, cerebral white matter, peripheral nerves, skeletal muscle, kidneys, liver, heart and testes can be involved. MRI may show leukodystrophy or cerebellar atrophy; kidney disease is particularly important in RMND1 or severe mitochondrial-ribosomal phenotypes. (oziebło2020twonovelpathogenic pages 1-3, forli2021ararecase pages 1-2)

### Localization and lateralization

Hearing impairment is characteristically **bilateral**, although severity can be asymmetric. Ovarian involvement is generally bilateral/systemic. Subcellular compartments are predominantly the mitochondrial matrix, inner membrane, mitoribosome, mtRNA-processing machinery and nucleoid; HSD17B4/PEX6 disease additionally implicates peroxisomes.

---

## 8. Temporal development

SNHL is often the first recognized feature and may be congenital, detected in childhood, or appear later. It may be stable or progressive. A CLPP case passed newborn otoacoustic-emission and automated auditory-brainstem screening but later developed progressive auditory neuropathy, showing that a normal newborn screen does not exclude Perrault syndrome. (forli2021ararecase pages 1-2)

Ovarian dysfunction is biologically developmental but often becomes clinically apparent at puberty through delayed/absent pubertal development and primary amenorrhea, or later through irregular menses, secondary amenorrhea and infertility. Neurologic disease can emerge later and progress. In one RMND1 family, hearing loss was diagnosed at ages 3–4, reproductive abnormalities at 17–18, and chronic kidney disease in the fourth decade. (oziebło2020twonovelpathogenic pages 1-3)

The condition is chronic and lifelong. There is no recognized spontaneous or treatment-induced molecular remission. Critical intervention windows include early hearing/language rehabilitation, prepubertal or early-pubertal endocrine evaluation, timely sex-steroid replacement, fertility preservation discussion before follicular reserve is exhausted, and early surveillance for genotype-specific organ disease.

---

## 9. Inheritance and population

### Epidemiology

Perrault syndrome is extremely rare, but no reliable population prevalence, incidence per 100,000, mortality rate, carrier frequency, or sex ratio has been established. Published evidence consists predominantly of small pedigrees and selected sequencing cohorts. Therefore, disease burden cannot responsibly be extrapolated from the gene-specific CLPP series or from the proportion of molecularly unresolved cases.

### Inheritance characteristics

* **Autosomal recessive**, with sex-influenced reproductive expression.
* Penetrance of the defining phenotype appears high in reported biallelic cases, but precise age-adjusted penetrance is unknown.
* Expressivity is markedly variable both across and within genes.
* No anticipation has been reported.
* Germline mosaicism is theoretically possible but not established as a recurrent mechanism.
* Founder alleles may exist in particular pedigrees/populations, but no single global founder mutation explains the disease.
* Consanguinity is relevant to homozygous cases; compound heterozygosity is also common.
* There is no known endemic region or established ethnicity-specific prevalence. Apparent geographic clustering reflects ascertainment and consanguinity more than proven population risk.

---

## 10. Diagnostics

### Clinical recognition

Perrault syndrome should be considered in:

1. any 46,XX person with SNHL plus delayed puberty, amenorrhea, hypergonadotropic hypogonadism, small/streak ovaries or infertility;
2. siblings of either sex with unexplained bilateral SNHL when a sister has ovarian insufficiency;
3. SNHL plus ataxia, neuropathy, leukodystrophy, renal disease or other mitochondrial signs.

### Clinical testing

* **Audiology:** pure-tone audiometry, tympanometry, otoacoustic emissions, auditory brainstem responses and speech testing; evaluate auditory neuropathy and progression.
* **Endocrine/reproductive:** FSH, LH, estradiol, anti-Müllerian hormone where informative; menstrual and pubertal assessment; pelvic ultrasound for uterine/ovarian size; karyotype to document 46,XX and exclude sex-chromosome causes.
* **Neurology:** examination, nerve-conduction/EMG studies where indicated, brain MRI for white-matter or cerebellar abnormalities.
* **Organ surveillance:** creatinine/eGFR, urinalysis and blood pressure; liver enzymes, lactate, glucose, CK, cardiac assessment and ophthalmology guided by genotype/phenotype.
* **Biopsy:** muscle biopsy may show mitochondrial pathology but is not required when molecular diagnosis is obtained and should not be routine.

### Genetic-testing strategy

1. Use a comprehensive **hearing-loss/POI/mitochondrial-peroxisomal panel** that includes at minimum the eight core genes and validated expanded-spectrum genes.
2. If negative, proceed to trio **WES or WGS** with copy-number and mitochondrial-disease-aware analysis. WGS is advantageous for exon-level/large deletions, noncoding splice variants and structural variants.
3. Confirm candidate variants and phase by parental testing/Sanger or equivalent methods.
4. Apply RNA studies/minigene assays for splice variants and functional studies where gene–disease validity or variant interpretation is uncertain.
5. CMA/karyotype is useful principally for differential diagnosis of POI or syndromic disease, not as the highest-yield test for classic Perrault syndrome. FISH and repeat-expansion testing are not routine. mtDNA sequencing may be warranted for broader mitochondrial differentials, but classic Perrault genes are nuclear encoded.

A real-world 237-gene hearing-loss panel successfully identified compound-heterozygous RMND1 variants after analysis against gnomAD, ClinVar, HGMD and ACMG/AMP criteria. (oziebło2020twonovelpathogenic pages 3-5, oziebło2020twonovelpathogenic pages 1-3)

### Differential diagnosis

Important alternatives include nonsyndromic hereditary deafness coinciding with unrelated POI; Turner syndrome or X-chromosome abnormalities; FMR1 premutation-associated POI; autoimmune or iatrogenic POI; congenital infection; ototoxic injury; Zellweger-spectrum/D-bifunctional protein deficiency; combined oxidative-phosphorylation disorders; Woodhouse–Sakati syndrome; Gordon Holmes/Boucher–Neuhäuser and other ataxia-hypogonadism syndromes; and syndromic hearing-loss disorders such as Alström or mitochondrial cytopathies. The possibility of **two independent monogenic diagnoses** should be retained when phenotype or segregation is discordant. (faridi2022newinsightsinto pages 11-13)

### Screening

Perrault syndrome is not on routine newborn biochemical screening panels. Universal newborn hearing screening can detect congenital disease but can miss later-onset/progressive auditory neuropathy. Cascade testing of relatives is appropriate after molecular diagnosis. Reproductive options include carrier testing, prenatal diagnosis and preimplantation genetic testing for a known familial genotype.

---

## 11. Outcome and prognosis

There are no robust 5- or 10-year survival estimates or disease-specific mortality rates. Classic type 1 disease is not generally considered life-shortening, but morbidity from deafness, infertility, estrogen deficiency and osteoporosis is important. Severe alleles in RMND1, MRPS7, DAP3 and other mitochondrial genes can cause renal/hepatic failure, cardiomyopathy, encephalopathy or early death; thus prognosis is genotype- and residual-function dependent. One previously reported MRPS7-affected sister died in early adolescence from liver and renal failure, illustrating the expanded spectrum rather than the expected course of every patient. (kline2022integralroleof pages 8-9, kline2022integralroleof pages 1-2)

Hearing loss generally does not spontaneously recover, although assistive technology can substantially improve communication. Ovarian reserve is not restored by hormone replacement; spontaneous ovarian activity may occur in POI generally, but no Perrault-specific recovery rate is known. Neurologic progression is variable. Prognostic biomarkers beyond genotype, baseline organ involvement and longitudinal audiologic/endocrine measures are not validated.

---

## 12. Treatment and real-world implementation

### Hearing management

Early hearing aids, speech/language therapy, educational support and sign-language access should be offered according to patient preference and auditory phenotype. Cochlear implantation is appropriate for severe/profound loss or poor aided speech recognition, including selected auditory-neuropathy cases. In RMND1-associated disease, bilateral implantation at ages 34 and 36 produced a reported “good outcome.” (oziebło2020twonovelpathogenic pages 1-3)

Suggested NCIt concepts: **Hearing Aid**, **Cochlear Implantation**, **Speech Therapy**, **Rehabilitation Therapy**.

### Endocrine, bone and reproductive care

Physiologic estrogen replacement with cyclic progestogen when a uterus is present supports pubertal development, menstrual management, bone health and cardiovascular/urogenital health. Monitor bone mineral density, vitamin D/calcium status and cardiovascular risk. In the RMND1 family, both affected sisters received estradiol plus dydrogesterone; one had osteoporosis. (oziebło2020twonovelpathogenic pages 1-3)

Fertility counseling should occur early. Depending on residual ovarian function, options may include fertility preservation, assisted reproduction, donor oocytes/embryos, gestational or adoption pathways consistent with local law and patient goals. No genotype-specific response rate is available.

Suggested NCIt concepts: **Hormone Replacement Therapy**, **Estradiol**, **Progesterone**, **In Vitro Fertilization**, **Oocyte Donation**, **Fertility Preservation Procedure**.

### Neurologic and multisystem management

Physical/occupational therapy, mobility aids, seizure treatment, neuropathy management and educational support are individualized. Genotype-directed renal, hepatic, cardiac and metabolic surveillance is essential. There is no established Perrault pharmacogenomic rule or approved mitochondrial cocktail.

### Advanced/experimental therapies and trials

No approved gene replacement, CRISPR, cell therapy, antisense/siRNA, mRNA or targeted small-molecule therapy exists. The clinical-trial search identified a broad observational deafness genetics study (**NCT00341874**), not a Perrault-specific therapeutic trial. The 2024 arginine/histidine supplementation proposal is preclinical and should not be presented as treatment. No response rates or controlled adverse-event data exist for disease-modifying therapy. (key2024clppnulleukaryoteswith pages 1-2)

---

## 13. Prevention

### Primary prevention

The inherited molecular defect cannot currently be prevented through lifestyle change, vaccination or prophylactic medication. The applicable primary-prevention strategy is reproductive genetic counseling with optional carrier, prenatal or preimplantation testing after familial variants are established.

### Secondary prevention

* Cascade testing and baseline audiology/endocrine evaluation of at-risk siblings.
* Serial hearing assessment despite a normal newborn screen.
* Early FSH/LH/estradiol and pubertal assessment in girls with unexplained SNHL.
* Early fertility counseling before established ovarian failure where feasible.

### Tertiary prevention

Early auditory rehabilitation reduces language/educational consequences; hormone replacement and bone surveillance reduce estrogen-deficiency complications; organ surveillance may identify renal, hepatic, cardiac or neurologic complications before irreversible decline. No vaccine, antimicrobial prophylaxis, public-health sanitation measure or environmental remediation is disease-specific.

---

## 14. Other species and natural disease

There is no evidence that Perrault syndrome is transmissible, zoonotic or infectious. Orthologs of the causal genes are broadly conserved across eukaryotes, particularly genes governing mitochondrial translation and CLP proteostasis. Relevant experimental taxa include:

* **Mus musculus**, NCBI Taxon **10090**—CLPP-null and other engineered models.
* **Podospora anserina**, a filamentous ascomycete—CLPP-null comparative aging/metabolism model.
* Human patient fibroblasts and recombinant-protein systems.

No well-established naturally occurring companion-animal breed syndrome equivalent to human Perrault syndrome was identified in the retrieved literature. Veterinary breed/VBO annotations and natural-disease transmission are therefore not applicable on current evidence.

---

## 15. Model organisms and experimental systems

### CLPP-null mouse

CLPP loss in mice reproduces growth deficits, infertility, deafness and ataxia, providing a strong multisystem model of PRLTS3. In male testis, chromosome pairing occurred, but crossover-marker abnormalities, persistent γH2AX, premature desynapsis, absence of meiotic M-phase cells and cell death indicated late-prophase/diplotene arrest. mtDNA extrusion and cGAMP increased, but STING/IFNAR deletion failed to rescue pathology. Strengths are organism-level auditory, neurologic and reproductive phenotypes; limitations include especially severe male infertility and incomplete correspondence to variable human alleles. (key2022clppdepletioncauses pages 1-2)

### Fungal CLPP-null model

*P. anserina* CLPP loss produces longevity rather than the mammalian syndrome, but provides experimentally tractable proteomic/metabolomic evidence concerning CLPX, ALAS/OAT, heme synthesis and arginine/histidine depletion. It is useful for conserved mitochondrial proteostasis, not for human ovarian or auditory anatomy. (key2024clppnulleukaryoteswith pages 1-2)

### Patient fibroblasts and rescue systems

PRORP patient fibroblasts demonstrated accumulated unprocessed mitochondrial transcripts and reduced mitochondrial proteins, rescued by wild-type PRORP cDNA. Recombinant RNase-P assays confirmed diminished tRNA processing. These systems strongly establish variant mechanism but cannot reproduce tissue-selective ovarian or cochlear degeneration. (hochberg2021biallelicvariantsin pages 1-2)

DAP3 patient fibroblasts and recombinant-protein assays showed reduced mitoribosomal small-subunit assembly, complex I/IV deficiency, altered thermal stability/GTPase function and altered apoptotic sensitivity; wild-type DAP3 partly rescued molecular abnormalities. This is compelling functional evidence for an emerging Perrault-spectrum gene but needs larger cohorts and longitudinal phenotype data. (smith2025biallelicvariantsin pages 1-2)

No mature Perrault-specific organoid, humanized knock-in, spatial-transcriptomic, or therapeutic CRISPR model was identified.

---

## Key recent developments, 2023–2024

1. **Mitoribosomal expansion:** a 2023 report implicated **MRPL50** deficiency in the Perrault spectrum, strengthening the view that both large and small mitoribosomal subunits are critical to ovarian and auditory function; detailed primary evidence should be independently curated before assigning definitive status. DOI: https://doi.org/10.1007/s00439-023-02563-z. (smith2025biallelicvariantsin pages 15-16)
2. **CLPP meiotic mechanism:** the 2023 *Cells* study localized CLPP-null germ-cell failure to late meiotic prophase and showed that downstream STING/IFNAR removal did not rescue infertility. DOI: https://doi.org/10.3390/cells12010052. (key2022clppdepletioncauses pages 1-2)
3. **CLPP metabolic mechanism, 2024:** cross-species metabolomics linked CLPP loss to altered heme biosynthesis and reduced arginine/histidine/citrulline, generating a testable—but not yet clinical—nutritional hypothesis. DOI: https://doi.org/10.3390/biom14020241. (key2024clppnulleukaryoteswith pages 1-2)
4. **DAP3 discovery, December 2024:** biallelic DAP3 variants in five unrelated individuals established a mitoribosomal-small-subunit/combined-OXPHOS Perrault-spectrum disorder through genetic, proteomic, rescue and biochemical evidence. DOI: https://doi.org/10.1016/j.ajhg.2024.11.007. (smith2025biallelicvariantsin pages 1-2)

---

## Selected exact abstract quotations and source metadata

* Faridi et al., accepted 14 July 2021; *Human Genetics* 2022: “Variants of these eight genes only account for approximately half of the individuals with clinical features of Perrault syndrome where the molecular genetic base remains under investigation.” DOI: https://doi.org/10.1007/s00439-021-02319-7. (faridi2022newinsightsinto pages 1-3)
* Kline et al., published 14 November 2022: “This second independent report validates that variants in MRPS7 are a cause of syndromic POI/Perrault syndrome.” DOI: https://doi.org/10.3390/genes13112113. (kline2022integralroleof pages 1-2)
* Hochberg et al., published 4 November 2021: “Fibroblasts from affected individuals in two families demonstrated decreased steady state levels of PRORP, an accumulation of unprocessed mitochondrial transcripts, and decreased steady state levels of mitochondrial-encoded proteins, which were rescued by introduction of the wild-type PRORP cDNA.” DOI: https://doi.org/10.1016/j.ajhg.2021.10.002; PMID **34715011**, https://pubmed.ncbi.nlm.nih.gov/34715011/. (hochberg2021biallelicvariantsin pages 1-2)
* Oziębło et al., published 8 September 2020: “Our study presents the mildest, so far reported, RMND1-related phenotype and delivers the first independent confirmation that RMND1 is causally involved in the development of Perrault syndrome with renal involvement.” DOI: https://doi.org/10.3390/genes11091060. (oziebło2020twonovelpathogenic pages 1-3)
* Smith et al., online December 2024/issue 2 January 2025: “Here, we describe five unrelated individuals with bi-allelic variants in death-associated protein 3 (DAP3) … with variable clinical presentations ranging from Perrault syndrome … to an early childhood neurometabolic phenotype.” DOI: https://doi.org/10.1016/j.ajhg.2024.11.007. (smith2025biallelicvariantsin pages 1-2)

## Evidence limitations

The central limitations are extreme rarity, retrospective ascertainment, small pedigrees, inconsistent historical gene lists, incomplete follow-up of 46,XY individuals, and frequent use of “Perrault-like” or “Perrault-spectrum” for broader mitochondrial disorders. Syndrome-wide phenotype percentages, penetrance, prevalence, life expectancy, quality-of-life scores, carrier frequencies, and treatment-response rates are not currently robust. Knowledge-base curation should therefore preserve evidence tier, publication date, exact genotype, sex/karyotype, phenotype age, functional evidence and whether the source represents classic Perrault syndrome or an expanded multisystem spectrum.

References

1. (faridi2022newinsightsinto pages 1-3): Rabia Faridi, Alessandro Rea, Cristina Fenollar-Ferrer, Raymond T. O’Keefe, Shoujun Gu, Zunaira Munir, Asma Ali Khan, Sheikh Riazuddin, Michael Hoa, Sadaf Naz, William G. Newman, and Thomas B. Friedman. New insights into perrault syndrome, a clinically and genetically heterogeneous disorder. Human Genetics, 141:805-819, Aug 2022. URL: https://doi.org/10.1007/s00439-021-02319-7, doi:10.1007/s00439-021-02319-7. This article has 51 citations and is from a peer-reviewed journal.

2. (kline2022integralroleof pages 1-2): Brianna L. Kline, Sylvie Jaillard, Katrina M. Bell, Shabnam Bakhshalizadeh, Gorjana Robevska, Jocelyn van den Bergen, Jérôme Dulon, Katie L. Ayers, John Christodoulou, Michel C. Tchan, Philippe Touraine, Andrew H. Sinclair, and Elena J. Tucker. Integral role of the mitochondrial ribosome in supporting ovarian function: mrps7 variants in syndromic premature ovarian insufficiency. Genes, 13:2113, Nov 2022. URL: https://doi.org/10.3390/genes13112113, doi:10.3390/genes13112113. This article has 18 citations.

3. (smith2025biallelicvariantsin pages 1-2): Thomas B. Smith, Robert Kopajtich, Leigh A.M. Demain, Alessandro Rea, Huw B. Thomas, Manuel Schiff, Christian Beetz, Shelagh Joss, Gerard S. Conway, Anju Shukla, Mayuri Yeole, Periyasamy Radhakrishnan, Hatem Azzouz, Amel Ben Chehida, Monique Elmaleh-Bergès, Ruth I.C. Glasgow, Kyle Thompson, Monika Oláhová, Langping He, Emma M. Jenkinson, Amir Jahic, Inna A. Belyantseva, Melanie Barzik, Jill E. Urquhart, James O’Sullivan, Simon G. Williams, Sanjeev S. Bhaskar, Samantha Carrera, Alexander J.M. Blakes, Siddharth Banka, Wyatt W. Yue, Jamie M. Ellingford, Henry Houlden, Kevin J. Munro, Thomas B. Friedman, Robert W. Taylor, Holger Prokisch, Raymond T. O’Keefe, and William G. Newman. Bi-allelic variants in dap3 result in reduced assembly of the mitoribosomal small subunit with altered apoptosis and a perrault-syndrome-spectrum phenotype. Jan 2025. URL: https://doi.org/10.1016/j.ajhg.2024.11.007, doi:10.1016/j.ajhg.2024.11.007. This article has 11 citations.

4. (faridi2022newinsightsinto pages 11-13): Rabia Faridi, Alessandro Rea, Cristina Fenollar-Ferrer, Raymond T. O’Keefe, Shoujun Gu, Zunaira Munir, Asma Ali Khan, Sheikh Riazuddin, Michael Hoa, Sadaf Naz, William G. Newman, and Thomas B. Friedman. New insights into perrault syndrome, a clinically and genetically heterogeneous disorder. Human Genetics, 141:805-819, Aug 2022. URL: https://doi.org/10.1007/s00439-021-02319-7, doi:10.1007/s00439-021-02319-7. This article has 51 citations and is from a peer-reviewed journal.

5. (oziebło2020twonovelpathogenic pages 1-3): Dominika Oziębło, Joanna Pazik, Iwona Stępniak, Henryk Skarżyński, and Monika Ołdak. Two novel pathogenic variants confirm rmnd1 causative role in perrault syndrome with renal involvement. Genes, 11:1060, Sep 2020. URL: https://doi.org/10.3390/genes11091060, doi:10.3390/genes11091060. This article has 30 citations.

6. (OpenTargets Search: Perrault syndrome): Open Targets Query (Perrault syndrome, 31 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

7. (forli2021ararecase pages 1-2): Francesca Forli, Luca Bruschini, Beatrice Franciosi, Roberta Battini, Gemma Marinella, Stefano Berrettini, and Francesco Lazzerini. A rare case of perrault syndrome with auditory neuropathy spectrum disorder: cochlear implantation treatment and literature review. Audiology Research, 11:609-617, Nov 2021. URL: https://doi.org/10.3390/audiolres11040055, doi:10.3390/audiolres11040055. This article has 13 citations.

8. (hochberg2021biallelicvariantsin pages 1-2): Irit Hochberg, Leigh A.M. Demain, Julie Richer, Kyle Thompson, Jill E. Urquhart, Alessandro Rea, Waheeda Pagarkar, Agustí Rodríguez-Palmero, Agatha Schlüter, Edgard Verdura, Aurora Pujol, Pilar Quijada-Fraile, Albert Amberger, Andrea J. Deutschmann, Sandra Demetz, Meredith Gillespie, Inna A. Belyantseva, Hugh J. McMillan, Melanie Barzik, Glenda M. Beaman, Reeya Motha, Kah Ying Ng, James O’Sullivan, Simon G. Williams, Sanjeev S. Bhaskar, Isabella R. Lawrence, Emma M. Jenkinson, Jessica L. Zambonin, Zeev Blumenfeld, Sergey Yalonetsky, Stephanie Oerum, Walter Rossmanith, Wyatt W. Yue, Johannes Zschocke, Kevin J. Munro, Brendan J. Battersby, Thomas B. Friedman, Robert W. Taylor, Raymond T. O’Keefe, and William G. Newman. Bi-allelic variants in the mitochondrial rnase p subunit prorp cause mitochondrial trna processing defects and pleiotropic multisystem presentations. The American Journal of Human Genetics, 108:2195-2204, Nov 2021. URL: https://doi.org/10.1016/j.ajhg.2021.10.002, doi:10.1016/j.ajhg.2021.10.002. This article has 53 citations.

9. (kline2022integralroleof pages 8-9): Brianna L. Kline, Sylvie Jaillard, Katrina M. Bell, Shabnam Bakhshalizadeh, Gorjana Robevska, Jocelyn van den Bergen, Jérôme Dulon, Katie L. Ayers, John Christodoulou, Michel C. Tchan, Philippe Touraine, Andrew H. Sinclair, and Elena J. Tucker. Integral role of the mitochondrial ribosome in supporting ovarian function: mrps7 variants in syndromic premature ovarian insufficiency. Genes, 13:2113, Nov 2022. URL: https://doi.org/10.3390/genes13112113, doi:10.3390/genes13112113. This article has 18 citations.

10. (key2024clppnulleukaryoteswith pages 1-2): Jana Key, Suzana Gispert, Arvind Reddy Kandi, Daniela Heinz, Andrea Hamann, Heinz D. Osiewacz, David Meierhofer, and Georg Auburger. Clpp-null eukaryotes with excess heme biosynthesis show reduced l-arginine levels, probably via clpx-mediated oat activation. Biomolecules, 14:241, Feb 2024. URL: https://doi.org/10.3390/biom14020241, doi:10.3390/biom14020241. This article has 4 citations.

11. (key2022clppdepletioncauses pages 1-2): Jana Key, Suzana Gispert, Lieke Koornneef, Esther Sleddens-Linkels, Aneesha Kohli, Sylvia Torres-Odio, Gabriele Koepf, Shady Amr, Marina Reichlmeir, Patrick N. Harter, Andrew Phillip West, Christian Münch, Willy M. Baarends, and Georg Auburger. Clpp depletion causes diplotene arrest; underlying testis mitochondrial dysfunction occurs with accumulation of perrault proteins eral1, peo1, and hars2. Cells, 12:52, Dec 2022. URL: https://doi.org/10.3390/cells12010052, doi:10.3390/cells12010052. This article has 15 citations.

12. (tucker2020genomicsequencinghighlights pages 1-7): Elena J. Tucker, Rocio Rius, Sylvie Jaillard, Katrina Bell, Phillipa J. Lamont, André Travessa, Juliette Dupont, Lurdes Sampaio, Jérôme Dulon, Sandrine Vuillaumier-Barrot, Sandra Whalen, Arnaud Isapof, Tanya Stojkovic, Susana Quijano-Roy, Gorjana Robevska, Jocelyn van den Bergen, Chloe Hanna, Andrea Simpson, Katie Ayers, David R. Thorburn, John Christodoulou, Philippe Touraine, and Andrew H. Sinclair. Genomic sequencing highlights the diverse molecular causes of perrault syndrome: a peroxisomal disorder (pex6), metabolic disorders (clpp, ggps1), and mtdna maintenance/translation disorders (lars2, tfam). Human Genetics, 139:1325-1343, May 2020. URL: https://doi.org/10.1007/s00439-020-02176-w, doi:10.1007/s00439-020-02176-w. This article has 48 citations and is from a peer-reviewed journal.

13. (oziebło2020twonovelpathogenic pages 3-5): Dominika Oziębło, Joanna Pazik, Iwona Stępniak, Henryk Skarżyński, and Monika Ołdak. Two novel pathogenic variants confirm rmnd1 causative role in perrault syndrome with renal involvement. Genes, 11:1060, Sep 2020. URL: https://doi.org/10.3390/genes11091060, doi:10.3390/genes11091060. This article has 30 citations.

14. (kline2022integralroleof pages 5-8): Brianna L. Kline, Sylvie Jaillard, Katrina M. Bell, Shabnam Bakhshalizadeh, Gorjana Robevska, Jocelyn van den Bergen, Jérôme Dulon, Katie L. Ayers, John Christodoulou, Michel C. Tchan, Philippe Touraine, Andrew H. Sinclair, and Elena J. Tucker. Integral role of the mitochondrial ribosome in supporting ovarian function: mrps7 variants in syndromic premature ovarian insufficiency. Genes, 13:2113, Nov 2022. URL: https://doi.org/10.3390/genes13112113, doi:10.3390/genes13112113. This article has 18 citations.

15. (smith2025biallelicvariantsin pages 15-16): Thomas B. Smith, Robert Kopajtich, Leigh A.M. Demain, Alessandro Rea, Huw B. Thomas, Manuel Schiff, Christian Beetz, Shelagh Joss, Gerard S. Conway, Anju Shukla, Mayuri Yeole, Periyasamy Radhakrishnan, Hatem Azzouz, Amel Ben Chehida, Monique Elmaleh-Bergès, Ruth I.C. Glasgow, Kyle Thompson, Monika Oláhová, Langping He, Emma M. Jenkinson, Amir Jahic, Inna A. Belyantseva, Melanie Barzik, Jill E. Urquhart, James O’Sullivan, Simon G. Williams, Sanjeev S. Bhaskar, Samantha Carrera, Alexander J.M. Blakes, Siddharth Banka, Wyatt W. Yue, Jamie M. Ellingford, Henry Houlden, Kevin J. Munro, Thomas B. Friedman, Robert W. Taylor, Holger Prokisch, Raymond T. O’Keefe, and William G. Newman. Bi-allelic variants in dap3 result in reduced assembly of the mitoribosomal small subunit with altered apoptosis and a perrault-syndrome-spectrum phenotype. Jan 2025. URL: https://doi.org/10.1016/j.ajhg.2024.11.007, doi:10.1016/j.ajhg.2024.11.007. This article has 11 citations.

## Artifacts

- [Edison artifact artifact-00](Perrault_Syndrome-deep-research-falcon_artifacts/artifact-00.md)