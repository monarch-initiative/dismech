---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-10-13T19:42:59.664412'
end_time: '2026-10-13T20:13:28.399561'
duration_seconds: 1828.74
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: EGLN1-related Erythrocytosis and Pheochromocytoma/Paraganglioma Predisposition
  mondo_id: MONDO:1060184
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 43
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 14
  on_topic: 6
  validator_version: 0.3.0
term_validation:
  total_terms: 2
  verified: 2
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:1060184
    reported_labels:
    - if available
    ontology_label: EGLN1-related erythrocytosis and pheochromocytoma/paraganglioma
      predisposition
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** EGLN1-related Erythrocytosis and Pheochromocytoma/Paraganglioma Predisposition
- **MONDO ID:** MONDO:1060184 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **EGLN1-related Erythrocytosis and Pheochromocytoma/Paraganglioma Predisposition** covering all of the
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
- **Disease Name:** EGLN1-related Erythrocytosis and Pheochromocytoma/Paraganglioma Predisposition
- **MONDO ID:** MONDO:1060184 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **EGLN1-related Erythrocytosis and Pheochromocytoma/Paraganglioma Predisposition** covering all of the
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


# EGLN1-related erythrocytosis and pheochromocytoma/paraganglioma predisposition

**Evidence scope.** This is a very rare, germline *EGLN1* (PHD2)–associated condition in which erythrocytosis can precede a pheochromocytoma or paraganglioma (PPGL). The clearest directly examined human example is the recurrent abdominal paraganglioma reported by Ladroue and colleagues in 2008. Most *EGLN1*-related erythrocytosis cases have **not** been reported to develop tumors. Consequently, findings for *all* familial erythrocytosis type 3 (ECYT3) cases, or for PPGLs of other genotypes, must not be entered as measured frequencies or outcomes for this narrower dual-phenotype condition. The evidence below distinguishes a **human case**, **other human cohorts**, **experimental models**, and **general PPGL guidance**. (ladroue2008phd2mutationand pages 1-2, ladroue2008phd2mutationand pages 2-4, wilson2016erythrocytosisdueto pages 6-7)

## 1. Disease information and identifiers

*EGLN1* encodes prolyl hydroxylase domain protein 2, an oxygen-dependent regulator of hypoxia-inducible factors (HIFs). Impaired regulation can cause increased red-cell production; exceptionally, a carrier also develops a neural-crest-derived PPGL. Useful names include **PHD2-related erythrocytosis with paraganglioma**, **EGLN1-related PPGL–polycythemia**, and, for the broader erythrocytosis phenotype, **familial erythrocytosis type 3/ECYT3**. “Polycythemia” in the older case literature means erythrocytosis here, **not** necessarily JAK2-positive polycythemia vera. (ladroue2008phd2mutationand pages 1-2, ladroue2008phd2mutationand pages 2-4, OpenTargets Search: familial erythrocytosis,paraganglioma-EGLN1)

The requested **MONDO:1060184** is provisionally recorded as the supplied identifier; it could not be independently verified against a current MONDO release in the available evidence. The distinguishable broader ECYT3 entry is **MONDO:0012353**. The available evidence does not establish a separate OMIM, Orphanet, MeSH, ICD-10, or ICD-11 identifier specific to the combined phenotype. These should remain *unverified*, rather than substituting the codes for polycythemia vera or for an unrelated PPGL syndrome. This report synthesizes published, aggregated disease-level literature and one identifiable published patient; it is **not** an individual’s EHR extract. (ladroue2008phd2mutationand pages 2-4, OpenTargets Search: familial erythrocytosis,paraganglioma-EGLN1)

## 2. Etiology, risk, protection, and environment

The established initiating factor is a **heterozygous germline *EGLN1* variant that impairs PHD2 activity**. For the original tumor-associated patient, the variant is **c.1121A>G, p.(His374Arg)**; analysis of his paraganglioma showed loss of heterozygosity involving the wild-type allele, providing case-level evidence for an additional, acquired tumor event. Heterozygous *EGLN1* variants cause erythrocytosis in other families, but a molecular finding in an erythrocytosis patient does not by itself establish PPGL risk for that particular allele. A review identified **two** PHD2-substitution carriers with paragangliomas, one also reported to have pheochromocytoma; this is a count of *reported cases*, **not** a penetrance estimate. (ladroue2008phd2mutationand pages 2-4, ladroue2008phd2mutationand pages 6-7, wilson2016erythrocytosisdueto pages 6-7)

A first-degree relative of a carrier of a **confirmed pathogenic germline** variant may inherit that variant; autosomal-dominant transmission is supported for familial PHD2-associated erythrocytosis, while the original tumor-associated proband was the only family member reported to have erythrocytosis or tumor. Tumor penetrance, variant-specific risk, genetic anticipation, founder effects, carrier frequency, and a role for consanguinity or germline mosaicism **cannot be quantified for this syndrome**. Other oxygen-sensing genes, notably *VHL* and *EPAS1*, belong in the **differential diagnosis**, not in a list of proven modifier genes for *EGLN1* disease. (wilson2016erythrocytosisdueto pages 7-8, ladroue2008phd2mutationand pages 2-4)

Low oxygen exposure, smoking, sleep-disordered breathing, and other acquired causes can independently increase hematocrit and complicate interpretation; a 2024 cohort noted different severity between two brothers carrying the same *EGLN1* VUS, one of whom smoked, but did **not** establish a causal gene–smoking interaction. No environmental toxin, infection, diet, protective allele, vaccine, or lifestyle intervention has been demonstrated to prevent *EGLN1*-associated PPGL. Claims about high-altitude adaptation should not be transferred to the rare tumor-predisposition variant without allele-specific evidence. (doma2024utilityofnextgeneration pages 4-6, wilson2016erythrocytosisdueto pages 7-8)

## 3. Phenotypes and suggested HPO annotations

**Direct case evidence is more informative than percentages.** At first evaluation in **1988, age 30**, the index man had an erythrocyte count of **6.2 million/mm³**, hematocrit **61.6%**, and hemoglobin **20.2 g/dL**; oxygen saturation was **96.5%** and measured erythropoietin (EPO) **18 mU/mL**. Bone marrow showed erythroid hyperplasia without fibrosis, and erythroid colonies were EPO-dependent. His abdominal para-aortic paraganglioma was recognized at approximately **age 43**; recurrence was subsequently investigated and resected. EPO measured **48 mU/mL before** the second operation and **32 mU/mL eight days afterward**, but EPO mRNA was *not detected in the tumor*. Thus, elevated circulating EPO must not automatically be interpreted as proof that the tumor secretes EPO. (ladroue2008phd2mutationand pages 1-2, ladroue2008phd2mutationand pages 2-4)

| Phenotype/type | Onset, course, and severity supported by evidence | HPO term suggestion; frequency and quality-of-life qualification |
|---|---|---|
| Erythrocytosis; hematologic sign/laboratory abnormality | Persistent from young adulthood in the index case; hematocrit 61.6% initially. Broader PHD2 erythrocytosis is often described as moderate, with EPO generally low or normal. | **Erythrocytosis** and **increased hemoglobin concentration/increased hematocrit**: select the current HPO labels and verify their identifiers before import. Fatigue or hyperviscosity effects are plausible but **not quantitatively measured for this syndrome**. (ladroue2008phd2mutationand pages 2-4, wilson2016erythrocytosisdueto pages 7-8) |
| Abdominal paraganglioma; tumor manifestation | In the index case, approximately age 43, para-aortic, surgically removed, subsequently recurrent; the initial main tumor measured **3.5 × 3.5 cm**, with additional **13- and 8-mm** nodules. | **Paraganglioma**; **abdominal paraganglioma** if an exact HPO term exists. Case-level recurrence is established; carrier-level occurrence is unknown. (ladroue2008phd2mutationand pages 2-4) |
| Pheochromocytoma; tumor manifestation | Reported concurrently in **one of the two** PHD2 tumor-associated patients summarized by a review; detailed onset and denominator of all carriers are unavailable. | **Pheochromocytoma**. Do not enter “50%” as penetrance: 1/2 refers only to the selected tumor reports. (wilson2016erythrocytosisdueto pages 6-7) |
| Hypertension; clinical sign | Mild hypertension was treated in the original patient. Catecholamine-driven episodic symptoms are possible in PPGL generally, but **not established as frequent in this genotype**. | **Hypertension**. Individual-level severity and quality-of-life impact have not been measured systematically. (ladroue2008phd2mutationand pages 1-2, garciacarbonero2021multidisciplinarypracticeguidelines pages 15-17) |
| Thrombosis; possible complication | A review notes a sagittal-sinus thrombosis with a PHD2 substitution elsewhere; it must **not** be assigned to the Ladroue patient or treated as a frequency for the combined syndrome. | Annotate thrombosis only against the applicable, separately verified case and HPO term. (wilson2016erythrocytosisdueto pages 7-8) |

The original tumor had **Zellballen** histology, chromogranin-A-positive chief cells, and S100-positive sustentacular cells. These are pathology findings for that tumor, not a unique immunohistochemical diagnostic signature of *EGLN1*. No disease-specific behavioral phenotype, EQ-5D/SF-36 score, symptom-frequency distribution, or validated severity scale was identified. (ladroue2008phd2mutationand pages 2-4)

## 4. Genetic and molecular information

***EGLN1*/PHD2 is the causal gene.** The best documented dual-phenotype allele, **c.1121A>G; p.(His374Arg)**, is a **germline missense** change involving a conserved catalytic-region residue; experimental assays show reduced function and HIF stabilization. The original tumor additionally had **somatic loss of the wild-type allele**. This is stronger functional evidence than an untested rare missense call, but a current ACMG/AMP classification and a current gnomAD allele frequency for this precise allele were **not independently verified** here and should not be invented. The available papers do not establish a disease-specific recurrent large structural rearrangement, aneuploidy, or chromosomal-microarray signature. (ladroue2008phd2mutationand pages 2-4, ladroue2008phd2mutationand pages 6-7, welander2011geneticsandclinical pages 7-8)

**Variant interpretation must be phenotype-specific.** A 2024 study of **40 patients with otherwise idiopathic erythrocytosis** detected two candidate heterozygous *EGLN1* changes, **c.1072C>T/p.(Pro358Ser)** in two brothers and **c.1124A>G/p.(Glu375Gly)** in one other individual. Both remained **variants of uncertain significance**; the report did not establish PPGL in these carriers. A separate 2024 cohort of **118 sporadic erythrocytosis patients** reported *EGLN1* findings, frequently alongside variants in other genes. These are **ascertainment-selected erythrocytosis cohorts, not estimates of syndrome prevalence or cancer penetrance**. No validated *EGLN1*-specific modifier locus, epigenetic marker, tumor metabolomic signature, single-cell atlas, spatial-transcriptomic profile, or CRISPR therapeutic screen was established by the retrieved patient evidence. (doma2024utilityofnextgeneration pages 4-6, benetti2024coexistenceofmultiple pages 6-7)

For a knowledge base, annotate **HGNC-approved symbol *EGLN1*** and PHD2 protein; verify the current numeric HGNC, NCBI Gene, transcript, ClinVar accession/classification, and population-frequency fields against their live records **before assigning identifiers**. Record **germline variant** and **tumor-acquired LOH** as distinct evidence items. The additional *EGLN2*/PHD1 case reported in the broader PPGL–polycythemia literature must not be re-labeled an *EGLN1* case. (ladroue2008phd2mutationand pages 2-4, welander2015geneticalterationsin pages 58-61, garciacarbonero2021multidisciplinarypracticeguidelines pages 10-11)

## 5. Environmental and lifestyle information

There is no identified infectious agent, transmissible exposure, occupation, or established toxin that causes this Mendelian condition. Smoking or hypoxia may create **additional acquired erythrocytosis** and affect diagnostic measurements, but are not proven initiating lesions for *EGLN1*-related tumors. Routine cardiovascular risk reduction and evaluation of acquired hypoxia are reasonable clinical measures, **not demonstrated genotype-specific protection**. (doma2024utilityofnextgeneration pages 4-6, wilson2016erythrocytosisdueto pages 7-8)

## 6. Mechanism and pathophysiology

**Ordered causal chain; evidentiary status is explicit:**

1. **Germline *EGLN1* p.(His374Arg) leads to** impaired PHD2 oxygen-sensing/prolyl-hydroxylase activity (**demonstrated for the original variant in cell assays**). (ladroue2008phd2mutationand pages 6-7, ladroue2008phd2mutationand pages 2-4)
2. **Reduced PHD2-dependent HIF-α hydroxylation leads to** less efficient pVHL recognition, ubiquitination, and proteasomal degradation, **resulting in** HIF-α stabilization (**established pathway; mutant-cell effects demonstrated**). Oxygen, iron and 2-oxoglutarate are relevant PHD cosubstrates. (ladroue2008phd2mutationand pages 1-2, ladroue2008phd2mutationand pages 6-7, jucht2024phd13oxygensensors pages 12-13)
3. **In EPO-regulating tissues, enhanced HIF signaling leads to** increased erythropoietic drive and ultimately **results in erythrocytosis** (**HIF-2α/EPO tissue connection strongly supported by conditional mice; the exact source of EPO in the original patient was not proved**). EPO-dependent marrow erythropoiesis was observed; the original tumor was negative for EPO mRNA. (ladroue2008phd2mutationand pages 2-4, jucht2024phd13oxygensensors pages 7-8)
4. **Tumor branch:** a subsequently acquired **loss of the remaining wild-type *EGLN1* allele leads to** more profound local loss of PHD2 regulation (**tumor LOH demonstrated**); consequent persistent pseudohypoxic signaling **may contribute to** paraganglionic-cell survival, altered differentiation, and tumor formation (**tumor-forming link is an inference, not a proven complete causal pathway in that individual**). (ladroue2008phd2mutationand pages 6-7, ladroue2008phd2mutationand pages 2-4, jucht2024phd13oxygensensors pages 12-13)
5. **Tumor growth leads to** an abdominal paraganglioma and potential recurrence (**observed**). A catecholamine-secreting tumor **could lead to** hypertension or crises, but secretion and causal attribution of the index patient’s mild hypertension must not be assumed. (ladroue2008phd2mutationand pages 1-2, ladroue2008phd2mutationand pages 2-4, garciacarbonero2021multidisciplinarypracticeguidelines pages 15-17)

The original mutant protein accumulated less efficiently than wild type in transfected cells, and its defective reporter activity persisted after expression was adjusted; at matched protein amounts, wild-type PHD2 reporter activity was approximately **2.5-fold** that of His374Arg for HIF-2α, with a comparable HIF-1α finding. A 2024 synthesis of rodent deletions reports HIF-2α-dependent EPO production and erythrocytosis after conditional PHD2 loss. Developmental, tyrosine-hydroxylase-lineage PHD2 deletion yields an abnormal, pseudohypoxic adrenal-medullary phenotype, whereas adult deletion did not reproduce that pattern; this does **not** establish a faithful mouse model of a human *EGLN1* PPGL. (ladroue2008phd2mutationand pages 6-7, jucht2024phd13oxygensensors pages 7-8, jucht2024phd13oxygensensors pages 12-13)

**Suggested annotations, subject to identifier verification:** GO biological processes **cellular response to hypoxia**, **protein hydroxylation**, **regulation of HIF-mediated transcription**, and **erythrocyte differentiation**; GO cellular components **cytosol**, **nucleus**, and **proteasome** for the relevant steps. Suggested cell types are **renal EPO-producing interstitial fibroblast-like cells**, **erythroid progenitor cells**, and **paraganglionic/chromaffin cells**; map these to exact **CL** IDs after checking the current ontology rather than assuming one CL term covers all paraganglionic populations. Candidate **ChEBI** annotations are molecular oxygen, iron(II), 2-oxoglutarate, and erythropoietin-related entities as appropriate; EPO itself is a protein, **not** a small-molecule metabolite. *SDHx*-associated succinate accumulation and hypermethylation are **other-genotype mechanisms**, not demonstrated *EGLN1*-tumor findings. (ladroue2008phd2mutationand pages 1-2, jucht2024phd13oxygensensors pages 7-8, zhikrivetskaya2017molecularmarkersof pages 6-7)

## 7. Anatomical structures affected

The **blood and hematopoietic system** are directly affected by erythrocytosis. The index tumor involved **extra-adrenal para-aortic paraganglionic tissue**; the kidneys’ EPO-regulating interstitium and bone-marrow erythroid precursors are mechanistically relevant, with kidney-cell attribution informed substantially by model organisms rather than patient biopsy. A separate reported carrier also had an **adrenal-medullary pheochromocytoma**. Suggested UBERON mappings are **blood**, **bone marrow**, **kidney**, **adrenal medulla**, and an appropriately verified **abdominal paraganglion** term; do not code every carrier as having all these tumor sites. The para-aortic location establishes an abdominal site, but a general bilateral or unilateral tendency cannot be estimated. Subcellular annotation should distinguish PHD2-dependent hydroxylation from downstream nuclear HIF transcription and proteasomal degradation. (ladroue2008phd2mutationand pages 2-4, wilson2016erythrocytosisdueto pages 6-7, ladroue2008phd2mutationand pages 1-2, jucht2024phd13oxygensensors pages 7-8)

## 8. Temporal development

The original patient’s persistent erythrocytosis was recognized at **30 years** and the abdominal tumor at approximately **43 years**, demonstrating that a hematologic presentation may precede detectable PPGL by years. Tumor recurrence was suspected in **2003**, corroborated by **¹³¹I-MIBG imaging in 2004**, and treated with a second resection. No standardized age-of-onset distribution, presymptomatic stages, progression rate, spontaneous remission probability, or critical developmental window has been established for human carriers. In experimental mice, timing of PHD2 deletion changes the adrenal phenotype, but it does **not** supply a human surveillance-onset age. Erythrocytosis may persist after tumor removal; tumor excision is not presumed to correct the underlying germline defect. (ladroue2008phd2mutationand pages 1-2, ladroue2008phd2mutationand pages 2-4, jucht2024phd13oxygensensors pages 12-13)

## 9. Inheritance and population

Familial PHD2-related erythrocytosis generally fits **autosomal-dominant** inheritance, with apparently isolated germline cases also reported. Importantly, inheritance of an *EGLN1* variant and development of a PPGL are **different endpoints**: the precise penetrance of the latter is unknown. No reliable **incidence, prevalence per 100,000, sex ratio, ancestry distribution, founder effect, or population carrier frequency** was identified for the combined syndrome. General-PPGL estimates such as approximately **2 cases per million per year** describe **all genotypes together** and cannot be entered as *EGLN1*-syndrome incidence. Likewise, the 2024 40-person idiopathic-erythrocytosis cohort and 118-person erythrocytosis cohort cannot estimate population prevalence. (wilson2016erythrocytosisdueto pages 7-8, ladroue2008phd2mutationand pages 2-4, doma2024utilityofnextgeneration pages 4-6, benetti2024coexistenceofmultiple pages 6-7)

## 10. Diagnosis and screening

**Clinical work-up.** Confirm persistent absolute erythrocytosis with repeated CBC, hematocrit, and—where needed—red-cell-mass assessment. Measure serum EPO and assess oxygenation and acquired causes; exclude JAK2-associated polycythemia vera, and consider hemoglobin electrophoresis/oxygen-affinity testing and a congenital erythrocytosis panel. A **normal EPO result does not exclude PHD2-related erythrocytosis**: the published review counted **21 normal, four elevated, and two low** EPO results among its reviewed PHD2 cases, with others unknown. The original case had EPO-dependent erythroid colonies, without evidence that its tumor produced EPO. (wilson2016erythrocytosisdueto pages 7-8, ladroue2008phd2mutationand pages 2-4)

If a PPGL is suspected, use **plasma-free or urine-fractionated metanephrines**, interpreted with attention to sampling conditions and interfering factors; consider additional biochemistry according to tumor phenotype. Localize a biochemically or clinically suspected lesion with **CT or MRI**, and choose functional imaging, such as MIBG or somatostatin-receptor PET, according to clinical purpose and tumor characteristics. Histology confirms tumor identity after appropriately planned surgery; unprepared biopsy of a possible functional PPGL is not an appropriate substitute for biochemical and imaging assessment. Routine ECG/cardiac evaluation is directed by blood pressure, symptoms, and perioperative risk rather than being a diagnostic test for the genotype. (garciacarbonero2021multidisciplinarypracticeguidelines pages 13-15, mercadoasis2018pheochromocytomaagenetic pages 6-10, garciacarbonero2021multidisciplinarypracticeguidelines pages 15-17)

**Genetic testing.** A germline next-generation-sequencing panel is generally more informative than testing *EGLN1* alone when erythrocytosis plus PPGL is unexplained. Include *EGLN1*, *EPAS1*, *VHL*, and other erythrocytosis and PPGL genes according to the differential; confirm clinically relevant variants and classify them under current ACMG/AMP criteria with segregation and functional evidence as available. Clinical-exome sequencing or WES/WGS can help when a well-designed panel is unrevealing or a structural/atypical lesion is suspected, but a negative assay does not exclude variants it does not detect. CMA, karyotyping, FISH, mitochondrial-genome assays, and repeat-expansion testing are **not routine tests for this single-gene presentation**. RNA, proteomic, metabolomic, or methylation testing is **not established as a clinical diagnostic test specific to this syndrome**. Genotype-directed testing of relatives is appropriate after identifying a **pathogenic or likely pathogenic** familial variant; a VUS alone should not be used as a definitive predictive result. (garciacarbonero2021multidisciplinarypracticeguidelines pages 10-11, doma2024utilityofnextgeneration pages 4-6, ladroue2008phd2mutationand pages 2-4, cascon2023geneticbasesof pages 6-8)

**Differential diagnosis.** Consider acquired hypoxia or EPO-producing lesions; JAK2-positive polycythemia vera; *EPOR*-related primary familial erythrocytosis; high-affinity hemoglobin and *BPGM*-related conditions; and *VHL*-, *EPAS1*-, or other hypoxia-pathway disorders. In particular, **EPAS1/HIF-2α-associated PPGL–polycythemia**, which may involve somatic mosaic variants and somatostatinomas, should not be merged with germline *EGLN1* disease. Other hereditary PPGL genes, particularly *SDHx*, remain relevant even when erythrocytosis has an independent cause. (wilson2016erythrocytosisdueto pages 7-8, welander2015geneticalterationsin pages 58-61, doma2024utilityofnextgeneration pages 4-6, garciacarbonero2021multidisciplinarypracticeguidelines pages 10-11)

## 11. Prognosis and outcomes

There are **no defensible genotype-specific five- or ten-year survival, mortality, life-expectancy, metastasis-risk, thrombosis-risk, disability, or quality-of-life estimates** for the combined disorder. The index patient’s tumor recurred and was resected again; that is evidence of possible recurrence, not a cohort-level recurrence rate. Likewise, the prognosis of *SDHB*- or *SDHA*-related PPGL must not be assigned to *EGLN1*. High hematocrit, hypertension, functional-tumor complications, recurrence, and possible thrombotic complications warrant clinical assessment, but no validated *EGLN1*-specific prognostic biomarker or risk model is available. (ladroue2008phd2mutationand pages 2-4, wilson2016erythrocytosisdueto pages 6-7, garciacarbonero2021multidisciplinarypracticeguidelines pages 18-19)

## 12. Treatment and current implementation

**Manage each manifestation, rather than claiming a proven genotype-curative therapy.**

* **Erythrocytosis:** hematology-directed venesection/phlebotomy was used in the index case, initially targeting hematocrit **below 45%**. That is **one patient’s regimen, not an evidence-based universal target** for hereditary PHD2 erythrocytosis or a justification for automatically applying polycythemia-vera treatment rules. Evaluate symptoms, thrombosis history, iron status, and individual risk when considering repeat phlebotomy or aspirin. No *EGLN1*-specific aspirin efficacy, response percentage, or pharmacogenomic rule was found. Suggested NCIT intervention concepts, pending exact code verification: **phlebotomy**, **aspirin therapy** when independently indicated. (ladroue2008phd2mutationand pages 1-2, wilson2016erythrocytosisdueto pages 7-8)
* **Localized PPGL:** complete resection is generally the potentially curative tumor treatment. For a pheochromocytoma or **functional** paraganglioma, multidisciplinary guidance recommends **7–14 days of preoperative adrenergic blockade**; a beta blocker, if required, is added **only after alpha blockade**. Examples are doxazosin or phenoxybenzamine for alpha blockade. The original patient underwent two abdominal tumor operations. Suggested NCIT concepts: **paraganglioma resection**, **adrenalectomy** when anatomically indicated, **alpha-adrenergic blockade**, and **beta-adrenergic blockade**; verify term identifiers. (garciacarbonero2021multidisciplinarypracticeguidelines pages 15-17, ladroue2008phd2mutationand pages 2-4)
* **Advanced PPGL:** systemic treatment is selected by disease course, tumor imaging, and specialist assessment. A later development, **belzutifan**, inhibits HIF-2α and was approved in **May 2025** for eligible patients aged **12 years or older** with locally advanced unresectable or metastatic PPGL; a cited overall PPGL trial summary reports **26% objective response in 72 patients**, **not an *EGLN1*-specific response rate**. ClinicalTrials.gov [**NCT04924075**](https://clinicaltrials.gov/study/NCT04924075), first posted **11 June 2021**, studies belzutifan across several advanced-tumor cohorts including PPGL; its registry does not establish efficacy in confirmed *EGLN1* carriers. Belzutifan can cause anemia and hypoxia, relevant considerations in any patient with an erythrocytosis background. Radionuclide or other systemic therapies are likewise **general advanced-PPGL options**, not validated *EGLN1*-directed treatments. Suggested NCIT concepts: **HIF-2α inhibitor therapy** and **radiopharmaceutical therapy**, with exact codes to verify. (ghosh2025updateonsystemic pages 9-11, NCT04924075 chunk 1, garciacarbonero2021multidisciplinarypracticeguidelines pages 17-18)

No disease-specific gene replacement, editing, antisense, cell therapy, checkpoint inhibitor, rehabilitation protocol, or combination regimen with proven benefit was identified. HIF–PHD inhibitors used for **anemia** would act in the opposite mechanistic direction from correcting PHD2-deficient erythrocytosis and are **not** a treatment for this disease. (jucht2024phd13oxygensensors pages 12-13, ladroue2008phd2mutationand pages 6-7)

## 13. Prevention and surveillance

**Primary prevention:** no intervention can prevent inheritance or is proved to prevent PPGL in a carrier. Genetic counseling supports cascade testing and informed reproductive planning when a familial pathogenic variant has been established; prenatal or preimplantation testing is a case-specific counseling matter, not a population-screening program. There is no pertinent vaccine, antimicrobial prophylaxis, or neonatal screening program. **Secondary prevention:** investigate newly identified erythrocytosis and possible tumor symptoms, and consider individualized tumor surveillance for a confirmed pathogenic-variant carrier. The original investigators specifically recommended stringent follow-up, but they did not establish an *EGLN1*-specific starting age, scan interval, or measured screening benefit. **Tertiary prevention:** control hematologic or hemodynamic problems and surveil for recurrent tumor after treatment. (ladroue2008phd2mutationand pages 6-7, ladroue2008phd2mutationand pages 2-4, cascon2023geneticbasesof pages 6-8)

As **extrapolation from general hereditary-PPGL guidance**, long-term review can include symptoms, blood pressure, and metanephrines; imaging is tailored to suspected or biochemically silent disease. Published multidisciplinary guidelines recommend **at least ten years** after resection for PPGL in general and **lifelong individualized follow-up** for hereditary PPGL. Their imaging interval of **every 2–3 years** in some silent-tumor circumstances is **not an *EGLN1*-validated protocol**; SDHx-specific pediatric starting ages must not be imported as such. (garciacarbonero2021multidisciplinarypracticeguidelines pages 18-19, jhawar2022newinsightson pages 6-7)

## 14. Other species and naturally occurring disease

The reported dual-phenotype patients are **human (*Homo sapiens*; NCBI Taxon 9606)**. *Egln1/PHD2* is evolutionarily conserved and is studied in mouse (*Mus musculus*; NCBI Taxon 10090). No independently confirmed naturally occurring, ortholog-variant-defined **erythrocytosis plus PPGL syndrome in another species**, affected breed or VBO identifier, veterinary prevalence, or cross-species transmission was found. It is **not infectious and has no zoonotic route**. A paraganglioma with erythrocytosis in another animal would not by itself establish an *EGLN1* ortholog disorder; the genotype would need confirmation. Exact ortholog NCBI Gene IDs should be verified before import. (ladroue2008phd2mutationand pages 6-7, jucht2024phd13oxygensensors pages 12-13)

## 15. Experimental models and limitations

**Human cells/in vitro:** transfected human 293T/HEK-293 cells expressing His374Arg PHD2 demonstrate reduced mutant protein accumulation and impaired suppression of HIF-responsive reporters. This directly assays the allele but cannot reproduce the inherited hematologic course or spontaneous tumor formation. **Mouse genetic models:** induced or tissue-restricted *Egln1* deletion increases EPO and erythrocytosis; conditional adrenal-medullary deletion produces HIF-2α-dependent developmental/pseudohypoxic changes. Global null, conditional, and heterozygous models have different biological consequences, and a complete experimental knockout should **not** be equated with the original human heterozygous missense allele. The reviewed adrenal model establishes a tumor-relevant molecular state, **not** necessarily a bona fide recurrent PPGL. MGI/IMSR allele and stock identifiers, zebrafish or other models, and patient-derived organoids/iPSCs require independent validation before database annotation. (ladroue2008phd2mutationand pages 6-7, jucht2024phd13oxygensensors pages 7-8, jucht2024phd13oxygensensors pages 12-13)

## Selected exact abstract evidence and publication links

* **Human case — Ladroue et al., *New England Journal of Medicine*, 18 December 2008**, “PHD2 mutation and congenital erythrocytosis with paraganglioma.” The paper’s summary states: **“We describe a patient with erythrocytosis and recurrent paraganglioma who carries a newly discovered PHD2 mutation.”** It adds: **“we demonstrate loss of heterozygosity of PHD2 in the tumor.”** [DOI: 10.1056/NEJMoa0806277](https://doi.org/10.1056/NEJMoa0806277). A PMID for this paper was **not confirmed from the accessed record** and is intentionally not guessed. (ladroue2008phd2mutationand pages 1-2)
* **Human case/review — Wilson et al., *Case Reports in Hematology*, February 2016**: its abstract states, **“Two patients with PHD2 substitution mutations were found to have paraganglioma and one of these patients had a concurrent pheochromocytoma.”** [DOI: 10.1155/2016/6373706](https://doi.org/10.1155/2016/6373706). This is a **review-derived case count**, not population statistics. (wilson2016erythrocytosisdueto pages 1-2)
* **Human cohort — Doma et al., *Frontiers in Medicine*, September 2024**: the abstract reports **“40 patients with idiopathic erythrocytosis”** and describes **p.(Pro358Ser)** and **p.(Glu375Gly)** as *EGLN1* **variants of uncertain significance**. [DOI: 10.3389/fmed.2024.1440712](https://doi.org/10.3389/fmed.2024.1440712). This is **not** a PPGL-incidence study. (doma2024utilityofnextgeneration pages 4-6)
* **Experimental-model review — Jucht and Scholz, *Pflügers Archiv*, March 2024**: the abstract identifies PHD1–3 as **“Fe2+- and 2-oxoglutarate-dependent dioxygenase[s]”** that hydroxylate HIF-α. [DOI: 10.1007/s00424-024-02944-x](https://doi.org/10.1007/s00424-024-02944-x). (jucht2024phd13oxygensensors pages 12-13, jucht2024phd13oxygensensors pages 7-8)
* **Clinical guidance — Garcia-Carbonero et al., *Clinical & Translational Oncology*, May 2021**: provides multidisciplinary PPGL diagnostic, perioperative, treatment, and follow-up guidance; **its recommendations are not a validated *EGLN1*-specific protocol**. [DOI: 10.1007/s12094-021-02622-9](https://doi.org/10.1007/s12094-021-02622-9). (garciacarbonero2021multidisciplinarypracticeguidelines pages 13-15, garciacarbonero2021multidisciplinarypracticeguidelines pages 15-17, garciacarbonero2021multidisciplinarypracticeguidelines pages 18-19)

**Knowledge-base caution:** No independently checked numeric HPO/GO/CL/UBERON/ChEBI/NCIT codes, OMIM/Orphanet mappings, current ClinVar classification, gnomAD frequency, or primary-paper PMID are supplied above. The *concept labels* are annotation suggestions; assign numeric ontology identifiers only after live ontology/database verification. Where the literature consists of a small number of reports, enter observations as **case-level evidence with their citation and ascertainment**, not as disease-wide frequency, penetrance, or prognosis. (ladroue2008phd2mutationand pages 2-4, wilson2016erythrocytosisdueto pages 6-7, doma2024utilityofnextgeneration pages 4-6)

References

1. (ladroue2008phd2mutationand pages 1-2): Charline Ladroue, Romain Carcenac, Michel Leporrier, Sophie Gad, Claire Le Hello, Françoise Galateau-Salle, Jean Feunteun, Jacques Pouysségur, Stéphane Richard, and Betty Gardie. Phd2 mutation and congenital erythrocytosis with paraganglioma. The New England journal of medicine, 359 25:2685-92, Dec 2008. URL: https://doi.org/10.1056/nejmoa0806277, doi:10.1056/nejmoa0806277. This article has 251 citations and is from a highest quality peer-reviewed journal.

2. (ladroue2008phd2mutationand pages 2-4): Charline Ladroue, Romain Carcenac, Michel Leporrier, Sophie Gad, Claire Le Hello, Françoise Galateau-Salle, Jean Feunteun, Jacques Pouysségur, Stéphane Richard, and Betty Gardie. Phd2 mutation and congenital erythrocytosis with paraganglioma. The New England journal of medicine, 359 25:2685-92, Dec 2008. URL: https://doi.org/10.1056/nejmoa0806277, doi:10.1056/nejmoa0806277. This article has 251 citations and is from a highest quality peer-reviewed journal.

3. (wilson2016erythrocytosisdueto pages 6-7): Rachel Wilson, Nausheen Syed, and Prabodh Shah. Erythrocytosis due to phd2 mutations: a review of clinical presentation, diagnosis, and genetics. Case Reports in Hematology, 2016:1-8, Feb 2016. URL: https://doi.org/10.1155/2016/6373706, doi:10.1155/2016/6373706. This article has 31 citations.

4. (OpenTargets Search: familial erythrocytosis,paraganglioma-EGLN1): Open Targets Query (familial erythrocytosis,paraganglioma-EGLN1, 16 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

5. (ladroue2008phd2mutationand pages 6-7): Charline Ladroue, Romain Carcenac, Michel Leporrier, Sophie Gad, Claire Le Hello, Françoise Galateau-Salle, Jean Feunteun, Jacques Pouysségur, Stéphane Richard, and Betty Gardie. Phd2 mutation and congenital erythrocytosis with paraganglioma. The New England journal of medicine, 359 25:2685-92, Dec 2008. URL: https://doi.org/10.1056/nejmoa0806277, doi:10.1056/nejmoa0806277. This article has 251 citations and is from a highest quality peer-reviewed journal.

6. (wilson2016erythrocytosisdueto pages 7-8): Rachel Wilson, Nausheen Syed, and Prabodh Shah. Erythrocytosis due to phd2 mutations: a review of clinical presentation, diagnosis, and genetics. Case Reports in Hematology, 2016:1-8, Feb 2016. URL: https://doi.org/10.1155/2016/6373706, doi:10.1155/2016/6373706. This article has 31 citations.

7. (doma2024utilityofnextgeneration pages 4-6): Saša Anžej Doma, Nika Kraljić, Aleša Kristan, Nataša Debeljak, Aleš Maver, Tadej Pajič, and Irena Preložnik Zupan. Utility of next-generation sequencing in identifying congenital erythrocytosis in patients with idiopathic erythrocytosis. Frontiers in Medicine, Sep 2024. URL: https://doi.org/10.3389/fmed.2024.1440712, doi:10.3389/fmed.2024.1440712. This article has 3 citations.

8. (garciacarbonero2021multidisciplinarypracticeguidelines pages 15-17): R. Garcia-Carbonero, F. Matute Teresa, E. Mercader-Cidoncha, M. Mitjavila-Casanovas, M. Robledo, I. Tena, C. Alvarez-Escola, M. Arístegui, M. R. Bella-Cueto, C. Ferrer-Albiach, and F. A. Hanzu. Multidisciplinary practice guidelines for the diagnosis, genetic counseling and treatment of pheochromocytomas and paragangliomas. Clinical & Translational Oncology, 23:1995-2019, May 2021. URL: https://doi.org/10.1007/s12094-021-02622-9, doi:10.1007/s12094-021-02622-9. This article has 226 citations and is from a peer-reviewed journal.

9. (welander2011geneticsandclinical pages 7-8): Jenny Welander, Peter Söderkvist, and Oliver Gimm. Genetics and clinical characteristics of hereditary pheochromocytomas and paragangliomas. Endocrine-related cancer, 18 6:R253-76, Dec 2011. URL: https://doi.org/10.1530/erc-11-0170, doi:10.1530/erc-11-0170. This article has 475 citations and is from a domain leading peer-reviewed journal.

10. (benetti2024coexistenceofmultiple pages 6-7): Andrea Benetti, MD Irene Bertozzi, PhD, Giulio Ceolotto, Irene Cortella, Daniela Regazzo, Giacomo Biagetti, Elisabetta Cosi, and Prof Maria Luigia Randi, MD. Coexistence of multiple gene variants in some patients with erythrocytoses. Mediterranean Journal of Hematology and Infectious Diseases, 16:e2024021, Feb 2024. URL: https://doi.org/10.4084/mjhid.2024.021, doi:10.4084/mjhid.2024.021. This article has 6 citations.

11. (welander2015geneticalterationsin pages 58-61): Jenny Welander. Genetic alterations in pheochromocytoma and paraganglioma. Linköping University Medical Dissertations, Apr 2015. URL: https://doi.org/10.3384/diss.diva-114806, doi:10.3384/diss.diva-114806. This article has 1 citations.

12. (garciacarbonero2021multidisciplinarypracticeguidelines pages 10-11): R. Garcia-Carbonero, F. Matute Teresa, E. Mercader-Cidoncha, M. Mitjavila-Casanovas, M. Robledo, I. Tena, C. Alvarez-Escola, M. Arístegui, M. R. Bella-Cueto, C. Ferrer-Albiach, and F. A. Hanzu. Multidisciplinary practice guidelines for the diagnosis, genetic counseling and treatment of pheochromocytomas and paragangliomas. Clinical & Translational Oncology, 23:1995-2019, May 2021. URL: https://doi.org/10.1007/s12094-021-02622-9, doi:10.1007/s12094-021-02622-9. This article has 226 citations and is from a peer-reviewed journal.

13. (jucht2024phd13oxygensensors pages 12-13): Agnieszka E. Jucht and Carsten C. Scholz. Phd1-3 oxygen sensors in vivo—lessons learned from gene deletions. Pflugers Archiv, 476:1307-1337, Mar 2024. URL: https://doi.org/10.1007/s00424-024-02944-x, doi:10.1007/s00424-024-02944-x. This article has 13 citations.

14. (jucht2024phd13oxygensensors pages 7-8): Agnieszka E. Jucht and Carsten C. Scholz. Phd1-3 oxygen sensors in vivo—lessons learned from gene deletions. Pflugers Archiv, 476:1307-1337, Mar 2024. URL: https://doi.org/10.1007/s00424-024-02944-x, doi:10.1007/s00424-024-02944-x. This article has 13 citations.

15. (zhikrivetskaya2017molecularmarkersof pages 6-7): Svetlana O. Zhikrivetskaya, Anastasiya V. Snezhkina, Andrew R. Zaretsky, Boris Y. Alekseev, Anatoly V. Pokrovsky, Alexander L. Golovyuk, Nataliya V. Melnikova, Oleg A. Stepanov, Dmitry V. Kalinin, Alexey A. Moskalev, George S. Krasnov, Alexey A. Dmitriev, and Anna V. Kudryavtseva. Molecular markers of paragangliomas/pheochromocytomas. Oncotarget, 8:25756-25782, Feb 2017. URL: https://doi.org/10.18632/oncotarget.15201, doi:10.18632/oncotarget.15201. This article has 53 citations.

16. (garciacarbonero2021multidisciplinarypracticeguidelines pages 13-15): R. Garcia-Carbonero, F. Matute Teresa, E. Mercader-Cidoncha, M. Mitjavila-Casanovas, M. Robledo, I. Tena, C. Alvarez-Escola, M. Arístegui, M. R. Bella-Cueto, C. Ferrer-Albiach, and F. A. Hanzu. Multidisciplinary practice guidelines for the diagnosis, genetic counseling and treatment of pheochromocytomas and paragangliomas. Clinical & Translational Oncology, 23:1995-2019, May 2021. URL: https://doi.org/10.1007/s12094-021-02622-9, doi:10.1007/s12094-021-02622-9. This article has 226 citations and is from a peer-reviewed journal.

17. (mercadoasis2018pheochromocytomaagenetic pages 6-10): Leilani B. Mercado-Asis, Katherine I. Wolf, Ivana Jochmanova, and David Taïeb. Pheochromocytoma: a genetic and diagnostic update. Endocrine Practice, 24:78-90, Jan 2018. URL: https://doi.org/10.4158/ep-2017-0057, doi:10.4158/ep-2017-0057. This article has 85 citations and is from a peer-reviewed journal.

18. (cascon2023geneticbasesof pages 6-8): Alberto Cascón, Bruna Calsina, María Monteagudo, Sara Mellid, Alberto Díaz-Talavera, Maria Currás-Freixes, and Mercedes Robledo. Genetic bases of pheochromocytoma and paraganglioma. Journal of Molecular Endocrinology, Apr 2023. URL: https://doi.org/10.1530/jme-22-0167, doi:10.1530/jme-22-0167. This article has 91 citations and is from a peer-reviewed journal.

19. (garciacarbonero2021multidisciplinarypracticeguidelines pages 18-19): R. Garcia-Carbonero, F. Matute Teresa, E. Mercader-Cidoncha, M. Mitjavila-Casanovas, M. Robledo, I. Tena, C. Alvarez-Escola, M. Arístegui, M. R. Bella-Cueto, C. Ferrer-Albiach, and F. A. Hanzu. Multidisciplinary practice guidelines for the diagnosis, genetic counseling and treatment of pheochromocytomas and paragangliomas. Clinical & Translational Oncology, 23:1995-2019, May 2021. URL: https://doi.org/10.1007/s12094-021-02622-9, doi:10.1007/s12094-021-02622-9. This article has 226 citations and is from a peer-reviewed journal.

20. (ghosh2025updateonsystemic pages 9-11): Imani Ghosh, Olivia Benson, Jorge H. Hernandez-Felix, Frank I. Lin, Karel Pacak, and Jaydira del Rivero. Update on systemic therapies for metastatic/unresectable pheochromocytomas and paragangliomas and future directions. Cancers, 17:3702, Nov 2025. URL: https://doi.org/10.3390/cancers17223702, doi:10.3390/cancers17223702. This article has 6 citations.

21. (NCT04924075 chunk 1):  Belzutifan/MK-6482 for the Treatment of Advanced Pheochromocytoma/Paraganglioma (PPGL), Pancreatic Neuroendocrine Tumor (pNET), Von Hippel-Lindau (VHL) Disease-Associated Tumors, Advanced Gastrointestinal Stromal Tumor (wt GIST), or Solid Tumors With HIF-2α Related Genetic Alterations (MK-6482-015). Merck Sharp & Dohme LLC. 2021. ClinicalTrials.gov Identifier: NCT04924075

22. (garciacarbonero2021multidisciplinarypracticeguidelines pages 17-18): R. Garcia-Carbonero, F. Matute Teresa, E. Mercader-Cidoncha, M. Mitjavila-Casanovas, M. Robledo, I. Tena, C. Alvarez-Escola, M. Arístegui, M. R. Bella-Cueto, C. Ferrer-Albiach, and F. A. Hanzu. Multidisciplinary practice guidelines for the diagnosis, genetic counseling and treatment of pheochromocytomas and paragangliomas. Clinical & Translational Oncology, 23:1995-2019, May 2021. URL: https://doi.org/10.1007/s12094-021-02622-9, doi:10.1007/s12094-021-02622-9. This article has 226 citations and is from a peer-reviewed journal.

23. (jhawar2022newinsightson pages 6-7): Sakshi Jhawar, Yasuhiro Arakawa, Suresh Kumar, Diana Varghese, Yoo Sun Kim, Nitin Roper, Fathi Elloumi, Yves Pommier, Karel Pacak, and Jaydira Del Rivero. New insights on the genetics of pheochromocytoma and paraganglioma and its clinical implications. Cancers, 14:594, Jan 2022. URL: https://doi.org/10.3390/cancers14030594, doi:10.3390/cancers14030594. This article has 101 citations.

24. (wilson2016erythrocytosisdueto pages 1-2): Rachel Wilson, Nausheen Syed, and Prabodh Shah. Erythrocytosis due to phd2 mutations: a review of clinical presentation, diagnosis, and genetics. Case Reports in Hematology, 2016:1-8, Feb 2016. URL: https://doi.org/10.1155/2016/6373706, doi:10.1155/2016/6373706. This article has 31 citations.

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 14 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 2 |
| Resolved | 2 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:1060184` (2 mentions) - the report calls it "if available"; MONDO calls it **EGLN1-related erythrocytosis and pheochromocytoma/paraganglioma predisposition**