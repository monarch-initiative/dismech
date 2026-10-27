---
provider: perplexity
model: sonar-reasoning-pro
cached: false
start_time: '2026-09-15T20:27:00.031123'
end_time: '2026-09-15T20:29:59.988859'
duration_seconds: 179.96
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Selective IgM Deficiency
  mondo_id: MONDO:0018039
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
citation_count: 15
reference_validation:
  total_references: 8
  verified: 8
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 8
  on_topic: 7
  validator_version: 0.2.1
term_validation:
  total_terms: 54
  verified: 50
  not_found: 4
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.074
  labels_checked: 27
  labels_matching: 13
  labels_mismatched: 11
  mislabelled_terms:
  - term_id: HP:0002318
    reported_labels:
    - 'Typical manifestations: chronic sinusitis'
    ontology_label: Cervical myelopathy
  - term_id: HP:0031800
    reported_labels:
    - abnormal B cell morphology/phenotype
    ontology_label: Elevated circulating apolipoprotein A-II concentration
  - term_id: GO:0002283
    reported_labels:
    - marginal zone B cell differentiation
    ontology_label: neutrophil activation involved in immune response
  - term_id: UBERON:0002048
    reported_labels:
    - spleen
    ontology_label: lung
  - term_id: UBERON:0001961
    reported_labels:
    - bone marrow
    ontology_label: mucosa-associated lymphoid tissue
  - term_id: UBERON:0001825
    reported_labels:
    - upper respiratory tract
    ontology_label: paranasal sinus
  - term_id: UBERON:0001043
    reported_labels:
    - lung
    ontology_label: esophagus
  - term_id: NCIT:C16070
    reported_labels:
    - 'NCIT: antibiotic prophylaxis'
    - Prophylactic antibiotics
    ontology_label: Prostate Cancer Prevention Trial
  - term_id: NCIT:C3443
    reported_labels:
    - 'NCIT: immunoglobulin therapy'
    ontology_label: Vulvar Neoplasm
  - term_id: NCIT:C28784
    reported_labels:
    - 'NCIT terms: antiallergic agent'
    ontology_label: 27-35(27L):MART-1 Peptide
  - term_id: NCIT:C1202
    reported_labels:
    - 'NCIT terms: immunosuppressive agent'
    ontology_label: Prednisolone Acetate
  labels_variant: 3
  unresolved_terms:
  - HP:0002776
  - HP:0004270
  - HP:0003822
  - HP:0002713
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Selective IgM Deficiency
- **MONDO ID:** MONDO:0018039 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Selective IgM Deficiency** covering all of the
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

Selective IgM deficiency (sIgMD) is a rare primary immunodeficiency characterized by isolated low serum IgM (below age‑adjusted reference or <2 SD below mean) with normal IgG and IgA, and a clinical spectrum ranging from asymptomatic individuals to patients with recurrent bacterial infections, allergic disease, and autoimmunity.[5][6][8][11][12] It is recognized by the International Union of Immunological Societies (IUIS) as a distinct primary antibody deficiency, although its etiology, natural history, and optimal management remain incompletely defined.[7][9][12]

---

## 1. Disease Information

**Definition and current understanding**

Selective IgM deficiency (sIgMD; also “selective immunoglobulin M deficiency,” “selective IgM immunodeficiency,” “primary selective IgM deficiency”) is defined as a persistent reduction of serum IgM below two standard deviations (SD) of the age‑adjusted mean (or absolute values <0.20 g/L in children and <0.30 g/L in adults) with normal serum IgG and IgA, and without evidence of other primary or secondary immunodeficiencies.[5][11][12] The IUIS criteria emphasize “absent serum IgM with preserved IgG and IgA concentrations” for the most stringent form.[7][9] 

The Diagnostics 2023 review summarizes the consensus: sIgMD is an isolated IgM deficiency, often detected during evaluation for recurrent infections, allergy, or autoimmunity, but sometimes found incidentally.[1][9][12] Many patients show normal lymphocyte numbers and basic function, and a subset demonstrates normal specific antibody responses, highlighting substantial heterogeneity.[3][5][12]

**Key identifiers**

- MONDO: Selective IgM deficiency – MONDO:0018039 (as given in the query).
- IUIS classification: Primary antibody deficiency, “selective IgM deficiency.”[7][9]
- ICD: No single, universally used ICD‑10/ICD‑11 code specific for sIgMD; patients are typically coded under “other immunodeficiency” or “hypogammaglobulinemia.” This limitation is explicitly noted in recent reviews.[1][5]
- OMIM/Orphanet: Reviews mention that sIgMD is recognized as a primary immunodeficiency but do not consistently quote specific OMIM or Orphanet numeric identifiers, reflecting the nosologic uncertainty.[1][5][12]
- MeSH: Articles are indexed under “Immunoglobulin Deficiency,” “Immunoglobulin M,” and “Primary Immunodeficiency Diseases” rather than a dedicated sIgMD MeSH heading.[3][8][12]

**Common synonyms/alternative names**

- Selective IgM deficiency (sIgMD).[5][6][12][13]  
- Selective immunoglobulin M deficiency.[5][12][13]  
- Selective primary IgM deficiency.[12][13]  
- Selective IgM immunodeficiency.[5][12]  

**Data source type**

Most information derives from:
- Aggregated disease‑level resources (expert society handbooks and web resources from primary immunodeficiency organizations).[4][6][10]  
- Case series and cohort studies (e.g., 62 adult patients; 2019; Pediatrics and allergy multicenter cohort in children).[2][8][15]  
- Narrative and systematic reviews synthesizing published clinical cases and immunologic investigations.[1][5][11][12]  

No large, EHR‑based epidemiologic datasets were identified; current knowledge is largely based on referred cohorts and specialist centers.[1][5][8][12]

---

## 2. Etiology

### 2.1 Disease causal factors

**Genetic and mechanistic factors**

The pathogenesis of sIgMD is currently unclear and appears heterogeneous.[5][12] The 2013 review notes:

> “The pathogenesis of selective IgM deficiency is unclear; decreased T helper activity, increased isotype-specific suppressor T cell activity, and intrinsic B cell defects have been reported.”[12] (PMID:23760686)

Several lines of evidence:

1. **Possible genetic contribution**
   - A subset of cases shows association with 22q11.2 microdeletion, classically linked to DiGeorge syndrome, suggesting that chromosomal defects affecting thymic/lymphoid development can manifest as sIgMD.[12]  
   - “Selective IgM deficiency, in some cases, is associated with 22q11.2 chromosome deletion and few familial cases of selective IgM deficiency have been reported.”[12]  

2. **B‑cell intrinsic abnormalities**
   - In some patients, circulating IgM⁺ B cells are decreased or absent, pointing to defects in IgM‑expressing B‑cell development or survival.[3][12]  
   - Detailed immunophenotyping found increased transitional B cells, decreased marginal zone B cells, and increased CD21^low B cells, suggesting disturbed peripheral B‑cell maturation and regulatory B‑cell subsets.[3]  

3. **T‑cell and regulatory defects (in a subset)**
   - Most patients have normal T‑cell numbers and basic function, but some show decreased T helper function or isotype‑specific suppressor T‑cell activity, supporting an immunoregulatory component.[12]  

Taken together, sIgMD likely represents a phenotypic endpoint (low serum IgM) arising from diverse upstream immunologic defects rather than a single Mendelian gene defect in most cases.[1][5][12]

### 2.2 Risk factors

**Genetic risk factors**

- **22q11.2 deletion**: Reported in some sIgMD patients, suggesting that this microdeletion can predispose to IgM deficiency alongside other immune abnormalities.[12]  
- **Familial cases**: “Few familial cases of selective IgM deficiency have been reported,” implying possible heritable factors, but no specific causative gene has been firmly identified.[12]  

No genome‑wide association studies, ClinVar‑annotated monogenic variants, or ClinGen curated loci specific for sIgMD were reported in the 2017 and 2023 reviews.[1][5][12] Evidence for a clear Mendelian inheritance pattern is therefore weak.

**Environmental and clinical risk factors**

The available literature does not identify classical environmental risk factors (toxins, occupational exposures) for developing sIgMD.[1][5][12] Reported associations are more likely consequences or comorbidities (e.g., infections, autoimmunity) than proven risk factors.

### 2.3 Protective factors

No genetic or environmental protective factors (variants conferring resistance, or lifestyle exposures reducing risk) have been described specifically for sIgMD in recent reviews or cohort studies.[1][5][12] The field generally treats sIgMD as a fixed immunologic state rather than a risk‑modifiable condition.

### 2.4 Gene–environment interactions

No direct gene–environment interaction studies (e.g., formal G×E analyses) are available for sIgMD.[1][5] Conceptually, impaired IgM‑mediated early responses to pathogens may interact with environmental pathogen exposure to determine infection burden, but this is inferred from immunologic principles rather than demonstrated in sIgMD‑specific G×E studies.[5][12]

---

## 3. Phenotypes

### 3.1 Core clinical phenotypes (human clinical evidence)

**Infection‑related phenotypes (symptoms/signs/laboratory)**

Adult cohort of 62 patients (human clinical study, 2019):

> “The majority of patients presented with recurrent and chronic upper and lower respiratory tract infections (73%), most often with recurrent sinusitis (29%), bronchitis (33%), pneumonia (21%), and recurrent urinary tract infections (16%).”[8] (PMID:31970029)

Primary immunodeficiency organization materials similarly state that symptomatic individuals predominantly have bacterial infections.[6][10][12]

Common infection phenotypes and suggested HPO terms:

1. Recurrent upper respiratory tract infections – HP:0002788  
   - Frequency: ~73% in adult cohort when including upper and lower respiratory infections.[8]  
   - Typical manifestations: chronic sinusitis (HP:0002318), recurrent otitis media (HP:0000403), pharyngitis.[6][8][10][12]  
   - Onset: often childhood or early adulthood.[5][8][12]  
   - Severity: usually mild to moderate but can be severe (pneumonia, sepsis).[6][8][12]  
   - Progression: episodic; recurrent episodes over years.[8][12]  
   - Quality of life impact: recurrent respiratory infections impair school/work attendance and daily functioning.[6][8][10][12]

2. Bronchitis (HP:0002776) and pneumonia (HP:0002090)  
   - Bronchitis 33%, pneumonia 21% in adult cohort.[8]  
   - May progress to chronic bronchial disease or structural lung damage in some cases.[5][8][12]

3. Recurrent urinary tract infections – HP:0000010  
   - 16% in adult cohort.[8]  
   - Usually episodic; severity variable.[8][12]

4. Serious invasive infections: meningitis (HP:0004270), sepsis (HP:0100806), cellulitis, osteomyelitis  
   - Patient handbook: “Occasionally cellulitis, sepsis and meningitis have been observed.”[6]  
   - Educational slide set reports meningitis, recurrent multifocal osteomyelitis, pyelonephritis, and sepsis among documented infections.[10]  
   - These events are rare but indicate potential for life‑threatening infection in severe cases.[6][10][12]

**Allergic/atopic phenotypes (symptoms/signs)**

Adult and mixed cohorts show high rates of allergic disease:

> “Approximately 35% of patients had atopic diseases, including allergic rhinitis and asthma.”[8]  

Patient handbook and 2025 educational materials report:

> “Almost 40% of individuals with Selective IgM Deficiency have allergic diseases including hay fever and asthma.”[6]  
> “Allergic diseases – 25–35%.”[10]  

Main atopic phenotypes and HPO terms:

- Allergic rhinitis – HP:0012384.[6][8][10]  
- Asthma – HP:0002099.[6][8][10]  
- Atopic dermatitis – HP:0001047.[10]  
- Angioedema – HP:0001824.[10]  

Frequency among symptomatic individuals: roughly 25–40%.[6][8][10]  
Severity: usually mild to moderate; occasionally persistent, requiring standard allergy/asthma management.[6][8][10]  
Quality of life: chronic allergic symptoms add to infection burden and may further impair daily activities.[6][8][10]

**Autoimmune phenotypes (clinical signs/disease entities)**

Reviews highlight a notable association with autoimmunity:

> “Selective IgM deficiency… is associated with infections, allergic diseases, and autoimmune diseases.”[12]  

Educational materials summarize:

> “Autoimmune diseases – 25–40%.”[10]  

Specific autoimmune conditions reported across case series/reviews include systemic lupus erythematosus, rheumatoid arthritis, immune thrombocytopenia, autoimmune hemolytic anemia, autoimmune thyroiditis, and celiac disease.[5][11][12] (human case series and narrative reviews).

Suggested HPO terms:

- Autoimmune disease – HP:0002960.  
- Autoimmune thrombocytopenia – HP:0001973.  
- Autoimmune hemolytic anemia – HP:0001890.  
- Autoimmune thyroiditis – HP:0100646.  
- Celiac disease – HP:0100323.  

Frequency: ~25–40% among symptomatic sIgMD patients.[5][10][12]  
Course: chronic with flares; may require immunosuppressive therapy.[5][11][12]  
Quality of life: substantial impact due to chronic pain, fatigue, organ involvement, and treatment side effects.[5][11][12]

**Asymptomatic phenotype**

Both the handbook and slides emphasize that many individuals are asymptomatic:

> “Individuals with Selective IgM Deficiency, partial or complete, may not have any symptoms, and therefore, are unrecognized or undiagnosed.”[6]  
> “Selective IgM deficiency may be symptomatic or asymptomatic (50%).”[10]  

Phenotype:

- “No or minimal clinical symptoms despite persistent low serum IgM” – HP:0003822 (asymptomatic).  
- Estimated ~50% asymptomatic in some series.[6][10]  

### 3.2 Immunologic and laboratory phenotypes

Key laboratory features (human immunologic studies):

1. **Serum immunoglobulins**
   - Low IgM (<2 SD below mean or <0.20–0.30 g/L) with normal IgG and IgA; IgE often elevated.[11][12]  
   - Adult cohort: strictly defined low IgM with normal IgG/A; some had decreased IgG4 (5/14).[3]  

2. **Isohemagglutinins and specific antibodies**
   - Very low isohemagglutinin titers: “very low titers of isohemagglutinins (OC 8/8; PC 18/21).”[3]  
   - A subset has impaired IgG antibody responses to pneumococcal polysaccharides.[3][12]  

3. **B‑cell subsets**
   - Study of 15 patients:

> “We found that some patients in our cohort (OC) and published cases (PC) had increased transitional B cell counts (OC 8/9), decreased marginal zone B cell counts (OC 8/9), and increased CD21^low B cell counts (OC 7/9).”[3] (PMID:28730517)

   - Most patients had normal total B‑cell numbers and surface IgM expression.[3]  

Suggested HPO and LOINC terms:

- Low IgM – HP:0002717; LOINC test codes for serum IgM (e.g., 2472‑9).  
- Elevated IgE – HP:0002713.[3][12]  
- Abnormal B‑cell subset distribution – HP:0031800 (abnormal B cell morphology/phenotype).  

### 3.3 Phenotype severity, progression, and quality of life

- Severity: ranges from asymptomatic to recurrent severe infections and significant autoimmunity; most cases have mild–moderate recurrent infections.[5][8][12]  
- Progression: unclear; some patients may remain stable, while a minority progress to broader antibody deficiency resembling common variable immunodeficiency (CVID).[5][11][12]  
- Quality of life: recurrent infections and chronic allergic/autoimmune disease reduce physical functioning and increase healthcare utilization.[6][8][10][11][12]  

---

## 4. Genetic/Molecular Information

### 4.1 Causal genes and variants

No single gene has been definitively established as causative for isolated sIgMD in the majority of patients.[1][5][12] Reviews explicitly state that sIgMD is not yet linked to specific high‑penetrance Mendelian mutations, in contrast to many other primary immunodeficiencies.[1][5]

**Chromosomal abnormalities**

- Association with 22q11.2 microdeletion has been reported in some cases.[12]  
  - This region affects multiple genes involved in thymic and cardiac development, and can manifest with immunodeficiency, including IgM deficiency.[12]  
  - Evidence type: human clinical case reports.

**B‑cell developmental/functional abnormalities**

Functional and phenotypic data (human clinical and in vitro):

- Increased transitional B cells and decreased marginal zone B cells suggest impaired maturation and marginal zone development, which is central to T‑independent IgM responses.[3]  
- Elevated CD21^low B cells (often considered anergic/exhausted B cells) point to chronic immune activation or regulatory dysfunction.[3][5]  
- In a minority, IgM production after stimulation is profoundly impaired.[3]  

These findings support a model of **B‑cell intrinsic dysfunction**, but no specific mutation (e.g., in BCR‑signaling genes) has been consistently identified.[3][5][12]

### 4.2 Modifier genes, epigenetics

- Modifier genes: None formally described for sIgMD; autoimmunity and allergy likely reflect polygenic background rather than sIgMD‑specific modifiers.[5][11][12]  
- Epigenetics: No epigenomic studies (DNA methylation, histone marks) specifically focused on sIgMD were identified.[1][5]  

---

## 5. Environmental Information

The literature does not identify specific environmental, occupational, or toxic exposures causing sIgMD.[1][5][12] Reported infections, allergies, and autoimmune conditions appear to be consequences of the immunodeficiency rather than causal exposures.[5][6][8][12]

Lifestyle factors (smoking, diet, exercise) and infectious agents are relevant for overall infection risk but have not been shown to determine the presence vs absence of sIgMD.[1][5][12]

---

## 6. Mechanism / Pathophysiology

### 6.1 Ordered causal chain (inferred mechanistic pathway)

1. **Underlying immune regulatory or developmental abnormality (often unknown; occasionally 22q11.2 deletion) leads to impaired IgM⁺ B‑cell maturation and/or IgM secretion.**[3][5][12]  
2. **Impaired IgM secretion results in persistently low serum IgM with preserved IgG and IgA levels (selective IgM deficiency phenotype).**[5][11][12]  
3. **Low circulating IgM leads to reduced early-phase opsonization and classical complement pathway activation against encapsulated and other extracellular pathogens.**[5][12] (mechanism inferred from IgM biology)  
4. **Reduced opsonization and complement activation result in increased susceptibility to recurrent bacterial (and some viral/fungal) infections, particularly of the respiratory and urinary tracts, and occasionally invasive infections (sepsis, meningitis).**[6][8][10][12]  
5. **Chronic antigenic stimulation in the context of dysregulated B‑cell subsets (e.g., increased transitional and CD21^low B cells, decreased marginal zone B cells) leads to immune dysregulation, which predisposes to allergic disease and autoimmunity.**[3][5][11][12] (partly inferred)  
6. **Autoimmune processes (e.g., production of autoantibodies, immune complex formation) and chronic inflammation further contribute to organ‑specific manifestations and morbidity (e.g., cytopenias, thyroid disease, arthritis).**[5][11][12]  
7. **In a minority of patients, additional or progressive defects in specific antibody responses (e.g., to pneumococcal polysaccharides) lead to a broader antibody deficiency phenotype approaching CVID.**[3][5][11][12]  

Upstream mechanisms: steps 1–3 (B‑cell and regulatory defects, IgM deficiency).  
Downstream mechanisms: steps 4–7 (infection susceptibility, autoimmunity, chronic inflammation, progression).

### 6.2 Key mechanistic elements

**Immune system involvement**

- sIgMD is fundamentally a **humoral immunodeficiency**, with primary involvement of B cells, antibodies, and complement, but T‑cell and NK‑cell abnormalities have been reported in a subset.[5][12]  
- Innate immunity is often relatively intact; most patients have normal neutrophil function.[12]  

Evidence quote:

> “Innate immunity is relatively intact. T cells, T cell subsets, and T cell functions are normal. However, several patients with selective IgM deficiency and T cell and NK cell defects with Mycobacterium avium intracellulare infections have been reported.”[12]

**Cellular processes and protein dysfunction**

- **B‑cell processes**: altered maturation (transitional → marginal zone), activation, and isotype‑specific secretion.[3][5][12]  
  - Suggested GO terms:  
    - GO:0002312 – B cell activation involved in immune response.  
    - GO:0002283 – marginal zone B cell differentiation.  
- **T‑cell help and suppressor functions**: decreased T helper activity and increased isotype‑specific suppressor T‑cell activity (older immunologic terminology) suggest altered CD4⁺ T‑cell regulation of B‑cell class switching and secretion.[12]  
  - GO:0002520 – immune system development; GO:0002376 – immune system process.  

**Complement and opsonization (inferred from IgM biology)**

- IgM is a potent activator of the classical complement pathway; deficiency reduces C1q binding and downstream complement activation, impairing opsonization of encapsulated bacteria (e.g., Streptococcus pneumoniae).[5][12]  
  - GO:0006956 – complement activation.  

**Autoimmunity and chronic inflammation**

- Autoimmunity likely arises from chronic immune dysregulation, altered B‑cell tolerance (CD21^low B cells often enriched for autoreactive specificities), and possibly imbalanced regulatory T‑cell function.[3][5][11][12]  
  - GO:0002449 – lymphocyte mediated immunity; GO:0002718 – negative regulation of immune system process.  

**Cell types (CL terms)**

- B cell – CL:0000236.  
- Marginal zone B cell – CL:0000827.  
- Transitional B cell – CL:0000837.  
- CD21^low B cell (exhausted/anergic B cell subset; not fully standardized in CL but falls under “B cell”).  
- CD4⁺ T helper cell – CL:0000625.  
- Regulatory T cell – CL:0000815.  

---

## 7. Anatomical Structures Affected

### 7.1 Organ‑level involvement

Primary organs/body systems:

- **Immune/hematologic system**: bone marrow, peripheral blood, spleen, lymph nodes.[5][12]  
  - UBERON:0000178 (blood), UBERON:0002048 (spleen), UBERON:0000029 (lymph node), UBERON:0001961 (bone marrow).  
- **Respiratory system**: nasal sinuses, bronchi, lungs – due to recurrent URTIs, sinusitis, bronchitis, pneumonia.[6][8][10][12]  
  - UBERON:0001825 (upper respiratory tract), UBERON:0001043 (lung), UBERON:0002185 (bronchus).  
- **Genitourinary system**: bladder, kidneys (recurrent UTIs, pyelonephritis).[8][10][12]  
  - UBERON:0001255 (urinary bladder), UBERON:0002113 (kidney).  

Secondary involvement:

- Organs affected by autoimmune disease (e.g., joints, thyroid, small intestine, hematopoietic system).[5][11][12]  

### 7.2 Tissue and cell level

- Primary tissue type: lymphoid tissue (spleen, lymph nodes), hematopoietic tissue (bone marrow).[5][12]  
- Primary cell populations: B cells (transitional, marginal zone, CD21^low), T helper cells, regulatory T cells; occasionally NK cells.[3][5][12]  

### 7.3 Subcellular level (inferred)

- IgM synthesis and secretion involve the endoplasmic reticulum, Golgi apparatus, and secretory vesicles in B cells.[5][12]  
  - GO:0005788 (endoplasmic reticulum), GO:0005794 (Golgi apparatus), GO:0030133 (transport vesicle).  
- B‑cell receptor (BCR) signaling involves the plasma membrane and associated signaling complexes.[5][12]  
  - GO:0005886 (plasma membrane).  

### 7.4 Localization and lateralization

Infections typically involve bilateral respiratory structures (e.g., both lungs) and are not characteristically lateralized.[6][8][10][12] Autoimmune manifestations follow disease‑specific patterns (e.g., symmetric arthritis in RA).[5][11][12]

---

## 8. Temporal Development

### 8.1 Onset

- Age of onset: sIgMD can present in childhood or adulthood; pediatric and adult cohorts are both reported.[2][8][12][15]  
- Onset pattern: usually chronic/insidious—recurrent infections over months to years rather than acute catastrophic onset.[5][8][12]  

### 8.2 Progression and disease course

- Course: many patients have a stable pattern of recurrent infections; some remain asymptomatic.[6][8][10][12]  
- Progression: a minority may evolve toward broader hypogammaglobulinemia or CVID‑like phenotypes, but data are limited and largely anecdotal.[5][11][12]  
- Duration: typically lifelong once identified; spontaneous normalization of IgM appears uncommon, though data are sparse compared to selective IgA deficiency.[5][12]  

### 8.3 Remission patterns and critical periods

- Infection burden may fluctuate with age, environmental exposures, and vaccination status.[5][8][12]  
- No well‑defined “critical periods” comparable to neonatal immune vulnerabilities are described specifically for sIgMD.[1][5][12]  

---

## 9. Inheritance and Population

### 9.1 Epidemiology

- Prevalence and incidence: true prevalence is unknown; sIgMD is considered rare, and existing data are derived from immunology clinic cohorts rather than population surveys.[1][5][6][12]  
- Reviews emphasize that sIgMD is “underestimated” and likely underdiagnosed due to asymptomatic cases and lack of routine IgM testing.[5][13]  

### 9.2 Inheritance pattern and genetic features

- Inheritance: no consistent autosomal dominant, autosomal recessive, X‑linked, or mitochondrial inheritance pattern has been demonstrated.[1][5][12]  
- Familial clustering: a few familial cases suggest possible genetic contribution, but penetrance, expressivity, and mode of inheritance are unclear.[12]  
- Anticipation, founder effects, consanguinity: not documented as specific features of sIgMD in the current literature.[1][5][12]  

### 9.3 Population demographics

- Sex ratio: not consistently reported; adult cohort included both sexes, but specific ratios were not highlighted in the abstract.[8]  
- Age distribution: includes children and adults; adult cohort (62 patients) illustrates that sIgMD is not confined to pediatric age.[2][8][15]  
- Ethnic/geographic distribution: no clear ethnic or geographic predilection has been identified; published series come from multiple countries.[1][5][8][12][13]  

---

## 10. Diagnostics

### 10.1 Clinical laboratory criteria

Diagnostic criteria (summarized from crossroad review, handbook, and IUIS):

> “Selective IgM deficiency (sIgMD) is an immunodeficiency characterised by low serum IgM levels (<0.20 g/L in children and <0.30 g/L in adults or <2 SD below the age-adjusted mean), alongside normal number and function of B and T lymphocytes, normal serum IgG and IgA levels (the IgE levels can be increased) and without other identifiable immunodeficiency.”[11]

Primary immunodeficiency resources add:

> “The diagnosis of partial selective IgM deficiency is made if the serum IgM level is below two standard deviations of the mean for age-matched controls. Complete selective IgM deficiency is diagnosed with serum IgM levels <5 mg/dl.”[4][6]

Key diagnostic steps:

1. **Serum immunoglobulin measurement**
   - Confirm low IgM with age‑adjusted reference ranges, normal IgG and IgA.[4][6][11][12]  
   - Evaluate IgG subclasses (e.g., IgG4) and IgE as they may show abnormalities.[3][11][12]  

2. **Specific antibody testing**
   - Measure isohemagglutinins (often very low) and responses to protein/polysaccharide vaccines (e.g., pneumococcal) to assess functional antibody production.[3][5][12]  

3. **Lymphocyte subset analysis**
   - B‑cell, T‑cell, and NK‑cell counts; B‑cell subset phenotyping can reveal characteristic changes (transitional, marginal zone, CD21^low).[3][12]  

4. **Exclusion of secondary causes**
   - Rule out protein‑losing conditions (nephrotic syndrome, enteropathy), hematologic malignancies, immunosuppressive drugs, and severe systemic diseases that can lower IgM.[5][12]  

Suggested LOINC terms: serum IgM, IgG, IgA, IgE tests; lymphocyte subset panels.

### 10.2 Genetic testing

Because no specific causative gene is known, routine genetic testing for sIgMD is not standardized:

- Genetic testing is mainly considered to identify associated conditions (e.g., 22q11.2 deletion) or to rule out other defined primary immunodeficiencies.[5][12]  
- Whole exome or genome sequencing may be used in research contexts for patients with complex or syndromic presentations.[1][5]  

### 10.3 Omics‑based diagnostics

No established RNA‑seq, proteomic, or metabolomic diagnostic signatures specific to sIgMD have been reported.[1][5]

### 10.4 Clinical criteria and differential diagnosis

Clinical criteria:

- Recurrent bacterial infections (especially respiratory and urinary) and/or allergic/autoimmune manifestations in a patient with persistently low IgM and normal IgG/A, without secondary causes.[5][6][8][11][12]  

Differential diagnoses:

- Common variable immunodeficiency (CVID) – typically shows low IgG (±IgA) plus impaired specific responses; sIgMD has preserved IgG/A.[5][11][12]  
- Secondary hypogammaglobulinemia (protein loss, immunosuppressive therapy, hematologic malignancy).[5][12]  
- Selective IgA deficiency – low IgA, normal IgM; different pattern.[5]  

Screening:

- There are no population‑level screening programs (e.g., newborn screening) for sIgMD; diagnosis is usually triggered by symptoms or incidental lab findings.[1][5][6][12]  

---

## 11. Outcome / Prognosis

### 11.1 Survival and mortality

No large survival or mortality datasets exist specifically for sIgMD.[1][5] Available information suggests:

- Most patients have normal life expectancy when appropriately managed, though severe infections or autoimmune complications can be life‑threatening in individual cases.[5][6][12]  
- Mortality appears low compared with more severe combined immunodeficiencies.[5][12]  

### 11.2 Morbidity, disability, quality of life

- Morbidity is driven by recurrent respiratory and urinary infections, chronic allergic disease, and autoimmune complications.[6][8][10][11][12]  
- Recurrent infections (73% in adult cohort) substantially impact daily functioning and may cause school/work absenteeism.[8]  
- Autoimmune diseases (25–40%) and chronic allergies further reduce quality of life via pain, fatigue, organ dysfunction, and treatment burden.[5][10][11][12]  

Validated QOL measures (EQ‑5D, SF‑36) have not been specifically reported for sIgMD; impact is inferred from clinical burden.[1][5][8][12]

### 11.3 Disease course and complications

Common complications:

- Chronic sinusitis and bronchial disease.[6][8][10][12]  
- Serious infections (sepsis, meningitis, osteomyelitis).[6][10][12]  
- Autoimmune cytopenias, thyroid disease, arthritis, and other organ‑specific autoimmunity.[5][11][12]  

Recovery potential:

- Many patients achieve good control of infections with prophylactic antibiotics and/or immunoglobulin replacement when indicated.[5][6][12]  
- Autoimmune disease outcomes depend on standard rheumatologic/endocrine management.[5][11][12]  

Prognostic factors (inferred):

- Severity and frequency of infections.  
- Presence of autoimmune disease.  
- Coexisting immune defects (e.g., impaired specific antibody responses).[3][5][12]  

---

## 12. Treatment

### 12.1 Pharmacotherapy (human clinical evidence)

There is no IgM‑specific replacement product; treatment focuses on infection prophylaxis, immunoglobulin replacement (IgG) when indicated, and management of comorbid allergy/autoimmunity.[5][6][12]

**1. Infection management and prophylaxis**

- **Acute treatment**: standard antibiotics guided by culture and local resistance patterns.[5][6][12]  
  - NCIT: anti‑infective agent (NCIT:C281).  
- **Prophylactic antibiotics**: considered for patients with frequent or severe infections.[5][6][12]  
  - NCIT: antibiotic prophylaxis (NCIT:C16070).  

**2. Immunoglobulin replacement therapy (IVIG/SCIG)**

> “Specific IgG antibody responses against pneumococcus polysaccharides are impaired in a subset of patients with selective IgM deficiency.”[12]

For patients with concomitant specific antibody deficiency (e.g., poor response to polysaccharide vaccines) and recurrent serious infections:

- Intravenous or subcutaneous IgG replacement may reduce infection frequency.[5][12]  
  - NCIT: immunoglobulin therapy (NCIT:C3443).  

**3. Management of allergic disease**

- Standard therapies for allergic rhinitis (antihistamines, intranasal steroids), asthma (inhaled corticosteroids, bronchodilators), and atopic dermatitis (topical steroids, emollients) are applied as in non‑immunodeficient populations.[5][6][8][10]  
  - NCIT terms: antiallergic agent (NCIT:C28784), anti‑asthmatic agent (NCIT:C287).  

**4. Management of autoimmunity**

- Autoimmune cytopenias: corticosteroids, immunosuppressants, or biologics as per standard guidelines.[5][11][12]  
- Autoimmune thyroiditis, arthritis, celiac disease: disease‑specific therapies (thyroxine replacement, DMARDs, gluten‑free diet).[5][11][12]  
  - NCIT terms: immunosuppressive agent (NCIT:C1202), disease‑modifying antirheumatic drug (NCIT:C93322).

### 12.2 Advanced therapeutics

- No gene therapy, cell therapy, or targeted biologics specifically developed for sIgMD have been reported.[1][5][12]  
- Biologic therapies (e.g., TNF inhibitors, rituximab) may be used to treat autoimmune complications, but they are not directed at correcting IgM deficiency itself.[5][11][12]  

### 12.3 Treatment outcomes

Evidence is mostly case‑based:

- IVIG appears beneficial in reducing infection frequency in patients with impaired specific antibody responses.[5][12]  
- Antibiotic prophylaxis is effective in reducing recurrent infections in many cases.[5][6][12]  
- Autoimmune disease outcomes are comparable to those in non‑sIgMD patients when appropriately treated.[5][11][12]  

---

## 13. Prevention

### 13.1 Primary, secondary, tertiary prevention

**Primary prevention**

- No known strategies to prevent the occurrence of sIgMD itself, given the uncertain etiology and lack of defined causal genes.[1][5][12]  

**Secondary prevention (early detection)**

- Routine immunoglobulin testing in patients with recurrent infections, allergy, or autoimmunity can detect sIgMD earlier.[5][6][12]  
- Early recognition allows timely prophylactic measures and vaccination strategies.[5][6][12]  

**Tertiary prevention (complication prevention)**

- Vaccinations (e.g., pneumococcal, influenza) to reduce infection risk.[5][6][12]  
- Prophylactic antibiotics and/or IVIG in high‑risk patients to prevent severe infections and hospitalizations.[5][6][12]  
- Early and optimal treatment of autoimmunity to prevent organ damage.[5][11][12]  

### 13.2 Immunization and prophylaxis

- Standard immunization schedules are recommended; additional polysaccharide or conjugate vaccines (e.g., pneumococcal) may be particularly important.[5][6][12]  
- Prophylactic antibiotics (NCIT:C16070) and IgG replacement therapy (NCIT:C3443) serve as tertiary prevention of severe infections.[5][6][12]  

### 13.3 Counseling

- Genetic counseling is limited by the lack of defined inheritance patterns but may be useful in families with 22q11.2 deletion or multiple affected relatives.[12]  
- Patients should be counseled on infection risk, prompt evaluation of febrile illnesses, and adherence to prophylactic regimens.[5][6][12]  

---

## 14. Other Species / Natural Disease

The reviewed human‑focused literature does not describe naturally occurring selective IgM deficiency as a defined veterinary syndrome in other species.[1][5][12] IgM deficiency models in animals (e.g., IgM‑knockout mice) exist as experimental tools but are not discussed in detail in the sIgMD clinical reviews.[1][5]

---

## 15. Model Organisms

No dedicated, clinically oriented model organism of “selective IgM deficiency” mirroring the human syndrome is described in the clinical reviews.[1][5][12] Experimental IgM‑deficient mice have been used more broadly to study IgM function (e.g., complement activation, early immune responses), but these are not yet integrated into a formal sIgMD disease model framework in the human clinical literature.[1][5]

---

## Key Evidence Quotes (for knowledge base linking)

Below are selected abstract quotes with PMIDs that directly support major claims:

1. Pathogenesis and associations (review; human clinical and mechanistic data):

> “The most common clinical manifestation of selective IgM deficiency is infections with extracellular and intracellular bacteria, viruses, and fungi… Selective IgM deficiency, in some cases, is associated with 22q11.2 chromosome deletion and few familial cases of selective IgM deficiency have been reported… In a subset of patients with selective IgM deficiency circulating IgM+ B cells are decreased or completely lacking. Specific IgG antibody responses against pneumococcus polysaccharides are impaired in a subset of patients… The pathogenesis of selective IgM deficiency is unclear; decreased T helper activity, increased isotype-specific suppressor T cell activity, and intrinsic B cell defects have been reported.”[12] (PMID:23760686)

2. Adult clinical cohort:

> “The majority of patients presented with recurrent and chronic upper and lower respiratory tract infections (73%), most often with recurrent sinusitis (29%), bronchitis (33%), pneumonia (21%), and recurrent urinary tract infections (16%). Approximately 35% of patients had atopic diseases, including allergic rhinitis and asthma.”[8] (PMID:31970029)

3. Detailed immunologic phenotype:

> “We found that some patients in our cohort (OC) and published cases (PC) had increased transitional B cell counts (OC 8/9), decreased marginal zone B cell counts (OC 8/9), and increased CD21^low B cell counts (OC 7/9)… A majority of the patients had normal antibody production to protein and polysaccharide antigens, basic lymphocyte subset counts, and expression of surface IgM molecules on B cells.”[3] (PMID:28730517)

4. Diagnostic definition (crossroad review):

> “Selective IgM deficiency (sIgMD) is an immunodeficiency characterised by low serum IgM levels (<0.20 g/L in children and <0.30 g/L in adults or <2 SD below the age-adjusted mean), alongside normal number and function of B and T lymphocytes, normal serum IgG and IgA levels (the IgE levels can be increased) and without other identifiable immunodeficiency.”[11]

5. Patient handbook (clinical spectrum):

> “Individuals with Selective IgM Deficiency have low levels or lack immunoglobulin M (IgM) but have normal levels of IgA, and IgG. These individuals may have no illness, whereas others develop a variety of illnesses including infections, allergy, and autoimmunity… Individuals with Selective IgM Deficiency, partial or complete, may not have any symptoms… Those individuals who do have symptoms commonly suffer from infections, allergies, and autoimmune diseases… Of those who are symptomatic, approximately 80% present with predominant bacterial infections… Almost 40% of individuals with Selective IgM Deficiency have allergic diseases including hay fever and asthma.”[6]

6. Educational slide set (frequency of phenotypes):

> “Selective IgM deficiency may be symptomatic or asymptomatic (50%). Most common clinical presentations in symptomatic patients are: Infections – 80%; Allergic diseases – 25–35%; Autoimmune diseases – 25–40%… Infections: Upper respiratory tract infections, Otitis media, Sinusitis, Bronchitis, Pneumonia, Meningitis, Recurrent UTI, Pyelonephritis, Recurrent multifocal osteomyelitis, Sepsis… Allergic rhinitis, Allergic asthma, Atopic dermatitis, Angioedema.”[10]

These evidence items, combined with the ontology suggestions above (HPO, GO, CL, UBERON, NCIT, MONDO), provide a structured basis for populating a disease knowledge base entry for selective IgM deficiency.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 8 |
| On topic | 7 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 54 |
| Resolved | 50 |
| Unresolved (possible confabulation) | 4 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 27 |
| Terms named correctly | 13 |
| Terms named as a **different** term | 11 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0002318` (1 mention) - the report calls it "Typical manifestations: chronic sinusitis"; HP calls it **Cervical myelopathy**
- `HP:0031800` (1 mention) - the report calls it "abnormal B cell morphology/phenotype"; HP calls it **Elevated circulating apolipoprotein A-II concentration**
- `GO:0002283` (1 mention) - the report calls it "marginal zone B cell differentiation"; GO calls it **neutrophil activation involved in immune response**
- `UBERON:0002048` (1 mention) - the report calls it "spleen"; UBERON calls it **lung**
- `UBERON:0001961` (1 mention) - the report calls it "bone marrow"; UBERON calls it **mucosa-associated lymphoid tissue**
- `UBERON:0001825` (1 mention) - the report calls it "upper respiratory tract"; UBERON calls it **paranasal sinus**
- `UBERON:0001043` (1 mention) - the report calls it "lung"; UBERON calls it **esophagus**
- `NCIT:C16070` (2 mentions) - the report calls it "NCIT: antibiotic prophylaxis", "Prophylactic antibiotics"; NCIT calls it **Prostate Cancer Prevention Trial**
- `NCIT:C3443` (2 mentions) - the report calls it "NCIT: immunoglobulin therapy"; NCIT calls it **Vulvar Neoplasm**
- `NCIT:C28784` (1 mention) - the report calls it "NCIT terms: antiallergic agent"; NCIT calls it **27-35(27L):MART-1 Peptide**
- `NCIT:C1202` (1 mention) - the report calls it "NCIT terms: immunosuppressive agent"; NCIT calls it **Prednisolone Acetate**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0002776` (1 mention), reported as "Bronchitis" - HP does not contain this term
- `HP:0004270` (1 mention), reported as "Serious invasive infections: meningitis" - HP does not contain this term
- `HP:0003822` (1 mention), reported as "asymptomatic" - HP does not contain this term
- `HP:0002713` (1 mention) - HP does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0002718` (1 mention) - the report calls it "negative regulation of immune system process"; GO calls it **regulation of cytokine production involved in immune response**, and lists "regulation of cytokine biosynthetic process involved in immune response" among its other names
- `GO:0005788` (1 mention) - the report calls it "endoplasmic reticulum"; GO calls it **endoplasmic reticulum lumen**
- `NCIT:C281` (1 mention) - the report calls it "NCIT: anti‑infective agent"; NCIT calls it **Antiviral Agent**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `NCIT:C16070` - called "NCIT: antibiotic prophylaxis", "Prophylactic antibiotics"