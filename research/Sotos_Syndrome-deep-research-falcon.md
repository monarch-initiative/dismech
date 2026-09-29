---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-05T17:55:38.598067'
end_time: '2026-09-05T18:06:56.069269'
duration_seconds: 677.47
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Sotos Syndrome
  mondo_id: MONDO:0019349
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 32
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 14
  on_topic: 9
  validator_version: 0.2.1
term_validation:
  total_terms: 72
  verified: 66
  not_found: 0
  obsolete: 2
  unverifiable: 4
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0019349
    reported_labels:
    - if available
    ontology_label: Sotos syndrome
  obsolete_terms:
  - term_id: GO:0016571
    ontology_label: obsolete histone methylation
  - term_id: GO:0006306
    ontology_label: obsolete DNA methylation
  unresolvable_prefixes:
  - Taxon
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Sotos_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Sotos Syndrome
- **MONDO ID:** MONDO:0019349 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Sotos Syndrome** covering all of the
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
- **Disease Name:** Sotos Syndrome
- **MONDO ID:** MONDO:0019349 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Sotos Syndrome** covering all of the
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


# Sotos syndrome: comprehensive disease-characteristics report

## Executive summary

Sotos syndrome is a congenital, lifelong Mendelian overgrowth–neurodevelopmental disorder caused principally by heterozygous loss of function of **NSD1**, an H3K36 histone methyltransferase. Its cardinal phenotype is distinctive facial appearance, developmental/learning disability, and childhood overgrowth—especially macrocephaly—although approximately 10% of molecularly confirmed individuals do not have overt overgrowth. Current care is supportive and surveillance-based; no disease-modifying therapy has been established. The most consequential recent advances are improved variant classification, broader sequencing-based diagnosis, recognition of neuropsychiatric and cardiovascular disease, and molecular definition of an NSD1-dependent transcriptional/DNA-methylation signature. (tattonbrown2007sotossyndrome pages 1-3, ocansey2025sotossyndrome pages 1-3, brennan2022nsd1mutationsderegulate pages 1-1, testa2023molecularanalysisand pages 1-2)

| Domain | Best-supported quantitative/current finding | Evidence type/year | Ontology-ready terms |
|---|---|---|---|
| Identifiers | Sotos syndrome; OMIM 117550; MONDO:0019349; synonym: cerebral gigantism syndrome | Curated disease resources, 2025 | MONDO:0019349; Sotos syndrome |
| Cardinal phenotypes | Distinctive facial appearance, learning/developmental disability, and childhood overgrowth occur in ≥90% of molecularly confirmed cases; overgrowth is not obligatory | Human cohort, 2005; clinical synthesis, 2025 | HP:0001513 Overgrowth; HP:0000256 Macrocephaly; HP:0001263 Global developmental delay; HP:0001622 Premature birth is **not** cardinal |
| Neonatal features | Hypotonia ~75%, poor feeding ~70%, and neonatal jaundice ~65% | Aggregated clinical cohorts, 2025 | HP:0001252 Hypotonia; HP:0011968 Feeding difficulties; HP:0000952 Jaundice |
| Growth and skeletal findings | Bone age is advanced in ~75–80% of prepubertal children; scoliosis occurs in ~30%; height often approaches the normal range after puberty, while macrocephaly usually persists | Human natural-history synthesis, 2005–2025 | HP:0005616 Accelerated skeletal maturation; HP:0002650 Scoliosis; HP:0000256 Macrocephaly |
| Neurologic and behavioral findings | Non-febrile seizures occur in ~25%; intellectual impairment varies from mild to severe and is generally stable; ASD, ADHD, anxiety, expressive-language difficulty, and sleep disturbance are recurrent | Human cohorts and review, 2024–2025 | HP:0001250 Seizure; HP:0001249 Intellectual disability; HP:0000729 Autistic behavior; HP:0007018 Attention deficit hyperactivity disorder; HP:0000739 Anxiety |
| Cardiovascular and renal complications | Historical cardiac-anomaly estimates are 15–40%; a selected 2024 molecularly confirmed cohort found heart defects in 27/45 (60%). Renal anomalies occur in ~15% | Human observational cohorts, 2024–2025 | HP:0001627 Abnormal heart morphology; HP:0000077 Abnormal renal morphology; UBERON:0000948 heart; UBERON:0002113 kidney |
| Genetics and inheritance | Heterozygous NSD1 loss-of-function variants or 5q35 deletions cause autosomal-dominant disease; ~95% are de novo and ~5% inherited. An affected individual has a 50% transmission risk | Human molecular cohorts and curated synthesis, 2005–2025 | NSD1; HGNC:14234; 5q35.3; HP:0000006 Autosomal dominant inheritance |
| Variant spectrum | Truncating, frameshift, nonsense, splice, pathogenic functional-domain missense, partial-gene deletion, and whole-gene/5q35 microdeletion variants occur. Microdeletions correlate with less prominent overgrowth and more severe learning disability | Human genotype–phenotype cohorts, 2005–2023 | SO:0001587 stop gained; SO:0001589 frameshift variant; SO:0001574 splice acceptor variant; SO:0000159 deletion |
| Molecular mechanism | NSD1 haploinsufficiency reduces H3K36 methyltransferase dosage, disturbing H3K36me1/2-directed DNA methylation and PRC2 regulation; human profiling shows promoter hypomethylation and dysregulation of bivalent developmental and neural-synapse genes | Human multi-omics plus biochemical evidence, 2011–2022 | GO:0046975 histone H3K36 methyltransferase activity; GO:0016571 histone methylation; GO:0006306 DNA methylation; GO:0040029 regulation of gene expression, epigenetic; GO:0000785 chromatin |
| Molecular diagnosis | Diagnosis is established by a heterozygous pathogenic/likely pathogenic NSD1 variant or NSD1-encompassing deletion. Testing may use sequencing plus deletion/duplication analysis, CMA, an overgrowth panel, exome, or genome sequencing | Clinical diagnostic guidance, 2023–2025 | NCIT:C15709 Genetic Testing; NCIT:C17609 Chromosomal Microarray; NCIT:C101295 Whole Exome Sequencing; NCIT:C101294 Whole Genome Sequencing |
| Recent diagnostic development | Among 1,530 clinically suspected cases, 292 (19.1%) had NSD1 findings; 115 novel intragenic variants, nine partial deletions, and 13 whole-gene microdeletions were identified. Twenty-five of 32 assessed missense VUS (78.1%) were reclassified as likely pathogenic or likely benign | Human diagnostic cohort, 2023 | NCIT:C118466 Variant Classification; NCIT:C17248 Mutation Analysis; NSD1 |
| Tumor risk and screening | Tumors are reported in approximately 3%; sacrococcygeal-teratoma/neuroblastoma risk is ~1%. Expert guidance does not recommend routine cancer screening or routine renal ultrasound because risk is insufficient and Wilms-tumor risk is not significantly increased | Cohort synthesis and expert guidance, 2017–2025 | HP:0002664 Neoplasm; NCIT:C15709 Genetic Testing; NCIT:C16210 Cancer Screening |
| Treatment and trials | No disease-modifying therapy is established. Care is individualized and supportive: developmental and educational services, speech/AAC, PT/OT, feeding support, behavioral/psychiatric care, antiseizure treatment, and organ-specific intervention. No relevant disease-modifying Sotos trial was identified | Expert guidance and trial-registry search, 2024–2025 | NCIT:C15308 Supportive Care; NCIT:C15986 Physical Therapy; NCIT:C16020 Occupational Therapy; NCIT:C17149 Speech Therapy; NCIT:C61577 Anticonvulsant Therapy |
| Mouse model | Nsd1+/− mice have ~50% lower cortical Nsd1 expression, impaired social novelty and fewer pup ultrasonic vocalizations, but no overgrowth, macrocephaly, gross cortical enlargement, or active-place-avoidance deficit. Nsd1−/− embryos die by approximately E10.5 with early patterning/forebrain abnormalities | Genetically engineered mouse, 2020–2021 | NCBITaxon:10090 Mus musculus; GO:0009790 embryo development; GO:0021987 cerebral cortex development; CL:0000540 neuron |


*Table: Concise evidence matrix summarizing the best-supported clinical, genetic, mechanistic, diagnostic, management, and model-organism findings for Sotos syndrome. Ontology-ready terms are included to support structured knowledge-base annotation.*

## 1. Disease information

**Definition.** Sotos syndrome is an autosomal-dominant overgrowth syndrome characterized by (1) a distinctive long, narrow facial gestalt with a broad/prominent forehead and pointed chin, (2) learning disability or developmental delay, and (3) childhood overgrowth, usually including macrocephaly. The face is often recognizable at birth, most characteristic at ages 1–6 years, and subtler in adulthood. A landmark molecular cohort found facial dysmorphism, learning disability, and childhood overgrowth in approximately 90% of 239 NSD1-positive individuals. (baujat2007sotossyndrome pages 1-2, ocansey2025sotossyndrome pages 5-7, tattonbrown2007sotossyndrome pages 1-3)

**Identifiers and terminology.** Recommended knowledge-base identifiers are **MONDO:0019349**, **OMIM #117550**, and the preferred name *Sotos syndrome*. Common synonyms include **cerebral gigantism** and **Sotos syndrome 1**. Open Targets maps MONDO:0019349 most strongly to NSD1 (Ensembl ENSG00000165671); APC2-associated “Sotos syndrome 3” and historical “Sotos syndrome 2” terminology for NFIX-related Malan syndrome should not be merged with molecularly confirmed NSD1-related Sotos syndrome. (baujat2007sotossyndrome pages 1-2, OpenTargets Search: Sotos syndrome-NSD1, oishi2020investigatingcorticalfeatures pages 1-5)

No single highly specific ICD-10-CM code is established; cases are commonly represented under broader congenital-malformation/overgrowth categories. ICD-11 and MeSH mappings should therefore be validated against the release used by the target database rather than inferred from the disease name.

**Evidence granularity.** The report synthesizes aggregated disease resources, molecularly confirmed cohorts, primary molecular studies, and experimental models. It is not based on an individual EHR. Individual case reports are identified as such and should not be used to estimate prevalence.

## 2. Etiology

### Causal factors and genetic risk

The primary cause is a heterozygous pathogenic or likely pathogenic **NSD1** variant, or a 5q35 deletion encompassing NSD1, producing **haploinsufficiency**. Established classes include nonsense, frameshift, canonical splice, partial-gene deletion, whole-gene deletion, and pathogenic missense variants concentrated in functional domains. Truncating variants occur throughout the gene. In strictly phenotyped historical cohorts, an NSD1 abnormality was detectable in approximately 90–93%; the 266-person study estimated 83% intragenic variants and 10% 5q35 microdeletions among clinically diagnosed cases. (tattonbrown2007sotossyndrome pages 1-3, krossa2022lysinemethyltransferasensd1 pages 3-4, visser2016nsd1andsotos pages 12-16)

Disease-associated alleles are constitutional/germline, usually de novo, and are expected to be absent or exceptionally rare in population databases. A common allele is not compatible with a fully penetrant, severe dominant developmental disorder. Somatic NSD1 alterations and NUP98–NSD1 fusions occur in cancers but are biologically distinct from germline Sotos syndrome. (ocansey2025sotossyndrome pages 1-3, brennan2022nsd1mutationsderegulate pages 1-1)

### Environmental, lifestyle, infectious, and protective factors

There is no established environmental, lifestyle, toxic, occupational, dietary, or infectious cause of Sotos syndrome. Maternal pre-eclampsia has been reported as an associated pregnancy feature, but it is not proven to cause the disorder. No validated genetic or environmental protective factor prevents phenotypic expression after an NSD1 pathogenic variant is present. Likewise, no reproducible gene–environment interaction explains disease occurrence. Phenotypic variability within families suggests contributions from background genotype, development, and possibly environment, but these remain unquantified. (tattonbrown2007sotossyndrome pages 1-3, saugierveber2007heterogeneityofnsd1 pages 10-10)

## 3. Phenotypes

The following are ontology-ready core annotations; frequencies are approximate because ascertainment and age differ between cohorts.

* **Overgrowth/tall stature** — physical sign, usually prenatal or early childhood; **HP:0001513**. Height and/or head circumference is ≥2 SD in about 90%, but either may be normal in approximately 10%. Linear growth commonly becomes less extreme after puberty. (ocansey2025sotossyndrome pages 5-7, tattonbrown2007sotossyndrome pages 1-3)
* **Macrocephaly/macrodolichocephaly** — congenital/childhood sign, **HP:0000256** and **HP:0000268**. It generally persists even when adult height normalizes; 18/21 adults in one molecularly confirmed series had head circumference above the 97th centile. (tattonbrown2007sotossyndrome pages 1-3, fickie2011adultswithsotos pages 4-5)
* **Characteristic facial morphology** — congenital physical manifestation; suggested terms include **HP:0011220** prominent forehead, **HP:0000343** long face, **HP:0000307** pointed chin, and **HP:0000272** malar flattening. It is most diagnostically useful at ages 1–6 years. (ocansey2025sotossyndrome pages 5-7, tattonbrown2007sotossyndrome pages 1-3)
* **Developmental delay/learning or intellectual disability** — developmental/behavioral phenotype; **HP:0001263**, **HP:0001249**, and **HP:0000750**. Severity ranges from mild/borderline to severe and is generally non-progressive. Expressive language, motor coordination, adaptive function, education, and independent living may be affected. (ocansey2025sotossyndrome pages 5-7, lesinskiene2024neuropsychiatricaspectsof pages 1-2)
* **Neonatal hypotonia and feeding difficulty** — early symptoms/signs; **HP:0001252**, **HP:0011968**. Approximate frequencies are 75% and 70%, respectively; they can impair oral safety, growth, and caregiver quality of life. (ocansey2025sotossyndrome pages 5-7, ocansey2025sotossyndrome pages 14-16)
* **Neonatal jaundice** — laboratory/clinical sign, **HP:0000952**, approximately 65%. (ocansey2025sotossyndrome pages 5-7)
* **Advanced bone age** — imaging sign, **HP:0005616**, approximately 75–80% of prepubertal children; historical estimates range from 74–100%. It is supportive but neither necessary nor sufficient for diagnosis. (baujat2007sotossyndrome pages 1-2, ocansey2025sotossyndrome pages 5-7)
* **Seizures** — episodic neurologic symptom, **HP:0001250**; non-febrile seizures occur in roughly 25%. EEG is clinically indicated when seizures are suspected. (ocansey2025sotossyndrome pages 5-7)
* **Scoliosis** — progressive musculoskeletal sign, **HP:0002650**, approximately 30%; it can affect mobility, pain, and respiratory mechanics in severe cases. (ocansey2025sotossyndrome pages 5-7, ocansey2025sotossyndrome pages 14-16)
* **Cardiac abnormalities** — congenital structural manifestations, **HP:0001627**. Historical prevalence is 15–40%. A selected 2024 referral cohort found defects in 27/45 (60%), including septal defects, aortic anomalies, patent ductus arteriosus, valve disease, and left-ventricular non-compaction; this high estimate should not be generalized without accounting for referral ascertainment. (ocansey2025sotossyndrome pages 5-7)
* **Renal/genitourinary anomalies** — congenital signs, **HP:0000077**, about 15%. (ocansey2025sotossyndrome pages 5-7)
* **Neuroimaging abnormalities** — radiologic phenotype, often ventriculomegaly or prominent occipital horns. A reviewed imaging dataset reported trigeminal prominence in 90%, occipital-horn prominence in 75%, and ventriculomegaly in 63%; clinical significance varies. (lesinskiene2024neuropsychiatricaspectsof pages 1-2)
* **Neurobehavioral manifestations** — autistic behavior (**HP:0000729**), ADHD (**HP:0007018**), anxiety (**HP:0000739**), aggression, phobias, and sleep disturbance. The 2024 expert review stresses slow language development and multidisciplinary psychosocial care but also notes the scarcity of longitudinal data. (lesinskiene2024neuropsychiatricaspectsof pages 1-2, lesinskiene2024neuropsychiatricaspectsof pages 6-8)

No disease-specific EQ-5D, SF-36, or validated Sotos quality-of-life dataset was identified. Functional burden is driven principally by developmental disability, communication needs, behavior, seizures, feeding problems, vision problems, scoliosis, and congenital organ disease.

## 4. Genetic and molecular information

**Gene.** **NSD1** (HGNC:14234; chromosome 5q35.3; Ensembl ENSG00000165671) encodes nuclear receptor-binding SET-domain protein 1. The reported protein is 2,696 amino acids and contains two PWWP domains, five PHD zinc fingers, a C5HCH domain, SET/SAC catalytic domains, and two nuclear-receptor interaction domains. Expression is documented in fetal/adult brain, skeletal muscle, kidney, spleen, thymus, lung, and blood leukocytes. (OpenTargets Search: Sotos syndrome-NSD1, visser2016nsd1andsotos pages 1-5, ocansey2025sotossyndrome pages 16-19)

**Functional consequence.** The established disease mechanism is dosage-sensitive loss of NSD1 function. SET-domain missense substitutions may destabilize the catalytic structure or sterically disrupt S-adenosylmethionine/substrate access; PHD-domain substitutions may disturb binding to methylated H3K4/H3K9. These findings support loss of chromatin recruitment and/or H3K36 methyltransferase activity, rather than gain of function or dominant-negative activity, as the general mechanism. (ha2016stericclashin pages 16-18, liu2023anovelnonsense pages 8-8)

**Structural variants and genotype–phenotype correlation.** The principal chromosomal lesion is a 5q35.2–q35.3 deletion encompassing NSD1. In 31 deletion versus 208 intragenic-variant cases, deletions were associated with less prominent overgrowth and more severe learning disability. No consistent correlation with deletion size was found, and individuals with identical intragenic variants can differ substantially. (visser2016nsd1andsotos pages 12-16)

**Modifiers and epigenetics.** No clinically validated modifier gene is available. NSD1 loss is associated with reduced H3K36me2, genome-wide/promoter DNA hypomethylation, altered PRC2/H3K27me3 balance, and a recognizable blood episignature. Human patient profiling found that most differentially expressed genes were downregulated and enriched for bivalent developmental and neural-synapse genes. The investigators concluded that NSD1-deposited H3K36 methylation directs promoter DNA methylation partly by opposing PRC2 activity. Accelerated transcriptional and DNA-methylation age was also observed, but its prognostic meaning is unknown. (krossa2022lysinemethyltransferasensd1 pages 3-4, brennan2022nsd1mutationsderegulate pages 1-1)

A useful abstract quotation is: **“Most abnormally expressed genes displayed reduced expression in SS; these downregulated genes consisted mostly of bivalent genes and were enriched for regulators of development and neural synapse function.”** This is human transcriptomic/methylomic association evidence, not proof that each altered gene causes a specific clinical feature. (brennan2022nsd1mutationsderegulate pages 1-1)

## 5. Environmental information

No toxin, radiation exposure, pollutant, diet, exercise pattern, smoking, alcohol use, or pathogen is known to initiate Sotos syndrome. Ordinary health recommendations remain appropriate but do not alter the underlying germline lesion. Environmental factors may modify general health, educational attainment, behavior, and secondary complications, but disease-specific effect sizes are unavailable. Immunization follows routine age- and risk-based schedules; Sotos syndrome is neither infectious nor zoonotic.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. A heterozygous loss-of-function NSD1 variant or NSD1-encompassing 5q35 deletion **leads to** reduced functional NSD1 dosage. (tattonbrown2007sotossyndrome pages 1-3, ocansey2025sotossyndrome pages 1-3)
2. Reduced NSD1 dosage **leads to** diminished or mistargeted H3K36 mono-/dimethylation and altered chromatin-reader interactions; catalytic impairment is demonstrated biochemically/structurally for selected variants. (krossa2022lysinemethyltransferasensd1 pages 3-4, ha2016stericclashin pages 16-18, liu2023anovelnonsense pages 8-8)
3. Disturbed H3K36 methylation **results in** abnormal recruitment/crosstalk with DNA-methylation machinery and altered opposition to PRC2, producing promoter/CpG-shore hypomethylation and abnormal H3K27me3 distribution. This step is supported by human multi-omics and cellular work. (krossa2022lysinemethyltransferasensd1 pages 3-4, brennan2022nsd1mutationsderegulate pages 1-1)
4. The altered epigenetic landscape **leads to** dysregulated transcription of bivalent developmental, cell-fate, growth, and neural-synapse genes. Human blood profiling demonstrates the signature; its precise tissue-specific developmental timing remains partly inferred. (brennan2022nsd1mutationsderegulate pages 1-1)
5. During embryonic and childhood development, transcriptional dysregulation **is inferred to result in** altered proliferation, differentiation, tissue patterning, and neuronal circuit development. Complete Nsd1 loss in mice causes endodermal, mesodermal, and neurectodermal patterning defects and embryonic lethality, supporting an essential upstream developmental role. (oishi2020investigatingcorticalfeatures pages 18-21, fallah2021impairedregulationof pages 5-6)
6. **Growth branch:** developmental/growth-gene dysregulation **is inferred to lead to** prenatal/childhood overgrowth, advanced skeletal maturation, and persistent macrocephaly. The exact growth-effector pathway is unresolved; a simple GH/IGF excess mechanism has not been established. (baujat2007sotossyndrome pages 1-2, brennan2022nsd1mutationsderegulate pages 1-1)
7. **Neural branch:** neuronal and synaptic gene dysregulation **is inferred to lead to** developmental delay, intellectual disability, language impairment, autism/ADHD/anxiety, and seizure susceptibility. Predominantly neuronal Nsd1 expression and mouse social phenotypes support, but do not fully reproduce, this branch. (lesinskiene2024neuropsychiatricaspectsof pages 1-2, oishi2020investigatingcorticalfeatures pages 18-21, oishi2020investigatingcorticalfeatures pages 13-18)
8. **Organogenesis branch:** altered developmental programs **are inferred to result in** craniofacial, cardiac, renal/genitourinary, and skeletal anomalies. Direct tissue-specific human causal chains remain incompletely mapped. (ocansey2025sotossyndrome pages 5-7, visser2016nsd1andsotos pages 12-16)

**Pathway interpretation.** Sotos syndrome is primarily a chromatin/epigenetic-regulation disorder, not a canonical single-pathway RAS/MAPK, PI3K–AKT–mTOR, immune, metabolic, or lysosomal disease. Relevant GO suggestions are **GO:0046975 histone H3K36 methyltransferase activity**, **GO:0016571 histone methylation**, **GO:0006306 DNA methylation**, **GO:0040029 epigenetic regulation of gene expression**, **GO:0006355 regulation of DNA-templated transcription**, **GO:0009790 embryo development**, and **GO:0021987 cerebral cortex development**. Relevant cell terms include **CL:0000540 neuron**, **CL:0000127 astrocyte**, **CL:0000128 oligodendrocyte**, **CL:0000047 neuronal stem cell**, cardiomyocyte **CL:0000746**, chondrocyte **CL:0000138**, and osteoblast **CL:0000062**. Neurons have the strongest direct model evidence; the other cell assignments reflect affected tissues and should be marked as inferred.

No reproducible Sotos-specific proteomic, metabolomic, or lipidomic diagnostic signature was identified. Human transcriptomics and DNA methylomics are the best-developed molecular profiles.

## 7. Anatomical structures affected

The nervous system and skeleton/growth axis are principal systems; the heart, kidneys/genitourinary tract, eyes, gastrointestinal/feeding apparatus, and musculoskeletal system are variably involved. Suggested anatomical mappings include brain **UBERON:0000955**, cerebral cortex **UBERON:0000956**, cerebellum **UBERON:0002037**, skull **UBERON:0003129**, bone tissue **UBERON:0002481**, vertebral column **UBERON:0002412**, heart **UBERON:0000948**, kidney **UBERON:0002113**, and eye **UBERON:0000970**. (ocansey2025sotossyndrome pages 5-7, fickie2011adultswithsotos pages 4-5, visser2016nsd1andsotos pages 1-5)

At the subcellular level, NSD1 acts principally in the **nucleus** and on **chromatin/nucleosomes**: GO:0005634, GO:0000785, and GO:0000786. There is no established mitochondrial, lysosomal, ER-storage, or laterality-specific pathology. Most manifestations are bilateral/systemic rather than consistently unilateral.

## 8. Temporal development

Sotos syndrome is congenital, with overgrowth and macrocephaly often apparent prenatally or at birth. Hypotonia, feeding difficulty, jaundice, and occasionally hypoglycemia dominate the neonatal period. The facial gestalt is most evident from one to six years; developmental and language differences emerge in infancy/early childhood. Advanced bone age and rapid linear growth are predominantly childhood findings. (baujat2007sotossyndrome pages 1-2, ocansey2025sotossyndrome pages 5-7)

The disease is chronic and lifelong, not relapsing-remitting. Intellectual impairment is usually stable rather than neurodegenerative. Height frequently approaches the normal range after puberty, while macrocephaly persists. Scoliosis, seizures, behavioral health needs, visual disorders, and organ-specific complications may require continued adult care. Adult data remain sparse; in 21 adults, mean reported height was 182 cm in men and 174 cm in women, and almost half had ocular/visual problems. (ocansey2025sotossyndrome pages 5-7, fickie2011adultswithsotos pages 4-5)

Critical intervention periods are infancy and early childhood for feeding safety, developmental therapy, communication support, hearing/vision assessment, and educational planning; adolescence is important for scoliosis and neuropsychiatric reassessment and transition planning. There is no biological remission.

## 9. Inheritance and population

Inheritance is **autosomal dominant** (**HP:0000006**). Approximately 95% of affected individuals have a de novo alteration and about 5% have an affected parent. Each child of an affected person has a 50% transmission probability. Expressivity is highly variable, including within families. Penetrance appears high for some recognizable developmental phenotype, but a precise age-specific penetrance estimate is unavailable. (ocansey2025sotossyndrome pages 1-3, visser2016nsd1andsotos pages 12-16)

The recurrence risk to unaffected parents after an apparently de novo event is low—historically quoted as <1%—but not zero because parental germline mosaicism cannot be completely excluded. Germline mosaicism has been rarely or not convincingly documented in older series. Genetic anticipation is not established; consanguinity is not etiologically relevant; there is no carrier state in the recessive-disease sense. (baujat2007sotossyndrome pages 1-2)

The frequently cited birth incidence is approximately **1 in 14,000**, or about **7.1 per 100,000 live births**, but exact prevalence remains uncertain because of variable recognition and historical underdiagnosis. No robust annual incidence, founder effect, ethnic predilection, or sex difference is established. Microdeletions have historically been relatively common in Japanese cohorts, whereas intragenic variants predominate in European cohorts, potentially reflecting genomic architecture and ascertainment rather than different overall disease prevalence. (baujat2007sotossyndrome pages 1-2, krossa2022lysinemethyltransferasensd1 pages 3-4)

## 10. Diagnostics

### Clinical assessment

Clinical suspicion rests on the facial gestalt, developmental/learning impairment, macrocephaly/tall stature, and supportive findings such as advanced bone age. There are no universally accepted purely clinical consensus criteria, and normal height does not exclude the disease. Molecular confirmation is therefore preferred. (baujat2007sotossyndrome pages 1-2, testa2023molecularanalysisand pages 1-2)

Baseline evaluation should include serial growth and head circumference, developmental and behavioral assessment, feeding/oral-motor evaluation, cardiovascular examination with echocardiography at diagnosis, renal evaluation guided by findings, spine examination, vision and hearing assessment, and neurologic assessment. MRI, EEG, bone-age radiography, renal ultrasound, and laboratory testing are indication-driven rather than universal biochemical diagnostic tests. No serum enzyme, protein, or metabolite is diagnostic. (ocansey2025sotossyndrome pages 5-7, ocansey2025sotossyndrome pages 14-16)

### Genetic-testing algorithm

1. In a classic phenotype, perform **NSD1 sequencing plus deletion/duplication analysis**.
2. If the phenotype overlaps multiple overgrowth/intellectual-disability syndromes, use a panel including NSD1 and important differentials such as **EZH2, DNMT3A, NFIX, PTEN, SETD2, EED, SUZ12, PPP2R5D, TCF20**, and **BRWD3**.
3. Use **chromosomal microarray** to detect 5q35 deletions and other pathogenic copy-number variants, especially in patients with congenital anomalies or more severe disability.
4. Use trio **WES/WGS** when targeted testing is negative, atypical, or a blended diagnosis is suspected. WGS can capture coding, noncoding, splice, and structural lesions but is not yet necessary in every classic case.
5. RNA studies can resolve suspected splice variants; methylation episignatures may support classification of a VUS, but neither presently replaces identification of a causal genomic variant. (ocansey2025sotossyndrome pages 1-3, visser2016nsd1andsotos pages 12-16, testa2023molecularanalysisand pages 1-2)

A 2023 real-world laboratory cohort screened 1,530 unrelated suspected cases and identified NSD1 findings in 292 (19.1%), including nine partial deletions, 13 whole-gene microdeletions, and 115 novel intragenic variants. Twenty-five of 32 assessed missense VUS (78.1%) moved to likely pathogenic or likely benign, emphasizing periodic reinterpretation and phenotype–laboratory communication. The authors’ abstract states that the work demonstrates **“the utility of sharing variant classification and the need to improve communication between the laboratory staff and the referring physician.”** (testa2023molecularanalysisand pages 1-2)

Karyotyping and FISH can detect large rearrangements but have largely been superseded by CMA and sequencing/dosage methods. Mitochondrial-DNA and repeat-expansion tests are not routine for Sotos syndrome.

### Differential diagnosis and screening

Important differentials include Weaver syndrome (**EZH2**), Tatton-Brown–Rahman syndrome (**DNMT3A**), Malan syndrome (**NFIX**), Beckwith–Wiedemann spectrum, Simpson–Golabi–Behmel syndrome (**GPC3**), PTEN hamartoma-tumor syndrome, SETD2/Luscan–Lumish syndrome, Fragile X syndrome, and terminal 22q deletion. Distinguishing features include the facial gestalt, tumor spectrum, organomegaly/macroglossia, segmental overgrowth, sex-linked inheritance, and molecular findings. (baujat2007sotossyndrome pages 1-2, testa2023molecularanalysisand pages 11-13)

Sotos syndrome is not part of routine newborn biochemical screening. Cascade testing is appropriate after an inherited variant is found. Prenatal and preimplantation testing are possible once the familial variant is known, but severity cannot be predicted accurately from genotype alone. (ocansey2025sotossyndrome pages 1-3)

## 11. Outcome and prognosis

Life expectancy is believed to be near normal for most individuals without severe cardiac, neurologic, or other complications, but no reliable 5-year, 10-year, or disease-specific mortality estimates exist. Major long-term morbidity arises from intellectual/developmental disability, communication and behavioral needs, seizures, scoliosis, feeding problems, congenital heart/renal disease, and visual impairment. Adult natural-history evidence remains limited. (ocansey2025sotossyndrome pages 14-16, fickie2011adultswithsotos pages 4-5)

Tumors have been reported in approximately 3% of affected individuals, but the spectrum is heterogeneous and absolute risk is low. Expert guidance estimates the combined sacrococcygeal-teratoma/neuroblastoma risk near 1%; Wilms-tumor risk is not significantly increased. Consequently, routine tumor-marker testing, whole-body imaging, or renal ultrasound solely for cancer surveillance is not recommended. New masses, unexplained pain, neurologic change, cytopenic symptoms, or constitutional symptoms warrant ordinary prompt assessment. (ocansey2025sotossyndrome pages 5-7, ocansey2025sotossyndrome pages 14-16)

No validated molecular prognostic biomarker predicts individual cognitive, growth, seizure, or cardiac outcome. A 5q35 microdeletion is associated at group level with more severe learning disability, but genotype does not reliably predict an individual course. (visser2016nsd1andsotos pages 12-16)

## 12. Treatment

There is no approved NSD1-restoring, gene-editing, RNA, cellular, epigenetic, or other disease-modifying treatment. A ClinicalTrials.gov search identified no relevant interventional disease-modifying Sotos trial. Treatment is therefore individualized and multidisciplinary. (ocansey2025sotossyndrome pages 14-16)

* **Development:** early-intervention services, individualized education, neuropsychology, speech/language therapy, and augmentative and alternative communication. Suggested NCIT terms: **Speech Therapy**, **Educational Therapy**, **Supportive Care**.
* **Motor/orthopedic:** physical and occupational therapy; orthopedic management or surgery for progressive scoliosis, hip problems, or functional deformity. NCIT: **Physical Therapy**, **Occupational Therapy**, **Orthopedic Surgery**.
* **Feeding/GI:** feeding and swallowing assessment, texture modification, reflux/constipation treatment, nutrition support, and NG or gastrostomy feeding when required. NCIT: **Nutritional Support**, **Gastrostomy**.
* **Neurologic:** standard antiseizure medication selected by seizure type; epilepsy-surgery evaluation may be appropriate for rare focal drug-resistant epilepsy. No Sotos-specific pharmacogenomic rule is known.
* **Behavior/psychiatry:** behavioral therapy, developmental pediatrics, school supports, and standard evidence-based treatment of ADHD, anxiety, aggression, ASD-associated impairment, and sleep disturbance. (ocansey2025sotossyndrome pages 14-16, lesinskiene2024neuropsychiatricaspectsof pages 6-8)
* **Cardiac, renal, visual, hearing, and endocrine complications:** standard specialist-directed treatment. The elevated cardiac-defect yield in a 2024 molecular cohort supports a detailed echocardiogram at diagnosis and individualized cardiology follow-up. (ocansey2025sotossyndrome pages 5-7)

Growth-suppressing endocrine treatment is not routinely recommended merely for tall stature. Surgery and medications should target clinically meaningful complications rather than the syndrome label.

## 13. Prevention

**Primary prevention:** There is no vaccine, lifestyle change, or prophylactic medication that prevents a de novo NSD1 variant. Reproductive options after identification of a familial variant include genetic counseling, prenatal diagnosis, donor gametes, and preimplantation genetic testing.

**Secondary prevention:** Early molecular diagnosis, cascade testing in relatives, developmental screening, and prompt assessment of feeding, hearing, vision, heart, kidneys, spine, seizures, and behavior can reduce diagnostic delay and secondary disability. Population-wide newborn or carrier screening is not recommended because most cases are de novo and there is no validated newborn biochemical marker. (ocansey2025sotossyndrome pages 1-3, ocansey2025sotossyndrome pages 14-16)

**Tertiary prevention:** At routine visits, monitor growth/nutrition, oral safety, constipation, seizures and neurologic changes, development/education, neurobehavioral health, mobility/spine, self-care, hearing, vision, cardiovascular status, and family support. Physical therapy may reduce contractures and orthopedic complications; communication support can reduce frustration and improve participation. Routine cancer screening beyond population recommendations is not justified by current risk estimates. (ocansey2025sotossyndrome pages 14-16)

## 14. Other species and natural disease

The causal gene has conserved orthologs, including mouse **Nsd1** in *Mus musculus* (**NCBI Taxon:10090**), zebrafish orthologous NSD-family genes in *Danio rerio* (**Taxon:7955**), and fly **nsd** in *Drosophila melanogaster* (**Taxon:7227**). Human and mouse proteins have approximately 83% amino-acid identity, supporting conserved chromatin function. (fallah2021impairedregulationof pages 5-6)

No well-established naturally occurring veterinary syndrome equivalent to human NSD1-related Sotos syndrome was identified, and no breed-specific VBO association is established. The disorder has no zoonotic potential and cannot be transmitted between species. Comparative evidence comes from engineered models rather than natural animal disease.

## 15. Model organisms and experimental systems

**Constitutive mouse knockout.** Homozygous Nsd1 loss is embryonic lethal by approximately E10.5, with abnormal endodermal, mesodermal, and neurectodermal patterning, increased apoptosis, and severe forebrain/prosencephalic abnormalities. This establishes an essential role in early development but prevents postnatal study of complete loss. (oishi2020investigatingcorticalfeatures pages 18-21, fallah2021impairedregulationof pages 5-6)

**Heterozygous mouse.** A CRISPR model targeting conserved exon 3 produced a premature stop and approximately 50% reduction in cortical Nsd1 mRNA. Nsd1+/− animals showed reduced SATB2-positive upper-layer neurons in retrosplenial cortex, impaired social-novelty preference, and fewer pup ultrasonic vocalizations. They did **not** show human-like overgrowth, macrocephaly, gross cortical enlargement, hippocampal abnormality, or active-place-avoidance learning deficit. Thus, they model selected social/cortical features but have limited face and construct validity for systemic human disease. (oishi2020investigatingcorticalfeatures pages 13-18, oishi2020investigatingcorticalfeatures pages 28-36)

**Cellular systems.** Mouse embryonic stem/germ-cell studies demonstrate reduced H3K36me2 after Nsd1 loss. Patient blood and cultured-cell methylome/transcriptome analyses model the molecular episignature. Patient-derived iPSC neurons, cerebral organoids, and lineage-specific conditional knockouts are rational next-generation systems, but mature, widely validated Sotos organoid or therapeutic-screen platforms were not established in the retrieved 2023–2024 literature. (krossa2022lysinemethyltransferasensd1 pages 3-4, brennan2022nsd1mutationsderegulate pages 1-1, oishi2020investigatingcorticalfeatures pages 18-21)

**Non-mammalian models.** Drosophila nsd deletion has been reported to cause developmental abnormalities resembling selected Sotos features, but direct quantitative evidence was not available in the retrieved full text. Zebrafish are not yet a standard NSD1-Sotos model. These systems offer high-throughput functional testing but cannot reproduce the human facial gestalt, cognition, or long developmental trajectory.

## Recent-development assessment and evidence gaps

The strongest 2023–2024 development is diagnostic rather than therapeutic: large-scale NSD1 variant re-evaluation, panel/exome integration, and improved recognition of cardiac, neuroimaging, and neuropsychiatric manifestations. The 2024 neuropsychiatric review concluded that autism, ADHD, anxiety, aggressive outbursts, language delay, and altered sleep are clinically important while emphasizing the lack of longitudinal intervention research. (lesinskiene2024neuropsychiatricaspectsof pages 1-2, testa2023molecularanalysisand pages 1-2, lesinskiene2024neuropsychiatricaspectsof pages 6-8)

Important unresolved questions are: the tissue-specific route from H3K36me2 loss to overgrowth; reliable penetrance and population prevalence; adult cardiovascular and neuropsychiatric natural history; validated patient-reported quality-of-life outcomes; functional classification of many missense variants; and whether safe correction of NSD1-dependent chromatin states is therapeutically feasible. Current expert interpretation should therefore avoid treating rare case-report findings as syndrome-defining or assuming that cancer-associated NSD1 inhibitors would benefit a haploinsufficiency disorder.

References

1. (tattonbrown2007sotossyndrome pages 1-3): Katrina Tatton-Brown and Nazneen Rahman. Sotos syndrome. European Journal of Human Genetics, 15:264-271, Sep 2007. URL: https://doi.org/10.1038/sj.ejhg.5201686, doi:10.1038/sj.ejhg.5201686. This article has 348 citations and is from a domain leading peer-reviewed journal.

2. (ocansey2025sotossyndrome pages 1-3): S Ocansey, TRP Cole, and N Rahman. Sotos syndrome. Mar 2025. URL: https://doi.org/10.1002/9780470893159.ch51, doi:10.1002/9780470893159.ch51. This article has 8 citations.

3. (brennan2022nsd1mutationsderegulate pages 1-1): Kevin Brennan, Hong Zheng, Jill A Fahrner, June Ho Shin, Andrew J Gentles, Bradley Schaefer, John B Sunwoo, Jonathan A Bernstein, and Olivier Gevaert. Nsd1 mutations deregulate transcription and dna methylation of bivalent developmental genes in sotos syndrome. Human Molecular Genetics, 31:2164-2184, Jan 2022. URL: https://doi.org/10.1093/hmg/ddac026, doi:10.1093/hmg/ddac026. This article has 32 citations and is from a domain leading peer-reviewed journal.

4. (testa2023molecularanalysisand pages 1-2): Barbara Testa, Giuseppina Conteduca, Marina Grasso, Massimiliano Cecconi, Francesca Lantieri, Chiara Baldo, Alessia Arado, Laura Andraghetti, Michela Malacarne, Donatella Milani, and Domenico Coviello. Molecular analysis and reclassification of nsd1 gene variants in a cohort of patients with clinical suspicion of sotos syndrome. Genes, 14(2):295, Jan 2023. URL: https://doi.org/10.3390/genes14020295, doi:10.3390/genes14020295. This article has 16 citations.

5. (baujat2007sotossyndrome pages 1-2): Geneviève Baujat and Valérie Cormier-Daire. Sotos syndrome. Orphanet Journal of Rare Diseases, 2:36-36, Sep 2007. URL: https://doi.org/10.1186/1750-1172-2-36, doi:10.1186/1750-1172-2-36. This article has 193 citations and is from a peer-reviewed journal.

6. (ocansey2025sotossyndrome pages 5-7): S Ocansey, TRP Cole, and N Rahman. Sotos syndrome. Mar 2025. URL: https://doi.org/10.1002/9780470893159.ch51, doi:10.1002/9780470893159.ch51. This article has 8 citations.

7. (OpenTargets Search: Sotos syndrome-NSD1): Open Targets Query (Sotos syndrome-NSD1, 9 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

8. (oishi2020investigatingcorticalfeatures pages 1-5): Sabrina Oishi, Oressia Zalucki, Michelle S. Vega, Danyon Harkins, Tracey J. Harvey, Maria Kasherman, Raul A. Davila, Lauren Hale, Melissa White, Sandra Piltz, Paul Thomas, Thomas H. J. Burne, Lachlan Harris, and Michael Piper. Investigating cortical features of sotos syndrome using mice heterozygous for <i>nsd1</i>. Jan 2020. URL: https://doi.org/10.1111/gbb.12637, doi:10.1111/gbb.12637. This article has 28 citations.

9. (krossa2022lysinemethyltransferasensd1 pages 3-4): Imène Krossa, Thomas Strub, Andrew E. Aplin, Robert Ballotti, and Corine Bertolotto. Lysine methyltransferase nsd1 and cancers: any role in melanoma? Oct 2022. URL: https://doi.org/10.3390/cancers14194865, doi:10.3390/cancers14194865. This article has 6 citations.

10. (visser2016nsd1andsotos pages 12-16): Remco Visser and Naomichi Matsumoto. Nsd1 and sotos syndrome. ArXiv, pages 1015-1020, Jun 2016. URL: https://doi.org/10.1093/med/9780199934522.003.0152, doi:10.1093/med/9780199934522.003.0152. This article has 5 citations.

11. (saugierveber2007heterogeneityofnsd1 pages 10-10): Pascale Saugier-Veber, Céline Bonnet, Alexandra Afenjar, Valérie Drouin-Garraud, Christine Coubes, Séverine Fehrenbach, Muriel Holder-Espinasse, Joëlle Roume, Valérie Malan, Marie-France Portnoi, Nicolas Jeanne, Clarisse Baumann, Delphine Héron, Albert David, Marion Gérard, Dominique Bonneau, Didier Lacombe, Valérie Cormier-Daire, Thierry Billette de Villemeur, Thierry Frébourg, and Lydie Bürglen. Heterogeneity of nsd1 alterations in 116 patients with sotos syndrome. Human Mutation, 28:1098-1107, Nov 2007. URL: https://doi.org/10.1002/humu.20568, doi:10.1002/humu.20568. This article has 81 citations and is from a domain leading peer-reviewed journal.

12. (fickie2011adultswithsotos pages 4-5): Matthew R. Fickie, Pablo Lapunzina, Jennifer K. Gentile, Nina Tolkoff‐Rubin, Daniela Kroshinsky, Enrique Galan, Esther Gean, Loreto Martorell, Valeria Romanelli, Joaquín Fernandez Toral, and Angela E. Lin. Adults with sotos syndrome: review of 21 adults with molecularly confirmed nsd1 alterations, including a detailed case report of the oldest person. American Journal of Medical Genetics Part A, 155:2105-2111, Sep 2011. URL: https://doi.org/10.1002/ajmg.a.34156, doi:10.1002/ajmg.a.34156. This article has 50 citations.

13. (lesinskiene2024neuropsychiatricaspectsof pages 1-2): Sigita Lesinskiene, Reda Montvilaite, Kamile Pociute, Ausra Matuleviciene, and Algirdas Utkus. Neuropsychiatric aspects of sotos syndrome: explorative review building multidisciplinary bridges in clinical practice. Apr 2024. URL: https://doi.org/10.3390/jcm13082204, doi:10.3390/jcm13082204. This article has 13 citations.

14. (ocansey2025sotossyndrome pages 14-16): S Ocansey, TRP Cole, and N Rahman. Sotos syndrome. Mar 2025. URL: https://doi.org/10.1002/9780470893159.ch51, doi:10.1002/9780470893159.ch51. This article has 8 citations.

15. (lesinskiene2024neuropsychiatricaspectsof pages 6-8): Sigita Lesinskiene, Reda Montvilaite, Kamile Pociute, Ausra Matuleviciene, and Algirdas Utkus. Neuropsychiatric aspects of sotos syndrome: explorative review building multidisciplinary bridges in clinical practice. Apr 2024. URL: https://doi.org/10.3390/jcm13082204, doi:10.3390/jcm13082204. This article has 13 citations.

16. (visser2016nsd1andsotos pages 1-5): Remco Visser and Naomichi Matsumoto. Nsd1 and sotos syndrome. ArXiv, pages 1015-1020, Jun 2016. URL: https://doi.org/10.1093/med/9780199934522.003.0152, doi:10.1093/med/9780199934522.003.0152. This article has 5 citations.

17. (ocansey2025sotossyndrome pages 16-19): S Ocansey, TRP Cole, and N Rahman. Sotos syndrome. Mar 2025. URL: https://doi.org/10.1002/9780470893159.ch51, doi:10.1002/9780470893159.ch51. This article has 8 citations.

18. (ha2016stericclashin pages 16-18): Kyungsoo Ha, Priya Anand, Jennifer Lee, Julie Jones, Chong Kim, Debora Bertola, Jonathan Labonne, Lawrence Layman, Wolfgang Wenzel, and Hyung-Goo Kim. Steric clash in the set domain of histone methyltransferase nsd1 as a cause of sotos syndrome and its genetic heterogeneity in a brazilian cohort. Genes, Nov 2016. URL: https://doi.org/10.3390/genes7110096, doi:10.3390/genes7110096. This article has 15 citations.

19. (liu2023anovelnonsense pages 8-8): Xinting Liu, Chen Chen, Lin Wan, Gang Zhu, Yan Zhao, Lizhu Hu, Yan Liang, Jing Gao, Jing Wang, and Guang Yang. A novel nonsense variant in nsd1 gene in a female child with sotos syndrome: a case report and literature review. Brain and Behavior, Oct 2023. URL: https://doi.org/10.1002/brb3.3290, doi:10.1002/brb3.3290. This article has 6 citations and is from a peer-reviewed journal.

20. (oishi2020investigatingcorticalfeatures pages 18-21): Sabrina Oishi, Oressia Zalucki, Michelle S. Vega, Danyon Harkins, Tracey J. Harvey, Maria Kasherman, Raul A. Davila, Lauren Hale, Melissa White, Sandra Piltz, Paul Thomas, Thomas H. J. Burne, Lachlan Harris, and Michael Piper. Investigating cortical features of sotos syndrome using mice heterozygous for <i>nsd1</i>. Jan 2020. URL: https://doi.org/10.1111/gbb.12637, doi:10.1111/gbb.12637. This article has 28 citations.

21. (fallah2021impairedregulationof pages 5-6): Merrick S. Fallah, Dora Szarics, Clara M. Robson, and James H. Eubanks. Impaired regulation of histone methylation and acetylation underlies specific neurodevelopmental disorders. Frontiers in Genetics, Jan 2021. URL: https://doi.org/10.3389/fgene.2020.613098, doi:10.3389/fgene.2020.613098. This article has 65 citations and is from a peer-reviewed journal.

22. (oishi2020investigatingcorticalfeatures pages 13-18): Sabrina Oishi, Oressia Zalucki, Michelle S. Vega, Danyon Harkins, Tracey J. Harvey, Maria Kasherman, Raul A. Davila, Lauren Hale, Melissa White, Sandra Piltz, Paul Thomas, Thomas H. J. Burne, Lachlan Harris, and Michael Piper. Investigating cortical features of sotos syndrome using mice heterozygous for <i>nsd1</i>. Jan 2020. URL: https://doi.org/10.1111/gbb.12637, doi:10.1111/gbb.12637. This article has 28 citations.

23. (testa2023molecularanalysisand pages 11-13): Barbara Testa, Giuseppina Conteduca, Marina Grasso, Massimiliano Cecconi, Francesca Lantieri, Chiara Baldo, Alessia Arado, Laura Andraghetti, Michela Malacarne, Donatella Milani, and Domenico Coviello. Molecular analysis and reclassification of nsd1 gene variants in a cohort of patients with clinical suspicion of sotos syndrome. Genes, 14(2):295, Jan 2023. URL: https://doi.org/10.3390/genes14020295, doi:10.3390/genes14020295. This article has 16 citations.

24. (oishi2020investigatingcorticalfeatures pages 28-36): Sabrina Oishi, Oressia Zalucki, Michelle S. Vega, Danyon Harkins, Tracey J. Harvey, Maria Kasherman, Raul A. Davila, Lauren Hale, Melissa White, Sandra Piltz, Paul Thomas, Thomas H. J. Burne, Lachlan Harris, and Michael Piper. Investigating cortical features of sotos syndrome using mice heterozygous for <i>nsd1</i>. Jan 2020. URL: https://doi.org/10.1111/gbb.12637, doi:10.1111/gbb.12637. This article has 28 citations.

## Artifacts

- [Edison artifact artifact-00](Sotos_Syndrome-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 14 |
| On topic | 9 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 72 |
| Resolved | 66 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 2 |
| Unverifiable | 4 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0019349` (5 mentions) - the report calls it "if available"; MONDO calls it **Sotos syndrome**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0016571` (obsolete histone methylation) (2 mentions)
- `GO:0006306` (obsolete DNA methylation) (2 mentions)

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `Taxon`.