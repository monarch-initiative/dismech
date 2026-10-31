---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-10-15T14:54:54.758974'
end_time: '2026-10-15T14:57:41.424372'
duration_seconds: 166.67
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Oculoauricular Syndrome
  mondo_id: MONDO:0012802
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: low
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 53
reference_validation:
  total_references: 19
  verified: 19
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 19
  on_topic: 6
  off_topic: 1
  off_topic_references:
  - PMC:PMC5123892
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 67
  verified: 64
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 9
  labels_matching: 0
  labels_mismatched: 9
  mislabelled_terms:
  - term_id: DOID:0060482
    reported_labels:
    - Disease Ontology
    ontology_label: oculoauricular syndrome
  - term_id: HP:0000568
    reported_labels:
    - Reduced visual potential, cosmetic and orbital-development effects
    ontology_label: Microphthalmia
  - term_id: HP:0000482
    reported_labels:
    - Complicates surgery and refraction
    ontology_label: Microcornea
  - term_id: HP:0007700
    reported_labels:
    - Risk of corneal opacity, glaucoma and impaired vision
    ontology_label: Ocular anterior segment dysgenesis
  - term_id: HP:0012376
    reported_labels:
    - Contributes to refractive and surgical complexity
    ontology_label: Microphakia
  - term_id: HP:0000510
    reported_labels:
    - Night blindness, field constriction and progressive visual disability
    ontology_label: Rod-cone dystrophy
  - term_id: HP:0001104
    reported_labels:
    - Poor central acuity
    ontology_label: Macular hypoplasia
  - term_id: HP:0000639
    reported_labels:
    - Impaired fixation and acuity
    ontology_label: Nystagmus
  - term_id: HP:0000356
    reported_labels:
    - Primarily cosmetic; may affect device fitting
    ontology_label: Abnormality of the outer ear
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
- **Disease Name:** Oculoauricular Syndrome
- **MONDO ID:** MONDO:0012802 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Oculoauricular Syndrome** covering all of the
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

# Oculoauricular syndrome: disease-characteristics research report

**Disease:** Oculoauricular syndrome, Schorderet type  
**Mondo:** **MONDO:0012802**  
**OMIM:** **612109**  
**Causal gene:** **HMX1**  
**Inheritance:** **Autosomal recessive**  
**Evidence cut-off:** 15 October 2026

## Executive summary

Oculoauricular syndrome (OAS) is an exceptionally rare congenital Mendelian disorder caused by **biallelic pathogenic variants in HMX1**, a homeobox transcription-factor gene. Its defining combination is:

1. **Developmental eye malformations**, particularly microphthalmia, microcornea, anterior-segment dysgenesis, congenital or developmental cataract, and ocular coloboma;
2. **Early-onset, progressive rod-cone retinal dystrophy** with substantial visual impairment; and
3. **Characteristic external-ear cartilage malformations**, including low-set or protruding pinnae, crumpled helices, narrow external acoustic meatus/intertragic notch, and absent or cleft lobules.

OMIM assigns phenotype number **612109** and maps it to **HMX1 at 4p16.1** with autosomal-recessive inheritance; MedGen maps the condition to **MONDO:0012802, ORPHA:157962**, and Concept ID **C2677500**.[31][33] This entity must not be conflated with **oculo-auriculo-vertebral spectrum/Goldenhar syndrome**, which usually involves facial asymmetry, mandibular hypoplasia, epibulbar dermoids, vertebral anomalies, and a heterogeneous or multifactorial etiology.

The human evidence base remains extremely small. The first family was published in 2008, and a 2026 cohort paper described the fifth documented family; a separate July 2026 case report adds another likely family. Therefore, percentages should not be inferred from ontology databases: fewer than approximately a dozen molecularly confirmed individuals in about six families have been reported in sufficient detail. The recent 2026 reports expanded the allelic series with **c.570_571del, p.(Glu191Argfs*34)** and **c.233_251dup, p.(Ala85Argfs*53)**.[145][5]

---

# 1. Disease information

## 1.1 Definition

OAS is a congenital developmental disorder in which loss or severe disruption of HMX1 function interferes with formation of the eye, retina, and external ear. MedGen defines it as complex ocular anomalies—congenital cataract, anterior-segment dysgenesis, iris coloboma, and early retinal dystrophy—together with dysplastic external-ear cartilage.[33]

A concise knowledge-base definition is:

> **A rare autosomal-recessive developmental disorder caused by biallelic HMX1 variants and characterized by congenital eye malformations, progressive rod-cone dystrophy, and distinctive malformation of the external ear.**

## 1.2 Identifiers and nomenclature

| Resource | Identifier/name | URL or qualification |
|---|---|---|
| MONDO | **MONDO:0012802**, oculoauricular syndrome | Confirmed through MedGen/Monarch mapping.[33] |
| OMIM phenotype | **OMIM 612109**, Oculoauricular syndrome | [OMIM phenotype/gene entry](https://omim.org/entry/142992); AR, mapping key 3.[31] |
| OMIM gene | **OMIM 142992**, HMX1 | Same OMIM gene entry.[31] |
| Orphanet | **ORPHA:157962** | Cross-reference reported by MedGen and MGI.[106][110] |
| MedGen | **C2677500**, UID 393758 | [NCBI MedGen](https://ncbi.nlm.nih.gov/medgen/393758).[33] |
| MeSH supplementary concept | **C567416** | MGI cross-reference.[110] |
| Disease Ontology | **DOID:0060482** | MGI cross-reference.[110] |
| ICD-10/ICD-10-CM | **Q87.8**, other specified congenital-malformation syndromes, not elsewhere classified | This is a broad umbrella code, not disease-specific.[105] |
| ICD-11 | No dedicated disease-specific code identified | Use the appropriate congenital-malformation syndrome parent and genetic-disease extension where required locally. |
| GTR condition | C2677500, Oculoauricular syndrome | [NCBI GTR](https://www.ncbi.nlm.nih.gov/gtr/conditions/C2677500/); currently lists HMX1-associated testing.[36] |

**Synonyms**

- Oculoauricular syndrome
- Oculo-auricular syndrome
- Oculoauricular syndrome, Schorderet type
- Schorderet–Munier–Franceschetti syndrome
- OCACS
- Microphthalmia–microcornea–anterior-segment dysgenesis–cataract–ocular-coloboma–retinal-dystrophy–external-ear-anomalies syndrome.[106]

## 1.3 Evidence granularity

Most information is **aggregated from disease resources**—OMIM, Orphanet, MedGen, GTR, HPO-derived databases—but ultimately derives from a handful of published pedigrees. It is not based on a large registry or EHR-derived cohort. Patient-level details in the primary literature are therefore disproportionately important, while database percentages can be misleading.

---

# 2. Etiology

## 2.1 Primary causal factor

The established cause is a **biallelic germline pathogenic or likely pathogenic variant in HMX1**, generally causing loss of transcription-factor function. The original 2008 pedigree carried a homozygous 26-bp deletion producing a truncated protein without the complete homeodomain. The abstract states:

> “Linkage analysis and mutation screening revealed in the first exon of the NKX5-3 gene a homozygous 26 nucleotide deletion, generating a truncating protein that lacked the complete homeodomain.”

—Schorderet et al., *American Journal of Human Genetics*, 2 May 2008; **PMID: 18423520**, DOI 10.1016/j.ajhg.2008.03.007; [PubMed](https://pubmed.ncbi.nlm.nih.gov/18423520/).[61]

The human inheritance pattern, segregation, and model-organism findings collectively support a **loss-of-function disease mechanism**.

## 2.2 Genetic risk factors

- Homozygosity or, in principle, compound heterozygosity for pathogenic **HMX1** alleles.
- Parental consanguinity, which increases the probability that both parents carry the same rare allele.
- Having two carrier parents: each pregnancy has the standard autosomal-recessive expectation of **25% affected, 50% carrier, and 25% unaffected/non-carrier**, assuming both parental variants are confirmed and no unusual mosaicism.
- Family history of the eye-plus-external-ear phenotype.

No reproducible susceptibility loci, polygenic scores, or GWAS associations have been established.

## 2.3 Environmental, infectious, and lifestyle risks

There is **no evidence that toxins, infection, diet, smoking, alcohol, occupation, pollution, or postnatal lifestyle cause HMX1-related OAS**. Environmental teratogens can produce overlapping microphthalmia or external-ear malformations and are therefore relevant to differential diagnosis, but not established causes of molecularly confirmed OAS.

## 2.4 Protective factors and gene–environment interaction

No protective HMX1 allele, modifier allele, dietary intervention, medication, or environmental exposure has been demonstrated to reduce penetrance. No disease-specific gene–environment interaction has been established. General avoidance of teratogens is sound prenatal care but is not proven to prevent OAS in a fetus carrying biallelic pathogenic HMX1 variants.

---

# 3. Phenotypes

Because the number of reported patients is tiny and ascertainment is ophthalmology-driven, robust frequencies are unavailable. “Characteristic” below means repeatedly reported, not a validated percentage.

| Phenotype/type | Onset, course, severity and estimated frequency | Quality-of-life relevance | Suggested HPO term |
|---|---|---|---|
| Microphthalmia; physical sign | Congenital; usually bilateral but potentially asymmetric; variable severity; characteristic | Reduced visual potential, cosmetic and orbital-development effects | **HP:0000568** |
| Microcornea; physical sign | Congenital, generally stable; characteristic | Complicates surgery and refraction | **HP:0000482** |
| Ocular coloboma, including iris/optic-disc coloboma | Congenital, nonprogressive structural defect; characteristic but variable site | Can cause glare, field loss, poor acuity or retinal complications | **HP:0000589**; iris coloboma **HP:0000612** |
| Anterior-segment dysgenesis | Congenital; structurally stable but complications can emerge | Risk of corneal opacity, glaucoma and impaired vision | **HP:0007700** |
| Sclerocornea/corneal opacity | Congenital; variable | Severe deprivation amblyopia or visual obstruction | **HP:0000647** / **HP:0007957** |
| Cataract, often congenital or developmental | Congenital or childhood; may progress | Further reduces acuity; surgery can be difficult and retinal disease limits benefit | **HP:0000518**; developmental cataract **HP:0000519** |
| Microphakia | Congenital | Contributes to refractive and surgical complexity | **HP:0012376** |
| Synechiae | Congenital anterior-segment anomaly | Can contribute to glaucoma | **HP:0011482** or more specific anterior/posterior-synechia term |
| Increased intraocular pressure/glaucoma | Childhood or later; not universal; potentially progressive | Pain and additional irreversible optic-nerve injury | **HP:0007906** / **HP:0000501** |
| Rod-cone dystrophy | Early childhood; **progressive**, initially rod-predominant and later involving other photoreceptors | Night blindness, field constriction and progressive visual disability | **HP:0000510** |
| Pigmentary retinopathy/RPE abnormality | Early childhood onward; progressive with retinal dystrophy | Progressive loss of field and acuity | **HP:0000546** / **HP:0000532** |
| Macular hypoplasia | Congenital; stable developmental defect | Poor central acuity | **HP:0001104** |
| Nystagmus | Infancy/early childhood, secondary to poor vision | Impaired fixation and acuity | **HP:0000639** |
| Severe visual impairment | Congenital/early childhood and may worsen through retinal degeneration | Major impact on mobility, education, reading and independence | **HP:0012373** or **HP:0000505** |
| Dysplastic pinna/abnormal outer ear | Congenital, nonprogressive; defining feature | Primarily cosmetic; may affect device fitting | **HP:0000356** |
| Low-set or protruding ears; crumpled helix | Congenital, stable | Psychosocial/cosmetic effects | **HP:0000369**, **HP:0000411**, **HP:0000396** |
| Narrow intertragic notch/external acoustic meatus | Congenital, stable | Potential otologic surveillance implications | **HP:0000402** for stenosis of external auditory canal |
| Lobule aplasia or cleft earlobe | Congenital, stable; highly characteristic in the first family | Cosmetic/reconstructive implications | **HP:0009906** or abnormal ear-lobule morphology |
| Craniofacial asymmetry/short mandibular ramus | Reported in the third family; probably variable rather than core | Cosmetic and possible dental/occlusal effects | **HP:0000324**, **HP:0000278** |
| Developmental delay/abnormal gait | Reported in one 2026 patient, whereas earlier families had normal neurodevelopment; association remains uncertain | Potential educational and mobility effects | **HP:0001263**, **HP:0001288** |

The 2015 clinical study concluded that OAS has “a profound effect on the development of the external ear, anterior segment, and retina, leading to significant visual loss at an early age.” **PMID: 25574057**, 8 January 2015, [PubMed](https://pubmed.ncbi.nlm.nih.gov/25574057/).[2]

A 12-year longitudinal assessment specifically established that:

> “The retinal degeneration in the recessively inherited oculo-auricular syndrome is a progressive rod-cone dystrophy.”

—Vaclavik et al., *Ophthalmic Genetics*, June 2011; **PMID: 21417677**, [PubMed](https://pubmed.ncbi.nlm.nih.gov/21417677/).[4]

### Hearing

Despite conspicuous outer-ear malformation, **hearing was reported as normal in the foundational families**. Hearing loss should not be assumed to be a core feature; nevertheless, formal audiology is prudent because the auditory canal can be narrow and the evidence base is small.[26]

### Quality of life

No OAS-specific EQ-5D, SF-36, PROMIS, or vision-related quality-of-life cohort has been published. The dominant expected burden is childhood visual impairment and progressive retinal degeneration, affecting education, mobility, employment options, face recognition, and independence. Ear morphology principally contributes cosmetic and psychosocial burden unless canal stenosis produces functional impairment.

---

# 4. Genetic and molecular information

## 4.1 Causal gene and protein

| Attribute | Value |
|---|---|
| Gene | **HMX1**, H6 family homeobox 1; former symbol **NKX5-3** |
| HGNC | **HGNC:5017** |
| NCBI Gene | **3166** |
| OMIM gene | **142992** |
| UniProt | **Q9NP08** |
| Locus | **4p16.1** |
| Protein | Nuclear homeodomain transcription factor, approximately 347 amino acids |
| Disease relationship | Biallelic loss or severe functional disruption causes OAS |
| Inheritance | Autosomal recessive |

The identifier mapping is supported by NCBI, MGI, and GenCC.[120][126][40]

## 4.2 Published OAS-associated variants

Transcript numbering differs between publications; variants should be normalized to the laboratory’s current MANE transcript before clinical reporting.

| Variant reported | Type/function | Human evidence | Interpretation |
|---|---|---|---|
| **26-bp deletion, nucleotides 215–240; predicted truncation at approximately codon 112** | Frameshift/truncating; removes complete homeodomain | Homozygous in three affected members of a consanguineous Swiss family; heterozygous parents; absent from >250 matched controls and >500 individuals with other eye diseases | Pathogenic; germline loss of function.[50][62] |
| **NM_018942:c.650A>C, p.(Gln217Pro)** | Missense in first helix of the conserved homeodomain | Homozygous in two affected male cousins; in-vitro testing showed preserved expression but impaired function | Pathogenic/likely pathogenic; functional loss.[92] |
| **c.487G>T, p.(Glu163Ter), commonly written p.E163\*** | Nonsense/truncating | Homozygous proband; heterozygous parents | Pathogenic/likely pathogenic; expected loss of function; **PMID: 29140751**.[90] |
| Nonsense variant reported in two siblings in 2022 | Nonsense | Homozygous affected siblings; full HGVS was not recoverable from the PubMed record because no abstract is available | Pathogenic/likely pathogenic in the report; **PMID: 35946463**.[91][93] |
| **c.570_571del, p.(Glu191Argfs*34)** | Frameshift | Homozygous in a 6-year-old girl from a consanguineous Egyptian family | Likely pathogenic/pathogenic loss-of-function candidate; reported January 2026.[145] |
| **NM_018942.3:c.233_251dup, p.(Ala85Argfs*53)** | Frameshift | Homozygous in a 2026 case; segregation confirmed by Sanger sequencing | Likely pathogenic/pathogenic loss-of-function candidate; published 4 July 2026.[5] |

These are **germline**, not somatic, variants. Population frequencies are either absent or extremely low; the original deletion was absent from disease and ethnically matched controls. No recurrent common pathogenic allele, founder mutation, or reliable carrier frequency is known.

A heterozygous HMX1 **c.335G>T, p.(Gly112Val)** VUS was reported in a patient whose coloboma was attributed to another gene and who lacked typical OAS ear anomalies; this does **not** establish dominant HMX1 disease.[136]

## 4.3 Functional consequences

- Truncating alleles before or within the homeodomain are expected to abolish DNA binding, nuclear localization, dimerization, or all three.
- p.Gln217Pro changes a highly conserved homeodomain residue and impairs HMX1 function without necessarily reducing protein abundance.[92]
- HMX1 normally dimerizes through its SD1 and homeodomains, localizes to the nucleus, and represses **EPHA6/epha4b**, a retinal axon-guidance gene. **PMID: 24945320**, 19 June 2014, [PubMed](https://pubmed.ncbi.nlm.nih.gov/24945320/).[131]

## 4.4 Modifiers, epigenetics and chromosomal abnormalities

No confirmed modifier gene, disease-specific methylation signature, histone-mark abnormality, or somatic mosaic mechanism is known.

A distinct HMX1 regulatory mechanism should be kept separate from OAS: **duplications involving a long-range HMX1 enhancer** can cause isolated bilateral concha-type microtia, apparently through altered dosage or spatiotemporal expression rather than biallelic coding loss. This is relevant to testing unexplained isolated microtia but is not the canonical OAS genotype.[41]

No recurrent OAS-causing aneuploidy, translocation, or inversion has been established.

---

# 5. Environmental information

| Factor class | Current evidence |
|---|---|
| Toxins/radiation/pollution | No disease-specific causal association |
| Maternal smoking/alcohol/diet | No demonstrated OAS association |
| Occupational exposure | None established |
| Infectious agent | None; OAS is neither infectious nor postinfectious |
| Lifestyle factor | None known to alter occurrence or progression |
| Teratogens | Can mimic individual eye/ear malformations but do not explain biallelic HMX1-associated OAS |
| CHEBI annotations | No etiologic chemical entity is appropriate |

---

# 6. Mechanism and pathophysiology

## 6.1 Ordered causal chain

1. **Biallelic truncating or function-disrupting HMX1 variants lead to** absent or defective HMX1 homeodomain-transcription-factor activity.
2. **Defective homeodomain/SD1 function leads to** impaired nuclear localization, DNA binding and/or HMX1 dimerization; these effects are demonstrated for domain disruption and mechanistically supported for reported variants.[131]
3. **Loss of transcriptional control leads to** dysregulation of developmental targets, including insufficient repression of **EPHA6/epha4b** in the retina and altered regulation of **uhrf1** in zebrafish craniofacial tissues.[78][79]
4. **Retinal target dysregulation leads to** abnormal nasal–temporal retinal patterning, delayed retinal-progenitor cell-cycle exit and impaired differentiation; zebrafish evidence also shows increased apoptosis in eye and brain.[82]
5. **Abnormal progenitor differentiation and cell survival lead to** microphthalmia, retinal stratification defects, macular/optic-disc abnormalities and malformed anterior-segment structures. The precise route from HMX1 target dysregulation to each human malformation remains partly inferred.
6. **Persistent developmental and cellular defects lead to two retinal branches:**  
   6a. **Malformed anterior segment/lens leads to** microcornea, cataract, synechiae, sclerocornea and glaucoma risk.  
   6b. **Photoreceptor/retinal-network dysfunction leads to** early rod dysfunction followed by broader photoreceptor degeneration and progressive visual loss.
7. **HMX1 deficiency in second-branchial-arch and auricular mesenchyme leads to** abnormal external-ear cartilage morphogenesis, producing a crumpled or protruding pinna, narrow meatus/intertragic notch and lobule aplasia or clefting. The specific downstream effector program in human auricular mesenchyme is not yet fully demonstrated.
8. **Combined congenital ocular malformation and progressive retinal degeneration result in** infantile nystagmus, poor acuity, night blindness, restricted visual field and lifelong visual disability.

## 6.2 Molecular and cellular detail

HMX1 is expressed in the embryonic eye, neural retina, lens, branchial arches, otic region, trigeminal ganglion and dorsal-root ganglia. In human embryos, expression has been observed in the optic vesicle at approximately 5–6 weeks and in developing pinna/auricular mesenchyme later in gestation.[83][84]

Important experimentally supported functions include:

- **Retinal progenitor differentiation:** zebrafish knockdown delays withdrawal from the cell cycle and retards retinal differentiation.
- **Cell survival:** increased apoptosis occurs in the zebrafish eye and brain.
- **Retinal regionalization:** polarized nasal retinal expression suggests a role in nasal–temporal patterning.
- **Axon guidance:** HMX1 dimerization is required to inhibit EPHA6/epha4b expression.
- **Craniofacial transcriptional regulation:** zebrafish Hmx1 regulates **uhrf1**, although its relevance to every human OAS feature remains inferential.

The zebrafish retinogenesis abstract directly reports:

> “Knockdown of hmx1 led to microphthalmia. Delayed withdrawal of retinal progenitors from the cell cycle resulting in retarded retinal differentiation was observed in morphant. The retina and brain also showed an increased cell death at 24 hpf.”

—Boisset and Schorderet, 2012; **PMID: 23068565**, [PubMed](https://pubmed.ncbi.nlm.nih.gov/23068565/).[82]

### Suggested GO terms

- **GO:0006355** regulation of DNA-templated transcription
- **GO:0045944** positive regulation of transcription by RNA polymerase II, where experimentally appropriate
- **GO:0000122** negative regulation of transcription by RNA polymerase II
- **GO:0042461** photoreceptor cell development
- **GO:0060041** retina development in camera-type eye
- **GO:0001709** cell fate determination
- **GO:0045165** cell fate commitment
- **GO:0007049** cell cycle
- **GO:0006915** apoptotic process
- **GO:0007411** axon guidance
- **GO:0042471** ear morphogenesis
- **GO:0005634** nucleus
- **GO:0003677** DNA binding
- **GO:0003700** DNA-binding transcription-factor activity

### Suggested Cell Ontology terms

- **CL:0000740** retinal pigment epithelial cell
- **CL:0000210** photoreceptor cell
- **CL:0000604** retinal rod cell
- **CL:0000573** retinal cone cell
- **CL:0000748** retinal ganglion cell
- **CL:0002633** retinal progenitor cell, if supported by the ontology release used
- Lens epithelial cell
- Cranial neural-crest-derived mesenchymal cell
- Chondrocyte of auricular cartilage

## 6.3 Metabolism, immunity, tissue injury and omics

No characteristic systemic metabolic, lipidomic, metabolomic, inflammatory, autoimmune, or immunodeficiency mechanism is established. Tissue injury is principally developmental malformation followed by retinal neurodegeneration rather than inflammation, fibrosis, infection or ischemia.

No validated human OAS:

- blood biomarker,
- transcriptomic signature,
- proteomic profile,
- metabolomic/lipidomic signature,
- single-cell atlas,
- spatial-transcriptomic dataset,
- patient-iPSC model,
- organoid series, or
- multi-omics diagnostic classifier

has been reported. This is a major research gap.

---

# 7. Anatomical structures affected

| Level | Structures | Suggested ontology annotations |
|---|---|---|
| Primary organs | Eye and external ear/pinna | UBERON:0000970 eye; UBERON:0001690 ear |
| Ocular structures | Globe, cornea, iris, iridocorneal angle, lens, retina, retinal pigment epithelium, macula and optic disc | UBERON:0000964 cornea; UBERON:0001769 iris; UBERON:0000965 lens; UBERON:0000966 retina; UBERON:0001782 retinal pigment epithelium |
| Auricular structures | Helix, antihelix, crus, tragus/intertragic notch, lobule, external acoustic meatus and auricular cartilage | UBERON external ear/pinna and external acoustic meatus terms |
| Secondary structures | Optic nerve in optic-disc coloboma or glaucoma; orbit in marked microphthalmia | UBERON:0000962 optic nerve; UBERON:0001697 orbit |
| Craniofacial, variable | Mandibular ramus and facial skeleton | UBERON:0001684 mandible |
| Tissue types | Neuroretina, RPE, lens epithelium, corneal/anterior-segment mesenchyme, neural-crest-derived auricular mesenchyme and cartilage | CL terms listed above; chondrocyte **CL:0000138** |
| Subcellular | Nucleus, chromatin and transcriptional-regulatory complexes | GO:0005634 nucleus; GO:0000785 chromatin |

The phenotype is usually **bilateral**, although severity can be asymmetric. Ear and eye findings may not be identical from side to side.

---

# 8. Temporal development

- **Initiation:** embryonic, during eye and branchial-arch morphogenesis.
- **Clinical onset:** congenital for structural eye and ear abnormalities.
- **Early childhood:** poor vision and nystagmus become evident; retinal electrophysiology may reveal rod-cone dysfunction.
- **Later childhood and adulthood:** retinal dystrophy progresses; cataract and glaucoma may add further impairment.
- **Course:** structural malformations are stable, while retinal degeneration is chronic and progressive.
- **Duration:** lifelong.
- **Remission:** no spontaneous remission is expected.
- **Critical periods:** prenatal organogenesis for disease causation; infancy and early childhood for cataract assessment, amblyopia management, glaucoma detection, visual habilitation and educational support.

There is no validated disease-stage classification. A practical clinical framework is: congenital structural phase, early visual-development phase, progressive retinal-dystrophy phase, and advanced visual-disability phase.

---

# 9. Inheritance and population

## 9.1 Epidemiology

No population prevalence or annual incidence has been measured. The condition is **ultra-rare**. As of early 2026, one review/case series described only five documented families; the later 2026 case report likely raises the published number to approximately six.[66][5]

Thus:

- Prevalence per 100,000: **unknown**
- Incidence per 100,000 births: **unknown**
- Carrier frequency: **unknown**
- Population-screening frequency: **not established**
- Sex ratio: **not estimable**
- Geographic/ethnic predilection: **none established**

Reported families include European, Asian/Pakistani and Egyptian or other Middle Eastern/North African ancestry, but this pattern likely reflects consanguinity and case ascertainment rather than ethnic specificity.

## 9.2 Genetic behavior

| Feature | Assessment |
|---|---|
| Inheritance | Autosomal recessive |
| Penetrance | Appears high for the eye-plus-ear phenotype in reported biallelic cases, but cannot be precisely estimated |
| Expressivity | Variable, especially the exact ocular structures involved and severity of retinal disease |
| Anticipation | Not reported; no repeat expansion mechanism |
| Germline mosaicism | Not demonstrated; low residual recurrence risk should still be discussed after an apparently de novo event |
| Founder effect | None established |
| Consanguinity | Present in several pedigrees and materially increases homozygosity risk |
| Sex bias | None established |
| Heterozygote phenotype | Generally unaffected; isolated heterozygous VUS findings are insufficient to establish dominant disease |

---

# 10. Diagnostics

## 10.1 Clinical evaluation

Diagnosis should be suspected when **characteristic external-ear malformation occurs with congenital ocular anomalies**, especially microphthalmia/microcornea, cataract, coloboma and early retinal dystrophy.

Recommended baseline assessment:

1. Complete dysmorphology and three-generation family history, including consanguinity.
2. Slit-lamp examination, cycloplegic refraction and measurement of corneal diameter/axial length.
3. Dilated fundus examination and wide-field retinal photography.
4. Optical coherence tomography where feasible.
5. Full-field electroretinography to document rod-cone dysfunction.
6. Intraocular-pressure measurement, gonioscopy where anatomically possible, and optic-nerve monitoring.
7. B-scan ocular ultrasonography if media opacity prevents fundus examination.
8. Audiology and otoscopic examination, despite normal hearing in early reports.
9. Developmental assessment if delay, gait abnormality or neurologic signs are present.

No blood chemistry, enzyme assay, biopsy or histopathologic test is diagnostic.

## 10.2 Genetic testing algorithm

1. **First-line:** a congenital eye-malformation, microphthalmia/coloboma, cataract, or inherited-retinal-disease panel that includes **HMX1**, with deletion/duplication calling.
2. **If the phenotype is highly characteristic:** sequence HMX1 with copy-number analysis; Sanger sequencing remains suitable for familial variant confirmation.
3. **If panel testing is negative:** trio **WES** or preferably **WGS**, because the differential is broad and WGS can detect coding, splice, copy-number and regulatory variants.
4. **CMA:** useful when developmental delay, multiple congenital abnormalities or a possible chromosomal syndrome accompanies the ocular phenotype; it is not the optimal standalone test for small HMX1 sequence variants.
5. **Karyotype/FISH:** only when a visible chromosomal rearrangement is suspected.
6. **RNA sequencing:** potentially useful for a suspected splice variant, but not a validated routine OAS assay.
7. **Not indicated routinely:** mitochondrial sequencing, repeat-expansion testing, liquid biopsy, proteomics or metabolomics.

NCBI GTR currently lists multiple tests in which HMX1 is included.[36]

## 10.3 Variant interpretation

Use ACMG/AMP criteria with attention to:

- **PVS1** for appropriate null alleles in a gene where loss of function is established;
- **PM2** for absence/extreme rarity in population databases;
- **PM3** for occurrence in trans with another pathogenic allele;
- **PP1** for cosegregation;
- **PP4** for the highly specific eye-plus-external-ear phenotype;
- **PS3** only where a validated functional assay demonstrates damaging effect.

## 10.4 Differential diagnosis

| Disorder | Distinguishing considerations |
|---|---|
| Oculo-auriculo-vertebral spectrum/Goldenhar syndrome | Facial microsomia, mandibular hypoplasia, epibulbar dermoids, vertebral anomalies; usually not progressive rod-cone dystrophy or biallelic HMX1 disease |
| Branchio-oto-renal syndrome | Branchial pits/fistulae, hearing loss and renal anomalies; EYA1/SIX1/SIX5 |
| CHARGE syndrome | Coloboma plus choanal atresia, heart defects, genital anomalies, characteristic ears and frequent hearing loss; CHD7 |
| Cat-eye syndrome | Coloboma, anal anomalies, preauricular tags/pits and supernumerary marker chromosome 22 |
| Lenz microphthalmia | X-linked microphthalmia with skeletal, dental, genital or developmental abnormalities |
| SOX2/OTX2/PAX6-related eye malformation | Often dominant/de novo; CNS, endocrine or aniridia-related findings; characteristic OAS ear-lobule anomaly generally absent |
| STRA6-related Matthew-Wood syndrome | Anophthalmia/microphthalmia with pulmonary, cardiac and diaphragmatic anomalies |
| Retinoic-acid embryopathy | Exposure history and broader teratogenic pattern; no biallelic HMX1 variant |
| Isolated congenital cataract or retinal dystrophy | Does not explain the characteristic external-ear phenotype |

There are no universally adopted formal diagnostic criteria. Molecular confirmation is strongly preferred.

## 10.5 Screening

OAS is not included in population newborn biochemical screening. Appropriate targeted approaches are:

- ophthalmic examination of newborns with microphthalmia, cataract or dysplastic ears;
- cascade testing of adult relatives after the familial variant is identified;
- carrier testing for reproductive partners in known families;
- prenatal or preimplantation testing when both familial pathogenic alleles are known.

---

# 11. Outcomes and prognosis

## 11.1 Survival

No disease-specific reduction in life expectancy or increased mortality has been demonstrated. Five- or ten-year survival statistics are unavailable. OAS is not known to cause cardiac, respiratory, renal, immune or metabolic failure.

## 11.2 Visual prognosis and morbidity

Visual prognosis is often guarded because multiple mechanisms coexist:

- congenital globe and anterior-segment malformation,
- cataract and deprivation amblyopia,
- optic-disc or retinal coloboma,
- macular hypoplasia,
- glaucoma, and
- progressive rod-cone degeneration.

Cataract surgery can improve media clarity but cannot reverse retinal dystrophy, macular hypoplasia, coloboma or severe microphthalmia. The University of Arizona resource accordingly cautions that permanent visual rehabilitation may remain limited because retinal dystrophy is progressive.[16]

## 11.3 Prognostic factors

Likely adverse factors include:

- severe microphthalmia;
- bilateral dense congenital cataract;
- central retinal or optic-disc coloboma;
- macular hypoplasia;
- markedly reduced early ERG responses;
- glaucoma or corneal opacity;
- delayed access to amblyopia treatment and low-vision services.

No validated molecular prognostic biomarker or genotype–phenotype model exists.

---

# 12. Treatment

There is no approved disease-modifying, gene, RNA or cell therapy for HMX1-related OAS. Treatment is individualized and multidisciplinary.

| Intervention | Indication and considerations | Evidence/outcome | Suggested NCIT concept |
|---|---|---|---|
| Cataract extraction, with or without intraocular lens | Visually significant cataract; timing balances amblyopia prevention against small-eye/anterior-segment surgical risk | May clear the visual axis; final acuity limited by retinal and structural disease | Cataract Surgery |
| Glaucoma medication | Elevated intraocular pressure | Standard topical treatment selected by pediatric/glaucoma specialist; no OAS-specific response data | Pharmacologic Therapy; Antiglaucoma Agent |
| Glaucoma surgery | Pressure uncontrolled medically | Technique individualized to abnormal anatomy | Glaucoma Surgery |
| Optical correction | Refractive error or aphakia | Essential for maximizing residual vision | Corrective Lens Therapy |
| Occlusion/amblyopia therapy | Asymmetric visual input during childhood | Most useful during the visual-development window | Amblyopia Therapy |
| Low-vision rehabilitation | Progressive or severe visual impairment | Magnification, contrast enhancement, mobility training and assistive technology | Low Vision Rehabilitation |
| Orientation and mobility training | Field loss/night blindness | Improves safety and independence | Rehabilitation Therapy |
| Educational accommodations | Childhood visual disability | Braille or large print, accessible devices and individualized education | Supportive Care |
| Hearing surveillance | Narrow canal or clinical concern | Hearing often normal, but evidence is limited | Audiologic Examination |
| Auricular reconstruction/otoplasty | Functional or cosmetic concerns | Elective; timing determined by reconstructive team | Reconstructive Surgery |
| Genetic counseling | Patient and family | Recurrence-risk clarification and reproductive planning | Genetic Counseling |

No OAS-specific drug, pharmacogenomic recommendation, immunotherapy, targeted small molecule, ASO, CRISPR product or registered interventional trial with an established efficacy signal was identified.

Potential future approaches include HMX1 gene replacement or cell-targeted developmental-pathway manipulation, but prenatal developmental malformations would be difficult to reverse after birth. Retinal rescue could theoretically remain relevant if ongoing degeneration depends on persistent HMX1 deficiency; this has not yet been demonstrated.

---

# 13. Prevention

## Primary prevention

No vaccine, diet, supplement, or lifestyle intervention prevents genetically determined OAS. In known families, reproductive options include:

- preconception carrier testing;
- testing the reproductive partner;
- preimplantation genetic testing for monogenic disease;
- chorionic-villus sampling or amniocentesis for the familial variants;
- donor gametes or other reproductive alternatives.

## Secondary prevention

- Early recognition of congenital cataract and glaucoma;
- early genetic testing of infants with the characteristic phenotype;
- cascade testing of siblings and relatives;
- prompt visual assessment and amblyopia prevention.

## Tertiary prevention

- Lifelong glaucoma monitoring;
- retinal surveillance;
- low-vision and orientation/mobility rehabilitation;
- educational and occupational accommodation;
- eye protection and prompt management of painful pressure elevation;
- psychosocial and reconstructive support for ear malformation.

Population-wide carrier or newborn genetic screening is not justified by current prevalence and evidence. There is no relevant immunization or antimicrobial prophylaxis.

---

# 14. Other species and naturally occurring disease

| Species | Taxon | Gene/model | Findings and relevance |
|---|---|---|---|
| Human | **NCBI Taxon 9606** | HMX1, NCBI Gene 3166 | Natural OAS from biallelic germline variants |
| Mouse, *Mus musculus* | **Taxon 10090** | *Hmx1*, MGI:107178 | Naturally arising/spontaneous or ENU alleles produce laterally protruding/low-set ears, reduced body mass, microphthalmia, cranial abnormalities and variably perinatal semilethality; two OAS models are curated by MGI.[23] |
| Zebrafish, *Danio rerio* | **Taxon 7955** | *hmx1* | Knockdown/mutant models show microphthalmia, delayed retinal differentiation, increased apoptosis and other developmental effects; useful for live embryology and retinal patterning.[82][85] |
| Domestic breeds/wildlife | — | — | No well-established naturally occurring veterinary syndrome directly equivalent to human HMX1-OAS was identified |

There is no zoonotic transmission, pathogen reservoir, or cross-species contagious susceptibility.

---

# 15. Model organisms

## 15.1 Mouse

Two curated mouse OAS models are:

- **Hmx1^mpe/Hmx1^mpe**
- **Hmx1^dmbo/Hmx1^dmbo**

MGI reports low-set/laterally protruding ears, reduced body mass, microphthalmia, mild cranial defects, and, in some backgrounds, perinatal semilethality or exencephaly.[23][44]

**Strengths**

- Mammalian auricular and craniofacial anatomy;
- endogenous Hmx1 developmental expression;
- recapitulation of external-ear and small-eye phenotypes;
- study of neural-crest and sensory-neuron development.

**Limitations**

- Human retinal dystrophy, cataract and complex anterior-segment dysgenesis are incompletely reproduced;
- background-dependent lethality and exencephaly are not typical human OAS manifestations;
- murine ocular phenotypes may be substantially milder or anatomically different. The mouse literature notes that human defects are extensive whereas mouse ocular defects can be largely restricted to microphthalmia.[130]

## 15.2 Zebrafish

Zebrafish models include morpholino knockdown, mutant lines and transgenic overexpression systems.

**Recapitulated features**

- microphthalmia;
- delayed/absent retinal stratification;
- delayed retinal-progenitor cell-cycle exit;
- increased retinal apoptosis;
- abnormal retinogenesis and regional patterning.

The original study reported microphthalmia in all injected embryos, with delayed retinal stratification in 73% and absent stratification in 27%, although morpholino-specific artifacts and dose effects must be considered.[84]

**Applications**

- live imaging of eye development;
- testing HMX1 dimerization and nuclear localization;
- analysis of EPHA6/epha4b regulation;
- developmental transcriptomics;
- rapid in-vivo testing of candidate variants;
- small-molecule modifier screens.

**Limitations**

- external-ear anatomy is not directly homologous to the human pinna;
- morpholino phenotypes require genetic validation;
- larval findings do not fully model decades-long human retinal degeneration.

## 15.3 In-vitro systems

Promoter assays and transfected-cell experiments have shown that HMX1 dimerizes, requires the SD1/homeodomain for dimerization, and represses EPHA6. These systems establish molecular function but do not reproduce tissue morphogenesis.[78]

No well-characterized patient-derived iPSC, retinal organoid, auricular-cartilage organoid, or CRISPR-corrected isogenic OAS model has yet become a standard resource.

---

# Recent developments and research priorities

## Important recent findings

1. **2022:** a fourth family with two affected siblings and a new homozygous nonsense HMX1 variant was reported; **PMID: 35946463**, publication 10 August/October 2022.[135]
2. **2023–2024:** no major OAS-specific clinical trial, natural-history cohort or disease-modifying study was identified. Research during this interval remained dominated by broader eye/ear developmental genetics rather than OAS-specific patient studies.
3. **January 2026:** an Egyptian cohort identified homozygous **c.570_571del, p.(Glu191Argfs*34)** in a child described as the fifth family; developmental delay and abnormal gait broadened the possible phenotype, although causality for those neurologic features remains uncertain.[145]
4. **July 2026:** another case report identified **c.233_251dup, p.(Ala85Argfs*53)**, further supporting loss of function as the main mechanism.[5]
5. HMX1 enhancer research has established that noncoding dosage changes can cause isolated bilateral microtia, emphasizing that coding loss and enhancer gain/dysregulation can generate different phenotypes.[41]

## Highest-priority knowledge gaps

- International registry and standardized natural-history data;
- patient-level phenotype tables with visual acuity, ERG and retinal-imaging trajectories;
- complete, transcript-normalized allelic catalog with ClinVar expert curation;
- penetrance and genotype–phenotype analysis;
- patient-derived retinal and auricular organoids;
- single-cell and spatial profiling of HMX1-expressing embryonic tissues;
- identification of direct transcriptional targets beyond EPHA6 and UHRF1;
- testing whether postnatal HMX1 restoration can slow retinal degeneration;
- validated patient-reported visual-function and quality-of-life measures.

## Overall evidence assessment

The **HMX1–OAS gene–disease relationship is strong**, supported by segregation in multiple independent consanguineous families, consistent biallelic variants, functional impairment, developmental expression, and concordant mouse and zebrafish phenotypes. Nevertheless, estimates of phenotype frequency, penetrance, prognosis and treatment outcome remain **low-certainty** because the clinical literature consists almost entirely of isolated families and case reports rather than cohorts.

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 19 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 19 |
| On topic | 6 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMC:PMC5123892` (1 mention) - Genetic Advances in the Understanding of Microtia.
  - shared terms: genetic, ear

Weighed against this report's own most characteristic terms: `retinal`, `hmx1`, `oas`, `phenotype`, `variant`, `microphthalmia`, `cataract`, `disease`, `developmental`, `gene`, `eye`, `malformation`, `established`, `loss`, `congenital`, `biallelic`, `genetic`, `ear`, `coloboma`, `visual`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 67 |
| Resolved | 64 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 9 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 9 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `DOID:0060482` (1 mention) - the report calls it "Disease Ontology"; DOID calls it **oculoauricular syndrome**
- `HP:0000568` (1 mention) - the report calls it "Reduced visual potential, cosmetic and orbital-development effects"; HP calls it **Microphthalmia**
- `HP:0000482` (1 mention) - the report calls it "Complicates surgery and refraction"; HP calls it **Microcornea**
- `HP:0007700` (1 mention) - the report calls it "Risk of corneal opacity, glaucoma and impaired vision"; HP calls it **Ocular anterior segment dysgenesis**
- `HP:0012376` (1 mention) - the report calls it "Contributes to refractive and surgical complexity"; HP calls it **Microphakia**
- `HP:0000510` (1 mention) - the report calls it "Night blindness, field constriction and progressive visual disability"; HP calls it **Rod-cone dystrophy**
- `HP:0001104` (1 mention) - the report calls it "Poor central acuity"; HP calls it **Macular hypoplasia**
- `HP:0000639` (1 mention) - the report calls it "Impaired fixation and acuity"; HP calls it **Nystagmus**
- `HP:0000356` (1 mention) - the report calls it "Primarily cosmetic; may affect device fitting"; HP calls it **Abnormality of the outer ear**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `MGI`.