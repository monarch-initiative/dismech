---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-02T15:07:39.833662'
end_time: '2026-09-02T15:17:40.837205'
duration_seconds: 601.0
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Developmental and Epileptic Encephalopathy 81
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 19
reference_validation:
  total_references: 5
  verified: 5
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 5
  on_topic: 3
  validator_version: 0.2.1
term_validation:
  total_terms: 47
  verified: 47
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
  path: Developmental_And_Epileptic_Encephalopathy_81-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Developmental and Epileptic Encephalopathy 81
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Developmental and Epileptic Encephalopathy 81** covering all of the
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
- **Disease Name:** Developmental and Epileptic Encephalopathy 81
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Developmental and Epileptic Encephalopathy 81** covering all of the
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


# Developmental and Epileptic Encephalopathy 81 (DEE81): Disease-Characteristics Report

## Executive summary and evidence limits

Developmental and epileptic encephalopathy 81 (DEE81) is an exceptionally rare, autosomal-recessive neurodevelopmental disorder caused by biallelic pathogenic variants in **DMXL2**. The defining report described six children—three sibling pairs from three unrelated families—with neonatal-onset Ohtahara syndrome, persistent suppression-burst EEG, profound developmental failure, hypomyelination, progressive cerebral volume loss, sensorineural deafness, and high childhood mortality. The mechanistic lesion is loss of rabconnectin-3α/DMXL2 function, disrupting V-ATPase regulation, endolysosomal homeostasis, autophagy, neurite development, and synapse formation. The evidence base remains dominated by this small 2019 case series; therefore, frequencies below are descriptive of that cohort, not population estimates. (esposito2019biallelicdmxl2mutations pages 1-2, esposito2019biallelicdmxl2mutations pages 6-7, esposito2019biallelicdmxl2mutations pages 5-6)

The principal primary source is Esposito et al., *Brain*, published December 2019, PMID **31688942**, DOI [10.1093/brain/awz326](https://doi.org/10.1093/brain/awz326). Its abstract states: **“Impaired lysosomal function and autophagy caused by biallelic DMXL2 mutations affect neuronal development and synapse formation and result in Ohtahara syndrome with profound developmental impairment and reduced life expectancy.”** (esposito2019biallelicdmxl2mutations pages 1-2, OpenTargets Search: -DMXL2)

| Domain | DEE81 evidence snapshot | Evidence status |
|---|---|---|
| Identity | Developmental and epileptic encephalopathy 81 (DEE81); OMIM **618663**; severe progressive Ohtahara/early-infantile DEE phenotype. A disease-specific MONDO, Orphanet, ICD-10/11, or MeSH identifier was not established in the retrieved evidence. | Human disease-level evidence (esposito2019biallelicdmxl2mutations pages 1-2, OpenTargets Search: -DMXL2) |
| Causal gene / inheritance | **DMXL2** (Dmx-like 2; rabconnectin-3α); biallelic loss-of-function or severe hypomorphic variants; **autosomal recessive**. Parents in the three foundational families were heterozygous and clinically unaffected. | Human segregation and functional evidence (esposito2019biallelicdmxl2mutations pages 6-7, esposito2019biallelicdmxl2mutations pages 13-14) |
| Known DEE81 variants | Family 1: compound heterozygous **c.5135C>T (p.Ala1712Val)** and **c.4478C>G (p.Ser1493\*)**; Family 2: homozygous **c.4478C>A (p.Ser1493\*)**; Family 3: homozygous **c.7518-1G>A**, causing exon-31 skipping and **p.Trp2507Argfs\*4** (also rendered p.Trp2508Argfs\*4 in one passage). All were absent from gnomAD in the original report. | Human molecular evidence (esposito2019biallelicdmxl2mutations pages 1-2, esposito2019biallelicdmxl2mutations pages 6-7, esposito2019biallelicdmxl2mutations pages 5-6) |
| Foundational cohort size | **6 affected children**, comprising **3 sibling pairs from 3 unrelated families**. No sufficiently large DEE81-specific natural-history cohort was identified. | Human case series (esposito2019biallelicdmxl2mutations pages 1-2) |
| Onset, EEG, and seizures | Manifestation began on the **first day or first days of life**. All six had persistent/continuous **suppression-burst EEG** consistent with Ohtahara syndrome. Seizures were predominantly tonic, less often myoclonic, with occasional focal seizures; epilepsy was described as intractable. Exact patient-level seizure frequencies and treatment-response rates are unknown. | Human clinical evidence (esposito2019biallelicdmxl2mutations pages 1-2, esposito2019biallelicdmxl2mutations pages 5-6) |
| Development and motor function | **6/6** had profound developmental impairment, hypotonia, and quadriparesis; **0/6** acquired developmental, communicative, or motor skills after birth. | Human clinical evidence (esposito2019biallelicdmxl2mutations pages 1-2, esposito2019biallelicdmxl2mutations pages 5-6) |
| Brain MRI | Early MRI showed **thin/hypoplastic corpus callosum and hypomyelination in 6/6**. Two children had a simplified gyral pattern. Serial MRI in **3 patients**, performed **9–21 months** later, showed progressive grey- and white-matter volume loss/brain shrinkage with leukoencephalopathy. | Human imaging evidence (esposito2019biallelicdmxl2mutations pages 8-10, esposito2019biallelicdmxl2mutations pages 5-6) |
| Extra-neurologic findings | Sensorineural hearing loss and dysmorphic features occurred in **6/6**. Mild peripheral polyneuropathy occurred in **4/4 evaluated children** from Families 1 and 2; nerve-conduction testing was not reported for Family 3. Respiratory/systemic complications contributed to deaths. Detailed organ-specific frequencies and standardized quality-of-life measurements are unknown. | Human clinical evidence (esposito2019biallelicdmxl2mutations pages 5-6) |
| Mortality / prognosis | **5/6 (83%)** died before age 9; one child was alive at 15 months at reporting. Cause-specific survival curves, median survival, and treated-versus-untreated life expectancy are unknown. | Human case-series evidence (esposito2019biallelicdmxl2mutations pages 1-2, esposito2019biallelicdmxl2mutations pages 5-6) |
| Mechanism | DMXL2 deficiency disrupts V-ATPase regulation and endolysosomal homeostasis, producing defective degradation and autophagy: reduced LC3/LC3-II, p62 and polyubiquitinated-protein accumulation, and abnormal autolysosomes. Patient fibroblast abnormalities were rescued by wild-type DMXL2. Dmxl2-silenced mouse hippocampal neurons showed impaired neurite growth and synaptic loss; the link from these cellular defects to seizures is strongly supported but partly inferential. | Human cells, rescue experiments, and mouse-neuron model (esposito2019biallelicdmxl2mutations pages 6-7, esposito2019biallelicdmxl2mutations pages 10-11, falace2024vatpasedysfunctionin pages 8-9, esposito2019biallelicdmxl2mutations pages 11-12) |
| Diagnostics | Molecular confirmation requires identification of pathogenic/likely pathogenic variants on both **DMXL2** alleles with parental phasing. Exome/genome sequencing or a comprehensive epilepsy/DEE panel with copy-number analysis is appropriate; EEG, brain MRI, hearing assessment, developmental evaluation, and neuropathy surveillance define extent. No validated DEE81-specific biochemical biomarker or formal diagnostic criteria are known. | Disease-specific discovery plus general epilepsy-genomics evidence (esposito2019biallelicdmxl2mutations pages 1-2, guerrini2023developmentalandepileptic pages 3-4, grew2024yieldandutility pages 1-2) |
| Treatment / trials | No disease-modifying therapy, genotype-specific drug, or relevant registered DMXL2/DEE81 interventional trial was identified. Care is supportive and phenotype-directed; no reproducible DEE81-specific antiseizure-drug response rate is available. V-ATPase, lysosomal-acidification, and autophagy modulation remain preclinical therapeutic concepts. | Evidence gap and mechanistic review (falace2024vatpasedysfunctionin pages 8-9) |
| Epidemiology | Population prevalence, incidence, carrier frequency, sex ratio, founder effects, and geographic-risk estimates are **unknown**. Published evidence is limited principally to three families, including consanguineous Israeli-Arab and Turkish families and a non-consanguineous Italian-Brazilian family; this does not establish population enrichment. | Very limited human case-series evidence (esposito2019biallelicdmxl2mutations pages 5-6) |


*Table: A compact evidence map of DMXL2-related DEE81, separating quantified observations from currently unknown epidemiologic, diagnostic, and therapeutic information.*

## 1. Disease information

### Definition

DEE81 is a severe early-infantile developmental and epileptic encephalopathy in which a primary prenatal/neonatal neurodevelopmental defect and severe epileptic activity both contribute to neurological dysfunction. In the original cohort, disease was recognizable as **Ohtahara syndrome**, now generally termed early-infantile developmental and epileptic encephalopathy with suppression-burst. DEEs more broadly are defined by early, often severe seizures and EEG abnormalities superimposed on developmental impairment, with developmental pathology and epileptic activity potentially making independent and interacting contributions. (esposito2019biallelicdmxl2mutations pages 1-2, guerrini2023developmentalandepileptic pages 3-4)

### Identifiers and names

- **Preferred name:** Developmental and epileptic encephalopathy 81
- **Abbreviation:** DEE81
- **OMIM:** **618663**
- **Causal gene:** **DMXL2**, OMIM gene **612186**
- **Synonyms:** early infantile epileptic encephalopathy 81; EIEE81; DMXL2-related developmental and epileptic encephalopathy; DMXL2-related Ohtahara syndrome; progressive Ohtahara syndrome due to biallelic DMXL2 variants.
- **MONDO:** a disease-specific DEE81 identifier was not established in the retrieved evidence. Broader applicable concepts include genetic developmental and epileptic encephalopathy (**MONDO:0100062**) and early-infantile DEE (**MONDO:0800491**); these should not be substituted automatically for a DEE81-specific identifier. Open Targets links DMXL2 to both broader concepts. (OpenTargets Search: -DMXL2)
- **Orphanet, MeSH:** no specific DEE81 entries were verified.
- **ICD-10/ICD-11:** no gene-specific code exists in the evidence reviewed; coding ordinarily uses epilepsy/epileptic-encephalopathy, developmental-disability, hearing-loss, and other manifestation codes.

The foundational evidence is aggregated from published patient-level clinical, segregation, imaging, and functional data, not from an EHR-derived population cohort. Database records such as OMIM and Open Targets are disease-level aggregations. (esposito2019biallelicdmxl2mutations pages 1-2, OpenTargets Search: -DMXL2)

## 2. Etiology, risk, and protective factors

### Cause

The primary cause is **germline biallelic DMXL2 dysfunction**, predominantly complete or near-complete loss of function. Reported DEE81 alleles were absent from gnomAD in the original publication and segregated with disease under an autosomal-recessive model. Heterozygous parents were clinically unaffected. (esposito2019biallelicdmxl2mutations pages 6-7, esposito2019biallelicdmxl2mutations pages 13-14)

### Genetic risk factors

The established risk state is inheritance of pathogenic variants on both alleles. Consanguinity increases the probability that both parents carry the same rare allele but is not required: two foundational families were consanguineous, whereas the Italian-Brazilian family was not. For carrier parents, the standard Mendelian risk for each pregnancy is 25% affected, 50% carrier, and 25% unaffected/non-carrier, assuming correctly phased fully penetrant alleles.

DMXL2 has allelic heterogeneity. Biallelic severe loss causes DEE81, whereas a biallelic in-frame deletion retaining approximately 30% transcript was associated with a comparatively milder polyendocrine-polyneuropathy syndrome. Heterozygous variants or deletions have been reported with dominant hearing loss or variably penetrant neurodevelopmental phenotypes; these should not be conflated with recessive DEE81. (esposito2019biallelicdmxl2mutations pages 2-3, esposito2019biallelicdmxl2mutations pages 13-14)

### Environmental, infectious, lifestyle, and protective factors

No environmental toxin, infection, diet, lifestyle exposure, or gene–environment interaction is established as causal for DEE81. No protective DMXL2 allele or environmental protective factor has been reported. Fever, sleep deprivation, infection, and medication nonadherence may generally precipitate seizures in epilepsy, but no DEE81-specific quantitative evidence was found. Vaccination is not causal; routine immunization remains appropriate unless individualized clinical considerations dictate otherwise.

## 3. Phenotypes

Observed frequencies refer to the original six-patient cohort.

- **Neonatal-onset epilepsy/Ohtahara syndrome:** 6/6; predominantly tonic seizures, less commonly myoclonic and occasional focal seizures; severe and persistent. Suggested HPO: **Seizure HP:0001250**, **Tonic seizure HP:0032792**, **Myoclonic seizure HP:0002123**, **Focal-onset seizure HP:0007359**, **EEG with suppression-burst pattern HP:0010851**. (esposito2019biallelicdmxl2mutations pages 5-6)
- **Persistent suppression-burst EEG:** 6/6, beginning in the first days of life and remaining continuous during follow-up; wake and sleep were difficult to distinguish. This is an objective electrophysiological sign rather than a symptom. (esposito2019biallelicdmxl2mutations pages 5-6)
- **Profound global developmental impairment:** 6/6; none acquired developmental, communicative, or motor skills after birth. Suggested HPO: **Global developmental delay HP:0001263**, **Profound global developmental delay HP:0012736**, **Absent speech HP:0001344**. The effect on daily function is catastrophic, implying complete dependence for activities of daily living, although no EQ-5D, SF-36, PROMIS, or caregiver-burden study exists. (esposito2019biallelicdmxl2mutations pages 1-2, esposito2019biallelicdmxl2mutations pages 5-6)
- **Hypotonia and quadriparesis:** 6/6, severe and persistent. HPO: **Muscular hypotonia HP:0001252**, **Quadriparesis HP:0002273**. (esposito2019biallelicdmxl2mutations pages 5-6)
- **Sensorineural hearing loss:** 6/6. HPO: **Sensorineural hearing impairment HP:0000407**. Formal severity distributions were not available. (esposito2019biallelicdmxl2mutations pages 5-6)
- **Peripheral polyneuropathy:** 4/4 evaluated children in Families 1 and 2; Family 3 was not assessed electrophysiologically. HPO: **Peripheral neuropathy HP:0009830**, potentially **Sensorimotor neuropathy HP:0007141**. (esposito2019biallelicdmxl2mutations pages 5-6)
- **Brain hypomyelination and thin/hypoplastic corpus callosum:** 6/6 on early MRI. HPO: **Hypomyelination HP:0003429**, **Thin corpus callosum HP:0002079**. (esposito2019biallelicdmxl2mutations pages 8-10, esposito2019biallelicdmxl2mutations pages 5-6)
- **Simplified gyral pattern:** 2/6, frontal-limited in one and diffuse with frontal predominance in another. HPO: **Simplified gyral pattern HP:0009879**. (esposito2019biallelicdmxl2mutations pages 5-6)
- **Progressive cerebral and white-matter volume loss/leukoencephalopathy:** observed in all three with serial MRI 9–21 months later. HPO: **Cerebral atrophy HP:0002059**, **Leukoencephalopathy HP:0002352**, **Ventriculomegaly HP:0002119** where present. (esposito2019biallelicdmxl2mutations pages 8-10, esposito2019biallelicdmxl2mutations pages 5-6)
- **Dysmorphic features:** 6/6, but no sufficiently specific recurrent gestalt was established. HPO annotation should be patient-specific rather than assigning a generic dysmorphism term. (esposito2019biallelicdmxl2mutations pages 5-6)
- **Laboratory/muscle findings:** muscle coenzyme-Q concentration was normal; one patient had abundant intramuscular lipid droplets. This isolated observation is not a validated biomarker. (esposito2019biallelicdmxl2mutations pages 5-6)

No systematic behavioral phenotype, pain assessment, sleep measure, laboratory signature, or formal quality-of-life dataset is available.

## 4. Genetic and molecular information

**Gene:** **DMXL2** (Dmx-like 2/rabconnectin-3α); Ensembl **ENSG00000104093**. HGNC and NCBI Gene numerical identifiers were not verified in the retrieved evidence. The protein contains 16 conserved WD40 domains and a central domain homologous to yeast Rav1p. It is brain enriched, abundant at synaptic terminals, and participates in complexes governing V-ATPase assembly and activity. (OpenTargets Search: -DMXL2, falace2024vatpasedysfunctionin pages 8-9, esposito2019biallelicdmxl2mutations pages 2-3)

### Foundational variants

1. **c.5135C>T, p.(Ala1712Val)** in trans with **c.4478C>G, p.(Ser1493Ter)** in Family 1.
2. Homozygous **c.4478C>A, p.(Ser1493Ter)** in Family 2.
3. Homozygous **c.7518-1G>A**, disrupting the exon-31 splice acceptor, causing exon skipping and a frameshift reported as **p.(Trp2507ArgfsTer4)**; one passage renders the residue as Trp2508. Transcript-specific HGVS normalization is therefore advisable before database ingestion. (esposito2019biallelicdmxl2mutations pages 1-2, esposito2019biallelicdmxl2mutations pages 6-7, esposito2019biallelicdmxl2mutations pages 5-6)

The nonsense and splice variants are loss-of-function alleles. The p.Ala1712Val missense allele occurred with a truncating allele and was supported by segregation and the near-absence of DMXL2 in patient cells. All foundational variants were absent from gnomAD at publication. They are constitutional germline variants; no somatic DEE81 mechanism is known. Patient fibroblasts showed nearly absent protein, and wild-type DMXL2 re-expression rescued the LysoTracker phenotype, providing strong functional support. (esposito2019biallelicdmxl2mutations pages 6-7)

No validated modifier genes, protective variants, recurrent structural rearrangement specific to DEE81, disease-associated episignature, or clinically actionable pharmacogenomic association is known. Rare heterozygous DMXL2-spanning CNVs have been associated with broader neurodevelopmental susceptibility, but they are not established causes of the classic recessive DEE81 phenotype. (esposito2019biallelicdmxl2mutations pages 2-3)

## 5. Environmental information

DEE81 is a Mendelian genetic disease. No toxin, radiation, pollution, occupational exposure, smoking, diet, alcohol, exercise pattern, or infectious organism has been implicated in disease initiation. Environmental factors may influence seizure burden or complications nonspecifically but do not explain the core disorder. Accordingly, CTD-style chemical–disease or pathogen annotations would presently be speculative.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic severe DMXL2 variants lead to absent or markedly reduced rabconnectin-3α.**
2. **DMXL2 deficiency leads to impaired assembly/trafficking and activity of V-ATPase on synaptic and endolysosomal membranes.**
3. **Defective V-ATPase regulation leads to abnormal organellar acidification and endosomal/lysosomal homeostasis.**
4. **Endolysosomal dysfunction results in slowed cargo degradation and defective autophagic flux**, demonstrated by reduced LC3/LC3-II, p62 and polyubiquitinated-protein accumulation, reduced endolysosomal markers, and abnormal autolysosomal ultrastructure.
5. **Defective neuronal clearance and vesicle physiology lead to impaired neurite elongation and loss of synaptic contacts** in Dmxl2-silenced mouse hippocampal neurons.
6. **Impaired prenatal circuit formation and synaptic maintenance are inferred to lead to neonatal suppression-burst EEG, severe seizures, and absent developmental acquisition.**
7. **A parallel branch of neural vulnerability leads to hypomyelination, corpus-callosum hypoplasia, deafness, and peripheral neuropathy; continued lysosomal/autophagic failure is inferred to result in progressive cerebral shrinkage, leukoencephalopathy, systemic vulnerability, and premature death.** (esposito2019biallelicdmxl2mutations pages 1-2, esposito2019biallelicdmxl2mutations pages 6-7, falace2024vatpasedysfunctionin pages 8-9, esposito2019biallelicdmxl2mutations pages 11-12)

DMXL2/rabconnectin-3α interacts with synaptic-vesicle Rab3A-associated machinery and participates in V-ATPase incorporation into synaptic vesicles through its Rav1p-homologous region. V-ATPase-driven proton transport is required for organelle acidification, endocytic degradation, autophagy, and neurotransmitter-vesicle biology. The 2024 expert review emphasizes that postmitotic neurons are uniquely vulnerable to lysosomal dyshomeostasis and identifies V-ATPase dysfunction as a mechanistic bridge among early DEE, neurodevelopmental disorders, and neurodegeneration. (falace2024vatpasedysfunctionin pages 8-9)

**Experimental evidence:** patient fibroblasts showed increased LysoTracker signal, reduced EEA1 and LAMP1, slowed EGFR and dextran degradation, decreased LC3-II/LC3-I, p62 accumulation, polyubiquitinated-protein accumulation, and abnormal vacuoles. Re-expression of wild-type DMXL2 rescued the acidic-organelle phenotype. Dmxl2-silenced mouse hippocampal neurons recapitulated lysosomal/autophagic abnormalities and showed reduced neurite complexity and synaptic contacts, especially excitatory dendritic connections. (esposito2019biallelicdmxl2mutations pages 6-7, esposito2019biallelicdmxl2mutations pages 10-11, esposito2019biallelicdmxl2mutations pages 5-6, esposito2019biallelicdmxl2mutations pages 11-12)

No DEE81-specific human brain single-cell, spatial-transcriptomic, proteomic, metabolomic, lipidomic, or integrated multi-omic dataset was found. The isolated muscle lipid-droplet observation is insufficient to define a lipidomic signature.

**Suggested GO biological processes:** vacuolar acidification (**GO:0007035**), autophagy (**GO:0006914**), macroautophagy (**GO:0016236**), endosomal transport (**GO:0016197**), lysosomal transport (**GO:0007041**), synapse organization (**GO:0050808**), neuron projection development (**GO:0031175**), and regulation of synaptic vesicle exocytosis (**GO:2000300**). Suggested cellular components include lysosome (**GO:0005764**), endosome (**GO:0005768**), autophagosome (**GO:0005776**), synaptic vesicle (**GO:0008021**), and V-type proton-transporting ATPase complex (**GO:0016471**).

**Suggested Cell Ontology terms:** neuron (**CL:0000540**), central nervous system neuron (**CL:0000117**), hippocampal neuron where experimentally relevant, oligodendrocyte (**CL:0000128**, inferred from hypomyelination), Schwann cell (**CL:0002573**, inferred from peripheral neuropathy), and inner-ear sensory hair cell (**CL:0000202**, inferred from sensorineural hearing loss).

## 7. Anatomical structures affected

The nervous system is primary: cerebral cortex and white matter, corpus callosum, synaptic networks, peripheral nerves, and auditory pathways/inner ear. The MRI phenotype is bilateral/diffuse rather than consistently lateralized. Suggested UBERON annotations are **brain UBERON:0000955**, **cerebral cortex UBERON:0000956**, **white matter UBERON:0002316**, **corpus callosum UBERON:0002336**, **hippocampus UBERON:0002421** for the experimental model, **peripheral nervous system UBERON:0000010**, and **inner ear UBERON:0001846**. (esposito2019biallelicdmxl2mutations pages 8-10, esposito2019biallelicdmxl2mutations pages 5-6)

At the subcellular level, lysosomes, endosomes, autophagosomes/autolysosomes, synaptic vesicles, axons/neurites, and synapses are implicated. No consistent primary cardiovascular, renal, hepatic, endocrine, immune, or skeletal-organ phenotype has been established for classic DEE81. Endocrine disease belongs chiefly to a distinct, partially residual-function DMXL2 phenotype. (esposito2019biallelicdmxl2mutations pages 2-3)

## 8. Temporal development

The classic course begins on day 1 or within the first days of life, implying prenatal pathogenesis with neonatal clinical expression. Seizures and suppression-burst EEG are chronic and severe rather than a self-limited neonatal epilepsy. Developmental skills fail to emerge, and neurological disability remains profound. Early MRI already shows hypomyelination and callosal hypoplasia; serial imaging over 9–21 months can show progressive grey- and white-matter loss and leukoencephalopathy. Thus, DEE81 combines a congenital developmental encephalopathy with superimposed progressive neurodegeneration. (esposito2019biallelicdmxl2mutations pages 1-2, esposito2019biallelicdmxl2mutations pages 5-6)

No validated stages or remission pattern exist. The neonatal period is the critical diagnostic window, but whether very early seizure suppression modifies development is unknown. The disorder is lifelong in survivors.

## 9. Inheritance and population

Inheritance is autosomal recessive. Available segregation suggests high penetrance for the severe biallelic genotypes, but the sample is too small for a formal estimate. Expressivity may depend on residual DMXL2 function; complete/near-complete loss produces severe DEE, whereas residual transcript has been associated with a milder multisystem phenotype. Anticipation is not expected. Parental germline mosaicism has not been demonstrated for DEE81, although it remains a generic residual-risk consideration after an apparently de novo variant. (esposito2019biallelicdmxl2mutations pages 6-7, esposito2019biallelicdmxl2mutations pages 13-14)

Prevalence, incidence, carrier frequency, sex ratio, founder effects, and ethnic/geographic enrichment are unknown. The initial families were Italian-Brazilian, Israeli Arab, and Turkish; two involved first-cousin parents. These observations demonstrate worldwide occurrence and a role for consanguinity but not population-specific enrichment. Five deaths among six reported children must not be interpreted as a population mortality rate without larger ascertainment-unbiased cohorts. (esposito2019biallelicdmxl2mutations pages 5-6)

For context, a 2023 authoritative review estimated that next-generation sequencing detects pathogenic single-gene variants in approximately 30–50% of DEEs overall and that recessive variants account for 11–38% in reported cohorts; these figures are not DEE81-specific. (guerrini2023developmentalandepileptic pages 3-4)

## 10. Diagnostics

### Clinical recognition

Suspect DEE81 in a neonate with tonic seizures, persistent suppression-burst EEG, profound hypotonia, absent developmental acquisition, sensorineural hearing loss, and MRI showing hypomyelination with a thin corpus callosum—especially with consanguinity, similarly affected siblings, or progressive cerebral volume loss.

Recommended evaluation is:

1. Prolonged video-EEG, including sleep and wake sampling.
2. Brain MRI with age-appropriate myelination assessment; repeat MRI when progression is clinically relevant.
3. Comprehensive neurological and developmental assessment.
4. Audiology, ideally auditory brainstem responses in infancy.
5. Peripheral-nerve examination and nerve-conduction studies where feasible.
6. Swallowing, nutrition, respiratory, orthopedic, vision, and palliative-care assessments according to manifestations.
7. Genetic counseling and parental segregation studies. (esposito2019biallelicdmxl2mutations pages 8-10, esposito2019biallelicdmxl2mutations pages 5-6)

### Molecular testing

Trio **WES or WGS** is preferred because early-infantile DEE is genetically heterogeneous. A comprehensive epilepsy/DEE panel is acceptable if it includes **DMXL2**, full coding/splice coverage, and deletion/duplication analysis. Confirm candidate variants by an orthogonal method and phase them in the parents. WGS may identify intronic, regulatory, structural, or copy-number lesions missed by WES. RNA studies from accessible cells can test suspected splice variants; fibroblast DMXL2 expression, endolysosomal markers, or LysoTracker rescue are research-level functional assays, not validated clinical diagnostics. (esposito2019biallelicdmxl2mutations pages 1-2, esposito2019biallelicdmxl2mutations pages 6-7, guerrini2023developmentalandepileptic pages 3-4)

Routine karyotyping, FISH, mitochondrial testing, or repeat-expansion testing is not specifically indicated after convincing biallelic DMXL2 findings, although CMA or genome-wide CNV analysis remains useful in unsolved DEE. There are no standardized DEE81 biochemical criteria, newborn screen, liquid biopsy, or validated metabolomic/proteomic biomarker.

Recent real-world evidence supports broad genomic testing: a 2024 pediatric study found pathogenic variants in 11/65 (16.9%) routine epilepsy panels, whereas a separate 142-family cohort obtained molecular diagnoses in 74/142 (52%), with therapeutic implications in 38/74 diagnosed families. These are general epilepsy data, not DMXL2-specific yields. (majethia2024geneticandphenotypic pages 1-3, grew2024yieldandutility pages 1-2)

**Differential diagnosis:** other suppression-burst/early-infantile DEEs, including STXBP1-, KCNQ2-, SCN2A-, KCNT1-, DNM1-, WWOX-, BRAT1-, DOCK7-, and ATP6V1A-related disorders; mitochondrial/metabolic epileptic encephalopathies; structural cortical malformations; congenital infections; and other lysosomal/autophagy or V-ATPase disorders. The combination of deafness, neuropathy, hypomyelination/callosal thinning, progression, and biallelic DMXL2 variants distinguishes DEE81.

## 11. Outcome and prognosis

Prognosis in the foundational cohort was extremely poor: none of six children acquired motor, communicative, or other developmental skills, and five died before nine years of age from respiratory or systemic complications. One child remained alive at 15 months when reported. No Kaplan–Meier survival estimate, median life expectancy, prognostic biomarker, or treated-versus-untreated comparison exists. (esposito2019biallelicdmxl2mutations pages 1-2, esposito2019biallelicdmxl2mutations pages 5-6)

Expected morbidity includes medically complex epilepsy, profound lifelong disability, immobility/quadriparesis, feeding and aspiration risk, respiratory vulnerability, deafness, neuropathy, contractures, and complete caregiver dependence. Serial MRI progression and null protein expression may indicate severe disease, but neither is validated as an individual prognostic biomarker. Formal quality-of-life data are unavailable.

## 12. Treatment

No disease-modifying or DMXL2-targeted therapy is approved, no reproducible genotype-specific antiseizure-medication response has been published, and no relevant registered DMXL2/DEE81 interventional trial was identified. Treatment is therefore individualized and supportive.

- **Epilepsy:** specialist management using antiseizure medications appropriate to neonatal/tonic seizures and EEG evolution; consider ketogenic diet, hormonal therapy if spasms develop, and other refractory-epilepsy strategies according to standard practice. Evidence for any one option in DEE81 is absent.
- **Respiratory and feeding care:** swallowing evaluation, aspiration prevention, nutrition support, airway-clearance planning, and gastrostomy when clinically indicated.
- **Rehabilitation:** physical, occupational, speech/communication, positioning, orthopedic, and contracture-prevention services, recognizing limited developmental potential in reported null genotypes.
- **Hearing:** audiologic monitoring and hearing-assistive interventions where benefit is feasible.
- **Neuropathy and immobility:** pain surveillance, orthotics, pressure-injury prevention, and mobility equipment.
- **Psychosocial and palliative care:** early family support, respite, goals-of-care discussions, and pediatric palliative involvement are appropriate given the severe natural history.

Suggested NCIt intervention concepts include **Anticonvulsant Therapy (NCIT:C64276)**, **Ketogenic Diet**, **Physical Therapy**, **Occupational Therapy**, **Speech and Language Therapy**, **Gastrostomy**, **Hearing Aid**, **Genetic Counseling**, and **Palliative Care**; local terminology services should verify exact current NCIt identifiers before ingestion.

Restoration of DMXL2 rescued lysosomal abnormalities in patient fibroblasts, making gene replacement conceptually attractive. Modulating V-ATPase assembly, lysosomal acidification, or autophagy is also mechanistically plausible, but the 2024 expert review treats these as emerging preclinical opportunities—not treatments ready for patients. Nonspecific autophagy activation could be harmful and should not be attempted outside research. (esposito2019biallelicdmxl2mutations pages 6-7, falace2024vatpasedysfunctionin pages 8-9)

## 13. Prevention

There is no lifestyle, environmental, drug, or vaccine-based primary prevention. Effective prevention is reproductive and diagnostic:

- Offer molecular confirmation and genetic counseling to affected families.
- Once familial variants are known, offer carrier testing to adult relatives, prenatal diagnosis by chorionic-villus sampling or amniocentesis, and preimplantation genetic testing for monogenic disease.
- For future pregnancies without prior testing, early trio sequencing is appropriate if fetal/neonatal neurological findings emerge.
- Population newborn or carrier screening is not supported because prevalence and carrier frequency are unknown.
- Secondary prevention consists of rapid recognition and treatment of neonatal seizures and early management of feeding, respiratory, hearing, and orthopedic complications; whether seizure control changes the underlying developmental trajectory is unknown.
- Tertiary prevention includes aspiration precautions, immunization against routine respiratory pathogens, contracture and pressure-injury prevention, nutrition optimization, and emergency seizure plans.

## 14. Other species and natural disease

No naturally occurring veterinary disease equivalent, affected breed, zoonotic transmission, or cross-species infectious susceptibility is known. DEE81 is noninfectious and has no zoonotic potential.

DMXL2 is evolutionarily conserved, as shown by its Rav1p-related domain and conserved role in V-ATPase regulation. **Mus musculus** (NCBI Taxon **10090**) Dmxl2 is the principal experimentally relevant ortholog; rat hippocampal neurons have also been used in mechanistic work. Exact NCBI Gene identifiers for orthologs were not verified in the retrieved evidence. (falace2024vatpasedysfunctionin pages 8-9, esposito2019biallelicdmxl2mutations pages 2-3)

## 15. Model organisms and experimental systems

- **Patient-derived fibroblasts:** the strongest human cellular model. They reproduce absent protein, endolysosomal and autophagic defects, and permit rescue by wild-type DMXL2. Limitation: fibroblasts do not reproduce neuronal network activity, myelination, or seizures. (esposito2019biallelicdmxl2mutations pages 6-7, esposito2019biallelicdmxl2mutations pages 10-11)
- **Primary mouse hippocampal neurons with Dmxl2 shRNA:** reproduce altered lysosomal/autophagy markers, reduced neurite complexity, and synaptic loss. Because silenced cells were embedded in a largely unaffected network, the phenotype supports a cell-autonomous component. Limitations include acute knockdown rather than germline human alleles and absence of a whole-animal seizure phenotype. (esposito2019biallelicdmxl2mutations pages 8-10, esposito2019biallelicdmxl2mutations pages 10-11, esposito2019biallelicdmxl2mutations pages 11-12)
- **Mouse genetics:** complete Dmxl2 loss is reported as embryonically lethal; heterozygous mice show macrocephaly and corpus-callosum dysplasia. This demonstrates developmental dosage sensitivity but does not fully model recessive human DEE81. (falace2024vatpasedysfunctionin pages 8-9)
- **Needed models:** patient iPSC-derived excitatory and inhibitory neurons, oligodendrocytes, auditory cells, cerebral organoids, and knock-in mice carrying the human alleles would enable testing of network excitability, myelination, developmental timing, and gene-replacement strategies. These are research recommendations, not currently demonstrated DEE81 resources.

## Current expert assessment

The 2024 V-ATPase review places DMXL2 among brain-enriched V-ATPase accessory proteins whose disruption unifies neurodevelopmental failure with progressive neuronal dysfunction. The best-supported interpretation is therefore not simply “epilepsy causing delay,” but a congenital disorder of organelle acidification and autophagy that directly impairs brain wiring, with epileptic activity adding further dysfunction. The decisive evidence consists of recessive segregation, absence of DMXL2 protein, reproducible lysosomal/autophagic abnormalities, rescue by wild-type DMXL2, and concordant neuronal knockdown phenotypes. Nevertheless, the clinical evidence remains only six foundational patients; prevalence, full allelic spectrum, treatment response, and long-term variability require international case aggregation and prospective natural-history study. (esposito2019biallelicdmxl2mutations pages 6-7, falace2024vatpasedysfunctionin pages 8-9)

### Key publications

1. Esposito A, et al. **Biallelic DMXL2 mutations impair autophagy and cause Ohtahara syndrome with progressive course.** *Brain*. December 2019;142:3876–3891. PMID: **31688942**. DOI: [10.1093/brain/awz326](https://doi.org/10.1093/brain/awz326). Primary human case series, patient-cell functional studies, and mouse-neuron experiments. (esposito2019biallelicdmxl2mutations pages 1-2, esposito2019biallelicdmxl2mutations pages 6-7)
2. Guerrini R, et al. **Developmental and epileptic encephalopathies: from genetic heterogeneity to phenotypic continuum.** *Physiological Reviews*. January 2023;103:433–513. DOI: [10.1152/physrev.00063.2021](https://doi.org/10.1152/physrev.00063.2021). Authoritative general DEE review. (guerrini2023developmentalandepileptic pages 3-4)
3. Falace A, et al. **V-ATPase Dysfunction in the Brain: Genetic Insights and Therapeutic Opportunities.** *Cells*. August 2024;13:1441. DOI: [10.3390/cells13171441](https://doi.org/10.3390/cells13171441). Recent mechanistic review covering DMXL2 and translational directions. (falace2024vatpasedysfunctionin pages 8-9)
4. Majethia P, et al. **Genetic and phenotypic landscape of pediatric-onset epilepsy in 142 Indian families.** *Clinical Genetics*. February 2024. DOI: [10.1111/cge.14495](https://doi.org/10.1111/cge.14495). Contemporary evidence for the diagnostic and therapeutic utility of genomic testing, not DEE81-specific. (majethia2024geneticandphenotypic pages 1-3)
5. Grew EC, et al. **Yield and Utility of Routine Epilepsy Panel Genetic Testing Among Young Patients With Seizures.** *Journal of Child Neurology*. March 2024. DOI: [10.1177/08830738241240516](https://doi.org/10.1177/08830738241240516). General pediatric epilepsy-testing implementation study. (grew2024yieldandutility pages 1-2)

References

1. (esposito2019biallelicdmxl2mutations pages 1-2): Alessandro Esposito, Antonio Falace, Matias Wagner, Moran Gal, Davide Mei, Valerio Conti, Tiziana Pisano, Davide Aprile, Maria Sabina Cerullo, Antonio De Fusco, Silvia Giovedì, Annette Seibt, Daniella Magen, Tilman Polster, Ayelet Eran, Sarah L Stenton, Chiara Fiorillo, Sarit Ravid, Ertan Mayatepek, Hava Hafner, Saskia Wortmann, Erez Y Levanon, Carla Marini, Hanna Mandel, Fabio Benfenati, Felix Distelmaier, Anna Fassio, and Renzo Guerrini. Biallelic dmxl2 mutations impair autophagy and cause ohtahara syndrome with progressive course. Brain : a journal of neurology, 142:3876-3891, Dec 2019. URL: https://doi.org/10.1093/brain/awz326, doi:10.1093/brain/awz326. This article has 51 citations.

2. (esposito2019biallelicdmxl2mutations pages 6-7): Alessandro Esposito, Antonio Falace, Matias Wagner, Moran Gal, Davide Mei, Valerio Conti, Tiziana Pisano, Davide Aprile, Maria Sabina Cerullo, Antonio De Fusco, Silvia Giovedì, Annette Seibt, Daniella Magen, Tilman Polster, Ayelet Eran, Sarah L Stenton, Chiara Fiorillo, Sarit Ravid, Ertan Mayatepek, Hava Hafner, Saskia Wortmann, Erez Y Levanon, Carla Marini, Hanna Mandel, Fabio Benfenati, Felix Distelmaier, Anna Fassio, and Renzo Guerrini. Biallelic dmxl2 mutations impair autophagy and cause ohtahara syndrome with progressive course. Brain : a journal of neurology, 142:3876-3891, Dec 2019. URL: https://doi.org/10.1093/brain/awz326, doi:10.1093/brain/awz326. This article has 51 citations.

3. (esposito2019biallelicdmxl2mutations pages 5-6): Alessandro Esposito, Antonio Falace, Matias Wagner, Moran Gal, Davide Mei, Valerio Conti, Tiziana Pisano, Davide Aprile, Maria Sabina Cerullo, Antonio De Fusco, Silvia Giovedì, Annette Seibt, Daniella Magen, Tilman Polster, Ayelet Eran, Sarah L Stenton, Chiara Fiorillo, Sarit Ravid, Ertan Mayatepek, Hava Hafner, Saskia Wortmann, Erez Y Levanon, Carla Marini, Hanna Mandel, Fabio Benfenati, Felix Distelmaier, Anna Fassio, and Renzo Guerrini. Biallelic dmxl2 mutations impair autophagy and cause ohtahara syndrome with progressive course. Brain : a journal of neurology, 142:3876-3891, Dec 2019. URL: https://doi.org/10.1093/brain/awz326, doi:10.1093/brain/awz326. This article has 51 citations.

4. (OpenTargets Search: -DMXL2): Open Targets Query (-DMXL2, 5 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

5. (esposito2019biallelicdmxl2mutations pages 13-14): Alessandro Esposito, Antonio Falace, Matias Wagner, Moran Gal, Davide Mei, Valerio Conti, Tiziana Pisano, Davide Aprile, Maria Sabina Cerullo, Antonio De Fusco, Silvia Giovedì, Annette Seibt, Daniella Magen, Tilman Polster, Ayelet Eran, Sarah L Stenton, Chiara Fiorillo, Sarit Ravid, Ertan Mayatepek, Hava Hafner, Saskia Wortmann, Erez Y Levanon, Carla Marini, Hanna Mandel, Fabio Benfenati, Felix Distelmaier, Anna Fassio, and Renzo Guerrini. Biallelic dmxl2 mutations impair autophagy and cause ohtahara syndrome with progressive course. Brain : a journal of neurology, 142:3876-3891, Dec 2019. URL: https://doi.org/10.1093/brain/awz326, doi:10.1093/brain/awz326. This article has 51 citations.

6. (esposito2019biallelicdmxl2mutations pages 8-10): Alessandro Esposito, Antonio Falace, Matias Wagner, Moran Gal, Davide Mei, Valerio Conti, Tiziana Pisano, Davide Aprile, Maria Sabina Cerullo, Antonio De Fusco, Silvia Giovedì, Annette Seibt, Daniella Magen, Tilman Polster, Ayelet Eran, Sarah L Stenton, Chiara Fiorillo, Sarit Ravid, Ertan Mayatepek, Hava Hafner, Saskia Wortmann, Erez Y Levanon, Carla Marini, Hanna Mandel, Fabio Benfenati, Felix Distelmaier, Anna Fassio, and Renzo Guerrini. Biallelic dmxl2 mutations impair autophagy and cause ohtahara syndrome with progressive course. Brain : a journal of neurology, 142:3876-3891, Dec 2019. URL: https://doi.org/10.1093/brain/awz326, doi:10.1093/brain/awz326. This article has 51 citations.

7. (esposito2019biallelicdmxl2mutations pages 10-11): Alessandro Esposito, Antonio Falace, Matias Wagner, Moran Gal, Davide Mei, Valerio Conti, Tiziana Pisano, Davide Aprile, Maria Sabina Cerullo, Antonio De Fusco, Silvia Giovedì, Annette Seibt, Daniella Magen, Tilman Polster, Ayelet Eran, Sarah L Stenton, Chiara Fiorillo, Sarit Ravid, Ertan Mayatepek, Hava Hafner, Saskia Wortmann, Erez Y Levanon, Carla Marini, Hanna Mandel, Fabio Benfenati, Felix Distelmaier, Anna Fassio, and Renzo Guerrini. Biallelic dmxl2 mutations impair autophagy and cause ohtahara syndrome with progressive course. Brain : a journal of neurology, 142:3876-3891, Dec 2019. URL: https://doi.org/10.1093/brain/awz326, doi:10.1093/brain/awz326. This article has 51 citations.

8. (falace2024vatpasedysfunctionin pages 8-9): Antonio Falace, Greta Volpedo, Marcello Scala, Federico Zara, Pasquale Striano, and Anna Fassio. V-atpase dysfunction in the brain: genetic insights and therapeutic opportunities. Cells, 13:1441, Aug 2024. URL: https://doi.org/10.3390/cells13171441, doi:10.3390/cells13171441. This article has 27 citations.

9. (esposito2019biallelicdmxl2mutations pages 11-12): Alessandro Esposito, Antonio Falace, Matias Wagner, Moran Gal, Davide Mei, Valerio Conti, Tiziana Pisano, Davide Aprile, Maria Sabina Cerullo, Antonio De Fusco, Silvia Giovedì, Annette Seibt, Daniella Magen, Tilman Polster, Ayelet Eran, Sarah L Stenton, Chiara Fiorillo, Sarit Ravid, Ertan Mayatepek, Hava Hafner, Saskia Wortmann, Erez Y Levanon, Carla Marini, Hanna Mandel, Fabio Benfenati, Felix Distelmaier, Anna Fassio, and Renzo Guerrini. Biallelic dmxl2 mutations impair autophagy and cause ohtahara syndrome with progressive course. Brain : a journal of neurology, 142:3876-3891, Dec 2019. URL: https://doi.org/10.1093/brain/awz326, doi:10.1093/brain/awz326. This article has 51 citations.

10. (guerrini2023developmentalandepileptic pages 3-4): Renzo Guerrini, Valerio Conti, Massimo Mantegazza, Simona Balestrini, Aristea S. Galanopoulou, and Fabio Benfenati. Developmental and epileptic encephalopathies: from genetic heterogeneity to phenotypic continuum. Physiological Reviews, 103:433-513, Jan 2023. URL: https://doi.org/10.1152/physrev.00063.2021, doi:10.1152/physrev.00063.2021. This article has 216 citations and is from a highest quality peer-reviewed journal.

11. (grew2024yieldandutility pages 1-2): Emily C Grew, Mayuri Reddy, Hayley Reichner, Jinsoo Kim, Misbah Salam, and Anjum Hashim. Yield and utility of routine epilepsy panel genetic testing among young patients with seizures. Journal of Child Neurology, 39:138-146, Mar 2024. URL: https://doi.org/10.1177/08830738241240516, doi:10.1177/08830738241240516. This article has 1 citations and is from a peer-reviewed journal.

12. (esposito2019biallelicdmxl2mutations pages 2-3): Alessandro Esposito, Antonio Falace, Matias Wagner, Moran Gal, Davide Mei, Valerio Conti, Tiziana Pisano, Davide Aprile, Maria Sabina Cerullo, Antonio De Fusco, Silvia Giovedì, Annette Seibt, Daniella Magen, Tilman Polster, Ayelet Eran, Sarah L Stenton, Chiara Fiorillo, Sarit Ravid, Ertan Mayatepek, Hava Hafner, Saskia Wortmann, Erez Y Levanon, Carla Marini, Hanna Mandel, Fabio Benfenati, Felix Distelmaier, Anna Fassio, and Renzo Guerrini. Biallelic dmxl2 mutations impair autophagy and cause ohtahara syndrome with progressive course. Brain : a journal of neurology, 142:3876-3891, Dec 2019. URL: https://doi.org/10.1093/brain/awz326, doi:10.1093/brain/awz326. This article has 51 citations.

13. (majethia2024geneticandphenotypic pages 1-3): Purvi Majethia, Namanpreet Kaur, Selinda Mascarenhas, Lakshmi Priya Rao, Shruti Pande, Dhanya Lakshmi Narayanan, Vivekananda Bhat, Shalini S. Nayak, Karthik Vijay Nair, Adarsh Pooradan Prasannakumar, Ankur Chaurasia, Bhagesh Hunakunti, Nalesh Jadhav, Sheeba Farooqui, Mayuri Yeole, Vishaka Kothiwale, Rohit Naik, Veena Bhat, Shrikiran Aroor, Leslie Lewis, Jayashree Purkayastha, Y. Ramesh Bhat, B. K. Praveen, B. L. Yatheesha, Siddaramappa J. Patil, Sheela Nampoothiri, Nutan Kamath, Shahyan Siddiqui, Stephanie Bielas, Katta Mohan Girisha, Suvasini Sharma, and Anju Shukla. Genetic and phenotypic landscape of pediatric-onset epilepsy in 142 indian families: counseling and therapeutic implications. Clinical genetics, 105:639-654, Feb 2024. URL: https://doi.org/10.1111/cge.14495, doi:10.1111/cge.14495. This article has 8 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Developmental_And_Epileptic_Encephalopathy_81-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 5 |
| Resolved | 5 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 5 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 47 |
| Resolved | 47 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |

Every term resolved, and every label the report gave matched.