---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-03T13:06:55.906141'
end_time: '2026-09-03T13:17:46.096427'
duration_seconds: 650.19
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Autosomal Recessive Nonsyndromic Hearing Loss 35 (DFNB35, ESRRB-related)
  mondo_id: MONDO:0012060
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
  total_references: 3
  verified: 3
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 3
  on_topic: 1
  validator_version: 0.2.1
term_validation:
  total_terms: 6
  verified: 6
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0012060
    reported_labels:
    - if available
    ontology_label: autosomal recessive nonsyndromic hearing loss 35
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Autosomal_Recessive_Nonsyndromic_Hearing_Loss_35-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autosomal Recessive Nonsyndromic Hearing Loss 35 (DFNB35, ESRRB-related)
- **MONDO ID:** MONDO:0012060 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Recessive Nonsyndromic Hearing Loss 35 (DFNB35, ESRRB-related)** covering all of the
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
- **Disease Name:** Autosomal Recessive Nonsyndromic Hearing Loss 35 (DFNB35, ESRRB-related)
- **MONDO ID:** MONDO:0012060 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Recessive Nonsyndromic Hearing Loss 35 (DFNB35, ESRRB-related)** covering all of the
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


# Autosomal Recessive Nonsyndromic Hearing Loss 35 (DFNB35; ESRRB-related)

## Executive summary

DFNB35 is an exceptionally rare Mendelian sensorineural hearing-loss disorder caused by **biallelic germline variants in ESRRB**, which encodes estrogen-related receptor β (ERRβ), an orphan nuclear-receptor transcription factor. The usual presentation is congenital or prelingual, bilateral, approximately symmetric severe-to-profound sensorineural hearing loss (SNHL), although moderate disease and asymmetric progressive loss are now documented. Before the first South Korean case in 2024, fewer than 20 affected families had been reported, with strong ascertainment in consanguineous Pakistani and Turkish pedigrees. Consequently, prevalence, penetrance, carrier frequency, natural history, treatment outcomes, and genotype–phenotype relationships remain poorly quantified. (choi2024functionalpathogenicityof pages 1-2, choi2024functionalpathogenicityof pages 7-8)

The principal 2024 advance was functional characterization of **ESRRB c.397+2T>G** and **c.1144C>T, p.(Arg382Cys)**. The splice variant caused exon-4 skipping, premature termination, and nonsense-mediated decay (NMD). p.Arg382Cys destabilized ERRβ, reduced transcriptional activity, and altered inner-ear-relevant downstream genes. Nevertheless, because p.Arg382Cys is relatively frequent in East Asians, its authors assigned only ACMG/AMP **PS3-supporting** evidence and called it a “warm VUS,” not definitively pathogenic. (choi2024functionalpathogenicityof pages 3-4, choi2024functionalpathogenicityof pages 5-7, choi2024functionalpathogenicityof pages 8-9)

| Domain | Best-supported finding | Evidence type/strength | Key source/date |
|---|---|---|---|
| Disease identity and inheritance | DFNB35 is autosomal-recessive nonsyndromic sensorineural hearing loss caused by biallelic germline **ESRRB** variants; locus **14q24.3**. | **Strong:** linkage, segregation, multiple independent families, and functional evidence. | Collin et al., Jan 2008, [DOI](https://doi.org/10.1016/j.ajhg.2007.09.008) (collin2008mutationsofesrrb pages 1-2, collin2008mutationsofesrrb pages 5-6); Choi et al., Sep 2024, [DOI](https://doi.org/10.1038/s41598-024-70795-8) (choi2024functionalpathogenicityof pages 1-2) |
| Core phenotype | Usually congenital/prelingual, bilateral, approximately symmetric severe-to-profound SNHL; moderate-to-severe and asymmetric progressive disease also occur. Vestibular dysfunction was absent in the original families. | **Moderate:** consistent case-series evidence, but few patients and incomplete longitudinal characterization. | Collin et al., Jan 2008 (collin2008mutationsofesrrb pages 5-6, collin2008mutationsofesrrb pages 11-12); Choi et al., Sep 2024 (choi2024functionalpathogenicityof pages 3-4, choi2024functionalpathogenicityof pages 7-8) |
| Rarity and populations | Fewer than 20 affected families had been reported before the 2024 Korean case; many early families were consanguineous and Pakistani or Turkish. Disease-specific prevalence, incidence, and carrier frequency are unknown. | **Moderate for extreme rarity; limited for population estimates:** ascertainment is strongly family- and ancestry-biased. | Choi et al., Sep 2024 (choi2024functionalpathogenicityof pages 1-2); Collin et al., Jan 2008 (collin2008mutationsofesrrb pages 1-2, collin2008mutationsofesrrb pages 5-6) |
| Causal gene and protein | **ESRRB** encodes estrogen-related receptor β (ERRβ), an orphan nuclear-receptor transcription factor with a C4 zinc-finger DNA-binding domain and a C-terminal ligand-binding domain. | **Strong:** established molecular genetics and protein-domain biology. | Collin et al., Jan 2008, [DOI](https://doi.org/10.1016/j.ajhg.2007.09.008) (collin2008mutationsofesrrb pages 5-6); Choi et al., Sep 2024 (choi2024functionalpathogenicityof pages 1-2) |
| Variant spectrum | A 2024 synthesis identified **25 reported alleles representing 22 unique variants**: 90.9% SNVs; 72.7% missense, 4.5% nonsense, 9.1% frameshift, 9.1% splice, and 4.5% in-frame. Nine coding variants mapped to each of the DNA- and ligand-binding domains. | **Moderate-to-strong:** literature synthesis backed by reported pedigrees; classifications may change with new population or functional evidence. | Choi et al., Sep 2024 (choi2024functionalpathogenicityof pages 5-7) |
| Exemplar pathogenic variants | Segregating examples include **c.1018_1024dupGAGTTTG (p.Val342GlyfsTer44)**, **p.Ala110Val**, **p.Leu320Pro**, **p.Val342Leu**, **p.Leu347Pro**, **c.397+2T>G**, and **p.Arg382Cys** in trans with a loss-of-function allele. **p.Pro386Ser** was found in controls and treated as polymorphic; **p.Thr389Met** remained uncertain. | **Strong for segregating loss-of-function/domain variants; variable for missense variants.** | Collin et al., Jan 2008 (collin2008mutationsofesrrb pages 5-6); Choi et al., Sep 2024 (choi2024functionalpathogenicityof pages 2-3, choi2024functionalpathogenicityof pages 8-9) |
| 2024 functional advance | **c.397+2T>G** caused exon-4 skipping, premature termination, and nonsense-mediated decay. **p.Arg382Cys** destabilized ERRβ and abolished/reduced transcriptional activity; authors assigned **PS3-supporting** but retained a “warm VUS” rather than pathogenic classification. Its gnomAD v4.1 East-Asian frequency was **0.007065**, versus **0.002095** overall. | **Strong functional evidence for splicing; moderate supporting evidence for p.Arg382Cys:** patient cells, minigene, reporter, protein, and computational assays, but one family and no knock-in animal. | Choi et al., Sep 2024, [DOI](https://doi.org/10.1038/s41598-024-70795-8) (choi2024functionalpathogenicityof pages 3-4, choi2024functionalpathogenicityof pages 5-7, choi2024functionalpathogenicityof pages 8-9) |
| Molecular mechanism | Biallelic loss or hypomorphic dysfunction reduces ERRβ-dependent transcription. In patient cells, **ATP1B1** and **EGR1** decreased 55.1% and 45.4% versus the father; splice-allele-associated targets **NRP1**, **TBX3**, and **SPARC** fell approximately 48–53%. Disruption of cochlear ion/fluid homeostasis is plausible, but the complete human causal pathway remains partly inferred. | **Moderate:** direct cellular transcriptional evidence plus animal/anatomical support; downstream electrophysiology has not been demonstrated in affected humans. | Choi et al., Sep 2024 (choi2024functionalpathogenicityof pages 5-7); Collin et al., Jan 2008 (collin2008mutationsofesrrb pages 11-12) |
| Anatomy and cell types | ESRRB localizes to cochlear supporting and nonsensory tissues, stria vascularis/spiral ligament, nerve fibers, and spiral-ganglion cells; it was not detected in inner or outer hair cells. Absent otoacoustic emissions therefore likely reflect secondary outer-hair-cell dysfunction. | **Moderate:** developmental mouse RNA localization and postnatal rat immunohistochemistry, supported by human audiology; direct human cochlear tissue evidence is lacking. | Collin et al., Jan 2008 (collin2008mutationsofesrrb pages 11-12, collin2008mutationsofesrrb pages 9-11) |
| Model-organism evidence | Complete **Esrrb** loss is embryonically lethal; rescued or conditional-null mice show impaired hearing and balance, circling/head tossing, and defective stria-vascularis development. | **Moderate-to-strong mechanistic support:** mammalian loss-of-function phenotype, although it does not precisely model every human allele or the nonsyndromic presentation. | Collin et al., Jan 2008 (collin2008mutationsofesrrb pages 11-12) |
| Diagnosis | Confirm SNHL audiologically, exclude acquired causes and structural anomalies as indicated, then use a comprehensive hearing-loss panel or exome/genome sequencing with CNV analysis. Establish **biallelic variants in trans**, perform segregation testing, and use RNA/minigene or other functional assays for splice variants and unresolved VUSs. | **Strong for molecular approach; disease-specific evidence derives mainly from targeted sequencing/WES and functional follow-up.** | Ghasemnejad et al., Feb 2022, [DOI](https://doi.org/10.1186/s12920-022-01165-4) (ghasemnejad2022anovelmissense pages 2-4); Choi et al., Sep 2024 (choi2024functionalpathogenicityof pages 2-3) |
| Treatment and trials | No disease-modifying or ESRRB-specific therapy is established. Current care is individualized hearing aids, cochlear-implant evaluation for severe-to-profound loss, speech/language and auditory rehabilitation, educational support, and serial audiometry. Searches identified no ESRRB/DFNB35-specific interventional trial. | **General standard-of-care evidence; very limited DFNB35-specific outcome evidence.** Absence of a retrieved trial is search-limited, not proof that none exists. | Choi et al., Sep 2024 (choi2024functionalpathogenicityof pages 1-2, choi2024functionalpathogenicityof pages 11-12) |
| Major evidence gaps | No reliable prevalence, penetrance, carrier-frequency, sex-ratio, natural-history, cochlear-implant outcome, modifier-gene, gene–environment, protective-factor, biomarker, epigenomic, metabolomic, or human single-cell dataset is available specifically for DFNB35. Dental-decay association and variant-specific genotype–phenotype correlations remain insufficiently established. | **Evidence insufficient:** conclusions should not be extrapolated from general SNHL without qualification. | Variant and family limitations summarized by Choi et al., Sep 2024 (choi2024functionalpathogenicityof pages 7-8, choi2024functionalpathogenicityof pages 1-2, choi2024functionalpathogenicityof pages 8-9) |


*Table: Compact evidence-grade synthesis of the disease identity, phenotype, genetics, mechanism, clinical implementation, and principal knowledge gaps in ESRRB-related DFNB35.*

## Evidence scope and limitations

This synthesis prioritizes the original gene-discovery study and the 2024 functional study. Evidence labels used below are **human clinical/genetic**, **animal**, **in vitro**, or **computational/inferred**. The retrieved primary-text excerpts did not provide verified PMID metadata; therefore, PMIDs are not guessed. DOI links and publication dates are supplied instead. Database identifiers should be revalidated against the live database before production ingestion, particularly because ontology releases and ClinVar assertions change.

---

## 1. Disease information

### Definition

DFNB35 is an **autosomal-recessive nonsyndromic hearing impairment** in which two disease-relevant ESRRB alleles impair cochlear auditory function without a consistently established extra-auditory syndrome. The locus maps to **14q24.3**. The original report established causality through linkage/homozygosity mapping, segregation of biallelic variants in multiple pedigrees, absence from matched controls, protein-domain modeling, and inner-ear expression studies. (collin2008mutationsofesrrb pages 1-2, collin2008mutationsofesrrb pages 5-6)

### Identifiers and synonyms

- **Preferred name:** autosomal recessive nonsyndromic hearing loss 35.
- **Synonyms:** DFNB35; deafness, autosomal recessive 35; ESRRB-related nonsyndromic hearing loss; ESRRB-related autosomal-recessive nonsyndromic hearing impairment.
- **MONDO:** **MONDO:0012060**, as supplied in the request; confirm against the current MONDO release.
- **Gene/locus:** **ESRRB**, chromosome 14q24.3; transcript used in the 2024 study: **NM_004452.4**. (choi2024functionalpathogenicityof pages 1-2)
- **OMIM:** commonly represented as the DFNB35/deafness phenotype and ESRRB gene entries, but exact accession numbers were not verified in the retrieved evidence and should not be populated without direct OMIM validation.
- **Orphanet:** no disease-specific identifier was verified.
- **ICD-10/ICD-11:** no genotype-specific code exists in the evidence reviewed. Code under congenital/bilateral sensorineural hearing loss according to the documented phenotype and local coding rules.
- **MeSH:** use *Hearing Loss, Sensorineural* and *Hearing Loss, Genetic*; no DFNB35-specific MeSH heading was identified.

The disease description is based on **aggregated family-level literature and disease resources**, not individual EHR-derived population surveillance. The 2024 report does include one deeply phenotyped clinical proband. (choi2024functionalpathogenicityof pages 2-3, choi2024functionalpathogenicityof pages 1-2)

---

## 2. Etiology, risk, protection, and gene–environment interaction

### Primary cause

The demonstrated cause is **biallelic germline ESRRB variation**, usually homozygous in consanguineous families but also compound heterozygous. Pathogenic mechanisms include frameshift/truncation, canonical-splice disruption with NMD, and damaging missense changes in the DNA-binding or ligand-binding domains. (collin2008mutationsofesrrb pages 5-6, choi2024functionalpathogenicityof pages 5-7)

### Genetic risk factors

- Having two pathogenic or functionally damaging alleles in trans is the principal risk factor.
- Parental consanguinity increases the probability of homozygosity for rare recessive alleles; many discovery pedigrees were consanguineous.
- Family history may be absent in a recessive condition, especially in a small family.
- p.Arg382Cys may be an East-Asian-enriched **hypomorphic risk allele** that manifests when paired with a severe loss-of-function allele, but this remains a hypothesis rather than a settled classification. Its reported gnomAD v4.1 allele frequency was **0.007065 in East Asians** and **0.002095 overall**. (choi2024functionalpathogenicityof pages 3-4, choi2024functionalpathogenicityof pages 8-9)

No validated modifier gene, susceptibility locus outside ESRRB, or protective ESRRB allele has been established specifically for DFNB35.

### Environmental and lifestyle factors

Noise, ototoxic drugs, congenital infection, and other exposures can independently worsen hearing, but they are **not demonstrated causes of DFNB35**. In the 2022 Iranian family, no relevant environmental or ototoxic exposure was reported; in the Korean proband, congenital CMV testing was negative. (ghasemnejad2022anovelmissense pages 2-4, choi2024functionalpathogenicityof pages 2-3)

No disease-specific association with smoking, alcohol, diet, exercise, occupation, radiation, toxins, or infectious agents is established. Avoidance of excessive noise and ototoxic exposure is prudent hearing conservation, not proven prevention of the inherited lesion.

### Protective factors and gene–environment interaction

No genetic, nutritional, pharmacological, or behavioral factor has been shown to prevent ESRRB-related disease. A formal ESRRB genotype-by-noise, infection, age, sex, hormone, or drug interaction has not been demonstrated. Because ERRβ is a transcriptional regulator and the Korean ear showed longitudinal progression, environmental modifiers are biologically possible but presently speculative.

---

## 3. Phenotypes

### Core auditory phenotype

1. **Sensorineural hearing loss** — clinical sign/functional abnormality; suggested HPO: **HP:0000407**.
2. **Congenital hearing impairment** — onset descriptor; suggested HPO: **HP:0008527**.
3. **Prelingual hearing loss** — suggested HPO: **HP:0012715**.
4. **Bilateral hearing impairment** — suggested HPO: **HP:0008619**.
5. **Severe or profound hearing impairment** — use the current HPO severity terms after release validation.
6. **Progressive hearing impairment**, where documented — **HP:0001730**.
7. **Asymmetric hearing loss**, documented in the 2024 proband — use an HPO asymmetry/laterality annotation if supported in the target HPO release.

Most reported patients had symmetric, prelingual, severe-to-profound SNHL. The Korean proband had moderate right-ear and severe-to-profound left-ear SNHL, with right-ear progression over 17 years. The Iranian p.Gly167Arg family had congenital bilateral severe-to-profound loss. (ghasemnejad2022anovelmissense pages 2-4, choi2024functionalpathogenicityof pages 3-4, choi2024functionalpathogenicityof pages 7-8)

Transient-evoked otoacoustic emissions were absent in affected members of the original TR-21 pedigree, indicating outer-hair-cell system dysfunction. Because ESRRB was not detected in hair cells, the authors interpreted this as a likely secondary physiological consequence. (collin2008mutationsofesrrb pages 11-12)

### Vestibular and extra-auditory features

The original human families had **no reported vestibular dysfunction**, despite vestibular expression and balance abnormalities in knockout animals. Normal vestibular function should therefore be regarded as typical but not proven universal. (collin2008mutationsofesrrb pages 11-12)

No reproducible endocrine, neurological, renal, ocular, cardiac, immune, or metabolic syndrome is established. One affected male reproduced, arguing against obligatory male infertility. (collin2008mutationsofesrrb pages 9-11)

A proposed association between ESRRB/DFNB35 and dental decay has appeared in the literature, but the retrieved evidence did not establish penetrance, causality, or a consistent syndromic dental phenotype. Dental caries should **not** presently be treated as a defining DFNB35 manifestation.

### Quality-of-life effects

No DFNB35-specific EQ-5D, SF-36, PROMIS, language, educational, or participation dataset exists. By clinical inference from congenital severe-to-profound SNHL, untreated disease can impair spoken-language acquisition, communication, education, social participation, and employment. These are general consequences of early severe hearing loss, not quantified DFNB35-specific outcomes.

---

## 4. Genetic and molecular information

### Gene and protein

**ESRRB** encodes ERRβ, a nuclear-receptor-family transcription factor. It contains an N-terminal C4 zinc-finger **DNA-binding domain** and a C-terminal **ligand-binding domain**. ERRβ is considered an orphan receptor; no disease-correcting endogenous ligand is established. (ghasemnejad2022anovelmissense pages 2-4, collin2008mutationsofesrrb pages 5-6)

Suggested annotations:

- HGNC symbol: **ESRRB**; HGNC identifier should be verified directly before ingestion.
- GO molecular function: DNA-binding transcription-factor activity; sequence-specific DNA binding; nuclear-receptor activity; transcription coregulator binding.
- GO cellular component: nucleus, nucleoplasm, transcription regulator complex.
- GO biological process: regulation of transcription by RNA polymerase II; inner-ear development; sensory perception of sound; epithelial/ion-homeostasis regulation. The last two should be annotated with evidence qualifiers reflecting model/inference.

### Variant spectrum

The 2024 synthesis counted **25 reported alleles representing 22 unique variants**. Of these, 90.9% were SNVs, 4.5% indels, and 4.5% duplications; 72.7% were missense, 4.5% nonsense, 9.1% frameshift, 9.1% splice, and 4.5% in-frame. Nine coding variants localized to the DNA-binding domain and nine to the ligand-binding domain. No significant phenotype difference by domain was demonstrated. (choi2024functionalpathogenicityof pages 5-7)

Representative variants include:

- **c.1018_1024dupGAGTTTG, p.Val342GlyfsTer44** — homozygous frameshift/truncating allele in TR-21.
- **c.329C>T, p.Ala110Val** — DNA-binding-domain missense.
- **c.959T>C, p.Leu320Pro**, **c.1024G>T, p.Val342Leu**, and **c.1040C>T, p.Leu347Pro** — ligand-binding-domain missense variants.
- **c.1018_1020delGAG, p.Glu340del** — in-frame ligand-binding-domain deletion, segregating in a Pakistani pedigree and absent from 500 control chromosomes.
- **c.499G>A, p.Gly167Arg** — homozygous missense variant in an Iranian Azeri Turkish family, absent from 200 controls and public frequency data available to that study.
- **c.397+2T>G** — canonical splice-region variant causing exon-4 skipping and NMD.
- **c.1144C>T, p.Arg382Cys** — recurrent ligand-binding-domain missense VUS with supporting functional evidence. (choi2024functionalpathogenicityof pages 2-3, ghasemnejad2022anovelmissense pages 2-4, collin2008mutationsofesrrb pages 5-6, choi2024functionalpathogenicityof pages 3-4)

Important counterexamples are **p.Pro386Ser**, seen in 9/100 Pakistani controls including two homozygotes and interpreted as polymorphic, and heterozygous **p.Thr389Met**, for which no second allele was found and pathogenicity remained uncertain. These illustrate why domain location and in-silico prediction alone are insufficient. (collin2008mutationsofesrrb pages 5-6)

All established disease alleles are **germline**. Somatic ESRRB alterations are not relevant to the inherited DFNB35 mechanism.

### Functional consequences

- **c.397+2T>G:** mutant minigene product was 260 bp versus 670 bp for wild type; sequencing confirmed exon-4 skipping. Premature termination and cycloheximide rescue of transcript levels supported NMD. (choi2024functionalpathogenicityof pages 3-4, choi2024functionalpathogenicityof pages 5-7)
- **p.Arg382Cys:** lost modeled interactions with Lys335, Glu337, and Glu385; molecular dynamics showed increased structural fluctuation and solvent exposure. Protein and reporter studies demonstrated instability and markedly impaired transcriptional activity. (choi2024functionalpathogenicityof pages 3-4)
- Patient-cell expression changes included **ATP1B1 −55.1%** and **EGR1 −45.4%** versus the father; NRP1, TBX3, and SPARC were reduced by approximately 48–53% in comparisons informative for the splice allele. (choi2024functionalpathogenicityof pages 5-7)

### Modifiers, epigenetics, and chromosomal abnormalities

No validated modifier gene or disease-specific methylation, histone, chromatin, or noncoding-regulatory signature is known. DFNB35 is not classically a chromosomal-abnormality disorder. CNV analysis remains appropriate diagnostically, but no recurrent large ESRRB deletion/duplication syndrome was established in the reviewed evidence.

---

## 5. Environmental information

No toxin, pollutant, radiation source, lifestyle exposure, or pathogen is necessary or sufficient to cause DFNB35. Congenital CMV and structural abnormalities should be excluded when clinically appropriate because they can phenocopy congenital SNHL; the Korean proband had negative CMV testing and normal CT/MRI. (choi2024functionalpathogenicityof pages 2-3)

Recommended knowledge-base representation is therefore:

- genetic causal factor: **present/established**;
- environmental causal factor: **none established**;
- infectious trigger: **none established**;
- lifestyle factor: **none established**;
- general aggravators such as noise/ototoxic drugs: **plausible but not DFNB35-specific**.

---

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic ESRRB variants lead to** absent, unstable, structurally altered, or hypomorphic ERRβ protein.
2. Defective ERRβ **results in** reduced nuclear transcriptional activity at ERRβ-regulated genes; exon-skipping alleles additionally **lead to** NMD and reduced transcript abundance.
3. Altered ERRβ transcription **leads to** dysregulation of inner-ear-relevant genes, including ATP1B1, EGR1, NRP1, TBX3, and SPARC in the 2024 cellular system. (Demonstrated in patient-derived or transfected cells.)
4. This transcriptional disturbance **is inferred to impair** development or maintenance of cochlear nonsensory/supporting, strial, ligament, neural, and fluid-homeostatic compartments.
5. **Stria-vascularis branch:** defective marginal-cell/strial development or function **is inferred to disturb** endolymph production, ionic homeostasis, and the endocochlear electrochemical environment required for mechanotransduction.
6. **Supporting/neural branch:** dysfunction in organ-of-Corti supporting cells, nerve fibers, and spiral-ganglion cells **may lead to** impaired sensory support and auditory signal transmission.
7. These changes **result in** cochlear dysfunction, secondary outer-hair-cell physiological failure, elevated auditory thresholds, and congenital/prelingual SNHL; in some genotypes the residual activity **may permit** moderate or progressive disease rather than congenital profound deafness. (choi2024functionalpathogenicityof pages 7-8, collin2008mutationsofesrrb pages 11-12, choi2024functionalpathogenicityof pages 5-7, collin2008mutationsofesrrb pages 9-11)

### Upstream versus downstream mechanisms

The upstream lesion is ESRRB loss or hypomorphic function. Intermediate events are altered transcription and impaired cochlear development/homeostasis. Downstream events are disturbed sensory transduction/neural signaling, absent otoacoustic emissions, and hearing loss. Direct endocochlear-potential measurements have not been reported in affected humans, so the human ion-homeostasis link remains mechanistically well motivated but partly inferred.

### Pathways and cellular processes

This is principally a **transcriptional-regulatory/nuclear-receptor** disorder, not a proven Wnt, MAPK, PI3K–AKT, mTOR, inflammatory, autophagic, or primary metabolic-storage disease. ATP1B1 dysregulation provides a plausible connection to Na+/K+-ATPase-dependent ion gradients. No primary immune mechanism, metabolite accumulation, fibrosis, ischemia, or apoptotic cascade has been established.

Suggested GO biological-process terms include regulation of transcription by RNA polymerase II; inner-ear morphogenesis; cochlear development; auditory receptor-cell support; potassium-ion homeostasis; sensory perception of sound; and auditory-system development. Ion-homeostasis annotations should carry an **inferred/model-supported** qualifier.

Suggested Cell Ontology targets, subject to exact ID validation, include marginal cell of stria vascularis, epithelial supporting cell, spiral-ganglion neuron, Schwann/glial cell, fibrocyte, and sensory epithelial supporting cell. Hair cells should not be annotated as the principal ESRRB-expressing target on current evidence. (collin2008mutationsofesrrb pages 11-12, collin2008mutationsofesrrb pages 9-11)

### Molecular profiling and advanced technologies

The strongest disease-specific molecular profiling is targeted transcript quantification in the 2024 family/cell experiments. No validated DFNB35-specific bulk transcriptomic, proteomic, metabolomic, lipidomic, spatial-transcriptomic, or integrated multi-omic signature is available. No ESRRB patient-derived inner-ear organoid, iPSC auditory model, or CRISPR functional screen was identified.

---

## 7. Anatomical structures affected

### Organ and tissue levels

The primary organ is the **inner ear**, specifically the cochlea. Suggested anatomy annotations are cochlea, cochlear duct, organ of Corti, stria vascularis, spiral ligament, spiral limbus, basilar membrane, and spiral ganglion. Exact UBERON identifiers should be programmatically validated against the target release.

Developmental mouse RNA and postnatal rat immunohistochemistry localized Esrrb/ERRβ to cochlear turns, stria vascularis, vestibular structures, vestibular ganglion, spiral-limbus and basilar-membrane mesothelial cells, organ-of-Corti supporting cells, parts of the spiral ligament, nerve fibers, and spiral-ganglion cells. It was absent from inner and outer hair cells. (collin2008mutationsofesrrb pages 11-12, collin2008mutationsofesrrb pages 9-11)

### Subcellular level

ERRβ acts principally in the **nucleus/nucleoplasm**, where its DNA-binding domain recognizes regulatory sequences and its ligand-binding domain supports receptor conformation and transcriptional regulation. p.Arg382Cys primarily affects protein stability and transcriptional competence rather than a demonstrated mitochondrial, lysosomal, ER, or ciliary process.

### Localization and laterality

Human disease is usually bilateral. Symmetry is common, but the 2024 case establishes that marked asymmetry can occur. Normal temporal-bone CT and internal-auditory-canal MRI in that patient indicate that gross malformation is not required. (choi2024functionalpathogenicityof pages 2-3)

---

## 8. Temporal development

Typical onset is congenital or recognized before language acquisition. The course is chronic and lifelong. Most early reports described severe-to-profound impairment without adequate longitudinal data to distinguish stable from progressive disease. The Korean case demonstrated progression in the better ear over 17 years, expanding the natural history. (choi2024functionalpathogenicityof pages 3-4, choi2024functionalpathogenicityof pages 7-8)

No formal stages, remission pattern, spontaneous recovery, or disease-specific progression rate has been defined. The critical clinical period is early infancy and childhood, when auditory access is required for language development. Newborn hearing screening, prompt confirmation, amplification or implant evaluation, and early communication intervention are therefore essential, although not ESRRB-specific.

---

## 9. Inheritance and population

### Inheritance

Inheritance is **autosomal recessive**. For two confirmed heterozygous carrier parents, each pregnancy has an expected 25% probability of an affected child, 50% probability of an unaffected carrier, and 25% probability of inheriting neither familial allele, assuming conventional Mendelian segregation.

Available pedigrees are compatible with high penetrance for severe biallelic alleles, but a numerical penetrance estimate is unavailable. Expressivity is variable in severity, symmetry, and progression. There is no evidence of anticipation. Germline mosaicism has not been specifically reported but cannot be reduced to zero in counseling.

### Epidemiology and demographics

No incidence or prevalence per 100,000 is available. Fewer than 20 families were known before the 2024 report; thus DFNB35 accounts for only a very small fraction of genetic hearing loss. (choi2024functionalpathogenicityof pages 1-2)

Early reports were enriched for Pakistani and Turkish consanguineous families, with additional Iranian, Tunisian, Czech, Egyptian, and Korean observations in the wider literature. This distribution reflects ascertainment and founder structure as well as possible allele enrichment; it does not imply restriction to those ancestries. No reliable male:female ratio, age distribution, carrier frequency, or global geographic prevalence is known.

The relatively high East-Asian frequency of p.Arg382Cys demands caution: functional impairment does not by itself prove that homozygosity causes fully penetrant DFNB35. Its proposed role as a hypomorphic allele in trans with loss of function needs replication. (choi2024functionalpathogenicityof pages 3-4, choi2024functionalpathogenicityof pages 8-9)

---

## 10. Diagnostics

### Clinical evaluation

1. Newborn or childhood hearing screening.
2. Diagnostic age-appropriate audiology: auditory brainstem response, otoacoustic emissions, tympanometry, behavioral pure-tone audiometry, and speech testing where developmentally appropriate.
3. Confirm sensorineural rather than conductive loss and document laterality, configuration, severity, and progression.
4. Assess vestibular symptoms and perform targeted examination.
5. Review prenatal/perinatal history, congenital infection, noise, trauma, and ototoxic exposure.
6. CT or MRI is not required to diagnose DFNB35 but may exclude structural or neural causes, particularly with asymmetry or implant planning. The Korean patient had normal CT/MRI. (choi2024functionalpathogenicityof pages 2-3)

There is no blood chemistry, urine test, enzyme assay, biopsy, histopathology, circulating protein, metabolite, or imaging biomarker specific to DFNB35.

### Genetic testing strategy

A comprehensive **hearing-loss multigene panel** including ESRRB is usually more efficient than initial ESRRB-only testing because congenital SNHL is highly heterogeneous. WES is appropriate when panel testing is negative or broad phenotyping is required; WGS can detect cryptic splice, regulatory, and structural variants missed by WES. In the reported families, successful methods included linkage/homozygosity mapping, targeted capture, WES, PCR/Sanger confirmation, segregation analysis, and functional RNA/minigene assays. (ghasemnejad2022anovelmissense pages 2-4, collin2008mutationsofesrrb pages 1-2, choi2024functionalpathogenicityof pages 2-3)

Required interpretation steps are:

- identify two relevant ESRRB alleles;
- demonstrate that they are **in trans**;
- apply hearing-loss-specific ACMG/AMP criteria;
- inspect population frequencies by ancestry;
- evaluate splice effects experimentally when feasible;
- avoid upgrading missense variants solely from in-silico prediction;
- test relatives for segregation.

CMA or genome-based CNV analysis may detect large deletions but is not a first-line standalone test for this sequence-variant-predominant disorder. Conventional karyotyping, FISH, mitochondrial testing, and repeat-expansion testing do not directly interrogate the usual DFNB35 mechanism; use them only when the broader differential indicates.

### Differential diagnosis

The differential includes GJB2/GJB6-related deafness, SLC26A4-related disease/Pendred syndrome, OTOF-related auditory neuropathy, STRC deletions, congenital CMV, inner-ear malformations, mitochondrial hearing loss, syndromic deafness, and environmental/ototoxic injury. Distinguishing evidence includes molecular diagnosis, vestibular/thyroid/ocular/renal findings, imaging, CMV testing, auditory-neuropathy physiology, and exposure history.

---

## 11. Outcome and prognosis

DFNB35 is not known to shorten life expectancy or cause disease-specific mortality. Survival statistics are therefore not applicable. Morbidity is auditory and communication-related. Untreated congenital severe-to-profound loss can produce lifelong language, educational, and social disability; timely rehabilitation can substantially reduce functional consequences, although DFNB35-specific outcome rates are unavailable.

Spontaneous biological recovery is not reported. Hearing aids or cochlear implants improve access to sound but do not correct ESRRB dysfunction. No disease-specific prognostic biomarker exists. Residual hearing, age at intervention, duration of auditory deprivation, communication support, and neural integrity are clinically relevant general predictors, but they have not been validated specifically in DFNB35.

---

## 12. Treatment

### Current clinical management

There is no approved ESRRB-directed drug or disease-modifying therapy. Management is phenotype based:

- conventional hearing aids for aidable residual hearing;
- cochlear-implant assessment for severe-to-profound loss or inadequate aided speech access;
- auditory-verbal, speech-language, sign-language, or bilingual communication support according to family preference and clinical context;
- educational accommodations and assistive listening systems;
- serial audiometry, especially because progression and asymmetry can occur;
- psychosocial and family support.

Suggested NCIt concepts include **Hearing Aid**, **Cochlear Implantation**, **Auditory Rehabilitation**, **Speech Therapy**, **Genetic Counseling**, and **Audiologic Examination**; exact NCIt codes should be validated before ingestion.

No DFNB35-specific hearing-aid response percentage, cochlear-implant speech score, adverse-event rate, or comparative treatment trial was identified. Preservation of spiral-ganglion function may influence implant performance, but ESRRB expression in ganglion cells makes genotype-specific prediction uncertain. Counseling should not promise a particular implant outcome.

### Advanced and experimental therapy

As of the search performed for this report, no ESRRB/DFNB35-specific interventional clinical trial, AAV replacement study, gene-editing program, RNA therapy, cell therapy, or pharmacological rescue was identified. This is a search-limited negative result, not proof that no newly registered study exists.

Inner-ear gene therapy advanced rapidly in 2023–2024, particularly for **OTOF/DFNB9**, but this cannot be extrapolated directly to ESRRB. ERRβ is expressed in several nonsensory and neural cochlear cell populations, so successful therapy would require appropriate vector tropism, developmental timing, dosage control, and safety for a transcription factor. The authors of the 2024 study specifically identified a knock-in model as a needed next step. (choi2024functionalpathogenicityof pages 8-9, choi2024functionalpathogenicityof pages 11-12)

No ESRRB-specific pharmacogenomic recommendation exists.

---

## 13. Prevention

### Primary prevention

The genotype cannot be prevented by lifestyle modification after conception. Reproductive options following identification of familial variants include genetic counseling, partner testing, cascade carrier testing, preimplantation genetic testing for monogenic disease, prenatal diagnosis, donor gametes, and informed natural conception. These are options, not directives.

### Secondary prevention

Universal newborn hearing screening, rapid diagnostic audiology, molecular testing, and cascade testing permit early intervention and identification of at-risk relatives. For siblings with the familial genotype, audiological surveillance should begin immediately even if initial screening is reassuring.

### Tertiary prevention

Early amplification/implant evaluation, communication access, speech-language services, educational support, and avoidance of preventable cochlear injury reduce secondary disability. Routine vaccination prevents infectious causes of hearing loss but does not prevent ESRRB-related DFNB35. No medication or prophylactic procedure prevents the molecular disease.

---

## 14. Other species and natural disease

### Comparative biology

Orthologous **Esrrb** is present in laboratory mouse (*Mus musculus*, NCBI Taxonomy 10090) and rat (*Rattus norvegicus*, Taxonomy 10116). Developmental expression is evolutionarily consistent with an inner-ear role. No naturally occurring companion-animal breed disorder confidently equivalent to human DFNB35 was identified, and no VBO breed annotation is warranted.

DFNB35 is neither infectious nor zoonotic; transmission is genetic. Cross-species susceptibility refers to conserved loss-of-function biology, not contagious transmission.

---

## 15. Model organisms

### Mouse models

Complete Esrrb-null mice die embryonically, limiting direct postnatal auditory analysis. Rescued or conditional-null animals show defective hearing and balance, walking abnormalities, circling/head tossing, and impaired stria-vascularis development. These findings support the proposed developmental and fluid-homeostatic mechanism. (collin2008mutationsofesrrb pages 11-12)

**Strengths:** mammalian cochlear architecture; recapitulation of hearing/balance dysfunction; capacity to study strial development and auditory physiology.

**Limitations:** embryonic lethality of complete loss; balance disease is more prominent than in reported humans; null alleles may not model human hypomorphic missense variants; no p.Arg382Cys knock-in model was available in the 2024 report. (choi2024functionalpathogenicityof pages 8-9)

### Rat and cellular systems

Postnatal rat inner-ear immunohistochemistry has been useful for mapping ERRβ to supporting, strial, ligament, neural, and ganglion compartments. (collin2008mutationsofesrrb pages 9-11)

Cell models used in 2024 included patient-derived lymphoblastoid cells, minigene splice assays, HEK293T reporter assays, protein-stability assays, and computational molecular dynamics. These directly test splicing and transcription but cannot reproduce cochlear biomechanics, endocochlear potential, or developmental cell interactions. (choi2024functionalpathogenicityof pages 5-7, choi2024functionalpathogenicityof pages 3-4, choi2024functionalpathogenicityof pages 11-12)

Useful resources for future model curation include MGI, IMPC, IMSR/MMRRC, and Alliance of Genome Resources. A priority model is an ESRRB p.Arg382Cys knock-in, alone and in trans with a null allele, with longitudinal ABR, DPOAE, endocochlear-potential, vestibular, histological, and single-cell profiling.

---

## Recent developments and authoritative interpretation

The most important recent disease-specific publication is Choi et al., **Scientific Reports**, published September 2024, DOI: https://doi.org/10.1038/s41598-024-70795-8. Its abstract states: “The splicing variant … caused exon 4 skipping, leading to premature stop codon formation and nonsense-mediated decay,” and reports that p.Arg382Cys “reduced transcriptional activity and altered expression of downstream target genes essential for inner ear function.” This is the strongest functional evidence yet for reinterpretation of an ESRRB VUS, but the authors appropriately stopped short of a definitive pathogenic classification. (choi2024functionalpathogenicityof pages 2-3, choi2024functionalpathogenicityof pages 8-9)

The landmark gene-discovery paper is Collin et al., **American Journal of Human Genetics**, published January 2008, DOI: https://doi.org/10.1016/j.ajhg.2007.09.008. It established ESRRB as the DFNB35 gene through multiple linked consanguineous pedigrees and connected human disease to cochlear and strial expression. (collin2008mutationsofesrrb pages 1-2, collin2008mutationsofesrrb pages 5-6, collin2008mutationsofesrrb pages 11-12)

Ghasemnejad et al., **BMC Medical Genomics**, published February 2022, DOI: https://doi.org/10.1186/s12920-022-01165-4, described homozygous p.Gly167Arg in a consanguineous Iranian Azeri Turkish family. Its abstract reports that the variant co-segregated with ARNSHL and emphasizes targeted genomic capture for genetically heterogeneous hearing loss. The pathogenic interpretation relied heavily on segregation and computational evidence and is consequently less functionally resolved than the 2024 alleles. (ghasemnejad2022anovelmissense pages 2-4)

## Priority knowledge gaps

1. A curated, transcript-consistent ClinVar/LOVD inventory of every ESRRB allele with current ACMG classifications and ancestry-specific frequencies.
2. Prospective natural-history data with standardized audiograms, vestibular testing, speech outcomes, and treatment history.
3. Replication and segregation studies for p.Arg382Cys, especially homozygotes and loss-of-function compound heterozygotes.
4. Human inner-ear or iPSC-derived cell models and allele-specific knock-in mice.
5. Direct measurements of endocochlear potential, ion transport, and strial physiology.
6. DFNB35-specific hearing-aid and cochlear-implant outcomes.
7. Rigorous assessment of proposed dental involvement, modifier genes, environmental interactions, and sex effects.
8. Cell-type-resolved transcriptomics/spatial profiling and evaluation of therapeutic vector tropism.

## Knowledge-base conclusion

The highest-confidence entry is: **biallelic germline ESRRB loss-of-function or damaging hypomorphic variants cause a very rare autosomal-recessive, usually congenital/prelingual bilateral SNHL through impaired ERRβ transcriptional regulation in cochlear nonsensory, strial, supporting, and neural compartments**. Disturbed stria-vascularis/endolymph ion homeostasis is strongly supported by expression and animal data but remains partly inferred in humans. Phenotypic breadth now includes moderate, asymmetric, and progressive hearing loss. No syndrome-defining extra-auditory feature, prevalence estimate, biomarker, disease-modifying therapy, or ESRRB-specific clinical trial is established. (collin2008mutationsofesrrb pages 11-12, choi2024functionalpathogenicityof pages 7-8, choi2024functionalpathogenicityof pages 5-7)

References

1. (choi2024functionalpathogenicityof pages 1-2): Won Hoon Choi, Yeijean Cho, Ju Hyuen Cha, Dae Hee Lee, Jong Gwan Jeong, Sung Ho Jung, Jae-Jin Song, Jun Ho Lee, and Sang-Yeon Lee. Functional pathogenicity of esrrb variant of uncertain significance contributes to hearing loss (dfnb35). Scientific Reports, Sep 2024. URL: https://doi.org/10.1038/s41598-024-70795-8, doi:10.1038/s41598-024-70795-8. This article has 3 citations and is from a peer-reviewed journal.

2. (choi2024functionalpathogenicityof pages 7-8): Won Hoon Choi, Yeijean Cho, Ju Hyuen Cha, Dae Hee Lee, Jong Gwan Jeong, Sung Ho Jung, Jae-Jin Song, Jun Ho Lee, and Sang-Yeon Lee. Functional pathogenicity of esrrb variant of uncertain significance contributes to hearing loss (dfnb35). Scientific Reports, Sep 2024. URL: https://doi.org/10.1038/s41598-024-70795-8, doi:10.1038/s41598-024-70795-8. This article has 3 citations and is from a peer-reviewed journal.

3. (choi2024functionalpathogenicityof pages 3-4): Won Hoon Choi, Yeijean Cho, Ju Hyuen Cha, Dae Hee Lee, Jong Gwan Jeong, Sung Ho Jung, Jae-Jin Song, Jun Ho Lee, and Sang-Yeon Lee. Functional pathogenicity of esrrb variant of uncertain significance contributes to hearing loss (dfnb35). Scientific Reports, Sep 2024. URL: https://doi.org/10.1038/s41598-024-70795-8, doi:10.1038/s41598-024-70795-8. This article has 3 citations and is from a peer-reviewed journal.

4. (choi2024functionalpathogenicityof pages 5-7): Won Hoon Choi, Yeijean Cho, Ju Hyuen Cha, Dae Hee Lee, Jong Gwan Jeong, Sung Ho Jung, Jae-Jin Song, Jun Ho Lee, and Sang-Yeon Lee. Functional pathogenicity of esrrb variant of uncertain significance contributes to hearing loss (dfnb35). Scientific Reports, Sep 2024. URL: https://doi.org/10.1038/s41598-024-70795-8, doi:10.1038/s41598-024-70795-8. This article has 3 citations and is from a peer-reviewed journal.

5. (choi2024functionalpathogenicityof pages 8-9): Won Hoon Choi, Yeijean Cho, Ju Hyuen Cha, Dae Hee Lee, Jong Gwan Jeong, Sung Ho Jung, Jae-Jin Song, Jun Ho Lee, and Sang-Yeon Lee. Functional pathogenicity of esrrb variant of uncertain significance contributes to hearing loss (dfnb35). Scientific Reports, Sep 2024. URL: https://doi.org/10.1038/s41598-024-70795-8, doi:10.1038/s41598-024-70795-8. This article has 3 citations and is from a peer-reviewed journal.

6. (collin2008mutationsofesrrb pages 1-2): Rob W.J. Collin, Ersan Kalay, Muhammad Tariq, Theo Peters, Bert van der Zwaag, Hanka Venselaar, Jaap Oostrik, Kwanghyuk Lee, Zubair M. Ahmed, Refik Çaylan, Yun Li, Henk A. Spierenburg, Erol Eyupoglu, Angelien Heister, Saima Riazuddin, Elif Bahat, Muhammad Ansar, Selcuk Arslan, Bernd Wollnik, Han G. Brunner, Cor W.R.J. Cremers, Ahmet Karaguzel, Wasim Ahmad, Frans P.M. Cremers, Gert Vriend, Thomas B. Friedman, Sheikh Riazuddin, Suzanne M. Leal, and Hannie Kremer. Mutations of esrrb encoding estrogen-related receptor beta cause autosomal-recessive nonsyndromic hearing impairment dfnb35. American journal of human genetics, 82 1:125-38, Jan 2008. URL: https://doi.org/10.1016/j.ajhg.2007.09.008, doi:10.1016/j.ajhg.2007.09.008. This article has 146 citations and is from a highest quality peer-reviewed journal.

7. (collin2008mutationsofesrrb pages 5-6): Rob W.J. Collin, Ersan Kalay, Muhammad Tariq, Theo Peters, Bert van der Zwaag, Hanka Venselaar, Jaap Oostrik, Kwanghyuk Lee, Zubair M. Ahmed, Refik Çaylan, Yun Li, Henk A. Spierenburg, Erol Eyupoglu, Angelien Heister, Saima Riazuddin, Elif Bahat, Muhammad Ansar, Selcuk Arslan, Bernd Wollnik, Han G. Brunner, Cor W.R.J. Cremers, Ahmet Karaguzel, Wasim Ahmad, Frans P.M. Cremers, Gert Vriend, Thomas B. Friedman, Sheikh Riazuddin, Suzanne M. Leal, and Hannie Kremer. Mutations of esrrb encoding estrogen-related receptor beta cause autosomal-recessive nonsyndromic hearing impairment dfnb35. American journal of human genetics, 82 1:125-38, Jan 2008. URL: https://doi.org/10.1016/j.ajhg.2007.09.008, doi:10.1016/j.ajhg.2007.09.008. This article has 146 citations and is from a highest quality peer-reviewed journal.

8. (collin2008mutationsofesrrb pages 11-12): Rob W.J. Collin, Ersan Kalay, Muhammad Tariq, Theo Peters, Bert van der Zwaag, Hanka Venselaar, Jaap Oostrik, Kwanghyuk Lee, Zubair M. Ahmed, Refik Çaylan, Yun Li, Henk A. Spierenburg, Erol Eyupoglu, Angelien Heister, Saima Riazuddin, Elif Bahat, Muhammad Ansar, Selcuk Arslan, Bernd Wollnik, Han G. Brunner, Cor W.R.J. Cremers, Ahmet Karaguzel, Wasim Ahmad, Frans P.M. Cremers, Gert Vriend, Thomas B. Friedman, Sheikh Riazuddin, Suzanne M. Leal, and Hannie Kremer. Mutations of esrrb encoding estrogen-related receptor beta cause autosomal-recessive nonsyndromic hearing impairment dfnb35. American journal of human genetics, 82 1:125-38, Jan 2008. URL: https://doi.org/10.1016/j.ajhg.2007.09.008, doi:10.1016/j.ajhg.2007.09.008. This article has 146 citations and is from a highest quality peer-reviewed journal.

9. (choi2024functionalpathogenicityof pages 2-3): Won Hoon Choi, Yeijean Cho, Ju Hyuen Cha, Dae Hee Lee, Jong Gwan Jeong, Sung Ho Jung, Jae-Jin Song, Jun Ho Lee, and Sang-Yeon Lee. Functional pathogenicity of esrrb variant of uncertain significance contributes to hearing loss (dfnb35). Scientific Reports, Sep 2024. URL: https://doi.org/10.1038/s41598-024-70795-8, doi:10.1038/s41598-024-70795-8. This article has 3 citations and is from a peer-reviewed journal.

10. (collin2008mutationsofesrrb pages 9-11): Rob W.J. Collin, Ersan Kalay, Muhammad Tariq, Theo Peters, Bert van der Zwaag, Hanka Venselaar, Jaap Oostrik, Kwanghyuk Lee, Zubair M. Ahmed, Refik Çaylan, Yun Li, Henk A. Spierenburg, Erol Eyupoglu, Angelien Heister, Saima Riazuddin, Elif Bahat, Muhammad Ansar, Selcuk Arslan, Bernd Wollnik, Han G. Brunner, Cor W.R.J. Cremers, Ahmet Karaguzel, Wasim Ahmad, Frans P.M. Cremers, Gert Vriend, Thomas B. Friedman, Sheikh Riazuddin, Suzanne M. Leal, and Hannie Kremer. Mutations of esrrb encoding estrogen-related receptor beta cause autosomal-recessive nonsyndromic hearing impairment dfnb35. American journal of human genetics, 82 1:125-38, Jan 2008. URL: https://doi.org/10.1016/j.ajhg.2007.09.008, doi:10.1016/j.ajhg.2007.09.008. This article has 146 citations and is from a highest quality peer-reviewed journal.

11. (ghasemnejad2022anovelmissense pages 2-4): Tohid Ghasemnejad, Mahmoud Shekari Khaniani, Jafar Nouri Nojadeh, and Sima Mansoori Derakhshan. A novel missense variant in esrrb gene causing autosomal recessive non-syndromic hearing loss: in silico analysis of a case. BMC Medical Genomics, Feb 2022. URL: https://doi.org/10.1186/s12920-022-01165-4, doi:10.1186/s12920-022-01165-4. This article has 4 citations and is from a peer-reviewed journal.

12. (choi2024functionalpathogenicityof pages 11-12): Won Hoon Choi, Yeijean Cho, Ju Hyuen Cha, Dae Hee Lee, Jong Gwan Jeong, Sung Ho Jung, Jae-Jin Song, Jun Ho Lee, and Sang-Yeon Lee. Functional pathogenicity of esrrb variant of uncertain significance contributes to hearing loss (dfnb35). Scientific Reports, Sep 2024. URL: https://doi.org/10.1038/s41598-024-70795-8, doi:10.1038/s41598-024-70795-8. This article has 3 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Autosomal_Recessive_Nonsyndromic_Hearing_Loss_35-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 3 |
| Resolved | 3 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 3 |
| On topic | 1 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0012060` (2 mentions) - the report calls it "if available"; MONDO calls it **autosomal recessive nonsyndromic hearing loss 35**