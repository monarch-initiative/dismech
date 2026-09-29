---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-02T10:25:57.310306'
end_time: '2026-09-02T10:40:32.709077'
duration_seconds: 875.4
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Spinocerebellar ataxia, autosomal recessive 32 (SCAR32), caused by
    biallelic variants in PRDX3 encoding mitochondrial peroxiredoxin 3, the thioredoxin-dependent
    peroxidase that clears mitochondrial matrix hydrogen peroxide
  mondo_id: MONDO:0859245
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 18
reference_validation:
  total_references: 6
  verified: 6
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 6
  on_topic: 6
  validator_version: 0.2.1
term_validation:
  total_terms: 15
  verified: 12
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0859245
    reported_labels:
    - if available
    ontology_label: spinocerebellar ataxia, autosomal recessive 32
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
  path: Spinocerebellar_Ataxia_Autosomal_Recessive_32-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Spinocerebellar ataxia, autosomal recessive 32 (SCAR32), caused by biallelic variants in PRDX3 encoding mitochondrial peroxiredoxin 3, the thioredoxin-dependent peroxidase that clears mitochondrial matrix hydrogen peroxide
- **MONDO ID:** MONDO:0859245 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Spinocerebellar ataxia, autosomal recessive 32 (SCAR32), caused by biallelic variants in PRDX3 encoding mitochondrial peroxiredoxin 3, the thioredoxin-dependent peroxidase that clears mitochondrial matrix hydrogen peroxide** covering all of the
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
- **Disease Name:** Spinocerebellar ataxia, autosomal recessive 32 (SCAR32), caused by biallelic variants in PRDX3 encoding mitochondrial peroxiredoxin 3, the thioredoxin-dependent peroxidase that clears mitochondrial matrix hydrogen peroxide
- **MONDO ID:** MONDO:0859245 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Spinocerebellar ataxia, autosomal recessive 32 (SCAR32), caused by biallelic variants in PRDX3 encoding mitochondrial peroxiredoxin 3, the thioredoxin-dependent peroxidase that clears mitochondrial matrix hydrogen peroxide** covering all of the
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


# SCAR32 / PRDX3-related cerebellar ataxia: disease-characteristics report

## Executive summary

Spinocerebellar ataxia, autosomal recessive 32 (SCAR32) is an ultra-rare Mendelian neurologic disorder caused by biallelic germline variants in **PRDX3**, which encodes the mitochondrial-matrix antioxidant enzyme peroxiredoxin 3. The replicated phenotype is cerebellar ataxia with cerebellar atrophy, but onset ranges from infancy to adulthood and the broader spectrum includes ocular-motor abnormalities, tremor or myoclonus, hypokinetic features, neuropathy, dysphagia, and cognitive or behavioral manifestations. Evidence remains based on small case series and individual patients rather than population cohorts. No disease-specific prevalence, survival estimate, validated biomarker, treatment guideline, or interventional trial is available. The best-supported mechanism is failure of the PRDX3–TXN2 peroxide-detoxification system, followed by mitochondrial oxidative stress, impaired bioenergetics and proteostasis, and increased neuronal vulnerability. Open Targets lists a replicated PRDX3–SCAR32 association based on five evidence records and identifies **MONDO:0859245** and **ENSG00000165672**. (OpenTargets Search: spinocerebellar ataxia autosomal recessive 32-PRDX3, rebelo2021bialleliclossoffunctionvariations pages 1-2)

| Domain | High-confidence finding | Evidence type/strength | Suggested ontology terms | Key source/date/DOI/PMID if known |
|---|---|---|---|---|
| Disease identity | Spinocerebellar ataxia, autosomal recessive 32 (SCAR32) is a rare PRDX3-related cerebellar ataxia/neurodegenerative disorder. MONDO records the entity as MONDO:0859245. Published reports use inconsistent OMIM numbers (#619862 and #619648), so the current OMIM record should be verified directly before database ingestion. | Strong disease-level genetic association; replicated human families | MONDO:0859245; cerebellar ataxia; autosomal recessive inheritance | Open Targets association (OpenTargets Search: spinocerebellar ataxia autosomal recessive 32-PRDX3); Rebelo et al., 2021, DOI: [10.1093/brain/awab071](https://doi.org/10.1093/brain/awab071), PMID: 33889951 (rebelo2021bialleliclossoffunctionvariations pages 1-2) |
| Causal gene and inheritance | Biallelic germline variants in **PRDX3** cause disease; unaffected parents commonly carry one variant. PRDX3 is Ensembl ENSG00000165672 and encodes mitochondrial peroxiredoxin 3. | Strong human segregation plus functional evidence; autosomal recessive | PRDX3; ENSG00000165672; loss of function; germline variant | Five simplex families in the discovery study and later independent cases (OpenTargets Search: spinocerebellar ataxia autosomal recessive 32-PRDX3, rebelo2021bialleliclossoffunctionvariations pages 1-2, naef2024scar32functionalcharacterization pages 2-3, martinezrubio2022proteinmisfoldingand pages 2-2) |
| Core motor phenotype | Gait and limb ataxia, dysmetria and cerebellar dysarthria constitute the core syndrome. Severity is variable and usually mild-to-moderate but may be severe in infantile disease; SARA scores reported include 7/40, 10/40, 19/40 and, in the original adult series, 8.5–21.5. | Strong but small human case series; exact pooled frequencies remain unreliable | HP:0001251 Ataxia; HP:0002072 Chorea is not core and should not be assigned routinely; cerebellar dysarthria; dysmetria; unsteady gait | Rebelo et al., 2021 (rebelo2021bialleliclossoffunctionvariations pages 6-7); Martínez-Rubio et al., 2022, DOI: [10.1093/hmg/ddac146](https://doi.org/10.1093/hmg/ddac146), PMID: 35766882 (martinezrubio2022proteinmisfoldingand pages 1-2); Naef et al., 2024 (naef2024scar32functionalcharacterization pages 2-3) |
| Onset and course | Reported onset extends from infancy/birth to approximately 35 years. Most cases show chronic, slowly progressive ataxia; the p.Asp163Glu case began acutely at 19 months, progressed rapidly initially, and then remained comparatively stable from ages 4–6.5 years. | Moderate human evidence; heterogeneous alleles and short follow-up | HP:0003593 Infantile onset; HP:0011463 Childhood onset; HP:0003581 Adult onset; progressive neurologic deterioration | Martínez-Rubio et al., 2022 (martinezrubio2022proteinmisfoldingand pages 2-2); comparative case summary (yang2025ahomozygousprdx3 pages 4-5) |
| Oculomotor and movement findings | Gaze-evoked nystagmus, saccadic pursuit, hypermetric or slow saccades and ophthalmoplegia occur variably. Myoclonus, postural tremor, cervical dystonia, bradykinesia, hypomimia, rigidity and global hypokinesia expand the movement-disorder spectrum. | Moderate human evidence; variable and not universal | HP:0000639 Nystagmus; abnormal ocular motility; ophthalmoplegia; myoclonus; tremor; dystonia; bradykinesia; rigidity | Rebelo et al., 2021 (rebelo2021bialleliclossoffunctionvariations pages 6-7); Naef et al., 2024 (naef2024scar32functionalcharacterization pages 2-3) |
| Additional neurologic phenotype | Dysphagia, peripheral motor-sensory neuropathy, learning difficulty, cognitive/academic decline, mood or behavioral disturbance and occasional hearing impairment have been reported. Cognition can remain normal. | Limited-to-moderate human evidence; mostly individual observations | HP:0002015 Dysphagia; HP:0009830 Peripheral neuropathy; learning disability; mild cognitive impairment; behavioral abnormality; hearing impairment | Martínez-Rubio et al., 2022 (martinezrubio2022proteinmisfoldingand pages 2-2); Naef et al., 2024 (naef2024scar32functionalcharacterization pages 2-3, naef2024scar32functionalcharacterization pages 3-5); comparative cases (yang2025ahomozygousprdx3 pages 4-5) |
| MRI and anatomy | Cerebellar atrophy is the defining imaging abnormality and was universal in the later comparative case table. Severe early atrophy, vermian involvement, cerebellar cortical or middle-cerebellar-peduncle T2 hyperintensity, and occasional olivary, brainstem or mild parietal degeneration are described. | Strong human imaging evidence for cerebellar atrophy; ancillary findings less consistent | HP:0001272 Cerebellar atrophy; cerebellar vermis; cerebellar cortex; middle cerebellar peduncle; brainstem; inferior olivary nucleus; UBERON terms should be verified before ingestion | Rebelo et al., 2021 (rebelo2021bialleliclossoffunctionvariations pages 1-2, rebelo2021bialleliclossoffunctionvariations pages 6-7); Martínez-Rubio et al., 2022 (martinezrubio2022proteinmisfoldingand pages 2-2); Naef et al., 2024 (naef2024scar32functionalcharacterization pages 2-3) |
| Pathogenic-variant spectrum | Reported variants include nonsense, frameshift, splice-altering and missense alleles. Examples include c.340dupG (p.Ala114GlyfsTer3), c.425C>G (p.Ala142Gly), c.489C>G (p.Asp163Glu), c.525_535del (p.Leu176TrpfsTer11), c.604G>A (p.Asp202Asn), and c.619C>T (p.Arg207Ter). Classification must be performed per allele rather than assuming every published missense allele is pathogenic. | Strong for segregating truncating alleles; moderate and functional-data-dependent for missense alleles | Sequence variant; frameshift variant; stop-gained variant; missense variant; splice-region variant | Rebelo et al., 2021 (rebelo2021bialleliclossoffunctionvariations pages 6-7, rebelo2021bialleliclossoffunctionvariations pages 14-15); Martínez-Rubio et al., 2022 (martinezrubio2022proteinmisfoldingand pages 2-2); Naef et al., 2024 (naef2024scar32functionalcharacterization pages 2-3); Yang et al., 2025 (yang2025ahomozygousprdx3 pages 1-2) |
| Population frequency and founder effects | Causal alleles are rare. Naef et al. reported p.Ala142Gly below 0.01% in gnomAD; Yang et al. reported p.Arg207Ter in 2/251,446 alleles overall and 1/18,394 East Asian alleles. Recurrence of p.Asp202Asn across ancestries is documented, but a founder effect has not been established. | Limited population-database evidence; no validated carrier-frequency estimate | Rare variant; carrier state; founder effect—not established | Naef et al., 2024 (naef2024scar32functionalcharacterization pages 2-3); Yang et al., 2025 (yang2025ahomozygousprdx3 pages 1-2, yang2025ahomozygousprdx3 pages 4-5) |
| Molecular mechanism | PRDX3 is a mitochondrial matrix, thioredoxin-dependent peroxidase that reduces hydrogen peroxide; oxidized PRDX3 is regenerated by TXN2. Biallelic damaging variants can cause absent or unstable protein, weakening mitochondrial peroxide detoxification. | Strong biochemical knowledge plus patient-fibroblast evidence | GO:0005739 mitochondrion; mitochondrial matrix; hydrogen peroxide catabolic process; cellular oxidant detoxification; peroxidase activity; thioredoxin-dependent peroxiredoxin activity | Rebelo et al., 2021 (rebelo2021bialleliclossoffunctionvariations pages 1-2, rebelo2021bialleliclossoffunctionvariations pages 14-15, rebelo2021bialleliclossoffunctionvariations pages 2-3) |
| Downstream pathophysiology | Deficient PRDX3 leads to increased mitochondrial H2O2/ROS and can result in reduced maximal respiration or respiratory reserve, mitochondrial membrane/cristae injury, protein instability or aggregation, unfolded-protein responses and greater apoptosis susceptibility. Selective cerebellar-neuronal degeneration then produces ataxia; the final cell-type-selectivity step is **inferred**, not demonstrated in human neuropathology. | Mixed: human fibroblasts support protein loss and redox/bioenergetic abnormalities; structural injury, neuronal degeneration and apoptosis rely substantially on cell and animal models | GO:0006979 response to oxidative stress; mitochondrial organization; cellular respiration; protein folding; response to unfolded protein; intrinsic apoptotic signaling; Purkinje cell and cerebellar neuron CL terms should be verified | Rebelo et al., 2021 (rebelo2021bialleliclossoffunctionvariations pages 1-2, rebelo2021bialleliclossoffunctionvariations pages 14-15); Martínez-Rubio et al., 2022 (martinezrubio2022proteinmisfoldingand pages 1-2, martinezrubio2022proteinmisfoldingand pages 2-2) |
| Functional-assay heterogeneity | Fibroblasts in the original and p.Asp163Glu studies showed PRDX3 depletion, oxidative-stress abnormalities and/or impaired respiration. In contrast, fibroblasts from a 2024 patient showed normal respiration and ROS responses despite reduced PRDX3 transcript, indicating that fibroblast assays are allele-, protocol- or tissue-dependent and are not validated diagnostic biomarkers. | Direct but discordant human-cell evidence | Skin fibroblast; oxygen-consumption rate; reactive oxygen species; mitochondrial respiratory capacity | Rebelo et al., 2021 (rebelo2021bialleliclossoffunctionvariations pages 1-2); Martínez-Rubio et al., 2022 (martinezrubio2022proteinmisfoldingand pages 2-2); Naef et al., 2024 (naef2024scar32functionalcharacterization pages 3-5) |
| Diagnostic approach | Diagnosis requires a compatible cerebellar syndrome/MRI plus identification of pathogenic or likely pathogenic **biallelic PRDX3 variants** in trans. Ataxia panels or WES are practical first-line approaches; WGS or RNA studies may resolve structural, intronic or splice-altering alleles. Segregation and allele-specific functional studies are especially important for missense or splice-region VUS. | Strong genomic-diagnostic rationale; no SCAR32-specific consensus guideline | Genetic testing; WES; WGS; multigene panel; RNA sequencing; segregation analysis | Trio exome sequencing identified recent cases after exclusion of common dominant and recessive ataxias (naef2024scar32functionalcharacterization pages 2-3, martinezrubio2022proteinmisfoldingand pages 2-2) |
| Ancillary testing and differential diagnosis | Brain MRI, SARA, ocular-motor examination, neuropsychology, swallowing assessment and nerve-conduction studies characterize extent and progression. Routine biochemical, neurometabolic and conduction studies may be normal. Differential diagnosis includes other recessive/mitochondrial ataxias and repeat-expansion disorders; PRDX3 sequencing does not replace repeat-expansion testing. | Moderate clinical-practice inference; individual-case support | Magnetic resonance imaging; SARA; nerve-conduction study; neuropsychological assessment; swallowing evaluation | Rebelo et al., 2021 (rebelo2021bialleliclossoffunctionvariations pages 6-7); Naef et al., 2024 (naef2024scar32functionalcharacterization pages 2-3) |
| Epidemiology | Prevalence, incidence, sex ratio and population carrier frequency are unavailable. Published evidence consists of very small, geographically diverse families; therefore case proportions must not be treated as population frequencies. | Major evidence gap | Rare disease; prevalence unknown; incidence unknown | Five unrelated discovery families plus subsequent isolated cases (rebelo2021bialleliclossoffunctionvariations pages 1-2, naef2024scar32functionalcharacterization pages 1-2, yang2025ahomozygousprdx3 pages 4-5) |
| Prognosis and quality of life | The disease is lifelong and commonly progressive, with mobility, falls, speech, swallowing, school/work and psychosocial consequences. Formal survival, mortality, life-expectancy, EQ-5D, SF-36 and validated SCAR32-specific natural-history data are unavailable. Some affected adults retain moderate function, while infantile disease may require assisted walking. | Limited longitudinal human evidence; no survival or formal QoL cohort | Mobility impairment; fall risk; speech impairment; activity limitation; quality of life—data unavailable | Adult severity data (rebelo2021bialleliclossoffunctionvariations pages 6-7); infantile follow-up (martinezrubio2022proteinmisfoldingand pages 2-2); 2024 cases (naef2024scar32functionalcharacterization pages 2-3) |
| Treatment | No approved disease-modifying treatment and no PRDX3/SCAR32-specific interventional trial were identified. Physical, occupational and speech/swallowing therapy; fall prevention; mobility aids; educational and psychosocial support; and symptom-directed management are reasonable supportive interventions. Antioxidants, ferroptosis modifiers and PRDX3 gene replacement remain **experimental hypotheses**, without demonstrated SCAR32 clinical efficacy. | Supportive-care extrapolation; disease-modifying evidence unavailable | Physical therapy; occupational therapy; speech therapy; rehabilitation; assistive device; genetic therapy—experimental; NCIT identifiers should be verified | Mechanistic studies identify potential targets but do not establish treatment efficacy (rebelo2021bialleliclossoffunctionvariations pages 1-2, rebelo2021bialleliclossoffunctionvariations pages 14-15, yang2025ahomozygousprdx3 pages 4-5) |
| Prevention and counseling | Acquired primary prevention is not applicable to a Mendelian disorder. Genetic counseling, parental testing, cascade carrier testing, and—when familial pathogenic variants are known—prenatal or preimplantation genetic testing can prevent recurrence or enable informed reproductive decisions. Each pregnancy of two heterozygous parents has the standard autosomal-recessive 25% affected, 50% carrier and 25% unaffected/non-carrier probabilities. | High-confidence Mendelian inference | Genetic counseling; carrier testing; cascade screening; prenatal diagnosis; preimplantation genetic testing | Segregation in multiple families supports recessive counseling (yang2025ahomozygousprdx3 pages 1-2, naef2024scar32functionalcharacterization pages 2-3, martinezrubio2022proteinmisfoldingand pages 2-2) |
| Drosophila model | Pan-neuronal or pan-glial Prdx3 depletion causes abnormal locomotion and reduced survival, especially under oxidative stress; brain degeneration has also been described. This supports redox-sensitive neural vulnerability but does not reproduce the complete human phenotype. | Moderate model-organism evidence; **inferred relevance to humans** | NCBI Taxon:7227; locomotory behavior; response to oxidative stress; neuron; glial cell | Rebelo et al., 2021 (rebelo2021bialleliclossoffunctionvariations pages 1-2, rebelo2021bialleliclossoffunctionvariations pages 14-15) |
| Zebrafish model | CRISPR/Cas9 prdx3 F0 crispants show reduced touch/burst responses, swim distance and velocity, impaired ATP production/maximal respiration, and increased oxidative-stress-associated apoptosis. Mosaic F0 knockdown and early developmental assays limit direct natural-history translation. | Moderate model-organism evidence; **inferred disease mechanism** | NCBI Taxon:7955; locomotory behavior; mitochondrial respiration; ATP metabolic process; apoptotic process | Naef et al., 2024 (naef2024scar32functionalcharacterization pages 3-5) |
| Mouse and cellular models | Prdx3-deficient mice show reduced strength, reduced skeletal-muscle mitochondrial DNA copy number and oxidative-stress-associated hippocampal cell loss. PRDX3 knockdown in cerebellar medulloblastoma cells increases H2O2, reduces viability and sensitizes cells to ROS-triggered apoptosis; mutant expression in primary mouse neurons disrupts neurites and mitochondria. These are mechanistic models, not proof of human Purkinje-cell pathology. | Moderate preclinical evidence; **inferred relevance to SCAR32** | NCBI Taxon:10090; neuron; mitochondrial DNA maintenance; cell death; neurite morphology; oxidative stress | Rebelo et al., 2021 (rebelo2021bialleliclossoffunctionvariations pages 1-2, rebelo2021bialleliclossoffunctionvariations pages 14-15); Martínez-Rubio et al., 2022 (martinezrubio2022proteinmisfoldingand pages 2-2, martinezrubio2022proteinmisfoldingand pages 1-2) |
| Other species/natural disease | No naturally occurring PRDX3-associated veterinary SCAR32 analogue or zoonotic/transmissible component was identified. Experimental models should not be entered as natural animal disease. | Data unavailable/not applicable | Natural disease—not established; zoonosis—not applicable | Available evidence describes induced laboratory models only (rebelo2021bialleliclossoffunctionvariations pages 1-2, naef2024scar32functionalcharacterization pages 3-5, rebelo2021bialleliclossoffunctionvariations pages 14-15) |


*Table: Compact evidence map for PRDX3-related SCAR32, separating replicated human findings from model-based inference and major knowledge gaps. Ontology labels are suggested conservatively, with uncertain identifiers explicitly left for verification.*

## 1. Disease information

**Definition.** SCAR32 is an autosomal-recessive cerebellar ataxia/neurodegenerative disorder produced by biallelic damaging variants in PRDX3. The discovery study identified affected individuals in five unrelated families and described “mild-to-moderate progressive cerebellar ataxia,” movement disorders, severe early cerebellar atrophy, and occasional olivary or brainstem degeneration. (rebelo2021bialleliclossoffunctionvariations pages 1-2, rebelo2021bialleliclossoffunctionvariations pages 2-3)

**Identifiers and synonyms.** The preferred ontology identifier is **MONDO:0859245**. Synonyms include *spinocerebellar ataxia, autosomal recessive 32*, *SCAR32*, *PRDX3-related cerebellar ataxia*, and *PRDX3-associated neurodegeneration/PRAN*. Open Targets maps the disease to PRDX3, Ensembl **ENSG00000165672**. Retrieved publications inconsistently cite OMIM **#619862** and **#619648**; consequently, the live OMIM entry should be checked before knowledge-base ingestion. No disease-specific ICD-10, ICD-11, or MeSH code was established in the retrieved literature; broader hereditary/cerebellar ataxia coding is required. (OpenTargets Search: spinocerebellar ataxia autosomal recessive 32-PRDX3, yang2025ahomozygousprdx3 pages 1-2, naef2024scar32functionalcharacterization pages 1-2)

The evidence is principally **aggregated disease-level literature derived from individually described patients and families**, not EHR-scale or registry-derived data.

## 2. Etiology, risk, protection, and environment

The cause is genetic: pathogenic or likely pathogenic **biallelic germline PRDX3 variants** inherited in an autosomal-recessive pattern. Truncating, frameshift, splice-altering, and functionally damaging missense alleles have been reported. Heterozygous parents and siblings are generally clinically unaffected carriers. (naef2024scar32functionalcharacterization pages 2-3, martinezrubio2022proteinmisfoldingand pages 2-2, yang2025ahomozygousprdx3 pages 4-5)

There are no validated susceptibility loci, modifier genes, protective alleles, environmental causes, infectious triggers, or lifestyle risk factors. Consanguinity increases the probability that both parents carry the same rare allele but is not required: compound-heterozygous disease occurred in a patient born to unrelated parents. Oxidative exposure worsens phenotypes in experimental systems, suggesting that cellular redox load can modify disease expression; this is a **model-based gene–environment inference**, not a demonstrated human exposure association. (rebelo2021bialleliclossoffunctionvariations pages 1-2, naef2024scar32functionalcharacterization pages 2-3, rebelo2021bialleliclossoffunctionvariations pages 14-15)

No diet, antioxidant, exercise regimen, or avoidance strategy has been shown to prevent onset. Ordinary health-promoting behaviors may support general function but should not be represented as SCAR32-specific protective factors.

## 3. Phenotypes

The small and incompletely ascertained cohort precludes reliable percentages. A later comparative table described gait ataxia, limb ataxia, and cerebellar atrophy across all tabulated cases, but this is a published-case proportion subject to ascertainment bias—not a population frequency. (yang2025ahomozygousprdx3 pages 4-5)

* **Core cerebellar syndrome:** gait/truncal ataxia, wide-based gait, limb dysmetria/ataxia, impaired finger-to-nose testing, dysarthria, falls, and loss of independent mobility. Suggested terms include **HP:0001251 Ataxia**, cerebellar dysarthria, dysmetria, unsteady gait, and frequent falls. Adult SARA scores in the original series ranged from 8.5–21.5; later patients scored 7/40 and 10/40, while the infantile case stabilized at 19/40 at ages five and 6.5 years. (rebelo2021bialleliclossoffunctionvariations pages 6-7, martinezrubio2022proteinmisfoldingand pages 1-2, naef2024scar32functionalcharacterization pages 2-3)
* **Ocular motor findings:** gaze-evoked nystagmus, saccadic pursuit, hypermetric or slow saccades, and ophthalmoplegia. Suggested terms: **HP:0000639 Nystagmus**, abnormal saccadic eye movements, and ophthalmoplegia. (rebelo2021bialleliclossoffunctionvariations pages 6-7, naef2024scar32functionalcharacterization pages 2-3)
* **Other movement abnormalities:** postural tremor, myoclonus, cervical dystonia, bradykinesia, hypomimia, rigidity, and global hypokinesia occur variably. These are associated features rather than diagnostic requirements. (rebelo2021bialleliclossoffunctionvariations pages 6-7, naef2024scar32functionalcharacterization pages 2-3)
* **Neuropathy:** the severe infantile p.Asp163Glu case developed lower-limb-predominant motor-sensory neuropathy; nerve-conduction studies were initially normal at 19 months and became moderately abnormal later. Suggested term: peripheral sensorimotor neuropathy. (martinezrubio2022proteinmisfoldingand pages 2-2)
* **Neurodevelopmental/psychiatric:** learning or language delay, academic decline, mild cognitive impairment, introversion/social isolation, and mood disorder have been reported, although other patients had normal cognition. A 2025 patient had WISC-IV full-scale IQ 74, perceptual reasoning 60, and processing speed 71. (yang2025ahomozygousprdx3 pages 1-2, naef2024scar32functionalcharacterization pages 2-3, naef2024scar32functionalcharacterization pages 3-5)
* **Additional findings:** dysphagia, ptosis, exercise intolerance, and occasional hearing impairment have been described. Thyroid enlargement, thyroid autoantibodies, and low selenium occurred in one 2025 patient but are not established components of SCAR32. (yang2025ahomozygousprdx3 pages 1-2, rebelo2021bialleliclossoffunctionvariations pages 6-7, yang2025ahomozygousprdx3 pages 4-5)

Quality-of-life effects likely include impaired ambulation, falls, communication and swallowing difficulties, reduced school/work participation, and psychosocial burden. No SCAR32 cohort has reported EQ-5D, SF-36, PROMIS, or disease-specific quality-of-life measurements.

## 4. Genetic and molecular information

**Gene.** PRDX3 encodes mitochondrial peroxiredoxin 3, the organelle-specific, thioredoxin-dependent peroxide scavenger. Reported pathogenic mechanisms are predominantly loss of protein abundance or function. The disease variants are constitutional/germline; somatic causation has not been reported. (rebelo2021bialleliclossoffunctionvariations pages 1-2, rebelo2021bialleliclossoffunctionvariations pages 2-3)

Representative alleles include:

* **c.340dupG (p.Ala114GlyfsTer3)**—frameshift;
* **c.425C>G (p.Ala142Gly)**—missense, reported at below 0.01% in gnomAD and classified as a VUS in the 2024 study; interpretation depended on its occurrence in trans with a likely pathogenic frameshift and functional/phenotypic evidence;
* **c.489C>G (p.Asp163Glu)**—homozygous missense causing protein instability/aggregation in experimental assays;
* **c.525_535delGTTAGAAGGTT (p.Leu176TrpfsTer11)**—novel frameshift, homozygous or in trans with p.Ala142Gly;
* **c.604G>A (p.Asp202Asn)**—recurrent homozygous missense allele at the dimer interface, associated with marked protein depletion;
* **c.619C>T (p.Arg207Ter)**—homozygous nonsense allele, ACMG pathogenic in the 2025 report; observed in 2/251,446 gnomAD alleles overall and 1/18,394 East Asian alleles. (yang2025ahomozygousprdx3 pages 1-2, rebelo2021bialleliclossoffunctionvariations pages 6-7, rebelo2021bialleliclossoffunctionvariations pages 14-15, naef2024scar32functionalcharacterization pages 2-3, martinezrubio2022proteinmisfoldingand pages 2-2)

Other published alleles include p.Arg170Ter, p.Gln220Ter, p.Lys166Ter, early frameshift/nonsense alleles, and splice-site changes. HGVS should be normalized against **NM_006793.5** before ingestion because typographical inconsistencies appear in secondary tables. Variant classification must be allele-specific; publication as a disease candidate does not automatically establish ACMG pathogenicity. (yang2025ahomozygousprdx3 pages 4-5)

No validated modifier gene, epigenetic signature, recurrent copy-number abnormality, translocation, or other chromosomal lesion is known. No disease-specific methylomic, histone, single-cell, or spatial-omics dataset was identified.

## 5. Environmental information

No toxin, radiation, pollution, occupational exposure, smoking, alcohol, diet, exercise pattern, or infectious agent is known to cause SCAR32. Experimental oxidative challenge increases cellular, fly, and zebrafish vulnerability, but clinical avoidance thresholds and human exposure-response data do not exist. The disorder is neither infectious nor transmissible. (rebelo2021bialleliclossoffunctionvariations pages 1-2, naef2024scar32functionalcharacterization pages 3-5)

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic damaging PRDX3 variants lead to** absent, unstable, misfolded, or functionally impaired mitochondrial PRDX3 protein. (rebelo2021bialleliclossoffunctionvariations pages 14-15, martinezrubio2022proteinmisfoldingand pages 2-2)
2. **Reduced PRDX3 activity leads to** impaired TXN2-dependent reduction of mitochondrial-matrix hydrogen peroxide to water. (rebelo2021bialleliclossoffunctionvariations pages 14-15, rebelo2021bialleliclossoffunctionvariations pages 2-3)
3. **Impaired peroxide clearance leads to** increased mitochondrial H₂O₂/ROS and reduced oxidative-stress resilience. (rebelo2021bialleliclossoffunctionvariations pages 1-2, martinezrubio2022proteinmisfoldingand pages 2-2)
4. **Redox imbalance leads to** mitochondrial membrane-potential, morphology, cristae, and respiratory abnormalities; patient fibroblasts demonstrated reduced maximal respiratory capacity in the discovery cohort, although a 2024 fibroblast line had normal respiration and ROS responses. (rebelo2021bialleliclossoffunctionvariations pages 1-2, naef2024scar32functionalcharacterization pages 3-5)
5. **A mechanistic branch leads to** protein instability/aggregation and mitochondrial plus ER unfolded-protein responses, demonstrated particularly for p.Asp163Glu in cell systems. (martinezrubio2022proteinmisfoldingand pages 1-2, martinezrubio2022proteinmisfoldingand pages 2-2)
6. **A second branch leads to** reduced ATP production/respiratory reserve and increased ROS-triggered apoptosis, demonstrated in cerebellar cells and zebrafish. (rebelo2021bialleliclossoffunctionvariations pages 1-2, naef2024scar32functionalcharacterization pages 3-5)
7. **These disturbances are inferred to lead to** selective vulnerability and dysfunction/loss of cerebellar neurons—probably including Purkinje-system circuitry—plus occasional brainstem, olivary, peripheral-nerve, or broader CNS involvement. Direct human neuropathologic proof of the responsible cell population is lacking.
8. **Cerebellar circuit degeneration leads to** ataxia, dysmetria, dysarthria, ocular-motor abnormalities, tremor, falls, and progressive disability. (rebelo2021bialleliclossoffunctionvariations pages 1-2, rebelo2021bialleliclossoffunctionvariations pages 6-7)

Relevant annotations include **GO:0005739 mitochondrion**, mitochondrial matrix, hydrogen-peroxide catabolic process, cellular oxidant detoxification, peroxidase activity, response to oxidative stress (**GO:0006979**), cellular respiration, mitochondrial organization, response to unfolded protein, and intrinsic apoptotic signaling. Candidate cell terms are cerebellar neuron, Purkinje neuron, neuron, astrocyte/glial cell, peripheral motor neuron, and sensory neuron; Purkinje-cell involvement should be flagged as biologically plausible rather than directly established in human tissue.

No canonical Wnt, PI3K–AKT, mTOR, or MAPK cascade has been established as the primary SCAR32 pathway. Ferroptosis and cystine-uptake effects have been proposed from broader PRDX3 cell biology, but are not demonstrated in patient nervous tissue. (yang2025ahomozygousprdx3 pages 4-5)

## 7. Anatomical structures affected

The **central nervous system**, especially the cerebellum, is primary. MRI demonstrates diffuse or vermian cerebellar atrophy; reported secondary sites include the cerebellar cortex, middle cerebellar peduncles, inferior olives, brainstem, and occasionally parietal regions. Peripheral nerves are involved in some severe cases. Changes are generally bilateral/diffuse rather than unilateral. Suggested anatomy terms include cerebellum, cerebellar vermis, cerebellar cortex, middle cerebellar peduncle, brainstem, inferior olivary nucleus, and peripheral nerve; exact UBERON identifiers should be validated before import. (rebelo2021bialleliclossoffunctionvariations pages 1-2, martinezrubio2022proteinmisfoldingand pages 2-2, naef2024scar32functionalcharacterization pages 2-3)

The relevant subcellular site is the **mitochondrial matrix**, with downstream effects on mitochondrial membranes and cristae. No human biopsy has established a definitive cell-selective histopathologic lesion; one original patient’s muscle biopsy showed some COX-negative fibers. (rebelo2021bialleliclossoffunctionvariations pages 6-7, martinezrubio2022proteinmisfoldingand pages 2-2)

## 8. Temporal development

Onset ranges from birth/infancy to approximately 35 years; earlier literature suggested a median near 21 years, but this estimate predates recognition of severe pediatric disease. Typical onset is insidious and chronic, followed by slow progression. The p.Asp163Glu patient was atypical: acute gait ataxia at 19 months, rapid development of cerebellar syndrome and atrophy, then relative stability between ages four and 6.5 years. (martinezrubio2022proteinmisfoldingand pages 1-2, martinezrubio2022proteinmisfoldingand pages 2-2, yang2025ahomozygousprdx3 pages 4-5)

There is no validated staging system. Pragmatic stages are: early imbalance/ocular-motor or school difficulties; intermediate established limb and gait ataxia with falls; and advanced mobility, speech, swallowing, or neuropathic disability. The disease is lifelong. Spontaneous remission has not been demonstrated, although plateaus can occur. No critical therapeutic window has been defined; early genetic diagnosis is nevertheless important for rehabilitation, monitoring, and counseling.

## 9. Inheritance and population

Inheritance is **autosomal recessive**. When both parents are heterozygous carriers, each pregnancy has a 25% probability of an affected child, 50% probability of a carrier, and 25% probability of an unaffected non-carrier. Penetrance for confirmed biallelic pathogenic loss-of-function genotypes appears high in reported families, but cannot be estimated formally; expressivity and age at onset are clearly variable. Anticipation is not expected because this is not a repeat-expansion disease. Germline mosaicism has not been documented. (yang2025ahomozygousprdx3 pages 1-2, naef2024scar32functionalcharacterization pages 2-3, martinezrubio2022proteinmisfoldingand pages 2-2)

Prevalence, incidence, carrier frequency, sex ratio, and population-attributable risk are unknown. Cases have arisen in geographically and ancestrally diverse families. Recurrence of p.Asp202Asn is documented, but a founder effect has not been established. Consanguinity occurs in some families but is not necessary. Published sex or ancestry distributions must not be interpreted epidemiologically because the denominator is extremely small and publication-biased. (naef2024scar32functionalcharacterization pages 1-2, rebelo2021bialleliclossoffunctionvariations pages 14-15, yang2025ahomozygousprdx3 pages 4-5)

## 10. Diagnostics

Diagnosis rests on: (1) a compatible cerebellar syndrome; (2) MRI showing cerebellar atrophy; and (3) pathogenic/likely pathogenic biallelic PRDX3 variants shown to be in trans. A practical workflow is neurological and ocular-motor examination, SARA scoring, brain MRI, then a hereditary-ataxia panel or WES that includes PRDX3. WGS is useful when exome/panel testing is negative or a structural/deep-intronic allele is suspected. RNA analysis can resolve abnormal splicing. Segregation, population frequency, conservation, protein consequence, and—where needed—functional evidence should be integrated for VUS interpretation. (naef2024scar32functionalcharacterization pages 2-3, martinezrubio2022proteinmisfoldingand pages 2-2)

Ancillary evaluation should include neuropsychology, hearing assessment when indicated, swallowing evaluation, nerve-conduction studies/EMG, and rehabilitation assessment. Routine biochemical and neurometabolic testing may be normal. PRDX3 protein, fibroblast ROS, and oxygen-consumption assays are research tools rather than validated clinical biomarkers, especially because 2024 fibroblasts showed normal bioenergetics despite a disease genotype. (naef2024scar32functionalcharacterization pages 3-5, naef2024scar32functionalcharacterization pages 2-3)

Differential diagnosis includes Friedreich ataxia, RFC1-related disease, ataxia with vitamin E deficiency, POLG and other mitochondrial ataxias, SETX-related ataxia with oculomotor apraxia, PNKP/APTX-related disorders, SPG7, SYNE1, COQ8A/ADCK3 disease, recessive spastic ataxias, and dominant or repeat-expansion SCAs. Repeat expansions require dedicated testing and can be missed by conventional WES. CMA, karyotyping, FISH, and mitochondrial-DNA testing are not first-line tests for isolated PRDX3 suspicion unless the wider phenotype indicates them.

Population newborn screening is unavailable. Targeted cascade and carrier testing are appropriate after a familial variant is established.

## 11. Outcome and prognosis

Available observations indicate chronic neurologic morbidity with variable progression. Some adults retain moderate function, whereas early-onset disease can require assisted walking. Dysphagia, falls, neuropathy, communication impairment, and neuropsychiatric or educational difficulties may add morbidity. (martinezrubio2022proteinmisfoldingand pages 2-2, rebelo2021bialleliclossoffunctionvariations pages 6-7, naef2024scar32functionalcharacterization pages 2-3)

There are no reliable 5- or 10-year survival rates, mortality rates, life-expectancy estimates, prognostic calculators, or validated prognostic biomarkers. Severe early onset, neuropathy, extensive atrophy, and higher SARA score may plausibly indicate greater disability, but none is validated as an independent prognostic factor. Recovery of established neurodegeneration has not been demonstrated.

## 12. Treatment

No approved disease-modifying pharmacotherapy, PRDX3-targeted treatment, pharmacogenomic recommendation, surgery, gene therapy, cell therapy, ASO/siRNA therapy, or SCAR32-specific clinical trial was identified. Mechanistic proposals—including mitochondria-targeted antioxidants, ferroptosis modulation, restoration of thioredoxin/peroxide detoxification, or PRDX3 gene replacement—remain preclinical hypotheses and should not be represented as effective treatments. (rebelo2021bialleliclossoffunctionvariations pages 1-2, rebelo2021bialleliclossoffunctionvariations pages 14-15, yang2025ahomozygousprdx3 pages 4-5)

Current care is supportive and individualized:

* physical therapy, balance/gait training, exercise within safe tolerance, fall prevention, and mobility aids;
* occupational therapy and home/school/work adaptation;
* speech therapy and augmentative communication where needed;
* swallowing assessment, dietetic support, and aspiration prevention;
* management of tremor, dystonia, rigidity, mood symptoms, pain, and sleep according to standard symptomatic practice;
* hearing, cognition, education, and psychosocial support;
* periodic SARA, mobility, nutrition, respiratory/aspiration-risk, and neurologic reassessment.

Suggested NCIT concepts are Physical Therapy, Occupational Therapy, Speech Therapy, Rehabilitation Therapy, Assistive Device, Genetic Counseling, and Gene Therapy—Experimental. No SCAR32-specific response rate or adverse-event dataset exists.

## 13. Prevention

Primary prevention through lifestyle modification, vaccination, environmental control, or prophylactic medication is not applicable. **Genetic prevention and informed reproductive choice** are possible through counseling, parental confirmation, cascade carrier testing, prenatal diagnosis, and preimplantation genetic testing when familial pathogenic variants are known. Secondary prevention consists of early recognition and molecular diagnosis, allowing earlier rehabilitation and surveillance. Tertiary prevention comprises fall reduction, contracture/deconditioning prevention, swallowing and aspiration management, and educational/psychosocial intervention. (yang2025ahomozygousprdx3 pages 1-2, naef2024scar32functionalcharacterization pages 2-3, martinezrubio2022proteinmisfoldingand pages 2-2)

## 14. Other species and natural disease

No naturally occurring PRDX3-associated SCAR32 analogue was identified in companion animals, livestock, or wildlife. There is no zoonotic potential or cross-species transmission. Orthologous PRDX3 systems are evolutionarily conserved and provide experimental models, but induced knockdown/knockout phenotypes should not be classified as natural veterinary disease.

## 15. Model organisms and research applications

* **Drosophila melanogaster** (NCBI Taxon 7227): pan-neuronal or pan-glial Prdx3 depletion caused abnormal locomotion and shortened survival under oxidative stress; brain degeneration and oxidative susceptibility were also described. The model supports neural redox vulnerability but does not reproduce the complete human syndrome. (rebelo2021bialleliclossoffunctionvariations pages 1-2, rebelo2021bialleliclossoffunctionvariations pages 14-15)
* **Danio rerio** (NCBI Taxon 7955): CRISPR/Cas9 F0 *prdx3* crispants showed diminished burst/touch responses, reduced swimming distance and velocity, reduced ATP production and maximal respiration, and increased oxidative-stress-associated apoptosis. Limitations include mosaic F0 disruption and early developmental endpoints. (naef2024scar32functionalcharacterization pages 3-5)
* **Mus musculus** (NCBI Taxon 10090): Prdx3 deficiency has been associated with reduced strength, reduced skeletal-muscle mitochondrial DNA copy number, and oxidative-stress-associated hippocampal cell loss. These models do not yet constitute a fully characterized SCAR32 knock-in natural-history model. (rebelo2021bialleliclossoffunctionvariations pages 14-15)
* **Human fibroblasts:** original disease lines showed absent PRDX3, reduced glutathione-peroxidase activity, and reduced maximal respiratory capacity; p.Asp163Glu fibroblasts showed increased mitochondrial oxidative stress. A later line had reduced transcript but normal respiration and ROS responses, demonstrating assay and allele heterogeneity. (rebelo2021bialleliclossoffunctionvariations pages 1-2, naef2024scar32functionalcharacterization pages 3-5, martinezrubio2022proteinmisfoldingand pages 2-2)
* **Cellular neuronal/cerebellar systems:** PRDX3 knockdown in cerebellar medulloblastoma cells increased H₂O₂, reduced viability, and sensitized cells to ROS-triggered apoptosis. Mutant expression in mouse primary neurons altered neurites and mitochondria; HeLa experiments demonstrated protein aggregation, damaged membranes/cristae, lipid-droplet-like structures, and mitochondrial/ER unfolded-protein responses. (rebelo2021bialleliclossoffunctionvariations pages 1-2, martinezrubio2022proteinmisfoldingand pages 2-2, martinezrubio2022proteinmisfoldingand pages 1-2)

These systems are suitable for allele-function studies, mitochondrial redox and respiration assays, modifier screens, and testing gene replacement or mitochondria-directed compounds. Major unmet needs are stable patient-derived neuronal/iPSC models, Purkinje-cell systems, allele-specific knock-in animals, longitudinal natural-history cohorts, standardized biomarkers, and genotype-stratified therapeutic studies.

## Key literature and dates

1. **Rebelo AP et al.** “Biallelic loss-of-function variations in PRDX3 cause cerebellar ataxia.” *Brain*. Published April 2021; 144:1467–1481. PMID **33889951**. DOI/URL: https://doi.org/10.1093/brain/awab071. The abstract states that the investigators identified recessive PRDX3 mutations in five unrelated families and that patient fibroblasts lacked PRDX3 protein. (OpenTargets Search: spinocerebellar ataxia autosomal recessive 32-PRDX3, rebelo2021bialleliclossoffunctionvariations pages 1-2)
2. **Martínez-Rubio D et al.** “Protein misfolding and clearance in the pathogenesis of a new infantile onset ataxia caused by mutations in PRDX3.” *Human Molecular Genetics*. Published June 2022; 31:3897–3913. PMID **35766882**. DOI/URL: https://doi.org/10.1093/hmg/ddac146. The report’s abstract describes onset at 19 months, severe cerebellar atrophy, early neuropathy, and nearly absent PRDX3 in fibroblasts. (OpenTargets Search: spinocerebellar ataxia autosomal recessive 32-PRDX3, martinezrubio2022proteinmisfoldingand pages 1-2)
3. **Naef V et al.** “SCAR32: Functional characterization and expansion of the clinical-genetic spectrum.” *Annals of Clinical and Translational Neurology*. Published June 2024; 11:1879–1886. DOI/URL: https://doi.org/10.1002/acn3.52094. Two additional unrelated patients and a zebrafish crispant model expanded the phenotype and functional evidence. (naef2024scar32functionalcharacterization pages 1-2, naef2024scar32functionalcharacterization pages 2-3, naef2024scar32functionalcharacterization pages 3-5)
4. **Yang J et al.** “A homozygous PRDX3 pathogenic variant in a paediatric case of spinocerebellar ataxia type 32.” *Neurogenetics*. Published online 6 December 2025. DOI/URL: https://doi.org/10.1007/s10048-025-00869-w. This post-2024 case added p.Arg207Ter, quantitative cognitive findings, and thyroid observations whose disease relationship remains uncertain. (yang2025ahomozygousprdx3 pages 1-2)

## Evidence limitations

The literature consists of very small, heterogeneous, largely cross-sectional family reports. Published-case frequencies cannot be converted into prevalence or penetrance estimates. Functional evidence is compelling but sometimes discordant across fibroblast lines, and much of the downstream causal chain rests on induced cell or animal models rather than human nervous tissue. Absence of disease-specific trials, longitudinal cohorts, neuropathology, validated fluid biomarkers, single-cell data, and formal quality-of-life or survival studies should be encoded explicitly as missing evidence rather than negative biological findings.

References

1. (OpenTargets Search: spinocerebellar ataxia autosomal recessive 32-PRDX3): Open Targets Query (spinocerebellar ataxia autosomal recessive 32-PRDX3, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (rebelo2021bialleliclossoffunctionvariations pages 1-2): Adriana P Rebelo, Ilse Eidhof, Vivian P Cintra, Léna Guillot-Noel, Claudia V Pereira, Dagmar Timmann, Andreas Traschütz, Ludger Schöls, Giulia Coarelli, Alexandra Durr, Mathieu Anheim, Christine Tranchant, Bart van de Warrenburg, Claire Guissart, Michel Koenig, Jack Howell, Carlos T Moraes, Annette Schenck, Giovanni Stevanin, Stephan Züchner, and Matthis Synofzik. Biallelic loss-of-function variations in prdx3 cause cerebellar ataxia. Brain : a journal of neurology, 144:1467-1481, Apr 2021. URL: https://doi.org/10.1093/brain/awab071, doi:10.1093/brain/awab071. This article has 46 citations.

3. (naef2024scar32functionalcharacterization pages 2-3): Valentina Naef, Maria Lieto, Sara Satolli, Rosa De Micco, Martina Troisi, Rosa Pasquariello, Stefano Doccini, Flavia Privitera, Alessandro Filla, Alessandro Tessitore, and Filippo Maria Santorelli. Scar32: functional characterization and expansion of the clinical‐genetic spectrum. Annals of Clinical and Translational Neurology, 11:1879-1886, Jun 2024. URL: https://doi.org/10.1002/acn3.52094, doi:10.1002/acn3.52094. This article has 4 citations and is from a peer-reviewed journal.

4. (martinezrubio2022proteinmisfoldingand pages 2-2): Dolores Martínez-Rubio, Ángela Rodríguez-Prieto, Paula Sancho, Carmen Navarro-González, Nerea Gorría-Redondo, Javier Miquel-Leal, Clara Marco-Marín, Alison Jenkins, Mario Soriano-Navarro, Alberto Hernández, Belén Pérez-Dueñas, Pietro Fazzari, Sergio Aguilera-Albesa, and Carmen Espinós. Protein misfolding and clearance in the pathogenesis of a new infantile onset ataxia caused by mutations in prdx3. Human Molecular Genetics, 31:3897-3913, Jun 2022. URL: https://doi.org/10.1093/hmg/ddac146, doi:10.1093/hmg/ddac146. This article has 20 citations and is from a domain leading peer-reviewed journal.

5. (rebelo2021bialleliclossoffunctionvariations pages 6-7): Adriana P Rebelo, Ilse Eidhof, Vivian P Cintra, Léna Guillot-Noel, Claudia V Pereira, Dagmar Timmann, Andreas Traschütz, Ludger Schöls, Giulia Coarelli, Alexandra Durr, Mathieu Anheim, Christine Tranchant, Bart van de Warrenburg, Claire Guissart, Michel Koenig, Jack Howell, Carlos T Moraes, Annette Schenck, Giovanni Stevanin, Stephan Züchner, and Matthis Synofzik. Biallelic loss-of-function variations in prdx3 cause cerebellar ataxia. Brain : a journal of neurology, 144:1467-1481, Apr 2021. URL: https://doi.org/10.1093/brain/awab071, doi:10.1093/brain/awab071. This article has 46 citations.

6. (martinezrubio2022proteinmisfoldingand pages 1-2): Dolores Martínez-Rubio, Ángela Rodríguez-Prieto, Paula Sancho, Carmen Navarro-González, Nerea Gorría-Redondo, Javier Miquel-Leal, Clara Marco-Marín, Alison Jenkins, Mario Soriano-Navarro, Alberto Hernández, Belén Pérez-Dueñas, Pietro Fazzari, Sergio Aguilera-Albesa, and Carmen Espinós. Protein misfolding and clearance in the pathogenesis of a new infantile onset ataxia caused by mutations in prdx3. Human Molecular Genetics, 31:3897-3913, Jun 2022. URL: https://doi.org/10.1093/hmg/ddac146, doi:10.1093/hmg/ddac146. This article has 20 citations and is from a domain leading peer-reviewed journal.

7. (yang2025ahomozygousprdx3 pages 4-5): Jiaxuan Yang, Yonglin Yu, Hongfang Jiang, Yueping Che, Dingwen Wu, Haifeng Li, Yaoqin Hu, Jinpiao Zhu, and Daqing Ma. A homozygous prdx3 pathogenic variant in a paediatric case of spinocerebellar ataxia type 32. Neurogenetics, Dec 2025. URL: https://doi.org/10.1007/s10048-025-00869-w, doi:10.1007/s10048-025-00869-w. This article has 1 citations and is from a peer-reviewed journal.

8. (naef2024scar32functionalcharacterization pages 3-5): Valentina Naef, Maria Lieto, Sara Satolli, Rosa De Micco, Martina Troisi, Rosa Pasquariello, Stefano Doccini, Flavia Privitera, Alessandro Filla, Alessandro Tessitore, and Filippo Maria Santorelli. Scar32: functional characterization and expansion of the clinical‐genetic spectrum. Annals of Clinical and Translational Neurology, 11:1879-1886, Jun 2024. URL: https://doi.org/10.1002/acn3.52094, doi:10.1002/acn3.52094. This article has 4 citations and is from a peer-reviewed journal.

9. (rebelo2021bialleliclossoffunctionvariations pages 14-15): Adriana P Rebelo, Ilse Eidhof, Vivian P Cintra, Léna Guillot-Noel, Claudia V Pereira, Dagmar Timmann, Andreas Traschütz, Ludger Schöls, Giulia Coarelli, Alexandra Durr, Mathieu Anheim, Christine Tranchant, Bart van de Warrenburg, Claire Guissart, Michel Koenig, Jack Howell, Carlos T Moraes, Annette Schenck, Giovanni Stevanin, Stephan Züchner, and Matthis Synofzik. Biallelic loss-of-function variations in prdx3 cause cerebellar ataxia. Brain : a journal of neurology, 144:1467-1481, Apr 2021. URL: https://doi.org/10.1093/brain/awab071, doi:10.1093/brain/awab071. This article has 46 citations.

10. (yang2025ahomozygousprdx3 pages 1-2): Jiaxuan Yang, Yonglin Yu, Hongfang Jiang, Yueping Che, Dingwen Wu, Haifeng Li, Yaoqin Hu, Jinpiao Zhu, and Daqing Ma. A homozygous prdx3 pathogenic variant in a paediatric case of spinocerebellar ataxia type 32. Neurogenetics, Dec 2025. URL: https://doi.org/10.1007/s10048-025-00869-w, doi:10.1007/s10048-025-00869-w. This article has 1 citations and is from a peer-reviewed journal.

11. (rebelo2021bialleliclossoffunctionvariations pages 2-3): Adriana P Rebelo, Ilse Eidhof, Vivian P Cintra, Léna Guillot-Noel, Claudia V Pereira, Dagmar Timmann, Andreas Traschütz, Ludger Schöls, Giulia Coarelli, Alexandra Durr, Mathieu Anheim, Christine Tranchant, Bart van de Warrenburg, Claire Guissart, Michel Koenig, Jack Howell, Carlos T Moraes, Annette Schenck, Giovanni Stevanin, Stephan Züchner, and Matthis Synofzik. Biallelic loss-of-function variations in prdx3 cause cerebellar ataxia. Brain : a journal of neurology, 144:1467-1481, Apr 2021. URL: https://doi.org/10.1093/brain/awab071, doi:10.1093/brain/awab071. This article has 46 citations.

12. (naef2024scar32functionalcharacterization pages 1-2): Valentina Naef, Maria Lieto, Sara Satolli, Rosa De Micco, Martina Troisi, Rosa Pasquariello, Stefano Doccini, Flavia Privitera, Alessandro Filla, Alessandro Tessitore, and Filippo Maria Santorelli. Scar32: functional characterization and expansion of the clinical‐genetic spectrum. Annals of Clinical and Translational Neurology, 11:1879-1886, Jun 2024. URL: https://doi.org/10.1002/acn3.52094, doi:10.1002/acn3.52094. This article has 4 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Spinocerebellar_Ataxia_Autosomal_Recessive_32-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 6 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 15 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0859245` (5 mentions) - the report calls it "if available"; MONDO calls it **spinocerebellar ataxia, autosomal recessive 32**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `Taxon`.