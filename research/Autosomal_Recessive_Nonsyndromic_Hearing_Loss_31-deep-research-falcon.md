---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-16T14:50:45.177653'
end_time: '2026-09-16T15:00:10.263108'
duration_seconds: 565.09
template_file: templates/disease_pathophysiology_research.md
template_sha: 1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666
template_variables:
  disease_name: DFNB31 WHRN whirlin-related autosomal recessive nonsyndromic hearing
    loss
  mondo_id: MONDO:0011767
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 27
reference_validation:
  total_references: 9
  verified: 9
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 9
  on_topic: 1
  validator_version: 0.2.1
term_validation:
  total_terms: 1
  verified: 1
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0011767
    reported_labels:
    - if available
    ontology_label: autosomal recessive nonsyndromic hearing loss 31
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Autosomal_Recessive_Nonsyndromic_Hearing_Loss_31-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** DFNB31 WHRN whirlin-related autosomal recessive nonsyndromic hearing loss
- **MONDO ID:** MONDO:0011767 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **DFNB31 WHRN whirlin-related autosomal recessive nonsyndromic hearing loss** covering all of the
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
- **Disease Name:** DFNB31 WHRN whirlin-related autosomal recessive nonsyndromic hearing loss
- **MONDO ID:** MONDO:0011767 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **DFNB31 WHRN whirlin-related autosomal recessive nonsyndromic hearing loss** covering all of the
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


# DFNB31 / WHRN-related autosomal-recessive nonsyndromic hearing loss

## Executive summary

DFNB31 is a rare Mendelian sensorineural hearing-loss disorder caused by **biallelic germline pathogenic variants in WHRN**, which encodes the PDZ-domain scaffold protein whirlin. The disease is usually described as congenital or prelingual, bilateral, severe-to-profound hearing loss without retinal disease. It must be distinguished from **WHRN-related Usher syndrome type 2D (USH2D)**, in which hearing impairment accompanies progressive rod–cone retinal degeneration. Open Targets specifically maps **WHRN (ENSG00000095397)** to autosomal-recessive nonsyndromic hearing loss 31, **MONDO:0011767**. (OpenTargets Search: autosomal recessive nonsyndromic hearing loss-WHRN, mathur2019ushersyndromeand pages 2-3)

The strongest mechanistic model is that loss of stereociliary tip-localized whirlin disrupts the **MYO15A–WHRN–EPS8** protein complex, causing deficient elongation and organization of actin-rich cochlear hair-cell stereocilia and consequently defective mechanotransduction. Mutation location and transcript/isoform disruption influence whether disease remains cochlear or also affects the retina, although this genotype–phenotype rule is not absolute. (mathur2015distinctexpressionand pages 11-12, mathur2015distinctexpressionand pages 1-2, mathur2015distinctexpressionand pages 12-13)

No approved molecular therapy or WHRN-targeted human clinical trial was identified. Hearing aids, cochlear implantation when indicated, communication access, and early habilitation remain standard care. Neonatal AAV8-mediated whirlin supplementation restored stereociliary morphology and improved inner-hair-cell survival in whirler mice but **did not restore ABR hearing sensitivity**; treatment of adults did not restore stereociliary architecture. (chien2016genetherapyrestores pages 9-9, chien2016genetherapyrestores pages 8-9, brotto2024autosomalrecessivenonsyndromic pages 2-3)

The following structured summary is suitable for knowledge-base ingestion.

| Domain | Established finding | Evidence type | Suggested ontology identifiers | Confidence / gap |
|---|---|---|---|---|
| Identity | Autosomal recessive nonsyndromic hearing loss 31 (DFNB31) is a Mendelian sensorineural hearing-loss disorder caused by biallelic **WHRN** variants. (OpenTargets Search: autosomal recessive nonsyndromic hearing loss-WHRN, mathur2015distinctexpressionand pages 2-2) | Aggregated disease–target resources; human genetic studies | **MONDO:0011767**; OMIM phenotype label: DFNB31; MeSH label: Hearing Loss, Sensorineural | High confidence for gene–disease relationship; dedicated ICD-10/ICD-11 codes are unavailable. |
| Core phenotype | Usually bilateral, congenital or prelingual, severe-to-profound sensorineural hearing loss; the canonical DFNB31 description emphasizes profound hearing loss with normal vision. (mathur2019ushersyndromeand pages 2-3) | Human pedigrees and literature synthesis | HPO: Sensorineural hearing impairment; Bilateral sensorineural hearing impairment; Congenital onset; Profound hearing impairment; Absent speech or delayed speech-and-language development | High confidence for hearing loss; exact frequencies and longitudinal progression rates are poorly quantified because reported cohorts are small. |
| Gene and protein | **WHRN** encodes whirlin, a cytoskeletal scaffolding protein with PDZ domains and a proline-rich region; the gene is located on chromosome 9q32–q34. (mathur2015distinctexpressionand pages 2-2, souissi2021novelpathogenicmutations pages 11-12) | Human genetics; molecular studies | HGNC label: WHRN; UniProt label: Whirlin; GO label: protein-containing complex scaffold activity | High confidence; transcript numbering and historical use of *DFNB31* as a gene symbol can complicate variant normalization. |
| Isoforms | Principal products include full-length whirlin with three PDZ domains, C-terminal whirlin containing the proline-rich region and PDZ3, and N-terminal forms containing PDZ1 and/or PDZ2. (mathur2015distinctexpressionand pages 11-12, mathur2015distinctexpressionand pages 2-2, mathur2019ushersyndromeand pages 2-3) | Mouse tissue expression, proteomics and molecular localization | Protein isoform labels: full-length whirlin, N-terminal whirlin, C-terminal whirlin; GO label: alternative mRNA splicing | High confidence in mice; exact expression and functional equivalence of every human transcript remain incompletely resolved. |
| Molecular mechanism | Loss of tip-localized whirlin disrupts the **MYO15A–WHRN–EPS8** elongation complex, leading to abnormally short and disorganized actin-rich stereocilia and impaired hair-cell mechanosensation. (mathur2015distinctexpressionand pages 11-12, mathur2015distinctexpressionand pages 1-2, mathur2015distinctexpressionand pages 12-13) | Biochemical interaction, localization and mouse-mutant evidence | GO: stereocilium organization; actin filament organization; sensory perception of sound; mechanosensory behavior; auditory receptor-cell stereocilium | High mechanistic confidence in model organisms; the complete causal sequence has not been directly observed in living human cochleae. |
| Anatomy and cell types | Primary disease sites are the cochlea and organ of Corti, particularly inner and outer hair-cell stereociliary bundles; whirlin also occurs in vestibular hair cells and, in long-isoform disease, photoreceptor periciliary regions. (mathur2015distinctexpressionand pages 11-12, mathur2015distinctexpressionand pages 12-13, mathur2015astudyof pages 1-2) | Mouse immunolocalization and functional studies | UBERON labels: cochlea, organ of Corti, inner ear, vestibular organ, retina; CL labels: inner hair cell, outer hair cell, vestibular hair cell, retinal photoreceptor cell; GO label: stereocilium | High confidence for cochlear localization; human vestibular involvement in isolated DFNB31 is insufficiently characterized. |
| Inheritance | Biallelic germline pathogenic variants produce autosomal recessive disease; heterozygous parents are generally clinically unaffected under the established human model. | Human segregation studies and Mendelian disease curation | HPO: Autosomal recessive inheritance; GENO label: germline allele | High confidence; penetrance is presumed high for severe biallelic loss-of-function genotypes, but formal penetrance estimates and verified human modifier genes are unavailable. |
| Pathogenic variants | Reported DFNB31-associated C-terminal truncating alleles include **p.Arg778Ter (R778X)** and **p.Gly808AspfsTer11 (G808DfsX11)**; pathogenic WHRN alleles also include other nonsense, frameshift and splice-disrupting variants. (mathur2015distinctexpressionand pages 10-11, mathur2019ushersyndromeand pages 2-3) | Human pedigrees, segregation and model comparison | Sequence Ontology labels: stop gained, frameshift variant, splice-region/splice-donor/splice-acceptor variant; ClinVar classification labels: pathogenic or likely pathogenic when criteria are met | Variant-level confidence must be assessed individually using current ClinVar/ACMG evidence, segregation and population frequency; no single founder allele explains most cases globally. |
| Distinction from USH2D | C-terminal variants that preserve a functional retinal N-terminal product tend to cause isolated DFNB31, whereas N-terminal variants disrupting full-length whirlin in ear and retina tend to cause moderate-to-severe hearing loss plus retinitis pigmentosa (USH2D). This is a useful but nonabsolute isoform-based correlation. (mathur2015distinctexpressionand pages 1-2, mathur2015distinctexpressionand pages 2-2, mathur2015distinctexpressionand pages 10-11, mathur2019ushersyndromeand pages 2-3) | Human genotype–phenotype observations plus allele-specific mouse models | MONDO label: Usher syndrome type 2D; HPO: Retinitis pigmentosa, Rod-cone dystrophy, Visual-field defect | Moderate confidence rather than a deterministic rule; retinal surveillance remains prudent after a WHRN diagnosis, especially for N-terminal or uncertain alleles. |
| Diagnosis | Confirm sensorineural hearing loss with newborn screening followed by diagnostic ABR, otoacoustic emissions and age-appropriate behavioral/pure-tone audiometry; establish etiology using a comprehensive hearing-loss panel including **WHRN**, with CNV analysis and segregation. Exome or genome sequencing is appropriate when panel testing is negative. | Standard genetic-hearing-loss practice; targeted sequencing studies; expert curation | LOINC labels: auditory brainstem response, otoacoustic emissions, pure-tone audiometry; NCIT labels: Genetic Testing, Whole Exome Sequencing, Whole Genome Sequencing | High confidence for the general workflow; no WHRN-specific biochemical biomarker, biopsy, metabolomic or epigenomic diagnostic is validated. |
| Additional evaluation | Ophthalmic history and baseline examination, with fundus imaging/OCT and electroretinography when indicated, help exclude evolving USH2D; vestibular testing is reasonable for imbalance or delayed motor milestones because mouse mutants show vestibular dysfunction. (mathur2015astudyof pages 1-2, terrasa2026ushersyndrometype pages 2-4) | Human syndromic differential diagnosis; mouse vestibular evidence | HPO: Vestibular dysfunction, Abnormal electroretinogram; NCIT labels: Electroretinography, Optical Coherence Tomography, Vestibular Function Test | Retinal evaluation is clinically important; routine vestibular screening specifically for DFNB31 lacks disease-specific outcome data. |
| Current treatment | No approved WHRN-directed pharmacotherapy exists. Management uses hearing aids when residual hearing is aidable, cochlear implantation for severe-to-profound loss with inadequate aided benefit, and early speech-language, auditory-verbal or sign-language intervention. | Standard-of-care extrapolation from congenital genetic sensorineural hearing loss | NCIT labels: Hearing Aid, Cochlear Implantation, Speech Therapy, Auditory Rehabilitation | Strong general clinical support, but no DFNB31-specific controlled response rates or genotype-based implantation thresholds are available. |
| Experimental AAV8 therapy | Neonatal round-window delivery of AAV8 carrying 2,724-bp long **Whrn** cDNA restored whirlin expression, stereociliary length/bundle architecture and inner-hair-cell survival in whirler mice; however, it did **not** improve ABR hearing sensitivity at tested frequencies. Adult treatment did not restore stereociliary length or row number. (chien2016genetherapyrestores pages 9-9, chien2016genetherapyrestores pages 8-9, brotto2024autosomalrecessivenonsyndromic pages 2-3) | Preclinical mouse gene-supplementation experiment | NCIT labels: Gene Therapy, Recombinant Adeno-Associated Viral Vector; NCBI Taxon: *Mus musculus*; GO label: stereocilium organization | Morphological rescue is reproducible evidence of target engagement, but functional efficacy was absent; there is no WHRN-targeted human clinical trial or approved therapy. |
| Epidemiology | Disease-specific prevalence, incidence, carrier frequency, sex ratio and geographic distribution have not been robustly estimated; WHRN appears to account for only a very small fraction of genetically diagnosed recessive hearing loss. | Rare-family reports and heterogeneous sequencing cohorts | Orphan disease label; epidemiology terms without disease-specific numerical identifiers | Major evidence gap: do not substitute prevalence estimates for all congenital hearing loss, all ARNSHL or Usher syndrome as DFNB31-specific statistics. |


*Table: Knowledge-base-ready summary of established WHRN-related DFNB31 findings, ontology mappings, evidence types, and major uncertainties. It separates isolated hearing loss from USH2D and morphological AAV8 rescue from functional hearing recovery.*

## 1. Disease information

### Definition and classification

**DFNB31** denotes autosomal-recessive nonsyndromic hearing loss 31: an inherited cochlear sensorineural hearing impairment caused by pathogenic variation on both WHRN alleles. “Nonsyndromic” means that hearing loss is the defining clinical manifestation; in particular, retinal degeneration is absent during the observed course. Canonical descriptions emphasize profound sensorineural hearing loss with normal vision. (OpenTargets Search: autosomal recessive nonsyndromic hearing loss-WHRN, mathur2019ushersyndromeand pages 2-3)

This entry should be kept distinct from **USH2D**, also caused by biallelic WHRN variants, because USH2D combines moderate-to-severe hearing impairment with progressive retinitis pigmentosa/rod–cone dystrophy. Long-term ophthalmic observation may nevertheless be necessary before confidently calling a young patient nonsyndromic. (mathur2015distinctexpressionand pages 1-2, mathur2015distinctexpressionand pages 2-2, mathur2019ushersyndromeand pages 2-3)

### Identifiers and synonyms

- **MONDO:** MONDO:0011767, autosomal recessive nonsyndromic hearing loss 31.
- **OMIM phenotype:** DFNB31; commonly represented as deafness, autosomal recessive 31. The cited molecular study identifies the WHRN/DFNB31 gene entry as **OMIM 607084** and USH2D as **OMIM 611383**. (mathur2015distinctexpressionand pages 2-2)
- **Gene:** WHRN; historical gene names include **DFNB31** and, in mice, **Whrn/Dfnb31**.
- **Synonyms:** DFNB31; autosomal recessive nonsyndromic deafness 31; nonsyndromic recessive deafness due to WHRN; whirlin-related nonsyndromic hearing loss.
- **ICD-10/ICD-11:** no WHRN- or DFNB31-specific billing code was identified. Use the applicable code for bilateral congenital/hereditary sensorineural hearing loss.
- **MeSH:** Hearing Loss, Sensorineural; Hearing Loss, Hereditary.
- **Data provenance:** this report describes an **aggregated disease entity**, derived from pedigrees, case series, curated gene–disease resources, and model systems—not individual EHR data.

## 2. Etiology, risks, protective factors, and environment

### Primary cause

The necessary initiating cause is generally a **biallelic germline WHRN pathogenic genotype**, usually involving loss-of-function alleles such as nonsense, frameshift, or splice-disrupting variants. C-terminal truncating alleles reported in DFNB31 include **p.Arg778Ter (R778X)** and **p.Gly808AspfsTer11 (G808DfsX11)**. (mathur2015distinctexpressionand pages 10-11, mathur2019ushersyndromeand pages 2-3)

### Genetic risk

- Two carrier parents have, for each pregnancy, the standard autosomal-recessive probabilities: **25% affected, 50% heterozygous carrier, and 25% inheriting neither familial pathogenic allele**.
- Consanguinity increases the probability that both parents carry the same rare allele; several recessive hearing-loss discoveries have arisen through consanguineous families.
- Mutation position and isoform disruption influence expression: premature termination in the N-terminal portion more often disrupts full-length whirlin in ear and retina and produces USH2D, whereas C-terminal termination may preserve a retinal N-terminal product and produce DFNB31. This is a probabilistic—not deterministic—correlation. (mathur2015distinctexpressionand pages 1-2, mathur2015distinctexpressionand pages 2-2, mathur2015distinctexpressionand pages 10-11)
- No validated human modifier gene, protective WHRN allele, anticipation mechanism, or quantified germline-mosaicism rate was identified.

### Environmental and lifestyle factors

No toxin, infection, diet, occupation, smoking exposure, or lifestyle behavior causes Mendelian DFNB31 in the absence of the causal genotype. Noise, aminoglycosides, platinum drugs, and other ototoxic exposures could impose **additional acquired cochlear injury**, but a WHRN-specific gene–environment interaction has not been demonstrated. Avoidance of hazardous noise and unnecessary ototoxic medication is therefore prudent tertiary prevention, not primary prevention of the genetic disorder.

No disease-specific metabolic, immune, inflammatory, infectious, or epigenetic trigger is established. Vaccination, antimicrobial prophylaxis, dietary supplementation, and immune therapy have no DFNB31-specific preventive role.

## 3. Phenotypes

### Core phenotype

| Manifestation | Characteristics | Suggested HPO terms |
|---|---|---|
| Sensorineural hearing impairment | Usually bilateral, congenital/prelingual, severe-to-profound; canonical DFNB31 reports emphasize profound loss | Sensorineural hearing impairment; Bilateral sensorineural hearing impairment; Congenital hearing impairment; Profound hearing impairment |
| Speech/language consequences | Delayed spoken-language acquisition or absent speech when early auditory/communication access is inadequate | Delayed speech and language development; Absent speech |
| Normal retinal function | Expected in canonical isolated DFNB31, but age and allele location affect confidence | Absence of retinitis pigmentosa; normal electroretinogram, where documented |
| Possible vestibular dysfunction | Not adequately quantified in humans; predicted from mouse models, especially where both long and short isoforms are affected | Vestibular dysfunction; Abnormality of balance; Delayed gross motor development |

Human reports are too few and heterogeneous for reliable phenotype percentages. Published synthesis characterizes DFNB31 as profound sensorineural hearing loss with normal vision, whereas USH2D tends toward moderate hearing loss with retinitis pigmentosa. (mathur2019ushersyndromeand pages 2-3)

A WHRN N-terminal frameshift, **p.Pro246HisfsTer13**, illustrates that subjective history may underestimate auditory abnormalities: a reported patient considered hearing normal, but formal testing detected an abnormality. This also cautions against assigning phenotype solely from patient report. (mathur2015distinctexpressionand pages 12-13)

### Quality of life

There are no validated DFNB31-specific EQ-5D, SF-36, PROMIS, or hearing-related quality-of-life datasets. Expected morbidity arises from impaired speech perception, communication, education, social participation, safety awareness, and occupational function. Early access to spoken language and/or sign language is therefore a central outcome rather than an ancillary intervention.

## 4. Genetic and molecular information

### Gene and protein

- **Gene:** WHRN; chromosome **9q32–q34**; Ensembl ENSG00000095397. (OpenTargets Search: autosomal recessive nonsyndromic hearing loss-WHRN, souissi2021novelpathogenicmutations pages 11-12)
- **Protein:** whirlin, a cytoskeletal scaffold rather than an enzyme or ion channel.
- **Architecture:** full-length whirlin contains three PDZ domains and a proline-rich region; C-terminal whirlin retains the proline-rich region and PDZ3, while N-terminal products contain PDZ1, PDZ2, or both. (mathur2015distinctexpressionand pages 2-2, mathur2019ushersyndromeand pages 2-3)
- **Major interactors:** MYO15A and EPS8 at stereociliary tips; USH2A/usherin, ADGRV1/GPR98 and PDZD7 at the ankle-link/base complex. (mathur2015distinctexpressionand pages 11-12, mathur2015distinctexpressionand pages 12-13)

### Variant interpretation

Variants must be normalized against a specified MANE/RefSeq transcript because historical reports use different isoforms and legacy nomenclature. Classification should follow ACMG/AMP hearing-loss specifications and incorporate population frequency, predicted loss of function, segregation, phenotype, transcript relevance, and functional evidence. A variant should not be called pathogenic merely because it is rare or computationally damaging.

The established mechanism is predominantly **loss of function**. Germline origin is expected. Somatic WHRN variation is not relevant to inherited DFNB31. Large deletions or other copy-number changes are plausible and should be detectable by panel/WES/WGS CNV analysis, but recurrent aneuploidies, translocations, inversions, repeat expansions, or mitochondrial lesions are not characteristic.

Population allele frequencies must be retrieved for each exact variant from the current gnomAD release; no single global carrier frequency can be responsibly assigned. The recent c.74dup USH2D allele was absent from gnomAD, but that case concerns syndromic disease and does not establish a DFNB31 founder allele. (terrasa2026ushersyndrometype pages 4-5, terrasa2026ushersyndrometype pages 2-4)

### Epigenetics and profiling

No reproducible disease-specific DNA-methylation, histone, metabolomic, lipidomic, circulating-protein, or immune signature is established. Existing transcript/protein work is primarily tissue localization and isoform analysis in mice. No validated single-cell, spatial-transcriptomic, or multi-omic diagnostic classifier for DFNB31 was identified.

## 5. Environmental information

DFNB31 is not an environmentally acquired or infectious disorder. Environmental history remains relevant to exclude mixed etiologies and prevent additional hearing damage. Clinicians should document perinatal infection, meningitis, neonatal intensive-care exposures, head trauma, noise, and ototoxic drugs, but none substitutes for molecular confirmation of WHRN-related disease.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic pathogenic WHRN variation leads to** absent, truncated, unstable, or mislocalized whirlin isoforms.
2. **Loss of functional tip-localized whirlin leads to** impaired assembly/retention of the MYO15A–WHRN–EPS8 stereociliary elongation complex. (mathur2015distinctexpressionand pages 11-12, mathur2015distinctexpressionand pages 12-13)
3. **Complex disruption leads to** deficient actin-dependent elongation and organization of cochlear hair-cell stereocilia.
4. **Short, dysmorphic stereociliary bundles lead to** abnormal coupling of sound-induced bundle displacement to mechanotransduction; this human step is inferred from conserved hair-cell biology and demonstrated mouse morphology.
5. **Defective hair-cell mechanosensation leads to** bilateral sensorineural hearing loss and, with prolonged dysfunction, hair-cell vulnerability/loss. AAV rescue increased inner-hair-cell survival, supporting this downstream relationship. (chien2016genetherapyrestores pages 9-9, chien2016genetherapyrestores pages 8-9)
6. **Retinal branch:** N-terminal lesions disrupting full-length whirlin **lead to** failure of the USH2/periciliary complex in photoreceptors and progressive retinal degeneration—USH2D rather than isolated DFNB31. (mathur2015distinctexpressionand pages 11-12, mathur2015distinctexpressionand pages 1-2)
7. **Retinal-sparing branch:** C-terminal lesions that preserve a partially functional N-terminal retinal product **can result in** normal retinal function but profound deafness—canonical DFNB31. (mathur2015distinctexpressionand pages 1-2, mathur2015distinctexpressionand pages 10-11)
8. **Vestibular branch:** loss of relevant isoforms in vestibular hair cells **leads to** abnormal vestibular stereociliary growth and severe vestibular deficits in mice; clinically important human vestibular involvement remains inferred and insufficiently measured. (mathur2015astudyof pages 1-2)

### Upstream and downstream biology

The upstream lesion is transcript/protein loss of function. The central cellular process is actin-rich stereocilium development and maintenance, not canonical Wnt, MAPK, mTOR, or PI3K–AKT signaling. Downstream events are impaired mechanotransduction, sensory-cell dysfunction, and possible degeneration. There is no evidence that systemic metabolism, autoimmunity, fibrosis, ischemia, or inflammation is primary.

**Suggested GO biological-process terms:** stereocilium organization; actin filament organization; sensory perception of sound; inner-ear receptor-cell differentiation; detection of mechanical stimulus involved in sensory perception of sound.

**Suggested GO cellular-component terms:** stereocilium; stereocilium tip; hair-cell stereociliary bundle; actin cytoskeleton; protein-containing complex; photoreceptor connecting cilium/periciliary membrane complex for the USH2D branch.

**Suggested Cell Ontology labels:** inner hair cell; outer hair cell; vestibular hair cell; retinal rod photoreceptor cell; retinal cone photoreceptor cell.

## 7. Anatomical structures affected

The principal organ is the **inner ear**, especially the cochlea and organ of Corti. Both inner- and outer-hair-cell stereociliary bundles are implicated. Full-length and C-terminal whirlin localize at inner-hair-cell stereociliary tips, while developing outer-hair-cell tips primarily contain C-terminal whirlin; full-length whirlin also transiently participates at stereociliary bases/ankle links. (mathur2015distinctexpressionand pages 11-12, mathur2015distinctexpressionand pages 12-13)

Vestibular sensory epithelia are a plausible secondary site. Mouse vestibular organs express full-length and C-terminal whirlin; loss produces abnormal stereocilia and electrophysiologic balance deficits. (mathur2015astudyof pages 1-2)

The retina is **not clinically affected in canonical DFNB31**, but photoreceptor periciliary structures are affected in WHRN-related USH2D. This distinction is central to diagnosis rather than evidence that every WHRN genotype is syndromic. (mathur2015distinctexpressionand pages 11-12, mathur2015distinctexpressionand pages 1-2)

Suggested anatomy labels include UBERON: inner ear, cochlea, organ of Corti, vestibular organ, retina, and photoreceptor layer. Hearing loss is expected to be **bilateral**; consistent unilateral WHRN disease would warrant investigation for another or additional cause.

## 8. Temporal development

Onset is usually congenital or prelingual and the disease is lifelong. Reliable DFNB31-specific longitudinal progression rates and formal clinical stages are unavailable. Unlike inflammatory or relapsing disorders, it is not episodic and spontaneous remission is not expected.

The most important intervention period is infancy and early childhood, when auditory access and language exposure shape neurodevelopment. Preclinical WHRN data also indicate a narrow biological window: neonatal treatment restored morphology, whereas adult AAV8-whirlin treatment did not recover stereociliary length or row number. (chien2016genetherapyrestores pages 9-9, chien2016genetherapyrestores pages 8-9)

## 9. Inheritance and population

Inheritance is autosomal recessive, with affected males and females expected in equal proportions. Penetrance appears high for clearly deleterious biallelic alleles causing profound congenital loss, but no robust numerical penetrance estimate exists. Expressivity can vary with allele position and isoform disruption. Anticipation is not expected.

No defensible DFNB31-specific prevalence, incidence, sex ratio, global carrier frequency, or number of living affected individuals is available. WHRN diagnoses have been reported across multiple ancestries, including families from South Asia, Türkiye, North Africa, and Europe, but these reports do not establish population prevalence. Consanguinity facilitates homozygosity for rare alleles. Disease-specific founder effects should be asserted only for a documented variant and population.

Statistics for all congenital hearing loss, autosomal-recessive nonsyndromic hearing loss, or Usher syndrome must not be relabeled as DFNB31 statistics. This is a major evidence gap.

## 10. Diagnostics

### Clinical evaluation

1. **Confirm hearing phenotype:** newborn otoacoustic-emission and/or automated ABR screening followed by diagnostic frequency-specific ABR; tympanometry; otoacoustic emissions; age-appropriate behavioral audiometry; later pure-tone and speech audiometry.
2. **Establish type:** air- and bone-conduction testing should demonstrate sensorineural rather than conductive loss.
3. **Assess functional needs:** aided speech perception, auditory development, communication milestones, and hearing-aid benefit.
4. **Evaluate syndromic mimics:** ophthalmic history/examination and, depending on genotype, age, or symptoms, OCT, fundus autofluorescence and electroretinography. Vestibular testing is appropriate for imbalance, delayed walking, oscillopsia, or abnormal motor development. The recent USH2D case demonstrates the utility of OCT, ERG and EOG for retinal characterization. (terrasa2026ushersyndrometype pages 4-5, terrasa2026ushersyndrometype pages 2-4)
5. **Imaging:** temporal-bone CT or MRI may be used for cochlear-implant planning or suspected anatomic/nerve abnormality, but no WHRN-specific radiologic lesion is expected.
6. **Biopsy/laboratory biomarkers:** no blood chemistry, enzyme assay, histopathology, liquid biopsy, or validated molecular biomarker diagnoses DFNB31.

### Genetic testing strategy

A comprehensive hearing-loss NGS panel that includes **WHRN and syndromic hearing-loss genes**, with exon-level deletion/duplication analysis, is generally the most efficient first molecular test. Test parental samples for phase and segregation. WES or WGS is appropriate when panel testing is negative, when structural/noncoding variation is suspected, or when phenotype is atypical. Targeted Sanger sequencing is useful for confirming and cascading a known familial variant, not for comprehensively screening this heterogeneous condition.

CMA, karyotyping and FISH are low-yield unless developmental anomalies suggest a chromosomal disorder. Mitochondrial sequencing and repeat-expansion assays are not WHRN tests but may be used in a broader differential.

### Differential diagnosis

The principal molecular differential includes numerous causes of congenital AR nonsyndromic hearing loss, particularly **GJB2, STRC, OTOF, MYO15A, EPS8, TMC1, TMIE, LOXHD1, CDH23, PCDH15, MYO7A, USH1C, USH1G, USH2A, ADGRV1, and PDZD7**. The critical phenotypic differential is evolving Usher syndrome. Congenital CMV, anatomic inner-ear abnormalities, auditory neuropathy, meningitis, and ototoxic injury should be considered based on history and testing.

### Screening

Universal newborn hearing screening can detect congenital profound DFNB31 but cannot specify the gene. Once familial variants are known, cascade carrier testing, prenatal diagnosis, and preimplantation genetic testing are technically feasible after nondirective counseling.

## 11. Outcome and prognosis

DFNB31 does not appear to shorten life expectancy, and no disease-specific mortality is known. Morbidity is predominantly communication and hearing-related. Hearing does not spontaneously recover because mammalian cochlear sensory hair cells and their specialized stereociliary architecture do not naturally regenerate sufficiently.

Prognosis for language and participation depends more on age at detection, communication access, intervention, aided hearing, educational support, and cochlear-implant candidacy than on a validated WHRN biomarker. Normal retinal surveillance substantially improves confidence that prognosis is nonsyndromic; development of rod–cone dysfunction changes the diagnosis and counseling to USH2D.

No DFNB31-specific cochlear-implant response rate, survival curve, validated prognostic model, or quality-of-life effect size was found.

## 12. Treatment

### Current care

There is no approved WHRN-directed drug, pharmacogenomic recommendation, cell therapy, RNA therapy, or genome-editing treatment.

- **Hearing aids:** appropriate when residual hearing and aided speech access are adequate. Suggested NCIT label: Hearing Aid.
- **Cochlear implantation:** evaluate severe-to-profound bilateral loss with inadequate hearing-aid benefit. Suggested NCIT labels: Cochlear Implant; Cochlear Implantation.
- **Communication and rehabilitation:** early speech-language therapy, auditory habilitation, educational accommodations, family-centered communication planning, and access to sign language according to family/patient goals. Suggested NCIT labels: Speech Therapy; Rehabilitation Therapy.
- **Vestibular rehabilitation:** consider when objective or symptomatic balance dysfunction is present.

### Experimental gene therapy

Chien and colleagues injected approximately **1 × 10^13 genome copies/mL AAV8** carrying the **2,724-bp long Whrn cDNA** under a CMV promoter through the round window of whirler mice at postnatal days **P1–P5**. Animals were assessed through P90, including ABRs at 4, 8, 16 and 32 kHz. Whirlin expression, normal stereociliary length/bundle architecture, and inner-hair-cell survival improved. (chien2016genetherapyrestores pages 8-9)

The abstract’s key claim was that “normal stereocilia length and bundle architecture were restored” and that therapy “increased inner hair cell survival.” Nevertheless, the subsequent evidence synthesis found **no improvement in hearing sensitivity at any tested ABR frequency**. Infection predominantly involved inner hair cells, likely limiting whole-cochlea rescue. Adult administration did not recover stereociliary length or row number. Thus this is target-engagement and morphological proof of concept, not functional cure. (chien2016genetherapyrestores pages 9-9, brotto2024autosomalrecessivenonsyndromic pages 2-3)

The 2024 review of AR nonsyndromic-deafness AAV programs identified 17 preclinical and three clinical studies overall, but excluded WHRN from functionally successful programs because hearing was not restored. No WHRN/DFNB31-specific NCT study was identified in the ClinicalTrials.gov search. (brotto2024autosomalrecessivenonsyndromic pages 2-3)

## 13. Prevention

The mutation cannot be prevented by lifestyle change.

- **Primary/reproductive prevention:** genetic counseling, partner testing where appropriate, cascade testing, prenatal diagnosis, or PGT-M after familial variants are established.
- **Secondary prevention:** universal newborn hearing screening, rapid diagnostic audiology, molecular diagnosis, and early communication intervention.
- **Tertiary prevention:** protect residual hearing from hazardous noise and avoid unnecessary ototoxic exposure; optimize hearing devices, education and rehabilitation; monitor vision when genotype or symptoms could indicate USH2D.
- Vaccination and antimicrobial prophylaxis have no WHRN-specific role, although routine vaccination can prevent some acquired causes of hearing loss.

## 14. Other species and natural disease

**Mus musculus** (NCBI Taxon 10090) has the ortholog **Whrn** and provides the principal comparative system. The naturally occurring **whirler (Whrnwi/wi)** mutant has profound deafness, short/dysmorphic stereocilia and overt vestibular behavior. Engineered **Dfnb31neo/neo** mice retain C-terminal whirlin, show hearing loss and later retinal degeneration, whereas wi/wi animals retain a truncated N-terminal retinal product and do not show comparable retinal degeneration. These allele-specific phenotypes closely model the DFNB31–USH2D isoform distinction. (mathur2015distinctexpressionand pages 1-2, mathur2015distinctexpressionand pages 2-2, mathur2015astudyof pages 1-2)

In vestibular studies, wi/wi mice displayed circling, head bobbing, severe-to-profound vestibular sensory-evoked-potential deficits, and greater balance impairment than neo/neo mice; neo/neo animals lacked an obvious balance phenotype despite objective deficits. (mathur2015astudyof pages 1-2)

No established naturally occurring veterinary syndrome in a named domestic breed, VBO breed mapping, or zoonotic transmission was identified. DFNB31 is genetic and noncommunicable.

## 15. Model organisms and experimental systems

### Available models

- **Whrnwi/wi whirler mouse:** naturally occurring recessive mutant; strong deafness and vestibular phenotype; useful for stereocilia biology and cochlear delivery studies.
- **Dfnb31neo/neo mouse:** engineered allele preferentially affecting long/full-length products; models combined auditory/retinal disease and retained C-terminal whirlin.
- Additional transcript-specific engineered mice have been used to resolve N-, C-, and full-length isoform functions.
- Hair-cell explants, immunolocalization, confocal microscopy and scanning electron microscopy serve as ex vivo/cellular systems.

### Strengths and limitations

Mouse models reproduce stereociliary shortening, hair-bundle disorganization, hearing dysfunction, vestibular abnormalities, and allele-dependent retinal involvement. They enable direct structural study that is impossible in living human cochleae. Limitations include species-specific cochlear maturation, vector tropism, delivery scale, and imperfect correspondence between mouse alleles and every human transcript. Most importantly, restored morphology did not translate into restored ABR thresholds in the AAV8 experiment. (chien2016genetherapyrestores pages 9-9, chien2016genetherapyrestores pages 8-9, brotto2024autosomalrecessivenonsyndromic pages 2-3)

## Recent developments and expert assessment

The most directly relevant 2023 report identified a novel pathogenic WHRN variant in a Moroccan family, extending the allelic spectrum, although accessible evidence did not provide sufficiently detailed variant-level findings to reproduce here safely. Recent 2024 reviews emphasize rapid progress in AAV treatment of recessive hearing loss generally, while classifying WHRN supplementation as morphologically promising but functionally unsuccessful to date. This distinction is essential: the WHRN program has not yet met the translational benchmark of hearing restoration. (brotto2024autosomalrecessivenonsyndromic pages 2-3)

The present expert interpretation is therefore:

1. **Gene–disease validity is strong:** biallelic WHRN loss is established for DFNB31. (OpenTargets Search: autosomal recessive nonsyndromic hearing loss-WHRN)
2. **Mechanistic validity is strong in models:** whirlin is a stereociliary scaffold required for normal bundle elongation and organization. (mathur2015distinctexpressionand pages 11-12, mathur2015distinctexpressionand pages 1-2)
3. **Genotype–phenotype prediction is useful but imperfect:** C-terminal retinal-sparing versus N-terminal USH2D is a guiding framework, not a substitute for longitudinal retinal assessment. (mathur2015distinctexpressionand pages 2-2, mathur2015distinctexpressionand pages 10-11, mathur2019ushersyndromeand pages 2-3)
4. **Clinical evidence remains sparse:** disease-specific prevalence, penetrance, natural history, treatment-response rates and quality-of-life statistics are unavailable.
5. **Therapeutic readiness is preclinical:** improved vector tropism, broader outer-hair-cell delivery, correct isoform selection, and very early administration may be required before WHRN therapy can restore hearing.

## Key publications and URLs

- Mburu et al. **“Defects in whirlin…cause deafness in the whirler mouse and families with DFNB31.”** *Nature Genetics* 34:421–428, August 2003. DOI: https://doi.org/10.1038/ng1208. Foundational human/mouse gene-discovery study; indexed among the supporting WHRN literature. (OpenTargets Search: autosomal recessive nonsyndromic hearing loss-WHRN, souissi2021novelpathogenicmutations pages 11-12)
- Mathur et al. **“Distinct expression and function of whirlin isoforms…”** *Human Molecular Genetics* 24:6213–6228, published online 24 August 2015. DOI: https://doi.org/10.1093/hmg/ddv339. (mathur2015distinctexpressionand pages 11-12, mathur2015distinctexpressionand pages 1-2)
- Mathur et al. **“A study of whirlin isoforms in the mouse vestibular system…”** *Human Molecular Genetics* 24:7017–7030, advance publication 29 September 2015. DOI: https://doi.org/10.1093/hmg/ddv403. (mathur2015astudyof pages 1-2)
- Chien et al. **“Gene Therapy Restores Hair Cell Stereocilia Morphology…”** *Molecular Therapy* 24:17–25, January 2016. DOI: https://doi.org/10.1038/mt.2015.150. (chien2016genetherapyrestores pages 9-9, chien2016genetherapyrestores pages 8-9)
- Mathur & Yang. **“Usher syndrome and non-syndromic deafness: Functions of different whirlin isoforms…”** *Hearing Research* 375:14–24, April 2019. DOI: https://doi.org/10.1016/j.heares.2019.02.007. (mathur2019ushersyndromeand pages 2-3)
- AitRaise et al. **“Novel pathogenic WHRN variant causing hearing loss in a Moroccan family.”** *Molecular Biology Reports* 50:10663–10669, November 2023. DOI: https://doi.org/10.1007/s11033-023-08901-8.
- Brotto et al. **“Autosomal Recessive Non-Syndromic Deafness: Is AAV Gene Therapy a Real Chance?”** *Audiology Research* 14:239–253, February 2024. DOI: https://doi.org/10.3390/audiolres14020022. (brotto2024autosomalrecessivenonsyndromic pages 2-3)

**Evidence caveat:** PMID values were not consistently exposed in the retrieved full texts, so DOI URLs are given rather than guessing identifiers. Direct quotations were limited to text verifiably present in retrieved abstracts. Assertions lacking DFNB31-specific data have been explicitly labeled unavailable, inferred from models, or extrapolated from standard congenital sensorineural-hearing-loss practice.

References

1. (OpenTargets Search: autosomal recessive nonsyndromic hearing loss-WHRN): Open Targets Query (autosomal recessive nonsyndromic hearing loss-WHRN, 13 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (mathur2019ushersyndromeand pages 2-3): Pranav Dinesh Mathur and Jun Yang. Usher syndrome and non-syndromic deafness: functions of different whirlin isoforms in the cochlea, vestibular organs, and retina. Hearing Research, 375:14-24, Apr 2019. URL: https://doi.org/10.1016/j.heares.2019.02.007, doi:10.1016/j.heares.2019.02.007. This article has 75 citations and is from a domain leading peer-reviewed journal.

3. (mathur2015distinctexpressionand pages 11-12): Pranav Dinesh Mathur, Junhuang Zou, Tihua Zheng, Ali Almishaal, Yong Wang, Qian Chen, Le Wang, Deepti Vashist, Steve Brown, Albert Park, and Jun Yang. Distinct expression and function of whirlin isoforms in the inner ear and retina: an insight into pathogenesis of ush2d and dfnb31. Human molecular genetics, 24 21:6213-28, Aug 2015. URL: https://doi.org/10.1093/hmg/ddv339, doi:10.1093/hmg/ddv339. This article has 43 citations and is from a domain leading peer-reviewed journal.

4. (mathur2015distinctexpressionand pages 1-2): Pranav Dinesh Mathur, Junhuang Zou, Tihua Zheng, Ali Almishaal, Yong Wang, Qian Chen, Le Wang, Deepti Vashist, Steve Brown, Albert Park, and Jun Yang. Distinct expression and function of whirlin isoforms in the inner ear and retina: an insight into pathogenesis of ush2d and dfnb31. Human molecular genetics, 24 21:6213-28, Aug 2015. URL: https://doi.org/10.1093/hmg/ddv339, doi:10.1093/hmg/ddv339. This article has 43 citations and is from a domain leading peer-reviewed journal.

5. (mathur2015distinctexpressionand pages 12-13): Pranav Dinesh Mathur, Junhuang Zou, Tihua Zheng, Ali Almishaal, Yong Wang, Qian Chen, Le Wang, Deepti Vashist, Steve Brown, Albert Park, and Jun Yang. Distinct expression and function of whirlin isoforms in the inner ear and retina: an insight into pathogenesis of ush2d and dfnb31. Human molecular genetics, 24 21:6213-28, Aug 2015. URL: https://doi.org/10.1093/hmg/ddv339, doi:10.1093/hmg/ddv339. This article has 43 citations and is from a domain leading peer-reviewed journal.

6. (chien2016genetherapyrestores pages 9-9): Wade W Chien, Kevin Isgrig, Soumen Roy, Inna A Belyantseva, Meghan C Drummond, Lindsey A May, Tracy S Fitzgerald, Thomas B Friedman, and Lisa L Cunningham. Gene therapy restores hair cell stereocilia morphology in inner ears of deaf whirler mice. Molecular therapy : the journal of the American Society of Gene Therapy, 24 1:17-25, Jan 2016. URL: https://doi.org/10.1038/mt.2015.150, doi:10.1038/mt.2015.150. This article has 120 citations.

7. (chien2016genetherapyrestores pages 8-9): Wade W Chien, Kevin Isgrig, Soumen Roy, Inna A Belyantseva, Meghan C Drummond, Lindsey A May, Tracy S Fitzgerald, Thomas B Friedman, and Lisa L Cunningham. Gene therapy restores hair cell stereocilia morphology in inner ears of deaf whirler mice. Molecular therapy : the journal of the American Society of Gene Therapy, 24 1:17-25, Jan 2016. URL: https://doi.org/10.1038/mt.2015.150, doi:10.1038/mt.2015.150. This article has 120 citations.

8. (brotto2024autosomalrecessivenonsyndromic pages 2-3): Davide Brotto, Marco Greggio, Cosimo De Filippis, and Patrizia Trevisi. Autosomal recessive non-syndromic deafness: is aav gene therapy a real chance? Audiology Research, 14:239-253, Feb 2024. URL: https://doi.org/10.3390/audiolres14020022, doi:10.3390/audiolres14020022. This article has 8 citations.

9. (mathur2015distinctexpressionand pages 2-2): Pranav Dinesh Mathur, Junhuang Zou, Tihua Zheng, Ali Almishaal, Yong Wang, Qian Chen, Le Wang, Deepti Vashist, Steve Brown, Albert Park, and Jun Yang. Distinct expression and function of whirlin isoforms in the inner ear and retina: an insight into pathogenesis of ush2d and dfnb31. Human molecular genetics, 24 21:6213-28, Aug 2015. URL: https://doi.org/10.1093/hmg/ddv339, doi:10.1093/hmg/ddv339. This article has 43 citations and is from a domain leading peer-reviewed journal.

10. (souissi2021novelpathogenicmutations pages 11-12): Amal Souissi, Mariem Ben Said, Ikhlas Ben Ayed, Ines Elloumi, Amal Bouzid, Mohamed Ali Mosrati, Mehdi Hasnaoui, Malek Belcadhi, Nabil Idriss, Hassen Kamoun, Nourhene Gharbi, Abdullah A. Gibriel, Abdelaziz Tlili, and Saber Masmoudi. Novel pathogenic mutations and further evidence for clinical relevance of genes and variants causing hearing impairment in tunisian population. Jul 2021. URL: https://doi.org/10.1016/j.jare.2021.01.005, doi:10.1016/j.jare.2021.01.005. This article has 27 citations and is from a peer-reviewed journal.

11. (mathur2015astudyof pages 1-2): Pranav Dinesh Mathur, Sarath Vijayakumar, Deepti Vashist, Sherri M. Jones, Timothy A. Jones, and Jun Yang. A study of whirlin isoforms in the mouse vestibular system suggests potential vestibular dysfunction in dfnb31-deficient patients. Human molecular genetics, 24 24:7017-30, Dec 2015. URL: https://doi.org/10.1093/hmg/ddv403, doi:10.1093/hmg/ddv403. This article has 21 citations and is from a domain leading peer-reviewed journal.

12. (mathur2015distinctexpressionand pages 10-11): Pranav Dinesh Mathur, Junhuang Zou, Tihua Zheng, Ali Almishaal, Yong Wang, Qian Chen, Le Wang, Deepti Vashist, Steve Brown, Albert Park, and Jun Yang. Distinct expression and function of whirlin isoforms in the inner ear and retina: an insight into pathogenesis of ush2d and dfnb31. Human molecular genetics, 24 21:6213-28, Aug 2015. URL: https://doi.org/10.1093/hmg/ddv339, doi:10.1093/hmg/ddv339. This article has 43 citations and is from a domain leading peer-reviewed journal.

13. (terrasa2026ushersyndrometype pages 2-4): Emilio A Cepeda Terrasa, Adriana Ramirez, and Natalio Izquierdo. Usher syndrome type 2d associated with a novel homozygous whrn c.74dup variant: a case report. Jun 2026. URL: https://doi.org/10.7759/cureus.110478, doi:10.7759/cureus.110478. This article has 0 citations.

14. (terrasa2026ushersyndrometype pages 4-5): Emilio A Cepeda Terrasa, Adriana Ramirez, and Natalio Izquierdo. Usher syndrome type 2d associated with a novel homozygous whrn c.74dup variant: a case report. Jun 2026. URL: https://doi.org/10.7759/cureus.110478, doi:10.7759/cureus.110478. This article has 0 citations.

## Artifacts

- [Edison artifact artifact-00](Autosomal_Recessive_Nonsyndromic_Hearing_Loss_31-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 9 |
| On topic | 1 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 1 |
| Resolved | 1 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0011767` (4 mentions) - the report calls it "if available"; MONDO calls it **autosomal recessive nonsyndromic hearing loss 31**
