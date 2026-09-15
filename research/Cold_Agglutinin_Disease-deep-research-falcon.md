---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-05T17:58:43.740951'
end_time: '2026-09-05T18:13:04.207536'
duration_seconds: 860.47
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Cold Agglutinin Disease
  mondo_id: MONDO:0018922
  category: Autoimmune
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 59
reference_validation:
  total_references: 17
  verified: 17
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  quotes_not_checkable: 1
  relevance_assessed: 17
  on_topic: 8
  validator_version: 0.2.1
term_validation:
  total_terms: 27
  verified: 26
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0018922
    reported_labels:
    - if available
    ontology_label: cold agglutinin disease
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
  path: Cold_Agglutinin_Disease-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Cold Agglutinin Disease
- **MONDO ID:** MONDO:0018922 (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on **Cold Agglutinin Disease** covering all of the
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
- **Disease Name:** Cold Agglutinin Disease
- **MONDO ID:** MONDO:0018922 (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on **Cold Agglutinin Disease** covering all of the
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


# Cold Agglutinin Disease: Comprehensive Disease-Characteristics Report

## Executive summary

Cold agglutinin disease (CAD) is a rare, chronic autoimmune hemolytic anemia and a distinct indolent clonal B-cell lymphoproliferative disorder of bone marrow. The clone usually secretes monoclonal IgMκ encoded by **IGHV4-34**; this antibody binds erythrocyte I antigen in cooler parts of the circulation, directly agglutinates red cells, and activates the classical complement pathway. C3-opsonized erythrocytes are cleared mainly by hepatic macrophages, while severe complement activation can also produce intravascular hemolysis. This dual mechanism explains the two principal clinical domains: complement-mediated anemia/fatigue and agglutination-mediated acral circulatory symptoms. CAD must be distinguished from **secondary cold agglutinin syndrome (CAS)** caused by infection, autoimmune disease, or overt malignancy. (berentsen2019coldagglutinindisease pages 1-2, berentsen2022coldagglutinindisease pages 1-2, berentsen2020newinsightsin pages 2-3)

The strongest recent advances are recognition of CAD-associated lymphoproliferative disorder as a distinct entity, molecular definition of its somatic landscape, and approval of **sutimlimab**, a C1s inhibitor that rapidly suppresses hemolysis. Long-term 2023–2024 studies show sustained hematologic and quality-of-life improvement during therapy, but recurrence after withdrawal and no reliable improvement in non-complement-mediated acral symptoms. (roth2024longtermefficacyand pages 1-2, berentsen2024theimpactof pages 11-12, berentsen2024theimpactof pages 3-4)

The following table summarizes the central quantitative evidence.

| Domain | Key quantitative finding | Evidence type/source (author/year) | DOI/URL |
|---|---|---|---|
| Epidemiology and anemia | 232 patients across 24 centers; cold versus warmer climates: prevalence 20 versus 5 per million and incidence 1.9 versus 0.48 per million/year. Mean baseline Hb 9.3 g/dL; 27% had Hb <8 g/dL. | Multinational observational cohort; Berentsen et al., 2020 (berentsen2020coldagglutinindiseasea pages 3-4) | [10.1182/blood.2020005674](https://doi.org/10.1182/blood.2020005674) |
| Clinical phenotypes | Anemia affects ~90%; cold-induced circulatory symptoms occur in 57–91%; acute hemolytic exacerbations in ~74%; fatigue was reported by 90% in a selected patient survey. | Clinical synthesis; Berentsen et al., 2024 (berentsen2024theimpactof pages 6-7) | [10.1080/17474086.2024.2372333](https://doi.org/10.1080/17474086.2024.2372333) |
| Thrombosis and mortality | At 1 year, thromboembolism occurred in 7.2% of CAD patients versus 1.9% of controls; at 5 years, 11.5% versus 7.8%. Median survival was 8.5 years; adjusted mortality HR 1.84 (95% CI 1.10–3.06). | Danish national-registry cohort; Bylsma et al., 2019 (berentsen2020coldagglutinindiseasea pages 10-11) | [10.1182/bloodadvances.2019000476](https://doi.org/10.1182/bloodadvances.2019000476) |
| Somatic genetics | In 18 patients, nonsynonymous mutations occurred in **KMT2D** 12/18 (67%), **CARD11** 6/18 (33%), and **CXCR4** 4/18 (22%); CARD11/CXCR4 lesions correlated with lower Hb. | Whole-exome/targeted genomic study; Małecka et al., 2021 (małecka2021themutationallandscape pages 1-3) | [10.1002/ajh.26205](https://doi.org/10.1002/ajh.26205) |
| Transcriptomics | RNA-seq of clonal B cells from 12 patients versus IgM-memory B cells from 4 controls identified 93 differentially expressed genes; **CR1/CD35** was reduced ~11-fold, with protein reduction confirmed by flow cytometry. | Human RNA-seq and flow-cytometry study; Małecka et al., 2024 (małecka2024geneexpressionanalysis pages 1-1) | [10.1093/cei/uxad135](https://doi.org/10.1093/cei/uxad135) |
| Diagnostic criteria | Confirmed CAD required chronic hemolysis, monospecific C3d-positive DAT, cold-agglutinin titer >64, and exclusion of overt lymphoma, active cancer, and recent *Mycoplasma pneumoniae* or EBV infection. | Cohort case-definition criteria; Berentsen et al., 2020 (berentsen2020coldagglutinindiseasea pages 6-7) | [10.1182/blood.2020005674](https://doi.org/10.1182/blood.2020005674) |
| Rituximab–bendamustine | Responses occurred in 35/45 (78%), including complete responses in 24/45 (53%); median response duration was not reached after 88 months, and estimated 5-year sustained remission was 77%. | Long-term observational treatment follow-up; Berentsen et al., 2020 (berentsen2020coldagglutinindiseasea pages 4-5, berentsen2020coldagglutinindiseasea pages 3-4) | [10.1182/blood.2020005674](https://doi.org/10.1182/blood.2020005674) |
| CARDINAL | Sutimlimab primary endpoint achieved by 13/24 (54%; 95% CI 33–74); mean Hb rose 1.2 g/dL at week 1 and 2.3 g/dL by week 3; bilirubin normalized by week 3. | Prospective phase 3 single-arm trial; summarized by Weitz, 2023 (weitz2023sutimlimabforthe pages 3-5) | [10.17925/OHR.2023.19.1.35](https://doi.org/10.17925/OHR.2023.19.1.35) |
| CADENZA | Composite response occurred in 16/22 (72.7%) with sutimlimab versus 3/20 (15%) with placebo; median Hb increase was 2.7 g/dL. | Randomized placebo-controlled phase 3 trial; summarized by Costa et al., 2025 (costa2025beneaththesurface pages 15-15) | [10.3389/fimmu.2025.1624667](https://doi.org/10.3389/fimmu.2025.1624667) |
| Long-term sutimlimab | Among 39 CADENZA Part B patients, 32 completed treatment; median exposure was 99 weeks. Mean on-treatment Hb remained ≥11.0 g/dL versus 9.3 at baseline, and bilirubin ≤20.0 μmol/L versus 35.0 at baseline; hemolysis recurred after withdrawal. | Phase 3 open-label extension; Röth et al., published August 2024 (roth2024longtermefficacyand pages 1-2) | [10.1016/j.eclinm.2024.102733](https://doi.org/10.1016/j.eclinm.2024.102733) |


*Table: Compact evidence table covering epidemiology, clinical burden, molecular findings, diagnostic criteria, and major treatment outcomes in cold agglutinin disease. It emphasizes cohort and trial-level quantitative findings without supplying unverified PMIDs.*

## 1. Disease information

### Definition and classification

CAD is a **primary, chronic, cold-antibody autoimmune hemolytic anemia** caused by a characteristic marrow B-cell clone. It accounts for approximately **15–30% of autoimmune hemolytic anemia**, although estimates depend on case definition. Contemporary classifications recognize the underlying marrow lesion—CAD-associated lymphoproliferative disorder—as distinct from lymphoplasmacytic lymphoma/Waldenström macroglobulinemia. (berentsen2019coldagglutinindisease pages 1-2, berentsen2022coldagglutinindisease pages 1-2, berentsen2024theimpactof pages 3-4)

A useful exact abstract statement is: **“Primary cold agglutinin disease is caused by a unique indolent B-cell lymphoproliferative disorder of the bone marrow.”** The evidence is human marrow pathology, flow cytometry, immunoglobulin sequencing, and somatic genomics—not inference from an animal model. (małecka2021themutationallandscape pages 1-3)

### Identifiers and synonyms

- **MONDO:** MONDO:0018922.
- **Orphanet:** commonly indexed as ORPHA:56425; database releases should be checked when ingesting the record.
- **ICD-10-CM:** D59.12, cold autoimmune hemolytic anemia. Older records may use less-specific D59.1.
- **ICD-11:** classified under autoimmune hemolytic anemia/cold-antibody hemolytic anemia; verify the current national ICD-11 extension code before implementation.
- **MeSH:** *Cold Agglutinin Disease*.
- **OMIM:** CAD is acquired and somatically clonal, not a defined Mendelian phenotype; no causal germline OMIM disease-gene entry should be assigned.
- **Synonyms:** primary cold agglutinin disease, chronic cold agglutinin disease, primary chronic CAD, cold-antibody autoimmune hemolytic anemia. “Cold agglutinin syndrome” should be reserved for secondary disease.

This report synthesizes **aggregated disease-level resources, cohorts, trials, and molecular studies**. EHR/claims studies are explicitly identified below; no individual-level patient record is represented.

## 2. Etiology and risk/protective factors

### Primary cause

The initiating lesion is an **acquired somatic B-cell clone**, not a known inherited mutation. Nearly all clones use IGHV4-34; IGKV3-20 or IGKV3-15 is common. Recurrent somatic lesions include **KMT2D** loss-of-function, activating **CARD11**, and C-terminal **CXCR4** variants predicted to impair receptor internalization. In an 18-patient sequencing cohort, nonsynonymous mutations occurred in KMT2D 12/18 (67%), CARD11 6/18 (33%), and CXCR4 4/18 (22%). These are disease-clone alterations, not germline pathogenic variants suitable for carrier testing. (małecka2021themutationallandscape pages 1-3, berentsen2022coldagglutinindisease pages 2-4)

### Demographic and environmental risk

CAD mainly affects older adults: large cohorts report onset around 67 years and diagnosis around 68 years, with mean/median patient ages near 70–76. Women are modestly overrepresented; one cohort reported a male:female ratio of 0.56. Incidence and prevalence are higher in colder climates, but complement-mediated hemolysis persists throughout the year. (berentsen2007primarychroniccold pages 1-2, berentsen2022coldagglutinindisease pages 6-8, berentsen2020coldagglutinindiseasea pages 3-4)

Cold exposure does not create the clone, but promotes antibody binding and agglutination. Febrile infection, inflammation, surgery, and major trauma can amplify complement availability and trigger acute hemolytic exacerbation. Such exacerbations occur in approximately 40–74% depending on ascertainment. (berentsen2024theimpactof pages 6-7, berentsen2022coldagglutinindisease pages 6-8)

**CAS triggers**, rather than causes of primary CAD, include *Mycoplasma pneumoniae*, Epstein–Barr virus, SARS-CoV-2, and overt B-cell lymphoma. (berentsen2019coldagglutinindisease pages 1-2, berentsen2022coldagglutinindisease pages 1-2)

### Protective factors and gene–environment interaction

No replicated germline protective allele, diet, smoking pattern, occupational exposure, or pharmacogenomic predictor is established. Avoiding cold reduces agglutination-mediated symptoms and may reduce individual crises, but does not eliminate year-round complement hemolysis. The principal demonstrated gene–environment interaction is functional: somatically generated, broad-thermal-amplitude IgM becomes pathogenic when cooler peripheral temperatures permit I-antigen binding; inflammation then increases complement-mediated destruction. (berentsen2022coldagglutinindisease pages 6-8, berentsen2018howimanage pages 1-2)

## 3. Phenotypes

- **Hemolysis/anemia:** present by definition; anemia occurs in approximately 88–90%, while 10–12% have compensated hemolysis. In the 232-patient cohort, mean Hb was 9.3 g/dL and 27% had Hb <8 g/dL. Suggested HPO: **Hemolytic anemia (HP:0001878), Anemia (HP:0001903), Reticulocytosis (HP:0001923), Hyperbilirubinemia (HP:0002904), Reduced haptoglobin**. Severity is variable and fluctuating. (berentsen2022coldagglutinindisease pages 6-8, berentsen2024theimpactof pages 4-6, berentsen2020coldagglutinindiseasea pages 3-4)
- **Fatigue:** reported by 90% in a selected 50-patient survey; 29% of fatigued respondents described constant daily fatigue. Suggested HPO: **Fatigue (HP:0012378)**. Fatigue impairs physical, social, emotional, and financial functioning. (berentsen2024theimpactof pages 6-7)
- **Acrocyanosis/Raynaud-like episodes:** cold-induced circulatory symptoms occur in 57–91%. Acrocyanosis is common; disabling Raynaud-like symptoms are less frequent, livedo uncommon, and ulceration/gangrene rare. Suggested HPO: **Acrocyanosis (HP:0001063), Raynaud phenomenon (HP:0030880), Livedo reticularis, Digital ulceration, Gangrene**. They are episodic, peripheral, non-complement-mediated, and may independently warrant therapy. (berentsen2007primarychroniccold pages 2-4, berentsen2024theimpactof pages 6-7)
- **Transfusion requirement:** 40–50% have received transfusion at some point. Suggested HPO: severe anemia rather than a separate phenotype. (berentsen2022coldagglutinindisease pages 6-8)
- **Jaundice/dark urine:** downstream manifestations of hemolysis; suggested HPO: **Jaundice (HP:0000952), Hemoglobinuria (HP:0003641)**.
- **Thrombosis:** overall relative risk is estimated at two- to threefold. In Denmark, 1-year thromboembolism was 7.2% versus 1.9% in matched controls; 5-year risk was 11.5% versus 7.8%. Suggested HPO: **Venous thromboembolism (HP:0004936)**. (berentsen2024theimpactof pages 6-7, berentsen2020coldagglutinindiseasea pages 10-11)
- **Mental-health/QoL burden:** claims-linked data found elevated medically attended anxiety/depression; fatigue and temperature avoidance restrict mobility, work, and social activities.

Leukopenia and thrombocytopenia are unusual and should prompt another diagnosis, marrow suppression, hypersplenism, or treatment toxicity. (berentsen2024theimpactof pages 4-6)

## 4. Genetic and molecular information

CAD has **no established germline causal gene, Mendelian inheritance, carrier frequency, penetrance, anticipation, founder mutation, or role for reproductive testing**.

The acquired clone shows:

- **IGHV4-34** usage in >80–85%; IGKV3-20 in roughly 59–74% and IGKV3-15 in approximately 15%.
- **KMT2D:** approximately 67–69%, generally loss-of-function.
- **CARD11:** approximately 31–33%, predicted gain-of-function/B-cell-receptor–NF-κB signaling activation.
- **CXCR4:** 22% coding or up to 28% including noncoding lesions; C-terminal frameshifts may prolong signaling.
- **IGLL5:** 44% coding or 61% including noncoding alterations.
- **MYD88 L265P:** usually absent, helping distinguish CAD-associated LPD from Waldenström macroglobulinemia.
- **Cytogenetics:** gain/trisomy 3 is nearly universal in small studied series; additional gain of chromosome 12 or 18 occurs frequently. These are somatic clone-level abnormalities, not constitutional aneuploidies. (berentsen2024theimpactof pages 3-4, berentsen2020newinsightsin pages 2-3, berentsen2022coldagglutinindisease pages 4-6, małecka2021themutationallandscape pages 1-3)

Population allele frequencies and ACMG germline classifications are therefore **not applicable**. No validated modifier gene or epigenetic biomarker is established, although KMT2D itself is an epigenetic regulator.

A 2024 human RNA-seq study of clonal B cells from 12 patients versus IgM-memory B cells from four controls found 93 differentially expressed genes and approximately **11-fold downregulation of CR1/CD35**, confirmed at protein level. Because CR1 negatively regulates B-cell activation/differentiation, the authors infer that reduced CR1 may promote clonal activation and antibody production; this is mechanistically plausible but not yet a clinical biomarker. (małecka2024geneexpressionanalysis pages 1-1)

## 5. Environmental and infectious information

No toxin, radiation, pollution, diet, alcohol, smoking, or occupational exposure has been shown to cause primary CAD. Temperature is a symptom modifier. Infection and inflammatory acute-phase responses can exacerbate established CAD, whereas *M. pneumoniae*, EBV, and occasionally other infections can cause secondary CAS. There is no zoonotic transmission.

Practical environmental management includes layered warm clothing, gloves, heated indoor environments, avoiding cold infusions, and maintaining body temperature during anesthesia or surgery. These measures are low-risk but supported mainly by physiology and expert practice rather than randomized prevention trials.

## 6. Mechanism/pathophysiology

### Ordered causal chain

1. **Acquired somatic alterations and restricted immunoglobulin selection lead to** expansion of a marrow IGHV4-34-positive mature B-cell/plasma-cell clone.
2. **Clonal differentiation leads to** secretion of monoclonal, usually IgMκ, cold agglutinin against erythrocyte I antigen.
3. **Cooling in acral circulation leads to** pentameric IgM binding and cross-linking of erythrocytes.
4. **Cross-linking leads to** reversible erythrocyte agglutination and impaired capillary flow, resulting in acrocyanosis and Raynaud-like ischemic symptoms.
5. **Antigen-bound IgM leads to** C1q binding and activation of C1r/C1s, then cleavage of C4 and C2 and formation of classical-pathway C3 convertase.
6. **C3 convertase leads to** C3b deposition on erythrocytes; IgM usually dissociates on central rewarming, but C3 fragments remain.
7. **C3b opsonization leads to** recognition and predominantly extravascular clearance by hepatic Kupffer cells, resulting in anemia, jaundice, reticulocytosis, elevated bilirubin/LDH, and reduced haptoglobin.
8. **When activation proceeds to C5 and membrane-attack complex, it leads to** a smaller intravascular-hemolysis branch with hemoglobinemia/hemoglobinuria.
9. **Hemolysis and complement-derived inflammatory signals lead to** fatigue, endothelial/coagulation activation, and increased thrombotic risk; parts of the thrombosis pathway remain inferred rather than fully demonstrated in CAD.
10. **Infection, surgery, trauma, or cold exposure lead to** episodic amplification of steps 3–9. (berentsen2019coldagglutinindisease pages 1-2, berentsen2020coldagglutinindisease pages 1-2, berentsen2020newinsightsin pages 2-3, berentsen2022coldagglutinindisease pages 4-6)

**Upstream:** marrow clone, B-cell receptor/NF-κB and CXCR4 signaling, antibody production. **Downstream:** agglutination, complement activation, macrophage clearance, anemia, ischemia, fatigue, and thrombosis.

Suggested ontologies: **GO:0006956 complement activation; GO:0006958 classical complement activation; GO:0002455 humoral immune response mediated by circulating immunoglobulin; GO:0042113 B-cell activation; GO:0030218 erythrocyte differentiation; GO:0006911 phagocytosis/engulfment.** Cell types: **CL:0000236 B cell; CL:0000787 memory B cell; CL:0000786 plasma cell; CL:0000232 erythrocyte; CL:0000860 classical monocyte/macrophage; CL:0000091 Kupffer cell.**

## 7. Anatomical structures affected

- **Primary site:** bone marrow (**UBERON:0002371**), containing the pathogenic B-cell/plasma-cell clone.
- **Direct target:** circulating erythrocytes in blood (**UBERON:0000178**).
- **Peripheral circulation:** fingers, toes, ears, nose, and acral skin; manifestations are generally bilateral and temperature-dependent rather than fixed to one side.
- **Major clearance organ:** liver (**UBERON:0002107**), particularly Kupffer cells/sinusoidal reticuloendothelial tissue.
- **Secondary involvement:** cardiovascular/venous systems through thrombosis; kidney injury can occur in unusually severe intravascular hemolysis but is not a defining organ lesion.
- **Subcellular compartments:** erythrocyte plasma membrane and extracellular complement cascade; no primary nuclear, mitochondrial, lysosomal, or ER defect is established.

Marrow histology shows small intertrabecular nodular or sparse interstitial B-cell infiltrates with surrounding/dispersed clonally related plasma cells and absence of the fibrosis, paratrabecular pattern, and mast-cell enrichment typical of lymphoplasmacytic lymphoma. Cells commonly express CD19, CD20, CD22, PAX5, CD79a/b, IgM, and monotypic κ; CD5 occurs in about 40%, whereas BCL6, MUM1, CD23, and cyclin D1 are usually negative. (berentsen2024theimpactof pages 3-4, berentsen2020newinsightsin pages 2-3, berentsen2022coldagglutinindisease pages 2-4)

## 8. Temporal development

Onset is usually insidious in late adulthood; pediatric and young-adult primary CAD is exceptionally rare. The course is chronic, fluctuating, and often lifelong rather than staged. Hemolysis persists year-round, with superimposed cold- or inflammation-associated exacerbations. In an older population cohort, disease was broadly non-progressive over a median five years, although individual Hb values fluctuated substantially. (berentsen2007primarychroniccold pages 1-2, berentsen2022coldagglutinindisease pages 6-8)

Spontaneous durable remission is uncommon. Clone-directed therapy can produce multi-year treatment-free remission, whereas complement inhibition controls downstream hemolysis only while treatment continues. Following sutimlimab withdrawal, complement activity and hemolytic markers approach baseline. (roth2024longtermefficacyand pages 1-2, berentsen2020coldagglutinindiseasea pages 4-5)

## 9. Inheritance and population epidemiology

CAD is acquired and non-hereditary. Family history, consanguinity, mosaicism, anticipation, carrier state, and prenatal testing are not applicable.

The 232-patient multinational study found a fourfold climatic gradient: prevalence **20 versus 5 per million** and incidence **1.9 versus 0.48 per million/year** in colder versus warmer regions. Earlier Northern European estimates were prevalence 16 per million and incidence 1 per million/year. A Danish registry estimated 2013 prevalence 1.26/100,000 and incidence 0.18/100,000/year. Differences reflect geography, age structure, ascertainment, and coding. (berentsen2019coldagglutinindisease pages 1-2, berentsen2020coldagglutinindiseasea pages 3-4, berentsen2020coldagglutinindiseasea pages 10-11)

No reproducible ethnic susceptibility or geographic variant distribution is established. Most data come from European, North American, and Japanese cohorts, leaving ancestry-related ascertainment gaps.

## 10. Diagnostics

### Core diagnostic framework

Confirmed CAD requires:

1. chronic biochemical/clinical hemolysis;
2. direct antiglobulin test strongly positive for **C3d**, usually negative or weak for IgG;
3. cold-agglutinin titer at 4°C generally **≥1:64**—the 232-patient study used >64; and
4. no relevant secondary infection, autoimmune disorder, active cancer, or overt lymphoma. (berentsen2020coldagglutinindiseasea pages 6-7)

A lower titer does not absolutely exclude CAD when there is acrocyanosis, IgMκ gammopathy, characteristic marrow pathology, and expert consensus. Thermal amplitude is often more clinically informative than titer. (berentsen2020coldagglutinindiseasea pages 6-7, berentsen2018howimanage pages 1-2)

### Recommended workup

- CBC and smear; spurious macrocytosis, low erythrocyte count, and high MCHC may result from in-vitro agglutination.
- Reticulocytes, bilirubin fractions, LDH, haptoglobin, urinalysis.
- Polyspecific then monospecific DAT for C3d and IgG.
- Cold-agglutinin titer and, where needed, thermal amplitude.
- Serum protein electrophoresis/immunofixation, quantitative immunoglobulins, free light chains.
- Bone-marrow aspirate/biopsy with immunohistochemistry and flow cytometry; expert review materially increases detection.
- MYD88 L265P testing when distinction from LPL/WM is difficult; broader somatic sequencing is investigational rather than mandatory.
- Directed infection/lymphoma/autoimmune evaluation based on presentation.

Blood for cold-agglutinin titer, immunoglobulin studies, and CBC should be maintained near 37°C until serum/plasma separation or analysis to prevent antibody adsorption and artifactual cell clumping.

### Differential diagnosis

Major alternatives are warm AIHA, mixed AIHA, paroxysmal cold hemoglobinuria, secondary CAS, cryoglobulinemia, Waldenström macroglobulinemia/LPL, other B-cell lymphomas, paroxysmal nocturnal hemoglobinuria, hereditary/acquired nonimmune hemolysis, and transfusion reactions. C3d-only DAT plus high-titer broad-thermal-amplitude IgM supports CAD; IgG-predominant DAT supports warm AIHA; Donath–Landsteiner antibody supports paroxysmal cold hemoglobinuria.

No population, newborn, cascade, carrier, WES, WGS, CMA, karyotype, mitochondrial, or repeat-expansion screening is recommended. RNA-seq and CR1 measurement remain research tools.

## 11. Outcome and prognosis

In the 232-patient cohort, 72/232 (31%) died during follow-up, but only 8 deaths (3.5% of the cohort) were attributed to CAD/complications. Estimated median survival was 16 years and 5-year survival 83%; DLBCL transformation occurred in 8 patients, approximately 3.4% over eight years. Potentially organ-damaging iron overload occurred in about one-fifth, especially after transfusion. (berentsen2020coldagglutinindiseasea pages 10-11, berentsen2020coldagglutinindiseasea pages 8-9)

Registry estimates are less favorable: Danish patients had median survival 8.5 years, adjusted mortality HR 1.84, and 1- and 5-year mortality of 17% and 39% versus 3% and 18% in controls. These differences likely reflect older age, coding/selection, comorbidity, and inclusion uncertainty. (berentsen2020coldagglutinindiseasea pages 10-11)

Poorer functional outcome is associated with severe anemia, recurrent transfusion, persistent hemolysis, infections, thrombosis, and comorbid frailty. No validated molecular prognostic score exists; CARD11/CXCR4 mutations correlate with lower Hb but are not established clinical decision biomarkers. (małecka2021themutationallandscape pages 1-3)

## 12. Treatment and current applications

### Treatment strategy

Observation plus thermal protection is appropriate for compensated, minimally symptomatic disease. Treat symptomatic anemia, transfusion dependence, disabling fatigue, significant hemolysis, or disabling circulatory symptoms. Choice should reflect phenotype:

- **Hemolysis/fatigue predominant:** rapid classical-complement inhibition is attractive.
- **Prominent acrocyanosis/Raynaud-like symptoms:** clone-directed therapy is preferred because complement blockade does not remove IgM or prevent agglutination.
- **Fit patient seeking durable treatment-free remission:** rituximab–bendamustine.
- **Frail patient:** rituximab monotherapy or sutimlimab according to urgency, access, and phenotype. (berentsen2024theimpactof pages 11-12, berentsen2020coldagglutinindiseasea pages 12-13)

### Pharmacotherapy

**Sutimlimab (anti-C1s monoclonal antibody; NCIT concept: monoclonal antibody/complement C1s inhibitor).** It blocks classical-pathway activation without eradicating the clone. In CARDINAL, 13/24 (54%; 95% CI 33–74) reached the composite response; Hb rose 1.2 g/dL by week 1 and 2.3 g/dL by week 3, and bilirubin normalized by week 3. FACIT-Fatigue improved rapidly. In CADENZA, 16/22 (72.7%) responded versus 3/20 (15%) on placebo, with median Hb increase 2.7 g/dL. (berentsen2022coldagglutinindisease pages 11-13, costa2025beneaththesurface pages 15-15, weitz2023sutimlimabforthe pages 3-5)

At 2024 CADENZA Part B follow-up, 32/39 completed treatment; median exposure was 99 weeks, mean on-treatment Hb remained ≥11.0 g/dL versus 9.3 baseline, and bilirubin ≤20 μmol/L versus 35 baseline. Benefits reversed after washout. No meningococcal infection or lupus was observed. A seven-patient Japanese extension reported median cumulative exposure of 3.8 years without a new safety signal; Hb and bilirubin worsened after withdrawal and recovered with retreatment. (roth2024longtermefficacyand pages 1-2)

Vaccination against encapsulated bacteria—particularly meningococcus, pneumococcus, and *Haemophilus influenzae* type b—is required before complement inhibition where feasible; urgent treatment may require bridging antibiotic prophylaxis. Sutimlimab does **not** reliably improve cold-induced circulatory symptoms. (berentsen2024theimpactof pages 11-12, roth2025[coldagglutinindisease pages 10-11)

**Rituximab–bendamustine (NCIT: rituximab; bendamustine; chemoimmunotherapy).** Long-term observational follow-up found 35/45 responses (78%), 24 complete responses (53%), and estimated 77% sustained remission at five years; median response duration was not reached at 88 months. Response can take months. Myelosuppression/infection make it less suitable for frail patients. (berentsen2020coldagglutinindiseasea pages 4-5, berentsen2020coldagglutinindiseasea pages 3-4)

**Rituximab monotherapy.** Approximately 45–60% respond, usually partially; median response duration is around 11–12 months. It is less toxic but slower and less durable. Corticosteroids are frequently used in practice but generally ineffective and should not be routine CAD therapy. (peters2020coldagglutinindisease pages 1-2, berentsen2020coldagglutinindiseasea pages 4-5, rossi2018shortcourseof pages 2-2)

**Other/selected approaches.** Rituximab–fludarabine is effective but has greater late toxicity. A short bortezomib course produced approximately 32% overall and 16% complete response in relapsed disease. Eculizumab reduced LDH from 572 to 334 U/L and raised Hb only from 9.35 to 10.15 g/dL, consistent with incomplete control when C3-mediated hepatic clearance persists. (rossi2018shortcourseof pages 2-2, costa2025beneaththesurface pages 15-16)

### Supportive and interventional care

Use warmed blood and an in-line blood warmer for transfusion; keep the patient and infusion limb warm. Folate supplementation is reasonable during active hemolysis. Treat infection promptly and maintain hydration during crises. Routine splenectomy is not recommended because clearance is predominantly hepatic. Routine indefinite anticoagulation is unsupported, but standard prophylaxis is appropriate during hospitalization, surgery, severe acute hemolysis, or additional thrombotic risk. (roth2025[coldagglutinindisease pages 10-11, berentsen2020coldagglutinindiseasea pages 10-11)

### Experimental/real-world developments

- **Pegcetacoplan, C3 inhibitor:** phase 3 NCT05096403 completed with 24 participants; randomized Part A ended in 2024. It addresses more proximal C3-mediated clearance but is not approved for CAD based on the evidence reviewed here. (NCT05096403 chunk 1)
- **Iptacopan, factor-B inhibitor:** studied in a phase 2 basket trial, NCT05086744, which was terminated; it remains investigational for CAD.
- **Riliprubart, long-acting anti-C1s:** early clinical testing showed rapid hematologic activity; confirmatory evidence is pending. (costa2025beneaththesurface pages 15-16)
- Other proposed clone-directed agents include BTK/SYK/PI3K inhibitors, daratumumab, and VH4-34-directed therapy; evidence remains early or case-based.

Implementation is constrained by cost and access: a 2024 expert review estimated US sutimlimab cost above $260,000 per year and noted limited reimbursement outside the United States, EU, and Japan. (berentsen2024theimpactof pages 11-12)

## 13. Prevention

There is no known primary prevention because the initiating clone is sporadic and acquired. There is no population or genetic screening program.

**Secondary prevention** consists of recognizing unexplained C3-positive hemolysis early, distinguishing CAD from warm AIHA/CAS, and avoiding ineffective prolonged corticosteroid exposure. **Tertiary prevention** includes thermal protection, warmed transfusions/infusions, infection treatment, vaccination before complement blockade, perioperative warming, iron-overload monitoring in transfused patients, and context-specific thromboprophylaxis. No vaccine prevents primary CAD; vaccination is used to reduce treatment-associated encapsulated-bacterial risk.

## 14. Other species and natural disease

Cold-reactive antibodies and immune-mediated hemolytic anemia occur naturally in veterinary medicine, particularly in dogs and occasionally horses/cats, often secondary to infection or immune disease. However, the reviewed literature does not establish a naturally occurring animal disorder that faithfully reproduces the human **IGHV4-34-restricted CAD-associated marrow clone**. No breed-specific VBO annotation, orthologous causal gene, cross-species transmission, or zoonotic potential should be assigned to human CAD.

## 15. Model organisms and advanced technologies

No validated mouse, rat, zebrafish, invertebrate, knockout, or knock-in model recapitulates the complete human disease. Current mechanistic systems are principally:

- patient serum/IgM incubated with human erythrocytes for temperature-dependent agglutination and complement assays;
- patient marrow biopsy, flow cytometry, and sorted clonal B cells;
- human genomic and bulk RNA-seq studies;
- pharmacodynamic classical-complement assays used in C1s-inhibitor development.

These systems model antibody binding and complement injury well but cannot fully reproduce chronic human clonal evolution, fatigue, thrombosis, or acral microcirculation. The 2024 CR1 study is bulk RNA-seq in a very small cohort, not single-cell or spatial transcriptomics. No clinically validated CAD proteomic, metabolomic, lipidomic, epigenomic, organoid, CRISPR-screen, liquid-biopsy, or multi-omics diagnostic signature is available. (małecka2024geneexpressionanalysis pages 1-1, małecka2021themutationallandscape pages 1-3)

## Evidence appraisal and knowledge gaps

The best clinical evidence includes a 232-patient multinational cohort, national registries, and phase 3 sutimlimab trials. Limitations include rarity, older and predominantly European/North American populations, inconsistent historical separation of CAD from CAS, small genomic cohorts, and limited head-to-head therapy comparisons. Major open questions are optimal sequencing of clone- versus complement-directed treatment, duration and cost-effectiveness of chronic C1s blockade, management of combined hemolytic/circulatory phenotypes, biomarkers of transformation and thrombosis, and whether CR1 downregulation is causal or merely associated.

Open Targets independently links **C1S** to MONDO:0018922 through approved and phase 3 clinical evidence, supporting C1s as a therapeutically validated target rather than a germline causal gene. (OpenTargets Search: cold agglutinin disease)

### Selected exact abstract quotations

- **Disease biology:** “Primary cold agglutinin disease is caused by a unique indolent B-cell lymphoproliferative disorder of the bone marrow.” (Małecka et al., 2021; DOI: https://doi.org/10.1002/ajh.26205). (małecka2021themutationallandscape pages 1-3)
- **Clinical burden:** “Cold-induced circulatory symptoms are reported in 57–91%” in the 2024 phenotype synthesis; anemia affects approximately 90%. (DOI: https://doi.org/10.1080/17474086.2024.2372333). (berentsen2024theimpactof pages 6-7)
- **Recent molecular development:** CR1/CD35 “was downregulated 11-fold in clonal CAD B cells compared to control B cells.” (Małecka et al., December 2024; DOI: https://doi.org/10.1093/cei/uxad135). (małecka2024geneexpressionanalysis pages 1-1)
- **Long-term treatment:** the 2024 CADENZA extension found that improvements in “haemolysis, anaemia, and quality of life were sustained,” but markers returned toward baseline after cessation. (DOI: https://doi.org/10.1016/j.eclinm.2024.102733). (roth2024longtermefficacyand pages 1-2)

References

1. (berentsen2019coldagglutinindisease pages 1-2): Sigbjørn Berentsen, Alexander Röth, Ulla Randen, Bernd Jilma, and Geir E Tjønnfjord. Cold agglutinin disease: current challenges and future prospects. Journal of Blood Medicine, 10:93-103, Apr 2019. URL: https://doi.org/10.2147/jbm.s177621, doi:10.2147/jbm.s177621. This article has 109 citations.

2. (berentsen2022coldagglutinindisease pages 1-2): Sigbjørn Berentsen, Shirley D’Sa, Ulla Randen, Agnieszka Małecka, and Josephine M. I. Vos. Cold agglutinin disease: improved understanding of pathogenesis helps define targets for therapy. Hemato, 3:574-594, Sep 2022. URL: https://doi.org/10.3390/hemato3040040, doi:10.3390/hemato3040040. This article has 34 citations.

3. (berentsen2020newinsightsin pages 2-3): Sigbjørn Berentsen. New insights in the pathogenesis and therapy of cold agglutinin-mediated autoimmune hemolytic anemia. Frontiers in Immunology, Apr 2020. URL: https://doi.org/10.3389/fimmu.2020.00590, doi:10.3389/fimmu.2020.00590. This article has 206 citations and is from a peer-reviewed journal.

4. (roth2024longtermefficacyand pages 1-2): Alexander Röth, Sigbjørn Berentsen, Wilma Barcellini, Shirley D’Sa, Bernd Jilma, Marc Michel, Ilene C. Weitz, Masaki Yamaguchi, Jun-ichi Nishimura, Josephine M.I. Vos, Joan Cid, Michael Storek, Nancy Wong, Ronnie Yoo, Deepthi Jayawardene, Shruti Srivastava, Marek Wardęcki, Frank Shafer, Michelle Lee, and Catherine M. Broome. Long-term efficacy and safety of continued complement c1s inhibition with sutimlimab in cold agglutinin disease: cadenza study part b. Aug 2024. URL: https://doi.org/10.1016/j.eclinm.2024.102733, doi:10.1016/j.eclinm.2024.102733. This article has 11 citations and is from a peer-reviewed journal.

5. (berentsen2024theimpactof pages 11-12): Sigbjørn Berentsen, Josephine M.I. Vos, Agnieszka Malecka, Geir E. Tjønnfjord, and Shirley D’Sa. The impact of individual clinical features in cold agglutinin disease: hemolytic versus non-hemolytic symptoms. Expert Review of Hematology, 17:479-492, Jun 2024. URL: https://doi.org/10.1080/17474086.2024.2372333, doi:10.1080/17474086.2024.2372333. This article has 5 citations and is from a peer-reviewed journal.

6. (berentsen2024theimpactof pages 3-4): Sigbjørn Berentsen, Josephine M.I. Vos, Agnieszka Malecka, Geir E. Tjønnfjord, and Shirley D’Sa. The impact of individual clinical features in cold agglutinin disease: hemolytic versus non-hemolytic symptoms. Expert Review of Hematology, 17:479-492, Jun 2024. URL: https://doi.org/10.1080/17474086.2024.2372333, doi:10.1080/17474086.2024.2372333. This article has 5 citations and is from a peer-reviewed journal.

7. (berentsen2020coldagglutinindiseasea pages 3-4): Sigbjørn Berentsen, Wilma Barcellini, Shirley D’Sa, Ulla Randen, Tor Henrik Anderson Tvedt, Bruno Fattizzo, Einar Haukås, Megan Kell, Robert Brudevold, Anders E. A. Dahm, Jakob Dalgaard, Hege Frøen, Randi Fykse Hallstensen, Pernille H. Jæger, Henrik Hjorth-Hansen, Agnieszka Małecka, Markku Oksman, Jürgen Rolke, Mallika Sekhar, Jon Hjalmar Sørbø, Eirik Tjønnfjord, Galina Tsykunova, and Geir E. Tjønnfjord. Cold agglutinin disease revisited: a multinational, observational study of 232 patients. Jul 2020. URL: https://doi.org/10.1182/blood.2020005674, doi:10.1182/blood.2020005674. This article has 229 citations and is from a highest quality peer-reviewed journal.

8. (berentsen2024theimpactof pages 6-7): Sigbjørn Berentsen, Josephine M.I. Vos, Agnieszka Malecka, Geir E. Tjønnfjord, and Shirley D’Sa. The impact of individual clinical features in cold agglutinin disease: hemolytic versus non-hemolytic symptoms. Expert Review of Hematology, 17:479-492, Jun 2024. URL: https://doi.org/10.1080/17474086.2024.2372333, doi:10.1080/17474086.2024.2372333. This article has 5 citations and is from a peer-reviewed journal.

9. (berentsen2020coldagglutinindiseasea pages 10-11): Sigbjørn Berentsen, Wilma Barcellini, Shirley D’Sa, Ulla Randen, Tor Henrik Anderson Tvedt, Bruno Fattizzo, Einar Haukås, Megan Kell, Robert Brudevold, Anders E. A. Dahm, Jakob Dalgaard, Hege Frøen, Randi Fykse Hallstensen, Pernille H. Jæger, Henrik Hjorth-Hansen, Agnieszka Małecka, Markku Oksman, Jürgen Rolke, Mallika Sekhar, Jon Hjalmar Sørbø, Eirik Tjønnfjord, Galina Tsykunova, and Geir E. Tjønnfjord. Cold agglutinin disease revisited: a multinational, observational study of 232 patients. Jul 2020. URL: https://doi.org/10.1182/blood.2020005674, doi:10.1182/blood.2020005674. This article has 229 citations and is from a highest quality peer-reviewed journal.

10. (małecka2021themutationallandscape pages 1-3): Agnieszka Małecka, Gunhild Trøen, Jan Delabie, Jędrzej Małecki, Ingunn Østlie, Anne Tierens, Ulla Randen, Sigbjørn Berentsen, and Geir E. Tjønnfjord. The mutational landscape of cold agglutinin disease: <scp><i>card11</i></scp> and <scp><i>cxcr4</i></scp> mutations are correlated with lower hemoglobin levels. May 2021. URL: https://doi.org/10.1002/ajh.26205, doi:10.1002/ajh.26205. This article has 18 citations and is from a domain leading peer-reviewed journal.

11. (małecka2024geneexpressionanalysis pages 1-1): Agnieszka Małecka, Ingunn Østlie, Gunhild Trøen, Jędrzej Małecki, Jan Delabie, Anne Tierens, Ludvig A Munthe, Sigbjørn Berentsen, and Geir E Tjønnfjord. Gene expression analysis revealed downregulation of complement receptor 1 in clonal b cells in cold agglutinin disease. Clinical and Experimental Immunology, 216:45-54, Dec 2024. URL: https://doi.org/10.1093/cei/uxad135, doi:10.1093/cei/uxad135. This article has 11 citations and is from a peer-reviewed journal.

12. (berentsen2020coldagglutinindiseasea pages 6-7): Sigbjørn Berentsen, Wilma Barcellini, Shirley D’Sa, Ulla Randen, Tor Henrik Anderson Tvedt, Bruno Fattizzo, Einar Haukås, Megan Kell, Robert Brudevold, Anders E. A. Dahm, Jakob Dalgaard, Hege Frøen, Randi Fykse Hallstensen, Pernille H. Jæger, Henrik Hjorth-Hansen, Agnieszka Małecka, Markku Oksman, Jürgen Rolke, Mallika Sekhar, Jon Hjalmar Sørbø, Eirik Tjønnfjord, Galina Tsykunova, and Geir E. Tjønnfjord. Cold agglutinin disease revisited: a multinational, observational study of 232 patients. Jul 2020. URL: https://doi.org/10.1182/blood.2020005674, doi:10.1182/blood.2020005674. This article has 229 citations and is from a highest quality peer-reviewed journal.

13. (berentsen2020coldagglutinindiseasea pages 4-5): Sigbjørn Berentsen, Wilma Barcellini, Shirley D’Sa, Ulla Randen, Tor Henrik Anderson Tvedt, Bruno Fattizzo, Einar Haukås, Megan Kell, Robert Brudevold, Anders E. A. Dahm, Jakob Dalgaard, Hege Frøen, Randi Fykse Hallstensen, Pernille H. Jæger, Henrik Hjorth-Hansen, Agnieszka Małecka, Markku Oksman, Jürgen Rolke, Mallika Sekhar, Jon Hjalmar Sørbø, Eirik Tjønnfjord, Galina Tsykunova, and Geir E. Tjønnfjord. Cold agglutinin disease revisited: a multinational, observational study of 232 patients. Jul 2020. URL: https://doi.org/10.1182/blood.2020005674, doi:10.1182/blood.2020005674. This article has 229 citations and is from a highest quality peer-reviewed journal.

14. (weitz2023sutimlimabforthe pages 3-5): Ilene Weitz. Sutimlimab for the treatment of cold agglutinin disease. Oncology &amp; Haematology, 19:35, Jan 2023. URL: https://doi.org/10.17925/ohr.2023.19.1.35, doi:10.17925/ohr.2023.19.1.35. This article has 0 citations.

15. (costa2025beneaththesurface pages 15-15): Alessandro Costa, Olga Mulas, Angela Maria Mereu, Mercede Schintu, Marianna Greco, and Giovanni Caocci. Beneath the surface in autoimmune hemolytic anemia: pathogenetic networks, therapeutic advancements and open questions. Frontiers in Immunology, Jul 2025. URL: https://doi.org/10.3389/fimmu.2025.1624667, doi:10.3389/fimmu.2025.1624667. This article has 8 citations and is from a peer-reviewed journal.

16. (berentsen2022coldagglutinindisease pages 2-4): Sigbjørn Berentsen, Shirley D’Sa, Ulla Randen, Agnieszka Małecka, and Josephine M. I. Vos. Cold agglutinin disease: improved understanding of pathogenesis helps define targets for therapy. Hemato, 3:574-594, Sep 2022. URL: https://doi.org/10.3390/hemato3040040, doi:10.3390/hemato3040040. This article has 34 citations.

17. (berentsen2007primarychroniccold pages 1-2): Sigbjørn Berentsen, Klaus Beiske, and Geir E. Tjønnfjord. Primary chronic cold agglutinin disease: an update on pathogenesis, clinical features and therapy. Oct 2007. URL: https://doi.org/10.1080/10245330701445392, doi:10.1080/10245330701445392. This article has 166 citations and is from a peer-reviewed journal.

18. (berentsen2022coldagglutinindisease pages 6-8): Sigbjørn Berentsen, Shirley D’Sa, Ulla Randen, Agnieszka Małecka, and Josephine M. I. Vos. Cold agglutinin disease: improved understanding of pathogenesis helps define targets for therapy. Hemato, 3:574-594, Sep 2022. URL: https://doi.org/10.3390/hemato3040040, doi:10.3390/hemato3040040. This article has 34 citations.

19. (berentsen2018howimanage pages 1-2): Sigbjørn Berentsen. How i manage patients with cold agglutinin disease. British Journal of Haematology, 181:320-330, May 2018. URL: https://doi.org/10.1111/bjh.15109, doi:10.1111/bjh.15109. This article has 167 citations and is from a domain leading peer-reviewed journal.

20. (berentsen2024theimpactof pages 4-6): Sigbjørn Berentsen, Josephine M.I. Vos, Agnieszka Malecka, Geir E. Tjønnfjord, and Shirley D’Sa. The impact of individual clinical features in cold agglutinin disease: hemolytic versus non-hemolytic symptoms. Expert Review of Hematology, 17:479-492, Jun 2024. URL: https://doi.org/10.1080/17474086.2024.2372333, doi:10.1080/17474086.2024.2372333. This article has 5 citations and is from a peer-reviewed journal.

21. (berentsen2007primarychroniccold pages 2-4): Sigbjørn Berentsen, Klaus Beiske, and Geir E. Tjønnfjord. Primary chronic cold agglutinin disease: an update on pathogenesis, clinical features and therapy. Oct 2007. URL: https://doi.org/10.1080/10245330701445392, doi:10.1080/10245330701445392. This article has 166 citations and is from a peer-reviewed journal.

22. (berentsen2022coldagglutinindisease pages 4-6): Sigbjørn Berentsen, Shirley D’Sa, Ulla Randen, Agnieszka Małecka, and Josephine M. I. Vos. Cold agglutinin disease: improved understanding of pathogenesis helps define targets for therapy. Hemato, 3:574-594, Sep 2022. URL: https://doi.org/10.3390/hemato3040040, doi:10.3390/hemato3040040. This article has 34 citations.

23. (berentsen2020coldagglutinindisease pages 1-2): S Berentsen and A Małecka. Cold agglutinin disease: where do we stand, and where are we going? Unknown journal, 2020.

24. (berentsen2020coldagglutinindiseasea pages 8-9): Sigbjørn Berentsen, Wilma Barcellini, Shirley D’Sa, Ulla Randen, Tor Henrik Anderson Tvedt, Bruno Fattizzo, Einar Haukås, Megan Kell, Robert Brudevold, Anders E. A. Dahm, Jakob Dalgaard, Hege Frøen, Randi Fykse Hallstensen, Pernille H. Jæger, Henrik Hjorth-Hansen, Agnieszka Małecka, Markku Oksman, Jürgen Rolke, Mallika Sekhar, Jon Hjalmar Sørbø, Eirik Tjønnfjord, Galina Tsykunova, and Geir E. Tjønnfjord. Cold agglutinin disease revisited: a multinational, observational study of 232 patients. Jul 2020. URL: https://doi.org/10.1182/blood.2020005674, doi:10.1182/blood.2020005674. This article has 229 citations and is from a highest quality peer-reviewed journal.

25. (berentsen2020coldagglutinindiseasea pages 12-13): Sigbjørn Berentsen, Wilma Barcellini, Shirley D’Sa, Ulla Randen, Tor Henrik Anderson Tvedt, Bruno Fattizzo, Einar Haukås, Megan Kell, Robert Brudevold, Anders E. A. Dahm, Jakob Dalgaard, Hege Frøen, Randi Fykse Hallstensen, Pernille H. Jæger, Henrik Hjorth-Hansen, Agnieszka Małecka, Markku Oksman, Jürgen Rolke, Mallika Sekhar, Jon Hjalmar Sørbø, Eirik Tjønnfjord, Galina Tsykunova, and Geir E. Tjønnfjord. Cold agglutinin disease revisited: a multinational, observational study of 232 patients. Jul 2020. URL: https://doi.org/10.1182/blood.2020005674, doi:10.1182/blood.2020005674. This article has 229 citations and is from a highest quality peer-reviewed journal.

26. (berentsen2022coldagglutinindisease pages 11-13): Sigbjørn Berentsen, Shirley D’Sa, Ulla Randen, Agnieszka Małecka, and Josephine M. I. Vos. Cold agglutinin disease: improved understanding of pathogenesis helps define targets for therapy. Hemato, 3:574-594, Sep 2022. URL: https://doi.org/10.3390/hemato3040040, doi:10.3390/hemato3040040. This article has 34 citations.

27. (roth2025[coldagglutinindisease pages 10-11): Alexander Röth, Kersten Borchert, Carla Dorn, Moritz Kleemiß, Sixten Körper, Stephanie Mayer, Philippe Schafhausen, Karin G. Schrenk, Peter Bramlage, and Frauke Theis. [cold agglutinin disease (cad)]. Innere Medizin, Jul 2025. URL: https://doi.org/10.1007/s00108-025-01926-0, doi:10.1007/s00108-025-01926-0. This article has 0 citations.

28. (peters2020coldagglutinindisease pages 1-2): Amy P. Gabbard and Garrett S. Booth. Cold agglutinin disease. Clinical Hematology International, 2:95-100, Feb 2020. URL: https://doi.org/10.2991/chi.k.200706.001, doi:10.2991/chi.k.200706.001. This article has 62 citations.

29. (rossi2018shortcourseof pages 2-2): Giuseppe Rossi, Doriana Gramegna, Francesca Paoloni, Bruno Fattizzo, Francesca Binda, Mariella D’Adda, Mirko Farina, Elisa Lucchini, Francesca Romana Mauro, Flavia Salvi, Monia Marchetti, Paola Fazi, Francesco Zaja, and Wilma Barcellini. Short course of bortezomib in anemic patients with relapsed cold agglutinin disease: a phase 2 prospective gimema study. Blood, 132 5:547-550, Aug 2018. URL: https://doi.org/10.1182/blood-2018-03-835413, doi:10.1182/blood-2018-03-835413. This article has 103 citations and is from a highest quality peer-reviewed journal.

30. (costa2025beneaththesurface pages 15-16): Alessandro Costa, Olga Mulas, Angela Maria Mereu, Mercede Schintu, Marianna Greco, and Giovanni Caocci. Beneath the surface in autoimmune hemolytic anemia: pathogenetic networks, therapeutic advancements and open questions. Frontiers in Immunology, Jul 2025. URL: https://doi.org/10.3389/fimmu.2025.1624667, doi:10.3389/fimmu.2025.1624667. This article has 8 citations and is from a peer-reviewed journal.

31. (NCT05096403 chunk 1):  A Study to Evaluate the Efficacy and Safety of Pegcetacoplan in Patients With Cold Agglutinin Disease (CAD). Swedish Orphan Biovitrum. 2022. ClinicalTrials.gov Identifier: NCT05096403

32. (OpenTargets Search: cold agglutinin disease): Open Targets Query (cold agglutinin disease, 7 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

## Artifacts

- [Edison artifact artifact-00](Cold_Agglutinin_Disease-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 17 |
| Resolved | 17 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| Quoted claims with nothing to check against | 1 |
| References weighed for topical relevance | 17 |
| On topic | 8 |
| Off topic | 0 |

### Quotes that could not be checked

There was no text to compare these against, so they are neither confirmed nor contradicted:

- `DOI:10.1002/ajh.26205`: "Primary cold agglutinin disease is caused by a unique indolent B-cell lymphoproliferative disorder of the bone marrow."
  - Reference resolved but exposes no abstract or full text to search

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
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0018922` (4 mentions) - the report calls it "if available"; MONDO calls it **cold agglutinin disease**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.