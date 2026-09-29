---
provider: perplexity
model: sonar-pro
cached: false
start_time: '2026-09-09T19:59:22.434823'
end_time: '2026-09-09T20:01:17.550056'
duration_seconds: 115.12
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: 3p- Syndrome
  mondo_id: MONDO:0013424
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 41
reference_validation:
  total_references: 19
  verified: 19
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 19
  on_topic: 15
  validator_version: 0.2.1
term_validation:
  total_terms: 59
  verified: 57
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 55
  labels_matching: 33
  labels_mismatched: 8
  mislabelled_terms:
  - term_id: HP:0001305
    reported_labels:
    - psychomotor delay
    ontology_label: Dandy-Walker malformation
  - term_id: HP:0000263
    reported_labels:
    - "Trigonocephaly / brachy\u2011trigonocephaly"
    ontology_label: Oxycephaly
  - term_id: HP:0000107
    reported_labels:
    - Renal anomalies / polycystic renal dysplasia
    ontology_label: Renal cyst
  - term_id: CL:0000127
    reported_labels:
    - neuron
    ontology_label: astrocyte
  - term_id: CL:0000182
    reported_labels:
    - cardiac muscle cell
    ontology_label: hepatocyte
  - term_id: UBERON:0008897
    reported_labels:
    - skull
    ontology_label: fin
  - term_id: UBERON:0001444
    reported_labels:
    - hand
    ontology_label: subdivision of head
  - term_id: UBERON:0002429
    reported_labels:
    - vertebral column
    ontology_label: cervical lymph node
  labels_variant: 14
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** 3p- Syndrome
- **MONDO ID:** MONDO:0013424 (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **3p- Syndrome** covering all of the
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

3p- syndrome (chromosome 3pter–p25 deletion; **MONDO:0013424**) is a rare contiguous gene deletion disorder caused by partial monosomy of the distal short arm of chromosome 3 (3p25–pter), characterized by pre‑ and post‑natal growth retardation, severe intellectual disability, developmental delay, craniofacial dysmorphism, hypotonia, and variable congenital malformations, particularly congenital heart defects, renal and gastrointestinal anomalies, and limb anomalies.[1][2][4][5][9][16][18][23][32][34][41][42][43][44]

Below is a structured research report, organized according to your template. Where possible, I highlight recent sources (2020–2025), but much of the core knowledge comes from earlier “landmark” cytogenetic and microarray studies.

---

## 1. Disease Information

### Definition and overview

“Distal monosomy 3p” or **3p deletion syndrome / 3p‑ syndrome** is a chromosomal anomaly caused by deletion of a variable segment at the terminal portion of 3p, typically spanning **3p25–pter**.[1][2][5][32][34][38][41]  

- Orphanet defines distal monosomy 3p as “a rare chromosomal anomaly syndrome, resulting from a partial deletion of the short arm of chromosome 3, with a highly variable phenotype typically characterized by pre‑ and post‑natal growth retardation, intellectual disability, developmental delay and craniofacial dysmorphism (microcephaly, trigonocephaly, downslanting palpebral fissures, telecanthus, ptosis, micrognathia).”[2]  
- MedlinePlus describes it as a condition “that results from a chromosomal change in which a small piece of chromosome 3 is deleted in each cell… at the end of the short (p) arm,” leading to intellectual disability, developmental delay, and abnormal physical features.[6][18][21]

The disorder is rare, with fewer than ~60 well‑documented distal 3p deletions reported worldwide in recent reviews and case compilations.[4][11][17][31][37][42]

### Key identifiers and classification

- **OMIM:** #613792 – “CHROMOSOME 3pter‑p25 DELETION” (distal 3p‑ syndrome).[1][23][44]  
- **Orphanet:** Distal deletion 3p syndrome (ORPHA:1620, also catalogued as partial deletion of short arm of chromosome 3, ORPHA:261875).[2][10]  
- **MONDO:** MONDO:0013424 – 3p‑ syndrome (ClinVar entry cross‑references MONDO:0013424).[3]  
- **MedGen:** C4706503 – 3p‑ syndrome.[3][7]  
- **MeSH / ICD‑10/ICD‑11:** No specific MeSH term; usually coded under “Other specified chromosome abnormalities” (e.g., ICD‑10 Q92.8, Q93.* for deletions of autosomes). This is typically inferred from chromosomal deletion coding practices, not from a dedicated 3p‑ code.  
- **Category:** Genetic / chromosomal, autosomal dominant (contiguous gene syndrome).[1][23][44]

### Synonyms and alternative names

Common synonyms:[1][2][5][8][10][14][34][38][41][44]

- **3p‑ syndrome** (three‑p minus syndrome)  
- **3p deletion syndrome**  
- **Distal monosomy 3p**  
- **Chromosome 3pter‑p25 deletion syndrome**  
- **Partial deletion of the short arm of chromosome 3 syndrome**  
- **Deletion 3p syndrome**  
- Sometimes specified by band: **3p25 deletion**, **3p26.3 deletion**, etc.

### Data type

Most information derives from **aggregated disease‑level resources** (OMIM, Orphanet, MedGen, MedlinePlus, RareChromosome support documents) summarizing multiple case reports and small series, supported by individual patient reports and microarray‑based cytogenetic studies.[1][2][5][7][16][18][23][31][32][34][37][38][41][42][43][44]  

---

## 2. Etiology

### Primary causal factor

3p‑ syndrome is caused by **heterozygous deletion** (partial monosomy) of distal **chromosome 3p** (typically 3p25–pter; deletion sizes ~200 kb to >10 Mb).[5][32][34][37][38][41][43]  

- Phipps et al. (Am J Hum Genet 2004, often cited in OMIM/Orphanet) and subsequent microarray studies show deletions from **3p25.3–p26.3 to 3pter**, with variable breakpoints and sizes, defining a contiguous gene syndrome.[27][32][34][43][45]  
- A genotype–phenotype review notes that “3p‑ syndrome is a rare contiguous gene syndrome which is caused by 200 kb to 12.5 Mb deletions in 3pter‑p25 region with a wide clinical spectrum.”[41]  

Most deletions are **de novo**, but familial cases with inherited terminal deletions or interstitial deletions have been reported, sometimes with variable expressivity or non‑penetrance.[5][37][38][40][41][43]

### Genetic risk factors

#### Causal loci and candidate genes

Multiple genes in distal 3p likely contribute to the phenotype; high‑impact candidates include:[5][9][20][31][32][34][37][43][45]

- **SRGAP3** (SLIT‑ROBO Rho GTPase‑activating protein 3):  
  “We suggest that current evidence suggests that SRGAP3 is the major determinant of mental retardation in distal 3p deletions.”[32] (microarray‑based analysis of 3p25‑p26 deletions)  
- **CHL1** (close homolog of L1): implicated in neurodevelopment; terminal 3p26.3 deletions containing only CHL1 were associated with developmental delay and mental retardation in some familial cases.[5][34]  
- **CNTN4, CNTN6** (contactins): involved in neuronal connectivity; recurrently deleted in distal 3p deletions and associated with neurodevelopmental phenotypes.[9][31]  
- **CRBN** (cereblon): suggested to contribute to cognitive impairment and developmental delay.[5][9]  
- **OXTR** (oxytocin receptor), **CAV3**, **SRGAP3**: discussed as genes affecting autistic behavior, congenital heart defect, and mental retardation in a patient with interstitial 3p25.3–p26.1 deletion.[20]  

Karyotype–phenotype studies identified **band 3p25.3** as critical for the classic 3p‑ phenotype:[43]

> “Karyotype‑phenotype comparisons… suggest that deficiency of the 3p25.3 band is critical to produce the main clinical manifestations of the del(3p) syndrome.”[43]

#### Variant classification and type

- The pathogenic lesion is usually a **constitutional (germline) structural variant**: terminal (or occasionally interstitial) **deletion** of 3p.[34][37][38][40][41][45]  
- Classified as **pathogenic** structural variants in ClinVar and OMIM, based on segregation, de novo occurrence, and concordant phenotype.[3][28][31][34]  
- Variants are **copy‑number losses** (CNVs), not point mutations; types include terminal deletions, interstitial deletions, sometimes combined with inverted duplications of proximal 3p.[29][34][41]

Allele frequencies in population databases (gnomAD, ExAC) are extremely low or absent, consistent with a rare, often severe developmental disorder; this is inferred from general CNV intolerance and not directly quantified for this specific syndrome.

### Environmental risk factors

No specific environmental, lifestyle, or toxic exposures have been shown to *cause* 3p‑ syndrome; the deletion is typically a **sporadic chromosomal event** during gametogenesis or early embryogenesis.[5][34][37][38][40][41]  
Standard obstetric risk factors (advanced maternal age) may modestly increase risk of chromosomal anomalies in general, but specific data for distal 3p deletions are lacking.

### Protective factors and gene–environment interactions

- Familial reports with **terminal 3p26.3 deletions and normal phenotype** indicate that small deletions restricted to **CHL1** (or to very distal 3p) may lack penetrance or cause only subtle deficits.[5][34][37][40]  
  > “A terminal 3p26.3 deletion is not associated with dysmorphic features and intellectual disability in a four‑generation family.”[40]  
- Other studies describe **chromosomal non‑penetrance** or modifier genes in terminal 3p deletions.[37]  

No robust gene–environment interaction data (e.g., exposure modifying severity) have been reported. Protective “modifier” alleles are speculative.

---

## 3. Phenotypes

### Core clinical phenotype

OMIM and MedGen summarize the **characteristic features** of distal 3p‑ syndrome:[7][23][44]

> “Characteristic features of the distal 3p‑ syndrome include low birth weight, microcephaly, trigonocephaly, hypotonia, psychomotor and growth retardation, ptosis, telecanthus, downslanting palpebral fissures, and micrognathia. Postaxial polydactyly, renal anomalies, cleft palate, congenital heart defects (especially atrioventricular septal defects), preauricular pits, sacral dimple, and gastrointestinal anomalies are variable features.”[23][44]

MedlinePlus similarly lists:[18][21]

> “slow growth, an abnormally small head (microcephaly), a small jaw (micrognathia), droopy eyelids (ptosis), malformed ears or nose, and widely spaced eyes (hypertelorism)… extra fingers or toes (polydactyly)… cleft palate… seizures, weak muscle tone (hypotonia), intestinal abnormalities, or congenital heart defects.”  

The 2021 case report and literature review provides an updated aggregated phenotype list:[16][31]

> “After more than 40 years of studies, the main clinical phenotypes… have been identified as follows: delayed growth and development, intellectual disability, hypotonia, micrognathia, ptosis, wide nose bridge, long philtrum, low ear position, deformed ears, polydactyly deformity, hearing abnormalities, CHD, renal abnormalities, syndactylism, gastrointestinal abnormalities, and scoliosis.”[31]

### Quantitative frequencies (Phipps et al., 2004 cohort)

A key quantitative summary (Am J Hum Genet, ~2004), often reproduced in reviews, reports phenotype frequencies across compiled cases:[27]

> Developmental delay 86%; postnatal growth retardation 86%; ptosis 77%; low birth weight 73%; malformed ears 68%; long philtrum 68%; broad nasal bridge 64%; hypotonia 50%; microcephaly 50%; micrognathia 50%; epicanthal folds 41%; postaxial polydactyly 40%; hypertelorism 36%; feeding problems 29%; clinodactyly 27%; trigonocephaly 23%; downturned corners of mouth 24%; synophrys 18%; low frontal hairline 14.[27]

These are **aggregated disease‑level frequencies** derived from case series.

### Age of onset, severity, progression

- **Onset:** Congenital – most features (growth restriction, craniofacial dysmorphism, cardiac defects) are present prenatally or at birth.[2][16][18][23][34][35][38][41][42]  
  Prenatal intrauterine growth restriction and cardiac defects have been described.[29]  
- **Severity:** Intellectual disability typically **severe to profound**; language remains severely limited.[18][21]  
  > “Individuals with 3p deletion syndrome typically have severe to profound intellectual disability… language ability usually remains limited.”[21]  
- **Progression:** Developmental delay is persistent; growth retardation continues postnatally.[2][16][18][21][23][31][34][41]  
  Neurological manifestations (hypotonia, seizures) may stabilize but cognitive deficits usually remain lifelong. Severity is **highly variable**, ranging from normal phenotype to severe multi‑system involvement.[5][34][37][38][40]

### Representative phenotype categories and suggested HPO terms

Below is a structured mapping (non‑exhaustive):

1. **Growth and development**  
   - Pre‑ and post‑natal growth retardation (HPO: HP:0001511 – growth delay; HP:0008897 – intrauterine growth restriction).[2][23][27][31][34][41]  
   - Psychomotor retardation / developmental delay (HP:0001263 – developmental delay; HP:0001305 – psychomotor delay).[2][7][16][18][23][27][31][34]  
   - Severe intellectual disability (HP:0002342).[16][18][21][23][31][34]  

2. **Craniofacial dysmorphism**  
   - Microcephaly (HP:0000252).[2][18][21][23][27][31][34][35][39][41][42]  
   - Trigonocephaly / brachy‑trigonocephaly (HP:0000263).[23][27][30][36][39]  
   - Telecanthus (HP:0000506).[2][23][36][41][42][44]  
   - Hypertelorism (HP:0000316).[18][21][23][27][35]  
   - Ptosis (HP:0000508).[2][7][18][21][23][27][31][34][35][39]  
   - Downslanting palpebral fissures (HP:0000494).[23][41][44]  
   - Epicanthal folds (HP:0000286).[18][21][27][39]  
   - Long philtrum (HP:0000343).[27][31][35][36][41][43]  
   - Broad nasal bridge (HP:0000431).[27][31][35][39]  
   - Micrognathia (HP:0000347).[2][18][21][23][27][31][35][39][41][42][44]  
   - Low set/malformed ears (HP:0000369, HP:0000377).[16][18][21][23][27][31][35][41][43]  

3. **Limb and skeletal anomalies**  
   - Postaxial polydactyly (HP:0001162).[23][27][31][39][44]  
   - Clinodactyly (HP:0030084).[27]  
   - Syndactyly (HP:0001159).[31]  
   - Scoliosis (HP:0002650).[31]  
   - Feeding difficulties (HP:0011968).[27][31]  

4. **Neurological and behavioral**  
   - Hypotonia (HP:0001290).[2][16][18][21][23][27][31][35][36][41][42][44]  
   - Seizures (HP:0001250).[18][21][31]  
   - Autism spectrum disorder features (HP:0000729 – autistic behavior).[18][20][21][26]  
   - Obsessive–compulsive disorder behaviors (HP:0000722 – obsessive‑compulsive behavior).[18][21]  
   - Hearing abnormalities / deafness (HP:0000365).[31][43]  

5. **Cardiac, renal, GI and other system involvement**  
   - Congenital heart defects, especially **atrioventricular septal defects** (HP:0001671 – atrioventricular septal defect).[23][31][41][42][45]  
     > “Congenital heart defects (especially atrioventricular septal defects)” are noted as variable features.[23][44]  
     First report of hypoplastic left heart syndrome in 3p‑ syndrome has been described.[4][11][42]  
   - Renal anomalies / polycystic renal dysplasia (HP:0000107).[9][23][31][42][44]  
   - Gastrointestinal abnormalities (e.g., hiatal hernia, intestinal malformations, umbilical hernia)[9][23][29][31][44]  
   - Cleft palate (HP:0000175).[18][21][23][44]  
   - Preauricular pits (HP:0004467).[23][44]  
   - Sacral dimple (HP:0000960).[23][44]  

### Quality‑of‑life impact

Severe intellectual disability, persistent developmental delay, hypotonia, and multi‑system malformations substantially impair **daily functioning, autonomy, and communication**.[16][18][21][31]  

MedlinePlus states that language ability “usually remains limited,” and affected individuals often have significant motor delays, seizures, and behavioral issues, affecting quality of life and caregiver burden.[18][21] No formal EQ‑5D or SF‑36 studies specific to 3p‑ syndrome were identified; extrapolation from severe developmental disorders suggests marked impairment across mobility, self‑care, usual activities, and cognition.

---

## 4. Genetic/Molecular Information

### Causal genes and candidate “critical regions”

Multiple studies attempt to define “critical regions” and genes within 3p25–pter responsible for specific aspects of the phenotype:[5][9][20][31][32][34][37][38][43][45]

- **SRGAP3** (3p25.3):  
  Microarray‑based analysis of multiple 3p25‑p26 deletions concluded:  
  > “We suggest that current evidence suggests that SRGAP3 is the major determinant of mental retardation in distal 3p deletions.”[32]  
- **CHL1 (3p26.3)**:  
  Terminal 3p26.3 deletions containing only CHL1 caused developmental delay and mental retardation in some families, implicating CHL1 in cognitive development, though non‑penetrant cases exist.[5][34][40]  
- **CNTN4 / CNTN6**:  
  These contactin genes are repeatedly deleted in patients with 3p deletion syndrome and are catalogued as associated with developmental delay, intellectual disability, microcephaly, and dysmorphisms.[9][31]  
- **CRBN**:  
  Mentioned as potentially sufficient to cause some typical features when deleted.[5][9]  
- **CAV3, OXTR, SRGAP3**:  
  A 3p25.3–p26.1 interstitial deletion case discussed these genes as candidates for congenital heart defect (CAV3), autistic behavior (OXTR), and mental retardation (SRGAP3).[20]

### Variant types and ACMG classification

- **Type:** Germline **structural deletions** (CNVs), either terminal (3pter) or interstitial (3p25–p26, 3p13–p14).[24][26][34][37][38][40][45]  
- **Classification:** Most are **pathogenic** or **likely pathogenic** based on ACMG CNV criteria (large deletion encompassing dosage‑sensitive genes, de novo occurrence, consistent phenotype).[3][28][31][34]  
- **Somatic vs. germline:** All reported classic 3p‑ syndrome cases involve **constitutional germline deletions**; somatic 3p loss is a separate oncologic context (renal cell carcinoma, etc.). A recent GEMM modeling extensive 3p deletion in kidney cancer patients underscores the role of 3p loss in tumorigenesis but is not a model of 3p‑ developmental syndrome.[33]

### Modifier genes and epigenetics

- Phenotypic variability and non‑penetrance suggest potential **modifier genes** and/or epigenetic influences, but specific modifiers have not been conclusively identified.[34][37][38][40][41]  
- A study entitled “Terminal 3p deletions: phenotypic variability, chromosomal non‑penetrance, or gene modification?” explicitly raises this question but does not identify specific modifiers.[37]  
- No disease‑specific DNA methylation or chromatin changes have been described; epigenetic information for 3p‑ syndrome remains largely unexplored.

### Chromosomal abnormalities

- Classic lesions: **terminal deletions** of 3p25–pter (del(3)(p25‑pter), del(3)(p26.3‑pter)).[30][34][37][38][41][43]  
- Interstitial deletions (e.g., 3p25.3–p26.2; 3p25.3–p26.1; 3p13–p14) produce overlapping but sometimes milder phenotypes.[20][24][26][45]  
- Complex rearrangements: inverted duplication of 3p with adjacent terminal 3p deletion.[29]

---

## 5. Environmental Information

No specific non‑genetic factors are established as causal. Published reports emphasize **chromosomal deletion** as the primary etiology.[5][34][37][38][40][41][43][45]  

- Environmental or lifestyle factors may influence severity of certain complications (e.g., cardiac outcomes) but **do not determine syndrome occurrence**.  
- Infectious agents have not been implicated.

Accordingly, the disease is best classified as a **primary genetic/chromosomal syndrome** with minimal documented environmental contribution.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (inferred from human CNV studies)

1. **Heterozygous terminal/interstitial deletion of distal 3p (3p25–pter) leads to hemizygous loss of multiple neurodevelopmental and organ‑development genes (e.g., SRGAP3, CHL1, CNTN4, CNTN6, CRBN), causing disturbed neuronal connectivity and organ morphogenesis.**[5][9][20][31][32][34][37][38][43][45]  
2. **Gene dosage reduction in SRGAP3 and CHL1 results in impaired axon guidance, synaptic development, and neurodevelopment, leading to intellectual disability, developmental delay, hypotonia, and behavioral abnormalities (autism/OCD); this is inferred from gene function and genotype–phenotype correlation.**[5][20][32][34][40][43]  
3. **Deletion of cardiac developmental genes (e.g., CAV3, possibly others in 3p25.3–p26) leads to congenital heart defects, particularly atrioventricular septal defects and, rarely, hypoplastic left heart syndrome; this is suggested by individual cases and positional candidate gene analyses.**[4][11][20][23][41][42][45]  
4. **Loss of genes involved in craniofacial and skeletal development results in craniofacial dysmorphism (microcephaly, trigonocephaly, telecanthus, ptosis, micrognathia) and limb anomalies (polydactyly, clinodactyly, syndactyly, scoliosis).**[2][23][27][30][31][35][36][39][41][44]  
5. **Deletion of genes involved in renal and gastrointestinal development contributes to structural renal anomalies, intestinal malformations, and hiatal hernia, which in turn lead to feeding difficulties, failure to thrive, and morbidity.**[2][9][23][29][31][44]  
6. **Global developmental impairment and congenital malformations result in chronic functional disability, reduced quality of life, and increased mortality from cardiac, respiratory, and infectious complications; this is inferred from general patterns in severe multisystem CNV syndromes.**[16][18][21][23][31][42]

### Molecular pathways and cellular processes (inferred)

Direct pathway studies specific to 3p‑ syndrome are limited; we extrapolate from known functions of candidate genes:

- **SRGAP3:** Involved in **SLIT‑ROBO signaling**, Rho GTPase regulation, and neuronal migration; its haploinsufficiency disrupts **axon guidance and synaptic development** (GO:0007411 – axon guidance; GO:0048856 – anatomical structure development).[32]  
- **CHL1:** Member of the L1 cell adhesion molecule family, implicated in neurite outgrowth and synaptic plasticity.[5][34]  
- **CNTN4/CNTN6:** GPI‑anchored neuronal adhesion molecules influencing **axon extension, synapse formation and organization of neural circuits** (GO:0007155 – cell adhesion).[9][31]  
- **OXTR:** Oxytocin receptor; deletion may contribute to **social behavior deficits and autistic features** via disrupted neuropeptide signaling.[20][26]

Suggested GO biological process terms (upstream):

- GO:0007399 – nervous system development  
- GO:0007411 – axon guidance  
- GO:0007268 – synaptic transmission  
- GO:0007507 – heart development  
- GO:0001655 – urogenital system development  

Suggested CL (Cell Ontology) terms:

- CL:0000127 – neuron  
- CL:0000182 – cardiac muscle cell  
- CL:0000731 – renal epithelial cell  

No specific metabolomic or proteomic signatures have been published for 3p‑ syndrome; multi‑omics work has focused more on somatic 3p loss in cancer (e.g., clear cell renal cell carcinoma GEMM).[33]

---

## 7. Anatomical Structures Affected

### Organ‑level

Primary involvement:[2][7][9][16][18][21][23][27][31][35][41][42][44]

- **Central nervous system** – intellectual disability, hypotonia, seizures, autism/OCD (UBERON:0000955 – brain).  
- **Craniofacial structures** – skull (microcephaly, trigonocephaly), face, jaw, eyes, ears (UBERON:0008897 – skull; UBERON:0001456 – face; UBERON:0001684 – mandible; UBERON:0000970 – eye; UBERON:0001690 – ear).  
- **Cardiovascular system** – congenital heart defects, especially atrioventricular septal defects and rare hypoplastic left heart (UBERON:0000948 – heart).[23][41][42][45]  
- **Renal/urinary system** – renal anomalies, polycystic renal dysplasia (UBERON:0002113 – kidney).[9][23][31][44]  
- **Gastrointestinal tract** – intestinal malformations, hiatal hernia, umbilical hernia, feeding difficulties (UBERON:0001007 – intestine).[9][23][27][29][31][44]  
- **Musculoskeletal system** – limb anomalies (polydactyly, clinodactyly, syndactyly, scoliosis) (UBERON:0001444 – hand; UBERON:0002429 – vertebral column).[27][31][39]

Secondary involvement includes **respiratory** complications (from cardiac defects or hypotonia) and **endocrine** abnormalities like congenital hypothyroidism in some cases.[31]

### Tissue, cell and subcellular levels

- Predominant impact on **neural tissue** (cortical and subcortical neurons, glia), **cardiac muscle**, **renal epithelium**, and **craniofacial mesenchyme**.  
- Suggested cell types (CL):  
  - CL:0000700 – cortical neuron  
  - CL:0000182 – cardiac muscle cell  
  - CL:0000731 – renal epithelial cell  
- Subcellular: Genes implicated function in **cytoplasm and plasma membrane**, modulating cytoskeleton and signaling (GO:0005886 – plasma membrane; GO:0005856 – cytoskeleton).

Localization patterns are **systemic** rather than localized; lateralization is not a major feature except in specific organ anomalies (e.g., unilateral renal defects).

---

## 8. Temporal Development

### Onset

- **Congenital/pediatric**: Most features are apparent in the neonatal period – low birth weight, craniofacial features, hypotonia, cardiac defects.[2][16][18][21][23][27][31][35][41][42][44]  
- Prenatal detection via ultrasound (growth restriction, cardiac defects) and chromosomal testing is increasingly reported.[29][31]

### Progression and disease course

- **Developmental course**: Chronic, lifelong developmental disability; language and motor skills remain substantially delayed.[16][18][21][31]  
- **Growth**: Slow, with persistent short stature and microcephaly in many patients.[2][23][27][31][34][35][41]  
- **Course pattern**: Generally **non‑relapsing but progressive in functional impact** (as developmental expectations increase) rather than in structural anomalies.  
- No formal staging or remission patterns are described; natural history is derived from case reports and small series.

---

## 9. Inheritance and Population

### Inheritance pattern

- OMIM lists **autosomal dominant** inheritance for 3p‑ syndrome, reflecting that a single copy‑number loss (heterozygous deletion) is sufficient to cause disease.[1][23]  
- Most cases are **de novo**; some are familial with **dominant transmission** and variable expressivity or non‑penetrance.[5][37][38][40][41][43]  

### Penetrance and expressivity

- **Penetrance:** Incomplete – families with terminal 3p26.3 deletions containing only CHL1 have normal or minimally affected individuals.[5][34][37][40]  
  > “Terminal deletions of the distal part of the short arm of chromosome 3 cause a wide range of phenotypes from normal to dysmorphic including microcephaly, developmental delay and intellectual disability.”[40]  
- **Expressivity:** Highly variable; phenotype ranges from normal to severe multi‑system involvement.[34][37][38][40][41]  

No evidence for genetic anticipation, germline mosaicism, or founder effects specific to 3p‑ syndrome has been clearly documented.

### Epidemiology

- Distal 3p‑ syndrome is classified by Orphanet as a **rare disease**; worldwide prevalence is extremely low (exact prevalence estimates are not provided but <1/1,000,000 is plausible given <60 reported cases).[2][4][11][37][42]  
- Sex ratio appears roughly equal based on case series; no strong sex predilection is reported.[27][31][35][37][38]  
- Cases have been reported across diverse ethnicities and geographies (Europe, Asia including Korea, Brazil, etc.), with no obvious geographic clustering.[16][17][22][35][42]

---

## 10. Diagnostics

### Clinical and laboratory evaluation

Diagnosis integrates **clinical dysmorphology** with **cytogenetic and molecular testing**.

#### Clinical features used for suspicion

- Neonatal low birth weight, hypotonia, craniofacial dysmorphia (microcephaly, trigonocephaly, telecanthus, ptosis, micrognathia), polydactyly, and congenital heart defects raise suspicion of distal 3p deletion.[2][23][27][30][31][35][36][39][41][42][44]  
- MedlinePlus emphasizes severe intellectual disability and characteristic craniofacial features.[18][21]

Routine laboratory tests (e.g., electrolyte panels, thyroid function) are supportive, not diagnostic; congenital hypothyroidism has been reported in individual cases.[31]

### Genetic testing

Standard diagnostic approach:[5][16][31][34][37][38][40][41][43][45]

1. **Chromosomal microarray (CMA)**  
   - Detects terminal or interstitial deletions of distal 3p.  
   - Microarray studies have been critical in defining deletion size, gene content, and genotype–phenotype correlations.[5][31][32][34][37][38]  

2. **Karyotyping**  
   - Can identify visible deletions or complex rearrangements (e.g., inverted duplication with adjacent deletion).[29][30][37][38][45]  
   - Early cases (1970s–1990s) relied on conventional karyotyping.[19][30][39][43][45]

3. **Targeted FISH / MLPA**  
   - Used historically to confirm 3p deletions and refine breakpoints, especially before high‑resolution arrays.[43][45]  

4. **Whole exome/genome sequencing**  
   - WES/WGS can detect CNVs but CMA remains first‑line for suspected chromosomal deletion syndromes.  
   - In atypical cases with normal CMA and strong suspicion, WGS may reveal cryptic structural variants.

ClinVar entries note that “clinical presentation may be dependent on the size and location of the deletion,” underscoring the need for precise structural characterization.[28]

### Clinical criteria and differential diagnosis

No formal consensus diagnostic criteria beyond “heterozygous terminal 3p25–pter or overlapping CNV plus consistent phenotype.” Differential diagnoses include other syndromic growth‑retardation and craniofacial dysmorphism disorders:

- **Distal duplication 3p syndrome** (3p trisomy), which presents with overlapping but distinct craniofacial and developmental features.[12]  
- Other microdeletion syndromes (e.g., 1p36 deletion, 22q11.2 deletion, 4p Wolf–Hirschhorn), distinguished by specific facial gestalt, cardiac defect patterns, and different chromosomal loci.

### Screening

Because of rarity and variable expressivity, there are **no population screening programs**. Prenatal CMA or WGS may detect 3p deletions incidentally or in fetuses with anomalies.

---

## 11. Outcome / Prognosis

### Survival and mortality

Published reports suggest that many patients survive into childhood and adolescence, but overall **prognosis depends on severity of cardiac, renal, and neurologic involvement**.[16][17][22][29][31][35][41][42]  

- Hypoplastic left heart and severe atrioventricular septal defects may carry high neonatal mortality.[4][11][42]  
- No systematic 5‑year or 10‑year survival statistics specific to 3p‑ syndrome were found; prognostic data are extrapolated from case series.

### Morbidity, disability, and quality of life

- Severe intellectual disability, language impairment, hypotonia, and congenital anomalies result in **high morbidity and long‑term disability**.[16][18][21][31]  
- Many patients require ongoing multidisciplinary care (cardiology, neurology, nephrology, developmental pediatrics, physical/speech therapy).  
- Behavioral problems (autism, OCD) and seizures further impact daily functioning.[18][20][21][26][31]

Prognostic factors (inferred):

- **Deletion size and gene content** (e.g., inclusion of SRGAP3, CHL1, CAV3, OXTR).[20][32][43][45]  
- **Presence and severity of cardiac defects**.[4][11][23][41][42]  
- **Renal and GI anomalies** and feeding issues.  
- **Family history and non‑penetrant carriers** may indicate milder spectrum.

---

## 12. Treatment

### Overall strategy

There is **no cure or disease‑specific pharmacologic therapy**; management is **supportive and symptom‑based**.[10][16][18][21][31]  

> “There is no cure for 3p deletion syndrome, and management is supportive and symptom-based.”[10]

### Pharmacotherapy and medical management

- **Cardiac management:** Standard pediatric cardiology protocols for atrioventricular septal defects and hypoplastic left heart syndrome (NCIT: C34736 – cardiac surgery; C25746 – congenital heart disease).  
- **Seizure control:** Conventional antiepileptic drugs as indicated (NCIT: C15388 – antiepileptic agent).[18][21][31]  
- **Endocrine management:** Treatment of congenital hypothyroidism when present (e.g., levothyroxine).  
- **Symptom‑directed therapies:** Gastroesophageal reflux management, constipation, infections.

No pharmacogenomic data specific to drug

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 19 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 19 |
| On topic | 15 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 59 |
| Resolved | 57 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 55 |
| Terms named correctly | 33 |
| Terms named as a **different** term | 8 |
| Terms whose name is worth a second look | 14 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001305` (1 mention) - the report calls it "psychomotor delay"; HP calls it **Dandy-Walker malformation**
- `HP:0000263` (1 mention) - the report calls it "Trigonocephaly / brachy‑trigonocephaly"; HP calls it **Oxycephaly**
- `HP:0000107` (1 mention) - the report calls it "Renal anomalies / polycystic renal dysplasia"; HP calls it **Renal cyst**
- `CL:0000127` (1 mention) - the report calls it "neuron"; CL calls it **astrocyte**
- `CL:0000182` (2 mentions) - the report calls it "cardiac muscle cell"; CL calls it **hepatocyte**
- `UBERON:0008897` (1 mention) - the report calls it "skull"; UBERON calls it **fin**
- `UBERON:0001444` (1 mention) - the report calls it "hand"; UBERON calls it **subdivision of head**
- `UBERON:0002429` (1 mention) - the report calls it "vertebral column"; UBERON calls it **cervical lymph node**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001511` (1 mention) - the report calls it "growth delay"; HP calls it **Intrauterine growth retardation**, and lists "Prenatal growth deficiency" among its other names
- `HP:0008897` (1 mention) - the report calls it "intrauterine growth restriction"; HP calls it **Postnatal growth retardation**
- `HP:0001263` (1 mention) - the report calls it "developmental delay"; HP calls it **Global developmental delay**, and lists "Developmental delay" among its other names
- `HP:0002342` (1 mention) - the report calls it "Severe intellectual disability"; HP calls it **Moderate intellectual disability**
- `HP:0000286` (1 mention) - the report calls it "Epicanthal folds"; HP calls it **Epicanthus**, and lists "Epicanthal fold" among its other names
- `HP:0001162` (1 mention) - the report calls it "Postaxial polydactyly"; HP calls it **Postaxial hand polydactyly**
- `HP:0001290` (1 mention) - the report calls it "Hypotonia"; HP calls it **Generalized hypotonia**
- `HP:0000365` (1 mention) - the report calls it "Hearing abnormalities / deafness"; HP calls it **Hearing impairment**, and lists "Hearing defect" among its other names
- `HP:0001671` (1 mention) - the report calls it "atrioventricular septal defect"; HP calls it **Abnormal cardiac septum morphology**, and lists "Heart septal defect" among its other names
- `HP:0004467` (1 mention) - the report calls it "Preauricular pits"; HP calls it **Preauricular pit**, and lists "Preauricular pits" among its other names
- `GO:0007268` (1 mention) - the report calls it "synaptic transmission"; GO calls it **chemical synaptic transmission**, and lists "synaptic transmission" among its other names
- `CL:0000731` (2 mentions) - the report calls it "renal epithelial cell"; CL calls it **urothelial cell**
- `UBERON:0001007` (1 mention) - the report calls it "intestine"; UBERON calls it **digestive system**, and lists "gastrointestinal system" among its other names
- `CL:0000700` (1 mention) - the report calls it "cortical neuron"; CL calls it **dopaminergic neuron**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.