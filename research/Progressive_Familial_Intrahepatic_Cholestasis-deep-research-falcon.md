---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-01T04:59:34.695775'
end_time: '2026-08-01T05:13:04.644305'
duration_seconds: 809.95
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Progressive Familial Intrahepatic Cholestasis
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 51
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Progressive_Familial_Intrahepatic_Cholestasis-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Progressive Familial Intrahepatic Cholestasis
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Progressive Familial Intrahepatic Cholestasis** covering all of the
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
- **Disease Name:** Progressive Familial Intrahepatic Cholestasis
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Progressive Familial Intrahepatic Cholestasis** covering all of the
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


# Progressive Familial Intrahepatic Cholestasis (PFIC): comprehensive disease-characteristics report

**Scope and evidence date.** This synthesis prioritizes 2023–2024 peer-reviewed evidence, supported by landmark genetics and natural-history studies. Evidence is labeled as human clinical, registry/observational, review/expert opinion, or preclinical. Because PFIC is ultrarare and molecular nomenclature is evolving, precise subtype-level frequencies, penetrance, carrier frequencies, and several newer-gene natural histories remain uncertain.

## Executive summary

PFIC is not one disease but a genetically heterogeneous group of predominantly autosomal-recessive disorders in which defective hepatocellular bile formation or export causes intrahepatic cholestasis, often beginning in infancy. Typical manifestations are jaundice, very high serum bile acids, severe pruritus, fat and fat-soluble-vitamin malabsorption, growth failure, progressive fibrosis, portal hypertension, and eventually liver failure. Estimated incidence is approximately **1 per 50,000–100,000 births**. PFIC2/BSEP deficiency and TJP2 deficiency confer notable childhood hepatocellular-carcinoma (HCC) risk. (mckiernan2024opinionpaperon pages 1-3, henkel2019expandingetiologyof pages 6-8)

The major recent clinical advance is inhibition of the ileal bile-acid transporter (IBAT/ASBT; **SLC10A2**) to interrupt enterohepatic bile-acid recycling. In PEDFIC-1, odevixibat produced a pruritus response in **55% versus 30%** with placebo and a serum-bile-acid response in **33% versus 0%**, while longer-term and real-world studies indicate sustained benefit in many—but not all—patients. Complete BSEP loss predicts poor response, making genotype and residual transporter activity clinically actionable. (mckiernan2024opinionpaperon pages 4-5, marx2024practicalconsiderationsfor pages 1-2, mckiernan2024opinionpaperon pages 5-6, komaniecka2024transporterproteinsas pages 24-26)

## 1. Disease information

### Definition and classification

PFIC comprises Mendelian hepatocellular cholestasis disorders caused by defects in canalicular transporters, membrane lipid organization, tight-junction integrity, bile-acid sensing, or intracellular transporter trafficking. Although “progressive” remains in the name, expression ranges from episodic benign recurrent intrahepatic cholestasis (BRIC) to rapidly progressive neonatal liver failure. (mckiernan2024opinionpaperon pages 1-3, ziccardi2026beyondthepump pages 1-3, ziccardi2026beyondthepump pages 3-4)

**Identifiers and synonyms**

- **MONDO:** **MONDO:0015762**, progressive familial intrahepatic cholestasis. Subtype records include PFIC1 **MONDO:0008892**, PFIC2 **MONDO:0011156**, PFIC3 **MONDO:0011214**, and PFIC4 **MONDO:0014381**. (OpenTargets Search: Progressive familial intrahepatic cholestasis)
- **Orphanet:** commonly represented under **ORPHA:43708** (PFIC); subtype records also exist.
- **OMIM phenotype examples:** PFIC1/Byler disease **#211600**; PFIC2/BSEP deficiency **#601847**; PFIC3/MDR3 deficiency **#602347**; PFIC4/TJP2 deficiency **#615878**; PFIC5/FXR deficiency **#617049**. Subtype numbering beyond PFIC5 differs among publications; gene-first naming is safer.
- **MeSH:** *Cholestasis, Intrahepatic* is the principal broad indexing term; PFIC does not consistently have a unique MeSH heading.
- **ICD:** there is no universally used subtype-specific ICD-10 code. Cases are generally coded under **K76.89** (other specified diseases of liver), **K71.0/K83.1** where locally appropriate, or rare-disease extensions. ICD-11 similarly places inherited cholestatic disorders within hepatobiliary disease; coding should be verified against the deploying jurisdiction/version.
- **Synonyms:** familial intrahepatic cholestasis; Byler disease (historically PFIC1); FIC1 deficiency; BSEP deficiency; MDR3 deficiency; hereditary intrahepatic cholestasis; low-GGT familial cholestasis.

This report aggregates disease-level literature, registries, trials, and expert guidance; it is **not derived from an individual EHR**.

## 2. Etiology, risk, protective factors, and gene–environment interaction

### Causal factors

PFIC is fundamentally genetic. Classical causal genes are **ATP8B1, ABCB11, and ABCB4**; firmly established newer causes include **TJP2, NR1H4, MYO5B, USP53**, and additional PFIC/PFIC-like genes such as **KIF12, SLC51A, ZFYVE19, VPS33B/VIPAS39**. Open Targets associates 12 targets with the umbrella phenotype, with strongest evidence for ATP8B1, ABCB4, ABCB11, TJP2, and MYO5B. (OpenTargets Search: Progressive familial intrahepatic cholestasis)

| Subtype / common name | Causal gene / protein | Core molecular defect | Expected GGT pattern | Typical onset / key phenotype and extrahepatic clues | Prognosis / cancer or treatment-response notes |
|---|---|---|---|---|---|
| PFIC1 / FIC1 deficiency | **ATP8B1** / FIC1 (aminophospholipid flippase) | Loss of canalicular membrane lipid asymmetry and stability, impairing bile formation and promoting bile-acid toxicity (mckiernan2024opinionpaperon pages 1-3, henkel2019expandingetiologyof pages 2-4) | Usually **low/normal** (mckiernan2024opinionpaperon pages 1-3, henkel2019expandingetiologyof pages 2-4) | Neonatal or early-infantile cholestasis with jaundice, severe pruritus, hepatosplenomegaly, failure to thrive; extrahepatic clues include diarrhea, pancreatic insufficiency, short stature, elevated sweat chloride, sensorineural hearing loss (mckiernan2024opinionpaperon pages 1-3, henkel2019expandingetiologyof pages 2-4) | Progressive disease; native-liver survival improved when serum bile acids fall after diversion; residual extrahepatic disease may persist after transplant, including diarrhea/steatosis (mckiernan2024opinionpaperon pages 5-6, mckiernan2024opinionpaperon pages 3-4) |
| PFIC2 / BSEP deficiency | **ABCB11** / BSEP | Defective canalicular bile-salt export causing intracellular bile-salt retention and hepatocyte injury (mckiernan2024opinionpaperon pages 1-3, ziccardi2026beyondthepump pages 3-4, henkel2019expandingetiologyof pages 2-4) | Usually **low/normal** (mckiernan2024opinionpaperon pages 1-3, mckiernan2024opinionpaperon pages 3-4) | Early infancy; severe pruritus, cholestasis, rapid progression; genotype-defined severity spectrum with residual vs absent BSEP expression/function (marx2024practicalconsiderationsfor pages 1-2, ziccardi2026beyondthepump pages 10-12) | Generally the most severe common form; higher HCC risk, especially biallelic truncating / severe BSEP groups; poorer response to biliary diversion and IBAT inhibitors when BSEP is absent; risk of antibody-induced BSEP deficiency after transplant (mckiernan2024opinionpaperon pages 4-5, marx2024practicalconsiderationsfor pages 1-2, mckiernan2024opinionpaperon pages 5-6, mckiernan2024opinionpaperon pages 3-4, ziccardi2026beyondthepump pages 10-12) |
| PFIC3 / MDR3 deficiency | **ABCB4** / MDR3 | Impaired phosphatidylcholine secretion into bile, leaving bile acids insufficiently buffered and injuring cholangiocytes/hepatocytes (henkel2019expandingetiologyof pages 6-8, henkel2019expandingetiologyof pages 2-4) | Usually **high** (henkel2019expandingetiologyof pages 6-8, mckiernan2024opinionpaperon pages 3-4) | Often later infancy, childhood, adolescence, or adulthood; cholestasis with portal fibrosis and bile duct proliferation; heterozygotes may have milder phenotypes such as transient neonatal cholestasis, cholelithiasis, ICP, or drug-induced cholestasis (henkel2019expandingetiologyof pages 6-8) | Variable expressivity; carcinogenesis including cholangiocarcinoma/HCC reported in severe disease; generally not the main low-GGT/IBAT-responsive archetype (henkel2019expandingetiologyof pages 6-8) |
| PFIC4 / TJP2 deficiency | **TJP2** / tight junction protein 2 (ZO-2) | Tight-junction failure with claudin-1 mislocalization and paracellular reflux of toxic bile acids from canaliculi (henkel2019expandingetiologyof pages 6-8, vinayagamoorthy2021newervariantsof pages 2-4) | Usually **low/normal** (henkel2019expandingetiologyof pages 6-8, mckiernan2024opinionpaperon pages 3-4) | Often severe neonatal/infantile cholestasis; giant-cell transformation on histology; some patients have respiratory or neurologic features; phenotype can range from self-limited to progressive liver disease (henkel2019expandingetiologyof pages 6-8, vinayagamoorthy2021newervariantsof pages 2-4) | Increased HCC risk reported even in infancy; close surveillance recommended; severity variable across families (henkel2019expandingetiologyof pages 6-8, vinayagamoorthy2021newervariantsof pages 10-11) |
| PFIC5 / FXR deficiency | **NR1H4** / FXR | Loss of bile-acid sensing/transcriptional control, with impaired **ABCB11/BSEP** induction and defective repression of bile-acid synthesis (henkel2019expandingetiologyof pages 6-8, vinayagamoorthy2021newervariantsof pages 2-4) | Usually **low/normal** (henkel2019expandingetiologyof pages 6-8, vinayagamoorthy2021newervariantsof pages 10-11) | Neonatal cholestasis with markedly elevated bile acids; characteristic early coagulopathy that may be vitamin K-unresponsive; often high AFP (henkel2019expandingetiologyof pages 6-8, vinayagamoorthy2021newervariantsof pages 10-11, vinayagamoorthy2021newervariantsof pages 2-4) | Usually rapidly progressive with early liver failure and need for transplant; very rare (henkel2019expandingetiologyof pages 6-8) |
| MYO5B-related PFIC / isolated MYO5B cholestasis / “PFIC6” in some sources | **MYO5B** / myosin Vb | Rab11-dependent apical trafficking defect causing BSEP/MDR3 mislocalization away from the canalicular membrane; epithelial polarity defect (henkel2019expandingetiologyof pages 6-8, vinayagamoorthy2021newervariantsof pages 2-4, henkel2019expandingetiologyof pages 8-10) | Usually **low/normal** (vinayagamoorthy2021newervariantsof pages 10-11, vinayagamoorthy2021newervariantsof pages 6-7) | Infancy or early childhood; may present as isolated cholestasis, microvillus inclusion disease, or both; extrahepatic clue is intractable diarrhea/enteropathy when intestinal disease is present (henkel2019expandingetiologyof pages 6-8, vinayagamoorthy2021newervariantsof pages 10-11, vinayagamoorthy2021newervariantsof pages 6-7) | Post-intestinal-transplant cholestasis can worsen; combined liver-intestinal strategies or diversion may be needed in selected cases; phenotype highly variable (henkel2019expandingetiologyof pages 6-8, vinayagamoorthy2021newervariantsof pages 10-11, vinayagamoorthy2021newervariantsof pages 6-7) |
| USP53-related cholestasis *(newer nomenclature varies)* | **USP53** / USP53 | Tight-junction–associated defect; protein colocalizes/interacts with TJP2 pathway (henkel2019expandingetiologyof pages 8-10, ziccardi2026beyondthepump pages 4-5) | Usually **low/normal** (vinayagamoorthy2021newervariantsof pages 10-11) | Low-GGT cholestasis identified by exome sequencing; currently a rarer PFIC-like presentation with limited phenotype definition (vinayagamoorthy2021newervariantsof pages 10-11, ziccardi2026beyondthepump pages 4-5) | Natural history and treatment-response data remain sparse (vinayagamoorthy2021newervariantsof pages 10-11, ziccardi2026beyondthepump pages 4-5) |
| KIF12-related cholestasis *(sometimes mapped to a later-numbered PFIC; nomenclature varies)* | **KIF12** / kinesin family member 12 | Intracellular trafficking / motor-protein defect affecting hepatocellular bile transport pathways (ziccardi2026beyondthepump pages 4-5, ziccardi2026beyondthepump pages 3-4) | Often reported in the **low/normal-GGT PFIC-like** spectrum, but source conventions vary (ziccardi2026beyondthepump pages 4-5) | Pediatric cholestatic liver disease; detailed extrahepatic pattern remains less established than classical PFIC forms (ziccardi2026beyondthepump pages 4-5) | Evidence base is emerging; numbering and disease boundaries vary across reviews and databases (ziccardi2026beyondthepump pages 4-5) |
| ZFYVE19-related cholestasis *(newer/related PFIC-like gene; numbering varies)* | **ZFYVE19** / zinc finger FYVE-type containing 19 | Ciliary / trafficking-related mechanism proposed in PFIC-like cholestasis; evidence base remains limited in the retrieved sources (OpenTargets Search: Progressive familial intrahepatic cholestasis) | Not firmly established here | Reported as a newer PFIC-related gene in expanded molecular classifications, but detailed phenotype data were not available in the retrieved evidence set (OpenTargets Search: Progressive familial intrahepatic cholestasis) | Important emerging gene; requires confirmation from primary case literature in a full database curation workflow (OpenTargets Search: Progressive familial intrahepatic cholestasis) |
| SLC51A-related cholestasis / OSTα deficiency *(newer/related PFIC-like form; numbering varies)* | **SLC51A** / OSTα | Defect in basolateral bile-acid transport (organic solute transporter α), disturbing enterohepatic bile-acid handling (ziccardi2026beyondthepump pages 4-5) | Often grouped with **low/normal-GGT** PFIC-like disorders, but conventions vary (ziccardi2026beyondthepump pages 4-5) | Early-onset cholestatic phenotype in expanded classifications; detailed syndrome boundaries were not fully captured in the retrieved sources (ziccardi2026beyondthepump pages 4-5) | Limited outcome and treatment-response data in current retrieved evidence (ziccardi2026beyondthepump pages 4-5) |
| VPS33B / VIPAS39-related cholestasis (ARC spectrum; PFIC-like, not always numbered as PFIC) | **VPS33B** / VPS33B; **VIPAS39** / VIPAR | Vesicular trafficking / apical membrane biogenesis defect causing multisystem cholestasis syndrome (vinayagamoorthy2021newervariantsof pages 10-11, ziccardi2026beyondthepump pages 4-5) | Often **low/normal** in ARC-associated cholestasis, though syndrome-based classification is preferred (vinayagamoorthy2021newervariantsof pages 10-11, ziccardi2026beyondthepump pages 4-5) | Neonatal/infantile cholestasis with multisystem clues: arthrogryposis, renal tubular dysfunction, developmental issues; histology may show bile duct paucity, giant cells, bile plugs (vinayagamoorthy2021newervariantsof pages 10-11) | Usually severe syndromic disease; better viewed as a PFIC-like cholestatic disorder rather than classical isolated PFIC (vinayagamoorthy2021newervariantsof pages 10-11, ziccardi2026beyondthepump pages 4-5) |
| **Nomenclature note for newer forms** | — | Expanded PFIC numbering beyond PFIC1-5 is **not standardized across sources**; some reviews now include many later-numbered forms, whereas others prefer “PFIC-like” or gene-specific cholestasis terminology (ziccardi2026beyondthepump pages 3-4, ziccardi2026beyondthepump pages 4-5) | — | Gene-first reporting is often clearer than subtype numbering for USP53, KIF12, ZFYVE19, SLC51A, and VPS33B/VIPAS39 (ziccardi2026beyondthepump pages 3-4, ziccardi2026beyondthepump pages 4-5) | Use explicit gene/protein names in knowledge-base entries to avoid cross-source ambiguity (ziccardi2026beyondthepump pages 3-4, ziccardi2026beyondthepump pages 4-5) |


*Table: This table summarizes major classical and newer PFIC-associated genotypes, their core molecular defects, expected GGT patterns, hallmark phenotypes, and key prognostic or treatment-response notes. It is useful for rapid subtype comparison and highlights that nomenclature for newer numbered forms is not standardized across sources.*

### Genetic risk

Most severe PFIC is caused by **biallelic germline pathogenic variants** and follows autosomal-recessive inheritance. Missense, nonsense, frameshift, canonical splice, exon-level deletion, and larger intragenic deletion variants are documented. For example, a 2024 Pakistani PFIC2 cohort of 66 unrelated children identified 20 ABCB11 variants—11 missense, two frameshift, two nonsense, and five splice variants—illustrating marked allelic heterogeneity and enrichment in consanguineous populations. Variants absent or extremely rare in ancestry-matched controls and gnomAD, together with segregation, phenotype, protein staining, RNA-splicing, or transport assays, support ACMG/AMP classification; frequency must be recorded per exact HGVS allele rather than generalized by gene.

In ABCB11 disease, residual-function missense alleles are generally milder than biallelic protein-truncating variants. The NAPPED risk groups classify p.Asp482Gly/p.Glu297Gly as BSEP1, other missense genotypes as BSEP2, and biallelic truncating genotypes as BSEP3; median native-liver survival falls from **20.4 years in BSEP1 to 3.5 years in BSEP3**. (ziccardi2026beyondthepump pages 10-12)

Heterozygous **ABCB4, ABCB11, or ATP8B1** variants can predispose to intrahepatic cholestasis of pregnancy, contraceptive/drug-induced cholestasis, gallstones, or adult cryptogenic cholestasis, usually with incomplete penetrance. ABCB11 p.Val444Ala/1331T>C is a susceptibility allele rather than a fully penetrant PFIC cause. (henkel2019expandingetiologyof pages 10-11, mattiaccio2020molecularcharacterizationof pages 109-113, henkel2019expandingetiologyof pages 6-8)

### Environmental, lifestyle, infectious, and protective factors

No environmental exposure, lifestyle behavior, or infectious agent is a primary cause of Mendelian PFIC, and PFIC is not contagious or zoonotic. Hormones and drugs can reveal or worsen partial transporter deficiency: estradiol can interfere with FXR-mediated BSEP regulation, while selected medicines may provoke cholestasis in genetically susceptible carriers. Intercurrent illness, fasting, pregnancy, and hormonal contraception may similarly trigger episodic phenotypes. (mattiaccio2020molecularcharacterizationof pages 109-113, ziccardi2026beyondthepump pages 10-12, henkel2019expandingetiologyof pages 6-8)

No validated genetic “protective allele” prevents PFIC. Functionally protective factors are **residual protein expression/activity** and effective lowering of the circulating bile-acid pool. Post-diversion serum bile acids are strongly prognostic, but this is treatment response rather than primary genetic protection. Modifier genes, polygenic haplotypes, and environment likely explain intrafamilial variability, but none is ready for routine risk prediction. PFIC-specific epigenetic protective/risk signatures have not been validated. (mckiernan2024opinionpaperon pages 5-6, mattiaccio2020molecularcharacterizationof pages 109-113)

## 3. Phenotypes

| Phenotype | Type, timing, course, and frequency | Quality-of-life effect | Suggested HPO term |
|---|---|---|---|
| Intrahepatic cholestasis | Laboratory/clinical sign; usually neonatal or infantile in PFIC1/2/4/5, later and more variable in PFIC3; chronic or episodic | Drives all downstream morbidity | **HP:0001406** |
| Pruritus | Symptom; usually severe, progressive or fluctuating; hallmark of low-GGT PFIC | Sleep loss, irritability, skin mutilation, poor attention and school performance | **HP:0000989** |
| Jaundice/conjugated hyperbilirubinemia | Sign/laboratory abnormality; neonatal to childhood, variable | Stigma and marker of active disease | **HP:0000952**, **HP:0002904** |
| Elevated serum bile acids | Laboratory abnormality; common and often marked | Correlates with itch and native-liver prognosis | **HP:0012202** |
| Low/normal GGT despite cholestasis | Laboratory discriminator in PFIC1/2/4/5 and several newer forms | Diagnostic rather than directly symptomatic | **HP:0031964** (abnormal GGT; annotate direction locally) |
| Elevated GGT | Typical of ABCB4/PFIC3 and selected newer forms | Helps subtype disease | **HP:0031964** |
| Hepatomegaly/splenomegaly | Physical sign; develops with chronic disease/portal hypertension | Abdominal discomfort and activity limitation | **HP:0002240**, **HP:0001744** |
| Failure to thrive/short stature | Physical manifestation; frequent in severe pediatric disease from malabsorption and chronic illness | Major developmental and family burden | **HP:0001508**, **HP:0004322** |
| Fat-soluble-vitamin deficiency | Laboratory/clinical; chronic cholestasis | Bleeding, rickets, visual or neurologic complications | **HP:0001882**, **HP:0002748** as applicable |
| Diarrhea | Symptom; particularly ATP8B1 and MYO5B disease; may worsen after PFIC1 transplant | Nutrition, continence, school/social burden | **HP:0002014** |
| Portal hypertension/cirrhosis | Progressive sign/pathology | Variceal bleeding, ascites, transplant need | **HP:0001409**, **HP:0001394** |
| Sensorineural hearing impairment | Extrahepatic sign in ATP8B1 deficiency; not universal | Communication/development | **HP:0000407** |
| Pancreatic insufficiency | Extrahepatic sign in ATP8B1 deficiency | Malabsorption and growth failure | **HP:0001738** |
| HCC | Complication, particularly severe ABCB11 and TJP2 disease; can occur in childhood | Life-threatening; mandates surveillance | **HP:0006744** |

Published studies seldom provide robust phenotype percentages by genotype. A systematic review found only two usable health-related-quality-of-life studies and substantial heterogeneity. Its abstract states that pruritus “**may affect many activities of daily living through loss of sleep, irritability, poor attention, and impaired school performance**.” (Human systematic review, published June 2021; DOI: [10.1186/s13023-021-01884-4](https://doi.org/10.1186/s13023-021-01884-4)). (joneshughes2021epidemiologyandburden pages 11-12)

## 4. Genetic and molecular information

### Variant interpretation

- **Origin:** constitutional/germline. Somatic variants are not an established cause of PFIC, although somatic oncogenic changes may occur secondarily in HCC.
- **Pathogenic mechanism:** predominantly loss of function, impaired folding/processing, reduced transport, defective membrane targeting, or loss of transcriptional regulation. Dominant-negative mechanisms are not the usual basis of classical severe PFIC.
- **Classification:** use ACMG/AMP criteria with ClinVar review status, segregation, ancestry-specific population frequency, immunohistochemistry, RNA assays, and functional transport/localization evidence. A VUS alone should not establish PFIC. Reanalysis is appropriate as gene–disease validity and variant databases evolve. (ziccardi2026beyondthepump pages 9-10, ziccardi2026beyondthepump pages 10-12)
- **Chromosomal abnormalities:** PFIC is not ordinarily an aneuploidy/translocation syndrome. Exon or intragenic copy-number variants can occur—for example a reported 31.7-kb NR1H4 deletion—and therefore panel/WES pipelines should include CNV calling. (vinayagamoorthy2021newervariantsof pages 2-4)
- **Epigenetics:** no reproducible PFIC-specific DNA-methylation, histone, or chromatin biomarker has entered clinical use.

## 5. Environmental information

Toxins, radiation, pollution, smoking, alcohol, occupation, diet, and infection are not established initiating causes. Drugs and sex hormones can act as **phenotypic stressors** in people with partial transporter function; potentially cholestatic medicines should therefore be reviewed carefully. Adequate energy intake, medium-chain triglycerides, and replacement of vitamins A, D, E, and K mitigate consequences but do not prevent the genotype. (vinayagamoorthy2021newervariantsof pages 10-11, mattiaccio2020molecularcharacterizationof pages 109-113, henkel2019expandingetiologyof pages 6-8)

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream germline defect.** A canalicular transporter, phospholipid flippase/floppase, tight-junction component, nuclear bile-acid receptor, or trafficking motor is absent or dysfunctional.
2. **Canalicular failure.** Bile salts cannot exit through BSEP; phosphatidylcholine cannot protect membranes in MDR3 deficiency; canalicular lipid asymmetry becomes unstable in FIC1 deficiency; bile leaks paracellularly in TJP2 deficiency; or BSEP/MDR3 fail to reach the apical membrane in MYO5B disease. FXR deficiency reduces BSEP transcription and physiological suppression of bile-acid synthesis. (henkel2019expandingetiologyof pages 6-8, vinayagamoorthy2021newervariantsof pages 2-4, ziccardi2026beyondthepump pages 3-4, henkel2019expandingetiologyof pages 2-4)
3. **Bile-acid retention and altered bile composition.** Toxic, detergent-like bile acids accumulate in hepatocytes and blood; in ABCB4 deficiency, poorly phospholipid-buffered bile also damages cholangiocytes.
4. **Cellular injury.** Bile acids disrupt mitochondria, increase oxidative stress and permeability transition, and promote hepatocyte apoptosis/necrosis and inflammatory signaling. (ziccardi2026beyondthepump pages 1-3)
5. **Tissue response.** Hepatocyte injury, ductular reaction, stellate-cell activation and extracellular-matrix deposition generate fibrosis, cirrhosis, portal hypertension and regenerative pressure that contributes to HCC.
6. **Clinical output.** Systemic bile acids produce pruritus; reduced intestinal bile causes fat/vitamin malabsorption and growth failure; advanced fibrosis causes synthetic failure and portal-hypertensive complications.

**Cell Ontology suggestions:** hepatocyte **CL:0000182**; cholangiocyte **CL:0002538**; hepatic stellate cell **CL:0000632**; liver-resident macrophage/Kupffer cell **CL:0000091**; ileal enterocyte **CL:0000584**. **GO biological-process suggestions:** bile-acid transport **GO:0015721**; bile-acid biosynthetic process **GO:0006699**; phospholipid translocation **GO:0045332**; epithelial-cell polarity **GO:0090162**; tight-junction assembly **GO:0120192**; response to oxidative stress **GO:0006979**; apoptotic process **GO:0006915**; extracellular-matrix organization **GO:0030198**. **GO cellular components:** bile canaliculus **GO:0044294**; apical plasma membrane **GO:0016324**; tight junction **GO:0070160**; recycling endosome **GO:0055037**; mitochondrion **GO:0005739**; nucleus **GO:0005634**.

### Molecular profiling and advanced technologies

Serum bile-acid concentration is the best-established molecular biomarker. Routine PFIC-specific transcriptomic, proteomic, lipidomic, single-cell, spatial-transcriptomic, or clinical multi-omic classifiers are **not yet validated**. Patient-derived hepatocyte organoids and iPSC systems are promising for testing trafficking defects and personalized rescue, but current organoid reviews emphasize incomplete maturation, absence of whole-organ enterohepatic physiology, and matrix/standardization limitations. The 2024 organoid review describes these systems as enabling “**better model liver disease, improve (personalized) drug testing, and advance bioengineering options**” (DOI: [10.1097/HEP.0000000000000343](https://doi.org/10.1097/HEP.0000000000000343)).

## 7. Anatomical structures affected

- **Primary organ:** liver **UBERON:0002107**, especially hepatic lobule **UBERON:0004647** and bile canaliculi. The principal cells are hepatocytes; cholangiocytes are particularly injured in ABCB4 deficiency.
- **Secondary sites:** ileum **UBERON:0002116** (enterohepatic recycling and IBAT target); small-intestinal epithelium in MYO5B disease; pancreas and inner ear in ATP8B1 deficiency; spleen through portal hypertension; bone through vitamin-D deficiency.
- **Systems:** digestive/hepatobiliary primarily, with nutritional, skeletal, hematologic and occasional auditory/neurologic effects.
- **Subcellular sites:** apical/canalicular membrane, tight junction, recycling endosome, nucleus/FXR transcriptional machinery, and mitochondria.
- **Lateralization:** not applicable; liver disease is diffuse rather than unilateral.

## 8. Temporal development

PFIC1/2/4/5 commonly begins in the neonatal period or first year, while PFIC3 may begin later in childhood, adolescence, or adulthood. The untreated course is chronic and usually progressive, although residual-function alleles may produce episodic BRIC or stable adult disease. Early disease consists of biochemical cholestasis, jaundice and itch; intermediate disease adds growth failure, hepatosplenomegaly and fibrosis; advanced disease includes portal hypertension and synthetic dysfunction; end-stage disease requires transplantation. (henkel2019expandingetiologyof pages 6-8, henkel2019expandingetiologyof pages 2-4, ziccardi2026beyondthepump pages 1-3)

Critical intervention windows are before irreversible fibrosis, severe growth compromise, or malignancy. Treatment-induced biochemical remission can occur after effective IBAT inhibition or biliary diversion; spontaneous durable remission is atypical in severe PFIC. Genotype and post-treatment bile-acid reduction should guide whether to continue medical therapy, perform diversion, or proceed to transplant. (mckiernan2024opinionpaperon pages 5-6, joneshughes2021epidemiologyandburden pages 11-12)

## 9. Inheritance and population

- **Incidence:** approximately **1:50,000–100,000 births**; reliable population prevalence and annual incidence are unavailable. (mckiernan2024opinionpaperon pages 1-3)
- **Hospital-based proportion:** three studies reported PFIC in **9–12%** of selected children admitted with cholestasis, acute liver failure, or splenomegaly; this is not population prevalence. The systematic review included 22 studies and **2,603 patients**. (joneshughes2021epidemiologyandburden pages 11-12)
- **Inheritance:** predominantly autosomal recessive; recurrence risk is 25% per pregnancy when both parents carry pathogenic variants in the same gene.
- **Penetrance/expressivity:** severe biallelic loss is often highly penetrant, but expression is allele- and gene-dependent. Heterozygous susceptibility phenotypes have incomplete penetrance. No genetic anticipation is known.
- **Consanguinity/founder effects:** consanguinity increases homozygosity and disease frequency; population-specific founder variants occur, but no single global founder allele exists. (henkel2019expandingetiologyof pages 6-8)
- **Germline mosaicism:** biologically possible but not a characteristic documented mechanism; standard counseling should mention a small residual recurrence risk after apparently de novo findings.
- **Carrier frequency:** not reliably established across ancestries because of extreme allelic heterogeneity.
- **Demographics:** all sexes are affected approximately equally; geographic clustering reflects ancestry, founder effects, testing access, and consanguinity rather than endemic exposure.

## 10. Diagnostics

### Recommended work-up

1. **Confirm cholestasis and severity:** fractionated bilirubin, serum bile acids, ALT, AST, ALP, GGT, albumin, glucose, PT/INR, CBC, fat-soluble vitamins, AFP, and renal/electrolyte tests. Low/normal GGT despite marked cholestasis strongly suggests ATP8B1, ABCB11, TJP2, NR1H4, MYO5B and selected newer forms; high GGT favors ABCB4 and structural/ductal disease. (ziccardi2026beyondthepump pages 9-10, ziccardi2026beyondthepump pages 7-9, henkel2019expandingetiologyof pages 2-4)
2. **Exclude urgent obstruction:** abdominal ultrasound with Doppler; in neonates, rapidly exclude biliary atresia and choledochal cyst. MRCP is selective, particularly with high GGT or ductal suspicion. (ziccardi2026beyondthepump pages 7-9, vinayagamoorthy2021newervariantsof pages 6-7)
3. **Genetic confirmation:** use a comprehensive cholestasis NGS panel with deletion/duplication analysis, followed by trio WES/WGS and periodic reanalysis if negative. Gene sequencing is the etiologic gold standard; reported targeted-panel diagnostic yield is **28.1–68%**, depending on selection and panel composition. (mckiernan2024opinionpaperon pages 3-4)
4. **Biopsy when needed:** stage fibrosis, resolve an inconclusive genetic result, or assess competing disease. Findings include bland canalicular/“Byler” bile and giant-cell change in PFIC1; paucity or reduced BSEP staining in ABCB11 disease; portal fibrosis/ductular proliferation and absent/reduced MDR3 in PFIC3; giant-cell transformation in TJP2/FXR disease. Immunostaining can support but not replace genetic interpretation. (henkel2019expandingetiologyof pages 6-8, henkel2019expandingetiologyof pages 2-4)
5. **Monitoring:** serial growth, itch/sleep scores, serum bile acids, liver synthetic function, ultrasound/elastography, and AFP/ultrasound HCC surveillance in high-risk ABCB11 and TJP2 disease.

### Differential diagnosis

Urgently exclude biliary atresia; also consider Alagille syndrome, alpha-1-antitrypsin deficiency, cystic fibrosis, neonatal sclerosing cholangitis, congenital infection, sepsis/TPN cholestasis, bile-acid synthesis defects, mitochondrial disease, galactosemia/tyrosinemia, ARC syndrome, citrin deficiency, endocrine disease, drug-induced injury and mechanical obstruction. Urinary bile-acid mass spectrometry is valuable when a primary bile-acid-synthesis defect is suspected. (vinayagamoorthy2021newervariantsof pages 10-11, ziccardi2026beyondthepump pages 7-9)

CMA, karyotype, FISH, mitochondrial DNA testing, and repeat-expansion assays are **not routine PFIC tests** unless syndromic findings suggest another diagnosis. RNA sequencing can resolve selected splice variants, but proteomics, metabolomics, epigenomics, and liquid biopsy remain investigational.

### Screening

PFIC is not included in routine population newborn screening. Test symptomatic infants promptly; offer cascade testing to relatives and targeted testing to siblings from birth. Carrier, prenatal, and preimplantation testing require prior identification of familial pathogenic variants.

## 11. Outcome and prognosis

Only about one-third of severe BSEP-deficient patients in historical cohorts reached adulthood with their native liver. BSEP native-liver survival varies sharply by genotype—median **20.4 years for BSEP1 versus 3.5 years for BSEP3**—and biallelic truncating disease has reported HCC risk up to **34% by age 15**. Less than half of historical PFIC1/2 cohorts retained native liver into adulthood. (marx2024practicalconsiderationsfor pages 1-2, joneshughes2021epidemiologyandburden pages 11-12, ziccardi2026beyondthepump pages 10-12)

Serum bile acids are both pharmacodynamic and prognostic. Values below **194 μmol/L** were associated with approximately threefold better 15-year native-liver survival; after diversion, a threshold near **102 μmol/L** identified particularly favorable BSEP outcomes. These are cohort associations, not universally validated individual cutoffs. (mckiernan2024opinionpaperon pages 5-6, joneshughes2021epidemiologyandburden pages 11-12)

Complications include malnutrition, rickets, bleeding, growth and developmental impairment, severe sleep disruption, portal hypertension, varices, ascites, liver failure, HCC and—in ABCB4 disease—possible cholangiocarcinoma. After transplant, PFIC2 can recur functionally through anti-BSEP antibodies; PFIC1 may develop persistent diarrhea and graft steatosis because extrahepatic ATP8B1 deficiency remains. (henkel2019expandingetiologyof pages 6-8, mckiernan2024opinionpaperon pages 3-4)

Standardized 5- and 10-year overall-survival estimates across all PFIC genotypes are unavailable. Prognosis is determined more meaningfully by genotype, residual protein function, fibrosis/portal hypertension, HCC, growth, and biochemical response to bile-acid-lowering therapy.

## 12. Treatment and current implementation

### Supportive and pharmacological care

- **Nutrition:** approximately **125–140%** of age-based recommended calories, protein **2–3 g/kg/day**, medium-chain triglycerides, and aggressive vitamins A/D/E/K replacement; monitor INR, vitamin levels, bone health and growth. (vinayagamoorthy2021newervariantsof pages 10-11)
- **UDCA** (CHEBI:9907) is often tried, especially in ABCB4 disease with residual MDR3 activity, but sustained benefit in severe PFIC1/2 is limited. Cholestyramine, rifampicin, naltrexone and sertraline are off-label antipruritic options with variable efficacy and safety burdens. (mckiernan2024opinionpaperon pages 4-5)
- **NCIt intervention suggestions:** Nutritional Support **C15469**; Drug Therapy **C15221**; Biliary Diversion Procedure (map to the nearest local NCIt surgical concept); Liver Transplantation **C15274**; Genetic Counseling **C15236**.

### IBAT inhibition: leading targeted therapy

Odevixibat inhibits ileal SLC10A2/IBAT, increases fecal bile-acid loss and lowers the returning hepatic bile-acid load. It was approved in the EU and US in **July 2021**—for PFIC treatment in the EU and PFIC-associated pruritus in the US, with exact age and label wording jurisdiction-dependent. (mckiernan2024opinionpaperon pages 4-5, marx2024practicalconsiderationsfor pages 2-3)

**PEDFIC-1, NCT03566238:** 62 patients aged 0.5–18 years with PFIC1/2 received 40 or 120 µg/kg/day or placebo for 24 weeks. Overall pruritus response was **55% versus 30%** with placebo (p=0.0038), and serum-bile-acid response was **33% versus 0%** (p=0.003). A secondary summary reported ≥70% bile-salt reduction in 71.4% and 28.6% of monitored patients in the two dose groups versus 0% placebo. (mckiernan2024opinionpaperon pages 4-5, komaniecka2024transporterproteinsas pages 24-26)

**PEDFIC-2, NCT03659916:** completed phase 3 open-label extension; **116 participants**, 40 or 120 µg/kg/day, planned 72 weeks. Evaluated patients maintained reductions in bile acids, ALT, AST and bilirubin with generally acceptable long-term tolerability. (komaniecka2024transporterproteinsas pages 24-26, NCT03659916 chunk 1)

**Real-world 2024 evidence:** in a German single-center series of nine patients (PFIC1 n=2; PFIC2 n=7), five improved in bile acids, itch, liver tests and sleep. Two siblings with complete BSEP loss did not respond and underwent transplantation; four reported transient abdominal symptoms or symptoms managed by dose reduction. The abstract concludes that “**clinical benefits were observed in most patients**,” while emphasizing monitoring in complete BSEP deficiency. Published December 2024; DOI: [10.3390/jcm13247508](https://doi.org/10.3390/jcm13247508). (marx2024practicalconsiderationsfor pages 1-2)

Maralixibat is another IBAT inhibitor. MARCH-PFIC (**NCT03905330**) was a multicenter randomized phase 3 study published in July 2024 (DOI: [10.1016/S2468-1253(24)00080-3](https://doi.org/10.1016/S2468-1253(24)00080-3)); its extension is **NCT04185363** with 84 participants. Genotype matters: biallelic ABCB11 truncating variants predict non-response because reducing enterohepatic return cannot restore absent canalicular export. (mckiernan2024opinionpaperon pages 5-6, mckiernan2024opinionpaperon pages 9-9)

Common class concerns are diarrhea, abdominal pain, altered bowel habits, and reduced absorption of fat-soluble vitamins. Monitor growth, vitamins, INR, liver tests, serum bile acids, itch and sleep. No established CPIC/PharmGKB pharmacogenomic dosing rule exists, but **disease genotype itself functions as a response biomarker**.

### Surgery and transplantation

Partial external/internal biliary diversion or ileal exclusion reduces enterohepatic recycling. Across 17 surgical series totaling **536 patients**, diversion reduced pruritus and bile acids, but response varied by genotype. A synthesis reported complete itch resolution in **59.5%**, while **27%** later required transplant; 10-year native-liver survival after diversion ranged **22–75%** by genotype. Stoma complications, diarrhea, malabsorption and recurrent itch occur. (mckiernan2024opinionpaperon pages 3-4, hupper2023surgicalversusmedical pages 10-12)

Liver transplantation is definitive for end-stage liver disease, unresectable HCC, severe portal hypertension, or refractory pruritus/growth failure. It corrects hepatocyte-specific transporter deficiency but not systemic ATP8B1 or intestinal MYO5B disease. Combined liver–intestinal transplantation may be required in severe MYO5B microvillus-inclusion disease. (henkel2019expandingetiologyof pages 6-8, mckiernan2024opinionpaperon pages 3-4)

### Practical treatment algorithm

1. Correct nutrition/vitamins and treat complications.
2. Obtain genotype while promptly treating severe itch.
3. Start a licensed IBAT inhibitor early when appropriate; one 2024 expert algorithm suggests odevixibat **40 µg/kg/day for 12 weeks**, then assess itch and serum-bile-acid response. (mckiernan2024opinionpaperon pages 5-6, mckiernan2024opinionpaperon pages 1-3)
4. Escalate dose/adjuncts according to label and response.
5. If inadequate response—especially complete BSEP loss—discuss diversion or transplant in a specialist multidisciplinary center.
6. Maintain HCC surveillance and monitor fibrosis irrespective of itch improvement.

### Experimental and ongoing research

Gene replacement, RNA therapy, CRISPR correction, and chemical chaperones for trafficking-defective missense variants remain preclinical. No approved PFIC gene, cell, or RNA therapy exists. Key research programs include NAPPED **NCT03930810** (planned 1,500 participants), TreatFIC **NCT06778174** (200), Indian PFIC Registry **NCT05704517** (200), and the odevixibat-versus-NAPPED external-control study **NCT07497724** (200). Some registry identifiers beginning NCT07 were initiated after 2024 and are included only as forward-looking developments, not as 2024 evidence. (NCT07497724 chunk 1, NCT07191704 chunk 1, NCT07497724 chunk 2)

## 13. Prevention

**Primary prevention:** no lifestyle or vaccine prevents a biallelic PFIC genotype. Genetic counseling, carrier testing in relatives or high-risk consanguineous families, preimplantation genetic testing, chorionic-villus/amniotic testing, and informed reproductive planning can prevent recurrence or enable early diagnosis.

**Secondary prevention:** rapid evaluation of neonatal cholestasis, cascade testing, presymptomatic sibling testing, early nutrition and early bile-acid-lowering therapy may prevent irreversible fibrosis and developmental harm.

**Tertiary prevention:** maintain vitamin and nutritional status; avoid unnecessary cholestatic medicines; vaccinate according to routine and chronic-liver-disease schedules, including hepatitis A/B where nonimmune; screen for varices, fibrosis and HCC; and refer before decompensation. Vaccination prevents superimposed infection, not PFIC itself.

## 14. Other species and natural disease

PFIC is not infectious and has no transmission or zoonotic potential. Orthologous bile-transport genes are evolutionarily conserved across vertebrates. Naturally occurring **ABCB4/MDR3-like** hepatobiliary disease has been described in veterinary species, but a standardized breed-specific PFIC counterpart was not established in the retrieved evidence; VBO annotation is therefore premature. Relevant taxonomy terms for experimental comparison are *Mus musculus* **NCBI Taxon 10090**, *Danio rerio* **7955**, and *Rattus norvegicus* **10116**.

## 15. Model organisms and experimental systems

- **Atp8b1-deficient mice:** model canalicular membrane instability and bile-acid susceptibility, but mouse bile-acid composition is more hydrophilic than humans and disease can be milder. (henkel2019expandingetiologyof pages 2-4)
- **Abcb11 knockout/edited mice:** reproduce impaired bile-salt export but often lack the severe human injury phenotype. A 2024 liver-specific CRISPR/AAV8 system simultaneously disrupted **Abcb11** and **Cyp2c70**, humanizing the bile-acid pool and producing higher transaminases and parenchymal necrosis. The abstract states that Abcb11 targeting alone caused “**hepatomegaly and cholestasis without histological evidence of liver injury**,” whereas bile-acid humanization better resembled human ABCB11 deficiency. Published March 2024; DOI: [10.1097/HC9.0000000000000382](https://doi.org/10.1097/HC9.0000000000000382).
- **Abcb4/Mdr2-null mice:** useful for phospholipid-deficient bile, cholangiocyte injury and fibrosis, although often used as a PSC-like model rather than a complete PFIC3 phenocopy.
- **Zebrafish:** transparent larvae enable bile-flow and canalicular-trafficking imaging; bsep and trafficking models are useful for rapid functional screens, but hepatic maturation and bile-acid physiology differ from humans.
- **Cellular systems:** polarized hepatocyte lines, primary hepatocytes, patient fibroblast/iPSC-derived hepatocyte-like cells and liver organoids permit localization, splicing, transport and rescue assays. They do not fully reproduce enterohepatic circulation, immune–stromal interaction, portal flow, or long-term carcinogenesis.

## Expert interpretation and evidence gaps

The strongest contemporary expert position is that PFIC management should be **gene-informed but response-driven**: sequence early, use serum bile acids and validated itch instruments serially, introduce licensed IBAT inhibition early, and avoid delaying diversion or transplantation in biochemical nonresponders or complete BSEP deficiency. The 2024 opinion paper recommends referral to experienced centers and concurrent genetic testing rather than waiting for molecular confirmation before addressing severe symptoms. (mckiernan2024opinionpaperon pages 5-6, mckiernan2024opinionpaperon pages 1-3)

Major gaps are: reliable population prevalence; phenotype frequencies for newer genes; ancestry-specific carrier frequencies; validated modifier/protective alleles; PFIC-specific epigenetic, single-cell and spatial maps; randomized comparisons of IBAT inhibition versus diversion; and proof that itch/serum-bile-acid improvement translates into long-term transplant-free and cancer-free survival. Ongoing registry and external-control studies are designed to address the last question. (joneshughes2021epidemiologyandburden pages 11-12, NCT07497724 chunk 1)

## Selected source index

- McKiernan P, et al. **Opinion paper on diagnosis and treatment of PFIC.** *JHEP Reports*. Published January 2024; DOI: [10.1016/j.jhepr.2023.100949](https://doi.org/10.1016/j.jhepr.2023.100949). (mckiernan2024opinionpaperon pages 3-4)
- Marx M, et al. **Real-world odevixibat case series.** *J Clin Med*. Published December 2024; DOI: [10.3390/jcm13247508](https://doi.org/10.3390/jcm13247508). (marx2024practicalconsiderationsfor pages 1-2)
- Hüpper MN, et al. **Surgical versus medical management.** *Children*. Published May 2023; DOI: [10.3390/children10060949](https://doi.org/10.3390/children10060949). (hupper2023surgicalversusmedical pages 10-12)
- Jones-Hughes T, et al. **Epidemiology and burden systematic review.** *Orphanet J Rare Dis*. Published June 2021; DOI: [10.1186/s13023-021-01884-4](https://doi.org/10.1186/s13023-021-01884-4). (joneshughes2021epidemiologyandburden pages 11-12)
- van Wessel DBE, et al. **BSEP genotype/natural history.** *J Hepatol*. Published July 2020; DOI: [10.1016/j.jhep.2020.02.007](https://doi.org/10.1016/j.jhep.2020.02.007).
- van Wessel DBE, et al. **FIC1 genotype, bile acids and diversion.** *Hepatology*. Published July 2021; DOI: [10.1002/hep.31787](https://doi.org/10.1002/hep.31787).
- Landmark gene-association PMIDs available in Open Targets include ATP8B1 **PMID:9500542**, ABCB11 **PMID:9806540**, TJP2 **PMID:24614073**, NR1H4 **PMID:26888176**, and MYO5B **PMID:27532546**. (OpenTargets Search: Progressive familial intrahepatic cholestasis)

References

1. (mckiernan2024opinionpaperon pages 1-3): Patrick McKiernan, Jesus Quintero Bernabeu, Muriel Girard, Giuseppe Indolfi, Eberhard Lurz, and Palak Trivedi. Opinion paper on the diagnosis and treatment of progressive familial intrahepatic cholestasis. Jan 2024. URL: https://doi.org/10.1016/j.jhepr.2023.100949, doi:10.1016/j.jhepr.2023.100949. This article has 36 citations and is from a peer-reviewed journal.

2. (henkel2019expandingetiologyof pages 6-8): Sarah AF Henkel, Judy H Squires, Mary Ayers, Armando Ganoza, Patrick Mckiernan, and James E Squires. Expanding etiology of progressive familial intrahepatic cholestasis. World Journal of Hepatology, 11:450-463, May 2019. URL: https://doi.org/10.4254/wjh.v11.i5.450, doi:10.4254/wjh.v11.i5.450. This article has 101 citations.

3. (mckiernan2024opinionpaperon pages 4-5): Patrick McKiernan, Jesus Quintero Bernabeu, Muriel Girard, Giuseppe Indolfi, Eberhard Lurz, and Palak Trivedi. Opinion paper on the diagnosis and treatment of progressive familial intrahepatic cholestasis. Jan 2024. URL: https://doi.org/10.1016/j.jhepr.2023.100949, doi:10.1016/j.jhepr.2023.100949. This article has 36 citations and is from a peer-reviewed journal.

4. (marx2024practicalconsiderationsfor pages 1-2): Milena Marx, Steffen Hartleif, Johannes Hilberath, Christoph P. Berg, Ilias Tsiflikas, Stephan Singer, and Ekkehard Sturm. Practical considerations for odevixibat treatment in patients with progressive familial intrahepatic cholestasis: a single-center case series. Journal of Clinical Medicine, 13:7508, Dec 2024. URL: https://doi.org/10.3390/jcm13247508, doi:10.3390/jcm13247508. This article has 8 citations.

5. (mckiernan2024opinionpaperon pages 5-6): Patrick McKiernan, Jesus Quintero Bernabeu, Muriel Girard, Giuseppe Indolfi, Eberhard Lurz, and Palak Trivedi. Opinion paper on the diagnosis and treatment of progressive familial intrahepatic cholestasis. Jan 2024. URL: https://doi.org/10.1016/j.jhepr.2023.100949, doi:10.1016/j.jhepr.2023.100949. This article has 36 citations and is from a peer-reviewed journal.

6. (komaniecka2024transporterproteinsas pages 24-26): Nina Komaniecka, Sonia Maroszek, Maria Drozdzik, Stefan Oswald, and Marek Drozdzik. Transporter proteins as therapeutic drug targets—with a focus on sglt2 inhibitors. International Journal of Molecular Sciences, 25:6926, Jun 2024. URL: https://doi.org/10.3390/ijms25136926, doi:10.3390/ijms25136926. This article has 16 citations.

7. (ziccardi2026beyondthepump pages 1-3): Ilaria Ziccardi, Michela Zorzi, and Adamo Pio d’Adamo. Beyond the pump: the evolving molecular landscape of intrahepatic cholestasis. Diagnostics, 16:726, Feb 2026. URL: https://doi.org/10.3390/diagnostics16050726, doi:10.3390/diagnostics16050726. This article has 1 citations.

8. (ziccardi2026beyondthepump pages 3-4): Ilaria Ziccardi, Michela Zorzi, and Adamo Pio d’Adamo. Beyond the pump: the evolving molecular landscape of intrahepatic cholestasis. Diagnostics, 16:726, Feb 2026. URL: https://doi.org/10.3390/diagnostics16050726, doi:10.3390/diagnostics16050726. This article has 1 citations.

9. (OpenTargets Search: Progressive familial intrahepatic cholestasis): Open Targets Query (Progressive familial intrahepatic cholestasis, 21 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

10. (henkel2019expandingetiologyof pages 2-4): Sarah AF Henkel, Judy H Squires, Mary Ayers, Armando Ganoza, Patrick Mckiernan, and James E Squires. Expanding etiology of progressive familial intrahepatic cholestasis. World Journal of Hepatology, 11:450-463, May 2019. URL: https://doi.org/10.4254/wjh.v11.i5.450, doi:10.4254/wjh.v11.i5.450. This article has 101 citations.

11. (mckiernan2024opinionpaperon pages 3-4): Patrick McKiernan, Jesus Quintero Bernabeu, Muriel Girard, Giuseppe Indolfi, Eberhard Lurz, and Palak Trivedi. Opinion paper on the diagnosis and treatment of progressive familial intrahepatic cholestasis. Jan 2024. URL: https://doi.org/10.1016/j.jhepr.2023.100949, doi:10.1016/j.jhepr.2023.100949. This article has 36 citations and is from a peer-reviewed journal.

12. (ziccardi2026beyondthepump pages 10-12): Ilaria Ziccardi, Michela Zorzi, and Adamo Pio d’Adamo. Beyond the pump: the evolving molecular landscape of intrahepatic cholestasis. Diagnostics, 16:726, Feb 2026. URL: https://doi.org/10.3390/diagnostics16050726, doi:10.3390/diagnostics16050726. This article has 1 citations.

13. (vinayagamoorthy2021newervariantsof pages 2-4): Vignesh Vinayagamoorthy, Anshu Srivastava, and Moinak Sen Sarma. Newer variants of progressive familial intrahepatic cholestasis. World Journal of Hepatology, 13:2024-2038, Dec 2021. URL: https://doi.org/10.4254/wjh.v13.i12.2024, doi:10.4254/wjh.v13.i12.2024. This article has 67 citations.

14. (vinayagamoorthy2021newervariantsof pages 10-11): Vignesh Vinayagamoorthy, Anshu Srivastava, and Moinak Sen Sarma. Newer variants of progressive familial intrahepatic cholestasis. World Journal of Hepatology, 13:2024-2038, Dec 2021. URL: https://doi.org/10.4254/wjh.v13.i12.2024, doi:10.4254/wjh.v13.i12.2024. This article has 67 citations.

15. (henkel2019expandingetiologyof pages 8-10): Sarah AF Henkel, Judy H Squires, Mary Ayers, Armando Ganoza, Patrick Mckiernan, and James E Squires. Expanding etiology of progressive familial intrahepatic cholestasis. World Journal of Hepatology, 11:450-463, May 2019. URL: https://doi.org/10.4254/wjh.v11.i5.450, doi:10.4254/wjh.v11.i5.450. This article has 101 citations.

16. (vinayagamoorthy2021newervariantsof pages 6-7): Vignesh Vinayagamoorthy, Anshu Srivastava, and Moinak Sen Sarma. Newer variants of progressive familial intrahepatic cholestasis. World Journal of Hepatology, 13:2024-2038, Dec 2021. URL: https://doi.org/10.4254/wjh.v13.i12.2024, doi:10.4254/wjh.v13.i12.2024. This article has 67 citations.

17. (ziccardi2026beyondthepump pages 4-5): Ilaria Ziccardi, Michela Zorzi, and Adamo Pio d’Adamo. Beyond the pump: the evolving molecular landscape of intrahepatic cholestasis. Diagnostics, 16:726, Feb 2026. URL: https://doi.org/10.3390/diagnostics16050726, doi:10.3390/diagnostics16050726. This article has 1 citations.

18. (henkel2019expandingetiologyof pages 10-11): Sarah AF Henkel, Judy H Squires, Mary Ayers, Armando Ganoza, Patrick Mckiernan, and James E Squires. Expanding etiology of progressive familial intrahepatic cholestasis. World Journal of Hepatology, 11:450-463, May 2019. URL: https://doi.org/10.4254/wjh.v11.i5.450, doi:10.4254/wjh.v11.i5.450. This article has 101 citations.

19. (mattiaccio2020molecularcharacterizationof pages 109-113): Alessandro Mattiaccio. Molecular characterization of gene defects associated with progressive familial intrahepatic cholestasis by next generation sequencing. ArXiv, Apr 2020. URL: https://doi.org/10.6092/unibo/amsdottorato/9386, doi:10.6092/unibo/amsdottorato/9386. This article has 0 citations.

20. (joneshughes2021epidemiologyandburden pages 11-12): Tracey Jones-Hughes, Jo Campbell, and Louise Crathorne. Epidemiology and burden of progressive familial intrahepatic cholestasis: a systematic review. Orphanet Journal of Rare Diseases, Jun 2021. URL: https://doi.org/10.1186/s13023-021-01884-4, doi:10.1186/s13023-021-01884-4. This article has 48 citations and is from a peer-reviewed journal.

21. (ziccardi2026beyondthepump pages 9-10): Ilaria Ziccardi, Michela Zorzi, and Adamo Pio d’Adamo. Beyond the pump: the evolving molecular landscape of intrahepatic cholestasis. Diagnostics, 16:726, Feb 2026. URL: https://doi.org/10.3390/diagnostics16050726, doi:10.3390/diagnostics16050726. This article has 1 citations.

22. (ziccardi2026beyondthepump pages 7-9): Ilaria Ziccardi, Michela Zorzi, and Adamo Pio d’Adamo. Beyond the pump: the evolving molecular landscape of intrahepatic cholestasis. Diagnostics, 16:726, Feb 2026. URL: https://doi.org/10.3390/diagnostics16050726, doi:10.3390/diagnostics16050726. This article has 1 citations.

23. (marx2024practicalconsiderationsfor pages 2-3): Milena Marx, Steffen Hartleif, Johannes Hilberath, Christoph P. Berg, Ilias Tsiflikas, Stephan Singer, and Ekkehard Sturm. Practical considerations for odevixibat treatment in patients with progressive familial intrahepatic cholestasis: a single-center case series. Journal of Clinical Medicine, 13:7508, Dec 2024. URL: https://doi.org/10.3390/jcm13247508, doi:10.3390/jcm13247508. This article has 8 citations.

24. (NCT03659916 chunk 1):  Long Term Safety & Efficacy Study Evaluating The Effect of A4250 in Children With PFIC. Albireo, an Ipsen Company. 2018. ClinicalTrials.gov Identifier: NCT03659916

25. (mckiernan2024opinionpaperon pages 9-9): Patrick McKiernan, Jesus Quintero Bernabeu, Muriel Girard, Giuseppe Indolfi, Eberhard Lurz, and Palak Trivedi. Opinion paper on the diagnosis and treatment of progressive familial intrahepatic cholestasis. Jan 2024. URL: https://doi.org/10.1016/j.jhepr.2023.100949, doi:10.1016/j.jhepr.2023.100949. This article has 36 citations and is from a peer-reviewed journal.

26. (hupper2023surgicalversusmedical pages 10-12): Maria Noelle Hüpper, Judith Pichler, Wolf-Dietrich Huber, Andreas Heilos, Rebecca Schaup, Martin Metzelder, and Sophie Langer. Surgical versus medical management of progressive familial intrahepatic cholestasis—case compilation and review of the literature. Children, 10:949, May 2023. URL: https://doi.org/10.3390/children10060949, doi:10.3390/children10060949. This article has 9 citations.

27. (NCT07497724 chunk 1):  Odevixibat Outcomes in Patients With PFIC Versus an External Control Cohort (OvEC-PFIC). Ipsen. 2026. ClinicalTrials.gov Identifier: NCT07497724

28. (NCT07191704 chunk 1):  A Study to Assess the Genetic Variations in Bile Flow Disorders: Linking Progressive Familial Intrahepatic Cholestasis (PFIC)-Related Genes to Symptoms in Adults With Recurrent Cholestasis in Spain. Ipsen. 2025. ClinicalTrials.gov Identifier: NCT07191704

29. (NCT07497724 chunk 2):  Odevixibat Outcomes in Patients With PFIC Versus an External Control Cohort (OvEC-PFIC). Ipsen. 2026. ClinicalTrials.gov Identifier: NCT07497724

## Artifacts

- [Edison artifact artifact-00](Progressive_Familial_Intrahepatic_Cholestasis-deep-research-falcon_artifacts/artifact-00.md)