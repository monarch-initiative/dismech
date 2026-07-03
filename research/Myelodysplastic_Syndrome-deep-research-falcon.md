---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-08T10:51:06.361126'
end_time: '2026-06-08T11:22:18.720072'
duration_seconds: 1872.36
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Myelodysplastic Syndrome
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 59
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Myelodysplastic_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Myelodysplastic Syndrome
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Myelodysplastic Syndrome** covering all of the
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
- **Disease Name:** Myelodysplastic Syndrome
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Myelodysplastic Syndrome** covering all of the
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


# Myelodysplastic Syndrome (Myelodysplastic Neoplasms, MDS): Disease Characteristics Research Report

## Target Disease
- **Disease name:** Myelodysplastic Syndrome (WHO 2022 preferred: **Myelodysplastic Neoplasms**, abbreviated **MDS**) (lucero2023managementofpatients pages 1-2)
- **Category:** Clonal hematopoietic stem/progenitor cell myeloid neoplasm / bone marrow failure malignancy with variable risk of AML transformation (niscola2024latestinsightsand pages 1-2, thalla2025advancesandchallenges pages 1-2)
- **ICD-10 (clinical coding commonly used):** **D46** (captured in GBD analyses covering ICD-10 D45–D47 and noted in MDS burden methods) (gou2025globalregionaland pages 2-3)
- **MONDO / MeSH / Orphanet / OMIM IDs:** Not directly retrievable with tool-backed evidence in this run; use external ontology sources to finalize identifiers.

---

## 1. Disease Information

### 1.1 Concise overview (current understanding)
MDS are **heterogeneous clonal myeloid malignancies** arising from hematopoietic stem cells, characterized by **morphologic dysplasia**, **ineffective hematopoiesis**, and resulting **peripheral blood cytopenias** with a variable propensity to progress to **acute myeloid leukemia (AML)** (thalla2025advancesandchallenges pages 1-2, lucero2023managementofpatients pages 1-2).

### 1.2 Common synonyms / alternative names
- Myelodysplastic syndromes (historical term) (lucero2023managementofpatients pages 1-2)
- Myelodysplastic neoplasms (WHO 2022 nomenclature) (lucero2023managementofpatients pages 1-2)
- “Preleukemic” bone marrow failure disorder (conceptual; progression risk emphasized in multiple reviews) (thalla2025advancesandchallenges pages 1-2)

### 1.3 Aggregated resources vs individual patients
The information below is derived from **aggregated disease-level resources** (reviews, registries, large cohorts, and randomized trials) rather than EHR-only case series (e.g., GBD analyses; registry-based classification validations; phase 3 trials) (zhang2022comparisonofthe pages 1-2, platzbecker2023…andsafety pages 1-2, gou2025globalregionaland pages 1-2).

---

## 2. Etiology

### 2.1 Disease causal factors (mechanistic, genetic, environmental)
MDS arises via **multistep acquisition of somatic genetic lesions** in hematopoietic stem/progenitor cells, producing clonal dominance, dysplasia, and marrow failure; the process is influenced by **aging**, **immune/inflammatory microenvironmental changes**, and **selection pressures** including genotoxic exposures (niscola2024latestinsightsand pages 1-2, karel2024myelodysplasticneoplasms(mds) pages 1-2, nachtkamp2023myelodysplasticsyndromesnew pages 1-2).

### 2.2 Risk factors

#### 2.2.1 Age and premalignant clonal states
- MDS commonly arises from antecedent clonal hematopoiesis states including **CHIP** and **CCUS**, which are detectable via genomic analysis and represent premalignant conditions in some individuals (niscola2024latestinsightsand pages 1-2).
- CHIP prevalence rises with age (≈10% by age ≥80 in one review), and CHIP confers an estimated **~0.5–1% per year** risk of developing MDS (nachtkamp2023myelodysplasticsyndromesnew pages 1-2).

#### 2.2.2 Therapy-related and genotoxic exposures
- Prior exposure to **chemotherapy, radiotherapy, and radioiodine therapy** is explicitly highlighted as an MDS risk factor in a 2023 clinical review (nachtkamp2023myelodysplasticsyndromesnew pages 1-2).
- In clonal hematopoiesis literature, selection pressures promoting CH expansion and therapy-related myeloid neoplasms include **chemotherapy agents** (e.g., **cisplatin, etoposide, doxorubicin**) and **radiation** (zhang2024implicationsofclonal pages 2-4).

#### 2.2.3 Smoking
Smoking is discussed as a selection pressure in CH biology and is associated with specific mutation patterns (e.g., association with **ASXL1 mutations**) (zhang2024implicationsofclonal pages 2-4).

#### 2.2.4 Autoimmune/inflammatory comorbidity
Pre-existing autoimmune disease is reported in **~10–30%** of MDS patients, and inflammatory pathway activation is implicated in pathogenesis (niscola2024latestinsightsand pages 1-2).

#### 2.2.5 Germline predisposition
Germline predisposition is described as **more frequent than previously recognized**, particularly in younger adults (nachtkamp2023myelodysplasticsyndromesnew pages 1-2).

### 2.3 Protective factors
No tool-retrieved primary evidence identified specific protective genetic variants or environmental protective factors for MDS in this run.

### 2.4 Gene–environment interactions
Gene–environment interactions are framed largely through **clonal selection**: genotoxic therapy/radiation and smoking can preferentially expand clones with certain mutations (e.g., TP53, PPM1D), increasing risk of therapy-related myeloid neoplasms (zhang2024implicationsofclonal pages 2-4).

---

## 3. Phenotypes

### 3.1 Core clinical phenotype (symptoms/signs)
MDS clinical hallmarks include **persistent cytopenias** and marrow dysplasia due to ineffective hematopoiesis, typically manifesting as:
- **Anemia** → fatigue, transfusion dependence
- **Neutropenia** → infection susceptibility
- **Thrombocytopenia** → bleeding/bruising
These are described as the clinical consequences of ineffective hematopoiesis and cytopenias (niscola2024latestinsightsand pages 1-2).

### 3.2 Phenotype characteristics
- **Typical onset:** largely **older adults** (median diagnosis around ~70–75 years in clinical reviews) (nachtkamp2023myelodysplasticsyndromesnew pages 1-2, thalla2025advancesandchallenges pages 1-2)
- **Severity/progression:** variable; risk of AML progression depends on blast percentage, cytogenetics, and molecular profile (niscola2024latestinsightsand pages 6-7, hoff2023moleculardriversof pages 5-7)

### 3.3 Suggested HPO terms (examples)
(These are ontology *suggestions*; verify exact term IDs in HPO.)
- Anemia; fatigue; dyspnea on exertion (symptom-level)
- Neutropenia; recurrent infections
- Thrombocytopenia; easy bruising; mucosal bleeding
- Pancytopenia
- Bone marrow dysplasia / ineffective hematopoiesis
Supported as common cytopenic manifestations of MDS pathobiology (niscola2024latestinsightsand pages 1-2, thalla2025advancesandchallenges pages 1-2).

### 3.4 Quality-of-life impact
Transfusion dependence and chronic cytopenias reduce quality of life; transfusion dependence is described as being associated with reduced QoL metrics and inferior outcomes (stempel2025advancesandchallenges pages 5-7).

---

## 4. Genetic / Molecular Information

### 4.1 Common somatic mutation classes (current landscape)
Recurrent mutations span multiple biological programs (examples):
- **Epigenetic regulators:** TET2, DNMT3A, ASXL1, EZH2, IDH1/2 (niscola2024latestinsightsand pages 1-2, hoff2023moleculardriversof pages 10-11)
- **Spliceosome:** SF3B1, SRSF2, U2AF1, ZRSR2 (niscola2024latestinsightsand pages 1-2, hoff2023moleculardriversof pages 10-11)
- **Transcription factors / tumor suppressor:** TP53, RUNX1, BCOR (niscola2024latestinsightsand pages 1-2, hoff2023moleculardriversof pages 10-11)
- **Cohesin complex:** STAG2 (hoff2023moleculardriversof pages 10-11)
- **Signaling genes:** NRAS/KRAS, JAK2, CBL (niscola2024latestinsightsand pages 1-2, hoff2023moleculardriversof pages 10-11)

At least one somatic mutation is reported in **>90%** of MDS patients (niscola2024latestinsightsand pages 6-7).

### 4.2 Quantitative mutation frequencies (selected examples)
- **ASXL1** ~15–20% in MDS (hoff2023moleculardriversof pages 10-11)
- **EZH2** ~5–10% (hoff2023moleculardriversof pages 10-11)
- **TP53** ~10% de novo; higher in therapy-related disease (25%) and in del(5q) disease (20%); multi-hit TP53 predicts worse OS and AML transformation (hoff2023moleculardriversof pages 10-11)

### 4.3 Cytogenetic abnormalities
Common lesions include del(5q), monosomy/deletion 7, del(20q), trisomy 8, and complex karyotype (niscola2024latestinsightsand pages 1-2, karel2024myelodysplasticneoplasms(mds) pages 1-2).

### 4.4 Epigenetic information
MDS biology is strongly influenced by epigenetic dysregulation (DNA methylation and histone modifications), reflected by frequent mutations in epigenetic regulators (DNMT3A/TET2/ASXL1/EZH2) (niscola2024latestinsightsand pages 1-2, hoff2023moleculardriversof pages 10-11).

### 4.5 Suggested gene/protein ontologies (examples)
- **GO biological processes (suggestions):** hematopoiesis; myeloid cell differentiation; RNA splicing; DNA methylation; chromatin organization; inflammatory response.
- **CL cell types (suggestions):** hematopoietic stem cell; myeloid progenitor cell; erythroid progenitor; megakaryocyte.

---

## 5. Environmental Information

### 5.1 Environmental/lifestyle contributors
Evidence in retrieved sources supports:
- **Smoking** as a modifiable exposure linked to clonal hematopoiesis patterns and highlighted as an addressable risk factor in burden discussions (gou2025globalregionaland pages 16-18, zhang2024implicationsofclonal pages 2-4).

### 5.2 Prior medical exposures
- Prior **chemotherapy** and **radiation therapy** are repeatedly flagged as risk-enhancing and are core to therapy-related myeloid neoplasms (nachtkamp2023myelodysplasticsyndromesnew pages 1-2, zhang2024implicationsofclonal pages 2-4).

### 5.3 Infectious agents
No evidence in retrieved sources supports a specific infectious etiology for MDS.

---

## 6. Mechanism / Pathophysiology

### 6.1 High-level causal chain (trigger → cellular effects → clinical phenotype)
1. **Aging and/or genotoxic exposures** (chemo/radiation; smoking; chronic inflammation) promote acquisition/selection of somatic mutations in HSCs (nachtkamp2023myelodysplasticsyndromesnew pages 1-2, zhang2024implicationsofclonal pages 2-4).
2. Emergence of **clonal hematopoiesis (CHIP)** and intermediate states such as **CCUS** (CHIP + persistent cytopenia), with increased risk of progression to myeloid neoplasia (testa2025clonalhematopoiesisa pages 16-18, niscola2024latestinsightsand pages 1-2).
3. Expansion of mutant clones with defects in differentiation/survival pathways produces **ineffective hematopoiesis** and **dysplasia**, causing persistent cytopenias (niscola2024latestinsightsand pages 1-2).
4. Accumulation of additional lesions (e.g., TP53 multi-hit, complex karyotype, signaling mutations) increases blasts and promotes progression to **higher-risk MDS/AML** (hoff2023moleculardriversof pages 10-11, hoff2023moleculardriversof pages 5-7).

### 6.2 Immune/inflammatory microenvironment
The marrow microenvironment is described as **immune/inflammatory dysregulated**, with inflammatory pathway activation contributing to clonal selection and suppression of normal hematopoiesis (niscola2024latestinsightsand pages 1-2). Mechanistically, inflammatory cytokines (e.g., TNFα, IL-6) can promote apoptosis of healthy progenitors and advantage MDS clones (baumann2025inflammatorysignalingin pages 5-7).

### 6.3 Molecular pathways and cellular processes (examples)
- **RNA splicing dysregulation** (SF3B1/SRSF2/U2AF1/ZRSR2) (niscola2024latestinsightsand pages 1-2)
- **Epigenetic dysregulation** (DNMT3A/TET2/ASXL1/EZH2; PRC2 biology) (hoff2023moleculardriversof pages 10-11)
- **DNA damage response selection** (TP53; therapy-related evolution) (zhang2024implicationsofclonal pages 2-4)

---

## 7. Anatomical Structures Affected

### 7.1 Organ/tissue level
- Primary site: **bone marrow** (hematopoietic tissue) with resulting peripheral blood cytopenias (niscola2024latestinsightsand pages 1-2, thalla2025advancesandchallenges pages 1-2)

### 7.2 Cell populations (suggestions)
- Hematopoietic stem and progenitor cells (HSPCs)
- Myeloid/erythroid/megakaryocytic lineages
Supported by disease definition (HSC origin; multilineage dysplasia) (niscola2024latestinsightsand pages 1-2, thalla2025advancesandchallenges pages 1-2).

### 7.3 UBERON suggestions
- Bone marrow (UBERON term suggested; verify ID externally)

---

## 8. Temporal Development

### 8.1 Onset pattern
Typically insidious/chronic, diagnosed during evaluation of cytopenias, predominantly in older adults (nachtkamp2023myelodysplasticsyndromesnew pages 1-2).

### 8.2 Progression and staging
Progression risk is tied to blast burden, cytogenetics, and molecular lesions; WHO/ICC provide blast-based increased-blast categories and ICC introduces an MDS/AML transitional group (hoff2023moleculardriversof pages 2-4, lucero2023managementofpatients pages 1-2).

---

## 9. Inheritance and Population

### 9.1 Epidemiology
- Incidence: ~**4 per 100,000 persons/year** reported in a clinical review (nachtkamp2023myelodysplasticsyndromesnew pages 1-2); another review reports ~4 per 100,000 overall and ~25 per 100,000 among those ≥65 (thalla2025advancesandchallenges pages 1-2).
- Median age: ~70–75 years (nachtkamp2023myelodysplasticsyndromesnew pages 1-2).
- Median survival: ~**3 years** (nachtkamp2023myelodysplasticsyndromesnew pages 1-2).

### 9.2 Global burden (GBD 2021-based)
A GBD analysis combining MDS/MPN reported global incidence increasing from **171,132 (1990)** to **341,017 (2021)** with projected incidence **~457,320 by 2045** (gou2025globalregionaland pages 1-2).

### 9.3 Sex/age distribution
Burden is described as higher in men and concentrated in older ages in the GBD analysis (gou2025globalregionaland pages 1-2).

### 9.4 Germline predisposition
Germline predisposition appears more frequent than previously appreciated, especially in younger adults (nachtkamp2023myelodysplasticsyndromesnew pages 1-2).

---

## 10. Diagnostics

### 10.1 Standard diagnostic workup (current practice)
- **Gold standard:** peripheral blood and bone marrow **cytomorphology** plus cytogenetics and molecular testing (nachtkamp2023myelodysplasticsyndromesnew pages 1-2).
- Reviews emphasize diagnosis by **cytomorphology** supplemented by **banding cytogenetics**, **histomorphology**, and **somatic mutation analyses** (nachtkamp2023myelodysplasticsyndromesnew pages 1-2).

### 10.2 WHO 2022 / ICC 2022 classification diagnostics (key points)
WHO 2022/WHO-HAEM5 emphasizes genetically defined subtypes (e.g., SF3B1-mutant, biallelic TP53), retains dysplasia threshold (10%), and uses blast categories MDS-LB and MDS-IB (lucero2023managementofpatients pages 1-2, hoff2023moleculardriversof pages 2-4). ICC provides an alternative framework including an MDS/AML category for 10–19% blasts (hoff2023moleculardriversof pages 2-4, lucero2023managementofpatients pages 1-2).

| Framework | Entity/category | BM blasts | PB blasts | Key defining features/notes | Primary citation id |
|---|---|---:|---:|---|---|
| WHO 2022 / WHO-HAEM5 | MDS-LB | <5% | <2% | Low-blast MDS; morphologic category; dysplasia threshold remains 10% in any lineage; WHO groups MDS into genetically defined and morphologically defined entities. (hoff2023moleculardriversof pages 2-4, lucero2023managementofpatients pages 1-2) | (hoff2023moleculardriversof pages 2-4) |
| WHO 2022 / WHO-HAEM5 | MDS-h | <5% | <2% | Hypoplastic MDS recognized as distinct subtype; bone marrow cellularity <25%. (hoff2023moleculardriversof pages 2-4, lee2024comparisonofthe pages 1-2) | (hoff2023moleculardriversof pages 2-4) |
| WHO 2022 / WHO-HAEM5 | MDS-IB1 | 5-9% | 2-9% | Replaces older MDS-EB1 terminology; 10% blast cutoff distinguishes IB1 from IB2. (hoff2023moleculardriversof pages 2-4, lucero2023managementofpatients pages 1-2, lapadat2025navigatingthenew pages 2-4) | (hoff2023moleculardriversof pages 2-4) |
| WHO 2022 / WHO-HAEM5 | MDS-IB2 | 10-19% | 5-19% | Includes Auer rods; WHO retains 20% blast cutoff separating MDS from AML. (hoff2023moleculardriversof pages 2-4, niscola2024latestinsightsand pages 4-6) | (hoff2023moleculardriversof pages 2-4) |
| WHO 2022 / WHO-HAEM5 | AML cutoff | ≥20% | ≥20% | WHO retains classic 20% blast threshold for AML in MDS blast-based categories, although AML-defining lesions can supersede blast counting in some contexts. (niscola2024latestinsightsand pages 4-6, lee2024comparisonofthe pages 1-2) | (niscola2024latestinsightsand pages 4-6) |
| ICC 2022 | MDS, NOS / low-blast equivalents | <5% | usually <2% | ICC retains MDS categories with 10% dysplasia threshold; also accepts certain MDS-defining cytogenetic/genetic lesions even without dysplasia in persistent cytopenia. (lucero2023managementofpatients pages 1-2) | (lucero2023managementofpatients pages 1-2) |
| ICC 2022 | MDS with excess blasts (MDS-EB) | ≥5% | ≥2% | ICC uses MDS-EB terminology; prior WHO MDS-EB2 concept split, with 10-19% blasts moved to MDS/AML. (niscola2024latestinsightsand pages 4-6, lucero2023managementofpatients pages 1-2) | (niscola2024latestinsightsand pages 4-6) |
| ICC 2022 | MDS/AML | 10-19% | 10-19% or corresponding increased blasts | Transitional category replacing prior MDS-EB2 for cases without AML-defining genetic lesions; emphasizes MDS-AML continuum. (hoff2023moleculardriversof pages 2-4, lee2024comparisonofthe pages 1-2, lapadat2025navigatingthenew pages 2-4) | (hoff2023moleculardriversof pages 2-4) |
| ICC 2022 | AML threshold for recurrent genetic abnormalities | ≥10% for most recurrent genetic abnormalities | ≥10% for most recurrent genetic abnormalities | ICC requires 10% blasts to define AML with recurrent genetic abnormalities, except BCR::ABL1 and TP53-related exceptions noted in comparative review. (lee2024comparisonofthe pages 1-2) | (lee2024comparisonofthe pages 1-2) |
| WHO 2022 / ICC 2022 | MDS-defining lesion: del(5q) | N/A | N/A | Recognized MDS-defining cytogenetic abnormality; isolated del(5q) remains a distinct entity/subtype; thrombocytosis can be present. (lucero2023managementofpatients pages 1-2, zhang2022comparisonofthe pages 1-2) | (lucero2023managementofpatients pages 1-2) |
| WHO 2022 / ICC 2022 | MDS-defining lesion: multi-hit / biallelic TP53 | N/A | N/A | Distinct high-risk entity in WHO (MDS-biTP53) and disease-defining lesion in ICC; associated with poor survival. (hoff2023moleculardriversof pages 2-4, zhang2022comparisonofthe pages 1-2) | (hoff2023moleculardriversof pages 2-4) |
| WHO 2022 / ICC 2022 | MDS-defining lesion: -7 / del(7q) | N/A | N/A | Listed among cytogenetic lesions that can define MDS in persistent cytopenia, even without morphologic dysplasia in ICC framework. (lucero2023managementofpatients pages 1-2, karel2024myelodysplasticneoplasms(mds) pages 1-2) | (lucero2023managementofpatients pages 1-2) |
| WHO 2022 / ICC 2022 | MDS-defining lesion: complex karyotype | N/A | N/A | Adverse cytogenetic category; ICC examples define complex karyotype as >3 unrelated clonal chromosomal abnormalities. (lucero2023managementofpatients pages 1-2) | (lucero2023managementofpatients pages 1-2) |
| ICC 2022 definition detail | Multi-hit TP53 definition | N/A | N/A | Multi-hit TP53 may be defined by: two distinct TP53 mutations each with VAF ≥10%; or one TP53 mutation plus 17p deletion; or TP53 mutation with VAF ≥50%; or TP53 mutation with copy-neutral LOH at 17p. (hoff2023moleculardriversof pages 2-4, abdulbaki2024abriefoverview pages 3-4) | (hoff2023moleculardriversof pages 2-4) |


*Table: This table compactly aligns WHO 2022/WHO-HAEM5 and ICC 2022 blast-based MDS categories and lists key MDS-defining cytogenetic/genetic lesions. It is useful for quickly comparing category names, blast cutoffs, and the operational definition of multi-hit TP53 used in contemporary classification.*

### 10.3 Flow cytometry
Multiparameter flow cytometry is described as a **complementary diagnostic tool**; it is not mandated by international baseline guidelines but is “almost universally adopted” in practice for suspected cytopenias and dysplasia detection across marrow lineages, and can support follow-up/MRD assessment (verigou2024immunophenotypingmyelodysplasticneoplasms pages 1-2).

### 10.4 Molecular diagnostics / genome sequencing
Modern classifications incorporate genomic profiling to define entities (e.g., SF3B1-mutant, TP53-mutant MDS) and inform prognosis via IPSS-M; this is emphasized in a 2024 Haematologica review on genome sequencing in MDS management (cazzola2024genomesequencingin pages 1-3).

### 10.5 Differential diagnosis (high-level)
Key differentials include CHIP/CCUS, aplastic anemia, MDS/MPN overlap entities (e.g., CMML), and AML; ICC/WHO frameworks refine boundaries and integrate genetic criteria (hoff2023moleculardriversof pages 2-4, testa2025clonalhematopoiesisa pages 16-18).

---

## 11. Outcome / Prognosis

### 11.1 Natural history and AML transformation
- Progression to acute leukemia occurs in **~25%** in one clinical review (nachtkamp2023myelodysplasticsyndromesnew pages 1-2).
- Another review states **30–40%** progress to AML with poor post-transformation survival (death within ~4–6 months after transformation) (thalla2025advancesandchallenges pages 1-2).

### 11.2 Risk-stratified survival (IPSS-R)
Median overall survival by IPSS-R group (years): **8.8** (very low), **5.3** (low), **3.0** (intermediate), **1.6** (high), **0.8** (very high) (niscola2024latestinsightsand pages 6-7).

### 11.3 IPSS-M (molecular prognostication)
IPSS-M integrates clinical parameters, cytogenetics, and mutations (31 genes) and can reclassify a substantial fraction of patients (e.g., 42.5% reclassified; 29.3% upstaged in one external validation cohort) (nachtkamp2023myelodysplasticsyndromesnew pages 1-2, lee2024comparisonofthe pages 1-2).

### 11.4 High-risk genetic subgroup example
WHO 2022 MDS-biTP53 has markedly poor survival (median ~10 months in a reclassification study) (zhang2022comparisonofthe pages 1-2).

---

## 12. Treatment

### 12.1 Treatment goals (risk-adapted)
- **Lower-risk MDS:** reduce cytopenia burden (especially anemia), decrease transfusion dependence, improve QoL (lucero2023managementofpatients pages 1-2, stempel2025advancesandchallenges pages 5-7).
- **Higher-risk MDS:** prolong survival, prevent AML transformation, and pursue cure when feasible (HSCT) (kroger2024treatmentofhighrisk pages 1-2, nachtkamp2023myelodysplasticsyndromesnew pages 1-2).

### 12.2 Supportive and rehabilitative care (real-world implementations)
- RBC transfusions are common (about half of patients require transfusions at diagnosis) and filtered products are recommended to reduce alloimmunization (kroger2024treatmentofhighrisk pages 1-2).
- Iron chelation: recommended after heavy transfusion exposure; one review suggests iron chelation after >20 RBC units and ferritin >2500 ng/mL with goal ferritin <1000 ng/mL (stempel2025advancesandchallenges pages 5-7); another emphasizes early deferasirox use to prevent iron overload and improve outcomes (niscola2024latestinsightsand pages 8-10).

**MAXO suggestions:** blood transfusion; iron chelation therapy.

### 12.3 ESAs (erythropoiesis-stimulating agents)
- ESA recommendation example: erythropoietin alfa for patients with endogenous EPO <200 ng/mL (nachtkamp2023myelodysplasticsyndromesnew pages 1-2).
- Another review indicates practice use of ESA when EPO ≤500 mU/mL and alternatives when EPO >500 mU/mL (stempel2025advancesandchallenges pages 4-5).

**MAXO suggestion:** erythropoiesis-stimulating agent therapy.

### 12.4 Lenalidomide for del(5q) MDS
- Lenalidomide is indicated for 5q deletion (nachtkamp2023myelodysplasticsyndromesnew pages 1-2).
- Reported efficacy: phase II—76% reduced transfusions and 67% achieved transfusion independence; phase III—RBC-TI 61% (10 mg) and 51.1% (5 mg) vs 7.8% placebo, with AML-free survival benefit (stempel2025advancesandchallenges pages 4-5).

**MAXO suggestion:** lenalidomide therapy.

### 12.5 Luspatercept (TGF-β superfamily ligand trap)
**Phase 3 COMMANDS (2023 interim analysis; ESA-naive, transfusion-dependent LR-MDS, sEPO <500 U/L):**
- Primary endpoint: RBC transfusion independence ≥12 weeks plus mean Hb increase ≥1.5 g/dL during weeks 1–24.
- Interim efficacy set: 86/147 (59%) luspatercept vs 48/154 (31%) epoetin alfa; risk difference 26.6% (95% CI 15.8–37.4), p<0.0001 (platzbecker2023…andsafety pages 1-2).
- Longer follow-up analyses report durable benefit including ≥1 year RBC-TI 44.5% vs 27.6% (p=0.0003) (garciamanero2025longtermtransfusionindependence pages 1-2).

**MAXO suggestion:** luspatercept therapy.

### 12.6 Imetelstat (telomerase inhibitor)
**IMerge phase 3 (lower-risk transfusion-dependent non-del(5q) MDS):**
- Primary endpoint: RBC transfusion independence ≥8 weeks.
- 40% imetelstat vs 15% placebo achieved ≥8-week TI (merz2024treatmentoflowerrisk pages 3-4, fahim2024imetelstatforanemia pages 2-3).
- Sustained TI ≥1 year reported 18% vs 2% (p=0.023) (fahim2024imetelstatforanemia pages 2-3).
- Key grade 3/4 toxicities include neutropenia and thrombocytopenia (e.g., 68% and 62% vs 3% and 8% placebo) (fahim2024imetelstatforanemia pages 2-3).

**MAXO suggestion:** imetelstat therapy.

### 12.7 Hypomethylating agents (HMAs) and higher-risk MDS
- For higher-risk MDS patients not transplant-eligible, HMAs remain standard-of-care; azacitidine is described as the only approved non-transplant option in a 2024 Haematologica review (kroger2024treatmentofhighrisk pages 1-2).
- Azacitidine improves outcomes in higher-risk non-transplant candidates per a 2023 clinical review (nachtkamp2023myelodysplasticsyndromesnew pages 1-2).

**MAXO suggestions:** azacitidine therapy; decitabine therapy.

### 12.8 Allogeneic hematopoietic stem cell transplantation (allo-HSCT)
Allo-HSCT is repeatedly emphasized as the **only curative** therapy for eligible patients, with relapse being a major cause of transplant failure (kroger2024treatmentofhighrisk pages 1-2, nachtkamp2023myelodysplasticsyndromesnew pages 1-2).

**MAXO suggestion:** allogeneic hematopoietic stem cell transplantation.

### 12.9 Targeted therapy example: IDH1 mutation (ivosidenib)
IDH1/2 mutations occur in ~5% of MDS (stempel2025advancesandchallenges pages 13-15). In IDH1-mutant MDS, ivosidenib is approved for relapsed/refractory disease with reported CR rates near 40% and median OS 35.7 months (AG120-C-001) (stempel2025advancesandchallenges pages 13-15).

**MAXO suggestion:** targeted small-molecule inhibitor therapy (IDH1 inhibitor).

---

## 13. Prevention

### 13.1 Primary prevention (risk factor modification)
- **Avoidance/minimization of unnecessary genotoxic exposure** (chemotherapy/radiation when alternatives exist) is conceptually supported by the association between prior cytotoxic exposure and therapy-related myeloid neoplasms and shortened time to t-MN in CH carriers (zhang2024implicationsofclonal pages 2-4, nachtkamp2023myelodysplasticsyndromesnew pages 1-2).
- **Smoking cessation** is supported as an addressable risk factor in burden discussions and is linked to clonal hematopoiesis selection patterns (gou2025globalregionaland pages 16-18, zhang2024implicationsofclonal pages 2-4).

### 13.2 Secondary prevention (early detection)
Emerging concept: monitoring high-risk **CH/CCUS** carriers for progression, since CH progression risk to malignancy is non-zero and measurable (e.g., ~4% over 8 years in one CH study cited in a review) (zhang2024implicationsofclonal pages 2-4). Practical implementation and validated screening programs are not established in the retrieved evidence.

### 13.3 Tertiary prevention
Supportive care (transfusions, iron chelation, infection management) to reduce complications of chronic cytopenias (kroger2024treatmentofhighrisk pages 1-2, stempel2025advancesandchallenges pages 5-7).

---

## 14. Other Species / Natural Disease
No tool-retrieved evidence in this run identified naturally occurring, veterinary-relevant MDS analogs with strong translational mapping.

---

## 15. Model Organisms / Experimental Systems

### 15.1 Human xenografts and humanized mice (current implementations)
A 2025 review summarizes that classical immunodeficient NSG/BRG mice support human HSC engraftment but **poorly support myeloid/erythroid/megakaryocytic differentiation**, motivating cytokine-humanized strains (munteanu2025humanizedmousemodels pages 2-3).

Key platforms:
- **NSG**: good engraftment but limited myeloid differentiation (munteanu2025humanizedmousemodels pages 2-3).
- **MISTRG** (human M-CSF, IL-3, GM-CSF, SIRPα, TPO): improved myeloid engraftment (>80% CD33+ reported) while preserving patient mutations (munteanu2025humanizedmousemodels pages 2-3).
- **NSG-SGM3 / NOG-EXL / NOGW-EXL / MISTRG6kitW41 (M6k)**: cytokine- and niche-engineered approaches improving lineage output and engraftment; NSG-SGM3 can have graft exhaustion and loss by ~24 weeks (munteanu2025humanizedmousemodels pages 7-7, munteanu2025humanizedmousemodels pages 5-7).
- **PDX models** preserve genetic/phenotypic heterogeneity and can maintain mutations such as SF3B1, DNMT3A, SRSF2, TET2, TP53, RUNX1, KIT; engraftment often needs preconditioning (irradiation or macrophage depletion) and remains challenging for low-risk MDS (munteanu2025humanizedmousemodels pages 7-7, munteanu2025humanizedmousemodels pages 5-7).

### 15.2 Genetically engineered mouse models (GEMMs)
Examples recapitulating MDS-like features:
- Runx1 deletion: anemia, trilineage dysplasia and rapid progression (munteanu2025humanizedmousemodels pages 5-7).
- U2af1S34F knock-in: impaired hematopoiesis, mild dysplasia, splicing defects (munteanu2025humanizedmousemodels pages 5-7).
- Ezh2 conditional knockout: impaired differentiation, dysplasia, leukemic progression (munteanu2025humanizedmousemodels pages 5-7).

### 15.3 Limitations (expert analysis)
No current murine model fully recapitulates the human marrow microenvironment and immune system; humanized models have limitations in long-term stability and modeling early/low-risk disease (munteanu2025humanizedmousemodels pages 1-2, munteanu2025humanizedmousemodels pages 8-10).

---

## Expert opinions / analysis (authoritative themes)
Across contemporary reviews, expert consensus emphasizes:
- **Risk-adapted management** integrating molecular profiling (IPSS-M, WHO/ICC genetically defined entities) (cazzola2024genomesequencingin pages 1-3, stempel2025advancesandchallenges pages 15-16).
- **Persistent clinical need** for durable disease-modifying therapies, particularly for high-risk genomics (e.g., multi-hit TP53) where outcomes remain poor (stempel2025advancesandchallenges pages 13-15, zhang2022comparisonofthe pages 1-2).
- **Pragmatic multimodality diagnostics**: morphology remains essential but is subjective; genomic and cytogenetic data increasingly define entities; flow cytometry is widely used as a complement (vicente2024whoiccclassificationfor pages 1-2, verigou2024immunophenotypingmyelodysplasticneoplasms pages 1-2).

---

## Key recent developments (prioritized 2023–2024)
1. **Classification modernization:** WHO 2022/WHO-HAEM5 and ICC 2022 incorporate genetically defined entities (SF3B1-mutant, biallelic TP53) and refine blast-based categories (hoff2023moleculardriversof pages 2-4, lucero2023managementofpatients pages 1-2).
2. **Frontline anemia therapy shift (2023):** COMMANDS showed luspatercept superiority over epoetin alfa for a composite transfusion/Hb endpoint in ESA-naive LR-MDS (platzbecker2023…andsafety pages 1-2, merz2024treatmentoflowerrisk pages 3-4).
3. **Molecular diagnostics and precision medicine (2024):** genome sequencing reviews emphasize molecular taxonomy and IPSS-M integration into decision-making (cazzola2024genomesequencingin pages 1-3).

---

## Notes on citation requirements (PMID limitation)
Many retrieved sources are journal articles with DOIs but PMIDs were not available in the extracted tool evidence; therefore, this report cites the retrieved sources via tool citation IDs, and provides URLs/DOIs (embedded in the evidence metadata). For a production knowledge base, PMIDs should be added by cross-referencing these DOIs in PubMed.


References

1. (lucero2023managementofpatients pages 1-2): Josephine Lucero, Salman Al-Harbi, and Karen W. L. Yee. Management of patients with lower-risk myelodysplastic neoplasms (mds). Current Oncology, 30:6177-6196, Jun 2023. URL: https://doi.org/10.3390/curroncol30070459, doi:10.3390/curroncol30070459. This article has 7 citations.

2. (niscola2024latestinsightsand pages 1-2): Pasquale Niscola, Valentina Gianfelici, Marco Giovannini, Daniela Piccioni, Carla Mazzone, and Paolo de Fabritiis. Latest insights and therapeutic advances in myelodysplastic neoplasms. Cancers, 16:1563, Apr 2024. URL: https://doi.org/10.3390/cancers16081563, doi:10.3390/cancers16081563. This article has 13 citations.

3. (thalla2025advancesandchallenges pages 1-2): Rohit Thalla, Ryan Mack, Jorgena Kosti-Schwartz, Peter Breslin, and Jiwang Zhang. Advances and challenges in the treatment of myelodysplastic syndromes. Experimental Hematology & Oncology, Jun 2025. URL: https://doi.org/10.1186/s40164-025-00678-9, doi:10.1186/s40164-025-00678-9. This article has 8 citations and is from a peer-reviewed journal.

4. (gou2025globalregionaland pages 2-3): Xinyue Gou, Zhuo Chen, and Yudi Shangguan. Global, regional, and national burden of myelodysplastic syndromes and myeloproliferative neoplasms, 1990-2021: an analysis from the global burden of disease study 2021. Frontiers in Oncology, Mar 2025. URL: https://doi.org/10.3389/fonc.2025.1559382, doi:10.3389/fonc.2025.1559382. This article has 10 citations.

5. (zhang2022comparisonofthe pages 1-2): Yudi Zhang, Junying Wu, Tiejun Qin, Zefeng Xu, Shiqiang Qu, Lijuan Pan, Bing Li, Huijun Wang, Peihong Zhang, Xin Yan, Jingye Gong, Qingyan Gao, Robert Peter Gale, and Zhijian Xiao. Comparison of the revised 4th (2016) and 5th (2022) editions of the world health organization classification of myelodysplastic neoplasms. Leukemia, 36:2875-2882, Oct 2022. URL: https://doi.org/10.1038/s41375-022-01718-7, doi:10.1038/s41375-022-01718-7. This article has 76 citations and is from a highest quality peer-reviewed journal.

6. (platzbecker2023…andsafety pages 1-2): U Platzbecker, MG Della Porta, V Santini, and AM Zeidan. … and safety of luspatercept versus epoetin alfa in erythropoiesis-stimulating agent-naive, transfusion-dependent, lower-risk myelodysplastic syndromes (commands) …. Unknown journal, 2023.

7. (gou2025globalregionaland pages 1-2): Xinyue Gou, Zhuo Chen, and Yudi Shangguan. Global, regional, and national burden of myelodysplastic syndromes and myeloproliferative neoplasms, 1990-2021: an analysis from the global burden of disease study 2021. Frontiers in Oncology, Mar 2025. URL: https://doi.org/10.3389/fonc.2025.1559382, doi:10.3389/fonc.2025.1559382. This article has 10 citations.

8. (karel2024myelodysplasticneoplasms(mds) pages 1-2): Daniel Karel, Claire Valburg, Navitha Woddor, Victor E. Nava, and Anita Aggarwal. Myelodysplastic neoplasms (mds): the current and future treatment landscape. Current Oncology, 31:1971-1993, Apr 2024. URL: https://doi.org/10.3390/curroncol31040148, doi:10.3390/curroncol31040148. This article has 19 citations.

9. (nachtkamp2023myelodysplasticsyndromesnew pages 1-2): Kathrin Nachtkamp, Guido Kobbe, Norbert Gattermann, and Ulrich Germing. Myelodysplastic syndromes: new methods of diagnosis, prognostication, and treatment. Deutsches Ärzteblatt international, Mar 2023. URL: https://doi.org/10.3238/arztebl.m2023.0005, doi:10.3238/arztebl.m2023.0005. This article has 31 citations.

10. (zhang2024implicationsofclonal pages 2-4): Qi Zhang, Rita Yim, Paul Lee, Lynn Chin, Vivian Li, and Harinder Gill. Implications of clonal hematopoiesis in hematological and non-hematological disorders. Cancers, 16:4118, Dec 2024. URL: https://doi.org/10.3390/cancers16234118, doi:10.3390/cancers16234118. This article has 5 citations.

11. (niscola2024latestinsightsand pages 6-7): Pasquale Niscola, Valentina Gianfelici, Marco Giovannini, Daniela Piccioni, Carla Mazzone, and Paolo de Fabritiis. Latest insights and therapeutic advances in myelodysplastic neoplasms. Cancers, 16:1563, Apr 2024. URL: https://doi.org/10.3390/cancers16081563, doi:10.3390/cancers16081563. This article has 13 citations.

12. (hoff2023moleculardriversof pages 5-7): Fieke W. Hoff and Yazan F. Madanat. Molecular drivers of myelodysplastic neoplasms (mds)—classification and prognostic relevance. Cells, 12:627, Feb 2023. URL: https://doi.org/10.3390/cells12040627, doi:10.3390/cells12040627. This article has 16 citations.

13. (stempel2025advancesandchallenges pages 5-7): J. Stempel, Tariq Kewan, and A. Zeidan. Advances and challenges in the management of myelodysplastic syndromes. Cancers, Jul 2025. URL: https://doi.org/10.3390/cancers17152469, doi:10.3390/cancers17152469. This article has 6 citations.

14. (hoff2023moleculardriversof pages 10-11): Fieke W. Hoff and Yazan F. Madanat. Molecular drivers of myelodysplastic neoplasms (mds)—classification and prognostic relevance. Cells, 12:627, Feb 2023. URL: https://doi.org/10.3390/cells12040627, doi:10.3390/cells12040627. This article has 16 citations.

15. (gou2025globalregionaland pages 16-18): Xinyue Gou, Zhuo Chen, and Yudi Shangguan. Global, regional, and national burden of myelodysplastic syndromes and myeloproliferative neoplasms, 1990-2021: an analysis from the global burden of disease study 2021. Frontiers in Oncology, Mar 2025. URL: https://doi.org/10.3389/fonc.2025.1559382, doi:10.3389/fonc.2025.1559382. This article has 10 citations.

16. (testa2025clonalhematopoiesisa pages 16-18): Ugo Testa, Germana Castelli, and Elvira Pelosi. Clonal hematopoiesis, a risk condition for developing myeloid neoplasia. Hemato, 6:10, Apr 2025. URL: https://doi.org/10.3390/hemato6020010, doi:10.3390/hemato6020010. This article has 3 citations.

17. (baumann2025inflammatorysignalingin pages 5-7): Artemis Margrith Baumann and Jana Maria Ellegast. Inflammatory signaling in the pathogenesis of acute myeloid leukemia. HemaSphere, Aug 2025. URL: https://doi.org/10.1002/hem3.70188, doi:10.1002/hem3.70188. This article has 6 citations and is from a peer-reviewed journal.

18. (hoff2023moleculardriversof pages 2-4): Fieke W. Hoff and Yazan F. Madanat. Molecular drivers of myelodysplastic neoplasms (mds)—classification and prognostic relevance. Cells, 12:627, Feb 2023. URL: https://doi.org/10.3390/cells12040627, doi:10.3390/cells12040627. This article has 16 citations.

19. (lee2024comparisonofthe pages 1-2): Wan-Hsuan Lee, Chien-Chin Lin, Cheng-Hong Tsai, Feng-Ming Tien, Min-Yen Lo, Mei-Hsuan Tseng, Yuan-Yeh Kuo, Shan-Chi Yu, Ming-Chih Liu, Chang-Tsu Yuan, Yi-Tsung Yang, Ming-Kai Chuang, Bor-Sheng Ko, Jih-Luh Tang, Hsun-I Sun, Yi-Kuang Chuang, Hwei-Fang Tien, Hsin-An Hou, and Wen-Chien Chou. Comparison of the 2022 world health organization classification and international consensus classification in myelodysplastic syndromes/neoplasms. Blood Cancer Journal, Apr 2024. URL: https://doi.org/10.1038/s41408-024-01031-9, doi:10.1038/s41408-024-01031-9. This article has 33 citations and is from a domain leading peer-reviewed journal.

20. (lapadat2025navigatingthenew pages 2-4): Mihai-Emilian Lapadat, Oana Stanca, Nicoleta Mariana Berbec, Cristina Negotei, and Andrei Colita. Navigating the new era in myelodysplastic neoplasms: a review of prognostic implications of the ipss-m score and 2022 who classification. Hematology Reports, 17:58, Oct 2025. URL: https://doi.org/10.3390/hematolrep17060058, doi:10.3390/hematolrep17060058. This article has 3 citations.

21. (niscola2024latestinsightsand pages 4-6): Pasquale Niscola, Valentina Gianfelici, Marco Giovannini, Daniela Piccioni, Carla Mazzone, and Paolo de Fabritiis. Latest insights and therapeutic advances in myelodysplastic neoplasms. Cancers, 16:1563, Apr 2024. URL: https://doi.org/10.3390/cancers16081563, doi:10.3390/cancers16081563. This article has 13 citations.

22. (abdulbaki2024abriefoverview pages 3-4): Rami Abdulbaki and Sheeja T. Pullarkat. A brief overview of the molecular landscape of myelodysplastic neoplasms. Current Oncology, 31:2353-2363, Apr 2024. URL: https://doi.org/10.3390/curroncol31050175, doi:10.3390/curroncol31050175. This article has 8 citations.

23. (verigou2024immunophenotypingmyelodysplasticneoplasms pages 1-2): Evgenia Verigou, Theodora Chatzilygeroudi, Vasileios Lazaris, Anne-Lise de Lastic, and Argiris Symeonidis. Immunophenotyping myelodysplastic neoplasms: the role of flow cytometry in the molecular classification era. Frontiers in Oncology, Oct 2024. URL: https://doi.org/10.3389/fonc.2024.1447001, doi:10.3389/fonc.2024.1447001. This article has 10 citations.

24. (cazzola2024genomesequencingin pages 1-3): Mario Cazzola and Luca Malcovati. Genome sequencing in the management of myelodysplastic syndromes and related disorders. Haematologica, 110:312-329, Oct 2024. URL: https://doi.org/10.3324/haematol.2023.284947, doi:10.3324/haematol.2023.284947. This article has 13 citations.

25. (kroger2024treatmentofhighrisk pages 1-2): Nicolaus Kröger. Treatment of high-risk myelodysplastic syndromes. Haematologica, 110:339-349, Dec 2024. URL: https://doi.org/10.3324/haematol.2023.284946, doi:10.3324/haematol.2023.284946. This article has 39 citations.

26. (niscola2024latestinsightsand pages 8-10): Pasquale Niscola, Valentina Gianfelici, Marco Giovannini, Daniela Piccioni, Carla Mazzone, and Paolo de Fabritiis. Latest insights and therapeutic advances in myelodysplastic neoplasms. Cancers, 16:1563, Apr 2024. URL: https://doi.org/10.3390/cancers16081563, doi:10.3390/cancers16081563. This article has 13 citations.

27. (stempel2025advancesandchallenges pages 4-5): J. Stempel, Tariq Kewan, and A. Zeidan. Advances and challenges in the management of myelodysplastic syndromes. Cancers, Jul 2025. URL: https://doi.org/10.3390/cancers17152469, doi:10.3390/cancers17152469. This article has 6 citations.

28. (garciamanero2025longtermtransfusionindependence pages 1-2): Guillermo Garcia-Manero, Valeria Santini, Amer M. Zeidan, Rami S. Komrokji, Veronika Pozharskaya, Shelonitda Rose, Karen Keeperman, Yinzhi Lai, Sameer Kalsekar, Barkha Aggarwal, Dimana Miteva, David Valcárcel, Pierre Fenaux, Jake Shortt, Matteo Giovanni Della Porta, and Uwe Platzbecker. Long-term transfusion independence with luspatercept versus epoetin alfa in erythropoiesis-stimulating agent-naive, lower-risk myelodysplastic syndromes in the commands trial. Advances in Therapy, 42:3576-3589, May 2025. URL: https://doi.org/10.1007/s12325-025-03208-5, doi:10.1007/s12325-025-03208-5. This article has 8 citations and is from a peer-reviewed journal.

29. (merz2024treatmentoflowerrisk pages 3-4): Almuth Maria Anni Merz and Uwe Platzbecker. Treatment of lower-risk myelodysplastic syndromes. Haematologica, 110:330-338, Oct 2024. URL: https://doi.org/10.3324/haematol.2023.284945, doi:10.3324/haematol.2023.284945. This article has 17 citations.

30. (fahim2024imetelstatforanemia pages 2-3): Shahariar Mohammed Fahim, Jeffrey A. Tice, Linda Luu, Josh J. Carlson, Marina Richardson, Belen Herce-Hagiwara, Ronald Dickerson, and Daniel A. Ollendorf. Imetelstat for anemia in lower-risk myelodysplastic syndromes: a summary from the institute for clinical and economic review's california technology assessment forum. Journal of managed care & specialty pharmacy, 30 12:1479-1485, Dec 2024. URL: https://doi.org/10.18553/jmcp.2024.30.12.1479, doi:10.18553/jmcp.2024.30.12.1479. This article has 0 citations.

31. (stempel2025advancesandchallenges pages 13-15): J. Stempel, Tariq Kewan, and A. Zeidan. Advances and challenges in the management of myelodysplastic syndromes. Cancers, Jul 2025. URL: https://doi.org/10.3390/cancers17152469, doi:10.3390/cancers17152469. This article has 6 citations.

32. (munteanu2025humanizedmousemodels pages 2-3): R. Munteanu, Diana Gulei, C. Moldovan, Emanuele Azzoni, Laura Belver, Richard-Ionut Feder, Simina Pîrv, A. Buzoianu, Hermann Einsele, Moshe Mittelman, Gabriel Ghiaur, Robert P Hasserjian, and C. Tomuleasa. Humanized mouse models in mds. Cell Death & Disease, Jul 2025. URL: https://doi.org/10.1038/s41419-025-07861-0, doi:10.1038/s41419-025-07861-0. This article has 4 citations and is from a peer-reviewed journal.

33. (munteanu2025humanizedmousemodels pages 7-7): R. Munteanu, Diana Gulei, C. Moldovan, Emanuele Azzoni, Laura Belver, Richard-Ionut Feder, Simina Pîrv, A. Buzoianu, Hermann Einsele, Moshe Mittelman, Gabriel Ghiaur, Robert P Hasserjian, and C. Tomuleasa. Humanized mouse models in mds. Cell Death & Disease, Jul 2025. URL: https://doi.org/10.1038/s41419-025-07861-0, doi:10.1038/s41419-025-07861-0. This article has 4 citations and is from a peer-reviewed journal.

34. (munteanu2025humanizedmousemodels pages 5-7): R. Munteanu, Diana Gulei, C. Moldovan, Emanuele Azzoni, Laura Belver, Richard-Ionut Feder, Simina Pîrv, A. Buzoianu, Hermann Einsele, Moshe Mittelman, Gabriel Ghiaur, Robert P Hasserjian, and C. Tomuleasa. Humanized mouse models in mds. Cell Death & Disease, Jul 2025. URL: https://doi.org/10.1038/s41419-025-07861-0, doi:10.1038/s41419-025-07861-0. This article has 4 citations and is from a peer-reviewed journal.

35. (munteanu2025humanizedmousemodels pages 1-2): R. Munteanu, Diana Gulei, C. Moldovan, Emanuele Azzoni, Laura Belver, Richard-Ionut Feder, Simina Pîrv, A. Buzoianu, Hermann Einsele, Moshe Mittelman, Gabriel Ghiaur, Robert P Hasserjian, and C. Tomuleasa. Humanized mouse models in mds. Cell Death & Disease, Jul 2025. URL: https://doi.org/10.1038/s41419-025-07861-0, doi:10.1038/s41419-025-07861-0. This article has 4 citations and is from a peer-reviewed journal.

36. (munteanu2025humanizedmousemodels pages 8-10): R. Munteanu, Diana Gulei, C. Moldovan, Emanuele Azzoni, Laura Belver, Richard-Ionut Feder, Simina Pîrv, A. Buzoianu, Hermann Einsele, Moshe Mittelman, Gabriel Ghiaur, Robert P Hasserjian, and C. Tomuleasa. Humanized mouse models in mds. Cell Death & Disease, Jul 2025. URL: https://doi.org/10.1038/s41419-025-07861-0, doi:10.1038/s41419-025-07861-0. This article has 4 citations and is from a peer-reviewed journal.

37. (stempel2025advancesandchallenges pages 15-16): J. Stempel, Tariq Kewan, and A. Zeidan. Advances and challenges in the management of myelodysplastic syndromes. Cancers, Jul 2025. URL: https://doi.org/10.3390/cancers17152469, doi:10.3390/cancers17152469. This article has 6 citations.

38. (vicente2024whoiccclassificationfor pages 1-2): Ana Isabel Vicente, Irene Luna, Juan Carlos Ruiz, María José Remigia, Andrés Jerez, Rafael Lluch, Inmaculada Llopis, María Josefa Marco, Carmen Benet, Carmen Alonso, María Dolores Linares, Luis Serrano, María Teresa Orero, Francisco José Ortuño, and María Leonor Senent. Who/icc classification for myelodysplastic neoplasms/syndromes performs better for subtype cytomorphological diagnosis? Diagnostics, 14:1631, Jul 2024. URL: https://doi.org/10.3390/diagnostics14151631, doi:10.3390/diagnostics14151631. This article has 2 citations.

## Artifacts

- [Edison artifact artifact-00](Myelodysplastic_Syndrome-deep-research-falcon_artifacts/artifact-00.md)