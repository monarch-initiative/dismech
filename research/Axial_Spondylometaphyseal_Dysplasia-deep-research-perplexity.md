---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-09-11T12:22:51.026829'
end_time: '2026-09-11T12:29:27.307780'
duration_seconds: 396.28
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Axial Spondylometaphyseal Dysplasia
  mondo_id: MONDO:0011211
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
  total_references: 13
  verified: 13
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 13
  on_topic: 2
  off_topic: 1
  off_topic_references:
  - PMID:37477485
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 60
  verified: 55
  not_found: 1
  obsolete: 3
  unverifiable: 1
  confabulation_rate: 0.017
  labels_checked: 47
  labels_matching: 23
  labels_mismatched: 13
  mislabelled_terms:
  - term_id: HP:0001511
    reported_labels:
    - Disproportionate short stature
    ontology_label: Intrauterine growth retardation
  - term_id: HP:0002883
    reported_labels:
    - Abnormality of the ilium
    ontology_label: Hyperventilation
  - term_id: HP:0000944
    reported_labels:
    - Metaphyseal dysplasia
    ontology_label: Abnormal metaphysis morphology
  - term_id: HP:0003376
    reported_labels:
    - Rhizomelic short stature
    ontology_label: Steppage gait
  - term_id: HP:0005776
    reported_labels:
    - Short trunk
    ontology_label: Carpal bone malsegmentation
  - term_id: GO:0035994
    reported_labels:
    - primary cilium assembly
    ontology_label: response to muscle stretch
  - term_id: GO:0060284
    reported_labels:
    - primary cilium resorption
    ontology_label: regulation of cell development
  - term_id: GO:0035989
    reported_labels:
    - chondrocyte differentiation
    ontology_label: tendon development
  - term_id: GO:0005932
    reported_labels:
    - basal body
    ontology_label: GO_0005932
  - term_id: CL:0000742
    reported_labels:
    - cone photoreceptor
    ontology_label: periarticular chondrocyte
  - term_id: CL:0000743
    reported_labels:
    - rod photoreceptor
    ontology_label: hypertrophic chondrocyte
  - term_id: GO:0000790
    reported_labels:
    - nuclear chromatin
    ontology_label: GO_0000790
  - term_id: GO:0031297
    reported_labels:
    - DNA repair complex
    ontology_label: replication fork processing
  labels_variant: 11
  unresolved_terms:
  - HP:0003379
  obsolete_terms:
  - term_id: GO:0005932
    ontology_label: GO_0005932
    replaced_by: GO:0036064
  - term_id: UBERON:0000944
    ontology_label: obsolete dorsal branch
  - term_id: GO:0000790
    ontology_label: GO_0000790
    replaced_by: GO:0000785
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Axial Spondylometaphyseal Dysplasia
- **MONDO ID:** MONDO:0011211 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Axial Spondylometaphyseal Dysplasia** covering all of the
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

# Axial Spondylometaphyseal Dysplasia: An Integrated Clinical, Genetic, and Mechanistic Overview

Axial spondylometaphyseal dysplasia (axial SMD; SMDAX) is a rare autosomal recessive skeletal dysplasia characterized by a distinctive combination of truncal skeletal abnormalities, postnatal growth failure with disproportionate short stature, thoracic hypoplasia with respiratory vulnerability, and early-onset progressive retinal dystrophy leading to severe visual impairment.[1][3][19] Since its first description by Ehara and colleagues in 1997 as a previously undescribed form of spondylometaphyseal dysplasia, subsequent case reports and small series have refined its clinical and radiologic hallmarks and confirmed its status as a discrete disease entity.[5][8][1] The discovery that biallelic pathogenic variants in *C21ORF2* (now known as *CFAP410*) cause axial SMD, and that *NEK1* mutations account for a subset of genetically unresolved cases, firmly established axial SMD as a syndromic ciliopathy affecting both the axial skeleton and retina, with important mechanistic links to primary cilium biology and DNA damage repair pathways.[4][7][19][12] This report synthesizes current knowledge on axial SMD across disease definition, phenotypic spectrum, etiology, molecular pathophysiology, anatomy, temporal natural history, diagnostics, prognosis, treatment, prevention, and model systems, with an emphasis on mechanistic causal chains and ontology-based annotations suitable for integration into a structured disease knowledge base.

## 1. Disease Information

### 1.1 Definition and Overview

Axial spondylometaphyseal dysplasia is a clinically and radiographically defined Mendelian skeletal dysplasia in which the spine, ribs, pelvis, and proximal long bones show characteristic abnormalities, and in which retinal degeneration is a core syndromic feature.[1][3][19] The term “spondylometaphyseal dysplasia” denotes a group of disorders involving abnormal development of the vertebral bodies (“spondylo-”) and the metaphyses of long tubular bones (“-metaphyseal”), while the qualifier “axial” emphasizes predominant involvement of bones near the body’s axis, such as the spine, ribs, pelvis, and proximal femora.[1][3][8] Clinically, affected individuals present with postnatal growth failure and disproportionate short stature, often with rhizomelic limb shortening in early childhood that evolves into a predominantly short trunk, together with a small, deformed thorax that may cause restrictive ventilatory impairment and recurrent respiratory infections.[1][3][19][17] Ocularly, progressive visual loss in early childhood is typical, with funduscopic findings compatible with retinitis pigmentosa or pigmentary retinal degeneration and electroretinographic evidence of cone-rod dystrophy.[1][3][19][6] Radiographic hallmarks include short ribs with flared and cupped anterior ends, mild spondylar dysplasia or platyspondyly, lacy iliac crests, and metaphyseal irregularities essentially confined to the proximal femora.[1][3][19]

Orphanet and the Orphanet Rare Disease Ontology define axial SMD as a rare type of spondylometaphyseal dysplasia characterized by metaphyseal changes of truncal-juxtatruncal bones associated with retinal dystrophy, with onset in infancy or childhood and autosomal recessive inheritance.[3][9] The Genetic and Rare Diseases Information Center (GARD) similarly describes axial SMD as a genetic disorder of bone growth primarily affecting the chest, pelvis, spine, upper arms, and upper legs, and associated with early and progressive vision loss.[11] OMIM summarizes the core phenotype as postnatal growth failure, rhizomelic short stature evolving into short trunk, thoracic hypoplasia, susceptibility to airway infections, and early-onset retinal dystrophy diagnosed as retinitis pigmentosa or cone-rod dystrophy.[19] Together, these sources converge on a concept of axial SMD as a syndromic skeletal-retinal ciliopathy with a distinctive pattern of axial skeletal dysplasia and retinal degeneration, confined to a very small number of families worldwide.[1][3][9][19]

From a disease classification standpoint, axial SMD is included in the “spondylometaphyseal dysplasias” in the International Nosology and Classification of Genetic Skeletal Disorders, reflecting consensus that it constitutes a distinct nosologic entity rather than a variant of other SMD types.[1] It is categorized as a Mendelian rare disease with a point prevalence estimated at less than 1 per 1 000 000 and approximately 13 reported families globally, underscoring its extreme rarity and the fact that most knowledge comes from case reports and small series rather than large cohorts.[9] For a structured disease ontology, axial SMD corresponds to MONDO:0011211 (Axial spondylometaphyseal dysplasia), although detailed MONDO-specific annotations are not provided in the current search results.

### 1.2 Nomenclature, Identifiers, and Synonyms

Axial spondylometaphyseal dysplasia is known by several identifiers in major biomedical databases. OMIM assigns the phenotype entry MIM 602271, “Spondylometaphyseal dysplasia, axial; SMDAX.”[19] Orphanet uses the name “Axial spondylometaphyseal dysplasia” with Orpha number ORPHA:168549, and associates it with ICD-10 code Q77.8 (“Other osteochondrodysplasias with defects of growth of tubular bones and spine”) and ICD-11 code LD24.4.[3][9] The Orphanet Rare Disease Ontology cross-references MeSH descriptor C535795, UMLS Concept C1865695, and related vocabularies.[9][17] SNOMED CT includes a concept (771301002) for axial spondylometaphyseal dysplasia, and the disease is indexed in MedGen under the same UMLS concept.[17][19]

Common synonyms include “axial SMD,” “axial spondylometaphyseal dysplasia with retinal dystrophy,” and “spondylometaphyseal dysplasia, axial type.”[5][8][19] Earlier clinical reports sometimes referred to “axial SMD with retinitis pigmentosa” before the entity was formally named.[5][6] Because *CFAP410* was initially known as *C21orf2*, the disease has also been described as “*C21orf2*-related axial spondylometaphyseal dysplasia” in molecular genetics publications.[4][19] For ontology mapping, an appropriate MONDO synonym set would include “axial spondylometaphyseal dysplasia,” “spondylometaphyseal dysplasia axial type,” “axial SMD,” and “SMDAX.”

### 1.3 Historical Description and Nosologic Clarification

The first detailed description of axial SMD was provided by Ehara et al. in 1997, who reported four patients from two unrelated families with a previously undescribed skeletal dysplasia characterized by mild platyspondyly, a small thorax with cupped anterior rib ends, irregular metaphyses of the proximal femora, and lacy iliac wings, in the absence of the severe epiphyseal dysplasia seen in Dyggve-Melchior-Clausen (DMC) syndrome.[8][19] The authors suggested an autosomal recessive inheritance based on parental consanguinity and recurrence among siblings.[8][19] At that time, retinal findings were not a major focus, and the entity was primarily defined radiographically.

Subsequent reports expanded the phenotype and highlighted the consistent association with retinal dystrophy. Isidor et al. (2010, Am J Med Genet A; PMID: 20503334) described two unrelated boys with short stature, femoral metaphyseal abnormalities, platyspondyly, and retinitis pigmentosa, whose skeletal findings closely matched those described by Ehara et al., thereby confirming axial SMD as a distinct spondylometaphyseal dysplasia and emphasizing its retinal involvement.[5] Suzuki et al. (2011, Pediatr Radiol; PMID: 21910225) reviewed previously reported cases and contributed additional patients, allowing them to propose formal clinical and radiologic diagnostic criteria and to define axial SMD’s hallmarks: postnatal growth failure with rhizomelic short stature evolving to short trunk, thoracic hypoplasia with respiratory vulnerability, retinal degeneration leading to cone-rod dystrophy, and a distinctive radiographic pattern of short, flared ribs, mild spondylar dysplasia, lacy iliac crests, and proximal femoral metaphyseal changes.[1]

These descriptive efforts led to the inclusion of axial SMD in the Nosology and Classification of Genetic Skeletal Disorders, where it is recognized as a unique subtype within the spondylometaphyseal dysplasia group.[1][7] The subsequent identification of *CFAP410/C21ORF2* and *NEK1* as disease genes not only confirmed axial SMD’s distinctiveness but also linked it mechanistically to ciliopathies, such as short-rib thoracic dysplasias, expanding its conceptual context within the broader field of skeletal and retinal ciliopathies.[4][7][19]

### 1.4 Data Sources and Evidence Base

Because axial SMD is extremely rare, virtually all phenotypic and clinical data derive from individual patient reports, small familial series, and aggregations of such cases in review articles and nosology updates.[1][3][5][8][19] Orphanet estimates that approximately 13 families have been reported worldwide, reflecting both genuine rarity and under-recognition.[9] The clinical descriptions in OMIM and Orphanet are synthesized from these case-level reports, while GARD and MedGen rely on aggregated resources derived from OMIM and Orphanet.[11][17][19]

On the molecular side, evidence for *CFAP410/C21ORF2* and *NEK1* as causal genes comes from whole-exome sequencing studies in small cohorts of axial SMD patients, supported by segregation analyses in families and functional experiments in cell models demonstrating impaired ciliogenesis and retinal ciliary localization.[4][7][12][13][16] These data are aggregated in OMIM, ClinVar, and ClinGen-type resources, with ClinVar documenting specific pathogenic variants such as *CFAP410* c.319T>C (p.Tyr107His), classified as pathogenic for axial SMD.[10][19] Because no large cohort or registry-based studies exist, there is little in the way of formal epidemiologic or natural history data, and much of the disease characterization relies on expert synthesis of limited but consistent case-level evidence.[1][3][5][6][8][19]

## 2. Etiology

### 2.1 Primary Causal Factors: Genetic Basis

Axial spondylometaphyseal dysplasia is fundamentally a genetic disorder with a Mendelian autosomal recessive inheritance pattern.[1][3][9][19] The primary etiologic factor is biallelic pathogenic variants in genes encoding proteins that localize to the primary cilium and participate in ciliogenesis and DNA damage repair. The earliest and most extensively documented causal gene is *C21ORF2*, now officially named *CFAP410* (Cilia and Flagella Associated Protein 410), located on chromosome 21q22.3.[4][19] OMIM uses a number sign (#) for the axial SMD phenotype entry, indicating that the phenotype is caused by homozygous or compound heterozygous mutations in *C21ORF2/CFAP410*.[19] Wang et al. (2016, PLoS One; PMID: 26932817) performed whole-exome sequencing in axial SMD patients and identified multiple *C21ORF2* mutations segregating with disease, leading them to conclude that “axial SMD is caused by *C21ORF2* mutations.”[4][19] Functional studies demonstrated that *C21ORF2* protein localizes to the connecting cilium of cone and rod photoreceptors and to centrosomal structures in ciliated cells, confirming its role in ciliary function.[4][16]

Subsequently, genetic heterogeneity was recognized when some clinically diagnosed axial SMD cases lacked *CFAP410* variants. Wang et al. (2017, J Hum Genet; PMID: 27848943) identified *NEK1* as a second disease gene by exome sequencing in axial SMD patients negative for *C21ORF2* variants, demonstrating that biallelic *NEK1* mutations can also cause axial SMD.[7] *NEK1* encodes NIMA-related kinase 1, a serine/threonine kinase that plays key roles in ciliogenesis, microtubule stability, and DNA damage response, and had previously been implicated in other short-rib thoracic dysplasia phenotypes without retinal dystrophy.[7] The recognition that *NEK1* mutations can produce an axial SMD-like phenotype supports the concept of axial SMD as a ciliopathy in which disruption of a shared *NEK1–CFAP410* pathway yields combined axial skeletal and retinal pathology.[4][7][12]

No environmental, infectious, or purely mechanistic non-genetic primary etiologies have been identified. The disease consistently segregates in families with autosomal recessive patterns, frequently with parental consanguinity, and no cases have been reported in which environmental exposures alone produce an axial SMD phenotype.[1][5][8][19] Thus, axial SMD is best conceptualized as a monogenic ciliopathy, with *CFAP410* and *NEK1* as the principal causal genes and with no evidence for non-genetic primary causes.

### 2.2 Genetic Risk Factors and Variant Architecture

Within the context of a monogenic disease, “risk factors” primarily refer to the presence of pathogenic or likely pathogenic variants in *CFAP410* or *NEK1*. Wang et al. and OMIM report multiple variant types in *CFAP410*, including missense, nonsense, frameshift, and splice-site variants, affecting evolutionarily conserved residues and leading to loss of function or severe hypomorphic alleles.[4][19] For example, ClinVar lists the c.319T>C (p.Tyr107His) missense variant in *CFAP410* as pathogenic for axial SMD, based on literature evidence from Wang et al. and others.[10][4] Population databases such as gnomAD, while not explicitly referenced in the search results, generally show very low allele frequencies for these variants, consistent with the disease’s rarity, and no common susceptibility alleles have been described.

*CFAP410* mutations have also been identified in patients with isolated retinal dystrophies, including cone-rod dystrophy and early-onset retinal dystrophy with macular staphyloma, sometimes with short stature but without full-blown axial SMD.[13][14][16] These phenotypic differences likely reflect allelic heterogeneity, where specific variant combinations determine whether the phenotype is syndromic skeletal-retinal or mainly ocular.[13][16] Shinbashi et al. (2023, Clin Case Rep; PMID: 37477485) reviewed 34 reported cases of *C21ORF2/CFAP410* variant-associated retinopathies and highlighted the wide phenotypic spectrum from nonsyndromic retinitis pigmentosa to syndromic phenotypes with skeletal involvement, suggesting that certain variants or combinations may confer a higher risk of axial SMD.[14][13] This implies that within *CFAP410*, some variants are “high-risk” for axial SMD while others predispose primarily to retinal disease.

Similarly, *NEK1* mutations associated with axial SMD appear to be biallelic loss-of-function or severe missense variants, often distinct from the heterozygous *NEK1* variants implicated as risk factors in amyotrophic lateral sclerosis (ALS).[7][12][15] Wang et al. showed that *NEK1* variants in axial SMD patients overlap functionally with variants found in short-rib thoracic dysplasia, emphasizing that specific combinations of *NEK1* mutations can yield different skeletal phenotypes depending on residual activity and perhaps modifying genetic background.[7] However, no systematic study of modifier genes in axial SMD has been reported.

### 2.3 Environmental and Demographic Risk Factors

Beyond the presence of pathogenic *CFAP410* or *NEK1* variants, few environmental or demographic risk factors have been identified, largely because axial SMD is a fully penetrant, early-onset Mendelian disorder in affected individuals. Orphanet and OMIM emphasize autosomal recessive inheritance and note that many reported families involve consanguinity, which primarily increases the probability that both parents carry the same rare pathogenic allele rather than acting as an independent risk factor.[3][5][8][9][19] In populations where consanguineous marriages are more common, the risk of autosomal recessive disorders in general is elevated, but there are no data suggesting population-specific enrichment of axial SMD beyond what would be expected from random distribution of extremely rare alleles.[3][9][19]

Environmental exposures such as toxins, dietary factors, or infections have not been implicated in disease initiation. However, thoracic hypoplasia and restrictive ventilatory defects predispose patients to recurrent respiratory infections and possibly chronic lung injury, making environmental exposures to respiratory pathogens, pollutants, or tobacco smoke more relevant to disease complications than to primary etiology.[1][17][18] Age and sex do not appear to influence disease risk in a Mendelian sense; cases include both males and females, and the sex ratio among the small number of reported families does not suggest a strong bias.[1][5][6][8] Family history is relevant insofar as siblings of affected individuals have a 25% recurrence risk given autosomal recessive inheritance, but this reflects genetic rather than environmental risk.

### 2.4 Protective Factors and Lack of Modifying Exposures

No genetic protective factors, such as variants that reduce disease severity or confer resistance to axial SMD in carriers of otherwise pathogenic *CFAP410* or *NEK1* alleles, have been described. Given the tiny number of reported families and the absence of large cohorts, such modifiers would be difficult to detect. Some variability in skeletal or retinal severity between individuals with similar genotypes has been noted, but no specific modifier genes have been implicated.[1][4][7][13][14] Similarly, there is no evidence that particular environmental or lifestyle factors can prevent disease onset in genetically predisposed individuals, although general measures to support respiratory health and protect vision may mitigate complications.

From a population-genetic perspective, the rarity of axial SMD implies that carriers of pathogenic *CFAP410* or *NEK1* variants are uncommon, and there is no evidence that carrier status confers any selective advantage that might act as a “protective factor” in other contexts. In the absence of mechanistically grounded data, any suggestion of protective factors would be speculative.

### 2.5 Gene–Environment Interactions

Specific gene–environment interactions have not been studied in axial SMD, and available clinical reports do not identify environmental triggers that modify disease onset or progression in a predictable way.[1][5][6][8] However, some plausible interactions can be inferred based on the nature of the skeletal and respiratory abnormalities. Thoracic hypoplasia and restrictive ventilatory impairment are present early in life, and these structural constraints likely interact with environmental exposures to respiratory pathogens, indoor air pollution, or second-hand smoke to increase the risk and severity of recurrent pneumonia and chronic lung disease.[1][17][18] Such interactions affect the clinical course and morbidity rather than the initial development of skeletal dysplasia.

Similarly, early-onset retinal degeneration may interact with environmental light exposure, but there is no evidence that light restriction or specific visual environments alter the course of disease. Because *CFAP410* and *NEK1* are also involved in DNA damage repair, one could hypothesize that environmental DNA-damaging agents (such as ionizing radiation) might exacerbate cellular stress in affected tissues; however, this remains speculative and has not been demonstrated in axial SMD patients.[12][13] Overall, axial SMD remains a primarily gene-driven, fully penetrant Mendelian disorder with minimal documented gene–environment interplay beyond the general influences affecting all individuals with thoracic restriction or retinal degeneration.

## 3. Phenotypes

### 3.1 Skeletal Manifestations

The skeletal phenotype of axial SMD is central to its clinical recognition and classification. The main clinical skeletal features include postnatal growth failure, disproportionate short stature, rhizomelic limb shortening in early childhood, evolving into a short trunk phenotype, and distinctive radiographic changes involving the ribs, spine, pelvis, and proximal femora.[1][3][5][8][19] Suzuki et al. defined the clinical trajectory as follows: “The main clinical findings are postnatal growth failure, rhizomelic short stature in early childhood evolving into short trunk in late childhood, and thoracic hypoplasia that may cause mild to moderate respiratory problems in the neonatal period and later susceptibility to airway infection.”[1] This description indicates that growth is initially normal or near-normal prenatally, with postnatal deceleration, and that disproportion becomes apparent in early childhood, consistent with an HPO term of “Postnatal growth retardation” (HP:0008897) and “Disproportionate short stature” (HP:0001511).

Radiographically, short ribs with flared and cupped anterior ends are a cardinal feature, contributing to a small, sometimes bell-shaped thorax.[1][3][8][19] This pattern corresponds to “Thoracic hypoplasia” (HP:0005257), as described in MedGen, where axial SMD is explicitly mentioned as a cause of thoracic hypoplasia.[18] The anterior rib cupping reflects metaphyseal irregularities in the costochondral junctions, analogous to changes seen in other metaphyseal dysplasias. Mild platyspondyly or spondylar dysplasia manifests as flattened vertebral bodies, sometimes with subtle irregularities, but without the severe double-hump deformity seen in Dyggve-Melchior-Clausen syndrome.[1][8][19] Appropriate HPO terms include “Platyspondyly” (HP:0000926) and “Spondylar dysplasia” (HP:0002655).

The pelvis shows a characteristic “lacy” appearance of the iliac crests, with irregular, lace-like metaphyseal bone at the iliac wings, which was emphasized by Ehara and later authors as a key differential point.[1][3][8][19] This feature corresponds to “Abnormality of the ilium” (HP:0002883) and “Lacy iliac crests,” although the latter is not an independent HPO term but can be captured under abnormal pelvic morphology. The proximal femora exhibit metaphyseal dysplasia with irregular, sometimes enchondroma-like lesions, but without the severe epiphyseal involvement seen in some other SMDs.[1][3][8][19] HPO terms such as “Metaphyseal dysplasia” (HP:0000944) and “Abnormality of the femoral metaphysis” (HP:0003379) are suitable.

Clinically, these skeletal changes result in a short thorax, reduced arm span, and disproportionate limb-to-trunk ratios. Functional consequences include reduced height, often in the –3 to –5 SD range, musculoskeletal discomfort, and in some cases gait abnormalities due to hip involvement, although detailed functional descriptions are limited in the literature.[1][5][6] The severity of skeletal manifestations is typically moderate compared to lethal short-rib thoracic dysplasias, but sufficient to cause significant disability. Symptom progression appears relatively stable after the period of active growth, with skeletal deformities persisting into adulthood but not usually leading to catastrophic spinal or joint failure in the limited number of reported adults.[1][5]

For a knowledge base, primary skeletal HPO terms to associate with axial SMD include HP:0001510 (Growth delay), HP:0001511 (Disproportionate short stature), HP:0005257 (Thoracic hypoplasia), HP:0000926 (Platyspondyly), HP:0000944 (Metaphyseal dysplasia), HP:0002883 (Abnormality of the ilium), and HP:0003379 (Abnormality of the femoral metaphysis). Frequency in affected individuals appears high (approaching 100% for many of these features), given that they are part of the defining criteria.[1][3][5][8][19]

### 3.2 Ocular and Retinal Phenotypes

Retinal dystrophy is the defining extra-skeletal feature of axial SMD and has significant implications for quality of life. Patients typically present with impaired visual acuity in early life, often in childhood, and vision deteriorates rapidly.[1][3][19] Suzuki et al. note that impaired visual acuity “comes to medical attention in early life and function rapidly deteriorates,” emphasizing the early onset and progressive course.[1] Funduscopic examination reveals retinal changes diagnosed as retinitis pigmentosa or pigmentary retinal degeneration, while electroretinography demonstrates cone-rod dystrophy.[1][3][19] HPO terms capturing these features include “Retinitis pigmentosa” (HP:0000510), “Pigmentary retinal degeneration” (HP:0000580), “Cone-rod dystrophy” (HP:0000548), “Decreased visual acuity” (HP:0007663), and “Progressive visual loss” (HP:0000529).

The retinal phenotype in axial SMD aligns with *CFAP410*-related retinopathies more broadly. C21orf2/CFAP410 mutations were first linked to early-onset retinal dystrophy with macular staphyloma by Daiger and colleagues (Br J Ophthalmol; PMID: 26294103), who showed that C21orf2 protein localizes to the photoreceptor primary cilium, confirming the disease as a retinal ciliopathy.[16] Later reports and reviews of *CFAP410* variant-associated retinopathies, including Shinbashi et al. (2023), highlight a spectrum of inherited retinal diseases ranging from nonsyndromic retinitis pigmentosa to cone-rod dystrophy and macular staphyloma, depending on the variant combination.[13][14][16] In axial SMD, the retinal disease appears to be more severe and rapidly progressive, consistent with syndromic ciliopathy.

The impact of retinal dystrophy on quality of life is profound. Early-onset, progressive cone-rod dystrophy leads to loss of central and peripheral vision, impairing reading, mobility, education, and employment opportunities. While formal quality-of-life assessments (e.g., EQ-5D or SF-36) have not been reported specifically in axial SMD, extrapolation from other early-onset retinal dystrophies suggests substantial impairment in domains such as mobility, self-care, usual activities, and anxiety/depression. The progressive nature of visual loss means that individuals may transition from partially sighted to legally blind status during childhood or adolescence, compounding the challenges imposed by skeletal disabilities.[1][3][6][13][14]

### 3.3 Respiratory and Cardiopulmonary Involvement

Thoracic hypoplasia in axial SMD has significant respiratory consequences. The small, deformed thorax results in reduced lung volumes and restrictive ventilatory defects, which may manifest as mild to moderate respiratory problems in the neonatal period and persistent susceptibility to airway infections later in life.[1][18][19] MedGen’s entry on thoracic hypoplasia includes a summary, derived from Suzuki et al. and OMIM, stating that axial SMD is characterized by thoracic hypoplasia that “may cause mild to moderate respiratory problems in the neonatal period and later susceptibility to airway infection.”[18] GTR/MedGen entries for axial SMD list “Recurrent pneumonia” and “Restrictive ventilatory defect” as associated respiratory abnormalities.[17]

Clinically, some infants may present with respiratory distress or difficulty during infections, and recurrent lower respiratory tract infections are common, particularly in early childhood when immune and respiratory systems are still developing.[1][17][18] HPO terms such as “Recurrent pneumonia” (HP:0006532), “Restrictive respiratory defect” (HP:0002795), and “Dyspnea” (HP:0002094) are appropriate descriptors. The severity of respiratory involvement appears variable; Suzuki et al. describe thoracic hypoplasia as causing “mild to moderate” respiratory problems, suggesting that life-threatening respiratory failure is not typical, unlike in some lethal short-rib thoracic dysplasias.[1][18] Nevertheless, recurrent infections can contribute to chronic lung disease and reduced cardiopulmonary reserve, particularly in adulthood.

There is limited data on direct cardiac involvement. Most reports focus on thoracic and pulmonary manifestations rather than intrinsic cardiomyopathy or structural heart disease.[1][5][6][8] However, chronic hypoxia or recurrent infections could secondarily affect cardiopulmonary health. Formal pulmonary function testing has not been systematically reported but is likely to show restrictive patterns due to chest wall restriction. The HPO term “Thoracic hypoplasia” (HP:0005257) thus serves as a primary anatomical descriptor, with functional consequences captured by respiratory phenotype terms.

### 3.4 Growth, Development, and Functional Impact

Beyond specific skeletal and ocular abnormalities, axial SMD significantly affects overall growth, development, and functional status. Postnatal growth failure leads to short stature, with some patients exhibiting rhizomelic limb shortening early on and evolving to a short trunk phenotype in late childhood.[1][3][19] HPO terms “Short stature” (HP:0004322) and “Rhizomelic short stature” (HP:0003376) capture this pattern, while “Short trunk” (HP:0005776) reflects the later disproportion. The growth pattern suggests normal or near-normal birth size followed by slowing of growth rates, indicating that the disorder primarily affects postnatal skeletal maturation rather than fetal development.[1][5][8][19]

Developmental milestones in terms of motor and cognitive function have not been extensively documented. The available case reports do not emphasize cognitive impairment, suggesting that neurodevelopment is typically normal.[1][5][6][8] However, musculoskeletal and visual disabilities likely delay gross motor milestones and limit participation in age-appropriate activities. Short stature, thoracic restriction, and visual impairment together constrain physical activities, school participation, and vocational opportunities, especially in environments lacking adaptive supports.

Quality-of-life impact is significant, even if not formally quantified. Short stature and skeletal deformities may lead to social stigmatization, while visual impairment dramatically affects independence and education. Early adulthood functioning depends heavily on access to orthopedic care, visual rehabilitation, and environmental accommodations. In the context of a knowledge base, it is important to recognize that axial SMD affects multiple domains of functioning, including physical, sensory, and psychosocial, even if exact scores on standardized instruments like EQ-5D are not available.[1][3][6][13][14]

### 3.5 Other Reported Features and Phenotypic Variability

Other features have been reported sporadically in axial SMD or related *CFAP410* syndromes, though they are not core diagnostic criteria. In some patients with biallelic *CFAP410* mutations and early-onset retinal dystrophy, short stature and obesity have been noted, suggesting that *CFAP410* mutations may cause broader syndromic ciliopathy phenotypes beyond classical axial SMD.[16][13] For example, Daiger et al. reported a girl with early-onset retinal dystrophy, short stature, and obesity, proposing that biallelic *C21ORF2* mutations may underlie a syndromic ciliopathy in some cases.[16] However, this phenotype overlaps only partially with axial SMD and may represent a related but distinct clinical category.

In the axial SMD cases, Isidor et al. and Suzuki et al. did not report major visceral malformations, renal cystic disease, or neurological deficits, distinguishing axial SMD from more pleiotropic ciliopathies such as Joubert or Bardet–Biedl syndromes.[1][5][6][8][19] Pain, fatigue, and musculoskeletal discomfort are likely but not systematically described. The phenotypic spectrum thus appears relatively focused on skeletal and retinal systems, with some variability in the degree of thoracic and visual impairment.

Phenotypic expressivity may be influenced by genotype. For instance, some *CFAP410* variants are associated primarily with retinal disease, while others cause combined skeletal and retinal phenotypes.[13][14][16] Similarly, *NEK1* variants produce different short-rib thoracic dysplasia phenotypes with or without retinal involvement.[7] However, within the limited axial SMD case series, most core features are present in nearly all patients, suggesting relatively consistent expressivity at the syndrome level.[1][3][5][6][8][19]

## 4. Genetic and Molecular Information

### 4.1 Causal Genes and Gene-Level Annotations

The two established causal genes for axial SMD are *CFAP410* (formerly *C21ORF2*) and *NEK1*. OMIM lists *CFAP410* (MIM 603191) on chromosome 21q22.3 as the principal gene associated with the axial SMD phenotype (MIM 602271).[19] *CFAP410* encodes a cilia and flagella-associated protein that localizes to the connecting cilium of photoreceptors and to centrosomal structures in other ciliated cells.[4][13][16] Gene ontology annotations for *CFAP410* include roles in “axoneme assembly” (GO:0035082), “cilium organization” (GO:0044782), and “DNA repair” (GO:0006281), reflecting experimental evidence that *CFAP410* participates in ciliogenesis and DNA damage repair processes.[12][13][16]

*NEK1* (NIMA-related kinase 1; MIM 604588) encodes a serine/threonine kinase localized to the basal body and pericentriolar matrix, where it regulates primary cilium assembly, microtubule dynamics, and DNA damage response.[7][12][15] Wang et al. showed that *NEK1* mutations underlie a subset of axial SMD cases negative for *CFAP410* mutations and noted that *NEK1* had previously been implicated in three types of short-rib thoracic dystrophy, but those lacked retinal dystrophy.[7] Gene ontology terms associated with NEK1 include “protein serine/threonine kinase activity” (GO:0004674), “primary cilium assembly” (GO:0035994), and “DNA damage checkpoint” (GO:0000077).[12][15]

Evidence from human cell models indicates that *CFAP410* and *NEK1* function in a shared pathway. Gene knockout of either *NEK1* or *C21ORF2/CFAP410* in human retinal pigment epithelial cells dramatically reduces ciliogenesis, suggesting that both are essential for primary cilium formation.[12] NEK1 phosphorylates CFAP410 and stabilizes it against ubiquitin-mediated degradation, while CFAP410 acts as a NEK1 interactor required for efficient DNA damage repair, likely functioning within the same pathway in both ciliogenesis and DNA repair.[12][13][15] These interactions position *CFAP410* and *NEK1* within a functional module critical for primary cilium integrity and genomic stability, consistent with their involvement in axial SMD and in other ciliopathy and neurodegenerative phenotypes.

### 4.2 Pathogenic Variant Spectrum and Classification

The pathogenic variant spectrum in *CFAP410* includes missense, nonsense, frameshift, and splice-site variants, many of which affect evolutionarily conserved residues and are predicted to disrupt protein structure or function.[4][13][14][16] Wang et al. identified multiple *C21ORF2* mutations in axial SMD patients, including splice-site and missense variants, and confirmed pathogenicity by demonstrating abnormal splicing at the RNA level and reduced or aberrant protein products.[4] For example, they reported complex patterns of abnormal splicing caused by splice-site and branch-point mutations and noted that these mutations resulted in truncated or altered proteins that compromised ciliary function.[4] ClinVar documents specific *CFAP410* variants, such as NM_004928.3:c.319T>C (p.Tyr107His), as pathogenic for axial SMD, based on literature evidence and expert assertion.[10]

In isolated retinal dystrophies associated with *CFAP410*, compound heterozygous variants such as c.319T>C (p.Tyr107His) and c.347C>T (p.Pro116Leu) have been reported in patients with cone-rod dystrophy and macular staphyloma.[13][16] Functional studies of these variants suggest that they impair CFAP410’s ability to localize to photoreceptor cilia or interact with partner proteins, leading to ciliary dysfunction.[13] The fact that the same variants can cause predominantly ocular phenotypes in some individuals and syndromic skeletal-retinal phenotypes in others underscores the complexity of genotype–phenotype correlations and hints at additional modifiers or threshold effects in ciliary pathways.[13][14][16]

The *NEK1* variant spectrum in axial SMD includes biallelic loss-of-function mutations, such as frameshifts and nonsense variants, and possibly hypomorphic missense changes affecting kinase activity or stability.[7] Wang et al. noted that *NEK1* mutations associated with axial SMD differ from heterozygous *NEK1* variants implicated in ALS, which typically act as risk factors rather than fully penetrant Mendelian causes.[7][12][15] ACMG/AMP classification of *CFAP410* and *NEK1* variants in axial SMD is generally “pathogenic” or “likely pathogenic,” based on segregation, functional evidence, and absence or extreme rarity in population databases.[4][7][10][13][16]

Most axial SMD variants are germline and inherited in an autosomal recessive manner, with affected individuals being homozygous or compound heterozygous for pathogenic alleles.[1][4][5][7][8][19] Somatic variants have not been implicated. Structural variants, such as large deletions or duplications, have not been reported in axial SMD per se, although such events could theoretically disrupt *CFAP410* or *NEK1*; current evidence focuses on single-nucleotide and small indel variants.

### 4.3 Functional Consequences and Molecular Mechanisms of Variants

Pathogenic *CFAP410* and *NEK1* variants generally result in loss of function, either through nonsense-mediated decay, truncated nonfunctional protein, or missense changes disrupting protein folding, localization, or interactions.[4][7][12][13][16] Wang et al. demonstrated that *C21ORF2/CFAP410* mutants associated with axial SMD impair ciliogenesis, as evidenced by reduced cilia formation in patient-derived cells and by mislocalization of CFAP410 away from ciliary structures.[4] Immunohistochemical studies localized C21ORF2 protein to the daughter basal body, centriole adjacent to the basal body, and connecting cilium in photoreceptor cells, supporting a role in photoreceptor ciliary structure and function.[16] Loss-of-function variants likely compromise this localization, leading to defects in photoreceptor outer segment maintenance and ultimately retinal degeneration.[13][16]

At the cellular level, knockout of *NEK1* or *C21ORF2/CFAP410* in retinal pigment epithelial cells significantly reduces ciliogenesis, pointing to a shared requirement for these proteins in primary cilium formation.[12] NEK1 phosphorylates CFAP410 and prevents its degradation by the FBXO3-mediated ubiquitin–proteasome system, suggesting that NEK1 stabilizes CFAP410 and that disruption of this interaction destabilizes the ciliary apparatus.[12][13] ALS-associated CFAP410 mutants have been shown to mislocalize from centrosomes and fail to rescue ciliogenesis defects, further supporting the importance of precise localization and interaction with NEK1 for ciliary function.[12][15]

In addition to ciliogenesis, both NEK1 and CFAP410 have been implicated in DNA damage repair. NEK1 plays a critical role in DNA damage repair pathways, particularly in the response to double-strand breaks and the regulation of homologous recombination.[12] CFAP410 depletion reduces the efficiency of homologous recombination repair, and this defect can be rescued by NEK1 overexpression, indicating that CFAP410 functions within the same pathway as NEK1 in DNA damage repair.[12] Interestingly, NEK1 translocates to sites of DNA damage, whereas CFAP410 does not, suggesting that CFAP410 acts as a cofactor or stabilizer rather than a direct DNA repair enzyme.[12][13] In the context of axial SMD, these DNA repair defects may contribute to cellular stress in chondrocytes and photoreceptors, although this has not yet been explored directly in patient tissues.

### 4.4 Potential Modifier Genes and Epigenetic Contributions

No specific modifier genes have been convincingly identified in axial SMD, but the phenotypic variability among *CFAP410* and *NEK1* mutation carriers suggests that other genetic factors modulate disease expression. The interaction of CFAP410 with SPATA7, another ciliary protein associated with retinal dystrophy, raises the possibility that variation in SPATA7 or other ciliary genes may influence retinal severity in axial SMD.[13] Similarly, genes involved in Hedgehog signaling, microtubule dynamics, or DNA repair could theoretically modify skeletal or retinal phenotypes in individuals with *CFAP410* or *NEK1* mutations.

Epigenetic changes specific to axial SMD have not been reported. However, more general epigenetic mechanisms, such as chromatin remodeling in chondrocytes or photoreceptors, could influence the extent to which impaired ciliogenesis translates into overt dysplasia or degeneration. The current absence of epigenomic studies in axial SMD is likely due to the rarity of the disease and the difficulty of obtaining relevant tissues. Thus, a knowledge base should note that epigenetic contributions are plausible but currently uncharacterized.

### 4.5 Chromosomal and Structural Genomic Considerations

There is no evidence that large-scale chromosomal abnormalities, such as aneuploidies, translocations, or inversions, cause axial SMD. The causal genes *CFAP410* and *NEK1* reside on chromosomes 21q22.3 and 4q33, respectively, and their involvement in axial SMD is due to point mutations and small indels rather than structural rearrangements.[4][7][19] DECIPHER and similar structural variation databases have not been specifically implicated in axial SMD, and chromosomal microarray or karyotyping is generally unrevealing in affected individuals. This underscores the importance of sequence-level analysis (e.g., whole-exome sequencing) for diagnosis.[4][7]

## 5. Environmental Information

### 5.1 Environmental Factors and Exposures

Because axial SMD is a monogenic autosomal recessive disorder, environmental factors do not play a causal role in disease initiation. No toxins, pollutants, or occupational exposures have been linked to the development of axial SMD in any reported case.[1][3][5][6][8] Comparative toxicogenomics databases do not list axial SMD as an environmentally induced condition, and mechanisms of disease are firmly rooted in genetic disruption of ciliogenesis and DNA repair pathways.

That said, environmental exposures can influence disease course and complications. Thoracic hypoplasia and restrictive lung function make patients more vulnerable to lower respiratory tract infections and potentially to environmental pollutants that exacerbate respiratory symptoms.[1][17][18] Exposure to indoor air pollution, second-hand smoke, or high levels of ambient particulate matter could worsen respiratory function and increase the frequency or severity of pneumonia episodes, although specific studies have not been conducted. Standard public health recommendations to reduce respiratory environmental exposures are therefore applicable to axial SMD, even if not disease-specific.

### 5.2 Lifestyle Factors

Lifestyle factors such as diet, physical activity, and smoking have not been formally studied in axial SMD but can be considered in general health management. Because skeletal and visual limitations may reduce physical activity, there is potential for weight gain and secondary metabolic issues, though obesity is not a core feature.[16] Maintaining a healthy diet and as much physical activity as feasible, with appropriate adaptations, may help prevent secondary complications such as deconditioning or cardiovascular risk. Smoking or vaping should be strongly discouraged in affected individuals due to the additive burden on already compromised respiratory systems.[1][17][18]

Alcohol consumption and other lifestyle factors have no documented impact on disease initiation or progression, but adherence to general health guidelines remains important. In a knowledge base, it is appropriate to note that no disease-specific lifestyle risk factors are known, but general respiratory and cardiovascular health measures are recommended.

### 5.3 Infectious Agents

No infectious agents have been implicated in axial SMD. The disease is not caused by bacteria, viruses, fungi, or parasites, and there is no evidence of infection-triggered onset or exacerbation of skeletal or retinal manifestations.[1][3][5][6][8] However, recurrent respiratory infections are common complications, particularly in early childhood, due to thoracic restriction and possibly reduced cough effectiveness.[1][17][18] Standard childhood infections such as viral bronchiolitis, bacterial pneumonia, and influenza may be more severe in axial SMD and contribute to transient or chronic worsening of respiratory function.

In sum, the environmental, lifestyle, and infectious context of axial SMD is best understood as influencing complications and quality of life rather than primary disease etiology. The knowledge base should emphasize that axial SMD is fundamentally genetic, with minimal evidence for environmental or infectious causation.

## 6. Mechanism / Pathophysiology

### 6.1 Ordered Causal Chain from Mutation to Clinical Phenotype

Step 1: Biallelic pathogenic variants in *CFAP410* or *NEK1* lead to loss or severe reduction of functional CFAP410 or NEK1 protein in cells, particularly chondrocytes and photoreceptors.[4][7][12][13][16][19]

Step 2: Loss of CFAP410 and/or NEK1 function results in defective primary ciliogenesis and impaired stability and function of the primary cilium in affected cells, as demonstrated in human retinal pigment epithelial cells and neuronal models.[4][12][13][15][16]

Step 3: Primary cilium dysfunction leads to altered ciliary signaling pathways, including Hedgehog and other morphogen gradients, which are critical for skeletal development and retinal photoreceptor maintenance; this step is inferred based on general cilium biology and indirect evidence rather than demonstrated specifically in axial SMD.[4][7][12][13][16]

Step 4: In developing chondrocytes of the axial skeleton, disrupted ciliary signaling results in abnormal endochondral ossification and metaphyseal modeling, leading to shortening and deformity of ribs, vertebrae, pelvis, and proximal femora, manifesting as thoracic hypoplasia, platyspondyly, lacy iliac crests, and proximal femoral metaphyseal dysplasia.[1][3][4][7][8][19]

Step 5: In photoreceptors, defective cilium structure and function compromise outer segment formation and maintenance, impairing phototransduction and leading to progressive cone-rod dystrophy and retinal degeneration, clinically manifested as retinitis pigmentosa, decreased visual acuity, and progressive visual loss.[1][3][4][13][14][16][19]

Step 6: Concurrently, loss of NEK1 and CFAP410 function disrupts DNA damage repair pathways, particularly homologous recombination, leading to increased DNA damage and cellular stress, especially in post-mitotic cells such as chondrocytes and photoreceptors; this step is demonstrated in vitro and inferred to contribute to tissue pathology in axial SMD.[12][13]

Step 7: The combination of structural ciliary defects and impaired DNA repair leads to progressive dysfunction and attrition of chondrocytes and photoreceptors, resulting in persistent skeletal deformities and progressive retinal degeneration.[1][3][4][12][13][16][19]

Step 8: Thoracic skeletal deformities and small rib cage dimensions cause restrictive ventilatory defects and reduced lung volumes, which in turn lead to mild to moderate respiratory problems, increased susceptibility to airway infections, and recurrent pneumonia.[1][17][18][19]

Step 9: The combination of skeletal dysplasia, respiratory compromise, and visual impairment results in postnatal growth failure, short stature, functional disability, and reduced quality of life, with disease course typically chronic and progressive for retinal manifestations and static for skeletal deformities after growth completion.[1][3][5][6][19]

### 6.2 Molecular Pathways and Primary Cilium Biology

The primary cilium is a sensory organelle present on many cell types, including chondrocytes and photoreceptors, and serves as a hub for signaling pathways such as Hedgehog, Wnt, and PDGF.[4][7][12][13][16] CFAP410 and NEK1 localize to the basal body and ciliary structures, where they regulate cilium assembly, stability, and signaling.[4][12][13][15][16] Gene ontology terms reflecting these functions include “primary cilium assembly” (GO:0035994), “cilium organization” (GO:0044782), “microtubule cytoskeleton organization” (GO:0000226), and “signal transduction” (GO:0007165). In photoreceptors, CFAP410 localizes to the connecting cilium, the bridge between the inner and outer segments, which is essential for trafficking phototransduction proteins.[16][13]

Wang et al. demonstrated that CFAP410 mutations associated with axial SMD disrupt ciliary morphology and function, evidenced by cupped and flared anterior ends of ribs and lacy ilia, consistent with ciliary signaling defects in chondrocytes.[4] Although specific signaling pathways have not been directly assayed in axial SMD patient cells, analogous ciliopathies show impaired Hedgehog signaling due to defective ciliary translocation of Gli transcription factors, leading to abnormal skeletal patterning and chondrocyte proliferation.[4][7] It is therefore reasonable to infer that CFAP410 and NEK1 mutations disrupt Hedgehog and related pathways in axial SMD, even if direct evidence is lacking.

In photoreceptors, CFAP410 mutations compromise ciliary transport, leading to mislocalization of phototransduction proteins and outer segment disorganization.[13][16] The outer segments are specialized sensory cilia, and their integrity depends on proper ciliary transport and structural maintenance.[13][16] Disruption of these processes leads to degeneration of rods and cones, consistent with cone-rod dystrophy and retinitis pigmentosa phenotypes observed in axial SMD and related *CFAP410* retinopathies.[1][3][13][14][16] These processes correspond to GO terms such as “photoreceptor cell maintenance” (GO:0045494) and “visual perception” (GO:0007601).

### 6.3 Cellular Processes: Ciliogenesis, Cell Cycle, and DNA Repair

At the cellular level, CFAP410 and NEK1 influence multiple processes, including ciliogenesis, cell cycle control, microtubule homeostasis, and DNA damage response.[4][12][13][15] NEK1 is part of the NIMA-related kinase family and has been implicated in regulation of primary cilium formation, ciliary disassembly, and cell cycle progression.[12][15] Its depletion in human retinal pigment epithelial cells reduces ciliogenesis, while overexpression inhibits ciliogenesis, indicating that precise levels of NEK1 activity are required for normal cilium dynamics.[12][15] CFAP410 interacts with NEK1 and is required for efficient DNA damage repair via homologous recombination; CFAP410 depletion reduces repair efficiency, which can be rescued by NEK1 overexpression.[12][13]

These findings map to GO biological processes such as “DNA double-strand break repair via homologous recombination” (GO:0000724), “cell cycle checkpoint” (GO:0000075), and “primary cilium resorption” (GO:0060284). In the context of axial SMD, disruption of these processes in chondrocytes may lead to accumulation of DNA damage, cell cycle arrest, or apoptosis, contributing to abnormal growth plate function and metaphyseal dysplasia.[4][7][12][13] Similarly, in photoreceptors, defective DNA repair may exacerbate stress from high metabolic activity and light exposure, promoting degeneration.

Importantly, NEK1 and CFAP410 are part of a broader network of proteins involved in ciliogenesis and DNA repair, including cyclin F and VCP, which have been studied in ALS and other diseases.[12][15] The intersection of these proteins suggests that primary cilium dysfunction and DNA damage repair defects are convergent mechanisms that can manifest in different tissue-specific diseases depending on additional context. In axial SMD, the primary affected cell types are chondrocytes (CL:0000097) and photoreceptors (CL:0000740), though other cells may be partially affected.[4][7][12][13][16]

### 6.4 Protein Dysfunction: Structural and Functional Consequences

Structurally, CFAP410 is a ciliary protein whose detailed three-dimensional configuration has not been fully elucidated, but pathogenic missense variants such as Y107H and P116L, identified in retinal dystrophy, likely destabilize the protein or disrupt interaction interfaces.[13][16] These variants may alter CFAP410’s ability to bind NEK1 or other ciliary proteins, or to localize properly to basal bodies and connecting cilia.[13][16] Nonsense and frameshift variants truncate the protein, often leading to nonsense-mediated decay and complete loss of function.[4][13][16]

NEK1’s kinase domain and regulatory regions are sensitive to missense variants that can impair catalytic activity, substrate recognition, or autophosphorylation, while truncating variants eliminate functional domains.[7][12][15] Loss of NEK1 activity disrupts phosphorylation of targets such as CFAP410, leading to its degradation via the FBXO3-mediated ubiquitin–proteasome system.[12] These biochemical interactions indicate that NEK1 stabilizes CFAP410 and that their loss leads to destabilization of ciliary structures.

In terms of biochemical abnormalities, there is no evidence of enzyme deficiencies or metabolic derangements typical of metabolic diseases; instead, the primary biochemical disturbance lies in signaling and structural maintenance pathways of cilia and DNA repair complexes.[4][7][12][13][16] This underlines that axial SMD is a structural and signaling disorder rather than a classical inborn error of metabolism.

### 6.5 Tissue Damage Mechanisms and Downstream Pathology

The downstream consequences of primary cilium dysfunction and DNA repair defects in axial SMD differ by tissue. In the skeleton, chondrocytes in growth plates rely on ciliary signaling to interpret morphogen gradients and regulate proliferation and differentiation. Disruption of these signals leads to abnormal stacking and maturation of chondrocytes, producing metaphyseal irregularities and shortened bones.[4][7][19] The ribs, vertebrae, pelvis, and proximal femora are particularly affected, leading to thoracic hypoplasia, platyspondyly, and lacy iliac crests.[1][3][8][19] Once formed, these structural deformities are relatively static, although growth may exacerbate disparity between trunk and limbs.

In the retina, photoreceptors are highly dependent on ciliary transport and constant renewal of outer segments. Ciliary defects disrupt the trafficking of opsins and other phototransduction proteins, causing mislocalization, accumulation of toxic intermediates, and eventual photoreceptor apoptosis.[13][16] DNA repair defects may further contribute by allowing accumulation of oxidative DNA damage induced by light exposure and high metabolic activity.[12][13] The result is progressive loss of rods and cones, manifested clinically as cone-rod dystrophy and retinitis pigmentosa, with early involvement of cones leading to central vision loss and later rod involvement causing night blindness and peripheral field loss.[1][3][13][14][16][19]

Thoracic hypoplasia and restrictive ventilatory defects represent a mechanical consequence of skeletal abnormalities. Reduced lung volumes increase work of breathing and limit respiratory reserve, making patients more vulnerable to infections and hypoventilation during illness.[1][17][18] Recurrent infections may lead to bronchiectasis or chronic lung disease, further compromising respiratory function. However, in contrast to some lethal thoracic dysplasias, axial SMD typically permits survival into adulthood, suggesting that residual thoracic dimensions are sufficient for basal respiratory needs in most cases.[1][5][6][19]

### 6.6 Suggested GO and CL Terms for Mechanistic Annotation

For mechanistic annotation, key GO biological process terms include “primary cilium assembly” (GO:0035994), “cilium organization” (GO:0044782), “DNA double-strand break repair via homologous recombination” (GO:0000724), “microtubule cytoskeleton organization” (GO:0000226), “chondrocyte differentiation” (GO:0035989), and “photoreceptor cell maintenance” (GO:0045494). Relevant GO molecular function terms include “protein serine/threonine kinase activity” (GO:0004674) for NEK1 and “protein binding” (GO:0005515) for CFAP410. GO cellular component terms encompass “basal body” (GO:0005932), “centrosome” (GO:0005813), “primary cilium” (GO:0097730), “photoreceptor connecting cilium” (GO:0032391), and “photoreceptor outer segment” (GO:0001750).[4][7][12][13][16][15]

Cell Ontology (CL) terms for cell types involved include CL:0000097 (chondrocyte), CL:0000740 (retinal photoreceptor cell), CL:0000742 (cone photoreceptor), and CL:0000743 (rod photoreceptor). These cell types are the primary sites of pathophysiologic events in axial SMD.[4][7][12][13][16] Additional involvement of retinal pigment epithelial cells (CL:0000746) is suggested by in vitro models.[12] Such annotations will facilitate integration of axial SMD into multi-omic and multi-organ atlases of disease mechanisms.

## 7. Anatomical Structures Affected

### 7.1 Organ-Level Involvement

At the organ level, axial SMD primarily affects the skeletal system, particularly the axial skeleton (spine, ribs, pelvis) and proximal appendicular skeleton (proximal femora, upper arms), and the visual system, specifically the retina.[1][3][5][8][19] In anatomical ontology terms, affected skeletal structures include the thoracic cage (UBERON:0002193), ribs (UBERON:0002224), vertebral column (UBERON:0001130), pelvis (UBERON:0001270), and femur (UBERON:0000981). The spine shows mild platyspondyly and spondylar dysplasia, the ribs are short with flared and cupped anterior ends, the pelvis exhibits lacy iliac crests, and the proximal femora show metaphyseal dysplasia.[1][3][8][19]

The retina (UBERON:0000966) is the primary ocular structure affected, with involvement of photoreceptors and retinal pigment epithelium leading to retinitis pigmentosa or cone-rod dystrophy.[1][3][6][13][14][16][19] These changes ultimately impact the entire visual pathway, but the lesion is primarily retinal rather than optic nerve or cortical. The lungs (UBERON:0002048) are secondarily affected due to thoracic restriction, with reduced lung volumes and susceptibility to infections.[1][17][18]

Body systems involved include the musculoskeletal system (SNOMED and ICD skeletal categories), respiratory system (due to thoracic hypoplasia and restrictive defects), and visual system. Cardiovascular, digestive, endocrine, and nervous systems are not prominently involved, distinguishing axial SMD from more pleiotropic syndromic ciliopathies.[1][3][5][6][8][19]

### 7.2 Tissue and Cell-Level Involvement

At the tissue level, the primary affected tissues are cartilage and bone of the axial skeleton and the neural retina. Skeletal changes arise from abnormal growth plate cartilage and endochondral ossification, implicating cartilage tissue (UBERON:0002384) and bone tissue (UBERON:0002481). Chondrocytes (CL:0000097) in growth plates and cartilage anlagen rely on primary cilia for sensing mechanical and chemical cues; their dysfunction leads to abnormal bone modeling.[4][7][19] Osteoblasts and osteocytes may also be indirectly affected, though specific data are lacking.

In the retina, the neural tissue (UBERON:0000944) and photoreceptor layer are affected, with primary involvement of rods and cones. Cone photoreceptors (CL:0000742) and rod photoreceptors (CL:0000743) are the main cell types that degenerate due to ciliary dysfunction.[13][16] Retinal pigment epithelial cells (CL:0000746) may also be impacted by impaired ciliogenesis and DNA repair pathways, as suggested by in vitro studies.[12] The tissue type is predominantly nervous tissue, with specialized modifications for phototransduction.

### 7.3 Subcellular Structures and Cellular Compartments

Subcellularly, axial SMD centers on the primary cilium and associated structures. GO cellular component terms include “primary cilium” (GO:0097730), “basal body” (GO:0005932), “centrosome” (GO:0005813), “photoreceptor connecting cilium” (GO:0032391), and “photoreceptor outer segment” (GO:0001750).[4][12][13][16][15] CFAP410 localizes to the connecting cilium and adjacent centriolar structures in photoreceptors, while NEK1 localizes to the basal body and pericentriolar matrix.[4][12][16][15] These locations are critical for ciliary assembly, trafficking, and signaling.

In DNA repair, nuclear compartments are also involved. CFAP410 participates indirectly in DNA damage repair, while NEK1 translocates to sites of DNA damage, implicating nuclear foci and chromatin as relevant compartments.[12][13] GO cellular component terms such as “nucleus” (GO:0005634), “nuclear chromatin” (GO:0000790), and “DNA repair complex” (GO:0031297) are applicable.

### 7.4 Spatial Localization and Lateralization

Axial SMD affects bilateral structures symmetrically. Short ribs, thoracic hypoplasia, platyspondyly, lacy iliac crests, and proximal femoral metaphyseal changes are bilateral and symmetric by definition.[1][3][8][19] The retinal involvement is also bilateral; retinitis pigmentosa and cone-rod dystrophy in axial SMD affect both eyes, with symmetric or near-symmetric degeneration.[1][3][6][13][14][16] There is no evidence of lateralized (unilateral) disease.

Specific anatomical sites of involvement include the anterior ends of ribs, vertebral bodies, iliac wings, and proximal femoral metaphyses, as detailed in radiologic descriptions.[1][3][8][19] Within the retina, the macular region may be particularly affected in some *CFAP410* retinopathies, with macular staphyloma reported in certain cases, though this has not been highlighted in axial SMD specifically.[13][16] For knowledge base annotation, mapping to UBERON terms for each anatomical site and linking to corresponding HPO terms will provide a structured representation of spatial pathology.

## 8. Temporal Development

### 8.1 Age of Onset and Early Course

Axial SMD typically presents in infancy or early childhood. Orphanet notes that age of onset is in infancy or childhood, and Orphanet/ORDO lists “Childhood” and “Infancy” as ages of onset.[3][9] OMIM and Suzuki et al. emphasize postnatal onset of growth failure, with rhizomelic short stature evident in early childhood and evolution to short trunk later.[1][19] Birth length and weight are often within normal ranges, indicating that prenatal development is relatively spared, and that pathogenic processes affecting skeletal growth are most active postnatally.[1][5][8][19]

Retinal dystrophy becomes clinically apparent in early life as well, with impaired visual acuity coming to medical attention in early childhood and rapid deterioration thereafter.[1][3][19] In some cases, night blindness or visual complaints may be the initial sign, while in others visual problems are detected during routine examinations or in the evaluation of syndromic features.[6][13][14][16] Thus, axial SMD is best categorized as a pediatric-onset chronic disorder with early manifestations in both skeletal and ocular domains.

### 8.2 Progression of Skeletal Abnormalities

Skeletal abnormalities in axial SMD evolve over time, particularly during the growth period. In early childhood, rhizomelic limb shortening may be more apparent, with disproportionate shortening of the upper arms and upper legs relative to trunk length.[1][3][19] As growth proceeds, the trunk may become relatively shorter, reflecting progressive impact of spinal and thoracic deformities on overall height.[1][5][8][19] Radiographic changes, such as platyspondyly and metaphyseal irregularities, become more pronounced as bones grow, but the basic pattern of deformities is established early.

Once skeletal maturation is complete, skeletal abnormalities become relatively static, though they may contribute to chronic pain, joint problems, or decreased mobility.[1][5][6] There is no evidence of progressive deformity into adulthood beyond what is expected from growth-based changes. Disease stages in terms of skeletal involvement can be conceptualized as early childhood (emergence of disproportion and thoracic hypoplasia), later childhood and adolescence (consolidation of skeletal deformities), and adulthood (stable skeletal phenotype with chronic functional consequences).[1][3][5][8][19]

### 8.3 Progression of Retinal Disease

Retinal disease in axial SMD is progressive and often more aggressive than skeletal changes. Suzuki et al. note that impaired visual acuity arises early and “function rapidly deteriorates,” suggesting a rapid progression to severe visual impairment.[1] Cone-rod dystrophy implies early involvement of cone photoreceptors, leading to central vision loss, color vision defects, and photophobia, followed by rod degeneration with night blindness and peripheral field constriction.[1][3][6][13][14][16][19] In related *CFAP410* retinopathies, patients can progress to legal blindness in adolescence or early adulthood, although exact timelines vary.[13][14][16]

Stages of retinal disease in axial SMD may be conceptualized as early childhood (onset of visual symptoms and early electrophysiologic abnormalities), mid-childhood to adolescence (rapid progression of cone-rod dystrophy and significant visual impairment), and adulthood (established severe visual loss, possibly with residual light perception only). The rate of progression likely depends on specific genotype and other factors, but data are limited due to the small number of cases and lack of systematic follow-up.[1][3][6][13][14][16][19]

### 8.4 Disease Course Patterns and Critical Periods

The overall disease course of axial SMD is chronic and lifelong. Skeletal deformities develop and stabilize during childhood and adolescence, while retinal degeneration continues to progress into adulthood. There is no evidence of remission or relapsing–remitting patterns; instead, the course is best characterized as progressive for retinal manifestations and non-progressive (after growth) for skeletal deformities.[1][3][5][6][19]

Critical periods include early childhood, when thoracic hypoplasia and respiratory vulnerability are greatest, and when visual impairment begins, and adolescence, when skeletal growth completes and retinal degeneration may reach advanced stages.[1][18][19] These periods represent windows of opportunity for interventions, such as respiratory support during severe infections, orthopedic management of skeletal complications, and visual rehabilitation or low-vision support. Because axial SMD is not currently modifiable at the genetic or mechanistic level, critical periods are defined more by management needs than by opportunities to alter disease pathogenesis.

## 9. Inheritance and Population

### 9.1 Inheritance Pattern and Penetrance

Axial SMD follows an autosomal recessive inheritance pattern, as evidenced by recurrence among siblings of both sexes, parental consanguinity in several families, and identification of biallelic pathogenic variants in *CFAP410* or *NEK1*.[1][3][5][8][9][19] OMIM and Orphanet both list autosomal recessive inheritance for axial SMD.[3][9][19] GTR/MedGen also notes autosomal recessive inheritance.[17] In affected families, parents are typically heterozygous carriers and are clinically unaffected, consistent with autosomal recessive transmission.

Penetrance appears to be high or complete for disease-defining features in biallelic

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 13 |
| On topic | 2 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:37477485` (1 mention) - [Optical voltage imaging in neurons in neurogenic erectile dysfunction: Progress in research].
  - shared terms: none

Weighed against this report's own most characteristic terms: `axial`, `smd`, `disease`, `retinal`, `cfap410`, `skeletal`, `nek1`, `thoracic`, `dystrophy`, `primary`, `phenotype`, `function`, `respiratory`, `photoreceptor`, `variant`, `dna`, `involvement`, `repair`, `affected`, `patient`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 60 |
| Resolved | 55 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 3 |
| Unverifiable | 1 |
| Terms whose name was checked | 47 |
| Terms named correctly | 23 |
| Terms named as a **different** term | 13 |
| Terms whose name is worth a second look | 11 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001511` (2 mentions) - the report calls it "Disproportionate short stature"; HP calls it **Intrauterine growth retardation**
- `HP:0002883` (2 mentions) - the report calls it "Abnormality of the ilium"; HP calls it **Hyperventilation**
- `HP:0000944` (2 mentions) - the report calls it "Metaphyseal dysplasia"; HP calls it **Abnormal metaphysis morphology**
- `HP:0003376` (1 mention) - the report calls it "Rhizomelic short stature"; HP calls it **Steppage gait**
- `HP:0005776` (1 mention) - the report calls it "Short trunk"; HP calls it **Carpal bone malsegmentation**
- `GO:0035994` (3 mentions) - the report calls it "primary cilium assembly"; GO calls it **response to muscle stretch**
- `GO:0060284` (1 mention) - the report calls it "primary cilium resorption"; GO calls it **regulation of cell development**
- `GO:0035989` (1 mention) - the report calls it "chondrocyte differentiation"; GO calls it **tendon development**
- `GO:0005932` (2 mentions) - the report calls it "basal body"; GO calls it **GO_0005932**
- `CL:0000742` (2 mentions) - the report calls it "cone photoreceptor"; CL calls it **periarticular chondrocyte**
- `CL:0000743` (2 mentions) - the report calls it "rod photoreceptor"; CL calls it **hypertrophic chondrocyte**
- `GO:0000790` (1 mention) - the report calls it "nuclear chromatin"; GO calls it **GO_0000790**
- `GO:0031297` (1 mention) - the report calls it "DNA repair complex"; GO calls it **replication fork processing**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0003379` (2 mentions), reported as "Abnormality of the femoral metaphysis" - HP does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0005932` (GO_0005932) (2 mentions) - replaced by `GO:0036064`
- `UBERON:0000944` (obsolete dorsal branch) (1 mention)
- `GO:0000790` (GO_0000790) (1 mention) - replaced by `GO:0000785`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002655` (1 mention) - the report calls it "Spondylar dysplasia"; HP calls it **Spondyloepiphyseal dysplasia**
- `HP:0000510` (1 mention) - the report calls it "Retinitis pigmentosa"; HP calls it **Rod-cone dystrophy**, and lists "Retinitis pigmentosa" among its other names
- `HP:0000580` (1 mention) - the report calls it "Pigmentary retinal degeneration"; HP calls it **Pigmentary retinopathy**, and lists "Retinal pigmentary degeneration" among its other names
- `HP:0007663` (1 mention) - the report calls it "Decreased visual acuity"; HP calls it **Reduced visual acuity**, and lists "Decreased visual acuity" among its other names
- `HP:0002795` (1 mention) - the report calls it "Restrictive respiratory defect"; HP calls it **Abnormal respiratory system physiology**, and lists "Functional respiratory abnormality" among its other names
- `GO:0000077` (1 mention) - the report calls it "DNA damage checkpoint"; GO calls it **DNA damage checkpoint signaling**, and lists "DNA damage checkpoint" among its other names
- `GO:0000724` (2 mentions) - the report calls it "DNA double-strand break repair via homologous recombination"; GO calls it **double-strand break repair via homologous recombination**
- `GO:0000075` (1 mention) - the report calls it "cell cycle checkpoint"; GO calls it **cell cycle checkpoint signaling**, and lists "cell cycle checkpoint" among its other names
- `CL:0000097` (3 mentions) - the report calls it "chondrocyte"; CL calls it **mast cell**, and lists "labrocyte" among its other names
- `CL:0000740` (2 mentions) - the report calls it "retinal photoreceptor cell"; CL calls it **retinal ganglion cell**
- `GO:0097730` (2 mentions) - the report calls it "primary cilium"; GO calls it **non-motile cilium**, and lists "immotile primary cilium" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.