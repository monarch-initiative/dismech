---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-31T10:08:53.788060'
end_time: '2026-08-31T10:18:17.350509'
duration_seconds: 563.56
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Muscular Dystrophy, Limb-Girdle, Autosomal Recessive 28
  mondo_id: MONDO:0957270
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 2
reference_validation:
  total_references: 3
  verified: 3
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 3
  on_topic: 3
  validator_version: 0.2.1
term_validation:
  total_terms: 16
  verified: 16
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0957270
    reported_labels:
    - if available
    ontology_label: muscular dystrophy, limb-girdle, autosomal recessive 28
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Muscular_Dystrophy_Limb-girdle_Autosomal_Recessive_28-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Muscular Dystrophy, Limb-Girdle, Autosomal Recessive 28
- **MONDO ID:** MONDO:0957270 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Muscular Dystrophy, Limb-Girdle, Autosomal Recessive 28** covering all of the
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
- **Disease Name:** Muscular Dystrophy, Limb-Girdle, Autosomal Recessive 28
- **MONDO ID:** MONDO:0957270 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Muscular Dystrophy, Limb-Girdle, Autosomal Recessive 28** covering all of the
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


# Muscular Dystrophy, Limb-Girdle, Autosomal Recessive 28

## Executive summary and evidence grade

**Muscular dystrophy, limb-girdle, autosomal recessive 28 (LGMD-AR28; MONDO:0957270)** is an exceptionally rare, newly delineated Mendelian myopathy attributed primarily to **biallelic variants in HMGCR**, encoding 3-hydroxy-3-methylglutaryl-CoA reductase, the rate-limiting enzyme of the mevalonate pathway. The principal disease-specific publication located was a 2023 conference abstract by Foley et al., whose title states: **“Bi-allelic variants in HMGCR cause limb girdle muscular dystrophy and further implicate the mevalonate pathway in muscle disease.”** DOI: https://doi.org/10.1016/j.nmd.2023.07.195 (October 2023). Aggregated Open Targets evidence links MONDO:0957270 most strongly to HMGCR and also returns CERT1, but the available records do not establish CERT1 as an independent cause of this muscular dystrophy. (OpenTargets Search: muscular dystrophy, limb-girdle, autosomal recessive 28)

The evidence base is therefore **very low-volume and incompletely published**. A full disease-defining article containing patient-level variants, clinical measurements, and functional experiments was not retrieved. Consequently, exact phenotype frequencies, prevalence, progression rates, survival, and treatment effects cannot presently be reported responsibly. Broad observations from other LGMDs, statin-associated muscle symptoms, and anti-HMGCR immune-mediated necrotizing myopathy must not be assigned to this Mendelian disorder.

| Topic | Current evidence status for MONDO:0957270 |
|---|---|
| Identity | **Muscular dystrophy, limb-girdle, autosomal recessive 28**; MONDO identifier surfaced in disease-target resources as **MONDO_0957270**. The entity appears to be a **newly catalogued ultra-rare autosomal-recessive LGMD** rather than a well-established legacy subtype with extensive literature. (OpenTargets Search: muscular dystrophy, limb-girdle, autosomal recessive 28) |
| Causal gene | **HMGCR** is the **primary implicated gene** based on current retrieved disease-target evidence and a cited 2023 neuromuscular conference abstract titled *“Bi-allelic variants in HMGCR cause limb girdle muscular dystrophy and further implicate the mevalonate pathway in muscle disease”* (DOI: https://doi.org/10.1016/j.nmd.2023.07.195). **CERT1** also appears in aggregated association outputs, but retrieved evidence does **not** establish CERT1 as an independent confirmed cause of this LGMD entity. (OpenTargets Search: muscular dystrophy, limb-girdle, autosomal recessive 28) |
| Inheritance | Reported/curated as **autosomal recessive**, with evidence summaries indicating **biallelic** variant interpretation for the HMGCR-associated disease signal. (OpenTargets Search: muscular dystrophy, limb-girdle, autosomal recessive 28) |
| Evidence date/source | Most disease-specific signal identified here is **recent (2023 onward)** and largely derives from **aggregated database evidence** plus the **2023 conference abstract** rather than a full-length, richly phenotyped primary paper retrievable in this search set. Open Targets lists supporting literature including **PMIDs 36745799 and 37167966**, but the retrieved context does not provide disease-specific full-text extraction sufficient for detailed phenotype/variant curation. (OpenTargets Search: muscular dystrophy, limb-girdle, autosomal recessive 28) |
| Phenotype | Disease label indicates a **limb-girdle muscular dystrophy phenotype**, implying predominant **proximal shoulder/pelvic girdle weakness**. However, **disease-specific quantitative phenotype data**—for example exact onset ages, CK ranges, MRI pattern, biopsy findings, cardiopulmonary involvement, cognition, or wheelchair-loss rates—were **not available** in retrieved disease-specific sources and should not be inferred from other LGMD subtypes. (OpenTargets Search: muscular dystrophy, limb-girdle, autosomal recessive 28) |
| Mechanism | Current best-supported mechanistic interpretation is **HMGCR dysfunction affecting the mevalonate pathway**, thereby implicating defective production/regulation of sterol and nonsterol isoprenoid metabolites important for muscle biology. Any more granular chain linking HMGCR deficiency to fiber degeneration, membrane instability, autophagy, or inflammation remains **plausible but incompletely demonstrated** for this exact disease in the retrieved evidence. **CERT1-related sphingolipid transport involvement remains ambiguous** for MONDO:0957270. (OpenTargets Search: muscular dystrophy, limb-girdle, autosomal recessive 28) |
| Diagnostics | At present, the most defensible disease-specific diagnostic approach is **genomic testing** in patients with unexplained LGMD/proximal myopathy, especially **exome or genome sequencing** or curated neuromuscular gene panels that include **HMGCR**. There is **no retrieved disease-specific validated biomarker set, pathology signature, or formal diagnostic criteria** unique to LGMD autosomal recessive 28. (OpenTargets Search: muscular dystrophy, limb-girdle, autosomal recessive 28) |
| Treatment / trials | **No disease-specific approved therapy or interventional clinical trial** for MONDO:0957270 was identified in retrieved sources. Results involving **statins** or **anti-HMGCR immune-mediated necrotizing myopathy** should **not** be transferred to this genetic LGMD, because those represent a distinct acquired autoimmune/statin-associated disorder rather than inherited biallelic HMGCR-related muscular dystrophy. (OpenTargets Search: muscular dystrophy, limb-girdle, autosomal recessive 28) |
| Epidemiology | **No disease-specific prevalence, incidence, carrier frequency, sex ratio, or founder-effect estimates** were identified in the retrieved evidence. The condition should currently be treated as **extremely rare/ultra-rare** with insufficient published epidemiologic quantification. (OpenTargets Search: muscular dystrophy, limb-girdle, autosomal recessive 28) |
| Major caveats | Major limitations are: **(1)** likely dependence on **very recent and sparse evidence**, **(2)** absence of a retrievable full disease-defining article in the search set, **(3)** **no invented variant-level curation should be made**, **(4)** **CERT1 association may reflect neighboring/overlapping submitted evidence rather than proven dual causality**, and **(5)** broad LGMD, statin-myopathy, or anti-HMGCR autoimmune literature must be kept separate from this Mendelian disease entry. (OpenTargets Search: muscular dystrophy, limb-girdle, autosomal recessive 28) |


*Table: This table summarizes what can currently be stated with confidence about muscular dystrophy, limb-girdle, autosomal recessive 28 from the retrieved evidence. It highlights HMGCR as the primary implicated gene, the unresolved CERT1 signal, and the major quantitative data gaps that should constrain downstream curation.*

## 1. Disease information

### Definition

LGMD-AR28 is a hereditary muscle disease characterized at the category level by a limb-girdle pattern—predominantly proximal pelvic- and shoulder-girdle muscle involvement—and autosomal-recessive inheritance. Its current molecular assignment is **HMGCR-related muscular dystrophy**. The designation is very recent and has not accumulated the detailed natural-history literature available for commoner LGMD subtypes. (OpenTargets Search: muscular dystrophy, limb-girdle, autosomal recessive 28)

### Identifiers and synonyms

- **MONDO:** MONDO:0957270; database form `MONDO_0957270`.
- **Preferred name:** muscular dystrophy, limb-girdle, autosomal recessive 28.
- **Useful synonyms:** LGMD autosomal recessive 28; LGMD-AR28; HMGCR-related limb-girdle muscular dystrophy; biallelic HMGCR-related muscular dystrophy.
- **OMIM, Orphanet, MeSH:** no disease-specific identifier was confirmed in the retrieved evidence. These should remain null rather than be inferred.
- **ICD-10:** no subtype-specific code was identified; clinically it would ordinarily fall under a nonspecific muscular-dystrophy category, subject to national coding rules.
- **ICD-11:** no confirmed subtype-specific code was retrieved.

The available information is derived from **aggregated disease-level resources and a small research case series/meeting abstract**, not population EHR data. Open Targets reports association scores of approximately **0.656 for HMGCR** and **0.429 for CERT1**; these are evidence-integration scores, not penetrance, risk ratios, or diagnostic probabilities. (OpenTargets Search: muscular dystrophy, limb-girdle, autosomal recessive 28)

## 2. Etiology, risk, and protective factors

The initiating cause is **germline biallelic HMGCR variation**, consistent with autosomal-recessive disease. Retrieved database evidence includes missense, splice-region/donor, and in-frame deletion categories, but it did not expose enough transcript-level information to report HGVS expressions safely. Somatic mutation is not implicated. (OpenTargets Search: muscular dystrophy, limb-girdle, autosomal recessive 28)

The apparent CERT1 signal requires caution. HMGCR and CERT1 are neighboring genes on chromosome 5q13; variant annotation, structural variation, or locus-level evidence may therefore associate both genes with a record. No retrieved evidence demonstrated that biallelic CERT1 variants independently cause LGMD-AR28. CERT1 should be retained as an **uncertain locus-level candidate**, not a second established causal gene. (OpenTargets Search: muscular dystrophy, limb-girdle, autosomal recessive 28)

- **Established risk factor:** inheriting two disease-causing HMGCR alleles.
- **Family history/consanguinity:** biologically relevant to recessive inheritance, but no disease-specific frequency was available.
- **Sex:** no sex-specific genetic risk is expected for an autosomal locus; a measured sex ratio is unavailable.
- **Environmental, infectious, occupational, dietary, or lifestyle causes:** none established.
- **Protective variants or modifier genes:** none reported specifically.
- **Gene–environment interaction:** unstudied. Pharmacological HMGCR inhibition by statins is biologically relevant but must not be assumed to initiate or modify this inherited disease without evidence. Statin toxicity and anti-HMGCR autoimmunity are separate entities.

## 3. Phenotypes

Only the general **limb-girdle muscular dystrophy/proximal myopathy** phenotype can be assigned with confidence. Patient-level onset, severity, frequency, CK values, MRI distribution, biopsy features, and cardiopulmonary findings were unavailable in the retrieved disease-specific material. (OpenTargets Search: muscular dystrophy, limb-girdle, autosomal recessive 28)

Suggested knowledge-base annotations, explicitly **provisional pending the primary case series**, are:

- Proximal muscle weakness — **HP:0003701**.
- Pelvic-girdle muscle weakness — **HP:0003749**.
- Shoulder-girdle muscle weakness — use the current HPO term for shoulder-girdle weakness after ontology-version validation.
- Muscular dystrophy — **HP:0003560**.
- Abnormality of skeletal muscle — **HP:0011805**.
- Elevated serum creatine kinase — **HP:0003236**, only if confirmed in individual records.
- Gowers sign, waddling gait, muscle atrophy, contractures, scapular winging, respiratory insufficiency, cardiomyopathy, dysphagia, and loss of ambulation — **not established for this subtype** and should not be entered as confirmed findings.

Onset is likely chronic/insidious by disease class, but neonatal, childhood, or adult onset cannot be assigned. There are no disease-specific phenotype percentages or validated quality-of-life measurements. Expected functional effects of proximal weakness include difficulty rising, climbing stairs, lifting the arms, and walking, but these are clinical implications rather than quantified LGMD-AR28 observations.

## 4. Genetic and molecular information

### Causal gene

- **HMGCR** — 3-hydroxy-3-methylglutaryl-CoA reductase; Ensembl **ENSG00000113161**.
- Molecular role: catalysis of HMG-CoA reduction to mevalonate, the committed/rate-limiting step in cholesterol and nonsterol-isoprenoid biosynthesis.
- Disease mechanism: most consistent with **partial loss of function/hypomorphism**, because profound systemic loss of this central biosynthetic activity would be expected to have broader consequences. That qualification is mechanistic inference; the retrieved disease-specific material did not provide a complete allelic or enzymatic series.

Open Targets identifies HMGCR as the higher-confidence target and cites PMIDs **36745799** and **37167966** in its evidence records. The available excerpts did not establish that both PMIDs are full clinical reports of LGMD-AR28, so they should be checked manually before creating patient-level evidence assertions. (OpenTargets Search: muscular dystrophy, limb-girdle, autosomal recessive 28)

### Variants and genomic architecture

The database evidence includes **missense, splice-donor/region, and in-frame deletion** classes. Exact HGVS, zygosity by patient, ClinVar accession, ACMG classification, and gnomAD frequency were not recoverable and must not be invented. Large deletions involving both HMGCR and neighboring CERT1 remain a possible explanation for some dual-gene records, but this was not demonstrated by the retrieved evidence. No aneuploidy, translocation, inversion, repeat expansion, mitochondrial mutation, or epigenetic cause is established. (OpenTargets Search: muscular dystrophy, limb-girdle, autosomal recessive 28)

No validated modifier genes, protective alleles, DNA-methylation signature, histone abnormality, or disease-specific chromatin mechanism has been reported.

## 5. Environmental information

No toxin, radiation, pollution, occupation, infection, diet, smoking, alcohol exposure, or exercise pattern is known to cause LGMD-AR28. Safe activity is nevertheless clinically relevant because excessive eccentric loading can aggravate symptoms in many dystrophies, whereas prolonged inactivity promotes deconditioning; this general principle has not been tested specifically here.

**Critical distinction:** statins inhibit the HMGCR protein and may produce toxic muscle symptoms or trigger anti-HMGCR immune-mediated necrotizing myopathy. Neither phenomenon is evidence that statins cause germline LGMD-AR28. Anti-HMGCR myopathy is acquired, antibody-associated, and potentially immunotherapy-responsive; LGMD-AR28 is inherited and biallelic.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic pathogenic HMGCR variants lead to** reduced or dysregulated HMGCR abundance/activity in skeletal muscle; variant causality is reported, whereas the exact biochemical magnitude remains incompletely documented.
2. **Reduced HMGCR activity leads to** impaired conversion of HMG-CoA to mevalonate.
3. **Mevalonate insufficiency results in** reduced availability of downstream sterols and/or nonsterol isoprenoids, including intermediates required for protein prenylation; the disease-specific balance among these branches is inferred.
4. **Branch A—inferred:** altered membrane-lipid/sterol homeostasis **leads to** impaired myofiber membrane and organelle function.
5. **Branch B—inferred:** reduced farnesyl- and geranylgeranyl-derived substrates **lead to** abnormal prenylation and localization of small GTPases, disrupting vesicle trafficking, cytoskeletal regulation, autophagy, and muscle maintenance.
6. **Branch C—inferred:** deficient ubiquinone/dolichol-related pathway output **may lead to** mitochondrial-energy or glycosylation stress.
7. These cellular disturbances **lead to** myofiber dysfunction, degeneration, and inadequate regeneration; direct demonstration in LGMD-AR28 tissue remains limited.
8. Progressive loss of functional proximal myofibers **results in** the limb-girdle weakness phenotype. The 2023 report specifically frames the finding as further implicating the **mevalonate pathway in muscle disease**. (OpenTargets Search: muscular dystrophy, limb-girdle, autosomal recessive 28)

### Annotation suggestions

- **GO biological processes:** mevalonate pathway (**GO:0019287**); cholesterol biosynthetic process (**GO:0006695**); isoprenoid biosynthetic process (**GO:0008299**); protein prenylation (**GO:0018342**); skeletal muscle tissue development (**GO:0007519**); muscle cell homeostasis—validate exact current GO identifier.
- **GO molecular function:** hydroxymethylglutaryl-CoA reductase (NADPH) activity (**GO:0004420**, version validation recommended).
- **GO cellular components:** endoplasmic-reticulum membrane (**GO:0005789**), where HMGCR resides; sarcoplasmic reticulum and mitochondrion are mechanistically plausible downstream compartments but not disease-specifically demonstrated.
- **Cell Ontology:** skeletal muscle fiber (**CL:0000188**); skeletal muscle satellite stem cell (**CL:0000594**) as a potential secondary regenerative cell population.

No disease-specific transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, CRISPR-screen, or integrated multi-omics dataset was identified. Immune-mediated necrosis should not be assigned merely because HMGCR is also an autoantigen in an unrelated acquired myopathy.

## 7. Anatomical structures affected

The primary organ is **skeletal muscle**, particularly proximal limb-girdle musculature by the diagnostic label. Suggested terms include skeletal muscle organ (**UBERON:0001630**), pelvic-girdle region and pectoral/shoulder-girdle structures after exact Uberon-version validation, and skeletal muscle fiber (**CL:0000188**). Bilateral involvement is expected for a genetic myopathy, but symmetry was not quantified.

At subcellular level, HMGCR is an integral **endoplasmic-reticulum membrane** enzyme. Downstream effects on sarcolemma, mitochondria, sarcoplasmic reticulum, Golgi trafficking, or lysosome/autophagosome are plausible but not yet demonstrated specifically. Cardiac and respiratory-muscle involvement remains unknown.

## 8. Temporal development

A chronic, inherited, potentially progressive course is consistent with the term muscular dystrophy, but no disease-specific longitudinal cohort was found. The evidence does not support numerical assignment of onset age, annual decline, time to wheelchair use, disease stages, critical intervention windows, remission, or life expectancy.

Spontaneous remission would be biologically unexpected for structural/metabolic genetic disease, but this has not been formally studied. The likely optimal intervention window is before irreversible myofiber loss and fibrofatty replacement; that is a general dystrophy principle, not an established LGMD-AR28 outcome.

## 9. Inheritance and population

Inheritance is **autosomal recessive**. For two heterozygous parents, the theoretical risk per pregnancy is 25% affected, 50% carrier, and 25% unaffected/non-carrier. This calculation assumes both parental variants are pathogenic and segregate conventionally.

Penetrance, age dependence, expressivity, anticipation, germline mosaicism, founder variants, carrier frequency, prevalence, incidence, ethnic enrichment, geographic distribution, and sex ratio are unknown. No registry-based denominator was identified. The disorder should be described as **ultra-rare with unquantified prevalence**, not assigned a fabricated rate. Consanguinity can increase the probability of homozygosity for rare alleles but no LGMD-AR28-specific statistic is available.

## 10. Diagnostics

### Recommended approach

1. Document distribution and tempo of weakness, three-generation pedigree, medication exposure, and systemic features.
2. Measure CK, AST/ALT, aldolase, renal indices if rhabdomyolysis is suspected, and lipid/metabolic parameters. No LGMD-AR28-specific biochemical cutoff exists.
3. Perform EMG/nerve-conduction testing to establish a myopathic pattern and exclude neuropathy when indicated.
4. Use muscle MRI to characterize distribution and select a biopsy site; no subtype-specific MRI pattern is validated.
5. Undertake a comprehensive neuromuscular gene panel, **WES**, or preferably **WGS** with HMGCR included. Analysis should cover SNVs, indels, exon-level copy-number changes, splice variants, and structural variants spanning HMGCR/CERT1.
6. Confirm candidate variants by orthogonal testing, parental segregation, population frequency, phenotype fit, and ACMG/AMP interpretation. RNA sequencing from muscle or fibroblasts may resolve splice variants; enzyme/protein assays would provide valuable functional support.

Single-gene HMGCR testing is reasonable in a strongly matched family or for segregation, but broad sequencing is generally preferable because proximal muscular dystrophy is highly heterogeneous. CMA, karyotyping, FISH, mitochondrial sequencing, and repeat-expansion assays are not first-line tests unless other clinical findings indicate them.

### Differential diagnosis

The differential includes other recessive LGMDs, dystrophinopathy, Pompe disease, metabolic/mitochondrial myopathy, congenital myopathy, spinal muscular atrophy, inflammatory myopathy, endocrine myopathy, and drug-induced myopathy. **Anti-HMGCR antibody testing** is especially relevant when onset is acquired, CK is markedly elevated, statin exposure is present, or necrotizing biopsy pathology suggests immune-mediated disease. A positive anti-HMGCR antibody supports a distinct treatable autoimmune diagnosis and does not establish biallelic HMGCR muscular dystrophy.

No standardized subtype-specific clinical criteria, newborn screen, validated metabolite biomarker, or liquid-biopsy test exists.

## 11. Outcome and prognosis

No disease-specific survival rate, mortality rate, life expectancy, ambulation-loss rate, respiratory decline, cardiac-event rate, or validated patient-reported outcome was identified. Potential morbidity is progressive mobility and self-care impairment, but magnitude and variability remain unknown. Prognostic biomarkers and genotype–phenotype rules have not been established.

Until natural-history data become available, longitudinal monitoring should include motor function, range of motion, falls, pain/fatigue, CK where clinically useful, pulmonary function, and symptom-directed cardiac assessment. Instruments used across LGMD research may be considered, but none is validated specifically for LGMD-AR28.

## 12. Treatment and current applications

There is **no approved disease-modifying treatment, gene therapy, RNA therapy, cell therapy, or genotype-directed drug** for LGMD-AR28, and no disease-specific trial was identified. The anti-HMGCR IVIG trial found during searching concerns autoimmune necrotizing myopathy and is not an LGMD-AR28 trial.

Current real-world management should be multidisciplinary and supportive:

- individualized low-to-moderate intensity physical therapy and avoidance of overwork injury;
- occupational therapy, mobility aids, orthoses, and fall prevention;
- contracture prevention and orthopedic management;
- respiratory surveillance and assisted ventilation/cough support if weakness develops;
- cardiac evaluation based on symptoms and emerging subtype data;
- nutrition, bone health, pain, fatigue, and psychosocial support;
- anesthesia planning as for an undifferentiated muscular dystrophy until specific risks are known.

Suggested NCIt concepts include **Physical Therapy (C15308)**, **Occupational Therapy (C16960)**, **Genetic Counseling (C15240)**, and assisted ventilation concepts after current NCIt validation. Corticosteroids, IVIG, rituximab, and other immunotherapies should not be prescribed solely on the basis of inherited HMGCR variants. Statin initiation or continuation requires individualized specialist review because HMGCR is the affected enzyme, but there is no evidence-based categorical rule for this genotype.

## 13. Prevention

The genetic lesion cannot currently be prevented through lifestyle modification.

- **Primary prevention:** carrier testing in relatives after familial variants are established; reproductive counseling; optional prenatal diagnosis or preimplantation genetic testing for monogenic disease.
- **Secondary prevention:** cascade testing and presymptomatic assessment of at-risk siblings may allow earlier surveillance and rehabilitation, although benefit has not been quantified.
- **Tertiary prevention:** preserve mobility, prevent falls and contractures, vaccinate according to routine schedules, maintain respiratory health, and detect cardiopulmonary complications early.

Population newborn screening is not established. Vaccination does not prevent the genetic disease, although routine respiratory immunization may reduce complications in individuals with respiratory weakness.

## 14. Other species and natural disease

No naturally occurring HMGCR-related limb-girdle muscular dystrophy was identified in companion animals, livestock, or wildlife. There is no zoonotic potential or cross-species transmission because this is a germline Mendelian disorder. HMGCR and the mevalonate pathway are strongly evolutionarily conserved, making comparative models biologically relevant, but conservation alone does not constitute a natural animal disease model.

## 15. Model organisms

No validated knock-in or knockout model reproducing the human biallelic HMGCR-LGMD phenotype was found. Complete Hmgcr loss may be developmentally incompatible and therefore may not model presumed human hypomorphic alleles. Appropriate future models include:

- patient fibroblasts, myoblasts, or iPSC-derived myotubes;
- CRISPR knock-in of patient alleles in human myogenic cells;
- muscle-specific or inducible hypomorphic mouse models;
- zebrafish knock-in/knockdown systems for rapid muscle and locomotor phenotyping.

Priority readouts should include HMGCR abundance/activity, mevalonate and downstream sterol/nonsterol metabolites, protein prenylation, mitochondrial respiration, membrane organization, autophagic flux, myotube formation, CK release, muscle histology, force, and locomotion. Rescue with wild-type HMGCR or carefully titrated downstream metabolites would strengthen causal inference. A major limitation is that pharmacological statin exposure may not faithfully reproduce allele-specific congenital deficiency.

## Recent developments, expert interpretation, and curation recommendations

The principal development in **2023** was recognition that biallelic HMGCR variants can cause an autosomal-recessive LGMD, extending mevalonate-pathway biology into inherited primary muscle disease. The most authoritative interpretation supported by available data is that HMGCR is causal, while the lower-scoring CERT1 association remains unresolved and should not be promoted to independent causality. (OpenTargets Search: muscular dystrophy, limb-girdle, autosomal recessive 28)

For knowledge-base population:

1. Mark **HMGCR–MONDO:0957270** as a recent, limited-evidence recessive association pending full publication and independent replication.
2. Record **CERT1** as uncertain/possibly annotation- or locus-related, not definitively causal.
3. Do not populate exact variants, phenotype frequencies, penetrance, prevalence, or treatment outcomes from the present evidence.
4. Keep **genetic HMGCR-related LGMD**, **statin toxic myopathy**, and **anti-HMGCR immune-mediated necrotizing myopathy** as separate entities.
5. Re-curate when the full Foley et al. cohort, ClinVar submissions, segregation data, functional assays, and additional families become publicly available.

### Core sources

- Foley A, Donkervoort S, Bharucha-Goebel D, et al. *Bi-allelic variants in HMGCR cause limb girdle muscular dystrophy and further implicate the mevalonate pathway in muscle disease.* **Neuromuscular Disorders**, conference abstract, October 2023. DOI: https://doi.org/10.1016/j.nmd.2023.07.195.
- Open Targets Platform disease–target record for **MONDO_0957270**, reporting HMGCR and CERT1 associations and linked literature including **PMID 36745799** and **PMID 37167966**. These PMID links require source-level verification before patient-level curation. (OpenTargets Search: muscular dystrophy, limb-girdle, autosomal recessive 28)

References

1. (OpenTargets Search: muscular dystrophy, limb-girdle, autosomal recessive 28): Open Targets Query (muscular dystrophy, limb-girdle, autosomal recessive 28, 2 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

## Artifacts

- [Edison artifact artifact-00](Muscular_Dystrophy_Limb-girdle_Autosomal_Recessive_28-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 3 |
| Resolved | 3 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 3 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0957270` (8 mentions) - the report calls it "if available"; MONDO calls it **muscular dystrophy, limb-girdle, autosomal recessive 28**