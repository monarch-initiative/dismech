---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-02T13:17:04.268215'
end_time: '2026-09-02T13:25:51.748838'
duration_seconds: 527.48
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Combined Oxidative Phosphorylation Defect Type 13
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 28
reference_validation:
  total_references: 6
  verified: 6
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 6
  on_topic: 2
  validator_version: 0.2.1
term_validation:
  total_terms: 27
  verified: 26
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 6
  labels_matching: 1
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: HP:0001252
    reported_labels:
    - Common early sign, neonatal or infantile
    ontology_label: Hypotonia
  - term_id: HP:0001332
    reported_labels:
    - Common movement disorder; may be progressive
    ontology_label: Dystonia
  - term_id: HP:0002151
    reported_labels:
    - Recurrent biochemical clue, usually mild to moderate; CSF may be elevated or
      normal
    ontology_label: Increased circulating lactate concentration
  - term_id: HP:0002134
    reported_labels:
    - Recurrent, often bilateral; putamen, caudate, globus pallidus, and substantia-nigra
      involvement reported
    ontology_label: Abnormal basal ganglia morphology
  labels_variant: 1
  unresolvable_prefixes:
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Combined_Oxidative_Phosphorylation_Defect_Type_13-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Combined Oxidative Phosphorylation Defect Type 13
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Combined Oxidative Phosphorylation Defect Type 13** covering all of the
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
- **Disease Name:** Combined Oxidative Phosphorylation Defect Type 13
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Combined Oxidative Phosphorylation Defect Type 13** covering all of the
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


# Combined Oxidative Phosphorylation Defect Type 13 (COXPD13)

## Executive summary

Combined oxidative phosphorylation defect/deficiency type 13 is an ultra-rare, autosomal-recessive primary mitochondrial disorder caused by biallelic pathogenic variants in **PNPT1**, which encodes mitochondrial polyribonucleotide phosphorylase (PNPase). Impaired PNPase-dependent mitochondrial RNA processing, turnover, and—in some experimental settings—RNA import disrupts respiratory-chain assembly and oxidative phosphorylation. The clinical spectrum extends from infantile, sometimes static encephalopathy to progressive Leigh syndrome with early death. Hearing loss, movement disorder, developmental impairment, seizures, visual abnormalities, feeding difficulty, growth failure, and elevated lactate are prominent but variably present. Approximately 15 COXPD13 cases had been reported worldwide by a February 2025 review, so phenotype frequencies, penetrance, survival rates, and treatment effects cannot yet be estimated reliably. (li2025anovelpolyribonucleotide pages 1-2, li2025anovelpolyribonucleotide pages 7-10)

The following table provides a compact knowledge-base representation; ontology mappings labeled “suggested” should be verified against the current ontology release before ingestion.

| Domain | Evidence-supported finding | Suggested ontology identifiers |
|---|---|---|
| Disease identity | Combined oxidative phosphorylation defect/deficiency type 13 (COXPD13) is a Mendelian primary mitochondrial disease associated with PNPT1; Open Targets lists MONDO:0013977 for “combined oxidative phosphorylation defect type 13.” OMIM disease number reported in the literature is 614932. Evidence comes from aggregated disease resources plus published individual case reports/series (OpenTargets Search: combined oxidative phosphorylation deficiency 13-PNPT1, li2025anovelpolyribonucleotide pages 7-10). | MONDO:0013977; OMIM:614932; MeSH/ICD: suggestion only, exact mapping not confirmed here |
| Synonyms / scope note | Common names include “combined oxidative phosphorylation deficiency 13,” “combined oxidative phosphorylation defect type 13,” and PNPT1-related mitochondrial disease. Distinguish from PNPT1-related autosomal-recessive nonsyndromic hearing loss and other broader PNPT1 phenotypes such as Leigh syndrome and interferonopathy-like presentations (vedrenne2012mutationinpnpt1 pages 2-3, ameln2012amutationin pages 1-2, matilainen2017defectivemitochondrialrna pages 10-16). | MONDO:0013977; exact synonym curation suggestion only |
| Causal gene / inheritance | Cause is biallelic germline PNPT1 variants encoding mitochondrial polyribonucleotide nucleotidyltransferase 1 (PNPase); inheritance is autosomal recessive, supported by affected siblings and parental heterozygosity in multiple reports (vedrenne2012mutationinpnpt1 pages 2-3, li2025anovelpolyribonucleotide pages 4-7, matilainen2017defectivemitochondrialrna pages 1-6). | Gene: PNPT1 (HGNC suggestion only); inheritance: HP:0000007 (Autosomal recessive inheritance) |
| Reported pathogenic variants | Published disease-associated PNPT1 variants include p.Gln387Arg, p.Arg136His, p.Pro140Leu, and p.Lys345Glu/K345E; variant classes are mainly missense and appear rare/ultra-rare in population databases when reported (vedrenne2012mutationinpnpt1 pages 2-3, matilainen2017defectivemitochondrialrna pages 21-26, li2025anovelpolyribonucleotide pages 4-7). | Sequence ontology suggestions only: missense_variant; ClinVar/gnomAD accession suggestion only |
| Hallmark neurologic phenotype | Hallmark manifestations include infantile/neonatal encephalopathy, hypotonia, dystonia, choreoathetosis/chorea, developmental delay/regression, seizures or infantile spasms, and abnormal movements; severity ranges from nonprogressive encephalopathy to fatal Leigh-like neurodegeneration (vedrenne2012mutationinpnpt1 pages 2-3, matilainen2017defectivemitochondrialrna pages 21-26, matilainen2017defectivemitochondrialrna pages 1-6). | HPO suggestions: HP:0001252 hypotonia; HP:0001332 dystonia; HP:0001263 developmental delay; HP:0001250 seizures; HP:0012469 infantile spasms; HP:0001288 chorea |
| Hearing / vision / growth | Hearing impairment, visual impairment/optic atrophy, poor growth or growth retardation, and feeding difficulty are recurrent extra-neurologic features in syndromic PNPT1 disease; hearing loss is not universal in the most severe Leigh-like presentations (li2025anovelpolyribonucleotide pages 1-2, matilainen2017defectivemitochondrialrna pages 21-26, matilainen2017defectivemitochondrialrna pages 10-16). | HPO suggestions: HP:0000365 hearing impairment; HP:0000648 optic atrophy; HP:0000505 visual impairment; HP:0001510 growth delay; HP:0011968 feeding difficulties |
| Laboratory abnormalities | Elevated plasma lactate and sometimes CSF lactate are recurring biochemical clues to mitochondrial dysfunction; respiratory-chain enzyme deficiencies are tissue-specific and may involve complexes I, III, IV, and V with relative sparing of complex II (vedrenne2012mutationinpnpt1 pages 2-3, matilainen2017defectivemitochondrialrna pages 21-26). | HPO suggestions: HP:0002151 increased serum lactate; HP:0002490 increased CSF lactate (suggestion); laboratory ontology suggestion only for OXPHOS enzyme deficiency |
| Neuroimaging / pathology | Brain MRI often shows bilateral basal ganglia signal abnormalities (putamen, caudate, globus pallidus), and some patients show white-matter abnormalities/atrophy. Neuropathology in severe disease has shown striatal/nigral degeneration, cerebellar atrophy, and Purkinje cell loss (vedrenne2012mutationinpnpt1 pages 2-3, matilainen2017defectivemitochondrialrna pages 26-34). | HPO suggestions: HP:0002134 basal ganglia MRI signal abnormality; HP:0002500 abnormal cerebral white matter morphology; UBERON suggestions: basal ganglion, putamen, caudate nucleus, cerebellum |
| Core mechanism | PNPT1/PNPase dysfunction impairs mitochondrial RNA import/processing and degradation, causing accumulation of unprocessed mtRNA intermediates, altered ND6/COX transcript handling, defective respiratory-chain assembly, and impaired oxidative phosphorylation; wild-type PNPT1 rescues complex I/IV defects in patient myoblasts (matilainen2017defectivemitochondrialrna pages 6-10, matilainen2017defectivemitochondrialrna pages 21-26). | GO suggestions: mitochondrial RNA processing; RNA import into mitochondrion; mitochondrial gene expression; oxidative phosphorylation; respiratory electron transport chain |
| Expanded immune mechanism | A broader PNPT1 mechanism, not yet proven in every classic COXPD13 case, is accumulation/leakage of mitochondrial double-stranded RNA with activation of antiviral innate immune signaling (mt-dsRNA–PKR–eIF2α or MDA5/MAVS/type I IFN pathways) (li2025anovelpolyribonucleotide pages 10-11). | GO suggestions: response to double-stranded RNA; type I interferon signaling pathway; innate immune response |
| Anatomy / cell types | Highest clinical vulnerability appears in high-energy tissues: central nervous system, cochlea/inner ear, skeletal muscle, and sometimes liver. Mouse and human data implicate neurons, myocytes/myoblasts, cochlear sensory hair cells, and auditory ganglion neurons (vedrenne2012mutationinpnpt1 pages 2-3, matilainen2017defectivemitochondrialrna pages 21-26, ameln2012amutationin pages 1-2, shimada2018pnpaseknockoutresults pages 8-10). | UBERON suggestions: brain, cerebellum, liver, skeletal muscle, cochlea/inner ear; CL suggestions: neuron, skeletal muscle cell, myoblast, sensory hair cell, spiral ganglion neuron |
| Subcellular localization | PNPase is a mitochondrial protein localized to the intermembrane space and also implicated in matrix RNA-processing functions in disease studies (vedrenne2012mutationinpnpt1 pages 2-3, matilainen2017defectivemitochondrialrna pages 10-16). | GO cellular component suggestions: mitochondrion; mitochondrial intermembrane space; mitochondrial matrix |
| Onset / course | Typical onset is neonatal or infancy; course may be fixed/nonprogressive in some cases or progressive and fatal in severe Leigh-like disease. Early feeding problems, irritability, hypotonia, and movement disorder are common presenting patterns (vedrenne2012mutationinpnpt1 pages 2-3, matilainen2017defectivemitochondrialrna pages 1-6). | HPO suggestions: HP:0003577 congenital onset or infantile onset term suggestion only; HP:0003676 congenital progressive? exact term confirmation needed |
| Diagnostics | Diagnostic workup is centered on genomic testing (WES or mitochondrial/neurometabolic panels with parental segregation), serum/CSF lactate, neuroimaging, and respiratory-chain biochemistry in affected tissue/cells. Functional confirmation has included transcript studies and complementation with wild-type PNPT1 (li2025anovelpolyribonucleotide pages 4-7, matilainen2017defectivemitochondrialrna pages 1-6, matilainen2017defectivemitochondrialrna pages 21-26). | NCIT suggestions: Whole Exome Sequencing; Sanger Sequencing; Magnetic Resonance Imaging; HPO suggestion: abnormal mitochondrial metabolism |
| Differential diagnosis | Differential diagnosis includes other nuclear or mtDNA primary mitochondrial diseases causing Leigh syndrome, infantile encephalopathy, hearing loss, or combined OXPHOS defects; isolated PNPT1-related deafness should be considered separately when syndromic features are absent (ameln2012amutationin pages 1-2, matilainen2017defectivemitochondrialrna pages 10-16). | MONDO/HPO suggestions only; exact differential mappings not enumerated here |
| Management | No disease-specific approved therapy was identified in the retrieved evidence. Current real-world management is supportive and multidisciplinary: seizure management, feeding/nutrition support, developmental therapies, hearing/vision support, and mitochondrial disease surveillance; genetic counseling is important (li2025anovelpolyribonucleotide pages 10-11). | NCIT suggestions: Supportive Care; Physical Therapy; Occupational Therapy; Speech Therapy; Anticonvulsant Therapy; Genetic Counseling |
| Epidemiology | Extremely rare; a 2025 literature review stated approximately 15 cases had been reported globally by that time. No reliable prevalence or incidence estimates were identified (li2025anovelpolyribonucleotide pages 1-2, li2025anovelpolyribonucleotide pages 7-10). | Epidemiology ontology suggestion only; no exact prevalence code available |
| Prognosis | Prognosis is variable but often poor in early severe presentations; reported outcomes range from static severe disability to early childhood death in Leigh-like disease. Mortality appears driven by multisystem mitochondrial failure rather than a single organ complication (vedrenne2012mutationinpnpt1 pages 2-3, matilainen2017defectivemitochondrialrna pages 1-6, li2025anovelpolyribonucleotide pages 10-11). | HPO suggestions: HP:0003819 motor regression; HP:0001268 mental deterioration; prognosis ontology suggestion only |
| Model evidence | Complete Pnpt1 loss is embryonic lethal in mice; MEF knockout causes mtDNA loss and impaired growth, and hair-cell knockout causes progressive hearing loss. Drosophila mitochondrial RNA turnover models support dsRNA accumulation and immune-response changes. These models are informative but often more severe than human hypomorphic COXPD13 (shimada2018pnpaseknockoutresults pages 1-2, shimada2018pnpaseknockoutresults pages 8-10, shimada2018pnpaseknockoutresults pages 10-12). | NCBI Taxon suggestions: Mus musculus, Drosophila melanogaster; GO suggestions: mtDNA maintenance, mitochondrial RNA catabolic process, auditory receptor cell development |
| Evidence limitations | Evidence base remains dominated by single families/case reports and mechanistic cell studies; no robust natural-history cohorts, treatment trials, penetrance estimates, or validated disease-specific biomarkers were identified in the retrieved sources (li2025anovelpolyribonucleotide pages 1-2, li2025anovelpolyribonucleotide pages 10-11). | Evidence ontology suggestion only |


*Table: This table summarizes the most evidence-supported knowledge-base facts for combined oxidative phosphorylation defect type 13, emphasizing disease identity, PNPT1 causality, hallmark phenotypes, mechanism, diagnostics, management, epidemiology, and model systems. Ontology mappings are intentionally labeled as suggestions when exact identifiers were not confirmed from the retrieved sources.*

## 1. Disease information

**Definition.** COXPD13 is a nuclear-encoded mitochondrial RNA-metabolism disorder in which deficient PNPase function produces tissue-variable respiratory-chain deficiency. Severe disease predominantly affects the developing nervous system and may satisfy clinicoradiologic criteria for Leigh syndrome. It belongs to the broader **PNPT1-related disease spectrum**, which also includes autosomal-recessive isolated hearing loss and other neurologic or interferonopathy-like presentations. These entities should not automatically be collapsed into COXPD13 because their severity and biochemical evidence differ. (matilainen2017defectivemitochondrialrna pages 6-10, ameln2012amutationin pages 1-2, matilainen2017defectivemitochondrialrna pages 10-16)

**Identifiers and names**

- **MONDO:** MONDO:0013977, “combined oxidative phosphorylation defect type 13.” Open Targets links this entity specifically to PNPT1 (ENSG00000138035). (OpenTargets Search: combined oxidative phosphorylation deficiency 13-PNPT1)
- **OMIM phenotype:** **614932**.
- **Preferred synonyms:** combined oxidative phosphorylation deficiency 13; combined oxidative phosphorylation defect type 13; COXPD13; PNPT1-related combined oxidative phosphorylation deficiency.
- **Gene:** PNPT1, polyribonucleotide nucleotidyltransferase 1. A 2025 report describes a 29-exon gene at chromosome 2p16.1 encoding a 783-amino-acid PNPase protein. (li2025anovelpolyribonucleotide pages 7-10)
- **ICD-10/ICD-11 and MeSH:** no retrieved evidence established a unique disease-specific code. In practice, broader mitochondrial-metabolism/mitochondrial-disease categories are likely used; these should not be represented as exact COXPD13 equivalences without terminology validation.
- **Do not confuse with:** PNPT1-related autosomal-recessive nonsyndromic hearing loss, historically described as DFNB70/DFNB74 and assigned a separate OMIM phenotype; or dominant PNPT1-associated ataxia reported in the broader literature. (li2025anovelpolyribonucleotide pages 7-10, ameln2012amutationin pages 1-2)

**Evidence provenance.** Disease-level identifiers are aggregated resources, whereas most clinical knowledge comes from individual patients or sibling pairs, not EHR-scale cohorts or registries. The evidence is consequently vulnerable to ascertainment and publication bias.

## 2. Etiology, risks, protection, and environment

### Causal factor

The necessary initiating lesion is generally a **biallelic germline PNPT1 variant** that reduces PNPase function. Segregation in the original sibling family and later cases showed unaffected heterozygous parents, supporting autosomal-recessive inheritance. Wild-type PNPT1 complementation restored respiratory-chain complexes I and IV in patient myoblasts, supplying strong functional evidence that PNPT1 deficiency—not merely correlation—is causal. (vedrenne2012mutationinpnpt1 pages 2-3, matilainen2017defectivemitochondrialrna pages 21-26)

### Reported variants with direct COXPD13/Leigh evidence

- **p.Gln387Arg:** homozygous in two siblings with severe, relatively fixed encephalopathy; absent from 100 controls in the original study. The parents were heterozygous. Publication: November 2012, *American Journal of Human Genetics*, DOI [10.1016/j.ajhg.2012.09.001](https://doi.org/10.1016/j.ajhg.2012.09.001), PMID **23084291**. (vedrenne2012mutationinpnpt1 pages 2-3)
- **p.Arg136His and p.Pro140Leu:** compound heterozygous variants in the first RNase-PH core/catalytic region in a child with fatal Leigh syndrome. Publication: September 2017, *Human Molecular Genetics*, DOI [10.1093/hmg/ddx221](https://doi.org/10.1093/hmg/ddx221). Patient-cell RNA and complementation experiments support pathogenicity. (matilainen2017defectivemitochondrialrna pages 6-10, matilainen2017defectivemitochondrialrna pages 21-26)
- **c.1033A>G, p.(Lys345Glu)/p.K345E:** reported homozygously in a Chinese infant, with both parents heterozygous. It was below 1 per 1,000,000 in surveyed population databases, but evidence presented was chiefly segregation, phenotype, rarity, and computational structural modeling; its clinical classification should therefore be checked in current ClinVar and independently functionally validated before being treated as definitively pathogenic. Publication: February 2025, DOI [10.21037/tp-24-419](https://doi.org/10.21037/tp-24-419). (li2025anovelpolyribonucleotide pages 4-7)

The p.Glu475Gly allele is important for genotype–phenotype interpretation but was originally associated with severe early-childhood **isolated hearing loss**, not classic COXPD13. It impaired trimerization/RNA import yet retained enough function to avoid the multisystem phenotype in that family. (ameln2012amutationin pages 1-2)

All established disease alleles are germline. No somatic PNPT1 cause, recurrent chromosomal rearrangement, repeat expansion, or pathogenic mtDNA variant defines COXPD13. Large mtDNA deletions/duplications were absent in the 2025 case. (li2025anovelpolyribonucleotide pages 4-7)

### Risk, protective, modifier, and environmental factors

- **Genetic risk:** two pathogenic PNPT1 alleles; parental relatedness increases the probability of homozygosity for a rare familial allele but is not itself causal.
- **Genotype–phenotype signal:** variants affecting the first RNase-PH core near the catalytic site were associated with particularly severe disease in the 2017 analysis. This is a preliminary structure–phenotype observation, not a validated prognostic rule. (matilainen2017defectivemitochondrialrna pages 10-16)
- **Modifiers/penetrance:** no validated modifier genes, protective alleles, formal penetrance estimates, or carrier-frequency estimates were identified.
- **Environment/lifestyle/infection:** no toxin, diet, smoking, alcohol, radiation, occupation, or infectious agent causes this Mendelian disease. Catabolic stress may plausibly precipitate decompensation in mitochondrial disorders, but COXPD13-specific gene–environment data were not retrieved.
- **Protective factors:** none proven. Avoidance of fasting and rapid treatment of intercurrent illness are reasonable general mitochondrial-care precautions, not demonstrated COXPD13 prevention.
- **Epigenetics:** no disease-specific methylation, histone, or chromatin abnormality is established.

## 3. Phenotypes

Because the denominator is approximately 15 published patients and reporting is inconsistent, percentages would imply false precision. Frequencies below are qualitative.

| Phenotype | Type and typical course | Suggested HPO term |
|---|---|---|
| Global developmental delay/regression | Common; severe; infancy; static in some siblings but progressive in Leigh presentations | HP:0001263; developmental regression term |
| Truncal/generalized hypotonia | Common early sign, neonatal or infantile | HP:0001252 |
| Dystonia | Common movement disorder; may be progressive | HP:0001332 |
| Chorea/choreoathetosis, buccofacial dyskinesia | Recurrent; severe motor disability | HP:0001288; choreoathetosis/dyskinesia terms |
| Seizures/infantile spasms | Variable; daily seizures in the fatal Leigh case; spasms began at nine months in the 2025 case | HP:0001250; HP:0012469 |
| Sensorineural hearing impairment | Recurrent but not universal; absent in the most severe reported Leigh case | HP:0000407 or HP:0000365 |
| Visual impairment, nystagmus, optic atrophy | Variable; bilateral optic atrophy documented in the 2025 case | HP:0000505; HP:0000639; HP:0000648 |
| Feeding difficulty/dysphagia | Early and clinically important; contributes to growth and aspiration risk | HP:0011968; HP:0002015 |
| Growth retardation/failure to thrive | Variable; 2025 patient had weight and height more than 3 SD below normal | HP:0001510; HP:0001508 |
| Elevated blood lactate | Recurrent biochemical clue, usually mild to moderate; CSF may be elevated or normal | HP:0002151 |
| Basal-ganglia MRI lesions | Recurrent, often bilateral; putamen, caudate, globus pallidus, and substantia-nigra involvement reported | HP:0002134 |
| White-matter abnormality/atrophy | Present in some patients, absent in the original siblings | HP:0002500 or specific leukodystrophy term after imaging review |

The original two siblings developed severe encephalopathy between 6 and 9 months, with truncal hypotonia, dystonia, choreoathetosis, mild plasma/CSF lactate elevation, and bilateral putamen/caudate MRI hyperintensity, but their condition was described as fixed and nonprogressive. (vedrenne2012mutationinpnpt1 pages 2-3)

By contrast, the 2017 patient presented at one month with irritability, hypotonia, feeding difficulty, and dystonic movements; she later developed infantile spasms, nystagmus, daily seizures, and progressive neurodegeneration and died at 2.4 years. MRI showed bilateral globus-pallidus disease, and postmortem examination showed severe putaminal and substantia-nigra neuronal loss, cerebellar atrophy, complete Purkinje-cell loss, and microglial proliferation. (matilainen2017defectivemitochondrialrna pages 1-6, matilainen2017defectivemitochondrialrna pages 26-34)

The 2025 child had abnormal limb movement by two weeks, severe developmental impairment, progressive weakness, epilepsy/infantile spasms, white-matter abnormalities, optic atrophy, hearing impairment, growth failure, and elevated plasma lactate. Developmental motor and cognitive scores were reportedly below the 0.1 percentile. (li2025anovelpolyribonucleotide pages 1-2)

**Quality of life.** No EQ-5D, SF-36, PROMIS, or disease-specific patient-reported outcome study exists in the retrieved evidence. Nevertheless, severe motor dependence, inability to communicate normally, seizures, feeding impairment, hearing/vision loss, and repeated specialist care imply profound effects on daily function and caregiver burden.

## 4. Genetic and molecular information

PNPase is a homotrimeric mitochondrial RNA-binding enzyme with 3′→5′ phosphorolytic/exoribonuclease and polymerase-associated functions. It has been localized prominently to the mitochondrial intermembrane space, while disease experiments also implicate matrix RNA-processing functions. PNPT1 dysfunction affects RNA import, processing, degradation, and mitochondrial-genome maintenance to differing degrees across experimental systems. (vedrenne2012mutationinpnpt1 pages 2-3, li2025anovelpolyribonucleotide pages 7-10, matilainen2017defectivemitochondrialrna pages 10-16)

The strongest variant evidence combines rarity and recessive segregation with:

1. localization to conserved catalytic/RNase-PH regions;
2. abnormal PNPase trimerization or predicted structural stability;
3. accumulation of unprocessed mitochondrial transcripts;
4. respiratory-chain deficiency; and
5. rescue after expression of wild-type PNPT1. (matilainen2017defectivemitochondrialrna pages 6-10, matilainen2017defectivemitochondrialrna pages 21-26)

No recurrent aneuploidy, translocation, inversion, pathogenic copy-number syndrome, somatic mosaicism, epigenetic signature, or established modifier gene has been demonstrated. Complete loss is probably incompatible with postimplantation survival, as constitutive mouse knockout is embryonic lethal; living patients therefore likely carry hypomorphic combinations that preserve residual function. (shimada2018pnpaseknockoutresults pages 1-2, shimada2018pnpaseknockoutresults pages 10-12)

## 5. Environmental information

COXPD13 is not an environmental, infectious, or lifestyle disease. No specific chemical exposure, pathogen, diet, or behavior has been shown to initiate or protect against it. Environmental management is consequently directed toward avoiding secondary metabolic stress—prolonged fasting, dehydration, fever, and poorly controlled infection—rather than removing a causal exposure. Evidence for these precautions is extrapolated from general mitochondrial medicine rather than COXPD13 trials.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic hypomorphic PNPT1 variants lead to** reduced abundance, trimerization, RNA binding, or catalytic activity of mitochondrial PNPase.
2. **Defective PNPase leads to** impaired mitochondrial RNA processing/turnover and, for some alleles and assays, reduced import of selected nuclear RNAs into mitochondria. (vedrenne2012mutationinpnpt1 pages 2-3, ameln2012amutationin pages 1-2)
3. **Defective RNA handling results in** accumulation of unprocessed polycistronic transcripts and degradation intermediates, including ND6–ND5, cytochrome-b–ND6, COXI–COXII, and COXIII–ATP6 species, with disturbed ND6, COXI, and COXIII transcript availability. (matilainen2017defectivemitochondrialrna pages 6-10, matilainen2017defectivemitochondrialrna pages 21-26)
4. **Abnormal mitochondrial transcripts lead to** impaired synthesis and assembly of mtDNA-encoded respiratory-chain components; complexes I, III, IV, and V may fall in a tissue-specific pattern, while nuclear-encoded complex II is relatively spared. (matilainen2017defectivemitochondrialrna pages 21-26)
5. **Combined respiratory-chain deficiency results in** impaired proton pumping, oxidative phosphorylation, and ATP production, with increased reliance on glycolysis and lactate accumulation.
6. **Energy failure and associated mitochondrial stress lead to** selective dysfunction and loss of high-demand neurons, cochlear hair cells, muscle cells, and other vulnerable cells.
7. **Neuronal injury leads to** bilateral basal-ganglia lesions, dystonia/choreoathetosis, hypotonia, developmental regression, seizures, visual dysfunction, and, in severe cases, Leigh syndrome and early death. Cochlear-cell injury leads to hearing loss.
8. **Mechanistic branch—partly demonstrated in broader PNPT1 deficiency but not every classic COXPD13 patient:** failed mtRNA degradation **leads to** mitochondrial double-stranded RNA accumulation and cytosolic escape, which **activates** dsRNA sensors and antiviral signaling, potentially including PKR–eIF2α translational arrest and MDA5/MAVS/type-I-interferon responses. This branch may explain interferonopathy-like PNPT1 presentations but should not yet be treated as obligatory in COXPD13. (li2025anovelpolyribonucleotide pages 10-11)

### Human mechanistic evidence

The 2017 study showed accumulation of unprocessed mitochondrial RNA in patient myoblasts and tissue-specific loss of respiratory-chain complexes. Wild-type PNPT1 restored complexes I and IV, providing a direct rescue experiment. mtDNA abundance remained normal in this patient, indicating that defective post-transcriptional RNA metabolism—not obligatory mtDNA depletion—was the proximal defect. (matilainen2017defectivemitochondrialrna pages 21-26, matilainen2017defectivemitochondrialrna pages 26-34)

A representative exact statement available from the 2018 model-study abstract is: **“PNPase knockout results in mtDNA loss and an altered metabolic gene expression program.”** This complete-knockout phenotype is informative but more severe than human hypomorphic disease. (shimada2018pnpaseknockoutresults pages 1-2)

### Cells, pathways, and ontology suggestions

- **Processes/GO suggestions:** mitochondrial RNA processing; mitochondrial RNA catabolic process; RNA import into mitochondrion; mitochondrial gene expression; respiratory-chain complex assembly; oxidative phosphorylation; ATP metabolic process; response to double-stranded RNA; type-I-interferon signaling; neuron death.
- **Cell types/CL suggestions:** neuron; Purkinje cell; microglial cell; skeletal-muscle cell/myoblast; cochlear sensory hair cell; spiral-ganglion neuron; hepatocyte. Exact CL identifiers should be ontology-validated.
- **Cellular components:** mitochondrion (GO:0005739); suggested mitochondrial matrix and mitochondrial intermembrane-space terms.
- **Metabolites/CHEBI suggestions:** L-lactate, pyruvate, ATP, NADH, oxygen; exact CHEBI accessions should be checked at ingestion.
- **Immune involvement:** secondary innate immune activation is biologically credible; primary autoimmunity or immunodeficiency is not established.

No disease-specific single-cell atlas, spatial transcriptomic study, patient multi-omics cohort, lipidomic signature, CRISPR therapeutic screen, or validated circulating molecular profile was identified.

## 7. Anatomical structures affected

**Primary:** central nervous system—especially basal ganglia, substantia nigra, cerebellum, and cerebral white matter—and auditory apparatus. **Additional:** skeletal muscle, optic pathways/retina, liver, and feeding/swallowing systems. The respiratory-chain defect is markedly tissue dependent: the fatal Leigh case had deficiencies of I/III/IV in cortex, I/IV in cerebellum and basal ganglia, isolated IV deficiency in liver, and only mild IV reduction in muscle. (matilainen2017defectivemitochondrialrna pages 6-10)

Suggested UBERON mappings include brain, cerebral cortex, basal ganglion, putamen, caudate nucleus, globus pallidus, substantia nigra, cerebellum, skeletal muscle, liver, optic nerve, cochlea, and inner ear. Lesions are generally bilateral where specified; unilateral disease is not characteristic. Neuropathology supports neuronal loss, Purkinje-cell depletion, and reactive microglial involvement. (matilainen2017defectivemitochondrialrna pages 26-34)

## 8. Temporal development

Onset is usually neonatal or infantile—from two weeks to approximately nine months in the best-characterized cases. Initial signs include reduced spontaneous movement, irritability, hypotonia, feeding difficulty, dystonia, or developmental delay. Course is heterogeneous:

- **Static/nonprogressive severe encephalopathy:** described in the original siblings.
- **Progressive Leigh phenotype:** rapid neurologic deterioration, seizures, basal-ganglia injury, and death at 2.4 years in the 2017 case.
- **Progressive multisystem disease:** motor regression, weakness, epilepsy, sensory impairment, and marked growth failure in the 2025 case. (vedrenne2012mutationinpnpt1 pages 2-3, matilainen2017defectivemitochondrialrna pages 1-6, li2025anovelpolyribonucleotide pages 1-2)

No validated clinical stages, remission pattern, median survival, or intervention window exists. Infancy is the critical vulnerability period and the best opportunity for molecular diagnosis, metabolic stabilization, hearing/vision assessment, seizure treatment, and family counseling.

## 9. Inheritance and population

Inheritance is **autosomal recessive**. For two known carrier parents, each pregnancy has the standard Mendelian expectation of 25% affected, 50% carrier, and 25% unaffected/noncarrier, assuming both parental variants are pathogenic and phase is confirmed.

Penetrance among individuals with two pathogenic alleles appears high, but cannot be quantified. Expressivity is clearly variable—from isolated deafness with particular hypomorphic alleles to severe encephalopathy—although isolated PNPT1 deafness is ordinarily curated as a distinct phenotype. Anticipation is not expected; founder effects, germline mosaicism, sex bias, and carrier frequency have not been established. Both sexes can be affected. Cases span Moroccan, Vietnamese, European-associated, Mexican, and Chinese reports, but these observations do not demonstrate population enrichment. (matilainen2017defectivemitochondrialrna pages 1-6, ameln2012amutationin pages 1-2, li2025anovelpolyribonucleotide pages 7-10)

The 2025 review reported approximately **15 cases globally**; no defensible prevalence per 100,000, annual incidence, geographic distribution, or sex ratio is available. (li2025anovelpolyribonucleotide pages 1-2)

## 10. Diagnostics

### Recommended approach

1. **Recognize the phenotype:** infantile encephalopathy or Leigh syndrome with movement disorder, developmental impairment, hearing/visual abnormalities, feeding failure, and/or elevated lactate.
2. **Baseline laboratory evaluation:** blood lactate and pyruvate, blood gas, glucose, liver profile, creatine kinase, amino acids, acylcarnitines, and urine organic acids. Lactate may be only mildly increased and normal CSF lactate does not exclude disease. (matilainen2017defectivemitochondrialrna pages 21-26)
3. **MRI brain:** assess bilateral basal ganglia, brainstem/cerebellum, and white matter; magnetic-resonance spectroscopy may be considered, though COXPD13-specific performance data are unavailable.
4. **Audiology and ophthalmology:** auditory brainstem response/audiometry, fundus and optic-nerve examination, visual evoked potentials as clinically indicated.
5. **Electrophysiology:** EEG for spasms or seizures; EMG/nerve-conduction studies if neuropathy/myopathy is suspected.
6. **Genetic testing:** trio WES/WGS or a comprehensive nuclear mitochondrial-disease/Leigh panel containing PNPT1, with copy-number calling and parental segregation. The 2025 case was detected by WES and confirmed by Sanger sequencing. (li2025anovelpolyribonucleotide pages 4-7)
7. **mtDNA analysis:** sequence and assess deletions/depletion when clinically indicated to exclude alternative mitochondrial diagnoses, although COXPD13 itself is nuclear.
8. **Functional validation for novel/VUS alleles:** patient fibroblast/myoblast respiratory-chain studies, immunoblot/complex assembly, mtRNA Northern blot or RNA sequencing, and ideally wild-type complementation. (matilainen2017defectivemitochondrialrna pages 21-26)

CMA, karyotyping, FISH, and repeat-expansion testing are not first-line PNPT1 assays unless another diagnosis is suspected. RNA sequencing can reveal abnormal transcript processing but remains a specialist functional test rather than a validated standalone diagnostic.

### Differential diagnosis

The principal differential comprises other genetic Leigh/Leigh-like and combined-OXPHOS disorders, including defects of mitochondrial translation/RNA processing and respiratory-chain assembly. Clinical alternatives include cerebral palsy/static encephalopathy, neurotransmitter disorders, leukodystrophies, congenital infection, Aicardi–Goutières/interferonopathy syndromes, epileptic encephalopathies, and isolated genetic deafness. Bilateral basal-ganglia lesions, lactate elevation, multisystem disease, and biallelic PNPT1 variants with functional evidence favor COXPD13.

There are no standardized disease-specific diagnostic criteria, newborn biochemical screen, or population screening program. Cascade testing is appropriate after a familial molecular diagnosis.

## 11. Outcome and prognosis

No 5- or 10-year survival estimate, median life expectancy, mortality rate, validated prognostic model, or quality-of-life scale has been published. Outcomes range from survival with severe static disability to progressive fatal Leigh syndrome. Earlier onset, progressive seizures, extensive basal-ganglia/brainstem disease, and multi-tissue respiratory-chain deficiency are plausible markers of severity, but are not validated prognostic factors. (vedrenne2012mutationinpnpt1 pages 2-3, matilainen2017defectivemitochondrialrna pages 1-6)

Likely long-term morbidity includes inability to walk or communicate independently, epilepsy, dystonia, dysphagia and aspiration risk, malnutrition, hearing/visual disability, and caregiver dependence. Recovery of established neurodegeneration is unlikely; stabilization may occur in milder forms. “Generally unfavorable prognosis” and unexplained deaths were noted in the 2025 review, but the tiny, selectively reported sample precludes rate estimates. (li2025anovelpolyribonucleotide pages 10-11)

## 12. Treatment and current applications

No approved PNPT1-directed, disease-modifying pharmacotherapy, gene therapy, RNA therapy, cell therapy, or surgery exists. The clinical-trial search retrieved no relevant COXPD13/PNPT1 interventional trial. Current implementation is individualized supportive mitochondrial care:

- seizure management by pediatric neurology; avoid drug choices with disproportionate mitochondrial toxicity when reasonable;
- nutrition and swallowing assessment, aspiration precautions, caloric support, and enteral feeding when necessary;
- physical, occupational, speech/communication, and respiratory therapy;
- hearing aids or cochlear-implant evaluation where auditory anatomy/function permit;
- low-vision services and ophthalmologic monitoring;
- treatment of dystonia/spasticity and orthopedic complications;
- cardiac, hepatic, respiratory, endocrine, and renal surveillance guided by symptoms;
- an emergency illness plan to minimize fasting, dehydration, hypoglycemia, and metabolic decompensation.

Suggested NCIT intervention terms include Supportive Care, Genetic Counseling, Physical Therapy, Occupational Therapy, Speech Therapy, Anticonvulsant Therapy, Enteral Nutrition, Hearing Aid, and Cochlear Implantation; exact NCIT codes require terminology lookup.

“Mitococktail” supplements such as coenzyme Q10, riboflavin, thiamine, or L-carnitine are sometimes used empirically in mitochondrial medicine, but no COXPD13 response rate or controlled efficacy evidence was retrieved. The patient-cell rescue by wild-type PNPT1 supplies a conceptual rationale for gene replacement, but constitutive PNPT1 requirement, multisystem delivery, developmental timing, and dosage control are major translational obstacles. (matilainen2017defectivemitochondrialrna pages 6-10)

## 13. Prevention

Primary lifestyle prevention is impossible because disease results from inherited variants. Relevant measures are reproductive and complication prevention:

- molecular confirmation and phase determination in the proband;
- parental carrier testing and cascade testing of at-risk relatives;
- prenatal diagnosis or preimplantation genetic testing for a known familial variant pair;
- early testing of symptomatic siblings and targeted testing of newborn relatives at 25% risk;
- tertiary prevention through vaccination according to routine schedules, prompt infection treatment, adequate nutrition, avoidance of prolonged fasting, seizure control, aspiration prevention, and sensory/rehabilitative support.

No vaccine, prophylactic drug, environmental intervention, or general-population newborn screening assay prevents COXPD13.

## 14. Other species and natural disease

No verified naturally occurring PNPT1-associated veterinary analogue, breed predisposition, zoonotic potential, or cross-species transmission was identified. COXPD13 is genetic and noncommunicable. Orthologous Pnpt1/PNPase function is strongly conserved, permitting experimental modeling in **Mus musculus** (NCBI Taxon 10090), **Drosophila melanogaster** (Taxon 7227), and cell systems. Exact ortholog NCBI Gene identifiers and any OMIA entries should be checked directly before database ingestion.

## 15. Model organisms

### Mouse and cell models

Constitutive **Pnpt1 knockout is embryonic lethal around embryonic day 8**, demonstrating that complete PNPase loss is incompatible with development. Engineered mouse embryonic fibroblasts tolerated knockout only after adaptation to respiratory deficiency; these cells lost mtDNA and respiration and accumulated biomass at only **1.7–2.4% per hour**, versus **3.3% per hour** in controls. Transcriptomics showed highly significant disturbances of cholesterol, lipid, and secondary-alcohol metabolism and enrichment of axonogenesis/axon-guidance programs. Publication: July 2018, *PLoS ONE*, DOI [10.1371/journal.pone.0200925](https://doi.org/10.1371/journal.pone.0200925). (shimada2018pnpaseknockoutresults pages 1-2, shimada2018pnpaseknockoutresults pages 8-10)

Atoh1-Cre conditional deletion in cochlear sensory hair cells produced progressive high-frequency hearing loss: at four weeks, thresholds at 32 kHz exceeded **78 dB**, compared with **39 dB** in controls, accompanied by stereocilia fusion and loss. This recapitulates auditory vulnerability but not the encephalopathy of COXPD13. (shimada2018pnpaseknockoutresults pages 8-10)

**Limitation:** complete knockout causes mtDNA loss and more profound respiratory failure than most human hypomorphic alleles; it is therefore a loss-of-function boundary model, not an exact genotype-specific COXPD13 model. (shimada2018pnpaseknockoutresults pages 10-12)

### Invertebrate and mechanistic models

Drosophila disruption of mitochondrial RNA turnover caused double-stranded RNA accumulation, cytosolic escape, and altered immune responses, supporting conservation of the RNA-surveillance mechanism. These models clarify pathway biology but do not establish that interferon signaling drives every human COXPD13 manifestation.

### Priority future models

Patient-derived iPSCs differentiated into basal-ganglia neurons, Purkinje cells, skeletal myocytes, retinal cells, and cochlear organoids; knock-in mice bearing patient hypomorphic alleles; and isogenic CRISPR-corrected controls would better test tissue selectivity, genotype–phenotype relationships, and therapeutic rescue.

## Recent developments and expert assessment

The most important recent development is expansion of the phenotype rather than a proven therapy. The February 2025 Chinese case added p.K345E and severe multisystem disease, while emphasizing that only about 15 cases had been described. Its structural modeling is hypothesis-generating and requires biochemical confirmation. (li2025anovelpolyribonucleotide pages 1-2, li2025anovelpolyribonucleotide pages 4-7)

Contemporary mechanistic work increasingly places PNPase at the intersection of mitochondrial RNA quality control and innate immunity. That framework can explain why some PNPT1 patients mimic interferonopathies, but classic COXPD13 remains best supported as an RNA-processing/respiratory-chain disorder. The authoritative interpretation is therefore a **spectrum model**: residual allele-specific PNPase activity and tissue demand probably determine whether disease presents as isolated deafness, static encephalopathy, Leigh syndrome, or an immune-activated phenotype. Direct evidence for modifier genes and quantitative residual-activity thresholds is still lacking. (li2025anovelpolyribonucleotide pages 10-11, ameln2012amutationin pages 1-2, matilainen2017defectivemitochondrialrna pages 10-16)

## Key primary references and supported quotations

1. **Vedrenne et al., November 2012.** “Mutation in PNPT1, which encodes a polyribonucleotide nucleotidyltransferase, impairs RNA import into mitochondria and causes respiratory-chain deficiency.” *American Journal of Human Genetics*. PMID 23084291; DOI [10.1016/j.ajhg.2012.09.001](https://doi.org/10.1016/j.ajhg.2012.09.001). This title accurately summarizes the original human clinical and functional finding. (vedrenne2012mutationinpnpt1 pages 2-3)
2. **von Ameln et al., November 2012.** “A mutation in PNPT1, encoding mitochondrial-RNA-import protein PNPase, causes hereditary hearing loss.” *American Journal of Human Genetics*. DOI [10.1016/j.ajhg.2012.09.002](https://doi.org/10.1016/j.ajhg.2012.09.002). This is primary evidence for the allelic isolated-deafness phenotype, not classic COXPD13. (ameln2012amutationin pages 1-2)
3. **Matilainen et al., September 2017.** “Defective mitochondrial RNA processing due to PNPT1 variants causes Leigh syndrome.” *Human Molecular Genetics*. DOI [10.1093/hmg/ddx221](https://doi.org/10.1093/hmg/ddx221). The patient-cell complementation and transcript-processing results provide the strongest mechanistic evidence for severe COXPD13. (matilainen2017defectivemitochondrialrna pages 6-10, matilainen2017defectivemitochondrialrna pages 21-26)
4. **Shimada et al., July 2018.** The abstract reports: “PKO in mouse inner ear hair cells caused progressive hearing loss that parallels human familial hearing loss previously linked to mutations in PNPase.” *PLoS ONE*. DOI [10.1371/journal.pone.0200925](https://doi.org/10.1371/journal.pone.0200925). (shimada2018pnpaseknockoutresults pages 1-2)
5. **Li et al., February 2025.** *A novel polyribonucleotide nucleotidyltransferase 1 (PNPT1) gene variant potentially associated with combined oxidative phosphorylation deficiency 13: case report and literature review.* DOI [10.21037/tp-24-419](https://doi.org/10.21037/tp-24-419). This is the newest disease-focused report retrieved, but its novel allele remains less functionally established than the 2017 alleles. (li2025anovelpolyribonucleotide pages 1-2, li2025anovelpolyribonucleotide pages 4-7)

## Evidence gaps

The principal unmet needs are an international registry and genotype-resolved natural-history cohort; standardized audiologic, neurologic, ophthalmic, and biochemical assessments; ClinGen-level variant curation; residual-enzyme/function assays; disease-specific biomarkers; patient-reported outcomes; and interventional studies. Statements about prevalence, penetrance, survival, treatment response, environmental triggers, pharmacogenomics, epigenetics, or protective factors cannot currently be made quantitatively from the available evidence.

References

1. (li2025anovelpolyribonucleotide pages 1-2): Yan-Yan Li, Yan Gao, Xiong-Xiong Zhong, and Guang-Fu Chen. A novel polyribonucleotide nucleotidyltransferase 1 (pnpt1) gene variant potentially associated with combined oxidative phosphorylation deficiency 13: case report and literature review. Translational Pediatrics, 14(2):338-349, Feb 2025. URL: https://doi.org/10.21037/tp-24-419, doi:10.21037/tp-24-419. This article has 1 citations and is from a peer-reviewed journal.

2. (li2025anovelpolyribonucleotide pages 7-10): Yan-Yan Li, Yan Gao, Xiong-Xiong Zhong, and Guang-Fu Chen. A novel polyribonucleotide nucleotidyltransferase 1 (pnpt1) gene variant potentially associated with combined oxidative phosphorylation deficiency 13: case report and literature review. Translational Pediatrics, 14(2):338-349, Feb 2025. URL: https://doi.org/10.21037/tp-24-419, doi:10.21037/tp-24-419. This article has 1 citations and is from a peer-reviewed journal.

3. (OpenTargets Search: combined oxidative phosphorylation deficiency 13-PNPT1): Open Targets Query (combined oxidative phosphorylation deficiency 13-PNPT1, 2 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

4. (vedrenne2012mutationinpnpt1 pages 2-3): Vanessa Vedrenne, Ali Gowher, Pascale De Lonlay, Patrick Nitschke, Valérie Serre, Nathalie Boddaert, Cecilia Altuzarra, Anne-Marie Mager-Heckel, Florence Chretien, Nina Entelis, Arnold Munnich, Ivan Tarassov, and Agnès Rötig. Mutation in pnpt1, which encodes a polyribonucleotide nucleotidyltransferase, impairs rna import into mitochondria and causes respiratory-chain deficiency. American journal of human genetics, 91 5:912-8, Nov 2012. URL: https://doi.org/10.1016/j.ajhg.2012.09.001, doi:10.1016/j.ajhg.2012.09.001. This article has 131 citations and is from a highest quality peer-reviewed journal.

5. (ameln2012amutationin pages 1-2): Simon von Ameln, Geng Wang, Redouane Boulouiz, Mark A. Rutherford, Geoffrey M. Smith, Yun Li, Hans-Martin Pogoda, Gudrun Nürnberg, Barbara Stiller, Alexander E. Volk, Guntram Borck, Jason S. Hong, Richard J. Goodyear, Omar Abidi, Peter Nürnberg, Kay Hofmann, Guy P. Richardson, Matthias Hammerschmidt, Tobias Moser, Bernd Wollnik, Carla M. Koehler, Michael A. Teitell, Abdelhamid Barakat, and Christian Kubisch. A mutation in pnpt1, encoding mitochondrial-rna-import protein pnpase, causes hereditary hearing loss. American journal of human genetics, 91 5:919-27, Nov 2012. URL: https://doi.org/10.1016/j.ajhg.2012.09.002, doi:10.1016/j.ajhg.2012.09.002. This article has 111 citations and is from a highest quality peer-reviewed journal.

6. (matilainen2017defectivemitochondrialrna pages 10-16): Sanna Matilainen, Christopher J. Carroll, Uwe Richter, Liliya Euro, Max Pohjanpelto, Anders Paetau, Pirjo Isohanni, and Anu Suomalainen. Defective mitochondrial rna processing due to pnpt1 variants causes leigh syndrome. Human Molecular Genetics, 26:3352–3361, Sep 2017. URL: https://doi.org/10.1093/hmg/ddx221, doi:10.1093/hmg/ddx221. This article has 65 citations and is from a domain leading peer-reviewed journal.

7. (li2025anovelpolyribonucleotide pages 4-7): Yan-Yan Li, Yan Gao, Xiong-Xiong Zhong, and Guang-Fu Chen. A novel polyribonucleotide nucleotidyltransferase 1 (pnpt1) gene variant potentially associated with combined oxidative phosphorylation deficiency 13: case report and literature review. Translational Pediatrics, 14(2):338-349, Feb 2025. URL: https://doi.org/10.21037/tp-24-419, doi:10.21037/tp-24-419. This article has 1 citations and is from a peer-reviewed journal.

8. (matilainen2017defectivemitochondrialrna pages 1-6): Sanna Matilainen, Christopher J. Carroll, Uwe Richter, Liliya Euro, Max Pohjanpelto, Anders Paetau, Pirjo Isohanni, and Anu Suomalainen. Defective mitochondrial rna processing due to pnpt1 variants causes leigh syndrome. Human Molecular Genetics, 26:3352–3361, Sep 2017. URL: https://doi.org/10.1093/hmg/ddx221, doi:10.1093/hmg/ddx221. This article has 65 citations and is from a domain leading peer-reviewed journal.

9. (matilainen2017defectivemitochondrialrna pages 21-26): Sanna Matilainen, Christopher J. Carroll, Uwe Richter, Liliya Euro, Max Pohjanpelto, Anders Paetau, Pirjo Isohanni, and Anu Suomalainen. Defective mitochondrial rna processing due to pnpt1 variants causes leigh syndrome. Human Molecular Genetics, 26:3352–3361, Sep 2017. URL: https://doi.org/10.1093/hmg/ddx221, doi:10.1093/hmg/ddx221. This article has 65 citations and is from a domain leading peer-reviewed journal.

10. (matilainen2017defectivemitochondrialrna pages 26-34): Sanna Matilainen, Christopher J. Carroll, Uwe Richter, Liliya Euro, Max Pohjanpelto, Anders Paetau, Pirjo Isohanni, and Anu Suomalainen. Defective mitochondrial rna processing due to pnpt1 variants causes leigh syndrome. Human Molecular Genetics, 26:3352–3361, Sep 2017. URL: https://doi.org/10.1093/hmg/ddx221, doi:10.1093/hmg/ddx221. This article has 65 citations and is from a domain leading peer-reviewed journal.

11. (matilainen2017defectivemitochondrialrna pages 6-10): Sanna Matilainen, Christopher J. Carroll, Uwe Richter, Liliya Euro, Max Pohjanpelto, Anders Paetau, Pirjo Isohanni, and Anu Suomalainen. Defective mitochondrial rna processing due to pnpt1 variants causes leigh syndrome. Human Molecular Genetics, 26:3352–3361, Sep 2017. URL: https://doi.org/10.1093/hmg/ddx221, doi:10.1093/hmg/ddx221. This article has 65 citations and is from a domain leading peer-reviewed journal.

12. (li2025anovelpolyribonucleotide pages 10-11): Yan-Yan Li, Yan Gao, Xiong-Xiong Zhong, and Guang-Fu Chen. A novel polyribonucleotide nucleotidyltransferase 1 (pnpt1) gene variant potentially associated with combined oxidative phosphorylation deficiency 13: case report and literature review. Translational Pediatrics, 14(2):338-349, Feb 2025. URL: https://doi.org/10.21037/tp-24-419, doi:10.21037/tp-24-419. This article has 1 citations and is from a peer-reviewed journal.

13. (shimada2018pnpaseknockoutresults pages 8-10): Eriko Shimada, Fasih M. Ahsan, Mahta Nili, Dian Huang, Sean Atamdede, Tara TeSlaa, Dana Case, Xiang Yu, Brian D. Gregory, Benjamin J. Perrin, Carla M. Koehler, and Michael A. Teitell. Pnpase knockout results in mtdna loss and an altered metabolic gene expression program. PLoS ONE, 13:e0200925, Jul 2018. URL: https://doi.org/10.1371/journal.pone.0200925, doi:10.1371/journal.pone.0200925. This article has 29 citations and is from a peer-reviewed journal.

14. (shimada2018pnpaseknockoutresults pages 1-2): Eriko Shimada, Fasih M. Ahsan, Mahta Nili, Dian Huang, Sean Atamdede, Tara TeSlaa, Dana Case, Xiang Yu, Brian D. Gregory, Benjamin J. Perrin, Carla M. Koehler, and Michael A. Teitell. Pnpase knockout results in mtdna loss and an altered metabolic gene expression program. PLoS ONE, 13:e0200925, Jul 2018. URL: https://doi.org/10.1371/journal.pone.0200925, doi:10.1371/journal.pone.0200925. This article has 29 citations and is from a peer-reviewed journal.

15. (shimada2018pnpaseknockoutresults pages 10-12): Eriko Shimada, Fasih M. Ahsan, Mahta Nili, Dian Huang, Sean Atamdede, Tara TeSlaa, Dana Case, Xiang Yu, Brian D. Gregory, Benjamin J. Perrin, Carla M. Koehler, and Michael A. Teitell. Pnpase knockout results in mtdna loss and an altered metabolic gene expression program. PLoS ONE, 13:e0200925, Jul 2018. URL: https://doi.org/10.1371/journal.pone.0200925, doi:10.1371/journal.pone.0200925. This article has 29 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Combined_Oxidative_Phosphorylation_Defect_Type_13-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 6 |
| On topic | 2 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 27 |
| Resolved | 26 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 6 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001252` (2 mentions) - the report calls it "Common early sign, neonatal or infantile"; HP calls it **Hypotonia**
- `HP:0001332` (2 mentions) - the report calls it "Common movement disorder; may be progressive"; HP calls it **Dystonia**
- `HP:0002151` (2 mentions) - the report calls it "Recurrent biochemical clue, usually mild to moderate; CSF may be elevated or normal"; HP calls it **Increased circulating lactate concentration**
- `HP:0002134` (2 mentions) - the report calls it "Recurrent, often bilateral; putamen, caudate, globus pallidus, and substantia-nigra involvement reported"; HP calls it **Abnormal basal ganglia morphology**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0005739` (1 mention) - the report calls it "Cellular components:** mitochondrion"; GO calls it **mitochondrion**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.