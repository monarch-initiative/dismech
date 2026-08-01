---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-01T05:03:13.498758'
end_time: '2026-08-01T05:12:02.397096'
duration_seconds: 528.9
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Porokeratosis
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 10
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Porokeratosis-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Porokeratosis
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Porokeratosis** covering all of the
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
- **Disease Name:** Porokeratosis
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Porokeratosis** covering all of the
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


# Porokeratosis: comprehensive disease-characteristics report

## Executive summary

Porokeratosis is a heterogeneous group of inherited or acquired epidermal keratinization disorders. Its defining clinicopathologic feature is an expanding clone of abnormal keratinocytes that produces a raised keratotic border and, histologically, a **cornoid lamella**. The principal modern disease model is loss of mevalonate/isoprenoid-pathway function—most firmly involving **MVK, PMVK, MVD, and FDPS**—combined in many lesions with a somatic “second hit,” ultraviolet (UV) exposure, immunosuppression, or another local trigger. Disease is usually cutaneous and chronic rather than life-limiting, but it carries a clinically important risk of keratinocyte carcinoma, especially squamous-cell carcinoma (SCC). A 2023 review estimated overall keratinocyte-cancer risk at approximately 6.8–11.6%, with substantial variation by subtype. (pietkiewicz2023porokeratoses—acomprehensivereview pages 36-37, pietkiewicz2023porokeratoses—acomprehensivereview pages 5-7, vargasmora2020porokeratosisareview pages 1-2, pietkiewicz2023porokeratoses—acomprehensivereview pages 41-43)

The most important recent therapeutic development is pathway-directed topical statin therapy. A completed 31-person randomized trial, **NCT04359823**, compared 2% lovastatin/2% cholesterol with 2% lovastatin alone for 12 weeks; its peer-reviewed report appeared in *JAMA Dermatology* in 2023 (PMID **36947042**). Evidence remains limited, however, and no treatment is uniformly curative. (NCT04359823 chunk 1, NCT04359823 chunk 2, pietkiewicz2023porokeratoses—acomprehensivereview pages 46-47)

The following structured table is suitable for knowledge-base ingestion.

| domain | entity/finding | evidence-ready interpretation | suggested ontology IDs/terms |
|---|---|---|---|
| disease identifier | Porokeratosis | Heterogeneous group of keratinization disorders defined histologically by the cornoid lamella; evidence is aggregated from disease-level reviews plus primary variant-specific studies (vargasmora2020porokeratosisareview pages 1-2, vargasmora2020porokeratosisareview pages 2-4, pietkiewicz2023porokeratoses—acomprehensivereview pages 2-5) | MONDO: verify exact class; MeSH: Porokeratosis; ICD-10: verify specific coding used locally |
| synonym/nomenclature | Porokeratoses | Preferred umbrella term when referring to the disease spectrum rather than a single clinicopathologic variant (vargasmora2020porokeratosisareview pages 1-2, pietkiewicz2023porokeratoses—acomprehensivereview pages 5-7) | MeSH term mapping to Porokeratosis; disease synonym: porokeratoses |
| variant | Disseminated superficial actinic porokeratosis (DSAP) | Most common clinical variant in reviewed series; multiple small annular atrophic/keratotic macules-papules on sun-exposed skin, often adult onset, female-predominant in reviews (pietkiewicz2023porokeratoses—acomprehensivereview pages 2-5, vargasmora2020porokeratosisareview pages 4-5, vargasmora2020porokeratosisareview pages 2-4) | HPO: Actinic keratosis-like lesion; Abnormality of the skin; Multiple skin lesions; UBERON: skin of upper limb, skin of lower limb |
| variant | Disseminated superficial porokeratosis (DSP) | Disseminated non-actinic form, often childhood onset, involving sun-exposed and non-exposed areas (vargasmora2020porokeratosisareview pages 4-5, vargasmora2020porokeratosisareview pages 2-4) | HPO: Generalized skin lesions; Childhood onset; UBERON: trunk skin |
| variant | Porokeratosis of Mibelli (PM) | Often begins in childhood; enlarging annular plaques with raised keratotic border, commonly limbs/trunk; higher malignant potential than DSAP (pietkiewicz2023porokeratoses—acomprehensivereview pages 16-19, vargasmora2020porokeratosisareview pages 4-5, vargasmora2020porokeratosisareview pages 2-4) | HPO: Plaque; Hyperkeratotic papule; Childhood onset; UBERON: limb skin |
| variant | Linear porokeratosis (LP) | Usually congenital/early onset, linear or Blaschkoid distribution; among the highest malignant-transformation risks in reviews (pietkiewicz2023porokeratoses—acomprehensivereview pages 37-39, vargasmora2020porokeratosisareview pages 4-5, pietkiewicz2023porokeratoses—acomprehensivereview pages 52-54) | HPO: Linear skin lesion; Blaschkoid distribution; Congenital onset |
| variant | Verrucous porokeratosis / porokeratosis ptychotropica | Pruritic or burning verrucous plaques, often anogenital/intertriginous, diagnostically difficult, prolonged course (pietkiewicz2023porokeratoses—acomprehensivereview pages 29-31, pietkiewicz2023porokeratoses—acomprehensivereview pages 31-33) | HPO: Pruritus; Burning sensation; Verrucous lesion; UBERON: perianal skin, genital skin |
| variant | Punctate palmoplantar porokeratosis / PPPD spectrum | Punctate keratotic lesions of palms/soles; low but non-zero premalignant concern in reviews (pietkiewicz2023porokeratoses—acomprehensivereview pages 37-39, pietkiewicz2023porokeratoses—acomprehensivereview pages 52-54) | HPO: Palmoplantar hyperkeratosis; Punctate keratosis; UBERON: skin of palm, skin of sole |
| variant | Porokeratoma | Solitary well-demarcated porokeratotic plaque/nodule, usually sporadic; PMVK implicated in a minority of studied index cases (pietkiewicz2023porokeratoses—acomprehensivereview pages 34-36) | HPO: Solitary skin nodule; Hyperkeratotic plaque |
| gene | MVK | Core causal gene in porokeratosis spectrum; mevalonate-pathway enzyme; AD inheritance with incomplete penetrance in familial disease; implicated strongly in DSAP and other variants (pietkiewicz2023porokeratoses—acomprehensivereview pages 5-7, pietkiewicz2023porokeratoses—acomprehensivereview pages 43-44, aersilan2022microrna874targetsphosphomevalonate pages 17-17) | HGNC: MVK; GO: mevalonate pathway, cholesterol biosynthetic process |
| gene | PMVK | Core causal gene; loss-of-function variants reported in AD porokeratosis; also found in sporadic porokeratoma subset (pietkiewicz2023porokeratoses—acomprehensivereview pages 46-47, pietkiewicz2023porokeratoses—acomprehensivereview pages 43-44, pietkiewicz2023porokeratoses—acomprehensivereview pages 34-36) | HGNC: PMVK; GO: phosphomevalonate kinase activity, isoprenoid biosynthetic process |
| gene | MVD | Core causal gene in porokeratosis; part of mevalonate/isoprenoid biosynthesis and implicated in second-hit models (pietkiewicz2023porokeratoses—acomprehensivereview pages 43-44, pietkiewicz2023porokeratoses—acomprehensivereview pages 41-43) | HGNC: MVD; GO: diphosphomevalonate decarboxylase activity |
| gene | FDPS | Core causal gene in porokeratosis reviews; supports mevalonate-pathway disease model (pietkiewicz2023porokeratoses—acomprehensivereview pages 5-7) | HGNC: FDPS; GO: farnesyl diphosphate biosynthetic process |
| gene, emerging | FDFT1 | Emerging 2024 mechanism: gene-specific somatic epigenetic mosaicism reported for a non-hereditary localized form; important but should be labeled emerging until independently consolidated across cohorts (pietkiewicz2023porokeratoses—acomprehensivereview pages 5-7) | HGNC: FDFT1; label as emerging/candidate mechanistic gene |
| gene, candidate/emerging | SLC17A9 | Candidate/legacy DSAP-associated gene/locus in some pedigrees; not part of the canonical mevalonate-pathway core and should be labeled candidate/emerging (pietkiewicz2023porokeratoses—acomprehensivereview pages 43-44, vargasmora2020porokeratosisareview pages 1-2) | HGNC: SLC17A9; label as candidate susceptibility/causal gene pending broader consensus |
| inheritance | Autosomal dominant with incomplete penetrance | Best-supported familial inheritance pattern across common inherited forms; one review cites ~22% penetrance for DSAP (pietkiewicz2023porokeratoses—acomprehensivereview pages 5-7, vargasmora2020porokeratosisareview pages 1-2, vargasmora2020porokeratosisareview pages 2-4) | HP: Autosomal dominant inheritance; HP: Reduced penetrance |
| molecular mechanism | Mevalonate/isoprenoid pathway dysfunction | Unifying current model: deficiency of enzymes in cholesterol/isoprenoid biosynthesis perturbs keratinocyte differentiation, apoptosis control, and local epidermal homeostasis (pietkiewicz2023porokeratoses—acomprehensivereview pages 5-7, aersilan2022microrna874targetsphosphomevalonate pages 17-17) | GO: cholesterol biosynthetic process; isoprenoid biosynthetic process; regulation of keratinocyte differentiation |
| molecular mechanism | Second-hit / mosaic clonal expansion | Localized lesions can reflect postzygotic or somatic second-hit events driving clonal lesional epidermis over a germline background (pietkiewicz2023porokeratoses—acomprehensivereview pages 41-43, vargasmora2020porokeratosisareview pages 1-2) | GO: somatic mutation; clonal cell proliferation |
| molecular mechanism | Premature keratinocyte apoptosis beneath cornoid lamella | Classic downstream histopathologic process with granular layer loss and abnormal terminal differentiation (vargasmora2020porokeratosisareview pages 2-4, pietkiewicz2023porokeratoses—acomprehensivereview pages 41-43) | GO: apoptotic process; keratinocyte differentiation; epidermis development |
| cell/anatomy | Keratinocyte | Principal implicated cell type in pathogenesis and malignant transformation models (vargasmora2020porokeratosisareview pages 1-2, vargasmora2020porokeratosisareview pages 2-4, pietkiewicz2023porokeratoses—acomprehensivereview pages 41-43) | CL: keratinocyte |
| cell/anatomy | Epidermis / spinous-granular layers | Primary tissue compartment showing cornoid lamella, granular layer attenuation, dyskeratosis, and abnormal keratinization (pietkiewicz2023porokeratoses—acomprehensivereview pages 16-19, pietkiewicz2023porokeratoses—acomprehensivereview pages 31-33, vargasmora2020porokeratosisareview pages 2-4) | UBERON: epidermis; GO CC: cornified envelope |
| phenotype | Annular keratotic plaque/papule with raised rim | Core clinical morphology across variants (pietkiewicz2023porokeratoses—acomprehensivereview pages 2-5, vargasmora2020porokeratosisareview pages 4-5, vargasmora2020porokeratosisareview pages 2-4) | HPO: Annular skin lesion; Hyperkeratotic papule; Plaque |
| phenotype | Atrophic center | Common central lesional feature, especially in DSAP and PM-type lesions (pietkiewicz2023porokeratoses—acomprehensivereview pages 2-5, pietkiewicz2023porokeratoses—acomprehensivereview pages 34-36) | HPO: Cutaneous atrophy |
| phenotype | Pruritus | Common but variable symptom; up to one-third in DSAP review data and prominent in ptychotropic/verrucous forms (vargasmora2020porokeratosisareview pages 4-5, pietkiewicz2023porokeratoses—acomprehensivereview pages 29-31) | HPO: Pruritus |
| phenotype | Burning sensation | Reported particularly in verrucous/ptychotropic disease (pietkiewicz2023porokeratoses—acomprehensivereview pages 29-31) | HPO: Burning sensation |
| phenotype | Symmetric photo-distributed lesions | Characteristic DSAP distribution on extensor extremities and back/shoulders (pietkiewicz2023porokeratoses—acomprehensivereview pages 2-5, vargasmora2020porokeratosisareview pages 4-5, vargasmora2020porokeratosisareview pages 2-4) | HPO: Photosensitivity-related skin finding; UBERON: skin of upper limb, skin of lower limb, back skin |
| diagnostic hallmark | Cornoid lamella | Histopathologic hallmark and defining diagnostic feature of porokeratosis spectrum (pietkiewicz2023porokeratoses—acomprehensivereview pages 2-5, vargasmora2020porokeratosisareview pages 1-2, vargasmora2020porokeratosisareview pages 2-4) | SNOMED/pathology concept: cornoid lamella; GO/UBERON not directly applicable |
| diagnostic method | Dermoscopy | Often shows a peripheral keratotic rim corresponding to the cornoid lamella; helpful for clinical diagnosis and monitoring suspicious change (pietkiewicz2023porokeratoses—acomprehensivereview pages 2-5, pietkiewicz2023porokeratoses—acomprehensivereview pages 16-19, pietkiewicz2023porokeratoses—acomprehensivereview pages 41-43) | NCIT: Dermoscopy |
| trigger/risk factor | Ultraviolet radiation / sun exposure | Major trigger and exacerbating factor, especially for DSAP; seasonal worsening and predilection for sun-exposed sites support gene-environment interaction (pietkiewicz2023porokeratoses—acomprehensivereview pages 2-5, vargasmora2020porokeratosisareview pages 1-2, vargasmora2020porokeratosisareview pages 2-4) | CHEBI/Exposome: ultraviolet radiation exposure |
| trigger/risk factor | Immunosuppression | Important acquired trigger/risk state, including organ transplantation and immunosuppressive therapy (pietkiewicz2023porokeratoses—acomprehensivereview pages 37-39, vargasmora2020porokeratosisareview pages 2-4, pietkiewicz2023porokeratoses—acomprehensivereview pages 16-19) | NCIT: Immunosuppression |
| trigger/risk factor | Mechanical trauma / friction / scratching | Reported aggravating factors, especially in intertriginous/verrucous forms (pietkiewicz2023porokeratoses—acomprehensivereview pages 29-31, pietkiewicz2023porokeratoses—acomprehensivereview pages 37-39, vargasmora2020porokeratosisareview pages 2-4) | Exposome term: skin trauma; friction exposure |
| trigger/risk factor | Medication-associated porokeratosis | Reported with several drugs in review literature; evidence is largely case-based (vargasmora2020porokeratosisareview pages 2-4) | NCIT: Drug exposure |
| trigger/risk factor | Infection-associated cases | Case-level associations reported for HPV, HSV, HCV, leishmania; causality uncertain (vargasmora2020porokeratosisareview pages 2-4) | NCBI Taxonomy terms as appropriate; label as reported trigger association |
| cancer complication | Keratinocyte carcinoma, especially squamous cell carcinoma | Main serious complication; overall malignant transformation estimated about 6.8-11.6% in one review, with higher risk in LP and PM than DSAP (pietkiewicz2023porokeratoses—acomprehensivereview pages 36-37, pietkiewicz2023porokeratoses—acomprehensivereview pages 37-39, vargasmora2020porokeratosisareview pages 2-4) | NCIT: Squamous Cell Carcinoma of the Skin; Basal Cell Carcinoma |
| prognostic factor | Large, long-standing, non-sun-exposed or acral lesions; older age; prior irradiation; immunosuppression | Factors associated with increased malignant risk in reviews (pietkiewicz2023porokeratoses—acomprehensivereview pages 36-37, vargasmora2020porokeratosisareview pages 2-4) | NCIT: Risk factor |
| intervention | Topical lovastatin plus cholesterol | Pathogenesis-directed therapy based on mevalonate-pathway defect; studied prospectively in DSAP and now a principal modern intervention of interest (pietkiewicz2023porokeratoses—acomprehensivereview pages 46-47, NCT04359823 chunk 1, NCT04359823 chunk 2) | NCIT: Lovastatin; CHEBI: cholesterol; NCIT: Topical Cream Dosage Form |
| intervention | Topical lovastatin monotherapy | Randomized DSAP trial suggests benefit may not require added cholesterol in all patients, though comparative evidence is still limited (NCT04359823 chunk 2, pietkiewicz2023porokeratoses—acomprehensivereview pages 46-47) | NCIT: Lovastatin |
| intervention | Surgical excision / shave-curettage | Best suited to localized lesions and suspicious or transformed lesions; several case-based reports show good local control (pietkiewicz2023porokeratoses—acomprehensivereview pages 36-37, vargasmora2020porokeratosisareview pages 12-13) | NCIT: Surgical Excision; Curettage |
| intervention | Cryotherapy | Common local destructive therapy with variable efficacy and recurrence risk (pietkiewicz2023porokeratoses—acomprehensivereview pages 31-33, vargasmora2020porokeratosisareview pages 12-13) | NCIT: Cryotherapy |
| intervention | Topical 5-fluorouracil | Traditional topical option; some complete responses reported but evidence mainly case based (pietkiewicz2023porokeratoses—acomprehensivereview pages 36-37, vargasmora2020porokeratosisareview pages 12-13) | NCIT: Fluorouracil |
| intervention | Topical imiquimod | Used especially in PM and some localized variants; response inconsistent (pietkiewicz2023porokeratoses—acomprehensivereview pages 31-33, vargasmora2020porokeratosisareview pages 12-13) | NCIT: Imiquimod |
| intervention | Topical/systemic retinoids including acitretin | Frequently used for disseminated or hyperkeratotic disease; outcomes variable and relapse common (pietkiewicz2023porokeratoses—acomprehensivereview pages 36-37, vargasmora2020porokeratosisareview pages 12-13) | NCIT: Acitretin; Retinoid Therapy |
| intervention | Photodynamic therapy / laser-based treatments | Employed in DSAP and localized lesions with modest or variable response and procedure-related adverse effects (pietkiewicz2023porokeratoses—acomprehensivereview pages 46-47, vargasmora2020porokeratosisareview pages 12-13) | NCIT: Photodynamic Therapy; Carbon Dioxide Laser Therapy |
| prevention/surveillance | Sun protection and long-term skin cancer surveillance | Supported by the disease’s photo-triggering and premalignant potential; biopsy is recommended for suspicious change (pietkiewicz2023porokeratoses—acomprehensivereview pages 2-5, vargasmora2020porokeratosisareview pages 2-4, vargasmora2020porokeratosisareview pages 12-13) | NCIT: Sunscreen/Sun Protection Counseling; Skin Examination |
| evidence caveat | Population prevalence/incidence | Robust population-based incidence and prevalence are not well established in retrieved sources; avoid over-precise epidemiologic coding without registry confirmation (vargasmora2020porokeratosisareview pages 1-2, vargasmora2020porokeratosisareview pages 4-5) | annotation note: evidence gap |
| evidence caveat | Protective factors | No validated genetic protective factors were identified in the retrieved evidence base (pietkiewicz2023porokeratoses—acomprehensivereview pages 5-7, vargasmora2020porokeratosisareview pages 1-2) | annotation note: none established |
| evidence caveat | Model organisms / other species | No disease-faithful animal model or robust natural veterinary counterpart was validated in the retrieved materials; current evidence is mainly human clinical/lesional tissue based (pietkiewicz2023porokeratoses—acomprehensivereview pages 41-43, vargasmora2020porokeratosisareview pages 1-2) | annotation note: evidence gap |


*Table: This table summarizes ontology-ready disease, gene, phenotype, mechanism, trigger, complication, and intervention annotations for porokeratosis. It is designed to support knowledge-base population while clearly labeling candidate or emerging findings and evidence gaps.*

## 1. Disease information

### Definition and terminology

Porokeratosis is an umbrella diagnosis encompassing multiple clinical variants of an epidermal keratinization disorder. Typical lesions are annular papules or plaques with an atrophic center and sharply raised, ridge-like peripheral scale. The histologic cornoid lamella is a column of parakeratotic cells overlying reduced or absent granular layer and abnormal underlying keratinocytes. The term **porokeratoses** appropriately emphasizes that this is a spectrum rather than one uniform phenotype. (pietkiewicz2023porokeratoses—acomprehensivereview pages 2-5, vargasmora2020porokeratosisareview pages 1-2, vargasmora2020porokeratosisareview pages 2-4)

A directly relevant 2023 review abstract states: **“Porokeratosis is a heterogeneous group of keratinising disorders characterised by … the presence of the cornoid lamella.”** It further attributes this structure to a defective isoprenoid pathway critical to cholesterol synthesis. Publication: Pietkiewicz et al., *Metabolites*, 30 November 2023; DOI/URL: https://doi.org/10.3390/metabo13121176. (pietkiewicz2023porokeratoses—acomprehensivereview pages 2-5, pietkiewicz2023porokeratoses—acomprehensivereview pages 5-7)

### Identifiers

- **MONDO:** an exact umbrella-class MONDO identifier was not reliably established in the retrieved sources and should be verified directly against the current MONDO release before ingestion.
- **MeSH:** *Porokeratosis*.
- **ICD-10-CM:** **L56.5**, disseminated superficial actinic porokeratosis. Other forms may be coded under broader local skin-disorder categories; coding should remain subtype- and jurisdiction-specific.
- **OMIM phenotype entries commonly used:** disseminated superficial actinic porokeratosis (**175800**), porokeratosis of Mibelli (**175900**), and porokeratosis palmaris et plantaris disseminata (**175850**); these should be release-verified because porokeratosis is genetically heterogeneous.
- **Common synonyms:** porokeratoses; disseminated superficial actinic porokeratosis (DSAP); disseminated superficial porokeratosis (DSP); porokeratosis of Mibelli (PM); linear porokeratosis (LP); porokeratosis palmaris et plantaris disseminata (PPPD); punctate porokeratosis; verrucous porokeratosis; porokeratosis ptychotropica; follicular porokeratosis; porokeratoma.

Most information in this report is **aggregated disease-level evidence** from reviews, cohorts, pedigrees, and trials—not individual EHR data. Case reports and lesional sequencing studies constitute patient-level evidence where explicitly noted.

## 2. Etiology and risk or protective factors

### Causal and susceptibility factors

The strongest causal genes encode enzymes in the mevalonate/isoprenoid pathway:

- **MVK**—mevalonate kinase;
- **PMVK**—phosphomevalonate kinase;
- **MVD**—mevalonate diphosphate decarboxylase;
- **FDPS**—farnesyl diphosphate synthase.

Familial disease is usually autosomal dominant with incomplete and age-dependent penetrance. One synthesis reported approximately **22% penetrance for DSAP**, although this figure should not be generalized to every genotype or subtype. Historical linked regions include 12q24.1–24.2, 15q25.1–26.1, 1p31.3–p31.1, and 16q24.1–24.3. **SLC17A9**, **SSH1**, and **SART3** have been reported in older pedigree/candidate-gene literature, but their status is less secure than that of the four canonical pathway genes. (pietkiewicz2023porokeratoses—acomprehensivereview pages 43-44, pietkiewicz2023porokeratoses—acomprehensivereview pages 5-7, vargasmora2020porokeratosisareview pages 1-2)

Localized and linear lesions may result from postzygotic mosaicism or a second somatic event in epidermis. Human lesional studies have reported second hits or loss of heterozygosity involving mevalonate-pathway genes, including UV-signature C>T substitutions, supporting clonal expansion of biallelically impaired keratinocytes. (pietkiewicz2023porokeratoses—acomprehensivereview pages 41-43)

A major 2024 development was the report of **gene-specific somatic epigenetic mosaicism of FDFT1** in nonhereditary localized porokeratosis (Saito et al., *American Journal of Human Genetics*, May 2024; DOI: https://doi.org/10.1016/j.ajhg.2024.03.017). This expands the disease model from sequence-level defects to focal epigenetic silencing of another cholesterol-biosynthesis gene, but independent replication and estimates of population contribution are still needed.

### Environmental and acquired risk factors

- **UV radiation:** the clearest environmental interaction, especially in DSAP. Lesions favor sun-exposed extensor limbs, often worsen in summer, and may be induced or aggravated by phototherapy. MVK also participates in keratinocyte differentiation and protection from UVA-induced apoptosis, providing a plausible gene–environment link. (pietkiewicz2023porokeratoses—acomprehensivereview pages 2-5, pietkiewicz2023porokeratoses—acomprehensivereview pages 5-7, vargasmora2020porokeratosisareview pages 4-5)
- **Immunosuppression:** organ or bone-marrow transplantation, AIDS, hematologic disease, and immunosuppressive medication can precipitate or disseminate disease and increase malignant risk. An older review reported porokeratosis in approximately **10% of kidney-transplant recipients**, generally 4–14 years after transplantation, but this estimate requires contemporary registry validation. (pietkiewicz2023porokeratoses—acomprehensivereview pages 16-19, pietkiewicz2023porokeratoses—acomprehensivereview pages 37-39, vargasmora2020porokeratosisareview pages 2-4)
- **Trauma/friction:** scratching, clothing friction, and local injury can aggravate lesions, particularly intertriginous verrucous/ptychotropic disease. (pietkiewicz2023porokeratoses—acomprehensivereview pages 29-31, pietkiewicz2023porokeratoses—acomprehensivereview pages 37-39)
- **Medication-associated cases:** reports involve hydroxyurea, thiazide and loop diuretics, suramin, gentamicin, exemestane, selected biologics, trastuzumab, and antibiotics. Evidence is mostly case-based and does not establish comparable causal risk across drugs. (vargasmora2020porokeratosisareview pages 2-4)
- **Infections:** HPV, HSV, HCV, and leishmaniasis have been reported in association with lesions, but none is established as a necessary infectious cause. Porokeratosis is neither contagious nor known to be zoonotic. (vargasmora2020porokeratosisareview pages 2-4)

No reproducible protective allele, diet, supplement, smoking/alcohol effect, or exercise association has been established. Practical environmental protection consists principally of reducing UV exposure and avoiding lesion trauma.

## 3. Phenotypes

### Major clinicopathologic variants

- **DSAP:** multiple pink-to-brown annular macules/papules, usually under 1 cm, symmetrically affecting sun-exposed arms and legs. Sporadic onset is commonly in the third–fifth decades; familial disease often appears in the third–fourth decades. It is usually asymptomatic, but pruritus occurs in up to one-third. Reviews describe female predominance, approximately **1.8:1**, and DSAP as 42–56% of clinical series. Suggested HPO concepts: annular skin lesion, multiple skin lesions, hyperkeratotic papule, cutaneous atrophy, pruritus, adult onset. (pietkiewicz2023porokeratoses—acomprehensivereview pages 2-5, vargasmora2020porokeratosisareview pages 4-5, vargasmora2020porokeratosisareview pages 2-4)
- **DSP:** disseminated lesions on both exposed and covered skin, often beginning at ages **5–10 years**. Suggested HPO: generalized skin lesions, childhood onset, hyperkeratosis. (vargasmora2020porokeratosisareview pages 4-5)
- **PM:** one or several slowly enlarging plaques, often beginning in childhood in hereditary disease and later in sporadic disease; limbs and trunk predominate, but palms, soles, scalp, face, mucosa, and genital skin can be involved. Suggested HPO: plaque, annular skin lesion, childhood onset, pruritus. (pietkiewicz2023porokeratoses—acomprehensivereview pages 16-19, vargasmora2020porokeratosisareview pages 4-5)
- **LP:** congenital or early-onset lesions following Blaschko lines; often unilateral or segmental and slowly progressive. Suggested HPO: linear skin lesion, Blaschkoid distribution, congenital onset. (pietkiewicz2023porokeratoses—acomprehensivereview pages 37-39, vargasmora2020porokeratosisareview pages 4-5)
- **PPPD/punctate disease:** punctate or disseminated palmoplantar keratotic lesions; nail dystrophy and pseudoainhum are uncommon complications. Suggested HPO: palmoplantar hyperkeratosis, punctate keratosis, nail dystrophy. (pietkiewicz2023porokeratoses—acomprehensivereview pages 37-39, pietkiewicz2023porokeratoses—acomprehensivereview pages 52-54)
- **Verrucous porokeratosis/ptychotropica:** intensely pruritic or burning verrucous plaques, usually genitogluteal, perianal, or intertriginous. Lesions may spread centrifugally for **5–10 years**. Male predominance and onset in the third–fifth decades are typical. Suggested HPO: verrucous lesion, pruritus, burning sensation. (pietkiewicz2023porokeratoses—acomprehensivereview pages 29-31, pietkiewicz2023porokeratoses—acomprehensivereview pages 31-33)
- **Follicular porokeratosis:** folliculocentric keratotic lesions with plugs; the genetic basis remains uncertain. (pietkiewicz2023porokeratoses—acomprehensivereview pages 34-36)
- **Porokeratoma:** usually a solitary plaque or nodule lacking the classic annular rim; pooled cases had a male:female ratio of **19:4** and mean onset of **55 years** (range 13–78). (pietkiewicz2023porokeratoses—acomprehensivereview pages 34-36)
- **Eruptive pruritic papular porokeratosis:** sudden inflammatory, itchy lesions; occasionally associated with malignancy or immunologic change and may regress when the associated disorder is treated. (pietkiewicz2023porokeratoses—acomprehensivereview pages 46-47, vargasmora2020porokeratosisareview pages 4-5)

### Quality of life

Formal EQ-5D/SF-36 data are sparse. Most burden derives from visible chronic lesions, pruritus, burning, treatment inconvenience, pigmentary change or scarring, and anxiety concerning malignancy. NCT04359823 therefore included the **Dermatology Life Quality Index**, appearance, color, size, pain, and itch as patient-centered outcomes. (NCT04359823 chunk 1, NCT04359823 chunk 2)

## 4. Genetic and molecular information

Pathogenic variants reported across the canonical genes include missense, nonsense, frameshift, splice-altering, and loss-of-function alleles. The aggregate mechanism is reduced enzymatic function rather than a well-established gain-of-function or dominant-negative effect. A 2016 study specifically identified loss-of-function **PMVK** variants causing autosomal-dominant disseminated superficial porokeratosis. **PMVK** variants were also detected in 5 of 134 index cases in one series containing porokeratoma, illustrating genetic heterogeneity rather than a universal subtype-specific mutation. (pietkiewicz2023porokeratoses—acomprehensivereview pages 46-47, pietkiewicz2023porokeratoses—acomprehensivereview pages 34-36)

Variant-level ACMG classification and allele frequencies must be assigned individually from the current ClinVar and gnomAD releases. It is unsafe to attach one classification or population frequency to a gene as a whole. Familial variants are germline; lesional second hits are somatic. Large recurrent chromosomal abnormalities, aneuploidy, repeat expansions, mitochondrial variants, and a routine role for karyotyping/FISH are not established. Chromosome 3p12–14 instability and lesional polyploidy have been described as tumor-associated findings, not as the usual inherited cause. (pietkiewicz2023porokeratoses—acomprehensivereview pages 37-39)

No clinically validated modifier gene or pharmacogenomic rule is available. The 2024 **FDFT1** finding is the principal disease-specific epigenetic development; broader methylome, histone, single-cell, spatial-transcriptomic, proteomic, and metabolomic signatures remain insufficiently validated for diagnosis.

## 5. Environmental information

The disease is best regarded as a genetic or mosaic keratinocyte disorder whose expression is modified by UV exposure, immune surveillance, trauma/friction, and selected medications. There is no established toxin, pollution, occupation, diet, alcohol, tobacco, or exercise exposure with quantified causal effect. Warm climate and friction may worsen ptychotropic disease, while UV exposure is particularly relevant to DSAP. Infectious associations are triggers or coincident findings, not transmissible causes. (pietkiewicz2023porokeratoses—acomprehensivereview pages 29-31, vargasmora2020porokeratosisareview pages 1-2, vargasmora2020porokeratosisareview pages 2-4)

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream defect:** germline or postzygotic impairment of MVK/PMVK/MVD/FDPS—or emerging focal FDFT1 epigenetic silencing—reduces normal mevalonate/isoprenoid-pathway flux.
2. **Metabolic consequences:** altered sterol/cholesterol synthesis and shortage of nonsterol isoprenoids disturb membrane biology and protein prenylation.
3. **Cellular dysfunction:** epidermal keratinocytes show abnormal differentiation, reduced granular layer, altered filaggrin/loricrin expression, dyskeratosis, and premature apoptosis.
4. **Clonal localization:** a somatic second hit, UV-induced mutation, or epigenetic event gives a local keratinocyte clone a distinctive lesional phenotype.
5. **Tissue manifestation:** centrifugally expanding abnormal epidermis creates the peripheral cornoid lamella and central atrophy.
6. **Downstream inflammation and cancer risk:** chronic injury, immune alteration, UV, and clonal genomic instability promote inflammatory symptoms and, in a minority, SCC/BCC or melanoma. (aersilan2022microrna874targetsphosphomevalonate pages 17-17, pietkiewicz2023porokeratoses—acomprehensivereview pages 5-7, vargasmora2020porokeratosisareview pages 2-4, pietkiewicz2023porokeratoses—acomprehensivereview pages 41-43)

Relevant GO suggestions include cholesterol biosynthetic process; isoprenoid biosynthetic process; protein prenylation; keratinocyte differentiation; epidermis development; cornification; apoptotic process; cell-cycle regulation; and response to UV. The principal Cell Ontology term is **keratinocyte**; follicular stem/progenitor keratinocytes may participate in follicular disease. Lesional studies report p53, p63, p16^INK4a, survivin, and hTERT abnormalities, but these are downstream markers of stress, senescence, or neoplastic potential rather than validated diagnostic biomarkers. (pietkiewicz2023porokeratoses—acomprehensivereview pages 37-39)

## 7. Anatomy

The primary organ is the **skin**, specifically epidermis and epidermal appendages. Relevant anatomical mappings are epidermis; skin of upper limb; skin of lower limb; trunk/back skin; facial/scalp skin; palm; sole; genital skin; and perianal skin. Mucosal and nail involvement is uncommon but documented. The affected cellular compartment extends from basal/spinous keratinocytes to the granular and cornified layers; the most conspicuous structure is the parakeratotic cornoid lamella. No consistent internal-organ disease is intrinsic to ordinary porokeratosis. (pietkiewicz2023porokeratoses—acomprehensivereview pages 16-19, pietkiewicz2023porokeratoses—acomprehensivereview pages 31-33, vargasmora2020porokeratosisareview pages 2-4)

## 8. Temporal development

Onset ranges from congenital LP to childhood PM/DSP and adult DSAP or ptychotropica. Most lesions emerge insidiously and expand slowly over years. Disease is generally chronic or lifelong, with variable activity and occasional inflammatory eruptions. Spontaneous durable remission is uncommon; recurrence after treatment is frequent. Malignant transformation may occur decades after onset—one review reports intervals as long as **36 years**—making long-term surveillance more important than short-term clearance alone. (pietkiewicz2023porokeratoses—acomprehensivereview pages 29-31, vargasmora2020porokeratosisareview pages 4-5, vargasmora2020porokeratosisareview pages 2-4)

## 9. Inheritance and population

The predominant familial pattern is **autosomal dominant with incomplete, variable, and age-dependent penetrance**. Expressivity is highly variable even within families. Segmental disease may reflect postzygotic mosaicism or type-2 segmental manifestation. Germline mosaicism, anticipation, founder effects, consanguinity effects, and carrier frequency are not well quantified. (pietkiewicz2023porokeratoses—acomprehensivereview pages 5-7, vargasmora2020porokeratosisareview pages 1-2, pietkiewicz2023porokeratoses—acomprehensivereview pages 41-43)

Robust population prevalence and incidence per 100,000 are unavailable. Porokeratosis is conventionally described as rare, although recent registry work suggests it may be among the more frequent genodermatoses. DSAP is enriched in fair-skinned populations living in high-UV settings; no exclusive ethnicity is affected. Sex ratios vary by subtype: DSAP and LP show female predominance in reviews, whereas PM, PPPD, ptychotropica, and porokeratoma tend toward male predominance. (pietkiewicz2023porokeratoses—acomprehensivereview pages 34-36, vargasmora2020porokeratosisareview pages 4-5, vargasmora2020porokeratosisareview pages 1-2)

## 10. Diagnostics

### Clinical and pathology workflow

1. Recognize the peripheral ridge or “Great Wall” morphology and subtype-specific distribution.
2. Perform dermoscopy: a sharply defined peripheral keratotic track corresponding to the cornoid lamella is characteristic. The furrow-ink test may accentuate the ridge.
3. Biopsy the **raised border**, not merely the atrophic center, when morphology is uncertain or malignancy is suspected.
4. Histology should identify a cornoid lamella, diminished/absent granular layer, dyskeratotic or vacuolated keratinocytes, and variable underlying inflammation. Multiple cornoid lamellae, papillomatosis, and psoriasiform hyperplasia favor verrucous disease. (pietkiewicz2023porokeratoses—acomprehensivereview pages 2-5, pietkiewicz2023porokeratoses—acomprehensivereview pages 16-19, pietkiewicz2023porokeratoses—acomprehensivereview pages 31-33)

Reflectance confocal microscopy, conventional or UV-fluorescence dermoscopy, and emerging line-field confocal optical coherence tomography can improve noninvasive discrimination, but histopathology remains necessary for suspicious transformation. Routine blood chemistry, imaging, electrophysiology, or circulating biomarkers are not diagnostic.

### Genetic testing

Testing is most useful in familial, early-onset, disseminated, linear/segmental, mixed, or atypical disease. A practical panel should include **MVK, PMVK, MVD, and FDPS**, with consideration of **FDFT1** and research-level candidate genes depending on phenotype and laboratory validation. Sequence plus copy-number analysis is preferable. WES/WGS may help panel-negative pedigrees and mosaic cases; paired lesional and blood sequencing can detect somatic second hits. Standard CMA, karyotype, FISH, mitochondrial testing, and repeat-expansion testing have low expected yield unless another syndrome is suspected. (pietkiewicz2023porokeratoses—acomprehensivereview pages 43-44, pietkiewicz2023porokeratoses—acomprehensivereview pages 5-7, pietkiewicz2023porokeratoses—acomprehensivereview pages 41-43)

### Differential diagnosis

Actinic keratosis, SCC in situ/invasive SCC, superficial BCC, psoriasis, tinea corporis, lichen planus, pityriasis, seborrheic keratosis, epidermal nevus, viral warts, cutaneous T-cell lymphoma, and inflammatory genital dermatoses should be considered. Rapid growth, ulceration, pain, bleeding, marked induration, or a new nodule warrants biopsy. (pietkiewicz2023porokeratoses—acomprehensivereview pages 34-36, pietkiewicz2023porokeratoses—acomprehensivereview pages 2-5, pietkiewicz2023porokeratoses—acomprehensivereview pages 16-19)

There is no population or newborn screening program. Cascade clinical examination and targeted familial-variant testing are reasonable after a molecular diagnosis.

## 11. Outcome and prognosis

Life expectancy is ordinarily normal, and disease-specific mortality statistics are unavailable. Morbidity is predominantly dermatologic, cosmetic, pruritic, and treatment-related. The major prognostic issue is malignancy. Reviews estimate overall keratinocyte-cancer transformation at approximately **6.8–11.6%** or **7.5–11%**. Subtype estimates include DSAP **3.4%**, PM **7.6–8%**, and LP **11–19%**; these figures derive from heterogeneous series and are vulnerable to referral and publication bias. SCC is the dominant tumor, followed by BCC; melanoma has also been reported. (pietkiewicz2023porokeratoses—acomprehensivereview pages 37-39, pietkiewicz2023porokeratoses—acomprehensivereview pages 36-37, vargasmora2020porokeratosisareview pages 4-5, vargasmora2020porokeratosisareview pages 2-4)

Higher-risk features include large, long-standing, linear, acral or non-sun-exposed lesions, older age, previous irradiation, and immunosuppression. Porokeratoma has no reported malignant transformation in the summarized literature, whereas linear disease carries the highest consistently cited risk. (pietkiewicz2023porokeratoses—acomprehensivereview pages 34-36, pietkiewicz2023porokeratoses—acomprehensivereview pages 36-37)

## 12. Treatment

No universally accepted guideline or curative algorithm exists. Choice depends on lesion number, site, thickness, symptoms, cosmetic burden, immunosuppression, and cancer suspicion.

### Pathway-directed topical statins

The strongest recent translational advance is topical statin therapy. By inhibiting upstream HMG-CoA reductase, topical lovastatin is intended to limit accumulation of potentially toxic intermediates; added cholesterol was intended to replace deficient end product. In **NCT04359823**, 31 adults were randomized and single-blinded to 2% lovastatin/2% cholesterol or 2% lovastatin alone, applied twice daily with occlusion for 12 weeks. Outcomes included DSAP-GASI, dermoscopic cornoid lamellae, lesion appearance/color/size, itch/pain, and DLQI. The study ran from 24 August 2020 through 23 April 2021. (NCT04359823 chunk 1, NCT04359823 chunk 2)

The publication is Santa Lucia et al., “Safety and Efficacy of Topical Lovastatin Plus Cholesterol Cream vs Topical Lovastatin Cream Alone…,” *JAMA Dermatology* 159, 488–495, published March 2023; PMID **36947042**; DOI: https://doi.org/10.1001/jamadermatol.2023.0205. Both regimens produced clinical improvement, and the trial did not establish that added cholesterol was necessary; small sample size, short follow-up, compounded formulations, and DSAP-only enrollment limit generalization. Earlier evidence included a 2021 split-body simvastatin/cholesterol study and a seven-person 2022 lovastatin/cholesterol series. (NCT04359823 chunk 2, pietkiewicz2023porokeratoses—acomprehensivereview pages 46-47)

Suggested NCIt mappings: Lovastatin; Cholesterol; Topical Drug Administration; Cream Dosage Form.

### Other therapies

- **Localized or suspicious lesions:** complete excision provides pathology and definitive local control; shave/curettage, electrosurgery, cryotherapy, and ablative laser are alternatives. Excision yielded no relapse in 10 of 12 summarized cases, although this is uncontrolled evidence. (pietkiewicz2023porokeratoses—acomprehensivereview pages 36-37, vargasmora2020porokeratosisareview pages 12-13)
- **Topical agents:** 5-fluorouracil, imiquimod, retinoids, vitamin-D analogues, diclofenac, and corticosteroids have variable efficacy. One 17-person DSAP study found 3% diclofenac over 3–6 months prevented progression in more than 50%, not necessarily complete clearance. (vargasmora2020porokeratosisareview pages 12-13)
- **Systemic retinoids:** acitretin may help extensive or hyperkeratotic disease but relapse and mucocutaneous/metabolic adverse effects limit long-term use. (pietkiewicz2023porokeratoses—acomprehensivereview pages 36-37)
- **Procedures:** photodynamic therapy produced approximately **31–35% response** in older studies but can be painful; CO₂, erbium, Q-switched ruby, and other lasers have inconsistent clearance and recurrence. (pietkiewicz2023porokeratoses—acomprehensivereview pages 46-47, vargasmora2020porokeratosisareview pages 12-13)
- **Ptychotropica:** particularly treatment-resistant. In summarized reports, topical corticosteroids largely supplied only transient antipruritic benefit; imiquimod was fully effective in 1, partly effective in 1, and ineffective in 8 cases. CO₂ laser and surgery can clear limited disease, but recurrence occurs. (pietkiewicz2023porokeratoses—acomprehensivereview pages 31-33)

There is no approved gene, cell, RNA, or immunotherapy and no established pharmacogenomic dosing rule. Treatment of SCC arising in porokeratosis follows skin-cancer standards.

## 13. Prevention

- **Primary:** rigorous sun protection—protective clothing, shade, and broad-spectrum sunscreen—especially in DSAP or genetically susceptible relatives; minimize unnecessary phototherapy and repeated lesion trauma.
- **Secondary:** regular self-examination and periodic clinician examination. Biopsy lesions showing rapid growth, nodularity, ulceration, bleeding, pain, or induration. Immunosuppressed patients and those with LP, large PM, or prior radiation merit closer review.
- **Tertiary:** treat symptomatic or repeatedly traumatized lesions, optimize immunosuppression when medically feasible, and excise confirmed malignant transformation.
- **Genetic counseling:** explain autosomal-dominant inheritance, incomplete penetrance, variable expression, and mosaic disease. If a familial pathogenic variant is known, cascade, prenatal, or preimplantation testing is technically possible, but proportionality should be considered because isolated porokeratosis is usually compatible with normal lifespan.

No vaccine, chemoprophylaxis, newborn screening, or validated preventive systemic medication exists. (pietkiewicz2023porokeratoses—acomprehensivereview pages 36-37, vargasmora2020porokeratosisareview pages 2-4, vargasmora2020porokeratosisareview pages 12-13)

## 14. Other species and natural disease

The retrieved evidence did not establish a well-characterized naturally occurring veterinary counterpart with a conserved causal genotype, breed association, or OMIA entry. Histologic cornoid-lamella-like lesions may be described in veterinary pathology, but they should not automatically be equated with human Mendelian porokeratosis. There is no zoonotic transmission. Orthologues of MVK, PMVK, MVD, FDPS, and FDFT1 are broadly conserved, supporting comparative biochemical studies, but not establishing homologous natural disease.

## 15. Model organisms and experimental systems

No disease-faithful mouse, rat, zebrafish, fly, or worm model emerged as a validated standard. Current mechanistic evidence rests mainly on:

- human pedigrees and germline sequencing;
- paired lesional/nonlesional skin sequencing for second hits;
- human histopathology and immunohistochemistry;
- cultured keratinocyte experiments addressing mevalonate flux, apoptosis, differentiation, and rescue by pathway metabolites.

A useful future model would conditionally reduce a pathway gene in sparse epidermal keratinocytes, permitting clonal mosaic expansion and controlled UV exposure. Global biallelic disruption may model severe systemic mevalonate disorders rather than cutaneous porokeratosis, which is an important limitation. Patient-derived keratinocyte organoids or reconstructed epidermis, CRISPR-corrected isogenic controls, single-cell RNA/ATAC sequencing, and spatial metabolomics are high-priority platforms but are not yet validated clinical tools.

## Evidence limitations and interpretation

The evidence base is dominated by case reports, small series, retrospective cohorts, and heterogeneous clinical definitions. Variant frequencies and cancer-risk percentages should therefore be stored with provenance and confidence metadata, not treated as universal population estimates. Exact abstract quotations were limited to retrieved source text; the principal quoted 2023 review is secondary evidence. Variant-specific pathogenicity, HGNC IDs, gnomAD frequencies, and MONDO/ontology numeric identifiers should be release-checked before production ingestion. The best-supported current conclusions are the cornoid-lamella phenotype, mevalonate-pathway genetic architecture, germline-plus-somatic/mosaic disease model, UV and immunosuppression interactions, malignant potential, and early clinical efficacy of topical lovastatin-based therapy.

References

1. (pietkiewicz2023porokeratoses—acomprehensivereview pages 36-37): P. Pietkiewicz, Katarzyna Korecka, Natalia Salwowska, Ihor Kohut, Adarsha Adhikari, M. Bowszyc‑Dmochowska, A. Pogorzelska-Antkowiak, and C. Navarrete-Dechent. Porokeratoses—a comprehensive review on the genetics and metabolomics, imaging methods and management of common clinical variants. Metabolites, Nov 2023. URL: https://doi.org/10.3390/metabo13121176, doi:10.3390/metabo13121176. This article has 42 citations.

2. (pietkiewicz2023porokeratoses—acomprehensivereview pages 5-7): P. Pietkiewicz, Katarzyna Korecka, Natalia Salwowska, Ihor Kohut, Adarsha Adhikari, M. Bowszyc‑Dmochowska, A. Pogorzelska-Antkowiak, and C. Navarrete-Dechent. Porokeratoses—a comprehensive review on the genetics and metabolomics, imaging methods and management of common clinical variants. Metabolites, Nov 2023. URL: https://doi.org/10.3390/metabo13121176, doi:10.3390/metabo13121176. This article has 42 citations.

3. (vargasmora2020porokeratosisareview pages 1-2): P. Vargas-Mora, D. Morgado-Carrasco, and X. Fustà-Novell. Porokeratosis: a review of its pathophysiology, clinical manifestations, diagnosis, and treatment. Sep 2020. URL: https://doi.org/10.1016/j.adengl.2020.08.005, doi:10.1016/j.adengl.2020.08.005. This article has 107 citations.

4. (pietkiewicz2023porokeratoses—acomprehensivereview pages 41-43): P. Pietkiewicz, Katarzyna Korecka, Natalia Salwowska, Ihor Kohut, Adarsha Adhikari, M. Bowszyc‑Dmochowska, A. Pogorzelska-Antkowiak, and C. Navarrete-Dechent. Porokeratoses—a comprehensive review on the genetics and metabolomics, imaging methods and management of common clinical variants. Metabolites, Nov 2023. URL: https://doi.org/10.3390/metabo13121176, doi:10.3390/metabo13121176. This article has 42 citations.

5. (NCT04359823 chunk 1): Dirk Elston, MD. DSAP Treatment Comparison: 2% Lovastatin/ 2% Cholesterol vs 2% Lovastatin Alone. Medical University of South Carolina. 2020. ClinicalTrials.gov Identifier: NCT04359823

6. (NCT04359823 chunk 2): Dirk Elston, MD. DSAP Treatment Comparison: 2% Lovastatin/ 2% Cholesterol vs 2% Lovastatin Alone. Medical University of South Carolina. 2020. ClinicalTrials.gov Identifier: NCT04359823

7. (pietkiewicz2023porokeratoses—acomprehensivereview pages 46-47): P. Pietkiewicz, Katarzyna Korecka, Natalia Salwowska, Ihor Kohut, Adarsha Adhikari, M. Bowszyc‑Dmochowska, A. Pogorzelska-Antkowiak, and C. Navarrete-Dechent. Porokeratoses—a comprehensive review on the genetics and metabolomics, imaging methods and management of common clinical variants. Metabolites, Nov 2023. URL: https://doi.org/10.3390/metabo13121176, doi:10.3390/metabo13121176. This article has 42 citations.

8. (vargasmora2020porokeratosisareview pages 2-4): P. Vargas-Mora, D. Morgado-Carrasco, and X. Fustà-Novell. Porokeratosis: a review of its pathophysiology, clinical manifestations, diagnosis, and treatment. Sep 2020. URL: https://doi.org/10.1016/j.adengl.2020.08.005, doi:10.1016/j.adengl.2020.08.005. This article has 107 citations.

9. (pietkiewicz2023porokeratoses—acomprehensivereview pages 2-5): P. Pietkiewicz, Katarzyna Korecka, Natalia Salwowska, Ihor Kohut, Adarsha Adhikari, M. Bowszyc‑Dmochowska, A. Pogorzelska-Antkowiak, and C. Navarrete-Dechent. Porokeratoses—a comprehensive review on the genetics and metabolomics, imaging methods and management of common clinical variants. Metabolites, Nov 2023. URL: https://doi.org/10.3390/metabo13121176, doi:10.3390/metabo13121176. This article has 42 citations.

10. (vargasmora2020porokeratosisareview pages 4-5): P. Vargas-Mora, D. Morgado-Carrasco, and X. Fustà-Novell. Porokeratosis: a review of its pathophysiology, clinical manifestations, diagnosis, and treatment. Sep 2020. URL: https://doi.org/10.1016/j.adengl.2020.08.005, doi:10.1016/j.adengl.2020.08.005. This article has 107 citations.

11. (pietkiewicz2023porokeratoses—acomprehensivereview pages 16-19): P. Pietkiewicz, Katarzyna Korecka, Natalia Salwowska, Ihor Kohut, Adarsha Adhikari, M. Bowszyc‑Dmochowska, A. Pogorzelska-Antkowiak, and C. Navarrete-Dechent. Porokeratoses—a comprehensive review on the genetics and metabolomics, imaging methods and management of common clinical variants. Metabolites, Nov 2023. URL: https://doi.org/10.3390/metabo13121176, doi:10.3390/metabo13121176. This article has 42 citations.

12. (pietkiewicz2023porokeratoses—acomprehensivereview pages 37-39): P. Pietkiewicz, Katarzyna Korecka, Natalia Salwowska, Ihor Kohut, Adarsha Adhikari, M. Bowszyc‑Dmochowska, A. Pogorzelska-Antkowiak, and C. Navarrete-Dechent. Porokeratoses—a comprehensive review on the genetics and metabolomics, imaging methods and management of common clinical variants. Metabolites, Nov 2023. URL: https://doi.org/10.3390/metabo13121176, doi:10.3390/metabo13121176. This article has 42 citations.

13. (pietkiewicz2023porokeratoses—acomprehensivereview pages 52-54): P. Pietkiewicz, Katarzyna Korecka, Natalia Salwowska, Ihor Kohut, Adarsha Adhikari, M. Bowszyc‑Dmochowska, A. Pogorzelska-Antkowiak, and C. Navarrete-Dechent. Porokeratoses—a comprehensive review on the genetics and metabolomics, imaging methods and management of common clinical variants. Metabolites, Nov 2023. URL: https://doi.org/10.3390/metabo13121176, doi:10.3390/metabo13121176. This article has 42 citations.

14. (pietkiewicz2023porokeratoses—acomprehensivereview pages 29-31): P. Pietkiewicz, Katarzyna Korecka, Natalia Salwowska, Ihor Kohut, Adarsha Adhikari, M. Bowszyc‑Dmochowska, A. Pogorzelska-Antkowiak, and C. Navarrete-Dechent. Porokeratoses—a comprehensive review on the genetics and metabolomics, imaging methods and management of common clinical variants. Metabolites, Nov 2023. URL: https://doi.org/10.3390/metabo13121176, doi:10.3390/metabo13121176. This article has 42 citations.

15. (pietkiewicz2023porokeratoses—acomprehensivereview pages 31-33): P. Pietkiewicz, Katarzyna Korecka, Natalia Salwowska, Ihor Kohut, Adarsha Adhikari, M. Bowszyc‑Dmochowska, A. Pogorzelska-Antkowiak, and C. Navarrete-Dechent. Porokeratoses—a comprehensive review on the genetics and metabolomics, imaging methods and management of common clinical variants. Metabolites, Nov 2023. URL: https://doi.org/10.3390/metabo13121176, doi:10.3390/metabo13121176. This article has 42 citations.

16. (pietkiewicz2023porokeratoses—acomprehensivereview pages 34-36): P. Pietkiewicz, Katarzyna Korecka, Natalia Salwowska, Ihor Kohut, Adarsha Adhikari, M. Bowszyc‑Dmochowska, A. Pogorzelska-Antkowiak, and C. Navarrete-Dechent. Porokeratoses—a comprehensive review on the genetics and metabolomics, imaging methods and management of common clinical variants. Metabolites, Nov 2023. URL: https://doi.org/10.3390/metabo13121176, doi:10.3390/metabo13121176. This article has 42 citations.

17. (pietkiewicz2023porokeratoses—acomprehensivereview pages 43-44): P. Pietkiewicz, Katarzyna Korecka, Natalia Salwowska, Ihor Kohut, Adarsha Adhikari, M. Bowszyc‑Dmochowska, A. Pogorzelska-Antkowiak, and C. Navarrete-Dechent. Porokeratoses—a comprehensive review on the genetics and metabolomics, imaging methods and management of common clinical variants. Metabolites, Nov 2023. URL: https://doi.org/10.3390/metabo13121176, doi:10.3390/metabo13121176. This article has 42 citations.

18. (aersilan2022microrna874targetsphosphomevalonate pages 17-17): Alimasi Aersilan, Naoko Hashimoto, Kazuyuki Yamagata, Masataka Yokoyama, Akitoshi Nakayama, Xiaoyan Shi, Hidekazu Nagano, Ikki Sakuma, Nijiro Nohata, Takashi Kinoshita, Naohiko Seki, Bahityar Rahmutulla, Atsushi Kaneda, Siti Nurul Zhahara, Yingbo Gong, Motoi Nishimura, Shoichiro Kawauchi, Eiryo Kawakami, and Tomoaki Tanaka. Microrna-874 targets phosphomevalonate kinase and inhibits cancer cell growth via the mevalonate pathway. Scientific Reports, Nov 2022. URL: https://doi.org/10.1038/s41598-022-23205-w, doi:10.1038/s41598-022-23205-w. This article has 17 citations and is from a peer-reviewed journal.

19. (vargasmora2020porokeratosisareview pages 12-13): P. Vargas-Mora, D. Morgado-Carrasco, and X. Fustà-Novell. Porokeratosis: a review of its pathophysiology, clinical manifestations, diagnosis, and treatment. Sep 2020. URL: https://doi.org/10.1016/j.adengl.2020.08.005, doi:10.1016/j.adengl.2020.08.005. This article has 107 citations.

## Artifacts

- [Edison artifact artifact-00](Porokeratosis-deep-research-falcon_artifacts/artifact-00.md)