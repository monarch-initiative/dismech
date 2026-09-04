---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-01T10:06:05.432302'
end_time: '2026-09-01T10:14:21.462248'
duration_seconds: 496.03
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Combined Oxidative Phosphorylation Defect Type 7 (COXPD7, MTRFR/C12orf65-related)
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 19
reference_validation:
  total_references: 5
  verified: 5
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 5
  on_topic: 0
  validator_version: 0.2.1
term_validation:
  total_terms: 42
  verified: 41
  not_found: 1
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.024
  labels_checked: 3
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: UBERON:0000955
    reported_labels:
    - Suggested UBERON terms:** brain
    ontology_label: brain
  labels_variant: 2
  unresolved_terms:
  - HP:0002184
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Combined_Oxidative_Phosphorylation_Defect_Type_7-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Combined Oxidative Phosphorylation Defect Type 7 (COXPD7, MTRFR/C12orf65-related)
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Combined Oxidative Phosphorylation Defect Type 7 (COXPD7, MTRFR/C12orf65-related)** covering all of the
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
- **Disease Name:** Combined Oxidative Phosphorylation Defect Type 7 (COXPD7, MTRFR/C12orf65-related)
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Combined Oxidative Phosphorylation Defect Type 7 (COXPD7, MTRFR/C12orf65-related)** covering all of the
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


# Combined Oxidative Phosphorylation Defect 7 (COXPD7): MTRFR/C12orf65-related disease

## Executive summary

Combined oxidative phosphorylation defect 7 is an ultra-rare, autosomal-recessive mitochondrial translation disorder caused by biallelic loss-of-function variants in **MTRFR**, historically named **C12orf65**. It is best regarded as a phenotypic continuum rather than a single uniform syndrome. Severe presentations include Leigh syndrome and progressive encephalomyopathy; attenuated presentations include complicated hereditary spastic paraplegia type 55 (SPG55), Behr-like syndrome, and axonal Charcot–Marie–Tooth type 6-like neuropathy. Across a 27-patient literature synthesis, optic atrophy occurred in 92.3%, peripheral neuropathy in 80%, and spastic paraparesis in 60%; median onset was 4 years and median molecular diagnosis 17 years, although infantile lethal/severe and slowly progressive childhood-onset cases both occur. These estimates are vulnerable to ascertainment bias and should not be treated as population frequencies. (perrone2020leighsyndromein pages 2-3, perrone2020leighsyndromein pages 3-5)

The protein is a mitochondrial matrix, class-I release-factor-family protein involved in mitoribosome rescue and recycling of abortive peptidyl-tRNA. Deficiency impairs synthesis of mitochondrial-DNA-encoded respiratory-chain subunits and assembly of multiple OXPHOS complexes—particularly I, IV, and V—reducing respiration, ATP-generating capacity, and mitochondrial membrane potential. No approved disease-modifying therapy or MTRFR-specific interventional clinical trial was identified; current implementation consists of molecular diagnosis, multidisciplinary supportive care, rehabilitation, respiratory/nutritional surveillance, and reproductive genetic counseling. (antolinezfernandez2024molecularpathwaysin pages 14-15, dennerlein2023cytochromecoxidase pages 4-4, tucci2014novelc12orf65mutations pages 4-5)

The cornerstone evidence is summarized below.

| Evidence/source and date | Evidence type | Cohort/model | Key genetic finding | Major phenotype/mechanistic result | DOI/URL |
|---|---|---|---|---|---|
| Antonicka et al., 2010 | Primary human + patient-cell study | 2 unrelated pedigrees; affected children with fibroblast studies | Homozygous frameshift variants in **C12orf65**: **248delT** and **210delA**; mitochondrial localization of C12orf65 protein shown (antonicka2010mutationsinc12orf65 pages 3-4, antonicka2010mutationsinc12orf65 pages 2-3) | Progressive encephalomyopathy with Leigh syndrome, optic atrophy/vision loss, ophthalmoplegia, bulbar dysfunction, polyneuropathy, respiratory insufficiency; decreased synthesis of all mitochondrially encoded polypeptides consistent with a mitochondrial translation defect (antonicka2010mutationsinc12orf65 pages 3-4, antonicka2010mutationsinc12orf65 pages 2-3) | https://doi.org/10.1016/j.ajhg.2010.06.004 |
| Tucci et al., 2014 | Primary human family study + patient-cell functional study | 1 consanguineous Indian family with 3 affected individuals; lymphoblast and nerve-biopsy analyses | Novel homozygous **C12orf65 c.346delG / p.V116X** truncating variant; no pathogenic variants found in an additional 183 screened patients with complex neuropathy (tucci2014novelc12orf65mutations pages 4-5, tucci2014novelc12orf65mutations pages 3-4) | Childhood-onset slowly progressive axonal neuropathy with bilateral optic atrophy (CMT6 spectrum); nerve biopsy showed loss of large myelinated and unmyelinated fibers; patient cells had decreased complex V activity/assembly, reduced basal oxygen consumption, reduced oligomycin sensitivity, and lower mitochondrial membrane potential (tucci2014novelc12orf65mutations pages 4-5, tucci2014novelc12orf65mutations pages 3-4, tucci2014novelc12orf65mutations pages 5-6, tucci2014novelc12orf65mutations pages 6-7) | https://doi.org/10.1136/jnnp-2013-306387 |
| Perrone et al., 2020 | Primary human case report + literature review | 1 female patient from consanguineous parents; plus review of 27 previously reported patients | Novel homozygous **C12orf65 c.207_220del; p.Pro70Asnfs*28** causing truncation with loss of the GGQ domain (perrone2020leighsyndromein pages 1-2, perrone2020leighsyndromein pages 2-3) | Severe Leigh syndrome with developmental delay/regression, hypotonia, respiratory failure, optic atrophy, elevated serum lactate **19-69 mg/dL** (ref **4.5-14.4**), characteristic bilateral MRI lesions and progressive cerebral atrophy; poor outcome despite mitochondrial vitamin cocktail. Review found optic atrophy **92.3%**, peripheral neuropathy **80%**, spastic paraparesis **60%**, median onset **4 years**, median diagnosis **17 years**; variants affecting GGQ associated with more severe phenotypes (perrone2020leighsyndromein pages 1-2, perrone2020leighsyndromein pages 2-3, perrone2020leighsyndromein pages 3-5) | https://doi.org/10.1590/1678-4685-gmb-2018-0271 |
| Dennerlein et al., 2023 | Review/mechanistic synthesis | Mitochondrial translation and COX1-biogenesis literature | C12ORF65 discussed as a mitochondrial ribosome quality control (**mtRQC**) factor; patient mutations linked to undetectable C12ORF65 and translation defects (dennerlein2023cytochromecoxidase pages 4-4) | mtRQC involving C12ORF65 is induced when COX1 translation termination is interrupted; depletion further decreases COX1 synthesis, supporting a ribosome-rescue role rather than selective COX1 release-factor activity (dennerlein2023cytochromecoxidase pages 4-4) | https://doi.org/10.1002/1873-3468.14671 |
| Antolínez-Fernández et al., 2024 | Review | Published human cases and mitochondrial-translation literature | Summarizes **>25 patients** with **C12ORF65** mutations; classifies C12ORF65 as a mitochondrial class I peptide release factor likely involved in recycling abortive peptidyl-tRNA species (antolinezfernandez2024molecularpathwaysin pages 14-15) | Clinical spectrum commonly includes optic atrophy, peripheral neuropathy, and spastic paraparesis; patient studies show generally decreased mitochondrial protein synthesis and assembly defects in OXPHOS complexes **I, IV, and V** (antolinezfernandez2024molecularpathwaysin pages 14-15) | https://doi.org/10.3389/fcell.2024.1410245 |


*Table: This compact table summarizes the most directly relevant primary and review evidence for MTRFR/C12orf65-related combined oxidative phosphorylation deficiency 7. It highlights the allelic spectrum, functional mechanism, and the limited but important patient-level data supporting current understanding.*

---

## 1. Disease information

### Definition and scope

COXPD7 is a **nuclear-encoded primary mitochondrial disease** in which defective MTRFR-mediated mitochondrial translation quality control causes combined respiratory-chain dysfunction. The historical disease label emphasizes biochemical OXPHOS deficiency, whereas **SPG55**, **CMT6-like neuropathy**, **Behr syndrome**, and **Leigh syndrome** describe overlapping clinical presentations of the same allelic disorder. More than 25 affected individuals had been reported by the 2024 review literature; Perrone et al. compiled 27 previously described patients and added a further severe case. (antolinezfernandez2024molecularpathwaysin pages 14-15, perrone2020leighsyndromein pages 2-3)

### Identifiers and synonyms

| Resource | Suggested entry/identifier | Qualification |
|---|---|---|
| OMIM phenotype | **613559 — Combined oxidative phosphorylation deficiency 7** | Principal biochemical disease identifier reported in the literature. |
| OMIM allelic phenotype | **SPG55 / spastic paraplegia 55** | Use as an allelic neurological presentation; verify the live OMIM identifier/version before database import. |
| Gene | **MTRFR**, previous symbol **C12orf65** | Current symbol should be primary; retain C12orf65 as an exact synonym for literature retrieval. |
| MONDO | Map to “combined oxidative phosphorylation deficiency 7” if a current dedicated record is present | A stable MONDO accession was not established from the retrieved evidence; do not infer one solely from name matching. |
| Orphanet | Likely represented under combined OXPHOS deficiency, Leigh syndrome, or rare HSP groupings | A disease-specific ORPHA number was not established from the retrieved texts. |
| ICD-10 | No specific COXPD7 code; commonly coded under mitochondrial metabolism disorder (e.g., E88.4) plus manifestations | Coding varies by jurisdiction/version. |
| ICD-11 | Use the current mitochondrial disease/mitochondrial metabolism category plus neurological manifestations | No uniquely verified COXPD7 code was found. |
| MeSH | No dedicated COXPD7 heading established; use “Mitochondrial Diseases,” “Leigh Disease,” “Optic Atrophy,” and “Spastic Paraplegia, Hereditary” | Indexing terms rather than disease-specific identifiers. |

**Common names:** combined oxidative phosphorylation deficiency 7; COXPD7; MTRFR-related mitochondrial disease; C12orf65-related mitochondrial disease; C12orf65 deficiency; SPG55; hereditary spastic paraplegia 55; C12orf65-related Behr syndrome; C12orf65-related Leigh syndrome; recessive CMT6-like neuropathy with optic atrophy.

### Evidence granularity

The evidence is principally **aggregated disease-level literature derived from a very small number of published families**, not EHR-scale data. Patient-level reports, patient fibroblasts/lymphoblasts, and family segregation studies underlie most assertions. Frequencies from the 27-case review are literature-case proportions rather than epidemiological estimates. (perrone2020leighsyndromein pages 2-3, perrone2020leighsyndromein pages 3-5)

---

## 2. Etiology

### Causal factors and genetic risk

The established cause is **biallelic germline pathogenic variation in MTRFR/C12orf65**, usually truncating loss-of-function variants. Reported examples include the original homozygous frameshifts **248delT** and **210delA**, **c.346delG (p.Val116Ter; historically p.V116X)**, and **c.207_220del (p.Pro70AsnfsTer28)**. The latter predicts a 96-amino-acid product lacking the conserved GGQ motif and C-terminal coiled-coil region. (perrone2020leighsyndromein pages 2-3, tucci2014novelc12orf65mutations pages 4-5, antonicka2010mutationsinc12orf65 pages 3-4)

Perrone et al. identified 11 pathogenic variants among 27 earlier patients, predominantly nonsense, frameshift, and splice-disrupting alleles. Variants disrupting the conserved GGQ functional region tend to cause severe Leigh/encephalomyopathic disease, whereas truncations farther toward the C terminus that preserve this region can produce slower SPG55/CMT6-like disease. This is a **provisional genotype–phenotype correlation**, not a deterministic rule. (perrone2020leighsyndromein pages 2-3, perrone2020leighsyndromein pages 3-5, tucci2014novelc12orf65mutations pages 5-6)

All established disease-causing variants are **germline**; a somatic disease mechanism has not been reported. Pathogenicity assessment should apply ACMG/AMP criteria—particularly predicted loss of function in a gene with an established loss-of-function mechanism, segregation, rarity, phenotype specificity, and functional evidence—using current ClinVar and population-database records at interpretation time.

### Other risk, protective, and gene–environment factors

* **Consanguinity/family history:** multiple reports involve consanguineous families and homozygous variants; this increases the probability that both parents carry the same rare allele but is not itself a biological cause. (perrone2020leighsyndromein pages 1-2, tucci2014novelc12orf65mutations pages 3-4, antonicka2010mutationsinc12orf65 pages 2-3)
* **Sex and age:** no sex-specific susceptibility is established. Age modifies clinical expression because disease often declares during development, but it is not an etiological risk factor.
* **Modifier genes/protective alleles:** none has been validated.
* **Environmental or infectious causes:** none is established. Intercurrent illness, fasting, or metabolic stress may plausibly precipitate decompensation in mitochondrial disease, but a specific MTRFR gene–environment interaction has not been demonstrated.
* **Protective diet/lifestyle/exposure:** no disease-specific protective factor has been demonstrated.

---

## 3. Phenotypes

The following ontology mappings are suggested; frequency estimates are available only for the principal triad.

| Phenotype | Type and characteristics | Frequency/course | Suggested HPO term |
|---|---|---|---|
| Optic atrophy/visual loss | Clinical sign; usually bilateral, childhood onset; progressive in severe cases | **92.3%** in the 27-case review | HP:0000648 Optic atrophy; HP:0000572 Visual loss |
| Peripheral/axonal neuropathy | Sign and electrophysiological/pathological abnormality; distal weakness, wasting and sensory loss | **80%**; usually progressive | HP:0009830 Peripheral neuropathy; HP:0003477 Axonal loss; HP:0003690 Limb muscle weakness |
| Spastic paraparesis/tetraparesis | Pyramidal motor sign; lower limbs predominate in SPG55; severe cases become nonambulatory or tetraplegic | **60%**; progressive | HP:0001257 Spasticity; HP:0002313 Spastic paraparesis; HP:0001285 Spastic tetraparesis |
| Developmental delay/intellectual impairment | Neurodevelopmental manifestation, especially when the GGQ region is disrupted | Variable; mild/static to profound/regressive | HP:0001263 Global developmental delay; HP:0001249 Intellectual disability; HP:0002376 Developmental regression |
| Leigh encephalopathy | Clinical/imaging syndrome with symmetric deep-gray/brainstem lesions and regression | Severe end of spectrum; infantile/early childhood | HP:0002283 Global brain atrophy; HP:0002184 T2 hyperintense basal-ganglia/deep-gray lesions; use HP:0002352 for leukoencephalopathy where appropriate |
| Hypotonia/ataxia | Neurological signs, often early | Variable, potentially followed by spasticity | HP:0001252 Hypotonia; HP:0001251 Ataxia |
| Ophthalmoplegia, ptosis, nystagmus | Ocular-motor signs | Variable; prominent in original severe cases | HP:0000602 Ophthalmoplegia; HP:0000508 Ptosis; HP:0000639 Nystagmus |
| Bulbar dysfunction | Dysphagia/dysarthria; aspiration and nutritional risk | Severe/progressive cases | HP:0002015 Dysphagia; HP:0001260 Dysarthria; HP:0001283 Bulbar palsy |
| Respiratory insufficiency | Functional/systemic complication from neuromuscular and central disease | Advanced severe disease; ventilation may be required | HP:0002093 Respiratory insufficiency |
| Failure to thrive | Physical manifestation | Particularly infantile/severe presentations | HP:0001508 Failure to thrive |
| Lactic acidemia | Laboratory abnormality reflecting impaired oxidative metabolism | Variable; Perrone case 19–69 mg/dL (reference 4.5–14.4) | HP:0002151 Increased serum lactate |
| Cerebral/white-matter abnormalities | MRI finding; symmetric thalamic, internal-capsule, cerebral-peduncle, brainstem, medullary and periventricular lesions reported | Progressive in severe Leigh disease | HP:0002500 Abnormal cerebral white matter morphology; HP:0002283 Brain atrophy |

The original severe cases included regression, ataxia, ptosis, abducens paresis, optic atrophy, ophthalmoplegia, bulbar dysfunction, generalized muscle atrophy, hypotonia, polyneuropathy, and respiratory failure. One girl developed symptoms around age 1, had Leigh-pattern MRI abnormalities by age 2, and died at age 8. (antonicka2010mutationsinc12orf65 pages 3-4, antonicka2010mutationsinc12orf65 pages 2-3)

In contrast, three members of a consanguineous family with p.Val116Ter developed childhood-onset, slowly progressive distal axonal neuropathy and bilateral optic atrophy; one also had delayed milestones and static cognitive impairment. Nerve biopsy demonstrated marked loss of large myelinated fibers, regenerative clusters, loss of unmyelinated fibers, and increased endoneurial collagen without a primary demyelinating pattern. (tucci2014novelc12orf65mutations pages 3-4)

**Quality of life:** no disease-specific EQ-5D, SF-36, PROMIS, or validated patient-reported-outcome study was found. Nevertheless, visual loss, progressive gait impairment, wheelchair dependence, dysphagia, communication impairment, and ventilatory dependence indicate major effects on mobility, self-care, education, social participation, and caregiver burden. These consequences are clinically evident but not quantitatively measured in the available cohort. (antonicka2010mutationsinc12orf65 pages 3-4, antonicka2010mutationsinc12orf65 pages 2-3)

---

## 4. Genetic and molecular information

### Gene and protein

* **Gene:** MTRFR; legacy symbol C12orf65.
* **Gene product:** mitochondrial translation release factor in rescue, a small nuclear-encoded protein imported into the mitochondrial matrix.
* **Disease mechanism:** recessive loss of function/hypomorphism rather than gain of function or dominant-negative action.
* **Functional region:** class-I release-factor-like domain containing the conserved **GGQ** motif, important for peptidyl-tRNA hydrolysis/ribosome rescue.

The 2010 study showed mitochondrial localization by colocalization of tagged C12orf65 with cytochrome c. Patient cells had normal steady-state mitochondrial mRNA, rRNA and tRNA abundance but reduced synthesis of mitochondrially encoded polypeptides, localizing the defect to translation rather than mtDNA transcript production. (antonicka2010mutationsinc12orf65 pages 3-4)

### Variant classes and interpretation

Known disease alleles are chiefly frameshift, nonsense, and splice variants. Missense or noncanonical splice variants require stronger functional/segregation evidence because simple proximity to the GGQ motif is insufficient. Disease-associated alleles should be checked against the current MANE transcript, ClinVar, LOVD/HGMD where licensed, and gnomAD; exact current allele frequencies were not recoverable from the reviewed full texts. The reported variants are rare and compatible with recessive disease. No recurrent pathogenic copy-number change, aneuploidy, translocation, inversion, repeat expansion, or mtDNA lesion defines COXPD7.

### Modifier and epigenetic evidence

No replicated modifier gene, disease-specific methylation signature, histone alteration, chromatin abnormality, or epigenetic diagnostic biomarker has been reported. Likewise, no COXPD7-specific transcriptomic, lipidomic, or single-cell atlas was identified.

---

## 5. Environmental information

COXPD7 is a Mendelian genetic disorder, not a toxin-, radiation-, pollution-, lifestyle-, or infection-caused disease. Smoking, alcohol, exercise, occupation, diet, and infectious agents have not been shown to alter penetrance. General mitochondrial practice often avoids prolonged fasting and drugs with substantial mitochondrial toxicity, but this is precautionary extrapolation rather than MTRFR-specific evidence. There is no zoonotic or transmissible component.

---

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic loss-of-function MTRFR variants lead to** absent, truncated, or functionally deficient MTRFR in the mitochondrial matrix. (perrone2020leighsyndromein pages 2-3, antonicka2010mutationsinc12orf65 pages 3-4)
2. **MTRFR deficiency leads to** defective rescue of stalled mitochondrial ribosomes and impaired hydrolysis/recycling of abortive peptidyl-tRNA species. This ribosome-quality-control role is strongly supported mechanistically, although the precise substrate spectrum in every human tissue remains incompletely resolved. (antolinezfernandez2024molecularpathwaysin pages 14-15, dennerlein2023cytochromecoxidase pages 4-4)
3. **Defective mitoribosome rescue leads to** reduced synthesis of mtDNA-encoded polypeptides, despite broadly preserved mitochondrial RNA abundance. (antonicka2010mutationsinc12orf65 pages 3-4, antonicka2010mutationsinc12orf65 pages 2-3)
4. **Reduced mitochondrial translation results in** defective assembly/stability of respiratory-chain complexes containing mtDNA-encoded subunits, prominently complexes I, IV, and V. (antolinezfernandez2024molecularpathwaysin pages 14-15, tucci2014novelc12orf65mutations pages 4-5)
5. **Respiratory-chain/ATP-synthase deficiency leads to** lower oxygen consumption, impaired oligomycin-sensitive complex-V activity, reduced mitochondrial membrane potential, and deficient ATP production. (tucci2014novelc12orf65mutations pages 4-5)
6. **Energy failure and disturbed mitochondrial homeostasis are inferred to lead to** selective dysfunction and degeneration of high-energy-demand cells—particularly retinal ganglion cells, long corticospinal axons, peripheral axons, brainstem neurons, and skeletal/respiratory muscle.
7. **Cell-type injury results in two overlapping branches:**
   * **central branch:** neurodevelopmental regression, Leigh-pattern deep-gray/brainstem lesions, spasticity, bulbar and respiratory dysfunction;
   * **optic/peripheral-axon branch:** bilateral optic atrophy, axonal neuropathy, distal weakness and wasting. (tucci2014novelc12orf65mutations pages 3-4, antonicka2010mutationsinc12orf65 pages 2-3)
8. **Progressive neuronal and neuromuscular loss leads to** visual disability, loss of ambulation, dysphagia, respiratory insufficiency, and—in severe childhood disease—premature death. (perrone2020leighsyndromein pages 1-2, antonicka2010mutationsinc12orf65 pages 3-4)

### Pathways and processes

This is primarily a **mitochondrial gene-expression/OXPHOS disorder**, not a canonical Wnt, MAPK, PI3K–AKT, or mTOR signaling disease. Relevant annotations include:

* **GO biological process:** mitochondrial translation; translational termination; ribosome rescue; peptidyl-tRNA hydrolysis; mitochondrial respiratory-chain complex assembly; oxidative phosphorylation; ATP synthesis coupled proton transport; cellular respiration; maintenance of mitochondrial membrane potential.
* **GO cellular component:** mitochondrion (GO:0005739), mitochondrial matrix (GO:0005759), mitochondrial ribosome (GO:0005761), respiratory-chain complex I, cytochrome-c oxidase/complex IV, and mitochondrial proton-transporting ATP synthase/complex V.
* **Suggested cell ontology targets:** retinal ganglion cell (CL:0000740), upper motor neuron (CL:0000705), peripheral sensory neuron, motor neuron (CL:0000100), skeletal muscle cell (CL:0000188), and Schwann cell (CL:0002573). Direct cell-type-specific molecular profiling has not yet demonstrated equal involvement of all these populations.

Evidence for oxidative stress, apoptosis, autophagy, ER stress, or inflammation specifically driving human COXPD7 remains limited. A preliminary patient-fibroblast report described altered LC3B-positive puncta/autophagy, but this has not established a clinical target or therapy. General mitochondrial stress studies—including tetracycline-induced mitoribosome quality control—should not be interpreted as evidence that tetracyclines treat MTRFR deficiency.

### Recent mechanistic developments, 2023–2024

Recent mitochondrial-translation work refines MTRFR as part of **mitoribosome-associated quality control**, rather than the principal release factor for ordinary canonical termination. C12ORF65/MTRFR is induced in experimental contexts of impaired COX1 termination, and further depletion reduces COX1 synthesis, supporting a rescue function for aberrantly stalled ribosomes. (dennerlein2023cytochromecoxidase pages 4-4)

A 2024 authoritative review characterized it as a mitochondrial class-I peptide release factor likely recycling abortive peptidyl-tRNA and emphasized generalized translation deficiency with complexes I, IV, and V assembly defects. Its abstract-level summary states that mitochondrial translation disorders “often present with neurodegenerative phenotypes,” matching the high-energy neural-tissue pattern in COXPD7. (antolinezfernandez2024molecularpathwaysin pages 14-15)

---

## 7. Anatomical structures affected

### Organ and system level

* **Primary:** central nervous system, optic nerves/retina, peripheral nerves, and skeletal/respiratory neuromuscular system.
* **Secondary/variable:** bulbar apparatus, respiratory system, and nutritional/gastrointestinal function through dysphagia and failure to thrive.
* **Suggested UBERON terms:** brain (UBERON:0000955), brainstem (UBERON:0002298), thalamus (UBERON:0001897), cerebral white matter, spinal cord (UBERON:0002240), optic nerve (UBERON:0000941), retina (UBERON:0000966), peripheral nerve (UBERON:0001021), and skeletal muscle tissue (UBERON:0001134).

MRI in the Perrone case showed bilateral abnormalities involving periventricular/peritrigonal white matter, internal capsules, thalami, cerebral peduncles, midbrain tegmentum, dorsal pons, and medulla, followed by cerebral atrophy. The distribution was symmetric, as expected for a metabolic encephalopathy; no consistent lateralization is known. (perrone2020leighsyndromein pages 1-2, perrone2020leighsyndromein pages 2-3)

### Subcellular level

The initiating lesion acts in the **mitochondrial matrix at the mitoribosome**, with downstream consequences at the inner mitochondrial membrane OXPHOS complexes. Patient lymphoblasts may retain grossly normal mitochondrial morphology despite marked bioenergetic dysfunction. (tucci2014novelc12orf65mutations pages 4-5, antonicka2010mutationsinc12orf65 pages 3-4)

---

## 8. Temporal development

Onset spans infancy to later childhood. In the literature synthesis, median onset was **4 years**, but severe cases can begin near birth or around the first year. Median diagnosis was **17 years**, implying a median 13-year diagnostic delay in the reviewed historical cases. (perrone2020leighsyndromein pages 2-3, perrone2020leighsyndromein pages 3-5)

Three practical trajectories are recognizable:

1. **Severe infantile/early-childhood Leigh trajectory:** hypotonia, developmental delay followed by regression, lactic acidosis, symmetric MRI lesions, bulbar/respiratory decline, and potentially death in childhood.
2. **Intermediate complicated-HSP/Behr trajectory:** optic atrophy and developmental or cognitive involvement followed by progressive spasticity, neuropathy, and loss of ambulation.
3. **Attenuated CMT6/SPG55 trajectory:** childhood-onset optic atrophy and slowly progressive axonal neuropathy/spastic paraparesis, sometimes with preserved cognition and survival into adulthood. (perrone2020leighsyndromein pages 3-5, tucci2014novelc12orf65mutations pages 3-4, tucci2014novelc12orf65mutations pages 5-6)

No validated staging system, remission pattern, or predictable relapse–remission course exists. Disease is generally chronic and progressive. Intercurrent metabolic stress may be a clinical vulnerability, but no disease-specific critical intervention window has been quantified.

---

## 9. Inheritance and population

Inheritance is **autosomal recessive**. Affected individuals generally carry homozygous variants in consanguineous pedigrees or biallelic variants inherited one from each parent. Parents are expected to be asymptomatic heterozygous carriers. For two carrier parents, each pregnancy has a 25% probability of an affected child, 50% probability of an unaffected carrier, and 25% probability of inheriting neither familial pathogenic allele.

Penetrance for clearly pathogenic biallelic loss-of-function genotypes appears high, but cannot be calculated precisely. Expressivity is markedly variable and correlates imperfectly with whether the GGQ region is disrupted. Anticipation is not expected; germline mosaicism has not been established but cannot be excluded in an apparently de novo recurrence scenario.

No valid COXPD7 prevalence, incidence, carrier-frequency, sex-ratio, founder-effect, or geographic-distribution estimate exists. The 2024 review reported only **more than 25 patients**, demonstrating extreme rarity. In one CMT6 study, no additional pathogenic MTRFR variants were found among 183 screened complex-neuropathy cases. General HSP prevalence figures must not be assigned to SPG55. (antolinezfernandez2024molecularpathwaysin pages 14-15, tucci2014novelc12orf65mutations pages 4-5)

Reported pedigrees include Turkish, Dutch, Indian, Brazilian, Japanese, and other ancestries, indicating worldwide occurrence rather than an established endemic population. Consanguinity enriches homozygous cases but does not imply ancestry-specific restriction.

---

## 10. Diagnostics

### When to suspect the disorder

MTRFR disease should be considered in children or adults with **bilateral optic atrophy plus axonal neuropathy and/or spastic paraparesis**, particularly when accompanied by developmental regression, Leigh-pattern MRI lesions, ophthalmoplegia, bulbar dysfunction, respiratory insufficiency, or biochemical evidence of combined OXPHOS deficiency. Tucci et al. specifically concluded that the optic-atrophy/axonal-neuropathy combination should prompt investigation for mitochondrial disease and C12orf65. (tucci2014novelc12orf65mutations pages 6-7)

### Recommended evaluation

1. **Clinical:** neurological, developmental, ophthalmological, swallowing/nutritional, respiratory, and rehabilitation assessments.
2. **Laboratory:** serum lactate, pyruvate with careful collection, blood gas, glucose, liver enzymes, CK, amino acids, acylcarnitines, and urine organic acids. Normal values do not exclude disease. Elevated lactate supports mitochondrial dysfunction but is nonspecific; one severe case ranged from 19–69 mg/dL. (perrone2020leighsyndromein pages 2-3)
3. **Imaging:** brain MRI with T1/T2/FLAIR and diffusion-weighted imaging to assess symmetric deep-gray, white-matter, brainstem lesions and atrophy.
4. **Electrophysiology:** nerve-conduction studies/EMG to distinguish axonal neuropathy; EEG when seizures or episodic encephalopathy are suspected.
5. **Ophthalmology:** visual acuity, color vision, pupils, fundus examination, optical coherence tomography, and visual evoked potentials as appropriate.
6. **Respiratory/swallowing:** spirometry where feasible, sleep study or nocturnal oximetry/capnography, and videofluoroscopic or endoscopic swallowing assessment when indicated.
7. **Tissue/functional studies:** respiratory-chain enzymology, BN-PAGE, mitochondrial translation assays, oxygen consumption, and membrane-potential studies in fibroblasts or muscle can support uncertain variants. Nerve biopsy is not routinely necessary; the reported pathology was axonal rather than demyelinating. (tucci2014novelc12orf65mutations pages 4-5, tucci2014novelc12orf65mutations pages 3-4)

### Genetic testing strategy

* **Preferred:** trio WES or WGS, or a comprehensive nuclear-plus-mtDNA mitochondrial/optic-neuropathy/HSP panel that includes **MTRFR** under both current and legacy symbols.
* **WGS:** useful when exome/panel testing is negative because it can detect noncoding splice variants, structural variants, and mtDNA changes in parallel.
* **WES:** well suited to coding truncating variants and agnostic phenotypes. Contemporary evidence from inherited-neuropathy cohorts favors exome/genome analysis over narrow panels because mitochondrial disease and CMT overlap clinically.
* **Single-gene sequencing:** appropriate when the phenotype and familial variant are highly specific; include deletion/duplication analysis if sequencing is negative.
* **RNA sequencing:** useful experimentally or diagnostically for suspected splice variants or reduced transcript, preferably in an expressing tissue.
* **CMA/karyotype/FISH:** low yield for isolated suspected COXPD7, although CMA may be appropriate for unexplained developmental disability.
* **mtDNA sequencing:** does not diagnose MTRFR disease but remains important in the broad mitochondrial differential.
* **Repeat-expansion testing:** not indicated unless another phenotype suggests it.

Confirmation requires two pathogenic/likely pathogenic variants in trans, compatible phenotype, and segregation. A single heterozygous allele does not establish recessive disease.

### Differential diagnosis

Key alternatives include OPA1/OPA3-related optic atrophy, MFN2-related CMT6, SPG7, ACO2, FDXR, RTN4IP1, TMEM126A, NDUFS6, mitochondrial DNA LHON variants, POLG/TWNK-related disease, other mitochondrial translation defects, and other complicated HSP/Leigh genes. Distinguishing evidence includes inheritance, MRI distribution, lactate/respiratory-chain findings, and molecular testing.

### Screening

There is no population or newborn biochemical screen. Cascade testing is appropriate after identification of familial variants. Targeted prenatal diagnosis and preimplantation genetic testing for monogenic disease are technically possible. Carrier screening is most informative in relatives or populations/families with a known pathogenic allele.

---

## 11. Outcome and prognosis

No 5- or 10-year survival rate, life-expectancy estimate, mortality rate, validated prognostic score, or prognostic biomarker is available. Prognosis is genotype- and phenotype-dependent.

Poor prognostic features include very early onset, GGQ-domain disruption, developmental regression, classic Leigh MRI lesions, bulbar dysfunction, respiratory failure, severe lactic acidosis, and early nonambulation. More distal truncations preserving the functional release-factor region have been associated with slower SPG55/CMT6-like courses, but individual prediction remains uncertain. (perrone2020leighsyndromein pages 2-3, perrone2020leighsyndromein pages 3-5, tucci2014novelc12orf65mutations pages 5-6)

Documented outcomes range from likely adult survival with slowly progressive neuropathy to ventilation dependence and childhood death. One original patient died at age 8; another required ventilatory support by age 14. A severe Perrone case progressed despite treatment to oxygen dependence, spastic tetraplegia, and profound developmental disability. (perrone2020leighsyndromein pages 1-2, antonicka2010mutationsinc12orf65 pages 3-4)

Major morbidity comprises blindness/low vision, falls and loss of mobility, contractures, neuropathic disability, dysphagia/aspiration, malnutrition, communication impairment, respiratory failure, and caregiver dependence. Recovery of established neurodegeneration is unlikely, although supportive treatment may preserve function and prevent secondary complications.

---

## 12. Treatment

### Current standard

There is **no approved molecularly targeted or curative treatment**. Management should be individualized by a mitochondrial/neurometabolic team:

* physical therapy, stretching, strengthening within tolerance, gait aids, orthoses, seating and contracture prevention;
* occupational therapy and adaptive technology;
* low-vision services and educational accommodations;
* speech/communication therapy and dysphagia management;
* adequate calories, feeding support, aspiration precautions, and gastrostomy when clinically necessary;
* noninvasive or invasive ventilatory support for hypoventilation/respiratory failure;
* spasticity treatment with oral agents, focal botulinum toxin, or intrathecal baclofen when benefits outweigh weakness/sedation risks;
* neuropathic-pain management, seizure treatment if present, and routine vaccination/infection prevention.

Suggested NCIt intervention concepts include **Physical Therapy**, **Occupational Therapy**, **Speech Therapy**, **Assistive Device**, **Noninvasive Ventilation**, **Gastrostomy**, **Baclofen**, and **Botulinum Toxin Therapy**; exact codes should be resolved against the current NCIt release.

### Pharmacotherapy and supplements

Empirical mitochondrial supplements—thiamine, riboflavin, coenzyme Q10, biotin, and L-carnitine—were used in the severe Perrone case without preventing progression to oxygen dependence and spastic tetraplegia. This single uncontrolled observation neither proves ineffectiveness nor supports efficacy. Treatment should correct documented nutritional deficiencies and avoid assuming that a “mitochondrial cocktail” is disease modifying. (perrone2020leighsyndromein pages 1-2)

No MTRFR-specific pharmacogenomic recommendation exists. Valproate caution is particularly important when POLG disease remains in the differential, but this is not an MTRFR-specific interaction.

### Experimental therapies and trials

No disease-specific gene replacement, CRISPR, RNA, cell, immunotherapy, or approved targeted small molecule was identified, and the ClinicalTrials.gov search did not identify a relevant MTRFR/COXPD7 interventional study. Patient-cell rescue experiments and mitoribosome-quality-control research provide target-validation concepts, but not clinical treatments. Tetracycline effects on mitochondrial/ER stress in other experimental systems should not be clinically extrapolated because these drugs also inhibit mitochondrial translation.

---

## 13. Prevention

* **Primary prevention:** the disease cannot be prevented by lifestyle modification, vaccination, or environmental avoidance. Reproductive options after molecular diagnosis include carrier testing, preimplantation genetic testing, chorionic-villus sampling, amniocentesis, donor gametes, or adoption.
* **Secondary prevention:** cascade testing and early molecular diagnosis can reduce diagnostic delay and enable early surveillance, but no newborn screening program exists.
* **Tertiary prevention:** respiratory monitoring, vaccination, aspiration prevention, nutrition management, contracture prevention, mobility aids, and prompt treatment of infection can reduce complications.
* **Genetic counseling:** essential for recurrence-risk explanation, testing of adult relatives, and family planning. Testing minors for the familial biallelic condition is appropriate where early clinical surveillance has potential benefit.

There is no vaccine, antimicrobial prophylaxis, public-health sanitation intervention, or environmental remediation specific to COXPD7.

---

## 14. Other species and natural disease

MTRFR is evolutionarily conserved within the mitochondrial release-factor/ribosome-quality-control system, but no well-characterized naturally occurring veterinary counterpart, breed predisposition, or OMIA-defined animal disease was established from the retrieved literature. Accordingly:

* **Taxonomy:** confirmed natural disease is currently human—*Homo sapiens* (NCBI Taxonomy 9606).
* **Orthologues:** mammalian and other vertebrate orthologues exist and can be retrieved from NCBI Gene/Alliance resources, but exact gene IDs should be version-checked before ingestion.
* **Veterinary relevance:** presently unestablished.
* **Transmission:** Mendelian inheritance within a species; no zoonosis or cross-species transmission.

---

## 15. Model organisms and experimental systems

### Available models

The strongest disease models are **patient-derived fibroblasts and lymphoblastoid cells** carrying defined biallelic truncating variants. They reproduce reduced mitochondrial translation, OXPHOS complex-assembly defects, reduced complex-V activity, lower oxygen consumption, and decreased membrane potential. Mitochondrial morphology may remain grossly normal, emphasizing that morphology alone is an insensitive disease readout. (tucci2014novelc12orf65mutations pages 4-5, antonicka2010mutationsinc12orf65 pages 3-4)

Tagged-protein localization, knockdown/depletion, and mitochondrial translation-termination perturbation systems have been used to establish matrix localization and participation in mitoribosome rescue. In mtRF1-deficient experimental cells, MTRFR/C12ORF65-associated quality control is induced; additional depletion worsens COX1 synthesis. (dennerlein2023cytochromecoxidase pages 4-4)

### Gaps and limitations

No robust, widely adopted Mtrfr knockout/knock-in mouse, zebrafish, Drosophila, C. elegans, organoid, or patient-iPSC neuronal model that comprehensively recapitulates human COXPD7 was identified in the searched evidence. Patient fibroblasts and lymphoblasts are accessible but do not model retinal ganglion cells, corticospinal axons, brain development, or long-term neurodegeneration. Priorities include isogenic CRISPR-corrected iPSCs differentiated into retinal ganglion and motor neurons, variant-specific knock-in animals, tissue-resolved metabolomics/proteomics, and longitudinal natural-history cohorts.

---

## Evidence appraisal and authoritative interpretation

The causal gene–disease relationship is strong: multiple independent recessive pedigrees, segregation, recurrent truncating alleles, mitochondrial localization, patient-cell translation defects, and OXPHOS rescue/quality-control biology converge. Nevertheless, almost all quantitative clinical knowledge derives from fewer than 30 historically published patients. The apparent phenotype frequencies and GGQ-domain correlation are therefore useful for hypothesis generation and variant interpretation, but are not precise penetrance estimates. (antolinezfernandez2024molecularpathwaysin pages 14-15, perrone2020leighsyndromein pages 2-3, perrone2020leighsyndromein pages 3-5)

Representative abstract statements include:

* Antonicka et al. (2010): **“Mutations in C12orf65 in patients with encephalomyopathy and a mitochondrial translation defect.”** This title accurately encapsulates the primary human and cellular evidence. DOI: https://doi.org/10.1016/j.ajhg.2010.06.004; publication July 2010. (antonicka2010mutationsinc12orf65 pages 3-4, antonicka2010mutationsinc12orf65 pages 2-3)
* Tucci et al. (2014): **“This work describes a mutation in the C12orf65 gene that causes recessive form of CMT6 and confirms the role of mitochondrial dysfunction in this complex axonal neuropathy.”** DOI: https://doi.org/10.1136/jnnp-2013-306387; journal issue 2014. (tucci2014novelc12orf65mutations pages 4-5)
* Perrone et al. (2020): **“Our study supports that the phenotype caused by C12orf65 gene variants is heterogeneous and varies from spastic paraparesis to Leigh syndrome.”** DOI: https://doi.org/10.1590/1678-4685-gmb-2018-0271; published May 2020. (perrone2020leighsyndromein pages 1-2, perrone2020leighsyndromein pages 3-5)
* Antolínez-Fernández et al. (2024) summarize that mitochondrial translation disorders are frequently multisystemic and affect high-energy-demand tissues, commonly producing neurodegenerative phenotypes. DOI: https://doi.org/10.3389/fcell.2024.1410245; published May 2024. (antolinezfernandez2024molecularpathwaysin pages 14-15)

## Key knowledge-base cautions

1. Store **MTRFR** as the preferred gene symbol and **C12orf65** as a legacy synonym.
2. Represent COXPD7, SPG55, Behr-like disease, Leigh syndrome, and CMT6-like neuropathy as an **allelic phenotypic spectrum**, not necessarily separate molecular diseases.
3. Mark phenotype frequencies as literature-derived case proportions with substantial ascertainment bias.
4. Do not infer environmental causation, population prevalence, survival rates, or treatment efficacy where none has been measured.
5. Record mitochondrial-ribosome rescue as the upstream demonstrated mechanism; oxidative stress, cell death, and selective neuronal vulnerability are downstream biological inferences unless directly tested in MTRFR models.

References

1. (perrone2020leighsyndromein pages 2-3): Eduardo Perrone, Thiago R. Cavole, Manuella G. Oliveira, Luiza do A. Virmond, Marina de França B. Silva, Maria de Fatima F. Soares, Simone Brasil de O. Iglesias, Ariane Falconi, Juliana S. Silva, Viviane Nakano, Maria Fernanda Milanezi, Carmen Silvia C. Mendes, Marco Antonio Curiati, and Cecília Micheletti. Leigh syndrome in a patient with a novel c12orf65 pathogenic variant: case report and literature review. Genetics and Molecular Biology, May 2020. URL: https://doi.org/10.1590/1678-4685-gmb-2018-0271, doi:10.1590/1678-4685-gmb-2018-0271. This article has 21 citations and is from a peer-reviewed journal.

2. (perrone2020leighsyndromein pages 3-5): Eduardo Perrone, Thiago R. Cavole, Manuella G. Oliveira, Luiza do A. Virmond, Marina de França B. Silva, Maria de Fatima F. Soares, Simone Brasil de O. Iglesias, Ariane Falconi, Juliana S. Silva, Viviane Nakano, Maria Fernanda Milanezi, Carmen Silvia C. Mendes, Marco Antonio Curiati, and Cecília Micheletti. Leigh syndrome in a patient with a novel c12orf65 pathogenic variant: case report and literature review. Genetics and Molecular Biology, May 2020. URL: https://doi.org/10.1590/1678-4685-gmb-2018-0271, doi:10.1590/1678-4685-gmb-2018-0271. This article has 21 citations and is from a peer-reviewed journal.

3. (antolinezfernandez2024molecularpathwaysin pages 14-15): Álvaro Antolínez-Fernández, Paula Esteban-Ramos, Miguel Ángel Fernández-Moreno, and Paula Clemente. Molecular pathways in mitochondrial disorders due to a defective mitochondrial protein synthesis. Frontiers in Cell and Developmental Biology, May 2024. URL: https://doi.org/10.3389/fcell.2024.1410245, doi:10.3389/fcell.2024.1410245. This article has 17 citations.

4. (dennerlein2023cytochromecoxidase pages 4-4): Sven Dennerlein, Peter Rehling, and Ricarda Richter‐Dennerlein. Cytochrome <i>c</i> oxidase biogenesis – from translation to early assembly of the core subunit <scp>cox1</scp>. May 2023. URL: https://doi.org/10.1002/1873-3468.14671, doi:10.1002/1873-3468.14671. This article has 40 citations and is from a peer-reviewed journal.

5. (tucci2014novelc12orf65mutations pages 4-5): A. Tucci, Y.-T. Liu, E. Preza, R. D. S. Pitceathly, A. Chalasani, V. Plagnol, J. M. Land, D. Trabzuni, M. Ryten, Z. Jaunmuktane, M. M. Reilly, S. Brandner, I. Hargreaves, J. Hardy, A. B. Singleton, A. Y. Abramov, and H. Houlden. Novel c12orf65 mutations in patients with axonal neuropathy and optic atrophy. Journal of Neurology, Neurosurgery, and Psychiatry, 85:486-492, Nov 2014. URL: https://doi.org/10.1136/jnnp-2013-306387, doi:10.1136/jnnp-2013-306387. This article has 63 citations.

6. (antonicka2010mutationsinc12orf65 pages 3-4): Hana Antonicka, Elsebet Østergaard, Florin Sasarman, Woranontee Weraarpachai, Flemming Wibrand, Anne Marie B. Pedersen, Richard J. Rodenburg, Marjo S. van der Knaap, Jan A.M. Smeitink, Zofia M. Chrzanowska-Lightowlers, and Eric A. Shoubridge. Mutations in c12orf65 in patients with encephalomyopathy and a mitochondrial translation defect. American journal of human genetics, 87 1:115-22, Jul 2010. URL: https://doi.org/10.1016/j.ajhg.2010.06.004, doi:10.1016/j.ajhg.2010.06.004. This article has 196 citations and is from a highest quality peer-reviewed journal.

7. (antonicka2010mutationsinc12orf65 pages 2-3): Hana Antonicka, Elsebet Østergaard, Florin Sasarman, Woranontee Weraarpachai, Flemming Wibrand, Anne Marie B. Pedersen, Richard J. Rodenburg, Marjo S. van der Knaap, Jan A.M. Smeitink, Zofia M. Chrzanowska-Lightowlers, and Eric A. Shoubridge. Mutations in c12orf65 in patients with encephalomyopathy and a mitochondrial translation defect. American journal of human genetics, 87 1:115-22, Jul 2010. URL: https://doi.org/10.1016/j.ajhg.2010.06.004, doi:10.1016/j.ajhg.2010.06.004. This article has 196 citations and is from a highest quality peer-reviewed journal.

8. (tucci2014novelc12orf65mutations pages 3-4): A. Tucci, Y.-T. Liu, E. Preza, R. D. S. Pitceathly, A. Chalasani, V. Plagnol, J. M. Land, D. Trabzuni, M. Ryten, Z. Jaunmuktane, M. M. Reilly, S. Brandner, I. Hargreaves, J. Hardy, A. B. Singleton, A. Y. Abramov, and H. Houlden. Novel c12orf65 mutations in patients with axonal neuropathy and optic atrophy. Journal of Neurology, Neurosurgery, and Psychiatry, 85:486-492, Nov 2014. URL: https://doi.org/10.1136/jnnp-2013-306387, doi:10.1136/jnnp-2013-306387. This article has 63 citations.

9. (tucci2014novelc12orf65mutations pages 5-6): A. Tucci, Y.-T. Liu, E. Preza, R. D. S. Pitceathly, A. Chalasani, V. Plagnol, J. M. Land, D. Trabzuni, M. Ryten, Z. Jaunmuktane, M. M. Reilly, S. Brandner, I. Hargreaves, J. Hardy, A. B. Singleton, A. Y. Abramov, and H. Houlden. Novel c12orf65 mutations in patients with axonal neuropathy and optic atrophy. Journal of Neurology, Neurosurgery, and Psychiatry, 85:486-492, Nov 2014. URL: https://doi.org/10.1136/jnnp-2013-306387, doi:10.1136/jnnp-2013-306387. This article has 63 citations.

10. (tucci2014novelc12orf65mutations pages 6-7): A. Tucci, Y.-T. Liu, E. Preza, R. D. S. Pitceathly, A. Chalasani, V. Plagnol, J. M. Land, D. Trabzuni, M. Ryten, Z. Jaunmuktane, M. M. Reilly, S. Brandner, I. Hargreaves, J. Hardy, A. B. Singleton, A. Y. Abramov, and H. Houlden. Novel c12orf65 mutations in patients with axonal neuropathy and optic atrophy. Journal of Neurology, Neurosurgery, and Psychiatry, 85:486-492, Nov 2014. URL: https://doi.org/10.1136/jnnp-2013-306387, doi:10.1136/jnnp-2013-306387. This article has 63 citations.

11. (perrone2020leighsyndromein pages 1-2): Eduardo Perrone, Thiago R. Cavole, Manuella G. Oliveira, Luiza do A. Virmond, Marina de França B. Silva, Maria de Fatima F. Soares, Simone Brasil de O. Iglesias, Ariane Falconi, Juliana S. Silva, Viviane Nakano, Maria Fernanda Milanezi, Carmen Silvia C. Mendes, Marco Antonio Curiati, and Cecília Micheletti. Leigh syndrome in a patient with a novel c12orf65 pathogenic variant: case report and literature review. Genetics and Molecular Biology, May 2020. URL: https://doi.org/10.1590/1678-4685-gmb-2018-0271, doi:10.1590/1678-4685-gmb-2018-0271. This article has 21 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Combined_Oxidative_Phosphorylation_Defect_Type_7-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 5 |
| Resolved | 5 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 5 |
| On topic | 0 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 42 |
| Resolved | 41 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 3 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `UBERON:0000955` (1 mention) - the report calls it "Suggested UBERON terms:** brain"; UBERON calls it **brain**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0002184` (1 mention) - HP does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0005739` (1 mention) - the report calls it "GO cellular component:** mitochondrion"; GO calls it **mitochondrion**
- `CL:0000740` (1 mention) - the report calls it "Suggested cell ontology targets:** retinal ganglion cell"; CL calls it **retinal ganglion cell**