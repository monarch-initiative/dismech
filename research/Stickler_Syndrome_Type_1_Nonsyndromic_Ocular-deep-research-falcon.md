---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-16T14:54:14.681294'
end_time: '2026-09-16T15:06:54.845652'
duration_seconds: 760.16
template_file: templates/disease_pathophysiology_research.md
template_sha: 1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666
template_variables:
  disease_name: Ocular-only Stickler syndrome type 1 (COL2A1 alternatively spliced
    exon 2 variants, predominantly ocular Stickler syndrome, OMIM 609508)
  mondo_id: MONDO:0012287
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
  total_references: 9
  verified: 9
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 9
  on_topic: 5
  validator_version: 0.2.1
term_validation:
  total_terms: 3
  verified: 3
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0012287
    reported_labels:
    - if available
    ontology_label: Stickler syndrome, type I, nonsyndromic ocular
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Stickler_Syndrome_Type_1_Nonsyndromic_Ocular-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Ocular-only Stickler syndrome type 1 (COL2A1 alternatively spliced exon 2 variants, predominantly ocular Stickler syndrome, OMIM 609508)
- **MONDO ID:** MONDO:0012287 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Ocular-only Stickler syndrome type 1 (COL2A1 alternatively spliced exon 2 variants, predominantly ocular Stickler syndrome, OMIM 609508)** covering all of the
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
- **Disease Name:** Ocular-only Stickler syndrome type 1 (COL2A1 alternatively spliced exon 2 variants, predominantly ocular Stickler syndrome, OMIM 609508)
- **MONDO ID:** MONDO:0012287 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Ocular-only Stickler syndrome type 1 (COL2A1 alternatively spliced exon 2 variants, predominantly ocular Stickler syndrome, OMIM 609508)** covering all of the
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


# Ocular-only Stickler syndrome type 1 due to alternatively spliced **COL2A1** exon 2 variants

## Executive summary and evidence boundary

This is a rare, autosomal-dominant type II collagenopathy in which pathogenic variants affecting alternatively spliced **COL2A1 exon 2** preferentially disrupt the eye. The characteristic phenotype comprises congenital abnormal vitreous architecture, congenital/early high myopia or megalophthalmos, peripheral retinal degeneration, retinal tears, and a major lifelong risk of rhegmatogenous retinal detachment (RRD), while hearing, craniofacial, and skeletal manifestations are absent or substantially attenuated. “Predominantly ocular” is preferable to an absolute “ocular-only,” because subtle extraocular findings may occur and ocular-only phenotypes can occasionally arise from variants outside exon 2. (mcalinden2008missenseandnonsense pages 1-2, richards2000col2a1exon2 pages 1-2, richards2000col2a1exon2 pages 2-3)

Subtype-specific evidence remains limited to small pedigrees, case reports, and functional-splicing experiments. Statistics from unselected Stickler syndrome or all-**COL2A1** cohorts are therefore identified below as **broader evidence** and should not be assigned directly to OMIM 609508 without qualification.

| Domain | Subtype-specific finding | Evidence type/strength | Key quantitative data | Caveat |
|---|---|---|---|---|
| Identity | Predominantly ocular/ocular-only Stickler syndrome type 1 associated with alternatively spliced `COL2A1` exon 2; phenotype MIM 609508. MONDO:0012287 was supplied in the request but should be independently validated before database ingestion. (snead2020therapeuticanddiagnostic pages 2-3, richards2000col2a1exon2 pages 1-2) | Curated disease designation plus human family evidence; moderate–strong | Three predominantly ocular families in an eight-family study carried exon 2 variants. (richards2000col2a1exon2 pages 1-2) | “Ocular-only” is phenotypic shorthand: subtle extraocular findings may occur, and ocular-predominant phenotypes can result from variants outside exon 2. |
| Inheritance | Heterozygous `COL2A1` variants cause autosomal-dominant disease; affected individuals have a 50% transmission probability per pregnancy. (mcalinden2008missenseandnonsense pages 1-2, richards2010sticklersyndromeand pages 1-4) | Segregating human pedigrees; strong | Exact exon-2 penetrance and de novo fraction are not established; a broader ocularly selected Stickler cohort reported de novo `COL2A1` variants in 37%. (huang2020mutationspectrumand pages 1-3) | The 37% estimate is not exon-2-specific, and parentage was not genomically verified. |
| Tissue-specific splicing | Exon 2 inclusion produces procollagen IIA, expressed during early chondroprogenitor development and in adult vitreous; exon 2 exclusion produces IIB, predominant in differentiated adult cartilage. This explains why exon-2 lesions disproportionately affect the eye. (mcalinden2008missenseandnonsense pages 1-2, majava2007moleculargeneticsof pages 65-67) | Human expression studies plus functional splicing assays; strong | Adult vitreous has been described as the only adult tissue containing procollagen IIA. (majava2007moleculargeneticsof pages 65-67) | Tissue restriction explains reduced systemic disease but does not prove that every exon-2 variant is strictly ocular-only. |
| Pathogenic variants | Reported exon-2 examples include nonsense p.Cys64Ter (“Cys64Stop”) and missense p.Cys57Tyr (“Cys57Tyr”); both can alter exon-2 splicing efficiency, while truncation can also reduce functional IIA collagen. (mcalinden2008missenseandnonsense pages 1-2, majava2007moleculargeneticsof pages 65-67) | Human cases plus minigene/cell assays; moderate–strong | McAlinden et al. studied three patients: two with Cys64Stop and one with Cys57Tyr. (mcalinden2008missenseandnonsense pages 1-2) | Transcript-specific HGVS nomenclature, genome build, ClinVar classification, and gnomAD frequency must be checked variant by variant before curation. |
| Vitreous phenotype | A congenital type-1 “membranous” vitreous anomaly is the principal clinical clue and reflects abnormal vitreous embryogenesis. (snead2020therapeuticanddiagnostic pages 2-3, richards2000col2a1exon2 pages 1-2, richards2010sticklersyndromeand pages 1-4) | Repeated specialist phenotyping across families; strong | No reliable exon-2-specific frequency is available. | Prior retinal detachment, hemorrhage, cataract, or vitreoretinal surgery can obscure the diagnostic vitreous architecture. |
| Myopia and globe phenotype | Congenital or early high myopia is typical; some nonmyopic patients may have congenital megalophthalmos/cornea plana and masked or “crypto-” myopia. (snead2020therapeuticanddiagnostic pages 2-3) | Expert clinical review supported by broader Stickler cohorts; moderate | Approximately 85% of general Stickler patients were reported to have congenital myopia; exon-2 ocular-only families had a mean semiquantitative myopia score of 1.8. (snead2020therapeuticanddiagnostic pages 2-3, richards2000col2a1exon2 pages 2-3) | The 85% estimate is not exon-2-specific; absence of high myopia does not exclude the diagnosis. |
| Retinal disease | Peripheral retinal degeneration, retinal tears, giant retinal tears, and rhegmatogenous retinal detachment—often bilateral—are the principal threats to vision. (snead2020therapeuticanddiagnostic pages 2-3, richards2000col2a1exon2 pages 1-2) | Human family/cohort observations; strong | Exon-2 ocular-only families had a mean retinal-detachment score of 1.5, where one affected eye scored 1 and both eyes scored 2. (richards2000col2a1exon2 pages 2-3) | A robust exon-2-specific lifetime detachment risk has not been calculated; broader Stickler estimates should not be treated as subtype-specific. |
| Systemic phenotype | Orofacial, auditory, and skeletal manifestations are absent or markedly reduced because mature cartilage predominantly excludes exon 2. Younger reported patients had normal habitus and lacked cleft palate, hearing deficit, osteoarthritis, and bone abnormalities. (mcalinden2008missenseandnonsense pages 1-2) | Subtype-specific human case/family evidence; moderate | In the ocular-only family group, mean scores were 0 for midfacial hypoplasia, 0.1 for clinical and radiographic joint abnormalities, 0.2 for conductive hearing loss, and 0.5 for sensorineural hearing loss. (richards2000col2a1exon2 pages 2-3) | “Predominantly ocular” is more accurate than universally “ocular-only”; formal audiology and musculoskeletal assessment may reveal mild findings. |
| Diagnosis | Diagnosis combines dilated vitreoretinal examination—especially recognition of congenital membranous vitreous—with molecular confirmation of a heterozygous pathogenic/likely pathogenic `COL2A1` exon-2 or splice-regulatory variant. (snead2020therapeuticanddiagnostic pages 2-3, richards2010sticklersyndromeand pages 1-4) | Human diagnostic cohorts and expert review; strong | A broader two-stage vitreous-phenotyping plus `COL2A1` sequencing strategy achieved high mutation-detection efficiency, although no exon-2-only sensitivity is available. (richards2010sticklersyndromeand pages 1-4) | Exome sequencing may miss deep-intronic splice-regulatory variants; genome sequencing or RNA/minigene studies may be needed. (spickett2016deepintronicsequence pages 1-5) |
| Differential diagnosis | Important alternatives include Wagner/`VCAN` vitreoretinopathy, other Stickler genotypes, familial exudative vitreoretinopathy, Knobloch syndrome, Marfan-related retinal disease, and nonsyndromic familial retinal detachment. Exon-2 families lack the characteristic lenticular, RPE, and choroidal changes of Wagner syndrome. (richards2000col2a1exon2 pages 2-3) | Comparative clinical phenotyping; moderate | No validated differential-diagnostic score exists specifically for exon-2 disease. | A negative systemic examination must not be used to dismiss Stickler syndrome. |
| Prophylactic retinopexy | Cryotherapy or circumferential laser is used in high-risk Stickler eyes to reduce retinal detachment; the evidence supports broader Stickler populations, not specifically exon-2 ocular-only disease. (morris2026ahistoricalreview pages 5-8, morris2026ahistoricalreview pages 10-11) | Retrospective comparative cohorts and meta-analysis; moderate; no completed randomized trial | A synthesis reported detachment in 6.6% of treated versus 36% of control eyes; one encircling-laser series reported 1/42 eyes (2.4%) detaching over mean 6.0 years, while Manchester laser yielded 9% versus 26% untreated. (morris2026ahistoricalreview pages 5-8) | Protocols differ in modality and posterior extent; selection bias and nonrandomized designs limit certainty, and risks/benefits require vitreoretinal-specialist counseling. |
| Clinical trials | `NCT07146516` is recruiting to evaluate laser prophylaxis in genetically confirmed Stickler types 1 and 2. `NCT04465188`, evaluating prophylactic encircling scleral buckling, was withdrawn after enrolling no participants. (NCT04465188 chunk 1, NCT07146516 chunk 2) | Prospective trial registrations; efficacy not yet established | `NCT07146516`: planned enrollment 500; `NCT04465188`: actual enrollment 0. (NCT04465188 chunk 1, NCT07146516 chunk 2) | Neither trial is restricted to alternatively spliced exon-2 disease; there are no outcome data from the withdrawn study. |
| Major unknowns | Unresolved areas include exon-2-specific prevalence, penetrance, age-specific detachment risk, modifier genes, environmental interactions, quality-of-life estimates, biomarkers, multi-omics signatures, and validated exon-2-specific animal models or molecular therapies. (spickett2016deepintronicsequence pages 1-5, jacobson2023characteristicsofa pages 9-10) | Evidence-gap assessment | Published subtype-specific evidence consists mainly of small pedigrees, case series, and in-vitro splicing studies. | General Stickler or all-`COL2A1` statistics should be explicitly labeled and not automatically assigned to MIM 609508. |


*Table: Compact evidence map distinguishing findings specific to ocular-predominant COL2A1 exon-2 Stickler syndrome from broader Stickler data. It highlights clinical utility, evidence strength, quantitative findings, and major limitations.*

## 1. Disease information

### Definition and identifiers

* **Preferred name:** ocular-only Stickler syndrome type 1; more accurately, *predominantly ocular Stickler syndrome type 1 associated with alternatively spliced COL2A1 exon 2 variants*.
* **OMIM phenotype:** **609508**, commonly described as Stickler syndrome, type I, nonsyndromic ocular/ocular-only form. The 2020 review identifies the ocular-only **COL2A1** subgroup as MIM 609508 and associates it with membranous vitreous anomaly, retinal detachment, congenital megalophthalmos, minimal systemic involvement, and high blindness risk. (snead2020therapeuticanddiagnostic pages 2-3)
* **MONDO:** **MONDO:0012287** was supplied in the request; it should be verified against the current MONDO release before production ingestion because ontology mappings can change.
* **Gene/locus:** **COL2A1**, chromosome **12q13.11**; type 1 Stickler syndrome is the relevant molecular class. (snead2020therapeuticanddiagnostic pages 2-3, jacobson2023characteristicsofa pages 1-2)
* **Orphanet, ICD-10/ICD-11, MeSH:** no dedicated code for the exon-2 ocular-only subtype was established in the retrieved evidence. It is generally nested under Stickler syndrome, hereditary vitreoretinopathy, or connective-tissue disorder codes. Coding the subtype solely as nonsyndromic retinal detachment would lose clinically important inherited-risk information.
* **Synonyms:** ocular variant of Stickler syndrome; predominantly ocular Stickler syndrome; nonsyndromic ocular Stickler syndrome; ocular-only type 1 Stickler syndrome; **COL2A1**-related ocular Stickler syndrome.

The evidence is principally **aggregated disease-level literature plus deeply phenotyped families**, not EHR-derived population data. Richards et al. studied eight type-1-vitreous families; three predominantly ocular families carried exon-2 variants, whereas five families with ocular plus systemic disease carried variants outside exon 2. (richards2000col2a1exon2 pages 1-2)

## 2. Etiology

### Causal factor

The primary cause is a **heterozygous germline pathogenic variant affecting exon 2 of COL2A1 or its splice-regulatory context**. **COL2A1** encodes the α1 chain of type II collagen, a fibrillar extracellular-matrix protein important in vitreous and cartilage. Exon 2 inclusion generates procollagen IIA; exclusion generates IIB. Adult vitreous retains IIA expression, whereas differentiated adult chondrocytes predominantly express IIB, explaining the ocular enrichment of exon-2 disease. (mcalinden2008missenseandnonsense pages 1-2, majava2007moleculargeneticsof pages 65-67, jacobson2023characteristicsofa pages 1-2)

Reported subtype-specific examples include **p.Cys64Ter/Cys64Stop** and **p.Cys57Tyr/Cys57Tyr**. In one study, two patients carried Cys64Stop and one carried Cys57Tyr; both nonsense and missense lesions affected alternative-splicing behavior. (mcalinden2008missenseandnonsense pages 1-2)

### Risk factors

* **Genetic:** carrying the familial pathogenic allele is the principal risk factor. Family history of congenital high myopia, retinal tears/detachment, or childhood blindness is highly informative.
* **De novo disease:** possible. A broader ocularly selected Stickler cohort found de novo **COL2A1** variants in 37%, although this was not exon-2-specific and parentage was not genomically confirmed. (huang2020mutationspectrumand pages 7-9, huang2020mutationspectrumand pages 1-3)
* **Modifier loci:** none validated for OMIM 609508. The common intronic variant **rs1635532** showed allele- and individual-dependent effects on exon-2 inclusion and a significant frequency difference between an RRD cohort and controls, but it is a candidate susceptibility/modifier signal rather than an established monogenic cause. (spickett2016deepintronicsequence pages 1-5)
* **Environmental/lifestyle risk:** no toxin, infection, diet, smoking, occupation, sex, or age exposure causes this Mendelian disorder. Ocular trauma may precipitate a retinal break in an already vulnerable eye, but a quantified exon-2-specific gene–environment interaction was not found.

### Protective factors

No validated protective allele, diet, drug, or lifestyle exposure prevents the genotype. Clinically, early diagnosis, retinal surveillance, avoidance of avoidable ocular trauma, urgent evaluation of flashes/floaters/field loss, and appropriately selected prophylactic retinopexy reduce complications rather than preventing inheritance.

## 3. Phenotypes

| Phenotype | Character and course | Frequency/evidence | Suggested HPO annotation |
|---|---|---|---|
| Congenital membranous vitreous anomaly | Clinical sign; congenital and persistent; key diagnostic feature | Strong subtype/family evidence; exact exon-2 frequency unavailable | Abnormality of the vitreous humor; membranous vitreous anomaly |
| High myopia/axial elongation | Usually congenital or early childhood; variable severity | Broader Stickler estimate approximately 85% congenital myopia; ocular-only families had mean semiquantitative myopia score 1.8 | **HP:0011003 High myopia**, myopia, increased axial length |
| Congenital megalophthalmos/cornea plana | May mask expected myopic refraction (“cryptomyopia”) | Recognized in ocular-only subgroup; frequency unknown | Megalocornea/megalophthalmos; cornea plana |
| Peripheral retinal degeneration/tears | Progressive structural vulnerability; may remain asymptomatic until tearing | Common but no exon-2 denominator | Retinal degeneration; retinal tear; lattice retinal degeneration |
| Rhegmatogenous retinal detachment, including giant retinal tear | Acute sight-threatening complication superimposed on lifelong predisposition; unilateral or bilateral | Ocular-only families had mean RD score 1.5, where one eye=1 and both eyes=2 | **HP:0000541 Retinal detachment**; giant retinal tear |
| Cataract | Congenital quadrantic lamellar cataract can occur; not subtype-discriminating | Broader type 1/type 2 evidence; exact exon-2 frequency unknown | Cataract; lamellar cataract |
| Glaucoma | Usually secondary or postoperative; infantile glaucoma is reported in broader COL2A1 disease | Not quantified for exon 2 | Glaucoma; elevated intraocular pressure |
| Craniofacial, hearing, and joint findings | Usually absent or mild | Ocular-only family mean scores: midfacial hypoplasia 0; clinical/radiographic joints 0.1 each; conductive hearing loss 0.2; sensorineural hearing loss 0.5 | Use relevant terms only when actually observed |

The broader clinical review states that absence of high myopia or radial paravascular pigmented lattice must not exclude Stickler syndrome; some apparently nonmyopic eyes have megalophthalmos/cornea plana. (snead2020therapeuticanddiagnostic pages 2-3) In the subtype report, younger patients had normal habitus and lacked cleft palate, hearing deficit, osteoarthritis, or bone abnormalities. (mcalinden2008missenseandnonsense pages 1-2)

**Quality of life:** no exon-2-specific EQ-5D, SF-36, PROMIS, or vision-related QOL study was found. The principal burden is preventable or irreversible visual loss, repeated vitreoretinal operations, activity restrictions, anxiety about fellow-eye detachment, educational/occupational effects, and loss of independence. A broader Korean cohort had mean BCVA 0.40 logMAR and mean refraction −8.23 D, demonstrating substantial visual morbidity but not estimating this subtype specifically. (choi2021geneticcharacteristicsand pages 6-8)

## 4. Genetic and molecular information

* **Gene:** **COL2A1**; protein, collagen α-1(II) chain. Suggested identifiers for curation: HGNC symbol **COL2A1** and gene-level cross-references to NCBI Gene/Ensembl should be resolved against the current releases.
* **Origin:** germline; usually heterozygous. This is not a somatic cancer disorder.
* **Variant classes:** nonsense, missense, canonical or noncanonical splice variants, and deep-intronic regulatory variants can alter exon-2 inclusion or the exon-2-containing protein. (mcalinden2008missenseandnonsense pages 1-2, spickett2016deepintronicsequence pages 1-5)
* **Functional consequence:** truncating alleles generally support reduced functional type II collagen/haploinsufficiency; an exon-2 missense allele may alter the N-propeptide and/or splicing regulatory elements. McAlinden et al. demonstrated altered IIA:IIB ratios, so “dominant negative” should not automatically be assigned to every exon-2 variant. (mcalinden2008missenseandnonsense pages 1-2)
* **Classification:** classify each allele independently under ACMG/AMP criteria using segregation, population rarity, predicted loss of function, splice assays, phenotype specificity, and ClinVar submissions. Historical disease association does not substitute for transcript-specific contemporary classification.
* **Population frequency:** no reliable aggregate carrier frequency exists. Exact gnomAD/TOPMed frequencies must be queried by transcript and genome build; pathogenic high-penetrance alleles are expected to be absent or very rare.
* **Chromosomal abnormalities:** whole-**COL2A1** deletions occur in broader Stickler cohorts, but no recurrent large rearrangement defines the exon-2 ocular-only entity. A study of 89 families found 57 novel variants and two complete **COL2A1** deletions. (richards2010sticklersyndromeand pages 1-4)
* **Modifiers/epigenetics:** no validated modifier gene, disease-specific methylation signature, histone alteration, or chromatin defect was identified.

A useful exact statement from the 2008 study is its title-level conclusion: **“Missense and nonsense mutations in the alternatively-spliced exon 2 of COL2A1 cause the ocular variant of Stickler syndrome.”** The paper was published online 22 August 2007 and in *Human Mutation* 29:83–90 (January 2008), DOI: [10.1002/humu.20603](https://doi.org/10.1002/humu.20603). (mcalinden2008missenseandnonsense pages 1-2)

## 5. Environmental information

No environmental, infectious, toxic, nutritional, or metabolic cause is known. Smoking, alcohol, diet, and exercise have not been shown to alter penetrance of the molecular disorder. General retinal-detachment precautions—eye protection during high-impact activities and prompt assessment after trauma or new photopsias, floaters, or visual-field loss—are prudent risk management, not evidence that environment causes the disease. Vaccination and antimicrobial measures are not relevant.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. A heterozygous pathogenic **COL2A1 exon-2 or exon-2 splice-regulatory lesion leads to** altered abundance and/or sequence of the exon-2-containing procollagen IIA isoform. (mcalinden2008missenseandnonsense pages 1-2, spickett2016deepintronicsequence pages 1-5)
2. Tissue-specific alternative splicing **results in** retention of exon 2 in early chondroprogenitors and adult vitreous but exclusion from predominant mature-cartilage IIB transcripts. (mcalinden2008missenseandnonsense pages 1-2, majava2007moleculargeneticsof pages 65-67)
3. Abnormal or insufficient procollagen IIA **leads to** defective type II collagen extracellular-matrix assembly in the developing vitreous; this link is strongly inferred from expression, segregation, and splicing assays, but variant-specific ultrastructural proof is incomplete.
4. Defective vitreous development **results in** congenital membranous/hypoplastic vitreous architecture and abnormal vitreoretinal mechanical relationships. (snead2020therapeuticanddiagnostic pages 2-3, richards2000col2a1exon2 pages 1-2)
5. The abnormal ocular matrix **leads to** axial elongation/high myopia or megalophthalmos and peripheral retinal degeneration; the precise molecular cause of axial elongation remains unresolved. (jacobson2023characteristicsofa pages 1-2)
6. Peripheral retinal vulnerability plus vitreoretinal traction **results in** retinal holes, horseshoe tears, or giant retinal tears.
7. A full-thickness break **leads to** liquefied vitreous passing under the neurosensory retina, **resulting in** rhegmatogenous retinal detachment, visual-field loss, and potentially blindness.
8. **Branch:** retinal detachment and repeated surgery may **lead to** proliferative vitreoretinopathy, cataract, glaucoma, amblyopia in children, and permanent visual disability.
9. Exon 2 exclusion from most mature cartilage **results in** relative sparing of joints, hearing structures, and craniofacial tissues, explaining the predominantly ocular phenotype. (mcalinden2008missenseandnonsense pages 1-2, richards2000col2a1exon2 pages 1-2)

### Processes and ontology suggestions

* **GO biological processes:** extracellular matrix organization; collagen fibril organization; eye development; vitreous body development; alternative mRNA splicing; retina homeostasis.
* **GO cellular components:** extracellular matrix; collagen-containing extracellular matrix; vitreous body; endoplasmic reticulum/secretory pathway when misfolding is demonstrated.
* **Cell Ontology candidates:** vitreous hyalocyte; retinal pigment epithelial cell; retinal Müller glial cell; photoreceptor cell; chondrocyte/chondroprogenitor. The primary collagen-producing ocular cell population responsible for the phenotype is not definitively resolved in the retrieved evidence.
* **Not established:** a primary Wnt, MAPK, mTOR, PI3K–AKT, immune, inflammatory, metabolic, oxidative-stress, or mitochondrial pathway; disease-specific single-cell, spatial-transcriptomic, proteomic, metabolomic, lipidomic, or integrated multi-omic signature.

Functional evidence includes illegitimate-transcript analysis, allele-specific minigenes, and knockdown/overexpression of candidate RNA-binding factors. These experiments found allele- and individual-dependent exon-2 inclusion, providing direct **in-vitro** support for a splice-regulatory mechanism. (spickett2016deepintronicsequence pages 1-5)

## 7. Anatomical structures affected

* **Primary organ:** eye, usually **bilateral**.
* **Principal sites:** vitreous body, vitreous base, peripheral retina, vitreoretinal interface, neurosensory retina; secondarily lens, cornea/globe, macula, optic nerve, and anterior chamber after complications.
* **Suggested UBERON annotations:** eye; vitreous body; retina; peripheral retina; lens; cornea; sclera. Current term IDs should be validated in the target ontology release.
* **Tissue class:** specialized ocular connective tissue/extracellular matrix and neural retina.
* **Subcellular:** secretory pathway and extracellular collagen matrix. ER retention should only be annotated where experimentally shown for a particular missense allele.
* **Secondary systemic sites:** cartilage, joints, middle/inner ear, and craniofacial structures are generally spared or mildly affected, not categorically impossible.

## 8. Temporal development

The matrix defect is **developmental and congenital**, even when diagnosis is delayed. Vitreous architecture and refractive abnormalities arise at birth or in early childhood. Retinal degeneration and traction evolve over years; retinal tears/detachment may occur in infancy, childhood, adolescence, or adulthood. Broader COL2A1 data include bilateral detachment presenting with leukocoria at two months and childhood detachments at ages 6, 8, and 10 years, illustrating the potentially very early window of vulnerability, although those cases were not exon-2-specific. (huang2020mutationspectrumand pages 7-9)

The disease is lifelong and does not remit. Retinal detachment is episodic and acute, whereas the predisposition is chronic. Half of detachments in broader Stickler data occur by age 20, and bilateral disease is common, but these figures are not validated specifically for exon 2. (morris2026ahistoricalreview pages 5-8) The critical intervention window is **before the first detachment**, or before fellow-eye detachment after unilateral disease.

## 9. Inheritance and population

* **Mode:** autosomal dominant. Each child of a heterozygous affected person has a **50% transmission probability**.
* **Penetrance:** high for an ocular phenotype in reported pedigrees, but no unbiased age-dependent exon-2 penetrance estimate exists.
* **Expressivity:** variable—myopia, retinal degeneration, detachment age, laterality, and subtle systemic findings differ among and within families.
* **Anticipation:** not established; this is not a repeat-expansion disorder.
* **Mosaicism:** parental germline or somatic mosaicism is biologically possible but not quantified.
* **Founder effect/consanguinity:** none established for this autosomal-dominant subtype; consanguinity is not a causal requirement.
* **Sex ratio:** expected to be approximately equal; no robust subtype-specific sex effect was found.
* **Ethnic/geographic distribution:** reported across populations, with no proven ancestry restriction.

General Stickler syndrome incidence is often quoted at approximately **1:7,500–1:10,000**, and type 1 accounts for roughly 70–90% of diagnosed Stickler syndrome. These are broad estimates, not prevalence figures for OMIM 609508. (choi2021geneticcharacteristicsand pages 6-8, jacobson2023characteristicsofa pages 1-2) No reliable incidence, prevalence, carrier-frequency, or population-attributable fraction exists for exon-2 ocular-only disease.

## 10. Diagnostics

### Clinical assessment

1. **Urgent comprehensive ophthalmic examination:** cycloplegic refraction, axial length, slit-lamp examination, intraocular pressure, and dilated peripheral retinal examination with scleral indentation when appropriate.
2. **Vitreous phenotyping:** seek the congenital type-1 **membranous vitreous anomaly**. COL2A1 disease most often gives membranous vitreous, whereas COL11A1 more often produces irregular beaded lamellae. (richards2010sticklersyndromeand pages 1-4)
3. **Imaging:** wide-field fundus photography documents peripheral degeneration; OCT evaluates macula and posterior vitreous. Serial pediatric OCT may help monitor posterior vitreous detachment, which correlated with earlier RD in a broader cohort. (choi2021geneticcharacteristicsand pages 8-9)
4. **Systemic baseline evaluation:** formal audiology, palate/craniofacial examination, and musculoskeletal history/examination. Normal findings support ocular-predominant disease but do not establish the molecular diagnosis.

There is no diagnostic serum, urine, enzyme, metabolite, electrophysiologic, or biopsy biomarker.

### Genetic testing pathway

* Preferred first-line testing is a **hereditary vitreoretinopathy/Stickler panel** containing at least **COL2A1, COL11A1, COL11A2, COL9A1, COL9A2, COL9A3, VCAN**, and other clinically overlapping genes.
* Ensure full coverage of **COL2A1 exon 2 and canonical splice junctions**, with deletion/duplication analysis.
* Targeted single-gene testing is efficient when the vitreous phenotype and pedigree strongly indicate type 1.
* **WES** detects most coding variants but can miss deep-intronic regulatory lesions. **WGS**, RNA studies, or a validated minigene assay should be considered when suspicion remains high after negative panel/WES testing. Deep-intronic variants can alter exon-2 splicing efficiency. (spickett2016deepintronicsequence pages 1-5)
* CMA, karyotyping, FISH, mitochondrial sequencing, and repeat-expansion testing are not routine unless another diagnosis is suspected.
* Cascade testing should use the confirmed familial allele. Prenatal diagnosis and PGT-M are technically possible after molecular confirmation.

### Differential diagnosis

* **VCAN-related Wagner vitreoretinopathy:** overlaps in vitreous degeneration but tends to have characteristic lenticular, retinal-pigment-epithelial, and choroidal changes absent from the reported exon-2 Stickler pedigrees. (richards2000col2a1exon2 pages 2-3)
* Other Stickler genotypes (**COL11A1, COL11A2, COL9A1–3**) and non-exon-2 **COL2A1** disease.
* Familial exudative vitreoretinopathy (**FZD4, LRP5, NDP, TSPAN12**), Knobloch syndrome (**COL18A1**), Marfan syndrome, high-myopia retinal degeneration, and nonsyndromic familial RRD.
* A negative craniofacial, hearing, or joint examination must not be used to exclude ocular-only Stickler syndrome.

No universally validated diagnostic criteria exist specifically for OMIM 609508; molecular confirmation plus compatible congenital vitreous disease is the strongest standard.

## 11. Outcome and prognosis

Life expectancy is expected to be normal because the principal morbidity is ocular; no disease-specific mortality signal or survival curve is available. Prognosis is dominated by whether retinal detachment occurs, its macular involvement, proliferative vitreoretinopathy, age at presentation, bilateral disease, and access to expert surgery/prophylaxis.

Untreated detachment can cause severe or permanent blindness, particularly in young children in whom presentation is delayed and amblyopia compounds structural damage. The broader literature characterizes Stickler syndrome as a leading inherited cause of retinal detachment and an important cause of childhood RRD. (snead2020therapeuticanddiagnostic pages 2-3) Recovery after uncomplicated, promptly repaired detachment may be useful, but complex giant-tear detachments often require repeated operations and can lead to cataract or secondary glaucoma. (jacobson2023characteristicsofa pages 1-2)

No validated molecular prognostic biomarker, exon-2-specific risk calculator, or QOL-adjusted survival estimate exists.

## 12. Treatment

### Practical management algorithm

1. **Correct refractive error early** with spectacles or contact lenses; treat amblyopia in children.
2. **Educate patients/families** about flashes, new floaters, curtain/field loss, sudden acuity change, and the need for same-day retinal assessment.
3. **Retinal-specialist surveillance** from diagnosis throughout life; examine relatives carrying the familial variant even when asymptomatic.
4. **Treat definite retinal breaks** with laser photocoagulation or cryotherapy according to retinal location and clinical circumstances.
5. **Discuss prophylactic circumferential retinopexy** in high-risk eyes at an experienced vitreoretinal center. Choice among Cambridge cryotherapy, Manchester-style laser, and more posterior encircling laser remains center- and anatomy-dependent.
6. **Repair established RRD urgently**, using scleral buckle, pars plana vitrectomy, retinopexy, tamponade, or combinations according to age, break configuration, lens status, and proliferative vitreoretinopathy.
7. Manage cataract, glaucoma, and low vision conventionally, accounting for retinal risk.

Suggested NCIT intervention concepts include ophthalmic examination, genetic testing, laser photocoagulation, cryotherapy, scleral buckling, vitrectomy, retinal-detachment repair, cataract surgery, corrective lenses, genetic counseling, and low-vision rehabilitation.

### Evidence for prophylaxis

Evidence is favorable but predominantly retrospective and **not exon-2-specific**. A later synthesis reported RD in **6.6% of treated versus 36% of control eyes**. An encircling-laser series reported detachment in **1/42 eyes (2.4%)** over mean 6.0 years; Manchester ora-focused laser was associated with no giant retinal tears but 9% detachment from smaller posterior tears versus 26% untreated. (morris2026ahistoricalreview pages 5-8) These data support offering informed discussion, but protocol heterogeneity, selection bias, and lack of completed randomized trials limit certainty. Experts recommend consent covering observation, focal treatment, and encircling prophylaxis. (morris2026ahistoricalreview pages 10-11)

There is no disease-modifying pharmacotherapy, approved gene therapy, ASO, siRNA, CRISPR treatment, cell therapy, immunotherapy, or subtype-specific pharmacogenomic guidance.

### Trials and recent implementation

* **NCT07146516**, “Retinal Detachment Prevention (Laser Prophylaxis) in Stickler Syndrome,” is recruiting genetically confirmed type 1 or type 2 participants at five US sites, with planned enrollment of 500. It is not restricted to exon-2 disease and has no efficacy results yet. ClinicalTrials.gov: [NCT07146516](https://clinicaltrials.gov/study/NCT07146516). (NCT07146516 chunk 2, NCT07146516 chunk 3)
* **NCT04465188**, a randomized phase-2 study of prophylactic encircling scleral buckling in the unaffected fellow eye of genetically confirmed patients aged 5–35 years, was withdrawn for “No inclusion,” with zero enrollment. ClinicalTrials.gov: [NCT04465188](https://clinicaltrials.gov/study/NCT04465188). (NCT04465188 chunk 1, NCT04465188 chunk 2)

A real-world implementation cited by an authoritative review is the NHS England Highly Specialised Stickler Syndrome Service, operating since 2011 and integrating molecular diagnosis, ophthalmology, audiology, and rheumatology. The authors state that molecular diagnosis can now be confirmed in over 95% of broadly defined Stickler cases and emphasize prophylactic prevention of blindness; these performance claims are not exon-2-specific. DOI: [10.1177/2633004020978661](https://doi.org/10.1177/2633004020978661), published 2020. (snead2020therapeuticanddiagnostic pages 2-3)

## 13. Prevention

* **Primary prevention of the genotype:** unavailable. Reproductive options include nondirective genetic counseling, PGT-M, prenatal diagnosis, donor gametes, or natural conception after counseling.
* **Secondary prevention:** cascade testing and early ophthalmic examination identify asymptomatic high-risk relatives before detachment.
* **Tertiary prevention:** surveillance, prompt treatment of tears, selected prophylactic retinopexy, urgent RD repair, amblyopia therapy, and low-vision rehabilitation.
* **Risk communication:** explain 50% transmission, variable expressivity, possible de novo occurrence, and the inadequacy of a normal systemic examination for excluding disease.
* **Population screening/newborn screening:** not currently established. Targeted family screening is substantially more appropriate than universal biochemical newborn screening.
* **Vaccines, medications, diet, and environmental remediation:** not applicable.

## 14. Other species and natural disease

No naturally occurring veterinary disorder specifically homologous to human **COL2A1 exon-2 ocular-only Stickler syndrome** was established in the retrieved literature. Orthologous **Col2a1/col2a1a** genes are evolutionarily conserved in mouse and zebrafish. The disease is not infectious, transmissible between species, or zoonotic. Breed predisposition and VBO mappings are unavailable.

## 15. Model organisms and experimental systems

* **Mouse:** targeted heterozygous inactivation of **Col2a1** has been used as a general Stickler model and produces ocular abnormalities; complete knockout causes severe chondrodysplasia. These models support type II collagen’s role but do not isolate the human exon-2 ocular-only mechanism. (majava2007moleculargeneticsof pages 65-67)
* **Zebrafish:** **col2a1a** perturbation has been used to examine early ocular/neural-crest development, again as a general COL2A1 model rather than a validated exon-2 knock-in.
* **Cell/in-vitro models:** allele-specific minigene assays, illegitimate transcripts, and manipulation of RNA-binding factors directly model exon-2 inclusion and are currently the most subtype-relevant experimental systems. (spickett2016deepintronicsequence pages 1-5)
* **Limitations:** general knockouts often produce skeletal disease unlike the human ocular-predominant phenotype; species differences in alternative splicing and vitreous biology limit translation.
* **Needed models:** patient-derived iPSC ocular cells or vitreous organoid systems, humanized exon-2 knock-in animals, long-read retinal/vitreous transcriptomics, and variant-specific rescue assays. No subtype-specific CRISPR screen, single-cell atlas, spatial transcriptomic study, or therapeutic-rescue model was found.

## Recent research assessment (2023–2024)

Recent publications have refined broader **COL2A1** genotype–phenotype interpretation rather than producing a new exon-2-specific natural-history cohort. A 2023 three-generation study showed markedly different ocular-versus-joint phenotypes from two exon-51 **COL2A1** variants and concluded that the molecular basis of these differences remains unknown, reinforcing the need for deep phenotyping and caution against simple variant-class predictions. DOI: [10.3390/genes14040847](https://doi.org/10.3390/genes14040847), published March/April 2023. (jacobson2023characteristicsofa pages 9-10, jacobson2023characteristicsofa pages 1-2) No 2023–2024 study retrieved here superseded the core exon-2 mechanism established by Richards et al. (2000), McAlinden et al. (2008), and Spickett et al. (2016). (mcalinden2008missenseandnonsense pages 1-2, spickett2016deepintronicsequence pages 1-5, richards2000col2a1exon2 pages 1-2)

## Knowledge-base curation recommendations

1. Represent OMIM 609508 as a **phenotypic/molecularly enriched subtype**, not as synonymous with every ocular-only **COL2A1** presentation.
2. Store exon-2 evidence at the **variant/transcript level**, including transcript accession, genome build, allele frequency, ClinVar review status, and functional-splicing result.
3. Annotate frequencies as **subtype-specific**, **all COL2A1**, or **all Stickler syndrome**; do not mix denominators.
4. Use “predominantly ocular” and permit mild hearing/joint findings.
5. Treat prophylactic-retinopexy efficacy as moderate-quality evidence extrapolated from broader high-risk Stickler cohorts.
6. Mark subtype-specific prevalence, age-dependent penetrance, modifiers, environmental interactions, QOL, omics signatures, biomarkers, and molecular therapies as **currently unavailable**, rather than zero or absent.

References

1. (mcalinden2008missenseandnonsense pages 1-2): Audrey McAlinden, Marja Majava, Paul N. Bishop, Rahat Perveen, Graeme CM. Black, Mary Ella Pierpont, Leena Ala-Kokko, and Minna Männikkö. Missense and nonsense mutations in the alternatively‐spliced exon 2 of col2a1 cause the ocular variant of stickler syndrome. Human Mutation, 29:83-90, Jan 2008. URL: https://doi.org/10.1002/humu.20603, doi:10.1002/humu.20603. This article has 77 citations and is from a domain leading peer-reviewed journal.

2. (richards2000col2a1exon2 pages 1-2): A. Richards, Sam Martin, J. Yates, John D. Scott, D. Baguley, F. Pope, and M. Snead. Col2a1 exon 2 mutations: relevance to the stickler and wagner syndromes. British Journal of Ophthalmology, 84:364-371, Apr 2000. URL: https://doi.org/10.1136/bjo.84.4.364, doi:10.1136/bjo.84.4.364. This article has 168 citations and is from a highest quality peer-reviewed journal.

3. (richards2000col2a1exon2 pages 2-3): A. Richards, Sam Martin, J. Yates, John D. Scott, D. Baguley, F. Pope, and M. Snead. Col2a1 exon 2 mutations: relevance to the stickler and wagner syndromes. British Journal of Ophthalmology, 84:364-371, Apr 2000. URL: https://doi.org/10.1136/bjo.84.4.364, doi:10.1136/bjo.84.4.364. This article has 168 citations and is from a highest quality peer-reviewed journal.

4. (snead2020therapeuticanddiagnostic pages 2-3): Martin Snead, Howard Martin, Peter Bale, Nick Shenker, David Baguley, Philip Alexander, Annie McNinch, and Arabella Poulson. Therapeutic and diagnostic advances in stickler syndrome. Therapeutic Advances in Rare Disease, Jan 2020. URL: https://doi.org/10.1177/2633004020978661, doi:10.1177/2633004020978661. This article has 42 citations.

5. (richards2010sticklersyndromeand pages 1-4): Allan J. Richards, Annie McNinch, Howard Martin, Kim Oakhill, Harjeet Rai, Sarah Waller, Becky Treacy, Joanne Whittaker, Sarah Meredith, Arabella Poulson, and Martin P. Snead. Stickler syndrome and the vitreous phenotype: mutations in col2a1 and col11a1. Human Mutation, 31:E1461-E1471, Jun 2010. URL: https://doi.org/10.1002/humu.21257, doi:10.1002/humu.21257. This article has 185 citations and is from a domain leading peer-reviewed journal.

6. (huang2020mutationspectrumand pages 1-3): Li Huang, Chonglin Chen, Zhirong Wang, Limei Sun, Songshan Li, Ting Zhang, Xiaoling Luo, and Xiaoyan Ding. Mutation spectrum and de novo mutation analysis in stickler syndrome patients with high myopia or retinal detachment. Aug 2020. URL: https://doi.org/10.3390/genes11080882, doi:10.3390/genes11080882. This article has 21 citations.

7. (majava2007moleculargeneticsof pages 65-67): M Majava. Molecular genetics of stickler and marshall syndromes, and the role of collagen ii and other candidate proteins in high myopia and impaired hearing. Unknown journal, 2007.

8. (spickett2016deepintronicsequence pages 1-5): Carl Spickett, Pirro Hysi, Chistopher J Hammond, Alan Prescott, Gregory S Fincham, Arabella V Poulson, Annie M McNinch, Allan J Richards, and Martin P Snead. Deep intronic sequence variants in col2a1 affect the alternative splicing efficiency of exon 2, and may confer a risk for rhegmatogenous retinal detachment. Human Mutation, 37:1085-1096, Oct 2016. URL: https://doi.org/10.1002/humu.23050, doi:10.1002/humu.23050. This article has 23 citations and is from a domain leading peer-reviewed journal.

9. (morris2026ahistoricalreview pages 5-8): Robert E. Morris, Ferenc Kuhn, M. Oltmanns, Matthew R. West, Cary R Baxter, Mathew R. Sapp, and Harshvardhan Chawla. A historical review of encircling laser retinopexy as a prophylaxis for rhegmatogenous retinal detachment; and a commentary on recent progress in stickler syndrome. Clinical Ophthalmology, Volume 20:1-12, Apr 2026. URL: https://doi.org/10.2147/opth.s588688, doi:10.2147/opth.s588688. This article has 1 citations and is from a peer-reviewed journal.

10. (morris2026ahistoricalreview pages 10-11): Robert E. Morris, Ferenc Kuhn, M. Oltmanns, Matthew R. West, Cary R Baxter, Mathew R. Sapp, and Harshvardhan Chawla. A historical review of encircling laser retinopexy as a prophylaxis for rhegmatogenous retinal detachment; and a commentary on recent progress in stickler syndrome. Clinical Ophthalmology, Volume 20:1-12, Apr 2026. URL: https://doi.org/10.2147/opth.s588688, doi:10.2147/opth.s588688. This article has 1 citations and is from a peer-reviewed journal.

11. (NCT04465188 chunk 1):  Scleral Buckling for Retinal Detachment Prevention in Genetically Confirmed Stickler Syndrome. Assistance Publique - Hôpitaux de Paris. 2023. ClinicalTrials.gov Identifier: NCT04465188

12. (NCT07146516 chunk 2):  Retinal Detachment Prevention (Laser Prophylaxis) in Stickler Syndrome (SS). Helen Keller Eye Research Foundation. 2025. ClinicalTrials.gov Identifier: NCT07146516

13. (jacobson2023characteristicsofa pages 9-10): Adam Jacobson, Cagri G. Besirli, and Brenda L. Bohnsack. Characteristics of a three-generation family with stickler syndrome type i carrying two different col2a1 mutations. Genes, 14:847, Mar 2023. URL: https://doi.org/10.3390/genes14040847, doi:10.3390/genes14040847. This article has 6 citations.

14. (jacobson2023characteristicsofa pages 1-2): Adam Jacobson, Cagri G. Besirli, and Brenda L. Bohnsack. Characteristics of a three-generation family with stickler syndrome type i carrying two different col2a1 mutations. Genes, 14:847, Mar 2023. URL: https://doi.org/10.3390/genes14040847, doi:10.3390/genes14040847. This article has 6 citations.

15. (huang2020mutationspectrumand pages 7-9): Li Huang, Chonglin Chen, Zhirong Wang, Limei Sun, Songshan Li, Ting Zhang, Xiaoling Luo, and Xiaoyan Ding. Mutation spectrum and de novo mutation analysis in stickler syndrome patients with high myopia or retinal detachment. Aug 2020. URL: https://doi.org/10.3390/genes11080882, doi:10.3390/genes11080882. This article has 21 citations.

16. (choi2021geneticcharacteristicsand pages 6-8): Soon-Il Choi, Se-Joon Woo, Baek-Lok Oh, Jinu Han, Hyun-Taek Lim, Byung-Joo Lee, Kwangsic Joo, Jun-Young Park, Ja-Hyun Jang, Min-Kyung So, and Sang-Jin Kim. Genetic characteristics and phenotype of korean patients with stickler syndrome: a korean multicenter analysis report no. 1. Oct 2021. URL: https://doi.org/10.3390/genes12101578, doi:10.3390/genes12101578. This article has 14 citations.

17. (choi2021geneticcharacteristicsand pages 8-9): Soon-Il Choi, Se-Joon Woo, Baek-Lok Oh, Jinu Han, Hyun-Taek Lim, Byung-Joo Lee, Kwangsic Joo, Jun-Young Park, Ja-Hyun Jang, Min-Kyung So, and Sang-Jin Kim. Genetic characteristics and phenotype of korean patients with stickler syndrome: a korean multicenter analysis report no. 1. Oct 2021. URL: https://doi.org/10.3390/genes12101578, doi:10.3390/genes12101578. This article has 14 citations.

18. (NCT07146516 chunk 3):  Retinal Detachment Prevention (Laser Prophylaxis) in Stickler Syndrome (SS). Helen Keller Eye Research Foundation. 2025. ClinicalTrials.gov Identifier: NCT07146516

19. (NCT04465188 chunk 2):  Scleral Buckling for Retinal Detachment Prevention in Genetically Confirmed Stickler Syndrome. Assistance Publique - Hôpitaux de Paris. 2023. ClinicalTrials.gov Identifier: NCT04465188

## Artifacts

- [Edison artifact artifact-00](Stickler_Syndrome_Type_1_Nonsyndromic_Ocular-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 9 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 3 |
| Resolved | 3 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0012287` (3 mentions) - the report calls it "if available"; MONDO calls it **Stickler syndrome, type I, nonsyndromic ocular**
