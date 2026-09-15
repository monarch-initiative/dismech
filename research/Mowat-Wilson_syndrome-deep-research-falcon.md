---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-30T17:46:58.665891'
end_time: '2026-07-30T18:01:07.384927'
duration_seconds: 848.72
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Mowat-Wilson syndrome
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
  path: Mowat-Wilson_syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Mowat-Wilson syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Mowat-Wilson syndrome** covering all of the
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

For each treatment, suggest MAXO (Medical Action Ontology) terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, MAXO, MONDO) where applicable
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
- Treatment annotations (MAXO terms)
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
- **Disease Name:** Mowat-Wilson syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Mowat-Wilson syndrome** covering all of the
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

For each treatment, suggest MAXO (Medical Action Ontology) terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, MAXO, MONDO) where applicable
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
- Treatment annotations (MAXO terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


# Mowat–Wilson syndrome: comprehensive disease-characteristics report

## Executive summary

Mowat–Wilson syndrome (MOWS) is a congenital, lifelong, multisystem Mendelian neurodevelopmental disorder caused primarily by heterozygous loss of function of **ZEB2** at chromosome 2q22.3. Its defining pattern combines moderate-to-profound intellectual disability and severe speech impairment with a recognizable facial gestalt, delayed motor development, frequent epilepsy, and variably penetrant congenital anomalies—especially Hirschsprung disease, congenital heart disease, genitourinary abnormalities, and malformations of the corpus callosum or hippocampus. The estimated prevalence is approximately 1 per 50,000–70,000 live births, although underdiagnosis is likely. Most cases are sporadic and de novo; inheritance is formally autosomal dominant. (zou2020genotypephenotypeanalysisin pages 1-2, birkhoff2021zeb2themowatwilson pages 1-2, peter2024mowat–wilsonsyndromecase pages 1-2)

The most important recent development is the 2024 discovery of a highly reproducible blood DNA-methylation episignature. In 29 molecularly confirmed individuals, investigators identified 296 differentially methylated probes, 98.6% hypomethylated, and separated MOWS from controls and 56 other neurodevelopmental-disorder episignatures. This is a promising functional diagnostic adjunct for atypical phenotypes and uncertain ZEB2 variants, but not a population-screening test. (giuseppe2024identificationofthe pages 5-6, giuseppe2024identificationofthe pages 1-2, giuseppe2024identificationofthe pages 2-2)

No approved disease-modifying, gene, cell, or RNA therapy was identified. Present implementation is multidisciplinary supportive care, developmental rehabilitation, antiseizure treatment, nutritional support, and surgical correction of Hirschsprung disease and congenital anomalies.

The following compact table provides a knowledge-base-oriented synopsis.

| Domain | Core finding / statistic | Suggested ontology terms | Evidence type | Key source / date / DOI |
|---|---|---|---|---|
| Identifiers / definition | Mowat-Wilson syndrome is a rare congenital neurodevelopmental disorder caused by heterozygous ZEB2 haploinsufficiency; prevalence commonly cited at ~1:50,000–70,000 live births; OMIM disease identifier: **OMIM #235730**; causal gene: **ZEB2** at 2q22.3, **OMIM *605802** (zou2020genotypephenotypeanalysisin pages 1-2, birkhoff2021zeb2themowatwilson pages 1-2) | MONDO: Mowat-Wilson syndrome; HPO: Intellectual disability, Seizure, Hirschsprung disease, Corpus callosum agenesis | Human clinical + review | Zou et al., 2020, Exp Ther Med, Oct 2020, https://doi.org/10.3892/etm.2020.9393; Birkhoff et al., 2021, Genes, Jul 2021, https://doi.org/10.3390/genes12071037 |
| Inheritance / recurrence | Inheritance is **autosomal dominant**, but most reported cases are **de novo** heterozygous loss-of-function variants; recurrence risk is generally low but not zero because parental germline mosaicism is possible in principle (direct recurrence data limited in retrieved evidence) (zou2020genotypephenotypeanalysisin pages 1-2, peter2024mowat–wilsonsyndromecase pages 1-2) | HPO: De novo mutation; autosomal dominant inheritance | Human clinical + review | Zou et al., 2020, https://doi.org/10.3892/etm.2020.9393; Peter et al., 2024, Feb 2024, https://doi.org/10.3390/ijms25052838 |
| ZEB2 genetics / variant spectrum | >220 pathogenic ZEB2 variants had been identified by 2020; a 2024 review compiled **298 patients** and found **exon 8 accounted for 66% (198/298)** of variants; **>90%** were **nonsense or frameshift**; the recurrent **c.2083C>T** variant represented **11%** of 298 reported patients (zou2020genotypephenotypeanalysisin pages 1-2, peter2024mowat–wilsonsyndromecase pages 1-2, peter2024mowat–wilsonsyndromecase pages 4-5) | HGNC: ZEB2; Sequence ontology labels: nonsense, frameshift, missense, splice-site, deletion | Human aggregated genetic evidence | Peter et al., 2024, Int J Mol Sci, Feb 2024, https://doi.org/10.3390/ijms25052838; Zou et al., 2020, https://doi.org/10.3892/etm.2020.9393 |
| Functional consequence | Disease mechanism is predominantly **loss of function / haploinsufficiency** of a SMAD-binding transcription factor with roles in transcriptional repression/activation, chromatin regulation, neural crest development, and neurodevelopment (zou2020genotypephenotypeanalysisin pages 1-2, giuseppe2024identificationofthe pages 2-2, putte2007neuralcrestspecificremoval pages 1-2) | GO: transcription regulation; neural crest cell migration; TGF-beta/BMP signaling | Human genetic + animal/model mechanistic | Caraffi et al., 2024, Eur J Hum Genet, Feb 2024, https://doi.org/10.1038/s41431-024-01548-4; van de Putte et al., 2007, Jun 2007, https://doi.org/10.1093/hmg/ddm093 |
| Major neurodevelopmental phenotype | Core phenotype includes **moderate-to-severe intellectual disability** with severe speech impairment and delayed motor milestones; mean walking age reported as about **4 years** in aggregate review data (peter2024mowat–wilsonsyndromecase pages 1-2, zou2020genotypephenotypeanalysisin pages 3-5) | HPO: Global developmental delay; Intellectual disability; Delayed walking; Speech delay | Human clinical + review | Peter et al., 2024, https://doi.org/10.3390/ijms25052838; Zou et al., 2020, https://doi.org/10.3892/etm.2020.9393 |
| Epilepsy / EEG | Seizures or abnormal EEG were reported in **84%** in the 2024 aggregate review; epilepsy occurred in **3/4** patients in one 2020 case series, with variable course including spontaneous remission in one child (peter2024mowat–wilsonsyndromecase pages 1-2, zou2020genotypephenotypeanalysisin pages 3-5) | HPO: Seizure; Abnormal EEG | Human clinical + review | Peter et al., 2024, https://doi.org/10.3390/ijms25052838; Zou et al., 2020, https://doi.org/10.3892/etm.2020.9393 |
| Gastrointestinal / enteric phenotype | **Hirschsprung disease affects ~50%** of patients in aggregate estimates; chronic constipation is also common, including patients without proven aganglionosis (peter2024mowat–wilsonsyndromecase pages 1-2, zou2020genotypephenotypeanalysisin pages 3-5, birkhoff2021zeb2themowatwilson pages 2-4) | HPO: Hirschsprung disease; Constipation | Human clinical + review | Peter et al., 2024, https://doi.org/10.3390/ijms25052838; Birkhoff et al., 2021, https://doi.org/10.3390/genes12071037 |
| Cardiac phenotype | Congenital heart disease was reported in **58%** in the 2024 review, supporting routine cardiology assessment (peter2024mowat–wilsonsyndromecase pages 1-2) | HPO: Congenital heart defect | Human aggregated clinical evidence | Peter et al., 2024, Int J Mol Sci, Feb 2024, https://doi.org/10.3390/ijms25052838 |
| Brain / growth / dysmorphism | Frequently reported features include **microcephaly**, corpus callosum and hippocampal anomalies, ventriculomegaly/white matter changes, and distinctive facial gestalt; brain malformations were estimated at about **80%** in review data (peter2024mowat–wilsonsyndromecase pages 1-2, birkhoff2021zeb2themowatwilson pages 2-4) | HPO: Microcephaly; Corpus callosum agenesis; Ventriculomegaly; Hypertelorism; Uplifted earlobe | Human clinical + review | Peter et al., 2024, https://doi.org/10.3390/ijms25052838; Birkhoff et al., 2021, https://doi.org/10.3390/genes12071037 |
| 2024 DNA methylation episignature | A 2024 study analyzed **29** molecularly confirmed cases (discovery **n=24**, validation **n=5**) and identified a **296-probe** episignature; **98.6%** of differentially methylated probes were **hypomethylated**; classifier scores separated all MWS cases from controls and **56 other neurodevelopmental disorder episignatures** (giuseppe2024identificationofthe pages 5-6, giuseppe2024identificationofthe pages 1-2, giuseppe2024identificationofthe pages 2-2) | DNA methylation signature; EpiSign; ZEB2 locus | Human molecular biomarker | Caraffi et al., 2024, Eur J Hum Genet, Feb 2024, https://doi.org/10.1038/s41431-024-01548-4 |
| Diagnostic implications | Diagnosis is primarily established by **molecular testing of ZEB2** using single-gene sequencing, multigene neurodevelopmental panels, exome/genome sequencing, and deletion/duplication analysis; the 2024 episignature provides an additional diagnostic biomarker, especially for uncertain/atypical cases (zou2020genotypephenotypeanalysisin pages 3-5, giuseppe2024identificationofthe pages 5-6, giuseppe2024identificationofthe pages 1-2) | HPO-based phenotyping; DNA methylation signature; sequence analysis; copy-number analysis | Human diagnostic evidence | Zou et al., 2020, https://doi.org/10.3892/etm.2020.9393; Caraffi et al., 2024, https://doi.org/10.1038/s41431-024-01548-4 |
| Management / real-world care | No disease-modifying therapy was identified in retrieved evidence; current care is **supportive and multidisciplinary**, including seizure management, surgery for Hirschsprung disease and congenital anomalies, feeding/nutrition support, developmental therapies, and surveillance for cardiac/GI/GU/neurologic issues (peter2024mowat–wilsonsyndromecase pages 2-4, cordelli2021neurologicalphenotypeof pages 1-2) | MAXO labels: antiseizure medication therapy; surgical correction; gastrostomy feeding support; speech therapy; physical therapy; occupational therapy | Human clinical practice / supportive care | Peter et al., 2024, https://doi.org/10.3390/ijms25052838; Cordelli et al., 2021, Jun 2021, https://doi.org/10.3390/genes12070982 |
| Current study implementation | Retrieved registry evidence showed one disease-specific study: **NCT07476417**, an observational oral-health/dentofacial/OHRQoL study, **not yet recruiting**, planned enrollment **25** | Oral health; quality of life | Observational study registry | ClinicalTrials.gov record NCT07476417 |
| Modifier / variable expressivity | Variable penetrance of Hirschsprung disease suggests modifiers beyond ZEB2. A 2026 preprint proposed a **RET enhancer risk haplotype** as a modifier of HSCR penetrance in MWS; this is promising but **not yet peer-reviewed** (collins2026wholegenomesequencing pages 6-9, collins2026wholegenomesequencing pages 13-19) | RET enhancer haplotype; variable expressivity | Human genomic preprint | Collins et al., medRxiv, Mar 2026, https://doi.org/10.64898/2026.03.19.26348831 |
| Molecular pathways | ZEB2 participates in **TGF-beta/BMP-SMAD** signaling and also modulates **Wnt, Notch, and FGF** pathway components; it can recruit **p300/KAT2B** for activation and CtBP/HDAC-associated repressive machinery for repression (giuseppe2024identificationofthe pages 2-2, cordelli2021neurologicalphenotypeof pages 1-2, birkhoff2021zeb2themowatwilson pages 1-2) | GO: TGF-beta receptor signaling pathway; BMP signaling; Wnt signaling; Notch signaling; neurogenesis | Review + mechanistic synthesis | Caraffi et al., 2024, https://doi.org/10.1038/s41431-024-01548-4; Cordelli et al., 2021, https://doi.org/10.3390/genes12070982; Birkhoff et al., 2021, https://doi.org/10.3390/genes12071037 |
| Cell / tissue systems affected | Major affected systems include **central nervous system**, **enteric nervous system**, **craniofacial neural crest derivatives**, **heart**, and **urogenital tract** (zou2020genotypephenotypeanalysisin pages 1-2, putte2007neuralcrestspecificremoval pages 1-2, cordelli2021neurologicalphenotypeof pages 1-2) | UBERON: brain, heart, intestine; CL: neural crest cell, cortical neuron, GABAergic interneuron, Bergmann glial cell | Human + animal | Zou et al., 2020, https://doi.org/10.3892/etm.2020.9393; van de Putte et al., 2007, https://doi.org/10.1093/hmg/ddm093; Cordelli et al., 2021, https://doi.org/10.3390/genes12070982 |
| Model systems | Useful models include **neural crest-specific conditional mouse knockout**, **cortical conditional knockouts**, **heterozygous Zeb2 mutant mice**, **zebrafish knockdown/perturbation models**, and emerging **patient-derived iPSC systems**; no single model captures the full human phenotype (birkhoff2021zeb2themowatwilson pages 24-25, epifanova2019roleofzeb2sip1 pages 3-4, epifanova2019roleofzeb2sip1 pages 2-3, putte2007neuralcrestspecificremoval pages 1-2, birkhoff2021zeb2themowatwilson pages 2-4) | Mouse model; zebrafish model; iPSC model | Animal + in vitro | van de Putte et al., 2007, https://doi.org/10.1093/hmg/ddm093; Epifanova et al., 2019, Feb 2019, https://doi.org/10.1016/j.brainres.2018.09.034; Birkhoff et al., 2021, https://doi.org/10.3390/genes12071037 |
| Key mechanistic model findings | Neural crest-specific Zfhx1b/Zeb2 loss causes craniofacial, GI, cardiac, melanocyte, and autonomic defects; cortical models show altered neuro-/gliogenesis timing via **Ntf3**, **Sfrp1/Wnt**, and **Fgf9**-linked mechanisms; interneuron defects support altered **GABAergic** development and seizure susceptibility (epifanova2019roleofzeb2sip1 pages 3-4, epifanova2019roleofzeb2sip1 pages 7-7, putte2007neuralcrestspecificremoval pages 1-2, cordelli2021neurologicalphenotypeof pages 1-2) | GO: neural crest cell migration; forebrain development; GABAergic neuron differentiation; gliogenesis | Animal mechanistic | Epifanova et al., 2019, https://doi.org/10.1016/j.brainres.2018.09.034; van de Putte et al., 2007, https://doi.org/10.1093/hmg/ddm093; Cordelli et al., 2021, https://doi.org/10.3390/genes12070982 |


*Table: This compact table summarizes high-yield disease knowledge-base facts for Mowat-Wilson syndrome, including identifiers, ZEB2 genetics, major phenotype frequencies, 2024 episignature data, diagnostics, management, and model systems. It is designed to support rapid curation with evidence type labeling and source-linked citations.*

## 1. Disease information

### Definition and classification

MOWS is a **Mendelian, autosomal-dominant developmental disorder/chromatin-transcription disorder and neurocristopathy** resulting from ZEB2 haploinsufficiency. ZEB2 is a DNA-binding, SMAD-interacting transcriptional regulator required during embryonic neural, neural-crest, cardiac, enteric, craniofacial, and urogenital development. The information summarized here is principally **aggregated disease-level evidence** from molecularly confirmed cohorts, literature/database compilations, and mechanistic models—not individual EHR-derived data—although some reports contain individual case histories. (zou2020genotypephenotypeanalysisin pages 1-2, peter2024mowat–wilsonsyndromecase pages 2-4, birkhoff2021zeb2themowatwilson pages 1-2)

### Identifiers and synonyms

- **OMIM:** Mowat–Wilson syndrome, **#235730**; ZEB2, **605802**.
- **MONDO:** Mowat–Wilson syndrome; the exact MONDO accession was not verified in the retrieved evidence and should be reconciled directly against the current MONDO release before database import.
- **Gene:** **ZEB2**, formerly **ZFHX1B** or **SIP1**; chromosome **2q22.3**.
- **Synonyms:** Mowat-Wilson syndrome; MWS/MOWS; ZEB2-related Mowat-Wilson syndrome; ZFHX1B-related syndrome; historically, Hirschsprung disease–intellectual disability syndrome.
- A unique ICD-10-CM or MeSH disease code was not established in the retrieved literature. In practice, cases may be represented through congenital-malformation, intellectual-disability, epilepsy, or genetic-syndrome codes. ICD-11/SNOMED mappings should be checked against current terminology services rather than inferred.

## 2. Etiology, risk, protection, and gene–environment interaction

### Causal factor

The primary cause is a heterozygous pathogenic ZEB2 variant or deletion producing **loss of function and haploinsufficiency**. Reported classes include nonsense, frameshift, splice-altering, missense/hypomorphic variants, intragenic or whole-gene deletions, larger 2q22 rearrangements, and rare duplications or regulatory lesions. More than 220 pathogenic variants had been catalogued by 2020. (zou2020genotypephenotypeanalysisin pages 1-2)

A 2024 aggregation of 298 individuals found that exon 8 contained **198/298 variants (66%)**, that **more than 90%** were nonsense or frameshift changes, and that recurrent **c.2083C>T** represented approximately **11%** of reported patients. These figures describe an assembled literature/database series and should not be interpreted as unbiased population frequencies. (peter2024mowat–wilsonsyndromecase pages 1-2, peter2024mowat–wilsonsyndromecase pages 4-5)

### Risk and protective factors

- **Genetic risk:** A constitutional pathogenic ZEB2 allele is sufficient. Most cases are de novo. Rare parental germline mosaicism makes sibling recurrence low but not zero.
- **Modifier genes:** No clinically validated modifier is established. A 2026, non-peer-reviewed two-trio preprint proposed a common **RET enhancer risk haplotype** as a modifier of Hirschsprung penetrance. The high-risk haplotype had a reported OR of 11.01 and had previously been associated with greater than 50% reduction of RET expression in neural-crest-derived cells/fetal gut. This result is hypothesis-generating, not ready for clinical risk prediction. (collins2026wholegenomesequencing pages 6-9, collins2026wholegenomesequencing pages 13-19)
- **Environmental/lifestyle/infectious risk:** None is known to cause MOWS or materially alter its penetrance. Smoking, diet, alcohol, toxins, radiation, occupation, infection, and parental lifestyle are not established causal factors.
- **Protective factors:** No protective allele, exposure, diet, medication, or behavior has been validated as preventing the syndrome.
- **Gene–environment interactions:** No reproducible MOWS-specific interaction is established. Environment and access to care can influence complications and functional outcomes, but not the underlying congenital genotype.

## 3. Phenotypes

Phenotypes are congenital or emerge during infancy/childhood. Severity is variable, but developmental disability is generally chronic and substantial. Aggregate percentages differ because cohorts are small and ascertainment is phenotype-biased.

### Neurodevelopment and behavior

- **Global developmental delay/intellectual disability:** Nearly universal; typically moderate to severe or profound. Suggested terms: **Global developmental delay**, **Intellectual disability**, **Severe intellectual disability**.
- **Speech:** Severe expressive-language impairment; many individuals remain nonverbal or use a few words/signs or augmentative communication. Suggested term: **Severely delayed speech and language development**.
- **Motor development/hypotonia:** Delayed sitting, standing, and walking; mean walking age in aggregate review data was about **4 years**. In one four-person molecular series, two were not walking, one walked at approximately 3 years, and one at approximately 2 years. Suggested terms: **Delayed walking**, **Muscular hypotonia**, **Abnormality of gait**. (peter2024mowat–wilsonsyndromecase pages 1-2, zou2020genotypephenotypeanalysisin pages 3-5)
- **Behavior:** A frequently described sociable or happy demeanor does not exclude autism-like behaviors, stereotypies, pain-expression differences, or sleep disturbance. Quantified quality-of-life and behavioral prevalence estimates remain sparse.

Developmental impairments substantially affect communication, self-care, mobility, education, independent living, and caregiver burden. Formal MOWS-specific EQ-5D, SF-36, PROMIS, or validated quality-of-life natural-history datasets were not found.

### Neurologic and structural brain phenotypes

- **Epilepsy/abnormal EEG:** Aggregate review estimate **84%**; onset is usually in infancy or childhood, with variable seizure types and medication response. A four-child series observed epilepsy in 3/4, including spontaneous remission in one. Suggested terms: **Seizure**, **Epilepsy**, **Abnormal EEG**. (peter2024mowat–wilsonsyndromecase pages 1-2, zou2020genotypephenotypeanalysisin pages 3-5)
- **Brain malformations:** Corpus-callosum and hippocampal abnormalities, ventriculomegaly, white-matter abnormalities, cortical atrophy/dysplasia, enlarged basal ganglia, and cerebellar anomalies are reported; one synthesis estimated CNS malformations at approximately 80%. Suggested terms: **Agenesis/hypoplasia of corpus callosum**, **Hippocampal abnormality**, **Ventriculomegaly**, **Cerebral white-matter abnormality**. (peter2024mowat–wilsonsyndromecase pages 1-2, birkhoff2021zeb2themowatwilson pages 2-4)
- **Microcephaly:** Common and may become more evident postnatally. Suggested term: **Microcephaly**.
- **Sleep:** Sleep disturbance and sleep-activated epileptiform abnormalities can occur, but robust syndrome-specific frequencies are unavailable.

Neurologic involvement is described by experts as one of the principal determinants of prognosis and quality of life. (cordelli2021neurologicalphenotypeof pages 1-2)

### Craniofacial, growth, and musculoskeletal findings

The evolving facial gestalt includes hypertelorism/deep-set eyes, broad or medially flared eyebrows, a prominent or broad nasal tip, open mouth, pointed/triangular chin, and uplifted earlobes with central depression. Suggested HPO labels include **Hypertelorism**, **Deeply set eye**, **Broad eyebrow**, **Prominent nasal tip**, **Pointed chin**, and **Uplifted earlobe**. Short stature, microcephaly, slender habitus, hypotonia, scoliosis, pes planus, contractures, and delayed motor milestones may develop. Facial features were present in all four patients in one molecular case series. (zou2020genotypephenotypeanalysisin pages 1-2, zou2020genotypephenotypeanalysisin pages 3-5)

### Gastrointestinal and feeding phenotypes

- **Hirschsprung disease:** Approximately **50%**, usually congenital/early infancy; reflects enteric aganglionosis and can cause neonatal obstruction, abdominal distension, delayed meconium, or enterocolitis. Suggested term: **Hirschsprung disease**. (peter2024mowat–wilsonsyndromecase pages 1-2, birkhoff2021zeb2themowatwilson pages 2-4)
- **Constipation/dysmotility:** Common even without confirmed aganglionosis. Suggested terms: **Constipation**, **Gastrointestinal dysmotility**.
- **Feeding/growth:** Oral-motor dysfunction, gastroesophageal reflux, gastroparesis, aspiration risk, and poor growth may require enteral feeding. A severe 2024 case required gastrostomy feeding. (peter2024mowat–wilsonsyndromecase pages 2-4)

### Cardiovascular, genitourinary, ophthalmic, and other manifestations

- **Congenital heart disease:** Approximately **58%** in a 2024 aggregate review; lesions include septal defects, pulmonary-artery/valve anomalies and, rarely, complex disease. Suggested term: **Congenital heart defect**. (peter2024mowat–wilsonsyndromecase pages 1-2)
- **Genitourinary:** Hypospadias, cryptorchidism, renal tract anomalies, vesicoureteral reflux, and structural genital anomalies. Suggested terms: **Hypospadias**, **Cryptorchidism**, **Renal structural abnormality**.
- **Eyes/vision:** Strabismus, refractive error, ptosis and cerebral visual impairment may occur. Suggested terms: **Strabismus**, **Refractive error**, **Visual impairment**.
- **Dental/oral:** Dental anomalies and oral-health burdens are recognized, but quantified data remain limited; this gap motivated observational study NCT07476417.
- **Laboratory abnormalities:** There is no characteristic biochemical, enzyme, hematologic, metabolic, or inflammatory laboratory signature used clinically.

## 4. Genetic and molecular information

### Gene and protein

**ZEB2** encodes a nuclear zinc-finger E-box-binding transcription factor with N- and C-terminal zinc-finger clusters, a homeodomain, SMAD-binding and CtBP-interacting regions. It can repress or activate transcription depending on promoter, cell type, and binding partners. ZEB2 interacts with receptor-regulated and co-SMADs, CtBP, p300 and KAT2B/PCAF, HDAC/methyltransferase-associated machinery, and the NuRD corepressor complex. (giuseppe2024identificationofthe pages 2-2, epifanova2019roleofzeb2sip1 pages 2-3, putte2007neuralcrestspecificremoval pages 1-2)

### Variant interpretation

- **Typical pathogenic variants:** Germline heterozygous nonsense, frameshift, canonical splice, exon-level/multiexon, whole-gene, or 2q22.3 deletions. Their expected consequence is nonsense-mediated decay or absent/truncated protein.
- **Missense variants:** Rare; some zinc-finger missense alleles are hypomorphic and can produce milder/atypical disease. Many remain VUS: one 2024 source noted 290 ClinVar ZEB2 missense VUS at the time of analysis. Functional evidence, segregation, phenotype match, and potentially the methylation episignature are therefore important. (giuseppe2024identificationofthe pages 2-2, birkhoff2021zeb2themowatwilson pages 2-4)
- **ACMG/AMP:** A de novo null variant in a gene where haploinsufficiency is established generally supports pathogenic/likely pathogenic classification, subject to transcript relevance, population absence, sequencing quality, and full ACMG evidence assessment. Four truncating variants in a 2020 series were classified pathogenic and confirmed de novo. (zou2020genotypephenotypeanalysisin pages 3-5)
- **Population frequency:** Pathogenic loss-of-function alleles are expected to be absent or extremely rare in population databases. No reliable carrier frequency was identified; because the disorder is dominant and predominantly de novo, conventional recessive carrier frequency is not meaningful.
- **Somatic versus germline:** The disease is a constitutional germline disorder. Somatic ZEB2 changes relevant to cancer are not the cause of MOWS.

### Chromosomal abnormalities and epigenetics

Whole-gene and larger 2q22 deletions can produce MOWS, sometimes with additional deletion-dependent features. CMA is therefore essential when sequencing is negative or a larger imbalance is suspected. Conventional karyotyping or FISH is useful mainly for visible rearrangements or targeted familial follow-up, not as first-line testing for small intragenic variants.

The 2024 episignature study used blood leukocyte DNA from **29 people**—24 discovery and 5 validation cases—and retained 772,557 array probes after filtering. It identified **296 DMPs**, of which **98.6% were hypomethylated**; 208 mapped to 167 annotated genes and 16 highly significant hypomethylated sites lay within the ZEB2 locus. All MOWS cases received classifier scores near 1 and segregated from controls and 56 other neurodevelopmental episignatures. The authors’ exact conclusion was that the signature is “**highly sensitive and reproducible, providing a useful tool to facilitate diagnosis**.” Formal independent, population-scale sensitivity and specificity estimates are still needed. (giuseppe2024identificationofthe pages 5-6, giuseppe2024identificationofthe pages 1-2, giuseppe2024identificationofthe pages 2-2)

No validated prognostic methylation, proteomic, metabolomic, or lipidomic signature is available.

## 5. Environmental information

MOWS is not environmentally caused. No toxin, pollutant, radiation exposure, occupation, diet, smoking, alcohol use, exercise pattern, bacterium, virus, fungus, or parasite has been established as a trigger. Standard nutrition, exercise, sleep, vaccination, infection prevention, and avoidance of smoke are appropriate for general health and complication reduction but are not primary prevention for the genotype.

## 6. Mechanism and pathophysiology

### Upstream causal chain

**Pathogenic ZEB2 allele/deletion → reduced functional nuclear ZEB2 → altered DNA binding, SMAD-dependent/independent transcription and chromatin-coregulator recruitment → mistimed lineage specification, migration and cell–cell signaling during embryogenesis → tissue-specific malformations and postnatal neurologic dysfunction.**

### Neural crest and enteric disease

ZEB2 limits BMP-SMAD signaling at the neural plate border, represses epithelial genes such as **CDH1** during epithelial-to-mesenchymal transition, and regulates neural-crest specifiers including **FOXD3** and **SOX10**. Loss impairs induction, delamination, migration, and differentiation of cranial, cardiac, vagal, melanocytic, and autonomic neural-crest lineages. The downstream clinical chain is defective vagal crest colonization of bowel → enteric ganglion deficiency → Hirschsprung disease/constipation; defective cranial/cardiac crest → facial and cardiovascular anomalies. Neural-crest-specific mouse deletion reproduced craniofacial, GI, cardiac, melanoblast, and autonomic defects. (epifanova2019roleofzeb2sip1 pages 3-4, putte2007neuralcrestspecificremoval pages 1-2)

Suggested terms: **GO neural crest cell development; neural crest cell migration; epithelial-to-mesenchymal transition; enteric nervous system development; BMP signaling**. Suggested cell types: **neural crest cell**, **enteric neural progenitor**, **enteric neuron**, **melanoblast**, **autonomic neuron**.

### Cortex, hippocampus, and corpus callosum

Conditional mouse studies indicate that ZEB2 controls neurogenesis/gliogenesis timing partly through non-cell-autonomous signaling from postmitotic neurons to progenitors. ZEB2 normally restrains **Ntf3**; excess Ntf3 shifts apical/basal progenitor balance and promotes premature upper-layer neurogenesis. Dorsal telencephalic loss also increases **Sfrp1**, suppressing Wnt signaling, reducing hippocampal progenitor proliferation, increasing apoptosis, and contributing to hippocampal/callosal agenesis. (epifanova2019roleofzeb2sip1 pages 7-7, cordelli2021neurologicalphenotypeof pages 1-2)

Suggested terms: **GO cerebral cortex development; hippocampus development; corpus callosum development; regulation of neurogenesis; gliogenesis; Wnt signaling; neuron-to-progenitor signaling**. Cell types: **radial glial cell**, **neural progenitor cell**, **cortical projection neuron**.

### GABAergic interneurons and epilepsy

In ventral telencephalic models, Zeb2 loss disrupts interneuron migration and subtype maturation; increased **Unc5b** repulsive signaling contributes to abnormal interneuron positioning/numbers. Heterozygous mice show reduced parvalbumin interneurons on some genetic backgrounds. The plausible chain is altered inhibitory-neuron development → excitation/inhibition imbalance → epilepsy and neurobehavioral impairment. This is strong animal-model biology but is not yet a validated patient biomarker. (epifanova2019roleofzeb2sip1 pages 3-4, epifanova2019roleofzeb2sip1 pages 2-3)

Suggested terms: **GO GABAergic neuron differentiation; interneuron migration; regulation of synaptic transmission, GABAergic**. Cell types: **GABAergic interneuron**, **parvalbumin-positive interneuron**.

### Glia and cerebellum

ZEB2 regulates neuro-/gliogenic timing and FGF, Notch, and TGF-β/BMP components. Cerebellar radial-glia deletion in mice impairs Bergmann-glia specification, granule-neuron migration, cerebellar lamination, and locomotion. These findings offer a mechanism for motor dysfunction but do not prove that all human motor impairment is cerebellar. (birkhoff2021zeb2themowatwilson pages 1-2, cordelli2021neurologicalphenotypeof pages 1-2)

Suggested terms: **GO gliogenesis; Bergmann glial cell differentiation; cerebellar cortex morphogenesis; granule-cell migration**. Cell types: **Bergmann glial cell**, **cerebellar radial glial cell**, **granule neuron progenitor**.

### Molecular profiling and advanced technology

The best validated human molecular profile is the blood episignature. Transcriptomic animal studies identify broad, context-dependent target sets; a universal human disease transcriptome, proteome, metabolome, lipidome, spatial-transcriptomic atlas, or CRISPR-screen-derived therapeutic target was not established. Patient iPSCs are an important emerging platform for mutation-specific neural phenotyping, but the retrieved evidence emphasizes that no model yet captures the full human syndrome. (birkhoff2021zeb2themowatwilson pages 24-25)

## 7. Anatomical structures affected

- **Primary systems:** CNS and peripheral/enteric nervous system; heart; GI tract; craniofacial structures; genitourinary tract.
- **Secondary structures:** Musculoskeletal system, eyes/visual pathways, teeth/oral cavity, feeding/respiratory apparatus.
- **Suggested UBERON labels:** brain, cerebral cortex, hippocampus, corpus callosum, cerebellum, enteric nervous system, colon, heart, kidney, urethra, eye.
- **Tissues/cells:** neuroepithelium, neural crest, cortical neurons/progenitors, GABAergic interneurons, radial and Bergmann glia, enteric neurons, cardiac/craniofacial neural-crest derivatives.
- **Subcellular localization:** ZEB2 acts principally in the **nucleus/chromatin**; suggested GO cellular components are **nucleus**, **chromatin**, and **transcription regulator complex**.
- **Lateralization:** Most findings are midline, bilateral, or systemic; no consistent unilateral predilection is established.

## 8. Temporal development

MOWS begins **prenatally**, because ZEB2 dosage affects early lineage and organ development. Congenital manifestations include facial patterning, heart/genitourinary anomalies, brain malformations, and Hirschsprung disease. Hypotonia, developmental delay, poor growth, microcephaly, epilepsy, constipation, scoliosis, and functional limitations become apparent or evolve during infancy and childhood.

The course is **chronic and lifelong**, not relapsing-remitting. Congenital structural defects are stable unless corrected, while manifestations such as seizures, constipation, sleep disturbance, orthopedic complications, and feeding problems may fluctuate. Developmental gains occur, often slowly, but complete recovery is not expected. There is no established stage system, remission definition, or end-stage disease. Critical windows include prenatal neurodevelopment and early childhood, when seizure control, nutrition, communication support, and intensive developmental therapies may maximize function.

## 9. Inheritance and population

- **Prevalence:** Approximately **1:50,000–70,000 live births**, equivalent to about 1.4–2 per 100,000. True prevalence may be higher because mild/atypical cases are missed. Incidence per year has not been robustly measured. (zou2020genotypephenotypeanalysisin pages 1-2, birkhoff2021zeb2themowatwilson pages 1-2)
- **Inheritance:** Autosomal dominant; predominantly de novo.
- **Penetrance:** ZEB2 loss-of-function has high penetrance for neurodevelopmental disease, but individual manifestations—especially Hirschsprung disease, epilepsy, cardiac disease, and malformations—show incomplete penetrance.
- **Expressivity:** Markedly variable. Rare hypomorphic missense variants may be milder than null alleles; larger deletions may add contiguous-gene features. Proposed position/severity correlations remain imperfect. (zou2020genotypephenotypeanalysisin pages 1-2, zou2020genotypephenotypeanalysisin pages 3-5, birkhoff2021zeb2themowatwilson pages 2-4)
- **Anticipation:** Not described; no repeat-expansion mechanism.
- **Mosaicism:** Parental germline mosaicism is a recognized counseling concern in de novo dominant disease, although quantitative MOWS-specific recurrence data were not retrieved.
- **Founder effect/consanguinity:** No established founder variant or consanguinity association. Consanguinity is not mechanistically relevant to a predominantly de novo dominant disorder.
- **Sex/ethnicity/geography:** Both sexes and diverse populations are affected. No robust sex bias, ethnic enrichment, or endemic geographic distribution is established.

## 10. Diagnostics

### Clinical recognition

Suspect MOWS in a child with developmental delay/severe speech impairment and characteristic facies, especially when accompanied by epilepsy, postnatal microcephaly, Hirschsprung disease/constipation, corpus-callosum abnormality, congenital heart disease, or male genital anomalies. Facial recognition can guide testing, but molecular confirmation is required because neonatal and mild cases can be subtle.

### Recommended molecular workflow

1. **Sequence and deletion/duplication analysis of ZEB2**, either as a single gene or within a developmental-delay/epilepsy/Hirschsprung panel.
2. If the phenotype is nonspecific, use **trio exome or genome sequencing**; WGS can detect coding, splice, structural, and selected regulatory lesions. A 2020 WGS study found four de novo truncating ZEB2 variants among 530 children referred for epilepsy/developmental delay. (zou2020genotypephenotypeanalysisin pages 3-5)
3. **Chromosomal microarray** for exon-level/whole-gene or broader 2q22 deletions; ensure the laboratory’s sequencing assay has validated CNV detection or add MLPA/qPCR/CMA.
4. **RNA studies** may clarify suspected splice variants; routine diagnostic proteomics/metabolomics is unsupported.
5. **Blood DNA methylation/EpiSign** may provide functional support for an atypical presentation or VUS, based on the 2024 episignature, but should complement—not replace—sequence/CNV analysis. (giuseppe2024identificationofthe pages 5-6, giuseppe2024identificationofthe pages 1-2)
6. **Karyotype/FISH** only when a balanced/large rearrangement is suspected or for targeted familial studies. Mitochondrial and repeat-expansion testing are not disease-specific.

### Baseline clinical evaluation after diagnosis

Recommended phenotype-directed assessments include growth/head circumference; developmental, speech-language and augmentative-communication evaluation; neurologic examination and EEG when seizures or regression are suspected; brain MRI; echocardiogram; renal ultrasound and urologic review; examination for Hirschsprung disease/constipation; feeding/swallow and nutritional assessment; vision/hearing, dental, orthopedic, and sleep evaluation.

### Differential diagnosis

Important alternatives include **Pitt–Hopkins syndrome (TCF4)**, Angelman syndrome, Rett syndrome, Kleefstra syndrome, Goldberg–Shprintzen syndrome, Koolen–de Vries syndrome, DYRK1A-related disorder, CHARGE syndrome, and other syndromic Hirschsprung/neurodevelopmental disorders. MOWS is favored by its characteristic ears/nasal tip/chin, ZEB2 variant, Hirschsprung disease, and callosal/hippocampal pattern. Molecular testing resolves overlap.

### Screening

There is no population newborn or carrier-screening program. Cascade testing is appropriate only after a familial variant is identified. Newborn biochemical screening does not detect MOWS.

## 11. Outcome and prognosis

Reliable 5-year/10-year survival curves, disease-specific mortality rates, and median life expectancy are unavailable. Survival into adulthood occurs, but evidence is limited by rarity and young historical cohorts. Mortality and serious morbidity are driven by complex heart disease, Hirschsprung-associated enterocolitis/obstruction, aspiration or feeding complications, severe epilepsy, infection, and perioperative risk—not by a known progressive metabolic degeneration. A reported 2024 child with severe cardiac and GI disease died around age five, illustrating possible severity but not population prognosis. (peter2024mowat–wilsonsyndromecase pages 2-4)

Long-term disability usually includes intellectual and expressive-language impairment, dependence in activities of daily living, and variable mobility and epilepsy. Recovery from the underlying syndrome is not expected, although seizures, nutrition, mobility, communication, and participation can improve with treatment. No validated molecular prognostic biomarker exists. Variant class/domain, deletion size, congenital anomaly burden, epilepsy control, aspiration, and Hirschsprung complications are clinically relevant but incompletely quantified prognostic factors.

## 12. Treatment and real-world implementation

### Current strategy

There is **no approved disease-modifying pharmacotherapy** and no established ZEB2-specific pharmacogenomic recommendation. Treatment is individualized and multidisciplinary:

- **Epilepsy:** Standard antiseizure medication selected by seizure type/EEG; rescue medication and safety planning when indicated. Suggested MAXO labels: antiseizure pharmacotherapy, EEG monitoring.
- **Hirschsprung disease:** Pediatric surgical evaluation and pull-through surgery; urgent treatment of obstruction or enterocolitis. Persistent constipation requires structured bowel management. Suggested MAXO: surgical correction of Hirschsprung disease, bowel-management therapy.
- **Cardiac/GU anomalies:** Guideline-based cardiology surveillance and surgical/interventional correction; urology/nephrology management for hypospadias, cryptorchidism, reflux or renal anomalies.
- **Feeding/nutrition:** Swallow assessment, reflux/constipation treatment, caloric support, and gastrostomy when oral feeding is unsafe or inadequate. A severe case required G-tube feeding. (peter2024mowat–wilsonsyndromecase pages 2-4)
- **Rehabilitation:** Early physical, occupational, speech-language, feeding, behavioral, educational and augmentative/alternative-communication services. Suggested MAXO: physical therapy, occupational therapy, speech therapy, augmentative communication assessment.
- **Other:** Vision/hearing correction, dental care, orthopedic surveillance, sleep evaluation, vaccination, and family psychosocial support.

There are no syndrome-specific response rates or comparative trials; adverse effects follow those of each conventional intervention.

### Experimental therapy and trials

No interventional gene-replacement, CRISPR, cell, ASO, siRNA, mRNA, targeted small-molecule, or immunotherapy trial was identified. ClinicalTrials.gov searching found **NCT07476417**, a not-yet-recruiting observational University of Milan study of oral health, dentofacial status, and oral-health-related quality of life, planned enrollment **25**. This is natural-history/implementation research, not treatment.

## 13. Prevention

Primary prevention by lifestyle or vaccination is not possible. Prevention consists mainly of reproductive counseling and complication reduction:

- **Genetic counseling:** Explain de novo autosomal-dominant causation, low but nonzero sibling recurrence from possible germline mosaicism, and 50% transmission risk for an affected reproductive individual.
- **Reproductive options:** If the familial variant is known, prenatal diagnosis by CVS/amniocentesis and preimplantation genetic testing are technically possible. A negative parental blood test does not make recurrence zero.
- **Secondary prevention:** Early molecular diagnosis; prompt evaluation for cardiac, bowel, renal, feeding, seizure, vision/hearing, and developmental complications.
- **Tertiary prevention:** Seizure safety, aspiration prevention, bowel regimens/enterocolitis education, nutrition, rehabilitation, orthopedic surveillance, oral care, and routine immunization.
- No MOWS-specific prophylactic drug or public-health/environmental intervention exists.

## 14. Other species and natural disease

ZEB2 is evolutionarily conserved in vertebrates. Relevant taxa include **Homo sapiens**, **Mus musculus** (mouse), and **Danio rerio** (zebrafish). A naturally occurring, breed-associated veterinary counterpart was not identified; available animal phenotypes are engineered or experimentally induced. There is no infectious transmission, zoonotic potential, or cross-species contagion.

Comparative biology supports conserved roles in neural-crest specification, neural patterning, cortical development, interneuron migration, gliogenesis, and organogenesis, but species differences in brain development and dosage sensitivity limit direct translation.

## 15. Model organisms and experimental systems

### Mouse

- **Constitutive Zeb2 knockout:** Embryonic death around E9.5 with neural-tube closure and neural-crest defects; useful for upstream embryology but too severe for postnatal MOWS. (epifanova2019roleofzeb2sip1 pages 3-4)
- **Wnt1-Cre neural-crest conditional knockout:** Craniofacial, GI/enteric, cardiac, melanoblast and autonomic defects resembling MOWS neurocristopathy. (putte2007neuralcrestspecificremoval pages 1-2)
- **Emx1-Cre/Nex-Cre cortical models:** Hippocampal/callosal abnormalities and altered cortical layer/neurogenic timing involving Sfrp1/Wnt, Ntf3 and Fgf9 signaling. (epifanova2019roleofzeb2sip1 pages 3-4, epifanova2019roleofzeb2sip1 pages 7-7, cordelli2021neurologicalphenotypeof pages 1-2)
- **Nestin-Cre or ventral telencephalic conditional models:** Perinatal lethality or GABAergic interneuron migration/subtype abnormalities; useful for epilepsy mechanisms. (epifanova2019roleofzeb2sip1 pages 3-4, epifanova2019roleofzeb2sip1 pages 2-3)
- **Heterozygous Δex7 models:** Some backgrounds show facial change, reduced motor activity, and fewer parvalbumin interneurons; background dependence is a major limitation. (epifanova2019roleofzeb2sip1 pages 2-3)

### Zebrafish

Knockdown/perturbation models show neural patterning and neural-crest defects and support conserved anti-BMP functions. Limitations include genome duplication, developmental differences, and incomplete correspondence to human cognition/facial anatomy. (birkhoff2021zeb2themowatwilson pages 2-4)

### Cellular/iPSC systems

Patient-derived iPSCs and differentiated neural progenitors/neurons are well suited to mutation-specific transcription, neurogenesis, and GABAergic phenotyping and to testing dosage-restoration strategies. Expert reviews emphasize their importance because most patients have unique alleles and no mouse model reproduces the entire syndrome. However, validated therapeutic screening endpoints and mature organoid/spatial or multi-omic standards remain under development. (birkhoff2021zeb2themowatwilson pages 24-25)

## Recent developments and expert interpretation

1. **2024 episignature:** The clearest recent translational advance. The exact abstract states that investigators “**identified and validated a DNA methylation signature involving 296 differentially methylated probes**.” Its near-universal hypomethylation is biologically consistent with ZEB2’s major repressor role. Independent prospective validation—especially in missense VUS, mosaic cases and differential diagnoses—is the next step. (giuseppe2024identificationofthe pages 5-6, giuseppe2024identificationofthe pages 1-2)
2. **2024 variant synthesis:** The abstract reports that “**more than 90% of the defects were due to nonsense or frameshift changes**,” reinforcing haploinsufficiency as the dominant mechanism and exon 8 as a diagnostic hotspot. Nevertheless, complete-gene coverage and CNV analysis remain necessary; hotspot-only testing would miss many cases. (peter2024mowat–wilsonsyndromecase pages 1-2, peter2024mowat–wilsonsyndromecase pages 4-5)
3. **Mechanistic convergence:** Experts view MOWS not as a single-pathway disorder but as a developmental transcription/chromatin-dosage disorder affecting neural crest, cortical progenitor feedback, inhibitory interneurons, and glia through TGF-β/BMP-SMAD, Wnt, Notch, FGF and chromatin-coregulator networks. (birkhoff2021zeb2themowatwilson pages 1-2, epifanova2019roleofzeb2sip1 pages 3-4, cordelli2021neurologicalphenotypeof pages 1-2)
4. **Evidence gap:** Clinical care remains extrapolated from organ-specific standards and expert consensus. Prospective natural-history cohorts, adult outcome studies, standardized quality-of-life measures, genotype-aware biomarkers, and interventional trials are major unmet needs.

## Evidence-quality and curation notes

- Phenotype percentages are mostly derived from small or aggregated, referral-biased cohorts and should carry a “variable/estimated” qualifier.
- The 2024 methylation work is human molecular evidence; mechanistic pathway chains are primarily conditional-mouse or cellular evidence and should not be represented as proven human biomarkers.
- The RET-modifier finding is a 2026 preprint based on two trios and must remain explicitly labeled preliminary. (collins2026wholegenomesequencing pages 6-9, collins2026wholegenomesequencing pages 13-19)
- PMIDs were not consistently present in the retrieved source metadata; therefore none were fabricated. DOI URLs and publication dates have been supplied for the major sources.

### Key source URLs and publication dates

- Caraffi et al., **February 2024**, *European Journal of Human Genetics*: https://doi.org/10.1038/s41431-024-01548-4. (giuseppe2024identificationofthe pages 5-6)
- Peter et al., **February 2024**, *International Journal of Molecular Sciences*: https://doi.org/10.3390/ijms25052838. (peter2024mowat–wilsonsyndromecase pages 1-2)
- Cordelli et al., **June 2021**, *Genes*: https://doi.org/10.3390/genes12070982. (cordelli2021neurologicalphenotypeof pages 1-2)
- Birkhoff et al., **July 2021**, *Genes*: https://doi.org/10.3390/genes12071037. (birkhoff2021zeb2themowatwilson pages 1-2)
- Zou et al., **October 2020**, *Experimental and Therapeutic Medicine*: https://doi.org/10.3892/etm.2020.9393. (zou2020genotypephenotypeanalysisin pages 1-2)
- Epifanova et al., **February 2019**, *Brain Research*: https://doi.org/10.1016/j.brainres.2018.09.034. (epifanova2019roleofzeb2sip1 pages 3-4)
- Van de Putte et al., **June 2007**, *Human Molecular Genetics*: https://doi.org/10.1093/hmg/ddm093. (putte2007neuralcrestspecificremoval pages 1-2)

References

1. (zou2020genotypephenotypeanalysisin pages 1-2): Dongfang Zou, Lin Wang, Feiqiu Wen, Hongdou Xiao, Jing Duan, Tongda Zhang, Zhenzhen Yin, Qiwen Dong, Jian Guo, and Jianxiang Liao. Genotype-phenotype analysis in mowat-wilson syndrome associated with two novel and two recurrent zeb2 variants. Experimental and Therapeutic Medicine, 20:1-1, Oct 2020. URL: https://doi.org/10.3892/etm.2020.9393, doi:10.3892/etm.2020.9393. This article has 11 citations and is from a peer-reviewed journal.

2. (birkhoff2021zeb2themowatwilson pages 1-2): Judith C. Birkhoff, Danny Huylebroeck, and Andrea Conidi. Zeb2, the mowat-wilson syndrome transcription factor: confirmations, novel functions, and continuing surprises. Genes, 12:1037, Jul 2021. URL: https://doi.org/10.3390/genes12071037, doi:10.3390/genes12071037. This article has 60 citations.

3. (peter2024mowat–wilsonsyndromecase pages 1-2): Caroline St. Peter, Waheeda A. Hossain, Scott Lovell, Syed K. Rafi, and Merlin G. Butler. Mowat–wilson syndrome: case report and review of zeb2 gene variant types, protein defects and molecular interactions. International Journal of Molecular Sciences, 25:2838, Feb 2024. URL: https://doi.org/10.3390/ijms25052838, doi:10.3390/ijms25052838. This article has 20 citations.

4. (giuseppe2024identificationofthe pages 5-6): Stefano Giuseppe Caraffi, Liselot van der Laan, Kathleen Rooney, Slavica Trajkova, Roberta Zuntini, Raissa Relator, Sadegheh Haghshenas, Michael A. Levy, Chiara Baldo, Giorgia Mandrile, Carolyn Lauzon, Duccio Maria Cordelli, Ivan Ivanovski, Anna Fetta, Elena Sukarova, Alfredo Brusco, Lisa Pavinato, Verdiana Pullano, Marcella Zollino, Haley McConkey, Marco Tartaglia, Giovanni Battista Ferrero, Bekim Sadikovic, and Livia Garavelli. Identification of the dna methylation signature of mowat-wilson syndrome. European Journal of Human Genetics, 32(6):619-629, Feb 2024. URL: https://doi.org/10.1038/s41431-024-01548-4, doi:10.1038/s41431-024-01548-4. This article has 9 citations and is from a domain leading peer-reviewed journal.

5. (giuseppe2024identificationofthe pages 1-2): Stefano Giuseppe Caraffi, Liselot van der Laan, Kathleen Rooney, Slavica Trajkova, Roberta Zuntini, Raissa Relator, Sadegheh Haghshenas, Michael A. Levy, Chiara Baldo, Giorgia Mandrile, Carolyn Lauzon, Duccio Maria Cordelli, Ivan Ivanovski, Anna Fetta, Elena Sukarova, Alfredo Brusco, Lisa Pavinato, Verdiana Pullano, Marcella Zollino, Haley McConkey, Marco Tartaglia, Giovanni Battista Ferrero, Bekim Sadikovic, and Livia Garavelli. Identification of the dna methylation signature of mowat-wilson syndrome. European Journal of Human Genetics, 32(6):619-629, Feb 2024. URL: https://doi.org/10.1038/s41431-024-01548-4, doi:10.1038/s41431-024-01548-4. This article has 9 citations and is from a domain leading peer-reviewed journal.

6. (giuseppe2024identificationofthe pages 2-2): Stefano Giuseppe Caraffi, Liselot van der Laan, Kathleen Rooney, Slavica Trajkova, Roberta Zuntini, Raissa Relator, Sadegheh Haghshenas, Michael A. Levy, Chiara Baldo, Giorgia Mandrile, Carolyn Lauzon, Duccio Maria Cordelli, Ivan Ivanovski, Anna Fetta, Elena Sukarova, Alfredo Brusco, Lisa Pavinato, Verdiana Pullano, Marcella Zollino, Haley McConkey, Marco Tartaglia, Giovanni Battista Ferrero, Bekim Sadikovic, and Livia Garavelli. Identification of the dna methylation signature of mowat-wilson syndrome. European Journal of Human Genetics, 32(6):619-629, Feb 2024. URL: https://doi.org/10.1038/s41431-024-01548-4, doi:10.1038/s41431-024-01548-4. This article has 9 citations and is from a domain leading peer-reviewed journal.

7. (peter2024mowat–wilsonsyndromecase pages 4-5): Caroline St. Peter, Waheeda A. Hossain, Scott Lovell, Syed K. Rafi, and Merlin G. Butler. Mowat–wilson syndrome: case report and review of zeb2 gene variant types, protein defects and molecular interactions. International Journal of Molecular Sciences, 25:2838, Feb 2024. URL: https://doi.org/10.3390/ijms25052838, doi:10.3390/ijms25052838. This article has 20 citations.

8. (putte2007neuralcrestspecificremoval pages 1-2): Tom Van de Putte, Annick Francis, Luc Nelles, Leo A. van Grunsven, and Danny Huylebroeck. Neural crest-specific removal of zfhx1b in mouse leads to a wide range of neurocristopathies reminiscent of mowat-wilson syndrome. Human molecular genetics, 16 12:1423-36, Jun 2007. URL: https://doi.org/10.1093/hmg/ddm093, doi:10.1093/hmg/ddm093. This article has 115 citations and is from a domain leading peer-reviewed journal.

9. (zou2020genotypephenotypeanalysisin pages 3-5): Dongfang Zou, Lin Wang, Feiqiu Wen, Hongdou Xiao, Jing Duan, Tongda Zhang, Zhenzhen Yin, Qiwen Dong, Jian Guo, and Jianxiang Liao. Genotype-phenotype analysis in mowat-wilson syndrome associated with two novel and two recurrent zeb2 variants. Experimental and Therapeutic Medicine, 20:1-1, Oct 2020. URL: https://doi.org/10.3892/etm.2020.9393, doi:10.3892/etm.2020.9393. This article has 11 citations and is from a peer-reviewed journal.

10. (birkhoff2021zeb2themowatwilson pages 2-4): Judith C. Birkhoff, Danny Huylebroeck, and Andrea Conidi. Zeb2, the mowat-wilson syndrome transcription factor: confirmations, novel functions, and continuing surprises. Genes, 12:1037, Jul 2021. URL: https://doi.org/10.3390/genes12071037, doi:10.3390/genes12071037. This article has 60 citations.

11. (peter2024mowat–wilsonsyndromecase pages 2-4): Caroline St. Peter, Waheeda A. Hossain, Scott Lovell, Syed K. Rafi, and Merlin G. Butler. Mowat–wilson syndrome: case report and review of zeb2 gene variant types, protein defects and molecular interactions. International Journal of Molecular Sciences, 25:2838, Feb 2024. URL: https://doi.org/10.3390/ijms25052838, doi:10.3390/ijms25052838. This article has 20 citations.

12. (cordelli2021neurologicalphenotypeof pages 1-2): Duccio Maria Cordelli, Veronica Di Pisa, Anna Fetta, Livia Garavelli, Lucia Maltoni, Luca Soliani, and Emilia Ricci. Neurological phenotype of mowat-wilson syndrome. Genes, 12:982, Jun 2021. URL: https://doi.org/10.3390/genes12070982, doi:10.3390/genes12070982. This article has 29 citations.

13. (collins2026wholegenomesequencing pages 6-9): Sydney Collins, Ibrahim Bah, Ryan Pysar, David Mowat, Tychele N. Turner, and Sumantra Chatterjee. Whole genome sequencing reveals a <i>ret</i> enhancer risk haplotype associated with hirschsprung disease in mowat wilson syndrome. medRxiv, Mar 2026. URL: https://doi.org/10.64898/2026.03.19.26348831, doi:10.64898/2026.03.19.26348831. This article has 0 citations.

14. (collins2026wholegenomesequencing pages 13-19): Sydney Collins, Ibrahim Bah, Ryan Pysar, David Mowat, Tychele N. Turner, and Sumantra Chatterjee. Whole genome sequencing reveals a <i>ret</i> enhancer risk haplotype associated with hirschsprung disease in mowat wilson syndrome. medRxiv, Mar 2026. URL: https://doi.org/10.64898/2026.03.19.26348831, doi:10.64898/2026.03.19.26348831. This article has 0 citations.

15. (birkhoff2021zeb2themowatwilson pages 24-25): Judith C. Birkhoff, Danny Huylebroeck, and Andrea Conidi. Zeb2, the mowat-wilson syndrome transcription factor: confirmations, novel functions, and continuing surprises. Genes, 12:1037, Jul 2021. URL: https://doi.org/10.3390/genes12071037, doi:10.3390/genes12071037. This article has 60 citations.

16. (epifanova2019roleofzeb2sip1 pages 3-4): Ekaterina Epifanova, Alexey Babaev, Andrew G. Newman, and Victor Tarabykin. Role of zeb2/sip1 in neuronal development. Brain Research, 1705:24-31, Feb 2019. URL: https://doi.org/10.1016/j.brainres.2018.09.034, doi:10.1016/j.brainres.2018.09.034. This article has 83 citations and is from a peer-reviewed journal.

17. (epifanova2019roleofzeb2sip1 pages 2-3): Ekaterina Epifanova, Alexey Babaev, Andrew G. Newman, and Victor Tarabykin. Role of zeb2/sip1 in neuronal development. Brain Research, 1705:24-31, Feb 2019. URL: https://doi.org/10.1016/j.brainres.2018.09.034, doi:10.1016/j.brainres.2018.09.034. This article has 83 citations and is from a peer-reviewed journal.

18. (epifanova2019roleofzeb2sip1 pages 7-7): Ekaterina Epifanova, Alexey Babaev, Andrew G. Newman, and Victor Tarabykin. Role of zeb2/sip1 in neuronal development. Brain Research, 1705:24-31, Feb 2019. URL: https://doi.org/10.1016/j.brainres.2018.09.034, doi:10.1016/j.brainres.2018.09.034. This article has 83 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Mowat-Wilson_syndrome-deep-research-falcon_artifacts/artifact-00.md)