---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-04T14:08:22.923465'
end_time: '2026-09-04T14:18:01.890513'
duration_seconds: 578.97
template_file: templates/disease_pathophysiology_research.md
template_sha: 1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666
template_variables:
  disease_name: Midface Hypoplasia, Hearing Impairment, Elliptocytosis, and Nephrocalcinosis
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 15
reference_validation:
  total_references: 4
  verified: 4
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 4
  on_topic: 3
  validator_version: 0.2.1
term_validation:
  total_terms: 30
  verified: 29
  not_found: 0
  obsolete: 1
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 2
  labels_matching: 0
  labels_variant: 2
  obsolete_terms:
  - term_id: HP:0010985
    ontology_label: obsolete Gonosomal inheritance
    replaced_by: HP:0000005
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Midface_Hypoplasia_Hearing_Impairment_Elliptocytosis_And_Nephrocalcinosis-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Midface Hypoplasia, Hearing Impairment, Elliptocytosis, and Nephrocalcinosis
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Midface Hypoplasia, Hearing Impairment, Elliptocytosis, and Nephrocalcinosis** covering all of the
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
- **Disease Name:** Midface Hypoplasia, Hearing Impairment, Elliptocytosis, and Nephrocalcinosis
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Midface Hypoplasia, Hearing Impairment, Elliptocytosis, and Nephrocalcinosis** covering all of the
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


# Research report: AMMECR1-related midface hypoplasia, hearing impairment, elliptocytosis, and nephrocalcinosis

## Executive summary

**Midface hypoplasia, hearing impairment, elliptocytosis, and nephrocalcinosis (MFHEIN; OMIM 300990)** is an ultra-rare X-linked Mendelian disorder caused by germline disruption of **AMMECR1** at Xq23. The best-established manifestations are midface hypoplasia/dysmorphism, developmental or speech delay, hypotonia, short stature or growth failure, sensorineural hearing loss (SNHL), skeletal abnormalities, and variably penetrant elliptocytosis. Nephrocalcinosis, hypercalciuria, cleft palate, congenital heart defects, hip dysplasia, and other congenital anomalies occur in some patients, but the very small literature prevents reliable frequencies and makes causality less certain for several findings. AMMECR1-related MFHEIN must be distinguished from the larger **Xq22.3–q23 AMME contiguous-gene deletion syndrome**, in which deletion of **COL4A5** causes Alport nephropathy and associated ocular/auditory disease. (andreoletti2017ammecr1asingle pages 1-1, moysesoliveira2018inactivationofammecr1 pages 2-3, andreoletti2017ammecr1asingle pages 5-6)

The foundational primary reports are Andreoletti et al., *Journal of Medical Genetics* 2017, DOI [10.1136/jmedgenet-2016-104100](https://doi.org/10.1136/jmedgenet-2016-104100); Moysés-Oliveira et al., *Human Mutation* 2018, DOI [10.1002/humu.23373](https://doi.org/10.1002/humu.23373); Poreau et al., *American Journal of Medical Genetics A* 2019, DOI [10.1002/ajmg.a.61057](https://doi.org/10.1002/ajmg.a.61057); and Koene et al., *American Journal of Medical Genetics A* 2022, DOI [10.1002/ajmg.a.62669](https://doi.org/10.1002/ajmg.a.62669). No disease-specific 2023–2024 mechanistic study, natural-history cohort, guideline, or interventional trial was identified. Consequently, this report avoids presenting case-series proportions as population frequencies.

The following table provides a compact knowledge-base representation.

| Domain | Best-supported finding | Evidence strength/type | Suggested ontology terms |
|---|---|---|---|
| Disease identity | **Midface hypoplasia, hearing impairment, elliptocytosis, and nephrocalcinosis (MFHEIN; OMIM 300990)** is an ultra-rare, multisystem AMMECR1-related disorder distinct from the broader COL4A5-containing AMME contiguous-gene deletion syndrome. | Strong disease-level evidence from multiple human case series; boundaries remain evolving because very few patients are known. (andreoletti2017ammecr1asingle pages 1-1, moysesoliveira2018inactivationofammecr1 pages 2-3, poreau2019xq22.3q23microdeletionharboring pages 4-5) | MONDO: AMMECR1-related MFHEIN; HP: phenotypic abnormality |
| Cause and inheritance | Hemizygous missense or loss-of-function variants and intragenic/whole-gene deletions affecting **AMMECR1** cause an X-linked disorder. Affected males usually have the fuller phenotype; heterozygous females can manifest features depending partly on X-inactivation. | Strong human genetic segregation plus functional evidence; variable expressivity demonstrated. (moysesoliveira2018inactivationofammecr1 pages 1-2, koene2022hearinglosscleft pages 1-3, andreoletti2017ammecr1asingle pages 3-4) | X-linked inheritance (HP:0010985); AMMECR1; germline variant |
| Core phenotypes | Recurrent findings include midface hypoplasia, short stature or growth failure, developmental/speech delay, sensorineural hearing loss, and subtle or overt elliptocytosis. | Moderate evidence from small human series; no reliable population-level frequencies. Elliptocytosis is variably penetrant and can be absent on an early smear. (moysesoliveira2018inactivationofammecr1 pages 4-6, andreoletti2017ammecr1asingle pages 6-7, poreau2019xq22.3q23microdeletionharboring pages 4-5) | Midface hypoplasia (HP:0011800); short stature (HP:0004322); global developmental delay (HP:0001263); speech delay (HP:0000750); sensorineural hearing impairment (HP:0000407); elliptocytosis (HP:0004445) |
| Associated phenotypes | Nephrocalcinosis/hypercalciuria, hypotonia, cleft or submucous cleft palate with bifid uvula, skeletal abnormalities, congenital hip dysplasia, joint hypermobility, cardiac defects, genital anomalies, talipes, ocular findings, and fetal edema have been reported. Some may be uncommon, incidental, or attributable to neighboring genes in larger deletions. | Limited human case evidence; causality is strongest for growth, skeletal, cardiac, palate, and hearing phenotypes but less secure for nephrocalcinosis and some ocular findings. (moysesoliveira2018inactivationofammecr1 pages 4-6, andreoletti2017ammecr1asingle pages 7-8, andreoletti2017ammecr1asingle pages 8-8) | Nephrocalcinosis (HP:0000121); hypercalciuria (HP:0002150); muscular hypotonia (HP:0001252); cleft palate (HP:0000175); bifid uvula (HP:0000193); joint hypermobility (HP:0001382); talipes equinovarus (HP:0001762) |
| Temporal course | Congenital findings may be detectable prenatally or neonatally; hypotonia, feeding problems, skeletal/palatal anomalies, and dysmorphism occur early. Hearing loss and elliptocytosis may emerge or worsen during childhood, while speech development and facial appearance can improve with age and intervention. | Longitudinal observations from individual patients, not a formal natural-history cohort. (andreoletti2017ammecr1asingle pages 1-2, andreoletti2017ammecr1asingle pages 6-7, andreoletti2017ammecr1asingle pages 3-3, andreoletti2017ammecr1asingle pages 5-6) | Congenital onset (HP:0003577); infantile onset (HP:0003593); childhood onset (HP:0011463); progressive hearing impairment (HP:0001730) |
| Female carriers | Three related heterozygous females with an exon-4 deletion all reported mild-to-moderate SNHL; one also had soft-palate cleft and congenital hip dysplasia. Peripheral-blood X-inactivation ranged from 60:40 to 90:10, suggesting—but not proving—a severity relationship. | Direct human pedigree, audiometric, deletion, and X-inactivation evidence; penetrance cannot be generalized from one family. (koene2022hearinglosscleft pages 4-5, koene2022hearinglosscleft pages 1-3, koene2022hearinglosscleft pages 3-4) | Female limited expression; skewed X-inactivation; sensorineural hearing impairment (HP:0000407); cleft soft palate (HP:0000185); congenital hip dislocation/dysplasia |
| Diagnostics | Phenotype-led evaluation should include sequencing and deletion/duplication analysis of AMMECR1, peripheral blood smear, audiology, renal ultrasound plus renal function/calcium studies, developmental and palatal assessment, growth/skeletal examination, and consideration of cardiac and ophthalmic assessment. WES identified the original missense family; CMA detects regional deletions; WGS may help when sequencing and copy-number tests are unrevealing. | WES, Sanger segregation, blood-smear, audiometric, ultrasound, and microarray approaches are documented in cases; no consensus diagnostic criteria or validated biomarker exists. (andreoletti2017ammecr1asingle pages 1-2, andreoletti2017ammecr1asingle pages 3-4, andreoletti2017ammecr1asingle pages 7-8, andreoletti2017ammecr1asingle pages 4-5) | Genetic testing; peripheral blood smear; pure-tone audiometry; renal ultrasonography; developmental assessment |
| Key differential | Exclude Xq22.3–q23 contiguous deletions involving **COL4A5**, which add Alport nephropathy/hematuria and related ocular manifestations. Other hearing-loss-plus-nephrocalcinosis disorders and hereditary red-cell membrane disorders should be considered according to biochemical findings. | Direct genotype–phenotype comparison supports the COL4A5 distinction; broader differential is clinical inference. (andreoletti2017ammecr1asingle pages 1-2, andreoletti2017ammecr1asingle pages 5-6, andreoletti2017ammecr1asingle pages 6-7) | Alport syndrome; hematuria (HP:0000790); distal renal tubular acidosis; hereditary elliptocytosis |
| Management | No disease-modifying therapy is established. Reported real-world care includes hearing aids, cleft-palate repair, developmental/speech support, surveillance of renal, growth, skeletal, and cardiac abnormalities, and individualized treatment of complications. Growth-hormone response was reported in one short-stature patient but is not validated as syndrome-specific therapy. | Case-level treatment evidence only; no controlled treatment studies. Hearing and palate treatment was followed by improved speech/language in affected children. (moysesoliveira2018inactivationofammecr1 pages 4-6, koene2022hearinglosscleft pages 1-3, andreoletti2017ammecr1asingle pages 6-6) | Hearing aid; palatoplasty; speech therapy; developmental intervention; genetic counseling; growth-hormone therapy |
| Cellular mechanism | AMMECR1 is a nuclear protein containing two RAGNYA folds. The p.Gly177Asp protein showed abnormal, nonuniform nuclear localization and fewer transfected GFP-positive cells, consistent with protein dysfunction or instability. AMMECR1 loss was associated with increased AMMECR1L expression, possibly providing partial compensation. | Nuclear localization and mutant mislocalization demonstrated in cultured cells; instability and AMMECR1L compensation remain inferred rather than proven. (andreoletti2017ammecr1asingle pages 8-9, andreoletti2017ammecr1asingle pages 4-5, moysesoliveira2018inactivationofammecr1 pages 6-8) | GO: nucleus (GO:0005634); protein localization to nucleus; protein stability; nucleic-acid binding; CL: cultured human epithelial cell |
| Molecular pathway | RAGNYA-fold structure predicts nucleic-acid interaction and possibly an RNA-associated catalytic role; coexpression with cell-cycle genes suggests a developmental growth mechanism. No specific Wnt, MAPK, mTOR, PI3K–AKT, immune, metabolic, or epigenetic pathway has been causally demonstrated. | Structural/computational prediction and coexpression evidence; biochemical substrate and downstream pathway remain unknown. (moysesoliveira2018inactivationofammecr1 pages 1-2, moysesoliveira2018inactivationofammecr1 pages 6-8) | GO: nucleic acid binding; cell-cycle regulation; developmental growth; RNA modification—provisional only |
| Affected tissues/cells | Clinical evidence implicates craniofacial mesenchyme/palate, inner ear, erythrocytes, growth plate/bone, kidney, heart, and nervous/developmental systems. AMMECR1 protein expression was demonstrated in developing human fetal cochlear epithelium at gestational weeks 13 and 17. | Multisystem human phenotype plus direct fetal-inner-ear immunohistochemistry; disease-critical cell populations are otherwise undefined. (koene2022hearinglosscleft pages 4-5, koene2022hearinglosscleft pages 1-3, andreoletti2017ammecr1asingle pages 7-8) | CL: erythrocyte (CL:0000232); epithelial cell (CL:0000066); chondrocyte (CL:0000138); UBERON: inner ear, kidney, midface, palate, bone, heart |
| Model organisms | Zebrafish ammecr1 knockdown altered approximately 90% of transcripts and generated patient-reminiscent developmental phenotypes. Mouse and human proteins share approximately 95.2% amino-acid identity, supporting evolutionary conservation, but no disease-specific mammalian knockout phenotype is established in the cited evidence. | Functional zebrafish knockdown plus comparative mouse-ortholog evidence; morpholino limitations apply and complete human MFHEIN recapitulation is unproven. (moysesoliveira2018inactivationofammecr1 pages 1-2, moysesoliveira2018inactivationofammecr1 pages 6-8) | Danio rerio (NCBITaxon:7955); Mus musculus (NCBITaxon:10090); gene knockdown; developmental abnormality |
| Epidemiology and evidence gaps | Prevalence, incidence, carrier frequency, sex ratio, survival, quality-of-life scores, penetrance, and prognostic biomarkers are unknown. Published evidence consists of a handful of families and deletion cases, precluding meaningful percentages. | Very low-certainty epidemiology; absence of registries and natural-history cohorts. (andreoletti2017ammecr1asingle pages 1-1, moysesoliveira2018inactivationofammecr1 pages 1-2, koene2022hearinglosscleft pages 1-3) | Rare disease; ultra-rare genetic disease; natural-history study needed |
| Trials and advanced therapies | No AMMECR1/MFHEIN-specific interventional trial, gene therapy, RNA therapy, cell therapy, targeted drug, or validated pharmacogenomic strategy was identified. | Clinical-trial search negative; current care is supportive and complication-directed. | Supportive care; symptom management; no applicable investigational intervention term |


*Table: Concise knowledge-base summary separating well-supported human and functional findings from hypotheses and evidence gaps. Ontology suggestions emphasize established terms while avoiding unsupported precision.*

## 1. Disease information

### Definition and nomenclature

MFHEIN is an AMMECR1-related, multisystem developmental disorder. Synonyms include **MFHEIN**, **AMMECR1-related disorder**, and, less precisely, **AMMECR1-related AMME phenotype**. The historical acronym **AMME** means *Alport syndrome, intellectual disability/mental retardation, midface hypoplasia, and elliptocytosis* and ordinarily refers to a larger Xq22.3–q23 contiguous deletion; it should not be used without qualification for isolated AMMECR1 disease. (andreoletti2017ammecr1asingle pages 1-1, andreoletti2017ammecr1asingle pages 6-7)

**Identifiers:** OMIM phenotype **300990** is supported by the literature. A dedicated MONDO identifier, Orphanet number, MeSH heading, and disease-specific ICD-10/ICD-11 code were not established in the retrieved authoritative sources. Practical coding therefore generally requires phenotype or congenital-anomaly codes rather than a unique MFHEIN code. Suggested knowledge-base label: **“AMMECR1-related midface hypoplasia, hearing impairment, elliptocytosis, and nephrocalcinosis.”**

The evidence is **aggregated disease-level literature derived from individual patients and families**, not EHR-scale cohorts, registries, or population surveillance. The original single-gene report described two maternal half-brothers; later work added a small number of loss-of-function cases, deletion cases, and manifesting female relatives. (andreoletti2017ammecr1asingle pages 1-1, moysesoliveira2018inactivationofammecr1 pages 1-2, koene2022hearinglosscleft pages 1-3)

### Direct abstract statements

Andreoletti et al. concluded that a single missense mutation “**causes a phenotype of midface hypoplasia, mild intellectual disability and the presence of elliptocytes**” and that AMMECR1 contributes to speech/language delay, hypotonia, and hearing loss. (andreoletti2017ammecr1asingle pages 1-1)

Koene et al. reported that “**all three women reported hearing loss**” and that audiograms showed “**mild to moderate SNHL with a variable pattern of the affected frequencies**.” (koene2022hearinglosscleft pages 1-3)

## 2. Etiology, risk, and protective factors

### Causal factors

The initiating cause is a **germline AMMECR1 variant that reduces or alters gene function**. Documented lesions include:

* Hemizygous missense **c.530G>A, p.(Gly177Asp)** in two maternal half-brothers, inherited from their heterozygous mother. It was absent from ExAC, dbSNP, and local controls at the time and altered nuclear distribution in transfected cells. (andreoletti2017ammecr1asingle pages 3-4, andreoletti2017ammecr1asingle pages 4-5)
* Nonsense variants **p.(Arg168Ter)**, maternally inherited, and **p.(Tyr143Ter)**, de novo. (moysesoliveira2018inactivationofammecr1 pages 4-6)
* A reported **c.133C>T, p.(Arg45Ter)** allele in comparative case material. (poreau2019xq22.3q23microdeletionharboring pages 4-4)
* Intragenic deletion of approximately 23 kb containing exon 4 in a family with affected females. (koene2022hearinglosscleft pages 1-3, koene2022hearinglosscleft pages 3-4)
* Whole-gene or multigene deletions and an X-autosome translocation interrupting AMMECR1; in the affected female with the translocation, the normal X was preferentially inactivated. (moysesoliveira2018inactivationofammecr1 pages 1-2, moysesoliveira2018inactivationofammecr1 pages 2-3)

These are constitutional variants. No somatic disease mechanism is known. Public-database ACMG classifications and current gnomAD allele counts could not be verified from the retrieved texts; the original p.Gly177Asp report called it a VUS before segregation and functional evidence supported pathogenicity. Variant interpretation should therefore be performed against current ClinVar/gnomAD data rather than copying the historical label.

### Risk factors and modifiers

The principal risk factor is inheritance of a familial AMMECR1 variant. Hemizygous males generally have greater risk of a multisystem phenotype. Heterozygous females can be symptomatic: in one family all three carriers had SNHL, and peripheral-blood X-inactivation ratios were 90:10, 80:20, and 60:40. Skewing may modify severity but was not proven causal and blood may not reflect disease-relevant tissues. (koene2022hearinglosscleft pages 4-5, koene2022hearinglosscleft pages 1-3)

**AMMECR1L** is a plausible molecular modifier: its RNA and protein abundance increased in AMMECR1-deficient patient cells, suggesting partial compensation, but no human modifier allele has been demonstrated. (moysesoliveira2018inactivationofammecr1 pages 6-8, moysesoliveira2018inactivationofammecr1 pages 1-2)

No environmental, infectious, lifestyle, occupational, age-related susceptibility, or protective factor is known to cause MFHEIN. No protective allele, diet, supplement, or exposure has been validated. Environmental influences may modify general renal-stone or hearing risk, but that is not established as an AMMECR1 gene–environment interaction.

## 3. Phenotypes

Because published patients number only in the low double digits across heterogeneous variant classes, **population frequencies cannot be calculated**. “Recurrent,” “reported,” and “uncertain” below are more defensible than percentages.

* **Midface hypoplasia and facial dysmorphism** — congenital physical sign; recurrent and sometimes less conspicuous with age. Associated features include thin upper lip, long philtrum, small or pointed jaw, broad nasal tip, abnormal palpebral fissures, and short neck. Suggested HPO: **Midface hypoplasia HP:0011800**, Micrognathia HP:0000347. (andreoletti2017ammecr1asingle pages 6-6, poreau2019xq22.3q23microdeletionharboring pages 4-5)
* **SNHL** — clinical/functional sign; may begin in childhood and progress. One patient’s loss began at age three. Female carriers had mild-to-moderate, flat, low-frequency, or high-frequency patterns; fetal cochlear expression supports biological plausibility. HPO: **Sensorineural hearing impairment HP:0000407**, Progressive hearing impairment HP:0001730. Hearing affects communication, schooling, and speech development. (koene2022hearinglosscleft pages 4-5, koene2022hearinglosscleft pages 1-3, andreoletti2017ammecr1asingle pages 5-6)
* **Elliptocytosis** — laboratory/morphologic abnormality, usually mild. Scattered elliptocytes and anisocytosis persisted on repeat smear in one older brother, whereas his younger affected brother had a normal smear at four years. This supports variable or age-related expression and means a normal smear does not exclude MFHEIN. HPO: **Elliptocytosis HP:0004445**. Clinically significant hemolysis has not been established. (andreoletti2017ammecr1asingle pages 6-7, andreoletti2017ammecr1asingle pages 3-4)
* **Nephrocalcinosis/hypercalciuria** — imaging/laboratory finding in the original family and selected tabulated cases; causality is less secure than the acronym implies. HPO: **Nephrocalcinosis HP:0000121**, Hypercalciuria HP:0002150. Long-term CKD risk specifically attributable to MFHEIN is unknown. (andreoletti2017ammecr1asingle pages 7-8, andreoletti2017ammecr1asingle pages 8-8)
* **Developmental, speech, and language delay** — pediatric neurodevelopmental phenotype, usually mild to variable. Some improvement/catch-up occurred: at age five one child attended mainstream school with better speech/language. Hearing loss and cleft palate may contribute. HPO: Global developmental delay HP:0001263; Delayed speech and language development HP:0000750. (andreoletti2017ammecr1asingle pages 3-3, andreoletti2017ammecr1asingle pages 6-6)
* **Hypotonia and motor delay** — congenital/infantile sign; may coexist with hypermobility. HPO: Muscular hypotonia HP:0001252; Delayed gross motor development HP:0002194. (andreoletti2017ammecr1asingle pages 1-2, andreoletti2017ammecr1asingle pages 7-8)
* **Growth and skeletal disease** — short stature/failure to thrive, delayed bone age, osteopenia/demineralization, scoliosis, radioulnar synostosis, wormian bones, Looser zones, cone-shaped phalanges, talipes, and hip dysplasia have been reported. Severity is variable. HPO: Short stature HP:0004322, Osteopenia HP:0000938, Scoliosis HP:0002650, Talipes equinovarus HP:0001762. (moysesoliveira2018inactivationofammecr1 pages 4-6, andreoletti2017ammecr1asingle pages 1-2)
* **Palatal/midline abnormalities** — cleft or submucous cleft palate and bifid uvula, congenital and surgically actionable. HPO: Cleft palate HP:0000175; Bifid uvula HP:0000193. These can impair feeding, speech, and middle-ear function. (andreoletti2017ammecr1asingle pages 1-1, andreoletti2017ammecr1asingle pages 6-6)
* **Cardiac findings** — atrial septal defect, arrhythmia/tachycardia, patent ductus arteriosus, right bundle-branch block, and mild tricuspid regurgitation occur in individual cases. HPO terms should be assigned per lesion rather than treating “heart disease” as obligatory. (moysesoliveira2018inactivationofammecr1 pages 4-6, andreoletti2017ammecr1asingle pages 7-8)
* **Other reported findings** — fetal nuchal edema/pericardial effusion, poor feeding, joint hypermobility, clinodactyly, genital anomalies, ureterocele/reflux, strabismus, cataract, myopia, and dental abnormalities. Several may be private, incidental, or deletion-size dependent. (andreoletti2017ammecr1asingle pages 1-2, moysesoliveira2018inactivationofammecr1 pages 4-6, andreoletti2017ammecr1asingle pages 8-8)

No validated EQ-5D, SF-36, PROMIS, behavioral, psychiatric, or disease-specific quality-of-life data exist. The probable major burdens are hearing/communication impairment, developmental support needs, repeated specialist surveillance, palate surgery, and skeletal or renal morbidity.

## 4. Genetic and molecular information

**Causal gene:** **AMMECR1**, Xq23, encoding an approximately 33-kDa nuclear protein with two RAGNYA folds. The retrieved literature used transcript **NM_015365.2**. The protein’s physiological substrate and catalytic activity remain unknown. (koene2022hearinglosscleft pages 3-4, moysesoliveira2018inactivationofammecr1 pages 6-8)

The combined human evidence supports loss of function as a major disease mechanism: nonsense alleles, intragenic/whole-gene deletions, and a gene-disrupting translocation all cause overlapping phenotypes. The p.Gly177Asp missense protein retains nuclear localization but has an abnormal nonuniform pattern and fewer GFP-positive transfected cells, consistent with altered localization, instability, or degradation. The latter two mechanisms are interpretations rather than directly quantified biochemical conclusions. (andreoletti2017ammecr1asingle pages 8-9, andreoletti2017ammecr1asingle pages 4-5)

No recurrent founder allele, pathogenic repeat expansion, mitochondrial variant, aneuploidy, inversion, somatic mosaicism, or validated epigenetic signature is known. Larger Xq22.3–q23 deletions can include **TMEM164, RGAG1, ACSL4, COL4A5**, and other genes; phenotypes in these patients cannot automatically be assigned solely to AMMECR1. In particular, **COL4A5** deletion explains Alport nephropathy, while **ACSL4** has been proposed to contribute substantially to intellectual disability in the broader deletion syndrome. (andreoletti2017ammecr1asingle pages 6-7, andreoletti2017ammecr1asingle pages 6-6)

## 5. Environmental information

There is no evidence that toxins, radiation, pollution, occupation, smoking, alcohol, diet, exercise, or infectious agents initiate MFHEIN. It is not infectious or zoonotic. General avoidance of excessive noise and nephrotoxic exposures may be clinically sensible in a patient with hearing or renal vulnerability, but these are precautionary principles—not demonstrated disease-specific protective factors.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. A germline **AMMECR1** missense, truncating, deletion, or gene-disrupting rearrangement **leads to** absent, reduced, or abnormally localized AMMECR1 protein. (moysesoliveira2018inactivationofammecr1 pages 1-2, andreoletti2017ammecr1asingle pages 4-5)
2. AMMECR1 dysfunction **leads to** impaired nuclear AMMECR1 activity; its two RAGNYA folds suggest nucleic-acid interaction, but the substrate and enzymatic function are **inferred, not demonstrated**. (moysesoliveira2018inactivationofammecr1 pages 6-8)
3. Impaired nuclear activity **is inferred to disrupt** developmental transcription/RNA handling or cell-cycle-linked programs; this is supported by coexpression with cell-cycle genes, not by a proven signaling pathway. (moysesoliveira2018inactivationofammecr1 pages 1-2)
4. These developmental disturbances **lead to**, or are inferred to lead to, tissue-specific defects in craniofacial/palatal development, growth plate and skeletal development, heart development, neurodevelopment, and fetal cochlear epithelium. Zebrafish knockdown producing patient-like developmental phenotypes supports this broad developmental role. (moysesoliveira2018inactivationofammecr1 pages 1-2)
5. **Craniofacial branch:** altered embryonic craniofacial development **results in** midface hypoplasia, dysmorphism, cleft/submucous palate, and bifid uvula. The intermediate cell biology is inferred.
6. **Auditory branch:** altered development or maintenance of AMMECR1-expressing cochlear epithelial cells **results in** SNHL; fetal-inner-ear expression is demonstrated, whereas the exact affected cochlear cell and lesion are unknown. (koene2022hearinglosscleft pages 4-5)
7. **Erythroid branch:** AMMECR1 dysfunction **results in** variably penetrant elliptocyte morphology, but the link to the erythrocyte membrane/cytoskeleton is unknown and no hemolytic mechanism has been demonstrated. (andreoletti2017ammecr1asingle pages 3-4)
8. **Renal branch:** an unresolved developmental or tubular mechanism **may lead to** hypercalciuria and nephrocalcinosis; causality is weaker and alternative renal genetic causes should be excluded. (andreoletti2017ammecr1asingle pages 8-8)
9. Increased **AMMECR1L** expression **may partially compensate for** AMMECR1 loss, contributing to variable severity; this is inferred from patient-cell expression rather than clinical modifier genetics. (moysesoliveira2018inactivationofammecr1 pages 6-8)

No causal Wnt, MAPK, mTOR, PI3K–AKT, autophagy, apoptosis, inflammatory, immune, oxidative-stress, or specific metabolic pathway has been established. Likewise, no disease-specific transcriptomic, proteomic, metabolomic, lipidomic, methylomic, single-cell, spatial-transcriptomic, organoid, iPSC, or CRISPR-screen signature has been reported.

Suggested provisional GO annotations are **nucleus (GO:0005634)**, nucleic-acid binding, protein localization to nucleus, regulation of cell cycle, developmental growth, skeletal-system development, heart development, and inner-ear development. “RNA modification” should be marked **computationally predicted**, not curated as a demonstrated MFHEIN mechanism. Suggested CL terms include erythrocyte **CL:0000232**, epithelial cell **CL:0000066**, and chondrocyte **CL:0000138**; only fetal cochlear epithelial expression is directly supported at cell-type level.

## 7. Anatomical structures affected

Primary implicated sites are the **midface and palate**, **inner ear/cochlea**, **blood/erythrocytes**, **kidney**, **skeleton/growth plate**, **heart**, and developing nervous system. Secondary sites can include eye, urinary tract, joints, and genital tract. Cochlear immunohistochemistry demonstrated AMMECR1 expression at gestational weeks 13 and 17, evolving from broad epithelial expression to selected apical cells. (koene2022hearinglosscleft pages 4-5)

Suggested UBERON concepts: midface, palate, inner ear/cochlea, kidney, blood, bone, growth plate, heart, and central nervous system. Subcellular localization is principally the **nucleus (GO:0005634)**, although overexpressed tagged protein was also detected in cytoplasmic fractions. (moysesoliveira2018inactivationofammecr1 pages 6-8)

Hearing loss may be symmetric or asymmetric; other disease manifestations have no established lateralization pattern. Talipes can be bilateral. (andreoletti2017ammecr1asingle pages 1-2, koene2022hearinglosscleft pages 1-3)

## 8. Temporal development and natural history

Onset is **congenital/developmental**. Fetal nuchal edema, pericardial effusion, short femurs, talipes, and structural anomalies can be prenatal; hypotonia, feeding difficulty, dysmorphism, cleft palate, and growth problems may be neonatal or infantile. (andreoletti2017ammecr1asingle pages 1-2)

Hearing loss can become evident in early childhood and may progress. Elliptocytosis may be detectable in infancy but can also be absent at age four and present by age ten. Facial dysmorphism can become less apparent, and some children show developmental and speech catch-up after treatment of hearing and palate problems. (andreoletti2017ammecr1asingle pages 6-7, andreoletti2017ammecr1asingle pages 3-3, andreoletti2017ammecr1asingle pages 7-8)

No validated disease stages, remission pattern, progression rate, or critical treatment window exists. The condition is genetically lifelong, but individual manifestations may be stable, progressive, or developmentally ameliorating. Early childhood is a practical intervention window for hearing, palate, feeding, and developmental support.

## 9. Inheritance and population

Inheritance is **X-linked**, usually described as X-linked recessive but with **manifesting heterozygous females**. Both maternally inherited and de novo variants occur. X-inactivation contributes to female expression, but penetrance is unknown. Variable expressivity is clear in males and females. (koene2022hearinglosscleft pages 4-5, moysesoliveira2018inactivationofammecr1 pages 1-2, andreoletti2017ammecr1asingle pages 3-4)

No evidence supports anticipation. Germline mosaicism remains theoretically possible after an apparently de novo variant but has not been documented. No founder effect, consanguinity association, carrier frequency, ethnic enrichment, geographic concentration, sex ratio, prevalence, or incidence estimate is available. The literature comprises a handful of families, so an estimate per 100,000 would be misleading.

Standard counseling for a heterozygous mother is a 50% transmission probability per pregnancy; sons inheriting the variant are hemizygous, while daughters inheriting it may be asymptomatic or variably affected. Counseling must account for uncertain female penetrance.

## 10. Diagnostics

There are no formal diagnostic criteria. A phenotype-led workup should include:

1. **Molecular testing:** sequencing plus deletion/duplication analysis of AMMECR1. WES identified the original missense family, with Sanger confirmation and segregation. Exome/genome analysis should include CNV calling. CMA is appropriate where multiple congenital anomalies or a regional Xq deletion is suspected; WGS can detect coding, copy-number, structural, and some deep-intronic lesions when earlier tests are negative. (andreoletti2017ammecr1asingle pages 1-2, andreoletti2017ammecr1asingle pages 3-4)
2. **Define deletion extent:** determine whether **COL4A5**, ACSL4, or other neighboring genes are involved, because this materially changes renal, ocular, and neurodevelopmental interpretation.
3. **Hematology:** complete blood count, reticulocytes/hemolysis studies if indicated, and expert peripheral smear. Mild scattered elliptocytes may be missed, and a normal smear does not exclude disease. (andreoletti2017ammecr1asingle pages 3-4, andreoletti2017ammecr1asingle pages 6-7)
4. **Audiology:** newborn screen review, age-appropriate pure-tone or objective audiometry, tympanometry, and longitudinal monitoring because SNHL can be progressive.
5. **Renal evaluation:** urinalysis for blood/protein, serum creatinine/electrolytes/bicarbonate/calcium/phosphate, urine calcium and citrate as clinically appropriate, blood pressure, and renal ultrasound for nephrocalcinosis or structural abnormalities.
6. **Development and anatomy:** developmental, speech/language, feeding, palate/velopharyngeal, growth, skeletal, joint, cardiac, ophthalmic, and genital/urinary assessments tailored to findings. The broad reported phenotype supports this baseline multisystem evaluation. (andreoletti2017ammecr1asingle pages 7-8)

**Differential diagnosis:** COL4A5-containing AMME deletion/Alport syndrome is distinguished by hematuria and progressive glomerular nephropathy; exome sequencing may miss deep-intronic COL4A5 variants. (andreoletti2017ammecr1asingle pages 5-6) Other important phenotype-driven alternatives include hereditary elliptocytosis due to erythrocyte-membrane genes; SLC4A1-related distal renal tubular acidosis with red-cell abnormalities; ATP6V1B1/ATP6V0A4-related distal RTA with SNHL and nephrocalcinosis; branchio-oto-renal disorders; and other syndromic cleft-palate/short-stature conditions. These broader alternatives are clinical differentials rather than documented AMMECR1 phenocopies.

There is no newborn population screen, biochemical biomarker, enzyme assay, biopsy criterion, or validated omics diagnostic. Cascade testing is appropriate after a familial pathogenic/likely pathogenic variant is established.

## 11. Outcome and prognosis

No survival curve, mortality rate, life-expectancy estimate, standardized disability score, or prognostic biomarker exists. The reported phenotype is generally compatible with childhood survival and, in some patients, normal intelligence and mainstream schooling. One child showed developmental improvement by age five, and facial features may soften over time. (andreoletti2017ammecr1asingle pages 3-3)

Likely morbidity arises from progressive hearing loss, communication delay, cleft-palate complications, growth/skeletal abnormalities, congenital heart disease, and possible renal calcification. Elliptocytosis is often subtle and has not been shown to produce consistent hemolytic anemia. Prognosis should be individualized according to renal function, hearing trajectory, cardiac lesion, skeletal disease, and deletion extent.

## 12. Treatment and current applications

There is **no disease-modifying pharmacotherapy** and no established genotype-specific drug, pharmacogenomic rule, gene therapy, RNA therapy, cell therapy, or immunotherapy.

Real-world management is multidisciplinary and complication directed:

* **Hearing:** hearing aids were used in reported patients; cochlear implantation would follow ordinary audiological criteria, although no MFHEIN-specific outcome is published. Suggested NCIT concepts: Hearing Aid; Cochlear Implantation. (koene2022hearinglosscleft pages 1-3, andreoletti2017ammecr1asingle pages 6-6)
* **Palate/feeding/speech:** cleft-palate repair plus speech-language and feeding therapy. Hearing aids and palate repair were followed by improved speech/language in the original family. NCIT: Cleft Palate Repair/Palatoplasty; Speech Therapy; Supportive Care. (andreoletti2017ammecr1asingle pages 6-6)
* **Development:** early intervention, educational support, physical and occupational therapy according to hypotonia and motor delay.
* **Renal:** nephrology surveillance and treatment guided by urine chemistry and renal function. Hydration and stone-prevention therapy should be individualized; no AMMECR1-specific alkali or thiazide evidence exists.
* **Growth/skeleton:** nutrition and endocrine evaluation, vitamin/mineral assessment where osteopenia is present, orthopedic management, and physiotherapy. Growth hormone produced a response in one patient, but this is anecdotal and not a validated syndrome-specific treatment. (moysesoliveira2018inactivationofammecr1 pages 4-6)
* **Cardiac/ocular/urogenital:** standard lesion-specific surveillance and intervention.

No MFHEIN/AMMECR1 interventional NCT study was identified, and treatment-response rates or syndrome-specific adverse-event statistics are unavailable.

## 13. Prevention

Primary lifestyle prevention is not possible for a germline Mendelian disorder. Primary reproductive options after molecular diagnosis include genetic counseling, familial variant testing, prenatal diagnosis, and preimplantation genetic testing where legally and clinically available.

Secondary prevention consists of early diagnosis through cascade testing and prompt audiology, palate/feeding, developmental, renal, cardiac, and skeletal evaluation. Tertiary prevention aims to reduce communication disability, renal complications, orthopedic morbidity, and developmental disadvantage through surveillance and timely treatment. Vaccination, antimicrobial prophylaxis, public-health sanitation, and environmental remediation have no disease-specific role.

## 14. Other species and natural disease

No naturally occurring veterinary MFHEIN analogue or zoonotic transmission is established. The relevant orthologues are **Ammecr1** in mouse (*Mus musculus*, NCBITaxon:10090) and **ammecr1** in zebrafish (*Danio rerio*, NCBITaxon:7955). Human and mouse AMMECR1 proteins were reported to share approximately **95.2% amino-acid identity**, including putative localization signals, supporting strong evolutionary conservation. No affected animal breed or VBO term is applicable.

## 15. Model organisms

A zebrafish morpholino model is the principal functional organismal evidence. An exon-3/intron-3 morpholino altered approximately **90%** of ammecr1 transcripts: about **65%** showed exon-3 skipping with frameshift and **25%** carried a 24-bp exon-3 deletion. Knockdown generated developmental phenotypes resembling patient growth, skeletal, and cardiac abnormalities; additional morpholinos and negative controls were used to address nonspecific effects. Morpholino models nevertheless have transient knockdown and off-target limitations and do not establish complete recapitulation of human hearing, erythrocyte, or renal disease. (moysesoliveira2018inactivationofammecr1 pages 6-8, moysesoliveira2018inactivationofammecr1 pages 1-2)

Mouse orthologues have been cloned and mapped, but the retrieved evidence did not establish a disease-specific knockout/knock-in mouse with full MFHEIN phenotyping. No validated patient iPSC, organoid, humanized model, or CRISPR knock-in model was identified.

## Evidence assessment and research priorities

The most authoritative interpretation is that **AMMECR1 loss or dysfunction causes an X-linked developmental syndrome with growth, craniofacial, auditory, skeletal, cardiac, neurodevelopmental, and erythrocyte manifestations**, while nephrocalcinosis and several rarer findings remain incompletely attributable. Experts have appropriately broadened the phenotype beyond the four words in “MFHEIN,” and the female-carrier study demonstrates that “recessive” should not be interpreted as clinically silent in every heterozygous female. (moysesoliveira2018inactivationofammecr1 pages 4-6, koene2022hearinglosscleft pages 4-5)

Highest-priority gaps are: an international patient registry; standardized HPO phenotyping; longitudinal audiology, renal, hematologic, growth, and cardiac data; current ClinVar/gnomAD curation; biochemical identification of the AMMECR1 substrate; stable CRISPR animal/cellular models; and direct comparison of isolated AMMECR1 variants with precisely mapped multigene deletions. Until these data exist, reported manifestations should be annotated with patient-level evidence and uncertainty rather than fixed frequencies.

References

1. (andreoletti2017ammecr1asingle pages 1-1): Gaia Andreoletti, Eleanor G Seaby, Jennifer M Dewing, Ita O'Kelly, Katherine Lachlan, Rodney D Gilbert, and Sarah Ennis. Ammecr1: a single point mutation causes developmental delay, midface hypoplasia and elliptocytosis. Journal of Medical Genetics, 54:269-277, Nov 2017. URL: https://doi.org/10.1136/jmedgenet-2016-104100, doi:10.1136/jmedgenet-2016-104100. This article has 19 citations and is from a domain leading peer-reviewed journal.

2. (moysesoliveira2018inactivationofammecr1 pages 2-3): Mariana Moysés-Oliveira, Giuliana Giannuzzi, Richard J. Fish, Jill A. Rosenfeld, Florence Petit, Maria de Fatima Soares, Leslie Domenici Kulikowski, Adriana Di-Battista, Malú Zamariolli, Fan Xia, Thomas Liehr, Nadezda Kosyakova, Gianna Carvalheira, Michael Parker, Eleanor G. Seaby, Sarah Ennis, Rodney D. Gilbert, R. Tanner Hagelstrom, Maria L. Cremona, Wenhui L. Li, Alka Malhotra, Anjana Chandrasekhar, Denise L. Perry, Ryan J. Taft, Julie McCarrier, Donald G. Basel, Joris Andrieux, Taiza Stumpp, Fernanda Antunes, Gustavo José Pereira, Marguerite Neerman-Arbez, Vera Ayres Meloni, Margaret Drummond-Borg, Maria Isabel Melaragno, and Alexandre Reymond. Inactivation of ammecr1 is associated with growth, bone, and heart alterations. Human Mutation, 39:281-291, Feb 2018. URL: https://doi.org/10.1002/humu.23373, doi:10.1002/humu.23373. This article has 20 citations and is from a domain leading peer-reviewed journal.

3. (andreoletti2017ammecr1asingle pages 5-6): Gaia Andreoletti, Eleanor G Seaby, Jennifer M Dewing, Ita O'Kelly, Katherine Lachlan, Rodney D Gilbert, and Sarah Ennis. Ammecr1: a single point mutation causes developmental delay, midface hypoplasia and elliptocytosis. Journal of Medical Genetics, 54:269-277, Nov 2017. URL: https://doi.org/10.1136/jmedgenet-2016-104100, doi:10.1136/jmedgenet-2016-104100. This article has 19 citations and is from a domain leading peer-reviewed journal.

4. (poreau2019xq22.3q23microdeletionharboring pages 4-5): Brice Poreau, Francis Ramond, Radu Harbuz, Véronique Satre, Claire Barro, Claire Vettier, Véronique Adouard, Julien Thevenon, Pierre‐Simon Jouk, Charles Coutton, Renaud Touraine, and Klaus Dieterich. Xq22.3q23 microdeletion harboring tmem164 and ammecr1 genes: two case reports confirming a recognizable phenotype with short stature, midface hypoplasia, intellectual delay, and elliptocytosis. American Journal of Medical Genetics Part A, 179:650-654, Apr 2019. URL: https://doi.org/10.1002/ajmg.a.61057, doi:10.1002/ajmg.a.61057. This article has 7 citations.

5. (moysesoliveira2018inactivationofammecr1 pages 1-2): Mariana Moysés-Oliveira, Giuliana Giannuzzi, Richard J. Fish, Jill A. Rosenfeld, Florence Petit, Maria de Fatima Soares, Leslie Domenici Kulikowski, Adriana Di-Battista, Malú Zamariolli, Fan Xia, Thomas Liehr, Nadezda Kosyakova, Gianna Carvalheira, Michael Parker, Eleanor G. Seaby, Sarah Ennis, Rodney D. Gilbert, R. Tanner Hagelstrom, Maria L. Cremona, Wenhui L. Li, Alka Malhotra, Anjana Chandrasekhar, Denise L. Perry, Ryan J. Taft, Julie McCarrier, Donald G. Basel, Joris Andrieux, Taiza Stumpp, Fernanda Antunes, Gustavo José Pereira, Marguerite Neerman-Arbez, Vera Ayres Meloni, Margaret Drummond-Borg, Maria Isabel Melaragno, and Alexandre Reymond. Inactivation of ammecr1 is associated with growth, bone, and heart alterations. Human Mutation, 39:281-291, Feb 2018. URL: https://doi.org/10.1002/humu.23373, doi:10.1002/humu.23373. This article has 20 citations and is from a domain leading peer-reviewed journal.

6. (koene2022hearinglosscleft pages 1-3): Saskia Koene, Jeroen Knijnenburg, Mariette J. V. Hoffer, Fleur Zwanenburg, Monique C. Haak, Heiko Locher, Edward S. A. van Beelen, Gijs W. E. Santen, and Liselotte J. C. Rotteveel. Hearing loss, cleft palate, and congenital hip dysplasia in female carriers of an intragenic deletion of ammecr1. American Journal of Medical Genetics. Part a, 188:1578-1582, Jan 2022. URL: https://doi.org/10.1002/ajmg.a.62669, doi:10.1002/ajmg.a.62669. This article has 5 citations and is from a peer-reviewed journal.

7. (andreoletti2017ammecr1asingle pages 3-4): Gaia Andreoletti, Eleanor G Seaby, Jennifer M Dewing, Ita O'Kelly, Katherine Lachlan, Rodney D Gilbert, and Sarah Ennis. Ammecr1: a single point mutation causes developmental delay, midface hypoplasia and elliptocytosis. Journal of Medical Genetics, 54:269-277, Nov 2017. URL: https://doi.org/10.1136/jmedgenet-2016-104100, doi:10.1136/jmedgenet-2016-104100. This article has 19 citations and is from a domain leading peer-reviewed journal.

8. (moysesoliveira2018inactivationofammecr1 pages 4-6): Mariana Moysés-Oliveira, Giuliana Giannuzzi, Richard J. Fish, Jill A. Rosenfeld, Florence Petit, Maria de Fatima Soares, Leslie Domenici Kulikowski, Adriana Di-Battista, Malú Zamariolli, Fan Xia, Thomas Liehr, Nadezda Kosyakova, Gianna Carvalheira, Michael Parker, Eleanor G. Seaby, Sarah Ennis, Rodney D. Gilbert, R. Tanner Hagelstrom, Maria L. Cremona, Wenhui L. Li, Alka Malhotra, Anjana Chandrasekhar, Denise L. Perry, Ryan J. Taft, Julie McCarrier, Donald G. Basel, Joris Andrieux, Taiza Stumpp, Fernanda Antunes, Gustavo José Pereira, Marguerite Neerman-Arbez, Vera Ayres Meloni, Margaret Drummond-Borg, Maria Isabel Melaragno, and Alexandre Reymond. Inactivation of ammecr1 is associated with growth, bone, and heart alterations. Human Mutation, 39:281-291, Feb 2018. URL: https://doi.org/10.1002/humu.23373, doi:10.1002/humu.23373. This article has 20 citations and is from a domain leading peer-reviewed journal.

9. (andreoletti2017ammecr1asingle pages 6-7): Gaia Andreoletti, Eleanor G Seaby, Jennifer M Dewing, Ita O'Kelly, Katherine Lachlan, Rodney D Gilbert, and Sarah Ennis. Ammecr1: a single point mutation causes developmental delay, midface hypoplasia and elliptocytosis. Journal of Medical Genetics, 54:269-277, Nov 2017. URL: https://doi.org/10.1136/jmedgenet-2016-104100, doi:10.1136/jmedgenet-2016-104100. This article has 19 citations and is from a domain leading peer-reviewed journal.

10. (andreoletti2017ammecr1asingle pages 7-8): Gaia Andreoletti, Eleanor G Seaby, Jennifer M Dewing, Ita O'Kelly, Katherine Lachlan, Rodney D Gilbert, and Sarah Ennis. Ammecr1: a single point mutation causes developmental delay, midface hypoplasia and elliptocytosis. Journal of Medical Genetics, 54:269-277, Nov 2017. URL: https://doi.org/10.1136/jmedgenet-2016-104100, doi:10.1136/jmedgenet-2016-104100. This article has 19 citations and is from a domain leading peer-reviewed journal.

11. (andreoletti2017ammecr1asingle pages 8-8): Gaia Andreoletti, Eleanor G Seaby, Jennifer M Dewing, Ita O'Kelly, Katherine Lachlan, Rodney D Gilbert, and Sarah Ennis. Ammecr1: a single point mutation causes developmental delay, midface hypoplasia and elliptocytosis. Journal of Medical Genetics, 54:269-277, Nov 2017. URL: https://doi.org/10.1136/jmedgenet-2016-104100, doi:10.1136/jmedgenet-2016-104100. This article has 19 citations and is from a domain leading peer-reviewed journal.

12. (andreoletti2017ammecr1asingle pages 1-2): Gaia Andreoletti, Eleanor G Seaby, Jennifer M Dewing, Ita O'Kelly, Katherine Lachlan, Rodney D Gilbert, and Sarah Ennis. Ammecr1: a single point mutation causes developmental delay, midface hypoplasia and elliptocytosis. Journal of Medical Genetics, 54:269-277, Nov 2017. URL: https://doi.org/10.1136/jmedgenet-2016-104100, doi:10.1136/jmedgenet-2016-104100. This article has 19 citations and is from a domain leading peer-reviewed journal.

13. (andreoletti2017ammecr1asingle pages 3-3): Gaia Andreoletti, Eleanor G Seaby, Jennifer M Dewing, Ita O'Kelly, Katherine Lachlan, Rodney D Gilbert, and Sarah Ennis. Ammecr1: a single point mutation causes developmental delay, midface hypoplasia and elliptocytosis. Journal of Medical Genetics, 54:269-277, Nov 2017. URL: https://doi.org/10.1136/jmedgenet-2016-104100, doi:10.1136/jmedgenet-2016-104100. This article has 19 citations and is from a domain leading peer-reviewed journal.

14. (koene2022hearinglosscleft pages 4-5): Saskia Koene, Jeroen Knijnenburg, Mariette J. V. Hoffer, Fleur Zwanenburg, Monique C. Haak, Heiko Locher, Edward S. A. van Beelen, Gijs W. E. Santen, and Liselotte J. C. Rotteveel. Hearing loss, cleft palate, and congenital hip dysplasia in female carriers of an intragenic deletion of ammecr1. American Journal of Medical Genetics. Part a, 188:1578-1582, Jan 2022. URL: https://doi.org/10.1002/ajmg.a.62669, doi:10.1002/ajmg.a.62669. This article has 5 citations and is from a peer-reviewed journal.

15. (koene2022hearinglosscleft pages 3-4): Saskia Koene, Jeroen Knijnenburg, Mariette J. V. Hoffer, Fleur Zwanenburg, Monique C. Haak, Heiko Locher, Edward S. A. van Beelen, Gijs W. E. Santen, and Liselotte J. C. Rotteveel. Hearing loss, cleft palate, and congenital hip dysplasia in female carriers of an intragenic deletion of ammecr1. American Journal of Medical Genetics. Part a, 188:1578-1582, Jan 2022. URL: https://doi.org/10.1002/ajmg.a.62669, doi:10.1002/ajmg.a.62669. This article has 5 citations and is from a peer-reviewed journal.

16. (andreoletti2017ammecr1asingle pages 4-5): Gaia Andreoletti, Eleanor G Seaby, Jennifer M Dewing, Ita O'Kelly, Katherine Lachlan, Rodney D Gilbert, and Sarah Ennis. Ammecr1: a single point mutation causes developmental delay, midface hypoplasia and elliptocytosis. Journal of Medical Genetics, 54:269-277, Nov 2017. URL: https://doi.org/10.1136/jmedgenet-2016-104100, doi:10.1136/jmedgenet-2016-104100. This article has 19 citations and is from a domain leading peer-reviewed journal.

17. (andreoletti2017ammecr1asingle pages 6-6): Gaia Andreoletti, Eleanor G Seaby, Jennifer M Dewing, Ita O'Kelly, Katherine Lachlan, Rodney D Gilbert, and Sarah Ennis. Ammecr1: a single point mutation causes developmental delay, midface hypoplasia and elliptocytosis. Journal of Medical Genetics, 54:269-277, Nov 2017. URL: https://doi.org/10.1136/jmedgenet-2016-104100, doi:10.1136/jmedgenet-2016-104100. This article has 19 citations and is from a domain leading peer-reviewed journal.

18. (andreoletti2017ammecr1asingle pages 8-9): Gaia Andreoletti, Eleanor G Seaby, Jennifer M Dewing, Ita O'Kelly, Katherine Lachlan, Rodney D Gilbert, and Sarah Ennis. Ammecr1: a single point mutation causes developmental delay, midface hypoplasia and elliptocytosis. Journal of Medical Genetics, 54:269-277, Nov 2017. URL: https://doi.org/10.1136/jmedgenet-2016-104100, doi:10.1136/jmedgenet-2016-104100. This article has 19 citations and is from a domain leading peer-reviewed journal.

19. (moysesoliveira2018inactivationofammecr1 pages 6-8): Mariana Moysés-Oliveira, Giuliana Giannuzzi, Richard J. Fish, Jill A. Rosenfeld, Florence Petit, Maria de Fatima Soares, Leslie Domenici Kulikowski, Adriana Di-Battista, Malú Zamariolli, Fan Xia, Thomas Liehr, Nadezda Kosyakova, Gianna Carvalheira, Michael Parker, Eleanor G. Seaby, Sarah Ennis, Rodney D. Gilbert, R. Tanner Hagelstrom, Maria L. Cremona, Wenhui L. Li, Alka Malhotra, Anjana Chandrasekhar, Denise L. Perry, Ryan J. Taft, Julie McCarrier, Donald G. Basel, Joris Andrieux, Taiza Stumpp, Fernanda Antunes, Gustavo José Pereira, Marguerite Neerman-Arbez, Vera Ayres Meloni, Margaret Drummond-Borg, Maria Isabel Melaragno, and Alexandre Reymond. Inactivation of ammecr1 is associated with growth, bone, and heart alterations. Human Mutation, 39:281-291, Feb 2018. URL: https://doi.org/10.1002/humu.23373, doi:10.1002/humu.23373. This article has 20 citations and is from a domain leading peer-reviewed journal.

20. (poreau2019xq22.3q23microdeletionharboring pages 4-4): Brice Poreau, Francis Ramond, Radu Harbuz, Véronique Satre, Claire Barro, Claire Vettier, Véronique Adouard, Julien Thevenon, Pierre‐Simon Jouk, Charles Coutton, Renaud Touraine, and Klaus Dieterich. Xq22.3q23 microdeletion harboring tmem164 and ammecr1 genes: two case reports confirming a recognizable phenotype with short stature, midface hypoplasia, intellectual delay, and elliptocytosis. American Journal of Medical Genetics Part A, 179:650-654, Apr 2019. URL: https://doi.org/10.1002/ajmg.a.61057, doi:10.1002/ajmg.a.61057. This article has 7 citations.

## Artifacts

- [Edison artifact artifact-00](Midface_Hypoplasia_Hearing_Impairment_Elliptocytosis_And_Nephrocalcinosis-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 4 |
| Resolved | 4 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 4 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 30 |
| Resolved | 29 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 0 |
| Terms whose name was checked | 2 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 2 |

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0010985` (obsolete Gonosomal inheritance) (1 mention) - replaced by `HP:0000005`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0010985` (1 mention) - the report calls it "X-linked inheritance"; HP calls it **obsolete Gonosomal inheritance**
- `GO:0005634` (3 mentions) - the report calls it "GO: nucleus"; GO calls it **nucleus**

29 of 30 terms resolved to a current term; the rest could not be looked up either way.
