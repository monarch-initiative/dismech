---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-24T14:50:49.016312'
end_time: '2026-07-24T14:58:32.887469'
duration_seconds: 463.87
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: ALG1-congenital disorder of glycosylation
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 14
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: ALG1-Congenital_Disorder_of_Glycosylation-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** ALG1-congenital disorder of glycosylation
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **ALG1-congenital disorder of glycosylation** covering all of the
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
- **Disease Name:** ALG1-congenital disorder of glycosylation
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **ALG1-congenital disorder of glycosylation** covering all of the
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


# ALG1-congenital disorder of glycosylation (ALG1-CDG): disease-characteristics report

## Executive summary

ALG1-CDG is an ultrarare, autosomal-recessive congenital disorder of protein N-glycosylation caused by biallelic pathogenic variants in **ALG1**, which encodes an endoplasmic-reticulum β1,4-mannosyltransferase. The enzyme adds the first mannose to the dolichol-linked oligosaccharide precursor used for N-glycosylation. Deficiency therefore produces incomplete lipid-linked glycans, under-occupancy of N-glycosylation sites, and systemic dysfunction of glycoproteins. Disease severity ranges from developmental disability to lethal neonatal/infantile multisystem disease. In the largest disease-specific cohort, developmental delay occurred in 37/37 evaluable patients, hypotonia in 37/39, seizures/epilepsy in 36/38, and premature death in 17/39. (ng2016alg1‐cdgclinicaland pages 4-6, ng2016alg1‐cdgclinicaland pages 1-3)

The most useful biochemical clue is a type-I carbohydrate-deficient transferrin pattern. A stronger ALG1-associated marker is the nonphysiologic N-linked tetrasaccharide **NeuAc-Gal-GlcNAc₂**, detected in all 27 tested patients in the landmark cohort. Diagnosis nevertheless requires demonstration of pathogenic biallelic ALG1 variants, ideally supported by glycan or functional evidence. There is no established disease-modifying treatment; current care is multidisciplinary and complication-directed. (ng2016alg1‐cdgclinicaland pages 1-3, ng2016alg1‐cdgclinicaland pages 6-8)

The following table summarizes high-value knowledge-base annotations.

| domain | high-confidence finding | quantitative evidence | suggested ontology terms | evidence type |
|---|---|---|---|---|
| Disease identifiers | ALG1-congenital disorder of glycosylation is a rare N-glycosylation disorder; former name CDG-Ik; disease OMIM/MIM 608540; causal gene ALG1 MIM 605907 | Landmark cohort expanded known cases to 57 total by 2016 (39 new + 18 previously reported) (ng2016alg1‐cdgclinicaland pages 1-3, ng2016alg1‐cdgclinicaland pages 6-8) | MONDO: not confirmed here; OMIM: 608540; MeSH/ICD not confidently established from retrieved sources; synonym: ALG1-CDG, CDG-Ik | Human clinical cohort + disease literature |
| Gene / inheritance | Caused by biallelic pathogenic variants in ALG1; inheritance is autosomal recessive | 39 affected individuals from 32 unrelated families; 17 male / 22 female (ng2016alg1‐cdgclinicaland pages 4-6, ng2016alg1‐cdgclinicaland pages 1-3) | ALG1 (HGNC gene symbol); autosomal recessive inheritance | Human clinical genetics |
| Molecular function | ALG1 encodes an ER-localized beta-1,4 mannosyltransferase that adds the first mannose to the growing dolichol-linked oligosaccharide in N-glycosylation | First of 9 mannose residues in the DLO precursor (ng2016alg1‐cdgclinicaland pages 1-3, ng2016alg1‐cdgclinicaland pages 10-13) | GO: protein N-linked glycosylation; GO cellular component: endoplasmic reticulum; CHEBI labels: GDP-mannose, dolichol-PP-GlcNAc2 | Human + biochemical pathway literature |
| Pathomechanism | ALG1 deficiency causes incomplete lipid-linked oligosaccharide synthesis, under-occupied N-glycosylation sites, and transfer of truncated glycans to proteins; NeuAc-Gal-GlcNAc2 can form after Golgi processing of truncated GlcNAc2-bearing proteins | ~2–8% of purified serum transferrin carried the xeno-tetrasaccharide in prior biomarker studies cited by cohort authors; 27/27 tested ALG1-CDG patients in the 2016 cohort had the biomarker present (ng2016alg1‐cdgclinicaland pages 4-6, ng2016alg1‐cdgclinicaland pages 6-8) | GO: dolichol-linked oligosaccharide biosynthetic process; GO: protein glycosylation; UBERON: blood serum | Human biochemical + model-supported mechanism |
| Variant spectrum | Broad allelic heterogeneity with many novel missense/splice variants; p.Ser258Leu is the most recurrent severe allele in available cohort data | 31 potential variants identified; 26/31 (84%) novel; p.Ser258Leu present in 17/39 (44%) patients (ng2016alg1‐cdgclinicaland pages 3-4) | Sequence variant classes: missense, splice-site; ACMG labels when individually assessed in later case reports | Human clinical genetics |
| Core phenotype: developmental delay | Neurodevelopmental impairment is near-universal | Developmental delay 37/37 (100%) (ng2016alg1‐cdgclinicaland pages 4-6) | HPO: Developmental delay (HP:0001263) | Human clinical cohort |
| Core phenotype: hypotonia | Hypotonia is highly prevalent from infancy | Hypotonia 37/39 (95%) (ng2016alg1‐cdgclinicaland pages 4-6) | HPO: Hypotonia (HP:0001252) | Human clinical cohort |
| Core phenotype: seizures/epilepsy | Seizures or epilepsy are highly prevalent | Seizures/epilepsy 36/38 (95%) (ng2016alg1‐cdgclinicaland pages 4-6) | HPO: Seizure (HP:0001250); Epilepsy (HP:0001250/label) | Human clinical cohort |
| Core phenotype: microcephaly | Microcephaly is common | Microcephaly 27/37 (73%) (ng2016alg1‐cdgclinicaland pages 4-6) | HPO: Microcephaly (HP:0000252) | Human clinical cohort |
| Core phenotype: intellectual disability | Intellectual disability is frequent among evaluable survivors | Intellectual disability 21/22 (95%) evaluable (ng2016alg1‐cdgclinicaland pages 4-6) | HPO: Intellectual disability (HP:0001249) | Human clinical cohort |
| Neuroimaging phenotype | Abnormal brain imaging is common, chiefly cerebral/cerebellar atrophy | Abnormal brain imaging 25/37 (68%); cerebral or cerebellar atrophy 11/25 (44% of abnormal scans) (ng2016alg1‐cdgclinicaland pages 4-6) | HPO: Abnormality of brain imaging; Cerebral atrophy (HP:0002059); Cerebellar atrophy (HP:0001272); UBERON: cerebrum, cerebellum | Human clinical cohort |
| Ocular phenotype | Ocular abnormalities are frequent | Ocular abnormalities 27/36 (75%); strabismus 10/27 (37%); nystagmus 6/27 (22%) (ng2016alg1‐cdgclinicaland pages 4-6) | HPO: Strabismus (HP:0000486); Nystagmus (HP:0000639); UBERON: eye | Human clinical cohort |
| Dysmorphism | Dysmorphic facial features are common | 24/39 (62%) (ng2016alg1‐cdgclinicaland pages 4-6) | HPO: Facial dysmorphism (label) | Human clinical cohort |
| Hematologic involvement | Hematologic defects are common but heterogeneous | 18/34 (53%) (ng2016alg1‐cdgclinicaland pages 4-6) | HPO: Hematologic abnormality (label); UBERON: blood | Human clinical cohort |
| Gastrointestinal involvement | GI disease is common and may include chronic diarrhea and protein-losing enteropathy | GI problems 20/38 (53%); among those with GI manifestations, chronic diarrhea 7/20 and PLE 5/20 (ng2016alg1‐cdgclinicaland pages 4-6) | HPO: Chronic diarrhea (HP:0002028); Protein-losing enteropathy (HP:0002242); UBERON: intestine | Human clinical cohort |
| Skeletal involvement | Skeletal abnormalities occur in about one-third | 13/39 (33%); scoliosis 5/13; kyphosis 2/13; joint contractures 3/13 (ng2016alg1‐cdgclinicaland pages 4-6) | HPO: Scoliosis (HP:0002650); Kyphosis (HP:0002808); Joint contracture (HP:0001371) | Human clinical cohort |
| Hypoalbuminemia / renal-enteric severity marker | Hypoalbuminemia marks severe multisystem disease and may reflect enteric or renal protein loss | Hypoalbuminemia 12/39 (31%); all 12 died, mean age at death 6.75 months; within this group PLE documented in 2 and renal disease in 3 (ng2016alg1‐cdgclinicaland pages 4-6) | HPO: Hypoalbuminemia (HP:0003073); Proteinuria/renal disease labels | Human clinical cohort |
| Prognosis / mortality | Mortality is high, especially in infancy and in specific genotypes | Premature death 17/39 (44%); deaths before 12 months 11/17 (65%); clinical range spans mild ID to death in first weeks/2 years (ng2016alg1‐cdgclinicaland pages 4-6, ng2016alg1‐cdgclinicaland pages 1-3) | HPO: Early death (label) | Human clinical cohort |
| Genotype-phenotype correlation | Homozygous p.Ser258Leu and compound heterozygous p.Gln50Arg are associated with particularly poor survival | All 6 homozygous p.Ser258Leu patients died within first 5 months; 4/5 with p.Gln50Arg compound heterozygosity died at 5–28 months (ng2016alg1‐cdgclinicaland pages 4-6, ng2016alg1‐cdgclinicaland pages 3-4) | Sequence variant labels; prognostic genotype annotation | Human clinical cohort |
| Diagnostic screening | Abnormal carbohydrate-deficient transferrin testing is a consistent screening clue in the major cohort, though normal transferrin can occur in some CDG and at least one later ALG1 case | 39/39 in Ng cohort had at least one abnormal CDT result; methods included ESI-MS and IEF. A later long-term series reported one ALG1-CDG patient with normal transferrin IEF (ng2016alg1‐cdgclinicaland pages 4-6, ng2016alg1‐cdgclinicaland pages 1-3, bogdanska2021clinicalbiochemicaland pages 6-8) | LOINC/HPO labels: abnormal transferrin glycosylation; UBERON: serum | Human clinical cohort + longitudinal center experience |
| Diagnostic biomarker | Xeno-tetrasaccharide NeuAc-Gal-GlcNAc2 is a high-value ALG1-associated biomarker useful to confirm diagnosis | Detected in all 27/27 tested ALG1-CDG patients in the 2016 cohort; present on either serum or fibroblast glycoproteins; prior studies detected it on ~2–8% of purified serum transferrin (ng2016alg1‐cdgclinicaland pages 1-3, ng2016alg1‐cdgclinicaland pages 6-8) | CHEBI labels: N-acetylglucosamine, galactose, sialic acid; biomarker label: NeuAc-Gal-GlcNAc2 | Human biochemical biomarker |
| Functional confirmation | Variant pathogenicity can be supported by yeast complementation rather than severity prediction | Human wild-type vs missense ALG1 constructs tested in temperature-sensitive alg1-deficient yeast for growth and CPY glycosylation rescue; authors caution assay does not rank clinical severity (ng2016alg1‐cdgclinicaland pages 1-3, ng2016alg1‐cdgclinicaland pages 4-6, ng2016alg1‐cdgclinicaland pages 10-13) | GO: carboxypeptidase Y glycosylation assay label; model: Saccharomyces cerevisiae | Functional model assay |
| Recent 2024 development | Targeted MRM proteomics in patient fibroblasts showed selective reduction of ALG1 protein abundance without broad compensatory changes in other ER glycosyltransferases | 3 ALG1-CDG fibroblast lines, all homozygous c.773C>T p.S258L, showed substantial reduction of ALG1 protein; other GT transcript/protein levels remained largely unchanged (lin2024targetedproteomicsreveals pages 1-2, lin2024targetedproteomicsreveals pages 4-6) | GO: proteomics; CL: fibroblast; protein abundance label | Human primary-cell proteomics (2024) |
| Epidemiology | Direct observed prevalence is not established; modeled birth prevalence is very low and varies by ancestry | Estimated prevalence from gnomAD/ClinVar model: NFE 1:881,984; AFR 1:329,069; AMR 1:2,981,452; EAS 1:2,543,998; SAS 1:1,559,334; ASJ 1:47,656; FIN 1:4,775,806; EST 1:3,882,716 (pajusalu2021theestimatedprevalence pages 3-4) | Epidemiology label; autosomal recessive rare disease | Computational population estimate |
| Treatment status | No ALG1-specific approved disease-modifying therapy was identified in retrieved evidence; management is supportive and complication-directed | No relevant ALG1-specific interventional trial or supplementation efficacy study was retrieved; supportive care inferred from multisystem complications such as epilepsy, feeding/GI, infection, renal/respiratory failure (ng2016alg1‐cdgclinicaland pages 4-6, zhao2025clinicalandgenetic pages 10-11) | MAXO labels: antiseizure therapy, nutritional support, infection management, respiratory support, rehabilitation (labels only) | Evidence gap + real-world supportive care inference |
| Prevention / family planning | Prevention is genetic rather than environmental: recurrence-risk counseling and reproductive testing are relevant | Later case literature documents prenatal diagnosis in an ALG1 family leading to a healthy subsequent pregnancy (zhao2025clinicalandgenetic pages 10-11) | Genetic counseling; prenatal diagnosis; carrier testing | Human case report |
| Environmental factors | No disease-specific environmental or infectious cause established; this is a Mendelian disorder | No validated environmental triggers/protective factors found in retrieved ALG1-specific evidence | Not applicable / no confident ontology term | Evidence gap |
| Anatomical systems affected | Multisystem disease with primary nervous system involvement and frequent eye, GI, hematologic, skeletal, renal, and respiratory complications | Quantitative system involvement summarized above; causes of death included respiratory failure, renal failure, and infections leading to sepsis (ng2016alg1‐cdgclinicaland pages 4-6) | UBERON: brain, eye, intestine, kidney, blood, skeletal system; CL labels as needed | Human clinical cohort |
| Other species / natural disease | No naturally occurring veterinary ALG1-CDG identified in retrieved evidence | No specific animal natural-disease reports found | NCBI Taxon: not established | Evidence gap |
| Models / evidence gaps | Available disease-relevant models are yeast and patient fibroblasts; no validated ALG1-specific vertebrate model, single-cell, spatial transcriptomic, or disease-specific multi-omics atlas was identified in retrieved evidence | Yeast temperature-sensitive alg1 model and patient fibroblasts available; no relevant ALG1 clinical trials found; no single-cell/spatial studies identified (ng2016alg1‐cdgclinicaland pages 1-3, ng2016alg1‐cdgclinicaland pages 6-8, lin2024targetedproteomicsreveals pages 1-2, lin2024targetedproteomicsreveals pages 4-6) | Model system labels: Saccharomyces cerevisiae, fibroblast | Model organism / in vitro + evidence gap |


*Table: This table compiles high-confidence, disease-specific findings for ALG1-CDG across identifiers, genetics, phenotypes, mechanism, biomarkers, prognosis, epidemiology, and current evidence gaps. It is designed as a compact knowledge-base artifact with quantitative evidence and ontology-oriented annotations.*

## 1. Disease information

### Definition and nomenclature

ALG1-CDG is a congenital disorder of glycosylation affecting the assembly of the dolichol-linked precursor for protein N-glycosylation. It was formerly called **congenital disorder of glycosylation type Ik**, **CDG-Ik**, or **GDP-mannose:GlcNAc₂-PP-dolichol mannosyltransferase deficiency**. The landmark clinical series describes it as a rare autosomal-recessive disorder whose spectrum extends from mild intellectual disability to death in the first weeks of life. (ng2016alg1‐cdgclinicaland pages 1-3)

**Identifiers supported by the retrieved literature**

- Disease: **OMIM/MIM 608540**.
- Gene: **ALG1**, OMIM/MIM **605907**; transcript used in the major cohort: **NM_019109.4**.
- Former designation: **CDG-Ik**.
- MONDO: ALG1-CDG is represented in MONDO, but an exact MONDO identifier was not verified in the retrieved primary literature and should be validated directly against the current MONDO release before database import.
- Orphanet, MeSH, ICD-10, and ICD-11: no disease-specific code was established from the retrieved primary sources. In clinical coding, it may be grouped under congenital glycosylation/metabolic disorders rather than a uniquely specific ICD code.

The evidence summarized here is principally **aggregated disease-level evidence** from international cohorts and laboratory studies, not individual EHR-derived data. Individual case reports are used only where explicitly noted.

## 2. Etiology, risk, and protective factors

### Causal factor

The sole established cause is **germline biallelic pathogenic variation in ALG1**. ALG1 encodes an ER-localized β1,4-mannosyltransferase that transfers the first of nine mannose residues onto the growing dolichol-linked oligosaccharide. The disorder is therefore a monogenic, autosomal-recessive inborn error of glycoprotein biosynthesis. (ng2016alg1‐cdgclinicaland pages 1-3)

### Genetic risk

Each child of two heterozygous carriers has, per pregnancy, a 25% probability of being affected, a 50% probability of being an unaffected carrier, and a 25% probability of inheriting neither familial variant. Penetrance appears high for clearly pathogenic biallelic genotypes, but clinical expressivity is markedly variable.

The 2016 cohort identified 31 candidate disease variants, 26/31 (84%) of which were novel at that time. Twenty-two were absent from ExAC and nine occurred only at very low heterozygous frequencies. The recurrent **c.773C>T (p.Ser258Leu)** allele occurred in 17/39 patients. (ng2016alg1‐cdgclinicaland pages 3-4)

### Environmental, lifestyle, infectious, and protective factors

No toxin, diet, lifestyle, infection, age, or sex exposure causes ALG1-CDG. Likewise, no validated protective allele, dietary factor, or gene–environment interaction has been demonstrated. Environmental events can alter complications—for example, infections may precipitate sepsis in medically fragile infants—but they do not constitute the primary etiology. Deaths in the major cohort included respiratory or renal failure and infections progressing to sepsis. (ng2016alg1‐cdgclinicaland pages 4-6)

## 3. Phenotypes

The best quantitative estimates come from Ng et al., published July 2016 in *Human Mutation* (DOI: [10.1002/humu.22983](https://doi.org/10.1002/humu.22983)). This was a clinically ascertained cohort of 39 patients and may overrepresent severe disease. (ng2016alg1‐cdgclinicaland pages 4-6)

### Neurologic and developmental phenotypes

- **Global developmental delay:** 37/37, 100%; usually evident in infancy or early childhood; severity variable. Suggested HPO: **HP:0001263**.
- **Hypotonia:** 37/39, 95%; commonly early and persistent. HPO: **HP:0001252**.
- **Seizures/epilepsy:** 36/38, 95%; may be severe or drug-resistant. HPO: **HP:0001250**.
- **Intellectual disability:** 21/22 evaluable patients, 95%; assessment was limited in patients who died young. HPO: **HP:0001249**.
- **Microcephaly:** 27/37, 73%. HPO: **HP:0000252**.
- **Abnormal brain imaging:** 25/37, 68%; cerebral or cerebellar atrophy accounted for 11/25 abnormal scans. Suggested HPO: cerebral atrophy **HP:0002059**; cerebellar atrophy **HP:0001272**. (ng2016alg1‐cdgclinicaland pages 4-6)

These findings profoundly affect quality of life: most affected children require assistance with mobility, communication, feeding, medication administration, and activities of daily living. No ALG1-specific EQ-5D, SF-36, PROMIS, or caregiver-burden study was identified.

### Ocular and craniofacial findings

Ocular abnormalities occurred in 27/36 patients (75%), including strabismus in 10/27 and nystagmus in 6/27. Suggested HPO terms are **HP:0000486** and **HP:0000639**, respectively. Dysmorphic facial features occurred in 24/39 (62%), but no single facial gestalt is sufficiently specific for diagnosis. (ng2016alg1‐cdgclinicaland pages 4-6)

### Gastrointestinal, nutritional, renal, and biochemical findings

Gastrointestinal problems occurred in 20/38 patients (53%). Within the 20 affected patients, chronic diarrhea occurred in seven and protein-losing enteropathy in five. Suggested HPO terms include chronic diarrhea **HP:0002028** and protein-losing enteropathy **HP:0002242**. (ng2016alg1‐cdgclinicaland pages 4-6)

Hypoalbuminemia occurred in 12/39 (31%) and was a particularly adverse marker: all 12 patients died, at a mean age of 6.75 months. Two had documented protein-losing enteropathy and three had renal disease, indicating that enteric and renal protein loss can both contribute. Suggested HPO: hypoalbuminemia **HP:0003073**, proteinuria **HP:0000093**. (ng2016alg1‐cdgclinicaland pages 4-6)

### Hematologic and skeletal findings

Hematologic abnormalities occurred in 18/34 patients (53%), although the cohort summary did not define one uniform defect. Skeletal abnormalities occurred in 13/39 (33%): scoliosis in 5/13, kyphosis in 2/13, and joint contractures in 3/13. Suggested HPO terms are scoliosis **HP:0002650**, kyphosis **HP:0002808**, and joint contracture **HP:0001371**. (ng2016alg1‐cdgclinicaland pages 4-6)

### Other reported involvement

Liver dysfunction, respiratory disease, renal disease, feeding difficulty/failure to thrive, and susceptibility to serious infections have been reported variably. A later Chinese case had drug-resistant epilepsy, facial dysmorphism, abnormal liver function, and death at 14 months, illustrating continuing recognition of severe infantile disease. (zhao2025clinicalandgenetic pages 10-11)

## 4. Genetic and molecular information

### Gene and variant mechanism

**ALG1** encodes a polytopic ER membrane glycosyltransferase. Most established disease alleles are missense, splice-site, nonsense, frameshift, or small insertion/deletion variants producing absent, unstable, or catalytically impaired enzyme. Disease-causing variants are germline, not somatic. The likely unifying mechanism is **loss of function or severe hypomorphism**, rather than gain of function or dominant-negative activity.

Known variants in the 2016 cohort included p.Ser150Arg, p.Ser258Leu, p.Arg276Trp, p.Ser359Leu, and p.Arg438Trp, plus 26 newly reported variants. Because many variants are individually extremely rare or absent from population databases, current allele frequencies and ClinVar classifications should be checked variant-by-variant at the time of interpretation. (ng2016alg1‐cdgclinicaland pages 3-4)

A 2025 case illustrates contemporary ACMG classification: **c.328C>A (p.Gln110Lys)** was classified likely pathogenic and **c.863-2A>G** pathogenic in a compound-heterozygous child. This is supportive case evidence rather than a 2023–2024 development. (zhao2025clinicalandgenetic pages 10-11)

### Genotype–phenotype relationships

- All six patients homozygous for **p.Ser258Leu** died within the first five months. Two previously reported homozygotes died at two and 11 weeks.
- Four of five patients compound heterozygous for **p.Gln50Arg** died between five and 28 months, irrespective of the second allele.
- Yeast complementation can establish functional impairment but did not reliably rank human clinical severity. The authors explicitly cautioned that yeast assays should be used “as a tool for determining pathogenicity, not clinical severity.” (ng2016alg1‐cdgclinicaland pages 4-6)

No validated modifier gene, epigenetic signature, anticipation, or recurrent disease-causing chromosomal rearrangement has been established. Large deletions encompassing ALG1 are theoretically detectable but are not the characteristic mechanism.

## 5. Environmental information

ALG1-CDG is not an environmentally acquired, infectious, toxic, radiation-associated, occupational, or lifestyle-mediated disorder. Smoking, alcohol, exercise, or diet have no established role in disease occurrence. Nutrition and infection exposure can influence morbidity after disease onset, particularly in patients with feeding problems, protein loss, respiratory compromise, or immune vulnerability, but this represents complication modification rather than gene–environment causation.

## 6. Mechanism and pathophysiology

### Upstream causal chain

1. **Biallelic ALG1 variants** reduce ALG1 abundance, stability, GDP-mannose interaction, complex formation, or catalytic activity.
2. The ALG1-dependent addition of the first mannose to **Dol-PP-GlcNAc₂** on the cytoplasmic ER face is impaired.
3. Full-length **Glc₃Man₉GlcNAc₂** lipid-linked oligosaccharide synthesis is reduced.
4. Nascent proteins receive too few glycans or unusually truncated glycans through the oligosaccharyltransferase complex.
5. Aberrant glycoprotein folding, stability, trafficking, receptor function, cell adhesion, and secretion affect many tissues, producing the neurologic and systemic phenotype. (ng2016alg1‐cdgclinicaland pages 1-3, lin2024targetedproteomicsreveals pages 1-2)

The early N-glycosylation machinery includes ALG1, ALG2, and ALG11, which sequentially add five cytoplasmic-side mannoses and can form heteromeric complexes. Suggested GO concepts include **protein N-linked glycosylation**, **dolichol-linked oligosaccharide biosynthetic process**, **mannosyltransferase activity**, and ER membrane localization. (ng2016alg1‐cdgclinicaland pages 6-8, lin2024targetedproteomicsreveals pages 1-2)

### Xeno-tetrasaccharide formation

ALG1 deficiency permits some Dol-PP-GlcNAc₂ to cross into the ER lumen and be transferred to protein. After Golgi transit, β1,4-galactosyltransferase adds galactose and an α2,6-sialyltransferase caps the structure, generating **NeuAcα2,6-Galβ1,4-GlcNAcβ1,4-GlcNAc**. This structure does not normally occur in mammals and is found principally in ALG1-CDG, although trace amounts may occur in PMM2-CDG and MPI-CDG. (ng2016alg1‐cdgclinicaland pages 6-8)

### Cellular and tissue effects

Direct cell-type-specific causal maps remain unavailable. Neurons and developing neural circuits appear particularly vulnerable, inferred from the near-universal neurodevelopmental phenotype. Hepatocytes, intestinal epithelium, renal glomerular/tubular cells, hematopoietic cells, ocular tissues, skeletal muscle, and connective tissue are plausible affected populations because their secreted and membrane proteins depend heavily on N-glycosylation. These cell assignments are mechanistic inferences, not single-cell evidence.

Suggested CL labels include neuron, astrocyte, hepatocyte, intestinal epithelial cell, renal epithelial cell, skeletal muscle cell, fibroblast, and hematopoietic cell. Suggested GO cellular components are **endoplasmic reticulum membrane**, **ER lumen**, **Golgi apparatus**, and **oligosaccharyltransferase complex**.

### Recent 2024 proteomics

A targeted multiple-reaction-monitoring study published **18 January 2024** analyzed primary fibroblasts from eight type-I CDG patients, including three ALG1-CDG lines homozygous for c.773C>T, p.Ser258Leu. It found substantial reduction of the corresponding ALG1 protein, while other measured glycosyltransferases remained largely unchanged at transcript and protein levels. The authors concluded that there is no evident compensatory “fail-safe mechanism” for these early ER glycosylation steps. DOI: [10.3390/ijms25021191](https://doi.org/10.3390/ijms25021191). (lin2024targetedproteomicsreveals pages 1-2, lin2024targetedproteomicsreveals pages 4-6)

No ALG1-CDG-specific single-cell atlas, spatial-transcriptomic study, lipidomics profile, comprehensive metabolomics signature, CRISPR screen, or integrated multi-omics analysis was identified.

## 7. Anatomical structures affected

The **central nervous system** is the dominant organ system, particularly the cerebrum and cerebellum. Other affected structures include the eye, gastrointestinal tract, liver, kidneys, blood/hematopoietic system, skeletal system, skeletal muscle, respiratory system, and possibly heart in individual patients. (ng2016alg1‐cdgclinicaland pages 4-6)

Suggested UBERON labels include brain, cerebral cortex, cerebellum, eye, liver, small intestine, colon, kidney, blood, skeletal muscle, bone, and lung. At the subcellular level, the primary lesion is in the **ER membrane**, with downstream processing in the Golgi. Lateralization is not characteristic; manifestations are systemic or bilateral rather than unilateral.

## 8. Temporal development and natural history

ALG1-CDG is genetically present from conception. Severe cases manifest prenatally, neonatally, or in early infancy with hypotonia, feeding problems, seizures, developmental impairment, dysmorphism, protein loss, or organ dysfunction. Milder cases may first be recognized through delayed development or epilepsy.

The course is chronic and lifelong in survivors. Neurologic impairment is generally persistent; systemic complications may be episodic or progressive. There is no validated staging system or evidence for spontaneous remission. The major critical period is infancy: 11/17 deaths in the cohort occurred before 12 months, and all six p.Ser258Leu homozygotes died before five months. (ng2016alg1‐cdgclinicaland pages 4-6)

## 9. Inheritance and population epidemiology

### Inheritance

Inheritance is **autosomal recessive**. The cohort’s 17 male and 22 female patients provide no evidence of sex-linked risk. Variable expressivity is clear; anticipation is not expected. Germline mosaicism is theoretically possible for any Mendelian disorder but has not emerged as a characteristic ALG1-CDG mechanism. Consanguinity increases the probability that two carriers of the same rare allele have affected offspring, but no single global founder effect is established. (ng2016alg1‐cdgclinicaland pages 4-6)

### Epidemiology

No robust observed incidence or prevalence registry estimate is available. A 2021 allele-frequency model using gnomAD and ClinVar estimated birth prevalence as follows:

- non-Finnish European: **1:881,984**;
- African/African American: **1:329,069**;
- Latino/Admixed American: **1:2,981,452**;
- East Asian: **1:2,543,998**;
- South Asian: **1:1,559,334**;
- Ashkenazi Jewish: **1:47,656**;
- Finnish: **1:4,775,806**;
- Estonian: **1:3,882,716**. (pajusalu2021theestimatedprevalence pages 3-4)

These are computational estimates, not screened-population observations. They assume Hardy–Weinberg equilibrium and accurate variant classification, omit many structural/regulatory or ultra-rare variants, and may over- or underestimate viable disease genotypes. The apparently higher Ashkenazi estimate requires epidemiologic validation.

## 10. Diagnostics

### Recommended diagnostic approach

1. **Clinical suspicion:** infantile developmental delay, hypotonia, epilepsy, microcephaly, abnormal brain imaging, dysmorphism, failure to thrive, diarrhea/protein-losing enteropathy, hypoalbuminemia, liver or renal abnormalities.
2. **Biochemical screening:** serum transferrin glycoform analysis by isoelectric focusing, capillary electrophoresis, HPLC, or electrospray-ionization mass spectrometry. A type-I pattern indicates deficient assembly or transfer of the lipid-linked oligosaccharide but is not gene-specific. In the 2016 cohort, all 39 patients had at least one abnormal carbohydrate-deficient transferrin result. (ng2016alg1‐cdgclinicaland pages 4-6)
3. **ALG1-associated glycan testing:** mass-spectrometric detection of NeuAc-Gal-GlcNAc₂ on transferrin or total glycoproteins. It was present in all 27 tested cohort patients and on approximately 2–8% of purified transferrin in prior biomarker studies. (ng2016alg1‐cdgclinicaland pages 1-3, ng2016alg1‐cdgclinicaland pages 6-8)
4. **Molecular confirmation:** identify pathogenic/likely pathogenic variants in trans by a CDG panel, exome sequencing, genome sequencing, or ALG1 sequencing with deletion/duplication analysis.
5. **Orthogonal confirmation:** segregation testing, RNA analysis for splice variants, glycomics, protein abundance, or functional complementation when variant interpretation remains uncertain.

A normal transferrin result does not absolutely exclude a CDG. A 2021 long-term series reported one molecularly diagnosed ALG1-CDG patient with normal transferrin IEF; moreover, an ALG1 p.Thr64Asn VUS with normal transferrin and absent tetrasaccharide was excluded from the major cohort despite abnormal yeast assays, illustrating why biochemical, molecular, and functional data must be integrated. (ng2016alg1‐cdgclinicaland pages 6-8, bogdanska2021clinicalbiochemicaland pages 6-8)

### Role of genomic methods

- **Single-gene testing:** reasonable when the biochemical xeno-tetrasaccharide strongly implicates ALG1 or familial variants are known.
- **CDG/multisystem panels:** efficient when transferrin indicates type-I CDG but the subtype is unclear.
- **WES/WGS:** appropriate for atypical or biochemically equivocal presentations; WGS can better detect noncoding, copy-number, and structural variants.
- **CMA, karyotype, FISH, mitochondrial DNA, and repeat-expansion testing:** not first-line tests for isolated suspected ALG1-CDG unless the phenotype suggests an alternative diagnosis.
- **RNA sequencing:** potentially useful for splice or expression variants, but not an established routine ALG1 assay.

### Baseline phenotyping after diagnosis

Reasonable assessments include neurologic examination, developmental evaluation, EEG for suspected seizures, brain MRI, ophthalmology, feeding and swallowing assessment, growth and nutrition review, serum albumin/total protein, liver enzymes, coagulation studies, CBC, urinalysis/protein quantification, renal function, and respiratory/infection review. Cardiac evaluation should be guided by symptoms and broader CDG practice.

### Differential diagnosis

The principal differential includes other type-I N-glycosylation disorders—especially PMM2-CDG, MPI-CDG, ALG2-CDG, ALG6-CDG, ALG8-CDG, ALG11-CDG, DPAGT1-CDG, and defects in dolichol-linked oligosaccharide synthesis. Protein-losing enteropathy may suggest MPI-, ALG6-, or ALG8-CDG, while the NeuAc-Gal-GlcNAc₂ marker and biallelic ALG1 variants favor ALG1-CDG. (ng2016alg1‐cdgclinicaland pages 4-6, ng2016alg1‐cdgclinicaland pages 6-8)

There is no established population newborn screening program. Targeted carrier screening, cascade testing, prenatal diagnosis, and preimplantation genetic testing are possible once familial variants are known.

## 11. Outcome and prognosis

The best available cohort estimate is **44% premature mortality (17/39)**; 11/17 deaths occurred before 12 months. Causes included respiratory failure, renal failure, and infections leading to sepsis. This is not a population survival curve and likely reflects referral/ascertainment bias. No reliable 5- or 10-year survival statistic or average life expectancy is available. (ng2016alg1‐cdgclinicaland pages 4-6)

Poor prognostic indicators include homozygous p.Ser258Leu, compound heterozygosity involving p.Gln50Arg, hypoalbuminemia, protein-losing enteropathy or renal protein loss, respiratory compromise, recurrent infection/sepsis, and severe early-onset epilepsy. All 12 hypoalbuminemic patients died at a mean age of 6.75 months. (ng2016alg1‐cdgclinicaland pages 4-6)

Survivors commonly have substantial long-term neurodevelopmental disability. Recovery to normal function has not been documented as an expected outcome, although symptom control, nutrition, mobility, communication, and family quality of life may improve with intensive supportive care.

## 12. Treatment and real-world management

### Treatment status

No approved ALG1-specific disease-modifying therapy, validated substrate supplementation, gene therapy, RNA therapy, cell therapy, or pharmacologic chaperone was identified. Mannose treatment used in **MPI-CDG** and galactose used in selected other CDGs should not be assumed effective for ALG1-CDG; a long-term CDG series documented biochemical improvement for MPI- and PGM1-CDG, not ALG1-CDG. (bogdanska2021clinicalbiochemicaland pages 6-8)

No ALG1-specific interventional ClinicalTrials.gov study was returned by the trial search. Thus, present treatment is supportive and individualized.

### Suggested management and MAXO-oriented annotations

- **Epilepsy:** standard genotype-independent antiseizure medication selection; rescue plan for prolonged seizures. Suggested MAXO: antiseizure-agent therapy, EEG monitoring.
- **Feeding/nutrition:** dietitian review, texture modification, swallow study, high-calorie support, enteral feeding when necessary. Suggested MAXO: nutritional supplementation, gastrostomy placement, swallowing assessment.
- **Protein loss:** monitor albumin, edema, stool/renal protein loss; treat underlying enteropathy or renal complications and provide albumin/support when clinically indicated.
- **Development:** early physical, occupational, speech/communication, and feeding therapies. Suggested MAXO: physical therapy, occupational therapy, speech therapy.
- **Vision:** ophthalmologic surveillance and treatment of strabismus/refractive problems.
- **Orthopedics:** monitor scoliosis, kyphosis, contractures, positioning, and bone health; use bracing or surgery according to standard indications.
- **Respiratory/infectious care:** airway-clearance and aspiration prevention when needed; prompt evaluation and treatment of infection; respiratory support in severe disease.
- **Renal/hepatic/hematologic care:** periodic laboratory and specialist surveillance tailored to baseline abnormalities.
- **Palliative care:** appropriate early in life-limiting genotypes or severe multisystem disease, alongside active treatment.

No ALG1-specific response rates, comparative treatment outcomes, or pharmacogenomic recommendations are available.

## 13. Prevention

Primary lifestyle prevention is not applicable because ALG1-CDG is genetic. Effective prevention options are reproductive:

- genetic counseling and parental carrier confirmation;
- cascade testing of at-risk relatives;
- prenatal diagnosis by chorionic-villus sampling or amniocentesis for known familial variants;
- preimplantation genetic testing for monogenic disease;
- donor gametes or other family-planning alternatives.

A later case series documented prenatal diagnosis in an ALG1 family followed by a healthy subsequent pregnancy. (zhao2025clinicalandgenetic pages 10-11)

Secondary prevention consists of early molecular diagnosis and prompt management of seizures, feeding problems, protein loss, aspiration, respiratory decline, renal dysfunction, and infection. Tertiary prevention includes rehabilitation, contracture/scoliosis prevention, nutritional support, vaccination according to routine schedules, and caregiver education. No disease-specific vaccine or pharmacologic prophylaxis exists.

## 14. Other species and natural disease

ALG1 and the early N-glycosylation pathway are evolutionarily conserved. Nevertheless, no well-characterized naturally occurring veterinary ALG1-CDG in a companion-animal breed or wildlife species was identified. There is no zoonotic potential or cross-species transmission because this is an inherited metabolic disorder.

## 15. Model organisms and experimental systems

### Yeast

Temperature-sensitive **Saccharomyces cerevisiae alg1** mutants are the principal functional model. At restrictive temperature they accumulate Dol-PP-GlcNAc₂ and can transfer GlcNAc₂ to glycoproteins. Human ALG1 variants can be tested for rescue of yeast growth and carboxypeptidase-Y glycosylation. This assay supported pathogenicity for variants in the 2016 study, but its biochemical severity did not correlate reliably with human outcomes. (ng2016alg1‐cdgclinicaland pages 4-6, ng2016alg1‐cdgclinicaland pages 10-13)

### Human cellular models

Patient-derived skin fibroblasts demonstrate abnormal glycosylation, the xeno-tetrasaccharide, and variant-dependent ALG1 protein instability. Attempts to generate a homozygous ALG1-indel human cell line by CRISPR/Cas9 failed despite targeting four exons, suggesting that complete ALG1 loss may be incompatible with cell viability. (ng2016alg1‐cdgclinicaland pages 4-6)

The 2024 MRM-proteomics assay offers a reproducible method to quantify low-abundance ER glycosyltransferases. In three p.Ser258Leu-homozygous ALG1-CDG fibroblast lines, ALG1 protein was substantially reduced without broad upregulation of other pathway enzymes. (lin2024targetedproteomicsreveals pages 1-2, lin2024targetedproteomicsreveals pages 4-6)

### Vertebrate and advanced models

No validated ALG1-CDG-specific mouse, rat, zebrafish, medaka, organoid, or iPSC model with demonstrated recapitulation of the human phenotype was identified in the retrieved literature. This is a major translational gap. Patient iPSC-derived neurons, liver/intestinal organoids, and viable hypomorphic vertebrate knock-in models would be particularly valuable for defining tissue vulnerability and screening therapies.

## Evidence quality and current research priorities

The strongest disease-specific evidence remains the 2016 international 39-patient cohort and associated biochemical studies. Its exact abstract states that the xeno-tetrasaccharide “**was seen in all twenty-seven patients tested**” and that the study “**triples the number of known patients and expands the molecular and clinical correlates of this disorder**.” (ng2016alg1‐cdgclinicaland pages 1-3)

Recent 2023–2024 ALG1-specific clinical research was sparse. The most substantive 2024 development was targeted proteomic confirmation that ALG1-deficient fibroblasts have reduced ALG1 protein without compensatory increases in other ER glycosyltransferases. Priorities now include prospective natural-history registries, standardized outcome measures, longitudinal glycomics, updated variant curation, disease-specific quality-of-life studies, viable vertebrate and organoid models, and preclinical testing of gene replacement, mRNA delivery, or variant-directed stabilization strategies. (lin2024targetedproteomicsreveals pages 1-2, lin2024targetedproteomicsreveals pages 4-6)

### Key primary references

1. Ng BG et al. **ALG1-CDG: Clinical and molecular characterization of 39 unreported patients.** *Human Mutation*. Published July 2016;37:653–660. DOI: [10.1002/humu.22983](https://doi.org/10.1002/humu.22983). (ng2016alg1‐cdgclinicaland pages 1-3)
2. Grubenmann CE et al. **Deficiency of the first mannosylation step in the N-glycosylation pathway causes CDG-Ik.** *Human Molecular Genetics*. 2004;13:535–542. PMID **14709599**. (ng2016alg1‐cdgclinicaland pages 10-13)
3. Kranz C et al. **CDG-Ik: a defect of mannosyltransferase I.** *American Journal of Human Genetics*. 2004;74:545–551. PMID **14973782**. (ng2016alg1‐cdgclinicaland pages 10-13)
4. Schwarz M et al. **Deficiency of GDP-Man:GlcNAc₂-PP-dolichol mannosyltransferase causes CDG-Ik.** *American Journal of Human Genetics*. 2004;74:472–481. PMID **14973778**. (ng2016alg1‐cdgclinicaland pages 10-13)
5. Dupré T et al. **Mannosyltransferase deficiency: five new patients and seven novel mutations.** *Journal of Medical Genetics*. 2010;47:729–735. PMID **20679665**. (ng2016alg1‐cdgclinicaland pages 10-13)
6. Morava E et al. **Defining the phenotype in congenital disorder of glycosylation due to ALG1 mutations.** *Pediatrics*. 2012;130:e1034–e1039. PMID **22966035**. (ng2016alg1‐cdgclinicaland pages 10-13)
7. Sakson R et al. **Targeted Proteomics Reveals Quantitative Differences in Low-Abundance Glycosyltransferases of Patients with CDG.** *International Journal of Molecular Sciences*. Published 18 January 2024;25:1191. DOI: [10.3390/ijms25021191](https://doi.org/10.3390/ijms25021191). (lin2024targetedproteomicsreveals pages 1-2)

References

1. (ng2016alg1‐cdgclinicaland pages 4-6): Bobby G. Ng, Sergey A. Shiryaev, Daisy Rymen, Erik A. Eklund, Kimiyo Raymond, Martin Kircher, Jose E. Abdenur, Fusun Alehan, Alina T. Midro, Michael J. Bamshad, Rita Barone, Gerard T. Berry, Jane E. Brumbaugh, Kati J. Buckingham, Katie Clarkson, F. Sessions Cole, Shawn O'Connor, Gregory M. Cooper, Rudy Van Coster, Laurie A. Demmer, Luisa Diogo, Alexander J. Fay, Can Ficicioglu, Agata Fiumara, William A. Gahl, Rebecca Ganetzky, Himanshu Goel, Lyndsay A. Harshman, Miao He, Jaak Jaeken, Philip M. James, Daniel Katz, Liesbeth Keldermans, Maria Kibaek, Andrew J. Kornberg, Katherine Lachlan, Christina Lam, Joy Yaplito-Lee, Deborah A. Nickerson, Heidi L. Peters, Valerie Race, Luc Régal, Jeffrey S. Rush, S. Lane Rutledge, Jay Shendure, Erika Souche, Susan E. Sparks, Pamela Trapane, Amarilis Sanchez-Valle, Eric Vilain, Arve Vøllo, Charles J. Waechter, Raymond Y. Wang, Lynne A. Wolfe, Derek A. Wong, Tim Wood, Amy C. Yang, Gert Matthijs, and Hudson H. Freeze. Alg1‐cdg: clinical and molecular characterization of 39 unreported patients. Human Mutation, 37:653-660, Jul 2016. URL: https://doi.org/10.1002/humu.22983, doi:10.1002/humu.22983. This article has 73 citations and is from a domain leading peer-reviewed journal.

2. (ng2016alg1‐cdgclinicaland pages 1-3): Bobby G. Ng, Sergey A. Shiryaev, Daisy Rymen, Erik A. Eklund, Kimiyo Raymond, Martin Kircher, Jose E. Abdenur, Fusun Alehan, Alina T. Midro, Michael J. Bamshad, Rita Barone, Gerard T. Berry, Jane E. Brumbaugh, Kati J. Buckingham, Katie Clarkson, F. Sessions Cole, Shawn O'Connor, Gregory M. Cooper, Rudy Van Coster, Laurie A. Demmer, Luisa Diogo, Alexander J. Fay, Can Ficicioglu, Agata Fiumara, William A. Gahl, Rebecca Ganetzky, Himanshu Goel, Lyndsay A. Harshman, Miao He, Jaak Jaeken, Philip M. James, Daniel Katz, Liesbeth Keldermans, Maria Kibaek, Andrew J. Kornberg, Katherine Lachlan, Christina Lam, Joy Yaplito-Lee, Deborah A. Nickerson, Heidi L. Peters, Valerie Race, Luc Régal, Jeffrey S. Rush, S. Lane Rutledge, Jay Shendure, Erika Souche, Susan E. Sparks, Pamela Trapane, Amarilis Sanchez-Valle, Eric Vilain, Arve Vøllo, Charles J. Waechter, Raymond Y. Wang, Lynne A. Wolfe, Derek A. Wong, Tim Wood, Amy C. Yang, Gert Matthijs, and Hudson H. Freeze. Alg1‐cdg: clinical and molecular characterization of 39 unreported patients. Human Mutation, 37:653-660, Jul 2016. URL: https://doi.org/10.1002/humu.22983, doi:10.1002/humu.22983. This article has 73 citations and is from a domain leading peer-reviewed journal.

3. (ng2016alg1‐cdgclinicaland pages 6-8): Bobby G. Ng, Sergey A. Shiryaev, Daisy Rymen, Erik A. Eklund, Kimiyo Raymond, Martin Kircher, Jose E. Abdenur, Fusun Alehan, Alina T. Midro, Michael J. Bamshad, Rita Barone, Gerard T. Berry, Jane E. Brumbaugh, Kati J. Buckingham, Katie Clarkson, F. Sessions Cole, Shawn O'Connor, Gregory M. Cooper, Rudy Van Coster, Laurie A. Demmer, Luisa Diogo, Alexander J. Fay, Can Ficicioglu, Agata Fiumara, William A. Gahl, Rebecca Ganetzky, Himanshu Goel, Lyndsay A. Harshman, Miao He, Jaak Jaeken, Philip M. James, Daniel Katz, Liesbeth Keldermans, Maria Kibaek, Andrew J. Kornberg, Katherine Lachlan, Christina Lam, Joy Yaplito-Lee, Deborah A. Nickerson, Heidi L. Peters, Valerie Race, Luc Régal, Jeffrey S. Rush, S. Lane Rutledge, Jay Shendure, Erika Souche, Susan E. Sparks, Pamela Trapane, Amarilis Sanchez-Valle, Eric Vilain, Arve Vøllo, Charles J. Waechter, Raymond Y. Wang, Lynne A. Wolfe, Derek A. Wong, Tim Wood, Amy C. Yang, Gert Matthijs, and Hudson H. Freeze. Alg1‐cdg: clinical and molecular characterization of 39 unreported patients. Human Mutation, 37:653-660, Jul 2016. URL: https://doi.org/10.1002/humu.22983, doi:10.1002/humu.22983. This article has 73 citations and is from a domain leading peer-reviewed journal.

4. (ng2016alg1‐cdgclinicaland pages 10-13): Bobby G. Ng, Sergey A. Shiryaev, Daisy Rymen, Erik A. Eklund, Kimiyo Raymond, Martin Kircher, Jose E. Abdenur, Fusun Alehan, Alina T. Midro, Michael J. Bamshad, Rita Barone, Gerard T. Berry, Jane E. Brumbaugh, Kati J. Buckingham, Katie Clarkson, F. Sessions Cole, Shawn O'Connor, Gregory M. Cooper, Rudy Van Coster, Laurie A. Demmer, Luisa Diogo, Alexander J. Fay, Can Ficicioglu, Agata Fiumara, William A. Gahl, Rebecca Ganetzky, Himanshu Goel, Lyndsay A. Harshman, Miao He, Jaak Jaeken, Philip M. James, Daniel Katz, Liesbeth Keldermans, Maria Kibaek, Andrew J. Kornberg, Katherine Lachlan, Christina Lam, Joy Yaplito-Lee, Deborah A. Nickerson, Heidi L. Peters, Valerie Race, Luc Régal, Jeffrey S. Rush, S. Lane Rutledge, Jay Shendure, Erika Souche, Susan E. Sparks, Pamela Trapane, Amarilis Sanchez-Valle, Eric Vilain, Arve Vøllo, Charles J. Waechter, Raymond Y. Wang, Lynne A. Wolfe, Derek A. Wong, Tim Wood, Amy C. Yang, Gert Matthijs, and Hudson H. Freeze. Alg1‐cdg: clinical and molecular characterization of 39 unreported patients. Human Mutation, 37:653-660, Jul 2016. URL: https://doi.org/10.1002/humu.22983, doi:10.1002/humu.22983. This article has 73 citations and is from a domain leading peer-reviewed journal.

5. (ng2016alg1‐cdgclinicaland pages 3-4): Bobby G. Ng, Sergey A. Shiryaev, Daisy Rymen, Erik A. Eklund, Kimiyo Raymond, Martin Kircher, Jose E. Abdenur, Fusun Alehan, Alina T. Midro, Michael J. Bamshad, Rita Barone, Gerard T. Berry, Jane E. Brumbaugh, Kati J. Buckingham, Katie Clarkson, F. Sessions Cole, Shawn O'Connor, Gregory M. Cooper, Rudy Van Coster, Laurie A. Demmer, Luisa Diogo, Alexander J. Fay, Can Ficicioglu, Agata Fiumara, William A. Gahl, Rebecca Ganetzky, Himanshu Goel, Lyndsay A. Harshman, Miao He, Jaak Jaeken, Philip M. James, Daniel Katz, Liesbeth Keldermans, Maria Kibaek, Andrew J. Kornberg, Katherine Lachlan, Christina Lam, Joy Yaplito-Lee, Deborah A. Nickerson, Heidi L. Peters, Valerie Race, Luc Régal, Jeffrey S. Rush, S. Lane Rutledge, Jay Shendure, Erika Souche, Susan E. Sparks, Pamela Trapane, Amarilis Sanchez-Valle, Eric Vilain, Arve Vøllo, Charles J. Waechter, Raymond Y. Wang, Lynne A. Wolfe, Derek A. Wong, Tim Wood, Amy C. Yang, Gert Matthijs, and Hudson H. Freeze. Alg1‐cdg: clinical and molecular characterization of 39 unreported patients. Human Mutation, 37:653-660, Jul 2016. URL: https://doi.org/10.1002/humu.22983, doi:10.1002/humu.22983. This article has 73 citations and is from a domain leading peer-reviewed journal.

6. (bogdanska2021clinicalbiochemicaland pages 6-8): Anna Bogdańska, Patryk Lipiński, Paulina Szymańska-Rożek, Aleksandra Jezela-Stanek, Dariusz Rokicki, Piotr Socha, and Anna Tylki-Szymańska. Clinical, biochemical and molecular phenotype of congenital disorders of glycosylation: long-term follow-up. Orphanet Journal of Rare Diseases, Jan 2021. URL: https://doi.org/10.1186/s13023-020-01657-5, doi:10.1186/s13023-020-01657-5. This article has 50 citations and is from a peer-reviewed journal.

7. (lin2024targetedproteomicsreveals pages 1-2): Qingsong Lin, Lei Zhou, Chuen Lam, Roman Sakson, Lars Beedgen, Patrick Bernhard, K. M. Alp, Nicole Lübbehusen, R. Röth, Beate Niesler, Marcin Luzarowski, Olga Shevchuk, Matthias P. Mayer, Christian Thiel, and Thomas Ruppert. Targeted proteomics reveals quantitative differences in low-abundance glycosyltransferases of patients with congenital disorders of glycosylation. International Journal of Molecular Sciences, 25:1191, Jan 2024. URL: https://doi.org/10.3390/ijms25021191, doi:10.3390/ijms25021191. This article has 5 citations.

8. (lin2024targetedproteomicsreveals pages 4-6): Qingsong Lin, Lei Zhou, Chuen Lam, Roman Sakson, Lars Beedgen, Patrick Bernhard, K. M. Alp, Nicole Lübbehusen, R. Röth, Beate Niesler, Marcin Luzarowski, Olga Shevchuk, Matthias P. Mayer, Christian Thiel, and Thomas Ruppert. Targeted proteomics reveals quantitative differences in low-abundance glycosyltransferases of patients with congenital disorders of glycosylation. International Journal of Molecular Sciences, 25:1191, Jan 2024. URL: https://doi.org/10.3390/ijms25021191, doi:10.3390/ijms25021191. This article has 5 citations.

9. (pajusalu2021theestimatedprevalence pages 3-4): Sander Pajusalu, Mari-Anne Vals, Laura Mihkla, Ustina Šamarina, Tiina Kahre, and Katrin Õunap. The estimated prevalence of n-linked congenital disorders of glycosylation across various populations based on allele frequencies in general population databases. Frontiers in Genetics, Aug 2021. URL: https://doi.org/10.3389/fgene.2021.719437, doi:10.3389/fgene.2021.719437. This article has 36 citations and is from a peer-reviewed journal.

10. (zhao2025clinicalandgenetic pages 10-11): Peiwei Zhao, Li Tan, Qingjie Meng, Lei Zhang, Yufeng Huang, Xiankai Zhang, Yanqiu Hu, Shiqiong Zhou, and Xuelian He. Clinical and genetic characterization of congenital disorders of glycosylation in 20 chinese patients. Orphanet Journal of Rare Diseases, Dec 2025. URL: https://doi.org/10.1186/s13023-025-04075-7, doi:10.1186/s13023-025-04075-7. This article has 2 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](ALG1-Congenital_Disorder_of_Glycosylation-deep-research-falcon_artifacts/artifact-00.md)