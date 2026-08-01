---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-01T05:01:49.231094'
end_time: '2026-08-01T05:11:53.485420'
duration_seconds: 604.25
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hyperinsulinemic Hypoglycemia
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 26
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Hyperinsulinemic_Hypoglycemia-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hyperinsulinemic Hypoglycemia
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Hyperinsulinemic Hypoglycemia** covering all of the
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
- **Disease Name:** Hyperinsulinemic Hypoglycemia
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Hyperinsulinemic Hypoglycemia** covering all of the
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


# Hyperinsulinemic Hypoglycemia: Disease-Characteristics Research Report

**Scope.** “Hyperinsulinemic hypoglycemia” (HH) is a biochemical-clinical state rather than one molecular disease. This report focuses on **congenital hyperinsulinism (CHI)**—the principal genetic category requested—while separating acquired perinatal-stress HI, syndromic HI, insulinoma, autoimmune HI, and drug-associated causes. Evidence is chiefly aggregated disease-level literature and registries, not individual EHR data. The leading authority is the international consensus published **July 2023**, DOI/URL: https://doi.org/10.1159/000531766. A major recent primary source is the Ukrainian national registry published **17 December 2024**, DOI/URL: https://doi.org/10.3389/fendo.2024.1497579. PMIDs were not consistently exposed in the retrieved records; DOI links are therefore supplied rather than unverified PMID values.

## 1. Disease information

HH is inappropriate insulin action or failure to suppress insulin during hypoglycemia. Excess insulin simultaneously increases glucose utilization and prevents hepatic glycogenolysis, gluconeogenesis, lipolysis, and ketogenesis; the resulting **hypoketotic hypoglycemia** deprives the brain of both glucose and alternative ketone fuel. CHI is the most common and most severe cause of persistent hypoglycemia in infancy and childhood. It is clinically, genetically, and histologically heterogeneous, encompassing focal, diffuse, and atypical/mosaic pancreatic disease. The 2024 Ukrainian study defines it directly as a condition “caused by inappropriate insulin secretion during hypoglycemia.” (globa2024congenitalhyperinsulinismin pages 1-2, leon2024internationalguidelinesfor pages 3-5)

**Names:** congenital hyperinsulinism; congenital hyperinsulinism of infancy; persistent hyperinsulinemic hypoglycemia of infancy; hyperinsulinemic hypoglycemia; familial hyperinsulinism; hyperinsulinism/hyperammonemia syndrome for the GLUD1 subtype. “Nesidioblastosis” is a historical/pathologic term and should not be used as a universal synonym.

**Suggested identifiers:** MONDO disease mapping should use the specific **congenital hyperinsulinism/familial hyperinsulinism** concept rather than generic hypoglycemia; OMIM uses separate phenotype entries by molecular subtype rather than one universal CHI entry. MeSH concepts include *Hyperinsulinism* and *Hypoglycemia*. ICD-10-CM commonly maps congenital hyperinsulinism to **E16.1, Other hypoglycemia** or **E16.2, Hypoglycemia, unspecified**, depending on local coding; ICD-11 should be mapped to the specific hyperinsulinism/hypoglycemia concept in the implementation used. Exact MONDO/Orphanet numeric identifiers should be database-validated before ingestion because HH and familial hyperinsulinism are represented at different granularity.

## 2. Etiology, risk, protective factors, and gene–environment interaction

### Genetic causes

The most frequent causes are loss-of-function variants in **ABCC8** and **KCNJ11**, encoding SUR1 and Kir6.2 of the pancreatic β-cell ATP-sensitive potassium channel. Other established or reported genes include **GLUD1, GCK, HADH, HK1, SLC16A1, HNF4A, HNF1A, FOXA2, UCP2, PGM1, PMM2, ADK, CACNA1D**, and additional rare/syndromic loci. The 2024 Ukrainian registry states that variants in more than 30 genes can cause CHI, although gene lists and strength of evidence vary across panels. (globa2024congenitalhyperinsulinismin pages 1-2, leon2024internationalguidelinesfor pages 5-6, maines2023anarrativereview pages 1-2)

| Gene / etiology | Molecular defect and inheritance | Distinguishing phenotype / biomarker | Focal / diffuse / syndromic status | Management implication |
|---|---|---|---|---|
| **ABCC8 / KCNJ11** | Loss-of-function variants in beta-cell KATP channel genes; diffuse HI from recessive bi-allelic or dominant mono-allelic variants; focal HI from a **paternally inherited recessive** variant plus paternal isodisomy of **11p15** confined to the lesion (leon2024internationalguidelinesfor pages 5-6, globa2024congenitalhyperinsulinismin pages 1-2) | Severe neonatal hypoketotic hypoglycemia; diazoxide-unresponsive cases strongly enriched for KATP defects; paternally inherited single variant predicts focal lesion with high PPV/sensitivity; persistent CHI commonly due to these genes (leon2024internationalguidelinesfor pages 5-6, globa2024congenitalhyperinsulinismin pages 1-2, globa2024congenitalhyperinsulinismin pages 3-5) | **Diffuse or focal**; atypical/mosaic forms also reported with somatic variants (leon2024internationalguidelinesfor pages 5-6, leon2024internationalguidelinesfor pages 11-13) | Rapid **ABCC8/KCNJ11** testing guides care; if diazoxide-unresponsive and focal likely, perform **18F-DOPA PET** and limited resection; focal lesions are usually surgically curable, whereas diffuse disease may require 90–98% pancreatectomy and long-term diabetes surveillance (leon2024internationalguidelinesfor pages 5-6, leon2024internationalguidelinesfor pages 6-8, leon2024internationalguidelinesfor pages 11-13) |
| **GLUD1** | Activating/regulatory variants affecting glutamate dehydrogenase; inheritance not specified in retrieved evidence (leon2024internationalguidelinesfor pages 5-6) | **Moderately elevated plasma ammonia**; protein/leucine-induced hypoglycemia; neurodevelopmental and seizure burden may be high (leon2024internationalguidelinesfor pages 5-6, leon2024internationalguidelinesfor pages 13-15) | Non-syndromic genetic HI (leon2024internationalguidelinesfor pages 5-6) | Gene-specific dietary management may include **protein restriction**; usually considered outside KATP/focal surgical pathway (mittal2024molecularmechanismsunderlying pages 7-9, leon2024internationalguidelinesfor pages 5-6) |
| **HADH (SCHAD)** | Enzyme defect; inheritance not specified in retrieved evidence (leon2024internationalguidelinesfor pages 5-6) | May show **elevated plasma C4-OH acylcarnitine** and **urine 3-OH-glutarate**; protein-induced hypoglycemia reported (leon2024internationalguidelinesfor pages 5-6) | Non-syndromic genetic HI (leon2024internationalguidelinesfor pages 5-6) | Dietary modification may help; review cited **high-carbohydrate/low-fat diet** as gene-specific support, but evidence level in retrieved material is limited (mittal2024molecularmechanismsunderlying pages 7-9) |
| **GCK** | Activating variants; somatic **GCK** variants also linked to LINE/mosaic pathology; one 2024 case report suggests **GCK duplication** as a novel cause of nesidioblastosis (mechanism/new association still uncertain) (leon2024internationalguidelinesfor pages 5-6, shoji2024casereportduplication pages 8-8) | May develop **ketotic hypoglycemia with prolonged fasting**, unlike typical hypoketotic HI (leon2024internationalguidelinesfor pages 5-6) | Can be **diffuse/non-focal**; **localized islet nuclear enlargement (LINE)/mosaic** with somatic variants; adult nesidioblastosis reported in a case with chromosome 7 duplication containing **GCK** (leon2024internationalguidelinesfor pages 5-6, shoji2024casereportduplication pages 8-8) | Often **diazoxide-unresponsive** per guideline discussion; if localized somatic disease suspected, pathology/imaging interpretation is important; mechanistic significance of copy-number gain remains provisional (leon2024internationalguidelinesfor pages 8-10, leon2024internationalguidelinesfor pages 5-6, shoji2024casereportduplication pages 8-8) |
| **HK1** | Heterozygous **non-coding variants** preventing beta-cell silencing of **HK1**; inappropriate pancreatic HK1 expression also reported in atypical tissue (leon2024internationalguidelinesfor pages 5-6, leon2024internationalguidelinesfor pages 11-13) | Isolated HI; mechanism is aberrant beta-cell expression of hexokinase 1 rather than classic KATP dysfunction (leon2024internationalguidelinesfor pages 5-6) | Usually **isolated**; may contribute to **atypical / mosaic** pancreatic disease (leon2024internationalguidelinesfor pages 11-13, leon2024internationalguidelinesfor pages 5-6) | Include **non-coding regions** in testing because exome/panels can miss deep intronic/non-coding causes; no gene-specific approved therapy identified in retrieved evidence (leon2024internationalguidelinesfor pages 5-6) |
| **SLC16A1** | Activating promoter-region variants affecting monocarboxylate transporter 1 (MCT1) (leon2024internationalguidelinesfor pages 5-6) | **Anaerobic exercise-induced hypoglycemia** (leon2024internationalguidelinesfor pages 5-6) | Non-syndromic genetic HI (leon2024internationalguidelinesfor pages 5-6) | History of exercise-triggered episodes helps diagnosis; management implication is trigger recognition/avoidance plus standard HI therapy as needed (leon2024internationalguidelinesfor pages 5-6) |
| **HNF1A / HNF4A** | MODY-related transcription factor variants; transient neonatal hyperinsulinism may occur with family history suggestive of MODY (leon2024internationalguidelinesfor pages 3-5) | Family history of MODY; some cases improve over time (leon2024internationalguidelinesfor pages 3-5, leon2024internationalguidelinesfor pages 13-15) | Non-syndromic genetic HI; not focal KATP-type disease in retrieved evidence (leon2024internationalguidelinesfor pages 3-5) | Consider targeted testing when MODY pedigree is present; severity may decrease over time, allowing medication reduction; requires later diabetes surveillance (leon2024internationalguidelinesfor pages 13-15, leon2024internationalguidelinesfor pages 3-5) |
| **KMT2D / KDM6A (Kabuki syndrome)** | Chromatin-regulating genes; **KMT2D** usually de novo AD, **KDM6A** X-linked dominant in Kabuki syndrome; mechanism for HH is **not fully clarified** and likely epigenetic/beta-cell developmental (maines2023anarrativereview pages 1-2, globa2024congenitalhyperinsulinismin pages 1-2) | Syndromic features of Kabuki syndrome; HH prevalence reported as **0.3–4%** in KS and association is stronger for **KDM6A**-KS than **KMT2D**-KS (maines2023anarrativereview pages 1-2) | **Syndromic HI** (maines2023anarrativereview pages 1-2, globa2024congenitalhyperinsulinismin pages 1-2) | Evaluate for multisystem syndrome and provide genetic counseling; mechanism remains uncertain, so management is mostly standard HI treatment plus syndrome-specific care (leon2024internationalguidelinesfor pages 3-5, maines2023anarrativereview pages 1-2) |
| **11p15 / Beckwith-Wiedemann spectrum (BWS/BWSp)** | Imprinting defect / paternal UPD11p; in focal lesions there is loss of maternal heterozygosity at **11p15** with loss of nuclear **p57** staining; severe HI in BWSp can occur with **11pUPD** plus a paternally inherited **ABCC8/KCNJ11** variant (leon2024internationalguidelinesfor pages 5-6, leon2024internationalguidelinesfor pages 11-13, globa2024congenitalhyperinsulinismin pages 3-5) | Syndromic overgrowth context; pathology may show expanded endocrine tissue over large pancreatic areas; requires methylation testing when clinically suspected (leon2024internationalguidelinesfor pages 5-6, leon2024internationalguidelinesfor pages 11-13) | **Syndromic**, may mimic/extensively involve pancreas; focal-type molecular mechanism overlaps with 11p15 loss in lesion tissue (leon2024internationalguidelinesfor pages 11-13, leon2024internationalguidelinesfor pages 5-6) | Perform **11p methylation testing** if BWSp suspected; surgery can be more complex than classic focal HI because endocrine overgrowth may be extensive (leon2024internationalguidelinesfor pages 5-6, leon2024internationalguidelinesfor pages 11-13) |
| **Acquired perinatal-stress HI (PSHI)** | Acquired, not established genetic etiology in current evidence; linked to maternal diabetes, perinatal stress, birth asphyxia, IUGR, maternal drug exposure, or high maternal glucose infusion during delivery (leon2024internationalguidelinesfor pages 3-5) | Presents in first 24 h of life; affects about **1 in 1,200–1,700** newborns; often resolves within **10–14 days**; severe persistent form beyond 2 weeks occurs in about **1 in 12,000–13,600** newborns (leon2024internationalguidelinesfor pages 3-5) | **Acquired**, not focal genetic CHI (leon2024internationalguidelinesfor pages 3-5) | Genetic testing is **not usually recommended** initially; treat supportively, including diazoxide if prolonged/severe; retest after 72 h if still hypoglycemic during transitional period (leon2024internationalguidelinesfor pages 3-5) |


*Table: This table summarizes the main genetic and acquired etiologies of hyperinsulinemic hypoglycemia/congenital hyperinsulinism, highlighting distinguishing biomarkers, histologic patterns, inheritance, and immediate management implications. It is designed as a concise knowledge-base artifact for genotype-phenotype-treatment mapping.*

**Inheritance:** biallelic recessive or monoallelic dominant ABCC8/KCNJ11 variants cause diffuse HI. Focal HI is a two-hit, parent-of-origin disorder: a paternally inherited recessive ABCC8/KCNJ11 variant is unmasked by somatic paternal isodisomy/loss of the maternal 11p15 region in a pancreatic clone. A single paternal KATP variant predicts focal disease with sensitivity around 97% and positive predictive value up to 94%. Somatic ABCC8 or GCK variants and inappropriate HK1 expression occur in LINE/mosaic disease. (leon2024internationalguidelinesfor pages 5-6)

**Syndromic/chromosomal causes:** Beckwith–Wiedemann spectrum/11p15 imprinting defects, Kabuki syndrome (**KMT2D/KDM6A**), Sotos syndrome, Turner syndrome, Costello syndrome, Simpson–Golabi–Behmel syndrome, trisomy 13, congenital disorders of glycosylation, and rare chromosomal deletions/duplications are reported. A December 2024 human case linked mosaic chromosome 7 duplication containing **GCK** to adult nesidioblastosis; this remains a novel case-level association rather than an established recurrent cause. (leon2024internationalguidelinesfor pages 19-20, leon2024internationalguidelinesfor pages 17-19, shoji2024casereportduplication pages 8-8, maines2023anarrativereview pages 1-2)

### Acquired and environmental/perinatal causes

Maternal diabetes, birth asphyxia/hypoxia, intrauterine growth restriction, perinatal stress, maternal drugs, and high intrapartum maternal glucose infusion can produce perinatal-stress HI. The proposed interaction is hypoxia-mediated lowering of the β-cell glucose threshold for insulin suppression. PSHI usually presents in the first 24 hours and resolves in 10–14 days; a severe form persists beyond two weeks. These exposures are triggers for acquired HI, not established causes of germline CHI. (leon2024internationalguidelinesfor pages 3-5)

No reproducible lifestyle, toxin, smoking, alcohol, pollution, occupational, or infectious cause is established for **genetic CHI**. Rare autoimmune insulin syndromes or postinfectious associations belong in the broader HH differential, not the congenital genetic entry. No validated protective allele is known. Practical “protective factors” are therefore prevention of fasting, rapid glucose rescue, avoidance of genotype-specific triggers—protein/leucine in GLUD1/HADH disease and anaerobic exercise in SLC16A1 disease—and early specialist treatment. (leon2024internationalguidelinesfor pages 29-29, leon2024internationalguidelinesfor pages 5-6)

## 3. Phenotypes

* **Biochemical hypoglycemia**—usually neonatal or infantile, episodic/recurrent, and potentially severe; suggested HPO: **Hypoglycemia (HP:0001943)**, **Hyperinsulinemia (HP:0000842)**. Insulin action suppresses β-hydroxybutyrate and free fatty acids. Severity ranges from spontaneous remission to glucose requirements of 20–30 mg/kg/min. (leon2024internationalguidelinesfor pages 25-29, leon2024internationalguidelinesfor pages 6-8)
* **Neuroglycopenic/autonomic manifestations**—jitteriness, lethargy, poor feeding, apnea/cyanosis, altered consciousness, seizures, and coma; suggested HPO: neonatal hypoglycemia, seizures, lethargy, feeding difficulties, apnea, coma. Onset is commonly neonatal, but milder genetic disease can appear later. Frequency is cohort-dependent.
* **Neurologic sequelae**—epilepsy, infantile spasms, microcephaly, cerebral palsy, motor/speech delay, cognitive impairment, and attention, memory, visual, and sensorimotor deficits; suggested HPO: **Seizure (HP:0001250)**, **Global developmental delay (HP:0001263)**, **Microcephaly (HP:0000252)**, **Abnormality of movement**, speech delay, intellectual disability. Transient HI still carries reported neurodevelopmental-deficit rates of **26–44%**. In the 2024 Ukrainian persistent-CHI cohort, **11/22 (50%)** had epilepsy and/or psychomotor retardation. GLUD1-HI has particularly high seizure/neurodevelopmental burden. (globa2024congenitalhyperinsulinismin pages 3-5, leon2024internationalguidelinesfor pages 13-15)
* **Feeding dysfunction**—vomiting, impaired suck/swallow, food aversion, tube dependence, and reflux; suggested HPO: feeding difficulties, dysphagia, vomiting. Feeding problems were reported in **68.6%**, often reflecting disease plus medications, high-carbohydrate feeds, IV glucose, and tube feeding. (leon2024internationalguidelinesfor pages 13-15)
* **Gene-specific phenotypes:** moderate hyperammonemia and protein-induced hypoglycemia in GLUD1-HI; C4-OH acylcarnitine/urinary 3-hydroxyglutarate abnormalities in HADH-HI; exercise-induced episodes in SLC16A1-HI; occasionally ketotic fasting hypoglycemia in GCK-HI. (leon2024internationalguidelinesfor pages 5-6)

Quality of life is impaired by unpredictable episodes, sleep/feeding schedules, intensive glucose monitoring, medication toxicity, pump/tube failure, developmental disability, and caregiver anxiety. The guideline notes that caregiver worry affects physical and mental health and recommends psychological and patient-organization support. Disease-specific EQ-5D/SF-36 population norms were not identified. (leon2024internationalguidelinesfor pages 13-15)

## 4. Genetic and molecular information

Variant classes include missense, nonsense, frameshift, splice, exon-level copy-number, deep-intronic/regulatory, imprinting, and somatic variants. Germline variants predominate in inherited diffuse disease; focal lesions combine a germline paternal allele with a pancreatic somatic 11p15 event. LINE/mosaic disease can arise from somatic ABCC8/GCK variants. Variant classification must follow ACMG/AMP criteria with ClinVar/ClinGen review and segregation/functional evidence; a gene finding should not automatically be called pathogenic. Population allele frequency should be checked variant-by-variant in gnomAD, because no single useful “CHI allele frequency” exists.

The Ukrainian cohort provides current real-world data: a molecular diagnosis was obtained in **27/40 (67.5%)**; yield was **19/22 (86.4%)** in persistent versus **8/18 (44.4%)** in early-remission disease. Causes were ABCC8 (n=20), KCNJ11 (n=2), INSR (n=2), KMT2D (n=1), and 11p15 imprinting defects (n=2); one ABCC8 VUS was not counted as causal. (globa2024congenitalhyperinsulinismin pages 1-2, globa2024congenitalhyperinsulinismin pages 3-5)

No robust, generally accepted modifier-gene set, protective variant, anticipation phenomenon, or recurrent germline mosaicism rate is established. Consanguinity increases the probability of recessive diffuse CHI; founder variants explain high rates in some endogamous populations, but carrier frequencies are population- and variant-specific.

**Epigenetics:** 11p15 imprinting is causal in focal HI and BWS. In Kabuki syndrome, KMT2D and KDM6A alter H3K4/H3K27 chromatin regulation and may disturb β-cell differentiation and insulin-secretory gene expression, but the review explicitly concludes that the pathway “remains to be fully clarified.” Kabuki-associated HH occurs in approximately **0.3–4%**, more strongly with KDM6A-Kabuki than KMT2D-Kabuki. (leon2024internationalguidelinesfor pages 11-13, maines2023anarrativereview pages 1-2)

## 5. Environmental information

Genetic CHI is not attributable to diet, obesity, smoking, alcohol, radiation, pollution, or infection. Feeding composition and physical activity can modify episode occurrence after disease exists: protein/leucine can trigger GLUD1, HADH, and sometimes KATP-HI; anaerobic exercise can trigger SLC16A1-HI; fasting is a general precipitant. Perinatal hypoxia, IUGR, maternal diabetes, and delivery-related glucose exposure cause acquired PSHI. Vaccines and antimicrobial measures are not etiologic or preventive interventions for CHI. (leon2024internationalguidelinesfor pages 3-5, leon2024internationalguidelinesfor pages 5-6)

## 6. Mechanism and pathophysiology

**Canonical causal chain:** glucose enters the β cell → metabolism raises ATP/ADP → KATP channels close → membrane depolarization → voltage-gated Ca²⁺ entry → insulin-granule exocytosis. ABCC8/KCNJ11 loss of function keeps the membrane depolarized despite low glucose, causing unsuppressed insulin. Diazoxide works upstream by opening functional KATP channels; it therefore often fails when the channel is severely defective. (leon2024internationalguidelinesfor pages 25-29, leon2024internationalguidelinesfor pages 8-10)

**Downstream chain:** excess insulin → increased peripheral glucose uptake plus suppressed hepatic glucose production, lipolysis, and ketogenesis → low glucose, free fatty acids, and β-hydroxybutyrate → cerebral fuel failure → seizures and hypoglycemic brain injury. Relevant GO suggestions include regulation of insulin secretion (**GO:0050796**), insulin secretion (**GO:0030073**), membrane depolarization during action potential, calcium-ion transmembrane transport, glucose homeostasis (**GO:0042593**), fatty-acid oxidation, and ketone-body biosynthesis.

Other upstream mechanisms include altered nutrient sensing (activating GCK), deregulated amino-acid oxidation (GLUD1), fatty-acid oxidation/SCHAD–GDH coupling (HADH), inappropriate low-Km hexokinase expression (HK1), pyruvate transport into β cells (SLC16A1), transcription-factor defects, and chromatin/imprinting abnormalities. Immune activation is not a core mechanism in genetic CHI. Tissue injury is secondary: repeated neuroglycopenia injures the developing brain, while near-total pancreatectomy can cause endocrine and exocrine insufficiency.

**Cell types:** pancreatic β cell—**CL:0000169**—is primary; α/δ cells and acinar/ductal structures are relevant to histology and surgery. Neurons, astrocytes, and oligodendroglial lineages are downstream targets of fuel deprivation. **Subcellular terms:** plasma membrane, KATP channel complex, voltage-gated calcium-channel complex, insulin secretory granule, cytosol, mitochondrion, and nucleus/chromatin.

Current single-cell, spatial-transcriptomic, proteomic, metabolomic, lipidomic, and multi-omic signatures are not sufficiently standardized for clinical annotation. No omics assay is currently a routine diagnostic replacement for biochemical and DNA testing.

## 7. Anatomical structures affected

The primary organ is the **pancreas**—suggested UBERON **pancreas (UBERON:0001264)**—specifically islets of Langerhans and β cells. Focal lesions are usually unencapsulated, approximately **0.5–1 cm**, with increased endocrine-cell mass; diffuse disease displays β-cell nuclear enlargement throughout the pancreas; atypical disease has regional/mosaic abnormalities. There is no lateralization. (leon2024internationalguidelinesfor pages 10-11)

The main secondary organ is the **brain**, particularly the developing cerebral cortex, hippocampal/visual pathways, and white matter affected by recurrent hypoglycemia. Liver, skeletal muscle, and adipose tissue are metabolic effectors of insulin. After large pancreatic resection, both endocrine pancreas and exocrine acinar tissue are affected.

## 8. Temporal development

Severe KATP-CHI commonly begins in the first days of life, acutely or with recurrent episodes; genetic forms can occasionally present later. PSHI presents within 24 hours and usually resolves by days 10–14. “Early-remission” CHI in the Ukrainian study was defined by remission by age two years and no hypoglycemia for 24 months. Persistent CHI can remain lifelong, although ABCC8, KCNJ11, HNF1A, and HNF4A disease may attenuate with age. Later-onset HI after age two years requires insulinoma evaluation. (globa2024congenitalhyperinsulinismin pages 1-2, leon2024internationalguidelinesfor pages 13-15, leon2024internationalguidelinesfor pages 3-5)

The critical intervention window is immediate: the neonatal brain has high glucose requirements and limited alternative fuel because insulin suppresses ketogenesis. Prompt recognition, normal-range glucose restoration, and avoidance of recurrent episodes are more important than waiting for molecular confirmation.

## 9. Inheritance and population

Non-syndromic genetic HI is estimated at **1 per 25,000–45,000 births**; a UK minimum estimate cited by recent literature is **1 per 28,389**. PSHI is much more common, approximately **1 per 1,200–1,700 newborns**, while prolonged severe PSHI occurs in about **1 per 12,000–13,600**. (leon2024internationalguidelinesfor pages 3-5, globa2024congenitalhyperinsulinismin pages 10-11)

No consistent sex bias is established. In the Ukrainian registry, sex distributions differed numerically but not significantly: persistent CHI 36.4% male/63.6% female and early-remission CHI 55.6% male/44.4% female. Median diagnosis was 3.5 versus 17 days, respectively. (globa2024congenitalhyperinsulinismin pages 3-5)

Autosomal recessive, autosomal dominant, X-linked dominant syndromic, imprinting/parent-of-origin, and somatic mosaic mechanisms all occur. Penetrance and expressivity are gene- and variant-dependent; dominant KATP disease can be variably expressed. Genetic anticipation is not characteristic. Founder effects and consanguinity can markedly increase incidence in particular populations, but global carrier-frequency estimates are inappropriate.

## 10. Diagnostics

### Biochemical diagnosis

Obtain a **critical sample during plasma glucose <50 mg/dL (2.8 mmol/L)**. Evidence of excessive insulin action includes β-hydroxybutyrate **<1.8 mmol/L**, free fatty acids **<1.7 mmol/L**, glucose infusion requirement **>8 mg/kg/min in neonates**, and a glucagon-associated glucose rise **≥30 mg/dL**. Inappropriately detectable insulin **>1.25 μU/mL** and C-peptide **>0.5 ng/mL** support diagnosis, but suppressed ketones/FFA and glucagon response are more sensitive than insulin concentration alone. Measure glucose, insulin, C-peptide, BOHB, FFA, cortisol, growth hormone, lactate, ammonia, acylcarnitines, and urine organic acids as clinically indicated. (leon2024internationalguidelinesfor pages 25-29, leon2024internationalguidelinesfor pages 3-5)

Infants tested before 72 hours during transitional hypoglycemia should be retested after 72 hours if hypoglycemia persists. Provocative glucose/leucine/protein tests are not needed to establish HI but can subtype selected disease. (leon2024internationalguidelinesfor pages 3-5)

### Genetic and imaging algorithm

1. Exclude likely acquired PSHI and assess syndromic features.
2. In diazoxide-unresponsive disease, perform rapid **ABCC8/KCNJ11** sequencing with parental testing.
3. If negative or disease persists beyond three months, use a comprehensive HI panel or WES/WGS with copy-number and non-coding coverage.
4. Add 11p15 methylation testing when BWS is suspected. WES can miss deep-intronic/regulatory variants; Sanger can miss CNVs. WGS is useful when panel/exome testing is negative but is not universally first-line. CMA is appropriate for syndromic/CNV suspicion; routine karyotype, FISH, mitochondrial DNA, and repeat-expansion testing are not indicated without phenotype-specific reasons. (leon2024internationalguidelinesfor pages 5-6)
5. For diazoxide-unresponsive cases without genetic proof of diffuse disease, perform **18F-DOPA PET/CT or PET/MRI**. Across 286 histologically assessed cases, sensitivity was **75–100%**, specificity **88–100%**, and localization accuracy over **90%** when a lesion was detected. Conventional ultrasound/CT/MRI does not reliably detect congenital focal lesions. (leon2024internationalguidelinesfor pages 6-8)

Differentials include transitional/PSHI, cortisol or growth-hormone deficiency, fatty-acid oxidation disorders, glycogen-storage disease, congenital glycosylation disorders, exogenous insulin or sulfonylurea exposure, insulinoma—especially after age two—insulin autoimmune syndrome, and non-insulin-mediated hypoglycemia. (leon2024internationalguidelinesfor pages 3-5)

No universal population newborn screen exists. Bedside glucose surveillance is indicated in high-risk newborns. Cascade testing, prenatal diagnosis, or preimplantation genetic testing is feasible once a familial pathogenic variant is known.

## 11. Outcome and prognosis

Survival is generally good with effective treatment; meaningful 5- or 10-year disease-specific survival statistics are not established because morbidity, not mortality, dominates. Untreated severe episodes can cause coma, death, epilepsy, cerebral palsy, and permanent cognitive/visual/motor disability.

Outcome depends on diagnostic delay, depth/duration and recurrence of hypoglycemia, genotype, diazoxide responsiveness, focal versus diffuse histology, and treatment access. More than **65.2%** of patients required regimen adjustment in the first three months after discharge. Formal developmental surveillance and early intervention are strongly recommended. (leon2024internationalguidelinesfor pages 13-15)

Focal resection is curative in over **95%** in expert series and generally avoids later diabetes if only the lesion is removed. After 95–98% pancreatectomy for diffuse disease, hypoglycemia recurs in **50–60%**; approximately **25%** have diabetes immediately after surgery and cumulative diabetes can reach **91% by age 14**. Resection over 50% also risks exocrine pancreatic insufficiency. (leon2024internationalguidelinesfor pages 11-13)

The 2024 Ukrainian cohort provides contemporary implementation data: 14/19 operated patients had focal disease, and all 14 were cured; relapse occurred in three patients with diffuse or atypical disease. (globa2024congenitalhyperinsulinismin pages 1-2, globa2024congenitalhyperinsulinismin pages 3-5)

## 12. Treatment

### Acute and chronic algorithm

* **IV dextrose:** 200 mg/kg—2 mL/kg of D10—then generally ≥8 mg/kg/min, escalating rapidly when necessary, to maintain plasma glucose **70–100 mg/dL**. NCIt suggestions: dextrose, glucose infusion. (leon2024internationalguidelinesfor pages 6-8)
* **Glucagon rescue:** 0.5–1 mg or 20–30 μg/kg IM/SC when IV access is delayed. Continuous IV glucagon **2.5–20 μg/kg/h** reduces dextrose/fluid requirements; vomiting 13%, rash 2%, respiratory distress 19%, and rare necrolytic migratory erythema are reported. (leon2024internationalguidelinesfor pages 6-8)
* **Diazoxide:** first-line established therapy, **5–15 mg/kg/day** orally in children. Add chlorothiazide **10 mg/kg/day** or hydrochlorothiazide **1–2 mg/kg/day** to limit fluid retention. Confirm response by a safety fast showing BOHB >1.8 mmol/L before glucose falls below 50–60 mg/dL. Stop if maximal therapy fails after five days. Adverse effects include hypertrichosis **84.1%**, facial coarsening 24%, pulmonary hypertension 2.4%, neutropenia 15.6%, thrombocytopenia 4.7%, hyperuricemia 5.0%, and serious events requiring discontinuation 9.7%. Obtain an echocardiogram about one week after initiation and periodic CBC/uric acid. NCIt: diazoxide. (leon2024internationalguidelinesfor pages 8-10)
* **Somatostatin analogues:** second-line off-label treatment. Octreotide starts at **5–10 μg/kg/day**, maximum around 20 μg/kg/day; tachyphylaxis and necrotizing enterocolitis, especially in unstable premature infants, are major concerns. Lanreotide commonly starts at **30–60 mg monthly**. Monitor growth, gallbladder ultrasound, liver enzymes, thyroid function, and growth factors. NCIt: octreotide; lanreotide. (leon2024internationalguidelinesfor pages 8-10, leon2024internationalguidelinesfor pages 10-11)
* **Nutrition/support:** frequent feeds, carbohydrate-enriched formula, and continuous gastric dextrose up to 20% via NG/gastrostomy when needed. Uncooked cornstarch 1–2 g/kg may help after nine months, but controlled evidence is lacking. Feeding, speech, occupational, physical, and neurodevelopmental therapy are integral. (leon2024internationalguidelinesfor pages 10-11)
* **Avoid routine nifedipine, sirolimus, and glucocorticoids.** The international panel found inadequate efficacy for nifedipine and serious infection, diabetes, hepatitis, and pancreatic-insufficiency concerns for sirolimus; use only in approved research protocols, apart from rare genotype-specific considerations such as CACNA1D. (leon2024internationalguidelinesfor pages 10-11)

### Surgery

Resect localized focal disease in an expert center with intraoperative pathology. For medically uncontrollable diffuse disease, 90–98% pancreatectomy balances hypoglycemia control against diabetes risk. Monitor postoperative glucose, HbA1c every 6–12 months, fecal elastase, fat-soluble vitamins, and need for insulin or pancreatic enzymes. (leon2024internationalguidelinesfor pages 11-13, leon2024internationalguidelinesfor pages 10-11)

### Real-world implementation and experimental therapy

A 2024 four-patient KATP-CHI series used IV glucagon, pump-delivered octreotide, later monthly long-acting somatostatin analogues, CGM, specialized feeds, and developmental follow-up. All octreotide-treated patients developed biliary debris, resolving with ursodeoxycholic acid; catheter obstruction and bloodstream infection complicated IV glucagon. This is useful implementation evidence but too small for response-rate inference. (takasawa2024clinicalmanagementof pages 10-13)

* **RZ358/ersodetug**, an allosteric insulin-receptor antibody, completed a 23-participant phase 2 study, **NCT04538989**; results were first posted 28 May 2025. A 56-participant phase 3 trial, **NCT06208215**, is active/not recruiting and uses CGM hypoglycemia endpoints. It remains investigational. (NCT04538989 chunk 1, NCT06208215 chunk 2)
* **Dasiglucagon**, a soluble glucagon analogue delivered by continuous SC infusion, completed a 32-participant phase 3 trial, **NCT03777176**; a 42-participant long-term extension, **NCT03941236**, is active/not recruiting through an estimated 2026 completion. It remains investigational for CHI. (NCT03941236 chunk 1, NCT03777176 chunk 1, NCT03777176 chunk 2)
* **Efpegerglucagon/HM15136**, weekly SC therapy, is in a 16-participant phase 2 study, **NCT04732416**, active/not recruiting with estimated completion in 2027. (NCT04732416 chunk 1)
* Continuous SC glucagon was tested in five infants in **NCT02937558**; the very small trial precludes broad conclusions. (NCT02937558 chunk 1)

No approved gene, RNA, or cell therapy is available. Genotype-guided focal-lesion surgery is currently the strongest precision-medicine implementation.

## 13. Prevention

Primary prevention of a de novo or inherited CHI phenotype is generally unavailable. Genetic counseling enables reproductive risk assessment, carrier/cascade testing, prenatal diagnosis, and PGT-M when a familial variant is known. Optimization of maternal diabetes and prevention of perinatal hypoxia/IUGR may reduce acquired PSHI risk but does not prevent genetic CHI.

Secondary prevention is rapid identification of at-risk neonates, critical-sample testing, early genetic diagnosis, and immediate maintenance of glucose above 70 mg/dL. Tertiary prevention includes home glucose monitoring, individualized fasting plans, rescue glucagon, CGM as an adjunct rather than sole diagnostic device, developmental and feeding surveillance, and diabetes/exocrine screening after surgery. No immunization or infectious prophylaxis is specific to CHI. (leon2024internationalguidelinesfor pages 11-13, leon2024internationalguidelinesfor pages 13-15, leon2024internationalguidelinesfor pages 6-8)

## 14. Other species and natural disease

The core β-cell KATP, glucokinase, glutamate-dehydrogenase, and insulin-signaling pathways are evolutionarily conserved. Naturally occurring hyperinsulinemic hypoglycemia/insulinoma is recognized in companion animals, especially dogs and ferrets, but it is usually tumor-associated rather than a validated orthologous congenital syndrome. No zoonotic transmission exists. Species-specific OMIA/VBO claims and breed associations were not sufficiently supported by the retrieved evidence and should not be populated without dedicated veterinary-database verification.

## 15. Model organisms

Available models include **Abcc8/Kcnj11** knockout or channel-defective mice, activating-Gck mice, Glud1 hyperactivity models, isolated rodent/human islets, β-cell lines, and patient-derived pancreatic tissue. Genetic glucokinase activation causes hypoglycemia in mice, supporting GCK dosage/activity as causal, but mouse insulin-secretory thresholds and compensatory physiology do not fully reproduce neonatal human disease. (shoji2024casereportduplication pages 8-8)

Model applications include KATP electrophysiology, stimulus–secretion coupling, diazoxide response, amino-acid sensitivity, focal-lesion genetics, and candidate-drug testing. Important limitations are inability of simple germline models to recreate the human pancreatic somatic 11p15 focal lesion, species differences in islet architecture, and limited modeling of human neonatal brain injury. In-vitro calcium-channel and mTOR observations supplied rationale for nifedipine and sirolimus, but lack of reliable clinical effectiveness illustrates the translational limitation. (leon2024internationalguidelinesfor pages 10-11)

Robust CHI-specific single-cell atlases, spatial transcriptomics, mature patient-iPSC β-cell models, and CRISPR screens remain research opportunities rather than validated knowledge-base facts.

## Overall assessment

Current expert consensus treats CHI as a **time-critical, genotype-informed disorder of pancreatic β-cell insulin secretion**. The strongest recent advance is not a newly approved drug but integration of rapid genetics, 18F-DOPA PET, expert pathology, and lesion-directed surgery. The 2024 Ukrainian national study demonstrates that international access to this pathway can produce molecular diagnoses in 67.5% overall and cure all identified focal cases. However, diffuse disease, feeding burden, medication toxicity, unequal access, and neurodevelopmental injury remain major unmet needs. (globa2024congenitalhyperinsulinismin pages 1-2, globa2024congenitalhyperinsulinismin pages 3-5, leon2024internationalguidelinesfor pages 13-15)

### Selected exact source statements

* 2024 Ukrainian registry: “Pathogenic variants were identified in 19/22 (86.3%) individuals with persistent CHI … and 8/18 (44.4%) with early remission CHI.” (globa2024congenitalhyperinsulinismin pages 1-2)
* Same study: “After surgery, complete recovery was observed in all 14 with focal disease.” (globa2024congenitalhyperinsulinismin pages 1-2)
* 2023 international guideline: “We Recommend Diazoxide as the First-Line Treatment for Patients with an Established Diagnosis of Hyperinsulinism.” (leon2024internationalguidelinesfor pages 8-10)
* 2023 Kabuki review: “The impact of pathogenic variants in KDM6A and KMT2D genes on β-cell insulin release remains to be fully clarified.” (maines2023anarrativereview pages 1-2)

References

1. (globa2024congenitalhyperinsulinismin pages 1-2): Evgenia Globa, Henrik Thybo Christesen, Michael Bau Mortensen, Jayne A. L. Houghton, Anne Lerberg Nielsen, Sönke Detlefsen, and Sarah E. Flanagan. Congenital hyperinsulinism in the ukraine: a 10-year national study. Frontiers in Endocrinology, Dec 2024. URL: https://doi.org/10.3389/fendo.2024.1497579, doi:10.3389/fendo.2024.1497579. This article has 6 citations.

2. (leon2024internationalguidelinesfor pages 3-5): Diva D. De Leon, Jean Baptiste Arnoux, Indraneel Banerjee, Ignacio Bergada, Tricia Bhatti, Louise S. Conwell, Junfen Fu, Sarah E. Flanagan, David Gillis, Thomas Meissner, Klaus Mohnike, Tai L.S. Pasquini, Pratik Shah, Charles A. Stanley, Adrian Vella, Tohru Yorifuji, and Paul S. Thornton. International guidelines for the diagnosis and management of hyperinsulinism. Jul 2023. URL: https://doi.org/10.1159/000531766, doi:10.1159/000531766. This article has 102 citations and is from a peer-reviewed journal.

3. (leon2024internationalguidelinesfor pages 5-6): Diva D. De Leon, Jean Baptiste Arnoux, Indraneel Banerjee, Ignacio Bergada, Tricia Bhatti, Louise S. Conwell, Junfen Fu, Sarah E. Flanagan, David Gillis, Thomas Meissner, Klaus Mohnike, Tai L.S. Pasquini, Pratik Shah, Charles A. Stanley, Adrian Vella, Tohru Yorifuji, and Paul S. Thornton. International guidelines for the diagnosis and management of hyperinsulinism. Jul 2023. URL: https://doi.org/10.1159/000531766, doi:10.1159/000531766. This article has 102 citations and is from a peer-reviewed journal.

4. (maines2023anarrativereview pages 1-2): Evelina Maines, Arianna Maiorana, Letizia Leonardi, Giovanni Piccoli, Massimo Soffiati, and Roberto Franceschi. A narrative review on pathogenetic mechanisms of hyperinsulinemic hypoglycemia in kabuki syndrome. Endocrine Regulations, 57:128-137, Jan 2023. URL: https://doi.org/10.2478/enr-2023-0016, doi:10.2478/enr-2023-0016. This article has 3 citations.

5. (globa2024congenitalhyperinsulinismin pages 3-5): Evgenia Globa, Henrik Thybo Christesen, Michael Bau Mortensen, Jayne A. L. Houghton, Anne Lerberg Nielsen, Sönke Detlefsen, and Sarah E. Flanagan. Congenital hyperinsulinism in the ukraine: a 10-year national study. Frontiers in Endocrinology, Dec 2024. URL: https://doi.org/10.3389/fendo.2024.1497579, doi:10.3389/fendo.2024.1497579. This article has 6 citations.

6. (leon2024internationalguidelinesfor pages 11-13): Diva D. De Leon, Jean Baptiste Arnoux, Indraneel Banerjee, Ignacio Bergada, Tricia Bhatti, Louise S. Conwell, Junfen Fu, Sarah E. Flanagan, David Gillis, Thomas Meissner, Klaus Mohnike, Tai L.S. Pasquini, Pratik Shah, Charles A. Stanley, Adrian Vella, Tohru Yorifuji, and Paul S. Thornton. International guidelines for the diagnosis and management of hyperinsulinism. Jul 2023. URL: https://doi.org/10.1159/000531766, doi:10.1159/000531766. This article has 102 citations and is from a peer-reviewed journal.

7. (leon2024internationalguidelinesfor pages 6-8): Diva D. De Leon, Jean Baptiste Arnoux, Indraneel Banerjee, Ignacio Bergada, Tricia Bhatti, Louise S. Conwell, Junfen Fu, Sarah E. Flanagan, David Gillis, Thomas Meissner, Klaus Mohnike, Tai L.S. Pasquini, Pratik Shah, Charles A. Stanley, Adrian Vella, Tohru Yorifuji, and Paul S. Thornton. International guidelines for the diagnosis and management of hyperinsulinism. Jul 2023. URL: https://doi.org/10.1159/000531766, doi:10.1159/000531766. This article has 102 citations and is from a peer-reviewed journal.

8. (leon2024internationalguidelinesfor pages 13-15): Diva D. De Leon, Jean Baptiste Arnoux, Indraneel Banerjee, Ignacio Bergada, Tricia Bhatti, Louise S. Conwell, Junfen Fu, Sarah E. Flanagan, David Gillis, Thomas Meissner, Klaus Mohnike, Tai L.S. Pasquini, Pratik Shah, Charles A. Stanley, Adrian Vella, Tohru Yorifuji, and Paul S. Thornton. International guidelines for the diagnosis and management of hyperinsulinism. Jul 2023. URL: https://doi.org/10.1159/000531766, doi:10.1159/000531766. This article has 102 citations and is from a peer-reviewed journal.

9. (mittal2024molecularmechanismsunderlying pages 7-9): Medha Mittal, Amit Kumar Gupta, and Seema Kapoor. Molecular mechanisms underlying congenital hyperinsulinemia of infancy and its relevance to management – a review. Journal of Pediatric Endocrinology and Diabetes, 4:9-20, Aug 2024. URL: https://doi.org/10.25259/jped\_25\_2024, doi:10.25259/jped\_25\_2024. This article has 1 citations.

10. (shoji2024casereportduplication pages 8-8): Takashi Shoji, Ichiro Yamauchi, Hidenori Kawasaki, Kogoro Iwanaga, Takuro Hakata, Daisuke Tanaka, Junji Fujikura, Toshihiko Masui, Hisato Suzuki, Mamiko Yamada, Kenjiro Kosaki, Yosuke Kasai, Etsuro Hatano, Akira Inaba, Takahito Wada, Shinji Kosugi, Yohei Ueda, Toshihito Fujii, Daisuke Taura, and Nobuya Inagaki. Case report: duplication of the gck gene is a novel cause of nesidioblastosis: evidence from a case with silver-russell syndrome-like phenotype related to chromosome 7. Frontiers in Endocrinology, Dec 2024. URL: https://doi.org/10.3389/fendo.2024.1431547, doi:10.3389/fendo.2024.1431547. This article has 0 citations.

11. (leon2024internationalguidelinesfor pages 8-10): Diva D. De Leon, Jean Baptiste Arnoux, Indraneel Banerjee, Ignacio Bergada, Tricia Bhatti, Louise S. Conwell, Junfen Fu, Sarah E. Flanagan, David Gillis, Thomas Meissner, Klaus Mohnike, Tai L.S. Pasquini, Pratik Shah, Charles A. Stanley, Adrian Vella, Tohru Yorifuji, and Paul S. Thornton. International guidelines for the diagnosis and management of hyperinsulinism. Jul 2023. URL: https://doi.org/10.1159/000531766, doi:10.1159/000531766. This article has 102 citations and is from a peer-reviewed journal.

12. (leon2024internationalguidelinesfor pages 19-20): Diva D. De Leon, Jean Baptiste Arnoux, Indraneel Banerjee, Ignacio Bergada, Tricia Bhatti, Louise S. Conwell, Junfen Fu, Sarah E. Flanagan, David Gillis, Thomas Meissner, Klaus Mohnike, Tai L.S. Pasquini, Pratik Shah, Charles A. Stanley, Adrian Vella, Tohru Yorifuji, and Paul S. Thornton. International guidelines for the diagnosis and management of hyperinsulinism. Jul 2023. URL: https://doi.org/10.1159/000531766, doi:10.1159/000531766. This article has 102 citations and is from a peer-reviewed journal.

13. (leon2024internationalguidelinesfor pages 17-19): Diva D. De Leon, Jean Baptiste Arnoux, Indraneel Banerjee, Ignacio Bergada, Tricia Bhatti, Louise S. Conwell, Junfen Fu, Sarah E. Flanagan, David Gillis, Thomas Meissner, Klaus Mohnike, Tai L.S. Pasquini, Pratik Shah, Charles A. Stanley, Adrian Vella, Tohru Yorifuji, and Paul S. Thornton. International guidelines for the diagnosis and management of hyperinsulinism. Jul 2023. URL: https://doi.org/10.1159/000531766, doi:10.1159/000531766. This article has 102 citations and is from a peer-reviewed journal.

14. (leon2024internationalguidelinesfor pages 29-29): Diva D. De Leon, Jean Baptiste Arnoux, Indraneel Banerjee, Ignacio Bergada, Tricia Bhatti, Louise S. Conwell, Junfen Fu, Sarah E. Flanagan, David Gillis, Thomas Meissner, Klaus Mohnike, Tai L.S. Pasquini, Pratik Shah, Charles A. Stanley, Adrian Vella, Tohru Yorifuji, and Paul S. Thornton. International guidelines for the diagnosis and management of hyperinsulinism. Jul 2023. URL: https://doi.org/10.1159/000531766, doi:10.1159/000531766. This article has 102 citations and is from a peer-reviewed journal.

15. (leon2024internationalguidelinesfor pages 25-29): Diva D. De Leon, Jean Baptiste Arnoux, Indraneel Banerjee, Ignacio Bergada, Tricia Bhatti, Louise S. Conwell, Junfen Fu, Sarah E. Flanagan, David Gillis, Thomas Meissner, Klaus Mohnike, Tai L.S. Pasquini, Pratik Shah, Charles A. Stanley, Adrian Vella, Tohru Yorifuji, and Paul S. Thornton. International guidelines for the diagnosis and management of hyperinsulinism. Jul 2023. URL: https://doi.org/10.1159/000531766, doi:10.1159/000531766. This article has 102 citations and is from a peer-reviewed journal.

16. (leon2024internationalguidelinesfor pages 10-11): Diva D. De Leon, Jean Baptiste Arnoux, Indraneel Banerjee, Ignacio Bergada, Tricia Bhatti, Louise S. Conwell, Junfen Fu, Sarah E. Flanagan, David Gillis, Thomas Meissner, Klaus Mohnike, Tai L.S. Pasquini, Pratik Shah, Charles A. Stanley, Adrian Vella, Tohru Yorifuji, and Paul S. Thornton. International guidelines for the diagnosis and management of hyperinsulinism. Jul 2023. URL: https://doi.org/10.1159/000531766, doi:10.1159/000531766. This article has 102 citations and is from a peer-reviewed journal.

17. (globa2024congenitalhyperinsulinismin pages 10-11): Evgenia Globa, Henrik Thybo Christesen, Michael Bau Mortensen, Jayne A. L. Houghton, Anne Lerberg Nielsen, Sönke Detlefsen, and Sarah E. Flanagan. Congenital hyperinsulinism in the ukraine: a 10-year national study. Frontiers in Endocrinology, Dec 2024. URL: https://doi.org/10.3389/fendo.2024.1497579, doi:10.3389/fendo.2024.1497579. This article has 6 citations.

18. (takasawa2024clinicalmanagementof pages 10-13): Kei Takasawa, Ryosei Iemura, Ryuta Orimoto, Haruki Yamano, Shizuka Kirino, Eriko Adachi, Yoko Saito, Kurara Yamamoto, Nozomi Matsuda, Shigeru Takishima, Kumi Shuno, Hanako Tajima, Manabu Sugie, Yuki Mizuno, Akito Sutani, Kentaro Okamoto, Michiya Masue, Tomohiro Morio, and Kenichi Kashimada. Clinical management of diazoxide-unresponsive congenital hyperinsulinism: a single-center experience. Clinical Pediatric Endocrinology, 33:187-194, Jun 2024. URL: https://doi.org/10.1297/cpe.2024-0004, doi:10.1297/cpe.2024-0004. This article has 4 citations and is from a peer-reviewed journal.

19. (NCT04538989 chunk 1):  An Open-Label Multiple Dose Study of RZ358 in Patients With Congenital Hyperinsulinism. Rezolute. 2020. ClinicalTrials.gov Identifier: NCT04538989

20. (NCT06208215 chunk 2):  RZ358 Treatment for Congenital Hyperinsulinism. Rezolute. 2024. ClinicalTrials.gov Identifier: NCT06208215

21. (NCT03941236 chunk 1):  Extension Trial Evaluating the Long-term Safety and Efficacy of Dasiglucagon in Children With Congenital Hyperinsulinism. Zealand Pharma. 2019. ClinicalTrials.gov Identifier: NCT03941236

22. (NCT03777176 chunk 1):  A Two-Period Open-label Trial Evaluating Efficacy and Safety of Dasiglucagon in Children With Congenital Hyperinsulinism. Zealand Pharma. 2019. ClinicalTrials.gov Identifier: NCT03777176

23. (NCT03777176 chunk 2):  A Two-Period Open-label Trial Evaluating Efficacy and Safety of Dasiglucagon in Children With Congenital Hyperinsulinism. Zealand Pharma. 2019. ClinicalTrials.gov Identifier: NCT03777176

24. (NCT04732416 chunk 1):  HM15136 (Efpegerglucagon) Treatment for 8 Weeks in Subjects Aged ≥2 Years With Congenital Hyperinsulinism (CHI). Hanmi Pharmaceutical Company Limited. 2022. ClinicalTrials.gov Identifier: NCT04732416

25. (NCT02937558 chunk 1):  CSI-Glucagon for Prevention of Hypoglycemia in Children With Congenital Hyperinsulinism. Xeris Pharmaceuticals. 2016. ClinicalTrials.gov Identifier: NCT02937558

## Artifacts

- [Edison artifact artifact-00](Hyperinsulinemic_Hypoglycemia-deep-research-falcon_artifacts/artifact-00.md)