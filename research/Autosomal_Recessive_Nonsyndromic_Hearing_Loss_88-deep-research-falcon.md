---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-17T10:01:48.780038'
end_time: '2026-09-17T10:11:20.312699'
duration_seconds: 571.53
template_file: templates/disease_pathophysiology_research.md
template_sha: 1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666
template_variables:
  disease_name: Autosomal Recessive Nonsyndromic Hearing Loss 88
  mondo_id: MONDO:0014182
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 29
reference_validation:
  total_references: 7
  verified: 7
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 7
  on_topic: 4
  validator_version: 0.2.1
term_validation:
  total_terms: 13
  verified: 13
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0014182
    reported_labels:
    - if available
    ontology_label: autosomal recessive nonsyndromic hearing loss 88
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Autosomal_Recessive_Nonsyndromic_Hearing_Loss_88-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autosomal Recessive Nonsyndromic Hearing Loss 88
- **MONDO ID:** MONDO:0014182 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Recessive Nonsyndromic Hearing Loss 88** covering all of the
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
- **Disease Name:** Autosomal Recessive Nonsyndromic Hearing Loss 88
- **MONDO ID:** MONDO:0014182 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Recessive Nonsyndromic Hearing Loss 88** covering all of the
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


# Autosomal Recessive Nonsyndromic Hearing Loss 88 (DFNB88): Research Report

## Executive summary

Autosomal recessive nonsyndromic hearing loss 88 (DFNB88) is an exceptionally rare Mendelian hearing disorder attributed to biallelic **ELMOD3** dysfunction. The disease-defining evidence comes principally from one large consanguineous Pakistani pedigree, PKDF468, in which homozygosity mapping, exome sequencing, segregation analysis, population controls, and functional assays implicated homozygous **ELMOD3 c.794T>C (p.Leu265Ser)**. Affected relatives had bilateral, prelingual, severe-to-profound **mixed** hearing loss without a consistent extra-auditory syndrome or vestibular deficit. Consequently, the phenotype, penetrance, prevalence, natural history, and variant spectrum remain incompletely defined (jaworek2013analterationin pages 1-2, jaworek2013analterationin pages 2-4, jaworek2013analterationin pages 4-6).

The strongest mechanistic model is impaired regulation of ARL2-family small GTPases and actin-rich cochlear hair-cell stereocilia. The p.Leu265Ser protein lost measurable ARL2 GTPase-activating-protein activity in vitro and localized abnormally to actin-based structures. Homozygous Elmod3-null mice developed progressive cochlear dysfunction, reduced F-actin, shortened/fused inner-hair-cell stereocilia, and progressive outer-hair-cell bundle degeneration (jaworek2013analterationin pages 1-2, li2019elmod3knockoutleads pages 1-2, li2019elmod3knockoutleads pages 2-3, li2019elmod3knockoutleads pages 3-5).

| Evidence domain | Finding | Evidence type | Key source/date/DOI/PMID | Confidence / limitation |
|---|---|---|---|---|
| Foundational genetics | In consanguineous Pakistani family PKDF468, homozygosity mapping defined DFNB88 at 2p11.2 (maximum two-point LOD 4.74), and exome sequencing identified homozygous **ELMOD3 c.794T>C (p.Leu265Ser)** segregating with hearing loss. The variant was absent from 524 ethnically matched control chromosomes, 1000 Genomes, and 6,500 NHLBI-ESP individuals. (jaworek2013analterationin pages 2-4, jaworek2013analterationin pages 4-6) | Human pedigree, linkage, segregation, exome sequencing | Jaworek et al.; published 2013-09-05; DOI [10.1371/journal.pgen.1003774](https://doi.org/10.1371/journal.pgen.1003774); PMID **24039609** (jaworek2013analterationin pages 1-2, liu2023generegulationanalysis pages 15-16) | **High for this family and variant.** Replication and disease-wide genotype–phenotype data remain sparse; evidence does not establish population-level penetrance or prevalence. |
| Human phenotype | Affected relatives had **bilateral, prelingual, severe-to-profound mixed hearing loss**, including a substantial conductive component in at least one documented audiogram. No clear vestibular, skin, renal, or retinal abnormalities were identified; temporal-bone CT was largely normal. (jaworek2013analterationin pages 1-2, jaworek2013analterationin pages 2-4) | Human clinical and audiologic characterization | Jaworek et al.; 2013-09-05; DOI [10.1371/journal.pgen.1003774](https://doi.org/10.1371/journal.pgen.1003774); PMID **24039609** | **Moderate.** Directly observed but based on one extended family; phenotype frequencies, longitudinal progression, and quality-of-life scores were not reported. |
| Biochemical mechanism | ELMOD3 localized to actin-rich cochlear stereocilia and exhibited GAP activity toward **ARL2**; p.Leu265Ser impaired localization to actin-based structures and **abolished recombinant ELMOD3 ARL2-GAP activity**, supporting a loss-of-function mechanism affecting small-GTPase/cytoskeletal regulation. (jaworek2013analterationin pages 1-2, jaworek2013analterationin pages 4-6) | Rodent tissue localization, transfected-cell assays, recombinant-protein biochemistry | Jaworek et al.; 2013-09-05; DOI [10.1371/journal.pgen.1003774](https://doi.org/10.1371/journal.pgen.1003774); PMID **24039609** | **Moderate-to-high mechanistic support.** Functional effect was demonstrated in vitro, but the complete causal sequence in human cochlear cells remains partly inferred. |
| Elmod3-null mouse | CRISPR-generated homozygous null mice developed moderate, progressive hearing loss beginning at 2 months; ABR abnormalities involved all tested frequencies, and DPOAE shifts implicated outer-hair-cell dysfunction. Mutants showed reduced cochlear F-actin, shortened/fused inner-hair-cell stereocilia, progressive outer-hair-cell stereocilia degeneration, reduced ARL2 expression, and normal vestibular behavior. (li2019elmod3knockoutleads pages 1-2, li2019elmod3knockoutleads pages 2-3, li2019elmod3knockoutleads pages 3-5, li2019elmod3knockoutleads pages 5-7) | In vivo genetic model; ABR, DPOAE, histology, immunostaining, SEM | Li et al.; advance publication 2019-10-19; DOI [10.1093/hmg/ddz240](https://doi.org/10.1093/hmg/ddz240) (li2019elmod3knockoutleads pages 1-2) | **High for mouse phenotype; moderate for human translation.** Mouse onset/severity differs from the documented prelingual severe-to-profound human phenotype, and only homozygous mice were affected. |
| 2023 iPSC transcriptomics | Patient-derived iPSCs with heterozygous **ELMOD3 c.512A>G (p.His171Arg)** and an isogenic CRISPR-corrected line showed altered cytoskeletal, ion-transport, ear-morphogenesis, GPCR, PI3K–AKT, cAMP, calcium-signaling, and cell-adhesion programs; 26 downregulated genes related to ion transmembrane transport and 16 to potassium transport were reported. **This variant causes autosomal-dominant progressive hearing loss and is not DFNB88-specific evidence.** (liu2023generegulationanalysis pages 1-2, liu2023generegulationanalysis pages 10-12) | Patient-derived iPSC model, CRISPR correction, bulk RNA-seq, computational enrichment, qRT-PCR | Liu et al.; published 2023-09-14; DOI [10.1371/journal.pone.0288640](https://doi.org/10.1371/journal.pone.0288640) | **Supporting ELMOD3 biology only.** Undifferentiated iPSCs are not cochlear hair cells; control comparisons were confounded by sex and other genomic differences, and the genotype/inheritance differs from DFNB88. |
| Population rarity | A 2024 review identified 51 ARNSHL genes in Pakistan. Thirteen common genes accounted for more than half of profound hearing-loss cases; other genes, the category containing rare ELMOD3, each contributed **<2%**. (shadab2024autosomalrecessivenon‐syndromic pages 1-2) | Population-focused literature review | Shadab et al.; accepted 2024-01-02; DOI [10.1111/jcmm.18119](https://doi.org/10.1111/jcmm.18119) | **Low-to-moderate for ELMOD3 frequency.** The <2% figure is a category-level estimate, not a DFNB88-specific prevalence or carrier-frequency measurement. |
| Diagnostics and management | Practical diagnosis combines newborn/clinical audiology, air- and bone-conduction testing, tympanometry/OAE/ABR as appropriate, and molecular confirmation of **biallelic pathogenic ELMOD3 variants**, preferably through a comprehensive hearing-loss panel with CNV analysis or exome/genome sequencing. Current management is phenotype-directed hearing rehabilitation with hearing aids, cochlear-implant assessment, speech-language support, educational accommodations, and genetic counseling. General reviews state that hearing aids and cochlear implants remain the principal corrective options. (petit2023deafnessfromgenetic pages 1-5, zhang2024aav‐mediatedgenetherapy pages 1-2) | Clinical application extrapolated from hereditary-hearing-loss standards; disease molecular evidence | Petit et al.; 2023; DOI [10.1038/s41576-023-00597-7](https://doi.org/10.1038/s41576-023-00597-7); Zhang et al.; 2024; DOI [10.1002/advs.202402166](https://doi.org/10.1002/advs.202402166) | **Moderate.** No DFNB88-specific diagnostic guideline, validated biomarker, treatment algorithm, or outcome series was identified. Conductive components require independent middle-ear evaluation rather than attribution to ELMOD3 alone. |
| Trials and disease-modifying therapy | No DFNB88/ELMOD3-specific interventional trial or approved pharmacologic, RNA, cell, editing, or gene-replacement therapy was identified. Hereditary-deafness gene therapy has restored hearing in more than 20 mouse models and reached clinical translation for **OTOF/DFNB9**, but this should not be extrapolated as demonstrated efficacy for DFNB88. (zhang2024aav‐mediatedgenetherapy pages 1-2) | Clinical-trial search and contemporary therapeutic review | Zhang et al.; 2024; DOI [10.1002/advs.202402166](https://doi.org/10.1002/advs.202402166) | **High confidence that evidence is absent in the searched sources, not proof that no unindexed study exists.** ELMOD3 therapy remains preclinical/conceptual, with delivery, target-cell, timing, efficacy, and safety unresolved. |


*Table: Compact appraisal of the principal human, biochemical, mouse, population, diagnostic, and therapeutic evidence for ELMOD3-associated DFNB88. It separates disease-specific findings from supportive but non-DFNB88 ELMOD3 research.*

## 1. Disease information

### Definition and nomenclature

DFNB88 is an **autosomal recessive nonsyndromic hearing-loss disorder** in which hearing impairment is the primary recognized manifestation. “Nonsyndromic” means that no reproducible pattern of abnormalities in other organs has been established. Synonyms include:

- autosomal recessive nonsyndromic hearing loss 88;
- deafness, autosomal recessive 88;
- DFNB88;
- ELMOD3-related autosomal recessive hearing loss;
- ELMOD3-related nonsyndromic deafness.

The supplied identifier is **MONDO:0014182**. The foundational publication designates the locus **DFNB88**, mapped to chromosome **2p11.2**. Disease-specific OMIM, Orphanet, ICD, and MeSH identifiers were not independently recoverable from the searched full-text literature and should be verified directly against current releases before database ingestion. ICD-10/ICD-11 and MeSH generally classify the hearing-loss phenotype rather than this molecular subtype (jaworek2013analterationin pages 2-4).

The evidence is predominantly **aggregated disease-level literature derived from individually phenotyped members of one pedigree**, rather than EHR-scale or registry data. Open Targets did not return an ELMOD3–DFNB88-specific association in the retrieved results, illustrating incomplete coverage of ultra-rare subtypes; its returned associations concerned broader recessive hearing loss and other DFNB entities (OpenTargets Search: autosomal recessive nonsyndromic hearing loss 88).

### Foundational evidence and direct abstract quotation

Jaworek et al., published **5 September 2013** in *PLOS Genetics*, DOI [10.1371/journal.pgen.1003774](https://doi.org/10.1371/journal.pgen.1003774), PMID **24039609**, reported: **“Exome sequencing coupled with homozygosity mapping was used to identify a transition mutation (c.794T>C; p.Leu265Ser) in ELMOD3 at the DFNB88 locus that is associated with nonsyndromic deafness in a large Pakistani family, PKDF468.”** The same abstract states that affected relatives exhibited **“pre-lingual, severe-to-profound degrees of mixed hearing loss.”** (jaworek2013analterationin pages 1-2, liu2023generegulationanalysis pages 15-16)

## 2. Etiology

### Causal factor

The established cause is a **germline, homozygous missense variant in ELMOD3**, c.794T>C (p.Leu265Ser), affecting a highly conserved residue in the ELMO domain. The variant segregated with recessive hearing loss, was absent from 524 ancestry-matched control chromosomes, 1000 Genomes, and 6,500 NHLBI-ESP participants, and was predicted deleterious by multiple computational methods (jaworek2013analterationin pages 2-4, jaworek2013analterationin pages 4-6).

### Risk factors

- **Genetic:** two pathogenic ELMOD3 alleles are the primary risk requirement. For two heterozygous parents, the conventional recurrence probabilities are 25% affected, 50% carrier, and 25% inheriting neither familial allele per pregnancy.
- **Family history/consanguinity:** the original family was consanguineous. Consanguinity increases the probability that both parents carry the same rare ancestral allele, but is not mechanistically required for recessive disease. Pakistan has high consanguinity rates, facilitating homozygous recessive-disease discovery (shadab2024autosomalrecessivenon‐syndromic pages 1-2).
- **Sex:** no evidence of sex-dependent risk; autosomal inheritance predicts both sexes can be affected.
- **Environmental:** no exposure has been shown to cause DFNB88. Noise, congenital infection, and ototoxic medication can independently worsen hearing and should be treated as competing or additive causes, not DFNB88-specific etiologies. Contemporary review evidence identifies noise, TORCH infections, aminoglycosides, platinum agents, and other exposures as general hearing-loss risks (petit2023deafnessfromgenetic pages 1-5).

### Protective factors and gene–environment interaction

No DFNB88-specific protective allele, modifier gene, dietary factor, medication, or validated gene–environment interaction has been reported. Avoiding excessive noise and unnecessary ototoxic exposure is prudent for preserving residual hearing but has not been shown to prevent genetically initiated DFNB88. Modifier, epigenetic, and pharmacogenomic evidence is unavailable.

## 3. Phenotypes

| Phenotype | Characterization in documented humans | Suggested HPO term |
|---|---|---|
| Hearing impairment | Bilateral, prelingual, severe-to-profound mixed conductive and sensorineural hearing loss | **Hearing impairment** HP:0000365; **Prelingual sensorineural hearing impairment** HP:0000399; **Mixed hearing impairment** HP:0000410; **Profound hearing impairment** HP:0012715 |
| Conductive component | A substantial air–bone gap was documented in at least one individual; bone-conduction thresholds ranged from borderline normal to moderately severe by frequency/ear | **Conductive hearing impairment** HP:0000405 |
| Bilaterality | Both ears affected in the described audiogram/pedigree phenotype | **Bilateral hearing impairment** HP:0008619 |
| Vestibular function | No clear vestibular impairment documented | Consider recording absence of **Vertigo** HP:0002321 and **Abnormality of vestibular function** HP:0001751 rather than asserting universal absence |
| Extra-auditory findings | No clear skin, renal, or retinal abnormalities in the original assessment | Nonsyndromic classification; negative phenotypes should remain family-specific |

The original temporal-bone CT assessments showed intact semicircular and internal auditory canals and well-aerated middle ear/mastoid, apart from a slightly narrow right internal auditory canal in one person. Thus, the large conductive component was not explained by a consistent gross malformation in the available imaging (jaworek2013analterationin pages 1-2, jaworek2013analterationin pages 2-4).

### Frequency, progression, and quality of life

The hearing phenotype occurred in affected relatives of the linked pedigree, but exact numerator/denominator frequencies for each clinical feature were not available in the retrieved evidence. Human longitudinal progression was not adequately characterized. The prelingual severe-to-profound impairment predicts major risk to spontaneous speech and language acquisition, education, communication, and social participation unless identified and treated early. Contemporary experts note that profound congenital/prelingual loss, conventionally ≥90 dB HL, impedes spontaneous oral-language development; moderate-to-severe loss can also produce school difficulties (petit2023deafnessfromgenetic pages 1-5).

No DFNB88-specific EQ-5D, SF-36, PROMIS, speech-perception, educational, or caregiver-burden statistics have been published in the retrieved literature.

## 4. Genetic and molecular information

### Gene and locus

- **Gene:** ELMOD3, ELMO domain containing 3.
- **Location:** chromosome 2p11.2; DFNB88 linkage interval was approximately **0.91 Mb**, bounded by D2S1387 and D2S2232.
- **Linkage:** maximum two-point LOD score **4.74** at D2S2333 (jaworek2013analterationin pages 2-4).
- **Protein:** an ELMO-domain protein with GAP activity toward ARF-family small GTPases, especially ARL2 in the foundational assay.
- **Isoforms:** at least seven alternatively spliced human isoforms were reported; isoforms B–D encode the same 381-amino-acid protein containing the ELMO domain (jaworek2013analterationin pages 4-6).

HGNC and NCBI Gene numeric identifiers should be imported directly from HGNC/NCBI rather than inferred from literature excerpts.

### Pathogenic variant appraisal

**NM_001135022.2:c.794T>C, p.(Leu265Ser)** is the disease-defining DFNB88 variant. It is a germline missense substitution, homozygous in affected relatives and heterozygous in carriers. Evidence supporting pathogenicity includes phenotype segregation, linkage, extreme rarity in historical controls, conservation, computational predictions, abnormal subcellular association, and complete loss of recombinant ARL2-GAP activity (jaworek2013analterationin pages 2-4, jaworek2013analterationin pages 4-6).

The exact current ClinVar classification and current gnomAD allele frequency were not established from the retrieved documents and must be checked against live records. Historical absence is not equivalent to a contemporary population frequency of zero.

### Important allelic distinction

ELMOD3 also has **autosomal dominant** hearing-loss associations. The heterozygous variants c.512A>G (p.His171Arg) and c.640G>A (p.Gly214Ser) belong to dominant, generally progressive ELMOD3-related hearing-loss literature and should **not** be annotated as DFNB88 variants without biallelic recessive evidence (yun2025confirmatoryinsightsinto pages 3-7, yun2025confirmatoryinsightsinto pages 21-22, liu2023generegulationanalysis pages 1-2).

No validated DFNB88 modifier genes, protective variants, somatic variants, methylation signatures, repeat expansions, aneuploidies, translocations, or inversions are known. A homozygous 2p11.2 deletion involving ELMOD3 has been discussed elsewhere, but the retrieved evidence was insufficient for detailed pathogenic interpretation.

## 5. Environmental information

DFNB88 is genetic, not infectious, toxic, occupational, nutritional, or lifestyle-induced. No pathogen, smoking pattern, diet, exercise level, alcohol exposure, pollutant, or radiation exposure has been causally associated with the molecular subtype. General hearing-preservation measures remain appropriate because acquired injury could add to an inherited cochlear deficit. There is no zoonotic or communicable component.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic ELMOD3 c.794T>C causes p.Leu265Ser substitution in the ELMO domain.**
2. **p.Leu265Ser leads to impaired association of ELMOD3 with actin-rich cellular structures and abolishes measurable ARL2-GAP activity in vitro.**
3. **Loss of ELMOD3 GAP regulation is inferred to dysregulate ARL2/ARF-family GTPase cycling and associated membrane/cytoskeletal organization.**
4. **This dysregulation is inferred to impair development or maintenance of cochlear hair-cell F-actin networks and stereocilia; reduced F-actin and bundle pathology are demonstrated in Elmod3-null mice.**
5. **Stereocilia shortening/fusion and outer-hair-cell bundle degeneration lead to defective mechanotransduction and cochlear amplification; elevated DPOAE thresholds in null mice support the outer-hair-cell branch.**
6. **Hair-cell dysfunction results in sensorineural hearing loss.**
7. **Branch—conductive component:** affected humans also had conductive loss, but its connection to ELMOD3 is unresolved because imaging did not reveal a consistent middle-ear or temporal-bone lesion; coincident middle-ear physiology remains possible (jaworek2013analterationin pages 1-2, li2019elmod3knockoutleads pages 2-3, li2019elmod3knockoutleads pages 3-5, li2019elmod3knockoutleads pages 5-7).

### Molecular and cellular detail

ELMOD3 was prominent in rodent cochlear stereocilia and was also detected in kinocilia, cuticular plates, hair-cell bodies, and supporting cells. Tagged ELMOD3 colocalized with actin in MDCK cells and actin-based microvilli in LLC-PK1-CL4 epithelial cells. The key direct biochemical result was that recombinant wild-type ELMOD3 had ARL2-GAP activity whereas p.Leu265Ser abolished it (jaworek2013analterationin pages 1-2, jaworek2013analterationin pages 4-6).

Elmod3-null mice showed reduced cochlear ARL2 protein at postnatal day 7, one month, and five months. ARL2 was normally detected in inner and outer hair cells, spiral ganglion, and spiral ligament. Whether reduced ARL2 abundance is causal, compensatory, or downstream remains unresolved (li2019elmod3knockoutleads pages 5-7).

A separate cellular study found that deletion of ELMOD1 or ELMOD3 reduced primary-cilium formation, removed subsets of proteins from cilia, and accumulated some ciliary proteins at the Golgi, consistent with compromised Golgi-to-cilium trafficking. This supports broader ELMOD3 biology but has not been demonstrated as the proximate lesion in DFNB88 cochleae (liu2023generegulationanalysis pages 15-16).

### Suggested ontology annotations

- **GO biological process:** actin filament organization; regulation of actin cytoskeleton organization; stereocilium organization; sensory perception of sound; auditory receptor-cell development; small GTPase-mediated signal transduction; GTPase-activator activity; cilium assembly; regulation of membrane trafficking; potassium-ion transmembrane transport.
- **GO cellular component:** stereocilium; hair-cell stereocilium; actin cytoskeleton; cuticular plate; kinocilium; Golgi apparatus; cilium; plasma membrane.
- **Cell Ontology:** inner hair cell (**CL:0000589**); outer hair cell (**CL:0000601**); auditory hair cell; cochlear supporting cell; spiral ganglion neuron.

### Molecular profiling and 2023 development

Liu et al., published **14 September 2023**, DOI [10.1371/journal.pone.0288640](https://doi.org/10.1371/journal.pone.0288640), generated iPSCs carrying heterozygous dominant c.512A>G (p.His171Arg), an isogenic CRISPR-corrected line, and a sibling control. Mutant-versus-corrected analysis mapped **382 upregulated** and **361 downregulated** genes into protein-interaction networks. Twenty-six downregulated genes related to ion transmembrane transport and 16 to potassium transport; altered programs included cytoskeletal organization, sensory-organ/ear development, GPCR, PI3K–AKT, cAMP, calcium, ephrin, chloride transport, and cell adhesion. Examples included KCNB1, KCNC3, KCNH2, KCNK2, KCNN3, KCNN4, TBX1, and ATOH1 (liu2023generegulationanalysis pages 10-12).

This is **not DFNB88-specific evidence**: the variant and inheritance are dominant, undifferentiated iPSCs are not cochlear hair cells, and sibling comparisons were confounded by sex and other background-genome differences. It nevertheless provides a current experimental platform for studying ELMOD3-regulated networks (liu2023generegulationanalysis pages 1-2, liu2023generegulationanalysis pages 12-13).

No DFNB88-specific single-cell, spatial-transcriptomic, proteomic, metabolomic, lipidomic, or multi-omic dataset was identified.

## 7. Anatomical structures affected

- **Primary organ/system:** inner ear and auditory system.
- **Primary site:** cochlea, especially the organ of Corti.
- **Cells:** inner and outer sensory hair cells; supporting cells may also express ELMOD3. Spiral ganglion and spiral ligament show ARL2 expression, but direct primary injury there is unproven.
- **Subcellular structures:** stereociliary F-actin cores, cuticular plate, kinocilium/cilium, and potentially Golgi-to-cilium trafficking machinery.
- **Laterality:** bilateral in the documented human phenotype.
- **Vestibular labyrinth:** no clear clinical dysfunction despite vestibular expression; null mice also had normal observed vestibular behavior (jaworek2013analterationin pages 2-4, li2019elmod3knockoutleads pages 2-3).

Suggested anatomy terms include **UBERON:0001849 cochlea**, **UBERON:0002227 organ of Corti**, inner ear, spiral ganglion, spiral ligament, and auditory hair-cell stereocilium. Numeric UBERON identifiers other than those confidently known should be validated before production use.

## 8. Temporal development

The documented human onset is **prelingual**, implying congenital or early-childhood functional impairment, but newborn-versus-infant onset was not precisely resolved. The severity was already severe-to-profound when characterized. There are no adequate serial audiograms to determine whether DFNB88 is stable or progressive in humans (jaworek2013analterationin pages 1-2).

The mouse null phenotype differs temporally: ABR thresholds were normal at one month, became elevated at two months, and worsened through five months. Stereocilia formation appeared delayed at postnatal day 1; morphology was broadly similar at day 14; inner-hair-cell stereocilia were shortened at two months and markedly degenerated by five months (li2019elmod3knockoutleads pages 2-3, li2019elmod3knockoutleads pages 3-5).

The disease is expected to be lifelong. There is no evidence for episodic attacks, remission, spontaneous recovery, anticipation, or a formal staging system. The key intervention window is early childhood, before language deprivation becomes established; this is a rehabilitation principle rather than a DFNB88 natural-history result.

## 9. Inheritance and population

Inheritance is autosomal recessive. The original family’s segregation was consistent with affected homozygotes and unaffected carriers. Penetrance appeared high among identified homozygotes in that pedigree, but disease-wide penetrance cannot be quantified. Variable expressivity, germline mosaicism, anticipation, and sex bias have not been demonstrated (jaworek2013analterationin pages 2-4).

No disease-specific prevalence, incidence, carrier frequency, founder age, or geographic distribution has been measured. A 2024 Pakistani review reported **51** ARNSHL genes in that population; 13 common genes accounted for more than half of profound cases, while each remaining gene category contributed **<2%**. This supports ELMOD3’s rarity but is not a DFNB88 prevalence estimate. The same review noted approximately **14.5 million** Pakistanis living with hearing loss, about half presumed genetic, but these figures encompass all hearing loss (shadab2024autosomalrecessivenon‐syndromic pages 1-2).

The apparent Pakistani concentration may reflect consanguinity and ascertainment through gene-mapping programs rather than population specificity. Both sexes should be equally susceptible. No validated founder effect or current carrier rate for p.Leu265Ser is available.

## 10. Diagnostics

### Clinical evaluation

1. Confirm hearing impairment with age-appropriate behavioral audiometry or ABR.
2. Determine type and severity using air- and bone-conduction thresholds, tympanometry, acoustic reflexes, and otoscopy.
3. Assess outer-hair-cell function using otoacoustic emissions where informative.
4. Evaluate speech detection/perception and functional communication.
5. Because mixed loss was reported, independently investigate middle-ear disease; do not assume every conductive component is caused by ELMOD3.
6. Consider temporal-bone CT/MRI when conductive loss, congenital malformation, cochlear implantation, or asymmetric findings warrant it.
7. Screen clinically for syndromic clues, congenital infection, ototoxic exposure, and common alternative genetic causes.

No blood chemistry, enzyme assay, biopsy, circulating biomarker, or pathology specimen is diagnostic.

### Genetic testing

A comprehensive hearing-loss panel including **ELMOD3**, sequence variants, and copy-number analysis is efficient because inherited hearing loss is highly heterogeneous. If nondiagnostic, trio/family **WES or WGS** can detect rare coding variants, CNVs, and—particularly with WGS—noncoding or structural lesions. Familial segregation is essential. Single-gene testing is reasonable when the familial ELMOD3 variant is already known. CMA may detect large deletions but is insensitive to the known missense variant; conventional karyotyping and FISH are not first-line. Mitochondrial and repeat-expansion testing should be phenotype- or ancestry-driven rather than routine DFNB88 tests.

Molecular diagnosis requires **biallelic pathogenic/likely pathogenic ELMOD3 variants in trans** plus a compatible phenotype. A single heterozygous ELMOD3 variant does not establish DFNB88 and may instead raise dominant ELMOD3 disease or carrier status. Current ACMG/AMP classification should use live ClinVar/gnomAD data, segregation, and functional evidence.

### Differential diagnosis and screening

Differentials include GJB2-, SLC26A4-, OTOF-, TMC1-, MYO15A-, CDH23-, and other recessive nonsyndromic hearing losses; congenital CMV; structural middle-ear disease; auditory neuropathy; and syndromic deafness. Universal newborn hearing screening detects hearing loss but not etiology. Once a familial variant is established, cascade carrier testing, testing of affected relatives, prenatal diagnosis, and preimplantation genetic testing are technically possible with counseling.

## 11. Outcome and prognosis

DFNB88 is not known to reduce life expectancy or cause disease-specific mortality. Survival statistics are therefore not applicable. The principal morbidity is communication disability, including impaired spoken-language development, educational difficulty, reduced social participation, and dependence on hearing rehabilitation. Severity at diagnosis, age at amplification or implantation, residual hearing, auditory-nerve integrity, consistency of device use, and access to speech-language/educational services are likely major functional prognostic factors, although none has been quantified specifically for DFNB88.

Recovery of native hearing without intervention has not been reported. Hearing aids and cochlear implants can improve access to sound, but no DFNB88-specific response rate, speech outcome, adverse-event rate, or prognostic biomarker is available. The reported absence of systemic disease suggests normal general medical prognosis, subject to the limited number of characterized families.

## 12. Treatment

### Current clinical management

There is no approved DFNB88-specific pharmacotherapy. Management follows severity- and anatomy-based hearing-loss care:

- hearing aids when useful residual hearing and the conductive/sensorineural profile permit;
- cochlear-implant evaluation for bilateral severe-to-profound loss with insufficient aided speech access;
- management of any independent middle-ear disorder;
- speech-language therapy, auditory habilitation, sign-language access according to family preference, educational accommodation, and assistive listening technology;
- serial audiology and device optimization;
- genetic counseling.

Suggested NCIt concepts include **Hearing Aid Device**, **Cochlear Implant**, **Cochlear Implantation**, **Speech Therapy**, **Auditory Rehabilitation**, and **Genetic Counseling**; identifiers should be resolved in the current NCIt release.

### Experimental treatment and recent developments

No ELMOD3/DFNB88-specific gene replacement, editing, RNA therapy, cell therapy, or interventional trial was identified. The 2024 AAV review states: **“Clinical treatment options are currently limited to external devices like hearing aids and cochlear implants.”** It reports hearing restoration in **>20 genetic deafness mouse models** and early clinical efficacy for OTOF/DFNB9, but those achievements do not establish efficacy for ELMOD3 disease (zhang2024aav‐mediatedgenetherapy pages 1-2).

ELMOD3 is conceptually amenable to gene augmentation because recessive p.Leu265Ser behaves as loss of biochemical function and cochlear hair cells are the likely target. Major unresolved issues include vector tropism for inner and outer hair cells, dose, expression control, therapeutic timing before irreversible bundle degeneration, durability, immunogenicity, and whether the human conductive component would respond. No treatment-response or adverse-event statistics exist for DFNB88.

## 13. Prevention

Primary prevention of a de novo molecular lesion through lifestyle measures is impossible. Reproductive risk can be reduced—not eliminated at the population level—through informed carrier testing, cascade testing, prenatal diagnosis, or preimplantation genetic testing after identification of familial variants. Genetic counseling should emphasize autosomal-recessive recurrence risk and preserve reproductive autonomy.

Secondary prevention comprises newborn hearing screening, prompt diagnostic audiology, early molecular diagnosis, and early communication intervention. Tertiary prevention includes optimized amplification/implantation, educational support, avoidance of harmful noise, and careful use or monitoring of ototoxic drugs. Vaccination and infection prevention reduce acquired hearing loss but do not prevent ELMOD3 mutations. No prophylactic medication exists.

## 14. Other species and natural disease

No naturally occurring veterinary disease conclusively equivalent to human ELMOD3-DFNB88 was identified. ELMOD3 is evolutionarily conserved, and orthologous biology can be studied in mammals. Relevant taxonomy includes *Homo sapiens* (**NCBI Taxon 9606**) and *Mus musculus* (**10090**). No breed-specific VBO annotation, zoonotic transmission, or cross-species infectious susceptibility applies.

Related ELMOD-family phenotypes in mice support conservation of small-GTPase/actin regulation in sensory hair bundles, but ELMOD1 disease should not be conflated with ELMOD3 deficiency.

## 15. Model organisms

### Mouse model

Li et al., *Human Molecular Genetics*, advance publication **19 October 2019**, DOI [10.1093/hmg/ddz240](https://doi.org/10.1093/hmg/ddz240), generated a C57BL/6 **Elmod3−/−** line by CRISPR/Cas9. A 277-bp deletion targeting exon 6 produced a frameshift and premature stop at residue 149; cochlear ELMOD3 protein was absent. Genotypes approximated a 1:2:1 Mendelian ratio without sex bias (li2019elmod3knockoutleads pages 1-2, li2019elmod3knockoutleads pages 2-3).

At one month, mutants and wild types had similar ABR and DPOAE thresholds. At two months, mutants showed significant ABR threshold shifts, particularly at 4, 8, and 16 kHz (**P<0.001**), and elevated DPOAE thresholds at 8, 12, 16, and 24 kHz (**P<0.05**). At five months, ABR differences remained prominent at 8 and 16 kHz (**P<0.001**) and DPOAE differences extended across tested frequencies (**P<0.01**). At least five animals per genotype were used in each age group for physiological testing (li2019elmod3knockoutleads pages 2-3, li2019elmod3knockoutleads pages 7-8).

Histology and microscopy showed reduced F-actin, delayed neonatal bundle maturation, inner-hair-cell stereocilia shortening at two months, marked inner-hair-cell bundle degeneration and looser/missing outer-hair-cell stereocilia at five months, while most hair-cell bodies remained present. Vestibular dysfunction was not observed (li2019elmod3knockoutleads pages 2-3, li2019elmod3knockoutleads pages 3-5).

**Strengths:** genetically controlled in-vivo system; age series; ABR, DPOAE, histology, immunostaining, and SEM converge on cochlear hair-cell dysfunction. **Limitations:** mouse disease was moderate and postnatal-progressive rather than prelingual severe-to-profound; only homozygous mice had measurable loss; C57BL/6 background can complicate aging-hearing studies; sample sizes for SEM were limited; and a null allele is not identical to human p.Leu265Ser (li2019elmod3knockoutleads pages 3-5, li2019elmod3knockoutleads pages 5-7, li2019elmod3knockoutleads pages 7-8).

### Cellular models

MDCK and LLC-PK1-CL4 epithelial cells established ELMOD3 association with actin-rich structures and the localization defect of p.Leu265Ser. Recombinant-protein assays established loss of ARL2-GAP activity. Patient-derived iPSCs and their CRISPR-corrected isogenic control are available for dominant p.His171Arg biology, but a DFNB88 p.Leu265Ser iPSC-derived hair-cell or cochlear-organoid model was not identified (jaworek2013analterationin pages 1-2, liu2023generegulationanalysis pages 1-2, liu2023generegulationanalysis pages 10-12).

## Evidence gaps and expert interpretation

The central limitation is that DFNB88 remains a **one-pedigree, one-clearly established recessive missense-variant disorder** in the retrieved human literature. Accordingly, assertions of universal progression, complete penetrance, a characteristic conductive mechanism, population prevalence, variant-specific cochlear-implant outcomes, or systemic absence would overstate the evidence. The most defensible knowledge-base representation is: high confidence in the ELMOD3–hearing-loss relationship and p.Leu265Ser functional impairment; moderate confidence in stereocilia/actin–ARL2 pathophysiology; and low confidence in disease-wide frequencies and natural history.

The 2023–2024 literature materially advanced hereditary-deafness therapeutics and ELMOD3 experimental systems, but did not deliver a DFNB88-specific therapy or broader recessive clinical cohort. Expert reviews characterize monogenic inner-ear gene therapy as promising while emphasizing cell-type-specific delivery, safety, durability, and timing challenges. They also continue to regard hearing aids and cochlear implants as the available corrective options (petit2023deafnessfromgenetic pages 1-5, zhang2024aav‐mediatedgenetherapy pages 1-2).

References

1. (jaworek2013analterationin pages 1-2): Thomas J. Jaworek, Elodie M. Richard, Anna A. Ivanova, Arnaud P. J. Giese, Daniel I. Choo, Shaheen N. Khan, Sheikh Riazuddin, Richard A. Kahn, and Saima Riazuddin. An alteration in elmod3, an arl2 gtpase-activating protein, is associated with hearing impairment in humans. Sep 2013. URL: https://doi.org/10.1371/journal.pgen.1003774, doi:10.1371/journal.pgen.1003774. This article has 60 citations and is from a domain leading peer-reviewed journal.

2. (jaworek2013analterationin pages 2-4): Thomas J. Jaworek, Elodie M. Richard, Anna A. Ivanova, Arnaud P. J. Giese, Daniel I. Choo, Shaheen N. Khan, Sheikh Riazuddin, Richard A. Kahn, and Saima Riazuddin. An alteration in elmod3, an arl2 gtpase-activating protein, is associated with hearing impairment in humans. Sep 2013. URL: https://doi.org/10.1371/journal.pgen.1003774, doi:10.1371/journal.pgen.1003774. This article has 60 citations and is from a domain leading peer-reviewed journal.

3. (jaworek2013analterationin pages 4-6): Thomas J. Jaworek, Elodie M. Richard, Anna A. Ivanova, Arnaud P. J. Giese, Daniel I. Choo, Shaheen N. Khan, Sheikh Riazuddin, Richard A. Kahn, and Saima Riazuddin. An alteration in elmod3, an arl2 gtpase-activating protein, is associated with hearing impairment in humans. Sep 2013. URL: https://doi.org/10.1371/journal.pgen.1003774, doi:10.1371/journal.pgen.1003774. This article has 60 citations and is from a domain leading peer-reviewed journal.

4. (li2019elmod3knockoutleads pages 1-2): Wu Li, Yong Feng, Anhai Chen, Taoxi Li, Sida Huang, Jing Liu, Xianlin Liu, Yalan Liu, Jiangang Gao, Denise Yan, Jie Sun, Lingyun Mei, Xuezhong Liu, and Jie Ling. Elmod3 knockout leads to progressive hearing loss and abnormalities in cochlear hair cell stereocilia. Human molecular genetics, 28:4103-4112, Oct 2019. URL: https://doi.org/10.1093/hmg/ddz240, doi:10.1093/hmg/ddz240. This article has 18 citations and is from a domain leading peer-reviewed journal.

5. (li2019elmod3knockoutleads pages 2-3): Wu Li, Yong Feng, Anhai Chen, Taoxi Li, Sida Huang, Jing Liu, Xianlin Liu, Yalan Liu, Jiangang Gao, Denise Yan, Jie Sun, Lingyun Mei, Xuezhong Liu, and Jie Ling. Elmod3 knockout leads to progressive hearing loss and abnormalities in cochlear hair cell stereocilia. Human molecular genetics, 28:4103-4112, Oct 2019. URL: https://doi.org/10.1093/hmg/ddz240, doi:10.1093/hmg/ddz240. This article has 18 citations and is from a domain leading peer-reviewed journal.

6. (li2019elmod3knockoutleads pages 3-5): Wu Li, Yong Feng, Anhai Chen, Taoxi Li, Sida Huang, Jing Liu, Xianlin Liu, Yalan Liu, Jiangang Gao, Denise Yan, Jie Sun, Lingyun Mei, Xuezhong Liu, and Jie Ling. Elmod3 knockout leads to progressive hearing loss and abnormalities in cochlear hair cell stereocilia. Human molecular genetics, 28:4103-4112, Oct 2019. URL: https://doi.org/10.1093/hmg/ddz240, doi:10.1093/hmg/ddz240. This article has 18 citations and is from a domain leading peer-reviewed journal.

7. (liu2023generegulationanalysis pages 15-16): Xianling Liu, Jie Wen, Xuezhong Liu, Anhai Chen, Sijun Li, Jing Liu, Jie Sun, Wei Gong, Xiaoming Kang, Zhili Feng, Chu-Feng He, Ling-Yun Mei, J. Ling, and Yong Feng. Gene regulation analysis of patient-derived ipscs and its crispr-corrected control provides a new tool for studying perturbations of elmod3 c.512a>g mutation during the development of inherited hearing loss. PLOS ONE, Sep 2023. URL: https://doi.org/10.1371/journal.pone.0288640, doi:10.1371/journal.pone.0288640. This article has 5 citations and is from a peer-reviewed journal.

8. (li2019elmod3knockoutleads pages 5-7): Wu Li, Yong Feng, Anhai Chen, Taoxi Li, Sida Huang, Jing Liu, Xianlin Liu, Yalan Liu, Jiangang Gao, Denise Yan, Jie Sun, Lingyun Mei, Xuezhong Liu, and Jie Ling. Elmod3 knockout leads to progressive hearing loss and abnormalities in cochlear hair cell stereocilia. Human molecular genetics, 28:4103-4112, Oct 2019. URL: https://doi.org/10.1093/hmg/ddz240, doi:10.1093/hmg/ddz240. This article has 18 citations and is from a domain leading peer-reviewed journal.

9. (liu2023generegulationanalysis pages 1-2): Xianling Liu, Jie Wen, Xuezhong Liu, Anhai Chen, Sijun Li, Jing Liu, Jie Sun, Wei Gong, Xiaoming Kang, Zhili Feng, Chu-Feng He, Ling-Yun Mei, J. Ling, and Yong Feng. Gene regulation analysis of patient-derived ipscs and its crispr-corrected control provides a new tool for studying perturbations of elmod3 c.512a>g mutation during the development of inherited hearing loss. PLOS ONE, Sep 2023. URL: https://doi.org/10.1371/journal.pone.0288640, doi:10.1371/journal.pone.0288640. This article has 5 citations and is from a peer-reviewed journal.

10. (liu2023generegulationanalysis pages 10-12): Xianling Liu, Jie Wen, Xuezhong Liu, Anhai Chen, Sijun Li, Jing Liu, Jie Sun, Wei Gong, Xiaoming Kang, Zhili Feng, Chu-Feng He, Ling-Yun Mei, J. Ling, and Yong Feng. Gene regulation analysis of patient-derived ipscs and its crispr-corrected control provides a new tool for studying perturbations of elmod3 c.512a>g mutation during the development of inherited hearing loss. PLOS ONE, Sep 2023. URL: https://doi.org/10.1371/journal.pone.0288640, doi:10.1371/journal.pone.0288640. This article has 5 citations and is from a peer-reviewed journal.

11. (shadab2024autosomalrecessivenon‐syndromic pages 1-2): Madiha Shadab, Ansar Ahmed Abbasi, Ahsan Ejaz, Afif Ben‐Mahmoud, Vijay Gupta, Hyung‐Goo Kim, and Barbara Vona. Autosomal recessive non‐syndromic hearing loss genes in pakistan during the previous three decades. Journal of Cellular and Molecular Medicine, Mar 2024. URL: https://doi.org/10.1111/jcmm.18119, doi:10.1111/jcmm.18119. This article has 10 citations and is from a peer-reviewed journal.

12. (petit2023deafnessfromgenetic pages 1-5): Christine Petit, Crystel Bonnet, and Saaïd Safieddine. Deafness: from genetic architecture to gene therapy. Nature Reviews Genetics, 24:665-686, May 2023. URL: https://doi.org/10.1038/s41576-023-00597-7, doi:10.1038/s41576-023-00597-7. This article has 122 citations and is from a domain leading peer-reviewed journal.

13. (zhang2024aav‐mediatedgenetherapy pages 1-2): Liyan Zhang, Fangzhi Tan, Jieyu Qi, Yicheng Lu, Xiaohan Wang, Xuehan Yang, Xiangyan Chen, Xinru Zhang, Jinyi Fan, Yinyi Zhou, Li Peng, Nianci Li, Lei Xu, Shiming Yang, and Renjie Chai. Aav‐mediated gene therapy for hereditary deafness: progress and perspectives. Advanced Science, Nov 2024. URL: https://doi.org/10.1002/advs.202402166, doi:10.1002/advs.202402166. This article has 43 citations and is from a peer-reviewed journal.

14. (OpenTargets Search: autosomal recessive nonsyndromic hearing loss 88): Open Targets Query (autosomal recessive nonsyndromic hearing loss 88, 23 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

15. (yun2025confirmatoryinsightsinto pages 3-7): Yejin Yun, Minjae Park, Sohyang Jeong, Sung Ho Jung, and Sang-Yeon Lee. Confirmatory insights into elmod3-associated autosomal dominant non-syndromic hearing loss. MedRxiv, Feb 2025. URL: https://doi.org/10.1101/2025.02.11.25321773, doi:10.1101/2025.02.11.25321773. This article has 0 citations.

16. (yun2025confirmatoryinsightsinto pages 21-22): Yejin Yun, Minjae Park, Sohyang Jeong, Sung Ho Jung, and Sang-Yeon Lee. Confirmatory insights into elmod3-associated autosomal dominant non-syndromic hearing loss. MedRxiv, Feb 2025. URL: https://doi.org/10.1101/2025.02.11.25321773, doi:10.1101/2025.02.11.25321773. This article has 0 citations.

17. (liu2023generegulationanalysis pages 12-13): Xianling Liu, Jie Wen, Xuezhong Liu, Anhai Chen, Sijun Li, Jing Liu, Jie Sun, Wei Gong, Xiaoming Kang, Zhili Feng, Chu-Feng He, Ling-Yun Mei, J. Ling, and Yong Feng. Gene regulation analysis of patient-derived ipscs and its crispr-corrected control provides a new tool for studying perturbations of elmod3 c.512a>g mutation during the development of inherited hearing loss. PLOS ONE, Sep 2023. URL: https://doi.org/10.1371/journal.pone.0288640, doi:10.1371/journal.pone.0288640. This article has 5 citations and is from a peer-reviewed journal.

18. (li2019elmod3knockoutleads pages 7-8): Wu Li, Yong Feng, Anhai Chen, Taoxi Li, Sida Huang, Jing Liu, Xianlin Liu, Yalan Liu, Jiangang Gao, Denise Yan, Jie Sun, Lingyun Mei, Xuezhong Liu, and Jie Ling. Elmod3 knockout leads to progressive hearing loss and abnormalities in cochlear hair cell stereocilia. Human molecular genetics, 28:4103-4112, Oct 2019. URL: https://doi.org/10.1093/hmg/ddz240, doi:10.1093/hmg/ddz240. This article has 18 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Autosomal_Recessive_Nonsyndromic_Hearing_Loss_88-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 7 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 7 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014182` (2 mentions) - the report calls it "if available"; MONDO calls it **autosomal recessive nonsyndromic hearing loss 88**
