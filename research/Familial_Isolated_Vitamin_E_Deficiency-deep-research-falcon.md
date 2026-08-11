---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-03T23:02:14.134652'
end_time: '2026-06-03T23:11:11.758834'
duration_seconds: 537.62
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Familial Isolated Vitamin E Deficiency
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 21
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Familial_Isolated_Vitamin_E_Deficiency-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Familial Isolated Vitamin E Deficiency
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Familial Isolated Vitamin E Deficiency** covering all of the
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
- **Disease Name:** Familial Isolated Vitamin E Deficiency
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Familial Isolated Vitamin E Deficiency** covering all of the
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


# Familial Isolated Vitamin E Deficiency (AVED) — Comprehensive Disease Characteristics Report

## 1. Disease Information

### Overview / definition
Familial isolated vitamin E deficiency—also referred to as *ataxia with isolated vitamin E deficiency* (AVED)—is a rare, **potentially treatable autosomal recessive neurodegenerative disorder** caused by impaired hepatic handling/transport of α‑tocopherol (vitamin E), leading to **very low circulating vitamin E** and progressive neurologic disease resembling Friedreich ataxia (FA). (holla2024geneticallyprovenataxia pages 1-2, hoshino1999ataxiawithisolated pages 22-23)

### Key identifiers and nomenclature
* **OMIM/MIM disease number:** **277460** (explicitly stated) (hoshino1999ataxiawithisolated pages 22-23)
* **Gene OMIM noted in one source:** **TTPA OMIM*600415** (referenced in a case report) (zhang2021clinicalandgenetic pages 1-4)
* **Orphanet / ICD‑10 / ICD‑11 / MeSH / MONDO:** Not retrievable from the currently available full-text evidence in this run; therefore not reported here.

### Synonyms / alternative names
* Ataxia with isolated vitamin E deficiency (AVED) (hoshino1999ataxiawithisolated pages 22-23)
* Ataxia with vitamin E deficiency (hoshino1999ataxiawithisolated pages 22-23)
* Familial isolated vitamin E deficiency (used interchangeably with AVED in the literature) (cavalier1998ataxiawithisolated pages 7-8)

### Evidence sources (individual vs aggregated)
The information summarized here is derived primarily from **aggregated cohorts** (e.g., multicenter family series) and **individual case reports** describing biochemically and genetically confirmed AVED. (cavalier1998ataxiawithisolated pages 7-8, holla2024geneticallyprovenataxia pages 1-2, iwasa2014retinitispigmentosaand pages 2-3, hoshino1999ataxiawithisolated pages 22-23)


## 2. Etiology

### Disease causal factors
**Primary cause:** biallelic pathogenic variants in **TTPA**, encoding α‑tocopherol transfer protein (α‑TTP/αTTP). (holla2024geneticallyprovenataxia pages 1-2, hoshino1999ataxiawithisolated pages 22-23)

Mechanistically, α‑TTP binds α‑tocopherol and supports its incorporation into circulating lipoproteins (e.g., VLDL); dysfunction yields **very low serum/plasma vitamin E** despite preserved intestinal absorption. (holla2024geneticallyprovenataxia pages 1-2, iwasa2014retinitispigmentosaand pages 2-3)

### Risk factors
* **Genetic:** autosomal recessive inheritance; consanguinity appears in some families/case reports. (esmer2013clinicalandmolecular pages 2-4, hoshino1999ataxiawithisolated pages 22-23)
* **Environmental:** not a primary driver in AVED; however, prolonged untreated deficiency is a major risk for irreversible neurologic sequelae (see prognosis/treatment). (esmer2013clinicalandmolecular pages 2-4, cavalier1998ataxiawithisolated pages 7-8)

### Protective factors
* **Early, sustained vitamin E supplementation** is repeatedly emphasized as protective against progression and irreversible damage. (esmer2013clinicalandmolecular pages 2-4, cavalier1998ataxiawithisolated pages 7-8)

### Gene–environment interactions
Direct gene–environment interactions were not described in the available evidence. The most actionable interaction is **genotype × timing of treatment**, where delayed supplementation is associated with incomplete reversibility of neurologic deficits. (esmer2013clinicalandmolecular pages 2-4)


## 3. Phenotypes

### Core clinical phenotype
AVED typically presents with a FA-like neurologic syndrome including:
* **Progressive gait/limb ataxia** (stoiloudis2022vitaminedeficiency pages 42-44, hoshino1999ataxiawithisolated pages 22-23)
* **Hyporeflexia/areflexia** (stoiloudis2022vitaminedeficiency pages 42-44, hoshino1999ataxiawithisolated pages 22-23)
* **Loss of proprioception and vibration sense** (posterior column involvement) (stoiloudis2022vitaminedeficiency pages 42-44, hoshino1999ataxiawithisolated pages 22-23)
* **Dysarthria** (stoiloudis2022vitaminedeficiency pages 42-44)
* **Peripheral neuropathy/sensory involvement** (iwasa2014retinitispigmentosaand pages 2-3)

Additional/variable features:
* **Head titubation / tremor; dystonia** (cavalier1998ataxiawithisolated pages 7-8, stoiloudis2022vitaminedeficiency pages 42-44)
* **Extensor plantar response / Babinski** (stoiloudis2022vitaminedeficiency pages 42-44)
* **Retinopathy/retinitis pigmentosa; macular degeneration** in some individuals, particularly with long-standing deficiency (iwasa2014retinitispigmentosaand pages 2-3, hoshino1999ataxiawithisolated pages 22-23)
* **Cardiomyopathy** occurs but at lower frequency than FA in cohort data (cavalier1998ataxiawithisolated pages 7-8, stoiloudis2022vitaminedeficiency pages 42-44)

### Phenotype statistics from a recent compiled frequency table
A review snippet reports phenotype frequencies (interpretable as proportion of affected individuals in the compiled dataset):
* Absent tendon reflexes **94.7%**
* Gait disturbance **93.4%**
* Plantar extensor response **85.5%**
* Posterior column involvement **67.1%**
* Speech disturbance/dysarthria **61.8%**
* Head titubation **40.8%**
* Retinitis pigmentosa **2.3%**
* Cardiomyopathy **1.5%** (stoiloudis2022vitaminedeficiency pages 42-44)

A large family series found cardiomyopathy **19%**, head titubation **28%**, and dystonia **13%** (in addition to the FA-like presentation). (cavalier1998ataxiawithisolated pages 7-8)

### Age of onset and progression
* Typical onset is **late childhood to early adolescence**, but reports include onset ranging from **early childhood/infancy to adulthood** (including the 4th decade in some descriptions). (holla2024geneticallyprovenataxia pages 1-2, zhang2021clinicalandgenetic pages 1-4)
* Untreated disease is described as generally manifesting **between ages 5 and 15 years** in one definition-style source. (esmer2013clinicalandmolecular pages 2-4)

### Suggested HPO terms (examples)
* Cerebellar ataxia — **HP:0001251**
* Areflexia — **HP:0001284**
* Loss of proprioception — **HP:0002355** (or related sensory ataxia terms)
* Decreased vibratory sensation — **HP:0002495**
* Dysarthria — **HP:0001260**
* Peripheral neuropathy — **HP:0009830**
* Head tremor / titubation — **HP:0002326** (tremor)
* Dystonia — **HP:0001332**
* Retinitis pigmentosa — **HP:0000510**
* Cardiomyopathy — **HP:0001638**

(These HPO codes are suggested to standardize phenotype capture; detailed mapping should be verified against the current HPO release.)


## 4. Genetic / Molecular Information

### Causal gene
* **TTPA** (α‑tocopherol transfer protein gene). (holla2024geneticallyprovenataxia pages 1-2, hoshino1999ataxiawithisolated pages 22-23)

### Protein and molecular role
α‑TTP binds α‑tocopherol and enables its export from the liver into circulating lipoproteins (described as incorporation into VLDL), supporting systemic delivery of vitamin E; deficiency leads to neuronal oxidative injury. (holla2024geneticallyprovenataxia pages 1-2, iwasa2014retinitispigmentosaand pages 2-3)

### Inheritance
Autosomal recessive; many reported individuals are homozygous in consanguineous families or biallelic (including compound heterozygous) in non-consanguineous settings. (holla2024geneticallyprovenataxia pages 1-2, hoshino1999ataxiawithisolated pages 22-23)

### Pathogenic variants (examples explicitly described in retrieved evidence)
* **c.744delA** — repeatedly highlighted as a major mutation in North Africa / Mediterranean and associated with earlier/severe course in some reports (esmer2013clinicalandmolecular pages 2-4, zhang2021clinicalandgenetic pages 1-4)
* **c.513_514insTT**, **c.486delT**, **c.400C>T** (European-origin recurrent mutations noted in one report) (esmer2013clinicalandmolecular pages 2-4)
* **c.205-1G>C** (splice-site; exon 2 skipping with premature stop described) (esmer2013clinicalandmolecular pages 2-4)
* **c.717delC (p.D239EfsX25)** (frameshift; associated with retinal disease in a case report) (iwasa2014retinitispigmentosaand pages 2-3)
* **NM_000370.3:c.58dupC (p.His20ProfsTer56)** (frameshift; 2024 case report) (holla2024geneticallyprovenataxia pages 1-2)
* **c.473C>T (p.Phe185Ser)** (novel homozygous variant in a 2021 report) (zhang2021clinicalandgenetic pages 1-4)
* **Start-codon abolishing variant** (Japanese family; “abolishes the start codon”) (hoshino1999ataxiawithisolated pages 23-24)

### Genotype–phenotype correlation
One large series distinguished milder vs more severe functional classes and reported that some missense variants (e.g., H101Q) can be associated with milder, later-onset phenotypes, whereas truncating/nonconservative variants associate with earlier/severe disease. (cavalier1998ataxiawithisolated pages 7-8)

### Population allele frequencies / gnomAD
Population allele frequencies were not available in the retrieved evidence and are not reported here.


## 5. Environmental Information

AVED is fundamentally genetic; non-genetic contributors are mainly **secondary causes of vitamin E deficiency** that are important for differential diagnosis (e.g., fat malabsorption syndromes) rather than etiologic contributors to familial isolated deficiency. Cohort/case evidence emphasizes that AVED patients can have intact intestinal absorption with low circulating vitamin E. (holla2024geneticallyprovenataxia pages 1-2, cavalier1998ataxiawithisolated pages 7-8)


## 6. Mechanism / Pathophysiology

### Causal chain (current understanding from retrieved evidence)
1. **Biallelic TTPA pathogenic variants** → defective α‑TTP function (holla2024geneticallyprovenataxia pages 1-2, hoshino1999ataxiawithisolated pages 22-23)
2. Impaired hepatic handling/export of α‑tocopherol via circulating lipoproteins (VLDL described) → **very low serum/plasma α‑tocopherol** despite intact absorption (holla2024geneticallyprovenataxia pages 1-2, iwasa2014retinitispigmentosaand pages 2-3)
3. Reduced antioxidant capacity in nervous system → **oxidative injury to neurons** (explicitly invoked as mechanism in a 2024 case report) (holla2024geneticallyprovenataxia pages 1-2)
4. Progressive neurodegeneration of cerebellar and sensory pathways → ataxia, proprioceptive loss, neuropathy, pyramidal signs, and in some patients retinal degeneration and cardiomyopathy. (stoiloudis2022vitaminedeficiency pages 42-44, iwasa2014retinitispigmentosaand pages 2-3)

### Molecular pathways / processes (ontology suggestions)
* **GO Biological Process (suggested):**
  * response to oxidative stress — GO:0006979
  * lipid transport — GO:0006869
  * regulation of lipid localization — GO:1905952
* **GO Cellular Component (suggested):**
  * very-low-density lipoprotein particle — GO:0034361
* **Cell types (CL suggestions):**
  * hepatocyte — CL:0000182 (site of major α‑TTP expression/function implied by hepatic export role)
  * neuron — CL:0000540 (target of oxidative injury)

(These terms are proposed for KB standardization; the retrieved evidence provides qualitative support for oxidative injury and lipoprotein-mediated trafficking but does not provide a full pathway map.)

### Molecular profiling (transcriptomics/proteomics/metabolomics)
Not reported in the retrieved evidence.


## 7. Anatomical Structures Affected

### Primary systems/organs
* **Nervous system** (cerebellar and sensory pathways; peripheral nerves) (stoiloudis2022vitaminedeficiency pages 42-44, iwasa2014retinitispigmentosaand pages 2-3)
* **Eye/retina** in a subset (retinitis pigmentosa; macular degeneration) (iwasa2014retinitispigmentosaand pages 2-3, hoshino1999ataxiawithisolated pages 22-23)
* **Heart** in a subset (cardiomyopathy) (cavalier1998ataxiawithisolated pages 7-8, stoiloudis2022vitaminedeficiency pages 42-44)

### Suggested UBERON terms (examples)
* cerebellum — UBERON:0002037
* spinal cord (posterior columns implied) — UBERON:0002240
* peripheral nerve — UBERON:0001021
* retina — UBERON:0000966
* heart — UBERON:0000948


## 8. Temporal Development

### Onset
Typically late childhood/early adolescence, but can range to adult onset depending on genotype and other factors. (holla2024geneticallyprovenataxia pages 1-2, zhang2021clinicalandgenetic pages 1-4)

### Course
Progressive without treatment; vitamin E therapy can halt progression and stabilize or partially improve signs, especially when initiated early. (esmer2013clinicalandmolecular pages 2-4, cavalier1998ataxiawithisolated pages 7-8, mariotti2004ataxiawithisolated pages 7-10)


## 9. Inheritance and Population

### Inheritance pattern
**Autosomal recessive**. (holla2024geneticallyprovenataxia pages 1-2, hoshino1999ataxiawithisolated pages 22-23)

### Epidemiology / distribution
Robust prevalence/incidence estimates were not available in the retrieved evidence. However:
* Recurrent mutation patterns suggest enrichment in **North Africa / Mediterranean** populations (e.g., c.744delA described as a major mutation in North Africa). (esmer2013clinicalandmolecular pages 2-4)

### Founder effects
Founder/recurrent alleles are reported in specific regions:
* **c.744delA**: emphasized as a major/frequent mutation in North Africa / Mediterranean (esmer2013clinicalandmolecular pages 2-4, zhang2021clinicalandgenetic pages 1-4)
* Additional recurrent European-origin alleles noted: **c.513_514insTT**, **c.486delT**, **c.400C>T** (esmer2013clinicalandmolecular pages 2-4)

Carrier frequency and penetrance were not provided in the retrieved evidence.


## 10. Diagnostics

### Core diagnostic pattern (real-world implementation)
AVED is suggested by:
1. **Neurologic syndrome resembling FA** (ataxia, areflexia, posterior column signs) (hoshino1999ataxiawithisolated pages 22-23)
2. **Markedly low plasma/serum α‑tocopherol (vitamin E)** with otherwise non-explanatory routine workup; multiple case reports emphasize low α‑tocopherol (e.g., 0.12 mg/dL reported in one case) (iwasa2014retinitispigmentosaand pages 2-3)
3. Evidence that intestinal absorption may be intact and lipid profile may be normal (noted explicitly in a 2024 case report and other descriptions) (holla2024geneticallyprovenataxia pages 1-2, vera2021pearls&amp;oysters pages 1-5)
4. **Confirmatory genetic testing** demonstrating biallelic TTPA pathogenic variants (holla2024geneticallyprovenataxia pages 1-2)

One report states that diagnostic testing should include α‑tocopherol determination and that AVED levels should be **<1.7 mg/L**. (esmer2013clinicalandmolecular pages 2-4)

### Genetic testing modalities
Evidence supports use of:
* **Single-gene sequencing of TTPA** (with exon/intron junction evaluation in one report; mutation detection rate stated as ~90% in that source) (esmer2013clinicalandmolecular pages 2-4)
* **Whole exome sequencing (WES)** as a practical route to diagnosis after excluding common ataxias (zhang2021clinicalandgenetic pages 1-4)

### Differential diagnosis (examples from evidence context)
* Friedreich ataxia (clinical resemblance is explicitly emphasized) (cavalier1998ataxiawithisolated pages 7-8, hoshino1999ataxiawithisolated pages 22-23)
* Other causes of vitamin E deficiency (e.g., fat malabsorption syndromes) should be excluded when interpreting low vitamin E; AVED differs by preserved absorption and isolated deficiency. (holla2024geneticallyprovenataxia pages 1-2)


## 11. Outcome / Prognosis

### Natural history
Without therapy, AVED is progressive and can lead to substantial disability. (esmer2013clinicalandmolecular pages 2-4)

### Treatment-modified prognosis
Multiple sources stress that **early initiation of vitamin E** can halt progression and may improve established signs, whereas delayed therapy may leave residual irreversible deficits (e.g., persistent proprioceptive/gait impairment). (esmer2013clinicalandmolecular pages 2-4, cavalier1998ataxiawithisolated pages 7-8)


## 12. Treatment

### Disease-specific therapy: vitamin E replacement
High-dose **oral vitamin E (α‑tocopherol)** is the central disease-modifying intervention.

Evidence-based statements on benefit:
* “The administration of vitamin E supplements in divided doses daily has resulted in cessation of progression … and in amelioration of established neurological abnormalities.” (cavalier1998ataxiawithisolated pages 7-8)
* Early supplementation is highlighted as necessary “before irreversible damage develops.” (cavalier1998ataxiawithisolated pages 7-8)

#### Dosing (examples explicitly reported)
* Recommended range **800–1500 mg/day** or **~40 mg/kg/day in children** (esmer2013clinicalandmolecular pages 2-4)
* Case regimens: **800 mg/day** (iwasa2014retinitispigmentosaand pages 2-3); **400 mg three times daily** (zhang2021clinicalandgenetic pages 1-4); **1,200 IU/day** (holla2024geneticallyprovenataxia pages 1-2); **2,000 units/day** (vera2021pearls&amp;oysters pages 1-5)

#### Outcomes
* Stabilization over 2 years with 400 mg TID in one case report (zhang2021clinicalandgenetic pages 1-4)
* Stabilization (no improvement) reported after short follow-up in a 2024 case report treated with 1,200 IU/day (holla2024geneticallyprovenataxia pages 1-2)
* Long-term therapy “led to stabilization of neurological status in most patients” in an Italian cohort report. (mariotti2004ataxiawithisolated pages 7-10)

### Supportive/rehabilitative therapies
Symptomatic pharmacotherapy may be used for movement disorder components (e.g., dystonia treated with clonazepam and trihexyphenidyl in a 2024 case report). (holla2024geneticallyprovenataxia pages 1-2)

### Suggested MAXO terms (examples)
* Vitamin supplementation — **MAXO:0000112** (vitamin E supplementation as subtype)
* Dietary supplement therapy — **MAXO:0000087**
* Genetic counseling — **MAXO:0000077** (mentioned as part of management planning in reviews/clinical practice; monitoring and counseling are explicitly recommended in one review snippet) (stoiloudis2022vitaminedeficiency pages 42-44)


## 13. Prevention

### Primary/secondary/tertiary prevention
In AVED, “prevention” is primarily **secondary/tertiary** through:
* Early biochemical screening for vitamin E deficiency in patients with FA-like ataxia and prompt genetic confirmation (cavalier1998ataxiawithisolated pages 7-8)
* Lifelong vitamin E therapy to prevent progression/complications (esmer2013clinicalandmolecular pages 2-4)

Prenatal/preimplantation options were not discussed in the retrieved evidence.


## 14. Other Species / Natural Disease

Cross-species disease analogs for *TTPA* were not established in the retrieved evidence for AVED itself.


## 15. Model Organisms

The retrieved evidence set used for this report did not include detailed model organism phenotyping for AVED; therefore model organism details are not reported here.


## Recent developments and latest research (prioritizing 2023–2024)

### 2024: Phenotypic expansion / diagnostic reminder
A 2024 case report emphasizes that AVED can present with **prominent cervicobrachial dystonic tremor** and may have **normal MRI**, reinforcing the need to consider AVED in atypical movement disorder presentations because it is “potentially treatable.” (Journal of Movement Disorders, Apr 2024; https://doi.org/10.14802/jmd.23227) (holla2024geneticallyprovenataxia pages 1-2)

### Ongoing research gap
Within the retrieved evidence, there were **no disease-specific interventional clinical trials** captured for AVED, consistent with AVED management being dominated by replacement therapy rather than novel therapeutics (clinical trial retrieval returned no relevant AVED trials). 


## Practical applications / real-world implementation summary

* **Clinical workflow:** FA-like ataxia → check serum/plasma α‑tocopherol → if markedly low and not explained by malabsorption/lipid abnormalities → sequence **TTPA** (or use WES panels for recessive ataxia) → begin high-dose vitamin E promptly and monitor serum vitamin E and neurologic progression. (cavalier1998ataxiawithisolated pages 7-8, holla2024geneticallyprovenataxia pages 1-2, zhang2021clinicalandgenetic pages 1-4)


## Structured summary table

| Disease / synonym(s) | Key identifiers explicitly supported in evidence | Causal gene / protein | Inheritance | Hallmark laboratory finding | Typical onset | Core phenotypes (with frequency when available) | Recurrent / founder or notable variants mentioned | Treatment and outcomes | Key references |
|---|---|---|---|---|---|---|---|---|---|
| Familial isolated vitamin E deficiency; Ataxia with isolated vitamin E deficiency (AVED); Ataxia with vitamin E deficiency (cavalier1998ataxiawithisolated pages 7-8, hoshino1999ataxiawithisolated pages 22-23) | OMIM/MIM **277460** explicitly stated for AVED (hoshino1999ataxiawithisolated pages 22-23); TTPA transcript/protein entry noted as **OMIM*600415** in one report (zhang2021clinicalandgenetic pages 1-4) | **TTPA** encoding **α-tocopherol transfer protein (α-TTP / αTTP)**; α-TTP binds α-tocopherol and mediates incorporation into VLDL / circulating lipoproteins (zhang2021clinicalandgenetic pages 1-4, iwasa2014retinitispigmentosaand pages 2-3) | **Autosomal recessive**; biallelic / homozygous or compound heterozygous TTPA variants reported (holla2024geneticallyprovenataxia pages 1-2, hoshino1999ataxiawithisolated pages 22-23) | Markedly **low plasma/serum vitamin E (α-tocopherol)** despite intact intestinal absorption and otherwise normal lipids in reported cases; one snippet notes AVED levels should be **<1.7 mg/L** (esmer2013clinicalandmolecular pages 2-4, vera2021pearls&amp;oysters pages 1-5, holla2024geneticallyprovenataxia pages 1-2) | Usually **late childhood to early adolescence**; broader reported range from **early childhood/infancy to adulthood/fourth decade**; untreated disease often manifests **5–15 years** (holla2024geneticallyprovenataxia pages 1-2, zhang2021clinicalandgenetic pages 1-4, hoshino1999ataxiawithisolated pages 22-23) | Friedreich-like phenotype with **progressive ataxia**, **areflexia/hyporeflexia**, loss of **proprioception/vibration sense**, **dysarthria**, sensory neuropathy; extra-neurologic/other features can include **head titubation/dystonia**, retinitis pigmentosa, scoliosis, cardiomyopathy. Frequency data from one review: absent tendon reflexes **94.7%**, gait disturbance **93.4%**, extensor plantar response **85.5%**, posterior column involvement **67.1%**, dysarthria **61.8%**, head titubation **40.8%**, retinitis pigmentosa **2.3%**, cardiomyopathy **1.5%** (stoiloudis2022vitaminedeficiency pages 42-44). Earlier cohort found cardiomyopathy **19%**, head titubation **28%**, dystonia **13%** (cavalier1998ataxiawithisolated pages 7-8). | Recurrent/founder variants mentioned: **c.744delA** major in **North Africa / Mediterranean** and associated with earlier/severe disease; **c.513_514insTT**, **c.486delT**, **c.400C>T (R134X)** in European-origin families; **H101Q** associated with milder, late-onset phenotype; additional reported variants include **c.205-1G>C**, **c.473C>T (p.F185S)**, **c.717delC (p.D239EfsX25)**, **c.58dupC (p.His20ProfsTer56)**, and a start-codon mutation in a Japanese family (esmer2013clinicalandmolecular pages 2-4, cavalier1998ataxiawithisolated pages 7-8, holla2024geneticallyprovenataxia pages 1-2, zhang2021clinicalandgenetic pages 1-4, iwasa2014retinitispigmentosaand pages 2-3, hoshino1999ataxiawithisolated pages 22-23) | Lifelong **high-dose oral vitamin E** replacement. Reported recommendations/examples: **800–1500 mg/day** or about **40 mg/kg/day in children**; case regimens include **800 mg/day**, **400 mg three times daily**, **1,200 IU/day**, and **2,000 units/day**. Early treatment can **halt progression**, **stabilize** disease, and sometimes improve established neurologic abnormalities; delayed treatment may leave persistent proprioceptive/gait deficits (esmer2013clinicalandmolecular pages 2-4, vera2021pearls&amp;oysters pages 1-5, holla2024geneticallyprovenataxia pages 1-2, zhang2021clinicalandgenetic pages 1-4, iwasa2014retinitispigmentosaand pages 2-3, cavalier1998ataxiawithisolated pages 7-8, mariotti2004ataxiawithisolated pages 7-10) | Cavalier 1998, Am J Hum Genet, DOI: https://doi.org/10.1086/301699 (cavalier1998ataxiawithisolated pages 7-8); Hoshino 1999, Ann Neurol, DOI: https://doi.org/10.1002/1531-8249(199906)45:6<809::aid-ana19>3.0.co;2-9 (hoshino1999ataxiawithisolated pages 22-23); Iwasa 2014, J Neurol Sci, DOI: https://doi.org/10.1016/j.jns.2014.07.001 (iwasa2014retinitispigmentosaand pages 2-3); Holla 2024, J Mov Disord, DOI: https://doi.org/10.14802/jmd.23227 (holla2024geneticallyprovenataxia pages 1-2) |


*Table: This table condenses the evidence-backed core facts for familial isolated vitamin E deficiency / AVED, including identifiers, genetics, phenotype, variants, and treatment. It is useful as a quick reference for knowledge-base population while limiting claims to those explicitly present in the provided snippets.*


## URLs and publication dates (from retrieved evidence)
* Cavalier et al., 1998-02, *American Journal of Human Genetics*: https://doi.org/10.1086/301699 (cavalier1998ataxiawithisolated pages 7-8)
* Hoshino et al., 1999-06, *Annals of Neurology*: https://doi.org/10.1002/1531-8249(199906)45:6<809::aid-ana19>3.0.co;2-9 (hoshino1999ataxiawithisolated pages 23-24)
* Iwasa et al., 2014-10, *Journal of the Neurological Sciences*: https://doi.org/10.1016/j.jns.2014.07.001 (iwasa2014retinitispigmentosaand pages 1-2)
* Zea Vera et al., 2021-01, *Neurology*: https://doi.org/10.1212/WNL.0000000000010853 (vera2021pearls&amp;oysters pages 1-5)
* Holla et al., 2024-04, *Journal of Movement Disorders*: https://doi.org/10.14802/jmd.23227 (holla2024geneticallyprovenataxia pages 1-2)


## Notes on limitations of this tool-based report
* Ontology identifiers beyond OMIM (e.g., Orphanet, MONDO, MeSH, ICD-10/11) could not be verified from the retrieved full-text evidence in this run and are therefore omitted rather than inferred.
* Population prevalence/incidence and population allele frequencies (gnomAD) were not present in the retrieved evidence snippets.
* Model organism evidence was not present in the retrieved evidence snippets used for citation; therefore it is not summarized here.


References

1. (holla2024geneticallyprovenataxia pages 1-2): Vikram V. Holla, Sandeep Gurram, Sneha D. Kamath, Gautham Arunachal, Nitish Kamble, Ravi Yadav, and Pramod Kumar Pal. Genetically proven ataxia with vitamin e deficiency with predominant cervicobrachial dystonic presentation: a case report from india. Journal of Movement Disorders, 17:220-222, Apr 2024. URL: https://doi.org/10.14802/jmd.23227, doi:10.14802/jmd.23227. This article has 0 citations and is from a peer-reviewed journal.

2. (hoshino1999ataxiawithisolated pages 22-23): Masataka Hoshino, Naoki Masuda, Yasuhiko Ito, Miho Murata, Jun Goto, Masaki Sakurai, and Ichiro Kanazawa. Ataxia with isolated vitamin e deficiency: a japanese family carrying a novel mutation in the α‐tocopherol transfer protein gene. Annals of Neurology, 45:809-812, Jun 1999. URL: https://doi.org/10.1002/1531-8249(199906)45:6<809::aid-ana19>3.0.co;2-9, doi:10.1002/1531-8249(199906)45:6<809::aid-ana19>3.0.co;2-9. This article has 38 citations and is from a highest quality peer-reviewed journal.

3. (zhang2021clinicalandgenetic pages 1-4): Linwei Zhang, Xiangfei Zhang, Pu Lv, and Dantao Peng. Clinical and genetic study of ataxia with vitamin e deficiency. ArXiv, Feb 2021. URL: https://doi.org/10.21203/rs.3.rs-175944/v1, doi:10.21203/rs.3.rs-175944/v1. This article has 0 citations.

4. (cavalier1998ataxiawithisolated pages 7-8): Laurent Cavalier, Karim Ouahchi, Herbert J. Kayden, Stephano Di Donato, Laurence Reutenauer, Jean-Louis Mandel, and Michel Koenig. Ataxia with isolated vitamin e deficiency: heterogeneity of mutations and phenotypic variability in a large number of families. American journal of human genetics, 62 2:301-10, Feb 1998. URL: https://doi.org/10.1086/301699, doi:10.1086/301699. This article has 383 citations and is from a highest quality peer-reviewed journal.

5. (iwasa2014retinitispigmentosaand pages 2-3): Kazuo Iwasa, Keisuke Shima, Kiyonobu Komai, Yoichiro Nishida, Takanori Yokota, and Masahito Yamada. Retinitis pigmentosa and macular degeneration in a patient with ataxia with isolated vitamin e deficiency with a novel c.717 del c mutation in the ttpa gene. Journal of the neurological sciences, 345 1-2:228-30, Oct 2014. URL: https://doi.org/10.1016/j.jns.2014.07.001, doi:10.1016/j.jns.2014.07.001. This article has 28 citations and is from a peer-reviewed journal.

6. (esmer2013clinicalandmolecular pages 2-4): C Esmer, AS Martínez, and ER Palomo. Clinical and molecular findings in a patient with ataxia with vitamin e deficiency, homozygous for the c. 205-1g› c mutation in the ttpa gene. Unknown journal, 2013.

7. (stoiloudis2022vitaminedeficiency pages 42-44): P Stoiloudis, AN Terzakis, and N Smyrni. Vitamin e deficiency: clinical characteristics, diagnosis and management. Unknown journal, 2022.

8. (hoshino1999ataxiawithisolated pages 23-24): Masataka Hoshino, Naoki Masuda, Yasuhiko Ito, Miho Murata, Jun Goto, Masaki Sakurai, and Ichiro Kanazawa. Ataxia with isolated vitamin e deficiency: a japanese family carrying a novel mutation in the α‐tocopherol transfer protein gene. Annals of Neurology, 45:809-812, Jun 1999. URL: https://doi.org/10.1002/1531-8249(199906)45:6<809::aid-ana19>3.0.co;2-9, doi:10.1002/1531-8249(199906)45:6<809::aid-ana19>3.0.co;2-9. This article has 38 citations and is from a highest quality peer-reviewed journal.

9. (mariotti2004ataxiawithisolated pages 7-10): C. Mariotti, C. Gellera, M. Rimoldi, R. Mineri, G. Uziel, G. Zorzi, D. Pareyson, G. Piccolo, D. Gambi, S. Piacentini, F. Squitieri, R. Capra, B. Castellotti, and S. Di Donato. Ataxia with isolated vitamin e deficiency: neurological phenotype, clinical follow-up and novel mutations in ttpagene in italian families. Neurological Sciences, 25:130-137, Jul 2004. URL: https://doi.org/10.1007/s10072-004-0246-z, doi:10.1007/s10072-004-0246-z. This article has 181 citations and is from a peer-reviewed journal.

10. (vera2021pearls&amp;oysters pages 1-5): Alonso Zea Vera, Wei Liu, Cameron Thomas, and Donald L. Gilbert. Pearls &amp; oy-sters: a novel presentation of ataxia with vitamin e deficiency caused by <i>ttpa</i> gene mutation. Jan 2021. URL: https://doi.org/10.1212/wnl.0000000000010853, doi:10.1212/wnl.0000000000010853. This article has 5 citations and is from a highest quality peer-reviewed journal.

11. (iwasa2014retinitispigmentosaand pages 1-2): Kazuo Iwasa, Keisuke Shima, Kiyonobu Komai, Yoichiro Nishida, Takanori Yokota, and Masahito Yamada. Retinitis pigmentosa and macular degeneration in a patient with ataxia with isolated vitamin e deficiency with a novel c.717 del c mutation in the ttpa gene. Journal of the neurological sciences, 345 1-2:228-30, Oct 2014. URL: https://doi.org/10.1016/j.jns.2014.07.001, doi:10.1016/j.jns.2014.07.001. This article has 28 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Familial_Isolated_Vitamin_E_Deficiency-deep-research-falcon_artifacts/artifact-00.md)