---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-01T18:14:41.950589'
end_time: '2026-09-01T18:25:59.312481'
duration_seconds: 677.36
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Autosomal dominant nonsyndromic hearing loss 50 (DFNA50), caused by
    MIR96 seed-region point mutations
  mondo_id: MONDO:0013114
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 49
reference_validation:
  total_references: 15
  verified: 15
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 15
  on_topic: 8
  validator_version: 0.2.1
term_validation:
  total_terms: 27
  verified: 26
  not_found: 1
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.037
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0013114
    reported_labels:
    - if available
    ontology_label: autosomal dominant nonsyndromic hearing loss 50
  unresolved_terms:
  - HP:0000404
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Autosomal_Dominant_Nonsyndromic_Hearing_Loss_50-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autosomal dominant nonsyndromic hearing loss 50 (DFNA50), caused by MIR96 seed-region point mutations
- **MONDO ID:** MONDO:0013114 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal dominant nonsyndromic hearing loss 50 (DFNA50), caused by MIR96 seed-region point mutations** covering all of the
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
- **Disease Name:** Autosomal dominant nonsyndromic hearing loss 50 (DFNA50), caused by MIR96 seed-region point mutations
- **MONDO ID:** MONDO:0013114 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal dominant nonsyndromic hearing loss 50 (DFNA50), caused by MIR96 seed-region point mutations** covering all of the
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


# DFNA50 due to **MIR96** mutation: disease-characteristics research report

## Executive summary

Autosomal dominant nonsyndromic hearing loss 50 (DFNA50) is an ultra-rare, usually postlingual and progressive cochlear sensorineural hearing loss caused by heterozygous pathogenic variants in **MIR96**, a non-protein-coding microRNA gene at 7q32. The defining human alleles are seed-region substitutions historically designated **+13G>A** and **+14C>A**; a third established allele, **NR_029512.1:c.57T>C**, lies outside mature miR-96 and disrupts precursor processing. Seed mutations change both loss of normal target repression and gain of novel targets, explaining why their dominant phenotype can be more severe than heterozygous deletion. Evidence comes from a few pedigrees, cultured-cell assays, and several mouse models rather than population cohorts or EHR-scale studies. Open Targets links MIR96 (ENSG00000199158) to autosomal dominant nonsyndromic hearing loss using five evidence records, including PMIDs **19363479**, **19363478**, **20301607**, and **24148127**. (OpenTargets Search: autosomal dominant nonsyndromic hearing loss 50-MIR96)

The most important recent developments are: (1) 2024 hair-cell-specific transcriptomics identifying **215 upregulated and 428 downregulated genes** in homozygous diminuendo hair cells; (2) human-variant knock-in mice demonstrating mutation-specific stereociliary versus synaptic pathology and **328 versus 693 differentially expressed genes**; (3) temporary pharmacologic delay of high-frequency loss with amitriptyline in mice; and (4) long-term auditory preservation/improvement after adult cochlear AAV–SaCas9-KKH editing of the **14C>A** allele. These remain preclinical; no approved disease-modifying therapy or DFNA50-specific clinical trial was identified. (zhu2024targetedgenomeediting pages 1-3, lewis2024pathologicalmechanismsand pages 17-18, lewis2024pathologicalmechanismsand pages 13-16, gwilliam2024acelltype–specific pages 1-2)

| Evidence domain | Source type | Key finding with exact quantitative detail | Interpretation / limitation | Citation context ID or DOI/PMID |
|---|---|---|---|---|
| Human genetics: original DFNA50 families | Human familial linkage/variant study | Two Spanish families with autosomal dominant progressive nonsyndromic hearing loss carried MIR96 seed-region variants **+13G>A** and **+14C>A**; both affect conserved seed nucleotides and were not found in **462 hearing controls**. The **+13G>A** family had affected frequencies across the audiogram, whereas **+14C>A** caused more severe **high-frequency** loss. Mutant miRNA levels were reported as about **20% of wild type**. | Foundational evidence for DFNA50 due to MIR96 seed mutations; quantitative clinical details in available excerpts are limited, and PMIDs were not provided in the retrieved context. | (friedman2009micrornasandepigenetic pages 8-9, lenz2011hereditaryhearingloss pages 5-6) |
| Human genetics: Italian family, precursor variant discovery | Human case-control + family segregation + in vitro functional assay | Screening of **882 NSHL patients** and **836/839 normal-hearing Italian controls** identified **MIR96 c.57T>C** (reported as miR-96(+57T>C); NR_029512.1:c.57T>C; NT_007933.15:g.67447397A>G) in one autosomal dominant family. Reported onset was about **25–40 years** with slow progression; the proband progressed from mild hearing loss at ~25 years to severe at **45** and profound in the **sixth decade**. Variant was present in **3 normal-hearing children**, supporting age-dependent/incomplete penetrance. | First non-seed MIR96 DFNA50 allele; phenotype appears milder/later than seed mutations. Control denominator appears as 836 in abstract text and 839 in results text of available excerpts. | (solda2012anovelmutation pages 5-7, robusto2014inheritedhearingloss pages 91-92, solda2012anovelmutation pages 1-2, solda2012anovelmutation pages 2-4) |
| In vitro mechanism: precursor-processing defect | In vitro transient-expression / qRT-PCR | For the Italian **+57T>C** precursor variant, mature **miR-96** was reduced by **85%** (**P=0.0006**) and **miR-96\*** by **77%** (**P=0.019**), while precursor levels were unaffected; compensatory mutation restored expression. | Supports a **quantitative** pathogenic mechanism through altered hairpin structure and impaired Dicer processing, rather than altered seed specificity. | (solda2012anovelmutation pages 2-4) |
| Mouse model: Dmdo discovery and phenotype | Animal model (ENU mutant mouse) | The **diminuendo (Dmdo)** mouse carries an **A>T** substitution in the Mir96 seed region. Heterozygotes lost the Preyer reflex between **4–6 weeks**, and compound action potential/ABR-type thresholds were raised by about **60 dB** at **4 weeks**; homozygotes had **no cochlear responses**. Microarray showed **96 transcripts** significantly altered, with downregulation of **Slc26a5, oncomodulin/Ocm, Gfi1, Ptprq, Pitpnm1**. | Strong mechanistic model for progressive DFNA50-like hearing loss; background is mouse, not human, and transcriptomics were whole-organ rather than cell-specific. | (lewis2009anenuinducedmutation pages 1-2) DOI:10.1038/ng.369 |
| Hair-cell-specific transcriptomics | Animal model (newborn Mir96Dmdo hair-cell RNA-seq) | First HC-specific RNA-seq dataset from newborn Mir96Dmdo mice identified **215 upregulated** and **428 downregulated** genes in homozygous mutant hair cells versus wild type; highlighted downregulated deafness/development genes included **Myo15a, Myo7a, Ush1c, Gfi1, Ptprq**. | Refines cell-autonomous consequences in hair cells; newborn time point may not capture later degenerative stages. | (gwilliam2024acelltype–specific pages 1-2) DOI:10.3389/fauot.2024.1400576 |
| Human-mutation knock-in transcriptomics | Animal model (2024 humanized Mir96 knock-in mice) | In 2024 knock-in mice carrying human MIR96 variants, homozygous **Mir96+13G>A** had **328 DEGs** and homozygous **Mir96+14C>A** had **693 DEGs** by RNA-seq. Table summary reports heterozygous **Mir96+14C>A** with progressive hearing loss, while **Mir96+13G>A** heterozygotes had normal hearing in mice. | Demonstrates mutation-specific biology and supports gain-of-novel-target effects; mismatch between human and mouse heterozygous +13G>A phenotype is a limitation. | (lewis2024pathologicalmechanismsand pages 17-18, lewis2024pathologicalmechanismsand pages 16-17) DOI:10.1186/s13073-024-01394-5 |
| Pharmacologic proof-of-concept | Animal model therapeutic experiment | Transcriptome-based drug repurposing selected **amitriptyline**. Mir96+14C>A mice received **200 µg/mL** or **400 µg/mL** in drinking water; hearing loss in heterozygotes was **significantly delayed at 24–36 kHz**, most visibly at **30 kHz at 4 weeks**, but **400 µg/mL** did not improve over **200 µg/mL** and homozygotes did not improve. | Proof of concept for pharmacologic delay of progression; effect was **temporary** and mouse doses were higher than standard human dosing, limiting translational use. | (lewis2024pathologicalmechanismsand pages 17-18, lewis2024pathologicalmechanismsand pages 13-16) DOI:10.1186/s13073-024-01394-5 |
| Adult genome editing | Animal model gene-editing therapy | 2024 study developed **AAV-delivered SaCas9-KKH** with sgRNA against **Mir96 14C>A** and treated presymptomatic **3-week-old** and symptomatic **6-week-old** adult heterozygous mice. Hearing improved **long term**, with better efficacy at the younger age; authors also reported transient Cas9 expression and **no evidence of AAV genomic integration**. A dual-AAV “master” system targeted **all known human MIR96 mutations**. | Highly relevant preclinical therapy for dominant MIR96 disease; available excerpts did not provide exact editing percentages or ABR/DPOAE delta values. | (zhu2024targetedgenomeediting pages 1-3, zhu2024targetedgenomeediting pages 12-14) DOI:10.1126/scitranslmed.adn0689 |


*Table: This table summarizes the strongest human, in vitro, and animal evidence for DFNA50 caused by MIR96 variants, including core family reports, mechanistic assays, transcriptomics, and 2024 therapeutic studies. It is useful as a compact citation-ready map of what is known and where current evidence remains limited.*

## 1. Disease information

### Definition and nomenclature

DFNA50 is a Mendelian form of **autosomal dominant nonsyndromic sensorineural hearing loss** caused by pathogenic MIR96 variants. “Nonsyndromic” means that hearing impairment is the principal phenotype, without a reproducible extra-auditory syndrome. Common names include **DFNA50**, **deafness, autosomal dominant 50**, **MIR96-related hearing loss**, and **autosomal dominant nonsyndromic hearing loss due to MIR96 mutation**.

### Identifiers

- **OMIM phenotype:** **613074**, Deafness, autosomal dominant 50.
- **Gene:** **MIR96**, microRNA 96; Ensembl **ENSG00000199158**. (OpenTargets Search: autosomal dominant nonsyndromic hearing loss 50-MIR96)
- **Locus:** chromosome **7q32**; MIR96 lies in an approximately 4.5-kb cluster with MIR183 and MIR182. (solda2012anovelmutation pages 1-2)
- **MONDO:** the user-supplied **MONDO:0013114** should be verified before production use. The retrieved Open Targets mapping is the broader **MONDO:0019587**, “autosomal dominant nonsyndromic hearing loss,” rather than a demonstrated DFNA50-specific MONDO record. (OpenTargets Search: autosomal dominant nonsyndromic hearing loss 50-MIR96)
- **Orphanet:** no confidently verified DFNA50-specific Orpha number was found.
- **ICD-10-CM:** no genotype-specific code; use phenotype codes such as **H90.3** (bilateral sensorineural hearing loss) where appropriate.
- **ICD-11:** classify under sensorineural hearing loss; no MIR96-specific code was verified.
- **MeSH:** **Hearing Loss, Sensorineural** and **Hearing Loss, Genetic** are appropriate indexing concepts.

### Evidence granularity

The phenotype is derived primarily from individual family members aggregated in pedigree publications—not from EHR cohorts, registries, or population surveillance. The original Spanish report concerned two pedigrees; the Italian study screened **882 genetically undiagnosed NSHL cases** and **836 controls** in its abstract (839 controls in the results text), finding one causal family. (solda2012anovelmutation pages 1-2, solda2012anovelmutation pages 2-4)

## 2. Etiology, risk, protection, and gene–environment interaction

### Primary cause

The necessary initiating factor is a **heterozygous germline pathogenic MIR96 allele**. For seed substitutions, altered nucleotide complementarity changes the set of mRNAs recognized by miR-96 while also reducing mature-miRNA abundance. For c.57T>C, altered precursor structure impairs DICER processing and quantitatively reduces mature miR-96 and miR-96* without changing the mature miR-96 seed. (lenz2011hereditaryhearingloss pages 5-6, solda2012anovelmutation pages 1-2, solda2012anovelmutation pages 2-4)

### Genetic risk factors

- A pathogenic allele confers an approximately **50% transmission probability per pregnancy**, independent of sex.
- Family history is a strong risk marker, but de novo occurrence is biologically possible in dominant hearing loss.
- Penetrance appears age-dependent and may be incomplete, especially for c.57T>C: three currently normal-hearing children carried the familial variant but were below the family’s average onset age. (solda2012anovelmutation pages 2-4)
- No validated modifier gene, protective allele, founder effect, carrier frequency, or anticipation has been demonstrated for DFNA50.
- Consanguinity is not etiologically important for this dominant disorder.

### Environmental and lifestyle factors

No toxin, infection, diet, smoking pattern, or occupational exposure causes genetically defined DFNA50. Noise, ototoxic medicines, and aging may add independent cochlear injury, but a DFNA50-specific gene–environment interaction has not been quantified. Humanized **+13G>A** mice retained normal ABR thresholds even after noise exposure in one experiment, illustrating that interaction may be allele- and species-specific rather than established generally. (lewis2024pathologicalmechanismsand pages 16-17)

### Protective factors

No genetic or pharmacologic protective factor is validated in humans. Prudent hearing conservation—avoiding excessive noise and unnecessary ototoxic exposure—is reasonable tertiary prevention but has not been shown to alter MIR96-specific natural history. Amitriptyline delayed loss temporarily in one mouse line and is not a recommended protective drug. (lewis2024pathologicalmechanismsand pages 17-18, lewis2024pathologicalmechanismsand pages 13-16)

## 3. Phenotypes

### Core phenotype

| Phenotype | Characteristics and frequency | Suggested HPO term |
|---|---|---|
| Sensorineural hearing impairment | Defining feature in clinically penetrant carriers; cochlear, generally bilateral | **HP:0000407 Sensorineural hearing impairment**; **HP:0000365 Hearing impairment** |
| Progressive hearing loss | Typical course; gradual worsening over years or decades | **HP:0001730 Progressive hearing impairment** |
| Postlingual/delayed onset | Spanish families were postlingual; c.57T>C onset approximately 25–40 years | **HP:0008527 Postlingual sensorineural hearing impairment**; adult-onset qualifier |
| High-frequency-predominant loss | Particularly prominent with +14C>A; +13G>A affected frequencies more uniformly | **HP:0005101 High-frequency hearing impairment** |
| Severe/profound hearing loss | Possible late stage; Italian proband progressed from mild at ~25, severe at 45, to profound in her sixth decade | **HP:0000404 Sensorineural hearing impairment, severe**; **HP:0012715 Profound hearing impairment** |
| Down-sloping audiogram | Documented in the Italian c.57T>C proband, with all tested frequencies affected | **HP:0008607 Abnormality of the auditory threshold** plus audiogram-shape annotation |
| Vertigo | Reported in the Italian proband, her mother, and affected brother; not established as a universal DFNA50 feature | **HP:0002321 Vertigo** |

The Spanish **+13G>A** family had broadly similar involvement across frequencies, whereas **+14C>A** produced more severe high-frequency loss. Mutant miRNA abundance was approximately 20% of wild type in available evidence. (friedman2009micrornasandepigenetic pages 8-9)

The c.57T>C proband had bilateral sensorineural impairment beginning mildly at approximately 25 years, becoming severe at 45 and profound in the sixth decade. No affected family member reported visual or olfactory impairment, although vertigo occurred in three relatives. (solda2012anovelmutation pages 2-4)

### Severity, progression, and frequency estimates

Reliable percentages cannot be assigned because the published denominator is only a few families and carriers. “Common,” “occasional,” and “rare” frequencies should therefore not be inferred from pedigree counts. Severity and onset are variable both between alleles and within families. The non-seed c.57T>C phenotype appears later and slower than the original seed-variant phenotypes. (solda2012anovelmutation pages 5-7, goel2024micrornaandrare pages 4-6)

### Behavioral, laboratory, and quality-of-life findings

No characteristic behavioral change, serum biomarker, metabolic abnormality, or histopathologic biopsy finding is known. Hearing loss can impair communication, education, employment, safety, social participation, and quality of life; however, no DFNA50-specific EQ-5D, SF-36, PROMIS, or hearing-related QoL cohort exists. Contemporary hearing-loss literature supports these general impacts, but extrapolation to DFNA50 should be labeled. (rosa2024hearinglossgenetic pages 4-5)

## 4. Genetic and molecular information

### Gene annotation

- **Symbol/name:** MIR96 / microRNA 96.
- **Molecule:** approximately 21–24-nt regulatory noncoding RNA, not a protein.
- **Cluster:** MIR183–MIR96–MIR182, coordinately expressed in neurosensory organs.
- **Expression:** cochlear inner and outer hair cells; experimental expression also occurs in other sensory tissues, but human disease remains predominantly auditory. (lenz2011hereditaryhearingloss pages 5-6, solda2012anovelmutation pages 1-2, gwilliam2024acelltype–specific pages 1-2)

Because MIR96 does not encode a protein, terms such as missense, nonsense, protein misfolding, catalytic deficiency, PDB structure, and dominant-negative protein are inapplicable. Variant class should be recorded as **single-nucleotide variants in a microRNA seed or precursor**.

### Established pathogenic variants

1. **MIR96 +13G>A**: historical mature/pre-miRNA-relative nomenclature; a seed-region nucleotide substitution affecting target recognition and mature-miRNA production. It segregated in a Spanish dominant pedigree and was absent from 462 hearing controls in the original evidence summarized by later sources. (friedman2009micrornasandepigenetic pages 8-9, lenz2011hereditaryhearingloss pages 5-6)
2. **MIR96 +14C>A**: adjacent seed-region substitution; associated with particularly high-frequency-predominant progressive hearing loss. (friedman2009micrornasandepigenetic pages 8-9)
3. **NR_029512.1:c.57T>C**; historical **miR-96(+57T>C)**; older genomic designation **NT_007933.15:g.67447397A>G**. It lies in the precursor stem and miR-96* sequence, enlarges a bulge near DICER cleavage, and reduces mature miR-96 by **85% (P=0.0006)** and miR-96* by **77% (P=0.019)** without reducing precursor levels. A compensatory mutation restoring hairpin pairing rescued expression, providing strong functional evidence. (solda2012anovelmutation pages 1-2, solda2012anovelmutation pages 2-4)

HGVS must be normalized against the current MANE/RefSeq genomic build before clinical reporting because the foundational papers use historical precursor-relative notation. These are germline variants; no somatic DFNA50 mechanism is known. Contemporary ClinVar classifications and gnomAD allele counts should be rechecked directly at ingestion time; the family studies found the variants absent from their hearing controls, but that is not equivalent to a modern global allele frequency. (solda2012anovelmutation pages 1-2, solda2012anovelmutation pages 2-4)

### Functional consequence and disease mechanism class

Seed mutations combine:

- **loss of normal targeting**, including reduced repression/buffering of wild-type targets;
- **gain of novel targeting**, because the altered seed recognizes new 3′-UTR motifs; and
- reduced mature-miRNA abundance/processing.

The dominant phenotype is therefore best considered a **neomorphic gain-of-target plus partial loss-of-function** mechanism, not simple haploinsufficiency. Heterozygous Mir183/96-null mice hear normally, whereas several heterozygous seed-mutant mice lose hearing. (lewis2024pathologicalmechanismsand pages 17-18, lewis2024pathologicalmechanismsand pages 16-17)

No validated modifier genes, disease-specific methylation signature, chromosomal rearrangement, copy-number disorder, or structural-variant mechanism has been reported.

## 5. Environmental information

There is no evidence that infection, radiation, pollution, alcohol, smoking, diet, exercise, or occupation initiates DFNA50. Environmental causes of sensorineural loss remain relevant as additive or alternative diagnoses: acoustic trauma, aminoglycosides, platinum chemotherapy, loop diuretics, congenital CMV, meningitis, and age-related hearing loss. Noise protection and medication review are sensible because cochlear hair-cell reserve is finite, but their MIR96-specific effect size is unknown.

No infectious agent, zoonotic transmission, vaccine strategy, or CHEBI-coded causal toxicant is intrinsic to DFNA50.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. A heterozygous **MIR96 seed-region point mutation** leads to altered seed complementarity and reduced normal miR-96 maturation; alternatively, **c.57T>C** leads to abnormal precursor folding and impaired DICER cleavage. (solda2012anovelmutation pages 1-2, solda2012anovelmutation pages 2-4)
2. Altered mature miR-96 leads to loss of repression/buffering of normal mRNA targets **and, for seed alleles, gain of repression of novel mRNAs**. (lewis2024pathologicalmechanismsand pages 17-18)
3. Broad target-network dysregulation leads to incomplete establishment and maintenance of cochlear hair-cell identity; 2024 hair-cell RNA-seq supports repression of supporting-cell transcriptional programs as one normal miR-96 role. (gwilliam2024acelltype–specific pages 1-2)
4. Hair-cell identity/maturation failure leads to reduced expression of auditory-development and function genes—including **MYO15A, MYO7A, USH1C, GFI1, PTPRQ, OCM, and SLC26A5**—and to abnormal electrophysiologic maturation. (lewis2009anenuinducedmutation pages 1-2, lewis2024pathologicalmechanismsand pages 17-18, gwilliam2024acelltype–specific pages 1-2)
5. These molecular abnormalities lead to mutation-dependent branching pathology: **stereociliary disorganization/loss and hair-bundle degeneration**, or **reduced inner-hair-cell ribbon synapses/disorganized innervation**. (lewis2024pathologicalmechanismsand pages 16-17)
6. Structural and synaptic dysfunction leads to impaired mechanoelectrical transduction, outer-hair-cell amplification, and auditory-nerve activation; this relationship is demonstrated in mice and inferred for human DFNA50.
7. Persistent dysfunction leads to progressive hair-cell degeneration, especially in basal/high-frequency cochlear regions, resulting in bilateral progressive sensorineural hearing loss and eventually severe/profound deafness. (friedman2009micrornasandepigenetic pages 8-9, lewis2009anenuinducedmutation pages 1-2)

### Molecular pathways and cellular processes

No single canonical Wnt, MAPK, mTOR, or PI3K–AKT cascade explains DFNA50. The proximal pathway is **miRNA biogenesis and RISC-mediated post-transcriptional gene silencing**: pri-miRNA processing by DROSHA–DGCR8, nuclear export, DICER cleavage, Argonaute/RISC loading, and seed-dependent recognition of target 3′ UTRs. A mature miRNA may regulate hundreds of transcripts through mRNA destabilization and translational inhibition. (solda2012anovelmutation pages 1-2)

Suggested GO biological-process terms include:

- **GO:0035195 gene silencing by miRNA**
- **GO:0006397 mRNA processing**
- **GO:0031054 pre-miRNA processing**
- **GO:0030219 megakaryocyte differentiation** is *not relevant* and should not be imported merely from broad miRNA annotations
- **GO:0050910 detection of mechanical stimulus involved in sensory perception of sound**
- **GO:0042490 mechanoreceptor differentiation**
- **GO:0035315 hair cell differentiation**
- **GO:0048870 cell motility** only if tied specifically to stereocilia/cytoskeletal data
- **GO:0098609 cell-cell adhesion**, **GO:0007015 actin filament organization**, and synapse-organization terms as supported by model datasets.

Relevant GO cellular components are the **RNA-induced silencing complex**, **cytoplasm**, **stereocilium**, **hair-cell apical surface**, **ribbon synapse**, and **postsynaptic density**. Suggested terms include **GO:0016442 RISC complex**, **GO:0032420 stereocilium**, and **GO:0098982 GABA-ergic synapse** only for specific brainstem model work, not core human DFNA50.

### Tissue damage, metabolism, and immunity

The demonstrated downstream tissue injury is hair-bundle disruption followed by sensory-hair-cell degeneration. Oxidative stress, inflammation, autophagy, immune dysregulation, fibrosis, ischemia, and a disease-specific metabolic signature have not been established as primary DFNA50 mechanisms. No human proteomic, metabolomic, lipidomic, or methylomic signature is available.

### Molecular profiling and advanced technologies

- **Dmdo microarray:** 96 significantly altered transcripts in homozygotes; downregulated genes included Slc26a5, Ocm, Gfi1, Ptprq, and Pitpnm1, while hundreds were predicted to be upregulated and novel mutant-seed targets were downregulated. Exact abstract quote: “**Microarray analysis revealed 96 transcripts with significantly altered expression in homozygotes**.” (lewis2009anenuinducedmutation pages 1-2)
- **2024 hair-cell RNA-seq:** 215 upregulated and 428 downregulated genes in newborn homozygous Dmdo hair cells. The authors concluded that the data support miR-96 “**possibly as a repressor of supporting cell transcriptional programs in HCs**.” The dataset is publicly available at [gEAR](https://umgear.org/p?l=miR96). (gwilliam2024acelltype–specific pages 1-2)
- **2024 human-variant knock-ins:** 328 DEGs in +13G>A and 693 in +14C>A homozygotes; only 124 were initially described as shared, with detailed supplementary accounting reporting 127 significant shared genes under the stated FDR criteria. Bulk organ-of-Corti profiling dilutes hair-cell-specific effects. (lewis2024pathologicalmechanismsand pages 17-18)
- No DFNA50 human single-cell, spatial-transcriptomic, organoid, proteomic, or multi-omic diagnostic study was identified.

## 7. Anatomical structures affected

### Organ and tissue levels

The primary organ is the **inner ear**, specifically the **cochlea** and **organ of Corti**. Suggested anatomy terms are **UBERON:0001844 inner ear**, **UBERON:0001851 cochlea**, and the corresponding current UBERON entry for organ of Corti after ontology validation. No consistent outer- or middle-ear abnormality is expected; Dmdo mice had grossly normal middle and inner-ear architecture despite microscopic sensory pathology. (lewis2009anenuinducedmutation pages 1-2)

### Cell level

Primary populations are:

- cochlear **inner hair cells**;
- cochlear **outer hair cells**;
- possibly secondary effects on afferent synapses/spiral-ganglion innervation;
- supporting cells as an aberrantly retained transcriptional identity rather than necessarily the primary injured population.

Suggested Cell Ontology terms: **CL:0000202 auditory hair cell**, with current child terms for inner and outer hair cells; verify exact release-specific IDs before ingestion.

### Subcellular level and localization

Relevant compartments are the pre-miRNA hairpin/RISC machinery, hair-cell cytoplasm, apical stereociliary bundle, and IHC ribbon synapse. Human hearing loss is generally **bilateral**; asymmetry was not established as a defining feature. Basal cochlear damage provides a plausible anatomical basis for high-frequency predominance, demonstrated most clearly in mouse models. (friedman2009micrornasandepigenetic pages 8-9, lewis2009anenuinducedmutation pages 1-2)

## 8. Temporal development

DFNA50 is generally chronic, insidious, postlingual, and progressive. The original seed-variant families developed progressive postlingual loss; c.57T>C caused onset around 25–40 years and slow worsening over decades. (solda2012anovelmutation pages 5-7, lenz2011hereditaryhearingloss pages 5-6, solda2012anovelmutation pages 2-4)

A practical staging model is:

1. **Presymptomatic carrier stage:** normal audiogram, particularly in younger carriers.
2. **Early stage:** mild threshold elevation, often high-frequency.
3. **Intermediate stage:** progressive multiband loss with speech-in-noise difficulty and increasing amplification needs.
4. **Advanced stage:** severe-to-profound bilateral loss and possible cochlear-implant candidacy.

There is no remission pattern. The disease is lifelong once manifest. Critical intervention windows are inferred from preservation of viable hair cells: auditory rehabilitation should begin when functional difficulty emerges, and mutation-directed therapy—if translated—would probably work best before extensive degeneration. In 2024 editing experiments, treatment at three weeks outperformed treatment at six weeks in mice. (zhu2024targetedgenomeediting pages 1-3)

## 9. Inheritance and population

- **Inheritance:** autosomal dominant.
- **Penetrance:** likely high but age-dependent; incomplete penetrance remains possible for c.57T>C.
- **Expressivity:** variable in age at onset, audiometric configuration, and progression.
- **Sex ratio:** no established difference; males and females can be affected.
- **Anticipation:** not reported.
- **Germline mosaicism:** not reported, although low recurrence risk cannot be absolutely excluded after an apparently de novo event.
- **Founder effects/geographic distribution:** variants were initially reported in Spanish families and c.57T>C in an Italian family; evidence supports private familial alleles rather than established founder mutations. Screening of 567 Spanish inherited-hearing-loss families and 150 American dominant families is discussed in the literature, with no replication variants in the latter cohort. (solda2012anovelmutation pages 2-4)
- **Prevalence/incidence:** no reliable cases-per-100,000 or annual incidence estimate exists. DFNA50 appears exceptionally rare: one c.57T>C family was found among 882 Italian undiagnosed NSHL patients, and the two original seed mutations were absent from 462 controls. These are ascertainment studies, not prevalence estimates. (lenz2011hereditaryhearingloss pages 5-6, solda2012anovelmutation pages 1-2)
- **Carrier frequency:** unknown; population databases should be queried variant-by-variant using current coordinates.

## 10. Diagnostics

### Clinical evaluation

Diagnosis begins with history, a three-generation pedigree, otoscopy, and comprehensive audiology:

- bilateral pure-tone air/bone audiometry;
- speech reception and word recognition, including speech-in-noise when possible;
- tympanometry to exclude conductive disease;
- otoacoustic emissions to assess outer-hair-cell function;
- auditory brainstem response when behavioral testing is unreliable;
- vestibular assessment if vertigo is present.

No blood chemistry, urine assay, imaging signature, or biopsy diagnoses DFNA50. MRI/CT is reserved for atypical asymmetry, neurologic signs, implant planning, or another suspected lesion.

### Molecular testing

The preferred method is a comprehensive hereditary-hearing-loss NGS panel that explicitly captures **noncoding MIR96 and its precursor/seed region**, with deletion/duplication analysis for other genes. Conventional exome sequencing may miss MIR96 because it is noncoding and poorly covered; WGS can detect it if properly analyzed. If a familial variant is known, targeted Sanger or NGS testing is efficient. Segregation and ACMG/AMP interpretation should incorporate rarity, phenotype, cosegregation, seed conservation, and functional processing/target data.

CMA, karyotyping, FISH, mitochondrial sequencing, and repeat-expansion testing are not first-line tests for classic DFNA50, but broader testing may be appropriate when phenotype or pedigree suggests another diagnosis. RNA-seq, proteomics, metabolomics, epigenomics, and liquid biopsy are research tools, not validated diagnostics.

### Diagnostic criteria and differential diagnosis

There are no formal DFNA50-specific clinical criteria. A molecular diagnosis requires a compatible progressive sensorineural phenotype plus a pathogenic/likely pathogenic MIR96 variant, or compelling segregation and functional evidence for a novel variant.

Differentials include other dominant progressive nonsyndromic forms—**KCNQ4/DFNA2, WFS1/DFNA6/14/38, TECTA/DFNA8/12, EYA4/DFNA10, MYO6/DFNA22, POU4F3/DFNA15, ACTG1/DFNA20/26**—and acquired noise, ototoxic, autoimmune, infectious, or age-related loss. Syndromic disease should be reconsidered if retinal, renal, cardiac, neurologic, pigmentary, or vestibular findings exceed the limited DFNA50 phenotype.

### Screening

Newborn physiologic screening may be normal because onset can be delayed. Once a familial variant is known, **cascade genetic testing plus baseline audiometry and longitudinal surveillance** is the most efficient secondary-prevention strategy. General reviews emphasize that delayed progressive forms can pass newborn screening and that molecular diagnosis improves prognosis, counseling, and timely intervention. (rosa2024hearinglossgenetic pages 4-5)

## 11. Outcome and prognosis

DFNA50 is disabling but not known to shorten life expectancy or increase disease-specific mortality. Five- and ten-year survival statistics are therefore not applicable. The principal outcome is progressive auditory disability, potentially reaching profound deafness.

No spontaneous recovery is expected. Hearing aids and cochlear implants can improve communication but do not reverse the underlying genetic lesion or regenerate lost hair cells. Prognosis depends mainly on the allele, current hearing thresholds, progression rate, speech recognition, and residual hair-cell/neural function; no validated molecular prognostic biomarker exists.

DFNA50-specific cochlear-implant outcomes have not been reported in a meaningful cohort. Because the major lesion is sensory hair-cell rather than primary spiral-ganglion degeneration, benefit is biologically plausible, but this is an inference. A 2023 genetic CI cohort found poorer outcomes particularly when mutations involved neural cochlear components, supporting—not proving—the expectation that sensory lesions may fare better. General CI evidence should not be represented as DFNA50-specific. (tropitzsch2023variabilityincochlear pages 1-5)

For context, a 2024 prospective study of 100 older adults with severe/profound loss found an 18-month HUI3 improvement of **0.13 (95% CI 0.07–0.18; P<0.001)**, loneliness reduction of **0.61**, and Hearing Handicap Inventory improvement of **8.7 points** after implantation. These values demonstrate rehabilitation potential but were not obtained from MIR96 carriers. (cuda2024improvingqualityof pages 1-2)

## 12. Treatment and current implementation

### Current clinical care

There is no FDA/EMA-approved MIR96-specific drug or gene therapy. Management follows progressive sensorineural-hearing-loss practice:

1. regular audiologic monitoring, generally annually or sooner with subjective change;
2. appropriately fitted bilateral hearing aids for aidable loss;
3. communication strategies, remote microphones/assistive listening devices, captioning, and auditory rehabilitation;
4. speech-language and educational support for pediatric onset;
5. cochlear-implant evaluation when hearing aids no longer provide adequate speech understanding;
6. management of tinnitus or vertigo when present;
7. genetic counseling and cascade testing.

Suggested NCIT intervention concepts include **Hearing Aid**, **Cochlear Implantation**, **Auditory Rehabilitation**, **Genetic Counseling**, **Genetic Testing**, **CRISPR-Cas9 Gene Editing**, and **Adeno-Associated Virus Vector Therapy**; exact NCIT codes should be validated against the current release.

The 2024 American Cochlear Implant Alliance recommends individualized, ear-specific evaluation and a revised “60/60” referral framework rather than waiting for bilateral profound loss. This is general adult guidance, not MIR96-specific. (zeitler2024americancochlearimplant pages 1-3)

### Experimental pharmacotherapy

Transcriptome anti-correlation nominated **amitriptyline**, a tricyclic antidepressant. In +14C>A heterozygous mice, 200 µg/mL in drinking water significantly delayed threshold deterioration at **24–36 kHz**, most clearly at 30 kHz at four weeks. A 400-µg/mL dose offered no additional benefit; homozygotes did not improve. The effect was temporary, doses were far above standard human exposure by body weight, and adverse-effect liability is substantial. The authors explicitly stated that this was proof of concept, not a recommendation for human use. (lewis2024pathologicalmechanismsand pages 17-18, lewis2024pathologicalmechanismsand pages 13-16)

### Genome editing—major 2024 development

Zhu et al., published July 2024 in *Science Translational Medicine*, optimized **SaCas9-KKH plus mutation-specific sgRNA**, delivered by AAV to the cochlea of heterozygous Mir96^14C>A/+ mice. Both presymptomatic three-week-old and symptomatic six-week-old adults had long-term auditory improvement/preservation, with greater efficacy at the younger age. Cas9 expression was transient, and the investigators found no evidence of AAV genomic integration. A dual-AAV “master” construct incorporated guides against all known human MIR96 mutations; mouse and human MIR96 sequences are 100% homologous. (zhu2024targetedgenomeediting pages 1-3)

Exact abstract quote: “**Targeted genome editing of MIR96 mutations preserved long-term hearing in adult mice without evidence of genomic integration.**” The work is strong preclinical evidence but does not establish human safety, off-target risk, immune tolerability, surgical delivery feasibility, durability over a human lifespan, or efficacy after advanced hair-cell loss. DOI: [10.1126/scitranslmed.adn0689](https://doi.org/10.1126/scitranslmed.adn0689), July 2024. (zhu2024targetedgenomeediting pages 1-3)

No DFNA50-targeted interventional trial or NCT identifier was found in the ClinicalTrials.gov search. Cell therapy, ASOs, siRNA, immunotherapy, or gene replacement are not clinically established; allele-selective silencing is mechanistically attractive because one wild-type copy is sufficient in heterozygous knockout mice. (lewis2024pathologicalmechanismsand pages 13-16, lewis2024pathologicalmechanismsand pages 16-17)

## 13. Prevention

### Primary prevention

The mutation cannot be prevented by lifestyle change. Reproductive options after molecular diagnosis include genetic counseling, natural conception with prenatal diagnosis, preimplantation genetic testing for monogenic disease, donor gametes, or adoption. Decisions require nondirective counseling because hearing status, Deaf identity, variable expressivity, and emerging treatments affect values and preferences.

### Secondary prevention

- Cascade testing of adult and minor relatives when results will change surveillance or early intervention.
- Baseline and serial audiograms for carriers, including those who passed newborn screening.
- Early amplification and communication support when functional loss appears.
- Prospective trial readiness through precise HGVS confirmation and natural-history documentation.

### Tertiary prevention

Use hearing conservation, avoid unnecessary ototoxic drugs, treat middle-ear disease promptly, optimize amplification, and refer before speech recognition becomes extremely poor. No vaccine, medication prophylaxis, or public-health sanitation intervention prevents DFNA50.

## 14. Other species and natural disease

No naturally occurring veterinary DFNA50 syndrome, breed association, zoonotic transmission, or cross-species infectious susceptibility was identified. The relevant orthologue is **Mir96** in mouse and miR-96 orthologues in zebrafish and other vertebrates. MIR96 sequence and neurosensory expression are strongly conserved.

In zebrafish, the miR-183 family is expressed in inner-ear and lateral-line hair cells. Experimental overexpression of miR-96/miR-182 can expand sensory patches and hair-cell numbers, whereas knockdown reduces hair cells and disrupts semicircular canals and neuromasts. These are induced developmental phenotypes, not naturally occurring veterinary disease. (solda2012anovelmutation pages 1-2)

Suggested taxonomy identifiers: **Homo sapiens, NCBI Taxon 9606**; **Mus musculus, 10090**; **Danio rerio, 7955**. No VBO breed term applies.

## 15. Model organisms

### Diminuendo mouse

The ENU-induced **Mir96^Dmdo** allele is an A>T seed substitution with semidominant inheritance. Heterozygotes lose the Preyer reflex at four to six weeks and have thresholds elevated by approximately **60 dB** at four weeks; homozygotes have no cochlear responses. Homozygotes develop abnormal stereocilia by postnatal days 4–5 and marked degeneration by day 7; heterozygotes later lose many outer hair cells in middle/basal turns. Vestibular hair-cell pathology and circling occur, especially in severe animals. (lewis2009anenuinducedmutation pages 1-2)

The landmark abstract states: “**Heterozygotes show progressive loss of hearing and hair cell anomalies, while homozygotes have no cochlear responses.**” DOI: [10.1038/ng.369](https://doi.org/10.1038/ng.369), May 2009; PMID **19363478**. (OpenTargets Search: autosomal dominant nonsyndromic hearing loss 50-MIR96, lewis2009anenuinducedmutation pages 1-2)

### Human-variant knock-in mice

Knock-in models carry human **+13G>A** or **+14C>A** alleles. Homozygotes of both are profoundly deaf; +14C>A heterozygotes develop progressive loss from around four weeks, whereas +13G>A heterozygotes retain normal ABR thresholds up to one year despite subtle shortest-row OHC stereocilia loss. +13G>A homozygotes show reduced IHC synaptic densities, while +14C>A produces more severe stereociliary-bundle pathology. The failure of mouse +13G>A heterozygotes to reproduce human deafness is an important species/3′-UTR limitation; human **RAB11A**, for example, has mutant-seed matches absent from mouse Rab11a. (lewis2024pathologicalmechanismsand pages 16-17)

### Null and cluster models

Heterozygous Mir183/96 double-null mice have normal hearing, whereas homozygotes are profoundly deaf with abnormal bundles and reduced IHC synapses. This comparison is central evidence that seed substitutions act through gained novel targets, not merely loss of MIR96 dosage. Cluster overexpression/misexpression also causes progressive loss and eventual inner/outer hair-cell degeneration, showing that cochlear homeostasis is sensitive to miRNA dosage in either direction. (lewis2024pathologicalmechanismsand pages 17-18, lewis2024pathologicalmechanismsand pages 16-17)

### Model strengths, limitations, and uses

**Strengths:** conserved mature sequence, accessible cochlear physiology, ABR/DPOAE endpoints, hair-cell ultrastructure, allele-specific targeting, and direct therapeutic testing. **Limitations:** much faster murine course, genetic-background effects, divergent target 3′ UTRs, homozygous models more severe than human dominant disease, and uncertain translation of cochlear dosing/surgery. Models are suited to target-network analysis, hair-cell maturation, therapeutic-window definition, pharmacologic screening, allele-selective silencing, and in vivo genome editing.

Resources include MGI, IMSR/MMRRC where lines are deposited, ArrayExpress **E-TABM-489** for the original Dmdo microarray, gEAR for 2024 hair-cell RNA-seq, and SRA **PRJNA1088125** for the 2024 editing study. (lewis2009anenuinducedmutation pages 1-2, zhu2024targetedgenomeediting pages 14-16, gwilliam2024acelltype–specific pages 1-2)

## Evidence assessment and key gaps

Human evidence strongly supports MIR96 causality through segregation, absence in controls, evolutionary conservation, and functional assays, but the clinical evidence base remains only a few pedigrees. The exact prevalence, penetrance by age, annual threshold deterioration, speech-recognition trajectory, environmental modifiers, CI outcomes, and patient-reported outcomes are unknown. Modern ClinVar/gnomAD normalization, prospective international natural-history cohorts, and variant-specific longitudinal audiometry are priorities.

The 2024 mouse studies materially advance understanding: cell-specific RNA-seq identifies a failure to suppress supporting-cell programs; humanized alleles demonstrate that different single-nucleotide changes produce distinct synaptic and stereociliary pathologies; transcriptome-guided pharmacology provides temporary proof of principle; and adult in vivo editing establishes mutation-directed rescue after symptom onset. Nevertheless, genome editing remains experimental and should not be offered outside an appropriately authorized clinical trial. (zhu2024targetedgenomeediting pages 1-3, lewis2024pathologicalmechanismsand pages 17-18, lewis2024pathologicalmechanismsand pages 13-16, gwilliam2024acelltype–specific pages 1-2)

### Selected primary and recent sources

- Mencía et al. *Nature Genetics*. May 2009. “Mutations in the seed region of human miR-96 are responsible for nonsyndromic progressive hearing loss.” PMID **19363479**; DOI [10.1038/ng.355](https://doi.org/10.1038/ng.355). (OpenTargets Search: autosomal dominant nonsyndromic hearing loss 50-MIR96, lenz2011hereditaryhearingloss pages 5-6)
- Lewis et al. *Nature Genetics*. May 2009. PMID **19363478**; DOI [10.1038/ng.369](https://doi.org/10.1038/ng.369). (OpenTargets Search: autosomal dominant nonsyndromic hearing loss 50-MIR96, lewis2009anenuinducedmutation pages 1-2)
- Soldà et al. *Human Molecular Genetics*. Advance publication October 28, 2011; volume publication 2012. DOI [10.1093/hmg/ddr493](https://doi.org/10.1093/hmg/ddr493). Exact abstract conclusion: “**a quantitative defect of this miRNA may contribute to NSHL**.” (solda2012anovelmutation pages 1-2)
- Aldè et al. *Biomedicines*. June 2023. DOI [10.3390/biomedicines11061616](https://doi.org/10.3390/biomedicines11061616). (alde2023autosomaldominantnonsyndromic pages 16-17)
- Gwilliam et al. *Frontiers in Audiology and Otology*. May 9, 2024. DOI [10.3389/fauot.2024.1400576](https://doi.org/10.3389/fauot.2024.1400576). (gwilliam2024acelltype–specific pages 1-2)
- Zhu et al. *Science Translational Medicine*. July 2024. DOI [10.1126/scitranslmed.adn0689](https://doi.org/10.1126/scitranslmed.adn0689). (zhu2024targetedgenomeediting pages 1-3)
- Lewis et al. *Genome Medicine*. October 2024; 16:121. DOI [10.1186/s13073-024-01394-5](https://doi.org/10.1186/s13073-024-01394-5). (lewis2024pathologicalmechanismsand pages 17-18, lewis2024pathologicalmechanismsand pages 13-16)

**Knowledge-base caution:** ontology identifiers, present-day ClinVar assertions, and population frequencies should be programmatically refreshed before ingestion. Historical MIR96 variant notation is not consistently compliant with current genomic HGVS, and the supplied MONDO identifier could not be independently confirmed from the retrieved evidence.

References

1. (OpenTargets Search: autosomal dominant nonsyndromic hearing loss 50-MIR96): Open Targets Query (autosomal dominant nonsyndromic hearing loss 50-MIR96, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (zhu2024targetedgenomeediting pages 1-3): Wenliang Zhu, Wan Du, Arun Prabhu Rameshbabu, Ariel Miura Armstrong, Stewart Silver, Yehree Kim, Wei Wei, Yilai Shu, Xuezhong Liu, Morag A. Lewis, Karen P. Steel, and Zheng-Yi Chen. Targeted genome editing restores auditory function in adult mice with progressive hearing loss caused by a human microrna mutation. Science translational medicine, 16:eadn0689-eadn0689, Jul 2024. URL: https://doi.org/10.1126/scitranslmed.adn0689, doi:10.1126/scitranslmed.adn0689. This article has 32 citations and is from a highest quality peer-reviewed journal.

3. (lewis2024pathologicalmechanismsand pages 17-18): Morag A. Lewis, Maria Lachgar-Ruiz, Francesca Di Domenico, Graham Duddy, Jing Chen, Sergio Fernandez, Matias Morin, Gareth Williams, Miguel Angel Moreno Pelayo, and Karen P. Steel. Pathological mechanisms and candidate therapeutic approaches in the hearing loss of mice carrying human mir96 mutations. Oct 2024. URL: https://doi.org/10.1186/s13073-024-01394-5, doi:10.1186/s13073-024-01394-5. This article has 4 citations and is from a highest quality peer-reviewed journal.

4. (lewis2024pathologicalmechanismsand pages 13-16): Morag A. Lewis, Maria Lachgar-Ruiz, Francesca Di Domenico, Graham Duddy, Jing Chen, Sergio Fernandez, Matias Morin, Gareth Williams, Miguel Angel Moreno Pelayo, and Karen P. Steel. Pathological mechanisms and candidate therapeutic approaches in the hearing loss of mice carrying human mir96 mutations. Oct 2024. URL: https://doi.org/10.1186/s13073-024-01394-5, doi:10.1186/s13073-024-01394-5. This article has 4 citations and is from a highest quality peer-reviewed journal.

5. (gwilliam2024acelltype–specific pages 1-2): Kathleen Gwilliam, Michal Sperber, Katherine Perry, Kevin P. Rose, Laura Ginsberg, Nikhil Paladugu, Yang Song, Beatrice Milon, Ran Elkon, and Ronna Hertzano. A cell type–specific approach to elucidate the role of mir-96 in inner ear hair cells. Frontiers in audiology and otology, May 2024. URL: https://doi.org/10.3389/fauot.2024.1400576, doi:10.3389/fauot.2024.1400576. This article has 2 citations.

6. (friedman2009micrornasandepigenetic pages 8-9): Lilach M. Friedman and Karen B. Avraham. Micrornas and epigenetic regulation in the mammalian inner ear: implications for deafness. Mammalian Genome, 20:581-603, Oct 2009. URL: https://doi.org/10.1007/s00335-009-9230-5, doi:10.1007/s00335-009-9230-5. This article has 68 citations and is from a peer-reviewed journal.

7. (lenz2011hereditaryhearingloss pages 5-6): Danielle R. Lenz and Karen B. Avraham. Hereditary hearing loss: from human mutation to mechanism. Hearing Research, 281:3-10, Nov 2011. URL: https://doi.org/10.1016/j.heares.2011.05.021, doi:10.1016/j.heares.2011.05.021. This article has 73 citations and is from a domain leading peer-reviewed journal.

8. (solda2012anovelmutation pages 5-7): Giulia Soldà, Michela Robusto, Paola Primignani, Pierangela Castorina, Elena Benzoni, Antonio Cesarani, Umberto Ambrosetti, Rosanna Asselta, and Stefano Duga. A novel mutation within the mir96 gene causes non-syndromic inherited hearing loss in an italian family by altering pre-mirna processing. Human Molecular Genetics, 21(3):577-585, Oct 2012. URL: https://doi.org/10.1093/hmg/ddr493, doi:10.1093/hmg/ddr493. This article has 136 citations and is from a domain leading peer-reviewed journal.

9. (robusto2014inheritedhearingloss pages 91-92): MICHELA ROBUSTO. Inherited hearing loss: from gene variants to mechanisms of disease. ArXiv, Jan 2014. URL: https://doi.org/10.13130/m-robusto\_phd2014-01-24, doi:10.13130/m-robusto\_phd2014-01-24. This article has 1 citations.

10. (solda2012anovelmutation pages 1-2): Giulia Soldà, Michela Robusto, Paola Primignani, Pierangela Castorina, Elena Benzoni, Antonio Cesarani, Umberto Ambrosetti, Rosanna Asselta, and Stefano Duga. A novel mutation within the mir96 gene causes non-syndromic inherited hearing loss in an italian family by altering pre-mirna processing. Human Molecular Genetics, 21(3):577-585, Oct 2012. URL: https://doi.org/10.1093/hmg/ddr493, doi:10.1093/hmg/ddr493. This article has 136 citations and is from a domain leading peer-reviewed journal.

11. (solda2012anovelmutation pages 2-4): Giulia Soldà, Michela Robusto, Paola Primignani, Pierangela Castorina, Elena Benzoni, Antonio Cesarani, Umberto Ambrosetti, Rosanna Asselta, and Stefano Duga. A novel mutation within the mir96 gene causes non-syndromic inherited hearing loss in an italian family by altering pre-mirna processing. Human Molecular Genetics, 21(3):577-585, Oct 2012. URL: https://doi.org/10.1093/hmg/ddr493, doi:10.1093/hmg/ddr493. This article has 136 citations and is from a domain leading peer-reviewed journal.

12. (lewis2009anenuinducedmutation pages 1-2): Morag A Lewis, Elizabeth Quint, Anne M Glazier, Helmut Fuchs, Martin Hrabé De Angelis, Cordelia Langford, Stijn van Dongen, Cei Abreu-Goodger, Matias Piipari, Nick Redshaw, Tamas Dalmay, Miguel Angel Moreno-Pelayo, Anton J Enright, and Karen P Steel. An enu-induced mutation of mir-96 associated with progressive hearing loss in mice. Apr 2009. URL: https://doi.org/10.1038/ng.369, doi:10.1038/ng.369. This article has 402 citations and is from a highest quality peer-reviewed journal.

13. (lewis2024pathologicalmechanismsand pages 16-17): Morag A. Lewis, Maria Lachgar-Ruiz, Francesca Di Domenico, Graham Duddy, Jing Chen, Sergio Fernandez, Matias Morin, Gareth Williams, Miguel Angel Moreno Pelayo, and Karen P. Steel. Pathological mechanisms and candidate therapeutic approaches in the hearing loss of mice carrying human mir96 mutations. Oct 2024. URL: https://doi.org/10.1186/s13073-024-01394-5, doi:10.1186/s13073-024-01394-5. This article has 4 citations and is from a highest quality peer-reviewed journal.

14. (zhu2024targetedgenomeediting pages 12-14): Wenliang Zhu, Wan Du, Arun Prabhu Rameshbabu, Ariel Miura Armstrong, Stewart Silver, Yehree Kim, Wei Wei, Yilai Shu, Xuezhong Liu, Morag A. Lewis, Karen P. Steel, and Zheng-Yi Chen. Targeted genome editing restores auditory function in adult mice with progressive hearing loss caused by a human microrna mutation. Science translational medicine, 16:eadn0689-eadn0689, Jul 2024. URL: https://doi.org/10.1126/scitranslmed.adn0689, doi:10.1126/scitranslmed.adn0689. This article has 32 citations and is from a highest quality peer-reviewed journal.

15. (goel2024micrornaandrare pages 4-6): Himanshu Goel and Amy Goel. Microrna and rare human diseases. Genes, 15:1243, Sep 2024. URL: https://doi.org/10.3390/genes15101243, doi:10.3390/genes15101243. This article has 20 citations.

16. (rosa2024hearinglossgenetic pages 4-5): Maria Agustina De Rosa, Maria T. Bernardi, Soledad Kleppe, and Katherina Walz. Hearing loss: genetic testing, current advances and the situation in latin america. Genes, 15:178, Jan 2024. URL: https://doi.org/10.3390/genes15020178, doi:10.3390/genes15020178. This article has 14 citations.

17. (tropitzsch2023variabilityincochlear pages 1-5): Anke Tropitzsch, Thore Schade-Mann, Philipp Gamerdinger, Saskia Dofek, Björn Schulte, Martin Schulze, Sarah Fehr, Saskia Biskup, Tobias B. Haack, Petra Stöbe, Andreas Heyd, Jennifer Harre, Anke Lesinski-Schiedat, Andreas Büchner, Thomas Lenarz, Athanasia Warnecke, Marcus Müller, Barbara Vona, Ernst Dahlhoff, Hubert Löwenheim, and Martin Holderried. Variability in cochlear implantation outcomes in a large german cohort with a genetic etiology of hearing loss. Ear and Hearing, 44:1464-1484, Jul 2023. URL: https://doi.org/10.1097/aud.0000000000001386, doi:10.1097/aud.0000000000001386. This article has 40 citations and is from a highest quality peer-reviewed journal.

18. (cuda2024improvingqualityof pages 1-2): D. Cuda, M. Manrique, Á. Ramos, M. Marx, R. Bovo, R. Khnifes, O. Hilly, J. Belmin, G. Stripeikyte, P. L. Graham, C. J. James, P. V. Greenham, and I. Mosnier. Improving quality of life in the elderly: hearing loss treatment with cochlear implants. BMC Geriatrics, Jan 2024. URL: https://doi.org/10.1186/s12877-023-04642-2, doi:10.1186/s12877-023-04642-2. This article has 49 citations and is from a domain leading peer-reviewed journal.

19. (zeitler2024americancochlearimplant pages 1-3): Daniel M. Zeitler, Sandra M. Prentiss, Sarah A. Sydlowski, and Camille C. Dunn. American cochlear implant alliance task force: recommendations for determining cochlear implant candidacy in adults. The Laryngoscope, Jul 2024. URL: https://doi.org/10.1002/lary.30879, doi:10.1002/lary.30879. This article has 55 citations.

20. (zhu2024targetedgenomeediting pages 14-16): Wenliang Zhu, Wan Du, Arun Prabhu Rameshbabu, Ariel Miura Armstrong, Stewart Silver, Yehree Kim, Wei Wei, Yilai Shu, Xuezhong Liu, Morag A. Lewis, Karen P. Steel, and Zheng-Yi Chen. Targeted genome editing restores auditory function in adult mice with progressive hearing loss caused by a human microrna mutation. Science translational medicine, 16:eadn0689-eadn0689, Jul 2024. URL: https://doi.org/10.1126/scitranslmed.adn0689, doi:10.1126/scitranslmed.adn0689. This article has 32 citations and is from a highest quality peer-reviewed journal.

21. (alde2023autosomaldominantnonsyndromic pages 16-17): Mirko Aldè, Giovanna Cantarella, Diego Zanetti, Lorenzo Pignataro, Ignazio La Mantia, Luigi Maiolino, Salvatore Ferlito, Paola Di Mauro, Salvatore Cocuzza, Jérôme René Lechien, Giannicola Iannella, Francois Simon, and Antonino Maniaci. Autosomal dominant non-syndromic hearing loss (dfna): a comprehensive narrative review. Biomedicines, 11:1616, Jun 2023. URL: https://doi.org/10.3390/biomedicines11061616, doi:10.3390/biomedicines11061616. This article has 65 citations.

## Artifacts

- [Edison artifact artifact-00](Autosomal_Dominant_Nonsyndromic_Hearing_Loss_50-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 15 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 15 |
| On topic | 8 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 27 |
| Resolved | 26 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0013114` (2 mentions) - the report calls it "if available"; MONDO calls it **autosomal dominant nonsyndromic hearing loss 50**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0000404` (1 mention) - HP does not contain this term