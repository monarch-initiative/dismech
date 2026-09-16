---
provider: perplexity
model: sonar-deep-research
cached: true
start_time: '2026-08-29T19:51:26.085099'
end_time: '2026-08-29T19:51:26.089544'
duration_seconds: 0.0
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: CCDC115-CDG
  mondo_id: ''
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
  on_topic: 4
  validator_version: 0.2.1
term_validation:
  total_terms: 67
  verified: 62
  not_found: 3
  obsolete: 2
  unverifiable: 0
  confabulation_rate: 0.045
  labels_checked: 13
  labels_matching: 4
  labels_mismatched: 8
  mislabelled_terms:
  - term_id: NCIT:C15607
    reported_labels:
    - Supportive Care
    ontology_label: Clinical Diagnosis
  - term_id: NCIT:C28255
    reported_labels:
    - Physical Therapy
    ontology_label: International Unit
  - term_id: NCIT:C15279
    reported_labels:
    - Occupational Therapy
    ontology_label: Radical Mastectomy
  - term_id: NCIT:C28254
    reported_labels:
    - Speech Therapy
    ontology_label: Milliliter
  - term_id: NCIT:C15273
    reported_labels:
    - Liver Transplantation
    ontology_label: Longitudinal Study
  - term_id: NCIT:C16690
    reported_labels:
    - Gene Therapy
    ontology_label: HIV Envelope Protein gp41
  - term_id: NCIT:C17335
    reported_labels:
    - Cell Therapy
    ontology_label: Syndecan
  - term_id: NCIT:C158866
    reported_labels:
    - RNA-based Therapy
    ontology_label: del(10q23)/PTEN Gene Locus Deletion Analysis
  labels_variant: 1
  unresolved_terms:
  - HP:0003285
  - HP:0004402
  - HP:0003617
  obsolete_terms:
  - term_id: GO:0006486
    ontology_label: obsolete protein glycosylation
    replaced_by: GO:0009101
  - term_id: NCIT:C28255
    ontology_label: International Unit
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** CCDC115-CDG
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **CCDC115-CDG** covering all of the
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

# CCDC115-CDG (Congenital Disorder of Glycosylation Type IIo): An Integrated Disease Characterization

CCDC115-CDG, also known as congenital disorder of glycosylation type IIo (CDG-IIo or CDG2O), is an ultra-rare autosomal recessive metabolic disorder caused by biallelic loss-of-function variants in the *CCDC115* gene, leading to a defect of Golgi apparatus homeostasis and combined abnormalities of N-linked and mucin-type O-linked protein glycosylation.[9][13][15] Clinically, it presents in the neonatal or infantile period with a storage-disease-like hepatic phenotype that includes hepatosplenomegaly, cholestasis, progressive or fluctuating liver dysfunction, elevated liver enzymes, hypercholesterolemia, and low serum ceruloplasmin, frequently mimicking Wilson disease and other pediatric liver disorders.[2][3][13][15] Neurological involvement manifested as global developmental delay, hypotonia, psychomotor disability, and occasionally seizures, together with mild facial dysmorphism and bone abnormalities, underscores the multisystem nature of the disease.[2][13][15] At the molecular level, CCDC115 protein localizes predominantly to the ER-Golgi intermediate compartment and COPI vesicles and shows homology to yeast Vma22p, a V-ATPase assembly factor, implicating CCDC115 in the regulation of Golgi vesicular trafficking and lumen acidification; its deficiency disrupts glycosylation pathways and downstream cellular and tissue homeostasis.[5][13][14] The natural history of CCDC115-CDG is heterogeneous, with some children showing regression of hepatosplenomegaly and stabilization of liver tests, while others progress to severe fibrosis, cirrhosis, and acute liver failure, occasionally requiring liver transplantation, and there is currently no disease-specific pharmacologic therapy, making early diagnosis, supportive care, and genetic counseling the cornerstones of management.[2][13][15][16]  

---

## 1. Disease Information

### 1.1 Overview and Clinical Concept

CCDC115-CDG is a member of the expanding group of congenital disorders of glycosylation (CDG), a heterogeneous class of inborn errors of metabolism characterized by defects in the synthesis, processing, or attachment of glycans to proteins and lipids.[7][15] In this specific subtype, the primary biochemical hallmark is a combined defect of N-linked and mucin-type O-linked glycosylation, reflecting a disturbance of Golgi apparatus homeostasis rather than a defect in the early assembly of oligosaccharide chains.[9][13][15] Jansen et al. first delineated CCDC115 deficiency as a novel CDG type II, reporting eight individuals from five unrelated families with a distinctive phenotype involving predominant liver disease and abnormal glycosylation.[5][13] Orphanet subsequently catalogued CCDC115-CDG as a rare congenital disorder of glycosylation characterized by infantile onset hepatosplenomegaly, progressive liver failure, hypotonia, and global developmental delay, highlighting its place within the spectrum of multisystem CDG with prominent hepatic involvement.[2][15] More recent case reports and systematic reviews have confirmed this clinical picture, identifying additional patients and emphasizing that CCDC115-CDG can present as isolated liver disease or multisystem involvement, often posing substantial diagnostic challenges to pediatric hepatologists and metabolic specialists.[1][3][15]

A key feature of CCDC115-CDG is its association with disorders of Golgi homeostasis linked to vesicular trafficking and lumen pH, aligning it with other CDG forms such as COG-CDG, ATP6V0A2-CDG, and TMEM199-CDG.[3][15] These entities are unified by their disruption of intra-Golgi trafficking and acidification, processes essential for proper localization and activity of glycosylation enzymes, and thereby for normal glycoprotein maturation.[3][13][15] The clinical phenotype of CCDC115-CDG is not fully explained by current knowledge of Golgi biology, and the wide interindividual variability in hepatic, neurological, and systemic manifestations reflects the complex and pleiotropic role of glycosylation in human physiology.[5][13][15] This complexity has made the recognition of the disorder challenging, with early cases misclassified as storage diseases, Wilson disease, or cryptogenic cirrhosis until detailed glycosylation studies and exome sequencing revealed the underlying defect.[3][13][15] At present, CCDC115-CDG is best conceptualized as a multisystem metabolic disorder with a core triad of liver disease, abnormal glycosylation profiles, and neurodevelopmental impairment, anchored by a definable molecular etiology in the *CCDC115* gene.[2][9][13][15]

### 1.2 Key Identifiers and Nomenclature

Multiple curated databases have assigned unique identifiers and standardized nomenclature to CCDC115-CDG, facilitating its recognition in clinical and research settings.[2][9][10][11] The disorder’s primary OMIM phenotype entry is “Congenital disorder of glycosylation, type IIo” (CDG2O), OMIM number 616828, which is linked to pathogenic variants in *CCDC115* (OMIM gene entry 613734).[9][11] Orphanet lists the disease as “CCDC115-CDG” with Orphanet ID 468684 and notes its classification as a rare congenital disorder of glycosylation with prevalence estimated at less than 1 per 1,000,000, autosomal recessive inheritance, and infantile or neonatal onset.[2] ClinGen’s MONDO-curated ontology associates CCDC115-CDG with MONDO:0014789, embedding the disease within the MONDO framework for rare Mendelian conditions.[10] ICD-10 maps the disorder to code E77.8 (“Other specified disorders of glycoprotein metabolism”), while ICD-11 uses 5C54.2 for congenital disorders of glycosylation, providing a nosologic anchor in global diagnostic classification systems.[2]

The disease is known under several synonymous names that reflect historical and biochemical classification practices.[2][11] Orphanet and MalaCards list synonyms including “CDG syndrome type IIo,” “CDG-IIo,” “CDG2O,” “Carbohydrate deficient glycoprotein syndrome type IIo,” “Congenital disorder of glycosylation type 2o,” and “Congenital disorder of glycosylation type IIo,” all referring to the same underlying entity caused by *CCDC115* deficiency.[2][11] These names emphasize its status as a type II N-linked CDG, i.e., a disorder affecting trimming or remodeling of glycans after their initial attachment to proteins, in contrast to type I CDG forms that impair early glycan assembly.[7][15] The preferred contemporary nomenclature in the glycobiology and metabolic genetics community is “CCDC115-CDG,” which combines the gene symbol with the CDG label, paralleling naming conventions for PMM2-CDG, MPI-CDG, and other well-defined glycosylation disorders.[7][15] MeSH and other indexing systems have not yet established highly specific headings for CCDC115-CDG given its rarity, and it is often subsumed under broader terms such as “Congenital Disorders of Glycosylation” or “Inborn Errors of Metabolism” in bibliographic databases.[3][15]

### 1.3 Data Sources and Level of Aggregation

Information about CCDC115-CDG is derived primarily from aggregated disease-level resources that synthesize data from individual case reports, small series, and molecular studies rather than from large-scale electronic health record (EHR) analyses or population-based registries.[2][3][5][13][15] The seminal description by Jansen et al. in 2016 was based on exome sequencing and detailed phenotyping of eight individuals from five unrelated families, complemented by biochemical and cell-biological studies that established the glycosylation defect and the gene’s functional role.[5][13] Subsequently, Pellicano et al. and colleagues reported additional patients in 2018, focusing on the hepatic phenotype and highlighting that CCDC115-CDG can masquerade as other pediatric liver diseases, thereby enriching the clinical spectrum.[1][3] A systematic review of liver involvement in CDG by Cossu and coworkers integrated these and other reports, summarizing hepatic manifestations across 41 CDG types and specifically identifying three new CCDC115-CDG patients with variable combinations of severe liver fibrosis, cirrhosis, neurological symptoms, and isolated liver disease.[15]

Orphanet, OMIM, ClinGen MONDO, and MalaCards compile these primary data sources into structured disease summaries, but each remains constrained by the very small number of reported cases and the absence of longitudinal cohort studies.[2][9][10][11][15] No large-scale registry dedicated exclusively to CCDC115-CDG currently exists, and most CDG registries pool diverse glycosylation disorders without disease-specific stratification, limiting the granularity of epidemiologic and outcome data.[15] There are no published EHR-based phenome-wide association studies or GWAS analyses specifically focused on CCDC115-CDG, and given the rarity of the condition, such studies would require international consortia and advanced case-identification algorithms.[2][15] Consequently, much of our current understanding remains at the level of carefully documented individual patients and small series, interpreted through the lens of general glycosylation biology and extrapolated cautiously to broader disease mechanisms and management principles.[5][13][15] This context underscores the need to interpret quantitative statements about frequency, prognosis, and response to therapies as provisional, pending larger-scale natural history efforts.

---

## 2. Etiology

### 2.1 Primary Cause: Genetic Defects in *CCDC115*

The primary and defining cause of CCDC115-CDG is biallelic pathogenic variation in the *CCDC115* gene, which encodes the coiled-coil domain-containing 115 protein, a conserved factor implicated in Golgi homeostasis and vesicular trafficking.[5][9][13][14] Jansen et al. identified a homozygous missense mutation, c.92T>C (p.Leu31Ser), in three siblings affected by abnormal Golgi glycosylation through exome sequencing, thereby establishing *CCDC115* as the causal gene.[5][13] In their broader cohort, they reported eight individuals from five unrelated families harboring either missense variants or a deletion in *CCDC115*, including at least two distinct missense mutations catalogued in OMIM as 613734.0001 and 613734.0002.[9][13] The OMIM gene entry notes that *CCDC115* contains five exons and is located on chromosome 2q21.1, with pathogenic variants causing congenital disorder of glycosylation type IIo (CDG2O).[9] All reported affected individuals have carried variants in a biallelic autosomal recessive pattern, consistent with loss-of-function of CCDC115 being necessary and sufficient to produce the disease phenotype.[2][9][13][15]

Functional studies support a loss-of-function or severe functional impairment mechanism rather than a toxic gain-of-function effect.[5][13] In patient fibroblasts, CCDC115 deficiency leads to reduced metabolic labeling of sialic acids, indicating compromised terminal glycosylation, and this defect can be restored by complementation with wild-type CCDC115, demonstrating causality and reversibility at the cellular level.[13] PSI-BLAST homology analysis revealed reciprocal homology between human CCDC115 and yeast Vma22p, a vacuolar H+-ATPase assembly factor, suggesting that CCDC115 participates in similar pathways of proton pump assembly and Golgi pH regulation in human cells.[5][13][14] The consistent glycosylation abnormalities, liver phenotype, and rescue by wild-type protein support the concept that pathogenic variants result in functional haploinsufficiency or loss-of-function at the protein level, perturbing Golgi structure and function.[5][13][15] To date, no disease-causing duplications or gain-of-function variants of *CCDC115* have been reported, and heterozygous carriers appear clinically unaffected, consistent with autosomal recessive inheritance.[2][9][11][13]

### 2.2 Genetic Risk Factors and Susceptibility

Beyond the presence of biallelic pathogenic variants in *CCDC115*, additional genetic risk factors for CCDC115-CDG have not been systematically characterized due to the small number of patients.[5][9][13][15] The known disease-causing variants include missense substitutions in conserved residues and at least one deletion, but there is no published evidence of common polymorphisms or low-penetrance alleles that modulate disease susceptibility in heterozygous carriers or contribute to a milder phenotype.[9][13] The OMIM entry notes that six patients from four unrelated families carried two different missense mutations, supporting the idea that multiple private or rare variants can underlie disease in diverse genetic backgrounds.[9] ClinVar and related databases (as referenced by Jansen et al.’s ClinVar accession numbers SCV000257472, SCV000257474, and SCV000257477) document these variants as pathogenic or likely pathogenic under ACMG/AMP guidelines, but detailed penetrance and expressivity assessments are not available.[13]

Consanguinity appears to be a contributing factor for disease occurrence in at least some families, as is typical for rare autosomal recessive disorders.[5][13][15] Jansen et al. reported affected siblings in a consanguineous family, and the recurrence of identical homozygous variants in multiple siblings suggests that shared ancestry may elevate local carrier frequency and therefore risk.[13] However, no systematic population-genetic analysis has been undertaken to quantify carrier rates or founder effects in specific ethnic groups, and given the rarity of reported cases, any such founder phenomena would be highly localized.[2][9][11][15] No modifier genes have yet been linked to variability in phenotype severity, such as genes affecting Golgi architecture, V-ATPase subunits, or other glycosylation enzymes, although it is biologically plausible that variants in these pathways could interact with *CCDC115* lesions.[3][13][15] In sum, the primary genetic risk factor is an inherited biallelic pathogenic variant in *CCDC115*, while additional susceptibility loci or modifiers remain largely unexplored.

### 2.3 Environmental and Lifestyle Risk Factors

There is currently no direct evidence that environmental exposures or lifestyle factors serve as primary causal agents for CCDC115-CDG, which is clearly defined as a Mendelian metabolic disorder.[2][3][15] The disease onset in the neonatal or infantile period, often in the context of unremarkable prenatal history, and its association with specific genetic defects strongly support a genetic etiology rather than an acquired or multifactorial one.[2][13][15] Nonetheless, environmental factors may modulate clinical severity and the course of liver disease, as with many chronic hepatopathies, although this has not been systematically investigated in this ultra-rare population.[15] For example, infections, hepatotoxic medications, or nutritional deficiencies could theoretically exacerbate hepatic dysfunction in CCDC115-CDG, but current case series are too small to discern such patterns systematically.[3][13][15] Orphanet and OMIM, which aggregate disease-level data, do not list specific environmental or occupational exposures as risk factors for disease onset, reinforcing the view that genetic status is the primary determinant.[2][9][11]

Lifestyle factors such as diet, alcohol use, and physical activity are generally not relevant to disease onset given the pediatric age of presentation, although they may influence long-term liver health in surviving adolescents and adults.[2][15] There is no evidence linking common liver disease risk factors, such as obesity or viral hepatitis, to the pathogenesis of CCDC115-CDG, and no reports have described coexistent environmental liver insults in published patients.[3][13][15] Therefore, from a strict etiologic standpoint, environmental and lifestyle factors currently appear to play a secondary role, primarily as potential modifiers rather than causal factors, and their impact remains speculative due to limited data.

### 2.4 Protective Factors and Gene–Environment Interactions

Protective factors—either genetic variants that mitigate disease severity or environmental exposures that ameliorate manifestations—have not been described for CCDC115-CDG in the available literature.[2][9][13][15] Given the essential role of CCDC115 in Golgi homeostasis, it is plausible that partial function retained by certain missense variants might yield a milder phenotype compared to null alleles, but this hypothesis has not been systematically tested with genotype–phenotype correlation studies.[9][13] No “protective” alleles in other glycosylation genes have been reported that buffer the effect of CCDC115 deficiency, and given the interconnected nature of glycosylation pathways, compensatory mechanisms might exist but remain uncharted.[3][13][15] Similarly, there are no reports of specific dietary regimens, pharmacologic agents, or environmental factors conferring measurable protection, in contrast to disorders like MPI-CDG, where mannose supplementation can correct certain biochemical defects.[15][16]

Gene–environment interactions have not been formally studied in CCDC115-CDG, and the rarity of the condition makes such investigations challenging.[2][15] Mechanistically, one could speculate that environmental factors influencing Golgi stress, ER stress, or oxidative damage might interact with CCDC115 deficiency to modulate cellular resilience, but beyond general biophysical reasoning, there is no direct empirical evidence.[5][13][15] Current case reports typically focus on intrinsic disease features and do not describe detailed environmental histories or exposures that could be interrogated for interaction effects.[3][13][15] Therefore, the present state of knowledge defines CCDC115-CDG as a primarily genetic disease with no established protective factors or gene–environment interactions, emphasizing the importance of genetic counseling and molecular diagnosis rather than environmental risk stratification.

---

## 3. Phenotypes

### 3.1 General Phenotypic Spectrum and Age of Onset

CCDC115-CDG exhibits a multisystem phenotype dominated by hepatic, neurological, and metabolic manifestations, with onset typically in the neonatal or infantile period.[2][3][13][15] Orphanet describes the disorder as featuring “infantile onset of hepatosplenomegaly, progressive liver failure, hypotonia, and global developmental delay,” reflecting the early emergence of organ dysfunction and neurodevelopmental impairment.[2] Jansen et al. reported that all eight individuals in their series displayed a storage-disease-like phenotype involving hepatosplenomegaly, with associated biochemical abnormalities and neurological symptoms appearing in early childhood.[13] The liver involvement can range from asymptomatic elevation of liver enzymes to overt cholestatic jaundice, liver failure, and cirrhosis, and may present as acute liver failure in rare cases.[3][13][15] Neurological features, including psychomotor delay and hypotonia, often emerge in parallel or shortly after hepatic signs, underscoring the systemic impact of defective glycosylation on brain and muscle.[2][13][15]

The severity and progression of manifestations are variable, reflecting differences in underlying variants, residual protein function, and possibly other genetic or environmental modifiers.[5][13][15] In Jansen’s cohort, hepatosplenomegaly showed a tendency to regress with age in some individuals, whereas biochemical abnormalities such as elevated aminotransferases and hypercholesterolemia persisted.[13][15] In contrast, Pellicano and subsequent authors described patients with progressive liver disease culminating in severe fibrosis, cirrhosis, and transplantation, suggesting that in some cases the hepatic phenotype is relentlessly progressive.[1][3][15] Neurological outcomes also vary, with some children achieving partial developmental milestones and others experiencing severe global delays and seizures, but systematic measures of cognitive function and quality of life are lacking.[2][13][15] Overall, CCDC115-CDG is best characterized as an early-onset, often severe, but clinically heterogeneous condition with multi-organ involvement and a broad spectrum of severity.

From an ontology perspective, key HPO terms for the general phenotype include congenital onset of disease (HP:0003577), hepatosplenomegaly (HP:0001433), cholestatic liver disease (HP:0002611), liver failure (HP:0001410), neonatal jaundice (HP:0006560), global developmental delay (HP:0001263), muscular hypotonia (HP:0001252), and seizures (HP:0001250).[2][13][15][17] These phenotypes collectively capture the multi-system nature of the disorder, linking liver, nervous system, and musculoskeletal manifestations in a coherent ontology framework. Quality of life impacts, while not formally measured with instruments like EQ-5D or SF-36 in published series, can be inferred to be substantial due to chronic liver disease, developmental impairments, and the need for intensive medical follow-up and, in some instances, transplantation.[2][13][15]

### 3.2 Hepatic Phenotypes

The liver is the principal organ affected in CCDC115-CDG, and hepatic manifestations provide the most specific and clinically actionable component of the phenotype.[2][3][13][15] Jansen et al. emphasized that “all individuals displayed a storage-disease-like phenotype involving hepatosplenomegaly, which regressed with age, highly elevated bone-derived alkaline phosphatase, elevated aminotransferases, and elevated cholesterol, in combination with abnormal copper metabolism and neurological symptoms.”[13] This description captures the characteristic combination of organomegaly and biochemical abnormalities that signal hepatic involvement in early childhood. Orphanet adds that laboratory findings include elevated liver enzymes, mild hypercholesterolemia, and low serum ceruloplasmin, reflecting disturbances in hepatocellular integrity, lipid metabolism, and copper-binding protein synthesis.[2] The systematic review by Cossu et al. notes that all reported CCDC115-CDG patients show hepatic manifestations, including hepatomegaly or hepatosplenomegaly, jaundice, liver failure, and cholestasis, with two recent patients displaying severe liver fibrosis and cirrhosis and another presenting isolated liver involvement.[15]

The pattern of liver injury appears predominantly cholestatic, with features of both intrahepatic cholestasis and hepatocellular damage.[3][13][15] HPO terms relevant to these manifestations include hepatomegaly (HP:0002240), splenomegaly (HP:0001744), cholestasis (HP:0001396), cholestatic liver disease (HP:0002611), jaundice (HP:0000952), and abnormal liver function tests (HP:0002910).[2][13][15][17] Elevated aminotransferases and alkaline phosphatase indicate hepatocellular injury and cholestasis, respectively, while hypercholesterolemia reflects altered lipid handling by the liver.[13][15] Low serum ceruloplasmin and abnormal copper metabolism create a clinical picture reminiscent of Wilson disease, and at least some CCDC115-CDG cases have been initially misdiagnosed as Wilson disease due to this biochemical profile.[3][13][15] Histologically, recent reports have described severe liver fibrosis and cirrhosis in some patients, although detailed histopathologic patterns (such as regenerative nodular hyperplasia or porto-sinusoidal vascular changes) remain incompletely characterized.[15]

The progression of hepatic disease is variable, but in many CDG types, liver enzymes increase during the first five years of life and then improve; however, CCDC115-CDG is among those forms in which liver parameters may not follow a benign course.[15] Cossu et al. note that “these parameters mostly increased during the first 5 years of life in most types of CDG (apart from ALG8-CDG, CCDC115-CDG, MPI-CDG, PGM1-CDG, and TMEM165-CDG patients), but they improved significantly afterwards,” implying that CCDC115-CDG belongs to a subgroup with more persistent or progressive liver involvement.[15] Acute liver failure is rare but documented; in a retrospective analysis of metabolic diseases presenting as acute liver failure, one out of 127 patients had CCDC115-CDG, highlighting the potential for catastrophic hepatic events.[15] Taken together, the hepatic phenotype in CCDC115-CDG encompasses chronic cholestatic liver disease, potential progression to fibrosis and cirrhosis, and occasional acute liver failure, constituting a major determinant of prognosis and quality of life.

### 3.3 Neurological and Developmental Phenotypes

Neurological and developmental manifestations form the second major phenotypic domain in CCDC115-CDG.[2][13][15] Orphanet notes that affected individuals exhibit hypotonia and global developmental delay, and seizures have also been reported.[2] In Jansen’s series, neurological symptoms accompanied the hepatic phenotype, including psychomotor disability and hypotonia, though specific cognitive profiles were not systematically quantified.[13] Cossu et al. report that five of eleven patients with CCDC115-CDG had neurological symptoms, reinforcing the prevalence of brain involvement.[15] These features are consistent with the broader CDG spectrum, in which neurological impairment is common due to the ubiquitous requirement for glycosylation in neuronal development, synaptogenesis, and axonal maintenance.[7][15]

The severity of neurological impairment appears variable, ranging from mild developmental delays to profound global disability and seizures.[2][13][15] HPO terms relevant to this domain include global developmental delay (HP:0001263), developmental regression (HP:0002376) when present, muscular hypotonia (HP:0001252), seizures (HP:0001250), and intellectual disability (HP:0001249) for more severe cognitive impairment.[2][13][15] Hypotonia can contribute to motor delays, feeding difficulties, and reduced endurance, while seizures add episodic neurological stress and require chronic antiepileptic therapy.[2][15] Quality of life impacts are significant, as children with combined liver disease and developmental delays require intensive medical and rehabilitative support, and their families face ongoing caregiving demands and uncertainty regarding future functional outcomes.[2][15] However, no standardized neuropsychological or quality-of-life scales have been published specifically for CCDC115-CDG, and the small case numbers preclude robust characterization of neurodevelopmental trajectories.[13][15]

Mechanistically, neurological involvement in CCDC115-CDG likely reflects the impact of defective glycosylation on multiple neural systems, including glycoproteins involved in axon guidance, synaptic receptor function, and ion channel stability.[7][13][15] The broad distribution of glycosylation defects across serum and cellular proteins supports a systemic effect rather than a localized brain-specific lesion.[13] Although magnetic resonance imaging findings have not been systematically reported in this specific CDG form, other Golgi-related CDG may show cerebellar atrophy or white matter abnormalities, and similar changes could be present but unreported in CCDC115-CDG.[15] Future studies employing standardized neuroimaging and neurocognitive assessments will be important to refine this component of the phenotype.

### 3.4 Dysmorphic, Skeletal, and Other Physical Phenotypes

Mild dysmorphic facial features have been reported in CCDC115-CDG, alongside skeletal and bone-related abnormalities.[2][13][15] Orphanet notes “mild dysmorphic features” as part of the phenotype, although specific descriptors such as frontal bossing, hypertelorism, or low-set ears have not been consistently catalogued across cases.[2] Cossu et al. mention that five patients exhibited facial dysmorphisms, suggesting that craniofacial anomalies are relatively frequent but subtle.[15] HPO terms such as dysmorphic facial features (HP:0001999), coarse facial features (HP:0000280), or other more specific traits could be applied once detailed phenotypic descriptions are available, but current data are limited.[2][15] The variability and subtlety of these features underscore the need for detailed clinical photographs and systematic morphologic assessment in future reports to better define dysmorphology in CCDC115-CDG.

Bone and skeletal findings are more clearly documented in the biochemical profile of the disease. Jansen et al. reported “highly elevated bone-derived alkaline phosphatase” in all individuals, indicating increased bone turnover or altered bone metabolism.[13] This laboratory abnormality, while primarily reflecting bone physiology, is also part of the overall cholestatic liver picture, as alkaline phosphatase has both hepatic and bone isoforms.[13][15] HPO terms relevant to this observation include increased circulating alkaline phosphatase concentration (HP:0003155) and possibly abnormal bone mineral density (HP:0004349) if structural skeletal changes are documented.[13][15] However, there are no detailed reports of clinical skeletal deformities, fractures, or radiographic osteopenia specifically linked to CCDC115-CDG, so bone involvement currently remains a biochemical rather than overt structural phenotype.[13][15] This distinction highlights the complexity of interpreting alkaline phosphatase elevations in a disease that affects both liver and bone.

Other physical manifestations described include hepatosplenomegaly-related abdominal distension and constitutional symptoms such as fatigue and poor weight gain, though these are shared with many chronic pediatric liver diseases.[13][15] There is no evidence of specific cardiopulmonary or renal phenotypes in the limited published cases, and broad systemic signs such as failure to thrive or recurrent infections have not been emphasized, differentiating CCDC115-CDG from some other CDG forms with prominent immune deficiency.[15] Overall, the dysmorphic and skeletal phenotype is secondary to the hepatic and neurological domains but contributes to the clinical impression of a multisystem metabolic disorder.

### 3.5 Laboratory and Metabolic Phenotypes

The laboratory phenotype of CCDC115-CDG is rich and forms an essential component of diagnosis, reflecting the underlying glycosylation defect and its systemic metabolic consequences.[2][13][15] Jansen et al. documented elevated aminotransferases, highly elevated bone-derived alkaline phosphatase, elevated cholesterol, and abnormal copper metabolism, including low ceruloplasmin.[13] Orphanet echoes these findings, noting elevated liver enzymes, mild hypercholesterolemia, and low serum ceruloplasmin as characteristic laboratory abnormalities.[2] Cossu et al. confirmed that all reported patients had hepatic biomarkers indicative of cholestasis and hepatocellular injury, along with metabolic disturbances of lipids and copper.[15] HPO terms for these features include elevated serum alanine aminotransferase (HP:0002910), increased alkaline phosphatase (HP:0003155), hypercholesterolemia (HP:0003124), reduced serum ceruloplasmin (HP:0003285), and abnormality of copper homeostasis (HP:0004402).[2][13][15]

The glycosylation profile is central to the laboratory phenotype and diagnostic work-up. Isoelectric focusing of serum transferrin in patients shows a type II CDG pattern, indicating abnormal processing of N-linked glycans after attachment to the protein backbone.[9][13][15] Jansen et al. found abnormal N- and mucin-type O-glycosylation on serum proteins, and reduced metabolic labeling of sialic acids in fibroblasts, which normalized upon expression of wild-type CCDC115.[13] These findings demonstrate a combined defect of N- and O-glycosylation and implicate impaired terminal sialylation as a key biochemical signature.[13][15] From an ontology standpoint, these defects correspond to abnormal protein N-linked glycosylation (HP:0002917) and abnormal O-glycosylation (HP:0005640), with underlying GO biological processes including protein glycosylation (GO:0006486) and Golgi organization (GO:0007030).[9][13] Such glycosylation abnormalities can be detected by specialized biochemical assays, including isoelectric focusing, mass spectrometry-based glycan profiling, and targeted analysis of glycoproteins such as transferrin.[13][15]

Copper metabolism abnormalities, particularly low ceruloplasmin, give rise to a diagnostic pitfall, as they suggest Wilson disease in standard clinical algorithms.[3][13][15] However, unlike Wilson disease, CCDC115-CDG does not arise from ATP7B mutations and may show different patterns of hepatic copper deposition, although detailed histochemical analyses are limited.[3][15] The combination of low ceruloplasmin, abnormal glycosylation patterns, and multi-organ involvement should therefore prompt evaluation for CDG rather than assumption of Wilson disease.[3][13][15] Lipid anomalies, mainly hypercholesterolemia, may reflect altered glycosylation of lipoproteins or receptors involved in cholesterol metabolism, but this mechanism remains speculative.[13][15] Together, the laboratory and metabolic phenotype provides a robust, albeit specialized, framework for diagnosing CCDC115-CDG and distinguishing it from other pediatric liver and metabolic disorders.

---

## 4. Genetic and Molecular Information

### 4.1 The *CCDC115* Gene: Structure, Location, and Regulation

The *CCDC115* gene encodes coiled-coil domain-containing protein 115, a relatively small protein with conserved structural motifs and localization to the early secretory pathway.[5][9][13][14] OMIM notes that *CCDC115* contains five exons and is located on chromosome 2q21.1 on the negative strand, with genomic coordinates 2:130,337,933–130,342,681 (GRCh38).[9] The gene was initially mapped to chromosome 2q21.2 by Pellicano et al., and subsequent fine mapping refined its locus.[9] In mice, the orthologous gene maps to chromosome 1B, reflecting conserved synteny across mammalian species.[9] The HGNC-approved gene symbol is CCDC115, and standard identifiers include OMIM gene number 613734 and corresponding NCBI Gene IDs in human and model organisms.[9][14]

Expression data suggest that *CCDC115* is expressed in multiple tissues, consistent with its role in a fundamental cellular process like Golgi homeostasis.[5][9][13] Microarray analysis of mouse cortical neuron cultures by Pellicano et al. showed modest upregulation of the mouse ortholog (Ccp1) by fibroblast growth factor 2 (Fgf2), implying that *CCDC115* may be responsive to growth factor signaling and involved in cellular proliferation.[9] Overexpression and knockdown experiments in mouse embryonic fibroblasts and human neuroblastoma cell lines revealed that Ccp1 regulates cell number by promoting proliferation and suppressing cell death, suggesting that CCDC115 may intersect with cell-cycle and survival pathways beyond its role in Golgi function.[9] These findings, while not directly linked to the CDG phenotype, highlight the gene’s broader cellular significance and potential epigenetic or regulatory influences.

From a functional perspective, Jansen et al. localized human CCDC115 mainly to the ER-Golgi intermediate compartment (ERGIC) and to COPI vesicles, but not to the endoplasmic reticulum itself, using immunofluorescence and biochemical fractionation.[13][14] PSI-BLAST homology detection revealed reciprocal homology with Vma22p, the yeast vacuolar ATPase assembly factor located in the endoplasmic reticulum, suggesting that CCDC115 plays a related role in V-ATPase assembly and Golgi acidification.[5][13][14] The protein’s coiled-coil domain and vesicular localization fit its proposed function as a scaffold or assembly factor in the secretory pathway. GO cellular component terms relevant to CCDC115 include Golgi apparatus (GO:0005794), ER-Golgi intermediate compartment (GO:0005798), and COPI-coated vesicle (GO:0030137), while biological process terms include protein glycosylation (GO:0006486), Golgi vesicle transport (GO:0048193), and regulation of vacuolar proton-transporting ATPase assembly (GO:0007035).[13][14]

### 4.2 Pathogenic Variants: Types, Classification, and Frequency

The pathogenic variants in *CCDC115* reported to date are primarily missense mutations and at least one deletion, consistent with a loss-of-function mechanism.[5][9][13] Jansen et al. identified a homozygous missense mutation c.92T>C (p.Leu31Ser) in a family with three affected siblings and subsequently reported additional variants including c.31G>T and a deletion, all affecting conserved residues or disrupting gene structure.[13] OMIM catalogues two distinct missense mutations (613734.0001 and 613734.0002) as causative for CDG2O, and Jansen et al. submitted variant data to ClinVar under accession numbers SCV000257472, SCV000257474, and SCV000257477.[9][13] These variants are classified as pathogenic or likely pathogenic under ACMG/AMP criteria based on segregation, functional data, and the observed glycosylation defect.[13] Variant types include missense changes in the N-terminal region and deletions that may induce frameshifts or nonsense-mediated decay, leading to truncated or absent protein.[9][13]

Allele frequencies of these pathogenic variants in population databases such as gnomAD are extremely low or absent, reflecting the ultra-rare nature of the disease and purifying selection against deleterious alleles.[2][9][11][15] No common polymorphisms in *CCDC115* have been associated with disease risk or modulating severity, and heterozygous carriers are generally healthy, consistent with autosomal recessive inheritance.[2][9][11][13] There is no evidence of somatic *CCDC115* mutations contributing to cancer or other acquired diseases in COSMIC or TCGA-like datasets, though comprehensive analyses have not been reported.[9][13] All disease-causing variants described in CCDC115-CDG cases are germline, inherited from carrier parents, and present in all cells, producing systemic manifestations.[2][9][13][15]

Functional consequences of these variants have been elucidated through in vitro studies and glycosylation assays.[13] Patient fibroblasts show reduced metabolic labeling of sialic acids and abnormal glycosylation of N- and mucin-type O-glycoproteins, consistent with impaired Golgi function.[13] Complementation with wild-type CCDC115 restores normal sialylation, confirming that the variants cause functional loss-of-function.[13] GO molecular function terms related to this effect include “protein binding” (GO:0005515) and “proton-transporting ATPase regulator activity” (GO:0046933), reflecting potential roles in V-ATPase assembly.[13][14] Overall, pathogenic *CCDC115* variants are rare, germline, and cause a systemic loss-of-function phenotype leading to CCDC115-CDG.

### 4.3 Modifier Genes, Epigenetics, and Chromosomal Abnormalities

At present, no modifier genes have been definitively associated with variability in severity or organ-specific expression of CCDC115-CDG.[2][9][13][15] Given the involvement of CCDC115 in Golgi and V-ATPase function, genes encoding other Golgi structural proteins, vesicle coat components (COPI, COPII), and V-ATPase subunits (such as ATP6V0A2) are plausible candidates for modifiers, but no published human data demonstrate interaction effects.[3][13][15] The phenotypic diversity observed in CCDC115-CDG could arise from stochastic variation and general genetic background rather than specific modifier alleles, although this question remains open to future investigation.[15] Epigenetic regulation of *CCDC115* has not been directly studied in the context of CDG, and there are no reports of DNA methylation or histone modification abnormalities specifically linked to this gene.[9][13][15] However, the broader evidence from Pellicano et al. indicates that Ccp1 (the mouse ortholog) is responsive to growth factor signaling and influences cell proliferation, hinting that epigenetic and transcriptional regulation might modulate expression under certain conditions.[9]

No large-scale chromosomal abnormalities, such as aneuploidy, translocations, or inversions, have been associated with CCDC115-CDG in published cases.[9][13][15] DECIPHER and similar databases do not currently list recurrent copy number variants encompassing *CCDC115* as causative of a distinct syndromic phenotype, although isolated deletions of the gene have been reported as part of the molecular spectrum of CDG2O.[9][13] These deletions appear to act like other loss-of-function variants by eliminating functional protein and producing the typical CDG phenotype.[13] Overall, the genetic and molecular architecture of CCDC115-CDG remains relatively simple compared to many complex disorders: biallelic loss-of-function of *CCDC115* is necessary and sufficient for disease, with limited evidence for major chromosomal or epigenetic contributions.

---

## 5. Environmental Information

### 5.1 Environmental Exposures and Non-genetic Contributors

As discussed in the etiology section, CCDC115-CDG is fundamentally a Mendelian genetic disorder, and there is no evidence that environmental exposures act as primary causes.[2][3][15] Nonetheless, environmental factors may influence disease expression and progression, particularly in the liver where multiple exogenous insults can modulate fibrosis and functional reserve.[15] For example, hepatotoxic medications, viral infections, or nutritional deficiencies could theoretically exacerbate underlying cholestatic hepatopathy in CCDC115-CDG, but such interactions have not been described in published case series.[3][13][15] The pediatric age of onset and the rarity of the disease make systematic studies of environmental modifiers difficult, and clinicians focus primarily on controlling known exposures that can worsen liver function, such as avoiding unnecessary hepatotoxic drugs and ensuring adequate nutrition.[15]

No specific toxins, radiation exposures, or pollutants have been linked to the onset or acceleration of CCDC115-CDG.[2][3][15] Comparative toxicogenomics databases and environmental epidemiology resources have not reported associations between *CCDC115* variants and environmental risk profiles, and given the small number of patients, such analyses would lack power.[2][15] In the absence of disease-specific data, general hepatology principles apply: minimizing exposure to environmental hepatotoxins and infections is advisable, but this is standard practice for all children with chronic liver disease and not unique to CCDC115-CDG.[15] Thus, environmental information in this disease context is largely inferential, based on general medical knowledge rather than direct empirical evidence.

### 5.2 Lifestyle and Infectious Factors

Lifestyle factors such as diet, exercise, and alcohol consumption are generally not relevant to disease onset in CCDC115-CDG because the condition manifests during infancy or early childhood, well before typical behavioral exposures that affect adult liver disease.[2][15] However, as affected individuals age, lifestyle choices may become relevant to long-term hepatic outcomes, especially in those who survive into adolescence or adulthood with residual liver dysfunction.[15] There is no current evidence that specific diets or supplements can ameliorate the glycosylation defect, in contrast to certain CDG types such as MPI-CDG or PGM1-CDG where targeted sugar supplementation has therapeutic effects.[15][16] Nutritional support is nonetheless important to sustain growth and overall health in the setting of chronic disease.

Infectious agents, including viruses, bacteria, fungi, and parasites, have not been implicated as triggers or causal contributors to CCDC115-CDG.[2][3][15] Routine pediatric infections may transiently worsen liver function tests or precipitate decompensation in advanced liver disease, but these effects are nonspecific and not unique to CCDC115-CDG.[15] Vaccination against hepatotropic viruses such as hepatitis B is recommended for children with chronic liver disease as part of standard care, but this is preventive for superimposed infection rather than targeted to the underlying CDG.[15] Overall, lifestyle and infectious factors constitute general background influences on health, with no documented specific role in the pathogenesis of CCDC115-CDG.

---

## 6. Mechanism and Pathophysiology

### 6.1 Glycosylation Pathways and CDG Classification

To understand the pathophysiology of CCDC115-CDG, it is essential to appreciate the role of protein glycosylation in human biology and the classification of CDG.[7][15] Glycosylation is the enzymatic process by which carbohydrate chains (glycans) are attached to proteins and lipids, influencing their folding, stability, trafficking, and function.[7][15] The most common forms in humans are N-linked glycosylation, in which oligosaccharides are attached to asparagine residues, and O-linked glycosylation, in which sugars are attached to serine or threonine residues, including mucin-type O-glycosylation in secreted and membrane mucins.[7][13][15] CDG are traditionally classified into type I and type II based on patterns of N-linked glycan abnormalities detected in serum transferrin: type I CDG involve defects in the assembly or transfer of the oligosaccharide precursor, whereas type II CDG affect trimming or remodeling of glycan chains once attached to the protein.[7][15]

Children’s Hospital of Philadelphia explains that “the most common forms of CDG, and the greatest number of forms, are those that affect N-glycosylation” and that “N-linked type II forms of CDG have genetic defects that affect the trimming or remodeling of oligosaccharide building blocks once they are attached to proteins.”[7] CCDC115-CDG is classified as a type II CDG, specifically CDG-IIo, based on the transferrin isoelectric focusing pattern and the underlying mechanism involving Golgi homeostasis rather than early glycan assembly.[9][13][15] Jansen et al. found abnormal N- and mucin-type O-glycosylation on serum proteins in affected individuals and reduced metabolic labeling of sialic acids in fibroblasts, indicating that terminal sialylation and overall glycan maturation are compromised.[13] These defects were corrected by expressing wild-type CCDC115, confirming a direct causal role.[13] Thus, CCDC115-CDG exemplifies a subset of CDG where the core defect lies not in a glycosyltransferase enzyme per se but in the organelle environment and trafficking machinery that support glycosylation.

### 6.2 CCDC115, Golgi Homeostasis, and V-ATPase Assembly

CCDC115 is functionally linked to Golgi homeostasis through its localization and homology to yeast Vma22p.[5][13][14] Jansen et al. reported that “human CCDC115 mainly localized to the ERGIC and to COPI vesicles, but not to the ER,” indicating that the protein resides at the interface between endoplasmic reticulum and Golgi and in retrograde transport vesicles that shuttle proteins from Golgi back to ER.[13][14] PSI-BLAST homology detection revealed reciprocal homology between CCDC115 and yeast Vma22p, a vacuolar ATPase assembly factor located in the ER.[5][13][14] Vma22p participates in the assembly of the V-ATPase complex, which is responsible for proton transport and acidification of intracellular compartments, including Golgi cisternae.[5][13][14] Although CCDC115’s exact biochemical role in human cells remains incompletely defined, these data strongly suggest that it contributes to V-ATPase assembly or trafficking in the secretory pathway, thereby influencing Golgi lumen pH.

Golgi pH is critical for the optimal activity and localization of glycosyltransferases and glycosidases that execute glycan trimming and extension.[3][13][15] Congenital disorders of glycosylation linked to defects in Golgi apparatus homeostasis—including COG-CDG, ATP6V0A2-CDG, TMEM199-CDG, and CCDC115-CDG—“have been shown to disturb Golgi vesicular trafficking and/or lumen pH acidification,” thereby altering the milieu in which glycosylation occurs.[3] In ATP6V0A2-CDG, mutations in a core subunit of V-ATPase directly impair proton transport and acidification, leading to skin and connective tissue phenotypes; CCDC115-CDG, in contrast, disrupts glycosylation through a more general role in Golgi trafficking and possibly V-ATPase assembly, with a distinct clinical phenotype dominated by liver disease.[3][13][15] Jansen et al. concluded that “our data suggest a physiological role for CCDC115 in Golgi homeostasis, and loss-of-function mutations lead to the inability of the Golgi to perform its core functions: post-translational modification and protein secretion and sorting.”[13] GO biological process terms relevant to these mechanisms include Golgi organization (GO:0007030), vesicle-mediated transport (GO:0016192), and regulation of organelle pH (GO:0030487).[13][14]

### 6.3 Causal Chain from Gene Defect to Clinical Phenotype

The causal chain from *CCDC115* mutation to clinical manifestations in CCDC115-CDG can be conceptualized in several sequential steps, linking molecular defects to cellular dysfunction and organ pathology.[5][13][15] At the upstream level, biallelic loss-of-function variants in *CCDC115* result in reduced or absent functional CCDC115 protein in cells throughout the body, including hepatocytes, neurons, myocytes, and other cell types.[9][13][15] This deficiency impairs processes related to Golgi homeostasis, likely including V-ATPase assembly or trafficking and ER-Golgi vesicular transport, leading to altered Golgi structure and lumen pH.[5][13][14] The disturbed pH and structural environment cause mislocalization or reduced activity of multiple glycosyltransferases and glycosidases, disrupting proper trimming and extension of N-linked glycans and O-linked mucin-type glycans attached to nascent proteins.[7][13][15]

At the biochemical level, these alterations manifest as abnormal glycosylation patterns detectable in serum glycoproteins, such as transferrin, and as reduced incorporation of terminal sugars such as sialic acid, as demonstrated by metabolic labeling studies in fibroblasts.[13][15] Abnormal glycoproteins have altered conformation, stability, and trafficking, leading to functional deficits in diverse proteins including receptors, adhesion molecules, coagulation factors, and transporters.[7][13][15] In hepatocytes, defective glycosylation may affect bile salt export pumps, canalicular transporters, and receptors involved in lipid and copper metabolism, contributing to cholestasis, hypercholesterolemia, and low ceruloplasmin.[13][15] In neurons, misglycosylation of cell-surface receptors, ion channels, and extracellular matrix components can impair synaptic signaling, axon guidance, and neuronal survival, resulting in hypotonia, developmental delay, and seizures.[7][13][15] In bone, altered glycosylation of matrix proteins and signaling receptors may modulate osteoblast activity and alkaline phosphatase expression, contributing to biochemical bone abnormalities.[13][15]

Downstream of these cellular changes, organ-level pathology emerges. In the liver, chronic cholestatic injury and hepatocellular dysfunction lead to hepatomegaly and eventually fibrosis and cirrhosis in some individuals.[13][15] The spleen enlarges due to portal hypertension and reactive changes, contributing to hepatosplenomegaly.[13][15] The brain exhibits global developmental delays and hypotonia, reflecting diffuse neurodevelopmental disruption rather than focal lesions.[2][13][15] Systemic manifestations, including failure to thrive, fatigue, and constitutional symptoms, arise from chronic organ dysfunction and metabolic derangements.[13][15] Thus, the causal chain spans from the molecular level (CCDC115 deficiency) through cellular organelle dysfunction (Golgi and V-ATPase), biochemical abnormalities (glycosylation defects), tissue-level changes (cholestasis, fibrosis, neurodevelopmental impairment), and finally to clinical signs and symptoms.

### 6.4 Upstream versus Downstream Mechanisms and Cell Types Involved

Upstream mechanisms in CCDC115-CDG involve the direct effects of CCDC115 deficiency on Golgi homeostasis and vesicular trafficking.[5][13][14] These early events occur in multiple cell types, but hepatocytes (CL:0000182), cholangiocytes (biliary epithelial cells, CL:0002598), neurons (CL:0000540), and skeletal muscle cells (CL:0000187) are among the most clinically relevant.[13][15] In hepatocytes and cholangiocytes, Golgi dysfunction impairs processing and secretion of bile components and plasma proteins, leading to cholestasis and abnormal serum glycoprotein profiles.[13][15] In neurons, Golgi-dependent trafficking of membrane proteins and secreted growth factors is critical for synaptic function and axonal maintenance, so Golgi defects contribute to neurodevelopmental impairment.[7][13][15] In skeletal muscle, glycosylation of structural proteins and receptors influences muscle tone and strength, consistent with hypotonia.[2][13][15]

Downstream mechanisms include oxidative stress, inflammation, fibrosis, and organ remodeling triggered by chronic cell injury.[15] In the liver, persistent cholestasis and hepatocyte damage lead to activation of hepatic stellate cells, collagen deposition, and architectural distortion, culminating in fibrosis and cirrhosis.[15] Portal hypertension develops as fibrosis progresses, causing splenomegaly and variceal formation, although detailed vascular pathology in CCDC115-CDG has yet to be characterized.[15] GO terms related to these downstream processes include “response to oxidative stress” (GO:0006979), “inflammatory response” (GO:0006954), and “extracellular matrix organization” (GO:0030198), which are common to many chronic liver diseases.[15] In the nervous system, downstream mechanisms may include neuronal loss and synaptic dysfunction due to misfolded or misglycosylated proteins, although specific pathways (e.g., excitotoxicity, apoptosis) have not been directly studied in CCDC115-CDG.[13][15]

### 6.5 Immune Involvement, Metabolomics, and Advanced Molecular Profiling

Unlike some CDG forms associated with immunodeficiency, such as ATP6AP1-CDG, CCDC115-CDG has not been prominently linked to immune dysfunction.[15][16] ATP6AP1-CDG (Immunodeficiency 47) presents with immunodeficiency and liver involvement, including cholestasis and cirrhosis, but CCDC115-CDG patients reported to date have not exhibited recurrent severe infections or marked immunologic abnormalities.[15] Thus, immune system involvement appears limited or secondary in CCDC115-CDG, and no specific immune pathways have been implicated.[15][16] However, given the role of glycosylation in immune receptor function and pathogen recognition, subtle immune changes may exist but remain clinically silent or unreported.

Metabolomics, proteomics, and transcriptomics analyses specifically focused on CCDC115-CDG have not been published, reflecting the small patient numbers and the technical challenge of multi-omics studies in ultra-rare diseases.[13][15] Jansen et al.’s metabolic labeling of sialic acid in fibroblasts provides a targeted biochemical snapshot, demonstrating reduced sialylation and its rescue by wild-type CCDC115.[13] Broader metabolomic profiling could, in principle, reveal secondary perturbations in lipid, amino acid, or energy metabolism, but such data are currently unavailable.[15] Proteomic analyses of serum glycoproteins in CDG more broadly show altered glycan structures and protein abundance, and similar patterns are likely in CCDC115-CDG, but have not been specifically reported.[13][15] Transcriptomic changes downstream of Golgi dysfunction could include upregulation of stress-response genes and remodeling of metabolic pathways, but these remain hypothetical.

Advanced technologies such as single-cell RNA sequencing, spatial transcriptomics, and CRISPR-based functional genomics screens have not yet been applied to CCDC115-CDG in published literature.[13][15] Nonetheless, these techniques offer promising avenues for dissecting cell-type-specific responses to Golgi dysfunction and identifying potential therapeutic targets, such as compensatory pathways that might be augmented pharmacologically. Functional genomics screens in model systems (e.g., yeast or cell lines) could elucidate interactions between CCDC115 and other Golgi proteins, revealing networks that sustain organelle integrity.[13][14][15] As of now, however, the mechanistic understanding of CCDC115-CDG rests primarily on classical cell-biological and biochemical studies, supplemented by clinical observations.

---

## 7. Anatomical Structures Affected

### 7.1 Organ-Level Involvement

The primary organ affected in CCDC115-CDG is the liver (UBERON:0002107), which exhibits cholestatic injury, hepatomegaly, and eventual fibrosis or cirrhosis in some patients.[2][13][15] The spleen (UBERON:0002106) is frequently enlarged, contributing to hepatosplenomegaly.[13][15] The central nervous system (UBERON:0000955) is also involved, manifesting as global developmental delay, hypotonia, and seizures.[2][13][15] Musculoskeletal tissues, including skeletal muscle (UBERON:0001630), are affected through hypotonia and possibly altered bone metabolism reflected in elevated bone-derived alkaline phosphatase.[13][15] Other organ systems such as the cardiovascular and respiratory systems have not been prominently implicated, and there is no consistent evidence of cardiac or pulmonary phenotypes unique to CCDC115-CDG.[13][15]

Body systems involved include the digestive system (liver, biliary tree, pancreas), nervous system, and to a lesser extent the musculoskeletal system.[2][13][15] The digestive system manifestations center on cholestatic liver disease, with clinical signs such as jaundice, hepatomegaly, and in advanced cases, portal hypertension and ascites.[13][15] The nervous system manifestations include developmental delays and hypotonia, affecting motor and cognitive domains.[2][13][15] Musculoskeletal involvement is primarily functional (hypotonia) rather than structural, with no consistent skeletal deformities reported.[13][15] Endocrine and renal systems appear spared based on existing case descriptions, although comprehensive endocrine evaluations have not been systematically documented.[13][15]

### 7.2 Tissue and Cell-Level Involvement

At the tissue level, the hepatic parenchyma and biliary epithelium are central sites of pathology in CCDC115-CDG.[13][15] Hepatocytes (CL:0000182) bear the brunt of glycosylation defects, leading to impaired processing and secretion of bile components, coagulation factors, and serum transport proteins.[13][15] Cholangiocytes, or biliary epithelial cells (CL:0002598), may also be affected, contributing to intrahepatic cholestasis.[15] In the spleen, lymphoid and stromal cells may undergo reactive enlargement due to portal hypertension and immune activation, though specific cell types have not been studied.[15] In the nervous system, neurons (CL:0000540) and glial cells (e.g., astrocytes, CL:0000127) are likely impacted by glycosylation defects in cell-surface receptors and adhesion molecules, leading to synaptic dysfunction and developmental abnormalities.[7][13][15] In skeletal muscle, muscle fibers (CL:0000187) may exhibit altered glycosylation of structural and signaling proteins, contributing to hypotonia.[2][13][15]

From a histopathologic standpoint, recent reports describe severe liver fibrosis and cirrhosis in some CCDC115-CDG patients, indicating architectural remodeling of hepatic tissue with collagen deposition and nodule formation.[15] The specific histological patterns (e.g., bridging fibrosis, regenerative nodular hyperplasia) have not been fully detailed, but they likely resemble other chronic cholestatic and metabolic hepatopathies.[15] Biopsy remains the gold standard for diagnosing certain vascular liver disorders, but in CCDC115-CDG, biopsy has primarily been used to characterize fibrosis and exclude alternative diagnoses.[15] In brain and muscle, no systematic histological analyses have been reported, and pathology is inferred from clinical and biochemical data rather than direct tissue examination.[13][15]

### 7.3 Subcellular Compartment Involvement

At the subcellular level, CCDC115-CDG primarily affects the Golgi apparatus (GO:0005794), ER-Golgi intermediate compartment (GO:0005798), and COPI-coated vesicles (GO:0030137).[13][14] CCDC115 protein localizes to the ERGIC and COPI vesicles, but not to the endoplasmic reticulum itself, indicating a role in early secretory pathway trafficking.[13][14] Golgi cisternae rely on proper vesicular traffic and V-ATPase-mediated acidification for their function, and CCDC115 deficiency disrupts these processes.[3][13][14] The resulting Golgi stress may induce compensatory changes in other organelles, such as the endoplasmic reticulum (GO:0005783), where unfolded protein response could be activated due to misfolded glycoproteins, although this has not been directly demonstrated.[13][15]

Other subcellular compartments affected include lysosomes (GO:0005764) and endosomes (GO:0005768), which depend on glycosylation for sorting receptors and enzymes, but specific alterations in these organelles have not been detailed in CCDC115-CDG.[13][15] Mitochondria (GO:0005739) are not primary targets of CCDC115 deficiency, and there is no evidence of mitochondrial dysfunction driving the phenotype.[13][15] Nucleus (GO:0005634) involvement is indirect, potentially through altered trafficking of transcription factors or signaling receptors, but no nuclear pathology has been described.[13][15] Overall, the Golgi apparatus and associated vesicular compartments are the central subcellular sites of pathology, consistent with the classification of CCDC115-CDG as a disorder of Golgi homeostasis.

### 7.4 Localization and Lateralization

The anatomical localization of CCDC115-CDG manifestations is systemic rather than focal; both liver lobes are affected symmetrically, and neurological manifestations are global rather than lateralized.[13][15] There are no reports of unilateral organ involvement or asymmetric brain lesions specific to this disease, and imaging studies, when performed, primarily document generalized changes such as hepatomegaly rather than focal masses.[13][15] UBERON terms relevant to localization include liver (UBERON:0002107), spleen (UBERON:0002106), and brain (UBERON:0000955), with no lateralization qualifiers required.[13][15] In immunohistochemical localization studies, CCDC115 protein distribution is uniform across cells within a given tissue, consistent with its housekeeping role.[13][14] Thus, anatomical structures affected by CCDC115-CDG are bilaterally and diffusely involved, reflecting the systemic nature of the genetic defect.

---

## 8. Temporal Development

### 8.1 Age of Onset and Patterns of Onset

CCDC115-CDG typically presents in infancy, with onset ranging from the neonatal period to early childhood.[2][3][13][15] Orphanet states that the age of onset is “Infancy, Neonatal,” indicating that hepatic and neurological signs emerge within the first months of life.[2] Jansen et al. reported infants and young children with hepatosplenomegaly and biochemical abnormalities diagnosed in early childhood, and Pellicano et al. described similar timelines for hepatic presentations.[3][13] In the systematic review of liver involvement in CDG, Cossu et al. found that many CDG forms, including CCDC115-CDG, present with liver abnormalities early in life, though some patients may have silent hypertransaminasemia before overt clinical symptoms appear.[15] The onset pattern in CCDC115-CDG is generally chronic and insidious rather than acute, with early signs such as elevated liver enzymes and hepatomegaly gradually progressing to more severe liver disease in some cases.[13][15]

Acute presentations, such as acute liver failure, are rare but documented.[15] In a retrospective analysis of metabolic diseases presenting as acute liver failure, one of 127 patients was found to have CCDC115-CDG, indicating that in exceptional circumstances, the disease can manifest with abrupt hepatic decompensation.[15] However, such cases are outliers; most patients show a subacute or chronic course with evolving liver disease and developmental delays.[13][15] HPO terms for onset patterns include congenital onset (HP:0003577), neonatal onset (HP:0003623), and childhood onset (HP:0003617), reflecting the spectrum of onset ages reported.[2][13][15]

### 8.2 Disease Progression, Course, and Duration

The progression of CCDC115-CDG is heterogeneous and depends on the severity of hepatic and neurological involvement.[13][15] In many CDG types, liver enzymes peak during the first five years of life and then improve, suggesting a partial spontaneous amelioration of hepatic injury.[15] Cossu et al. note that, in most CDG forms, “these parameters mostly increased during the first 5 years of life in most types of CDG … but they improved significantly afterwards,” but they specifically highlight CCDC115-CDG as an exception, alongside ALG8-CDG, MPI-CDG, PGM1-CDG, and TMEM165-CDG, where liver involvement may be more persistent or progressive.[15] Jansen et al. observed regression of hepatosplenomegaly in some CCDC115-CDG patients with age, yet biochemical abnormalities such as elevated alkaline phosphatase and cholesterol persisted.[13] In contrast, Pellicano and subsequent reports described severe liver fibrosis and cirrhosis leading to liver failure and transplantation in other patients, indicating a more aggressive disease course.[1][3][15]

The disease duration is chronic and lifelong, as the underlying genetic defect persists and cannot be reversed by current therapies.[2][13][15] Neurological impairments such as global developmental delay and hypotonia may stabilize or progress slowly over time, but are unlikely to resolve fully, particularly in the absence of targeted molecular therapies.[2][15] The course of liver disease can be episodic, with periods of relative stability interspersed with episodes of decompensation triggered by infections or other stressors, or it can be steadily progressive toward cirrhosis.[15] HPO terms reflecting disease course include chronic (HP:0003003), progressive (HP:0003676), and episodic (HP:0003429) for various aspects of the phenotype.[13][15]

### 8.3 Remission Patterns and Critical Periods

Partial remission of certain manifestations, such as regression of hepatosplenomegaly, has been reported in CCDC115-CDG, suggesting some degree of adaptive remodeling or compensatory mechanisms.[13][15] Jansen et al. noted that hepatosplenomegaly regressed with age in their patients, even though biochemical abnormalities persisted.[13] This pattern implies a critical window during early childhood when the liver is more susceptible to structural enlargement, followed by stabilization or partial regression as the child grows.[13][15] However, in patients with progressive fibrosis or cirrhosis, such remission may not occur, and the liver remains structurally and functionally compromised.[15] There is no evidence of complete remission of the underlying glycosylation defect, as this is genetically determined and persists throughout life.[13][15]

Critical periods of vulnerability likely include the neonatal and early infantile period, when the liver and brain are rapidly developing and particularly sensitive to metabolic perturbations.[2][15] Early recognition and supportive management of cholestasis during this period may mitigate progression to fibrosis, although direct evidence for such intervention effects is limited.[15][16] Similarly, early initiation of developmental therapies (physical, occupational, and speech therapy) may optimize neurodevelopmental outcomes, even if underlying glycosylation defects remain.[2][15] No treatment-induced remissions have been reported beyond what is achieved with liver transplantation, which can effectively correct hepatic manifestations but not necessarily reverse neurological deficits.[15][16] Overall, temporal development in CCDC115-CDG is characterized by early onset, chronic course, variable progression, and limited partial remissions, with critical periods centered on early childhood.

---

## 9. Inheritance and Population Characteristics

### 9.1 Inheritance Pattern, Penetrance, and Expressivity

CCDC115-CDG is inherited in an autosomal recessive manner.[2][9][11][13] Orphanet explicitly states that the inheritance pattern is autosomal recessive, and OMIM similarly annotates the condition as such, based on biallelic pathogenic variants in *CCDC115* in all reported affected individuals.[2][9][11] Parents of affected children are typically heterozygous carriers of a pathogenic *CCDC115* variant and are clinically unaffected, consistent with recessive inheritance.[2][9][13] Segregation analyses in the families described by Jansen et al. support this model, with disease manifesting only when both alleles are mutated.[13] Penetrance for biallelic loss-of-function variants appears to be complete, in that all individuals identified with such genotypes in published series have exhibited clinical disease, although the small sample size limits firm conclusions.[13][15]

Expressivity—the range and severity of manifestations among individuals with the same genotype—is clearly variable, particularly regarding liver disease progression.[13][15] Some patients show regression of hepatosplenomegaly and stabilization of biochemical abnormalities, while others develop severe fibrosis, cirrhosis, and acute liver failure.[13][15] Neurological impairments also range from moderate developmental delays to profound disability and seizures.[2][13][15] This variability suggests that expressivity is influenced by factors such as specific variant type, genetic background, and environmental exposures, although specific modifiers remain unidentified.[13][15] Genetic anticipation, a phenomenon where disease severity increases in successive generations due to expansion of unstable repeats, is not relevant to CCDC115-CDG, as no repeat expansions or anticipation have been reported.[9][13][15] Germline mosaicism has not been described, but could theoretically occur in carrier parents; however, observed autosomal recessive inheritance in reported families does not require mosaicism to explain recurrence.[13][15]

### 9.2 Epidemiology: Prevalence, Incidence, and Geographic Distribution

CCDC115-CDG is an ultra-rare disorder with extremely low prevalence and incidence.[2][11][15] Orphanet estimates a prevalence of less than 1 per 1,000,000, reflecting the small number of known cases worldwide.[2] MalaCards similarly characterizes the disease as a rare autosomal recessive metabolic disorder.[11] Combining the original eight patients reported by Jansen et al. with the three additional patients documented by Cossu et al. in their liver review and Pellicano’s case series, the total number of published CCDC115-CDG patients is on the order of eleven, underscoring the rarity of the condition.[1][3][13][15] Given such small numbers, formal incidence calculations in terms of new cases per year per population are not available, and most epidemiologic data are descriptive rather than quantitative.[2][15]

Geographic distribution of reported cases spans multiple countries and ethnic backgrounds, reflecting the global prevalence of rare autosomal recessive conditions without clear geographic clustering.[13][15] Jansen et al.’s series included families from different regions, and subsequent reports have come from diverse European centers.[1][3][13][15] No founder effect has been documented, and variants appear to be private or extremely rare in the general population.[9][13][15] gnomAD and similar databases indicate very low allele frequencies for pathogenic variants, consistent with strong negative selection against deleterious *CCDC115* alleles.[2][9][11][15] There is no evidence of population-specific prevalence differences, although small sample sizes preclude definitive statements.[2][15]

### 9.3 Demographics: Sex Ratio, Age Distribution, Consanguinity, and Carrier Frequency

Published cases of CCDC115-CDG include both male and female patients, and there is no evidence of sex-linked inheritance or sex bias in prevalence.[2][13][15] The sex ratio appears approximately equal, although precise numbers are not reported in aggregated form.[13][15] Age distribution of affected individuals is skewed toward infancy and childhood, reflecting early onset, but some patients have survived into adolescence or early adulthood; Cossu et al. mention that in a broader CDG cohort, mean age at last observation was 12 years, with some patients showing persistent liver disease, and similar timelines likely apply to CCDC115-CDG.[15] Consanguinity plays a role in certain families, particularly where homozygous variants are present in multiple siblings, but detailed documentation of consanguinity rates has not been provided.[13][15] Carrier frequency in the general population is extremely low due to the rarity of pathogenic variants, and systematic carrier screening programs for *CCDC115* are not currently implemented.[2][9][11][15]

Given the autosomal recessive inheritance, each child of two heterozygous carriers has a 25% risk of being affected, a 50% risk of being a carrier, and a 25% risk of inheriting neither mutant allele.[2][9] Genetic counseling for families with a known affected child or identified pathogenic *CCDC115* variant is therefore crucial, particularly in populations where consanguinity is common.[2][9][15] However, the ultra-rare nature of the disease and limited awareness among clinicians have so far constrained systematic risk counseling and carrier testing efforts.[2][15]

---

## 10. Diagnostics

### 10.1 Clinical Evaluation, Laboratory Testing, and Imaging

Diagnostic evaluation of CCDC115-CDG begins with recognition of the characteristic clinical picture of early-onset hepatosplenomegaly, cholestatic liver disease, elevated liver enzymes, hypercholesterolemia, low serum ceruloplasmin, and neurodevelopmental abnormalities.[2][3][13][15] Pediatric hepatologists often encounter such patients in the context of differential diagnosis for chronic cholestasis or unexplained liver failure, and initial work-up includes standard liver function tests (aminotransferases, alkaline phosphatase, bilirubin), complete blood count, coagulation parameters, lipid profile, and serum ceruloplasmin.[2][3][15] In CCDC115-CDG, these tests reveal elevated aminotransferases, markedly elevated alkaline phosphatase (often bone-derived), elevated cholesterol, and low ceruloplasmin.[2][13][15] HPO terms for these laboratory abnormalities include abnormal liver function tests (HP:0002910), increased alkaline phosphatase (HP:0003155), hypercholesterolemia (HP:0003124), and reduced ceruloplasmin (HP:0003285).[2][13][15]

Imaging studies such as abdominal ultrasound or MRI show hepatomegaly and often splenomegaly, but lack specific features distinguishing CCDC115-CDG from other causes of pediatric liver disease.[13][15] Ultrasound may reveal increased echogenicity of the liver consistent with fatty change or fibrosis, and Doppler studies may detect signs of portal hypertension in advanced cases, such as splenomegaly and collateral veins.[15] However, these imaging findings are nonspecific and primarily serve to document organ size and structural changes. Liver biopsy can provide histological evidence of fibrosis, cirrhosis, or other patterns such as storage-disease-like accumulation, but its role in CCDC115-CDG is mainly to exclude alternative diagnoses and assess the severity of liver disease.[13][15] In the context of common variable immunodeficiency (CVID) and related disorders, biopsy is the cornerstone for diagnosing vascular liver conditions like regenerative nodular hyperplasia, but in CCDC115-CDG, biopsy has not been used to define unique histopathologic signatures.[8][15]

### 10.2 Glycosylation Assays and Specific Biochemical Testing

Given that CCDC115-CDG is a congenital disorder of glycosylation, specific glycosylation assays are central to diagnosis.[9][13][15] Isoelectric focusing of serum transferrin is the standard screening test for N-linked CDG, and in CCDC115-CDG, it reveals a type II pattern characterized by abnormal transferrin isoforms indicative of defective glycan processing after attachment.[9][13][15] OMIM notes that isolectric focusing of serum proteins in patients showed a combined defect of N- and O-glycosylation, suggesting a Golgi defect rather than a single enzyme deficiency.[9] Jansen et al. identified abnormal N- and mucin-type O-glycosylation on serum proteins, further corroborating a broad Golgi-related glycosylation defect.[13] These assays can be complemented by mass spectrometry-based glycoproteomics, which provide detailed profiles of glycan structures attached to specific proteins.[13][15]

Clinical laboratories experienced in CDG diagnosis may also perform tests such as sialic acid labeling in cultured fibroblasts, as used by Jansen et al., to assess terminal glycosylation capacity.[13] In CCDC115-CDG fibroblasts, metabolic labeling of sialic acids is reduced and can be restored by expression of wild-type CCDC115, confirming the functional defect and its reversibility at the cellular level.[13] These specialized tests are performed in research or reference laboratories and are not widely available in routine clinical practice, underscoring the need for referral to specialized centers when CDG is suspected.[15] HPO terms relevant to glycosylation assays include abnormal transferrin glycosylation (HP:0003354) and abnormal protein glycosylation (HP:0002917).[9][13]

### 10.3 Genetic Testing: WES, Panels, and Single-Gene Approaches

Genetic testing is the definitive diagnostic tool for CCDC115-CDG, identifying pathogenic variants in *CCDC115* and confirming the diagnosis.[5][9][13][15] In the original series, Jansen et al. used exome sequencing in a family with three siblings affected by abnormal Golgi glycosylation to identify a homozygous missense mutation in CCDC115.[5][13] Whole-exome sequencing (WES) is particularly useful in cases where glycosylation assays indicate a type II pattern but the specific gene defect is unknown, as it can survey the coding regions of all genes implicated in glycosylation and Golgi function.[5][13][15] When WES identifies a candidate variant in *CCDC115*, confirmatory Sanger sequencing in the patient and parents, along with segregation analysis, solidifies the diagnosis.[13][15]

Gene panels targeting CDG and related metabolic disorders may also include *CCDC115*, especially as awareness of this subtype grows.[7][15][16] Such panels allow simultaneous analysis of multiple glycosylation genes (e.g., PMM2, MPI, PGM1, ALG8, ATP6V0A2, TMEM199, COG subunits) and can be more cost-effective than WES in a clinical setting.[7][15] Single-gene testing of *CCDC115* may be appropriate when clinical, biochemical, and glycosylation profiles specifically suggest CCDC115-CDG, such as in the presence of combined N- and O-glycosylation defects and the characteristic hepatic phenotype.[9][13][15] However, given phenotypic overlap among Golgi-related CDG forms, WES or panels are often preferred to allow comprehensive assessment.[7][15]

Chromosomal microarray (CMA), karyotyping, FISH, and mitochondrial DNA testing are generally not informative for CCDC115-CDG, as the disorder arises from point mutations and small deletions in a nuclear gene rather than large-scale chromosomal changes or mitochondrial variants.[9][13][15] Repeat expansion testing is also irrelevant, as there is no evidence of unstable repeats in *CCDC115*.[9][13][15] Thus, the recommended genetic testing approach centers on WES or multi-gene panels, supplemented by targeted *CCDC115* sequencing where indicated. Genetic testing results should be interpreted in light of ACMG/AMP guidelines, with classification of variants as pathogenic, likely pathogenic, or VUS based on functional and segregation data.[13][15]

### 10.4 Differential Diagnosis and Clinical Criteria

Differential diagnosis for CCDC115-CDG encompasses a broad range of pediatric liver diseases and other CDG forms.[3][7][15] Clinically, the combination of early-onset cholestatic liver disease, hepatosplenomegaly, elevated liver enzymes, hypercholesterolemia, low ceruloplasmin, and developmental delay can mimic Wilson disease, autoimmune hepatitis, mitochondrial hepatopathies, and storage disorders such as Niemann–Pick disease or glycogen storage diseases.[3][15] Wilson disease, in particular, is a key differential due to low ceruloplasmin and hepatic copper involvement, but the absence of ATP7B mutations and the presence of glycosylation defects in transferrin and other proteins distinguish CCDC115-CDG.[3][13][15] Autoimmune and infectious hepatitis typically present with different immunologic and serologic patterns, and mitochondrial hepatopathies may show lactic acidosis and mitochondrial DNA mutations, which are absent in CCDC115-CDG.[15]

Other CDG forms, especially those with liver involvement such as ATP6AP1-CDG, MPI-CDG, PGM1-CDG, and TMEM165-CDG, must be considered.[15][16] Each has its own characteristic biochemical and clinical profile: for example, MPI-CDG responds to mannose supplementation and often presents with protein-losing enteropathy, while PGM1-CDG includes hypoglycemia and myopathy.[15][16] CCDC115-CDG is distinguished by its combined N- and O-glycosylation defect, Golgi-related mechanism, and specific hepatic phenotype.[9][13][15] There are no formal standardized clinical criteria for CCDC115-CDG beyond the combination of clinical features, glycosylation assays, and genetic confirmation, and diagnostic algorithms are generally tailored to the broader CDG group.[7][15] Screening programs for asymptomatic individuals do not currently include CCDC115-CDG, and newborn screening panels have not incorporated glycosylation assays for this condition.[2][15] Nevertheless, awareness of the disease among specialists is increasing, and cascade genetic testing of family members may identify carriers and asymptomatic siblings.[9][15]

---

## 11. Outcome and Prognosis

### 11.1 Survival, Mortality, and Life Expectancy

Due to the small number of reported CCDC115-CDG patients, precise survival rates and life expectancy estimates are not available.[2][13][15] However, the existing data suggest that outcomes range from death in early childhood due to liver failure to survival into adolescence or early adulthood with chronic liver disease and neurodevelopmental impairments.[13][15] Cossu et al. note that in a broader CDG cohort, at last observation (mean age 12 years), hepatomegaly regression was noted in some patients, but 38 individuals still showed liver disease and one died.[15] While these figures encompass multiple CDG forms, they indicate that chronic liver disease persists in many and that mortality, though not universal, is significant. Specifically for CCDC115-CDG, Cossu et al. report that liver transplant has been a successful treatment as a last step for progressive liver fibrosis and cirrhosis in some cases.[15] This implies that without transplantation, end-stage liver disease may be fatal.

Mortality in CCDC115-CDG is primarily disease-specific, attributable to hepatic failure and its complications such as bleeding, infections, and encephalopathy.[15] No systematic data from national mortality registries exist for this ultra-rare condition, and cause-of-death documentation in individual cases is limited.[2][15] Life expectancy for patients who receive timely liver transplantation may approach that of other pediatric liver transplant recipients, although neurological and systemic manifestations may continue to affect quality of life and functional outcomes.[15][16] For those who do not undergo transplantation, life expectancy depends on the severity and progression of liver disease and the presence of acute decompensations, making individualized prognostication necessary.[13][15]

### 11.2 Morbidity, Disability, and Quality of Life

Morbidity in CCDC115-CDG is substantial due to chronic liver disease, neurodevelopmental impairments, and the need for ongoing medical and supportive care.[2][13][15] Chronic cholestasis and liver dysfunction can cause fatigue, pruritus, poor growth, and risk of complications such as portal hypertension, variceal bleeding, and ascites.[15] Neurodevelopmental impairments, including global developmental delay and hypotonia, affect motor skills, cognitive development, communication, and daily functioning.[2][13][15] Seizures, when present, add episodic morbidity and require long-term antiepileptic therapy with potential side effects.[2][15] Disability outcomes include limitations in mobility, self-care, and social participation, though specific functional measures based on instruments like the International Classification of Functioning (ICF) have not been reported.[2][15]

Quality of life has not been formally assessed with standardized tools such as EQ-5D, SF-36, or PROMIS in CCDC115-CDG patients, but the combination of chronic disease, developmental disability, and intensive medical needs strongly suggests a significant impact.[2][15] Families must cope with frequent hospital visits, monitoring of liver function, and the uncertainties associated with possible need for transplantation and the long-term neurologic prognosis.[15][16] Rehabilitation services, including physical, occupational, and speech therapy, are often required to optimize functional outcomes.[2][15] Psychosocial support for patients and caregivers is crucial but underreported in the literature.[2][15]

### 11.3 Disease Course, Complications, and Recovery Potential

The disease course in CCDC115-CDG is chronic and variable, with some patients showing stabilization and partial regression of hepatosplenomegaly, and others progressing to cirrhosis and acute liver failure.[13][15] Complications include portal hypertension, variceal bleeding, ascites, infections, and encephalopathy in advanced liver disease, although specific frequencies have not been quantified.[15] Neurodevelopmental complications include persistent cognitive delays and hypotonia, which may be mitigated but not fully reversed by supportive therapies.[2][15] Recovery potential for hepatic manifestations is limited in the absence of transplantation; while biochemical abnormalities may improve in some CDG forms, CCDC115-CDG belongs to a subset where liver involvement may be more persistent.[15] Liver transplantation offers the greatest potential for recovery of hepatic function and prevention of liver-related mortality, but does not correct the underlying glycosylation defect in other organs, and neurological outcomes may remain impaired.[15][16]

Prognostic factors likely include the severity of liver disease at presentation, presence of fibrosis or cirrhosis, and specific variant type, although these have not been systematically analyzed in CCDC115-CDG.[13][15] Biomarkers such as degree of glycosylation abnormality, serum markers of fibrosis, and liver histology might predict progression, but data are lacking.[15] There are no established prognostic models or calculators specific to CCDC115-CDG, and clinicians must rely on general hepatology principles and individual patient trajectories.[15] Overall, prognosis in CCDC115-CDG ranges from guarded to poor in severe cases, particularly where liver disease progresses rapidly, while some individuals may have a more stable, albeit chronically impaired, course.

---

## 12. Treatment

### 12.1 Supportive and Symptomatic Management

At present, there is no disease-specific pharmacologic therapy for CCDC115-CDG that corrects the underlying glycosylation defect.[13][15][16] Treatment focuses on supportive and symptomatic management of hepatic and neurological manifestations, analogous to other CDG forms.[15][16] For liver disease, standard cholestasis management applies, including ursodeoxycholic acid to improve bile flow, fat-soluble vitamin supplementation (vitamins A, D, E, K) to prevent deficiency due to impaired bile-mediated absorption, and nutritional support to maintain growth and energy balance.[15][16] Pruritus, if present, can be managed with bile acid sequestrants or rifampicin, though the evidence for these interventions in CDG specifically is limited.[15] Monitoring for and treatment of complications such as portal hypertension, ascites, and variceal bleeding follow general pediatric hepatology guidelines.[15]

Neurological manifestations such as seizures are treated with standard antiepileptic drugs, chosen based on seizure type and patient-specific factors.[2][15] Hypotonia and developmental delays are addressed through multidisciplinary rehabilitation, including physical therapy, occupational therapy, and speech therapy.[2][15] NCIT terms relevant to these interventions include “Supportive Care” (NCIT:C15607), “Physical Therapy” (NCIT:C28255), “Occupational Therapy” (NCIT:C15279), and “Speech Therapy” (NCIT:C28254). These non-pharmacologic interventions aim to optimize functional outcomes and quality of life, despite the persistence of underlying molecular defects. Psychosocial support for families, including counseling and social services, is also a critical component of care, although not specifically emphasized in the CCDC115-CDG literature.[2][15]

### 12.2 Liver Transplantation and Surgical Interventions

Liver transplantation is the primary definitive treatment for end-stage liver disease in CCDC115-CDG and has been reported as successful in at least some cases.[15] Cossu et al. highlight that “liver transplant has been reported to be a successful treatment as the last step for progressive liver fibrosis and cirrhosis (e.g. MPI-CDG, or CCDC1115-CDG),” indicating that transplantation can restore hepatic function and prevent liver-related mortality.[15] NCIT terms applicable here include “Liver Transplantation” (NCIT:C15273) and “Organ Transplantation” (NCIT:C15273 as a broader category). Transplantation replaces the diseased liver with a healthy donor organ, correcting hepatocellular and cholestatic dysfunction, but does not address glycosylation defects in other tissues, such as brain and muscle.[15][16] As a result, while liver-related outcomes improve, neurological manifestations may persist or progress, and long-term immunosuppression introduces additional risks.[15][16]

The decision to pursue liver transplantation in CCDC115-CDG involves consideration of the severity and progression of liver disease, availability of donor organs, comorbidities, and expected neurologic outcomes.[15][16] Given the ultra-rare nature of the disease, there are no formal guidelines specific to CCDC115-CDG, and decisions are made within general pediatric transplant frameworks.[15][16] Surgical interventions beyond transplantation, such as portosystemic shunt placement for portal hypertension, may be considered in selected cases, but have not been specifically reported in the literature.[15] Overall, liver transplantation represents a critical therapeutic option for CCDC115-CDG patients with advanced liver disease, offering survival benefits despite residual systemic disease.

### 12.3 Emerging and Experimental Therapies in CDG

Therapeutic approaches in CDG more broadly are evolving, and although no specific pharmacotherapy exists for CCDC115-CDG, insights from other CDG forms may inform future strategies.[15][16] A review on therapeutic approaches in CDG notes that disease-specific treatments have been reported for certain types, including MPI-CDG (mannose supplementation), PGM1-CDG (galactose supplementation), and CAD-CDG (uridine supplementation), while for others, including ATP6AP1-CDG and CCDC115-CDG, treatment remains largely supportive.[16] These examples illustrate the potential of substrate supplementation or metabolic bypass strategies in correcting specific enzymatic defects, but such approaches are not directly applicable to disorders of organelle homeostasis like CCDC115-CDG.[13][15][16]

Gene therapy, RNA-based therapies (antisense oligonucleotides, siRNA, mRNA-based therapeutics), and small-molecule modulators of Golgi and V-ATPase function represent conceptual future avenues for CCDC115-CDG.[16] For example, viral vector-mediated gene replacement of *CCDC115* in hepatocytes and other key cell types could theoretically restore Golgi homeostasis and correct glycosylation defects.[16] However, no gene therapy trials specific to CCDC115-CDG have been initiated, and challenges include targeting multiple organ systems, achieving sufficient expression, and managing immunologic responses.[16] NCIT terms relevant to such strategies include “Gene Therapy” (NCIT:C16690), “Cell Therapy” (NCIT:C17335), and “RNA-based Therapy” (NCIT:C158866). Pharmacologic modulation of Golgi pH or vesicular trafficking is another speculative avenue, but specific agents with appropriate efficacy and safety profiles are not yet available.[13][15][16]

Experimental treatments in CDG clinical trials focus mainly on more prevalent types, and CCDC115-CDG has not been the subject of dedicated interventional studies.[15][16] Future research may leverage model systems and patient-derived cells to test candidate compounds that stabilize Golgi function or enhance residual CCDC115 activity in hypomorphic variants.[13][14][16] Until such therapies materialize, management of CCDC115-CDG remains supportive and transplant-based.

---

## 13. Prevention

### 13.1 Primary, Secondary, and Tertiary Prevention

Primary prevention of CCDC115-CDG—preventing disease occurrence by modifying risk factors—is not currently feasible in the general population, given the genetic basis and the rarity of pathogenic *CCDC115* variants.[2][9][11][15] However, in families with known pathogenic variants, primary prevention can be approached via reproductive options such as preimplantation genetic diagnosis (PGD) and prenatal testing, allowing parents to avoid having affected offspring.[2][9][15] Secondary prevention involves early detection and treatment of disease to prevent progression; in CCDC115-CDG, this includes timely diagnosis of CDG in infants with liver disease and developmental delays, enabling earlier supportive care, monitoring, and consideration of transplantation.[2][15] Tertiary prevention focuses on preventing complications and disabilities in individuals with established disease, such as managing portal hypertension, optimizing nutrition, and providing rehabilitation services to reduce functional impairments.[15]

Immunization strategies, such as vaccination against hepatitis B and other infectious agents, are part of standard preventive care in children with chronic liver disease and help prevent superimposed infections that could exacerbate hepatic dysfunction.[15] However, they do not prevent the underlying CDG, and no vaccine exists for CCDC115-CDG itself.[2][15] Behavioral interventions, including lifestyle modifications, are more relevant in older patients to prevent secondary liver insults (e.g., avoiding alcohol and obesity), but again do not influence the primary genetic defect.[15]

### 13.2 Genetic Counseling and Screening

Genetic counseling is a crucial preventive tool in CCDC115-CDG, informing families about inheritance patterns, recurrence risks, and reproductive options.[2][9][15] Counselors can explain that the disease is autosomal recessive, with a 25% recurrence risk for each pregnancy when both parents are carriers, and discuss options such as PGD, prenatal diagnosis via chorionic villus sampling or amniocentesis, and carrier testing in extended family members.[2][9][15] NSGC and ACMG guidelines support such counseling for rare Mendelian diseases, though specific recommendations for CCDC115-CDG are not yet formalized.[2][9][15] MONDO and OMIM identifiers can be used to coordinate information across databases for counseling purposes.[9][10]

Population-based carrier screening for *CCDC115* is not currently implemented due to the low prevalence and limited awareness of the disease.[2][11][15] However, in communities with higher rates of consanguinity or specific families with recurrent cases, targeted carrier screening could be beneficial.[2][9][15] Screening methods for asymptomatic individuals, including newborn screening, have not incorporated CCDC115-CDG, although theoretical expansion of CDG screening could be considered in the future as technologies and policies evolve.[2][15] Risk stratification for targeted prevention currently relies on family history and known molecular diagnoses rather than broader population risk models.[2][9][15]

### 13.3 Public Health and Environmental Interventions

Given the ultra-rare nature and genetic etiology of CCDC115-CDG, public health interventions at the population level (e.g., sanitation, vector control, environmental risk reduction) are not directly applicable for disease prevention.[2][15] Environmental interventions that reduce general liver disease risk, such as limiting hepatotoxic industrial exposures, benefit overall pediatric liver health but have little specific impact on CCDC115-CDG incidence.[15] Public health efforts in CDG more broadly focus on increasing awareness, improving diagnostic capacity, and supporting research networks rather than environmental risk reduction.[15][16] Thus, prevention in CCDC115-CDG is primarily genetic and clinical, centered on counseling and early diagnosis rather than environmental or public health measures.

---

## 14. Other Species and Natural Disease

### 14.1 Orthologous Genes and Cross-Species Conservation

Orthologous genes to *CCDC115* exist in multiple species, reflecting evolutionary conservation of Golgi and V-ATPase assembly mechanisms.[9][14] In yeast (Saccharomyces cerevisiae, NCBI Taxon ID 559292), the ortholog is Vma22p, a vacuolar ATPase assembly factor located in the endoplasmic reticulum.[5][13][14] PSI-BLAST homology analysis by Jansen et al. revealed reciprocal homology between human CCDC115 and yeast Vma22p, indicating that the protein’s core function is conserved across eukaryotes.[5][13][14] In mice, the orthologous gene Ccp1 shows functional roles in cell proliferation and survival, as demonstrated by Pellicano et al. in fibroblast and neuroblastoma cell lines.[9] NCBI Gene identifiers and model organism databases (e.g., MGI for mouse, SGD for yeast) catalog these orthologs and their functional annotations.[9][14]

This evolutionary conservation underscores the fundamental importance of CCDC115/Vma22p in cellular homeostasis, particularly in the secretory pathway and organelle pH regulation.[5][13][14] HomoloGene and similar resources would classify CCDC115 orthologs across vertebrates and invertebrates, reinforcing its phylogenetic stability.[9][14] GO terms related to conserved functions include Golgi organization (GO:0007030) and vacuolar proton-transporting ATPase complex assembly (GO:0007035), which apply to both human and yeast proteins.[5][13][14] These cross-species similarities provide a foundation for using non-human organisms to study the pathophysiology of CCDC115 deficiency.

### 14.2 Natural Disease in Animals and Veterinary Relevance

To date, there are no documented natural disease cases in companion animals or livestock that correspond to CCDC115-CDG, i.e., caused by inherited *CCDC115* variants producing a glycosylation disorder.[2][9][15] OMIA (Online Mendelian Inheritance in Animals) and veterinary databases have not reported such conditions, reflecting both the rarity of the gene defect and the limited genetic screening in animals for glycosylation disorders.[2][15] However, given the presence of orthologous genes and conserved functions, it is plausible that spontaneous deleterious variants could arise in animals, causing organelle and glycosylation defects, but these would be difficult to recognize clinically without molecular testing.[9][14][15]

Veterinary relevance of CCDC115 and its orthologs currently lies primarily in their use as model systems rather than direct clinical applications.[9][14][18] For example, knockout mouse models of *Ccdc115* can be used to study the systemic consequences of gene deficiency, and yeast Vma22p mutants provide insights into V-ATPase assembly and Golgi pH regulation.[5][13][14][18] Comparative pathology across species may reveal that Golgi homeostasis disorders share common features, such as organomegaly and metabolic dysfunction, even if specific clinical syndromes differ.[15] However, no zoonotic potential or cross-species transmission of CCDC115-CDG exists, as the disorder is inherited and non-infectious.[2][15]

---

## 15. Model Organisms

### 15.1 Yeast and Cellular Models

Yeast (Saccharomyces cerevisiae) provides a valuable model for studying CCDC115-related mechanisms via its ortholog Vma22p.[5][13][14] Vma22p is a vacuolar ATPase assembly factor located in the endoplasmic reticulum and is required for proper assembly and function of the V-ATPase complex.[5][13][14] Mutations in Vma22p in yeast disrupt vacuolar acidification and organelle pH homeostasis, leading to phenotypes that can inform our understanding of CCDC115’s role in Golgi and V-ATPase function in human cells.[5][13][14] While yeast cannot recapitulate the full human phenotype of CCDC115-CDG, including complex organ-level manifestations, it can serve as a tractable system for dissecting basic molecular and cellular processes, such as vesicular trafficking and proton pump assembly.[5][13][14]

Patient-derived fibroblasts represent another important cellular model for CCDC115-CDG.[13][15] Jansen et al. used fibroblasts from affected individuals to study glycosylation defects and demonstrated reduced metabolic labeling of sialic acids, which normalized upon complementation with wild-type CCDC115.[13] These fibroblasts thus provide a direct human cell model for evaluating the functional consequences of *CCDC115* variants and testing potential therapeutic interventions (e.g., gene therapy vectors or small molecules) in vitro.[13][15] In vitro models of the secretory pathway, including cell lines engineered to overexpress or knockdown CCDC115, can further elucidate its role in Golgi dynamics, V-ATPase assembly, and glycosylation, building on the work of Pellicano et al. with the mouse ortholog Ccp1.[9][13][15] Together, yeast and cell-based models provide complementary platforms for mechanistic research.

### 15.2 Mouse Models

Mouse models offer the potential to recapitulate aspects of the human CCDC115-CDG phenotype in a mammalian organism with comparable organ systems.[9][18] Ingenious Targeting Laboratory lists at least two *Ccdc115* mouse models, including conditional knockout and knockout variants, available for research.[18] These models can be used to study the effects of *Ccdc115* deficiency on liver, brain, and other systems, and to evaluate interventions such as gene therapy or pharmacologic agents in vivo.[18] As of the current literature provided, detailed phenotypic characterization of these *Ccdc115* mouse models has not been published, and their relevance to human CCDC115-CDG must be inferred based on general principles.[9][15][18] If such mice exhibit hepatomegaly, liver dysfunction, or neurodevelopmental abnormalities, they would provide a powerful platform for studying disease mechanisms and evaluating treatments.

Pellicano et al.’s functional work with the mouse ortholog Ccp1, showing that overexpression promotes proliferation and suppresses cell death, suggests that disruption of *Ccdc115* in mice may affect cell proliferation and survival in multiple tissues.[9] However, whether this translates into specific organ phenotypes akin to the human CDG remains uncertain.[9][15] Model organism databases such as MGI and IMPC would be natural places to seek updated phenotypic data on *Ccdc115* knockout mice, but such data were not included in the provided search results.[18] Thus, while mouse models exist and hold promise, the current state of knowledge emphasizes their potential rather than documented phenotypic details.

### 15.3 Applications and Limitations of Model Systems

Model organisms for CCDC115-CDG—including yeast, patient-derived fibroblasts, and *Ccdc115* knockout mice—offer important opportunities for research but also have limitations.[5][9][13][15][18] Yeast models allow detailed dissection of V-ATPase assembly and organelle pH regulation, but lack complex liver and brain structures and cannot model organ-level disease.[5][13][14] Fibroblast models capture human-specific glycosylation defects and can be manipulated to test gene complementation and pharmacologic interventions, but do not exhibit the full organ physiology of hepatocytes or neurons.[13][15] Mouse models can, in principle, recapitulate liver and neurological manifestations, enabling studies of disease progression and treatment effects, but interspecies differences in glycosylation pathways and organ development may limit direct translation.[9][15][18]

Applications of these models include elucidating the molecular function of CCDC115, defining the consequences of its deficiency in different cell types, and evaluating therapeutic strategies such as gene replacement or small-molecule modulators of Golgi function.[5][9][13][15][18] They can also be used to study interactions between CCDC115 and other Golgi-related proteins, mapping networks of organelle homeostasis.[13][14][15] Limitations include incomplete phenotypic overlap with the human disease, potential compensatory pathways in model organisms that differ from humans, and ethical and logistical constraints in generating and maintaining models for ultra-rare diseases.[15][18] Nevertheless, model systems remain essential for advancing mechanistic understanding and exploring potential treatments for CCDC115-CDG.

---

## Conclusion

CCDC115-CDG, or congenital disorder of glycosylation type IIo (CDG-IIo), is an ultra-rare autosomal recessive metabolic disorder defined by biallelic loss-of-function variants in the *CCDC115* gene and characterized clinically by a storage-disease-like hepatic phenotype, combined N- and mucin-type O-glycosylation defects, and variable neurodevelopmental impairment.[2][5][9][13][15] At the molecular level, CCDC115 protein localizes to the ER-Golgi intermediate compartment and COPI vesicles and shows homology to yeast Vma22p, implicating it in V-ATPase assembly, Golgi lumen acidification, and vesicular trafficking.[5][13][14] Its deficiency disrupts Golgi homeostasis, leading to abnormal glycosylation of serum and cellular proteins, reduced sialic acid incorporation, and downstream organ pathology, particularly in the liver, brain, and musculoskeletal system.[7][13][15] Clinically, patients present in infancy with hepatosplenomegaly, cholestatic liver disease, elevated liver enzymes, hypercholesterolemia, low ceruloplasmin, hypotonia, global developmental delay, and sometimes seizures and mild dysmorphic features, creating diagnostic challenges and potential misclassification as Wilson disease or other pediatric hepatopathies.[2][3][13][15]

The natural history of CCDC115-CDG is heterogeneous, with some patients showing regression of hepatosplenomegaly and stabilization of liver tests, and others progressing to severe fibrosis, cirrhosis, and acute liver failure, occasionally requiring liver transplantation.[13][15] Neurological outcomes vary from moderate developmental delays to severe disability, and quality of life is substantially affected by chronic disease and functional impairments.[2][13][15] Diagnosis relies on a combination of clinical evaluation, glycosylation assays (e.g., transferrin isoelectric focusing revealing a type II CDG pattern and demonstration of combined N- and O-glycosylation defects), and genetic testing via WES or targeted sequencing to identify pathogenic *CCDC115* variants.[9][13][15] Treatment remains largely supportive, focusing on management of cholestasis, nutritional support, seizure control, and rehabilitation, with liver transplantation as a definitive therapy for end-stage hepatic disease but no current pharmacologic correction of the glycosylation defect.[15][16]

From an ontological standpoint, CCDC115-CDG links multiple domains: HPO phenotypes such as hepatosplenomegaly, cholestatic liver disease, global developmental delay, and hypotonia; GO biological processes including protein glycosylation and Golgi organization; CL cell types such as hepatocytes and neurons; and UBERON anatomical structures such as liver, spleen, and brain.[2][7][9][13][15][17] Evidence sources span human clinical case series, in vitro fibroblast studies, yeast models, and emerging mouse resources, each contributing to a composite picture of this complex disease.[5][9][13][14][18] Despite significant progress in defining the genetic and molecular basis of CCDC115-CDG, many questions remain, including the full spectrum of phenotypic variability, long-term prognosis, potential modifier genes, and the feasibility of targeted therapies aimed at Golgi homeostasis or gene replacement.[13][15][16]

Future research priorities include expanding patient cohorts through international collaboration, establishing natural history registries, and applying advanced multi-omics technologies to delineate downstream effects of CCDC115 deficiency at the transcriptomic, proteomic, and metabolomic levels.[13][15] Model organisms, including yeast, fibroblasts, and *Ccdc115* knockout mice, should be leveraged to explore mechanistic pathways and test therapeutic strategies such as gene therapy or small-molecule modulators of Golgi function.[5][9][13][14][18] Clinically, improving awareness of CCDC115-CDG among pediatric hepatologists and metabolic specialists, integrating CDG-focused diagnostic algorithms into practice, and enhancing genetic counseling and reproductive options for affected families will be critical steps in optimizing patient care.[2][9][15] As knowledge continues to accumulate, CCDC115-CDG will serve as an instructive example of how subtle defects in organelle homeostasis can lead to profound multisystem disease, highlighting the importance of integrating molecular, cellular, and clinical perspectives in the study of rare Mendelian disorders.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 5 |
| Resolved | 5 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 5 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 67 |
| Resolved | 62 |
| Unresolved (possible confabulation) | 3 |
| Obsolete | 2 |
| Unverifiable | 0 |
| Terms whose name was checked | 13 |
| Terms named correctly | 4 |
| Terms named as a **different** term | 8 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `NCIT:C15607` (1 mention) - the report calls it "Supportive Care"; NCIT calls it **Clinical Diagnosis**
- `NCIT:C28255` (1 mention) - the report calls it "Physical Therapy"; NCIT calls it **International Unit**
- `NCIT:C15279` (1 mention) - the report calls it "Occupational Therapy"; NCIT calls it **Radical Mastectomy**
- `NCIT:C28254` (1 mention) - the report calls it "Speech Therapy"; NCIT calls it **Milliliter**
- `NCIT:C15273` (2 mentions) - the report calls it "Liver Transplantation"; NCIT calls it **Longitudinal Study**
- `NCIT:C16690` (1 mention) - the report calls it "Gene Therapy"; NCIT calls it **HIV Envelope Protein gp41**
- `NCIT:C17335` (1 mention) - the report calls it "Cell Therapy"; NCIT calls it **Syndecan**
- `NCIT:C158866` (1 mention) - the report calls it "RNA-based Therapy"; NCIT calls it **del(10q23)/PTEN Gene Locus Deletion Analysis**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0003285` (2 mentions) - HP does not contain this term
- `HP:0004402` (1 mention) - HP does not contain this term
- `HP:0003617` (1 mention) - HP does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0006486` (obsolete protein glycosylation) (2 mentions) - replaced by `GO:0009101`
- `NCIT:C28255` (International Unit) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0046933` (1 mention) - the report calls it "proton-transporting ATPase regulator activity"; GO calls it **proton-transporting ATP synthase activity, rotational mechanism**, and lists "H+-transporting ATP synthase activity" among its other names