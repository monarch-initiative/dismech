---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-06T02:48:22.886777'
end_time: '2026-09-06T02:56:36.318456'
duration_seconds: 493.43
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Multiple Mitochondrial Dysfunctions Syndrome 2
  mondo_id: MONDO:0013675
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 29
reference_validation:
  total_references: 8
  verified: 8
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 8
  on_topic: 6
  validator_version: 0.2.1
term_validation:
  total_terms: 60
  verified: 60
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0013675
    reported_labels:
    - if available
    ontology_label: multiple mitochondrial dysfunctions syndrome 2
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Multiple_Mitochondrial_Dysfunctions_Syndrome_2-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Multiple Mitochondrial Dysfunctions Syndrome 2
- **MONDO ID:** MONDO:0013675 (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Multiple Mitochondrial Dysfunctions Syndrome 2** covering all of the
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
- **Disease Name:** Multiple Mitochondrial Dysfunctions Syndrome 2
- **MONDO ID:** MONDO:0013675 (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Multiple Mitochondrial Dysfunctions Syndrome 2** covering all of the
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


# Multiple Mitochondrial Dysfunctions Syndrome 2 (MMDS2): Research Report

## Executive summary

Multiple mitochondrial dysfunctions syndrome 2 (MMDS2) is an ultrarare, autosomal-recessive mitochondrial disorder caused by biallelic **BOLA3** variants. BOLA3 participates in mitochondrial iron–sulfur (Fe–S) cluster delivery. Its deficiency compromises oxidative phosphorylation, lipoate-dependent 2-oxoacid dehydrogenases, glycine cleavage, and—as demonstrated in 2023—mitochondrial ribosome assembly and translation. Classical MMDS2 presents in infancy with rapidly progressive encephalopathy, leukodystrophy, hypotonia or weakness, lactic acidosis, hyperglycinemia, cardiomyopathy, respiratory failure, and early death. Nevertheless, residual-function alleles can produce substantially attenuated disease, including documented neurological recovery. Evidence remains limited to fewer than a few dozen published patients, retrospective reports, patient fibroblasts, and experimental models; there is no established disease-modifying treatment or disease-specific clinical trial.

The following compact table summarizes the principal knowledge-base fields; the narrative afterward supplies interpretation and ontology annotations.

| Knowledge-base field | MMDS2 summary | Evidence |
|---|---|---|
| Identity and identifiers | Multiple mitochondrial dysfunctions syndrome 2 (MMDS2); multiple mitochondrial dysfunctions syndrome type 2 with hyperglycinemia; BOLA3-related multiple mitochondrial dysfunction syndrome. **MONDO:** MONDO:0013675; **OMIM:** 614299. Specific ICD-10, ICD-11, MeSH, and Orphanet identifiers were not established from the retrieved evidence. | Open Targets independently maps MONDO:0013675 to BOLA3; systematic clinical literature identifies OMIM 614299 (OpenTargets Search: multiple mitochondrial dysfunctions syndrome 2-BOLA3, stutterd2019severeleukoencephalopathywith pages 1-2, lebigot2021areviewof pages 7-9). |
| Gene and inheritance | Caused by **biallelic germline variants in BOLA3** (bolA family member 3; Ensembl ENSG00000163170). Inheritance is **autosomal recessive**; obligate heterozygous parents are generally unaffected. Penetrance has not been quantified but appears high for damaging biallelic genotypes. | Human genetic association and recessive pedigrees (OpenTargets Search: multiple mitochondrial dysfunctions syndrome 2-BOLA3, stutterd2019severeleukoencephalopathywith pages 1-2, stutterd2019severeleukoencephalopathywith pages 2-4). |
| Reported population | A 2021 systematic review identified **18 patients from 14 families worldwide** and eight BOLA3 variants. Disease-specific prevalence, incidence, carrier frequency, sex ratio, and population-based survival statistics are unavailable. | Aggregated systematic-review evidence; very small, ascertainment-biased case series (lebigot2021areviewof pages 11-13). |
| Onset and core neurologic phenotypes | Usually neonatal or infantile onset, commonly within the first year; prior cases in one comparison began from birth to 8 months. Motor delay or regression occurred in **12/12**, seizures in **5/10**, and independent walking in **1/5** evaluable previously reported patients. An attenuated case began acutely at 18 months with hemiparesis, ataxia, and speech/cognitive regression. | Patient-level and aggregated human evidence (stutterd2019severeleukoencephalopathywith pages 4-6, stutterd2019severeleukoencephalopathywith pages 1-2, stutterd2019severeleukoencephalopathywith pages 2-4). |
| Multisystem manifestations | Severe cases may include hypotonia or weakness, feeding difficulty/failure to thrive, respiratory failure, optic atrophy or nystagmus, renal or hepatic failure, and cardiomyopathy. Cardiomyopathy occurred in **7/9** in one historical comparison and in approximately half of the 18-patient review cohort; hypertrophic and dilated forms were reported. | Aggregated human clinical evidence (stutterd2019severeleukoencephalopathywith pages 4-6, lebigot2021areviewof pages 7-9, lebigot2021areviewof pages 11-13). |
| Biochemical markers | Typical abnormalities include elevated plasma/urine glycine, lactate, pyruvate, and metabolic acidosis; historical denominators were elevated lactate **11/12**, glycine **8/8**, reduced respiratory-chain complex I/II activity **10/12**, and reduced pyruvate-dehydrogenase activity **6/7**. Normal lactate or tissue respiratory-chain assays do not exclude MMDS2: the recovery case had elevated plasma/urine glycine, normal CSF glycine and lactate, but fibroblast PDH activity was **20% of control** with reduced complex I/II subunits. | Human biochemical evidence (stutterd2019severeleukoencephalopathywith pages 4-6, stutterd2019severeleukoencephalopathywith pages 2-4). |
| Neuroimaging | Characteristic MRI findings include bilateral diffuse or multifocal periventricular/deep-white-matter T2 hyperintensity, dysmyelination or cavitating/cystic leukodystrophy, restricted diffusion, corpus-callosum, brainstem, cerebellar, spinal-cord, or basal-ganglia involvement, and cerebral/cerebellar atrophy. MR spectroscopy may show a lactate peak and reduced N-acetylaspartate. | Human neuroradiologic evidence (stutterd2019severeleukoencephalopathywith pages 4-6, stutterd2019severeleukoencephalopathywith pages 2-4, lebigot2021areviewof pages 9-11). |
| Key variants | Reported variants include **c.123dupA (p.Glu42Argfs*13), c.136C>T (p.Arg46*), c.159dupT (p.Asp54*), c.176G>A (p.Cys59Tyr), c.200T>A (p.Ile67Asn), c.220_222del (p.Glu74del), c.225_229del (p.Lys75Asnfs*9), c.287A>G (p.His96Arg), and c.295C>T (p.Arg99Trp)** across retrieved reports/reviews. The 2021 review counted eight variants; the larger list reflects subsequent/independently tabulated reports and should be reconciled against current ClinVar and transcript versions before database import. Population allele frequencies and current ACMG/ClinVar classifications were not retrieved. | Aggregated variant tables and case report (lebigot2021areviewof pages 7-9, stutterd2019severeleukoencephalopathywith pages 2-4, lebigot2021areviewof pages 9-11). |
| Variant-specific functional effects | **p.Cys59Tyr:** retains partial Fe–S transfer; NFU1 became [4Fe–4S]-bound at **25% versus 65% with wild type**, consistent with an attenuated Arg46*/Cys59Tyr phenotype. **p.Ile67Asn:** preserves global fold but disrupts GLRX5 binding and BOLA3–GLRX5 heterocomplex formation. **p.His96Arg:** permits partner interaction but forms an aberrant complex unable to assemble an NFU1 [4Fe–4S] cluster. **p.Arg46\*:** predicted/truncating loss of function; direct functional quantification was not retrieved. | Recombinant-protein/in-vitro studies and human genotype–phenotype correlation; DOI 10.3390/ijms22094848, 10.1093/mtomcs/mfab010, and 10.3390/ijms241411734 (sen2021biochemicalimpactof pages 1-2, bargagna2023understandingthemolecular pages 1-2, saudino2021molecularbasisof pages 1-2, saudino2021molecularbasisof pages 11-12, sen2021biochemicalimpactof pages 7-8). |
| Core mechanism | BOLA3 and GLRX5 form a bridged [2Fe–2S] carrier complex that transfers clusters to NFU1, where reductive coupling generates [4Fe–4S] clusters. BOLA3 deficiency therefore impairs maturation of respiratory-chain Fe–S proteins and lipoic-acid synthase, reducing oxidative phosphorylation and lipoylation of PDH, α-ketoglutarate dehydrogenase, branched-chain ketoacid dehydrogenase, and glycine-cleavage proteins. The resulting ATP deficit, lactic acidosis, and impaired glycine cleavage lead to high-energy-tissue injury, particularly leukoencephalopathy and cardiomyopathy. | Biochemical and cellular evidence; some links from energy failure to tissue-selective clinical injury remain inferred (bargagna2023understandingthemolecular pages 1-2, saudino2021molecularbasisof pages 1-2, saudino2021molecularbasisof pages 11-12). |
| 2023 mechanistic development | The **GLRX5–BOLA3 node also supplies [2Fe–2S] clusters to mitochondrial ribosomal subunits**. BOLA3 depletion reduced mitochondrial translation to **60–70% of control**, and five-day depletion made mitoribosomal ⁵⁵Fe incorporation virtually undetectable. BOLA3-mutant patient fibroblasts showed attenuated mitochondrial protein synthesis and defective assembled OXPHOS complexes, adding impaired mitoribosome assembly to the disease mechanism. | HEK293T knockdown and patient-fibroblast evidence; published online 12 October 2023, DOI 10.1093/nar/gkad842 (zhong2023bola3andnfu1 pages 9-11, zhong2023bola3andnfu1 pages 1-2). |
| Diagnosis | Suspect MMDS2 in early-onset regression, leukodystrophy, cardiomyopathy, lactic acidosis, and hyperglycinemia. Evaluate plasma/CSF/urine lactate, pyruvate and glycine; acylglycine/organic-acid profiles; brain MRI/MRS; ECG/echocardiography; ophthalmology; respiratory status; and respiratory-chain, PDH, and protein-lipoylation studies in fibroblasts or muscle where available. Confirm with a nuclear mitochondrial/leukodystrophy panel or WES/WGS identifying pathogenic biallelic BOLA3 variants, followed by segregation and, for uncertain variants, RNA or functional studies. This is an evidence-based diagnostic approach, not a formal disease-specific guideline. | Human diagnostic and review evidence (stutterd2019severeleukoencephalopathywith pages 1-2, stutterd2019severeleukoencephalopathywith pages 2-4, lebigot2021areviewof pages 1-2). |
| Treatment and trials | No established disease-modifying therapy was identified. Management is supportive: nutrition and feeding support; treatment of seizures, acidosis, respiratory insufficiency, and heart failure; and physical, occupational, and speech rehabilitation. “Mitochondrial” vitamin/cofactor cocktails have been used without clear evidence of benefit; one possible partial methylprednisolone response is anecdotal and cannot establish efficacy. The retrieved ClinicalTrials.gov search found **no relevant MMDS2-specific interventional trial or NCT identifier**. | Case-based treatment evidence and direct trial-registry search (stutterd2019severeleukoencephalopathywith pages 6-7, lebigot2021areviewof pages 11-13). |
| Prognosis | Classical disease is severe, progressive, and frequently fatal in infancy or early childhood. In one historical series, survival ranged from **3 months to 11 years**, and recovery occurred in **0/10** evaluable prior cases. Genotype-dependent attenuation is documented: the Arg46*/Cys59Tyr patient recovered clinically over four years and was alive at age eight with improved MRI, while an Arg99Trp patient reportedly survived to age 12. Formal 5- or 10-year survival estimates are unavailable. | Human natural-history and genotype–phenotype evidence (stutterd2019severeleukoencephalopathywith pages 4-6, stutterd2019severeleukoencephalopathywith pages 1-2, lebigot2021areviewof pages 11-13). |
| Evidence limitations | Evidence is dominated by individual patients, small retrospective case series, one systematic review, patient fibroblasts, gene-silencing models, and recombinant-protein experiments. Frequencies use incomplete and varying denominators; ascertainment favors severe cases. No population epidemiology, validated quality-of-life instruments, standardized diagnostic criteria, controlled treatment trials, prognostic model, protective variants, established modifier genes, disease-specific epigenomic signature, single-cell/spatial study, or validated biomarker was identified. | Cross-source evidence assessment (stutterd2019severeleukoencephalopathywith pages 6-7, stutterd2019severeleukoencephalopathywith pages 4-6, lebigot2021areviewof pages 11-13, zhong2023bola3andnfu1 pages 9-11). |


*Table: Concise disease-level summary of BOLA3-related MMDS2, integrating clinical frequencies, variants, mechanisms, diagnosis, management, prognosis, and major evidence gaps. Findings distinguish human observations from experimental or inferred mechanisms.*

## 1. Disease information

**Definition.** MMDS2 is a nuclear-encoded mitochondrial Fe–S-cluster biogenesis disorder in which defective BOLA3 impairs several mitochondrial enzyme systems simultaneously. It belongs to the multiple mitochondrial dysfunction syndromes but is genetically distinct from NFU1-, IBA57-, ISCA2-, ISCA1-, and PMPCB-associated conditions. The Open Targets association is specific to BOLA3 and is supported by five genetic-evidence records (OpenTargets Search: multiple mitochondrial dysfunctions syndrome 2-BOLA3).

**Identifiers and synonyms**

- **MONDO:** MONDO:0013675.
- **OMIM phenotype:** **614299**.
- **Gene:** BOLA3; Ensembl **ENSG00000163170**; approved name *bolA family member 3* (OpenTargets Search: multiple mitochondrial dysfunctions syndrome 2-BOLA3).
- **Synonyms:** multiple mitochondrial dysfunctions syndrome type 2; MMDS2; multiple mitochondrial dysfunctions syndrome 2 with hyperglycinemia/hyperglycinaemia; BOLA3-related multiple mitochondrial dysfunction syndrome; BOLA3-associated mitochondrial leukoencephalopathy.
- A disease-specific Orphanet, MeSH, ICD-10, or ICD-11 code was not verified in the retrieved evidence. In clinical coding, cases are therefore likely captured under broader mitochondrial-metabolism or leukodystrophy categories rather than a unique MMDS2 code.

The evidence is principally **aggregated disease-level literature derived from individual published patients**, not EHR-scale population data. The 2021 systematic review assembled 18 patients from 14 families, while individual reports provide more detailed longitudinal and biochemical observations (stutterd2019severeleukoencephalopathywith pages 1-2, lebigot2021areviewof pages 11-13).

## 2. Etiology, risk, and protective factors

### Primary cause

The cause is biallelic, germline, loss-of-function or function-impairing variation in **BOLA3**, inherited in an autosomal-recessive pattern. Truncating variants can reduce functional protein, whereas missense variants can disrupt Fe–S coordination, GLRX5 recognition, or cluster transfer without necessarily unfolding BOLA3 (sen2021biochemicalimpactof pages 1-2, bargagna2023understandingthemolecular pages 1-2, sen2021biochemicalimpactof pages 7-8).

### Risk factors

- **Genetic:** having two pathogenic BOLA3 alleles is the defining risk. Consanguinity may increase the probability of homozygosity for rare alleles, but a disease-specific quantitative estimate is unavailable.
- **Family history:** each full sibling of an affected child has the standard autosomal-recessive prior probabilities of 25% affected, 50% carrier, and 25% unaffected/non-carrier, assuming both parents are heterozygous and no unusual mechanism.
- **Environmental, lifestyle, infectious, sex, or occupational risks:** none are established as primary causes. An attenuated patient's acute presentation at 18 months occurred without preceding illness or injury; the authors proposed increased developmental/myelination-related metabolic demand as a possible trigger, but this remains inference (stutterd2019severeleukoencephalopathywith pages 6-7).

### Protective factors and gene–environment interaction

No validated protective allele, modifier gene, diet, drug, or environmental exposure has been demonstrated. Residual biochemical activity is a plausible genotype-dependent protective mechanism: p.Cys59Tyr retained partial NFU1 cluster assembly and occurred in the patient with clinical recovery. That association is biologically coherent but is based on one genotype and must not be treated as a validated prognostic rule (saudino2021molecularbasisof pages 1-2, saudino2021molecularbasisof pages 11-12). Fever, fasting, or illness could theoretically expose limited mitochondrial reserve, as in other mitochondrial diseases, but MMDS2-specific gene–environment evidence is absent.

## 3. Phenotypes

### Neurological and developmental

Typical onset is neonatal or infantile. In one historical comparison, previous patients began from birth to eight months. Motor delay or regression occurred in **12/12**, seizures in **5/10**, and only **1/5** evaluable children acquired independent walking. Suggested terms include **HP:0001263 global developmental delay**, **HP:0002376 developmental regression**, **HP:0001252 muscular hypotonia**, **HP:0001250 seizure**, **HP:0002063 rigidity/spasticity**, **HP:0001288 gait disturbance**, and **HP:0000238 hydrocephalus only if individually documented**—the latter should not be assigned generically (stutterd2019severeleukoencephalopathywith pages 4-6).

The attenuated Arg46*/Cys59Tyr case developed acute hemiparesis, ataxia, and loss of speech at 18 months, then recovered substantially over four years. At age eight, only subtle weakness and attention-deficit disorder remained. Suggested terms are **HP:0001269 hemiparesis**, **HP:0001251 ataxia**, **HP:0002167 speech regression**, and **HP:0007018 attention deficit/hyperactivity disorder** where clinically confirmed (stutterd2019severeleukoencephalopathywith pages 2-4).

### White-matter and imaging phenotype

MRI commonly shows bilateral periventricular and deep-white-matter T2 hyperintensity, dysmyelination or cavitating/cystic leukodystrophy, restricted diffusion, corpus-callosum lesions, and variable brainstem, cerebellar, basal-ganglia, or spinal-cord involvement. Cerebral/cerebellar atrophy and an MRS lactate peak with reduced N-acetylaspartate can occur. Suggested HPO terms include **HP:0002415 leukodystrophy**, **HP:0012444 brain atrophy**, **HP:0002059 cerebral atrophy**, and **HP:0001272 cerebellar atrophy**, assigning only findings actually present in an individual (stutterd2019severeleukoencephalopathywith pages 4-6, stutterd2019severeleukoencephalopathywith pages 2-4, lebigot2021areviewof pages 9-11).

### Cardiopulmonary, ophthalmic, and systemic

Cardiomyopathy was reported in **7/9** evaluable historical patients and in approximately half of the broader 18-patient review cohort; both dilated and hypertrophic forms occur. Respiratory distress/failure, failure to thrive, feeding difficulty, optic atrophy or nystagmus, and occasional hepatic or renal failure have been reported. Suggested terms include **HP:0001638 cardiomyopathy**, **HP:0001644 dilated cardiomyopathy**, **HP:0001639 hypertrophic cardiomyopathy**, **HP:0002093 respiratory insufficiency**, **HP:0001508 failure to thrive**, **HP:0002039 feeding difficulty**, **HP:0000648 optic atrophy**, and **HP:0000639 nystagmus** (lebigot2021areviewof pages 7-9, lebigot2021areviewof pages 11-13).

### Laboratory phenotype

Historical frequencies were elevated lactate **11/12**, elevated glycine **8/8**, reduced respiratory-chain complex I/II activity **10/12**, and reduced pyruvate-dehydrogenase activity **6/7**. Suggested HPO terms are **HP:0002151 increased serum lactate**, **HP:0002148 hypoglycemia only if observed**, **HP:0001992 metabolic acidosis**, and **HP:0002154 hyperglycinemia**. Normal lactate or respiratory-chain testing does not exclude MMDS2: the recovery case had elevated plasma/urine glycine but normal CSF glycine and lactate and normal conventional respiratory-chain assays, while fibroblast PDH was only 20% of control (stutterd2019severeleukoencephalopathywith pages 4-6, stutterd2019severeleukoencephalopathywith pages 2-4).

### Quality of life

No MMDS2-specific EQ-5D, SF-36, PROMIS, or caregiver-burden study was identified. Severe disease causes profound dependence through motor/cognitive regression, feeding and respiratory support needs, seizures, and cardiac disease. This functional burden is clinically evident but has not been measured with validated instruments.

## 4. Genetic and molecular information

**BOLA3** encodes a mitochondrial BolA-family Fe–S cluster delivery protein. Reported variants include c.123dupA (p.Glu42Argfs*13), c.136C>T (p.Arg46*), c.159dupT (p.Asp54*), c.176G>A (p.Cys59Tyr), c.200T>A (p.Ile67Asn), c.220_222del (p.Glu74del), c.225_229del (p.Lys75Asnfs*9), c.287A>G (p.His96Arg), and c.295C>T (p.Arg99Trp). Transcript versions differ among reports, so every knowledge-base import should retain the source transcript and remap to a current MANE transcript (lebigot2021areviewof pages 7-9, lebigot2021areviewof pages 9-11).

Variant-level consequences include:

- **p.Arg46\*** and other premature-termination/frameshift alleles: expected loss of function through truncation and/or nonsense-mediated decay; variant-specific RNA/protein quantification was not retrieved.
- **p.Cys59Tyr:** Cys59 normally ligates the BOLA3–GLRX5 [2Fe–2S] cluster. The variant perturbs the cluster environment and creates an aberrant apo interaction but retains partial function: [4Fe–4S]-bound NFU1 reached **25% versus 65% with wild type** (saudino2021molecularbasisof pages 1-2, saudino2021molecularbasisof pages 11-12).
- **p.Ile67Asn:** leaves the global fold largely intact but essentially eliminates measurable GLRX5 binding and prevents normal heterocomplex assembly; BOLA3 homodimer cluster exchange remains possible (sen2021biochemicalimpactof pages 1-2, sen2021biochemicalimpactof pages 7-8).
- **p.His96Arg:** preserves BOLA3–GLRX5 association but produces an aberrant Fe–S complex unable to assemble a [4Fe–4S] cluster on NFU1 (bargagna2023understandingthemolecular pages 1-2).
- **p.Arg99Trp:** associated with longer survival and absence of reported cardiomyopathy in one patient, but direct functional proof and replication are limited (lebigot2021areviewof pages 11-13).

Current ClinVar ACMG classifications and exact gnomAD/TOPMed allele frequencies were not retrieved and should be queried contemporaneously before variant curation. All disease-causing alleles are germline; no somatic mechanism is implicated. No validated modifier gene, disease-specific epigenetic signature, recurrent structural chromosome abnormality, or anticipation has been demonstrated.

## 5. Environmental information

MMDS2 is not caused by toxins, radiation, pollution, lifestyle, or infection. No reproducible relationship with smoking, alcohol, exercise, diet, occupational exposure, or pathogen has been reported. Environmental stress may modulate the timing of decompensation in a genetically affected child, but direct MMDS2 data are insufficient. Consequently, CTD-style chemical–disease associations should not be interpreted as causal without BOLA3-specific human evidence.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic pathogenic BOLA3 variation leads to** absent, unstable, or functionally defective mitochondrial BOLA3.
2. **Defective BOLA3 leads to** impaired formation or function of the GLRX5–BOLA3 [2Fe–2S] carrier complex.
3. **Impaired carrier function leads to** defective transfer and reductive coupling of Fe–S clusters on NFU1 and impaired maturation of downstream [4Fe–4S] proteins (demonstrated biochemically).
4. **Defective Fe–S delivery leads to** reduced activities/assembly of respiratory-chain complexes, aconitase, lipoic-acid synthase, ETF–ubiquinone oxidoreductase, and other Fe–S clients.
5. **Reduced lipoic-acid synthase function leads to** deficient lipoylation of PDH, α-ketoglutarate dehydrogenase, branched-chain ketoacid dehydrogenase, and glycine-cleavage-system components.
6. **These enzyme deficiencies lead to** reduced oxidative ATP production, pyruvate/lactate accumulation, impaired glycine cleavage and hyperglycinemia, and broad metabolic inflexibility.
7. **In parallel, defective GLRX5–BOLA3 Fe–S delivery leads to** unstable Fe–S-containing mitoribosomes and attenuated mitochondrial translation, further reducing OXPHOS assembly; this branch was newly demonstrated in 2023.
8. **Energy failure and metabolite imbalance lead to** dysfunction and injury in high-demand oligodendroglial/neural, cardiac-muscle, skeletal-muscle, and respiratory tissues; the exact basis of selective white-matter vulnerability is partly inferred.
9. **Tissue dysfunction results in** leukodystrophy, developmental regression, hypotonia/weakness, seizures, cardiomyopathy, respiratory failure, and—at the severe end—multiorgan failure and early death.

The experimentally supported GLRX5–BOLA3–NFU1 pathway transfers two [2Fe–2S] clusters to NFU1, where reductive coupling forms a [4Fe–4S] cluster. Cys59 and His96 in BOLA3 participate directly in heterocomplex cluster coordination (bargagna2023understandingthemolecular pages 1-2, saudino2021molecularbasisof pages 1-2, saudino2021molecularbasisof pages 11-12).

**Latest major development (2023).** Zhong et al., published online **12 October 2023**, found that the GLRX5–BOLA3 node supplies Fe–S clusters to both mitoribosomal subunits. BOLA3/related-factor silencing reduced mitochondrial translation to **60–70% of control**; after five days, mitoribosomal ⁵⁵Fe incorporation was virtually undetectable with BOLA3 depletion. BOLA3-mutant patient fibroblasts also had attenuated mitochondrial protein synthesis and defective assembled OXPHOS complexes (DOI: https://doi.org/10.1093/nar/gkad842) (zhong2023bola3andnfu1 pages 9-11, zhong2023bola3andnfu1 pages 1-2).

A concise exact quotation from that abstract is: **“the mitoribosome receives its [2Fe-2S] clusters from the GLRX5-BOLA3 node.”** The authors further report that patient fibroblasts **“display previously unrecognized attenuation of mitochondrial protein synthesis.”** These results expand MMDS2 from a conventional Fe–S-client/lipoylation disorder to a combined Fe–S delivery and mitochondrial-translation disorder (zhong2023bola3andnfu1 pages 1-2).

Suggested ontology annotations include **GO:0016226 iron–sulfur cluster assembly**, **GO:0051539 4 iron, 4 sulfur cluster binding**, **GO:0006120 mitochondrial electron transport**, **GO:0006412 translation**, **GO:0032543 mitochondrial translation**, **GO:0006096 glycolytic process**, **GO:0009060 aerobic respiration**, and **GO:0044281 small-molecule metabolic process**. Relevant compartments are **GO:0005739 mitochondrion**, **GO:0005759 mitochondrial matrix**, **GO:0005761 mitochondrial ribosome**, and **GO:0005743 mitochondrial inner membrane**.

Cell-type assignments are inferential rather than single-cell validated: **CL:0000128 oligodendrocyte**, **CL:0000540 neuron**, **CL:0000746 cardiac muscle cell**, **CL:0000187 muscle cell**, and **CL:0000115 endothelial cell**. No MMDS2 single-cell, spatial-transcriptomic, lipidomic, or integrated patient multi-omics study was identified.

## 7. Anatomical structures affected

The central nervous system is the dominant organ system, especially cerebral periventricular/deep white matter, corpus callosum, and sometimes brainstem, cerebellum and spinal cord. Suggested anatomy terms include **UBERON:0000955 brain**, **UBERON:0002316 white matter**, **UBERON:0002336 corpus callosum**, **UBERON:0002240 spinal cord**, **UBERON:0002037 cerebellum**, and **UBERON:0002298 brainstem**. Cardiac, skeletal-muscle, respiratory, hepatic, renal, and ophthalmic involvement is variable; suggested terms include **UBERON:0000948 heart**, **UBERON:0001134 skeletal muscle tissue**, **UBERON:0002048 lung**, **UBERON:0002107 liver**, **UBERON:0002113 kidney**, and **UBERON:0000966 retina** (lebigot2021areviewof pages 7-9, lebigot2021areviewof pages 9-11).

At the subcellular level, the initiating lesion is in the mitochondrial matrix Fe–S assembly/delivery machinery, with downstream effects on the inner-membrane respiratory chain and mitochondrial ribosome. MRI abnormalities are usually bilateral; no consistent left/right lateralization is characteristic.

## 8. Temporal development

Classical disease begins congenitally or during the first year, often with developmental delay followed by rapid regression and progressive multisystem deterioration. Prior reported onset ranged from birth to eight months in one comparison; severe cases died between three months and early childhood. Later onset does occur: the recovery case presented at 18 months, while another reviewed patient had onset around 22 months and survived to 11 years (stutterd2019severeleukoencephalopathywith pages 4-6, lebigot2021areviewof pages 7-9).

No validated stages exist. A practical descriptive course is: (1) presymptomatic/early developmental vulnerability, (2) metabolic-neurological presentation, (3) progressive leukodystrophy and multisystem involvement, and (4) respiratory/cardiac/multiorgan end stage. This is not a formal staging system. Remission is generally absent, but mutation-dependent stabilization or recovery is possible. The developmental period of rapid myelination may represent a critical vulnerability window; this remains mechanistic inference rather than proven epidemiology (stutterd2019severeleukoencephalopathywith pages 6-7).

## 9. Inheritance and population

Inheritance is autosomal recessive. A 2021 review found **18 affected individuals from 14 families worldwide**, emphasizing extreme rarity rather than defining prevalence. No reliable incidence per 100,000, prevalence, carrier frequency, sex ratio, ethnic enrichment, or geographic distribution is available (lebigot2021areviewof pages 11-13).

Penetrance for clearly damaging biallelic variants appears high among reported families, but it has not been formally estimated. Expressivity is variable, ranging from fatal infantile disease to survival into later childhood with recovery or residual deficits. No anticipation is expected. Germline mosaicism has not been established, although standard counseling should acknowledge a small residual recurrence risk if an apparently de novo allele is encountered. Founder effects remain possible for recurrent alleles but were not established by the retrieved MMDS2 evidence.

## 10. Diagnostics

### Recommended approach

1. **Clinical suspicion:** infantile regression or weakness plus leukodystrophy, unexplained cardiomyopathy, respiratory disease, lactic acidosis, or hyperglycinemia.
2. **Biochemical testing:** plasma lactate, pyruvate, glycine, glucose, blood gas, ammonia, liver/renal indices; plasma amino acids; urine organic acids/acylglycines; CSF lactate and glycine where clinically justified. Normal lactate does not exclude disease.
3. **Imaging:** brain MRI with diffusion and, where available, proton MRS; consider spinal imaging if signs indicate.
4. **Systems assessment:** ECG/echocardiography, respiratory assessment, ophthalmology, feeding/nutrition, hearing, and developmental evaluation.
5. **Genetic confirmation:** a nuclear mitochondrial-disease, Fe–S-biogenesis, metabolic-encephalopathy, or leukodystrophy panel that includes BOLA3, or trio WES/WGS. Confirm phase and segregation by parental testing.
6. **Functional resolution:** for VUSs, consider RNA analysis, BOLA3 protein/interaction studies, respiratory-chain enzymology, PDH activity, immunoblotting of OXPHOS subunits, and protein lipoylation in fibroblasts or muscle through a specialist laboratory.

Trio WGS identified the Arg46*/Cys59Tyr genotype in the recovery case, illustrating the value of genome-scale testing when enzyme assays are nondiagnostic (stutterd2019severeleukoencephalopathywith pages 1-2, stutterd2019severeleukoencephalopathywith pages 2-4). CMA, karyotyping, FISH, repeat-expansion testing, and isolated mtDNA sequencing do not directly test the usual MMDS2 mechanism, although mtDNA analysis may be appropriate in the broader differential.

### Differential diagnosis

Important alternatives are MMDS1/NFU1, MMDS3/IBA57, ISCA2- and ISCA1-related MMDS, PMPCB disease, primary pyruvate-dehydrogenase deficiency, nonketotic hyperglycinemia caused by GLDC/AMT/GCSH, other mitochondrial respiratory-chain disorders, and genetic cavitating leukodystrophies. BOLA3 sequencing and segregation provide definitive etiologic discrimination; biochemical overlap is substantial (lebigot2021areviewof pages 1-2).

There are no validated disease-specific diagnostic criteria, newborn-screening program, or population-screening assay. Cascade testing of relatives is appropriate after a familial genotype is established.

## 11. Outcome and prognosis

Classical MMDS2 has high infantile/early-childhood mortality, but formal survival curves do not exist. In one historical compilation, survival ranged from **3 months to 11 years**, and **0/10** evaluable previous patients had documented recovery. The Arg46*/Cys59Tyr patient was alive at eight years after apparent clinical recovery and substantial MRI improvement; an Arg99Trp patient reportedly survived to 12 years (stutterd2019severeleukoencephalopathywith pages 4-6, stutterd2019severeleukoencephalopathywith pages 1-2, lebigot2021areviewof pages 11-13).

Poor-prognosis features plausibly include neonatal onset, profound lactic acidosis, severe cardiomyopathy, respiratory failure, multiorgan disease, and genotypes abolishing BOLA3 function. Residual-function missense alleles may predict a milder course, but the number of observations is too small for clinical prediction. No validated prognostic biomarker, five- or ten-year survival statistic, life-expectancy estimate, or quality-of-life dataset exists.

## 12. Treatment and real-world implementation

No approved or proven disease-modifying treatment exists. Published practice is supportive and multidisciplinary:

- seizure treatment (**NCIT:C15313 anticonvulsant therapy**);
- ventilation/oxygen and respiratory support (**NCIT:C71576 supportive care**, broad mapping);
- standard cardiomyopathy/heart-failure management;
- correction of dehydration and severe acid–base disturbances;
- enteral nutritional support when needed;
- physical, occupational, speech, feeding, and developmental therapies (**NCIT:C15302 rehabilitation therapy**, broad mapping);
- avoidance of prolonged fasting and prompt treatment of intercurrent illness as general mitochondrial-disease precautions, although MMDS2-specific efficacy has not been tested.

“Mitochondrial cocktails” of vitamins/cofactors have been administered without clear evidence of benefit. A possible partial response to methylprednisolone was anecdotal and does not justify routine immunosuppression (stutterd2019severeleukoencephalopathywith pages 6-7, lebigot2021areviewof pages 11-13). A direct ClinicalTrials.gov search found no relevant MMDS2-specific interventional study or NCT identifier.

Gene replacement, mRNA delivery, or editing is conceptually attractive because MMDS2 is monogenic, but no BOLA3-directed clinical therapy was identified. The 2023 mitoribosome findings and variant-resolved Fe–S-transfer assays provide potential pharmacodynamic platforms, not current treatments (zhong2023bola3andnfu1 pages 9-11, zhong2023bola3andnfu1 pages 1-2).

## 13. Prevention

There is no lifestyle or vaccine-based primary prevention. The principal prevention strategy is reproductive genetics:

- molecular confirmation and carrier testing in parents;
- cascade testing of adult relatives;
- preimplantation genetic testing for monogenic disease;
- prenatal diagnosis by chorionic-villus sampling or amniocentesis for known familial variants;
- donor gametes or other reproductive options after nondirective counseling.

Secondary prevention consists of early molecular diagnosis and anticipatory cardiac, respiratory, nutritional, neurological, and ophthalmic surveillance. Tertiary prevention aims to reduce aspiration, malnutrition, contractures, seizure injury, respiratory decompensation, and cardiac complications. There is no evidence-based prophylactic medication.

## 14. Other species and natural disease

BOLA/GLRX Fe–S biology is evolutionarily conserved, but no well-characterized, naturally occurring veterinary equivalent of human BOLA3-MMDS2 was identified. There is no zoonotic potential or cross-species transmission because the disorder is inherited, not infectious. Before database import, ortholog identifiers should be obtained directly from current NCBI Gene/Alliance records rather than inferred from human nomenclature.

## 15. Model organisms and experimental systems

The strongest disease-relevant systems are:

- **Patient fibroblasts:** reproduce PDH/lipoylation and OXPHOS defects and, in 2023, reduced mitochondrial translation and mitoribosome abnormalities (human ex-vivo evidence) (stutterd2019severeleukoencephalopathywith pages 2-4, zhong2023bola3andnfu1 pages 9-11).
- **Recombinant BOLA3–GLRX5–NFU1 systems:** define cluster ligands, partner recognition, transfer, and mutation-specific residual activity. These provide high mechanistic precision but cannot model organ-specific disease (in-vitro biochemical evidence) (sen2021biochemicalimpactof pages 1-2, bargagna2023understandingthemolecular pages 1-2, saudino2021molecularbasisof pages 11-12).
- **HEK293T knockdown:** BOLA3 depletion exceeding 95% reduced mitochondrial translation and Fe incorporation into mitoribosomes; useful for pathway dissection but not developmental phenotyping (cellular functional-genomics evidence) (zhong2023bola3andnfu1 pages 9-11).
- **Pulmonary-artery endothelial cells and mouse pulmonary-hypertension models:** BOLA3 loss perturbed Fe–S integrity, lipoate-dependent enzymes, respiration, glycine homeostasis, proliferation and vascular behavior. These models illuminate a BOLA3-dependent vascular mechanism but are not complete germline MMDS2 models.
- **Adipocyte knockdown models:** demonstrate requirements for mitochondrial homeostasis and oxidative metabolism but have uncertain direct relevance to the human neurological phenotype.

No validated germline BOLA3-null/knock-in mouse, zebrafish, Drosophila, *C. elegans*, organoid, or iPSC model that comprehensively recapitulates human MMDS2 was established in the retrieved literature. Complete loss may also create embryonic or perinatal viability limitations; that possibility requires empirical confirmation.

## Evidence assessment and key references

The most authoritative quantitative clinical synthesis available in the retrieved literature is the 2021 systematic review (DOI: https://doi.org/10.3390/biomedicines9080989), but its denominators vary because records were incomplete. The landmark genetic/biochemical report is Cameron et al., 2011, **PMID: 21944046**, DOI: https://doi.org/10.1016/j.ajhg.2011.08.011. The recovery case is Stutterd et al., published January 2019, DOI: https://doi.org/10.1007/8904_2018_100 (OpenTargets Search: multiple mitochondrial dysfunctions syndrome 2-BOLA3, stutterd2019severeleukoencephalopathywith pages 1-2, lebigot2021areviewof pages 11-13).

Variant-mechanism studies include Cys59Tyr (published May 2021; DOI: https://doi.org/10.3390/ijms22094848), Ile67Asn (published March 2021; DOI: https://doi.org/10.1093/mtomcs/mfab010), and His96Arg (published July 2023; DOI: https://doi.org/10.3390/ijms241411734) (sen2021biochemicalimpactof pages 1-2, bargagna2023understandingthemolecular pages 1-2, saudino2021molecularbasisof pages 1-2). The latest major disease-specific mechanistic advance within the requested 2023–2024 window is Zhong et al., 2023 (DOI: https://doi.org/10.1093/nar/gkad842); no comparably direct 2024 human MMDS2 study was identified (zhong2023bola3andnfu1 pages 1-2).

Important limitations are the minute, ascertainment-biased cohort; inconsistent transcript notation; missing population allele-frequency and contemporary ClinVar data; variable laboratory methods; no controlled therapy study; and no disease-specific epidemiology, patient-reported outcome, single-cell, spatial, or longitudinal registry dataset. Accordingly, numerical phenotype frequencies describe published cases—not population risks—and genotype–prognosis conclusions should remain provisional.

References

1. (OpenTargets Search: multiple mitochondrial dysfunctions syndrome 2-BOLA3): Open Targets Query (multiple mitochondrial dysfunctions syndrome 2-BOLA3, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (stutterd2019severeleukoencephalopathywith pages 1-2): C. Stutterd, N. Lake, H. Peters, H. Peters, P. Lockhart, R. Taft, M. Knaap, A. Vanderver, A. Vanderver, D. Thorburn, Cas Simons, R. Leventer, and R. Leventer. Severe leukoencephalopathy with clinical recovery caused by recessive bola3 mutations. JIMD reports, 43:63-70, Jan 2019. URL: https://doi.org/10.1007/8904\_2018\_100, doi:10.1007/8904\_2018\_100. This article has 15 citations and is from a peer-reviewed journal.

3. (lebigot2021areviewof pages 7-9): Elise Lebigot, Manuel Schiff, and Marie-Pierre Golinelli-Cohen. A review of multiple mitochondrial dysfunction syndromes, syndromes associated with defective fe-s protein maturation. Aug 2021. URL: https://doi.org/10.3390/biomedicines9080989, doi:10.3390/biomedicines9080989. This article has 35 citations.

4. (stutterd2019severeleukoencephalopathywith pages 2-4): C. Stutterd, N. Lake, H. Peters, H. Peters, P. Lockhart, R. Taft, M. Knaap, A. Vanderver, A. Vanderver, D. Thorburn, Cas Simons, R. Leventer, and R. Leventer. Severe leukoencephalopathy with clinical recovery caused by recessive bola3 mutations. JIMD reports, 43:63-70, Jan 2019. URL: https://doi.org/10.1007/8904\_2018\_100, doi:10.1007/8904\_2018\_100. This article has 15 citations and is from a peer-reviewed journal.

5. (lebigot2021areviewof pages 11-13): Elise Lebigot, Manuel Schiff, and Marie-Pierre Golinelli-Cohen. A review of multiple mitochondrial dysfunction syndromes, syndromes associated with defective fe-s protein maturation. Aug 2021. URL: https://doi.org/10.3390/biomedicines9080989, doi:10.3390/biomedicines9080989. This article has 35 citations.

6. (stutterd2019severeleukoencephalopathywith pages 4-6): C. Stutterd, N. Lake, H. Peters, H. Peters, P. Lockhart, R. Taft, M. Knaap, A. Vanderver, A. Vanderver, D. Thorburn, Cas Simons, R. Leventer, and R. Leventer. Severe leukoencephalopathy with clinical recovery caused by recessive bola3 mutations. JIMD reports, 43:63-70, Jan 2019. URL: https://doi.org/10.1007/8904\_2018\_100, doi:10.1007/8904\_2018\_100. This article has 15 citations and is from a peer-reviewed journal.

7. (lebigot2021areviewof pages 9-11): Elise Lebigot, Manuel Schiff, and Marie-Pierre Golinelli-Cohen. A review of multiple mitochondrial dysfunction syndromes, syndromes associated with defective fe-s protein maturation. Aug 2021. URL: https://doi.org/10.3390/biomedicines9080989, doi:10.3390/biomedicines9080989. This article has 35 citations.

8. (sen2021biochemicalimpactof pages 1-2): Sambuddha Sen, Zechariah Thompson, Christine Wachnowsky, Sean R. Cleary, Sophie R. Harvey, and J. Cowan. Biochemical impact of a disease-causing ile67asn substitution on bola3 protein. Metallomics : integrated biometal science, Mar 2021. URL: https://doi.org/10.1093/mtomcs/mfab010, doi:10.1093/mtomcs/mfab010. This article has 2 citations.

9. (bargagna2023understandingthemolecular pages 1-2): Beatrice Bargagna, Lucia Banci, and Francesca Camponeschi. Understanding the molecular basis of the multiple mitochondrial dysfunctions syndrome 2: the disease-causing his96arg mutation of bola3. Jul 2023. URL: https://doi.org/10.3390/ijms241411734, doi:10.3390/ijms241411734. This article has 1 citations.

10. (saudino2021molecularbasisof pages 1-2): Giovanni Saudino, Dafne Suraci, Veronica Nasta, Simone Ciofi-Baffoni, and Lucia Banci. Molecular basis of multiple mitochondrial dysfunctions syndrome 2 caused by cys59tyr bola3 mutation. May 2021. URL: https://doi.org/10.3390/ijms22094848, doi:10.3390/ijms22094848. This article has 10 citations.

11. (saudino2021molecularbasisof pages 11-12): Giovanni Saudino, Dafne Suraci, Veronica Nasta, Simone Ciofi-Baffoni, and Lucia Banci. Molecular basis of multiple mitochondrial dysfunctions syndrome 2 caused by cys59tyr bola3 mutation. May 2021. URL: https://doi.org/10.3390/ijms22094848, doi:10.3390/ijms22094848. This article has 10 citations.

12. (sen2021biochemicalimpactof pages 7-8): Sambuddha Sen, Zechariah Thompson, Christine Wachnowsky, Sean R. Cleary, Sophie R. Harvey, and J. Cowan. Biochemical impact of a disease-causing ile67asn substitution on bola3 protein. Metallomics : integrated biometal science, Mar 2021. URL: https://doi.org/10.1093/mtomcs/mfab010, doi:10.1093/mtomcs/mfab010. This article has 2 citations.

13. (zhong2023bola3andnfu1 pages 9-11): Hui Zhong, Alexandre Janer, Oleh Khalimonchuk, Hana Antonicka, Eric A Shoubridge, and Antoni Barrientos. Bola3 and nfu1 link mitoribosome iron–sulfur cluster assembly to multiple mitochondrial dysfunctions syndrome. Oct 2023. URL: https://doi.org/10.1093/nar/gkad842, doi:10.1093/nar/gkad842. This article has 39 citations and is from a highest quality peer-reviewed journal.

14. (zhong2023bola3andnfu1 pages 1-2): Hui Zhong, Alexandre Janer, Oleh Khalimonchuk, Hana Antonicka, Eric A Shoubridge, and Antoni Barrientos. Bola3 and nfu1 link mitoribosome iron–sulfur cluster assembly to multiple mitochondrial dysfunctions syndrome. Oct 2023. URL: https://doi.org/10.1093/nar/gkad842, doi:10.1093/nar/gkad842. This article has 39 citations and is from a highest quality peer-reviewed journal.

15. (lebigot2021areviewof pages 1-2): Elise Lebigot, Manuel Schiff, and Marie-Pierre Golinelli-Cohen. A review of multiple mitochondrial dysfunction syndromes, syndromes associated with defective fe-s protein maturation. Aug 2021. URL: https://doi.org/10.3390/biomedicines9080989, doi:10.3390/biomedicines9080989. This article has 35 citations.

16. (stutterd2019severeleukoencephalopathywith pages 6-7): C. Stutterd, N. Lake, H. Peters, H. Peters, P. Lockhart, R. Taft, M. Knaap, A. Vanderver, A. Vanderver, D. Thorburn, Cas Simons, R. Leventer, and R. Leventer. Severe leukoencephalopathy with clinical recovery caused by recessive bola3 mutations. JIMD reports, 43:63-70, Jan 2019. URL: https://doi.org/10.1007/8904\_2018\_100, doi:10.1007/8904\_2018\_100. This article has 15 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Multiple_Mitochondrial_Dysfunctions_Syndrome_2-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 8 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 60 |
| Resolved | 60 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0013675` (4 mentions) - the report calls it "if available"; MONDO calls it **multiple mitochondrial dysfunctions syndrome 2**