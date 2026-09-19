---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-01T17:06:43.569706'
end_time: '2026-08-01T17:15:40.643572'
duration_seconds: 537.07
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Leber Hereditary Optic Neuropathy
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
  path: Leber_Hereditary_Optic_Neuropathy-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Leber Hereditary Optic Neuropathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Leber Hereditary Optic Neuropathy** covering all of the
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
- **Disease Name:** Leber Hereditary Optic Neuropathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Leber Hereditary Optic Neuropathy** covering all of the
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


# Leber Hereditary Optic Neuropathy: Comprehensive Disease-Characteristics Report

**Evidence scope.** This report prioritizes peer-reviewed 2023–2024 literature, supplemented by landmark studies and current ClinicalTrials.gov records. Most information is aggregated disease-level evidence; the cited Madrid registry study used linked health records plus clinician-confirmed cases, while clinical trials and cohorts contain individual-participant observations. The report is not based on a single patient’s EHR.

## Executive summary

Leber hereditary optic neuropathy (LHON) is an inherited mitochondrial neurodegenerative disorder characterized by selective loss of retinal ganglion cells (RGCs), producing rapid, painless, usually sequential bilateral central visual loss. Classical LHON is caused predominantly by one of three germline mitochondrial-DNA missense variants—**m.11778G>A in MT-ND4, m.3460G>A in MT-ND1, and m.14484T>C in MT-ND6**—which impair respiratory-chain complex I. Recently recognized, clinically similar autosomal-recessive forms result from biallelic nuclear variants, particularly in **DNAJC30**, and less commonly **NDUFS2, NDUFA12, MCAT**, and possibly other complex-I-associated genes. Incomplete, sex- and age-dependent penetrance means that carrying a pathogenic variant is not equivalent to developing optic neuropathy. (zeppieri2025isolatedandsyndromic pages 2-4, morgia2024recognizingleber’shereditary pages 1-2, lee2024hereditaryopticneuropathies pages 1-2, layrolle2024theopticnerve pages 2-4)

The upstream lesion is defective complex-I electron transfer; downstream consequences include impaired oxidative phosphorylation, reduced ATP reserve, excess reactive oxygen species, altered mitochondrial homeostasis, and apoptosis of metabolically vulnerable RGCs—especially small-caliber axons of the papillomacular bundle. This explains the characteristic central/centrocecal scotoma, dyschromatopsia, and eventual optic atrophy. (esmaeil2023leber’shereditaryoptic pages 1-2, layrolle2024theopticnerve pages 1-2, layrolle2024theopticnerve pages 2-4)

The principal disease-specific treatment is **idebenone**, authorized in Europe, commonly administered at 300 mg three times daily. Early and sufficiently prolonged therapy is favored. AAV2-mediated allotopic **ND4** gene replacement has produced sustained bilateral improvements in trials, but contralateral improvement after unilateral injection complicates efficacy interpretation; it was not established routine clinical care in the 2023–2024 evidence base. (lee2024hereditaryopticneuropathies pages 2-4, lee2024hereditaryopticneuropathies pages 4-5, NCT02652767 chunk 1, NCT03406104 chunk 1, NCT03293524 chunk 1)

| domain | key facts | ontology/identifier suggestions | evidence/source |
|---|---|---|---|
| Disease definition | Primary inherited optic neuropathy causing rapid, painless, usually sequential bilateral central vision loss due to selective retinal ganglion cell degeneration and mitochondrial dysfunction | MONDO: **MONDO:0010788**; OMIM: **535000**; MeSH: **D029242** (“Optic Atrophy, Hereditary, Leber”); Category: Mendelian, mitochondrial; autosomal-recessive subtype noted separately | (OpenTargets Search: Leber hereditary optic neuropathy, esmaeil2023leber’shereditaryoptic pages 1-2, NCT01892943 chunk 1) |
| Disease identifiers / subtypes | Classical form is maternally inherited mtDNA disease; autosomal-recessive LHON also recognized | OMIM arLHON: **619382**; MONDO arLHON: **MONDO:0030309**; “Leber-like hereditary optic neuropathy, autosomal recessive 1/2” MONDOs available via Open Targets context; ICD-10/ICD-11: **uncertain—verify in OMIM/Orphanet/WHO** | (OpenTargets Search: Leber hereditary optic neuropathy, lee2024hereditaryopticneuropathies pages 1-2, layrolle2024theopticnerve pages 1-2) |
| Synonyms | Leber hereditary optic neuropathy; Leber hereditary optic atrophy; hereditary optic atrophy, Leber type; LHON | Synonym curation term set; MeSH disease heading above | (NCT01892943 chunk 1, NCT02652767 chunk 1) |
| Causal genes / variants | >90–95% of cases due to three mtDNA missense variants affecting complex I: **m.11778G>A (MT-ND4)**, **m.3460G>A (MT-ND1)**, **m.14484T>C (MT-ND6)** | Genes: **MT-ND4, MT-ND1, MT-ND6**; variant class: missense, germline mtDNA; inheritance: mitochondrial | (esmaeil2023leber’shereditaryoptic pages 1-2, morgia2024recognizingleber’shereditary pages 1-2, layrolle2024theopticnerve pages 2-4) |
| Additional genetic causes | Nuclear autosomal-recessive LHON genes recently implicated: **DNAJC30, NDUFS2, NDUFAF5**; 2023 review also lists **MCAT, NDUFA12** in unresolved LHON phenotype | OMIM gene IDs available for DNAJC30 **618202**, NDUFS2 **612985**, NDUFAF5 **612360**; inheritance: autosomal recessive | (lee2024hereditaryopticneuropathies pages 1-2, zeppieri2025isolatedandsyndromic pages 2-4) |
| Modifier biology | Incomplete penetrance; male bias; estrogen proposed as protective for mitochondrial function; treatment response may be modified by **NQO1** levels | Modifier genes/factors: **NQO1** (pharmacogenetic response modifier), sex-related hormonal effect; haplogroup/heteroplasmy details **not fully resolved in gathered evidence** | (lee2024hereditaryopticneuropathies pages 2-4, lee2024hereditaryopticneuropathies pages 1-2, lee2024hereditaryopticneuropathies pages 4-5) |
| Environmental risk factors | Smoking, excessive alcohol use, and toxic medications/exposures are advised against in carriers; environmental triggers modulate disease expression | CHEBI/Exposures: tobacco smoke **uncertain CHEBI mapping here**; ethanol **CHEBI:16236** (verify if needed); exposure ontology terms **uncertain—verify** | (esmaeil2023leber’shereditaryoptic pages 1-2, layrolle2024theopticnerve pages 1-2, lee2024hereditaryopticneuropathies pages 4-5) |
| Protective / preventive factors | Avoid oxidative stressors; family screening/counseling; early recognition may enable treatment; vitamin B12 screening may be relevant in carriers because deficiency is enriched | Prevention annotations: cascade screening; genetic counseling; vitamin B12 monitoring (**CHEBI:176843 cyanocobalamin class mapping uncertain**) | (esmaeil2023leber’shereditaryoptic pages 1-2, lee2024hereditaryopticneuropathies pages 4-5) |
| Core phenotype | Bilateral painless subacute central visual loss, often sequential; dyschromatopsia; dense central/centrocecal scotoma; poor acuity often worse than 20/200 | HPO suggestions: **central scotoma (HP term verify)**, **decreased visual acuity (HP term verify)**, **dyschromatopsia/color vision defect (HP term verify)**, **optic atrophy (HP:0000648 likely, verify)** | (zeppieri2025isolatedandsyndromic pages 2-4, esmaeil2023leber’shereditaryoptic pages 1-2, lee2024hereditaryopticneuropathies pages 2-4, morgia2024recognizingleber’shereditary pages 1-2) |
| Fundus / structural ocular findings | Acute/subacute phase may show optic disc hyperemia, peripapillary telangiectasia, vascular tortuosity, RNFL swelling; chronic phase shows RNFL and ganglion cell thinning with temporal then diffuse optic pallor | HPO suggestions: **optic disc pallor (verify)**, **retinal nerve fiber layer thinning (verify)**, **abnormality of color vision (verify)** | (zeppieri2025isolatedandsyndromic pages 2-4, esmaeil2023leber’shereditaryoptic pages 1-2, morgia2024recognizingleber’shereditary pages 1-2, layrolle2024theopticnerve pages 2-4) |
| Disease stages / temporal development | Stages commonly described as asymptomatic carrier, subacute **<6 months**, dynamic **6–12 months**, chronic **>12 months**; second eye usually affected within weeks to months | Temporal annotations for KB; onset: adolescent/young adult; pattern: subacute progressive bilateral sequential | (zeppieri2025isolatedandsyndromic pages 2-4, lee2024hereditaryopticneuropathies pages 2-4, iorga2025evaluationofvisual pages 1-2) |
| Age / sex distribution | Peak onset typically **15–30/35 years**; onset can range from childhood to late adulthood; male predominance; penetrance estimates in gathered evidence range around **17.5% males, 5.4% females** or older estimates **40–50% males, ~10% females** | Demography fields: male-biased expression; age-at-onset = adolescent/young adult | (esmaeil2023leber’shereditaryoptic pages 1-2, lee2024hereditaryopticneuropathies pages 2-4, morgia2024recognizingleber’shereditary pages 1-2, lee2024hereditaryopticneuropathies pages 1-2) |
| Epidemiology | Prevalence estimates vary by population: approximately **1/30,000 to 1/50,000** commonly cited; Madrid population study estimated **0.55/100,000 confirmed**, **0.79/100,000 capture-recapture**; susceptibility allele prevalence may be **1 in 800–1000** | Epidemiology fields: prevalence, sex-stratified prevalence; disease rarity | (esmaeil2023leber’shereditaryoptic pages 1-2, morgia2024recognizingleber’shereditary pages 1-2, layrolle2024theopticnerve pages 1-2) |
| Extraocular / LHON-plus manifestations | Some patients have neurologic/systemic disease: dystonia, epilepsy, cerebellar ataxia, parkinsonism, myoclonus, peripheral neuropathy, encephalopathy; cardiac/endocrine dysfunction; overlap with multiple sclerosis (“Harding disease”) | HPO suggestions: **ataxia (verify)**, **peripheral neuropathy (verify)**, **dystonia (verify)**; disease note: LHON-plus / Harding disease | (lee2024hereditaryopticneuropathies pages 2-4, layrolle2024theopticnerve pages 2-4) |
| Molecular mechanism | Primary lesion is **complex I dysfunction** in oxidative phosphorylation, reducing ATP generation and increasing reactive oxygen species; this initiates retinal ganglion cell dysfunction/apoptosis | GO suggestions: **oxidative phosphorylation (GO:0006119)**, **mitochondrial electron transport, NADH to ubiquinone (GO term verify)**, **ATP synthesis coupled electron transport (GO:0042773 verify)**, **reactive oxygen species metabolic process (GO:0072593 verify)**, **apoptotic process (GO:0006915)** | (layrolle2024theopticnerve pages 1-2, layrolle2024theopticnerve pages 2-4) |
| Selective vulnerability | Preferential involvement of small axons in the **papillomacular bundle** serving central vision; degeneration extends along optic pathways | Anatomy/process links: papillomacular bundle **anatomy term uncertain—verify**; optic nerve degeneration | (zeppieri2025isolatedandsyndromic pages 2-4, layrolle2024theopticnerve pages 2-4) |
| Cell types involved | Primary affected cells are **retinal ganglion cells** and their axons; glial involvement/demyelination inferred in visual pathways on MRI/histopathology | CL suggestions: **retinal ganglion cell (CL term verify)**; oligodendrocyte/astrocyte involvement **secondary, verify** | (esmaeil2023leber’shereditaryoptic pages 1-2, layrolle2024theopticnerve pages 2-4) |
| Anatomy affected | Retina, retinal nerve fiber layer, ganglion cell layer, optic disc, optic nerve, optic chiasm/tracts, lateral geniculate nucleus, visual cortex | UBERON suggestions: **retina (UBERON:0000966 likely, verify)**, **optic nerve (UBERON term verify)**, **optic chiasm (verify)**, **lateral geniculate nucleus (verify)**, **visual cortex (verify)** | (layrolle2024theopticnerve pages 2-4) |
| Subcellular localization | Inner mitochondrial membrane / respiratory chain complex I are central sites of dysfunction | GO Cellular Component suggestions: **mitochondrion (GO:0005739)**, **mitochondrial inner membrane (GO:0005743)**, **respiratory chain complex I (GO term verify)** | (layrolle2024theopticnerve pages 1-2, layrolle2024theopticnerve pages 2-4) |
| Diagnostic workflow | Clinical recognition plus targeted genetic testing for three common mtDNA variants first; if negative but suspicion persists, comprehensive mtDNA sequencing; consider nuclear arLHON genes if unresolved | Diagnostic concepts: targeted mtDNA testing; full mtDNA sequencing; nuclear gene panel incl. **DNAJC30/NDUFS2/NDUFAF5** and others | (zeppieri2025isolatedandsyndromic pages 2-4, morgia2024recognizingleber’shereditary pages 1-2) |
| Diagnostic tests | Ophthalmic evaluation includes ETDRS visual acuity, OCT (RNFL/GCL changes), visual field testing with central/centrocecal scotoma, contrast sensitivity, color vision testing | LOINC-specific mappings **not gathered**; functional tests: OCT, Humphrey visual field, Pelli-Robson, Farnsworth-Munsell | (esmaeil2023leber’shereditaryoptic pages 1-2, NCT02652767 chunk 1, NCT02652767 chunk 2) |
| Differential diagnosis | Frequently misdiagnosed as inflammatory optic neuritis; also other optic neuropathies/toxic-metabolic causes should be excluded | Differential disease concepts: optic neuritis, NMOSD/MOGAD-related optic neuritis, toxic/nutritional optic neuropathy | (morgia2024recognizingleber’shereditary pages 1-2) |
| Prognosis / natural history | Visual acuity often plateaus by ~4 months at severe impairment; spontaneous recovery depends strongly on genotype, best with **m.14484T>C**; chronic deficits common | Prognosis fields: genotype-dependent recovery; early childhood onset may have better prognosis | (lee2024hereditaryopticneuropathies pages 2-4, catarino2017useofidebenone pages 5-6) |
| Variant-specific recovery | Spontaneous recovery estimates in gathered evidence: **m.14484T>C up to 70%** (or 37–71% in older review) vs **m.11778G>A ~4–23% / ~15%** and **m.3460G>A ~15–25% / ~15%** | Genotype–phenotype annotation | (morgia2024recognizingleber’shereditary pages 1-2, catarino2017useofidebenone pages 5-6) |
| Quality of life / burden | Vision-related QoL is markedly impaired; Slovenian 2024 patient study reported mean **VFQ-25 = 30.4 (SD 12.9)** and annual productivity loss **EUR 11,608/person** | Outcome concepts: VFQ-25 composite score; disability/productivity loss | (NCT03406104 chunk 1) |
| Standard treatment | **Idebenone** is the main approved disease-specific therapy in Europe; commonly dosed **300 mg three times daily (900 mg/day)**, usually for **≥1 year**, ideally within **12 months** of onset | NCIT suggestions: **Idebenone (NCIT term verify)**; treatment class: antioxidant / quinone analog | (lee2024hereditaryopticneuropathies pages 2-4, catarino2017useofidebenone pages 5-6, zeppieri2025isolatedandsyndromic pages 13-14) |
| Idebenone evidence | RHODOS secondary endpoints favored idebenone; LEROS showed higher clinically relevant benefit at 12 months versus natural history cohort; longer treatment may improve chance of recovery | NCIT concept: pharmacologic intervention; pharmacogenetic modifier: **NQO1** low-level variants associated with poorer response | (lee2024hereditaryopticneuropathies pages 4-5) |
| Gene therapy | **Lenadogene nolparvovec / GS010 / rAAV2/2-ND4** studied in RESCUE, REVERSE, REFLECT, RESTORE; unilateral and bilateral intravitreal approaches investigated | NCIT suggestions: **Gene Therapy (NCIT:C15238)**; **Intravitreal Injection (NCIT term verify)**; vector: AAV2-based ND4 allotopic expression | (NCT02652767 chunk 1, NCT03406104 chunk 1, NCT03293524 chunk 1) |
| Gene-therapy trial details | RESCUE enrolled **39**; RESTORE long-term follow-up enrolled **62**; REFLECT enrolled **98**; outcomes included BCVA, OCT GCL/RNFL, visual field, contrast sensitivity, color vision, QoL | ClinicalTrials.gov IDs: **NCT02652767 (RESCUE)**, **NCT03406104 (RESTORE)**, **NCT03293524 (REFLECT)** | (NCT02652767 chunk 1, NCT03406104 chunk 1, NCT03293524 chunk 1) |
| Supportive care | Visual rehabilitation and psychological support are recommended for all patients; counseling to avoid smoking/alcohol/toxic medications in carriers | NCIT suggestions: **Rehabilitation (verify)**, **Psychological Support (verify)** | (lee2024hereditaryopticneuropathies pages 4-5) |
| Prevention / counseling | No established pharmacologic prophylaxis for unaffected carriers in gathered evidence; emphasize maternal inheritance/arLHON counseling, cascade testing, avoidance of triggers, and timely diagnosis | Genetic counseling; family screening; reproductive counseling | (esmaeil2023leber’shereditaryoptic pages 1-2, layrolle2024theopticnerve pages 1-2, lee2024hereditaryopticneuropathies pages 4-5) |
| Model systems | Cybrids, patient-derived fibroblasts, iPSC-derived retinal ganglion cells, and retinal organoids model LHON; models show increased RGC death, ATP/membrane-potential deficits, and rescue with correction or idebenone in some systems | Model annotations: **in vitro cybrid**, **iPSC-RGC**, **retinal organoid**; animal models mentioned but robust human-like models remain limited | (esmaeil2023leber’shereditaryoptic pages 1-2, zeppieri2025isolatedandsyndromic pages 13-14) |
| Model readouts / limitations | iPSC/cybrid-corrected systems help test causality and rescue; limitations include incomplete reproduction of whole visual pathway and scarcity of robust animal models for selective human RGC degeneration | Evidence type labels: human cell model, organoid, translational preclinical model | (zeppieri2025isolatedandsyndromic pages 13-14) |


*Table: This compact table organizes gathered Leber hereditary optic neuropathy facts into knowledge-base-ready domains, including identifiers, genetics, phenotypes, mechanisms, diagnostics, treatment, epidemiology, and models. Ontology and identifier fields are suggested conservatively, with uncertain IDs clearly marked for later verification.*

## 1. Disease information

### Definition and identifiers

LHON is a primary inherited optic neuropathy and mitochondrial disease causing acute/subacute degeneration of RGCs and the optic nerve.

* **MONDO:** MONDO:0010788.
* **OMIM:** #535000, LHON; autosomal-recessive LHON #619382.
* **MeSH:** D029242, *Optic Atrophy, Hereditary, Leber*.
* **Autosomal-recessive MONDO entry:** MONDO:0030309.
* **Orphanet:** commonly indexed as ORPHA:104; this identifier should be validated against the current Orphanet release before production ingestion.
* **ICD:** LHON is generally coded within hereditary optic atrophy/optic-nerve disorder categories rather than by a uniformly implemented disease-specific ICD-10 code. Country-specific mappings and the current ICD-11 browser should therefore be checked before deployment.

Open Targets associates MONDO:0010788 most strongly with MT-ND1, MT-ND4, MT-ND6 and other mitochondrial genes, and recognizes DNAJC30/NDUFS2 associations for autosomal-recessive LHON. (OpenTargets Search: Leber hereditary optic neuropathy, lee2024hereditaryopticneuropathies pages 1-2, layrolle2024theopticnerve pages 1-2, NCT01892943 chunk 1)

**Synonyms:** Leber hereditary optic neuropathy; Leber’s hereditary optic neuropathy; LHON; Leber hereditary optic atrophy; hereditary optic atrophy, Leber type. It must not be confused with **Leber congenital amaurosis**, a different retinal dystrophy.

## 2. Etiology, risk, and protective factors

### Causal factors

Approximately 90–95% of molecularly resolved classical cases carry one of three mtDNA variants: m.11778G>A (MT-ND4; usually the most frequent), m.3460G>A (MT-ND1), or m.14484T>C (MT-ND6). These are germline, maternally transmitted missense variants, usually homoplasmic, affecting complex-I subunits. More than 50 rarer mtDNA variants have been reported, but pathogenicity requires careful evaluation because mtDNA variation is common. (morgia2024recognizingleber’shereditary pages 1-2, lee2024hereditaryopticneuropathies pages 1-2, layrolle2024theopticnerve pages 2-4)

Autosomal-recessive LHON phenocopies classical disease. **DNAJC30** is particularly important in Eastern and Central European populations; biallelic **NDUFS2, MCAT, NDUFA12**, and reported **NDUFAF5** defects should be considered when the phenotype is convincing but mtDNA testing is unrevealing. These discoveries overturn the older assumption that all LHON is maternally inherited. (zeppieri2025isolatedandsyndromic pages 2-4, lee2024hereditaryopticneuropathies pages 1-2)

### Genetic susceptibility and modifiers

Penetrance is incomplete. Older estimates were approximately 40–50% in male and 10% in female carriers; more recent family data cited in 2024 guidance estimate 17.5% in males and 5.4% in females. Differences reflect ascertainment, genotype, age, ancestry, exposure, and family structure. Male predominance is not explained by mtDNA inheritance alone; estrogen-enhanced mitochondrial biogenesis and antioxidant defenses are a plausible protective mechanism, but not a clinically validated prophylaxis. (lee2024hereditaryopticneuropathies pages 2-4, morgia2024recognizingleber’shereditary pages 1-2, lee2024hereditaryopticneuropathies pages 1-2, layrolle2024theopticnerve pages 1-2)

Mitochondrial haplogroup, heteroplasmic load, nuclear background, and mitochondrial biogenesis influence expression, although no single modifier predicts conversion adequately. A clinically relevant 2024 development is evidence that variants lowering **NQO1** protein can impair activation/effectiveness of idebenone, making NQO1 a candidate pharmacogenetic response modifier rather than a primary cause. (lee2024hereditaryopticneuropathies pages 4-5)

### Environmental and lifestyle risks

Smoking is the best-supported modifiable risk factor. Heavy alcohol use is also associated with conversion, probably through oxidative stress, nutritional deficiency, and mitochondrial toxicity; the evidence for moderate alcohol is weaker. Other reported precipitating contexts include nutritional deficiency, severe illness, mitochondrial-toxic medicines, occupational toxins, and some antiretroviral, antitubercular, or toxic-optic-neuropathy drugs, but most drug associations rest on case reports rather than controlled estimates. There is no infectious cause and no zoonotic transmission. (esmaeil2023leber’shereditaryoptic pages 1-2, layrolle2024theopticnerve pages 1-2, lee2024hereditaryopticneuropathies pages 4-5)

A prospective cohort of 244 carriers/patients found vitamin-B12 deficiency in 21% of carriers younger than 65 versus 5–7% in the comparison population; excessive alcohol was a significant predictor. This does not prove that B12 deficiency triggers conversion, but supports periodic screening and correction. 

### Protective factors and gene–environment interaction

Recommended risk reduction consists of smoking abstinence, avoiding binge/heavy alcohol use, maintaining adequate nutrition—especially B12—and avoiding unnecessary mitochondrial/optic-nerve toxins. No medication has proven primary prophylactic efficacy in unaffected carriers. The conceptual interaction is: **pathogenic complex-I genotype → reduced bioenergetic reserve → sex/nuclear/mtDNA-background modulation → environmental oxidative or nutritional stress → threshold crossing → RGC dysfunction and death**. (layrolle2024theopticnerve pages 1-2, lee2024hereditaryopticneuropathies pages 4-5)

## 3. Phenotypes

### Core ocular phenotype

The typical patient is an otherwise healthy adolescent or young adult, often male, with painless blurring and impaired color vision in one eye, followed by the fellow eye within approximately 6–12 weeks or 2–3 months. Simultaneous bilateral onset occurs in roughly 25–50% in older series. Visual acuity frequently deteriorates to worse than 20/200, counting fingers, or poorer, with a dense central or centrocecal scotoma and markedly impaired contrast and color discrimination. Relative afferent pupillary asymmetry may be absent once disease is bilateral. (zeppieri2025isolatedandsyndromic pages 2-4, esmaeil2023leber’shereditaryoptic pages 1-2, lee2024hereditaryopticneuropathies pages 2-4, morgia2024recognizingleber’shereditary pages 1-2)

Acute fundus signs include optic-disc hyperemia, circumpapillary telangiectatic microangiopathy, vascular tortuosity, and pseudoedema/RNFL swelling without typical fluorescein leakage. Macular ganglion-cell thinning can precede symptoms, while peripapillary RNFL initially thickens and then becomes severely thin. Chronic disease produces temporal and subsequently diffuse optic pallor. (zeppieri2025isolatedandsyndromic pages 2-4, esmaeil2023leber’shereditaryoptic pages 1-2, morgia2024recognizingleber’shereditary pages 1-2, layrolle2024theopticnerve pages 2-4)

**Suggested HPO annotations:** optic atrophy (HP:0000648); reduced visual acuity; central/centrocecal scotoma; color-vision defect/dyschromatopsia; painless visual loss; retinal nerve-fiber-layer thinning; optic-disc pallor; vascular tortuosity. Exact HPO identifiers other than HP:0000648 should be validated against the current HPO release.

### Frequency, onset, severity, and progression

Peak onset is approximately 15–30 years; reported onset spans about 2–90 years, and around 10% may present after 50. Mean onset is approximately 25 years in males and 30 in females. Vision often reaches a nadir or plateau near four months. Most macular RGC loss is completed in the first six months, although anatomic degeneration may continue after functional stabilization. Childhood onset, especially before age 9–12, is less typical and often has a better prognosis. (zeppieri2025isolatedandsyndromic pages 2-4, esmaeil2023leber’shereditaryoptic pages 1-2, lee2024hereditaryopticneuropathies pages 2-4)

### LHON-plus

A minority develop extraocular disease—movement disorders, dystonia, tremor, parkinsonism, ataxia, epilepsy, myoclonus, peripheral neuropathy, myopathy, encephalopathy, cardiac conduction abnormalities, or endocrine dysfunction. Coexisting LHON and multiple-sclerosis-like disease is termed **Harding disease** and is reported disproportionately in women. In one cited imaging cohort, as many as 25% of 31 patients had MS-like T2 lesions, but causal overlap remains uncertain. (lee2024hereditaryopticneuropathies pages 2-4, layrolle2024theopticnerve pages 2-4)

### Quality of life

Severe central visual loss impairs reading, driving, education, employment, facial recognition, and independent navigation, with substantial psychological effects. A 2024 Slovenian study of nine adults—one-third of known national cases—reported mean VFQ-25 of **30.4/100 (SD 12.9)** and estimated annual productivity loss of **€11,608 per affected person**. Its small sample limits generalizability, but quantifies the major real-world burden.

## 4. Genetic and molecular information

### Variant classes and population frequency

The three primary variants are germline mtDNA single-nucleotide missense substitutions. They are commonly homoplasmic, so a conventional nuclear-variant allele frequency is not directly applicable. Population genomic studies find primary LHON susceptibility variants in approximately 1/800–1/1,000 people—far more common than manifest disease—illustrating low penetrance and the danger of interpreting genotype without phenotype and pedigree. Heteroplasmic cases require quantification in blood and, if suspicion remains, another tissue because heteroplasmy may vary by tissue. (layrolle2024theopticnerve pages 1-2, layrolle2024theopticnerve pages 2-4)

Nuclear arLHON variants are biallelic germline variants and can include missense, frameshift, nonsense, and splice-altering alleles. Classification should follow ACMG/AMP criteria with segregation, population frequency, phenotype, and functional evidence; ClinVar assertions must be reviewed variant by variant. Somatic mutation is not the usual etiology. Large chromosomal abnormalities, repeat expansions, aneuploidy, and translocations are not established causes, so karyotype, FISH, and chromosomal microarray are low-yield in a typical isolated LHON phenotype.

### Epigenetics and omics

No validated disease-defining methylation, histone, or chromatin signature is used clinically. Transcriptomic work in patient-specific RGCs has implicated altered glutamatergic/AMPA-receptor signaling; cellular models also demonstrate abnormal mitochondrial transport, bioenergetics, apoptosis susceptibility, and mitophagy. These remain research findings rather than diagnostic biomarkers. Single-cell and spatial-transcriptomic human data are still limited, largely because affected retinal and optic-nerve tissue is inaccessible.

## 5. Environmental information

Tobacco smoke and heavy alcohol are the principal actionable exposures. Nutritional insufficiency, particularly B12 deficiency, may compound mitochondrial dysfunction. Occupational solvent/toxin exposure should be elicited because toxic optic neuropathy both mimics and may aggravate LHON. Radiation, pollution, and exercise have no established disease-specific causal estimates. There is no recognized bacterial, viral, fungal, or parasitic etiology. (esmaeil2023leber’shereditaryoptic pages 1-2, layrolle2024theopticnerve pages 1-2)

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream genetic lesion:** defective mtDNA- or nuclear-encoded complex-I component/maintenance protein.
2. **Respiratory dysfunction:** impaired NADH-to-ubiquinone electron transfer and reduced proton-gradient efficiency.
3. **Metabolic stress:** diminished ATP reserve, altered NADH/NAD+ redox balance, and increased electron leak/ROS.
4. **Cellular response:** altered mitochondrial dynamics, transport, mitophagy, membrane potential, calcium/redox signaling, and heightened apoptotic susceptibility.
5. **Selective tissue injury:** RGC somata and their long, partly unmyelinated, energy-intensive axons—especially the papillomacular bundle—fail.
6. **Clinical manifestation:** central/centrocecal field loss, dyschromatopsia, severe central acuity loss, RNFL/GCL thinning, and optic atrophy. (layrolle2024theopticnerve pages 1-2, layrolle2024theopticnerve pages 2-4)

Complex I is embedded in the mitochondrial inner membrane and normally oxidizes NADH while reducing ubiquinone. Idebenone’s rationale is to accept electrons through NQO1 and deliver them downstream to complex III, partly bypassing complex I while also limiting oxidative injury. (zeppieri2025isolatedandsyndromic pages 13-14, lee2024hereditaryopticneuropathies pages 4-5, layrolle2024theopticnerve pages 2-4)

**Suggested GO terms:** oxidative phosphorylation (GO:0006119); apoptotic process (GO:0006915); mitochondrial electron transport, NADH to ubiquinone; ATP synthesis coupled electron transport; reactive-oxygen-species metabolic process; mitophagy; mitochondrial transport. **GO cellular components:** mitochondrion (GO:0005739), mitochondrial inner membrane (GO:0005743), respiratory-chain complex I. **Cell Ontology:** retinal ganglion cell; astrocyte and oligodendrocyte may be secondary participants. Exact current IDs should be release-validated.

Immune activation is not the primary mechanism, although secondary gliosis/inflammation may accompany degeneration. MRI abnormalities can resemble inflammatory demyelination, explaining frequent misdiagnosis.

## 7. Anatomical structures affected

The primary organ is the eye/afferent visual system. At tissue level, the retinal ganglion-cell layer, RNFL, optic disc, papillomacular bundle, and optic nerve are affected. MRI and pathology show downstream involvement of optic chiasm, optic tracts, lateral geniculate nuclei, optic radiations, and visual cortex. Histopathology has found up to approximately 95% reduction in temporal fibers and 40% reduction in optic-nerve cross-sectional area compared with controls. Disease is ultimately bilateral, often sequential and mildly asymmetric early. (layrolle2024theopticnerve pages 2-4)

**Suggested UBERON:** retina (UBERON:0000966), optic nerve, optic chiasm, optic tract, lateral geniculate nucleus, and visual cortex; validate exact release-specific IDs. Subcellular localization is the mitochondrial inner membrane/complex I.

## 8. Temporal development

A practical staging system is:

* **Asymptomatic carrier:** normal acuity, although subtle color, electrophysiologic, OCT, or microvascular abnormalities may occur.
* **Subacute, <6 months:** rapid visual decline, disc hyperemia/telangiectasia, RNFL swelling, early GCL loss.
* **Dynamic, 6–12 months:** continued structural loss, transition from swelling to atrophy; some eyes begin recovery.
* **Chronic, >12 months:** stable severe central deficit and optic atrophy, with possible delayed recovery.

The fellow eye is most vulnerable in the first weeks to months. This and the period before extensive GCL/RNFL loss constitute the strongest opportunity for intervention. Spontaneous or treatment-associated improvement may begin after approximately one year and continue for years; it is recovery rather than true remission because the causal genotype persists. (zeppieri2025isolatedandsyndromic pages 2-4, lee2024hereditaryopticneuropathies pages 2-4, iorga2025evaluationofvisual pages 1-2, catarino2017useofidebenone pages 5-6)

## 9. Inheritance and population

Classical LHON is maternally inherited: all children of a woman carrying the mtDNA variant may inherit it, while affected men do not transmit their mtDNA. Penetrance is incomplete, age-dependent, sex-biased, and family-specific. Expressivity is variable; anticipation is not established. Germline mosaicism is less relevant than heteroplasmy/mitotic segregation. Consanguinity is not important for classical mtLHON but may increase arLHON risk. Nuclear arLHON follows autosomal-recessive inheritance, giving a 25% affected-child risk when both parents carry pathogenic alleles in the same gene.

Manifest-disease prevalence in Europe is often reported between 1/27,000 and 1/50,000. A rigorous 2024 Madrid study identified 37 confirmed cases: observed prevalence **0.55/100,000** and capture–recapture prevalence **0.79/100,000**, 43.6% higher than observed; sex-specific estimates were 1.15/100,000 in men and 0.43/100,000 in women, with a male:female ratio of 2.4:1. This study also showed that automated health-record ascertainment had low positive predictive value, emphasizing clinician confirmation. (zeppieri2025isolatedandsyndromic pages 2-4, esmaeil2023leber’shereditaryoptic pages 1-2, morgia2024recognizingleber’shereditary pages 1-2)

Founder effects occur: m.14484T>C is enriched in some French-Canadian pedigrees, while DNAJC30 p.Tyr51Cys is prominent in Eastern Europe. Carrier frequency is much higher than disease prevalence because penetrance is low.

## 10. Diagnostics

### Clinical and functional evaluation

Urgent neuro-ophthalmic assessment should document best-corrected visual acuity, color vision, contrast sensitivity, automated visual fields, pupils, dilated fundus examination, fundus photography, and spectral-domain OCT of peripapillary RNFL and macular GCL/GCC. OCT can reveal GCL loss before obvious optic atrophy and helps distinguish LHON from inflammatory optic neuritis. Visual evoked potentials and pattern electroretinography/photopic negative response can document RGC dysfunction but are not required for molecular confirmation. MRI of brain and orbits with contrast is useful in atypical cases to exclude inflammation, compression, and demyelination; LHON can nevertheless show optic-nerve/chiasmal T2 abnormalities. (esmaeil2023leber’shereditaryoptic pages 1-2, morgia2024recognizingleber’shereditary pages 1-2, layrolle2024theopticnerve pages 2-4, NCT02652767 chunk 2)

Routine blood tests should be directed at mimics or modifiers: B12 with methylmalonic acid/homocysteine when indicated, folate, thiamine, copper, CBC, metabolic panel, and toxic-exposure testing. Lactate may be normal and is neither sensitive nor specific. Biopsy is generally unnecessary.

### Genetic workflow

1. Test blood for m.11778G>A, m.3460G>A, and m.14484T>C.
2. If negative but suspicion remains, sequence the entire mitochondrial genome with heteroplasmy-sensitive methods and assess deletion/coverage quality.
3. If mtDNA testing is unrevealing, use an inherited-optic-neuropathy/nuclear mitochondrial panel including at least DNAJC30, NDUFS2, NDUFA12, MCAT, NDUFAF5, and differential genes such as OPA1.
4. WES/WGS is useful for unresolved or syndromic disease; WGS may better capture mtDNA and structural/noncoding variation, but laboratory validation is required.
5. Test the maternal lineage or siblings for segregation and counseling. (morgia2024recognizingleber’shereditary pages 1-2, lee2024hereditaryopticneuropathies pages 1-2)

CMA, karyotyping, FISH, and repeat-expansion tests are not first-line. RNA-seq, proteomics, metabolomics, epigenomics, and liquid biopsy are investigational, not standard diagnostics.

### Differential diagnosis

Major alternatives are inflammatory optic neuritis associated with multiple sclerosis, AQP4-NMOSD or MOGAD; dominant optic atrophy; toxic/nutritional optic neuropathy; compressive optic neuropathy; ischemic optic neuropathy; glaucoma; macular disease; and other mitochondrial syndromes. LHON is favored by painless sequential central loss, male/maternal pedigree, disc telangiectasia without leakage, early macular GCL loss, poor spontaneous early recovery, and a pathogenic genotype. Prompt distinction matters because corticosteroids/plasma exchange treat inflammatory disease but not primary LHON. (morgia2024recognizingleber’shereditary pages 1-2)

No population newborn screening is established. Cascade testing of maternal relatives and targeted testing of at-risk siblings in arLHON are appropriate after counseling.

## 11. Outcome and prognosis

LHON usually does not directly shorten life expectancy, and disease-specific survival statistics are not meaningful for isolated disease. Morbidity is substantial because severe central blindness occurs during education and working life. LHON-plus disease may add neurologic or cardiac risk and warrants phenotype-directed surveillance.

Spontaneous recovery is genotype-dependent: approximately **37–71% or as high as 70%** for m.14484T>C, **4–23%** for m.11778G>A, and **15–25%** for m.3460G>A in cited series. Recovery definitions and follow-up differ substantially. Favorable factors include m.14484T>C, younger/childhood onset, larger residual RNFL/GCL reserve, and possibly earlier treatment; m.11778G>A generally has the poorest natural prognosis. (morgia2024recognizingleber’shereditary pages 1-2, catarino2017useofidebenone pages 5-6)

## 12. Treatment

### Idebenone

Idebenone is a short-chain benzoquinone/CoQ analog and antioxidant. The standard European regimen is **900 mg/day—300 mg three times daily with food**. Consensus practice favors initiation as soon as possible, preferably within one year of onset, and continuation for at least one year; because recovery can be delayed, two years or continuation until a stable plateau is often considered. It is the only EMA-authorized disease-specific treatment in the gathered evidence. (lee2024hereditaryopticneuropathies pages 2-4, catarino2017useofidebenone pages 5-6, zeppieri2025isolatedandsyndromic pages 13-14)

RHODOS enrolled 85 patients and missed its prespecified primary endpoint, but secondary analyses favored idebenone. LEROS compared **199 treated patients with 372 external natural-history controls** and found significantly more clinically relevant benefit at 12 months. Benefit varied by stage and genotype: subacute/dynamic benefit was clearest for m.11778G>A; chronic m.11778G>A and m.14484T>C groups showed consistent benefit, whereas m.3460G>A showed less effect. This is meaningful but not equivalent to a contemporaneous randomized comparison. (lee2024hereditaryopticneuropathies pages 2-4, lee2024hereditaryopticneuropathies pages 4-5)

Common trial adverse events were generally mild—nasopharyngitis 25.5%, headache 23.6%, and cough 10.9% in the cited RHODOS analysis. Candidate NQO1 low-expression genotypes may predict poorer response, but routine NQO1-guided prescribing is not yet established. (catarino2017useofidebenone pages 5-6, lee2024hereditaryopticneuropathies pages 4-5)

**NCIt suggestions:** Idebenone; antioxidant; pharmacologic intervention. Verify current NCIt concept codes before ingestion.

### Gene therapy

Lenadogene nolparvovec (GS010) uses intravitreal rAAV2/2 to deliver a nuclear-compatible wild-type ND4 with a mitochondrial targeting sequence—**allotopic expression**. RESCUE was a randomized, quadruple-masked phase III trial in 39 patients with ≤6 months’ visual loss; one eye received 9×10^10 vector genomes and the fellow eye sham. Both eyes improved, undermining the within-patient comparison, plausibly because vector/DNA or biological signaling crossed the optic pathways. (lee2024hereditaryopticneuropathies pages 4-5, NCT02652767 chunk 1)

REFLECT enrolled 98 patients with ≤1 year of loss and compared bilateral active injection with active first-eye/placebo fellow-eye treatment. RESTORE followed 62 RESCUE/REVERSE participants to five years and assessed BCVA, clinically relevant recovery, adverse events, and VFQ-25 quality of life. These studies support durable biological activity, but bilateral improvement after unilateral dosing, natural recovery, and absence of an independent untreated group limit causal effect estimates. (NCT03406104 chunk 1, NCT03293524 chunk 1)

Relevant records and URLs:

* RESCUE, **NCT02652767**: https://clinicaltrials.gov/study/NCT02652767.
* RESTORE, **NCT03406104**: https://clinicaltrials.gov/study/NCT03406104.
* REFLECT, **NCT03293524**: https://clinicaltrials.gov/study/NCT03293524.
* Historical natural history, **NCT01892943**, 306 records: https://clinicaltrials.gov/study/NCT01892943. (NCT01892943 chunk 1, NCT02652767 chunk 1, NCT03406104 chunk 1, NCT03293524 chunk 1)

As of the 2023–2024 literature, gene therapy remained investigational/not routine, and the European marketing application had been withdrawn. New trials should not be represented as approved care. **NCIt suggestions:** gene therapy (NCIt C15238), viral-vector therapy, intravitreal injection.

### Other and supportive approaches

Brimonidine, cyclosporine, EPI-743/vatiquinone, elamipretide, bezafibrate, nicotinamide, mitochondrial biogenesis agents, stem cells, and mitochondrial gene editing/replacement remain experimental or unsupported for routine LHON care. The completed bezafibrate trial is NCT04561466; early rAAV2-ND4 studies include NCT01267422 and NCT03153293. No surgery restores the optic nerve. Low-vision rehabilitation, assistive technology, orientation/mobility training, occupational/educational accommodations, psychological care, and management of depression are essential. (zeppieri2025isolatedandsyndromic pages 13-14, lee2024hereditaryopticneuropathies pages 4-5)

## 13. Prevention

**Primary prevention in carriers:** do not smoke; avoid heavy alcohol and recreational/occupational mitochondrial toxins; maintain adequate nutrition; screen and treat B12 deficiency; review potentially optic-toxic drugs; and educate carriers about urgent assessment for new color or central-vision changes. No vaccine or proven prophylactic medicine applies.

**Secondary prevention:** cascade genetic testing, baseline neuro-ophthalmic assessment, rapid OCT/genetic confirmation after first-eye symptoms, and early idebenone where locally indicated. Routine population screening is not justified by current evidence.

**Tertiary prevention:** protect residual vision, avoid further mitochondrial insults, treat systemic LHON-plus disease, provide low-vision and psychological rehabilitation, and monitor the fellow eye during the high-risk interval.

Genetic counseling must explain maternal transmission, incomplete penetrance, inability to predict precisely who will convert, and different autosomal-recessive risks. Reproductive options include prenatal testing and preimplantation genetic testing; mitochondrial donation/replacement is jurisdiction-dependent and raises regulatory and ethical issues.

## 14. Other species and natural disease

No well-established, naturally occurring companion-animal or livestock disease is accepted as a direct LHON ortholog, and LHON has no zoonotic potential. Complex-I genes and RGC bioenergetics are deeply conserved, but veterinary optic neuropathies should not automatically be labeled LHON. Accordingly, no reliable VBO breed association or nonhuman natural-disease prevalence can be assigned from current evidence.

Nonhuman primates have been used to study AAV2 vector trafficking: vector transfer toward the contralateral optic pathway offers a mechanistic explanation for bilateral improvement after unilateral treatment. This is an induced experimental observation, not natural disease. (lee2024hereditaryopticneuropathies pages 4-5)

## 15. Model organisms and experimental systems

**Cybrids and fibroblasts:** Patient mtDNA can be placed in a standardized nuclear background to isolate mitochondrial effects. Cybrids reproduce complex-I/ROS phenotypes but are often non-neuronal and cannot model tissue architecture or sex/environmental penetrance.

**Patient-derived iPSC-RGCs:** These preserve patient nuclear and mitochondrial backgrounds. LHON-RGCs show abnormal morphology, reduced mitochondrial function/transport, altered signaling, and increased death. In a mitochondrial-replacement model, replacing mutant mtDNA generated isogenic corrected cells and rescued the increased RGC-death phenotype. These models support causality and are useful for drug screening, but differentiation variability and immature cellular state remain limitations.

**Retinal organoids:** Three-dimensional systems improve cell–cell context and can model RGC/axon loss, mitochondrial membrane-potential and ATP defects, and mitophagy. They still lack a mature vascularized optic nerve and long-range brain connections.

**Rodent models:** Induced complex-I-deficient and allotopic ND4-expression models reproduce selected RGC loss or treatment biology. No mouse fully captures human incomplete penetrance, maternal pedigree, papillomacular-bundle anatomy, and sequential bilateral onset. Ndufs4 models are broader complex-I disease models rather than exact classical LHON.

**Applications:** mechanism dissection, modifier validation, AAV biodistribution/safety, idebenone and antioxidant testing, CRISPR/mitochondrial-editing feasibility, and biomarker development. Robust translational conclusions require convergence across human cohorts, isogenic cells, organoids, and in-vivo systems.

## Recent developments and expert assessment

1. **Recognition of nuclear arLHON (2023):** DNAJC30 and additional nuclear genes require a diagnostic pathway beyond the three primary mtDNA variants, particularly in Eastern European cases. This is a major shift from the historical “exclusively maternal” model. (zeppieri2025isolatedandsyndromic pages 2-4, lee2024hereditaryopticneuropathies pages 1-2)
2. **Improved diagnostic guidance (2024):** experts emphasize early OCT recognition and immediate targeted mtDNA testing to avoid misdiagnosis as optic neuritis, followed by full mtDNA sequencing and nuclear testing when necessary. (morgia2024recognizingleber’shereditary pages 1-2)
3. **Population ascertainment (2024):** the Madrid capture–recapture study showed that routine administrative sources undercount LHON and have poor positive predictive value without clinician validation. This argues for specialist-confirmed rare-disease registries.
4. **Pharmacogenetic refinement (2024):** NQO1 expression variants may explain some idebenone nonresponse, but prospective validation is required before genotype-guided therapy. (lee2024hereditaryopticneuropathies pages 4-5)
5. **Gene-therapy interpretation:** long-term improvement is encouraging, but contralateral-eye improvement after unilateral injection means that the fellow eye is not a true independent placebo. Authoritative reviews therefore regard allotopic therapy as promising but not yet definitive routine treatment. (lee2024hereditaryopticneuropathies pages 4-5, NCT02652767 chunk 1, NCT03406104 chunk 1)

## Key source links and publication dates

* Esmaeil A, Ali A, Behbehani R. *Frontiers in Ophthalmology*, January 2023. DOI: https://doi.org/10.3389/fopht.2022.1077395. The abstract summarizes LHON as respiratory-chain dysfunction that “eventually leads to apoptosis of retinal ganglion cells.” (esmaeil2023leber’shereditaryoptic pages 1-2)
* Lenaers G et al. *Brain*, April 2023. DOI: https://doi.org/10.1093/brain/awad131. Abstract: “The discovery of arLHON cases breaks with the dogma of exclusive maternal inheritance.” (zeppieri2025isolatedandsyndromic pages 2-4)
* Layrolle P et al. *Biomedicines*, March 2024. DOI: https://doi.org/10.3390/biomedicines12030584. Abstract: “Environmental factors are critical in LHON triggering or severity.” (layrolle2024theopticnerve pages 1-2)
* Lee SK et al. *Journal of Clinical & Translational Ophthalmology*, June 2024. DOI: https://doi.org/10.3390/jcto2030006. (lee2024hereditaryopticneuropathies pages 2-4, lee2024hereditaryopticneuropathies pages 4-5)
* La Morgia C et al. *Frontiers in Neurology*, September 2024. DOI: https://doi.org/10.3389/fneur.2024.1466275. Abstract: “Given the availability of a specific treatment for LHON, its early diagnosis is imperative.” (morgia2024recognizingleber’shereditary pages 1-2)
* Open Targets disease–target evidence, accessed through MONDO:0010788. (OpenTargets Search: Leber hereditary optic neuropathy)

## Evidence gaps and curation cautions

Incidence is poorly quantified; prevalence varies with ascertainment and founder effects. Exact phenotype frequencies outside the core ocular syndrome are uncertain. No validated epigenetic or circulating biomarker predicts conversion. Environmental associations beyond smoking/heavy alcohol are mostly observational. Idebenone evidence combines randomized, follow-up, real-world, and externally controlled data with different recovery definitions. Gene-therapy efficacy remains difficult to isolate from natural recovery and bilateral vector effects. Ontology identifiers marked “verify” in the embedded table should be checked against current HPO, GO, CL, UBERON, CHEBI, NCIt, ICD-11, and Orphanet releases before database ingestion.

References

1. (zeppieri2025isolatedandsyndromic pages 2-4): Marco Zeppieri, Caterina Gagliano, Marco Di Maita, Alessandro Avitabile, Giuseppe Gagliano, Edoardo Dammino, Daniele Tognetto, Maria Francesca Cordeiro, and Fabiana D’Esposito. Isolated and syndromic genetic optic neuropathies: a review of genetic and phenotypic heterogeneity. International Journal of Molecular Sciences, 26:3892, Apr 2025. URL: https://doi.org/10.3390/ijms26083892, doi:10.3390/ijms26083892. This article has 5 citations.

2. (morgia2024recognizingleber’shereditary pages 1-2): Chiara La Morgia, Maria Lucia Cascavilla, Anna Maria De Negri, Marcello Romano, Fabrizio Canalini, Silvia Rossi, Diego Centonze, and Massimo Filippi. Recognizing leber’s hereditary optic neuropathy to avoid delayed diagnosis and misdiagnosis. Frontiers in Neurology, Sep 2024. URL: https://doi.org/10.3389/fneur.2024.1466275, doi:10.3389/fneur.2024.1466275. This article has 14 citations and is from a peer-reviewed journal.

3. (lee2024hereditaryopticneuropathies pages 1-2): Samuel K. Lee, Caroline Mura, Nicolas J. Abreu, Janet C. Rucker, Steven L. Galetta, Laura J. Balcer, and Scott N. Grossman. Hereditary optic neuropathies: an updated review. Journal of Clinical &amp; Translational Ophthalmology, 2:64-78, Jun 2024. URL: https://doi.org/10.3390/jcto2030006, doi:10.3390/jcto2030006. This article has 5 citations.

4. (layrolle2024theopticnerve pages 2-4): Pierre Layrolle, Christophe Orssaud, Maryse Leleu, Pierre Payoux, and Stéphane Chavanas. The optic nerve at stake: update on environmental factors modulating expression of leber’s hereditary optic neuropathy. Biomedicines, 12:584, Mar 2024. URL: https://doi.org/10.3390/biomedicines12030584, doi:10.3390/biomedicines12030584. This article has 10 citations.

5. (esmaeil2023leber’shereditaryoptic pages 1-2): Ali Esmaeil, Ali Ali, and Raed Behbehani. Leber’s hereditary optic neuropathy: update on current diagnosis and treatment. Frontiers in Ophthalmology, Jan 2023. URL: https://doi.org/10.3389/fopht.2022.1077395, doi:10.3389/fopht.2022.1077395. This article has 34 citations.

6. (layrolle2024theopticnerve pages 1-2): Pierre Layrolle, Christophe Orssaud, Maryse Leleu, Pierre Payoux, and Stéphane Chavanas. The optic nerve at stake: update on environmental factors modulating expression of leber’s hereditary optic neuropathy. Biomedicines, 12:584, Mar 2024. URL: https://doi.org/10.3390/biomedicines12030584, doi:10.3390/biomedicines12030584. This article has 10 citations.

7. (lee2024hereditaryopticneuropathies pages 2-4): Samuel K. Lee, Caroline Mura, Nicolas J. Abreu, Janet C. Rucker, Steven L. Galetta, Laura J. Balcer, and Scott N. Grossman. Hereditary optic neuropathies: an updated review. Journal of Clinical &amp; Translational Ophthalmology, 2:64-78, Jun 2024. URL: https://doi.org/10.3390/jcto2030006, doi:10.3390/jcto2030006. This article has 5 citations.

8. (lee2024hereditaryopticneuropathies pages 4-5): Samuel K. Lee, Caroline Mura, Nicolas J. Abreu, Janet C. Rucker, Steven L. Galetta, Laura J. Balcer, and Scott N. Grossman. Hereditary optic neuropathies: an updated review. Journal of Clinical &amp; Translational Ophthalmology, 2:64-78, Jun 2024. URL: https://doi.org/10.3390/jcto2030006, doi:10.3390/jcto2030006. This article has 5 citations.

9. (NCT02652767 chunk 1):  Efficacy Study of GS010 for the Treatment of Vision Loss up to 6 Months From Onset in LHON Due to the ND4 Mutation. GenSight Biologics. 2016. ClinicalTrials.gov Identifier: NCT02652767

10. (NCT03406104 chunk 1):  RESCUE and REVERSE Long-term Follow-up. GenSight Biologics. 2018. ClinicalTrials.gov Identifier: NCT03406104

11. (NCT03293524 chunk 1):  Efficacy & Safety Study of Bilateral IVT Injection of GS010 in LHON Subjects Due to the ND4 Mutation for up to 1 Year. GenSight Biologics. 2018. ClinicalTrials.gov Identifier: NCT03293524

12. (OpenTargets Search: Leber hereditary optic neuropathy): Open Targets Query (Leber hereditary optic neuropathy, 24 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

13. (NCT01892943 chunk 1):  Leber Hereditary Optic Neuropathy (LHON) Historical Case Record Survey. Santhera Pharmaceuticals. 2013. ClinicalTrials.gov Identifier: NCT01892943

14. (iorga2025evaluationofvisual pages 1-2): Raluca Eugenia Iorga, Andreea Dana Moraru, Răzvana Sorina Munteanu-Dănulescu, Delia Urdea, and Ciprian Danielescu. Evaluation of visual and optical coherence tomography outcomes in patients with leber’s hereditary optic neuropathy treated with idebenone. Life, 15:1172, Jul 2025. URL: https://doi.org/10.3390/life15081172, doi:10.3390/life15081172. This article has 1 citations.

15. (NCT02652767 chunk 2):  Efficacy Study of GS010 for the Treatment of Vision Loss up to 6 Months From Onset in LHON Due to the ND4 Mutation. GenSight Biologics. 2016. ClinicalTrials.gov Identifier: NCT02652767

16. (catarino2017useofidebenone pages 5-6): Claudia B. Catarino and Thomas Klopstock. Use of idebenone for the treatment of leber’s hereditary optic neuropathy: review of the evidence. ArXiv, 5:232640981773111, Sep 2017. URL: https://doi.org/10.1177/2326409817731112, doi:10.1177/2326409817731112. This article has 10 citations.

17. (zeppieri2025isolatedandsyndromic pages 13-14): Marco Zeppieri, Caterina Gagliano, Marco Di Maita, Alessandro Avitabile, Giuseppe Gagliano, Edoardo Dammino, Daniele Tognetto, Maria Francesca Cordeiro, and Fabiana D’Esposito. Isolated and syndromic genetic optic neuropathies: a review of genetic and phenotypic heterogeneity. International Journal of Molecular Sciences, 26:3892, Apr 2025. URL: https://doi.org/10.3390/ijms26083892, doi:10.3390/ijms26083892. This article has 5 citations.

## Artifacts

- [Edison artifact artifact-00](Leber_Hereditary_Optic_Neuropathy-deep-research-falcon_artifacts/artifact-00.md)