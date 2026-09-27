---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-02T17:09:50.669376'
end_time: '2026-09-02T17:22:41.989529'
duration_seconds: 771.32
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Dilated Cardiomyopathy 1KK
  mondo_id: ''
  category: Cardiovascular
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 18
reference_validation:
  total_references: 4
  verified: 4
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 4
  on_topic: 1
  validator_version: 0.2.1
term_validation:
  total_terms: 9
  verified: 9
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
  path: Dilated_Cardiomyopathy_1KK-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Dilated Cardiomyopathy 1KK
- **MONDO ID:**  (if available)
- **Category:** Cardiovascular

## Research Objectives

Please provide a comprehensive research report on **Dilated Cardiomyopathy 1KK** covering all of the
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
- **Disease Name:** Dilated Cardiomyopathy 1KK
- **MONDO ID:**  (if available)
- **Category:** Cardiovascular

## Research Objectives

Please provide a comprehensive research report on **Dilated Cardiomyopathy 1KK** covering all of the
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


# Dilated Cardiomyopathy 1KK (DCM1KK): comprehensive disease-characteristics report

## Executive summary and evidence boundary

Dilated cardiomyopathy 1KK is the disease label used for **MYPN-associated dilated cardiomyopathy**. Open Targets maps it to **MONDO:0014100** and to the single target **MYPN**, encoding myopalladin. The foundational literature consists mainly of small pedigrees, sporadic cases, patient myocardium, neonatal-rat cardiomyocyte assays, and engineered mice—not prospective DCM1KK registries or randomized trials. Consequently, variant-specific facts below are distinguished from evidence extrapolated from genetic DCM generally. (OpenTargets Search: Dilated cardiomyopathy 1KK, duboscqbidot2008mutationsinthe pages 1-2)

A major interpretive warning is warranted: although historical studies established a plausible MYPN–DCM association, MYPN was not among the 19 moderate-to-definitive DCM genes in the 2021 ClinGen curation. A MYPN variant—especially a missense variant or variant of uncertain significance (VUS)—therefore should not by itself establish DCM1KK or drive irreversible management. Contemporary transcript normalization, population-frequency review, segregation, phenotype matching, and ACMG/AMP classification are essential.

The following table provides a knowledge-base-ready summary.

| Domain | Subtype-specific finding | Evidence level/source type | Ontology/identifier suggestions | Caveat |
|---|---|---|---|---|
| Disease identity | Dilated cardiomyopathy 1KK (DCM1KK), a proposed MYPN-associated inherited DCM subtype characterized by ventricular dilation and systolic dysfunction. | Curated disease–target association and historical human case-series evidence (OpenTargets Search: Dilated cardiomyopathy 1KK, duboscqbidot2008mutationsinthe pages 1-2) | MONDO:0014100; broader phenotype: dilated cardiomyopathy; MeSH: Cardiomyopathy, Dilated | No dedicated ICD-10, ICD-11, or Orphanet subtype code was identified; broader DCM coding is appropriate. |
| Causal gene/protein | MYPN encodes myopalladin, a striated-muscle protein localized to the sarcomeric Z-disc, I-band, and nucleus at chromosome 10q21.3. (OpenTargets Search: Dilated cardiomyopathy 1KK, purevjav2012molecularbasisfor pages 2-2) | Human genetic association supported by cellular and mouse experiments | MYPN; OMIM gene 608517; historical transcript NM_032578; protein: myopalladin | MYPN has historically had limited evidence for monogenic DCM relative to core ClinGen-validated genes; interpret variants cautiously. |
| Inheritance | Familial variants were heterozygous and cosegregated with DCM, supporting likely autosomal-dominant inheritance with age-dependent, incomplete, or variable penetrance. (duboscqbidot2008mutationsinthe pages 3-3) | Small pedigrees; human observational evidence | Autosomal dominant inheritance; HPO concept: incomplete penetrance | Numerical penetrance, anticipation, germline-mosaicism rate, founder effects, and carrier frequency are unavailable. |
| Historical variant | MYPN I83fsX105, described as exon-2 ins/del_T735, produced no detectable premature-termination transcript, supporting nonsense-mediated decay or haploinsufficiency. (duboscqbidot2008mutationsinthe pages 5-6, duboscqbidot2008mutationsinthe pages 7-8) | Familial segregation and patient-derived RNA assay | Sequence Ontology: frameshift variant; loss-of-function mechanism | Historical nomenclature may not conform to current HGVS; transcript/build normalization and current ClinVar/ACMG classification are required. |
| Historical variant | MYPN R1088H cosegregated with familial DCM; linkage was suggestive with LOD 2.1 at theta 0, and left-ventricular tissue showed reduced myopalladin at alpha-actinin-positive Z-discs. (duboscqbidot2008mutationsinthe pages 3-3, duboscqbidot2008mutationsinthe pages 5-6) | Familial human and myocardial-tissue functional evidence | Sequence Ontology: missense variant; GO: Z disc | Absent from 400 historical controls, but current population frequency and formal ACMG/AMP classification were not established. |
| Historical variants | MYPN P1112L and V1195M occurred in apparently sporadic DCM; expression in neonatal rat cardiomyocytes caused mislocalization, sarcomeric disorganization, and increased cell death. (duboscqbidot2008mutationsinthe pages 1-2, duboscqbidot2008mutationsinthe pages 5-6, duboscqbidot2008mutationsinthe pages 7-8) | Human cases and in-vitro functional evidence | Sequence Ontology: missense variant; GO: sarcomere organization | Overexpression assays do not independently establish human pathogenicity; modern ClinVar, gnomAD, segregation, and ACMG reassessment are necessary. |
| Pleiotropic variant | MYPN Y20C was reported in DCM and hypertrophic cardiomyopathy, altered CARP binding and nuclear shuttling, and produced predominantly hypertrophic disease in transgenic mice. (purevjav2012molecularbasisfor pages 1-2, purevjav2012molecularbasisfor pages 2-2, purevjav2012molecularbasisfor pages 2-3) | Human cases, in-vitro assays, and transgenic-mouse evidence | dbSNP rs140148105; Sequence Ontology: missense variant; GO concepts: protein binding and nuclear transport | Historical 1000 Genomes frequency was approximately 0.001; pleiotropy and model–human discordance weaken DCM1KK specificity. |
| Variant spectrum | Four variants were found among 114 unrelated DCM probands: 2 of 65 familial cases and 2 of 49 sporadic cases; mean diagnosis age among carriers was 40.2 ± 18.3 years. (duboscqbidot2008mutationsinthe pages 1-2, duboscqbidot2008mutationsinthe pages 3-3) | Historical European-descent DCM cohort | HPO concept: adult onset | The 3–4% cohort frequency is era- and cohort-dependent and is not contemporary population prevalence. |
| Core structural phenotype | Left-ventricular or biventricular dilation with reduced systolic contraction is the defining phenotype. (duboscqbidot2008mutationsinthe pages 1-2) | Human clinical phenotype | HPO: Dilated cardiomyopathy, HP:0001644; ventricular dilatation; decreased ejection fraction | Variant-level frequencies and standardized imaging measurements were not reported. |
| Heart-failure phenotype | Progressive systolic dysfunction may cause exertional dyspnea, fatigue, exercise intolerance, edema, and advanced heart failure, as in DCM generally. | General DCM extrapolation; not systematically demonstrated in DCM1KK | HPO: Heart failure, HP:0001635; Dyspnea, HP:0002094; fatigue; exercise intolerance; peripheral edema | Symptom prevalence, severity, quality-of-life scores, hospitalization rates, and survival are unavailable for DCM1KK. |
| Electrical phenotype | Conduction abnormalities or arrhythmias occurred in a minority of the broader discovery cohort, but MYPN-variant-specific frequencies were not established. (duboscqbidot2008mutationsinthe pages 3-3) | Human cohort; weak subtype specificity | HPO: Cardiac arrhythmia, HP:0011675; Abnormal cardiac conduction, HP:0001678 | No MYPN-specific sudden-death or ventricular-arrhythmia estimate supports genotype-specific ICD decisions. |
| Anatomy | Primary involvement is myocardium, particularly left-ventricular cardiomyocytes and sarcomeric I–Z–I regions; biventricular disease may involve the right ventricle. (duboscqbidot2008mutationsinthe pages 5-6, purevjav2012molecularbasisfor pages 2-2) | Patient myocardium and experimental models | UBERON: heart, UBERON:0000948; left ventricle; right ventricle; myocardium; cardiac muscle tissue | No lateralization applies; skeletal-muscle disease from other MYPN genotypes should not automatically be assigned to DCM1KK. |
| Upstream mechanism | MYPN loss or dysfunctional missense protein disrupts Z-disc/I-band scaffolding and interactions with titin, alpha-actinin-2, CARP/ANKRD1, desmin, and nebulette. (duboscqbidot2008mutationsinthe pages 5-6, purevjav2012molecularbasisfor pages 1-2, purevjav2012molecularbasisfor pages 2-2) | Patient tissue, biochemical assays, and cellular models | GO: Z disc, GO:0030018; sarcomere, GO:0030017; I band; actin binding; titin binding; CL: cardiomyocyte | Mechanisms differ by variant: haploinsufficiency is supported for I83fsX105, while dominant-negative effects are proposed for some missense variants. |
| Downstream mechanism | Sarcomeric disorganization leads to reduced force and abnormal mechanotransduction; altered calcium handling is inferred to compound dysfunction, followed by dilation, fibrosis, and heart failure. (duboscqbidot2008mutationsinthe pages 5-6) | Mechanistic inference based mainly on cellular and MYPN-knockout mouse studies | GO concepts: cardiac muscle contraction, calcium-ion homeostasis, response to mechanical stimulus, extracellular-matrix organization; CL: ventricular cardiomyocyte and cardiac fibroblast | Calcium-handling and fibrotic mechanisms have not been demonstrated directly in carriers of the historical DCM1KK variants. |
| Diagnostic testing | Evaluation includes pedigree, ECG, ambulatory rhythm monitoring, echocardiography, cardiac MRI, BNP or NT-proBNP, and troponin where clinically indicated. | General DCM guideline practice; not MYPN-specific | Phenotyping concepts: ventricular volume, ejection fraction, late gadolinium enhancement | No test uniquely identifies DCM1KK apart from a credible MYPN genotype in a compatible phenotype. |
| Genetic testing | Use a curated cardiomyopathy multigene panel with deletion/duplication analysis; consider WES or WGS if panel testing is negative, and confirm variants by segregation analysis. | Current inherited-DCM practice informed by limited MYPN evidence | MYPN plus high-evidence DCM genes; ACMG/AMP; ClinVar; gnomAD | A MYPN VUS must not establish DCM1KK, direct predictive testing, or guide irreversible treatment. |
| Family screening | For a confirmed pathogenic or likely pathogenic familial variant, offer genetic counseling and cascade testing; carriers require longitudinal ECG and imaging. | General genetic-DCM practice plus familial MYPN segregation | HPO concept: asymptomatic; genetic counseling; cascade screening | MYPN-specific screening intervals and lifetime penetrance are not established. |
| Pharmacotherapy | Treat symptomatic HFrEF with guideline-directed therapy: ARNI or ACE inhibitor/ARB, evidence-based beta blocker, mineralocorticoid-receptor antagonist, SGLT2 inhibitor, and diuretics for congestion. | Extrapolated from randomized HFrEF evidence; no MYPN-specific trials | NCIT categories: Pharmacologic Therapy; Angiotensin Receptor–Neprilysin Inhibitor Therapy; Beta Blocker Therapy; SGLT2 Inhibitor Therapy; Diuretic Therapy | No drug is approved specifically for DCM1KK, and no established MYPN pharmacogenomic rule exists. |
| Device and surgical treatment | ICD, cardiac resynchronization, ventricular-assist device, and transplantation are considered using standard arrhythmic, conduction, ejection-fraction, and advanced-heart-failure criteria. | General DCM implementation | NCIT categories: Implantable Cardioverter-Defibrillator Therapy; Cardiac Resynchronization Therapy; Ventricular Assist Device; Heart Transplantation | MYPN is not an established high-arrhythmic-risk genotype and does not justify gene-specific device thresholds. |
| Advanced therapeutics | No MYPN-directed gene replacement, genome editing, antisense, siRNA, mRNA, or cell therapy has established clinical efficacy or an identified disease-specific trial. | Explicit evidence gap | NCIT categories: Gene Therapy; Genetic Engineering; RNA Therapy; Cell Therapy | Experimental concepts must not be represented as available treatment. |
| Prevention | Primary genetic prevention is unavailable; general risk reduction includes avoiding cardiotoxic alcohol, illicit stimulants, unnecessary cardiotoxic drugs, uncontrolled hypertension, and inappropriate extreme exercise. | General DCM risk-management extrapolation | Genetic counseling; reproductive counseling; cardiovascular surveillance | No exposure has been proven to trigger DCM specifically in MYPN carriers, although stress sensitivity is biologically plausible. |
| Mouse model | Mypn-knockout mice develop mild dilation, systolic dysfunction, reduced myofibrillar tension, abnormal passive tension and calcium handling, and severe dilation and fibrosis after pressure overload. | Genetic animal model | NCBI Taxon: Mus musculus, 10090; GO concepts: response to mechanical stimulus, cardiac muscle contraction, calcium-ion transport | The knockout models haploinsufficiency better than individual heterozygous missense variants and does not reproduce full human natural history. |
| Variant-specific model | Cardiac-restricted Y20C transgenic mice show Z-disc and intercalated-disc abnormalities, altered junctional proteins, hypertrophy, and reduced ejection fraction. (purevjav2012molecularbasisfor pages 8-10, purevjav2012molecularbasisfor pages 1-2) | Transgenic mouse model | NCBI Taxon: Mus musculus, 10090; GO concepts: intercalated disc and cell–cell junction organization | Predominantly HCM-like remodeling limits fidelity as a DCM1KK model. |
| Cellular models | Neonatal rat cardiomyocytes expressing historical variants reproduce myopalladin mislocalization, defective myofibrillogenesis, sarcomeric disruption, and cell death. (duboscqbidot2008mutationsinthe pages 1-2, duboscqbidot2008mutationsinthe pages 7-8) | In-vitro overexpression model | CL: cardiomyocyte; GO concepts: myofibril assembly, sarcomere organization, programmed cell death | Immature rodent cells and overexpression may exaggerate effects; no validated patient-derived MYPN-DCM iPSC or organoid model was identified. |
| Natural disease in other species | No convincing naturally occurring orthologous MYPN-associated DCM1KK syndrome was identified in companion animals or wildlife. | Explicit evidence gap | NCBI Taxonomy and VBO terms: not assignable | Canine and feline DCM should not be attributed to MYPN without variant-specific evidence. |
| Molecular profiling | No DCM1KK-specific single-cell, spatial-transcriptomic, proteomic, metabolomic, lipidomic, or epigenomic signature has been established. | Explicit evidence gap | GEO, PRIDE, MetaboLights, and ENCODE: no subtype-specific term assignable | General DCM fibroblast, immune, fibrotic, and metabolic signatures cannot be assumed to be MYPN-specific. |
| Epidemiology and prognosis | Population prevalence, incidence, sex ratio, geographic distribution, survival, transplantation, recovery, and validated prognostic biomarkers are unknown for DCM1KK. | Explicit evidence gap; evidence is limited to small cohorts and families | Orphan-disease epidemiology fields: unavailable | Store general DCM statistics separately and label them as extrapolated rather than subtype-specific. |
| Data provenance | Evidence is aggregated from disease databases, published pedigrees, myocardial tissue, cellular assays, and engineered animals rather than individual EHR records. (OpenTargets Search: Dilated cardiomyopathy 1KK, duboscqbidot2008mutationsinthe pages 1-2, purevjav2012molecularbasisfor pages 1-2) | Aggregated disease-level evidence | Evidence categories: human genetic; human tissue; in vitro; model organism | Patient-level EHR frequencies, standardized longitudinal outcomes, and contemporary reinterpretations were unavailable. |


*Table: Concise disease, gene, variant, phenotype, mechanism, diagnostic, treatment, and model annotations for MYPN-associated Dilated Cardiomyopathy 1KK. Subtype-specific findings are separated from general DCM extrapolations and explicit evidence gaps.*

## 1. Disease information

### Definition

DCM is a myocardial phenotype characterized by left-ventricular or biventricular dilation and impaired systolic function not adequately explained by coronary artery disease, hypertension, valvular disease, congenital heart disease, or another loading condition. DCM1KK denotes the proposed monogenic subset associated with germline MYPN variants. The discovery cohort described affected individuals as having predominantly isolated DCM; the mean age at diagnosis among reported MYPN carriers was **40.2 ± 18.3 years**. (duboscqbidot2008mutationsinthe pages 1-2, duboscqbidot2008mutationsinthe pages 3-3)

### Identifiers and synonyms

- **MONDO:** MONDO:0014100.
- **Gene:** MYPN, myopalladin; **OMIM gene 608517**; historical transcript **NM_032578**; chromosome **10q21.3**. (OpenTargets Search: Dilated cardiomyopathy 1KK, purevjav2012molecularbasisfor pages 2-2)
- **Synonyms:** dilated cardiomyopathy 1KK; DCM1KK; MYPN-related dilated cardiomyopathy; myopalladin-related DCM.
- **OMIM disease number:** not securely recovered from the retrieved primary texts; it should not be inferred from the MYPN gene number.
- **Orphanet:** no dedicated DCM1KK identifier found.
- **ICD-10:** use the broader DCM code, generally **I42.0**; there is no gene-specific code.
- **ICD-11/MeSH/SNOMED CT:** map to the broader dilated-cardiomyopathy concept; no dedicated MYPN subtype code was established in the retrieved evidence.

The evidence is **aggregated disease-level information**, not an EHR-derived patient dataset. It combines curated databases, published cases/pedigrees, explanted myocardium, in-vitro assays, and engineered animals. (OpenTargets Search: Dilated cardiomyopathy 1KK, duboscqbidot2008mutationsinthe pages 1-2, purevjav2012molecularbasisfor pages 1-2)

## 2. Etiology, risk, protection, and gene–environment interaction

### Causal factor

The proposed primary lesion is a heterozygous germline MYPN variant affecting myopalladin, a striated-muscle Z-disc/I-band/nuclear protein. The original study sequenced **114 unrelated DCM probands**—65 familial and 49 sporadic—and found four heterozygous variants: **I83fsX105, R1088H, P1112L, and V1195M**. Variants occurred in **2/65 familial cases (3%)** and **2/49 sporadic cases (4%)**, and were absent from 400 historical controls. These proportions are discovery-cohort yields, not current population prevalence. (duboscqbidot2008mutationsinthe pages 1-2, duboscqbidot2008mutationsinthe pages 3-3)

### Genetic risk and modifiers

The familial variants cosegregated with disease, supporting an autosomal-dominant model with variable or incomplete penetrance; R1088H produced suggestive linkage with **LOD 2.1 at θ=0**. No reliable numerical penetrance, sex-specific penetrance, anticipation, founder effect, carrier frequency, or germline-mosaicism rate has been established for DCM1KK. (duboscqbidot2008mutationsinthe pages 3-3)

MYPN also shows allelic and phenotypic heterogeneity. The p.Y20C variant was reported in both DCM and hypertrophic cardiomyopathy, whereas other MYPN variants are associated with restrictive cardiomyopathy or, when biallelic, skeletal myopathies. Thus, genotype, zygosity, other variants, and environmental stress probably influence expression. (purevjav2012molecularbasisfor pages 1-2, purevjav2012molecularbasisfor pages 2-2, purevjav2012molecularbasisfor pages 2-3)

No DCM1KK-specific modifier gene is validated. More generally, the 2024 genetic-DCM literature supports a spectrum from monogenic through oligogenic and polygenic susceptibility. In a 2024 meta-analysis of 57 studies, the median fraction of adult/mixed DCM cohorts classified as genetic was **20.2%**; pediatric genetic DCM had a weighted mean of **21.3%**. These are general DCM data, not MYPN-specific. (myers2024prevalenceofgenetically pages 1-2)

### Environmental and lifestyle risks

No alcohol, infection, medication, pregnancy, occupational exposure, toxin, smoking pattern, or exercise dose has been proven specifically to trigger DCM in MYPN carriers. However, R1088H showed no measurable phenotype in an unstressed cellular system despite a left-ventricular effect in vivo, and Mypn-null mice deteriorate markedly under pressure overload. These observations support—but do not prove—a two-hit model in which mechanical or environmental stress unmasks genetic susceptibility. (duboscqbidot2008mutationsinthe pages 5-6)

General DCM-relevant acquired stressors include heavy alcohol exposure, anthracyclines and other cardiotoxic drugs, myocarditis, pregnancy/peripartum stress, uncontrolled hypertension, tachyarrhythmia, nutritional/metabolic disease, and illicit stimulants. In genetic DCM broadly, inherited susceptibility can modify alcohol- or chemotherapy-associated disease. (arnautu2024riskassessmentand pages 1-2)

### Protective factors

No protective MYPN allele or DCM1KK-specific dietary, pharmacological, or lifestyle factor is established. Rational risk reduction includes blood-pressure control, avoidance of heavy alcohol and stimulants, careful management of cardiotoxic therapy, prompt assessment of myocarditis-like symptoms, adherence to heart-failure therapy, and individualized exercise counseling. These are tertiary or risk-modifying measures rather than proven prevention of MYPN penetrance.

## 3. Phenotypes

The phenotype evidence is sparse and variably ascertained. Reported carrier disease was chiefly isolated, adult-onset DCM, but onset and severity were variable. (duboscqbidot2008mutationsinthe pages 3-3)

- **Ventricular dilation and systolic dysfunction:** defining clinical signs; typically left ventricular, potentially biventricular. Suggested terms: **HP:0001644 Dilated cardiomyopathy**, decreased left-ventricular ejection fraction, left-ventricular dilatation.
- **Heart failure:** exertional dyspnea, fatigue, reduced exercise tolerance, orthopnea, edema, and congestion are expected when systolic dysfunction becomes symptomatic. Suggested terms: **HP:0001635 Heart failure**, **HP:0002094 Dyspnea**, exercise intolerance, fatigue, peripheral edema. These symptom frequencies are not quantified in DCM1KK.
- **Arrhythmia/conduction disease:** present in a minority of the broader discovery cohort, but not quantified by MYPN variant. Suggested terms: **HP:0011675 Cardiac arrhythmia**, **HP:0001678 Abnormality of cardiac conduction**. (duboscqbidot2008mutationsinthe pages 3-3)
- **Fibrosis:** supported strongly in stressed Mypn-null mice and is plausible in human DCM, but variant-specific human CMR or histological prevalence is unknown.
- **Skeletal-muscle findings:** mild muscular dystrophy was present in part of the broader screened cohort, but it cannot be assigned to DCM1KK carriers as a defining feature. Biallelic MYPN myopathy is a distinct allelic disorder.

No DCM1KK-specific frequency percentages, neonatal phenotype, behavioral changes, validated laboratory signature, EQ-5D, SF-36, PROMIS score, or per-phenotype quality-of-life study is available. Functionally, symptomatic heart failure can impair mobility, employment, sleep, exercise, and psychosocial well-being, but that statement is extrapolated from general DCM.

## 4. Genetic and molecular information

### Gene and protein

**MYPN** encodes the approximately 147-kDa protein myopalladin. It localizes to the sarcomeric Z-disc and I-band and can shuttle to the nucleus. MYPN tethers or interacts with titin, α-actinin-2, CARP/ANKRD1, desmin, and nebulette, thereby linking sarcomere architecture, mechanosensing, intercalated-disc organization, and transcriptional responses. (purevjav2012molecularbasisfor pages 2-2, purevjav2012molecularbasisfor pages 2-3)

### Reported variants

1. **I83fsX105 / exon-2 ins/del_T735:** heterozygous frameshift with an aberrant 22-amino-acid tail. Patient-derived RNA showed wild-type but not premature-termination transcript, supporting nonsense-mediated decay and haploinsufficiency. Historical nomenclature must be remapped to the current MANE transcript before clinical use. (duboscqbidot2008mutationsinthe pages 5-6, duboscqbidot2008mutationsinthe pages 7-8)
2. **R1088H:** familial heterozygous missense variant with cosegregation and reduced myopalladin localization at α-actinin-positive Z-discs in explanted left-ventricular myocardium; right-ventricular localization was reported as normal. (duboscqbidot2008mutationsinthe pages 3-3, duboscqbidot2008mutationsinthe pages 5-6)
3. **P1112L and V1195M:** apparently sporadic heterozygous missense variants. Expression in neonatal-rat cardiomyocytes produced myopalladin mislocalization, sarcomeric disorganization, and premature cell death, leading to a proposed dominant-negative mechanism. (duboscqbidot2008mutationsinthe pages 1-2, duboscqbidot2008mutationsinthe pages 5-6, duboscqbidot2008mutationsinthe pages 7-8)
4. **Y20C, I213V, Y339F, A611T, A882T, F954L:** reported in a later DCM cohort. Y20C was de novo in reported cardiomyopathy cases, was also observed in HCM, carried dbSNP **rs140148105**, and had a historical 1000 Genomes frequency near 0.001. Its pleiotropy reduces DCM1KK specificity. (purevjav2012molecularbasisfor pages 2-2, purevjav2012molecularbasisfor pages 2-3)

These historical reports predate current population databases and disease-specific ACMG refinements. Absence from 400 or 1,020 controls is not equivalent to rarity in gnomAD. Current ClinVar assertions, gnomAD ancestry-specific frequency, read quality, splice predictions, segregation, and phenotype concordance must be rechecked. A VUS is neither diagnostic nor appropriate for predictive cascade testing.

### Origin, chromosomal and epigenetic findings

The proposed variants are **germline**, not somatic. No recurrent MYPN copy-number alteration, translocation, inversion, aneuploidy, disease-specific DNA-methylation pattern, histone mark, or chromatin-accessibility signature has been established for DCM1KK. CMA, karyotyping, and FISH are therefore not first-line tests for isolated DCM1KK unless syndromic features suggest a broader genomic disorder.

## 5. Environmental information

DCM1KK is not infectious, transmissible, occupational, or zoonotic. Viral infection may trigger myocarditis and a DCM phenotype in genetically susceptible people generally, but no pathogen–MYPN interaction has been demonstrated. Environmental assessment should nevertheless document alcohol, cocaine/amphetamine exposure, chemotherapy or immunotherapy, pregnancy, viral prodrome, endocrine/nutritional disease, hypertension, sustained tachycardia, and family history because identifying a competing or interacting cause changes management.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. A heterozygous MYPN loss-of-function or function-altering missense variant **leads to** reduced normal myopalladin or production of dysfunctional myopalladin.
2. Altered myopalladin **leads to** impaired interaction/localization within the Z-disc–I-band complex involving titin, α-actinin-2, CARP/ANKRD1, desmin, and nebulette. (duboscqbidot2008mutationsinthe pages 5-6, purevjav2012molecularbasisfor pages 2-2)
3. Defective scaffolding and mechanosensing **lead to** disordered myofibrillogenesis and sarcomere organization; for some missense variants, a dominant-negative effect is inferred rather than proven in patients. (duboscqbidot2008mutationsinthe pages 7-8)
4. Sarcomere disorganization **results in** reduced active tension and abnormal passive mechanics; MYPN-null mouse data also support delayed calcium release/reuptake. The calcium step is demonstrated in mice but inferred for human DCM1KK.
5. Reduced contractile reserve **leads to** systolic dysfunction, which is amplified by mechanical stress; stress sensitivity is supported by severe deterioration after pressure overload in Mypn-null mice.
6. **Branch A:** persistent mechanical dysfunction **leads to** chamber remodeling and ventricular dilation.
7. **Branch B:** cardiomyocyte injury/death and stress signaling **lead to** fibroblast activation, extracellular-matrix deposition, and fibrosis; this is demonstrated chiefly in models and general DCM, not historical MYPN-carrier tissue.
8. Dilation plus fibrosis **results in** lower ejection fraction, functional mitral regurgitation, neurohormonal activation, and clinical heart failure.
9. Structural remodeling **can lead to** atrial or ventricular arrhythmia, conduction disease, thromboembolism, progressive pump failure, transplantation, or death, although MYPN-specific event rates are unavailable.

### Pathways, cells, and ontology suggestions

Upstream biology is structural/mechanosensory rather than a single canonical kinase pathway. CARP-associated transcriptional signaling, nuclear shuttling, actin/titin anchoring, calcium handling, and stress-response programs are implicated. Y20C reduced CARP binding and failed normal nuclear translocation; Q529X disrupted recruitment of α-actinin-2, desmin, and CARP. (purevjav2012molecularbasisfor pages 1-2, purevjav2012molecularbasisfor pages 8-10)

Suggested GO concepts include **Z disc (GO:0030018)**, **sarcomere (GO:0030017)**, I band, myofibril assembly, sarcomere organization, cardiac-muscle contraction, actin binding, titin binding, response to mechanical stimulus, calcium-ion homeostasis, regulation of cell death, extracellular-matrix organization, and cardiac-muscle-tissue development. Suggested Cell Ontology concepts are cardiomyocyte, ventricular cardiomyocyte, cardiac fibroblast, endothelial cell, macrophage, and cardiac conduction cell.

No DCM1KK-specific metabolomic or lipidomic abnormality has been defined. Energetic failure, oxidative stress, inflammation, and fibrosis are plausible downstream features of advanced DCM but should not be annotated as demonstrated MYPN-primary lesions.

### Advanced profiling

No MYPN-stratified single-cell, spatial-transcriptomic, proteomic, metabolomic, lipidomic, or epigenomic study was identified. General DCM studies should be stored separately. A 2024 genetic-DCM meta-analysis found broad under-detection from incomplete evaluation of intronic, mitochondrial, structural, and non-coding variants and advocated long-read WGS studies. (myers2024prevalenceofgenetically pages 1-2)

## 7. Anatomical structures affected

- **Primary organ:** heart (**UBERON:0000948**), principally ventricular myocardium.
- **Primary site:** left-ventricular myocardium; right-ventricular involvement is possible in biventricular DCM.
- **Tissues/cells:** cardiac muscle tissue and ventricular cardiomyocytes; cardiac fibroblasts become important downstream during fibrosis.
- **Subcellular compartments:** Z-disc, I-band, sarcomere/myofibril, intercalated disc, cytoplasm, and nucleus. Y20C models additionally showed altered desmin, desmoplakin, connexin-43, and vinculin organization. (purevjav2012molecularbasisfor pages 8-10)
- **Secondary organs:** lungs, liver, kidneys, skeletal muscle, and peripheral tissues may be affected secondarily by congestion or low output, but no characteristic DCM1KK extra-cardiac distribution is established.
- **Lateralization:** not applicable; chamber involvement rather than right–left body asymmetry is relevant.

## 8. Temporal development

The best historical estimate is adult onset, with mean diagnosis at **40.2 years**, but the large standard deviation (**18.3 years**) indicates broad variability. Disease can remain subclinical before dilation or symptoms emerge. (duboscqbidot2008mutationsinthe pages 3-3)

A practical course is: genotype-positive/phenotype-negative state → early electrical or subtle imaging abnormalities → overt ventricular dilation and systolic dysfunction → symptomatic chronic heart failure → recovery/remission, stable treated disease, arrhythmia, or advanced heart failure. This staging is extrapolated from general inherited DCM. No MYPN-specific median age of penetrance, annual progression rate, remission rate, or critical intervention window is known.

Recovery of ejection fraction may occur under guideline-directed therapy in DCM generally, but genetic substrate may persist; therapy and surveillance should not automatically be withdrawn after apparent reverse remodeling.

## 9. Inheritance and population

The likely historical model is **autosomal dominant with incomplete, age-dependent penetrance and variable expressivity**. De novo disease is possible, as illustrated by Y20C reports, but its frequency is unknown. (duboscqbidot2008mutationsinthe pages 3-3, purevjav2012molecularbasisfor pages 2-3)

There is no evidence for anticipation, a recurrent founder variant, a role for consanguinity in dominant DCM1KK, or a known sex ratio. Biallelic MYPN variants cause distinct recessive skeletal-myopathy phenotypes and should not be conflated with dominant DCM1KK.

Population prevalence and incidence of DCM1KK are unknown. The original estimate that MYPN variants accounted for 3–4% of European-descent DCM cases came from a small, pre-gnomAD cohort and likely overstates clinically established pathogenic variation today. (duboscqbidot2008mutationsinthe pages 1-2)

For context only, genetic DCM constituted a median **20.2%** of adult/mixed DCM cohorts in the 2024 meta-analysis, with substantial geographic and methodological heterogeneity. (myers2024prevalenceofgenetically pages 1-2)

## 10. Diagnostics

### Clinical evaluation

Diagnosis requires both a compatible DCM phenotype and credible etiologic evidence. Recommended evaluation includes:

- three-generation pedigree and examination for syndromic or neuromuscular signs;
- ECG and ambulatory monitoring for conduction disease, atrial arrhythmia, and ventricular ectopy;
- transthoracic echocardiography for chamber dimensions, ejection fraction, strain, valve function, and right-heart involvement;
- cardiac MRI for volumes, function, edema, and late-gadolinium-enhancement fibrosis;
- BNP/NT-proBNP, high-sensitivity troponin, complete blood count, electrolytes, renal/liver/thyroid studies, iron indices, and other etiologic tests as indicated;
- ischemic assessment when clinically appropriate;
- endomyocardial biopsy only for selected suspected myocarditis, infiltrative, inflammatory, or rapidly progressive presentations—not routinely for genetic DCM.

Differential diagnoses include ischemic cardiomyopathy, hypertensive or valvular remodeling, myocarditis, alcohol/toxin/chemotherapy-related cardiomyopathy, peripartum cardiomyopathy, tachycardia-induced cardiomyopathy, endocrine/metabolic disease, muscular dystrophy, mitochondrial disease, arrhythmogenic cardiomyopathy, and non-dilated left-ventricular cardiomyopathy.

### Genetic testing

A contemporary curated cardiomyopathy panel is preferred over isolated MYPN sequencing because DCM is highly heterogeneous and MYPN evidence is limited. Testing should include sequence and deletion/duplication analysis of high-evidence DCM genes. WES or WGS can be considered after negative panel testing, particularly for syndromic, pediatric, recessive, structural, intronic, or non-coding hypotheses. RNA sequencing may resolve suspected splice variants when informative tissue or validated assays are available. The 2024 meta-analysis specifically identified under-investigation of structural and non-coding variation as an important diagnostic gap. (myers2024prevalenceofgenetically pages 1-2)

Karyotyping, CMA, FISH, mitochondrial sequencing, or repeat-expansion testing should be phenotype-driven rather than routine for isolated MYPN-associated DCM.

### Screening

For a convincingly pathogenic/likely pathogenic familial variant, offer genetic counseling and targeted cascade testing. Genotype-positive relatives require longitudinal ECG and imaging even when asymptomatic. If no credible familial variant is identified, first-degree relatives still need phenotype screening because a negative panel does not exclude inherited DCM. Prenatal or preimplantation testing is technically possible only after a familial pathogenic variant is established and after nondirective counseling.

## 11. Outcomes and prognosis

No DCM1KK-specific survival curve, five- or ten-year survival, transplantation rate, sudden-death rate, recovery rate, or validated prognostic biomarker exists. General DCM outcomes should not be entered as subtype-specific facts.

A 2024 inherited-DCM review reported a general DCM five-year survival estimate near **50%**, but this combines heterogeneous eras, causes, and severities and is unsuitable as a DCM1KK estimate. (arnautu2024riskassessmentand pages 1-2)

Relevant general prognostic factors include baseline ejection fraction, right-ventricular dysfunction, persistent congestion, ventricular arrhythmia, conduction disease, extensive CMR fibrosis, failure of reverse remodeling, recurrent hospitalization, renal dysfunction, and pathogenic variants in established high-arrhythmic-risk genes. MYPN is not currently established as such a high-risk genotype. Potential complications are progressive heart failure, functional mitral regurgitation, atrial fibrillation, ventricular tachyarrhythmia, thromboembolism, stroke, device therapy, mechanical support, transplantation, and death.

## 12. Treatment and real-world implementation

No therapy corrects MYPN dysfunction, and no MYPN-specific treatment-response study was found. Management follows phenotype-based DCM/HFrEF care:

1. **Foundational pharmacotherapy:** ARNI, or ACE inhibitor/ARB when ARNI is unsuitable; evidence-based beta blocker; mineralocorticoid-receptor antagonist; and an SGLT2 inhibitor. Loop diuretics treat congestion. Suggested NCIT concepts: Pharmacologic Therapy, Angiotensin Receptor–Neprilysin Inhibitor Therapy, Beta Blocker Therapy, Mineralocorticoid Receptor Antagonist Therapy, SGLT2 Inhibitor Therapy, and Diuretic Therapy.
2. **Additional therapy:** ivabradine, hydralazine/isosorbide dinitrate, digoxin, iron replacement, anticoagulation, or antiarrhythmic therapy when standard indications are met. Routine anticoagulation is not indicated solely for DCM in sinus rhythm.
3. **Devices:** ICD for accepted primary- or secondary-prevention indications; CRT for qualifying ejection fraction, QRS morphology/duration, and symptoms. MYPN status alone does not justify an ICD. Suggested NCIT concepts: Implantable Cardioverter-Defibrillator Therapy and Cardiac Resynchronization Therapy.
4. **Advanced heart failure:** referral for ventricular-assist device and heart transplantation when refractory. Suggested NCIT concepts: Ventricular Assist Device and Heart Transplantation.
5. **Supportive/rehabilitative care:** sodium and fluid advice individualized to congestion, vaccination, smoking cessation, supervised cardiac rehabilitation, psychosocial care, reproductive counseling, and exercise prescription based on phenotype and arrhythmic risk.

No established MYPN pharmacogenomic rule exists. No disease-specific gene replacement, AAV, CRISPR, antisense, siRNA, mRNA, cell therapy, or immunotherapy trial was identified. Therefore, gene-therapy and RNA-therapy concepts should be marked **preclinical/not available**, not listed as treatment options.

## 13. Prevention

- **Primary prevention:** no intervention is proven to prevent penetrance. Counsel at-risk families regarding inheritance, avoid heavy alcohol and illicit stimulants, control hypertension and metabolic risk, and minimize cardiotoxic exposure where alternatives exist.
- **Secondary prevention:** pedigree-based case finding, cascade testing for established pathogenic variants, and serial ECG/imaging permit treatment before advanced remodeling.
- **Tertiary prevention:** guideline-directed therapy, arrhythmia surveillance, indicated ICD/CRT, vaccination, rehabilitation, and early advanced-heart-failure referral reduce complications.
- **Reproductive prevention/options:** genetic counseling, prenatal diagnosis, and preimplantation genetic testing may be discussed only for a clearly pathogenic familial variant.
- **Immunization:** no vaccine prevents DCM1KK; routine influenza, COVID-19, and pneumococcal vaccination may reduce decompensation risk in patients with heart failure.

There is no population newborn-screening or carrier-screening program for DCM1KK.

## 14. Other species and natural disease

No convincing naturally occurring orthologous MYPN-associated DCM1KK syndrome was identified in dogs, cats, livestock, or wildlife. Canine and feline DCM occurs naturally but should not be attributed to MYPN without breed- and variant-specific evidence. There is no transmission or zoonotic potential.

The relevant experimental species is **Mus musculus, NCBI Taxon 10090**; neonatal-rat cardiomyocytes derive from **Rattus norvegicus, Taxon 10116**. Orthologous myopalladin biology is sufficiently conserved to model sarcomeric function, but species differences in heart rate, loading, lifespan, and transgene expression limit clinical translation.

## 15. Model organisms and experimental systems

### MYPN knockout mouse

Mypn-null mice develop mild chamber dilation and systolic dysfunction with reduced myofibrillar isometric tension and increased resting tension at long sarcomere lengths. Following transverse-aortic constriction, they rapidly develop severe dilation, systolic dysfunction, fibrosis, fetal-gene reactivation, intercalated-disc abnormalities, altered calsequestrin-2/desmoplakin/SORBS2 abundance, delayed calcium release and reuptake, and reduced calcium-spark amplitude. This model strongly supports a role for MYPN in contractile mechanics, calcium handling, and response to load, but it models complete loss better than heterozygous missense disease.

### Variant-specific mice

Cardiac-restricted Y20C transgenic mice developed a predominantly hypertrophic phenotype, reduced ejection fraction, abnormal terminal Z-disc/intercalated-disc organization, and altered desmin, desmoplakin, connexin-43, and vinculin. The model demonstrates variant dysfunction and pleiotropy but has limited fidelity for human DCM1KK. (purevjav2012molecularbasisfor pages 8-10, purevjav2012molecularbasisfor pages 1-2)

Q529X knock-in models primarily reproduce restrictive-cardiomyopathy biology and should not be used as direct DCM1KK models.

### Cellular systems

Neonatal-rat cardiomyocytes expressing P1112L or V1195M showed abnormal localization, myofibrillar disruption, and increased death; patient-derived lymphoblastoid RNA supported loss of the I83fsX105 transcript. (duboscqbidot2008mutationsinthe pages 1-2, duboscqbidot2008mutationsinthe pages 7-8)

No well-validated patient-derived MYPN-DCM iPSC-cardiomyocyte, engineered-heart-tissue, organoid, CRISPR isogenic pair, or high-throughput rescue screen was identified. Such systems are a priority because they could test variant-specific contractility, mechanostress, calcium cycling, dominant-negative effects, and correction strategies under human genetic backgrounds.

## Recent developments and expert assessment

The most important 2023–2024 development is not a MYPN-specific treatment but a change in how inherited DCM is evaluated: phenotype-first cardiomyopathy classification is now combined with multimodality imaging, careful gene-validity assessment, segregation, and family screening. At the same time, broader sequencing has revealed that many historically proposed DCM genes have weak evidence, making overdiagnosis from large panels a major concern.

The 2024 meta-analysis summarized this uncertainty directly: adult/mixed cohorts had a median genetic-DCM prevalence of **20.2%**, but estimates varied substantially and probably missed structural, intronic, mitochondrial, and non-coding causes. Its abstract conclusion was that evidence “may underestimate the genetic contributions due to limited screening and detection,” and it called for long-read WGS and large genotype–phenotype cohorts. (myers2024prevalenceofgenetically pages 1-2)

For DCM1KK, the expert interpretation is therefore conservative: MYPN is biologically compelling and supported by historical human and model evidence, but variant causality must be judged case by case. The highest-priority research needs are contemporary reanalysis of historical variants, international MYPN carrier registries, quantitative penetrance and outcome studies, myocardial/iPSC functional validation, and stress-exposure analyses.

## Selected primary and authoritative references

- Duboscq-Bidot L, et al. **Mutations in the Z-band protein myopalladin gene and idiopathic dilated cardiomyopathy.** *Cardiovascular Research.* 2008;77:118–125. DOI/URL: https://doi.org/10.1093/cvr/cvm015. PMID: **18006477**. Foundational human MYPN–DCM cohort and functional study. (duboscqbidot2008mutationsinthe pages 1-2, duboscqbidot2008mutationsinthe pages 3-3)
- Purevjav E, et al. **Molecular basis for clinical heterogeneity in inherited cardiomyopathies due to myopalladin mutations.** *Human Molecular Genetics.* Published online January 27, 2012; print May 2012;21:2039–2053. DOI/URL: https://doi.org/10.1093/hmg/dds022. PMID: **22286171**. Human, in-vitro, and mouse evidence for MYPN allelic heterogeneity. (purevjav2012molecularbasisfor pages 1-2)
- Myers MC, et al. **Prevalence of Genetically Associated Dilated Cardiomyopathy: A Systematic Literature Review and Meta-Analysis.** *Cardiology Research.* August 2024;15:233–245. DOI/URL: https://doi.org/10.14740/cr1680. General genetic-DCM epidemiology, not DCM1KK-specific. (myers2024prevalenceofgenetically pages 1-2)
- Arnautu D-A, et al. **Risk Assessment and Personalized Treatment Options in Inherited Dilated Cardiomyopathies.** *Biomedicines.* July 2024;12:1643. DOI/URL: https://doi.org/10.3390/biomedicines12081643. General inherited-DCM synthesis. (arnautu2024riskassessmentand pages 1-2)

## Knowledge gaps to encode explicitly

Subtype-specific prevalence, incidence, penetrance, sex ratio, ancestry distribution, founder effects, quality-of-life scores, natural-history stages, remission frequency, five- and ten-year survival, sudden-death risk, transplantation rate, prognostic biomarkers, pharmacogenomics, treatment-response rates, natural veterinary disease, and clinical trials are **not available**. No DCM1KK-specific epigenomic, single-cell, spatial, proteomic, metabolomic, or lipidomic signature is established. These fields should remain null or be labeled “unknown,” rather than populated with unqualified general-DCM estimates.

References

1. (OpenTargets Search: Dilated cardiomyopathy 1KK): Open Targets Query (Dilated cardiomyopathy 1KK, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (duboscqbidot2008mutationsinthe pages 1-2): Laëtitia Duboscq-Bidot, Peng Xu, Philippe Charron, Nathalie Neyroud, Gilles Dilanian, Alain Millaire, Valéria Bors, Michel Komajda, and Eric Villard. Mutations in the z-band protein myopalladin gene and idiopathic dilated cardiomyopathy. Cardiovascular research, 77 1:118-25, Sep 2008. URL: https://doi.org/10.1093/cvr/cvm015, doi:10.1093/cvr/cvm015. This article has 136 citations and is from a domain leading peer-reviewed journal.

3. (purevjav2012molecularbasisfor pages 2-2): Enkhsaikhan Purevjav, Takuro Arimura, Sibylle Augustin, Anne-Cecile Huby, Ken Takagi, Shinichi Nunoda, Debra L. Kearney, Michael D. Taylor, Fumio Terasaki, Johan M. Bos, Steve R. Ommen, Hiroki Shibata, Megumi Takahashi, Manatsu Itoh-Satoh, William J. McKenna, Ross T. Murphy, Siegfried Labeit, Yoichi Yamanaka, Noboru Machida, Jeong-Euy Park, Peta M.A. Alexander, Robert G. Weintraub, Yasushi Kitaura, Michael J. Ackerman, Akinori Kimura, and Jeffrey A. Towbin. Molecular basis for clinical heterogeneity in inherited cardiomyopathies due to myopalladin mutations. Human molecular genetics, 21 9:2039-53, May 2012. URL: https://doi.org/10.1093/hmg/dds022, doi:10.1093/hmg/dds022. This article has 127 citations and is from a domain leading peer-reviewed journal.

4. (duboscqbidot2008mutationsinthe pages 3-3): Laëtitia Duboscq-Bidot, Peng Xu, Philippe Charron, Nathalie Neyroud, Gilles Dilanian, Alain Millaire, Valéria Bors, Michel Komajda, and Eric Villard. Mutations in the z-band protein myopalladin gene and idiopathic dilated cardiomyopathy. Cardiovascular research, 77 1:118-25, Sep 2008. URL: https://doi.org/10.1093/cvr/cvm015, doi:10.1093/cvr/cvm015. This article has 136 citations and is from a domain leading peer-reviewed journal.

5. (duboscqbidot2008mutationsinthe pages 5-6): Laëtitia Duboscq-Bidot, Peng Xu, Philippe Charron, Nathalie Neyroud, Gilles Dilanian, Alain Millaire, Valéria Bors, Michel Komajda, and Eric Villard. Mutations in the z-band protein myopalladin gene and idiopathic dilated cardiomyopathy. Cardiovascular research, 77 1:118-25, Sep 2008. URL: https://doi.org/10.1093/cvr/cvm015, doi:10.1093/cvr/cvm015. This article has 136 citations and is from a domain leading peer-reviewed journal.

6. (duboscqbidot2008mutationsinthe pages 7-8): Laëtitia Duboscq-Bidot, Peng Xu, Philippe Charron, Nathalie Neyroud, Gilles Dilanian, Alain Millaire, Valéria Bors, Michel Komajda, and Eric Villard. Mutations in the z-band protein myopalladin gene and idiopathic dilated cardiomyopathy. Cardiovascular research, 77 1:118-25, Sep 2008. URL: https://doi.org/10.1093/cvr/cvm015, doi:10.1093/cvr/cvm015. This article has 136 citations and is from a domain leading peer-reviewed journal.

7. (purevjav2012molecularbasisfor pages 1-2): Enkhsaikhan Purevjav, Takuro Arimura, Sibylle Augustin, Anne-Cecile Huby, Ken Takagi, Shinichi Nunoda, Debra L. Kearney, Michael D. Taylor, Fumio Terasaki, Johan M. Bos, Steve R. Ommen, Hiroki Shibata, Megumi Takahashi, Manatsu Itoh-Satoh, William J. McKenna, Ross T. Murphy, Siegfried Labeit, Yoichi Yamanaka, Noboru Machida, Jeong-Euy Park, Peta M.A. Alexander, Robert G. Weintraub, Yasushi Kitaura, Michael J. Ackerman, Akinori Kimura, and Jeffrey A. Towbin. Molecular basis for clinical heterogeneity in inherited cardiomyopathies due to myopalladin mutations. Human molecular genetics, 21 9:2039-53, May 2012. URL: https://doi.org/10.1093/hmg/dds022, doi:10.1093/hmg/dds022. This article has 127 citations and is from a domain leading peer-reviewed journal.

8. (purevjav2012molecularbasisfor pages 2-3): Enkhsaikhan Purevjav, Takuro Arimura, Sibylle Augustin, Anne-Cecile Huby, Ken Takagi, Shinichi Nunoda, Debra L. Kearney, Michael D. Taylor, Fumio Terasaki, Johan M. Bos, Steve R. Ommen, Hiroki Shibata, Megumi Takahashi, Manatsu Itoh-Satoh, William J. McKenna, Ross T. Murphy, Siegfried Labeit, Yoichi Yamanaka, Noboru Machida, Jeong-Euy Park, Peta M.A. Alexander, Robert G. Weintraub, Yasushi Kitaura, Michael J. Ackerman, Akinori Kimura, and Jeffrey A. Towbin. Molecular basis for clinical heterogeneity in inherited cardiomyopathies due to myopalladin mutations. Human molecular genetics, 21 9:2039-53, May 2012. URL: https://doi.org/10.1093/hmg/dds022, doi:10.1093/hmg/dds022. This article has 127 citations and is from a domain leading peer-reviewed journal.

9. (purevjav2012molecularbasisfor pages 8-10): Enkhsaikhan Purevjav, Takuro Arimura, Sibylle Augustin, Anne-Cecile Huby, Ken Takagi, Shinichi Nunoda, Debra L. Kearney, Michael D. Taylor, Fumio Terasaki, Johan M. Bos, Steve R. Ommen, Hiroki Shibata, Megumi Takahashi, Manatsu Itoh-Satoh, William J. McKenna, Ross T. Murphy, Siegfried Labeit, Yoichi Yamanaka, Noboru Machida, Jeong-Euy Park, Peta M.A. Alexander, Robert G. Weintraub, Yasushi Kitaura, Michael J. Ackerman, Akinori Kimura, and Jeffrey A. Towbin. Molecular basis for clinical heterogeneity in inherited cardiomyopathies due to myopalladin mutations. Human molecular genetics, 21 9:2039-53, May 2012. URL: https://doi.org/10.1093/hmg/dds022, doi:10.1093/hmg/dds022. This article has 127 citations and is from a domain leading peer-reviewed journal.

10. (myers2024prevalenceofgenetically pages 1-2): Michael C. Myers, Su Wang, Yue Zhong, Sonomi Maruyama, Cindy Bueno, Arnaud Bastien, Mir Sohail Fazeli, and Negar Golchin. Prevalence of genetically associated dilated cardiomyopathy: a systematic literature review and meta-analysis. Cardiology Research, 15:233-245, Aug 2024. URL: https://doi.org/10.14740/cr1680, doi:10.14740/cr1680. This article has 11 citations.

11. (arnautu2024riskassessmentand pages 1-2): Diana-Aurora Arnautu, Dragos Cozma, Ioan-Radu Lala, Sergiu-Florin Arnautu, Mirela-Cleopatra Tomescu, and Minodora Andor. Risk assessment and personalized treatment options in inherited dilated cardiomyopathies: a narrative review. Biomedicines, 12:1643, Jul 2024. URL: https://doi.org/10.3390/biomedicines12081643, doi:10.3390/biomedicines12081643. This article has 9 citations.

## Artifacts

- [Edison artifact artifact-00](Dilated_Cardiomyopathy_1KK-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 4 |
| Resolved | 4 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 4 |
| On topic | 1 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |

Every term resolved, and every label the report gave matched.