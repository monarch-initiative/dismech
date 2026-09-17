---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-09-16T20:51:23.845361'
end_time: '2026-09-16T20:57:25.049878'
duration_seconds: 361.2
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: ALG2-congenital disorder of glycosylation
  mondo_id: MONDO:0011933
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
  total_references: 6
  verified: 6
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 6
  on_topic: 5
  validator_version: 0.2.1
term_validation:
  total_terms: 94
  verified: 91
  not_found: 2
  obsolete: 1
  unverifiable: 0
  confabulation_rate: 0.021
  labels_checked: 52
  labels_matching: 21
  labels_mismatched: 21
  mislabelled_terms:
  - term_id: NCIT:C123879
    reported_labels:
    - Congenital Disorder of Glycosylation
    ontology_label: Paritaprevir
  - term_id: HP:0002063
    reported_labels:
    - hypomyelination
    ontology_label: Rigidity
  - term_id: HP:0000514
    reported_labels:
    - coloboma of iris
    ontology_label: Slow saccadic eye movements
  - term_id: HP:0002019
    reported_labels:
    - gastroesophageal reflux
    ontology_label: Constipation
  - term_id: HP:0003118
    reported_labels:
    - hypoalbuminemia
    ontology_label: Increased circulating cortisol level
  - term_id: HP:0003401
    reported_labels:
    - easy fatigability
    ontology_label: Paresthesia
  - term_id: HP:0001370
    reported_labels:
    - skeletal dysplasia
    ontology_label: Rheumatoid arthritis
  - term_id: HP:0001615
    reported_labels:
    - stridor
    ontology_label: Hoarse cry
  - term_id: HP:0001744
    reported_labels:
    - respiratory muscle weakness
    ontology_label: Splenomegaly
  - term_id: GO:0042285
    reported_labels:
    - "GDP-mannose:Man(1)GlcNAc(2)-PP-dolichol alpha\u20111,3-mannosyltransferase"
    ontology_label: xylosyltransferase activity
  - term_id: CHEBI:17646
    reported_labels:
    - GDP-mannose
    ontology_label: mevaldic acid
  - term_id: CHEBI:15996
    reported_labels:
    - UDP-GlcNAc
    ontology_label: GTP
  - term_id: CL:0000540
    reported_labels:
    - hepatocyte
    ontology_label: neuron
  - term_id: CL:0000066
    reported_labels:
    - neuron
    ontology_label: epithelial cell
  - term_id: CL:0000565
    reported_labels:
    - skeletal muscle cell
    ontology_label: fat body cell
  - term_id: CL:0000317
    reported_labels:
    - endothelial cell
    ontology_label: sebocyte
  - term_id: GO:0006489
    reported_labels:
    - N-linked glycosylation via asparagine
    ontology_label: dolichyl diphosphate biosynthetic process
  - term_id: UBERON:0002107
    reported_labels:
    - liver
    - skeletal muscle organ
    ontology_label: liver
  - term_id: UBERON:0002048
    reported_labels:
    - respiratory system
    ontology_label: lung
  - term_id: NCIT:C20190
    reported_labels:
    - Prognostic Factor
    ontology_label: Chemical Agents
  - term_id: NCIT:C18163
    reported_labels:
    - Biomarker
    ontology_label: Kallikrein-2
  labels_variant: 10
  unresolved_terms:
  - HP:0003285
  - CHEBI:27112
  obsolete_terms:
  - term_id: NCIT:C62036
    ontology_label: Nasal Cavity
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** ALG2-congenital disorder of glycosylation
- **MONDO ID:** MONDO:0011933 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **ALG2-congenital disorder of glycosylation** covering all of the
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

# ALG2-Congenital Disorder of Glycosylation (ALG2-CDG, CDG-Ii): Comprehensive Disease Characteristics

ALG2-congenital disorder of glycosylation (ALG2-CDG, historically CDG-Ii) is a very rare autosomal recessive inborn error of metabolism caused by biallelic pathogenic variants in the *ALG2* gene, which encodes an endoplasmic reticulum (ER) α1,3‑mannosyltransferase required for early steps of N‑linked glycosylation.[7][10][11] The disorder manifests as a multi‑system disease with prominent neurologic involvement, including global developmental delay or intellectual disability, hypotonia, infantile spasms or other seizures, ophthalmologic anomalies such as iris coloboma and cataracts, dysmorphic facial features, hepatopathy with coagulation abnormalities, and, in some individuals, a neuromuscular junction phenotype consistent with congenital myasthenic syndrome (CMS).[2][7][8][11][12][14][16] Since first description in 2003, only approximately 14–15 patients have been reported worldwide, underscoring its ultra‑rare nature and limiting robust epidemiologic estimates.[2][7][14][16] At the molecular level, loss of ALG2 activity leads to accumulation of truncated lipid‑linked oligosaccharide precursors, generalized hypoglycosylation of glycoproteins, and characteristic alterations in transferrin glycoforms, including a highly specific heptasaccharide glycan biomarker that can be detected by mass spectrometry.[4][11][14][16] There is currently no disease‑specific curative therapy; management is symptomatic and supportive, although acetylcholinesterase inhibitors can improve neuromuscular symptoms in ALG2‑related CMS.[2][12][13][16] The pathophysiology of ALG2-CDG provides a unique window into the early stages of dolichol‑linked oligosaccharide biosynthesis and highlights the critical role of N‑glycosylation for nervous system development, neuromuscular junction integrity, and multi‑organ function.[11][12][18]

## 1. Disease Information

### 1.1 Definition and Overview

ALG2-congenital disorder of glycosylation (ALG2-CDG) is a subtype of congenital disorders of N‑linked glycosylation characterized by defective mannose addition to the dolichol‑linked oligosaccharide precursor in the ER, resulting in hypoglycosylation of numerous glycoproteins and a multisystem clinical phenotype.[2][7][11][12] In the current nosology of CDG, ALG2-CDG is classified as a CDG type I disorder affecting the assembly of the lipid‑linked oligosaccharide prior to its transfer to nascent polypeptides.[2][11][12] OMIM designates the phenotype as “congenital disorder of glycosylation, type Ii” (MIM 607906) and recognizes that it is caused by homozygous or compound heterozygous mutations in *ALG2* (MIM 607905) on chromosome 9q22.33.[7][10] Orphanet describes “Syndrome CDG‑ALG2” as a form of congenital N‑glycosylation anomaly characterized by iris coloboma, cataract, infantile spasms, developmental delay, and abnormal coagulation factors, with onset in the neonatal or early infancy period.[8] The Genetic and Rare Diseases Information Center (GARD) similarly notes that ALG2-CDG presents in newborns or infants with neurological, ophthalmological, and coagulation abnormalities and distinctive facial morphology.[1][2]

Clinically, ALG2-CDG spans a spectrum. A “classic” severe multisystem presentation includes profound developmental delay or intellectual disability, seizures, hypotonia, coloboma, cataracts, hepatomegaly, coagulopathy, and hypomyelination.[7][8][11][12][16] A milder allelic phenotype manifests primarily as a neuromuscular transmission disorder with fatigable muscle weakness, termed ALG2 congenital myasthenic syndrome (ALG2-CMS, associated with OMIM 616228).[2][10][12][13] The disease is rare enough that most knowledge derives from individual case reports and small case series rather than large cohorts, but recent systematic glycophenotyping and ClinGen curation have consolidated ALG2-CDG as a distinct, strongly validated Mendelian entity.[9][14][16]

From a mechanistic standpoint, ALG2-CDG is prototypical of disorders in which defective glycosyltransferase activity at the cytosolic face of the ER disrupts the assembly of the N‑glycan precursor. Thiel et al. identified deficiency of human ALG2 (GDP‑Man:Man\(_1\)GlcNAc\(_2\)‑PP‑dolichol α1,3‑mannosyltransferase) as the cause of a “new type of congenital disorders of glycosylation (CDG) designated CDG-Ii,” with accumulation of Man\(_1\)GlcNAc\(_2\)‑PP‑dolichol and Man\(_2\)GlcNAc\(_2\)‑PP‑dolichol in patient fibroblasts.[11] This biochemical defect underlies the clinical features and provides a clear functional link between gene, pathway, and phenotype.

### 1.2 Key Identifiers and Ontology Mapping

ALG2-CDG is represented in multiple disease ontologies and classification systems, which is crucial for interoperability in disease knowledge bases. OMIM assigns phenotype MIM number 607906 for “congenital disorder of glycosylation, type Ii,” with the associated gene *ALG2* having MIM number 607905.[7][10] Orphanet lists the disorder as “ALG2-CDG” or “Syndrome CDG‑ALG2” with ORPHA code 79326 and notes autosomal recessive inheritance and prevalence <1/1,000,000.[8][15] SNOMED CT code 897592003 is referenced in OMIM as an associated clinical concept for the disorder.[7][10] The Disease Ontology (DO) maps congenital disorder of glycosylation type Ii to DOID:0080561.[7] The MONDO ontology, via ClinVar and GenCC, uses MONDO:0011933 for “ALG2-congenital disorder of glycosylation,” linking to MedGen C1842836 and Orphanet 79326.[9][17]

In genetic testing and clinical genetics resources, the condition is linked to MedGen C1842836 and OMIM 607906 in the NCBI Gene and GTR records for *ALG2*, alongside GeneReviews coverage under the umbrella of “Congenital Disorders of N-Linked Glycosylation and Multiple Pathway Overview.”[3][5] ClinVar entries explicitly associate individual *ALG2* variants, such as NM_033087.4:c.92G>C (p.Arg31Pro), with the condition “ALG2-congenital disorder of glycosylation,” using the same MONDO and MedGen identifiers.[17]

For ontology‑based phenotypic mapping, the overarching disease concept aligns with MONDO:0011933 (ALG2-CDG), and the broader class “congenital disorder of glycosylation” corresponds to MONDO:0018993. The disease can be further mapped to NCIT concepts such as NCIT:C123879 (Congenital Disorder of Glycosylation) in oncology and metabolic disease terminologies.

### 1.3 Synonyms and Alternative Names

ALG2-CDG has accrued several synonyms over time, reflecting evolving nomenclature in the CDG field. OMIM and Orphanet list “congenital disorder of glycosylation type Ii,” “CDG-Ii,” “CDG1I,” and “carbohydrate-deficient glycoprotein syndrome type Ii” as alternative names.[2][7][8] The term “alpha-1,3-mannosyltransferase 2 congenital disorder of glycosylation” emphasizes the specific enzymatic defect.[2] Orphanet and CDGHub also refer to “mannosyltransferase 2 deficiency” and “Syndrome CDG type Ii,” highlighting the glycosyltransferase nature of the disease.[2][8] Historically, CDG-Ii corresponded to the patient described by Thiel et al.; in more recent literature, “ALG2-CDG” has become the preferred term to clarify the gene involved.[11][14][16]

At the gene level, *ALG2* is known by several synonyms, including CDG1I, CDGIi, CMS14, NET38, CMSTA3, and hALPG2, as indicated in NCBI Gene and Harmonizome.[3][5][6] CMS14 refers to “myasthenic syndrome, congenital, 14, with tubular aggregates,” the allelic neuromuscular phenotype associated with *ALG2* mutations.[10] In clinical neuromuscular literature, the term “ALG2 congenital myasthenic syndrome (ALG2-CMS)” is commonly used to denote patients whose manifestations are largely confined to fatigable muscle weakness with relatively preserved cognition.[2][12][13]

### 1.4 Nature of Available Information and Evidence Sources

Given its extreme rarity, information on ALG2-CDG is largely derived from individual patients and small case series reported in the medical literature, supplemented by aggregated disease‑level summaries in specialized databases. The seminal description by Thiel et al. in 2003 is based on detailed biochemical and genetic analysis of a single patient.[11] Subsequent reports have added a small number of additional probands, including Argentinian individuals with the homozygous p.Arg251Leu variant, patients with compound heterozygous missense and frameshift variants, and a recent Mexican child with a novel frameshift allele, collectively totaling about 14 documented ALG2-CDG cases worldwide.[7][14][16]

These case reports provide granular clinical, biochemical, and molecular data, including detailed neurologic, ophthalmologic, hepatic, hematologic, and neuromuscular findings, as well as transferrin glycoform profiling and functional studies in patient fibroblasts.[11][14][16] Aggregated disease-level resources such as OMIM, Orphanet, GARD, CDGHub, and ClinGen synthesize and curate these primary observations into consensus descriptions of the phenotype, inheritance pattern, and molecular etiology, but they remain anchored in the limited published case material.[1][2][7][8][9][12]

ClinGen’s Congenital Disorders of Glycosylation Gene Curation Expert Panel evaluated the *ALG2*–ALG2-CDG gene–disease relationship and assigned a “STRONG” classification based on case-level and experimental evidence, citing at least six unique pathogenic variants reported across five probands and supporting biochemical data showing that ALG2 catalyzes the second and third mannosylation steps in N‑linked glycosylation.[9] Thus, while sample sizes are small, the gene–disease association is well validated, and the mechanistic link between ALG2 deficiency and the CDG phenotype is robust.

## 2. Etiology

### 2.1 Primary Causal Factors: Genetic Basis and Mechanism

ALG2-CDG is unequivocally a monogenic, autosomal recessive disorder caused by biallelic loss-of-function variants in the *ALG2* gene, which encodes a GDP‑Man:Man(1)GlcNAc(2)‑PP‑dolichol α1,3-mannosyltransferase essential for early N‑glycan precursor assembly.[2][7][10][11][16] OMIM notes that congenital disorder of glycosylation type Ii is caused by homozygous or compound heterozygous mutation in *ALG2* on chromosome 9q22.[7] NCBI Gene similarly states that defects in *ALG2* “have been associated with congenital disorder of glycosylation type Ih (CDG-Ii),” identifying the protein as an alpha‑1,3‑mannosyltransferase that mannosylates Man(2)GlcNAc(2)-dolichol diphosphate and Man(1)GlcNAc(2)-dolichol diphosphate.[3][5]

Functionally, human ALG2 catalyzes the transfer of mannose residues from GDP‑mannose to Man\(_1\)GlcNAc\(_2\)‑PP‑dolichol and Man\(_2\)GlcNAc\(_2\)‑PP‑dolichol, forming Man\(_3\)GlcNAc\(_2\)‑PP‑dolichol and enabling further extension of the lipid‑linked oligosaccharide (LLO) that will become the core N‑linked glycan.[11][18] Thiel et al. showed that in fibroblasts from their patient, there was marked accumulation of Man\(_1\)GlcNAc\(_2\) and Man\(_2\)GlcNAc\(_2\) dolichol‑linked intermediates, along with severely reduced mannosyltransferase activity when extracts were incubated with GDP‑mannose and Man\(_1\)GlcNAc\(_2\)‑PP‑dolichol.[11] Expression of wild‑type hALG2 cDNA in these fibroblasts restored mannosyltransferase activity and LLO biosynthesis, firmly establishing ALG2 deficiency as the primary biochemical lesion.[11]

More recent biochemical and glycophenotypic studies of ALG2-CDG patients reinforce this mechanism. ALG2-CDG serum transferrin profiling reveals mild type I CDG patterns and characteristic increases in hyposialylated biantennary and triantennary N‑glycans, as well as generalized increased fucosylation of serum glycoproteins.[14][16] Alcántara‑Ortigoza et al. and Papazoglu et al. detailed the serum glycophenotype of Argentine ALG2-CDG patients with the p.Arg251Leu variant, showing reduced Alg2 protein expression and lower glycan levels compared to wild‑type controls across tissues, consistent with loss-of-function.[16] These findings confirm that *ALG2* variants act through a loss-of-function mechanism producing hypoglycosylation, rather than gain-of-function or dominant negative effects.

### 2.2 Risk Factors: Genetic

Because ALG2-CDG is autosomal recessive and exceedingly rare, the primary risk factor is inheriting two pathogenic alleles in *ALG2*, one from each parent. Carriers (heterozygous individuals) are reported to be clinically unaffected, and no dominant phenotype has been associated with heterozygous *ALG2* variants.[9][10][11][14][16] The disease mechanism appears to be biallelic loss-of-function; ClinGen explicitly notes that heterozygous carriers are reportedly unaffected and that no convincing evidence contradicts the gene–disease relationship.[9]

Several pathogenic or likely pathogenic *ALG2* variants have been documented. Thiel et al. identified compound heterozygous mutations consisting of a 1‑bp deletion and a 1‑bp substitution in hALG2, both predicted to disrupt the protein and abolish activity.[11][10] Papazoglu et al. and later Alcántara‑Ortigoza et al. described a homozygous missense variant c.752G>T; p.Arg251Leu, which is classified as pathogenic in ClinVar (ID 1676197, dbSNP rs201729325) and is of germline origin.[7][16] A recent case report from Mexico identified a novel frameshift variant c.1055_1056delinsTGA p.(Ser352Leufs*3) in compound heterozygosity with a missense variant of uncertain significance c.964C>A p.(Pro322Thr); glycan profiling supported the pathogenicity of the frameshift and implicated the missense variant.[4][14] ClinVar also lists NM_033087.4:c.92G>C (p.Arg31Pro) as pathogenic or likely pathogenic for ALG2-CDG, associated with MONDO:0011933 and OMIM 607906.[17]

There is suggestive evidence of founder effects or population clustering for some variants, particularly Arg251Leu in Argentine families, where three patients (including a sib pair) from unrelated families shared this homozygous missense allele.[7][16] This pattern implies increased carrier frequency in certain populations with high consanguinity or geographic isolation, although robust population-based data are lacking. In gnomAD and other population databases, *ALG2* pathogenic alleles appear at extremely low minor allele frequencies, consistent with an ultra‑rare recessive disorder, but specific frequency values for each variant were not provided in the immediate search results.

Beyond classic ALG2-CDG, mutations in *ALG2* also cause congenital myasthenic syndrome type 14 (CMS14), a neuromuscular junction disorder characterized by fatigable muscle weakness and often tubular aggregates on muscle biopsy.[10][13] In CMS14, missense variants such as p.Val68Gly were shown to markedly reduce ALG2 expression in muscle cells, impairing acetylcholine receptor (AChR) subunit glycosylation and assembly.[6][10][13] While CMS14 is genetically allelic to ALG2-CDG, patients may lack the full multisystem CDG phenotype, underscoring phenotypic variability rather than distinct risk factors.

### 2.3 Risk Factors: Environmental, Lifestyle, and Other Non-genetic Influences

No environmental, occupational, lifestyle, infectious, or other non-genetic risk factors have been identified as causative or contributory to ALG2-CDG. The disease arises in the context of inherited germline variants present from conception, and clinical manifestations begin in the neonatal or early infancy period, consistent with a primary genetic developmental disorder.[1][2][7][8][11][12][14][16] Major CDG reviews emphasize that these disorders are monogenic and typically autosomal recessive, with multi‑system manifestations but no known environmental triggers.[12]

While general health behaviors, nutrition, and avoidance of toxins may modify overall disease course or susceptibility to complications (for example, reducing infection risk or supporting growth), there is no evidence that they influence the underlying glycosylation defect or primary risk of disease onset. Thus, environmental and lifestyle factors are best considered in the domain of clinical management and prognosis rather than etiologic risk.

### 2.4 Protective Factors and Gene–Environment Interactions

At present, no specific genetic protective variants or modifier alleles have been identified that reliably attenuate or prevent ALG2-CDG in individuals carrying biallelic pathogenic *ALG2* variants. Likewise, no protective environmental exposures or lifestyle factors are known to mitigate the core glycosylation defect. Given the small number of documented ALG2-CDG patients, studies of modifier genes or gene–environment interactions have not been feasible, and the existing clinical data do not suggest substantial variation in disease penetrance among individuals with bona fide loss-of-function alleles.[7][9][11][14][16]

For the allelic CMS14 phenotype, some variability in severity has been observed, and there is speculative discussion about other components of the neuromuscular junction glycosylation machinery (such as *ALG14*, *DPAGT1*, or *GFPT1*) acting as modifiers, but direct evidence in ALG2 patients is limited.[12][13] More broadly, CDG reviews note that differences in tissue‑specific glycosylation profiles and compensatory pathways may shape organ involvement and clinical features, suggesting that subtle genetic and epigenetic variation in glycosylation networks could modulate expressivity.[12][16] However, these ideas remain inferential rather than demonstrated for ALG2-CDG.

Given the purely genetic origin and early onset of ALG2-CDG, gene–environment interactions are not thought to play a major role in disease causation. Standard supportive practices (vaccination, infection control, nutritional support) may alter morbidity and mortality, but they do not prevent or reverse the underlying defect in N‑glycan biosynthesis.

## 3. Phenotypes

### 3.1 Overall Phenotypic Landscape and Age of Onset

ALG2-CDG presents as a multisystem disorder in which neurologic, ophthalmologic, neuromuscular, hepatic, coagulation, and developmental abnormalities coexist.[1][2][7][8][11][12][14][16] Almost all reported patients developed symptoms in the neonatal period or early infancy, although some were noted to be clinically normal at birth and then manifested signs during the first year of life.[1][2][8][11][14] Thiel’s original patient was described as normal at birth, but within the first year developed mental retardation, seizures, iris coloboma, hypomyelination, hepatomegaly, and coagulation abnormalities.[11] Orphanet similarly states that symptoms appear in “petite enfance, néonatal,” capturing this early onset.[8]

In the recent Mexican ALG2-CDG case, the child exhibited perinatal asphyxia, muscular weakness, feeding difficulties due to absent sucking reflex, congenital hip dislocation, and hypotonia from birth, followed by inspiratory stridor, gastroesophageal reflux, recurrent seizures, respiratory infections, inability to hold the head upright, and global developmental delay over time.[4][14] CDGHub emphasizes that symptoms typically begin in infancy, though they may not be present at birth.[2] Thus, the typical age of onset is congenital or within the first months of life, with some variability in which features emerge first.

The phenotype severity ranges from severe global impairment with multi‑organ involvement to milder neuromuscular presentations in ALG2-CMS. In the compiled series up to 2024, intellectual disability/global developmental delay was reported in 11 of 15 ALG2-CDG patients (including the Mexican case), seizures in 5 of 15, hypotonia in most, ophthalmologic anomalies such as coloboma or cataracts in several, and neuromuscular fatigability in those with CMS.[14][16] Overall, symptom severity is often moderate to severe, with progressive developmental impact but variable progression of specific organ manifestations.

### 3.2 Neurologic and Developmental Phenotypes

Neurologic and neurodevelopmental features are central to ALG2-CDG. The most consistent manifestations are global developmental delay and intellectual disability, hypotonia, and seizures or infantile spasms.[7][8][11][12][14][16] Thiel’s patient had mental retardation and seizures as part of a multisystem disorder, with hypomyelination documented on neuroimaging.[11] Orphanet lists infantile spasms and developmental delay as characteristic features, emphasizing early onset.[8] In the Mexican case, global developmental delay became evident as the child failed to achieve motor milestones, including holding the head upright, and displayed recurrent seizures.[4][14]

Global developmental delay and intellectual disability correspond to HPO terms HP:0001263 (global developmental delay) and HP:0001249 (intellectual disability). Based on compiled case data, intellectual disability or global developmental delay was present in roughly 73% (11/15) of reported patients.[14] Hypotonia, usually axial and generalized, aligns with HP:0001290 (generalized hypotonia) and was nearly universal in described cases, from neonatal “floppy baby” presentations to persistent low muscle tone in infancy.[2][11][14][16] Seizures, including infantile spasms, align with HP:0001250 (seizure) and HP:0012469 (infantile spasms). These were present in about one‑third of patients (5/15) in the series, though they feature prominently in Orphanet’s definition and may be underreported.[8][11][14]

Neuromuscular junction involvement is particularly salient in ALG2-CMS, where fatigable muscle weakness, ptosis, ophthalmoparesis, and respiratory crises can occur, often responsive to acetylcholinesterase inhibitors.[2][12][13] This phenotype corresponds to HP:0003701 (fatigable weakness), HP:0000508 (ptosis), and HP:0000490 (ophthalmoparesis). Cossins et al. showed that ALG2 mutations in CMS patients lead to impaired AChR subunit glycosylation and reduced receptor surface expression, confirming a mechanistic basis for neuromuscular symptoms.[13] In combined ALG2-CDG/ALG2-CMS presentations, neuromuscular involvement compounds overall disability, particularly affecting motor function and respiratory capacity.

Quality of life impact from neurologic and developmental phenotypes is profound. Intellectual disability and global developmental delay impair education, communication, and independence, often necessitating lifelong supportive care. Hypotonia and fatigable weakness limit mobility and daily functioning, increase risk of falls and orthopedic complications, and can compromise respiratory function. Seizures and infantile spasms add further morbidity, with risks of status epilepticus, developmental regression, and neurocognitive impairment. From an EQ‑5D or SF‑36 perspective, these features severely affect domains of mobility, self‑care, usual activities, pain/discomfort (due to procedures and complications), and anxiety/depression in caregivers.

Suggested HPO terms for neurologic and developmental phenotypes include HP:0001263 (global developmental delay), HP:0001249 (intellectual disability), HP:0001290 (hypotonia), HP:0001250 (seizures), HP:0012469 (infantile spasms), HP:0003701 (fatigable weakness), HP:0000508 (ptosis), HP:0000490 (ophthalmoparesis), HP:0001270 (motor delay), and HP:0002063 (hypomyelination) reflecting neuroimaging findings.[7][11][14][16]

### 3.3 Ophthalmologic Phenotypes

Ophthalmologic anomalies are characteristic of ALG2-CDG, particularly iris coloboma and congenital cataracts. Thiel’s original patient had coloboma of the iris, a structural defect in the anterior segment of the eye.[11] Orphanet’s disease definition prominently lists “colobome de l’iris” and “cataracte” as key features.[8] Iris coloboma corresponds to HP:0000514 (coloboma of iris), and congenital cataract aligns with HP:0000519 (cataract).

In the compiled literature, several ALG2-CDG patients have reported structural eye anomalies, although exact frequencies are less well quantified than neurologic features.[7][8][11][14][16] CDGHub notes “ophthalmological problems” as a core component of the severe presentation.[2] Alg2-CMS patients may also display ophthalmologic signs, particularly ptosis and ophthalmoparesis, reflecting neuromuscular involvement rather than structural anomalies.[13]

The impact on quality of life depends on severity. Iris coloboma may cause photophobia, reduced visual acuity, and cosmetic concerns, influencing activities of daily living and social interaction. Cataracts can lead to significant visual impairment, requiring surgical intervention where feasible. Combined with neurologic disability, ophthalmologic problems further limit communication, exploration, and learning in affected children.

Suggested HPO terms for ophthalmologic phenotypes include HP:0000514 (coloboma of iris), HP:0000519 (cataract), HP:0000508 (ptosis), HP:0000490 (ophthalmoparesis), and HP:0000479 (abnormality of the anterior segment of the eye).[8][11][13][14]

### 3.4 Hepatic, Coagulation, and Gastrointestinal Phenotypes

Hepatic involvement and coagulation abnormalities are well documented in ALG2-CDG and mirror those seen in other N‑linked CDG subtypes.[7][8][11][12][16] Thiel’s patient had hepatomegaly and coagulation abnormalities as part of the multisystem presentation.[11] OMIM and Orphanet emphasize “anomalie des facteurs de coagulation” and coagulopathy as characteristic features.[7][8] These manifestations correspond to HPO terms HP:0002240 (hepatomegaly) and HP:0001928 (abnormal coagulation).

CDGHub lists “abnormal coagulation factors” and notes that general CDG presentations often include coagulopathy and hepatopathy, including elevated transaminases, protein‑losing enteropathy, diarrhea, failure to thrive, and hypoalbuminemia.[2][12] In ALG2-CDG specifically, the Mexican patient developed gastroesophageal reflux (HP:0002019), low intake (feeding difficulties; HP:0011968), and recurrent respiratory infections likely related to aspiration and overall vulnerability.[4][14] These features illustrate how hepatic and gastrointestinal dysfunction interact with neuromuscular and neurologic deficits to produce complex clinical challenges.

Coagulopathy in CDG often manifests as a combined deficiency of multiple coagulation factors and natural anticoagulants, leading to bleeding tendencies or thrombosis.[12] While detailed factor levels are not provided in the ALG2-CDG case summaries, Orphanet’s emphasis suggests that similar patterns occur, impacting both quality of life and safety. Hepatomegaly and hepatopathy can produce abdominal discomfort, risk of portal hypertension, and metabolic instability.

Suggested HPO terms include HP:0002240 (hepatomegaly), HP:0001928 (abnormal coagulation), HP:0002019 (gastroesophageal reflux), HP:0011968 (feeding difficulties), HP:0001508 (failure to thrive), and HP:0003118 (hypoalbuminemia) where documented.[2][8][11][12][14][16]

### 3.5 Musculoskeletal, Orthopedic, and Dysmorphic Phenotypes

Musculoskeletal and orthopedic anomalies, as well as distinctive facial morphology, are reported in ALG2-CDG. The Mexican patient had congenital hip dislocation, corresponding to HP:0003285 (congenital dislocation of the hip), and an inability to maintain the head upright due to hypotonia and muscle weakness.[4][14] CDGHub and GARD note low muscle tone and fatigue, aligning with HP:0001290 (hypotonia) and HP:0003401 (easy fatigability).[1][2] Dysmorphic facial features are repeatedly mentioned: GARD describes “an abnormal morphology (form) of the face or its components,” synonymous with “facial dysmorphism” or “distinctive facies.”[1] This corresponds to HP:0001999 (facial dysmorphism).

In broader CDG cohorts, skeletal abnormalities, including kyphoscoliosis, osteopenia, and skeletal dysplasia, are common.[12] While specific skeletal details for ALG2-CDG are limited, the presence of congenital hip dislocation suggests that connective tissue and musculoskeletal development can be affected, likely reflecting altered glycosylation of structural proteins and signaling molecules.

From a quality of life perspective, orthopedic issues impair mobility, cause pain, and may require surgical intervention. Dysmorphic facial features can influence social integration and self‑image, though in young children the impact is largely mediated through caregiver perceptions. Combined with hypotonia and neuromuscular weakness, musculoskeletal anomalies significantly constrain gross motor function.

Suggested HPO terms include HP:0003285 (congenital dislocation of the hip), HP:0001999 (facial dysmorphism), HP:0001290 (hypotonia), HP:0001270 (motor delay), and HP:0001370 (skeletal dysplasia) where broader CDG features are extrapolated.[1][2][12][14][16]

### 3.6 Respiratory and Other Systemic Phenotypes

Respiratory involvement in ALG2-CDG arises from multiple mechanisms: neuromuscular weakness affecting respiratory muscles, structural airway issues, aspiration due to feeding difficulties and reflux, and increased susceptibility to infections. The Mexican patient experienced inspiratory stridor (HP:0001615), recurrent respiratory infections (HP:0002205), and feeding difficulties with absent sucking reflex, all contributing to respiratory compromise.[4][14] In ALG2-CMS patients, respiratory crises during acute illness or stress have been described, tied to fatigable weakness of the diaphragm and accessory muscles.[13]

General CDG reviews highlight recurrent infections, particularly respiratory, as common complications due to combined neuromuscular and immune or structural factors.[12] While immunologic defects per se have not been highlighted in ALG2-CDG, the combination of hypotonia, reflux, and coagulopathy may predispose to severe pneumonia and respiratory distress.

Other systemic features include poor growth and failure to thrive (HP:0001508), as common across CDG subtypes, and endocrine or cardiac manifestations in some N‑linked CDG, though specific cardiac involvement in ALG2-CDG has not been prominent in the limited case data.[12][16] Quality of life effects include frequent hospitalizations, need for respiratory support, and constraints on activity levels.

Suggested HPO terms include HP:0001615 (stridor), HP:0002205 (recurrent respiratory infections), HP:0002019 (gastroesophageal reflux), HP:0001508 (failure to thrive), and HP:0001744 (respiratory muscle weakness).[4][12][14][16]

### 3.7 Phenotype Progression and Variability

Phenotype progression in ALG2-CDG appears to be chronic and often progressive in terms of developmental impact, but specific organ involvement may be relatively stable or fluctuate. Thiel’s patient developed multisystem features during the first year of life, with mental and motor regression noted, suggesting a trajectory of initial normal development followed by deterioration.[11] In the Mexican case, neurologic and neuromuscular features worsened over time, with new seizures, poor head control, and increased respiratory complications.[4][14] However, some aspects, such as structural eye anomalies, are fixed developmental defects rather than progressive lesions.

Expressivity is clearly variable, particularly when comparing classic multisystem ALG2-CDG with allelic ALG2-CMS, where neuromuscular features dominate and central neurologic involvement may be milder.[2][10][13][16] Some patients have severe cognitive impairment and seizures, while others have only mild developmental delay. This variability likely reflects differences in variant type, residual ALG2 activity, tissue‑specific glycosylation, and possibly other genetic modifiers.

Remission of core phenotypes is uncommon; developmental and structural abnormalities are permanent. However, seizures may be controlled with antiepileptic therapy, and neuromuscular symptoms can improve with acetylcholinesterase inhibitors, representing treatment‑induced modulation rather than disease remission.[2][12][13][14][16] The overall disease course is chronic and lifelong, with fluctuating symptom burden depending on management and intercurrent illnesses.

## 4. Genetic and Molecular Information

### 4.1 Causal Gene: *ALG2* (HGNC: ALG2)

The causal gene for ALG2-CDG is *ALG2*, officially approved by HGNC with symbol ALG2 and full name “ALG2, alpha-1,3/1,6-mannosyltransferase.”[3][5][10] NCBI Gene describes ALG2 as encoding “a member of the glycosyltransferase 1 family” that acts as an alpha‑1,3‑mannosyltransferase, mannosylating Man(2)GlcNAc(2)-dolichol diphosphate and Man(1)GlcNAc(2)-dolichol diphosphate to form Man(3)GlcNAc(2)-dolichol diphosphate.[3][5] The gene is located on chromosome 9q22.33 (GRCh38 coordinates 9:99,216,425–99,221,942, complement), with multiple transcript variants generated by alternative splicing.[3][5][10]

OMIM’s gene entry (607905) summarizes that ALG2 encodes an alpha‑1,3-mannosyltransferase catalyzing the second and third mannosylation steps in the N‑linked glycosylation pathway.[10] Genomic mapping places the locus at 9q22.33, though some older resources, including Orphanet and GARD, cite 9q31.1 or 9q31.1, likely reflecting previous cytogenetic coordinates.[1][8][10] The functional protein resides in the ER membrane and participates early in N‑glycan precursor assembly.

ALG2 has multiple synonyms, including CDG1I, CDGIi, CMS14, NET38, CMSTA3, hALPG2, and HALPG2.[3][5][6][10] CMS14 refers to an allelic phenotype, “myasthenic syndrome, congenital, 14, with tubular aggregates” (OMIM 616228), emphasizing the neuromuscular junction involvement.[10] Harmonizome notes that ALG2 has thousands of functional associations across diseases, phenotypes, and cellular pathways, reflecting its central role in glycosylation.[6]

### 4.2 Pathogenic Variants: Types, Classification, and Functional Consequences

A small but diverse set of pathogenic *ALG2* variants has been reported in ALG2-CDG patients. Thiel et al. identified compound heterozygous mutations in the patient designated as CDG-Ii, consisting of a one‑base deletion and a one‑base substitution in the human ortholog of yeast ALG2; these variants severely reduced mannosyltransferase activity and LLO biosynthesis in patient fibroblasts, and expression of wild‑type hALG2 rescued the defect.[11][10] These variants are classified as loss-of-function, likely frameshift/nonsense or severe missense, producing truncated or nonfunctional protein.

Papazoglu et al. reported a homozygous missense variant c.752G>T; p.Arg251Leu in three patients from two Argentinian families, associated with multisystem ALG2-CDG.[7][16] Alcántara‑Ortigoza et al. further characterized this variant, demonstrating reduced ALG2 protein expression and lower glycan levels compared to wild‑type controls in patient samples and cell models.[16] The missense variant is pathogenic and of germline origin, as noted in ClinVar (ID 1676197).[16] ClinGen cites this variant as one of at least six unique pathogenic *ALG2* alleles reported.[9]

A 2024 case report described two *ALG2* variants in compound heterozygosity in a Mexican child: a novel frameshift variant c.1055_1056delinsTGA p.(Ser352Leufs*3), and a missense variant of uncertain significance c.964C>A p.(Pro322Thr).[4][14] Glycan profiling and detection of a specific heptasaccharide biomarker confirmed ALG2-CDG and supported the pathogenicity of the combination, with the frameshift variant strongly implicated as loss-of-function.[4][14] ClinVar also lists NM_033087.4:c.92G>C (p.Arg31Pro) as associated with ALG2-congenital disorder of glycosylation, classified as pathogenic or likely pathogenic for multiple conditions.[17] Other reported variants include missense changes affecting conserved residues and indels that disrupt ALG2’s catalytic domain.[9][11][16]

Variant types include missense, frameshift (small deletions/insertions), and single nucleotide substitutions, including nonsense mutations. Most are germline, present in all tissues, and inherited in autosomal recessive fashion; somatic *ALG2* variants have not been implicated in disease. All documented ALG2-CDG variants act by loss-of-function, either reducing or abolishing enzymatic activity, leading to incomplete LLO assembly and hypoglycosylation.[2][9][11][14][16] In CMS14, missense variants such as p.Val68Gly reduce ALG2 expression in muscle and impair AChR glycosylation, again representing loss-of-function, though with more restricted phenotypic consequences.[6][10][13]

From an ACMG/AMP classification standpoint, pathogenicity is supported by functional studies (rescue by wild‑type cDNA, reduced protein expression, altered glycan profiles), segregation in affected families, absence or extremely low frequency in general population databases, and strong gene–disease specificity. Variants like p.Arg251Leu and the Thiel compound heterozygous alleles meet criteria for pathogenic; frameshift variants such as p.Ser352Leufs*3 are predicted to be null alleles with severe impact, classified as pathogenic. Some missense variants, like p.Pro322Thr, initially labeled as VUS, gain evidence for likely pathogenicity when combined with biochemical markers and clinical phenotype.[4][14][16]

### 4.3 Modifier Genes, Epigenetic Information, and Chromosomal Abnormalities

Specific modifier genes influencing ALG2-CDG severity have not been systematically identified. However, the broader network of N‑glycosylation genes, including *ALG14*, *DPAGT1*, *GFPT1*, and others, is known to harbor variants causing related CDG and CMS phenotypes, and subtle differences in these pathways may modulate tissue‑specific glycosylation and clinical expression.[12][13][18] In CDG, tissue‑specific glycosylation patterns and alternative pathway usage can shape organ involvement, suggesting a complex genotype–phenotype landscape, but direct evidence for modifiers in ALG2-CDG is limited by the small number of cases.[12][16]

Epigenetic information specific to ALG2-CDG has not been reported. No studies have detailed DNA methylation, histone modifications, or chromatin changes directly affecting *ALG2* expression in human patients. Given the congenital, germline nature of the disorder and the fact that pathogenic variants reduce enzyme function regardless of epigenetic regulation, epigenetic mechanisms are unlikely to be primary drivers, though they might influence residual expression of wild-type alleles in carriers or modulate broader glycosylation machinery.

Large-scale chromosomal abnormalities involving the *ALG2* locus (9q22.33) have not been implicated in ALG2-CDG. DECIPHER and structural variant databases do not highlight recurrent deletions or rearrangements affecting *ALG2* as a cause of CDG, and all reported cases involve sequence-level variants (missense, frameshift, indel) rather than copy number changes.[7][9][10][11][16] Thus, chromosomal aneuploidy or translocations are not typical etiologic factors.

### 4.4 Gene Ontology and Molecular Pathways

ALG2’s role is best captured by specific Gene Ontology (GO) terms and pathway annotations. At the biological process level, ALG2 participates in “protein N-linked glycosylation” (GO:0006487) and “dolichol-linked oligosaccharide biosynthetic process” (GO:0006488), representing key steps in assembling the Glc\(_3\)Man\(_9\)GlcNAc\(_2\) precursor.[11][18] At the molecular function level, ALG2 is a “GDP-mannose:Man(1)GlcNAc(2)-PP-dolichol alpha‑1,3-mannosyltransferase” (GO:0042285), catalyzing the transfer of mannose from GDP‑mannose (CHEBI:17646) to the growing oligosaccharide.[11][18] Cellular component terms include “endoplasmic reticulum membrane” (GO:0005789) and specifically the cytosolic side of the ER, where early N‑glycan assembly occurs.[11][18]

KEGG’s N‑glycan biosynthesis pathway (sce00510 in yeast, with YGL065C as the orthologous ALG2) shows that biosynthesis begins with transfer of GlcNAc from UDP‑GlcNAc (CHEBI:15996) to dolichol phosphate (CHEBI:27112), followed by sequential monosaccharide additions by ALG glycosyltransferases, including ALG2.[18] Defects in N‑glycan biosynthesis lead to human CDG, including ALG2-CDG.[12][18] This pathway mapping underscores ALG2’s position as an early, essential mannosyltransferase whose failure halts proper LLO formation and disrupts subsequent oligosaccharyltransferase (OST)-mediated glycan transfer to proteins.

Reactome and other pathway resources similarly place ALG2 within ER glycosylation cascades, with upstream inputs including GDP‑mannose synthesis and downstream effects on glycoprotein folding, ER quality control, and trafficking. This network provides a mechanistic framework for understanding how ALG2 defects can impact diverse tissues and systems that depend on properly glycosylated receptors, enzymes, adhesion molecules, and structural proteins.

## 5. Environmental Information

### 5.1 Environmental, Lifestyle, and Infectious Factors

As noted in the etiology section, ALG2-CDG is a purely genetic disorder with no known environmental, lifestyle, or infectious etiologic factors. No data link toxins, radiation, pollutants, occupational exposures, diet, smoking, alcohol, or specific infections to increased incidence of ALG2-CDG.[1][2][7][8][11][12][14][16] CDG overall is regarded as a group of monogenic metabolic diseases rather than environmentally induced conditions.[12] There is likewise no evidence of infectious agents, such as bacteria, viruses, fungi, or parasites, directly triggering ALG2-CDG or mimicking its core glycosylation defect.

In clinical management, standard public health measures, including vaccination (NCIT:C258), infection control, and good nutrition, are important to prevent complications in affected individuals but they do not modify the primary disorder. Lifestyle factors such as physical activity, smoking avoidance, and balanced diet may influence general health and morbidity but are not specific risk or protective factors.

### 5.2 Gene–Environment Considerations in Clinical Care

While gene–environment interactions do not influence disease onset, they may play a role in disease course. For example, respiratory infections can precipitate neuromuscular crises in ALG2-CMS patients, necessitating careful infection prevention and rapid treatment.[12][13] Nutritional status can affect growth and resilience in ALG2-CDG children who already have failure to thrive and feeding difficulties.[2][4][14][16] Certain medications that stress the neuromuscular junction or the coagulation system may exacerbate symptoms.

From an ontology standpoint, relevant environmental terms could include ENVO (Environment Ontology) concepts for infection exposure and CHEBI chemicals representing supportive drugs or toxins, but their involvement is secondary. Overall, the core pathophysiology remains driven by inherited *ALG2* loss-of-function, with environment shaping context but not cause.

## 6. Mechanism and Pathophysiology

### 6.1 Ordered Causal Chain from Mutation to Clinical Manifestation

In ALG2-CDG, the causal cascade can be summarized as follows in narrative sequence. First, biallelic pathogenic variants in the *ALG2* gene lead to reduced or absent activity of the ALG2 α1,3‑mannosyltransferase in the endoplasmic reticulum, representing a germline loss-of-function lesion demonstrated by fibroblast and cell model studies.[7][9][11][16] Second, decreased ALG2 activity results in impaired transfer of mannose from GDP‑mannose to Man\(_1\)GlcNAc\(_2\)‑PP‑dolichol and Man\(_2\)GlcNAc\(_2\)‑PP‑dolichol, causing accumulation of truncated LLO intermediates and incomplete synthesis of the canonical Man\(_3\)GlcNAc\(_2\) precursor; this step is directly demonstrated by Thiel et al. and subsequent glycophenotypic analyses.[11][16][18] Third, incomplete LLO assembly leads to reduced efficiency and quality of N‑glycan transfer by the OST complex onto nascent polypeptides, resulting in generalized hypoglycosylation (type I CDG pattern) and altered glycan structures, including increased hyposialylation and fucosylation of serum glycoproteins; these changes are shown by transferrin IEF/mass spectrometry and glycoprotein analyses.[12][14][16] Fourth, hypoglycosylated glycoproteins exhibit impaired folding, stability, trafficking, and function in diverse cell types, affecting receptors, adhesion molecules, coagulation factors, enzymes, and structural proteins; this step is inferred from general CDG biology and supported by specific studies on acetylcholine receptor assembly in ALG2-CMS.[12][13][16] Fifth, tissue- and cell‑specific consequences of glycoprotein dysfunction manifest clinically as multi‑system phenotypes: in the central nervous system, defective glycosylation of cell surface receptors and adhesion molecules leads to abnormal myelination, synaptic function, and neuronal development, resulting in hypotonia, developmental delay, seizures, and hypomyelination; in the neuromuscular junction, impaired AChR glycosylation leads to decreased receptor density and fatigable muscle weakness; in the liver and coagulation system, hypoglycosylated coagulation factors and glycoproteins contribute to hepatomegaly and coagulopathy; in the eye, disrupted glycoprotein signaling during development leads to iris coloboma and cataracts.[7][8][11][12][13][14][16] Finally, these organ‑level defects culminate in the clinical syndrome of ALG2-CDG, characterized by multi‑system involvement, chronic morbidity, and variable but often significant impacts on growth, development, and survival.

### 6.2 Molecular Pathways and Biochemical Abnormalities

The core molecular pathway affected in ALG2-CDG is N‑linked glycan biosynthesis in the ER, specifically the early steps of dolichol‑linked oligosaccharide assembly. The canonical precursor for N‑linked glycosylation is Glc\(_3\)Man\(_9\)GlcNAc\(_2\), built on a dolichol pyrophosphate carrier through sequential addition of monosaccharides.[11][12][18] In Saccharomyces cerevisiae, biosynthesis begins with transferase reactions involving UDP‑GlcNAc and dolichol phosphate to generate GlcNAc\(_1\)‑PP‑dolichol, followed by addition of GlcNAc and mannose residues by ALG glycosyltransferases such as ALG1, ALG2, ALG11, and others.[18] Human ALG2 is the ortholog of yeast YGL065C (ALG2), functioning as GDP‑Man:Man(1)GlcNAc(2)-PP‑dolichol alpha‑1,3-mannosyltransferase.[11][18]

Thiel et al. demonstrated that deficiency of GDP‑Man:Man\(_1\)GlcNAc\(_2\)-PP‑dolichol mannosyltransferase (hALG2) in their patient caused a new type of CDG, with accumulation of Man\(_1\)GlcNAc\(_2\)-PP‑dolichol and Man\(_2\)GlcNAc\(_2\)-PP‑dolichol in skin fibroblasts.[11] Their biochemical assays showed severely reduced activity of this mannosyltransferase when patient fibroblast extracts were incubated with Man\(_1\)GlcNAc\(_2\)-PP‑dolichol and GDP‑mannose, and expression of wild‑type hALG2 cDNA restored both mannosyltransferase activity and dolichol-linked oligosaccharide biosynthesis.[11] These findings establish ALG2 deficiency as the first defect of a glycosyltransferase catalyzing transfer of monosaccharide residues from a nucleotide sugar donor onto the nascent LLO chain at the cytosolic side of the ER.[7][11]

Subsequent glycophenotypic studies in ALG2-CDG patients, including Arg251Leu homozygotes and the Mexican child, revealed characteristic patterns. Mass spectrometry of serum transferrin showed mild type I CDG profiles with increased hyposialylated biantennary and triantennary N‑glycans and generalized increased fucosylation of serum glycoproteins.[14][16] An abnormal transferrin glycoform containing a linear heptasaccharide consisting of one sialic acid, one galactose, one N‑acetylglucosamine, two mannoses, and two N‑acetylglucosamines (NeuAc‑Gal‑GlcNAc‑Man\(_2\)‑GlcNAc\(_2\)) emerged as a specific diagnostic biomarker of ALG2-CDG.[4][14] This unusual glycan, present in transferrin and other plasma glycoproteins, reflects the altered LLO biosynthesis and downstream glycan remodeling peculiar to ALG2 deficiency.[4][14][16]

Biochemically, these glycan abnormalities indicate that incomplete LLO precursors still enter the glycosylation pathway, creating aberrant N‑glycans attached to proteins, with reduced sialylation and altered branching. Hypoglycosylation can impair protein folding via calnexin/calreticulin cycles, trigger ER stress, and alter trafficking. Specific glycoproteins, such as coagulation factors, AChR subunits, and cell adhesion molecules, may be particularly sensitive to these changes, leading to functional deficits.

The primary biochemical abnormality is thus enzyme deficiency of ALG2 (EC 2.4.1.132), causing defective LLO synthesis and generalized N‑glycoprotein hypoglycosylation. Upstream of this, GDP‑mannose synthesis and transport must be intact; downstream, OST and Golgi glycosyltransferases act on altered substrates, further shaping glycan patterns. No evidence suggests involvement of canonical signaling pathways like Wnt, MAPK, or mTOR in primary pathogenesis, though such pathways may be secondarily affected by glycosylation status of receptors.

### 6.3 Cellular Processes: ER Function, Protein Processing, and Neuromuscular Junction

At the cellular level, ALG2-CDG disrupts several processes. First, ER glycosylation and protein quality control are perturbed. N‑linked glycosylation is critical for proper folding of many secretory and membrane proteins; altered glycan structures can lead to misfolding, retention in the ER, or degradation via ER‑associated degradation (ERAD).[12] In ALG2-CDG, hypoglycosylation and abnormal glycans likely increase ER stress and activate unfolded protein response (UPR) pathways, though direct measurements in patient cells have been limited.[11][16] These processes can influence cell survival, differentiation, and function across tissues.

Second, cells in the central nervous system and neuromuscular junction are particularly vulnerable. Engel and colleagues pioneered the concept that neuromuscular junction glycosylation defects underlie certain CMS, including those due to *ALG2* mutations.[12][13] Cossins et al. showed that ALG2 and ALG14 mutations lead to reduced N‑linked glycosylation of AChR subunits, impairing assembly and resulting in fewer receptors on the muscle cell surface.[13] This leads to decreased synaptic transmission and fatigable weakness. This mechanism corresponds to GO processes such as “synaptic transmission, cholinergic” (GO:0007271) and “neuromuscular junction development” (GO:0007528). In ALG2-CDG, similar defects may affect central synapses and axonal myelination, contributing to hypotonia, seizures, and neurodevelopmental delay.

Third, hepatic cells and endothelial cells in the coagulation cascade rely heavily on glycosylated proteins. Hypoglycosylated coagulation factors may be less stable or functional, resulting in coagulopathy.[12] Hepatocytes producing glycoprotein hormones and transport proteins may also exhibit dysfunction, leading to hepatomegaly and metabolic disturbances.[11][12][16] GO terms such as “blood coagulation” (GO:0007596) and “protein secretion” (GO:0009306) reflect these processes.

Cell types involved span CL terms such as CL:0000540 (hepatocyte), CL:0000066 (neuron), CL:0000565 (skeletal muscle cell), CL:0000097 (Schwann cell), and CL:0000317 (endothelial cell), all reliant on proper N‑glycosylation for their secretory and membrane protein repertoire.[12][16][18] In each case, ALG2 deficiency impairs glycoprotein function, leading to cell‑type specific pathophysiology.

### 6.4 Metabolic Changes and Systemic Physiology

Metabolically, ALG2-CDG impacts glycan synthesis but may secondarily affect other metabolic pathways. Accumulation of truncated LLO intermediates (Man\(_1\)GlcNAc\(_2\)‑PP‑dolichol, Man\(_2\)GlcNAc\(_2\)‑PP‑dolichol) may alter dolichol phosphate turnover and GDP‑mannose utilization, subtlely impacting lipid metabolism and nucleotide sugar pools.[11][18] General CDG disorders often show abnormalities in serum lipids, hormones, and metabolic parameters, though specific data on ALG2-CDG are limited.[12][16]

From a systemic physiology perspective, growth failure, failure to thrive, and muscle weakness reflect both metabolic and structural consequences. Energy metabolism may be secondarily impaired due to decreased physical activity, recurrent illness, and inefficient protein function. However, no primary mitochondrial or energy metabolism defects have been demonstrated in ALG2-CDG; the core lesion remains in glycosylation.

Metabolomics studies in ALG2-CDG have focused mainly on glycan profiling rather than global metabolite analysis. The distinctive linear heptasaccharide glycan NeuAc‑Gal‑GlcNAc‑Man\(_2\)‑GlcNAc\(_2\) serves as a metabolic signature of altered N‑glycan biosynthesis.[4][14] This glycan is found not only on transferrin but also on other plasma glycoproteins, suggesting a generalized metabolic shift in glycosylation patterns.[14][16]

### 6.5 Immune System and Tissue Damage Mechanisms

Direct immune system involvement—autoimmunity or immunodeficiency—has not been prominently reported in ALG2-CDG. Some CDG subtypes are associated with immune dysfunction, such as leukocyte adhesion deficiency or congenital dyserythropoietic anemia in mixed glycosylation disorders.[12] In ALG2-CDG, recurrent infections are more likely to be secondary to neuromuscular and respiratory vulnerabilities rather than primary immune deficits.[4][12][14] Nonetheless, glycosylation is critical for immune receptors and complement proteins, so subtle immune alterations cannot be excluded.

Tissue damage mechanisms in ALG2-CDG are primarily developmental and functional rather than acute necrosis or fibrosis. Hypomyelination in the brain reflects impaired development of oligodendrocytes and myelin sheaths rather than demyelinating inflammation.[11] Hepatomegaly and hepatopathy likely arise from altered glycoprotein trafficking and secretion in hepatocytes. No strong evidence indicates oxidative stress, ischemia, or fibrosis as primary mechanisms, though chronic disease can lead to secondary changes.

### 6.6 Epigenetic, Transcriptomic, Proteomic, and Other Molecular Profiling

Specific epigenetic changes in ALG2-CDG have not been reported. Transcriptomic and proteomic profiling are limited but some insights derive from cell models and fibroblasts. Alcántara‑Ortigoza et al. studied ALG2 mutant constructs and observed reduced ALG2 protein expression and altered glycan levels compared to wild‑type, consistent across fibroblasts and other cell types.[16] These experiments imply that transcription of mutant alleles may be normal but protein stability is compromised, perhaps leading to increased degradation.

Proteomics in ALG2-CDG is implicit in glycoprotein analyses, particularly transferrin and IgG glycoforms.[14][16] Removal of IgG and transferrin followed by glycan analysis showed increased levels of both linear and fucosylated linear glycans on other plasma glycoproteins, indicating widespread proteomic changes.[14] These findings highlight that ALG2 deficiency affects not just one protein but a large swath of the glycoproteome.

Single‑cell and spatial transcriptomics, multi‑omics integration, and functional genomics screens have not yet been applied directly to ALG2-CDG, reflecting the rarity of the disease and the complexity of performing such studies. However, yeast and mammalian cell models of ALG2 function, including CRISPR knockouts or RNAi, provide functional genomics insights into N‑glycan biosynthesis.[11][18] Such models confirm that ALG2 is essential for viability and glycosylation in yeast, and that its dual mannosyltransferase function is critical in early LLO assembly.[18]

Suggested GO biological process terms include GO:0006487 (protein N-linked glycosylation), GO:0006488 (dolichol-linked oligosaccharide biosynthetic process), GO:0006489 (N-linked glycosylation via asparagine), GO:0007596 (blood coagulation), GO:0007528 (neuromuscular junction development), and GO:0007268 (synaptic transmission). CL terms include CL:0000540 (hepatocyte), CL:0000066 (neuron), CL:0000565 (skeletal muscle cell), CL:0000097 (Schwann cell), and CL:0000317 (endothelial cell). Cellular component GO terms include GO:0005783 (endoplasmic reticulum), GO:0005789 (endoplasmic reticulum membrane), and GO:0000139 (Golgi apparatus). CHEBI entities relevant to the pathway include CHEBI:17646 (GDP-mannose), CHEBI:15996 (UDP-GlcNAc), and CHEBI:27112 (dolichol phosphate).

## 7. Anatomical Structures Affected

### 7.1 Organ-Level Involvement

ALG2-CDG affects multiple organ systems, with primary involvement of the nervous system, neuromuscular junction, liver, hematologic/coagulation system, and eyes.[7][8][11][12][14][16] The brain and central nervous system (UBERON:0000955) show developmental abnormalities, including hypomyelination (HP:0002063) and impaired synaptic function leading to hypotonia, seizures, and developmental delay.[11][12] The neuromuscular junction in skeletal muscle (UBERON:0002107 for skeletal muscle organ, GO:0031594 for neuromuscular junction) is affected in ALG2-CMS, resulting in fatigable weakness and respiratory compromise.[10][12][13]

The liver (UBERON:0002107 for liver) displays hepatomegaly and hepatopathy, reflecting glycosylation defects in secretory and membrane proteins.[11][12][16] The coagulation system, including circulating factors and endothelial cells, experiences coagulopathy, aligning with organ-level hematologic involvement (UBERON:0000178 for blood, UBERON:0001981 for vascular system).[7][8][12] The eyes (UBERON:0000970 for eyeball) manifest iris coloboma and cataracts, indicating developmental anomalies in ocular structures.[8][11]

Secondary organ involvement includes respiratory system (UBERON:0002048 for respiratory system), due to neuromuscular weakness, aspiration, and recurrent infections, and gastrointestinal tract (UBERON:0001043), due to reflux and feeding difficulties.[4][12][14] The cardiovascular system, kidneys, and endocrine organs may be affected in some N‑linked CDG subtypes but are less prominently reported in ALG2-CDG given the limited case data.[12]

### 7.2 Tissue and Cell-Level Involvement

At the tissue level, multiple tissue types are affected. Nervous tissue (UBERON:0001016) is impacted through neuronal and glial dysfunction, leading to developmental delay and hypomyelination.[11][12] Muscle tissue (UBERON:0002385) is affected in both skeletal (UBERON:0002107) and possibly cardiac muscle, although cardiac involvement has not been emphasized specifically in ALG2-CDG.[12] Epithelial tissue in liver, gastrointestinal tract, and vascular endothelium is altered due to glycosylation defects in membrane proteins.[11][12][16]

Specific cell populations include neurons (CL:0000066), oligodendrocytes (CL:0000128), skeletal muscle cells (CL:0000565), hepatocytes (CL:0000540), endothelial cells (CL:0000317), and lens epithelial cells in the eye (CL:0000650). In each of these cell types, ALG2 deficiency impairs N‑glycosylation of key proteins, such as receptors, enzymes, and structural components. For example, skeletal muscle cells at the neuromuscular junction depend on properly glycosylated AChR subunits, while hepatocytes rely on glycosylated coagulation factors and plasma proteins.[11][12][13][16]

### 7.3 Subcellular Localization and Compartments

ALG2’s primary subcellular localization is the endoplasmic reticulum (ER), specifically the ER membrane facing the cytosol, where early N‑glycan biosynthesis occurs.[11][18] GO cellular component terms relevant here include GO:0005783 (endoplasmic reticulum) and GO:0005789 (endoplasmic reticulum membrane). The lipid-linked oligosaccharides synthesized by ALG2 and allied enzymes reside in the ER membrane, while OST transfers them to nascent polypeptides within the ER lumen.[11][18]

Consequences of ALG2 deficiency ripple into other cellular compartments. The Golgi apparatus (GO:0000139) receives hypoglycosylated glycoproteins, altering glycan trimming and extension. The plasma membrane (GO:0005886) displays fewer or abnormal glycoprotein receptors, such as AChR in muscle and neurotransmitter receptors in neurons.[13] Lysosomes (GO:0005764) and endosomes (GO:0005768) may experience altered trafficking of glycoproteins and receptors. Although mitochondria (GO:0005739) and nuclei (GO:0005634) are not directly targeted by ALG2, global cellular stress due to misfolded glycoproteins can impact their function.

### 7.4 Localization and Lateralization

Anatomical localization of ALG2-CDG manifestations is generally bilateral and systemic rather than unilateral. Iris coloboma and cataracts may affect one or both eyes, but many reports do not specify lateralization.[8][11][14] Neuromuscular weakness is diffuse, affecting proximal and distal muscles symmetrically. Brain hypomyelination is global rather than focal, as noted by Thiel et al.[11]

The neuromuscular junction involvement in ALG2-CMS affects muscle groups variably but not in a lateralized pattern; fatigable weakness can be more apparent in certain muscles (e.g., extraocular muscles causing ptosis) but is not restricted to one side.[13] Hepatomegaly, coagulopathy, and systemic features are inherently whole‑body phenomena.

UBERON terms for localization include UBERON:0000955 (brain), UBERON:0000970 (eyeball), UBERON:0002107 (liver), UBERON:0002107 (skeletal muscle organ), and UBERON:0002048 (respiratory system). Lateralization is not a defining feature of ALG2-CDG; instead, the systemic nature of glycosylation defects leads to widespread organ involvement.

## 8. Temporal Development

### 8.1 Age of Onset and Onset Pattern

ALG2-CDG is a congenital or early-onset disorder, with symptoms appearing in the neonatal period or within the first year of life.[1][2][7][8][11][14][16] Orphanet explicitly lists age of appearance as “Petite enfance, Néonatal,” and GARD notes that symptoms may start to appear as a newborn or infant.[1][8] Thiel’s patient was normal at birth but developed multisystem disease in the first year, including mental retardation, seizures, iris coloboma, hypomyelination, hepatomegaly, and coagulation abnormalities.[11] The Mexican case exhibited perinatal asphyxia, hypotonia, absent sucking reflex, and congenital hip dislocation from birth, followed by additional manifestations over months.[4][14]

The onset pattern is chronic and insidious rather than acute. Initial signs may include hypotonia and feeding difficulties, subtle developmental delays, and ocular anomalies detected in infancy. Seizures and more overt neurologic signs may emerge later in infancy or early childhood. Neuromuscular junction symptoms in ALG2-CMS, such as fatigable weakness and ptosis, can present in childhood, sometimes as a child begins to walk or engage in sustained activity.[12][13]

### 8.2 Disease Progression, Course, and Duration

The disease course of ALG2-CDG is chronic, lifelong, and typically progressive in terms of developmental and functional impairment. Early hypotonia and developmental delay often evolve into persistent intellectual disability and motor deficits.[7][11][14][16] Seizures may be intermittent but can contribute to regression or plateauing of developmental progress. Structural anomalies (iris coloboma, cataracts, hip dislocation) are fixed and do not regress.

Progression rate varies. In some patients, there is relatively rapid emergence of multisystem disease during the first year, followed by stabilization of certain features with supportive care. In others, neuromuscular and respiratory complications may exacerbate over time, particularly in ALG2-CMS, where fatigable weakness can lead to increasing disability if not treated.[12][13] Developmental milestones may continue to be gained, albeit slowly, in some children, suggesting partial compensation or residual ALG2 activity.

ALG2-CDG is not self-limited; it persists throughout life. There are no defined disease stages analogous to cancer staging or organ failure scales, but clinical descriptions often refer to early, intermediate, and late phases in terms of developmental and organ involvement. Early childhood is a critical period, with opportunities for early intervention (physiotherapy, seizure control, cataract surgery) to optimize outcomes. Later, focus shifts to managing complications and supporting quality of life.

### 8.3 Patterns of Remission, Critical Periods, and Interventions

Spontaneous remission of core ALG2-CDG features does not occur. However, specific manifestations can be modulated by treatment. Seizures may enter remission with antiepileptic drugs, reducing seizure burden and improving behavior and cognition.[12][14][16] Neuromuscular symptoms in ALG2-CMS often respond to acetylcholinesterase inhibitors such as pyridostigmine (NCIT:C519), improving muscle strength and stamina.[2][12][13][16] These improvements represent treatment-induced amelioration of symptoms rather than reversal of underlying pathophysiology.

Critical periods in ALG2-CDG include the perinatal and early infancy period, when feeding difficulties, respiratory instability, and neurologic crises can pose life-threatening risks. Early diagnosis through transferrin profiling and genetic testing allows for anticipatory management of coagulopathy, seizures, and neuromuscular weakness.[2][12][14][16] Developmental intervention (NCIT:C21480) is crucial in the first years to maximize cognitive and motor potentials.

Another critical window arises when structural eye anomalies such as cataracts are identified; timely surgical correction (NCIT:C15189, cataract extraction) can preserve or improve vision, impacting developmental trajectories. Similarly, early recognition of congenital hip dislocation allows orthopedic management to optimize mobility.[4][14]

Thus, while the disease itself does not remit, targeted interventions during critical periods can significantly influence functional outcomes and quality of life.

## 9. Inheritance and Population

### 9.1 Inheritance Pattern, Penetrance, and Expressivity

ALG2-CDG follows an autosomal recessive inheritance pattern. OMIM and Orphanet clearly state that congenital disorder of glycosylation type Ii is autosomal recessive, and that affected individuals inherit one defective copy of *ALG2* from each asymptomatic parent.[2][7][8][10] ClinGen’s gene curation notes that heterozygous carriers are reportedly unaffected and that the disease mechanism is biallelic loss-of-function.[9]

Penetrance among individuals with biallelic pathogenic *ALG2* variants appears to be complete; all reported homozygotes or compound heterozygotes exhibit some degree of ALG2-CDG or ALG2-CMS phenotype.[7][9][11][14][16] Expressivity, however, is variable. Some patients have severe multisystem involvement with profound intellectual disability, seizures, and coagulopathy, while others show milder neuromuscular phenotypes, primarily fatigable weakness, with relatively preserved cognition.[2][10][13][16] This variability reflects differences in variant type, residual enzymatic activity, and possibly tissue‑specific glycosylation patterns and modifiers.

No evidence supports genetic anticipation (increasing severity in successive generations) or germline mosaicism as drivers of ALG2-CDG. The disorder is rare and appears in isolated families, often with consanguinity or shared ancestry. Founder effects may exist for variants such as p.Arg251Leu in Argentine families, suggesting increased carrier frequency in localized populations.[7][16] However, specific carrier frequencies in the general population have not been quantified in available sources.

### 9.2 Epidemiology, Prevalence, and Incidence

ALG2-CDG is an ultra‑rare disease. Orphanet reports prevalence as <1/1,000,000, consistent with only a handful of cases worldwide.[8][15] CDGHub notes that to date nine cases had been reported in the medical literature at the time of its writing, while more recent publications update the count to approximately fourteen documented ALG2-CDG cases worldwide.[2][14][16] The 2024 Mexican case report explicitly states that “to date, fourteen cases of ALG2-CDG have been documented worldwide,” and includes the new case as the fifteenth in some tabulations.[14] ClinGen’s curation references at least five probands across multiple publications.[9]

Because of the very low number of known cases, incidence and prevalence estimates are approximate and likely underestimates. CDG overall has an occurrence rate of approximately 1 in 20,000 to 1 in 50,000 live births, but ALG2-CDG represents only a tiny fraction of CDG diagnoses.[12][16] Many CDG types remain undiagnosed or misdiagnosed, particularly in regions lacking specialized glycosylation testing, so ALG2-CDG may be somewhat more frequent than currently recognized.

### 9.3 Population Demographics, Geography, Sex Ratio, and Age Distribution

Reported ALG2-CDG patients come from diverse geographic and ethnic backgrounds, including European, Middle Eastern, Argentinian, and Mexican ancestry.[7][11][14][16] The p.Arg251Leu variant appears in Argentine families, suggesting a regional cluster.[7][16] The Mexican case represents the first child of Mexican ancestry diagnosed with ALG2-CDG, expanding the geographic distribution.[14] Cossins et al.’s CMS cohort included patients from multiple countries, including Saudi Arabia and other Middle Eastern populations.[13]

No clear sex predilection has been reported; both males and females are affected. Age distribution among diagnosed patients spans newborns to children, with primary disease onset in infancy and ongoing manifestations into childhood. Adult ALG2-CDG patients have not been prominently described in available sources, though some ALG2-CMS patients may reach adulthood with milder phenotypes.[12][13]

Consanguinity plays a role in some families, particularly where homozygous missense variants, like p.Arg251Leu, are present in multiple siblings from consanguineous unions.[7][16] In outbred populations, compound heterozygous variants are more common, as in Thiel’s and the Mexican cases.[11][14] Founder effects may exist for certain alleles in specific populations, but detailed population genetics studies are lacking.

Carrier frequency for pathogenic *ALG2* variants is very low globally. In general population databases such as gnomAD, rare missense variants and indels in *ALG2* appear at extremely low allele frequencies, consistent with an ultra‑rare recessive disorder.[9][10][16] However, these databases are not yet finely resolved enough to provide exact carrier frequencies for all pathogenic alleles, particularly in underrepresented populations.

## 10. Diagnostics

### 10.1 Clinical and Laboratory Diagnostics

Diagnosis of ALG2-CDG relies on a combination of clinical evaluation, laboratory glycosylation assays, and genetic testing. Clinically, suspicion arises in infants with multi‑system involvement—hypotonia, developmental delay, seizures or infantile spasms, iris coloboma or cataracts, hepatomegaly, coagulopathy, and distinctive facies—or in children with neuromuscular fatigable weakness consistent with CMS.[2][7][8][11][12][13][14][16]

A key screening test is transferrin isoform analysis, typically performed by isoelectric focusing (IEF), HPLC, or mass spectrometry to detect carbohydrate-deficient transferrin (CDT).[2][12][14][16] CDGHub notes that screening in suspected patients begins with a blood test to analyze serum transferrin, and that transferrin profiling can show a type I CDG pattern in ALG2-CDG.[2] Alcántara‑Ortigoza et al. and Papazoglu et al. characterized the serum glycophenotype of ALG2-CDG patients, observing mild type I CDT patterns and increased hyposialylated biantennary and triantennary N‑glycans.[16] In the Mexican case, CDT analysis revealed a mild type I CDG pattern and, importantly, the presence of a specific abnormal transferrin glycoform containing the linear heptasaccharide NeuAc‑Gal‑GlcNAc‑Man\(_2\)‑GlcNAc\(_2\), which served as a diagnostic biomarker.[4][14]

This heptasaccharide glycan can be detected via advanced mass spectrometry of transferrin and other plasma glycoproteins, providing high specificity for ALG2-CDG.[4][14][16] Its presence indicates generalized glycosylation abnormality and adds diagnostic precision beyond generic CDT patterns. Thus, laboratory diagnostics involve LOINC-coded assays for transferrin isoforms (e.g., LOINC: 34658-1 Carbohydrate-deficient transferrin) and specialized glycomics analyses.

Other laboratory evaluations include coagulation profiles (PT, aPTT, fibrinogen, factor levels), liver function tests (ALT, AST, bilirubin), metabolic panels, and hematologic assessments. In CDG, coagulopathy with multiple factor deficiencies, hepatic transaminase elevation, and hypoalbuminemia are common; similar findings are expected in ALG2-CDG.[7][8][11][12][16] Neurophysiologic studies such as EEG (for seizures) and EMG/nerve conduction studies (for neuromuscular junction function) may be employed.[12][13][14] In CMS, repetitive nerve stimulation EMG demonstrates decremental responses typical of neuromuscular transmission defect.[13]

Brain MRI often shows hypomyelination or delayed myelination in ALG2-CDG, as noted by Thiel et al.[11] Radiologic imaging of the liver can demonstrate hepatomegaly. Ophthalmologic examinations confirm iris coloboma and cataracts. Orthopedic imaging may reveal congenital hip dislocation.

Histopathology is less commonly performed but can include muscle biopsy in CMS, revealing tubular aggregates and mitochondrial changes.[10][13] Liver biopsy is rarely indicated but might show nonspecific changes in CDG.

### 10.2 Genetic Testing Strategies

Definitive diagnosis of ALG2-CDG requires molecular genetic testing. CDGHub emphasizes that although transferrin analysis can suggest ALG2-CDG, direct molecular genetic testing is the only definitive diagnostic test.[2] Whole exome sequencing (WES) and whole genome sequencing (WGS) have proven highly valuable in identifying *ALG2* variants in patients with complex phenotypes.[4][14][16] In the Mexican case, WGS revealed compound heterozygous variants c.1055_1056delinsTGA and c.964C>A in *ALG2*.[4][14] Earlier cases used targeted sequencing of CDG genes or candidate gene approaches guided by biochemical findings.[11][16]

The NCBI Genetic Testing Registry (GTR) lists multiple tests for *ALG2*, including single-gene sequencing tests and larger CDG or CMS gene panels.[3][5] For a patient with suspected CDG based on transferrin profiling, a CDG gene panel encompassing N‑linked glycosylation genes (e.g., *ALG2*, *ALG3*, *ALG6*, *PMM2*, *MPI*) may be used. For a patient with CMS phenotype, neuromuscular junction gene panels (including *ALG2*, *ALG14*, *DPAGT1*, *GFPT1*, *COLQ*, *RAPSN*, *CHRNE*) are appropriate.[12][13] Single‑gene testing of *ALG2* can be considered when biochemical features strongly implicate ALG2-CDG or when specific variants have been identified in family members.

Chromosomal microarray (CMA), karyotyping, FISH, and mitochondrial DNA testing are generally not informative for ALG2-CDG, as the disease is driven by sequence-level nuclear gene variants rather than copy number changes or mitochondrial defects.[7][10][11][16] Repeat expansion testing is also not relevant. Instead, exome/genome sequencing or targeted gene panels are the primary tools.

### 10.3 Omics-Based Diagnostics and Biomarker Development

Beyond standard genetic testing, omics-based diagnostics have particular relevance in ALG2-CDG. Glycomics and glycoproteomics, using mass spectrometry of serum transferrin, IgG, and other glycoproteins, are central for characterizing the glycosylation defect and identifying disease-specific biomarkers.[4][14][16] The discovery of the linear heptasaccharide NeuAc‑Gal‑GlcNAc‑Man\(_2\)‑GlcNAc\(_2\) as a specific biomarker for ALG2-CDG is a prime example.[4][14] Alcántara‑Ortigoza et al. noted that this unusual glycan was increased on transferrin and other plasma glycoproteins in ALG2-CDG patients, suggesting a generalized glycosylation abnormality.[14][16]

Proteomics, focusing on glycoprotein isoforms, can help differentiate ALG2-CDG from other CDG types, as each glycosyltransferase defect may produce a distinct glycan signature.[12][14][16] Metabolomics of nucleotide sugars and dolichol derivatives has been less explored but could theoretically serve as additional diagnostic avenues.

RNA sequencing and transcriptomics are not routinely used for diagnosis but could, in research settings, assess *ALG2* expression and splicing. Epigenomic profiling is likewise more exploratory than diagnostic at present.

Liquid biopsy concepts used in oncology have limited applicability to ALG2-CDG, though circulating glycoproteins form a kind of “glyco-liquid biopsy” for diagnosing glycosylation disorders.

### 10.4 Clinical Criteria, Differential Diagnosis, and Screening

No formal standardized diagnostic criteria (such as DSM or specific society guidelines) exist exclusively for ALG2-CDG, given its rarity. Instead, diagnostic criteria align with broader CDG evaluation frameworks: presence of multi‑system disease with neurologic, hepatic, coagulopathic, and ocular features; positive CDT/transferrin profile; and identification of biallelic pathogenic variants in a known CDG gene.[12] GeneReviews and CDG reviews outline generic diagnostic pathways for CDG, which can be tailored to ALG2-CDG.[12]

Differential diagnosis includes other N‑linked CDG subtypes (e.g., PMM2-CDG, ALG6-CDG) that share neurologic and hepatic features, but often differ in specific glycan profiles, structural anomalies, and gene variants.[12] Infantile spasms and developmental delay can result from numerous neurologic disorders, including perinatal brain injury, metabolic encephalopathies, and other genetic syndromes. Iris coloboma and cataracts are seen in conditions like CHARGE syndrome and GALNS-related mucopolysaccharidoses, requiring careful evaluation. Congenital myasthenic syndromes due to other genes, such as *DPAGT1*, *GFPT1*, *COLQ*, and *RAPSN*, must be distinguished from ALG2-CMS; here, genetic testing and detailed EMG findings guide differentiation.[12][13]

Screening programs for ALG2-CDG do not exist at the population level. Newborn screening panels currently include only a few inborn errors of metabolism and no CDG disorders. Carrier screening for *ALG2* has not been widely implemented. In families with known ALG2-CDG, cascade genetic testing can be performed to identify carriers and inform reproductive decisions. Prenatal or preimplantation genetic diagnosis (NCIT:C90442) can be considered where pathogenic variants have been identified.

## 11. Outcome and Prognosis

### 11.1 Survival, Mortality, and Life Expectancy

Because ALG2-CDG is so rare and only a small number of patients have been reported, robust survival and mortality statistics are not available. Many CDG subtypes are associated with increased childhood mortality due to infections, organ failure, and severe neurologic complications.[12] For ALG2-CDG, case reports suggest that patients can survive into childhood, but severe morbidity is common.[11][14][16] Thiel’s original patient was described with significant multisystem disease but survival status beyond early childhood was not detailed.[11] The Mexican case was reported during childhood with ongoing complications.[4][14]

Given the multi‑system nature of ALG2-CDG, life expectancy is likely reduced compared to the general population, particularly in severe presentations with uncontrolled seizures, coagulopathy, and recurrent respiratory infections. However, with improved supportive care and early diagnosis, survival may be extended. No formal life expectancy estimates (e.g., 5‑year or 10‑year survival rates) are available in the literature, and disease-specific mortality data from registries are lacking.

### 11.2 Morbidity, Disability, and Quality of Life

Morbidity in ALG2-CDG is high. Patients experience chronic disabilities across multiple domains: motor function (due to hypotonia and CMS), cognition (due to intellectual disability), sensory function (due to ophthalmologic anomalies), and systemic health (due to hepatopathy, coagulopathy, and recurrent infections).[7][8][11][12][14][16] Disability outcomes include dependence on caregivers for daily activities, limited mobility (sometimes requiring assistive devices), and poor communication abilities.

Quality of life is profoundly affected, both for patients and families. Children with ALG2-CDG often require frequent hospitalizations, complex medication regimens, therapy services (physical, occupational, speech), and special education. Caregivers face significant emotional and financial burdens. Standardized quality of life instruments such as EQ‑5D, SF‑36, or PROMIS have not been systematically applied to ALG2-CDG, but extrapolation from similar CDG and neurodevelopmental disorders indicates low baseline scores in physical functioning, role limitations, and mental health domains.[12]

### 11.3 Disease Course, Complications, and Recovery Potential

Complications in ALG2-CDG derive from the underlying pathophysiology: seizures can lead to status epilepticus and brain injury; coagulopathy can cause bleeding or thrombotic events; hepatopathy may progress to chronic liver disease; neuromuscular weakness can result in respiratory failure during infections; and structural anomalies can cause functional impairments.[7][8][11][12][14][16] Recurrent respiratory infections, aspiration pneumonia, and orthopedic complications like hip dislocation or scoliosis are significant morbid events.

Recovery potential is limited in terms of complete reversal of disease. However, targeted treatment of specific symptoms can improve function. Seizure control can enhance developmental progress and reduce acute morbidity. Cataract surgery can restore some vision. Acetylcholinesterase inhibitors can improve neuromuscular strength and reduce respiratory crises in ALG2-CMS.[2][12][13][16] Early developmental therapies can maximize motor and cognitive abilities.

Prognostic factors likely include the severity of neurologic involvement (presence of infantile spasms, profound intellectual disability), extent of coagulopathy and hepatopathy, and effectiveness of neuromuscular management. Early diagnosis and comprehensive care correlate with better outcomes, although no formal prognostic models exist. The presence of residual ALG2 function (e.g., in milder missense variants) may confer less severe disease, as indicated by the difference between classic ALG2-CDG and ALG2-CMS.[10][13][16]

### 11.4 Prognostic Biomarkers and Predictive Indicators

The linear heptasaccharide glycan NeuAc‑Gal‑GlcNAc‑Man\(_2\)‑GlcNAc\(_2\) functions primarily as a diagnostic biomarker rather than a prognostic one.[4][14] However, the degree of hypoglycosylation in transferrin and other glycoproteins, as reflected by CDT patterns and glycan profiles, might correlate with disease severity, though explicit studies are lacking.[14][16] Coagulation factor levels, liver function tests, and EEG findings could serve as clinical biomarkers for risk stratification.

In neuromuscular phenotypes, EMG results and response to acetylcholinesterase inhibitors provide prognostic information about functional improvement potential.[13] Genetic variant type may be predictive: frameshift or nonsense alleles typically produce more severe phenotypes, whereas hypomorphic missense variants might allow partial residual function and milder disease. However, the small case numbers limit robust genotype–phenotype correlations.

NCIT terms relevant to outcomes include NCIT:C20190 (Prognostic Factor) and NCIT:C18163 (Biomarker), useful for annotating predictive indicators in knowledge bases.

## 12. Treatment

### 12.1 Pharmacotherapy and Symptomatic Management

There is currently no approved disease-specific pharmacologic therapy for ALG2-CDG that directly corrects the glycosylation defect.[2][12][14][16] Treatment is primarily focused on managing specific symptoms and preventing complications. In ALG2-CMS, acetylcholinesterase inhibitors such as pyridostigmine bromide (NCIT:C519) are commonly used to treat muscle-related symptoms, improving neuromuscular transmission by increasing acetylcholine availability at the synaptic cleft.[2][12][13][16] CDGHub notes that acetylcholinesterase inhibitors have been used to treat muscle-related symptoms in some ALG2-CDG patients with CMS features.[2] Cossins et al. and Engel et al. document the efficacy of such drugs in CMS due to *ALG2* and *ALG14* mutations.[12][13]

Antiepileptic drugs (NCIT:C1628, e.g., levetiracetam, valproate) are used to control seizures and infantile spasms. Proton pump inhibitors (NCIT:C62036) or H2 blockers can manage gastroesophageal reflux.[4][14] Coagulopathy may be addressed with factor replacement (NCIT:C20034, Fresh Frozen Plasma) or vitamin K (NCIT:C715), depending on the pattern of deficiency. Hepatic symptoms are managed supportively; there is no specific hepatoprotective drug known to correct CDG liver involvement.

Pain control, sedation during procedures, and management of spasticity or movement disorders (if present) may involve additional pharmacotherapy. Nutritional support, including high-calorie formulas or feeding via gastrostomy tube (NCIT:C38285), helps address failure to thrive and low intake.[2][4][14][16]

Pharmacogenomics data specific to ALG2-CDG are not available. However, general considerations for drug metabolism and interactions apply, particularly in children with liver disease and coagulopathy.

### 12.2 Advanced Therapeutics: Gene Therapy, Cell Therapy, RNA-Based Approaches

No gene therapy, cell therapy, or RNA-based therapy has yet been developed or tested specifically for ALG2-CDG. In principle, gene replacement therapy using viral vectors (NCIT:C101294) or CRISPR-based gene editing (NCIT:C121629) could correct the *ALG2* defect in certain tissues, but the multi‑system nature, early developmental onset, and ER localization pose substantial challenges.

Cell therapy approaches, such as stem cell transplantation (NCIT:C17384), have not been explored for ALG2-CDG. RNA-based therapies, such as antisense oligonucleotides (ASOs; NCIT:C123893) or mRNA replacement, are conceptually plausible for some CDG, but no preclinical or clinical work has been reported for ALG2.

Targeted therapies directed at specific glycosylation pathways, such as substrate supplementation (e.g., mannose in MPI-CDG), exist for certain CDG types.[12] For ALG2-CDG, substrate supplementation (GDP‑mannose or mannose) would not bypass the defective mannosyltransferase, and no evidence supports its use.

Immunotherapies (NCIT:C17206) are not relevant to the primary pathophysiology of ALG2-CDG.

### 12.3 Surgical and Interventional Treatments

Surgical interventions in ALG2-CDG focus on structural anomalies and complications. Cataract extraction (NCIT:C15189) can be performed to remove congenital cataracts, improving visual function. Orthopedic surgery (NCIT:C17173) may be required for congenital hip dislocation (open or closed reduction, osteotomies) and for severe scoliosis or kyphosis.[4][14] Gastrostomy tube placement (NCIT:C38285) can be used for long-term feeding in children with severe feeding difficulties and aspiration risk.

Tracheostomy and airway interventions (NCIT:C29846) may be considered in cases of persistent inspiratory stridor and respiratory insufficiency, although specific reports in ALG2-CDG are lacking. Surgical management of refractory seizures (e.g., vagus nerve stimulation, NCIT:C15228) is theoretically possible but has not been described in ALG2-CDG.

### 12.4 Supportive Care, Rehabilitation, and Experimental Therapies

Supportive care is central to ALG2-CDG management. Physical therapy (NCIT:C15229), occupational therapy (NCIT:C48280), and speech therapy (NCIT:C18225) aim to improve motor skills, mobility, communication, and swallowing. Nutritional support with dietitian oversight ensures adequate caloric intake and addresses failure to thrive.[2][4][12][14][16] Respiratory support, including oxygen therapy (NCIT:C50488) and noninvasive ventilation (NCIT:C70931), may be needed during infections or chronic respiratory insufficiency.

Experimental treatments are limited. ClinicalTrials.gov lists numerous trials for CDG broadly but not specifically for ALG2-CDG. Research studies focus on glycophenotyping, pathophysiology, and diagnostic method development rather than therapeutic interventions.[14][16] As gene therapy and enzyme replacement concepts evolve for other CDG types, ALG2-CDG may eventually become a candidate for such approaches.

Treatment outcomes depend on early intervention and comprehensive care. Neuromuscular symptoms in ALG2-CMS often show good response to acetylcholinesterase inhibitors, improving functional capacity.[12][13] Seizure control improves neurologic outcomes. Cataract surgery restores vision. However, intellectual disability and structural anomalies remain challenging.

Treatment strategies should follow individualized clinical pathways rather than standardized algorithms, given case heterogeneity. Personalized medicine approaches, including genotype-guided treatment (e.g., focusing on CMS therapy in patients with CMS-dominant phenotypes), are important.[10][12][13][16]

## 13. Prevention

### 13.1 Primary, Secondary, and Tertiary Prevention

Primary prevention of ALG2-CDG involves preventing occurrence of the disease by avoiding the birth of affected individuals. Because the disorder is autosomal recessive, primary prevention hinges on genetic counseling (NCIT:C17015), carrier testing, and reproductive decision-making in families with known disease. For the general population, carrier screening for *ALG2* is not currently recommended or practical, given the ultra‑rare incidence.

Secondary prevention focuses on early detection and early intervention to mitigate the disease expression. In ALG2-CDG, secondary prevention involves recognizing CDG features quickly, performing transferrin profiling and genetic testing, and initiating supportive therapies (seizure control, nutrition, physical therapy) as early as possible.[2][12][14][16] At present, no population-based newborn screening includes ALG2-CDG, but increased awareness among neonatologists and neurologists can facilitate earlier diagnosis.

Tertiary prevention aims to prevent complications in individuals already living with ALG2-CDG. This includes rigorous infection control, management of coagulopathy and hepatopathy, orthopedic interventions, and ongoing rehabilitation to prevent contractures, scoliosis, and disuse atrophy.[12][14][16] Careful surveillance and proactive management reduce morbidity and improve quality of life.

### 13.2 Immunization, Screening, and Genetic Counseling

Standard immunization schedules (NCIT:C28222, Immunization) should be followed for ALG2-CDG patients, with particular emphasis on vaccinations that reduce respiratory infection risk (e.g., pneumococcal, influenza). These vaccinations represent tertiary prevention, protecting against complications of neuromuscular and respiratory vulnerability. There is no specific vaccine for ALG2-CDG, as the disease is genetic rather than infectious.

Screening and early detection rely on clinician awareness rather than structured programs. When multi‑system CDG features are present, transferrin profiling should be ordered to screen for N‑linked glycosylation defects.[2][12][14][16] In families with known ALG2-CDG, genetic screening via carrier testing and prenatal diagnosis can prevent recurrence. Carrier testing involves sequencing *ALG2* in parents and extended family members, while prenatal diagnosis uses chorionic villus sampling or amniocentesis followed by genetic testing.[12] Preimplantation genetic diagnosis (NCIT:C90442) offers another pathway for at-risk couples.

Behavioral interventions to reduce risk of complications include promoting safe feeding practices, maintaining airway clearance (e.g., physiotherapy), and using protective devices during mobility to prevent falls. Genetic counseling provides risk assessment and family planning guidance, explaining autosomal recessive inheritance, recurrence risks, and testing options.[9][12][14][16]

Public health measures specific to ALG2-CDG are not established, but general environmental interventions (sanitation, pollution control) improve health for affected children. Prophylactic medications to prevent particular complications (e.g., antiepileptic drugs to prevent seizures, prophylactic antibiotics in recurrent infections) are considered case‑by‑case.

## 14. Other Species and Natural Disease

### 14.1 Orthologous Genes and Comparative Biology

Orthologous genes to human *ALG2* exist in multiple species, including yeast, mouse, and other mammals. In Saccharomyces cerevisiae, the ortholog is YGL065C (ALG2), annotated in KEGG as a GDP-Man:Man(1)GlcNAc(2)-PP‑dolichol α1,3-mannosyltransferase with EC numbers 2.4.1.132 and 2.4.1.257.[18] ALG2 in yeast plays a dual role, adding mannose residues to LLO precursors during N‑glycan biosynthesis, and is essential for viability; defects in yeast ALG2 lead to severe growth defects and glycosylation abnormalities.[11][18]

Orthologs in mice and other vertebrates have conserved function, but natural disease due to ALG2 deficiency in animals has not been reported in veterinary databases such as OMIA. The primary relevance of nonhuman ALG2 is as a model for understanding N‑glycan biosynthesis and glycosyltransferase function.

Comparative pathology shows that N‑glycan biosynthesis is evolutionarily conserved across eukaryotes, and defects in ALG genes produce growth and viability defects in model organisms similar to CDG phenotypes in humans.[11][18] Yeast and cell models of ALG2 deficiency replicate biochemical and glycosylation features of ALG2-CDG, providing mechanistic insights but not natural disease analogues.

No zoonotic potential or cross‑species transmission is relevant to ALG2-CDG, as it is a genetic metabolic disorder rather than an infectious disease.

### 14.2 Veterinary Relevance

No naturally occurring ALG2-CDG analogues have been reported in companion animals (dogs, cats) or livestock. Consequently, veterinary relevance is mainly academic, illustrating conserved glycosylation pathways across species. It is conceivable that as veterinary genomics advances, rare glycosylation disorders analogous to ALG2-CDG may be identified, but none are currently recognized.

## 15. Model Organisms

### 15.1 Yeast and Cellular Models

Yeast has been a key model organism for studying ALG2 function. Thiel et al. used alg2-1 yeast cells to demonstrate that human ALG2 cDNA could complement the yeast defect, restoring mannosyltransferase activity and dolichol-linked oligosaccharide biosynthesis.[11] Their work established cross-species functional conservation and provided evidence that ALG2 acts as an alpha‑1,3-mannosyltransferase in both yeast and humans.[11] KEGG’s Saccharomyces cerevisiae N‑glycan biosynthesis pathway (sce00510) further situates ALG2 as an essential mannosyltransferase in this organism, with in vitro evidence for dual function alongside Alg11.[18]

Yeast

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 6 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 94 |
| Resolved | 91 |
| Unresolved (possible confabulation) | 2 |
| Obsolete | 1 |
| Unverifiable | 0 |
| Terms whose name was checked | 52 |
| Terms named correctly | 21 |
| Terms named as a **different** term | 21 |
| Terms whose name is worth a second look | 10 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `NCIT:C123879` (1 mention) - the report calls it "Congenital Disorder of Glycosylation"; NCIT calls it **Paritaprevir**
- `HP:0002063` (2 mentions) - the report calls it "hypomyelination"; HP calls it **Rigidity**
- `HP:0000514` (2 mentions) - the report calls it "coloboma of iris"; HP calls it **Slow saccadic eye movements**
- `HP:0002019` (3 mentions) - the report calls it "gastroesophageal reflux"; HP calls it **Constipation**
- `HP:0003118` (1 mention) - the report calls it "hypoalbuminemia"; HP calls it **Increased circulating cortisol level**
- `HP:0003401` (1 mention) - the report calls it "easy fatigability"; HP calls it **Paresthesia**
- `HP:0001370` (1 mention) - the report calls it "skeletal dysplasia"; HP calls it **Rheumatoid arthritis**
- `HP:0001615` (2 mentions) - the report calls it "stridor"; HP calls it **Hoarse cry**
- `HP:0001744` (1 mention) - the report calls it "respiratory muscle weakness"; HP calls it **Splenomegaly**
- `GO:0042285` (1 mention) - the report calls it "GDP-mannose:Man(1)GlcNAc(2)-PP-dolichol alpha‑1,3-mannosyltransferase"; GO calls it **xylosyltransferase activity**
- `CHEBI:17646` (2 mentions) - the report calls it "GDP-mannose"; CHEBI calls it **mevaldic acid**
- `CHEBI:15996` (2 mentions) - the report calls it "UDP-GlcNAc"; CHEBI calls it **GTP**
- `CL:0000540` (3 mentions) - the report calls it "hepatocyte"; CL calls it **neuron**
- `CL:0000066` (3 mentions) - the report calls it "neuron"; CL calls it **epithelial cell**
- `CL:0000565` (3 mentions) - the report calls it "skeletal muscle cell"; CL calls it **fat body cell**
- `CL:0000317` (3 mentions) - the report calls it "endothelial cell"; CL calls it **sebocyte**
- `GO:0006489` (1 mention) - the report calls it "N-linked glycosylation via asparagine"; GO calls it **dolichyl diphosphate biosynthetic process**
- `UBERON:0002107` (5 mentions) - the report calls it "liver", "skeletal muscle organ"; UBERON calls it **liver**
- `UBERON:0002048` (2 mentions) - the report calls it "respiratory system"; UBERON calls it **lung**
- `NCIT:C20190` (1 mention) - the report calls it "Prognostic Factor"; NCIT calls it **Chemical Agents**
- `NCIT:C18163` (1 mention) - the report calls it "Biomarker"; NCIT calls it **Kallikrein-2**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0003285` (2 mentions), reported as "congenital dislocation of the hip" - HP does not contain this term
- `CHEBI:27112` (2 mentions), reported as "dolichol phosphate" - CHEBI does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `NCIT:C62036` (Nasal Cavity) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001290` (4 mentions) - the report calls it "generalized hypotonia", "hypotonia"; HP calls it **Generalized hypotonia**
- `HP:0003701` (2 mentions) - the report calls it "fatigable weakness"; HP calls it **Proximal muscle weakness**, and lists "Proximal limb weakness" among its other names
- `HP:0000490` (3 mentions) - the report calls it "ophthalmoparesis"; HP calls it **Deeply set eye**, and lists "Enophthalmos" among its other names
- `HP:0000519` (2 mentions) - the report calls it "cataract"; HP calls it **Developmental cataract**, and lists "Cataract, congenital" among its other names
- `HP:0000479` (1 mention) - the report calls it "abnormality of the anterior segment of the eye"; HP calls it **Abnormal retinal morphology**, and lists "Abnormality of the retina" among its other names
- `HP:0001928` (2 mentions) - the report calls it "abnormal coagulation"; HP calls it **Abnormality of coagulation**
- `CL:0000097` (2 mentions) - the report calls it "Schwann cell"; CL calls it **mast cell**
- `GO:0007268` (1 mention) - the report calls it "synaptic transmission"; GO calls it **chemical synaptic transmission**, and lists "synaptic transmission" among its other names
- `GO:0000139` (2 mentions) - the report calls it "Golgi apparatus"; GO calls it **Golgi membrane**, and lists "Golgi apparatus membrane" among its other names
- `UBERON:0000970` (2 mentions) - the report calls it "eyeball"; UBERON calls it **eye**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0001290` - called "generalized hypotonia", "hypotonia"
- `HP:0001250` - called "seizure", "seizures"
- `UBERON:0002107` - called "liver", "skeletal muscle organ"