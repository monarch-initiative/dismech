---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-09-17T14:19:20.918085'
end_time: '2026-09-17T14:25:19.174721'
duration_seconds: 358.26
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Hypercholanemia Familial 2
  mondo_id: MONDO:0031003
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 18
reference_validation:
  total_references: 5
  verified: 5
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 5
  on_topic: 5
  validator_version: 0.2.1
term_validation:
  total_terms: 32
  verified: 32
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 17
  labels_matching: 5
  labels_mismatched: 10
  mislabelled_terms:
  - term_id: HP:0012113
    reported_labels:
    - Hypercholanemia
    ontology_label: Abnormal circulating creatine concentration
  - term_id: HP:0012111
    reported_labels:
    - Abnormal serum bile acid concentration
    ontology_label: Abnormality of circulating glucocorticoid level
  - term_id: HP:0006564
    reported_labels:
    - Neonatal cholestatic jaundice
    ontology_label: Fluctuating hepatomegaly
  - term_id: HP:0012023
    reported_labels:
    - Vitamin D deficiency
    ontology_label: Galactosuria
  - term_id: HP:0012112
    reported_labels:
    - Abnormal bile acid profile
    ontology_label: Abnormal circulating corticosterone level
  - term_id: HP:0006560
    reported_labels:
    - Hepatic cholestasis
    ontology_label: Biliary hyperplasia
  - term_id: HP:0002599
    reported_labels:
    - Giant cell hepatitis
    ontology_label: Head titubation
  - term_id: HP:0033863
    reported_labels:
    - Hepatocellular ballooning
    ontology_label: Abnormal cortical peritubular capillary lumen morphology
  - term_id: HP:0011902
    reported_labels:
    - Vitamin K deficiency
    ontology_label: Abnormal hemoglobin
  - term_id: GO:0048029
    reported_labels:
    - bile acid transmembrane transport
    ontology_label: monosaccharide binding
  labels_variant: 2
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hypercholanemia Familial 2
- **MONDO ID:** MONDO:0031003 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hypercholanemia Familial 2** covering all of the
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

# Familial Hypercholanemia 2 (NTCP Deficiency): Comprehensive Disease Characterization

Familial hypercholanemia 2 (FHCA2), also known as sodium taurocholate cotransporting polypeptide (NTCP) deficiency, is an autosomal recessive inborn error of bile acid metabolism caused by biallelic loss-of-function variants in the SLC10A1 gene, which encodes the hepatocellular bile acid transporter NTCP.[2][7][11] The disorder is characterized biochemically by persistently and often markedly elevated serum levels of conjugated bile acids from infancy, with a distinctive bile acid profile dominated by glycine- and taurine-conjugated species.[2][3][7] Clinically, most individuals are asymptomatic or have only mild manifestations, although some neonates and infants present with transient cholestatic jaundice, hepatomegaly, and fat-soluble vitamin deficiency, particularly of vitamins D and K, which may predispose to decreased bone mineral density and coagulopathy.[2][7][9][13] NTCP deficiency has emerged as a paradigmatic example of a relatively benign monogenic disruption of a major transporter in the enterohepatic circulation of bile acids, with human and mouse data indicating that auxiliary transporters (notably organic anion transporting polypeptides) can partially compensate for the loss of NTCP-mediated sodium-dependent bile acid uptake.[6][7][16] At the same time, the condition is mechanistically and clinically important because NTCP is also the high-affinity entry receptor for hepatitis B and D viruses and the pharmacologic target of the HBV/HDV entry inhibitor bulevirtide, linking FHCA2 to antiviral therapeutics and host–virus interactions in the hepatobiliary system.[9][15][18] The following report provides an in-depth, structured synthesis of current knowledge on FHCA2/NTCP deficiency, integrating genetic, molecular, clinical, diagnostic, and epidemiologic evidence to support knowledge base curation and ontology-based annotation.

## 1. Disease Information

### 1.1 Definition and Overview

Familial hypercholanemia 2 (FHCA2) is an autosomal recessive metabolic disorder defined by persistent hypercholanemia—markedly elevated plasma levels of predominantly conjugated bile salts—caused by inherited deficiency of the sodium taurocholate cotransporting polypeptide (NTCP).[2][7][11] NTCP, encoded by the SLC10A1 gene on chromosome 14q24.1, is a basolateral hepatocyte transporter that mediates sodium-dependent uptake of glycine- and taurine-conjugated bile acids from portal and systemic blood into hepatocytes, thereby playing a central role in the enterohepatic circulation of bile salts.[6][7][15] NTCP deficiency disrupts this uptake step, causing accumulation of conjugated bile acids in the systemic circulation while leaving bile acid synthesis and intestinal signaling relatively intact, as evidenced by normal plasma levels of the bile acid synthetic marker 7α-hydroxy-4-cholesten-3-one (C4) and fibroblast growth factor 19 (FGF19) in the first reported patient.[7][16] Unlike classical cholestatic liver diseases, FHCA2 often lacks overt cholestasis, pruritus, or progressive liver dysfunction, and in many individuals the condition is detected only through biochemical testing showing extreme hypercholanemia.[2][7][9]

The disease has been recognized both as a specific clinical entity and as a genetic subtype of familial hypercholanemia, distinguished from FHCA1 (caused by TJP2 mutations) and from bile acid conjugation defects due to BAAT mutations.[1][2][5] ClinVar and OMIM designate the condition as “Hypercholanemia, familial, 2” with the alternative name “NTCP deficiency,” emphasizing that the defining lesion is the loss of NTCP function.[10][11] The clinical spectrum ranges from asymptomatic adults with biochemically isolated hypercholanemia to infants presenting with cholestatic jaundice that resolves, leaving persistent elevation of serum bile acids as the main residual abnormality.[2][7][12][13][17] The relatively mild phenotype, despite profound biochemical derangement, has prompted considerable interest in FHCA2 as an example of human “knockout” of a major transporter and has informed the safety profile of drugs that pharmacologically inhibit NTCP.[6][15][18]

### 1.2 Key Identifiers and Ontology Placement

FHCA2 is catalogued in multiple rare disease and ontology systems. OMIM lists the entity as “HYPERCHOLANEMIA, FAMILIAL 2; FHCA2” under phenotype MIM number 619256, with causative variants in SLC10A1 (gene MIM 182396).[2][11] ClinVar entries for the canonical pathogenic variant c.800C>T (p.Ser267Phe) in SLC10A1 explicitly associate this variant with “Hypercholanemia, familial, 2” and provide cross-references to OMIM and MONDO.[10][11] The MONDO ontology assigns the identifier MONDO:0031003 to this condition under the name “hypercholanemia, familial, 2,” reflecting its classification as a Mendelian disorder of bile acid metabolism. MalaCards similarly lists “Hypercholanemia, Familial, 2” as a genetic metabolic disease with autosomal recessive inheritance.[2]

Although Orphanet has historically grouped familial hypercholanemias under broader bile acid metabolism defects, more recent ontological releases such as ORDO recognize familial hypercholanemia as a distinct rare disease category within bile acid synthesis and transport disorders.[8] At a higher level, FHCA2 falls under MeSH and ICD categories related to inborn errors of metabolism and cholestatic liver disease, although disease-specific ICD-10 or ICD-11 codes have not yet been widely adopted, and clinical coding typically uses more generic cholestasis or hyperbilirubinemia codes in symptomatic infants. From a Mondo ontology perspective, FHCA2 is a child of “primary bile acid metabolic disorder” and is aligned with HPO terms such as “Hypercholanemia” (HP:0012113) and “Abnormal serum bile acid concentration” (HP:0012111) for phenotype-level modeling.

### 1.3 Synonyms and Alternative Names

The disease is known by several synonyms in the clinical and research literature, reflecting its dual identity as both a familial hypercholanemia and a transporter deficiency. ClinVar explicitly lists “NTCP deficiency” as a synonym of “Hypercholanemia, familial, 2,” and multiple case reports and reviews refer to the condition as “sodium taurocholate cotransporting polypeptide (SLC10A1) deficiency” or simply “NTCP deficiency.”[7][11][14][16][17] MalaCards lists “Familial hypercholanemia-2” and “FHCA2” as official synonyms, underscoring its classification alongside FHCA1.[2] In some publications, particularly those focused on genetics, the disease is described as “SLC10A1 deficiency” or “SLC10A1-related hypercholanemia,” highlighting the gene-based etiology.[7][9][12]

At the biochemical level, the disorder has been described as “conjugated hypercholanemia without a clear clinical phenotype,” a phrase used in the title and abstract of the seminal report by Vaz et al. on the first NTCP-deficient patient.[7][16] This terminology emphasizes the discrepancy between the severe biochemical abnormality (extreme elevation of conjugated bile salts) and the relatively mild or absent clinical manifestations. However, as more pediatric cases have been described, some authors have highlighted that transient cholestatic jaundice and fat-soluble vitamin deficiency can be clinically significant in infancy, suggesting that the “asymptomatic” descriptor applies primarily to long-term outcomes rather than early life presentation.[12][13][17]

### 1.4 Data Sources and Evidence Base

Knowledge about FHCA2/NTCP deficiency is derived primarily from aggregated disease-level resources, case reports, and small case series, rather than large epidemiological cohorts or EHR-based studies. The core clinical and mechanistic description comes from the first identified NTCP-deficient patient reported by Vaz et al. in 2015, which established NTCP deficiency as “a new inborn error of metabolism with a relatively mild clinical phenotype.”[7][16] Subsequent pediatric case reports from East Asia, particularly China and Japan, have expanded the phenotype by describing infants with cholestatic jaundice who were later found to have homozygous SLC10A1 variants, most commonly the c.800C>T (p.Ser267Phe) allele.[12][13][17] A population-based study of homozygous p.Ser267Phe individuals in East Asia further characterized the biochemical and hormonal consequences of this variant and confirmed persistent hypercholanemia in otherwise asymptomatic adults.[9]

Aggregated databases such as MalaCards and ClinVar synthesize these primary data sources, classifying SLC10A1 variants by pathogenicity and linking them to FHCA2.[2][10][11] Metabolomic profiling studies of serum bile acids in NTCP-deficient children and adults, including recent work analyzing bile acid patterns to distinguish NTCP deficiency from other cholestatic liver diseases, provide more detailed biochemical characterization and support robust diagnostic criteria.[3] Overall, the evidence base is heavily weighted toward human clinical and biochemical observations, supplemented by mechanistic studies in Slc10a1 knockout mice and structural studies of NTCP as an HBV/HDV receptor.[6][15] There is currently no large registry or longitudinal cohort dedicated specifically to FHCA2, and natural history data are pieced together from follow-up of individual case reports and small series.[7][13][16][17]

## 2. Etiology

### 2.1 Primary Causal Factors: SLC10A1 Variants and NTCP Deficiency

The primary causal factor in FHCA2 is biallelic loss-of-function mutation in the SLC10A1 gene, which encodes the Na\(^+\)-taurocholate cotransporting polypeptide (NTCP).[2][7][11] SLC10A1 is a member of the solute carrier family 10 and is expressed predominantly in hepatocytes, where its protein product NTCP localizes to the basolateral (sinusoidal) membrane and mediates sodium-dependent uptake of conjugated bile acids, including taurocholic acid and glycocholic acid, from the portal circulation into the liver.[6][7][15] The central etiologic mechanism of FHCA2 is therefore a transporter deficiency: genetic disruption of NTCP activity results in diminished hepatic clearance of conjugated bile salts from plasma, leading to systemic hypercholanemia.[7][9][16]

The first identified patient with NTCP deficiency carried a homozygous nonsynonymous point mutation c.755G>A in SLC10A1, resulting in an arginine-to-histidine substitution at position 252 (p.Arg252His, R252H).[7][16] Functional studies showed that this missense mutation caused a marked reduction in taurocholic acid uptake, and immunofluorescence and surface biotinylation experiments demonstrated that the mutant protein was virtually absent from the plasma membrane, indicating that loss of cell-surface NTCP expression underlies the functional defect.[7] In the words of Vaz et al., “functional studies showed that this mutation resulted in a markedly reduced uptake activity of taurocholic acid… [and] immunofluorescence studies and surface biotinylation experiments demonstrated that the mutant protein is virtually absent from the plasma membrane.”[7][16] This established R252H as a pathogenic loss-of-function allele and confirmed that NTCP is the main import system for conjugated bile salts into hepatocytes in humans.[7][16]

Subsequent reports, particularly from East Asia, identified another recurrent pathogenic variant, c.800C>T, which leads to a serine-to-phenylalanine substitution at position 267 (p.Ser267Phe, S267F).[2][9][10][11][12][13][17] In a 30‑month-old Chinese boy with FHCA2, Deng et al. found homozygosity for c.800C>T, and ClinVar now lists this variant as pathogenic for “Hypercholanemia, familial, 2,” with the alternative disease name “NTCP deficiency.”[10][11] The same variant was detected in multiple pediatric patients with NTCP deficiency in China and Japan, often in the context of neonatal cholestasis or coexisting citrin deficiency, indicating that S267F is a major disease-causing allele in East Asian populations.[12][13][17] A population-based study showed that individuals homozygous for p.Ser267Phe have persistent hypercholanemia composed mainly of conjugated bile acids and are prone to vitamin D deficiency and subtle alterations in sex hormones and blood lipids, confirming the phenotypic impact of this variant even in ostensibly healthy adults.[9]

Together, these findings support a model in which homozygous or compound heterozygous loss-of-function variants in SLC10A1 are necessary and sufficient to cause NTCP deficiency and FHCA2, with R252H and S267F as the best-characterized examples.[7][9][10][11][16] The disease is therefore etiologically monogenic at the locus level but allelically heterogeneous, with different missense mutations converging on the shared outcome of reduced NTCP activity and membrane expression. All known pathogenic variants are germline and inherited in autosomal recessive fashion; somatic variants in SLC10A1 have not been implicated in FHCA2.[2][7][10][11]

### 2.2 Genetic Risk Factors: Causal and Susceptibility Variants

The principal genetic risk factors for FHCA2 are biallelic pathogenic variants in SLC10A1, with c.800C>T (p.Ser267Phe) being particularly important due to its relatively high allele frequency in East Asian populations.[2][9][11] MalaCards notes that “the s267f allele is prevalent among individuals of east asian origin,” reflecting population genetic studies that have identified this variant with appreciable frequency in East Asians but not in other ancestral groups.[2] The Sci Rep study on p.Ser267Phe homozygotes found that all homozygous individuals had persistent hypercholanemia and that homozygosity for S267F was strongly associated with elevated serum bile acids, suggesting high biochemical penetrance.[9] In that study, “all homozygous individuals had persistent hypercholanemia… homozygosity of p.Ser267Phe in SLC10A1 is associated with asymptomatic hypercholanemia,” and these individuals were noted to be prone to vitamin D deficiency and altered lipid profiles.[9]

In addition to S267F and R252H, other rare missense variants in SLC10A1 have been reported in NTCP-deficient patients, though they are less well characterized. Case series from China identifying NTCP deficiency in infants with cholestatic jaundice and persistent hypercholanemia uniformly found biallelic SLC10A1 variants, often involving S267F in homozygous state, reinforcing its importance as the major disease allele in that population.[12][13][17] ClinVar lists c.800C>T (p.Ser267Phe) as a pathogenic missense variant with germline origin and autosomal recessive inheritance, providing a curated classification based on multiple clinical submissions.[10][11]

Beyond clearly pathogenic alleles, population sequencing studies have identified additional SLC10A1 variants with reduced function, some of which may act as susceptibility alleles or modifiers. However, as emphasized in a commentary on NTCP and Slc10a1 knockout mice, “nonfunctional NTCP variants have turned up in population-based sequencing studies” and yet only a single NTCP-deficient patient with hypercholanemia was initially described, indicating that some individuals with NTCP deficiency may be normocholanemic or underdiagnosed.[6] This observation suggests that the phenotypic expression of SLC10A1 variants may be modulated by other genetic or environmental factors, though specific modifier loci have not yet been convincingly identified.

### 2.3 Environmental and Lifestyle Risk Factors

There is no evidence that environmental, dietary, or lifestyle factors cause FHCA2 in the absence of SLC10A1 variants, as the disorder is clearly an inherited inborn error of metabolism.[2][7][11] Unlike multifactorial disorders, FHCA2 does not appear to be influenced by exogenous toxins, occupational exposures, or infections in a way that would initiate disease in genetically normal individuals. However, environmental and physiologic factors can modulate the clinical manifestation of NTCP deficiency, particularly in early life.

One notable example is the interaction between NTCP deficiency and citrin deficiency, a metabolic disorder caused by mutations in SLC25A13 that produces neonatal intrahepatic cholestasis.[12][17] In three pediatric patients described by Ding et al., cholestatic jaundice in early infancy was initially attributed to citrin deficiency based on SLC25A13 variants, and NTCP deficiency was only recognized later when hypercholanemia persisted despite resolution of cholestatic jaundice, prompting SLC10A1 sequencing.[12][17] These cases illustrate how coexisting metabolic stressors in the liver can unmask or exacerbate the biochemical consequences of NTCP deficiency in infancy, even though the underlying etiology remains genetic. They also highlight that clinical presentation can be shaped by environmental factors such as diet, since specialized lactose-free and medium-chain triglyceride–enriched formulas improved cholestasis in these infants, even as hypercholanemia persisted.[12][17]

Pharmacologic inhibition of NTCP by drugs such as bulevirtide (Myrcludex B), a myristoylated HBV preS1-derived lipopeptide that binds NTCP and blocks hepatitis B and D virus entry, can induce secondary hypercholanemia that phenocopies aspects of FHCA2.[15][18] Clinical studies of bulevirtide in HBV/HDV-infected adults have documented increases in serum bile acids, reflecting on-target inhibition of NTCP-mediated bile acid uptake.[15][18] These drug-induced changes do not cause FHCA2 per se, since the genetic background remains intact, but they demonstrate that environmental exposures which transiently inactivate NTCP can interact with existing SLC10A1 variants or reveal subclinical transporter deficiency. However, data directly linking such exposures to altered disease risk or severity in genetically NTCP-deficient individuals remain sparse.

### 2.4 Protective Genetic and Environmental Factors

Protective factors for FHCA2 can be conceptualized at two levels: factors that reduce the risk of developing the biochemical phenotype in genetically at-risk individuals, and factors that mitigate clinical consequences in those with established NTCP deficiency. At present, there is no evidence of genetic variants that protect against FHCA2 by enhancing alternative bile acid uptake pathways or compensatory mechanisms in hepatocytes, though mouse studies suggest that upregulation of organic anion transporting polypeptides (OATPs) can maintain near-normal serum bile acid levels in some Slc10a1 knockout animals.[6] In these mice, approximately 70% had normal serum bile acid levels despite complete loss of Ntcp, implying that genetic or epigenetic modifiers of Oatp expression or function might confer a protective effect, but such modifiers have not been identified in humans.[6]

Clinically, environmental and medical interventions can be protective against the downstream consequences of NTCP deficiency, particularly vitamin deficiency and bone disease. Fat-soluble vitamin supplementation, notably vitamin D and vitamin K, is routinely used in pediatric NTCP-deficient patients with evidence of deficiency or prolonged prothrombin time, thereby preventing rickets and coagulopathy.[2][13][17] In the pediatric NTCP-deficient infant reported by Sun et al., supplementation with fat-soluble vitamins and liver-protective therapies led to normalization of bilirubin and transaminases, while hypercholanemia persisted, indicating that these interventions can protect against liver dysfunction and vitamin-deficiency complications even without correcting the primary transporter defect.[13] Similarly, in citrin-deficient infants with concomitant NTCP deficiency, dietary management with lactose-free, medium-chain triglyceride–rich formulas improved cholestatic jaundice and growth, reflecting the protective effect of tailored nutrition on the liver and biliary system.[12][17]

At a broader level, the absence of chronic cholestasis or progressive liver disease in most NTCP-deficient individuals suggests that the human liver possesses intrinsic protective mechanisms—such as redundant bile acid uptake pathways, canalicular secretion via BSEP, and adaptive changes in bile acid synthesis and composition—that prevent toxic accumulation of bile acids in hepatocytes despite markedly elevated systemic levels.[6][7][9][16] These protective mechanisms are likely polygenic and context-dependent and are best conceptualized as emergent properties of the bile acid homeostatic network rather than single-gene protective factors.

### 2.5 Gene–Environment Interactions

While FHCA2 is fundamentally a monogenic disorder, gene–environment interactions influence its clinical presentation and course. Coexisting liver diseases, metabolic disorders, or dietary factors can modulate the phenotype of NTCP deficiency. For instance, citrin deficiency creates a neonatal cholestatic environment in which the impact of NTCP deficiency on bile acid handling is amplified, producing more pronounced cholestatic jaundice in early infancy than might occur with NTCP deficiency alone.[12][17] As these infants are treated and the cholestatic stress resolves, residual NTCP deficiency manifests primarily as persistent hypercholanemia without ongoing cholestasis, illustrating a time-dependent interaction between genetic transporter deficiency and environmental/metabolic context.[12][17]

Similarly, infectious or inflammatory liver insults in an NTCP-deficient individual might transiently exacerbate cholestasis or liver dysfunction, although such scenarios have not yet been systematically documented. Pharmacologic NTCP inhibitors such as bulevirtide provide a controlled example of a gene–environment interaction: in a genetically NTCP-normal individual, bulevirtide binding to NTCP induces a functional deficiency analogous to FHCA2, while in a person with partial NTCP activity due to heterozygous SLC10A1 variants, drug exposure might push hepatic bile acid uptake below a critical threshold, exacerbating hypercholanemia.[15][18] However, clinical data on bulevirtide use in heterozygous or homozygous SLC10A1 variant carriers are not yet available.

In summary, SLC10A1 mutations are the primary etiologic agents of FHCA2, but environmental and metabolic factors can shape the phenotypic expression of NTCP deficiency, particularly in infancy and in the setting of coexisting liver disorders. The interaction between NTCP deficiency and other hepatic stressors underscores the importance of considering gene–environment interactions when interpreting clinical manifestations and designing management strategies.

## 3. Phenotypes

### 3.1 Overview of Clinical and Biochemical Phenotypes

The core phenotype of FHCA2/NTCP deficiency is persistent hypercholanemia, defined as markedly elevated serum concentrations of total bile acids, particularly conjugated primary bile acids such as taurocholic acid, glycocholic acid, and glycochenodeoxycholic acid.[2][3][7][9] In the first NTCP-deficient patient, total plasma bile salts reached levels up to 1,500 μM, more than 100-fold above the upper limit of normal (<16.3 μM), yet there were no clinical signs of cholestatic jaundice, pruritus, or liver dysfunction.[7][16] This biochemical phenotype corresponds to the HPO terms “Hypercholanemia” (HP:0012113) and “Abnormal serum bile acid concentration” (HP:0012111) and is present in essentially all diagnosed individuals, making it the defining feature of FHCA2.[2][3][7][9][13][17]

Clinically, the phenotype is variable and age-dependent. Most adult individuals homozygous for pathogenic SLC10A1 variants, especially p.Ser267Phe, are asymptomatic or exhibit only mild manifestations such as subclinical vitamin D deficiency or subtle deviations in sex hormones and lipids.[9] Pediatric presentations, by contrast, often involve transient cholestatic jaundice in infancy, sometimes accompanied by hepatomegaly, elevated conjugated bilirubin, mildly elevated liver transaminases, and fat-soluble vitamin deficiency.[2][12][13][17] These features align with HPO terms such as “Neonatal cholestatic jaundice” (HP:0006564), “Conjugated hyperbilirubinemia” (HP:0002908), “Hepatomegaly” (HP:0002240), and “Vitamin D deficiency” (HP:0012023). Importantly, in most cases the jaundice and liver enzyme abnormalities improve or resolve with age, while hypercholanemia persists, indicating a dissociation between biochemical and clinical manifestations over time.[2][12][13][17]

### 3.2 Age of Onset, Severity, and Progression

FHCA2 is typically a pediatric-onset disorder at the biochemical level, with elevated serum bile acids apparent from infancy.[2][3][7][12][13] MalaCards emphasizes that FHCA2 is “an autosomal recessive inborn error of metabolism characterized by persistently increased plasma levels of conjugated bile salts apparent from infancy,” and that “most patients are asymptomatic.”[2] In many cases, hypercholanemia is detected in the course of evaluating neonatal jaundice, cholestasis, or other metabolic disorders, as in the NTCP-deficient infants with concomitant citrin deficiency.[12][17] In others, particularly adults in population-based studies, hypercholanemia is discovered incidentally during routine blood tests or research assessments of bile acid profiles.[9]

Symptom severity is generally mild. In the first reported NTCP-deficient child, mild hypotonia, growth retardation, and delayed motor milestones were noted, but there were no signs of cholestatic jaundice, pruritus, or significant liver dysfunction, and growth and development eventually normalized.[7][16] In the pediatric case reported by Sun et al., a 3.3‑month-old infant presented with moderate jaundice, hepatomegaly, elevated transaminases and direct hyperbilirubinemia, and low 25‑OH vitamin D, but these abnormalities improved markedly with treatment, and by 34.3 months of age the child had normal growth and neurobehavioral development, with resolved jaundice and normalized liver function tests, despite persistent hypercholanemia.[13] Similarly, in the series of three infants with NTCP and citrin deficiency, cholestatic jaundice resolved before one year of age, while elevated total bile acids persisted.[12][17] These observations support a phenotype that is at most moderately severe in early infancy and becomes mild or subclinical thereafter.

Symptom progression in FHCA2 appears to be stable or improving rather than progressive. Long-term follow-up of the first NTCP-deficient patient showed no progression of liver disease or emergence of pruritus or cholestasis, despite sustained extreme hypercholanemia, leading the authors to conclude that NTCP deficiency “remains attenuated” over time.[16] The pediatric patient followed to nearly three years likewise showed stable or improved clinical status.[13] The adult S267F homozygotes with asymptomatic hypercholanemia reported by Hsu et al. (Sci Rep 2017) did not exhibit overt liver disease, though subtle biochemical and hormonal deviations were present.[9] Collectively, these data indicate that FHCA2 is not associated with progressive liver failure or cirrhosis in currently observed cohorts, though longer-term follow-up into later adulthood is limited.

### 3.3 Detailed Phenotypic Features and HPO Mapping

The major phenotypic domains in FHCA2 encompass biochemical abnormalities, hepatic manifestations, systemic metabolic consequences, and neurologic or developmental features.

Biochemically, persistent and often extreme hypercholanemia is universal. Serum total bile acid levels are markedly elevated, with a strong predominance of conjugated primary bile acids such as taurocholic acid (TCA), glycocholic acid (GCA), and glycochenodeoxycholic acid (GCDCA).[3][7][9] Targeted metabolomic studies in NTCP-deficient patients have shown increased total conjugated bile acids, total primary bile acids, and total secondary bile acids compared with healthy controls, with particularly elevated levels of taurocholic acid and glycochenodeoxycholic acid.[3] In one study of NTCP-deficient children, taurochenodeoxycholic acid, glycolithocholate, taurohyocholate, and tauro-α-muricholic acid were significantly increased, while glycodeoxycholic acid, glycolithocholate, and lithocholic acid were decreased compared with NTCP-deficient adults.[3] These detailed patterns correspond to HPO concepts of “Abnormal bile acid profile” (HP:0012112) and “Increased circulating conjugated bile acids,” and highlight differences between pediatric and adult phenotypes.[3]

Hepatic manifestations include transient neonatal or infantile cholestatic jaundice in a subset of patients, hepatomegaly, and mild to moderate elevation of liver transaminases.[2][12][13][17] In the pediatric NTCP-deficient infant reported by Sun et al., direct (conjugated) hyperbilirubinemia and elevated transaminases accompanied hepatomegaly and histologic evidence of hepatocyte ballooning, cholestatic multinucleate giant cells, distortion of lobular architecture, and portal tract lymphocytic infiltration.[13] These features align with HPO terms such as “Hepatic cholestasis” (HP:0006560), “Giant cell hepatitis” (HP:0002599), and “Hepatocellular ballooning” (HP:0033863), though it remains unclear whether they reflect NTCP deficiency per se or concomitant liver insults. In many NTCP-deficient individuals, particularly adults, liver enzymes and bilirubin are within normal ranges, indicating that overt hepatic injury is not a consistent feature.[7][9][16]

Systemic metabolic consequences center on fat-soluble vitamin malabsorption. MalaCards notes that “the bile acid defect can result in impaired absorption of fat-soluble vitamins, including D and K, causing decreased bone mineral density or prolonged prothrombin time (PT).”[2] In the pediatric case described by Sun et al., 25‑OH vitamin D was decreased, consistent with vitamin D deficiency, and supplementation was initiated.[13] Vitamin K deficiency, inferred from prolonged PT or clinical coagulopathy, has been reported or anticipated based on malabsorption of bile acid-dependent fat-soluble vitamins, although specific case-level data are limited.[2] These features map to HPO terms such as “Vitamin D deficiency” (HP:0012023), “Vitamin K deficiency” (HP:0011902), “Decreased bone mineral density” (HP:0004349), and “Prolonged prothrombin time” (HP:0003645). Growth retardation in early childhood, noted in the first NTCP-deficient patient, appears to be mild and reversible with age and appropriate nutritional support.[7][16]

Neurologic and developmental features are generally mild. The first NTCP-deficient child exhibited mild hypotonia, growth retardation, and delayed motor milestones, but no intellectual disability or seizures, and subsequent development was reported as normal.[7][16] The pediatric patient followed to 34.3 months showed normal anthropometric indices and neurobehavioral milestones despite early cholestasis.[13] These observations correspond to HPO terms like “Mild generalized hypotonia” (HP:0008936) and “Delayed gross motor development” (HP:0002194), though these features are not universal and may reflect non-specific effects of early-life metabolic stress and malnutrition rather than direct consequences of NTCP deficiency.

### 3.4 Laboratory Abnormalities and Bile Acid Profiles

Beyond elevated total bile acids, NTCP deficiency is characterized by distinctive bile acid profiles that can aid in diagnosis and differential diagnosis. A recent study analyzing serum bile acid profiles in NTCP-deficient children compared with healthy controls and other chronic liver disease (CLD) groups found that NTCP-deficient patients had significantly increased total conjugated bile acids, total primary bile acids, total secondary bile acids, glycocholic acid, taurocholic acid, and glycochenodeoxycholic acid.[3] Compared with NTCP-deficient adults, NTCP-deficient children had higher levels of total conjugated and total primary bile acids.[3] Notably, secondary bile acids such as lithocholic acid, deoxycholic acid, and hyodeoxycholic acid were significantly higher in children with NTCP deficiency than in other CLD groups including neonatal intrahepatic cholestasis caused by citrin deficiency (NICCD), Alagille syndrome, and biliary atresia.[3]

Ratios such as total primary bile acids to total secondary bile acids and total conjugated to total unconjugated bile acids, as well as individual bile acid species like taurocholic acid, taurodeoxycholic acid, and glycodeoxycholic acid, were found to effectively distinguish NTCP-deficient children from those with other cholestatic liver diseases.[3] The authors concluded that “serum bile acid profile analysis has an important reference value for facilitating the diagnosis and differential diagnosis of NTCP deficiency,” and that these metabolomic signatures deepen scientific understanding of bile acid profile changes in NTCP-deficient CLDs and provide clues to underlying pathogenesis.[3] These laboratory features map to LOINC concepts related to quantitative bile acid measurements and to HPO terms describing qualitative and quantitative abnormalities of serum bile acids.

### 3.5 Quality of Life Impact

Available data suggest that the quality of life impact of FHCA2 is modest, particularly beyond early childhood. Adults with NTCP deficiency identified through population studies of p.Ser267Phe homozygotes were reported to be asymptomatic, with no clinical signs of liver disease, pruritus, or significant functional impairment, despite persistent hypercholanemia.[9] In pediatric cases, early-life cholestatic jaundice, hepatomegaly, and vitamin deficiencies can transiently affect well-being, feeding, and growth, but these issues generally improve with appropriate nutritional management and supportive therapies.[12][13][17] Long-term follow-up of individual patients has not documented chronic fatigue, pruritus, or significant limitations in daily functioning attributable to NTCP deficiency.[7][13][16]

Nonetheless, subtle quality of life effects may arise from subclinical vitamin D deficiency (e.g., reduced bone mineral density or increased risk of fractures) or hormonal alterations associated with persistent hypercholanemia, and these have not yet been systematically studied using standardized tools such as SF‑36 or EQ‑5D. The potential psychosocial impact of a chronic biochemical abnormality, even if clinically mild, especially in children and their families, also warrants consideration. At present, the overall impression from case reports and series is that FHCA2/NTCP deficiency is compatible with normal growth, development, and everyday functioning, provided that fat-soluble vitamin status is monitored and corrected as needed.[7][9][13][16][17]

## 4. Genetic and Molecular Information

### 4.1 Causal Gene: SLC10A1 and NTCP

SLC10A1 encodes the sodium taurocholate cotransporting polypeptide (NTCP), a member of the solute carrier family 10 that plays a central role in hepatic bile acid uptake.[6][7][15] The SLC10A1 gene is located on chromosome 14q24.1, as indicated in ClinVar and OMIM entries for the c.800C>T (p.Ser267Phe) variant.[11] NTCP is a glycoprotein localized to the basolateral (sinusoidal) membrane of hepatocytes, where it mediates sodium-dependent uptake of conjugated bile acids from portal blood, effectively clearing approximately 80% of bile salts returning to the liver and maintaining bile acid homeostasis.[6][15] NTCP’s role in bile acid transport was established through cloning and functional expression studies in the early 1990s and subsequently reinforced by identification of NTCP-deficient humans and Slc10a1 knockout mice.[6][7][16]

In addition to its physiologic role in bile acid transport, NTCP is the high-affinity receptor for hepatitis B and D viruses (HBV and HDV), binding the viral preS1 domain and mediating viral entry into hepatocytes.[9][15] Structural work has shown that NTCP’s transmembrane architecture accommodates both bile acids and the preS1-derived antiviral drug bulevirtide, highlighting the dual functional roles of this transporter.[15] This duality makes SLC10A1 a gene of interest not only in inherited metabolic disease but also in infectious disease and pharmacology, as NTCP deficiency can theoretically influence susceptibility to HBV/HDV infection and response to NTCP-targeting drugs, although such interactions have not yet been extensively documented in FHCA2 patients.[9][15]

### 4.2 Pathogenic Variants and Functional Consequences

The best-characterized pathogenic SLC10A1 variants associated with FHCA2 are p.Arg252His (c.755G>A) and p.Ser267Phe (c.800C>T).[7][9][10][11][12][13][16][17] Both are missense variants that result in loss of NTCP function through distinct mechanisms.

The R252H variant, identified in the first NTCP-deficient patient, dramatically reduces NTCP-mediated taurocholic acid uptake and abolishes membrane localization of NTCP.[7][16] Functional studies using expression systems demonstrated markedly reduced uptake activity, and immunofluorescence plus surface biotinylation indicated that the mutant protein is virtually absent from the plasma membrane, implying defective trafficking or stability.[7] Thus, R252H can be classified as a loss-of-function missense variant with a molecular consequence best described as impaired membrane targeting and reduced transporter activity. Its pathogenicity is supported by the homozygous state in the index patient, segregation in the family, and the consistent biochemical phenotype of extreme hypercholanemia.[7][16]

The S267F variant (c.800C>T) has emerged as a major pathogenic allele in East Asian populations.[2][9][10][11][12][13][17] ClinVar classifies this variant as pathogenic for FHCA2, and OMIM lists it as a disease-causing allele at the SLC10A1 locus.[10][11] Functional studies have shown that S267F leads to reduced NTCP transport activity and altered bile acid uptake, although the exact mechanistic details (e.g., impact on membrane expression versus substrate binding) have been less extensively characterized than for R252H.[9] Hsu et al. demonstrated that homozygous S267F individuals consistently exhibit persistent hypercholanemia, with elevated conjugated bile acids including taurodeoxycholic acid (TDCA) and glycodeoxycholic acid (GDCA), indicating substantial loss of NTCP function in vivo.[9] The variant is therefore considered a loss-of-function missense allele with high biochemical penetrance.

Other SLC10A1 variants reported in NTCP-deficient patients include rare missense changes identified in East Asian cohorts, often in compound heterozygosity with S267F.[12][13][17] While detailed functional characterization of these variants is limited, their co-segregation with FHCA2 phenotypes, absence or rarity in population controls, and predicted impact on conserved residues support their classification as likely pathogenic or pathogenic under ACMG/AMP guidelines. All known disease-associated variants are germline, with no evidence for somatic SLC10A1 mutations causing FHCA2.[2][7][10][11]

From a molecular pathology perspective, NTCP deficiency is best conceptualized as a loss-of-function disease, in which reduced or absent transporter activity impairs sodium-dependent uptake of conjugated bile acids into hepatocytes. This is supported by the preserved biliary excretion machinery and bile acid synthesis and signaling, as indicated by normal C4 and FGF19 levels in NTCP-deficient patients, and by the ability of auxiliary carriers such as OATP1B1 and OATP1B3 to partially compensate.[6][7][16] There is no evidence for gain-of-function, dominant-negative, or toxic effects of SLC10A1 variants in FHCA2; heterozygous carriers are clinically and biochemically normal, and dominant inheritance has not been reported.[2][7][10][11]

### 4.3 Allele Frequency and Population Genetics

The allele frequency of SLC10A1 pathogenic variants varies considerably among populations. The c.800C>T (p.Ser267Phe) variant is particularly enriched in East Asians, where it reaches appreciable minor allele frequencies, as reflected in MalaCards’ note that “the s267f allele is prevalent among individuals of east asian origin.”[2] The Sci Rep study by Hsu et al. systematically genotyped S267F in an East Asian cohort and identified multiple homozygous individuals, all of whom had persistent hypercholanemia, highlighting both the relatively high carrier frequency and the under-recognition of NTCP deficiency in these populations.[9] Exact allele frequencies and carrier rates are best obtained from large-scale population databases such as gnomAD, but these are not explicitly detailed in the provided sources; nonetheless, the presence of numerous homozygotes in a single study suggests an allele frequency in the low-percent range in some East Asian subpopulations.[2][9]

By contrast, R252H and other rare pathogenic variants appear to be sporadic and have not been reported at significant frequencies in any population. The first NTCP-deficient patient with R252H was of non-East Asian ancestry, indicating that NTCP deficiency can arise in diverse populations through private or rare alleles.[7][16] Taken together, these data support a genetic architecture in which one common pathogenic allele (S267F) contributes substantially to disease burden in East Asia, while a multitude of rare variants underlies cases in other populations. Founder effects for S267F in specific East Asian groups are likely but have not been fully delineated.

### 4.4 Modifier Genes, Epigenetics, and Structural Variations

To date, no specific modifier genes have been definitively shown to alter the clinical severity or biochemical expression of NTCP deficiency in humans. However, studies in Slc10a1 knockout mice provide indirect evidence that variation in other bile acid transporters, particularly members of the OATP (Slco) family, may modulate the hypercholanemic phenotype.[6] In these mice, about 70% had normal serum bile acid levels despite complete absence of Ntcp, while the remaining 30% had dramatically elevated bile acids; this bimodal distribution suggests that genetic or epigenetic factors influencing alternative bile acid uptake pathways determine whether hypercholanemia manifests.[6] Although analogous human modifier loci have not been identified, plausible candidates include SLCO1B1 and SLCO1B3 (encoding OATP1B1 and OATP1B3), ABC transporters, and nuclear receptors regulating bile acid synthesis and transport (e.g., NR1H4 encoding FXR).

There is currently no evidence that epigenetic changes (DNA methylation, histone modifications) at the SLC10A1 locus or elsewhere play a primary role in FHCA2 pathogenesis. Similarly, structural variants such as large deletions, duplications, or chromosomal rearrangements involving SLC10A1 have not been reported as causes of NTCP deficiency.[2][10][11] The genetic etiology appears to be confined to point mutations and small indels, primarily missense variants that abrogate transporter function.

### 4.5 Protein Structure–Function Insights

Recent structural work on NTCP, particularly studies examining the binding of antiviral drug bulevirtide to NTCP, provides insight into how specific SLC10A1 variants might disrupt function.[15] Bulevirtide is a myristoylated peptide derived from the HBV preS1 domain that binds NTCP and blocks HBV/HDV entry into hepatocytes, and its interaction with NTCP reveals key structural features of the transporter’s substrate-binding pocket.[15][18] NTCP is a multi-pass transmembrane protein with a central cavity accommodating bile acid substrates and preS1-derived ligands, and the region around residues 252 and 267 is thought to play a role in substrate binding or conformational change.[7][9][15] Although detailed structural data specific to R252H and S267F are limited, the severe functional consequences of these variants suggest that they destabilize the transporter, alter critical interactions within the binding pocket, or impair the conformational cycle required for sodium-coupled transport.

In summary, the genetic and molecular landscape of FHCA2 is dominated by loss-of-function missense variants in SLC10A1 that abolish or severely reduce NTCP-mediated bile acid uptake. The disease provides a unique human model of complete or near-complete NTCP deficiency, with implications for understanding bile acid physiology, transporter redundancy, and antiviral drug targeting.

## 5. Environmental Information

### 5.1 Environmental and Lifestyle Contributors

FHCA2 is fundamentally a genetic disease, and there is no evidence that environmental or lifestyle factors can cause NTCP deficiency in the absence of SLC10A1 mutations.[2][7][11] Unlike cholestatic liver diseases driven by toxins, drugs, or infections, FHCA2 arises from an inborn error of bile acid transport, and environmental exposures play at most a modulatory role. Diet, physical activity, and other lifestyle factors do not appear to significantly alter the core biochemical phenotype of hypercholanemia, although they may influence secondary consequences such as vitamin D status or bone health.

That said, nutritional interventions can modify clinical manifestations in affected infants. In the series of NTCP-deficient infants with concomitant citrin deficiency, cholestatic jaundice improved with dietary management using lactose-free and medium-chain triglyceride–rich formulas.[12][17] Medium-chain triglycerides are more readily absorbed in the absence of bile acids and thus partially bypass the need for bile acid–mediated fat absorption, reducing cholestatic stress on the liver and improving growth.[12][17] While this intervention does not alter the underlying transporter defect or hypercholanemia, it demonstrates that environmental manipulations can ameliorate clinical sequelae of NTCP deficiency in early life.

### 5.2 Pharmacologic Modulation of NTCP

The most important environmental factor affecting NTCP function is exposure to drugs that inhibit NTCP, particularly bulevirtide (Myrcludex B), an HBV/HDV entry inhibitor that binds NTCP and blocks both viral entry and bile acid uptake.[15][18] Bulevirtide is a myristoylated preS1-derived lipopeptide that binds with high affinity to NTCP, inactivating it as an HBV/HDV receptor and partially inhibiting its bile acid transport function.[15][18] Clinical studies of bulevirtide in HBV/HDV-infected patients have observed increases in serum bile acids consistent with pharmacologic NTCP inhibition, effectively inducing a reversible NTCP-deficient state.[15][18] These drug-induced changes provide a human analogue to gene-based NTCP deficiency and demonstrate that chronic NTCP inhibition is generally tolerated, supporting the benign nature of FHCA2.

Other drugs, including some statins, antibiotics, and immunosuppressants, have been shown in vitro to inhibit NTCP or compete for bile acid transport, though their clinical relevance in FHCA2 patients has not been well studied.[6][15] In principle, NTCP-deficient individuals might be more sensitive to drugs that rely on NTCP for hepatic uptake or that modulate bile acid homeostasis, but specific gene–drug interactions have not been documented. Environmental toxins affecting bile acid metabolism, such as certain pesticides or endocrine-disrupting chemicals, could theoretically interact with NTCP deficiency, but no data currently support such interactions.

### 5.3 Infectious Agents and NTCP Deficiency

NTCP’s role as an entry receptor for HBV and HDV raises the question of whether NTCP deficiency modifies susceptibility to these infections.[9][15] Since NTCP is essential for HBV and HDV entry, individuals with complete NTCP deficiency due to biallelic SLC10A1 loss-of-function variants would be predicted to be resistant to infection by these viruses, at least at the level of hepatocyte entry.[15][18] However, direct evidence for reduced HBV/HDV infection rates in NTCP-deficient individuals is lacking, in part because FHCA2 is rare and screening for HBV/HDV infection in such patients has not been systematically reported. The Sci Rep study on S267F homozygotes focused on bile acids, vitamin D, and hormonal profiles and did not report HBV/HDV infection status.[9]

Nonetheless, structural and functional data firmly establish NTCP as an essential HBV/HDV receptor, and pharmacologic NTCP inhibition by bulevirtide effectively blocks viral entry and suppresses viral spread in the liver.[15][18] In a bulevirtide clinical trial protocol, the drug is described as “a 47 amino acids long, N-terminally myristoylated, HBV-L-protein derived lipopeptide” that “blocks the entry of HBV into hepatocytes by binding to and inactivating an NTCP/SLC10A1, a bile acid liver transporter serving as essential HBV and HDV entry receptor.”[18] By analogy, genetic inactivation of NTCP in FHCA2 could confer innate protection against HBV/HDV infection, though this remains a theoretical consideration pending epidemiologic data.

In summary, environmental factors play a secondary role in FHCA2, mainly by influencing clinical manifestations and interacting with NTCP function pharmacologically or via coexisting liver diseases. The primary etiologic driver remains the genetic disruption of SLC10A1.

## 6. Mechanism and Pathophysiology

### 6.1 Ordered Causal Chain from Mutation to Phenotype

The pathophysiology of FHCA2/NTCP deficiency can be described as a stepwise causal chain linking SLC10A1 mutations to clinical manifestations. Step 1: Biallelic loss-of-function variants in the SLC10A1 gene lead to reduced or absent expression and/or function of NTCP at the basolateral membrane of hepatocytes.[7][9][11][16] Step 2: Loss of NTCP function leads to markedly reduced sodium-dependent uptake of conjugated bile acids (e.g., taurocholic acid, glycocholic acid, glycochenodeoxycholic acid) from portal and systemic blood into hepatocytes.[6][7][15] Step 3: Reduced hepatic uptake of conjugated bile acids results in accumulation of these bile salts in the systemic circulation, causing persistent hypercholanemia dominated by conjugated primary bile acids.[2][3][7][9] Step 4: Accumulation of conjugated bile acids in plasma and reduced hepatocellular uptake lead to decreased replenishment of the intrahepatic and canalicular bile acid pool, potentially reducing bile acid concentrations in bile and the intestinal lumen, particularly under conditions of stress or in early infancy; this is inferred from the role of NTCP in maintaining the enterohepatic circulation and is not directly measured in patients.[6][7] Step 5: A reduced intestinal bile acid pool leads to mild impairment of bile acid–dependent fat absorption, which in turn results in decreased absorption of fat-soluble vitamins, notably vitamins D and K.[2][7][13] Step 6: Vitamin D deficiency results in decreased bone mineralization and, if severe and prolonged, rickets, while vitamin K deficiency leads to reduced production of vitamin K–dependent clotting factors and prolonged prothrombin time; these consequences are inferred from the general physiology of fat-soluble vitamin deficiency and have been variably observed in NTCP-deficient patients.[2][13] Step 7: In early infancy, coexisting cholestatic conditions (e.g., citrin deficiency) or immature compensatory mechanisms can exacerbate impaired bile acid handling, leading to transient cholestatic jaundice, hepatomegaly, and histologic changes such as hepatocyte ballooning and giant cell transformation.[12][13][17] Step 8: Over time, auxiliary bile acid transporters, particularly organic anion transporting polypeptides (OATP1B1/1B3), compensate for the loss of NTCP, maintaining sufficient hepatocellular bile acid uptake to prevent chronic cholestasis, thereby limiting clinical manifestations despite persistent hypercholanemia.[6][7][16] Throughout this chain, NTCP deficiency is upstream, while vitamin deficiency and transient cholestasis are downstream effects; the primary cell type involved is the hepatocyte, and the primary biological process perturbed is bile acid transport.

### 6.2 Molecular Pathways and Transport Systems

NTCP deficiency disrupts the enterohepatic circulation of bile acids, a tightly regulated process involving multiple transporters and signaling pathways. At the molecular level, NTCP (gene symbol SLC10A1) mediates sodium-dependent uptake of conjugated bile acids across the hepatocyte basolateral membrane, coupling the inward sodium gradient maintained by the Na\(^+\)/K\(^+\)-ATPase to bile acid transport.[6][7][15] This process corresponds to the Gene Ontology (GO) term “bile acid transmembrane transport” (GO:0048029) and is part of broader pathways for “bile acid and bile salt metabolism” catalogued in KEGG and Reactome.

When NTCP is absent or dysfunctional, as in FHCA2, alternative transporters assume a greater role in bile acid uptake. Chief among these are the organic anion transporting polypeptides OATP1B1 and OATP1B3 (encoded by SLCO1B1 and SLCO1B3), which mediate sodium-independent uptake of unconjugated and some conjugated bile acids.[6][15] Their contribution is particularly evident in Slc10a1 knockout mice, where a subset of animals maintain normal serum bile acid levels despite complete loss of Ntcp, implicating upregulated or more efficient Oatp-mediated transport.[6] In humans, the persistent hypercholanemia in NTCP-deficient individuals suggests that auxiliary transporters cannot fully compensate for the loss of NTCP, at least for conjugated bile acids, but they are sufficient to prevent severe cholestasis and liver injury.[7][9][16]

Downstream of hepatocellular uptake, bile acids are secreted into bile canaliculi via the bile salt export pump (BSEP, ABCB11) and then enter the intestine, where they facilitate micellar solubilization of dietary lipids and fat-soluble vitamins.[6][7] They are then reabsorbed via the apical sodium-dependent bile acid transporter (ASBT, SLC10A2) in the terminal ileum and return to the liver via the portal vein, completing the enterohepatic cycle. NTCP deficiency disrupts this cycle by reducing hepatic reuptake, leading to increased spillover of conjugated bile acids into the systemic circulation and altered bile acid gradients between portal and systemic compartments.[6][7][9][16] However, bile acid synthesis (as reflected by normal C4 levels) and signaling (as reflected by normal FGF19 levels) appear intact in NTCP-deficient patients, indicating that nuclear receptor pathways such as FXR-FGF19 and SHP-SREBP remain functional.[7][16]

### 6.3 Protein Dysfunction and Structural Mechanisms

At the protein level, NTCP deficiency stems from missense mutations that destabilize the transporter, impair folding, alter substrate-binding sites, or disrupt trafficking to the plasma membrane. The R252H variant leads to almost complete loss of plasma membrane NTCP, as demonstrated by immunofluorescence and surface biotinylation, suggesting that the mutation either prevents proper folding and ER exit or targets the protein for degradation.[7][16] This corresponds to a misfolding-type loss-of-function mechanism, where the protein never reaches its functional location at the basolateral membrane.

The S267F variant appears to act primarily by reducing transporter activity, as indicated by the consistent hypercholanemia in homozygotes and the association with altered bile acid profiles.[9] While detailed structural data are lacking, Ser267 likely resides in or near a transmembrane helix contributing to the substrate-binding pocket or sodium-binding sites, and substitution with a bulky hydrophobic phenylalanine may disrupt local conformation, substrate interactions, or the conformational changes required for alternating access transport. Structural analysis of NTCP in complex with bulevirtide reveals that the transporter’s binding pocket accommodates both bile acids and the HBV preS1-derived peptide, and many disease-associated residues, including those near positions 252 and 267, cluster around this region.[15] Thus, pathogenic SLC10A1 variants can be interpreted in the context of a structured, multi-pass transporter whose function depends on precise residue positioning and dynamic conformational changes.

### 6.4 Metabolic Changes and Bile Acid Profiles

The metabolic hallmark of NTCP deficiency is an altered bile acid profile characterized by elevated conjugated primary bile acids and specific changes in secondary bile acids.[3][7][9] Loss of NTCP-mediated uptake diminishes the liver’s ability to clear conjugated bile acids from the circulation, leading to their accumulation in plasma; this is particularly evident for taurocholic acid (TCA), glycocholic acid (GCA), and glycochenodeoxycholic acid (GCDCA), which are major NTCP substrates.[3][7][9] At the same time, unconjugated bile acids and some secondary bile acids display heterogeneous changes, reflecting complex interactions with intestinal bacteria, alternative uptake pathways, and feedback regulation of bile acid synthesis.[3][9]

The metabolomic study by Zhang et al. (as summarized in the provided abstract) demonstrated increased total conjugated bile acids, total primary bile acids, total secondary bile acids, and specific species such as taurocholic acid, glycocholic acid, and glycochenodeoxycholic acid in NTCP-deficient patients compared with healthy controls.[3] In NTCP-deficient children, taurochenodeoxycholic acid, glycolithocholate, taurohyocholate, and tauro-α-muricholic acid were particularly elevated, while glycodeoxycholic acid, glycolithocholate, and lithocholic acid were decreased compared with NTCP-deficient adults.[3] These differences suggest developmental changes in bile acid metabolism and gut microbiota, with children having distinct secondary bile acid profiles relative to adults.

Importantly, ratios such as total primary to total secondary bile acids and total conjugated to total unconjugated bile acids, as well as specific conjugated secondary bile acids like taurodeoxycholic acid and glycodeoxycholic acid, were found to distinguish NTCP deficiency from other cholestatic liver diseases such as NICCD, Alagille syndrome, and biliary atresia.[3] This indicates that NTCP deficiency creates a unique metabolic signature within the broader landscape of cholestatic and hypercholanemic conditions, reflecting its specific disruption of basolateral hepatic uptake rather than canalicular excretion or bile acid synthesis.

### 6.5 Immune System and Tissue Damage

Unlike many cholestatic liver diseases, NTCP deficiency does not appear to involve significant immune-mediated injury or chronic inflammation. In the first NTCP-deficient patient, liver function tests were normal, and there were no clinical signs of chronic liver damage or fibrosis.[7][16] In the pediatric case with liver biopsy, histologic findings included hepatocyte ballooning, cholestatic multinucleate giant cells, distorted lobular architecture, and portal tract lymphocytic infiltration, a pattern consistent with neonatal cholestatic hepatitis rather than a specific immunologic signature of NTCP deficiency.[13] These changes likely reflect generalized cholestatic stress and inflammation in early infancy, potentially influenced by concomitant conditions, rather than a direct effect of NTCP loss.

There is no evidence that NTCP deficiency triggers autoimmunity or immune deficiency. The primary tissue injury in FHCA2 is minimal, as indicated by the absence of progressive fibrosis, cirrhosis, or liver failure in reported patients.[7][9][13][16][17] This reinforces the concept that NTCP deficiency is a relatively benign transporter defect buffered by redundant transport pathways and adaptative mechanisms.

### 6.6 Cellular and Tissue-Level Mechanisms

The principal cell type affected in FHCA2 is the hepatocyte, corresponding to the Cell Ontology term “hepatocyte” (CL:0000182). NTCP is expressed on the basolateral membrane of hepatocytes facing the sinusoidal blood supply, in the anatomical context of the liver lobule (UBERON:0002107).[7][15] Loss of NTCP alters hepatocyte interaction with circulating bile acids, but because canalicular secretion machinery and other transporters remain intact, hepatocytes can still excrete bile acids into bile and maintain canalicular flow.

Cholangiocytes (CL:0002412) and enterocytes in the ileum (CL:0000632) are indirectly affected through altered bile acid delivery and composition. Reduced hepatic uptake and altered enterohepatic circulation may change bile acid concentrations in bile and the intestinal lumen, impacting cholangiocyte and enterocyte exposure to bile acids and possibly influencing FXR-mediated signaling pathways in the intestine and liver. However, direct evidence for cholangiocyte or enterocyte pathology in NTCP deficiency is lacking.

At the subcellular level, NTCP’s loss affects the plasma membrane compartment (GO:0005886), specifically the basolateral domain of hepatocytes. The Na\(^+\)/K\(^+\)-ATPase, which maintains the sodium gradient, remains functional, but its coupling to bile acid uptake via NTCP is diminished. Other compartments, such as the endoplasmic reticulum (ER) and lysosomes, may be involved in the processing and degradation of misfolded NTCP mutants like R252H, but these effects have not been systematically examined.

### 6.7 Multi-Omics and Advanced Technologies

To date, there are no published large-scale transcriptomic, proteomic, or multi-omics analyses specifically focused on NTCP-deficient human patients. However, insights into gene expression and regulatory networks can be inferred from studies of Slc10a1 knockout mice, which showed differential expression of bile acid transporters and metabolic genes, as well as from general bile acid homeostasis research.[6] Metabolomics, as discussed, has been the main omics approach applied directly to NTCP-deficient patients, providing detailed bile acid profiles.[3] There are no reports of single-cell RNA sequencing, spatial transcriptomics, or CRISPR-based functional genomics screens directly addressing NTCP deficiency, although NTCP (SLC10A1) features in broader transporter-focused screens.

In summary, the pathophysiology of FHCA2 is rooted in a relatively simple primary lesion—loss of basolateral hepatocyte NTCP function—that leads to complex but buffered changes in bile acid transport and metabolism, resulting in persistent hypercholanemia with limited clinical sequelae. The disease illustrates the resilience and redundancy of bile acid handling pathways and provides a human model for studying bile acid transport, host–virus interactions, and transporter-targeted therapies.

## 7. Anatomical Structures Affected

### 7.1 Organ-Level Involvement

The primary organ affected in FHCA2 is the liver, corresponding to UBERON:0002107. NTCP is expressed almost exclusively in hepatocytes, and its loss directly affects hepatic uptake of bile acids from the circulation.[6][7][15] The liver’s role in bile acid synthesis, conjugation, and secretion places it at the center of FHCA2 pathophysiology; however, unlike many cholestatic disorders, FHCA2 does not commonly cause chronic liver injury, fibrosis, or cirrhosis.[7][9][16] Transient hepatomegaly and cholestatic changes in infancy, as described in some pediatric cases, reflect temporary stress rather than permanent structural damage.[12][13][17]

The biliary tree and gallbladder (UBERON:0002110 for biliary tree, UBERON:0002112 for gallbladder) are indirectly involved through changes in bile composition and flow. Reduced hepatocellular uptake of bile acids may alter bile acid concentration in bile, potentially influencing micellar formation and gallstone risk, though such implications have not yet been systematically explored in NTCP-deficient individuals. The small intestine, particularly the ileum (UBERON:0002116), is affected in that bile acid-mediated fat absorption may be modestly impaired, especially in infancy.[2][7][13]

Secondary organ involvement arises mainly from fat-soluble vitamin deficiencies and systemic metabolic effects of hypercholanemia. The skeletal system (UBERON:0001434) can be affected through vitamin D deficiency–induced reductions in bone mineral density and, in severe cases, rickets.[2][13] The hematologic system (UBERON:0000178) is implicated when vitamin K deficiency leads to coagulopathy and prolonged prothrombin time, affecting hemostatic function.[2] However, these complications are preventable and treatable with appropriate vitamin supplementation.

### 7.2 Tissue and Cell Types

Within the liver, the key tissue is the hepatic parenchyma composed of hepatocytes (CL:0000182). NTCP is localized to the basolateral membrane of hepatocytes facing the sinusoidal blood, where it mediates bile acid uptake.[6][7][15] Hepatocytes are thus the primary cell type experiencing altered transport and metabolic stress in NTCP deficiency. Histologic changes observed in pediatric NTCP-deficient patients—such as hepatocyte ballooning, cholestatic multinucleate giant cells, and portal tract lymphocytic infiltration—reflect hepatocellular and canalicular stress rather than a specific NTCP-related lesion.[13]

Cholangiocytes (CL:0002412), the epithelial cells lining bile ducts, may experience altered bile acid exposure due to changes in bile composition, but there is no evidence of specific cholangiocyte pathology in FHCA2. Likewise, intestinal epithelial cells (enterocytes; CL:0000632) in the ileum handle altered bile acid flux and may adapt to changes in luminal bile acid concentration, but again, no specific pathology has been described.

In the skeletal system, osteoblasts (CL:0000062) and osteoclasts (CL:0000092) are indirectly affected by vitamin D deficiency, which alters calcium homeostasis and bone remodeling.[2][13] In the hematologic system, hepatocytes are responsible for synthesizing vitamin K–dependent clotting factors, and their production is compromised in vitamin K deficiency, although this reflects the systemic consequence of fat-soluble vitamin malabsorption rather than a direct structural defect in bone marrow or hematopoietic tissues.

### 7.3 Subcellular Localization and Compartments

NTCP is localized to the plasma membrane (GO:0005886), specifically the basolateral domain of hepatocytes (GO:0016328), where it mediates Na\(^+\)-dependent bile acid transport.[6][7][15] This localization is critical for its function in clearing conjugated bile acids from portal blood. Pathogenic variants such as R252H lead to loss of NTCP from the plasma membrane, likely via retention in the endoplasmic reticulum (ER; GO:0005783) and subsequent degradation, though detailed subcellular trafficking defects have not been fully characterized.[7][16]

Other subcellular compartments involved indirectly include the canalicular membrane (part of the apical plasma membrane domain; GO:0016327), where BSEP transports bile acids into bile, and the cytosol and mitochondria, where bile acid synthesis enzymes operate. However, these compartments remain structurally and functionally intact in NTCP deficiency, as evidenced by normal C4 levels and lack of progressive liver injury.[7][16]

### 7.4 Anatomical Localization and Lateralization

FHCA2 does not exhibit lateralization in the sense of left versus right organ involvement; bile acid transport defects are systemic and affect all hepatocytes. Anatomical localization is therefore best described at the organ and tissue level rather than by segmental or lobar distribution. Radiologic imaging in pediatric cases has not revealed focal lesions, masses, or asymmetry in liver involvement; hepatomegaly, when present, is diffuse.[13]

In conclusion, the anatomical impact of FHCA2 is centered on the liver and hepatocytes, with secondary effects on intestine, bone, and hematologic systems via fat-soluble vitamin malabsorption. At the subcellular level, the key defect resides in the basolateral plasma membrane domain of hepatocytes, where NTCP is absent or dysfunctional.

## 8. Temporal

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 5 |
| Resolved | 5 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 5 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 32 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 17 |
| Terms named correctly | 5 |
| Terms named as a **different** term | 10 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0012113` (2 mentions) - the report calls it "Hypercholanemia"; HP calls it **Abnormal circulating creatine concentration**
- `HP:0012111` (2 mentions) - the report calls it "Abnormal serum bile acid concentration"; HP calls it **Abnormality of circulating glucocorticoid level**
- `HP:0006564` (1 mention) - the report calls it "Neonatal cholestatic jaundice"; HP calls it **Fluctuating hepatomegaly**
- `HP:0012023` (2 mentions) - the report calls it "Vitamin D deficiency"; HP calls it **Galactosuria**
- `HP:0012112` (1 mention) - the report calls it "Abnormal bile acid profile"; HP calls it **Abnormal circulating corticosterone level**
- `HP:0006560` (1 mention) - the report calls it "Hepatic cholestasis"; HP calls it **Biliary hyperplasia**
- `HP:0002599` (1 mention) - the report calls it "Giant cell hepatitis"; HP calls it **Head titubation**
- `HP:0033863` (1 mention) - the report calls it "Hepatocellular ballooning"; HP calls it **Abnormal cortical peritubular capillary lumen morphology**
- `HP:0011902` (1 mention) - the report calls it "Vitamin K deficiency"; HP calls it **Abnormal hemoglobin**
- `GO:0048029` (1 mention) - the report calls it "bile acid transmembrane transport"; GO calls it **monosaccharide binding**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0003645` (1 mention) - the report calls it "Prolonged prothrombin time"; HP calls it **Prolonged partial thromboplastin time**
- `HP:0008936` (1 mention) - the report calls it "Mild generalized hypotonia"; HP calls it **Axial hypotonia**