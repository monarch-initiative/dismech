---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-05T17:15:43.183901'
end_time: '2026-09-05T17:23:56.518815'
duration_seconds: 493.33
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Kasabach-Merritt Syndrome
  mondo_id: MONDO:0007708
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 20
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
  total_terms: 28
  verified: 28
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0007708
    reported_labels:
    - if available
    ontology_label: Kasabach-Merritt syndrome
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Kasabach-Merritt_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Kasabach-Merritt Syndrome
- **MONDO ID:** MONDO:0007708 (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Kasabach-Merritt Syndrome** covering all of the
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
- **Disease Name:** Kasabach-Merritt Syndrome
- **MONDO ID:** MONDO:0007708 (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Kasabach-Merritt Syndrome** covering all of the
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


# Kasabach–Merritt Syndrome/Phenomenon: Disease Characteristics Report

**Scope and terminology.** The preferred modern term is **Kasabach–Merritt phenomenon (KMP)** rather than “Kasabach–Merritt syndrome” (KMS). KMP is not an independent inherited disease: it is a severe platelet-consuming coagulopathy arising almost exclusively in **kaposiform hemangioendothelioma (KHE)** and, less often, **tufted angioma (TA)**. It should not be attributed to ordinary infantile hemangioma. Evidence below is aggregated disease-level literature and trial data, not individual EHR records, except where explicitly identified as a case or case series. The strongest recent source retrieved was a 70-patient 2024 retrospective cohort; much management evidence nevertheless remains observational or expert consensus because the disorder is exceptionally rare. (li2024treatmentexperiencefor pages 1-2, ji2020kaposiformhemangioendotheliomacurrent pages 1-2)

## 1. Disease information

KMP comprises profound thrombocytopenia caused by intralesional platelet trapping, with consumptive coagulopathy, hypofibrinogenemia, elevated D-dimer and, frequently, microangiopathic or hemorrhagic anemia. The underlying KHE is a rare, locally aggressive vascular neoplasm with combined blood-vascular and lymphatic endothelial differentiation but no usual distant metastasis. TA and KHE are regarded as a clinicopathologic spectrum, with TA generally more superficial and less aggressive. (gasparella2025thevascernvascadiagnostic pages 2-6, ji2020kaposiformhemangioendotheliomacurrent pages 1-2, NCT03188068 chunk 1)

**Identifiers and synonyms**

- **MONDO:** MONDO:0007708, *Kasabach–Merritt syndrome* (user-supplied identifier; current clinical terminology favors KMP).
- **MeSH:** D059885, *Kasabach-Merritt Syndrome*, confirmed in ClinicalTrials.gov indexing. (NCT04077515 chunk 1)
- **Synonyms:** Kasabach–Merritt phenomenon, Kasabach–Merritt syndrome, KMP, KMS, Kasabach–Merritt coagulopathy, thrombocytopenic coagulopathy associated with KHE/TA.
- **OMIM/Orphanet:** no verified syndrome-specific number was established from the retrieved evidence; KMP is better modeled as a complication/phenotype of KHE or TA rather than a Mendelian disease.
- **ICD-10/ICD-11:** no uniquely verified KMP code was identified. Coding generally requires the vascular tumor plus thrombocytopenia/coagulopathy codes; local coding authority should be consulted.

The ontology-ready synopsis is:

| Domain | Core finding | Quantitative/current evidence | Suggested ontology terms |
|---|---|---|---|
| Definition | Kasabach–Merritt phenomenon (KMP; historically “Kasabach–Merritt syndrome”) is a tumor-associated consumptive coagulopathy arising with kaposiform hemangioendothelioma (KHE) or tufted angioma (TA), not infantile or congenital hemangioma. | KMP occurs in an estimated 42–71% of KHE; a 2024 KHE cohort found KMP in 55/70 (78%). (ji2020kaposiformhemangioendotheliomacurrent pages 1-2, li2024treatmentexperiencefor pages 1-2, ji2020kaposiformhemangioendotheliomacurrent pages 5-6) | MONDO:0007708 Kasabach–Merritt syndrome; MeSH D059885 Kasabach-Merritt Syndrome; candidate: kaposiform hemangioendothelioma; candidate: tufted angioma |
| Hematologic phenotype | Profound thrombocytopenia from intralesional platelet trapping, consumptive coagulopathy, hypofibrinogenemia, elevated D-dimer, and sometimes severe anemia from sequestration or intralesional hemorrhage. | Median initial platelet count reported as 21 × 10⁹/L; in the 2024 cohort, median KMP platelet count was 24,000/µL and thrombocytopenia began at median age 27.8 days. Clinically significant severe KMP is generally associated with platelets below 30 × 10⁹/L. (li2024treatmentexperiencefor pages 1-2, ji2020kaposiformhemangioendotheliomacurrent pages 5-6, NCT03188068 chunk 1) | HP:0001873 Thrombocytopenia; HP:0011890 Prolonged bleeding time; HP:0001892 Abnormal bleeding; HP:0001903 Anemia; HP:0011900 Hypofibrinogenemia; candidate: elevated D-dimer; candidate: consumptive coagulopathy |
| Lesion phenotype and anatomy | The KHE lesion is typically an enlarging, infiltrative, indurated blue-purple or purpuric mass that becomes warm, swollen, and painful during KMP; deep lesions may lack skin findings. Musculoskeletal infiltration can cause restricted motion, contracture, bone erosion, and chronic pain. | In a 2024 cohort, 89% had a locally aggressive blue-purple cutaneous mass and 20% had pain or joint dysfunction; sites were lower extremity 35%, trunk 29%, head/neck 24%, and upper extremity 10%. Approximately 12% may lack cutaneous involvement. (li2024treatmentexperiencefor pages 1-2, ji2020kaposiformhemangioendotheliomacurrent pages 5-6, ji2020kaposiformhemangioendotheliomacurrent pages 6-8) | HP:0000969 Edema; HP:0000978 Bruising susceptibility; HP:0002829 Arthralgia; HP:0001376 Limitation of joint mobility; HP:0002653 Bone pain; candidate: painful vascular tumor; UBERON:0002101 limb; UBERON:0002102 forelimb; UBERON:0002103 hindlimb; UBERON:0000479 tissue |
| Mechanism | Dysregulated angiogenesis and lymphangiogenesis form abnormal podoplanin-positive vascular channels. Platelet CLEC-2 engagement by podoplanin and, inferentially, endothelial injury plus high shear/von-Willebrand-factor signaling activate and aggregate platelets. This leads to coagulation-cascade activation, consumption of platelets and clotting factors, intralesional thrombosis/hemorrhage, and clinical KMP. | Histologic platelet trapping occurs in KHE with and without KMP. VEGF-C/VEGFR3 and Ang-2/Tie-2 signaling can activate PI3K–AKT–mTOR; elevated Ang-2 falls with sirolimus, but its causal role in KMP remains unproven. (ji2020kaposiformhemangioendotheliomacurrent pages 5-6, ji2020kaposiformhemangioendotheliomacurrent pages 2-5) | GO:0001525 angiogenesis; GO:0001946 lymphangiogenesis; GO:0030168 platelet activation; GO:0070527 platelet aggregation; GO:0007596 blood coagulation; GO:0001934 positive regulation of protein phosphorylation; CL:0000115 endothelial cell; CL:0000233 platelet; candidate: lymphatic endothelial cell |
| Diagnostics | Diagnosis integrates lesion behavior, CBC/coagulation studies, Doppler ultrasound, contrast MRI, and—when safe—histopathology. MRI commonly shows an ill-defined, infiltrative, T1-isointense and T2-hyperintense, diffusely enhancing lesion with multiplanar involvement and fat stranding. Biopsy may worsen severe coagulopathy. | Initial laboratory evaluation includes platelet count, fibrinogen, and D-dimer. Histology shows infiltrative spindle-endothelial nodules, slit-like channels, platelet thrombi, and hemosiderin; immunophenotype is CD31/CD34/VEGFR3/D2-40/LYVE1/PROX1 positive and GLUT1/HHV8 negative. (gasparella2025thevascernvascadiagnostic pages 2-6, ji2020kaposiformhemangioendotheliomacurrent pages 6-8, ji2020kaposiformhemangioendotheliomacurrent pages 8-10) | HP:0001873 Thrombocytopenia; HP:0011900 Hypofibrinogenemia; NCIT candidate: Complete Blood Count; NCIT candidate: Coagulation Study; NCIT candidate: Doppler Ultrasound; NCIT candidate: Magnetic Resonance Imaging; NCIT candidate: Biopsy; CL:0000115 endothelial cell |
| Treatment | Severe KMP generally requires urgent multidisciplinary treatment of the tumor and coagulopathy. Contemporary practice favors systemic sirolimus plus a short corticosteroid course; vincristine is an alternative/add-on for inadequate response or compression. Completely resectable localized disease may be cured surgically, but active extensive KMP makes surgery hazardous. Platelets are reserved for active bleeding or procedures. | Common sirolimus initiation is 0.8 mg/m² twice daily with trough 8–15 ng/mL; lower maintenance targets are being studied. Historical response estimates are 94% for sirolimus after prior-treatment failure, 72% for vincristine, and 10–27% for corticosteroid monotherapy. A 2024 surgical cohort reported corticosteroid sensitivity in 36–58%, depending on analysis. (li2024treatmentexperiencefor pages 5-7, NCT03188068 chunk 1, ji2020kaposiformhemangioendotheliomacurrent pages 8-10, ji2020kaposiformhemangioendotheliomacurrent pages 10-12) | NCIT:C1212 Sirolimus; NCIT:C769 Prednisolone; NCIT:C933 Vincristine; NCIT candidate: Surgical Resection; NCIT candidate: Embolization; NCIT candidate: Platelet Transfusion; NCIT candidate: Cryoprecipitate Transfusion |
| Prognosis and evidence gaps | Untreated or refractory KMP can cause fatal hemorrhage, hemodynamic instability, vital-structure compression, and organ injury. Survivors may have fibrosis, lymphedema, chronic pain, contractures, impaired mobility, or recurrence. No validated KMP-specific prognostic score, germline inheritance model, preventive intervention, or routine molecular diagnostic test is established. | Historical KHE/KMP mortality has been reported as high as 20–30%. In the 2024 cohort, six patients recurred and two died after discharge; two stopped sirolimus because of severe pneumonia. Prospective evidence remains constrained by rarity: a randomized vincristine-versus-sirolimus trial terminated after enrolling only four participants. (li2024treatmentexperiencefor pages 1-2, li2024treatmentexperiencefor pages 5-7, NCT02110069 chunk 1, ji2020kaposiformhemangioendotheliomacurrent pages 6-8) | HP:0002721 Immunodeficiency—candidate only for treatment-related susceptibility; HP:0001004 Lymphedema; HP:0001376 Limitation of joint mobility; candidate: chronic pain; candidate: recurrent disease; candidate: treatment-related infection |


*Table: Compact disease-knowledge-base summary distinguishing KMP from its underlying vascular tumors and mapping established clinical, mechanistic, diagnostic, treatment, and prognostic findings to candidate ontology terms.*

## 2. Etiology, risk and protective factors

### Causal factors

The immediate cause is an abnormal KHE/TA vascular bed that traps and activates platelets. The initiating cause of most KHE remains unknown. Almost all cases are sporadic, without a recognized germline, infectious, toxic, dietary or lifestyle cause. Somatic mosaic signaling variants are plausible tumor initiators, but none is necessary or sufficient to diagnose KMP. (ji2020kaposiformhemangioendotheliomacurrent pages 2-5, ji2020kaposiformhemangioendotheliomacurrent pages 1-2)

### Risk factors

Established clinical correlates include congenital presentation, young age, large tumor—particularly **>8 cm**—deep infiltration, and intrathoracic or retroperitoneal location. Tumor size, depth, location and associated hematologic abnormalities also predict complications. Trauma, surgery, infection and post-vaccination inflammation have preceded lesion enlargement or KMP in case reports; these are possible **triggers of an existing lesion**, not proven primary causes, and routine vaccination itself should not be characterized as causal. Adult KMP is exceptional and has sometimes followed trauma or pregnancy. (ji2020kaposiformhemangioendotheliomacurrent pages 2-5, ji2020kaposiformhemangioendotheliomacurrent pages 5-6)

No reproducible sex, ethnicity, family-history, occupational or lifestyle risk has been established. A 2024 cohort showed only slight male predominance, 38 boys versus 32 girls. (li2024treatmentexperiencefor pages 1-2)

### Protective factors and gene–environment interaction

No validated protective allele, diet, lifestyle measure or prophylactic drug is known. The proposed gene–environment model is that a somatic vascular-tumor clone creates susceptibility, while tissue injury or inflammation may increase endothelial activation, blood flow and platelet consumption. This interaction is biologically plausible but has not been demonstrated prospectively. (ji2020kaposiformhemangioendotheliomacurrent pages 2-5)

## 3. Phenotypes

- **Severe thrombocytopenia:** usually neonatal/infantile, acute or rapidly progressive during tumor activation; median initial platelet count reported as **21 ×10⁹/L**, and **24 ×10³/µL** in the 2024 cohort. Severe KMP is commonly defined by platelets below 30 ×10⁹/L. Suggested HPO: **HP:0001873**. (li2024treatmentexperiencefor pages 1-2, ji2020kaposiformhemangioendotheliomacurrent pages 5-6, NCT03188068 chunk 1)
- **Consumptive coagulopathy:** low fibrinogen, elevated D-dimer/FDP and continued clotting-factor consumption; severe and fluctuating with tumor activity. Suggested HPO: hypofibrinogenemia (**HP:0011900**), abnormal coagulation profile.
- **Anemia and bleeding:** blood sequestration, intralesional hemorrhage and possible microangiopathic hemolysis produce pallor, ecchymoses, petechiae or clinically important bleeding. Suggested HPO: anemia (**HP:0001903**), abnormal bleeding (**HP:0001892**), bruising susceptibility (**HP:0000978**). (li2019localsutureligationassisted pages 1-2, NCT03188068 chunk 1)
- **Tumor findings:** an enlarging, indurated blue-purple/purpuric mass that becomes warm, swollen and intensely painful. Deep KHE may have no skin finding—approximately 12% in one synthesis. Suggested HPO: edema (**HP:0000969**), pain, vascular skin lesion. (ji2020kaposiformhemangioendotheliomacurrent pages 5-6)
- **Functional phenotypes:** restricted range of motion, muscular atrophy, fibrosis, flexion contracture, joint subluxation, bone erosion, scoliosis and chronic pain. Suggested HPO: limitation of joint mobility (**HP:0001376**), scoliosis, bone pain, muscle atrophy. In the 2024 cohort, pain or joint dysfunction occurred in 20%. (li2024treatmentexperiencefor pages 1-2, ji2020kaposiformhemangioendotheliomacurrent pages 6-8)
- **Lymphatic/vital-organ effects:** chronic lymphedema, airway compromise, pleural complications or obstructive jaundice depending on site. Suggested HPO: lymphedema (**HP:0001004**), upper-airway obstruction, jaundice. (ji2020kaposiformhemangioendotheliomacurrent pages 5-6)

Formal per-phenotype prevalence and validated EQ-5D/SF-36 data are unavailable. KHE can substantially impair mobility, routine activities and family functioning; trials have therefore used PedsQL infant/child and Family Impact instruments. (NCT03188068 chunk 1, NCT04775173 chunk 1)

## 4. Genetic and molecular information

A somatic activating **GNA14 c.614A>T (p.Gln205Leu)** variant has been reported in approximately one-third of KHE and one-quarter of TA specimens. It can induce growth-factor independence and MAPK/ERK1/2 activation in experimental systems, but sample sizes were small and it has not been shown to directly cause KMP. A 13q14/16p13.3 translocation was reported in 10% of metaphases in a single study. These are tumor-level, presumably mosaic alterations—not germline disease alleles. (ji2020kaposiformhemangioendotheliomacurrent pages 1-2)

No clinically validated ACMG pathogenic germline variant, HGNC-defined causal gene, population allele frequency, carrier frequency, penetrance, modifier gene, founder effect or pharmacogenomic marker exists for KMP. Consequently, ClinVar-style germline classification, inheritance counseling and population carrier screening are not applicable. **NRAS p.Gln61Arg**, found in kaposiform lymphangiomatosis, was absent from tested KHE and may help distinguish those entities, but is not a KMP marker. (ji2020kaposiformhemangioendotheliomacurrent pages 8-10)

No consistent chromosomal abnormality, DNA-methylation signature, histone modification, repeat expansion or mitochondrial defect has been established. Tumor sequencing remains investigational and may miss low-level mosaicism unless affected tissue is tested.

## 5. Environmental information

There is no evidence that toxins, radiation, pollution, smoking, alcohol, diet, exercise or occupational exposure initiates KMP. No bacterial, viral, fungal or parasitic agent is causal; KHE is HHV-8-negative. Infection or inflammatory events may exacerbate an existing tumor and coagulopathy. (ji2020kaposiformhemangioendotheliomacurrent pages 6-8)

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **A sporadic somatic vascular-cell lesion—GNA14 activation in a subset, but unknown in most cases—leads to** clonal KHE/TA growth and dysregulated MAPK signaling.
2. **Abnormal endothelial/lymphatic differentiation leads to** infiltrative spindle-cell channels expressing CD31/CD34 and lymphatic markers PROX1, podoplanin/D2-40, LYVE1 and VEGFR3.
3. **VEGF-C–VEGFR3 and Ang-2–Tie2 signaling leads to** pathological angiogenesis/lymphangiogenesis and PI3K–AKT–mTOR activation; its direct causal role in KMP remains inferred.
4. **Abnormal podoplanin-positive channels lead to** platelet adhesion and activation through platelet CLEC-2/Src-family signaling; endothelial injury/exposed matrix provides an additional inferred route.
5. **Platelet-rich microthrombi lead to** vessel obstruction, turbulent flow and high shear, which further activate platelets through von Willebrand factor–GPIb-IX/GPIIb-IIIa signaling—an inferred amplification loop.
6. **Persistent platelet aggregation leads to** profound thrombocytopenia and coagulation-cascade activation with consumption of fibrinogen and other factors.
7. **Consumptive coagulopathy branches into:** (a) intralesional hemorrhage, anemia, purpura, pain and rapid tumor engorgement; and (b) systemic bleeding/hemodynamic instability.
8. **Tumor expansion and chronic platelet/inflammatory signaling lead to** compression, ischemic tissue injury, fibrosis, bone/joint destruction, contracture and lymphedema. (ji2020kaposiformhemangioendotheliomacurrent pages 5-6, ji2020kaposiformhemangioendotheliomacurrent pages 2-5, ji2020kaposiformhemangioendotheliomacurrent pages 6-8)

Platelet trapping has been observed histologically in KHE with and without overt KMP, showing that trapping is necessary but not alone sufficient for severe systemic coagulopathy. Podoplanin–CLEC-2 signaling is mechanistically credible, but podoplanin-positive lymphatic malformations do not ordinarily produce the same platelet aggregation, implying additional architecture, flow or endothelial signals. (ji2020kaposiformhemangioendotheliomacurrent pages 5-6)

KHE-derived mesenchymal stromal cells form vascular networks in vitro, express VEGFR3 and produce increased VEGF-C. PROX1 overexpression in mouse hemangioendothelioma cells increases migration, invasiveness, D2-40 and VEGFR3. Serum Ang-2 is elevated in KHE and falls during sirolimus treatment, but this association does not prove Ang-2 causes KMP. (ji2020kaposiformhemangioendotheliomacurrent pages 2-5)

**Suggested annotations:** GO:0001525 angiogenesis; GO:0001946 lymphangiogenesis; GO:0030168 platelet activation; GO:0070527 platelet aggregation; GO:0007596 blood coagulation; GO terms for MAPK cascade and TOR signaling. Candidate Cell Ontology classes: endothelial cell (**CL:0000115**), lymphatic endothelial cell, platelet (**CL:0000233**), mesenchymal stromal cell. Relevant compartments include plasma membrane receptors, cytoplasm and platelet α-granules.

Robust single-cell, spatial-transcriptomic, proteomic, metabolomic, lipidomic or integrated multi-omic KMP signatures were not established in the retrieved evidence. VEGF-A/C/D, IL-6, IL-8 and Ang-1/2 have been prospective exploratory biomarkers, not validated diagnostics. (NCT02110069 chunk 1, NCT03188068 chunk 1)

## 7. Anatomical structures affected

KHE most often affects skin, subcutaneous connective tissue, fascia and skeletal muscle, with possible periarticular, osseous, retroperitoneal, mediastinal, thoracic or visceral extension. In the 2024 cohort, sites were lower extremity **35%**, trunk **29%**, head/neck **24%**, upper extremity **10%**. Approximately 10–12% may lack visible cutaneous disease. (gasparella2025thevascernvascadiagnostic pages 2-6, li2024treatmentexperiencefor pages 1-2, ji2020kaposiformhemangioendotheliomacurrent pages 5-6)

Secondary structures include joints, bone cortex/epiphysis, lymphatic vessels/nodes, airway, pancreas/biliary tract and cardiopulmonary system. Lesions are generally solitary and asymmetric rather than bilaterally distributed. Candidate UBERON annotations should be assigned lesion-by-lesion: skin, subcutaneous tissue, skeletal muscle, limb, thorax, retroperitoneal space, bone and joint. At the subcellular level, no organelle-specific disease defect is established.

## 8. Temporal development

Approximately 90% of KHE becomes evident in the first year and roughly half of cutaneous lesions are detectable at birth. In the 2024 series, 84% were present at birth, 27% of patients were neonates, and thrombocytopenia began at a median **27.8 days**. (li2024treatmentexperiencefor pages 1-2, ji2020kaposiformhemangioendotheliomacurrent pages 2-5)

The active phase may progress over days to weeks with rapid swelling, purpura, pain and falling platelets. Temporary spontaneous softening or platelet recovery can be followed by rebound tumor growth and severe KMP; one documented infant went from 7 to 161 and then 3 ×10⁹/L platelets as the lesion changed. Chronic residual disease may fibrose and continue to cause pain, lymphedema or contracture. (ji2020kaposiformhemangioendotheliomacurrent pages 12-13, ji2020kaposiformhemangioendotheliomacurrent pages 6-8)

The critical intervention window is active KMP, especially platelets <30 ×10⁹/L, falling fibrinogen, bleeding or vital-structure compression. Stable uncomplicated KHE may sometimes be observed, but spontaneous involution is not assumed.

## 9. Inheritance and population

KMP is sporadic and non-Mendelian. There is no established autosomal dominant/recessive, X-linked or mitochondrial inheritance; penetrance, anticipation, germline mosaicism, consanguinity, founder effects and carrier frequency are therefore not applicable.

Reported KHE prevalence and incidence in Massachusetts were approximately **0.91 per 100,000** and **0.071 per 100,000 children per year**, respectively, likely underestimates because small lesions are missed or misclassified. A later expert pathway cited a North American incidence around **0.71 per million**; methodological differences and the rarity of disease preclude a precise global estimate. KMP develops in approximately **42–71%** of KHE, although the selected 2024 surgical cohort reported 78%. (li2019localsutureligationassisted pages 1-2, ji2020kaposiformhemangioendotheliomacurrent pages 1-2, gasparella2025thevascernvascadiagnostic pages 1-2, ji2020kaposiformhemangioendotheliomacurrent pages 5-6)

Sex distribution is approximately equal with occasional slight male predominance. No reproducible ethnic or geographic enrichment has been shown. Adult disease is very rare.

## 10. Diagnostics

### Clinical and laboratory assessment

Urgently obtain serial CBC/platelets, fibrinogen, D-dimer, PT/aPTT, FDP, hemoglobin, blood film/hemolysis studies, and organ-function tests. A practical KMP diagnosis combines a compatible KHE/TA lesion with marked thrombocytopenia and consumptive coagulopathy. Platelets <30 ×10⁹/L indicate severe disease; one trial defined hematologic response as platelets >100,000/µL or twice baseline plus fibrinogen >150 mg/dL. (NCT02110069 chunk 1, NCT03188068 chunk 1)

### Imaging

Doppler ultrasound is useful for superficial lesions and shows an ill-defined hypervascular solid mass. Contrast-enhanced MRI is preferred for mapping deep extent: typical findings are ill-defined margins, multiplanar infiltration, diffuse enhancement, adjacent fat stranding, T1 signal similar to muscle and T2 hyperintensity; dilated fast-flow vessels, edema and adjacent bone/joint injury may occur. Chest/abdominal MRI should be considered in unexplained severe thrombocytopenia when no superficial lesion is evident. (gasparella2025thevascernvascadiagnostic pages 2-6, ji2020kaposiformhemangioendotheliomacurrent pages 6-8)

### Biopsy/pathology

Biopsy is the reference standard when safe, but can worsen severe KMP and may be deferred when clinical/imaging findings are characteristic. Histology shows rounded/confluent infiltrative nodules of spindle endothelial cells forming slit-like blood and malformed lymphatic channels, with erythrocytes, platelet thrombi, hyaline bodies, hemosiderin and fibrosis. Typical immunophenotype is **CD31+, CD34+, ERG/FLI1+, VEGFR3+, D2-40+, LYVE1+, PROX1+, GLUT1−, HHV8−**. (gasparella2025thevascernvascadiagnostic pages 2-6, ji2020kaposiformhemangioendotheliomacurrent pages 6-8, ji2020kaposiformhemangioendotheliomacurrent pages 8-10)

### Differential diagnosis

- **Infantile hemangioma:** GLUT1-positive and does not cause KMP.
- **Congenital hemangioma:** fully formed at birth; RICH involutes, NICH remains stable; any coagulopathy is usually mild and self-limited over 1–2 weeks.
- **Venous malformation:** slow-flow channels, localized intravascular coagulopathy but usually less profound thrombocytopenia.
- **Kaposiform lymphangiomatosis:** multifocal thoracic/osseous lymphatic disease; may carry NRAS p.Q61R and has poorer reported survival.
- **Sarcoma or metastatic neuroblastoma:** must be excluded in atypical deep masses.
- **TA:** may be histologically indistinguishable and belongs to the same spectrum, but is usually more superficial/less aggressive. (gasparella2025thevascernvascadiagnostic pages 2-6, ji2020kaposiformhemangioendotheliomacurrent pages 6-8, ji2020kaposiformhemangioendotheliomacurrent pages 8-10)

Routine WES, WGS, germline panels, CMA, karyotyping, FISH, mitochondrial or repeat-expansion testing is not recommended. Targeted sequencing of affected tissue may be research-useful but does not establish or exclude KMP. No population or newborn screening program exists.

## 11. Outcomes and prognosis

Acute death can result from hemorrhage, rapid tumor expansion, vital-organ compression, tissue destruction or hemodynamic instability. Historical mortality estimates reached **20–30%**, although contemporary multidisciplinary care is likely better; the estimate comes from older/selected series, not modern population survival analysis. (NCT02110069 chunk 1)

In the 2024 cohort, six patients recurred and two died at one and three months after discharge. Long-term morbidity includes fibrosis, chronic pain, lymphedema, reduced range of motion, contracture, scoliosis, bone destruction and functional impairment. No reliable 5- or 10-year survival estimate, life-expectancy decrement, validated prognostic score or molecular prognostic biomarker is available. (li2024treatmentexperiencefor pages 5-7, ji2020kaposiformhemangioendotheliomacurrent pages 6-8)

Poor prognostic features include very young age, large/deep tumors, intrathoracic or retroperitoneal disease, platelets <30 ×10⁹/L, severe anemia, low fibrinogen, rapid enlargement and vital-structure involvement. Early hematologic response is favorable, but radiologic involution may require months to years.

## 12. Treatment

Management belongs in a multidisciplinary vascular-anomalies center. No drug was originally approved specifically for KHE/KMP; systemic uses below are generally off-label. (ji2020kaposiformhemangioendotheliomacurrent pages 1-2, gasparella2025thevascernvascadiagnostic pages 1-2)

### Practical strategy

1. **Stabilize:** assess bleeding and organ compromise; use packed red cells for symptomatic severe anemia, cryoprecipitate/FFP for active bleeding or marked hypofibrinogenemia.
2. **Avoid routine platelet transfusion:** trapped platelets are rapidly consumed; reserve platelets for active bleeding or an imminent procedure, especially when <30 ×10⁹/L. In the 2024 cohort, transfused counts fell again within 48 hours. (li2024treatmentexperiencefor pages 5-7, ji2020kaposiformhemangioendotheliomacurrent pages 8-10)
3. **Treat severe KMP:** contemporary expert practice favors **sirolimus plus a short course of corticosteroid**. A common sirolimus start is 0.8 mg/m² twice daily, adjusted to trough 8–15 ng/mL; prednisolone 2 mg/kg/day can be tapered over 4–6 weeks after stabilization. NCIt candidates: sirolimus, prednisolone, systemic pharmacotherapy. (NCT03188068 chunk 1, ji2020kaposiformhemangioendotheliomacurrent pages 8-10)
4. **Escalate/add vincristine** for inadequate response, severe compression or where sirolimus is unsuitable: 0.05 mg/kg weekly in children <10 kg or 1.5 mg/m² in larger patients. NCIt: vincristine. (NCT02110069 chunk 1)
5. **Localized resectable tumor:** complete excision can be definitive after correction of coagulopathy. Surgery during uncontrolled extensive KMP is hazardous because of hemorrhage and functional injury. Embolization or sclerotherapy is reserved for selected anatomy and experienced centers. (li2024treatmentexperiencefor pages 9-10, ji2020kaposiformhemangioendotheliomacurrent pages 10-12)

### Comparative evidence and outcomes

Historical response estimates were **10–27%** for corticosteroid monotherapy, **72%** for vincristine, and **94%** for sirolimus among patients who had failed or relapsed after previous therapy. These are cross-study observational estimates, not head-to-head modern trials. Steroids can normalize platelets rapidly but sustained response is inconsistent; adverse effects include infection, growth retardation and behavioral change. Vincristine requires intravenous/central access and can cause neurotoxicity. (NCT03188068 chunk 1, ji2020kaposiformhemangioendotheliomacurrent pages 10-12)

The 2024 70-patient cohort used a surgery-heavy strategy: 65/70 underwent surgery, 54 had complete first-operation removal, six recurred and two died. Platelets rose from 38.4×10³/µL at admission to 97.7 after pretreatment, 160.9 one day after surgery and a mean peak of 462.1×10³/µL. Because this was a selected retrospective center cohort, it does not prove surgery is superior to medical therapy. (li2024treatmentexperiencefor pages 5-7)

Sirolimus toxicities include stomatitis/oral mucositis, dyslipidemia, cytopenias, liver-enzyme abnormalities and infection; rare interstitial pneumonitis and Pneumocystis pneumonia may be fatal. Two patients in the 2024 cohort stopped sirolimus because of severe pneumonia. Drug levels, CBC, renal/liver function, lipids, infections and drug interactions require monitoring. (li2024treatmentexperiencefor pages 1-2, ji2020kaposiformhemangioendotheliomacurrent pages 10-12)

### Recent trials and implementation

- **NCT03188068**, completed phase 2: sirolimus versus sirolimus plus prednisolone; 30 enrolled. It assessed platelets/fibrinogen at two months, MRI volume, symptoms, biomarkers and PedsQL. (NCT03188068 chunk 1)
- **NCT04077515**, completed phase 4: 92 children randomized to troughs 7–10 versus >10–15 ng/mL, motivated by possible infection reduction at lower exposure. (NCT04077515 chunk 1)
- **NCT04775173**, completed phase 2: 79 patients, trough 5–8 versus 10–15 ng/mL; objective MRI response was ≥20% volume reduction at 12 months. (NCT04775173 chunk 1)
- **NCT04448873**, completed phase 4: 30 patients in guided discontinuation versus maintenance after at least two years’ remission; tapering was limited to 10% monthly over at least six months. Results were not available in the retrieved record. (NCT04448873 chunk 1)
- **NCT02110069**, randomized sirolimus-versus-vincristine study: terminated after only four participants because KHE/KMP incidence was too rare and sporadic, illustrating why comparative certainty remains low. (NCT02110069 chunk 1)

Topical sirolimus or tacrolimus may help a truly superficial KHE/TA without deep disease, but evidence consists largely of case reports and mostly TA. Gene, cell, RNA and immune therapies have no established role. There is no validated genotype-guided treatment or KMP pharmacogenomic recommendation.

## 13. Prevention

**Primary prevention:** none; there is no established modifiable exposure, vaccine, inherited carrier state or prenatal test. Standard immunization should not be withheld solely because post-vaccination exacerbations have appeared in isolated reports.

**Secondary prevention:** population screening and newborn screening are not justified. For a known KHE/TA, education about rapid enlargement, purpura, pain and bleeding; prompt CBC/fibrinogen/D-dimer testing; baseline MRI; and specialist follow-up can detect KMP early.

**Tertiary prevention:** avoid nonessential tumor trauma and biopsy during uncontrolled coagulopathy; avoid routine platelet transfusion; promptly treat infection; monitor sirolimus exposure/toxicity; protect joint motion with rehabilitation; and surveil for fibrosis, lymphedema and relapse. Sirolimus tapering should be slow and clinically monitored because optimal duration is unresolved. (ji2020kaposiformhemangioendotheliomacurrent pages 6-8, NCT04448873 chunk 1)

Genetic counseling should explain that current evidence supports a sporadic somatic lesion with negligible known recurrence risk to siblings or offspring, rather than a hereditary syndrome.

## 14. Other species and natural disease

No well-validated naturally occurring veterinary counterpart of human KHE-associated KMP, breed association, OMIA disorder, zoonotic transmission or cross-species infectious susceptibility was established in the retrieved evidence. Accordingly, NCBI Taxon/VBO breed annotations, veterinary inheritance and transmission fields should be recorded as **not established**, not negative in principle.

The relevant signaling proteins and platelet pathways are evolutionarily conserved, but conservation alone does not demonstrate a natural animal disease.

## 15. Models and research gaps

Available models are limited. Mouse hemangioendothelioma cells can form KHE-like intradermal tumors; forced **PROX1** increases invasion, migration, podoplanin and VEGFR3. Patient-derived KHE mesenchymal stromal cells support vascular-network formation in vitro and show VEGF-C/VEGFR3 activity. These systems model angiogenic/lymphatic tumor biology but do not fully reproduce infant KMP, systemic platelet consumption, bleeding and chronic musculoskeletal sequelae. (ji2020kaposiformhemangioendotheliomacurrent pages 2-5)

No validated GNA14 knock-in animal that consistently recapitulates KHE plus KMP, patient-derived organoid, humanized platelet model, large CRISPR screen, or mature single-cell/spatial atlas was found. Priorities are: defining the tumor-initiating cell; determining why only some KHEs produce KMP; directly testing podoplanin–CLEC-2 and shear amplification in vivo; identifying predictors of sirolimus resistance/relapse; establishing infant pharmacokinetics and safer troughs; and conducting multicenter natural-history and quality-of-life studies.

## Key source notes and exact quotations

- Ji et al., *Orphanet Journal of Rare Diseases*, **3 February 2020**, PMID **32014025**, DOI/URL: https://doi.org/10.1186/s13023-020-1320-1. The abstract states: **“The initiating mechanism during the pathogenesis of KHE has yet to be discovered”** and identifies abnormal angiogenesis and lymphangiogenesis as its main pathological features. (ji2020kaposiformhemangioendotheliomacurrent pages 1-2)
- Li et al., *Frontiers in Oncology*, **5 June 2024**, DOI/URL: https://doi.org/10.3389/fonc.2024.1336763. Its abstract reports: **“KHE may develop into the Kasabach–Merritt phenomenon (KMP), which is characterized by thrombocytopenia and consumptive coagulopathy.”** This is recent primary human cohort evidence, but retrospective and center-specific. (li2024treatmentexperiencefor pages 1-2)
- Drolet et al., *Journal of Pediatrics*, **July 2013**, PMID **23796341**, DOI: https://doi.org/10.1016/j.jpeds.2013.03.080, remains a foundational consensus standard, although its recommendations were expert-derived rather than based on large randomized trials. (NCT04077515 chunk 1, ji2020kaposiformhemangioendotheliomacurrent pages 8-10)
- The newer VASCERN-VASCA pathway, published online **13 December 2025**, DOI/URL: https://doi.org/10.1007/s00431-025-06631-6, provides multidisciplinary European expert guidance but is explicitly level-V consensus evidence. (gasparella2025thevascernvascadiagnostic pages 1-2)

**Overall conclusion.** KMP is best represented in a knowledge base as a life-threatening hematologic complication of KHE/TA, not as a conventional germline syndrome. The most supported mechanism is self-amplifying intratumoral platelet trapping and activation within an abnormal angiogenic/lymphangiogenic vascular bed. Sirolimus plus short-course corticosteroid has become the principal medical strategy for severe disease, but optimal dose, duration and tapering remain unsettled, and much of the quantitative literature is retrospective.

References

1. (li2024treatmentexperiencefor pages 1-2): Miaomiao Li, Xusheng Wang, Rosalind Kieran, Zheng Wei Sun, Yubin Gong, Hongzhao Lei, Bin Sun, Li Xiao, Yanlin Wang, Song Wang, Zhiyu Li, Luying Wang, Renrong Lv, Feng Xue, Jianfeng Ge, Changxian Dong, and Ran Huo. Treatment experience for different risk groups of kaposiform hemangioendothelioma. Frontiers in Oncology, Jun 2024. URL: https://doi.org/10.3389/fonc.2024.1336763, doi:10.3389/fonc.2024.1336763. This article has 10 citations.

2. (ji2020kaposiformhemangioendotheliomacurrent pages 1-2): Yi Ji, Siyuan Chen, Kaiying Yang, Chunchao Xia, and Li Li. Kaposiform hemangioendothelioma: current knowledge and future perspectives. Orphanet Journal of Rare Diseases, Feb 2020. URL: https://doi.org/10.1186/s13023-020-1320-1, doi:10.1186/s13023-020-1320-1. This article has 230 citations and is from a peer-reviewed journal.

3. (gasparella2025thevascernvascadiagnostic pages 2-6): Paolo Gasparella, Emir Q. Haxhija, Rune Andersen, Maria Barea, Eulalia Baselga, Miguel Bejarano Serrano, Sigurd Berger, Annouk Anne Bisdorff, Olivia Boccara, Petra Borgards, Maria Bom-Sucesso, Laurence M. Boon, Anca Maria Cimpean, Andrea Diociaiuti, Veronika Dvorakova, May El Hachem, Sofia Frisk, Nader Ghaffarpour, Annegret Holm, Alan D. Irvine, Mikkel Kaltoft, Friedrich G. Kapp, Olga Koskova, Kristiina Kyrklund, Miguel Madureira, Darius Palionis, Przemysław Przewratil, Bitten Schönewolf-Greulich, Maria-Corina Stanciulescu, Jaroslav Štěrba, Jukka Tolonen, Birute Vaisnyte, Carine van der Vleuten, Dariusz Wyrzykowski, Leo Schultze Kool, and Miikka Vikkula. The vascern-vasca diagnostic and management pathways for kaposiform hemangioendothelioma. European Journal of Pediatrics, Dec 2025. URL: https://doi.org/10.1007/s00431-025-06631-6, doi:10.1007/s00431-025-06631-6. This article has 5 citations and is from a peer-reviewed journal.

4. (NCT03188068 chunk 1): Yi Ji. Sirolimus Versus Sirolimus Plus Prednisolone for Kaposiform Hemangioendothelioma. West China Hospital. 2017. ClinicalTrials.gov Identifier: NCT03188068

5. (NCT04077515 chunk 1):  Safety and Efficacy of Low-dose Sirolimus to Kaposiform Hemangioendothelioma. Children's Hospital of Fudan University. 2019. ClinicalTrials.gov Identifier: NCT04077515

6. (ji2020kaposiformhemangioendotheliomacurrent pages 5-6): Yi Ji, Siyuan Chen, Kaiying Yang, Chunchao Xia, and Li Li. Kaposiform hemangioendothelioma: current knowledge and future perspectives. Orphanet Journal of Rare Diseases, Feb 2020. URL: https://doi.org/10.1186/s13023-020-1320-1, doi:10.1186/s13023-020-1320-1. This article has 230 citations and is from a peer-reviewed journal.

7. (ji2020kaposiformhemangioendotheliomacurrent pages 6-8): Yi Ji, Siyuan Chen, Kaiying Yang, Chunchao Xia, and Li Li. Kaposiform hemangioendothelioma: current knowledge and future perspectives. Orphanet Journal of Rare Diseases, Feb 2020. URL: https://doi.org/10.1186/s13023-020-1320-1, doi:10.1186/s13023-020-1320-1. This article has 230 citations and is from a peer-reviewed journal.

8. (ji2020kaposiformhemangioendotheliomacurrent pages 2-5): Yi Ji, Siyuan Chen, Kaiying Yang, Chunchao Xia, and Li Li. Kaposiform hemangioendothelioma: current knowledge and future perspectives. Orphanet Journal of Rare Diseases, Feb 2020. URL: https://doi.org/10.1186/s13023-020-1320-1, doi:10.1186/s13023-020-1320-1. This article has 230 citations and is from a peer-reviewed journal.

9. (ji2020kaposiformhemangioendotheliomacurrent pages 8-10): Yi Ji, Siyuan Chen, Kaiying Yang, Chunchao Xia, and Li Li. Kaposiform hemangioendothelioma: current knowledge and future perspectives. Orphanet Journal of Rare Diseases, Feb 2020. URL: https://doi.org/10.1186/s13023-020-1320-1, doi:10.1186/s13023-020-1320-1. This article has 230 citations and is from a peer-reviewed journal.

10. (li2024treatmentexperiencefor pages 5-7): Miaomiao Li, Xusheng Wang, Rosalind Kieran, Zheng Wei Sun, Yubin Gong, Hongzhao Lei, Bin Sun, Li Xiao, Yanlin Wang, Song Wang, Zhiyu Li, Luying Wang, Renrong Lv, Feng Xue, Jianfeng Ge, Changxian Dong, and Ran Huo. Treatment experience for different risk groups of kaposiform hemangioendothelioma. Frontiers in Oncology, Jun 2024. URL: https://doi.org/10.3389/fonc.2024.1336763, doi:10.3389/fonc.2024.1336763. This article has 10 citations.

11. (ji2020kaposiformhemangioendotheliomacurrent pages 10-12): Yi Ji, Siyuan Chen, Kaiying Yang, Chunchao Xia, and Li Li. Kaposiform hemangioendothelioma: current knowledge and future perspectives. Orphanet Journal of Rare Diseases, Feb 2020. URL: https://doi.org/10.1186/s13023-020-1320-1, doi:10.1186/s13023-020-1320-1. This article has 230 citations and is from a peer-reviewed journal.

12. (NCT02110069 chunk 1): Denise Martin Adams. A Study to Compare Vincristine to Sirolimus for Treatment of High Risk Vascular Tumors. Boston Children's Hospital. 2017. ClinicalTrials.gov Identifier: NCT02110069

13. (li2019localsutureligationassisted pages 1-2): Xiao Li, Ming‑Zhe Wen, Li‑Xin Su, Xi‑Tao Yang, Yi‑Feng Han, and Xin‑Dong Fan. Local suture ligation-assisted percutaneous sclerotherapy for kasabach-merritt phenomenon-associated kaposiform haemangioendothelioma. Oncology Letters, 17:981-989, Nov 2019. URL: https://doi.org/10.3892/ol.2018.9661, doi:10.3892/ol.2018.9661. This article has 5 citations and is from a peer-reviewed journal.

14. (NCT04775173 chunk 1): Yi Ji. Efficacy and Safety of Different Concentrations of Sirolimus in the Treatment of Kaposiform Hemangioendothelioma.. West China Hospital. 2021. ClinicalTrials.gov Identifier: NCT04775173

15. (ji2020kaposiformhemangioendotheliomacurrent pages 12-13): Yi Ji, Siyuan Chen, Kaiying Yang, Chunchao Xia, and Li Li. Kaposiform hemangioendothelioma: current knowledge and future perspectives. Orphanet Journal of Rare Diseases, Feb 2020. URL: https://doi.org/10.1186/s13023-020-1320-1, doi:10.1186/s13023-020-1320-1. This article has 230 citations and is from a peer-reviewed journal.

16. (gasparella2025thevascernvascadiagnostic pages 1-2): Paolo Gasparella, Emir Q. Haxhija, Rune Andersen, Maria Barea, Eulalia Baselga, Miguel Bejarano Serrano, Sigurd Berger, Annouk Anne Bisdorff, Olivia Boccara, Petra Borgards, Maria Bom-Sucesso, Laurence M. Boon, Anca Maria Cimpean, Andrea Diociaiuti, Veronika Dvorakova, May El Hachem, Sofia Frisk, Nader Ghaffarpour, Annegret Holm, Alan D. Irvine, Mikkel Kaltoft, Friedrich G. Kapp, Olga Koskova, Kristiina Kyrklund, Miguel Madureira, Darius Palionis, Przemysław Przewratil, Bitten Schönewolf-Greulich, Maria-Corina Stanciulescu, Jaroslav Štěrba, Jukka Tolonen, Birute Vaisnyte, Carine van der Vleuten, Dariusz Wyrzykowski, Leo Schultze Kool, and Miikka Vikkula. The vascern-vasca diagnostic and management pathways for kaposiform hemangioendothelioma. European Journal of Pediatrics, Dec 2025. URL: https://doi.org/10.1007/s00431-025-06631-6, doi:10.1007/s00431-025-06631-6. This article has 5 citations and is from a peer-reviewed journal.

17. (li2024treatmentexperiencefor pages 9-10): Miaomiao Li, Xusheng Wang, Rosalind Kieran, Zheng Wei Sun, Yubin Gong, Hongzhao Lei, Bin Sun, Li Xiao, Yanlin Wang, Song Wang, Zhiyu Li, Luying Wang, Renrong Lv, Feng Xue, Jianfeng Ge, Changxian Dong, and Ran Huo. Treatment experience for different risk groups of kaposiform hemangioendothelioma. Frontiers in Oncology, Jun 2024. URL: https://doi.org/10.3389/fonc.2024.1336763, doi:10.3389/fonc.2024.1336763. This article has 10 citations.

18. (NCT04448873 chunk 1):  Guided Discontinuation Versus Maintenance Treatment of Sirolimus in Pediatric Patients With Kaposiform Hemangioendothelioma. Children's Hospital of Fudan University. 2020. ClinicalTrials.gov Identifier: NCT04448873

## Artifacts

- [Edison artifact artifact-00](Kasabach-Merritt_Syndrome-deep-research-falcon_artifacts/artifact-00.md)

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
| Terms checked | 28 |
| Resolved | 28 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0007708` (3 mentions) - the report calls it "if available"; MONDO calls it **Kasabach-Merritt syndrome**