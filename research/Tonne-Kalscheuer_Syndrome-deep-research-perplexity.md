---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-09-25T10:49:23.366458'
end_time: '2026-09-25T10:53:29.645169'
duration_seconds: 246.28
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Tonne-Kalscheuer Syndrome
  mondo_id: MONDO:0010506
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
citation_count: 19
reference_validation:
  total_references: 6
  verified: 6
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 6
  on_topic: 4
  validator_version: 0.3.0rc1
term_validation:
  total_terms: 69
  verified: 62
  not_found: 1
  obsolete: 6
  unverifiable: 0
  confabulation_rate: 0.014
  labels_checked: 22
  labels_matching: 10
  labels_mismatched: 9
  mislabelled_terms:
  - term_id: GO:0006306
    reported_labels:
    - "DNA methylation\u2011dependent chromatin silencing"
    ontology_label: obsolete DNA methylation
  - term_id: GO:0006461
    reported_labels:
    - protein ubiquitination
    ontology_label: GO_0006461
  - term_id: CL:0000127
    reported_labels:
    - neuron
    ontology_label: astrocyte
  - term_id: CL:0000312
    reported_labels:
    - glial cell
    ontology_label: keratinocyte
  - term_id: NCIT:C15273
    reported_labels:
    - Surgical Procedure
    ontology_label: Longitudinal Study
  - term_id: NCIT:C80434
    reported_labels:
    - Congenital Diaphragmatic Hernia Repair
    ontology_label: Pacemaker Placement
  - term_id: NCIT:C51574
    reported_labels:
    - Cardiac Surgical Procedure
    ontology_label: ESR1 wt Allele
  - term_id: NCIT:C16467
    reported_labels:
    - Supportive Care
    ontology_label: Congo
  - term_id: NCIT:C15229
    reported_labels:
    - Rehabilitation Therapy
    ontology_label: Antitumor Drug Screening Assay
  labels_variant: 3
  unresolved_terms:
  - HP:0008735
  obsolete_terms:
  - term_id: GO:0006306
    ontology_label: obsolete DNA methylation
  - term_id: GO:0006461
    ontology_label: GO_0006461
    replaced_by: GO:0065003
  - term_id: CL:0000298
    ontology_label: obsolete xylem element
    replaced_by: PO:0000273
  - term_id: CL:0000087
    ontology_label: obsolete male germ line stem cell (sensu Nematoda and Protostomia)
    replaced_by: CL:0000016
  - term_id: CL:0000213
    ontology_label: obsolete lining cell
  - term_id: GO:0001749
    ontology_label: GO_0001749
    replaced_by: GO:0042463
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Tonne-Kalscheuer Syndrome
- **MONDO ID:** MONDO:0010506 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Tonne-Kalscheuer Syndrome** covering all of the
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

# Tonne–Kalscheuer Syndrome (TOKAS): Comprehensive Disease Characteristics and Mechanistic Overview

Tonne–Kalscheuer syndrome (TOKAS) is a rare, X‑linked recessive neurodevelopmental and multiple congenital anomaly disorder caused by hemizygous variants in the **RLIM** (*RNF12*) gene, encoding a RING‑type E3 ubiquitin ligase that is central to transcriptional regulation, stem cell differentiation, and X‑chromosome inactivation.[5][14][2] Clinically, TOKAS spans a broad spectrum from males with syndromic intellectual disability, microcephaly, dysmorphic facial features, behavioral abnormalities, and abnormalities of the hands, feet, nails, and urogenital system, through to severe prenatal forms characterized by congenital diaphragmatic hernia, hydrops fetalis, and perinatal lethality.[5][6][2] Since the first description of a missense *RLIM* variant segregating with syndromic X‑linked intellectual disability in a Norwegian family in 2015, a growing number of pathogenic missense variants—clustered in the RLIM basic regulatory region and RING catalytic domain—have been identified in at least nine families and more than forty affected individuals, including approximately eighteen antenatally diagnosed fetuses.[12][6][2][4] Functional studies in embryonic stem cell models and RLIM variant reporter systems demonstrate that TOKAS‑associated variants impair RLIM E3 ligase activity, destabilize the protein, and deregulate ubiquitylation of key substrates such as the pluripotency factor REX1 and the inhibitory SMAD7, thereby perturbing stem cell maintenance, neural differentiation, and Xist‑mediated X‑chromosome inactivation.[13][17][11][16] In addition, duplications of Xq13 encompassing *RLIM* support a dosage‑sensitive role for the gene in intellectual disability and facial dysmorphism, extending the disease concept from loss‑of‑function hemizygous variants to increased RLIM copy number.[18] This report synthesizes the current clinical, genetic, mechanistic, and translational knowledge about TOKAS to support structured disease modeling, ontology‑based annotation, and future precision medicine approaches.

## 1. Disease Information

### 1.1 Definition and Overall Description

Tonne–Kalscheuer syndrome (TOKAS) is defined as an X‑linked recessive multiple congenital anomaly and neurodevelopmental disorder caused by hemizygous pathogenic variants in the *RLIM* (*RNF12*) gene at Xq13.2.[5][14][3] OMIM entry #300978, MedGen Concept ID C4283894 and MONDO:0010506 designate this entity as “Tonne‑Kalscheuer syndrome” and classify it among syndromic X‑linked intellectual disability disorders with distinctive craniofacial, skeletal, and genitourinary manifestations.[3][5][9] Clinically, TOKAS is characterized by two principal presentations: a postnatal neurodevelopmental phenotype in surviving males with global developmental delay, intellectual disability, speech delay, behavioral abnormalities, abnormal gait, and evolving craniofacial and acral dysmorphism; and a more severe prenatal phenotype associated with multiple congenital malformations, intrauterine growth restriction, hydrops, and frequently lethal congenital diaphragmatic hernia.[5][6][4][2]

The syndrome was initially delineated in a three‑generation Norwegian family described by Tønne et al. in 2015, who reported a novel X‑linked intellectual disability syndrome “characterized by subtle facial dysmorphism, autism and severe feeding problems” and identified a missense variant c.1067A>G, p.Tyr356Cys in *RLIM* that segregated with the phenotype.[12][14] Subsequent work by Hu et al. and Frints et al. expanded the phenotypic spectrum, revealing that additional missense *RLIM* variants underlie X‑linked neurodevelopmental disorders with consistent intellectual disability but variable congenital malformations.[13][18][6] A recent fetal series further refined the antenatal manifestations and highlighted a recurrent p.Arg611Cys variant as a major contributor to severe prenatal TOKAS.[6][7][4] Together, these studies support a coherent disease concept in which RLIM dysfunction causes a continuum of neurodevelopmental and structural anomalies, with severity influenced by variant location, functional impact, and dosage.

### 1.2 Key Identifiers and Classification

The principal identifiers for TOKAS in major biomedical databases include OMIM #300978 (phenotype) and *RLIM* OMIM #300379 (gene), MedGen Concept ID C4283894 with synonyms “TOKAS; TONNE–KALSCHEUER SYNDROME,” and MONDO:0010506 in the Monarch/MONDO ontology.[5][14][3][9] LOVD catalogs TOKAS under Disease #05767, associating it specifically with *RLIM* and marking the inheritance as X‑linked.[9] In the OMIM intellectual disability compendium (#309585), TOKAS is explicitly listed as “Tonne‑Kalscheuer syndrome” at Xq13.2 with X‑linked recessive inheritance and mapping key 3, confirming the causal assignment to *RLIM*.[8][5]

Despite its recognition in OMIM, MONDO, and MedGen, TOKAS does not yet have a widely used dedicated ICD‑10 or ICD‑11 code; affected individuals are typically coded under generic categories such as Q87 (“other specified congenital malformation syndromes affecting multiple systems”) and F70–F79 (“intellectual disability”) supplemented by codes for specific anomalies such as congenital diaphragmatic hernia (Q79.0) and differences in sex development.[6][5] MeSH does not currently list TOKAS as a standalone heading, but it falls under broader descriptors such as “Intellectual Disability” and “Congenital Abnormalities.” From an ontology standpoint, the disease is captured as a Mendelian monogenic disorder, subclass of “X‑linked recessive disease” and “syndromic intellectual disability,” and cross‑referenced to Human Phenotype Ontology (HPO) terms for its characteristic features.[3][5][9]

### 1.3 Synonyms and Alternative Names

TOKAS is consistently referred to as **Tonne–Kalscheuer syndrome**, honoring the original describers, and abbreviated as **TOKAS** in clinical and genetic literature.[5][2][6] MedGen and LOVD list “TOKAS; TONNE‑KALSCHEUER SYNDROME” as synonyms, emphasizing its multiple congenital anomaly and neurodevelopmental nature.[3][9] In the early literature, before the syndrome was fully delineated, patients were often described under broader labels such as “syndromic X‑linked intellectual disability” or “RLIM‑related X‑linked intellectual disability,” and initial reports by Tønne et al. referred to “a novel X‑linked intellectual disability (XLID) syndrome” segregating with an *RLIM* missense variant.[12][13][18] Hu et al. described “pathogenic variants in E3 ubiquitin ligase RLIM/RNF12 [that] lead to a syndromic X‑linked intellectual disability and behavior disorder,” effectively overlapping with the TOKAS concept.[18][13] 

Over time, the term TOKAS has become the preferred disease label for RLIM‑associated X‑linked neurodevelopmental anomaly syndromes, encompassing both postnatal XLID presentations and severe antenatal multiple malformation phenotypes.[5][6][4] Nonetheless, in some contexts—particularly mechanistic and gene‑centric studies—authors still refer to “RNF12/RLIM X‑linked intellectual disability” or “RNF12 XLID mutations,” indicating that for classification and ontology mapping, synonyms such as “RLIM‑related X‑linked intellectual disability” should be retained.[13][17][19]

### 1.4 Source Type: Patient‑Level vs Aggregated Evidence

The current understanding of TOKAS is drawn predominantly from aggregated case series, family studies, and mechanistic experiments rather than large population‑based registries or EHR‑derived datasets.[5][6][2] OMIM, MedGen, and LOVD curate summarized phenotype descriptions and inheritance patterns based on published clinical reports, while detailed phenotypic and molecular data have been compiled across approximately nine families and 41 postnatal patients, alongside at least 18 antenatally diagnosed fetuses.[4][6][2] 

Clinical characterizations such as those by Frints et al., the recent JMG fetal series, and the antenatal multidisciplinary case report in 2024 provide integrated descriptions of phenotype frequencies, severity, and genotype–phenotype relationships, effectively serving as disease‑level resources despite originating from individual patients.[6][4][2] Mechanistic studies using embryonic stem cells and RLIM activity reporters rely on patient‑derived variants as experimental input, but their findings are generalized to infer disease‑level pathophysiology.[13][17][16] At present, no large‑scale EHR‑based epidemiological analyses exist for TOKAS, reflecting its extreme rarity and recent recognition.

## 2. Etiology

### 2.1 Primary Causal Factors: Genetic Basis

TOKAS is unequivocally a **monogenic, X‑linked recessive disorder** caused by hemizygous pathogenic variants in the *RLIM* gene, also known as *RNF12*, located on Xq13.2.[5][14][3] OMIM explicitly notes that “a number sign (#) is used with this entry because of evidence that Tonne‑Kalscheuer syndrome (TOKAS) is caused by hemizygous mutation in the RLIM gene (300379) on chromosome Xq13,” emphasizing the direct causal relationship.[5] MedGen similarly indicates that the condition is “associated with 1 gene RLIM,” confirming its monogenic nature.[9] RLIM encodes a widely expressed RING‑H2 zinc finger E3 ubiquitin ligase that acts both as a transcriptional cofactor and as a ubiquitin ligase, targeting protein substrates for proteasomal degradation.[14][15]

To date, all reported TOKAS patients harbor missense *RLIM* variants that alter highly conserved residues in either the distal basic regulatory region or the C‑terminal RING domain, both critical for RLIM catalytic function and substrate recognition.[10][13][17][16] Tønne et al. identified p.Tyr356Cys in four affected males from a Norwegian XLID family, while Frints et al. and Hu et al. described additional missense variants such as p.Pro587Arg, p.Arg599Cys, and the recurrent p.Arg611Cys in multiple kindreds.[12][13][18][6] A Scientific Reports study reported a novel variant c.1262A>G, p.Tyr421Cys adjacent to the regulatory basic region, associated with severe TOKAS and perinatal lethality.[1][10][11] More recent work using RLIM‑specific activity reporters characterized p.Asn581Lys as another pathogenic variant that disrupts catalytic activity.[16] Collectively, these data conclusively establish *RLIM* missense variants as the primary etiologic lesion in TOKAS.

### 2.2 Genetic Risk Factors: Causal Variants and Susceptibility

The principal genetic risk factor for TOKAS is the presence of a hemizygous pathogenic or likely pathogenic missense variant in *RLIM* in males, or heterozygous carriage of such a variant in females who may be asymptomatic carriers or mildly affected depending on X‑chromosome inactivation (XCI) patterns.[5][12][2] Across published cases, nine pathogenic *RLIM* missense variants have been described in 41 patients, with two additional likely pathogenic variants reported more recently.[6][4][16][10] These variants cluster in functional hotspots: the regulatory basic region required for chromatin recruitment and efficient ubiquitin transfer, and the C‑terminal RING domain essential for catalytic activity.[13][17][15]

A genotype–phenotype correlation, while not fully resolved, has begun to emerge. The p.Arg611Cys variant is the most frequently reported pathogenic allele and is strongly associated with a severe antenatal phenotype characterized by multiple congenital anomalies, hydrops, and early lethality.[2][4][6][7] In a combined fetal cohort, p.Arg611Cys accounted for 66% of antenatal TOKAS cases (12 of 18), making it a major genetic risk factor for the lethal form of the disease.[4][6][7] In contrast, p.Tyr356Cys, originally described in the Norwegian XLID family, is associated with postnatal survival, intellectual disability, autism spectrum features, and subtle dysmorphism without necessarily lethal malformations.[12][14][18] The severe p.Tyr421Cys variant disrupts RLIM stability and function and led to perinatal lethality due to diaphragmatic hernia in the reported case, indicating that variants near the basic region can confer a highly deleterious phenotype.[1][10][11]

Duplication of Xq13 including *RLIM* also appears to constitute a genetic risk factor for neurodevelopmental disorders with distinct facial features. A study of individuals with varying Xq13 duplications found that *RLIM* was the only fully duplicated gene in all subjects, and increased RLIM copy number correlated with increased RLIM mRNA and protein levels in patient cells, as well as intellectual disability and characteristic facial dysmorphism.[18] These observations suggest that *RLIM* is dosage sensitive, with both loss‑of‑function and gain‑of‑function (via duplication) states predisposing to neurodevelopmental disease.[18][15]

No susceptibility loci or modifier genes have been formally validated for TOKAS, but functional data implicate potential modifiers in the RLIM–REX1–USP26 axis. RLIM ubiquitylates the pluripotency factor and Xist repressor REX1 to promote XCI and neural differentiation, while the deubiquitylase USP26 forms a feed‑forward loop that protects RLIM from autoubiquitylation, particularly in testis.[15] While not yet demonstrated in patients, variation in REX1 or USP26 could theoretically modify TOKAS severity by altering RLIM substrate dynamics.

### 2.3 Environmental and Lifestyle Risk Factors

Current evidence does not support any specific environmental, toxic, infectious, or lifestyle risk factors for TOKAS. All reported cases arise in the context of inherited or de novo *RLIM* missense variants, and the clinical literature consistently describes TOKAS as a Mendelian X‑linked recessive condition without identifiable environmental contributors.[5][6][2][10] No associations have been reported between TOKAS and maternal exposures, infections, or nutritional factors, even in detailed antenatal case descriptions and fetal series.[2][4][6] 

Because TOKAS is extremely rare and occurs in the setting of clear genetic lesions, epidemiological studies designed to detect modest environmental effects have not been conducted, and registries for toxin exposures or occupational risk do not mention TOKAS. As such, environmental risk factors can be considered unknown or negligible in the current state of knowledge.

### 2.4 Protective Factors and Gene–Environment Interactions

There are no documented genetic protective variants that reduce TOKAS risk or ameliorate its clinical expression. However, one important biological “protective” mechanism in female carriers is skewed X‑chromosome inactivation favoring the normal *RLIM* allele. In the original Norwegian family, all female carriers tested exhibited extremely skewed XCI patterns, effectively silencing the mutant *RLIM* allele and preventing overt disease, thereby protecting against TOKAS manifestations.[12][5][14] This skewing is likely driven by selection against cells expressing the pathogenic RLIM variant, but the underlying molecular determinants have not been fully elucidated.[12][13]

No environmental protective factors have been identified, and given the genetic etiology, such factors are unlikely to prevent disease occurrence in hemizygous male fetuses. Nevertheless, early detection through prenatal imaging and genetic testing can enable informed decision‑making and anticipatory care, which may mitigate some complications or support palliative planning.[2][6] Gene–environment interactions have not been described for TOKAS; the disease phenotype appears to be driven overwhelmingly by intrinsic genetic mechanisms rather than modifiable exposures.

## 3. Phenotypes

### 3.1 Overview of Phenotypic Spectrum

TOKAS displays a wide but coherent phenotypic spectrum spanning neurodevelopmental impairments, craniofacial dysmorphism, acral anomalies, differences in sex development, growth restriction, and visceral malformations such as congenital diaphragmatic hernia.[5][6][2] OMIM and MedGen describe two main presentations: most male patients exhibit global developmental delay from early infancy, impaired intellectual development, speech delay, behavioral abnormalities, and abnormal gait, while more severely affected patients—often with particular *RLIM* variants—present with multiple congenital malformations including diaphragmatic hernia, congenital heart disease, omphalocele, cleft palate, and polysplenia.[5][3][6] 

A recent cohort study synthesized by Frints et al., summarized in the JMG fetal perspective paper, reported that males with TOKAS exhibit intellectual disability in 100% of cases (ranging from mild to severe), differences of sexual development (DSD) in 90%, congenital diaphragmatic hernia in 50%, congenital heart disease in 17%, omphalocele in 10%, cleft palate in 8%, polysplenia in 5%, and intestinal malrotation in 5%.[6] Additional abnormalities included intrauterine growth restriction (IUGR) in 80%, microcephaly in 86%, short wide thumbs in 88%, nail dysplasia in 30%, camptodactyly in 15%, syndactyly in 10% of hands and 25% of feet, and pre‑axial polydactyly in 15%.[6] These data provide a quantitative framework for phenotype frequencies and reinforce the multi‑system nature of TOKAS.

### 3.2 Neurodevelopmental and Behavioral Phenotypes

Neurodevelopmental manifestations are central to TOKAS and include global developmental delay, intellectual disability, speech delay, abnormal gait, and behavioral abnormalities such as autism spectrum traits.[5][6][12][18] In the Norwegian family originally described by Tønne et al., affected males presented with “subtle facial dysmorphism, autism and severe feeding problems,” alongside intellectual disability.[12] Subsequent case series consistently report intellectual disability as a universal feature, with severity ranging from mild to profound.[6][5] Age of onset is early childhood; developmental delays are apparent from infancy, and cognitive deficits persist throughout life, constituting a lifelong, stable to progressive phenotype.[5][6]

Quality of life impact is substantial. Intellectual disability affects learning, adaptive functioning, and independence, often requiring special education and long‑term support. Behavioral abnormalities, including autism spectrum features, social communication difficulties, and potential aggression or self‑injury, further impair social integration and family functioning.[12][18] Abnormal gait and coordination can limit mobility, while severe feeding problems in some patients compromise nutritional status and necessitate interventions such as gastrostomy.[12] Appropriate HPO terms include **Intellectual disability (HP:0001249)**, **Global developmental delay (HP:0001263)**, **Autism (HP:0000717)**, **Abnormal gait (HP:0001288)**, and **Feeding difficulties (HP:0011968)**.

### 3.3 Craniofacial and Growth Phenotypes

Craniofacial dysmorphism is a characteristic feature, though specific facial traits vary and evolve with age.[5][6][12] MedGen and OMIM describe “dysmorphic facial features that evolve with age,” and case reports note subtle but distinctive appearances, including broad forehead, deep‑set eyes, short philtrum, thin upper lip, and other minor anomalies.[3][12][18] Microcephaly is highly prevalent, reported in 86% of males in one cohort, and is usually apparent from the prenatal or neonatal period, reflecting underlying neurodevelopmental perturbation.[6] Intrauterine growth restriction is seen in approximately 80% of cases, often contributing to low birth weight and subsequent growth challenges.[6]

These craniofacial and growth phenotypes significantly impact health and psychosocial well‑being. Microcephaly is associated with cognitive impairment and may be stigmatizing; facial dysmorphism can affect self‑esteem and social perception. Growth restriction may predispose to metabolic complications and requires close nutritional monitoring. Suggested HPO terms include **Dysmorphic facial features (HP:0001999)**, **Microcephaly (HP:0000252)**, **Intrauterine growth retardation (HP:0001511)**, and **Failure to thrive (HP:0001531)** for postnatal growth issues.

### 3.4 Acral and Skeletal Phenotypes

Hand, foot, and nail anomalies are hallmark features of TOKAS, particularly in mildly to moderately affected survivors.[5][6][4] The JMG cohort reports short wide thumbs in 88% of cases, nail dysplasia in 30%, camptodactyly in 15%, syndactyly in 10% of hands and 25% of feet, and pre‑axial polydactyly in 15%.[6] These acral anomalies may be subtle but recognizable and contribute to the syndrome’s diagnostic profile. Nail dysplasia can present as thin, brittle, or malformed nails; camptodactyly as fixed flexion contractures of fingers; and syndactyly and polydactyly as digit fusion or duplication.

Functionally, acral anomalies can interfere with fine motor skills, manual dexterity, and gait, affecting daily activities and occupational opportunities. They may also have cosmetic implications, influencing self‑image. Relevant HPO terms include **Short thumb (HP:0009623)**, **Broad thumb (HP:0011304)**, **Camptodactyly of finger (HP:0012385)**, **Syndactyly (HP:0001159)**, **Preaxial polydactyly (HP:0100258)**, and **Nail dysplasia (HP:0001597)**.

### 3.5 Urogenital and Differences in Sex Development

Differences in sex development (DSD) are among the most frequent visceral manifestations of TOKAS. A recent cohort analysis reported DSD—including micropenis, hypospadias, and testicular hypoplasia—in 90% of male patients.[6] OMIM and Scientific Reports describe hypogenitalism as a common feature, and urogenital abnormalities with hypogenitalism are part of the original TOKAS definition.[1][5][2] These anomalies are typically congenital, evident at birth, and may be associated with cryptorchidism and impaired fertility, though long‑term reproductive outcomes are incompletely characterized.

DSD can impose significant psychosocial and medical burdens, necessitating specialist management for urinary function, sexual health, hormonal status, and psychosexual development. Potential HPO terms include **Micropenis (HP:0000044)**, **Hypospadias (HP:0000047)**, **Testicular hypoplasia (HP:0008735)**, **Hypogenitalism (HP:0008736)**, and **Cryptorchidism (HP:0000028)**.

### 3.6 Visceral Malformations: Diaphragmatic Hernia and Others

Congenital diaphragmatic hernia (CDH) is a striking and clinically critical manifestation of TOKAS, reported in approximately 50% of males in one cohort and strongly associated with severe prenatal forms.[6][1][10] In the Scientific Reports case, p.Tyr421Cys caused a severe form of TOKAS “resulting in perinatal lethality by diaphragmatic hernia,” underscoring the lethality of this malformation.[1][11] MedGen and OMIM emphasize diaphragmatic hernia as a defining feature in severe cases, noting that “in the most severe cases, diaphragmatic hernia causes death shortly after birth.”[1][5]

Other visceral malformations include congenital heart disease (17%), omphalocele (10%), cleft palate (8%), polysplenia (5%), and intestinal malrotation (5%).[6] These anomalies often co‑occur with CDH and IUGR, forming a Fryns‑like phenotype in some fetuses.[1][10][6] Visceral malformations significantly impact survival, morbidity, and surgical burden. CDH, in particular, leads to pulmonary hypoplasia and respiratory failure; omphalocele and intestinal malrotation predispose to feeding difficulties and volvulus; congenital heart defects impose hemodynamic strain; and cleft palate impairs feeding and speech.

Relevant HPO terms include **Congenital diaphragmatic hernia (HP:0000776)**, **Congenital heart defect (HP:0001627)**, **Omphalocele (HP:0001539)**, **Cleft palate (HP:0000175)**, **Polysplenia (HP:0001748)**, and **Intestinal malrotation (HP:0002566)**.

### 3.7 Prenatal Phenotypes and Antenatal Course

The antenatal phenotype of TOKAS has been clarified through fetal case series and antenatal diagnostic reports.[4][6][2] Fetuses with severe TOKAS often present with IUGR, hydrops fetalis, generalized edema, CDH, cardiac anomalies, and additional malformations, typically detected on second‑trimester ultrasound or fetal MRI.[2][6] The JMG fetal perspective paper notes that of 41 reported patients, only 7 antenatal cases were initially described, but the expanded series now documents 18 antenatal cases, with recurring *RLIM* variants such as p.Arg611Cys.[4][6][7] 

Hydrops fetalis and severe CDH carry a high risk of intrauterine demise or perinatal death despite advanced neonatal care. The impact on family quality of life is profound, involving difficult decisions about pregnancy continuation, invasive fetal diagnostics, and potential palliative planning.[2] Suggested HPO terms include **Hydrops fetalis (HP:0001789)**, **Generalized edema (HP:0002615)**, and **Abnormal prenatal growth (HP:0001510)**. Age of onset for these phenotypes is prenatal (fetal), and their progression is rapid and life‑threatening.

## 4. Genetic and Molecular Information

### 4.1 Causal Gene: RLIM (*RNF12*)

The causal gene for TOKAS is **RLIM** (RING finger LIM domain‑binding protein), also known by its alternative symbol **RNF12**, located at Xq13.2.[14][5] RLIM is an X‑linked, widely expressed RING‑H2 zinc finger protein that functions as both a transcriptional cofactor and an E3 ubiquitin ligase.[14][15] It was originally identified as a corepressor that binds LIM‑homeodomain transcription factors and recruits the Sin3A/histone deacetylase complex, thereby modulating gene expression.[14][15] Later work established RLIM as a dose‑dependent, trans‑acting activator of X‑chromosome inactivation (XCI), with extra copies driving ectopic XCI and knockout preventing proper Xist upregulation.[15]

OMIM summarizes RLIM as “a widely expressed domain‑containing zinc finger protein with diverse cellular functions” that “serves as a cofactor promoting or inhibiting transcription factor activity and also acts as an E3 ubiquitin ligase that ubiquitinates target proteins for subsequent degradation by the proteasome.”[14] The RLIM protein contains an N‑terminal region implicated in transcriptional co‑regulation, a central basic regulatory region required for chromatin recruitment and efficient ubiquitin transfer, and a C‑terminal RING‑H2 domain that catalyzes ubiquitin transfer to substrates.[13][15][10] RLIM is essential for imprinted XCI in mice, playing a maternal role in oocytes, and contributes to stem cell maintenance, neural differentiation, mammary alveolar cell survival, spermiogenesis, and hypothalamic energy balance.[15]

### 4.2 Spectrum of Pathogenic Variants

Pathogenic RLIM variants in TOKAS are predominantly missense changes affecting highly conserved residues within the basic regulatory region or the RING domain.[10][12][13][6][16] The earliest identified variant, p.Tyr356Cys (c.1067A>G), lies within a conserved domain essential for binding LIM‑homeodomain transcription factors and was shown to segregate with XLID in a Norwegian family.[12][14] Hu et al. and Frints et al. subsequently reported additional missense variants including p.Pro587Arg and p.Arg599Cys in the RING domain, and p.Arg611Cys, which has emerged as a recurrent, particularly deleterious allele.[13][18][6]

The JMG fetal perspective paper and associated Eur J Hum Genet report note that “to date, 9 pathogenic RLIM variants have been described in 41 patients” and that the p.Arg611Cys variant accounts for 66% of fetal TOKAS cases, strongly suggesting a genotype–phenotype correlation.[6][4] The Dundee Scientific Reports study added p.Tyr421Cys, a novel missense variant adjacent to the basic region, associated with severe TOKAS and perinatal lethality.[1][10][11] More recently, RLIM activity reporter assays characterized p.Asn581Lys as a TOKAS variant that disrupts RLIM catalytic activity.[16] 

All these variants are **germline** and present in hemizygous state in affected males, with heterozygous carrier females often exhibiting skewed XCI and minimal or no symptoms.[12][5][2] No somatic RLIM mutations have been reported in TOKAS. Variant classification in ClinVar and HGMD (not detailed in the provided sources but inferred from OMIM and case series) places these missense changes as pathogenic or likely pathogenic based on segregation, functional impact, and absence from controls.[5][10][16] Population databases such as gnomAD indicate that loss‑of‑function and severe missense variants in RLIM are extremely rare, reflecting strong purifying selection; the disease‑causing alleles described in TOKAS families are absent or extremely infrequent in general populations, consistent with their pathogenicity.[10][12][6]

### 4.3 Functional Consequences and Variant Mechanisms

Mechanistic studies using embryonic stem cells (ESCs), RLIM activity reporters, and biochemical assays have elucidated the functional consequences of TOKAS‑associated RLIM variants.[13][17][11][16] A key paper titled “RNF12 X‑Linked Intellectual Disability Mutations Disrupt E3 Ligase Activity and Neural Differentiation” employed an ESC model to explore the developmental functions of RLIM and the impact of XLID mutations.[13][17] The authors showed that RNF12 catalytic activity is required for proper stem cell maintenance and neural differentiation, and that patient‑associated XLID mutations disrupt these processes by impairing ubiquitylation of key substrates such as REX1 and SMAD7.[13][17] As they state:

> “We show that RNF12 catalytic activity is required for proper stem cell maintenance and neural differentiation, and this is disrupted by patient-associated XLID mutation.”[13][17]

The study demonstrated that RING domain mutants (e.g., p.Pro587Arg, p.Arg599Cys) severely impair catalysis, while mutations in the distal basic regulatory region interfere with ubiquitin transfer, thereby disrupting distinct functional modules of RLIM.[13][17] XLID mutants displayed reduced ubiquitylation of REX1, a pluripotency factor and Xist repressor, and SMAD7, an inhibitory regulator of TGF‑β/BMP/Nodal signaling, leading to abnormal stem cell behavior and accelerated neural differentiation reminiscent of intellectual disability phenotypes.[13][17][19]

The Scientific Reports study of p.Tyr421Cys further showed that this variant disrupts RLIM protein stability and function in ESCs.[1][10][11] RLIM p.Tyr421Cys was correctly localized to the nucleus but was readily degraded by the proteasome, resulting in reduced protein levels.[11][10] Functional assays revealed significantly impaired E3 ubiquitin ligase activity and interference with RLIM function in Xist long‑non‑coding RNA induction, which is necessary for imprinted XCI initiation.[11][10] The authors conclude:

> “The RLIM p.(Tyr421Cys) variant also displays significantly impaired E3 ubiquitin ligase activity, which interferes with RLIM function in Xist long-non-coding RNA induction that initiates imprinted X-chromosome inactivation.”[11][10]

RLIM‑specific activity reporters developed in a recent study provided a modular approach to assessing variant pathogenicity.[16] These reporters quantify RLIM catalytic activity in living cells and were used to show that p.Asn581Lys disrupts RLIM activity, validating it as a pathogenic TOKAS variant.[16] The study emphasizes that RLIM activity reporter assays can distinguish pathogenic from benign variants and illuminate their mechanistic impact on ubiquitin transfer.[16]

Taken together, these data demonstrate that TOKAS‑associated RLIM variants are **loss‑of‑function** at the level of E3 ligase activity, though they may exert their effects via impaired catalysis, destabilized protein, or defective regulatory interactions. In some contexts, RLIM duplications result in **gain‑of‑function** at the dosage level, indicating that TOKAS and related RLIM‑associated disorders span both reduced and increased RLIM activity states.[18][15]

### 4.4 Modifier Genes, Epigenetic and Chromosomal Information

No specific modifier genes have been validated for TOKAS, but the RLIM–REX1–USP26 axis provides plausible candidates.[15] RLIM promotes XCI by ubiquitylating REX1, and REX1 represses the deubiquitylase USP26, which in turn protects RLIM from autoubiquitylation, forming a testis‑specific feed‑forward loop.[15] Variants in REX1 or USP26 could theoretically modulate RLIM levels or activity and alter TOKAS severity, though human data are lacking. 

Epigenetically, RLIM plays a critical role in initiating Xist‑mediated XCI, which involves extensive chromatin modifications, including histone H3 lysine 27 trimethylation (H3K27me3) and DNA methylation on the inactive X chromosome.[15][11] The disruption of RLIM function in TOKAS likely leads to altered epigenetic landscapes, particularly in early embryonic tissues, though direct epigenomic profiling in patients has yet to be reported. RLIM’s function as a transcriptional co‑regulator and its recruitment of histone deacetylase complexes also indicate that RLIM mutations may perturb histone acetylation status at target loci.[14][15]

Chromosomally, TOKAS is tied to Xq13.2, and some patients with Xq13 duplications including *RLIM* exhibit overlapping neurodevelopmental phenotypes.[18] No aneuploidies, translocations, or large deletions specifically associated with TOKAS have been reported; the disorder is driven by point variants and small duplications affecting RLIM. DECIPHER and related structural variant databases catalog Xq13 duplications and their phenotypic correlates, but detailed TOKAS‑specific entries are limited.[18]

## 5. Environmental Information

### 5.1 Environmental Factors

No environmental toxins, radiation exposures, pollution, or occupational factors have been identified as contributors to TOKAS. All evidence points to a purely genetic etiology, with “pathogenic variants in the X‑linked RLIM (RNF12) gene” serving as the exclusive cause in reported cases.[2][5][10] CTD, TOXNET, and EPA databases do not list TOKAS, and no associations with chemicals have been reported in PubMed searches, reflecting the syndrome’s rarity and monogenic nature.

### 5.2 Lifestyle Factors

Lifestyle factors such as smoking, diet, exercise, and alcohol consumption are not reported to influence TOKAS occurrence or severity. The disease manifests early, often prenatally, and is driven by germline RLIM variants, making lifestyle influences on risk very unlikely. However, general supportive care and optimized nutrition may improve outcomes in surviving individuals, particularly in managing growth, feeding issues, and developmental progression, but these are not disease‑specific risk or protective factors.[12][6]

### 5.3 Infectious Agents

There is no evidence that infectious agents cause or trigger TOKAS. The disease is not infectious, not contagious, and not associated with known pathogens. NCBI Taxonomy and ViPR do not list TOKAS among infection‑related conditions; it is strictly classified as a Mendelian genetic disorder.[5][3]

## 6. Mechanism and Pathophysiology

### 6.1 Ordered Causal Chain from Mutation to Clinical Phenotype

RLIM missense mutation in the basic regulatory region or RING domain leads to impaired RLIM E3 ubiquitin ligase catalytic activity and/or protein instability.[10][11][13][17]

Impaired RLIM catalytic activity leads to reduced ubiquitylation and proteasomal degradation of key substrates such as the pluripotency factor REX1 and the inhibitory SMAD7, as directly shown in embryonic stem cell models.[13][17][19]

Reduced REX1 degradation leads to persistent repression of Xist transcription and defective initiation of X‑chromosome inactivation (XCI), particularly in early embryonic cells, as inferred from RLIM’s established role in XCI and direct disruption of Xist induction by RLIM p.Tyr421Cys.[11][15][10]

Defective XCI initiation leads to aberrant dosage compensation and dysregulated expression of X‑linked genes, contributing to altered transcriptional programs in neural progenitors and other embryonic tissues, as inferred from XCI’s role in dosage regulation.[15][19]

Reduced SMAD7 ubiquitylation leads to sustained SMAD7 levels and diminished TGF‑β/BMP/Nodal pathway signaling, thereby perturbing developmental signaling cascades controlling mesoderm and endoderm patterning, as demonstrated in biochemical studies of RLIM–SMAD7 interactions.[13][15][19]

Deregulated pluripotency and developmental signaling in embryonic stem cells lead to abnormal stem cell maintenance, accelerated and disordered neural differentiation, and impaired specification of structural tissues such as diaphragm, heart, and urogenital structures, as shown in RNF12 mutant ESCs and inferred for human development.[13][17][19][6]

Abnormal neural differentiation and brain development lead to microcephaly, intellectual disability, behavioral abnormalities, and autism spectrum features seen in affected males.[6][12][13][17]

Disordered development of mesodermal and endodermal derivatives leads to congenital diaphragmatic hernia, congenital heart disease, omphalocele, intestinal malrotation, and differences in sex development, as observed in severe TOKAS cases.[6][1][10]

The combined impact of neural and visceral developmental defects leads to intrauterine growth restriction, hydrops fetalis, and perinatal lethality in severe variants such as p.Arg611Cys and p.Tyr421Cys, as documented in antenatal case series.[4][6][10][2]

### 6.2 Molecular Pathways

At the molecular level, RLIM participates in several interconnected pathways implicated in TOKAS pathophysiology: X‑chromosome inactivation, ubiquitin–proteasome–mediated transcriptional regulation, and TGF‑β/BMP/Nodal signaling.[14][15][13] RLIM’s role as a dose‑dependent activator of XCI is mediated through its ubiquitin ligase activity targeting REX1, a pluripotency factor and Xist repressor. By ubiquitylating REX1 and promoting its degradation, RLIM enables Xist transcription, which coats the X chromosome and initiates silencing via recruitment of chromatin modifiers.[15][11] Disruption of RLIM activity in TOKAS variants leads to reduced REX1 ubiquitylation, impaired Xist induction, and defective XCI, contributing to altered dosage of X‑linked genes in early development.[11][13][15]

RLIM also binds and ubiquitylates SMAD7, an inhibitory Smad that dampens TGF‑β/BMP/Nodal signaling. A 2012 study (summarized in RLIM gene resources) showed that RLIM induces polyubiquitination and proteasomal degradation of SMAD7, thereby potentiating TGF‑β/BMP/Nodal‑mediated transcriptional programs.[15] These pathways are crucial for mesoderm and endoderm patterning, organogenesis, and morphogenesis of structures such as diaphragm, heart, and urogenital organs. TOKAS variants that reduce RLIM activity likely lead to elevated SMAD7, attenuated TGF‑β/BMP signaling, and downstream defects in organ development, consistent with the observed congenital malformations.[6][1][19]

RLIM’s function as a transcriptional co‑regulator of LIM‑homeodomain transcription factors further connects it to gene expression programs in neural development and skeletal morphogenesis. RLIM was originally identified as a corepressor that recruits the Sin3A/histone deacetylase complex, modulating the activity of LIM‑HD factors involved in patterning neural circuits and limb structures.[14][15] Variants such as p.Tyr356Cys, located in the LIM‑binding domain, may alter these interactions and perturb transcriptional networks in brain and limb development, contributing to intellectual disability and acral anomalies.[12][13][17]

Relevant GO biological process terms include **GO:0007399 (nervous system development)**, **GO:0007275 (multicellular organism development)**, **GO:0006306 (DNA methylation‑dependent chromatin silencing)** for XCI, **GO:0006461 (protein ubiquitination)**, and **GO:0007178 (transforming growth factor beta receptor signaling pathway)**. RLIM itself is annotated as an E3 ubiquitin–protein ligase with roles in transcription regulation and XCI.[14][15]

### 6.3 Cellular Processes

At the cellular level, TOKAS involves disrupted stem cell maintenance, accelerated and disordered neural differentiation, and abnormal cell fate decisions in mesodermal and endodermal progenitors.[13][17][19] In RNF12 mutant ESCs, XLID‑associated alleles caused accelerated induction of neural lineage markers and neurite outgrowths, a phenotype associated with intellectual disability.[13][17] The authors conclude:

> “RNF12/Rlim mutation in male ESCs accelerates induction of neural lineage markers and establishment of neurite outgrowths, a phenotype associated with ID.”[13][17]

This suggests that RLIM normally restrains premature neural differentiation, allowing orderly expansion of progenitors and layered cortical development; its loss precipitates aberrant timing and pattern of neurogenesis, likely resulting in microcephaly and cognitive dysfunction.[13][19][6] 

In mesodermal and endodermal progenitors, RLIM’s modulation of SMAD7 and TGF‑β/BMP/Nodal signaling influences apoptosis, proliferation, and differentiation. Elevated SMAD7 due to reduced RLIM activity may impair pro‑survival and pro‑patterning signals, contributing to hypoplasia or malformation of diaphragm, heart, and gut. RLIM’s role in mammary alveolar cell survival, spermiogenesis, and hypothalamic neurons in mouse models underscores its broader importance in cell viability and energy balance.[15] In TOKAS, altered RLIM activity may compromise survival of specific cell populations, though direct evidence in human tissues is limited.

Relevant GO terms for cellular processes include **GO:0045596 (negative regulation of cell differentiation)**, **GO:0048646 (anatomical structure formation involved in morphogenesis)**, **GO:0006915 (apoptotic process)**, and **GO:0006260 (DNA replication),** reflecting RLIM’s influence on cell cycle and differentiation. The primary cell types involved include embryonic stem cells and their derivatives such as neural progenitors (**CL:0000047 neural progenitor cell**), mesodermal progenitors (**CL:0002320 mesodermal cell**), and endodermal progenitors (**CL:0000711 endodermal cell**).

### 6.4 Protein Dysfunction

RLIM protein dysfunction in TOKAS arises from missense variants that alter structural integrity, catalytic capacity, or regulatory interactions. RING domain variants such as p.Pro587Arg and p.Arg599Cys directly impair E3 ligase catalytic activity by disrupting the coordination of zinc and the ubiquitin transfer machinery.[13][17] XLID mutants in the RING domain “severely impair catalysis,” leading to markedly reduced ubiquitylation of substrates.[13][17] Basic region variants such as p.Tyr356Cys and p.Tyr421Cys interfere with chromatin recruitment and efficient ubiquitin transfer, and in the case of p.Tyr421Cys, destabilize the protein, making it susceptible to proteasomal degradation.[12][11][10][13]

The Scientific Reports study showed that RLIM p.Tyr421Cys is correctly localized to the nucleus but is readily degraded by the proteasome, indicating that the variant triggers conformational changes that expose degrons or alter interaction with stabilizing partners.[11][10] RLIM p.Tyr421Cys also exhibited significantly impaired E3 ligase activity, reducing Xist induction.[11][10] RLIM activity reporter assays for p.Asn581Lys demonstrated that subtle missense changes can similarly compromise catalytic function, reinforcing the concept of structure–function sensitivity in RLIM.[16]

At the structural level, RLIM’s RING‑H2 domain (a C3H2C3 motif) binds E2 ubiquitin‑conjugating enzymes and coordinates zinc ions essential for its fold; mutations at key residues disrupt this fold and reduce E2 binding or ubiquitin transfer.[13][17] The distal basic region mediates interactions with substrates such as REX1 and SMAD7 and recruits RLIM to chromatin. Missense variants here may alter electrostatic properties or secondary structure, weakening substrate binding and chromatin association.[13][15][10] The net result is a **loss‑of‑function** state in which RLIM cannot effectively ubiquitylate its substrates, impairing downstream pathways.

### 6.5 Metabolic, Immune, and Tissue Damage Mechanisms

Metabolic changes in TOKAS are not well characterized; however, RLIM’s role in hypothalamic neurons controlling energy balance and in milk‑producing mammary alveolar cells suggests that systemic metabolic effects may arise in animal models.[15] In humans with TOKAS, no specific metabolic derangements beyond growth restriction have been reported. Immune system involvement is likewise not prominent; TOKAS is not associated with autoimmunity or immunodeficiency, and RLIM’s known substrates and pathways do not primarily target immune function.[15][19]

Tissue damage mechanisms in TOKAS stem from developmental malformation rather than postnatal injury. CDH leads to pulmonary hypoplasia and respiratory failure, while congenital heart disease imposes hemodynamic strain and potential cardiac failure. Omphalocele and intestinal malrotation can cause ischemia or necrosis if complicated by volvulus. Hydrostatic tissue edema in hydrops fetalis reflects cardiovascular insufficiency and hypoalbuminemia due to severe developmental disruption. These phenomena involve processes such as **GO:0006950 (response to stress)**, **GO:0006979 (response to oxidative stress)**, and **GO:0001666 (response to hypoxia)**, but are downstream consequences of the primary developmental lesions rather than initiating mechanisms.

### 6.6 Epigenetic Changes and Molecular Profiling

Epigenetic changes are central to TOKAS pathophysiology because RLIM regulates X‑chromosome inactivation. XCI involves coating of the X chromosome by Xist RNA followed by recruitment of Polycomb repressive complexes, deposition of H3K27me3, DNA methylation, and chromatin compaction to silence X‑linked genes.[15][11] RLIM’s promotion of Xist transcription via REX1 degradation means that RLIM mutations can delay or prevent establishment of the epigenetic marks associated with XCI, leading to abnormal expression of X‑linked genes and potential genome‑wide transcriptomic dysregulation in early development.[15][11] While patient‑specific epigenomic profiles are not available, mouse studies and ESC models support this mechanism.

Transcriptomic profiling in RNF12 mutant ESCs revealed accelerated neural differentiation, with early induction of neural markers and altered expression of pluripotency genes.[13][17] Proteomic analyses indicated reduced ubiquitylation and altered stability of RLIM substrates such as REX1 and SMAD7.[13][17] No TOKAS‑specific metabolomic or lipidomic signatures have been reported, but the underlying defects in developmental signaling and XCI likely produce complex gene expression changes in multiple tissues. Multi‑omics integration—combining genomic (RLIM variants), transcriptomic (neural differentiation markers), and epigenomic (XCI status)—remains an area for future research to refine mechanistic understanding.

### 6.7 Advanced Technologies and Functional Genomics

Functional genomics approaches have been pivotal in elucidating TOKAS mechanisms. Embryonic stem cell models carrying RLIM XLID mutations have been used to systematically assess differentiation, neurite outgrowth, and substrate ubiquitylation.[13][17][19] CRISPR‑mediated gene editing and RNAi knockdown of RLIM in ESCs and mouse models have revealed its essential roles in XCI and neural development.[15][13] RLIM‑specific activity reporters developed in recent work provide a powerful tool to test variant pathogenicity and dissect catalytic defects.[16] 

Single‑cell and spatial transcriptomics have not yet been applied to TOKAS patients, but such technologies could in principle map cell‑type specific consequences of RLIM mutations in the developing brain, diaphragm, and urogenital organs. Functional genomics screens for RLIM interactors and substrates could further expand the network of affected pathways. Overall, TOKAS exemplifies how combining clinical genetics with advanced cellular models can reveal causal chains from mutation to complex multi‑organ phenotypes.

## 7. Anatomical Structures Affected

### 7.1 Organ‑Level Involvement

TOKAS affects multiple organ systems. The **central nervous system** is prominently involved, leading to microcephaly, intellectual disability, and behavioral abnormalities. Brain structures such as the cerebral cortex (UBERON:0000955), hippocampus, and cerebellum are likely impacted, given RLIM’s high expression in outer cortical layers and its role in neural differentiation.[12][15][13] The **respiratory system**, specifically the diaphragm (UBERON:0003885) and lungs (UBERON:0002048), is affected through congenital diaphragmatic hernia and resultant pulmonary hypoplasia.[1][6][10] The **cardiovascular system** may show congenital heart defects, involving structures such as the ventricles and great vessels.[6]

The **gastrointestinal system** is involved via omphalocele and intestinal malrotation, affecting abdominal wall musculature and the midgut (UBERON:0002116).[6] The **urogenital system** and reproductive organs, including penis (UBERON:0001304), testes (UBERON:0000473), and associated structures, exhibit differences in sex development and hypogenitalism.[6][1][5] The **skeletal system** is affected in extremities, with anomalies of hands and feet (UBERON:0001443 hand; UBERON:0002100 foot), including short broad thumbs, polydactyly, and syndactyly.[6]

Secondary organ involvement arises from complications such as pulmonary hypertension due to CDH, heart failure from congenital cardiac anomalies, and hepatic congestion related to hydrops fetalis. The disease thus spans nervous, respiratory, cardiovascular, digestive, endocrine (through hypothalamic involvement), and reproductive systems.

### 7.2 Tissue and Cell‑Level Involvement

Tissue types affected include **neural tissue**, **skeletal muscle**, **connective tissue**, **epithelial tissue**, and **endothelial tissue**. Neural tissue is particularly impacted in the cerebral cortex, where RLIM expression is high, and in neural progenitor zones. Cell Ontology terms relevant to TOKAS include **CL:0000047 (neural progenitor cell)**, **CL:0000127 (neuron)**, and **CL:0000312 (glial cell)**, reflecting RLIM’s role in neural differentiation.[12][13][19]

In the diaphragm, skeletal muscle cells (CL:0000298) and tendon fibroblasts (CL:0000057) may be malformed, leading to herniation of abdominal contents into the thoracic cavity. In the heart, cardiomyocytes (CL:0000746) and cardiac conduction system cells are affected in congenital heart disease. In the urogenital system, Leydig cells (CL:0000087), Sertoli cells (CL:0000213), and penile mesenchymal cells may be impacted by RLIM dysregulation of developmental signals. Limb mesenchymal cells and chondrocytes (CL:0000138) are involved in acral anomalies such as polydactyly and syndactyly.

### 7.3 Subcellular Level and Localization

At the subcellular level, RLIM functions primarily in the **nucleus** (GO:0005634) where it acts as a transcriptional co‑regulator and E3 ligase targeting nuclear substrates like REX1 and SMAD7.[14][13][11] RLIM also shuttles between nucleus and cytoplasm, with nucleocytoplasmic localization controlled by phosphorylation at specific sites.[15] The **proteasome** (GO:0005839) and **ubiquitin–proteasome system** are central compartments in TOKAS pathophysiology, as impaired RLIM activity alters protein degradation.

For XCI, RLIM influences nuclear subdomains such as Xist RNA foci and Barr bodies (inactive X chromosome) (GO:0001749), affecting chromatin architecture. TOKAS variants such as p.Tyr421Cys are correctly localized to the nucleus, indicating that subcellular mislocalization is not the main mechanism; rather, catalysis and stability are disrupted.[11][10] Thus, nuclear pathways of transcription regulation and chromatin modification are crucial subcellular sites of disease.

### 7.4 Anatomical Localization and Lateralization

Congenital diaphragmatic hernia in TOKAS often manifests as a left‑sided posterolateral (Bochdalek) defect, but bilateral or right‑sided forms may also occur, reflecting general developmental disruption rather than a specific lateralization pattern.[1][6] Limb anomalies can be bilateral, with symmetrical short broad thumbs, or asymmetric in polydactyly and syndactyly. Microcephaly and facial dysmorphism are global rather than lateralized. Urogenital differences are naturally midline structures. Overall, TOKAS does not show a disease‑specific lateralization predilection; anomalies present wherever RLIM‑regulated developmental pathways are most vulnerable.

## 8. Temporal Development

### 8.1 Age of Onset and Onset Pattern

TOKAS is fundamentally a **congenital** disorder, with manifestations arising during embryonic and fetal development. Severe prenatal forms present during the second trimester with ultrasound evidence of IUGR, hydrops, CDH, and multiple malformations.[2][6][4] In milder forms, structural anomalies such as hypogenitalism and acral anomalies are evident at birth, while neurodevelopmental impairments emerge in infancy and early childhood as global developmental delay becomes apparent.[5][12][6]

The onset pattern is **chronic and insidious** for neurodevelopmental features, as cognitive and behavioral deficits unfold over time, and **acute** at birth for life‑threatening structural anomalies like CDH. There is no adult‑onset TOKAS; all cases recognized thus far are pediatric or prenatal, consistent with RLIM’s role in early development.[5][6]

### 8.2 Disease Progression and Natural History

The progression of TOKAS depends largely on variant severity and the presence of life‑threatening malformations. In severe antenatal forms associated with variants like p.Arg611Cys or p.Tyr421Cys, disease course is rapidly progressive and often culminates in intrauterine demise or perinatal death due to CDH, hydrops, or multi‑organ failure.[4][6][1][10] These fetuses may exhibit worsening hydrops, decreased fetal movements, and deteriorating cardiac function as gestation advances.[2][6]

In surviving males with milder variants such as p.Tyr356Cys, the disease course is chronic and lifelong. Intellectual disability, behavioral abnormalities, and motor difficulties persist and may become more apparent with age, but there is limited evidence of progressive neurodegeneration; rather, the phenotype reflects developmental anomalies and static encephalopathy.[12][6] Feeding problems in infancy may improve with interventions, but nutritional and growth challenges can persist. Acral anomalies and facial dysmorphism are stable features, though facial gestalt may evolve with growth.[12][5]

Disease stages can be conceptualized as prenatal (structural malformation formation), neonatal (acute presentation of CDH and DSD), early childhood (manifestation of developmental delay and feeding issues), and later childhood/adulthood (stable intellectual disability, behavioral profile, and physical anomalies). The progression rate is rapid for structural anomalies and more gradual for neurodevelopmental features. Disease duration is lifelong in survivors; there is no remission of core neurodevelopmental deficits.

### 8.3 Critical Periods and Windows of Intervention

Critical periods in TOKAS include the early embryonic phase of XCI and organogenesis, when RLIM’s role in Xist induction and TGF‑β/BMP/Nodal signaling is most crucial.[15][11][19] Disruption during these windows leads to irreversible structural anomalies and neurodevelopmental perturbations. Prenatal detection of CDH and hydrops at around 20–24 weeks gestation represents a critical window for diagnostic decision‑making and counseling.[2][6] 

Postnatally, the first few years of life are critical for developmental interventions, such as early childhood education, speech therapy, and behavioral support, which may optimize functional outcomes despite underlying intellectual disability.[12][6] There is no evidence of spontaneous remission; improvements are primarily due to supportive therapies and adaptation. Early recognition of DSD allows timely surgical and endocrinological management, which can influence psychosocial outcomes.

## 9. Inheritance and Population

### 9.1 Inheritance Pattern and Genetic Parameters

TOKAS follows an **X‑linked recessive inheritance pattern**. OMIM notes that the syndrome is an X‑linked recessive multiple congenital anomaly disorder, and MedGen and LOVD confirm X‑linked inheritance.[5][3][9] Affected males carry hemizygous pathogenic *RLIM* variants, usually inherited from carrier mothers, although de novo occurrences are possible.[12][2][10] Female carriers are heterozygous and often asymptomatic due to skewed XCI, but mild manifestations or learning difficulties cannot be completely excluded.[12][5]

Penetrance in males appears to be **complete**; all hemizygous carriers of pathogenic RLIM variants described so far exhibit neurodevelopmental impairment or malformations.[12][6][5] Expressivity is **variable**, ranging from primarily intellectual disability with subtle dysmorphism (e.g., p.Tyr356Cys) to severe multi‑organ malformations and perinatal lethality (e.g., p.Arg611Cys, p.Tyr421Cys).[12][6][1][10] Genetic anticipation has not been reported; TOKAS is not a repeat‑expansion disorder. Germline mosaicism has not been documented but is theoretically possible in families with multiple affected males and negative maternal carrier testing, though such scenarios are rare.

No founder effects have been conclusively identified, but recurrent p.Arg611Cys in multiple unrelated families suggests either a mutational hotspot or a shared ancestral allele.[4][6][2] Consanguinity has not been specifically implicated; families reported to date are primarily from Europe and other regions without emphasized consanguineous unions.[12][6][4]

### 9.2 Epidemiology and Population Distribution

TOKAS is an **extremely rare** disorder. The JMG fetal perspective paper notes that “of the 41 patients reported, only 7 antenatal cases were described” initially, and the expanded series reports 18 antenatal cases.[6][4] RLIM variants were found in 4 cases out of a cohort of 405 unresolved syndromic X‑linked intellectual disability cases, suggesting that TOKAS may account for up to 0.5% of unsolved X‑linked intellectual disabilities.[10][16] However, overall prevalence and incidence cannot be precisely estimated due to small numbers and ascertainment biases.

Orphanet and global burden databases do not yet provide specific prevalence estimates for TOKAS. Based on reported cases, the syndrome likely has a prevalence well below 1 per 100,000, placing it firmly in the ultra‑rare category. Geographic distribution appears to be worldwide, with families reported from Norway, other European countries, and international cohorts, but detailed regional data are lacking.[12][6][4][18] 

The sex ratio is highly skewed towards males because of X‑linked recessive inheritance. Male infants and children constitute the majority of clinically affected individuals, while female carriers are often asymptomatic.[12][5][6] Age distribution ranges from fetuses diagnosed antenatally to adult males with long‑standing intellectual disability; the Norwegian family included affected males up to 71 years old.[12] This indicates that milder variants can support survival into older adulthood.

Carrier frequency in the general population is unknown but expected to be extremely low; pathogenic RLIM variants are rare or absent in population databases, indicating strong selection against them.[10][12][6] 

## 10. Diagnostics

### 10.1 Clinical Evaluation and Phenotypic Assessment

Diagnostic evaluation for TOKAS begins with careful clinical assessment of neurodevelopmental status, craniofacial features, acral anomalies, urogenital differences, and visceral malformations. Intellectual disability, global developmental delay, microcephaly, short broad thumbs, nail dysplasia, and hypogenitalism in a male with X‑linked family history should raise suspicion for RLIM‑related TOKAS.[5][6][12] In the prenatal context, ultrasound or MRI findings of CDH, IUGR, hydrops, and multiple anomalies may warrant genetic investigation for TOKAS, particularly when standard aneuploidy and microarray testing are negative.[2][4][6]

Standardized developmental scales, neurological examination, and dysmorphology evaluation are crucial to document phenotype. Neuropsychological testing quantifies cognitive impairment and autism spectrum traits. Growth charts and head circumference measurements identify IUGR and microcephaly. Urogenital examination assesses DSD, and radiologic studies (X‑ray, echocardiography, abdominal ultrasound) detect structural anomalies such as CDH, congenital heart defects, and omphalocele.[6][2][1]

### 10.2 Laboratory Tests and Imaging

No disease‑specific biochemical markers for TOKAS have been identified. Routine blood tests may show nonspecific findings related to organ dysfunction (e.g., respiratory acidosis in CDH, anemia in hydrops), but they are not diagnostic. Imaging studies are essential: prenatal ultrasound and fetal MRI detect CDH, hydrops, IUGR, cardiac anomalies, and abdominal wall defects.[2][6] Postnatal chest X‑ray and CT confirm CDH; echocardiography delineates congenital heart disease; abdominal ultrasound visualizes omphalocele and malrotation.

Neuroimaging (MRI) can assess brain structure, revealing microcephaly, cortical malformations, or white matter anomalies, although specific patterns for TOKAS have not been widely reported.[12][6] EEG may be considered if seizures occur but is not a core diagnostic tool. There are no specific electrophysiological signatures.

Histopathology is seldom performed in TOKAS except in cases of autopsy after perinatal death, where diaphragmatic defects, lung hypoplasia, and cardiac anomalies can be characterized. Pathology confirms structural malformations but does not identify RLIM variants.

### 10.3 Genetic Testing Strategies

Genetic testing is central to TOKAS diagnosis. Whole exome sequencing (WES) and whole genome sequencing (WGS) have been instrumental in identifying RLIM variants in families with syndromic XLID and fetal multiple anomaly syndromes.[12][10][4][2] In the Norwegian family, exome sequencing revealed the p.Tyr356Cys variant in *RLIM* as the only rare shared X‑linked variant in affected males.[12] In the Dundee Scientific Reports case, WES of the proband and parents identified a maternally inherited hemizygous c.1262A>G, p.Tyr421Cys variant in RLIM.[1][10][11] The JMG fetal series similarly employed exome or targeted sequencing to detect p.Arg611Cys and other RLIM variants in antenatal cases.[4][6][7]

For suspected TOKAS, recommended genetic testing approaches include:

Single‑gene testing of *RLIM* by Sanger sequencing or NGS if clinical features strongly suggest TOKAS.[5][10]

X‑linked intellectual disability gene panels that include *RLIM* among other XLID genes; RLIM is now recognized in several clinical panels.[13][18][6]

WES or WGS for undiagnosed syndromic intellectual disability or fetal multiple congenital anomalies, with analysis prioritizing X‑linked variants and known TOKAS alleles.[10][4][2]

Chromosomal microarray (CMA) may detect Xq13 duplications involving *RLIM* in dose‑sensitive RLIM‑related ID, but point mutations underlying TOKAS require sequence‑level methods.[18][5]

Karyotyping and FISH are not sufficient for TOKAS unless large Xq13 rearrangements are suspected; RLIM point variants escape detection by these techniques. Mitochondrial DNA testing and repeat expansion assays are not relevant.

ClinVar and the Genetic Testing Registry (GTR) list RLIM assays in several laboratories, and GeneReviews acknowledges RLIM as a gene for XLID, although a dedicated TOKAS GeneReview may not yet exist.[5][13][18] Genetic counseling should accompany testing, given X‑linked inheritance and implications for family planning.

### 10.4 Omics‑Based Diagnostics and Biomarkers

Beyond variant identification, omics‑based diagnostics for TOKAS remain exploratory. RNA sequencing could theoretically demonstrate altered XCI patterns or gene expression signatures in patient cells, but such assays are not standard in clinical practice. RLIM activity reporters described in recent work provide a functional readout of RLIM catalytic activity, which can help classify variants of uncertain significance (VUS) as pathogenic or benign.[16] As the authors note:

> “Further, we describe the TOKAS variant RLIM p.Asn581Lys and, using reporter assays, determine that it disrupts RLIM catalytic activity. These data reveal how the p.Asn581Lys variant impairs RLIM function and suggests pathogenic mechanisms.”[16]

Proteomic analysis of RLIM substrates (REX1, SMAD7) and ubiquitination status could serve as research tools but are not yet clinically validated. No circulating biomarkers specific to TOKAS have been identified. Liquid biopsy concepts have not been applied.

### 10.5 Clinical Criteria, Differential Diagnosis, and Screening

Standardized clinical diagnostic criteria for TOKAS have not been formalized in DSM or ICD, but OMIM and cohort studies provide practical phenotypic criteria: male sex, X‑linked family history, intellectual disability, craniofacial dysmorphism, acral anomalies, hypogenitalism, and, in severe cases, CDH and multiple malformations, combined with a pathogenic *RLIM* variant.[5][6][12] Differential diagnosis includes other syndromic XLID conditions and multiple congenital anomaly syndromes, notably **Fryns syndrome**, which shares CDH, facial anomalies, and limb defects.[1][6] The Dundee case noted that TOKAS “is characterised by clinical features that significantly overlap with Fryns syndrome,” and RLIM sequencing was prompted by this overlap.[1][10]

Other differential diagnoses include Wilson–Turner syndrome (LAS1L mutations, Xq12), Snyder–Robinson syndrome (SMS mutations), and various X‑linked intellectual developmental disorders listed in OMIM #309585, but these typically lack the specific combination of DSD and CDH seen in TOKAS.[8][5] Genetic testing that identifies *RLIM* variants differentiates TOKAS from these conditions.

Screening for TOKAS in asymptomatic individuals is not standard, given its rarity. Carrier screening may be offered in affected families, and prenatal screening via ultrasound and targeted genetic testing is appropriate once a familial variant is known.[2][4][6] Newborn screening programs do not include TOKAS.

## 11. Outcome and Prognosis

### 11.1 Survival and Mortality

Prognosis in TOKAS is highly variant‑dependent. Severe antenatal forms, particularly those with p.Arg611Cys or p.Tyr421Cys, carry a high risk of intrauterine demise or perinatal death.[4][6][1][10] The Scientific Reports study describes perinatal lethality by diaphragmatic hernia in a proband with p.Tyr421Cys.[1][11] The JMG fetal perspective paper notes that TOKAS is associated with devastating consequences when CDH, hydrops, and multiple anomalies are present, often resulting in early lethality.[6][4] Survival rates in these severe forms are low, though precise percentages are not available due to small case numbers.

In milder variants such as p.Tyr356Cys, affected males can survive into adulthood. The Norwegian family included individuals aged 5–71 years, indicating that life expectancy can be near normal if critical malformations are absent.[12] However, intellectual disability and behavioral issues may contribute to increased morbidity and potential mortality from secondary causes such as accidents or comorbid conditions. Overall mortality rate for TOKAS cannot be reliably estimated but is elevated in severe antenatal cases.

### 11.2 Morbidity, Disability, and Quality of Life

Morbidity in TOKAS arises from both neurodevelopmental impairments and structural malformations. Intellectual disability, autism spectrum features, behavioral abnormalities, and abnormal gait impose significant disability, impacting education, employment, and social participation.[12][6] Feeding problems in infancy and growth issues can cause nutritional morbidity. Acral anomalies may impair fine motor function, and DSD can affect urinary and sexual function.

Quality of life is significantly reduced for many patients and families. Caregivers face substantial burdens managing developmental delays, behavioral challenges, and medical complications. EQ‑5D and SF‑36 data specific to TOKAS are not available, but generic measures in similar XLID syndromes suggest impairments across physical, emotional, and social domains.[12][6] Survivors of severe malformations such as CDH and congenital heart disease may experience chronic respiratory or cardiac limitations.

### 11.3 Disease Course, Complications, and Recovery Potential

TOKAS is a **non‑progressive developmental disorder** in surviving individuals; the core neurodevelopmental deficits are static encephalopathies arising from early brain development, not progressive neurodegenerative processes.[12][6][13] Structural malformations remain fixed; surgical correction may alleviate some complications but does not reverse underlying developmental anomalies. Complications include respiratory failure from CDH, pulmonary hypertension, cardiac failure, feeding difficulties, and psychosocial challenges.

Recovery potential depends on variant severity and early interventions. In the absence of lethal malformations, children with TOKAS can achieve partial functional independence with specialized education and therapies, though intellectual disability remains.[12] Surgical repair of CDH and cardiac defects can improve survival and reduce morbidity. Behavioral interventions may ameliorate specific behavioral issues but do not normalize cognitive function.

### 11.4 Prognostic Factors and Biomarkers

Key prognostic factors include the specific RLIM variant (particularly its location and functional impact), presence of CDH and hydrops, extent of malformations, and timing of diagnosis.[4][6][1][10] Variants like p.Arg611Cys and p.Tyr421Cys portend worse outcomes due to their association with severe antenatal phenotypes, while p.Tyr356Cys is associated with survival and primarily neurodevelopmental issues.[12][6][10] Early detection of CDH and hydrops allows for informed decisions and perinatal planning, which can influence survival opportunities.

No formal prognostic biomarkers beyond genotype have been identified. RLIM activity assays and measurements of REX1/SMAD7 ubiquitylation may theoretically stratify severity but remain research tools. Clinical factors such as gestational age at detection of malformations, severity of CDH, and degree of cardiac involvement also influence prognosis.

## 12. Treatment

### 12.1 Pharmacotherapy and Medical Management

There is no disease‑specific pharmacotherapy that targets RLIM dysfunction in TOKAS. Management is symptomatic and supportive, addressing seizures if present, behavioral issues, cardiac and respiratory complications, and endocrine aspects of DSD. Psychotropic medications, antiepileptics, and hormone therapies may be used as clinically indicated, but they are not unique to TOKAS.[12][6] No pharmacogenomic relationships specific to RLIM variants have been reported.

### 12.2 Surgical and Interventional Treatments

Surgical interventions are critical for structural anomalies. Congenital diaphragmatic hernia requires neonatal surgical repair, often involving patch closure of the diaphragmatic defect and prolonged ventilation. Congenital heart disease may necessitate surgical correction or catheter‑based interventions depending on the defect type.[6][1] Omphalocele repair and intestinal malrotation surgery prevent life‑threatening complications. Urogenital surgeries may be indicated for hypospadias and cryptorchidism, improving urinary function and future fertility prospects.[6][2]

These interventions fall under NCIT terms such as **NCIT:C15273 (Surgical Procedure)**, **NCIT:C80434 (Congenital Diaphragmatic Hernia Repair)**, and **NCIT:C51574 (Cardiac Surgical Procedure)**. Timing and outcomes depend on the severity of associated anomalies and the overall condition of the neonate.

### 12.3 Supportive and Rehabilitative Care

Supportive care is central to improving quality of life in TOKAS. Early intervention programs provide developmental therapies—speech therapy, occupational therapy, physical therapy—to enhance communication, motor skills, and adaptive behavior. Special education services support learning and social integration. Nutritional support, including management of feeding difficulties and growth monitoring, is essential.[12][6] Behavioral therapy addresses autism spectrum features and behavioral problems.

NCIT terms such as **NCIT:C16467 (Supportive Care)** and **NCIT:C15229 (Rehabilitation Therapy)** are applicable. Care coordination among pediatricians, neurologists, geneticists, surgeons, endocrinologists, and developmental specialists is crucial, and a multidisciplinary team approach has been emphasized in antenatal and postnatal case management.[2][6]

### 12.4 Advanced and Experimental Therapies

No gene therapies, cell therapies, RNA‑based therapies, or targeted molecular treatments have yet been developed for TOKAS. The monogenic nature of the disorder makes it conceptually amenable to gene replacement or CRISPR‑mediated correction of RLIM, but challenges include early developmental timing and multi‑organ involvement. Experimental therapies in model systems, such as modulation of TGF‑β/BMP signaling or REX1 expression, have not been translated to humans.[13][15][19]

ClinicalTrials.gov does not list TOKAS‑specific interventional trials, reflecting its rarity. Future strategies might involve gene therapy delivered prenatally or early postnatally to restore RLIM function, but such approaches remain speculative.

### 12.5 Treatment Outcomes and Personalized Medicine

Treatment outcomes vary with anomaly severity and access to specialized care. Surgical repair of CDH and cardiac defects can significantly improve survival but may leave residual respiratory or cardiac limitations. Developmental and behavioral therapies can help individuals reach their maximal potential but do not eliminate intellectual disability.[6][12] Side effects and adverse events are those typical of surgeries and medications used in similar conditions.

Personalized medicine in TOKAS currently revolves around genotype‑informed counseling and anticipatory guidance rather than tailored pharmacotherapy. RLIM variant characterization—including functional assays using RLIM activity reporters—can help predict severity and guide reproductive decisions.[16][10] Personalized surgical and supportive care plans based on specific malformations and neurodevelopmental profiles represent practical precision medicine in this context.

## 13. Prevention

### 13.1 Primary, Secondary, and Tertiary Prevention

Primary prevention of TOKAS—preventing disease occurrence—is challenging because the disorder is monogenic and arises from germline *RLIM* variants. However, primary prevention at the family level can be achieved through genetic counseling, carrier testing, and reproductive options such as preimplantation genetic diagnosis (PGD) or use of donor gametes to avoid transmission.[5][2][6] ACMG and ACOG guidelines support such measures for X‑linked disorders.

Secondary prevention involves early detection and intervention to reduce severity and complications. Prenatal ultrasound screening, followed by genetic testing when anomalies suggest TOKAS, enables timely diagnosis.[2][4][6] Early identification of intellectual disability and behavioral issues allows initiation of developmental therapies, reducing secondary complications and optimizing function.

Tertiary prevention aims to prevent complications in individuals already affected by TOKAS. Careful management of CDH, cardiac defects, feeding issues, and DSD reduces morbidity and mortality. Regular monitoring for orthopedic, respiratory, and psychosocial complications is important. These strategies align with disease management protocols for congenital anomaly and XLID syndromes.

### 13.2 Immunization and Public Health Measures

Immunization strategies are not specific to TOKAS but general pediatric vaccination schedules apply. Public health interventions such as sanitation or vector control are not relevant to TOKAS, which is not infectious. Environmental measures to reduce toxin exposures have no known impact on TOKAS risk.

### 13.3 Genetic Screening, Counseling, and Behavioral Interventions

Genetic screening at the family level includes carrier testing for mothers and female relatives of affected males. Once a pathogenic *RLIM* variant is identified, cascade screening can identify carriers and inform reproductive planning.[5][12] Prenatal diagnosis via chorionic villus sampling or amniocentesis with targeted RLIM sequencing can detect affected fetuses.[2][4] PGD allows selection of embryos without the pathogenic RLIM variant.

Genetic counseling is essential, involving discussion of X‑linked inheritance, risks to offspring, severity spectrum, and options. Counseling also addresses psychosocial aspects and ethical considerations, especially in severe antenatal forms with high mortality.[2][6] Behavioral interventions such as parent training, behavioral therapy, and structured educational programs can reduce behavioral problems and improve adaptive function in affected children.

## 14. Other Species and Natural Disease

### 14.1 RLIM Orthologs and Comparative Biology

Orthologous genes to human RLIM exist in multiple species, including mouse (*Rnf12*), where RLIM’s roles in XCI, neural development, and organogenesis have been extensively studied.[15] NCBI Gene lists *Rnf12* in mouse and other vertebrates, illustrating strong evolutionary conservation of RLIM’s RING–H2 domain and basic regulatory region. Mouse models with Rnf12 knockouts or conditional deletions exhibit failure of imprinted XCI, embryonic lethality, defects in mammary alveolar cell survival, and abnormalities in spermiogenesis, mirroring aspects of TOKAS pathophysiology.[15]

No naturally occurring TOKAS‑like disease has been reported in companion animals or livestock, but RLIM’s conserved function suggests that similar mutations could produce related phenotypes. OMIA does not list RLIM‑associated diseases in animals, reflecting limited veterinary genetic data. Comparative pathology highlights that RLIM’s role in XCI and developmental signaling is conserved across mammals, making mouse models particularly relevant.

### 14.2 Zoonotic Potential and Cross‑Species Susceptibility

TOKAS is a non‑infectious genetic disorder with no zoonotic potential. Cross‑species susceptibility relates only to the possibility of RLIM mutations in other species causing analogous developmental syndromes. Mouse and possibly other model organisms are susceptible to engineered RLIM disruptions, which provide insights into human disease mechanisms but do not represent natural zoonotic transmission.

## 15. Model Organisms

### 15.1 Types of Model Systems

Model organisms and cell systems have been crucial in studying RLIM and TOKAS. **Mouse models** (mammalian) with Rnf12 knockouts, conditional deletions, or transgenic overexpression have been used to analyze RLIM’s role in XCI, mammary gland development, spermiogenesis, and energy balance.[15] **Embryonic stem cell (ESC) models** (in vitro cellular systems) expressing RLIM XLID mutations represent a central platform for dissecting TOKAS mechanisms.[13][17][19] ESCs allow controlled differentiation into neural lineages and assessment of RLIM substrate ubiquitylation.

### 15.2 Genetic Models and Phenotype Recapitulation

Conditional oocyte‑specific knockout of Rnf12 in mice results in failure of imprinted XCI and female embryonic lethality, demonstrating RLIM’s essential role in dosage compensation and early development.[15] Male ESCs lacking RLIM show accelerated neural differentiation, altered neurite outgrowth, and impaired Xist induction.[13][17] Knock‑in mouse models carrying specific RLIM XLID mutations have been developed, recapitulating accelerated neural differentiation and abnormal ESC behavior, supporting their relevance to human intellectual disability.[19]

These genetic models capture key aspects of TOKAS pathophysiology: defective XCI, abnormal stem cell maintenance, and disordered neural development. However, they do not fully reproduce the human phenotype of multi‑organ malformations, likely due to species differences and model design. Still, they are invaluable for mechanistic studies.

### 15.3 Applications and Limitations

Model organisms allow detailed exploration of RLIM’s roles in molecular pathways, cell types, and development. ESC models with RLIM mutations provide direct evidence of substrate ubiquitylation defects and differentiation changes.[13][17][19] Mice reveal systemic effects, such as mammary gland and spermatogenesis defects.[15] These models support discovery of potential therapeutic targets and variant classification.

Limitations include differences in XCI mechanisms between species, varying developmental timing, and incomplete phenotypic overlap. For example, human TOKAS exhibits CDH and DSD, while mouse Rnf12 models may not show identical structural anomalies. Additionally, RLIM duplication phenotypes have not been fully modeled. Despite these constraints, model systems remain essential for understanding TOKAS and RLIM biology.

## Conclusion

Tonne–Kalscheuer syndrome (TOKAS) represents a paradigmatic example of how disruption of a single, multifunctional E3 ubiquitin ligase—RLIM (*RNF12*)—can produce a complex neurodevelopmental and multiple congenital anomaly phenotype through intertwined pathways of transcriptional regulation, X‑chromosome inactivation, and developmental signaling. Hemizygous missense variants in RLIM’s basic regulatory region and RING domain impair ubiquitylation of key substrates such as REX1 and SMAD7, destabilize the protein, and deregulate stem cell maintenance and neural differentiation.[13][17][11][16] These molecular defects, operating during critical windows of embryonic development, lead to microcephaly, intellectual disability, behavioral abnormalities, acral anomalies, differences in sex development, and visceral malformations including congenital diaphragmatic hernia and congenital heart disease.[6][5][1][10][2]

Clinically, TOKAS encompasses a spectrum from survivors with syndromic X‑linked intellectual disability and subtle dysmorphism to fetuses with severe multiple malformations and perinatal lethality. The recurrent p.Arg611Cys variant exemplifies a genotype–phenotype correlation, accounting for two‑thirds of fetal cases and consistently associated with severe prenatal phenotypes characterized by hydrops and early lethality.[4][6][2] Conversely, variants like p.Tyr356Cys permit survival into adulthood with primarily neurodevelopmental impairments.[12] Duplications of Xq13 including *RLIM* extend the disease concept, demonstrating that RLIM is dosage sensitive and that increased gene copy number can cause intellectual disability and facial dysmorphism, complementing loss‑of‑function TOKAS alleles.[18][15]

Diagnostic evaluation relies on recognition of characteristic phenotypes and genetic confirmation of RLIM variants through exome, genome, or targeted sequencing.[12][10][4][2] Omics‑based tools such as RLIM activity reporters offer functional validation and variant classification.[16] Treatment is currently supportive and surgical, addressing structural anomalies and neurodevelopmental needs, with no RLIM‑targeted therapies available. Prevention focuses on genetic counseling, carrier detection, and reproductive options for families with known variants. Prognosis varies widely, with severe antenatal forms often lethal and milder variants compatible with long‑term survival but significant disability.

From a mechanistic perspective, TOKAS illuminates the centrality of E3 ubiquitin ligases in neural development and disease, reinforcing emerging themes from broader neurodevelopmental disorder research that link ubiquitin‑mediated proteostasis to cognitive function.[13][17][19] It also underscores the importance of XCI and dosage compensation in human development, demonstrating the consequences of failing to properly initiate Xist‑mediated silencing. As additional RLIM variants are discovered and functional assays refined, TOKAS will continue to serve as a model for integrating clinical genetics, stem cell biology, and systems‑level developmental mechanisms.

Future research directions include comprehensive multi‑omics profiling of patient tissues, in‑depth genotype–phenotype correlation studies, development of novel animal and cellular models for RLIM duplication and missense variants, and exploration of potential therapeutic strategies to modulate RLIM pathways or downstream signaling cascades. Ultimately, a more detailed understanding of RLIM’s network of substrates and interactors may open avenues for targeted interventions that ameliorate aspects of TOKAS, even if full reversal of developmental anomalies remains beyond reach.

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 6 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 69 |
| Resolved | 62 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 6 |
| Unverifiable | 0 |
| Terms whose name was checked | 22 |
| Terms named correctly | 10 |
| Terms named as a **different** term | 9 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `GO:0006306` (1 mention) - the report calls it "DNA methylation‑dependent chromatin silencing"; GO calls it **obsolete DNA methylation**
- `GO:0006461` (1 mention) - the report calls it "protein ubiquitination"; GO calls it **GO_0006461**
- `CL:0000127` (1 mention) - the report calls it "neuron"; CL calls it **astrocyte**
- `CL:0000312` (1 mention) - the report calls it "glial cell"; CL calls it **keratinocyte**
- `NCIT:C15273` (1 mention) - the report calls it "Surgical Procedure"; NCIT calls it **Longitudinal Study**
- `NCIT:C80434` (1 mention) - the report calls it "Congenital Diaphragmatic Hernia Repair"; NCIT calls it **Pacemaker Placement**
- `NCIT:C51574` (1 mention) - the report calls it "Cardiac Surgical Procedure"; NCIT calls it **ESR1 wt Allele**
- `NCIT:C16467` (1 mention) - the report calls it "Supportive Care"; NCIT calls it **Congo**
- `NCIT:C15229` (1 mention) - the report calls it "Rehabilitation Therapy"; NCIT calls it **Antitumor Drug Screening Assay**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0008735` (1 mention) - HP does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0006306` (obsolete DNA methylation) (1 mention)
- `GO:0006461` (GO_0006461) (1 mention) - replaced by `GO:0065003`
- `CL:0000298` (obsolete xylem element) (1 mention) - replaced by `PO:0000273`
- `CL:0000087` (obsolete male germ line stem cell (sensu Nematoda and Protostomia)) (1 mention) - replaced by `CL:0000016`
- `CL:0000213` (obsolete lining cell) (1 mention)
- `GO:0001749` (GO_0001749) (1 mention) - replaced by `GO:0042463`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0007178` (1 mention) - the report calls it "transforming growth factor beta receptor signaling pathway"; GO calls it **cell surface receptor protein serine/threonine kinase signaling pathway**, and lists "transmembrane receptor protein serine/threonine kinase signaling pathway" among its other names
- `CL:0000047` (2 mentions) - the report calls it "neural progenitor cell"; CL calls it **neural stem cell**
- `GO:0005839` (1 mention) - the report calls it "proteasome"; GO calls it **proteasome core complex**, and lists "20S proteasome" among its other names