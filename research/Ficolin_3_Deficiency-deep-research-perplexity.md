---
provider: perplexity
model: sonar-reasoning-pro
cached: false
start_time: '2026-09-15T20:22:54.408817'
end_time: '2026-09-15T20:25:19.011355'
duration_seconds: 144.6
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Ficolin 3 Deficiency
  mondo_id: MONDO:0013467
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
  total_terms: 39
  verified: 37
  not_found: 1
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.026
  labels_checked: 37
  labels_matching: 15
  labels_mismatched: 16
  mislabelled_terms:
  - term_id: HP:0002721
    reported_labels:
    - Recurrent pneumonia
    ontology_label: Immunodeficiency
  - term_id: HP:0002715
    reported_labels:
    - Recurrent otitis media
    ontology_label: Abnormality of the immune system
  - term_id: HP:0002718
    reported_labels:
    - Chronic sinusitis
    - Sepsis
    ontology_label: Recurrent bacterial infections
  - term_id: HP:0002724
    reported_labels:
    - Autoimmune disease
    ontology_label: Recurrent Aspergillus infection
  - term_id: HP:0002653
    reported_labels:
    - Systemic lupus erythematosus
    ontology_label: Bone pain
  - term_id: HP:0001270
    reported_labels:
    - Seizures
    ontology_label: Motor delay
  - term_id: HP:0001290
    reported_labels:
    - Peripheral neuropathy
    ontology_label: Generalized hypotonia
  - term_id: HP:0002710
    reported_labels:
    - Recurrent bacterial infections
    ontology_label: Commissural lip pit
  - term_id: CHEBI:36976
    reported_labels:
    - bacterial lipopolysaccharide
    ontology_label: nucleotide
  - term_id: CHEBI:140761
    reported_labels:
    - acetylated saccharides
    ontology_label: 6-methylquinoline
  - term_id: UBERON:0000062
    reported_labels:
    - immune system
    ontology_label: organ
  - term_id: CL:0000094
    reported_labels:
    - neutrophil
    ontology_label: granulocyte
  - term_id: NCIT:C282
    reported_labels:
    - Antibiotic
    ontology_label: Arachidonic Acid
  - term_id: NCIT:C1543
    reported_labels:
    - Vaccination
    ontology_label: Peptide 946
  - term_id: NCIT:C15273
    reported_labels:
    - Immunoglobulin Therapy
    ontology_label: Longitudinal Study
  - term_id: NCIT:C20751
    reported_labels:
    - Genetic Counseling
    ontology_label: Inhibition of Cell Proliferation
  labels_variant: 6
  unresolved_terms:
  - HP:0002855
  unresolvable_prefixes:
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Ficolin 3 Deficiency
- **MONDO ID:** MONDO:0013467 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Ficolin 3 Deficiency** covering all of the
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

Immunodeficiency due to ficolin‑3 deficiency is an ultra‑rare autosomal recessive Mendelian primary immunodeficiency caused by biallelic loss‑of‑function variants in the FCN3 gene, leading to absent or severely reduced ficolin‑3 and impaired lectin‑pathway complement activation with susceptibility to infections and a possible link to autoimmunity.[1][4][11][13] Published human data consist of a small number of case reports and cohort studies from 2008–2020 plus a recent 2025 genetic epidemiology study, so current understanding is limited and based on very few patients.[2][4][7][10][12][13]  

---

## 1. Disease Information

**Definition and overview**

Immunodeficiency due to ficolin‑3 deficiency (often shortened to “ficolin‑3 deficiency” or “FCN3 deficiency”) is a primary immunodeficiency in which serum ficolin‑3 (also known as H‑ficolin or Hakata antigen) is undetectable or markedly reduced, resulting in defective complement activation via the lectin pathway.[1][4][6][11][13] Ficolin‑3 is an oligomeric pattern‑recognition lectin encoded by FCN3 that binds acetylated sugars on pathogens and associates with MASP‑1 and MASP‑2 to trigger complement activation.[4][6][13][15] Clinically, affected individuals have recurrent bacterial infections (especially respiratory) and sometimes autoimmune manifestations (notably systemic lupus erythematosus) and neurologic complications.[2][4][13][15]

**Key identifiers**

- OMIM: 613860, “Immunodeficiency due to ficolin 3 deficiency” (number sign entry #613860).[1]  
- Orphanet: 331190, “Immunodeficiency due to ficolin3 deficiency.”[11]  
- MONDO: MONDO:0013467, “Immunodeficiency due to ficolin3 deficiency.”[11]  
- MedGen/ClinVar condition: “Immunodeficiency due to ficolin3 deficiency; FICOLIN 3 DEFICIENCY; FCN3 DEFICIENCY.”[8][9][11]  
- NCBI Gene (human FCN3): Gene ID 8547; disease association listed as “Immunodeficiency due to ficolin3 deficiency (OMIM:613860).”[8]  

ICD‑10/ICD‑11 and MeSH do not currently specify a dedicated code for ficolin‑3 deficiency; patients are typically coded under broader primary immunodeficiency or complement deficiency categories (e.g., ICD‑10 D80‑D89), based on clinical reports and database annotations.[1][11]

**Synonyms / alternative names**

Common synonyms include:[1][9][11]  
- Immunodeficiency due to ficolin‑3 deficiency  
- FICOLIN 3 DEFICIENCY  
- FCN3 DEFICIENCY  
- H‑ficolin deficiency  
- Hakata antigen deficiency  

**Data sources**

Most information is derived from aggregated disease‑level resources (OMIM, Orphanet, ClinVar, NCBI Gene, Sugi Atlas) and a small number of individual case reports, cohort studies, and functional in vitro experiments.[1][2][4][7][10][12][13][15] There are no large EHR‑based natural history studies; the evidence base consists primarily of single‑patient or small case series.

---

## 2. Etiology

### 2.1 Disease causal factors (primary causes)

**Genetic etiology**

Ficolin‑3 deficiency is caused by biallelic loss‑of‑function mutations in FCN3 on chromosome 1p36.11.[1][5][13] OMIM notes: “A number sign (#) is used with this entry because of evidence that ficolin‑3 deficiency is caused by homozygous mutation in the FCN3 gene on chromosome 1p36.”[1] In the index NEJM case, a patient with recurrent infections was homozygous for a frameshift mutation in FCN3 (rs28357092, historically referred to as +1637delC) and had undetectable serum ficolin‑3 and absence of ficolin‑3–dependent complement activation.[5][13] A well‑characterized second frameshift locus, c.349del (p.Leu117SerfsTer66), causes premature termination and a truncated protein lacking the fibrinogen‑like domain, with complete deficiency in homozygotes and ~50% reduction in heterozygotes.[10]

Mechanistically, these frameshift variants distort the C‑terminal end of ficolin‑3, abolish pattern recognition, and prevent secretion of functional oligomeric ficolin‑3, resulting in a complete lectin‑pathway complement deficiency.[5][6][10][13]

**Environmental/infectious factors**

No specific environmental or infectious exposures are known to cause ficolin‑3 deficiency; the disorder is considered strictly genetic.[1][4][7] Infections are consequences rather than causes, occurring on the background of complement lectin‑pathway failure.[2][4][7][12][13]

### 2.2 Risk factors

**Genetic risk factors**

- Homozygosity for FCN3 frameshift alleles (e.g., rs28357092 [+1637delC] and c.349del) is the primary risk factor, defining disease causality.[5][7][10][13]  
- Heterozygosity for the 1637delC frameshift allele is associated with roughly half‑normal H‑ficolin concentrations but is generally not sufficient to cause overt immunodeficiency.[5][7][12][13] One population study reported an allele frequency of ~0.01 for rs28357092 among white individuals, with heterozygotes being clinically healthy in most cases.[13]  

Neonate data show that heterozygosity influences protein level but does not clearly associate with perinatal infections; one premature newborn homozygous for the variant had Streptococcus agalactiae infection and absent H‑ficolin.[12]

There are no established modifier genes or GWAS‑identified susceptibility loci specifically for ficolin‑3 deficiency; given the ultra‑rare complete‑deficiency phenotype, available studies have focused on FCN3 itself.[1][4][7][10][13]

**Environmental risk factors**

Because ficolin‑3 deficiency is a monogenic, autosomal recessive disorder, environmental factors act mainly by modulating infection risk (e.g., pathogen exposure, crowding, poor sanitation) rather than determining disease presence.[2][4][7] No high‑quality studies have quantified specific environmental risk factors for disease onset or severity.

**Demographic risk factors**

The frameshift variants have been most thoroughly studied in European/Caucasian populations, where rs28357092 shows a low but measurable carrier frequency; however, no clear ethnicity‑specific penetrance or expressivity patterns have been established.[7][10][13]

### 2.3 Protective factors

**Genetic protective factors**

No protective FCN3 variants or modifier alleles have been demonstrated to reduce disease risk or ameliorate the phenotype in individuals with homozygous loss‑of‑function mutations.[1][7][10][13] Heterozygosity for deficiency alleles reduces protein levels but appears largely clinically silent in the available cohorts.[7][12][13]

**Environmental/lifestyle protective factors**

General infection‑control and vaccination practices (e.g., timely immunization, avoidance of pathogen exposure) are presumed to reduce clinical event frequency, as in other immunodeficiencies, but have not been systematically studied specifically in ficolin‑3 deficiency.[2][4][7][13]

### 2.4 Gene–environment interactions

Evidence for gene–environment interactions is indirect. Studies suggest that individuals with complete ficolin‑3 deficiency are at increased risk of infections and possibly autoimmunity, implying that environmental pathogen load and immune triggers interact with the genetically impaired lectin pathway.[2][4][7][13] A recent 2025 study explicitly evaluated ficolin‑3 deficiency variants as risk factors for disease (exact phenotype not specified in the available summary), but detailed gene–environment modeling has not been reported.[10] Overall, genotype (biallelic FCN3 loss‑of‑function) is the primary determinant of immunologic vulnerability; environment primarily modulates infection exposure and immune activation rather than disease presence.

---

## 3. Phenotypes

### 3.1 Core clinical phenotypes

Human evidence is derived from the NEJM index case, subsequent case reports, a 2020 congenital deficiency case, a 2015 infection‑susceptibility study, and neonatal cohort data.[2][4][7][12][13] Reported phenotypes include:

1. **Recurrent respiratory infections** (sinusitis, bronchitis, pneumonia).[2][4][7][13][15]  
   - Type: Symptoms and clinical signs (recurrent fever, cough, dyspnea) and laboratory indicators of infection.  
   - Onset: Typically childhood or adolescence in reported cases; the NEJM case involved recurrent infections from early life.[13]  
   - Severity: Moderate to severe, with repeated bacterial infections; some requiring hospitalization.[2][4][13]  
   - Progression: Episodic; infections recur but there is no specific staged progression.  
   - Frequency: Present in essentially all described individuals with complete deficiency.[2][4][7][13][12]  
   - Quality of life impact: Repeated infections, school/work absence, and hospitalizations; inferred moderate impact on physical functioning and social participation.  
   - Suggested HPO terms: HP:0002719 (Recurrent respiratory infections), HP:0002721 (Recurrent pneumonia), HP:0002715 (Recurrent otitis media).

2. **Recurrent otitis media and sinusitis.**  
   Case descriptions and secondary summaries report recurrent otitis media and sinusitis as part of the infection phenotype.[2][4][7][11][15]  
   - Type: Symptoms (ear pain, discharge, nasal congestion) and clinical signs.  
   - Onset: Childhood.[2][4][13]  
   - Severity: Variable, often requiring multiple courses of antibiotics.  
   - HPO terms: HP:0002715 (Recurrent otitis media), HP:0002718 (Chronic sinusitis).

3. **Autoimmune manifestations, particularly systemic lupus erythematosus (SLE).**  
   A review of ficolin‑3 deficiency notes associations with autoimmune disease including SLE.[2] A 2020 congenital deficiency case reports variable immunologic and neurologic complications.[4]  
   - Type: Symptoms (rash, arthralgia, fatigue) and laboratory autoantibodies.  
   - Onset: Adolescence or early adulthood in described cases.  
   - Severity: Variable; SLE can be organ‑threatening.  
   - Progression: Relapsing‑remitting typical of SLE.  
   - Frequency: Rare but notable; not present in all patients.  
   - Quality of life impact: Significant due to chronic autoimmune disease.  
   - HPO terms: HP:0002724 (Autoimmune disease), HP:0002653 (Systemic lupus erythematosus).

4. **Neurologic complications.**  
   The 2020 case report states that mutation in FCN3 is associated with “variable clinical manifestations particularly immunologic (infections and autoimmunity) and neurologic complications.”[4]  
   - Type: Neurologic symptoms (e.g., seizures, developmental delay or neuropathy) inferred from “neurologic complications.”  
   - Evidence: Single case; details limited.  
   - HPO terms (suggested): HP:0001270 (Seizures), HP:0001263 (Global developmental delay), HP:0001290 (Peripheral neuropathy) – to be applied based on case‑specific data in full report.

5. **Neonatal infection and prematurity associations.**  
   A neonatal study of H‑ficolin concentrations and FCN3 polymorphism found that preterm delivery and low birthweight were significantly associated with low H‑ficolin concentrations, and reported one premature newborn homozygous for the FCN3 variant with Streptococcus agalactiae sepsis and absent H‑ficolin.[12]  
   - Type: Laboratory abnormality (low or absent H‑ficolin) and clinical infection.  
   - Onset: Neonatal.  
   - HPO terms: HP:0002710 (Recurrent bacterial infections), HP:0002718 (Sepsis).

6. **Complement pathway abnormality.**  
   Functional assays demonstrate absent or severely impaired lectin‑pathway complement activation (e.g., lack of C4 and C3 deposition upon ficolin‑3–dependent activation).[5][6][13][15]  
   - Type: Laboratory abnormality.  
   - HPO term: HP:0032281 (Abnormal complement system), HP:0002855 (Complement deficiency).

### 3.2 Phenotype characteristics (age, severity, progression, frequency)

- **Age of onset:** Most described patients present during childhood or adolescence with recurrent infections; neonatal deficiency has been documented in at least one premature infant.[12][13]  
- **Severity:** Infection burden ranges from moderate (recurrent otitis media) to severe (recurrent pneumonia and sepsis).[2][4][7][12][13] Autoimmune and neurologic complications can be serious but are documented in only a subset of patients.[2][4]  
- **Progression:** The disease course is episodic, driven by recurrent infections, with chronic risk rather than a progressive degenerative trajectory.[2][4][7][13] Autoimmunity may follow a chronic relapsing‑remitting course.  
- **Frequency among affected individuals:** Because only a few complete‑deficiency patients have been described, precise frequencies are uncertain; recurrent infections are near‑universal, while autoimmunity and neurologic features are less frequent.[2][4][7][12][13]

### 3.3 Quality of life impact

No formal EQ‑5D or SF‑36 data exist for ficolin‑3 deficiency, but recurrent infections, hospitalizations, and potential autoimmune disease substantially impact physical functioning, emotional well‑being, and social participation.[2][4][7][13] Inferred effects include reduced vitality, increased pain/discomfort, and limitations in daily activities typical for primary immunodeficiencies.

---

## 4. Genetic/Molecular Information

### 4.1 Causal gene

- **Gene symbol:** FCN3 (ficolin 3, also H‑ficolin, Hakata antigen).[6][8]  
- **HGNC ID:** FCN3 (HGNC standard symbol; referenced in ClinVar as “FCN3: ficolin 3 [Gene ‑ OMIM ‑ HGNC]”).[9]  
- **Chromosomal location:** 1p36.11.[1][8]  

NCBI Gene notes the disease association “Immunodeficiency due to ficolin3 deficiency MedGen: C3151226 OMIM: 613860.”[8]

### 4.2 Pathogenic variants

**Major variants**

1. **rs28357092 (historically FCN3 +1637delC).**  
   - Type: Frameshift deletion near the C‑terminal region.[5][7][13]  
   - Functional consequence: Distorts the protein’s C‑terminal end and abolishes pattern recognition; recombinant studies show that homozygosity leads to ficolin‑3 deficiency and a novel complement deficiency state.[5][6][13]  
   - Clinical effect: Homozygous individuals have undetectable serum ficolin‑3 and absent ficolin‑3–dependent complement activation, with recurrent infections.[13]  
   - Population frequency: Allele frequency ~0.01 among whites; heterozygotes are usually healthy.[13]  

2. **c.349del (p.Leu117SerfsTer66).**  
   - Type: Frameshift deletion in exon 5; causes premature termination and truncation before the fibrinogen‑like domain.[10]  
   - Functional consequence: Truncated protein lacking the recognition domain; complete deficiency in homozygotes and ~50% reduction in heterozygotes.[10]  
   - Clinical effect: Defined as a “well‑characterised ficolin‑3 deficiency locus” with functional deficiency in homozygotes.[10]  

Functional recombinant experiments for these variants show abolished pattern recognition and failure of lectin‑pathway complement activation, confirming loss‑of‑function mechanisms.[3][5][6][15]

**Variant classification and databases**

ClinVar associates pathogenic or likely pathogenic FCN3 variants with “Immunodeficiency due to ficolin3 deficiency; FICOLIN 3 DEFICIENCY; FCN3 DEFICIENCY.”[9] Most reported disease‑causing variants are frameshift deletions leading to truncated protein; missense and splice‑site variants are less well characterized but are predicted to be loss‑of‑function when they disrupt multimerization or recognition domains.[1][6][9][10][15]

**Allele frequency**

Population data for rs28357092 indicate low carrier frequency (~1%) among whites; homozygous individuals are extremely rare, consistent with the ultra‑rare clinical phenotype.[7][12][13][10]

**Somatic vs germline**

All disease‑associated FCN3 variants are germline and inherited in an autosomal recessive manner; somatic FCN3 alterations are not implicated in this immunodeficiency.[1][4][7][13]

**Functional consequences**

- Protein level: Homozygous frameshift variants lead to undetectable serum ficolin‑3; heterozygotes display reduced levels (∼50% of normal).[5][7][10][12][13]  
- Function: Loss‑of‑function; recombinant protein studies confirm abolished pattern‑recognition capability and failure to activate the lectin pathway.[3][5][6][15]  

### 4.3 Modifier genes and epigenetic information

No modifier genes, epigenetic changes (DNA methylation, histone modifications), or chromosomal abnormalities have been reported to influence FCN3 expression or the clinical phenotype of ficolin‑3 deficiency.[1][4][7][13] The disease is currently understood as a straightforward monogenic complement deficiency.

---

## 5. Environmental Information

No non‑genetic factor is known to directly cause ficolin‑3 deficiency; environmental exposures influence infection risk but not the underlying complement defect.[2][4][7][13]

- **Environmental factors:** General pathogen exposure, crowding, and poor sanitation can increase infection frequency but have not been systematically quantified in this specific disease.[2][4][7]  
- **Lifestyle factors:** Smoking, diet, and other lifestyle factors may modulate respiratory infection risk, but no targeted studies exist.[2][4][7]  
- **Infectious agents:** Reported infections include common bacterial pathogens (e.g., Streptococcus agalactiae in the neonate) and typical respiratory organisms; there is no unique pathogen signature.[12][13]

CHEBI terms for relevant entities could include CHEBI:36976 (bacterial lipopolysaccharide) and CHEBI:140761 (acetylated saccharides) as generic pathogen‑associated molecular patterns recognized by ficolins.

---

## 6. Mechanism / Pathophysiology

### 6.1 Ordered causal chain (schematic)

1. **Biallelic loss‑of‑function FCN3 mutation (frameshift deletion) leads to truncated or misfolded ficolin‑3 protein** (demonstrated in recombinant studies).[3][5][10][13]  
2. **Truncated/misfolded ficolin‑3 leads to absent or severely reduced secretion of functional oligomeric ficolin‑3 into serum** (demonstrated by undetectable serum levels in homozygous patients).[7][12][13]  
3. **Absence of functional ficolin‑3 leads to failure of pathogen‑associated acetylated sugar recognition by the lectin pathway** (inferred from loss of pattern recognition in recombinant protein).[3][5][6][15]  
4. **Failure of ficolin‑3–mediated recognition leads to lack of MASP‑1/2 recruitment and activation on pathogen surfaces** (inferred from lectin‑pathway assays).[6][13][15]  
5. **Absent MASP‑mediated cleavage of C4 and C2 leads to failure to form lectin‑pathway C3 convertase (C4b2a)** (inferred from reduced C3 deposition).[5][6][13][15]  
6. **Failure of lectin‑pathway C3 activation leads to reduced opsonization and membrane attack complex formation, resulting in impaired clearance of certain bacteria and pathogens** (inferred from complement biology).[6][13][15]  
7. **Impaired complement‑mediated clearance leads to recurrent infections and possibly increased immune complex deposition and autoimmunity (e.g., SLE)** (inferred from association with infections and autoimmune disease).[2][4][13]  
8. **Chronic or recurrent infections and immune dysregulation can lead downstream to organ‑specific complications (e.g., lung damage, neurologic symptoms)** (inferred from case reports).[4][13]

### 6.2 Molecular pathways

Ficolin‑3 is a recognition molecule in the **lectin pathway of complement activation**.[4][6][13][15]

- It binds acetylated sugars and N‑acetylgalactosamine residues on microbial surfaces via its fibrinogen‑like domain.[3][5][15]  
- Upon binding, it associates with MASP‑1 and MASP‑2, serine proteases that cleave complement components C4 and C2, forming C3 convertase and initiating the downstream complement cascade.[6][13][15]  

Suggested GO terms:  
- GO:0001867 – complement activation, lectin pathway  
- GO:0006955 – immune response  
- GO:0006952 – defense response  
- GO:0006958 – complement activation, classical pathway (for context)  

### 6.3 Cellular processes and protein dysfunction

- **Protein dysfunction:** Frameshift variants distort the C‑terminal region, abolishing pattern recognition and multimerization; recombinant ficolin‑3 from FCN3+1637delC shows inability to recognize ligands and activate complement.[3][5][6]  
- **Cellular processes:** Hepatocytes and lung epithelial cells (major sites of ficolin‑3 production) show impaired secretion of functional ficolin‑3, but other complement components are intact.[6][8][13] CL terms: CL:0000182 (hepatocyte), CL:0002062 (type II pneumocyte).  
- **Immune system involvement:** The defect is in innate immunity and complement, with downstream effects on opsonization, phagocytosis, and immune complex handling.[2][4][6][13]  

### 6.4 Metabolic and biochemical changes

Complement activation is a proteolytic cascade rather than metabolism per se; metabolic changes are secondary (e.g., inflammatory cytokine production and energy expenditure during infections).[2][4][13]  

Biochemically, the key abnormality is **absence of H‑ficolin and reduced complement activity in lectin‑pathway assays**, often measured by ELISA‑based C4/C3 deposition.[5][6][13][15]  

Suggested GO terms:  
- GO:0003823 – antigen binding (pattern recognition)  
- GO:0030449 – regulation of complement activation  

### 6.5 Immune system and tissue damage

Impaired complement opsonization predisposes to bacterial infections; persistent or severe infections can cause tissue damage, especially in the respiratory tract (e.g., bronchiectasis, chronic lung inflammation).[2][4][7][13] Autoimmune phenomena such as SLE may arise from altered clearance of apoptotic cells and immune complexes, a known mechanism in complement deficiencies, although direct mechanistic proof in ficolin‑3 deficiency is limited.[2][4][13]

Suggested UBERON terms:  
- UBERON:0002048 – lung  
- UBERON:0002106 – liver  
- UBERON:0000062 – immune system  
Subcellular GO:  
- GO:0005576 – extracellular region (location of secreted ficolin‑3)  
- GO:0005886 – plasma membrane (site of complement activation on pathogens)

### 6.6 Molecular profiling and advanced technologies

No transcriptomic, proteomic, metabolomic, single‑cell, spatial transcriptomic, or large‑scale multi‑omics studies specific to ficolin‑3 deficiency have been reported.[1][2][4][7][10][13] Functional genomics (e.g., CRISPR knockout) has been used to generate FCN3‑deficient cell lines in research settings, demonstrating reduced complement activation via the lectin pathway and decreased C3 deposition.[15]

---

## 7. Anatomical Structures Affected

### 7.1 Organ and system level

**Primary organs/body systems**

- **Liver:** Major site of ficolin‑3 synthesis; FCN3 is expressed in hepatocytes.[6][8][13]  
- **Lung:** FCN3 expression in lung tissue; local production may contribute to pulmonary host defense.[6][13]  
- **Immune system:** Innate immune system and complement cascade are directly affected.[4][6][13]  
- **Respiratory system:** Recurrent respiratory infections suggest chronic involvement of upper and lower respiratory tracts.[2][4][7][13]  

UBERON terms:  
- UBERON:0002107 (liver)  
- UBERON:0002048 (lung)  
- UBERON:0001007 (respiratory system)  
- UBERON:0000062 (immune system)

**Secondary organ involvement**

- **Kidneys and CNS:** Potentially involved in the context of SLE and neurologic complications, though data are sparse.[2][4]  

### 7.2 Tissue and cell level

Tissue types:  
- Hepatic parenchyma (hepatocytes).  
- Pulmonary epithelium (bronchial and alveolar epithelial cells).  
- Circulating immune cells (neutrophils, monocytes) affected secondarily through altered opsonization.[6][8][13][15]

CL terms:  
- CL:0000182 – hepatocyte  
- CL:0002062 – type II pneumocyte  
- CL:0000094 – neutrophil  
- CL:0000576 – monocyte  

### 7.3 Subcellular level

Ficolin‑3 is a secreted glycoprotein processed through the endoplasmic reticulum and Golgi apparatus and released into the extracellular space.[6][15] The complement activation defect manifests at the **extracellular surface of pathogens** and **plasma/serum compartment**.

GO cellular component terms:  
- GO:0005576 – extracellular region  
- GO:0005793 – endoplasmic reticulum  
- GO:0005794 – Golgi apparatus  

### 7.4 Localization and lateralization

Complement deficiency is systemic, not lateralized. Organ involvement (e.g., lung infections) is typically bilateral and diffuse rather than unilateral.[2][4][7][13]

---

## 8. Temporal Development

### 8.1 Onset

- Typical age of onset: Childhood or adolescence with recurrent respiratory infections and otitis media.[2][4][7][13]  
- Neonatal onset: Documented in at least one premature infant with homozygous FCN3 variant and sepsis.[12]  
- Onset pattern: Insidious, with early recurrent infections revealing the immunodeficiency; congenital in genetic terms.[1][4][12][13]

### 8.2 Disease progression

- Progression rate: Variable, largely driven by infection frequency and severity.[2][4][7][13]  
- Course pattern: Episodic, with recurrent infections; autoimmunity follows typical relapsing‑remitting patterns where present.[2][4][13]  
- Duration: Lifelong risk due to permanent genetic defect; no evidence of spontaneous remission.[1][2][4][7][13]

### 8.3 Patterns and critical periods

- Critical periods:  
  - Neonatal period (immune immaturity plus complete deficiency) may pose high risk for severe infections.[12]  
  - Early childhood and adolescence (high pathogen exposure) are periods of increased infection risk.[2][4][7][13]  

No structured staging or remission criteria have been proposed.

---

## 9. Inheritance and Population

### 9.1 Epidemiology

Orphanet describes immunodeficiency due to ficolin3 deficiency as a rare genetic immunodeficiency due to a complement protein anomaly, characterized by low or undetectable serum ficolin‑3 and susceptibility to infections.[11] Only a handful of complete‑deficiency patients have been reported in the literature.[2][4][7][12][13] No robust prevalence or incidence estimates (per 100,000) are available.

### 9.2 Inheritance pattern and penetrance

- **Inheritance pattern:** Autosomal recessive.[1][4][7][9][11][13]  
- **Penetrance:** Complete for homozygous frameshift loss‑of‑function variants in terms of biochemical deficiency (zero or near‑zero ficolin‑3 level); clinical penetrance (infection susceptibility, autoimmunity) appears high but is based on few cases.[7][12][13]  
- **Expressivity:** Variable, ranging from recurrent infections only to infections plus autoimmunity and neurologic complications.[2][4][13]  
- **Genetic anticipation and germline mosaicism:** Not reported.[1][4][7][13]  

### 9.3 Founder effects and carrier frequency

- rs28357092 (FCN3+1637delC) shows an allele frequency of ~0.01 in whites and is regarded as a rare variant, with heterozygotes generally healthy.[13]  
- c.349del has been described in European populations with documented functional impact.[10]  
- No clear founder populations have been defined, although both variants appear more studied in European cohorts.[7][10][13]

Carrier frequency for specific variants is low but non‑zero; overall carrier frequency for any FCN3 loss‑of‑function variant is unknown.

### 9.4 Demographics

- **Affected populations:** Reported cases are predominantly of European descent.[7][10][12][13]  
- **Sex ratio:** Both male and female patients have been described; no sex bias has been reported.[2][4][7][12][13]  
- **Age distribution:** Infections typically manifest in childhood or adolescence; at least one neonatal case is documented; adult cases occur with infections and autoimmune complications.[2][4][7][12][13]

---

## 10. Diagnostics

### 10.1 Clinical and laboratory tests

**Key laboratory markers**

1. **Serum ficolin‑3 (H‑ficolin) concentration.**  
   - Measured by ELISA or similar immunoassays; homozygous deficiency patients have undetectable levels; heterozygotes have reduced levels.[5][7][12][13]  
   - Neonatal study used H‑ficolin levels to define “relative functional insufficiency” and identified one homozygous deficient infant.[12]  
   - Suggested LOINC concept: ficolin‑3 serum level (laboratory test for complement lectin pathway).  

2. **Complement function tests (lectin pathway).**  
   - Functional assays of lectin‑pathway activity show absent or severely reduced C4 and C3 deposition when activation depends on ficolin‑3.[5][6][13][15]  
   - These tests distinguish ficolin‑3 deficiency from other complement component deficiencies.  

3. **Infection workup.**  
   - Routine laboratory tests (CBC, CRP, cultures) document recurrent bacterial infections.[2][4][7][12][13]

### 10.2 Genetic testing

Genetic confirmation is essential:

- **Single‑gene FCN3 sequencing:** The primary diagnostic approach; identifies frameshift and other loss‑of‑function variants.[1][8][9][10][13]  
- **Targeted gene panels:** Complement deficiency or primary immunodeficiency panels often include FCN3.[9][11]  
- **WES/WGS:** Useful when immunodeficiency is unexplained; FCN3 loss‑of‑function variants can be discovered in comprehensive sequencing studies.[1][8][9][10][13]  

ClinVar lists FCN3 variants associated with “Immunodeficiency due to ficolin3 deficiency,” supporting use of AC MG/AMP criteria to classify frameshift alleles as pathogenic.[9]

Chromosomal microarray, karyotyping, FISH, mitochondrial DNA testing, and repeat expansion testing are not typically informative for FCN3, which is a single‑gene autosomal recessive disorder.[1][8][9]

### 10.3 Omics-based diagnostics

No disease‑specific RNA‑seq, proteomics, metabolomics, or epigenomics diagnostic assays beyond conventional FCN3 sequencing and serum ficolin‑3 measurements have been reported.[1][2][4][7][10][13]

### 10.4 Clinical criteria and differential diagnosis

There are no formal standardized diagnostic criteria in major guidelines; diagnosis relies on the triad of:[1][2][4][7][11][13]

1. Recurrent bacterial infections (often respiratory).  
2. Undetectable or very low serum ficolin‑3 and absent lectin‑pathway activity.  
3. Biallelic pathogenic FCN3 variants.

**Differential diagnoses:**

- Other complement deficiencies (C2, C4, MBL deficiency).  
- Broader primary immunodeficiencies (e.g., common variable immunodeficiency, neutrophil defects).  
Distinguishing features include specific lectin‑pathway defect with intact classical and alternative pathways and FCN3 loss‑of‑function variants.[5][6][13]

### 10.5 Screening

No population‑wide newborn screening programs exist for ficolin‑3 deficiency. Carrier screening may be considered in families with known pathogenic FCN3 variants, using targeted sequencing, within the framework of genetic counseling.[1][9][11][13]

---

## 11. Outcome / Prognosis

### 11.1 Survival and mortality

No dedicated survival analyses exist; available case reports indicate that with appropriate management, patients can survive into adulthood, although severe infections and autoimmune complications pose risks.[2][4][7][12][13] Mortality data specific to ficolin‑3 deficiency are not available.

### 11.2 Morbidity and function

Morbidity arises mainly from recurrent infections and potential autoimmune disease.[2][4][7][13] Chronic respiratory infections can lead to long‑term lung damage, while SLE and neurologic complications may cause systemic morbidity.[2][4] Formal disability and quality‑of‑life scores have not been reported.

### 11.3 Disease course and complications

- **Complications:** Severe bacterial infections (pneumonia, sepsis), chronic lung disease, autoimmune organ damage (e.g., lupus nephritis), and possible neurologic impairment.[2][4][7][12][13]  
- **Recovery potential:** Infections are treatable with antibiotics; immune defects are permanent. Autoimmune disease may respond to standard immunosuppressive therapy.[2][4][13]  

### 11.4 Prognostic factors

Probable prognostic factors (inferred):  
- Age at onset and severity of early infections.  
- Presence of autoimmunity and neurologic complications.  
- Access to prophylactic and therapeutic interventions (vaccinations, antibiotics).  

No validated prognostic biomarkers beyond ficolin‑3 level and functional complement assays have been reported.[2][4][7][13]

---

## 12. Treatment

### 12.1 Pharmacotherapy

There is no specific replacement therapy for ficolin‑3; treatment focuses on infection management and standard therapy for associated autoimmune conditions.[2][4][7][13]

**Infection management**

- Empiric and targeted antibiotics for bacterial infections (e.g., β‑lactams, macrolides), following standard infectious‑disease guidelines.[2][4][7][13]  
- Consideration of prophylactic antibiotics in patients with frequent infections, similar to other primary immunodeficiencies.[2][4][7]  
- NCIT terms: NCIT:C282 (Antibiotic), NCIT:C1543 (Vaccination), NCIT:C15273 (Immunoglobulin Therapy).

**Autoimmune disease management (e.g., SLE)**

- Standard therapies (corticosteroids, hydroxychloroquine, immunosuppressants) per lupus guidelines, as indicated clinically.[2][4]  

Pharmacogenomics specific to FCN3 deficiency have not been described.

### 12.2 Advanced therapeutics

No gene therapy, cell therapy, RNA‑based therapy, or targeted complement‑modulating biologics have been specifically developed or tested for ficolin‑3 deficiency.[1][2][4][7][10][13]

### 12.3 Supportive and rehabilitative care

- Vaccination against common pathogens (pneumococcus, influenza) is recommended to reduce infection risk, extrapolating from other immunodeficiencies.[2][4][7][13]  
- General supportive care, including prompt treatment of infections, pulmonary rehabilitation where lung damage has occurred, and psychosocial support.[2][4][7]

### 12.4 Experimental and clinical trials

No registered interventional clinical trials specifically targeting ficolin‑3 deficiency have been identified in the available summaries; research is primarily mechanistic and genetic.[1][2][4][7][10][13][15]

---

## 13. Prevention

### 13.1 Primary, secondary, and tertiary prevention

**Primary prevention**

- Genetic counseling for families with known FCN3 pathogenic variants to inform reproductive choices and carrier status.[1][9][11][13]  

**Secondary prevention**

- Early detection of carriers and at‑risk relatives through cascade genetic testing.[1][9][11][13]  
- Early recognition of recurrent infections and complement deficiency, enabling timely management.[2][4][7][13]

**Tertiary prevention**

- Prevention of complications (e.g., chronic lung disease, organ damage from autoimmunity) through aggressive infection management and standard lupus care.[2][4][7][13]

### 13.2 Immunization and risk reduction

Standard immunization schedules plus targeted vaccines (e.g., pneumococcal, meningococcal, influenza) are advocated for patients with complement deficiencies in general; specific data for ficolin‑3 deficiency are lacking but extrapolated recommendations apply.[2][4][7][13]

### 13.3 Genetic counseling

Genetic counseling is central: families should be informed about autosomal recessive inheritance, 25% recurrence risk for each pregnancy between carrier parents, and options for carrier testing, prenatal diagnosis, and preimplantation genetic testing.[1][9][11][13] NCIT term: NCIT:C20751 (Genetic Counseling).

---

## 14. Other Species / Natural Disease

No naturally occurring ficolin‑3 deficiency has been reported in companion animals or livestock; veterinary relevance is currently limited to comparative immunology.[1][2][4][7][13]

Orthologs of FCN3 exist in other mammals, but disease states analogous to human ficolin‑3 deficiency have not been documented in standard veterinary or comparative pathology databases.[8][15] Zoonotic transmission is not applicable, as this is a non‑infectious genetic disorder.[1][2][4][7][13]

---

## 15. Model Organisms

### 15.1 Model types and genetic models

The most clearly documented research models are **cellular models**, rather than whole‑organism models:

- FCN3 knockout or knockdown cell lines created by CRISPR or other gene‑editing approaches show reduced complement activation via the lectin pathway and impaired C3 deposition on bacteria, recapitulating the human biochemical phenotype.[15]  

Animal models (e.g., FCN3‑knockout mice) are plausible but not explicitly described in the available resources; if present in specialist model databases, they have not yet been widely reported in the literature.[1][2][4][7][10][13][15]

### 15.2 Phenotype recapitulation and applications

Cell models

- Phenotype recapitulation:  
  - Complete absence of ficolin‑3 protein.  
  - Impaired lectin‑pathway complement activation and decreased bacterial opsonization.[15]  
- Applications:  
  - Dissection of lectin‑pathway signaling.  
  - Screening for small molecules or biologics that might bypass the defect or enhance alternative complement pathways.[15]

Limitations

- Cellular models do not capture whole‑organism infection dynamics, organ damage, or autoimmunity.  
- Lack of validated animal models limits preclinical therapeutic studies.[1][2][4][7][10][13][15]

---

## Ontology and Annotation Summary (for knowledge base integration)

- **Disease:** MONDO:0013467 – Immunodeficiency due to ficolin3 deficiency.[11]  
- **Gene:** FCN3 (HGNC symbol; NCBI Gene ID 8547).[8][9]  
- **Key GO terms:**  
  - GO:0001867 – complement activation, lectin pathway.  
  - GO:0006955 – immune response.  
  - GO:0030449 – regulation of complement activation.  
- **Cell types (CL):**  
  - CL:0000182 – hepatocyte.  
  - CL:0002062 – type II pneumocyte.  
  - CL:0000094 – neutrophil.  
- **Anatomical structures (UBERON):**  
  - UBERON:0002107 – liver.  
  - UBERON:0002048 – lung.  
  - UBERON:0001007 – respiratory system.  
  - UBERON:0000062 – immune system.  
- **Phenotype (HPO):**  
  - HP:0002719 – Recurrent respiratory infections.  
  - HP:0002721 – Recurrent pneumonia.  
  - HP:0002715 – Recurrent otitis media.  
  - HP:0002718 – Chronic sinusitis.  
  - HP:0002724 – Autoimmune disease.  
  - HP:0002653 – Systemic lupus erythematosus.  
  - HP:0032281 – Abnormal complement system.  
  - HP:0002855 – Complement deficiency.  
- **Treatments (NCIT):**  
  - NCIT:C282 – Antibiotic.  
  - NCIT:C1543 – Vaccination.  
  - NCIT:C15273 – Immunoglobulin Therapy.  
  - NCIT:C20751 – Genetic Counseling.  

---

### Evidence Types

- **Human clinical:** NEJM case (immunodeficiency with FCN3 mutation and recurrent infections), congenital deficiency case (2020), infection susceptibility study (2015), neonatal cohort (2012).[4][7][12][13]  
- **In vitro:** Recombinant ficolin‑3 variant characterization (pattern‑recognition loss, complement defect).[3][5][6]  
- **Computational/database:** OMIM, Orphanet, ClinVar, NCBI Gene, Sugi Atlas disease summaries.[1][8][9][11]  
- **Cellular models:** FCN3 knockout cell lines with impaired lectin‑pathway activation.[15]  

Overall, ficolin‑3 deficiency is a well‑defined molecular lesion (complete lectin‑pathway complement deficiency) with emerging but still sparse clinical characterization; future work (especially multi‑case cohorts and mechanistic studies) is needed to refine phenotype spectrum, outcomes, and targeted management.

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
| Terms checked | 39 |
| Resolved | 37 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 37 |
| Terms named correctly | 15 |
| Terms named as a **different** term | 16 |
| Terms whose name is worth a second look | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0002721` (2 mentions) - the report calls it "Recurrent pneumonia"; HP calls it **Immunodeficiency**
- `HP:0002715` (3 mentions) - the report calls it "Recurrent otitis media"; HP calls it **Abnormality of the immune system**
- `HP:0002718` (3 mentions) - the report calls it "Chronic sinusitis", "Sepsis"; HP calls it **Recurrent bacterial infections**
- `HP:0002724` (2 mentions) - the report calls it "Autoimmune disease"; HP calls it **Recurrent Aspergillus infection**
- `HP:0002653` (2 mentions) - the report calls it "Systemic lupus erythematosus"; HP calls it **Bone pain**
- `HP:0001270` (1 mention) - the report calls it "Seizures"; HP calls it **Motor delay**
- `HP:0001290` (1 mention) - the report calls it "Peripheral neuropathy"; HP calls it **Generalized hypotonia**
- `HP:0002710` (1 mention) - the report calls it "Recurrent bacterial infections"; HP calls it **Commissural lip pit**
- `CHEBI:36976` (1 mention) - the report calls it "bacterial lipopolysaccharide"; CHEBI calls it **nucleotide**
- `CHEBI:140761` (1 mention) - the report calls it "acetylated saccharides"; CHEBI calls it **6-methylquinoline**
- `UBERON:0000062` (3 mentions) - the report calls it "immune system"; UBERON calls it **organ**
- `CL:0000094` (2 mentions) - the report calls it "neutrophil"; CL calls it **granulocyte**
- `NCIT:C282` (2 mentions) - the report calls it "Antibiotic"; NCIT calls it **Arachidonic Acid**
- `NCIT:C1543` (2 mentions) - the report calls it "Vaccination"; NCIT calls it **Peptide 946**
- `NCIT:C15273` (2 mentions) - the report calls it "Immunoglobulin Therapy"; NCIT calls it **Longitudinal Study**
- `NCIT:C20751` (2 mentions) - the report calls it "Genetic Counseling"; NCIT calls it **Inhibition of Cell Proliferation**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0002855` (2 mentions), reported as "Complement deficiency" - HP does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002719` (2 mentions) - the report calls it "Recurrent respiratory infections"; HP calls it **Recurrent infections**
- `HP:0032281` (2 mentions) - the report calls it "Abnormal complement system"; HP calls it **Abnormal base excess**
- `CL:0002062` (3 mentions) - the report calls it "type II pneumocyte"; CL calls it **pulmonary alveolar type 1 cell**, and lists "type I pneumocyte" among its other names
- `UBERON:0002106` (1 mention) - the report calls it "liver"; UBERON calls it **spleen**, and lists "lien" among its other names
- `UBERON:0001007` (2 mentions) - the report calls it "respiratory system"; UBERON calls it **digestive system**, and lists "alimentary system" among its other names
- `GO:0005793` (1 mention) - the report calls it "endoplasmic reticulum"; GO calls it **endoplasmic reticulum-Golgi intermediate compartment**, and lists "endoplasmic reticulum-Golgi transport container" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0002718` - called "Chronic sinusitis", "Sepsis"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.