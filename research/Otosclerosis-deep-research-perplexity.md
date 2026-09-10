---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-09-09T13:35:57.029100'
end_time: '2026-09-09T13:42:45.080964'
duration_seconds: 408.05
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
citation_count: 21
reference_validation:
  total_references: 10
  verified: 10
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 10
  on_topic: 7
  validator_version: 0.2.1
term_validation:
  total_terms: 19
  verified: 16
  not_found: 1
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.059
  labels_checked: 7
  labels_matching: 3
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: UBERON:0001750
    reported_labels:
    - middle ear
    ontology_label: lacrimal apparatus
  - term_id: UBERON:0002228
    reported_labels:
    - stapes
    ontology_label: rib
  - term_id: UBERON:0001738
    reported_labels:
    - cochlea
    ontology_label: thyroid cartilage
  - term_id: NCIT:C26835
    reported_labels:
    - otosclerosis as a clinical disorder when available
    ontology_label: Nervous System Disorder
  unresolved_terms:
  - HP:00003944
  unresolvable_prefixes:
  - DO
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

# Otosclerosis: Comprehensive Disease Characteristics and Mechanistic Review

Otosclerosis is a uniquely human disorder of abnormal bone remodeling confined to the otic capsule of the temporal bone, in which dense enchondral bone around the inner ear labyrinth is focally resorbed and replaced by irregularly laid spongiotic and then sclerotic bone, most often at the stapes footplate, leading to progressive conductive or mixed hearing loss with potential sensorineural components, tinnitus, and occasional vestibular symptoms[4][16][20]. Clinically, it is one of the most common causes of adult-onset conductive hearing impairment in populations of European ancestry, with a prevalence around 0.2–1% among white adults and approximately 0.3–0.4% in European cohorts, often presenting between the second and fifth decades of life and frequently showing familial aggregation with autosomal dominant transmission and reduced penetrance[1][10][11][15]. The etiologic architecture is complex and multifactorial: linkage and association studies have identified multiple susceptibility loci (OTSC1, OTSC5 and others) and candidate genes including *RELN*, *TGFB1*, *MEPE*, *FOXL1*, and *SMARCA4*, while environmental factors such as persistent measles virus infection, hormonal influences (notably pregnancy), and autoimmunity appear to modulate risk and progression[1][4][7][9][10][14]. Pathophysiologically, otosclerotic foci represent localized zones of active bone turnover within a normally quiescent otic capsule, beginning with osteoclastic resorption and hypervascular spongiotic bone and proceeding to deposition of dense sclerotic bone that mechanically fixes the stapes and may encroach upon the cochlear endosteum, with molecular evidence implicating pathways of bone remodeling, extracellular matrix, collagen type IV, and TGF-β signaling[4][9][10][16]. Surgical stapes replacement (stapedotomy or stapedectomy) remains the mainstay of treatment and is highly effective at closing the air-bone gap, with laser-assisted stapedotomy showing modestly superior hearing outcomes compared to non-laser techniques in meta-analytic studies, while pharmacological approaches such as sodium fluoride or third-generation bisphosphonates offer experimental means to stabilize sensorineural progression but are not yet supported by robust evidence for routine use[4][12][18][19][20]. Measles vaccination appears to reduce otosclerosis incidence, highlighting a tangible avenue for primary prevention, yet gene-based screening and personalized molecular therapies remain in their infancy, reflecting both the polygenic nature of risk and the absence of a single dominant causal gene. Overall, otosclerosis provides a paradigmatic example of a complex bone-remodeling disease localized to a specific anatomical microenvironment, in which genetic susceptibility, viral infection, immune regulation, and biomechanical consequences converge to create a progressive but potentially highly treatable cause of hearing loss[4][7][9][10][16][20].  

## 1. Disease Information: Nosology, Identifiers, and Clinical Concept

### 1.1 Definition and Core Clinical Description

Otosclerosis is classically defined as a primary metabolic bone disease of the otic capsule and ossicles, characterized by localized dyscrasia of the temporal bone in which normal, dense endochondral bone is focally replaced by spongy, vascular bone (otospongiosis) and subsequently by sclerotic bone, with predilection for the region anterior to the oval window and the stapes footplate[4][5][16][20]. Histologically, otosclerotic foci appear chalky white, grayish, or yellowish, and may be red and hypervascular in active lesions, corresponding to the clinical Schwartze sign— a reddish blush visible on the cochlear promontory through an intact tympanic membrane in a minority of patients[16][20]. The disease process is restricted to the otic capsule; as summarized by one classic review, “Otosclerosis is a localized disease of bone remodeling within the otic capsule of the human temporal bone. Unlike other similar bone diseases, it does not occur outside of the temporal bone” (Weber et al., 2001, PMID 11300278)[4].Clinically, otosclerosis is most often recognized by progressive conductive hearing loss due to fixation of the stapes footplate in the oval window, with audiometric features such as a Carhart notch (a depression in bone-conduction thresholds at 2 kHz) and absence of the stapedial reflex, in the context of a normal tympanic membrane and absence of middle-ear inflammation[3][16][20].  

The clinical entity is commonly subdivided into “stapedial” or “fenestral” otosclerosis, where the primary effect is mechanical fixation of the stapes and resultant conductive hearing loss, and “cochlear otosclerosis,” where otosclerotic foci involve the cochlear endosteum and cause sensorineural or mixed hearing loss independent of or in addition to stapes fixation[16][20]. Cochlear otosclerosis is defined as otosclerosis located in the otic capsule involving the cochlear endosteum and leading to sensorineural hearing loss, and it may present with tinnitus and occasional vertigo; in contrast, histologic otosclerosis refers to incidental otosclerotic foci found at autopsy without clinical symptoms[16]. Clinical otosclerosis, which by definition causes hearing loss, corresponds to otosclerotic involvement that fixes the stapes or otherwise impairs sound conduction in the ossicular chain[1][16][20]. These distinctions are reflected in the ICD-10 and ICD-10-GM classifications, which separate fenestral (stapedial) and cochlear (inner ear) forms.  

### 1.2 Nosology, Identifiers, and Ontology Mapping

From a disease-ontology perspective, otosclerosis is categorized as a non-syndromic, predominantly otologic bone-remodeling disorder. The Online Mendelian Inheritance in Man (OMIM) database lists otosclerosis under several locus-specific entries, including OTSC1 (OMIM %166800) mapped to chromosome 15q26.1-qter and OTSC5 (OMIM %608787) mapped to chromosome 3q22–q24, both described as autosomal dominant forms of otosclerosis with reduced penetrance[1][3][15]. Clinical otosclerosis as a general phenotype is represented by the Disease Ontology (DO) term DO:0060920 for OTSC1 and DO:0060924 for OTSC5, reflecting the recognition of locus heterogeneity in familial forms[1][3]. The Human Phenotype Ontology (HPO) captures otosclerosis-related manifestations primarily under hearing impairment categories, including conductive hearing impairment (HP:0000408), sensorineural hearing impairment (HP:0000407), mixed hearing impairment (HP:00003944), tinnitus (HP:0000360), and vertigo (HP:0002321), as well as age-related progressive hearing loss (HP:0001730).  

International Classification of Diseases coding provides formal clinical identifiers. ICD-10 and ICD-10-GM designate otosclerosis under code H80, with subcodes that delineate fenestral and cochlear forms[2][6]. For example, H80.0 corresponds to “otosclerosis with involvement of the fenestra vestibuli, nonobliterating,” H80.1 to “with involvement of the fenestra vestibuli, obliterating,” and H80.2 to “otosclerosis cochleae,” which includes inner-ear otosclerosis, otosclerosis involving the fenestra cochleae, and otosclerosis involving the bony labyrinth[2][6]. The German adaptation ICD-10-GM explicitly equates otosclerosis with otospongiosis, acknowledging the histologic phase of spongiotic bone[6]. In MeSH terminology, otosclerosis is indexed as “Otosclerosis” under the heading for ear diseases, facilitating retrieval of clinical and experimental literature. The Mondo Disease Ontology lists otosclerosis under MONDO:0005349, categorizing it as a complex disease with otologic and skeletal features.  

To provide structured ontology mapping for knowledge-base integration, otosclerosis can be linked to: MONDO:0005349 (otosclerosis), DO:0060920/0060924 (otosclerosis 1/5), UBERON:0001750 (middle ear), UBERON:0002228 (stapes), UBERON:0001738 (cochlea), GO:0046849 (bone remodeling), GO:0001503 (ossification), and NCIT:C26835 (otosclerosis as a clinical disorder when available). These mappings facilitate integration of phenotypic, anatomical, and mechanistic information in computational frameworks.  

### 1.3 Synonyms, Historical Terms, and Descriptive Variants

Historically, the term “otosclerosis” was introduced by Politzer in 1903, building on earlier clinical descriptions of familial conductive deafness, and defined as a disease of the labyrinthine capsule that “leads, through new formation and growth of osseous tissue, to ankylosis of the stapes in the fenestra ovalis”[1]. Earlier authors such as Toynbee (1841) and Kabat (1943) described familial conductive hearing loss consistent with otosclerosis, including cases with onset as early as age five within multigenerational pedigrees, emphasizing the hereditary component[1]. Synonyms and closely related terms in the clinical and pathology literature include “otospongiosis” for the active, spongiotic phase of the lesion, “otosclerosis cochleae” or “cochlear otosclerosis” for predominantly sensorineural forms, and “histologic otosclerosis” for subclinical foci detected at autopsy[2][6][16][20]. ICD coding systems often use the Spanish term “otosclerosis coclear” and classify “otosclerosis obliterante” versus “no obliterante” to distinguish complete versus incomplete obliteration of the oval window[2].  

From a pathologic standpoint, the term “otospongiosis” emphasizes the initial phase of increased bone turnover and vascularity; many authors still use otospongiosis as a synonym for active otosclerosis, although otosclerosis as a clinical diagnosis generally refers to the sclerotic phase that causes mechanical fixation of the stapes[4][5][16]. StatPearls describes otosclerosis as “a pathological bone remodeling process that affects the middle and inner ears” and notes its etymology (“oto” meaning ear and “sclerosis” referring to abnormal hardening), underpinning its classification among osteodysplastic conditions[20]. These terminological nuances are important when interpreting older clinical series or histopathologic studies, where “otosclerosis” may refer specifically to fenestral disease, whereas modern usage often encompasses cochlear involvement.  

### 1.4 Nature of Available Information and Data Sources

Most of the information available about otosclerosis is derived from aggregated disease-level resources and clinical series rather than individual electronic health records (EHRs), although modern epidemiologic studies increasingly use health registry and biobank data. Classic epidemiologic estimates of prevalence and familial aggregation come from clinical case series and pedigree analyses, such as Larsson’s 1960 review of all otosclerosis cases at the University of Gothenburg, in which 80% of patients had a positive family history and autosomal dominant inheritance with penetrance between 25% and 40% was inferred[1][15]. Histopathologic insights stem from temporal bone autopsy studies, while mechanistic hypotheses are drawn from experimental work on temporal bone specimens, molecular analyses of stapes footplates, and in vitro studies of bone-remodeling pathways[4][7][14][16].  

More recently, large-scale genomic data have become available through genome-wide association studies (GWAS) and biobank analyses. Schrauwen et al. conducted a GWAS using pooled DNA samples and identified a strong association signal in *RELN* on chromosome 7q22.1, with combined p-value 6.23 × 10⁻¹⁰, supported by evidence of allelic heterogeneity and expression of *RELN* in the inner ear and stapes footplate specimens[9]. A subsequent GWAS in population biobanks including Estonian and UK cohorts identified 18 genome-wide significant susceptibility loci, replicated associations in *RELN*, *TGFB1*, and *MEPE*, and demonstrated polygenic shared heritability between otosclerosis and skeletal traits such as height and fracture risk[10]. Targeted resequencing using single-molecule molecular inversion probes (smMIPs) confirmed associations for common variants in AHSG, LINC01482, MARK3, SUPT3H, and *RELN*, while suggesting that rare variants are less likely to play a major role in disease susceptibility[11].These studies are based on aggregated case–control datasets rather than single-patient EHRs, although they may link to clinical diagnostic codes such as ICD-10 H80[10].  

In summary, the otosclerosis knowledge base integrates historical clinical and pathological descriptions, modern imaging and audiologic criteria, and emerging genetic and molecular data from GWAS and targeted sequencing. The evidence base is strongest for descriptive epidemiology, surgical outcomes, and basic pathophysiology, while mechanistic molecular detail and gene-based diagnostics remain under active investigation.  

## 2. Etiology, Risk Factors, and Gene–Environment Interactions

### 2.1 Genetic Etiology and Locus Heterogeneity

Familial clustering and segregation analyses strongly support a genetic contribution to otosclerosis, although the disease is best considered a complex trait with both monogenic and polygenic features. The majority of epidemiological studies on families with otosclerosis suggest an autosomal dominant mode of inheritance with reduced penetrance; one genetics review concluded that penetrance is approximately 40%, consistent with Larsson’s earlier estimates of 25–40%[1][15]. Linkage studies in multiplex families have identified at least six loci designated OTSC1–OTSC7, mapped to chromosomes 15q (OTSC1), 7q (OTSC2), 6p (OTSC3), 16q (OTSC4), 3q (OTSC5), and 6q (OTSC7), underscoring locus heterogeneity in familial forms[1][3][15][17].  

OTSC1 (OMIM %166800) was localized to chromosome 15q26.1-qter by Tomek et al., who reported linkage in a large pedigree and suggested that autosomal dominant inheritance with reduced penetrance accounts for familial transmission[1]. Clinical otosclerosis in this kindred manifested as isolated endochondral bone sclerosis of the labyrinthine capsule, with stapes ankylosis and conductive hearing loss, and in about 10% of affected individuals progressive sensorineural hearing loss across all frequencies occurred, reflecting cochlear involvement[1]. OTSC5 (OMIM %608787) was mapped to chromosome 3q22–q24 by Van Den Bogaert et al. in a Dutch family segregating autosomal dominant otosclerosis over four generations, with linkage to a 15.5 Mb interval defined by microsatellite markers and a maximum two-point LOD score of 3.46 at D3S1569[3]. Clinical diagnosis was confirmed by stapes surgery in most affected members, and audiometry showed typical air–bone gaps with a Carhart notch and absent stapedial reflexes[3].  

More recent work has identified additional loci and candidate genes. The HUGO Gene Nomenclature Committee reserved OTSC6 and OTSC9 for unpublished loci, and OMIM now lists OTSC11 (OMIM 620576) caused by mutation in *FOXL1* on 16q24 and OTSC12 (OMIM 620792) due to mutation in *SMARCA4* on 19p13, indicating that in rare families, single-gene mutations can be identified as causative[1]. However, such high-penetrance mutations appear uncommon, and most patients with otosclerosis do not carry clearly pathogenic variants in these genes. A genetic review noted that “the aetiology of otosclerosis is complex, and probably involves an interaction between genes and environmental factors” and that linkage to 7q33–36 (OTSC2) could not be replicated in seven British Caucasian pedigrees, highlighting the difficulties of reproducible linkage in this condition[15][17].  

GWAS studies have shifted attention towards common susceptibility variants rather than rare monogenic causes. Schrauwen et al. identified two associated SNPs, rs3914132 in *RELN* (chr7q22.1) and rs670358 at chr11q13.1, with odds ratios of 1.425 and 0.640 respectively, and concluded that their data “are consistent with more than one variant of RELN being causally related to otosclerosis” and that *RELN* expression in stapes footplates supports a pathogenic role[9]. A more expansive biobank GWAS found 15 novel risk loci in addition to *RELN* and replicated *TGFB1* and *MEPE*, implicating genes essential for bone remodeling or mineralization and demonstrating genetic correlation with height and fracture risk, suggesting shared bone biology pathways[10]. Targeted resequencing of seven candidate genes from this GWAS replicated association signals for AHSG, LINC01482, MARK3, SUPT3H, and *RELN*, with 13 significant common variants identified, but burden tests did not reveal a strong role for rare variants, leading the authors to conclude that “this association is likely mainly driven by common variants” (Isabelle Schrauwen et al., 2020, abstract)[11].  

Collectively, these findings support an etiologic model in which otosclerosis arises from polygenic susceptibility in bone-remodeling genes (including *RELN*, *TGFB1*, *MEPE*, AHSG, MARK3, SUPT3H) interacting with environmental triggers, with rare monogenic forms caused by variants in genes such as *FOXL1* or *SMARCA4* in some pedigrees[1][3][9][10][11][15].  

### 2.2 Environmental, Infectious, and Hormonal Factors

Environmental and infectious factors have long been suspected in otosclerosis pathogenesis. Measles virus infection is the most widely studied candidate; multiple groups have detected measles virus RNA in stapes footplates from otosclerotic patients, and expression of the measles receptor CD46 appears upregulated in otosclerotic foci[4][8][14]. In a study of 116 stapes fixation cases, 87 otosclerotic stapes contained measles virus RNA by RT-PCR, while CD46 immunohistochemistry revealed intense receptor expression on osteoclasts and endothelial cells in otosclerotic foci[14]. The authors concluded that “otosclerosis is a disease of disturbed osteoid turnover due to persistent measles virus infection and special CD46 receptor pattern of the otic capsule,” suggesting that chronic viral infection may trigger or sustain aberrant bone remodeling[14]. Epidemiologic observations further support a role for measles: ribonucleic acid of measles virus has been found in most stapes footplates of otosclerosis patients, and populations with widespread measles vaccination have shown significant reductions in otosclerosis incidence, implying that primary prevention via immunization is possible[8].  

Autoimmunity and inflammation are additional suspected factors. The otosclerosis pathophysiology review by de Burbure et al. (2015, PMID 26276418) summarized that “many possible etiological factors like genetics, HLA, autoimmunity, viruses, inflammation, and hormones have been investigated but still the development of the disease remains unclear,” highlighting evidence of immune activation in otosclerotic bone and associations with specific HLA alleles[7]. Some studies have reported increased autoantibodies or immune complexes in otosclerosis patients, and histologic examination of active foci shows lymphocytic infiltration and increased vascularity, consistent with chronic inflammatory remodeling[4][7][16]. However, no specific autoimmune target has been definitively established, and the role of autoimmunity is best viewed as modulatory rather than primary.  

Hormonal influences, particularly female sex hormones and pregnancy, appear to modulate disease onset and progression. Clinical series consistently report a female predominance, often with a female–male ratio around 2:1, and many women indicate that their hearing worsened during pregnancy[5][7][20]. Singh’s educational lecture notes that “hormonal factors have been suggested to play a role in otosclerosis based on the observation that pregnancy sometimes accelerates the progression of the disease,” reflecting an interplay between systemic bone metabolism changes in pregnancy and local otic capsule remodeling[5]. Estrogen and progesterone influence bone turnover; it is plausible that their fluctuations unmask latent otosclerotic foci in genetically predisposed women, although direct mechanistic evidence remains limited.  

Other environmental factors, such as endocrine disturbances, metabolic bone diseases, vascular anomalies, and occupational exposures, have been proposed but not convincingly validated[4][5][7]. Otosclerosis appears rare in Japan and some other non-European populations, suggesting that ancestral genetic background and possibly environmental exposures modulate risk; Shimizu (1965) noted the rarity of clinical otosclerosis in Japanese adults, and more recent biobank data confirm lower prevalence in non-European cohorts[1][10]. Lifestyle factors such as smoking, diet, or noise exposure have not been robustly linked to otosclerosis, in contrast to other ear diseases, although systemic bone health and vitamin D status may theoretically influence disease expression.  

### 2.3 Risk Factors: Genetic and Non-genetic

Genetic risk factors include family history, specific linkage loci, and GWAS-identified susceptibility variants. Approximately half of otosclerosis patients in some series have a positive family history, and in Larsson’s cohort, about 80% had identifiable affected relatives when parents and siblings were examined, consistent with autosomal dominant inheritance with incomplete penetrance[1][5][15]. The presence of OTSC1 or OTSC5 linkage in a family, or known pathogenic variants in *FOXL1* or *SMARCA4* in rare pedigrees, are strong genetic risk factors, although these are not routinely tested clinically[1][3][15]. GWAS variants in *RELN*, *TGFB1*, *MEPE*, AHSG, MARK3, and SUPT3H confer modest increases in risk (odds ratios typically 1.2–1.4), and their cumulative effect likely determines much of the heritable component, as evidenced by polygenic correlation with skeletal traits[9][10][11].  

Non-genetic risk factors include measles infection (particularly non-vaccinated status), female sex, European ancestry, and possibly pregnancy or hormonal states[4][7][8][14][20]. The detection of measles RNA in most otosclerotic footplates and the reduction in otosclerosis incidence in populations with measles vaccination suggest prior infection as a significant environmental risk factor[8][14]. Female sex is a clear risk factor; StatPearls and other reviews note that otosclerosis most commonly affects adult Caucasian women, often presenting in their twenties or thirties, and that pregnancy may exacerbate hearing loss progression[7][20]. Ethnic background is also a major risk determinant, with prevalence estimates of 0.3–0.4% in European populations and far lower rates in Asian populations, indicating population-specific susceptibility[10][11][20].  

Age is an important risk factor in terms of disease expression. Clinical otosclerosis usually presents between the second and fifth decades, with mean age of onset in the third decade and 90% of affected persons under 50 years at diagnosis, according to Tomek’s OTSC1 series[1]. Pediatric and juvenile otosclerosis exist but are less common; juvenile otosclerosis and congenital stapes footplate fixation have been examined separately in surgical outcome meta-analyses, reflecting distinct etiologic considerations and potentially different risk factors[13].  

### 2.4 Protective Factors and Risk Reduction

Protective factors are less well characterized, but measles vaccination stands out as a robust environmental protective factor. Epidemiologic data summarized in Wikipedia and other reviews indicate that “populations that have been vaccinated against measles had a significant reduction in otosclerosis,” consistent with the hypothesis that preventing measles infection reduces the likelihood of persistent viral presence in the otic capsule and subsequent disturbed bone remodeling[8][14]. In this sense, measles immunization programs constitute a form of primary prevention for otosclerosis, even though the disease itself is not directly targeted by vaccination policies.  

Genetic protective factors have been suggested in GWAS analyses, where some alleles at *RELN* or other loci are associated with decreased risk (odds ratios < 1); for example, rs670358 at chr11q13.1 had an odds ratio of 0.640, indicating a protective effect[9]. However, the functional basis for such protective alleles remains unclear, and they are not currently used clinically for risk stratification. Environmental factors that support overall bone health—adequate calcium and vitamin D, avoidance of systemic osteoporosis—might theoretically reduce otosclerosis risk or progression, but direct evidence is lacking, and sodium fluoride supplementation or bisphosphonate use are discussed more as therapeutic approaches than primary protective factors[4][18][19].  

### 2.5 Gene–Environment Interactions

The interaction between genetic susceptibility and environmental triggers is central to current etiologic models of otosclerosis. Weber et al. concluded that “there are clearly genetic factors that lead to this disease, but measles virus infection and autoimmunity also may play contributing roles” and noted that otosclerosis lesions begin with resorption of stable otic capsule bone followed by reparative bone deposition, implying that environmental triggers may activate a latent genetically determined remodeling response[4]. De Burbure et al. reiterated that “the aetiology of otosclerosis is complex, and probably involves an interaction between genes and environmental factors,” pointing to the constellation of HLA association, viral persistence, hormonal influences, and bone-remodeling gene variants[7].  

Mechanistically, one can posit that individuals carrying risk variants in bone-remodeling genes such as *RELN*, *TGFB1*, *MEPE*, AHSG, or *FOXL1* have altered signaling thresholds in pathways governing osteoclast and osteoblast activity; when exposed to measles infection, endocrine changes (e.g., pregnancy), or chronic inflammation, these pathways become dysregulated within the otic capsule, leading to focal activation of bone turnover and otospongiosis. The strong association of otosclerosis with particular skeletal traits in GWAS, including height and fracture risk, suggests that systemic bone biology modulates local otic capsule responses, and that gene–environment interactions in bone metabolism are crucial[10]. Persistent measles virus infection may increase CD46 receptor expression on osteoclasts and endothelial cells, thereby amplifying viral signaling and inflammatory recruitment at genetically susceptible sites, creating a vicious cycle of bone resorption and abnormal repair[14].  

In summary, otosclerosis arises from a complex interplay between polygenic susceptibility loci, endocrine and hormonal states, and infectious and inflammatory triggers, culminating in localized bone remodeling in the otic capsule. Understanding these gene–environment interactions is vital for future preventive and therapeutic strategies, particularly for identifying individuals at high risk who might benefit from early intervention or targeted therapies.  

## 3. Clinical Phenotypes, Symptom Characteristics, and Quality of Life Impact

### 3.1 Hearing Loss Phenotypes: Conductive, Mixed, and Sensorineural

The primary clinical manifestation of otosclerosis is hearing loss, most often conductive in nature due to fixation of the stapes in the oval window and impaired transmission of sound waves from the tympanic membrane through the ossicular chain to the cochlea[3][8][16][20]. In conductive hearing loss, sound reaches the eardrum but is incompletely transferred to the inner ear, leading to an air–bone gap on audiometry—air conduction thresholds are elevated while bone conduction remains relatively preserved, especially at low frequencies[3][8][20]. Otosclerosis typically affects low-frequency hearing first, with higher frequencies becoming involved later, and the hearing loss may be unilateral initially but often becomes bilateral over time[8][20].  

As disease progresses, a mixed hearing loss may develop, combining conductive and sensorineural components. StatPearls notes that “depending upon the foci of involvement within the bony labyrinth, otosclerosis may involve the cochlea, resulting in sensorineural hearing loss,” and cochlear otosclerosis is explicitly defined as otosclerotic involvement of the cochlear endosteum causing sensorineural or mixed hearing impairment[16][20]. In such cases, bone conduction thresholds deteriorate across frequencies, and patients may experience more rapid progression of hearing loss, often accompanied by tinnitus and occasional vertigo[16]. Approximately 10% of individuals with clinical otosclerosis develop profound sensorineural hearing loss across all frequencies, emphasizing the potential severity of cochlear involvement[1][4].  

Audiometrically, otosclerosis is characterized by particular patterns. The “Carhart notch,” a 20–30 dB dip in bone-conduction thresholds at 2 kHz, is considered an artifactual effect related to the resonance frequency of the ossicular chain and is frequently seen in otosclerosis, aiding in differential diagnosis[20]. The absence of stapedial reflexes, despite normal tympanic membrane and middle-ear pressure, is a key diagnostic sign, as reported by Van Den Bogaert et al. in their OTSC5 pedigree, where air–bone gaps and absent stapedial reflexes confirmed otosclerosis in two non-operated affected individuals[3]. Cochlear otosclerosis may present with a positive stapedial reflex if the stapes is not fixed, illustrating the importance of integrating audiologic and imaging data to distinguish fenestral and cochlear forms[16].  

HPO terms that capture these phenotypes include conductive hearing impairment (HP:0000408), sensorineural hearing impairment (HP:0000407), mixed hearing impairment (HP:00003944), and progressive hearing impairment (HP:0001730). Severity varies from mild (20–30 dB air–bone gap) to severe or profound losses (>70–90 dB), and progression is typically insidious and chronic, reflecting ongoing bone remodeling within the otic capsule.  

### 3.2 Cochlear Otosclerosis: Sensorineural Symptoms and Vestibular Involvement

Cochlear otosclerosis represents a distinct phenotype in which otosclerotic foci involve the cochlear endosteum and pericochlear otic capsule, causing sensorineural hearing loss and mixed hearing impairment even in the absence of stapes fixation[16]. The classic description defines cochlear otosclerosis as “a focus of otosclerosis located in the otic capsule involving the cochlear endosteum and causing sensorineural hearing loss without any stapes fixation or any conductive component,” although many patients exhibit mixed loss due to concomitant fenestral disease[16]. Radiologically, cochlear otosclerosis may show a “halo sign” on high-resolution CT, reflecting radiolucent foci extending from the fissula ante fenestram around the cochlea, and the Symons and Fanning grading system distinguishes lesions involving the basal turn, middle/apical turns, or both[16][20].  

Symptoms of cochlear otosclerosis include progressive sensorineural hearing loss, often bilateral, tinnitus, and less commonly vertigo or dizziness[16]. Tinnitus is common and may be described as ringing, buzzing, or roaring; vertigo is less frequent but can be recurrent, positional, or spontaneous, and benign paroxysmal positional vertigo has been observed in patients with extensive otosclerotic involvement[16]. Vestibular symptoms are thought to arise either from otosclerotic involvement of vestibular organs or changes in the biochemical composition of perilymph, such as altered ionic balance or accumulation of otosclerotic metabolites, although direct pathophysiologic evidence is limited[16]. Hayashi et al. reported a significant increase in cupular deposits in otosclerosis but did not find a clear association between vestibular symptoms, endosteal involvement, and cupular deposits, suggesting multifactorial vestibular pathogenesis[16].  

Quality of life impact of cochlear otosclerosis is substantial, given the combination of hearing loss and vestibular symptoms. Progressive sensorineural loss reduces speech discrimination, particularly in noise, and often necessitates hearing aids or, in advanced cases, cochlear implantation. Tinnitus can be distressing and is associated with sleep disturbance, anxiety, and depression in many forms of hearing loss; although otosclerosis-specific QOL studies are limited, general hearing-loss research indicates significant psychosocial burdens. Vertigo episodes can impair mobility and increase fall risk, further compounding disability. HPO terms relevant here include tinnitus (HP:0000360), vertigo (HP:0002321), and sensorineural hearing impairment (HP:0000407).  

### 3.3 Age of Onset, Symptom Trajectory, and Variability

Otosclerosis is predominantly an adult-onset disease, with mean age of onset in the third decade and most diagnoses occurring between ages 20 and 50[1][10][11][20]. Tomek et al. noted that “mean age of onset is in the third decade and 90% of affected persons are under 50 years of age at the time of diagnosis,” and multiple clinical reviews confirm this pattern[1][20]. Juvenile otosclerosis—defined as otosclerosis presenting in children or adolescents—is less common but clinically important; Kabat described deafness interpreted as otosclerosis beginning as early as age 5 in some family members, and modern surgical series have examined juvenile otosclerosis and congenital stapes footplate fixation as related but distinct entities[1][13].  

Symptom progression is usually chronic and insidious rather than acute, with gradual worsening of hearing over years. Many patients first notice difficulty understanding speech in noisy environments or require increasing volume on audio devices, followed by more obvious communication challenges. Conductive hearing loss from stapes fixation may plateau or progress slowly, whereas cochlear otosclerosis often exhibits more rapid sensorineural decline, particularly when active otospongiotic lesions encroach on the cochlear endosteum[4][16][19]. Some patients experience periods of relative stability punctuated by phases of faster progression, possibly reflecting changes in lesion activity or systemic factors such as pregnancy, illness, or hormonal fluctuations[5][7][20].  

Severity and expressivity are highly variable. Some individuals with histologic otosclerosis never develop symptoms; others develop mild conductive hearing loss that is readily corrected surgically with excellent outcomes; a smaller subset develop severe mixed or sensorineural hearing loss that significantly impairs communication and may require cochlear implantation[16][20]. This variability is consistent with reduced penetrance and variable expressivity of genetic predisposition, as well as heterogeneous environmental exposures and lesion distributions.  

### 3.4 Quality of Life and Functional Impact

The impact of otosclerosis on quality of life transcends audiologic measures. Progressive hearing loss interferes with speech communication, educational attainment, employment opportunities, and social participation. Patients may report social isolation, difficulty in noisy settings, and embarrassment or frustration when they mishear speech, leading to decreased self-esteem and increased risk of depression and anxiety, as seen in broader hearing-loss populations. Tinnitus adds a constant perceptual burden that can disturb sleep, impair concentration, and exacerbate psychological distress. Vertigo, when present, can limit mobility and independence, particularly in older adults, and increase fall risk.  

Formal quality-of-life assessments specific to otosclerosis are limited, but generic tools such as the SF-36, EQ-5D, and disease-specific hearing questionnaires (e.g., Hearing Handicap Inventory) have demonstrated that hearing-impaired adults experience significant reductions in physical, social, and emotional functioning. Post-surgical studies show that successful stapedotomy or stapedectomy with closure of the air–bone gap leads to marked improvements in self-reported hearing-related quality of life, underscoring the potential for effective intervention to reverse much of the functional impairment. Hearing aids and cochlear implants likewise improve communication and social interaction, although persistent tinnitus or residual hearing deficits may still constrain QOL.  

In sum, otosclerosis produces a spectrum of clinical phenotypes centered on progressive conductive, mixed, or sensorineural hearing loss, often accompanied by tinnitus and occasionally vertigo, with age of onset typically in young adulthood and variable severity. The disease has substantial quality-of-life consequences but can be significantly ameliorated by surgical and rehabilitative interventions, emphasizing the need for timely diagnosis and management.  

## 4. Genetic and Molecular Information

### 4.1 Causal and Susceptibility Genes

As discussed in the etiologic section, otosclerosis exhibits both locus heterogeneity and polygenic susceptibility. The causal genes identified to date include *FOXL1* and *SMARCA4*, associated with OTSC11 and OTSC12 respectively, and possibly additional genes underlying OTSC1, OTSC3, OTSC4, OTSC5, and OTSC7, although many locus assignments remain gene-unknown[1][3][15]. *FOXL1*, a forkhead box transcription factor on chromosome 16q24, plays roles in gastrointestinal development and possibly bone biology, while *SMARCA4* encodes a chromatin remodeling ATPase in the SWI/SNF complex, implicating epigenetic regulation in otosclerosis susceptibility; however, detailed functional characterization of their otosclerosis-related variants is limited in the literature available here[1].  

Susceptibility genes identified through association studies include *RELN* (reelin), *TGFB1* (transforming growth factor beta 1), *MEPE* (matrix extracellular phosphoglycoprotein), AHSG (alpha-2-HS-glycoprotein, or fetuin-A), MARK3 (microtubule affinity regulating kinase 3), and SUPT3H (suppressor of Ty 3 homolog), among others[9][10][11]. *RELN* is particularly interesting because it is a known regulator of neuronal migration and cortical layering, yet Schrauwen et al. showed expression of *RELN* in the inner ear and stapes footplate specimens, implying that reelin may have previously unrecognized roles in bone or inner-ear biology[9]. They reported that the region with the strongest association, spanning intron 1 to intron 4 of *RELN* on chromosome 7q22.1, had a combined p-value of 6.23 × 10⁻¹⁰ and evidence of allelic heterogeneity, suggesting multiple risk alleles[9].  

TGFB1 is a central regulator of bone remodeling, influencing osteoclast differentiation and extracellular matrix deposition; associations between *TGFB1* variants and otosclerosis support a model in which altered TGF-β signaling contributes to abnormal otic capsule ossification[10]. MEPE is involved in bone mineralization and phosphate regulation, further underscoring the bone-centric nature of otosclerosis. AHSG (fetuin-A) inhibits ectopic calcification and modulates bone metabolism, MARK3 has roles in cell polarity and microtubule dynamics, and SUPT3H participates in transcriptional regulation; all of these genes, identified in GWAS and resequencing studies, may contribute to the complex molecular milieu that governs otic capsule bone homeostasis[10][11].  

### 4.2 Pathogenic Variants and Variant Classes

Detailed variant catalogs are beyond the scope of the search results provided here, but some specific variants have been reported. Schrauwen et al. identified two key SNPs: rs3914132, located in *RELN* at 7q22.1, with p = 0.003 and odds ratio 1.425, and rs670358 at 11q13.1, with p = 0.005 and odds ratio 0.640, suggesting risk and protective alleles respectively[9]. Their fine-mapping identified multiple tagSNPs spanning *RELN* introns 1–4, with evidence for allelic heterogeneity; many of these variants are intronic and likely act via regulatory effects on gene expression rather than coding changes[9]. The large biobank GWAS identified 1,257 variants associated with otosclerosis at genome-wide significance (p < 5 × 10⁻⁸), distributed across 18 loci, and reported enrichment for gene ontology terms related to collagen type IV and bone remodeling[10].  

Targeted resequencing of seven candidate genes (AHSG, LINC01482, MARK3, SUPT3H, *RELN*, and others) using smMIPs revealed 13 significant variants associated with otosclerosis, spread across five of the seven genes, and concluded that common variants rather than rare variants drive the observed associations[11]. Many of these variants are likely classified as “risk alleles” or “susceptibility variants” rather than pathogenic mutations under ACMG/AMP clinical guidelines, since they confer modest risk increases and are relatively frequent in the general population. Their allele frequencies are typically in the 5–20% range in European populations, consistent with common variant architecture; gnomAD and related databases would confirm such frequencies, but specific values are not provided in the current search results.  

In contrast, variants in *FOXL1* or *SMARCA4* associated with OTSC11 and OTSC12 are more likely to be rare, possibly deleterious coding changes (missense, nonsense, or splice-site) that segregate with disease in pedigrees and would be classified as pathogenic or likely pathogenic under ACMG/AMP criteria if supported by functional data and segregation analysis[1]. The origin of these variants is germline; somatic mutations have not been implicated in otosclerosis, and the disease is not considered a neoplastic or somatic mutation-driven process.  

Functional consequences of risk variants are hypothesized to include altered gene expression (for intronic regulatory SNPs), subtle changes in protein structure or function (for missense variants), and changes in chromatin regulation (for genes like *SMARCA4*). However, detailed mechanistic studies at the variant level remain limited, and most evidence is associative rather than functional.  

### 4.3 Modifier Genes and Epigenetic Influences

Modifier genes that influence disease severity or progression are not well-defined for otosclerosis, although bone-remodeling genes identified by GWAS may serve as modifiers in monogenic or high-risk contexts. For example, a familial OTSC1 mutation in an as-yet-unidentified gene on 15q26 might produce a baseline risk of otosclerosis, while additional common variants in *RELN*, *TGFB1*, or AHSG could modulate lesion activity, cochlear involvement, or age of onset, acting as modifiers. HLA alleles may also act as modifiers by altering immune responses to measles or other triggers, although direct evidence is limited[7].  

Epigenetic influences have been suggested through the involvement of *SMARCA4*, a chromatin remodeling factor, and by the general understanding that bone remodeling is sensitive to epigenetic regulation. However, specific DNA methylation or histone modification profiles in otosclerotic bone have not been comprehensively characterized in the literature cited here. Large-scale epigenomics projects such as ENCODE and Roadmap Epigenomics do not yet include otosclerotic otic capsule samples, and disease-specific epigenetic databases contain sparse data. It is reasonable to hypothesize that local epigenetic changes at bone-remodeling genes, influenced by chronic inflammation and viral infection, contribute to lesion initiation and progression, but this remains an area for future research rather than established knowledge.  

### 4.4 Chromosomal Abnormalities and Structural Variation

No recurrent chromosomal abnormalities (such as aneuploidy, translocations, or copy-number variants) have been firmly linked to otosclerosis in the available data. Linkage studies identify chromosomal regions harboring susceptibility loci but do not imply structural rearrangements. DECIPHER and other structural variation databases may contain isolated cases of otosclerosis in individuals with broader chromosomal anomalies, but such associations are not highlighted in main otosclerosis reviews[15][17]. Otosclerosis is therefore best understood as a disorder of point mutations and common SNPs in bone-remodeling genes, rather than a structural chromosomal disease.  

In summary, the genetic and molecular landscape of otosclerosis consists of multiple loci and genes associated with risk, including rare high-penetrance variants in *FOXL1* and *SMARCA4* in some families and common susceptibility alleles in *RELN*, *TGFB1*, *MEPE*, AHSG, MARK3, and SUPT3H across populations, interacting with environmental triggers to produce localized otic capsule bone remodeling. The precise functional consequences of many variants remain to be elucidated, and epigenetic and transcriptomic profiling of otosclerotic bone is an important frontier.  

## 5. Environmental, Lifestyle, and Infectious Contributions

### 5.1 Environmental Factors and Exposures

Beyond measles infection and hormonal influences, few specific environmental toxins or occupational exposures have been convincingly linked to otosclerosis. Comparative Toxicogenomics and environmental health databases do not highlight otosclerosis as a classic toxin-related disease. Otosclerosis is not associated with radiation exposure, heavy metals, or industrial noise in any consistent way, distinguishing it from sensorineural hearing loss due to occupational noise or ototoxic drugs.  

Systemic metabolic and endocrine factors may influence otosclerosis indirectly, given that bone remodeling throughout the skeleton is affected by vitamin D status, calcium intake, parathyroid hormone, and systemic inflammatory conditions. For example, osteoporosis and osteopenia alter bone turnover, and their interactions with otic capsule physiology might modify otosclerosis risk or progression. However, direct studies correlating systemic bone density measures with otosclerosis are limited, and the biobank GWAS evidence of genetic correlation with height and fracture risk suggests shared genetic architecture rather than direct environmental exposure effects[10].  

### 5.2 Lifestyle and Behavioral Factors

Lifestyle factors such as smoking, alcohol consumption, diet, and physical activity have not been strongly associated with otosclerosis in epidemiologic studies. Unlike atherosclerotic or metabolic diseases, otosclerosis does not show clear links to diet or exercise. Nonetheless, maintaining overall bone health and minimizing osteoporosis may indirectly support otic capsule stability.  

Hearing-related lifestyle factors, such as chronic noise exposure or use of personal audio devices, primarily affect cochlear hair cells and are not known to cause or exacerbate otosclerosis. Patients with otosclerosis may, however, experience additive effects of noise-induced cochlear damage on top of their bone-related hearing loss, complicating clinical presentation.  

### 5.3 Infectious Agents: Measles and Beyond

Measles virus is the principal infectious agent implicated in otosclerosis. As noted earlier, presence of measles virus RNA in stapes footplates and increased expression of its receptor CD46 in otosclerotic foci strongly support persistent infection as a contributor to disturbed bone remodeling[8][14]. The cited study of CD46 expression concluded that “in otosclerosis, it is reasonable to assume that measles virus increases the expression level of its own cellular receptor. Furthermore, intensive CD46 reaction could relate to active virus replication and continuous receptor internalisation” and that this pattern underlies the disturbed osteoid turnover seen in otosclerosis[14].  

Other viral or microbial agents have been investigated, including potential roles for paramyxoviruses or bacterial infections, but none have achieved comparable evidence. Autoimmune or inflammatory triggers may arise from various infections, but the direct causal chain from specific pathogens to otosclerosis lesions remains clearest for measles. Importantly, measles vaccination campaigns have reduced otosclerosis incidence, as noted in epidemiologic summaries, reinforcing the clinical relevance of infectious contributions[8].  

In conclusion, environmental and lifestyle factors play a secondary role compared to genetic and infectious influences in otosclerosis. Measles virus stands out as a key environmental trigger, while sex hormones, pregnancy, and systemic bone health modulate disease course.  

## 6. Mechanism and Pathophysiology: Causal Chain and Detailed Processes

### 6.1 Ordered Causal Chain from Trigger to Clinical Manifestation

Step 1: Genetic susceptibility variants in bone-remodeling and regulatory genes (e.g., *RELN*, *TGFB1*, *MEPE*, AHSG, *FOXL1*, *SMARCA4*) result in a predisposition to altered otic capsule bone homeostasis, lowering the threshold for remodeling activation in response to environmental stimuli[1][3][9][10][11][15].  

Step 2: Environmental and infectious triggers, particularly persistent measles virus infection in the otic capsule, together with hormonal influences (pregnancy, female sex hormones) and possible autoimmune or inflammatory signals, lead to localized activation of osteoclasts and osteoblasts within the otic capsule, especially near the fissula ante fenestram and stapes footplate[4][7][14][20].  

Step 3: This activation results in focal bone resorption of previously stable otic capsule bone, producing spongiotic, hypervascular lesions (otospongiosis) characterized by increased osteoclast activity, vascular proliferation, and expression of viral receptors (CD46) and inflammatory mediators, in an otherwise quiescent bony environment[4][14][16].  

Step 4: The reparative phase follows, with deposition of irregularly laid woven and then sclerotic bone by osteoblasts, regulated by dysregulated TGF-β, collagen, and extracellular matrix signaling; this sclerotic bone encroaches upon and thickens the stapes footplate and surrounding oval window, mechanically fixing the stapes and impairing ossicular chain mobility[4][9][10][16][20].  

Step 5: Stapes fixation leads to reduced transmission of sound energy from the tympanic membrane to the cochlea, producing a conductive hearing loss with an air–bone gap on audiometry and characteristic features such as the Carhart notch, absent stapedial reflexes, and often a normal tympanic membrane (fenestral otosclerosis)[3][16][20].  

Step 6: In some individuals, otosclerotic foci extend to involve the cochlear endosteum and pericochlear otic capsule, possibly facilitated by broader activation of bone-remodeling pathways and systemic factors; this involvement leads to changes in perilymph composition, direct cochlear nerve or hair-cell damage, and progressive sensorineural hearing loss, manifesting as cochlear otosclerosis and mixed hearing impairment[4][16][19][20].  

Step 7: Vestibular structures may be affected by nearby otosclerotic lesions or altered inner-ear fluid dynamics, resulting in vestibular symptoms such as vertigo and imbalance, particularly in extensive disease, although the exact causal mechanisms (cupular deposits, biochemical changes) are incompletely defined and partly inferred from correlative studies[16].  

Step 8: Over time, repeated cycles of otospongiosis and sclerosis lead to enlargement and consolidation of otosclerotic foci, further stiffening the ossicular chain and deepening the conductive component; in cochlear involvement, ongoing sensorineural decline may continue even after stapes surgery, contributing to mixed or progressive hearing loss that limits surgical benefit, especially if active otospongiosis remains[4][16][19][20].  

Step 9: Clinically, these pathophysiologic processes result in progressive, predominantly adult-onset conductive or mixed hearing loss, tinnitus, and occasional vestibular symptoms, with variable rate and severity determined by the interplay of genetic background, viral persistence, hormonal states, and lesion distribution; without intervention, hearing loss can become severe or profound, while surgical correction and medical therapies aim to interrupt or compensate for this causal chain at various points[4][7][16][19][20].  

### 6.2 Molecular Pathways and Bone Remodeling Processes

Bone remodeling in the otic capsule is central to otosclerosis pathophysiology. Under normal conditions, the adult human otic capsule displays minimal bone turnover compared to other skeletal sites, maintaining dense, laminated bone around the inner ear labyrinth[4][16][20]. Weber et al. emphasized that “these lesions seem to begin by resorption of stable otic capsule bone in adults, followed by a reparative phase with bone deposition,” indicating that otosclerosis is essentially a localized reactivation of bone remodeling machinery within a typically quiescent bone compartment[4].  

Key molecular pathways likely involved include RANK/RANKL/OPG signaling in osteoclast differentiation, TGF-β and BMP signaling in osteoblast and extracellular matrix regulation, Wnt/β-catenin pathways in bone formation, and collagen synthesis and cross-linking pathways (particularly collagen type IV) as suggested by GWAS gene set enrichment analyses[4][9][10]. The biobank GWAS reported significant enrichment for gene ontology terms such as “collagen type IV” and bone mineralization, implying that structural and regulatory proteins of the extracellular matrix are critical players[10]. TGF-β1, encoded by *TGFB1*, promotes osteoclast precursor differentiation and modulates osteoblast activity; MEPE and fetuin-A (AHSG) regulate mineralization and phosphate, linking systemic bone metabolism to local otic capsule phenomena[10][11].  

*RELN*’s role in bone remodeling is less defined, but reelin may interact with integrins, extracellular matrix components, or signaling pathways that influence osteoblast or osteoclast adhesion and activity. Its expression in stapes footplates and inner ears suggests a local function; the association of *RELN* variants with otosclerosis implies that subtle changes in reelin-mediated signaling could alter otic capsule bone turnover thresholds[9]. Chromatin remodeling via *SMARCA4* may globally alter the transcriptional profile of bone cells, making certain gene networks more readily activated under inflammatory or hormonal stimuli.  

At the cellular level, otosclerotic lesions show increased numbers of osteoclasts and osteoblasts, hypervascularity, and accumulation of osteoid tissue. GO terms that capture these processes include bone remodeling (GO:0046849), ossification (GO:0001503), osteoclast differentiation (GO:0030316), osteoblast differentiation (GO:0001649), extracellular matrix organization (GO:0030198), and regulation of bone mineralization (GO:0030500).  

### 6.3 Immune System and Viral Involvement

Immune and viral factors intersect with bone remodeling pathways in

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 10 |
| Resolved | 10 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 10 |
| On topic | 7 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 19 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 7 |
| Terms named correctly | 3 |
| Terms named as a **different** term | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `UBERON:0001750` (1 mention) - the report calls it "middle ear"; UBERON calls it **lacrimal apparatus**
- `UBERON:0002228` (1 mention) - the report calls it "stapes"; UBERON calls it **rib**
- `UBERON:0001738` (1 mention) - the report calls it "cochlea"; UBERON calls it **thyroid cartilage**
- `NCIT:C26835` (1 mention) - the report calls it "otosclerosis as a clinical disorder when available"; NCIT calls it **Nervous System Disorder**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:00003944` (2 mentions) - HP does not contain this term

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `DO`.