---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-31T18:06:58.888430'
end_time: '2026-07-31T18:15:05.206435'
duration_seconds: 486.32
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Otofacial Neurodevelopmental Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Otofacial_Neurodevelopmental_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Otofacial Neurodevelopmental Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Otofacial Neurodevelopmental Syndrome** covering all of the
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
- **Disease Name:** Otofacial Neurodevelopmental Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Otofacial Neurodevelopmental Syndrome** covering all of the
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


# Otofacial Neurodevelopmental Syndrome: Disease-Characteristics Report

## Executive summary and evidence limits

Otofacial neurodevelopmental syndrome is an ultra-rare, newly delineated autosomal-recessive developmental disorder caused by biallelic loss-of-function variants in **ZSCAN10**. The disease-defining publication reported only **seven affected individuals**, so essentially all frequency estimates remain provisional. Its most reproducible features are global developmental delay, facial asymmetry, external-ear malformations, semicircular-canal dysplasia, and sensorineural hearing loss (SNHL), confirmed in **4/5 individuals tested**. The current MONDO identifier is **MONDO:0975705**. Open Targets lists ZSCAN10 as the sole associated target and links the association to PMID **38386308**. (OpenTargets Search: Otofacial neurodevelopmental syndrome, owrang2025neurogeneticdisorderswith pages 13-14)

The foundational primary report is Laugwitz L, Cheng F, Collins SC, et al., **“ZSCAN10 deficiency causes a neurodevelopmental disorder with characteristic oto-facial malformations,”** *Brain*. 2024;147(7):2471–2482, PMID: **38386308**; PubMed: https://pubmed.ncbi.nlm.nih.gov/38386308/. A subsequent authoritative review is Owrang D, Vona B, **“Neurogenetic Disorders with Hearing Loss: Mechanisms, Classifications, and Emerging Insights,”** published November 2025, DOI: https://doi.org/10.1007/s11910-025-01466-y. (owrang2025neurogeneticdisorderswith pages 13-14, owrang2025neurogeneticdisorderswith pages 18-19)

| Domain | Established finding | Quantitative evidence | Suggested ontology/identifier | Evidence status/limitations |
|---|---|---:|---|---|
| Disease entity | Otofacial neurodevelopmental syndrome is a recently defined Mendelian disorder linked to ZSCAN10 deficiency | 1 disease-target association in Open Targets (score 0.607) | MONDO:0975705 | Disease appears newly described; cross-resource coverage is still sparse (OpenTargets Search: Otofacial neurodevelopmental syndrome) |
| Causal gene | The only currently associated gene identified in retrieved disease-level resources is **ZSCAN10** | 1 associated target; 5-7 evidence records depending on source view | ZSCAN10; ENSG00000130182 | Evidence in retrieved materials converges on a single gene, but detailed variant list was not recoverable from available contexts (OpenTargets Search: Otofacial neurodevelopmental syndrome) |
| Foundational report | Primary disease-defining report is **Laugwitz et al., Brain (2024)** | 7 affected individuals reported | PMID:38386308; Brain 2024; DOI/publication details cited in review | Full primary-text patient table/variant appendix not available in retrieved contexts (owrang2025neurogeneticdisorderswith pages 18-19) |
| Inheritance | Reported as **biallelic loss-of-function** disorder with **autosomal recessive** inheritance | 7 affected individuals from the foundational cohort | Autosomal recessive; germline inherited disorder | Open Targets also notes one entry as “biallelic, autosomal or pseudoautosomal”; autosomal recessive is the clearer formulation from review-based clinical summary (owrang2025neurogeneticdisorderswith pages 13-14, OpenTargets Search: Otofacial neurodevelopmental syndrome) |
| Variant class | Pathogenic alleles are described as **loss-of-function**, including **frameshift** and **stop-gained/nonsense** classes | High-confidence variant evidence scores ~0.90-0.92 in Open Targets/EVA-backed entries | Loss-of-function variant class | Exact HGVS nomenclature and allele frequencies were not available in retrieved contexts (OpenTargets Search: Otofacial neurodevelopmental syndrome) |
| Core neurodevelopmental phenotype | **Global developmental delay** is a consistent clinical feature | Described as present consistently across the 7 affected individuals | Suggested HPO term: global developmental delay | No fine-grained severity percentages or developmental testing metrics available from retrieved contexts (owrang2025neurogeneticdisorderswith pages 13-14) |
| Craniofacial phenotype | **Facial asymmetry** is part of the characteristic phenotype | Reported consistently in the 7 affected individuals | Suggested HPO term: facial asymmetry | Frequency reported qualitatively as consistent; no standardized dysmorphology breakdown available here (owrang2025neurogeneticdisorderswith pages 13-14) |
| External ear phenotype | **Outer-ear malformations** are characteristic | Reported consistently in the 7 affected individuals | Suggested HPO term: external ear malformation / abnormality of the external ear | Specific malformation subtypes were not available in retrieved contexts (owrang2025neurogeneticdisorderswith pages 13-14) |
| Inner ear anatomy | **Semicircular-canal dysplasia** documented on cerebral MRI/inner-ear imaging | Present in imaged affected individuals per review summary; exact denominator not stated | Suggested HPO term: semicircular canal dysplasia; UBERON: semicircular canal | Anatomical description is available, but full radiology details and laterality were not recoverable (owrang2025neurogeneticdisorderswith pages 13-14) |
| Hearing phenotype | **Sensorineural hearing loss (SNHL)** is a major associated feature | **4/5 tested** individuals had confirmed SNHL | Suggested HPO term: sensorineural hearing impairment | Denominator indicates incomplete testing; true frequency among all affected individuals remains uncertain (owrang2025neurogeneticdisorderswith pages 13-14) |
| Anatomical systems affected | Disorder involves nervous system, craniofacial structures, outer ear, and inner ear/vestibular apparatus | At least 4 organ-system domains implicated by reported phenotype set | Suggested UBERON labels: brain, external ear, inner ear, semicircular canal | Direct cellular pathology for each tissue has not yet been defined in retrieved sources (owrang2025neurogeneticdisorderswith pages 13-14) |
| Molecular function | ZSCAN10 is a **zinc finger and SCAN domain-containing transcription factor** implicated in control of **embryonic stem-cell pluripotency** | Qualitative functional role, no disease-specific effect size reported | ZSCAN10; transcription factor; pluripotency-related regulator | Disease mechanism beyond this high-level role remains incompletely resolved in available contexts (owrang2025neurogeneticdisorderswith pages 13-14) |
| Mechanism / pathophysiology | Current understanding supports an upstream defect in transcriptional regulation during development, plausibly affecting neurodevelopment and otic/craniofacial morphogenesis | Evidence is descriptive rather than pathway-quantified | Suggested GO labels: regulation of transcription, stem cell maintenance, developmental process | Review explicitly notes that precise downstream targets remain unknown; no validated disease pathway map retrieved (owrang2025neurogeneticdisorderswith pages 13-14) |
| Age at onset / course | Findings are most compatible with **congenital or early-childhood onset neurodevelopmental disorder** | No exact onset ages available in retrieved contexts | Suggested onset label: congenital/infancy/childhood onset | Formal natural-history data, progression rate, and lifespan data unavailable (owrang2025neurogeneticdisorderswith pages 13-14, owrang2025neurogeneticdisorderswith pages 18-19) |
| Epidemiology | Prevalence and incidence are **unknown** | Only **7 affected individuals** identified in available foundational report | Ultra-rare Mendelian disorder | No population-based studies, registries, or prevalence estimates identified in retrieved contexts (owrang2025neurogeneticdisorderswith pages 18-19, OpenTargets Search: Otofacial neurodevelopmental syndrome) |
| Population genetics | No founder effect, carrier frequency, penetrance estimate, or ancestry-specific enrichment established from available contexts | Not reported | Not established | These fields remain evidence gaps pending larger cohorts and database curation (owrang2025neurogeneticdisorderswith pages 18-19, OpenTargets Search: Otofacial neurodevelopmental syndrome) |
| Diagnostics | Most evidence-supported diagnosis is **genomic testing** identifying biallelic ZSCAN10 loss-of-function variants, with phenotypic support from hearing assessment and imaging of inner-ear anomalies | 7 molecularly defined individuals; hearing loss confirmed in 4/5 tested | Molecular diagnosis; ZSCAN10 sequencing; consider exome/genome in neurodevelopmental + hearing-loss workup | No formal disease-specific diagnostic criteria or validated biomarker studies retrieved (owrang2025neurogeneticdisorderswith pages 13-14, OpenTargets Search: Otofacial neurodevelopmental syndrome) |
| Clinical implementation | Broader expert opinion in neurogenetic hearing loss recommends considering neurogenetic diagnosis when hearing loss co-occurs with developmental delay, hypotonia, or regression | Qualitative recommendation | Neurogenetic hearing-loss diagnostic framework | This is expert contextual guidance, not disease-specific management consensus for ZSCAN10 syndrome (owrang2025neurogeneticdisorderswith pages 13-14) |
| Treatment | **No disease-specific therapy established** in retrieved sources | 0 disease-specific treatments identified | Supportive care only (conceptual) | No pharmacotherapy, gene therapy, trial, or interventional outcome data retrieved (OpenTargets Search: Otofacial neurodevelopmental syndrome) |
| Prognosis | **Unknown** from current retrieved evidence | No survival or long-term outcome series identified | Not established | Natural history, mortality, functional outcomes, and quality-of-life metrics are not yet defined (owrang2025neurogeneticdisorderswith pages 18-19, OpenTargets Search: Otofacial neurodevelopmental syndrome) |
| Environmental / lifestyle factors | No disease-specific environmental, lifestyle, infectious, or gene-environment risk factors established | 0 identified | Not applicable/unknown | Consistent with a rare Mendelian disorder; absence of evidence should not be overinterpreted as evidence of absence (OpenTargets Search: Otofacial neurodevelopmental syndrome) |
| Protective factors | No genetic or environmental protective factors identified | 0 identified | Not established | No modifier/protective data available in retrieved contexts (OpenTargets Search: Otofacial neurodevelopmental syndrome) |
| Omics / epigenetics | No disease-specific transcriptomic, proteomic, metabolomic, lipidomic, or epigenomic datasets were retrieved | 0 disease-specific omics studies identified in available contexts | Not established | Mechanistic inference is based mainly on known gene function, not disease-specific multi-omics evidence (owrang2025neurogeneticdisorderswith pages 13-14, OpenTargets Search: Otofacial neurodevelopmental syndrome) |
| Model organisms / natural disease | No disease-specific animal model or naturally occurring non-human disease evidence was retrieved | 0 disease-specific models identified | Not established | Although ZSCAN10 has broader stem-cell biology literature, no syndrome-specific model evidence was available in retrieved contexts (owrang2025neurogeneticdisorderswith pages 13-14, OpenTargets Search: Otofacial neurodevelopmental syndrome) |


*Table: This table provides an evidence-bound summary of what is currently established versus unknown for otofacial neurodevelopmental syndrome, centered on the 2024 ZSCAN10 cohort report and supporting disease-resource evidence. It is useful for rapid knowledge-base population while clearly separating confirmed findings from gaps.*

## 1. Disease information

### Definition

This is a congenital/early-childhood syndromic neurodevelopmental disorder combining impaired neurodevelopment with characteristic craniofacial, external-ear, inner-ear, and auditory abnormalities. “ZSCAN10 deficiency” is the mechanistically preferable name because the demonstrated cause is biallelic ZSCAN10 loss of function. (owrang2025neurogeneticdisorderswith pages 13-14)

### Identifiers and names

- **MONDO:** MONDO:0975705.
- **Causal gene:** **ZSCAN10**, zinc finger and SCAN domain containing 10.
- **Ensembl gene:** ENSG00000130182.
- **Primary-literature PMID:** 38386308.
- **Useful synonyms:** ZSCAN10-related otofacial neurodevelopmental syndrome; ZSCAN10 deficiency; neurodevelopmental disorder with characteristic oto-facial malformations.
- **OMIM, Orphanet, MeSH, ICD-10, and ICD-11:** no disease-specific identifiers were established in the retrieved evidence. Broad codes such as developmental disorder, congenital ear malformation, or hearing loss would be nonspecific and should not be represented as exact disease mappings. (OpenTargets Search: Otofacial neurodevelopmental syndrome, owrang2025neurogeneticdisorderswith pages 18-19)

The evidence is **aggregated disease-level evidence derived from individually phenotyped patients**, not EHR-derived population surveillance. The primary cohort comprised seven molecularly diagnosed individuals; Open Targets subsequently aggregated genetic evidence from EVA, UniProt literature, and Genomics England. (OpenTargets Search: Otofacial neurodevelopmental syndrome)

## 2. Etiology

### Causal and genetic factors

The established cause is **germline biallelic loss of function in ZSCAN10**, consistent with autosomal-recessive inheritance. Retrieved disease-resource evidence includes frameshift and stop-gained alleles, with Open Targets/EVA confidence scores of approximately 0.90–0.92. Exact HGVS descriptions were not recoverable from the available primary-text extract and should therefore be imported directly from PMID 38386308, ClinVar, or EVA rather than inferred. (owrang2025neurogeneticdisorderswith pages 13-14, OpenTargets Search: Otofacial neurodevelopmental syndrome)

Family history, parental consanguinity, and carrier status may increase recurrence risk in the usual autosomal-recessive manner, but no founder allele, carrier frequency, modifier gene, susceptibility locus, or ancestry-specific enrichment has been established.

### Environmental, infectious, and lifestyle factors

No toxins, medications, radiation, infection, maternal exposure, diet, smoking, alcohol, occupation, or other environmental cause has been linked specifically to this syndrome. No gene–environment interaction has been demonstrated. This is a monogenic developmental disorder; environmental contributors should not be asserted without new evidence.

### Protective factors

No protective ZSCAN10 alleles, modifier variants, dietary factors, lifestyle exposures, or pharmacologic prophylaxis are known. Population loss-of-function constraint and allele frequencies require direct gnomAD review at variant level.

## 3. Phenotypes

The small denominator makes “consistent” more appropriate than a population-level percentage except where a tested denominator was reported.

| Phenotype | Type and characteristics | Observed frequency | Suggested HPO term |
|---|---|---:|---|
| Global developmental delay | Neurodevelopmental sign; early-childhood recognition; severity and developmental domains not fully quantified | Described consistently among 7 cases | Global developmental delay |
| Facial asymmetry | Congenital physical manifestation/dysmorphology; likely stable | Described consistently among 7 cases | Facial asymmetry |
| External-ear malformation | Congenital structural sign; subtype and laterality unavailable | Described consistently among 7 cases | Abnormality of the external ear / external-ear malformation |
| Semicircular-canal dysplasia | Inner-ear imaging abnormality; congenital structural defect | Denominator not specified in retrieved extract | Abnormal semicircular canal morphology / semicircular-canal dysplasia |
| Sensorineural hearing loss | Auditory functional impairment; onset and severity incompletely reported | **4/5 tested (80%)** | Sensorineural hearing impairment |

These findings are directly summarized in the review as: **“Biallelic ZSCAN10 loss-of-function variants were identified in seven affected individuals who consistently reported global developmental delay, facial asymmetry and malformations of the outer ear.”** It further states that imaging showed semicircular-canal dysplasia and that **“4/5 individuals were confirmed with SNHL.”** (owrang2025neurogeneticdisorderswith pages 13-14)

No robust data are available for seizures, behavior, cognition level, speech, motor milestones, hypotonia, vestibular symptoms, growth, ophthalmology, laboratory abnormalities, or other organ involvement. Their absence from this report must not be interpreted as clinical absence.

### Quality-of-life implications

No EQ-5D, SF-36, PROMIS, or syndrome-specific quality-of-life study exists in the retrieved evidence. Nevertheless, developmental delay can impair education and independent daily functioning, while SNHL can compound speech-language and social-communication disability. That functional interpretation is clinically reasonable but has not been quantified in this syndrome.

## 4. Genetic and molecular information

**ZSCAN10** encodes a zinc-finger and SCAN-domain transcription factor. The current evidence supports biallelic germline truncating variants—frameshift and nonsense/stop-gained—as the pathogenic class. The expected consequence is loss of functional protein, rather than gain of function or dominant-negative action. Somatic causation is not implicated. (OpenTargets Search: Otofacial neurodevelopmental syndrome, owrang2025neurogeneticdisorderswith pages 13-14)

Suggested annotations include:

- **Gene/protein:** ZSCAN10; ENSG00000130182.
- **Variant concepts:** sequence variant; frameshift variant; stop-gained variant; loss-of-function variant; germline variant.
- **Inheritance:** autosomal recessive.
- **Molecular-function GO labels:** DNA-binding transcription-factor activity; sequence-specific DNA binding.
- **Cellular-component GO label:** nucleus.
- **Biological-process GO labels:** regulation of transcription by RNA polymerase II; stem-cell population maintenance; regulation of cell differentiation; embryonic development.

The retrieved evidence did not establish HGNC ID, UniProt accession, exact transcript, exact HGVS variants, gnomAD frequencies, ACMG criteria applied to each variant, penetrance, or pathogenicity of individual ClinVar records. Likewise, no modifier genes, syndrome-specific methylation signature, chromosomal rearrangement, copy-number mechanism, or repeat expansion is established.

## 5. Environmental information

Environmental, lifestyle, occupational, infectious, and toxicologic factors are **not applicable as demonstrated primary causes**. There is no evidence for infection-triggered disease or zoonotic transmission. General avoidance of ototoxic drugs is prudent for a person with SNHL, but it does not prevent the underlying genetic syndrome and is not a ZSCAN10-specific intervention.

## 6. Mechanism and pathophysiology

### Current causal model

The best-supported chain is:

**biallelic truncating ZSCAN10 variants → ZSCAN10 deficiency → disruption of transcriptional regulation during embryonic stem-cell pluripotency/lineage specification → abnormal neural and cranio-otic development → developmental delay, facial asymmetry, external-ear malformations, semicircular-canal dysplasia, and SNHL.**

The first two links are genetically established; ZSCAN10’s role in embryonic stem-cell pluripotency is established gene biology; the tissue-specific developmental links are biologically plausible interpretations of the human phenotype but remain incompletely mapped. The review identifies ZSCAN10 as a transcription factor that “controls pluripotency of embryonic stem cells.” (owrang2025neurogeneticdisorderswith pages 13-14)

### Upstream versus downstream

- **Upstream:** germline loss-of-function alleles and deficient transcription-factor activity.
- **Intermediate:** altered developmental transcriptional programs and cell-fate decisions; exact targets are unknown.
- **Downstream:** malformation of craniofacial/external-ear structures and the semicircular canals, plus neurodevelopmental and auditory dysfunction.

No disease-specific evidence currently establishes Wnt, MAPK, mTOR, PI3K–AKT, immune activation, oxidative stress, apoptosis, autophagy, fibrosis, enzyme deficiency, receptor dysfunction, ion-channel dysfunction, or a metabolic lesion. No syndrome-specific transcriptomic, proteomic, metabolomic, lipidomic, methylomic, single-cell, spatial-transcriptomic, multi-omic, CRISPR-screen, or patient-iPSC dataset was identified.

Suggested cell types—**only as developmental hypotheses**—include neural progenitor cells, cranial neural-crest derivatives, otic progenitors, cochlear sensory hair cells, and vestibular sensory cells. Candidate Cell Ontology labels include neural progenitor cell, neural crest cell, hair cell, and sensory neuron. These should be tagged “inferred,” not “experimentally demonstrated.”

## 7. Anatomical structures affected

Established or strongly indicated anatomical domains are:

- **Nervous system/brain:** inferred from global developmental delay; no specific cerebral lesion was recoverable.
- **Craniofacial complex:** facial asymmetry.
- **External ear/pinna:** congenital malformation.
- **Inner ear/vestibular labyrinth:** semicircular-canal dysplasia.
- **Auditory system:** SNHL, with the precise cochlear, neural, or mixed lesion not established.

Suggested UBERON labels are brain, face, external ear, inner ear, vestibular labyrinth, semicircular canal, cochlea, and auditory system. Suggested subcellular annotation is **nucleus**, reflecting transcription-factor localization. Laterality and degree of asymmetry were not available. (owrang2025neurogeneticdisorderswith pages 13-14)

## 8. Temporal development

The structural ear and facial findings imply prenatal/congenital origin; developmental delay and hearing impairment become clinically evident during infancy or childhood. The disease is expected to be lifelong. However, there is no longitudinal cohort establishing progression, developmental plateau, neurodegeneration, episodic worsening, remission, or adult natural history.

A critical practical period is early childhood, when hearing detection and language intervention may influence developmental trajectory. The expert review notes that hearing loss may occur early in neurogenetic disease and sometimes precede overt neurological findings. (owrang2025neurogeneticdisorderswith pages 13-14)

## 9. Inheritance and population

- **Inheritance:** autosomal recessive, biallelic.
- **Penetrance:** apparently high for the core phenotype among reported biallelic cases, but seven individuals are insufficient to estimate penetrance.
- **Expressivity:** likely variable, particularly for hearing loss, because only 4/5 tested individuals had confirmed SNHL; incomplete testing prevents a firm estimate.
- **Anticipation:** not expected and not reported.
- **Germline mosaicism:** not reported; a low residual recurrence risk may remain after apparently de novo findings, although de novo biallelic causation was not established here.
- **Founder effects, consanguinity, carrier frequency, sex ratio, ancestry effects, and geographic clustering:** unknown.
- **Prevalence/incidence:** unknown. Only seven cases were documented in the foundational report, which supports classification as ultra-rare but cannot yield a population prevalence. (owrang2025neurogeneticdisorderswith pages 13-14, owrang2025neurogeneticdisorderswith pages 18-19)

For confirmed carrier parents, the standard Mendelian expectation is a 25% affected, 50% carrier, and 25% unaffected/non-carrier probability in each pregnancy, assuming both parents carry pathogenic variants in the same gene.

## 10. Diagnostics

### Recommended clinical work-up

There are no formal syndrome-specific diagnostic criteria. A reasonable approach is:

1. Document developmental history, neurologic findings, facial asymmetry, and external-ear morphology.
2. Perform age-appropriate audiology—otoacoustic emissions, auditory brainstem response in infants or uncooperative children, and behavioral pure-tone/speech audiometry when feasible.
3. Use high-resolution temporal-bone MRI or CT when inner-ear malformation is suspected; MRI documented semicircular-canal dysplasia in the reported syndrome.
4. Obtain developmental, speech-language, vestibular, and otolaryngologic assessments.
5. Confirm **two pathogenic/likely pathogenic ZSCAN10 variants in trans**, with parental segregation where possible. (owrang2025neurogeneticdisorderswith pages 13-14)

### Genetic-testing strategy

- **Preferred discovery test:** trio whole-exome sequencing or whole-genome sequencing for syndromic developmental delay with hearing/ear anomalies.
- **Panel testing:** include ZSCAN10 on neurodevelopmental-disorder, syndromic hearing-loss, congenital ear-malformation, or intellectual-disability panels.
- **Single-gene testing:** suitable when the phenotype is highly characteristic or familial variants are known.
- **Deletion/duplication analysis:** consider if sequencing finds only one allele, although a ZSCAN10 copy-number mechanism was not established in the retrieved evidence.
- **CMA:** useful for the broader differential diagnosis but does not reliably detect small sequence variants.
- **Karyotype/FISH, mitochondrial DNA, and repeat-expansion tests:** not first-line tests for this specific molecular diagnosis.
- **RNA sequencing:** potentially useful to resolve splice variants, but no disease-specific diagnostic validation exists.

The 2025 review’s expert recommendation is that hearing loss in a child with developmental delay, hypotonia, or unexplained regression should prompt a neurogenetic diagnosis. (owrang2025neurogeneticdisorderswith pages 13-14)

### Differential diagnosis

Consider other syndromic causes combining neurodevelopmental impairment and hearing or ear malformations, including CHARGE syndrome/CHD7 disorder, branchio-oto-renal spectrum, Kabuki syndrome, craniofacial microsomia, and other recently defined neurogenetic hearing-loss disorders. Distinguishing features for ZSCAN10 deficiency are recessive inheritance and the combination of facial asymmetry, external-ear malformation, semicircular-canal dysplasia, and developmental delay. Because the cohort is very small, this gestalt is supportive rather than diagnostic.

## 11. Outcome and prognosis

Survival, mortality, life expectancy, adult independence, seizure risk, and long-term neurologic progression have not been quantified. No disease-specific prognostic biomarkers or prediction model exists. Likely morbidity arises from developmental disability and hearing impairment. Recovery of the congenital syndrome is not expected, although hearing, communication, education, and adaptive function may improve with early supportive intervention. No formal quality-of-life or disability-scale data are available.

## 12. Treatment

There is no approved disease-modifying therapy, genotype-specific drug, gene therapy, RNA therapy, cell therapy, immunotherapy, or registered disease-specific interventional trial in the retrieved evidence.

Management should therefore be individualized and multidisciplinary:

- early-developmental services and special education;
- speech-language therapy, including augmentative and alternative communication when required;
- audiology and otolaryngology follow-up;
- hearing aids where residual hearing permits;
- cochlear-implant evaluation for severe/profound SNHL, with anatomy assessed because semicircular-canal dysplasia is present;
- occupational and physical therapy according to functional deficits;
- vestibular assessment and balance therapy if symptomatic;
- clinical-genetics follow-up and family counseling.

These are extrapolated standards for developmental disability and pediatric SNHL, not interventions tested specifically in ZSCAN10 deficiency. Suitable NCIT concept labels include Genetic Counseling, Audiologic Examination, Hearing Aid, Cochlear Implantation, Speech and Language Therapy, Occupational Therapy, and Physical Therapy.

No response rates, adverse-event series, pharmacogenomic recommendations, combination algorithms, or experimental NCT identifiers exist for this syndrome.

## 13. Prevention

Primary prevention through lifestyle modification, vaccination, or avoidance of an exposure is not available. Reproductive prevention options after familial variants are known include carrier testing of relatives, prenatal diagnosis, and preimplantation genetic testing for monogenic disease. Secondary prevention consists of early molecular diagnosis, audiologic surveillance, and prompt developmental/hearing intervention. Tertiary prevention aims to limit communication, educational, balance, and functional complications. Genetic counseling should explain autosomal-recessive recurrence and available reproductive choices.

Population newborn genomic or carrier screening is not currently supported by prevalence, natural-history, or implementation evidence. Standard newborn hearing screening may detect hearing impairment but is neither sensitive nor specific for ZSCAN10 deficiency.

## 14. Other species and natural disease

No naturally occurring ZSCAN10-related otofacial neurodevelopmental syndrome was identified in companion animals, livestock, or wildlife. No breed association, OMIA entry, veterinary burden, cross-species transmission, or zoonotic potential was established. Orthologues likely exist in standard vertebrate models, but NCBI Gene and taxon identifiers should be verified directly before database import.

## 15. Model organisms and experimental systems

The retrieved literature supports a role for ZSCAN10 in embryonic stem-cell pluripotency and transcriptional regulation, but it did not establish a syndrome-specific knockout or knock-in animal model that recapitulates the human neurodevelopmental, external-ear, semicircular-canal, and hearing phenotypes. Accordingly, no model can yet be rated for phenotypic fidelity. (owrang2025neurogeneticdisorderswith pages 13-14)

High-priority future models are:

- CRISPR ZSCAN10-null human iPSCs differentiated toward neural-crest, neural, and otic lineages;
- patient-derived iPSCs with isogenic correction;
- zebrafish or mouse knockout/knock-in models assessed for craniofacial symmetry, ear morphology, vestibular function, auditory thresholds, and neurobehavior;
- rescue experiments restoring wild-type ZSCAN10 to establish causal reversibility;
- single-cell RNA/ATAC sequencing during otic and neural differentiation to identify downstream transcriptional targets.

These are proposed research applications, not currently validated implementations.

## Overall assessment

The syndrome–gene relationship is supported by a coherent 2024 human cohort, recessive loss-of-function genetics, and a biologically plausible role for ZSCAN10 in developmental transcription. Its defining clinical signal is the conjunction of developmental delay with characteristic otofacial and inner-ear abnormalities. Nevertheless, the evidence base remains at the initial disease-description stage: seven cases, incomplete hearing testing, no prevalence estimate, no longitudinal natural history, no disease-specific therapy, and no validated model or molecular biomarker. The immediate real-world application is therefore improved genomic diagnosis and early audiologic/developmental management—not molecularly targeted treatment. (owrang2025neurogeneticdisorderswith pages 13-14, OpenTargets Search: Otofacial neurodevelopmental syndrome)

References

1. (OpenTargets Search: Otofacial neurodevelopmental syndrome): Open Targets Query (Otofacial neurodevelopmental syndrome, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (owrang2025neurogeneticdisorderswith pages 13-14): Daniel Owrang and Barbara Vona. Neurogenetic disorders with hearing loss: mechanisms, classifications, and emerging insights. Current Neurology and Neuroscience Reports, Nov 2025. URL: https://doi.org/10.1007/s11910-025-01466-y, doi:10.1007/s11910-025-01466-y. This article has 2 citations and is from a domain leading peer-reviewed journal.

3. (owrang2025neurogeneticdisorderswith pages 18-19): Daniel Owrang and Barbara Vona. Neurogenetic disorders with hearing loss: mechanisms, classifications, and emerging insights. Current Neurology and Neuroscience Reports, Nov 2025. URL: https://doi.org/10.1007/s11910-025-01466-y, doi:10.1007/s11910-025-01466-y. This article has 2 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Otofacial_Neurodevelopmental_Syndrome-deep-research-falcon_artifacts/artifact-00.md)