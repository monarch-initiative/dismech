---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-03T16:09:26.208318'
end_time: '2026-09-03T16:17:37.920833'
duration_seconds: 491.71
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Spondyloepiphyseal Dysplasia, Nishimura Type (MIR140-related skeletal
    dysplasia)
  mondo_id: MONDO:0032835
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 21
reference_validation:
  total_references: 9
  verified: 9
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 9
  on_topic: 3
  off_topic: 1
  off_topic_references:
  - DOI:10.1002/jbmr.2438
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 28
  verified: 26
  not_found: 0
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0032835
    reported_labels:
    - if available
    ontology_label: spondyloepiphyseal dysplasia, nishimura type
  obsolete_terms:
  - term_id: GO:0016573
    ontology_label: obsolete histone acetylation
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Spondyloepiphyseal_Dysplasia_Nishimura_Type-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Spondyloepiphyseal Dysplasia, Nishimura Type (MIR140-related skeletal dysplasia)
- **MONDO ID:** MONDO:0032835 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Spondyloepiphyseal Dysplasia, Nishimura Type (MIR140-related skeletal dysplasia)** covering all of the
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
- **Disease Name:** Spondyloepiphyseal Dysplasia, Nishimura Type (MIR140-related skeletal dysplasia)
- **MONDO ID:** MONDO:0032835 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Spondyloepiphyseal Dysplasia, Nishimura Type (MIR140-related skeletal dysplasia)** covering all of the
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


# Spondyloepiphyseal Dysplasia, Nishimura Type (MIR140-Related Skeletal Dysplasia)

## Executive summary and evidence limits

Spondyloepiphyseal dysplasia, Nishimura type is an ultra-rare, autosomal-dominant skeletal dysplasia caused by a neomorphic seed-region variant in the cartilage-enriched microRNA gene **MIR140**. The defining evidence remains the 2019 *Nature Medicine* report of only **three affected people from two unrelated families**. Consequently, phenotype frequencies, penetrance, prevalence, prognosis, and treatment effects cannot yet be estimated reliably. No additional substantive human cohort or disease-specific clinical trial was identified in the 2023–2024 literature searched for this report. The most important recent development is instead a 2023 preclinical metabolic model linking mutant MIR140 to reduced HIF1A/glycolysis, reduced acetyl-CoA and histone acetylation, and possible FGFR3 upregulation in resting-zone chondrocytes. That downstream chain remains partly inferential. (grigelioniene2019gainoffunctionmutationofa pages 1-3, kobayashi2023reducedglycolysislinks pages 26-30, kobayashi2023reducedglycolysislinks pages 1-5)

The compact evidence summary below should be interpreted in light of that very small human denominator.

| Field | Key fact | Evidence / uncertainty |
|---|---|---|
| Disease identity | Spondyloepiphyseal dysplasia, Nishimura type; also **SED, MIR140 type Nishimura** or **MIR140-related skeletal dysplasia** | Ultra-rare, monoallelic Mendelian skeletal dysplasia first delineated in 2019. (grigelioniene2019gainoffunctionmutationof pages 1-3, grigelioniene2019gainoffunctionmutationof pages 6-7) |
| Identifiers | **OMIM 618618**; **Orphanet 163649**; **MONDO:0032835** | Orphanet identifier is supported by Open Targets; OMIM and MONDO identifiers were user-supplied and were not independently verified with the available tools. (OpenTargets Search: Spondyloepiphyseal dysplasia Nishimura type-MIR140) |
| Causal gene / variant | **MIR140** (microRNA 140; Ensembl **ENSG00000208017**); heterozygous **NR_029681.1:n.24A>G**, equivalent to **chr16:g.69967007A>G (hg19)** | The substitution affects the miR-140-5p seed region. Only this recurrent disease-causing variant was established in the retrieved human literature. (grigelioniene2019gainoffunctionmutationof pages 3-4, OpenTargets Search: Spondyloepiphyseal dysplasia Nishimura type-MIR140) |
| Inheritance | Autosomal dominant / monoallelic; de novo in two probands and transmitted from an affected mother to her son | Germline variant with vertical segregation in one family; recurrence risk is 50% for an affected heterozygote, while parental germline mosaicism after an apparently de novo event remains theoretically possible but unquantified. (grigelioniene2019gainoffunctionmutationofa pages 1-3, grigelioniene2019gainoffunctionmutationofa pages 6-7) |
| Known human evidence | **3 affected individuals from 2 unrelated families** in the foundational report; **PMID 30804514** | No substantive additional human cohort was identified through the 2023–2024 literature search, so frequencies and penetrance estimates remain highly uncertain. (grigelioniene2019gainoffunctionmutationofa pages 1-3, OpenTargets Search: Spondyloepiphyseal dysplasia Nishimura type-MIR140) |
| Core phenotype | Disproportionate short stature, short limbs, small hands and feet, severe brachydactyly with cone-shaped phalangeal epiphyses, midface hypoplasia/small nose, delayed hip and knee epiphyseal ossification, small epiphyses, mild platyspondyly/spondylar dysplasia, and scaphocephaly | Adult findings included premature spondylosis and degenerative joint disease; respiratory infections, prolonged cough, stridor, and suspected laryngeal-cartilage laxity/narrowing occurred in two related patients. Intelligence, hearing, vision, dentition, routine blood tests, and age-adjusted bone density were reported as normal where assessed. (grigelioniene2019gainoffunctionmutationofa pages 1-3, grigelioniene2019gainoffunctionmutationof pages 6-7, grigelioniene2019gainoffunctionmutationof pages 3-4) |
| Mechanism | Neomorphic miRNA seed mutation causes **loss of normal targeting plus gain of novel targeting**: wild-type miR-140-5p targets are derepressed, mutant-seed targets are repressed, and mutant miR-140-5p competes with **YBX1** at overlapping RNA sites | Demonstrated in chondrocytes and a corresponding knock-in mouse. A newer preclinical model proposes a downstream **HIF1A↓ → glycolysis↓ → citrate/acetyl-CoA↓ → histone acetylation↓ → FGFR3↑** branch, but direct MIR140-to-FGFR3 epigenetic causality remains inferred. (grigelioniene2019gainoffunctionmutationof pages 1-3, kobayashi2023reducedglycolysislinks pages 26-30, kobayashi2023reducedglycolysislinks pages 1-5) |
| Diagnosis | Recognition of the characteristic spondyloepiphyseal/brachydactyly pattern followed by sequencing that adequately covers **noncoding MIR140**; confirm the variant by an orthogonal method and test parents | WES may miss or inadequately prioritize a microRNA locus; WGS enabled discovery after coding-exome analysis was unrevealing. Differentiate from acrodysostosis, which commonly has advanced carpal ossification, endocrine abnormalities, and **PDE4D** or **PRKAR1A** variants. No standardized disease-specific criteria or validated biochemical biomarker exists. (grigelioniene2019gainoffunctionmutationof pages 6-7, grigelioniene2019gainoffunctionmutationofa pages 6-7) |
| Management / trials | No disease-modifying drug, gene/RNA therapy, approved targeted treatment, or disease-specific interventional trial was identified | Care is supportive and individualized: orthopedic and spine surveillance, joint/pain management, physical and occupational therapy, airway/ENT evaluation when symptomatic, and genetic counseling. These measures are extrapolated from skeletal-dysplasia practice rather than tested specifically in MIR140 disease. |
| Epidemiology | Prevalence, incidence, carrier frequency, sex ratio, ethnic enrichment, and geographic distribution are unknown | Only three molecularly confirmed individuals in two families were documented in the retrieved primary human evidence; no founder effect is known. (grigelioniene2019gainoffunctionmutationofa pages 1-3) |
| Models | CRISPR **Mir140 seed knock-in mouse**, **Mir140-null mouse**, primary mouse chondrocytes, reporter/transcriptomic systems, and zebrafish functional assays | Seed knock-in mice reproduce delayed ossification, reduced **Col10a1**, widened growth plates, expanded resting zones, reduced epiphyseal mineralization, and mildly flat vertebrae; null mice show distinct loss-of-function biology involving **DNPEP/BMP** and **PTHrP–HDAC4–MEF2C/p38** pathways. No naturally occurring veterinary counterpart was identified. (grigelioniene2019gainoffunctionmutationof pages 3-4, papaioannou2015microrna‐140providesrobustness pages 19-22, nakamura2011chondrocytespecificmicrorna140regulates pages 1-2, nakamura2011chondrocytespecificmicrorna140regulates pages 9-10) |


*Table: Compact evidence summary of the disease identity, defining MIR140 variant, clinical spectrum, mechanism, diagnosis, management, epidemiology, and experimental models. It highlights where conclusions rest on only three reported human cases or on preclinical evidence.*

## 1. Disease information

### Definition and nomenclature

The disorder is a congenital growth-plate disease affecting endochondral ossification, vertebral bodies, epiphyses, and short tubular bones. Preferred and alternative names include:

- **Spondyloepiphyseal dysplasia, Nishimura type**
- **Spondyloepiphyseal dysplasia, MIR140 type**
- **SED MIR140 type Nishimura**
- **MIR140-related skeletal dysplasia**

The foundational authors proposed the Nishimura eponym after identifying the same MIR140 variant in two unrelated families. (grigelioniene2019gainoffunctionmutationof pages 6-7, grigelioniene2019gainoffunctionmutationofa pages 6-7)

### Identifiers

- **OMIM phenotype:** 618618. Some secondary snippets incorrectly associate 611894 with this entity; 618618 is the identifier consistently attached to SED MIR140 type in the retrieved disease reviews.
- **Orphanet:** ORPHA:163649, independently represented in Open Targets.
- **MONDO:** MONDO:0032835, supplied in the request but not independently resolved by the available tools.
- **Causal-gene identifiers:** MIR140; Ensembl **ENSG00000208017**; approved name “microRNA 140.” (OpenTargets Search: Spondyloepiphyseal dysplasia Nishimura type-MIR140)
- **ICD-10/ICD-11 and MeSH:** no disease-specific code or descriptor was found. It would ordinarily be represented under a broader osteochondrodysplasia/spondyloepiphyseal-dysplasia category.

The clinical information is **individual-patient evidence** from three published cases; identifiers and gene associations are aggregated disease-level resources derived largely from that report and animal data. Open Targets identifies MIR140 as the sole associated target and gives an aggregate association score of 0.385, drawing on EVA, Gene2Phenotype, IMPC, ClinGen, and the primary publication. (OpenTargets Search: Spondyloepiphyseal dysplasia Nishimura type-MIR140)

## 2. Etiology, risk, protection, and environment

### Primary cause

The established cause is a **germline heterozygous MIR140 seed-region substitution**, **NR_029681.1:n.24A>G**, corresponding to **chr16:g.69967007A>G (hg19)**. It changes the first nucleotide of the mature miR-140-5p seed and creates an altered target-recognition repertoire. The lesion is not a conventional protein missense variant: Sequence Ontology class **mature_miRNA_variant, SO:0001620** is appropriate. (grigelioniene2019gainoffunctionmutationof pages 3-4, OpenTargets Search: Spondyloepiphyseal dysplasia Nishimura type-MIR140)

The variant arose de novo in the two independent probands and was transmitted from an affected mother to her son in one family. This establishes monoallelic autosomal-dominant causation. No second pathogenic MIR140 allele or susceptibility locus was established in the retrieved human literature. (grigelioniene2019gainoffunctionmutationofa pages 1-3, grigelioniene2019gainoffunctionmutationofa pages 6-7)

### Risk and protective factors

- **Genetic risk:** carrying the pathogenic seed variant is the only demonstrated risk factor. An affected heterozygote has a theoretical 50% transmission probability per pregnancy.
- **Modifiers:** no human modifier gene is established. Experimental genetic interaction with **Pthrp** and **Hdac4**, but not clearly with **Ihh**, has been demonstrated in Mir140-null mice; this is pathway evidence, not a validated human modifier association. (papaioannou2015microrna‐140providesrobustness pages 9-12)
- **Protective variants:** none reported.
- **Environmental, lifestyle, occupational, dietary, toxic, or infectious causes:** none supported. This is a congenital Mendelian disorder, not an acquired dysplasia.
- **Gene–environment interaction:** none demonstrated. Mechanical loading, aging, and body weight could plausibly influence secondary joint degeneration, but this has not been studied in MIR140 patients.

## 3. Phenotypes

The denominator is three, so statements such as “all” or “two of three” describe the original case series rather than stable population frequencies.

| Clinical domain | Reported characteristics and course | Suggested ontology terms |
|---|---|---|
| Growth | Congenital/developmental disproportionate short stature with short limbs; severity appears compatible with survival into adulthood, but standardized height data were not available in the extracted evidence | Short stature **HP:0004322**; disproportionate short stature **HP:0003498**; micromelia **HP:0002983** |
| Hands and feet | Small hands and feet, severe brachydactyly, and cone-shaped phalangeal epiphyses | Brachydactyly **HP:0001156**; small hand **HP:0200055**; cone-shaped epiphyses **HP:0010579** |
| Spine | Mild spondylar dysplasia/platyspondyly during development; premature spondylosis in adulthood | Platyspondyly **HP:0000926**; spondylosis |
| Epiphyses/joints | Delayed hip and knee epiphyseal ossification, small epiphyses, epiphyseal dysplasia; premature degenerative joint disease in adults | Delayed epiphyseal ossification; epiphyseal dysplasia **HP:0002656**; osteoarthritis **HP:0002758** |
| Craniofacial | Midface hypoplasia, small/short nose, and scaphocephaly | Midface retrusion **HP:0011800**; scaphocephaly **HP:0030799** |
| Respiratory/airway | Recurrent respiratory infections, prolonged cough, inspiratory stridor, and suspected narrow/floppy laryngeal cartilage in the affected mother and son | Recurrent respiratory infections **HP:0002205**; stridor **HP:0010307**; laryngomalacia **HP:0001601**, if clinically confirmed |
| Preserved findings | Intelligence, dentition, hearing, vision, routine blood tests, and endocrine evaluation were reported normal where assessed; age-adjusted bone density was normal in the 43-year-old woman | These are useful negative phenotypes, not defining HPO disease features |

These manifestations and negative findings derive from the foundational human report. Adult findings show that the skeletal dysplasia is lifelong and that joint/spine morbidity may progress even after linear growth ends. (grigelioniene2019gainoffunctionmutationofa pages 1-3, grigelioniene2019gainoffunctionmutationof pages 1-3, grigelioniene2019gainoffunctionmutationof pages 6-7)

**Quality of life:** no EQ-5D, SF-36, PROMIS, pain score, mobility scale, or formal patient-reported outcome was published. Short stature, hand/foot disproportion, degenerative joint disease, spondylosis, and airway symptoms are likely to affect mobility, pain, activities of daily living, and respiratory well-being, but disease-specific effect sizes are unavailable.

## 4. Genetic and molecular information

### Gene and variant interpretation

**MIR140** encodes miR-140-5p and miR-140-3p rather than a protein. It is highly enriched in cartilage and lies in a chondrocyte-specific super-enhancer context. The n.24A>G lesion is a seed change with a combined **loss of normal function and neomorphic gain of function**, not simple haploinsufficiency. The corresponding knock-in phenotype differs from Mir140-null mice, strongly supporting that interpretation. (grigelioniene2019gainoffunctionmutationof pages 1-3, grigelioniene2019gainoffunctionmutationof pages 3-4, nakamura2011chondrocytespecificmicrorna140regulates pages 1-2)

The human evidence and ClinVar/EVA-linked record support pathogenicity, although the Open Targets extraction notes that the EVA assertion had no supplied assertion criteria. A knowledge-base entry should therefore retain the primary functional evidence rather than relying only on an automated ACMG label. (OpenTargets Search: Spondyloepiphyseal dysplasia Nishimura type-MIR140)

- **Variant class:** single-nucleotide mature-miRNA seed variant.
- **Origin:** germline; de novo in two probands and inherited in one affected child.
- **Population frequency:** no frequency was supplied by the retrieved sources; the recurrence in two unrelated families and de novo observations imply an extremely rare allele. It should be checked directly in the current gnomAD release before clinical reporting.
- **Other variants:** no additional definitively disease-causing MIR140 variants were found.
- **Chromosomal abnormalities:** none established as causative.
- **Somatic variation:** not relevant to the congenital disorder.
- **Epigenetics:** MIR140 is super-enhancer associated. Reduced histone acetylation is seen in mutant mouse chondrocytes, but no patient-specific DNA-methylation or chromatin signature is validated. (grigelioniene2019gainoffunctionmutationof pages 1-3, kobayashi2023reducedglycolysislinks pages 26-30)

## 5. Environmental information

No toxin, radiation, pollution, occupation, diet, smoking, alcohol, exercise pattern, or pathogen is known to initiate the disorder. Environmental measures cannot prevent a de novo germline seed mutation. Ordinary orthopedic risk factors may modify secondary osteoarthritis, but no MIR140-specific epidemiologic evidence exists. Infectious disease is not etiologic; recurrent respiratory infections in two patients were manifestations or complications, possibly related to airway cartilage. (grigelioniene2019gainoffunctionmutationofa pages 1-3)

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Heterozygous MIR140 n.24A>G alters the first nucleotide of the miR-140-5p seed, which leads to a new RNA-target recognition sequence.**
2. **High chondrocyte expression of mutant miR-140-5p leads to simultaneous derepression of normal miR-140-5p targets and repression of novel mutant-seed targets.**
3. **Mutant miR-140-5p binding overlaps and competes with YBX1, which leads to unusually strong repression of newly recognized transcripts.**
4. **The altered chondrocyte transcriptome leads to impaired growth-plate maturation, reduced COL10A1, widened growth plates, expansion of resting-zone chondrocytes, and delayed epiphyseal mineralization.**
5. **These growth-plate abnormalities lead to delayed endochondral ossification, small/dysplastic epiphyses, short limbs, brachydactyly, platyspondyly, and disproportionate short stature.**
6. **Abnormal epiphyseal and articular-cartilage development likely leads to premature spondylosis and degenerative joint disease in adulthood** *(clinically supported, exact molecular bridge inferred)*.
7. **Branch—metabolic model:** mutant Mir140 leads to reduced Hif1a and glycolytic adaptation, which leads to lower cytoplasmic citrate/acetyl-CoA and histone acetylation, which may lead to increased Fgfr3 expression/signaling and resting-zone expansion *(mouse evidence; direct MIR140→epigenetic FGFR3 causality remains inferred)*. (grigelioniene2019gainoffunctionmutationof pages 3-4, kobayashi2023reducedglycolysislinks pages 26-30, kobayashi2023reducedglycolysislinks pages 1-5)

### Detailed pathway interpretation

The 2019 study demonstrated abundant mutant miR-140-5p without a gross miRNA-processing defect. Chondrocyte transcriptomics showed widespread loss of repression of wild-type targets and gain of repression at novel, particularly predicted 8-mer, mutant-seed sites. Competition with **YBX1**, an RNA-binding protein recognizing overlapping motifs, provides a mechanistic explanation for the potency of a newly created miRNA seed that lacks evolutionary coadaptation with its targets. The authors’ abstract states: **“the mutation produces both loss-of-function and gain-of-function effects”** and describes the report as **“the first case of a pathogenic gain-of-function miRNA mutation.”** (grigelioniene2019gainoffunctionmutationof pages 1-3, grigelioniene2019gainoffunctionmutationof pages 3-4)

The 2023 preprint broadened this model. Chondrocyte-specific deletion of **Ldha/Ldhb** reduced glycolysis and reproduced resting-zone expansion; deletion of **Acly** reduced acetyl-CoA and reproduced the phenotype without generalized energy deficiency. Overlapping transcriptomic changes included **Fgfr3** upregulation, and constitutively active FGFR3 expanded the resting zone. The authors’ abstract concludes that reduced glycolysis is linked to acetyl-CoA deficiency, **“possibly through epigenetic upregulation of FGFR3 signaling.”** “Possibly” is critical: direct increased FGFR3 signaling and direct chromatin deregulation of Fgfr3 were not demonstrated in the extracted evidence. RNA-seq data were deposited as **GEO GSE192971**. (kobayashi2023reducedglycolysislinks pages 26-30, kobayashi2023reducedglycolysislinks pages 1-5, kobayashi2023reducedglycolysislinks pages 5-8)

Relevant processes and ontology suggestions include:

- miRNA-mediated post-transcriptional gene silencing — **GO:0035195**
- regulation of gene expression — **GO:0010468**
- chondrocyte differentiation — **GO:0002062**
- cartilage development — **GO:0051216**
- endochondral ossification — **GO:0001958**
- histone acetylation — **GO:0016573**
- glycolytic process — **GO:0006096**
- BMP signaling — **GO:0030509**
- MAPK cascade — **GO:0000165**
- principal cell: chondrocyte — **CL:0000138**; resting, proliferative, and hypertrophic growth-plate chondrocyte subtypes should be represented where the target ontology supports them.

**Important distinction:** Mir140-null mechanisms—DNPEP/BMP attenuation, increased p38-MAPK/MEF2C, and interaction with PTHrP–HDAC4—clarify normal miR-140 biology but are not equivalent to the human seed-mutant mechanism. Null mice have short endochondral bones, craniofacial abnormalities, accelerated hypertrophy, and impaired resting-to-columnar differentiation; heterozygous null mice were reportedly indistinguishable from wild type. (papaioannou2015microrna‐140providesrobustness pages 19-22, nakamura2011chondrocytespecificmicrorna140regulates pages 1-2, nakamura2011chondrocytespecificmicrorna140regulates pages 9-10)

No disease-specific proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, patient-iPSC, organoid, or CRISPR-screen dataset was identified. Lipid synthesis and Ras prenylation showed no overt deficit in the metabolic models, arguing against lipid shortage as the principal downstream mechanism. (kobayashi2023reducedglycolysislinks pages 26-30)

## 7. Anatomical structures affected

Primary involvement is bilateral/systemic rather than unilateral:

- **Organs/system:** skeleton and joints; possible upper airway cartilage.
- **Sites:** vertebral bodies, long-bone growth plates and epiphyses—especially hip and knee—phalanges, skull, and facial skeleton.
- **Tissues:** hyaline growth-plate cartilage, epiphyseal/articular cartilage, and bone formed by endochondral ossification.
- **Cells:** resting-zone, proliferating/columnar, prehypertrophic, and hypertrophic chondrocytes; osteoblast abnormalities are secondary to disturbed cartilage-template maturation rather than a demonstrated primary osteoblast lesion.
- **Subcellular structures:** nuclear/cytoplasmic miRNA-processing and Argonaute/RISC machinery; target mRNAs and YBX1-containing ribonucleoprotein interactions. No mitochondrial structural defect is established.

Suggested UBERON concepts include cartilage tissue (**UBERON:0002418**), growth plate cartilage, epiphysis, vertebral body, phalanx, hip joint, knee joint, and laryngeal cartilage. (grigelioniene2019gainoffunctionmutationofa pages 1-3, grigelioniene2019gainoffunctionmutationof pages 3-4)

## 8. Temporal development

Onset is congenital/developmental, although the exact prenatal ultrasound phenotype is unknown. Delayed secondary ossification and disproportion become evident in childhood. The disease is chronic and lifelong rather than episodic or remitting. Growth-plate abnormalities dominate childhood; premature spondylosis and degenerative joint disease emerge or worsen in adulthood. A 45-year-old affected woman and her affected son demonstrate survival into adulthood and vertical transmission. (grigelioniene2019gainoffunctionmutationof pages 6-7, grigelioniene2019gainoffunctionmutationofa pages 6-7)

There is no validated staging system, progression rate, remission pattern, or critical therapeutic window. Biologically, the period before growth-plate closure is likely the principal window for any future growth-directed intervention, whereas lifelong surveillance addresses joint, spine, and airway complications.

## 9. Inheritance and population

- **Inheritance:** autosomal dominant, monoallelic.
- **Penetrance:** appears high for the reported variant because all three carriers were affected, but three observations cannot establish complete penetrance.
- **Expressivity:** some variability is evident, especially age-dependent degeneration and respiratory involvement.
- **Anticipation:** not reported and mechanistically unexpected for a single-nucleotide variant.
- **Mosaicism:** no somatic or germline mosaic case reported; low-level parental germline mosaicism remains a standard theoretical consideration after an apparently de novo diagnosis.
- **Founder effect/consanguinity:** none reported; consanguinity is not relevant to the dominant mechanism.
- **Carrier frequency, incidence, prevalence, sex ratio, ethnicity, and geographic distribution:** unknown. The evidence base—three affected individuals in two unrelated families—is too small for rates per 100,000 or demographic inference. (grigelioniene2019gainoffunctionmutationofa pages 1-3)

## 10. Diagnostics

### Clinical and radiographic diagnosis

A diagnostic work-up should begin with history, three-generation pedigree, anthropometry including sitting-height/leg-length proportions, hand and foot examination, and a skeletal survey. Hallmark radiographic findings are delayed hip/knee epiphyseal ossification, small or dysplastic epiphyses, cone-shaped phalangeal epiphyses, severe brachydactyly, and mild platyspondyly. Spine and joint imaging should be symptom directed in adults. Airway endoscopy or dynamic imaging may be considered for stridor, but no disease-specific airway protocol exists. (grigelioniene2019gainoffunctionmutationofa pages 1-3, grigelioniene2019gainoffunctionmutationof pages 3-4)

No diagnostic serum enzyme, metabolite, circulating miRNA, histopathologic criterion, or electrophysiologic biomarker is validated. Routine laboratory and endocrine tests may help exclude mimics but can be normal in MIR140 disease. (grigelioniene2019gainoffunctionmutationof pages 1-3, grigelioniene2019gainoffunctionmutationof pages 6-7)

### Genetic testing strategy

1. Use a skeletal-dysplasia panel that explicitly includes **noncoding MIR140**, or WGS with analysis of miRNA genes.
2. If prior WES was negative, review whether MIR140 was captured and interpreted; the original discovery required WGS after coding-exome analysis did not identify a cause.
3. Confirm a candidate variant by an orthogonal assay and perform parental testing to determine de novo versus inherited status.
4. Use segregation, population databases, mature-miRNA seed location, and functional literature in classification.

CMA, karyotyping, FISH, mitochondrial sequencing, and repeat-expansion testing are not first-line tests for the canonical phenotype unless another diagnosis is suspected. RNA-seq, proteomics, metabolomics, and methylation profiling remain research tools rather than validated diagnostics. (grigelioniene2019gainoffunctionmutationofa pages 6-7)

### Differential diagnosis

The closest explicitly discussed mimic is **acrodysostosis** due to **PDE4D** or **PRKAR1A**. Both can cause midface hypoplasia and brachydactyly with cone epiphyses. MIR140 disease instead shows delayed epiphyseal maturation/epiphyseal dysplasia, whereas acrodysostosis characteristically has advanced carpal maturation and may include endocrine resistance. The reported MIR140 patients lacked PDE4D/PRKAR1A variants and characteristic endocrine abnormalities. (grigelioniene2019gainoffunctionmutationof pages 6-7, grigelioniene2019gainoffunctionmutationofa pages 6-7)

Other radiographic differentials include COL2A1-related spondyloepiphyseal dysplasia, TRPV4-related dysplasias, ACAN-related short stature/spondyloepiphyseal dysplasia, multiple epiphyseal dysplasia, and other brachydactyly–epiphyseal dysplasia syndromes; molecular testing is usually decisive.

There is no newborn population screening. Once a familial variant is known, cascade testing, prenatal diagnosis, and preimplantation genetic testing are technically possible after nondirective genetic counseling.

## 11. Outcome and prognosis

No survival curve, mortality rate, life-expectancy estimate, disability-adjusted life-year analysis, or validated prognostic biomarker exists. Survival into the fifth decade is documented, and no lethal visceral phenotype was reported. Normal intelligence and absence of a consistent major neurologic, cardiac, renal, or endocrine disorder are relatively favorable findings. (grigelioniene2019gainoffunctionmutationof pages 1-3, grigelioniene2019gainoffunctionmutationof pages 6-7)

Likely major morbidity is orthopedic: short stature, altered biomechanics, premature joint degeneration, spondylosis, pain, and mobility limitation. Respiratory morbidity may occur when laryngeal cartilage is involved. Recovery from the underlying dysplasia is not expected; symptomatic function may improve with rehabilitation or orthopedic treatment. Age, baseline epiphyseal abnormality, mechanical joint burden, and airway involvement are plausible prognostic factors, but none is validated.

## 12. Treatment and current applications

No approved disease-modifying treatment, genotype-directed drug, RNA therapy, gene therapy, cell therapy, or MIR140-specific surgical outcome series exists. No disease-specific ClinicalTrials.gov interventional study was identified. Broad skeletal-disorder observational studies should not be treated as therapeutic evidence for this disease.

Current real-world care is therefore individualized and multidisciplinary:

- pediatric genetics and skeletal-dysplasia expertise;
- serial growth, limb-alignment, hip/knee, and spine assessment;
- physical therapy, occupational therapy, joint protection, weight optimization, and mobility aids when needed;
- standard analgesic and osteoarthritis care, individualized to age and comorbidity;
- orthopedic procedures for clinically significant deformity or end-stage joint disease, based on anatomy rather than disease-specific evidence;
- ENT/pulmonology evaluation for stridor, recurrent infections, or suspected laryngomalacia;
- genetic counseling and psychosocial support.

Suggested NCIt intervention concepts include **Genetic Counseling**, **Physical Therapy**, **Occupational Therapy**, **Pain Management**, **Orthopedic Surgery**, and **Respiratory Monitoring**. No response rate or MIR140-specific adverse-event estimate is available.

Although mutant-miRNA inhibition, seed-selective oligonucleotides, restoration of wild-type target regulation, or modulation of downstream FGFR3 signaling are conceivable precision strategies, none has reached human testing. Because the mutant combines loss and gain of targeting, nonspecific miR-140 replacement or inhibition could worsen one mechanistic branch; target and allele selectivity would be essential. The 2023 FGFR3 observation is hypothesis-generating, not a basis for off-label FGFR inhibition. (kobayashi2023reducedglycolysislinks pages 26-30, kobayashi2023reducedglycolysislinks pages 1-5)

## 13. Prevention

Primary prevention by lifestyle or vaccination is not applicable. For affected families, reproductive prevention options are genetic counseling, familial-variant testing, prenatal diagnosis, and preimplantation genetic testing. For an apparently de novo case, recurrence risk is low but not zero because parental germline mosaicism cannot be excluded; an affected heterozygote has a 50% transmission risk.

Secondary prevention consists of early molecular diagnosis and surveillance for growth, alignment, spine/joint degeneration, and airway symptoms. Tertiary prevention includes joint protection, rehabilitation, healthy weight, timely orthopedic care, and respiratory management. There is no prophylactic medication, immunization, public-health program, or population carrier-screening recommendation specific to MIR140 disease.

## 14. Other species and natural disease

No naturally occurring MIR140-associated veterinary disease, breed predisposition, zoonotic transmission, or cross-species infectious risk was identified. Relevant experimental species are:

- **Mus musculus**, NCBI Taxonomy **10090**: Mir140-null and seed knock-in models.
- **Danio rerio**, NCBI Taxonomy **7955**: miR-140/Dnpep functional developmental assays.
- **Homo sapiens**, NCBI Taxonomy **9606**: human disease and cultured-cell evidence.

MIR140 sequence and cartilage enrichment are evolutionarily conserved, supporting comparative validity, but engineered phenotypes must not be labeled natural animal disease. (nakamura2011chondrocytespecificmicrorna140regulates pages 1-2, nakamura2011chondrocytespecificmicrorna140regulates pages 9-10, OpenTargets Search: Spondyloepiphyseal dysplasia Nishimura type-MIR140)

## 15. Model organisms

### Seed knock-in mouse—the closest disease model

CRISPR mice carrying the corresponding A-to-G seed substitution show dose-dependent skeletal abnormalities. Heterozygous and homozygous animals exhibit short stature/short nose, delayed ossification, reduced **Col10a1**, delayed cartilage maturation, reduced epiphyseal mineralization, widened growth plates, expanded resting zones, and mildly flattened vertebral bodies. Their phenotype differs from Mir140-null mice, reproducing the human neomorphic mechanism rather than simple deficiency. Limitations include species-specific growth-plate biology, greater severity in homozygotes—whereas known patients are heterozygous—and incomplete modeling of adult joint, airway, and quality-of-life outcomes. (grigelioniene2019gainoffunctionmutationof pages 3-4, grigelioniene2019gainoffunctionmutationofa pages 3-4, kobayashi2023reducedglycolysislinks pages 5-8)

### Mir140-null mouse

Null mice have growth retardation, shortened endochondral bones, craniofacial deformation, fewer columnar proliferating chondrocytes, accelerated hypertrophic differentiation, and impaired resting-to-columnar transition. Mechanistic experiments implicate **DNPEP-mediated attenuation of BMP signaling** and a **PTHrP–HDAC4–MEF2C/p38-MAPK** regulatory axis. PTHrP-pathway activation partially rescued skeletal defects, while reduced Pthrp or Hdac4 dosage worsened them. These models define physiological miR-140 functions but only partially model the loss-of-normal-targeting branch of the human mutation. (papaioannou2015microrna‐140providesrobustness pages 19-22, papaioannou2015microrna‐140providesrobustness pages 9-12, nakamura2011chondrocytespecificmicrorna140regulates pages 1-2)

### Cellular, zebrafish, and omics systems

Primary mouse rib chondrocytes, reporter assays, small-RNA sequencing, and transcriptomics demonstrated altered wild-type and mutant target repression and YBX1 competition. Zebrafish assays showed that Dnpep transcripts could rescue a miR-140-induced palatal defect, supporting direct miR-140–Dnpep regulation. The 2023 Ldh/Acly/Fgfr3 mouse and chondrocyte systems probe the metabolic/epigenetic branch; they are valuable for target validation but are not themselves MIR140-specific therapies. (grigelioniene2019gainoffunctionmutationof pages 1-3, kobayashi2023reducedglycolysislinks pages 1-5, nakamura2011chondrocytespecificmicrorna140regulates pages 9-10)

## Recent research status and expert assessment

The 2024 review literature recognizes MIR140 skeletal dysplasia as a paradigmatic rare disease caused by altered microRNA target recognition, but it does not add a new clinical cohort. The field’s authoritative interpretation is that this is not merely miR-140 deficiency: the disease arises from simultaneous loss of ancestral targeting and acquisition of a novel, YBX1-competing target network. (grigelioniene2019gainoffunctionmutationof pages 1-3, goel2024micrornaandrare pages 14-15)

The strongest unmet needs are independent case ascertainment, standardized longitudinal phenotyping, current population-frequency confirmation, patient-derived chondrocytes or iPSCs, direct mapping of mutant targets responsible for human disease, validation of the proposed HIF1A–acetyl-CoA–FGFR3 branch, and development of allele-selective RNA therapeutics. Until those gaps are addressed, clinical decisions should rely on molecular confirmation, radiographic pattern recognition, multidisciplinary supportive care, and transparent acknowledgment that most mechanistic depth comes from engineered animals and cells rather than treatment studies.

## Key publications and URLs

1. **Grigelioniene G, et al.** “Gain-of-function mutation of microRNA-140 in human skeletal dysplasia.” *Nature Medicine*. Published online 25 February 2019; 25:583–590. **PMID: 30804514**. DOI/URL: https://doi.org/10.1038/s41591-019-0353-2. This is the defining primary human, mouse, and mechanistic study. (grigelioniene2019gainoffunctionmutationof pages 1-3, OpenTargets Search: Spondyloepiphyseal dysplasia Nishimura type-MIR140)
2. **Kobayashi T, Young C, Zhou W, Rhee EP.** “Reduced glycolysis links resting zone chondrocyte proliferation in the growth plate.” *bioRxiv*. January 2023. DOI/URL: https://doi.org/10.1101/2023.01.18.524550. Preclinical preprint; GEO **GSE192971**. (kobayashi2023reducedglycolysislinks pages 1-5, kobayashi2023reducedglycolysislinks pages 5-8)
3. **Nakamura Y, et al.** “Chondrocyte-Specific MicroRNA-140 Regulates Endochondral Bone Development and Targets Dnpep To Modulate Bone Morphogenetic Protein Signaling.” *Molecular and Cellular Biology*. 2011;31:3019–3028. DOI/URL: https://doi.org/10.1128/MCB.05178-11. Primary mouse/chondrocyte study. (nakamura2011chondrocytespecificmicrorna140regulates pages 1-2, nakamura2011chondrocytespecificmicrorna140regulates pages 9-10)
4. **Papaioannou G, et al.** “MicroRNA-140 Provides Robustness to the Regulation of Hypertrophic Chondrocyte Differentiation by the PTHrP-HDAC4 Pathway.” *Journal of Bone and Mineral Research*. June 2015;30:1044–1052. DOI/URL: https://doi.org/10.1002/jbmr.2438. Primary mouse/chondrocyte study. (papaioannou2015microrna‐140providesrobustness pages 19-22, papaioannou2015microrna‐140providesrobustness pages 9-12)
5. **Goel H, Goel A.** “MicroRNA and Rare Human Diseases.” *Genes*. September 2024;15:1243. DOI/URL: https://doi.org/10.3390/genes15101243. Recent review; useful context but not new patient evidence. (goel2024micrornaandrare pages 14-15)

References

1. (grigelioniene2019gainoffunctionmutationofa pages 1-3): G. Grigelioniene, Hiroshi I. Suzuki, F. Taylan, Fatemeh Mirzamohammadi, Z. Borochowitz, U. Ayturk, S. Tzur, E. Horemuzova, A. Lindstrand, M. Weis, Gintautas Grigelionis, A. Hammarsjö, E. Marsk, A. Nordgren, M. Nordenskjöld, D. Eyre, M. Warman, G. Nishimura, P. Sharp, and Tatsuya Kobayashi. Gain-of-function mutation of microrna-140 in human skeletal dysplasia. Sep 2019. URL: https://doi.org/10.1530/ey.16.5.6, doi:10.1530/ey.16.5.6. This article has 89 citations.

2. (kobayashi2023reducedglycolysislinks pages 26-30): Tatsuya Kobayashi, Cameron Young, Wen Zhou, and Eugene P. Rhee. Reduced glycolysis links resting zone chondrocyte proliferation in the growth plate. bioRxiv, Jan 2023. URL: https://doi.org/10.1101/2023.01.18.524550, doi:10.1101/2023.01.18.524550. This article has 4 citations.

3. (kobayashi2023reducedglycolysislinks pages 1-5): Tatsuya Kobayashi, Cameron Young, Wen Zhou, and Eugene P. Rhee. Reduced glycolysis links resting zone chondrocyte proliferation in the growth plate. bioRxiv, Jan 2023. URL: https://doi.org/10.1101/2023.01.18.524550, doi:10.1101/2023.01.18.524550. This article has 4 citations.

4. (grigelioniene2019gainoffunctionmutationof pages 1-3): Giedre Grigelioniene, Hiroshi I. Suzuki, Fulya Taylan, Fatemeh Mirzamohammadi, Zvi U. Borochowitz, Ugur M. Ayturk, Shay Tzur, Eva Horemuzova, Anna Lindstrand, Mary Ann Weis, Gintautas Grigelionis, Anna Hammarsjö, Elin Marsk, Ann Nordgren, Magnus Nordenskjöld, David R. Eyre, Matthew L. Warman, Gen Nishimura, Phillip A. Sharp, and Tatsuya Kobayashi. Gain-of-function mutation of microrna-140 in human skeletal dysplasia. Feb 2019. URL: https://doi.org/10.1038/s41591-019-0353-2, doi:10.1038/s41591-019-0353-2. This article has 112 citations and is from a highest quality peer-reviewed journal.

5. (grigelioniene2019gainoffunctionmutationof pages 6-7): Giedre Grigelioniene, Hiroshi I. Suzuki, Fulya Taylan, Fatemeh Mirzamohammadi, Zvi U. Borochowitz, Ugur M. Ayturk, Shay Tzur, Eva Horemuzova, Anna Lindstrand, Mary Ann Weis, Gintautas Grigelionis, Anna Hammarsjö, Elin Marsk, Ann Nordgren, Magnus Nordenskjöld, David R. Eyre, Matthew L. Warman, Gen Nishimura, Phillip A. Sharp, and Tatsuya Kobayashi. Gain-of-function mutation of microrna-140 in human skeletal dysplasia. Feb 2019. URL: https://doi.org/10.1038/s41591-019-0353-2, doi:10.1038/s41591-019-0353-2. This article has 112 citations and is from a highest quality peer-reviewed journal.

6. (OpenTargets Search: Spondyloepiphyseal dysplasia Nishimura type-MIR140): Open Targets Query (Spondyloepiphyseal dysplasia Nishimura type-MIR140, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

7. (grigelioniene2019gainoffunctionmutationof pages 3-4): Giedre Grigelioniene, Hiroshi I. Suzuki, Fulya Taylan, Fatemeh Mirzamohammadi, Zvi U. Borochowitz, Ugur M. Ayturk, Shay Tzur, Eva Horemuzova, Anna Lindstrand, Mary Ann Weis, Gintautas Grigelionis, Anna Hammarsjö, Elin Marsk, Ann Nordgren, Magnus Nordenskjöld, David R. Eyre, Matthew L. Warman, Gen Nishimura, Phillip A. Sharp, and Tatsuya Kobayashi. Gain-of-function mutation of microrna-140 in human skeletal dysplasia. Feb 2019. URL: https://doi.org/10.1038/s41591-019-0353-2, doi:10.1038/s41591-019-0353-2. This article has 112 citations and is from a highest quality peer-reviewed journal.

8. (grigelioniene2019gainoffunctionmutationofa pages 6-7): G. Grigelioniene, Hiroshi I. Suzuki, F. Taylan, Fatemeh Mirzamohammadi, Z. Borochowitz, U. Ayturk, S. Tzur, E. Horemuzova, A. Lindstrand, M. Weis, Gintautas Grigelionis, A. Hammarsjö, E. Marsk, A. Nordgren, M. Nordenskjöld, D. Eyre, M. Warman, G. Nishimura, P. Sharp, and Tatsuya Kobayashi. Gain-of-function mutation of microrna-140 in human skeletal dysplasia. Sep 2019. URL: https://doi.org/10.1530/ey.16.5.6, doi:10.1530/ey.16.5.6. This article has 89 citations.

9. (papaioannou2015microrna‐140providesrobustness pages 19-22): Garyfallia Papaioannou, Fatemeh Mirzamohammadi, Thomas S Lisse, Shigeki Nishimori, Marc N Wein, and Tatsuya Kobayashi. Microrna‐140 provides robustness to the regulation of hypertrophic chondrocyte differentiation by the pthrp‐hdac4 pathway. Journal of Bone and Mineral Research, 30:1044-1052, Jun 2015. URL: https://doi.org/10.1002/jbmr.2438, doi:10.1002/jbmr.2438. This article has 67 citations and is from a highest quality peer-reviewed journal.

10. (nakamura2011chondrocytespecificmicrorna140regulates pages 1-2): Yukio Nakamura, Jennifer B. Inloes, Takenobu Katagiri, and Tatsuya Kobayashi. Chondrocyte-specific microrna-140 regulates endochondral bone development and targets <i>dnpep</i> to modulate bone morphogenetic protein signaling. Jul 2011. URL: https://doi.org/10.1128/mcb.05178-11, doi:10.1128/mcb.05178-11. This article has 236 citations and is from a domain leading peer-reviewed journal.

11. (nakamura2011chondrocytespecificmicrorna140regulates pages 9-10): Yukio Nakamura, Jennifer B. Inloes, Takenobu Katagiri, and Tatsuya Kobayashi. Chondrocyte-specific microrna-140 regulates endochondral bone development and targets <i>dnpep</i> to modulate bone morphogenetic protein signaling. Jul 2011. URL: https://doi.org/10.1128/mcb.05178-11, doi:10.1128/mcb.05178-11. This article has 236 citations and is from a domain leading peer-reviewed journal.

12. (papaioannou2015microrna‐140providesrobustness pages 9-12): Garyfallia Papaioannou, Fatemeh Mirzamohammadi, Thomas S Lisse, Shigeki Nishimori, Marc N Wein, and Tatsuya Kobayashi. Microrna‐140 provides robustness to the regulation of hypertrophic chondrocyte differentiation by the pthrp‐hdac4 pathway. Journal of Bone and Mineral Research, 30:1044-1052, Jun 2015. URL: https://doi.org/10.1002/jbmr.2438, doi:10.1002/jbmr.2438. This article has 67 citations and is from a highest quality peer-reviewed journal.

13. (kobayashi2023reducedglycolysislinks pages 5-8): Tatsuya Kobayashi, Cameron Young, Wen Zhou, and Eugene P. Rhee. Reduced glycolysis links resting zone chondrocyte proliferation in the growth plate. bioRxiv, Jan 2023. URL: https://doi.org/10.1101/2023.01.18.524550, doi:10.1101/2023.01.18.524550. This article has 4 citations.

14. (grigelioniene2019gainoffunctionmutationofa pages 3-4): G. Grigelioniene, Hiroshi I. Suzuki, F. Taylan, Fatemeh Mirzamohammadi, Z. Borochowitz, U. Ayturk, S. Tzur, E. Horemuzova, A. Lindstrand, M. Weis, Gintautas Grigelionis, A. Hammarsjö, E. Marsk, A. Nordgren, M. Nordenskjöld, D. Eyre, M. Warman, G. Nishimura, P. Sharp, and Tatsuya Kobayashi. Gain-of-function mutation of microrna-140 in human skeletal dysplasia. Sep 2019. URL: https://doi.org/10.1530/ey.16.5.6, doi:10.1530/ey.16.5.6. This article has 89 citations.

15. (goel2024micrornaandrare pages 14-15): Himanshu Goel and Amy Goel. Microrna and rare human diseases. Genes, 15:1243, Sep 2024. URL: https://doi.org/10.3390/genes15101243, doi:10.3390/genes15101243. This article has 20 citations.

## Artifacts

- [Edison artifact artifact-00](Spondyloepiphyseal_Dysplasia_Nishimura_Type-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 9 |
| On topic | 3 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `DOI:10.1002/jbmr.2438` (7 mentions) - MicroRNA-140 Provides Robustness to the Regulation of Hypertrophic Chondrocyte Differentiation by the PTHrP-HDAC4 Pathway
  - shared terms: none

Weighed against this report's own most characteristic terms: `disease`, `human`, `gene`, `clinical`, `dysplasia`, `genetic`, `type`, `affected`, `model`, `mir140`, `variant`, `phenotype`, `target`, `primary`, `joint`, `spondyloepiphyseal`, `skeletal`, `nishimura`, `abnormalitie`, `seed`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 28 |
| Resolved | 26 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0032835` (3 mentions) - the report calls it "if available"; MONDO calls it **spondyloepiphyseal dysplasia, nishimura type**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0016573` (obsolete histone acetylation) (1 mention)

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.