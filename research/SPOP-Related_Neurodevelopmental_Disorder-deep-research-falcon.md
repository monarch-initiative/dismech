---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-02T13:18:54.403891'
end_time: '2026-09-02T13:37:56.273909'
duration_seconds: 1141.87
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: SPOP-Related Neurodevelopmental Disorder
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 23
reference_validation:
  total_references: 8
  verified: 8
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 8
  on_topic: 1
  validator_version: 0.2.1
term_validation:
  total_terms: 23
  verified: 23
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: SPOP-Related_Neurodevelopmental_Disorder-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** SPOP-Related Neurodevelopmental Disorder
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **SPOP-Related Neurodevelopmental Disorder** covering all of the
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

**Present this section as an ordered causal chain first, then the detail below.**
Open with a numbered sequence of mechanistic steps running from the initiating
lesion (mutation, exposure, infection) to the clinical manifestation, one step per
line, each naming what it causes next. State the causal verb explicitly ("leads
to", "results in") and say where a step is inferred rather than demonstrated.
Where the mechanism branches, show the branch. The categories below are a
checklist of what to cover within those steps, not the organizing structure —
a step may draw on several of them, and a category may contribute to several
steps.

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
- **Disease Name:** SPOP-Related Neurodevelopmental Disorder
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **SPOP-Related Neurodevelopmental Disorder** covering all of the
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

**Present this section as an ordered causal chain first, then the detail below.**
Open with a numbered sequence of mechanistic steps running from the initiating
lesion (mutation, exposure, infection) to the clinical manifestation, one step per
line, each naming what it causes next. State the causal verb explicitly ("leads
to", "results in") and say where a step is inferred rather than demonstrated.
Where the mechanism branches, show the branch. The categories below are a
checklist of what to cover within those steps, not the organizing structure —
a step may draw on several of them, and a category may contribute to several
steps.

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


# SPOP-Related Neurodevelopmental Disorder

## Executive summary

SPOP-related neurodevelopmental disorder is an ultra-rare, autosomal-dominant developmental disorder caused principally by heterozygous **de novo missense variants in SPOP**, encoding the substrate-recognition adaptor of the CUL3–RBX1 E3 ubiquitin-ligase complex. It is also called **Nabais Sá–de Vries syndrome (NSDVS)**. Two molecularly and clinically distinguishable forms have been proposed: a microcephaly/hearing-loss form associated with SPOP variants that increase degradation of BET-family proteins, and a macrocephaly/multisystem form associated with dominant-negative variants that increase BET-protein abundance. The foundational evidence remains a 2020 series of only seven individuals; therefore, frequencies, penetrance, prognosis, and genotype–phenotype relationships are provisional. (sa2020denovovariants pages 2-4, sa2020denovovariants pages 1-2)

The strongest disease-specific mechanism is altered stability of BRD2, BRD3, and BRD4. SPOP–GLI3/Hedgehog dysregulation is strongly supported by mouse genetic and rescue studies but has not been demonstrated in affected human neural tissue. No disease-modifying treatment, clinical-management guideline, validated biomarker, epidemiologic estimate, or relevant interventional trial was identified. Current care is multidisciplinary and symptom directed. (sa2020denovovariants pages 5-6, cai2016spoppromotesskeletal pages 4-5, olivareshuerta2026nabaissádevries pages 7-8, olivareshuerta2026nabaissádevries pages 8-9)

| Domain | Key finding | Quantitative detail | Evidence type | Source/date/DOI |
|---|---|---:|---|---|
| Disease definition | Foundational description of SPOP-related neurodevelopmental disorder identified two clinically distinct syndromic presentations caused by de novo SPOP missense variants | 7 affected individuals; 6 unique de novo missense variants; ascertainment from large exome cohorts including 4,749 unexplained ID cases, 1,133 developmental disorder cases, and 14,183 NDD cases | Human clinical + human functional | Sá et al., *Am J Hum Genet*, Mar 2020, doi:10.1016/j.ajhg.2020.02.001 (sa2020denovovariants pages 2-4, sa2020denovovariants pages 1-2) |
| Core phenotype | Shared phenotype across reported individuals includes intellectual disability, motor delay, speech delay, facial dysmorphism, and congenital anomalies | ID 7/7; motor delay 7/7; speech delay 7/7; facial dysmorphism 7/7; congenital anomalies 7/7 | Human clinical | Sá et al., Mar 2020, doi:10.1016/j.ajhg.2020.02.001 (sa2020denovovariants pages 2-4) |
| Variant group 1 | p.Arg121Gln and p.Asp144Asn define a microcephaly/hearing-loss group with gain-of-function behavior toward BET protein reduction | 2/7 individuals; congenital microcephaly 2/2; hearing loss 2/2 | Human clinical + human cell functional | Sá et al., Mar 2020, doi:10.1016/j.ajhg.2020.02.001 (sa2020denovovariants pages 2-4) |
| Variant group 2 | p.Thr25Ala, p.Tyr83Cys, p.Gly132Val, and recurrent p.Arg138Cys define a macrocephaly/multisystem group with dominant-negative behavior and BET protein increase | 5/7 individuals; macrocephaly/relative macrocephaly 5/5; cardiovascular abnormalities 4/4 reported; endocrine abnormalities 3/4; epilepsy 2/5; sleep disturbance 4/5; short stature/failure to thrive 2/5 | Human clinical + human cell functional | Sá et al., Mar 2020, doi:10.1016/j.ajhg.2020.02.001 (sa2020denovovariants pages 2-4) |
| Molecular mechanism in patients | Opposite functional classes converge on dysregulation of BET proteins BRD2/3/4 | Group 1 variants reduced BET protein amounts; group 2 variants increased BET protein amounts | Human cell functional | Sá et al., Mar 2020, doi:10.1016/j.ajhg.2020.02.001 (sa2020denovovariants pages 2-4, sa2020denovovariants pages 5-6) |
| Structural interpretation | Disease variants cluster in or near the substrate-recognition region of SPOP, consistent with altered substrate handling | 6 pathogenic missense alleles reported in MATH/BTB-related functional regions; recurrent p.Arg138Cys in 2 individuals | Human genetics + structural inference | Sá et al., Mar 2020, doi:10.1016/j.ajhg.2020.02.001 (sa2020denovovariants pages 4-5, sa2020denovovariants pages 5-6) |
| General SPOP biology | SPOP is the substrate adaptor of the CUL3/RBX1 E3 ligase complex; substrate binding uses MATH domain, dimerization/oligomerization uses BTB/BACK, and LLPS-like condensates can enhance ubiquitination | 374-aa protein; >33 substrates reported in review literature; BET proteins included among substrates | Authoritative review; non-disease-specific | Zhang et al., *Cancer Research*, Dec 2023, doi:10.1158/0008-5472.CAN-22-2801 (zhang2023deregulationofspop pages 1-1, zhang2023deregulationofspop pages 2-3); Ovalle et al., Sep 2021, doi:10.35509/01239015.717 (ovalle2021speckletypepozadaptor pages 2-5, ovalle2021speckletypepozadaptor pages 1-2) |
| Upstream/downstream interpretation | **Inferred:** altered substrate recognition by mutant SPOP leads to abnormal BRD2/3/4 turnover, which likely perturbs cell-cycle progression and neuronal differentiation, contributing to head-size and neurodevelopmental phenotypes | No patient neural tissue transcriptomic/proteomic readout available | Inference from human functional data + literature | Sá et al., Mar 2020 (sa2020denovovariants pages 5-6); Zhang et al., Dec 2023 (zhang2023deregulationofspop pages 1-1) |
| Brain imaging/anatomy | Available neuroimaging evidence is limited but includes ventriculomegaly in part of the macrocephaly group | Postnatal ventriculomegaly reported in 2 individuals (individuals 3-4) | Human clinical | Sá et al., Mar 2020, doi:10.1016/j.ajhg.2020.02.001 (sa2020denovovariants pages 5-6) |
| Mouse developmental mechanism | Spop regulates Gli3 abundance and modulates Shh/Hedgehog signaling during spinal cord development; nervous-system defects occur in some loss-of-function embryos | Subset with exencephaly/spina bifida; normal D/V patterning in simple Spop mutants but severe ventralization in sensitized double/triple mutant contexts | Mouse genetics/mechanistic | Cai & Liu, *Dev Biol*, Dec 2017, doi:10.1016/j.ydbio.2017.04.002 (cai2017spopregulatesgli3 pages 9-9, cai2017spopregulatesgli3 pages 2-3, cai2017spopregulatesgli3 pages 3-7) |
| Mouse skeletal rescue | Spop promotes skeletal development by restraining Gli3 repressor; lowering Gli3 dosage rescues Spop skeletal phenotypes | Spop-null/conditional mice show brachydactyly, osteopenia, delayed ossification; rescue demonstrated in Spop;Gli3+/− backgrounds | Mouse genetics + rescue | Cai & Liu, *PNAS*, Dec 2016, doi:10.1073/pnas.1612520114 (cai2016spoppromotesskeletal pages 4-5, cai2016spoppromotesskeletal pages 5-5, cai2016spoppromotesskeletal pages 1-1, cai2016spoppromotesskeletal pages 1-2, cai2016spoppromotesskeletal pages 2-4) |
| Relevance of animal models to human NDD | **Inferred/plausible branch:** GLI3/Hedgehog dysregulation may contribute to human SPOP syndrome, but this has not been directly demonstrated in patient-derived neural tissue or patient cohorts | 0 direct patient GLI3/Hedgehog biomarker studies identified | Cross-species inference/data gap | Human study + mouse studies (sa2020denovovariants pages 5-6, cai2017spopregulatesgli3 pages 9-9, cai2016spoppromotesskeletal pages 1-2) |
| Recent developments (2023-2024) | Recent literature places SPOP-related disease within the broader chromatinopathy/epigene-disorder landscape and emphasizes epigenetic-state imbalance as a diagnostic concept | Review notes 154 epigenes linked to chromatinopathies overall; no SPOP-specific episignature demonstrated in retrieved evidence | 2024 review; contextual | Bukowska-Olech et al., *J Appl Genet*, Jan 2024, doi:10.1007/s13353-023-00824-1 (context available from paper search results; no disease-specific context ID extracted) |
| Diagnostics | Real-world identification is via exome/genome-based rare-disease diagnostics, typically trio analysis with de novo confirmation | All foundational SPOP variants were de novo; Sanger confirmation reported | Human clinical genomics | Sá et al., Mar 2020, doi:10.1016/j.ajhg.2020.02.001 (sa2020denovovariants pages 2-4) |
| Epidemiology | Ultra-rare Mendelian disorder; no prevalence or incidence estimates were found in retrieved authoritative sources | Prevalence: not available; incidence: not available | Data gap | No retrievable disease-specific epidemiology in available evidence (sa2020denovovariants pages 2-4, olivareshuerta2026nabaissádevries pages 8-9) |
| Treatment/guidelines | No disease-specific pharmacologic therapy, gene therapy, or formal management guideline identified | 0 relevant clinical trials found; 0 disease-specific treatment studies found | Negative evidence / data gap | Clinical-trial searches negative; case-report literature states no follow-up guidelines established (olivareshuerta2026nabaissádevries pages 7-8, olivareshuerta2026nabaissádevries pages 8-9) |
| Current care implementation | Management is phenotype-driven multidisciplinary care rather than syndrome-specific therapy | Specialists explicitly suggested include neurology, cardiology, ophthalmology, and otorhinolaryngology | Case report / extrapolated standard care | Olivares-Huerta et al., *Cureus*, Apr 2026, doi:10.7759/cureus.107064 (olivareshuerta2026nabaissádevries pages 7-8, olivareshuerta2026nabaissádevries pages 8-9) |
| Evidence gaps | No disease-specific natural history, survival statistics, QoL studies, penetrance estimates, protective factors, environmental triggers, gene-environment interactions, single-cell/spatial omics, or episignature validation were found | 0 direct studies identified for each listed category in retrieved evidence | Data gap | Synthesized from all retrieved evidence (sa2020denovovariants pages 2-4, olivareshuerta2026nabaissádevries pages 8-9) |


*Table: This compact table summarizes the strongest available evidence for SPOP-related neurodevelopmental disorder, spanning the founding human cohort, mechanistic variant groups, relevant SPOP biology, and model-organism studies. It also highlights major evidence gaps, including the lack of disease-specific trials or guidelines.*

## 1. Disease information

### Definition and scope

The disorder was delineated by Sá and colleagues in *The American Journal of Human Genetics* in 2020. Clinical exome sequencing identified seven affected individuals carrying six unique de novo SPOP missense variants. Every individual had intellectual disability, motor delay, speech delay, facial dysmorphism, and congenital anomalies. Opposite effects on BET-protein abundance separated the cohort into two clinical groups. (sa2020denovovariants pages 2-4)

The source is therefore primarily an **aggregated disease-level case series**, although it is assembled from individual clinical records and sequencing results. The seven cases arose from large diagnostic cohorts, including 4,749 individuals with unexplained intellectual disability, 1,133 with developmental disorders, and 14,183 with neurodevelopmental disorders; these denominators are ascertainment cohorts, not prevalence studies. (sa2020denovovariants pages 2-4)

### Names and identifiers

- Preferred descriptive name: **SPOP-related neurodevelopmental disorder**.
- Eponym: **Nabais Sá–de Vries syndrome**.
- Subtype terminology: **Nabais Sá–de Vries syndrome type 1/type 2**; published usage is not yet fully standardized, so knowledge-base records should retain the functional and phenotypic description alongside any subtype number.
- Gene: **SPOP**, speckle-type POZ protein; chromosomal locus **17q21.33**. (ovalle2021speckletypepozadaptor pages 2-5)
- MONDO, OMIM, Orphanet, ICD-10/11, and MeSH identifiers: **not independently verified in the retrieved evidence**. A dedicated syndrome-specific ICD or MeSH code was not demonstrated; clinically, coding will generally use manifestations such as developmental delay, intellectual disability, epilepsy, hearing loss, and congenital anomalies.

### Key primary source

Sá MJN et al. “De Novo Variants in SPOP Cause Two Clinically Distinct Neurodevelopmental Disorders.” *Am J Hum Genet.* Published February 27/March 5, 2020. DOI: [10.1016/j.ajhg.2020.02.001](https://doi.org/10.1016/j.ajhg.2020.02.001). The retrieved record did not expose a PMID, so one is not supplied here rather than risk an erroneous identifier. (sa2020denovovariants pages 2-4, sa2020denovovariants pages 5-6)

A source-supported summary quotation is: **“all had intellectual disability, motor and speech delay, facial dysmorphisms”**; the paper further separated them into two phenotypic groups according to opposite functional effects on BET proteins. (sa2020denovovariants pages 2-4)

## 2. Etiology

### Causal factors and genetic risk

The established cause is a heterozygous germline SPOP variant affecting protein function. In the foundational series, all variants were missense, de novo, and confirmed by Sanger sequencing:

- NM-reference transcript as reported: **c.73A>G, p.Thr25Ala**
- **c.248A>G, p.Tyr83Cys**
- **c.362G>A, p.Arg121Gln**
- **c.395G>T, p.Gly132Val**
- **c.412C>T, p.Arg138Cys**, recurrent in two unrelated individuals
- **c.430G>A, p.Asp144Asn**. (sa2020denovovariants pages 2-4)

These variants cluster in or near the SPOP MATH substrate-binding region, supporting altered substrate recognition rather than simple haploinsufficiency. Tyr83, Arg138, and Asp144 lie on a protein surface relevant to substrate interaction, whereas replacement of Gly132 by the larger valine was predicted to disturb local conformation. (sa2020denovovariants pages 4-5)

### Environmental, infectious, and lifestyle risk

No environmental toxin, infection, maternal exposure, diet, smoking, alcohol use, occupation, or lifestyle factor has been shown to cause or modify this Mendelian disorder. No gene–environment interaction has been reported. Likewise, no protective genetic allele, modifier gene, diet, exposure, or behavioral factor is established.

Family history is usually absent because reported variants were de novo. A negative family history therefore does not reduce suspicion. Conversely, family history could become relevant if an affected person reproduces or if parental germline mosaicism is present, although neither was quantified in the available series. (sa2020denovovariants pages 2-4)

## 3. Phenotypes

All frequency estimates below are based on the original seven-person series and are vulnerable to missing data and ascertainment bias.

### Core neurodevelopmental phenotype

- Intellectual disability: **7/7**; suggested HPO: *Intellectual disability* (**HP:0001249**).
- Global/motor developmental delay: **7/7**; suggested HPO: *Global developmental delay* (**HP:0001263**), *Delayed gross motor development*.
- Speech/language delay: **7/7**; suggested HPO: *Delayed speech and language development* (**HP:0000750**).
- Facial dysmorphism and congenital anomalies: **7/7**; use feature-specific HPO terms rather than a nonspecific dysmorphism term where possible. (sa2020denovovariants pages 2-4)

Developmental manifestations begin in infancy or early childhood and are chronic. Severity was variable, but sufficiently marked for all seven individuals to undergo clinical exome evaluation. The foundational cohort included children and adults aged approximately 4–20 years, demonstrating persistence rather than a transient delay. Available evidence does not establish neurodegeneration or regression. (sa2020denovovariants pages 4-4)

### Microcephaly/BET-reduction group

The p.Arg121Gln and p.Asp144Asn group comprised two individuals:

- Congenital microcephaly: **2/2**; HPO **HP:0000252**.
- Hearing loss: **2/2**; HPO *Hearing impairment* (**HP:0000365**), with a more specific conductive/sensorineural term if audiology permits.
- Craniofacial pattern: small forehead, highly arched eyebrows, blepharophimosis/narrow palpebral fissures, round face, prominent glabella, depressed nasal bridge, and micrognathia. Suggested HPO terms include *Blepharophimosis* (**HP:0000581**), *Highly arched eyebrow*, *Depressed nasal bridge* (**HP:0005280**), and *Micrognathia* (**HP:0000347**). (sa2020denovovariants pages 1-2, sa2020denovovariants pages 2-4)

### Macrocephaly/BET-increase group

The other five individuals showed:

- Macrocephaly or relative macrocephaly: **5/5**; HPO *Macrocephaly* (**HP:0000256**) or *Relative macrocephaly*.
- High/broad forehead, hypertelorism, long face, and widely spaced eyes; suggested HPO: *High forehead* (**HP:0000348**), *Broad forehead* (**HP:0000337**), *Hypertelorism* (**HP:0000316**), *Long face* (**HP:0000276**).
- Cardiovascular abnormalities: **4/4 evaluated**; HPO should be assigned at lesion level after echocardiography.
- Endocrine abnormalities: **3/4 evaluated**; assign the specific endocrine HPO term rather than a generic category.
- Sleep disturbance: **4/5**; HPO *Sleep disturbance* (**HP:0002360**).
- Epilepsy/seizures: approximately **2/4–2/5**, depending on the available-data denominator; HPO *Seizure* (**HP:0001250**) or epilepsy subtype after EEG classification.
- Failure to thrive and/or short stature: approximately **2/5**; HPO *Failure to thrive* (**HP:0001508**), *Short stature* (**HP:0004322**).
- Postnatal ventriculomegaly was reported in individuals 3 and 4; HPO *Ventriculomegaly* (**HP:0002119**). (sa2020denovovariants pages 2-4, sa2020denovovariants pages 5-6)

### Function and quality of life

Formal EQ-5D, SF-36, PROMIS, adaptive-function, or caregiver-burden data have not been published in the retrieved literature. Nonetheless, intellectual, motor, and speech impairment plausibly affect education, communication, independence, and daily living; hearing loss, epilepsy, sleep disturbance, and cardiac/endocrine disease add morbidity. These impacts are clinical inferences, not quantified syndrome-specific outcomes.

## 4. Genetic and molecular information

### Gene and protein

SPOP encodes a 374-amino-acid predominantly nuclear protein. It contains an N-terminal **MATH domain** that recognizes SPOP-binding-consensus motifs in substrates, a **BTB domain** that binds CUL3 and supports dimerization, a **BACK domain** supporting higher-order oligomerization, and a C-terminal nuclear-localization sequence. SPOP acts as the substrate adaptor in a CUL3–RBX1 E3 ubiquitin-ligase complex and can mediate degradative or nondegradative polyubiquitination. (zhang2023deregulationofspop pages 1-1, zhang2023deregulationofspop pages 2-3, ovalle2021speckletypepozadaptor pages 1-2)

The 2023 authoritative review states that SPOP is a **“substrate-binding adaptor of the CULLIN3/RING-box1 E3 ubiquitin ligase complex.”** Oligomerization permits multivalent substrate binding and formation of phase-separated SPOP/substrate condensates that increase ubiquitination efficiency. Documented substrates include BRD4, androgen receptor, SRC-3, TRIM24, PD-L1, 53BP1, GLP/G9a, c-MYC, and SENP7. These general substrate relationships are largely derived from cancer/cell biology, not neural tissue from affected patients. (zhang2023deregulationofspop pages 1-1)

Suggested annotations include GO *ubiquitin-protein transferase regulator activity*, *protein ubiquitination*, *proteasome-mediated ubiquitin-dependent protein catabolic process*, *regulation of transcription*, and cellular components *nucleus*, *nuclear speck*, and *biomolecular condensate*. Exact GO accessions should be validated against the current GO release before database ingestion.

### Variant consequences

- **p.Arg121Gln and p.Asp144Asn:** disease study classified these as gain-of-function toward substrate degradation; they reduced BRD2/3/4 abundance and were associated with microcephaly and hearing loss.
- **p.Thr25Ala, p.Tyr83Cys, p.Gly132Val, and p.Arg138Cys:** dominant-negative effects increased BET-protein abundance and were associated with macrocephaly and multisystem disease. (sa2020denovovariants pages 2-4)

Some retrieved secondary summaries reversed generic “loss-of-function/gain-of-function” labels while agreeing on the measured direction of BET abundance. For a knowledge base, the least ambiguous representation is therefore **“BET-reducing SPOP functional class”** versus **“dominant-negative, BET-increasing class,”** with the assay result stored separately from categorical labels. (sa2020denovovariants pages 2-4, sa2020denovovariants pages 5-6)

All six variants were germline in affected individuals, although de novo in origin. Somatic SPOP variants are well known in cancer, but somatic cancer mechanisms must not be conflated with this congenital disorder. No cancers had been reported in NSDVS in the later case-report literature. (sa2020denovovariants pages 5-6, olivareshuerta2026nabaissádevries pages 7-8)

### Classification and population frequency

The founding report regarded these de novo variants as disease causing based on recurrence, absence/rarity in reference populations, phenotype concordance, structural location, and functional assays. However, variant-by-variant current ClinVar assertions, review status, and gnomAD frequencies were not independently retrieved. The knowledge base should query the current ClinVar and gnomAD releases and should not assume that every missense change in SPOP is pathogenic.

No disease modifier, protective allele, founder variant, epigenetic signature, chromosomal rearrangement, or recurrent pathogenic copy-number alteration is established. A later C-terminal truncating variant reportedly produced a mixed phenotype, but the full report was unavailable and cannot be characterized reliably here.

## 5. Environmental information

No non-genetic etiologic factor is established. Toxins, radiation, pollution, occupation, nutrition, exercise, alcohol, tobacco, and pathogens are not implicated as causes or validated modifiers. The disorder is not infectious or transmissible. Routine healthy-lifestyle and immunization advice remains appropriate for general health but is not syndrome-specific prevention.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. A heterozygous germline SPOP missense variant **leads to** altered structure or substrate recognition in/near the MATH substrate-binding region. (sa2020denovovariants pages 4-5)
2. Altered substrate recognition **leads to** abnormal CUL3–RBX1-mediated ubiquitination and turnover of selected SPOP substrates. (zhang2023deregulationofspop pages 1-1, zhang2023deregulationofspop pages 2-3)
3. **Branch A:** p.Arg121Gln/p.Asp144Asn **lead to** lower BRD2/BRD3/BRD4 abundance; **Branch B:** dominant-negative p.Thr25Ala/p.Tyr83Cys/p.Gly132Val/p.Arg138Cys **lead to** higher BRD2/BRD3/BRD4 abundance. This step was demonstrated in cellular assays. (sa2020denovovariants pages 2-4)
4. Abnormal BET abundance **is inferred to lead to** altered chromatin-dependent transcription, cell-cycle timing, and neuronal differentiation; reduced BET levels were linked to accelerated cell-cycle progression and impaired neuronal differentiation, whereas increased levels were linked to increased differentiation. Direct confirmation in patient neural cells is lacking. (sa2020denovovariants pages 5-6)
5. Altered progenitor proliferation/differentiation **is inferred to result in** opposite effects on brain growth—microcephaly versus macrocephaly—and disrupted circuit development **results in** intellectual, motor, and speech disability. (sa2020denovovariants pages 5-6, sa2020denovovariants pages 2-4)
6. **Additional model-supported branch:** altered SPOP activity **may lead to** abnormal GLI3 turnover and Hedgehog-signal amplitude; this **can result in** neural-patterning and skeletal defects in mice, but this branch remains unproven in affected humans. (cai2016spoppromotesskeletal pages 4-5, cai2017spopregulatesgli3 pages 2-3, cai2017spopregulatesgli3 pages 3-7)
7. Multisystem developmental disturbance **results in** craniofacial, auditory, cardiac, endocrine, growth, sleep, seizure, and other congenital manifestations. (sa2020denovovariants pages 2-4)

### Molecular and cellular detail

SPOP oligomerization through BTB/BACK domains creates multivalent complexes and can promote liquid–liquid phase separation with substrates. This provides a biophysical mechanism by which relatively subtle substrate-binding changes could alter ubiquitination efficiency. Whether condensate properties are altered by NSDVS alleles has not been tested directly. (zhang2023deregulationofspop pages 1-1, ovalle2021speckletypepozadaptor pages 2-5)

BET proteins are chromatin readers involved in transcription and cell-cycle regulation. The human study’s BET-protein measurements provide the most direct disease-specific molecular readout. No patient-brain transcriptomics, neural proteomics, metabolomics, lipidomics, single-cell sequencing, spatial transcriptomics, or multi-omics dataset was identified. (sa2020denovovariants pages 5-6)

In mice, Spop directly regulates GLI3 abundance. Spop loss increases full-length and repressor GLI3 in spinal cord; uncomplicated mutants can retain normal dorsoventral patterning, whereas sensitized Gli/Sufu backgrounds show marked changes in Shh response and ventral cell fates. This context dependence cautions against a simplistic “SPOP activates” or “SPOP inhibits” Hedgehog model. (cai2017spopregulatesgli3 pages 9-9, cai2017spopregulatesgli3 pages 2-3, cai2017spopregulatesgli3 pages 3-7)

Suggested biological-process GO labels include neural precursor-cell proliferation, neuron differentiation, chromatin organization, regulation of cell cycle, protein polyubiquitination, Hedgehog signaling, spinal-cord patterning, chondrocyte differentiation, and osteoblast differentiation. Candidate Cell Ontology labels, based mainly on inferred targets and mouse evidence, include neural stem/progenitor cell, neuron, oligodendrocyte precursor cell, floor-plate cell, V3 interneuron, chondrocyte, hypertrophic chondrocyte, osteoblast, and limb mesenchymal cell. These are mechanistic annotations, not proven patient-cell lesions.

## 7. Anatomical structures affected

### Organ and system level

- Primary: central nervous system/brain, with abnormal brain growth and neurodevelopment.
- Sensory: auditory system; vision abnormalities have appeared in case-report tables but were not quantified in the founding cohort.
- Craniofacial structures.
- Cardiovascular and endocrine systems, especially in the macrocephaly group.
- Growth and skeletal system; direct skeletal mechanisms are strongest in mouse models.
- Sleep and seizure networks as functional CNS manifestations. (sa2020denovovariants pages 2-4, cai2016spoppromotesskeletal pages 1-2)

Suggested UBERON labels include brain (**UBERON:0000955**), cerebral cortex (**UBERON:0000956**), spinal cord (**UBERON:0002240**), inner ear (**UBERON:0001846**), heart (**UBERON:0000948**), endocrine system, craniofacial skeleton, cartilage, and bone tissue. Ventriculomegaly implies ventricular-system involvement; no consistent lateralization has been reported. (sa2020denovovariants pages 5-6)

### Subcellular level

The principal compartment is the nucleus, including nuclear speckles and SPOP/substrate condensates. The ubiquitin–proteasome system is the key biochemical machinery. SPOP’s nuclear localization sequence supports this localization. (zhang2023deregulationofspop pages 1-1, ovalle2021speckletypepozadaptor pages 1-2)

## 8. Temporal development

The disorder is congenital/developmental. Head-size abnormality and congenital anomalies may be evident prenatally or at birth, whereas developmental, speech, motor, seizure, sleep, and behavioral manifestations become apparent through infancy and childhood. Individuals aged up to 20 years were reported, supporting a chronic lifelong course. (sa2020denovovariants pages 4-4)

No validated clinical stages, progression rate, remission pattern, or critical therapeutic window has been defined. Available evidence is more consistent with a static developmental encephalopathy than demonstrated progressive neurodegeneration, but longitudinal data are inadequate. Early childhood is nevertheless a practical intervention window for hearing correction, developmental therapy, communication support, seizure treatment, nutrition, and cardiac/endocrine surveillance.

## 9. Inheritance and population

The expected inheritance pattern is **autosomal dominant**. All foundational cases were de novo; thus, most parents have a low recurrence risk, but recurrence is not zero because parental germline mosaicism cannot be excluded. An affected individual would theoretically have a 50% chance of transmitting the variant in each pregnancy, subject to reproductive fitness and uncertain penetrance. (sa2020denovovariants pages 2-4)

Penetrance appears high for the functionally established alleles, because every identified carrier was affected, but the sample is too small to estimate penetrance. Expressivity is variable and strongly related to functional class. Anticipation, founder effects, consanguinity, carrier frequency, and population-specific enrichment have not been demonstrated.

No incidence or prevalence per 100,000 is available. The original cohort’s sex distribution was approximately four females and three males, but seven cases cannot establish a sex ratio. Cases from different diagnostic settings suggest no demonstrated ethnic or geographic restriction. (sa2020denovovariants pages 4-4)

## 10. Diagnostics

### Clinical recognition

Consider SPOP testing in a child with global developmental delay/intellectual disability, marked speech and motor delay, dysmorphic features, and congenital anomalies, especially when either of the following patterns is present:

1. Congenital microcephaly plus hearing impairment and blepharophimosis-like craniofacial features.
2. Macrocephaly/relative macrocephaly plus hypertelorism/high forehead, cardiac or endocrine anomalies, sleep disturbance, epilepsy, or abnormal growth. (sa2020denovovariants pages 2-4)

No consensus clinical diagnostic criteria exist. Phenotype alone is insufficient because many chromatinopathies and monogenic NDDs overlap.

### Genetic testing strategy

1. **First choice:** trio whole-exome or whole-genome sequencing with SNV/indel and copy-number analysis. All foundational diagnoses were made through clinical exome approaches and de novo status was confirmed by Sanger sequencing. (sa2020denovovariants pages 2-4)
2. A comprehensive NDD/intellectual-disability panel that includes SPOP is reasonable where exome/genome sequencing is unavailable.
3. Single-gene SPOP sequencing is appropriate when the phenotype is highly suggestive or for familial confirmation.
4. Confirm candidate variants by an orthogonal method and test both parents to establish de novo status.
5. Interpret missense variants using ACMG/AMP criteria, phenotype concordance, population frequency, domain location, computational/structural evidence, and—where available—functional evidence. Do not classify a novel SPOP missense variant solely from gene-level association.

WGS may detect noncoding and structural variants missed by WES, but no syndrome-specific incremental yield is known. CMA is useful in unexplained syndromic NDD but will generally miss the pathogenic single-nucleotide substitutions reported here. Karyotyping and FISH are not targeted tests for this disorder. Mitochondrial and repeat-expansion testing are not indicated specifically unless the differential diagnosis suggests them.

### Phenotype-directed assessment

Recommended baseline characterization, based on reported manifestations rather than formal guidelines, includes developmental and neuropsychological assessment; speech/language and augmentative-communication evaluation; audiology; ophthalmology; neurologic examination and EEG if seizures are suspected; brain MRI when macrocephaly, microcephaly, seizures, focal findings, or regression warrant it; echocardiography/ECG; growth and nutrition evaluation; endocrine testing guided by symptoms; and skeletal assessment where clinically indicated. A 2026 case report explicitly noted that follow-up guidelines had not been established. (olivareshuerta2026nabaissádevries pages 7-8, olivareshuerta2026nabaissádevries pages 8-9)

### Differential diagnosis

The differential includes other monogenic chromatinopathies and syndromic NDDs with abnormal head size, including disorders involving CUL3 ubiquitin-ligase adaptors or BET/chromatin regulation; PTEN-related macrocephaly, DNMT3A-related Tatton-Brown–Rahman syndrome, SETD2/Luscan–Lumish syndrome, KBG syndrome, Cornelia de Lange spectrum, and microcephaly-hearing-loss syndromes. Distinction depends on molecular testing and the direction of head-size change, hearing phenotype, characteristic face, and multisystem findings.

No validated biochemical, circulating, proteomic, metabolomic, methylation, or imaging biomarker exists. BET abundance was a research functional readout, not a clinical assay. No SPOP-specific episignature was demonstrated in the retrieved evidence.

## 11. Outcome and prognosis

No survival curve, mortality rate, life-expectancy estimate, five- or ten-year outcome, or disease-specific cause-of-death data exist. Survival into young adulthood was observed in the initial cohort. There is no evidence that germline NSDVS itself causes malignancy, despite the important role of somatic SPOP variants in cancer. (sa2020denovovariants pages 4-4, olivareshuerta2026nabaissádevries pages 7-8)

Expected morbidity is driven by lifelong intellectual, speech, and motor impairment and by variable hearing loss, epilepsy, sleep disorder, growth difficulty, cardiac disease, and endocrine disease. Recovery to typical neurodevelopment has not been documented. Functional gains from supportive therapy are plausible but have not been quantified. No prognostic molecular biomarker is validated; functional variant class and head-size phenotype are the leading candidate predictors, based on seven individuals only. (sa2020denovovariants pages 2-4)

## 12. Treatment

### Current management

There is no approved or investigational syndrome-specific pharmacotherapy and no evidence-based treatment algorithm. Management is individualized:

- early developmental intervention;
- physical therapy—NCIt concept: *Physical Therapy*;
- occupational therapy—NCIt: *Occupational Therapy*;
- speech/language and augmentative-communication therapy—NCIt: *Speech Therapy*;
- hearing aids, cochlear evaluation, or ENT treatment according to audiology;
- standard antiseizure medication selected by seizure type;
- sleep-hygiene and behavioral sleep treatment, with medication only when clinically indicated;
- nutrition and feeding support;
- standard cardiology and endocrine treatment for identified lesions;
- educational, behavioral, psychosocial, and family support.

These interventions are extrapolated from standard management of the component manifestations; syndrome-specific response rates and adverse-event data do not exist. A later case report recommends coordinated neurology, cardiology, ophthalmology, and otorhinolaryngology care while explicitly acknowledging the absence of guidelines. (olivareshuerta2026nabaissádevries pages 7-8, olivareshuerta2026nabaissádevries pages 8-9)

### Advanced and experimental therapy

No SPOP-directed gene replacement, editing, ASO, siRNA, mRNA, cell therapy, immunotherapy, or BET-modulating treatment has reached clinical testing for NSDVS. Although opposite BET abnormalities suggest a future genotype-specific therapeutic strategy, systemic BET inhibition or enhancement would have broad transcriptional and developmental effects and cannot presently be recommended. Cancer-directed SPOP or BET agents are not interchangeable with treatment for a germline developmental disorder. (sa2020denovovariants pages 5-6, zhang2023deregulationofspop pages 10-11)

ClinicalTrials.gov searches using SPOP-related NDD and Nabais Sá–de Vries terminology yielded no relevant interventional studies or NCT identifiers.

## 13. Prevention

Primary prevention through environmental or lifestyle modification is not available. Vaccination does not prevent this genetic disorder.

The actionable prevention framework is reproductive:

- genetic counseling after molecular diagnosis;
- parental testing and discussion of residual germline-mosaicism risk;
- prenatal diagnosis through chorionic-villus sampling or amniocentesis for a known familial variant;
- preimplantation genetic testing for monogenic disease where desired and legally available;
- cascade testing if a parent or other relative is found to carry the variant.

Population carrier screening and newborn screening are not justified because the disorder is exceptionally rare, primarily de novo, and lacks a validated population assay or presymptomatic disease-modifying treatment. Secondary/tertiary prevention consists of early recognition and treatment of hearing loss, seizures, feeding/growth problems, cardiac abnormalities, endocrine disease, sleep problems, and developmental needs.

## 14. Other species and natural disease

No naturally occurring SPOP-related neurodevelopmental syndrome was found in companion animals, livestock, or wildlife. There is no zoonotic potential or cross-species transmission.

Orthologous systems include mouse **Spop**, Drosophila **hib/roadkill**, and corresponding vertebrate SPOP proteins. Conservation of CUL3-adaptor control of GLI/Cubitus interruptus supports comparative relevance, but species and tissue context alter pathway output. (cai2017spopregulatesgli3 pages 9-9, cai2017spopregulatesgli3 pages 2-3)

Suggested taxonomy identifiers are *Homo sapiens* NCBI Taxon 9606, *Mus musculus* 10090, *Drosophila melanogaster* 7227, and *Xenopus laevis* 8355. Ortholog-specific NCBI Gene identifiers should be validated directly in the current NCBI Gene record.

## 15. Model organisms

### Mouse models

Spop-null and tissue-conditional mouse models are available as experimental rather than natural-disease models. Spop loss can cause neonatal lethality, delayed ossification, enlarged fontanelles, brachydactyly, osteopenia, impaired hypertrophic-chondrocyte and osteoblast differentiation, and occasional exencephaly or spina bifida. (cai2017spopregulatesgli3 pages 2-3, cai2016spoppromotesskeletal pages 1-2, cai2016spoppromotesskeletal pages 2-4)

In skeletal tissue, Spop loss increased GLI3 repressor, reduced Ihh targets such as Ptch1, and compromised chondrocyte hypertrophy. Reducing Gli3 dosage rescued ossification, brachydactyly, and osteopenia, providing unusually strong genetic evidence that GLI3 mediates this model phenotype. (cai2016spoppromotesskeletal pages 4-5, cai2016spoppromotesskeletal pages 5-5, cai2016spoppromotesskeletal pages 1-1)

In spinal cord, Spop loss increased GLI3 but did not by itself consistently disturb dorsoventral patterning. Severe ventralization emerged in sensitized Sufu/Gli genetic backgrounds, demonstrating that SPOP’s effect depends on the broader Hedgehog regulatory state. (cai2017spopregulatesgli3 pages 9-9, cai2017spopregulatesgli3 pages 2-3, cai2017spopregulatesgli3 pages 3-7)

### Drosophila and Xenopus

Drosophila HIB/Roadkill targets Cubitus interruptus for Cul3-directed proteolysis. Xenopus experiments also support conserved SPOP-mediated GLI turnover. These models are useful for pathway dissection and variant-function assays but do not reproduce the human craniofacial, cognitive, speech, or behavioral syndrome. (cai2017spopregulatesgli3 pages 9-9)

### Principal limitations and priorities

Existing models mainly represent complete or conditional loss of Spop, whereas human disease is caused predominantly by heterozygous missense alleles with substrate-specific gain-of-function or dominant-negative effects. No retrieved mouse, zebrafish, fly, organoid, or iPSC model knocked in the six foundational human alleles and measured cognition, neuronal differentiation, or BET abundance in disease-relevant neural cells.

High-priority models therefore include allele-specific knock-in mice, patient-derived iPSCs differentiated into neural progenitors and cortical neurons, and cerebral organoids. Appropriate readouts include SPOP condensate dynamics; BRD2/3/4 stability; ubiquitin proteomics; cell-cycle length; neuronal differentiation; neural-network activity; GLI3 processing; Hedgehog response; and rescue with allele-specific normalization of BET abundance.

## Recent-development assessment and expert interpretation

The 2023 molecular review strengthened the general mechanistic framework by emphasizing SPOP’s multivalent substrate recognition, oligomerization, phase separation, and broad control of transcriptional and genome-integrity proteins. The 2024 chromatinopathy literature places SPOP-related disease in the expanding category of developmental disorders caused by disturbed chromatin-state regulation, but no validated SPOP-specific DNA-methylation episignature was found. (zhang2023deregulationofspop pages 1-1)

The most important expert-level conclusion is that NSDVS should not be modeled as generic SPOP loss. The human alleles have **directionally opposite, substrate-specific effects**, and categorical “gain-of-function” versus “loss-of-function” terminology can obscure the directly measured phenotype. Database representation should preserve: variant, protein domain, substrate tested, direction of substrate-abundance change, assay system, and clinical subtype as separate fields. (sa2020denovovariants pages 2-4, sa2020denovovariants pages 5-6)

## Evidence limitations

The evidence base is exceptionally small. Most clinical frequencies derive from seven individuals reported in 2020; several later case reports were unavailable in full text, and the only retrieved recent management statement was from a 2026 case report. No robust 2023–2024 disease-specific cohort, natural-history study, registry, trial, omics study, or epidemiologic analysis was identified. Consequently, absence of evidence should not be interpreted as proof that a feature never occurs. All ontology mappings beyond explicitly established HPO concepts should be validated against current ontology releases before knowledge-base import.

References

1. (sa2020denovovariants pages 2-4): Maria J. Nabais Sá, Geniver El Tekle, Arjan P.M. de Brouwer, Sarah L. Sawyer, Daniela del Gaudio, Michael J. Parker, Farah Kanani, Marie-José H. van den Boogaard, Koen van Gassen, Margot I. Van Allen, Klaas Wierenga, Gabriela Purcarin, Ellen Roy Elias, Amber Begtrup, Jennifer Keller-Ramey, Tiziano Bernasocchi, Laurens van de Wiel, Christian Gilissen, Hanka Venselaar, Rolph Pfundt, Lisenka E.L.M. Vissers, Jean-Philippe P. Theurillat, and Bert B.A. de Vries. De novo variants in spop cause two clinically distinct neurodevelopmental disorders. Mar 2020. URL: https://doi.org/10.1016/j.ajhg.2020.02.001, doi:10.1016/j.ajhg.2020.02.001. This article has 21 citations.

2. (sa2020denovovariants pages 1-2): Maria J. Nabais Sá, Geniver El Tekle, Arjan P.M. de Brouwer, Sarah L. Sawyer, Daniela del Gaudio, Michael J. Parker, Farah Kanani, Marie-José H. van den Boogaard, Koen van Gassen, Margot I. Van Allen, Klaas Wierenga, Gabriela Purcarin, Ellen Roy Elias, Amber Begtrup, Jennifer Keller-Ramey, Tiziano Bernasocchi, Laurens van de Wiel, Christian Gilissen, Hanka Venselaar, Rolph Pfundt, Lisenka E.L.M. Vissers, Jean-Philippe P. Theurillat, and Bert B.A. de Vries. De novo variants in spop cause two clinically distinct neurodevelopmental disorders. Mar 2020. URL: https://doi.org/10.1016/j.ajhg.2020.02.001, doi:10.1016/j.ajhg.2020.02.001. This article has 21 citations.

3. (sa2020denovovariants pages 5-6): Maria J. Nabais Sá, Geniver El Tekle, Arjan P.M. de Brouwer, Sarah L. Sawyer, Daniela del Gaudio, Michael J. Parker, Farah Kanani, Marie-José H. van den Boogaard, Koen van Gassen, Margot I. Van Allen, Klaas Wierenga, Gabriela Purcarin, Ellen Roy Elias, Amber Begtrup, Jennifer Keller-Ramey, Tiziano Bernasocchi, Laurens van de Wiel, Christian Gilissen, Hanka Venselaar, Rolph Pfundt, Lisenka E.L.M. Vissers, Jean-Philippe P. Theurillat, and Bert B.A. de Vries. De novo variants in spop cause two clinically distinct neurodevelopmental disorders. Mar 2020. URL: https://doi.org/10.1016/j.ajhg.2020.02.001, doi:10.1016/j.ajhg.2020.02.001. This article has 21 citations.

4. (cai2016spoppromotesskeletal pages 4-5): Hongchen Cai and Aimin Liu. Spop promotes skeletal development and homeostasis by positively regulating ihh signaling. Proceedings of the National Academy of Sciences, 113:14751-14756, Dec 2016. URL: https://doi.org/10.1073/pnas.1612520114, doi:10.1073/pnas.1612520114. This article has 79 citations and is from a highest quality peer-reviewed journal.

5. (olivareshuerta2026nabaissádevries pages 7-8): Oscar Olivares-Huerta, Dulce María Castro-Coyotl, Israel Enrique Crisanto-López, Jonathan Cervantes-Larios, Renata Ochoa-Precoma, Blanca Frisia Morales-López, Itzel Alejandra Trejo-Toscano, and Daniela Juárez-Melchor. Nabais sá-de vries syndrome type 1 in a mexican girl: a case report. Cureus, Apr 2026. URL: https://doi.org/10.7759/cureus.107064, doi:10.7759/cureus.107064. This article has 0 citations.

6. (olivareshuerta2026nabaissádevries pages 8-9): Oscar Olivares-Huerta, Dulce María Castro-Coyotl, Israel Enrique Crisanto-López, Jonathan Cervantes-Larios, Renata Ochoa-Precoma, Blanca Frisia Morales-López, Itzel Alejandra Trejo-Toscano, and Daniela Juárez-Melchor. Nabais sá-de vries syndrome type 1 in a mexican girl: a case report. Cureus, Apr 2026. URL: https://doi.org/10.7759/cureus.107064, doi:10.7759/cureus.107064. This article has 0 citations.

7. (sa2020denovovariants pages 4-5): Maria J. Nabais Sá, Geniver El Tekle, Arjan P.M. de Brouwer, Sarah L. Sawyer, Daniela del Gaudio, Michael J. Parker, Farah Kanani, Marie-José H. van den Boogaard, Koen van Gassen, Margot I. Van Allen, Klaas Wierenga, Gabriela Purcarin, Ellen Roy Elias, Amber Begtrup, Jennifer Keller-Ramey, Tiziano Bernasocchi, Laurens van de Wiel, Christian Gilissen, Hanka Venselaar, Rolph Pfundt, Lisenka E.L.M. Vissers, Jean-Philippe P. Theurillat, and Bert B.A. de Vries. De novo variants in spop cause two clinically distinct neurodevelopmental disorders. Mar 2020. URL: https://doi.org/10.1016/j.ajhg.2020.02.001, doi:10.1016/j.ajhg.2020.02.001. This article has 21 citations.

8. (zhang2023deregulationofspop pages 1-1): Hui Zhang, Xiaofeng Jin, and Haojie Huang. Deregulation of spop in cancer. Cancer research, 83:489-499, Dec 2023. URL: https://doi.org/10.1158/0008-5472.can-22-2801, doi:10.1158/0008-5472.can-22-2801. This article has 73 citations and is from a highest quality peer-reviewed journal.

9. (zhang2023deregulationofspop pages 2-3): Hui Zhang, Xiaofeng Jin, and Haojie Huang. Deregulation of spop in cancer. Cancer research, 83:489-499, Dec 2023. URL: https://doi.org/10.1158/0008-5472.can-22-2801, doi:10.1158/0008-5472.can-22-2801. This article has 73 citations and is from a highest quality peer-reviewed journal.

10. (ovalle2021speckletypepozadaptor pages 2-5): Wendy Johana Montero Ovalle, María Carolina Sanabria Salas, and Martha Lucia Serrano Lopez. Speckle-type poz adaptor protein (spop) and its role in cancer. Sep 2021. URL: https://doi.org/10.35509/01239015.717, doi:10.35509/01239015.717. This article has 1 citations.

11. (ovalle2021speckletypepozadaptor pages 1-2): Wendy Johana Montero Ovalle, María Carolina Sanabria Salas, and Martha Lucia Serrano Lopez. Speckle-type poz adaptor protein (spop) and its role in cancer. Sep 2021. URL: https://doi.org/10.35509/01239015.717, doi:10.35509/01239015.717. This article has 1 citations.

12. (cai2017spopregulatesgli3 pages 9-9): Hongchen Cai and Aimin Liu. Spop regulates gli3 activity and shh signaling in dorsoventral patterning of the mouse spinal cord. Developmental biology, 432 1:72-85, Dec 2017. URL: https://doi.org/10.1016/j.ydbio.2017.04.002, doi:10.1016/j.ydbio.2017.04.002. This article has 36 citations and is from a peer-reviewed journal.

13. (cai2017spopregulatesgli3 pages 2-3): Hongchen Cai and Aimin Liu. Spop regulates gli3 activity and shh signaling in dorsoventral patterning of the mouse spinal cord. Developmental biology, 432 1:72-85, Dec 2017. URL: https://doi.org/10.1016/j.ydbio.2017.04.002, doi:10.1016/j.ydbio.2017.04.002. This article has 36 citations and is from a peer-reviewed journal.

14. (cai2017spopregulatesgli3 pages 3-7): Hongchen Cai and Aimin Liu. Spop regulates gli3 activity and shh signaling in dorsoventral patterning of the mouse spinal cord. Developmental biology, 432 1:72-85, Dec 2017. URL: https://doi.org/10.1016/j.ydbio.2017.04.002, doi:10.1016/j.ydbio.2017.04.002. This article has 36 citations and is from a peer-reviewed journal.

15. (cai2016spoppromotesskeletal pages 5-5): Hongchen Cai and Aimin Liu. Spop promotes skeletal development and homeostasis by positively regulating ihh signaling. Proceedings of the National Academy of Sciences, 113:14751-14756, Dec 2016. URL: https://doi.org/10.1073/pnas.1612520114, doi:10.1073/pnas.1612520114. This article has 79 citations and is from a highest quality peer-reviewed journal.

16. (cai2016spoppromotesskeletal pages 1-1): Hongchen Cai and Aimin Liu. Spop promotes skeletal development and homeostasis by positively regulating ihh signaling. Proceedings of the National Academy of Sciences, 113:14751-14756, Dec 2016. URL: https://doi.org/10.1073/pnas.1612520114, doi:10.1073/pnas.1612520114. This article has 79 citations and is from a highest quality peer-reviewed journal.

17. (cai2016spoppromotesskeletal pages 1-2): Hongchen Cai and Aimin Liu. Spop promotes skeletal development and homeostasis by positively regulating ihh signaling. Proceedings of the National Academy of Sciences, 113:14751-14756, Dec 2016. URL: https://doi.org/10.1073/pnas.1612520114, doi:10.1073/pnas.1612520114. This article has 79 citations and is from a highest quality peer-reviewed journal.

18. (cai2016spoppromotesskeletal pages 2-4): Hongchen Cai and Aimin Liu. Spop promotes skeletal development and homeostasis by positively regulating ihh signaling. Proceedings of the National Academy of Sciences, 113:14751-14756, Dec 2016. URL: https://doi.org/10.1073/pnas.1612520114, doi:10.1073/pnas.1612520114. This article has 79 citations and is from a highest quality peer-reviewed journal.

19. (sa2020denovovariants pages 4-4): Maria J. Nabais Sá, Geniver El Tekle, Arjan P.M. de Brouwer, Sarah L. Sawyer, Daniela del Gaudio, Michael J. Parker, Farah Kanani, Marie-José H. van den Boogaard, Koen van Gassen, Margot I. Van Allen, Klaas Wierenga, Gabriela Purcarin, Ellen Roy Elias, Amber Begtrup, Jennifer Keller-Ramey, Tiziano Bernasocchi, Laurens van de Wiel, Christian Gilissen, Hanka Venselaar, Rolph Pfundt, Lisenka E.L.M. Vissers, Jean-Philippe P. Theurillat, and Bert B.A. de Vries. De novo variants in spop cause two clinically distinct neurodevelopmental disorders. Mar 2020. URL: https://doi.org/10.1016/j.ajhg.2020.02.001, doi:10.1016/j.ajhg.2020.02.001. This article has 21 citations.

20. (zhang2023deregulationofspop pages 10-11): Hui Zhang, Xiaofeng Jin, and Haojie Huang. Deregulation of spop in cancer. Cancer research, 83:489-499, Dec 2023. URL: https://doi.org/10.1158/0008-5472.can-22-2801, doi:10.1158/0008-5472.can-22-2801. This article has 73 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](SPOP-Related_Neurodevelopmental_Disorder-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 8 |
| On topic | 1 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 23 |
| Resolved | 23 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |

Every term resolved, and every label the report gave matched.