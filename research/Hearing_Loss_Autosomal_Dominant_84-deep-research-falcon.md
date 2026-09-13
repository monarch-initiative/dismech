---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-03T23:48:20.376872'
end_time: '2026-09-04T00:01:35.388890'
duration_seconds: 795.01
template_file: templates/disease_pathophysiology_research.md
template_sha: 1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666
template_variables:
  disease_name: Hearing Loss Autosomal Dominant 84
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 16
reference_validation:
  total_references: 6
  verified: 6
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 6
  on_topic: 5
  validator_version: 0.2.1
term_validation:
  total_terms: 12
  verified: 11
  not_found: 0
  obsolete: 1
  unverifiable: 0
  confabulation_rate: 0.0
  obsolete_terms:
  - term_id: GO:0004012
    ontology_label: GO_0004012
    replaced_by: GO:0140326
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Hearing_Loss_Autosomal_Dominant_84-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hearing Loss Autosomal Dominant 84
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hearing Loss Autosomal Dominant 84** covering all of the
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
- **Disease Name:** Hearing Loss Autosomal Dominant 84
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hearing Loss Autosomal Dominant 84** covering all of the
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


# Hearing Loss, Autosomal Dominant 84 (DFNA84): Disease-Characteristics Report

**Target category:** rare Mendelian, autosomal-dominant hearing disorder  
**Core gene:** **ATP11A**, encoding ATPase phospholipid-transporting 11A, a P4-type phospholipid flippase  
**Evidence cutoff:** literature retrieved through 2025, with emphasis on 2023–2024 evidence. Because this is an exceptionally rare disorder, most disease-specific knowledge comes from one extended family, supplemented by allelic ATP11A families and model systems.

## Executive summary and nomenclature caution

Hearing loss, autosomal dominant 84 is best understood as the ATP11A-associated disorder originally phenotyped as **AUNA2**, a slowly progressive, nonsyndromic auditory synaptopathy/auditory neuropathy. The defining pedigree contained 11 affected people over four generations. Hearing may appear normal in the first decade even though auditory-brainstem responses (ABRs) are already abnormal; clinically recognized loss usually begins at 10–20 years, initially affects middle and high frequencies, and can progress to severe or profound pan-frequency loss in later adulthood. Otoacoustic emissions (OAEs) and cochlear microphonics may initially be preserved but deteriorate in advanced disease (loh2021atp11acausesautosomaldominanta pages 22-25, loh2021atp11acausesautosomaldominanta pages 25-29).

A major curation issue is that other dominant ATP11A-associated families were published under the historical **DFNA33** locus. Those families provide allelic support for ATP11A-related progressive hearing loss, but should not automatically be relabeled as the original DFNA84/AUNA2 pedigree. A 2023 reanalysis also found improbable haplotype assignments in the original German DFNA33 pedigree and did not resolve that family as ATP11A-related (pater2022autosomaldominantnonsyndromic pages 9-11, vona2023unravelinghaplotypeerrors pages 2-4).

The evidence base is summarized below.

| Domain | Key finding | Evidence type | Evidence strength / limitations |
|---|---|---|---|
| Identifiers and nomenclature | **Hearing loss, autosomal dominant 84 (DFNA84)** refers to the ATP11A-associated disorder reported as **autosomal-dominant auditory neuropathy type 2 (AUNA2)**. Historical ATP11A families were mapped to **DFNA33 (13q34)**; DFNA33 and DFNA84/AUNA2 should not be treated as automatically interchangeable disease labels. | Curated disease nomenclature plus human linkage and molecular studies | Strong ATP11A–dominant hearing-loss association, but locus naming is historically inconsistent and should be retained with provenance. The German DFNA33 pedigree was later found to contain improbable haplotype assignments and was not resolved as ATP11A-related (vona2023unravelinghaplotypeerrors pages 2-4). |
| Causal lesion in AUNA2/DFNA84 | A heterozygous **5,500-bp germline deletion**, GRCh38 chr13:112877723–112883222, described as **ATP11A c.3327+1782del5500**, removes the alternative terminal coding exons 29a/29b. It causes aberrant use of an alternative last exon while the mutant transcript escapes nonsense-mediated decay (loh2021atp11acausesautosomaldominanta pages 25-29). | Human four-generation pedigree; linkage, WGS, segregation, patient RNA, and in-vitro functional assays | Strong disease-specific evidence: deletion found at the linked locus and associated with the phenotype; stable biallelic RNA and altered splicing were demonstrated. Published evidence derives principally from one extended family, limiting genotype–phenotype generalization. |
| Human phenotype | Eleven individuals across four generations had predominantly **nonsyndromic, bilateral, symmetric, progressive auditory synaptopathy/neuropathy**. Neurologic examinations did not support generalized hereditary peripheral neuropathy; isolated comorbidities in individual relatives were not shown to be ATP11A manifestations (loh2021atp11acausesautosomaldominanta pages 22-25, loh2021atp11acausesautosomaldominanta pages 25-29). | Human family phenotyping | Strong for the core auditory phenotype within the pedigree; small sample and single-family ascertainment preclude reliable estimates of rare extracochlear manifestations. |
| Audiologic trajectory | Hearing can appear normal in the first decade although ABR is already abnormal. Typical recognized onset is **10–20 years**, initially affecting middle/high frequencies; loss becomes moderate in the third–fourth decades and can progress across all frequencies to severe/profound loss by approximately 40–50 years or later. TEOAEs are initially preserved and commonly disappear only with severe loss; ABR is abnormal or absent, and speech recognition declines with severity (loh2021atp11acausesautosomaldominanta pages 22-25, loh2021atp11acausesautosomaldominanta pages 25-29). | Serial and cross-sectional pure-tone audiometry, monosyllabic speech testing, TEOAE, cochlear microphonics, ABR, and cortical evoked potentials | Detailed disease-specific physiologic evidence. The available observations do not yield a validated annual threshold-shift rate or population-level penetrance estimate. |
| Quantitative audiology | At ages 7–16 years, hearing ranged from normal/abnormal to mild loss with speech recognition of **60–95%**, while ABR could already be pathologic or absent. At ages 38–41, moderate loss accompanied speech recognition of **0–42%** unaided; at ages 46–73, severe/profound loss accompanied **0%** unaided recognition. Hearing aids produced variable, generally limited gains (loh2021atp11acausesautosomaldominanta pages 22-25, loh2021atp11acausesautosomaldominanta pages 25-29). | Human clinical testing | Valuable within-family natural-history data, but based on approximately ten tested relatives at different ages rather than a prospective longitudinal cohort. |
| Molecular mechanism | ATP11A is a plasma-membrane P4-ATPase that, with the β-subunit CDC50A, flips phosphatidylserine and phosphatidylethanolamine from the exoplasmic to cytoplasmic leaflet. The AUNA2 mutant protein reached the plasma membrane normally but showed markedly diminished phosphatidylserine transport, supporting functional loss rather than trafficking failure (loh2021atp11acausesautosomaldominanta pages 1-7, loh2021atp11acausesautosomaldominanta pages 83-88, loh2021atp11acausesautosomaldominant pages 135-139). | Patient-informed HEK293/HEK293T expression, immunocytochemistry, surface biotinylation, and fluorescent-lipid uptake assay | Direct evidence for reduced mutant flippase activity. Downstream disruption of membrane stability, vesicle cycling, calcium handling, synaptic function, apoptosis, or phagocytic removal of auditory cells remains biologically plausible but substantially inferred rather than demonstrated in human cochlea (loh2021atp11acausesautosomaldominanta pages 135-139, loh2021atp11acausesautosomaldominant pages 123-126). |
| Supporting ATP11A allelic families | A 2022 study reported a Newfoundland family and two Jewish Israeli families with variable bilateral progressive SNHL and distinct 3′ ATP11A variants, including **c.3322_3327+2dupGTCCAGGT**, predicted **p.Asn1110ValfsTer43**, and a cryptic-donor variant causing 153-bp intron retention. These were published under **DFNA33**, not as the original AUNA2/DFNA84 pedigree (pater2022autosomaldominantnonsyndromic pages 9-11, pater2021autosomaldominantnonsyndromic pages 1-5, pater2021autosomaldominantnonsyndromic pages 5-7). | Human linkage/WGS, segregation, RT-PCR, cloning, Sanger sequencing, and minigene testing | Moderate-to-strong allelic support that ATP11A disruption causes dominant progressive hearing loss. Phenotypes were described as SNHL rather than fully documented auditory neuropathy, and some transcript/isoform consequences remained unresolved. |
| 2025 zebrafish model | CRISPR loss-of-function **atp11a** zebrafish with 5-bp or 7-bp deletions showed fewer stereocilia and inner-ear hair cells, including abnormalities in maculae and cristae, plus fewer cells in an otic neuromast. Reported stereocilia-analysis groups were wild type **n=17**, heterozygous **n=22**, and homozygous **n=7** (hawkeynoble2025thep4phospholipidflippase pages 14-18). | ATP11A-specific vertebrate loss-of-function model | Strong support for a conserved requirement in ear/hair-cell maintenance, but it does not reproduce the exact human deletion or establish whether human disease is primarily hair-cell, synaptic, or neural. Homozygous fish effects may exceed those of heterozygous human disease. |
| Diagnosis | Confirm auditory neuropathy physiology using pure-tone and speech audiometry together with **ABR** and preserved **OAE and/or cochlear microphonics**, recognizing that emissions may disappear in advanced disease. Molecular evaluation should use a comprehensive hearing-loss panel with validated CNV/SV detection or WGS; suspected ATP11A variants require segregation and, where relevant, RNA/minigene studies because terminal-exon, intronic, and structural lesions can evade routine exome analysis (loh2021atp11acausesautosomaldominanta pages 22-25, loh2021atp11acausesautosomaldominanta pages 25-29, pater2021autosomaldominantnonsyndromic pages 7-10, pater2019amultiomicapproach pages 154-158). | Disease-specific audiology and genomic case-discovery evidence; standard clinical-genetics extrapolation | Strong rationale for combined physiologic and genomic testing. No ATP11A-specific diagnostic criteria, biochemical biomarker, or clinically validated RNA assay exists. |
| Treatment and trials | No approved disease-modifying ATP11A therapy and no ATP11A-targeted clinical trial were identified. Management is supportive: serial audiology, communication accommodations, speech/hearing rehabilitation, appropriately fitted hearing aids, and cochlear-implant evaluation when functional benefit is inadequate. In the reported family, hearing aids gave little benefit and three relatives met implantation criteria, but none had been implanted at assessment (loh2021atp11acausesautosomaldominanta pages 22-25, loh2021atp11acausesautosomaldominanta pages 25-29). | Human family experience plus general auditory-neuropathy practice | Disease-specific treatment evidence is very weak: there are no ATP11A pharmacotherapy, cochlear-implant outcome, gene-therapy, RNA-therapy, or editing trials. Proposed targeting of exposed phosphatidylserine remains speculative and preclinical (pater2021autosomaldominantnonsyndromic pages 10-13). |
| Epidemiology and inheritance gaps | Transmission is autosomal dominant, implying a **50% recurrence risk** to each child of a heterozygous affected person. Disease-specific prevalence, incidence, carrier frequency, sex ratio, measured penetrance, de-novo rate, anticipation, germline mosaicism, and confirmed founder frequency are unavailable. A 99% penetrance value used in linkage analysis was a modeling assumption, not an empirical estimate (pater2021autosomaldominantnonsyndromic pages 5-7). | Mendelian inference and sparse family reports | Inheritance pattern is strong; all population estimates are absent. Reported Newfoundland, Israeli, and German pedigrees cannot be used to calculate population prevalence or ethnic risk. |


*Table: Compact evidence appraisal for ATP11A-associated AUNA2/DFNA84, separating direct human and model findings from allelic support, clinical extrapolation, and unresolved nomenclature or epidemiology.*

## 1. Disease information

### Definition

DFNA84/AUNA2 is a rare, postlingual, progressive, usually bilateral and symmetric sensorineural hearing disorder in which electrophysiology indicates impaired synchronous signaling at the inner-hair-cell synapse, spiral-ganglion neuron, or auditory nerve. It is described as **nonsyndromic** because generalized hereditary peripheral neuropathy or a reproducible extracochlear syndrome was not demonstrated in the defining family (loh2021atp11acausesautosomaldominanta pages 22-25, loh2021atp11acausesautosomaldominanta pages 25-29).

### Identifiers and synonyms

- **Preferred label:** Hearing loss, autosomal dominant 84.
- **Common symbols/names:** **DFNA84**, **AUNA2**, autosomal-dominant auditory neuropathy type 2, ATP11A-related autosomal-dominant auditory synaptopathy/auditory neuropathy, ATP11A-related dominant nonsyndromic hearing loss.
- **Gene:** ATP11A, chromosome **13q34**.
- **Historical locus requiring provenance:** **DFNA33**, OMIM **614211**, was the locus label used in the 2022 ATP11A study; it is not necessarily synonymous with DFNA84 (pater2021autosomaldominantnonsyndromic pages 1-5, vona2023unravelinghaplotypeerrors pages 2-4).
- **OMIM/MONDO/Orphanet:** The retrieved primary texts did not provide a reliably verifiable disease-entry number for DFNA84 or a dedicated MONDO/Orphanet identifier. A knowledge base should therefore map the disease label to ATP11A and retain AUNA2/DFNA84/DFNA33 assertions with source-specific provenance rather than infer an unverified identifier.
- **ICD-10/ICD-11/MeSH:** There is no disease-specific billing code. Broader coding falls under sensorineural hearing loss or auditory neuropathy, with laterality and severity recorded separately.

The evidence is predominantly **aggregated disease-level research data** from pedigrees, audiological examinations, genomic studies, patient-derived RNA, and experimental cells—not routine EHR-derived individual-patient data.

## 2. Etiology

### Causal factor

The initiating cause is a **heterozygous germline ATP11A lesion**. In the defining AUNA2 pedigree, WGS identified a 5,500-bp deletion at GRCh38 chr13:112877723–112883222, described as **c.3327+1782del5500**, removing alternative terminal coding exons 29a and 29b. The deletion produces aberrant terminal-exon use, but the mutant transcript remains stable rather than undergoing nonsense-mediated decay (loh2021atp11acausesautosomaldominanta pages 25-29, loh2021atp11acausesautosomaldominant pages 135-139).

Supporting dominant ATP11A alleles reported in other families include:

- **NM_032189.3:c.3322_3327+2dupGTCCAGGT**, extending exon 28 by 8 bp and predicting **p.Asn1110ValfsTer43**;
- a 3′ cryptic-donor variant reported as **chr13:113534963G>A**, causing retention of 153 intronic bases in several ATP11A transcripts;
- **NM_015205.3:c.1221+5G>C**, reported in 2025 as a **VUS**, not an established causal DFNA84 allele (pater2022autosomaldominantnonsyndromic pages 9-11, pater2021autosomaldominantnonsyndromic pages 5-7, rosso2025unravelingthefunctional pages 5-7).

### Risk factors

- **Genetic:** A pathogenic heterozygous ATP11A allele and a positive autosomal-dominant family history are the principal known risk factors.
- **Environmental:** Noise, ototoxic drugs, infections, and aging can independently worsen hearing, but no ATP11A-specific gene–environment interaction has been demonstrated.
- **Sex, lifestyle, occupational, infectious, or dietary risks:** No disease-specific associations are known.

### Protective factors

No protective ATP11A variants, modifier alleles, diets, drugs, or environmental exposures have been established. Hearing conservation—avoiding hazardous noise and unnecessary ototoxic medication—is prudent tertiary prevention but has not been shown to alter the genetic disease’s natural history.

## 3. Phenotypes

### Core phenotypes and suggested HPO annotations

1. **Progressive sensorineural hearing impairment** — **HP:0000407**, with **progressive hearing impairment HP:0001730**. Usually bilateral and symmetric; initially middle/high-frequency, later extending across frequencies. Severity ranges from normal behavioral thresholds in childhood to profound loss in older adults (loh2021atp11acausesautosomaldominanta pages 22-25, loh2021atp11acausesautosomaldominanta pages 25-29).
2. **Postlingual hearing impairment** — **HP:0008615**. Typical recognized onset is 10–20 years, although electrophysiological abnormalities may precede symptoms (loh2021atp11acausesautosomaldominanta pages 25-29).
3. **Auditory neuropathy spectrum disorder** — use the current HPO auditory-neuropathy term where available; operational phenotype is absent/pathologic ABR with initially preserved OAE and/or cochlear microphonics (loh2021atp11acausesautosomaldominanta pages 22-25).
4. **Abnormal auditory brainstem response** — **HP:0006958**. In the family, ABR was absent or severely abnormal in most tested relatives, sometimes before measurable hearing loss (loh2021atp11acausesautosomaldominanta pages 22-25).
5. **Impaired speech discrimination** — annotate with an HPO term for impaired speech discrimination/word recognition if supported by the deployed HPO release. Unaided monosyllabic recognition fell from 60–95% at ages 7–16 to 0–42% at ages 38–41 and 0% in several people aged 46–73 (loh2021atp11acausesautosomaldominanta pages 22-25, loh2021atp11acausesautosomaldominanta pages 25-29).
6. **Preserved then lost otoacoustic emissions.** TEOAEs were detectable with normal through moderate loss and generally disappeared in severe/profound stages; this is a temporal biomarker rather than an invariant phenotype (loh2021atp11acausesautosomaldominanta pages 22-25, loh2021atp11acausesautosomaldominanta pages 25-29).

### Frequency and severity

The core auditory phenotype occurred in all 11 clinically affected relatives in the defining pedigree. Exact population frequencies cannot be inferred. One seven-year-old had normal pure-tone hearing but pathological ABR; a ten-year-old had mild loss, 90% unaided recognition and absent ABR at 85 dB; a 38-year-old had moderate loss but only 15% word recognition; adults aged 46–73 had severe/profound loss and 0% unaided recognition (loh2021atp11acausesautosomaldominanta pages 22-25).

### Quality-of-life impact

Disease-specific EQ-5D, SF-36, PROMIS, or hearing-quality-of-life scores have not been reported. Expected burdens include difficulty understanding speech—especially in noise—reduced educational or occupational communication, social isolation, and reliance on visual or assistive communication. In auditory neuropathy, temporal dyssynchrony can impair speech perception disproportionately to pure-tone thresholds (loh2021atp11acausesautosomaldominanta pages 19-22).

## 4. Genetic and molecular information

### Gene and protein

**ATP11A** encodes a catalytic P4-ATPase α-subunit that partners with **CDC50A/TMEM30A** and uses ATP to translocate phosphatidylserine (PS) and phosphatidylethanolamine (PE) from the exoplasmic/luminal leaflet to the cytoplasmic leaflet, maintaining membrane-lipid asymmetry (loh2021atp11acausesautosomaldominanta pages 1-7, loh2021atp11acausesautosomaldominanta pages 29-32).

Suggested annotations include **GO:0004012 phospholipid-translocating ATPase activity**, **GO:0045332 phospholipid translocation**, **GO:0097035 regulation of membrane lipid distribution**, **GO:0005886 plasma membrane**, and **GO:0016020 membrane**; term identifiers should be checked against the current GO release before ingestion.

### Variant mechanism

The defining deletion is germline and heterozygous. Patient RNA showed biallelic expression and aberrant splicing rather than simple transcript destruction. In HEK293/HEK293T assays, mutant ATP11A still reached the plasma membrane in a CDC50A-dependent manner but had markedly diminished PS-flipping activity, close to loss-of-function controls. The evidence therefore supports **functional loss/hypomorphic activity**, while dominant-negative action has not been excluded in the relevant cochlear cells (loh2021atp11acausesautosomaldominanta pages 83-88, loh2021atp11acausesautosomaldominant pages 135-139, loh2021atp11acausesautosomaldominanta pages 135-139).

### Population frequency and ACMG classification

The defining 5.5-kb deletion was discovered by WGS and segregated with disease; a precise gnomAD-SV frequency was not supplied in the retrieved evidence. The Newfoundland cryptic-donor variant was absent from local controls and from 202 additional Newfoundland hearing-loss probands. The exon-28 duplication was classified as pathogenic in the 2022 study. By contrast, c.1221+5G>C remained a VUS in 2025 despite in-silico splice predictions and limited segregation information (pater2021autosomaldominantnonsyndromic pages 5-7, rosso2025unravelingthefunctional pages 5-7).

### Modifiers, epigenetics, and chromosomal abnormalities

No validated modifier gene, epigenetic signature, anticipation mechanism, aneuploidy, translocation, or inversion is known. The causal 5.5-kb deletion is a submicroscopic structural variant, not a cytogenetically visible chromosomal abnormality.

## 5. Environmental information

No toxin, radiation exposure, pollutant, lifestyle factor, or infectious organism causes DFNA84. General hearing-health factors—unsafe noise, aminoglycosides, platinum chemotherapy, severe infections, and aging—may add independent cochlear injury, but ATP11A-specific interaction data are absent. The disorder is not infectious, contagious, or immune-mediated.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. A heterozygous terminal **ATP11A** deletion **leads to** aberrant terminal-exon splicing while allowing stable mutant RNA.
2. Aberrant RNA **results in** an altered ATP11A C-terminus and reduced functional phospholipid-flippase activity.
3. Reduced ATP11A activity **leads to** deficient inward translocation of PS, and possibly PE, at the plasma membrane; reduced PS transport is demonstrated in transfected cells (loh2021atp11acausesautosomaldominanta pages 1-7, loh2021atp11acausesautosomaldominant pages 135-139).
4. Deficient lipid transport **results in** impaired membrane-lipid asymmetry. In inner-ear cells, this step is strongly biologically supported but not directly demonstrated in human tissue.
5. Altered membrane asymmetry is **inferred to lead to** one or more branches:  
   **(a)** disturbed synaptic vesicle exocytosis/endocytosis and Ca²⁺ handling at inner-hair-cell ribbon synapses;  
   **(b)** altered membrane stability, stereociliary maintenance, and hair-cell survival;  
   **(c)** externalized PS acting as an “eat-me” signal, promoting inappropriate phagocytic clearance or apoptosis;  
   **(d)** impaired spiral-ganglion neurite maintenance or auditory-nerve synchrony (pater2021autosomaldominantnonsyndromic pages 10-13, loh2021atp11acausesautosomaldominant pages 123-126).
6. Synaptic/neural dysfunction **leads to** abnormal or absent ABR despite initially preserved OAE/cochlear microphonics.
7. Progressive cellular dysfunction or loss **results in** worsening speech discrimination, middle/high-frequency threshold elevation, later OAE loss, and ultimately severe/profound hearing impairment (loh2021atp11acausesautosomaldominanta pages 22-25, loh2021atp11acausesautosomaldominanta pages 25-29).

### Upstream versus downstream evidence

The upstream sequence—structural variant, aberrant splicing, stable mutant protein, preserved membrane localization, and reduced PS transport—is experimentally supported. The exact downstream lesion in humans remains unresolved: the clinical physiology favors a synaptic/neural disorder, whereas zebrafish loss-of-function data demonstrate stereocilia and hair-cell abnormalities. Thus ATP11A deficiency may affect several cochlear compartments or shift from neural/synaptic dysfunction to secondary sensory-cell degeneration with age (loh2021atp11acausesautosomaldominant pages 135-139, hawkeynoble2025thep4phospholipidflippase pages 14-18).

Suggested biological-process terms include phospholipid translocation, establishment of membrane asymmetry, auditory receptor-cell maintenance, synaptic vesicle cycling, calcium-ion homeostasis, apoptotic signaling, neuron-projection maintenance, and sensory perception of sound. Suggested cell terms are **inner hair cell**, **outer hair cell**, **Deiters cell**, **spiral ganglion neuron**, and **auditory sensory neuron**. No DFNA84-specific immune, metabolic, methylomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, or multi-omic disease signature has been established.

## 7. Anatomical structures affected

- **Primary organ/system:** inner ear and auditory system; suggested **UBERON:0001846 inner ear** and **UBERON:0002240 cochlea**.
- **Key tissue:** organ of Corti; suggested **UBERON:0002227** if confirmed in the current release.
- **Likely cells:** cochlear inner and outer hair cells, Deiters supporting cells, spiral-ganglion neurons, and auditory/vestibular ganglion neurons. Mouse expression supports these locations, but does not prove which cell initiates human disease (pater2021autosomaldominantnonsyndromic pages 10-13).
- **Subcellular compartment:** ATP11A–CDC50A complex at the plasma membrane; the disease variant is trafficked to the membrane rather than retained in the endoplasmic reticulum (loh2021atp11acausesautosomaldominanta pages 83-88).
- **Laterality:** predominantly bilateral and symmetric. Some ATP11A/DFNA33 families showed possible asymmetry, demonstrating broader allelic variability (pater2022autosomaldominantnonsyndromic pages 9-11).
- **Secondary organs:** no reproducible renal, neurological, vestibular, visual, or systemic involvement has been established in DFNA84.

## 8. Temporal development

Behavioral hearing can be normal during the first decade, while ABR abnormalities may already be present. Recognized onset is usually insidious and postlingual at 10–20 years. Mild middle/high-frequency loss and speech difficulty progress through adolescence and early adulthood; moderate loss is typical by the third or fourth decade in the defining family, and severe/profound loss may occur from approximately 40–50 years onward. Low frequencies become involved later, producing broader or flat audiometric loss (loh2021atp11acausesautosomaldominanta pages 22-25, loh2021atp11acausesautosomaldominanta pages 25-29).

The condition is chronic and lifelong, without documented spontaneous remission or episodic relapses. There is no validated staging system or annual threshold-shift estimate. Early electrophysiological abnormality and retained sensory-cell function may constitute an intervention window, but this remains unproven.

## 9. Inheritance and population

Inheritance is **autosomal dominant**. A heterozygous affected person has a theoretical **50% chance per pregnancy** of transmitting the variant. Both sexes are affected. The defining family showed vertical transmission across four generations; however, measured penetrance is unavailable. A 99% penetrance parameter used in linkage analysis was a modeling assumption, not an empirical estimate (pater2021autosomaldominantnonsyndromic pages 5-7, loh2021atp11acausesautosomaldominanta pages 22-25).

Disease-specific prevalence, incidence, carrier frequency, sex ratio, de-novo rate, germline-mosaicism rate, and age distribution are unknown. Families have been reported from Germany, Newfoundland/Northern-European ancestry, and Jewish Israeli families with roots in Afghanistan or Bukhara, Uzbekistan, but these observations do not establish ethnic susceptibility. The Newfoundland allele may be locally private; 202 additional local probands did not carry it (pater2022autosomaldominantnonsyndromic pages 9-11, pater2021autosomaldominantnonsyndromic pages 5-7).

There is no evidence of anticipation or a consanguinity effect. Founder effects remain possible but unproven.

## 10. Diagnostics

### Clinical testing

A practical work-up should include:

1. Otoscopy and tympanometry to exclude conductive disease.
2. Pure-tone air- and bone-conduction audiometry, including high frequencies.
3. Age-appropriate speech recognition and speech-in-noise testing.
4. **ABR**, including waveform morphology, synchrony, and threshold.
5. **OAE** and/or **cochlear microphonics** to identify preserved outer-hair-cell function. Preserved responses support auditory neuropathy early, but their absence in advanced disease does not exclude DFNA84 (loh2021atp11acausesautosomaldominanta pages 22-25, loh2021atp11acausesautosomaldominanta pages 25-29).
6. Vestibular and neurological examination when clinically indicated, principally to exclude syndromic auditory neuropathy.

There is no blood biomarker, imaging signature, biopsy finding, or biochemical assay specific for DFNA84. MRI of the internal auditory canals/brain may exclude cochlear-nerve deficiency or acquired lesions, but is not diagnostic.

### Genetic testing

The preferred first-line molecular test is a comprehensive hereditary-hearing-loss panel that includes **ATP11A** and validated exon-level CNV/structural-variant detection. If negative, **WGS** is particularly valuable because the defining deletion and noncanonical terminal-exon/intronic lesions can be missed by routine WES. Segregation testing should follow, and splice-region or terminal-exon variants may require patient RNA, full-length transcript analysis, or a minigene assay (pater2021autosomaldominantnonsyndromic pages 7-10, pater2019amultiomicapproach pages 154-158).

Single-gene ATP11A testing is reasonable when the family shows dominant auditory-neuropathy physiology or a known familial variant. CMA, karyotype, FISH, mitochondrial testing, and repeat-expansion testing are not primary tests unless another diagnosis is suspected. WES can identify coding variants but is less reliable for the structural and transcript-complex lesions already associated with ATP11A.

### Differential diagnosis

Important genetic differentials include **DIAPH3/AUNA1**, **OTOF**, **OPA1**, **ATP1A3**, **ATP1A1**, **PJVK/GSDME**, **PMP22**, **MPZ**, and other auditory-neuropathy genes. Distinguishing features include recessive versus dominant inheritance, congenital versus postlingual onset, optic atrophy, ataxia, peripheral neuropathy, or syndromic manifestations. Conventional cochlear hearing-loss genes should also be considered because OAEs can disappear in advanced DFNA84.

### Screening

Newborn OAE-only screening may be insufficient because auditory-neuropathy disorders can retain OAEs; ABR-based screening is more informative. In known families, cascade genetic testing and baseline ABR/OAE—even in apparently normal-hearing children—are appropriate. Prenatal and preimplantation genetic testing become technically possible after a familial pathogenic variant is established.

## 11. Outcome and prognosis

Life expectancy and mortality appear unaffected because the condition is nonsyndromic; no disease-specific survival statistics exist. The principal morbidity is progressive communication disability. Prognosis is variable but generally entails worsening thresholds and speech recognition over decades. ABR abnormality may precede perceived hearing difficulty and is therefore a plausible early prognostic marker, although no validated prediction model exists (loh2021atp11acausesautosomaldominanta pages 22-25, loh2021atp11acausesautosomaldominanta pages 25-29).

Recovery of lost native hearing has not been reported. Hearing aids may improve audibility but cannot directly restore neural synchrony. Older relatives in the defining family had little benefit; three met cochlear-implant criteria, but none had undergone implantation at the reported assessment, leaving ATP11A-specific implant outcomes unknown (loh2021atp11acausesautosomaldominanta pages 25-29).

## 12. Treatment

### Current clinical management

There is no approved ATP11A-directed pharmacotherapy. Management is individualized and supportive:

- serial audiology, including speech testing, ABR, and OAE where informative;
- hearing conservation and avoidance of unnecessary ototoxic exposure;
- appropriately fitted hearing aids when behavioral thresholds are elevated;
- remote microphones, captioning, visual communication, educational/workplace accommodations, auditory-verbal or speech-language therapy;
- cochlear-implant evaluation for severe functional impairment or inadequate aided speech understanding, after confirming cochlear-nerve integrity.

Suggested NCIT concepts include **Hearing Aid Device**, **Cochlear Implantation**, **Audiologic Rehabilitation**, **Speech Therapy**, and **Genetic Counseling**; exact NCIT codes should be validated against the release used by the knowledge base.

In general auditory neuropathy, cochlear implants may restore more synchronous neural activation when pathology is presynaptic, but outcome varies by genotype and lesion site. This principle cannot yet be converted into an ATP11A-specific response estimate (loh2021atp11acausesautosomaldominanta pages 22-25).

### Experimental approaches

No ATP11A-specific gene replacement, gene editing, ASO, siRNA, cell therapy, or pharmacological trial was identified. Pharmacologically limiting externalized PS or restoring membrane asymmetry has been proposed, but remains speculative and preclinical (pater2021autosomaldominantnonsyndromic pages 10-13). Gene therapy successes in other forms of auditory neuropathy—particularly OTOF deficiency—should not be represented as evidence for ATP11A treatment.

## 13. Prevention

**Primary prevention:** The inherited variant cannot currently be prevented after conception. Reproductive options include genetic counseling, preimplantation genetic testing, prenatal diagnosis, donor gametes, and natural conception with or without testing.

**Secondary prevention:** Cascade testing, early ABR/OAE assessment, regular audiometry, prompt amplification or communication support, and monitoring of speech/language development can reduce avoidable developmental and social consequences.

**Tertiary prevention:** Hearing conservation, avoidance of excessive noise and unnecessary ototoxic medication, optimized assistive devices, rehabilitation, and timely cochlear-implant referral may limit disability. No vaccine, chemoprophylaxis, or disease-specific preventive drug is applicable.

## 14. Other species and natural disease

Relevant orthologs include **Atp11a** in mouse (*Mus musculus*, NCBI Taxonomy **10090**) and zebrafish (*Danio rerio*, Taxonomy **7955**). No naturally occurring ATP11A-associated veterinary hearing disorder, breed predisposition, zoonotic transmission, or cross-species infectious susceptibility was identified.

Conservation is supported by ATP11A expression in vertebrate auditory cells and by experimental zebrafish ear phenotypes. Comparative pathology suggests that membrane-lipid asymmetry is required for sensory-hair-cell and stereocilia maintenance, but the precise human auditory-neuropathy phenotype may require mammalian synaptic and neural physiology not captured by larval fish (hawkeynoble2025thep4phospholipidflippase pages 14-18).

## 15. Model organisms and experimental systems

### Human-cell model

HEK293/HEK293T cells expressing wild-type or mutant human ATP11A with CDC50A demonstrated that the disease protein can reach the plasma membrane but has markedly reduced PS-flippase activity. This is the strongest direct functional evidence, although kidney-derived cells do not reproduce cochlear-cell architecture or auditory synapses (loh2021atp11acausesautosomaldominanta pages 83-88, loh2021atp11acausesautosomaldominant pages 135-139).

### Zebrafish

A 2025 *Journal of Cell Science* study generated CRISPR loss-of-function **atp11a** alleles with 5-bp and 7-bp deletions. At 5 days post-fertilization, mutants showed fewer stereocilia and hair cells in inner-ear maculae/cristae and fewer cells in an otic neuromast. Stereocilia analyses included wild type n=17, heterozygotes n=22, and homozygotes n=7. This supports a conserved ear-maintenance requirement but is not an exact knock-in of the human variant (hawkeynoble2025thep4phospholipidflippase pages 14-18). Publication: May 2025, DOI/URL: https://doi.org/10.1242/jcs.263657.

### Mouse and related models

Mouse expression data place Atp11a in inner and outer hair cells, Deiters cells, otic progenitors, and auditory/vestibular ganglion neurons, with postnatal upregulation. However, a validated mouse carrying the human DFNA84 deletion and reproducing its progressive auditory-neuropathy phenotype was not identified (pater2021autosomaldominantnonsyndromic pages 10-13). Phenotypes of other P4-ATPase models—such as Atp8a2- or Atp8b1-deficient mice—support roles in spiral-ganglion and hair-cell maintenance but are mechanistic analogies, not ATP11A disease models (pater2019amultiomicapproach pages 154-158).

## Recent developments and authoritative interpretation

- **2023:** Chepurwar and colleagues published the ATP11A causal assignment for autosomal-dominant auditory neuropathy type 2 in *Human Molecular Genetics*, volume 32, pages 1083–1089; DOI/URL: https://doi.org/10.1093/hmg/ddac267. The key mechanistic conclusion is captured by the associated thesis abstract: the 5.5-kb deletion causes aberrant splicing without nonsense-mediated decay, and the mutant displays reduced PS-flipping activity while reaching the plasma membrane normally (loh2021atp11acausesautosomaldominanta pages 1-7).
- **2023:** Vona et al. revisited the historical DFNA33 pedigree and identified highly improbable double/triple recombination assignments, cautioning against automatically attributing the original German locus to ATP11A. Publication: August 2023, *Frontiers in Genetics* 14:1214736; DOI/URL: https://doi.org/10.3389/fgene.2023.1214736 (vona2023unravelinghaplotypeerrors pages 2-4).
- **2023–2024:** No new DFNA84 human cohort, penetrance estimate, treatment trial, or disease-specific omics study was found. This absence is scientifically important: proposed downstream pathways remain hypotheses rather than clinically validated therapeutic targets.
- **2025:** The zebrafish knockout study supplied the first strong ATP11A-specific vertebrate evidence for loss of ear hair cells and stereocilia, extending the mechanism from membrane transport assays to tissue maintenance (hawkeynoble2025thep4phospholipidflippase pages 14-18).

## Exact source quotations available from retrieved abstracts/full text

> “The causative mutation is a 5,500 bp deletion covering the last coding exon. This results in aberrant splicing with the use of an alternative last exon, without induction of nonsense-mediated mRNA decay.” (Disease-specific experimental thesis abstract.) (loh2021atp11acausesautosomaldominanta pages 1-7)

> “A flippase activity assay … displays a hypoactivity of PS translocating function from the exoplasmic to the cytoplasmic leaflet of the plasma membrane in the presence of the mutation.” (Disease-specific in-vitro evidence.) (loh2021atp11acausesautosomaldominanta pages 1-7)

> “We report a new DFNA gene, ATP11A, in a Newfoundland family with a variable form of bilateral sensorineural hearing loss.” (Allelic human evidence published as DFNA33, not the defining AUNA2 pedigree.) (pater2022autosomaldominantnonsyndromic pages 9-11)

## Principal evidence limitations

The disorder’s phenotype, penetrance, and prognosis are based chiefly on one multigenerational family. There are no population prevalence data, prospective natural-history cohorts, validated biomarkers, ATP11A-specific cochlear-implant outcomes, or interventional trials. The precise affected human cell type remains unresolved, and claims involving apoptosis, phagocytosis, calcium dysregulation, synaptic-vesicle cycling, or neurite degeneration should be stored as **inferred mechanisms**, not established causal steps. Finally, disease-name harmonization must preserve the distinction between DFNA84/AUNA2 and ATP11A-associated families historically reported as DFNA33.

References

1. (loh2021atp11acausesautosomaldominanta pages 22-25): SM von Loh. Atp11a causes autosomal-dominant progressive, non-syndromic auditory synaptopathy/auditory neuropathy. Unknown journal, 2021.

2. (loh2021atp11acausesautosomaldominanta pages 25-29): SM von Loh. Atp11a causes autosomal-dominant progressive, non-syndromic auditory synaptopathy/auditory neuropathy. Unknown journal, 2021.

3. (pater2022autosomaldominantnonsyndromic pages 9-11): Justin A. Pater, Cindy Penney, Darren D. O’Rielly, Anne Griffin, Lara Kamal, Zippora Brownstein, Barbara Vona, Chana Vinkler, Mordechai Shohat, Ortal Barel, Curtis R. French, Sushma Singh, Salem Werdyani, Taylor Burt, Nelly Abdelfatah, Jim Houston, Lance P. Doucette, Jessica Squires, Fabian Glaser, Nicole M. Roslin, Daniel Vincent, Pascale Marquis, Geoffrey Woodland, Touati Benoukraf, Alexia Hawkey-Noble, Karen B. Avraham, Susan G. Stanton, and Terry-Lynn Young. Autosomal dominant non-syndromic hearing loss maps to dfna33 (13q34) and co-segregates with splice and frameshift variants in atp11a, a phospholipid flippase gene. Human Genetics, 141:431-444, Mar 2022. URL: https://doi.org/10.1007/s00439-022-02444-x, doi:10.1007/s00439-022-02444-x. This article has 27 citations and is from a peer-reviewed journal.

4. (vona2023unravelinghaplotypeerrors pages 2-4): Barbara Vona, Sabrina Regele, Aboulfazl Rad, Nicola Strenzke, Justin A. Pater, Katrin Neumann, Marc Sturm, Tobias B. Haack, and Antoinette G. Am Zehnhoff-Dinnesen. Unraveling haplotype errors in the dfna33 locus. Frontiers in Genetics, Aug 2023. URL: https://doi.org/10.3389/fgene.2023.1214736, doi:10.3389/fgene.2023.1214736. This article has 3 citations and is from a peer-reviewed journal.

5. (loh2021atp11acausesautosomaldominanta pages 1-7): SM von Loh. Atp11a causes autosomal-dominant progressive, non-syndromic auditory synaptopathy/auditory neuropathy. Unknown journal, 2021.

6. (loh2021atp11acausesautosomaldominanta pages 83-88): SM von Loh. Atp11a causes autosomal-dominant progressive, non-syndromic auditory synaptopathy/auditory neuropathy. Unknown journal, 2021.

7. (loh2021atp11acausesautosomaldominant pages 135-139): SM von Loh. Atp11a causes autosomal-dominant progressive, non-syndromic auditory synaptopathy/auditory neuropathy. Unknown journal, 2021.

8. (loh2021atp11acausesautosomaldominanta pages 135-139): SM von Loh. Atp11a causes autosomal-dominant progressive, non-syndromic auditory synaptopathy/auditory neuropathy. Unknown journal, 2021.

9. (loh2021atp11acausesautosomaldominant pages 123-126): SM von Loh. Atp11a causes autosomal-dominant progressive, non-syndromic auditory synaptopathy/auditory neuropathy. Unknown journal, 2021.

10. (pater2021autosomaldominantnonsyndromic pages 1-5): Justin Pater, Cindy Penney, Darren O’Rielly, Anne Griffin, Mordechai Shohat, Ortal Barel, Curtis R French, Sushma Singh, Salem Werdyani, Taylor Burt, Nelly Abdelfatah, Jim Houston, Lance Doucette, Jessica Squires, Nicole Roslin, Daniel Vincent, Pascale Marquis, Geoffrey Woodland, Susan Stanton, and Terry-Lynn Young. Autosomal dominant non-syndromic hearing loss maps to dfna33 (13q34) and co-segregates with splice site variants in atp11a, a phospholipid flippase gene. Unknown journal, May 2021. URL: https://doi.org/10.21203/rs.3.rs-530835/v1, doi:10.21203/rs.3.rs-530835/v1. This article has 0 citations.

11. (pater2021autosomaldominantnonsyndromic pages 5-7): Justin Pater, Cindy Penney, Darren O’Rielly, Anne Griffin, Mordechai Shohat, Ortal Barel, Curtis R French, Sushma Singh, Salem Werdyani, Taylor Burt, Nelly Abdelfatah, Jim Houston, Lance Doucette, Jessica Squires, Nicole Roslin, Daniel Vincent, Pascale Marquis, Geoffrey Woodland, Susan Stanton, and Terry-Lynn Young. Autosomal dominant non-syndromic hearing loss maps to dfna33 (13q34) and co-segregates with splice site variants in atp11a, a phospholipid flippase gene. Unknown journal, May 2021. URL: https://doi.org/10.21203/rs.3.rs-530835/v1, doi:10.21203/rs.3.rs-530835/v1. This article has 0 citations.

12. (hawkeynoble2025thep4phospholipidflippase pages 14-18): Alexia Hawkey-Noble, Cameron Tobin, Muhammad T. Ameen, Liam Osmond, Colby Gill, Christina S. Bottaro, Terry-Lynn Young, and Curtis R. French. The p4-phospholipid flippase atp11a is required for maintenance of eye and ear structure in zebrafish. May 2025. URL: https://doi.org/10.1242/jcs.263657, doi:10.1242/jcs.263657. This article has 0 citations and is from a domain leading peer-reviewed journal.

13. (pater2021autosomaldominantnonsyndromic pages 7-10): Justin Pater, Cindy Penney, Darren O’Rielly, Anne Griffin, Mordechai Shohat, Ortal Barel, Curtis R French, Sushma Singh, Salem Werdyani, Taylor Burt, Nelly Abdelfatah, Jim Houston, Lance Doucette, Jessica Squires, Nicole Roslin, Daniel Vincent, Pascale Marquis, Geoffrey Woodland, Susan Stanton, and Terry-Lynn Young. Autosomal dominant non-syndromic hearing loss maps to dfna33 (13q34) and co-segregates with splice site variants in atp11a, a phospholipid flippase gene. Unknown journal, May 2021. URL: https://doi.org/10.21203/rs.3.rs-530835/v1, doi:10.21203/rs.3.rs-530835/v1. This article has 0 citations.

14. (pater2019amultiomicapproach pages 154-158): J Pater. A multi-omic approach to genetic hearing loss in the newfoundland founder population. Unknown journal, 2019.

15. (pater2021autosomaldominantnonsyndromic pages 10-13): Justin Pater, Cindy Penney, Darren O’Rielly, Anne Griffin, Mordechai Shohat, Ortal Barel, Curtis R French, Sushma Singh, Salem Werdyani, Taylor Burt, Nelly Abdelfatah, Jim Houston, Lance Doucette, Jessica Squires, Nicole Roslin, Daniel Vincent, Pascale Marquis, Geoffrey Woodland, Susan Stanton, and Terry-Lynn Young. Autosomal dominant non-syndromic hearing loss maps to dfna33 (13q34) and co-segregates with splice site variants in atp11a, a phospholipid flippase gene. Unknown journal, May 2021. URL: https://doi.org/10.21203/rs.3.rs-530835/v1, doi:10.21203/rs.3.rs-530835/v1. This article has 0 citations.

16. (rosso2025unravelingthefunctional pages 5-7): Lara Emily Rosso, Giulia Pianigiani, Anna Morgan, Elisa Rubinato, Elisa Paccagnella, Stefania Lenarduzzi, Anita Wischmeijer, Beatrice Spedicati, and Giorgia Girotto. Unraveling the functional impact of splicing variants in inherited hearing disorders through minigene splicing assays. Sep 2025. URL: https://doi.org/10.3390/biomedicines13092245, doi:10.3390/biomedicines13092245. This article has 5 citations.

17. (loh2021atp11acausesautosomaldominanta pages 19-22): SM von Loh. Atp11a causes autosomal-dominant progressive, non-syndromic auditory synaptopathy/auditory neuropathy. Unknown journal, 2021.

18. (loh2021atp11acausesautosomaldominanta pages 29-32): SM von Loh. Atp11a causes autosomal-dominant progressive, non-syndromic auditory synaptopathy/auditory neuropathy. Unknown journal, 2021.

## Artifacts

- [Edison artifact artifact-00](Hearing_Loss_Autosomal_Dominant_84-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 6 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 12 |
| Resolved | 11 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 0 |

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0004012` (GO_0004012) (1 mention) - replaced by `GO:0140326`

11 of 12 terms resolved to a current term; the rest could not be looked up either way.
