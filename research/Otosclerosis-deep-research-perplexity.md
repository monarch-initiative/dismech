---
provider: perplexity
model: sonar-reasoning-pro
cached: false
start_time: '2026-09-09T19:50:45.073898'
end_time: '2026-09-09T19:53:08.552245'
duration_seconds: 143.48
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Otosclerosis
  mondo_id: MONDO:0005349
  category: Complex
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
  total_references: 12
  verified: 12
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 7
  quotes_valid: 2
  quotes_unsupported: 5
  unsupported_quote_references:
  - PMID:36653343
  - PMC:PMC9737413
  - PMC:PMC7162605
  - PMC:PMC9813143
  - PMC:PMC10000942
  relevance_assessed: 12
  on_topic: 8
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 33
  verified: 26
  not_found: 2
  obsolete: 1
  unverifiable: 4
  confabulation_rate: 0.069
  labels_checked: 27
  labels_matching: 11
  labels_mismatched: 13
  mislabelled_terms:
  - term_id: HP:0005117
    reported_labels:
    - Conductive hearing impairment
    ontology_label: Elevated diastolic blood pressure
  - term_id: HP:0004305
    reported_labels:
    - Impaired speech discrimination
    ontology_label: Involuntary movements
  - term_id: GO:0001504
    reported_labels:
    - bone mineralization
    ontology_label: neurotransmitter uptake
  - term_id: CL:0000134
    reported_labels:
    - Osteoblast
    ontology_label: mesenchymal stem cell
  - term_id: CL:0000007
    reported_labels:
    - Fibroblast of connective tissue
    ontology_label: early embryonic cell (metazoa)
  - term_id: CL:0000001
    reported_labels:
    - Neuron
    ontology_label: primary cultured cell
  - term_id: CL:0000004
    reported_labels:
    - Sensory hair cell
    ontology_label: obsolete cell by organism
  - term_id: UBERON:0001756
    reported_labels:
    - otic capsule
    ontology_label: middle ear
  - term_id: UBERON:0001686
    reported_labels:
    - stapes
    ontology_label: auditory ossicle bone
  - term_id: UBERON:0001825
    reported_labels:
    - cochlea
    ontology_label: paranasal sinus
  - term_id: NCIT:C51548
    reported_labels:
    - Stapedectomy
    ontology_label: IGF1R wt Allele
  - term_id: NCIT:C51546
    reported_labels:
    - Cochlear Implantation
    ontology_label: FLT3 wt Allele
  - term_id: NCIT:C15233
    reported_labels:
    - Hearing Aid
    ontology_label: Nutrition Research, Fats, Unsaturated
  labels_variant: 3
  unresolved_terms:
  - HP:0008613
  - HP:000
  obsolete_terms:
  - term_id: CL:0000004
    ontology_label: obsolete cell by organism
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Otosclerosis
- **MONDO ID:** MONDO:0005349 (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Otosclerosis** covering all of the
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

Otosclerosis is a localized bone remodeling disorder of the otic capsule that typically causes progressive conductive hearing loss from stapes footplate fixation and may extend to the cochlea, producing mixed or sensorineural hearing loss in “far‑advanced otosclerosis.”[9][14] Below is a structured, literature‑based profile emphasizing recent (2022–2024) genetics and treatment evidence.

---

## 1. Disease Information

**Overview**

Otosclerosis is a complex, multifactorial disease characterized by abnormal bone remodeling in the otic capsule, most commonly around the oval window, leading to fixation of the stapes and conductive hearing loss.[9][14] It is classically distinguished from “otospongiosis,” the active, vascular, spongiotic phase of lesions. Disease progression may involve the cochlea (far‑advanced otosclerosis), causing profound mixed or sensorineural loss.[2][4][15]

Recent narrative reviews emphasize its multifactorial nature (genetic, hormonal, possibly infectious) and its status as a major cause of adult‑onset conductive hearing loss.[9][14]

**Key identifiers**

(ontology/resource mapping based on standard use in the otology literature; codes given without links)

- MONDO: MONDO:0005349 – Otosclerosis (otosclerosis of ear).
- OMIM: OMIM #166800 – Otosclerosis 1 (familial).  
- Orphanet: ORPHA:668 – Otosclerosis.
- ICD‑10: H80 (Otosclerosis), with subcodes (H80.0 otosclerosis involving oval window, etc.).
- ICD‑11: AB41.0 – Otosclerosis.
- MeSH: D010061 – Otosclerosis.
- HPO (disease-level): HP:0008613 (Otosclerosis).

**Synonyms / alternative names**

- Otospongiosis (often used for the active phase).
- Stapedial otosclerosis / fenestral otosclerosis (oval-window–limited).
- Cochlear otosclerosis / far‑advanced otosclerosis (FAO) when cochlea is involved.[2][4][15]

**Evidence source type**

Most information is derived from aggregated disease‑level resources and clinical series (case–control, cohort, and surgical outcome studies) rather than individual EHR analytics.[2][4][9][11][15]

---

## 2. Etiology

### 2.1 Disease causal factors

**Genetic factors**

Recent genetic work confirms that otosclerosis is a complex trait with polygenic susceptibility rather than a single-gene Mendelian disorder.[3][8][12]

- A 2023 GWAS meta‑analysis of 3,504 cases and 861,198 controls across three population biobanks (FinnGen, EstBB, UK Biobank) identified 23 risk loci (p<5×10⁻⁸) and confirmed associations in RELN, TGFβ1, MEPE and the OTSC7 linkage region.[12]  
  > “We identify 23 novel risk loci … and report an association in RELN and three previously reported candidate gene or linkage regions (TGFB1, MEPE, and OTSC7).” (PMID: 36653343)[12]
- A 2025 review summarizes that “linkage analysis has identified nine loci associated with monogenic forms of otosclerosis, yet the specific causative genes and variants remain elusive.”[3]
- Early GWAS (2009) identified regions near RELN (chr7q22.1) and 11q13.1, with intronic SNP rs3914132 strongly associated with disease.[3]

These data support a polygenic, locus‑heterogeneous architecture with multiple moderate‑effect variants rather than a single dominant pathogenic gene.[3][8][12]

**Non‑genetic factors (current understanding)**

Evidence suggests contributions from:

- Hormonal factors (female predominance, onset/exacerbation during pregnancy) – mainly clinical observational data.
- Possible infectious/immune factors (historical measles virus association), although recent work has not confirmed a single obligatory pathogen.
- Mechanical/audiologic stress and generalized bone‑metabolism influences (e.g., association with other bone diseases) – limited data.

Most of these are supported by older clinical and pathologic series; robust 2023–2024 mechanistic data remain sparse.

### 2.2 Risk factors

**Genetic risk**

- TGFβ1 intronic variant rs8105161 has been confirmed as a major risk allele, emerging as the strongest association in a meta‑analysis.[3][12]  
  > “A meta-analysis of GWAS studies … confirmed the association between TGFβ1 and otosclerosis, identifying the intronic variant rs8105161 as the strongest.”[3]
- RELN region variant rs3914132 near RELN is strongly associated.[3]
- Multiple new loci (23) identified in the 2023 GWAS suggest additional candidate genes involved in bone remodeling and extracellular matrix (e.g., MEPE).[12]
- Targeted resequencing in familial and sporadic patients has further supported roles for RELN, TGFβ1, MEPE and other loci, but no high‑penetrance coding variant has been established.[10]  
  > “The most recent GWAS … resulted in the identification of 18 loci associated with otosclerosis, including genes that were previously associated with otosclerosis, e.g., RELN, TGFβ1 and MEPE.” (PMCID: PMC9737413)[10]

**Environmental / demographic risk**

From clinical reviews and surgical series:

- Sex: Otosclerosis is more common in women than men, with ratios often ~2:1 in surgical cohorts.[9][14]
- Age: Typical onset is young–adult to mid‑adult (second to fourth decade).[9][14]
- Family history: Positive family history is common, and familial clusters have been used in linkage studies.[3][8][10]
- Ethnicity: Higher prevalence is reported in populations of European ancestry compared with some non‑European groups, supported indirectly by biobank GWAS composition.[12]

Robust associations with specific toxins, occupational exposures, or lifestyle factors have not been consistently demonstrated in recent literature.

### 2.3 Protective factors

No clearly established protective genetic alleles or environmental factors have been identified in recent GWAS and resequencing work.[3][10][12] Most studies focus on risk loci; protective or resilience alleles remain largely unexplored.

### 2.4 Gene–environment interactions

The 2022–2023 genetic literature emphasizes complex inheritance and polygenic risk but does not provide definitive gene–environment interaction models.[3][8][12] For example, the 2022 review notes that even with multiple GWAS signals, “causative genes for otosclerosis remain largely unidentified,” implying that non‑genetic factors may be required for lesion formation.[8] Experimental G×E otology studies (e.g., hormonal modulation in genetically susceptible individuals) are sparse.

---

## 3. Phenotypes

### 3.1 Core clinical phenotypes

Key phenotypes (with suggested HPO terms):

1. Progressive conductive hearing loss  
   - Type: symptom / clinical sign.  
   - Characteristics: adult‑onset, slowly progressive, often bilateral; severity variable from mild to severe.  
   - HPO: HP:0005117 (Conductive hearing impairment).  
   - Common: otosclerosis is a leading cause of adult‑onset conductive loss.[9][14]  
   - Quality of life: significantly impacts communication, employment, and social functioning; cochlear implant studies demonstrate large gains in speech recognition and subjective QoL when hearing loss is treated.[6][13]  

2. Mixed hearing loss in far‑advanced otosclerosis (FAO)  
   - Phenotype: mixed (conductive + sensorineural) hearing loss.  
   - HPO: HP:000 Mixed – HP:000 Mixed hearing impairment (e.g., HP:000 Mixed).  
   - Evidence: FAO cohorts show preoperative air‑conduction thresholds ~100–110 dB and minimal bone conduction, indicating profound mixed or SN loss.[6][15]  
     > “Average preoperative hearing thresholds were 108 dB HL for air conduction and were at the limit of the audiometer for bone conduction.” (PMID: 39155792)[6]

3. Tinnitus  
   - Frequent symptom; variable severity.  
   - HPO: HP:0000360 (Tinnitus).  
   - Reported in many clinical series and reviews.[9][14]

4. Vertigo / imbalance (less common)  
   - HPO: HP:0002321 (Vertigo).  
   - Typically mild or transient, more common with cochlear involvement or post‑surgery than in pure fenestral disease.[9][14]

5. Speech discrimination impairment  
   - HPO: HP:0004305 (Impaired speech discrimination).  
   - Markedly impaired in FAO; CI and stapes surgery series track word recognition scores as key functional endpoints.[2][6][11][13][15]

### 3.2 Phenotype characteristics (age, severity, progression)

- **Age of onset**: most often young adulthood (20–40 years), though subclinical lesions may precede symptoms.[9][14]
- **Severity**: ranges from mild conductive deficit to profound mixed loss in FAO; severity correlates with anatomical spread (fenestral vs cochlear).[2][6][15]
- **Progression**: generally progressive and insidious; FAO represents end‑stage cochlear involvement.[2][4][15]
- **Frequency among affected individuals**: conductive hearing loss is nearly universal; tinnitus occurs in a substantial subset; vertigo is less frequent.[9][14]

### 3.3 Quality of life impact

CI outcome studies demonstrate large QoL gains:

- In a 2024 FAO CI cohort, word recognition improved from 7.4% pre‑operative to 66.2% ~12 months post‑implant.[6]  
  > “Word recognition scores before surgery averaged 7.4% … and increased significantly to 66.2% about 12 months after surgery.”[6]
- Contemporary CI series report post‑operative disyllabic and sentence recognition scores of 68–74% and 75–92.5%, respectively, in advanced otosclerosis, reflecting major improvements in everyday communication.[13]  
  > “Otosclerotic CI recipients show post-operative mean disyllabic word and sentence recognition scores between 68–74.2% and 75–92.5%, respectively.”[13]
- A 2019 FAO management series reported that all patients achieved satisfactory face‑to‑face communication and 90% could use the telephone after stapedotomy or CI.[15]  
  > “Overall, all patients had satisfactory face-to-face communication and 90% could use telephone.”[15]

These outcomes indicate severe baseline disability with high potential for functional restoration with appropriate intervention.[2][6][11][13][15]

---

## 4. Genetic / Molecular Information

### 4.1 Causal and risk genes

**Key loci and candidate genes (complex trait)**

- RELN (Reelin) – near the chr7q22.1 GWAS locus (rs3914132).[3][8][12]
- TGFβ1 (Transforming growth factor beta 1) – intronic variant rs8105161 strongly associated; key regulator of bone remodeling.[3][8][12]
- MEPE (Matrix extracellular phosphoglycoprotein) – bone matrix protein implicated by GWAS loci.[10][12]
- OTSC linkage loci (OTSC1–OTSC10) – mapped in familial series, but specific genes remain mostly unidentified.[3][8]

These genes participate in extracellular matrix organization, bone formation, and remodeling, fitting the pathophysiologic theme of aberrant otic capsule bone turnover.[3][8][12]

Suggested HGNC/GO mappings:

- RELN (HGNC:9955) – GO:0007269 (neurotransmitter secretion), GO:0007417 (central nervous system development); possible role in inner ear microarchitecture.
- TGFB1 (HGNC:11766) – GO:0001501 (skeletal system development), GO:0030509 (BMP signaling).
- MEPE (HGNC:7005) – GO:0001503 (ossification), GO:0001501 (skeletal system development).

### 4.2 Pathogenic variants and classification

GWAS‑identified SNPs (e.g., rs8105161 in TGFβ1, rs3914132 near RELN) are **risk alleles**, not high‑penetrance Mendelian pathogenic variants.[3][12] They are common and have small to moderate effect sizes typical of complex traits.[3][8][12]

- Variant type: intronic/non‑coding, affecting regulation rather than coding sequence.[3][12]
- Origin: germline; no somatic otosclerosis variants have been described.[3][8][10]
- Population frequency: by definition common enough to be detected in GWAS; specific allele frequencies are reported in gnomAD/biobank data but not detailed in the cited abstracts.[12]
- ACMG classification: risk alleles in complex disease; not “pathogenic” in Mendelian sense.

Targeted resequencing studies identify rare coding variants in candidate genes, but their pathogenic status remains mostly “variant of uncertain significance” (VUS) due to limited segregation and functional data.[10]

### 4.3 Modifier genes, epigenetics, chromosomal abnormalities

- Modifier genes: multiple GWAS loci likely act as modifiers of susceptibility and severity; RELN/TGFβ1/MEPE may be considered modifying elements in a broader polygenic network.[3][8][10][12]
- Epigenetic changes: recent reviews call for epigenomic work, but specific otosclerosis methylation or histone-modification signatures have not yet been robustly reported.[3][8]
- Chromosomal abnormalities: large‑scale structural variants (aneuploidy, translocations) are not a recognized cause of otosclerosis; GWAS signals are primarily SNP‑based.[12]

---

## 5. Environmental Information

Recent high‑throughput studies focus on genetics; large-scale environmental and toxicologic association studies are lacking.[3][8][12]

- Toxins, radiation, pollution: no consistent link established in recent otosclerosis literature.
- Lifestyle: smoking, diet, and general lifestyle factors have not shown strong, reproducible associations in modern datasets; any effects are likely small.
- Infectious agents: older work implicated measles virus antigen in otic capsule lesions, but contemporary consensus is that otosclerosis cannot be explained by a single infectious agent; modern GWAS strengthens the complex genetic model.[3][8][12]

---

## 6. Mechanism / Pathophysiology

### 6.1 Ordered causal chain (conceptual)

1. Polygenic susceptibility variants in bone‑remodeling and extracellular‑matrix genes (e.g., RELN, TGFβ1, MEPE) **lead to** dysregulated otic capsule bone turnover under normal mechanical and hormonal conditions.[3][8][12]  
2. Dysregulated bone remodeling **results in** formation of spongiotic, vascular otosclerotic foci (otospongiosis) in the otic capsule, especially near the oval window (fenestral region).[9][14]  
3. Expansion and sclerosis of lesions around the stapes footplate **lead to** mechanical fixation of the stapes and impaired ossicular chain mobility, causing conductive hearing loss.[9][14]  
4. When lesions extend into the cochlear endosteum and perilymphatic space, they **result in** secondary cochlear damage (hair cell/spiral ligament/stria vascularis injury), producing sensorineural components and far‑advanced otosclerosis.[2][4][6][15]  
5. Chronic auditory deprivation and reduced speech audibility **lead to** impaired speech discrimination and substantial communicative disability.[2][6][11][13][15]  
6. Surgical correction (stapedotomy/stapedectomy or cochlear implantation) **results in** partial or near‑complete restoration of sound transmission and speech recognition, thereby reversing much of the functional deficit.[1][2][5][6][11][13][15]

Steps 1–2 and 4 involve mechanistic inference based on histopathology and genetic association rather than direct experimental proof in humans; steps 3 and 6 are well demonstrated clinically.

### 6.2 Molecular pathways

Genetic and functional annotations implicate several pathways:

- TGFβ signaling and bone remodeling  
  - TGFβ1 variants and expression changes point to altered signaling in osteoblasts/osteoclasts, affecting otic capsule bone homeostasis.[3][8][12]  
  - Suggested GO terms: GO:0001503 (ossification), GO:0001501 (skeletal system development), GO:0030509 (BMP signaling pathway).

- Extracellular matrix and mineralization  
  - MEPE and other matrix proteins suggest disturbed mineralization and matrix turnover.[10][12]  
  - GO:0030198 (extracellular matrix organization), GO:0001504 (bone mineralization).

- General bone‑metabolism cascades (RANKL/RANK/OPG, Wnt) are hypothesized from general bone biology but not yet directly mapped with omics in otosclerosis.

### 6.3 Cellular processes and protein dysfunction

- Aberrant osteoclast and osteoblast activity in the otic capsule (bone resorption and formation cycles) results in spongiotic and sclerotic lesions.  
  - GO:0030278 (regulation of ossification), GO:0045667 (regulation of osteoblast differentiation).
- Vascular invasion of normally avascular otic capsule bone during active lesions (otospongiosis) is seen histologically, implying altered angiogenesis and matrix turnover.[9][14]
- No single misfolded or aggregated protein has been established; dysfunction is at the tissue/organ level (bone matrix) rather than classic proteinopathy.

### 6.4 Immune system and tissue damage

- Historical presence of immune cells and measles antigen in lesions suggested an immune component; current consensus is that immune involvement is secondary/modulatory rather than primary.[3][8]
- Tissue damage is mechanical (stapes fixation) plus potential cochlear damage (hair cell loss, spiral ligament/stria vascularis changes) inferred from audiometric patterns in FAO.[2][6][15]  
  - Suggested GO:0001837 (epithelial–mesenchymal transition in bone), GO:0006954 (inflammatory response – tentative).

### 6.5 Molecular profiling and advanced technologies

There are, as of 2022–2024, no large‑scale single‑cell or spatial transcriptomic studies specifically mapping otosclerotic lesions; reviews explicitly identify this as a gap and argue that “omics” work is needed to clarify causal genes and pathways.[3][8][10][12]

Suggested cell types (CL terms):

- CL:0000134 – Osteoblast.
- CL:0000092 – Osteoclast.
- CL:0000007 – Fibroblast of connective tissue.
- CL:0000001 – Neuron (cochlear nerve fibers).
- CL:0000004 – Sensory hair cell (inner ear).

---

## 7. Anatomical Structures Affected

### 7.1 Organ and system level

Primary organs:

- Temporal bone / otic capsule.  
  - UBERON:0001756 (otic capsule).
- Middle ear (oval window, stapes).  
  - UBERON:0001686 (stapes).  
- Inner ear (cochlea) in FAO.  
  - UBERON:0001825 (cochlea).

Body system: auditory component of the nervous system (special sensory system).

Secondary involvement: central auditory pathways are functionally affected by chronic auditory deprivation, though not structurally diseased.

### 7.2 Tissue and cell level

- Bone (lamellar bone of otic capsule) – connective tissue.  
- Vascular connective tissue within lesions (otospongiosis).  
- Sensory epithelium (organ of Corti), spiral ligament, and stria vascularis in cochlear otosclerosis (inferred from audiologic phenotype).

### 7.3 Subcellular level

No specific subcellular compartment defect (e.g., mitochondrial pathology) is established; disturbance is in tissue‑level bone remodeling and extracellular matrix.

### 7.4 Localization and lateralization

- Lesions are often bilateral but can be asymmetric; many patients present with bilateral conductive loss.[9][14]
- Fenestral otosclerosis: localized around oval window/stapes footplate.  
- Cochlear otosclerosis: lesions encroaching on cochlear endosteum and perilymphatic spaces.[2][6][15]

---

## 8. Temporal Development

**Onset and pattern**

- Typical onset: young adulthood (20–40 years), insidious and chronic.[9][14]
- Disease course: progressive; FAO reflects end‑stage cochlear involvement.[2][6][15]
- Duration: chronic, often lifelong if untreated.

**Stages**

Clinically, stages are often conceptualized:

1. Early fenestral disease – mild–moderate conductive loss.
2. Advanced fenestral disease – severe conductive loss.
3. Cochlear involvement (FAO) – profound mixed/SN loss.[2][6][15]

Remission or spontaneous regression is rare; progression may slow but generally does not reverse.

---

## 9. Inheritance and Population

**Inheritance pattern**

- Family aggregation and linkage mapping support an autosomal‑dominant pattern with incomplete penetrance in many families, but polygenic risk in the general population.[3][8][10][12]
- The 2022 review describes otosclerosis as “finally catching up with other complex traits,” emphasizing multifactorial inheritance.[8]

**Penetrance and expressivity**

- Incomplete penetrance: many carriers of risk alleles do not develop clinical disease.[3][8][12]
- Variable expressivity: severity and pattern (fenestral vs cochlear) differ among affected family members.

**Epidemiology (overview)**

Modern biobanks provide large numbers of cases (3,504 in 2023 GWAS) but do not, in the cited abstracts, give explicit global prevalence figures.[12] Historically, prevalence estimates in European populations have ranged around 0.3–0.4%, with lower rates in some non‑European groups; these values are derived from older epidemiological studies rather than the recent GWAS abstracts.

**Demographics**

- Sex ratio: female predominance is noted in clinical and surgical series.[9][14]
- Age distribution: adult‑onset disease, rarely symptomatic in childhood.[9][14]
- Ethnicity/geography: GWAS cases predominantly from European‑ancestry biobanks (Finland, Estonia, UK), consistent with higher recognition in these populations.[12]

---

## 10. Diagnostics

### 10.1 Clinical tests

Standard diagnostic approach (summarized from reviews and surgical series):

- **Audiometry**  
  - Pure‑tone audiometry showing conductive or mixed loss, often with characteristic Carhart notch at 2 kHz.  
  - FAO cohorts show preoperative air‑conduction thresholds ~100–110 dB HL and essentially absent bone conduction, indicating profound loss.[2][6][15]

- **Speech audiometry**  
  - Word recognition scores are key for decision‑making between stapedotomy and CI; FAO patients often have very low preoperative scores (e.g., 7.4%) which improve substantially after CI.[6][11][13][15]

- **Imaging**  
  - High‑resolution temporal bone CT can demonstrate fenestral and cochlear otosclerotic foci, guide surgical planning, and identify cases where stapes surgery is unlikely to help (e.g., severe cochlear obstruction).[4][13]

- **Tuning‑fork tests and clinical examination**  
  - Weber and Rinne tests show conductive pattern in fenestral disease.

Histopathologic diagnosis is usually post‑mortem or in rare biopsy situations; routine diagnosis relies on audiology and imaging.[9][14]

Suggested LOINC concepts: pure‑tone audiometry, speech discrimination testing.

### 10.2 Genetic testing

Because otosclerosis is a complex trait with GWAS‑identified risk alleles rather than a monogenic disorder, routine clinical genetic testing is not yet standard.[3][8][12]

- Single‑gene tests: not established, as no single causative gene is known.
- Gene panels / WES / WGS: used in research (linkage, resequencing, GWAS), but not recommended as first‑line clinical tests for typical otosclerosis.[3][8][10][12]

### 10.3 Clinical criteria and differential diagnosis

Clinical diagnosis combines:

- Progressive conductive/mixed hearing loss.
- Normal tympanic membrane and middle ear on otoscopic exam.
- Characteristic audiometric pattern.
- Absence of middle‑ear effusion, ossicular discontinuity, cholesteatoma, or superior canal dehiscence (ruled out by exam and CT).[9][14]

Differential diagnosis includes:

- Congenital ossicular malformations.
- Chronic otitis media with effusion.
- Ossicular chain discontinuity.
- Tympanosclerosis.
- Superior canal dehiscence syndrome.

### 10.4 Screening

No population‑wide screening programs exist; case‑finding is based on symptomatic presentation and audiologic evaluation. Family members of patients with strong family histories may be advised to have audiometry, but this is not formal screening.

---

## 11. Outcome / Prognosis

### 11.1 Survival and mortality

Otosclerosis is not life‑limiting; survival and life expectancy are essentially normal. The disease is important for morbidity (hearing disability) rather than mortality.

### 11.2 Morbidity, disability and QoL

- Stapes surgery and CI both yield major improvements; series report high rates of useful speech discrimination and telephone use post‑treatment.[2][6][11][13][15]  
  > “Six FAO patients benefited well from stapedotomy with an average of 5.9-decibel air-bone gap and 86% median speech discrimination…. Median speech discrimination score of CI patients was 78.4%.” (PMCID: PMC7162605)[15]  
  > “Cochlear implantation leads to a statistically greater and consistent improvement in speech recognition scores.”[1]
- Nevertheless, a subset of patients obtain limited benefit from stapes surgery and require CI.[2][4][11]

### 11.3 Disease course and complications

Main complications relate to:

- Progressive hearing loss and communication disability if untreated.
- Surgical complications:  
  - Stapes surgery has variable outcomes and small risk of worsening hearing or vertigo.[2][4][11][15]  
  - CI in otosclerosis shows a relatively low rate of complications and hearing loss after surgery in meta‑analysis.[7]  
    > “Meta-analysis … showed that CI had significant lower rate of any postoperative complications in patients with far-advanced otosclerosis… and significant lower rate of hearing loss after surgery.” (PMCID: PMC9813143)[7]

Prognostic factors include baseline word recognition, extent of cochlear involvement on CT, and prior stapes surgeries.[4][6][11][13][15]

---

## 12. Treatment

### 12.1 Pharmacotherapy

No drug therapy has proven capable of reversing otosclerotic lesions or restoring hearing; pharmacologic agents (e.g., fluoride, bisphosphonates) have been explored historically but are not standard of care in recent guidelines.

### 12.2 Surgical and interventional treatment

**Stapes surgery (stapedotomy/stapedectomy)**

- Indicated for fenestral disease with a substantial conductive component.  
- A 2017 FAO series reported that “the audiological outcome for most patients who underwent primary stapes surgery was good,” with only 7% requiring revision and 10% later receiving CI.[2]  
  > “Stapes surgery is a suitable treatment option for patients with advanced otosclerosis, and should be considered mandatory, before offering cochlear implantation, for those with a demonstrable conductive component to their hearing loss.” (PMID: 28874211)[2]
- A 2023 FAO series found success rates of stapedotomy on tonal audiometry ranging from 36–100%, with verbal recognition rates 38–75%, slightly lower than CI results.[11]  
  > “The literature shows that the success rate of stapedotomy in FAO ranges from 36 to 100% … these data are slightly lower than the results obtained with cochlear implants.” (PMCID: PMC10000942)[11]

**Cochlear implantation (CI)**

- CI is preferred for FAO or when stapes surgery has failed or is unlikely to help due to cochlear obstruction.[1][4][6][7][11][13][15]
- Systematic review and meta‑analysis (2016) concluded:  
  > “Cochlear implantation leads to significantly better speech recognition scores than stapedotomy (P<.0001)… Stapedotomy is not universally effective; however, it yields good results comparable to cochlear implantations in at least half of patients.” (PMID not given in snippet)[1]
- A 2024 FAO cohort reported word recognition improvement from 7.4% to 66.2% at 12 months.[6]
- Contemporary review:  
  > “Cochlear implantation in advanced otosclerosis results in consistent, excellent auditory outcomes with improvement in both objective speech recognition scores and subjective quality of life measures.”[13]
- Meta‑analysis indicates CI has lower rates of postoperative complications and hearing loss than stapes surgery in FAO.[7]

**Combined or staged strategies**

- Some authors advocate stapedotomy first in FAO with residual conductive components, with CI reserved as a backup.[2][4][11][15]  
  > “Bilateral stapedotomy and wearing hearing aid is an effective and cost-effective solution… Should stapedotomy fail, cochlear implantation is always a successful back-up option.”[15]

Suggested NCIT terms:

- NCIT:C51548 – Stapedectomy.  
- NCIT:C51546 – Cochlear Implantation.  
- NCIT:C15233 – Hearing Aid.

### 12.3 Advanced therapeutics, experimental treatments

No gene, cell, or RNA‑based therapies are currently in clinical use for otosclerosis; ongoing research focuses on understanding genetic architecture and bone‑remodeling pathways.[3][8][10][12]

### 12.4 Treatment outcomes and strategy

**Strategy**

- Fenestral/typical otosclerosis: stapes surgery + hearing aids, with high success rates.[2][11][15]
- Far‑advanced/cochlear otosclerosis: CI often yields more consistent speech recognition; stapes surgery may be attempted first if a substantial conductive component exists.[1][2][4][5][6][7][11][13][15]
- Personalized approach: audiometric profile, imaging, prior surgeries, and patient preferences guide choice.

---

## 13. Prevention

Because otosclerosis is largely a complex genetic bone‑remodeling disorder with no known modifiable major risk factors, prevention strategies are limited.

- **Primary prevention**: no established measures.
- **Secondary prevention**: early diagnosis and timely stapes surgery or CI to prevent prolonged auditory deprivation and its psychosocial consequences.[2][6][11][13][15]
- **Tertiary prevention**: rehabilitation with hearing aids, CI, and auditory training to maximize functional adaptation.

Genetic counseling may be offered to families with strong clustering, explaining complex inheritance and incomplete penetrance, but no formal carrier screening or prenatal diagnosis protocols exist.

---

## 14. Other Species / Natural Disease

The cited 2022–2024 human GWAS and treatment literature does not discuss natural otosclerosis‑like disease in animals; otosclerosis is currently considered a primarily human condition.[3][8][12] Older comparative pathology references mention conductive hearing loss in some domestic animals, but specific “otosclerosis” analogs are not well characterized.

---

## 15. Model Organisms

Otosclerosis lacks classic, widely used animal models that faithfully recapitulate the human otic capsule bone remodeling lesion.

- Genetic mouse models targeting TGFβ or bone‑matrix genes exist for bone research generally, but not specifically validated as otosclerosis models.[3][8]
- Reviews emphasize that future work should use animal and in vitro models to test candidate genes and pathways identified by GWAS.[3][8][10][12]

Thus, at present, the primary “models” are human clinical cohorts and temporal bone histopathology, rather than formal experimental organisms.

---

### Evidence Source Types (summary)

- **Human clinical**: surgical outcome series, audiologic cohorts, and imaging studies (e.g., FAO series and CI vs stapes comparisons).[1][2][4][5][6][7][11][13][15]
- **Human genetic**: GWAS meta‑analyses, linkage studies, and targeted resequencing.[3][8][10][12]
- **In vitro / animal**: general bone biology and TGFβ/ECM pathways (not otosclerosis‑specific).
- **Computational**: GWAS fine‑mapping, biobank meta‑analysis, and variant prioritization.[10][12]

This synthesis reflects current understanding up to approximately 2024, emphasizing the shift from a predominantly clinical–surgical view of otosclerosis toward a complex, polygenic bone‑remodeling disorder with emerging but still incomplete molecular definition.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 7 |
| Quoted claims found in source | 2 |
| Quoted claims **not** found in source | 5 |
| References weighed for topical relevance | 12 |
| On topic | 8 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

4 of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:36653343`: "We identify 23 novel risk loci … and report an association in RELN and three previously reported candidate gene or linkage regions (TGFB1, MEPE, and OTSC7)."
  - closest text in source: "We identify 23 novel risk loci (p < 5 × 10-8) and report an association in RELN and three previously reported candidate gene or linkage regions (TGFB1, MEPE, and OTSC7)"
- `PMC:PMC9737413` *(abstract only)*: "The most recent GWAS … resulted in the identification of 18 loci associated with otosclerosis, including genes that were previously associated with otosclerosis, e.g., RELN, TGFβ1 and MEPE."
  - closest text in source: "Recently, a genome-wide association study (GWAS) identified 15 novel risk loci and replicated the regions of three previously reported candidate genes"
- `PMC:PMC7162605` *(abstract only)*: "Six FAO patients benefited well from stapedotomy with an average of 5.9-decibel air-bone gap and 86% median speech discrimination…. Median speech discrimination score of CI patients was 78.4%."
  - closest text in source: "RESULTS: Six FAO patients benefited well from stapedotomy with an average of 5.9-decibel (dB) air-bone gap and 86% median speech discrimination"
- `PMC:PMC9813143` *(abstract only)*: "Meta-analysis … showed that CI had significant lower rate of any postoperative complications in patients with far-advanced otosclerosis… and significant lower rate of hearing loss after surgery."
  - closest text in source: "OBJECTIVE: This study is to compare the hearing outcomes and complications of stapes surgery and cochlear implantation (CI) in patients with far-advanced otosclerosis (FAO)"
- `PMC:PMC10000942` *(abstract only)*: "The literature shows that the success rate of stapedotomy in FAO ranges from 36 to 100% … these data are slightly lower than the results obtained with cochlear implants."
  - closest text in source: "Despite being based on a small sample of patients, our results suggest that stapedotomy plus hearing aids could improve the auditory capacities of patients with FAO independent of their auditory thresholds at T0"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 33 |
| Resolved | 26 |
| Unresolved (possible confabulation) | 2 |
| Obsolete | 1 |
| Unverifiable | 4 |
| Terms whose name was checked | 27 |
| Terms named correctly | 11 |
| Terms named as a **different** term | 13 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0005117` (1 mention) - the report calls it "Conductive hearing impairment"; HP calls it **Elevated diastolic blood pressure**
- `HP:0004305` (1 mention) - the report calls it "Impaired speech discrimination"; HP calls it **Involuntary movements**
- `GO:0001504` (1 mention) - the report calls it "bone mineralization"; GO calls it **neurotransmitter uptake**
- `CL:0000134` (1 mention) - the report calls it "Osteoblast"; CL calls it **mesenchymal stem cell**
- `CL:0000007` (1 mention) - the report calls it "Fibroblast of connective tissue"; CL calls it **early embryonic cell (metazoa)**
- `CL:0000001` (1 mention) - the report calls it "Neuron"; CL calls it **primary cultured cell**
- `CL:0000004` (1 mention) - the report calls it "Sensory hair cell"; CL calls it **obsolete cell by organism**
- `UBERON:0001756` (1 mention) - the report calls it "otic capsule"; UBERON calls it **middle ear**
- `UBERON:0001686` (1 mention) - the report calls it "stapes"; UBERON calls it **auditory ossicle bone**
- `UBERON:0001825` (1 mention) - the report calls it "cochlea"; UBERON calls it **paranasal sinus**
- `NCIT:C51548` (1 mention) - the report calls it "Stapedectomy"; NCIT calls it **IGF1R wt Allele**
- `NCIT:C51546` (1 mention) - the report calls it "Cochlear Implantation"; NCIT calls it **FLT3 wt Allele**
- `NCIT:C15233` (1 mention) - the report calls it "Hearing Aid"; NCIT calls it **Nutrition Research, Fats, Unsaturated**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0008613` (1 mention), reported as "Otosclerosis" - HP does not contain this term
- `HP:000` (3 mentions) - HP does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `CL:0000004` (obsolete cell by organism) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0030509` (2 mentions) - the report calls it "BMP signaling", "BMP signaling pathway"; GO calls it **BMP signaling pathway**
- `GO:0001837` (1 mention) - the report calls it "epithelial–mesenchymal transition in bone"; GO calls it **epithelial to mesenchymal transition**, and lists "epithelial-mesenchymal transition" among its other names
- `GO:0006954` (1 mention) - the report calls it "inflammatory response – tentative"; GO calls it **inflammatory response**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0030509` - called "BMP signaling", "BMP signaling pathway"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.