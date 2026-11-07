---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-10-27T14:37:59.377727'
end_time: '2026-10-27T14:44:09.378776'
duration_seconds: 370.0
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Cataract 21 Multiple Types
  mondo_id: MONDO:0012437
  category: Genetic
  causal_genes: MAF
  omim_id: not recorded
  synonyms: not recorded
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 51
reference_validation:
  total_references: 20
  verified: 20
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 20
  on_topic: 16
  validator_version: 0.4.0
term_validation:
  total_terms: 38
  verified: 34
  not_found: 0
  obsolete: 0
  unverifiable: 4
  confabulation_rate: 0.0
  labels_checked: 19
  labels_matching: 9
  labels_mismatched: 10
  mislabelled_terms:
  - term_id: MONDO:0012437
    reported_labels:
    - MONDO
    ontology_label: cataract 21 multiple types
  - term_id: DOID:0110256
    reported_labels:
    - Disease Ontology
    ontology_label: cataract 21 multiple types
  - term_id: HP:0007780
    reported_labels:
    - "Gradual acuity loss; surgery at 25\u201329 years in one pedigree"
    ontology_label: Cortical pulverulent cataract
  - term_id: HP:0007976
    reported_labels:
    - Reading/distance difficulty develops gradually; extraction may occur in adolescence
      or adulthood
    ontology_label: Cerulean cataract
  - term_id: HP:0100018
    reported_labels:
    - High amblyopia risk if central and untreated
    ontology_label: Nuclear cataract
  - term_id: HP:0001134
    reported_labels:
    - May be observed if not visually significant
    ontology_label: Anterior polar cataract
  - term_id: HP:0000482
    reported_labels:
    - Complicates surgery and may influence refractive outcome
    ontology_label: Microcornea
  - term_id: HP:0000612
    reported_labels:
    - Glare, photophobia or additional acuity impairment
    ontology_label: Iris coloboma
  - term_id: HP:0000568
    reported_labels:
    - Poorer visual prognosis; glaucoma risk after surgery
    ontology_label: Microphthalmia
  - term_id: HP:0000639
    reported_labels:
    - Marker of poorer visual prognosis
    ontology_label: Nystagmus
  unresolvable_prefixes:
  - ORPHA
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Cataract 21 Multiple Types
- **MONDO ID:** MONDO:0012437 (if available)
- **Causal gene(s):** MAF
- **OMIM:** not recorded
- **Synonyms:** not recorded
- **Category:** Genetic

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Cataract 21 Multiple Types** covering all of the
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

# Cataract 21, Multiple Types — Comprehensive Disease Report

**Scope and identity.** Cataract 21, multiple types is a rare, usually nonsyndromic developmental cataract caused by heterozygous germline variants in **MAF**, which encodes the c-MAF basic-region leucine-zipper transcription factor. This report follows **MONDO:0012437 / OMIM 610202 / MAF**, not similarly numbered cataracts caused by other genes and, except where needed for differential diagnosis, not the allelic multisystem **Aymé-Gripp syndrome** caused mainly by variants in a different MAF domain. Authoritative resources define the disorder as early-onset nonsyndromic cataract, variably accompanied by microcornea, iris coloboma or other anterior-segment abnormalities.[2][4][157]

**Evidence date:** 27 October 2026. Disease-specific evidence remains largely from pedigrees, individual case reports and experimental models rather than registries or prospective cohorts.

---

## 1. Disease information

### 1.1 Definition

Cataract 21 is an autosomal-dominant lens-development disorder with unusually heterogeneous cataract morphology. Reported forms include cortical pulverulent, lamellar/zonular, nuclear, nuclear pulverulent, nuclear stellate, anterior polar, anterior or posterior subcapsular, posterior polar and cerulean/blue-dot cataracts. Onset ranges from congenital to juvenile; progression ranges from clinically significant cataract in early infancy to slowly progressive opacities requiring extraction in adolescence or adulthood.[69][158]

“Pulverulent” describes punctate, dust-like opacities, whereas cerulean cataract comprises blue-white opacities that may develop in concentric lens layers.[145][148]

### 1.2 Identifiers and synonyms

| Resource | Identifier/name | Comments |
|---|---|---|
| MONDO | **MONDO:0012437** | Target disease |
| OMIM phenotype | **610202** | Cataract 21, multiple types |
| OMIM gene | **177075** | MAF |
| MedGen | **C1857768**, UID 347538 | Aggregated disease record |
| Disease Ontology | **DOID:0110256** | Heterozygous MAF-related cataract |
| Orphanet | **ORPHA:91492** | Broader parent category: early-onset nonsyndromic cataract |
| Orphanet | **ORPHA:98984** | Pulverulent cataract; MAF is listed as a disease gene |
| ICD-10-CM | **Q12.0** | Congenital cataract; not MAF-specific |
| ICD-11 | **LA12.1** congenital cataract; **9B10.1** infantile/juvenile cataract | Not MAF-specific |
| UMLS | **C1857768** | Cataract 21 multiple types |
| MeSH | **Cataract / congenital; Cataract / genetics** | No disease-specific MeSH descriptor |
| HGNC | **HGNC:6776** | MAF |
| NCBI Gene | **4094** | MAF |
| Ensembl | **ENSG00000178573** | MAF |
| RefSeq | **NM_005360.5**, **NP_005351.2** | Common clinical transcript/protein |
| UniProtKB | **O75444** | Human transcription factor Maf |

The chromosome location is **16q23.2**. MAF is a protein-coding gene whose product can act as a homodimer or heterodimer and as a transcriptional activator or repressor, depending on target sequence and partner.[88][89][93]

**Common alternative names:** CTRCT21; CCA4; cataract 21 with or without microcornea; congenital cerulean cataract type 4; juvenile-onset pulverulent cataract; MAF-related early-onset nonsyndromic cataract; cataract, pulverulent or cerulean, with or without microcornea.[148]

### 1.3 Data provenance

The core assertions are **aggregated disease-level knowledge derived from published families and individual patients**, not routine EHR-derived evidence. OMIM, Mondo, MedGen, ClinVar and Orphanet aggregate those reports. The 2024 p.Lys308Glu report, for example, is one deeply phenotyped child, while the R288P and K297R evidence comes from multigenerational pedigrees.[58][105][118]

---

## 2. Etiology

### 2.1 Primary cause

The initiating cause is generally a **heterozygous germline MAF variant**, most often a missense change affecting the C-terminal extended homology, basic DNA-binding or leucine-zipper region. These variants disturb c-MAF regulation of lens-fiber differentiation and crystallin/noncrystallin target genes. Autosomal-dominant transmission and de novo occurrence are both documented.[52]

A regulatory chromosomal lesion has also been reported: a familial **t(5;16)(p15.3;q23.2)** breakpoint disrupted the genomic-control domain of MAF and cosegregated with cataract, anterior-segment dysgenesis and microphthalmia.[58]

### 2.2 Genetic risk factors

| Genetic factor | Evidence and interpretation |
|---|---|
| Pathogenic/likely pathogenic MAF variant | Principal causal factor; monoallelic |
| Location in C-terminal DNA-binding/bZIP region | Strongly enriched among isolated ocular cases |
| Positive family history | Substantially increases prior probability under AD inheritance |
| De novo variant | Documented, including p.Lys308Glu and p.Arg299Cys |
| Variant-specific transcriptional effect | Correlates imperfectly with morphology and severity |
| Genetic background/modifiers | Suggested by marked intrafamilial variability and demonstrated in Ofl mice, but no human modifier gene is established |
| N-terminal phosphorylation-motif variant | Raises concern for Aymé-Gripp syndrome rather than isolated Cataract 21 |

C-terminal MAF variants tend to cause isolated ocular disease, whereas variants around N-terminal GSK3 phosphorylation motifs more often cause Aymé-Gripp syndrome. This correlation is clinically useful but not absolute: some N-terminal variants have been reported with isolated cataract.[396][421]

### 2.3 Environmental, infectious and lifestyle factors

No toxin, infection, diet or lifestyle exposure is established as a cause or penetrance modifier of **molecularly confirmed MAF-related Cataract 21**. Maternal rubella, CMV, toxoplasmosis, syphilis, varicella, radiation, selected medicines and metabolic disease are important causes of *phenotypically similar congenital cataract*, but are alternative etiologies rather than causes of this Mendelian disorder.[493][500]

Smoking, alcohol, diabetes and ultraviolet exposure are recognized in broader acquired cataract biology, but should not be annotated as demonstrated risk factors for MAF-related developmental cataract.

### 2.4 Protective factors and gene–environment interaction

- **Genetic protective variants:** none established.
- **Environmental protective factor after conception:** none shown to prevent cataract in a person carrying a pathogenic MAF allele.
- **Rubella immunization and avoidance of fetal teratogens:** prevent some non-MAF congenital cataracts but do not prevent transmission or action of a MAF variant.
- **Gene–environment interaction:** not directly demonstrated. Variable expressivity among relatives with the same variant suggests modifiers, but environmental causation has not been separated from stochastic developmental or genetic-background effects.[502]

---

## 3. Phenotypes

Frequency estimates are unreliable because published cases are selected by cataract clinics and often comprise single families. “Common” below therefore means repeatedly reported, not a population prevalence.

| Phenotype/type | Onset, severity, course and frequency | Functional/QoL effect | Suggested HPO term |
|---|---|---|---|
| Cataract, multiple morphologies — sign | Congenital, infancy, childhood or juvenile; usually bilateral; severity highly variable; defining feature | Blurred vision, poor fixation and impaired visual development | Cataract **HP:0000518**; congenital cataract **HP:0000519** |
| Cortical pulverulent cataract — sign | Juvenile symptoms in the R288P family; punctate cortical opacities; progressive posterior subcapsular opacification in adults | Gradual acuity loss; surgery at 25–29 years in one pedigree | **HP:0007780** |
| Cerulean/blue-dot cataract — sign | Early-onset bilateral; tiny blue/white opacities may become apparent around 18–24 months; generally slow progression | Reading/distance difficulty develops gradually; extraction may occur in adolescence or adulthood | **HP:0007976** |
| Nuclear cataract — sign | Congenital or early childhood; may be visually dense | High amblyopia risk if central and untreated | **HP:0100018** |
| Lamellar/zonular cataract — sign | Congenital or childhood; variable visual significance | Central opacities impair acuity and contrast | Lamellar cataract **HP:0007971** |
| Anterior polar cataract — sign | Congenital/early-onset; often small but variable | May be observed if not visually significant | **HP:0001134** |
| Posterior polar/subcapsular cataract — sign | Sometimes secondary progression after an initial pulverulent phenotype | Glare and progressive visual impairment | Posterior polar cataract **HP:0001115**; posterior subcapsular cataract |
| Total cataract — sign | Rare but reported; the 2024 p.Tyr301His proband progressed rapidly around age three | Severe monocular visual loss and leukocoria | Total cataract; leukocoria **HP:0000554** |
| Microcornea — physical sign | Variable and not obligatory; 2/5 in the R288P pedigree and 6/12 in the K297R family | Complicates surgery and may influence refractive outcome | **HP:0000482** |
| Iris coloboma — physical sign | Occasional; one of five R288P relatives had bilateral inferior colobomas | Glare, photophobia or additional acuity impairment | **HP:0000612** |
| Peters anomaly/anterior-segment dysgenesis — sign | Rare; especially associated with MAF regulatory disruption or severe developmental phenotypes | Corneal opacity and higher surgical complexity | **HP:0000659**; anterior-segment dysgenesis |
| Microphthalmia — sign | Rare; reported in the translocation family and Maf-null models | Poorer visual prognosis; glaucoma risk after surgery | **HP:0000568** |
| Reduced visual acuity/visual impairment — symptom/sign | Proportional to density, location and treatment delay | Reading, mobility, play and educational difficulties | Visual impairment **HP:0000505** |
| Deprivation/anisometropic amblyopia — complication | Develops during the early visual-plasticity window | Can permanently limit vision despite anatomically successful surgery | Amblyopia **HP:0000646** |
| Strabismus/esotropia — complication | Secondary to unequal or deprived vision | Binocular and psychosocial effects | Strabismus **HP:0000486**; esotropia **HP:0000565** |
| Nystagmus — complication | Develops after prolonged early bilateral deprivation | Marker of poorer visual prognosis | **HP:0000639** |
| Secondary glaucoma — postoperative complication | Not intrinsic in most families; reported after early lensectomy and with a few C-terminal variants | Lifelong monitoring and medication/surgery may be required | Glaucoma **HP:0000501** |

In the five-person R288P pedigree, every examined affected relative had cortical and/or nuclear pulverulent cataract, two had microcornea, one had iris coloboma and all affected adults developed additional posterior subcapsular opacity. This is strong evidence for variable expressivity within one genotype.[60]

The 2024 p.Lys308Glu child illustrates severe congenital disease: bilateral nuclear/cortical cataracts at six weeks, surgery at seven and eight weeks, postoperative glaucoma and amblyopia, with final acuity of 20/125 and 20/40 at age five.[23]

### Quality of life

No MAF-specific QoL cohort exists. In broader surgically treated congenital/developmental cataract populations, postoperative children remain below controls across PedEyeQ domains; one 107-child study found the largest deficit—27 points—in functional vision among children aged 0–4 years.[452] A prospective pediatric study nevertheless found improved or maintained questionnaire scores after surgery in 78.2% for general health, 82.6% for general vision, and 95.6% for competence.[451]

---

## 4. Genetic and molecular information

### 4.1 Gene/protein

| Attribute | Value |
|---|---|
| Gene | **MAF** |
| HGNC | **HGNC:6776** |
| NCBI Gene | **4094** |
| OMIM gene | **177075** |
| Location | **16q23.2** |
| Reference transcript | **NM_005360.5** |
| Protein | c-MAF/transcription factor Maf, **NP_005351.2**, UniProt **O75444** |
| Functional class | Large-MAF bZIP transcription factor |
| Relevant domains | N-terminal transactivation domain; extended homology region; basic DNA-binding motif; leucine zipper |
| Cellular localization | Predominantly nucleus |
| Origin of disease variants | Germline; inherited AD or de novo |

### 4.2 Published isolated-ocular variants

This table emphasizes published variants linked to nonsyndromic cataract. Classification is study/ClinVar dependent and may change.

| Variant, NM_005360.5 | Protein/domain | Phenotype/evidence | Classification/population evidence |
|---|---|---|---|
| c.782T>C | p.Phe261Ser; C-terminal | Isolated cataract reported | Missense; rare; detailed frequency unavailable |
| c.809C>A | p.Ser270Tyr; extended homology | Nuclear cataract, bilateral microcornea, glaucoma | Reported pathogenic |
| c.812T>A | p.Val271Glu; extended homology | Bilateral nuclear/lamellar cataract | Pathogenic; impaired CRYAA, CRYBA1, CRYBA4, CRYGA, HMOX1 and KDELR2 activation, PMID **30659945**[409] |
| c.819G>C | p.Glu273Asp; extended homology | Sporadic congenital cataract | Likely pathogenic |
| c.863G>C | p.Arg288Pro; basic motif | Pulverulent/lamellar cataract ± microcornea/coloboma | Pathogenic; rs121917735; AD; PMID **11772997**[58][479] |
| c.880C>T | p.Arg294Trp; basic motif | Nuclear cataract | Pathogenic/likely pathogenic |
| c.890A>G | p.Lys297Arg; basic motif | Cerulean cataract; microcornea in 6/12 affected relatives | Pathogenic; rs121917736; absent from 106 controls; PMID **16470690**[105] |
| c.892A>T | p.Asn298Tyr; basic motif | Congenital cataract | Significance varies by report |
| c.895C>A | p.Arg299Ser; basic motif | Lamellar/stellate cataract, microcornea, occasional coloboma | Disease-associated; PMID **17982426**[487] |
| c.895C>T | p.Arg299Cys; basic motif | Bilateral cataract, sometimes de novo | ClinVar pathogenic/likely pathogenic; absent from ExAC[103][104] |
| c.901T>C | p.Tyr301His; basic motif | Rapidly progressive total congenital cataract in a Chinese AD family | Likely pathogenic: PM1, PM2, PP1, PP2, PP3; absent from public databases and 200 controls; PMID **38487030**[120] |
| c.905C>T | p.Ala302Val; basic motif | Congenital cataract | Likely pathogenic |
| c.908A>C | p.Gln303Pro; basic motif | Lamellar cataract ± microcornea/iris coloboma | AD; six affected relatives; reported pathogenic |
| c.915C>T | p.Cys305Trp; basic motif | Congenital cataract, glaucoma reported | Likely pathogenic |
| c.916C>G | p.Arg306Gly; basic motif | Congenital cataract | Rare missense; classification incompletely documented |
| c.922A>G | p.Lys308Glu; near leucine zipper | De novo bilateral nuclear/cortical congenital cataract | Likely pathogenic: PS2, PM1, PM2, PP3; absent from gnomAD; PMID **38927621**[23] |
| c.947T>C | p.Leu316Pro; leucine zipper | Nuclear, zonular/structural cataract | Likely pathogenic; AD |
| c.950A>G | p.Glu317Gly; leucine zipper | Posterior polar cataract | Pathogenic; AD |
| c.958A>G | p.Lys320Glu; leucine zipper | Cataract with microcornea | AD |
| frameshift near p.Pro366 | p.Pro366Argfs*8 | Cataract reported | Putative loss-of-function; evidence more limited than recurrent missense variants |

A 2024 review counted 17 previously reported C-terminal variants associated with isolated cataract; all were missense and inherited dominantly or de novo. The same review documented microcornea with variants in multiple C-terminal subdomains and occasional iris coloboma, confirming that domain location does not fully predict severity.[23]

### 4.3 Functional consequence

The molecular consequence is **variant-specific**, not a simple uniform haploinsufficiency:

- R288P can abolish transcriptional activation despite preserved in-vitro DNA-complex stability; it was not dominantly negative in every reporter context.[410]
- R288P reduced CRYGA and CRYBA1 reporter expression; R299S produced the strongest overall reduction across four crystallin reporters, while K297R had a comparatively modest effect. These differences may explain some genotype–phenotype variation (PMID **25064449**).[433][434]
- Val271Glu impaired both structural-crystallin genes and stress-response targets.[409]
- Mouse Asp90Val is a gain-of-transactivation mutation, demonstrating that both reduced and excessive c-MAF activity can disturb lens transparency.[444]

### 4.4 Modifier, epigenetic and structural information

- **Established human modifier genes:** none.
- **Epigenetic disease signature:** none validated in patient lenses or blood.
- **Chromosomal abnormalities:** the t(5;16)(p15.3;q23.2) regulatory-domain disruption is the principal structural example.[58]
- **Somatic variants:** not the recognized mechanism; disease-associated variants are germline.
- **Allele frequency:** established pathogenic alleles are absent or extremely rare in population datasets. Exact gnomAD frequencies should be verified against the current build and transcript during variant interpretation rather than inferred from dbSNP presence.

---

## 5. Environmental information

| Category | Disease-specific conclusion |
|---|---|
| Toxins/radiation/pollution | No demonstrated role in genetically confirmed Cataract 21 |
| Maternal infection | TORCH infections are differential etiologies, not known MAF modifiers |
| Smoking/alcohol/diet/exercise | No MAF-specific association |
| Occupational exposure | Not applicable to congenital onset |
| Infectious agent | None; disease is not infectious |
| Protective exposure | None established |
| Immune involvement | MAF has important immune functions, but isolated Cataract 21 has no demonstrated immune pathogenesis |

The absence of disease-specific environmental evidence is important: general cataract risk-factor annotations should not automatically be imported into this Mendelian entry.

---

## 6. Mechanism and pathophysiology

### 6.1 Ordered causal chain

1. A heterozygous germline **MAF** coding variant—or, rarely, disruption of its regulatory domain—**leads to** altered c-MAF abundance, conformation, DNA-target recognition, dimerization or transcriptional activity.  
2. Altered c-MAF activity **leads to** abnormal binding/transactivation at Maf-recognition elements in crystallin and noncrystallin lens-development genes.  
3. This transcriptional defect **results in** reduced or mistimed expression of structural proteins such as CRYAA, CRYBA1, CRYBA4 and CRYGA and of stress/homeostasis genes such as HMOX1 and KDELR2; the precise targets are variant-dependent.  
4. Dysregulated target expression **leads to** abnormal withdrawal from the cell cycle, elongation and terminal differentiation of equatorial lens epithelial cells into lens-fiber cells.  
5. Defective fiber-cell maturation **results in** disordered fiber architecture and altered high-concentration crystallin composition/solubility. Protein aggregation and refractive-index heterogeneity are strongly inferred downstream events but have not been directly measured in most MAF patient lenses.  
6. Abnormal fiber structure and protein homeostasis **lead to** light scattering and focal or diffuse lens opacity—pulverulent, nuclear, lamellar, cerulean, polar or subcapsular cataract.  
7. **Branch A:** if early ocular morphogenesis is more broadly disturbed, abnormal lens–anterior-segment interactions **lead to** microcornea, iris coloboma, Peters anomaly or microphthalmia.  
8. **Branch B:** if a dense cataract blocks the visual axis during early visual plasticity, degraded retinal input **leads to** deprivation/anisometropic amblyopia, strabismus and sometimes sensory nystagmus.  
9. **Treatment branch:** lensectomy restores optical passage but **can lead to** aphakia, capsular opacification/phimosis and lifelong risk of secondary glaucoma.

### 6.2 Upstream molecular events

MAF binds DNA through its basic region and dimerizes through the leucine zipper. Its extended homology region stabilizes DNA interactions. c-MAF also recruits coactivators **CREBBP/CBP** and **EP300/p300** to crystallin promoters. The best-established direct pathway is therefore a transcription-factor network rather than a conventional receptor cascade.[86][224]

Relevant suggested GO terms include:

- lens-fiber-cell differentiation — **GO:0070306**
- lens development in camera-type eye — **GO:0002088**
- regulation of transcription by RNA polymerase II — **GO:0006357**
- DNA-binding transcription activator activity, RNA polymerase-II-specific
- sequence-specific double-stranded DNA binding
- protein homodimerization and heterodimerization
- cell-cycle exit and epithelial-cell differentiation
- nucleus — **GO:0005634**
- transcription regulator complex — **GO:0005667**

### 6.3 Cellular and tissue mechanisms

The critical transition is from anterior/equatorial lens epithelial cells to elongated secondary fiber cells. In Maf-null mice, posterior fiber elongation fails and crystallin expression is markedly impaired, causing microphthalmia and abnormal lens formation (PMID **10097114**).[211] A second developmental study found MAF highly upregulated at the lens equator, where epithelial cells leave the cell cycle and differentiate; MAF directly activated many β-crystallin genes (PMID **10603348**).[235]

Suggested Cell Ontology terms:

- lens epithelial cell — **CL:0002224**
- anterior lens cell — **CL:0002223**
- secondary lens fiber — **CL:0002225**

### 6.4 Metabolic, immune and tissue-damage components

No primary enzyme deficiency or systemic metabolomic signature is known. Altered HMOX1 activation suggests that cellular stress handling may contribute for some alleles, but oxidative stress is downstream/supportive rather than the demonstrated initiating lesion.[409] There is no evidence that autoimmunity or inflammation initiates isolated MAF cataract.

### 6.5 Recent single-cell and multi-omics research

A 2024 embryonic-chicken lens study integrated **single-nucleus RNA-seq, single-nucleus ATAC-seq and CUT&RUN**. It found progressive MAF expression and increasing accessibility of MAF motifs along the epithelial-to-fiber trajectory. The analysis predicted 114 positively linked target genes, including BFSP2, CRYBB1, CRYBA1, CRYBA4, CRYBB2, GATA3, TDRD7 and MAF itself, suggesting autoregulatory circuitry. FGF2 hyperstimulation accelerated MAF activation and increased intermediate/fiber-cell states.[217]

This is developmental model evidence, not molecular profiling of human Cataract 21 patients. Predicted regulatory links require functional validation.

### 6.6 Exact abstract evidence

> “The mutation results in the substitution of an evolutionarily highly conserved arginine with a proline at residue 288 (R288P) in the basic region of the DNA-binding domain of MAF.” — Jamieson et al., *Human Molecular Genetics*, 1 January 2002, PMID **11772997**.[58]

> “Dual luciferase activity assay shows the mutation significantly impair the transcriptional activity of four crystallin genes (CRYAA, CRYBA4, CRYBA1, and CRYGA) and two non-crystallin genes (HMOX1 and KDELR2).” — Si et al., 2019, PMID **30659945**.[409]

> “A 4-year-old patient with a history of bilateral nuclear and cortical cataracts was found to have a novel, likely pathogenic de novo variant in MAF, NM_005360.5:c.922A>G (p.Lys308Glu).” — Zhao et al., *Genes*, 25 May 2024, PMID **38927621**.[23]

---

## 7. Anatomical structures affected

| Level | Structure/cell/compartment | Ontology suggestion | Relevance |
|---|---|---|---|
| Organ | Eye | UBERON:0000970 | Affected system |
| Primary organ structure | Lens of camera-type eye | **UBERON:0000965** | Direct site of opacity |
| Secondary structure | Cornea | **UBERON:0000964** | Microcornea/corneal opacity |
| Secondary structure | Iris | **UBERON:0001769** | Coloboma |
| Secondary structure | Anterior chamber | **UBERON:0001766** | Anterior-segment dysgenesis/glaucoma context |
| Tissue | Lens epithelium | Lens epithelium ontology term | Progenitor/differentiating layer |
| Cell | Lens epithelial cell | **CL:0002224** | Upstream differentiation state |
| Cell | Secondary lens fiber | **CL:0002225** | Principal dysfunctional cell |
| Subcellular | Nucleus | **GO:0005634** | c-MAF localization/transcription |
| Subcellular | Transcription-regulator complex | **GO:0005667** | MAF homo-/heterodimer complexes |

Most reports describe **bilateral** disease, although severity may be asymmetric and unilateral total cataract occurred in the p.Tyr301His proband. Microcornea and iris coloboma can also vary between relatives.

---

## 8. Temporal development

### Onset and natural history

| Phase | Typical features |
|---|---|
| Prenatal lens development | Molecular lesion is present from conception; abnormal developmental transcription begins during lens-fiber differentiation |
| Congenital/neonatal | Dense nuclear, cortical or total cataract may be present and visually significant at birth |
| Infancy | Cerulean opacities may become slit-lamp visible around 18–24 months; untreated dense cataract begins causing amblyopia earlier |
| Childhood/juvenile | Pulverulent, lamellar or nuclear cataract may become symptomatic; progression is variable |
| Adolescence/adulthood | Some slowly progressive forms develop posterior subcapsular opacity and require extraction |
| Lifelong after surgery | Optical correction, amblyopia care in childhood and glaucoma surveillance are required |

In one R288P family, adult cataract extraction occurred at 25–29 years, while a 16-year-old relative retained only minor visual reduction. Conversely, the p.Lys308Glu child required bilateral surgery at seven and eight weeks.[60][23]

### Critical intervention window

The critical window is early visual development, not a molecular “remission” period. For dense bilateral cataracts, expert guidance generally favors surgery around **6–8 weeks**, while dense unilateral cataracts are commonly treated around **4–6 weeks**, balancing amblyopia against early-surgery complications.[164][172] Small, non-axis-obscuring cataracts may remain under observation.

No spontaneous molecular remission is established. Cataract may remain stable, progress slowly or progress rapidly depending on allele and morphology.

---

## 9. Inheritance and population

### 9.1 Inheritance

- **Pattern:** autosomal dominant.
- **Recurrence risk:** an affected heterozygous individual has a **50% probability per pregnancy** of transmitting the variant.
- **Sex ratio:** no expected sex bias.
- **Penetrance:** apparently high or complete in several large pedigrees, especially reported cerulean families, but a universal numerical estimate for all MAF variants is unavailable.
- **Expressivity:** markedly variable, including within families.
- **Anticipation:** not demonstrated.
- **Germline mosaicism:** not specifically reported; low residual recurrence risk remains in an apparently de novo case.
- **Founder effects:** none established.
- **Consanguinity:** not expected to be important for this dominant disorder.
- **Carrier frequency:** not established; “carrier” is not generally an asymptomatic recessive state because heterozygotes are at risk of disease.

### 9.2 Epidemiology

No disease-specific prevalence or incidence estimate exists for MAF-related Cataract 21. Cat-Map’s 2024 review counted approximately **29 MAF-associated cataract entries**, but this is a literature count, not a population denominator.[391]

For context only:

- Congenital cataract prevalence across studies ranges from **0.63–9.74 per 10,000 children**, median 1.71 per 10,000.[197]
- A meta-analysis estimated a pooled prevalence of **4.24 per 10,000**.[198]
- Childhood cataract incidence has been estimated at **1.8–3.6 per 10,000 children per year**.[203]

The fraction caused specifically by MAF is unknown and much smaller. Families have been reported in Europe, India, Japan, China and North America, without a proven ethnic or geographic concentration.

---

## 10. Diagnostics

### 10.1 Clinical evaluation

1. **Urgent pediatric ophthalmology examination** after leukocoria or an abnormal red reflex.
2. Assess visual behavior, fixation, ocular alignment and nystagmus.
3. Slit-lamp examination after dilation to document cataract morphology, density and laterality.
4. Measure corneal diameter, axial length and intraocular pressure; evaluate for microcornea, coloboma and anterior-segment dysgenesis.
5. Dilated fundus examination; use B-scan ultrasonography if the posterior segment is obscured.
6. Examine parents and other relatives, preferably after dilation.

An abnormal red reflex in a newborn requires urgent consultation. Current AAO/AAP guidance supports red-reflex testing in the newborn nursery and specialist examination for infants with a family history of childhood cataract.[299][307]

### 10.2 Molecular testing strategy

| Test | Recommended role |
|---|---|
| Multigene congenital/childhood cataract panel | Practical first-line test; should include MAF and deletion/duplication analysis |
| Trio testing | Important when a variant is initially a VUS; can establish de novo status |
| WES | Appropriate when a broad panel is negative or when syndromic disease is possible |
| WGS | Useful after negative panel/WES and for regulatory, repetitive-region or structural variants |
| MAF single-gene sequencing | Reasonable in a clearly segregating pulverulent/cerulean cataract with or without microcornea, but broad panels reduce the risk of choosing the wrong cataract gene |
| CMA | Low yield for isolated cataract but useful with developmental delay, multiple congenital anomalies or suspected copy-number disease |
| Karyotype/FISH | Not routine; consider if a balanced rearrangement like t(5;16) is suspected |
| mtDNA/repeat-expansion testing | Not indicated for this disease |
| RNA-seq/proteomics/metabolomics | Research only; no validated diagnostic signature |

In a diverse US pediatric cohort, WES and cataract panels produced diagnostic yields of **46.2% and 37.5%**, respectively, versus **11% for microarray**.[315] In another 52-proband cohort, genome sequencing yielded an overall diagnosis in **40/52 (77%)**, adding diagnoses in 5/52 through small CNVs, repetitive-region indels and GC-rich SNVs missed by prior methods.[313]

A dedicated postnatal MAF sequence test for OMIM 610202 is listed in the Genetic Testing Registry.[373]

### 10.3 Variant interpretation

Apply ACMG/AMP criteria with:

- phenotype specificity and segregation;
- confirmed de novo status;
- absence or extreme rarity in gnomAD;
- location in the constrained EHR/basic/leucine-zipper domain;
- published functional assays;
- avoidance of circular reliance on computational predictions;
- assessment for Aymé-Gripp features when the variant lies in the N-terminal phosphorylation region.

### 10.4 Differential diagnosis

| Differential | Distinguishing evaluation |
|---|---|
| Other AD cataracts: CRYAA, CRYBB2, CRYGD, GJA3, GJA8, MIP, HSF4, PITX3 | Multigene panel; morphology alone is insufficient |
| Aymé-Gripp syndrome | Hearing loss, seizures, developmental delay, short stature and characteristic face; usually N-terminal MAF variant |
| Galactosemia/galactokinase deficiency | Feeding/liver illness, reducing substances, galactose metabolites/enzyme testing |
| TORCH infection | Maternal history, systemic signs and targeted serology/PCR |
| Lowe syndrome | Male patient, hypotonia, renal Fanconi syndrome |
| Persistent fetal vasculature | Usually unilateral; retrolental tissue/microphthalmia on examination or ultrasound |
| Retinoblastoma | Leukocoria with retinal mass/calcification; urgent exclusion |
| Coats disease, toxocariasis, retinal detachment, ROP | Posterior-segment examination/imaging |
| Peters anomaly/PAX6-related disease | Primary corneal/anterior-segment abnormalities and relevant molecular testing |

Broad metabolic/TORCH testing is most appropriate for bilateral cataract without a convincing familial molecular diagnosis or when systemic history suggests it; indiscriminate testing has low yield.[328][338]

---

## 11. Outcome and prognosis

### Survival and mortality

Cataract 21 is not known to reduce life expectancy or cause disease-specific mortality. Survival statistics therefore are not applicable.

### Visual prognosis

Prognosis depends primarily on:

- cataract density and centrality;
- unilateral versus bilateral deprivation;
- age at onset and surgery;
- presence of microcornea, microphthalmia or anterior-segment dysgenesis;
- prompt optical correction;
- adherence to amblyopia therapy;
- postoperative glaucoma or visual-axis opacification.

Untreated dense early cataract can cause irreversible amblyopia, nystagmus and permanent visual impairment.[524] Early surgery improves the probability of useful vision but does not guarantee normal acuity, particularly after unilateral deprivation.

### Complications

- deprivation or anisometropic amblyopia;
- strabismus and nystagmus;
- aphakia/refractive error;
- posterior capsule opacification or capsular phimosis;
- glaucoma following cataract surgery;
- retinal detachment, inflammation or endophthalmitis—less common surgical risks.

In a 37-year longitudinal congenital-cataract cohort, glaucoma prevalence was **14.8%** after a mean 23.2 years; microphthalmos conferred a relative risk of 7.75, supporting lifelong follow-up.[189] In the Infant Aphakia Treatment Study, glaucoma risk after infant cataract surgery rose to **22% at ten years**, and glaucoma plus glaucoma-suspect status to 40%; this trial involved unilateral congenital cataract and is not MAF-specific.[178]

---

## 12. Treatment

There is no approved MAF-directed drug, RNA therapy, gene therapy or cell therapy. Management addresses optical obstruction and its developmental consequences.

| Intervention | Indication/implementation | Important outcomes/risks | Suggested NCIt concept |
|---|---|---|---|
| Observation | Small, peripheral/paracentral, nonprogressive opacity with good red reflex and age-appropriate vision | Requires frequent monitoring for progression/amblyopia | Observation |
| Pharmacologic pupil dilation | Selected partial cataracts allowing vision through a clear lens area | Not cataract-clearing therapy; cycloplegia may worsen blur | Pharmacologic dilation |
| Lensectomy/cataract aspiration | Visually significant central/dense cataract | Restores optical axis; risks inflammation, glaucoma and visual-axis opacity | Cataract extraction; lensectomy |
| Posterior capsulotomy and anterior vitrectomy | Common in young children to reduce secondary visual-axis opacity | Additional surgical risks | Posterior capsulotomy; anterior vitrectomy |
| Aphakic contact lens or spectacles | Immediate correction when no primary IOL is implanted | Fit changes with growth; adherence essential | Contact lens; corrective lens |
| Intraocular lens implantation | Primary or delayed, individualized by age, anatomy and surgeon | Residual refractive error; complications and reoperations possible | Intraocular lens implantation |
| Occlusion/patching | Unilateral or asymmetric amblyopia | Adherence determines benefit; excessive patching can impair the better eye | Occlusion therapy |
| Strabismus surgery | Persistent functionally/cosmetically significant deviation | Does not replace amblyopia treatment | Strabismus surgery |
| Glaucoma medication/surgery | Postoperative ocular hypertension/glaucoma | Lifelong monitoring often required | Glaucoma therapy |
| Low-vision/educational support | Residual visual disability | Supports learning, mobility and independence | Low-vision rehabilitation |
| Genetic counseling | All molecularly confirmed patients/families | Recurrence and reproductive planning | Genetic counseling |

For infants under approximately one year, a common procedure is lensectomy with primary posterior capsulotomy and anterior vitrectomy, followed by aphakic optical correction and amblyopia management.[343] The 2024 p.Lys308Glu case provides a real-world implementation: surgery at seven/eight weeks, aphakic contact lenses, capsulectomies for phimosis, topical glaucoma therapy, patching and later strabismus surgery.[23]

No ClinicalTrials.gov study specifically targeting MAF-related Cataract 21 was identified. Current pediatric cataract trials primarily concern surgical technique, postoperative inflammation or optical rehabilitation, not correction of MAF transcriptional dysfunction.

---

## 13. Prevention

### Primary prevention

The occurrence of a de novo MAF variant cannot currently be prevented by lifestyle measures. For a known familial variant, reproductive options include:

- preconception genetic counseling;
- preimplantation genetic testing for monogenic disease;
- prenatal targeted testing by chorionic-villus sampling or amniocentesis;
- donor gametes or other family-planning options.

These tests predict inheritance more reliably than eventual severity because expressivity is variable.

### Secondary prevention

- Newborn and routine infant red-reflex examination.
- Immediate ophthalmology referral for leukocoria, abnormal/asymmetric red reflex or positive family history.
- Cascade testing and ophthalmic examination of first-degree relatives.
- Early surgery or close observation according to visual significance.
- Immediate postoperative optical correction and amblyopia therapy.

### Tertiary prevention

- Frequent refraction and replacement of contact lenses/spectacles.
- Monitoring for visual-axis opacification, strabismus and amblyopia.
- Lifelong intraocular-pressure and optic-nerve surveillance after surgery.
- Low-vision and educational accommodations where needed.

Rubella vaccination and appropriate antenatal infection prevention reduce non-genetic congenital cataract burden, but they do not prevent MAF-related Cataract 21.

---

## 14. Other species and natural disease

| Species | Taxonomy/gene | Natural MAF disease evidence | Comparative relevance |
|---|---|---|---|
| Human, *Homo sapiens* | NCBI Taxon **9606**; MAF Gene **4094** | Target disease | Germline C-terminal variants produce dominant cataract |
| Mouse, *Mus musculus* | Taxon **10090**; Maf Gene **17132**, MGI:96909 | Naturally/spontaneously detected Ofl allele and induced alleles cause cataract | Strong mechanistic homology |
| Zebrafish, *Danio rerio* | Taxon **7955**; duplicated human-MAF orthologs include **mafa** | No validated natural MAF-equivalent Cataract 21 identified | Lens expression and tractable developmental model |
| Domestic animals | Multiple species develop inherited cataracts | No well-established naturally occurring MAF ortholog variant equivalent to human Cataract 21 located in OMIA | Generic animal cataracts should not be labeled MAF-related |

OMIA documents cataracts in many companion, livestock and wildlife species but does not establish a breed-specific natural MAF Cataract 21 counterpart.[269] Consequently, no VBO breed annotation is presently justified. The condition has no zoonotic or cross-species transmission potential.

---

## 15. Model organisms and experimental systems

| Model | Genotype/system | Recapitulated findings | Mechanistic use and limitation |
|---|---|---|---|
| Maf-null mouse | Homozygous targeted knockout | Failed posterior lens-fiber elongation, severe defective lens formation, microphthalmia and reduced crystallins | Demonstrates MAF necessity; more severe than human heterozygous Cataract 21 |
| Ofl mouse | **Maf p.Arg291Gln**, heterozygous/homozygous | Mild pulverulent “opaque flecks” in heterozygotes; severe fiber-differentiation defects in homozygotes; anterior-segment phenotype depends on background | Closely models dominant DNA-binding-domain disease and genetic-background effects; PMID **12620964**[284][289] |
| ENU424 mouse | **Maf p.Asp90Val** | Mild granular nuclear opacity in heterozygotes, denser cataract in homozygotes | Models gain-of-transactivation cataract; N-terminal mechanism differs from most human CTRCT21 |
| Reporter cell systems | COS-1, HLECB3, HEK293T with crystallin-promoter luciferase constructs | Quantifies variant-specific transcriptional activation | Does not reproduce lens architecture, development or optical transparency |
| Embryonic chicken lens multi-omics | snRNA-seq, snATAC-seq, CUT&RUN, FGF2 perturbation | Defines epithelial, intermediate and fiber states; maps MAF-associated chromatin accessibility and candidate targets | High-resolution developmental network, but nonhuman and largely computational |
| Zebrafish | Lens-expression and promoter/transgenic systems | MAF ortholog expression and crystallin-promoter regulation can be studied | No validated endogenous MAF Cataract 21 knock-in model currently established |
| Patient-derived iPSC/lens organoid | No established disease-standard model found | Potential future system for allele-specific developmental and therapeutic studies | Not yet validated for CTRCT21 |

The Ofl model is particularly informative because heterozygous Maf knockout mice lack cataract, while heterozygous p.Arg291Gln mice develop disease. That contrast argues against simple haploinsufficiency and supports a dominant altered-function mechanism for at least some DNA-binding-domain variants.[284]

---

## Overall evidence assessment

**High-confidence conclusions**

- The disease is caused by heterozygous germline **MAF** alterations and is usually autosomal dominant.
- C-terminal DNA-binding/bZIP variants are strongly associated with nonsyndromic cataract, often with variable microcornea or iris coloboma.
- c-MAF is required for lens-fiber differentiation and transcriptional control of crystallin and other lens-homeostasis genes.
- Early optical treatment is essential to prevent irreversible amblyopia.

**Important uncertainties**

- Disease-specific prevalence, penetrance across all alleles, modifier genes and variant-specific prognosis remain unknown.
- Functional consequence is not uniform: loss of activation, altered target selectivity and gain of activation have all been observed.
- No patient-derived transcriptomic, proteomic, metabolomic or epigenomic biomarker is clinically validated.
- No MAF-directed preventive or molecular therapy is currently available.

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 20 |
| Resolved | 20 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 20 |
| On topic | 16 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 38 |
| Resolved | 34 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 4 |
| Terms whose name was checked | 19 |
| Terms named correctly | 9 |
| Terms named as a **different** term | 10 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0012437` (2 mentions) - the report calls it "MONDO"; MONDO calls it **cataract 21 multiple types**
- `DOID:0110256` (2 mentions) - the report calls it "Disease Ontology"; DOID calls it **cataract 21 multiple types**
- `HP:0007780` (1 mention) - the report calls it "Gradual acuity loss; surgery at 25–29 years in one pedigree"; HP calls it **Cortical pulverulent cataract**
- `HP:0007976` (1 mention) - the report calls it "Reading/distance difficulty develops gradually; extraction may occur in adolescence or adulthood"; HP calls it **Cerulean cataract**
- `HP:0100018` (1 mention) - the report calls it "High amblyopia risk if central and untreated"; HP calls it **Nuclear cataract**
- `HP:0001134` (1 mention) - the report calls it "May be observed if not visually significant"; HP calls it **Anterior polar cataract**
- `HP:0000482` (1 mention) - the report calls it "Complicates surgery and may influence refractive outcome"; HP calls it **Microcornea**
- `HP:0000612` (1 mention) - the report calls it "Glare, photophobia or additional acuity impairment"; HP calls it **Iris coloboma**
- `HP:0000568` (1 mention) - the report calls it "Poorer visual prognosis; glaucoma risk after surgery"; HP calls it **Microphthalmia**
- `HP:0000639` (1 mention) - the report calls it "Marker of poorer visual prognosis"; HP calls it **Nystagmus**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `MGI`.